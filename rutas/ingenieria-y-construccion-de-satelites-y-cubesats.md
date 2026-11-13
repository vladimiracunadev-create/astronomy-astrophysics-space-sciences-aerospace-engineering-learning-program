# 🛠️ Ingeniería y construcción de satélites y CubeSats

> Diseñas, integras y calificas un satélite pequeño: conviertes una necesidad de misión en requisitos, repartes masa, energía y datos entre subsistemas, y demuestras con ensayos que el conjunto cumple lo que prometiste.
>
> **Nivel de entrada:** base sólida de matemática, física y programación; sin ella el rol se queda corto · **Foco:** requisitos, presupuestos, subsistemas, interfaces, integración y calificación · **Entrega:** presupuestos de misión con márgenes, especificaciones de interfaz, un modelo de diseño trazable a requisitos y el expediente de integración y ensayos.

## 🧭 Qué es y por qué importa

Un satélite no es un objeto: es un **sistema de subsistemas acoplados**. La potencia que generan los paneles decide cuánto puede transmitir la radio; la radio y la carga útil deciden cuántos datos hay que guardar; la actitud decide hacia dónde apuntan paneles y antenas; y todo eso cabe, o no, en la masa y el volumen del bus. Cambiar una decisión en un subsistema mueve las demás. El trabajo de este rol es **mantener coherente ese conjunto**.

Un **CubeSat** es un satélite pequeño construido sobre un formato estándar por unidades. Ese formato abarata y acelera el desarrollo, y por eso hay equipos universitarios, empresas jóvenes y agencias que lo usan; pero no elimina la ingeniería: reduce el margen de error. Con poca masa, poca potencia y poco volumen, cada decisión se paga en otro lado.

En la práctica el rol se reparte en tres miradas que conviene conocer antes de elegir:

- **Ingeniería de sistemas.** Traduce la necesidad de misión en requisitos verificables, reparte los presupuestos de masa, energía y datos, define la arquitectura y las interfaces, y gobierna la configuración y los riesgos. Su pregunta es: *¿el conjunto cumple, y cómo lo demuestro?*
- **Ingeniería de subsistema.** Diseña y verifica una parte: potencia, actitud, comunicaciones, térmica, estructura o aviónica. Su pregunta es: *¿esta parte cumple su presupuesto y su interfaz?*
- **Integración y calificación.** Ensambla, prueba y deja la evidencia: pruebas funcionales, vibración, vacío térmico, compatibilidad electromagnética y trazabilidad. Su pregunta es: *¿qué prueba demuestra cada requisito?*

Muchas carreras empiezan en un subsistema y se abren hacia sistemas o integración; otras hacen el camino inverso. Este programa te hace recorrer las tres miradas para que elijas con conocimiento.

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es armar un kit.** Existen plataformas y componentes comerciales, y se integran; pero el rol decide qué plataforma, qué margen y qué prueba, y responde por el resultado. Elegir un componente sin comprender su interfaz y su riesgo es el error más caro del oficio.
- **No es la ingeniería de la misión científica.** Quien define qué se observa y por qué trabaja con la comunidad científica ([Ingeniería óptica](ingenieria-optica-y-telescopios-profesionales.md), [Astrofísica](astrofisica-estelar-y-galactica.md)); tú traduces esa necesidad a un satélite que la pueda cumplir.
- **No es operaciones.** Operar el satélite en órbita, planificar contactos y recuperar anomalías es otro oficio (bloque de operaciones de misión); tú entregas el satélite, su documentación y sus procedimientos.
- **No es el especialista de un solo subsistema.** [Aviónica y software](avionica-y-software-espacial-de-alta-fiabilidad.md), [materiales, estructuras y térmica](materiales-estructuras-e-ingenieria-termica-espacial.md) y [telecomunicaciones](telecomunicaciones-y-estaciones-terrestres-espaciales.md) profundizan cada parte; este rol las integra y arbitra entre ellas.
- **No es una certificación de vuelo.** Lo que enseña este programa es educativo: no sustituye las normas ni los procesos del proveedor de lanzamiento ni de la autoridad correspondiente (ver *Referencias profesionales*).

## 🗓️ Un día en el puesto

No hay un día típico, pero el trabajo se reparte entre estas actividades:

