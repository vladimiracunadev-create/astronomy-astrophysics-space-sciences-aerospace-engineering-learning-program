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

- **Astrogeología y geodesia planetaria:** forma, topografía, cartografía ([**B53** · Astrogeología y geodesia planetaria](../programa/tronco-comun/B53-astrogeologia-y-geodesia-planetaria.md)).
- **Geofísica de interiores:** estructura, gravedad, térmica ([**B65** · Geofísica de interiores planetarios](../programa/tronco-comun/B65-geofisica-de-interiores-planetarios.md)).
- **Geomorfología y procesos superficiales** ([**B66** · Geomorfología y procesos superficiales planetarios](../programa/tronco-comun/B66-geomorfologia-y-procesos-superficiales-planetarios.md)); **cráteres de impacto** ([**B61** · Cráteres de impacto y geología de impactos](../programa/tronco-comun/B61-crateres-de-impacto-y-geologia-de-impactos.md)); **vulcanismo planetario** ([**B70** · Vulcanismo planetario](../programa/tronco-comun/B70-vulcanismo-planetario.md)).
- **Atmósferas, química y astrobiología:** contexto de los procesos ([**B54** · Atmósferas y climatología planetaria](../programa/tronco-comun/B54-atmosferas-y-climatologia-planetaria.md), [**B55** · Astroquímica y geoquímica extraterrestre](../programa/tronco-comun/B55-astroquimica-y-geoquimica-extraterrestre.md), [**B56** · Astrobiología y vida extraterrestre](../programa/tronco-comun/B56-astrobiologia-y-vida-extraterrestre.md)).
- **Exploración in situ y muestras** ([**B63** · Exploración in situ y análisis de muestras planetarias](../programa/tronco-comun/B63-exploracion-in-situ-y-analisis-de-muestras-planetarias.md)).
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
6. 📚 [**B54** · Atmósferas y climatología planetaria](../programa/tronco-comun/B54-atmosferas-y-climatologia-planetaria.md) — A05 · 20 clases
7. 📚 [**B59** · Recursos in situ y sostenibilidad extraterrestre](../programa/tronco-comun/B59-recursos-in-situ-y-sostenibilidad-extraterrestre.md) — A05 · 23 clases

### 🎯 El núcleo del rol

**A01 · Alfabetización científica, astronómica y tecnológica**

1. 📚 [**B06** · Química y materia del universo](../programa/tronco-comun/B06-quimica-y-materia-del-universo.md) — usa 2 de 20 clases: `B06-` C19–C20

**A02 · Matemática, física computacional y métodos científicos**

2. 📚 [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) — usa 3 de 26 clases: `B12-` C03, C16, C20
3. 📚 [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) — usa 4 de 23 clases: `B13-` C11, C14, C18, C20
4. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — usa 1 de 31 clases: `B14-` C21

**A04 · Óptica, telescopios y observatorios científicos**

5. 📚 [**B45** · Espectroscopía, fotometría y polarimetría](../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md) — usa 1 de 24 clases: `B45-` C14
6. 📚 [**B47** · Instrumentación y observatorios espaciales](../programa/tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md) — usa 1 de 25 clases: `B47-` C08

**A05 · Ciencias planetarias, astroquímica y habitabilidad**

