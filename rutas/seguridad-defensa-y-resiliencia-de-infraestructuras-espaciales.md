# 🛡️ Seguridad defensa y resiliencia de infraestructuras espaciales

> Proteges la continuidad de lo que el espacio presta a la sociedad —satélites, estaciones terrestres, enlaces y servicios— con enfoque defensivo: conciencia situacional, riesgo de colisión, desechos, continuidad y gestión de crisis.
>
> **Nivel de entrada:** base de mecánica orbital, probabilidad e informática; criterio para trabajar con fuentes públicas y reglas escritas · **Foco:** seguimiento orbital, conjunciones, desechos, modelo defensivo de riesgos, continuidad y crisis · **Entrega:** informes de precisión de seguimiento, decisiones de conjunción documentadas, planes de fin de vida y de continuidad, modelo defensivo de riesgos y un informe posterior a un simulacro.

> **Alcance de esta guía.** Tratamiento **histórico, regulatorio, defensivo y de resiliencia**. No enseña capacidades de daño, técnicas de intrusión ni de interferencia, ni procedimientos operativos ofensivos, y no describe cómo vulnerar un sistema.

## 🧭 Qué es y por qué importa

Navegación, comunicaciones, observación de la Tierra y tiempo dependen de infraestructura espacial. Esa infraestructura tiene dos particularidades: **no se repara con facilidad** (un satélite no se reinicia ni se visita) y **comparte un entorno saturado** de objetos y de espectro. Proteger su continuidad es un trabajo con una mitad técnica y otra institucional.

Tu unidad de trabajo es el **riesgo a la continuidad**: un objeto que se acerca, un desecho que se fragmenta, un enlace que se pierde, una estación sin respaldo, una vulnerabilidad en un proceso de telecomando. De la parte técnica salen el seguimiento orbital, la probabilidad de colisión y la mitigación de desechos; de la institucional, los modelos de amenaza defensivos, los planes de continuidad, la coordinación y la comunicación en una crisis.

En la práctica el rol se reparte en tres miradas que conviene conocer antes de elegir:

- **Conciencia situacional y tráfico.** Catálogos, seguimiento óptico y por radar, calidad y latencia de los datos, conjunciones, probabilidad de colisión y evasión. Su pregunta es: *¿qué hay ahí, qué tan bien lo sé y qué decisión justifica el dato?*
- **Sostenibilidad orbital.** Generación y mitigación de desechos, disposición al fin de vida, reentrada, directrices técnicas. Su pregunta es: *¿cómo dejo la órbita en un estado que otros puedan usar?*
- **Infraestructura y continuidad.** Modelo defensivo de riesgos, seguridad de estaciones terrestres, gestión de accesos, respuesta a incidentes, evidencias, comunicación de crisis y continuidad institucional. Su pregunta es: *¿cuánto aguanta el servicio y cómo se recupera?*

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es ciberseguridad general.** Comparte el vocabulario defensivo, pero los activos, los tiempos (un satélite no se reinicia fácilmente) y los marcos jurídicos son del sector espacial.
- **No es operación de misiones.** El centro de control (bloque [**B96**](../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md)) opera el satélite; tú evalúas su exposición y su continuidad y te coordinas con él.
- **No es derecho espacial.** El marco jurídico se conoce, pero su interpretación pertenece a [Derecho, políticas y negocios espaciales](derecho-politicas-y-negocios-espaciales.md).
- **No es el especialista de un solo componente.** [Telecomunicaciones y estaciones terrestres](telecomunicaciones-y-estaciones-terrestres-espaciales.md) y [aviónica y software de alta fiabilidad](avionica-y-software-espacial-de-alta-fiabilidad.md) profundizan cada parte; este rol evalúa la exposición del conjunto.
- **No es un rol ofensivo ni militar operativo.** Este programa no enseña capacidades de daño. Las doctrinas y la historia se estudian a partir de fuentes públicas.

## 🗓️ Un día en el puesto

No hay un día típico, pero el trabajo se reparte entre estas actividades:

- **Alerta de conjunción.** Entra una alerta: comparas la distancia de aproximación y la probabilidad de colisión con la incertidumbre del seguimiento, consultas a quien opera el satélite y documentas la decisión y su justificación.
- **Calidad del dato.** Revisas cobertura, latencia y sesgos de las fuentes de seguimiento y comparas con efemérides de referencia.
- **Fin de vida.** Contrastas un plan de disposición con la norma de mitigación vigente, citada con versión y fecha.
- **Modelo de riesgos.** Ajustas el modelo defensivo de una estación terrestre: activos, dependencias de proveedores, controles de acceso y objetivos de recuperación.
- **Preparar un simulacro de mesa.** Escenario, roles, comunicación con operadores y autoridades, y criterios para escalar.
- **Informes.** De precisión, de decisión y posteriores a un incidente. Distingues siempre el hecho de la atribución.

