// SPDX-License-Identifier: Apache-2.0
// Datos físicos de los cuerpos principales. Cada valor lleva su fuente en simuladores/documentacion/FUENTES_Y_MODELOS.md.
//  - Radios y GM: IAU 2015 Resolution B3 / NASA-JPL Solar System Dynamics (DE440), valores publicados.
//  - Orientación (polo y meridiano): IAU WGCCRS (Archinal et al. 2018), términos periódicos omitidos (ver doc).
// Unidades: km, km^3/s^2, grados (ascensión recta/declinación del polo norte en ICRF, W en grados, tasa en grados/día).

export const UA_KM = 149597870.7;       // IAU 2012 B2
export const C_KM_S = 299792.458;
export const OBLICUIDAD_J2000 = 23.4392911 * Math.PI / 180; // IAU 2006

export const SOL = { id: "10", nombre: "Sol", radio: 695700, gm: 132712440041.94, color: "#ffd45e",
  polo: { a0: 286.13, d0: 63.87, W0: 84.176, Wd: 14.1844 } };

// `aplan` = achatamiento (a-b)/a; `radio` = radio ecuatorial [km]
export const PLANETAS = {
  "199": { nombre: "Mercurio", radio: 2439.4, gm: 22031.868, aplan: 0, color: "#a8a29e", albedo: 0.088, polo: { a0: 281.0103, d0: 61.4155, W0: 329.5988, Wd: 6.1385108 } },
  "299": { nombre: "Venus", radio: 6051.8, gm: 324858.592, aplan: 0, color: "#e6c88b", albedo: 0.76, polo: { a0: 272.76, d0: 67.16, W0: 160.20, Wd: -1.4813688 } },
  "399": { nombre: "Tierra", radio: 6378.1366, gm: 398600.435, aplan: 1 / 298.25642, color: "#3b82c4", albedo: 0.306, polo: { a0: 0.0, d0: 90.0, W0: 190.147, Wd: 360.9856235, da0: -0.641, dd0: -0.557 } },
  "499": { nombre: "Marte", radio: 3396.19, gm: 42828.375, aplan: 1 / 169.779, color: "#c8643c", albedo: 0.25, polo: { a0: 317.269202, d0: 54.432516, W0: 176.049863, Wd: 350.891982443297, da0: -0.10927547, dd0: -0.05827105 } },
  "599": { nombre: "Júpiter", radio: 71492, gm: 126686534.9, aplan: 0.06487, color: "#d8b48a", albedo: 0.503, polo: { a0: 268.056595, d0: 64.495303, W0: 284.95, Wd: 870.5360000, da0: -0.006499, dd0: 0.002413 } },
  "699": { nombre: "Saturno", radio: 60268, gm: 37931207.8, aplan: 0.09796, color: "#e3cf9f", albedo: 0.342, polo: { a0: 40.589, d0: 83.537, W0: 38.90, Wd: 810.7939024, da0: -0.036, dd0: -0.004 } },
  "799": { nombre: "Urano", radio: 25559, gm: 5793951.3, aplan: 0.02293, color: "#9fd8e0", albedo: 0.3, polo: { a0: 257.311, d0: -15.175, W0: 203.81, Wd: -501.1600928 } },
  "899": { nombre: "Neptuno", radio: 24764, gm: 6835099.5, aplan: 0.01708, color: "#4b70dd", albedo: 0.29, polo: { a0: 299.36, d0: 43.46, W0: 249.978, Wd: 541.1397757 } },
  "9": { nombre: "Plutón", radio: 1188.3, gm: 975.5 /* GM del sistema Plutón–Caronte */, aplan: 0, color: "#c9b79c", albedo: 0.52, polo: { a0: 132.993, d0: -6.163, W0: 302.695, Wd: 56.3625225 }, enano: true },
  "2000001": { nombre: "Ceres", radio: 469.7, gm: 62.6284, aplan: 0, color: "#9a948c", albedo: 0.09, polo: { a0: 291.418, d0: 66.764, W0: 170.650, Wd: 952.1532 }, enano: true },
};

export const LUNA = { id: "301", nombre: "Luna", radio: 1737.4, gm: 4902.800, color: "#cfcfc8", albedo: 0.12 };

