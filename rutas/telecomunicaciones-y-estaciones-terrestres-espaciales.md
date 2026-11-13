# 📶 Telecomunicaciones y estaciones terrestres espaciales

> Haces que una nave y el suelo se oigan: calculas si un enlace cierra, eliges antena, banda, modulación y codificación, y diseñas u operas la estación terrestre que recibe la telemetría y envía los telecomandos.
>
> **Nivel de entrada:** base sólida de física, señales, probabilidad y programación; sin ella el rol se queda en operar equipos · **Foco:** propagación, antenas, ruido, modulación y codificación, protocolos de enlace, tiempo y frecuencia, pases y operación de estación · **Entrega:** presupuestos de enlace con supuestos y márgenes, especificaciones de estación y de protocolos, planes de pases, registros de operación e informes de diagnóstico

## 🧭 Qué es y por qué importa

Un satélite que no se comunica es un objeto inerte. Todo lo que la misión produce llega a la Tierra por un enlace, y todo lo que le ordenas viaja por otro. La potencia de la señal cae con la distancia, el ruido de la antena y del receptor se suma, la atmósfera y la lluvia atenúan, y la geometría cambia en cada pase. El trabajo consiste en demostrar con números que, **aun en el peor caso razonable, llegan los datos con un margen**.

Su unidad de trabajo es el **enlace** y el **pase**: una ventana de tiempo en la que el satélite es visible, con un presupuesto que debe cerrar y un registro que demuestra qué ocurrió. El rol se reparte en tres miradas:

- **Diseño del enlace.** Calcula potencia, ganancia, pérdidas, ruido y relación señal/ruido; elige banda, modulación y codificación ([**B91** · Antenas y propagación para enlaces espaciales](../programa/tronco-comun/B91-antenas-y-propagacion-para-enlaces-espaciales.md), [**B94** · Modulación, codificación y protocolos de enlace](../programa/tronco-comun/B94-modulacion-codificacion-y-protocolos-de-enlace.md)). Su pregunta: *¿cierra el enlace con margen y cómo lo defiendo?*
- **Estación terrestre.** Antena, radio, apuntado, enrutado hacia el centro de datos y automatización de pases. Su pregunta: *¿la estación recibe y registra lo que debe, pase tras pase?*
- **Enlaces especiales.** Espacio profundo y comunicaciones ópticas, con mucho más ancho de banda pero con apuntamiento muy fino y dependencia de las nubes ([**B92** · Comunicaciones ópticas espaciales (profundización)](../programa/tronco-comun/B92-comunicaciones-opticas-espaciales-profundizacion.md)).

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

- **Propagación, antenas y ruido:** pérdida de espacio libre, ganancia, temperatura de ruido, relación señal/ruido y Eb/N0 ([**B91** · Antenas y propagación para enlaces espaciales](../programa/tronco-comun/B91-antenas-y-propagacion-para-enlaces-espaciales.md), [**B89** · Comunicaciones y navegación satelital](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md)).
- **Modulación y codificación:** esquemas digitales, corrección de errores, sincronización de portadora y de bit ([**B94** · Modulación, codificación y protocolos de enlace](../programa/tronco-comun/B94-modulacion-codificacion-y-protocolos-de-enlace.md), [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md)).
- **Protocolos y tramas:** telemetría, telecomando y su validación.
- **Tiempo y frecuencia:** UTC, TAI, estándares de frecuencia y Doppler ([**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md)).
- **Pases y apuntado:** predicción de visibilidad a partir de la órbita y planificación de contactos ([**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md), [**B96** · Control y operación de misiones espaciales](../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md)).
- **Enlaces ópticos:** presupuesto, apuntamiento y efectos atmosféricos ([**B92** · Comunicaciones ópticas espaciales (profundización)](../programa/tronco-comun/B92-comunicaciones-opticas-espaciales-profundizacion.md)).
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

2. 📚 [**B46** · Radioastronomía e interferometría](../programa/tronco-comun/B46-radioastronomia-e-interferometria.md) — usa 4 de 20 clases: `B46-` C04–C06, C08
3. 📚 [**B48** · Operaciones de observatorios científicos](../programa/tronco-comun/B48-operaciones-de-observatorios-cientificos.md) — usa 2 de 23 clases: `B48-` C04, C14

