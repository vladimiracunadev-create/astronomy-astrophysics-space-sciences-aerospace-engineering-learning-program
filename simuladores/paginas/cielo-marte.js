// SPDX-License-Identifier: Apache-2.0
import { iniciarCielo } from "../motor/app-cielo.js";

iniciarCielo({
  clave: "cielo-marte", id: "499", sistema: "marte", titulo: "Cielo desde Marte", lugarTexto: "Observador en Marte",
  fechaInicial: "2027-03-21T13:00", vista: { az: 90, alt: 25, fov: 120 },
  lugares: [["Cráter Jezero (Perseverance)", 18.44, 77.45], ["Cráter Gale (Curiosity)", -5.4, 137.8], ["Elysium Planitia (InSight)", 4.5, 135.6], ["Valles Marineris", -13.9, -59], ["Monte Olimpo", 18.65, -133.8], ["Polo norte", 90, 0], ["Polo sur", -90, 0]],
  atmosfera: { dia: [201, 162, 122], crepusculo: [70, 84, 118], extincion: 0.2 }, suelo: [96, 60, 42],
  aviso: "Latitud planetográfica y longitud este (marco IAU). Se muestra el color del cielo marciano de forma ilustrativa: ocre de día y azulado en el crepúsculo.",
  nota: "Sin refracción. El Sol mide 21′ (≈ 2/3 del tamaño visto desde la Tierra). Fobos y Deimos con su tamaño angular real; magnitudes de las lunas con albedo medio 0,25.",
});
