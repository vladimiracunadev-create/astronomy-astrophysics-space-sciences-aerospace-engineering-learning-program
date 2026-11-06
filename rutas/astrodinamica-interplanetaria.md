# 🌌 Astrodinámica interplanetaria

> Diseñas trayectorias para llegar a otros cuerpos del sistema solar: transferencias, asistencias gravitatorias y ventanas de lanzamiento, con optimización y análisis de robustez.
>
> **Nivel de entrada:** matemática, física y programación de nivel universitario; rol técnico de diseño de misión · **Foco:** mecánica orbital, problema de Lambert, transferencias, asistencias gravitatorias, optimización de trayectorias, robustez · **Entrega:** un diseño de trayectoria reproducible, con su presupuesto de velocidad, sus ventanas y su análisis de sensibilidad

## 🧭 Qué es y por qué importa

Llegar a Marte, a Júpiter o a un asteroide exige elegir una trayectoria entre infinitas posibles. El diseñador busca la que cumple las restricciones de la misión con el **menor costo de propulsante, tiempo o riesgo**, y que además resista errores reales de lanzamiento y de navegación.

El oficio combina mecánica orbital con optimización numérica. Las trayectorias interplanetarias se construyen por tramos: se resuelven transferencias entre dos puntos, se encadenan con encuentros planetarios que aportan velocidad gratis y se refinan con un optimizador hasta cumplir todas las restricciones.

Las miradas del rol son:

- **Mecánica de transferencias.** Lambert, cónicas empalmadas, asistencias. Su pregunta es: *¿qué trayectoria base conecta origen y destino?*
- **Optimización.** Trayectorias de bajo empuje o impulsivas, restricciones. Su pregunta es: *¿cuál es el mejor diseño y cuán sensible es?*
- **Robustez.** Errores de ejecución y de navegación. Su pregunta es: *¿sigue funcionando si las cosas salen mal?*

### 🚫 Qué NO es este rol (y con quién se confunde)

- **No es navegación a bordo.** Esa estima el estado real del vehículo ([Navegación guiado y autonomía espacial](navegacion-guiado-y-autonomia-espacial.md)); tú diseñas la trayectoria nominal.
- **No es propulsión.** Usas las capacidades del motor como restricción; diseñarlo es otro rol ([Ingeniería de lanzadores y propulsión](ingenieria-de-lanzadores-y-propulsion.md)).
- **No es solo teoría orbital.** Exige optimización numérica y software.
- **No es «copiar la trayectoria de una misión anterior».** Cada misión cambia fechas, masas y restricciones.

## 🗓️ Un día en el puesto

- **Diseño preliminar:** calculas transferencias candidatas y comparas su costo.
- **Optimización:** refinas una trayectoria con un optimizador y verificas restricciones.
- **Ventanas:** exploras fechas de lanzamiento y arribo.
- **Robustez:** simulas errores y evalúas la corrección necesaria.
- **Documentación:** dejas el diseño reproducible para el equipo.

