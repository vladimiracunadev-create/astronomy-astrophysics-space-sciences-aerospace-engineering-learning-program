# 🚀 Ingeniería de lanzadores y propulsión

> Diseñas y analizas los sistemas que llevan una carga al espacio: motores, flujos y combustión, dinámica de ascenso y reentrada, y las restricciones de masa que lo gobiernan.
>
> **Nivel de entrada:** física, termodinámica y matemática de nivel universitario; rol técnico de ingeniería · **Foco:** propulsión, termodinámica y fluidos, aerotermodinámica, dinámica de lanzamiento y reentrada, ingeniería de sistemas de un lanzador · **Entrega:** un análisis de desempeño de un motor o de un ascenso, con sus supuestos, sus unidades y su margen frente a la referencia

## 🧭 Qué es y por qué importa

Un lanzador es, sobre todo, una forma de convertir masa de propulsante en velocidad. La ecuación del cohete lo resume: cada incremento de velocidad exige una fracción de masa que crece de forma exponencial, y de ahí que la ingeniería de lanzadores sea una lucha constante por cada kilogramo.

El rol cubre tres frentes: el **motor** (cómo se produce el empuje), el **vehículo** (cómo asciende y cómo soporta cargas) y la **reentrada** (cómo se disipa la energía al volver). Los tres comparten fluidos, termodinámica y dinámica.

Las miradas del rol son:

- **Propulsión.** Combustión, toberas, ciclos. Su pregunta es: *¿qué empuje y qué eficiencia entrega, y a qué costo de masa?*
- **Ascenso y reentrada.** Dinámica, cargas y calentamiento. Su pregunta es: *¿qué cargas y qué temperaturas debe soportar el vehículo?*
- **Sistema.** Compromisos de misión. Su pregunta es: *¿qué diseño cumple la misión con margen?*

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es diseño de trayectorias interplanetarias.** Esa usa las capacidades del lanzador como entrada ([Astrodinámica interplanetaria](astrodinamica-interplanetaria.md)).
- **No es ingeniería de satélites.** Es el vehículo que lo lleva, no la carga ([Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md)).
- **No es solo un motor.** Exige entender el vehículo completo y su misión.
- **No es regulación espacial.** La seguridad y la normativa de lanzamiento existen, pero son otro campo.

## 🗓️ Un día en el puesto

- **Análisis de desempeño:** calculas empuje, impulso específico y masa para un diseño.
- **Fluidos y calor:** estimas flujo en una tobera o calentamiento en reentrada.
- **Simulación de ascenso:** evalúas cargas y trayectoria.
- **Compromisos:** comparas alternativas por masa, costo y riesgo.
- **Revisión de supuestos:** verificas unidades, hipótesis y márgenes.