**A06 · Mecánica orbital, navegación y vuelo espacial**

4. 📚 [**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md) — usa 2 de 30 clases: `B74-` C16, C28

**A07 · Ingeniería y construcción de sistemas espaciales**

5. 📚 [**B83** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) — usa 1 de 24 clases: `B83-` C15
6. 📚 [**B88** · Aviónica y software crítico espacial](../programa/tronco-comun/B88-avionica-y-software-critico-espacial.md) — usa 1 de 44 clases: `B88-` C04
7. 📚 [**B89** · Comunicaciones y navegación satelital](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) — usa 18 de 25 clases: `B89-` C03–C15, C17–C18, C20, C23–C24
8. 📚 [**B90** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) — usa 1 de 24 clases: `B90-` C16
9. 📚 [**B91** · Antenas y propagación para enlaces espaciales](../programa/tronco-comun/B91-antenas-y-propagacion-para-enlaces-espaciales.md) — usa 8 de 8 clases: `B91-` C01–C08
10. 📚 [**B92** · Comunicaciones ópticas espaciales (profundización)](../programa/tronco-comun/B92-comunicaciones-opticas-espaciales-profundizacion.md) — usa 8 de 8 clases: `B92-` C01–C08
11. 📚 [**B94** · Modulación, codificación y protocolos de enlace](../programa/tronco-comun/B94-modulacion-codificacion-y-protocolos-de-enlace.md) — usa 6 de 6 clases: `B94-` C01–C06

**A08 · Operaciones de misión y robótica espacial**

12. 📚 [**B96** · Control y operación de misiones espaciales](../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) — usa 15 de 30 clases: `B96-` C04–C07, C17, C20, C22–C30

<!-- /ruta -->

<!-- recorrido:inicio -->
### 🗺️ Recorrido módulo por módulo

El rol se estudia en **8 módulos** de 10 temas cada uno (cada tema es un par «concepto + aplicación»). Haz el diagnóstico, avanza por los módulos **en orden** y cierra cada uno con su checkpoint; al final, el proyecto y el criterio de salida.

**🩺 Diagnóstico de entrada.** Si respondes «no sé» a dos o más, empieza por los fundamentos de arriba:

- ¿Puedes calcular pérdidas por espacio libre y ganancia de antena?
- ¿Sabes qué es la relación señal-ruido y la tasa de error?
- ¿Entiendes la modulación digital básica?
- ¿Conoces el retardo de la luz y su efecto en los protocolos?

#### R15-M01 · Antenas espaciales avanzadas

1. **Teoría de antenas** — [`B91-C01`](../programa/clases/B91/B91-C01-fundamentos-de-teoria-de-antenas/CLASE.md)
2. **Apertura y ganancia** — [`B46-C05`](../programa/clases/B46/B46-C05-ganancia-y-temperatura-de-antena/CLASE.md), [`B89-C06`](../programa/clases/B89/B89-C06-ganancias-y-perdidas-de-antena/CLASE.md)
3. **Diagramas y lóbulos** — [`B46-C04`](../programa/clases/B46/B46-C04-diagramas-de-radiacion/CLASE.md)
4. **Polarización** — [`B91-C02`](../programa/clases/B91/B91-C02-polarizacion-de-antenas-y-perdidas-por-desadaptacion/CLASE.md)
5. **Arreglos de fase** — [`B91-C03`](../programa/clases/B91/B91-C03-arreglos-de-antenas-y-antenas-de-barrido-electronico/CLASE.md)
6. **Antenas desplegables** — [`B91-C04`](../programa/clases/B91/B91-C04-antenas-desplegables-y-estructuras-de-gran-apertura/CLASE.md)
7. **Eficiencia de antena** — [`B89-C06`](../programa/clases/B89/B89-C06-ganancias-y-perdidas-de-antena/CLASE.md)
8. **Apuntado de estación** — [`B96-C05`](../programa/clases/B96/B96-C05-estaciones-de-seguimiento/CLASE.md), [`B89-C15`](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md)
9. **Calibración de patrón** — [`B91-C05`](../programa/clases/B91/B91-C05-medicion-y-calibracion-de-antenas/CLASE.md)
10. **Análisis de compromiso de antenas** — [`B91-C06`](../programa/clases/B91/B91-C06-seleccion-y-compromiso-de-diseno-de-antenas/CLASE.md)

