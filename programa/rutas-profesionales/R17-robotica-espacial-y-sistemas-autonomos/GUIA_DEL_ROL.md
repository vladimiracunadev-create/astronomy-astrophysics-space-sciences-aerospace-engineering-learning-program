# R17 — Guía del rol: ingeniero/a de robótica espacial y sistemas autónomos

> Esta guía describe el rol para quien decide si es para sí. No es un temario ni una promesa de empleo, habilitación o título. El orden de clases está en [RECORRIDO.md](RECORRIDO.md).

## Qué es

Es la persona que hace que una máquina **actúe sola, o casi sola, donde nadie puede tocarla**: un brazo que agarra una pieza, un rover que cruza un terreno suelto, un vehículo que se acerca a otro satélite sin chocar. Combina cinemática y dinámica (cómo se mueve), percepción y localización (qué ve y dónde está), control (cómo corrige) y autonomía (qué decide sin esperar al operador, porque la señal tarda o se pierde).

Su unidad de trabajo es la **tarea verificada**: no «el robot funciona», sino «esta maniobra se completa dentro de estos límites, y si algo sale mal el robot se detiene de forma segura».

## Qué NO es (y con qué se confunde)

- **No es navegación y guiado de vehículos orbitales** ([R10](../R10-navegacion-guiado-y-autonomia-espacial/INDICE.md)): ese rol trata la estimación de órbita y la autonomía de naves; este trata manipuladores, rovers y autonomía de tareas en superficie o a corta distancia.
- **No es aviónica y software de alta fiabilidad** ([R13](../R13-avionica-y-software-espacial-de-alta-fiabilidad/INDICE.md)): usa ese software, pero el foco es el comportamiento del robot.
- **No es arquitectura de hábitats** ([R20](../R20-arquitectura-y-habitats-extraterrestres/INDICE.md)) ni recursos extraterrestres ([R21](../R21-recursos-extraterrestres-y-economia-industrial-espacial/INDICE.md)), aunque construya o excave para ellos.
- **No es astronáutica tripulada** ([R18](../R18-astronautica-tripulada-y-entrenamiento-de-astronautas/INDICE.md)), aunque diseñe robots que trabajan junto a astronautas.
- **No es «inteligencia artificial» en general.** La autonomía aquí es un conjunto de decisiones acotadas y verificables, no un sistema abierto.

## Un día de trabajo

Se simula una maniobra y se compara con el modelo: la pose estimada por la cámara contra la pose de referencia, la deriva del odómetro tras 100 m, el tiempo que tarda el brazo en llegar a una configuración sin cruzar una singularidad. Se escriben o ajustan pruebas con escenarios adversos (pérdida de enlace, sensor degradado, terreno distinto al esperado) y se revisan los logs de las corridas fallidas. En la parte de integración se discuten con el resto del equipo los límites de seguridad: qué fuerza máxima, qué distancia mínima, cuándo el robot se detiene.

## Qué decide y qué entrega

**Decide:** qué cinemática, percepción, localización y nivel de autonomía permiten cumplir la tarea con seguridad; qué queda bajo control de un operador y qué se delega al robot.

**Entrega:** modelos verificables, cadenas de percepción y localización con métricas, arquitecturas de autonomía, pruebas en simulación y de escenarios adversos, y el informe de una misión robótica simulada.

## Conocimientos y herramientas

- Álgebra lineal, rotaciones, jacobianos; cinemática directa e inversa; dinámica multicuerpo.
- Control automático, estabilidad, saturación; estimación con filtros de Kalman y de partículas.
- Visión, calibración, mapas de profundidad, SLAM.
- Teleoperación con retardo: control supervisado, colas de comandos, respuesta a pérdida de enlace.
- Programación, pruebas, simulación y reproducibilidad.

Los entornos de simulación y las bibliotecas concretas son decisión del equipo; el programa no las recomienda por marca.

## Qué dicen las fuentes consultadas

El capítulo de guiado, navegación y control de la referencia de NASA sobre tecnología de satélites pequeños (consultado el 2026-11-05; página con fecha 7 de mayo de 2026; leído hasta aproximadamente el 90 %) trata la aproximación y operaciones de proximidad y señala que los mecanismos de acoplamiento y sujeción son esenciales para el servicio en órbita; insiste en reducir la dependencia del apoyo desde tierra y afirma que la navegación futura de espacio profundo probablemente dependerá solo de métodos autónomos, y remite la manipulación robótica al capítulo de estructuras y mecanismos. Este último (consultado el 2026-11-05; página con fecha 4 de agosto de 2026; leído hasta aproximadamente el 80 %) incluye brazos robóticos pequeños y advierte que los mecanismos han contribuido a más del 10 % de las fallas reportadas de satélites pequeños, por lo que recomienda margen, pruebas de vida y probar «como se vuela». Las dos referencias señalan que las prestaciones comerciales no están verificadas de forma independiente.

Fuentes:

- NASA, *State-of-the-Art of Small Spacecraft Technology*, cap. 5 «Guidance, Navigation, and Control», <https://www.nasa.gov/smallsat-institute/sst-soa/guidance-navigation-and-control/> — consultado 2026-11-05.
- NASA, *State-of-the-Art of Small Spacecraft Technology*, cap. 6 «Structures, Materials, and Mechanisms», <https://www.nasa.gov/smallsat-institute/sst-soa/structures-materials-and-mechanisms/> — consultado 2026-11-05.

No se citan salarios, cifras de empleo ni certificaciones: no se verificaron.

## Evidencias y portafolio

Una simulación de un brazo con cinemática inversa, singularidades y restricciones articulares, con pruebas; una cadena de odometría y SLAM con su deriva medida contra rutas conocidas; un mapa de profundidad calibrado y su evaluación de falsos positivos en detección de obstáculos; una simulación de teleoperación con retardo y pérdida de enlace; un informe de pruebas en escenarios adversos con las condiciones en que el robot se detiene.

## Progresión

Se entra implementando y validando módulos (percepción, cinemática, control); luego se integra una cadena completa y se especifican pruebas; después se diseña la arquitectura de autonomía de una misión. Los niveles y requisitos dependen de cada organización.

## Límites éticos y de seguridad

- Un robot cerca de personas o de activos de terceros necesita límites de fuerza, distancia y parada segura verificados antes de operar; este recorrido no sustituye la certificación ni la supervisión profesional.
- La autonomía no debe esconder decisiones que afecten a vidas o bienes: se deja registrada y puede ser anulada por un operador.
- Los robots de servicio o de captura pueden usarse con fines no pacíficos: se aplica el marco de dual use y de normas del tronco (B63).
- Una prueba en simulación no autoriza una operación real.
