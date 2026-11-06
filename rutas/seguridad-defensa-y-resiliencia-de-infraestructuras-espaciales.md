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
