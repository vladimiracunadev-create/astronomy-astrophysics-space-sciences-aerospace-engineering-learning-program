// SPDX-License-Identifier: Apache-2.0
// Asteroides: posición por propagación kepleriana (dos cuerpos) de los elementos osculadores del JPL Small-Body Database.
// Es una APROXIMACIÓN: ignora las perturbaciones de los planetas (sobre todo Júpiter), así que el error crece con el tiempo desde la época
// de los elementos. El error se mide contra JPL Horizons (pruebas/verificacion_asteroides.json) y se documenta; NO es una efemérides oficial.
import { UA_KM } from "./cuerpos.js";

const K = 0.01720209895;          // constante gaussiana (UA^1.5 / día)
const RAD = Math.PI / 180;

export const CLASES = {
  MBA: ["Cinturón principal", "#9fb0cf"], IMB: ["Cinturón interior", "#a8d08d"], OMB: ["Cinturón exterior", "#8ab4f8"], MCA: ["Cruza la órbita de Marte", "#f6b26b"],
  TJN: ["Troyano de Júpiter", "#ea9999"], HYA: ["Hilda", "#d5a6bd"], IEO: ["Atira (interior a la Tierra)", "#ffd966"], ATE: ["Atón", "#ffd966"], APO: ["Apolo", "#ffe599"], AMO: ["Amor", "#ffe599"],
};

/** Posición heliocéntrica [km] en el marco eclíptico J2000 de un asteroide (fila de asteroides.json) en `jdTdb`. */
export function posicion(f, jdTdb, out = [0, 0, 0]) {
  const a = f[4], e = f[5], inc = f[6] * RAD, om = f[7] * RAD, w = f[8] * RAD;
  const n = K / Math.pow(a, 1.5);                    // rad/día
  let M = (f[9] * RAD + n * (jdTdb - f[10])) % (2 * Math.PI); if (M < 0) M += 2 * Math.PI;
  let E = e < 0.8 ? M : Math.PI;
  for (let k = 0; k < 40; k++) { const d = (E - e * Math.sin(E) - M) / (1 - e * Math.cos(E)); E -= d; if (Math.abs(d) < 1e-12) break; }
  const x = a * (Math.cos(E) - e), y = a * Math.sqrt(1 - e * e) * Math.sin(E);
  const cw = Math.cos(w), sw = Math.sin(w), co = Math.cos(om), so = Math.sin(om), ci = Math.cos(inc), si = Math.sin(inc);
  const x1 = x * cw - y * sw, y1 = x * sw + y * cw;
  out[0] = (x1 * co - y1 * ci * so) * UA_KM; out[1] = (x1 * so + y1 * ci * co) * UA_KM; out[2] = (y1 * si) * UA_KM;
  return out;
}

/** Datos derivados: perihelio, afelio (UA) y periodo (años). */
export function derivados(f) { return { peri: f[4] * (1 - f[5]), afe: f[4] * (1 + f[5]), periodo: Math.pow(f[4], 1.5) }; }

/** Puntos de la órbita (N+1) en el plano de la eclíptica J2000 [km]. */
export function trazaOrbita(f, N = 160) {
  const out = new Float64Array((N + 1) * 3), a = f[4], e = f[5], inc = f[6] * RAD, om = f[7] * RAD, w = f[8] * RAD;
  const cw = Math.cos(w), sw = Math.sin(w), co = Math.cos(om), so = Math.sin(om), ci = Math.cos(inc), si = Math.sin(inc);
  for (let k = 0; k <= N; k++) {
    const E = (k / N) * 2 * Math.PI, x = a * (Math.cos(E) - e), y = a * Math.sqrt(1 - e * e) * Math.sin(E), x1 = x * cw - y * sw, y1 = x * sw + y * cw;
    out[k * 3] = (x1 * co - y1 * ci * so) * UA_KM; out[k * 3 + 1] = (x1 * so + y1 * ci * co) * UA_KM; out[k * 3 + 2] = y1 * si * UA_KM;
  }
  return out;
}
