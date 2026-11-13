// SPDX-License-Identifier: Apache-2.0
// Franja de totalidad (o anularidad) de un eclipse solar sobre la Tierra y circunstancias locales, a partir de las efemérides de JPL.
// Geometría: el eje de la sombra pasa por el centro del Sol y de la Luna; su intersección con el elipsoide terrestre (WGS 84) en cada instante
// da la línea central. La anchura sale del radio de la umbra (o antiumbra) y de la inclinación del rayo. NO modela el relieve lunar (valles y
// montañas del limbo), ni la refracción, ni la elevación del terreno.
import { SOL, LUNA } from "./cuerpos.js";
import { Observador } from "./cielo.js";
import { jdUtcDesdeTdb } from "./tiempo.js";

const RAD = Math.PI / 180, A = 6378.137, F = 1 / 298.257223563, C = A * (1 - F);
const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
const norma = (a) => Math.hypot(a[0], a[1], a[2]);
const unit = (a) => { const n = norma(a); return [a[0] / n, a[1] / n, a[2] / n]; };

export function crearFranja(sol, tierra, geo) {
  const obs = new Observador({ id: "399", sol, sis: tierra });
  const aCuerpo = (v, b) => [dot(v, b.x), dot(v, b.y), dot(v, b.z)];
  const geodesica = (p) => {
    const lon = Math.atan2(p[1], p[0]), r = Math.hypot(p[0], p[1]); let lat = Math.atan2(p[2], r * (1 - F));
    for (let i = 0; i < 6; i++) { const e2 = 2 * F - F * F, N = A / Math.sqrt(1 - e2 * Math.sin(lat) ** 2); lat = Math.atan2(p[2] + e2 * N * Math.sin(lat), r); }
    return [lat / RAD, lon / RAD];
  };
  /** Punto donde el eje de la sombra toca la Tierra en `jd` (TDB), o null si lo pasa de largo. */
  function impacto(jd) {
    const r = geo.solar(jd), b = obs.baseEn(jd, jdUtcDesdeTdb(jd)), d = unit([r.M[0] - r.S[0], r.M[1] - r.S[1], r.M[2] - r.S[2]]);
    const o = aCuerpo(r.M, b), dd = aCuerpo(d, b);
    const k = [1 / (A * A), 1 / (A * A), 1 / (C * C)];
    const a2 = k[0] * dd[0] ** 2 + k[1] * dd[1] ** 2 + k[2] * dd[2] ** 2, b2 = 2 * (k[0] * o[0] * dd[0] + k[1] * o[1] * dd[1] + k[2] * o[2] * dd[2]), c2 = k[0] * o[0] ** 2 + k[1] * o[1] ** 2 + k[2] * o[2] ** 2 - 1;
    const disc = b2 * b2 - 4 * a2 * c2; if (disc < 0) return null;
    const s = (-b2 - Math.sqrt(disc)) / (2 * a2);
    const P = [o[0] + s * dd[0], o[1] + s * dd[1], o[2] + s * dd[2]];
    const n = unit([P[0] / (A * A), P[1] / (A * A), P[2] / (C * C)]), cosInc = Math.abs(dot(n, dd));
    const [lat, lon] = geodesica(P), RM = LUNA.radio, f2 = Math.asin((SOL.radio - RM) / r.D); // radio de la umbra (o antiumbra) a la distancia s de la Luna
    return { jdTdb: jd, lat, lon, P, altSol: Math.asin(cosInc) / RAD, anchoKm: 2 * Math.abs(RM / Math.cos(f2) - s * Math.tan(f2)) / Math.max(0.05, cosInc), tipo: r.l2 > 0 ? "total" : "anular" };
  }
  /** Línea central: puntos cada `pasoMin` minutos mientras el eje toque la Tierra. */
  function trayectoria(jdMax, pasoMin = 2) {
    const pts = [], dt = pasoMin / 1440;
    for (let k = -240; k <= 240; k++) { const h = impacto(jdMax + k * dt); if (h) pts.push(h); }
    return pts;
  }
  function minimizar(f, lo, hi) {
    const g = (Math.sqrt(5) - 1) / 2; let x1 = hi - g * (hi - lo), x2 = lo + g * (hi - lo), f1 = f(x1), f2 = f(x2);
    for (let i = 0; i < 60; i++) { if (f1 < f2) { hi = x2; x2 = x1; f2 = f1; x1 = hi - g * (hi - lo); f1 = f(x1); } else { lo = x1; x1 = x2; f1 = f2; x2 = lo + g * (hi - lo); f2 = f(x2); } }
    return (lo + hi) / 2;
  }
  /** Mayor eclipse: instante de mínima distancia del eje al centro de la Tierra, lugar de la línea central y duración de la fase central. */
  function mayorEclipse(jdAprox) {
    const t = minimizar((x) => geo.solar(x).q, jdAprox - 0.1, jdAprox + 0.1), h = impacto(t);
    if (!h) return null;
    const dt = 10 / 86400, h1 = impacto(t - dt), h2 = impacto(t + dt);
    let dur = null;
    if (h1 && h2) { const v = Math.hypot(...[0, 1, 2].map((i) => (h2.P[i] - h1.P[i]) / (2 * dt * 86400))); dur = h.anchoKm / v; } // P en ejes del cuerpo: dP/dt ya es respecto del suelo
    return { ...h, duracion_s: dur, jdUtc: jdUtcDesdeTdb(t) };
  }
  /** Circunstancias locales (magnitud y obscuración máximas) en un lugar (grados) cerca de `jdAprox` (TDB). */
  function local(lat, lon, jdAprox) {
    obs.lugar(lat, lon);
    const sep = (jd) => {
      obs.actualizar(jd, jdUtcDesdeTdb(jd));
      const e = sol.pos("399", jd), m = tierra.pos("301", jd);
      const vs = [-(e[0] + obs.rel[0]), -(e[1] + obs.rel[1]), -(e[2] + obs.rel[2])], vm = [m[0] - obs.rel[0], m[1] - obs.rel[1], m[2] - obs.rel[2]];
      return { s: Math.acos(Math.max(-1, Math.min(1, dot(unit(vs), unit(vm))))), rs: Math.asin(SOL.radio / norma(vs)), rm: Math.asin(LUNA.radio / norma(vm)), alt: Math.asin(dot(unit(vs), obs.up)) / RAD };
    };
    const t = minimizar((x) => sep(x).s, jdAprox - 0.2, jdAprox + 0.2), r = sep(t);
    // magnitud del eclipse (convención de los catálogos): en un eclipse central, cociente de diámetros Luna/Sol; en uno parcial, fracción del diámetro solar cubierta
    const mag = r.s <= Math.abs(r.rs - r.rm) ? r.rm / r.rs : (r.rs + r.rm - r.s) / (2 * r.rs);
    let obsc = 0;
    if (r.s < r.rs + r.rm) {
      if (r.s <= Math.abs(r.rs - r.rm)) obsc = r.rm >= r.rs ? 1 : (r.rm / r.rs) ** 2;
      else {
        const R = r.rs, q = r.rm, d = r.s, a1 = Math.acos((d * d + R * R - q * q) / (2 * d * R)), a2 = Math.acos((d * d + q * q - R * R) / (2 * d * q));
        obsc = (R * R * (a1 - Math.sin(2 * a1) / 2) + q * q * (a2 - Math.sin(2 * a2) / 2)) / (Math.PI * R * R);
      }
    }
    return { mag: Math.max(0, mag), obscuracion: Math.min(1, obsc), jdTdb: t, jdUtc: jdUtcDesdeTdb(t), altSol: r.alt };
  }
  return { impacto, trayectoria, mayorEclipse, local };
}
