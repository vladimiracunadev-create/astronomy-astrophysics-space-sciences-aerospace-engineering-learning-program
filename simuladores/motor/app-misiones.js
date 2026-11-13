// SPDX-License-Identifier: Apache-2.0
// Simulador de misiones espaciales ya realizadas: se elige una misión y se recorre su trayectoria con ▶ (fechas, distancias, acercamientos).
import { cargarSistema } from "./efemerides.js";
import { Vista } from "./vista.js";
import { SOL, PLANETAS, UA_KM, C_KM_S, baseDelCuerpo } from "./cuerpos.js";
import { jdTdbDesdeUtc, jdUtcDesdeTdb, formatoUtc, jdUtcDesdeInput, valorInputUtc } from "./tiempo.js";
import { MISIONES, NOMBRE_PLANETA, hitosDeMision } from "./misiones.js";
import { barraNavegacion } from "./navegacion.js";

const fmt = (x, d = 0) => x.toLocaleString("es-CL", { minimumFractionDigits: d, maximumFractionDigits: d });
const VEL = [["1 día / s", 86400], ["10 días / s", 864000], ["30 días / s", 2592000], ["1 año / s", 31557600], ["3 años / s", 94672800]];
const PLAN = ["199", "299", "399", "499", "599", "699", "799", "899", "9"];

