# B124 — Industria, economía, ética y proyectos espaciales

> **Bloque ampliado.** Las 20 clases de la línea base y las 4 programadas por la ampliación (`B124-C21` a `B124-C24`) están redactadas. Ver el [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md).

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial
**Área:** A11 — Economía, industria y gestión de proyectos espaciales
**Nivel:** N3–N4 (fundamentos y aplicación) · **Clases:** 24 · **Carga:** por calibrar con el uso
**Estado:** guía pedagógica del bloque (resumen de qué se aprende en cada clase). Las clases enlazadas en las tablas ya están redactadas; todas conservan el estado E0 en el catálogo hasta registrar revisión disciplinar.

## 🎯 Propósito del bloque

Enseña **cómo se razona con números un proyecto espacial desde el lado de la industria, el dinero, la ética y la gestión**, con modelos pequeños, verificables y siempre rotulados. Recorre la cadena de valor y los mercados, la diferencia entre agencias y empresas, el diseño de una propuesta de valor y los acuerdos de nivel de servicio de un producto de datos; después los costos (de misión, de un servicio, del transporte por kilogramo y de una instalación extraterrestre), el financiamiento público y privado, el seguro y el riesgo, la propiedad intelectual, los contratos y la sostenibilidad económica de una constelación. Sigue con el retorno científico, la ética de datos y la ciencia abierta, y cierra con la gestión de un proyecto: cronograma, equipos, comunicación, propuesta de misión y portafolio. Cada clase termina con un laboratorio en Python con semilla fija; las cifras salen de datos **sintéticos o ilustrativos** (rotulados) o de documentos primarios consultados con fecha.

## 📚 Al terminar el bloque podrás

1. Descomponer una cadena de valor y un mercado y medir su concentración y su dependencia entre etapas.
2. Estimar costos con relaciones paramétricas, curvas de aprendizaje, costo por kilogramo y costos de capital y de operación, y decir cuánta incertidumbre arrastran.
3. Comparar fuentes de financiamiento y contratos con valor actual, tasa interna de retorno, dilución y reparto de sobrecostos.
4. Cuantificar el riesgo asegurable y la disponibilidad de un servicio de datos con una segunda vía de verificación.
5. Evaluar el retorno científico, el riesgo de reidentificación de datos y la reproducibilidad de un análisis.
6. Planificar un proyecto con valor ganado, ruta crítica, equipos y comunicación, y armar una propuesta de misión y un portafolio.
7. Rotular qué es consultado, qué es sintético y qué es ilustrativo, y recordar que nada de esto es asesoría financiera, legal ni de inversión.

## 🧭 Secuencia del bloque

```mermaid
flowchart LR
    A["Tramo 1<br/>Industria, mercados<br/>y propuesta de valor"]
    B["Tramo 2<br/>Costos y<br/>financiamiento"]
    C["Tramo 3<br/>Riesgo, derecho<br/>y contratos"]
    D["Tramo 4<br/>Ciencia, ética<br/>y datos"]
    E["Tramo 5<br/>Gestión del<br/>proyecto"]
    A --> B --> C --> D --> E
```

**Descripción textual.** Cinco tramos encadenados: quién hace qué y qué valor ofrece (tramo 1), cuánto cuesta y cómo se paga (tramo 2), cómo se asegura, se licencia y se contrata (tramo 3), cómo se evalúa lo científico y se protegen los datos (tramo 4) y cómo se gestiona y se presenta el proyecto (tramo 5). El hilo común es poner un número, con su incertidumbre, a cada decisión.

## 🗂️ Las 24 clases en resumen

**Navegación:** cada clase enlaza a la anterior, a la siguiente y a este bloque.

La columna «Evidencia» indica el producto que demostrará el aprendizaje. Los laboratorios usan datos **sintéticos** o **ilustrativos** (rotulados) o valores publicados con fuente y fecha.