- **Revisión de requisitos y presupuestos.** Cambia un componente, un proveedor o una necesidad; recalculas masa, energía y datos y verificas que los márgenes sigan siendo aceptables. Lo que no está en un presupuesto no existe para el diseño.
- **Trabajo de subsistema o de modelo.** Un balance de potencia durante el eclipse, un modelo térmico por nodos, una simulación de actitud o un presupuesto de enlace: números que se comparan con el requisito.
- **Reunión de interfaces.** Dos subsistemas discrepan sobre un conector, un bus o un protocolo. Se resuelve por escrito, en el documento de control de interfaz, no de palabra.
- **Integración y pruebas.** Preparas un procedimiento, ejecutas una prueba funcional, registras resultados y gestionas lo que salió mal. Una anomalía bien documentada vale más que una prueba perfecta sin registro.
- **Trazabilidad y riesgos.** Mantienes al día qué requisito se verifica con qué prueba, qué riesgo sigue abierto y qué cambió desde la última revisión.

Dicho sin adornos: hay **mucha documentación** y **muchas decisiones de compromiso**. La habilidad no es dominar un subsistema, sino saber cuánto margen guardar y a quién pedírselo.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Ingeniería de sistemas:** necesidad de misión, concepto de operaciones, requisitos verificables, trazabilidad, presupuestos, revisiones de diseño, riesgos y gestión de configuración.
- **Órbita y entorno:** qué órbita cumple la misión, cuántos eclipses tiene, qué perturbaciones sufre y cómo afectan al diseño.
- **Potencia y térmica:** balance de energía, paneles y baterías, y el equilibrio térmico de un cuerpo en el vacío.
- **Actitud y control:** sensores, actuadores, orientación y el lazo de control que mantiene el satélite apuntando.
- **Comunicaciones:** presupuesto de enlace, bandas, modulación y estación terrena.
- **Aviónica y software de vuelo:** arquitectura del computador, buses, tolerancia a fallos y verificación.
- **Estructuras, materiales y ensayos:** cargas de lanzamiento, vibración, vacío térmico, compatibilidad electromagnética y calificación.
- **Incertidumbre:** propagar errores y justificar un margen con números, no con intuición.

### Herramientas del oficio

```text
Cálculo y simulación:   Python (NumPy, SciPy), hojas de cálculo para presupuestos
Modelado de sistemas:   modelos de requisitos y arquitectura (MBSE), matrices de trazabilidad
Modelado de subsistemas: balance de potencia, modelo térmico por nodos, simulación de actitud
Documentación:          documentos de control de interfaz, planes y procedimientos de prueba
Control de cambios:     control de versiones y de configuración
```

Ninguna herramienta decide por ti. Un modelo bien hecho con datos de entrada equivocados da una respuesta equivocada con aspecto serio; lo que se paga es tu criterio para comprobarlo.

### Habilidades no técnicas

- **Comunicación entre disciplinas:** explicarle a quien diseña la radio por qué necesitas diez gramos menos.
- **Rigor documental:** si no está escrito y trazado, no ocurrió.
- **Negociación de márgenes:** repartir un presupuesto escaso sin que cada subsistema se lo quede todo.
- **Gestión de la incertidumbre y del riesgo:** decir «no lo sé todavía» con un plan para saberlo.

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md) — A02 · 20 clases
2. 📚 [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) — A02 · 20 clases
3. 📚 [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) — A02 · 26 clases
4. 📚 [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) — A02 · 26 clases
5. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — A02 · 31 clases
6. 📚 [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) — A02 · 24 clases
7. 📚 [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) — A02 · 20 clases

### 🎯 El núcleo del rol

**A02 · Matemática, física computacional y métodos científicos**

1. 📚 [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) — usa 1 de 23 clases: `B13-` C05

**A04 · Óptica, telescopios y observatorios científicos**

2. 📚 [**B44** · Detectores y adquisición astronómica](../programa/tronco-comun/B44-detectores-y-adquisicion-astronomica.md) — usa 5 de 20 clases: `B44-` C02–C04, C06, C17
3. 📚 [**B46** · Radioastronomía e interferometría](../programa/tronco-comun/B46-radioastronomia-e-interferometria.md) — usa 2 de 20 clases: `B46-` C06–C07
4. 📚 [**B47** · Instrumentación y observatorios espaciales](../programa/tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md) — usa 5 de 25 clases: `B47-` C02, C15–C16, C18, C25

**A06 · Mecánica orbital, navegación y vuelo espacial**

5. 📚 [**B71** · Mecánica orbital fundamental](../programa/tronco-comun/B71-mecanica-orbital-fundamental.md) — usa 2 de 20 clases: `B71-` C07–C08

