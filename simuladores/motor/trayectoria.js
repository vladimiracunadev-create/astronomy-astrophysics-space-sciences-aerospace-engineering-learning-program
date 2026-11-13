// SPDX-License-Identifier: Apache-2.0
// Trayectorias interplanetarias de dos cuerpos (cónicas empalmadas): problema de Lambert, propagación kepleriana, delta-v y gráfico «porkchop».
// Las posiciones de los planetas salen de las efemérides de JPL; la nave sólo siente la gravedad del Sol (sin asistencias, sin empuje continuo,
// sin perturbaciones): sirve para entender ventanas de lanzamiento y costos, NO para diseñar una misión.
// Unidades: km, km/s, segundos; ángulos en radianes. Marco: eclíptica J2000 heliocéntrica.
import { SOL, PLANETAS } from "./cuerpos.js";

const MU_SOL = SOL.gm;
const DIA = 86400;
const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
const cruz = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
const norm = (a) => Math.hypot(a[0], a[1], a[2]);
const resta = (a, b) => [a[0] - b[0], a[1] - b[1], a[2] - b[2]];

function stumpffC(z) { if (z > 1e-6) return (1 - Math.cos(Math.sqrt(z))) / z; if (z < -1e-6) return (Math.cosh(Math.sqrt(-z)) - 1) / -z; return 0.5 - z / 24 + z * z / 720; }
function stumpffS(z) { if (z > 1e-6) { const s = Math.sqrt(z); return (s - Math.sin(s)) / (s * s * s); } if (z < -1e-6) { const s = Math.sqrt(-z); return (Math.sinh(s) - s) / (s * s * s); } return 1 / 6 - z / 120 + z * z / 5040; }

/**
 * Problema de Lambert (variables universales, Bate-Mueller-White / Curtis alg. 5.2), sin vueltas completas.
 * r1, r2 [km], tof [s], mu [km^3/s^2]. `directo`: la transferencia gira en sentido antihorario visto desde el polo norte eclíptico (como los planetas).
 * Devuelve {v1, v2} [km/s] o null si no converge.
 */
export function lambert(r1, r2, tof, mu = MU_SOL, directo = true) {
  const n1 = norm(r1), n2 = norm(r2);
  const c = cruz(r1, r2);
  let dth = Math.acos(Math.max(-1, Math.min(1, dot(r1, r2) / (n1 * n2))));
  if (directo ? c[2] < 0 : c[2] >= 0) dth = 2 * Math.PI - dth;
  const A = Math.sin(dth) * Math.sqrt(n1 * n2 / (1 - Math.cos(dth)));
  if (Math.abs(A) < 1e-9) return null;
  const y = (z) => n1 + n2 + A * (z * stumpffS(z) - 1) / Math.sqrt(stumpffC(z));
  const F = (z) => { const yy = y(z); return Math.pow(yy / stumpffC(z), 1.5) * stumpffS(z) + A * Math.sqrt(yy) - Math.sqrt(mu) * tof; };
  // cota: y(z) > 0. z crece hacia elipses de periodo corto; en z = 4π² la órbita completa una vuelta
  let lo = -4 * Math.PI * Math.PI, hi = 4 * Math.PI * Math.PI - 1e-6;
  while (y(lo) < 0 && lo < hi) lo += 0.5;                // sólo para A > 0 hay que subir hasta y > 0
  let flo = F(lo), fhi = F(hi);
  if (!isFinite(flo) || !isFinite(fhi) || flo * fhi > 0) {
    // F es monótona creciente en z para y>0: si no hay cambio de signo, no existe solución de 0 vueltas en el intervalo
    if (flo > 0) return null;
    if (fhi < 0) return null;
  }
  let z = 0;
  for (let i = 0; i < 100; i++) { // bisección con paso final de Newton
    z = 0.5 * (lo + hi);
    if (y(z) < 0) { lo = z; continue; }
    const f = F(z);
    if (Math.abs(f) < 1e-9 * Math.sqrt(mu) * tof || hi - lo < 1e-13) break;
    if (f < 0) lo = z; else hi = z;
  }
  const yy = y(z);
  if (!(yy > 0) || !(Math.abs(F(z)) < 1e-6 * Math.sqrt(mu) * tof)) return null; // sin solución de 0 vueltas para ese tiempo de vuelo
  const f = 1 - yy / n1, g = A * Math.sqrt(yy / mu), gdot = 1 - yy / n2;
  const v1 = [(r2[0] - f * r1[0]) / g, (r2[1] - f * r1[1]) / g, (r2[2] - f * r1[2]) / g];
  const v2 = [(gdot * r2[0] - r1[0]) / g, (gdot * r2[1] - r1[1]) / g, (gdot * r2[2] - r1[2]) / g];
  return { v1, v2, z };
}

