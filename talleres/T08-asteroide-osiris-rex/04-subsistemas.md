# Capítulo 4 · Subsistemas

## Por qué existe este capítulo

Los subsistemas de una nave que se acerca a un asteroide hacen **trabajo de precisión**: cartografiar, medir la distancia, navegar por la superficie y tocarla. Este capítulo recorre lo que lo permite.

## Instrumentos de caracterización

Un conjunto de instrumentos para **conocer el cuerpo antes de tocarlo** (⚠ verifica nombres y funciones en la fuente):

- **Cámaras** de varias resoluciones, con un conjunto de tres.
- **Lídar** (altímetro láser) que mide la forma con precisión de centímetros.
- **Espectrómetros** visible-infrarrojo y térmico, que dan composición y temperatura.
- **Espectrómetro de rayos X** que estudia los elementos de la superficie.

La información de cada uno se combina en **mapas** del cuerpo con una resolución de pocos centímetros en el sitio de muestreo.

## Navegación relativa

Cerca de un asteroide no hay GPS: la nave se orienta por la **forma y las marcas del terreno**. Un sistema de **navegación por características naturales** compara imágenes tomadas durante el descenso con un **mapa** guardado y calcula posición y velocidad. Es el equivalente a la navegación relativa al terreno de T01.

## El brazo de muestreo (TAGSAM)

Un brazo de ≈ 3,35 m con un cabezal circular. Al tocar la superficie, **dispara un chorro de nitrógeno** que levanta el polvo y las piedras pequeñas hacia el interior del cabezal. Tiene **tres botellas de gas**: **tres intentos** posibles. Después, el cabezal se coloca en la cápsula.

**Decisión clave:** muestrear con gas, sin excavar ni perforar, que es más sencillo y soporta mejor una superficie desconocida.

## Potencia

Paneles solares grandes (a 1 UA hay luz de sobra) con **baterías** para las fases en la sombra. No hay material nuclear.

## Comunicaciones

Antena de alta ganancia en banda X y antenas de emergencia. Con un retardo de hasta 18,5 minutos (laboratorio, sección 4) para el momento del muestreo.

## Cómputo y autonomía

Computadores redundantes con software de **guiado autónomo** para el muestreo: durante los últimos minutos la nave decide por sí sola, con reglas que **abortan** el intento si algo sale de los límites (velocidad, altura, orientación).

## Propulsión

Un conjunto de **motores de hidrazina** de varios tamaños: grandes para las maniobras de traslado y pequeños para las **correcciones finas** cerca del cuerpo. Se usaron también **ráfagas de empuje** muy pequeñas para el contacto.

## La cápsula

Un cuerpo con un **escudo térmico**, un **paracaídas** y una **baliza**. Mantiene la muestra aislada y **sin ventilación** hasta llegar a una sala limpia.

## Ejercicio del capítulo

1. Diseña las **reglas de aborto** del muestreo: tres parámetros, sus límites y la acción si se superan.
2. Calcula cuánta masa de nitrógeno necesitas para tres intentos si cada uno usa 100 g.
3. Explica por qué una nave cerca de un asteroide necesita navegación por **características naturales**.

Anterior: [capítulo 3](03-lanzador-masas-y-vehiculo.md) · Siguiente: [capítulo 5](05-cerca-del-cuerpo-y-toma-de-muestra.md)
