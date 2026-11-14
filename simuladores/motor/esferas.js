// SPDX-License-Identifier: Apache-2.0
// Dibujo de esferas iluminadas por el Sol. La GEOMETRÍA (posición, tamaño, fase, orientación, sombras) procede de los datos;
// las TEXTURAS son ilustrativas (procedurales; la Tierra usa la máscara tierra/mar de Natural Earth y la Luna sus
// grandes mares en coordenadas selenográficas aproximadas). No son imágenes de misión.
import { BITS, ANCHO as MW, ALTO as MH } from "./mascara_tierra.js";

const GRANDES = new Set(["tierra", "luna"]);
const cache = new Map();
/** Texturas de imágenes reales (mapas equirectangulares, longitud −180…180 hacia el este); el resto son procedurales e ilustrativas. Créditos en DATA_LICENSES.md. */
export const TEXTURAS_REALES = { marte: { url: "texturas/marte.jpg", credito: "mapa de imágenes Viking procesadas por el USGS · NASA/JPL-Caltech" } };
const pedidas = new Set();
function cargarImagen(clave) {
  if (pedidas.has(clave) || typeof document === "undefined") return; pedidas.add(clave);
  const im = new Image();
  im.onload = () => {
    const w = Math.min(1440, im.naturalWidth), h = Math.round(w / 2), c = document.createElement("canvas"); c.width = w; c.height = h;
    const g = c.getContext("2d", { willReadFrequently: true }); g.drawImage(im, 0, 0, w, h);
    const px = g.getImageData(0, 0, w, h).data, d = new Uint8ClampedArray(w * h * 3);
    for (let i = 0, k = 0; i < px.length; i += 4, k += 3) { d[k] = px[i]; d[k + 1] = px[i + 1]; d[k + 2] = px[i + 2]; }
    d.ancho = w; d.alto = h; cache.set(clave, d);
    for (const e of porObjeto.values()) e.clave = "";            // fuerza a redibujar con la imagen
  };
  im.onerror = () => {};                                          // sin la imagen se conserva la textura procedural
  im.src = TEXTURAS_REALES[clave].url;
}

// ---- ruido de valor 3D determinista
function hash(ix, iy, iz) {
  let h = (ix * 374761393 + iy * 668265263 + iz * 2147483647) | 0;
  h = (h ^ (h >>> 13)) * 1274126177 | 0;
  return ((h ^ (h >>> 16)) >>> 0) / 4294967295;
}
function ruido(x, y, z) {
  const ix = Math.floor(x), iy = Math.floor(y), iz = Math.floor(z);
  const fx = x - ix, fy = y - iy, fz = z - iz;
  const u = fx * fx * (3 - 2 * fx), v = fy * fy * (3 - 2 * fy), w = fz * fz * (3 - 2 * fz);
  const c = (a, b, d) => hash(ix + a, iy + b, iz + d);
  const x00 = c(0, 0, 0) + (c(1, 0, 0) - c(0, 0, 0)) * u, x10 = c(0, 1, 0) + (c(1, 1, 0) - c(0, 1, 0)) * u;
  const x01 = c(0, 0, 1) + (c(1, 0, 1) - c(0, 0, 1)) * u, x11 = c(0, 1, 1) + (c(1, 1, 1) - c(0, 1, 1)) * u;
  const y0 = x00 + (x10 - x00) * v, y1 = x01 + (x11 - x01) * v;
  return y0 + (y1 - y0) * w;
}
function fbm(x, y, z, oct = 4) {
  let a = 0.5, s = 0, f = 1;
  for (let i = 0; i < oct; i++) { s += a * ruido(x * f, y * f, z * f); f *= 2.03; a *= 0.5; }
  return s;
}
const mezcla = (a, b, t) => [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t];
const hex = (h) => [parseInt(h.slice(1, 3), 16), parseInt(h.slice(3, 5), 16), parseInt(h.slice(5, 7), 16)];

function masaTierra(lonDeg, latDeg) {
  const x = Math.min(MW - 1, Math.max(0, Math.floor(((lonDeg + 180) / 360) * MW)));
  const y = Math.min(MH - 1, Math.max(0, Math.floor(((90 - latDeg) / 180) * MH)));
  const k = y * MW + x;
  return (MASCARA[k >> 3] >> (7 - (k & 7))) & 1;
}
let MASCARA = null;
function iniciarMascara() {
  if (MASCARA) return;
  const s = (typeof atob === "function") ? atob(BITS) : Buffer.from(BITS, "base64").toString("binary");
  MASCARA = new Uint8Array(s.length);
  for (let i = 0; i < s.length; i++) MASCARA[i] = s.charCodeAt(i);
}

