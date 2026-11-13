// SPDX-License-Identifier: Apache-2.0
import { iniciar } from "../motor/app.js";
import { crearAstronomia } from "../motor/astronomia.js";
import { UA_KM, C_KM_S } from "../motor/cuerpos.js";
import { JD_UTC_INICIO, JD_UTC_FIN, jdTdbDesdeUtc } from "../motor/tiempo.js";

const RAD = Math.PI / 180;
const EXTERIORES = [["499", "Marte"], ["599", "Júpiter"], ["699", "Saturno"], ["799", "Urano"], ["899", "Neptuno"]];
let astro = null;

iniciar({
  clave: "sol", titulo: "Sistema Solar", planetaId: null,
  distInicial: 6.5e8, distMax: 2.4e10, velocidad: 86400, paso: 86400, umbralEtiquetas: 40,
  ampliaciones: [1, 100, 1000, 10000], seleccionInicial: "399", camara: { yaw: -1.0, pitch: 0.9 },
  atajos: ({ vista, solObj }) => [
    { texto: "Planetas interiores", accion: () => { vista.seguir = solObj; vista.cam.distObj = 6.5e8; vista.cam.pitch = 0.9; } },
    { texto: "Hasta Júpiter", accion: () => { vista.seguir = solObj; vista.cam.distObj = 2.1e9; vista.cam.pitch = 0.9; } },
    { texto: "Todo el sistema", accion: () => { vista.seguir = solObj; vista.cam.distObj = 1.45e10; vista.cam.pitch = 1.0; } },
    { texto: "Vista lateral", accion: () => { vista.seguir = solObj; vista.cam.distObj = 1.1e10; vista.cam.pitch = 0.04; } },
    { texto: "Sobre la Tierra", accion: () => vista.enfocar(vista.porId.get("399"), 2.5e4) },
    { texto: "Sobre Júpiter", accion: () => vista.enfocar(vista.porId.get("599"), 4.5e5) },
    { texto: "Sobre Saturno", accion: () => vista.enfocar(vista.porId.get("699"), 6.5e5) },
  ],
  eventos: ({ sol, sis }) => {
    astro ??= crearAstronomia(sol, sis);
    const j0 = jdTdbDesdeUtc(JD_UTC_INICIO), j1 = jdTdbDesdeUtc(JD_UTC_FIN);
    return EXTERIORES.map(([id, n]) => ({
      titulo: `Oposiciones de ${n}`,
      aviso: "Instante en que la longitud eclíptica geocéntrica del planeta se opone a la del Sol; se indica la distancia a la Tierra. Calculado de las efemérides de JPL.",
      filas: astro.oposiciones(id, j0, j1).map((o) => ({ jdUtc: o.jdUtc, etiqueta: n, dato: `${o.dist_ua.toFixed(3).replace(".", ",")} UA` })),
    }));
  },
  extra: ({ o, vista, reloj, fmt }) => {
    const out = [];
    const E = vista.porId.get("399").pos;
    if (o.id !== "10" && o.id !== "399" && o.id !== "301") {
      const p = o.pos, rel = [p[0] - E[0], p[1] - E[1], p[2] - E[2]], d = Math.hypot(...rel);
      const toSun = [-E[0], -E[1], -E[2]], dS = Math.hypot(...toSun);
      const elong = Math.acos((rel[0] * toSun[0] + rel[1] * toSun[1] + rel[2] * toSun[2]) / (d * dS)) / RAD;
      const pSun = [-p[0], -p[1], -p[2]], pE = [-rel[0], -rel[1], -rel[2]];
      const cosI = (pSun[0] * pE[0] + pSun[1] * pE[1] + pSun[2] * pE[2]) / (Math.hypot(...pSun) * d);
      out.push(["Distancia a la Tierra", `${fmt(d / UA_KM, 4)} UA · luz ${fmt(d / C_KM_S / 60, 1)} min`]);
      out.push(["Elongación desde la Tierra", `${fmt(elong, 1)}°`]);
      out.push(["Fase (iluminación vista desde la Tierra)", `${fmt((1 + cosI) / 2 * 100, 1)} %`]);
    }
    if (o.id === "399") out.push(["Velocidad orbital", `${fmt(Math.hypot(...o.tabla.vel(reloj.jdTdb)), 3)} km/s`]);
    return out;
  },
});