7. 📚 [**B52** · Formación y dinámica de sistemas planetarios](../programa/tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md) — usa 1 de 20 clases: `B52-` C18
8. 📚 [**B53** · Astrogeología y geodesia planetaria](../programa/tronco-comun/B53-astrogeologia-y-geodesia-planetaria.md) — usa 25 de 30 clases: `B53-` C01–C15, C17–C26
9. 📚 [**B55** · Astroquímica y geoquímica extraterrestre](../programa/tronco-comun/B55-astroquimica-y-geoquimica-extraterrestre.md) — usa 6 de 20 clases: `B55-` C06, C10, C12, C15, C18–C19
10. 📚 [**B56** · Astrobiología y vida extraterrestre](../programa/tronco-comun/B56-astrobiologia-y-vida-extraterrestre.md) — usa 4 de 21 clases: `B56-` C06, C09–C10, C17
11. 📚 [**B57** · Observación terrestre y geociencias orbitales](../programa/tronco-comun/B57-observacion-terrestre-y-geociencias-orbitales.md) — usa 5 de 34 clases: `B57-` C01, C05, C10, C18–C19
12. 📚 [**B58** · Asteroides, cometas y defensa planetaria](../programa/tronco-comun/B58-asteroides-cometas-y-defensa-planetaria.md) — usa 1 de 20 clases: `B58-` C15
13. 📚 [**B61** · Cráteres de impacto y geología de impactos](../programa/tronco-comun/B61-crateres-de-impacto-y-geologia-de-impactos.md) — usa 7 de 7 clases: `B61-` C01–C07
14. 📚 [**B63** · Exploración in situ y análisis de muestras planetarias](../programa/tronco-comun/B63-exploracion-in-situ-y-analisis-de-muestras-planetarias.md) — usa 3 de 6 clases: `B63-` C01–C03
15. 📚 [**B65** · Geofísica de interiores planetarios](../programa/tronco-comun/B65-geofisica-de-interiores-planetarios.md) — usa 6 de 6 clases: `B65-` C01–C06
16. 📚 [**B66** · Geomorfología y procesos superficiales planetarios](../programa/tronco-comun/B66-geomorfologia-y-procesos-superficiales-planetarios.md) — usa 5 de 5 clases: `B66-` C01–C05
17. 📚 [**B70** · Vulcanismo planetario](../programa/tronco-comun/B70-vulcanismo-planetario.md) — usa 7 de 7 clases: `B70-` C01–C07

**A06 · Mecánica orbital, navegación y vuelo espacial**

18. 📚 [**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md) — usa 2 de 30 clases: `B74-` C04, C07

**A07 · Ingeniería y construcción de sistemas espaciales**

19. 📚 [**B89** · Comunicaciones y navegación satelital](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) — usa 1 de 25 clases: `B89-` C15

**A11 · Economía, industria y gestión de proyectos espaciales**

20. 📚 [**B124** · Industria, economía, ética y proyectos espaciales](../programa/tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) — usa 1 de 24 clases: `B124-` C19

<!-- /ruta -->

<!-- recorrido:inicio -->
### 🗺️ Recorrido módulo por módulo

El rol se estudia en **8 módulos** de 10 temas cada uno (cada tema es un par «concepto + aplicación»). Haz el diagnóstico, avanza por los módulos **en orden** y cierra cada uno con su checkpoint; al final, el proyecto y el criterio de salida.

**🩺 Diagnóstico de entrada.** Si respondes «no sé» a dos o más, empieza por los fundamentos de arriba:

- ¿Puedes calcular la gravedad superficial de un cuerpo a partir de su masa y radio?
- ¿Distingues roca ígnea, sedimentaria y metamórfica?
- ¿Sabes leer un mapa con curvas de nivel y una escala?
- ¿Puedes calcular edades relativas por conteo de cráteres?

#### R05-M01 · Geodesia planetaria

1. **Marcos de coordenadas planetarias** — [`B53-C05`](../programa/clases/B53/B53-C05-sistemas-de-coordenadas-lunares/CLASE.md), [`B53-C06`](../programa/clases/B53/B53-C06-geodesia-de-marte/CLASE.md)
2. **Rotación y orientación de cuerpos** — [`B53-C21`](../programa/clases/B53/B53-C21-rotacion-y-orientacion-de-cuerpos-planetarios-polos-y-meridiano-origen/CLASE.md)
3. **Geoides planetarios** — [`B53-C04`](../programa/clases/B53/B53-C04-geoides-y-elipsoides/CLASE.md)
4. **Gravedad por armónicos** — [`B53-C03`](../programa/clases/B53/B53-C03-campo-gravitatorio-planetario/CLASE.md)
5. **Medición de campo gravitatorio** — [`B53-C03`](../programa/clases/B53/B53-C03-campo-gravitatorio-planetario/CLASE.md), [`B74-C04`](../programa/clases/B74/B74-C04-doppler-de-navegacion/CLASE.md)
6. **Altimetría láser** — [`B53-C07`](../programa/clases/B53/B53-C07-topografia-por-altimetria/CLASE.md)
7. **Topografía radial** — [`B53-C07`](../programa/clases/B53/B53-C07-topografia-por-altimetria/CLASE.md), [`B53-C04`](../programa/clases/B53/B53-C04-geoides-y-elipsoides/CLASE.md)
8. **Geodesia Doppler** — [`B74-C04`](../programa/clases/B74/B74-C04-doppler-de-navegacion/CLASE.md), [`B89-C15`](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md)
9. **Geodesia satelital** — [`B57-C10`](../programa/clases/B57/B57-C10-geodesia-mediante-gnss/CLASE.md), [`B53-C06`](../programa/clases/B53/B53-C06-geodesia-de-marte/CLASE.md)
10. **Ajuste de sistemas de referencia** — [`B74-C07`](../programa/clases/B74/B74-C07-ajuste-por-minimos-cuadrados/CLASE.md), [`B13-C11`](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md), [`B53-C05`](../programa/clases/B53/B53-C05-sistemas-de-coordenadas-lunares/CLASE.md)