// Mares lunares principales: [lon E (°), lat N (°), radio angular aproximado (°), intensidad]
const MARES = [[-57, 18, 22, 0.55], [-16, 33, 11, 0.6], [18, 28, 7, 0.55], [31, 8.5, 9, 0.6], [59, 17, 4.5, 0.65], [51, -7.8, 7, 0.45],
  [-16, -21, 8, 0.5], [-39, -24, 5, 0.55], [35, -15, 4.5, 0.5], [-1, 56, 9, 0.35], [-2, 0, 5, 0.4], [-20, 8, 6, 0.4]];

const BANDAS_JUPITER = [[-90, "#c9b79a"], [-60, "#b48c66"], [-45, "#d8c4a4"], [-30, "#9c6a49"], [-20, "#e4d3b4"], [-8, "#b87a52"], [0, "#efe1c6"], [8, "#c58a5e"], [20, "#e6d4b6"],
  [30, "#a8794f"], [42, "#d9c6a6"], [55, "#b49470"], [70, "#a9a7a8"], [90, "#8f9193"]];
const BANDAS_SATURNO = [[-90, "#9fa3a8"], [-55, "#c6b58c"], [-35, "#e0cb9a"], [-15, "#d3b980"], [0, "#ead6a2"], [12, "#d6bc84"], [30, "#e3cf9e"], [48, "#c2ab7c"], [70, "#b3a98f"], [90, "#8f9aa5"]];

function colorAnillos(tabla, lat, lon, turb) {
  let i = 0;
  while (i < tabla.length - 1 && lat > tabla[i][0]) i++;
  const [l1, c1] = tabla[Math.max(0, i - 1)], [l2, c2] = tabla[i];
  const t = Math.min(1, Math.max(0, (lat - l1) / Math.max(1e-6, l2 - l1)));
  const base = mezcla(hex(c1), hex(c2), t * t * (3 - 2 * t));
  const f = 0.94 + 0.12 * turb;
  return [base[0] * f, base[1] * f, base[2] * f];
}

function colorTextura(clave, x, y, z, lon, lat) {
  const turb = fbm(x * 3 + 7, y * 3, z * 3, 3);
  switch (clave) {
    case "tierra": {
      iniciarMascara();
      const dx = 0.17, dy = 0.17;
      const tierra = (masaTierra(lon - dx, lat - dy) + masaTierra(lon + dx, lat - dy) + masaTierra(lon - dx, lat + dy) + masaTierra(lon + dx, lat + dy)) / 4;
      const n = fbm(x * 6, y * 6, z * 6, 4);
      const oceano = mezcla([10, 44, 98], [22, 78, 140], n * 0.7);
      const suelo0 = mezcla(mezcla([58, 110, 52], [86, 126, 58], n), [182, 150, 98], Math.min(1, Math.max(0, 1 - Math.abs(lat) / 38) * (0.4 + 0.6 * n) * 0.9));
      const hielo = Math.abs(lat) > 66 || lat < -62;
      const suelo = hielo ? mezcla(suelo0, [238, 242, 246], 0.92) : suelo0;
      let c = mezcla(oceano, suelo, tierra);
      if (tierra < 0.5 && Math.abs(lat) > 72) c = mezcla(c, [225, 235, 242], 0.85);
      const nube = Math.max(0, fbm(x * 4 + 11, y * 4, z * 4, 5) - 0.52) * 3.2;
      return mezcla(c, [250, 250, 252], Math.min(0.85, nube));
    }
    case "luna": {
      const n = fbm(x * 9, y * 9, z * 9, 5);
      let osc = 0;
      for (const [lo, la, r, k] of MARES) {
        const dl = ((lon - lo + 540) % 360) - 180;
        const d = Math.hypot(dl * Math.cos(la * Math.PI / 180), lat - la) / r;
        osc = Math.max(osc, k * Math.exp(-d * d * 1.6));
      }
      const g = 150 + 70 * (n - 0.5) - 85 * osc;
      return [g, g * 0.985, g * 0.95];
    }
    case "marte": {
      const n = fbm(x * 5, y * 5, z * 5, 5);
      let c = mezcla([186, 98, 56], [214, 142, 88], n);
      const osc = Math.max(0, fbm(x * 3 + 5, y * 3, z * 3, 4) - 0.5) * 2.2;
      c = mezcla(c, [88, 56, 44], Math.min(0.75, osc));
      if (Math.abs(lat) > 80) c = mezcla(c, [244, 244, 248], 0.9);
      return c;
    }
    case "jupiter": return colorAnillos(BANDAS_JUPITER, lat + (turb - 0.5) * 6, lon, turb);
    case "saturno": return colorAnillos(BANDAS_SATURNO, lat + (turb - 0.5) * 4, lon, turb);
    case "urano": { const f = 1 - Math.abs(lat) / 260; return [150 * f + 12 * turb, 214 * f + 8 * turb, 224 * f]; }
    case "neptuno": { const f = 0.9 + 0.2 * turb; const banda = 0.5 + 0.5 * Math.sin(lat * 0.18 + turb * 2); return mezcla([48, 82, 190], [86, 124, 226], banda * 0.5).map((v) => v * f); }
    case "pluton": { // ilustrativo: llanuras claras («corazón») y terreno oscuro rojizo
      const n = fbm(x * 6, y * 6, z * 6, 5);
      const dl = ((lon - 178 + 540) % 360) - 180, d = Math.hypot(dl * Math.cos(20 * Math.PI / 180), lat - 20) / 22;
      const claro = Math.exp(-d * d * 2);
      const base = mezcla([112, 78, 62], [176, 140, 112], n);
      return mezcla(base, [232, 214, 196], Math.min(0.92, claro));
    }
    case "mercurio": { const n = fbm(x * 10, y * 10, z * 10, 5); const g = 120 + 80 * n; return [g, g * 0.97, g * 0.94]; }
    case "venus": { const n = fbm(x * 3, y * 3, z * 3, 4); return mezcla([226, 196, 130], [244, 226, 176], n); }
    case "sol": { const n = fbm(x * 8, y * 8, z * 8, 4); return mezcla([255, 190, 70], [255, 232, 140], n); }
    default: { // satélite genérico: gris con cráteres suaves
      const n = fbm(x * 8, y * 8, z * 8, 5);
      const base = hex(clave.startsWith("#") ? clave : "#b8b3aa");
      const f = 0.72 + 0.5 * n;
      return [base[0] * f, base[1] * f, base[2] * f];
    }
  }
}

