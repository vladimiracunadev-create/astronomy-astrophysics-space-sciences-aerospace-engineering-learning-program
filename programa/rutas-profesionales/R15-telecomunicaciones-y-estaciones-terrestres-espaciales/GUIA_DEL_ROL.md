# R15 — Guía del rol: ingeniero/a de telecomunicaciones espaciales y estaciones terrestres

> Esta guía describe el rol para quien decide si es para sí. No es un temario ni una promesa de empleo, habilitación o título. El orden de clases está en [RECORRIDO.md](RECORRIDO.md).

## Qué es

Es la persona responsable de que una nave y el suelo **se oigan**: calcula si un enlace cierra (cuánta potencia llega, con cuánto ruido, con qué margen), elige antena, banda, modulación y codificación, define cómo se sincronizan y se empaquetan los datos, y opera o diseña la estación terrestre que recibe la telemetría y envía los telecomandos.

Su unidad de trabajo es el **enlace** y el **pase**: una ventana de tiempo en la que el satélite es visible, con un presupuesto que debe cerrar y un registro que demuestra qué ocurrió.

## Qué NO es (y con qué se confunde)

- **No es el ingeniero de sistemas del satélite** ([R12](../R12-ingenieria-y-construccion-de-satelites-y-cubesats/INDICE.md)): ese rol reparte recursos de todo el satélite; este es dueño del subsistema de comunicaciones y del lado terreno.
- **No es aviónica ni software de vuelo** ([R13](../R13-avionica-y-software-espacial-de-alta-fiabilidad/INDICE.md)): ve el formato de telemetría que genera el computador, no su código.
- **No es radioastronomía** ([R04](../R04-radioastronomia-e-interferometria/INDICE.md)): comparte antenas, ruido y receptores, pero el objetivo es transportar datos de misión, no medir el cielo.
- **No es seguridad y defensa** ([R22](../R22-seguridad-defensa-y-resiliencia-de-infraestructuras-espaciales/INDICE.md)): la autenticación y el cifrado de enlaces son del módulo de R22; aquí se reconocen como requisito.
- **No es regulación del espectro**: conoce el marco, pero el trámite de coordinación es de quien tenga competencia regulatoria.

## Un día de trabajo

Un día típico alterna dos mundos. En el diseño: actualizar el presupuesto de enlace cuando cambia la potencia del transmisor o la antena, y defender el margen frente a la lluvia o la polarización. En la operación: revisar la lista de pases del día, preparar la estación (antena, radio, enrutado hacia el centro de datos), recibir la telemetría, comprobar la calidad del enlace y registrar anomalías; si un pase falla, diagnosticar si fue el apuntado, el ruido, la interferencia o un error de configuración.

## Qué decide y qué entrega

**Decide:** qué antena, banda, modulación y codificación cierran el enlace con margen; cómo se sincroniza; y qué debe tener la estación (o la red de estaciones) para sostenerlo.

**Entrega:** presupuestos de enlace con supuestos y fuentes; especificaciones de estación y de protocolos; planes de pases; registros de operación; informes de diagnóstico.

## Conocimientos y herramientas

- Propagación, antenas, ruido de sistema, relación señal/ruido y Eb/N0.
- Modulación digital, codificación de canal, sincronización de portadora y de bit.
- Protocolos y tramas de enlace espacial, telemetría y telecomando, y su validación.
- Tiempo y frecuencia: UTC, TAI, estándares de frecuencia, Doppler.
- Predicción de pases desde la órbita, apuntado de antena, planificación de contactos.
- Programación para procesar registros y automatizar cálculos.

Las herramientas concretas (analizadores, radios definidas por software, programas de planificación) son una decisión del equipo; el programa no las recomienda por marca.

## Qué dicen las fuentes consultadas

El capítulo de comunicaciones de la referencia de NASA sobre tecnología de satélites pequeños (consultado el 2026-11-05; fecha de página 18 de mayo de 2026; leído hasta aproximadamente el 80 %) separa los enlaces de radiofrecuencia, de 300 MHz a 40 GHz con UHF, S, X y Ka como bandas principales, de los ópticos, que ofrecen mucho más ancho de banda pero exigen apuntamiento muy fino y dependen de las nubes; y recuerda que la radiofrecuencia requiere licencia, mientras que la regulación de láseres involucra otros organismos. El capítulo de sistemas de datos terrestres y operaciones (consultado el 2026-11-05; fecha de página 11 de mayo de 2026; leído hasta aproximadamente el 45 %) describe el centro de operaciones de misión, el centro de operaciones científicas, las estaciones, los enlaces directos a la Tierra frente a los de relevo, las redes de agencias y los servicios comerciales de estaciones. El Comité Consultivo para Sistemas de Datos Espaciales (CCSDS), consultado el 2026-11-05, es el foro multinacional que desarrolla los estándares de comunicación y datos de uso común en misiones; qué versión de cada estándar aplica es un asunto de cada proyecto.

Fuentes:

- NASA, *State-of-the-Art of Small Spacecraft Technology*, cap. 9 «Communications», <https://www.nasa.gov/smallsat-institute/sst-soa/communications/> — consultado 2026-11-05.
- NASA, *State-of-the-Art of Small Spacecraft Technology*, cap. 11 «Ground Data Systems and Mission Operations», <https://www.nasa.gov/smallsat-institute/sst-soa/ground-data-systems-and-mission-operations/> — consultado 2026-11-05.
- CCSDS, <https://ccsds.org/> — consultado 2026-11-05.

No se citan salarios, cifras de empleo ni certificaciones: no se verificaron.

## Evidencias y portafolio

Un presupuesto de enlace para una misión con tablas de supuestos, márgenes y análisis de sensibilidad; un simulador de pases (Python con unidades y pruebas) que prediga visibilidad y Doppler; la validación de una cadena de modulación y codificación con curvas de tasa de error; un plan de operaciones de estación y una simulación de campaña con registros; un diagnóstico de enlace reproducible a partir de datos de telemetría.

## Progresión

Se entra operando pases y registrando; luego se diseñan presupuestos de enlace y se eligen componentes; después se asume el diseño de una red de estaciones o enlaces de espacio profundo y ópticos. Los nombres de nivel y los requisitos dependen de cada organización.

## Límites éticos y de seguridad

- Transmitir exige licencia y coordinación; operar un transmisor sin autorización puede causar interferencias a terceros y es ilegal en la mayoría de las jurisdicciones. Este programa no sustituye el trámite regulatorio.
- Enviar telecomandos es una acción irreversible sobre un activo real: se hace con autorización, procedimiento y registro.
- La interferencia, el bloqueo y la suplantación son amenazas reales; las estaciones se protegen física y lógicamente.
- Las decisiones críticas se derivan a normas vigentes y a profesionales habilitados.