### Tramo 1 · Industria, mercados y propuesta de valor

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b124-c01"></a>[B124-C01](../clases/B124/B124-C01-cadena-de-valor-de-industria-espacial/CLASE.md) | Cadena de valor de industria espacial | Valor agregado por etapa, participación y multiplicador de una cadena sintética. | Ficha de cadena de valor con valor agregado por etapa |
| <a id="b124-c02"></a>[B124-C02](../clases/B124/B124-C02-agencias-cientificas-y-empresas/CLASE.md) | Agencias científicas y empresas | Comprar un servicio frente a poseer el sistema; precio por asiento recalculado desde un informe de la OIG de la NASA. | Ficha de decisión comprar o poseer |
| <a id="b124-c03"></a>[B124-C03](../clases/B124/B124-C03-mercados-downstream-y-upstream/CLASE.md) | Mercados downstream y upstream | Concentración (HHI) y arrastre de la demanda aguas abajo con un modelo insumo-producto. | Ficha de concentración y arrastre de un mercado sintético |
| <a id="b124-c04"></a>[B124-C04](../clases/B124/B124-C04-diseno-de-propuesta-de-valor/CLASE.md) | Diseño de propuesta de valor | Puntaje multicriterio con pesos y estabilidad del ranking ante cambios de peso. | Matriz de propuesta de valor con sensibilidad |
| <a id="b124-c21"></a>[B124-C21](../clases/B124/B124-C21-acuerdos-de-nivel-de-servicio-para-productos-de-datos/CLASE.md) | Acuerdos de nivel de servicio para productos de datos | Disponibilidad desde MTBF y MTTR, presupuesto de error y cumplimiento de un plazo. | Ficha de acuerdo de nivel de servicio de un producto de datos |

### Tramo 2 · Costos y financiamiento

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b124-c05"></a>[B124-C05](../clases/B124/B124-C05-estimacion-de-costos-de-mision/CLASE.md) | Estimación de costos de misión | Relación paramétrica de costo en escala log-log, curva de aprendizaje y banda de incertidumbre. | Estimación de costo de una misión sintética con banda |
| <a id="b124-c22"></a>[B124-C22](../clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md) | Modelo de costo de un servicio de datos | Costos fijos y variables, punto de equilibrio y precio con margen objetivo. | Modelo de costo y precio de un servicio de datos |
| <a id="b124-c23"></a>[B124-C23](../clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md) | Costos de transporte por kilogramo a superficie | Ecuación del cohete, fracción de carga útil y costo por kilogramo a órbita y a superficie. | Tabla de costo por kilogramo con sensibilidad |
| <a id="b124-c24"></a>[B124-C24](../clases/B124/B124-C24-capex-y-opex-de-una-instalacion-extraterrestre/CLASE.md) | CapEx y OpEx de una instalación extraterrestre | Factor de recuperación de capital, costo nivelado y peso del transporte. | Costo nivelado de una instalación sintética |
| <a id="b124-c06"></a>[B124-C06](../clases/B124/B124-C06-financiamiento-publico/CLASE.md) | Financiamiento público | Perfil de gasto frente a tope anual y retraso por brecha de fondos; cifras de adjudicación de la OIG. | Ficha de brecha de financiamiento anual |
| <a id="b124-c07"></a>[B124-C07](../clases/B124/B124-C07-financiamiento-privado/CLASE.md) | Financiamiento privado | Valor actual neto, tasa interna de retorno y dilución en rondas. | Ficha de flujo, retorno y dilución sintéticos |

