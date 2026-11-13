// SPDX-License-Identifier: Apache-2.0
import { iniciarCielo } from "../motor/app-cielo.js";

iniciarCielo({
  clave: "cielo-tierra", id: "399", sistema: "tierra", titulo: "Cielo desde la Tierra", lugarTexto: "Observador en la Tierra",
  fechaInicial: "2027-03-21T01:00", vista: { az: 0, alt: 35, fov: 120 },
  lugares: [["Santiago de Chile", -33.45, -70.67], ["Observatorio Paranal (Chile)", -24.63, -70.40], ["Greenwich", 51.4769, 0], ["Quito (ecuador)", -0.18, -78.5], ["Ciudad de México", 19.43, -99.13], ["Madrid", 40.42, -3.70], ["Tokio", 35.68, 139.69], ["Sídney", -33.87, 151.2], ["Reikiavik", 64.15, -21.94], ["Polo Norte", 90, 0], ["Polo Sur", -90, 0]],
  atmosfera: { dia: [100, 156, 224], crepusculo: [58, 58, 110], extincion: 0.38 }, suelo: [34, 42, 30],
  aviso: "Latitud y longitud geodésicas, nivel del mar. Se aplica la refracción atmosférica estándar (opcional).",
  nota: "Refracción: fórmula de Bennett. Salidas y puestas: borde superior con 34′ de refracción y paralaje (convención del almanaque).",
});
