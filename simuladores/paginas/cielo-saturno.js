// SPDX-License-Identifier: Apache-2.0
import { iniciarCielo } from "../motor/app-cielo.js";

iniciarCielo({
  clave: "cielo-saturno", id: "699", sistema: "saturno", titulo: "Cielo desde Saturno", lugarTexto: "Cima de las nubes de Saturno",
  fechaInicial: "2027-03-21T00:00", vista: { az: 180, alt: 45, fov: 130 },
  lugares: [["Ecuador (anillos de canto)", 0, 0], ["Latitud 30° N", 30, 0], ["Latitud 30° S", -30, 0], ["Latitud 60° N", 60, 0], ["Polo norte", 90, 0]],
  atmosfera: null, suelo: [150, 126, 86],
  aviso: "Saturno no tiene superficie: el observador está sobre las nubes (1 bar), con el radio ecuatorial IAU y la rotación de su sistema III. Los anillos (C, B, A y F) se dibujan con sus radios publicados y opacidad ilustrativa.",
  nota: "Sin refracción ni atmósfera. Las lunas muestran su tamaño angular real; sólo se dibujan las que tienen radio publicado en Horizons.",
});
