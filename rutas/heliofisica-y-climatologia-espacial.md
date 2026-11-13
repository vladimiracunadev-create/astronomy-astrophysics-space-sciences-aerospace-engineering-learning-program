# ☀️ Heliofísica y climatología espacial

> Estudias el Sol y su influencia sobre el entorno espacial: plasma, campo magnético, erupciones y su efecto en satélites, comunicaciones y tripulaciones.
>
> **Nivel de entrada:** física y matemática de nivel universitario, más programación; rol de investigación y de servicio operativo · **Foco:** física del plasma y MHD, corona y erupciones, viento solar, magnetosfera, pronóstico y riesgo del clima espacial · **Entrega:** un análisis o un modelo de un fenómeno solar o geoespacial, con datos, supuestos e incertidumbre explícitos

## 🧭 Qué es y por qué importa

La heliofísica trata al Sol y al espacio que domina como un solo sistema: la estrella, el viento solar que emite, la magnetosfera que lo recibe y las perturbaciones que viajan entre ambos. El **clima espacial** es su cara aplicada: lo que esas perturbaciones hacen a satélites, enlaces de radio, navegación, redes eléctricas y tripulaciones.

El material con que se trabaja es plasma, es decir, gas ionizado que obedece a la vez a la dinámica de fluidos y al electromagnetismo. De ahí que el rol exija magnetohidrodinámica y métodos numéricos, además de datos de instrumentos en órbita y en tierra.

Las miradas del rol son:

- **Física del Sol.** Corona, erupciones y eyecciones de masa. Su pregunta es: *¿qué configuración magnética libera esta energía y cuándo?*
- **Propagación y acople.** Viento solar, choques y magnetosfera. Su pregunta es: *¿qué llegará a la Tierra, cuándo y con qué intensidad?*
- **Impacto y riesgo.** Efectos en sistemas tecnológicos. Su pregunta es: *¿qué sistema se ve afectado y cómo se comunica el riesgo?*

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es astrofísica estelar general.** El Sol se estudia con resolución que ninguna otra estrella permite y con foco en su efecto sobre el entorno ([Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md)).
- **No es meteorología terrestre.** Comparte la idea de pronóstico, pero la física y los datos son otros.
- **No es ingeniería de satélites.** Tú caracterizas la amenaza; quien diseña el satélite decide cómo protegerlo ([Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md)).
- **No es un pronóstico infalible.** El pronóstico de erupciones y de su llegada tiene incertidumbre que hay que comunicar.

## 🗓️ Un día en el puesto

- **Datos:** revisas observaciones solares y mediciones in situ, y verificas calibración y marcos de tiempo.
- **Análisis de un evento:** reconstruyes la secuencia de una erupción y su propagación.
- **Modelo:** corres una simulación numérica y comparas con lo observado.
- **Evaluación de riesgo:** traduces un resultado a su efecto probable sobre un sistema concreto.
- **Comunicación:** redactas un aviso o un informe que distinga lo observado de lo pronosticado.

Dicho sin adornos: **la incertidumbre del pronóstico** es parte del producto, no un defecto de él.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Heliofísica y física de plasmas** ([**B30** · Heliofísica y física de plasmas](../programa/tronco-comun/B30-heliofisica-y-fisica-de-plasmas.md)); **plasmas y MHD avanzada** ([**B35** · Física avanzada de plasmas y MHD espacial](../programa/tronco-comun/B35-fisica-avanzada-de-plasmas-y-mhd-espacial.md)).
- **Corona solar y erupciones** ([**B34** · Corona solar y erupciones: diagnóstico y modelos](../programa/tronco-comun/B34-corona-solar-y-erupciones-diagnostico-y-modelos.md)); **clima espacial: impactos, pronóstico y riesgo** ([**B33** · Clima espacial: impactos, pronóstico y riesgo](../programa/tronco-comun/B33-clima-espacial-impactos-pronostico-y-riesgo.md)).
- **Ecuaciones diferenciales y métodos numéricos** ([**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md), [**B21** · Métodos numéricos para EDP y fluidos computacionales](../programa/tronco-comun/B21-metodos-numericos-para-edp-y-fluidos-computacionales.md)).
- **Estadística e incertidumbre** ([**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md)); **señales e imágenes** ([**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md)).
- **Instrumentación espacial** ([**B47** · Instrumentación y observatorios espaciales](../programa/tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md)) y **entorno térmico y de radiación** ([**B85** · Gestión térmica y entorno espacial](../programa/tronco-comun/B85-gestion-termica-y-entorno-espacial.md)).
- **Computación científica reproducible** ([**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md)).