✅ **Checkpoint R05-M01.** Sin mirar el material, explica cómo se relacionan «Marcos de coordenadas planetarias», «Altimetría láser» y «Ajuste de sistemas de referencia», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R05-M02 · Geofísica de interiores

1. **Diferenciación de interiores** — [`B52-C18`](../programa/clases/B52/B52-C18-diferenciacion-planetaria/CLASE.md), [`B53-C01`](../programa/clases/B53/B53-C01-interior-de-planetas-rocosos/CLASE.md)
2. **Densidad y momento de inercia** — [`B53-C01`](../programa/clases/B53/B53-C01-interior-de-planetas-rocosos/CLASE.md), [`B53-C03`](../programa/clases/B53/B53-C03-campo-gravitatorio-planetario/CLASE.md)
3. **Sismología lunar** — [`B53-C02`](../programa/clases/B53/B53-C02-sismologia-planetaria/CLASE.md)
4. **Sismología marciana** — [`B53-C02`](../programa/clases/B53/B53-C02-sismologia-planetaria/CLASE.md)
5. **Convección del manto** — [`B65-C01`](../programa/clases/B65/B65-C01-conveccion-del-manto-y-evolucion-termica-de-interiores-planetarios/CLASE.md)
6. **Dinamos planetarias** — [`B65-C02`](../programa/clases/B65/B65-C02-dinamos-planetarias-y-campos-magneticos-de-origen-interno/CLASE.md)
7. **Campo magnético residual** — [`B65-C03`](../programa/clases/B65/B65-C03-magnetismo-cortical-remanente-y-anomalias-magneticas/CLASE.md)
8. **Flujo térmico** — [`B65-C04`](../programa/clases/B65/B65-C04-flujo-termico-planetario-y-balance-termico-del-interior/CLASE.md)
9. **Modelos de estructura interior** — [`B53-C01`](../programa/clases/B53/B53-C01-interior-de-planetas-rocosos/CLASE.md), [`B53-C02`](../programa/clases/B53/B53-C02-sismologia-planetaria/CLASE.md), [`B53-C03`](../programa/clases/B53/B53-C03-campo-gravitatorio-planetario/CLASE.md)
10. **Validación con datos geofísicos** — [`B65-C05`](../programa/clases/B65/B65-C05-inversion-geofisica-conjunta-validacion-de-modelos-interiores/CLASE.md)

✅ **Checkpoint R05-M02.** Sin mirar el material, explica cómo se relacionan «Diferenciación de interiores», «Dinamos planetarias» y «Validación con datos geofísicos», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R05-M03 · Geomorfología comparada

