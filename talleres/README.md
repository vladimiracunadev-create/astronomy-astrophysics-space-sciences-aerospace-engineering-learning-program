# 🛠️ Talleres integradores de misión

> **Qué son.** Los anexos se leen; los talleres **se hacen**. Cada taller toma una **misión espacial real**, la desarma por capítulos (objetivo, trayectoria, vehículo, subsistemas, fase crítica, operaciones, fiabilidad, seguridad, costos y derecho) y te pide planificar **tu propia versión**, aplicando todo lo aprendido en las 12 áreas del programa.
>
> **Estado:** E0 (redactado, pendiente de revisión disciplinar). Las cifras de cada misión son redondeadas y de referencia pública; las inciertas llevan ⚠ y hay que verificarlas en la fuente primaria. Los talleres **no sirven para diseñar ni operar una misión real**.

## Cómo está hecho cada taller

Una carpeta `Txx-misión/` con:

- `README.md`: la ficha de la misión real, los objetivos de aprendizaje, el índice de capítulos y las fuentes.
- **Diez capítulos** numerados, con ejercicios al final.
- `laboratorio_Txx.py`: cálculos en Python (solo biblioteca estándar) que declaran unidades, sistema de referencia, modelo y tolerancia.
- `figuras/` y `figuras_Txx.py`: esquemas SVG generados con el mismo modelo del laboratorio (trayectoria, secuencias, presupuestos).

Los diez capítulos siguen la misma estructura para que puedas comparar misiones:

| # | Capítulo | Pregunta que contesta |
|---|---|---|
| 1 | Objetivo y requisitos | ¿Para qué vamos y cómo sabremos que se logró? |
| 2 | Ventana y trayectoria | ¿Cuándo salir y por dónde? |
| 3 | Lanzador, masas y vehículo | ¿Qué cohete y cuánto pesa cada parte? |
| 4 | Subsistemas | ¿Cómo se alimenta, se calienta, se comunica y piensa la nave? |
| 5 | La fase crítica | ¿Qué momento decide la misión y cómo se prepara? |
| 6 | Operaciones y comunicaciones | ¿Cómo se conduce a esa distancia? |
| 7 | Fiabilidad, fallos y contingencias | ¿Cómo no fallar y qué hacer si algo falla? |
| 8 | Protección y seguridad | ¿Qué daño puede hacer la misión y cómo se evita? |
| 9 | Costos, cronograma y derecho | ¿Cuánto cuesta, cuánto tarda y bajo qué reglas? |
| 10 | Entregables y rúbrica | ¿Qué se entrega y cómo se evalúa? |

## Los diez talleres

| Taller | Misión real de referencia | Qué reto domina | Estado |
|---|---|---|---|
| [**T01 · Marte**](T01-marte-mars-2020-perseverance/README.md) | Mars 2020 / Perseverance (2020-2021) | Entrada, descenso y aterrizaje autónomos; muestras para retorno | ✅ Redactado |
| T02 · Luna | Artemis I (2022) | Cápsula tripulable en un viaje de ida y vuelta, escudo térmico y reentrada | ⏳ En preparación |
| T03 · Plutón | New Horizons (2006-2015) | Sobrevuelo a 30 UA, asistencia gravitatoria de Júpiter, enlace débil | ⏳ En preparación |
| T04 · Punto L2 | Telescopio James Webb (2021) | Observatorio desplegable en un punto de equilibrio, despliegues sin retorno | ⏳ En preparación |
| T05 · Saturno | Cassini-Huygens (1997-2017) | Asistencias gravitatorias múltiples, inserción orbital, sonda de descenso | ⏳ En preparación |
| T06 · Cometa | Rosetta y Philae (2004-2016) | Encuentro de baja velocidad con un cuerpo de gravedad casi nula | ⏳ En preparación |
| T07 · Sol | Parker Solar Probe (2018-) | Protección térmica extrema, aproximación por asistencias de Venus | ⏳ En preparación |
| T08 · Asteroide | OSIRIS-REx (2016-2023) | Toma de muestra y retorno a la Tierra | ⏳ En preparación |
| T09 · Órbita baja | Crew Dragon Demo-2 (2020) | Vuelo tripulado, acoplamiento, abortos y seguridad de la tripulación | ⏳ En preparación |
| T10 · Defensa planetaria | DART (2021-2022) | Impacto cinético sobre un asteroide, navegación autónoma terminal | ⏳ En preparación |

Los talleres se publican **uno por uno**. Se empieza por T01 porque sirve de plantilla de calidad para los demás.

## Para quién y cuánto toma

Cada taller toma entre 25 y 40 horas repartidas en diez sesiones. Sirve a estudiantes avanzados y profesionales: casi todas las rutas del programa (astrodinámica, ingeniería de satélites, operaciones, astronáutica, derecho espacial, gestión) tienen partes que ejercitar.

## Reglas comunes

1. **Cada cifra lleva su unidad**, y cada trayectoria su sistema de referencia y su fecha en UTC.
2. **Cada dato real cita su fuente**; si no tiene fuente, es una suposición y se marca como tal.
3. **Cada cálculo declara su modelo y tolerancia.**
4. **Nada de lo que aquí aparece habilita decisiones de vuelo, seguridad o regulatorias reales.**

Volver al [README del programa](../README.md) · [Anexos](../anexos/README.md) · [Documentación](../documentacion/README.md).
