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
- **Tecnologías de propulsión** ([**B78** · Tecnologías de propulsión espacial](../programa/tronco-comun/B78-tecnologias-de-propulsion-espacial.md)); **fluidos, termodinámica y aerotermodinámica de propulsión** ([**B79** · Fluidos, termodinámica y aerotermodinámica de propulsión](../programa/tronco-comun/B79-fluidos-termodinamica-y-aerotermodinamica-de-propulsion.md)).
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
10. 📚 [**B79** · Fluidos, termodinámica y aerotermodinámica de propulsión](../programa/tronco-comun/B79-fluidos-termodinamica-y-aerotermodinamica-de-propulsion.md) — usa 16 de 16 clases: `B79-` C01–C16

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

<!-- recorrido:inicio -->
### 🗺️ Recorrido módulo por módulo

El rol se estudia en **8 módulos** de 10 temas cada uno (cada tema es un par «concepto + aplicación»). Haz el diagnóstico, avanza por los módulos **en orden** y cierra cada uno con su checkpoint; al final, el proyecto y el criterio de salida.

**🩺 Diagnóstico de entrada.** Si respondes «no sé» a dos o más, empieza por los fundamentos de arriba:

- ¿Puedes aplicar la ecuación del cohete y calcular un presupuesto de masa?
- ¿Sabes el balance de energía en una tobera?
- ¿Manejas termodinámica de gases ideales?
- ¿Entiendes la presión dinámica y el máximo Q?

#### R11-M01 · Mecánica de fluidos para propulsión

1. **Conservación de masa en fluidos** — [`B79-C01`](../programa/clases/B79/B79-C01-conservacion-de-masa-en-fluidos/CLASE.md)
2. **Ecuaciones de Euler** — [`B79-C02`](../programa/clases/B79/B79-C02-ecuaciones-de-euler-para-flujo-no-viscoso/CLASE.md)
3. **Ecuaciones de Navier-Stokes** — [`B79-C03`](../programa/clases/B79/B79-C03-ecuaciones-de-navier-stokes/CLASE.md)
4. **Regímenes laminares y turbulentos** — [`B79-C04`](../programa/clases/B79/B79-C04-regimenes-laminar-y-turbulento/CLASE.md)
5. **Fluidos compresibles** — [`B79-C05`](../programa/clases/B79/B79-C05-dinamica-de-fluidos-compresibles/CLASE.md)
6. **Flujos supersónicos** — [`B79-C06`](../programa/clases/B79/B79-C06-flujos-supersonicos/CLASE.md)
7. **Ondas de choque** — [`B79-C07`](../programa/clases/B79/B79-C07-ondas-de-choque-normales-y-oblicuas/CLASE.md)
8. **Flujo por toberas como teoría** — [`B79-C08`](../programa/clases/B79/B79-C08-flujo-en-toberas-convergente-divergentes/CLASE.md)
9. **CFD académico** — [`B79-C09`](../programa/clases/B79/B79-C09-cfd-academico-fundamentos-y-limites/CLASE.md)
10. **Validación de flujo idealizado** — [`B11-C19`](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md), [`B83-C17`](../programa/clases/B83/B83-C17-verificacion-frente-a-validacion/CLASE.md)

✅ **Checkpoint R11-M01.** Sin mirar el material, explica cómo se relacionan «Conservación de masa en fluidos», «Flujos supersónicos» y «Validación de flujo idealizado», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R11-M02 · Termodinámica de sistemas propulsivos

1. **Primera ley termodinámica** — [`B79-C10`](../programa/clases/B79/B79-C10-primera-ley-de-la-termodinamica-en-sistemas-abiertos/CLASE.md)
2. **Segunda ley y entropía** — [`B79-C11`](../programa/clases/B79/B79-C11-segunda-ley-y-entropia/CLASE.md)
3. **Gas ideal y real** — [`B06-C09`](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md), [`B05-C14`](../programa/clases/B05/B05-C14-gases-y-presion/CLASE.md)
4. **Procesos adiabáticos** — [`B79-C12`](../programa/clases/B79/B79-C12-procesos-adiabaticos-e-isentropicos/CLASE.md)
5. **Entalpía de flujo** — [`B79-C13`](../programa/clases/B79/B79-C13-entalpia-de-flujo-y-entalpia-total/CLASE.md)
6. **Transferencia de calor** — [`B85-C02`](../programa/clases/B85/B85-C02-conduccion-termica-en-estructuras/CLASE.md), [`B85-C04`](../programa/clases/B85/B85-C04-radiacion-termica-de-superficies/CLASE.md)
7. **Propiedades de gases calientes** — [`B79-C14`](../programa/clases/B79/B79-C14-propiedades-de-gases-calientes/CLASE.md)
8. **Ciclos térmicos** — [`B79-C15`](../programa/clases/B79/B79-C15-ciclos-termodinamicos-de-propulsion/CLASE.md)
9. **Eficiencias termodinámicas** — [`B79-C16`](../programa/clases/B79/B79-C16-eficiencias-termodinamicas-de-motores/CLASE.md)
10. **Análisis de límites físicos** — [`B78-C18`](../programa/clases/B78/B78-C18-energia-especifica-y-limitaciones/CLASE.md)

