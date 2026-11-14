// SPDX-License-Identifier: Apache-2.0
// Genera las figuras SVG de los simuladores de cielo (simuladores/img/cielo-*.svg) con el MISMO motor que la página:
// cielo completo (proyección estereográfica centrada en el cénit) en un instante y lugar fijos.
// Uso: node simuladores/pruebas/generar_svg_cielo.mjs [--check]
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { sistemaDesdeBytes } from "../motor/efemerides.js";
import { Observador, ObservadorLuna, ecuatorialAEclipticoJ2000 } from "../motor/cielo.js";
import { jdUtcDesdeInput, jdTdbDesdeUtc, jdUtcDesdeTdb, formatoUtc } from "../motor/tiempo.js";
import { porkchop, trazaTransferencia } from "../motor/trayectoria.js";
import { asistencia as asist, desdeEncuentro as desdeEnc } from "../motor/asistencia.js";
import { COMETAS, hitosCometa, ETIQUETA as ETQ_COM } from "../motor/cometas.js";
import { crearCalendario, NOMBRE as NOMB_CAL, TIPOS as TIPOS_CAL, COLOR as COL_CAL } from "../motor/calendario.js";
import { crearNave } from "../motor/misiones.js";
import { crearGeometria } from "../motor/eclipses.js";
import { crearFranja } from "../motor/franja.js";
import { posicion as posAst } from "../motor/asteroides.js";
import { BITS, ANCHO as MW, ALTO as MH } from "../motor/mascara_tierra.js";

const aqui = dirname(fileURLToPath(import.meta.url)), datos = join(aqui, "..", "datos"), img = join(aqui, "..", "img");
const cargar = (n) => sistemaDesdeBytes(JSON.parse(readFileSync(join(datos, `${n}.json`), "utf8")), readFileSync(join(datos, `${n}.bin`)));
const cielo = JSON.parse(readFileSync(join(datos, "cielo.json"), "utf8"));
const RAD = Math.PI / 180, W = 1200, H = 675, H0 = 675;
const n1 = (x) => x.toFixed(1), coma = (s) => s.replace(/(\d)\.(\d)/g, "$1,$2");
const esc = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;");
const FIGURAS = [
  { archivo: "cielo-tierra", id: "399", sistema: "tierra", titulo: "Cielo desde la Tierra", lugar: "Santiago de Chile (33,45° S, 70,67° O)", lat: -33.45, lon: -70.67, fecha: "2027-03-21T01:00", fondo: "#02030a" },
  { archivo: "cielo-marte", id: "499", sistema: "marte", titulo: "Cielo desde Marte", lugar: "Cráter Jezero (18,44° N, 77,45° E)", lat: 18.44, lon: 77.45, fecha: "2027-03-21T13:00", fondo: "#02030a" },
  { archivo: "cielo-jupiter", id: "599", sistema: "jupiter", titulo: "Cielo desde Júpiter", lugar: "Cima de las nubes, latitud 22° S", lat: -22, lon: 0, fecha: "2027-03-21T00:00", fondo: "#02030a" },
  { archivo: "cielo-saturno", id: "699", sistema: "saturno", titulo: "Cielo desde Saturno", lugar: "Cima de las nubes, latitud 30° N", lat: 30, lon: 0, fecha: "2027-03-21T00:00", fondo: "#02030a" },
  { archivo: "cielo-europa", id: "599", luna: "502", sistema: "jupiter", titulo: "Cielo desde Europa", lugar: "Superficie de Europa, hemisferio que mira a Júpiter (20° N, 30° E)", lat: 20, lon: 30, fecha: "2027-03-21T00:00", fondo: "#02030a" },
  { archivo: "cielo-titania", id: "799", luna: "703", sistema: "urano", titulo: "Cielo desde Titania", lugar: "Superficie de Titania, hemisferio que mira a Urano (20° N, 30° E)", lat: 20, lon: 30, fecha: "2027-03-21T00:00", fondo: "#02030a" },
  { archivo: "cielo-triton", id: "899", luna: "801", sistema: "neptuno", titulo: "Cielo desde Tritón", lugar: "Superficie de Tritón, hemisferio que mira a Neptuno (20° N, 30° E)", lat: 20, lon: 30, fecha: "2027-03-21T00:00", fondo: "#02030a" },
  { archivo: "cielo-titan", id: "699", luna: "606", sistema: "saturno", titulo: "Cielo desde Titán", lugar: "Superficie de Titán, hemisferio que mira a Saturno (20° N, 30° E)", lat: 20, lon: 30, fecha: "2027-03-21T00:00", fondo: "#02030a" },
];

