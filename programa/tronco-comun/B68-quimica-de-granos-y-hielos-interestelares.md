# B68 — Química de granos y hielos interestelares

> **Bloque de la malla `0.2.0`.** Ver el [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md).

**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial
**Área:** A05 — Ciencias planetarias, astroquímica y habitabilidad
**Nivel:** N3 (fundamentos disciplinares) · **Clases:** 4 · **Carga:** por calibrar con el uso
**Estado:** guía pedagógica del bloque (resumen de qué se aprende en cada clase). Las clases enlazadas en la tabla ya están redactadas; todas conservan el estado E0 en el catálogo hasta registrar revisión disciplinar.

## 🎯 Propósito del bloque

Enseña **cómo los hielos que recubren los granos de polvo interestelar intercambian moléculas con el gas y se transforman bajo la energía que reciben**. La primera clase estudia la desorción térmica con la ecuación de Polanyi–Wigner (energía de enlace, factor preexponencial, orden cinético y rampa de calentamiento). La segunda estudia la fotodesorción: el rendimiento por fotón ultravioleta, su dependencia de la temperatura y del espesor, y cómo separar la desorción de la fotólisis. La tercera trata la irradiación por partículas y fotones energéticos: pulverización (*sputtering*) por iones pesados, dosis, cinética de destrucción y formación de productos, y la diferencia entre fotoquímica y química de radiación. La cuarta describe el montaje de laboratorio de ultra alto vacío criogénico: cuánto tarda en contaminarse una superficie, cuánto hielo se deposita, cómo se mide el espesor y qué entrega una desorción programada. Cada clase cierra con un laboratorio en Python que contrasta con un caso analítico o con dos vías independientes, y distingue lo consultado de lo ilustrativo.

## 📚 Al terminar el bloque podrás

1. Calcular tiempos de residencia y temperaturas de desorción de un hielo con la ecuación de Polanyi–Wigner de orden cero y uno, con unidades explícitas.
2. Simular una desorción programada por temperatura (TPD) y estimar cómo cambian el pico y el inicio con la energía de enlace y la velocidad de calentamiento.
3. Calcular la vida de una capa de hielo bajo un flujo ultravioleta con un rendimiento de fotodesorción dado, y separar la desorción de la fotólisis en una curva de espesor frente a fluencia.
4. Aplicar la parametrización del rendimiento de pulverización con el poder de frenado y su dependencia del espesor del hielo.
5. Resolver la cinética de destrucción y formación de productos bajo irradiación y convertir entre fluencia, dosis y valor G.
6. Dimensionar un experimento criogénico en ultra alto vacío: tiempo de contaminación, tasa de deposición, espesor y rampa de desorción.

## 🧭 Secuencia del bloque

```mermaid
flowchart LR
    A["C01<br/>Desorción térmica"]
    B["C02<br/>Fotodesorción"]
    C["C03<br/>Radiólisis y productos"]
    D["C04<br/>Laboratorio UHV criogénico"]
    A --> B --> C --> D
```

**Descripción textual.** Cuatro clases encadenadas: primero el mecanismo térmico (C01), después los dos mecanismos no térmicos (fotodesorción en C02 e irradiación con productos en C03) y por último el laboratorio donde todo esto se mide (C04).

## 🗂️ Las 4 clases en resumen

**Navegación:** cada clase desarrollada enlaza a la anterior, a la siguiente y a este bloque; mientras una clase siga solo programada, su enlace lleva a su fila en esta tabla.

La columna «Evidencia» indica el producto que demostrará el aprendizaje. Los laboratorios usan datos **sintéticos** o **ilustrativos** (rotulados) o valores publicados con fuente y fecha.

### Tramo 1 · Mecanismo térmico

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b68-c01"></a>[B68-C01](../clases/B68/B68-C01-desorcion-termica-de-hielos-interestelares/CLASE.md) | Desorción térmica de hielos interestelares | Polanyi–Wigner de orden cero y uno, tiempo de residencia y TPD con parámetros publicados. | Ficha de la desorción térmica |

### Tramo 2 · Mecanismos no térmicos

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b68-c02"></a>[B68-C02](../clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md) | Fotodesorción de hielos interestelares | Rendimiento por fotón, dependencia de la temperatura y del espesor, y separación entre desorción y fotólisis. | Ficha de la fotodesorción |
| <a id="b68-c03"></a>[B68-C03](../clases/B68/B68-C03-irradiacion-de-hielos-por-rayos-cosmicos-y-uv-radiolisis-y-productos/CLASE.md) | Irradiación de hielos por rayos cósmicos y UV: radiólisis y productos | Pulverización con poder de frenado, dosis y valor G, y cinética de destrucción con productos. | Ficha de la radiólisis |

### Tramo 3 · El laboratorio

