# B97 — Robótica y construcción extraterrestre

> **Bloque ampliado.** Además de las 20 clases de la línea base, el bloque tiene 7 clases programadas por la ampliación (`B97-C21` a `B97-C27`). Las 27 clases están redactadas y se listan por tramo temático. Ver el [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md).

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial
**Área:** A08 — Astronáutica humana, operaciones, sociedad y futuro espacial
**Nivel:** N3 (fundamentos disciplinares) · **Clases:** 20 + 7 de la ampliación · **Carga:** por calibrar con el uso
**Estado:** guía pedagógica del bloque (resumen de qué se aprende en cada clase). Las clases enlazadas en las tablas ya están redactadas; todas conservan el estado E0 en el catálogo hasta registrar revisión disciplinar.

## 🎯 Propósito del bloque

Enseña **cómo se razona y se calcula en robótica espacial y en construcción fuera de la Tierra**: qué hace un rover frente a un orbitador, cómo se mueve un brazo, cómo percibe y se localiza un robot, cuánto cuesta moverse sobre un regolito blando, qué hace la latencia con la teleoperación, cómo se planifica, se coordina, se mantiene y se prueba una flota, y cómo se excava, se imprime y se cubre con regolito un hábitat. Cada clase cierra con un laboratorio en Python (solo biblioteca estándar, con semilla fija cuando hay azar) que usa **datos sintéticos o ilustrativos rotulados** y valores publicados con fuente y fecha, y que se contrasta con una segunda vía de cálculo.

## 📚 Al terminar el bloque podrás

1. Resolver la cinemática directa e inversa de un brazo y reconocer sus singularidades.
2. Calcular el error de profundidad de un par estéreo, fusionar sensores y medir la deriva de una trayectoria.
3. Estimar la tracción disponible en regolito blando con la gravedad de Marte o de la Luna.
4. Calcular el retardo de luz de un enlace y el tiempo de una tarea teleoperada.
5. Planificar una ruta, repartir tareas entre robots y evaluar una estrategia de exploración autónoma.
6. Dimensionar repuestos, cronogramas de ensamblaje y la cobertura de regolito de un hábitat.
7. Evaluar la probabilidad de falla de una arquitectura redundante y planificar una campaña de pruebas.
8. Distinguir en todo resultado lo observado, lo consultado y lo simulado.

## 🧭 Secuencia del bloque

```mermaid
flowchart LR
    P["Plataformas<br/>y movilidad"]
    M["Manipulación<br/>y actuadores"]
    S["Percepción<br/>y autonomía"]
    O["Operaciones<br/>en órbita"]
    C["Construcción<br/>y maquinaria"]
    V["Seguridad, pruebas<br/>y simulación"]
    P --> M --> S --> O --> C --> V
```

**Descripción textual.** Seis tramos: las plataformas y su movilidad (C01, C06, C07, C08, C16); la manipulación y los actuadores (C02, C10, C24); la percepción y la autonomía (C03, C04, C05, C21, C22); las operaciones robóticas en órbita (C09, C11, C12, C13, C19); la construcción y la maquinaria extraterrestre (C14, C15, C25, C26, C27); y la seguridad, las pruebas y la simulación (C17, C18, C20, C23). El hilo común es que toda cifra es un modelo contrastado, no una medición.

## 🗂️ Las 27 clases en resumen

**Navegación:** cada clase enlaza a la anterior, a la siguiente y a este bloque. La numeración `C01`–`C27` es la del catálogo; los tramos agrupan por tema.

La columna «Evidencia» indica el producto que demostrará el aprendizaje. Los laboratorios usan datos **sintéticos** o **ilustrativos** (rotulados) o valores publicados con fuente y fecha.