✅ **Checkpoint R11-M02.** Sin mirar el material, explica cómo se relacionan «Primera ley termodinámica», «Transferencia de calor» y «Análisis de límites físicos», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R11-M03 · Modelos de propulsión química

1. **Impulso específico** — [`B78-C01`](../programa/clases/B78/B78-C01-empuje-e-impulso-especifico/CLASE.md)
2. **Balance energético de propulsión** — [`B78-C18`](../programa/clases/B78/B78-C18-energia-especifica-y-limitaciones/CLASE.md), [`B06-C12`](../programa/clases/B06/B06-C12-termoquimica-y-energia-de-reaccion/CLASE.md)
3. **Modelos de combustión conceptual** — [`B78-C02`](../programa/clases/B78/B78-C02-propulsion-quimica-como-sistema-fisico/CLASE.md), [`B06-C12`](../programa/clases/B06/B06-C12-termoquimica-y-energia-de-reaccion/CLASE.md), [`B06-C14`](../programa/clases/B06/B06-C14-cinetica-quimica-inicial/CLASE.md)
4. **Expansión de gases** — [`B78-C03`](../programa/clases/B78/B78-C03-termodinamica-de-camaras/CLASE.md), [`B06-C09`](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md)
5. **Rendimiento ideal de cohetes** — [`B78-C01`](../programa/clases/B78/B78-C01-empuje-e-impulso-especifico/CLASE.md), [`B77-C05`](../programa/clases/B77/B77-C05-ecuacion-de-cohete-ideal/CLASE.md)
6. **Modelos de masa** — [`B78-C17`](../programa/clases/B78/B78-C17-masa-de-propelente-y-presupuesto/CLASE.md), [`B77-C06`](../programa/clases/B77/B77-C06-relacion-masa-impulso/CLASE.md)
7. **Ecuación de Tsiolkovski** — [`B77-C05`](../programa/clases/B77/B77-C05-ecuacion-de-cohete-ideal/CLASE.md)
8. **Presupuesto de delta-v** — [`B75-C09`](../programa/clases/B75/B75-C09-presupuestos-de-delta-v/CLASE.md), [`B78-C17`](../programa/clases/B78/B78-C17-masa-de-propelente-y-presupuesto/CLASE.md)
9. **Pérdidas de rendimiento** — [`B77-C08`](../programa/clases/B77/B77-C08-perdidas-gravitacionales/CLASE.md), [`B77-C09`](../programa/clases/B77/B77-C09-perdidas-aerodinamicas/CLASE.md)
10. **Comparación de arquitecturas conceptuales** — [`B78-C20`](../programa/clases/B78/B78-C20-comparacion-no-operativa-de-arquitecturas-de-propulsion/CLASE.md), [`B78-C05`](../programa/clases/B78/B78-C05-propulsion-bipropelente-conceptual/CLASE.md), [`B78-C04`](../programa/clases/B78/B78-C04-propulsion-monopropelente-conceptual/CLASE.md)

✅ **Checkpoint R11-M03.** Sin mirar el material, explica cómo se relacionan «Impulso específico», «Modelos de masa» y «Comparación de arquitecturas conceptuales», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R11-M04 · Tecnologías de propulsión eléctrica