/** Propaga un estado kepleriano (r0, v0) durante dt segundos (variables universales). */
export function propagar(r0, v0, dt, mu = MU_SOL) {
  const r = norm(r0), vr = dot(r0, v0) / r, alfa = 2 / r - dot(v0, v0) / mu;
  let chi = Math.sqrt(mu) * Math.abs(alfa) * dt;
  if (Math.abs(alfa) < 1e-14) chi = Math.sqrt(mu) * dt / r;
  for (let i = 0; i < 60; i++) {
    const z = alfa * chi * chi, C = stumpffC(z), S = stumpffS(z);
    const F = r * vr / Math.sqrt(mu) * chi * chi * C + (1 - alfa * r) * chi ** 3 * S + r * chi - Math.sqrt(mu) * dt;
    const dF = r * vr / Math.sqrt(mu) * chi * (1 - alfa * chi * chi * S) + (1 - alfa * r) * chi * chi * C + r;
    const d = F / dF; chi -= d; if (Math.abs(d) < 1e-9 * Math.max(1, Math.abs(chi))) break;
  }
  const z = alfa * chi * chi, C = stumpffC(z), S = stumpffS(z);
  const f = 1 - chi * chi / r * C, g = dt - chi ** 3 / Math.sqrt(mu) * S;
  const rr = [f * r0[0] + g * v0[0], f * r0[1] + g * v0[1], f * r0[2] + g * v0[2]], rn = norm(rr);
  const fd = Math.sqrt(mu) / (rn * r) * (alfa * chi ** 3 * S - chi), gd = 1 - chi * chi / rn * C;
  return { r: rr, v: [fd * r0[0] + gd * v0[0], fd * r0[1] + gd * v0[1], fd * r0[2] + gd * v0[2]] };
}

/** Elementos de la órbita de transferencia: semieje, excentricidad, perihelio y afelio [km]. */
export function elementosTransferencia(r, v, mu = MU_SOL) {
  const rn = norm(r), a = 1 / (2 / rn - dot(v, v) / mu), h = cruz(r, v);
  const e = [(dot(v, v) - mu / rn) * r[0] / mu - dot(r, v) * v[0] / mu, (dot(v, v) - mu / rn) * r[1] / mu - dot(r, v) * v[1] / mu, (dot(v, v) - mu / rn) * r[2] / mu - dot(r, v) * v[2] / mu];
  const en = norm(e);
  return { a, e: en, perihelio: a * (1 - en), afelio: a > 0 ? a * (1 + en) : Infinity, i: Math.acos(Math.max(-1, Math.min(1, h[2] / norm(h)))) * 180 / Math.PI };
}

/** Delta-v para salir de (o capturarse en) una órbita en torno a un planeta: v∞ y órbita de periapsis rp y apoapsis ra [km] (ra = rp: circular). */
export function deltaVOrbita(vinf, mu, rp, ra = rp) {
  const vp = Math.sqrt(vinf * vinf + 2 * mu / rp);
  const e = (ra - rp) / (ra + rp);
  return vp - Math.sqrt(mu * (1 + e) / rp);
}