### Tramo 1 · Plataformas y movilidad

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b97-c01"></a>[B97-C01](../clases/B97/B97-C01-robots-rover-y-orbitadores/CLASE.md) | Robots rover y orbitadores | Presupuesto de recorrido de un rover frente a la cobertura de un orbitador; `GM = g R²` derivado de la ficha de Marte. | Ficha comparativa rover frente a orbitador |
| <a id="b97-c06"></a>[B97-C06](../clases/B97/B97-C06-control-de-movilidad-sobre-regolito/CLASE.md) | Control de movilidad sobre regolito | Empuje y tracción de una rueda en suelo blando según el deslizamiento, con la gravedad de Marte y de la Luna. | Ficha de tracción y pendiente máxima en regolito |
| <a id="b97-c07"></a>[B97-C07](../clases/B97/B97-C07-teleoperacion-con-latencia/CLASE.md) | Teleoperación con latencia | Retardo de luz Tierra–Luna y Tierra–Marte y tiempo de una tarea con ciclo «mover y esperar». | Ficha de latencia y duración de una tarea teleoperada |
| <a id="b97-c08"></a>[B97-C08](../clases/B97/B97-C08-planificacion-de-trayectorias-roboticas/CLASE.md) | Planificación de trayectorias robóticas | Planificación en rejilla con A* sobre un mapa de costos y comprobación contra Dijkstra. | Ficha de ruta planificada sobre un mapa sintético |
| <a id="b97-c16"></a>[B97-C16](../clases/B97/B97-C16-autonomia-de-exploracion/CLASE.md) | Autonomía de exploración | Exploración por fronteras sobre una rejilla con semilla frente a una exploración aleatoria. | Ficha de cobertura de una estrategia de exploración |

### Tramo 2 · Manipulación y actuadores

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b97-c02"></a>[B97-C02](../clases/B97/B97-C02-cinematica-de-manipuladores/CLASE.md) | Cinemática de manipuladores | Cinemática directa e inversa de un brazo plano de dos articulaciones, jacobiano y singularidades. | Ficha cinemática de un brazo de dos eslabones |
| <a id="b97-c10"></a>[B97-C10](../clases/B97/B97-C10-manipulacion-de-herramientas/CLASE.md) | Manipulación de herramientas | Fuerza de agarre por fricción para una herramienta con distinta gravedad y aceleración. | Ficha de fuerza de agarre de una herramienta |
| <a id="b97-c24"></a>[B97-C24](../clases/B97/B97-C24-modelos-de-actuadores-virtuales-e-integracion-en-simulacion/CLASE.md) | Modelos de actuadores virtuales e integración en simulación | Actuador de motor con saturación, retardo y holgura y su efecto en un lazo de control. | Ficha de un actuador virtual y su respuesta |

### Tramo 3 · Percepción y autonomía

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b97-c03"></a>[B97-C03](../clases/B97/B97-C03-sensores-y-percepcion-robotica/CLASE.md) | Sensores y percepción robótica | Fusión de dos sensores por varianza inversa y comprobación por Monte Carlo con semilla. | Ficha de presupuesto de ruido de un conjunto de sensores |
| <a id="b97-c04"></a>[B97-C04](../clases/B97/B97-C04-vision-estereoscopica/CLASE.md) | Visión estereoscópica | Profundidad por disparidad `Z = f B / d` y propagación del error de disparidad. | Ficha de error de profundidad de un par estéreo |
| <a id="b97-c05"></a>[B97-C05](../clases/B97/B97-C05-localizacion-y-mapeo-slam/CLASE.md) | Localización y mapeo SLAM | Deriva de la odometría y cierre de bucle por mínimos cuadrados en un grafo de poses sintético. | Ficha de deriva y cierre de bucle de una trayectoria |
| <a id="b97-c21"></a>[B97-C21](../clases/B97/B97-C21-clasificacion-y-priorizacion-autonoma-de-muestras-a-bordo/CLASE.md) | Clasificación y priorización autónoma de muestras a bordo | Clasificador de muestras con espectros sintéticos y selección de datos bajo un presupuesto de enlace. | Ficha de priorización de muestras a bordo |
| <a id="b97-c22"></a>[B97-C22](../clases/B97/B97-C22-deteccion-autonoma-de-eventos-cientificos/CLASE.md) | Detección autónoma de eventos científicos | Detector CUSUM de eventos en una serie sintética: retraso de detección y falsas alarmas. | Ficha de un detector autónomo de eventos |

