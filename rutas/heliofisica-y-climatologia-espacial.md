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

- **Heliofísica y física de plasmas** ([**B30** · Heliofísica y física de plasmas](../programa/tronco-comun/B30-heliofisica-y-fisica-de-plasmas.md)); **plasmas y MHD avanzada** ([**B35** · Física avanzada de plasmas y MHD espacial](../../programa/tronco-comun/B35-fisica-avanzada-de-plasmas-y-mhd-espacial.md)).
- **Corona solar y erupciones** ([**B34** · Corona solar y erupciones: diagnóstico y modelos](../../programa/tronco-comun/B34-corona-solar-y-erupciones-diagnostico-y-modelos.md)); **clima espacial: impactos, pronóstico y riesgo** ([**B33** · Clima espacial: impactos, pronóstico y riesgo](../../programa/tronco-comun/B33-clima-espacial-impactos-pronostico-y-riesgo.md)).
- **Ecuaciones diferenciales y métodos numéricos** ([**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md), [**B21** · Métodos numéricos para EDP y fluidos computacionales](../../programa/tronco-comun/B21-metodos-numericos-para-edp-y-fluidos-computacionales.md)).
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
3. Profundiza en **corona y erupciones** ([**B34** · Corona solar y erupciones: diagnóstico y modelos](../../programa/tronco-comun/B34-corona-solar-y-erupciones-diagnostico-y-modelos.md)) y **MHD avanzada** ([**B35** · Física avanzada de plasmas y MHD espacial](../../programa/tronco-comun/B35-fisica-avanzada-de-plasmas-y-mhd-espacial.md)).
4. Avanza a **clima espacial** ([**B33** · Clima espacial: impactos, pronóstico y riesgo](../../programa/tronco-comun/B33-clima-espacial-impactos-pronostico-y-riesgo.md)) y a los **métodos numéricos** ([**B21** · Métodos numéricos para EDP y fluidos computacionales](../../programa/tronco-comun/B21-metodos-numericos-para-edp-y-fluidos-computacionales.md)).
5. Reúne tu **análisis documentado** con su historial.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Astrofísica estelar y galáctica](astrofisica-estelar-y-galactica.md) · [Seguridad defensa y resiliencia de infraestructuras espaciales](seguridad-defensa-y-resiliencia-de-infraestructuras-espaciales.md) · [Observación terrestre y geointeligencia científica](observacion-terrestre-y-geointeligencia-cientifica.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R07-heliofisica-y-climatologia-espacial/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