Dicho sin adornos: **un buen diseño se reconoce porque se sabe dónde falla**.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Mecánica orbital** ([**B71** · Mecánica orbital fundamental](../programa/tronco-comun/B71-mecanica-orbital-fundamental.md)); **perturbaciones** ([**B72** · Perturbaciones y evolución de órbitas](../programa/tronco-comun/B72-perturbaciones-y-evolucion-de-orbitas.md)); **mecánica celeste y caos** ([**B73** · Mecánica celeste, resonancias y caos](../programa/tronco-comun/B73-mecanica-celeste-resonancias-y-caos.md)).
- **Estimación de órbitas** ([**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md)).
- **Trayectorias y misiones interplanetarias** ([**B75** · Trayectorias y misiones interplanetarias](../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md)); **problema de Lambert** ([**B82** · Problema de Lambert y transferencias de dos puntos](../PROGRAMA_ACADEMICO_COMPLETO.md#b82--problema-de-lambert-y-transferencias-de-dos-puntos)).
- **Optimización de trayectorias y diseño robusto** ([**B81** · Optimización de trayectorias y diseño robusto](../PROGRAMA_ACADEMICO_COMPLETO.md#b81--optimización-de-trayectorias-y-diseño-robusto)).
- **Dinámica cislunar** ([**B76** · Dinámica cislunar y operaciones de proximidad](../programa/tronco-comun/B76-dinamica-cislunar-y-operaciones-de-proximidad.md)).
- **Simulación numérica** ([**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md)).

### Herramientas del oficio

```text
Cálculo:              Python científico y propagadores orbitales
Optimización:         optimizadores no lineales con restricciones
Efemérides:           datos de posición de los cuerpos del sistema solar
Pruebas:              casos conocidos para verificar el código
Documentación:        registro de versión de datos, modelos y parámetros
```

Un optimizador devuelve una solución aunque el problema esté mal planteado. Verifica con casos conocidos antes de confiar.

### Habilidades no técnicas

- **Pensar en restricciones reales.**
- **Comunicación con ingeniería de sistemas y con operaciones.**
- **Documentación clara de supuestos.**
- **Paciencia con la convergencia.**

<!-- ruta:inicio -->
## 📚 Tu ruta en el programa

Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).

### 🧱 Fundamentos (según tu diagnóstico)

1. 📚 [**B15** · Señales, imágenes y estimación científica](../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) — A02 · 24 clases
2. 📚 [**B16** · Sistemas dinámicos y control automático](../programa/tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) — A02 · 20 clases

### 🎯 El núcleo del rol

**A01 · Alfabetización científica, astronómica y tecnológica**

1. 📚 [**B07** · Informática científica desde cero](../programa/tronco-comun/B07-informatica-cientifica-desde-cero.md) — usa 1 de 20 clases: `B07-` C17

**A02 · Matemática, física computacional y métodos científicos**

2. 📚 [**B09** · Cálculo diferencial e integral](../programa/tronco-comun/B09-calculo-diferencial-e-integral.md) — usa 1 de 20 clases: `B09-` C07
3. 📚 [**B10** · Álgebra lineal y matemáticas geométricas](../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) — usa 1 de 20 clases: `B10-` C16
4. 📚 [**B11** · Ecuaciones diferenciales y simulación numérica](../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md) — usa 3 de 26 clases: `B11-` C08, C17, C19
5. 📚 [**B12** · Probabilidad, estadística e incertidumbre](../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) — usa 1 de 26 clases: `B12-` C16
6. 📚 [**B13** · Metrología, tiempo y mediciones científicas](../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) — usa 2 de 23 clases: `B13-` C08, C11
7. 📚 [**B14** · Computación científica y ciencia abierta](../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md) — usa 1 de 31 clases: `B14-` C10

**A05 · Ciencias planetarias, astroquímica y habitabilidad**

8. 📚 [**B53** · Astrogeología y geodesia planetaria](../programa/tronco-comun/B53-astrogeologia-y-geodesia-planetaria.md) — usa 1 de 30 clases: `B53-` C03

**A06 · Mecánica orbital, navegación y vuelo espacial**

9. 📚 [**B71** · Mecánica orbital fundamental](../programa/tronco-comun/B71-mecanica-orbital-fundamental.md) — usa 4 de 20 clases: `B71-` C09, C18–C20
10. 📚 [**B72** · Perturbaciones y evolución de órbitas](../programa/tronco-comun/B72-perturbaciones-y-evolucion-de-orbitas.md) — usa 8 de 21 clases: `B72-` C02, C06, C08–C10, C18–C20
11. 📚 [**B73** · Mecánica celeste, resonancias y caos](../programa/tronco-comun/B73-mecanica-celeste-resonancias-y-caos.md) — usa 6 de 22 clases: `B73-` C08, C10–C12, C21–C22
12. 📚 [**B74** · Estimación de órbitas y navegación espacial](../programa/tronco-comun/B74-estimacion-de-orbitas-y-navegacion-espacial.md) — usa 8 de 30 clases: `B74-` C07, C11–C12, C15, C19–C22
13. 📚 [**B75** · Trayectorias y misiones interplanetarias](../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md) — usa 26 de 30 clases: `B75-` C01–C14, C17–C18, C21–C30
14. 📚 [**B76** · Dinámica cislunar y operaciones de proximidad](../programa/tronco-comun/B76-dinamica-cislunar-y-operaciones-de-proximidad.md) — usa 1 de 20 clases: `B76-` C18
15. 📚 [**B77** · Dinámica de lanzamiento y reentrada](../programa/tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md) — usa 1 de 25 clases: `B77-` C11
16. 📚 [**B81** · Optimización de trayectorias y diseño robusto](../PROGRAMA_ACADEMICO_COMPLETO.md#b81--optimización-de-trayectorias-y-diseño-robusto) — usa 15 de 15 clases: `B81-` C01–C15
17. 📚 [**B82** · Problema de Lambert y transferencias de dos puntos](../PROGRAMA_ACADEMICO_COMPLETO.md#b82--problema-de-lambert-y-transferencias-de-dos-puntos) — usa 7 de 7 clases: `B82-` C01–C07

**A07 · Ingeniería y construcción de sistemas espaciales**

18. 📚 [**B86** · Sistemas de potencia y energía espacial](../programa/tronco-comun/B86-sistemas-de-potencia-y-energia-espacial.md) — usa 1 de 23 clases: `B86-` C04
19. 📚 [**B89** · Comunicaciones y navegación satelital](../programa/tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) — usa 1 de 25 clases: `B89-` C14

**A08 · Operaciones de misión y robótica espacial**

20. 📚 [**B96** · Control y operación de misiones espaciales](../programa/tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) — usa 1 de 30 clases: `B96-` C11

<!-- /ruta -->

### 🧪 Práctica y evidencias

El producto que demuestra el rol es un **diseño de trayectoria documentado**:

- una misión de ejemplo con sus restricciones;
- una trayectoria base y su refinamiento optimizado;
- un presupuesto de velocidad y una exploración de ventanas;
- un análisis de sensibilidad frente a errores;
- el código y las efemérides para repetirlo.

Los bloques de la ruta aportan ejercicios y laboratorios; guarda la primera versión y sus cambios.

## 🎓 Reconocimientos y referencias profesionales

Este rol no tiene, en este programa, una certificación profesional verificada, y para esta guía no se consultó una fuente externa específica (2026-11-05). Por eso no se citan normas, requisitos de acceso ni cifras: cuando se necesiten, deben consultarse en la fuente oficial vigente de la institución, agencia o empresa correspondiente.

## 📈 Progresión del rol

Rutas habituales: **analista de misión o de trayectorias → responsable del diseño de trayectoria de una misión → liderazgo de análisis de misión**. Se abren la dinámica de vuelo y la navegación. No se publican cifras salariales por no poder verificarlas.

Roles vecinos con los que se comparte formación: [Navegación guiado y autonomía espacial](navegacion-guiado-y-autonomia-espacial.md), [Ingeniería de lanzadores y propulsión](ingenieria-de-lanzadores-y-propulsion.md) y [Matemática y computación científica espacial](matematica-y-computacion-cientifica-espacial.md).

## ⚠️ Mitos y errores comunes

- **«La trayectoria más corta es la mejor».** Suele no serlo en costo ni en riesgo.
- **«La asistencia gravitatoria es gratis».** Cuesta tiempo y restricciones de geometría.
- **«Una solución del optimizador es la óptima».** Puede ser un óptimo local.
- **«Una vez diseñada, no cambia».** Se rediseña cuando cambian masas y fechas.
- **«Es solo matemática».** Es matemática al servicio de restricciones de ingeniería.

## 🚀 Siguientes pasos

1. **Asienta la base** con el área A01 y la matemática de tu diagnóstico.
2. Estudia **mecánica orbital** ([**B71** · Mecánica orbital fundamental](../programa/tronco-comun/B71-mecanica-orbital-fundamental.md)) y **perturbaciones** ([**B72** · Perturbaciones y evolución de órbitas](../programa/tronco-comun/B72-perturbaciones-y-evolucion-de-orbitas.md)).
3. Avanza a **trayectorias interplanetarias** ([**B75** · Trayectorias y misiones interplanetarias](../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md)) y al **problema de Lambert** ([**B82** · Problema de Lambert y transferencias de dos puntos](../PROGRAMA_ACADEMICO_COMPLETO.md#b82--problema-de-lambert-y-transferencias-de-dos-puntos)).
4. Profundiza en **optimización y robustez** ([**B81** · Optimización de trayectorias y diseño robusto](../PROGRAMA_ACADEMICO_COMPLETO.md#b81--optimización-de-trayectorias-y-diseño-robusto)).
5. Reúne tu **diseño documentado** con su historial.

<!-- pie:inicio -->
---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Navegación guiado y autonomía espacial](navegacion-guiado-y-autonomia-espacial.md) · [Ingeniería de lanzadores y propulsión](ingenieria-de-lanzadores-y-propulsion.md) · [Ingeniería y construcción de satélites y CubeSats](ingenieria-y-construccion-de-satelites-y-cubesats.md)
- 🧭 [Recorrido detallado y equivalencias de los módulos](../programa/rutas-profesionales/R09-astrodinamica-interplanetaria/RECORRIDO.md)
- 🏠 [Inicio del programa](../README.md)
<!-- /pie -->
