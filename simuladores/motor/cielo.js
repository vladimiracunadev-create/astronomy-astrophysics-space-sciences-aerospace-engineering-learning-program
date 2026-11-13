// SPDX-License-Identifier: Apache-2.0
// Cálculo del cielo visto desde la superficie (o la cima de las nubes) de la Tierra, Marte, Júpiter o Saturno.
// Posiciones: efemérides de JPL (planetas heliocéntricos y satélites respecto de su planeta). Estrellas: Hipparcos/Tycho vía d3-celestial,
// coordenadas ICRS J2000 con movimiento propio lineal de Hipparcos. Todo se calcula en el marco eclíptico J2000 de las efemérides y se pasa al horizonte local
// con la orientación IAU del planeta (la Tierra, con el ángulo de rotación terrestre ERA).
import { PLANETAS, SOL, LUNA, OBLICUIDAD_J2000, C_KM_S, UA_KM, baseDelCuerpo } from "./cuerpos.js";
import { anguloRotacionTerrestre, jdUtcDesdeTdb } from "./tiempo.js";

const RAD = Math.PI / 180;
const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
const cruz = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
const norma = (a) => Math.hypot(a[0], a[1], a[2]);
const unit = (a) => { const n = norma(a) || 1; return [a[0] / n, a[1] / n, a[2] / n]; };

/** Dirección ecuatorial ICRS (grados) -> vector unitario en la eclíptica J2000. */
export function ecuatorialAEclipticoJ2000(raDeg, decDeg) {
  const ra = raDeg * RAD, de = decDeg * RAD, c = Math.cos(OBLICUIDAD_J2000), s = Math.sin(OBLICUIDAD_J2000);
  const x = Math.cos(de) * Math.cos(ra), y = Math.cos(de) * Math.sin(ra), z = Math.sin(de);
  return [x, c * y + s * z, -s * y + c * z];
}

// Albedo geométrico y radio (km) para el modelo de magnitud de Lambert cuando no hay fórmula publicada
const ALBEDO = { "199": 0.142, "299": 0.689, "399": 0.434, "499": 0.170, "599": 0.538, "699": 0.499, "799": 0.488, "899": 0.442, "9": 0.52, "301": 0.12 };
const M_SOL = -26.74;

/** Magnitud aparente: fórmulas de Meeus/Almanaque Astronómico para planetas vistos desde la Tierra; modelo de Lambert en los demás casos. */
export function magnitud(id, r, delta, i, desdeTierra, radio, albedo, B = 0) {
  if (desdeTierra) {
    const L = 5 * Math.log10(r * delta), d = i / RAD;
    switch (id) {
      case "199": return -0.42 + L + 0.0380 * d - 0.000273 * d * d + 0.000002 * d ** 3;
      case "299": return -4.40 + L + 0.0009 * d + 0.000239 * d * d - 0.00000065 * d ** 3;
      case "499": return -1.52 + L + 0.016 * d;
      case "599": return -9.40 + L + 0.005 * d;
      case "699": return -8.88 + L - 2.60 * Math.abs(Math.sin(B)) + 1.25 * Math.sin(B) ** 2 + 0.044 * 0;
      case "799": return -7.19 + L;
      case "899": return -6.87 + L;
      default: break;
    }
  }
  const fase = (Math.sin(i) + (Math.PI - i) * Math.cos(i)) / Math.PI;
  const R = radio / UA_KM;
  return M_SOL - 2.5 * Math.log10(Math.max(1e-30, albedo * R * R * fase / (r * r * delta * delta)));
}

/** Observador sobre un planeta. `sol` y `sis` son Sistema (efemerides.js); `cielo` el JSON de estrellas. */
export class Observador {
  constructor({ id, sol, sis, tierra }) {
    this.id = id; this.sol = sol; this.sis = sis; this.tierra = tierra;
    this.fis = PLANETAS[id];
    this.lat = 0; this.lon = 0;
    this.base = null; this.up = [0, 0, 1]; this.este = [1, 0, 0]; this.norte = [0, 1, 0];
    this.centro = [0, 0, 0]; this.pos = [0, 0, 0];
  }
  /** Fija el lugar (grados; latitud planetográfica, longitud este). */
  lugar(lat, lon) { this.lat = lat; this.lon = lon; }

