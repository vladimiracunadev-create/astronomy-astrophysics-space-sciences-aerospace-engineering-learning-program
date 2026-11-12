# Capítulo 4 · Subsistemas

## Por qué existe este capítulo

Cada subsistema de un telescopio infrarrojo responde a un solo problema: **mantenerse frío, apuntar con precisión y no moverse**. Este capítulo los recorre.

## Espejo y óptica

- **18 segmentos hexagonales** de berilio recubiertos de oro (el oro refleja muy bien el infrarrojo).
- Cada segmento tiene **actuadores** que lo mueven con una precisión de nanómetros: tras el despliegue se **alinea activamente** hasta que los 18 se comportan como un solo espejo (unos tres meses de alineación en la práctica).
- **Espejo secundario** en un mástil, y un **espejo de guiado fino**.
- **Tolerancia:** el error de superficie debe ser de decenas de nanómetros, una fracción de la longitud de onda.

## Escudo solar

Cinco láminas de un material plástico muy fino con recubrimiento metálico, separadas por espacios. Funciona como una **cadena de pantallas**: cada una refleja y reemite parte del calor hacia el espacio. El laboratorio (sección 4) muestra el modelo ideal de láminas paralelas: de 383 K en la cara caliente a ≈ 160 K tras cinco láminas. El **diseño real** llega a ≈ 40 K porque las láminas están **inclinadas y separadas**, de modo que el calor escapa por los lados.

**Decisión clave:** el escudo hace posible que el telescopio sea pasivo (sin refrigerante) en casi todo, pero es **el elemento más delicado**: miles de cables, poleas y tensores.

## Instrumentos

Cuatro instrumentos científicos (⚠ verifica en la fuente): una cámara de infrarrojo cercano, un espectrógrafo de infrarrojo cercano con una matriz de microobturadores, un instrumento de infrarrojo medio (cámara y espectrógrafo) y un sensor de guiado fino con un espectrógrafo adicional. El de infrarrojo medio necesita **≈ 7 K**, que se logra con un **refrigerador criogénico** activo.

## Potencia

Un panel solar siempre apuntando al Sol, detrás del escudo, de ≈ 2 kW (⚠), y baterías para los eventos críticos. El panel y el escudo comparten el lado caliente.

## Control de actitud y propulsión

- **Ruedas de reacción** y **sensores de estrellas** para apuntar con precisión; la presión de la luz solar sobre el escudo es una perturbación que hay que equilibrar.
- **Propulsores de hidrazina** para el mantenimiento orbital y la descarga de las ruedas.

## Comunicaciones

- Banda Ka a ≈ 25,9 Mbit/s hacia la Tierra para la ciencia (≈ 2,4 horas de enlace al día para 28 GB; laboratorio, sección 7) y banda S para la telemetría y los comandos.
- La Tierra siempre está en el campo de visión de la antena.

## Cómputo

Computadores redundantes de vuelo y un **registro de datos en estado sólido** para guardar las observaciones hasta el enlace. Se diseña para operar **sin ayuda** durante días.

## Ejercicio del capítulo

1. Calcula con el laboratorio la temperatura tras 7 láminas en el modelo ideal. ¿Qué te dice sobre la eficiencia de añadir láminas?
2. Calcula el volumen de datos de un día si el instrumento principal produce 2 Mbit/s durante 18 horas.
3. Dibuja el **diagrama de temperaturas** del observatorio (lado caliente, escudo, lado frío) y explica qué componentes van en cada zona.

Anterior: [capítulo 3](03-lanzador-masas-y-vehiculo.md) · Siguiente: [capítulo 5](05-los-despliegues.md)