### Herramientas del oficio

```text
Datos:                archivos públicos de observatorios y de misiones solares y geoespaciales
Análisis:             Python científico, series de tiempo e imágenes
Modelos:              códigos MHD y modelos empíricos del entorno
Cómputo:              clústeres o servicios de cómputo para simulaciones
Documentación:        registros de versión de datos, modelo y parámetros
```

Un modelo corrido con parámetros no registrados no se puede repetir ni criticar. Anota versión, entradas y condiciones de cada corrida.

### Habilidades no técnicas

- **Comunicación de incertidumbre** a públicos técnicos y no técnicos.
- **Trabajo bajo plazo** cuando un evento está en curso.
- **Rigor con series de datos largas.**
- **Colaboración con operadores de satélites y de redes.**

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md) — A02 · 20 clases
2. 📚 [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) — A02 · 20 clases
3. 📚 [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) — A02 · 26 clases
4. 📚 [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) — A02 · 20 clases

### 🎯 El núcleo del rol

**A02 · Matemática, física computacional y métodos científicos**

1. 📚 [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) — usa 3 de 26 clases: `B12-` C16–C17, C24
2. 📚 [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) — usa 1 de 23 clases: `B13-` C05
3. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — usa 4 de 31 clases: `B14-` C09, C12, C20, C22
4. 📚 [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) — usa 3 de 24 clases: `B15-` C01, C17, C21
5. 📚 [**B21** · Métodos numéricos para EDP y fluidos computacionales](../programa/tronco-comun/B21-metodos-numericos-para-edp-y-fluidos-computacionales.md) — usa 1 de 5 clases: `B21-` C01

**A03 · Astrofísica y ciencias fundamentales del universo**

6. 📚 [**B30** · Heliofísica y física de plasmas](../programa/tronco-comun/B30-heliofisica-y-fisica-de-plasmas.md) — usa 18 de 23 clases: `B30-` C02, C05–C18, C20, C22–C23
7. 📚 [**B31** · Física cuántica, nuclear y astropartículas](../programa/tronco-comun/B31-fisica-cuantica-nuclear-y-astroparticulas.md) — usa 1 de 20 clases: `B31-` C14
8. 📚 [**B33** · Clima espacial: impactos, pronóstico y riesgo](../programa/tronco-comun/B33-clima-espacial-impactos-pronostico-y-riesgo.md) — usa 14 de 14 clases: `B33-` C01–C14
9. 📚 [**B34** · Corona solar y erupciones: diagnóstico y modelos](../programa/tronco-comun/B34-corona-solar-y-erupciones-diagnostico-y-modelos.md) — usa 9 de 9 clases: `B34-` C01–C09
10. 📚 [**B35** · Física avanzada de plasmas y MHD espacial](../programa/tronco-comun/B35-fisica-avanzada-de-plasmas-y-mhd-espacial.md) — usa 10 de 10 clases: `B35-` C01–C10

**A04 · Óptica, telescopios y observatorios científicos**

11. 📚 [**B45** · Espectroscopía, fotometría y polarimetría](../programa/tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md) — usa 3 de 24 clases: `B45-` C10–C12
12. 📚 [**B47** · Instrumentación y observatorios espaciales](../programa/tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md) — usa 6 de 25 clases: `B47-` C07, C09, C21–C24

**A06 · Mecánica orbital, navegación y vuelo espacial**

13. 📚 [**B72** · Perturbaciones y evolución de órbitas](../programa/tronco-comun/B72-perturbaciones-y-evolucion-de-orbitas.md) — usa 2 de 21 clases: `B72-` C06–C07
14. 📚 [**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md) — usa 1 de 30 clases: `B74-` C08

**A07 · Ingeniería y construcción de sistemas espaciales**

15. 📚 [**B85** · Gestión térmica y entorno espacial](../programa/tronco-comun/B85-gestion-termica-y-entorno-espacial.md) — usa 3 de 29 clases: `B85-` C15, C21–C22
16. 📚 [**B89** · Comunicaciones y navegación satelital](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) — usa 2 de 25 clases: `B89-` C21–C22

