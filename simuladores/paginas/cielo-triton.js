// SPDX-License-Identifier: Apache-2.0
import { iniciarCielo } from "../motor/app-cielo.js";

iniciarCielo({
  clave: "cielo-triton", id: "899", sistema: "neptuno", luna: "801", titulo: "Cielo desde Tritón", lugarTexto: "Superficie de Tritón",
  fechaInicial: "2027-03-21T00:00", velocidad: 3600, vista: { az: 270, alt: 45, fov: 100 }, mirarPlaneta: true,
  lugares: [["Hemisferio que mira al planeta (lat 20°, lon 30°)", 20, 30], ["Punto subplanetario (el planeta en el cénit)", 0, 0], ["Hemisferio delantero (lon 90° E)", 0, 90], ["Punto antiplanetario (el planeta nunca se ve)", 0, 180], ["Hemisferio trasero (lon 270°)", 0, 270], ["Polo norte", 90, 0], ["Polo sur", -90, 0]],
  atmosfera: null, suelo: [150, 150, 158],
  aviso: "Tritón gira en 5,88 días con la misma cara hacia Neptuno y orbita al revés que el planeta (órbita retrógrada e inclinada ≈ 157°). Desde el hemisferio que lo mira, Neptuno (≈ 8° de diámetro) está fijo en el cielo. Tritón tiene una atmósfera muy tenue que no se modela.",
  nota: "Sin atmósfera apreciable. Tritón se modela como una esfera de 1 352,6 km con rotación síncrona; su eje se toma normal a la órbita.",
});