function figura(f, sol) {
  const sis = cargar(f.sistema), obs = f.luna ? new ObservadorLuna({ idPlaneta: f.id, idLuna: f.luna, sol, sis }) : new Observador({ id: f.id, sol, sis });
  const jdU = jdUtcDesdeInput(f.fecha), jd = jdTdbDesdeUtc(jdU);
  obs.lugar(f.lat, f.lon); obs.actualizar(jd, jdU);
  const cx = 330, cy = 350, R = 285;
  const P = (v) => { const z = v[0] * obs.up[0] + v[1] * obs.up[1] + v[2] * obs.up[2]; if (z < -0.0001) return null;
    const alt = Math.asin(Math.max(-1, Math.min(1, z))), az = Math.atan2(v[0] * obs.este[0] + v[1] * obs.este[1] + v[2] * obs.este[2], v[0] * obs.norte[0] + v[1] * obs.norte[1] + v[2] * obs.norte[2]);
    const r = R * Math.tan((Math.PI / 2 - alt) / 2); return [cx + r * Math.sin(az), cy - r * Math.cos(az)]; };   // N arriba, E a la derecha (visto desde dentro: E a la izquierda)
  const L = [`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-labelledby="t d" font-family="system-ui, Segoe UI, Roboto, sans-serif">`,
    `<title id="t">${esc(f.titulo)}</title>`, `<desc id="d">Cielo completo visto desde ${esc(f.lugar)} el ${formatoUtc(jdU, false)}: estrellas hasta la magnitud 4,5, constelaciones y astros calculados con efemérides de JPL Horizons.</desc>`,
    `<rect width="${W}" height="${H}" fill="#070a14"/>`, `<text x="32" y="44" font-size="28" fill="#e6ecf8" font-weight="600">${esc(f.titulo)}</text>`,
    `<text x="32" y="70" font-size="14" fill="#9fb0cf">${esc(f.lugar)} · ${formatoUtc(jdU, false)}</text>`,
    `<defs><clipPath id="c"><circle cx="${cx}" cy="${cy}" r="${R}"/></clipPath></defs>`, `<circle cx="${cx}" cy="${cy}" r="${R}" fill="#02030a" stroke="#26314f"/>`, `<g clip-path="url(#c)">`];
  // vista desde dentro: el este queda a la izquierda -> se refleja el eje x
  const Pm = (v) => { const p = P(v); return p ? [2 * cx - p[0], p[1]] : null; };
  let d = "";
  for (const fg of cielo.figuras) for (const l of fg.lineas) { let ant = null; for (const [ra, de] of l) { const v = ecuatorialAEclipticoJ2000(ra, de), p = Pm(v); if (ant && p) d += `M${n1(ant[0])} ${n1(ant[1])}L${n1(p[0])} ${n1(p[1])}`; ant = p; } }
  L.push(`<path d="${d}" fill="none" stroke="#5b7bb8" stroke-opacity="0.45" stroke-width="0.8"/>`);
  for (const [ra, de, mag] of cielo.estrellas) { if (mag > 4.5) continue; const p = Pm(ecuatorialAEclipticoJ2000(ra, de)); if (p) L.push(`<circle cx="${n1(p[0])}" cy="${n1(p[1])}" r="${(0.6 + (4.6 - mag) * 0.38).toFixed(1)}" fill="#dfe8ff"/>`); }
  const cuerpos = obs.cuerpos(), vis = [];
  for (const c of cuerpos) { if (c.alt < 0) continue; const p = Pm(c.dir); if (!p) continue; vis.push(c);
    if (c.tipo === "sol") L.push(`<circle cx="${n1(p[0])}" cy="${n1(p[1])}" r="9" fill="#ffd45e"/>`);
    else if (c.anfitrion) L.push(`<circle cx="${n1(p[0])}" cy="${n1(p[1])}" r="${n1(Math.max(4, c.tam * R / 4))}" fill="${c.color || "#ccc"}" fill-opacity="0.85"/>`);
    else if (c.tipo === "luna" && c.mag > 9) continue;
    else L.push(`<circle cx="${n1(p[0])}" cy="${n1(p[1])}" r="${Math.max(2.2, Math.min(6, 2.5 + (1 - c.mag) * 0.6)).toFixed(1)}" fill="${c.color || "#fff"}"/>`);
    L.push(`<text x="${n1(p[0] + 9)}" y="${n1(p[1] - 6)}" font-size="12" fill="#ffe9a8">${esc(c.nombre)}</text>`); }
  L.push(`</g>`);
  for (const [t, az] of [["N", 0], ["E", 90], ["S", 180], ["O", 270]]) { const x = cx - (R + 16) * Math.sin(az * RAD), y = cy - (R + 16) * Math.cos(az * RAD) + 5; L.push(`<text x="${n1(x)}" y="${n1(y)}" font-size="15" fill="#ffd45e" text-anchor="middle" font-weight="600">${t}</text>`); }
  // tabla
  L.push(`<rect x="660" y="100" width="508" height="520" rx="10" fill="#0b1020" stroke="#26314f"/>`, `<text x="680" y="130" font-size="14" fill="#ffd45e" font-weight="600">Sobre el horizonte (altura · acimut · magnitud)</text>`);
  const lista = vis.filter((c) => c.tipo !== "luna" || c.mag < 6).sort((a, b) => a.mag - b.mag).slice(0, 14);
  lista.forEach((c, i) => L.push(`<text x="680" y="${158 + i * 25}" font-size="14" fill="#e6ecf8">${esc(c.nombre)}</text><text x="1148" y="${158 + i * 25}" font-size="14" fill="#9fb0cf" text-anchor="end">${coma((c.alt / RAD).toFixed(0))}° · ${coma((c.az / RAD).toFixed(0))}° · ${coma(c.mag.toFixed(1))}</text>`));
  L.push(`<text x="680" y="600" font-size="11" fill="#9fb0cf">Estrellas: Hipparcos/Tycho (d3-celestial, BSD). Posiciones: NASA/JPL Horizons.</text>`, `<text x="${W - 32}" y="${H - 10}" font-size="11" fill="#9fb0cf" text-anchor="end">Esquema calculado con el motor del simulador · proyección estereográfica centrada en el cénit</text>`, `</svg>`);
  return L.join("\n") + "\n";
}


// ---- figura de trayectorias: porkchop Tierra -> Marte (C3) y la transferencia óptima sobre las órbitas
function figuraTrayectoria(sol) {
  const pk = porkchop(sol, "399", "499", { jdIni: jdTdbDesdeUtc(jdUtcDesdeInput("2028-06-01T00:00")), jdFin: jdTdbDesdeUtc(jdUtcDesdeInput("2029-08-01T00:00")), nSalida: 90, tofMin: 150, tofMax: 450, nTof: 90 });
  const ok = pk.celdas.filter(Boolean), mejor = ok.reduce((a, c) => (c.c3 < a.c3 ? c : a)), vmin = mejor.c3, vmax = vmin * 3;
  const x0 = 80, y0 = 110, w = 520, h = 480, jx0 = pk.fechas[0], jx1 = pk.fechas[pk.nSalida - 1], jy0 = jx0 + pk.tofs[0], jy1 = jx1 + pk.tofs[pk.nTof - 1];
  const X = (j) => x0 + (j - jx0) / (jx1 - jx0) * w, Y = (j) => y0 + h - (j - jy0) / (jy1 - jy0) * h;
  const pal = [[16, 24, 90], [24, 104, 170], [32, 168, 138], [168, 204, 64], [246, 210, 60], [232, 110, 46], [150, 24, 24]];
  const col = (t) => { const x = Math.max(0, Math.min(0.9999, t)) * 6, i = Math.floor(x), f = x - i; return pal[i].map((v, k) => Math.round(v + (pal[i + 1][k] - v) * f)); };
  const L = [`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H0}" width="${W}" height="${H0}" role="img" aria-labelledby="t d" font-family="system-ui, Segoe UI, Roboto, sans-serif">`,
    `<title id="t">Trayectorias entre planetas</title>`, `<desc id="d">Gráfico porkchop del C3 de salida Tierra–Marte entre junio de 2028 y agosto de 2029 y la transferencia óptima sobre las órbitas de la Tierra y Marte.</desc>`,
    `<rect width="${W}" height="${H0}" fill="#070a14"/>`, `<text x="32" y="44" font-size="28" fill="#e6ecf8" font-weight="600">Trayectorias entre planetas</text>`,
    `<text x="32" y="70" font-size="14" fill="#9fb0cf">Tierra → Marte · C3 de salida · mínimo ${coma(vmin.toFixed(1))} km²/s² con salida el ${formatoUtc(jdUtcDesdeTdb(mejor.jdSalida), false).slice(0, 10)} y ${coma(mejor.tof_d.toFixed(0))} días de vuelo</text>`,
    `<rect x="${x0}" y="${y0}" width="${w}" height="${h}" fill="#0b1020" stroke="#26314f"/>`];
  for (let i = 0; i < pk.nSalida - 1; i++) for (let j = 0; j < pk.nTof - 1; j++) { const c = pk.celdas[i * pk.nTof + j]; if (!c || c.c3 > vmax) continue; const t = Math.floor((c.c3 - vmin) / (vmax - vmin) * 16) / 16;
    L.push(`<path d="M${n1(X(pk.fechas[i]))} ${n1(Y(pk.fechas[i] + pk.tofs[j]))}L${n1(X(pk.fechas[i + 1]))} ${n1(Y(pk.fechas[i + 1] + pk.tofs[j]))}L${n1(X(pk.fechas[i + 1]))} ${n1(Y(pk.fechas[i + 1] + pk.tofs[j + 1]))}L${n1(X(pk.fechas[i]))} ${n1(Y(pk.fechas[i] + pk.tofs[j + 1]))}Z" fill="rgb(${col(t).join(",")})"/>`); }
  L.push(`<circle cx="${n1(X(mejor.jdSalida))}" cy="${n1(Y(mejor.jdLlegada))}" r="7" fill="none" stroke="#fff" stroke-width="2"/>`, `<text x="${x0 + w / 2}" y="${y0 + h + 40}" font-size="13" fill="#e6ecf8" text-anchor="middle">Fecha de salida (UTC) →</text>`, `<text x="30" y="${y0 + h / 2}" font-size="13" fill="#e6ecf8" text-anchor="middle" transform="rotate(-90 30 ${y0 + h / 2})">Fecha de llegada (UTC) →</text>`);
  for (const [j, a] of [[jx0, "2028-06"], [jx0 + (jx1 - jx0) / 2, "2029-01"], [jx1, "2029-08"]]) L.push(`<text x="${n1(X(j))}" y="${y0 + h + 18}" font-size="11" fill="#9fb0cf" text-anchor="middle">${a}</text>`);
  for (let k = 0; k <= 4; k++) L.push(`<rect x="${x0 + 10 + k * 40}" y="${y0 - 22}" width="40" height="10" fill="rgb(${col(k / 4 * 0.9999).join(",")})"/>`);
  L.push(`<text x="${x0 + 10}" y="${y0 - 28}" font-size="11" fill="#e6ecf8">${coma(vmin.toFixed(1))}</text><text x="${x0 + 210}" y="${y0 - 28}" font-size="11" fill="#e6ecf8" text-anchor="end">${coma(vmax.toFixed(0))}+ km²/s²</text>`);
  // vista cenital: órbitas de la Tierra y Marte, posiciones y transferencia
  const cx = 900, cy = 350, R = 255, esc = R / (1.7 * 149597870.7);
  L.push(`<rect x="650" y="110" width="518" height="480" rx="10" fill="#0b1020" stroke="#26314f"/>`, `<text x="666" y="136" font-size="13" fill="#ffd45e" font-weight="600">Transferencia óptima (vista desde el polo norte eclíptico)</text>`);
  for (const id of ["399", "499"]) { let d = ""; const P = id === "399" ? 365.256 : 686.98; for (let k = 0; k <= 160; k++) { const p = sol.pos(id, mejor.jdSalida + P * k / 160); d += (k ? "L" : "M") + n1(cx + p[0] * esc) + " " + n1(cy - p[1] * esc); } L.push(`<path d="${d}" fill="none" stroke="#7d93c0" stroke-opacity="0.45"/>`); }
  const tr = trazaTransferencia(mejor, 120); let dt = ""; for (let k = 0; k <= 120; k++) dt += (k ? "L" : "M") + n1(cx + tr[k * 3] * esc) + " " + n1(cy - tr[k * 3 + 1] * esc);
  L.push(`<path d="${dt}" fill="none" stroke="#ffe08a" stroke-width="2.2"/>`, `<circle cx="${cx}" cy="${cy}" r="7" fill="#ffd45e"/>`);
  for (const [id, j, nom, c] of [["399", mejor.jdSalida, "Tierra (salida)", "#3b82c4"], ["499", mejor.jdLlegada, "Marte (llegada)", "#c8643c"]]) { const p = sol.pos(id, j); L.push(`<circle cx="${n1(cx + p[0] * esc)}" cy="${n1(cy - p[1] * esc)}" r="6" fill="${c}"/>`, `<text x="${n1(cx + p[0] * esc + 10)}" y="${n1(cy - p[1] * esc - 8)}" font-size="12" fill="#e6ecf8">${nom}</text>`); }
  L.push(`<text x="666" y="570" font-size="11" fill="#9fb0cf">Cónicas empalmadas con la gravedad del Sol (Lambert, sin asistencias): herramienta didáctica.</text>`, `<text x="${W - 32}" y="${H0 - 10}" font-size="11" fill="#9fb0cf" text-anchor="end">Posiciones de los planetas: NASA/JPL Horizons · calculado con el motor del simulador</text>`, `</svg>`);
  return L.join("\n") + "\n";
}