✅ **Checkpoint R15-M01.** Sin mirar el material, explica cómo se relacionan «Teoría de antenas», «Antenas desplegables» y «Análisis de compromiso de antenas», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R15-M02 · Presupuesto de enlace de misión

1. **Ecuación de Friis** — [`B89-C04`](../programa/clases/B89/B89-C04-propagacion-y-perdidas-de-espacio-libre/CLASE.md), [`B89-C05`](../programa/clases/B89/B89-C05-presupuesto-de-enlace/CLASE.md)
2. **Atenuación atmosférica** — [`B91-C07`](../programa/clases/B91/B91-C07-atenuacion-atmosferica-y-efectos-de-la-lluvia-en-enlaces/CLASE.md)
3. **Pérdidas de polarización** — [`B91-C02`](../programa/clases/B91/B91-C02-polarizacion-de-antenas-y-perdidas-por-desadaptacion/CLASE.md)
4. **Temperatura de ruido** — [`B89-C07`](../programa/clases/B89/B89-C07-figura-de-ruido-de-receptor/CLASE.md), [`B46-C06`](../programa/clases/B46/B46-C06-ruido-de-sistema-y-radiometria/CLASE.md)
5. **Relación C/N0** — [`B89-C23`](../programa/clases/B89/B89-C23-relacion-c-n0-eb-n0-y-tasa-de-error-de-bit/CLASE.md)
6. **Margen de enlace** — [`B89-C05`](../programa/clases/B89/B89-C05-presupuesto-de-enlace/CLASE.md)
7. **BER y Eb/N0** — [`B89-C23`](../programa/clases/B89/B89-C23-relacion-c-n0-eb-n0-y-tasa-de-error-de-bit/CLASE.md)
8. **Efectos de lluvia** — [`B91-C07`](../programa/clases/B91/B91-C07-atenuacion-atmosferica-y-efectos-de-la-lluvia-en-enlaces/CLASE.md)
9. **Presupuesto ascendente** — [`B89-C05`](../programa/clases/B89/B89-C05-presupuesto-de-enlace/CLASE.md)
10. **Presupuesto descendente** — [`B89-C05`](../programa/clases/B89/B89-C05-presupuesto-de-enlace/CLASE.md)

✅ **Checkpoint R15-M02.** Sin mirar el material, explica cómo se relacionan «Ecuación de Friis», «Margen de enlace» y «Presupuesto descendente», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R15-M03 · Modulación y codificación de canal

1. **Modulación PSK** — [`B89-C08`](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md)
2. **Modulación QAM** — [`B89-C08`](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md)
3. **Codificación convolucional** — [`B89-C09`](../programa/clases/B89/B89-C09-codificacion-correctora-de-errores/CLASE.md)
4. **Códigos Reed-Solomon** — [`B94-C01`](../programa/clases/B94/B94-C01-codigos-reed-solomon-y-ldpc/CLASE.md)
5. **Códigos LDPC** — [`B94-C01`](../programa/clases/B94/B94-C01-codigos-reed-solomon-y-ldpc/CLASE.md)
6. **Entrelazado** — [`B94-C02`](../programa/clases/B94/B94-C02-entrelazado-y-concatenacion-de-codigos/CLASE.md)
7. **Sincronización de bit** — [`B89-C10`](../programa/clases/B89/B89-C10-sincronizacion-de-portadora/CLASE.md)
8. **Corrección de errores** — [`B89-C09`](../programa/clases/B89/B89-C09-codificacion-correctora-de-errores/CLASE.md), [`B88-C04`](../programa/clases/B88/B88-C04-memorias-y-correccion-de-errores/CLASE.md)
9. **Tramas CCSDS** — [`B94-C03`](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md)
10. **Prueba de enlace digital** — [`B90-C16`](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md)

✅ **Checkpoint R15-M03.** Sin mirar el material, explica cómo se relacionan «Modulación PSK», «Entrelazado» y «Prueba de enlace digital», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R15-M04 · Diseño de redes de estaciones terrestres

