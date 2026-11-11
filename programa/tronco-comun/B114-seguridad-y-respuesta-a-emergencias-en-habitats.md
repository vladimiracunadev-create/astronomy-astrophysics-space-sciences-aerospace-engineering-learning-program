# B114 — Seguridad y respuesta a emergencias en hábitats

> **Bloque nuevo de la estructura `0.2.0`.** Sus 6 clases estaban programadas por la ampliación y ahora están redactadas. Ver el [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md).

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial
**Área:** A09 — Astronáutica humana, medicina y hábitats
**Nivel:** N3 (fundamentos disciplinares) · **Clases:** 6 · **Carga:** por calibrar con el uso
**Estado:** guía pedagógica del bloque (resumen de qué se aprende en cada clase). Las clases enlazadas en la tabla ya están redactadas; todas conservan el estado E0 en el catálogo hasta registrar revisión disciplinar.

## 🎯 Propósito del bloque

Enseña **cómo se razona cuantitativamente una emergencia en un hábitat presurizado**: cuánto tiempo hay para actuar, qué umbrales disparan una alarma, dónde está la fuga y cuán protegido está un refugio. Recorre el trazado de rutas de evacuación y su tiempo de salida, la detección y localización de fugas de presión, la lógica de alarmas ante desviaciones de O₂, CO₂ y presión, el refugio contra tormentas solares, los escenarios de despresurización y la matriz de riesgo ambiental que los ordena. Cada clase cierra con un laboratorio en Python con semilla fija y datos **sintéticos** rotulados.

## 📚 Al terminar el bloque podrás

1. Calcular el tiempo de evacuación de una red de pasillos y comprobar que cada ruta tiene una alternativa independiente.
2. Estimar la tasa de fuga desde la caída de presión y localizar el origen con mediciones en varios compartimentos.
3. Diseñar umbrales de alarma con histéresis y confirmación, y medir sus falsos positivos y su retraso.
4. Estimar la atenuación de dosis de un refugio con un modelo exponencial ilustrativo y comparar contra un objetivo de dosis.
5. Calcular el tiempo de despresurización de un volumen por un orificio y compararlo con un umbral de presión.
6. Construir una matriz de riesgo de probabilidad por severidad y priorizar medidas, rotulando sus supuestos.

## 🧭 Secuencia del bloque

```mermaid
flowchart LR
    A["C01<br/>Rutas de evacuación"]
    B["C02<br/>Fugas de presión"]
    C["C03<br/>Alarmas atmosféricas"]
    D["C04<br/>Refugio solar"]
    E["C05<br/>Despresurización"]
    F["C06<br/>Matriz de riesgo"]
    A --> B --> C --> D --> E --> F
```

**Descripción textual.** Seis clases encadenadas: salir del hábitat (C01), detectar y localizar la fuga (C02), alarmar a tiempo y sin ruido (C03), refugiarse de la radiación (C04), calcular cuánto tarda una despresurización (C05) y ordenar todos los peligros en una matriz de riesgo (C06). El hilo común es el **tiempo disponible frente al tiempo necesario**.

## 🗂️ Las 6 clases en resumen

**Navegación:** cada clase enlaza a la anterior, a la siguiente y a este bloque.

La columna «Evidencia» indica el producto que demostrará el aprendizaje. Los laboratorios usan datos **sintéticos** o **ilustrativos** (rotulados) o valores publicados con fuente y fecha.

### Tramo 1 · Atmósfera y salida

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b114-c01"></a>[B114-C01](../clases/B114/B114-C01-rutas-de-evacuacion-y-salidas-de-emergencia-en-habitats/CLASE.md) | Rutas de evacuación y salidas de emergencia en hábitats | Tiempo de evacuación por camino mínimo, rutas independientes y cuello de botella. | Plano de evacuación sintético con tiempos |
| <a id="b114-c02"></a>[B114-C02](../clases/B114/B114-C02-deteccion-localizacion-y-respuesta-a-fugas-de-presion/CLASE.md) | Detección, localización y respuesta a fugas de presión | Tasa de fuga desde la caída de presión y localización por mínimos cuadrados. | Informe de fuga con tasa, origen e incertidumbre |
| <a id="b114-c03"></a>[B114-C03](../clases/B114/B114-C03-alarmas-y-procedimientos-ante-desviaciones-atmosfericas/CLASE.md) | Alarmas y procedimientos ante desviaciones atmosféricas | Umbrales, histéresis, confirmación y retraso de detección de O₂, CO₂ y presión. | Tabla de umbrales y desempeño de alarma |