// ---- figura de eclipses solares: franja del eclipse total del 2 de agosto de 2027
function figuraEclipse(sol) {
  const tierra = cargar("tierra"), geo = crearGeometria(sol, tierra), fr = crearFranja(sol, tierra, geo);
  const e = geo.buscar(jdTdbDesdeUtc(jdUtcDesdeInput("2027-07-30T00:00")), jdTdbDesdeUtc(jdUtcDesdeInput("2027-08-05T00:00"))).find((x) => x.tipo === "solar"), g = fr.mayorEclipse(e.jdTdb), tr = fr.trayectoria(g.jdTdb, 4);
  const bytes = Buffer.from(BITS, "base64"), tierraEn = (x, y) => (bytes[(y * MW + x) >> 3] >> (7 - ((y * MW + x) & 7))) & 1;
  const x0 = 60, y0 = 110, w = 1080, h = 540, X = (lon) => x0 + (lon + 180) / 360 * w, Y = (lat) => y0 + (90 - lat) / 180 * h;
  const L = [`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H0}" width="${W}" height="${H0}" role="img" aria-labelledby="t d" font-family="system-ui, Segoe UI, Roboto, sans-serif">`,
    `<title id="t">Eclipses solares</title>`, `<desc id="d">Franja de totalidad del eclipse solar total del 2 de agosto de 2027 sobre un mapamundi, calculada con efemérides de JPL.</desc>`,
    `<rect width="${W}" height="${H0}" fill="#070a14"/>`, `<text x="32" y="44" font-size="28" fill="#e6ecf8" font-weight="600">Eclipses solares</text>`,
    `<text x="32" y="70" font-size="14" fill="#9fb0cf">Eclipse total del 2 de agosto de 2027 · mayor eclipse a ${coma(Math.abs(g.lat).toFixed(1))}° N, ${coma(Math.abs(g.lon).toFixed(1))}° E · franja de ≈ ${g.anchoKm.toFixed(0)} km · fase central de ≈ ${Math.floor(g.duracion_s / 60)} min ${Math.round(g.duracion_s % 60)} s</text>`,
    `<rect x="${x0}" y="${y0}" width="${w}" height="${h}" fill="#0b1426" stroke="#26314f"/>`];
  let d = ""; const cw = w / MW, ch = h / MH;
  for (let y = 0; y < MH; y++) { let ini = -1; for (let x = 0; x <= MW; x++) { const t = x < MW && tierraEn(x, y); if (t && ini < 0) ini = x; if (!t && ini >= 0) { d += `M${n1(x0 + ini * cw)} ${n1(y0 + y * ch)}h${n1((x - ini) * cw)}v${n1(ch + 0.3)}h${n1(-(x - ini) * cw)}z`; ini = -1; } } }
  L.push(`<path d="${d}" fill="#26402c"/>`);
  for (const q of tr) { const rx = Math.max(1.5, q.anchoKm / 2 / 111.32 / Math.max(0.2, Math.cos(q.lat * Math.PI / 180)) / 360 * w), ry = Math.max(1.5, q.anchoKm / 2 / 111.32 / 180 * h); L.push(`<ellipse cx="${n1(X(q.lon))}" cy="${n1(Y(q.lat))}" rx="${n1(rx)}" ry="${n1(ry)}" fill="#ffb347" fill-opacity="0.9"/>`); }
  L.push(`<path d="M${tr.map((q) => n1(X(q.lon)) + " " + n1(Y(q.lat))).join("L")}" fill="none" stroke="#fff4d6" stroke-width="1.4"/>`);
  for (const q of tr) { const m = Math.round((q.jdTdb - tr[0].jdTdb) * 1440); if (m % 30 === 0) L.push(`<circle cx="${n1(X(q.lon))}" cy="${n1(Y(q.lat))}" r="3" fill="#fff"/>`, `<text x="${n1(X(q.lon) + 6)}" y="${n1(Y(q.lat) - 6)}" font-size="12" fill="#e6ecf8">${formatoUtc(jdUtcDesdeTdb(q.jdTdb), false).slice(11, 16)}</text>`); }
  L.push(`<text x="${W - 32}" y="${H0 - 10}" font-size="11" fill="#9fb0cf" text-anchor="end">Efemérides de NASA/JPL Horizons · tierra/mar: Natural Earth · horas en UTC · calculado con el motor del simulador</text>`, `</svg>`);
  return L.join("\n") + "\n";
}

