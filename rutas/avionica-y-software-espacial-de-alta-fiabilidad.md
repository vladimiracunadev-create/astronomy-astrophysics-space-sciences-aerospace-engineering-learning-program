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

- **Aviónica y software crítico espacial** ([**B88** · Aviónica y software crítico espacial](../programa/tronco-comun/B88-avionica-y-software-critico-espacial.md)).
- **Electrónica embarcada y compatibilidad electromagnética** ([**B93** · Electrónica embarcada y compatibilidad electromagnética](../programa/tronco-comun/B93-electronica-embarcada-y-compatibilidad-electromagnetica.md)).
- **Ingeniería de sistemas** ([**B83** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md)); **integración, ensayos y calificación** ([**B90** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md)).
- **Verificación y validación de software** ([**B23** · Verificación y validación de software científico](../programa/tronco-comun/B23-verificacion-y-validacion-de-software-cientifico.md)).
- **Sensores y control de actitud** ([**B87** · Sensores y control de actitud](../programa/tronco-comun/B87-sensores-y-control-de-actitud.md)).
- **Computación científica** ([**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md)) y **resiliencia de infraestructura espacial** ([**B122** · Resiliencia y continuidad de infraestructura espacial](../programa/tronco-comun/B122-resiliencia-y-continuidad-de-infraestructura-espacial.md)).

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
4. 📚 [**B84** · Estructuras, materiales y fabricación espacial](../programa/tronco-comun/B84-estructuras-materiales-y-fabricacion-espacial.md) — A07 · 38 clases
5. 📚 [**B85** · Gestión térmica y entorno espacial](../programa/tronco-comun/B85-gestion-termica-y-entorno-espacial.md) — A07 · 29 clases
6. 📚 [**B87** · Sensores y control de actitud](../programa/tronco-comun/B87-sensores-y-control-de-actitud.md) — A07 · 22 clases

### 🎯 El núcleo del rol

**A02 · Matemática, física computacional y métodos científicos**

1. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — usa 1 de 31 clases: `B14-` C10

**A04 · Óptica, telescopios y observatorios científicos**

2. 📚 [**B47** · Instrumentación y observatorios espaciales](../programa/tronco-comun/B47-instrumentacion-y-observatorios-espaciales.md) — usa 1 de 25 clases: `B47-` C14

**A06 · Mecánica orbital, navegación y vuelo espacial**

3. 📚 [**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md) — usa 1 de 30 clases: `B74-` C16

**A07 · Ingeniería y construcción de sistemas espaciales**

4. 📚 [**B83** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) — usa 6 de 24 clases: `B83-` C04–C05, C14, C17, C22, C24
5. 📚 [**B86** · Sistemas de potencia y energía espacial](../programa/tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md) — usa 4 de 23 clases: `B86-` C07–C09, C11
6. 📚 [**B88** · Aviónica y software crítico espacial](../programa/tronco-comun/B88-avionica-y-software-critico-espacial.md) — usa 41 de 44 clases: `B88-` C01–C17, C19–C20, C22–C43
7. 📚 [**B89** · Comunicaciones y navegación satelital](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) — usa 2 de 25 clases: `B89-` C09, C11
8. 📚 [**B90** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md) — usa 8 de 24 clases: `B90-` C05, C07–C08, C13–C14, C16, C18–C19
9. 📚 [**B93** · Electrónica embarcada y compatibilidad electromagnética](../programa/tronco-comun/B93-electronica-embarcada-y-compatibilidad-electromagnetica.md) — usa 4 de 4 clases: `B93-` C01–C04

**A08 · Operaciones de misión y robótica espacial**

10. 📚 [**B96** · Control y operación de misiones espaciales](../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) — usa 6 de 30 clases: `B96-` C06, C08, C13–C15, C21

<!-- /ruta -->

<!-- recorrido:inicio -->
### 🗺️ Recorrido módulo por módulo

