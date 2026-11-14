// SPDX-License-Identifier: Apache-2.0
// Simulador de misiones espaciales: se elige una misión en una lista, se pulsa ▶ y se ve su trayectoria real entre los planetas, sus encuentros
// (sobrevuelos, asistencias gravitatorias, inserciones en órbita) con la ganancia de velocidad y el detalle del encuentro respecto del planeta.
import { cargarSistema } from "./efemerides.js";
import { UA_KM, C_KM_S } from "./cuerpos.js";
import { jdTdbDesdeUtc, jdUtcDesdeTdb, formatoUtc, jdUtcDesdeInput } from "./tiempo.js";
import { MISIONES, GRUPOS, NOMBRE_PLANETA, COLOR_PLANETA, crearNave, posicionPlanetocentrica } from "./misiones.js";
import { barraNavegacion } from "./navegacion.js";

const fmt = (x, d = 0) => x.toLocaleString("es-CL", { minimumFractionDigits: d, maximumFractionDigits: d });
const signo = (x, d = 1) => (x >= 0 ? "+" : "−") + fmt(Math.abs(x), d);
const VEL = [["1 hora / s", 3600], ["1 día / s", 86400], ["10 días / s", 864000], ["30 días / s", 2592000], ["1 año / s", 31557600], ["3 años / s", 94672800]];
const PLAN = ["199", "299", "399", "499", "599", "699", "799", "899", "9"];
const SEMIEJE = { "199": 0.387, "299": 0.723, "399": 1, "499": 1.524, "599": 5.203, "699": 9.537, "799": 19.19, "899": 30.07, "9": 39.5 };
const MU_SOL = 132712440041.94;
const JD_HOY = jdTdbDesdeUtc(jdUtcDesdeInput("2026-11-14T00:00")), JD_TOPE = 2470172.5;
const fechaCorta = (jdTdb) => formatoUtc(jdUtcDesdeTdb(jdTdb), false).slice(0, 10);

