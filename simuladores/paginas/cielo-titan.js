// SPDX-License-Identifier: Apache-2.0
import { iniciarCielo } from "../motor/app-cielo.js";

iniciarCielo({
  clave: "cielo-titan", id: "699", sistema: "saturno", luna: "606", titulo: "Cielo desde Titán", lugarTexto: "Superficie de Titán",
  fechaInicial: "2027-03-21T00:00", velocidad: 3600, vista: { az: 270, alt: 45, fov: 100 }, mirarPlaneta: true,
  lugares: [["Hemisferio que mira al planeta (lat 20°, lon 30°)", 20, 30], ["Punto subplanetario (el planeta en el cénit)", 0, 0], ["Hemisferio delantero (lon 90° E)", 0, 90], ["Punto antiplanetario (el planeta nunca se ve)", 0, 180], ["Hemisferio trasero (lon 270°)", 0, 270], ["Polo norte", 90, 0], ["Polo sur", -90, 0]],
  atmosfera: null, suelo: [150, 150, 158],
  aviso: "Titán gira en 15,9 días con la misma cara hacia Saturno. Desde el hemisferio que lo mira, Saturno (≈ 5° de diámetro) está fijo en el cielo; los anillos se ven casi de canto, como una línea fina. El Sol sale y se pone cada 15,9 días.",
  nota: "La atmósfera real de Titán es opaca (bruma anaranjada que oculta el cielo desde la superficie): aquí se muestra el cielo como se vería sin ella, p. ej. sobre la bruma. Titán se modela como una esfera de 2 574,7 km con rotación síncrona. Los anillos se dibujan como desde cualquier lugar del sistema.",
});
