// SPDX-License-Identifier: Apache-2.0
// Simulador de cielo: lo que se ve desde un lugar de la Tierra, Marte, Júpiter o Saturno en cualquier instante de 2027 a 2050.
import { cargarSistema } from "./efemerides.js";
import { Reloj, JD_UTC_INICIO, JD_UTC_FIN, formatoUtc, valorInputUtc, jdUtcDesdeInput, jdTdbDesdeUtc } from "./tiempo.js";
import { PLANETAS, ANILLOS, UA_KM, baseDelCuerpo } from "./cuerpos.js";
import { Observador, ecuatorialAEclipticoJ2000, salidasYPuestas } from "./cielo.js";
import { barraNavegacion } from "./navegacion.js";

const RAD = Math.PI / 180;
const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
const cruz = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
const unit = (a) => { const n = Math.hypot(a[0], a[1], a[2]) || 1; return [a[0] / n, a[1] / n, a[2] / n]; };
const fmt = (x, d = 0) => x.toLocaleString("es-CL", { minimumFractionDigits: d, maximumFractionDigits: d });
const VELOCIDADES = [["Tiempo real (1×)", 1], ["1 min / s", 60], ["10 min / s", 600], ["1 h / s", 3600], ["6 h / s", 21600], ["1 día / s", 86400], ["30 días / s", 2592000]];
const PUNTOS = ["N", "E", "S", "O"];
const NOMBRE_PLAN = { "399": "la Tierra", "499": "Marte", "599": "Júpiter", "699": "Saturno" };

function colorEstrella(bv) {
  const t = Math.max(0, Math.min(1, (bv + 0.4) / 2.4));
  const pal = [[155, 176, 255], [202, 215, 255], [255, 244, 234], [255, 210, 161], [255, 160, 100]];
  const x = t * 4, i = Math.min(3, Math.floor(x)), f = x - i;
  return pal[i].map((v, k) => Math.round(v + (pal[i + 1][k] - v) * f));
}
/** Refracción atmosférica estándar (Bennett) en radianes para una altura geométrica `h` (rad). */
function refraccion(h) {
  const d = Math.max(h / RAD, -1);
  return (1 / Math.tan((d + 7.31 / (d + 4.4)) * RAD)) / 60 * RAD;
}

