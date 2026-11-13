// SPDX-License-Identifier: Apache-2.0
import { iniciarCielo } from "../motor/app-cielo.js";

iniciarCielo({
  clave: "cielo-jupiter", id: "599", sistema: "jupiter", titulo: "Cielo desde Júpiter", lugarTexto: "Cima de las nubes de Júpiter",
  fechaInicial: "2027-03-21T00:00", vista: { az: 90, alt: 40, fov: 120 },
  lugares: [["Ecuador (longitud 0°)", 0, 0], ["Latitud 22° S (Gran Mancha Roja)", -22, 0], ["Latitud 45° N", 45, 0], ["Polo norte", 90, 0]],
  atmosfera: null, suelo: [118, 86, 62],
  aviso: "Júpiter no tiene superficie: el observador está sobre las nubes (presión de 1 bar), con el radio ecuatorial IAU y la rotación de su sistema III. El cielo es negro (sin atmósfera por encima).",
  nota: "Sin refracción ni atmósfera. Las lunas muestran su tamaño angular real (Ío ≈ 0,5°, casi el de la Luna vista desde la Tierra); sólo se dibujan las que tienen radio publicado en Horizons.",
});
