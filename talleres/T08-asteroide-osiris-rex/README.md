# T08 · Asteroide: planificar un retorno de muestras como OSIRIS-REx

> **Qué es un taller.** Se hace, no se lee. Aquí el caso es **OSIRIS-REx**, la misión de la NASA que fue al asteroide Bennu, tomó una muestra y la trajo a la Tierra. Despegó el 8 de septiembre de 2016, llegó a Bennu el 3 de diciembre de 2018, recogió la muestra el 20 de octubre de 2020 en un contacto de unos 5 segundos y la cápsula aterrizó en Utah el 24 de septiembre de 2023.
>
> **Estado:** E0 (redactado, pendiente de revisión disciplinar). Las cifras son redondeadas y de referencia pública; las inciertas llevan ⚠. El taller **no sirve para diseñar ni operar una misión real**.

## Por qué esta misión

Es el taller del **viaje de ida y vuelta**: no basta con llegar, hay que **volver** y con un objeto en las manos. Traer material de un asteroide primitivo permite analizarlo con instrumentos que no caben en una nave. El reto es la combinación de **gravedad casi nula**, un **contacto de pocos segundos** a 18 minutos luz y una **reentrada** que debe devolver la muestra intacta.

## Qué vas a lograr

1. Calcular por qué ir a un asteroide **inclinado** cuesta más de lo que sugiere su distancia.
2. Diseñar la **aproximación y la órbita** alrededor de un cuerpo diminuto.
3. Planificar una **toma de muestra** autónoma, con retardo de comunicación mayor que el propio contacto.
4. Dimensionar la **reentrada y la recuperación** de una cápsula.
5. Proteger la **muestra** de la contaminación y definir su custodia.
6. Gestionar un resultado **mejor de lo esperado** (y el problema que trajo).

## Capítulos

| # | Capítulo | Qué resuelve |
|---|---|---|
| 1 | [Objetivo y requisitos](01-objetivo-y-requisitos.md) | Por qué Bennu y qué se hará con la muestra |
| 2 | [Ventana y trayectoria](02-ventana-y-trayectoria.md) | La inclinación manda, y el paso por la Tierra |
| 3 | [Lanzador, masas y vehículo](03-lanzador-masas-y-vehiculo.md) | Una nave de ≈ 2 toneladas con más de la mitad de combustible |
| 4 | [Subsistemas](04-subsistemas.md) | Brazo de muestreo, cámaras, lídar y navegación |
| 5 | [Cerca del cuerpo y toma de muestra](05-cerca-del-cuerpo-y-toma-de-muestra.md) | Orbitar a 1 km y tocar durante 5 s |
| 6 | [Operaciones y comunicaciones](06-operaciones-y-comunicaciones.md) | Operar a 18 minutos luz |
| 7 | [Fiabilidad, fallos y contingencias](07-fiabilidad-fallos-y-contingencias.md) | Partículas lanzadas por el asteroide y una muestra que se escapa |
| 8 | [Seguridad y protección](08-seguridad-y-proteccion.md) | Retorno de muestras y custodia |
| 9 | [Costos, cronograma y derecho](09-costos-cronograma-y-derecho.md) | Una misión de clase media y los recursos espaciales |
| 10 | [Entregables y rúbrica](10-entregables-y-rubrica.md) | El dossier y su evaluación |

Laboratorio: [`laboratorio_T08.py`](laboratorio_T08.py). Figuras: [`figuras_T08.py`](figuras_T08.py) (SVG en `figuras/`).

## Fuentes

Materiales públicos de la NASA, del Centro de Vuelos Espaciales Goddard y de la Universidad de Arizona (kit de prensa del lanzamiento, de la toma de muestra y del retorno, hoja de datos de la misión), publicaciones abiertas del equipo científico, la política de protección planetaria de COSPAR y el Tratado del Espacio Ultraterrestre. Se citan por nombre y alcance; verifica las cifras marcadas con ⚠.

Volver al [índice de talleres](../README.md) · [README del programa](../../README.md).