**A07 · Ingeniería y construcción de sistemas espaciales**

6. 📚 [**B83** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) — usa 12 de 24 clases: `B83-` C01, C04–C05, C07–C11, C13–C15, C23
7. 📚 [**B84** · Estructuras, materiales y fabricación espacial](../programa/tronco-comun/B84-estructuras-materiales-y-fabricacion-espacial.md) — usa 2 de 38 clases: `B84-` C13, C20
8. 📚 [**B85** · Gestión térmica y entorno espacial](../programa/tronco-comun/B85-gestion-termica-y-entorno-espacial.md) — usa 5 de 29 clases: `B85-` C01, C18–C20, C23
9. 📚 [**B86** · Sistemas de potencia y energía espacial](../programa/tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md) — usa 15 de 23 clases: `B86-` C01–C10, C12–C13, C19–C21
10. 📚 [**B87** · Sensores y control de actitud](../programa/tronco-comun/B87-sensores-y-control-de-actitud.md) — usa 15 de 22 clases: `B87-` C01–C07, C11–C12, C15–C16, C18–C20, C22
11. 📚 [**B88** · Aviónica y software crítico espacial](../programa/tronco-comun/B88-avionica-y-software-critico-espacial.md) — usa 6 de 44 clases: `B88-` C07–C08, C11–C12, C18, C21
12. 📚 [**B89** · Comunicaciones y navegación satelital](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) — usa 12 de 25 clases: `B89-` C03, C05–C06, C08–C09, C11–C15, C17, C19
13. 📚 [**B90** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) — usa 17 de 24 clases: `B90-` C01–C03, C05–C10, C12–C14, C16–C20
14. 📚 [**B95** · Plataformas de satélites pequeños y CubeSat](../programa/tronco-comun/B95-plataformas-de-satelites-pequenos-y-cubesat.md) — usa 4 de 4 clases: `B95-` C01–C04

**A08 · Operaciones de misión y robótica espacial**

15. 📚 [**B96** · Control y operación de misiones espaciales](../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) — usa 3 de 30 clases: `B96-` C04, C06, C16

**A10 · Entorno orbital, derecho y seguridad espacial**

16. 📚 [**B119** · Derecho, seguridad y geopolítica espacial](../programa/tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md) — usa 1 de 36 clases: `B119-` C09

<!-- /ruta -->

<!-- recorrido:inicio -->
### 🗺️ Recorrido módulo por módulo

El rol se estudia en **8 módulos** de 10 temas cada uno (cada tema es un par «concepto + aplicación»). Haz el diagnóstico, avanza por los módulos **en orden** y cierra cada uno con su checkpoint; al final, el proyecto y el criterio de salida.

**🩺 Diagnóstico de entrada.** Si respondes «no sé» a dos o más, empieza por los fundamentos de arriba:

- ¿Puedes hacer un presupuesto de masa y de energía de un sistema sencillo?
- ¿Sabes qué es un presupuesto de enlace?
- ¿Entiendes la estabilización por giro y por ruedas?
- ¿Puedes leer un diagrama de bloques de ingeniería?

#### R12-M01 · Arquitectura de misión satelital

1. **Objetivo del satélite** — [`B83-C01`](../programa/clases/B83/B83-C01-necesidad-de-mision-y-caso-cientifico/CLASE.md)
2. **Requisitos de servicio** — [`B83-C04`](../programa/clases/B83/B83-C04-requisitos-verificables/CLASE.md)
3. **Órbita y cobertura** — [`B71-C07`](../programa/clases/B71/B71-C07-orbitas-circulares/CLASE.md), [`B71-C08`](../programa/clases/B71/B71-C08-orbitas-elipticas/CLASE.md), [`B89-C17`](../programa/clases/B89/B89-C17-constelaciones-y-cobertura/CLASE.md)
4. **Presupuesto de masa** — [`B83-C09`](../programa/clases/B83/B83-C09-presupuestos-de-masa/CLASE.md)
5. **Presupuesto de energía** — [`B83-C10`](../programa/clases/B83/B83-C10-presupuestos-de-energia/CLASE.md)
6. **Presupuesto de datos** — [`B83-C11`](../programa/clases/B83/B83-C11-presupuestos-de-datos/CLASE.md)
7. **Arquitectura de plataforma** — [`B83-C07`](../programa/clases/B83/B83-C07-arquitecturas-de-sistemas/CLASE.md)
8. **Cargas útiles compatibles** — [`B83-C08`](../programa/clases/B83/B83-C08-interfaz-entre-subsistemas/CLASE.md)
9. **Redundancia de misión** — [`B83-C23`](../programa/clases/B83/B83-C23-redundancia-y-tolerancia-a-fallos-de-mision/CLASE.md)
10. **Revisión conceptual de diseño** — [`B83-C13`](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md)