1. **Cobertura de estaciones** — [`B89-C17`](../programa/clases/B89/B89-C17-constelaciones-y-cobertura/CLASE.md), [`B96-C05`](../programa/clases/B96/B96-C05-estaciones-de-seguimiento/CLASE.md)
2. **Visibilidad de pases** — [`B96-C04`](../programa/clases/B96/B96-C04-planificacion-de-contactos/CLASE.md), [`B48-C04`](../programa/clases/B48/B48-C04-planificacion-por-visibilidad/CLASE.md)
3. **Coordinación temporal** — [`B96-C17`](../programa/clases/B96/B96-C17-coordinacion-de-multiples-estaciones/CLASE.md), [`B74-C16`](../programa/clases/B74/B74-C16-sincronizacion-temporal/CLASE.md)
4. **Redes de estaciones** — [`B96-C05`](../programa/clases/B96/B96-C05-estaciones-de-seguimiento/CLASE.md), [`B96-C17`](../programa/clases/B96/B96-C17-coordinacion-de-multiples-estaciones/CLASE.md)
5. **Enlaces hacia centros de datos** — [`B96-C22`](../programa/clases/B96/B96-C22-transferencia-de-datos-entre-estacion-y-centro-de-datos/CLASE.md)
6. **Redundancia terrestre** — [`B96-C23`](../programa/clases/B96/B96-C23-continuidad-y-redundancia-de-las-operaciones-terrestres/CLASE.md)
7. **Operación remota** — [`B96-C24`](../programa/clases/B96/B96-C24-operacion-remota-y-automatizada-de-estaciones/CLASE.md)
8. **Seguridad física** — [`B96-C25`](../programa/clases/B96/B96-C25-seguridad-fisica-y-control-de-acceso-de-estaciones-terrestres/CLASE.md)
9. **Gestión de incidentes** — [`B96-C26`](../programa/clases/B96/B96-C26-gestion-de-incidentes-en-la-operacion-de-estaciones/CLASE.md)
10. **Diseño de red global** — [`B89-C20`](../programa/clases/B89/B89-C20-diseno-de-red-de-comunicaciones-de-mision/CLASE.md), [`B96-C17`](../programa/clases/B96/B96-C17-coordinacion-de-multiples-estaciones/CLASE.md)

✅ **Checkpoint R15-M04.** Sin mirar el material, explica cómo se relacionan «Cobertura de estaciones», «Redundancia terrestre» y «Diseño de red global», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R15-M05 · Enlaces de radiofrecuencia profundos

1. **Pérdidas de espacio profundo** — [`B89-C04`](../programa/clases/B89/B89-C04-propagacion-y-perdidas-de-espacio-libre/CLASE.md), [`B89-C13`](../programa/clases/B89/B89-C13-protocolos-para-espacio-profundo/CLASE.md)
2. **Antenas de gran apertura** — [`B91-C08`](../programa/clases/B91/B91-C08-antenas-de-gran-apertura-y-estaciones-de-espacio-profundo/CLASE.md)
3. **Bandas X y Ka** — [`B89-C03`](../programa/clases/B89/B89-C03-bandas-vhf-uhf-s-x-ka/CLASE.md)
4. **Seguimiento Doppler** — [`B89-C15`](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md)
5. **Medidas de rango** — [`B74-C28`](../programa/clases/B74/B74-C28-medidas-de-rango-y-doppler-para-determinar-la-orbita/CLASE.md)
6. **Osciladores ultraestables** — [`B46-C08`](../programa/clases/B46/B46-C08-osciladores-y-estabilidad/CLASE.md)
7. **Telemetría débil** — [`B89-C24`](../programa/clases/B89/B89-C24-recepcion-de-telemetria-debil/CLASE.md)
8. **Corrección atmosférica** — [`B91-C07`](../programa/clases/B91/B91-C07-atenuacion-atmosferica-y-efectos-de-la-lluvia-en-enlaces/CLASE.md)
9. **Planificación de sesiones** — [`B96-C04`](../programa/clases/B96/B96-C04-planificacion-de-contactos/CLASE.md)
10. **Caso de enlace interplanetario** — [`B89-C05`](../programa/clases/B89/B89-C05-presupuesto-de-enlace/CLASE.md), [`B89-C13`](../programa/clases/B89/B89-C13-protocolos-para-espacio-profundo/CLASE.md)

