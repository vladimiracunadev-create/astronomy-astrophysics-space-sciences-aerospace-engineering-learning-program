// SPDX-License-Identifier: Apache-2.0
import { iniciarCielo } from "../motor/app-cielo.js";

iniciarCielo({
  clave: "cielo-titania", id: "799", sistema: "urano", luna: "703", titulo: "Cielo desde Titania", lugarTexto: "Superficie de Titania",
  fechaInicial: "2027-03-21T00:00", velocidad: 3600, vista: { az: 270, alt: 45, fov: 100 }, mirarPlaneta: true,
  lugares: [["Hemisferio que mira al planeta (lat 20°, lon 30°)", 20, 30], ["Punto subplanetario (el planeta en el cénit)", 0, 0], ["Hemisferio delantero (lon 90° E)", 0, 90], ["Punto antiplanetario (el planeta nunca se ve)", 0, 180], ["Hemisferio trasero (lon 270°)", 0, 270], ["Polo norte", 90, 0], ["Polo sur", -90, 0]],
  atmosfera: null, suelo: [150, 150, 158],
  aviso: "Titania gira en 8,7 días con la misma cara hacia Urano. Desde el hemisferio que lo mira, Urano (≈ 7° de diámetro) está fijo en el cielo; sus anillos son finos y casi invisibles desde esta distancia. El Sol sale y se pone cada 8,7 días.",
  nota: "Sin atmósfera apreciable. Titania se modela como una esfera de 788,9 km con rotación síncrona. Los anillos de Urano no se dibujan desde esta posición (son muy tenues).",
});
