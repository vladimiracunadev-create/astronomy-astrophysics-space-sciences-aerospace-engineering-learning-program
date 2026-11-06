# 💾 Aviónica y software espacial de alta fiabilidad

> Escribes y verificas el software y la electrónica que controlan un vehículo espacial, donde una falla no se arregla en el sitio y cada defecto debe haberse evitado o contenido de antemano.
>
> **Nivel de entrada:** programación y electrónica de nivel universitario o experiencia equivalente; rol técnico de ingeniería · **Foco:** software de vuelo, sistemas de tiempo real, tolerancia a fallas, electrónica embarcada, pruebas y verificación · **Entrega:** un software o una arquitectura de vuelo con su plan de verificación, su manejo de fallas y la evidencia de sus pruebas

## 🧭 Qué es y por qué importa

El computador de un satélite funciona en un ambiente que no se puede visitar: radiación que corrompe bits, temperaturas extremas, energía limitada y comunicación intermitente. Por eso el software de vuelo se escribe con una prioridad distinta de la habitual: **que nada falle sin que el sistema lo detecte y se recupere**.

El rol combina programación de tiempo real, arquitectura de computadores y electrónica. Se trabaja con reglas de codificación estrictas, revisión formal y pruebas que cubren no solo el funcionamiento normal sino cada modo de falla previsto.

Las miradas del rol son:

- **Software de vuelo.** Tareas, planificación, manejo de errores. Su pregunta es: *¿qué hace el sistema cuando algo sale mal?*
- **Electrónica embarcada.** Radiación, compatibilidad electromagnética, potencia. Su pregunta es: *¿qué le pasa al circuito en el ambiente real?*
- **Verificación.** Pruebas, trazabilidad, simulación. Su pregunta es: *¿qué evidencia demuestra que cumple el requisito?*

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es desarrollo de aplicaciones.** Las restricciones de memoria, tiempo y fiabilidad cambian cómo se programa.
- **No es navegación y guiado.** Aquí se construye la plataforma donde esos algoritmos corren ([Navegación guiado y autonomía espacial](navegacion-guiado-y-autonomia-espacial.md)).
- **No es ingeniería de satélites completa.** Es un subsistema que debe integrarse con los demás ([Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md)).
- **No es ciberseguridad.** Se solapan en algunos riesgos, pero el foco aquí es la fiabilidad y la tolerancia a fallas.

## 🗓️ Un día en el puesto

- **Requisitos:** trazas cada requisito a código y a una prueba.
- **Implementación:** escribes y revisas código bajo reglas estrictas.
- **Pruebas:** corres pruebas unitarias, de integración y con hardware simulado.
- **Fallas:** inyectas fallas y verificas que el sistema se recupere.
- **Revisión:** discutes con el equipo cada hallazgo y su corrección.