Dicho sin adornos: se trabaja con **datos imperfectos y decisiones con consecuencias**; la habilidad es decidir bien con la incertidumbre que hay y dejarlo por escrito.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Mecánica orbital y estimación:** órbitas, perturbaciones, determinación y covarianza, en [**B71**](../programa/tronco-comun/B71-mecanica-orbital-fundamental.md), [**B72**](../programa/tronco-comun/B72-perturbaciones-y-evolucion-de-orbitas.md) y [**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md).
- **Tráfico y sostenibilidad:** población de objetos, catálogos, seguimiento óptico y por radar, conjunciones, probabilidad de colisión, evasión, desechos, fin de vida, calidad y límites de las redes de vigilancia, en [**B118** · Tráfico espacial y sostenibilidad orbital](../programa/tronco-comun/B118-trafico-espacial-y-sostenibilidad-orbital.md).
- **Marco jurídico y de política:** tratados, registro, autorización de operadores, doctrinas declaradas públicamente, normas de comportamiento responsable, atribución y desinformación, en [**B119** · Derecho, seguridad y geopolítica espacial](../programa/tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md).
- **Resiliencia y continuidad:** dependencias de proveedores, impacto y objetivos de recuperación, modelo defensivo de riesgos, seguridad de estaciones, accesos, respuesta a incidentes, severidad, comunicación de crisis, evidencias y continuidad institucional, en [**B122** · Resiliencia y continuidad de infraestructura espacial](../programa/tronco-comun/B122-resiliencia-y-continuidad-de-infraestructura-espacial.md).
- **Software crítico, comunicaciones y operaciones:** [**B88**](../programa/tronco-comun/B88-avionica-y-software-critico-espacial.md), [**B89**](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) y [**B96**](../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md).
- **Probabilidad e incertidumbre:** cómo se propaga la incertidumbre del seguimiento a una probabilidad de colisión y cuándo esa cifra no basta para decidir.

### Herramientas del oficio

```text
Análisis orbital:      Python (NumPy, SciPy), propagadores y herramientas de estimación con efemérides de referencia
Datos de vigilancia:   catálogos y mensajes de conjunción de fuentes públicas, con su procedencia y latencia
Riesgo defensivo:      modelos de activos, dependencias y controles; análisis de impacto y de recuperación
Gestión de incidentes: planes, guías de comunicación y registros con cadena de custodia
Ejercicios:            simulacros de mesa con roles y criterios de escalamiento
```

El trabajo defensivo sobre estaciones y satélites se hace **solo en entornos autorizados**, con sistemas propios o simulados y reglas de actuación escritas. Ninguna herramienta decide por ti: una probabilidad de colisión sin su incertidumbre no es una razón suficiente para maniobrar ni para no hacerlo.

### Habilidades no técnicas

- **Decidir con datos imperfectos** y documentar el porqué.
- **Comunicación en crisis:** mensajes claros a operadores, autoridades y público, sin sobreprometer.
- **Distinguir hecho de atribución:** una de las habilidades más valiosas y menos comunes del campo.
- **Rigor ético y de confidencialidad:** manejar datos de vigilancia y servicios duales con criterio.

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B71** · Mecánica orbital fundamental](../programa/tronco-comun/B71-mecanica-orbital-fundamental.md) — A06 · 20 clases
2. 📚 [**B73** · Mecánica celeste, resonancias y caos](../programa/tronco-comun/B73-mecanica-celeste-resonancias-y-caos.md) — A06 · 22 clases
3. 📚 [**B75** · Trayectorias y misiones interplanetarias](../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md) — A06 · 30 clases

### 🎯 El núcleo del rol

**A01 · Alfabetización científica, astronómica y tecnológica**

1. 📚 [**B02** · Historia, arqueoastronomía y culturas del cielo](../programa/tronco-comun/B02-historia-arqueoastronomia-y-culturas-del-cielo.md) — usa 1 de 20 clases: `B02-` C19

**A06 · Mecánica orbital, navegación y vuelo espacial**

2. 📚 [**B72** · Perturbaciones y evolución de órbitas](../programa/tronco-comun/B72-perturbaciones-y-evolucion-de-orbitas.md) — usa 2 de 21 clases: `B72-` C20–C21
3. 📚 [**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md) — usa 14 de 30 clases: `B74-` C01–C04, C06–C09, C11–C12, C19–C20, C29–C30
4. 📚 [**B76** · Dinámica cislunar y operaciones de proximidad](../programa/tronco-comun/B76-dinamica-cislunar-y-operaciones-de-proximidad.md) — usa 2 de 20 clases: `B76-` C11, C14
5. 📚 [**B77** · Dinámica de lanzamiento y reentrada](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md) — usa 1 de 25 clases: `B77-` C14

**A07 · Ingeniería y construcción de sistemas espaciales**