export async function iniciarCielo(cfg) {
  const raiz = document.getElementById("app");
  const cab = document.createElement("header"); cab.className = "cabecera"; cab.innerHTML = `<h1>${cfg.titulo}</h1>`; cab.appendChild(barraNavegacion(cfg.clave)); document.body.insertBefore(cab, raiz);
  raiz.className = "app";
  raiz.innerHTML = `
    <section class="escena" aria-label="Cielo visto desde ${cfg.lugarTexto}">
      <canvas id="lienzo" tabindex="0" aria-label="Cielo. Arrastre para girar la vista, rueda para el zoom, clic en un astro para ver sus datos."></canvas>
      <div class="hud"><div class="fecha" id="fecha"></div><div class="sub" id="sub"></div></div>
      <div class="cargando" id="cargando"><div>Cargando efemérides y estrellas…</div><progress id="prog" max="1" value="0"></progress></div>
      <div class="barra">
        <div class="grupo" role="group" aria-label="Control del tiempo">
          <button id="bAtras" aria-label="Retroceder un paso" title="Retroceder un paso">◀</button><button id="bPlay" aria-label="Reproducir" title="Reproducir / pausar (espacio)">▶</button><button id="bAdel" aria-label="Avanzar un paso" title="Avanzar un paso">▶|</button>
        </div>
        <div class="grupo"><label for="sVel" class="etq">Velocidad</label><select id="sVel"></select></div>
        <div class="grupo"><label for="sPaso" class="etq">Paso</label><select id="sPaso"><option value="60">1 min</option><option value="3600">1 hora</option><option value="86400">1 día</option><option value="604800">7 días</option><option value="2592000">30 días</option></select></div>
        <div class="grupo"><label for="iFecha" class="etq">Fecha UTC</label><input type="datetime-local" id="iFecha" min="2027-01-01T00:00" max="2050-12-31T23:59"><button id="bIr">Ir</button></div>
      </div>
    </section>
    <aside class="lateral" aria-label="Lugar, vista y datos">
      <h2>Lugar de observación</h2>
      <div><label class="etq" for="sLugar">Lugar </label><select id="sLugar"></select></div>
      <div style="display:flex;gap:8px;margin-top:6px;flex-wrap:wrap"><label class="etq">Latitud <input id="iLat" type="number" step="0.01" min="-90" max="90" style="width:90px"></label><label class="etq">Longitud E <input id="iLon" type="number" step="0.01" min="-180" max="360" style="width:90px"></label></div>
      <p class="aviso">${cfg.aviso}</p>
      <h2>Qué ocurre</h2><div class="ficha" id="estado" aria-live="polite"></div>
      <h2>Vista</h2>
      <div style="display:flex;flex-wrap:wrap;gap:6px 14px"><label class="chk"><input type="checkbox" id="cCons" checked> Constelaciones</label><label class="chk"><input type="checkbox" id="cNom" checked> Nombres</label><label class="chk"><input type="checkbox" id="cAlt"> Cuadrícula altazimutal</label><label class="chk"><input type="checkbox" id="cEcl" checked> Eclíptica</label><label class="chk"><input type="checkbox" id="cEcu"> Ecuador celeste</label>${cfg.id === "399" ? '<label class="chk"><input type="checkbox" id="cRef" checked> Refracción</label>' : ""}</div>
      <div style="display:flex;gap:6px;flex-wrap:wrap;margin-top:8px"><button id="bN">Norte</button><button id="bE">Este</button><button id="bS">Sur</button><button id="bO">Oeste</button><button id="bCen">Cénit</button></div>
      <h2>Astro seleccionado</h2><div class="ficha" id="ficha"></div>
      <h2>Sobre el horizonte</h2><div class="lista" id="lista" role="listbox" aria-label="Astros sobre el horizonte"></div>
      <details><summary>Datos, modelo y tolerancias</summary><div class="aviso" id="meta"></div></details>
      <p class="aviso">Posiciones: NASA/JPL Horizons. Estrellas: Hipparcos/Tycho vía d3-celestial (BSD). Documentación: <a href="documentacion/README.html">documentación de los simuladores</a>.</p>
    </aside>`;
  const $ = (i) => document.getElementById(i);
  const lienzo = $("lienzo"), ctx = lienzo.getContext("2d");

  // ---------------------------------------------------------------- datos
  let sol, sis, cielo;
  try {
    const p = [0, 0, 0], pr = () => { $("prog").value = (p[0] + p[1] + p[2]) / 3; };
    const [a, b, c] = await Promise.all([cargarSistema("sol", "datos", (f) => { p[0] = f; pr(); }), cargarSistema(cfg.sistema, "datos", (f) => { p[1] = f; pr(); }),
      fetch("datos/cielo.json").then((r) => r.json()).then((j) => { p[2] = 1; pr(); return j; })]);
    sol = a; sis = b; cielo = c;
  } catch (e) {
    $("cargando").classList.add("error"); $("cargando").innerHTML = `<div><strong>No se pudieron cargar los datos.</strong></div><div>${e.message}</div><small>Abra el sitio publicado en GitHub Pages o sirva la carpeta con <code>python -m http.server</code>.</small>`; return;
  }
  $("cargando").remove();

  const obs = new Observador({ id: cfg.id, sol, sis });
  const est = cielo.estrellas.map(([ra, de, mag, bv], i) => ({ v: ecuatorialAEclipticoJ2000(ra, de), mag, rgb: colorEstrella(bv), nombre: cielo.nombres[i] || null, ra, de }));
  const figuras = cielo.figuras.map((f) => ({ id: f.id, nombre: cielo.constelaciones[f.id] || f.id, lineas: f.lineas.map((l) => l.map(([ra, de]) => ecuatorialAEclipticoJ2000(ra, de))) }));
  const reloj = new Reloj(jdUtcDesdeInput(cfg.fechaInicial));
  reloj.velocidad = 60;
  const vista = { az: cfg.vista.az * RAD, alt: cfg.vista.alt * RAD, fov: cfg.vista.fov * RAD };
  const lugares = cfg.lugares;
  $("sLugar").innerHTML = lugares.map((l, i) => `<option value="${i}">${l[0]}</option>`).join("");
  const fijarLugar = (lat, lon) => { obs.lugar(lat, lon); $("iLat").value = lat; $("iLon").value = lon; };
  fijarLugar(lugares[0][1], lugares[0][2]);
  $("sLugar").onchange = () => { const l = lugares[+$("sLugar").value]; fijarLugar(l[1], l[2]); };
  const leerLatLon = () => { const la = Math.max(-90, Math.min(90, +$("iLat").value)), lo = +$("iLon").value; obs.lugar(la, lo); };
  $("iLat").onchange = leerLatLon; $("iLon").onchange = leerLatLon;
  $("sVel").innerHTML = VELOCIDADES.map(([t, v]) => `<option value="${v}">${t}</option>`).join(""); $("sVel").value = "60"; $("sPaso").value = "3600";
  $("sVel").onchange = () => { reloj.velocidad = +$("sVel").value; };
  const play = () => { reloj.activo = !reloj.activo; $("bPlay").textContent = reloj.activo ? "⏸" : "▶"; $("bPlay").setAttribute("aria-label", reloj.activo ? "Pausar" : "Reproducir"); };
  $("bPlay").onclick = play;
  $("bAtras").onclick = () => reloj.fijar(reloj.jdUtc - +$("sPaso").value / 86400); $("bAdel").onclick = () => reloj.fijar(reloj.jdUtc + +$("sPaso").value / 86400);
  $("bIr").onclick = () => { const j = jdUtcDesdeInput($("iFecha").value); if (j) reloj.fijar(j); };
  window.addEventListener("keydown", (e) => { if (/INPUT|SELECT|TEXTAREA/.test(document.activeElement.tagName)) return; if (e.code === "Space") { e.preventDefault(); play(); } });
  const mirar = (az, alt) => { vista.az = az * RAD; vista.alt = Math.max(2, alt) * RAD; };
  $("bN").onclick = () => mirar(0, 25); $("bE").onclick = () => mirar(90, 25); $("bS").onclick = () => mirar(180, 25); $("bO").onclick = () => mirar(270, 25); $("bCen").onclick = () => { vista.alt = 88 * RAD; };
  const chk = (id) => $(id) && $(id).checked;

  // ---------------------------------------------------------------- proyección estereográfica sobre el eje de la vista
  let W = 800, H = 600, F = 400, dpr = 1;
  const ajustar = () => { const p = lienzo.parentElement; dpr = Math.min(2, devicePixelRatio || 1); W = Math.max(200, p.clientWidth); H = Math.max(200, p.clientHeight); lienzo.width = W * dpr; lienzo.height = H * dpr; lienzo.style.width = W + "px"; lienzo.style.height = H + "px"; };
  new ResizeObserver(ajustar).observe(lienzo.parentElement); ajustar();
  let eje, der, arr;
  const baseVista = () => {
    eje = obs.desdeHorizonte(vista.alt, vista.az);
    der = unit(cruz(eje, obs.up)); if (Math.hypot(...der) < 1e-6) der = obs.este;
    arr = cruz(der, eje);
    F = H / (4 * Math.tan(vista.fov / 4));
  };
  const proy = (v, salida) => {
    const z = dot(v, eje); if (z < -0.985) return false;
    const k = 2 * F / (1 + z);
    salida[0] = W / 2 + dot(v, der) * k; salida[1] = H / 2 - dot(v, arr) * k; return true;
  };
  const lim = (x, y, m = 40) => x > -m && y > -m && x < W + m && y < H + m;
  const aparente = (v) => {
    if (!(cfg.id === "399" && chk("cRef"))) return v;
    const h = Math.asin(Math.max(-1, Math.min(1, dot(v, obs.up))));
    if (h > 0.6) return v;
    const R = refraccion(h);
    const az = Math.atan2(dot(v, obs.este), dot(v, obs.norte));
    return obs.desdeHorizonte(h + R, az);
  };

  // ---------------------------------------------------------------- dibujo
  let cuerpos = [], seleccionado = null, alturaSol = -1, p2 = [0, 0], p3 = [0, 0];
  const colorCielo = (hs) => {
    if (!cfg.atmosfera) return "#02030a";
    const d = cfg.atmosfera.dia, c = cfg.atmosfera.crepusculo;
    const mezcla = (a, b, t) => a.map((v, i) => Math.round(v + (b[i] - v) * t));
    let rgb;
    if (hs > 0) rgb = d; else if (hs > -6) rgb = mezcla(c, d, (hs + 6) / 6); else if (hs > -18) rgb = mezcla([2, 3, 10], c, (hs + 18) / 12 * 0.8); else rgb = [2, 3, 10];
    return `rgb(${rgb.join(",")})`;
  };
  const limMag = (hs) => (cfg.atmosfera ? Math.max(-3, Math.min(6.6, 6.6 - Math.max(0, (hs + 18)) * (cfg.atmosfera.extincion || 0.4))) : 6.8);

  function lineaSky(puntos, estilo, ancho = 1, cerrar = false) {
    ctx.strokeStyle = estilo; ctx.lineWidth = ancho; ctx.beginPath(); let en = false;
    for (const v of puntos) { if (proy(aparente(v), p2) && lim(p2[0], p2[1], 400)) { if (!en) { ctx.moveTo(p2[0], p2[1]); en = true; } else ctx.lineTo(p2[0], p2[1]); } else en = false; }
    ctx.stroke();
  }
  const circuloMaximo = (n1, n2, t0, t1, paso = 3) => { const out = []; for (let a = t0; a <= t1; a += paso) out.push([n1[0] * Math.cos(a * RAD) + n2[0] * Math.sin(a * RAD), n1[1] * Math.cos(a * RAD) + n2[1] * Math.sin(a * RAD), n1[2] * Math.cos(a * RAD) + n2[2] * Math.sin(a * RAD)]); return out; };

  function dibujar() {
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    baseVista();
    const jd = reloj.jdTdb;
    obs.actualizar(jd, reloj.jdUtc);
    cuerpos = obs.cuerpos();
    const sunC = cuerpos.find((c) => c.id === "10"); alturaSol = sunC.alt / RAD;
    ctx.fillStyle = colorCielo(alturaSol); ctx.fillRect(0, 0, W, H);
    const lm = limMag(alturaSol);
    // cuadrículas
    if (chk("cAlt")) {
      for (let al = -60; al <= 80; al += 30) { const pts = []; for (let az = 0; az <= 360; az += 4) pts.push(obs.desdeHorizonte(al * RAD, az * RAD)); lineaSky(pts, "rgba(120,170,255,0.22)"); }
      for (let az = 0; az < 360; az += 30) { const pts = []; for (let al = -85; al <= 89; al += 4) pts.push(obs.desdeHorizonte(al * RAD, az * RAD)); lineaSky(pts, "rgba(120,170,255,0.22)"); }
    }
    if (chk("cEcu")) { const c = Math.cos(23.4392911 * RAD), s = Math.sin(23.4392911 * RAD); lineaSky(circuloMaximo([1, 0, 0], [0, c, -s], 0, 360), "rgba(255,120,120,0.5)", 1.2); }
    if (chk("cEcl")) lineaSky(circuloMaximo([1, 0, 0], [0, 1, 0], 0, 360), "rgba(255,220,120,0.55)", 1.2);
    // constelaciones
    if (chk("cCons")) {
      ctx.strokeStyle = "rgba(140,170,230,0.45)"; ctx.lineWidth = 1; ctx.beginPath();
      for (const f of figuras) for (const l of f.lineas) {
        let a = null;
        for (const v of l) {
          if (a) { for (let k = 0; k <= 3; k++) { const t = k / 3, w = unit([a[0] + (v[0] - a[0]) * t, a[1] + (v[1] - a[1]) * t, a[2] + (v[2] - a[2]) * t]); const ok = proy(aparente(w), p2); if (k === 0 && ok) ctx.moveTo(p2[0], p2[1]); else if (ok) ctx.lineTo(p2[0], p2[1]); } }
          a = v;
        }
      }
      ctx.stroke();
    }
    // estrellas
    const escala = Math.min(1.8, Math.max(0.8, 0.6 + (H / 600) * 0.4 + (1.4 / (vista.fov / RAD / 60 + 1))));
    for (const s of est) {
      if (s.mag > lm) continue;
      if (!proy(aparente(s.v), p2) || !lim(p2[0], p2[1])) continue;
      const r = Math.max(0.5, (0.55 + (6.8 - s.mag) * 0.42) * escala * 0.9);
      const aten = Math.min(1, (lm - s.mag) / 1.2 + 0.25);
      ctx.fillStyle = `rgba(${s.rgb.join(",")},${aten})`; ctx.beginPath(); ctx.arc(p2[0], p2[1], r, 0, 7); ctx.fill();
      if (chk("cNom") && s.nombre && s.mag < 2.2 + (60 / (vista.fov / RAD + 20))) { ctx.fillStyle = "rgba(200,215,240,0.8)"; ctx.font = "11px system-ui"; ctx.fillText(s.nombre, p2[0] + r + 3, p2[1] - 2); }
    }
    if (chk("cNom") && vista.fov < 100 * RAD) for (const f of figuras) {
      const pts = f.lineas.flat(); if (!pts.length) continue;
      const c = unit(pts.reduce((a, v) => [a[0] + v[0], a[1] + v[1], a[2] + v[2]], [0, 0, 0]));
      if (proy(aparente(c), p2) && lim(p2[0], p2[1], -20)) { ctx.fillStyle = "rgba(120,150,210,0.7)"; ctx.font = "italic 12px system-ui"; ctx.textAlign = "center"; ctx.fillText(f.nombre, p2[0], p2[1]); ctx.textAlign = "start"; }
    }
    // anillos del planeta anfitrión (Saturno, Júpiter)
    if (ANILLOS[cfg.id]) {
      const z = obs.base.z; let u = cruz(z, [0, 0, 1]); if (Math.hypot(...u) < 1e-6) u = [1, 0, 0]; u = unit(u); const w = cruz(z, u);
      for (const an of ANILLOS[cfg.id]) {
        if (an.o < 0.05) continue;
        const N = 240; let prevIn = null, prevOut = null;
        for (let k = 0; k <= N; k++) {
          const th = (k / N) * 2 * Math.PI, cs = Math.cos(th), sn = Math.sin(th);
          const pa = [(cs * u[0] + sn * w[0]) * an.a - obs.rel[0], (cs * u[1] + sn * w[1]) * an.a - obs.rel[1], (cs * u[2] + sn * w[2]) * an.a - obs.rel[2]];
          const pb = [(cs * u[0] + sn * w[0]) * an.b - obs.rel[0], (cs * u[1] + sn * w[1]) * an.b - obs.rel[1], (cs * u[2] + sn * w[2]) * an.b - obs.rel[2]];
          const A = [0, 0], B = [0, 0], oka = proy(unit(pa), A), okb = proy(unit(pb), B);
          if (oka && okb && prevIn && prevOut) { ctx.fillStyle = `rgba(226,206,160,${Math.min(0.85, an.o)})`; ctx.beginPath(); ctx.moveTo(prevIn[0], prevIn[1]); ctx.lineTo(prevOut[0], prevOut[1]); ctx.lineTo(B[0], B[1]); ctx.lineTo(A[0], A[1]); ctx.closePath(); ctx.fill(); }
          prevIn = oka ? A.slice() : null; prevOut = okb ? B.slice() : null;
        }
      }
    }
    // astros
    const cajas = [];
    const orden = [...cuerpos].sort((a, b) => b.dist_km - a.dist_km);
    for (const c of orden) {
      const vv = aparente(c.dir);
      if (!proy(vv, p2) || !lim(p2[0], p2[1], 20)) { c._p = null; continue; }
      c._p = [p2[0], p2[1]];
      const px = Math.max(0, c.tam * F);               // radio angular -> píxeles (centro: 2F·tan(θ/2) ~ F·θ)
      if (c.tipo === "sol") {
        const r = Math.max(4, px / 2 * 2 * 0.5 + 0);
        const rr = Math.max(4, c.tam * F);
        const g = ctx.createRadialGradient(p2[0], p2[1], 0, p2[0], p2[1], rr * 6); g.addColorStop(0, "rgba(255,244,200,0.9)"); g.addColorStop(1, "rgba(255,220,120,0)");
        ctx.fillStyle = g; ctx.beginPath(); ctx.arc(p2[0], p2[1], rr * 6, 0, 7); ctx.fill();
        ctx.fillStyle = "#fffbe6"; ctx.beginPath(); ctx.arc(p2[0], p2[1], rr, 0, 7); ctx.fill();
      } else if (px > 3 || c.tipo === "luna" && px > 1.5) {
        const rr = Math.max(2.5, px); ctx.save(); ctx.translate(p2[0], p2[1]);
        // dirección del Sol en pantalla (ángulo de posición del limbo iluminado)
        const sv = sunC.dir, t = unit([sv[0] - c.dir[0] * dot(sv, c.dir), sv[1] - c.dir[1] * dot(sv, c.dir), sv[2] - c.dir[2] * dot(sv, c.dir)]);
        const q = unit([c.dir[0] + t[0] * 0.002, c.dir[1] + t[1] * 0.002, c.dir[2] + t[2] * 0.002]); const Q = [0, 0];
        const ang = proy(q, Q) ? Math.atan2(Q[1] - p2[1], Q[0] - p2[0]) : 0;
        ctx.rotate(ang); const k = Math.cos(c.angFase);   // k = coseno del ángulo de fase: lado iluminado hacia el Sol
        ctx.fillStyle = "rgba(20,22,32,0.95)"; ctx.beginPath(); ctx.arc(0, 0, rr, 0, 7); ctx.fill();
        ctx.beginPath(); ctx.arc(0, 0, rr, -Math.PI / 2, Math.PI / 2, false); ctx.ellipse(0, 0, Math.max(0.01, Math.abs(k)) * rr, rr, 0, Math.PI / 2, k >= 0 ? 1.5 * Math.PI : -Math.PI / 2, k < 0); ctx.closePath();
        ctx.fillStyle = c.id === "301" ? "#e9e6dc" : c.color || "#ddd"; ctx.fill(); ctx.restore();
      } else {
        const r = Math.max(1.3, 1.6 + (1.5 - c.mag) * 0.55 * (c.tipo === "planeta" ? 0.9 : 0.6));
        ctx.fillStyle = c.color || "#fff"; ctx.beginPath(); ctx.arc(p2[0], p2[1], Math.min(r, 7), 0, 7); ctx.fill();
      }
      if (c === seleccionado) { ctx.strokeStyle = "#ffe08a"; ctx.beginPath(); ctx.arc(p2[0], p2[1], 14, 0, 7); ctx.stroke(); }
      const visible = c.tipo !== "luna" || c.mag < 8.5;
      if (visible && (c.alt > -3 * RAD || c === seleccionado)) { ctx.fillStyle = c === seleccionado ? "#ffe08a" : "rgba(235,240,250,0.92)"; ctx.font = "12px system-ui"; const rx = p2[0] + 10, ry = p2[1] - 8; if (!cajas.some((b) => Math.abs(b[0] - rx) < 60 && Math.abs(b[1] - ry) < 13)) { ctx.fillText(c.nombre, rx, ry); cajas.push([rx, ry]); } }
    }
    // suelo
    const poly = []; let todos = true;
    for (let az = 0; az <= 360; az += 2) { const v = obs.desdeHorizonte(0, az * RAD); if (proy(v, p2)) poly.push([p2[0], p2[1]]); else todos = false; }
    if (poly.length > 8) {
      const cena = cfg.suelo, hs = alturaSol;
      const luz = Math.max(0.12, Math.min(1, (hs + 10) / 25));
      ctx.beginPath(); ctx.rect(-5000, -5000, 10000, 10000);
      // el suelo es el exterior del círculo del horizonte si el cénit está en pantalla; en otro caso el polígono mismo. Se decide por el cénit.
      const zen = obs.up; const zenVisible = proy(zen, p3);
      const cx = poly.reduce((a, p) => a + p[0], 0) / poly.length, cy = poly.reduce((a, p) => a + p[1], 0) / poly.length;
      const cenDentro = proy(obs.desdeHorizonte(Math.PI / 2 - 0.001, 0), p3);
      ctx.beginPath();
      if (vista.alt > 0.0) { // se mira por encima del horizonte: el cielo es el interior del círculo; el suelo, el resto
        ctx.rect(-5000, -5000, 10000, 10000); ctx.moveTo(poly[0][0], poly[0][1]); for (const p of poly) ctx.lineTo(p[0], p[1]); ctx.closePath();
        ctx.fillStyle = `rgb(${cena.map((v) => Math.round(v * luz)).join(",")})`; ctx.fill("evenodd");
      }
      ctx.strokeStyle = "rgba(255,255,255,0.35)"; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(poly[0][0], poly[0][1]); for (const p of poly) ctx.lineTo(p[0], p[1]); ctx.closePath(); ctx.stroke();
    }
    // puntos cardinales
    ctx.font = "bold 14px system-ui"; ctx.textAlign = "center";
    PUNTOS.forEach((n, i) => { const v = obs.desdeHorizonte(3 * RAD, i * Math.PI / 2); if (proy(v, p2) && lim(p2[0], p2[1], -10)) { ctx.fillStyle = "#ffd45e"; ctx.fillText(n, p2[0], p2[1]); } });
    ctx.textAlign = "start";
  }

  // ---------------------------------------------------------------- entrada
  let drag = null;
  lienzo.addEventListener("pointerdown", (e) => { lienzo.setPointerCapture(e.pointerId); drag = { x: e.clientX, y: e.clientY, m: 0 }; });
  lienzo.addEventListener("pointermove", (e) => { if (!drag) return; const dx = e.clientX - drag.x, dy = e.clientY - drag.y; drag.x = e.clientX; drag.y = e.clientY; drag.m += Math.abs(dx) + Math.abs(dy); const f = vista.fov / H; vista.az -= dx * f * 1.0; vista.alt = Math.max(2 * RAD, Math.min(Math.PI / 2 - 0.0001, vista.alt + dy * f)); vista.az = (vista.az + 2 * Math.PI) % (2 * Math.PI); });
  lienzo.addEventListener("pointerup", (e) => {
    if (drag && drag.m < 5) { const r = lienzo.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top; let mejor = null, md = 20 * 20; for (const c of cuerpos) if (c._p) { const d = (c._p[0] - x) ** 2 + (c._p[1] - y) ** 2; if (d < md) { md = d; mejor = c; } } seleccionar(mejor); }
    drag = null;
  });
  lienzo.addEventListener("wheel", (e) => { e.preventDefault(); vista.fov = Math.max(4 * RAD, Math.min(170 * RAD, vista.fov * Math.exp(e.deltaY * 0.0012))); }, { passive: false });
  lienzo.addEventListener("keydown", (e) => { const k = e.key, f = vista.fov * 0.1; if (k === "ArrowLeft") vista.az -= f; else if (k === "ArrowRight") vista.az += f; else if (k === "ArrowUp") vista.alt = Math.min(Math.PI / 2 - 0.0001, vista.alt + f); else if (k === "ArrowDown") vista.alt = Math.max(2 * RAD, vista.alt - f); else if (k === "+" || k === "=") vista.fov = Math.max(4 * RAD, vista.fov * 0.85); else if (k === "-") vista.fov = Math.min(170 * RAD, vista.fov * 1.18); else return; e.preventDefault(); });

  // ---------------------------------------------------------------- paneles
  const hhmm = (jdU) => formatoUtc(jdU, false).slice(11, 16);
  function nombreCrepusculo(h) { return h > 0 ? "día" : h > -6 ? "crepúsculo civil" : h > -12 ? "crepúsculo náutico" : h > -18 ? "crepúsculo astronómico" : "noche"; }
  function seleccionar(c) { seleccionado = c; pintarFicha(); }
  function pintarFicha() {
    const c = seleccionado; if (!c) { $("ficha").innerHTML = "<span class='etq'>Haga clic en un astro.</span>"; return; }
    const v = c.dir, ra = ((Math.atan2(v[1] * Math.cos(23.4392911 * RAD) - v[2] * Math.sin(23.4392911 * RAD), v[0]) / RAD) + 360) % 360, de = Math.asin(v[1] * Math.sin(23.4392911 * RAD) + v[2] * Math.cos(23.4392911 * RAD)) / RAD;
    const filas = [["Altura · acimut", `${fmt(c.alt / RAD, 1)}° · ${fmt(c.az / RAD, 1)}°`], ["AR · Dec (J2000)", `${fmt(ra / 15, 3)} h · ${fmt(de, 2)}°`], ["Distancia", c.dist_km > 1e7 ? `${fmt(c.dist_km / UA_KM, 4)} UA` : `${fmt(c.dist_km)} km`],
      ["Magnitud aparente", fmt(c.mag, 1)], ["Tamaño angular", c.tam > 1e-3 ? `${fmt(c.tam / RAD * 3600, c.tam / RAD * 3600 > 100 ? 0 : 1)}″` : "< 4″"]];
    if (c.fase !== undefined) filas.push(["Iluminación vista", `${fmt(c.fase * 100, 1)} %`]);
    $("ficha").innerHTML = `<h3>${c.nombre}</h3><dl class="datos">${filas.map(([k, x]) => `<dt>${k}</dt><dd>${x}</dd>`).join("")}</dl>`;
  }
  function pintarEstado() {
    const sun = cuerpos.find((c) => c.id === "10"), h = sun.alt / RAD;
    const hoy = Math.floor(reloj.jdUtc - 0.5) + 0.5;
    const um = -(34 / 60 * RAD * (cfg.id === "399" ? 1 : 0) + sun.tam / 2) / 1;
    const esc = salidasYPuestas(obs, (jdT) => { const O = obs.pos; return [-O[0], -O[1], -O[2]]; }, um, hoy);
    obs.actualizar(reloj.jdTdb, reloj.jdUtc);
    const sal = esc.filter((e) => e.tipo === "salida").map((e) => hhmm(e.jdUtc)).join(", ") || "—", pue = esc.filter((e) => e.tipo === "puesta").map((e) => hhmm(e.jdUtc)).join(", ") || "—";
    let html = `<dl class="datos"><dt>Altura del Sol</dt><dd>${fmt(h, 1)}° · ${nombreCrepusculo(h)}</dd><dt>Salida del Sol (UTC)</dt><dd>${sal}</dd><dt>Puesta del Sol (UTC)</dt><dd>${pue}</dd>`;
    const luna = cuerpos.find((c) => c.id === "301");
    if (luna) {
      const k = Math.round(luna.fase * 100);
      html += `<dt>Luna</dt><dd>${fmt(luna.alt / RAD, 1)}° · ${k} % iluminada</dd>`;
    }
    $("estado").innerHTML = html + "</dl>";
    const sobre = cuerpos.filter((c) => c.alt > 0 && c.id !== "10" && (c.mag < 9 || c.tipo === "planeta")).sort((a, b) => a.mag - b.mag);
    $("lista").innerHTML = sobre.map((c) => `<button data-id="${c.id}"><span>${c.nombre}</span><small>${fmt(c.alt / RAD, 0)}° · mag ${fmt(c.mag, 1)}</small></button>`).join("") || "<div class='aviso' style='padding:8px'>Ningún astro de la lista sobre el horizonte.</div>";
    $("meta").innerHTML = `<p>Marco: eclíptica J2000 de las efemérides; horizonte local por la orientación IAU de ${NOMBRE_PLAN[cfg.id]} (${cfg.id === "399" ? "ángulo de rotación terrestre ERA" : "polo y meridiano IAU sin términos periódicos"}). Planetas con corrección de tiempo luz; sin aberración ni paralaje estelar; estrellas sin movimiento propio (error típico < 1′). ${cfg.nota}</p>`;
  }
  $("lista").addEventListener("click", (e) => { const b = e.target.closest("button"); if (!b) return; const c = cuerpos.find((x) => x.id === b.dataset.id); if (c) { seleccionar(c); vista.az = c.az; vista.alt = Math.max(3 * RAD, c.alt); } });
  seleccionar(cuerpos.find((c) => c.id === "10") || null);

  let ultima = 0;
  function cuadro(t) {
    reloj.paso(t);
    dibujar();
    if (t - ultima > 500) {
      ultima = t; pintarEstado(); if (seleccionado) seleccionado = cuerpos.find((c) => c.id === seleccionado.id) || seleccionado; pintarFicha();
      $("fecha").textContent = formatoUtc(reloj.jdUtc); $("sub").textContent = `${cfg.lugarTexto}: ${fmt(obs.lat, 2)}°, ${fmt(obs.lon, 2)}° E · campo ${fmt(vista.fov / RAD, 0)}°`;
      if (document.activeElement !== $("iFecha")) $("iFecha").value = valorInputUtc(reloj.jdUtc);
    }
    requestAnimationFrame(cuadro);
  }
  reloj.fijar(reloj.jdUtc); mirar(vista.az / RAD, vista.alt / RAD);
  requestAnimationFrame(cuadro);
  window.__cielo = { obs, reloj, vista, sol, sis, est, get cuerpos() { return cuerpos; } };
}