### Tramo 3 · Riesgo, derecho y contratos

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b124-c08"></a>[B124-C08](../clases/B124/B124-C08-seguros-y-riesgo-espacial/CLASE.md) | Seguros y riesgo espacial | Pérdida esperada, prima con recargo y cola de pérdidas con Monte Carlo; régimen de responsabilidad. | Ficha de prima y riesgo de una cobertura sintética |
| <a id="b124-c09"></a>[B124-C09](../clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md) | Propiedad intelectual y licencias | Valor actual de regalías, licencia exclusiva frente a no exclusiva y apilamiento de regalías. | Ficha de valoración de una licencia sintética |
| <a id="b124-c10"></a>[B124-C10](../clases/B124/B124-C10-contratos-y-compras-espaciales/CLASE.md) | Contratos y compras espaciales | Precio fijo frente a costo más incentivo y reparto de un sobrecosto. | Ficha comparativa de tipos de contrato |
| <a id="b124-c11"></a>[B124-C11](../clases/B124/B124-C11-sostenibilidad-economica-de-constelaciones/CLASE.md) | Sostenibilidad económica de constelaciones | Reposición de flota, costo por suscriptor y punto de equilibrio. | Ficha de equilibrio de una constelación sintética |

### Tramo 4 · Ciencia, ética y datos

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b124-c12"></a>[B124-C12](../clases/B124/B124-C12-evaluacion-de-retorno-cientifico/CLASE.md) | Evaluación de retorno científico | Valor científico con rendimientos decrecientes y frontera de Pareto costo-ciencia. | Ficha de retorno científico y frontera de Pareto |
| <a id="b124-c13"></a>[B124-C13](../clases/B124/B124-C13-etica-de-investigacion-y-datos/CLASE.md) | Ética de investigación y datos | k-anonimato, generalización y pérdida de información en datos sintéticos. | Ficha de riesgo de reidentificación |
| <a id="b124-c14"></a>[B124-C14](../clases/B124/B124-C14-ciencia-abierta-y-reproducibilidad/CLASE.md) | Ciencia abierta y reproducibilidad | Semilla, orden de operaciones y huella criptográfica; lista FAIR puntuada. | Manifiesto reproducible con huella y lista FAIR |

### Tramo 5 · Gestión del proyecto

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b124-c15"></a>[B124-C15](../clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md) | Gestión de proyectos espaciales | Estructura de desglose, valor ganado (CPI, SPI) y estimación al término. | Tablero de valor ganado de un proyecto sintético |
| <a id="b124-c16"></a>[B124-C16](../clases/B124/B124-C16-planificacion-de-cronograma-y-entregables/CLASE.md) | Planificación de cronograma y entregables | Ruta crítica, holguras y distribución de la duración con Monte Carlo. | Cronograma con ruta crítica y probabilidad de plazo |
| <a id="b124-c17"></a>[B124-C17](../clases/B124/B124-C17-gestion-de-equipos-multidisciplinarios/CLASE.md) | Gestión de equipos multidisciplinarios | Canales de comunicación, cobertura de competencias y tamaño del equipo. | Ficha de composición de un equipo sintético |
| <a id="b124-c18"></a>[B124-C18](../clases/B124/B124-C18-comunicacion-y-divulgacion/CLASE.md) | Comunicación y divulgación | Embudo de alcance, prueba de dos proporciones y tamaño de muestra. | Plan de divulgación con prueba A/B sintética |
| <a id="b124-c19"></a>[B124-C19](../clases/B124/B124-C19-redaccion-de-propuesta-de-mision/CLASE.md) | Redacción de propuesta de misión | Matriz de trazabilidad de requisitos y presupuesto con reservas. | Esqueleto de propuesta con trazabilidad y reservas |
| <a id="b124-c20"></a>[B124-C20](../clases/B124/B124-C20-proyecto-integrador-y-portafolio-profesional/CLASE.md) | Proyecto integrador y portafolio profesional | Rúbrica ponderada con condiciones críticas no compensables sobre un portafolio. | Portafolio profesional con rúbrica autoaplicada |

## 🧵 Hilos que atraviesan el bloque

