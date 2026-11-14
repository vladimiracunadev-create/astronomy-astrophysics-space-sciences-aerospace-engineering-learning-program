// SPDX-License-Identifier: Apache-2.0
// Calendario planetario 2027–2050: oposiciones, conjunciones, cuadraturas, máximas elongaciones y estacionarios con la geometría Sol–Tierra–planeta.
import { cargarSistema } from "./efemerides.js";
import { UA_KM, C_KM_S } from "./cuerpos.js";
import { JD_UTC_INICIO, JD_UTC_FIN, jdTdbDesdeUtc, jdUtcDesdeTdb, formatoUtc } from "./tiempo.js";
import { crearCalendario, PLANETAS_CAL, NOMBRE, COLOR, TIPOS } from "./calendario.js";
import { barraNavegacion } from "./navegacion.js";

const fmt = (x, d = 0) => x.toLocaleString("es-CL", { minimumFractionDigits: d, maximumFractionDigits: d });
const RAD = Math.PI / 180;
const VEL = [["1 día / s", 1], ["10 días / s", 10], ["30 días / s", 30], ["100 días / s", 100], ["1 año / s", 365.25]];
const GRUPOS = [["oposicion", "Oposiciones", ["oposicion"]], ["conj", "Conjunciones con el Sol", ["conj_sup", "conj_inf", "conjuncion"]], ["cuad", "Cuadraturas", ["cuad_este", "cuad_oeste"]], ["elong", "Máximas elongaciones", ["elong_este", "elong_oeste"]], ["est", "Estacionarios (retrógrados)", ["est_retro", "est_directo"]], ["pp", "Conjunciones entre planetas", ["conj_planetas"]]];
const MARCA = { oposicion: "#ffd45e", conj_sup: "#c9d3ea", conj_inf: "#c9d3ea", conjuncion: "#c9d3ea", cuad_este: "#7ee0a1", cuad_oeste: "#7ee0a1", elong_este: "#6cb4ff", elong_oeste: "#6cb4ff", est_retro: "#ff8a8a", est_directo: "#ff8a8a", conj_planetas: "#d9a0ff" };
const AYUDA = {
  oposicion: "La Tierra pasa entre el Sol y el planeta: está en el cielo toda la noche, en su mayor tamaño y brillo. Es el mejor momento para observarlo.",
  conjuncion: "El planeta está detrás del Sol visto desde la Tierra: no se puede observar.",
  conj_sup: "El planeta pasa detrás del Sol: no es visible (pasa de la tarde a la mañana… o al revés: del cielo de la mañana al de la tarde).",
  conj_inf: "El planeta pasa entre la Tierra y el Sol: no es visible; cambia del cielo vespertino al matutino y está en su mayor cercanía.",
  cuad_este: "El planeta está a 90° al este del Sol: visible en la primera mitad de la noche.", cuad_oeste: "El planeta está a 90° al oeste del Sol: visible en la segunda mitad de la noche y al amanecer.",
  elong_este: "Mayor separación aparente al este del Sol: la mejor ocasión para verlo en el cielo del atardecer.", elong_oeste: "Mayor separación aparente al oeste del Sol: la mejor ocasión para verlo antes del amanecer.",
  est_retro: "Su longitud aparente deja de crecer: empieza el movimiento retrógrado (el planeta parece volver atrás sobre las estrellas).", est_directo: "Su longitud aparente vuelve a crecer: termina el movimiento retrógrado.",
  conj_planetas: "Los dos planetas tienen la misma longitud eclíptica vista desde la Tierra (la separación en latitud se indica).",
};
const fecha = (e) => formatoUtc(e.jdUtc, false);
const etiquetaPlaneta = (e) => (e.planeta2 ? `${NOMBRE[e.planeta]}–${NOMBRE[e.planeta2]}` : NOMBRE[e.planeta]);