// Satélites principales con nombre/colores. El resto se dibuja con color por familia.
export const COLOR_SATELITE = {
  "301": "#cfcfc8", "401": "#8d8174", "402": "#a89a88",
  "501": "#e8d36a", "502": "#c9b79a", "503": "#9d9488", "504": "#6f685f", "505": "#a35c3c",
  "601": "#c8c4bd", "602": "#f1f3f5", "603": "#d7d3cc", "604": "#c3b9ae", "605": "#cdc6bb", "606": "#d9a441", "607": "#9a8f82", "608": "#6c6256",
  "701": "#b9b6b0", "702": "#7d7a76", "703": "#a8a5a0", "704": "#9b9893", "705": "#bdb8b0",
  "801": "#d9cfc6",
};

/** Polo y meridiano origen de `p` en la fecha: devuelve {a0,d0,W} en radianes. */
export function orientacion(p, jdTdb) {
  const d = jdTdb - 2451545.0;
  const T = d / 36525;
  const rad = Math.PI / 180;
  let a0 = p.a0 + (p.da0 || 0) * T;
  let d0 = p.d0 + (p.dd0 || 0) * T;
  if (p === PLANETAS["899"].polo) { // término principal de Neptuno (Archinal et al. 2018)
    const N = (357.85 + 52.316 * T) * rad;
    a0 += 0.70 * Math.sin(N); d0 -= 0.51 * Math.cos(N);
    return { a0: a0 * rad, d0: d0 * rad, W: ((249.978 + 541.1397757 * d - 0.48 * Math.sin(N)) % 360) * rad };
  }
  return { a0: a0 * rad, d0: d0 * rad, W: (((p.W0 + p.Wd * d) % 360) + 360) % 360 * rad };
}

/** Vector unitario del polo norte en el marco eclíptico J2000 (el de las efemérides). */
export function poloEclipticoJ2000(o) {
  const x = Math.cos(o.d0) * Math.cos(o.a0), y = Math.cos(o.d0) * Math.sin(o.a0), z = Math.sin(o.d0);
  const c = Math.cos(OBLICUIDAD_J2000), s = Math.sin(OBLICUIDAD_J2000);
  return [x, c * y + s * z, -s * y + c * z]; // rotación ecuatorial -> eclíptica
}

/** Base ortonormal del cuerpo (ejes x del meridiano 0, y, polo) en el marco eclíptico J2000. */
export function baseDelCuerpo(p, jdTdb, Wforzado) {
  const o = orientacion(p, jdTdb);
  if (Wforzado !== undefined) o.W = Wforzado;
  const n = poloEclipticoJ2000(o);
  // nodo: intersección del ecuador del cuerpo con el ecuador terrestre (ICRF): dirección z_ICRF x polo
  const c = Math.cos(OBLICUIDAD_J2000), s = Math.sin(OBLICUIDAD_J2000);
  const zIcrfEcl = [0, s, c];
  let q = [zIcrfEcl[1] * n[2] - zIcrfEcl[2] * n[1], zIcrfEcl[2] * n[0] - zIcrfEcl[0] * n[2], zIcrfEcl[0] * n[1] - zIcrfEcl[1] * n[0]];
  const nq = Math.hypot(q[0], q[1], q[2]) || 1;
  q = [q[0] / nq, q[1] / nq, q[2] / nq];
  // eje del meridiano 0: q girado W alrededor del polo
  const cw = Math.cos(o.W), sw = Math.sin(o.W);
  const pq = [n[1] * q[2] - n[2] * q[1], n[2] * q[0] - n[0] * q[2], n[0] * q[1] - n[1] * q[0]];
  const x = [q[0] * cw + pq[0] * sw, q[1] * cw + pq[1] * sw, q[2] * cw + pq[2] * sw];
  const y = [n[1] * x[2] - n[2] * x[1], n[2] * x[0] - n[0] * x[2], n[0] * x[1] - n[1] * x[0]];
  return { x, y, z: n };
}