6. 📚 [**B83** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) — usa 1 de 24 clases: `B83-` C15
7. 📚 [**B86** · Sistemas de potencia y energía espacial](../programa/tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md) — usa 2 de 23 clases: `B86-` C11, C13
8. 📚 [**B88** · Aviónica y software crítico espacial](../programa/tronco-comun/B88-avionica-y-software-critico-espacial.md) — usa 6 de 44 clases: `B88-` C11–C13, C17–C19
9. 📚 [**B89** · Comunicaciones y navegación satelital](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) — usa 5 de 25 clases: `B89-` C12, C14–C15, C20, C25

**A08 · Operaciones de misión y robótica espacial**

10. 📚 [**B96** · Control y operación de misiones espaciales](../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) — usa 10 de 30 clases: `B96-` C01, C03–C04, C07, C12–C15, C17, C19

**A09 · Astronáutica humana, medicina y hábitats**

11. 📚 [**B104** · Astronáutica y preparación de astronautas](../programa/tronco-comun/B104-astronautica-y-preparacion-de-astronautas.md) — usa 1 de 23 clases: `B104-` C09

**A10 · Entorno orbital, derecho y seguridad espacial**

12. 📚 [**B118** · Tráfico espacial y sostenibilidad orbital](../programa/tronco-comun/B118-trafico-espacial-y-sostenibilidad-orbital.md) — usa 22 de 24 clases: `B118-` C01–C15, C18–C24
13. 📚 [**B119** · Derecho, seguridad y geopolítica espacial](../programa/tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md) — usa 19 de 36 clases: `B119-` C01, C04, C06–C08, C11–C16, C18–C20, C26–C30
14. 📚 [**B122** · Resiliencia y continuidad de infraestructura espacial](../programa/tronco-comun/B122-resiliencia-y-continuidad-de-infraestructura-espacial.md) — usa 10 de 10 clases: `B122-` C01–C10

<!-- /ruta -->

<!-- recorrido:inicio -->
### 🗺️ Recorrido módulo por módulo

El rol se estudia en **8 módulos** de 10 temas cada uno (cada tema es un par «concepto + aplicación»). Haz el diagnóstico, avanza por los módulos **en orden** y cierra cada uno con su checkpoint; al final, el proyecto y el criterio de salida.

**🩺 Diagnóstico de entrada.** Si respondes «no sé» a dos o más, empieza por los fundamentos de arriba:

- ¿Puedes calcular la posición de un satélite a partir de elementos orbitales?
- ¿Sabes qué es una conjunción y una probabilidad de colisión?
- ¿Entiendes conceptos básicos de seguridad de la información?
- ¿Conoces el marco jurídico básico del uso del espacio?

#### R22-M01 · Vigilancia y conciencia situacional espacial

1. **Objetos residentes espaciales** — [`B118-C01`](../programa/clases/B118/B118-C01-poblacion-de-objetos-orbitales/CLASE.md), [`B118-C02`](../programa/clases/B118/B118-C02-catalogos-de-objetos-espaciales/CLASE.md)
2. **Sensores ópticos** — [`B118-C03`](../programa/clases/B118/B118-C03-deteccion-y-seguimiento-optico/CLASE.md), [`B119-C13`](../programa/clases/B119/B119-C13-vigilancia-y-conciencia-situacional-espacial/CLASE.md)
3. **Radar de seguimiento** — [`B118-C04`](../programa/clases/B118/B118-C04-deteccion-por-radar/CLASE.md)
4. **Catálogos orbitales** — [`B118-C02`](../programa/clases/B118/B118-C02-catalogos-de-objetos-espaciales/CLASE.md)
5. **Identificación de objetos** — [`B118-C02`](../programa/clases/B118/B118-C02-catalogos-de-objetos-espaciales/CLASE.md), [`B119-C04`](../programa/clases/B119/B119-C04-convenio-de-registro/CLASE.md), [`B119-C07`](../programa/clases/B119/B119-C07-registro-nacional-de-objetos/CLASE.md)
6. **Calidad de datos SSA** — [`B118-C21`](../programa/clases/B118/B118-C21-calidad-latencia-y-trazabilidad-de-datos-de-vigilancia-espacial/CLASE.md)
7. **Situational awareness civil** — [`B119-C13`](../programa/clases/B119/B119-C13-vigilancia-y-conciencia-situacional-espacial/CLASE.md), [`B118-C18`](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md)
8. **Compartición de información** — [`B118-C22`](../programa/clases/B118/B118-C22-intercambio-de-datos-de-vigilancia-entre-operadores-y-estados/CLASE.md)
9. **Limitaciones de vigilancia** — [`B118-C23`](../programa/clases/B118/B118-C23-cobertura-sesgos-y-limites-de-las-redes-de-vigilancia/CLASE.md)
10. **Reporte de evento orbital** — [`B118-C20`](../programa/clases/B118/B118-C20-evaluacion-de-riesgo-de-conjuncion-documentada/CLASE.md), [`B96-C19`](../programa/clases/B96/B96-C19-lecciones-aprendidas-operativas/CLASE.md)

