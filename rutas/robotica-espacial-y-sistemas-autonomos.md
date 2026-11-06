# 🤖 Robótica espacial y sistemas autónomos

> Haces que una máquina actúe sola, o casi sola, donde nadie puede tocarla: un brazo que agarra una pieza, un rover que cruza terreno suelto, un vehículo que se acerca a otro sin chocar. Y demuestras que, si algo sale mal, se detiene de forma segura.
>
> **Nivel de entrada:** base sólida de álgebra lineal, ecuaciones diferenciales, control y programación; el rol vive de modelos y de simulación · **Foco:** cinemática y dinámica, percepción y localización, control y estimación, autonomía y teleoperación con retardo · **Entrega:** modelos verificables, cadenas de percepción y localización con métricas, arquitecturas de autonomía, pruebas en escenarios adversos y el informe de una misión robótica simulada

## 🧭 Qué es y por qué importa

Una máquina en el espacio no tiene mecánico cerca. La señal tarda, se pierde o se interrumpe; el terreno no es el esperado; el sensor se degrada. Por eso el rol combina cuatro capacidades: **cómo se mueve** (cinemática y dinámica), **qué ve y dónde está** (percepción y localización), **cómo corrige** (control) y **qué decide sin esperar al operador** (autonomía).

Su unidad de trabajo es la **tarea verificada**: no «el robot funciona», sino «esta maniobra se completa dentro de estos límites, y si algo sale mal el robot se detiene de forma segura».

Tres frentes se reparten el oficio:

- **Manipulación.** Brazos y mecanismos: cinemática directa e inversa, singularidades, restricciones articulares, captura y acoplamiento ([**B101** · Manipuladores robóticos espaciales](../../programa/tronco-comun/B101-manipuladores-roboticos-espaciales.md)).
- **Movilidad y localización.** Rovers y vehículos de superficie: tracción en terreno suelto, odometría, mapeo y localización simultánea ([**B102** · Movilidad de robots planetarios](../../programa/tronco-comun/B102-movilidad-de-robots-planetarios.md), [**B99** · Localización y mapeo robótico](../../programa/tronco-comun/B99-localizacion-y-mapeo-robotico.md), [**B103** · Percepción visual robótica](../../programa/tronco-comun/B103-percepcion-visual-robotica.md)).
- **Autonomía y teleoperación.** Qué delega el operador al robot, cómo se controla con retardo y qué ocurre si se pierde el enlace ([**B98** · Autonomía y teleoperación espacial](../../programa/tronco-comun/B98-autonomia-y-teleoperacion-espacial.md)).

Un recordatorio práctico de la referencia de la NASA sobre tecnología de satélites pequeños: los mecanismos han contribuido a más del 10 % de las fallas reportadas de satélites pequeños, por lo que se diseñan con margen, ensayo de vida y prueba «como se vuela».

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es navegación y guiado de vehículos orbitales.** [Navegación, guiado y autonomía espacial](navegacion-guiado-y-autonomia-espacial.md) estima órbitas y guía naves; tú trabajas con manipuladores, rovers y autonomía de tareas en superficie o a corta distancia.
- **No es aviónica y software de alta fiabilidad.** [Aviónica y software espacial de alta fiabilidad](avionica-y-software-espacial-de-alta-fiabilidad.md) construye la base que tú usas; el foco tuyo es el comportamiento del robot.
- **No es arquitectura de hábitats ni recursos extraterrestres.** [Arquitectura y hábitats extraterrestres](arquitectura-y-habitats-extraterrestres.md) y [Recursos extraterrestres y economía industrial espacial](recursos-extraterrestres-y-economia-industrial-espacial.md) usan robots para construir o excavar; tú los diseñas, ellos definen el uso.
- **No es astronáutica tripulada.** [Astronáutica tripulada y entrenamiento de astronautas](astronautica-tripulada-y-entrenamiento-de-astronautas.md) trabaja junto a robots; tú los diseñas.
- **No es «inteligencia artificial» en general.** La autonomía aquí es un conjunto de decisiones acotadas y verificables, no un sistema abierto.

## 🗓️ Un día en el puesto

Un día típico se reparte entre simulación, prueba e integración:

- **Simular y comparar.** Una maniobra se simula y se contrasta con el modelo: la pose estimada por la cámara contra la pose de referencia, la deriva del odómetro tras 100 m, el tiempo que tarda el brazo en llegar a una configuración sin cruzar una singularidad.
- **Escribir pruebas adversas.** Escenarios con pérdida de enlace, sensor degradado o terreno distinto al esperado; revisas los registros de las corridas fallidas.
- **Discutir los límites de seguridad.** Qué fuerza máxima, qué distancia mínima, cuándo el robot se detiene; se decide por escrito con el resto del equipo.
- **Ajustar percepción y localización.** Calibración, mapas de profundidad, falsos positivos en la detección de obstáculos.
- **Documentar.** Decisiones, supuestos y condiciones en que el robot se detiene.

La habilidad no es hacer que el robot funcione una vez, sino **saber en qué condiciones deja de funcionar y qué hace entonces**.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Cinemática y dinámica:** rotaciones, jacobianos, cinemática directa e inversa, dinámica multicuerpo ([**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md), [**B101** · Manipuladores robóticos espaciales](../../programa/tronco-comun/B101-manipuladores-roboticos-espaciales.md)).
- **Control y estimación:** estabilidad, saturación, filtros de Kalman y de partículas ([**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md), [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md), [**B80** · Navegación inercial y fusión multisensorial](../../programa/tronco-comun/B80-navegacion-inercial-y-fusion-multisensorial.md)).
- **Percepción:** visión, calibración, mapas de profundidad y SLAM ([**B103** · Percepción visual robótica](../../programa/tronco-comun/B103-percepcion-visual-robotica.md), [**B99** · Localización y mapeo robótico](../../programa/tronco-comun/B99-localizacion-y-mapeo-robotico.md)).
- **Movilidad:** interacción rueda-terreno y planificación de rutas ([**B102** · Movilidad de robots planetarios](../../programa/tronco-comun/B102-movilidad-de-robots-planetarios.md)).
- **Autonomía y teleoperación:** control supervisado, colas de comandos, respuesta a pérdida de enlace ([**B98** · Autonomía y teleoperación espacial](../../programa/tronco-comun/B98-autonomia-y-teleoperacion-espacial.md)).
- **Operaciones de proximidad:** aproximación y acoplamiento ([**B76** · Dinámica cislunar y operaciones de proximidad](../programa/tronco-comun/B76-dinamica-cislunar-y-operaciones-de-proximidad.md)).
- **Software y pruebas:** programación, simulación, reproducibilidad ([**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md), [**B88** · Aviónica y software crítico espacial](../programa/tronco-comun/B88-avionica-y-software-critico-espacial.md)).
- **Incertidumbre:** propagar errores de sensores y justificar márgenes ([**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md)).

### Herramientas del oficio

```text
Simulación:         entornos de simulación de robots y de dinámica multicuerpo
Cálculo:            Python (NumPy, SciPy), álgebra lineal, optimización
Percepción:         bibliotecas de visión, calibración de cámaras, nubes de puntos
Estimación/control: filtros de Kalman y de partículas, diseño de controladores
Pruebas:            escenarios adversos automatizados, registro y repetición de corridas
Control de cambios: control de versiones de modelos, parámetros y datos
```

Estas son categorías; los entornos y bibliotecas concretos son una decisión del equipo y este programa no los recomienda por marca. Una prueba en simulación no autoriza una operación real.

### Habilidades no técnicas

- **Mentalidad de falla:** pensar primero en cómo se rompe y cómo se detiene.
- **Honestidad con las métricas:** reportar deriva, falsos positivos y casos adversos, no solo el caso feliz.
- **Comunicación con el equipo:** acordar límites de seguridad con quien integra y quien opera.
- **Paciencia con la depuración:** muchos fallos aparecen solo en una combinación de condiciones.
- **Criterio ético:** registrar las decisiones autónomas y mantener la posibilidad de anulación humana.

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md) — A02 · 20 clases
2. 📚 [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) — A02 · 26 clases
3. 📚 [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) — A02 · 26 clases
4. 📚 [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) — A02 · 23 clases
5. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — A02 · 31 clases
6. 📚 [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) — A02 · 20 clases
7. 📚 [**B87** · Sensores y control de actitud](../programa/tronco-comun/B87-sensores-y-control-de-actitud.md) — A07 · 22 clases

### 🎯 El núcleo del rol

