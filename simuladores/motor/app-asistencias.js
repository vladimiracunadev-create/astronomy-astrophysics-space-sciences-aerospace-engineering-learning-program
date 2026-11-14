// SPDX-License-Identifier: Apache-2.0
// Asistencias gravitatorias: calculadora interactiva del método de las cónicas empalmadas con el planeta a escala y los casos reales de las misiones.
import { cargarSistema } from "./efemerides.js";
import { jdTdbDesdeUtc, jdUtcDesdeTdb, jdUtcDesdeInput, formatoUtc } from "./tiempo.js";
import { asistencia, desdeEncuentro } from "./asistencia.js";
import { NOMBRE_PLANETA, COLOR_PLANETA } from "./misiones.js";
import { barraNavegacion } from "./navegacion.js";

const fmt = (x, d = 0) => x.toLocaleString("es-CL", { minimumFractionDigits: d, maximumFractionDigits: d });
const sg = (x, d = 2) => (x >= 0 ? "+" : "−") + fmt(Math.abs(x), d);
const RAD = Math.PI / 180, PLAN = ["199", "299", "399", "499", "599", "699", "799", "899"];

export async function iniciarAsistencias() {
  const raiz = document.getElementById("app");
  const cab = document.createElement("header"); cab.className = "cabecera"; cab.innerHTML = "<h1>Asistencias gravitatorias</h1>"; cab.appendChild(barraNavegacion("asistencias")); document.body.insertBefore(cab, raiz);
  raiz.className = "app";
  raiz.innerHTML = `
    <section class="escena" aria-label="Geometría de la asistencia" style="display:flex;flex-direction:column">
      <div style="position:relative;flex:1 1 0;min-height:0"><canvas id="cPlan" style="position:absolute;inset:0;width:100%;height:100%" aria-label="Trayectoria de la nave respecto del planeta, una hipérbola, con el planeta a escala y las velocidades de entrada y salida."></canvas>
        <div class="hud"><div class="fecha" id="titulo"></div><div class="sub" id="sub"></div></div>
        <div class="cargando" id="cargando"><div>Cargando planetas y encuentros reales…</div><progress id="prog" max="1" value="0"></progress></div></div>
      <div style="position:relative;flex:1 1 0;min-height:0;border-top:1px solid var(--borde)"><canvas id="cSol" style="position:absolute;inset:0;width:100%;height:100%" aria-label="Diagrama de velocidades respecto del Sol: velocidad del planeta más la de la nave antes y después del encuentro."></canvas></div>
    </section>
    <aside class="lateral" aria-label="Controles y resultados">
      <h2>Caso real</h2><select id="sCaso" aria-label="Cargar un encuentro real" style="width:100%"></select>
      <h2>Parámetros</h2>
      <div class="ficha" style="display:grid;gap:8px">
        <label class="etq" for="sPlan">Planeta</label><select id="sPlan"></select>
        <label class="etq" for="rVinf">Velocidad en el infinito v∞: <b id="oVinf"></b></label><input type="range" id="rVinf" min="1" max="30" step="0.1" value="10">
        <label class="etq" for="rAlt">Altura del paso (periastro): <b id="oAlt"></b></label><input type="range" id="rAlt" min="0" max="1000" step="1" value="300">
        <label class="etq" for="rTheta">Ángulo de llegada θ (entre v∞ y la velocidad del planeta): <b id="oTheta"></b></label><input type="range" id="rTheta" min="0" max="180" step="0.5" value="90">
        <label class="etq" for="rGamma">Hacia dónde gira γ (0° y ±180° en el plano; ±90° fuera de él): <b id="oGamma"></b></label><input type="range" id="rGamma" min="-180" max="180" step="1" value="0">
        <label class="etq" for="iFecha">Fecha (fija la velocidad real del planeta)</label><input type="date" id="iFecha" value="2030-01-01" min="1970-01-01" max="2050-12-31">
        <div style="display:flex;gap:6px;flex-wrap:wrap"><button id="bMax">Máxima ganancia</button><button id="bMin">Máximo frenado</button></div>
      </div>
      <h2>Resultado</h2><dl class="datos" id="res"></dl>
      <div class="aviso" id="aviso" aria-live="polite"></div>
      <details><summary>Cómo funciona</summary><div class="aviso" id="meta"></div></details>
      <p class="aviso">Documentación: <a href="documentacion/README.html">documentación de los simuladores</a>.</p>
    </aside>`;
  const $ = (i) => document.getElementById(i);
  let ph, EN;
  try { const p = [0, 0], pr = () => { $("prog").value = (p[0] + p[1]) / 2; }; [ph, EN] = await Promise.all([cargarSistema("planetas_hist", "datos", (f) => { p[0] = f; pr(); }), fetch("datos/encuentros.json").then((r) => { if (!r.ok) throw new Error("encuentros.json " + r.status); return r.json(); }).then((j) => { p[1] = 1; pr(); return j; })]); }
  catch (e) { $("cargando").classList.add("error"); $("cargando").innerHTML = `<div><strong>No se pudieron cargar los datos.</strong></div><div>${e.message}</div><small>Abra el sitio publicado en GitHub Pages o sirva la carpeta con <code>python -m http.server</code>.</small>`; return; }
  $("cargando").remove();
  const reales = EN.encuentros.filter((e) => !e.orbita && e.vh_out && PLAN.includes(e.planeta));
  $("sPlan").innerHTML = PLAN.map((i) => `<option value="${i}">${NOMBRE_PLANETA[i]}</option>`).join("");
  $("sCaso").innerHTML = `<option value="">Personalizado</option>` + reales.map((e, i) => `<option value="${i}">${e.nombre} · ${NOMBRE_PLANETA[e.planeta]} · ${formatoUtc(jdUtcDesdeTdb(e.jd_ca), false).slice(0, 10)} (${sg(e.dv_helio, 1)} km/s)</option>`).join("");
  const S = { planeta: "599", vinf: 10, rpR: 4, theta: 90 * RAD, gamma: 0, jd: jdTdbDesdeUtc(jdUtcDesdeInput("2030-01-01T00:00")), caso: null };
  const R = () => EN.radio_km[S.planeta], MU = () => EN.gm_km3_s2[S.planeta], Vp = () => Math.hypot(...ph.cuerpo(S.planeta).vel(S.jd));
  const rpKm = () => S.rpR * R();
  // el deslizador de altura es logarítmico: rp/R de 1,001 a 60
  const sliderDeRp = (rpR) => Math.round(1000 * Math.log(rpR / 1.001) / Math.log(60 / 1.001));
  const rpRDeSlider = (v) => 1.001 * Math.pow(60 / 1.001, v / 1000);

  function leerControles() { S.vinf = +$("rVinf").value; S.rpR = rpRDeSlider(+$("rAlt").value); S.theta = +$("rTheta").value * RAD; S.gamma = +$("rGamma").value * RAD; }
  function escribirControles() { $("sPlan").value = S.planeta; $("rVinf").value = Math.min(30, S.vinf); $("rAlt").value = sliderDeRp(Math.min(60, Math.max(1.001, S.rpR))); $("rTheta").value = (S.theta / RAD).toFixed(1); $("rGamma").value = Math.round(S.gamma / RAD); }
  function cargarCaso(i) {
    if (i === "") { S.caso = null; $("iFecha").disabled = false; calcular(); return; }
    const e = reales[+i]; S.caso = e; S.planeta = e.planeta; S.jd = e.jd_ca; $("iFecha").value = formatoUtc(jdUtcDesdeTdb(e.jd_ca), false).slice(0, 10); $("iFecha").disabled = true;
    const d = desdeEncuentro(e, MU(), Vp()); S.vinf = e.vinf_kms; S.rpR = e.dist_km / R(); S.theta = d.theta; S.gamma = d.gamma; escribirControles(); calcular();
  }
  let r = null;
  function calcular() {
    leerControles(); const rp = rpKm(), Vpl = Vp(); r = asistencia(MU(), S.vinf, rp, Vpl, S.theta, S.gamma);
    $("oVinf").textContent = `${fmt(S.vinf, 1)} km/s`; $("oAlt").textContent = `${fmt(rp - R(), 0)} km (${fmt(S.rpR, 2)} radios del centro)`; $("oTheta").textContent = `${fmt(S.theta / RAD, 1)}°`; $("oGamma").textContent = `${fmt(S.gamma / RAD, 0)}°`;
    const d = r.dv, color = d > 0.3 ? "#7ee0a1" : d < -0.3 ? "#ff8a8a" : "#e6ecf8";
    $("res").innerHTML = `<dt>Velocidad del planeta</dt><dd>${fmt(Vpl, 2)} km/s</dd><dt>Excentricidad e</dt><dd>${fmt(r.e, 3)}</dd><dt>Giro de v∞ (2·asin 1/e)</dt><dd>${fmt(r.delta / RAD, 1)}°</dd><dt>Velocidad en el periastro</dt><dd>${fmt(r.vperi, 2)} km/s</dd><dt>Velocidad respecto del Sol: antes</dt><dd>${fmt(r.vhIn, 2)} km/s</dd><dt>Velocidad respecto del Sol: después</dt><dd>${fmt(r.vhOut, 2)} km/s</dd><dt>Cambio de velocidad</dt><dd style="color:${color};font-weight:650">${sg(d)} km/s</dd><dt>Cambio máximo posible (2·v∞·sin δ/2)</dt><dd>${fmt(2 * S.vinf * Math.sin(r.delta / 2), 2)} km/s</dd>`;
    const av = []; if (rp < R() * 1.0005) av.push("La nave chocaría con el planeta: el periastro debe quedar por encima de la superficie (y de su atmósfera)."); if (S.caso) av.push(`Caso real: ${S.caso.nombre} en ${NOMBRE_PLANETA[S.caso.planeta]} (${formatoUtc(jdUtcDesdeTdb(S.caso.jd_ca), false).slice(0, 10)}): Horizons da ${sg(S.caso.dv_helio)} km/s; el modelo reproduce ${sg(r.dv)} km/s.`);
    if (r.hin[2] !== 0 || r.hout[2] !== 0) av.push(`Componente fuera del plano de la órbita del planeta: ${sg(r.hout[2] - r.hin[2], 1)} km/s (cambia la inclinación).`);
    $("aviso").innerHTML = av.join("<br>");
    $("titulo").textContent = `Asistencia en ${NOMBRE_PLANETA[S.planeta]}`; $("sub").textContent = S.caso ? `${S.caso.nombre} · ${formatoUtc(jdUtcDesdeTdb(S.caso.jd_ca), false).slice(0, 10)}` : `v∞ ${fmt(S.vinf, 1)} km/s · altura ${fmt(rp - R(), 0)} km`;
  }
  function optimizar(signo) {
    leerControles(); let mejor = null; for (let a = 0; a <= 180; a += 1) for (let g = -180; g < 180; g += 2) { const q = asistencia(MU(), S.vinf, rpKm(), Vp(), a * RAD, g * RAD); if (!mejor || signo * q.dv > signo * mejor.q.dv) mejor = { a, g, q }; }
    S.theta = mejor.a * RAD; S.gamma = mejor.g * RAD; $("sCaso").value = ""; S.caso = null; $("iFecha").disabled = false; escribirControles(); calcular();
  }
  for (const id of ["rVinf", "rAlt", "rTheta", "rGamma"]) $(id).addEventListener("input", () => { $("sCaso").value = ""; S.caso = null; $("iFecha").disabled = false; calcular(); });
  $("sPlan").onchange = () => { S.planeta = $("sPlan").value; $("sCaso").value = ""; S.caso = null; $("iFecha").disabled = false; calcular(); };
  $("iFecha").onchange = () => { const j = jdUtcDesdeInput($("iFecha").value + "T00:00"); if (j) { S.jd = jdTdbDesdeUtc(j); calcular(); } };
  $("sCaso").onchange = () => cargarCaso($("sCaso").value); $("bMax").onclick = () => optimizar(1); $("bMin").onclick = () => optimizar(-1);

  function cajas(cv) { const dpr = Math.min(2, devicePixelRatio || 1), W = cv.clientWidth, H = cv.clientHeight; if (cv.width !== Math.round(W * dpr) || cv.height !== Math.round(H * dpr)) { cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr); } const c = cv.getContext("2d"); c.setTransform(dpr, 0, 0, dpr, 0, 0); return [c, W, H]; }
  const flecha = (c, x0, y0, x1, y1, col, w = 2) => { c.strokeStyle = col; c.fillStyle = col; c.lineWidth = w; c.beginPath(); c.moveTo(x0, y0); c.lineTo(x1, y1); c.stroke(); const a = Math.atan2(y1 - y0, x1 - x0); c.beginPath(); c.moveTo(x1, y1); c.lineTo(x1 - 9 * Math.cos(a - 0.4), y1 - 9 * Math.sin(a - 0.4)); c.lineTo(x1 - 9 * Math.cos(a + 0.4), y1 - 9 * Math.sin(a + 0.4)); c.fill(); };
  function dibujarPlaneta(t) {
    const [c, W, H] = cajas($("cPlan")); c.fillStyle = "#02030a"; c.fillRect(0, 0, W, H); if (!r) return; c.textBaseline = "middle";
    const rp = rpKm(), e = r.e, a = -r.a, b = a * Math.sqrt(e * e - 1), th = Math.acos(-1 / e), vista = Math.max(rp * 3, R() * 2.6), cx = W * 0.42, cy = H * 0.52, k = Math.min(W * 0.4, H * 0.42) / vista;
    const Q = (x, y) => [cx - x * k, cy - y * k];                      // x hacia el periastro (a la izquierda del planeta), y en el sentido del movimiento (hacia arriba)
    const Hm = Math.acosh(Math.max(1.0001, (1.0 * vista / a + 1) / e)), en = (Hh) => Q(a * (e - Math.cosh(Hh)), b * Math.sinh(Hh));
    c.strokeStyle = "rgba(125,147,192,0.2)"; c.lineWidth = 1; for (const f of [2, 4, 6]) { c.beginPath(); c.arc(cx, cy, rp * f * k, 0, 7); c.stroke(); }
    c.fillStyle = COLOR_PLANETA[S.planeta]; c.beginPath(); c.arc(cx, cy, Math.max(3, R() * k), 0, 7); c.fill();
    c.strokeStyle = "#fff"; c.lineWidth = 2.2; c.beginPath(); for (let i = -80; i <= 80; i++) { const p = en(Hm * i / 80); if (i === -80) c.moveTo(p[0], p[1]); else c.lineTo(p[0], p[1]); } c.stroke();
    // v∞ de entrada y de salida (direcciones de la velocidad en las asíntotas, v ∝ (−sin θ, e + cos θ), en pantalla con x e y invertidos)
    const n = Math.hypot(Math.sin(th), e - 1 / e), vIn = [-Math.sin(th) / n, -(e - 1 / e) / n], vOut = [Math.sin(th) / n, -(e - 1 / e) / n], Lf = Math.min(W, H) * 0.2, pI = en(-Hm), pO = en(Hm);
    flecha(c, pI[0], pI[1], pI[0] + vIn[0] * Lf, pI[1] + vIn[1] * Lf, "#6cb4ff", 2.4); flecha(c, pO[0] - vOut[0] * Lf, pO[1] - vOut[1] * Lf, pO[0], pO[1], "#7ee0a1", 2.4);
    c.font = "12px system-ui,sans-serif"; c.textAlign = "left"; c.fillStyle = "#6cb4ff"; c.fillText(`v∞ de entrada ${fmt(S.vinf, 1)} km/s`, Math.min(W - 170, pI[0] + 12), Math.min(H - 24, pI[1] - 2));
    c.fillStyle = "#7ee0a1"; c.fillText("v∞ de salida (igual módulo, girada)", Math.min(W - 230, Math.max(8, pO[0] + 12)), Math.max(40, pO[1] + 6));
    const pp = Q(rp, 0); c.strokeStyle = "#ffd45e"; c.lineWidth = 1.4; c.beginPath(); c.arc(pp[0], pp[1], 4.5, 0, 7); c.stroke(); c.fillStyle = "#ffd45e"; c.textAlign = "right"; c.fillText(`periastro: ${fmt(rp - R(), 0)} km de altura`, pp[0] - 10, pp[1] - 14);
    // la nave recorre la hipérbola con la ley de Kepler (anomalía media uniforme)
    const Mmax = e * Math.sinh(Hm) - Hm, M = (2 * ((t / 7000) % 1) - 1) * Mmax; let Hh = Math.asinh(M / e); for (let i = 0; i < 40; i++) Hh -= (e * Math.sinh(Hh) - Hh - M) / (e * Math.cosh(Hh) - 1);
    const ps = en(Hh); c.fillStyle = "#fff"; c.beginPath(); c.arc(ps[0], ps[1], 5, 0, 7); c.fill();
    c.fillStyle = "#9fb0cf"; c.textAlign = "right"; c.fillText(`en el sistema del planeta · giro ${fmt(r.delta / RAD, 1)}° · e = ${fmt(e, 2)} · vista de ${fmt(2 * vista / 1000, 0)} mil km`, W - 10, 14);
  }
  function dibujarSol() {
    const [c, W, H] = cajas($("cSol")); c.fillStyle = "#070a14"; c.fillRect(0, 0, W, H); if (!r) return; c.textBaseline = "middle";
    const Vpl = Math.hypot(...[0, r.hin[1] - r.vin[1]]), maxv = Math.max(r.vhIn, r.vhOut, Vpl + S.vinf) * 1.05, k = Math.min((W - 80) / 2, (H - 40)) / maxv, ox = W * 0.5, oy = H - 22;
    const T = (v) => [ox + v[0] * k, oy - v[1] * k];
    for (const rad of [r.vhIn]) { c.strokeStyle = "rgba(255,255,255,0.35)"; c.setLineDash([4, 5]); c.lineWidth = 1; c.beginPath(); c.arc(ox, oy, rad * k, Math.PI, 2 * Math.PI); c.stroke(); c.setLineDash([]); }
    const pT = T([0, Vpl]); c.strokeStyle = "rgba(125,147,192,0.5)"; c.lineWidth = 1; c.beginPath(); c.arc(pT[0], pT[1], S.vinf * k, 0, 7); c.stroke();
    flecha(c, ox, oy, pT[0], pT[1], COLOR_PLANETA[S.planeta], 2.4);
    const a = T(r.hin), b = T(r.hout); flecha(c, pT[0], pT[1], a[0], a[1], "#6cb4ff", 1.8); flecha(c, pT[0], pT[1], b[0], b[1], "#7ee0a1", 1.8);
    flecha(c, ox, oy, a[0], a[1], "#6cb4ff", 3); flecha(c, ox, oy, b[0], b[1], r.dv >= 0 ? "#7ee0a1" : "#ff8a8a", 3);
    c.font = "12px system-ui,sans-serif"; c.textAlign = "left"; c.fillStyle = COLOR_PLANETA[S.planeta]; c.textAlign = "right"; c.fillText(`velocidad del planeta ${fmt(Vpl, 1)} km/s`, ox - 10, (oy + pT[1]) / 2); c.textAlign = "left";
    c.fillStyle = "#6cb4ff"; c.fillText(`antes ${fmt(r.vhIn, 2)} km/s`, Math.min(W - 130, a[0] + 8), a[1] - 8); c.fillStyle = r.dv >= 0 ? "#7ee0a1" : "#ff8a8a"; c.fillText(`después ${fmt(r.vhOut, 2)} km/s (${sg(r.dv)})`, Math.min(W - 190, b[0] + 8), b[1] + 12);
    c.fillStyle = "#9fb0cf"; c.textAlign = "right"; c.fillText("en el sistema del Sol (proyección en el plano de la órbita del planeta) · la circunferencia es el lugar de las salidas posibles", W - 10, 14);
  }
  $("meta").innerHTML = `<p>Método de las <b>cónicas empalmadas</b>: dentro de la esfera de influencia sólo actúa el planeta y la nave describe una hipérbola de excentricidad e = 1 + r<sub>p</sub>·v∞²/μ; su velocidad en el infinito v∞ conserva el módulo y gira 2·asin(1/e). En el sistema del Sol la velocidad es la del planeta más v∞, y el giro cambia su módulo: pasar por <i>detrás</i> del planeta (respecto de su movimiento) acelera la nave y por <i>delante</i> la frena; el cambio máximo de velocidad es 2·v∞·sin(δ/2). Los casos reales salen de <code>datos/encuentros.json</code> (Horizons) y el modelo los reproduce con error inferior a 0,001 km/s. La velocidad del planeta es la real a la fecha indicada (efemérides de JPL, 1970–2050). No modela la gravedad del Sol durante el encuentro, el aplanamiento del planeta, su atmósfera ni las maniobras de la nave.</p>`;
  escribirControles(); { const i0 = String(Math.max(0, reales.findIndex((e) => e.nombre === "Voyager 2" && e.planeta === "599"))); $("sCaso").value = i0; cargarCaso(i0); }
  (function cuadro(t) { dibujarPlaneta(t); dibujarSol(); requestAnimationFrame(cuadro); })(0);
  window.__asi = { S, reales, calcular };
}
