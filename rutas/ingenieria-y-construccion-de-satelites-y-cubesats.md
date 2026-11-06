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
14. 📚 [**B95** · Plataformas de satélites pequeños y CubeSat](../PROGRAMA_ACADEMICO_COMPLETO.md#b95--plataformas-de-satélites-pequeños-y-cubesat) — usa 4 de 4 clases: `B95-` C01–C04

**A08 · Operaciones de misión y robótica espacial**

15. 📚 [**B96** · Control y operación de misiones espaciales](../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) — usa 3 de 30 clases: `B96-` C04, C06, C16

**A10 · Entorno orbital, derecho y seguridad espacial**

16. 📚 [**B119** · Derecho, seguridad y geopolítica espacial](../programa/tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md) — usa 1 de 36 clases: `B119-` C09

<!-- /ruta -->

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
