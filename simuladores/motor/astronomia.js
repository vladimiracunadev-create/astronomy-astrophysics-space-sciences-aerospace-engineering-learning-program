// SPDX-License-Identifier: Apache-2.0
// Fenómenos derivados de las efemérides: equinoccios y solsticios, perihelio y afelio, fases de la Luna y oposiciones de los planetas.
// Se calculan con las posiciones de JPL (Sol visto desde la Tierra, Luna geocéntrica) y se contrastan en pruebas/ con el
// U.S. Naval Observatory (estaciones, ápsides y fases lunares 2027–2050) sin necesidad de red.
import { jdUtcDesdeTdb } from "./tiempo.js";

const RAD = Math.PI / 180;
const ASEG = RAD / 3600;
const KAPPA = 20.4955 * ASEG;          // constante de aberración anual
const UA_KM = 149597870.7;
const envolver = (x) => { x = (x + Math.PI) % (2 * Math.PI); if (x < 0) x += 2 * Math.PI; return x - Math.PI; };

/** Nutación en longitud (radianes), términos principales (Meeus, cap. 22). */
export function nutacionLongitud(jd) {
  const T = (jd - 2451545.0) / 36525;
  const om = (125.04452 - 1934.136261 * T) * RAD, L = (280.4665 + 36000.7698 * T) * RAD, Lp = (218.3165 + 481267.8813 * T) * RAD;
  return (-17.20 * Math.sin(om) - 1.32 * Math.sin(2 * L) - 0.23 * Math.sin(2 * Lp) + 0.21 * Math.sin(2 * om)) * ASEG;
}

/** Precesión general en longitud desde J2000 (radianes). */
export const precesionLongitud = (jd) => { const T = (jd - 2451545.0) / 36525; return (5028.796195 * T + 1.1054348 * T * T) * ASEG; };

export function crearAstronomia(sol, tierra) {
  const tE = sol.cuerpo("399"), tM = tierra.cuerpo("301");
  const solGeo = (jd) => { const e = tE.pos(jd); return [-e[0], -e[1], -e[2]]; };
  const lon = (v) => Math.atan2(v[1], v[0]);

  /** Longitud eclíptica aparente del Sol respecto del equinoccio verdadero de la fecha (radianes). */
  function lonSolAparente(jd) {
    const S = solGeo(jd), R = Math.hypot(...S) / UA_KM;
    return lon(S) + precesionLongitud(jd) + nutacionLongitud(jd) - (20.4898 * ASEG) / R;
  }
  /** Diferencia aparente de longitud Luna − Sol (radianes, -π..π). Incluye la aberración, que no se cancela en la oposición. */
  function dlAparente(jd) {
    const S = solGeo(jd), M = tM.pos(jd), R = Math.hypot(...S) / UA_KM;
    const d = lon(M) - lon(S);
    return envolver(d - KAPPA * Math.cos(d) + (20.4898 * ASEG) / R);
  }

  function cruces(f, objetivo, jd0, jd1, paso) {
    const out = [];
    const g = (x) => envolver(f(x) - objetivo);
    let a = jd0, ga = g(a);
    for (let t = jd0 + paso; t <= jd1 + paso; t += paso) {
      const gb = g(t);
      if (ga < 0 && gb >= 0 && Math.abs(ga) < 1 && Math.abs(gb) < 1) {
        let lo = a, hi = t;
        for (let i = 0; i < 48; i++) { const m = (lo + hi) / 2; if (g(m) < 0) lo = m; else hi = m; }
        out.push((lo + hi) / 2);
      }
      a = t; ga = gb;
    }
    return out;
  }

  const NOMBRE_ESTACION = ["Equinoccio de marzo", "Solsticio de junio", "Equinoccio de septiembre", "Solsticio de diciembre"];
  function estaciones(jd0, jd1) {
    const out = [];
    NOMBRE_ESTACION.forEach((n, k) => cruces(lonSolAparente, k * Math.PI / 2 - (k === 0 ? 0 : 0), jd0, jd1, 1).forEach((t) => out.push({ nombre: n, k, jdTdb: t, jdUtc: jdUtcDesdeTdb(t) })));
    return out.sort((a, b) => a.jdTdb - b.jdTdb);
  }

  /** Perihelio y afelio: extremos de la distancia entre el Sol y el CENTRO de la Tierra (la definición del U.S. Naval Observatory). */
  function distTierra(jd) { const e = tE.pos(jd); return Math.hypot(e[0], e[1], e[2]); }
  function apsides(jd0, jd1) {
    const out = [];
    const anio0 = new Date((jd0 - 2440587.5) * 86400000).getUTCFullYear(), anio1 = new Date((jd1 - 2440587.5) * 86400000).getUTCFullYear();
    for (let y = anio0; y <= anio1; y++) {
      for (const [signo, nombre, mes, dia] of [[1, "Perihelio", 0, 3], [-1, "Afelio", 6, 5]]) {
        const c = Date.UTC(y, mes, dia) / 86400000 + 2440587.5;
        if (c < jd0 || c > jd1) continue;
        const f = (x) => signo * distTierra(x);
        let a = c - 25, b = c + 25;
        const g = (Math.sqrt(5) - 1) / 2;
        let x1 = b - g * (b - a), x2 = a + g * (b - a), f1 = f(x1), f2 = f(x2);
        for (let i = 0; i < 70; i++) {
          if (f1 < f2) { b = x2; x2 = x1; f2 = f1; x1 = b - g * (b - a); f1 = f(x1); } else { a = x1; x1 = x2; f1 = f2; x2 = a + g * (b - a); f2 = f(x2); }
        }
        const t0 = (a + b) / 2;
        out.push({ nombre, jdTdb: t0, jdUtc: jdUtcDesdeTdb(t0), dist_ua: distTierra(t0) / UA_KM });
      }
    }
    return out.sort((a, b) => a.jdTdb - b.jdTdb);
  }

  const NOMBRE_FASE = ["Luna nueva", "Cuarto creciente", "Luna llena", "Cuarto menguante"];
  function fases(jd0, jd1) {
    const out = [];
    NOMBRE_FASE.forEach((n, k) => cruces(dlAparente, k * Math.PI / 2 > Math.PI ? k * Math.PI / 2 - 2 * Math.PI : k * Math.PI / 2, jd0, jd1, 0.5).forEach((t) => out.push({ nombre: n, k, jdTdb: t, jdUtc: jdUtcDesdeTdb(t) })));
    return out.sort((a, b) => a.jdTdb - b.jdTdb);
  }

  /** Oposiciones de un planeta exterior: longitud eclíptica geocéntrica del planeta opuesta a la del Sol. */
  function oposiciones(id, jd0, jd1) {
    const t = sol.cuerpo(id);
    const dl = (jd) => { const e = tE.pos(jd), p = t.pos(jd); return envolver(Math.atan2(-e[1], -e[0]) - Math.atan2(p[1] - e[1], p[0] - e[0])); }; // crece con el tiempo (el Sol avanza más rápido que un planeta exterior)
    return cruces(dl, Math.PI, jd0, jd1, 2).map((x) => { const e = tE.pos(x), p = t.pos(x); return { jdTdb: x, jdUtc: jdUtcDesdeTdb(x), dist_ua: Math.hypot(p[0] - e[0], p[1] - e[1], p[2] - e[2]) / UA_KM }; });
  }

  return { lonSolAparente, dlAparente, estaciones, apsides, fases, distTierra, oposiciones };
}