1. **Propulsión electrostática** — [`B78-C07`](../programa/clases/B78/B78-C07-motores-ionicos/CLASE.md), [`B78-C06`](../programa/clases/B78/B78-C06-propulsion-electrica-general/CLASE.md)
2. **Propulsión electromagnética** — [`B78-C09`](../programa/clases/B78/B78-C09-propulsion-por-plasma/CLASE.md), [`B78-C08`](../programa/clases/B78/B78-C08-propulsores-hall/CLASE.md)
3. **Motores iónicos** — [`B78-C07`](../programa/clases/B78/B78-C07-motores-ionicos/CLASE.md)
4. **Propulsores Hall** — [`B78-C08`](../programa/clases/B78/B78-C08-propulsores-hall/CLASE.md)
5. **Fuentes de alimentación** — [`B86-C08`](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md), [`B86-C09`](../programa/clases/B86/B86-C09-electronica-de-potencia/CLASE.md), [`B78-C06`](../programa/clases/B78/B78-C06-propulsion-electrica-general/CLASE.md)
6. **Erosión de componentes** — [`B78-C21`](../programa/clases/B78/B78-C21-erosion-y-vida-util-de-propulsores-electricos/CLASE.md)
7. **Ciclos de trabajo** — [`B78-C22`](../programa/clases/B78/B78-C22-ciclos-de-trabajo-y-operacion-de-propulsion-electrica/CLASE.md)
8. **Balance de energía** — [`B78-C18`](../programa/clases/B78/B78-C18-energia-especifica-y-limitaciones/CLASE.md), [`B86-C01`](../programa/clases/B86/B86-C01-balance-de-potencia-electrica/CLASE.md)
9. **Eficiencia propulsiva** — [`B78-C01`](../programa/clases/B78/B78-C01-empuje-e-impulso-especifico/CLASE.md), [`B78-C18`](../programa/clases/B78/B78-C18-energia-especifica-y-limitaciones/CLASE.md)
10. **Madurez de tecnologías eléctricas** — [`B78-C19`](../programa/clases/B78/B78-C19-madurez-tecnologica-trl/CLASE.md)

✅ **Checkpoint R11-M04.** Sin mirar el material, explica cómo se relacionan «Propulsión electrostática», «Erosión de componentes» y «Madurez de tecnologías eléctricas», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R11-M05 · Dinámica de vehículos de lanzamiento

1. **Ecuaciones de movimiento** — [`B77-C02`](../programa/clases/B77/B77-C02-movimiento-en-atmosfera/CLASE.md), [`B77-C12`](../programa/clases/B77/B77-C12-perfil-de-ascenso-orbital/CLASE.md)
2. **Modelos de atmósfera** — [`B72-C07`](../programa/clases/B72/B72-C07-modelos-de-densidad-atmosferica/CLASE.md), [`B77-C02`](../programa/clases/B77/B77-C02-movimiento-en-atmosfera/CLASE.md)
3. **Arrastre y sustentación** — [`B77-C03`](../programa/clases/B77/B77-C03-fuerzas-aerodinamicas/CLASE.md), [`B77-C04`](../programa/clases/B77/B77-C04-coeficientes-de-arrastre-y-sustentacion/CLASE.md)
4. **Centro de presión** — [`B77-C21`](../programa/clases/B77/B77-C21-centro-de-presion-y-margen-estatico/CLASE.md)
5. **Centro de masa** — [`B77-C22`](../programa/clases/B77/B77-C22-centro-de-masa-y-su-variacion-con-el-consumo-de-propelente/CLASE.md)
6. **Estabilidad de vuelo** — [`B77-C23`](../programa/clases/B77/B77-C23-estabilidad-de-vuelo-de-lanzadores-en-ascenso/CLASE.md)
7. **Cargas dinámicas** — [`B77-C10`](../programa/clases/B77/B77-C10-restricciones-de-cargas-estructurales/CLASE.md), [`B84-C09`](../programa/clases/B84/B84-C09-analisis-de-cargas/CLASE.md)
8. **Orientación y control** — [`B77-C24`](../programa/clases/B77/B77-C24-guiado-y-control-de-actitud-de-lanzadores-tvc/CLASE.md)
9. **Separación como evento simulado** — [`B77-C07`](../programa/clases/B77/B77-C07-separacion-de-etapas-conceptual/CLASE.md)
10. **Análisis de dispersión de trayectoria** — [`B77-C13`](../programa/clases/B77/B77-C13-inyeccion-y-dispersion-orbital/CLASE.md), [`B75-C18`](../programa/clases/B75/B75-C18-propagacion-de-dispersion-inicial/CLASE.md), [`B12-C14`](../programa/clases/B12/B12-C14-simulacion-monte-carlo/CLASE.md)

✅ **Checkpoint R11-M05.** Sin mirar el material, explica cómo se relacionan «Ecuaciones de movimiento», «Estabilidad de vuelo» y «Análisis de dispersión de trayectoria», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R11-M06 · Ascenso y reentrada atmosféricos

