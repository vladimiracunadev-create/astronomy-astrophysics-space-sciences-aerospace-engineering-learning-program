# Capítulo 10 · Entregables y rúbrica

## Por qué existe este capítulo

Un taller se cierra con un producto. Este capítulo define qué debe contener tu **dossier de misión**, cómo se revisa y cómo se evalúa, para que sea comparable y verificable.

## El dossier de misión

Un documento de **20 a 40 páginas** (más anexos) con estas secciones, una por capítulo:

| Sección | Contenido mínimo | Capítulo |
|---|---|---|
| 1. Objetivo | Pregunta científica, objetivos, 10 requisitos con unidad y método de verificación, niveles de éxito | 1 |
| 2. Trayectoria | Ventana propuesta, C3, Δv, tiempo de vuelo, plan B, sistema de referencia y unidades | 2 |
| 3. Lanzador y masas | Lanzador elegido con su curva, tabla CBE/reserva/MEV, margen de masa | 3 |
| 4. Subsistemas | Decisión clave por subsistema; presupuestos de potencia y de enlace | 4 |
| 5. Entrada y aterrizaje | Secuencia, riesgos, probabilidad de éxito, criterios de «no ir» | 5 |
| 6. Operaciones | Sol típico, modos seguros, volumen de datos, fin de misión | 6 |
| 7. Fiabilidad | FMEA (10 filas), árbol de fallas, márgenes y responsables, contingencias | 7 |
| 8. Seguridad y protección planetaria | Plan de una página, seguridad de lanzamiento, ciberseguridad | 8 |
| 9. Costos y calendario | WBS, costo con reservas, cronograma y camino crítico, marco legal | 9 |
| 10. Revisión | Lista de riesgos abiertos, supuestos, límites y lo que no sabes | este |

### Reglas de formato (no negociables)

- **Cada cifra lleva unidad** y, si procede, sistema de referencia y fecha (en UTC).
- **Cada dato real** cita su fuente (nombre del documento y alcance). Si no puedes citarlo, no es un dato: es una suposición y se marca como tal.
- **Cada cálculo** indica el modelo usado y su tolerancia. «Resultado de diseño preliminar (±5 %)» es una frase honesta; «el resultado es exacto» casi nunca lo es.
- **Los límites** se dicen: qué no cubre tu análisis.

## La revisión

Preséntalo a un «comité» (compañeros, docente o tú en otro momento) como en una **revisión de diseño preliminar (PDR)**. El comité busca:

1. **¿Cumple los requisitos?** Cada requisito debe rastrearse hasta una decisión de diseño y a una forma de verificación.
2. **¿Hay un riesgo rojo sin plan?** Es motivo de no pasar.
3. **¿Están los márgenes y los supuestos a la vista?**
4. **¿Las cifras cuadran entre capítulos?** (La masa del capítulo 3 es la que usa el 5, el costo del 9 es el que usa la reserva.)

El comité anota **observaciones**, y tú respondes por escrito a cada una: aceptada, rechazada con razones o aplazada con fecha.

## Rúbrica

Cada criterio se califica de 0 a 4 (0 ausente, 1 básico, 2 correcto, 3 sólido, 4 ejemplar). Máximo 40 puntos.

| Criterio | Qué se mira |
|---|---|
| Claridad del objetivo | Pregunta concreta, requisitos comprobables |
| Corrección técnica | Cálculos reproducibles con el laboratorio, unidades correctas |
| Realismo | Datos reales con fuente, supuestos declarados |
| Análisis de riesgos | FMEA y árbol de fallas coherentes, controles con sentido |
| Márgenes y reservas | Declarados, con dueño y regla de uso |
| Operaciones | Plan factible con el retardo de luz y la autonomía |
| Seguridad y protección planetaria | Requisitos identificados y cumplidos |
| Costo y calendario | WBS, reservas, camino crítico |
| Integración | Las secciones se corresponden entre sí |
| Honestidad y límites | Se dice qué se ignora y qué falta |

**Aprobado:** 24 puntos o más y **ningún criterio en 0**. Un dossier con un riesgo rojo sin plan **no se aprueba**, sin importar el puntaje.

## Cómo se conecta con el resto del programa

Este taller toca casi todo lo aprendido:

- **A01 y A02:** unidades, escalas, matemática y laboratorio en Python.
- **A03 y A05:** el objetivo científico y el destino.
- **A06:** trayectoria, ventana y entrada atmosférica.
- **A07:** subsistemas, pruebas e integración.
- **A08:** operaciones y autonomía.
- **A09 y A10:** protección planetaria, seguridad y derecho.
- **A11 y A12:** costo, gestión y comunicación del proyecto.

Al terminar, tu dossier es un **portafolio** de lo que sabes hacer, y la mejor evidencia de que dominas el programa más allá de las clases sueltas.

## Para seguir

Cuando termines el taller de Marte, el [índice de talleres](../README.md) propone otras misiones con retos distintos: llegar a la Luna con personas, sobrevolar Plutón, observar desde un punto de equilibrio, entrar en órbita de Saturno, acompañar un cometa, acercarse al Sol, traer una muestra de un asteroide, volar en órbita baja con tripulación y desviar un asteroide.

Anterior: [capítulo 9](09-costos-cronograma-y-derecho.md) · [Índice del taller](README.md)