✅ **Checkpoint R22-M01.** Sin mirar el material, explica cómo se relacionan «Objetos residentes espaciales», «Calidad de datos SSA» y «Reporte de evento orbital», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R22-M02 · Seguimiento de objetos orbitales

1. **Observaciones de rastreo** — [`B74-C01`](../programa/clases/B74/B74-C01-modelos-de-observacion/CLASE.md), [`B74-C02`](../programa/clases/B74/B74-C02-observacion-angular-y-astrometria/CLASE.md), [`B74-C03`](../programa/clases/B74/B74-C03-medicion-de-alcance-por-radio/CLASE.md), [`B74-C04`](../programa/clases/B74/B74-C04-doppler-de-navegacion/CLASE.md), [`B89-C15`](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md)
2. **Órbitas preliminares** — [`B74-C06`](../programa/clases/B74/B74-C06-determinacion-inicial-de-orbita/CLASE.md)
3. **Estimación de estados** — [`B74-C07`](../programa/clases/B74/B74-C07-ajuste-por-minimos-cuadrados/CLASE.md), [`B74-C08`](../programa/clases/B74/B74-C08-filtrado-recursivo-de-estados/CLASE.md), [`B74-C09`](../programa/clases/B74/B74-C09-filtro-de-kalman-extendido/CLASE.md)
4. **Catálogos TLE/OMM** — [`B74-C29`](../programa/clases/B74/B74-C29-formatos-tle-y-omm-de-elementos-orbitales/CLASE.md)
5. **Propagación SGP4** — [`B72-C21`](../programa/clases/B72/B72-C21-propagador-sgp4-y-teoria-general-de-perturbaciones/CLASE.md)
6. **Covarianza de seguimiento** — [`B74-C11`](../programa/clases/B74/B74-C11-matrices-de-covarianza-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md), [`B74-C12`](../programa/clases/B74/B74-C12-propagacion-de-incertidumbre-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md)
7. **Asociación de objetos** — [`B74-C30`](../programa/clases/B74/B74-C30-asociacion-de-observaciones-y-correlacion-de-pistas/CLASE.md)
8. **Diferencias entre propagadores** — [`B72-C20`](../programa/clases/B72/B72-C20-comparacion-de-propagadores-de-fidelidad-distinta/CLASE.md)
9. **Validación con efemérides** — [`B74-C20`](../programa/clases/B74/B74-C20-validacion-frente-a-efemerides-de-referencia/CLASE.md)
10. **Informe de precisión de seguimiento** — [`B74-C19`](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md)

✅ **Checkpoint R22-M02.** Sin mirar el material, explica cómo se relacionan «Observaciones de rastreo», «Covarianza de seguimiento» y «Informe de precisión de seguimiento», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R22-M03 · Riesgo de conjunciones y colisiones

1. **Detección de conjunciones** — [`B118-C05`](../programa/clases/B118/B118-C05-conjunciones-orbitales/CLASE.md)
2. **Distancia de aproximación** — [`B118-C05`](../programa/clases/B118/B118-C05-conjunciones-orbitales/CLASE.md), [`B76-C11`](../programa/clases/B76/B76-C11-operaciones-de-aproximacion/CLASE.md)
3. **Incertidumbre de posición** — [`B74-C11`](../programa/clases/B74/B74-C11-matrices-de-covarianza-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md), [`B118-C08`](../programa/clases/B118/B118-C08-propagacion-de-incertidumbre-en-conjunciones/CLASE.md)
4. **Probabilidad de colisión** — [`B118-C06`](../programa/clases/B118/B118-C06-probabilidad-de-colision/CLASE.md)
5. **Ventanas de maniobra** — [`B118-C07`](../programa/clases/B118/B118-C07-estrategias-de-evasion/CLASE.md), [`B76-C14`](../programa/clases/B76/B76-C14-evasion-de-colision/CLASE.md)
6. **Restricciones operativas** — [`B118-C07`](../programa/clases/B118/B118-C07-estrategias-de-evasion/CLASE.md), [`B96-C04`](../programa/clases/B96/B96-C04-planificacion-de-contactos/CLASE.md)
7. **Evaluación de alertas** — [`B118-C20`](../programa/clases/B118/B118-C20-evaluacion-de-riesgo-de-conjuncion-documentada/CLASE.md), [`B118-C05`](../programa/clases/B118/B118-C05-conjunciones-orbitales/CLASE.md)
8. **Decisión documentada** — [`B118-C20`](../programa/clases/B118/B118-C20-evaluacion-de-riesgo-de-conjuncion-documentada/CLASE.md)
9. **Postanálisis de conjunción** — [`B96-C19`](../programa/clases/B96/B96-C19-lecciones-aprendidas-operativas/CLASE.md), [`B118-C20`](../programa/clases/B118/B118-C20-evaluacion-de-riesgo-de-conjuncion-documentada/CLASE.md)
10. **Simulacro de respuesta a alerta** — [`B119-C20`](../programa/clases/B119/B119-C20-simulacion-de-respuesta-institucional-a-incidentes/CLASE.md), [`B118-C20`](../programa/clases/B118/B118-C20-evaluacion-de-riesgo-de-conjuncion-documentada/CLASE.md)

