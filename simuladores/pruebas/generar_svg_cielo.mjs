// SPDX-License-Identifier: Apache-2.0
// Genera las figuras SVG de los simuladores de cielo (simuladores/img/cielo-*.svg) con el MISMO motor que la página:
// cielo completo (proyección estereográfica centrada en el cénit) en un instante y lugar fijos.
// Uso: node simuladores/pruebas/generar_svg_cielo.mjs [--check]
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { sistemaDesdeBytes } from "../motor/efemerides.js";
import { Observador, ecuatorialAEclipticoJ2000 } from "../motor/cielo.js";
import { jdUtcDesdeInput, jdTdbDesdeUtc, formatoUtc } from "../motor/tiempo.js";

const aqui = dirname(fileURLToPath(import.meta.url)), datos = join(aqui, "..", "datos"), img = join(aqui, "..", "img");
const cargar = (n) => sistemaDesdeBytes(JSON.parse(readFileSync(join(datos, `${n}.json`), "utf8")), readFileSync(join(datos, `${n}.bin`)));
const cielo = JSON.parse(readFileSync(join(datos, "cielo.json"), "utf8"));
const RAD = Math.PI / 180, W = 1200, H = 675;
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

const sol = cargar("sol");
let mal = 0;
for (const f of FIGURAS) {
  if (!existsSync(join(datos, `${f.sistema}.bin`)) || !existsSync(join(aqui, "..", `${f.archivo}.html`))) continue;  // sólo las páginas publicadas
  const svg = figura(f, sol), ruta = join(img, `${f.archivo}.svg`);
  if (process.argv.includes("--check")) { if (!existsSync(ruta) || readFileSync(ruta, "utf8").replace(/\r\n/g, "\n") !== svg) { console.log(`ERROR ${f.archivo}.svg desfasada: ejecute node simuladores/pruebas/generar_svg_cielo.mjs`); mal++; } }
  else writeFileSync(ruta, svg);
}
console.log(mal ? `${mal} figuras desfasadas` : "figuras de cielo al día");
process.exit(mal ? 1 : 0);