**A09 · Astronáutica humana, medicina y hábitats**

17. 📚 [**B105** · Medicina y biología espacial](../programa/tronco-comun/B105-medicina-y-biologia-espacial.md) — usa 2 de 27 clases: `B105-` C06–C07

**A10 · Entorno orbital, derecho y seguridad espacial**

18. 📚 [**B119** · Derecho, seguridad y geopolítica espacial](../programa/tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md) — usa 1 de 36 clases: `B119-` C16

<!-- /ruta -->

<!-- recorrido:inicio -->
### 🗺️ Recorrido módulo por módulo

El rol se estudia en **8 módulos** de 10 temas cada uno (cada tema es un par «concepto + aplicación»). Haz el diagnóstico, avanza por los módulos **en orden** y cierra cada uno con su checkpoint; al final, el proyecto y el criterio de salida.

**🩺 Diagnóstico de entrada.** Si respondes «no sé» a dos o más, empieza por los fundamentos de arriba:

- ¿Puedes calcular la trayectoria de una carga en un campo magnético uniforme?
- ¿Sabes qué es un plasma y por qué es buen conductor?
- ¿Manejas series temporales y su filtrado?
- ¿Sabes qué son el viento solar y la magnetosfera?

#### R07-M01 · Plasmas avanzados

1. **Distribuciones de velocidades** — [`B35-C01`](../programa/clases/B35/B35-C01-funciones-de-distribucion-de-velocidades-en-plasmas/CLASE.md)
2. **Debye shielding** — [`B30-C07`](../programa/clases/B30/B30-C07-longitud-de-debye-y-plasma/CLASE.md)
3. **Frecuencia de plasma** — [`B30-C08`](../programa/clases/B30/B30-C08-frecuencias-y-ondas-de-plasma/CLASE.md)
4. **Radio de Larmor** — [`B30-C06`](../programa/clases/B30/B30-C06-particulas-cargadas-y-movimientos/CLASE.md)
5. **Ondas de Alfvén** — [`B35-C02`](../programa/clases/B35/B35-C02-ondas-de-alfven-y-ondas-magnetosonicas/CLASE.md)
6. **Ondas electrostáticas** — [`B30-C08`](../programa/clases/B30/B30-C08-frecuencias-y-ondas-de-plasma/CLASE.md)
7. **Inestabilidades de plasma** — [`B35-C03`](../programa/clases/B35/B35-C03-inestabilidades-de-plasma-cineticas-y-de-fluido/CLASE.md)
8. **Colisiones y régimen cinético** — [`B35-C04`](../programa/clases/B35/B35-C04-colisiones-regimen-cinetico-y-ecuacion-de-vlasov/CLASE.md)
9. **Simulación de partículas** — [`B35-C05`](../programa/clases/B35/B35-C05-simulacion-de-plasmas-por-particulas-pic/CLASE.md)
10. **Observaciones in situ** — [`B35-C06`](../programa/clases/B35/B35-C06-mediciones-in-situ-de-plasmas-espaciales/CLASE.md)

✅ **Checkpoint R07-M01.** Sin mirar el material, explica cómo se relacionan «Distribuciones de velocidades», «Ondas electrostáticas» y «Observaciones in situ», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R07-M02 · Magnetohidrodinámica aplicada

1. **Ecuaciones MHD** — [`B30-C09`](../programa/clases/B30/B30-C09-magnetohidrodinamica/CLASE.md)
2. **Conservación magnética** — [`B35-C07`](../programa/clases/B35/B35-C07-congelamiento-del-flujo-magnetico-y-conservacion-en-mhd-ideal/CLASE.md)
3. **Flujos de plasma** — [`B35-C08`](../programa/clases/B35/B35-C08-flujos-de-plasma-estacionarios-y-balance-de-presiones/CLASE.md)
4. **Choques magnetohidrodinámicos** — [`B30-C14`](../programa/clases/B30/B30-C14-choques-y-aceleracion-de-particulas/CLASE.md)
5. **Re conexión magnética** — [`B30-C11`](../programa/clases/B30/B30-C11-reconexion-magnetica/CLASE.md)
6. **Turbulencia MHD** — [`B35-C09`](../programa/clases/B35/B35-C09-turbulencia-en-plasmas-y-mhd/CLASE.md)
7. **Condiciones de frontera** — [`B35-C10`](../programa/clases/B35/B35-C10-condiciones-de-frontera-en-modelos-mhd/CLASE.md)
8. **Modelos de viento solar** — [`B30-C10`](../programa/clases/B30/B30-C10-viento-solar-y-heliosfera/CLASE.md)
9. **Métodos numéricos MHD** — [`B21-C01`](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md)
10. **Validación con eventos solares** — [`B33-C01`](../programa/clases/B33/B33-C01-validacion-de-modelos-mhd-con-eventos-solares-documentados/CLASE.md)