1. **Perfiles de ascenso** — [`B77-C12`](../programa/clases/B77/B77-C12-perfil-de-ascenso-orbital/CLASE.md)
2. **Pérdidas gravitacionales** — [`B77-C08`](../programa/clases/B77/B77-C08-perdidas-gravitacionales/CLASE.md)
3. **Pérdidas aerodinámicas** — [`B77-C09`](../programa/clases/B77/B77-C09-perdidas-aerodinamicas/CLASE.md)
4. **Inyección orbital** — [`B77-C13`](../programa/clases/B77/B77-C13-inyeccion-y-dispersion-orbital/CLASE.md)
5. **Dinámica de reentrada** — [`B77-C14`](../programa/clases/B77/B77-C14-dinamica-de-reentrada/CLASE.md)
6. **Flujo de calor de reentrada** — [`B77-C15`](../programa/clases/B77/B77-C15-calentamiento-aerodinamico/CLASE.md)
7. **Escudos térmicos** — [`B77-C16`](../programa/clases/B77/B77-C16-proteccion-termica/CLASE.md)
8. **Corredores de entrada** — [`B77-C25`](../programa/clases/B77/B77-C25-corredores-de-entrada-y-limites-de-trayectoria/CLASE.md)
9. **Aterrizaje controlado como modelo** — [`B77-C18`](../programa/clases/B77/B77-C18-aterrizaje-y-recuperacion/CLASE.md)
10. **Simulación de misión de entrada** — [`B77-C20`](../programa/clases/B77/B77-C20-simulacion-academica-de-una-trayectoria-de-vuelo/CLASE.md), [`B77-C14`](../programa/clases/B77/B77-C14-dinamica-de-reentrada/CLASE.md)

✅ **Checkpoint R11-M06.** Sin mirar el material, explica cómo se relacionan «Perfiles de ascenso», «Flujo de calor de reentrada» y «Simulación de misión de entrada», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R11-M07 · Seguridad y evaluación de sistemas de lanzamiento

1. **Cultura de seguridad aeroespacial** — [`B119-C21`](../programa/clases/B119/B119-C21-cultura-de-seguridad-aeroespacial-y-aprendizaje-de-incidentes/CLASE.md)
2. **Identificación de peligros** — [`B83-C21`](../programa/clases/B83/B83-C21-identificacion-de-peligros-en-sistemas-de-lanzamiento-hazid/CLASE.md)
3. **Análisis de fallos** — [`B83-C22`](../programa/clases/B83/B83-C22-analisis-de-modos-y-efectos-de-fallo-fmea-en-sistemas-espaciales/CLASE.md)
4. **Revisiones de seguridad** — [`B83-C13`](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md), [`B83-C14`](../programa/clases/B83/B83-C14-revisiones-cdr-y-trr/CLASE.md)
5. **Seguridad de instalaciones** — [`B119-C22`](../programa/clases/B119/B119-C22-seguridad-de-instalaciones-y-operaciones-de-sitio-de-lanzamiento/CLASE.md)
6. **Protección ambiental** — [`B119-C23`](../programa/clases/B119/B119-C23-proteccion-ambiental-de-las-actividades-de-lanzamiento/CLASE.md)
7. **Responsabilidad regulatoria** — [`B119-C08`](../programa/clases/B119/B119-C08-autorizacion-y-supervision-de-operadores/CLASE.md), [`B119-C10`](../programa/clases/B119/B119-C10-responsabilidad-por-danos-espaciales/CLASE.md)
8. **Límites de experimentación educativa** — [`B119-C24`](../programa/clases/B119/B119-C24-limites-legales-y-de-seguridad-de-la-experimentacion-educativa/CLASE.md)
9. **Procesos de autorización** — [`B119-C08`](../programa/clases/B119/B119-C08-autorizacion-y-supervision-de-operadores/CLASE.md), [`B119-C07`](../programa/clases/B119/B119-C07-registro-nacional-de-objetos/CLASE.md)
10. **Casos documentados de accidentes** — [`B96-C19`](../programa/clases/B96/B96-C19-lecciones-aprendidas-operativas/CLASE.md), [`B90-C17`](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md)

✅ **Checkpoint R11-M07.** Sin mirar el material, explica cómo se relacionan «Cultura de seguridad aeroespacial», «Protección ambiental» y «Casos documentados de accidentes», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R11-M08 · Simulación de misión propulsiva