1. **Morfología de cráteres** — [`B53-C08`](../programa/clases/B53/B53-C08-cartografia-de-crateres/CLASE.md), [`B53-C10`](../programa/clases/B53/B53-C10-geologia-de-impacto/CLASE.md)
2. **Valles y canales** — [`B66-C01`](../programa/clases/B66/B66-C01-valles-y-canales-morfologia-y-origen-en-superficies-planetarias/CLASE.md)
3. **Laderas y transporte** — [`B66-C02`](../programa/clases/B66/B66-C02-procesos-de-ladera-y-transporte-de-masa/CLASE.md)
4. **Formas de origen glaciar** — [`B53-C13`](../programa/clases/B53/B53-C13-geomorfologia-de-hielos/CLASE.md)
5. **Dunas y erosión eólica** — [`B66-C03`](../programa/clases/B66/B66-C03-procesos-eolicos-dunas-ripples-y-erosion-planetaria/CLASE.md)
6. **Sistemas fluviales fósiles** — [`B66-C04`](../programa/clases/B66/B66-C04-redes-fluviales-fosiles-y-paleohidrologia-marciana/CLASE.md)
7. **Depósitos sedimentarios** — [`B66-C05`](../programa/clases/B66/B66-C05-depositos-sedimentarios-y-sedimentologia-planetaria/CLASE.md)
8. **Tectónica superficial** — [`B53-C12`](../programa/clases/B53/B53-C12-tectonica-planetaria/CLASE.md)
9. **Estadística de formas geológicas** — [`B53-C08`](../programa/clases/B53/B53-C08-cartografia-de-crateres/CLASE.md), [`B12-C03`](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md)
10. **Interpretación geomorfológica** — [`B53-C09`](../programa/clases/B53/B53-C09-estratigrafia-planetaria/CLASE.md), [`B53-C18`](../programa/clases/B53/B53-C18-cartografia-geologica-digital/CLASE.md)

✅ **Checkpoint R05-M03.** Sin mirar el material, explica cómo se relacionan «Morfología de cráteres», «Sistemas fluviales fósiles» y «Interpretación geomorfológica», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R05-M04 · Geología de impactos

1. **Física del impacto** — [`B53-C10`](../programa/clases/B53/B53-C10-geologia-de-impacto/CLASE.md), [`B58-C15`](../programa/clases/B58/B58-C15-modelos-de-impacto-planetario/CLASE.md)
2. **Dinámica de eyección** — [`B61-C01`](../programa/clases/B61/B61-C01-dinamica-de-eyeccion-y-escalado-de-crateres/CLASE.md)
3. **Cráteres simples** — [`B61-C02`](../programa/clases/B61/B61-C02-crateres-simples-morfologia-y-formacion/CLASE.md)
4. **Cráteres complejos** — [`B61-C03`](../programa/clases/B61/B61-C03-crateres-complejos-colapso-picos-centrales-y-terrazas/CLASE.md)
5. **Mantos de ejecta** — [`B61-C04`](../programa/clases/B61/B61-C04-mantos-de-ejecta-y-depositos-de-impacto/CLASE.md)
6. **Fusión por impacto** — [`B61-C05`](../programa/clases/B61/B61-C05-fusion-por-impacto-y-metamorfismo-de-choque/CLASE.md)
7. **Datación por conteo de cráteres** — [`B61-C06`](../programa/clases/B61/B61-C06-datacion-por-conteo-de-crateres-funciones-de-produccion-y-edades-de-modelo/CLASE.md)
8. **Cuencas multianillo** — [`B61-C07`](../programa/clases/B61/B61-C07-cuencas-multianillo-y-grandes-impactos/CLASE.md)
9. **Meteorización espacial** — [`B53-C22`](../programa/clases/B53/B53-C22-meteorizacion-espacial-micrometeoritos-viento-solar-y-maduracion-del-regolito/CLASE.md)
10. **Cartografía de terreno de impacto** — [`B53-C08`](../programa/clases/B53/B53-C08-cartografia-de-crateres/CLASE.md), [`B53-C18`](../programa/clases/B53/B53-C18-cartografia-geologica-digital/CLASE.md), [`B53-C10`](../programa/clases/B53/B53-C10-geologia-de-impacto/CLASE.md)

✅ **Checkpoint R05-M04.** Sin mirar el material, explica cómo se relacionan «Física del impacto», «Fusión por impacto» y «Cartografía de terreno de impacto», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R05-M05 · Vulcanismo planetario

