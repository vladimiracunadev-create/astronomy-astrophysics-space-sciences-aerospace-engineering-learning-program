# R20 — Guía del rol: arquitectura y hábitats extraterrestres

> Esta guía describe un rol de trabajo para decidir si es el tuyo. No es una promesa de empleo, habilitación ni título, y no sustituye a un profesional habilitado ni a la norma vigente. El recorrido concreto de clases está en [RECORRIDO.md](RECORRIDO.md).

## Qué es

Quien ocupa este rol diseña el lugar donde personas viven y trabajan fuera de la Tierra: un módulo presurizado en órbita, un hábitat lunar o una base marciana. Su unidad de trabajo es el **recinto habitable**: cuánta atmósfera contiene, cuánta agua y alimento necesita, cuánta energía consume, qué lo protege de la radiación y cómo se mueven las personas dentro cuando algo falla. El trabajo es de síntesis: junta balances de masa y energía con decisiones de distribución, de factores humanos y de riesgo.

## Qué NO es (y con quién se confunde)

- **No es ingeniería de satélites.** El satélite no se ocupa de personas; el hábitat sí. Un satélite se califica por su misión; un hábitat, por si mantiene vivas y en condiciones de trabajar a quienes lo ocupan. El rol de [R12](../R12-ingenieria-y-construccion-de-satelites-y-cubesats/INDICE.md) comparte la ingeniería de sistemas, no el objeto.
- **No es medicina espacial.** Se usan sus resultados como requisitos (sueño, hueso, radiación); la salud de las personas la atiende la ruta de [R19](../R19-medicina-y-bioingenieria-espacial/INDICE.md).
- **No es astronáutica tripulada.** Esa ruta ([R18](../R18-astronautica-tripulada-y-entrenamiento-de-astronautas/INDICE.md)) entrena y opera a la tripulación; aquí se diseña el entorno donde opera.
- **No es arquitectura civil con otro paisaje.** El aire, el agua y el calor se cuentan como masas y vatios; no basta con el aspecto ni con la forma.

## Un día de trabajo

Una jornada típica mezcla cuatro actividades. Se revisa el balance de masa de la semana (¿cuánta agua se recupera y cuánto se pierde?) y se actualiza su incertidumbre. Se trabaja un plano: dónde cabe el módulo de higiene sin cruzar la ruta de evacuación. Se discute con quien diseña estructuras o energía una interfaz o un presupuesto. Y se escribe: un requisito, una justificación, una matriz de riesgos. Casi todo es contraste entre un cálculo y una decisión de diseño.

## Qué decide y qué entrega

Decide qué disposición y qué sistemas de soporte vital cumplen los requisitos dentro de los presupuestos de masa, energía y riesgo, y si una amenaza se resuelve con redundancia, con blindaje o con un cambio de arquitectura. Entrega requisitos de habitabilidad trazables, planos de distribución, balances de aire, agua, alimento y energía con incertidumbre, una matriz de riesgo ambiental y un diseño integral revisado. Las entregas están descritas en `metadatos/recorridos/R20.json`.

## Conocimientos y herramientas

Fundamentos de física, química y matemática de balances; ingeniería de sistemas (requisitos, presupuestos); soporte vital y control de atmósfera; energía y térmica; radiación y clima espacial; y factores humanos. Las herramientas son hojas de cálculo o código con unidades y pruebas, modelos de balance y herramientas de dibujo. Qué herramienta concreta usa un equipo depende del equipo; la guía no prescribe productos.

## Evidencias y portafolio

El portafolio ideal contiene: un balance de aire y agua de una tripulación con incertidumbre declarada; un plano con rutas de evacuación justificadas; una matriz de riesgo ambiental; y un diseño integral (el módulo R20-M08) con revisión final. Cada pieza declara sus supuestos, sus fuentes y su versión.

## Progresión

Se empieza por un subsistema (un balance, un plano, un cálculo de blindaje) y se crece hacia la integración de varios. El rol puede derivar hacia soporte vital especializado, hacia estructuras presurizadas o hacia el diseño de misión. El orden y el peso de las clases están en el recorrido; no se avanza por acumulación sino por evidencia.

## Límites éticos y de seguridad

Un hábitat protege vidas: ninguna decisión de seguridad se aprueba por promedio, y una falla crítica detiene el diseño. Los resultados de este programa son educativos; un diseño real requiere normas vigentes, revisión de profesionales habilitados y pruebas. También deben tratarse la contaminación planetaria y el impacto ambiental, y el consentimiento de las personas que participarían en un análogo o en un ensayo (ver [Seguridad y ética profesional](../../../documentacion/SEGURIDAD_Y_ETICA_PROFESIONAL.md)).

## Fuentes consultadas

- NASA, *NASA Spaceflight Human-System Standard, Volume 2: Human Factors, Habitability, and Environmental Health* (NASA-STD-3001 Vol. 2), ficha en [standards.nasa.gov/node/237](https://standards.nasa.gov/node/237). Consultada el 05/11/2026. La ficha indica la revisión F (fecha 14/07/2026), estado activo, y que es un estándar «endorsed» y no obligatorio de la agencia. Solo se consultó la ficha, no el texto completo de los requisitos.

No se consultaron otras fuentes para esta guía. Otras referencias de la ruta (por ejemplo el *Human Integration Design Handbook* de NASA) no se pudieron abrir en esta sesión y no se citan.
