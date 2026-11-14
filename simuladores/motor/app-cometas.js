// SPDX-License-Identifier: Apache-2.0
// Simulador de cometas 2027–2050: se elige un cometa, se pulsa ▶ y se ve su órbita real entre los planetas, con perihelio, afelio y acercamientos.
import { cargarSistema } from "./efemerides.js";
import { UA_KM, C_KM_S, elementos } from "./cuerpos.js";
import { JD_UTC_INICIO, JD_UTC_FIN, jdTdbDesdeUtc, jdUtcDesdeTdb, formatoUtc } from "./tiempo.js";
import { COMETAS, hitosCometa, ETIQUETA } from "./cometas.js";
import { barraNavegacion } from "./navegacion.js";

const fmt = (x, d = 0) => x.toLocaleString("es-CL", { minimumFractionDigits: d, maximumFractionDigits: d });
const VEL = [["1 día / s", 1], ["10 días / s", 10], ["30 días / s", 30], ["100 días / s", 100], ["1 año / s", 365.25]];
const SEMIEJE = { "199": 0.387, "299": 0.723, "399": 1, "499": 1.524, "599": 5.203, "699": 9.537, "799": 19.19, "899": 30.07 };
const COLP = { "199": "#b8b0a8", "299": "#f0d9a0", "399": "#5a9bf0", "499": "#d9673f", "599": "#e8c18a", "699": "#ead7a2", "799": "#9be1e8", "899": "#5b7dff" };
const NOMP = { "199": "Mercurio", "299": "Venus", "399": "Tierra", "499": "Marte", "599": "Júpiter", "699": "Saturno", "799": "Urano", "899": "Neptuno" };
const MU = 132712440041.94;
const COLH = { perihelio: "#ffd45e", afelio: "#8fa0c0", tierra: "#5a9bf0", jupiter: "#e8c18a" };

