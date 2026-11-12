# T01 · Marte: planificar una misión como Mars 2020 / Perseverance

> **Qué es un taller.** Un taller no se lee: se hace. Reúne lo aprendido en las 12 áreas del programa para planificar, de principio a fin, una misión real. Aquí el caso es **Mars 2020**: un rover de la NASA que despegó el 30 de julio de 2020, aterrizó en el cráter Jezero el 18 de febrero de 2021 y busca señales de vida antigua y prepara muestras para traerlas a la Tierra.
>
> **Estado:** E0 (redactado, pendiente de revisión disciplinar). Las cifras de la misión son **redondeadas y de referencia pública**; antes de usarlas en un trabajo hay que contrastarlas con la fuente primaria (ver [fuentes](#fuentes)). El taller **no sirve para diseñar ni operar una misión real**.

## Qué vas a lograr

Al terminar podrás:

1. Definir el **objetivo científico** de una misión y traducirlo en requisitos medibles.
2. Elegir **ventana de lanzamiento y trayectoria** y calcular su delta-v, C3 y tiempo de vuelo.
3. Hacer un **presupuesto de masa, potencia y comunicaciones** con márgenes.
4. Planificar la **fase más peligrosa** (entrada, descenso y aterrizaje) y sus contingencias.
5. Construir un análisis de **fallos y riesgos** que deje la misión «a prueba de fallos» en lo que se puede controlar y honesta en lo que no.
6. Estimar **costo, cronograma y reservas**, y revisar el marco legal y de protección planetaria.
7. Presentar un **dossier de misión** que un comité pueda evaluar.

## Capítulos

| # | Capítulo | Qué resuelve | Áreas del programa que usa |
|---|---|---|---|
| 1 | [Objetivo y requisitos](01-objetivo-y-requisitos.md) | Para qué vamos a Marte y qué debe cumplirse | A03, A05, A12 |
| 2 | [Ventana y trayectoria](02-ventana-y-trayectoria.md) | Cuándo salir y por qué camino | A02, A06 |
| 3 | [Lanzador, masas y vehículo](03-lanzador-masas-y-vehiculo.md) | Qué cohete y cuánto pesa cada parte | A06, A07 |
| 4 | [Subsistemas de la nave](04-subsistemas.md) | Potencia, térmica, comunicaciones, cómputo y propulsión | A07 |
| 5 | [Entrada, descenso y aterrizaje](05-entrada-descenso-y-aterrizaje.md) | Los siete minutos que deciden la misión | A05, A06, A07 |
| 6 | [Operaciones y comunicaciones](06-operaciones-y-comunicaciones.md) | Cómo se conduce un rover a 20 minutos luz | A08 |
| 7 | [Fiabilidad, fallos y contingencias](07-fiabilidad-fallos-y-contingencias.md) | Cómo no fallar, y qué hacer si algo falla | A07, A08 |
| 8 | [Protección planetaria y seguridad](08-proteccion-planetaria-y-seguridad.md) | No contaminar Marte ni poner en riesgo a la Tierra | A10 |
| 9 | [Costos, cronograma, derecho y cooperación](09-costos-cronograma-y-derecho.md) | Cuánto cuesta, cuánto tarda, bajo qué reglas | A10, A11 |
| 10 | [Entregables y rúbrica](10-entregables-y-rubrica.md) | Qué debe tener tu dossier y cómo se evalúa | todas |

Laboratorio de apoyo: [`laboratorio_T01.py`](laboratorio_T01.py) (Python, solo biblioteca estándar). Se ejecuta con `python laboratorio_T01.py` y calcula las cifras de los capítulos 2 a 9.

## Cómo trabajar este taller

1. **Lee el capítulo** y mira los datos reales de Mars 2020 que trae.
2. **Ejecuta la parte del laboratorio** que corresponde y comprueba que obtienes lo mismo.
3. **Haz el ejercicio** del capítulo, pero para *tu propia versión* de la misión (otro sitio de aterrizaje, otra ventana, otro presupuesto).
4. **Guarda tus decisiones** con su porqué: eso es el dossier del capítulo 10.

Tiempo orientativo: 25 a 40 horas de trabajo, repartidas en 10 sesiones.

## Prerrequisitos

Se recomienda haber pasado por: matemática y física del área A02, mecánica orbital del área A06 (bloques B71 a B82), sistemas espaciales del área A07 y operaciones del área A08. Quien no los tenga puede hacer el taller igual: cada capítulo recuerda lo necesario y enlaza con las clases.

## Fuentes

Las cifras de la misión provienen de materiales públicos de la NASA y del JPL (hoja de datos de la misión, kit de prensa del lanzamiento y del aterrizaje, resúmenes del Mars Exploration Program) y de publicaciones técnicas abiertas sobre la entrada, el descenso y el aterrizaje. Se citan **por nombre y alcance**, no se reproducen. Cuando una cifra es incierta aparece marcada con ⚠ para que se verifique.

- NASA/JPL, *Mars 2020 Perseverance Launch Press Kit* y *Landing Press Kit*.
- NASA, *Mars 2020 Mission Overview* y hoja de datos del vehículo (masas, instrumentos, sitio de aterrizaje).
- NASA Planetary Protection Office, políticas para misiones a Marte; COSPAR, *Policy on Planetary Protection*.
- Tratado del Espacio Ultraterrestre (1967).

Volver al [índice de talleres](../README.md) · [README del programa](../../README.md).
