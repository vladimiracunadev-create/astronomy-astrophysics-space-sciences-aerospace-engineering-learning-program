# Capítulo 4 · Subsistemas

## Por qué existe este capítulo

Un vehículo diseñado para personas exige más que uno robótico: aire, agua, temperatura, protección contra la radiación y, sobre todo, **que ningún fallo simple mate a la tripulación**. Este capítulo recorre qué cambia.

## Soporte vital (probado, no usado)

Artemis I voló sin personas, pero con el sistema de soporte vital **instalado y probado** donde fue posible: control de presión, temperatura y humedad, y almacenamiento de agua y oxígeno. Una tripulación consume por persona y día de ≈ 0,84 kg de oxígeno, ≈ 2,5 kg de agua potable y produce ≈ 1 kg de dióxido de carbono (valores típicos; verifica). Sobre esa base se dimensionan los tanques, los purificadores y las reservas.

## Potencia y propulsión: el módulo de servicio

El **módulo de servicio europeo** aporta:

- Cuatro conjuntos de paneles solares que producen la electricidad de la cápsula.
- Un motor principal (heredado del transbordador) para las grandes quemas y varios propulsores para las correcciones.
- Control térmico por radiadores.
- Tanques de agua y oxígeno.

**Interfaz internacional:** Orion es de la NASA y el módulo de servicio de la ESA (Airbus). La interfaz entre ambos es un caso de libro de **unidades y sistemas de referencia explícitos** (capítulo 7 de T01).

## Control térmico

La cápsula alterna entre el Sol directo y la sombra, y entre el calor de la reentrada y el frío del espacio. Cálculos básicos con el laboratorio común (`temperatura_equilibrio`) muestran cómo la temperatura de una superficie depende del flujo solar, de su absortividad y de su emisividad.

## Aviónica y software

Orion usa **computadores de vuelo redundantes** y una arquitectura **tolerante a fallos** pensada para que dos fallos no dejen sin mando al vehículo (⚠ detalle de la arquitectura: verifica en la fuente). Para el vuelo con personas se exige que el software de seguridad sea independiente del software de la misión.

## Comunicaciones

- Enlaces con la **Red del Espacio Profundo** (DSN) y con la **red de comunicaciones cercanas** de la NASA.
- Retardo de una vía ≈ 1,3 s a la Luna, ≈ 1,44 s a la distancia máxima: lo bastante pequeño como para **operar con la Tierra en el bucle**, a diferencia de Marte.
- Se probó el sistema de comunicaciones con velocidades altas durante el crucero.

## Protección contra la radiación

Fuera de la protección del campo magnético terrestre, la tripulación recibe más radiación: partículas del Sol y rayos cósmicos. Artemis I llevó **maniquíes con sensores** (y un maniquí con un chaleco de protección, ⚠ verificar) para medir la dosis y comparar protecciones.

## Ejercicio del capítulo

1. Calcula las reservas de oxígeno, agua y absorción de CO₂ para una tripulación de 4 personas durante 21 días, con 30 % de margen.
2. Con el laboratorio común, calcula la temperatura de equilibrio de una superficie blanca (α=0,2, ε=0,9) y de una negra (α=0,95, ε=0,9) al Sol a 1 UA.
3. Describe una arquitectura de aviónica en la que **un fallo de software** no pueda dejar a la tripulación sin mando.
4. Haz el **presupuesto de energía** de un día de la misión con las cargas principales.

Anterior: [capítulo 3](03-lanzador-masas-y-vehiculo.md) · Siguiente: [capítulo 5](05-reentrada-y-amerizaje.md)
