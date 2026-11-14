// SPDX-License-Identifier: Apache-2.0
// Lista única de simuladores (la usan el concentrador y la barra de navegación de cada página).
export const SIMULADORES = [
  { clave: "sol", imagen: "sistema-solar", href: "sistema-solar.html", titulo: "Sistema Solar", resumen: "Sol, ocho planetas, Plutón y Ceres con posiciones heliocéntricas oficiales de JPL (2027–2050)." },
  { clave: "tierra", imagen: "tierra", href: "tierra-sol-luna.html", titulo: "Tierra · Sol · Luna", resumen: "Fases, distancia y tamaños angulares, iluminación y eclipses calculados desde las efemérides." },
  { clave: "marte", imagen: "marte", href: "marte.html", titulo: "Marte y sus dos lunas", resumen: "Fobos y Deimos alrededor de Marte, con órbitas, sombras y tamaños reales." },
  { clave: "jupiter", imagen: "jupiter", href: "jupiter.html", titulo: "Júpiter y sus lunas", resumen: "Las lunas jovianas con efemérides (Io, Europa, Ganimedes, Calisto y el resto), anillos y eclipses por el planeta." },
  { clave: "saturno", imagen: "saturno", href: "saturno.html", titulo: "Saturno y sus lunas", resumen: "Titán, Encélado y las demás lunas, más los anillos a escala." },
  { clave: "urano", imagen: "urano", href: "urano.html", titulo: "Urano y sus lunas", resumen: "Un sistema tumbado: ejes casi en el plano orbital, lunas mayores y menores, y anillos." },
  { clave: "neptuno", imagen: "neptuno", href: "neptuno.html", titulo: "Neptuno y sus lunas", resumen: "Tritón retrógrada, Nereida excéntrica y las lunas internas." },
  { clave: "pluton", imagen: "pluton", href: "pluton.html", titulo: "Plutón y sus lunas", resumen: "Plutón, Caronte, Estigia, Nix, Cerbero e Hidra girando en torno a un baricentro exterior a Plutón." },
  { clave: "cielo-tierra", imagen: "cielo-tierra", href: "cielo-tierra.html", titulo: "Cielo desde la Tierra", resumen: "Sol, Luna, planetas y 5.000 estrellas desde cualquier lugar, con salidas y puestas validadas con el U.S. Naval Observatory." },
  { clave: "cielo-marte", imagen: "cielo-marte", href: "cielo-marte.html", titulo: "Cielo desde Marte", resumen: "Fobos y Deimos cruzando el cielo, el Sol de 21′, la Tierra como una estrella y los planetas." },
  { clave: "cielo-jupiter", imagen: "cielo-jupiter", href: "cielo-jupiter.html", titulo: "Cielo desde Júpiter", resumen: "Desde la cima de las nubes: las lunas galileanas como discos, los planetas y las estrellas." },
  { clave: "cielo-saturno", imagen: "cielo-saturno", href: "cielo-saturno.html", titulo: "Cielo desde Saturno", resumen: "Los anillos como un arco inmenso, Titán y las demás lunas, los planetas y las estrellas." },
  { clave: "cielo-europa", imagen: "cielo-europa", href: "cielo-europa.html", titulo: "Cielo desde Europa", resumen: "Júpiter como un disco de 12° con fases, el Sol que sale cada 3,55 días y las demás lunas galileanas." },
  { clave: "cielo-titania", imagen: "cielo-titania", href: "cielo-titania.html", titulo: "Cielo desde Titania", resumen: "Urano como un disco de casi 7° fijo en el cielo, con fases, y el Sol que sale cada 8,7 días." },
  { clave: "trayectorias", imagen: "trayectorias", href: "trayectorias.html", titulo: "Trayectorias entre planetas", resumen: "Gráfico porkchop, problema de Lambert, C3, v∞ y delta-v entre dos planetas con posiciones oficiales de JPL." },
  { clave: "eclipses-solares", imagen: "eclipses-solares", href: "eclipses-solares.html", titulo: "Eclipses solares", resumen: "Franja de totalidad y anularidad de los 54 eclipses solares de 2027–2050 sobre un mapa y circunstancias locales, validadas con la NASA." },
  { clave: "misiones", imagen: "misiones", href: "misiones.html", titulo: "Misiones espaciales", resumen: "Voyager 1 y 2, Pioneer 10 y 11, Galileo, Cassini, New Horizons, Juno, James Webb y más: elige una misión y recorre su trayectoria real con fechas y acercamientos." },
  { clave: "asteroides", imagen: "asteroides", href: "asteroides.html", titulo: "Cinturón de asteroides", resumen: "1.674 asteroides (cinturón principal, troyanos, Hildas y cercanos a la Tierra) con elementos del JPL y el error de la aproximación medido." },
];

export function barraNavegacion(actual) {
  const nav = document.createElement("nav");
  nav.setAttribute("aria-label", "Simuladores");
  nav.innerHTML = `<a href="index.html">Inicio</a>` + SIMULADORES.map((s) => `<a href="${s.href}"${s.clave === actual ? ' aria-current="page"' : ""}>${s.titulo}</a>`).join("");
  return nav;
}