✅ **Checkpoint R07-M02.** Sin mirar el material, explica cómo se relacionan «Ecuaciones MHD», «Turbulencia MHD» y «Validación con eventos solares», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R07-M03 · Física de corona solar

1. **Estructura coronal** — [`B30-C02`](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md)
2. **Campos coronales** — [`B30-C05`](../programa/clases/B30/B30-C05-campos-magneticos-solares/CLASE.md)
3. **Calentamiento coronal** — [`B34-C01`](../programa/clases/B34/B34-C01-calentamiento-coronal-mecanismos-y-evidencias/CLASE.md)
4. **Emisión EUV** — [`B34-C02`](../programa/clases/B34/B34-C02-emision-euv-y-rayos-x-de-la-corona/CLASE.md)
5. **Bucles magnéticos** — [`B34-C03`](../programa/clases/B34/B34-C03-bucles-magneticos-coronales/CLASE.md)
6. **Ondas coronales** — [`B34-C04`](../programa/clases/B34/B34-C04-ondas-y-oscilaciones-coronales-como-sismologia-solar/CLASE.md)
7. **Densidad electrónica** — [`B34-C05`](../programa/clases/B34/B34-C05-diagnostico-de-densidad-electronica-coronal/CLASE.md)
8. **Espectros solares** — [`B45-C10`](../programa/clases/B45/B45-C10-lineas-de-emision/CLASE.md), [`B45-C11`](../programa/clases/B45/B45-C11-lineas-de-absorcion/CLASE.md), [`B45-C12`](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md)
9. **Tomografía coronal** — [`B34-C06`](../programa/clases/B34/B34-C06-tomografia-coronal/CLASE.md)
10. **Comparación con observaciones** — [`B34-C07`](../programa/clases/B34/B34-C07-comparacion-de-modelos-coronales-con-observaciones/CLASE.md)

✅ **Checkpoint R07-M03.** Sin mirar el material, explica cómo se relacionan «Estructura coronal», «Ondas coronales» y «Comparación con observaciones», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R07-M04 · Erupciones solares

1. **Fulguraciones solares** — [`B30-C12`](../programa/clases/B30/B30-C12-erupciones-y-fulguraciones-solares/CLASE.md)
2. **Eyecciones de masa coronal** — [`B30-C13`](../programa/clases/B30/B30-C13-eyecciones-de-masa-coronal/CLASE.md)
3. **Erupciones de filamentos** — [`B34-C08`](../programa/clases/B34/B34-C08-erupciones-de-filamentos-y-prominencias/CLASE.md)
4. **Aceleración de partículas** — [`B30-C14`](../programa/clases/B30/B30-C14-choques-y-aceleracion-de-particulas/CLASE.md)
5. **Campos y reconexión** — [`B30-C11`](../programa/clases/B30/B30-C11-reconexion-magnetica/CLASE.md)
6. **Modelos de propagación CME** — [`B33-C02`](../programa/clases/B33/B33-C02-modelos-de-propagacion-de-cme/CLASE.md)
7. **Choques interplanetarios** — [`B30-C14`](../programa/clases/B30/B30-C14-choques-y-aceleracion-de-particulas/CLASE.md)
8. **Eventos extremos históricos** — [`B33-C03`](../programa/clases/B33/B33-C03-eventos-extremos-historicos-de-clima-espacial/CLASE.md)
9. **Medición de severidad** — [`B33-C04`](../programa/clases/B33/B33-C04-escalas-de-severidad-de-clima-espacial/CLASE.md)
10. **Comunicación de riesgo solar** — [`B33-C05`](../programa/clases/B33/B33-C05-comunicacion-de-riesgo-y-alertas-de-clima-espacial/CLASE.md)

