# 🌍 Observación terrestre y geointeligencia científica

> Conviertes lo que miden los satélites que miran la Tierra en información que alguien puede usar: un mapa de deformación, una serie de cambio de cobertura, una alerta de inundación. Cubres la cadena entera, del sensor al usuario, con incertidumbre honesta.
>
> **Nivel de entrada:** base de matemática, estadística y programación; hace falta soltura para trabajar con datos grandes · **Foco:** calibración y corrección, radar e interferometría, validación estadística, formatos y catálogos geoespaciales · **Entrega:** productos con metadatos y trazabilidad, informes de calidad e incertidumbre, mapas reproducibles y propuestas técnicas de servicio

## 🧭 Qué es y por qué importa

Un satélite de observación no entrega «la verdad»: entrega números de un sensor, con una geometría, una atmósfera de por medio y un instante concreto. Convertir eso en una decisión (¿se hundió esta ladera?, ¿cuánta superficie se quemó?, ¿está subiendo el agua?) exige un oficio: elegir el sensor y la fecha, calibrar y corregir, medir o clasificar, **validar con datos de referencia** y publicar con metadatos y una incertidumbre honesta.

«Geointeligencia científica» significa aquí **análisis geoespacial con método científico**, reproducible, con incertidumbre y fuentes. No es inteligencia de seguridad ni vigilancia de personas.

Los sensores se agrupan en dos familias que debes dominar: los **activos**, que emiten su propia energía (radar, LiDAR, altímetros), y los **pasivos**, que detectan la que emite o refleja el entorno (óptico, térmico). Cada uno responde mejor a ciertas preguntas, y todos cargan compromisos entre cuatro resoluciones: espacial, espectral, radiométrica y temporal ([**B57** · Observación terrestre y geociencias orbitales](../programa/tronco-comun/B57-observacion-terrestre-y-geociencias-orbitales.md)).

El rol se vive en tres miradas:

- **Procesamiento y calidad.** Calibración, corrección atmosférica y geométrica, productos listos para análisis. Su pregunta: *¿puedo confiar en este dato?*
- **Análisis y producto.** Índices, interferogramas, clasificaciones, modelos de elevación y detección de cambios ([**B69** · Radar de apertura sintética e interferometría (profundización)](../programa/tronco-comun/B69-radar-de-apertura-sintetica-e-interferometria-profundizacion.md)). Su pregunta: *¿qué dice esto, con qué error?*
- **Servicio y datos.** Catálogos, formatos, versiones y reproducibilidad para que otros usen el producto. Su pregunta: *¿alguien más puede repetirlo y entenderlo?*

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es ciencia planetaria.** [Ciencias planetarias y astrogeología](ciencias-planetarias-y-astrogeologia.md) usa técnicas parecidas (cartografía, altimetría) sobre otros cuerpos; en la Tierra puedes verificar en terreno, y eso cambia el rigor que se te exige.
- **No es matemática y computación científica pura.** [Matemática y computación científica espacial](matematica-y-computacion-cientifica-espacial.md) construye métodos y herramientas; tú los aplicas a un producto con un usuario.
- **No es seguridad ni defensa.** [Seguridad, defensa y resiliencia de infraestructuras espaciales](seguridad-defensa-y-resiliencia-de-infraestructuras-espaciales.md) protege activos orbitales; tú no analizas objetos orbitales ni operas con fines militares.
- **No es ingeniería de satélites.** Consumes el instrumento y especificas qué necesitas; no integras el satélite.
- **No es heliofísica ni clima espacial**, aunque «clima» aparezca en los dos nombres: aquí se mira la Tierra, no el Sol.
- **No es desarrollo de software puro.** Programas, pero cada cifra debe tener sentido físico y una cota de error.

## 🗓️ Un día en el puesto

Se parte de una pregunta de un usuario: *«¿se hundió esta ladera?»*. A partir de ahí:

- **Elegir sensor y fecha** según resolución, cobertura de nubes y frecuencia de revisita.
- **Descargar y comprobar el nivel de procesado**, y anotar versiones.
- **Corregir o verificar** la corrección atmosférica y radiométrica.
- **Generar el producto:** un índice, un interferograma, una clasificación.
- **Compararlo con datos de referencia** y estimar el error (matriz de confusión, puntos de control).
- **Escribir un informe** que diga qué se puede concluir y qué no.

Una parte importante del día son tareas de datos: catálogos, formatos, versiones, reproducibilidad. La habilidad central es **saber cuándo un resultado no es suficientemente fiable como para decidir algo con él**.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Resoluciones y sensores:** compromisos entre las cuatro resoluciones; sensores activos y pasivos ([**B57** · Observación terrestre y geociencias orbitales](../programa/tronco-comun/B57-observacion-terrestre-y-geociencias-orbitales.md)).
- **Radiometría y calibración:** de cuentas digitales a magnitud física; corrección atmosférica; índices espectrales ([**B44** · Detectores y adquisición astronómica](../programa/tronco-comun/B44-detectores-y-adquisicion-astronomica.md), [**B45** · Espectroscopía, fotometría y polarimetría](../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md)).
- **Radar e interferometría:** radar de apertura sintética, coherencia y desplazamiento ([**B69** · Radar de apertura sintética e interferometría (profundización)](../programa/tronco-comun/B69-radar-de-apertura-sintetica-e-interferometria-profundizacion.md)); altimetría y LiDAR.
- **Estadística aplicada:** muestreo, incertidumbre, validación y falsos positivos ([**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md)).
- **Geometría y datos:** coordenadas, proyecciones, formatos, catálogos y servicios estándar ([**B04** · Álgebra, trigonometría y geometría espacial](../programa/tronco-comun/B04-algebra-trigonometria-y-geometria-espacial.md), [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md)).
- **Aprendizaje automático:** clasificación supervisada, con validación fuera de la región de entrenamiento ([**B17** · Aprendizaje automático científico](../programa/tronco-comun/B17-aprendizaje-automatico-cientifico.md)).
- **Programación y entornos reproducibles** ([**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md)).

### Herramientas del oficio

```text
Datos:               catálogos y portales de datos abiertos de observación de la Tierra
Procesado:           software de corrección radiométrica y atmosférica, cadenas de radar (SAR)
Análisis geoespacial: bibliotecas y sistemas de información geográfica, Python (NumPy, SciPy)
Aprendizaje:         bibliotecas de aprendizaje automático con validación espacial
Reproducibilidad:    cuadernos, control de versiones, contenedores, metadatos y formatos abiertos
Calidad:             matrices de error, puntos de control, informes de incertidumbre
```

Estas son categorías; los programas y bibliotecas concretos son una decisión del equipo y este programa no los recomienda por marca. La herramienta calcula; tú decides si el resultado tiene sentido físico.

### Habilidades no técnicas

- **Pensamiento crítico ante el dato:** desconfiar de un mapa bonito sin matriz de error.
- **Comunicación de la incertidumbre:** decirle a quien decide qué se puede y qué no se puede concluir.
- **Orden y reproducibilidad:** versiones, metadatos y semillas; otro debe poder repetir tu producto.
- **Criterio ético:** privacidad, uso dual y licencias antes de publicar.
- **Trabajo con usuarios:** traducir su pregunta a una medición posible.

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md) — A02 · 20 clases
2. 📚 [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) — A02 · 20 clases
3. 📚 [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) — A02 · 26 clases
4. 📚 [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) — A02 · 20 clases

### 🎯 El núcleo del rol

**A01 · Alfabetización científica, astronómica y tecnológica**

