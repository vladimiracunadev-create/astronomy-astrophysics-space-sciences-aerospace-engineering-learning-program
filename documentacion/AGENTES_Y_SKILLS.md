# Agentes y skills especializados

El repositorio incluye **11 agentes** y **7 skills** de Claude Code (en `.claude/agents/` y `.claude/skills/`) que trabajan con el contenido de este programa: 12 áreas, 133 bloques, 2 077 clases, 24 rutas profesionales, 10 talleres de misión y 23 simuladores. Se cargan al abrir el repositorio con Claude Code (en una sesión ya abierta, reinicie la sesión para que los detecte).

> **Alcance honesto.** Los agentes se apoyan en las clases del programa, que están **redactadas pero pendientes de revisión** (ninguna está impartida, revisada ni verificada), y en simuladores y herramientas de apoyo que **no sirven para decisiones de vuelo**. Cada cifra sin fuente pública verificable se marca con ⚠. Las reglas de una competencia concreta deben tomarse de su convocatoria oficial, no del programa.

## Agentes

| Agente | Úselo para | Áreas y bloques principales |
|---|---|---|
| `nasa-competencia-estratega` | Convertir la convocatoria y la rúbrica en plan, entregables, lista de comprobación y ensayo de preguntas | A12 B130 · A11 B124 · A07 B83 · talleres |
| `planificador-de-viaje-espacial` | Destino, ventana de lanzamiento, delta-v, duración, retardo de señal y cronograma de un viaje o misión | A06 B75, B71, B81, B82, B76, B77 · A08 B96 |
| `analista-de-mecanica-orbital-y-propulsion` | Cálculos y revisión de órbitas, maniobras, Lambert, lanzamiento, propulsión | A06 B71–B82 |
| `ingeniero-de-sistemas-espaciales` | Requisitos, concepto de operaciones, presupuestos con margen, riesgos, verificación | A07 B83–B95 |
| `cientifico-planetario-y-astrobiologo` | Objetivos científicos, instrumentos, sitios, habitabilidad | A05 B52–B70 · A03 · A04 |
| `especialista-en-operaciones-y-robotica-espacial` | Concepto de operaciones, telemetría, anomalías, autonomía, rovers y brazos | A08 B96–B103 |
| `medico-y-disenador-de-habitats-espaciales` | Misiones tripuladas, soporte vital, radiación, EVA, emergencias, factores humanos | A09 B104–B117 |
| `analista-de-entorno-derecho-y-seguridad-espacial` | Basura y tráfico, tratados, espectro, protección planetaria, responsabilidad | A10 B118–B123 |
| `gestor-de-proyecto-y-economia-espacial` | Cronograma, costos, financiamiento, seguros, viabilidad | A11 B124–B127 |
| `comunicador-y-pitch-cientifico` | Presentación, resumen, historia y preguntas del jurado, accesibilidad | A12 B128–B133 |
| `tutor-del-programa` | Plan de estudio según el tiempo disponible y explicación de un tema con las clases del programa | todo el programa |

## Skills

| Skill | Hace |
|---|---|
| `consultar-el-programa` | Localiza clases y bloques por tema y los cita con su ruta |
| `planificar-viaje-espacial` | Hohmann, ventanas 2027–2050, delta-v, duración, retardo y cronograma de un viaje |
| `presupuesto-de-mision` | Delta-v y masa (ecuación del cohete), potencia, enlace y consumibles con márgenes |
| `plan-de-competencia-nasa` | Plan hora a hora, mapa regla→entregable y lista de comprobación final |
| `revisar-rigor-y-fuentes` | Auditoría de unidades, cifras y fuentes; marca lo no verificable |
| `preparar-pitch-cientifico` | Guion con tiempos, diapositivas esenciales y 10 preguntas del jurado |
| `estudio-relampago` | Plan de estudio intensivo con clases, simuladores y ejercicios |

## Herramientas nuevas que usan

- [`herramientas/consulta_programa.py`](../herramientas/consulta_programa.py): `tema "<término>" [--texto]`, `bloque B75`, `area A06`, `areas`. Encuentra qué clases responden una pregunta y da su ruta.
- [`herramientas/planificador_de_misiones.py`](../herramientas/planificador_de_misiones.py): `resumen`, `hohmann --destino marte`, `ventanas --destino marte --desde 2027 --hasta 2050`. Hohmann circular y coplanar con las posiciones oficiales de JPL de los simuladores (error de una ventana de semanas frente al óptimo de Lambert, p. ej. Marte: salida óptima 2028-11-29 frente a 2029-01-06 de primera aproximación; Venus 2028-03-25 frente a 2028-03-08). Para diseñar, use el [simulador de trayectorias](../simuladores/documentacion/trayectorias.md).
- [`herramientas/calculadora_cientifica.py`](../herramientas/calculadora_cientifica.py): constantes con fuente, órbitas, Hohmann, ecuación del cohete, conversiones.

## Guía rápida (preparar una competencia en poco tiempo)

1. **Reglas primero:** `nasa-competencia-estratega` con la convocatoria y la rúbrica oficiales → plan hora a hora y lista de comprobación.
2. **Contenido técnico:** el agente del tema (viaje, sistemas, ciencia planetaria, operaciones, hábitats, derecho, proyecto) con la pregunta concreta.
3. **Cifras:** `presupuesto-de-mision` y luego `revisar-rigor-y-fuentes` para que todo número tenga unidades y fuente.
4. **Presentación:** `preparar-pitch-cientifico` y un ensayo cronometrado con 10 preguntas del jurado.
5. **Estudio de refuerzo:** `estudio-relampago` o `tutor-del-programa` según el tiempo que quede.
