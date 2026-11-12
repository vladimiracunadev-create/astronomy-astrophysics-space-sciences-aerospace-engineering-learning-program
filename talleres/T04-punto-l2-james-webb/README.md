# T04 · Punto L2: planificar un observatorio como el telescopio James Webb

> **Qué es un taller.** Se hace, no se lee. Aquí el caso es el **telescopio espacial James Webb (JWST)**: un observatorio infrarrojo de la NASA, la ESA y la agencia espacial de Canadá. Despegó el 25 de diciembre de 2021, llegó al punto L2 el 24 de enero de 2022 y entregó sus primeras imágenes científicas el 12 de julio de 2022.
>
> **Estado:** E0 (redactado, pendiente de revisión disciplinar). Las cifras son redondeadas y de referencia pública; las inciertas llevan ⚠. El taller **no sirve para diseñar ni operar un observatorio real**.

## Por qué esta misión

Es el problema de la **fiabilidad total**: un telescopio de 6,5 m no cabe en ningún cohete, así que **se pliega y se despliega solo** a 1,5 millones de km, donde nadie puede ir a arreglarlo. Cada una de sus 344 piezas críticas debía funcionar la primera vez. Aquí se estudia cómo se diseña, se prueba y se opera algo así.

## Qué vas a lograr

1. Entender por qué un telescopio infrarrojo debe ir **lejos, frío y a la sombra**.
2. Calcular la geometría del punto **L2** y el comportamiento de una órbita de halo.
3. Dimensionar **resolución y área colectora** y compararlas con otro observatorio.
4. Evaluar la **fiabilidad de una cadena de despliegues** y el requisito por punto.
5. Planificar **cientos de eventos críticos** sin posibilidad de reparación.
6. Analizar cómo un costo y un calendario se multiplican en un proyecto largo.

## Capítulos

| # | Capítulo | Qué resuelve |
|---|---|---|
| 1 | [Objetivo y requisitos](01-objetivo-y-requisitos.md) | Qué ciencia exige un telescopio infrarrojo gigante |
| 2 | [Ventana y trayectoria](02-ventana-y-trayectoria.md) | Por qué L2 y cómo se llega |
| 3 | [Lanzador, masas y vehículo](03-lanzador-masas-y-vehiculo.md) | Un espejo de 6,5 m en un cohete de 5 m |
| 4 | [Subsistemas](04-subsistemas.md) | Espejo, escudo solar, instrumentos y refrigeración |
| 5 | [Los despliegues](05-los-despliegues.md) | Dos semanas sin posibilidad de error |
| 6 | [Operaciones y comunicaciones](06-operaciones-y-comunicaciones.md) | Observar, descargar y repartir tiempo de telescopio |
| 7 | [Fiabilidad, fallos y contingencias](07-fiabilidad-fallos-y-contingencias.md) | Probar hasta el límite lo que no se puede reparar |
| 8 | [Seguridad y entorno](08-seguridad-y-entorno.md) | Micrometeoroides, combustible y operación |
| 9 | [Costos, cronograma y derecho](09-costos-cronograma-y-derecho.md) | De ≈ 1.000 a ≈ 10.000 millones de dólares |
| 10 | [Entregables y rúbrica](10-entregables-y-rubrica.md) | El dossier y su evaluación |

Laboratorio: [`laboratorio_T04.py`](laboratorio_T04.py). Figuras: [`figuras_T04.py`](figuras_T04.py) (SVG en `figuras/`).

## Fuentes

Materiales públicos de la NASA, la ESA, la agencia espacial de Canadá y del Instituto de Ciencia del Telescopio Espacial (hoja de datos del observatorio, documentación para usuarios, kits de prensa del lanzamiento y de las primeras imágenes) y el Tratado del Espacio Ultraterrestre. Se citan por nombre y alcance; verifica las cifras marcadas con ⚠.

Volver al [índice de talleres](../README.md) · [README del programa](../../README.md).
