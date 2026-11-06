# 🪐 Ciencias planetarias y astrogeología

> Estudias la geología y la física de los cuerpos del sistema solar: su forma, interior, superficie, volcanes, impactos y hielos, con datos de misiones y mapas.
>
> **Nivel de entrada:** geología o física de nivel universitario, más manejo de datos geoespaciales y programación; rol de investigación · **Foco:** geodesia, geofísica de interiores, geomorfología, impactos, vulcanismo, criósferas, cartografía y muestras · **Entrega:** mapas y análisis geológicos de cuerpos planetarios, con datos de procedencia verificable y su incertidumbre

## 🧭 Qué es y por qué importa

Las ciencias planetarias aplican la geología, la geofísica y la química a otros mundos. No hay afloramientos que visitar: se trabaja con **imágenes, topografía, datos gravitacionales, espectros y, para unos pocos cuerpos, muestras traídas a la Tierra**. De ahí se infieren la historia de una superficie, la estructura de un interior o la edad relativa de unidades geológicas.

Según su propia página, el Planetary Data System (PDS) de la NASA es un archivo de largo plazo, gestionado activamente por científicos planetarios, que contiene los productos digitales devueltos por las misiones planetarias de la NASA y también datos de observaciones desde tierra y de experimentos de laboratorio. Ese archivo es el insumo cotidiano del rol.

Las miradas del rol son:

- **Superficie y procesos.** Geomorfología, cráteres, vulcanismo y criósferas. Su pregunta es: *¿qué procesos formaron esta superficie y cuándo?*
- **Interior.** Geofísica y geodesia: forma, gravedad, rotación. Su pregunta es: *¿qué estructura interna explica estas mediciones?*
- **Mapas y muestras.** Cartografía, estratigrafía y análisis de materiales. Su pregunta es: *¿qué evidencia sostiene esta unidad geológica?*

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es astrobiología.** Esta busca habitabilidad y vida; tú caracterizas el cuerpo ([Astroquímica y astrobiología](astroquimica-y-astrobiologia.md)).
- **No es observación de la Tierra.** Usa herramientas parecidas (teledetección, SAR) pero otro objeto de estudio ([Observación terrestre y geointeligencia científica](observacion-terrestre-y-geointeligencia-cientifica.md)).
- **No es ingeniería de misión.** Tú eres usuario de los datos de una misión, no su diseñador.
- **No es geología terrestre simplificada.** Las condiciones (gravedad, atmósfera, composición) cambian los procesos y exigen razonamiento propio.

## 🗓️ Un día en el puesto

- **Acceso a datos:** localizas un conjunto de imágenes o de altimetría en un archivo y verificas su procesamiento y su marco de coordenadas.
- **Mapeo y análisis:** delimitas unidades, mides cráteres o estimas pendientes.
- **Modelo:** contrastas una hipótesis (un flujo volcánico, un impacto) con la topografía o la gravedad.
- **Escritura:** documentas cómo llegaste a una unidad y cuánta incertidumbre tiene.