function textura(clave) {
  if (TEXTURAS_REALES[clave]) cargarImagen(clave);
  if (cache.has(clave)) return cache.get(clave);
  const ANCHO_T = GRANDES.has(clave) ? 1024 : 512, ALTO_T = ANCHO_T / 2;
  const d = new Uint8ClampedArray(ANCHO_T * ALTO_T * 3);
  for (let j = 0; j < ALTO_T; j++) {
    const lat = 90 - ((j + 0.5) / ALTO_T) * 180;
    const cl = Math.cos(lat * Math.PI / 180), sl = Math.sin(lat * Math.PI / 180);
    for (let i = 0; i < ANCHO_T; i++) {
      const lon = -180 + ((i + 0.5) / ANCHO_T) * 360;
      const a = lon * Math.PI / 180;
      const c = colorTextura(clave, cl * Math.cos(a), cl * Math.sin(a), sl, lon, lat);
      const k = (j * ANCHO_T + i) * 3;
      d[k] = c[0]; d[k + 1] = c[1]; d[k + 2] = c[2];
    }
  }
  d.ancho = ANCHO_T; d.alto = ALTO_T;
  if (!TEXTURAS_REALES[clave]) cache.set(clave, d);               // la procedural de un cuerpo con imagen real es provisional
  return d;
}

const porObjeto = new Map(); // un lienzo por cuerpo: si la vista, la luz y la orientación no cambian, no se vuelve a calcular

/**
 * Dibuja la esfera de `o` con proyección ortográfica y sombreado de Lambert.
 * v = {r, u, t} ejes de la vista en el marco eclíptico (derecha, arriba, hacia la cámara); luz: vector unitario hacia el Sol.
 * base = {x,y,z} ejes del cuerpo (meridiano 0, este, polo) en el marco eclíptico. Devuelve nada.
 */
