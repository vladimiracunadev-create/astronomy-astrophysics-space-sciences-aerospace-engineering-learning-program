# T02 · Luna: planificar una misión como Artemis I

> **Qué es un taller.** Se hace, no se lee: reúne lo aprendido en las 12 áreas para planificar una misión real de principio a fin. Aquí el caso es **Artemis I**: el primer vuelo integrado del cohete SLS y la cápsula Orion de la NASA. Despegó el 16 de noviembre de 2022, rodeó la Luna sin tripulación y amerizó en el Pacífico el 11 de diciembre de 2022, tras unos 25,5 días.
>
> **Estado:** E0 (redactado, pendiente de revisión disciplinar). Las cifras son redondeadas y de referencia pública; las inciertas llevan ⚠. El taller **no sirve para diseñar ni operar una misión real**.

## Por qué esta misión

Es el ensayo general de llevar personas a la Luna. Su pregunta de diseño es distinta a la de Marte: no se trata de llegar lejos, sino de **volver vivo**. La prueba que importa es la **reentrada a ≈ 11 km/s**, que ninguna cápsula moderna había hecho.

## Qué vas a lograr

1. Definir qué debe **demostrar** una misión de prueba antes de llevar personas.
2. Calcular la inyección translunar, el sobrevuelo y el retorno.
3. Entender una **órbita retrógrada distante** y por qué se eligió.
4. Dimensionar la **reentrada con rebote** y su escudo térmico.
5. Gestionar el riesgo de un cohete nuevo, con aplazamientos, huracanes y fugas.
6. Estimar costos por lanzamiento y comparar con la capacidad del cohete.

## Capítulos

| # | Capítulo | Qué resuelve |
|---|---|---|
| 1 | [Objetivo y requisitos](01-objetivo-y-requisitos.md) | Qué debe probar un vuelo sin tripulación |
| 2 | [Ventana y trayectoria](02-ventana-y-trayectoria.md) | Salida, sobrevuelo, órbita distante y regreso |
| 3 | [Lanzador, masas y vehículo](03-lanzador-masas-y-vehiculo.md) | SLS, Orion y el módulo de servicio europeo |
| 4 | [Subsistemas](04-subsistemas.md) | Qué cambia cuando el vehículo es para personas |
| 5 | [Reentrada y amerizaje](05-reentrada-y-amerizaje.md) | El escudo térmico y el rebote atmosférico |
| 6 | [Operaciones y comunicaciones](06-operaciones-y-comunicaciones.md) | Control de lanzamiento y de misión |
| 7 | [Fiabilidad, fallos y contingencias](07-fiabilidad-fallos-y-contingencias.md) | Aplazamientos, fugas, huracanes y abortos |
| 8 | [Seguridad y radiación](08-seguridad-y-radiacion.md) | Público, tripulación futura y entorno |
| 9 | [Costos, cronograma y derecho](09-costos-cronograma-y-derecho.md) | Cuánto cuesta y bajo qué acuerdos |
| 10 | [Entregables y rúbrica](10-entregables-y-rubrica.md) | El dossier y su evaluación |

Laboratorio: [`laboratorio_T02.py`](laboratorio_T02.py). Figuras: [`figuras_T02.py`](figuras_T02.py) (SVG en `figuras/`).

## Fuentes

Materiales públicos de la NASA (resumen de la misión Artemis I, kit de prensa, hoja de datos de SLS y Orion, informes de la oficina de auditoría sobre costos del programa), de la ESA (módulo de servicio europeo) y el Tratado del Espacio Ultraterrestre y los Acuerdos Artemis. Se citan por nombre y alcance, no se reproducen. Verifica las cifras marcadas con ⚠.

Volver al [índice de talleres](../README.md) · [README del programa](../../README.md).
