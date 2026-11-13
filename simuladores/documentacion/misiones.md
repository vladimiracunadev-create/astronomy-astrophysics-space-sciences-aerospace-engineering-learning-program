# Simulador de misiones espaciales

[▶ Abrir el simulador](https://vladimiracunadev-create.github.io/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program/simuladores/misiones.html) · [Guía de uso](GUIA_DE_USO.md) · [Datos y efemérides](DATOS_Y_EFEMERIDES.md) · [Talleres de misión](../../talleres/README.md)

![Trayectorias de Pioneer, Voyager y New Horizons](../img/misiones.svg)

## Qué hace

Se **elige una misión**, se pulsa ▶ y se ve su trayectoria real moverse entre los planetas, con la fecha, los días desde el inicio de los datos, la distancia al Sol y a la Tierra, la velocidad, el tiempo que tarda la señal en llegar a la Tierra y el planeta más cercano. Una lista de **hitos y acercamientos** permite saltar al instante de cada sobrevuelo. Se puede «seguir la nave» con la cámara, recorrer el tiempo con la barra y cambiar la velocidad (de 1 día por segundo a 3 años por segundo).

| Misión | Qué se ve |
|---|---|
| **Pioneer 10** y **Pioneer 11** | Los primeros sobrevuelos de Júpiter (1973 y 1974) y el de Saturno de Pioneer 11 (1979) |
| **Voyager 1** y **Voyager 2** | El «Gran Tour»: Júpiter, Saturno, Urano y Neptuno (Voyager 2) y el cruce de la heliopausa (2012 y 2018) |
| **Galileo** | La llegada a Júpiter (1995) y su órbita hasta 2003 |
| **Cassini** | Asistencias de Venus (1998 y 1999), la Tierra (1999) y Júpiter (2000), y la llegada a Saturno (2004) |
| **New Horizons** | La asistencia de Júpiter (2007) y el sobrevuelo de Plutón (2015) |
| **Juno** | La órbita polar de Júpiter desde 2016 |
| **Parker Solar Probe** | Las siete asistencias de Venus de 2018 a 2024 |
| **James Webb** | El punto L2 Sol–Tierra, a ≈ 1,5 millones de km, siempre en el lado opuesto al Sol |
| **Europa Clipper** | Asistencias de Marte (2025) y la Tierra (2026) y la llegada a Júpiter en 2030 |

## Datos

Las trayectorias son las **reconstruidas por JPL con datos de seguimiento** (SPICE), descargadas de Horizons como posiciones heliocéntricas (eclíptica y equinoccio J2000) con paso de 1 a 3 días y evaluadas con la misma interpolación de Lagrange que el resto de los simuladores. Los planetas (Mercurio a Neptuno y el baricentro de Plutón) salen de las efemérides oficiales de 1970 a 2051. Las trayectorias posteriores al 13 de noviembre de 2026 (Voyager y Pioneer más allá de esa fecha, Juno, Parker, Webb y Europa Clipper) son **predicciones** de JPL y se rotulan así. Generador: [`herramientas/efemerides/generar_misiones.py`](../../herramientas/efemerides/generar_misiones.py).

## Validación

| Comprobación | Referencia | Resultado |
|---|---|---|
| Acercamientos a planetas detectados en los datos | Fechas históricas publicadas por la NASA de 27 sobrevuelos e inserciones en órbita | Coinciden a ≤ 2,5 días en los 27 |
| Distancia al cruzar la heliopausa | Voyager 1 (25-08-2012) ≈ 121 UA, Voyager 2 (05-11-2018) ≈ 119 UA | Dentro de ±1,5 UA |
| James Webb | En L2: 1,0–1,9 millones de km de la Tierra y más lejos del Sol que ella | Cumple |
| Interpolación contra Horizons | 120 épocas no nodales por cuerpo | Planetas interiores y Plutón ≤ 0,01 km, Saturno 12 km, Urano 21 km, Neptuno 143 km y Júpiter 165 km (oscilación real del centro del planeta); naves: del orden de 10³ km en la mayoría y hasta ≈ 3×10⁵ km en las que hacen maniobras y sobrevuelos cercanos (Cassini, Juno, Galileo, Parker, Europa Clipper) |

Los acercamientos **se detectan** como mínimos de la distancia nave–planeta en los datos; no se escriben a mano. Por eso la distancia indicada en un sobrevuelo rápido es aproximada: con datos heliocéntricos de 1 día, una nave que pasa a 200 000 km de un planeta a 30 km/s se mueve ≈ 2,6 millones de km por muestra.

## Límites

- **Es una visualización de trayectorias heliocéntricas, no un simulador de sobrevuelos.** No muestra la geometría del encuentro (planos de la trayectoria, ocultaciones, fases de la nave respecto del planeta).
- Los **tamaños** de los puntos son simbólicos; las distancias, reales.
- La precisión de la posición cae durante las maniobras y los sobrevuelos (véase la tabla); lejos de ellos es de pocos cientos de km.
- Sólo se incluyen las misiones citadas; otras relevantes (Mariner 10, Ulysses, Dawn, Rosetta, OSIRIS-REx, Hayabusa2, las misiones a Marte) podrían añadirse con el mismo generador.

Sistema de referencia: eclíptica y equinoccio J2000 (ICRF), centro el Sol; unidades: km, UA, km/s y días; tiempo: TDB mostrado en UTC; datos descargados el 13 de noviembre de 2026.

## Archivos

[`misiones.html`](https://vladimiracunadev-create.github.io/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program/simuladores/misiones.html) · [`paginas/misiones.js`](../paginas/misiones.js) · [`motor/misiones.js`](../motor/misiones.js) · [`motor/app-misiones.js`](../motor/app-misiones.js) · [`datos/misiones.json`](../datos/misiones.json) · [`datos/planetas_hist.json`](../datos/planetas_hist.json)