✅ **Checkpoint R07-M04.** Sin mirar el material, explica cómo se relacionan «Fulguraciones solares», «Modelos de propagación CME» y «Comunicación de riesgo solar», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R07-M05 · Magnetosferas y radiación

1. **Magnetopausa** — [`B30-C15`](../programa/clases/B30/B30-C15-magnetosfera-terrestre/CLASE.md)
2. **Cola magnética** — [`B30-C15`](../programa/clases/B30/B30-C15-magnetosfera-terrestre/CLASE.md)
3. **Anillos de corriente** — [`B30-C22`](../programa/clases/B30/B30-C22-anillo-de-corriente-y-corrientes-magnetosfericas/CLASE.md)
4. **Cinturones de radiación** — [`B30-C16`](../programa/clases/B30/B30-C16-cinturones-de-van-allen/CLASE.md)
5. **Tormentas geomagnéticas** — [`B30-C18`](../programa/clases/B30/B30-C18-tormentas-geomagneticas/CLASE.md)
6. **Corrientes ionosféricas** — [`B30-C17`](../programa/clases/B30/B30-C17-auroras-y-corrientes-ionosfericas/CLASE.md)
7. **Precipitación auroral** — [`B30-C17`](../programa/clases/B30/B30-C17-auroras-y-corrientes-ionosfericas/CLASE.md)
8. **Índices Kp y Dst** — [`B30-C23`](../programa/clases/B30/B30-C23-indices-geomagneticos-kp-y-dst/CLASE.md)
9. **Efectos de partículas energéticas** — [`B85-C21`](../programa/clases/B85/B85-C21-efectos-de-particulas-energeticas-en-electronica-y-materiales/CLASE.md)
10. **Modelos de exposición** — [`B85-C22`](../programa/clases/B85/B85-C22-modelos-de-exposicion-a-radiacion-en-orbita/CLASE.md)

✅ **Checkpoint R07-M05.** Sin mirar el material, explica cómo se relacionan «Magnetopausa», «Corrientes ionosféricas» y «Modelos de exposición», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R07-M06 · Observatorios heliofísicos

1. **Imágenes coronográficas** — [`B47-C07`](../programa/clases/B47/B47-C07-coronografos-espaciales/CLASE.md)
2. **Magnetogramas** — [`B47-C21`](../programa/clases/B47/B47-C21-magnetografos-y-medicion-de-campos-solares/CLASE.md)
3. **Satélites de física solar** — [`B47-C22`](../programa/clases/B47/B47-C22-misiones-de-fisica-solar-soho-sdo-y-solar-orbiter/CLASE.md)
4. **Sondas heliosféricas** — [`B47-C23`](../programa/clases/B47/B47-C23-sondas-heliosfericas-parker-solar-probe-y-voyager/CLASE.md)
5. **Detectores de partículas** — [`B47-C09`](../programa/clases/B47/B47-C09-detectores-de-particulas-instrumentacion-y-observatorios-espaciales/CLASE.md), [`B31-C14`](../programa/clases/B31/B31-C14-detectores-de-particulas/CLASE.md)
6. **Instrumentos de plasma** — [`B47-C24`](../programa/clases/B47/B47-C24-instrumentos-de-plasma-y-campos-in-situ/CLASE.md)
7. **Calibración de sensores** — [`B13-C05`](../programa/clases/B13/B13-C05-calibracion-instrumental/CLASE.md)
8. **Series de tiempo solares** — [`B15-C01`](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md)
9. **Acceso a datos abiertos** — [`B14-C22`](../programa/clases/B14/B14-C22-acceso-a-datos-heliofisicos-abiertos-con-sunpy/CLASE.md)
10. **Integración multiinstrumento** — [`B34-C09`](../programa/clases/B34/B34-C09-integracion-multiinstrumento-de-datos-heliofisicos/CLASE.md)

✅ **Checkpoint R07-M06.** Sin mirar el material, explica cómo se relacionan «Imágenes coronográficas», «Instrumentos de plasma» y «Integración multiinstrumento», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R07-M07 · Impactos tecnológicos del clima espacial