✅ **Checkpoint R22-M03.** Sin mirar el material, explica cómo se relacionan «Detección de conjunciones», «Restricciones operativas» y «Simulacro de respuesta a alerta», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R22-M04 · Mitigación de desechos espaciales

1. **Fragmentación orbital** — [`B118-C09`](../programa/clases/B118/B118-C09-generacion-de-desechos/CLASE.md), [`B118-C10`](../programa/clases/B118/B118-C10-sindrome-de-kessler-como-escenario/CLASE.md)
2. **Entorno de residuos** — [`B118-C01`](../programa/clases/B118/B118-C01-poblacion-de-objetos-orbitales/CLASE.md), [`B118-C09`](../programa/clases/B118/B118-C09-generacion-de-desechos/CLASE.md), [`B118-C10`](../programa/clases/B118/B118-C10-sindrome-de-kessler-como-escenario/CLASE.md)
3. **Diseño para desorbitación** — [`B118-C11`](../programa/clases/B118/B118-C11-diseno-para-mitigacion-de-desechos/CLASE.md), [`B118-C13`](../programa/clases/B118/B118-C13-desorbitacion-controlada/CLASE.md)
4. **Pasivación al fin de vida** — [`B118-C11`](../programa/clases/B118/B118-C11-diseno-para-mitigacion-de-desechos/CLASE.md), [`B118-C12`](../programa/clases/B118/B118-C12-disposicion-al-fin-de-vida/CLASE.md)
5. **Reentrada no controlada** — [`B118-C14`](../programa/clases/B118/B118-C14-reentrada-y-riesgos-en-superficie/CLASE.md), [`B77-C14`](../programa/clases/B77/B77-C14-dinamica-de-reentrada/CLASE.md)
6. **Seguimiento de fragmentos** — [`B118-C03`](../programa/clases/B118/B118-C03-deteccion-y-seguimiento-optico/CLASE.md), [`B118-C04`](../programa/clases/B118/B118-C04-deteccion-por-radar/CLASE.md), [`B118-C15`](../programa/clases/B118/B118-C15-seguimiento-de-mega-constelaciones/CLASE.md)
7. **Prevención de colisiones** — [`B118-C07`](../programa/clases/B118/B118-C07-estrategias-de-evasion/CLASE.md), [`B76-C14`](../programa/clases/B76/B76-C14-evasion-de-colision/CLASE.md)
8. **Medición de sostenibilidad** — [`B118-C19`](../programa/clases/B118/B118-C19-sostenibilidad-y-gobernanza-orbital/CLASE.md), [`B118-C18`](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md)
9. **Normas de mitigación** — [`B118-C24`](../programa/clases/B118/B118-C24-directrices-tecnicas-de-mitigacion-de-desechos-iadc-iso-24113/CLASE.md)
10. **Evaluación de plan de fin de vida** — [`B118-C12`](../programa/clases/B118/B118-C12-disposicion-al-fin-de-vida/CLASE.md), [`B118-C13`](../programa/clases/B118/B118-C13-desorbitacion-controlada/CLASE.md)

✅ **Checkpoint R22-M04.** Sin mirar el material, explica cómo se relacionan «Fragmentación orbital», «Seguimiento de fragmentos» y «Evaluación de plan de fin de vida», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R22-M05 · Seguridad de infraestructura crítica espacial

