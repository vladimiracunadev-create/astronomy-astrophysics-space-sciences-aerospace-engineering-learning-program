// SPDX-License-Identifier: Apache-2.0
import { iniciar } from "../motor/app.js";

const RAD = Math.PI / 180;

iniciar({
  clave: "neptuno", titulo: "Neptuno y sus lunas", planetaId: "899", anillos: true,
  distInicial: 1.2e6, distMax: 3e8, velocidad: 3600, paso: 3600, umbralEtiquetas: 0,
  ampliaciones: [1, 10, 50, 200], seleccionInicial: "801", camara: { yaw: -1.0, pitch: 0.5 },
  atajos: ({ vista, central }) => [
    { texto: "Tritón y lunas internas", accion: () => { vista.seguir = central; vista.cam.distObj = 1.2e6; } },
    { texto: "Anillos y lunas internas", accion: () => { vista.seguir = central; vista.cam.distObj = 3e5; } },
    { texto: "Neptuno", accion: () => vista.enfocar(central, 1.1e5) },
    { texto: "Nereida y lunas lejanas", accion: () => { vista.seguir = central; vista.cam.distObj = 2.6e7; } },
    { texto: "Tritón", accion: () => vista.enfocar(vista.porId.get("801"), 8000) },
    { texto: "Nereida", accion: () => vista.enfocar(vista.porId.get("802"), 2500) },
    { texto: "Proteo", accion: () => vista.enfocar(vista.porId.get("808"), 2500) },
  ],
  extra: ({ o, central, solObj, fmt }) => {
    const out = [];
    if (o.id === "899" && central.base) {
      const d = Math.hypot(...solObj.pos), s = solObj.pos.map((v) => v / d), z = central.base.z;
      out.push(["Latitud subsolar (planetográfica)", `${fmt(Math.asin(s[0] * z[0] + s[1] * z[1] + s[2] * z[2]) / RAD, 2)}°`]);
      out.push(["Inclinación del eje respecto de la órbita", "≈ 28,3° (IAU)"]);
    }
    if (o.id === "801") out.push(["Particularidad", "órbita retrógrada e inclinada ≈ 157°: probablemente un objeto capturado"]);
    return out;
  },
});
