// SPDX-License-Identifier: Apache-2.0
// Pruebas del motor de simuladores (sin red, sin navegador): node simuladores/pruebas/ejecutar.mjs
import { readFileSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { sistemaDesdeBytes } from "../motor/efemerides.js";
import { crearGeometria } from "../motor/eclipses.js";
import { crearAstronomia } from "../motor/astronomia.js";
import { jdUtcDesdeTdb, jdTdbDesdeUtc, jdUtcDesdeMs, JD_UTC_INICIO, JD_UTC_FIN, formatoUtc, jdUtcDesdeInput, valorInputUtc } from "../motor/tiempo.js";
import { elementos, PLANETAS, baseDelCuerpo, poloEclipticoJ2000, orientacion, UA_KM, longitudSolar } from "../motor/cuerpos.js";

const aqui = dirname(fileURLToPath(import.meta.url));
const datos = join(aqui, "..", "datos");
let fallos = 0, ok = 0;
const afirmar = (cond, msg) => { if (cond) ok++; else { fallos++; console.log("FALLO:", msg); } };
const cerca = (a, b, tol, msg) => afirmar(Math.abs(a - b) <= tol, `${msg}: ${a} vs ${b} (tol ${tol})`);

function cargar(nombre) {
  const meta = JSON.parse(readFileSync(join(datos, `${nombre}.json`), "utf8"));
  return sistemaDesdeBytes(meta, readFileSync(join(datos, `${nombre}.bin`)));
}
const sistemas = {};
for (const n of ["sol", "tierra", "marte", "jupiter", "saturno", "urano", "neptuno"]) if (existsSync(join(datos, `${n}.bin`))) sistemas[n] = cargar(n);
const verif = JSON.parse(readFileSync(join(datos, "verificacion.json"), "utf8"));

// 1. Interpolación: reproduce el error medido contra JPL en épocas que no son nodos de la tabla
for (const [clave, v] of Object.entries(verif)) {
  const [sis, id] = clave.split("/");
  if (!sistemas[sis]) continue;
  const t = sistemas[sis].cuerpo(id);
  let peor = 0;
  for (const [jd, x, y, z] of v.epocas) {
    const p = t.pos(jd);
    peor = Math.max(peor, Math.hypot(p[0] - x, p[1] - y, p[2] - z));
  }
  afirmar(peor <= v.error_max_km * 1.001 + 0.01, `${clave} (${v.nombre}): error ${peor} km > ${v.error_max_km}`);
}
console.log(`interpolación: ${Object.keys(verif).length} cuerpos comprobados`);

// 2. Tolerancias de calidad por cuerpo (relativas al radio orbital)
for (const [n, s] of Object.entries(sistemas)) {
  for (const c of s.meta.cuerpos) {
    const a = c.a_km || (n === "sol" ? 1.5e8 : 1e6);
    const lim = n === "sol" ? 300 : Math.max(5, 6e-4 * a);
    afirmar(c.error_max_km <= lim, `${n}/${c.nombre}: error máx ${c.error_max_km} km > ${lim}`);
  }
}

// 3. Tiempo
cerca(JD_UTC_INICIO, 2461406.5, 1e-9, "JD 2027-01-01");
afirmar(formatoUtc(jdUtcDesdeMs(Date.UTC(2040, 5, 15, 12, 30, 5))) === "2040-06-15 12:30:05 UTC", "formato UTC");
cerca(jdUtcDesdeInput(valorInputUtc(2461500.25)), 2461500.25, 1e-6, "ida y vuelta input fecha");
cerca(jdTdbDesdeUtc(2461406.5) - 2461406.5, 69.184 / 86400, 1e-9, "TDB-UTC");

// 4. Sistema Solar: distancias reales
if (sistemas.sol) {
  const sol = sistemas.sol;
  const jd = jdTdbDesdeUtc(JD_UTC_INICIO);
  const d = (id) => Math.hypot(...sol.pos(id, jd)) / UA_KM;
  console.log("distancias al Sol 2027-01-01 (UA):", ["199", "299", "399", "499", "599", "699", "799", "899", "9"].map((i) => d(i).toFixed(3)).join(" "));
  cerca(d("399"), 0.9833, 0.0015, "Tierra cerca del perihelio a inicios de enero"); // ~0,9833 UA
  cerca(d("599"), 5.0, 0.6, "Júpiter ~5 UA"); cerca(d("899"), 30.0, 0.5, "Neptuno ~30 UA");
  // elementos osculadores de la Tierra
  const tE = sol.cuerpo("399"); const el = elementos(tE.pos(jd), tE.vel(jd), 132712440041.94 + 398600.435 + 4902.8);
  cerca(el.a / UA_KM, 1.0, 0.003, "a de la Tierra"); cerca(el.e, 0.0167, 0.0015, "e de la Tierra"); cerca(el.i, 0.0, 0.01, "i de la Tierra (eclíptica J2000)");
  // continuidad: sin saltos en 24 años
  for (const c of sol.meta.cuerpos) {
    const t = sol.cuerpo(c.id); let prev = t.pos(jd), maxSalto = 0;
    for (let k = 1; k <= 400; k++) { const p = t.pos(jd + k * 21.9); maxSalto = Math.max(maxSalto, Math.hypot(p[0] - prev[0], p[1] - prev[1], p[2] - prev[2])); prev = p; }
    const v = Math.hypot(...t.vel(jd)) * 86400 * 21.9 * 4;
    afirmar(maxSalto < v, `${c.nombre}: salto inesperado`);
  }
}

// 5. Orientación: polo de la Tierra y de Marte en la eclíptica
{
  const polo = poloEclipticoJ2000(orientacion(PLANETAS["399"].polo, 2451545.0));
  cerca(polo[2], Math.cos(23.4392911 * Math.PI / 180), 1e-9, "polo terrestre J2000 vs oblicuidad");
  const b = baseDelCuerpo(PLANETAS["499"].polo, 2461406.5);
  cerca(b.x[0] * b.y[0] + b.x[1] * b.y[1] + b.x[2] * b.y[2], 0, 1e-9, "base ortogonal");
}

// 5b. Marte: longitud solar Ls. Por definición, el perihelio de Marte ocurre en Ls ≈ 251° (convención de Clancy et al. 2000)
if (sistemas.sol) {
  const m = sistemas.sol.cuerpo("499");
  const dist = (jd) => Math.hypot(...m.pos(jd));
  const ls = (jd) => longitudSolar(m.pos(jd), m.vel(jd), baseDelCuerpo(PLANETAS["499"].polo, jd).z);
  const dif = (a, b) => Math.abs(((a - b + 540) % 360) - 180);
  const j0 = jdTdbDesdeUtc(JD_UTC_INICIO); let n = 0, peor = 0;
  for (let jd = j0 + 1; jd < j0 + 8700; jd += 1) {
    if (dist(jd) < dist(jd - 1) && dist(jd) < dist(jd + 1)) {
      let lo = jd - 1, hi = jd + 1; // mínimo por sección áurea
      for (let k = 0; k < 40; k++) { const c = lo + (hi - lo) * 0.382, d = lo + (hi - lo) * 0.618; if (dist(c) < dist(d)) hi = d; else lo = c; }
      const v = ls((lo + hi) / 2); peor = Math.max(peor, dif(v, 251)); n++;
    }
  }
  afirmar(n >= 12, `perihelios de Marte encontrados: ${n}`);
  afirmar(peor < 3, `Ls en el perihelio de Marte se aparta ${peor.toFixed(2)}° de 251°`);
  // continuidad y sentido: Ls crece ~0,5°/día
  const v1 = ls(j0), v2 = ls(j0 + 10);
  afirmar(dif(v2 - v1, 5) < 2.5, `Ls crece ${((v2 - v1 + 360) % 360).toFixed(2)}° en 10 d`);
  console.log(`Marte Ls: ${n} perihelios, peor desvío de 251°: ${peor.toFixed(2)}°`);
}

// 5c. Estaciones de los gigantes: la latitud subsolar sale de la posición del Sol y del polo IAU
if (sistemas.sol) {
  const lat = (id, jd) => { const r = sistemas.sol.cuerpo(id).pos(jd); const d = Math.hypot(...r); const z = baseDelCuerpo(PLANETAS[id].polo, jd).z; return Math.asin(-(r[0] * z[0] + r[1] * z[1] + r[2] * z[2]) / d) * 180 / Math.PI; };
  const j0 = jdTdbDesdeUtc(JD_UTC_INICIO), anio = (jd) => 2027 + (jd - j0) / 365.25;
  // Urano: latitud subsolar máxima = 180° - 97,77° = 82,2°. Desde el equinoccio de 2007-12 el Sol tarda ~22,8 años en alcanzar el solsticio
  // (parte del afelio, donde el planeta va más lento): hacia 2030
  let mejor = -99, tmax = 0;
  for (let jd = j0; jd < j0 + 8766; jd += 5) { const l = lat("799", jd); if (l > mejor) { mejor = l; tmax = jd; } }
  afirmar(Math.abs(mejor - 82.2) < 0.7, `latitud subsolar máxima de Urano ${mejor.toFixed(2)}°`);
  afirmar(anio(tmax) > 2029.5 && anio(tmax) < 2031.0, `solsticio de Urano en ${anio(tmax).toFixed(2)}`);
  // Saturno: el Sol cruza el plano de los anillos hacia 2039 (equinoccio)
  let cruce = null;
  for (let jd = j0; jd < j0 + 8766; jd += 1) { const a = lat("699", jd), b = lat("699", jd + 1); if (a * b < 0) { cruce = jd; break; } }
  afirmar(cruce !== null && anio(cruce) > 2038.5 && anio(cruce) < 2040.0, `equinoccio de Saturno en ${cruce ? anio(cruce).toFixed(2) : "ninguno"}`);
  console.log(`Urano: latitud subsolar máx ${mejor.toFixed(2)}° en ${anio(tmax).toFixed(2)}; Saturno: el Sol cruza el plano de los anillos en ${cruce ? formatoUtc(jdUtcDesdeTdb(cruce), false) : "-"}`);
}

// 6. Eclipses (Sol/Luna) contra el catálogo de la NASA
if (sistemas.sol && sistemas.tierra) {
  const geo = crearGeometria(sistemas.sol, sistemas.tierra);
  const lista = geo.buscar(jdTdbDesdeUtc(JD_UTC_INICIO), jdTdbDesdeUtc(JD_UTC_FIN));
  const f = (e) => `${formatoUtc(e.jdUtc, false)} ${e.tipo} ${e.clase}`;
  console.log(`eclipses 2027–2050 encontrados: ${lista.filter((e) => e.tipo === "solar").length} solares, ${lista.filter((e) => e.tipo === "lunar").length} lunares`);
  // Catálogo de la NASA (Espenak y Meeus), 2027–2050: debe coincidir uno a uno (mismo número, clase, hora del máximo y γ)
  const ref = JSON.parse(readFileSync(join(aqui, "referencia_nasa_eclipses.json"), "utf8")).eclipses;
  const claseNasa = (e) => (e.tipo === "solar" ? { T: ["total"], A: ["anular"], H: ["total", "anular"], P: ["parcial"] }[e.clase[0]] : { T: ["total"], P: ["parcial"], N: ["penumbral"] }[e.clase[0]]);
  const hms = (td) => { const [h, m, s] = td.split(":").map(Number); return h * 3600 + m * 60 + s; };
  let peorMin = 0, peorGamma = 0, peorMag = 0, n = 0;
  for (const r of ref) {
    const dia = Date.UTC(+r.fecha.slice(0, 4), +r.fecha.slice(5, 7) - 1, +r.fecha.slice(8, 10)) / 86400000 + 2440587.5; // 00:00 TD de ese día (TD ~ TDB)
    const jdNasa = dia + hms(r.td) / 86400; // JD en TD
    const e = lista.find((x) => x.tipo === r.tipo && Math.abs(x.jdTdb - jdNasa) < 0.25);
    afirmar(!!e, `eclipse NASA ${r.tipo} ${r.fecha} (${r.clase}) no encontrado`);
    if (!e) continue;
    n++;
    afirmar(claseNasa(r).includes(e.clase), `${r.fecha} ${r.tipo}: clase ${e.clase}, NASA ${r.clase}`);
    const dmin = Math.abs(e.jdTdb - jdNasa) * 1440; peorMin = Math.max(peorMin, dmin);
    afirmar(dmin < 3, `${r.fecha} ${r.tipo}: hora del máximo difiere ${dmin.toFixed(2)} min`);
    if (r.tipo === "solar") { const dg = Math.abs(e.gamma - Math.abs(r.gamma)); peorGamma = Math.max(peorGamma, dg); afirmar(dg < 0.01, `${r.fecha}: γ ${e.gamma.toFixed(4)} vs ${r.gamma}`); }
    else if (r.clase[0] !== "N") { const dm = Math.abs(e.mag_umbral - r.mag_umbral); peorMag = Math.max(peorMag, dm); afirmar(dm < 0.005, `${r.fecha}: magnitud umbral ${e.mag_umbral.toFixed(3)} vs ${r.mag_umbral}`); }
  }
  afirmar(lista.length === ref.length, `número de eclipses: ${lista.length} vs NASA ${ref.length}`);
  console.log(`eclipses contrastados con NASA: ${n}/${ref.length}; peor diferencia de hora ${peorMin.toFixed(2)} min, de γ ${peorGamma.toFixed(4)}, de magnitud umbral ${peorMag.toFixed(3)}`);
  // ningún eclipse inventado: cada lunación con eclipse solar debe tener γ < 1,6
  afirmar(lista.filter((e) => e.tipo === "solar").every((e) => e.gamma < 1.6), "γ fuera de rango");
}

// 7. Estaciones, ápsides y fases lunares frente al U.S. Naval Observatory (2027–2050)
if (sistemas.sol && sistemas.tierra) {
  const ast = crearAstronomia(sistemas.sol, sistemas.tierra);
  const usno = JSON.parse(readFileSync(join(aqui, "referencia_usno.json"), "utf8"));
  const j0 = jdTdbDesdeUtc(JD_UTC_INICIO) - 1, j1 = jdTdbDesdeUtc(JD_UTC_FIN) + 1;
  const cmp = (lista, refs, coincide, etiqueta, tolMin) => {
    let peor = 0, n = 0, suma = 0;
    for (const [f, h, tipo] of refs) {
      const jd = jdUtcDesdeInput(`${f}T${h}`); const e = lista.find((x) => Math.abs(x.jdUtc - jd) < 1.5 && coincide(x, tipo));
      afirmar(!!e, `${etiqueta} ${f} ${tipo} no encontrado`);
      if (!e) continue;
      const dm = (e.jdUtc - jd) * 1440; suma += dm; n++; peor = Math.max(peor, Math.abs(dm));
      afirmar(Math.abs(dm) < tolMin, `${etiqueta} ${f} ${tipo}: diferencia ${dm.toFixed(2)} min`);
    }
    afirmar(lista.length === refs.length, `${etiqueta}: ${lista.length} eventos y USNO tiene ${refs.length}`);
    console.log(`USNO · ${etiqueta}: ${n}/${refs.length}, peor diferencia ${peor.toFixed(2)} min, sesgo ${(suma / n).toFixed(2)} min`);
  };
  const FASE = { "New Moon": 0, "First Quarter": 1, "Full Moon": 2, "Last Quarter": 3 };
  cmp(ast.estaciones(j0, j1), usno.estaciones.filter((r) => /Equinox|Solstice/.test(r[2])), () => true, "equinoccios y solsticios", 2);
  cmp(ast.apsides(j0, j1), usno.estaciones.filter((r) => /Peri|Aph/.test(r[2])), (x, t) => (t === "Perihelion") === (x.nombre === "Perihelio"), "perihelio y afelio", 2);
  cmp(ast.fases(j0, j1), usno.fases, (x, t) => x.k === FASE[t], "fases de la Luna", 2.5);
}

// 7b. Oposiciones de Marte (fechas conocidas: 2027-02-19, 2029-03-25, 2031-05-04)
if (sistemas.sol && sistemas.tierra) {
  const ast = crearAstronomia(sistemas.sol, sistemas.tierra);
  const op = ast.oposiciones("499", jdTdbDesdeUtc(JD_UTC_INICIO), jdTdbDesdeUtc(JD_UTC_FIN));
  for (const [f, d] of [["2027-02-19", 0.678], ["2029-03-25", 0.649], ["2031-05-04", 0.559]]) {
    const o = op.find((x) => formatoUtc(x.jdUtc, false).startsWith(f));
    afirmar(!!o, `oposición de Marte del ${f} no encontrada`);
    if (o) cerca(o.dist_ua, d, 0.002, `distancia en la oposición de Marte ${f}`);
  }
  afirmar(op.length === 12, `oposiciones de Marte 2027–2050: ${op.length}`);
}

console.log(`\n${ok} comprobaciones correctas, ${fallos} fallos`);
process.exit(fallos ? 1 : 0);