// ---- figura de misiones: trayectorias de las naves a los planetas exteriores y su distancia al Sol
function figuraMisiones() {
  const ph = cargar("planetas_hist"), nv = cargar("misiones"), UA = 149597870.7;
  const L = [`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H0}" width="${W}" height="${H0}" role="img" aria-labelledby="t d" font-family="system-ui, Segoe UI, Roboto, sans-serif">`,
    `<title id="t">Misiones espaciales</title>`, `<desc id="d">Trayectorias de Pioneer 10 y 11, Voyager 1 y 2 y New Horizons vistas desde el polo norte eclíptico, y la velocidad de Voyager 2 con sus cuatro asistencias gravitatorias, con datos de JPL.</desc>`,
    `<rect width="${W}" height="${H0}" fill="#070a14"/>`, `<text x="32" y="44" font-size="28" fill="#e6ecf8" font-weight="600">Misiones espaciales</text>`,
    `<text x="32" y="70" font-size="14" fill="#9fb0cf">Pioneer 10 y 11, Voyager 1 y 2 y New Horizons · trayectorias reconstruidas por JPL (las posteriores a 2026 son predicciones)</text>`];
  const cx = 330, cy = 360, R = 250, esc = R / (46 * UA);
  L.push(`<rect x="60" y="100" width="540" height="520" rx="10" fill="#0b1020" stroke="#26314f"/>`, `<text x="76" y="126" font-size="13" fill="#ffd45e" font-weight="600">Vista desde el polo norte eclíptico (hasta 46 UA)</text>`);
  for (const [id, P] of [["599", 4333], ["699", 10759], ["799", 30688], ["899", 60182]]) { L.push(`<circle cx="${cx}" cy="${cy}" r="${n1(ph.cuerpo(id).pos(2451545 + 0)[0] ? Math.hypot(...ph.cuerpo(id).pos(2451545)) * esc : 0)}" fill="none" stroke="#7d93c0" stroke-opacity="0.3" stroke-dasharray="3 4"/>`); }
  L.push(`<circle cx="${cx}" cy="${cy}" r="5" fill="#ffd45e"/>`);
  const NAVES = [["-23", "Pioneer 10", "#ffb454"], ["-24", "Pioneer 11", "#ffd166"], ["-31", "Voyager 1", "#6cb4ff"], ["-32", "Voyager 2", "#7ee0a1"], ["-98", "New Horizons", "#ff7a7a"]];
  for (const [id, nom, col] of NAVES) { const t = nv.cuerpo(id); let d = "", ult = null; for (let k = 0; k <= 400; k++) { const jd = t.meta.jd_valido_ini + (Math.min(t.meta.jd_valido_fin, 2470172) - t.meta.jd_valido_ini) * k / 400, p = t.pos(jd), x = cx + p[0] * esc, y = cy - p[1] * esc; if (Math.hypot(p[0], p[1]) > 46 * UA) break; d += (d ? "L" : "M") + n1(x) + " " + n1(y); ult = [x, y]; } L.push(`<path d="${d}" fill="none" stroke="${col}" stroke-width="1.6"/>`); if (ult) L.push(`<text x="${n1(ult[0] + 4)}" y="${n1(ult[1] - 4)}" font-size="11" fill="${col}">${nom}</text>`); }
  // velocidad respecto del Sol de Voyager 2 y sus cuatro encuentros: cada asistencia gravitatoria deja su marca
  const EN = JSON.parse(readFileSync(join(datos, "encuentros.json"), "utf8")).encuentros, plan = new Map(["199", "299", "399", "499", "599", "699", "799", "899", "9"].map((i) => [i, ph.cuerpo(i)]));
  const NOMP = { "599": "Júpiter", "699": "Saturno", "799": "Urano", "899": "Neptuno" }, v2 = crearNave("-32", nv.cuerpo("-32"), EN, plan), x0 = 650, y0 = 100, w = 520, h = 520;
  const j0 = v2.ini, j1 = Math.min(v2.fin, 2470172), ax = (j) => x0 + 50 + (j - j0) / (j1 - j0) * (w - 80), ay = (v) => y0 + h - 50 - v / 40 * (h - 120);
  L.push(`<rect x="${x0}" y="${y0}" width="${w}" height="${h}" rx="10" fill="#0b1020" stroke="#26314f"/>`, `<text x="${x0 + 16}" y="${y0 + 26}" font-size="13" fill="#ffd45e" font-weight="600">Voyager 2: velocidad respecto del Sol (km/s) y asistencias gravitatorias</text>`);
  for (const v of [0, 10, 20, 30, 40]) L.push(`<path d="M${x0 + 50} ${n1(ay(v))}H${x0 + w - 30}" stroke="#26314f"/>`, `<text x="${x0 + 42}" y="${n1(ay(v) + 4)}" font-size="10" fill="#9fb0cf" text-anchor="end">${v}</text>`);
  for (const a of [1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050]) { const j = 2440587.5 + (a - 1970) * 365.25; if (j > j0 && j < j1) L.push(`<text x="${n1(ax(j))}" y="${y0 + h - 30}" font-size="10" fill="#9fb0cf" text-anchor="middle">${a}</text>`); }
  let d = ""; for (let k = 0; k <= 500; k++) { const j = j0 + (j1 - j0) * k / 500, v = Math.hypot(...v2.vel(j)); d += (k ? "L" : "M") + n1(ax(j)) + " " + n1(ay(v)); }
  L.push(`<path d="${d}" fill="none" stroke="#7ee0a1" stroke-width="2"/>`);
  const COLP = { "599": "#e8c18a", "699": "#ead7a2", "799": "#9be1e8", "899": "#5b7dff" };
  EN.filter((e) => e.nave === "-32" && NOMP[e.planeta]).forEach((e, i) => { const x = ax(e.jd_ca); L.push(`<path d="M${n1(x)} ${y0 + 50}V${y0 + h - 50}" stroke="${COLP[e.planeta]}" stroke-dasharray="3 4"/>`, `<text x="${n1(x + 6)}" y="${y0 + 66 + i * 30}" font-size="12" fill="${COLP[e.planeta]}">${NOMP[e.planeta]} ${formatoUtc(jdUtcDesdeTdb(e.jd_ca), false).slice(0, 4)}</text>`, `<text x="${n1(x + 6)}" y="${y0 + 82 + i * 30}" font-size="12" fill="${e.dv_helio > 0 ? "#7ee0a1" : "#ff8a8a"}">${e.dv_helio > 0 ? "▲" : "▼"} ${coma(Math.abs(e.dv_helio).toFixed(1))} km/s · ${coma(e.alt_km.toFixed(0)).replace(/\B(?=(\d{3})+(?!\d))/g, " ")} km de altura</text>`); });
  L.push(`<text x="${W - 32}" y="${H0 - 10}" font-size="11" fill="#9fb0cf" text-anchor="end">Trayectorias y encuentros: NASA/JPL Horizons (SPICE) · calculado con el motor del simulador</text>`, `</svg>`);
  return L.join("\n") + "\n";
}