✅ **Checkpoint R15-M05.** Sin mirar el material, explica cómo se relacionan «Pérdidas de espacio profundo», «Osciladores ultraestables» y «Caso de enlace interplanetario», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R15-M06 · Enlaces ópticos espaciales

1. **Terminales ópticos** — [`B89-C18`](../programa/clases/B89/B89-C18-comunicaciones-opticas-espaciales/CLASE.md)
2. **Fuentes láser espaciales** — [`B92-C01`](../programa/clases/B92/B92-C01-fuentes-laser-y-amplificadores-para-enlaces-espaciales/CLASE.md)
3. **Dispersión del haz** — [`B92-C02`](../programa/clases/B92/B92-C02-divergencia-del-haz-y-perdidas-por-apuntamiento-optico/CLASE.md)
4. **Apuntamiento fino** — [`B92-C03`](../programa/clases/B92/B92-C03-adquisicion-apuntamiento-y-seguimiento-opticos/CLASE.md)
5. **Atmósfera y nubes** — [`B92-C04`](../programa/clases/B92/B92-C04-atmosfera-y-nubes-en-enlaces-opticos-con-la-tierra/CLASE.md)
6. **Detectores ópticos** — [`B92-C05`](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md)
7. **Modulación óptica** — [`B92-C06`](../programa/clases/B92/B92-C06-modulacion-y-codificacion-en-enlaces-opticos/CLASE.md)
8. **Enlace óptico de espacio profundo** — [`B92-C07`](../programa/clases/B92/B92-C07-enlaces-opticos-de-espacio-profundo/CLASE.md)
9. **Márgenes y disponibilidad** — [`B92-C08`](../programa/clases/B92/B92-C08-margenes-y-disponibilidad-de-enlaces-opticos/CLASE.md)
10. **Evaluación de arquitectura óptica** — [`B89-C18`](../programa/clases/B89/B89-C18-comunicaciones-opticas-espaciales/CLASE.md), [`B89-C20`](../programa/clases/B89/B89-C20-diseno-de-red-de-comunicaciones-de-mision/CLASE.md)

✅ **Checkpoint R15-M06.** Sin mirar el material, explica cómo se relacionan «Terminales ópticos», «Detectores ópticos» y «Evaluación de arquitectura óptica», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R15-M07 · Sincronización y protocolos de misión

1. **Tiempo UTC y TAI** — [`B13-C08`](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md), [`B13-C09`](../programa/clases/B13/B13-C09-segundos-intercalares-y-cronologia/CLASE.md)
2. **Estándares de frecuencia** — [`B13-C07`](../programa/clases/B13/B13-C07-relojes-atomicos-y-frecuencia/CLASE.md)
3. **Sincronización de estación** — [`B74-C16`](../programa/clases/B74/B74-C16-sincronizacion-temporal/CLASE.md)
4. **Protocolos CCSDS** — [`B89-C11`](../programa/clases/B89/B89-C11-telemetria-ccsds/CLASE.md), [`B89-C12`](../programa/clases/B89/B89-C12-telecomandos-ccsds/CLASE.md), [`B89-C13`](../programa/clases/B89/B89-C13-protocolos-para-espacio-profundo/CLASE.md)
5. **Telemetría transfer frame** — [`B94-C03`](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md)
6. **Telecomandos transfer frame** — [`B94-C03`](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md)
7. **Enrutamiento y almacenamiento** — [`B94-C04`](../programa/clases/B94/B94-C04-redes-con-retardo-y-desconexion-enrutamiento-y-almacenamiento/CLASE.md)
8. **Calidad de servicio** — [`B94-C05`](../programa/clases/B94/B94-C05-calidad-de-servicio-y-prioridades-en-redes-espaciales/CLASE.md)
9. **Gestión de configuraciones** — [`B83-C15`](../programa/clases/B83/B83-C15-gestion-de-configuracion/CLASE.md)
10. **Validación de protocolos** — [`B94-C06`](../programa/clases/B94/B94-C06-validacion-y-conformidad-de-protocolos-de-enlace/CLASE.md)

