// SPDX-License-Identifier: Apache-2.0
import { iniciar } from "../motor/app.js";

const RAD = Math.PI / 180;
const NOMBRES = { 701: "Ariel", 702: "Umbriel", 703: "Titania", 704: "Oberón", 705: "Miranda" };

iniciar({
  clave: "urano", titulo: "Urano y sus lunas", planetaId: "799", anillos: true,
  distInicial: 1.7e6, distMax: 1.5e8, velocidad: 3600, paso: 3600, umbralEtiquetas: 8,
  ampliaciones: [1, 10, 50, 200], seleccionInicial: "703", camara: { yaw: -1.0, pitch: 0.5 },
  atajos: ({ vista, central }) => [
    { texto: "Sistema completo", accion: () => { vista.seguir = central; vista.cam.distObj = 1.7e6; } },
    { texto: "Anillos y lunas internas", accion: () => { vista.seguir = central; vista.cam.distObj = 2.6e5; } },
    { texto: "Urano", accion: () => vista.enfocar(central, 1.2e5) },
    { texto: "Toda la familia de lunas", accion: () => { vista.seguir = central; vista.cam.distObj = 4e7; } },
    ...Object.entries(NOMBRES).map(([id, n]) => ({ texto: n, accion: () => vista.enfocar(vista.porId.get(id), 3000) })),
  ],
  extra: ({ o, central, solObj, fmt }) => {
    const out = [];
    if (o.id === "799" && central.base) {
      const d = Math.hypot(...solObj.pos), s = solObj.pos.map((v) => v / d), z = central.base.z;
      const lat = Math.asin(s[0] * z[0] + s[1] * z[1] + s[2] * z[2]) / RAD;
      out.push(["Latitud subsolar (planetográfica)", `${fmt(lat, 2)}° (${lat >= 0 ? "hemisferio norte IAU" : "hemisferio sur IAU"} iluminado)`]);
      out.push(["Inclinación del eje respecto de la órbita", "≈ 97,8° (IAU): rota «de lado» y en sentido retrógrado"]);
    }
    return out;
  },
});