// ---- figura del cinturón de asteroides el 1 de enero de 2027 (propagación kepleriana de los elementos de JPL)
function figuraAsteroides(sol) {
  const ast = JSON.parse(readFileSync(join(datos, "asteroides.json"), "utf8")).asteroides, UA = 149597870.7, jd = jdTdbDesdeUtc(jdUtcDesdeInput("2027-01-01T00:00")), NL = String.fromCharCode(10);
  const col = { MBA: "#9fb0cf", IMB: "#a8d08d", OMB: "#8ab4f8", MCA: "#f6b26b", TJN: "#ea9999", HYA: "#d5a6bd", IEO: "#ffd966", ATE: "#ffd966", APO: "#ffe599", AMO: "#ffe599" };
  const L = [`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H0}" width="${W}" height="${H0}" role="img" aria-labelledby="t d" font-family="system-ui, Segoe UI, Roboto, sans-serif">`,
    `<title id="t">Cinturón de asteroides</title>`, `<desc id="d">${ast.length} asteroides y las órbitas de Mercurio a Júpiter el 1 de enero de 2027, vistos desde el polo norte eclíptico.</desc>`,
    `<rect width="${W}" height="${H0}" fill="#070a14"/>`, `<text x="32" y="44" font-size="28" fill="#e6ecf8" font-weight="600">Cinturón de asteroides</text>`,
    `<text x="32" y="70" font-size="14" fill="#9fb0cf">${ast.length} asteroides del JPL Small-Body Database · 1 de enero de 2027 · posiciones keplerianas aproximadas (error medido en la documentación)</text>`];
  const cx = 600, cy = 365, R = 270, esc = R / (6 * UA);
  L.push(`<circle cx="${cx}" cy="${cy}" r="${R + 6}" fill="#0b1020" stroke="#26314f"/>`);
  for (const [id, nom] of [["199", "Mercurio"], ["299", "Venus"], ["399", "Tierra"], ["499", "Marte"], ["599", "Júpiter"]]) { const p = sol.pos(id, jd), r = Math.hypot(p[0], p[1]) * esc; L.push(`<circle cx="${cx}" cy="${cy}" r="${n1(r)}" fill="none" stroke="#7d93c0" stroke-opacity="0.35" stroke-dasharray="3 4"/>`, `<circle cx="${n1(cx + p[0] * esc)}" cy="${n1(cy - p[1] * esc)}" r="4" fill="#fff"/>`, `<text x="${n1(cx + p[0] * esc + 6)}" y="${n1(cy - p[1] * esc - 5)}" font-size="12" fill="#e6ecf8">${nom}</text>`); }
  L.push(`<circle cx="${cx}" cy="${cy}" r="5" fill="#ffd45e"/>`);
  for (const f of ast) { const p = posAst(f, jd), x = cx + p[0] * esc, y = cy - p[1] * esc; if ((x - cx) ** 2 + (y - cy) ** 2 < R * R) L.push(`<circle cx="${n1(x)}" cy="${n1(y)}" r="1.1" fill="${col[f[3]] || "#ccc"}"/>`); }
  L.push(`<text x="${W - 32}" y="${H0 - 10}" font-size="11" fill="#9fb0cf" text-anchor="end">Elementos orbitales: NASA/JPL Small-Body Database · planetas: NASA/JPL Horizons · calculado con el motor del simulador</text>`, `</svg>`);
  return L.join(NL) + NL;
}

// ---- figura del calendario planetario: oposición de Marte del 19 de febrero de 2027 y lista de los próximos fenómenos
function figuraCalendario(sol) {
  const cal = crearCalendario(sol), J0 = jdTdbDesdeUtc(jdUtcDesdeInput("2027-01-01T00:00")), J1 = jdTdbDesdeUtc(jdUtcDesdeInput("2050-12-31T23:59")), NL = String.fromCharCode(10);
  const todos = cal.todos(J0, J1), op = todos.find((e) => e.tipo === "oposicion" && e.planeta === "499"), UA = 149597870.7;
  const L = [`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H0}" width="${W}" height="${H0}" role="img" aria-labelledby="t d" font-family="system-ui, Segoe UI, Roboto, sans-serif">`,
    `<title id="t">Calendario planetario</title>`, `<desc id="d">Geometría Sol–Tierra–Marte en la oposición del 19 de febrero de 2027, la longitud de Marte menos la del Sol de 2027 a 2037 con sus oposiciones y los fenómenos planetarios de los primeros meses de 2027, calculados con efemérides de JPL.</desc>`,
    `<rect width="${W}" height="${H0}" fill="#070a14"/>`, `<text x="32" y="44" font-size="28" fill="#e6ecf8" font-weight="600">Calendario planetario</text>`,
    `<text x="32" y="70" font-size="14" fill="#9fb0cf">${todos.length} fenómenos entre 2027 y 2050 · oposiciones, conjunciones, cuadraturas, máximas elongaciones y estacionarios · efemérides de JPL</text>`];
  // diagrama a la fecha de la oposición
  const cx = 230, cy = 360, R = 170, k = R / 1.9, P = (v) => [cx + v[0] / UA * k, cy - v[1] / UA * k], E = P(sol.pos("399", op.jdTdb)), M = P(sol.pos("499", op.jdTdb));
  L.push(`<rect x="40" y="100" width="380" height="520" rx="10" fill="#0b1020" stroke="#26314f"/>`, `<text x="56" y="126" font-size="13" fill="#ffd45e" font-weight="600">Oposición de Marte · ${formatoUtc(op.jdUtc, false).slice(0, 16)} UTC</text>`);
  for (const a of [0.387, 0.723, 1, 1.524]) L.push(`<circle cx="${cx}" cy="${cy}" r="${n1(a * k)}" fill="none" stroke="#7d93c0" stroke-opacity="0.35" stroke-dasharray="3 4"/>`);
  L.push(`<path d="M${n1(E[0])} ${n1(E[1])}L${cx} ${cy}" stroke="#ffd45e" stroke-width="1.4"/>`, `<path d="M${n1(E[0])} ${n1(E[1])}L${n1(M[0])} ${n1(M[1])}" stroke="${COL_CAL["499"]}" stroke-width="1.4"/>`, `<circle cx="${cx}" cy="${cy}" r="9" fill="#ffd45e"/>`,
    `<circle cx="${n1(E[0])}" cy="${n1(E[1])}" r="6" fill="${COL_CAL["399"]}"/><text x="${n1(E[0] + 10)}" y="${n1(E[1] - 8)}" font-size="12" fill="#e6ecf8">Tierra</text>`,
    `<circle cx="${n1(M[0])}" cy="${n1(M[1])}" r="6" fill="${COL_CAL["499"]}"/><text x="${n1(M[0] + 10)}" y="${n1(M[1] - 8)}" font-size="12" fill="#e6ecf8">Marte · ${coma(op.dist_ua.toFixed(2))} UA</text>`,
    `<text x="${cx + 10}" y="${cy + 24}" font-size="12" fill="#ffd45e">Sol</text>`, `<text x="56" y="600" font-size="11" fill="#9fb0cf">Vista desde el polo norte eclíptico · el Sol, la Tierra y Marte alineados</text>`);
  // longitud de Marte menos la del Sol de 2027 a 2037
  const x0 = 480, y0 = 110, w = 690, h = 230, jf = jdTdbDesdeUtc(jdUtcDesdeInput("2037-12-31T00:00")), X = (j) => x0 + 40 + (j - J0) / (jf - J0) * (w - 60), Y = (v) => y0 + h - 25 - (v + 180) / 360 * (h - 85);
  L.push(`<rect x="${x0}" y="${y0}" width="${w}" height="${h}" rx="10" fill="#0b1020" stroke="#26314f"/>`, `<text x="${x0 + 16}" y="${y0 + 24}" font-size="13" fill="#ffd45e" font-weight="600">Longitud de Marte menos la del Sol: cada oposición es un paso por ±180°</text>`);
  for (const v of [-180, -90, 0, 90, 180]) L.push(`<path d="M${x0 + 40} ${n1(Y(v))}H${x0 + w - 20}" stroke="#26314f"/>`, `<text x="${x0 + 34}" y="${n1(Y(v) + 4)}" font-size="10" fill="#9fb0cf" text-anchor="end">${v}°</text>`);
  for (let a = 2027; a <= 2037; a += 2) L.push(`<text x="${n1(X(jdTdbDesdeUtc(jdUtcDesdeInput(a + "-01-01T00:00"))))}" y="${y0 + h - 8}" font-size="10" fill="#9fb0cf" text-anchor="middle">${a}</text>`);
  let d = "", prev = null; for (let i = 0; i <= 1400; i++) { const j = J0 + (jf - J0) * i / 1400, v = cal.elLon("499", j) * 180 / Math.PI; d += (prev === null || Math.abs(v - prev) > 180 ? "M" : "L") + n1(X(j)) + " " + n1(Y(v)); prev = v; }
  L.push(`<path d="${d}" fill="none" stroke="${COL_CAL["499"]}" stroke-width="1.8"/>`);
  for (const e of todos.filter((q) => q.tipo === "oposicion" && q.planeta === "499" && q.jdTdb < jf)) L.push(`<circle cx="${n1(X(e.jdTdb))}" cy="${n1(Y(180))}" r="4" fill="#ffd45e"/>`, `<text x="${n1(X(e.jdTdb))}" y="${n1(Y(180) - 8)}" font-size="10" fill="#ffd45e" text-anchor="middle">${formatoUtc(e.jdUtc, false).slice(0, 7)}</text>`);
  // fenómenos de los primeros meses de 2027
  const ty = 370, lista = todos.filter((e) => e.jdUtc < jdUtcDesdeInput("2027-12-31T00:00")).filter((e) => !["est_retro", "est_directo", "cuad_este", "cuad_oeste"].includes(e.tipo)).slice(0, 14);
  L.push(`<rect x="${x0}" y="${ty}" width="${w}" height="250" rx="10" fill="#0b1020" stroke="#26314f"/>`, `<text x="${x0 + 16}" y="${ty + 24}" font-size="13" fill="#ffd45e" font-weight="600">Fenómenos de 2027 (UTC)</text>`);
  lista.forEach((e, i) => { const col = i < 7 ? 0 : 1, fila = i % 7, tx = x0 + 16 + col * 340, tyy = ty + 50 + fila * 26, nom = e.planeta2 ? `${NOMB_CAL[e.planeta]}–${NOMB_CAL[e.planeta2]} (conjunción)` : `${NOMB_CAL[e.planeta]}: ${TIPOS_CAL[e.tipo].toLowerCase()}`;
    L.push(`<circle cx="${tx}" cy="${tyy - 4}" r="4" fill="${COL_CAL[e.planeta]}"/>`, `<text x="${tx + 12}" y="${tyy}" font-size="12" fill="#e6ecf8">${formatoUtc(e.jdUtc, false).slice(5, 16)} · ${esc(nom)}</text>`); });
  L.push(`<text x="${W - 32}" y="${H0 - 10}" font-size="11" fill="#9fb0cf" text-anchor="end">Posiciones aparentes: NASA/JPL Horizons · calculado con el motor del simulador</text>`, `</svg>`);
  return L.join(NL) + NL;
}