// Órbitas de referencia (altitud sobre el radio ecuatorial IAU, km): salida y llegada. Circular salvo que `apo` se indique.
export const ORBITAS_PREDETERMINADAS = {
  "199": { alt: 400 }, "299": { alt: 300 }, "399": { alt: 300 }, "499": { alt: 300 }, "599": { rp: 4, ra: 100 }, "699": { rp: 2, ra: 50 }, "799": { rp: 2.5, ra: 50 }, "899": { rp: 2.5, ra: 50 }, "9": { alt: 1000 },
};
/** Radios de periapsis y apoapsis [km] desde el centro del planeta. rp/ra en radios planetarios o alt en km. */
export function radiosOrbita(id, o = ORBITAS_PREDETERMINADAS[id]) {
  const R = PLANETAS[id].radio;
  if (o.alt !== undefined) return { rp: R + o.alt, ra: R + (o.altApo ?? o.alt) };
  return { rp: o.rp * R, ra: o.ra * R };
}

/**
 * Evalúa una transferencia entre dos planetas: salida en jdSalida, llegada en jdLlegada (JD TDB). `tablas` = {sol: Sistema}.
 * Devuelve null si Lambert no converge.
 */
export function evaluar(sol, desde, hacia, jdSalida, jdLlegada, orbitas = {}) {
  const t1 = sol.cuerpo(desde), t2 = sol.cuerpo(hacia);
  const r1 = t1.pos(jdSalida), r2 = t2.pos(jdLlegada), tof = (jdLlegada - jdSalida) * DIA;
  if (tof <= 0) return null;
  const s = lambert(r1, r2, tof, MU_SOL, true);
  if (!s) return null;
  const vp1 = t1.vel(jdSalida), vp2 = t2.vel(jdLlegada);
  const vinfS = norm(resta(s.v1, vp1)), vinfL = norm(resta(s.v2, vp2));
  if (!isFinite(vinfS) || !isFinite(vinfL)) return null;
  const o1 = radiosOrbita(desde, orbitas.salida || ORBITAS_PREDETERMINADAS[desde]), o2 = radiosOrbita(hacia, orbitas.llegada || ORBITAS_PREDETERMINADAS[hacia]);
  const dv1 = deltaVOrbita(vinfS, PLANETAS[desde].gm, o1.rp, o1.ra), dv2 = deltaVOrbita(vinfL, PLANETAS[hacia].gm, o2.rp, o2.ra);
  return { jdSalida, jdLlegada, tof_d: tof / DIA, vinfSalida: vinfS, vinfLlegada: vinfL, c3: vinfS * vinfS, dvSalida: dv1, dvLlegada: dv2, dvTotal: dv1 + dv2, v1: s.v1, v2: s.v2, r1, r2 };
}

/** Rejilla «porkchop»: salidas × duraciones. Devuelve {fechas, tofs, celdas:[{...}|null]} (por filas de salida). */
export function porkchop(sol, desde, hacia, { jdIni, jdFin, nSalida, tofMin, tofMax, nTof, orbitas }, progreso) {
  const celdas = new Array(nSalida * nTof).fill(null);
  const fechas = [], tofs = [];
  for (let i = 0; i < nSalida; i++) fechas.push(jdIni + (jdFin - jdIni) * i / (nSalida - 1));
  for (let j = 0; j < nTof; j++) tofs.push(tofMin + (tofMax - tofMin) * j / (nTof - 1));
  for (let i = 0; i < nSalida; i++) {
    for (let j = 0; j < nTof; j++) celdas[i * nTof + j] = evaluar(sol, desde, hacia, fechas[i], fechas[i] + tofs[j], orbitas);
    if (progreso) progreso(i / nSalida);
  }
  return { fechas, tofs, celdas, nSalida, nTof };
}

/** Puntos de la trayectoria heliocéntrica de la nave (N+1 puntos, de la salida a la llegada). */
export function trazaTransferencia(ev, N = 200) {
  const pts = new Float64Array((N + 1) * 3), tof = ev.tof_d * DIA;
  for (let k = 0; k <= N; k++) { const p = propagar(ev.r1, ev.v1, tof * k / N); pts[k * 3] = p.r[0]; pts[k * 3 + 1] = p.r[1]; pts[k * 3 + 2] = p.r[2]; }
  return pts;
}