✅ **Checkpoint R15-M07.** Sin mirar el material, explica cómo se relacionan «Tiempo UTC y TAI», «Telecomandos transfer frame» y «Validación de protocolos», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R15-M08 · Operaciones integrales de estaciones terrestres

1. **Gestión de estación terrestre** — [`B89-C14`](../programa/clases/B89/B89-C14-estaciones-terrestres/CLASE.md), [`B96-C05`](../programa/clases/B96/B96-C05-estaciones-de-seguimiento/CLASE.md)
2. **Planificación de pases** — [`B96-C04`](../programa/clases/B96/B96-C04-planificacion-de-contactos/CLASE.md)
3. **Operación de RF** — [`B96-C27`](../programa/clases/B96/B96-C27-operacion-de-equipos-de-radiofrecuencia-en-la-estacion/CLASE.md)
4. **Control de antena** — [`B96-C28`](../programa/clases/B96/B96-C28-control-y-seguimiento-de-la-antena-de-estacion/CLASE.md)
5. **Recepción de telemetría** — [`B96-C06`](../programa/clases/B96/B96-C06-telemetria-operativa/CLASE.md)
6. **Envío autorizado de telecomandos** — [`B96-C07`](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md)
7. **Diagnóstico de enlace** — [`B96-C29`](../programa/clases/B96/B96-C29-diagnostico-de-fallas-de-enlace/CLASE.md)
8. **Mantenimiento preventivo** — [`B48-C14`](../programa/clases/B48/B48-C14-mantenimiento-preventivo/CLASE.md)
9. **Registro de operaciones** — [`B96-C30`](../programa/clases/B96/B96-C30-registro-y-auditoria-de-operaciones/CLASE.md)
10. **Simulación de campaña de operación** — [`B96-C20`](../programa/clases/B96/B96-C20-simulacion-de-jornada-de-control-de-mision/CLASE.md)

✅ **Checkpoint R15-M08.** Sin mirar el material, explica cómo se relacionan «Gestión de estación terrestre», «Envío autorizado de telecomandos» y «Simulación de campaña de operación», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

**🎯 Proyecto final · Presupuesto de enlace y diseño de una estación terrestre.** Para una misión de órbita baja y otra de espacio profundo, calcula el presupuesto de enlace, elige modulación y codificación y diseña la estación y su red.

Entregables:

- Presupuestos de enlace con márgenes
- Elección de modulación y codificación con su justificación
- Diseño de la estación y de la red de apoyo
- Plan de operaciones con contactos y recuperación

Criterios de evaluación:

- Los presupuestos se verifican con una segunda herramienta
- Los márgenes cubren lluvia y desapuntado
- El diseño de red cubre las ventanas de la misión
- El plan contempla pérdida de enlace

**🏁 Criterio de salida.** Has terminado la ruta cuando:

- Puedes cerrar un presupuesto de enlace y justificar sus márgenes.
- Puedes diseñar una estación terrestre y una red de apoyo.
- Puedes planear operaciones de comunicaciones con contingencias.

<!-- /recorrido -->

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
2. Calcula tu primer presupuesto de enlace con [**B91** · Antenas y propagación para enlaces espaciales](../programa/tronco-comun/B91-antenas-y-propagacion-para-enlaces-espaciales.md) y [**B89** · Comunicaciones y navegación satelital](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md).
3. Aprende modulación, codificación y protocolos con [**B94** · Modulación, codificación y protocolos de enlace](../programa/tronco-comun/B94-modulacion-codificacion-y-protocolos-de-enlace.md) y valida una cadena con curvas de tasa de error.
4. Practica la operación con [**B96** · Control y operación de misiones espaciales](../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md): planifica pases y simula una campaña con registros.
5. Reúne tu **expediente** y guarda su historia; si te atrae la profundización, explora [**B92** · Comunicaciones ópticas espaciales (profundización)](../programa/tronco-comun/B92-comunicaciones-opticas-espaciales-profundizacion.md).

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md) · [Radioastronomía e interferometría](radioastronomia-e-interferometria.md) · [Seguridad defensa y resiliencia de infraestructuras espaciales](seguridad-defensa-y-resiliencia-de-infraestructuras-espaciales.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R15-telecomunicaciones-y-estaciones-terrestres-espaciales/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