  baseEn(jdTdb, jdUtc) {
    const p = this.fis.polo;
    if (this.id === "399") {
      const T = (jdTdb - 2451545.0) / 36525, a0 = (p.a0 + p.da0 * T) * RAD;
      return baseDelCuerpo(p, jdTdb, anguloRotacionTerrestre(jdUtc) - (a0 + Math.PI / 2));
    }
    return baseDelCuerpo(p, jdTdb);
  }

  /** Actualiza posición del observador y su horizonte local en `jdTdb` (y `jdUtc` para la rotación terrestre). */
  actualizar(jdTdb, jdUtc = jdUtcDesdeTdb(jdTdb)) {
    this.jd = jdTdb;
    this.base = this.baseEn(jdTdb, jdUtc);
    this.centro = this.sol.pos(this.id, jdTdb);
    const f = this.fis.aplan || 0, e2 = 2 * f - f * f, a = this.fis.radio;
    const phi = this.lat * RAD, lam = this.lon * RAD, sp = Math.sin(phi), cp = Math.cos(phi);
    const N = a / Math.sqrt(1 - e2 * sp * sp);
    const loc = [N * cp * Math.cos(lam), N * cp * Math.sin(lam), N * (1 - e2) * sp];
    const nor = [cp * Math.cos(lam), cp * Math.sin(lam), sp];          // normal elipsoidal (cenit) en ejes del cuerpo
    const aEcl = (v) => [this.base.x[0] * v[0] + this.base.y[0] * v[1] + this.base.z[0] * v[2], this.base.x[1] * v[0] + this.base.y[1] * v[1] + this.base.z[1] * v[2], this.base.x[2] * v[0] + this.base.y[2] * v[1] + this.base.z[2] * v[2]];
    this.rel = aEcl(loc);                                               // observador respecto del centro del planeta [km]
    this.up = unit(aEcl(nor));
    this.este = unit(cruz(this.base.z, this.up));
    this.norte = cruz(this.up, this.este);
    this.pos = [this.centro[0] + this.rel[0], this.centro[1] + this.rel[1], this.centro[2] + this.rel[2]];
  }

  /** Altura y acimut (rad; acimut desde el norte hacia el este) de un vector (cualquier longitud) en el marco eclíptico. */
  horizonte(v) {
    const n = unit(v);
    return { alt: Math.asin(Math.max(-1, Math.min(1, dot(n, this.up)))), az: (Math.atan2(dot(n, this.este), dot(n, this.norte)) + 2 * Math.PI) % (2 * Math.PI) };
  }
  /** Vector unitario eclíptico de una altura y un acimut. */
  desdeHorizonte(alt, az) {
    const c = Math.cos(alt);
    return [(this.norte[0] * Math.cos(az) + this.este[0] * Math.sin(az)) * c + this.up[0] * Math.sin(alt),
      (this.norte[1] * Math.cos(az) + this.este[1] * Math.sin(az)) * c + this.up[1] * Math.sin(alt),
      (this.norte[2] * Math.cos(az) + this.este[2] * Math.sin(az)) * c + this.up[2] * Math.sin(alt)];
  }

  /** Posición heliocéntrica de un planeta con corrección de tiempo luz (una iteración). */
  posPlaneta(id, jd) {
    let p = this.sol.pos(id, jd);
    const d = Math.hypot(p[0] - this.pos[0], p[1] - this.pos[1], p[2] - this.pos[2]);
    return this.sol.pos(id, jd - d / C_KM_S / 86400);
  }

