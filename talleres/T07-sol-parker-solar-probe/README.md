# T07 · Sol: planificar un acercamiento como Parker Solar Probe

> **Qué es un taller.** Se hace, no se lee. Aquí el caso es **Parker Solar Probe**, la nave de la NASA que se acerca al Sol más que ningún objeto fabricado. Despegó el 12 de agosto de 2018, hizo su primer perihelio el 5 de noviembre de 2018 y, tras siete pasos por Venus, llegó el 24 de diciembre de 2024 a unos 6,1 millones de km de la superficie solar, a ≈ 690.000 km/h.
>
> **Estado:** E0 (redactado, pendiente de revisión disciplinar). Las cifras son redondeadas y de referencia pública; las inciertas llevan ⚠. El taller **no sirve para diseñar ni operar una misión real**.

## Por qué esta misión

Acercarse al Sol parece fácil: ya estamos en su órbita. Es **lo más difícil del sistema solar**. La Tierra viaja a 30 km/s alrededor del Sol; para caer hacia él hay que **frenar 21 km/s**, más de lo que cualquier cohete podía dar. Y cuando por fin llegas, el calor es **476 veces** el de la Tierra. Este taller es el de la **protección térmica**, la **autonomía** y el **uso de la gravedad de otro planeta para frenar**.

## Qué vas a lograr

1. Entender por qué se necesita **Venus** para frenar y cómo se diseña una secuencia de pasos.
2. Calcular la **órbita final** y la velocidad en el perihelio.
3. Dimensionar el **flujo de calor** y la temperatura de un escudo y de unos paneles.
4. Diseñar un sistema de **autoprotección** que actúe antes de que la Tierra pueda reaccionar.
5. Planificar **datos y enlace** cuando la antena queda detrás del escudo.
6. Gestionar el riesgo de una misión de **tecnología nueva**.

## Capítulos

| # | Capítulo | Qué resuelve |
|---|---|---|
| 1 | [Objetivo y requisitos](01-objetivo-y-requisitos.md) | Qué enseña la corona solar |
| 2 | [Ventana y trayectoria](02-ventana-y-trayectoria.md) | Frenar con Venus, siete veces |
| 3 | [Lanzador, masas y vehículo](03-lanzador-masas-y-vehiculo.md) | El cohete más potente para una nave de 685 kg |
| 4 | [Subsistemas](04-subsistemas.md) | Escudo térmico, paneles refrigerados e instrumentos |
| 5 | [El perihelio](05-el-perihelio.md) | Las horas en que todo está en juego |
| 6 | [Operaciones y comunicaciones](06-operaciones-y-comunicaciones.md) | Operar lo que no se puede mirar |
| 7 | [Fiabilidad, fallos y contingencias](07-fiabilidad-fallos-y-contingencias.md) | Autoprotección y márgenes |
| 8 | [Seguridad y protección](08-seguridad-y-proteccion.md) | Lanzamiento, pruebas térmicas y fin de misión |
| 9 | [Costos, cronograma y derecho](09-costos-cronograma-y-derecho.md) | Tecnología nueva, 60 años de ideas |
| 10 | [Entregables y rúbrica](10-entregables-y-rubrica.md) | El dossier y su evaluación |

Laboratorio: [`laboratorio_T07.py`](laboratorio_T07.py). Figuras: [`figuras_T07.py`](figuras_T07.py) (SVG en `figuras/`).

## Fuentes

Materiales públicos de la NASA y del Laboratorio de Física Aplicada de la Universidad Johns Hopkins (kit de prensa del lanzamiento, hoja de datos de la misión, artículos del equipo científico) y el Tratado del Espacio Ultraterrestre. Se citan por nombre y alcance; verifica las cifras marcadas con ⚠.

Volver al [índice de talleres](../README.md) · [README del programa](../../README.md).