// ---- figura de cometas: órbitas de seis cometas entre 2027 y 2050 y sus perihelios
function figuraCometas(sol) {
  const com = cargar("cometas"), UA = 149597870.7, NL = String.fromCharCode(10), J0 = jdTdbDesdeUtc(jdUtcDesdeInput("2027-01-01T00:00")), J1 = jdTdbDesdeUtc(jdUtcDesdeInput("2050-12-31T23:59"));
  const ids = ["2P", "9P", "67P", "55P", "96P", "1P"], L = [`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H0}" width="${W}" height="${H0}" role="img" aria-labelledby="t d" font-family="system-ui, Segoe UI, Roboto, sans-serif">`,
    `<title id="t">Cometas</title>`, `<desc id="d">Órbitas de los cometas Encke, Tempel 1, Churyumov–Gerasimenko, Tempel–Tuttle, Machholz 1 y Halley entre 2027 y 2050 vistas desde el polo norte eclíptico, y sus perihelios, con efemérides de JPL.</desc>`,
    `<rect width="${W}" height="${H0}" fill="#070a14"/>`, `<text x="32" y="44" font-size="28" fill="#e6ecf8" font-weight="600">Cometas</text>`,
    `<text x="32" y="70" font-size="14" fill="#9fb0cf">${Object.keys(COMETAS).length} cometas periódicos · tramos 2027–2050 de sus órbitas (predicción de JPL) · escala comprimida (√ de la distancia)</text>`];
  const cx = 360, cy = 370, R = 255, rfit = 36, P = (v) => { const r = Math.hypot(v[0], v[1]) / UA; if (r < 1e-9) return [cx, cy]; const k = Math.sqrt(r / rfit) * R / r; return [cx + v[0] / UA * k, cy - v[1] / UA * k]; };
  L.push(`<circle cx="${cx}" cy="${cy}" r="${R + 6}" fill="#0b1020" stroke="#26314f"/>`);
  for (const [id, a] of [["199", 0.387], ["399", 1], ["599", 5.203], ["799", 19.19]]) L.push(`<circle cx="${cx}" cy="${cy}" r="${n1(Math.sqrt(a / rfit) * R)}" fill="none" stroke="#7d93c0" stroke-opacity="0.3" stroke-dasharray="3 4"/>`);
  for (const [id, a, n] of [["399", 1, "Tierra"], ["599", 5.203, "Júpiter"], ["799", 19.19, "Urano"]]) L.push(`<text x="${n1(cx + Math.sqrt(a / rfit) * R + 4)}" y="${cy - 4}" font-size="10" fill="#9fb0cf">${n}</text>`);
  for (const id of ids) { const t = com.cuerpo(id); let d = ""; for (let k = 0; k <= 500; k++) { const p = P(t.pos(J0 + (J1 - J0) * k / 500)); d += (k ? "L" : "M") + n1(p[0]) + " " + n1(p[1]); } L.push(`<path d="${d}" fill="none" stroke="${COMETAS[id].color}" stroke-width="1.8"/>`); const p0 = P(t.pos(J0)); L.push(`<circle cx="${n1(p0[0])}" cy="${n1(p0[1])}" r="3.5" fill="${COMETAS[id].color}"/>`);
    for (const h of hitosCometa(t, sol).filter((x) => x.tipo === "perihelio")) { const p = P(t.pos(h.jdTdb)); L.push(`<circle cx="${n1(p[0])}" cy="${n1(p[1])}" r="3" fill="#ffd45e" stroke="${COMETAS[id].color}"/>`); } }
  L.push(`<circle cx="${cx}" cy="${cy}" r="6" fill="#ffd45e"/>`);
  // lista de perihelios
  const x0 = 660, y0 = 100, w = 510, h = 520, filas = []; for (const id of Object.keys(COMETAS)) for (const q of hitosCometa(com.cuerpo(id), sol).filter((x) => x.tipo === "perihelio")) filas.push([q.jdTdb, id, q.dist_ua]);
  filas.sort((a, b) => a[0] - b[0]);
  L.push(`<rect x="${x0}" y="${y0}" width="${w}" height="${h}" rx="10" fill="#0b1020" stroke="#26314f"/>`, `<text x="${x0 + 16}" y="${y0 + 26}" font-size="13" fill="#ffd45e" font-weight="600">Próximos perihelios entre 2027 y 2050 (UTC)</text>`);
  filas.slice(0, 18).forEach(([j, id, d], i) => L.push(`<circle cx="${x0 + 22}" cy="${y0 + 52 + i * 26 - 4}" r="4" fill="${COMETAS[id].color}"/>`, `<text x="${x0 + 34}" y="${y0 + 52 + i * 26}" font-size="13" fill="#e6ecf8">${formatoUtc(jdUtcDesdeTdb(j), false).slice(0, 10)} · ${esc(COMETAS[id].nombre)}</text>`, `<text x="${x0 + w - 18}" y="${y0 + 52 + i * 26}" font-size="13" fill="#9fb0cf" text-anchor="end">${coma(d.toFixed(2))} UA</text>`));
  L.push(`<text x="${W - 32}" y="${H0 - 10}" font-size="11" fill="#9fb0cf" text-anchor="end">Efemérides de NASA/JPL Horizons (predicción) · calculado con el motor del simulador</text>`, `</svg>`);
  return L.join(NL) + NL;
}

