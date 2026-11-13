// SPDX-License-Identifier: Apache-2.0
import { iniciarCielo } from "../motor/app-cielo.js";

iniciarCielo({
  clave: "cielo-europa", id: "599", sistema: "jupiter", luna: "502", titulo: "Cielo desde Europa", lugarTexto: "Superficie de Europa",
  fechaInicial: "2027-03-21T00:00", velocidad: 3600, vista: { az: 270, alt: 45, fov: 100 }, mirarPlaneta: true,
  lugares: [["Hemisferio que mira al planeta (lat 20°, lon 30°)", 20, 30], ["Punto subplanetario (el planeta en el cénit)", 0, 0], ["Hemisferio delantero (lon 90° E)", 0, 90], ["Punto antiplanetario (el planeta nunca se ve)", 0, 180], ["Hemisferio trasero (lon 270°)", 0, 270], ["Polo norte", 90, 0], ["Polo sur", -90, 0]],
  atmosfera: null, suelo: [150, 150, 158],
  aviso: "Europa gira en 3,55 días y siempre muestra la misma cara a Júpiter: desde el hemisferio que lo mira, Júpiter está fijo en el cielo (≈ 12° de diámetro, 23 veces la Luna llena), con fases como la Luna, y el Sol sale y se pone cada 3,55 días.",
  nota: "Sin atmósfera apreciable. Europa se modela como una esfera de 1 560,8 km con rotación síncrona (sin libración ni inclinación del eje). Las demás lunas galileanas se ven con su tamaño angular real; Júpiter, como un disco liso con su fase.",
});
