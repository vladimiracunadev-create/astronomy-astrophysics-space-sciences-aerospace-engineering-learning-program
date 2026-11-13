// SPDX-License-Identifier: Apache-2.0
// Tiempo del simulador. Escala interna: TDB (la de las efemérides de JPL). Se muestra en UTC.
// UTC -> TDB = UTC + (TAI-UTC) + 32,184 s + (TDB-TT, < 2 ms). Con 37 s de segundos intercalares (vigentes desde 2017)
// resultan 69,184 s. No se conocen los segundos intercalares futuros (y la CGPM decidió eliminarlos hacia 2035):
// se mantiene 69,184 s constante; el error posible hasta 2050 es de pocos segundos (< 0,002 grados en la Luna).

export const JD_UNIX = 2440587.5;
export const JD_J2000 = 2451545.0;
export const SEG_DIA = 86400;
export const DELTA_TDB_UTC_S = 69.184;
export const INICIO_UTC_MS = Date.UTC(2027, 0, 1, 0, 0, 0);
export const FIN_UTC_MS = Date.UTC(2050, 11, 31, 23, 59, 59);

export const jdUtcDesdeMs = (ms) => ms / 86400000 + JD_UNIX;
export const msDesdeJdUtc = (jd) => (jd - JD_UNIX) * 86400000;
export const jdTdbDesdeUtc = (jdUtc) => jdUtc + DELTA_TDB_UTC_S / SEG_DIA;
export const jdUtcDesdeTdb = (jdTdb) => jdTdb - DELTA_TDB_UTC_S / SEG_DIA;
export const siglosJ2000 = (jdTdb) => (jdTdb - JD_J2000) / 36525;

const dos = (n) => String(n).padStart(2, "0");

/** Texto "AAAA-MM-DD hh:mm:ss UTC" desde un JD UTC. */
export function formatoUtc(jdUtc, conSegundos = true) {
  const d = new Date(Math.round(msDesdeJdUtc(jdUtc)));
  const s = `${d.getUTCFullYear()}-${dos(d.getUTCMonth() + 1)}-${dos(d.getUTCDate())} ${dos(d.getUTCHours())}:${dos(d.getUTCMinutes())}`;
  return (conSegundos ? `${s}:${dos(d.getUTCSeconds())}` : s) + " UTC";
}

/** Valor para <input type="datetime-local"> (en UTC). */
export function valorInputUtc(jdUtc) {
  const d = new Date(Math.round(msDesdeJdUtc(jdUtc)));
  return `${d.getUTCFullYear()}-${dos(d.getUTCMonth() + 1)}-${dos(d.getUTCDate())}T${dos(d.getUTCHours())}:${dos(d.getUTCMinutes())}`;
}

export function jdUtcDesdeInput(txt) {
  const m = /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})/.exec(txt || "");
  if (!m) return null;
  return jdUtcDesdeMs(Date.UTC(+m[1], +m[2] - 1, +m[3], +m[4], +m[5]));
}

export const JD_UTC_INICIO = jdUtcDesdeMs(INICIO_UTC_MS);
export const JD_UTC_FIN = jdUtcDesdeMs(FIN_UTC_MS);
export const limitar = (jd) => Math.min(JD_UTC_FIN, Math.max(JD_UTC_INICIO, jd));

/** Reloj de simulación: avanza `velocidad` segundos simulados por segundo real. */
export class Reloj {
  constructor(jdUtc = JD_UTC_INICIO) {
    this.jdUtc = limitar(jdUtc);
    this.velocidad = 3600; // 1 h simulada por segundo
    this.activo = false;
    this._t = null;
  }
  get jdTdb() { return jdTdbDesdeUtc(this.jdUtc); }
  fijar(jdUtc) { this.jdUtc = limitar(jdUtc); }
  paso(ahoraMs) {
    if (this._t !== null && this.activo) {
      const dt = Math.min(0.25, (ahoraMs - this._t) / 1000);
      let jd = this.jdUtc + (dt * this.velocidad) / SEG_DIA;
      if (jd >= JD_UTC_FIN) { jd = JD_UTC_FIN; this.activo = false; }
      if (jd <= JD_UTC_INICIO) { jd = JD_UTC_INICIO; if (this.velocidad < 0) this.activo = false; }
      this.jdUtc = jd;
    }
    this._t = ahoraMs;
  }
}

/** Ángulo de rotación terrestre (ERA, IERS 2003), radianes, con UT1 ~ UTC (|UT1-UTC| < 0,9 s). */
export function anguloRotacionTerrestre(jdUtc) {
  const t = jdUtc - JD_J2000;
  const f = 0.7790572732640 + 1.00273781191135448 * t;
  return 2 * Math.PI * (f - Math.floor(f));
}
