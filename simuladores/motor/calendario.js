// SPDX-License-Identifier: Apache-2.0
// Calendario de conjunciones, oposiciones, cuadraturas, máximas elongaciones y estacionarios de los planetas (2027–2050).
// Todo se calcula con las efemérides heliocéntricas de JPL: posiciones geocéntricas con tiempo luz y aberración anual, y el
// instante de cada fenómeno se busca por bisección. No hay fechas tecleadas. Se contrasta con JPL Horizons (pruebas/).
import { jdUtcDesdeTdb } from "./tiempo.js";

const RAD = Math.PI / 180, ASEG = RAD / 3600, KAPPA = 20.4955 * ASEG, C_UA_DIA = 173.1446326846693, UA_KM = 149597870.7;
const envolver = (x) => { x = (x + Math.PI) % (2 * Math.PI); if (x < 0) x += 2 * Math.PI; return x - Math.PI; };
export const PLANETAS_CAL = ["199", "299", "499", "599", "699", "799", "899"];
export const NOMBRE = { "199": "Mercurio", "299": "Venus", "499": "Marte", "599": "Júpiter", "699": "Saturno", "799": "Urano", "899": "Neptuno" };
export const COLOR = { "199": "#b8b0a8", "299": "#f0d9a0", "499": "#d9673f", "599": "#e8c18a", "699": "#ead7a2", "799": "#9be1e8", "899": "#5b7dff", "399": "#5a9bf0" };
const INTERIORES = new Set(["199", "299"]);
export const TIPOS = {
  conj_sup: "Conjunción superior", conj_inf: "Conjunción inferior", conjuncion: "Conjunción con el Sol", oposicion: "Oposición",
  cuad_este: "Cuadratura oriental", cuad_oeste: "Cuadratura occidental", elong_este: "Máxima elongación este", elong_oeste: "Máxima elongación oeste",
  est_retro: "Estacionario: empieza el retrógrado", est_directo: "Estacionario: termina el retrógrado", conj_planetas: "Conjunción entre planetas",
};