1. **Modelo integrado de vehículo** — [`B77-C20`](../programa/clases/B77/B77-C20-simulacion-academica-de-una-trayectoria-de-vuelo/CLASE.md), [`B83-C07`](../programa/clases/B83/B83-C07-arquitecturas-de-sistemas/CLASE.md)
2. **Definición de etapas conceptuales** — [`B77-C01`](../programa/clases/B77/B77-C01-sistemas-de-lanzamiento/CLASE.md), [`B77-C07`](../programa/clases/B77/B77-C07-separacion-de-etapas-conceptual/CLASE.md)
3. **Perfil de empuje como entrada** — [`B78-C01`](../programa/clases/B78/B78-C01-empuje-e-impulso-especifico/CLASE.md)
4. **Trayectoria simulada** — [`B77-C20`](../programa/clases/B77/B77-C20-simulacion-academica-de-una-trayectoria-de-vuelo/CLASE.md), [`B77-C12`](../programa/clases/B77/B77-C12-perfil-de-ascenso-orbital/CLASE.md)
5. **Condiciones iniciales** — [`B77-C13`](../programa/clases/B77/B77-C13-inyeccion-y-dispersion-orbital/CLASE.md), [`B11-C02`](../programa/clases/B11/B11-C02-problemas-de-valor-inicial/CLASE.md)
6. **Variaciones ambientales** — [`B72-C07`](../programa/clases/B72/B72-C07-modelos-de-densidad-atmosferica/CLASE.md), [`B12-C14`](../programa/clases/B12/B12-C14-simulacion-monte-carlo/CLASE.md)
7. **Integración numérica** — [`B11-C07`](../programa/clases/B11/B11-C07-runge-kutta-de-cuarto-orden/CLASE.md), [`B11-C08`](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md), [`B11-C19`](../programa/clases/B11/B11-C19-estimacion-de-error-y-convergencia/CLASE.md)
8. **Rendimiento contra requisitos** — [`B83-C04`](../programa/clases/B83/B83-C04-requisitos-verificables/CLASE.md), [`B83-C17`](../programa/clases/B83/B83-C17-verificacion-frente-a-validacion/CLASE.md)
9. **Análisis de fallo simulado** — [`B77-C20`](../programa/clases/B77/B77-C20-simulacion-academica-de-una-trayectoria-de-vuelo/CLASE.md), [`B83-C16`](../programa/clases/B83/B83-C16-gestion-de-riesgos-tecnicos/CLASE.md)
10. **Informe de simulación y límites** — [`B12-C20`](../programa/clases/B12/B12-C20-informe-de-incertidumbre-de-una-mision/CLASE.md), [`B14-C19`](../programa/clases/B14/B14-C19-publicacion-de-codigo-y-datos/CLASE.md), [`B83-C17`](../programa/clases/B83/B83-C17-verificacion-frente-a-validacion/CLASE.md)

✅ **Checkpoint R11-M08.** Sin mirar el material, explica cómo se relacionan «Modelo integrado de vehículo», «Variaciones ambientales» y «Informe de simulación y límites», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

**🎯 Proyecto final · Dimensionamiento de un lanzador de dos etapas.** Define un lanzador pequeño: motores, masas, trayectoria de ascenso y análisis de seguridad, y verifica que alcanza una órbita baja con margen.

Entregables:

- Dimensionamiento de etapas y motores con la ecuación del cohete
- Simulación del ascenso con pérdidas
- Análisis de cargas en el máximo Q
- Evaluación de seguridad del lanzamiento y de rango

Criterios de evaluación:

- La simulación reproduce un caso de lanzamiento real dentro de ±10 %
- Los márgenes de masa y de delta-v están declarados
- El análisis de seguridad cubre trayectorias de fallo
- Las suposiciones propulsivas están referenciadas

**🏁 Criterio de salida.** Has terminado la ruta cuando:

- Puedes dimensionar un sistema propulsivo y un perfil de ascenso preliminares.
- Puedes analizar cargas y seguridad de un lanzamiento.
- Puedes comparar propulsión química y eléctrica según la misión.

<!-- /recorrido -->

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
3. Profundiza en **fluidos y termodinámica de propulsión** ([**B79** · Fluidos, termodinámica y aerotermodinámica de propulsión](../programa/tronco-comun/B79-fluidos-termodinamica-y-aerotermodinamica-de-propulsion.md)).
4. Avanza a **ingeniería de sistemas** ([**B83** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md)) y **gestión térmica** ([**B85** · Gestión térmica y entorno espacial](../programa/tronco-comun/B85-gestion-termica-y-entorno-espacial.md)).
5. Reúne tu **análisis documentado** con su historial.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Astrodinámica interplanetaria](astrodinamica-interplanetaria.md) · [Materiales estructuras e ingeniería térmica espacial](materiales-estructuras-e-ingenieria-termica-espacial.md) · [Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R11-ingenieria-de-lanzadores-y-propulsion/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