export function esferaPixeles(ctx, o, cx, cy, rpx, v, luz, base) {
  const S = Math.max(24, Math.min(340, Math.ceil(rpx * 2)));
  let ent = porObjeto.get(o.id);
  if (!ent || ent.S !== S) {
    const l = document.createElement("canvas"); l.width = l.height = S;
    const c2 = l.getContext("2d");
    ent = { S, lienzo: l, lctx: c2, imagen: c2.createImageData(S, S), clave: "" };
    porObjeto.set(o.id, ent);
  }
  const q = (a) => a.map((x) => Math.round(x * 1e5)).join(",");
  const clave = [S, q(v.r), q(v.u), q(v.t), q(luz), q(base.x), q(base.y), q(base.z)].join("|");
  const lienzo = ent.lienzo;
  if (clave === ent.clave) {
    ctx.imageSmoothingEnabled = true;
    ctx.drawImage(lienzo, cx - rpx, cy - rpx, rpx * 2, rpx * 2);
    return;
  }
  ent.clave = clave;
  const imagen = ent.imagen, lctx = ent.lctx;
  const tex = textura(o.textura || "generico");
  const TW = tex.ancho, TH = tex.alto;
  const c = 1 / ((1 - (o.aplan || 0)) ** 2);
  // componentes de los ejes de la vista en el sistema del cuerpo
  const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
  const R = [dot(v.r, base.x), dot(v.r, base.y), dot(v.r, base.z)];
  const U = [dot(v.u, base.x), dot(v.u, base.y), dot(v.u, base.z)];
  const T = [dot(v.t, base.x), dot(v.t, base.y), dot(v.t, base.z)];
  const L = [dot(luz, base.x), dot(luz, base.y), dot(luz, base.z)];
  const A = T[0] * T[0] + T[1] * T[1] + c * T[2] * T[2];
  const d = imagen.data, half = S / 2;
  const luna = o.textura === "luna", atm = o.atmosfera;
  const ambiente = o.autoluminoso ? 1 : 0.035;
  for (let j = 0; j < S; j++) {
    const Y = -((j + 0.5) - half) / half;
    for (let i = 0; i < S; i++) {
      const X = ((i + 0.5) - half) / half;
      const px = (j * S + i) * 4;
      const q0 = R[0] * X + U[0] * Y, q1 = R[1] * X + U[1] * Y, q2 = R[2] * X + U[2] * Y;
      const B = T[0] * q0 + T[1] * q1 + c * T[2] * q2;
      const C = q0 * q0 + q1 * q1 + c * q2 * q2 - 1;
      const disc = B * B - A * C;
      if (disc < 0) { d[px + 3] = 0; continue; }
      const Z = (-B + Math.sqrt(disc)) / A;
      const x = q0 + T[0] * Z, y = q1 + T[1] * Z, z = q2 + T[2] * Z;
      // normal del elipsoide ~ (x, y, c z)
      const nn = Math.hypot(x, y, c * z) || 1;
      const nx = x / nn, ny = y / nn, nz = c * z / nn;
      const lam = nx * L[0] + ny * L[1] + nz * L[2];
      const rr = Math.hypot(x, y, z) || 1;
      const lat = Math.asin(Math.max(-1, Math.min(1, z / rr)));
      const lon = Math.atan2(y, x);
      const fu = (lon * 180 / Math.PI + 180) / 360 * TW - 0.5, fv = Math.min(TH - 1.001, Math.max(0, (90 - lat * 180 / Math.PI) / 180 * TH - 0.5));
      const i0 = Math.floor(fu), j0 = Math.floor(fv), wu = fu - i0, wv = fv - j0;
      const ia = ((i0 % TW) + TW) % TW, ib = (ia + 1) % TW;
      const k00 = (j0 * TW + ia) * 3, k10 = (j0 * TW + ib) * 3, k01 = ((j0 + 1) * TW + ia) * 3, k11 = ((j0 + 1) * TW + ib) * 3;
      const w00 = (1 - wu) * (1 - wv), w10 = wu * (1 - wv), w01 = (1 - wu) * wv, w11 = wu * wv;
      const tr = tex[k00] * w00 + tex[k10] * w10 + tex[k01] * w01 + tex[k11] * w11;
      const tg = tex[k00 + 1] * w00 + tex[k10 + 1] * w10 + tex[k01 + 1] * w01 + tex[k11 + 1] * w11;
      const tb = tex[k00 + 2] * w00 + tex[k10 + 2] * w10 + tex[k01 + 2] * w01 + tex[k11 + 2] * w11;
      let luzf;
      if (o.autoluminoso) {
        const mu = Math.max(0, (T[0] * x + T[1] * y + c * T[2] * z) / rr);
        luzf = 0.6 + 0.4 * mu;
      } else {
        const t = Math.min(1, Math.max(0, (lam + 0.04) / 0.14));
        luzf = ambiente + (1 - ambiente) * t * t * (3 - 2 * t) * (luna ? 1 : 0.55 + 0.45 * Math.max(0, lam));
      }
      let r = tr * luzf, g = tg * luzf, b = tb * luzf;
      if (atm) { // halo atmosférico en el limbo, sólo del lado iluminado
        const mu = Math.max(0, (T[0] * x + T[1] * y + c * T[2] * z) / rr);
        const rim = Math.pow(1 - mu, 3) * Math.max(0, Math.min(1, lam + 0.25)) * atm.k;
        r += atm.c[0] * rim; g += atm.c[1] * rim; b += atm.c[2] * rim;
      }
      d[px] = r; d[px + 1] = g; d[px + 2] = b; d[px + 3] = 255;
    }
  }
  lctx.putImageData(imagen, 0, 0);
  const dd = rpx * 2;
  ctx.imageSmoothingEnabled = true;
  ctx.drawImage(lienzo, cx - rpx, cy - rpx, dd, dd);
}