✅ **Checkpoint R12-M01.** Sin mirar el material, explica cómo se relacionan «Objetivo del satélite», «Presupuesto de datos» y «Revisión conceptual de diseño», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R12-M02 · Diseño de cargas útiles

1. **Objetivos de carga útil** — [`B47-C02`](../programa/clases/B47/B47-C02-requisitos-de-instrumentos-orbitales/CLASE.md)
2. **Sensores ópticos** — [`B44-C02`](../programa/clases/B44/B44-C02-sensores-ccd/CLASE.md), [`B44-C03`](../programa/clases/B44/B44-C03-sensores-cmos/CLASE.md)
3. **Sensores de radio** — [`B46-C06`](../programa/clases/B46/B46-C06-ruido-de-sistema-y-radiometria/CLASE.md), [`B46-C07`](../programa/clases/B46/B46-C07-receptores-superheterodinos/CLASE.md)
4. **Dosímetros** — [`B85-C23`](../programa/clases/B85/B85-C23-dosimetros-y-monitores-de-radiacion-a-bordo/CLASE.md)
5. **Carga útil educativa** — [`B47-C25`](../programa/clases/B47/B47-C25-diseno-de-cargas-utiles-educativas/CLASE.md)
6. **Resolución y sensibilidad** — [`B44-C04`](../programa/clases/B44/B44-C04-eficiencia-cuantica-espectral/CLASE.md), [`B44-C06`](../programa/clases/B44/B44-C06-ruido-de-lectura/CLASE.md), [`B44-C17`](../programa/clases/B44/B44-C17-escala-de-imagen-y-muestreo/CLASE.md)
7. **Masa y energía de instrumento** — [`B83-C09`](../programa/clases/B83/B83-C09-presupuestos-de-masa/CLASE.md), [`B83-C10`](../programa/clases/B83/B83-C10-presupuestos-de-energia/CLASE.md), [`B85-C20`](../programa/clases/B85/B85-C20-presupuesto-termico-de-carga-util/CLASE.md)
8. **Calibración de carga útil** — [`B47-C15`](../programa/clases/B47/B47-C15-calibracion-a-bordo/CLASE.md), [`B13-C05`](../programa/clases/B13/B13-C05-calibracion-instrumental/CLASE.md)
9. **Flujo de datos científicos** — [`B47-C16`](../programa/clases/B47/B47-C16-compresion-de-datos-cientificos/CLASE.md), [`B47-C18`](../programa/clases/B47/B47-C18-downlink-de-instrumentos-cientificos/CLASE.md), [`B96-C16`](../programa/clases/B96/B96-C16-gestion-de-datos-cientificos/CLASE.md)
10. **Aceptación de carga útil** — [`B90-C19`](../programa/clases/B90/B90-C19-aceptacion-de-unidades-de-vuelo/CLASE.md)

✅ **Checkpoint R12-M02.** Sin mirar el material, explica cómo se relacionan «Objetivos de carga útil», «Resolución y sensibilidad» y «Aceptación de carga útil», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R12-M03 · Plataformas y buses satelitales

1. **CubeSat Unit y dimensiones** — [`B95-C01`](../programa/clases/B95/B95-C01-unidad-cubesat-dimensiones-y-formatos/CLASE.md)
2. **Plataforma estructural** — [`B84-C20`](../programa/clases/B84/B84-C20-diseno-estructural-de-plataforma-satelital/CLASE.md)
3. **Arquitectura de buses** — [`B83-C07`](../programa/clases/B83/B83-C07-arquitecturas-de-sistemas/CLASE.md), [`B88-C07`](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md)
4. **Mecanismos y desplegables** — [`B84-C13`](../programa/clases/B84/B84-C13-mecanismos-desplegables/CLASE.md)
5. **Paneles de interfaces** — [`B90-C05`](../programa/clases/B90/B90-C05-documentacion-de-interfaces/CLASE.md)
6. **Componentes comerciales** — [`B95-C02`](../programa/clases/B95/B95-C02-componentes-comerciales-en-vuelo-seleccion-y-riesgo/CLASE.md)
7. **Compatibilidad electromagnética** — [`B90-C13`](../programa/clases/B90/B90-C13-compatibilidad-electromagnetica-emc/CLASE.md), [`B90-C14`](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md)
8. **Diseño térmico de plataforma** — [`B85-C01`](../programa/clases/B85/B85-C01-balance-radiativo-de-satelite/CLASE.md), [`B85-C18`](../programa/clases/B85/B85-C18-modelado-termico-por-nodos/CLASE.md)
9. **Análisis de compatibilidad** — [`B83-C08`](../programa/clases/B83/B83-C08-interfaz-entre-subsistemas/CLASE.md)
10. **Selección argumentada de plataforma** — [`B95-C03`](../programa/clases/B95/B95-C03-seleccion-y-comparacion-de-plataformas/CLASE.md)

