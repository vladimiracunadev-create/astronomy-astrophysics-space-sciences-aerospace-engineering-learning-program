# Simulador del cielo desde Titán

[▶ Abrir el simulador](https://vladimiracunadev-create.github.io/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program/simuladores/cielo-titan.html) · [Guía de uso](GUIA_DE_USO.md) · [Datos y efemérides](DATOS_Y_EFEMERIDES.md) · [Fuentes y modelos](FUENTES_Y_MODELOS.md)

![Cielo completo visto desde la superficie de Titán, con Saturno](../img/cielo-titan.svg)

## Qué muestra

El cielo desde la **superficie de Titán**, la mayor luna de Saturno, la única con atmósfera densa, en cualquier lugar (7 predefinidos). Titán gira en 15,95 días y siempre muestra la misma cara a Saturno: desde el hemisferio que lo mira, **Saturno queda casi fijo en el cielo**, con un diámetro angular de ≈ 5,5° (unas 10 veces la Luna llena vista desde la Tierra) y con **fases** como las de la Luna. El Sol sale y se pone cada 15,95 días, y las demás lunas (Rea, Jápeto, Dione, Tetis y otras) y los anillos casi de canto cruzan el cielo; el resto de planetas y las estrellas completan la vista. En el hemisferio opuesto Saturno nunca sale.

## Cómo funciona

1. **Observador sobre una luna:** el sistema de referencia de la luna tiene el eje x hacia el planeta y el eje z en la normal a su órbita (producto de la posición y la velocidad relativas, de las efemérides de JPL); la rotación es síncrona. Latitud y longitud se miden sobre una esfera del radio publicado de la luna.
2. **Astros:** el Sol, los planetas, las demás lunas del sistema y **el planeta anfitrión** salen de las efemérides de JPL con la misma geometría que los simuladores de cielo desde un planeta ([cielo desde Saturno](cielo-saturno.md)); se calculan tamaño angular, fase y magnitud.
3. **Estrellas y proyección:** igual que en los demás simuladores de cielo (Hipparcos/Tycho, movimiento propio, proyección estereográfica).

## Validación

Las pruebas automáticas comprueban que el diámetro angular de Saturno visto desde Titán es de 5,5° ± 0,5°, que el planeta está en el cénit del punto subplanetario y que, tras 3,3 días, sigue casi en el mismo lugar del cielo (la libración debida a la excentricidad de la órbita es de pocos grados).

## Tolerancias y límites

- **Atmósfera:** la bruma anaranjada de Titán es opaca; el simulador muestra el cielo como se vería sin ella (p. ej. por encima de la bruma), no lo que se ve desde la superficie real. Rotación síncrona **idealizada**: se ignoran la libración física y la leve rotación no síncrona; el punto subplanetario se toma sobre la dirección media al planeta.
- Sin refracción ni extinción atmosférica. Magnitudes de planetas y lunas con el modelo de Lambert y albedos medios; la luz reflejada por Saturno sobre la superficie no se modela.
- Radio de Titán: 2 574,7 km (valor publicado, esfera).

Sistema de referencia: eclíptica J2000 (ICRF); tiempo: TDB mostrado en UTC; datos: NASA/JPL Horizons (DE441 y kernels de satélites).

## Archivos

[`cielo-titan.html`](https://vladimiracunadev-create.github.io/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program/simuladores/cielo-titan.html) · [`paginas/cielo-titan.js`](../paginas/cielo-titan.js) · [`motor/cielo.js`](../motor/cielo.js)