El rol se estudia en **8 módulos** de 10 temas cada uno (cada tema es un par «concepto + aplicación»). Haz el diagnóstico, avanza por los módulos **en orden** y cierra cada uno con su checkpoint; al final, el proyecto y el criterio de salida.

**🩺 Diagnóstico de entrada.** Si respondes «no sé» a dos o más, empieza por los fundamentos de arriba:

- ¿Sabes diseñar un circuito digital sencillo?
- ¿Conoces el concepto de tiempo real y de prioridad de tareas?
- ¿Escribes código en un lenguaje de sistemas con control de memoria?
- ¿Entiendes qué es una falla y qué es una falla latente?

#### R13-M01 · Electrónica embarcada avanzada

1. **Diseño de PCB espacial conceptual** — [`B93-C01`](../programa/clases/B93/B93-C01-diseno-de-pcb-espacial-conceptual/CLASE.md)
2. **Selección de componentes** — [`B93-C02`](../programa/clases/B93/B93-C02-seleccion-de-componentes-y-derating/CLASE.md)
3. **Compatibilidad eléctrica** — [`B90-C07`](../programa/clases/B90/B90-C07-integracion-electrica-de-buses/CLASE.md), [`B86-C07`](../programa/clases/B86/B86-C07-distribucion-de-potencia/CLASE.md)
4. **Integridad de señal** — [`B93-C03`](../programa/clases/B93/B93-C03-integridad-de-senal-en-electronica-embarcada/CLASE.md)
5. **Conversión de potencia** — [`B86-C08`](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md), [`B86-C09`](../programa/clases/B86/B86-C09-electronica-de-potencia/CLASE.md)
6. **Blindaje EMI** — [`B90-C13`](../programa/clases/B90/B90-C13-compatibilidad-electromagnetica-emc/CLASE.md), [`B90-C14`](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md)
7. **Radiación y electrónica** — [`B88-C03`](../programa/clases/B88/B88-C03-procesadores-tolerantes-a-radiacion/CLASE.md), [`B47-C14`](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md)
8. **Prueba funcional de placas** — [`B90-C08`](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md)
9. **Análisis de confiabilidad** — [`B93-C04`](../programa/clases/B93/B93-C04-analisis-de-confiabilidad-de-electronica-mtbf-y-derating/CLASE.md)
10. **Documentación de electrónica** — [`B90-C05`](../programa/clases/B90/B90-C05-documentacion-de-interfaces/CLASE.md), [`B90-C18`](../programa/clases/B90/B90-C18-trazabilidad-de-evidencias/CLASE.md)

✅ **Checkpoint R13-M01.** Sin mirar el material, explica cómo se relacionan «Diseño de PCB espacial conceptual», «Blindaje EMI» y «Documentación de electrónica», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R13-M02 · Arquitectura de computadores de vuelo

1. **Arquitecturas OBC** — [`B88-C01`](../programa/clases/B88/B88-C01-arquitectura-de-computador-de-vuelo/CLASE.md)
2. **Procesadores y microcontroladores** — [`B88-C02`](../programa/clases/B88/B88-C02-microcontroladores-embarcados/CLASE.md), [`B88-C03`](../programa/clases/B88/B88-C03-procesadores-tolerantes-a-radiacion/CLASE.md)
3. **Memoria ECC** — [`B88-C04`](../programa/clases/B88/B88-C04-memorias-y-correccion-de-errores/CLASE.md)
4. **Interrupciones** — [`B88-C22`](../programa/clases/B88/B88-C22-interrupciones-y-manejo-de-excepciones-en-el-computador-de-vuelo/CLASE.md)
5. **Temporización** — [`B88-C05`](../programa/clases/B88/B88-C05-sistemas-de-tiempo-real/CLASE.md), [`B74-C16`](../programa/clases/B74/B74-C16-sincronizacion-temporal/CLASE.md)
6. **Jerarquía de software** — [`B88-C23`](../programa/clases/B88/B88-C23-arquitectura-de-software-de-vuelo-capas-y-ejecutivo/CLASE.md)
7. **Capas HAL** — [`B88-C24`](../programa/clases/B88/B88-C24-capa-de-abstraccion-de-hardware-hal-y-controladores/CLASE.md)
8. **Redundancia de procesamiento** — [`B88-C25`](../programa/clases/B88/B88-C25-redundancia-de-procesamiento-y-ejecucion-en-paralelo-lockstep/CLASE.md)
9. **Supervisión de computadores** — [`B88-C11`](../programa/clases/B88/B88-C11-watchdogs-y-recuperacion/CLASE.md), [`B88-C12`](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md)
10. **Evaluación de arquitectura** — [`B88-C20`](../programa/clases/B88/B88-C20-plan-de-verificacion-de-computador-de-vuelo/CLASE.md)

