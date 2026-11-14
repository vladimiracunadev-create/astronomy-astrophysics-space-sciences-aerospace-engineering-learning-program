// SPDX-License-Identifier: Apache-2.0
// Misiones espaciales ya realizadas: trayectorias heliocéntricas reconstruidas por JPL (SPICE, vía Horizons), los planetas 1970–2050 y los
// ENCUENTROS (sobrevuelos, asistencias gravitatorias e inserciones en órbita) con su geometría planetocéntrica de alta resolución
// (datos/encuentros.json, generado con herramientas/efemerides/generar_encuentros.py). Nada de esto se teclea a mano.
// Las trayectorias posteriores a la fecha de descarga (13-nov-2026) son PREDICCIONES de JPL.
import { UA_KM } from "./cuerpos.js";

export const GRUPOS = ["Planetas exteriores", "Mercurio, Venus y el Sol", "Marte, asteroides y cometas", "Telescopios"];
export const MISIONES = {
  "-23": { nombre: "Pioneer 10", grupo: 0, anio: "1972", color: "#ffb454", resumen: "Primera nave en cruzar el cinturón de asteroides y en visitar Júpiter (1973). Su última señal llegó en 2003; la trayectoria posterior es una extrapolación.", sinContacto: "2003-01-23" },
  "-24": { nombre: "Pioneer 11", grupo: 0, anio: "1973", color: "#ffd166", resumen: "Visitó Júpiter (1974) y fue la primera nave en llegar a Saturno (1979). Sin contacto desde 1995; la trayectoria posterior es una extrapolación.", sinContacto: "1995-11-24" },
  "-31": { nombre: "Voyager 1", grupo: 0, anio: "1977", color: "#6cb4ff", resumen: "Sobrevoló Júpiter (1979) y Saturno (1980) y es el objeto humano más lejano: cruzó la heliopausa en 2012.", hitos: [["Cruza la heliopausa", "2012-08-25", 121]] },
  "-32": { nombre: "Voyager 2", grupo: 0, anio: "1977", color: "#7ee0a1", resumen: "La única nave que ha visitado los cuatro planetas gigantes: Júpiter (1979), Saturno (1981), Urano (1986) y Neptuno (1989). Cruzó la heliopausa en 2018.", hitos: [["Cruza la heliopausa", "2018-11-05", 119]] },
  "-77": { nombre: "Galileo", grupo: 0, anio: "1989", color: "#f78fb3", resumen: "Primer orbitador de Júpiter (1995–2003): una asistencia de Venus y dos de la Tierra para llegar; lanzó una sonda a la atmósfera y estudió las lunas. Terminó hundiéndose en Júpiter." },
  "-55": { nombre: "Ulysses", grupo: 0, anio: "1990", color: "#9ad0ff", resumen: "Usó la asistencia de Júpiter (1992) para salir del plano de la eclíptica y fue la primera nave en sobrevolar los polos del Sol (1994–2009)." },
  "-82": { nombre: "Cassini", grupo: 0, anio: "1997", color: "#c3a6ff", resumen: "Orbitó Saturno de 2004 a 2017 y llevó la sonda Huygens a Titán. Cuatro asistencias gravitatorias: Venus dos veces, la Tierra y Júpiter." },
  "-98": { nombre: "New Horizons", grupo: 0, anio: "2006", color: "#ff7a7a", resumen: "Primer sobrevuelo de Plutón (2015), tras la asistencia de Júpiter (2007); después visitó Arrokoth (2019)." },
  "-61": { nombre: "Juno", grupo: 0, anio: "2011", color: "#ffe08a", resumen: "Orbitador polar de Júpiter desde 2016, tras una asistencia de la Tierra (2013). Trayectoria posterior a 2026: predicción de JPL." },
  "-159": { nombre: "Europa Clipper", grupo: 0, anio: "2024", color: "#ffd1a1", resumen: "Misión a la luna Europa de Júpiter: asistencias de Marte (2025) y de la Tierra (2026) y llegada a Júpiter en 2030. Trayectoria posterior a 2026: predicción de JPL." },
  "-236": { nombre: "MESSENGER", grupo: 1, anio: "2004", color: "#c9b6a6", resumen: "Primera nave en orbitar Mercurio (2011–2015). Para frenar usó la Tierra (2005), Venus (dos veces) y tres sobrevuelos de Mercurio." },
  "-121": { nombre: "BepiColombo", grupo: 1, anio: "2018", color: "#e6a06c", resumen: "Misión de ESA y JAXA a Mercurio: una asistencia de la Tierra, dos de Venus y seis sobrevuelos de Mercurio antes de su inserción en órbita (2026). Trayectoria posterior a 2026: predicción de JPL." },
  "-96": { nombre: "Parker Solar Probe", grupo: 1, anio: "2018", color: "#ff9f43", resumen: "Se acerca al Sol más que ninguna otra nave, con asistencias gravitatorias de Venus que reducen su órbita. Trayectoria posterior a 2026: predicción de JPL." },
  "-144": { nombre: "Solar Orbiter", grupo: 1, anio: "2020", color: "#7bd88f", resumen: "Misión de ESA y NASA que usa la Tierra y ocho asistencias de Venus para inclinar su órbita y observar los polos del Sol. Trayectoria posterior a 2026: predicción de JPL." },
  "-226": { nombre: "Rosetta", grupo: 2, anio: "2004", color: "#d9a0ff", resumen: "Misión de ESA que orbitó el cometa 67P/Churyumov–Gerasimenko (2014–2016). Tres asistencias de la Tierra y una de Marte." },
  "-203": { nombre: "Dawn", grupo: 2, anio: "2007", color: "#ffc4a0", resumen: "Orbitó los asteroides Vesta y Ceres. Una asistencia de Marte (2009). Los datos se cortan en el fin de la misión (2018).", fin: "2018-11-01" },
  "-64": { nombre: "OSIRIS-REx", grupo: 2, anio: "2016", color: "#8fe3d2", resumen: "Tomó una muestra del asteroide Bennu y la devolvió a la Tierra (2023); la nave continúa como OSIRIS-APEX hacia Apophis. Trayectoria posterior a 2026: predicción de JPL." },
  "-37": { nombre: "Hayabusa2", grupo: 2, anio: "2014", color: "#a9ff9f", resumen: "Misión japonesa al asteroide Ryugu: asistencia de la Tierra (2015) y devolución de la muestra (2020); sigue hacia otros asteroides. Trayectoria posterior a 2026: predicción de JPL." },
  "-49": { nombre: "Lucy", grupo: 2, anio: "2021", color: "#ffdf6e", resumen: "Visita a los asteroides troyanos de Júpiter con tres asistencias de la Tierra (2022, 2024 y 2030). Trayectoria posterior a 2026: predicción de JPL." },
  "-255": { nombre: "Psyche", grupo: 2, anio: "2023", color: "#b8c0ff", resumen: "Viaja al asteroide metálico (16) Psyche con una asistencia de Marte (2026). Trayectoria posterior a 2026: predicción de JPL." },
  "-202": { nombre: "MAVEN", grupo: 2, anio: "2013", color: "#ff8a6c", resumen: "Orbitador de la atmósfera de Marte desde 2014; sus datos llegan hasta 2026." },
  "-170": { nombre: "James Webb", grupo: 3, anio: "2021", color: "#4dd2ff", resumen: "Telescopio espacial infrarrojo en el punto L2 Sol–Tierra, a unos 1,5 millones de km de la Tierra, siempre en el lado opuesto al Sol." },
};
export const NOMBRE_PLANETA = { "199": "Mercurio", "299": "Venus", "399": "Tierra", "499": "Marte", "599": "Júpiter", "699": "Saturno", "799": "Urano", "899": "Neptuno", "9": "Plutón" };
export const COLOR_PLANETA = { "199": "#b8b0a8", "299": "#f0d9a0", "399": "#5a9bf0", "499": "#d9673f", "599": "#e8c18a", "699": "#ead7a2", "799": "#9be1e8", "899": "#5b7dff", "9": "#cdb9a6" };