export async function iniciarMisiones() {
  const raiz = document.getElementById("app");
  const cab = document.createElement("header"); cab.className = "cabecera"; cab.innerHTML = "<h1>Misiones espaciales</h1>"; cab.appendChild(barraNavegacion("misiones")); document.body.insertBefore(cab, raiz);
  raiz.className = "app";
  raiz.innerHTML = `
    <section class="escena" aria-label="Trayectoria de la misión" style="display:flex;flex-direction:column">
      <div style="flex:0 0 auto;display:flex;gap:10px;align-items:center;padding:8px 12px;background:var(--panel);border-bottom:1px solid var(--borde)"><label class="etq" for="sMision" style="font-weight:650;color:var(--acento)">Misión</label><select id="sMision" aria-label="Elegir misión" style="flex:1 1 auto;min-width:0;max-width:360px"></select></div>
      <div style="position:relative;flex:1 1 auto;min-height:0"><canvas id="mapa" tabindex="0" style="position:absolute;inset:0;width:100%;height:100%" aria-label="Mapa del Sistema Solar visto desde el polo norte eclíptico con la trayectoria de la nave, los planetas y los encuentros. Clic en un encuentro para ver su detalle."></canvas>
        <div class="hud"><div class="fecha" id="fecha"></div><div class="sub" id="sub"></div></div>
        <div class="cargando" id="cargando"><div>Cargando trayectorias y encuentros de JPL…</div><progress id="prog" max="1" value="0"></progress></div></div>
      <div style="position:relative;flex:0 0 150px;border-top:1px solid var(--borde)"><canvas id="veloc" style="position:absolute;inset:0;width:100%;height:100%;cursor:pointer" aria-label="Velocidad de la nave respecto del Sol a lo largo de la misión, con los encuentros marcados. Clic para ir a esa fecha."></canvas></div>
      <div class="barra" style="position:relative;flex:0 0 auto;border-top:1px solid var(--borde)"><div class="grupo" role="group" aria-label="Control del tiempo">
          <button id="bIni" aria-label="Ir al lanzamiento" title="Lanzamiento">⏮</button><button id="bAnt" aria-label="Encuentro anterior" title="Encuentro anterior">⏪</button>
          <button id="bPlay" aria-label="Reproducir" title="Reproducir / pausar (espacio)" style="min-width:48px">▶</button>
          <button id="bSig" aria-label="Siguiente encuentro" title="Siguiente encuentro">⏩</button><button id="bFin" aria-label="Ir al final" title="Final de los datos">⏭</button></div>
        <div class="grupo"><label class="etq" for="sVel">Velocidad</label><select id="sVel"></select></div>
        <div class="grupo"><label class="chk" title="Reduce la velocidad al acercarse a cada planeta para ver el encuentro"><input type="checkbox" id="cLenta" checked> Cámara lenta en los encuentros</label>
          <label class="chk" title="Sin comprimir las distancias: las proporciones son reales"><input type="checkbox" id="cLineal"> Escala lineal</label></div></div>
    </section>
    <aside class="lateral" aria-label="Misión y datos">
      <div class="ficha" id="ficha" aria-live="polite"></div>
      <h2>Estado</h2><dl class="datos" id="estado"></dl>
      <h2>Encuentros con planetas</h2><div class="lista" id="eventos" style="max-height:200px"></div>
      <h2>Detalle del encuentro</h2><canvas id="detalle" style="width:100%;height:250px;background:#02030a;border:1px solid var(--borde);border-radius:8px" aria-label="Trayectoria de la nave respecto del planeta en el encuentro seleccionado, con el planeta a escala."></canvas>
      <div class="aviso" id="detalleTxt" aria-live="polite"></div>
      <details><summary>Datos, modelo y límites</summary><div class="aviso" id="meta"></div></details>
      <p class="aviso">Documentación: <a href="documentacion/README.html">documentación de los simuladores</a>.</p>
    </aside>`;
  const $ = (i) => document.getElementById(i);
  let planHist, nav, EN;
  try { const p = [0, 0, 0], pr = () => { $("prog").value = (p[0] + p[1] + p[2]) / 3; };
    [planHist, nav, EN] = await Promise.all([cargarSistema("planetas_hist", "datos", (f) => { p[0] = f; pr(); }), cargarSistema("misiones", "datos", (f) => { p[1] = f; pr(); }), fetch("datos/encuentros.json").then((r) => { if (!r.ok) throw new Error("encuentros.json " + r.status); return r.json(); }).then((j) => { p[2] = 1; pr(); return j; })]); }
  catch (e) { $("cargando").classList.add("error"); $("cargando").innerHTML = `<div><strong>No se pudieron cargar los datos.</strong></div><div>${e.message}</div><small>Abra el sitio publicado en GitHub Pages o sirva la carpeta con <code>python -m http.server</code>.</small>`; return; }
  $("cargando").remove();
  const planetas = new Map(PLAN.map((id) => [id, planHist.cuerpo(id)]));
  for (const e of EN.encuentros) e.radio = EN.radio_km[e.planeta];

  let m = null, jd = 0, jugando = false, velocidad = 86400, sel = -1, vp = null, tprev = 0, rfit = 2, rvista = 2, mapaGeom = null, dtFrame = 0;
  const tmp = [0, 0, 0], tmp2 = [0, 0, 0];

  // ---------- selección de la misión
  $("sMision").innerHTML = GRUPOS.map((g, k) => `<optgroup label="${g}">` + Object.entries(MISIONES).filter(([id, d]) => d.grupo === k && nav.cuerpos.has(id)).sort((a, b) => a[1].anio - b[1].anio).map(([id, d]) => `<option value="${id}">${d.nombre} (${d.anio})</option>`).join("") + "</optgroup>").join("");
  function elegir(id) {
    const d = MISIONES[id], t = nav.cuerpo(id), nave = crearNave(id, t, EN.encuentros, planetas);
    const fin = Math.min(nave.fin, JD_TOPE, d.fin ? jdTdbDesdeUtc(jdUtcDesdeInput(d.fin + "T00:00")) : Infinity);
    const encs = nave.encuentros.filter((e) => e.jd_ca <= fin);
    const hitos = (d.hitos || []).map(([nom, f, au]) => ({ hito: true, nombre: nom, jd_ca: jdTdbDesdeUtc(jdUtcDesdeInput(f + "T00:00")), au }));
    const lista = encs.map((e) => ({ e, jd: e.jd_ca })).concat(hitos.map((h) => ({ h, jd: h.jd_ca }))).sort((a, b) => a.jd - b.jd);
    m = { id, d, nave, ini: nave.ini, fin, encs, lista };
    // trayectoria completa (1 000 puntos) y velocidad heliocéntrica
    const N = 1000; m.camino = new Float64Array((N + 1) * 3); m.vh = new Float64Array(N + 1); m.vesc = new Float64Array(N + 1); let rmax = 0;
    // en órbita alrededor de un planeta la velocidad oscila en pocos días: se promedia
    const orb = encs.find((e) => e.orbita), jOrb = orb ? orb.jd_ca : Infinity;
    for (let k = 0; k <= N; k++) { const j = m.ini + (m.fin - m.ini) * k / N; nave.pos(j, tmp); nave.vel(j, tmp2); m.camino.set(tmp, k * 3); m.vh[k] = Math.hypot(...tmp2);
      if (j > jOrb + 5) { let acum = 0; const M = 36, w = (m.fin - m.ini) / N; for (let q = 0; q < M; q++) { nave.vel(j + (q / M - 0.5) * w, tmp2); acum += Math.hypot(...tmp2); } m.vh[k] = acum / M; } const r = Math.hypot(...tmp); m.vesc[k] = Math.sqrt(2 * MU_SOL / r); rmax = Math.max(rmax, r / UA_KM); }
    m.vmax = Math.max(...m.vh) * 1.12; rfit = Math.max(1.3, rmax * 1.08); m.rcum = new Float64Array(N + 1); for (let k = 0, r = 0; k <= N; k++) { r = Math.max(r, Math.hypot(m.camino[k * 3], m.camino[k * 3 + 1], m.camino[k * 3 + 2]) / UA_KM); m.rcum[k] = r; } rvista = Math.max(1.3, m.rcum[0] * 1.2);
    $("sMision").value = id; jd = m.ini; vp = null;
    const gan = encs.filter((e) => !e.orbita && e.dv_helio > 0.3).length;
    $("ficha").innerHTML = `<h3 style="color:${d.color}">${d.nombre}</h3><p style="margin:4px 0">${d.resumen}</p><dl class="datos"><dt>Lanzamiento</dt><dd>${fechaCorta(m.ini)}</dd><dt>Datos hasta</dt><dd>${fechaCorta(m.fin)}</dd><dt>Encuentros con planetas</dt><dd>${encs.length}${gan ? ` · ${gan} con ganancia de velocidad` : ""}</dd></dl>`;
    $("eventos").innerHTML = lista.map((x, i) => {
      if (x.h) return `<button data-i="${i}"><span>${fechaCorta(x.jd)} · <b>${x.h.nombre}</b></span><small>${fmt(x.h.au, 0)} UA</small></button>`;
      const e = x.e, planeta = NOMBRE_PLANETA[e.planeta], acc = e.orbita ? "inserción en órbita" : e.dv_helio > 0.3 ? `<span style="color:#7ee0a1">▲ ${signo(e.dv_helio)} km/s</span>` : e.dv_helio < -0.3 ? `<span style="color:#ff8a8a">▼ ${signo(e.dv_helio)} km/s</span>` : "desvío";
      return `<button data-i="${i}"><span><span style="color:${COLOR_PLANETA[e.planeta]}">●</span> ${fechaCorta(e.jd_ca)} · ${planeta}</span><small>${acc} · ${fmt(e.alt_km, 0)} km</small></button>`;
    }).join("") || "<div class='aviso' style='padding:8px'>Sin encuentros con planetas (la nave no se acerca a ninguno).</div>";
    const primero = lista.find((x) => x.e); seleccionarEncuentro(primero ? primero.e : null);
    history.replaceState(null, "", `#m=${id}`); dibujarVeloc(true);
  }
  function seleccionarEncuentro(e) {
    vp = e; for (const b of document.querySelectorAll("#eventos button")) b.setAttribute("aria-current", String(!!e && m.lista[+b.dataset.i].e === e));
    pintarDetalleTxt();
  }
  const irA = (j) => { jd = Math.max(m.ini, Math.min(m.fin, j)); };

  // ---------- geometría del mapa (vista cenital, escala comprimida o lineal)
  function cajas(cv) { const dpr = Math.min(2, devicePixelRatio || 1), W = cv.clientWidth, H = cv.clientHeight; if (cv.width !== Math.round(W * dpr) || cv.height !== Math.round(H * dpr)) { cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr); } const c = cv.getContext("2d"); c.setTransform(dpr, 0, 0, dpr, 0, 0); return [c, W, H]; }
  function dibujarMapa() {
    const [c, W, H] = cajas($("mapa")); c.fillStyle = "#02030a"; c.fillRect(0, 0, W, H);
    const N0 = m.vh.length - 1, k0 = Math.max(0, Math.min(N0, Math.ceil((jd - m.ini) / (m.fin - m.ini) * N0)));
    const meta = Math.max(1.3, m.rcum[k0] * 1.15, (vp && Math.abs(jd - vp.jd_ca) < 400 ? SEMIEJE[vp.planeta] * 1.25 : 0)); rvista += (meta - rvista) * (1 - Math.exp(-dtFrame / 0.35));   // el encuadre crece con la nave
    const cx = W / 2, cy = H / 2 + 8, R = Math.min(W / 2 - 54, H / 2 - 36), lineal = $("cLineal").checked;
    const esc = (r) => (lineal ? r / rvista : Math.sqrt(r / rvista)) * R;                  // r en UA -> píxeles
    const P = (v) => { const r = Math.hypot(v[0], v[1]) / UA_KM; if (r < 1e-9) return [cx, cy]; const k = esc(r) / r; return [cx + v[0] / UA_KM * k, cy - v[1] / UA_KM * k]; };
    mapaGeom = { P, R, cx, cy }; c.save(); c.beginPath(); c.arc(cx, cy, R * 1.04, 0, 7); c.clip();
    // órbitas de los planetas
    c.lineWidth = 1; c.font = "11px system-ui,sans-serif"; c.textBaseline = "middle";
    for (const id of PLAN) { const r = esc(SEMIEJE[id]); if (r > R * 1.02) continue; c.strokeStyle = "rgba(125,147,192,0.28)"; c.setLineDash([3, 5]); c.beginPath(); c.arc(cx, cy, r, 0, 7); c.stroke(); c.setLineDash([]); }
    // trayectoria completa (tenue) y recorrida (intensa)
    const N = m.vh.length - 1, k = Math.max(0, Math.min(N, Math.floor((jd - m.ini) / (m.fin - m.ini) * N)));
    const traza = (a, b, col, w) => { c.strokeStyle = col; c.lineWidth = w; c.beginPath(); for (let i = a; i <= b; i++) { const p = P([m.camino[i * 3], m.camino[i * 3 + 1]]); if (i === a) c.moveTo(p[0], p[1]); else c.lineTo(p[0], p[1]); } c.stroke(); };
    traza(0, N, "rgba(255,255,255,0.16)", 1.2); traza(0, k, m.d.color, 2.4); c.restore(); c.strokeStyle = "rgba(125,147,192,0.35)"; c.lineWidth = 1; c.beginPath(); c.arc(cx, cy, R * 1.04, 0, 7); c.stroke();
    // planetas en la fecha actual
    for (const id of PLAN) { const t = planetas.get(id); if (jd < t.meta.jd_valido_ini || jd > t.meta.jd_valido_fin) continue; const p = P(t.pos(jd, tmp)); if (Math.hypot(p[0] - cx, p[1] - cy) > R * 1.04) continue; c.fillStyle = COLOR_PLANETA[id]; c.beginPath(); c.arc(p[0], p[1], 4.2, 0, 7); c.fill(); c.fillStyle = "#cfd8ea"; c.textAlign = "left"; c.fillText(NOMBRE_PLANETA[id], p[0] + 7, p[1] - 6); }
    c.fillStyle = "#ffd45e"; c.beginPath(); c.arc(cx, cy, 5.5, 0, 7); c.fill(); c.fillStyle = "rgba(255,212,94,0.18)"; c.beginPath(); c.arc(cx, cy, 11, 0, 7); c.fill();
    // encuentros: anillo del color del planeta en el punto del recorrido; relleno si ya ocurrió
    mapaGeom.marcas = []; const ocupados = [];
    m.lista.forEach((x, i) => {
      if (x.h) { m.nave.pos(x.jd, tmp); const p = P(tmp); if (Math.hypot(p[0] - cx, p[1] - cy) > R * 1.04) return; c.strokeStyle = "#fff"; c.lineWidth = 1.4; c.beginPath(); c.moveTo(p[0] - 5, p[1] - 5); c.lineTo(p[0] + 5, p[1] + 5); c.moveTo(p[0] + 5, p[1] - 5); c.lineTo(p[0] - 5, p[1] + 5); c.stroke(); texto(c, x.h.nombre, p, ocupados, "#fff", W, H); mapaGeom.marcas.push({ p, i }); return; }
      const e = x.e; m.nave.pos(e.jd_ca, tmp); const p = P(tmp); if (Math.hypot(p[0] - cx, p[1] - cy) > R * 1.04) return; const pasado = jd >= e.jd_ca, col = COLOR_PLANETA[e.planeta], activo = vp === e;
      c.lineWidth = activo ? 3 : 2; c.strokeStyle = col; c.fillStyle = pasado ? col : "#02030a"; c.beginPath(); c.arc(p[0], p[1], activo ? 8 : 6, 0, 7); c.fill(); c.stroke();
      const dv = !e.orbita && Math.abs(e.dv_helio) > 0.3 ? `  ${e.dv_helio > 0 ? "▲" : "▼"}${signo(e.dv_helio)}` : "";
      texto(c, `${NOMBRE_PLANETA[e.planeta]} ${fechaCorta(e.jd_ca).slice(0, 7)}${dv}`, p, ocupados, activo ? "#fff" : "#cfd8ea", W, H); mapaGeom.marcas.push({ p, i });
    });
    // la nave
    m.nave.pos(jd, tmp); const pn = P(tmp);
    c.fillStyle = m.d.color + "44"; c.beginPath(); c.arc(pn[0], pn[1], 11, 0, 7); c.fill(); c.fillStyle = "#fff"; c.strokeStyle = m.d.color; c.lineWidth = 2.5; c.beginPath(); c.arc(pn[0], pn[1], 5, 0, 7); c.fill(); c.stroke();
    c.fillStyle = "#fff"; c.font = "600 12px system-ui,sans-serif"; c.textAlign = "left"; c.fillText(m.d.nombre, pn[0] + 11, pn[1] + 14);
    c.fillStyle = "#8fa0c0"; c.font = "11px system-ui,sans-serif"; c.textAlign = "right"; c.fillText(W < 560 ? (lineal ? "escala lineal" : "escala comprimida (√)") : lineal ? "escala lineal: las proporciones son reales" : "escala comprimida (√ de la distancia); «Escala lineal» muestra las proporciones reales", W - 12, H - 10);
  }
  function texto(c, t, p, ocupados, col, W, H) {   // etiqueta con evitación sencilla de solapes
    c.font = "11px system-ui,sans-serif"; c.textAlign = "left"; const w = c.measureText(t).width;
    for (const dy of [-12, 14, -26, 28]) { const r = [p[0] + 9, p[1] + dy - 7, w + 4, 14]; if (r[0] + r[2] > W || r[1] < 0 || r[1] + r[3] > H) continue; if (ocupados.some((o) => r[0] < o[0] + o[2] && r[0] + r[2] > o[0] && r[1] < o[1] + o[3] && r[1] + r[3] > o[1])) continue; ocupados.push(r); c.fillStyle = col; c.fillText(t, r[0], p[1] + dy); return; }
  }

  // ---------- velocidad heliocéntrica frente al tiempo
  let ultV = null;
  function dibujarVeloc(fuerza) {
    const [c, W, H] = cajas($("veloc")); const x0 = 46, x1 = W - 12, y0 = 18, y1 = H - 22, N = m.vh.length - 1;
    const X = (j) => x0 + (j - m.ini) / (m.fin - m.ini) * (x1 - x0), Y = (v) => y1 - v / m.vmax * (y1 - y0);
    c.fillStyle = "#070a14"; c.fillRect(0, 0, W, H); c.font = "10px system-ui,sans-serif"; c.textBaseline = "middle";
    c.strokeStyle = "rgba(125,147,192,0.2)"; c.fillStyle = "#8fa0c0"; c.textAlign = "right";
    const paso = m.vmax > 60 ? 20 : m.vmax > 30 ? 10 : 5; for (let v = 0; v <= m.vmax; v += paso) { c.beginPath(); c.moveTo(x0, Y(v)); c.lineTo(x1, Y(v)); c.stroke(); c.fillText(String(v), x0 - 5, Y(v)); }
    c.save(); c.translate(11, (y0 + y1) / 2); c.rotate(-Math.PI / 2); c.textAlign = "center"; c.fillText("km/s respecto del Sol", 0, 0); c.restore();
    c.textAlign = "center"; const a0 = jdUtcDesdeTdb(m.ini) , a1 = jdUtcDesdeTdb(m.fin), y_ini = new Date((a0 - 2440587.5) * 864e5).getUTCFullYear(), y_fin = new Date((a1 - 2440587.5) * 864e5).getUTCFullYear(), sp = Math.max(1, Math.ceil((y_fin - y_ini) / 8));
    for (let y = Math.ceil(y_ini / sp) * sp; y <= y_fin; y += sp) { const j = jdTdbDesdeUtc(Date.UTC(y, 0, 1) / 864e5 + 2440587.5); if (j > m.ini && j < m.fin) c.fillText(String(y), X(j), y1 + 12); }
    // velocidad de escape del Sol (si la nave la supera, está en órbita abierta)
    c.setLineDash([4, 4]); c.strokeStyle = "rgba(255,255,255,0.35)"; c.beginPath(); for (let i = 0; i <= N; i++) { const x = x0 + i / N * (x1 - x0), y = Y(Math.min(m.vesc[i], m.vmax)); if (i) c.lineTo(x, y); else c.moveTo(x, y); } c.stroke(); c.setLineDash([]);
    const linea = (a, b, col, w) => { c.strokeStyle = col; c.lineWidth = w; c.beginPath(); for (let i = a; i <= b; i++) { const x = x0 + i / N * (x1 - x0), y = Y(m.vh[i]); if (i === a) c.moveTo(x, y); else c.lineTo(x, y); } c.stroke(); };
    const k = Math.max(0, Math.min(N, Math.round((jd - m.ini) / (m.fin - m.ini) * N)));
    linea(0, N, "rgba(255,255,255,0.25)", 1.2); linea(0, k, m.d.color, 2.2);
    // encuentros con su ganancia
    c.font = "10px system-ui,sans-serif";
    let ultX = -99; for (const e of m.encs) { const x = X(e.jd_ca); c.strokeStyle = COLOR_PLANETA[e.planeta]; c.globalAlpha = 0.65; c.beginPath(); c.moveTo(x, y0); c.lineTo(x, y1); c.stroke(); c.globalAlpha = 1; c.fillStyle = COLOR_PLANETA[e.planeta]; c.beginPath(); c.arc(x, y1, 3, 0, 7); c.fill();
      if (!e.orbita && Math.abs(e.dv_helio) > 0.3 && x - ultX > 44) { ultX = x; c.fillStyle = e.dv_helio > 0 ? "#7ee0a1" : "#ff8a8a"; c.textAlign = "center"; c.fillText(`${e.dv_helio > 0 ? "▲" : "▼"}${signo(e.dv_helio)}`, x, y0 - 6); } }
    c.strokeStyle = "#fff"; c.lineWidth = 1.5; c.beginPath(); c.moveTo(X(jd), y0 - 4); c.lineTo(X(jd), y1); c.stroke();
    c.fillStyle = "#8fa0c0"; c.textAlign = "right"; c.fillText("┄ velocidad de escape del Sol", x1, y0 + 8);
    ultV = { X, x0, x1 };
  }
  $("veloc").addEventListener("pointerdown", (ev) => { const mover = (e) => { if (!ultV) return; const r = $("veloc").getBoundingClientRect(); irA(m.ini + (e.clientX - r.left - ultV.x0) / (ultV.x1 - ultV.x0) * (m.fin - m.ini)); }; mover(ev); const mv = (e) => mover(e), up = () => { removeEventListener("pointermove", mv); removeEventListener("pointerup", up); }; addEventListener("pointermove", mv); addEventListener("pointerup", up); });

  // ---------- detalle del encuentro (centrado en el planeta, el planeta a escala)
  function dibujarDetalle() {
    const [c, W, H] = cajas($("detalle")); c.fillStyle = "#02030a"; c.fillRect(0, 0, W, H); c.textBaseline = "middle";
    if (!vp) { c.fillStyle = "#8fa0c0"; c.font = "12px system-ui,sans-serif"; c.textAlign = "center"; c.fillText("Elija un encuentro de la lista", W / 2, H / 2); return; }
    const e = vp, tr = e.traza, r0 = tr.find((t) => Math.abs(t[0]) < 1e-9), x = [r0[1], r0[2], r0[3]], v = [r0[4], r0[5], r0[6]], dx = Math.hypot(...x);
    const ux = x.map((q) => q / dx), vx = v[0] * ux[0] + v[1] * ux[1] + v[2] * ux[2], vy = [v[0] - vx * ux[0], v[1] - vx * ux[1], v[2] - vx * ux[2]], nvy = Math.hypot(...vy), uy = vy.map((q) => q / nvy);
    const proy = (r) => [r[0] * ux[0] + r[1] * ux[1] + r[2] * ux[2], r[0] * uy[0] + r[1] * uy[1] + r[2] * uy[2]];
    const vista = Math.max(dx * 9, e.radio * 3), cx = W * 0.5, cy = H * 0.5, S = Math.min(W, H) / 2 / vista * 0.96;
    const Q = (p) => [cx + p[0] * S - W * 0.0, cy - p[1] * S];
    // anillos de referencia y el planeta
    c.strokeStyle = "rgba(125,147,192,0.22)"; c.lineWidth = 1; for (const f of [3, 6, 9]) { c.beginPath(); c.arc(cx, cy, dx * f * S, 0, 7); c.stroke(); }
    c.fillStyle = COLOR_PLANETA[e.planeta]; c.beginPath(); c.arc(cx, cy, Math.max(2.5, e.radio * S), 0, 7); c.fill();
    // direcciones útiles: hacia el Sol y movimiento del planeta (proyectadas en el plano del encuentro)
    const tp = planetas.get(e.planeta), pp = tp.pos(e.jd_ca), hacia = proy([-pp[0], -pp[1], -pp[2]]), vpl = (() => { const a = tp.pos(e.jd_ca - 0.05), b = tp.pos(e.jd_ca + 0.05); return proy([b[0] - a[0], b[1] - a[1], b[2] - a[2]]); })();
    const flecha = (d, col, txt, off) => {
      const n = Math.hypot(d[0], d[1]) || 1, ex = d[0] / n, ey = -d[1] / n, big = Math.min(W, H) * 0.34, L = Math.min(W, H) * 0.14, x1 = cx + ex * big, y1 = cy + ey * big;
      c.strokeStyle = col; c.fillStyle = col; c.lineWidth = 1.6; c.beginPath(); c.moveTo(cx + ex * (big - L), cy + ey * (big - L)); c.lineTo(x1, y1); c.stroke();
      const a = Math.atan2(ey, ex); c.beginPath(); c.moveTo(x1, y1); c.lineTo(x1 - 8 * Math.cos(a - 0.4), y1 - 8 * Math.sin(a - 0.4)); c.lineTo(x1 - 8 * Math.cos(a + 0.4), y1 - 8 * Math.sin(a + 0.4)); c.fill();
      c.font = "10px system-ui,sans-serif"; c.textAlign = "center"; c.fillText(txt, x1, y1 + off); };
    flecha(hacia, "#ffd45e", "☀ al Sol", -10); flecha(vpl, COLOR_PLANETA[e.planeta], "movimiento del planeta", 12);
    // trayectoria
    c.strokeStyle = m.d.color; c.lineWidth = 2.2; c.beginPath(); let primero = true; for (const t of tr) { const p = Q(proy([t[1], t[2], t[3]])); if (p[0] < -50 || p[0] > W + 50 || p[1] < -50 || p[1] > H + 50) { primero = true; continue; } if (primero) { c.moveTo(p[0], p[1]); primero = false; } else c.lineTo(p[0], p[1]); } c.stroke();
    // nave en el instante actual (si está dentro de la ventana del encuentro) y mayor acercamiento
    const pa = Q([dx, 0]); c.strokeStyle = "#fff"; c.lineWidth = 1.2; c.beginPath(); c.arc(pa[0], pa[1], 4, 0, 7); c.stroke();
    if (jd >= e.jd_ca + tr[0][0] && jd <= e.jd_ca + tr[tr.length - 1][0]) { const r = posicionPlanetocentrica(tr, jd - e.jd_ca), p = Q(proy(r)); c.fillStyle = "#fff"; c.beginPath(); c.arc(p[0], p[1], 5, 0, 7); c.fill(); c.strokeStyle = m.d.color; c.lineWidth = 2; c.stroke(); }
    c.fillStyle = "#8fa0c0"; c.font = "10px system-ui,sans-serif"; c.textAlign = "left"; c.fillText(`vista: ±${fmt(vista / 1e3, 0)} mil km`, 8, H - 10); c.textAlign = "right"; c.fillText("círculos: 3×, 6× y 9× la distancia mínima", W - 8, 12);
  }
  function pintarDetalleTxt() {
    const e = vp; if (!e) { $("detalleTxt").textContent = ""; return; }
    if (e.orbita) { $("detalleTxt").innerHTML = `<b>${NOMBRE_PLANETA[e.planeta]} · ${fechaCorta(e.jd_ca)}</b>: llegada y <b>inserción en órbita</b> (la nave se frena con su motor; no es una asistencia gravitatoria). Altura mínima ${fmt(e.alt_km, 0)} km sobre el nivel de referencia del planeta.`; return; }
    const ganancia = e.dv_helio, etiqueta = ganancia > 0.3 ? "acelera la nave" : ganancia < -0.3 ? "frena la nave" : "casi sólo cambia su dirección";
    $("detalleTxt").innerHTML = `<b>${NOMBRE_PLANETA[e.planeta]} · ${fechaCorta(e.jd_ca)}</b>: el planeta ${etiqueta}. Pasa a <b>${fmt(e.alt_km, 0)} km</b> de altura (${fmt(e.dist_km, 0)} km del centro) a ${fmt(e.vrel_kms, 1)} km/s; velocidad en el infinito ${fmt(e.vinf_kms, 1)} km/s; desvío <b>${fmt(e.desvio_deg, 0)}°</b> (excentricidad ${fmt(e.excentricidad, 2)}). Velocidad respecto del Sol: ${fmt(e.vh_in, 1)} → ${fmt(e.vh_out, 1)} km/s (<b>${signo(e.dv_helio)} km/s</b>).`;
  }

  // ---------- estado, controles y bucle
  function estado() {
    m.nave.pos(jd, tmp); m.nave.vel(jd, tmp2); const E = planetas.get("399").pos(jd, [0, 0, 0]), dS = Math.hypot(...tmp), dE = Math.hypot(tmp[0] - E[0], tmp[1] - E[1], tmp[2] - E[2]), v = Math.hypot(...tmp2);
    let cerca = null; for (const id of PLAN) { const t = planetas.get(id); if (jd < t.meta.jd_valido_ini || jd > t.meta.jd_valido_fin) continue; const d = Math.hypot(...t.pos(jd, [0, 0, 0]).map((q, i) => q - tmp[i])); if (!cerca || d < cerca[1]) cerca = [id, d]; }
    const ut = jdUtcDesdeTdb(jd), sinc = m.d.sinContacto && ut > jdUtcDesdeInput(m.d.sinContacto + "T00:00"), pred = jd > JD_HOY;
    $("fecha").textContent = formatoUtc(ut, false).slice(0, 10);
    $("sub").textContent = `${m.d.nombre} · día ${fmt(jd - m.ini, 0)} desde el lanzamiento${sinc ? " · extrapolación (sin contacto)" : pred ? " · predicción de JPL" : ""}`;
    const sen = dE / C_KM_S, n = m.lista.filter((x) => x.e && x.jd <= jd).length, tot = m.encs.length;
    $("estado").innerHTML = `<dt>Distancia al Sol</dt><dd>${fmt(dS / UA_KM, 2)} UA</dd><dt>Distancia a la Tierra</dt><dd>${fmt(dE / UA_KM, 2)} UA</dd><dt>Velocidad respecto del Sol</dt><dd>${fmt(v, 1)} km/s</dd><dt>Señal de radio a la Tierra</dt><dd>${sen > 7200 ? fmt(sen / 3600, 1) + " h" : fmt(sen / 60, 1) + " min"}</dd><dt>Planeta más cercano</dt><dd>${cerca ? `${NOMBRE_PLANETA[cerca[0]]} · ${cerca[1] < 5e7 ? fmt(cerca[1] / 1e3, 0) + " mil km" : fmt(cerca[1] / 1e6, 1) + " M km"}` : "—"}</dd><dt>Encuentros realizados</dt><dd>${n} de ${tot}</dd>`;
    // encuentro mostrado: el activo en la ventana temporal, si lo hay
    const en = m.nave.enEncuentro(jd); if (en && vp !== en.e) seleccionarEncuentro(en.e);
  }
  function velocidadEfectiva() {   // días de misión por segundo real
    let v = velocidad / 86400;
    if ($("cLenta").checked) { const en = m.nave.enEncuentro(jd); if (en) { const dt = Math.abs(jd - en.e.jd_ca); v = Math.min(v, 0.5 * dt + 0.0005); } }
    return v;
  }
  $("sMision").onchange = () => elegir($("sMision").value);
  $("eventos").addEventListener("click", (e) => { const b = e.target.closest("button"); if (!b) return; const x = m.lista[+b.dataset.i]; if (x.e) { seleccionarEncuentro(x.e); irA(x.e.jd_ca - Math.min(3, Math.max(0.5, (x.e.jd_ca - x.e.jd_in) * 0.05))); } else irA(x.jd); });
  $("mapa").addEventListener("click", (ev) => { if (!mapaGeom) return; const r = $("mapa").getBoundingClientRect(), x = ev.clientX - r.left, y = ev.clientY - r.top; let mejor = null; for (const k of mapaGeom.marcas) { const d = Math.hypot(k.p[0] - x, k.p[1] - y); if (d < 14 && (!mejor || d < mejor[1])) mejor = [k, d]; } if (!mejor) return; const it = m.lista[mejor[0].i]; if (it.e) { seleccionarEncuentro(it.e); irA(it.e.jd_ca - 1.5); } else irA(it.jd); });
  $("sVel").innerHTML = VEL.map(([t, v]) => `<option value="${v}">${t}</option>`).join(""); $("sVel").value = "86400"; $("sVel").onchange = () => { velocidad = +$("sVel").value; };
  const play = () => { jugando = !jugando; $("bPlay").textContent = jugando ? "⏸" : "▶"; $("bPlay").setAttribute("aria-label", jugando ? "Pausar" : "Reproducir"); if (jugando && jd >= m.fin - 1) jd = m.ini; };
  $("bPlay").onclick = play; $("bIni").onclick = () => irA(m.ini); $("bFin").onclick = () => irA(m.fin);
  const vecino = (dir) => { const l = m.lista.filter((x) => x.e || x.h); const t = dir > 0 ? l.find((x) => x.jd > jd + 0.5) : [...l].reverse().find((x) => x.jd < jd - 0.5); return t; };
  $("bSig").onclick = () => { const t = vecino(1); if (t) { if (t.e) seleccionarEncuentro(t.e); irA((t.e ? t.e.jd_in : t.jd) - 0.5); } };
  $("bAnt").onclick = () => { const t = vecino(-1); if (t) { if (t.e) seleccionarEncuentro(t.e); irA((t.e ? t.e.jd_in : t.jd) - 0.5); } };
  addEventListener("keydown", (e) => { if (/INPUT|SELECT|TEXTAREA/.test(document.activeElement.tagName)) return; if (e.code === "Space") { e.preventDefault(); play(); } });
  $("meta").innerHTML = `<p>Trayectorias reconstruidas por JPL con datos de seguimiento (SPICE), de Horizons, en posiciones heliocéntricas (eclíptica J2000) con paso de 1 a 3 días e interpolación de Lagrange; las posteriores al 13-11-2026 son <b>predicciones</b>. <b>Cada encuentro</b> (de entrar a salir de la esfera de influencia del planeta) usa la trayectoria planetocéntrica calculada por Horizons con paso de minutos cerca del mayor acercamiento; así la nave pasa por el planeta con la altura real. La <b>ganancia de velocidad</b> es la del método de las cónicas empalmadas: la velocidad heliocéntrica de la asíntota de salida menos la de entrada, con la hipérbola calculada del estado en el mayor acercamiento. Los planetas salen de las efemérides oficiales de 1970 a 2050. Los puntos de la nave y los planetas son simbólicos (no a escala); en el detalle del encuentro el planeta sí está a escala.</p>`;
  const pedida = /m=(-?\d+)/.exec(location.hash); elegir(pedida && MISIONES[pedida[1]] && nav.cuerpos.has(pedida[1]) ? pedida[1] : "-31");
  let ult = 0;
  (function cuadro(t) {
    if (jugando) { jd = Math.min(m.fin, jd + ((t - (tprev || t)) / 1000) * velocidadEfectiva()); if (jd >= m.fin) { jugando = false; $("bPlay").textContent = "▶"; } }
    dtFrame = Math.min(2, (t - (tprev || t)) / 1000); tprev = t; dibujarMapa(); dibujarVeloc(); dibujarDetalle(); if (t - ult > 100) { ult = t; estado(); } requestAnimationFrame(cuadro);
  })(0);
  window.__mis = { get rvista() { return rvista; }, get geom() { return mapaGeom; }, get jd() { return jd; }, set jd(v) { jd = v; }, elegir, nav, planHist, EN, get m() { return m; } };
}
