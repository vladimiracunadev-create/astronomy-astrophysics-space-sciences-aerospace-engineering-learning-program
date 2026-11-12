# T09 · Órbita baja: planificar un vuelo tripulado como Crew Dragon Demo-2

> **Qué es un taller.** Se hace, no se lee. Aquí el caso es **Demo-2**, el primer vuelo con personas de la cápsula **Crew Dragon** de SpaceX para la NASA. Despegó el 30 de mayo de 2020 con Douglas Hurley y Robert Behnken, se acopló a la Estación Espacial Internacional unas 19 horas después, pasó 62 días a bordo y amerizó en el Golfo de México el 2 de agosto de 2020.
>
> **Estado:** E0 (redactado, pendiente de revisión disciplinar). Las cifras son redondeadas y de referencia pública; las inciertas llevan ⚠. El taller **no sirve para diseñar ni operar una misión real** y, sobre todo, **no habilita decisiones de seguridad de la tripulación**.

## Por qué esta misión

Es el taller donde **la seguridad de las personas manda sobre todo**: cada decisión se toma pensando en que alguien va dentro. La misión no es lejana (420 km) ni larga, pero concentra los problemas del vuelo tripulado: **abortos**, soporte vital, **acoplamiento**, riesgo acumulado y un modelo de contratación nuevo (la NASA compra un **servicio**, no una nave).

## Qué vas a lograr

1. Calcular la **órbita de la estación**, el azimut de lanzamiento y la **maniobra de alcance**.
2. Diseñar un **sistema de aborto** y comprobar su aceleración.
3. Dimensionar el **soporte vital** de una cápsula independiente.
4. Entender el **riesgo de pérdida de la tripulación** y cómo se acumula.
5. Planificar un **retorno** con deorbitación, reentrada y recuperación.
6. Comparar **modelos de contratación** y costos por asiento.

## Capítulos

| # | Capítulo | Qué resuelve |
|---|---|---|
| 1 | [Objetivo y requisitos](01-objetivo-y-requisitos.md) | Qué debe demostrar un vuelo de certificación |
| 2 | [Ventana y trayectoria](02-ventana-y-trayectoria.md) | De la plataforma a la estación en 19 horas |
| 3 | [Lanzador, masas y vehículo](03-lanzador-masas-y-vehiculo.md) | Falcon 9 y Crew Dragon |
| 4 | [Subsistemas](04-subsistemas.md) | Soporte vital, trajes, pantallas y propulsión |
| 5 | [Abortos, acoplamiento y retorno](05-abortos-acoplamiento-y-retorno.md) | Las fases en que se protege a las personas |
| 6 | [Operaciones y comunicaciones](06-operaciones-y-comunicaciones.md) | Control de lanzamiento, control de vuelo y estación |
| 7 | [Fiabilidad, fallos y contingencias](07-fiabilidad-fallos-y-contingencias.md) | Pérdida de la tripulación y certificación |
| 8 | [Seguridad y salud](08-seguridad-y-salud.md) | Peligros en cabina y en la recuperación |
| 9 | [Costos, cronograma y derecho](09-costos-cronograma-y-derecho.md) | Contratos de precio fijo y responsabilidad |
| 10 | [Entregables y rúbrica](10-entregables-y-rubrica.md) | El dossier y su evaluación |

Laboratorio: [`laboratorio_T09.py`](laboratorio_T09.py). Figuras: [`figuras_T09.py`](figuras_T09.py) (SVG en `figuras/`).

## Fuentes

Materiales públicos de la NASA (kit de prensa de Demo-2, resumen del Programa de Tripulación Comercial, informes de la oficina de auditoría sobre costos del programa) y de SpaceX, publicaciones abiertas de los equipos y el Tratado del Espacio Ultraterrestre. Se citan por nombre y alcance; verifica las cifras marcadas con ⚠.

Volver al [índice de talleres](../README.md) · [README del programa](../../README.md).
