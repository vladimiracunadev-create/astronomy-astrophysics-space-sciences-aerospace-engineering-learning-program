# 📡 Radioastronomía e interferometría

> Observas el universo con ondas de radio: diseñas antenas y receptores de bajo ruido, combinas varias antenas como un interferómetro y reduces los datos para obtener imágenes y espectros.
>
> **Nivel de entrada:** física de ondas, electromagnetismo y procesamiento de señales, más programación; rol técnico y de investigación · **Foco:** antenas y receptores, radiofrecuencia, interferometría, calibración, correlación y reducción de datos · **Entrega:** un sistema de recepción o un análisis interferométrico con su calibración, su presupuesto de ruido y datos reducidos reproducibles

## 🧭 Qué es y por qué importa

La radioastronomía observa el cielo en longitudes de onda largas, desde el decímetro hasta el milímetro. La señal que llega es extremadamente débil: el trabajo consiste en **recogerla con una antena, amplificarla con poco ruido, digitalizarla y, si hay varias antenas, correlacionarlas** para lograr imágenes de alta resolución. Un interferómetro consigue así la resolución de una antena de tamaño mucho mayor que cada plato individual.

ALMA ilustra la escala del oficio: según su propia página, está en la meseta de Chajnantor, en el desierto de Atacama, en Chile, y se compone de 66 antenas de alta precisión que operan como un solo instrumento, con separaciones entre 150 metros y 16 kilómetros y longitudes de onda de 0,32 a 3,6 mm.

El rol se reparte en tres miradas:

- **Hardware de recepción.** Antenas, receptores de bajo ruido, osciladores estables y cadena de radiofrecuencia. Su pregunta es: *¿cuánto ruido agrego y cómo lo mido?*
- **Interferometría.** Calibración de fase, correlación y síntesis de apertura. Su pregunta es: *¿qué errores de fase y de amplitud limitan mi imagen?*
- **Reducción de datos.** Del dato crudo a la imagen calibrada, con su incertidumbre. Su pregunta es: *¿qué le debo a la calibración y qué es señal real?*

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es óptica.** Comparte la teoría de aperturas, pero trabaja con antenas, receptores y electrónica distinta ([Ingeniería óptica y telescopios profesionales](ingenieria-optica-y-telescopios-profesionales.md)).
- **No es telecomunicaciones.** Una estación de comunicaciones busca transmitir información; tú buscas medir una señal natural muy débil ([Telecomunicaciones y estaciones terrestres espaciales](telecomunicaciones-y-estaciones-terrestres-espaciales.md)).
- **No es astrofísica de objetos.** Interpretar la fuente es el trabajo de quien estudia ese objeto ([Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md)); tú aseguras que el dato sea confiable.
- **No es «usar un radiotelescopio».** Observar con un instrumento ya construido es una parte; este rol llega hasta su diseño y su calibración.

## 🗓️ Un día en el puesto

- **Cadena de recepción:** mides ruido y ganancia de un receptor, ajustas y documentas.
- **Calibración:** estimas errores de fase y amplitud con una fuente conocida y verificas que la calibración se mantiene.
- **Reducción de datos:** corres un flujo de procesamiento, revisas artefactos y repites con otro criterio de edición.
- **Código:** mucho análisis y automatización en Python o similar.
- **Revisión con el equipo:** discutes qué datos se descartan y por qué.

Dicho sin adornos: la mayor parte del tiempo se va en **separar señal de error**, y casi todos los errores se parecen a una señal.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Radioastronomía y propagación:** espectro radio, antenas, ruido de sistema y radiometría ([**B46** · Radioastronomía e interferometría](../programa/tronco-comun/B46-radioastronomia-e-interferometria.md)).
- **Antenas y receptores:** diseño, ganancia, temperatura de ruido ([**B49** · Antenas y receptores de radioastronomía](../programa/tronco-comun/B49-antenas-y-receptores-de-radioastronomia.md)).
- **Interferometría y reducción de datos:** líneas de base, correladores, calibración y síntesis ([**B51** · Interferometría avanzada y reducción de datos de radio](../programa/tronco-comun/B51-interferometria-avanzada-y-reduccion-de-datos-de-radio.md), [**B46** · Radioastronomía e interferometría](../programa/tronco-comun/B46-radioastronomia-e-interferometria.md)).
- **Señales e imágenes:** procesamiento, transformadas y estimación ([**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md)).
- **Metrología y tiempo:** estabilidad de frecuencia y sincronización ([**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md)).
- **Computación científica:** reducción de datos reproducible ([**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md)).

