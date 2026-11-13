// SPDX-License-Identifier: Apache-2.0
import { iniciar } from "../motor/app.js";

const GALILEANAS = ["501", "502", "503", "504"];

iniciar({
  clave: "jupiter", titulo: "Júpiter y sus lunas", planetaId: "599", anillos: true,
  distInicial: 3.4e6, distMax: 1.5e8, velocidad: 3600, paso: 3600, umbralEtiquetas: 40,
  ampliaciones: [1, 10, 50, 200], seleccionInicial: "501", camara: { yaw: -1.0, pitch: 0.6 },
  atajos: ({ vista, central }) => [
    { texto: "Sistema galileano", accion: () => { vista.seguir = central; vista.cam.distObj = 3.4e6; } },
    { texto: "Lunas internas y anillos", accion: () => { vista.seguir = central; vista.cam.distObj = 8e5; } },
    { texto: "Júpiter", accion: () => vista.enfocar(central, 4.2e5) },
    { texto: "Toda la familia de lunas", accion: () => { vista.seguir = central; vista.cam.distObj = 6e7; } },
    ...GALILEANAS.map((id) => ({ texto: { 501: "Ío", 502: "Europa", 503: "Ganimedes", 504: "Calisto" }[id], accion: () => vista.enfocar(vista.porId.get(id), 9000) })),
  ],
  extra: ({ o, fmt }) => {
    const out = [];
    if (o.id === "599") out.push(["Rotación (sistema III)", "9 h 55,5 min (IAU)"]);
    if (GALILEANAS.includes(o.id) && o.meta) out.push(["Resonancia de Laplace", "Ío : Europa : Ganimedes = 4 : 2 : 1 en periodo"]);
    return out;
  },
});