/** Hermite cúbico por tramos: posición (km) de la nave respecto del planeta en el instante `dt` (días desde el mayor acercamiento). */
export function posicionPlanetocentrica(tr, dt, out = [0, 0, 0]) {
  const n = tr.length;
  if (dt <= tr[0][0]) { for (let k = 0; k < 3; k++) out[k] = tr[0][1 + k]; return out; }
  if (dt >= tr[n - 1][0]) { for (let k = 0; k < 3; k++) out[k] = tr[n - 1][1 + k]; return out; }
  let lo = 0, hi = n - 1;
  while (hi - lo > 1) { const m = (lo + hi) >> 1; if (tr[m][0] <= dt) lo = m; else hi = m; }
  const a = tr[lo], b = tr[hi], h = (b[0] - a[0]) * 86400, u = (dt - a[0]) / (b[0] - a[0]);
  const h00 = 2 * u ** 3 - 3 * u * u + 1, h10 = u ** 3 - 2 * u * u + u, h01 = -2 * u ** 3 + 3 * u * u, h11 = u ** 3 - u * u;
  for (let k = 0; k < 3; k++) out[k] = h00 * a[1 + k] + h10 * h * a[4 + k] + h01 * b[1 + k] + h11 * h * b[4 + k];
  return out;
}