✅ **Checkpoint R13-M02.** Sin mirar el material, explica cómo se relacionan «Arquitecturas OBC», «Jerarquía de software» y «Evaluación de arquitectura», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R13-M03 · Sistemas de tiempo real

1. **Planificación de tareas** — [`B88-C06`](../programa/clases/B88/B88-C06-planificacion-de-tareas-rtos/CLASE.md)
2. **Latencia de interrupciones** — [`B88-C26`](../programa/clases/B88/B88-C26-latencia-de-interrupciones-y-jitter/CLASE.md)
3. **RTOS y prioridades** — [`B88-C05`](../programa/clases/B88/B88-C05-sistemas-de-tiempo-real/CLASE.md), [`B88-C06`](../programa/clases/B88/B88-C06-planificacion-de-tareas-rtos/CLASE.md)
4. **Mutex y semáforos** — [`B88-C27`](../programa/clases/B88/B88-C27-exclusion-mutua-y-semaforos/CLASE.md)
5. **Deadlocks** — [`B88-C28`](../programa/clases/B88/B88-C28-inversion-de-prioridad-y-deadlocks/CLASE.md)
6. **Sistemas deterministas** — [`B88-C05`](../programa/clases/B88/B88-C05-sistemas-de-tiempo-real/CLASE.md)
7. **Registro de eventos** — [`B88-C10`](../programa/clases/B88/B88-C10-gestion-de-eventos/CLASE.md), [`B88-C08`](../programa/clases/B88/B88-C08-telemetria-interna/CLASE.md)
8. **Gestión de memoria** — [`B88-C29`](../programa/clases/B88/B88-C29-gestion-de-memoria-determinista-en-software-de-vuelo/CLASE.md)
9. **Pruebas de plazos** — [`B88-C14`](../programa/clases/B88/B88-C14-pruebas-de-software-embarcado/CLASE.md), [`B88-C05`](../programa/clases/B88/B88-C05-sistemas-de-tiempo-real/CLASE.md)
10. **Análisis de peor caso** — [`B88-C30`](../programa/clases/B88/B88-C30-analisis-de-peor-caso-de-tiempo-de-ejecucion-wcet/CLASE.md)

✅ **Checkpoint R13-M03.** Sin mirar el material, explica cómo se relacionan «Planificación de tareas», «Sistemas deterministas» y «Análisis de peor caso», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R13-M04 · Comunicaciones y buses internos

