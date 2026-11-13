// SPDX-License-Identifier: Apache-2.0
import { iniciar } from "../motor/app.js";
import { PLANETAS, LUNA, SOL, UA_KM } from "../motor/cuerpos.js";

const RAD = Math.PI / 180;
const nombreFase = (d) => {
  const g = ((d % 360) + 360) % 360;
  const n = [[0, "Luna nueva"], [45, "Creciente"], [90, "Cuarto creciente"], [135, "Gibosa creciente"], [180, "Luna llena"], [225, "Gibosa menguante"], [270, "Cuarto menguante"], [315, "Menguante"], [360, "Luna nueva"]];
  let mejor = n[0];
  for (const x of n) if (Math.abs(g - x[0]) < Math.abs(g - mejor[0])) mejor = x;
  return mejor[1];
};

iniciar({
  clave: "tierra", titulo: "Tierra · Sol · Luna", planetaId: "399",
  distInicial: 1.35e6, distMax: 4e8, velocidad: 3600, paso: 86400,
  ampliaciones: [1, 5, 20], eclipses: true, seleccionInicial: "301", umbralEtiquetas: 0,
  camara: { yaw: -1.1, pitch: 0.8 },
  atajos: ({ vista, central, objetos }) => [
    { texto: "Sistema Tierra–Luna", accion: () => { vista.seguir = central; vista.cam.distObj = 1.35e6; } },
    { texto: "Solo la Tierra", accion: () => vista.enfocar(central, 4e4) },
    { texto: "Sólo la Luna", accion: () => vista.enfocar(vista.porId.get("301"), 9e3) },
    { texto: "Desde sobre el Sol", accion: () => { vista.seguir = central; vista.cam.pitch = 1.5; vista.cam.distObj = 8e5; } },
  ],
  extra: ({ o, geo, reloj, central, solObj, nrm, dot, fmt }) => {
    const out = [];
    const sd = solObj.pos, sn = nrm(sd);
    if (o.id === "301") {
      const m = o.pos, d = nrm(m);
      const dl = geo.dl(reloj.jdTdb) / RAD;
      const elong = Math.acos(dot(m, sd) / (d * sn)) / RAD;
      out.push(["Fase", `${nombreFase(dl)} (Δλ ${fmt(((dl % 360) + 360) % 360, 1)}°)`]);
      out.push(["Elongación Sol–Tierra–Luna", `${fmt(elong, 1)}°`]);
      out.push(["Diámetro angular", `Luna ${fmt(2 * Math.asin(LUNA.radio / d) / RAD * 60, 2)}′ · Sol ${fmt(2 * Math.asin(SOL.radio / sn) / RAD * 60, 2)}′`]);
      out.push(["Distancia", d < 367000 ? "cerca del perigeo" : d > 400000 ? "cerca del apogeo" : "intermedia"]);
    }
    if (o.id === "399" && central.base) {
      const s = [sd[0] / sn, sd[1] / sn, sd[2] / sn], b = central.base;
      const x = dot(s, b.x), y = dot(s, b.y), z = dot(s, b.z);
      out.push(["Punto subsolar", `${fmt(Math.asin(z) / RAD, 2)}° lat · ${fmt(Math.atan2(y, x) / RAD, 2)}° lon`]);
    }
    return out;
  },
});