export function crearCalendario(sol) {
  const tE = sol.cuerpo("399"), tP = {};
  for (const id of PLANETAS_CAL) tP[id] = sol.cuerpo(id);
  const tmpE = [0, 0, 0], tmpP = [0, 0, 0];

  /** Dirección aparente (longitud, latitud eclípticas J2000, radianes) y distancia (UA) de un planeta visto desde el centro de la Tierra. */
  function geo(id, jd, out = {}) {
    const e = tE.pos(jd, tmpE), ex = e[0], ey = e[1], ez = e[2];
    const S = [-ex, -ey, -ez], Ls = Math.atan2(S[1], S[0]);
    let x, y, z, d;
    if (id === "10") { x = S[0]; y = S[1]; z = S[2]; d = Math.hypot(x, y, z); }
    else {
      const p0 = tP[id].pos(jd, tmpP); d = Math.hypot(p0[0] - ex, p0[1] - ey, p0[2] - ez);
      for (let i = 0; i < 3; i++) { const p = tP[id].pos(jd - d / UA_KM / C_UA_DIA, tmpP); d = Math.hypot(p[0] - ex, p[1] - ey, p[2] - ez); x = p[0] - ex; y = p[1] - ey; z = p[2] - ez; }
      // tiempo luz en días = distancia en UA / (c en UA/día)
    }
    let lam = Math.atan2(y, x); const bet = Math.atan2(z, Math.hypot(x, y));
    out.lam = lam - KAPPA * Math.cos(Ls - lam) / Math.cos(bet); out.bet = bet - KAPPA * Math.sin(bet) * Math.sin(Ls - lam); out.dist = d / UA_KM; out.dist_km = d; out.Ls = Ls;
    return out;
  }
  const a = {}, b = {};
  /** Longitud del planeta menos la del Sol (radianes, -π..π): positiva = el planeta está al este del Sol (cielo vespertino). */
  const elLon = (id, jd) => { geo(id, jd, a); geo("10", jd, b); return envolver(a.lam - b.lam); };
  /** Elongación al Sol (radianes, 0..π) y su signo (este +). */
  function elongacion(id, jd) {
    geo(id, jd, a); geo("10", jd, b);
    const c = Math.sin(a.bet) * Math.sin(b.bet) + Math.cos(a.bet) * Math.cos(b.bet) * Math.cos(a.lam - b.lam);
    return Math.acos(Math.max(-1, Math.min(1, c)));
  }
  const sinEste = (id, jd) => elLon(id, jd) >= 0 ? 1 : -1;
  const sepPlanetas = (p, q, jd) => { geo(p, jd, a); geo(q, jd, b); const c = Math.sin(a.bet) * Math.sin(b.bet) + Math.cos(a.bet) * Math.cos(b.bet) * Math.cos(a.lam - b.lam); return Math.acos(Math.max(-1, Math.min(1, c))); };

  /** Cruces de g(t) = envolver(f(t) − objetivo) por cero (en cualquier sentido). */
  function cruces(f, objetivo, jd0, jd1, paso) {
    const out = [], g = (x) => envolver(f(x) - objetivo);
    let t0 = jd0, g0 = g(t0);
    for (let t = jd0 + paso; t <= jd1 + paso; t += paso) {
      const g1 = g(t);
      if (((g0 < 0 && g1 >= 0) || (g0 > 0 && g1 <= 0)) && Math.abs(g0) < 1 && Math.abs(g1) < 1) {
        let lo = t0, hi = t, glo = g0;
        for (let i = 0; i < 50; i++) { const m = (lo + hi) / 2, gm = g(m); if ((glo < 0) === (gm < 0)) { lo = m; glo = gm; } else hi = m; }
        out.push({ jd: (lo + hi) / 2, sube: g1 > g0 });
      }
      t0 = t; g0 = g1;
    }
    return out;
  }
  /** Máximos de f (búsqueda por la sección áurea alrededor de cada máximo local muestreado). */
  function maximos(f, jd0, jd1, paso) {
    const out = [], n = Math.ceil((jd1 - jd0) / paso) + 1, v = new Float64Array(n);
    for (let i = 0; i < n; i++) v[i] = f(jd0 + i * paso);
    for (let i = 1; i < n - 1; i++) if (v[i] >= v[i - 1] && v[i] > v[i + 1]) {
      let lo = jd0 + (i - 1) * paso, hi = jd0 + (i + 1) * paso; const gr = (Math.sqrt(5) - 1) / 2;
      let x1 = hi - gr * (hi - lo), x2 = lo + gr * (hi - lo), f1 = f(x1), f2 = f(x2);
      for (let k = 0; k < 60; k++) { if (f1 > f2) { hi = x2; x2 = x1; f2 = f1; x1 = hi - gr * (hi - lo); f1 = f(x1); } else { lo = x1; x1 = x2; f1 = f2; x2 = lo + gr * (hi - lo); f2 = f(x2); } }
      out.push((lo + hi) / 2);
    }
    return out;
  }
  const evento = (tipo, id, jd, extra = {}) => { const el = elongacion(id, jd) / RAD; geo(id, jd, a); return { tipo, planeta: id, jdTdb: jd, jdUtc: jdUtcDesdeTdb(jd), elong: el, dist_ua: a.dist, ...extra }; };

  /** Fenómenos de un planeta respecto del Sol y su movimiento aparente. */
  function eventosPlaneta(id, jd0, jd1) {
    const out = [], lon = (j) => elLon(id, j), interior = INTERIORES.has(id), paso = interior ? 0.5 : 2;
    if (interior) {
      for (const c of cruces(lon, 0, jd0, jd1, paso)) { geo(id, c.jd, a); geo("10", c.jd, b); out.push(evento(a.dist < b.dist ? "conj_inf" : "conj_sup", id, c.jd)); }
      for (const t of maximos((j) => elongacion(id, j), jd0, jd1, 1)) out.push(evento(lon(t) > 0 ? "elong_este" : "elong_oeste", id, t));
    } else {
      for (const c of cruces(lon, 0, jd0, jd1, paso)) out.push(evento("conjuncion", id, c.jd));
      for (const c of cruces(lon, Math.PI, jd0, jd1, paso)) out.push(evento("oposicion", id, c.jd));
      for (const c of cruces(lon, Math.PI / 2, jd0, jd1, paso)) out.push(evento("cuad_este", id, c.jd));
      for (const c of cruces(lon, -Math.PI / 2, jd0, jd1, paso)) out.push(evento("cuad_oeste", id, c.jd));
    }
    // estacionarios: la longitud geocéntrica (aparente) deja de crecer o de decrecer
    const h = 0.25, vel = (j) => { geo(id, j + h, a); const l1 = a.lam; geo(id, j - h, b); return envolver(l1 - b.lam); };
    for (const c of cruces(vel, 0, jd0 + 1, jd1 - 1, interior ? 0.5 : 2)) out.push(evento(c.sube ? "est_directo" : "est_retro", id, c.jd));
    return out;
  }

  /** Conjunciones entre planetas: igual longitud eclíptica geocéntrica aparente. `sep_grados` es la separación en ese instante (≈ diferencia de latitud). */
  function conjuncionesPlanetas(jd0, jd1) {
    const out = [];
    for (let i = 0; i < PLANETAS_CAL.length; i++) for (let j = i + 1; j < PLANETAS_CAL.length; j++) {
      const p = PLANETAS_CAL[i], q = PLANETAS_CAL[j];
      const dl = (t) => { geo(p, t, a); geo(q, t, b); return envolver(a.lam - b.lam); };
      for (const c of cruces(dl, 0, jd0, jd1, 1)) {
        const sep = sepPlanetas(p, q, c.jd) / RAD, ep = elongacion(p, c.jd) / RAD, eq = elongacion(q, c.jd) / RAD;
        out.push({ tipo: "conj_planetas", planeta: p, planeta2: q, jdTdb: c.jd, jdUtc: jdUtcDesdeTdb(c.jd), sep_grados: sep, elong: Math.min(ep, eq), dist_ua: 0 });
      }
    }
    return out;
  }

  /** Todos los fenómenos entre dos instantes TDB, ordenados por fecha. */
  function todos(jd0, jd1) {
    const out = [];
    for (const id of PLANETAS_CAL) out.push(...eventosPlaneta(id, jd0, jd1));
    out.push(...conjuncionesPlanetas(jd0, jd1));
    return out.sort((x, y) => x.jdTdb - y.jdTdb);
  }
  return { geo, elLon, elongacion, eventosPlaneta, conjuncionesPlanetas, todos };
}
