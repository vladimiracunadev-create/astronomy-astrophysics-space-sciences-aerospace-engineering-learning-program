// SPDX-License-Identifier: Apache-2.0
import { iniciar } from "../motor/app.js";

const RAD = Math.PI / 180;
const NOMBRES = { 601: "Mimas", 602: "Encélado", 603: "Tetis", 604: "Dione", 605: "Rea", 606: "Titán", 607: "Hiperión", 608: "Jápeto", 609: "Febe" };

iniciar({
  clave: "saturno", titulo: "Saturno y sus lunas", planetaId: "699", anillos: true,
  distInicial: 4.2e6, distMax: 3e8, velocidad: 3600, paso: 3600, umbralEtiquetas: 60,
  ampliaciones: [1, 10, 50, 200], seleccionInicial: "606", camara: { yaw: -1.0, pitch: 0.45 },
  atajos: ({ vista, central }) => [
    { texto: "Sistema de Titán", accion: () => { vista.seguir = central; vista.cam.distObj = 4.2e6; } },
    { texto: "Anillos y lunas internas", accion: () => { vista.seguir = central; vista.cam.distObj = 9e5; } },
    { texto: "Saturno", accion: () => vista.enfocar(central, 4e5) },
    { texto: "Toda la familia de lunas", accion: () => { vista.seguir = central; vista.cam.distObj = 7e7; } },
    ...Object.entries(NOMBRES).filter(([id]) => ["602", "606", "608"].includes(id)).map(([id, n]) => ({ texto: n, accion: () => vista.enfocar(vista.porId.get(id), 9000) })),
  ],
  extra: ({ o, central, solObj, fmt }) => {
    const out = [];
    if (o.id === "699" && central.base) {
      const d = Math.hypot(...solObj.pos), s = solObj.pos.map((v) => v / d), z = central.base.z;
      const elev = Math.asin(s[0] * z[0] + s[1] * z[1] + s[2] * z[2]) / RAD;
      out.push(["Elevación del Sol sobre los anillos", `${fmt(elev, 2)}° (${elev >= 0 ? "cara norte" : "cara sur"} iluminada)`]);
      out.push(["Inclinación del eje respecto de la órbita", "≈ 26,7° (IAU)"]);
    }
    return out;
  },
});