✅ **Checkpoint R12-M03.** Sin mirar el material, explica cómo se relacionan «CubeSat Unit y dimensiones», «Componentes comerciales» y «Selección argumentada de plataforma», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R12-M04 · Sistema eléctrico de potencia

1. **Generación fotovoltaica** — [`B86-C02`](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md), [`B86-C03`](../programa/clases/B86/B86-C03-arreglos-fotovoltaicos-desplegables/CLASE.md)
2. **Baterías de a bordo** — [`B86-C05`](../programa/clases/B86/B86-C05-baterias-de-ion-litio/CLASE.md), [`B86-C06`](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md)
3. **Regulación de potencia** — [`B86-C08`](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md), [`B86-C09`](../programa/clases/B86/B86-C09-electronica-de-potencia/CLASE.md)
4. **Distribución de buses** — [`B86-C07`](../programa/clases/B86/B86-C07-distribucion-de-potencia/CLASE.md)
5. **Protecciones eléctricas** — [`B86-C10`](../programa/clases/B86/B86-C10-proteccion-contra-sobrecorriente/CLASE.md), [`B90-C03`](../programa/clases/B90/B90-C03-proteccion-frente-a-esd/CLASE.md)
6. **Estados de bajo consumo** — [`B86-C21`](../programa/clases/B86/B86-C21-modos-de-operacion-y-estados-de-bajo-consumo/CLASE.md)
7. **Energía en eclipse** — [`B86-C04`](../programa/clases/B86/B86-C04-orientacion-solar-y-eclipses/CLASE.md), [`B86-C13`](../programa/clases/B86/B86-C13-energia-durante-eclipse/CLASE.md)
8. **Dimensionamiento de arreglos** — [`B86-C01`](../programa/clases/B86/B86-C01-balance-de-potencia-electrica/CLASE.md), [`B86-C19`](../programa/clases/B86/B86-C19-presupuesto-de-potencia-de-mision/CLASE.md)
9. **Márgenes de potencia** — [`B86-C12`](../programa/clases/B86/B86-C12-eficiencia-y-disipacion/CLASE.md)
10. **Prueba de ciclo eléctrico** — [`B86-C20`](../programa/clases/B86/B86-C20-simulacion-de-ciclo-energetico-orbital/CLASE.md), [`B90-C16`](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md)

✅ **Checkpoint R12-M04.** Sin mirar el material, explica cómo se relacionan «Generación fotovoltaica», «Estados de bajo consumo» y «Prueba de ciclo eléctrico», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R12-M05 · Sistema de comunicaciones satelitales

1. **Antenas de CubeSat** — [`B95-C04`](../programa/clases/B95/B95-C04-antenas-desplegables-para-satelites-pequenos/CLASE.md)
2. **Presupuesto de enlace** — [`B89-C05`](../programa/clases/B89/B89-C05-presupuesto-de-enlace/CLASE.md), [`B89-C06`](../programa/clases/B89/B89-C06-ganancias-y-perdidas-de-antena/CLASE.md)
3. **Radio TT&C** — [`B89-C11`](../programa/clases/B89/B89-C11-telemetria-ccsds/CLASE.md), [`B89-C12`](../programa/clases/B89/B89-C12-telecomandos-ccsds/CLASE.md)
4. **Bandas autorizadas** — [`B89-C03`](../programa/clases/B89/B89-C03-bandas-vhf-uhf-s-x-ka/CLASE.md), [`B89-C19`](../programa/clases/B89/B89-C19-coordinacion-del-espectro-ante-itu/CLASE.md), [`B119-C09`](../programa/clases/B119/B119-C09-derecho-y-normas-de-telecomunicaciones/CLASE.md)
5. **Codificación de datos** — [`B89-C08`](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md), [`B89-C09`](../programa/clases/B89/B89-C09-codificacion-correctora-de-errores/CLASE.md)
6. **Protocolo de comunicación** — [`B89-C13`](../programa/clases/B89/B89-C13-protocolos-para-espacio-profundo/CLASE.md)
7. **Estación terrestre** — [`B89-C14`](../programa/clases/B89/B89-C14-estaciones-terrestres/CLASE.md)
8. **Gestión de telemetría** — [`B88-C08`](../programa/clases/B88/B88-C08-telemetria-interna/CLASE.md), [`B96-C06`](../programa/clases/B96/B96-C06-telemetria-operativa/CLASE.md)
9. **Análisis de contactos** — [`B89-C15`](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md), [`B96-C04`](../programa/clases/B96/B96-C04-planificacion-de-contactos/CLASE.md)
10. **Prueba de enlace extremo a extremo** — [`B90-C16`](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md)