export async function iniciarMisiones() {
  const raiz = document.getElementById("app");
  const cab = document.createElement("header"); cab.className = "cabecera"; cab.innerHTML = "<h1>Misiones espaciales</h1>"; cab.appendChild(barraNavegacion("misiones")); document.body.insertBefore(cab, raiz);
  raiz.className = "app";
  raiz.innerHTML = `
    <section class="escena" aria-label="Trayectoria de la misión">
      <canvas id="lienzo" tabindex="0" aria-label="Trayectoria de la nave y posiciones de los planetas, vistos desde el polo norte eclíptico. Arrastre para girar, rueda para el zoom."></canvas>
      <div class="hud"><div class="fecha" id="fecha"></div><div class="sub" id="sub"></div></div>
      <div class="cargando" id="cargando"><div>Cargando trayectorias de JPL…</div><progress id="prog" max="1" value="0"></progress></div>
      <div class="barra"><div class="grupo" role="group" aria-label="Control del tiempo"><button id="bIni" aria-label="Ir al lanzamiento" title="Lanzamiento">⏮</button><button id="bPlay" aria-label="Reproducir" title="Reproducir / pausar (espacio)">▶</button><button id="bFin" aria-label="Ir al final" title="Final de los datos">⏭</button></div>
        <div class="grupo"><label class="etq" for="rango">Tiempo</label><input type="range" id="rango" min="0" max="2000" value="0" style="width:min(380px,38vw)"></div>
        <div class="grupo"><label class="etq" for="sVel">Velocidad</label><select id="sVel"></select></div>
        <div class="grupo"><label class="chk"><input type="checkbox" id="cSeg"> Seguir la nave</label><label class="chk"><input type="checkbox" id="cAjuste" checked> Encuadre automático</label></div></div>
    </section>
    <aside class="lateral" aria-label="Misión y datos">
      <h2>Misión</h2><div id="misiones" style="display:flex;flex-wrap:wrap;gap:6px"></div>
      <div class="ficha" id="ficha" style="margin-top:8px" aria-live="polite"></div>
      <h2>Hitos y acercamientos</h2><div class="lista" id="eventos" style="max-height:230px"></div>
      <p class="aviso">Los acercamientos se detectan en los datos (distancia mínima nave–planeta con datos heliocéntricos); la distancia indicada es aproximada en los sobrevuelos rápidos.</p>
      <details><summary>Datos, modelo y límites</summary><div class="aviso" id="meta"></div></details>
      <p class="aviso">Documentación: <a href="documentacion/README.html">documentación de los simuladores</a>.</p>
    </aside>`;
  const $ = (i) => document.getElementById(i);
  let planHist, nav;
  try { const p = [0, 0]; const pr = () => { $("prog").value = (p[0] + p[1]) / 2; }; [planHist, nav] = await Promise.all([cargarSistema("planetas_hist", "datos", (f) => { p[0] = f; pr(); }), cargarSistema("misiones", "datos", (f) => { p[1] = f; pr(); })]); }
  catch (e) { $("cargando").classList.add("error"); $("cargando").innerHTML = `<div><strong>No se pudieron cargar los datos.</strong></div><div>${e.message}</div><small>Abra el sitio publicado en GitHub Pages o sirva la carpeta con <code>python -m http.server</code>.</small>`; return; }
  $("cargando").remove();
  const vista = new Vista($("lienzo"), { dist: 6e8, limites: { min: 1e5, max: 4e10 } });
  vista.cam.pitch = 1.1; vista.cam.yaw = -1.0;
  const solObj = vista.añadir({ id: "10", nombre: "Sol", radio: SOL.radio, color: SOL.color, autoluminoso: true, textura: "sol", prioridad: 1000, ampliable: false, base: baseDelCuerpo(SOL.polo, 2461406.5), noSeleccionable: true });
  vista.sol = solObj; solObj.ocultarFlecha = true; vista.seguir = solObj;
  const planetas = PLAN.map((id) => { const f = PLANETAS[id]; return vista.añadir({ id, nombre: NOMBRE_PLANETA[id], radio: 0, color: f.color, prioridad: 500, ampliable: false, noSeleccionable: true, tabla: planHist.cuerpo(id), ocultarOrbita: true }); });
  const planTab = planetas.map((p) => [p.id, p.tabla]);
  const naveObj = vista.añadir({ id: "nave", nombre: "", radio: 0, color: "#fff", prioridad: 900, ampliable: false, noSeleccionable: true, ocultarOrbita: false, colorOrbita: "rgba(255,255,255,0.25)" });
  const traza = vista.añadir({ id: "traza", nombre: "", radio: 0, color: "#fff", etiqueta: false, ampliable: false, noSeleccionable: true, ocultarOrbita: false, colorOrbita: "#fff" });
  traza.pos = [1e30, 1e30, 1e30]; traza.oculto = false;
  let m = null, jd = 0, jugando = false, velocidad = 864000, eventos = [], camino = null, maxR = 1e8;
  const tab = (id) => nav.cuerpo(id);
  const jdAFecha = (j) => formatoUtc(jdUtcDesdeTdb(j), false).slice(0, 10);

  function pintarMisiones() {
    $("misiones").innerHTML = Object.entries(MISIONES).filter(([id]) => nav.cuerpos.has(id)).map(([id, d]) => `<button data-id="${id}" aria-pressed="false" style="border-left:4px solid ${d.color}">${d.nombre}</button>`).join("");
  }
  function elegir(id) {
    const d = MISIONES[id], t = tab(id); m = { id, d, t, ini: t.meta.jd_valido_ini, fin: t.meta.jd_valido_fin };
    for (const b of document.querySelectorAll("#misiones button")) b.setAttribute("aria-pressed", String(b.dataset.id === id));
    naveObj.nombre = d.nombre; naveObj.color = d.color; traza.colorOrbita = d.color;
    // camino completo (600 puntos)
    const N = 600; camino = new Float64Array((N + 1) * 3); const tmp = [0, 0, 0]; maxR = 1e8;
    for (let k = 0; k <= N; k++) { t.pos(m.ini + (m.fin - m.ini) * k / N, tmp); camino[k * 3] = tmp[0]; camino[k * 3 + 1] = tmp[1]; camino[k * 3 + 2] = tmp[2]; }
    naveObj.orbita = camino;
    eventos = hitosDeMision(id, t, planTab);
    const hitos = (d.hitos || []).map(([n, f, au]) => ({ hito: true, nombre: n, jdTdb: jdTdbDesdeUtc(jdUtcDesdeInput(f + "T00:00")), au }));
    eventos = eventos.concat(hitos).sort((a, b) => a.jdTdb - b.jdTdb);
    const lanz = m.ini, fin = m.fin;
    $("ficha").innerHTML = `<h3>${d.nombre}</h3><p style="margin:4px 0">${d.resumen}</p><dl class="datos"><dt>Datos desde</dt><dd>${jdAFecha(lanz)}</dd><dt>Datos hasta</dt><dd>${jdAFecha(fin)}${fin > jdTdbDesdeUtc(jdUtcDesdeInput("2026-11-14T00:00")) ? " (predicción)" : ""}</dd><dt>Error de interpolación (máx.)</dt><dd>${fmt(t.meta.error_max_km, 0)} km</dd></dl>`;
    $("eventos").innerHTML = eventos.map((e, i) => `<button data-i="${i}"><span>${jdAFecha(e.jdTdb)} · ${e.hito ? e.nombre : e.etiqueta}</span><small>${e.hito ? fmt(e.au, 0) + " UA" : fmt(e.dist_km / 1e3, 0) + " mil km"}</small></button>`).join("") || "<div class='aviso' style='padding:8px'>Sin acercamientos a planetas.</div>";
    jd = m.ini; $("rango").value = 0; camara();
    history.replaceState(null, "", `#m=${id}`);
  }
  function camara() { vista.seguir = $("cSeg").checked ? naveObj : solObj; }
  function autoajuste() {
    if (!$("cAjuste").checked || $("cSeg").checked || !m) return;
    const tmp = [0, 0, 0]; let mr = 0; const n = 80; for (let k = 0; k <= n; k++) { m.t.pos(m.ini + (jd - m.ini) * k / n, tmp); mr = Math.max(mr, Math.hypot(...tmp)); } mr = Math.max(mr, 2.2e8);
    const objetivo = Math.min(3.6e10, mr * 2.6); vista.cam.distObj += (objetivo - vista.cam.distObj) * 0.04;
  }
  function actualizar() {
    for (const p of planetas) { const t = p.tabla.meta; p.oculto = jd < t.jd_valido_ini || jd > t.jd_valido_fin; if (!p.oculto) p.tabla.pos(jd, p.pos); p.radio = vista.cam.dist * 0.006; }
    solObj.radio = vista.cam.dist * 0.003;
    if (!m) return;
    m.t.pos(jd, naveObj.pos); naveObj.radio = vista.cam.dist * 0.007;
    const k = Math.max(2, Math.round(300 * (jd - m.ini) / (m.fin - m.ini))), tr = new Float64Array((k + 1) * 3), tmp = [0, 0, 0];
    for (let i = 0; i <= k; i++) { m.t.pos(m.ini + (jd - m.ini) * i / k, tmp); tr[i * 3] = tmp[0]; tr[i * 3 + 1] = tmp[1]; tr[i * 3 + 2] = tmp[2]; }
    traza.orbita = tr;
  }
  function info() {
    if (!m) return; const P = naveObj.pos, E = planetas[2].pos, v = m.t.vel(jd), dS = Math.hypot(...P), dE = Math.hypot(P[0] - E[0], P[1] - E[1], P[2] - E[2]);
    let cerca = null; for (const p of planetas) { if (p.oculto) continue; const d = Math.hypot(P[0] - p.pos[0], P[1] - p.pos[1], P[2] - p.pos[2]); if (!cerca || d < cerca[1]) cerca = [p, d]; }
    const sig = eventos.find((e) => e.jdTdb > jd), ant = [...eventos].reverse().find((e) => e.jdTdb <= jd);
    $("fecha").textContent = formatoUtc(jdUtcDesdeTdb(jd), false).slice(0, 10) + (jd > jdTdbDesdeUtc(jdUtcDesdeInput("2026-11-14T00:00")) ? " · predicción" : "");
    $("sub").innerHTML = `${m.d.nombre} · día ${fmt(jd - m.ini, 0)} desde el inicio de los datos · ${fmt(dS / UA_KM, 2)} UA del Sol · ${fmt(dE / UA_KM, 2)} UA de la Tierra · ${fmt(Math.hypot(...v), 1)} km/s · señal a la Tierra: ${dE / C_KM_S > 7200 ? fmt(dE / C_KM_S / 3600, 1) + " h" : fmt(dE / C_KM_S / 60, 1) + " min"}${cerca ? ` · más cerca: ${cerca[0].nombre} (${fmt(cerca[1] / 1e6, 1)} M km)` : ""}${ant ? ` · último: ${jdAFecha(ant.jdTdb)}` : ""}${sig ? ` · siguiente: ${jdAFecha(sig.jdTdb)}` : ""}`;
  }
  $("misiones").addEventListener("click", (e) => { const b = e.target.closest("button"); if (b) elegir(b.dataset.id); });
  $("eventos").addEventListener("click", (e) => { const b = e.target.closest("button"); if (b) { jd = eventos[+b.dataset.i].jdTdb; sync(); } });
  const sync = () => { $("rango").value = Math.round(2000 * (jd - m.ini) / (m.fin - m.ini)); };
  $("rango").oninput = () => { if (m) jd = m.ini + (m.fin - m.ini) * (+$("rango").value / 2000); };
  $("sVel").innerHTML = VEL.map(([t, v]) => `<option value="${v}">${t}</option>`).join(""); $("sVel").value = "864000"; $("sVel").onchange = () => { velocidad = +$("sVel").value; };
  const play = () => { jugando = !jugando; $("bPlay").textContent = jugando ? "⏸" : "▶"; $("bPlay").setAttribute("aria-label", jugando ? "Pausar" : "Reproducir"); if (jugando && m && jd >= m.fin - 1) jd = m.ini; };
  $("bPlay").onclick = play; $("bIni").onclick = () => { if (m) { jd = m.ini; sync(); } }; $("bFin").onclick = () => { if (m) { jd = m.fin; sync(); } };
  window.addEventListener("keydown", (e) => { if (/INPUT|SELECT|TEXTAREA/.test(document.activeElement.tagName)) return; if (e.code === "Space") { e.preventDefault(); play(); } });
  $("cSeg").onchange = () => { camara(); if ($("cSeg").checked) vista.cam.distObj = 2e7; };
  $("meta").innerHTML = `<p>Trayectorias reconstruidas por JPL con datos de seguimiento (SPICE), obtenidas de Horizons como posiciones heliocéntricas (eclíptica J2000) y evaluadas por interpolación de Lagrange; las de fechas posteriores a la descarga (13-11-2026) son <strong>predicciones</strong>. Paso de 1 a 3 días: en los sobrevuelos y maniobras rápidas la posición tiene errores de hasta decenas de miles de km (se indica el máximo medido de cada misión). Los planetas salen de las efemérides oficiales 1970–2050. Los tamaños de los puntos son simbólicos (no a escala).</p>`;
  pintarMisiones();
  const pedida = /m=(-?\d+)/.exec(location.hash); elegir(pedida && MISIONES[pedida[1]] ? pedida[1] : "-31");
  let ult = 0, tprev = 0;
  (function cuadro(t) {
    if (jugando && m) { jd = Math.min(m.fin, jd + ((t - (tprev || t)) / 1000) * velocidad / 86400); if (jd >= m.fin) { jugando = false; $("bPlay").textContent = "▶"; } sync(); }
    tprev = t; if (m) { autoajuste(); actualizar(); if (t - ult > 120) { ult = t; info(); } vista.dibujar(jd); } requestAnimationFrame(cuadro);
  })(0);
  window.__mis = { vista, get jd() { return jd; }, elegir, nav, planHist };
}