Dicho sin adornos: **las unidades y los márgenes** se equivocan con más frecuencia que las ecuaciones.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Dinámica de lanzamiento y reentrada** ([**B77** · Dinámica de lanzamiento y reentrada](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md)).
- **Tecnologías de propulsión** ([**B78** · Tecnologías de propulsión espacial](../programa/tronco-comun/B78-tecnologias-de-propulsion-espacial.md)); **fluidos, termodinámica y aerotermodinámica de propulsión** ([**B79** · Fluidos, termodinámica y aerotermodinámica de propulsión](../PROGRAMA_ACADEMICO_COMPLETO.md#b79--fluidos-termodinámica-y-aerotermodinámica-de-propulsión)).
- **Ingeniería de sistemas** ([**B83** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md)); **gestión térmica** ([**B85** · Gestión térmica y entorno espacial](../programa/tronco-comun/B85-gestion-termica-y-entorno-espacial.md)).
- **Simulación numérica** ([**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md)).
- **Derecho, seguridad y geopolítica espacial** como contexto ([**B119** · Derecho, seguridad y geopolítica espacial](../programa/tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md)).

### Herramientas del oficio

```text
Cálculo:              Python científico y hojas de cálculo verificadas
Termodinámica:        bases de propiedades de fluidos y de combustión
Simulación:           modelos de ascenso y de aerotermodinámica
Ingeniería:           herramientas de diseño de sistemas y de masas
Documentación:        registro de supuestos y de unidades
```

Un resultado sin unidades ni referencia de comparación no es verificable. Declara unidades, hipótesis y fuente de cada dato.

### Habilidades no técnicas

- **Pensar en seguridad y en margen.**
- **Trabajo en equipos multidisciplinarios.**
- **Documentación rigurosa de supuestos.**
- **Comunicación clara de compromisos.**

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md) — A02 · 20 clases
2. 📚 [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) — A02 · 20 clases
3. 📚 [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) — A02 · 23 clases
4. 📚 [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) — A02 · 24 clases
5. 📚 [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) — A02 · 20 clases

### 🎯 El núcleo del rol

**A01 · Alfabetización científica, astronómica y tecnológica**

1. 📚 [**B05** · Física fundamental para el espacio](../programa/tronco-comun/B05-fisica-fundamental-para-el-espacio.md) — usa 1 de 20 clases: `B05-` C14
2. 📚 [**B06** · Química y materia del universo](../programa/tronco-comun/B06-quimica-y-materia-del-universo.md) — usa 3 de 20 clases: `B06-` C09, C12, C14

**A02 · Matemática, física computacional y métodos científicos**

3. 📚 [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) — usa 4 de 26 clases: `B11-` C02, C07–C08, C19
4. 📚 [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) — usa 2 de 26 clases: `B12-` C14, C20
5. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — usa 1 de 31 clases: `B14-` C19

**A06 · Mecánica orbital, navegación y vuelo espacial**

6. 📚 [**B72** · Perturbaciones y evolución de órbitas](../programa/tronco-comun/B72-perturbaciones-y-evolucion-de-orbitas.md) — usa 1 de 21 clases: `B72-` C07
7. 📚 [**B75** · Trayectorias y misiones interplanetarias](../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md) — usa 2 de 30 clases: `B75-` C09, C18
8. 📚 [**B77** · Dinámica de lanzamiento y reentrada](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md) — usa 22 de 25 clases: `B77-` C01–C10, C12–C16, C18, C20–C25
9. 📚 [**B78** · Tecnologías de propulsión espacial](../programa/tronco-comun/B78-tecnologias-de-propulsion-espacial.md) — usa 15 de 22 clases: `B78-` C01–C09, C17–C22
10. 📚 [**B79** · Fluidos, termodinámica y aerotermodinámica de propulsión](../PROGRAMA_ACADEMICO_COMPLETO.md#b79--fluidos-termodinámica-y-aerotermodinámica-de-propulsión) — usa 16 de 16 clases: `B79-` C01–C16

**A07 · Ingeniería y construcción de sistemas espaciales**

11. 📚 [**B83** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) — usa 8 de 24 clases: `B83-` C04, C07, C13–C14, C16–C17, C21–C22
12. 📚 [**B84** · Estructuras, materiales y fabricación espacial](../programa/tronco-comun/B84-estructuras-materiales-y-fabricacion-espacial.md) — usa 1 de 38 clases: `B84-` C09
13. 📚 [**B85** · Gestión térmica y entorno espacial](../programa/tronco-comun/B85-gestion-termica-y-entorno-espacial.md) — usa 2 de 29 clases: `B85-` C02, C04
14. 📚 [**B86** · Sistemas de potencia y energía espacial](../programa/tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md) — usa 3 de 23 clases: `B86-` C01, C08–C09
15. 📚 [**B90** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) — usa 1 de 24 clases: `B90-` C17

**A08 · Operaciones de misión y robótica espacial**

16. 📚 [**B96** · Control y operación de misiones espaciales](../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) — usa 1 de 30 clases: `B96-` C19

**A10 · Entorno orbital, derecho y seguridad espacial**

17. 📚 [**B119** · Derecho, seguridad y geopolítica espacial](../programa/tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md) — usa 7 de 36 clases: `B119-` C07–C08, C10, C21–C24

<!-- /ruta -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es un **análisis de desempeño documentado**:

- un caso de referencia con datos publicados;
- el cálculo de empuje, impulso específico y masa con unidades explícitas;
- una simulación de ascenso o de reentrada con sus cargas;
- una comparación con la referencia y una estimación del error;
- el código para repetirlo.

Los bloques de la ruta aportan ejercicios y laboratorios; guarda la primera versión y sus cambios.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional verificada, y para esta guía no se consultó una fuente externa específica (2026-11-05). Por eso no se citan normas, requisitos de acceso ni cifras: cuando se necesiten, deben consultarse en la fuente oficial vigente de la institución, agencia o empresa correspondiente.

## 📈 Progresión del rol

Rutas habituales: **ingeniero/a de propulsión o de sistemas de lanzamiento → responsable de un subsistema → liderazgo técnico de vehículo**. Se abren la aerotermodinámica y la ingeniería de sistemas. No se publican cifras salariales por no poder verificarlas.

Roles vecinos con los que se comparte formación: [Astrodinámica interplanetaria](astrodinamica-interplanetaria.md), [Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md) y [Aviónica y software espacial de alta fiabilidad](avionica-y-software-espacial-de-alta-fiabilidad.md).

## ⚠️ Mitos y errores comunes

- **«Más empuje resuelve todo».** Sin masa estructural baja no alcanza.
- **«La reentrada es solo frenado».** El calentamiento y las cargas dominan el diseño.
- **«Un motor probado en banco está listo para el vuelo».** El entorno de vuelo cambia las condiciones.
- **«Es mecánica pura».** Es termodinámica, fluidos, materiales y sistemas.
- **«Reutilizar siempre ahorra».** Depende de la tasa de uso y del costo de recuperación.

## 🚀 Siguientes pasos

1. **Asienta la base** con el área A01 y la física de tu diagnóstico.
2. Estudia **dinámica de lanzamiento y reentrada** ([**B77** · Dinámica de lanzamiento y reentrada](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md)) y **propulsión** ([**B78** · Tecnologías de propulsión espacial](../programa/tronco-comun/B78-tecnologias-de-propulsion-espacial.md)).
3. Profundiza en **fluidos y termodinámica de propulsión** ([**B79** · Fluidos, termodinámica y aerotermodinámica de propulsión](../PROGRAMA_ACADEMICO_COMPLETO.md#b79--fluidos-termodinámica-y-aerotermodinámica-de-propulsión)).
4. Avanza a **ingeniería de sistemas** ([**B83** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md)) y **gestión térmica** ([**B85** · Gestión térmica y entorno espacial](../programa/tronco-comun/B85-gestion-termica-y-entorno-espacial.md)).
5. Reúne tu **análisis documentado** con su historial.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Astrodinámica interplanetaria](astrodinamica-interplanetaria.md) · [Materiales estructuras e ingeniería térmica espacial](materiales-estructuras-e-ingenieria-termica-espacial.md) · [Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R11-ingenieria-de-lanzadores-y-propulsion/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