✅ **Checkpoint R12-M05.** Sin mirar el material, explica cómo se relacionan «Antenas de CubeSat», «Protocolo de comunicación» y «Prueba de enlace extremo a extremo», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R12-M06 · Sistema de determinación y control de actitud

1. **Sensores de actitud** — [`B87-C03`](../programa/clases/B87/B87-C03-sensores-solares/CLASE.md), [`B87-C04`](../programa/clases/B87/B87-C04-sensores-terrestres/CLASE.md), [`B87-C05`](../programa/clases/B87/B87-C05-magnetometros/CLASE.md), [`B87-C06`](../programa/clases/B87/B87-C06-giroscopios-mems/CLASE.md), [`B87-C07`](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md)
2. **Dinámica rotacional** — [`B87-C01`](../programa/clases/B87/B87-C01-dinamica-de-cuerpo-rigido/CLASE.md), [`B87-C02`](../programa/clases/B87/B87-C02-representaciones-de-orientacion/CLASE.md)
3. **Detumbling** — [`B87-C16`](../programa/clases/B87/B87-C16-detumbling-despues-del-despliegue/CLASE.md)
4. **Ruedas de reacción** — [`B87-C11`](../programa/clases/B87/B87-C11-ruedas-de-reaccion/CLASE.md)
5. **Magnetopares** — [`B87-C12`](../programa/clases/B87/B87-C12-magnetopares/CLASE.md)
6. **Control de apuntamiento** — [`B87-C15`](../programa/clases/B87/B87-C15-apuntamiento-de-alta-precision/CLASE.md)
7. **Perturbaciones orbitales** — [`B87-C18`](../programa/clases/B87/B87-C18-estabilidad-ante-perturbaciones/CLASE.md)
8. **Presupuesto de error** — [`B87-C22`](../programa/clases/B87/B87-C22-presupuesto-de-error-de-apuntamiento/CLASE.md)
9. **Modos seguros** — [`B88-C11`](../programa/clases/B88/B88-C11-watchdogs-y-recuperacion/CLASE.md), [`B88-C12`](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md)
10. **Prueba de controlador ADCS** — [`B87-C19`](../programa/clases/B87/B87-C19-verificacion-de-ley-de-control/CLASE.md), [`B87-C20`](../programa/clases/B87/B87-C20-simulacion-adcs-integral/CLASE.md)

✅ **Checkpoint R12-M06.** Sin mirar el material, explica cómo se relacionan «Sensores de actitud», «Control de apuntamiento» y «Prueba de controlador ADCS», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R12-M07 · Ingeniería de interfaces y configuración

1. **Documentos de control de interfaces** — [`B90-C05`](../programa/clases/B90/B90-C05-documentacion-de-interfaces/CLASE.md), [`B83-C08`](../programa/clases/B83/B83-C08-interfaz-entre-subsistemas/CLASE.md)
2. **Matriz de requisitos** — [`B83-C04`](../programa/clases/B83/B83-C04-requisitos-verificables/CLASE.md), [`B83-C05`](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md)
3. **Control de configuración** — [`B83-C15`](../programa/clases/B83/B83-C15-gestion-de-configuracion/CLASE.md), [`B88-C18`](../programa/clases/B88/B88-C18-control-de-configuracion-de-firmware/CLASE.md)
4. **Gestión de masas** — [`B83-C09`](../programa/clases/B83/B83-C09-presupuestos-de-masa/CLASE.md)
5. **Gestión térmica** — [`B85-C20`](../programa/clases/B85/B85-C20-presupuesto-termico-de-carga-util/CLASE.md), [`B85-C18`](../programa/clases/B85/B85-C18-modelado-termico-por-nodos/CLASE.md)
6. **Interfaces mecánicas** — [`B90-C06`](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md)
7. **Interfaces eléctricas** — [`B90-C07`](../programa/clases/B90/B90-C07-integracion-electrica-de-buses/CLASE.md)
8. **Interfaces de software** — [`B88-C21`](../programa/clases/B88/B88-C21-interfaces-y-documentos-de-control-de-software-de-vuelo/CLASE.md)
9. **Gestión de cambios** — [`B83-C15`](../programa/clases/B83/B83-C15-gestion-de-configuracion/CLASE.md)
10. **Revisión de coherencia integral** — [`B83-C14`](../programa/clases/B83/B83-C14-revisiones-cdr-y-trr/CLASE.md)