export async function iniciarCalendario() {
  const raiz = document.getElementById("app");
  const cab = document.createElement("header"); cab.className = "cabecera"; cab.innerHTML = "<h1>Calendario planetario</h1>"; cab.appendChild(barraNavegacion("calendario")); document.body.insertBefore(cab, raiz);
  raiz.className = "app";
  raiz.innerHTML = `
    <section class="escena" aria-label="Geometría Sol–Tierra–planeta" style="display:flex;flex-direction:column">
      <div style="position:relative;flex:1 1 auto;min-height:0"><canvas id="mapa" tabindex="0" style="position:absolute;inset:0;width:100%;height:100%" aria-label="Sistema Solar visto desde el polo norte eclíptico con la línea de visión de la Tierra al Sol y al planeta del fenómeno seleccionado."></canvas>
        <div class="hud"><div class="fecha" id="fecha"></div><div class="sub" id="sub"></div></div>
        <div class="cargando" id="cargando"><div>Calculando 24 años de fenómenos con las efemérides de JPL…</div><progress id="prog" max="1" value="0"></progress></div></div>
      <div style="position:relative;flex:0 0 150px;border-top:1px solid var(--borde)"><canvas id="serie" style="position:absolute;inset:0;width:100%;height:100%;cursor:pointer" aria-label="Elongación del planeta respecto del Sol (longitud eclíptica menos la del Sol) de 2027 a 2050, con los fenómenos marcados. Clic para ir a esa fecha."></canvas></div>
      <div class="barra" style="position:relative;flex:0 0 auto;border-top:1px solid var(--borde)"><div class="grupo" role="group" aria-label="Control del tiempo">
          <button id="bIni" aria-label="Ir al inicio (2027)" title="Inicio">⏮</button><button id="bAnt" aria-label="Fenómeno anterior" title="Fenómeno anterior de la lista">⏪</button>
          <button id="bPlay" aria-label="Reproducir" title="Reproducir / pausar (espacio)" style="min-width:48px">▶</button>
          <button id="bSig" aria-label="Fenómeno siguiente" title="Fenómeno siguiente de la lista">⏩</button><button id="bFin" aria-label="Ir al final (2050)" title="Final">⏭</button></div>
        <div class="grupo"><label class="etq" for="sVel">Velocidad</label><select id="sVel"></select></div>
        <div class="grupo"><label class="etq" for="sEnc">Encuadre</label><select id="sEnc"><option value="0">Automático</option><option value="1.8">Hasta Marte</option><option value="6">Hasta Júpiter</option><option value="32">Hasta Neptuno</option></select></div></div>
    </section>
    <aside class="lateral" aria-label="Fenómenos y filtros">
      <h2>Fenómeno seleccionado</h2><div class="ficha" id="ficha" aria-live="polite"><span class="etq">Elija un fenómeno de la lista.</span></div>
      <h2>Filtros</h2>
      <div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center"><label class="etq" for="sAnio">Año</label><select id="sAnio"></select><label class="etq" for="sPlan">Planeta</label><select id="sPlan"></select></div>
      <div id="tipos" style="display:flex;flex-wrap:wrap;gap:4px 12px;margin-top:8px"></div>
      <h2>Fenómenos <small id="cuenta" style="color:var(--suave);font-weight:400"></small></h2>
      <div class="lista" id="lista" style="max-height:300px"></div>
      <div style="margin-top:6px"><button id="bCsv">Descargar la lista (CSV)</button></div>
      <details><summary>Cómo se calcula y límites</summary><div class="aviso" id="meta"></div></details>
      <p class="aviso">Documentación: <a href="documentacion/README.html">documentación de los simuladores</a>.</p>
    </aside>`;
  const $ = (i) => document.getElementById(i);
  let sol;
  try { sol = await cargarSistema("sol", "datos", (f) => { $("prog").value = f; }); }
  catch (e) { $("cargando").classList.add("error"); $("cargando").innerHTML = `<div><strong>No se pudieron cargar los datos.</strong></div><div>${e.message}</div><small>Abra el sitio publicado en GitHub Pages o sirva la carpeta con <code>python -m http.server</code>.</small>`; return; }
  await new Promise((r) => setTimeout(r, 30));
  const cal = crearCalendario(sol), J0 = jdTdbDesdeUtc(JD_UTC_INICIO), J1 = jdTdbDesdeUtc(JD_UTC_FIN);
  const TODOS = cal.todos(J0, J1);
  $("cargando").remove();
  const planetas = new Map(["199", "299", "399", "499", "599", "699", "799", "899"].map((i) => [i, sol.cuerpo(i)]));
  let jd = J0, jugando = false, velocidad = 1, sel = null, lista = [], planetaSerie = "499", rvista = 2, tprev = 0, dtFrame = 0, serieGeom = null;
  const activos = new Set(GRUPOS.map((g) => g[0]).filter((k) => k !== "est"));
  const tmp = [0, 0, 0];

  // ---------- filtros y lista
  $("sAnio").innerHTML = `<option value="0">2027–2050</option>` + Array.from({ length: 24 }, (_, i) => `<option value="${2027 + i}">${2027 + i}</option>`).join("");
  $("sPlan").innerHTML = `<option value="">Todos</option>` + PLANETAS_CAL.map((p) => `<option value="${p}">${NOMBRE[p]}</option>`).join("");
  $("tipos").innerHTML = GRUPOS.map(([k, n]) => `<label class="chk"><input type="checkbox" data-g="${k}" ${activos.has(k) ? "checked" : ""}> ${n}</label>`).join("");
  function filtrar() {
    const anio = +$("sAnio").value, pl = $("sPlan").value, tipos = new Set(GRUPOS.filter((g) => activos.has(g[0])).flatMap((g) => g[2]));
    lista = TODOS.filter((e) => tipos.has(e.tipo) && (!pl || e.planeta === pl || e.planeta2 === pl) && (!anio || new Date((e.jdUtc - 2440587.5) * 864e5).getUTCFullYear() === anio));
    $("cuenta").textContent = `(${lista.length})`;
    const mostrar = lista.slice(0, 500);
    $("lista").innerHTML = mostrar.map((e, i) => `<button data-i="${i}"><span><span style="color:${MARCA[e.tipo]}">●</span> ${fecha(e).slice(0, 16)} · ${etiquetaPlaneta(e)}</span><small>${e.planeta2 ? "conjunción" : TIPOS[e.tipo].replace("Conjunción con el Sol", "conj. con el Sol").replace("Estacionario: ", "est. ")}</small></button>`).join("") + (lista.length > 500 ? `<div class="aviso" style="padding:6px">Se muestran los primeros 500 de ${lista.length}: acote por año o planeta.</div>` : "") || `<div class="aviso" style="padding:8px">Ningún fenómeno con estos filtros.</div>`;
    for (const b of $("lista").querySelectorAll("button")) b.setAttribute("aria-current", String(lista[+b.dataset.i] === sel));
    dibujarSerie();
  }
  $("tipos").addEventListener("change", (e) => { const k = e.target.dataset.g; if (e.target.checked) activos.add(k); else activos.delete(k); filtrar(); });
  $("sAnio").onchange = filtrar; $("sPlan").onchange = () => { if ($("sPlan").value) planetaSerie = $("sPlan").value; filtrar(); };

  // ---------- selección
  function seleccionar(e, mover = true) {
    sel = e; if (!e) return; planetaSerie = e.planeta; if (mover) jd = e.jdTdb;
    const ayuda = AYUDA[e.tipo], c = e.planeta2 ? null : cal.geo(e.planeta, e.jdTdb, {});
    const filas = e.planeta2
      ? [["Planetas", `${NOMBRE[e.planeta]} y ${NOMBRE[e.planeta2]}`], ["Separación", `${fmt(e.sep_grados, 2)}°`], ["Elongación al Sol del más cercano a él", `${fmt(e.elong, 0)}°`]]
      : [["Planeta", NOMBRE[e.planeta]], ["Elongación al Sol", `${fmt(e.elong, 1)}°`], ["Distancia a la Tierra", `${fmt(e.dist_ua, 3)} UA`], ["Luz tarda", `${e.dist_ua * UA_KM / C_KM_S > 3600 ? fmt(e.dist_ua * UA_KM / C_KM_S / 3600, 2) + " h" : fmt(e.dist_ua * UA_KM / C_KM_S / 60, 1) + " min"}`]];
    $("ficha").innerHTML = `<h3 style="color:${MARCA[e.tipo]}">${e.planeta2 ? "Conjunción entre planetas" : TIPOS[e.tipo]}</h3><div class="etq">${fecha(e)}</div><dl class="datos">${filas.map(([k, v]) => `<dt>${k}</dt><dd>${v}</dd>`).join("")}</dl><p style="margin:8px 0 0;font-size:.86rem">${ayuda}${e.planeta2 && e.elong < 15 ? " <b>Está muy cerca del Sol: probablemente no se pueda observar.</b>" : ""}</p>`;
    void c; for (const b of $("lista").querySelectorAll("button")) b.setAttribute("aria-current", String(lista[+b.dataset.i] === e));
    dibujarSerie();
  }
  $("lista").addEventListener("click", (ev) => { const b = ev.target.closest("button"); if (b) seleccionar(lista[+b.dataset.i]); });
  const vecino = (dir) => dir > 0 ? lista.find((e) => e.jdTdb > jd + 0.01) : [...lista].reverse().find((e) => e.jdTdb < jd - 0.01);
  $("bSig").onclick = () => { const e = vecino(1); if (e) seleccionar(e); }; $("bAnt").onclick = () => { const e = vecino(-1); if (e) seleccionar(e); };
  $("bIni").onclick = () => { jd = J0; }; $("bFin").onclick = () => { jd = J1; };
  $("sVel").innerHTML = VEL.map(([t, v]) => `<option value="${v}">${t}</option>`).join(""); $("sVel").onchange = () => { velocidad = +$("sVel").value; };
  const play = () => { jugando = !jugando; $("bPlay").textContent = jugando ? "⏸" : "▶"; $("bPlay").setAttribute("aria-label", jugando ? "Pausar" : "Reproducir"); if (jugando && jd >= J1 - 1) jd = J0; };
  $("bPlay").onclick = play; addEventListener("keydown", (e) => { if (/INPUT|SELECT|TEXTAREA/.test(document.activeElement.tagName)) return; if (e.code === "Space") { e.preventDefault(); play(); } });
  $("bCsv").onclick = () => {
    const filas = [["fecha_utc", "fenomeno", "planeta", "planeta2", "elongacion_grados", "distancia_tierra_ua", "separacion_grados"]].concat(lista.map((e) => [fecha(e), TIPOS[e.tipo], NOMBRE[e.planeta], e.planeta2 ? NOMBRE[e.planeta2] : "", e.elong.toFixed(2), e.planeta2 ? "" : e.dist_ua.toFixed(4), e.planeta2 ? e.sep_grados.toFixed(3) : ""]));
    const url = URL.createObjectURL(new Blob(["﻿" + filas.map((r) => r.join(";")).join("\n")], { type: "text/csv;charset=utf-8" })), a = document.createElement("a");
    a.href = url; a.download = "calendario_planetario.csv"; a.click(); setTimeout(() => URL.revokeObjectURL(url), 2000);
  };

  // ---------- diagrama cenital
  function cajas(cv) { const dpr = Math.min(2, devicePixelRatio || 1), W = cv.clientWidth, H = cv.clientHeight; if (cv.width !== Math.round(W * dpr) || cv.height !== Math.round(H * dpr)) { cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr); } const c = cv.getContext("2d"); c.setTransform(dpr, 0, 0, dpr, 0, 0); return [c, W, H]; }
  const SEMIEJE = { "199": 0.387, "299": 0.723, "399": 1, "499": 1.524, "599": 5.203, "699": 9.537, "799": 19.19, "899": 30.07 };
  function dibujarMapa() {
    const [c, W, H] = cajas($("mapa")); c.fillStyle = "#02030a"; c.fillRect(0, 0, W, H);
    const fijo = +$("sEnc").value, objetivo = fijo || Math.max(1.7, (SEMIEJE[planetaSerie] || 1.5) * 1.18 + 0.1);
    rvista += (objetivo - rvista) * (1 - Math.exp(-dtFrame / 0.4));
    const cx = W / 2, cy = H / 2 + 6, R = Math.min(W / 2 - 20, H / 2 - 24), k = R / rvista;   // px por UA (escala lineal: los ángulos son los reales)
    const P = (v) => [cx + v[0] / UA_KM * k, cy - v[1] / UA_KM * k];
    c.font = "11px system-ui,sans-serif"; c.textBaseline = "middle";
    for (const id of Object.keys(SEMIEJE)) { const r = SEMIEJE[id] * k; if (r > R * 1.5) continue; c.strokeStyle = "rgba(125,147,192,0.25)"; c.setLineDash([3, 5]); c.beginPath(); c.arc(cx, cy, r, 0, 7); c.stroke(); } c.setLineDash([]);
    const E = planetas.get("399").pos(jd, [0, 0, 0]), pe = P(E);
    const a = sel || { planeta: planetaSerie };
    const objs = a.planeta2 ? [a.planeta, a.planeta2] : [a.planeta];
    // líneas de visión desde la Tierra: al Sol y a cada planeta del fenómeno, con el arco de la elongación
    const rayo = (to, col, ext) => { const dx = to[0] - pe[0], dy = to[1] - pe[1], n = Math.hypot(dx, dy) || 1; c.strokeStyle = col; c.lineWidth = 1.4; c.beginPath(); c.moveTo(pe[0], pe[1]); c.lineTo(pe[0] + dx / n * (n + ext), pe[1] + dy / n * (n + ext)); c.stroke(); return Math.atan2(dy, dx); };
    const aSol = rayo([cx, cy], "rgba(255,212,94,0.8)", 0);
    objs.forEach((id, i) => { const p = P(planetas.get(id).pos(jd, tmp)), aP = rayo(p, COLOR[id], 400 * (i + 1)); let d = aP - aSol; while (d > Math.PI) d -= 2 * Math.PI; while (d < -Math.PI) d += 2 * Math.PI; c.strokeStyle = COLOR[id]; c.lineWidth = 1.6; c.beginPath(); c.arc(pe[0], pe[1], 26 + 8 * i, aSol, aSol + d, d < 0); c.stroke(); const m = aSol + d / 2; c.fillStyle = COLOR[id]; c.textAlign = "center"; c.fillText(`${fmt(Math.abs(cal.elongacion(id, jd) / RAD), 1)}°`, pe[0] + Math.cos(m) * (44 + 8 * i), pe[1] + Math.sin(m) * (44 + 8 * i)); });
    c.fillStyle = "#ffd45e"; c.beginPath(); c.arc(cx, cy, 7, 0, 7); c.fill(); c.fillStyle = "rgba(255,212,94,0.2)"; c.beginPath(); c.arc(cx, cy, 14, 0, 7); c.fill();
    for (const id of ["199", "299", "399", "499", "599", "699", "799", "899"]) { const p = P(id === "399" ? E : planetas.get(id).pos(jd, tmp)); if (Math.hypot(p[0] - cx, p[1] - cy) > R * 1.5) continue; const resalta = objs.includes(id) || id === "399"; c.fillStyle = COLOR[id]; c.beginPath(); c.arc(p[0], p[1], resalta ? 5.5 : 3.6, 0, 7); c.fill(); c.fillStyle = resalta ? "#fff" : "#9fb0cf"; c.textAlign = "left"; c.fillText(NOMBRE[id] || "Tierra", p[0] + 8, p[1] - 7); }
    c.fillStyle = "#5a9bf0"; c.textAlign = "left"; c.fillText("Tierra", pe[0] + 8, pe[1] - 7);
    c.fillStyle = "#8fa0c0"; c.textAlign = "right"; c.fillText("vista desde el polo norte eclíptico · escala lineal", W - 10, H - 10);
  }

  // ---------- serie temporal: longitud del planeta menos la del Sol
  let cache = { id: null, y: null };
  function dibujarSerie() {
    const [c, W, H] = cajas($("serie")), x0 = 44, x1 = W - 12, y0 = 14, y1 = H - 22, N = 1200;
    if (cache.id !== planetaSerie) { cache = { id: planetaSerie, y: new Float32Array(N + 1) }; for (let i = 0; i <= N; i++) cache.y[i] = cal.elLon(planetaSerie, J0 + (J1 - J0) * i / N) / RAD; }
    const X = (j) => x0 + (j - J0) / (J1 - J0) * (x1 - x0), Y = (v) => y1 - (v + 180) / 360 * (y1 - y0);
    c.fillStyle = "#070a14"; c.fillRect(0, 0, W, H); c.font = "10px system-ui,sans-serif"; c.textBaseline = "middle"; c.textAlign = "right";
    for (const v of [-180, -90, 0, 90, 180]) { c.strokeStyle = v === 0 ? "rgba(255,255,255,0.28)" : "rgba(125,147,192,0.2)"; c.beginPath(); c.moveTo(x0, Y(v)); c.lineTo(x1, Y(v)); c.stroke(); c.fillStyle = "#8fa0c0"; c.fillText(v > 0 ? `+${v}°` : `${v}°`, x0 - 4, Y(v)); }
    c.textAlign = "center"; for (let a = 2030; a <= 2050; a += 5) c.fillText(String(a), X(jdTdbDesdeUtc(Date.UTC(a, 0, 1) / 864e5 + 2440587.5)), y1 + 12);
    c.fillStyle = "#8fa0c0"; c.textAlign = "left"; c.fillText(`${NOMBRE[planetaSerie]}: longitud menos la del Sol`, x0 + 6, y0 + 4);
    c.strokeStyle = COLOR[planetaSerie]; c.lineWidth = 1.6; c.beginPath(); let prev = null; for (let i = 0; i <= N; i++) { const x = x0 + i / N * (x1 - x0), y = Y(cache.y[i]); if (prev !== null && Math.abs(cache.y[i] - prev) > 180) c.moveTo(x, y); else if (i) c.lineTo(x, y); else c.moveTo(x, y); prev = cache.y[i]; } c.stroke();
    const tiposAct = new Set(GRUPOS.filter((g) => activos.has(g[0])).flatMap((g) => g[2]));
    for (const e of TODOS) { if (e.planeta !== planetaSerie || e.planeta2 || !tiposAct.has(e.tipo)) continue; const v = e.planeta2 ? null : cal.elLon(e.planeta, e.jdTdb) / RAD; if (v === null) continue; c.fillStyle = MARCA[e.tipo]; c.beginPath(); c.arc(X(e.jdTdb), Y(v), e === sel ? 5 : 3, 0, 7); c.fill(); }
    c.strokeStyle = "#fff"; c.lineWidth = 1.4; c.beginPath(); c.moveTo(X(jd), y0); c.lineTo(X(jd), y1); c.stroke(); serieGeom = { x0, x1 };
  }
  $("serie").addEventListener("pointerdown", (ev) => { const mover = (e) => { if (!serieGeom) return; const r = $("serie").getBoundingClientRect(); jd = Math.max(J0, Math.min(J1, J0 + (e.clientX - r.left - serieGeom.x0) / (serieGeom.x1 - serieGeom.x0) * (J1 - J0))); }; mover(ev); const mv = (e) => mover(e), up = () => { removeEventListener("pointermove", mv); removeEventListener("pointerup", up); }; addEventListener("pointermove", mv); addEventListener("pointerup", up); });

  $("meta").innerHTML = `<p>Las posiciones heliocéntricas son las efemérides oficiales de JPL (2027–2050). Se pasan a posiciones geocéntricas <b>aparentes</b> (tiempo luz y aberración anual) y cada fenómeno se encuentra por bisección: oposición y conjunción, cuando la longitud eclíptica del planeta menos la del Sol vale 180° o 0°; cuadraturas, ±90°; máxima elongación de Mercurio y Venus, máximo de su separación angular al Sol; estacionarios, velocidad nula de la longitud aparente; conjunciones entre planetas, igual longitud. Se contrastó con JPL Horizons en 168 épocas (elongación ≤ 0,0003°, longitud ≤ 0,0006°: menos de un minuto en el instante de un fenómeno). Las horas son UTC. No considera el brillo, la altura sobre el horizonte del observador ni la luz del crepúsculo: «no visible» se refiere a la geometría respecto del Sol.</p>`;
  const anio0 = TODOS.find((e) => e.tipo === "oposicion"); $("sAnio").value = "2027"; filtrar(); seleccionar(lista.find((e) => e.tipo === "oposicion") || anio0 || lista[0]);
  let ult = 0;
  (function cuadro(t) {
    dtFrame = Math.min(2, (t - (tprev || t)) / 1000);
    if (jugando) { jd = Math.min(J1, jd + dtFrame * velocidad); if (jd >= J1) { jugando = false; $("bPlay").textContent = "▶"; } }
    tprev = t; dibujarMapa(); dibujarSerie();
    if (t - ult > 120) { ult = t; $("fecha").textContent = formatoUtc(jdUtcDesdeTdb(jd), false).slice(0, 16) + " UTC"; const el = cal.elLon(planetaSerie, jd) / RAD; $("sub").textContent = `${NOMBRE[planetaSerie]} · longitud relativa al Sol ${el >= 0 ? "+" : "−"}${fmt(Math.abs(el), 1)}° · elongación ${fmt(cal.elongacion(planetaSerie, jd) / RAD, 1)}°`; }
    requestAnimationFrame(cuadro);
  })(0);
  window.__cal = { cal, TODOS, get jd() { return jd; }, set jd(v) { jd = v; } };
}
