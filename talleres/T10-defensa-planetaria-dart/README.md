# T10 · Defensa planetaria: planificar un impacto como DART

> **Qué es un taller.** Se hace, no se lee. Aquí el caso es **DART** (Double Asteroid Redirection Test), la primera misión que **cambió el movimiento de un cuerpo celeste** a propósito. Despegó el 24 de noviembre de 2021 y el 26 de septiembre de 2022 chocó a 6,1 km/s con Dimorphos, la pequeña luna del asteroide Didymos, y acortó su período orbital en unos 32 minutos. El sistema no suponía ningún peligro para la Tierra.
>
> **Estado:** E0 (redactado, pendiente de revisión disciplinar). Las cifras son redondeadas y de referencia pública; las inciertas llevan ⚠. El taller **no sirve para diseñar ni operar una misión real** ni para decisiones de defensa planetaria.

## Por qué esta misión

Es el taller de **la técnica que podría proteger a la Tierra**. La idea es simple (golpear un asteroide para desviarlo un poco) y enormemente exigente: hay que **acertar** a un blanco de 160 m a 11 millones de km, de forma autónoma, y **medir el resultado** con la precisión suficiente como para fiarse de él. Es, además, el único taller en que **el éxito es chocar**.

## Qué vas a lograr

1. Calcular el **efecto de un impacto** en la órbita de un asteroide, con el factor β.
2. Entender por qué la **antelación** pesa más que la fuerza del golpe.
3. Diseñar una **navegación autónoma terminal** con retardo de comunicación.
4. Planificar la **medición del resultado**: qué se observa y con qué incertidumbre.
5. Evaluar el marco de **cooperación internacional** de la defensa planetaria.
6. Reflexionar sobre los límites éticos y de comunicación de una misión de este tipo.

## Capítulos

| # | Capítulo | Qué resuelve |
|---|---|---|
| 1 | [Objetivo y requisitos](01-objetivo-y-requisitos.md) | Qué se quiere demostrar con un impacto |
| 2 | [Ventana y trayectoria](02-ventana-y-trayectoria.md) | Llegar con la geometría correcta |
| 3 | [Lanzador, masas y vehículo](03-lanzador-masas-y-vehiculo.md) | Una nave que es el proyectil |
| 4 | [Subsistemas](04-subsistemas.md) | Cámara, navegación autónoma y propulsión eléctrica |
| 5 | [Los últimos minutos](05-los-ultimos-minutos.md) | Acertar a 160 m a 6,1 km/s |
| 6 | [Operaciones y observación](06-operaciones-y-observacion.md) | Medir el efecto desde tierra y desde el espacio |
| 7 | [Fiabilidad, fallos y contingencias](07-fiabilidad-fallos-y-contingencias.md) | Una misión sin segunda oportunidad |
| 8 | [Seguridad y ética](08-seguridad-y-etica.md) | No desviar lo que no se debe y comunicar con honestidad |
| 9 | [Costos, cronograma y derecho](09-costos-cronograma-y-derecho.md) | Cooperación internacional y responsabilidad |
| 10 | [Entregables y rúbrica](10-entregables-y-rubrica.md) | El dossier y su evaluación |

Laboratorio: [`laboratorio_T10.py`](laboratorio_T10.py). Figuras: [`figuras_T10.py`](figuras_T10.py) (SVG en `figuras/`).

## Fuentes

Materiales públicos de la NASA, del Laboratorio de Física Aplicada de la Universidad Johns Hopkins, de la agencia espacial italiana (LICIACube) y de la ESA (misión Hera), publicaciones abiertas del equipo de investigación, el Tratado del Espacio Ultraterrestre y los documentos públicos de la Red Internacional de Alerta de Asteroides y del Grupo Asesor de Planificación de Misiones Espaciales. Se citan por nombre y alcance; verifica las cifras marcadas con ⚠.

Volver al [índice de talleres](../README.md) · [README del programa](../../README.md).