Dicho sin adornos: **el sistema de coordenadas y la calibración** son el error más frecuente y el menos glamoroso.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Astrogeología y geodesia planetaria:** forma, topografía, cartografía ([**B34** · Astrogeología y geodesia planetaria](../programa/tronco-comun/B34-astrogeologia-y-geodesia-planetaria.md)).
- **Geofísica de interiores:** estructura, gravedad, térmica ([**B89** · Geofísica de interiores planetarios](../PROGRAMA_ACADEMICO_COMPLETO.md#b89--geofísica-de-interiores-planetarios)).
- **Geomorfología y procesos superficiales** ([**B90** · Geomorfología y procesos superficiales planetarios](../PROGRAMA_ACADEMICO_COMPLETO.md#b90--geomorfología-y-procesos-superficiales-planetarios)); **cráteres de impacto** ([**B85** · Cráteres de impacto y geología de impactos](../PROGRAMA_ACADEMICO_COMPLETO.md#b85--cráteres-de-impacto-y-geología-de-impactos)); **vulcanismo planetario** ([**B94** · Vulcanismo planetario](../PROGRAMA_ACADEMICO_COMPLETO.md#b94--vulcanismo-planetario)).
- **Atmósferas, química y astrobiología:** contexto de los procesos ([**B35** · Atmósferas y climatología planetaria](../programa/tronco-comun/B35-atmosferas-y-climatologia-planetaria.md), [**B36** · Astroquímica y geoquímica extraterrestre](../programa/tronco-comun/B36-astroquimica-y-geoquimica-extraterrestre.md), [**B37** · Astrobiología y vida extraterrestre](../programa/tronco-comun/B37-astrobiologia-y-vida-extraterrestre.md)).
- **Exploración in situ y muestras** ([**B87** · Exploración in situ y análisis de muestras planetarias](../PROGRAMA_ACADEMICO_COMPLETO.md#b87--exploración-in-situ-y-análisis-de-muestras-planetarias)).
- **Datos, estadística y computación** ([**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md), [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md)).

### Herramientas del oficio

```text
Datos:                archivos de misiones (por ejemplo, el Planetary Data System)
SIG:                  software de información geográfica y de mapeo planetario
Análisis:             Python científico, procesamiento de imágenes
Modelos:              modelos geofísicos y térmicos simples
Documentación:        registro de procedencia de datos y de decisiones
```

Un mapa bien dibujado sobre un dato mal georreferenciado es un error elegante. El marco de coordenadas y la calibración son tu responsabilidad.

### Habilidades no técnicas

- **Razonamiento por analogía con cautela:** comparar con la Tierra sin forzar la comparación.
- **Escritura científica clara.**
- **Paciencia con datos incompletos.**
- **Trabajo colaborativo con equipos de misión.**

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md) — A02 · 20 clases
2. 📚 [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) — A02 · 20 clases
3. 📚 [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) — A02 · 26 clases
4. 📚 [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) — A02 · 24 clases
5. 📚 [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) — A02 · 20 clases
6. 📚 [**B35** · Atmósferas y climatología planetaria](../programa/tronco-comun/B35-atmosferas-y-climatologia-planetaria.md) — A05 · 20 clases
7. 📚 [**B40** · Recursos in situ y sostenibilidad extraterrestre](../programa/tronco-comun/B40-recursos-in-situ-y-sostenibilidad-extraterrestre.md) — A05 · 23 clases

### 🎯 El núcleo del rol

**A01 · Alfabetización científica, astronómica y tecnológica**

1. 📚 [**B06** · Química y materia del universo](../programa/tronco-comun/B06-quimica-y-materia-del-universo.md) — usa 2 de 20 clases: `B06-` C19–C20

**A02 · Matemática, física computacional y métodos científicos**

2. 📚 [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) — usa 3 de 26 clases: `B12-` C03, C16, C20
3. 📚 [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) — usa 4 de 23 clases: `B13-` C11, C14, C18, C20
4. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — usa 1 de 31 clases: `B14-` C21

**A04 · Óptica, telescopios y observatorios científicos**

5. 📚 [**B29** · Espectroscopía, fotometría y polarimetría](../programa/tronco-comun/B29-espectroscopia-fotometria-y-polarimetria.md) — usa 1 de 24 clases: `B29-` C14
6. 📚 [**B31** · Instrumentación y observatorios espaciales](../programa/tronco-comun/B31-instrumentacion-y-observatorios-espaciales.md) — usa 1 de 25 clases: `B31-` C08

**A05 · Ciencias planetarias, astroquímica y habitabilidad**

7. 📚 [**B33** · Formación y dinámica de sistemas planetarios](../programa/tronco-comun/B33-formacion-y-dinamica-de-sistemas-planetarios.md) — usa 1 de 20 clases: `B33-` C18
8. 📚 [**B34** · Astrogeología y geodesia planetaria](../programa/tronco-comun/B34-astrogeologia-y-geodesia-planetaria.md) — usa 25 de 30 clases: `B34-` C01–C15, C17–C26
9. 📚 [**B36** · Astroquímica y geoquímica extraterrestre](../programa/tronco-comun/B36-astroquimica-y-geoquimica-extraterrestre.md) — usa 6 de 20 clases: `B36-` C06, C10, C12, C15, C18–C19
10. 📚 [**B37** · Astrobiología y vida extraterrestre](../programa/tronco-comun/B37-astrobiologia-y-vida-extraterrestre.md) — usa 4 de 21 clases: `B37-` C06, C09–C10, C17
11. 📚 [**B38** · Observación terrestre y geociencias orbitales](../programa/tronco-comun/B38-observacion-terrestre-y-geociencias-orbitales.md) — usa 5 de 34 clases: `B38-` C01, C05, C10, C18–C19
12. 📚 [**B39** · Asteroides, cometas y defensa planetaria](../programa/tronco-comun/B39-asteroides-cometas-y-defensa-planetaria.md) — usa 1 de 20 clases: `B39-` C15
13. 📚 [**B85** · Cráteres de impacto y geología de impactos](../PROGRAMA_ACADEMICO_COMPLETO.md#b85--cráteres-de-impacto-y-geología-de-impactos) — usa 7 de 7 clases: `B85-` C01–C07
14. 📚 [**B87** · Exploración in situ y análisis de muestras planetarias](../PROGRAMA_ACADEMICO_COMPLETO.md#b87--exploración-in-situ-y-análisis-de-muestras-planetarias) — usa 3 de 6 clases: `B87-` C01–C03
15. 📚 [**B89** · Geofísica de interiores planetarios](../PROGRAMA_ACADEMICO_COMPLETO.md#b89--geofísica-de-interiores-planetarios) — usa 6 de 6 clases: `B89-` C01–C06
16. 📚 [**B90** · Geomorfología y procesos superficiales planetarios](../PROGRAMA_ACADEMICO_COMPLETO.md#b90--geomorfología-y-procesos-superficiales-planetarios) — usa 5 de 5 clases: `B90-` C01–C05
17. 📚 [**B94** · Vulcanismo planetario](../PROGRAMA_ACADEMICO_COMPLETO.md#b94--vulcanismo-planetario) — usa 7 de 7 clases: `B94-` C01–C07

**A06 · Mecánica orbital, navegación y vuelo espacial**

18. 📚 [**B44** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B44-estimacion-de-orbitas-y-navegacion-espacial.md) — usa 2 de 30 clases: `B44-` C04, C07

**A07 · Ingeniería y construcción de sistemas espaciales**

19. 📚 [**B55** · Comunicaciones y navegación satelital](../programa/tronco-comun/B55-comunicaciones-y-navegacion-satelital.md) — usa 1 de 25 clases: `B55-` C15

**A11 · Economía, industria y gestión de proyectos espaciales**

20. 📚 [**B64** · Industria, economía, ética y proyectos espaciales](../programa/tronco-comun/B64-industria-economia-etica-y-proyectos-espaciales.md) — usa 1 de 24 clases: `B64-` C19

<!-- /ruta -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es un **análisis geológico de un cuerpo con datos abiertos**:

- una pregunta geológica acotada y los datos de procedencia verificable;
- un mapa o un conjunto de mediciones con su marco de coordenadas declarado;
- una interpretación con hipótesis alternativas y su incertidumbre;
- el flujo de procesamiento documentado para repetirlo.

Los bloques de la ruta aportan ejercicios y laboratorios; guarda la primera versión y sus cambios.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional verificada. Referencia de trabajo consultada (2026-11-05):

- 📘 **NASA Planetary Data System** — https://pds.nasa.gov/: archivo de largo plazo de los productos digitales devueltos por las misiones planetarias de la NASA, más datos de observaciones desde tierra y de laboratorio.

Los requisitos para publicar o para acceder a muestras dependen de cada institución y no están verificados aquí.

## 📈 Progresión del rol

Rutas habituales: **grado en geología, física o ciencias planetarias → posgrado → investigación en una institución → liderazgo de un análisis de misión**. Se abren la geoinformática y la ciencia de datos geoespaciales. No se publican cifras salariales por no poder verificarlas.

Roles vecinos con los que se comparte formación: [Astroquímica y astrobiología](astroquimica-y-astrobiologia.md), [Observación terrestre y geointeligencia científica](observacion-terrestre-y-geointeligencia-cientifica.md) y [Recursos extraterrestres y economía industrial espacial](recursos-extraterrestres-y-economia-industrial-espacial.md).

## ⚠️ Mitos y errores comunes

- **«Todo está en una foto».** La interpretación exige topografía, composición y contexto.
- **«Los cráteres cuentan toda la historia».** Datan superficies con supuestos que hay que declarar.
- **«Si es como la Tierra, funciona igual».** La gravedad, la atmósfera y la composición cambian el resultado.
- **«El archivo de datos ya está limpio».** Cada producto tiene un procesamiento que hay que entender.
- **«Es geología fácil».** Con datos remotos, es geología con menos evidencia directa y más inferencia.

## 🚀 Siguientes pasos

1. **Asienta la base** con el área A01 (física y química) y la matemática de tu diagnóstico.
2. Estudia **astrogeología y geodesia planetaria** ([**B34** · Astrogeología y geodesia planetaria](../programa/tronco-comun/B34-astrogeologia-y-geodesia-planetaria.md)) y **atmósferas** ([**B35** · Atmósferas y climatología planetaria](../programa/tronco-comun/B35-atmosferas-y-climatologia-planetaria.md)).
3. Profundiza en **geomorfología** ([**B90** · Geomorfología y procesos superficiales planetarios](../PROGRAMA_ACADEMICO_COMPLETO.md#b90--geomorfología-y-procesos-superficiales-planetarios)), **impactos** ([**B85** · Cráteres de impacto y geología de impactos](../PROGRAMA_ACADEMICO_COMPLETO.md#b85--cráteres-de-impacto-y-geología-de-impactos)) y **vulcanismo** ([**B94** · Vulcanismo planetario](../PROGRAMA_ACADEMICO_COMPLETO.md#b94--vulcanismo-planetario)).
4. Aprende **geofísica de interiores** ([**B89** · Geofísica de interiores planetarios](../PROGRAMA_ACADEMICO_COMPLETO.md#b89--geofísica-de-interiores-planetarios)) y el análisis de **muestras** ([**B87** · Exploración in situ y análisis de muestras planetarias](../PROGRAMA_ACADEMICO_COMPLETO.md#b87--exploración-in-situ-y-análisis-de-muestras-planetarias)).
5. Reúne tu **análisis con datos abiertos** y su historial.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Astroquímica y astrobiología](astroquimica-y-astrobiologia.md) · [Observación terrestre y geointeligencia científica](observacion-terrestre-y-geointeligencia-cientifica.md) · [Recursos extraterrestres y economía industrial espacial](recursos-extraterrestres-y-economia-industrial-espacial.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R05-ciencias-planetarias-y-astrogeologia/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