export async function iniciarCometas() {
  const raiz = document.getElementById("app");
  const cab = document.createElement("header"); cab.className = "cabecera"; cab.innerHTML = "<h1>Cometas</h1>"; cab.appendChild(barraNavegacion("cometas")); document.body.insertBefore(cab, raiz);
  raiz.className = "app";
  raiz.innerHTML = `
    <section class="escena" aria-label="Órbita del cometa" style="display:flex;flex-direction:column">
      <div style="flex:0 0 auto;display:flex;gap:10px;align-items:center;padding:8px 12px;background:var(--panel);border-bottom:1px solid var(--borde)"><label class="etq" for="sCom" style="font-weight:650;color:var(--acento)">Cometa</label><select id="sCom" aria-label="Elegir cometa" style="flex:1 1 auto;min-width:0;max-width:360px"></select></div>
      <div style="position:relative;flex:1 1 auto;min-height:0"><canvas id="mapa" tabindex="0" style="position:absolute;inset:0;width:100%;height:100%" aria-label="Órbita del cometa y posiciones de los planetas vistas desde el polo norte eclíptico o de canto."></canvas>
        <div class="hud"><div class="fecha" id="fecha"></div><div class="sub" id="sub"></div></div>
        <div class="cargando" id="cargando"><div>Cargando efemérides de los cometas…</div><progress id="prog" max="1" value="0"></progress></div></div>
      <div style="position:relative;flex:0 0 140px;border-top:1px solid var(--borde)"><canvas id="serie" style="position:absolute;inset:0;width:100%;height:100%;cursor:pointer" aria-label="Distancia del cometa al Sol y a la Tierra de 2027 a 2050, con perihelio y afelio marcados. Clic para ir a esa fecha."></canvas></div>
      <div class="barra" style="position:relative;flex:0 0 auto;border-top:1px solid var(--borde)"><div class="grupo" role="group" aria-label="Control del tiempo">
          <button id="bIni" aria-label="Ir al inicio (2027)" title="Inicio">⏮</button><button id="bAnt" aria-label="Hito anterior" title="Hito anterior">⏪</button>
          <button id="bPlay" aria-label="Reproducir" title="Reproducir / pausar (espacio)" style="min-width:48px">▶</button>
          <button id="bSig" aria-label="Hito siguiente" title="Hito siguiente">⏩</button><button id="bFin" aria-label="Ir al final (2050)" title="Final">⏭</button></div>
        <div class="grupo"><label class="etq" for="sVel">Velocidad</label><select id="sVel"></select></div>
        <div class="grupo"><label class="etq" for="sVista">Vista</label><select id="sVista"><option value="0">Desde el polo norte</option><option value="1">De canto (inclinación)</option></select>
          <label class="chk" title="Sin comprimir las distancias"><input type="checkbox" id="cLineal"> Escala lineal</label></div></div>
    </section>
    <aside class="lateral" aria-label="Datos del cometa">
      <div class="ficha" id="ficha" aria-live="polite"></div>
      <h2>Estado</h2><dl class="datos" id="estado"></dl>
      <h2>Elementos osculadores</h2><dl class="datos" id="elem"></dl>
      <h2>Hitos entre 2027 y 2050</h2><div class="lista" id="hitos" style="max-height:230px"></div>
      <details><summary>Datos, modelo y límites</summary><div class="aviso" id="meta"></div></details>
      <p class="aviso">Documentación: <a href="documentacion/README.html">documentación de los simuladores</a>.</p>
    </aside>`;
  const $ = (i) => document.getElementById(i);
  let sol, com;
  try { const p = [0, 0], pr = () => { $("prog").value = (p[0] + p[1]) / 2; }; [sol, com] = await Promise.all([cargarSistema("sol", "datos", (f) => { p[0] = f; pr(); }), cargarSistema("cometas", "datos", (f) => { p[1] = f; pr(); })]); }
  catch (e) { $("cargando").classList.add("error"); $("cargando").innerHTML = `<div><strong>No se pudieron cargar los datos.</strong></div><div>${e.message}</div><small>Abra el sitio publicado en GitHub Pages o sirva la carpeta con <code>python -m http.server</code>.</small>`; return; }
  $("cargando").remove();
  const planetas = new Map(Object.keys(NOMP).map((i) => [i, sol.cuerpo(i)])), tierra = planetas.get("399");
  const J0 = jdTdbDesdeUtc(JD_UTC_INICIO), J1 = jdTdbDesdeUtc(JD_UTC_FIN), tmp = [0, 0, 0], tmp2 = [0, 0, 0];
  let c = null, jd = J0, jugando = false, velocidad = 1, rvista = 2, dtFrame = 0, tprev = 0, serieGeom = null;
  const fechaCorta = (j) => formatoUtc(jdUtcDesdeTdb(j), false).slice(0, 10);

  $("sCom").innerHTML = Object.keys(COMETAS).filter((id) => com.cuerpos.has(id)).map((id) => `<option value="${id}">${COMETAS[id].nombre}</option>`).join("");
  function elegir(id) {
    const t = com.cuerpo(id), d = COMETAS[id], hitos = hitosCometa(t, sol), N = 1000; c = { id, t, d, hitos };
    c.camino = new Float64Array((N + 1) * 3); c.rS = new Float64Array(N + 1); c.rT = new Float64Array(N + 1); let rmax = 0;
    for (let k = 0; k <= N; k++) { const j = J0 + (J1 - J0) * k / N; t.pos(j, tmp); c.camino.set(tmp, k * 3); tierra.pos(j, tmp2); c.rS[k] = Math.hypot(...tmp) / UA_KM; c.rT[k] = Math.hypot(tmp[0] - tmp2[0], tmp[1] - tmp2[1], tmp[2] - tmp2[2]) / UA_KM; rmax = Math.max(rmax, c.rS[k]); }
    c.rfit = Math.max(1.8, rmax * 1.1); c.smax = Math.max(...c.rS) * 1.08; c.zmax = Math.max(...Array.from({ length: N + 1 }, (_, k) => Math.abs(c.camino[k * 3 + 2]))) / UA_KM;
    $("sCom").value = id; jd = J0; rvista = c.rfit;
    const per = hitos.filter((h) => h.tipo === "perihelio");
    $("ficha").innerHTML = `<h3 style="color:${d.color}">${d.nombre}</h3><p style="margin:4px 0">${d.nota}</p>${per.length ? "" : '<p class="etq" style="margin:4px 0">Sin perihelio entre 2027 y 2050: aquí sólo se ve un tramo de su órbita.</p>'}`;
    $("hitos").innerHTML = hitos.map((h, i) => `<button data-i="${i}"><span><span style="color:${COLH[h.tipo]}">●</span> ${fechaCorta(h.jdTdb)} · ${ETIQUETA[h.tipo]}</span><small>${fmt(h.dist_ua, 2)} UA</small></button>`).join("") || "<div class='aviso' style='padding:8px'>Sin hitos en este tramo.</div>";
    history.replaceState(null, "", `#c=${id}`); dibujarSerie();
  }
  $("sCom").onchange = () => elegir($("sCom").value);
  $("hitos").addEventListener("click", (e) => { const b = e.target.closest("button"); if (b) jd = c.hitos[+b.dataset.i].jdTdb; });
  const vecino = (dir) => dir > 0 ? c.hitos.find((h) => h.jdTdb > jd + 0.5) : [...c.hitos].reverse().find((h) => h.jdTdb < jd - 0.5);
  $("bSig").onclick = () => { const h = vecino(1); if (h) jd = h.jdTdb; }; $("bAnt").onclick = () => { const h = vecino(-1); if (h) jd = h.jdTdb; };
  $("bIni").onclick = () => { jd = J0; }; $("bFin").onclick = () => { jd = J1; };
  $("sVel").innerHTML = VEL.map(([t, v]) => `<option value="${v}">${t}</option>`).join(""); $("sVel").onchange = () => { velocidad = +$("sVel").value; };
  const play = () => { jugando = !jugando; $("bPlay").textContent = jugando ? "⏸" : "▶"; $("bPlay").setAttribute("aria-label", jugando ? "Pausar" : "Reproducir"); if (jugando && jd >= J1 - 1) jd = J0; };
  $("bPlay").onclick = play; addEventListener("keydown", (e) => { if (/INPUT|SELECT|TEXTAREA/.test(document.activeElement.tagName)) return; if (e.code === "Space") { e.preventDefault(); play(); } });

  function cajas(cv) { const dpr = Math.min(2, devicePixelRatio || 1), W = cv.clientWidth, H = cv.clientHeight; if (cv.width !== Math.round(W * dpr) || cv.height !== Math.round(H * dpr)) { cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr); } const k = cv.getContext("2d"); k.setTransform(dpr, 0, 0, dpr, 0, 0); return [k, W, H]; }
  function dibujarMapa() {
    const [g, W, H] = cajas($("mapa")); g.fillStyle = "#02030a"; g.fillRect(0, 0, W, H);
    const canto = $("sVista").value === "1", lineal = $("cLineal").checked, cx = W / 2, cy = H / 2 + 6, R = Math.min(W / 2 - 40, H / 2 - 30);
    const esc = (r) => (lineal ? r / c.rfit : Math.sqrt(r / c.rfit)) * R;
    const P = (v) => { const x = v[0] / UA_KM, y = (canto ? v[2] : v[1]) / UA_KM, r = Math.hypot(x, y); if (r < 1e-9) return [cx, cy]; const k = esc(r) / r; return [cx + x * k, cy - y * k]; };
    g.font = "11px system-ui,sans-serif"; g.textBaseline = "middle";
    if (!canto) for (const id of Object.keys(SEMIEJE)) { const r = esc(SEMIEJE[id]); if (r > R * 1.03) continue; g.strokeStyle = "rgba(125,147,192,0.28)"; g.setLineDash([3, 5]); g.beginPath(); g.arc(cx, cy, r, 0, 7); g.stroke(); } else { g.strokeStyle = "rgba(125,147,192,0.25)"; g.setLineDash([3, 5]); g.beginPath(); g.moveTo(cx - R, cy); g.lineTo(cx + R, cy); g.stroke(); }
    g.setLineDash([]);
    g.save(); g.beginPath(); g.rect(cx - R * 1.08, cy - R * 1.02, R * 2.16, R * 2.04); g.clip();
    const N = c.rS.length - 1, k = Math.max(0, Math.min(N, Math.floor((jd - J0) / (J1 - J0) * N)));
    const traza = (a, b, col, w) => { g.strokeStyle = col; g.lineWidth = w; g.beginPath(); for (let i = a; i <= b; i++) { const p = P([c.camino[i * 3], c.camino[i * 3 + 1], c.camino[i * 3 + 2]]); if (i === a) g.moveTo(p[0], p[1]); else g.lineTo(p[0], p[1]); } g.stroke(); };
    traza(0, N, "rgba(255,255,255,0.22)", 1.2); traza(0, k, c.d.color, 2.4); g.restore();
    for (const id of Object.keys(NOMP)) { const p = P(planetas.get(id).pos(jd, tmp)); if (Math.hypot(p[0] - cx, p[1] - cy) > R * 1.06) continue; g.fillStyle = COLP[id]; g.beginPath(); g.arc(p[0], p[1], id === "399" ? 4.6 : 3.6, 0, 7); g.fill(); g.fillStyle = "#9fb0cf"; g.textAlign = "left"; g.fillText(NOMP[id], p[0] + 7, p[1] - 6); }
    g.fillStyle = "#ffd45e"; g.beginPath(); g.arc(cx, cy, 5.5, 0, 7); g.fill(); g.fillStyle = "rgba(255,212,94,0.18)"; g.beginPath(); g.arc(cx, cy, 11, 0, 7); g.fill();
    // hitos: perihelio y afelio sobre la órbita
    for (const h of c.hitos) { if (h.tipo !== "perihelio" && h.tipo !== "afelio") continue; c.t.pos(h.jdTdb, tmp); const p = P(tmp); if (Math.hypot(p[0] - cx, p[1] - cy) > R * 1.05) continue; g.strokeStyle = COLH[h.tipo]; g.lineWidth = 1.6; g.fillStyle = jd >= h.jdTdb ? COLH[h.tipo] : "#02030a"; g.beginPath(); g.arc(p[0], p[1], 4.5, 0, 7); g.fill(); g.stroke(); g.fillStyle = "#cfd8ea"; g.textAlign = "left"; g.fillText(`${ETIQUETA[h.tipo]} ${fechaCorta(h.jdTdb).slice(0, 7)}`, p[0] + 8, p[1] + 12); }
    // el cometa con su cola (esquema: apunta lejos del Sol)
    c.t.pos(jd, tmp); const pc = P(tmp), rS = Math.hypot(...tmp) / UA_KM, sx = pc[0] - cx, sy = pc[1] - cy, sn = Math.hypot(sx, sy) || 1;
    if (rS < 3.2) { const L = Math.min(70, 26 / Math.max(0.35, rS)); const gr = g.createLinearGradient(pc[0], pc[1], pc[0] + sx / sn * L, pc[1] + sy / sn * L); gr.addColorStop(0, c.d.color + "cc"); gr.addColorStop(1, c.d.color + "00"); g.strokeStyle = gr; g.lineWidth = 6; g.beginPath(); g.moveTo(pc[0], pc[1]); g.lineTo(pc[0] + sx / sn * L, pc[1] + sy / sn * L); g.stroke(); }
    g.fillStyle = c.d.color + "44"; g.beginPath(); g.arc(pc[0], pc[1], 10, 0, 7); g.fill(); g.fillStyle = "#fff"; g.strokeStyle = c.d.color; g.lineWidth = 2.2; g.beginPath(); g.arc(pc[0], pc[1], 4.6, 0, 7); g.fill(); g.stroke();
    g.fillStyle = "#fff"; g.font = "600 12px system-ui,sans-serif"; g.textAlign = "left"; g.fillText(c.d.nombre, pc[0] + 11, pc[1] + 14);
    g.fillStyle = "#8fa0c0"; g.font = "11px system-ui,sans-serif"; g.textAlign = "right"; g.fillText(`${canto ? "de canto (eje vertical: sobre / bajo la eclíptica)" : "desde el polo norte eclíptico"} · ${lineal ? "escala lineal" : "escala comprimida (√)"}${rS < 3.2 ? " · cola: esquema" : ""}`, W - 10, H - 9);
  }
  function dibujarSerie() {
    const [g, W, H] = cajas($("serie")), x0 = 44, x1 = W - 12, y0 = 14, y1 = H - 22, N = c.rS.length - 1, X = (j) => x0 + (j - J0) / (J1 - J0) * (x1 - x0), Y = (v) => y1 - v / c.smax * (y1 - y0);
    g.fillStyle = "#070a14"; g.fillRect(0, 0, W, H); g.font = "10px system-ui,sans-serif"; g.textBaseline = "middle"; g.textAlign = "right";
    const paso = c.smax > 25 ? 10 : c.smax > 12 ? 5 : c.smax > 5 ? 2 : 1; for (let v = 0; v <= c.smax; v += paso) { g.strokeStyle = "rgba(125,147,192,0.2)"; g.beginPath(); g.moveTo(x0, Y(v)); g.lineTo(x1, Y(v)); g.stroke(); g.fillStyle = "#8fa0c0"; g.fillText(`${v}`, x0 - 4, Y(v)); }
    g.textAlign = "center"; for (let a = 2030; a <= 2050; a += 5) g.fillText(String(a), X(jdTdbDesdeUtc(Date.UTC(a, 0, 1) / 864e5 + 2440587.5)), y1 + 12);
    const linea = (arr, col, w) => { g.strokeStyle = col; g.lineWidth = w; g.beginPath(); for (let i = 0; i <= N; i++) { const x = x0 + i / N * (x1 - x0), y = Y(Math.min(arr[i], c.smax)); if (i) g.lineTo(x, y); else g.moveTo(x, y); } g.stroke(); };
    linea(c.rT, "rgba(90,155,240,0.75)", 1.2); linea(c.rS, c.d.color, 2);
    g.textAlign = "left"; g.fillStyle = c.d.color; g.fillText("distancia al Sol (UA)", x0 + 6, y0 + 3); g.fillStyle = "#5a9bf0"; g.fillText("distancia a la Tierra", x0 + 140, y0 + 3);
    for (const h of c.hitos) { g.fillStyle = COLH[h.tipo]; g.beginPath(); g.arc(X(h.jdTdb), Y(h.tipo === "tierra" ? h.dist_ua : h.tipo === "jupiter" ? 0 : h.dist_ua), 3.5, 0, 7); g.fill(); }
    g.strokeStyle = "#fff"; g.lineWidth = 1.4; g.beginPath(); g.moveTo(X(jd), y0); g.lineTo(X(jd), y1); g.stroke(); serieGeom = { x0, x1 };
  }
  $("serie").addEventListener("pointerdown", (ev) => { const mover = (e) => { if (!serieGeom) return; const r = $("serie").getBoundingClientRect(); jd = Math.max(J0, Math.min(J1, J0 + (e.clientX - r.left - serieGeom.x0) / (serieGeom.x1 - serieGeom.x0) * (J1 - J0))); }; mover(ev); const mv = (e) => mover(e), up = () => { removeEventListener("pointermove", mv); removeEventListener("pointerup", up); }; addEventListener("pointermove", mv); addEventListener("pointerup", up); });

  function estado() {
    c.t.pos(jd, tmp); c.t.vel(jd, tmp2); const E = tierra.pos(jd, [0, 0, 0]), dS = Math.hypot(...tmp), dE = Math.hypot(tmp[0] - E[0], tmp[1] - E[1], tmp[2] - E[2]), v = Math.hypot(...tmp2), el = elementos(tmp, tmp2, MU);
    $("fecha").textContent = fechaCorta(jd); $("sub").textContent = `${c.d.nombre} · ${fmt(dS / UA_KM, 2)} UA del Sol · predicción de JPL${jd < jdTdbDesdeUtc(JD_UTC_INICIO) ? "" : ""}`;
    const sen = dE / C_KM_S;
    $("estado").innerHTML = `<dt>Distancia al Sol</dt><dd>${fmt(dS / UA_KM, 3)} UA</dd><dt>Distancia a la Tierra</dt><dd>${fmt(dE / UA_KM, 3)} UA</dd><dt>Velocidad respecto del Sol</dt><dd>${fmt(v, 1)} km/s</dd><dt>La luz tarda en llegar</dt><dd>${sen > 7200 ? fmt(sen / 3600, 1) + " h" : fmt(sen / 60, 1) + " min"}</dd><dt>Altura sobre la eclíptica</dt><dd>${fmt(tmp[2] / UA_KM, 2)} UA</dd>`;
    const q = el.a * (1 - el.e), Q = el.a * (1 + el.e);
    $("elem").innerHTML = el.e < 1 ? `<dt>Semieje mayor a</dt><dd>${fmt(el.a / UA_KM, 2)} UA</dd><dt>Excentricidad e</dt><dd>${fmt(el.e, 3)}</dd><dt>Inclinación i</dt><dd>${fmt(el.i, 1)}°${el.i > 90 ? " (retrógrada)" : ""}</dd><dt>Perihelio q</dt><dd>${fmt(q / UA_KM, 2)} UA</dd><dt>Afelio Q</dt><dd>${fmt(Q / UA_KM, 1)} UA</dd><dt>Periodo</dt><dd>${fmt(el.periodo_d / 365.25, 2)} años</dd>` : `<dt>Órbita</dt><dd>abierta</dd>`;
  }
  $("meta").innerHTML = `<p>Posiciones heliocéntricas (eclíptica J2000) del <b>centro del cometa</b> según la solución orbital vigente de JPL Horizons para cada cometa (con fuerzas no gravitatorias), con paso de 1 a 2 días e interpolación de Lagrange de 10 puntos (error máximo medido ≤ 0,05 km frente a Horizons). <b>Es una predicción</b>: la incertidumbre de la órbita de un cometa crece con el tiempo y tras acercamientos a Júpiter (de décimas de grado a varios días en la fecha del perihelio, según el cometa); los datos reflejan el ajuste del 13 de noviembre de 2026. Los elementos osculadores se calculan del estado instantáneo (dos cuerpos con el Sol) y varían con las perturbaciones. La cola es un esquema que apunta lejos del Sol; no se modela el brillo ni la actividad. Los planetas salen de las efemérides oficiales de JPL.</p>`;
  const pedida = /c=([0-9]+P)/.exec(location.hash); elegir(pedida && COMETAS[pedida[1]] && com.cuerpos.has(pedida[1]) ? pedida[1] : "1P");
  let ult = 0;
  (function cuadro(t) {
    dtFrame = Math.min(2, (t - (tprev || t)) / 1000);
    if (jugando) { jd = Math.min(J1, jd + dtFrame * velocidad); if (jd >= J1) { jugando = false; $("bPlay").textContent = "▶"; } }
    tprev = t; dibujarMapa(); dibujarSerie(); if (t - ult > 120) { ult = t; estado(); } requestAnimationFrame(cuadro);
  })(0);
  window.__com = { get jd() { return jd; }, set jd(v) { jd = v; }, elegir, com, sol };
}
