// SPDX-License-Identifier: Apache-2.0
// Simulador del cinturón de asteroides: ~2 500 asteroides del JPL Small-Body Database con los planetas interiores y Júpiter.
import { cargarSistema } from "./efemerides.js";
import { Vista } from "./vista.js";
import { SOL, PLANETAS, UA_KM, baseDelCuerpo } from "./cuerpos.js";
import { Reloj, JD_UTC_INICIO, JD_UTC_FIN, formatoUtc, valorInputUtc, jdUtcDesdeInput } from "./tiempo.js";
import { CLASES, posicion, derivados, trazaOrbita } from "./asteroides.js";
import { barraNavegacion } from "./navegacion.js";

const fmt = (x, d = 0) => x.toLocaleString("es-CL", { minimumFractionDigits: d, maximumFractionDigits: d });
const VEL = [["1 día / s", 86400], ["10 días / s", 864000], ["30 días / s", 2592000], ["1 año / s", 31557600], ["5 años / s", 157788000]];
const PLAN = ["199", "299", "399", "499", "599"];

export async function iniciarAsteroides() {
  const raiz = document.getElementById("app");
  const cab = document.createElement("header"); cab.className = "cabecera"; cab.innerHTML = "<h1>Cinturón de asteroides</h1>"; cab.appendChild(barraNavegacion("asteroides")); document.body.insertBefore(cab, raiz);
  raiz.className = "app";
  raiz.innerHTML = `
    <section class="escena" aria-label="Escena 3D de los asteroides">
      <canvas id="lienzo" tabindex="0" aria-label="Asteroides y planetas vistos desde arriba. Arrastre para girar, rueda para acercar, clic en un asteroide para ver sus datos."></canvas>
      <div class="hud"><div class="fecha" id="fecha"></div><div class="sub" id="sub"></div></div>
      <div class="cargando" id="cargando"><div>Cargando efemérides y elementos orbitales…</div><progress id="prog" max="1" value="0"></progress></div>
      <div class="barra"><div class="grupo"><button id="bPlay" aria-label="Reproducir">▶</button><button id="bAtras" aria-label="Retroceder 30 días">◀</button><button id="bAdel" aria-label="Avanzar 30 días">▶|</button></div>
        <div class="grupo"><label class="etq" for="sVel">Velocidad</label><select id="sVel"></select></div>
        <div class="grupo"><label class="etq" for="iFecha">Fecha UTC</label><input type="datetime-local" id="iFecha" min="2027-01-01T00:00" max="2050-12-31T23:59"><button id="bIr">Ir</button></div></div>
    </section>
    <aside class="lateral" aria-label="Datos y controles">
      <h2>Asteroide seleccionado</h2><div class="ficha" id="ficha" aria-live="polite"></div>
      <h2>Familias</h2><div id="clases" style="display:flex;flex-wrap:wrap;gap:4px 12px"></div>
      <div style="margin-top:8px;display:flex;gap:6px;flex-wrap:wrap"><button id="vInt">Hasta Marte</button><button id="vCin">Cinturón</button><button id="vJup">Hasta Júpiter</button><button id="vLat">Vista lateral</button></div>
      <h2>Buscar</h2><input type="search" id="buscar" placeholder="Ceres, Vesta, Apophis…" aria-label="Buscar asteroide" style="width:100%"><div class="lista" id="lista" role="listbox" aria-label="Asteroides" style="max-height:220px"></div>
      <details><summary>Modelo, datos y precisión</summary><div class="aviso" id="meta"></div></details>
      <p class="aviso">Documentación: <a href="documentacion/README.html">documentación de los simuladores</a>.</p>
    </aside>`;
  const $ = (i) => document.getElementById(i);
  let sol, ast;
  try { const p = [0, 0]; const pr = () => { $("prog").value = (p[0] + p[1]) / 2; }; [sol, ast] = await Promise.all([cargarSistema("sol", "datos", (f) => { p[0] = f; pr(); }), fetch("datos/asteroides.json").then((r) => r.json()).then((j) => { p[1] = 1; pr(); return j; })]); }
  catch (e) { $("cargando").classList.add("error"); $("cargando").innerHTML = `<div><strong>No se pudieron cargar los datos.</strong></div><div>${e.message}</div>`; return; }
  $("cargando").remove();
  const reloj = new Reloj(JD_UTC_INICIO); reloj.velocidad = 864000;
  const vista = new Vista($("lienzo"), { dist: 1.4e9, limites: { min: 1e6, max: 3e10 }, alSeleccionar: (o) => seleccionar(o) });
  vista.cam.pitch = 1.05; vista.cam.yaw = -1.0;
  const solObj = vista.añadir({ id: "10", nombre: "Sol", radio: SOL.radio, color: SOL.color, autoluminoso: true, textura: "sol", prioridad: 1000, ampliable: false, base: baseDelCuerpo(SOL.polo, 2461406.5), noSeleccionable: true });
  vista.sol = solObj; solObj.ocultarFlecha = true; vista.seguir = solObj;
  const planetas = PLAN.map((id) => vista.añadir({ id, nombre: PLANETAS[id].nombre, radio: 0, color: PLANETAS[id].color, prioridad: 500, ampliable: false, noSeleccionable: true, tabla: sol.cuerpo(id), colorOrbita: "rgba(120,160,220,0.3)" }));
  const filas = ast.asteroides, objs = filas.map((f, i) => vista.añadir({ id: "a" + i, nombre: f[2], radio: 0, color: (CLASES[f[3]] || ["", "#ccc"])[1], etiqueta: false, prioridad: 0, ampliable: false, ocultarOrbita: true, fila: f, clase: f[3] }));
  const activa = new Set(Object.keys(CLASES));
  $("clases").innerHTML = Object.entries(CLASES).filter(([k]) => filas.some((f) => f[3] === k)).map(([k, [n, c]]) => `<label class="chk"><input type="checkbox" data-c="${k}" checked><span style="color:${c}">●</span> ${n} <small>(${filas.filter((f) => f[3] === k).length})</small></label>`).join("");
  $("clases").addEventListener("change", (e) => { const c = e.target.dataset.c; if (e.target.checked) activa.add(c); else activa.delete(c); for (const o of objs) o.oculto = !activa.has(o.clase); });
  const el = (r, v, mu) => null; void el;
  // órbitas planetarias: arco de un periodo desde la tabla, o elipse osculadora para los gigantes
  function orbitasPlanetas() { const jd = reloj.jdTdb; for (const p of planetas) { const P = { "199": 88, "299": 225, "399": 365.25, "499": 687, "599": 4333 }[p.id], tmp = [0, 0, 0], N = 160, pts = new Float64Array((N + 1) * 3); const v0 = p.tabla.meta.jd_valido_ini, v1 = p.tabla.meta.jd_valido_fin; const a = Math.min(Math.max(jd - P / 2, v0), v1 - P); for (let k = 0; k <= N; k++) { p.tabla.pos(a + P * k / N, tmp); pts[k * 3] = tmp[0]; pts[k * 3 + 1] = tmp[1]; pts[k * 3 + 2] = tmp[2]; } p.orbita = pts; } }
  let sel = null, orbSel = null;
  function seleccionar(o) {
    if (!o || !o.fila) { sel = null; $("ficha").innerHTML = "<span class='etq'>Haga clic en un asteroide o elija uno de la lista.</span>"; return; }
    sel = o; vista.seleccionado = o; o.orbita = trazaOrbita(o.fila); o.ocultarOrbita = false; o.colorOrbita = "rgba(255,224,138,0.9)"; if (orbSel && orbSel !== o) { orbSel.orbita = null; } orbSel = o; pintarFicha();
  }
  function pintarFicha() {
    if (!sel) return; const f = sel.fila, d = derivados(f), P = sel.pos, tierra = planetas[2].pos, dS = Math.hypot(...P), dT = Math.hypot(P[0] - tierra[0], P[1] - tierra[1], P[2] - tierra[2]);
    const t = [["Clase", (CLASES[f[3]] || ["", ""])[0]], ["Número / designación", f[1]], ["Magnitud absoluta H", fmt(f[11], 2)], ["Diámetro", f[12] ? `${fmt(f[12], f[12] < 10 ? 1 : 0)} km` : "no publicado"], ["a · e · i", `${fmt(f[4], 3)} UA · ${fmt(f[5], 3)} · ${fmt(f[6], 1)}°`], ["Perihelio · afelio", `${fmt(d.peri, 2)} · ${fmt(d.afe, 2)} UA`], ["Periodo", `${fmt(d.periodo, 2)} años`], ["Distancia al Sol", `${fmt(dS / UA_KM, 3)} UA`], ["Distancia a la Tierra", `${fmt(dT / UA_KM, 3)} UA`]];
    $("ficha").innerHTML = `<h3>${f[2]}</h3><dl class="datos">${t.map(([k, v]) => `<dt>${k}</dt><dd>${v}</dd>`).join("")}</dl>`;
  }
  function lista() {
    const q = $("buscar").value.trim().toLowerCase();
    const l = filas.map((f, i) => [f, i]).filter(([f]) => !q || (f[2] + " " + f[1]).toLowerCase().includes(q)).slice(0, 120);
    $("lista").innerHTML = l.map(([f, i]) => `<button data-i="${i}"><span>${f[2]}</span><small>H ${fmt(f[11], 1)}</small></button>`).join("");
  }
  $("lista").addEventListener("click", (e) => { const b = e.target.closest("button"); if (b) { const o = objs[+b.dataset.i]; seleccionar(o); vista.cam.distObj = Math.max(5e7, Math.hypot(...o.pos) * 2.2); } });
  $("buscar").addEventListener("input", lista); lista();
  const camara = (dist, pit) => { vista.seguir = solObj; vista.cam.distObj = dist; vista.cam.pitch = pit; };
  $("vInt").onclick = () => camara(5e8, 1.1); $("vCin").onclick = () => camara(1.4e9, 1.05); $("vJup").onclick = () => camara(2.4e9, 1.05); $("vLat").onclick = () => camara(1.6e9, 0.05);
  $("sVel").innerHTML = VEL.map(([t, v]) => `<option value="${v}">${t}</option>`).join(""); $("sVel").onchange = () => { reloj.velocidad = +$("sVel").value; };
  const play = () => { reloj.activo = !reloj.activo; $("bPlay").textContent = reloj.activo ? "⏸" : "▶"; };
  $("bPlay").onclick = play; $("bAtras").onclick = () => reloj.fijar(reloj.jdUtc - 30); $("bAdel").onclick = () => reloj.fijar(reloj.jdUtc + 30);
  $("bIr").onclick = () => { const j = jdUtcDesdeInput($("iFecha").value); if (j) reloj.fijar(j); };
  window.addEventListener("keydown", (e) => { if (/INPUT|SELECT|TEXTAREA/.test(document.activeElement.tagName)) return; if (e.code === "Space") { e.preventDefault(); play(); } });
  $("meta").innerHTML = `<p>${fmt(filas.length)} asteroides de ${Object.keys(CLASES).length} familias (cinturón principal y sus subgrupos, troyanos, Hildas y cercanos a la Tierra) del JPL Small-Body Database. <strong>Las posiciones son una aproximación:</strong> propagación kepleriana de dos cuerpos desde los elementos osculadores de JPL (marco eclíptico J2000), sin perturbaciones planetarias. El error crece con el tiempo desde la época de los elementos (2026): en una muestra de 24 asteroides contrastada con JPL Horizons, la mediana es de ≈ 1,5 millones de km en 2030 y de ≈ 7,7 millones de km (0,05 UA) en 2050, con casos de decenas de millones en los asteroides cercanos a la Tierra. Sirve para ver la estructura del cinturón y sus familias, no para predecir posiciones. Los planetas salen de las efemérides oficiales.</p>`;
  orbitasPlanetas(); seleccionar(objs.find((o) => o.fila[1] === "4") || objs[0]);
  let ult = 0;
  (function cuadro(t) {
    reloj.paso(t); const jd = reloj.jdTdb;
    for (const p of planetas) p.tabla.pos(jd, p.pos);
    for (const o of objs) posicion(o.fila, jd, o.pos);
    if (t - ult > 400) { ult = t; $("fecha").textContent = formatoUtc(reloj.jdUtc, false); $("sub").textContent = `${fmt(filas.length)} asteroides · posiciones keplerianas aproximadas`; if (document.activeElement !== $("iFecha")) $("iFecha").value = valorInputUtc(reloj.jdUtc); pintarFicha(); }
    vista.dibujar(jd); requestAnimationFrame(cuadro);
  })(0);
  window.__ast = { vista, reloj, filas };
}