1. 📚 [**B04** · Álgebra, trigonometría y geometría espacial](../programa/tronco-comun/B04-algebra-trigonometria-y-geometria-espacial.md) — usa 3 de 20 clases: `B04-` C11, C17, C19
2. 📚 [**B07** · Informática científica desde cero](../programa/tronco-comun/B07-informatica-cientifica-desde-cero.md) — usa 1 de 20 clases: `B07-` C19

**A02 · Matemática, física computacional y métodos científicos**

3. 📚 [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) — usa 2 de 26 clases: `B12-` C16, C18
4. 📚 [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) — usa 8 de 23 clases: `B13-` C05, C11, C13, C17–C20, C23
5. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — usa 11 de 31 clases: `B14-` C09, C11–C12, C19, C25–C31
6. 📚 [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) — usa 3 de 24 clases: `B15-` C22–C24
7. 📚 [**B17** · Aprendizaje automático científico](../programa/tronco-comun/B17-aprendizaje-automatico-cientifico.md) — usa 3 de 12 clases: `B17-` C10–C12

**A04 · Óptica, telescopios y observatorios científicos**

8. 📚 [**B44** · Detectores y adquisición astronómica](../programa/tronco-comun/B44-detectores-y-adquisicion-astronomica.md) — usa 4 de 20 clases: `B44-` C12–C14, C20
9. 📚 [**B45** · Espectroscopía, fotometría y polarimetría](../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md) — usa 1 de 24 clases: `B45-` C01
10. 📚 [**B47** · Instrumentación y observatorios espaciales](../programa/tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md) — usa 1 de 25 clases: `B47-` C15

**A05 · Ciencias planetarias, astroquímica y habitabilidad**

11. 📚 [**B53** · Astrogeología y geodesia planetaria](../programa/tronco-comun/B53-astrogeologia-y-geodesia-planetaria.md) — usa 1 de 30 clases: `B53-` C07
12. 📚 [**B57** · Observación terrestre y geociencias orbitales](../programa/tronco-comun/B57-observacion-terrestre-y-geociencias-orbitales.md) — usa 30 de 34 clases: `B57-` C02–C09, C11–C12, C14–C18, C20–C34
13. 📚 [**B69** · Radar de apertura sintética e interferometría (profundización)](../programa/tronco-comun/B69-radar-de-apertura-sintetica-e-interferometria-profundizacion.md) — usa 7 de 7 clases: `B69-` C01–C07

**A07 · Ingeniería y construcción de sistemas espaciales**

14. 📚 [**B83** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) — usa 2 de 24 clases: `B83-` C01–C02
15. 📚 [**B89** · Comunicaciones y navegación satelital](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) — usa 1 de 25 clases: `B89-` C17
16. 📚 [**B90** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) — usa 1 de 24 clases: `B90-` C16

**A08 · Operaciones de misión y robótica espacial**

17. 📚 [**B96** · Control y operación de misiones espaciales](../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) — usa 2 de 30 clases: `B96-` C13, C20

**A11 · Economía, industria y gestión de proyectos espaciales**

18. 📚 [**B124** · Industria, economía, ética y proyectos espaciales](../programa/tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) — usa 5 de 24 clases: `B124-` C04, C13, C19, C21–C22

<!-- /ruta -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es un **portafolio de productos reproducibles** (con datos públicos):

- un mapa multiespectral con código, datos, versiones, unidades y proyección declaradas, y su matriz de error;
- un interferograma con su evaluación de coherencia y una lectura prudente del desplazamiento;
- un modelo de elevación validado con puntos de control;
- un informe de calidad radiométrica;
- un catálogo de escenas con metadatos;
- un caso de desastre analizado con su tasa de falsos positivos.

Guarda la primera versión, la retroalimentación y los cambios. Cada producto debe poder repetirlo otra persona desde tus datos y tu código.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional única verificada. Las referencias que sí se consultaron (2026-11-05) son:

- 📘 **NASA Earthdata, «Earth Observation Data Basics»** — el sitio indica actualización el 3 de noviembre de 2026. Distingue sensores activos de pasivos y enumera cuatro resoluciones (radiométrica, espacial, espectral y temporal); la página no define las resoluciones radiométrica y espectral, por lo que el programa las apoya en B57-C02 y B57-C03. (https://www.earthdata.nasa.gov/learn/backgrounders/remote-sensing)
- 📗 **CEOS (Comité de Satélites de Observación de la Tierra), «Analysis Ready Data»** — define esos productos como datos satelitales procesados con un conjunto mínimo de requisitos para facilitar el análisis, y lista familias como reflectancia de superficie, temperatura de superficie, reflectancia acuática, luz nocturna y radar combinado, cada una con su versión de especificación. (https://ceos.org/ard/)

Las certificaciones personales, las normas de calidad de datos y las licencias de cada proveedor dependen de la jurisdicción y de la versión vigente, y **no están verificadas aquí**. Consúltalas en su fuente oficial.

## 📈 Progresión del rol

Rutas habituales: **analista que ejecuta cadenas de procesado y valida productos → especialista que diseña métodos y asume incertidumbres → responsable de servicios o de especificación de instrumentos**. Desde el análisis se abren la ciencia de datos geoespaciales, la gestión de riesgo de desastres y la especificación de misiones. Los niveles y requisitos dependen de cada organización; no se publican cifras salariales porque no se pudieron verificar con fuentes.

Roles vecinos con los que se comparte formación: [ciencias planetarias y astrogeología](ciencias-planetarias-y-astrogeologia.md), [matemática y computación científica](matematica-y-computacion-cientifica-espacial.md) y [seguridad y resiliencia](seguridad-defensa-y-resiliencia-de-infraestructuras-espaciales.md).

## ⚠️ Mitos y errores comunes

- **«Más resolución es siempre mejor.»** Las cuatro resoluciones se compensan; más detalle espacial puede significar menos cobertura o menor revisita.
- **«Un mapa de clasificación se explica solo.»** Sin matriz de error y validación con datos de referencia es una ilustración, no una medición.
- **«Un modelo entrenado en una región sirve en otra.»** No se traslada sin validarlo.
- **«El radar ve a través de todo.»** Puede penetrar nubes, pero tiene sus propios artefactos y sus límites de coherencia.
- **«Una alerta temprana siempre ayuda.»** Un falso positivo o negativo tiene costo para comunidades reales; se comunica la incertidumbre y la decisión corresponde a la autoridad competente.
- **«Los datos abiertos se usan sin condiciones.»** Se respetan licencias y se citan las fuentes; la resolución puede revelar a personas y propiedades.

## 🚀 Siguientes pasos

1. **Asienta la base** con [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md), [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md), [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) y [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md).
2. Aprende los sensores y las resoluciones con [**B57** · Observación terrestre y geociencias orbitales](../programa/tronco-comun/B57-observacion-terrestre-y-geociencias-orbitales.md) y produce un índice espectral reproducible.
3. Incorpora el análisis de incertidumbre con [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) y [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md): matriz de error y puntos de control.
4. Profundiza en radar con [**B69** · Radar de apertura sintética e interferometría (profundización)](../programa/tronco-comun/B69-radar-de-apertura-sintetica-e-interferometria-profundizacion.md) y evalúa la coherencia de un interferograma.
5. Reúne tu **portafolio** de productos reproducibles; si te atrae el aprendizaje automático, suma [**B17** · Aprendizaje automático científico](../programa/tronco-comun/B17-aprendizaje-automatico-cientifico.md).

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Ciencias planetarias y astrogeología](ciencias-planetarias-y-astrogeologia.md) · [Matemática y computación científica espacial](matematica-y-computacion-cientifica-espacial.md) · [Seguridad defensa y resiliencia de infraestructuras espaciales](seguridad-defensa-y-resiliencia-de-infraestructuras-espaciales.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R16-observacion-terrestre-y-geointeligencia-cientifica/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