### Tramo 4 · Operaciones robóticas en órbita

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b97-c09"></a>[B97-C09](../clases/B97/B97-C09-robotica-colaborativa/CLASE.md) | Robótica colaborativa | Asignación de tareas entre robots y comparación de una heurística voraz con el óptimo exhaustivo. | Ficha de asignación de tareas de un equipo de robots |
| <a id="b97-c11"></a>[B97-C11](../clases/B97/B97-C11-robots-de-inspeccion-orbital/CLASE.md) | Robots de inspección orbital | Movimiento relativo de Clohessy–Wiltshire para una órbita de inspección, verificado por integración numérica. | Ficha de una órbita relativa de inspección |
| <a id="b97-c12"></a>[B97-C12](../clases/B97/B97-C12-robots-de-mantenimiento/CLASE.md) | Robots de mantenimiento | Reemplazo de unidades y repuestos con Poisson; confianza de cubrir las fallas de una misión. | Ficha de repuestos de mantenimiento para una misión |
| <a id="b97-c13"></a>[B97-C13](../clases/B97/B97-C13-ensamblaje-de-estructuras-en-orbita/CLASE.md) | Ensamblaje de estructuras en órbita | Cronograma de ensamblaje con precedencias, ruta crítica y número de robots. | Ficha de cronograma de ensamblaje de una armadura |
| <a id="b97-c19"></a>[B97-C19](../clases/B97/B97-C19-logistica-de-piezas-y-reparaciones/CLASE.md) | Logística de piezas y reparaciones | Repuestos y masa de un kit logístico con tiempo de reabastecimiento y confianza. | Ficha de kit de repuestos y reabastecimiento |

### Tramo 5 · Construcción y maquinaria extraterrestre

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b97-c14"></a>[B97-C14](../clases/B97/B97-C14-construccion-con-regolito-robotica-y-construccion-extraterrestre/CLASE.md) | Construcción con regolito — Robótica y construcción extraterrestre | Presión interna frente a cobertura de regolito, blindaje por densidad superficial y gravedad lunar. | Ficha de cobertura de regolito de un hábitat |
| <a id="b97-c15"></a>[B97-C15](../clases/B97/B97-C15-impresion-3d-espacial/CLASE.md) | Impresión 3D espacial | Energía de sinterizado, tiempo de impresión y masa depositada por capa. | Ficha de energía y tiempo de una impresión 3D |
| <a id="b97-c25"></a>[B97-C25](../clases/B97/B97-C25-excavacion-y-manejo-de-regolito-con-robots/CLASE.md) | Excavación y manejo de regolito con robots | Fuerza de excavación, límite de tracción y productividad de una excavadora robótica. | Ficha de excavación y acarreo de regolito |
| <a id="b97-c26"></a>[B97-C26](../clases/B97/B97-C26-monitoreo-de-condicion-de-maquinaria-extraterrestre/CLASE.md) | Monitoreo de condición de maquinaria extraterrestre | Indicadores de vibración (RMS, curtosis) y proyección de vida útil restante por regresión. | Ficha de condición de un rodamiento sintético |
| <a id="b97-c27"></a>[B97-C27](../clases/B97/B97-C27-simulacion-de-productividad-de-flotas-de-maquinaria/CLASE.md) | Simulación de productividad de flotas de maquinaria | Productividad de una flota con simulación de eventos, cola y comparación con el modelo analítico. | Ficha de productividad de una flota de maquinaria |

### Tramo 6 · Seguridad, pruebas y simulación

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b97-c17"></a>[B97-C17](../clases/B97/B97-C17-seguridad-funcional-robotica/CLASE.md) | Seguridad funcional robótica | Probabilidad de falla de arquitecturas 1oo1, 1oo2 y 2oo3, con comprobación por Monte Carlo. | Ficha de probabilidad de falla de una arquitectura redundante |
| <a id="b97-c18"></a>[B97-C18](../clases/B97/B97-C18-pruebas-en-entornos-analogos/CLASE.md) | Pruebas en entornos análogos | Teorema de ejecución exitosa y escalado de Froude para el diseño de campañas análogas. | Plan de campaña de pruebas en un entorno análogo |
| <a id="b97-c20"></a>[B97-C20](../clases/B97/B97-C20-mision-robotica-integrada-simulada/CLASE.md) | Misión robótica integrada simulada | Misión integrada simulada: traslado, energía, latencia y planificación con Monte Carlo. | Informe de una misión robótica simulada |
| <a id="b97-c23"></a>[B97-C23](../clases/B97/B97-C23-diseno-de-simulador-de-mision-robotica/CLASE.md) | Diseño de simulador de misión robótica | Paso de integración, error y determinismo de un simulador de una dinámica simple. | Especificación de un simulador de misión robótica |