/** Elementos keplerianos osculadores respecto al marco eclíptico J2000. r [km], v [km/s], mu [km^3/s^2]. */
export function elementos(r, v, mu) {
  const rn = Math.hypot(...r), v2 = v[0] ** 2 + v[1] ** 2 + v[2] ** 2;
  const h = [r[1] * v[2] - r[2] * v[1], r[2] * v[0] - r[0] * v[2], r[0] * v[1] - r[1] * v[0]];
  const hn = Math.hypot(...h);
  const a = 1 / (2 / rn - v2 / mu);
  const rv = r[0] * v[0] + r[1] * v[1] + r[2] * v[2];
  const e = [(v2 - mu / rn) * r[0] / mu - rv * v[0] / mu, (v2 - mu / rn) * r[1] / mu - rv * v[1] / mu, (v2 - mu / rn) * r[2] / mu - rv * v[2] / mu];
  const en = Math.hypot(...e);
  const inc = Math.acos(Math.max(-1, Math.min(1, h[2] / hn)));
  return { a, e: en, i: inc * 180 / Math.PI, periodo_d: a > 0 ? 2 * Math.PI * Math.sqrt(a ** 3 / mu) / 86400 : Infinity, r: rn, v: Math.sqrt(v2) };
}

/** Anillos [radio interior, exterior] en km desde el centro del planeta, con opacidad orientativa 0..1. */
export const ANILLOS = {
  "599": [ { n: "Halo", a: 92000, b: 122500, o: 0.05 }, { n: "Principal", a: 122500, b: 129000, o: 0.25 }, { n: "Gossamer de Amaltea", a: 129000, b: 182000, o: 0.04 }, { n: "Gossamer de Tebe", a: 129000, b: 226000, o: 0.03 } ],
  "699": [ { n: "D", a: 66900, b: 74510, o: 0.08 }, { n: "C", a: 74658, b: 92000, o: 0.25 }, { n: "B", a: 92000, b: 117580, o: 0.85 }, { n: "A", a: 122170, b: 136775, o: 0.6 }, { n: "F", a: 140180, b: 140280, o: 0.5 }, { n: "G", a: 166000, b: 175000, o: 0.04 }, { n: "E", a: 180000, b: 480000, o: 0.025 } ],
  "799": [ { n: "6", a: 41837, b: 41840, o: 0.5 }, { n: "5", a: 42234, b: 42237, o: 0.5 }, { n: "4", a: 42570, b: 42573, o: 0.5 }, { n: "α", a: 44718, b: 44724, o: 0.55 }, { n: "β", a: 45661, b: 45667, o: 0.55 }, { n: "η", a: 47176, b: 47178, o: 0.4 }, { n: "γ", a: 47627, b: 47631, o: 0.5 }, { n: "δ", a: 48300, b: 48304, o: 0.5 }, { n: "λ", a: 50024, b: 50026, o: 0.35 }, { n: "ε", a: 51149, b: 51159, o: 0.7 } ],
  "899": [ { n: "Galle", a: 40900, b: 42900, o: 0.1 }, { n: "Le Verrier", a: 53200, b: 53250, o: 0.3 }, { n: "Arago", a: 57200, b: 57250, o: 0.1 }, { n: "Adams", a: 62900, b: 62960, o: 0.4 } ],
};

const RAD_ = Math.PI / 180;
/** Longitud solar areocéntrica Ls (0° = equinoccio de primavera boreal). */
export function longitudSolar(rM, vM, polo) {
  const nrm = (a) => Math.hypot(a[0], a[1], a[2]);
  const cr = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
  const dt = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
  let h = cr(rM, vM); const hn = nrm(h); h = [h[0] / hn, h[1] / hn, h[2] / hn];
  let x = cr(polo, h); const xn = nrm(x); x = [x[0] / xn, x[1] / xn, x[2] / xn];
  if (dt(cr(h, x), polo) < 0) x = [-x[0], -x[1], -x[2]]; // el Sol cruza el ecuador hacia el norte en x
  const y = cr(h, x);
  const rn = nrm(rM), s = [-rM[0] / rn, -rM[1] / rn, -rM[2] / rn];
  return ((Math.atan2(dt(s, y), dt(s, x)) / RAD_) + 360) % 360;
}