1. **Magma y diferenciación** — [`B52-C18`](../programa/clases/B52/B52-C18-diferenciacion-planetaria/CLASE.md), [`B53-C11`](../programa/clases/B53/B53-C11-vulcanismo-extraterrestre/CLASE.md)
2. **Volcanismo basáltico** — [`B70-C01`](../programa/clases/B70/B70-C01-volcanismo-basaltico-escudos-fisuras-y-llanuras-planetarias/CLASE.md)
3. **Domos volcánicos** — [`B70-C02`](../programa/clases/B70/B70-C02-domos-volcanicos-y-vulcanismo-evolucionado/CLASE.md)
4. **Calderas planetarias** — [`B70-C03`](../programa/clases/B70/B70-C03-calderas-planetarias-formacion-y-colapso/CLASE.md)
5. **Vulcanismo marciano** — [`B70-C04`](../programa/clases/B70/B70-C04-vulcanismo-marciano-provincias-edades-y-evolucion/CLASE.md)
6. **Actividad volcánica venusina** — [`B70-C05`](../programa/clases/B70/B70-C05-actividad-volcanica-venusina-llanuras-coronas-e-indicios-de-actividad-reciente/CLASE.md)
7. **Criovulcanismo** — [`B70-C06`](../programa/clases/B70/B70-C06-criovulcanismo-lavas-heladas-y-emision-de-volatiles/CLASE.md)
8. **Flujos y depósitos** — [`B70-C07`](../programa/clases/B70/B70-C07-flujos-de-lava-y-depositos-piroclasticos/CLASE.md)
9. **Teledetección térmica volcánica** — [`B57-C18`](../programa/clases/B57/B57-C18-volcanismo-y-monitoreo/CLASE.md), [`B57-C01`](../programa/clases/B57/B57-C01-fundamentos-de-teledeteccion/CLASE.md)
10. **Reconstrucción de historia eruptiva** — [`B53-C09`](../programa/clases/B53/B53-C09-estratigrafia-planetaria/CLASE.md), [`B53-C11`](../programa/clases/B53/B53-C11-vulcanismo-extraterrestre/CLASE.md)

✅ **Checkpoint R05-M05.** Sin mirar el material, explica cómo se relacionan «Magma y diferenciación», «Actividad volcánica venusina» y «Reconstrucción de historia eruptiva», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R05-M06 · Criósferas y mundos helados

1. **Hielos de agua y otros volátiles** — [`B55-C06`](../programa/clases/B55/B55-C06-hielos-astrofisicos/CLASE.md), [`B06-C19`](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md), [`B53-C13`](../programa/clases/B53/B53-C13-geomorfologia-de-hielos/CLASE.md)
2. **Mecánica de hielo** — [`B53-C23`](../programa/clases/B53/B53-C23-mecanica-de-hielo-reologia-fracturas-y-deformacion/CLASE.md)
3. **Fracturas de corteza helada** — [`B53-C14`](../programa/clases/B53/B53-C14-geologia-de-europa/CLASE.md), [`B53-C12`](../programa/clases/B53/B53-C12-tectonica-planetaria/CLASE.md)
4. **Océanos subsuperficiales** — [`B55-C15`](../programa/clases/B55/B55-C15-quimica-de-oceanos-internos/CLASE.md), [`B56-C09`](../programa/clases/B56/B56-C09-oceanos-de-europa/CLASE.md), [`B56-C10`](../programa/clases/B56/B56-C10-oceanos-de-encelado/CLASE.md)
5. **Mareas y calentamiento** — [`B65-C06`](../programa/clases/B65/B65-C06-calentamiento-por-marea-y-equilibrio-termico-en-satelites/CLASE.md)
6. **Plumas de Encélado** — [`B53-C15`](../programa/clases/B53/B53-C15-geologia-de-encelado/CLASE.md), [`B56-C10`](../programa/clases/B56/B56-C10-oceanos-de-encelado/CLASE.md)
7. **Geología de Europa** — [`B53-C14`](../programa/clases/B53/B53-C14-geologia-de-europa/CLASE.md)
8. **Terrenos poligonales** — [`B53-C13`](../programa/clases/B53/B53-C13-geomorfologia-de-hielos/CLASE.md)
9. **Radar de penetración de hielo** — [`B53-C24`](../programa/clases/B53/B53-C24-sondeo-radar-de-penetracion-de-hielo/CLASE.md)
10. **Inferencias de habitabilidad** — [`B56-C09`](../programa/clases/B56/B56-C09-oceanos-de-europa/CLASE.md), [`B56-C10`](../programa/clases/B56/B56-C10-oceanos-de-encelado/CLASE.md), [`B56-C06`](../programa/clases/B56/B56-C06-agua-liquida-y-solventes-alternativos/CLASE.md)

