// SPDX-License-Identifier: Apache-2.0
// Genera las figuras SVG de los simuladores de cielo (simuladores/img/cielo-*.svg) con el MISMO motor que la página:
// cielo completo (proyección estereográfica centrada en el cénit) en un instante y lugar fijos.
// Uso: node simuladores/pruebas/generar_svg_cielo.mjs [--check]
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { sistemaDesdeBytes } from "../motor/efemerides.js";
import { Observador, ecuatorialAEclipticoJ2000 } from "../motor/cielo.js";
import { jdUtcDesdeInput, jdTdbDesdeUtc, jdUtcDesdeTdb, formatoUtc } from "../motor/tiempo.js";
import { porkchop, trazaTransferencia } from "../motor/trayectoria.js";

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
];

function figura(f, sol) {
  const sis = cargar(f.sistema), obs = new Observador({ id: f.id, sol, sis });
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

const sol = cargar("sol");
let mal = 0;
for (const f of FIGURAS) {
  if (!existsSync(join(datos, `${f.sistema}.bin`)) || !existsSync(join(aqui, "..", `${f.archivo}.html`))) continue;  // sólo las páginas publicadas
  const svg = figura(f, sol), ruta = join(img, `${f.archivo}.svg`);
  if (process.argv.includes("--check")) { if (!existsSync(ruta) || readFileSync(ruta, "utf8").replace(/\r\n/g, "\n") !== svg) { console.log(`ERROR ${f.archivo}.svg desfasada: ejecute node simuladores/pruebas/generar_svg_cielo.mjs`); mal++; } }
  else writeFileSync(ruta, svg);
}
if (existsSync(join(aqui, "..", "trayectorias.html"))) {
  const svg = figuraTrayectoria(sol), ruta = join(img, "trayectorias.svg");
  if (process.argv.includes("--check")) { if (!existsSync(ruta) || readFileSync(ruta, "utf8").replace(/\r\n/g, "\n") !== svg) { console.log("ERROR trayectorias.svg desfasada: ejecute node simuladores/pruebas/generar_svg_cielo.mjs"); mal++; } }
  else writeFileSync(ruta, svg);
}
console.log(mal ? `${mal} figuras desfasadas` : "figuras de cielo y trayectorias al día");
process.exit(mal ? 1 : 0);
