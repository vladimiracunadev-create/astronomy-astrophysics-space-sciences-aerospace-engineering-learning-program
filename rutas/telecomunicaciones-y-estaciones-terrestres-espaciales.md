# 📶 Telecomunicaciones y estaciones terrestres espaciales

> Haces que una nave y el suelo se oigan: calculas si un enlace cierra, eliges antena, banda, modulación y codificación, y diseñas u operas la estación terrestre que recibe la telemetría y envía los telecomandos.
>
> **Nivel de entrada:** base sólida de física, señales, probabilidad y programación; sin ella el rol se queda en operar equipos · **Foco:** propagación, antenas, ruido, modulación y codificación, protocolos de enlace, tiempo y frecuencia, pases y operación de estación · **Entrega:** presupuestos de enlace con supuestos y márgenes, especificaciones de estación y de protocolos, planes de pases, registros de operación e informes de diagnóstico

## 🧭 Qué es y por qué importa

Un satélite que no se comunica es un objeto inerte. Todo lo que la misión produce llega a la Tierra por un enlace, y todo lo que le ordenas viaja por otro. La potencia de la señal cae con la distancia, el ruido de la antena y del receptor se suma, la atmósfera y la lluvia atenúan, y la geometría cambia en cada pase. El trabajo consiste en demostrar con números que, **aun en el peor caso razonable, llegan los datos con un margen**.

Su unidad de trabajo es el **enlace** y el **pase**: una ventana de tiempo en la que el satélite es visible, con un presupuesto que debe cerrar y un registro que demuestra qué ocurrió. El rol se reparte en tres miradas:

- **Diseño del enlace.** Calcula potencia, ganancia, pérdidas, ruido y relación señal/ruido; elige banda, modulación y codificación ([**B99** · Antenas y propagación para enlaces espaciales](../PROGRAMA_ACADEMICO_COMPLETO.md#b99--antenas-y-propagación-para-enlaces-espaciales), [**B102** · Modulación, codificación y protocolos de enlace](../PROGRAMA_ACADEMICO_COMPLETO.md#b102--modulación,-codificación-y-protocolos-de-enlace)). Su pregunta: *¿cierra el enlace con margen y cómo lo defiendo?*
- **Estación terrestre.** Antena, radio, apuntado, enrutado hacia el centro de datos y automatización de pases. Su pregunta: *¿la estación recibe y registra lo que debe, pase tras pase?*
- **Enlaces especiales.** Espacio profundo y comunicaciones ópticas, con mucho más ancho de banda pero con apuntamiento muy fino y dependencia de las nubes ([**B100** · Comunicaciones ópticas espaciales (profundización)](../PROGRAMA_ACADEMICO_COMPLETO.md#b100--comunicaciones-ópticas-espaciales-profundización)).

Muchas carreras empiezan operando pases y se abren hacia el diseño de enlaces o hacia redes de estaciones; este programa te hace recorrer las tres miradas.

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es el ingeniero de sistemas del satélite.** [Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md) reparte los recursos de todo el satélite; tú eres dueño del subsistema de comunicaciones y del lado terreno.
- **No es aviónica ni software de vuelo.** [Aviónica y software espacial de alta fiabilidad](avionica-y-software-espacial-de-alta-fiabilidad.md) genera el formato de telemetría; tú lo transportas y lo validas, no escribes el software de a bordo.
- **No es radioastronomía.** [Radioastronomía e interferometría](radioastronomia-e-interferometria.md) comparte antenas, ruido y receptores, pero su objetivo es medir el cielo; el tuyo es transportar datos de misión.
- **No es seguridad y defensa.** [Seguridad, defensa y resiliencia de infraestructuras espaciales](seguridad-defensa-y-resiliencia-de-infraestructuras-espaciales.md) diseña autenticación y cifrado de enlaces; tú los reconoces como requisito.
- **No es regulación del espectro.** Conoces el marco, pero el trámite de coordinación corresponde a quien tenga competencia regulatoria.
- **No es una habilitación para transmitir.** Transmitir exige licencia y coordinación; este programa no sustituye ese trámite.

## 🗓️ Un día en el puesto

Un día típico alterna dos mundos:

- **Diseño.** Cambia la potencia del transmisor o la antena; actualizas el presupuesto de enlace y defiendes el margen frente a lluvia, polarización o pérdidas de apuntado. Lo que no está en el presupuesto no existe.
- **Operación.** Revisas la lista de pases del día, preparas la estación (antena, radio, enrutado), recibes la telemetría, compruebas la calidad del enlace y registras anomalías.
- **Diagnóstico.** Un pase falla: ¿fue el apuntado, el ruido, una interferencia o un error de configuración? Reconstruyes el pase con los registros.
- **Procesamiento.** Convierte registros crudos en métricas (relación señal/ruido, tasa de error, Doppler) y comprueba que el formato de tramas se cumple.
- **Coordinación.** Con el centro de operaciones de misión, con el equipo de aviónica y con quien gestione licencias.

La habilidad no es dominar un equipo, sino **distinguir rápido entre un problema de señal, de geometría y de configuración**.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Propagación, antenas y ruido:** pérdida de espacio libre, ganancia, temperatura de ruido, relación señal/ruido y Eb/N0 ([**B99** · Antenas y propagación para enlaces espaciales](../PROGRAMA_ACADEMICO_COMPLETO.md#b99--antenas-y-propagación-para-enlaces-espaciales), [**B55** · Comunicaciones y navegación satelital](../programa/tronco-comun/B55-comunicaciones-y-navegacion-satelital.md)).
- **Modulación y codificación:** esquemas digitales, corrección de errores, sincronización de portadora y de bit ([**B102** · Modulación, codificación y protocolos de enlace](../PROGRAMA_ACADEMICO_COMPLETO.md#b102--modulación,-codificación-y-protocolos-de-enlace), [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md)).
- **Protocolos y tramas:** telemetría, telecomando y su validación.
- **Tiempo y frecuencia:** UTC, TAI, estándares de frecuencia y Doppler ([**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md)).
- **Pases y apuntado:** predicción de visibilidad a partir de la órbita y planificación de contactos ([**B44** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B44-estimacion-de-orbitas-y-navegacion-espacial.md), [**B57** · Control y operación de misiones espaciales](../programa/tronco-comun/B57-control-y-operacion-de-misiones-espaciales.md)).
- **Enlaces ópticos:** presupuesto, apuntamiento y efectos atmosféricos ([**B100** · Comunicaciones ópticas espaciales (profundización)](../PROGRAMA_ACADEMICO_COMPLETO.md#b100--comunicaciones-ópticas-espaciales-profundización)).
- **Programación y estadística** para procesar registros y automatizar cálculos ([**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md), [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md)).

### Herramientas del oficio

```text
Cálculo:              Python (NumPy, SciPy), hojas de cálculo para presupuestos de enlace
Instrumentación:      analizadores de espectro, generadores de señal, medidores de potencia
Radio:                receptores y transmisores, radios definidas por software
Estación:             controladores de antena y rotores, enrutado de datos
Planificación:        predicción de pases y calendarización de contactos
Registro:             bitácoras de pase, almacenamiento versionado de telemetría
```

Estas son categorías; los productos concretos son una decisión del equipo y este programa no los recomienda por marca. Una herramienta no sustituye el criterio: un presupuesto con supuestos optimistas cierra en el papel y falla en el pase.

### Habilidades no técnicas

- **Rigor documental:** cada margen con su supuesto y su fuente.
- **Diagnóstico bajo presión:** el pase dura minutos y no se repite; ordena la hipótesis y descarta rápido.
- **Disciplina operativa:** un telecomando es una acción irreversible sobre un activo real; se hace con procedimiento, autorización y registro.
- **Comunicación entre equipos:** traducir un problema de señal para quien diseña la carga útil o la operación.
- **Cuidado regulatorio:** saber cuándo una decisión pertenece a otra persona o institución.

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B05** · Física fundamental para el espacio](../programa/tronco-comun/B05-fisica-fundamental-para-el-espacio.md) — A01 · 20 clases
2. 📚 [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md) — A02 · 20 clases
3. 📚 [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) — A02 · 20 clases
4. 📚 [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) — A02 · 26 clases
5. 📚 [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) — A02 · 26 clases
6. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — A02 · 31 clases
7. 📚 [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) — A02 · 24 clases
8. 📚 [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) — A02 · 20 clases

### 🎯 El núcleo del rol

**A02 · Matemática, física computacional y métodos científicos**

1. 📚 [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) — usa 3 de 23 clases: `B13-` C07–C09

**A04 · Óptica, telescopios y observatorios científicos**

2. 📚 [**B30** · Radioastronomía e interferometría](../programa/tronco-comun/B30-radioastronomia-e-interferometria.md) — usa 4 de 20 clases: `B30-` C04–C06, C08
3. 📚 [**B32** · Operaciones de observatorios científicos](../programa/tronco-comun/B32-operaciones-de-observatorios-cientificos.md) — usa 2 de 23 clases: `B32-` C04, C14

**A06 · Mecánica orbital, navegación y vuelo espacial**

4. 📚 [**B44** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B44-estimacion-de-orbitas-y-navegacion-espacial.md) — usa 2 de 30 clases: `B44-` C16, C28

**A07 · Ingeniería y construcción de sistemas espaciales**

5. 📚 [**B49** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md) — usa 1 de 24 clases: `B49-` C15
6. 📚 [**B54** · Aviónica y software crítico espacial](../programa/tronco-comun/B54-avionica-y-software-critico-espacial.md) — usa 1 de 44 clases: `B54-` C04
7. 📚 [**B55** · Comunicaciones y navegación satelital](../programa/tronco-comun/B55-comunicaciones-y-navegacion-satelital.md) — usa 18 de 25 clases: `B55-` C03–C15, C17–C18, C20, C23–C24
8. 📚 [**B56** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) — usa 1 de 24 clases: `B56-` C16
9. 📚 [**B99** · Antenas y propagación para enlaces espaciales](../PROGRAMA_ACADEMICO_COMPLETO.md#b99--antenas-y-propagación-para-enlaces-espaciales) — usa 8 de 8 clases: `B99-` C01–C08
10. 📚 [**B100** · Comunicaciones ópticas espaciales (profundización)](../PROGRAMA_ACADEMICO_COMPLETO.md#b100--comunicaciones-ópticas-espaciales-profundización) — usa 8 de 8 clases: `B100-` C01–C08
11. 📚 [**B102** · Modulación, codificación y protocolos de enlace](../PROGRAMA_ACADEMICO_COMPLETO.md#b102--modulación-codificación-y-protocolos-de-enlace) — usa 6 de 6 clases: `B102-` C01–C06

**A08 · Operaciones de misión y robótica espacial**

12. 📚 [**B57** · Control y operación de misiones espaciales](../programa/tronco-comun/B57-control-y-operacion-de-misiones-espaciales.md) — usa 15 de 30 clases: `B57-` C04–C07, C17, C20, C22–C30

<!-- /ruta -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es un **expediente de enlace y operación** (educativo, sin transmitir):

- un presupuesto de enlace con tablas de supuestos, márgenes y análisis de sensibilidad;
- un simulador de pases en Python, con unidades y pruebas, que prediga visibilidad y Doppler;
- la validación de una cadena de modulación y codificación con curvas de tasa de error;
- un plan de operaciones de estación y una simulación de campaña con registros;
- un diagnóstico de enlace reproducible a partir de datos de telemetría.

Usa datos públicos o sintéticos. No transmitas sin licencia: toda práctica de este expediente es de cálculo o de simulación. Guarda la primera versión y los cambios: el historial pesa tanto como el resultado.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional única verificada. Las referencias que sí se consultaron (2026-11-05) son:

- 📘 **NASA, *State-of-the-Art of Small Spacecraft Technology*, cap. 9 «Communications»** — página con fecha de 18 de mayo de 2026, leída hasta aproximadamente el 80 %. Separa los enlaces de radiofrecuencia (de 300 MHz a 40 GHz, con UHF, S, X y Ka como bandas principales) de los ópticos, que ofrecen mucho más ancho de banda pero exigen apuntamiento muy fino y dependen de las nubes; recuerda que la radiofrecuencia requiere licencia y que la regulación de láseres involucra otros organismos. (https://www.nasa.gov/smallsat-institute/sst-soa/communications/)
- 📗 **NASA, mismo informe, cap. 11 «Ground Data Systems and Mission Operations»** — página con fecha de 11 de mayo de 2026, leída hasta aproximadamente el 45 %. Describe el centro de operaciones de misión, el centro de operaciones científicas, las estaciones, los enlaces directos frente a los de relevo, las redes de agencias y los servicios comerciales de estaciones. (https://www.nasa.gov/smallsat-institute/sst-soa/ground-data-systems-and-mission-operations/)
- 📙 **CCSDS (Comité Consultivo para Sistemas de Datos Espaciales)** — portada del sitio: foro multinacional que desarrolla los estándares de comunicación y datos de uso común en misiones. Qué versión de cada estándar aplica es asunto de cada proyecto. (https://ccsds.org/)

Las licencias, la coordinación de frecuencias y las certificaciones personales dependen de la jurisdicción y **no están verificadas aquí**; consúltalas en la autoridad competente.

## 📈 Progresión del rol

Rutas habituales: **operador/a de estación → ingeniero/a de enlaces y de estación → responsable del diseño de una red de estaciones, de enlaces de espacio profundo u ópticos**. Desde la operación se abre también el control de misión; desde el diseño, la ingeniería de sistemas. Los nombres de nivel y los requisitos dependen de cada organización; no se publican cifras salariales porque no se pudieron verificar con fuentes.

Roles vecinos con los que se comparte formación: [satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md), [radioastronomía](radioastronomia-e-interferometria.md) y [seguridad y resiliencia](seguridad-defensa-y-resiliencia-de-infraestructuras-espaciales.md).

## ⚠️ Mitos y errores comunes

- **«Más potencia arregla cualquier enlace.»** Potencia, ganancia de antena, ancho de banda y ruido están acoplados; subir uno puede violar un límite de otro (licencia, masa, consumo).
- **«Si el presupuesto cierra, el pase funcionará.»** El presupuesto es un modelo; el apuntado, la polarización y la interferencia lo desmienten el día del pase.
- **«Lo óptico reemplaza a la radiofrecuencia.»** Ofrece mucho ancho de banda, pero exige apuntamiento muy fino y depende de las nubes.
- **«Transmitir es solo conectar un equipo.»** Exige licencia y coordinación; operar sin autorización puede causar interferencias a terceros.
- **«La seguridad del enlace es asunto de otro.»** Interferencia, bloqueo y suplantación son amenazas reales; la autenticación es requisito que debes reconocer en tu diseño.

## 🚀 Siguientes pasos

1. **Asienta la base** con física, señales y probabilidad: [**B05** · Física fundamental para el espacio](../programa/tronco-comun/B05-fisica-fundamental-para-el-espacio.md), [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) y [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md).
2. Calcula tu primer presupuesto de enlace con [**B99** · Antenas y propagación para enlaces espaciales](../PROGRAMA_ACADEMICO_COMPLETO.md#b99--antenas-y-propagación-para-enlaces-espaciales) y [**B55** · Comunicaciones y navegación satelital](../programa/tronco-comun/B55-comunicaciones-y-navegacion-satelital.md).
3. Aprende modulación, codificación y protocolos con [**B102** · Modulación, codificación y protocolos de enlace](../PROGRAMA_ACADEMICO_COMPLETO.md#b102--modulación,-codificación-y-protocolos-de-enlace) y valida una cadena con curvas de tasa de error.
4. Practica la operación con [**B57** · Control y operación de misiones espaciales](../programa/tronco-comun/B57-control-y-operacion-de-misiones-espaciales.md): planifica pases y simula una campaña con registros.
5. Reúne tu **expediente** y guarda su historia; si te atrae la profundización, explora [**B100** · Comunicaciones ópticas espaciales (profundización)](../PROGRAMA_ACADEMICO_COMPLETO.md#b100--comunicaciones-ópticas-espaciales-profundización).

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md) · [Radioastronomía e interferometría](radioastronomia-e-interferometria.md) · [Seguridad defensa y resiliencia de infraestructuras espaciales](seguridad-defensa-y-resiliencia-de-infraestructuras-espaciales.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R15-telecomunicaciones-y-estaciones-terrestres-espaciales/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
