# 🧱 Materiales estructuras e ingeniería térmica espacial

> Respondes dos preguntas sobre un vehículo o instrumento espacial: ¿aguanta el lanzamiento, el vacío y la fatiga?, y ¿a qué temperatura queda en el sol, en el eclipse y al final de su vida? Eliges materiales, dimensionas, modelas y demuestras con ensayos que tu análisis era correcto.
>
> **Nivel de entrada:** base sólida de cálculo, álgebra lineal, física y programación; el rol se apoya en modelos numéricos · **Foco:** mecánica de sólidos, elementos finitos, transferencia de calor, selección de materiales y ensayos · **Entrega:** informes de análisis trazables a requisitos, modelos documentados, selección de materiales justificada y el plan e informe de calificación

## 🧭 Qué es y por qué importa

Un vehículo espacial vive entre dos extremos: durante el lanzamiento soporta vibración, aceleración y choque; en órbita pasa del sol directo al eclipse en el vacío, donde el calor solo sale por radiación. Una estructura que falla o un componente que se sale de su rango de temperatura pueden perder la misión entera. Este rol es el dueño de **dos subsistemas, la estructura y el control térmico**, y de la evidencia de que cumplen.

El trabajo es una **cadena de márgenes**: cada cifra de resistencia o de temperatura se compara con un límite, y se deja escrito cuánto sobra y con qué incertidumbre. Dos miradas conviene distinguir:

- **Estructuras y materiales.** Dimensionan piezas y uniones, eligen aleaciones, compuestos o polímeros, y verifican pandeo, fatiga y modos de vibración. Su pregunta: *¿aguanta, con qué margen y cómo lo demuestro?*
- **Control térmico.** Equilibra la absorción solar, el albedo, la disipación interna y la radiación al espacio con técnicas pasivas (recubrimientos, aislamiento) o activas (calentadores, conductos de calor). Su pregunta: *¿cada componente queda dentro de su rango en el caso caliente y en el frío?*

Ambas se cruzan con los ensayos: un modelo no es una prueba, y la calificación es donde el análisis se confronta con la realidad. La referencia de la NASA sobre tecnología de satélites pequeños advierte, por ejemplo, que los mecanismos han contribuido a más del 10 % de las fallas reportadas de satélites pequeños (ver *Reconocimientos y referencias*): lo que se mueve, se prueba «como se vuela».

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es el ingeniero de sistemas del satélite.** [Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md) reparte masa, energía y datos entre subsistemas; tú eres dueño de dos subsistemas y entregas los márgenes que ese rol necesita.
- **No es ingeniería de lanzadores ni de propulsión.** [Ingeniería de lanzadores y propulsión](ingenieria-de-lanzadores-y-propulsion.md) diseña el lanzador; para ti es una fuente de cargas. La protección térmica de reentrada aparece solo como contexto.
- **No es arquitectura de hábitats.** [Arquitectura y hábitats extraterrestres](arquitectura-y-habitats-extraterrestres.md) diseña espacios presurizados habitables; tú aportas materiales y análisis estructural y térmico.
- **No es aviónica ni potencia.** El calor que disipan las tarjetas es un dato de entrada que otro subsistema te entrega, no un diseño tuyo.
- **No es operar el vibrador o la cámara de vacío.** Eso lo hace el técnico de ensayos; tú defines qué se ensaya, con qué criterio de aceptación y qué se concluye.
- **No es una certificación de vuelo.** Lo que enseña este programa es educativo y no sustituye normas ni procesos de calificación reales.

## 🗓️ Un día en el puesto

No hay un día típico, pero el trabajo se reparte así:

- **Revisar resultados de elementos finitos.** Antes de leer una sola tensión compruebas que la malla converge y que las condiciones de contorno representan la interfaz real.
- **Actualizar el modelo térmico.** Otro subsistema informa una nueva potencia disipada; recalculas el caso caliente con propiedades ópticas de **fin de vida**, porque los recubrimientos se degradan.
- **Correlacionar modelo y ensayo.** Un modo medido no coincide con el calculado: investigas rigidez de una unión, masa, condición de apoyo o error de modelo, y emites un informe de desviación.
- **Revisar un plan de ensayo.** Qué nivel, qué duración, qué criterio de aceptación y qué se concluye si falla.
- **Seleccionar o justificar un material.** Con criterio múltiple (resistencia, masa, comportamiento en vacío, desgasificación, costo, disponibilidad) y registro de supuestos.

