// SPDX-License-Identifier: Apache-2.0
// Cometas periódicos 2027–2050: efemérides de JPL Horizons (solución orbital vigente de cada cometa) y sus hitos (perihelio, afelio y acercamientos
// a la Tierra y a Júpiter) hallados en los datos, no tecleados. Todo posterior a la fecha de descarga es una PREDICCIÓN.
import { UA_KM } from "./cuerpos.js";

export const COMETAS = {
  "1P": { nombre: "1P/Halley", color: "#9ad0ff", nota: "El cometa más famoso: órbita retrógrada de ≈ 76 años; su último perihelio fue en 1986 y el próximo será en 2061. En 2027–2050 se acerca desde el afelio (2023). Origina las Oriónidas y las Eta Acuáridas." },
  "2P": { nombre: "2P/Encke", color: "#ffd166", nota: "El cometa de periodo más corto conocido (≈ 3,3 años); su órbita no sale de la de Júpiter. Se asocia a las Táuridas." },
  "8P": { nombre: "8P/Tuttle", color: "#ff9f9f", nota: "Periodo de ≈ 13,6 años y órbita inclinada." },
  "9P": { nombre: "9P/Tempel 1", color: "#c3a6ff", nota: "Blanco de la sonda Deep Impact de la NASA, que lanzó un impactador contra su núcleo en 2005." },
  "10P": { nombre: "10P/Tempel 2", color: "#b8e6a0", nota: "Cometa de la familia de Júpiter con ≈ 5,4 años de periodo." },
  "12P": { nombre: "12P/Pons–Brooks", color: "#ffb36b", nota: "Cometa de tipo Halley de ≈ 71 años; su último perihelio fue en 2024, así que en 2027–2050 se aleja." },
  "17P": { nombre: "17P/Holmes", color: "#e0c3ff", nota: "Famoso por su estallido de 2007, cuando su coma se hizo mayor que el Sol durante unos días." },
  "19P": { nombre: "19P/Borrelly", color: "#7ee0d1", nota: "Visitado por la sonda Deep Space 1 en 2001." },
  "21P": { nombre: "21P/Giacobini–Zinner", color: "#8fb7ff", nota: "Origina la lluvia de las Dracónidas; fue visitado por la sonda ICE en 1985." },
  "46P": { nombre: "46P/Wirtanen", color: "#a8f0c6", nota: "Objetivo original de la misión Rosetta; en diciembre de 2018 pasó a 0,08 UA de la Tierra." },
  "55P": { nombre: "55P/Tempel–Tuttle", color: "#ffd9a0", nota: "Origina las Leónidas (periodo de ≈ 33 años); su perihelio de 2031 será el siguiente a los de 1998 y 1965." },
  "67P": { nombre: "67P/Churyumov–Gerasimenko", color: "#ff8a6c", nota: "Orbitado por la sonda Rosetta de la ESA (2014–2016), que le dejó el módulo Philae." },
  "81P": { nombre: "81P/Wild 2", color: "#9dd0ff", nota: "La sonda Stardust recogió polvo de su coma en 2004 y lo trajo a la Tierra." },
  "96P": { nombre: "96P/Machholz 1", color: "#ff7fb0", nota: "Pasa muy cerca del Sol (perihelio ≈ 0,12 UA) en una órbita de ≈ 5,3 años." },
  "103P": { nombre: "103P/Hartley 2", color: "#ffe08a", nota: "Visitado por la misión EPOXI en 2010." },
  "109P": { nombre: "109P/Swift–Tuttle", color: "#d9a0ff", nota: "Origina las Perseidas; periodo de ≈ 133 años y núcleo de unos 26 km. Su próximo perihelio será en 2126." },
};

const dist = (a, b) => Math.hypot(a[0] - b[0], a[1] - b[1], a[2] - b[2]);

/** Mínimo local de f(jd) con refinamiento por la sección áurea alrededor del mínimo muestreado. */
function minimos(f, jd0, jd1, paso, signo = 1) {
  const out = [], n = Math.floor((jd1 - jd0) / paso), v = new Float64Array(n + 1);
  for (let i = 0; i <= n; i++) v[i] = signo * f(jd0 + i * paso);
  for (let i = 1; i < n; i++) if (v[i] <= v[i - 1] && v[i] < v[i + 1]) {
    let lo = jd0 + (i - 1) * paso, hi = jd0 + (i + 1) * paso; const g = (Math.sqrt(5) - 1) / 2;
    let x1 = hi - g * (hi - lo), x2 = lo + g * (hi - lo), f1 = signo * f(x1), f2 = signo * f(x2);
    for (let k = 0; k < 60; k++) { if (f1 < f2) { hi = x2; x2 = x1; f2 = f1; x1 = hi - g * (hi - lo); f1 = signo * f(x1); } else { lo = x1; x1 = x2; f1 = f2; x2 = lo + g * (hi - lo); f2 = signo * f(x2); } }
    out.push((lo + hi) / 2);
  }
  return out;
}

/**
 * Hitos de un cometa dentro de los datos: perihelio, afelio, mínimos de la distancia a la Tierra (< 1,5 UA) y a Júpiter (< 1 UA).
 * `sol` es el sistema heliocéntrico con la Tierra («399») y Júpiter («599»).
 */
export function hitosCometa(tabla, sol) {
  const ini = tabla.meta.jd_valido_ini, fin = tabla.meta.jd_valido_fin, tE = sol.cuerpo("399"), tJ = sol.cuerpo("599"), a = [0, 0, 0], b = [0, 0, 0];
  const rS = (j) => Math.hypot(...tabla.pos(j, a)), dE = (j) => dist(tabla.pos(j, a), tE.pos(j, b)), dJ = (j) => dist(tabla.pos(j, a), tJ.pos(j, b));
  const out = [];
  for (const j of minimos(rS, ini, fin, 2)) out.push({ tipo: "perihelio", jdTdb: j, dist_ua: rS(j) / UA_KM });
  for (const j of minimos(rS, ini, fin, 2, -1)) out.push({ tipo: "afelio", jdTdb: j, dist_ua: rS(j) / UA_KM });
  for (const j of minimos(dE, ini, fin, 2)) if (dE(j) / UA_KM < 1.5) out.push({ tipo: "tierra", jdTdb: j, dist_ua: dE(j) / UA_KM });
  for (const j of minimos(dJ, ini, fin, 2)) if (dJ(j) / UA_KM < 1.0) out.push({ tipo: "jupiter", jdTdb: j, dist_ua: dJ(j) / UA_KM });
  return out.sort((x, y) => x.jdTdb - y.jdTdb);
}
export const ETIQUETA = { perihelio: "Perihelio", afelio: "Afelio", tierra: "Más cerca de la Tierra", jupiter: "Más cerca de Júpiter" };
