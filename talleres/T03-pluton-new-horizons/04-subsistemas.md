# Capítulo 4 · Subsistemas

## Por qué existe este capítulo

A 32 UA el Sol es una estrella brillante más y su luz llega con **1/1.000** de la intensidad que en la Tierra. Cada subsistema se diseña para sobrevivir décadas casi sin mantenimiento y con pocos vatios.

## Potencia: un generador de radioisótopos

La luz del Sol a 32 UA es unos 1,3 W/m² (laboratorio común, `flujo_solar`): un panel solar necesario sería enorme. La solución es un **generador termoeléctrico de radioisótopos (GPHS-RTG)**: el plutonio-238 se desintegra y genera calor que se convierte en electricidad.

- ≈ **245 W** al lanzamiento (⚠ redondeado).
- Baja con los años por el **decaimiento** del plutonio (vida media ≈ 87,7 años) y por la **degradación** de los termopares. El laboratorio (sección 5) calcula ≈ 202 W al sobrevuelo (año 9,5) y ≈ 162 W en el año 20.

**Decisión de diseño:** el presupuesto de potencia se hace con el **final** de la vida útil, y los instrumentos se encienden **por turnos** para no superar los vatios disponibles.

## Térmica

El calor sobrante del generador ayuda a mantener la nave caliente, y el resto se gestiona con aislamiento, persianas y calefactores. Todo el vehículo se diseña para **no gastar vatios de más** en calentarse.

## Cómputo

**Dos computadores** idénticos (uno de respaldo) con procesadores resistentes a la radiación y de potencia modesta. Un **sistema de protección de fallos** vigila al conjunto y, ante una anomalía, pasa a un **modo seguro**: apuntar la antena a la Tierra y esperar órdenes. Este sistema es una pieza clave del capítulo 7.

## Comunicaciones

- Antena de alta ganancia de ≈ 2,1 m, enlace en banda X.
- Velocidad de datos **de unos pocos kbit/s a la distancia de Plutón** (laboratorio, sección 4): la señal es unas 40 veces más débil que a 5 UA.
- Recibe en la Tierra con las antenas de 70 m de la Red del Espacio Profundo.

## Control y propulsión

Pequeños propulsores de **hidrazina** para correcciones y apuntado; **estabilización por giro** durante el crucero y por tres ejes durante las observaciones. Sensores de estrellas para saber hacia dónde apunta.

## Instrumentos (7)

(⚠ verifica nombres y funciones en la fuente): una cámara de alta resolución (LORRI), una cámara y espectrómetro en el visible e infrarrojo (Ralph), un espectrómetro ultravioleta (Alice), un experimento de radio (REX), un analizador de viento solar (SWAP), un detector de partículas energéticas (PEPSSI) y un contador de polvo (construido por estudiantes, SDC).

## Ejercicio del capítulo

1. Calcula el flujo solar a 32 UA y la superficie de panel necesaria para 200 W con eficiencia del 20 %.
2. Con el laboratorio, calcula la potencia del generador en el año 15 y haz un presupuesto de encendido de instrumentos por turnos.
3. Describe cómo funciona un **modo seguro**: qué hace, cuándo se activa y cómo se sale de él.
4. Calcula la velocidad de datos máxima a 32 UA con la fórmula de Friis (potencia 12 W, antenas 2,1 m y 70 m, banda X).

Anterior: [capítulo 3](03-lanzador-masas-y-vehiculo.md) · Siguiente: [capítulo 5](05-el-sobrevuelo.md)