Hay mucho cálculo reproducible y mucha documentación. La habilidad no es resolver un modelo, sino saber **cuánto confiar en él**.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Mecánica de sólidos:** elasticidad, pandeo, uniones atornilladas, fatiga y fractura ([**B50** · Estructuras, materiales y fabricación espacial](../programa/tronco-comun/B50-estructuras-materiales-y-fabricacion-espacial.md)).
- **Elementos finitos:** malla, convergencia, condiciones de contorno, análisis modal y correlación con ensayos; apoyado en [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) y [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md).
- **Transferencia de calor:** conducción y radiación, modelos de nodos, casos extremos caliente y frío ([**B51** · Gestión térmica y entorno espacial](../programa/tronco-comun/B51-gestion-termica-y-entorno-espacial.md)).
- **Materiales:** aleaciones, compuestos, polímeros y cerámicos; comportamiento en vacío y desgasificación.
- **Entorno espacial:** oxígeno atómico, radiación, ultravioleta, micrometeoritos y contaminación.
- **Ensayos y calificación:** vibración, choque, vacío térmico y criterios de aceptación ([**B56** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md)).
- **Incertidumbre y medición:** propagar errores y justificar un margen con números ([**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md), [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md)).
- **Programación** para automatizar cálculos y hacerlos reproducibles ([**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md)).

### Herramientas del oficio

```text
Estructuras:         solvers de elementos finitos, análisis modal, cálculo de uniones
Térmica:             modelado por nodos, análisis de radiación orbital, casos caliente/frío
Cálculo:             Python (NumPy, SciPy), hojas de cálculo para márgenes
Materiales:          bases de propiedades, selección multicriterio, fichas de desgasificación
Documentación:       informes trazables a requisitos, planes y procedimientos de ensayo
Control de cambios:  control de versiones de modelos, datos y supuestos
```

Estas son categorías; cualquier producto concreto es una decisión del equipo y este programa no lo recomienda por marca. Un modelo bien hecho con propiedades equivocadas da una respuesta equivocada con aspecto serio: contrasta siempre las propiedades de fabricante.

### Habilidades no técnicas

- **Rigor con los supuestos:** registrar cuáles son, cuáles no se cumplen y qué pasa si fallan.
- **Comunicación entre disciplinas:** explicarle a quien diseña electrónica cuánto calor puede disipar su tarjeta, y por qué.
- **Honestidad ante el margen:** decir «no sobra nada» a tiempo, no en la revisión final.
- **Mentalidad de ensayo:** un análisis es una hipótesis hasta que una prueba lo confirma.
- **Cuidado con la sostenibilidad:** los materiales y el diseño influyen en desechos y fin de vida.

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B05** · Física fundamental para el espacio](../programa/tronco-comun/B05-fisica-fundamental-para-el-espacio.md) — A01 · 20 clases
2. 📚 [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md) — A02 · 20 clases
3. 📚 [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) — A02 · 20 clases
4. 📚 [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) — A02 · 26 clases
5. 📚 [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) — A02 · 26 clases
6. 📚 [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) — A02 · 23 clases
7. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — A02 · 31 clases
8. 📚 [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) — A02 · 24 clases
9. 📚 [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) — A02 · 20 clases
10. 📚 [**B52** · Sistemas de potencia y energía espacial](../programa/tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md) — A07 · 23 clases
11. 📚 [**B53** · Sensores y control de actitud](../programa/tronco-comun/B53-sensores-y-control-de-actitud.md) — A07 · 22 clases
12. 📚 [**B54** · Aviónica y software crítico espacial](../programa/tronco-comun/B54-avionica-y-software-critico-espacial.md) — A07 · 44 clases
13. 📚 [**B55** · Comunicaciones y navegación satelital](../programa/tronco-comun/B55-comunicaciones-y-navegacion-satelital.md) — A07 · 25 clases

### 🎯 El núcleo del rol

**A04 · Óptica, telescopios y observatorios científicos**

1. 📚 [**B31** · Instrumentación y observatorios espaciales](../programa/tronco-comun/B31-instrumentacion-y-observatorios-espaciales.md) — usa 1 de 25 clases: `B31-` C11

**A06 · Mecánica orbital, navegación y vuelo espacial**

2. 📚 [**B47** · Dinámica de lanzamiento y reentrada](../programa/tronco-comun/B47-dinamica-de-lanzamiento-y-reentrada.md) — usa 1 de 25 clases: `B47-` C10

**A07 · Ingeniería y construcción de sistemas espaciales**

3. 📚 [**B50** · Estructuras, materiales y fabricación espacial](../programa/tronco-comun/B50-estructuras-materiales-y-fabricacion-espacial.md) — usa 33 de 38 clases: `B50-` C02–C19, C21–C35
4. 📚 [**B51** · Gestión térmica y entorno espacial](../programa/tronco-comun/B51-gestion-termica-y-entorno-espacial.md) — usa 18 de 29 clases: `B51-` C01, C04, C06–C07, C09–C11, C13–C14, C16, C18–C19, C24–C29
5. 📚 [**B56** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) — usa 11 de 24 clases: `B56-` C04, C09–C12, C17–C20, C23–C24

**A09 · Astronáutica humana, medicina y hábitats**

6. 📚 [**B60** · Hábitats espaciales y soporte vital](../programa/tronco-comun/B60-habitats-espaciales-y-soporte-vital.md) — usa 1 de 29 clases: `B60-` C15

<!-- /ruta -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es un **expediente de análisis y calificación** (educativo, no de vuelo):

