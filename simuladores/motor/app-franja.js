// SPDX-License-Identifier: Apache-2.0
// Simulador de eclipses solares: franja de totalidad (o anularidad) sobre un mapa y circunstancias locales en cualquier lugar.
import { cargarSistema } from "./efemerides.js";
import { crearGeometria } from "./eclipses.js";
import { crearFranja } from "./franja.js";
import { jdTdbDesdeUtc, jdUtcDesdeTdb, JD_UTC_INICIO, JD_UTC_FIN, formatoUtc } from "./tiempo.js";
import { BITS, ANCHO as MW, ALTO as MH } from "./mascara_tierra.js";
import { barraNavegacion } from "./navegacion.js";

const fmt = (x, d = 0) => x.toLocaleString("es-CL", { minimumFractionDigits: d, maximumFractionDigits: d });
const CLASE = { total: "total", anular: "anular", parcial: "parcial" };

export async function iniciarFranjas() {
  const raiz = document.getElementById("app");
  const cab = document.createElement("header"); cab.className = "cabecera"; cab.innerHTML = "<h1>Eclipses solares 2027–2050</h1>"; cab.appendChild(barraNavegacion("eclipses-solares")); document.body.insertBefore(cab, raiz);
  raiz.className = "app";
  raiz.innerHTML = `
    <section class="escena" aria-label="Mapa de la franja del eclipse">
      <canvas id="mapa" tabindex="0" aria-label="Mapamundi con la franja de totalidad o anularidad del eclipse elegido. Haga clic en un lugar para ver las circunstancias locales."></canvas>
      <div class="hud"><div class="fecha" id="titulo" style="font-size:1.05rem"></div><div class="sub" id="sub"></div></div>
      <div class="cargando" id="cargando"><div>Cargando efemérides…</div><progress id="prog" max="1" value="0"></progress></div>
    </section>
    <aside class="lateral" aria-label="Eclipses y datos">
      <h2>Eclipses solares</h2><div class="lista" id="lista" role="listbox" aria-label="Eclipses solares" style="max-height:230px"></div>
      <h2>Eclipse elegido</h2><div class="ficha" id="ficha" aria-live="polite"></div>
      <h2>Circunstancias locales</h2>
      <div style="display:flex;gap:6px;flex-wrap:wrap"><label class="etq">Latitud <input id="iLat" type="number" step="0.01" min="-90" max="90" style="width:84px"></label><label class="etq">Longitud E <input id="iLon" type="number" step="0.01" min="-180" max="180" style="width:84px"></label><button id="bLoc">Calcular</button></div>
      <p class="aviso">También puede hacer clic en el mapa.</p><div class="ficha" id="loc"></div>
      <details><summary>Modelo y límites</summary><div class="aviso">Franja: intersección del eje de la sombra (Sol–Luna, efemérides de JPL) con el elipsoide WGS 84; anchura por el radio de la umbra o antiumbra y la inclinación del rayo. Validado contra el catálogo de la NASA (34 eclipses centrales): lugar del mayor eclipse, anchura y magnitud. <strong>No incluye</strong> el relieve del limbo lunar, la refracción ni la altitud del terreno: la duración y los límites exactos de la franja pueden diferir de las predicciones oficiales.</div></details>
      <p class="aviso">Documentación: <a href="documentacion/README.html">documentación de los simuladores</a>.</p>
    </aside>`;
  const $ = (i) => document.getElementById(i);
  let sol, tierra;
  try { [sol, tierra] = await Promise.all([cargarSistema("sol", "datos", (f) => { $("prog").value = f / 2; }), cargarSistema("tierra", "datos")]); } catch (e) { $("cargando").classList.add("error"); $("cargando").innerHTML = `<div><strong>No se pudieron cargar los datos.</strong></div><div>${e.message}</div>`; return; }
  $("cargando").remove();
  const geo = crearGeometria(sol, tierra), fr = crearFranja(sol, tierra, geo);
  const todos = geo.buscar(jdTdbDesdeUtc(JD_UTC_INICIO), jdTdbDesdeUtc(JD_UTC_FIN)).filter((e) => e.tipo === "solar");
  $("lista").innerHTML = todos.map((e, i) => `<button data-i="${i}"><span>${formatoUtc(e.jdUtc, false).slice(0, 10)} · ${CLASE[e.clase]}</span><small>γ ${fmt(e.gamma, 3)}</small></button>`).join("");
  // máscara tierra/mar
  const bin = atob(BITS), mascara = new Uint8Array(bin.length); for (let i = 0; i < bin.length; i++) mascara[i] = bin.charCodeAt(i);
  const tierraEn = (x, y) => { const k = y * MW + x; return (mascara[k >> 3] >> (7 - (k & 7))) & 1; };
  const cv = $("mapa"), cx = cv.getContext("2d");
  let sel = null, tray = [], punto = null, W = 800, H = 400, ox = 0, oy = 0, esc = 1;
  const proy = (lat, lon) => [ox + (lon + 180) / 360 * W, oy + (90 - lat) / 180 * H];
  function dibujar() {
    const p = cv.parentElement, dpr = Math.min(2, devicePixelRatio || 1), pw = p.clientWidth, ph = p.clientHeight;
    if (cv.width !== pw * dpr || cv.height !== ph * dpr) { cv.width = pw * dpr; cv.height = ph * dpr; cv.style.width = pw + "px"; cv.style.height = ph + "px"; }
    cx.setTransform(dpr, 0, 0, dpr, 0, 0); cx.fillStyle = "#0b1426"; cx.fillRect(0, 0, pw, ph);
    W = Math.min(pw - 16, (ph - 70) * 2); H = W / 2; ox = (pw - W) / 2; oy = (ph - H) / 2 + 20;
    const celda = W / MW; cx.fillStyle = "#26402c";
    for (let y = 0; y < MH; y++) for (let x = 0; x < MW; x++) if (tierraEn(x, y)) cx.fillRect(ox + x * celda, oy + y * celda, celda + 0.4, celda + 0.4);
    cx.strokeStyle = "rgba(160,190,230,0.2)"; cx.lineWidth = 1; cx.beginPath();
    for (let lon = -180; lon <= 180; lon += 30) { const [x] = proy(0, lon); cx.moveTo(x, oy); cx.lineTo(x, oy + H); }
    for (let lat = -60; lat <= 60; lat += 30) { const [, y] = proy(lat, 0); cx.moveTo(ox, y); cx.lineTo(ox + W, y); }
    cx.stroke(); cx.strokeRect(ox, oy, W, H);
    if (tray.length) {
      // banda de la umbra: círculos con el ancho real (km -> grados) a lo largo de la línea central
      const off = document.createElement("canvas"); off.width = pw; off.height = ph; const o = off.getContext("2d"); o.fillStyle = "#ffb347";
      for (const q of tray) { const [x, y] = proy(q.lat, q.lon), rx = (q.anchoKm / 2 / 111.32 / Math.max(0.2, Math.cos(q.lat * Math.PI / 180))) / 360 * W, ry = (q.anchoKm / 2 / 111.32) / 180 * H; o.beginPath(); o.ellipse(x, y, Math.max(1.5, rx), Math.max(1.5, ry), 0, 0, 7); o.fill(); }
      cx.globalAlpha = 0.85; cx.drawImage(off, 0, 0, pw, ph); cx.globalAlpha = 1;
      cx.strokeStyle = "#fff4d6"; cx.lineWidth = 1.2; cx.beginPath(); let prev = null;
      for (const q of tray) { const [x, y] = proy(q.lat, q.lon); if (prev && Math.abs(x - prev[0]) < W / 2) cx.lineTo(x, y); else cx.moveTo(x, y); prev = [x, y]; } cx.stroke();
      cx.fillStyle = "#e6ecf8"; cx.font = "11px system-ui";
      for (const q of tray) { const m = Math.round((q.jdTdb - tray[0].jdTdb) * 1440); if (m % 30 === 0) { const [x, y] = proy(q.lat, q.lon); cx.beginPath(); cx.arc(x, y, 2.5, 0, 7); cx.fill(); cx.fillText(formatoUtc(jdUtcDesdeTdb(q.jdTdb), false).slice(11, 16), x + 5, y - 5); } }
      if (sel && sel.g) { const [x, y] = proy(sel.g.lat, sel.g.lon); cx.strokeStyle = "#fff"; cx.lineWidth = 2; cx.beginPath(); cx.arc(x, y, 7, 0, 7); cx.stroke(); }
    }
    if (punto) { const [x, y] = proy(punto[0], punto[1]); cx.strokeStyle = "#6cb4ff"; cx.lineWidth = 2; cx.beginPath(); cx.moveTo(x - 7, y); cx.lineTo(x + 7, y); cx.moveTo(x, y - 7); cx.lineTo(x, y + 7); cx.stroke(); }
  }
  function elegir(i) {
    const e = todos[i]; const g = fr.mayorEclipse(e.jdTdb); sel = { e, g };
    tray = g ? fr.trayectoria(g.jdTdb, 2) : [];
    for (const b of document.querySelectorAll("#lista button")) b.setAttribute("aria-current", String(+b.dataset.i === i));
    const f = [["Fecha del máximo (UTC)", formatoUtc(e.jdUtc, false)], ["Clase", CLASE[e.clase]], ["γ (gamma)", fmt(e.gamma, 4)]];
    if (g) f.push(["Mayor eclipse", `${fmt(Math.abs(g.lat), 1)}° ${g.lat >= 0 ? "N" : "S"} · ${fmt(Math.abs(g.lon), 1)}° ${g.lon >= 0 ? "E" : "O"}`], ["Altura del Sol allí", `${fmt(g.altSol, 0)}°`], ["Anchura de la franja", `≈ ${fmt(g.anchoKm, 0)} km`], ["Duración de la fase central", g.duracion_s ? `≈ ${Math.floor(g.duracion_s / 60)} min ${fmt(g.duracion_s % 60, 0)} s` : "—"]);
    else f.push(["Franja", "no hay línea central: el eje de la sombra no toca la Tierra (eclipse parcial)"]);
    $("ficha").innerHTML = `<dl class="datos">${f.map(([k, v]) => `<dt>${k}</dt><dd>${v}</dd>`).join("")}</dl>`;
    $("titulo").textContent = `Eclipse ${CLASE[e.clase]} del ${formatoUtc(e.jdUtc, false).slice(0, 10)}`; $("sub").textContent = g ? "franja naranja = totalidad/anularidad; puntos cada 30 min (UTC)" : "eclipse parcial: sin franja central";
    if (punto) local(punto[0], punto[1]);
    dibujar();
  }
  function local(lat, lon) {
    punto = [lat, lon]; $("iLat").value = lat.toFixed(2); $("iLon").value = lon.toFixed(2);
    if (!sel) return; const l = fr.local(lat, lon, sel.e.jdTdb);
    const vis = l.altSol > 0 && l.mag > 0;
    $("loc").innerHTML = `<dl class="datos"><dt>Magnitud máxima</dt><dd>${fmt(l.mag, 3)}</dd><dt>Obscuración</dt><dd>${fmt(l.obscuracion * 100, 1)} %</dd><dt>Instante del máximo (UTC)</dt><dd>${formatoUtc(l.jdUtc, false)}</dd><dt>Altura del Sol</dt><dd>${fmt(l.altSol, 1)}°</dd><dt>¿Se ve desde aquí?</dt><dd>${vis ? (l.mag >= 1 ? "sí: " + (sel.e.clase === "total" ? "total" : "anular") : "sí, parcial") : l.mag > 0 ? "el Sol está bajo el horizonte" : "no"}</dd></dl>`;
    dibujar();
  }
  $("lista").addEventListener("click", (ev) => { const b = ev.target.closest("button"); if (b) elegir(+b.dataset.i); });
  cv.addEventListener("click", (ev) => { const r = cv.getBoundingClientRect(), x = ev.clientX - r.left, y = ev.clientY - r.top; if (x < ox || x > ox + W || y < oy || y > oy + H) return; local(90 - (y - oy) / H * 180, (x - ox) / W * 360 - 180); });
  $("bLoc").onclick = () => local(Math.max(-90, Math.min(90, +$("iLat").value)), +$("iLon").value);
  new ResizeObserver(dibujar).observe(cv.parentElement);
  const m = /f=(\d{4}-\d{2}-\d{2})/.exec(location.hash), ini = m ? todos.findIndex((e) => formatoUtc(e.jdUtc, false).startsWith(m[1])) : -1;
  const primero = ini >= 0 ? ini : todos.findIndex((e) => formatoUtc(e.jdUtc, false).startsWith("2027-08-02"));
  elegir(primero >= 0 ? primero : 0);
  window.__franja = { fr, geo, todos };
}