1. **Perturbaciones GNSS** — [`B89-C21`](../programa/clases/B89/B89-C21-efectos-ionosfericos-y-centelleo-en-senales-gnss/CLASE.md)
2. **Corrientes geomagnéticas inducidas** — [`B33-C06`](../programa/clases/B33/B33-C06-corrientes-geomagneticas-inducidas-gic/CLASE.md)
3. **Impactos en redes eléctricas** — [`B33-C07`](../programa/clases/B33/B33-C07-impactos-del-clima-espacial-en-redes-electricas/CLASE.md)
4. **Dosis en aviación** — [`B33-C08`](../programa/clases/B33/B33-C08-dosis-de-radiacion-en-aviacion/CLASE.md)
5. **Efectos en satélites** — [`B85-C15`](../programa/clases/B85/B85-C15-electrificacion-superficial/CLASE.md), [`B72-C06`](../programa/clases/B72/B72-C06-arrastre-atmosferico/CLASE.md), [`B72-C07`](../programa/clases/B72/B72-C07-modelos-de-densidad-atmosferica/CLASE.md)
6. **Comunicación HF** — [`B89-C22`](../programa/clases/B89/B89-C22-propagacion-ionosferica-y-comunicaciones-hf/CLASE.md)
7. **Radiación para tripulación** — [`B105-C06`](../programa/clases/B105/B105-C06-radiacion-ionizante-y-exposicion/CLASE.md), [`B105-C07`](../programa/clases/B105/B105-C07-dosimetria-personal/CLASE.md)
8. **Gestión de infraestructura crítica** — [`B119-C16`](../programa/clases/B119/B119-C16-proteccion-de-infraestructura-critica/CLASE.md)
9. **Planes de continuidad** — [`B33-C09`](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md)
10. **Análisis de episodio documentado** — [`B30-C20`](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md)

✅ **Checkpoint R07-M07.** Sin mirar el material, explica cómo se relacionan «Perturbaciones GNSS», «Comunicación HF» y «Análisis de episodio documentado», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R07-M08 · Modelos de pronóstico espacial

1. **Modelos de viento solar** — [`B33-C10`](../programa/clases/B33/B33-C10-modelos-de-viento-solar-para-pronostico-parker-y-wsa/CLASE.md)
2. **Modelos empíricos** — [`B33-C11`](../programa/clases/B33/B33-C11-modelos-empiricos-y-de-persistencia-en-clima-espacial/CLASE.md)
3. **Pronóstico de CME** — [`B33-C12`](../programa/clases/B33/B33-C12-pronostico-de-llegada-y-severidad-de-cme/CLASE.md)
4. **Pronóstico geomagnético** — [`B33-C13`](../programa/clases/B33/B33-C13-pronostico-de-actividad-geomagnetica/CLASE.md)
5. **Asimilación de observaciones** — [`B74-C08`](../programa/clases/B74/B74-C08-filtrado-recursivo-de-estados/CLASE.md), [`B15-C17`](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md)
6. **Series multivariadas** — [`B15-C21`](../programa/clases/B15/B15-C21-series-temporales-multivariadas-y-regresion-dinamica/CLASE.md)
7. **Incertidumbre pronóstica** — [`B12-C16`](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md), [`B12-C17`](../programa/clases/B12/B12-C17-analisis-de-sensibilidad/CLASE.md)
8. **Verificación de alertas** — [`B33-C14`](../programa/clases/B33/B33-C14-verificacion-de-alertas-con-tablas-de-contingencia/CLASE.md)
9. **Métricas skill score** — [`B12-C24`](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md)
10. **Panel de pronóstico reproducible** — [`B14-C09`](../programa/clases/B14/B14-C09-jupyter-y-experimentos-reproducibles/CLASE.md), [`B14-C12`](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md), [`B14-C20`](../programa/clases/B14/B14-C20-proyecto-reproducible-de-analisis-astronomico/CLASE.md)

✅ **Checkpoint R07-M08.** Sin mirar el material, explica cómo se relacionan «Modelos de viento solar», «Series multivariadas» y «Panel de pronóstico reproducible», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