1. **Segmentos críticos de sistema** — [`B119-C16`](../programa/clases/B119/B119-C16-proteccion-de-infraestructura-critica/CLASE.md), [`B96-C01`](../programa/clases/B96/B96-C01-segmento-espacial-y-segmento-terrestre/CLASE.md)
2. **Amenazas de disponibilidad** — [`B119-C14`](../programa/clases/B119/B119-C14-amenazas-ciberneticas-a-satelites/CLASE.md), [`B119-C15`](../programa/clases/B119/B119-C15-interferencias-y-resiliencia-de-comunicaciones/CLASE.md)
3. **Pérdidas de comunicación** — [`B119-C15`](../programa/clases/B119/B119-C15-interferencias-y-resiliencia-de-comunicaciones/CLASE.md), [`B89-C20`](../programa/clases/B89/B89-C20-diseno-de-red-de-comunicaciones-de-mision/CLASE.md)
4. **Fallos de energía** — [`B86-C11`](../programa/clases/B86/B86-C11-redundancia-electrica/CLASE.md), [`B96-C12`](../programa/clases/B96/B96-C12-gestion-de-energia-en-operaciones/CLASE.md), [`B86-C13`](../programa/clases/B86/B86-C13-energia-durante-eclipse/CLASE.md)
5. **Dependencias de proveedores** — [`B122-C01`](../programa/clases/B122/B122-C01-dependencias-de-proveedores-y-cadena-de-suministro-de-infraestructura-espacial/CLASE.md)
6. **Respaldo de estaciones** — [`B96-C17`](../programa/clases/B96/B96-C17-coordinacion-de-multiples-estaciones/CLASE.md), [`B89-C14`](../programa/clases/B89/B89-C14-estaciones-terrestres/CLASE.md)
7. **Gestión de incidentes** — [`B96-C15`](../programa/clases/B96/B96-C15-operaciones-de-emergencia/CLASE.md), [`B119-C20`](../programa/clases/B119/B119-C20-simulacion-de-respuesta-institucional-a-incidentes/CLASE.md)
8. **Monitoreo de integridad** — [`B96-C13`](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md), [`B88-C12`](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md)
9. **Continuidad de servicio** — [`B122-C02`](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md)
10. **Modelo defensivo de riesgos** — [`B122-C03`](../programa/clases/B122/B122-C03-modelo-defensivo-de-riesgos-de-infraestructura-espacial/CLASE.md)

✅ **Checkpoint R22-M05.** Sin mirar el material, explica cómo se relacionan «Segmentos críticos de sistema», «Respaldo de estaciones» y «Modelo defensivo de riesgos», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R22-M06 · Ciberdefensa y continuidad satelital

1. **Modelo de amenazas satelital** — [`B119-C14`](../programa/clases/B119/B119-C14-amenazas-ciberneticas-a-satelites/CLASE.md), [`B88-C17`](../programa/clases/B88/B88-C17-ciberseguridad-de-avionica/CLASE.md)
2. **Seguridad de estaciones terrestres** — [`B122-C04`](../programa/clases/B122/B122-C04-seguridad-de-estaciones-terrestres-y-segmento-de-control/CLASE.md)
3. **Autenticación de telecomandos** — [`B96-C07`](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md), [`B89-C12`](../programa/clases/B89/B89-C12-telecomandos-ccsds/CLASE.md)
4. **Cifrado de enlaces** — [`B89-C25`](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md)
5. **Control de accesos** — [`B122-C05`](../programa/clases/B122/B122-C05-control-de-accesos-y-gestion-de-identidades-en-operaciones/CLASE.md)
6. **Inventario y parches** — [`B88-C13`](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md), [`B88-C18`](../programa/clases/B88/B88-C18-control-de-configuracion-de-firmware/CLASE.md), [`B83-C15`](../programa/clases/B83/B83-C15-gestion-de-configuracion/CLASE.md)
7. **Detección de anomalías** — [`B96-C13`](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md), [`B88-C12`](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md)
8. **Respuesta a incidentes** — [`B122-C06`](../programa/clases/B122/B122-C06-respuesta-a-incidentes-ciberneticos-en-operaciones-de-mision/CLASE.md)
9. **Recuperación segura** — [`B96-C14`](../programa/clases/B96/B96-C14-procedimientos-de-recuperacion/CLASE.md), [`B88-C11`](../programa/clases/B88/B88-C11-watchdogs-y-recuperacion/CLASE.md), [`B88-C13`](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md)
10. **Ejercicio de defensa controlada** — [`B88-C19`](../programa/clases/B88/B88-C19-simulacion-hardware-in-the-loop/CLASE.md), [`B119-C20`](../programa/clases/B119/B119-C20-simulacion-de-respuesta-institucional-a-incidentes/CLASE.md)

✅ **Checkpoint R22-M06.** Sin mirar el material, explica cómo se relacionan «Modelo de amenazas satelital», «Inventario y parches» y «Ejercicio de defensa controlada», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R22-M07 · Geopolítica y doctrina espacial