### Herramientas del oficio

```text
Instrumentación:       analizadores de espectro, generadores de señal, radios definidas por software
Cálculo y datos:      Python científico y paquetes de reducción de datos interferométricos
Calibración:          fuentes de referencia y procedimientos de calibración de fase y amplitud
Control:              sistemas de adquisición y sincronización de tiempo y frecuencia
Documentación:        registros de calibración y bitácoras
```

Una cadena de radiofrecuencia mal caracterizada produce datos precisos y falsos. Lo que se paga es tu capacidad de medir tus propios errores.

### Habilidades no técnicas

- **Meticulosidad experimental:** registrar cada ajuste y cada condición.
- **Paciencia ante la depuración:** encontrar la fuente de una interferencia puede llevar días.
- **Comunicación con astrónomos e ingenieros.**
- **Trabajo en equipos internacionales y multilingües.**

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B05** · Física fundamental para el espacio](../programa/tronco-comun/B05-fisica-fundamental-para-el-espacio.md) — A01 · 20 clases
2. 📚 [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md) — A02 · 20 clases
3. 📚 [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) — A02 · 20 clases
4. 📚 [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) — A02 · 26 clases
5. 📚 [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) — A02 · 20 clases
6. 📚 [**B45** · Espectroscopía, fotometría y polarimetría](../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md) — A04 · 24 clases
7. 📚 [**B47** · Instrumentación y observatorios espaciales](../programa/tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md) — A04 · 25 clases

### 🎯 El núcleo del rol

**A02 · Matemática, física computacional y métodos científicos**

1. 📚 [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) — usa 2 de 26 clases: `B12-` C05, C16
2. 📚 [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) — usa 10 de 23 clases: `B13-` C05, C07, C11–C12, C17–C22
3. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — usa 8 de 31 clases: `B14-` C05–C06, C10, C12–C14, C16, C19
4. 📚 [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) — usa 8 de 24 clases: `B15-` C02, C05–C08, C11–C12, C16

**A03 · Astrofísica y ciencias fundamentales del universo**

5. 📚 [**B30** · Heliofísica y física de plasmas](../programa/tronco-comun/B30-heliofisica-y-fisica-de-plasmas.md) — usa 1 de 23 clases: `B30-` C21

**A04 · Óptica, telescopios y observatorios científicos**

6. 📚 [**B42** · Óptica física y óptica adaptativa](../programa/tronco-comun/B42-optica-fisica-y-optica-adaptativa.md) — usa 1 de 24 clases: `B42-` C08
7. 📚 [**B44** · Detectores y adquisición astronómica](../programa/tronco-comun/B44-detectores-y-adquisicion-astronomica.md) — usa 1 de 20 clases: `B44-` C19
8. 📚 [**B46** · Radioastronomía e interferometría](../programa/tronco-comun/B46-radioastronomia-e-interferometria.md) — usa 17 de 20 clases: `B46-` C03–C11, C13–C20
9. 📚 [**B48** · Operaciones de observatorios científicos](../programa/tronco-comun/B48-operaciones-de-observatorios-cientificos.md) — usa 1 de 23 clases: `B48-` C17
10. 📚 [**B49** · Antenas y receptores de radioastronomía](../programa/tronco-comun/B49-antenas-y-receptores-de-radioastronomia.md) — usa 11 de 11 clases: `B49-` C01–C11
11. 📚 [**B51** · Interferometría avanzada y reducción de datos de radio](../programa/tronco-comun/B51-interferometria-avanzada-y-reduccion-de-datos-de-radio.md) — usa 14 de 14 clases: `B51-` C01–C14

**A05 · Ciencias planetarias, astroquímica y habitabilidad**

12. 📚 [**B53** · Astrogeología y geodesia planetaria](../programa/tronco-comun/B53-astrogeologia-y-geodesia-planetaria.md) — usa 1 de 30 clases: `B53-` C04
13. 📚 [**B57** · Observación terrestre y geociencias orbitales](../programa/tronco-comun/B57-observacion-terrestre-y-geociencias-orbitales.md) — usa 1 de 34 clases: `B57-` C10