1. **Bus I2C** — [`B88-C07`](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md)
2. **Bus SPI** — [`B88-C07`](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md)
3. **Bus CAN** — [`B88-C07`](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md)
4. **SpaceWire** — [`B88-C07`](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md)
5. **Protocolos de telemetría interna** — [`B88-C08`](../programa/clases/B88/B88-C08-telemetria-interna/CLASE.md), [`B89-C11`](../programa/clases/B89/B89-C11-telemetria-ccsds/CLASE.md)
6. **Topología de red** — [`B88-C31`](../programa/clases/B88/B88-C31-topologias-de-red-de-datos-a-bordo/CLASE.md)
7. **Sincronización de mensajes** — [`B74-C16`](../programa/clases/B74/B74-C16-sincronizacion-temporal/CLASE.md), [`B88-C07`](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md)
8. **Detección de errores de bus** — [`B89-C09`](../programa/clases/B89/B89-C09-codificacion-correctora-de-errores/CLASE.md), [`B88-C07`](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md)
9. **Instrumentación de tráfico** — [`B88-C08`](../programa/clases/B88/B88-C08-telemetria-interna/CLASE.md), [`B88-C19`](../programa/clases/B88/B88-C19-simulacion-hardware-in-the-loop/CLASE.md)
10. **Pruebas de interoperabilidad** — [`B90-C07`](../programa/clases/B90/B90-C07-integracion-electrica-de-buses/CLASE.md), [`B90-C16`](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md)

✅ **Checkpoint R13-M04.** Sin mirar el material, explica cómo se relacionan «Bus I2C», «Topología de red» y «Pruebas de interoperabilidad», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R13-M05 · Tolerancia a fallos de hardware y software

1. **Fallos transitorios** — [`B88-C03`](../programa/clases/B88/B88-C03-procesadores-tolerantes-a-radiacion/CLASE.md), [`B88-C12`](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md), [`B47-C14`](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md)
2. **Fallos permanentes** — [`B88-C12`](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md), [`B86-C11`](../programa/clases/B86/B86-C11-redundancia-electrica/CLASE.md)
3. **ECC y EDAC** — [`B88-C04`](../programa/clases/B88/B88-C04-memorias-y-correccion-de-errores/CLASE.md)
4. **Watchdogs** — [`B88-C11`](../programa/clases/B88/B88-C11-watchdogs-y-recuperacion/CLASE.md)
5. **Modo seguro** — [`B88-C12`](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md), [`B96-C15`](../programa/clases/B96/B96-C15-operaciones-de-emergencia/CLASE.md)
6. **Redundancia fría y caliente** — [`B88-C32`](../programa/clases/B88/B88-C32-redundancia-fria-y-caliente-estrategias-y-conmutacion/CLASE.md)
7. **Votación de sistemas** — [`B88-C33`](../programa/clases/B88/B88-C33-votacion-y-redundancia-modular-triple-tmr/CLASE.md)
8. **Detección FDIR** — [`B88-C12`](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md)
9. **Análisis FMEA** — [`B83-C22`](../programa/clases/B83/B83-C22-analisis-de-modos-y-efectos-de-fallo-fmea-en-sistemas-espaciales/CLASE.md)
10. **Pruebas de inyección de fallos** — [`B88-C34`](../programa/clases/B88/B88-C34-pruebas-de-inyeccion-de-fallos/CLASE.md)

✅ **Checkpoint R13-M05.** Sin mirar el material, explica cómo se relacionan «Fallos transitorios», «Redundancia fría y caliente» y «Pruebas de inyección de fallos», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R13-M06 · Recuperación autónoma de anomalías

1. **Gestión autónoma de estados** — [`B96-C08`](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md), [`B88-C09`](../programa/clases/B88/B88-C09-telecomandos-y-estados-de-mision/CLASE.md)
2. **Árboles de fallos** — [`B83-C24`](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md)
3. **Monitoreo de salud** — [`B88-C08`](../programa/clases/B88/B88-C08-telemetria-interna/CLASE.md), [`B96-C06`](../programa/clases/B96/B96-C06-telemetria-operativa/CLASE.md)
4. **Detección de anomalías** — [`B96-C13`](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md), [`B88-C12`](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md)
5. **Diagnóstico explicable** — [`B96-C21`](../programa/clases/B96/B96-C21-diagnostico-explicable-de-anomalias/CLASE.md)
6. **Recuperación de procesos** — [`B88-C11`](../programa/clases/B88/B88-C11-watchdogs-y-recuperacion/CLASE.md), [`B96-C14`](../programa/clases/B96/B96-C14-procedimientos-de-recuperacion/CLASE.md)
7. **Reinicio y persistencia** — [`B88-C35`](../programa/clases/B88/B88-C35-reinicio-en-caliente-y-persistencia-de-estado/CLASE.md)
8. **Prioridades de supervivencia** — [`B96-C15`](../programa/clases/B96/B96-C15-operaciones-de-emergencia/CLASE.md), [`B96-C08`](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md)
9. **Telemetría de incidentes** — [`B88-C10`](../programa/clases/B88/B88-C10-gestion-de-eventos/CLASE.md), [`B96-C06`](../programa/clases/B96/B96-C06-telemetria-operativa/CLASE.md)
10. **Validación de recuperación** — [`B96-C14`](../programa/clases/B96/B96-C14-procedimientos-de-recuperacion/CLASE.md), [`B88-C14`](../programa/clases/B88/B88-C14-pruebas-de-software-embarcado/CLASE.md)

