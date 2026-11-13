// SPDX-License-Identifier: Apache-2.0
// Búsqueda de eclipses de Sol y de Luna a partir de las efemérides del Sol (-Tierra heliocéntrica) y de la Luna geocéntrica.
// Geometría de conos (penumbra/umbra) con radios reales; sin atmósfera salvo el agrandamiento atmosférico de 1 % del radio terrestre
// para la sombra. Es un cálculo propio de este proyecto, NO un catálogo oficial: sus resultados se contrastan con el catálogo
// de la NASA (Espenak/Meeus) en pruebas/ y la diferencia esperada es de minutos en la hora del máximo.
import { jdUtcDesdeTdb } from "./tiempo.js";
import { SOL, PLANETAS, LUNA } from "./cuerpos.js";

const RS = SOL.radio, RE = PLANETAS["399"].radio, RM = LUNA.radio;
const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
const sub = (a, b) => [a[0] - b[0], a[1] - b[1], a[2] - b[2]];
const mul = (a, k) => [a[0] * k, a[1] * k, a[2] * k];
const nrm = (a) => Math.hypot(a[0], a[1], a[2]);
const envolver = (x) => { x = (x + Math.PI) % (2 * Math.PI); if (x < 0) x += 2 * Math.PI; return x - Math.PI; };

export function crearGeometria(sol, tierra) {
  const tE = sol.cuerpo("399"), tM = tierra.cuerpo("301");
  const estado = (jd) => { const e = tE.pos(jd); return { S: [-e[0], -e[1], -e[2]], M: tM.pos(jd) }; };

  function solar(jd) {
    const { S, M } = estado(jd);
    const dSM = sub(M, S), D = nrm(dSM), d = mul(dSM, 1 / D);
    const w = mul(S, -1);
    const q = nrm(sub(w, mul(d, dot(w, d))));
    const f1 = Math.asin((RS + RM) / D), f2 = Math.asin((RS - RM) / D);
    const z = -dot(M, d);
    const l1 = z * Math.tan(f1) + RM / Math.cos(f1);
    const l2 = RM / Math.cos(f2) - z * Math.tan(f2);
    return { q, l1, l2, D, S, M };
  }
  function lunar(jd) {
    const { S, M } = estado(jd);
    const Dse = nrm(S), a = mul(S, -1 / Dse);
    const x = dot(M, a), q = nrm(sub(M, mul(a, x)));
    const Re2 = RE * 1.01; // agrandamiento atmosférico de la sombra: 1 % (convención del catálogo de la NASA)
    const fu = Math.asin((RS - Re2) / Dse), fp = Math.asin((RS + Re2) / Dse);
    const ru = Re2 - x * Math.tan(fu), rp = Re2 + x * Math.tan(fp);
    return { q, x, ru, rp, umbral: (ru + RM - q) / (2 * RM), penumbral: (rp + RM - q) / (2 * RM), S, M };
  }
  const dl = (jd) => { const { S, M } = estado(jd); return envolver(Math.atan2(M[1], M[0]) - Math.atan2(S[1], S[0])); };

  function minimizar(f, a, b) {
    const g = (Math.sqrt(5) - 1) / 2;
    let c = b - g * (b - a), d = a + g * (b - a), fc = f(c), fd = f(d);
    for (let i = 0; i < 60 && b - a > 1e-7; i++) {
      if (fc < fd) { b = d; d = c; fd = fc; c = b - g * (b - a); fc = f(c); }
      else { a = c; c = d; fc = fd; d = a + g * (b - a); fd = f(d); }
    }
    return (a + b) / 2;
  }

  function buscar(jdTdb0, jdTdb1) {
    const res = [];
    const paso = 0.25;
    for (const [objetivo, tipo] of [[0, "solar"], [Math.PI, "lunar"]]) {
      const g = (jd) => envolver(dl(jd) - objetivo);
      let a = jdTdb0, ga = g(a);
      for (let t = jdTdb0 + paso; t <= jdTdb1 + paso; t += paso) {
        const gb = g(t);
        if (ga < 0 && gb >= 0 && Math.abs(ga) < 1 && Math.abs(gb) < 1) {
          let lo = a, hi = t;
          for (let i = 0; i < 50; i++) { const m = (lo + hi) / 2; if (g(m) < 0) lo = m; else hi = m; }
          const tc = (lo + hi) / 2;
          if (tipo === "solar") {
            const tm = minimizar((x) => solar(x).q, tc - 0.4, tc + 0.4);
            const r = solar(tm);
            let clase = null;
            if (r.q < RE + Math.abs(r.l2)) clase = r.l2 > 0 ? "total" : "anular";
            else if (r.q < RE + r.l1) clase = "parcial";
            if (clase) res.push({ tipo, clase, jdTdb: tm, jdUtc: jdUtcDesdeTdb(tm), gamma: r.q / RE, penumbra_re: r.l1 / RE, umbra_km: r.l2 });
          } else {
            const tm = minimizar((x) => lunar(x).q, tc - 0.4, tc + 0.4);
            const r = lunar(tm);
            let clase = null;
            if (r.umbral >= 1) clase = "total";
            else if (r.umbral > 0) clase = "parcial";
            else if (r.penumbral > 0) clase = "penumbral";
            if (clase) res.push({ tipo, clase, jdTdb: tm, jdUtc: jdUtcDesdeTdb(tm), mag_umbral: r.umbral, mag_penumbral: r.penumbral });
          }
        }
        a = t; ga = gb;
      }
    }
    return res.sort((p, q) => p.jdTdb - q.jdTdb);
  }
  return { solar, lunar, buscar, estado, dl };
}