- **Todo número tiene incertidumbre:** C05, C08, C16, C18 y C21 la estiman con una segunda vía (analítica y Monte Carlo).
- **Del costo al precio:** C05, C22, C23 y C24 encadenan costo de misión, de servicio, de transporte y de instalación.
- **Quién asume el riesgo:** C06 a C11 reparten el riesgo entre el Estado, el privado, el asegurador y el contratista.
- **Datos con responsabilidad:** C13 y C14 unen ética y reproducibilidad; C21 y C22 las llevan a un servicio.
- **Observado frente a modelado:** las cifras de los modelos son sintéticas o ilustrativas; las pocas cifras reales vienen de un informe de la OIG de la NASA y se rotulan.

## 📝 Evaluación del bloque (propuesta, por calibrar)

- Fichas y ejercicios por clase, con retroalimentación y recuperación con evidencia distinta.
- Portafolio: el proyecto integrador (C20) con su propuesta (C19), su presupuesto con reservas y su cronograma.
- Las condiciones críticas (rotular lo sintético e ilustrativo, no dar asesoría financiera ni legal, citar solo lo consultado) no se compensan con promedio.

## ⚠️ Seguridad y límites

El bloque es educativo. **No es asesoría financiera, legal, tributaria ni de inversión**, y no sustituye a un profesional habilitado ni a la normativa vigente de cada Estado. Los modelos son simplificados (flujos deterministas o independientes, tasas constantes, distribuciones supuestas). Las cifras de mercado, precios, tasas y probabilidades de falla son sintéticas o ilustrativas, salvo las pocas citadas del informe de la OIG de la NASA; no se consultaron datos de mercado, primas de seguros reales, contratos reales ni normas de gestión de pago.

## 📖 Fuentes consultadas en el bloque (resumen)

Consultadas el 2026-11-11: el texto de las Naciones Unidas de los tratados sobre el espacio ultraterrestre (Oficina de Asuntos del Espacio Ultraterrestre, UNOOSA; artículos I, II, VI y VII del Tratado de 1967 y II y III del Convenio sobre responsabilidad), el informe IG-20-005 de la Oficina del Inspector General de la NASA (noviembre de 2019) sobre el programa de tripulación comercial, la página del Cost Estimating Handbook v4.0 de la NASA y su apéndice E, el NASA Systems Engineering Handbook (SP-6105, Rev 2; página y PDF, para la ruta crítica y las fases del ciclo de vida), el artículo de los principios FAIR (Wilkinson et al., 2016, vía PubMed Central) y la página de la UNESCO sobre su Recomendación sobre Ciencia Abierta (2021). El Handbook on Measuring the Space Economy de la OCDE solo apareció en resultados de búsqueda y **no se consultó**; tampoco se consultaron normas ISO, ECSS ni de gestión de proyectos de pago, datos de primas de seguros, mercados de lanzamiento ni legislación nacional. Las fórmulas (valor actual, tasa interna de retorno, valor ganado, ruta crítica, Poisson, ecuación del cohete) son relaciones estándar que verifica cada laboratorio y no se consultaron en una fuente concreta.

## Fuentes de orientación preliminar

- **[NASA-HUMAN]** [NASA Human Research Program](https://www.nasa.gov/hrp/) — Factores humanos, medicina y riesgos de exploración tripulada.
- **[UNOOSA]** [United Nations Office for Outer Space Affairs](https://www.unoosa.org/) — Tratados, regulación e iniciativas de cooperación internacional.
- **[ITU]** [International Telecommunication Union](https://www.itu.int/) — Telecomunicaciones y coordinación del espectro internacional.
- **[NASA-SYSTEMS]** [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — Ingeniería de sistemas, verificación, validación y gestión técnica.

> La asociación de estas fuentes es orientativa por bloque. Las fuentes realmente consultadas para cada afirmación se registran en la sección 11 de cada clase.

## Roles que lo usan

Pendiente: la asignación de roles y recorridos la define el autor al final.

[🏠 Volver al programa](../../README.md) · [➡️ B125 — Creación y operación de empresas espaciales](./B125-creacion-y-operacion-de-empresas-espaciales.md)