✅ **Checkpoint R05-M06.** Sin mirar el material, explica cómo se relacionan «Hielos de agua y otros volátiles», «Plumas de Encélado» y «Inferencias de habitabilidad», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R05-M07 · Cartografía y estratigrafía planetaria

1. **Cartografía orbital** — [`B53-C08`](../programa/clases/B53/B53-C08-cartografia-de-crateres/CLASE.md), [`B53-C18`](../programa/clases/B53/B53-C18-cartografia-geologica-digital/CLASE.md)
2. **Modelos digitales de elevación** — [`B53-C07`](../programa/clases/B53/B53-C07-topografia-por-altimetria/CLASE.md), [`B53-C18`](../programa/clases/B53/B53-C18-cartografia-geologica-digital/CLASE.md)
3. **Estratigrafía relativa** — [`B53-C09`](../programa/clases/B53/B53-C09-estratigrafia-planetaria/CLASE.md)
4. **Unidades geológicas** — [`B53-C09`](../programa/clases/B53/B53-C09-estratigrafia-planetaria/CLASE.md), [`B53-C18`](../programa/clases/B53/B53-C18-cartografia-geologica-digital/CLASE.md)
5. **Análisis de lineamientos** — [`B53-C12`](../programa/clases/B53/B53-C12-tectonica-planetaria/CLASE.md), [`B53-C18`](../programa/clases/B53/B53-C18-cartografia-geologica-digital/CLASE.md)
6. **Composición mineral multiespectral** — [`B53-C17`](../programa/clases/B53/B53-C17-mineralogia-espectral/CLASE.md), [`B57-C05`](../programa/clases/B57/B57-C05-imagenes-multiespectrales/CLASE.md)
7. **Sistemas GIS** — [`B53-C18`](../programa/clases/B53/B53-C18-cartografia-geologica-digital/CLASE.md), [`B57-C19`](../programa/clases/B57/B57-C19-sig-y-analisis-de-riesgo/CLASE.md), [`B53-C20`](../programa/clases/B53/B53-C20-proyecto-sig-de-terreno-extraterrestre/CLASE.md)
8. **Corrección geométrica** — [`B53-C25`](../programa/clases/B53/B53-C25-correccion-geometrica-y-ortorrectificacion-de-imagenes-planetarias/CLASE.md)
9. **Mapas con incertidumbre** — [`B53-C19`](../programa/clases/B53/B53-C19-incertidumbre-en-mapas-planetarios/CLASE.md)
10. **Publicación de mapas geológicos** — [`B53-C26`](../programa/clases/B53/B53-C26-publicacion-de-mapas-geologicos-planetarios-estandares-y-leyendas/CLASE.md)

✅ **Checkpoint R05-M07.** Sin mirar el material, explica cómo se relacionan «Cartografía orbital», «Composición mineral multiespectral» y «Publicación de mapas geológicos», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R05-M08 · Muestras y resultados de misiones planetarias