✅ **Checkpoint R13-M06.** Sin mirar el material, explica cómo se relacionan «Gestión autónoma de estados», «Recuperación de procesos» y «Validación de recuperación», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R13-M07 · Seguridad y aseguramiento del software

1. **Ciclo de vida seguro** — [`B88-C16`](../programa/clases/B88/B88-C16-ingenieria-de-seguridad-funcional/CLASE.md), [`B88-C17`](../programa/clases/B88/B88-C17-ciberseguridad-de-avionica/CLASE.md)
2. **Revisión de requisitos** — [`B83-C04`](../programa/clases/B83/B83-C04-requisitos-verificables/CLASE.md), [`B83-C05`](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md)
3. **Codificación defensiva** — [`B88-C36`](../programa/clases/B88/B88-C36-codificacion-defensiva-y-estandares-de-codigo-seguro/CLASE.md)
4. **Análisis estático** — [`B88-C15`](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md)
5. **Pruebas de fuzzing autorizadas** — [`B88-C37`](../programa/clases/B88/B88-C37-fuzzing-autorizado-de-software-embarcado-en-banco-de-pruebas/CLASE.md)
6. **Firmas de firmware** — [`B88-C13`](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md), [`B88-C17`](../programa/clases/B88/B88-C17-ciberseguridad-de-avionica/CLASE.md)
7. **Gestión de secretos** — [`B88-C38`](../programa/clases/B88/B88-C38-gestion-de-claves-y-secretos-en-avionica/CLASE.md)
8. **Actualización verificada** — [`B88-C13`](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md)
9. **Normas de aseguramiento** — [`B88-C39`](../programa/clases/B88/B88-C39-normas-de-aseguramiento-de-software-ecss-do-178c/CLASE.md)
10. **Auditoría de software espacial** — [`B88-C40`](../programa/clases/B88/B88-C40-auditoria-de-software-espacial/CLASE.md)

✅ **Checkpoint R13-M07.** Sin mirar el material, explica cómo se relacionan «Ciclo de vida seguro», «Firmas de firmware» y «Auditoría de software espacial», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

#### R13-M08 · Verificación integral de aviónica