### Tramo 2 · Escenarios extremos y riesgo

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b114-c04"></a>[B114-C04](../clases/B114/B114-C04-refugio-contra-tormentas-solares-y-compartimentos-de-proteccion/CLASE.md) | Refugio contra tormentas solares y compartimentos de protección | Atenuación de dosis con blindaje y tiempo de permanencia frente a un objetivo. | Ficha de dosis de un refugio |
| <a id="b114-c05"></a>[B114-C05](../clases/B114/B114-C05-despresurizacion-escenarios-tiempos-y-respuesta/CLASE.md) | Despresurización: escenarios, tiempos y respuesta | Flujo por un orificio, tiempo hasta un umbral y margen de respuesta. | Cuadro de escenarios de despresurización |
| <a id="b114-c06"></a>[B114-C06](../clases/B114/B114-C06-matriz-de-riesgo-ambiental-de-un-habitat/CLASE.md) | Matriz de riesgo ambiental de un hábitat | Probabilidad por severidad, clasificación y priorización de medidas. | Matriz de riesgo con medidas y riesgo residual |

## 🧵 Hilos que atraviesan el bloque

- **Tiempo disponible frente a tiempo necesario:** C01, C02, C05 y C04 comparan lo que tarda el peligro con lo que tarda la respuesta.
- **Umbral y confirmación:** C03 y C06 deciden cuándo actuar y cuánto ruido se tolera.
- **Sintético frente a observado:** todo número del bloque es un modelo con datos sintéticos o ilustrativos; ninguno es una medición de un hábitat real.
- **Verificación independiente:** cada laboratorio contrasta con un caso analítico o con otra vía de cálculo.

## 📝 Evaluación del bloque (propuesta, por calibrar)

- Fichas y ejercicios por clase, con retroalimentación y recuperación con evidencia distinta.
- Portafolio: la matriz de riesgo (C06) con sus supuestos y su sensibilidad.
- Las condiciones críticas (rotular lo ilustrativo y sintético, no presentar un modelo como un procedimiento operativo y citar solo lo consultado) no se compensan con promedio.

## ⚠️ Seguridad y límites

El bloque es **educativo**. No es consejo médico ni operativo, no sustituye a las normas, procedimientos ni al entrenamiento de ninguna agencia o programa, y ningún número puede usarse para dimensionar, certificar ni operar un hábitat real. Los umbrales de atmósfera y dosis son ejemplos rotulados; los límites reales los fija la norma vigente del programa. Las fugas, tormentas y despresurizaciones simuladas no son observaciones.

## 📖 Fuentes consultadas en el bloque (resumen)

Consultadas el 2026-11-10: las notas técnicas de la NASA OCHMO sobre atmósfera habitable (OCHMO-TB-003, Rev A, 2023, derivada de NASA-STD-3001 Vol. 2 Rev D) y sobre dióxido de carbono (OCHMO-TB-004), leídas con PyMuPDF; la ficha de la Tierra de NASA/NSSDC; las constantes del NIST (CODATA 2022) y la respuesta de la Health Physics Society (23-02-2026) sobre el refugio de Artemis I. No se consultaron los rangos numéricos de `[V2 6003]` ni los requisitos de salidas de emergencia, de detección de fugas ni de blindaje de refugio de NASA-STD-3001. Las relaciones físicas (flujo por orificio, ley de gas ideal, atenuación exponencial, camino mínimo) son estándar y las verifica cada laboratorio.

## Fuentes de orientación preliminar

- **[NASA-STD-3001]** [NASA Technical Standards](https://standards.nasa.gov/) — Normas de salud y desempeño humano.
- **[ECSS]** [European Cooperation for Space Standardization](https://ecss.nl/) — Estándares europeos de ingeniería espacial.
- **[NCRP]** [National Council on Radiation Protection](https://ncrponline.org/) — Informes de protección radiológica.
- **[NASA-NTRS]** [NASA Technical Reports Server](https://ntrs.nasa.gov/) — Informes técnicos de la NASA.

> La asociación de estas fuentes es orientativa por bloque. Las fuentes realmente consultadas para cada afirmación se registran en la sección 11 de cada clase.

## Roles que lo usan

- [Arquitectura y hábitats extraterrestres](../../rutas/arquitectura-y-habitats-extraterrestres.md)

[🏠 Volver al programa](../../README.md)