  /** Lista de cuerpos del cielo con su dirección, altura, acimut, tamaño angular, fase y magnitud. */
  cuerpos(opciones = {}) {
    const jd = this.jd, out = [];
    const O = this.pos, desdeTierra = this.id === "399";
    const añadir = (id, nombre, vec, radio, extra = {}) => {
      const d = norma(vec), u = unit(vec), h = this.horizonte(vec);
      out.push({ id, nombre, vec, dir: u, dist_km: d, ...h, tam: 2 * Math.asin(Math.min(1, radio / d)), radio, ...extra });
    };
    // Sol
    const vs = [-O[0], -O[1], -O[2]];
    añadir("10", "Sol", vs, SOL.radio, { tipo: "sol", mag: M_SOL + 5 * Math.log10(norma(vs) / UA_KM), color: "#fff1c0" });
    // planetas
    for (const id of ["199", "299", "399", "499", "599", "699", "799", "899"]) {
      if (id === this.id) continue;
      const P = this.posPlaneta(id, jd), v = [P[0] - O[0], P[1] - O[1], P[2] - O[2]];
      const r = norma(P) / UA_KM, delta = norma(v) / UA_KM;
      const sP = [-P[0], -P[1], -P[2]], vP = [-v[0], -v[1], -v[2]];
      const i = Math.acos(Math.max(-1, Math.min(1, dot(unit(sP), unit(vP)))));
      const f = PLANETAS[id];
      // B de Saturno (apertura de los anillos vista desde el observador) para su magnitud
      let B = 0;
      if (id === "699") { const z = baseDelCuerpo(PLANETAS["699"].polo, jd).z; B = Math.asin(dot(unit([-v[0], -v[1], -v[2]]), z)); }
      añadir(id, f.nombre, v, f.radio, { tipo: "planeta", fase: (1 + Math.cos(i)) / 2, angFase: i, mag: magnitud(id, r, delta, i, desdeTierra, f.radio, ALBEDO[id], B), color: f.color, r_ua: r, delta_ua: delta });
    }
    // satélites del propio planeta
    if (this.sis) {
      for (const m of this.sis.meta.cuerpos) {
        const radioM = m.id === "301" ? LUNA.radio : m.radio_km;
        if (!(radioM > 0)) continue;
        if (jd < m.jd_valido_ini || jd > m.jd_valido_fin) continue;
        const rel = this.sis.pos(m.id, jd), v = [rel[0] - this.rel[0], rel[1] - this.rel[1], rel[2] - this.rel[2]];
        const sP = [this.centro[0] + rel[0], this.centro[1] + rel[1], this.centro[2] + rel[2]];
        const i = Math.acos(Math.max(-1, Math.min(1, dot(unit([-sP[0], -sP[1], -sP[2]]), unit([-v[0], -v[1], -v[2]])))));
        const r = norma(sP) / UA_KM, delta = norma(v) / UA_KM;
        const nom = m.id === "301" ? "Luna" : m.id === "999" ? "Plutón" : m.nombre;
        añadir(String(m.id), nom, v, radioM, { tipo: "luna", fase: (1 + Math.cos(i)) / 2, angFase: i, mag: magnitud(String(m.id), r, delta, i, false, radioM, m.id === "301" ? 0.12 : 0.25), color: "#d8d4cc" });
      }
    }
    return out;
  }
}

/** Instante de salida, culminación y puesta de un cuerpo en el día que contiene `jd0` (UTC +/- 0,5 d): [{tipo, jdUtc}] */
export function salidasYPuestas(obs, fnVector, umbral, jd0Utc) {
  const res = [];
  const alt = (jdU) => { obs.actualizar(jdU + 69.184 / 86400, jdU); return obs.horizonte(fnVector(jdU + 69.184 / 86400)).alt; };
  const paso = 10 / 1440, n = Math.round(1.0 / paso);
  let a0 = alt(jd0Utc), prev = a0, pt = jd0Utc;
  for (let k = 1; k <= n; k++) {
    const t = jd0Utc + k * paso, a = alt(t);
    const e0 = prev - umbral, e1 = a - umbral;
    if (e0 < 0 && e1 >= 0 || e0 >= 0 && e1 < 0) {
      let lo = pt, hi = t;
      for (let j = 0; j < 30; j++) { const m = (lo + hi) / 2; const em = alt(m) - umbral; if ((em < 0) === (e0 < 0)) lo = m; else hi = m; }
      res.push({ tipo: e0 < 0 ? "salida" : "puesta", jdUtc: (lo + hi) / 2 });
    }
    prev = a; pt = t;
  }
  return res;
}

