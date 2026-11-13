// SPDX-License-Identifier: Apache-2.0
// Lectura de las tablas de efemérides de JPL Horizons y evaluación por interpolación de Lagrange de 10 puntos.
// Formato: <sistema>.json (metadatos) + <sistema>.bin (posiciones x,y,z en km, eclíptica J2000, centradas en el
// planeta —o en el Sol para `sol`— con paso regular). Ver simuladores/documentacion/DATOS_Y_EFEMERIDES.md.

const NODOS = 10;
const DESDE = -(NODOS / 2 - 1); // -4
const HASTA = NODOS / 2;        //  5
const DEN = new Float64Array(NODOS); // denominadores de Lagrange (constantes)
for (let a = 0; a < NODOS; a++) {
  let d = 1;
  for (let b = 0; b < NODOS; b++) if (a !== b) d *= a - b;
  DEN[a] = d;
}

function pesos(u, w) {
  for (let a = 0; a < NODOS; a++) {
    const j = a + DESDE;
    let n = 1;
    for (let b = 0; b < NODOS; b++) if (a !== b) n *= u - (b + DESDE);
    w[a] = n / DEN[a];
  }
}

export class TablaCuerpo {
  constructor(meta, buffer) {
    this.meta = meta;
    this.id = String(meta.id);
    this.nombre = meta.nombre;
    this.t0 = meta.t0;
    this.h = meta.paso_min / 1440;
    this.n = meta.n;
    this.esc = meta.fmt === "i16" ? meta.escala_i16 : 1;
    const raw = buffer.slice(meta.offset, meta.offset + meta.longitud); // copia alineada
    this.datos = meta.fmt === "f64" ? new Float64Array(raw) : meta.fmt === "f32" ? new Float32Array(raw) : new Int16Array(raw);
    this._w = new Float64Array(NODOS);
  }

  /** Posición [x,y,z] (km) en `jdTdb`. Escribe en `out` si se da. */
  pos(jdTdb, out = [0, 0, 0]) {
    const s = (jdTdb - this.t0) / this.h;
    let i = Math.floor(s);
    if (i + DESDE < 0) i = -DESDE;
    if (i + HASTA >= this.n) i = this.n - HASTA - 1;
    const u = s - i;
    const w = this._w;
    pesos(u, w);
    let x = 0, y = 0, z = 0;
    const d = this.datos;
    for (let a = 0; a < NODOS; a++) {
      const k = (i + a + DESDE) * 3;
      const wa = w[a];
      x += wa * d[k]; y += wa * d[k + 1]; z += wa * d[k + 2];
    }
    out[0] = x * this.esc; out[1] = y * this.esc; out[2] = z * this.esc;
    return out;
  }

  /** Velocidad [km/s] por diferencia central de la propia interpolación (paso = 1/200 del intervalo de la tabla). */
  vel(jdTdb, out = [0, 0, 0]) {
    const dt = this.h / 200;
    const a = this.pos(jdTdb - dt), b = this.pos(jdTdb + dt);
    const k = 1 / (2 * dt * 86400);
    out[0] = (b[0] - a[0]) * k; out[1] = (b[1] - a[1]) * k; out[2] = (b[2] - a[2]) * k;
    return out;
  }
}

export class Sistema {
  constructor(meta, buffer) {
    this.meta = meta;
    this.nombre = meta.sistema;
    this.cuerpos = new Map();
    for (const c of meta.cuerpos) this.cuerpos.set(String(c.id), new TablaCuerpo(c, buffer));
  }
  cuerpo(id) { return this.cuerpos.get(String(id)); }
  pos(id, jdTdb, out) { return this.cuerpos.get(String(id)).pos(jdTdb, out); }
}

/** Descarga un sistema. `base` es la URL de la carpeta `datos/`. `progreso(fraccion)` es opcional. */
export async function cargarSistema(nombre, base, progreso = () => {}) {
  const meta = await (await fetch(`${base}/${nombre}.json`)).json();
  const r = await fetch(`${base}/${nombre}.bin`);
  if (!r.ok) throw new Error(`No se pudo descargar ${nombre}.bin (${r.status})`);
  const total = +r.headers.get("content-length") || 0;
  let buffer;
  if (r.body && total) {
    const lector = r.body.getReader();
    const trozos = [];
    let rec = 0;
    for (;;) {
      const { done, value } = await lector.read();
      if (done) break;
      trozos.push(value); rec += value.length;
      progreso(Math.min(1, rec / total));
    }
    const todo = new Uint8Array(rec);
    let p = 0;
    for (const t of trozos) { todo.set(t, p); p += t.length; }
    buffer = todo.buffer;
  } else {
    buffer = await r.arrayBuffer();
  }
  progreso(1);
  return new Sistema(meta, buffer);
}

/** Versión para Node (pruebas): lee desde disco. */
export function sistemaDesdeBytes(meta, bytes) {
  const buf = bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength);
  return new Sistema(meta, buf);
}