**A02 · Matemática, física computacional y métodos científicos**

1. 📚 [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) — usa 2 de 20 clases: `B10-` C16, C19
2. 📚 [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) — usa 3 de 24 clases: `B15-` C14, C17–C18

**A06 · Mecánica orbital, navegación y vuelo espacial**

3. 📚 [**B76** · Dinámica cislunar y operaciones de proximidad](../programa/tronco-comun/B76-dinamica-cislunar-y-operaciones-de-proximidad.md) — usa 4 de 20 clases: `B76-` C09, C12, C14, C16
4. 📚 [**B80** · Navegación inercial y fusión multisensorial](../programa/tronco-comun/B80-navegacion-inercial-y-fusion-multisensorial.md) — usa 1 de 9 clases: `B80-` C09

**A07 · Ingeniería y construcción de sistemas espaciales**

5. 📚 [**B83** · Ingeniería de sistemas y diseño de misiones](../programa/tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) — usa 5 de 24 clases: `B83-` C01, C03–C04, C07, C17
6. 📚 [**B86** · Sistemas de potencia y energía espacial](../programa/tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md) — usa 1 de 23 clases: `B86-` C19
7. 📚 [**B88** · Aviónica y software crítico espacial](../programa/tronco-comun/B88-avionica-y-software-critico-espacial.md) — usa 8 de 44 clases: `B88-` C08–C09, C11–C12, C14, C17, C19, C44
8. 📚 [**B89** · Comunicaciones y navegación satelital](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) — usa 2 de 25 clases: `B89-` C12–C13

**A08 · Operaciones de misión y robótica espacial**

9. 📚 [**B96** · Control y operación de misiones espaciales](../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) — usa 8 de 30 clases: `B96-` C04, C06–C07, C09, C12–C15
10. 📚 [**B97** · Robótica y construcción extraterrestre](../programa/tronco-comun/B97-robotica-y-construccion-extraterrestre.md) — usa 20 de 27 clases: `B97-` C01–C08, C10–C12, C16–C24
11. 📚 [**B98** · Autonomía y teleoperación espacial](../programa/tronco-comun/B98-autonomia-y-teleoperacion-espacial.md) — usa 5 de 8 clases: `B98-` C03–C07
12. 📚 [**B99** · Localización y mapeo robótico](../programa/tronco-comun/B99-localizacion-y-mapeo-robotico.md) — usa 7 de 7 clases: `B99-` C01–C07
13. 📚 [**B101** · Manipuladores robóticos espaciales](../programa/tronco-comun/B101-manipuladores-roboticos-espaciales.md) — usa 8 de 10 clases: `B101-` C01–C08
14. 📚 [**B102** · Movilidad de robots planetarios](../programa/tronco-comun/B102-movilidad-de-robots-planetarios.md) — usa 8 de 8 clases: `B102-` C01–C08
15. 📚 [**B103** · Percepción visual robótica](../programa/tronco-comun/B103-percepcion-visual-robotica.md) — usa 8 de 8 clases: `B103-` C01–C08

**A11 · Economía, industria y gestión de proyectos espaciales**

16. 📚 [**B124** · Industria, economía, ética y proyectos espaciales](../programa/tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) — usa 2 de 24 clases: `B124-` C12, C19

<!-- /ruta -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es un **portafolio de simulaciones verificadas** (educativo, sin operar robots reales):

- una simulación de un brazo con cinemática inversa, singularidades y restricciones articulares, con pruebas;
- una cadena de odometría y SLAM con su deriva medida contra rutas conocidas;
- un mapa de profundidad calibrado y la evaluación de falsos positivos en detección de obstáculos;
- una simulación de teleoperación con retardo y pérdida de enlace;
- un informe de pruebas en escenarios adversos, con las condiciones en que el robot se detiene.

Todo reproducible (código, datos, versiones) y con unidades, marcos de referencia y tolerancias declarados. Guarda la primera versión, la retroalimentación y los cambios.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional única verificada. Las referencias de trabajo que sí se consultaron (2026-11-05) son:

- 📘 **NASA, *State-of-the-Art of Small Spacecraft Technology*, cap. 5 «Guidance, Navigation, and Control»** — página con fecha de 7 de mayo de 2026, leída hasta aproximadamente el 90 %. Trata la aproximación y las operaciones de proximidad, señala que los mecanismos de acoplamiento y sujeción son esenciales para el servicio en órbita, insiste en reducir la dependencia del apoyo desde tierra y afirma que la navegación de espacio profundo probablemente dependerá solo de métodos autónomos. (https://www.nasa.gov/smallsat-institute/sst-soa/guidance-navigation-and-control/)
- 📗 **NASA, mismo informe, cap. 6 «Structures, Materials, and Mechanisms»** — página con fecha de 4 de agosto de 2026, leída hasta aproximadamente el 80 %. Incluye brazos robóticos pequeños y advierte que los mecanismos han contribuido a más del 10 % de las fallas reportadas de satélites pequeños; recomienda margen, pruebas de vida y probar «como se vuela». (https://www.nasa.gov/smallsat-institute/sst-soa/structures-materials-and-mechanisms/)

Ambas referencias señalan que las prestaciones comerciales no están verificadas de forma independiente. Las normas de seguridad de robots y las certificaciones personales dependen de la jurisdicción y de la versión vigente, y **no están verificadas aquí**; consúltalas en su fuente oficial.

## 📈 Progresión del rol

Rutas habituales: **implementador/a y validador/a de módulos (percepción, cinemática, control) → integrador/a de una cadena completa que especifica las pruebas → responsable de la arquitectura de autonomía de una misión**. Desde ahí se abren la navegación y guiado, la aviónica y la ingeniería de sistemas. Los niveles y requisitos dependen de cada organización; no se publican cifras salariales porque no se pudieron verificar con fuentes.

Roles vecinos con los que se comparte formación: [navegación, guiado y autonomía](navegacion-guiado-y-autonomia-espacial.md), [aviónica y software](avionica-y-software-espacial-de-alta-fiabilidad.md) y [hábitats extraterrestres](arquitectura-y-habitats-extraterrestres.md).

## ⚠️ Mitos y errores comunes

- **«Si funciona en simulación, funciona en el terreno.»** Una prueba en simulación no autoriza una operación real; el terreno, el polvo y el sensor degradado no figuran en el modelo.
- **«Más autonomía siempre es mejor.»** La autonomía se limita a decisiones acotadas y verificables; lo crítico se deja registrado y puede ser anulado por un operador.
- **«La localización se resuelve con un buen sensor.»** La deriva existe: se mide contra rutas conocidas y se acota.
- **«El brazo es solo cinemática.»** Singularidades, límites articulares y fallas de mecanismos son la causa de muchos fallos.
- **«El retardo se compensa con rapidez.»** Se compensa con arquitectura: control supervisado, colas de comandos y respuesta definida a pérdida de enlace.
- **«Un robot de servicio es siempre pacífico.»** Los robots de captura pueden usarse con fines no pacíficos; se aplica el marco de uso dual y de normas del tronco ([B119](../programa/tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md)).

## 🚀 Siguientes pasos

1. **Asienta la base** con [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md), [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md), [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) y [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md).
2. Aprende cinemática y manipulación con [**B101** · Manipuladores robóticos espaciales](../../programa/tronco-comun/B101-manipuladores-roboticos-espaciales.md) y simula un brazo con pruebas.
3. Aprende percepción y localización con [**B103** · Percepción visual robótica](../../programa/tronco-comun/B103-percepcion-visual-robotica.md) y [**B99** · Localización y mapeo robótico](../../programa/tronco-comun/B99-localizacion-y-mapeo-robotico.md); mide la deriva de tu odometría.
4. Estudia movilidad y autonomía con [**B102** · Movilidad de robots planetarios](../../programa/tronco-comun/B102-movilidad-de-robots-planetarios.md) y [**B98** · Autonomía y teleoperación espacial](../../programa/tronco-comun/B98-autonomia-y-teleoperacion-espacial.md); simula teleoperación con retardo y pérdida de enlace.
5. Reúne tu **portafolio** de simulaciones y guarda su historia: primera versión, retroalimentación y cambios.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Navegación guiado y autonomía espacial](navegacion-guiado-y-autonomia-espacial.md) · [Aviónica y software espacial de alta fiabilidad](avionica-y-software-espacial-de-alta-fiabilidad.md) · [Arquitectura y hábitats extraterrestres](arquitectura-y-habitats-extraterrestres.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R17-robotica-espacial-y-sistemas-autonomos/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
