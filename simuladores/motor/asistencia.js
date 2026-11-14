// SPDX-License-Identifier: Apache-2.0
// Asistencia gravitatoria en el modelo de cónicas empalmadas (plano del encuentro, dos cuerpos):
// en el sistema del planeta la nave describe una hipérbola y sólo gira su velocidad en el infinito v∞; en el sistema del Sol, la velocidad
// es la del planeta Vp más v∞, y el giro de v∞ cambia su módulo. Unidades: km, km/s, km³/s².

/** Hipérbola de v∞ y distancia del periastro rp [km] alrededor de un cuerpo de parámetro gravitatorio mu. */
export function hiperbola(mu, vinf, rp) {
  const e = 1 + rp * vinf * vinf / mu, delta = 2 * Math.asin(1 / e), vp = Math.sqrt(vinf * vinf + 2 * mu / rp), a = -mu / (vinf * vinf), b = -a * Math.sqrt(e * e - 1);
  return { e, delta, vperi: vp, a, b, deltaMax: (rpMin) => 2 * Math.asin(1 / (1 + rpMin * vinf * vinf / mu)) };
}

/**
 * `Vp` = velocidad heliocéntrica del planeta (módulo, km/s; el eje y apunta en su dirección);
 * `theta` = ángulo entre v∞ de entrada y la velocidad del planeta (rad, 0..π): 0 = la nave llega «por detrás» y 180° = de frente;
 * `gamma` = hacia dónde gira v∞ alrededor de su dirección de entrada (rad): 0 y π = giro dentro del plano (a un lado u otro del planeta),
 * ±π/2 = giro fuera del plano de la órbita del planeta (cambia la inclinación). El módulo del giro es el de la hipérbola, 2·asin(1/e).
 */
export function asistencia(mu, vinf, rp, Vp, theta, gamma) {
  const h = hiperbola(mu, vinf, rp), vin = [vinf * Math.sin(theta), vinf * Math.cos(theta), 0], e1 = [Math.cos(theta), -Math.sin(theta), 0], e2 = [0, 0, 1];
  const vout = [0, 1, 2].map((k) => vin[k] * Math.cos(h.delta) + vinf * Math.sin(h.delta) * (Math.cos(gamma) * e1[k] + Math.sin(gamma) * e2[k]));
  const hin = [vin[0], vin[1] + Vp, vin[2]], hout = [vout[0], vout[1] + Vp, vout[2]], vhIn = Math.hypot(...hin), vhOut = Math.hypot(...hout);
  return { ...h, vin, vout, hin, hout, vhIn, vhOut, dv: vhOut - vhIn, desvioHelio: Math.acos(Math.max(-1, Math.min(1, (hin[0] * hout[0] + hin[1] * hout[1] + hin[2] * hout[2]) / (vhIn * vhOut)))), theta, gamma };
}

/**
 * Reconstruye (theta, gamma) de un encuentro real de `encuentros.json`: theta sale de v∞ y de la velocidad heliocéntrica de entrada; gamma es el
 * giro que reproduce la velocidad de salida medida (siempre existe: v∞ de salida está sobre un cono de semiabertura 2·asin(1/e) en torno a la de entrada).
 */
export function desdeEncuentro(e, mu, Vp) {
  const c = (e.vh_in ** 2 - Vp * Vp - e.vinf_kms ** 2) / (2 * Vp * e.vinf_kms), theta = Math.acos(Math.max(-1, Math.min(1, c)));
  const f = (g) => Math.abs(asistencia(mu, e.vinf_kms, e.dist_km, Vp, theta, g).vhOut - e.vh_out);
  let g0 = 0, f0 = Infinity; for (let k = 0; k < 720; k++) { const g = -Math.PI + 2 * Math.PI * k / 720, v = f(g); if (v < f0) { f0 = v; g0 = g; } }
  let lo = g0 - Math.PI / 360, hi = g0 + Math.PI / 360; for (let k = 0; k < 60; k++) { const m1 = lo + (hi - lo) / 3, m2 = hi - (hi - lo) / 3; if (f(m1) < f(m2)) hi = m2; else lo = m1; }
  const gamma = (lo + hi) / 2, r = asistencia(mu, e.vinf_kms, e.dist_km, Vp, theta, gamma);
  return { r, err: Math.abs(r.vhOut - e.vh_out), theta, gamma };
}
