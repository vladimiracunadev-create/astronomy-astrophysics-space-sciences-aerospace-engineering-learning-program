// SPDX-License-Identifier: Apache-2.0
import { iniciar } from "../motor/app.js";

iniciar({
  clave: "pluton", titulo: "Plutón y sus lunas", planetaId: "9", baricentro: "Baricentro Plutón–Caronte",
  distInicial: 2.2e5, distMax: 6e7, velocidad: 3600, paso: 3600, umbralEtiquetas: 0,
  ampliaciones: [1, 10, 50, 200], seleccionInicial: "901", camara: { yaw: -1.0, pitch: 0.6 },
  atajos: ({ vista, central }) => [
    { texto: "Sistema completo", accion: () => { vista.seguir = central; vista.cam.distObj = 2.2e5; } },
    { texto: "Plutón y Caronte", accion: () => { vista.seguir = central; vista.cam.distObj = 6e4; } },
    { texto: "Plutón", accion: () => vista.enfocar(vista.porId.get("999"), 4500) },
    { texto: "Caronte", accion: () => vista.enfocar(vista.porId.get("901"), 2500) },
    { texto: "Hidra", accion: () => vista.enfocar(vista.porId.get("903"), 120) },
  ],
  extra: ({ o }) => {
    const out = [];
    if (o.id === "999") out.push(["Particularidad", "Plutón y Caronte giran en torno a un punto fuera de Plutón (≈ 2 100 km de su centro) y se miran siempre la misma cara"]);
    if (["902", "903", "904", "905"].includes(o.id)) out.push(["Particularidad", "órbita casi circular y coplanar, con resonancias cercanas con Caronte; rotación caótica"]);
    return out;
  },
});