1. **Historia de seguridad espacial** — [`B119-C12`](../programa/clases/B119/B119-C12-historia-de-competencia-estrategica-espacial/CLASE.md), [`B02-C19`](../programa/clases/B02/B02-C19-historia-de-la-exploracion-espacial/CLASE.md)
2. **Doctrinas declaradas públicamente** — [`B119-C26`](../programa/clases/B119/B119-C26-doctrinas-y-politicas-espaciales-declaradas-publicamente/CLASE.md)
3. **Tratados y restricciones** — [`B119-C01`](../programa/clases/B119/B119-C01-tratado-del-espacio-ultraterrestre/CLASE.md), [`B119-C11`](../programa/clases/B119/B119-C11-uso-pacifico-y-limitaciones-militares/CLASE.md)
4. **Protección de servicios duales** — [`B119-C16`](../programa/clases/B119/B119-C16-proteccion-de-infraestructura-critica/CLASE.md), [`B119-C11`](../programa/clases/B119/B119-C11-uso-pacifico-y-limitaciones-militares/CLASE.md)
5. **Diplomacia de incidentes** — [`B119-C27`](../programa/clases/B119/B119-C27-diplomacia-y-comunicacion-entre-estados-ante-incidentes-espaciales/CLASE.md)
6. **Normas de conducta responsable** — [`B119-C28`](../programa/clases/B119/B119-C28-normas-de-comportamiento-responsable-en-el-espacio/CLASE.md)
7. **Escalada y desescalada** — [`B119-C29`](../programa/clases/B119/B119-C29-escalada-desescalada-y-medidas-de-fomento-de-la-confianza/CLASE.md)
8. **Desinformación y atribución** — [`B119-C30`](../programa/clases/B119/B119-C30-atribucion-de-incidentes-y-desinformacion-en-el-dominio-espacial/CLASE.md)
9. **Ética de decisiones** — [`B119-C18`](../programa/clases/B119/B119-C18-etica-y-derechos-en-actividades-espaciales/CLASE.md)
10. **Análisis comparado de políticas** — [`B119-C19`](../programa/clases/B119/B119-C19-legislacion-comparada-y-casos-nacionales/CLASE.md)

✅ **Checkpoint R22-M07.** Sin mirar el material, explica cómo se relacionan «Historia de seguridad espacial», «Normas de conducta responsable» y «Análisis comparado de políticas», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R22-M08 · Gestión institucional de crisis espaciales

1. **Detección de crisis** — [`B96-C13`](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md), [`B119-C13`](../programa/clases/B119/B119-C13-vigilancia-y-conciencia-situacional-espacial/CLASE.md)
2. **Clasificación de impacto** — [`B122-C07`](../programa/clases/B122/B122-C07-clasificacion-de-severidad-e-impacto-de-incidentes-espaciales/CLASE.md)
3. **Roles institucionales** — [`B96-C03`](../programa/clases/B96/B96-C03-roles-de-control-de-mision/CLASE.md), [`B119-C06`](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md), [`B119-C08`](../programa/clases/B119/B119-C08-autorizacion-y-supervision-de-operadores/CLASE.md)
4. **Comunicaciones de crisis** — [`B122-C08`](../programa/clases/B122/B122-C08-comunicacion-de-crisis-con-operadores-autoridades-y-publico/CLASE.md)
5. **Coordinación internacional** — [`B119-C06`](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md), [`B118-C18`](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md)
6. **Preservación de evidencias** — [`B122-C09`](../programa/clases/B122/B122-C09-preservacion-de-evidencias-y-cadena-de-custodia-de-datos-de-incidentes/CLASE.md)
7. **Continuidad de servicios** — [`B122-C10`](../programa/clases/B122/B122-C10-planes-de-continuidad-institucional-y-de-operaciones/CLASE.md)
8. **Planes de recuperación** — [`B96-C14`](../programa/clases/B96/B96-C14-procedimientos-de-recuperacion/CLASE.md), [`B96-C19`](../programa/clases/B96/B96-C19-lecciones-aprendidas-operativas/CLASE.md)
9. **Simulacro de mesa** — [`B119-C20`](../programa/clases/B119/B119-C20-simulacion-de-respuesta-institucional-a-incidentes/CLASE.md), [`B104-C09`](../programa/clases/B104/B104-C09-entrenamiento-en-simuladores/CLASE.md)
10. **Informe posterior al incidente** — [`B96-C19`](../programa/clases/B96/B96-C19-lecciones-aprendidas-operativas/CLASE.md), [`B118-C20`](../programa/clases/B118/B118-C20-evaluacion-de-riesgo-de-conjuncion-documentada/CLASE.md)

✅ **Checkpoint R22-M08.** Sin mirar el material, explica cómo se relacionan «Detección de crisis», «Preservación de evidencias» y «Informe posterior al incidente», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

**🎯 Proyecto final · Evaluación de riesgo de conjunciones y plan de resiliencia.** Con datos públicos de objetos orbitales, evalúa el riesgo de conjunción de un satélite y diseña su plan de continuidad ante colisión o ciberataque.

Entregables:

- Cálculo de acercamientos y probabilidad de colisión con incertidumbre
- Criterios de maniobra de evasión con su costo
- Análisis de amenazas cibernéticas de la misión
- Plan de continuidad y de gestión de crisis

Criterios de evaluación:

- La incertidumbre orbital se incorpora al riesgo
- Los umbrales de maniobra están justificados
- El plan de continuidad tiene responsables y tiempos
- Las conclusiones no exigen información restringida

**🏁 Criterio de salida.** Has terminado la ruta cuando:

- Puedes evaluar el riesgo orbital y decidir una maniobra con criterios explícitos.
- Puedes analizar amenazas y diseñar continuidad de operaciones.
- Puedes explicar el entorno de seguridad espacial sin sobrepasar lo público.

<!-- /recorrido -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es un **expediente de seguridad y resiliencia** (educativo, sobre sistemas propios o simulados):

