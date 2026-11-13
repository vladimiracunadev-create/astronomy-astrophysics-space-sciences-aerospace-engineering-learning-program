// SPDX-License-Identifier: Apache-2.0
// Misiones espaciales ya realizadas: trayectorias heliocéntricas reconstruidas por JPL (SPICE, vía Horizons) y los planetas 1970–2050.
// Los acercamientos a planetas se DETECTAN en los datos (mínimos de distancia nave–planeta), no se teclean a mano.
// Las trayectorias posteriores a la fecha de descarga (13-nov-2026) son PREDICCIONES de JPL.
import { UA_KM } from "./cuerpos.js";

export const MISIONES = {
  "-23": { nombre: "Pioneer 10", color: "#ffb454", resumen: "Primera nave en cruzar el cinturón de asteroides y en visitar Júpiter (1973). Envió una placa con un mensaje para otras civilizaciones.", planetas: ["599"] },
  "-24": { nombre: "Pioneer 11", color: "#ffd166", resumen: "Visitó Júpiter (1974) y fue la primera nave en llegar a Saturno (1979).", planetas: ["599", "699"] },
  "-31": { nombre: "Voyager 1", color: "#6cb4ff", resumen: "Sobrevoló Júpiter (1979) y Saturno (1980) y es el objeto humano más lejano: cruzó la heliopausa en 2012.", planetas: ["599", "699"], hitos: [["Cruza la heliopausa", "2012-08-25", 121]] },
  "-32": { nombre: "Voyager 2", color: "#7ee0a1", resumen: "La única nave que ha visitado los cuatro planetas gigantes: Júpiter (1979), Saturno (1981), Urano (1986) y Neptuno (1989). Cruzó la heliopausa en 2018.", planetas: ["599", "699", "799", "899"], hitos: [["Cruza la heliopausa", "2018-11-05", 119]] },
  "-77": { nombre: "Galileo", color: "#f78fb3", resumen: "Primer orbitador de Júpiter (1995–2003); lanzó una sonda a su atmósfera y estudió sus lunas. Terminó hundiéndose en Júpiter.", planetas: ["599"], orbita: "599" },
  "-82": { nombre: "Cassini", color: "#c3a6ff", resumen: "Orbitó Saturno de 2004 a 2017 y llevó la sonda Huygens a Titán. Usó cuatro asistencias gravitatorias (Venus dos veces, la Tierra y Júpiter).", planetas: ["599", "699"], orbita: "699" },
  "-98": { nombre: "New Horizons", color: "#ff7a7a", resumen: "Primer sobrevuelo de Plutón (2015); asistencia de Júpiter (2007) y posterior visita al objeto Arrokoth (2019).", planetas: ["599", "9"] },
  "-61": { nombre: "Juno", color: "#ffe08a", resumen: "Orbitador polar de Júpiter desde 2016. Trayectoria posterior a 2026: predicción de JPL.", planetas: ["599"], orbita: "599" },
  "-96": { nombre: "Parker Solar Probe", color: "#ff9f43", resumen: "Se acerca al Sol más que ninguna otra nave, con asistencias gravitatorias de Venus. Trayectoria posterior a 2026: predicción de JPL.", planetas: ["299"], umbral_km: 5e5 },
  "-170": { nombre: "James Webb", color: "#4dd2ff", resumen: "Telescopio espacial infrarrojo en el punto L2 Sol–Tierra, a unos 1,5 millones de km de la Tierra, siempre en el lado opuesto al Sol.", planetas: [], l2: true },
  "-159": { nombre: "Europa Clipper", color: "#ffd1a1", resumen: "Misión a la luna Europa de Júpiter (lanzamiento en 2024; llegada prevista en 2030) con asistencias de Marte y la Tierra. Trayectoria posterior a 2026: predicción de JPL.", planetas: ["499", "399", "599"], orbita: "599" },
};
export const NOMBRE_PLANETA = { "199": "Mercurio", "299": "Venus", "399": "Tierra", "499": "Marte", "599": "Júpiter", "699": "Saturno", "799": "Urano", "899": "Neptuno", "9": "Plutón" };

const dist = (a, b) => Math.hypot(a[0] - b[0], a[1] - b[1], a[2] - b[2]);

/** Acercamientos de una nave a los planetas: mínimos locales de la distancia (UA < `umbralUa`) con refinamiento parabólico. */
export function acercamientos(nave, planetas, umbralUa = 0.06) {
  const t = nave, h = t.h, out = [];
  const ini = t.meta.jd_valido_ini, fin = t.meta.jd_valido_fin, p = [0, 0, 0], q = [0, 0, 0];
  for (const [id, tp] of planetas) {
    if (id === "9" && !(ini < 2470000)) continue;
    const f = (jd) => dist(nave.pos(jd, p), tp.pos(jd, q));
    let d0 = f(ini), d1 = f(ini + h);
    for (let jd = ini + h; jd < fin - h; jd += h) {
      const d2 = f(jd + h);
      if (d1 < d0 && d1 <= d2 && d1 < umbralUa * UA_KM) {
        // parábola por tres puntos
        const den = d0 - 2 * d1 + d2, off = den !== 0 ? 0.5 * (d0 - d2) / den : 0, jm = jd + off * h;
        let lo = jm - h, hi = jm + h; for (let k = 0; k < 40; k++) { const m1 = lo + (hi - lo) / 3, m2 = hi - (hi - lo) / 3; if (f(m1) < f(m2)) hi = m2; else lo = m1; }
        const jmin = (lo + hi) / 2;
        out.push({ planeta: id, jdTdb: jmin, dist_km: f(jmin) });
      }
      d0 = d1; d1 = d2;
    }
  }
  return out.sort((a, b) => a.jdTdb - b.jdTdb);
}

/**
 * Hitos de una misión: acercamientos a sus planetas objetivo (o a cualquier cuerpo a < 0,02 UA); un orbitador conserva sólo la llegada (inserción en órbita)
 * y se descartan los pasos siguientes (pericentros) para no inundar la lista.
 */
export function hitosDeMision(id, nave, planetas) {
  const d = MISIONES[id]; if (!d || d.l2) return [];
  const umbral = d.umbral_km || 3e6;
  const todos = acercamientos(nave, planetas, 0.06).filter((e) => e.dist_km < umbral && ((d.planetas || []).includes(e.planeta) || e.dist_km < 0.002 * UA_KM));
  const out = [], visto = {};
  for (const e of todos) {
    const previo = visto[e.planeta]; visto[e.planeta] = e.jdTdb;
    if (previo !== undefined && d.orbita === e.planeta && e.jdTdb - previo < 365.25 * 1.5) continue; // un orbitador repite pericentros: sólo se conserva la llegada
    const orbita = d.orbita === e.planeta && previo === undefined;
    out.push({ ...e, etiqueta: orbita ? `llegada y órbita de ${NOMBRE_PLANETA[e.planeta]}` : `sobrevuelo de ${NOMBRE_PLANETA[e.planeta]}`, orbita });
  }
  return out;
}