**🎯 Proyecto final · Pronóstico de un evento de clima espacial.** Con datos públicos de una erupción y su tormenta geomagnética, construye un modelo de pronóstico simple y evalúa su acierto con métricas estándar.

Entregables:

- Cadena de datos y limpieza reproducible
- Modelo de tiempo de llegada y de intensidad
- Evaluación con métricas de acierto y falsas alarmas
- Nota técnica sobre el impacto en satélites y redes eléctricas

Criterios de evaluación:

- La evaluación usa datos no vistos por el modelo
- Se reportan aciertos y falsas alarmas, no solo el mejor caso
- Los impactos se asocian a mecanismos físicos
- El código y los datos están versionados

**🏁 Criterio de salida.** Has terminado la ruta cuando:

- Puedes explicar la física de la corona, las erupciones y la magnetosfera.
- Puedes construir y evaluar un pronóstico con métricas honestas.
- Puedes traducir un evento solar en riesgo para una infraestructura.

<!-- /recorrido -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es un **análisis de un evento o un modelo con datos abiertos**:

- un evento o una pregunta acotada y los datos de procedencia verificable;
- una reconstrucción o una simulación con sus supuestos;
- una comparación con la observación y una estimación del error;
- una nota de impacto sobre un sistema concreto;
- el código y los datos para repetirlo.

Los bloques de la ruta aportan ejercicios y laboratorios; guarda la primera versión y sus cambios.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional verificada, y para esta guía no se consultó una fuente externa específica (2026-11-05). Por eso no se citan normas, requisitos de acceso ni cifras: cuando se necesiten, deben consultarse en la fuente oficial vigente de la institución, agencia o empresa correspondiente.

## 📈 Progresión del rol

Rutas habituales: **grado en física o ingeniería → posgrado → investigación o servicio operativo de clima espacial → responsable de un modelo o de un servicio de alerta**. Se abren la modelación numérica y la gestión de riesgo de infraestructura. No se publican cifras salariales por no poder verificarlas.

Roles vecinos con los que se comparte formación: [Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md), [Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md) y [Telecomunicaciones y estaciones terrestres espaciales](telecomunicaciones-y-estaciones-terrestres-espaciales.md).

## ⚠️ Mitos y errores comunes

- **«Una erupción grande siempre causa daño grande».** Depende de la orientación del campo y de la geometría del evento.
- **«El clima espacial es un tema de ciencia ficción».** Afecta a sistemas reales; su magnitud en cada caso es lo que se estudia.
- **«Un modelo MHD predice con exactitud».** Aproxima, y su error hay que medirlo.
- **«Es solo observar el Sol».** Gran parte del trabajo es acople, propagación e impacto.
- **«Más resolución es mejor modelo».** Sin las condiciones correctas, solo es más cómputo.

## 🚀 Siguientes pasos

1. **Asienta la base** con el área A01 y la matemática de tu diagnóstico.
2. Estudia **heliofísica y plasmas** ([**B30** · Heliofísica y física de plasmas](../programa/tronco-comun/B30-heliofisica-y-fisica-de-plasmas.md)) y **ecuaciones diferenciales** ([**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md)).
3. Profundiza en **corona y erupciones** ([**B34** · Corona solar y erupciones: diagnóstico y modelos](../programa/tronco-comun/B34-corona-solar-y-erupciones-diagnostico-y-modelos.md)) y **MHD avanzada** ([**B35** · Física avanzada de plasmas y MHD espacial](../programa/tronco-comun/B35-fisica-avanzada-de-plasmas-y-mhd-espacial.md)).
4. Avanza a **clima espacial** ([**B33** · Clima espacial: impactos, pronóstico y riesgo](../programa/tronco-comun/B33-clima-espacial-impactos-pronostico-y-riesgo.md)) y a los **métodos numéricos** ([**B21** · Métodos numéricos para EDP y fluidos computacionales](../programa/tronco-comun/B21-metodos-numericos-para-edp-y-fluidos-computacionales.md)).
5. Reúne tu **análisis documentado** con su historial.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md) · [Seguridad defensa y resiliencia de infraestructuras espaciales](seguridad-defensa-y-resiliencia-de-infraestructuras-espaciales.md) · [Observación terrestre y geointeligencia científica](observacion-terrestre-y-geointeligencia-cientifica.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R07-heliofisica-y-climatologia-espacial/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