/**
 * Observador sobre la superficie de una luna en rotación síncrona (Europa, Titania, Tritón…): el planeta anfitrión queda fijo en el cielo
 * (salvo libración) y el Sol sale y se pone una vez por órbita. Ejes de la luna: x hacia el planeta, z = normal a la órbita (sentido de
 * la órbita = sentido de rotación), y = z × x (este). Longitud 0° = punto subplanetario. Superficie esférica de radio `radioLuna`.
 */
export class ObservadorLuna extends Observador {
  constructor({ idPlaneta, idLuna, sol, sis }) {
    super({ id: idPlaneta, sol, sis });
    this.idLuna = String(idLuna);
    this.meta = sis.cuerpo(this.idLuna).meta;
    this.radioLuna = this.meta.radio_km || LUNA.radio;
    this.nombreLuna = this.meta.nombre;
  }
  actualizar(jdTdb, jdUtc = jdUtcDesdeTdb(jdTdb)) {
    this.jd = jdTdb;
    this.base = this.baseEn(jdTdb, jdUtc);                       // orientación del PLANETA (para sus anillos)
    this.centro = this.sol.pos(this.id, jdTdb);
    const rel = this.sis.pos(this.idLuna, jdTdb), v = this.sis.cuerpo(this.idLuna).vel(jdTdb);
    this.relLuna = rel;
    const x = unit([-rel[0], -rel[1], -rel[2]]);                // hacia el planeta
    let z = unit(cruz(rel, v));                                  // normal a la órbita (momento angular)
    const k = dot(z, x); z = unit([z[0] - k * x[0], z[1] - k * x[1], z[2] - k * x[2]]);
    const y = cruz(z, x);
    const phi = this.lat * RAD, lam = this.lon * RAD, cp = Math.cos(phi), sp = Math.sin(phi);
    const n = [cp * Math.cos(lam) * x[0] + cp * Math.sin(lam) * y[0] + sp * z[0], cp * Math.cos(lam) * x[1] + cp * Math.sin(lam) * y[1] + sp * z[1], cp * Math.cos(lam) * x[2] + cp * Math.sin(lam) * y[2] + sp * z[2]];
    this.up = n;
    this.rel = [rel[0] + n[0] * this.radioLuna, rel[1] + n[1] * this.radioLuna, rel[2] + n[2] * this.radioLuna];
    this.este = unit(cruz(z, n)); this.norte = cruz(n, this.este);
    this.pos = [this.centro[0] + this.rel[0], this.centro[1] + this.rel[1], this.centro[2] + this.rel[2]];
  }
  cuerpos() {
    const lista = super.cuerpos().filter((c) => c.id !== this.idLuna);
    const v = [-this.rel[0], -this.rel[1], -this.rel[2]], f = this.fis, d = norma(v);
    const sP = [this.centro[0], this.centro[1], this.centro[2]];
    const i = Math.acos(Math.max(-1, Math.min(1, dot(unit([-sP[0], -sP[1], -sP[2]]), unit([-v[0], -v[1], -v[2]])))));
    const r = norma(sP) / UA_KM, delta = d / UA_KM, h = this.horizonte(v);
    lista.push({ id: this.id, nombre: f.nombre + " (anfitrión)", vec: v, dir: unit(v), dist_km: d, ...h, tam: 2 * Math.asin(Math.min(1, f.radio / d)), radio: f.radio, tipo: "planeta", fase: (1 + Math.cos(i)) / 2, angFase: i,
      mag: magnitud(this.id, r, delta, i, false, f.radio, ALBEDO[this.id] || 0.4), color: f.color, anfitrion: true });
    return lista;
  }
}
