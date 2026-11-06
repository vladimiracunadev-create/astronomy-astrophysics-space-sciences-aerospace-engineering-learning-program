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
| 5 | Tronco común | obligatoria | **Álgebra lineal, rotaciones y marcos**<br>[`B10-C01`](../../clases/B10/B10-C01-espacios-vectoriales/CLASE.md)–[`B10-C20`](../../tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) (20 clases) | Representar la orientación del satélite con matrices y cuaterniones y cambiar de marco. | C12 a C16 son el núcleo de actitud. |
| 6 | Tronco común | obligatoria | **Simulación numérica**<br>[`B11-C01`](../../clases/B11/B11-C01-ecuaciones-diferenciales-ordinarias/CLASE.md)–[`B11-C11`](../../clases/B11/B11-C11-metodos-simplecticos/CLASE.md) (11 clases)<br>[`B11-C19`](../../tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md)–[`B11-C20`](../../tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) (2 clases) | Integrar numéricamente el movimiento y comprobar error y convergencia. | C12 a C18 se omiten salvo necesidad. |
| 7 | Tronco común | obligatoria | **Incertidumbre y metrología**<br>[`B12-C07`](../../clases/B12/B12-C07-estimacion-de-parametros/CLASE.md) Estimación de parámetros<br>[`B12-C10`](../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) Regresión lineal y no lineal<br>[`B12-C14`](../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) Simulación Monte Carlo<br>[`B12-C16`](../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md)–[`B12-C18`](../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) (3 clases)<br>[`B13-C01`](../../clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md)–[`B13-C05`](../../clases/B13/B13-C05-calibracion-instrumental/CLASE.md) (5 clases)<br>[`B13-C12`](../../clases/B13/B13-C12-incertidumbre-expandida/CLASE.md)–[`B13-C13`](../../tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) (2 clases)<br>[`B13-C19`](../../tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md)–[`B13-C20`](../../tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) (2 clases) | Propagar incertidumbres y justificar márgenes de diseño. | B12-C20 se integra en el informe del paso final. |
| 8 | Tronco común | recomendada | **Datos reproducibles**<br>[`B14-C04`](../../clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md) Unidades y constantes con Astropy<br>[`B14-C09`](../../clases/B14/B14-C09-jupyter-y-experimentos-reproducibles/CLASE.md) Jupyter y experimentos reproducibles<br>[`B14-C10`](../../clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md) Pruebas de regresión numérica<br>[`B14-C12`](../../clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md) Ejecución reproducible con uv<br>[`B14-C17`](../../tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) Contenedores y ambientes científicos | Mantener análisis y simulaciones reproducibles. |  |
| 9 | Tronco común | obligatoria | **Control automático**<br>[`B16-C01`](../../clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md)–[`B16-C14`](../../tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) (14 clases)<br>[`B16-C18`](../../tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md)–[`B16-C20`](../../tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) (3 clases) | Analizar la estabilidad de un lazo de control y sintonizar un controlador de actitud. |  |
| 10 | Tronco común | obligatoria | **Órbita del satélite**<br>[`B71-C01`](../../tronco-comun/B71-mecanica-orbital-fundamental.md)–[`B71-C20`](../../tronco-comun/B71-mecanica-orbital-fundamental.md) (20 clases) | Describir la órbita, su período y su geometría y propagarla con un modelo verificable. | La perturbación orbital (B72) se estudia cuando el rol lo requiera. |
| 11 | Tronco común | recomendada | **Perturbaciones orbitales**<br>[`B72-C01`](../../tronco-comun/B72-perturbaciones-y-evolucion-de-orbitas.md)–[`B72-C20`](../../tronco-comun/B72-perturbaciones-y-evolucion-de-orbitas.md) (20 clases) | Estimar cuánto deriva la órbita por arrastre y J2 durante la vida de la misión. |  |
| 12 | Tronco común | obligatoria | **Ingeniería de sistemas y diseño de misiones**<br>[`B83-C01`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md)–[`B83-C20`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) (20 clases) | Pasar de una necesidad de misión a requisitos verificables, presupuestos y revisiones. | Es el eje del rol: las clases de la ruta lo profundizan. |
| 13 | Tronco común | obligatoria | **Estructuras y materiales**<br>[`B84-C01`](../../tronco-comun/B84-estructuras-materiales-y-fabricacion-espacial.md) Entorno mecánico de lanzamiento<br>[`B84-C05`](../../tronco-comun/B84-estructuras-materiales-y-fabricacion-espacial.md)–[`B84-C07`](../../tronco-comun/B84-estructuras-materiales-y-fabricacion-espacial.md) (3 clases)<br>[`B84-C09`](../../tronco-comun/B84-estructuras-materiales-y-fabricacion-espacial.md)–[`B84-C12`](../../tronco-comun/B84-estructuras-materiales-y-fabricacion-espacial.md) (4 clases)<br>[`B84-C20`](../../tronco-comun/B84-estructuras-materiales-y-fabricacion-espacial.md) Diseño estructural de plataforma satelital | Seleccionar materiales y verificar que la estructura resiste el lanzamiento. |  |
| 14 | Tronco común | obligatoria | **Térmica y entorno espacial**<br>[`B85-C01`](../../tronco-comun/B85-gestion-termica-y-entorno-espacial.md)–[`B85-C08`](../../tronco-comun/B85-gestion-termica-y-entorno-espacial.md) (8 clases)<br>[`B85-C11`](../../tronco-comun/B85-gestion-termica-y-entorno-espacial.md)–[`B85-C12`](../../tronco-comun/B85-gestion-termica-y-entorno-espacial.md) (2 clases)<br>[`B85-C18`](../../tronco-comun/B85-gestion-termica-y-entorno-espacial.md)–[`B85-C20`](../../tronco-comun/B85-gestion-termica-y-entorno-espacial.md) (3 clases) | Armar un balance térmico y definir un control térmico pasivo o activo. |  |
| 15 | Tronco común | obligatoria | **Potencia**<br>[`B86-C01`](../../tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md)–[`B86-C14`](../../tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md) (14 clases)<br>[`B86-C19`](../../tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md)–[`B86-C20`](../../tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md) (2 clases) | Dimensionar paneles y batería para el ciclo orbital. |  |
| 16 | Tronco común | obligatoria | **Actitud y control**<br>[`B87-C01`](../../tronco-comun/B87-sensores-y-control-de-actitud.md)–[`B87-C20`](../../tronco-comun/B87-sensores-y-control-de-actitud.md) (20 clases) | Elegir sensores y actuadores y verificar el control de actitud. |  |
| 17 | Tronco común | obligatoria | **Aviónica y software de vuelo**<br>[`B88-C01`](../../tronco-comun/B88-avionica-y-software-critico-espacial.md)–[`B88-C09`](../../tronco-comun/B88-avionica-y-software-critico-espacial.md) (9 clases)<br>[`B88-C11`](../../tronco-comun/B88-avionica-y-software-critico-espacial.md)–[`B88-C12`](../../tronco-comun/B88-avionica-y-software-critico-espacial.md) (2 clases)<br>[`B88-C14`](../../tronco-comun/B88-avionica-y-software-critico-espacial.md) Pruebas de software embarcado<br>[`B88-C19`](../../tronco-comun/B88-avionica-y-software-critico-espacial.md)–[`B88-C20`](../../tronco-comun/B88-avionica-y-software-critico-espacial.md) (2 clases) | Diseñar la arquitectura del computador de vuelo y su verificación. |  |
| 18 | Tronco común | obligatoria | **Comunicaciones**<br>[`B89-C01`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md)–[`B89-C12`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) (12 clases)<br>[`B89-C14`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md)–[`B89-C15`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) (2 clases)<br>[`B89-C19`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md)–[`B89-C20`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) (2 clases) | Cerrar un presupuesto de enlace y definir la estación terrena. |  |
| 19 | Tronco común | obligatoria | **Integración y ensayos**<br>[`B90-C01`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md)–[`B90-C20`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) (20 clases) | Planificar integración, ensayos y calificación con evidencia trazable. |  |
| 20 | Tronco común | recomendada | **Operaciones de misión**<br>[`B96-C02`](../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) Concepto de operaciones de misión<br>[`B96-C04`](../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md)–[`B96-C09`](../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) (6 clases)<br>[`B96-C13`](../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md)–[`B96-C14`](../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) (2 clases)<br>[`B96-C18`](../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) Fin de vida y disposición orbital<br>[`B96-C20`](../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) Simulación de jornada de control de misión | Escribir el concepto de operaciones y los procedimientos de contingencia. |  |
| 21 | Ruta | obligatoria | **Arquitectura de misión satelital**<br>[`B89-C17`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) Constelaciones y cobertura<br>[`R12-M01-C17`](R12-M01-arquitectura-de-mision-satelital.md)–[`R12-M01-C18`](R12-M01-arquitectura-de-mision-satelital.md) (2 clases) | Cubrir los temas de este módulo que aún no se habían visto en el tronco, con la aplicación concreta al satélite. | Módulo R12-M01: las clases del tronco ya cursadas antes se listan en la tabla de módulos; los temas nuevos usan los IDs de la ruta como referencia provisional. |
| 22 | Ruta | obligatoria | **Diseño de cargas útiles**<br>[`B44-C02`](../../tronco-comun/B44-detectores-y-adquisicion-astronomica.md)–[`B44-C04`](../../tronco-comun/B44-detectores-y-adquisicion-astronomica.md) (3 clases)<br>[`B44-C06`](../../tronco-comun/B44-detectores-y-adquisicion-astronomica.md) Ruido de lectura<br>[`B44-C17`](../../tronco-comun/B44-detectores-y-adquisicion-astronomica.md) Escala de imagen y muestreo<br>[`B46-C06`](../../tronco-comun/B46-radioastronomia-e-interferometria.md)–[`B46-C07`](../../tronco-comun/B46-radioastronomia-e-interferometria.md) (2 clases)<br>[`B47-C02`](../../tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md) Requisitos de instrumentos orbitales<br>[`B47-C15`](../../tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md)–[`B47-C16`](../../tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md) (2 clases)<br>[`B47-C18`](../../tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md) Downlink de instrumentos científicos<br>[`B96-C16`](../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) Gestión de datos científicos<br>[`R12-M02-C07`](R12-M02-diseno-de-cargas-utiles.md)–[`R12-M02-C10`](R12-M02-diseno-de-cargas-utiles.md) (4 clases) | Cubrir los temas de este módulo que aún no se habían visto en el tronco, con la aplicación concreta al satélite. | Módulo R12-M02: las clases del tronco ya cursadas antes se listan en la tabla de módulos; los temas nuevos usan los IDs de la ruta como referencia provisional. |
| 23 | Ruta | obligatoria | **Plataformas y buses satelitales**<br>[`B84-C13`](../../tronco-comun/B84-estructuras-materiales-y-fabricacion-espacial.md) Mecanismos desplegables<br>[`R12-M03-C01`](R12-M03-plataformas-y-buses-satelitales.md)–[`R12-M03-C02`](R12-M03-plataformas-y-buses-satelitales.md) (2 clases)<br>[`R12-M03-C11`](R12-M03-plataformas-y-buses-satelitales.md)–[`R12-M03-C12`](R12-M03-plataformas-y-buses-satelitales.md) (2 clases)<br>[`R12-M03-C19`](R12-M03-plataformas-y-buses-satelitales.md)–[`R12-M03-C20`](R12-M03-plataformas-y-buses-satelitales.md) (2 clases) | Cubrir los temas de este módulo que aún no se habían visto en el tronco, con la aplicación concreta al satélite. | Módulo R12-M03: las clases del tronco ya cursadas antes se listan en la tabla de módulos; los temas nuevos usan los IDs de la ruta como referencia provisional. |
| 24 | Ruta | obligatoria | **Sistema eléctrico de potencia**<br>[`R12-M04-C11`](R12-M04-sistema-electrico-de-potencia.md)–[`R12-M04-C12`](R12-M04-sistema-electrico-de-potencia.md) (2 clases) | Cubrir los temas de este módulo que aún no se habían visto en el tronco, con la aplicación concreta al satélite. | Módulo R12-M04: las clases del tronco ya cursadas antes se listan en la tabla de módulos; los temas nuevos usan los IDs de la ruta como referencia provisional. |
| 25 | Ruta | obligatoria | **Sistema de comunicaciones satelitales**<br>[`B89-C13`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) Protocolos para espacio profundo<br>[`B119-C09`](../../tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md) Derecho y normas de telecomunicaciones<br>[`R12-M05-C01`](R12-M05-sistema-de-comunicaciones-satelitales.md)–[`R12-M05-C02`](R12-M05-sistema-de-comunicaciones-satelitales.md) (2 clases) | Cubrir los temas de este módulo que aún no se habían visto en el tronco, con la aplicación concreta al satélite. | Módulo R12-M05: las clases del tronco ya cursadas antes se listan en la tabla de módulos; los temas nuevos usan los IDs de la ruta como referencia provisional. |
| 26 | Ruta | obligatoria | **Sistema de determinación y control de actitud**<br>[`R12-M06-C15`](R12-M06-sistema-de-determinacion-y-control-de-actitud.md)–[`R12-M06-C16`](R12-M06-sistema-de-determinacion-y-control-de-actitud.md) (2 clases) | Cubrir los temas de este módulo que aún no se habían visto en el tronco, con la aplicación concreta al satélite. | Módulo R12-M06: las clases del tronco ya cursadas antes se listan en la tabla de módulos; los temas nuevos usan los IDs de la ruta como referencia provisional. |
| 27 | Ruta | obligatoria | **Ingeniería de interfaces y configuración**<br>[`B88-C18`](../../tronco-comun/B88-avionica-y-software-critico-espacial.md) Control de configuración de firmware<br>[`R12-M07-C15`](R12-M07-ingenieria-de-interfaces-y-configuracion.md)–[`R12-M07-C16`](R12-M07-ingenieria-de-interfaces-y-configuracion.md) (2 clases) | Cubrir los temas de este módulo que aún no se habían visto en el tronco, con la aplicación concreta al satélite. | Módulo R12-M07: las clases del tronco ya cursadas antes se listan en la tabla de módulos; los temas nuevos usan los IDs de la ruta como referencia provisional. |

