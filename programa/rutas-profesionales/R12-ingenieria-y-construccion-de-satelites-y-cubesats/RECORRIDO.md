# R12 — Recorrido del rol: Ingeniero/a de sistemas y subsistemas de satélites y CubeSats

> Diseña, integra y califica un satélite pequeño: parte de una necesidad de misión, reparte masa, energía y datos entre subsistemas, y demuestra con ensayos que el conjunto cumple sus requisitos.

- **Decide:** Qué arquitectura y qué compromisos entre subsistemas cumplen los requisitos con los presupuestos de masa, potencia, datos y riesgo disponibles.
- **Entrega:** Presupuestos de misión, especificaciones de interfaz, modelo de diseño trazable a requisitos y plan y evidencias de integración y calificación.

**Alcance del recorrido:** 370 clases: 350 del tronco común y 20 propias de la ruta (temas que aún no tienen clase en el tronco); 334 obligatorias. Las clases del tronco se redactan una sola vez y se reutilizan; los módulos de la ruta no duplican contenido. No es una titulación: el avance se demuestra con evidencias.

## Pasos en orden

| # | Fase | Tipo | Clases | Capacidad que aporta | Nota |
|---:|---|---|---|---|---|
| 1 | Fundamentos | obligatoria | **Unidades, incertidumbre y fuentes**<br>[`B01-C04`](../../clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md) Espacio y tiempo en ciencia<br>[`B01-C08`](../../clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md) Mediciones y unidades astronómicas<br>[`B01-C18`](../../clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md) Incertidumbre y errores elementales<br>[`B01-C19`](../../clases/B01/B01-C19-fuentes-confiables-y-desinformacion-espacial/CLASE.md) Fuentes confiables y desinformación espacial | Reportar cualquier cifra de diseño con unidad, marco, incertidumbre y fuente. | Omitible si aprueba el diagnóstico de unidades y marcos. |
| 2 | Fundamentos | obligatoria | **Matemática y geometría operativas**<br>[`B03-C01`](../../clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md)–[`B03-C20`](../../clases/B03/B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md) (20 clases)<br>[`B04-C01`](../../clases/B04/B04-C01-polinomios-y-factorizacion/CLASE.md)–[`B04-C20`](../../clases/B04/B04-C20-triangulacion-espacial-aplicada/CLASE.md) (20 clases) | Resolver los cálculos algebraicos, trigonométricos y vectoriales de un presupuesto o de una orientación. | Omitible si aprueba el diagnóstico de matemática. |
| 3 | Fundamentos | obligatoria | **Física del entorno espacial**<br>[`B05-C01`](../../clases/B05/B05-C01-magnitudes-fisicas-y-dimensiones/CLASE.md)–[`B05-C20`](../../clases/B05/B05-C20-problema-fisico-integrado-de-satelite-ideal/CLASE.md) (20 clases) | Aplicar mecánica, energía, calor y electromagnetismo a un satélite. | Omitible si aprueba el diagnóstico de física. |
| 4 | Fundamentos | obligatoria | **Programación científica**<br>[`B07-C01`](../../clases/B07/B07-C01-pensamiento-algoritmico/CLASE.md)–[`B07-C20`](../../clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md) (20 clases) | Escribir y probar el código de un modelo de subsistema. | Omitible si demuestra un proyecto en Python con pruebas. |
| 5 | Tronco común | obligatoria | **Álgebra lineal, rotaciones y marcos**<br>[`B10-C01`](../../tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md)–[`B10-C20`](../../tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) (20 clases) | Representar la orientación del satélite con matrices y cuaterniones y cambiar de marco. | C12 a C16 son el núcleo de actitud. |
| 6 | Tronco común | obligatoria | **Simulación numérica**<br>[`B11-C01`](../../tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md)–[`B11-C11`](../../tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) (11 clases)<br>[`B11-C19`](../../tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md)–[`B11-C20`](../../tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) (2 clases) | Integrar numéricamente el movimiento y comprobar error y convergencia. | C12 a C18 se omiten salvo necesidad. |
| 7 | Tronco común | obligatoria | **Incertidumbre y metrología**<br>[`B12-C07`](../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) Estimación de parámetros<br>[`B12-C10`](../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) Regresión lineal y no lineal<br>[`B12-C14`](../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) Simulación Monte Carlo<br>[`B12-C16`](../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md)–[`B12-C18`](../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) (3 clases)<br>[`B13-C01`](../../tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md)–[`B13-C05`](../../tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) (5 clases)<br>[`B13-C12`](../../tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md)–[`B13-C13`](../../tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) (2 clases)<br>[`B13-C19`](../../tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md)–[`B13-C20`](../../tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) (2 clases) | Propagar incertidumbres y justificar márgenes de diseño. | B12-C20 se integra en el informe del paso final. |
| 8 | Tronco común | recomendada | **Datos reproducibles**<br>[`B14-C04`](../../tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) Unidades y constantes con Astropy<br>[`B14-C09`](../../tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) Jupyter y experimentos reproducibles<br>[`B14-C10`](../../tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) Pruebas de regresión numérica<br>[`B14-C12`](../../tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) Ejecución reproducible con uv<br>[`B14-C17`](../../tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) Contenedores y ambientes científicos | Mantener análisis y simulaciones reproducibles. |  |
| 9 | Tronco común | obligatoria | **Control automático**<br>[`B16-C01`](../../tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md)–[`B16-C14`](../../tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) (14 clases)<br>[`B16-C18`](../../tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md)–[`B16-C20`](../../tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) (3 clases) | Analizar la estabilidad de un lazo de control y sintonizar un controlador de actitud. |  |
| 10 | Tronco común | obligatoria | **Órbita del satélite**<br>[`B41-C01`](../../tronco-comun/B41-mecanica-orbital-fundamental.md)–[`B41-C20`](../../tronco-comun/B41-mecanica-orbital-fundamental.md) (20 clases) | Describir la órbita, su período y su geometría y propagarla con un modelo verificable. | La perturbación orbital (B42) se estudia cuando el rol lo requiera. |
| 11 | Tronco común | recomendada | **Perturbaciones orbitales**<br>[`B42-C01`](../../tronco-comun/B42-perturbaciones-y-evolucion-de-orbitas.md)–[`B42-C20`](../../tronco-comun/B42-perturbaciones-y-evolucion-de-orbitas.md) (20 clases) | Estimar cuánto deriva la órbita por arrastre y J2 durante la vida de la misión. |  |
| 12 | Tronco común | obligatoria | **Ingeniería de sistemas y diseño de misiones**<br>[`B49-C01`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md)–[`B49-C20`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md) (20 clases) | Pasar de una necesidad de misión a requisitos verificables, presupuestos y revisiones. | Es el eje del rol: las clases de la ruta lo profundizan. |
| 13 | Tronco común | obligatoria | **Estructuras y materiales**<br>[`B50-C01`](../../tronco-comun/B50-estructuras-materiales-y-fabricacion-espacial.md) Entorno mecánico de lanzamiento<br>[`B50-C05`](../../tronco-comun/B50-estructuras-materiales-y-fabricacion-espacial.md)–[`B50-C07`](../../tronco-comun/B50-estructuras-materiales-y-fabricacion-espacial.md) (3 clases)<br>[`B50-C09`](../../tronco-comun/B50-estructuras-materiales-y-fabricacion-espacial.md)–[`B50-C12`](../../tronco-comun/B50-estructuras-materiales-y-fabricacion-espacial.md) (4 clases)<br>[`B50-C20`](../../tronco-comun/B50-estructuras-materiales-y-fabricacion-espacial.md) Diseño estructural de plataforma satelital | Seleccionar materiales y verificar que la estructura resiste el lanzamiento. |  |
| 14 | Tronco común | obligatoria | **Térmica y entorno espacial**<br>[`B51-C01`](../../tronco-comun/B51-gestion-termica-y-entorno-espacial.md)–[`B51-C08`](../../tronco-comun/B51-gestion-termica-y-entorno-espacial.md) (8 clases)<br>[`B51-C11`](../../tronco-comun/B51-gestion-termica-y-entorno-espacial.md)–[`B51-C12`](../../tronco-comun/B51-gestion-termica-y-entorno-espacial.md) (2 clases)<br>[`B51-C18`](../../tronco-comun/B51-gestion-termica-y-entorno-espacial.md)–[`B51-C20`](../../tronco-comun/B51-gestion-termica-y-entorno-espacial.md) (3 clases) | Armar un balance térmico y definir un control térmico pasivo o activo. |  |
| 15 | Tronco común | obligatoria | **Potencia**<br>[`B52-C01`](../../tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md)–[`B52-C14`](../../tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md) (14 clases)<br>[`B52-C19`](../../tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md)–[`B52-C20`](../../tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md) (2 clases) | Dimensionar paneles y batería para el ciclo orbital. |  |
| 16 | Tronco común | obligatoria | **Actitud y control**<br>[`B53-C01`](../../tronco-comun/B53-sensores-y-control-de-actitud.md)–[`B53-C20`](../../tronco-comun/B53-sensores-y-control-de-actitud.md) (20 clases) | Elegir sensores y actuadores y verificar el control de actitud. |  |
| 17 | Tronco común | obligatoria | **Aviónica y software de vuelo**<br>[`B54-C01`](../../tronco-comun/B54-avionica-y-software-critico-espacial.md)–[`B54-C09`](../../tronco-comun/B54-avionica-y-software-critico-espacial.md) (9 clases)<br>[`B54-C11`](../../tronco-comun/B54-avionica-y-software-critico-espacial.md)–[`B54-C12`](../../tronco-comun/B54-avionica-y-software-critico-espacial.md) (2 clases)<br>[`B54-C14`](../../tronco-comun/B54-avionica-y-software-critico-espacial.md) Pruebas de software embarcado<br>[`B54-C19`](../../tronco-comun/B54-avionica-y-software-critico-espacial.md)–[`B54-C20`](../../tronco-comun/B54-avionica-y-software-critico-espacial.md) (2 clases) | Diseñar la arquitectura del computador de vuelo y su verificación. |  |
| 18 | Tronco común | obligatoria | **Comunicaciones**<br>[`B55-C01`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md)–[`B55-C12`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md) (12 clases)<br>[`B55-C14`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md)–[`B55-C15`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md) (2 clases)<br>[`B55-C19`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md)–[`B55-C20`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md) (2 clases) | Cerrar un presupuesto de enlace y definir la estación terrena. |  |
| 19 | Tronco común | obligatoria | **Integración y ensayos**<br>[`B56-C01`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md)–[`B56-C20`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) (20 clases) | Planificar integración, ensayos y calificación con evidencia trazable. |  |
| 20 | Tronco común | recomendada | **Operaciones de misión**<br>[`B57-C02`](../../tronco-comun/B57-control-y-operacion-de-misiones-espaciales.md) Concepto de operaciones de misión<br>[`B57-C04`](../../tronco-comun/B57-control-y-operacion-de-misiones-espaciales.md)–[`B57-C09`](../../tronco-comun/B57-control-y-operacion-de-misiones-espaciales.md) (6 clases)<br>[`B57-C13`](../../tronco-comun/B57-control-y-operacion-de-misiones-espaciales.md)–[`B57-C14`](../../tronco-comun/B57-control-y-operacion-de-misiones-espaciales.md) (2 clases)<br>[`B57-C18`](../../tronco-comun/B57-control-y-operacion-de-misiones-espaciales.md) Fin de vida y disposición orbital<br>[`B57-C20`](../../tronco-comun/B57-control-y-operacion-de-misiones-espaciales.md) Simulación de jornada de control de misión | Escribir el concepto de operaciones y los procedimientos de contingencia. |  |
| 21 | Ruta | obligatoria | **Arquitectura de misión satelital**<br>[`B55-C17`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md) Constelaciones y cobertura<br>[`R12-M01-C17`](R12-M01-arquitectura-de-mision-satelital.md)–[`R12-M01-C18`](R12-M01-arquitectura-de-mision-satelital.md) (2 clases) | Cubrir los temas de este módulo que aún no se habían visto en el tronco, con la aplicación concreta al satélite. | Módulo R12-M01: las clases del tronco ya cursadas antes se listan en la tabla de módulos; los temas nuevos usan los IDs de la ruta como referencia provisional. |
| 22 | Ruta | obligatoria | **Diseño de cargas útiles**<br>[`B28-C02`](../../tronco-comun/B28-detectores-y-adquisicion-astronomica.md)–[`B28-C04`](../../tronco-comun/B28-detectores-y-adquisicion-astronomica.md) (3 clases)<br>[`B28-C06`](../../tronco-comun/B28-detectores-y-adquisicion-astronomica.md) Ruido de lectura<br>[`B28-C17`](../../tronco-comun/B28-detectores-y-adquisicion-astronomica.md) Escala de imagen y muestreo<br>[`B30-C06`](../../tronco-comun/B30-radioastronomia-e-interferometria.md)–[`B30-C07`](../../tronco-comun/B30-radioastronomia-e-interferometria.md) (2 clases)<br>[`B31-C02`](../../tronco-comun/B31-instrumentacion-y-observatorios-espaciales.md) Requisitos de instrumentos orbitales<br>[`B31-C15`](../../tronco-comun/B31-instrumentacion-y-observatorios-espaciales.md)–[`B31-C16`](../../tronco-comun/B31-instrumentacion-y-observatorios-espaciales.md) (2 clases)<br>[`B31-C18`](../../tronco-comun/B31-instrumentacion-y-observatorios-espaciales.md) Downlink de instrumentos científicos<br>[`B57-C16`](../../tronco-comun/B57-control-y-operacion-de-misiones-espaciales.md) Gestión de datos científicos<br>[`R12-M02-C07`](R12-M02-diseno-de-cargas-utiles.md)–[`R12-M02-C10`](R12-M02-diseno-de-cargas-utiles.md) (4 clases) | Cubrir los temas de este módulo que aún no se habían visto en el tronco, con la aplicación concreta al satélite. | Módulo R12-M02: las clases del tronco ya cursadas antes se listan en la tabla de módulos; los temas nuevos usan los IDs de la ruta como referencia provisional. |
| 23 | Ruta | obligatoria | **Plataformas y buses satelitales**<br>[`B50-C13`](../../tronco-comun/B50-estructuras-materiales-y-fabricacion-espacial.md) Mecanismos desplegables<br>[`R12-M03-C01`](R12-M03-plataformas-y-buses-satelitales.md)–[`R12-M03-C02`](R12-M03-plataformas-y-buses-satelitales.md) (2 clases)<br>[`R12-M03-C11`](R12-M03-plataformas-y-buses-satelitales.md)–[`R12-M03-C12`](R12-M03-plataformas-y-buses-satelitales.md) (2 clases)<br>[`R12-M03-C19`](R12-M03-plataformas-y-buses-satelitales.md)–[`R12-M03-C20`](R12-M03-plataformas-y-buses-satelitales.md) (2 clases) | Cubrir los temas de este módulo que aún no se habían visto en el tronco, con la aplicación concreta al satélite. | Módulo R12-M03: las clases del tronco ya cursadas antes se listan en la tabla de módulos; los temas nuevos usan los IDs de la ruta como referencia provisional. |
| 24 | Ruta | obligatoria | **Sistema eléctrico de potencia**<br>[`R12-M04-C11`](R12-M04-sistema-electrico-de-potencia.md)–[`R12-M04-C12`](R12-M04-sistema-electrico-de-potencia.md) (2 clases) | Cubrir los temas de este módulo que aún no se habían visto en el tronco, con la aplicación concreta al satélite. | Módulo R12-M04: las clases del tronco ya cursadas antes se listan en la tabla de módulos; los temas nuevos usan los IDs de la ruta como referencia provisional. |
| 25 | Ruta | obligatoria | **Sistema de comunicaciones satelitales**<br>[`B55-C13`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md) Protocolos para espacio profundo<br>[`B63-C09`](../../tronco-comun/B63-derecho-seguridad-y-geopolitica-espacial.md) Derecho y normas de telecomunicaciones<br>[`R12-M05-C01`](R12-M05-sistema-de-comunicaciones-satelitales.md)–[`R12-M05-C02`](R12-M05-sistema-de-comunicaciones-satelitales.md) (2 clases) | Cubrir los temas de este módulo que aún no se habían visto en el tronco, con la aplicación concreta al satélite. | Módulo R12-M05: las clases del tronco ya cursadas antes se listan en la tabla de módulos; los temas nuevos usan los IDs de la ruta como referencia provisional. |
| 26 | Ruta | obligatoria | **Sistema de determinación y control de actitud**<br>[`R12-M06-C15`](R12-M06-sistema-de-determinacion-y-control-de-actitud.md)–[`R12-M06-C16`](R12-M06-sistema-de-determinacion-y-control-de-actitud.md) (2 clases) | Cubrir los temas de este módulo que aún no se habían visto en el tronco, con la aplicación concreta al satélite. | Módulo R12-M06: las clases del tronco ya cursadas antes se listan en la tabla de módulos; los temas nuevos usan los IDs de la ruta como referencia provisional. |
| 27 | Ruta | obligatoria | **Ingeniería de interfaces y configuración**<br>[`B54-C18`](../../tronco-comun/B54-avionica-y-software-critico-espacial.md) Control de configuración de firmware<br>[`R12-M07-C15`](R12-M07-ingenieria-de-interfaces-y-configuracion.md)–[`R12-M07-C16`](R12-M07-ingenieria-de-interfaces-y-configuracion.md) (2 clases) | Cubrir los temas de este módulo que aún no se habían visto en el tronco, con la aplicación concreta al satélite. | Módulo R12-M07: las clases del tronco ya cursadas antes se listan en la tabla de módulos; los temas nuevos usan los IDs de la ruta como referencia provisional. |