- un modelo de elementos finitos de una pieza, con estudio de convergencia y comparación con una solución analítica;
- un modelo térmico de nodos de un satélite pequeño, con casos caliente y frío y análisis de incertidumbre;
- una selección de materiales justificada con criterio múltiple;
- un plan de calificación con criterios de aceptación y un informe de desviaciones.

Todo reproducible (código, datos, versiones) y con unidades, marco de referencia y tolerancias declarados. Guarda la primera versión, la retroalimentación y los cambios: el portafolio con su historia pesa más que un informe final impecable.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional única verificada. Las referencias de trabajo que sí se consultaron (2026-11-05) son:

- 📘 **NASA, *State-of-the-Art of Small Spacecraft Technology*, cap. 6 «Structures, Materials, and Mechanisms»** — página con fecha de 4 de agosto de 2026, leída hasta aproximadamente el 80 %. Describe estructuras primarias comerciales y a medida, dispensadores, mecanismos y manufactura aditiva polimérica; señala que los mecanismos han contribuido a más del 10 % de las fallas reportadas de satélites pequeños e insiste en probar «como se vuela», en margen y en ensayos de vida. (https://www.nasa.gov/smallsat-institute/sst-soa/structures-materials-and-mechanisms/)
- 📗 **NASA, mismo informe, cap. 7 «Thermal Control»** — página con fecha de 7 de mayo de 2026. Plantea el balance de calor entre absorción solar, albedo, disipación interna y radiación, separa técnicas pasivas de activas y advierte que las prestaciones publicadas por fabricantes no están verificadas de forma independiente. (https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/)
- 📙 **ECSS (Cooperación Europea para la Normalización Espacial)** — portada del sitio: mantiene un conjunto único de normas europeas, con ejemplos publicados sobre limpieza y control de contaminación. Qué norma aplica a un proyecto, en qué versión y bajo qué jurisdicción es una decisión contractual. (https://ecss.nl/)

Las normas de ingeniería, los requisitos del proveedor de lanzamiento y las certificaciones personales dependen de la jurisdicción y de la versión vigente, y **no están verificados aquí**. Consúltalos en su fuente oficial antes de usarlos en un proyecto real.

## 📈 Progresión del rol

Rutas habituales: **analista de un subsistema (estructura o térmica) → responsable de modelos completos de un vehículo → coordinación de la calificación con el resto del sistema**. Desde ahí se abren la ingeniería de sistemas y la gestión técnica de proyectos. Cómo se llama cada nivel y qué se exige depende de la organización; no se publican cifras salariales porque no se pudieron verificar con fuentes.

Roles vecinos con los que se comparte formación: [satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md), [lanzadores y propulsión](ingenieria-de-lanzadores-y-propulsion.md) y [hábitats extraterrestres](arquitectura-y-habitats-extraterrestres.md).

## ⚠️ Mitos y errores comunes

- **«Si la malla tiene muchos elementos, el resultado es bueno.»** Sin estudio de convergencia y condiciones de contorno correctas, una tensión precisa a seis decimales puede ser falsa.
- **«El caso caliente es el que importa.»** El frío (eclipse, fin de vida, calentadores sin energía) mata componentes tanto como el calor.
- **«Las propiedades de la ficha del fabricante bastan.»** Se contrastan: la propia NASA advierte que las prestaciones publicadas no están verificadas de forma independiente.
- **«Un mecanismo es un detalle.»** Los mecanismos están entre las causas más citadas de fallas en satélites pequeños; llevan margen, ensayo de vida y prueba «como se vuela».
- **«El ensayo es burocracia.»** Es la única evidencia de que el modelo representa la realidad.
- **«Un modelo es una prueba.»** Lo analizado se verifica con ensayo antes de volar; las cargas que afecten a personas o terceros se derivan a normas vigentes y a profesionales habilitados.

## 🚀 Siguientes pasos

1. **Asienta la base** con física y matemática: [**B05** · Física fundamental para el espacio](../programa/tronco-comun/B05-fisica-fundamental-para-el-espacio.md), [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md), [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) y [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md).
2. Aprende estructuras y materiales con [**B50** · Estructuras, materiales y fabricación espacial](../programa/tronco-comun/B50-estructuras-materiales-y-fabricacion-espacial.md) y resuelve una pieza con elementos finitos y su solución analítica.
3. Modela el control térmico con [**B51** · Gestión térmica y entorno espacial](../programa/tronco-comun/B51-gestion-termica-y-entorno-espacial.md): un satélite pequeño con caso caliente y frío.
4. Aprende a demostrar con [**B56** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) y escribe un plan de calificación con criterios de aceptación.
5. Reúne tu **expediente** y guarda su historia: primera versión, retroalimentación y cambios.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md) · [Ingeniería de lanzadores y propulsión](ingenieria-de-lanzadores-y-propulsion.md) · [Arquitectura y hábitats extraterrestres](arquitectura-y-habitats-extraterrestres.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R14-materiales-estructuras-e-ingenieria-termica-espacial/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
