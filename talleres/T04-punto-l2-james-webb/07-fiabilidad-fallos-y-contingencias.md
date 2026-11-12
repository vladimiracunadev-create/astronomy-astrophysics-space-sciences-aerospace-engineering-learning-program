# Capítulo 7 · Fiabilidad, fallos y contingencias

## Por qué existe este capítulo

La regla de este observatorio fue **«no se puede reparar, por lo tanto hay que probarlo todo»**. Su historia de pruebas y de retrasos es un curso de cómo se asegura una misión de un solo intento.

## Estrategia de fiabilidad

1. **Reducir puntos únicos de fallo** cuando se puede (con redundancia).
2. **Probar los restantes** con una intensidad desproporcionada.
3. **Márgenes grandes:** de potencia, de masa, de combustible y de tiempo.
4. **Revisiones independientes** de cada mecanismo y de cada línea de código crítico.

## Lo que mostraron las pruebas (⚠ contrasta con los informes oficiales)

| Hallazgo | Fecha aprox. | Efecto |
|---|---|---|
| Desgarro en una lámina del escudo y tornillos flojos tras una prueba de vibración | 2018 | Retraso de meses; revisión del diseño y del procedimiento |
| Problemas de comunicación entre equipos (telescopio y lanzador) | 2021 | Aplazamiento del lanzamiento por semanas |
| Una abrazadera que se liberó sola durante un ensayo en el lanzamiento | 2021 | Nueva verificación antes de despegar |

**Lección:** una prueba que **no encuentra nada** es sospechosa; una que **encuentra algo** es una prueba que cumple su misión.

## El requisito por punto

Con 344 puntos únicos (laboratorio, sección 5):

- Con 99,9 % por punto, el éxito global es ≈ 71 %.
- Para 90 % global hace falta 99,97 % por punto.

Para alcanzar ese nivel **no basta con probar el conjunto**: se verifica cada mecanismo **por separado** con una cantidad de ciclos mucho mayor de la que usará en el espacio (por ejemplo, abrir y cerrar un mecanismo cientos de veces), con **margen de fuerza** (el motor tiene varias veces la fuerza necesaria).

## Redundancia y sus límites

- **Motores y calentadores duplicados** en mecanismos críticos.
- **Computadores y electrónica redundantes.**
- **Modos degradados:** si falla la alineación fina, el telescopio sigue útil con menor resolución.
- **Pero** un escudo solar no tiene respaldo: si no se despliega, **no hay misión**. La decisión de aceptarlo se justifica con pruebas.

## Contingencias en vuelo

Para cada paso del despliegue hubo un **procedimiento alternativo** ensayado (calentar una zona con una luz, reintentar un mecanismo, usar un motor de respaldo). Los controladores ensayaron durante **meses** simulaciones con fallos introducidos por el equipo de pruebas, sin avisar.

## Gestión de la fatiga y de la presión

Un equipo humano, durante semanas, con decisiones cada hora: se planifican **turnos**, descansos y relevos. Es un riesgo operativo tan real como una pieza.

## Ejercicio del capítulo

1. Calcula el requisito por punto para un 95 % de éxito global en una cadena de 150 puntos.
2. Diseña un **plan de pruebas** para un mecanismo crítico: número de ciclos, margen de fuerza y condiciones ambientales.
3. Construye un **FMEA** de cinco filas para el despliegue de un mástil con un resorte, un motor y un cable.
4. Escribe un **escenario de ensayo con fallo introducido** para el equipo de operaciones.

Anterior: [capítulo 6](06-operaciones-y-comunicaciones.md) · Siguiente: [capítulo 8](08-seguridad-y-entorno.md)
