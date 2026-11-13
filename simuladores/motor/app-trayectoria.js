// SPDX-License-Identifier: Apache-2.0
// Simulador de trayectorias entre planetas: gráfico «porkchop», solución de Lambert y vista 3D de la transferencia.
import { cargarSistema } from "./efemerides.js";
import { Vista } from "./vista.js";
import { PLANETAS, SOL, UA_KM, baseDelCuerpo } from "./cuerpos.js";
import { jdTdbDesdeUtc, jdUtcDesdeTdb, jdUtcDesdeInput, formatoUtc, JD_UTC_INICIO, JD_UTC_FIN, valorInputUtc } from "./tiempo.js";
import { porkchop, evaluar, trazaTransferencia, propagar, elementosTransferencia, ORBITAS_PREDETERMINADAS, radiosOrbita } from "./trayectoria.js";
import { barraNavegacion } from "./navegacion.js";

const DIA = 86400;
const fmt = (x, d = 0) => x.toLocaleString("es-CL", { minimumFractionDigits: d, maximumFractionDigits: d });
const CUERPOS = [["199", "Mercurio"], ["299", "Venus"], ["399", "Tierra"], ["499", "Marte"], ["599", "Júpiter"], ["699", "Saturno"], ["799", "Urano"], ["899", "Neptuno"], ["9", "Plutón (baricentro)"], ["2000001", "Ceres"]];
const NOMBRE = Object.fromEntries(CUERPOS);
const PERIODO = { "199": 87.969, "299": 224.701, "399": 365.256, "499": 686.98, "599": 4332.59, "699": 10759.22, "799": 30688.5, "899": 60182, "9": 90560, "2000001": 1680 };
const SEMIEJE = (id) => UA_KM * Math.cbrt((PERIODO[id] / 365.256) ** 2);
const METRICAS = { c3: ["C3 de salida (km²/s²)", (c) => c.c3], dvTotal: ["Δv total (km/s)", (c) => c.dvTotal], vinfLlegada: ["v∞ de llegada (km/s)", (c) => c.vinfLlegada], dvSalida: ["Δv de salida (km/s)", (c) => c.dvSalida], dvLlegada: ["Δv de llegada (km/s)", (c) => c.dvLlegada] };
const PRESETS = [
  ["Tierra → Marte (ventana 2028–2029)", "399", "499", "2028-06-01", "2029-08-01", 150, 450],
  ["Tierra → Marte (ventana 2031)", "399", "499", "2030-09-01", "2031-11-01", 150, 450],
  ["Tierra → Venus (2027–2028)", "399", "299", "2027-06-01", "2028-09-01", 80, 260],
  ["Tierra → Júpiter (2027–2029)", "399", "599", "2027-01-01", "2029-03-01", 500, 1400],
  ["Tierra → Saturno (2027–2029)", "399", "699", "2027-01-01", "2029-03-01", 1000, 2600],
  ["Marte → Tierra (2029–2031)", "499", "399", "2029-06-01", "2031-06-01", 150, 450],
  ["Tierra → Mercurio (2027–2028)", "399", "199", "2027-01-01", "2028-06-01", 60, 260],
];

function colorMapa(t) { // 0..1 -> degradado (azul oscuro → verde → amarillo → rojo)
  const pal = [[16, 24, 90], [24, 104, 170], [32, 168, 138], [168, 204, 64], [246, 210, 60], [232, 110, 46], [150, 24, 24]];
  const x = Math.max(0, Math.min(0.9999, t)) * (pal.length - 1), i = Math.floor(x), f = x - i;
  return pal[i].map((v, k) => Math.round(v + (pal[i + 1][k] - v) * f));
}
function elipseOsc(r, v, mu, N = 200) {
  const rn = Math.hypot(...r), v2 = v[0] ** 2 + v[1] ** 2 + v[2] ** 2, rv = r[0] * v[0] + r[1] * v[1] + r[2] * v[2];
  const h = [r[1] * v[2] - r[2] * v[1], r[2] * v[0] - r[0] * v[2], r[0] * v[1] - r[1] * v[0]], e = [0, 1, 2].map((k) => ((v2 - mu / rn) * r[k] - rv * v[k]) / mu);
  const en = Math.hypot(...e), hn = Math.hypot(...h), p = hn * hn / mu;
  if (en >= 0.99) return null;
  const ex = en > 1e-9 ? e.map((x) => x / en) : r.map((x) => x / rn), hh = h.map((x) => x / hn), q = [hh[1] * ex[2] - hh[2] * ex[1], hh[2] * ex[0] - hh[0] * ex[2], hh[0] * ex[1] - hh[1] * ex[0]];
  const out = new Float64Array((N + 1) * 3);
  for (let i = 0; i <= N; i++) { const nu = i / N * 2 * Math.PI, rr = p / (1 + en * Math.cos(nu)); for (let k = 0; k < 3; k++) out[i * 3 + k] = rr * (Math.cos(nu) * ex[k] + Math.sin(nu) * q[k]); }
  return out;
}

