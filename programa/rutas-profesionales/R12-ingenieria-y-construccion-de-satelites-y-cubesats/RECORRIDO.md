# R12 — Recorrido del rol: Ingeniero/a de sistemas y subsistemas de satélites y CubeSats

> Diseña, integra y califica un satélite pequeño: parte de una necesidad de misión, reparte masa, energía y datos entre subsistemas, y demuestra con ensayos que el conjunto cumple sus requisitos.

- **Decide:** Qué arquitectura y qué compromisos entre subsistemas cumplen los requisitos con los presupuestos de masa, potencia, datos y riesgo disponibles.
- **Entrega:** Presupuestos de misión, especificaciones de interfaz, modelo de diseño trazable a requisitos y plan y evidencias de integración y calificación.

**Alcance del recorrido:** 493 clases (333 del tronco común y 160 de la ruta); 457 obligatorias. No es una titulación: el avance se demuestra con evidencias, no cursando en orden por obligación.

## Pasos en orden

| # | Fase | Tipo | Clases | Capacidad que aporta | Nota |
|---:|---|---|---|---|---|
| 1 | Fundamentos | obligatoria | **Unidades, incertidumbre y fuentes**<br>`B01-C04` Espacio y tiempo en ciencia<br>`B01-C08` Mediciones y unidades astronómicas<br>`B01-C18` Incertidumbre y errores elementales<br>`B01-C19` Fuentes confiables y desinformación espacial | Reportar cualquier cifra de diseño con unidad, marco, incertidumbre y fuente. | Omitible si aprueba el diagnóstico de unidades y marcos. |
| 2 | Fundamentos | obligatoria | **Matemática y geometría operativas**<br>`B03-C01`–`C20` (20 clases)<br>`B04-C01`–`C20` (20 clases) | Resolver los cálculos algebraicos, trigonométricos y vectoriales de un presupuesto o de una orientación. | Omitible si aprueba el diagnóstico de matemática. |
| 3 | Fundamentos | obligatoria | **Física del entorno espacial**<br>`B05-C01`–`C20` (20 clases) | Aplicar mecánica, energía, calor y electromagnetismo a un satélite. | Omitible si aprueba el diagnóstico de física. |
| 4 | Fundamentos | obligatoria | **Programación científica**<br>`B07-C01`–`C20` (20 clases) | Escribir y probar el código de un modelo de subsistema. | Omitible si demuestra un proyecto en Python con pruebas. |
| 5 | Tronco común | obligatoria | **Álgebra lineal, rotaciones y marcos**<br>`B10-C01`–`C20` (20 clases) | Representar la orientación del satélite con matrices y cuaterniones y cambiar de marco. | C12 a C16 son el núcleo de actitud. |
| 6 | Tronco común | obligatoria | **Simulación numérica**<br>`B11-C01`–`C11` (11 clases)<br>`B11-C19`–`C20` (2 clases) | Integrar numéricamente el movimiento y comprobar error y convergencia. | C12 a C18 se omiten salvo necesidad. |
| 7 | Tronco común | obligatoria | **Incertidumbre y metrología**<br>`B12-C07` Estimación de parámetros<br>`B12-C10` Regresión lineal y no lineal<br>`B12-C14` Simulación Monte Carlo<br>`B12-C16`–`C18` (3 clases)<br>`B13-C01`–`C05` (5 clases)<br>`B13-C12`–`C13` (2 clases)<br>`B13-C19`–`C20` (2 clases) | Propagar incertidumbres y justificar márgenes de diseño. | B12-C20 se integra en el informe del paso final. |
| 8 | Tronco común | recomendada | **Datos reproducibles**<br>`B14-C04` Unidades y constantes con Astropy<br>`B14-C09` Jupyter y experimentos reproducibles<br>`B14-C10` Pruebas de regresión numérica<br>`B14-C12` Ejecución reproducible con uv<br>`B14-C17` Contenedores y ambientes científicos | Mantener análisis y simulaciones reproducibles. |  |
| 9 | Tronco común | obligatoria | **Control automático**<br>`B16-C01`–`C14` (14 clases)<br>`B16-C18`–`C20` (3 clases) | Analizar la estabilidad de un lazo de control y sintonizar un controlador de actitud. |  |
| 10 | Tronco común | obligatoria | **Órbita del satélite**<br>`B41-C01`–`C20` (20 clases) | Describir la órbita, su período y su geometría y propagarla con un modelo verificable. | La perturbación orbital (B42) se estudia cuando el rol lo requiera. |
| 11 | Tronco común | recomendada | **Perturbaciones orbitales**<br>`B42-C01`–`C20` (20 clases) | Estimar cuánto deriva la órbita por arrastre y J2 durante la vida de la misión. |  |
| 12 | Tronco común | obligatoria | **Ingeniería de sistemas y diseño de misiones**<br>`B49-C01`–`C20` (20 clases) | Pasar de una necesidad de misión a requisitos verificables, presupuestos y revisiones. | Es el eje del rol: las clases de la ruta lo profundizan. |
| 13 | Tronco común | obligatoria | **Estructuras y materiales**<br>`B50-C01` Entorno mecánico de lanzamiento<br>`B50-C05`–`C07` (3 clases)<br>`B50-C09`–`C12` (4 clases)<br>`B50-C20` Diseño estructural de plataforma satelital | Seleccionar materiales y verificar que la estructura resiste el lanzamiento. |  |
| 14 | Tronco común | obligatoria | **Térmica y entorno espacial**<br>`B51-C01`–`C08` (8 clases)<br>`B51-C11`–`C12` (2 clases)<br>`B51-C18`–`C20` (3 clases) | Armar un balance térmico y definir un control térmico pasivo o activo. |  |
| 15 | Tronco común | obligatoria | **Potencia**<br>`B52-C01`–`C14` (14 clases)<br>`B52-C19`–`C20` (2 clases) | Dimensionar paneles y batería para el ciclo orbital. |  |
| 16 | Tronco común | obligatoria | **Actitud y control**<br>`B53-C01`–`C20` (20 clases) | Elegir sensores y actuadores y verificar el control de actitud. |  |
| 17 | Tronco común | obligatoria | **Aviónica y software de vuelo**<br>`B54-C01`–`C09` (9 clases)<br>`B54-C11`–`C12` (2 clases)<br>`B54-C14` Pruebas de software embarcado<br>`B54-C19`–`C20` (2 clases) | Diseñar la arquitectura del computador de vuelo y su verificación. |  |
| 18 | Tronco común | obligatoria | **Comunicaciones**<br>`B55-C01`–`C12` (12 clases)<br>`B55-C14`–`C15` (2 clases)<br>`B55-C19`–`C20` (2 clases) | Cerrar un presupuesto de enlace y definir la estación terrena. |  |
| 19 | Tronco común | obligatoria | **Integración y ensayos**<br>`B56-C01`–`C20` (20 clases) | Planificar integración, ensayos y calificación con evidencia trazable. |  |
| 20 | Tronco común | recomendada | **Operaciones de misión**<br>`B57-C02` Concepto de operaciones de misión<br>`B57-C04`–`C09` (6 clases)<br>`B57-C13`–`C14` (2 clases)<br>`B57-C18` Fin de vida y disposición orbital<br>`B57-C20` Simulación de jornada de control de misión | Escribir el concepto de operaciones y los procedimientos de contingencia. |  |
| 21 | Ruta | obligatoria | **Arquitectura de misión satelital**<br>`R12-M01-C01`–`C20` (20 clases) | Definir la arquitectura de un satélite con presupuestos de masa, energía y datos. | Reutiliza B49; aquí se aplica a un satélite concreto. |
| 22 | Ruta | obligatoria | **Plataformas y buses**<br>`R12-M03-C01`–`C20` (20 clases) | Elegir plataforma y bus (unidad CubeSat, componentes comerciales, compatibilidad). |  |
| 23 | Ruta | obligatoria | **Diseño de cargas útiles**<br>`R12-M02-C01`–`C20` (20 clases) | Dimensionar la carga útil y verificar su compatibilidad con el bus. |  |
| 24 | Ruta | obligatoria | **Sistema eléctrico de potencia**<br>`R12-M04-C01`–`C20` (20 clases) | Diseñar y verificar el subsistema eléctrico de un satélite pequeño. |  |
| 25 | Ruta | obligatoria | **Comunicaciones satelitales**<br>`R12-M05-C01`–`C20` (20 clases) | Diseñar el subsistema de comunicaciones de un satélite pequeño. |  |
| 26 | Ruta | obligatoria | **Determinación y control de actitud**<br>`R12-M06-C01`–`C20` (20 clases) | Diseñar y verificar el subsistema de actitud de un satélite pequeño. |  |
| 27 | Ruta | obligatoria | **Interfaces y configuración**<br>`R12-M07-C01`–`C20` (20 clases) | Controlar interfaces y configuración entre subsistemas. |  |
| 28 | Integración | obligatoria | **Integración y calificación de un CubeSat**<br>`R12-M08-C01`–`C20` (20 clases) | Planificar y documentar la integración y calificación de un CubeSat de extremo a extremo. | Es el proyecto final del rol. |

## Huecos detectados en el catálogo

Temas que este rol necesita y que el catálogo `0.1.0` no cubre. Alimentan las [ampliaciones aditivas](../../../documentacion/AMPLIACION_DEL_TRONCO_COMUN.md); no cambian ningún ID existente.

- **Interfaz con el lanzador, despliegue y papeles de integración de lanzamiento.** Ningún título del catálogo trata el despliegue desde el lanzador ni la documentación de interfaz con el proveedor de lanzamiento; B50-C01 cubre solo el entorno mecánico. *Propuesta:* clases nuevas en B56 o módulo nuevo de R12.
- **Normas y estándares de ingeniería espacial con versión y jurisdicción.** No hay clases sobre estándares de ingeniería espacial (por ejemplo de agencias o ECSS); R13-M07-C17 menciona normas de aseguramiento solo para software. *Propuesta:* bloque nuevo transversal de estándares y aseguramiento del producto.

[⬅️ Índice de la ruta](INDICE.md)
