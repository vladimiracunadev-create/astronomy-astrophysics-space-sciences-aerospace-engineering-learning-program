# Simulador del cielo desde Europa

[▶ Abrir el simulador](https://vladimiracunadev-create.github.io/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program/simuladores/cielo-europa.html) · [Guía de uso](GUIA_DE_USO.md) · [Datos y efemérides](DATOS_Y_EFEMERIDES.md) · [Fuentes y modelos](FUENTES_Y_MODELOS.md)

![Cielo completo visto desde la superficie de Europa, con Júpiter](../img/cielo-europa.svg)

## Qué muestra

El cielo desde la **superficie de Europa**, la luna helada de Júpiter, en cualquier lugar (7 predefinidos). Europa gira en 3,55 días y siempre muestra la misma cara a Júpiter: desde el hemisferio que lo mira, **Júpiter queda casi fijo en el cielo**, con un diámetro angular de ≈ 12° (unas 23 veces la Luna llena vista desde la Tierra) y con **fases** como las de la Luna. El Sol sale y se pone cada 3,55 días, y las otras lunas galileanas (Ío, Ganímedes, Calisto) cruzan el cielo; el resto de planetas y las estrellas completan la vista. En el hemisferio opuesto Júpiter nunca sale.

## Cómo funciona

1. **Observador sobre una luna:** el sistema de referencia de la luna tiene el eje x hacia el planeta y el eje z en la normal a su órbita (producto de la posición y la velocidad relativas, de las efemérides de JPL); la rotación es síncrona. Latitud y longitud se miden sobre una esfera del radio publicado de la luna.
2. **Astros:** el Sol, los planetas, las demás lunas del sistema y **el planeta anfitrión** salen de las efemérides de JPL con la misma geometría que los simuladores de cielo desde un planeta ([cielo desde Júpiter](cielo-jupiter.md)); se calculan tamaño angular, fase y magnitud.
3. **Estrellas y proyección:** igual que en los demás simuladores de cielo (Hipparcos/Tycho, movimiento propio, proyección estereográfica).

## Validación

Las pruebas automáticas comprueban que el diámetro angular de Júpiter visto desde Europa es de 12,2° ± 0,5°, que el planeta está en el cénit del punto subplanetario y que, tras 3,3 días, sigue casi en el mismo lugar del cielo (la libración debida a la excentricidad de la órbita es de pocos grados).

## Tolerancias y límites

- Rotación síncrona **idealizada**: se ignoran la libración física y la leve rotación no síncrona; el punto subplanetario se toma sobre la dirección media al planeta.
- Sin atmósfera apreciable ni refracción. Magnitudes de planetas y lunas con el modelo de Lambert y albedos medios; la luz reflejada por Júpiter sobre la superficie no se modela.
- Radio de Europa: 1 560,8 km (valor publicado, esfera).

Sistema de referencia: eclíptica J2000 (ICRF); tiempo: TDB mostrado en UTC; datos: NASA/JPL Horizons (DE441 y kernels de satélites).

## Archivos

[`cielo-europa.html`](https://vladimiracunadev-create.github.io/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program/simuladores/cielo-europa.html) · [`paginas/cielo-europa.js`](../paginas/cielo-europa.js) · [`motor/cielo.js`](../motor/cielo.js)
