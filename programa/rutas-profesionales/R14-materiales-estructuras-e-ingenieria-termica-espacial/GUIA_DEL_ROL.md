# R14 — Guía del rol: ingeniero/a de estructuras, materiales y térmica de vehículos espaciales

> Esta guía describe el rol para quien decide si es para sí. No es un temario ni una promesa de empleo, habilitación o título. El orden de clases está en [RECORRIDO.md](RECORRIDO.md).

## Qué es

Es la persona que responde dos preguntas sobre un vehículo o instrumento espacial: **¿aguanta?** (el lanzamiento, el vacío, los impactos, la fatiga) y **¿a qué temperatura queda?** (en el sol, en el eclipse, en el peor caso al final de la vida). Elige materiales, dimensiona la estructura, construye modelos de elementos finitos y de nodos térmicos, define el control térmico y diseña, o revisa, los ensayos que demuestran que el análisis era correcto.

El trabajo es una cadena de **márgenes**: cada cifra de resistencia o de temperatura se compara con un límite y se deja escrito cuánto sobra y con qué incertidumbre.

## Qué NO es (y con qué se confunde)

- **No es el ingeniero de sistemas del satélite** ([R12](../R12-ingenieria-y-construccion-de-satelites-y-cubesats/INDICE.md)). Ese rol reparte masa, potencia y datos entre subsistemas; este rol es dueño de dos subsistemas y entrega los márgenes que el primero necesita.
- **No es ingeniería de lanzadores ni de propulsión** ([R11](../R11-ingenieria-de-lanzadores-y-propulsion/INDICE.md)). Aquí el lanzador es una fuente de cargas; allá se diseña. La protección térmica de reentrada aparece solo como contexto.
- **No es aviónica ni potencia.** El calor que disipan las tarjetas es un dato de entrada, no un diseño propio.
- **No es mecánica de pruebas por sí sola.** Quien opera el vibrador o la cámara de vacío es técnico de ensayos; este rol define qué se ensaya, con qué criterio de aceptación y qué se concluye.

## Un día de trabajo

Mañana típica: revisar el resultado de una corrida de elementos finitos y comprobar primero que la malla converge y que las condiciones de contorno representan la interfaz real, antes de leer una sola tensión. Después, actualizar el modelo térmico con la potencia disipada que informó otro subsistema y recalcular el caso caliente con propiedades ópticas de fin de vida (los recubrimientos se degradan; la referencia de NASA lo advierte expresamente). Por la tarde, reunión de revisión de un plan de ensayo, correlación entre un modo medido y el modelo, y un informe de desviación si el modo medido no coincide.

## Qué decide y qué entrega

**Decide:** qué material y qué espesor cumplen los requisitos con margen, qué técnica térmica (pasiva o activa) basta, y qué ensayo demuestra que el diseño es aceptable.

**Entrega:** informes de análisis trazables a requisitos, modelos documentados, selección de materiales con su justificación, y el plan e informe de calificación.

## Conocimientos y herramientas

- Mecánica de sólidos, elasticidad, pandeo, uniones atornilladas, fatiga y fractura.
- Elementos finitos: malla, convergencia, condiciones de contorno, análisis modal y correlación con ensayos.
- Transferencia de calor por conducción y radiación, modelos de nodos, casos extremos (caliente y frío).
- Materiales: aleaciones, compuestos, polímeros, cerámicos; comportamiento en vacío y desgasificación.
- Entorno espacial: oxígeno atómico, radiación, ultravioleta, micrometeoritos, contaminación.
- Programación para automatizar cálculos y reproducirlos.

La categoría de herramientas (solvers de elementos finitos, programas de modelado térmico por nodos, hojas de cálculo y Python) es general; cualquier producto concreto es una decisión del equipo y no una recomendación de este programa.

## Qué dicen las fuentes consultadas

La referencia de NASA sobre tecnología de satélites pequeños, en su capítulo de estructuras, materiales y mecanismos (consultado el 2026-11-05, edición con fecha de página 4 de agosto de 2026, y leído hasta aproximadamente el 80 % del capítulo), describe estructuras primarias comerciales y a medida, dispensadores, mecanismos y manufactura aditiva polimérica, y señala que los mecanismos han contribuido a más del 10 % de las fallas reportadas de satélites pequeños; insiste en probar «como se vuela», en margen y en ensayos de vida. Su capítulo de control térmico (consultado el 2026-11-05, fecha de página 7 de mayo de 2026) plantea el balance de calor entre absorción solar, albedo, disipación interna y radiación, separa técnicas pasivas de activas, y advierte que las prestaciones publicadas por fabricantes no están verificadas de forma independiente. La organización ECSS (consultada el 2026-11-05, portada del sitio) mantiene un conjunto único de normas europeas, con ejemplos publicados sobre limpieza y control de contaminación; qué norma aplica a cada proyecto, en qué versión y con qué jurisdicción es una decisión contractual que este programa no resuelve (ver huecos del recorrido).

Fuentes:

- NASA, *State-of-the-Art of Small Spacecraft Technology*, cap. 6 «Structures, Materials, and Mechanisms», <https://www.nasa.gov/smallsat-institute/sst-soa/structures-materials-and-mechanisms/> — consultado 2026-11-05.
- NASA, *State-of-the-Art of Small Spacecraft Technology*, cap. 7 «Thermal Control», <https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/> — consultado 2026-11-05.
- ECSS, <https://ecss.nl/> — consultado 2026-11-05.

No se citan salarios, cifras de empleo ni certificaciones: no se verificaron.

## Evidencias y portafolio

Evidencia que sí demuestra el trabajo: un modelo de elementos finitos de una pieza con estudio de convergencia y comparación con una solución analítica; un modelo térmico de nodos de un satélite pequeño con casos caliente y frío y su análisis de incertidumbre; una selección de materiales justificada con criterio múltiple; un plan de calificación con criterios de aceptación e informe de desviaciones. Todo reproducible (código, datos, versiones) y con unidades, marco de referencia y tolerancias declarados.

## Progresión

Se entra resolviendo piezas y casos de un subsistema, luego se asumen modelos completos de un vehículo y finalmente se coordina la calificación con el resto del sistema. Cómo se llama cada nivel y qué se exige depende de la organización; el programa no lo fija.

## Límites éticos y de seguridad

- Un modelo no es una prueba: lo analizado se verifica con ensayo antes de volar.
- Las cargas de seguridad de personas o de terceros (reentrada, estructuras presurizadas, impactos) se derivan a normas vigentes y a profesionales habilitados; este recorrido no sustituye formación, licencia ni supervisión.
- No usar propiedades de fabricante sin contrastar; registrar supuestos inválidos y casi incidentes.
- La sostenibilidad cuenta: materiales y diseño influyen en desechos y fin de vida.