/**
 * Nave con precisión de encuentro: lejos de los planetas usa la tabla heliocéntrica de JPL (paso de 1 a 3 días) y, dentro de cada sobrevuelo
 * (de entrar a salir de la esfera de influencia), la posición del planeta más la trayectoria planetocéntrica de alta resolución.
 */
export function crearNave(id, tabla, encuentros, planetas) {
  const lista = encuentros.filter((e) => e.nave === id).map((e) => ({ e, ini: e.jd_ca + e.traza[0][0], fin: e.jd_ca + e.traza[e.traza.length - 1][0], tp: planetas.get(e.planeta) })).filter((x) => x.tp);
  const tmp = [0, 0, 0], rel = [0, 0, 0];
  function enEncuentro(jd) { for (const x of lista) if (jd >= x.ini && jd <= x.fin) return x; return null; }
  function pos(jd, out = [0, 0, 0]) {
    const x = enEncuentro(jd);
    if (!x) return tabla.pos(jd, out);
    x.tp.pos(jd, tmp); posicionPlanetocentrica(x.e.traza, jd - x.e.jd_ca, rel);
    out[0] = tmp[0] + rel[0]; out[1] = tmp[1] + rel[1]; out[2] = tmp[2] + rel[2]; return out;
  }
  const a = [0, 0, 0], b = [0, 0, 0];
  function vel(jd, out = [0, 0, 0]) {
    const dt = 2e-4, k = 1 / (2 * dt * 86400); pos(jd - dt, a); pos(jd + dt, b);
    out[0] = (b[0] - a[0]) * k; out[1] = (b[1] - a[1]) * k; out[2] = (b[2] - a[2]) * k; return out;
  }
  return { id, tabla, encuentros: lista.map((x) => x.e), pos, vel, ini: tabla.meta.jd_valido_ini, fin: tabla.meta.jd_valido_fin, enEncuentro };
}

/** Velocidad relativa y distancia respecto del planeta de un encuentro en el instante `jd` (planetocéntrica). */
export function estadoEncuentro(e, jd) {
  const r = posicionPlanetocentrica(e.traza, jd - e.jd_ca), d = Math.hypot(r[0], r[1], r[2]);
  return { r, dist_km: d, alt_km: d - (e.radio || 0) };
}
export const kmAUa = (km) => km / UA_KM;