- informe de precisión de seguimiento comparado con efemérides de referencia;
- una decisión de conjunción documentada, con su postanálisis;
- plan de fin de vida evaluado contra una norma citada con versión y fecha;
- modelo defensivo de riesgos de una infraestructura, con objetivos de recuperación;
- informe posterior a un simulacro de crisis o incidente simulado.

Las clases del programa cierran con ejercicios y proyectos que alimentan ese expediente (por ejemplo, la evaluación de riesgo de conjunción documentada de B118 y la simulación de respuesta institucional de B119). Guarda la primera versión, la retroalimentación y los cambios.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional única verificada. Las referencias de trabajo que sí se consultaron (2026-11-05) son:

- 📘 **NIST IR 8401** — *Satellite Ground Segment: Applying the Cybersecurity Framework to Satellite Command and Control*. La noticia de publicación indica fecha 03/01/2023, que el perfil aplica el Marco de Ciberseguridad al segmento terrestre de comando y control de satélites y que apoya los objetivos de la Space Policy Directive 5. Solo se consultó la noticia, **no el texto completo**. (https://csrc.nist.gov/news/2023/nist-releases-nist-ir-8401)
- 📗 **NASA Orbital Debris Program Office — «Orbital Debris Mitigation»** — indica que NASA emitió directrices de mitigación en 1995, que existe NASA-STD-8719.14, que NPR 8715.6E rige desde el 18/04/2024 y que las prácticas estándar del gobierno de EE. UU. se actualizaron en 2019. (https://orbitaldebris.jsc.nasa.gov/mitigation/)

Las directrices del IADC y las de largo plazo de la ONU no se pudieron abrir y no se citan. Las normas y la regulación dependen de la jurisdicción y de la versión vigente: consúltalas en su fuente oficial con fecha antes de aplicarlas.

## 📈 Progresión del rol

Rutas habituales: **análisis de datos de seguimiento → riesgo de conjunciones y desechos → infraestructura y gestión de crisis**. Desde ahí se abren la vigilancia espacial civil, la sostenibilidad orbital y la gestión de continuidad. El avance se demuestra con evidencia. No se publican aquí cifras salariales ni de mercado: no se pudieron verificar con fuentes.

Roles vecinos con los que se comparte formación: [telecomunicaciones y estaciones terrestres](telecomunicaciones-y-estaciones-terrestres-espaciales.md), [aviónica y software de alta fiabilidad](avionica-y-software-espacial-de-alta-fiabilidad.md) y [derecho, políticas y negocios espaciales](derecho-politicas-y-negocios-espaciales.md).

## ⚠️ Mitos y errores comunes

- **«Es ciberseguridad con satélites.»** Los tiempos, los activos y los marcos son distintos; aplicar sin más un perfil terrestre falla donde un satélite no se reinicia.
- **«Una probabilidad de colisión alta ordena maniobrar.»** Depende de la incertidumbre del seguimiento y de lo que cuesta maniobrar; por eso se documenta cada decisión.
- **«Los desechos son un problema del futuro.»** La mitigación se diseña desde el inicio de la misión, con plan de fin de vida.
- **«El dato de vigilancia es la verdad.»** Tiene cobertura, sesgos y latencia; conocer sus límites es parte del oficio.
- **«Se atribuye un incidente de inmediato.»** Hecho y atribución se separan; atribuir mal escala crisis.
- **«Si cumple la norma, es resiliente.»** La norma fija un mínimo; la continuidad se demuestra con simulacros y recuperación.

## 🚀 Siguientes pasos

1. **Asienta la base** con [**B71** · Mecánica orbital fundamental](../programa/tronco-comun/B71-mecanica-orbital-fundamental.md) y probabilidad e incertidumbre.
2. Aprende la **estimación y el seguimiento** con [**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md).
3. Recorre **tráfico y sostenibilidad** en [**B118** · Tráfico espacial y sostenibilidad orbital](../programa/tronco-comun/B118-trafico-espacial-y-sostenibilidad-orbital.md) y documenta una evaluación de conjunción.
4. Estudia el **marco y la doctrina** en [**B119** · Derecho, seguridad y geopolítica espacial](../programa/tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md), con fuentes públicas.
5. Cierra con la **resiliencia** en [**B122** · Resiliencia y continuidad de infraestructura espacial](../programa/tronco-comun/B122-resiliencia-y-continuidad-de-infraestructura-espacial.md) y reúne tu expediente con un informe de simulacro.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Telecomunicaciones y estaciones terrestres espaciales](telecomunicaciones-y-estaciones-terrestres-espaciales.md) · [Aviónica y software espacial de alta fiabilidad](avionica-y-software-espacial-de-alta-fiabilidad.md) · [Derecho políticas y negocios espaciales](derecho-politicas-y-negocios-espaciales.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R22-seguridad-defensa-y-resiliencia-de-infraestructuras-espaciales/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