## Dónde vive el contenido de cada módulo de la ruta

Cada módulo de la ruta es una lista de 10 temas. Su contenido pertenece al área y bloque del tronco común que corresponde; cuando el tema aún no existe allí, se propone una clase nueva (ver [ampliación del tronco común](../../../documentacion/AMPLIACION_DEL_TRONCO_COMUN.md)).

### R12-M01 — Arquitectura de misión satelital

| Clases de la ruta | Tema | Contenido en el tronco común |
|---|---|---|
| `R12-M01-C01..C02` | Objetivo del satélite | [`B83-C01`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M01-C03..C04` | Requisitos de servicio | [`B83-C04`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M01-C05..C06` | Órbita y cobertura | [`B71-C07`](../../tronco-comun/B71-mecanica-orbital-fundamental.md), [`B71-C08`](../../tronco-comun/B71-mecanica-orbital-fundamental.md), [`B89-C17`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) |
| `R12-M01-C07..C08` | Presupuesto de masa | [`B83-C09`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M01-C09..C10` | Presupuesto de energía | [`B83-C10`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M01-C11..C12` | Presupuesto de datos | [`B83-C11`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M01-C13..C14` | Arquitectura de plataforma | [`B83-C07`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M01-C15..C16` | Cargas útiles compatibles | [`B83-C08`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M01-C17..C18` | Redundancia de misión | **Clase nueva propuesta** en A07 · B83: Redundancia y tolerancia a fallos de misión |
| `R12-M01-C19..C20` | Revisión conceptual de diseño | [`B83-C13`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) |

### R12-M02 — Diseño de cargas útiles

| Clases de la ruta | Tema | Contenido en el tronco común |
|---|---|---|
| `R12-M02-C01..C02` | Objetivos de carga útil | [`B47-C02`](../../tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md) |
| `R12-M02-C03..C04` | Sensores ópticos | [`B44-C02`](../../tronco-comun/B44-detectores-y-adquisicion-astronomica.md), [`B44-C03`](../../tronco-comun/B44-detectores-y-adquisicion-astronomica.md) |
| `R12-M02-C05..C06` | Sensores de radio | [`B46-C06`](../../tronco-comun/B46-radioastronomia-e-interferometria.md), [`B46-C07`](../../tronco-comun/B46-radioastronomia-e-interferometria.md) |
| `R12-M02-C07..C08` | Dosímetros | **Clase nueva propuesta** en A07 · B85: Dosímetros y monitores de radiación a bordo |
| `R12-M02-C09..C10` | Carga útil educativa | **Clase nueva propuesta** en A04 · B47: Diseño de cargas útiles educativas |
| `R12-M02-C11..C12` | Resolución y sensibilidad | [`B44-C04`](../../tronco-comun/B44-detectores-y-adquisicion-astronomica.md), [`B44-C06`](../../tronco-comun/B44-detectores-y-adquisicion-astronomica.md), [`B44-C17`](../../tronco-comun/B44-detectores-y-adquisicion-astronomica.md) |
| `R12-M02-C13..C14` | Masa y energía de instrumento | [`B83-C09`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md), [`B83-C10`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md), [`B85-C20`](../../tronco-comun/B85-gestion-termica-y-entorno-espacial.md) |
| `R12-M02-C15..C16` | Calibración de carga útil | [`B47-C15`](../../tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md), [`B13-C05`](../../clases/B13/B13-C05-calibracion-instrumental/CLASE.md) |
| `R12-M02-C17..C18` | Flujo de datos científicos | [`B47-C16`](../../tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md), [`B47-C18`](../../tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md), [`B96-C16`](../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) |
| `R12-M02-C19..C20` | Aceptación de carga útil | [`B90-C19`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) |

### R12-M03 — Plataformas y buses satelitales

| Clases de la ruta | Tema | Contenido en el tronco común |
|---|---|---|
| `R12-M03-C01..C02` | CubeSat Unit y dimensiones | **Clase nueva propuesta** en A07 · nuevo: Plataformas de satélites pequeños y CubeSat: Unidad CubeSat, dimensiones y formatos |
| `R12-M03-C03..C04` | Plataforma estructural | [`B84-C20`](../../tronco-comun/B84-estructuras-materiales-y-fabricacion-espacial.md) |
| `R12-M03-C05..C06` | Arquitectura de buses | [`B83-C07`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md), [`B88-C07`](../../tronco-comun/B88-avionica-y-software-critico-espacial.md) |
| `R12-M03-C07..C08` | Mecanismos y desplegables | [`B84-C13`](../../tronco-comun/B84-estructuras-materiales-y-fabricacion-espacial.md) |
| `R12-M03-C09..C10` | Paneles de interfaces | [`B90-C05`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M03-C11..C12` | Componentes comerciales | **Clase nueva propuesta** en A07 · nuevo: Plataformas de satélites pequeños y CubeSat: Componentes comerciales en vuelo: selección y riesgo |
| `R12-M03-C13..C14` | Compatibilidad electromagnética | [`B90-C13`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md), [`B90-C14`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M03-C15..C16` | Diseño térmico de plataforma | [`B85-C01`](../../tronco-comun/B85-gestion-termica-y-entorno-espacial.md), [`B85-C18`](../../tronco-comun/B85-gestion-termica-y-entorno-espacial.md) |
| `R12-M03-C17..C18` | Análisis de compatibilidad | [`B83-C08`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M03-C19..C20` | Selección argumentada de plataforma | **Clase nueva propuesta** en A07 · nuevo: Plataformas de satélites pequeños y CubeSat: Selección y comparación de plataformas |

### R12-M04 — Sistema eléctrico de potencia

| Clases de la ruta | Tema | Contenido en el tronco común |
|---|---|---|
| `R12-M04-C01..C02` | Generación fotovoltaica | [`B86-C02`](../../tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md), [`B86-C03`](../../tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md) |
| `R12-M04-C03..C04` | Baterías de a bordo | [`B86-C05`](../../tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md), [`B86-C06`](../../tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md) |
| `R12-M04-C05..C06` | Regulación de potencia | [`B86-C08`](../../tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md), [`B86-C09`](../../tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md) |
| `R12-M04-C07..C08` | Distribución de buses | [`B86-C07`](../../tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md) |
| `R12-M04-C09..C10` | Protecciones eléctricas | [`B86-C10`](../../tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md), [`B90-C03`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M04-C11..C12` | Estados de bajo consumo | **Clase nueva propuesta** en A07 · B86: Modos de operación y estados de bajo consumo |
| `R12-M04-C13..C14` | Energía en eclipse | [`B86-C04`](../../tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md), [`B86-C13`](../../tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md) |
| `R12-M04-C15..C16` | Dimensionamiento de arreglos | [`B86-C01`](../../tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md), [`B86-C19`](../../tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md) |
| `R12-M04-C17..C18` | Márgenes de potencia | [`B86-C12`](../../tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md) |
| `R12-M04-C19..C20` | Prueba de ciclo eléctrico | [`B86-C20`](../../tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md), [`B90-C16`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) |

### R12-M05 — Sistema de comunicaciones satelitales

| Clases de la ruta | Tema | Contenido en el tronco común |
|---|---|---|
| `R12-M05-C01..C02` | Antenas de CubeSat | **Clase nueva propuesta** en A07 · nuevo: Plataformas de satélites pequeños y CubeSat: Antenas desplegables para satélites pequeños |
| `R12-M05-C03..C04` | Presupuesto de enlace | [`B89-C05`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md), [`B89-C06`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) |
| `R12-M05-C05..C06` | Radio TT&C | [`B89-C11`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md), [`B89-C12`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) |
| `R12-M05-C07..C08` | Bandas autorizadas | [`B89-C03`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md), [`B89-C19`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md), [`B119-C09`](../../tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md) |
| `R12-M05-C09..C10` | Codificación de datos | [`B89-C08`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md), [`B89-C09`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) |
| `R12-M05-C11..C12` | Protocolo de comunicación | [`B89-C13`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) |
| `R12-M05-C13..C14` | Estación terrestre | [`B89-C14`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) |
| `R12-M05-C15..C16` | Gestión de telemetría | [`B88-C08`](../../tronco-comun/B88-avionica-y-software-critico-espacial.md), [`B96-C06`](../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) |
| `R12-M05-C17..C18` | Análisis de contactos | [`B89-C15`](../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md), [`B96-C04`](../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) |
| `R12-M05-C19..C20` | Prueba de enlace extremo a extremo | [`B90-C16`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) |

### R12-M06 — Sistema de determinación y control de actitud

| Clases de la ruta | Tema | Contenido en el tronco común |
|---|---|---|
| `R12-M06-C01..C02` | Sensores de actitud | [`B87-C03`](../../tronco-comun/B87-sensores-y-control-de-actitud.md), [`B87-C04`](../../tronco-comun/B87-sensores-y-control-de-actitud.md), [`B87-C05`](../../tronco-comun/B87-sensores-y-control-de-actitud.md), [`B87-C06`](../../tronco-comun/B87-sensores-y-control-de-actitud.md), [`B87-C07`](../../tronco-comun/B87-sensores-y-control-de-actitud.md) |
| `R12-M06-C03..C04` | Dinámica rotacional | [`B87-C01`](../../tronco-comun/B87-sensores-y-control-de-actitud.md), [`B87-C02`](../../tronco-comun/B87-sensores-y-control-de-actitud.md) |
| `R12-M06-C05..C06` | Detumbling | [`B87-C16`](../../tronco-comun/B87-sensores-y-control-de-actitud.md) |
| `R12-M06-C07..C08` | Ruedas de reacción | [`B87-C11`](../../tronco-comun/B87-sensores-y-control-de-actitud.md) |
| `R12-M06-C09..C10` | Magnetopares | [`B87-C12`](../../tronco-comun/B87-sensores-y-control-de-actitud.md) |
| `R12-M06-C11..C12` | Control de apuntamiento | [`B87-C15`](../../tronco-comun/B87-sensores-y-control-de-actitud.md) |
| `R12-M06-C13..C14` | Perturbaciones orbitales | [`B87-C18`](../../tronco-comun/B87-sensores-y-control-de-actitud.md) |
| `R12-M06-C15..C16` | Presupuesto de error | **Clase nueva propuesta** en A07 · B87: Presupuesto de error de apuntamiento |
| `R12-M06-C17..C18` | Modos seguros | [`B88-C11`](../../tronco-comun/B88-avionica-y-software-critico-espacial.md), [`B88-C12`](../../tronco-comun/B88-avionica-y-software-critico-espacial.md) |
| `R12-M06-C19..C20` | Prueba de controlador ADCS | [`B87-C19`](../../tronco-comun/B87-sensores-y-control-de-actitud.md), [`B87-C20`](../../tronco-comun/B87-sensores-y-control-de-actitud.md) |

### R12-M07 — Ingeniería de interfaces y configuración

| Clases de la ruta | Tema | Contenido en el tronco común |
|---|---|---|
| `R12-M07-C01..C02` | Documentos de control de interfaces | [`B90-C05`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md), [`B83-C08`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M07-C03..C04` | Matriz de requisitos | [`B83-C04`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md), [`B83-C05`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M07-C05..C06` | Control de configuración | [`B83-C15`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md), [`B88-C18`](../../tronco-comun/B88-avionica-y-software-critico-espacial.md) |
| `R12-M07-C07..C08` | Gestión de masas | [`B83-C09`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M07-C09..C10` | Gestión térmica | [`B85-C20`](../../tronco-comun/B85-gestion-termica-y-entorno-espacial.md), [`B85-C18`](../../tronco-comun/B85-gestion-termica-y-entorno-espacial.md) |
| `R12-M07-C11..C12` | Interfaces mecánicas | [`B90-C06`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M07-C13..C14` | Interfaces eléctricas | [`B90-C07`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M07-C15..C16` | Interfaces de software | **Clase nueva propuesta** en A07 · B88: Interfaces y documentos de control de software de vuelo |
| `R12-M07-C17..C18` | Gestión de cambios | [`B83-C15`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) |
| `R12-M07-C19..C20` | Revisión de coherencia integral | [`B83-C14`](../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) |

### R12-M08 — Integración y calificación de CubeSat

| Clases de la ruta | Tema | Contenido en el tronco común |
|---|---|---|
| `R12-M08-C01..C02` | Plan de ensamblaje | [`B90-C01`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M08-C03..C04` | Procedimientos de integración | [`B90-C06`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md), [`B90-C07`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md), [`B90-C08`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M08-C05..C06` | Control ESD | [`B90-C02`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md), [`B90-C03`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M08-C07..C08` | Pruebas de subsistemas | [`B90-C08`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M08-C09..C10` | Pruebas funcionales | [`B90-C16`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M08-C11..C12` | Vibración y choque | [`B90-C09`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md), [`B90-C10`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M08-C13..C14` | Vacío térmico | [`B90-C12`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md), [`B85-C19`](../../tronco-comun/B85-gestion-termica-y-entorno-espacial.md) |
| `R12-M08-C15..C16` | Trazabilidad de evidencia | [`B90-C18`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M08-C17..C18` | Resolución de no conformidades | [`B90-C17`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) |
| `R12-M08-C19..C20` | Revisión de aceptación de CubeSat | [`B90-C19`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md), [`B90-C20`](../../tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) |

## Huecos detectados en el catálogo

Temas que este rol necesita y que el catálogo `0.1.0` no cubre. Alimentan la [ampliación del tronco común](../../../documentacion/AMPLIACION_DEL_TRONCO_COMUN.md); no cambian ningún ID existente.

- **Interfaz con el lanzador, despliegue y papeles de integración de lanzamiento.** Ningún título del catálogo trata el despliegue desde el lanzador ni la documentación de interfaz con el proveedor de lanzamiento; B84-C01 cubre solo el entorno mecánico. *Propuesta:* clases nuevas en B90 o módulo nuevo de R12.
- **Normas y estándares de ingeniería espacial con versión y jurisdicción.** No hay clases sobre estándares de ingeniería espacial (por ejemplo de agencias o ECSS); R13-M07-C17 menciona normas de aseguramiento solo para software. *Propuesta:* bloque nuevo transversal de estándares y aseguramiento del producto.

[⬅️ Índice de la ruta](INDICE.md)