✅ **Checkpoint R12-M07.** Sin mirar el material, explica cómo se relacionan «Documentos de control de interfaces», «Interfaces mecánicas» y «Revisión de coherencia integral», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R12-M08 · Integración y calificación de CubeSat

1. **Plan de ensamblaje** — [`B90-C01`](../programa/clases/B90/B90-C01-plan-de-ensamblaje-e-integracion/CLASE.md)
2. **Procedimientos de integración** — [`B90-C06`](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md), [`B90-C07`](../programa/clases/B90/B90-C07-integracion-electrica-de-buses/CLASE.md), [`B90-C08`](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md)
3. **Control ESD** — [`B90-C02`](../programa/clases/B90/B90-C02-buenas-practicas-de-sala-limpia/CLASE.md), [`B90-C03`](../programa/clases/B90/B90-C03-proteccion-frente-a-esd/CLASE.md)
4. **Pruebas de subsistemas** — [`B90-C08`](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md)
5. **Pruebas funcionales** — [`B90-C16`](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md)
6. **Vibración y choque** — [`B90-C09`](../programa/clases/B90/B90-C09-ensayos-de-vibracion/CLASE.md), [`B90-C10`](../programa/clases/B90/B90-C10-ensayos-de-choque/CLASE.md)
7. **Vacío térmico** — [`B90-C12`](../programa/clases/B90/B90-C12-vacio-termico-y-ciclos/CLASE.md), [`B85-C19`](../programa/clases/B85/B85-C19-ensayos-de-vacio-termico/CLASE.md)
8. **Trazabilidad de evidencia** — [`B90-C18`](../programa/clases/B90/B90-C18-trazabilidad-de-evidencias/CLASE.md)
9. **Resolución de no conformidades** — [`B90-C17`](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md)
10. **Revisión de aceptación de CubeSat** — [`B90-C19`](../programa/clases/B90/B90-C19-aceptacion-de-unidades-de-vuelo/CLASE.md), [`B90-C20`](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md)

✅ **Checkpoint R12-M08.** Sin mirar el material, explica cómo se relacionan «Plan de ensamblaje», «Vibración y choque» y «Revisión de aceptación de CubeSat», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

**🎯 Proyecto final · Diseño preliminar de un CubeSat de observación.** Diseña un CubeSat 3U para una misión de observación: arquitectura, presupuestos y plan de integración y pruebas, con revisión de diseño preliminar.

Entregables:

- Concepto de misión y requisitos verificables
- Presupuestos de masa, energía, datos y enlace
- Arquitectura de bus con interfaces
- Plan de integración, calificación y operación

Criterios de evaluación:

- Cada requisito tiene un método de verificación
- Los presupuestos tienen margen y reserva
- Las interfaces están documentadas con unidades
- El plan contempla fallos y pruebas ambientales

**🏁 Criterio de salida.** Has terminado la ruta cuando:

- Puedes llevar una misión satelital pequeña desde el requisito hasta un diseño preliminar revisable.
- Puedes dimensionar los subsistemas principales de un satélite.
- Puedes planear su integración y calificación.

<!-- /recorrido -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es un **expediente de diseño de un CubeSat** (educativo, no de vuelo):

- presupuestos de masa, energía y datos con márgenes y su propagación de incertidumbre;
- arquitectura, interfaces entre subsistemas y matriz de requisitos con su verificación;
- balance de potencia del ciclo orbital, modelo térmico y simulación de actitud;
- presupuesto de enlace y plan de contactos;
- plan de integración y de ensayos, con criterios de aceptación y gestión de anomalías.