## Dónde vive el contenido de cada módulo de la ruta

Cada módulo de la ruta es una lista de 10 temas. Su contenido pertenece al área y bloque del tronco común que corresponde; cuando el tema aún no existe allí, se propone una clase nueva (ver [ampliación del tronco común](../../../documentacion/AMPLIACION_DEL_TRONCO_COMUN.md)).

### R12-M01 — Arquitectura de misión satelital

| Clases de la ruta | Tema | Contenido en el tronco común |
|---|---|---|
| `R12-M01-C01..C02` | Objetivo del satélite | [`B49-C01`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M01-C03..C04` | Requisitos de servicio | [`B49-C04`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M01-C05..C06` | Órbita y cobertura | [`B41-C07`](../../tronco-comun/B41-mecanica-orbital-fundamental.md), [`B41-C08`](../../tronco-comun/B41-mecanica-orbital-fundamental.md), [`B55-C17`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md) |
| `R12-M01-C07..C08` | Presupuesto de masa | [`B49-C09`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M01-C09..C10` | Presupuesto de energía | [`B49-C10`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M01-C11..C12` | Presupuesto de datos | [`B49-C11`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M01-C13..C14` | Arquitectura de plataforma | [`B49-C07`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M01-C15..C16` | Cargas útiles compatibles | [`B49-C08`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M01-C17..C18` | Redundancia de misión | **Clase nueva propuesta** en A07 · B49: Redundancia y tolerancia a fallos de misión |
| `R12-M01-C19..C20` | Revisión conceptual de diseño | [`B49-C13`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md) |

### R12-M02 — Diseño de cargas útiles

| Clases de la ruta | Tema | Contenido en el tronco común |
|---|---|---|
| `R12-M02-C01..C02` | Objetivos de carga útil | [`B31-C02`](../../tronco-comun/B31-instrumentacion-y-observatorios-espaciales.md) |
| `R12-M02-C03..C04` | Sensores ópticos | [`B28-C02`](../../tronco-comun/B28-detectores-y-adquisicion-astronomica.md), [`B28-C03`](../../tronco-comun/B28-detectores-y-adquisicion-astronomica.md) |
| `R12-M02-C05..C06` | Sensores de radio | [`B30-C06`](../../tronco-comun/B30-radioastronomia-e-interferometria.md), [`B30-C07`](../../tronco-comun/B30-radioastronomia-e-interferometria.md) |
| `R12-M02-C07..C08` | Dosímetros | **Clase nueva propuesta** en A07 · B51: Dosímetros y monitores de radiación a bordo |
| `R12-M02-C09..C10` | Carga útil educativa | **Clase nueva propuesta** en A04 · B31: Diseño de cargas útiles educativas |
| `R12-M02-C11..C12` | Resolución y sensibilidad | [`B28-C04`](../../tronco-comun/B28-detectores-y-adquisicion-astronomica.md), [`B28-C06`](../../tronco-comun/B28-detectores-y-adquisicion-astronomica.md), [`B28-C17`](../../tronco-comun/B28-detectores-y-adquisicion-astronomica.md) |
| `R12-M02-C13..C14` | Masa y energía de instrumento | [`B49-C09`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md), [`B49-C10`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md), [`B51-C20`](../../tronco-comun/B51-gestion-termica-y-entorno-espacial.md) |
| `R12-M02-C15..C16` | Calibración de carga útil | [`B31-C15`](../../tronco-comun/B31-instrumentacion-y-observatorios-espaciales.md), [`B13-C05`](../../tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) |
| `R12-M02-C17..C18` | Flujo de datos científicos | [`B31-C16`](../../tronco-comun/B31-instrumentacion-y-observatorios-espaciales.md), [`B31-C18`](../../tronco-comun/B31-instrumentacion-y-observatorios-espaciales.md), [`B57-C16`](../../tronco-comun/B57-control-y-operacion-de-misiones-espaciales.md) |
| `R12-M02-C19..C20` | Aceptación de carga útil | [`B56-C19`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) |

### R12-M03 — Plataformas y buses satelitales

| Clases de la ruta | Tema | Contenido en el tronco común |
|---|---|---|
| `R12-M03-C01..C02` | CubeSat Unit y dimensiones | **Clase nueva propuesta** en A07 · nuevo: Plataformas de satélites pequeños y CubeSat: Unidad CubeSat, dimensiones y formatos |
| `R12-M03-C03..C04` | Plataforma estructural | [`B50-C20`](../../tronco-comun/B50-estructuras-materiales-y-fabricacion-espacial.md) |
| `R12-M03-C05..C06` | Arquitectura de buses | [`B49-C07`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md), [`B54-C07`](../../tronco-comun/B54-avionica-y-software-critico-espacial.md) |
| `R12-M03-C07..C08` | Mecanismos y desplegables | [`B50-C13`](../../tronco-comun/B50-estructuras-materiales-y-fabricacion-espacial.md) |
| `R12-M03-C09..C10` | Paneles de interfaces | [`B56-C05`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M03-C11..C12` | Componentes comerciales | **Clase nueva propuesta** en A07 · nuevo: Plataformas de satélites pequeños y CubeSat: Componentes comerciales en vuelo: selección y riesgo |
| `R12-M03-C13..C14` | Compatibilidad electromagnética | [`B56-C13`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md), [`B56-C14`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M03-C15..C16` | Diseño térmico de plataforma | [`B51-C01`](../../tronco-comun/B51-gestion-termica-y-entorno-espacial.md), [`B51-C18`](../../tronco-comun/B51-gestion-termica-y-entorno-espacial.md) |
| `R12-M03-C17..C18` | Análisis de compatibilidad | [`B49-C08`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M03-C19..C20` | Selección argumentada de plataforma | **Clase nueva propuesta** en A07 · nuevo: Plataformas de satélites pequeños y CubeSat: Selección y comparación de plataformas |

### R12-M04 — Sistema eléctrico de potencia

| Clases de la ruta | Tema | Contenido en el tronco común |
|---|---|---|
| `R12-M04-C01..C02` | Generación fotovoltaica | [`B52-C02`](../../tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md), [`B52-C03`](../../tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md) |
| `R12-M04-C03..C04` | Baterías de a bordo | [`B52-C05`](../../tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md), [`B52-C06`](../../tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md) |
| `R12-M04-C05..C06` | Regulación de potencia | [`B52-C08`](../../tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md), [`B52-C09`](../../tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md) |
| `R12-M04-C07..C08` | Distribución de buses | [`B52-C07`](../../tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md) |
| `R12-M04-C09..C10` | Protecciones eléctricas | [`B52-C10`](../../tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md), [`B56-C03`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M04-C11..C12` | Estados de bajo consumo | **Clase nueva propuesta** en A07 · B52: Modos de operación y estados de bajo consumo |
| `R12-M04-C13..C14` | Energía en eclipse | [`B52-C04`](../../tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md), [`B52-C13`](../../tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md) |
| `R12-M04-C15..C16` | Dimensionamiento de arreglos | [`B52-C01`](../../tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md), [`B52-C19`](../../tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md) |
| `R12-M04-C17..C18` | Márgenes de potencia | [`B52-C12`](../../tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md) |
| `R12-M04-C19..C20` | Prueba de ciclo eléctrico | [`B52-C20`](../../tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md), [`B56-C16`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) |

### R12-M05 — Sistema de comunicaciones satelitales

| Clases de la ruta | Tema | Contenido en el tronco común |
|---|---|---|
| `R12-M05-C01..C02` | Antenas de CubeSat | **Clase nueva propuesta** en A07 · nuevo: Plataformas de satélites pequeños y CubeSat: Antenas desplegables para satélites pequeños |
| `R12-M05-C03..C04` | Presupuesto de enlace | [`B55-C05`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md), [`B55-C06`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md) |
| `R12-M05-C05..C06` | Radio TT&C | [`B55-C11`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md), [`B55-C12`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md) |
| `R12-M05-C07..C08` | Bandas autorizadas | [`B55-C03`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md), [`B55-C19`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md), [`B63-C09`](../../tronco-comun/B63-derecho-seguridad-y-geopolitica-espacial.md) |
| `R12-M05-C09..C10` | Codificación de datos | [`B55-C08`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md), [`B55-C09`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md) |
| `R12-M05-C11..C12` | Protocolo de comunicación | [`B55-C13`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md) |
| `R12-M05-C13..C14` | Estación terrestre | [`B55-C14`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md) |
| `R12-M05-C15..C16` | Gestión de telemetría | [`B54-C08`](../../tronco-comun/B54-avionica-y-software-critico-espacial.md), [`B57-C06`](../../tronco-comun/B57-control-y-operacion-de-misiones-espaciales.md) |
| `R12-M05-C17..C18` | Análisis de contactos | [`B55-C15`](../../tronco-comun/B55-comunicaciones-y-navegacion-satelital.md), [`B57-C04`](../../tronco-comun/B57-control-y-operacion-de-misiones-espaciales.md) |
| `R12-M05-C19..C20` | Prueba de enlace extremo a extremo | [`B56-C16`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) |

### R12-M06 — Sistema de determinación y control de actitud

| Clases de la ruta | Tema | Contenido en el tronco común |
|---|---|---|
| `R12-M06-C01..C02` | Sensores de actitud | [`B53-C03`](../../tronco-comun/B53-sensores-y-control-de-actitud.md), [`B53-C04`](../../tronco-comun/B53-sensores-y-control-de-actitud.md), [`B53-C05`](../../tronco-comun/B53-sensores-y-control-de-actitud.md), [`B53-C06`](../../tronco-comun/B53-sensores-y-control-de-actitud.md), [`B53-C07`](../../tronco-comun/B53-sensores-y-control-de-actitud.md) |
| `R12-M06-C03..C04` | Dinámica rotacional | [`B53-C01`](../../tronco-comun/B53-sensores-y-control-de-actitud.md), [`B53-C02`](../../tronco-comun/B53-sensores-y-control-de-actitud.md) |
| `R12-M06-C05..C06` | Detumbling | [`B53-C16`](../../tronco-comun/B53-sensores-y-control-de-actitud.md) |
| `R12-M06-C07..C08` | Ruedas de reacción | [`B53-C11`](../../tronco-comun/B53-sensores-y-control-de-actitud.md) |
| `R12-M06-C09..C10` | Magnetopares | [`B53-C12`](../../tronco-comun/B53-sensores-y-control-de-actitud.md) |
| `R12-M06-C11..C12` | Control de apuntamiento | [`B53-C15`](../../tronco-comun/B53-sensores-y-control-de-actitud.md) |
| `R12-M06-C13..C14` | Perturbaciones orbitales | [`B53-C18`](../../tronco-comun/B53-sensores-y-control-de-actitud.md) |
| `R12-M06-C15..C16` | Presupuesto de error | **Clase nueva propuesta** en A07 · B53: Presupuesto de error de apuntamiento |
| `R12-M06-C17..C18` | Modos seguros | [`B54-C11`](../../tronco-comun/B54-avionica-y-software-critico-espacial.md), [`B54-C12`](../../tronco-comun/B54-avionica-y-software-critico-espacial.md) |
| `R12-M06-C19..C20` | Prueba de controlador ADCS | [`B53-C19`](../../tronco-comun/B53-sensores-y-control-de-actitud.md), [`B53-C20`](../../tronco-comun/B53-sensores-y-control-de-actitud.md) |

### R12-M07 — Ingeniería de interfaces y configuración

| Clases de la ruta | Tema | Contenido en el tronco común |
|---|---|---|
| `R12-M07-C01..C02` | Documentos de control de interfaces | [`B56-C05`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md), [`B49-C08`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M07-C03..C04` | Matriz de requisitos | [`B49-C04`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md), [`B49-C05`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M07-C05..C06` | Control de configuración | [`B49-C15`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md), [`B54-C18`](../../tronco-comun/B54-avionica-y-software-critico-espacial.md) |
| `R12-M07-C07..C08` | Gestión de masas | [`B49-C09`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M07-C09..C10` | Gestión térmica | [`B51-C20`](../../tronco-comun/B51-gestion-termica-y-entorno-espacial.md), [`B51-C18`](../../tronco-comun/B51-gestion-termica-y-entorno-espacial.md) |
| `R12-M07-C11..C12` | Interfaces mecánicas | [`B56-C06`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M07-C13..C14` | Interfaces eléctricas | [`B56-C07`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M07-C15..C16` | Interfaces de software | **Clase nueva propuesta** en A07 · B54: Interfaces y documentos de control de software de vuelo |
| `R12-M07-C17..C18` | Gestión de cambios | [`B49-C15`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M07-C19..C20` | Revisión de coherencia integral | [`B49-C14`](../../tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md) |

### R12-M08 — Integración y calificación de CubeSat

| Clases de la ruta | Tema | Contenido en el tronco común |
|---|---|---|
| `R12-M08-C01..C02` | Plan de ensamblaje | [`B56-C01`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M08-C03..C04` | Procedimientos de integración | [`B56-C06`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md), [`B56-C07`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md), [`B56-C08`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M08-C05..C06` | Control ESD | [`B56-C02`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md), [`B56-C03`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M08-C07..C08` | Pruebas de subsistemas | [`B56-C08`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M08-C09..C10` | Pruebas funcionales | [`B56-C16`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M08-C11..C12` | Vibración y choque | [`B56-C09`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md), [`B56-C10`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M08-C13..C14` | Vacío térmico | [`B56-C12`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md), [`B51-C19`](../../tronco-comun/B51-gestion-termica-y-entorno-espacial.md) |
| `R12-M08-C15..C16` | Trazabilidad de evidencia | [`B56-C18`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M08-C17..C18` | Resolución de no conformidades | [`B56-C17`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M08-C19..C20` | Revisión de aceptación de CubeSat | [`B56-C19`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md), [`B56-C20`](../../tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) |

## Huecos detectados en el catálogo

Temas que este rol necesita y que el catálogo `0.1.0` no cubre. Alimentan la [ampliación del tronco común](../../../documentacion/AMPLIACION_DEL_TRONCO_COMUN.md); no cambian ningún ID existente.

- **Interfaz con el lanzador, despliegue y papeles de integración de lanzamiento.** Ningún título del catálogo trata el despliegue desde el lanzador ni la documentación de interfaz con el proveedor de lanzamiento; B50-C01 cubre solo el entorno mecánico. *Propuesta:* clases nuevas en B56 o módulo nuevo de R12.
- **Normas y estándares de ingeniería espacial con versión y jurisdicción.** No hay clases sobre estándares de ingeniería espacial (por ejemplo de agencias o ECSS); R13-M07-C17 menciona normas de aseguramiento solo para software. *Propuesta:* bloque nuevo transversal de estándares y aseguramiento del producto.

[⬅️ Índice de la ruta](INDICE.md)