1. **Plan de pruebas de aviónica** — [`B88-C20`](../programa/clases/B88/B88-C20-plan-de-verificacion-de-computador-de-vuelo/CLASE.md), [`B83-C17`](../programa/clases/B83/B83-C17-verificacion-frente-a-validacion/CLASE.md)
2. **SIL y PIL** — [`B88-C41`](../programa/clases/B88/B88-C41-pruebas-sil-y-pil-del-software-de-vuelo/CLASE.md)
3. **HIL** — [`B88-C19`](../programa/clases/B88/B88-C19-simulacion-hardware-in-the-loop/CLASE.md)
4. **Mocks de sensores** — [`B88-C42`](../programa/clases/B88/B88-C42-simuladores-y-mocks-de-sensores-para-pruebas/CLASE.md)
5. **Simulación de buses** — [`B88-C19`](../programa/clases/B88/B88-C19-simulacion-hardware-in-the-loop/CLASE.md), [`B88-C07`](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md)
6. **Pruebas de cargas** — [`B88-C43`](../programa/clases/B88/B88-C43-pruebas-de-carga-y-estres-del-software-de-vuelo/CLASE.md)
7. **Pruebas de regresión** — [`B14-C10`](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md), [`B88-C14`](../programa/clases/B88/B88-C14-pruebas-de-software-embarcado/CLASE.md)
8. **Matriz de trazabilidad** — [`B83-C05`](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md), [`B90-C18`](../programa/clases/B90/B90-C18-trazabilidad-de-evidencias/CLASE.md)
9. **Resultados de validación** — [`B90-C18`](../programa/clases/B90/B90-C18-trazabilidad-de-evidencias/CLASE.md), [`B90-C16`](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md)
10. **Informe técnico de liberación** — [`B90-C19`](../programa/clases/B90/B90-C19-aceptacion-de-unidades-de-vuelo/CLASE.md), [`B83-C14`](../programa/clases/B83/B83-C14-revisiones-cdr-y-trr/CLASE.md), [`B90-C18`](../programa/clases/B90/B90-C18-trazabilidad-de-evidencias/CLASE.md)

✅ **Checkpoint R13-M08.** Sin mirar el material, explica cómo se relacionan «Plan de pruebas de aviónica», «Pruebas de cargas» y «Informe técnico de liberación», y resuelve un ejercicio de dos de esos temas. Guarda el resultado como evidencia de este módulo.

**🎯 Proyecto final · Software de vuelo tolerante a fallos para un computador de a bordo.** Implementa y verifica un núcleo de software con tareas de tiempo real, vigilancia y recuperación automática, probado con inyección de fallos.

Entregables:

- Arquitectura con tareas, prioridades y plazos
- Mecanismos de vigilancia y recuperación
- Campaña de inyección de fallos con resultados
- Plan de aseguramiento y trazabilidad de requisitos

Criterios de evaluación:

- Los plazos de tiempo real se cumplen en el peor caso
- Cada fallo inyectado se detecta y se recupera o se aísla
- La trazabilidad cubre el 100 % de los requisitos
- Se documentan las reglas de codificación aplicadas

**🏁 Criterio de salida.** Has terminado la ruta cuando:

- Puedes diseñar y verificar software crítico de tiempo real.
- Puedes demostrar tolerancia a fallos con evidencia.
- Puedes aplicar un proceso de aseguramiento a un producto de vuelo.

<!-- /recorrido -->

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
2. Estudia **aviónica y software crítico** ([**B88** · Aviónica y software crítico espacial](../programa/tronco-comun/B88-avionica-y-software-critico-espacial.md)) y **sensores y control de actitud** ([**B87** · Sensores y control de actitud](../programa/tronco-comun/B87-sensores-y-control-de-actitud.md)).
3. Profundiza en **electrónica embarcada** ([**B93** · Electrónica embarcada y compatibilidad electromagnética](../programa/tronco-comun/B93-electronica-embarcada-y-compatibilidad-electromagnetica.md)) e **ingeniería de sistemas** ([**B83** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md)).
4. Avanza a **integración y ensayos** ([**B90** · Integración, ensayos y calificación espacial](../programa/tronco-comun/B90-integracion-ensayos-y-calificacion-espacial.md)) y **verificación de software** ([**B23** · Verificación y validación de software científico](../programa/tronco-comun/B23-verificacion-y-validacion-de-software-cientifico.md)).
5. Reúne tu **software con su evidencia** y su historial.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md) · [Robótica espacial y sistemas autónomos](robotica-espacial-y-sistemas-autonomos.md) · [Seguridad defensa y resiliencia de infraestructuras espaciales](seguridad-defensa-y-resiliencia-de-infraestructuras-espaciales.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R13-avionica-y-software-espacial-de-alta-fiabilidad/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