| ID | Clase | Qué se aprende | Evidencia |
|---|---|---|---|
| <a id="b68-c04"></a>[B68-C04](../clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md) | Laboratorio de astroquímica de hielos en ultra alto vacío criogénico | Flujo de Hertz–Knudsen, tiempo de contaminación, dosis en langmuir, espesor por infrarrojo y planificación de una TPD. | Ficha del montaje criogénico |

## 🧵 Hilos que atraviesan el bloque

- **Un mismo hielo, tres formas de perder moléculas:** C01 (calor), C02 (fotones) y C03 (iones y electrones secundarios) se comparan con la misma magnitud: moléculas desorbidas por monocapa y por unidad de tiempo o de fluencia.
- **Del laboratorio al cielo:** los parámetros salen de experimentos en ultra alto vacío (C04) y se extrapolan a escalas de tiempo astrofísicas con supuestos que cada clase declara.
- **Incertidumbre:** las energías de enlace, los rendimientos y los factores preexponenciales se informan con su incertidumbre publicada y se propaga su efecto.
- **Observado frente a simulado:** ningún espectro ni abundancia del medio interestelar se reproduce aquí; los valores de laboratorio se citan con su fuente y los de ejemplo se rotulan sintéticos.

## 📝 Evaluación del bloque (propuesta, por calibrar)

- Fichas y ejercicios por clase, con retroalimentación y recuperación con evidencia distinta.
- Portafolio: ficha de la desorción térmica (C01) y ficha del montaje criogénico (C04).
- Las condiciones críticas (rotular lo sintético, no presentar un parámetro de laboratorio como universal y citar solo lo consultado) no se compensan con promedio.

## ⚠️ Seguridad y límites

El bloque es educativo. Los modelos son cinéticas de campo medio de una sola especie y no sustituyen a un modelo gas–grano completo ni al análisis de un experimento real. Los hielos reales son mezclas y su estructura (porosidad, amorfo o cristalino) cambia los parámetros; aquí se usan valores de hielos puros o de capa múltiple y se dice cuándo. Los criógenos y el vacío ultra alto implican riesgos de laboratorio (asfixia por nitrógeno, quemaduras por frío, implosión); la clase 4 los menciona como contexto y no sustituye la formación de seguridad del laboratorio.

## Roles que lo usan

- [Astroquímica y astrobiología](../../rutas/astroquimica-y-astrobiologia.md)

## Fuentes consultadas

Consultadas el 2026-11-09 (el detalle por afirmación está en la sección 11 de cada clase):

- **[Fraser2001]** Fraser, Collings, McCoustra y Williams, *Thermal desorption of water ice in the interstellar medium*, MNRAS 327, 1165 (2001), arXiv:astro-ph/0107487 — solo resumen.
- **[Kruczkiewicz2024]** Kruczkiewicz et al., *Comprehensive laboratory constraints on thermal desorption of interstellar ice analogues*, A&A (2024), arXiv:2404.02695 — texto completo en PDF.
- **[Oberg2009]** Öberg, van Dishoeck y Linnartz, *Photodesorption of ices I: CO, N₂ and CO₂*, A&A 496, 281 (2009), arXiv:0809.1333 — texto completo en PDF.
- **[Fayolle2011]** Fayolle et al., *CO ice photodesorption: a wavelength-dependent study*, ApJ 739, L36 (2011), arXiv:1109.0281 — texto completo en PDF.
- **[Dartois2021]** Dartois et al., *Cosmic ray sputtering yield of interstellar ice mantles*, A&A 647, A177 (2021), arXiv:2102.04499 — texto completo en PDF.
- **[Arumainayagam2019]** Arumainayagam et al., *Extraterrestrial prebiotic molecules: photochemistry vs. radiation chemistry of interstellar ices*, Chem. Soc. Rev. 48, 2293 (2019) — solo resumen.
- **[GarrodHerbst2006]** Garrod y Herbst, *Formation of methyl formate and other organic species in the warm-up phase of hot molecular cores*, A&A (2006), arXiv:astro-ph/0607560 — solo resumen.
- **[CODATA2022]** NIST, constantes físicas fundamentales (CODATA 2022), `allascii.txt`.

> No consultadas (no se citan como respaldo): Paardekooper et al. 2016 (A&A 596, A72; la página del editor devolvió 403) y cualquier valor de fuerza de banda infrarroja. La asociación de fuentes con cada afirmación se registra en la sección 11 de cada clase.

[🏠 Volver al programa](../../README.md) · [⬅️ B67 — Prospección y evaluación de reservas de recursos extraterrestres](./B67-prospeccion-y-evaluacion-de-reservas-de-recursos-extraterrestres.md) · [➡️ B69 — Radar de apertura sintética e interferometría: profundización](./B69-radar-de-apertura-sintetica-e-interferometria-profundizacion.md)