1. **Instrumentos de sondas planetarias** — [`B63-C01`](../programa/clases/B63/B63-C01-instrumentacion-de-sondas-y-rovers-planetarios/CLASE.md)
2. **Muestreo superficial** — [`B63-C02`](../programa/clases/B63/B63-C02-muestreo-superficial-y-estrategias-de-recoleccion/CLASE.md)
3. **Espectrómetros de rover** — [`B45-C14`](../programa/clases/B45/B45-C14-composicion-quimica-por-espectros/CLASE.md), [`B47-C08`](../programa/clases/B47/B47-C08-espectrometros-de-masas-orbitales/CLASE.md), [`B55-C10`](../programa/clases/B55/B55-C10-identificacion-de-moleculas-organicas/CLASE.md)
4. **Análisis de meteoritos** — [`B55-C12`](../programa/clases/B55/B55-C12-geoquimica-de-meteoritos/CLASE.md), [`B06-C20`](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md)
5. **Cadenas de custodia** — [`B63-C03`](../programa/clases/B63/B63-C03-curaduria-y-cadena-de-custodia-de-muestras/CLASE.md)
6. **Contaminación de muestras** — [`B55-C18`](../programa/clases/B55/B55-C18-contaminacion-de-muestras/CLASE.md), [`B56-C17`](../programa/clases/B56/B56-C17-control-de-contaminacion-biologica/CLASE.md)
7. **Control de calidad de laboratorio** — [`B13-C14`](../programa/clases/B13/B13-C14-repetibilidad-y-reproducibilidad/CLASE.md), [`B13-C18`](../programa/clases/B13/B13-C18-intercomparacion-de-instrumentos/CLASE.md), [`B13-C20`](../programa/clases/B13/B13-C20-validacion-de-una-cadena-de-medida/CLASE.md)
8. **Datos PDS** — [`B14-C21`](../programa/clases/B14/B14-C21-datos-de-misiones-planetarias-pds4-etiquetas-y-spice/CLASE.md)
9. **Integración de mediciones** — [`B55-C19`](../programa/clases/B55/B55-C19-interpretacion-de-firmas-quimicas/CLASE.md), [`B12-C16`](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md), [`B13-C18`](../programa/clases/B13/B13-C18-intercomparacion-de-instrumentos/CLASE.md)
10. **Redacción de reporte de misión** — [`B124-C19`](../programa/clases/B124/B124-C19-redaccion-de-propuesta-de-mision/CLASE.md), [`B12-C20`](../programa/clases/B12/B12-C20-informe-de-incertidumbre-de-una-mision/CLASE.md)

✅ **Checkpoint R05-M08.** Sin mirar el material, explica cómo se relacionan «Instrumentos de sondas planetarias», «Contaminación de muestras» y «Redacción de reporte de misión», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

**🎯 Proyecto final · Mapa geológico de un sitio de aterrizaje.** Con imágenes y topografía públicas de un cuerpo, produce un mapa geomorfológico y estratigráfico de un sitio candidato y propone una historia geológica con edades relativas.

Entregables:

- Mapa con leyenda y unidades definidas
- Perfil estratigráfico con el orden de eventos
- Conteo de cráteres con el método y su incertidumbre
- Propuesta de tres hipótesis a contrastar con una misión

Criterios de evaluación:

- Las unidades se definen con criterios observables
- Las edades relativas son coherentes con los contactos
- Se citan los datos y sus resoluciones
- Las hipótesis son falsables

**🏁 Criterio de salida.** Has terminado la ruta cuando:

- Puedes cartografiar y datar unidades de un cuerpo planetario con datos públicos.
- Puedes explicar procesos de impacto, vulcanismo y mundos helados con evidencia.
- Puedes reconocer qué puede y qué no puede decir una muestra.

<!-- /recorrido -->

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
2. Estudia **astrogeología y geodesia planetaria** ([**B53** · Astrogeología y geodesia planetaria](../programa/tronco-comun/B53-astrogeologia-y-geodesia-planetaria.md)) y **atmósferas** ([**B54** · Atmósferas y climatología planetaria](../programa/tronco-comun/B54-atmosferas-y-climatologia-planetaria.md)).
3. Profundiza en **geomorfología** ([**B66** · Geomorfología y procesos superficiales planetarios](../programa/tronco-comun/B66-geomorfologia-y-procesos-superficiales-planetarios.md)), **impactos** ([**B61** · Cráteres de impacto y geología de impactos](../programa/tronco-comun/B61-crateres-de-impacto-y-geologia-de-impactos.md)) y **vulcanismo** ([**B70** · Vulcanismo planetario](../programa/tronco-comun/B70-vulcanismo-planetario.md)).
4. Aprende **geofísica de interiores** ([**B65** · Geofísica de interiores planetarios](../programa/tronco-comun/B65-geofisica-de-interiores-planetarios.md)) y el análisis de **muestras** ([**B63** · Exploración in situ y análisis de muestras planetarias](../programa/tronco-comun/B63-exploracion-in-situ-y-analisis-de-muestras-planetarias.md)).
5. Reúne tu **análisis con datos abiertos** y su historial.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Astroquímica y astrobiología](astroquimica-y-astrobiologia.md) · [Observación terrestre y geointeligencia científica](observacion-terrestre-y-geointeligencia-cientifica.md) · [Recursos extraterrestres y economía industrial espacial](recursos-extraterrestres-y-economia-industrial-espacial.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R05-ciencias-planetarias-y-astrogeologia/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