// ---- figura de asistencias gravitatorias: Voyager 2 en Júpiter (1979) y las mayores ganancias de velocidad
function figuraAsistencias() {
  const ph = cargar("planetas_hist"), EN = JSON.parse(readFileSync(join(datos, "encuentros.json"), "utf8")), NL = String.fromCharCode(10), RJ = EN.radio_km["599"];
  const e = EN.encuentros.find((x) => x.nave === "-32" && x.planeta === "599"), Vp = Math.hypot(...ph.cuerpo("599").vel(e.jd_ca)), d = desdeEnc(e, EN.gm_km3_s2["599"], Vp), r = d.r;
  const miles = (x) => Math.round(x).toString().split("").reverse().join("").replace(/(\d{3})(?=\d)/g, "$1 ").split("").reverse().join("");
  const L = [`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H0}" width="${W}" height="${H0}" role="img" aria-labelledby="t d" font-family="system-ui, Segoe UI, Roboto, sans-serif">`,
    `<title id="t">Asistencias gravitatorias</title>`, `<desc id="d">Asistencia gravitatoria de Voyager 2 en Júpiter el 9 de julio de 1979: la hipérbola respecto del planeta, el diagrama de velocidades respecto del Sol y las mayores ganancias de velocidad de las misiones, con datos de JPL.</desc>`,
    `<rect width="${W}" height="${H0}" fill="#070a14"/>`, `<text x="32" y="44" font-size="28" fill="#e6ecf8" font-weight="600">Asistencias gravitatorias</text>`,
    `<text x="32" y="70" font-size="14" fill="#9fb0cf">Voyager 2 en Júpiter, 9 de julio de 1979 · pasó a ${miles(e.alt_km)} km de la superficie y ganó ${coma(e.dv_helio.toFixed(1))} km/s respecto del Sol</text>`];
  // hipérbola en el sistema de Júpiter
  const cx = 250, cy = 330, rp = e.dist_km, vista = rp * 3, k = 170 / vista, a = -r.a, b = a * Math.sqrt(r.e * r.e - 1), Hm = Math.acosh(Math.max(1.0001, (vista / a + 1) / r.e)), th = Math.acos(-1 / r.e);
  const Q = (x, y) => [cx - x * k, cy - y * k], en = (h) => Q(a * (r.e - Math.cosh(h)), b * Math.sinh(h));
  L.push(`<rect x="40" y="100" width="420" height="520" rx="10" fill="#0b1020" stroke="#26314f"/>`, `<text x="56" y="126" font-size="13" fill="#ffd45e" font-weight="600">En el sistema de Júpiter: una hipérbola (planeta a escala)</text>`);
  for (const f of [1, 2, 3]) L.push(`<circle cx="${cx}" cy="${cy}" r="${n1(rp * f * k)}" fill="none" stroke="#7d93c0" stroke-opacity="0.25"/>`);
  L.push(`<circle cx="${cx}" cy="${cy}" r="${n1(RJ * k)}" fill="#e8c18a"/>`);
  let dd = ""; for (let i = -80; i <= 80; i++) { const p = en(Hm * i / 80); dd += (i === -80 ? "M" : "L") + n1(p[0]) + " " + n1(p[1]); } L.push(`<path d="${dd}" fill="none" stroke="#fff" stroke-width="2.4"/>`);
  const nn = Math.hypot(Math.sin(th), r.e - 1 / r.e), vi = [-Math.sin(th) / nn, -(r.e - 1 / r.e) / nn], vo = [Math.sin(th) / nn, -(r.e - 1 / r.e) / nn], pI = en(-Hm), pO = en(Hm), Lf = 70;
  const fl = (x0, y0, x1, y1, col) => { const an = Math.atan2(y1 - y0, x1 - x0); return `<path d="M${n1(x0)} ${n1(y0)}L${n1(x1)} ${n1(y1)}" stroke="${col}" stroke-width="2.6"/><path d="M${n1(x1)} ${n1(y1)}L${n1(x1 - 10 * Math.cos(an - 0.4))} ${n1(y1 - 10 * Math.sin(an - 0.4))}L${n1(x1 - 10 * Math.cos(an + 0.4))} ${n1(y1 - 10 * Math.sin(an + 0.4))}Z" fill="${col}"/>`; };
  L.push(fl(pI[0], pI[1], pI[0] + vi[0] * Lf, pI[1] + vi[1] * Lf, "#6cb4ff"), fl(pO[0] - vo[0] * Lf, pO[1] - vo[1] * Lf, pO[0], pO[1], "#7ee0a1"), `<text x="${n1(pI[0] + 10)}" y="${n1(pI[1] - 4)}" font-size="12" fill="#6cb4ff">v∞ de entrada ${coma(e.vinf_kms.toFixed(1))} km/s</text>`, `<text x="${n1(pO[0] + 10)}" y="${n1(pO[1] + 10)}" font-size="12" fill="#7ee0a1">v∞ de salida (girada ${coma(e.desvio_deg.toFixed(0))}°)</text>`);
  const pp = Q(rp, 0); L.push(`<circle cx="${n1(pp[0])}" cy="${n1(pp[1])}" r="4.5" fill="none" stroke="#ffd45e" stroke-width="1.5"/>`, `<text x="${n1(pp[0] - 8)}" y="${n1(pp[1] - 12)}" font-size="12" fill="#ffd45e" text-anchor="end">periastro</text>`);
  // triángulo de velocidades respecto del Sol
  const ox = 670, oy = 570, ek = 330 / Math.max(r.vhIn, r.vhOut, Vp + e.vinf_kms), T = (v) => [ox + v[0] * ek, oy - v[1] * ek], pT = T([0, Vp]), ai = T(r.hin), ao = T(r.hout);
  L.push(`<rect x="500" y="100" width="340" height="520" rx="10" fill="#0b1020" stroke="#26314f"/>`, `<text x="516" y="126" font-size="13" fill="#ffd45e" font-weight="600">En el sistema del Sol: sumar velocidades</text>`,
    `<circle cx="${n1(pT[0])}" cy="${n1(pT[1])}" r="${n1(e.vinf_kms * ek)}" fill="none" stroke="#7d93c0" stroke-opacity="0.5"/>`,
    fl(ox, oy, pT[0], pT[1], "#e8c18a"), fl(pT[0], pT[1], ai[0], ai[1], "#6cb4ff"), fl(pT[0], pT[1], ao[0], ao[1], "#7ee0a1"), fl(ox, oy, ai[0], ai[1], "#6cb4ff"), fl(ox, oy, ao[0], ao[1], "#7ee0a1"),
    `<text x="${n1(ox - 10)}" y="${n1((oy + pT[1]) / 2)}" font-size="12" fill="#e8c18a" text-anchor="end">Júpiter ${coma(Vp.toFixed(1))} km/s</text>`, `<text x="${n1(ai[0] + 10)}" y="${n1(ai[1] + 4)}" font-size="12" fill="#6cb4ff">antes ${coma(r.vhIn.toFixed(1))} km/s</text>`, `<text x="${n1(ao[0] - 10)}" y="${n1(ao[1] - 8)}" font-size="12" fill="#7ee0a1" text-anchor="end">después ${coma(r.vhOut.toFixed(1))} km/s</text>`);
  // mayores ganancias de velocidad
  const NP = { "199": "Mercurio", "299": "Venus", "399": "Tierra", "499": "Marte", "599": "Júpiter", "699": "Saturno", "799": "Urano", "899": "Neptuno" };
  const top = EN.encuentros.filter((x) => !x.orbita && x.dv_helio).sort((p, q) => q.dv_helio - p.dv_helio).slice(0, 10), tx = 870;
  L.push(`<rect x="${tx}" y="100" width="${W - tx - 32}" height="520" rx="10" fill="#0b1020" stroke="#26314f"/>`, `<text x="${tx + 14}" y="126" font-size="13" fill="#ffd45e" font-weight="600">Mayores ganancias (km/s)</text>`);
  top.forEach((x, i) => L.push(`<text x="${tx + 14}" y="${160 + i * 44}" font-size="13" fill="#e6ecf8">${esc(x.nombre)} · ${NP[x.planeta]}</text>`, `<text x="${tx + 14}" y="${178 + i * 44}" font-size="12" fill="#9fb0cf">${formatoUtc(jdUtcDesdeTdb(x.jd_ca), false).slice(0, 10)}</text>`, `<text x="${W - 46}" y="${170 + i * 44}" font-size="15" fill="#7ee0a1" text-anchor="end">▲ ${coma(x.dv_helio.toFixed(1))}</text>`));
  L.push(`<text x="${W - 32}" y="${H0 - 10}" font-size="11" fill="#9fb0cf" text-anchor="end">Encuentros: NASA/JPL Horizons (SPICE) · cónicas empalmadas · calculado con el motor del simulador</text>`, `</svg>`);
  return L.join(NL) + NL;
}

