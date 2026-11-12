# Capítulo 7 · Fiabilidad, fallos y contingencias

## Por qué existe este capítulo

New Horizons tenía que funcionar **diez años** y entregar su ciencia en un **único día**. Esa combinación define su estrategia de fiabilidad: simplicidad, redundancia de lo crítico, protección ante fallos y una **hibernación** que reduce el desgaste.

## Hibernación: apagar para que dure

Durante casi **1.900 días** (⚠ ≈ 5 años), la nave estuvo en **hibernación**: la mayoría de los sistemas apagados, giro estable y solo un «latido» semanal a la Tierra. Esto:

- **Reduce el desgaste** de componentes y el consumo del generador.
- **Reduce el costo** de operar (menos horas de antena y menos personal).
- **Añade un riesgo propio**: cada encendido y apagado puede fallar. El laboratorio (sección 6) calcula la probabilidad de que 18 ciclos salgan bien con 0,9995 cada uno: ≈ 0,991.

**Decisión de ingeniería:** se acepta el riesgo de los ciclos a cambio de la vida útil. Se compensa con pruebas y con la posibilidad de una **vuelta** a un modo seguro.

## Protección ante fallos

El computador tiene un **modo seguro** y un **segundo computador**. Si un dato se sale del rango, la nave:

1. Pasa a un estado conocido y seguro.
2. Gira la antena hacia la Tierra.
3. Informa y **espera**.

Esto basta para un crucero tranquilo, pero **es peligroso en un encuentro**: si pasa a modo seguro justo antes del sobrevuelo, pierdes la ciencia. Por eso se **ajustan** las reglas de protección durante el encuentro: algunos fallos no deben detener la secuencia (⚠ detalle en la fuente).

## El 4 de julio de 2015

Diez días antes del acercamiento, la nave dejó de comunicarse y pasó a modo seguro (la causa: una sobrecarga del computador por dos tareas simultáneas, ⚠ verifica). El equipo:

1. Esperó a que el modo seguro enviara su señal (≈ 4,4 horas más 3 horas de la distancia).
2. Diagnosticó con la telemetría que recibió.
3. Mandó restablecer el computador principal y las tareas.
4. Reprogramó el calendario de encuentro con un ajuste mínimo.

En unos tres días la nave volvió a su plan. **Moraleja:** el **ensayo de contingencias** y un equipo preparado valen más que un diseño que se crea perfecto.

## Márgenes

- **Margen de potencia:** el generador decae; el presupuesto se hace al final de vida.
- **Margen de combustible:** lo que sobró permitió visitar otro objeto.
- **Margen de calendario:** días de holgura antes del encuentro, para resolver problemas.

## Análisis de riesgos

El FMEA de un encuentro único prioriza lo que **no se puede recuperar**: el apuntado de la secuencia, la memoria de datos y la protección ante un impacto de polvo. La matriz de riesgos incluía el **polvo**: a 13,8 km/s un grano diminuto puede dañar la nave. Se decidió **orientar la antena como escudo** durante el paso por una zona de riesgo (⚠ detalle de la fuente).

## Ejercicio del capítulo

1. Calcula la probabilidad de éxito de la hibernación para 10, 18 y 30 ciclos con 0,999 por ciclo.
2. Haz un **FMEA** de cinco filas para el sobrevuelo: modo de fallo, efecto, detección y mitigación.
3. Diseña las **reglas de protección** para el crucero y para el encuentro, y explica por qué son distintas.
4. Describe el procedimiento de **recuperación** ante un modo seguro a diez días del encuentro.

Anterior: [capítulo 6](06-operaciones-y-comunicaciones.md) · Siguiente: [capítulo 8](08-seguridad-y-proteccion.md)
