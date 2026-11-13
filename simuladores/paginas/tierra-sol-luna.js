// SPDX-License-Identifier: Apache-2.0
import { iniciar } from "../motor/app.js";
import { PLANETAS, LUNA, SOL, UA_KM } from "../motor/cuerpos.js";
import { crearAstronomia } from "../motor/astronomia.js";
import { formatoUtc, JD_UTC_INICIO, JD_UTC_FIN, jdTdbDesdeUtc } from "../motor/tiempo.js";

let astro = null;

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
  eventos: ({ sol, sis }) => {
    astro ??= crearAstronomia(sol, sis);
    const j0 = jdTdbDesdeUtc(JD_UTC_INICIO) - 1, j1 = jdTdbDesdeUtc(JD_UTC_FIN) + 1;
    const est = astro.estaciones(j0, j1).map((e) => ({ jdUtc: e.jdUtc, etiqueta: e.nombre }));
    const aps = astro.apsides(j0, j1).map((e) => ({ jdUtc: e.jdUtc, etiqueta: e.nombre, dato: `${e.dist_ua.toFixed(5).replace(".", ",")} UA` }));
    return [
      { titulo: "Equinoccios y solsticios", aviso: "Longitud aparente del Sol 0°, 90°, 180°, 270° (precesión, nutación y aberración incluidas). Contrastado con el U.S. Naval Observatory: ≤ 1 minuto en los 96.", filas: est },
      { titulo: "Perihelio y afelio", aviso: "Extremos de la distancia entre el Sol y el centro de la Tierra. Contrastado con el U.S. Naval Observatory: ≤ 1 minuto en los 48.", filas: aps.sort((a, b) => a.jdUtc - b.jdUtc) },
    ];
  },
  extra: ({ o, geo, reloj, sol, sis, central, solObj, nrm, dot, fmt }) => {
    const out = [];
    astro ??= crearAstronomia(sol, sis);
    if (o.id === "301") {
      const proximas = astro.fases(reloj.jdTdb, reloj.jdTdb + 24).slice(0, 4);
      out.push(["Próximas fases", proximas.map((f) => `${f.nombre.replace("Luna ", "").replace("Cuarto ", "C. ")} ${formatoUtc(f.jdUtc, false).slice(5, 16)}`).join(" · ")]);
    }
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