## 🧵 Hilos que atraviesan el bloque

- **Escalado con la gravedad:** `g` interviene en la tracción (C06), el agarre (C10), la excavación (C25) y la cobertura de regolito (C14).
- **Incertidumbre propagada:** el ruido de los sensores (C03, C04), la deriva (C05) y la detección (C22) se cuantifican con una segunda vía y, cuando hay azar, con semilla fija.
- **Latencia y autonomía:** C07 mide el retardo; C08, C16, C21 y C22 muestran qué decide el robot sin esperar a la Tierra.
- **De la máquina a la flota:** C09, C12, C19, C26 y C27 pasan del robot individual a coordinación, repuestos, condición y productividad.
- **Observado frente a simulado:** todo número del bloque es un modelo con datos sintéticos o ilustrativos; ninguno describe una misión real ni una medición.

## 📝 Evaluación del bloque (propuesta, por calibrar)

- Fichas y ejercicios por clase, con retroalimentación y recuperación con evidencia distinta.
- Portafolio: el informe de la misión robótica simulada (C20), con sus supuestos, su sensibilidad y los límites del simulador.
- Las condiciones críticas (rotular lo ilustrativo y sintético, no presentar un modelo como observación y citar solo lo consultado) no se compensan con promedio.

## ⚠️ Seguridad y límites

El bloque es educativo. Los modelos son simplificados (brazo plano, suelo de Mohr–Coulomb simplificado, cámaras ideales, fallas independientes, reloj de simulación determinista) y no sustituyen a las normas de seguridad funcional, a la literatura primaria ni a las pruebas de hardware. Ningún laboratorio controla un robot real. Las normas ECSS, ISO e IEC citadas como contexto **no se consultaron** y no se reproduce su contenido.

## 📖 Fuentes consultadas en el bloque (resumen)

Consultadas el 2026-11-10: las fichas de datos de la NASA/NSSDC de la Tierra, la Luna y Marte (gravedad media, radio medio y distancias); la página de componentes del rover Perseverance de la NASA (masa, ruedas, brazo y velocidad máxima); la página de Canadarm2 de la Agencia Espacial Canadiense (longitud del brazo y masa de carga útil); y el valor de la velocidad de la luz de las constantes del NIST. Las leyes y algoritmos usados (cinemática, mínimos cuadrados, A*, Poisson, CUSUM, Mohr–Coulomb, Clohessy–Wiltshire, Euler y Runge–Kutta) son relaciones estándar que verifica cada laboratorio por una segunda vía y no se consultaron en una fuente concreta. Las normas ECSS, las de seguridad funcional y los datos de regolito de las misiones Apolo **no se consultaron**: los parámetros de suelo son ilustrativos.

## Fuentes de orientación preliminar

- **[NASA-HUMAN]** [NASA Human Research Program](https://www.nasa.gov/hrp/) — Factores humanos, medicina y riesgos de exploración tripulada.
- **[UNOOSA]** [United Nations Office for Outer Space Affairs](https://www.unoosa.org/) — Tratados, regulación e iniciativas de cooperación internacional.
- **[ITU]** [International Telecommunication Union](https://www.itu.int/) — Telecomunicaciones y coordinación del espectro internacional.
- **[NASA-SYSTEMS]** [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — Ingeniería de sistemas, verificación, validación y gestión técnica.

> La asociación de estas fuentes es orientativa por bloque. Las fuentes realmente consultadas para cada afirmación se registran en la sección 11 de cada clase.

[🏠 Volver al programa](../../README.md) · [⬅️ B96 — Control y operación de misiones espaciales](./B96-control-y-operacion-de-misiones-espaciales.md) · [➡️ B98 — Autonomía y teleoperación espacial](./B98-autonomia-y-teleoperacion-espacial.md)