Las clases del programa cierran con ejercicios, laboratorios y proyectos que alimentan ese expediente (por ejemplo, el diseño preliminar completo de misión y la campaña conceptual de calificación de un CubeSat). Guarda la primera versión, la retroalimentación y los cambios: el portafolio con su historia pesa más que un documento final impecable.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional única verificada. Las referencias de trabajo que sí se consultaron (2026-11-05) son:

- 📘 **NASA Systems Engineering Handbook** — página de la NASA, actualizada el 27 de marzo de 2024, con seis capítulos: introducción, fundamentos, ciclo de vida de programas y proyectos, procesos de diseño, realización del producto y gestión técnica transversal. Es la referencia de método para la mirada de sistemas. (https://www.nasa.gov/reference/systems-engineering-handbook/)
- 📗 **State-of-the-Art of Small Spacecraft Technology** — informe anual de la NASA, edición 2026, con un capítulo por subsistema (potencia, propulsión, guía y control, térmica, aviónica, comunicaciones, desorbitación) y por plataforma, lanzamiento, despliegue y operaciones en tierra. Útil para conocer el estado de la tecnología; la propia NASA aclara que no es un panorama exhaustivo. (https://www.nasa.gov/smallsat-institute/sst-soa/)

Las normas de ingeniería espacial, los requisitos del proveedor de lanzamiento y la regulación aplicable dependen de la jurisdicción y de la versión vigente, y **no están verificados aquí**: antes de usar cualquiera en un proyecto real, consúltala en su fuente oficial.

## 📈 Progresión del rol

Rutas habituales: **ingeniero/a de subsistema → ingeniero/a de sistemas → líder de integración y ensayos o de proyecto**. Desde sistemas se abren la gestión de proyectos espaciales y la ingeniería de misión; desde integración, la calificación y el aseguramiento del producto. No se publican aquí cifras salariales: varían demasiado por país, empresa y sector y no se pudieron verificar con fuentes.

Roles vecinos con los que se comparte formación: [aviónica y software](avionica-y-software-espacial-de-alta-fiabilidad.md), [materiales, estructuras y térmica](materiales-estructuras-e-ingenieria-termica-espacial.md) y [telecomunicaciones](telecomunicaciones-y-estaciones-terrestres-espaciales.md).

## ⚠️ Mitos y errores comunes

- **«Un CubeSat es un juguete.»** Es un satélite con el mismo tipo de problemas, con menos margen. Los fallos de integración y de interfaz son la causa más común de que un proyecto pequeño no llegue a funcionar.
- **«Si cabe en la masa, cabe en el diseño.»** La masa es un presupuesto más. La energía, los datos, la térmica y la actitud también cierran, o no.
- **«Los ensayos son burocracia.»** Son la única evidencia de que el satélite cumple lo que prometiste. Se diseñan desde el requisito, no al final.
- **«El software lo arregla después.»** El software de vuelo tiene presupuestos y verificación propios; no corrige un subsistema mal dimensionado.
- **«Mi subsistema está bien, el problema es de otro.»** En un sistema acoplado, el problema suele estar en la interfaz.

## 🚀 Siguientes pasos

1. **Asienta la base** con el área A01 y, según tu diagnóstico, con matemática, física y programación.
2. Recorre el **núcleo de ingeniería de sistemas** ([**B83** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md)) y arma un presupuesto de masa, energía y datos para un satélite de ejemplo.
3. Profundiza un subsistema a elección y cierra su presupuesto: [**B86** · Sistemas de potencia y energía espacial](../programa/tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md) (potencia), [**B87** · Sensores y control de actitud](../programa/tronco-comun/B87-sensores-y-control-de-actitud.md) (actitud), [**B89** · Comunicaciones y navegación satelital](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) (comunicaciones) o [**B85** · Gestión térmica y entorno espacial](../programa/tronco-comun/B85-gestion-termica-y-entorno-espacial.md) (térmica).
4. Practica la **integración y los ensayos** con [**B90** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) y escribe un plan de calificación con criterios de aceptación.
5. Reúne tu **expediente** y guarda su historia: primera versión, retroalimentación y cambios.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Aviónica y software espacial de alta fiabilidad](avionica-y-software-espacial-de-alta-fiabilidad.md) · [Materiales estructuras e ingeniería térmica espacial](materiales-estructuras-e-ingenieria-termica-espacial.md) · [Telecomunicaciones y estaciones terrestres espaciales](telecomunicaciones-y-estaciones-terrestres-espaciales.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R12-ingenieria-y-construccion-de-satelites-y-cubesats/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