const sol = cargar("sol");
let mal = 0;
for (const f of FIGURAS) {
  if (!existsSync(join(datos, `${f.sistema}.bin`)) || !existsSync(join(aqui, "..", `${f.archivo}.html`))) continue;  // sólo las páginas publicadas
  const svg = figura(f, sol), ruta = join(img, `${f.archivo}.svg`);
  if (process.argv.includes("--check")) { if (!existsSync(ruta) || readFileSync(ruta, "utf8").replace(/\r\n/g, "\n") !== svg) { console.log(`ERROR ${f.archivo}.svg desfasada: ejecute node simuladores/pruebas/generar_svg_cielo.mjs`); mal++; } }
  else writeFileSync(ruta, svg);
}
if (existsSync(join(aqui, "..", "asistencias.html")) && existsSync(join(datos, "encuentros.json"))) {
  const svg = figuraAsistencias(), ruta = join(img, "asistencias.svg");
  if (process.argv.includes("--check")) { if (!existsSync(ruta) || readFileSync(ruta, "utf8").split(String.fromCharCode(13)).join("") !== svg) { console.log("ERROR asistencias.svg desfasada: ejecute node simuladores/pruebas/generar_svg_cielo.mjs"); mal++; } }
  else writeFileSync(ruta, svg);
}
if (existsSync(join(aqui, "..", "cometas.html")) && existsSync(join(datos, "cometas.bin"))) {
  const svg = figuraCometas(sol), ruta = join(img, "cometas.svg");
  if (process.argv.includes("--check")) { if (!existsSync(ruta) || readFileSync(ruta, "utf8").split(String.fromCharCode(13)).join("") !== svg) { console.log("ERROR cometas.svg desfasada: ejecute node simuladores/pruebas/generar_svg_cielo.mjs"); mal++; } }
  else writeFileSync(ruta, svg);
}
if (existsSync(join(aqui, "..", "calendario.html"))) {
  const svg = figuraCalendario(sol), ruta = join(img, "calendario.svg");
  if (process.argv.includes("--check")) { if (!existsSync(ruta) || readFileSync(ruta, "utf8").split(String.fromCharCode(13)).join("") !== svg) { console.log("ERROR calendario.svg desfasada: ejecute node simuladores/pruebas/generar_svg_cielo.mjs"); mal++; } }
  else writeFileSync(ruta, svg);
}
if (existsSync(join(aqui, "..", "asteroides.html")) && existsSync(join(datos, "asteroides.json"))) {
  const svg = figuraAsteroides(sol), ruta = join(img, "asteroides.svg");
  if (process.argv.includes("--check")) { if (!existsSync(ruta) || readFileSync(ruta, "utf8").split(String.fromCharCode(13)).join("") !== svg) { console.log("ERROR asteroides.svg desfasada: ejecute node simuladores/pruebas/generar_svg_cielo.mjs"); mal++; } }
  else writeFileSync(ruta, svg);
}
if (existsSync(join(aqui, "..", "misiones.html"))) {
  const svg = figuraMisiones(), ruta = join(img, "misiones.svg");
  if (process.argv.includes("--check")) { if (!existsSync(ruta) || readFileSync(ruta, "utf8").replace(/\r\n/g, "\n") !== svg) { console.log("ERROR misiones.svg desfasada: ejecute node simuladores/pruebas/generar_svg_cielo.mjs"); mal++; } }
  else writeFileSync(ruta, svg);
}
if (existsSync(join(aqui, "..", "eclipses-solares.html"))) {
  const svg = figuraEclipse(sol), ruta = join(img, "eclipses-solares.svg");
  if (process.argv.includes("--check")) { if (!existsSync(ruta) || readFileSync(ruta, "utf8").replace(/\r\n/g, "\n") !== svg) { console.log("ERROR eclipses-solares.svg desfasada: ejecute node simuladores/pruebas/generar_svg_cielo.mjs"); mal++; } }
  else writeFileSync(ruta, svg);
}
if (existsSync(join(aqui, "..", "trayectorias.html"))) {
  const svg = figuraTrayectoria(sol), ruta = join(img, "trayectorias.svg");
  if (process.argv.includes("--check")) { if (!existsSync(ruta) || readFileSync(ruta, "utf8").replace(/\r\n/g, "\n") !== svg) { console.log("ERROR trayectorias.svg desfasada: ejecute node simuladores/pruebas/generar_svg_cielo.mjs"); mal++; } }
  else writeFileSync(ruta, svg);
}
console.log(mal ? `${mal} figuras desfasadas` : "figuras de cielo y trayectorias al día");
process.exit(mal ? 1 : 0);
