// SPDX-License-Identifier: Apache-2.0
import { iniciar } from "../motor/app.js";
import { longitudSolar } from "../motor/cuerpos.js";

const RAD = Math.PI / 180;
const SOL_MARCIANO_D = 1.0274912510; // día solar medio de Marte en días terrestres
const ESTACIONES = [[0, "primavera boreal"], [90, "verano boreal"], [180, "otoño boreal"], [270, "invierno boreal"]];

iniciar({
  clave: "marte", titulo: "Marte y sus dos lunas", planetaId: "499",
  distInicial: 7.5e4, distMax: 6e7, velocidad: 600, paso: 3600,
  ampliaciones: [1, 10, 100, 1000], seleccionInicial: "401", camara: { yaw: -1.0, pitch: 0.9 },
  atajos: ({ vista, central, objetos }) => [
    { texto: "Sistema completo", accion: () => { vista.seguir = central; vista.cam.distObj = 7.5e4; } },
    { texto: "Marte", accion: () => vista.enfocar(central, 1.2e4) },
    { texto: "Fobos", accion: () => vista.enfocar(vista.porId.get("401"), 90) },
    { texto: "Deimos", accion: () => vista.enfocar(vista.porId.get("402"), 60) },
  ],
  extra: ({ o, sol, reloj, central, fmt }) => {
    const out = [];
    const t = sol.cuerpo("499"), jd = reloj.jdTdb;
    if (o.id === "499") {
      const ls = longitudSolar(t.pos(jd), t.vel(jd), central.base.z);
      const est = ESTACIONES.filter(([a]) => a <= ls).pop()[1];
      out.push(["Longitud solar Ls", `${fmt(ls, 1)}° · ${est}`]);
      const sd = central.base.z, s = [-t.pos(jd)[0], -t.pos(jd)[1], -t.pos(jd)[2]], n = Math.hypot(...s);
      out.push(["Declinación del Sol (latitud subsolar)", `${fmt(Math.asin((s[0] * sd[0] + s[1] * sd[1] + s[2] * sd[2]) / n) / RAD, 2)}°`]);
      out.push(["Oblicuidad (polo vs. órbita)", "≈ 25,2° (IAU)"]);
    } else if (o.meta && o.meta.periodo_d) {
      out.push(["Vueltas por día marciano", fmt(SOL_MARCIANO_D / o.meta.periodo_d, 3)]);
      out.push(["Diámetro angular visto desde Marte", `${fmt(2 * Math.asin(o.radio / Math.hypot(...o.pos)) / RAD * 60, 1)}′ (Sol: ${fmt(2 * Math.asin(695700 / Math.hypot(...t.pos(jd))) / RAD * 60, 1)}′)`]);
    }
    return out;
  },
});
