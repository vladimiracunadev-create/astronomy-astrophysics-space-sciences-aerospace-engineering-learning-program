// SPDX-License-Identifier: Apache-2.0
// Lista única de simuladores (la usan el concentrador y la barra de navegación de cada página).
export const SIMULADORES = [
  { clave: "tierra", href: "tierra-sol-luna.html", titulo: "Tierra · Sol · Luna", resumen: "Fases, distancia y tamaños angulares, iluminación y eclipses calculados desde las efemérides." },
  { clave: "marte", href: "marte.html", titulo: "Marte y sus dos lunas", resumen: "Fobos y Deimos alrededor de Marte, con órbitas, sombras y tamaños reales." },
  { clave: "jupiter", href: "jupiter.html", titulo: "Júpiter y sus lunas", resumen: "Las lunas jovianas con efemérides (Io, Europa, Ganimedes, Calisto y el resto), anillos y eclipses por el planeta." },
  { clave: "saturno", href: "saturno.html", titulo: "Saturno y sus lunas", resumen: "Titán, Encélado y las demás lunas, más los anillos a escala." },
  { clave: "urano", href: "urano.html", titulo: "Urano y sus lunas", resumen: "Un sistema tumbado: ejes casi en el plano orbital, lunas mayores y menores, y anillos." },
];

export function barraNavegacion(actual) {
  const nav = document.createElement("nav");
  nav.setAttribute("aria-label", "Simuladores");
  nav.innerHTML = `<a href="index.html">Inicio</a>` + SIMULADORES.map((s) => `<a href="${s.href}"${s.clave === actual ? ' aria-current="page"' : ""}>${s.titulo}</a>`).join("");
  return nav;
}