export async function iniciarTrayectorias() {
  const raiz = document.getElementById("app");
  const cab = document.createElement("header"); cab.className = "cabecera"; cab.innerHTML = "<h1>Trayectorias entre planetas</h1>"; cab.appendChild(barraNavegacion("trayectorias")); document.body.insertBefore(cab, raiz);
  raiz.className = "app";
  raiz.innerHTML = `
    <section class="escena" style="display:grid;grid-template-rows:minmax(260px,52%) 1fr" aria-label="Gráfico porkchop y trayectoria">
      <div style="position:relative;border-bottom:1px solid var(--borde)"><canvas id="pork" tabindex="0" aria-label="Gráfico porkchop: fecha de salida en horizontal, fecha de llegada en vertical, el color es el costo. Haga clic para elegir una transferencia."></canvas>
        <div class="hud"><div class="fecha" id="titulo" style="font-size:1rem"></div><div class="sub" id="leyenda"></div></div>
        <div class="cargando" id="cargando"><div>Cargando efemérides de JPL…</div><progress id="prog" max="1" value="0"></progress></div></div>
      <div style="position:relative"><div id="escena3d" style="position:absolute;inset:0"><canvas id="lienzo3d" aria-label="Trayectoria de la nave en el Sistema Solar, vista desde el polo norte eclíptico. Arrastre para girar."></canvas></div>
        <div class="hud"><div class="fecha" id="fecha3d" style="font-size:1rem"></div><div class="sub" id="sub3d"></div></div>
        <div class="barra"><div class="grupo"><button id="bPlay" aria-label="Reproducir el viaje">▶</button><label class="etq" for="rango">Instante del viaje</label><input type="range" id="rango" min="0" max="1000" value="0" style="width:min(420px,50vw)"></div>
        <div class="grupo"><label class="chk"><input type="checkbox" id="cOrb" checked> Órbitas planetarias</label></div></div></div>
    </section>
    <aside class="lateral" aria-label="Controles y resultados">
      <h2>Transferencia</h2>
      <label class="etq" for="sPre">Ejemplos </label><select id="sPre"></select>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px"><label class="etq">Desde <select id="sDe"></select></label><label class="etq">Hacia <select id="sHa"></select></label>
        <label class="etq">Salida desde <input type="date" id="dIni" min="2027-01-01" max="2050-12-31"></label><label class="etq">Salida hasta <input type="date" id="dFin" min="2027-01-01" max="2050-12-31"></label>
        <label class="etq">Vuelo mín. (d) <input type="number" id="tMin" min="20" max="6000" step="10" style="width:100%"></label><label class="etq">Vuelo máx. (d) <input type="number" id="tMax" min="30" max="9000" step="10" style="width:100%"></label>
        <label class="etq">Resolución <select id="sRes"><option value="80">80 × 80</option><option value="120" selected>120 × 120</option><option value="180">180 × 180</option></select></label>
        <label class="etq">Mostrar <select id="sMet"></select></label></div>
      <h2>Órbitas en los planetas</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px"><label class="etq">Salida: altitud (km) <input type="number" id="aSal" min="0" step="10" style="width:100%"></label><span></span>
        <label class="etq">Llegada: periapsis (km) <input type="number" id="aPer" min="0" step="10" style="width:100%"></label><label class="etq">Llegada: apoapsis (km) <input type="number" id="aApo" min="0" step="10" style="width:100%"></label></div>
      <p class="aviso">Altitudes sobre el radio ecuatorial. Salida y llegada son órbitas en torno a los planetas; con apoapsis = periapsis la captura es a órbita circular.</p>
      <button id="bCalc" style="margin-top:6px">Calcular</button> <progress id="progCalc" max="1" value="0" style="width:120px;vertical-align:middle"></progress>
      <h2>Transferencia elegida</h2><div class="ficha" id="res" aria-live="polite"></div>
      <details><summary>Modelo, datos y límites</summary><div class="aviso" id="meta">Cónicas empalmadas: la nave sólo siente la gravedad del Sol (problema de Lambert, sin vueltas completas, sentido directo) y se compara con la velocidad real del planeta (efemérides de JPL) para obtener v∞; el planeta se trata como esfera de influencia puntual. Sin asistencias gravitatorias, empuje continuo, perturbaciones ni margen de maniobra. <strong>Es una herramienta didáctica, no de diseño de misiones.</strong> Tiempos en TDB mostrados en UTC.</div></details>
      <p class="aviso">Documentación: <a href="documentacion/README.html">documentación de los simuladores</a>.</p>
    </aside>`;
  const $ = (i) => document.getElementById(i);
  let sol;
  try { sol = await cargarSistema("sol", "datos", (f) => { $("prog").value = f; }); } catch (e) { $("cargando").classList.add("error"); $("cargando").innerHTML = `<div><strong>No se pudieron cargar las efemérides.</strong></div><div>${e.message}</div><small>Abra el sitio publicado en GitHub Pages o sirva la carpeta con <code>python -m http.server</code>.</small>`; return; }
  $("cargando").remove();
  $("sDe").innerHTML = $("sHa").innerHTML = CUERPOS.map(([i, n]) => `<option value="${i}">${n}</option>`).join("");
  $("sMet").innerHTML = Object.entries(METRICAS).map(([k, [n]]) => `<option value="${k}">${n}</option>`).join("");
  $("sPre").innerHTML = PRESETS.map((p, i) => `<option value="${i}">${p[0]}</option>`).join("");

  // ---------------------------------------------------------------- escena 3D
  const vista = new Vista($("lienzo3d"), { dist: 5e8, limites: { min: 1e6, max: 2e10 } });
  vista.cam.pitch = 1.25; vista.cam.yaw = -1.2; vista.mostrarEtiquetas = true;
  const solObj = vista.añadir({ id: "10", nombre: "Sol", radio: SOL.radio, color: SOL.color, autoluminoso: true, textura: "sol", prioridad: 1000, ampliable: false, base: baseDelCuerpo(SOL.polo, 2461406.5), noSeleccionable: true });
  vista.sol = solObj; vista.sol.ocultarFlecha = true; vista.seguir = solObj; vista.ampliacion = 1;
  const objs = {};
  for (const [id, nom] of CUERPOS) { const f = PLANETAS[id]; objs[id] = vista.añadir({ id, nombre: nom.replace(" (baricentro)", ""), radio: f.radio, color: f.color, prioridad: 100, ampliable: false, noSeleccionable: true, ocultarOrbita: false, colorOrbita: "rgba(120,150,200,0.28)" }); }
  const nave = vista.añadir({ id: "nave", nombre: "Nave", radio: 0, color: "#ffe08a", prioridad: 900, ampliable: false, noSeleccionable: true, colorOrbita: "rgba(255,224,138,0.95)" });
  const trazadoPorOrigen = {};
  let ev = null, grid = null, sel = null, t01 = 0, jugando = false;
  vista.etiquetaExtra = null;

  function actualizar3D() {
    if (!ev) return;
    const jd = ev.jdSalida + (ev.jdLlegada - ev.jdSalida) * t01;
    for (const [id] of CUERPOS) sol.cuerpo(id).pos(jd, objs[id].pos);
    const p = propagar(ev.r1, ev.v1, (jd - ev.jdSalida) * DIA); nave.pos[0] = p.r[0]; nave.pos[1] = p.r[1]; nave.pos[2] = p.r[2];
    $("fecha3d").textContent = formatoUtc(jdUtcDesdeTdb(jd), false);
    $("sub3d").textContent = `día ${fmt((jd - ev.jdSalida), 0)} de ${fmt(ev.tof_d, 0)} · distancia al Sol ${fmt(Math.hypot(...p.r) / UA_KM, 3)} UA · velocidad ${fmt(Math.hypot(...p.v), 2)} km/s`;
  }
  function configurarOrbitas() {
    for (const [id] of CUERPOS) {
      const o = objs[id], t = sol.cuerpo(id), jd = ev ? ev.jdSalida : jdTdbDesdeUtc(JD_UTC_INICIO);
      const el = elipseOsc(t.pos(jd), t.vel(jd), SOL.gm + (PLANETAS[id].gm || 0));
      o.orbita = el && $("cOrb").checked ? el : null; o.ocultarOrbita = !$("cOrb").checked;
    }
  }
  $("cOrb").onchange = configurarOrbitas;
  const ajustarCamara = () => { const a = Math.max(SEMIEJE($("sDe").value), SEMIEJE($("sHa").value)); vista.cam.distObj = Math.max(3e7, 3.4 * a); };

  // ---------------------------------------------------------------- porkchop
  const cv = $("pork"), cx = cv.getContext("2d");
  const M = { l: 70, r: 22, t: 52, b: 52 };
  function dibujarPork() {
    const p = cv.parentElement, dpr = Math.min(2, devicePixelRatio || 1), W = p.clientWidth, H = p.clientHeight;
    if (cv.width !== W * dpr || cv.height !== H * dpr) { cv.width = W * dpr; cv.height = H * dpr; cv.style.width = W + "px"; cv.style.height = H + "px"; }
    cx.setTransform(dpr, 0, 0, dpr, 0, 0); cx.fillStyle = "#0b1020"; cx.fillRect(0, 0, W, H);
    if (!grid) return;
    const met = METRICAS[$("sMet").value][1];
    const vals = grid.celdas.filter(Boolean).map(met).filter(isFinite).sort((a, b) => a - b);
    if (!vals.length) { cx.fillStyle = "#9fb0cf"; cx.font = "14px system-ui"; cx.fillText("Sin soluciones para estos tiempos de vuelo.", M.l, H / 2); return; }
    const vmin = vals[0], vmax = Math.min(vals[vals.length - 1], vmin * 3 + 1, vals[Math.floor(vals.length * 0.9)]);
    const x0 = grid.fechas[0], x1 = grid.fechas[grid.nSalida - 1], y0 = x0 + grid.tofs[0], y1 = x1 + grid.tofs[grid.nTof - 1];
    const X = (jd) => M.l + (jd - x0) / (x1 - x0) * (W - M.l - M.r), Y = (jd) => H - M.b - (jd - y0) / (y1 - y0) * (H - M.t - M.b);
    const nBandas = 16;
    for (let i = 0; i < grid.nSalida - 1; i++) for (let j = 0; j < grid.nTof - 1; j++) {
      const c = grid.celdas[i * grid.nTof + j]; if (!c) continue; const v = met(c); if (!isFinite(v) || v > vmax) continue;
      const t = Math.floor((v - vmin) / (vmax - vmin) * nBandas) / nBandas, col = colorMapa(t);
      const xa = X(grid.fechas[i]), xb = X(grid.fechas[i + 1]);
      cx.fillStyle = `rgb(${col.join(",")})`; cx.beginPath(); cx.moveTo(xa, Y(grid.fechas[i] + grid.tofs[j])); cx.lineTo(xb, Y(grid.fechas[i + 1] + grid.tofs[j])); cx.lineTo(xb, Y(grid.fechas[i + 1] + grid.tofs[j + 1])); cx.lineTo(xa, Y(grid.fechas[i] + grid.tofs[j + 1])); cx.closePath(); cx.fill();
    }
    // ejes
    cx.strokeStyle = "#26314f"; cx.fillStyle = "#9fb0cf"; cx.font = "11px system-ui"; cx.lineWidth = 1;
    const marcas = (a, b) => { const o = []; const d = new Date((a - 2440587.5) * 86400000), fin = (b - 2440587.5) * 86400000; const meses = (b - a) / 30.4 > 36 ? 12 : (b - a) / 30.4 > 14 ? 3 : 1; let y = d.getUTCFullYear(), m = Math.floor(d.getUTCMonth() / meses) * meses; for (let k = 0; k < 400; k++) { const ms = Date.UTC(y, m, 1); if (ms > fin) break; if (ms >= d.getTime()) o.push(ms / 86400000 + 2440587.5); m += meses; if (m >= 12) { y += Math.floor(m / 12); m %= 12; } } return o; };
    const et = (jd) => { const d = new Date((jd - 2440587.5) * 86400000); return `${d.getUTCFullYear()}-${String(d.getUTCMonth() + 1).padStart(2, "0")}`; };
    for (const m of marcas(x0, x1)) { const x = X(m); cx.beginPath(); cx.moveTo(x, H - M.b); cx.lineTo(x, H - M.b + 5); cx.stroke(); cx.save(); cx.translate(x, H - M.b + 8); cx.rotate(0.5); cx.fillText(et(m), 0, 8); cx.restore(); }
    for (const m of marcas(y0, y1)) { const y = Y(m); cx.beginPath(); cx.moveTo(M.l - 5, y); cx.lineTo(M.l, y); cx.stroke(); cx.fillText(et(m), 6, y + 3); }
    cx.strokeRect(M.l, M.t, W - M.l - M.r, H - M.t - M.b);
    cx.fillStyle = "#e6ecf8"; cx.font = "12px system-ui"; cx.fillText("Fecha de salida (UTC) →", M.l + (W - M.l - M.r) / 2 - 60, H - 6);
    cx.save(); cx.translate(14, M.t + (H - M.t - M.b) / 2 + 60); cx.rotate(-Math.PI / 2); cx.fillText("Fecha de llegada (UTC) →", 0, 0); cx.restore();
    // leyenda
    for (let k = 0; k < 120; k++) { const c = colorMapa(Math.floor(k / 120 * nBandas) / nBandas); cx.fillStyle = `rgb(${c.join(",")})`; cx.fillRect(W - M.r - 220 + k * 1.8, 20, 2, 10); }
    cx.fillStyle = "#e6ecf8"; cx.fillText(fmt(vmin, 1), W - M.r - 224, 42); cx.textAlign = "end"; cx.fillText(fmt(vmax, 1) + "+", W - M.r, 42); cx.textAlign = "start";
    // óptimo y selección
    const mejor = grid.celdas.filter(Boolean).reduce((a, c) => (met(c) < met(a) ? c : a));
    const marcar = (c, color, r) => { cx.strokeStyle = color; cx.lineWidth = 2; cx.beginPath(); cx.arc(X(c.jdSalida), Y(c.jdLlegada), r, 0, 7); cx.stroke(); };
    marcar(mejor, "#ffffff", 7); if (sel) marcar(sel, "#ffe08a", 10);
    cv._geo = { X, Y, x0, x1, y0, y1, W, H, mejor };
    $("titulo").textContent = `${NOMBRE[$("sDe").value]} → ${NOMBRE[$("sHa").value]} · ${METRICAS[$("sMet").value][0]}`;
    $("leyenda").textContent = `mínimo ${fmt(vmin, 2)} (círculo blanco): salida ${formatoUtc(jdUtcDesdeTdb(mejor.jdSalida), false).slice(0, 10)}, vuelo ${fmt(mejor.tof_d, 0)} d`;
  }
  cv.addEventListener("click", (e) => {
    if (!grid || !cv._geo) return; const r = cv.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top, g = cv._geo;
    const jdS = g.x0 + (x - M.l) / (g.W - M.l - M.r) * (g.x1 - g.x0), jdL = g.y0 + (g.H - M.b - y) / (g.H - M.t - M.b) * (g.y1 - g.y0);
    const orbs = leerOrbitas(); const c = evaluar(sol, $("sDe").value, $("sHa").value, jdS, jdL, orbs);
    if (c) elegir(c);
  });
  function leerOrbitas() {
    const de = $("sDe").value, ha = $("sHa").value, Rd = PLANETAS[de].radio, Rh = PLANETAS[ha].radio;
    return { salida: { alt: Math.max(0, +$("aSal").value) }, llegada: { alt: Math.max(0, +$("aPer").value), altApo: Math.max(+$("aPer").value, +$("aApo").value) } };
  }
  function elegir(c) {
    sel = c; ev = c; t01 = 0; $("rango").value = 0; configurarOrbitas();
    nave.orbita = trazaTransferencia(c); nave.ocultarOrbita = false;
    const el = elementosTransferencia(c.r1, c.v1), de = $("sDe").value, ha = $("sHa").value;
    const a1 = SEMIEJE(de), a2 = SEMIEJE(ha), mu = SOL.gm, aH = (a1 + a2) / 2, tH = Math.PI * Math.sqrt(aH ** 3 / mu) / DIA;
    const hv1 = Math.sqrt(mu / a1) * (Math.sqrt(2 * a2 / (a1 + a2)) - 1);
    const ang = Math.acos(Math.max(-1, Math.min(1, (c.r1[0] * c.r2[0] + c.r1[1] * c.r2[1] + c.r1[2] * c.r2[2]) / (Math.hypot(...c.r1) * Math.hypot(...c.r2))))) * 180 / Math.PI;
    const filas = [["Salida (UTC)", formatoUtc(jdUtcDesdeTdb(c.jdSalida), false)], ["Llegada (UTC)", formatoUtc(jdUtcDesdeTdb(c.jdLlegada), false)], ["Tiempo de vuelo", `${fmt(c.tof_d, 1)} d (${fmt(c.tof_d / 30.44, 1)} meses)`],
      ["C3 de salida", `${fmt(c.c3, 2)} km²/s²`], ["v∞ de salida · llegada", `${fmt(c.vinfSalida, 2)} · ${fmt(c.vinfLlegada, 2)} km/s`], ["Δv de salida (desde la órbita)", `${fmt(c.dvSalida, 2)} km/s`], ["Δv de llegada (captura)", `${fmt(c.dvLlegada, 2)} km/s`], ["Δv total", `${fmt(c.dvTotal, 2)} km/s`],
      ["Perihelio · afelio de la nave", `${fmt(el.perihelio / UA_KM, 3)} · ${fmt(el.afelio / UA_KM, 3)} UA`], ["Excentricidad · inclinación", `${fmt(el.e, 3)} · ${fmt(el.i, 2)}°`], ["Ángulo de transferencia", `${fmt(ang, 0)}°`],
      ["Referencia de Hohmann (circular y coplanar)", `Δv₁ ${fmt(Math.abs(hv1), 2)} km/s · ${fmt(tH, 0)} d`]];
    $("res").innerHTML = `<dl class="datos">${filas.map(([k, v]) => `<dt>${k}</dt><dd>${v}</dd>`).join("")}</dl>`;
    ajustarCamara(); actualizar3D(); dibujarPork();
  }

  // ---------------------------------------------------------------- cálculo
  let token = 0;
  function ajustarVentana(de, ha) { // valores razonables según los periodos
    const sin = Math.abs(1 / (1 / PERIODO[de] - 1 / PERIODO[ha])), a = (SEMIEJE(de) + SEMIEJE(ha)) / 2, tH = Math.PI * Math.sqrt(a ** 3 / SOL.gm) / DIA;
    return { sin, tMin: Math.round(tH * 0.55 / 10) * 10, tMax: Math.round(tH * 1.8 / 10) * 10 };
  }
  function predeterminarOrbitas() {
    const de = $("sDe").value, ha = $("sHa").value, o1 = radiosOrbita(de, ORBITAS_PREDETERMINADAS[de]), o2 = radiosOrbita(ha, ORBITAS_PREDETERMINADAS[ha]);
    $("aSal").value = Math.round(o1.rp - PLANETAS[de].radio); $("aPer").value = Math.round(o2.rp - PLANETAS[ha].radio); $("aApo").value = Math.round(o2.ra - PLANETAS[ha].radio);
  }
  function calcular() {
    const mi = ++token, de = $("sDe").value, ha = $("sHa").value;
    if (de === ha) { $("res").textContent = "Elija planetas distintos."; return; }
    const ini = jdTdbDesdeUtc(jdUtcDesdeInput($("dIni").value + "T00:00")), fin = jdTdbDesdeUtc(jdUtcDesdeInput($("dFin").value + "T00:00")), n = +$("sRes").value;
    if (!(fin > ini)) { $("res").textContent = "La fecha final debe ser posterior a la inicial."; return; }
    const orbitas = leerOrbitas(), par = { jdIni: ini, jdFin: fin, nSalida: n, tofMin: +$("tMin").value, tofMax: Math.max(+$("tMax").value, +$("tMin").value + 10), nTof: n, orbitas };
    const celdas = new Array(par.nSalida * par.nTof).fill(null), fechas = [], tofs = [];
    for (let i = 0; i < n; i++) fechas.push(ini + (fin - ini) * i / (n - 1)); for (let j = 0; j < n; j++) tofs.push(par.tofMin + (par.tofMax - par.tofMin) * j / (n - 1));
    grid = { fechas, tofs, celdas, nSalida: n, nTof: n }; let i = 0;
    const paso = () => {
      if (mi !== token) return;
      const lim = Math.min(n, i + 6);
      for (; i < lim; i++) for (let j = 0; j < n; j++) celdas[i * n + j] = evaluar(sol, de, ha, fechas[i], fechas[i] + tofs[j], orbitas);
      $("progCalc").value = i / n; dibujarPork();
      if (i < n) setTimeout(paso, 0);
      else { const met = METRICAS[$("sMet").value][1], ok = celdas.filter(Boolean); if (ok.length) elegir(ok.reduce((a, c) => (met(c) < met(a) ? c : a))); }
    };
    sel = null; paso();
  }
  function aplicarEjemplo(i) {
    const p = PRESETS[i]; $("sDe").value = p[1]; $("sHa").value = p[2]; $("dIni").value = p[3]; $("dFin").value = p[4]; $("tMin").value = p[5]; $("tMax").value = p[6]; predeterminarOrbitas(); calcular();
  }
  $("sPre").onchange = () => aplicarEjemplo(+$("sPre").value);
  const alCambiarPlanetas = () => { const w = ajustarVentana($("sDe").value, $("sHa").value); $("tMin").value = w.tMin; $("tMax").value = w.tMax; $("dIni").value = "2027-01-01"; $("dFin").value = formatoUtc(jdUtcDesdeInput("2027-01-01T00:00") + Math.min(3600, w.sin * 1.05)).slice(0, 10); predeterminarOrbitas(); };
  $("sDe").onchange = alCambiarPlanetas; $("sHa").onchange = alCambiarPlanetas;
  $("bCalc").onclick = calcular; $("sMet").onchange = dibujarPork;
  $("rango").oninput = () => { t01 = +$("rango").value / 1000; actualizar3D(); };
  $("bPlay").onclick = () => { jugando = !jugando; $("bPlay").textContent = jugando ? "⏸" : "▶"; if (jugando && t01 >= 1) t01 = 0; };
  new ResizeObserver(dibujarPork).observe(cv.parentElement);
  aplicarEjemplo(0);

  let ult = 0;
  (function cuadro(t) {
    if (jugando && ev) { t01 = Math.min(1, t01 + (t - (ult || t)) / 1000 / 14); $("rango").value = Math.round(t01 * 1000); if (t01 >= 1) { jugando = false; $("bPlay").textContent = "▶"; } }
    ult = t; for (const [id] of CUERPOS) objs[id].radio = vista.cam.dist * 0.007; solObj.radio = vista.cam.dist * 0.004; actualizar3D(); vista.dibujar(ev ? ev.jdSalida : 0); requestAnimationFrame(cuadro);
  })(0);
  window.__tray = { sol, vista, get ev() { return ev; }, calcular };
}