Dicho sin adornos: **la mayor parte del trabajo es probar lo que no debería ocurrir**.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Aviónica y software crítico espacial** ([**B54** · Aviónica y software crítico espacial](../programa/tronco-comun/B54-avionica-y-software-critico-espacial.md)).
- **Electrónica embarcada y compatibilidad electromagnética** ([**B101** · Electrónica embarcada y compatibilidad electromagnética](../PROGRAMA_ACADEMICO_COMPLETO.md#b101--electrónica-embarcada-y-compatibilidad-electromagnética)).
- **Ingeniería de sistemas** ([**B49** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md)); **integración, ensayos y calificación** ([**B56** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md)).
- **Verificación y validación de software** ([**B71** · Verificación y validación de software científico](../PROGRAMA_ACADEMICO_COMPLETO.md#b71--verificación-y-validación-de-software-científico)).
- **Sensores y control de actitud** ([**B53** · Sensores y control de actitud](../programa/tronco-comun/B53-sensores-y-control-de-actitud.md)).
- **Computación científica** ([**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md)) y **resiliencia de infraestructura espacial** ([**B123** · Resiliencia y continuidad de infraestructura espacial](../PROGRAMA_ACADEMICO_COMPLETO.md#b123--resiliencia-y-continuidad-de-infraestructura-espacial)).

### Herramientas del oficio

```text
Lenguajes:            un lenguaje de sistemas para el software de vuelo
Pruebas:              marcos de prueba automatizada y simuladores de hardware
Análisis:             análisis estático y revisión formal de código
Trazabilidad:         gestión de requisitos y de evidencia
Control de versiones: Git con revisión obligatoria
```

Una herramienta no sustituye al criterio: un análisis estático limpio no prueba que el requisito sea el correcto.

### Habilidades no técnicas

- **Disciplina y atención al detalle.**
- **Comunicación con ingeniería de sistemas y con operaciones.**
- **Documentación rigurosa.**
- **Aceptar la revisión crítica del propio código.**

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B07** · Informática científica desde cero](../programa/tronco-comun/B07-informatica-cientifica-desde-cero.md) — A01 · 20 clases
2. 📚 [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) — A02 · 24 clases
3. 📚 [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) — A02 · 20 clases
4. 📚 [**B50** · Estructuras, materiales y fabricación espacial](../programa/tronco-comun/B50-estructuras-materiales-y-fabricacion-espacial.md) — A07 · 38 clases
5. 📚 [**B51** · Gestión térmica y entorno espacial](../programa/tronco-comun/B51-gestion-termica-y-entorno-espacial.md) — A07 · 29 clases
6. 📚 [**B53** · Sensores y control de actitud](../programa/tronco-comun/B53-sensores-y-control-de-actitud.md) — A07 · 22 clases

### 🎯 El núcleo del rol

**A02 · Matemática, física computacional y métodos científicos**

1. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — usa 1 de 31 clases: `B14-` C10

**A04 · Óptica, telescopios y observatorios científicos**

2. 📚 [**B31** · Instrumentación y observatorios espaciales](../programa/tronco-comun/B31-instrumentacion-y-observatorios-espaciales.md) — usa 1 de 25 clases: `B31-` C14

**A06 · Mecánica orbital, navegación y vuelo espacial**

3. 📚 [**B44** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B44-estimacion-de-orbitas-y-navegacion-espacial.md) — usa 1 de 30 clases: `B44-` C16

**A07 · Ingeniería y construcción de sistemas espaciales**

4. 📚 [**B49** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md) — usa 6 de 24 clases: `B49-` C04–C05, C14, C17, C22, C24
5. 📚 [**B52** · Sistemas de potencia y energía espacial](../programa/tronco-comun/B52-sistemas-de-potencia-y-energia-espacial.md) — usa 4 de 23 clases: `B52-` C07–C09, C11
6. 📚 [**B54** · Aviónica y software crítico espacial](../programa/tronco-comun/B54-avionica-y-software-critico-espacial.md) — usa 41 de 44 clases: `B54-` C01–C17, C19–C20, C22–C43
7. 📚 [**B55** · Comunicaciones y navegación satelital](../programa/tronco-comun/B55-comunicaciones-y-navegacion-satelital.md) — usa 2 de 25 clases: `B55-` C09, C11
8. 📚 [**B56** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md) — usa 8 de 24 clases: `B56-` C05, C07–C08, C13–C14, C16, C18–C19
9. 📚 [**B101** · Electrónica embarcada y compatibilidad electromagnética](../PROGRAMA_ACADEMICO_COMPLETO.md#b101--electrónica-embarcada-y-compatibilidad-electromagnética) — usa 4 de 4 clases: `B101-` C01–C04

**A08 · Operaciones de misión y robótica espacial**

10. 📚 [**B57** · Control y operación de misiones espaciales](../programa/tronco-comun/B57-control-y-operacion-de-misiones-espaciales.md) — usa 6 de 30 clases: `B57-` C06, C08, C13–C15, C21

<!-- /ruta -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es un **software de vuelo con evidencia de verificación**:

- un conjunto pequeño de requisitos trazables;
- un software de tiempo real que los cumple;
- pruebas que incluyen inyección de fallas;
- una matriz de trazabilidad entre requisito, código y prueba;
- el entorno para repetir todo.

Los bloques de la ruta aportan ejercicios y laboratorios; guarda la primera versión y sus cambios.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional verificada, y para esta guía no se consultó una fuente externa específica (2026-11-05). Por eso no se citan normas, requisitos de acceso ni cifras: cuando se necesiten, deben consultarse en la fuente oficial vigente de la institución, agencia o empresa correspondiente.

## 📈 Progresión del rol

Rutas habituales: **desarrollador/a de software embarcado → responsable de un subsistema de software de vuelo → liderazgo técnico de aviónica o de software crítico**. Se abren la ingeniería de sistemas y la verificación independiente. No se publican cifras salariales por no poder verificarlas.

Roles vecinos con los que se comparte formación: [Navegación guiado y autonomía espacial](navegacion-guiado-y-autonomia-espacial.md), [Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md) y [Telecomunicaciones y estaciones terrestres espaciales](telecomunicaciones-y-estaciones-terrestres-espaciales.md).

## ⚠️ Mitos y errores comunes

- **«Si compila y pasa las pruebas, está bien».** Las pruebas solo cubren lo que se pensó probar.
- **«La redundancia garantiza fiabilidad».** Mal diseñada, introduce fallas comunes.
- **«Se puede parchear en órbita».** Depende de la arquitectura; no siempre es posible ni seguro.
- **«El software crítico es lento de escribir por burocracia».** Es lento porque el costo de un defecto es muy alto.
- **«Es solo programación».** Incluye electrónica, ambiente y sistemas.

## 🚀 Siguientes pasos

1. **Asienta la base** con el área A01 (informática científica) y la matemática de tu diagnóstico.
2. Estudia **aviónica y software crítico** ([**B54** · Aviónica y software crítico espacial](../programa/tronco-comun/B54-avionica-y-software-critico-espacial.md)) y **sensores y control de actitud** ([**B53** · Sensores y control de actitud](../programa/tronco-comun/B53-sensores-y-control-de-actitud.md)).
3. Profundiza en **electrónica embarcada** ([**B101** · Electrónica embarcada y compatibilidad electromagnética](../PROGRAMA_ACADEMICO_COMPLETO.md#b101--electrónica-embarcada-y-compatibilidad-electromagnética)) e **ingeniería de sistemas** ([**B49** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B49-ingenieria-de-sistemas-y-diseno-de-misiones.md)).
4. Avanza a **integración y ensayos** ([**B56** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B56-integracion-ensayos-y-calificacion-espacial.md)) y **verificación de software** ([**B71** · Verificación y validación de software científico](../PROGRAMA_ACADEMICO_COMPLETO.md#b71--verificación-y-validación-de-software-científico)).
5. Reúne tu **software con su evidencia** y su historial.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md) · [Robótica espacial y sistemas autónomos](robotica-espacial-y-sistemas-autonomos.md) · [Seguridad defensa y resiliencia de infraestructuras espaciales](seguridad-defensa-y-resiliencia-de-infraestructuras-espaciales.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R13-avionica-y-software-espacial-de-alta-fiabilidad/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
