// SPDX-License-Identifier: Apache-2.0
// Pruebas del motor de simuladores (sin red, sin navegador): node simuladores/pruebas/ejecutar.mjs
import { readFileSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { sistemaDesdeBytes } from "../motor/efemerides.js";
import { crearGeometria } from "../motor/eclipses.js";
import { crearAstronomia } from "../motor/astronomia.js";
import { crearFranja } from "../motor/franja.js";
import { crearCalendario, NOMBRE as NOMBRE_CAL } from "../motor/calendario.js";
import { MISIONES, crearNave, posicionPlanetocentrica } from "../motor/misiones.js";
import { posicion as posAst } from "../motor/asteroides.js";
import { Observador, ObservadorLuna, salidasYPuestas, ecuatorialAEclipticoJ2000 } from "../motor/cielo.js";
import { SOL, LUNA } from "../motor/cuerpos.js";
import { lambert, propagar, evaluar, porkchop, elementosTransferencia, deltaVOrbita } from "../motor/trayectoria.js";
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
for (const n of ["sol", "tierra", "marte", "jupiter", "saturno", "urano", "neptuno", "pluton", "planetas_hist", "misiones"]) if (existsSync(join(datos, `${n}.bin`))) sistemas[n] = cargar(n);
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
    const lim = (n === "sol" || n === "planetas_hist") ? 300 : n === "misiones" ? 1e6 : Math.max(5, 6e-4 * a);
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

// 5d. Sistema de Plutón: baricentro fuera de Plutón; cociente de masas = cociente inverso de distancias al baricentro
if (sistemas.pluton) {
  const P = sistemas.pluton, jd = jdTdbDesdeUtc(JD_UTC_INICIO);
  const dP = Math.hypot(...P.pos("999", jd)), dC = Math.hypot(...P.pos("901", jd));
  const sep = Math.hypot(...[0, 1, 2].map((k) => P.pos("901", jd)[k] - P.pos("999", jd)[k]));
  cerca(dP / dC, 0.1218, 0.001, "cociente de masas Caronte/Plutón"); // M_Caronte/M_Plutón ≈ 0,1218 (New Horizons)
  cerca(sep, 19591, 15, "separación Plutón–Caronte [km]");
  afirmar(dP > 1188.3, "el baricentro debe quedar fuera de Plutón");
}

// 8. Cielo: salidas y puestas del Sol y de la Luna contra el USNO; geometría de los demás mundos
if (sistemas.sol && sistemas.tierra) {
  const ref = JSON.parse(readFileSync(join(aqui, "referencia_usno_salidas.json"), "utf8")).dias;
  const obs = new Observador({ id: "399", sol: sistemas.sol, sis: sistemas.tierra });
  const REF = 34 / 60 * Math.PI / 180;
  let peor = { sol: 0, luna: 0 }, n = { sol: 0, luna: 0 };
  for (const r of ref) {
    obs.lugar(r.lat, r.lon);
    const jd0 = jdUtcDesdeInput(r.fecha + "T00:00");
    const vSol = (j) => { const e = sistemas.sol.pos("399", j); return [-(e[0] + obs.rel[0]), -(e[1] + obs.rel[1]), -(e[2] + obs.rel[2])]; };
    const vLuna = (j) => { const m = sistemas.tierra.pos("301", j); return [m[0] - obs.rel[0], m[1] - obs.rel[1], m[2] - obs.rel[2]]; };
    for (const [clave, fn, radio, lista] of [["sol", vSol, SOL.radio, r.sol], ["luna", vLuna, LUNA.radio, r.luna]]) {
      obs.actualizar(jd0 + 0.5 + 69.184 / 86400, jd0 + 0.5);
      const um = -(REF + Math.asin(radio / Math.hypot(...fn(jd0 + 0.5 + 69.184 / 86400))));
      const ev = salidasYPuestas(obs, fn, um, jd0);
      for (const [phen, hhmm] of lista) {
        const t = jdUtcDesdeInput(r.fecha + "T" + hhmm);
        const dm = ev.filter((e) => e.tipo === (phen === "Rise" ? "salida" : "puesta")).map((e) => Math.abs((e.jdUtc - t) * 1440)).sort((a, b) => a - b)[0];
        afirmar(dm !== undefined && dm < 2, `${r.lugar} ${r.fecha} ${clave} ${phen}: ${dm === undefined ? "sin evento" : dm.toFixed(2) + " min"}`);
        if (dm !== undefined) { peor[clave] = Math.max(peor[clave], dm); n[clave]++; }
      }
    }
  }
  console.log(`USNO · salidas y puestas: Sol ${n.sol} (peor ${peor.sol.toFixed(2)} min), Luna ${n.luna} (peor ${peor.luna.toFixed(2)} min)`);
  // Polaris (AR 37,95°, Dec +89,26°) en el polo norte está a ~89,3° de altura; en el ecuador, a ~0°
  const jd = jdTdbDesdeUtc(JD_UTC_INICIO), pol = ecuatorialAEclipticoJ2000(37.95, 89.264);
  obs.lugar(90, 0); obs.actualizar(jd, JD_UTC_INICIO); cerca(obs.horizonte(pol).alt * 180 / Math.PI, 89.26, 0.15, "Polaris en el polo norte (altura)");
  obs.lugar(0, 0); obs.actualizar(jd, JD_UTC_INICIO); cerca(obs.horizonte(pol).alt * 180 / Math.PI, 0.7, 1.0, "Polaris en el ecuador (≈ 0°)");
  obs.lugar(-33.45, -70.67); obs.actualizar(jd, JD_UTC_INICIO); afirmar(obs.horizonte(pol).alt < 0, "Polaris no es visible desde Santiago");
  // la Luna desde la Tierra mide ≈ 29–34′ y el Sol ≈ 31,4–32,6′
  const c = obs.cuerpos(); const sol = c.find((x) => x.id === "10"), luna = c.find((x) => x.id === "301");
  cerca(sol.tam * 180 / Math.PI * 60, 32.5, 0.6, "diámetro angular del Sol en enero [′]"); afirmar(luna.tam * 180 / Math.PI * 60 > 29 && luna.tam * 180 / Math.PI * 60 < 34.2, "diámetro angular de la Luna");
}
if (sistemas.sol && sistemas.marte) {
  const o = new Observador({ id: "499", sol: sistemas.sol, sis: sistemas.marte }), jd = jdTdbDesdeUtc(JD_UTC_INICIO);
  o.lugar(18.44, 77.45); o.actualizar(jd, JD_UTC_INICIO);
  const c = o.cuerpos(); const sol = c.find((x) => x.id === "10"); const ang = sol.tam * 180 / Math.PI * 60;
  cerca(ang, 2 * Math.asin(SOL.radio / (1.6467 * 149597870.7)) * 180 / Math.PI * 60, 0.3, "Sol visto desde Marte [′]");   // ≈ 19,4′ en enero de 2027 (Marte a 1,65 UA)
  const fobos = c.find((x) => x.id === "401"); afirmar(fobos && fobos.tam * 180 / Math.PI * 60 > 3 && fobos.tam * 180 / Math.PI * 60 < 15, "tamaño angular de Fobos visto desde Marte");
  afirmar(c.some((x) => x.id === "399"), "la Tierra aparece en el cielo de Marte");
}
if (sistemas.sol && sistemas.jupiter) {
  const o = new Observador({ id: "599", sol: sistemas.sol, sis: sistemas.jupiter }), jd = jdTdbDesdeUtc(JD_UTC_INICIO);
  o.lugar(0, 0); o.actualizar(jd, JD_UTC_INICIO);
  const io = o.cuerpos().find((x) => x.id === "501"); const grados = io.tam * 180 / Math.PI;
  afirmar(grados > 0.25 && grados < 0.6, `Ío visto desde las nubes de Júpiter: ${grados.toFixed(2)}° (esperado ≈ 0,3–0,5°)`);
}

// 8b. Cielo desde las lunas: el planeta anfitrión (rotación síncrona) y el Sol
for (const [pid, sid, lid, nom, esperado] of [["599", "jupiter", "502", "Júpiter desde Europa", 12.2], ["799", "urano", "703", "Urano desde Titania", 6.7], ["899", "neptuno", "801", "Neptuno desde Tritón", 8.0], ["699", "saturno", "606", "Saturno desde Titán", 5.5]]) {
  if (!(sistemas.sol && sistemas[sid])) continue;
  const o = new ObservadorLuna({ idPlaneta: pid, idLuna: lid, sol: sistemas.sol, sis: sistemas[sid] }), jd0 = jdTdbDesdeUtc(JD_UTC_INICIO);
  o.lugar(0, 0); o.actualizar(jd0, JD_UTC_INICIO);
  const h = o.cuerpos().find((x) => x.anfitrion);
  afirmar(!!h, `${nom}: aparece el planeta anfitrión`);
  if (h) { cerca(h.tam * 180 / Math.PI, esperado, 0.5, `diámetro angular de ${nom} [°]`); cerca(h.alt * 180 / Math.PI, 90, 1, `${nom}: en el cénit del punto subplanetario [°]`);
    // rotación síncrona: en cualquier otro día el planeta sigue casi en el mismo lugar del cielo
    const jd1 = jd0 + 3.3; o.actualizar(jd1, jd1 - (jd0 - JD_UTC_INICIO) * 0 - (jd0 - JD_UTC_INICIO));
    const h2 = o.cuerpos().find((x) => x.anfitrion), dalt = Math.abs(h2.alt - h.alt) * 180 / Math.PI;
    afirmar(dalt < 12, `${nom}: casi fijo en el cielo (libración ${dalt.toFixed(1)}°)`); }
}

// 9. Trayectorias: problema de Lambert, propagación y ventanas Tierra–Marte/Júpiter/Venus
{
  // Ejemplo 5.2 de Curtis (Orbital Mechanics for Engineering Students): el resultado publicado es v1 = (-5,9925; 1,9254; 3,2456) y v2 = (-3,3125; -4,1966; -0,38529) km/s
  const L = lambert([5000, 10000, 2100], [-14600, 2500, 7000], 3600, 398600, true);
  afirmar(!!L, "Lambert (Curtis 5.2) sin solución");
  if (L) { [-5.9925, 1.9254, 3.2456].forEach((v, k) => cerca(L.v1[k], v, 5e-4, `Curtis 5.2 v1[${k}]`)); [-3.3125, -4.1966, -0.38529].forEach((v, k) => cerca(L.v2[k], v, 5e-4, `Curtis 5.2 v2[${k}]`));
    const p = propagar([5000, 10000, 2100], L.v1, 3600, 398600); [-14600, 2500, 7000].forEach((v, k) => cerca(p.r[k], v, 0.05, `propagación hasta r2[${k}] [km]`)); }
  // Hohmann Tierra–Marte con órbitas circulares y coplanares (ángulo de transferencia 179,99°): v∞ de salida 2,945 km/s y 258,8 d
  const mu = 132712440041.94, r1 = 149597870.7, r2 = 1.523679 * r1, th = 179.99 * Math.PI / 180;
  const a = (r1 + r2) / 2, tof = Math.PI * Math.sqrt(a ** 3 / mu), H = lambert([r1, 0, 0], [r2 * Math.cos(th), r2 * Math.sin(th), 0], tof, mu, true);
  afirmar(!!H, "Lambert Hohmann sin solución");
  if (H) { cerca(Math.hypot(H.v1[0], H.v1[1]) - Math.sqrt(mu / r1), Math.sqrt(mu / r1) * (Math.sqrt(2 * r2 / (r1 + r2)) - 1), 0.02, "Hohmann: Δv de salida [km/s]"); cerca(tof / 86400, 258.8, 0.3, "Hohmann: tiempo de vuelo Tierra–Marte [d]"); }
  cerca(deltaVOrbita(3.6, 398600.435, 6678.14), Math.sqrt(3.6 ** 2 + 2 * 398600.435 / 6678.14) - Math.sqrt(398600.435 / 6678.14), 1e-9, "Δv desde órbita circular");
}
if (sistemas.sol) {
  const sol = sistemas.sol, j0 = jdTdbDesdeUtc(JD_UTC_INICIO);
  const ventana = (desde, hacia, ini, fin, tmin, tmax) => porkchop(sol, desde, hacia, { jdIni: jdTdbDesdeUtc(jdUtcDesdeInput(ini)), jdFin: jdTdbDesdeUtc(jdUtcDesdeInput(fin)), nSalida: 120, tofMin: tmin, tofMax: tmax, nTof: 120 });
  const mejor = (pk, f) => pk.celdas.filter(Boolean).reduce((m, c) => (f(c) < f(m) ? c : m));
  // Marte: la ventana de salida de 2028-2029 (oposición 2029-03-25): C3 mínimo ≈ 8–15 km²/s² hacia diciembre de 2028 – febrero de 2029
  const pm = ventana("399", "499", "2028-08-01T00:00", "2029-06-01T00:00", 150, 450), bm = mejor(pm, (c) => c.c3);
  console.log(`Tierra→Marte 2028-29: C3 mín ${bm.c3.toFixed(2)} km²/s², salida ${formatoUtc(jdUtcDesdeTdb(bm.jdSalida), false)}, ${bm.tof_d.toFixed(0)} d, v∞ llegada ${bm.vinfLlegada.toFixed(2)} km/s`);
  afirmar(bm.c3 > 7 && bm.c3 < 16, `C3 mínimo Tierra→Marte: ${bm.c3.toFixed(2)}`);
  const d0 = jdUtcDesdeInput("2028-11-01T00:00"), d1 = jdUtcDesdeInput("2029-02-28T00:00"), sd = jdUtcDesdeTdb(bm.jdSalida);
  afirmar(sd > d0 && sd < d1, `la salida óptima a Marte cae entre noviembre de 2028 y febrero de 2029: ${formatoUtc(sd, false)}`);
  afirmar(bm.tof_d > 180 && bm.tof_d < 320, `tiempo de vuelo óptimo a Marte: ${bm.tof_d.toFixed(0)} d`);
  // Venus: salida hacia fines de 2027, C3 mínimo bajo (≈ 5–12), vuelo de 3–5 meses
  const pv = ventana("399", "299", "2027-06-01T00:00", "2028-06-01T00:00", 80, 250), bv = mejor(pv, (c) => c.c3);
  console.log(`Tierra→Venus 2027-28: C3 mín ${bv.c3.toFixed(2)} km²/s², salida ${formatoUtc(jdUtcDesdeTdb(bv.jdSalida), false)}, ${bv.tof_d.toFixed(0)} d`);
  afirmar(bv.c3 > 3 && bv.c3 < 16, `C3 mínimo Tierra→Venus: ${bv.c3.toFixed(2)}`);
  // Júpiter directo: Hohmann v∞ = 8,8 km/s (C3 ≈ 77); con la excentricidad real entre ≈ 75 y ≈ 95 km²/s²
  const pj = ventana("399", "599", "2027-01-01T00:00", "2028-06-01T00:00", 600, 1200), bj = mejor(pj, (c) => c.c3);
  console.log(`Tierra→Júpiter 2027-28: C3 mín ${bj.c3.toFixed(1)} km²/s², ${bj.tof_d.toFixed(0)} d`);
  afirmar(bj.c3 > 70 && bj.c3 < 100, `C3 mínimo Tierra→Júpiter: ${bj.c3.toFixed(1)}`);
  // consistencia: la nave llega al planeta (propagación de 2 cuerpos contra la posición de JPL)
  const ev = evaluar(sol, "399", "499", bm.jdSalida, bm.jdLlegada), pp = propagar(ev.r1, ev.v1, ev.tof_d * 86400), rr = sol.cuerpo("499").pos(bm.jdLlegada);
  cerca(Math.hypot(pp.r[0] - rr[0], pp.r[1] - rr[1], pp.r[2] - rr[2]), 0, 1, "la nave llega a Marte [km]");
  const el = elementosTransferencia(ev.r1, ev.v1); afirmar(el.perihelio < 1.02 * 149597870.7 && el.afelio > 1.3 * 149597870.7, "la transferencia a Marte va del perihelio terrestre al afelio marciano");
}

// 10. Movimiento propio estelar (Hipparcos): Sirio se desplaza ~ -1,223″/año en declinación
{
  const cielo = JSON.parse(readFileSync(join(datos, "cielo.json"), "utf8"));
  const i = cielo.estrellas.findIndex(([ra, de]) => Math.abs(ra - 101.287) < 0.01 && Math.abs(de + 16.716) < 0.01);
  afirmar(i >= 0, "Sirio presente en el catálogo");
  if (i >= 0) { const [pa, pd] = cielo.pm_mas_ano[i]; cerca(pa, -546, 2, "movimiento propio de Sirio en AR [mas/año]"); cerca(pd, -1223, 2, "movimiento propio de Sirio en Dec [mas/año]");
    cerca(pd * 50 / 1000, -61.15, 0.2, "desplazamiento de Sirio en 50 años [″]"); }
  const n = cielo.pm_mas_ano.filter(([a, d]) => Math.hypot(a, d) > 100).length;
  afirmar(n > 200 && n < 3000, `estrellas con movimiento propio > 100 mas/año: ${n}`);
}

// 11. Franjas de eclipses centrales 2027–2050 contra el catálogo de la NASA (34 eclipses): lugar del mayor eclipse, anchura y magnitud
if (sistemas.sol && sistemas.tierra) {
  const geo = crearGeometria(sistemas.sol, sistemas.tierra), fr = crearFranja(sistemas.sol, sistemas.tierra, geo);
  const ref = JSON.parse(readFileSync(join(aqui, "referencia_nasa_franjas.json"), "utf8")).eclipses;
  const todos = geo.buscar(jdTdbDesdeUtc(JD_UTC_INICIO), jdTdbDesdeUtc(JD_UTC_FIN)).filter((x) => x.tipo === "solar");
  let peorPos = 0, peorMag = 0, okAncho = 0, okDur = 0;
  for (const r of ref) {
    const jdn = Date.UTC(+r.fecha.slice(0, 4), +r.fecha.slice(5, 7) - 1, +r.fecha.slice(8, 10)) / 86400000 + 2440587.5 + r.td.split(":").reduce((a, x, i) => a + x * [3600, 60, 1][i], 0) / 86400;
    const e = todos.find((x) => Math.abs(x.jdTdb - jdn) < 0.25), g = e && fr.mayorEclipse(e.jdTdb);
    afirmar(!!g, `franja de ${r.fecha}: sin punto de mayor eclipse`);
    if (!g) continue;
    const dist = Math.hypot(g.lat - r.lat, (g.lon - r.lon) * Math.cos(r.lat * Math.PI / 180)); peorPos = Math.max(peorPos, dist);
    afirmar(dist < 1.0, `${r.fecha}: mayor eclipse a ${dist.toFixed(2)}° del catálogo (${g.lat.toFixed(1)}, ${g.lon.toFixed(1)} vs ${r.lat}, ${r.lon}; el catálogo redondea a 1°)`);
    if (Math.abs(g.anchoKm - r.ancho_km) <= Math.max(12, 0.12 * r.ancho_km)) okAncho++;
    if (g.duracion_s && Math.abs(g.duracion_s - r.dur_s) <= 0.1 * r.dur_s) okDur++;
    const loc = fr.local(g.lat, g.lon, e.jdTdb), dm = Math.abs(loc.mag - r.mag); peorMag = Math.max(peorMag, dm);
    afirmar(dm < 0.02, `${r.fecha}: magnitud en el mayor eclipse ${loc.mag.toFixed(4)} vs ${r.mag}`);
  }
  afirmar(okAncho >= 30, `anchura de la franja dentro de ±12 % (o 12 km): ${okAncho} de ${ref.length}`);
  console.log(`Franjas: ${ref.length} eclipses centrales; mayor eclipse a ≤ ${peorPos.toFixed(2)}°; anchura ±12 %: ${okAncho}; duración ±10 %: ${okDur}; magnitud ≤ ${peorMag.toFixed(4)}`);
}

// 12. Asteroides: propagación kepleriana contra Horizons (error medido; no es una efemérides oficial)
if (existsSync(join(datos, "asteroides.json")) && existsSync(join(aqui, "verificacion_asteroides.json"))) {
  const ast = JSON.parse(readFileSync(join(datos, "asteroides.json"), "utf8")), ver = JSON.parse(readFileSync(join(aqui, "verificacion_asteroides.json"), "utf8")).asteroides;
  const porId = new Map(ast.asteroides.map((f) => [f[0], f]));
  const errs = [[], [], []];
  for (const v of ver) { const f = porId.get(v.spkid); if (!f) continue; v.epocas.forEach(([jd, x, y, z], k) => { const p = posAst(f, jd); errs[k].push(Math.hypot(p[0] - x, p[1] - y, p[2] - z)); }); }
  const med = (a) => a.slice().sort((p, q) => p - q)[Math.floor(a.length / 2)], p95 = (a) => a.slice().sort((p, q) => p - q)[Math.floor(a.length * 0.95)];
  console.log(`Asteroides (${ast.asteroides.length}): error kepleriano vs Horizons en ${errs[0].length} cuerpos — 2030 mediana ${(med(errs[0]) / 1e3).toFixed(0)} mil km, 2039 ${(med(errs[1]) / 1e3).toFixed(0)} mil km, 2050 mediana ${(med(errs[2]) / 1e3).toFixed(0)} mil km (p95 ${(p95(errs[2]) / 1e3).toFixed(0)} mil km)`);
  afirmar(errs[0].length >= 20, "muestra de verificación de asteroides");
  afirmar(med(errs[0]) < 5e6 && med(errs[2]) < 2e7 && p95(errs[2]) < 2e8, `error kepleriano de asteroides en 2050 acotado: mediana ${med(errs[2]).toFixed(0)} km`);
  afirmar(ast.asteroides.length > 1000, "asteroides cargados");
}

// 13. Misiones: encuentros (sobrevuelos y asistencias) calculados con JPL Horizons contra las fechas y distancias históricas publicadas
if (existsSync(join(datos, "misiones.bin")) && existsSync(join(datos, "planetas_hist.bin")) && existsSync(join(datos, "encuentros.json"))) {
  const ph = cargar("planetas_hist"), nv = cargar("misiones"), EN = JSON.parse(readFileSync(join(datos, "encuentros.json"), "utf8"));
  const conocidos = { // [planeta, fecha publicada (UTC)]
    "-23": [["599", "1973-12-04"]], "-24": [["599", "1974-12-03"], ["699", "1979-09-01"]], "-31": [["599", "1979-03-05"], ["699", "1980-11-12"]],
    "-32": [["599", "1979-07-09"], ["699", "1981-08-26"], ["799", "1986-01-24"], ["899", "1989-08-25"]], "-77": [["299", "1990-02-10"], ["399", "1990-12-08"], ["399", "1992-12-08"], ["599", "1995-12-07"]],
    "-82": [["299", "1998-04-26"], ["299", "1999-06-24"], ["399", "1999-08-18"], ["599", "2000-12-30"], ["699", "2004-07-01"]],
    "-98": [["599", "2007-02-28"], ["9", "2015-07-14"]], "-61": [["399", "2013-10-09"], ["599", "2016-07-05"]], "-159": [["499", "2025-03-01"], ["399", "2026-12-03"], ["599", "2030-04-11"]],
    "-96": [["299", "2018-10-03"], ["299", "2019-12-26"], ["299", "2020-07-11"], ["299", "2021-02-20"], ["299", "2021-10-16"], ["299", "2023-08-21"], ["299", "2024-11-06"]],
    "-55": [["599", "1992-02-08"]], "-236": [["399", "2005-08-02"], ["299", "2006-10-24"], ["299", "2007-06-05"], ["199", "2008-01-14"], ["199", "2008-10-06"], ["199", "2009-09-29"]],
    "-226": [["399", "2005-03-04"], ["499", "2007-02-25"], ["399", "2007-11-13"], ["399", "2009-11-13"]], "-203": [["499", "2009-02-17"]],
    "-121": [["399", "2020-04-10"], ["299", "2020-10-15"], ["299", "2021-08-10"], ["199", "2021-10-01"], ["199", "2022-06-23"], ["199", "2023-06-19"], ["199", "2024-09-04"]],
    "-144": [["299", "2020-12-27"], ["299", "2021-08-09"], ["399", "2021-11-27"], ["299", "2022-09-04"]], "-49": [["399", "2022-10-16"], ["399", "2024-12-12"]],
    "-37": [["399", "2015-12-03"]], "-64": [["399", "2017-09-22"], ["399", "2023-09-24"]],
  };
  let n = 0;
  for (const [id, lista] of Object.entries(conocidos)) {
    afirmar(!!nv.cuerpo(id), `misión ${id} sin datos`);
    for (const [pid, fecha] of lista) {
      const jd = jdUtcDesdeInput(fecha + "T12:00"), e = EN.encuentros.filter((x) => x.nave === id && x.planeta === pid).map((x) => ({ x, d: Math.abs(jdUtcDesdeTdb(x.jd_ca) - jd) })).sort((a, b) => a.d - b.d)[0];
      afirmar(!!e && e.d < 0.75, `${MISIONES[id].nombre} ${pid} ${fecha}: ${e ? e.d.toFixed(2) + " d de diferencia" : "no detectado"}`); n++;
    }
  }
  // distancias publicadas del mayor acercamiento (km): Voyager 1–Júpiter 349 000 al centro (348 890), New Horizons–Plutón 12 500 sobre la superficie, Rosetta–Tierra 2005 a 1 954 km, Cassini–Tierra 1999 a 1 171 km, Cassini–Venus 284 y 600 km, Dawn–Marte 549 km
  const busca = (id, pid, f) => EN.encuentros.filter((x) => x.nave === id && x.planeta === pid).sort((a, b) => Math.abs(jdUtcDesdeTdb(a.jd_ca) - jdUtcDesdeInput(f + "T12:00")) - Math.abs(jdUtcDesdeTdb(b.jd_ca) - jdUtcDesdeInput(f + "T12:00")))[0];
  cerca(busca("-31", "599", "1979-03-05").dist_km, 348890, 1500, "Voyager 1 – Júpiter: distancia mínima al centro [km]");
  cerca(busca("-98", "9", "2015-07-14").alt_km, 12500, 150, "New Horizons – Plutón: altura mínima [km]");
  cerca(busca("-226", "399", "2005-03-04").alt_km, 1954, 25, "Rosetta – Tierra 2005: altura mínima [km]");
  cerca(busca("-82", "399", "1999-08-18").alt_km, 1171, 15, "Cassini – Tierra 1999: altura mínima [km]");
  cerca(busca("-82", "299", "1998-04-26").alt_km, 284, 15, "Cassini – Venus 1998: altura mínima [km]");
  cerca(busca("-82", "299", "1999-06-24").alt_km, 600, 15, "Cassini – Venus 1999: altura mínima [km]");
  cerca(busca("-203", "499", "2009-02-17").alt_km, 549, 15, "Dawn – Marte: altura mínima [km]");
  // asistencia: la velocidad en el infinito de Galileo en la Tierra (8,95 km/s publicada) y su ganancia heliocéntrica (≈ 5,2 km/s)
  const g1 = busca("-77", "399", "1990-12-08"); cerca(g1.vinf_kms, 8.95, 0.05, "Galileo – Tierra 1990: v∞ [km/s]"); cerca(g1.dv_helio, 5.2, 0.2, "Galileo – Tierra 1990: ganancia heliocéntrica [km/s]");
  // coherencia interna: la excentricidad y el desvío de cada hipérbola, y la interpolación de Hermite entre épocas
  let peorHermite = 0, vistos = 0;
  for (const e of EN.encuentros) {
    afirmar(Math.abs(e.alt_km - (e.dist_km - EN.radio_km[e.planeta])) < 0.2, `altura = distancia − radio (${e.nombre} ${e.planeta})`);
    if (!e.orbita) { const delta = 2 * Math.asin(1 / e.excentricidad) * 180 / Math.PI; cerca(e.desvio_deg, delta, 0.05, `desvío de ${e.nombre} en ${e.planeta}: 2·asin(1/e) [°]`); }
    if (!e.orbita) for (let k = 1; k < e.traza.length - 1; k += 3) {   // se omite una época y se interpola con las vecinas: error ≈ el de una malla del doble de paso
      const sin = [e.traza[k - 1], e.traza[k + 1]], r = posicionPlanetocentrica(sin, e.traza[k][0]), t = e.traza[k];
      const err = Math.hypot(r[0] - t[1], r[1] - t[2], r[2] - t[3]), d = Math.hypot(t[1], t[2], t[3]); peorHermite = Math.max(peorHermite, err / d); vistos++;
    }
  }
  afirmar(peorHermite < 0.03, `interpolación de Hermite de las trayectorias planetocéntricas: error relativo máximo ${(peorHermite * 100).toFixed(2)} % en ${vistos} épocas`);
  // la nave con precisión de encuentro pasa por el mayor acercamiento
  const planetasT = new Map(["199", "299", "399", "499", "599", "699", "799", "899", "9"].map((i) => [i, ph.cuerpo(i)]));
  const nave = crearNave("-82", nv.cuerpo("-82"), EN.encuentros, planetasT), cv = busca("-82", "399", "1999-08-18"), pn = nave.pos(cv.jd_ca), pt = ph.cuerpo("399").pos(cv.jd_ca);
  cerca(Math.hypot(pn[0] - pt[0], pn[1] - pt[1], pn[2] - pt[2]), cv.dist_km, 10, "Cassini pasa por el mayor acercamiento [km]");
  // heliopausa: Voyager 1 (2012-08-25) a ≈ 121 UA y Voyager 2 (2018-11-05) a ≈ 119 UA
  for (const [id, f, au] of [["-31", "2012-08-25", 121.6], ["-32", "2018-11-05", 119.0]]) { const r = nv.cuerpo(id).pos(jdTdbDesdeUtc(jdUtcDesdeInput(f + "T00:00"))); cerca(Math.hypot(...r) / UA_KM, au, 1.5, `distancia de ${MISIONES[id].nombre} al cruzar la heliopausa [UA]`); }
  // JWST en L2: ~ 1,5 millones de km de la Tierra, en el lado opuesto al Sol
  const j = jdTdbDesdeUtc(jdUtcDesdeInput("2024-06-01T00:00")), w = nv.cuerpo("-170").pos(j), e = ph.cuerpo("399").pos(j), dJ = Math.hypot(w[0] - e[0], w[1] - e[1], w[2] - e[2]);
  afirmar(dJ > 1.0e6 && dJ < 1.9e6, `JWST a ${(dJ / 1e6).toFixed(2)} millones de km de la Tierra`);
  afirmar(Math.hypot(...w) > Math.hypot(...e), "JWST más lejos del Sol que la Tierra (L2)");
  console.log(`Misiones: ${n} encuentros contrastados con las fechas históricas (±0,75 d) y con distancias y velocidades publicadas; heliopausa y L2 verificados`);
}

// 14. Calendario de fenómenos planetarios: posiciones aparentes contra JPL Horizons y definición de cada fenómeno
if (sistemas.sol && existsSync(join(aqui, "referencia_calendario.json"))) {
  const cal = crearCalendario(sistemas.sol), ref = JSON.parse(readFileSync(join(aqui, "referencia_calendario.json"), "utf8")), D = 180 / Math.PI;
  const env = (x) => { x = (x + 180) % 360; if (x < 0) x += 360; return x - 180; };
  let pe = 0, pl = 0;
  for (const m of ref.muestras) { const jd = m.jdUtc + 69.184 / 86400; pe = Math.max(pe, Math.abs(cal.elongacion(m.planeta, jd) * D - m.elong)); pl = Math.max(pl, Math.abs(env(cal.elLon(m.planeta, jd) * D - env(m.lonP - m.lonS)))); }
  afirmar(pe < 0.001 && pl < 0.001, `calendario: elongación (${pe.toFixed(5)}°) y longitud relativa al Sol (${pl.toFixed(5)}°) contra Horizons en ${ref.muestras.length} épocas`);
  const ev = cal.todos(jdTdbDesdeUtc(JD_UTC_INICIO), jdTdbDesdeUtc(JD_UTC_FIN)), por = (t, p) => ev.filter((e) => e.tipo === t && (!p || e.planeta === p));
  for (const e of por("oposicion")) cerca(Math.abs(env(cal.elLon(e.planeta, e.jdTdb) * D)), 180, 0.001, `oposición de ${NOMBRE_CAL[e.planeta]}: longitud relativa 180°`);
  for (const e of por("cuad_este")) cerca(env(cal.elLon(e.planeta, e.jdTdb) * D), 90, 0.001, `cuadratura oriental de ${NOMBRE_CAL[e.planeta]}`);
  for (const e of [...por("conj_sup"), ...por("conj_inf"), ...por("conjuncion")]) cerca(env(cal.elLon(e.planeta, e.jdTdb) * D), 0, 0.001, `conjunción con el Sol de ${NOMBRE_CAL[e.planeta]}`);
  for (const e of [...por("elong_este"), ...por("elong_oeste")]) { const a = cal.elongacion(e.planeta, e.jdTdb), b = cal.elongacion(e.planeta, e.jdTdb - 0.5), c = cal.elongacion(e.planeta, e.jdTdb + 0.5); afirmar(a >= b && a >= c, `máxima elongación de ${NOMBRE_CAL[e.planeta]} es un máximo`); afirmar(e.elong > 17 && e.elong < 48, `elongación máxima de ${NOMBRE_CAL[e.planeta]}: ${e.elong.toFixed(1)}° (esperado 17°–47°)`); }
  for (const e of [...por("est_retro"), ...por("est_directo")]) { const h = cal.geo(e.planeta, e.jdTdb + 0.01, {}).lam, g = cal.geo(e.planeta, e.jdTdb - 0.01, {}).lam, dl = env((h - g) * D) / 0.02; afirmar(Math.abs(dl) < 0.002, `estacionario de ${NOMBRE_CAL[e.planeta]}: velocidad en longitud ${dl.toFixed(5)}°/d`); }
  // fechas publicadas: oposición de Marte 2027-02-19, de Saturno 2027-10-18 y de Neptuno 2027-09-28; conjunción Júpiter–Saturno 2040-10-31 a ≈ 1,1°
  for (const [p, f] of [["499", "2027-02-19"], ["699", "2027-10-18"], ["899", "2027-09-28"]]) { const e = por("oposicion", p).sort((a, b) => Math.abs(a.jdUtc - jdUtcDesdeInput(f + "T12:00")) - Math.abs(b.jdUtc - jdUtcDesdeInput(f + "T12:00")))[0]; afirmar(Math.abs(e.jdUtc - jdUtcDesdeInput(f + "T12:00")) < 0.75, `oposición de ${NOMBRE_CAL[p]} el ${f}`); }
  const gc = ev.find((e) => e.tipo === "conj_planetas" && e.planeta === "599" && e.planeta2 === "699" && e.jdUtc > jdUtcDesdeInput("2040-10-01T00:00") && e.jdUtc < jdUtcDesdeInput("2040-12-01T00:00"));
  afirmar(!!gc && Math.abs(gc.jdUtc - jdUtcDesdeInput("2040-10-31T12:00")) < 1 && Math.abs(gc.sep_grados - 1.1) < 0.1, "gran conjunción Júpiter–Saturno del 31 de octubre de 2040 (separación 1,1°)");
  const cuenta = (t, p) => por(t, p).length; afirmar(cuenta("oposicion", "499") === 12 && cuenta("oposicion", "599") >= 21 && cuenta("oposicion", "699") >= 22, `oposiciones 2027–2050: Marte ${cuenta("oposicion", "499")}, Júpiter ${cuenta("oposicion", "599")}, Saturno ${cuenta("oposicion", "699")}`);
  console.log(`Calendario: ${ev.length} fenómenos 2027–2050; posiciones aparentes contra Horizons: elongación ≤ ${pe.toFixed(5)}°, longitud ≤ ${pl.toFixed(5)}°`);
}

console.log(`\n${ok} comprobaciones correctas, ${fallos} fallos`);
process.exit(fallos ? 1 : 0);