**A06 · Mecánica orbital, navegación y vuelo espacial**

14. 📚 [**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md) — usa 2 de 30 clases: `B74-` C01, C07

**A07 · Ingeniería y construcción de sistemas espaciales**

15. 📚 [**B89** · Comunicaciones y navegación satelital](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) — usa 2 de 25 clases: `B89-` C06–C07
16. 📚 [**B90** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) — usa 2 de 24 clases: `B90-` C13–C14

**A10 · Entorno orbital, derecho y seguridad espacial**

17. 📚 [**B118** · Tráfico espacial y sostenibilidad orbital](../programa/tronco-comun/B118-trafico-espacial-y-sostenibilidad-orbital.md) — usa 1 de 24 clases: `B118-` C17

<!-- /ruta -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es un **sistema o un análisis radioastronómico documentado**:

- un presupuesto de ruido de una cadena de recepción con mediciones;
- una observación o simulación interferométrica con calibración explícita;
- datos reducidos con sus incertidumbres y un registro de decisiones de edición;
- una comparación con una fuente o un resultado de referencia;
- el código y los datos para repetirlo.

Los bloques de la ruta aportan ejercicios y laboratorios para cada pieza; guarda la primera versión y los cambios.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional verificada. Referencia de trabajo consultada (2026-11-05):

- 📘 **ALMA Observatory** — página «About ALMA» (https://www.almaobservatory.org/en/about-alma/): describe el observatorio en la meseta de Chajnantor, construido por ESO, NRAO y NAOJ con la República de Chile; 66 antenas de alta precisión, longitudes de onda de 0,32 a 3,6 mm.

Las normas de protección del espectro y de acceso a tiempo de observación dependen de cada observatorio y de la regulación vigente, y no están verificadas aquí.

## 📈 Progresión del rol

Rutas habituales: **ingeniero/a o científico/a de datos de radio → especialista en calibración o en receptores → responsable de un instrumento o de un flujo de reducción**. Se abren la instrumentación de telecomunicaciones y la metrología de tiempo y frecuencia. No se publican cifras salariales por no poder verificarlas.

Roles vecinos con los que se comparte formación: [Ingeniería óptica y telescopios profesionales](ingenieria-optica-y-telescopios-profesionales.md), [Telecomunicaciones y estaciones terrestres espaciales](telecomunicaciones-y-estaciones-terrestres-espaciales.md) y [Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md).

## ⚠️ Mitos y errores comunes

- **«El radiotelescopio solo escucha».** Mide potencia, fase y polarización, y su análisis es tan exigente como el óptico.
- **«Más antenas es siempre mejor imagen».** Sin buena calibración y cobertura de líneas de base, la imagen se degrada.
- **«La interferencia es un detalle».** Es uno de los límites principales del oficio.
- **«El dato calibrado es la verdad».** Es la mejor estimación posible con los errores que no se pudieron eliminar.
- **«Es solo electrónica».** Es electrónica, física de ondas, estadística y programación juntas.

## 🚀 Siguientes pasos

1. **Asienta la base** con el área A01 y la física de ondas de tu diagnóstico.
2. Estudia **radioastronomía** ([**B46** · Radioastronomía e interferometría](../programa/tronco-comun/B46-radioastronomia-e-interferometria.md)) y **señales e imágenes** ([**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md)).
3. Profundiza en **antenas y receptores** ([**B49** · Antenas y receptores de radioastronomía](../programa/tronco-comun/B49-antenas-y-receptores-de-radioastronomia.md)).
4. Avanza a **interferometría y reducción de datos** ([**B51** · Interferometría avanzada y reducción de datos de radio](../programa/tronco-comun/B51-interferometria-avanzada-y-reduccion-de-datos-de-radio.md)).
5. Reúne tu **análisis documentado** con su historial.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Ingeniería óptica y telescopios profesionales](ingenieria-optica-y-telescopios-profesionales.md) · [Telecomunicaciones y estaciones terrestres espaciales](telecomunicaciones-y-estaciones-terrestres-espaciales.md) · [Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R04-radioastronomia-e-interferometria/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
