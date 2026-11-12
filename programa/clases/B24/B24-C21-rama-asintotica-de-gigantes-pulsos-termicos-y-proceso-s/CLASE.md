# B24-C21 — Rama asintótica de gigantes: pulsos térmicos y proceso s

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B24](../../../tronco-comun/B24-fisica-y-evolucion-de-estrellas.md) · [← Anterior: B24-C20 — Modelo simplificado de estructura estelar](../B24-C20-modelo-simplificado-de-estructura-estelar/CLASE.md) · [Siguiente: B24-C22 — Evolución binaria: lóbulo de Roche y transferencia de masa →](../B24-C22-evolucion-binaria-lobulo-de-roche-y-transferencia-de-masa/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 21 del bloque B24 (ampliación). Nivel N3. [C16](../B24-C16-gigantes-rojas/CLASE.md) describió las gigantes rojas de forma general y [C18](../B24-C18-etapas-finales-de-evolucion/CLASE.md) los finales de vida. Falta el tramo intermedio de las estrellas de masa baja y media: la **rama asintótica de gigantes (AGB)**, donde la estrella alterna fuentes de energía en capa, mezcla material nuclear hacia la superficie (**dragados**) y fabrica elementos más pesados que el hierro por **capturas lentas de neutrones** (**proceso s**). Usas la nucleosíntesis de [C08](../B24-C08-nucleosintesis-estelar/CLASE.md), el equilibrio de [C04](../B24-C04-equilibrio-hidrostatico-estelar/CLASE.md) y las ecuaciones diferenciales ([B11-C07](../../B11/B11-C07-runge-kutta-de-cuarto-orden/CLASE.md)). La física nuclear detallada está en [B31](../../../tronco-comun/B31-fisica-cuantica-nuclear-y-astroparticulas.md).

## 2. Por qué esta clase existe

Las estrellas AGB son una fuente importante de carbono, nitrógeno y elementos pesados del medio interestelar, y sus abundancias superficiales son el registro observable de lo que ocurre en su interior. Entender la cadena de capturas de neutrones y el efecto de un dragado permite leer una composición anómala como un resultado, no como una rareza. La decisión central: **dado un flujo de neutrones y las secciones eficaces, ¿qué abundancias resultan, y cuántos dragados hacen falta para que una envoltura rica en oxígeno se vuelva rica en carbono?**

## 3. Lo que podrás hacer al terminar

1. Describir la estructura y el ciclo de una estrella AGB (cualitativamente).
2. Definir proceso s, exposición de neutrones y flujo estacionario.
3. Resolver la cadena de capturas con la misma sección eficaz y compararla con la solución de Poisson.
4. Explicar por qué `σ_i N_i` es constante en el flujo estacionario.
5. Calcular el cambio de `C/O` por dragados sucesivos con conservación de masa.
6. Nombrar qué deja fuera el modelo (decaimientos beta, ramificaciones, mezcla real).

La evidencia es la **ficha de la fase AGB** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es una captura de neutrones y cómo cambia el núcleo?
2. ¿Qué es la sección eficaz?
3. ¿Qué es una distribución de Poisson?
4. ¿Qué es la razón `C/O` por número?
5. ¿Qué es un estado estacionario de una ecuación cinética?

<details>
<summary>Ver respuestas</summary>

1. Aumenta en uno el número de neutrones, sin cambiar el elemento. 2. Un área efectiva para que ocurra la reacción. 3. `P(i) = λⁱe^{−λ}/i!`. 4. El cociente de átomos de carbono y de oxígeno. 5. Aquel donde las derivadas temporales son cero.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa C08, B11-C07 y B12-C03.

## 5. Un caso real: cambios recurrentes en la superficie

Karakas y Lattanzio revisan la nucleosíntesis de estrellas individuales de masa baja e intermedia (por debajo de unas 10 `M☉`): episodios recurrentes de mezcla cambian de forma importante la composición de la envoltura y explican los enriquecimientos observados en carbono, nitrógeno, flúor y elementos pesados, producidos por captura lenta de neutrones, el proceso s (S1, resumen). Los diagramas de Gaia incluyen estrellas post-AGB y nebulosas planetarias en el HR (S2, resumen), y los modelos de MESA muestran pulsos térmicos de la fase AGB (S3, resumen). El **ejemplo conductor** es **sintético**: una cadena de capturas con secciones eficaces dadas y una envoltura que acumula carbono en cada dragado.

## 6. Vocabulario

La **rama asintótica de gigantes (AGB)** es la fase de masa baja e intermedia con un núcleo inerte de carbono y oxígeno rodeado de dos capas de fusión, de helio y de hidrógeno (descripción cualitativa estándar; las cifras no se consultaron). Un **pulso térmico** es un episodio recurrente de ignición de la capa de helio. El **dragado** (*dredge-up*) es la mezcla convectiva que lleva a la superficie material procesado. El **proceso s** es la captura lenta de neutrones, lenta frente a la desintegración beta. La **exposición de neutrones** `τ = ∫ σ n_n v dt` mide cuántas capturas ocurren por núcleo. Un **flujo estacionario** es aquel en que cada abundancia deja de cambiar. Una **estrella de carbono** es una estrella con `C/O > 1` en la superficie. Una **nebulosa planetaria** es la envoltura expulsada al final de la fase AGB.

## 7. Modelo mental: una cadena de montaje de pesos crecientes

Cada núcleo capta un neutrón y pasa a la siguiente posición de la cadena; si capta con facilidad (σ grande), no se acumula; si capta con dificultad (σ pequeña), se acumula, como una pieza que tarda en procesarse.

```mermaid
flowchart LR
    A["Pulso térmico<br/>(capa de He)"] --> B["Fuente de neutrones<br/>en la zona intermedia"]
    B --> C["Cadena N₀ → N₁ → N₂ ...<br/>(capturas con σᵢ)"]
    C --> D["Dragado: material<br/>llega a la envoltura"]
    D --> E["Superficie enriquecida<br/>C, N, elementos s"]
```

*Descripción textual:* en cada pulso se generan neutrones que alimentan una cadena de capturas; el dragado lleva el material a la envoltura y enriquece la superficie.

Analogía: una cadena de montaje con cuellos de botella. Límite: aquí la cadena es lineal y sin ramificaciones; la real puede bifurcarse en isótopos inestables.

## 8. La explicación, paso a paso

### 8.1 Estructura y ciclo de la AGB

Una estrella de masa baja o media que ha agotado el helio del núcleo (C16, C08) tiene un núcleo de carbono y oxígeno. En la fase AGB, dos capas de fusión (hidrógeno y helio) rodean el núcleo y la capa de helio se enciende de forma recurrente: son los pulsos térmicos. Tras cada pulso, la convección puede arrastrar material procesado a la envoltura (dragado). Esa descripción es estándar y cualitativa; los números concretos (periodos entre pulsos, masas dragadas) dependen del modelo y no se citan.

### 8.2 Cadena de capturas con la misma σ

Si todas las secciones eficaces son iguales y la exposición es `τ`, la abundancia relativa del núcleo con `i` capturas sigue `dN_i/dτ = N_{i−1} − N_i`, con solución de Poisson `N_i = τⁱ e^{−τ}/i!`. Con `τ = 2`, `N₀ = 0,135`, `N₁ = N₂ = 0,271` y `N₃ = 0,180`. El laboratorio integra con Runge–Kutta y coincide con Poisson a `6 × 10⁻¹⁵`. Cuanto mayor la exposición, más capturas por núcleo.

### 8.3 Secciones eficaces distintas y flujo estacionario

Con secciones distintas y una fuente que mantiene `N₀`, `dN_i/dt = σ_{i−1}N_{i−1} − σ_iN_i`. En el estado estacionario, `σ_iN_i = σ₀N₀` para todo `i`. Con `σ = [1, 0,5, 2, 0,1, 1,5, 0,8]` (sintéticas), las abundancias son `[1, 2, 0,5, 10, 0,67, 1,25]` y todos los productos valen `1,00000`. El núcleo de sección pequeña (`σ₃ = 0,1`) acumula una abundancia diez veces mayor: es el origen de los picos de abundancia de los elementos s en núcleos con secciones eficaces pequeñas.

### 8.4 Dragados y composición de la superficie

Si en cada pulso un dragado lleva `ΔM` de material con fracción de masa de carbono `X_C,dr` y de oxígeno `X_O,dr` a la envoltura, la masa de carbono crece en `ΔM X_C,dr` y la envoltura en `ΔM`. Con valores **sintéticos** (envoltura de `0,5 M☉`, `ΔM = 0,002 M☉`, `X_C,dr = 0,05`, `X_O,dr = 0,005`), la razón `C/O` por número pasa de `0,444` a `1,497` tras `40` pulsos y supera `1` en el pulso `21`. El laboratorio comprueba que la masa de carbono y de envoltura se conservan exactamente. Una envoltura con `C/O > 1` corresponde a una estrella de carbono.

### 8.5 Qué falta

El modelo no incluye decaimientos beta, ramificaciones, la fuente de neutrones, la mezcla parcial ni la pérdida de masa. La pérdida de masa en la AGB acaba expulsando la envoltura (nebulosa planetaria) y deja la enana blanca de C18. Los resultados son ilustrativos.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `τ` | exposición de neutrones | — | `2` (ilustrativo) |
| `σ_i` | sección eficaz relativa | — | `[1, 0,5, 2, 0,1, 1,5, 0,8]` (sintéticas) |
| `N_i` | abundancia relativa | — | Poisson o estacionaria |
| `ΔM` | masa dragada por pulso | `M☉` | `0,002` (sintético) |
| `X_C,dr`, `X_O,dr` | fracciones de masa en el material dragado | — | `0,05`; `0,005` (sintéticas) |
| `C/O` | razón por número | — | `0,444 → 1,497` |

## 10. Convenciones y referencias

Cadena lineal, sin decaimientos beta ni ramificaciones; todos los valores numéricos son **sintéticos**. `C/O` por número: `(m_C/12)/(m_O/16)`.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | Karakas y Lattanzio, *The Dawes Review 2: Nucleosynthesis and stellar yields of low and intermediate-mass single stars*, arXiv:1405.0062 | https://arxiv.org/abs/1405.0062 | Mezclas recurrentes cambian la composición superficial; enriquecimientos en C, N, F y elementos pesados por el proceso s | Solo resumen, consultado el 2026-11-09 |
| S2 | Gaia Collaboration, arXiv:1804.09378 | https://arxiv.org/abs/1804.09378 | HRD con post-AGB y nebulosas planetarias | Solo resumen, consultado el 2026-11-09 |
| S3 | Paxton et al., *MESA*, arXiv:1009.1622 | https://arxiv.org/abs/1009.1622 | Pulsos térmicos de AGB entre los casos demostrados | Solo resumen, consultado el 2026-11-09 |

Límites: S1–S3 solo resumen. La descripción cualitativa de pulsos térmicos y dragados es estándar, pero no se consultó ninguna cifra (duración de ciclos, masas dragadas, fuentes de neutrones); la solución de Poisson, el flujo estacionario y la conservación de masa se verifican numéricamente en el laboratorio.

## 12. Cómo ver la cadena

| `i` | `N_i` (Poisson, `τ = 2`) | `σ_i` | `N_i` (estacionario) |
|---|---|---|---|
| 0 | 0,135 | 1,0 | 1,00 |
| 1 | 0,271 | 0,5 | 2,00 |
| 2 | 0,271 | 2,0 | 0,50 |
| 3 | 0,180 | 0,1 | 10,0 |
| 4 | 0,090 | 1,5 | 0,67 |
| 5 | 0,036 | 0,8 | 1,25 |

Descripción larga: en Poisson, el máximo está cerca de `i = τ`; en el flujo estacionario, la abundancia es inversamente proporcional a la sección eficaz.

## 13. Ejemplo trabajado: ¿cuántos dragados para una estrella de carbono?

**Paso 1 · Datos.** Envoltura de `0,5 M☉` con `X_C = 0,003`, `X_O = 0,009`; cada pulso dragas `ΔM = 0,002 M☉` con `X_C,dr = 0,05`, `X_O,dr = 0,005` (sintéticos).

**Paso 2 · Estado inicial.** `m_C = 0,0015`, `m_O = 0,0045`; `C/O = (0,0015/12)/(0,0045/16) = 0,444`.

**Paso 3 · Tras `k` pulsos.** `m_C = 0,0015 + 10⁻⁴k`, `m_O = 0,0045 + 10⁻⁵k`.

**Paso 4 · Condición `C/O > 1`.** `(m_C/12)/(m_O/16) > 1` ⇒ `m_C > 0,75 m_O`: `0,0015 + 10⁻⁴k > 0,003375 + 7,5 × 10⁻⁶k` ⇒ `9,25 × 10⁻⁵ k > 1,875 × 10⁻³` ⇒ `k > 20,3`: el pulso 21 (el laboratorio también da 21).

**Paso 5 · Sentido.** Con estos valores sintéticos hacen falta unos veinte dragados. Es una demostración de la aritmética, no un resultado astrofísico.

## 14. Distintas formas de estudiar el proceso s

**Cadena local con secciones eficaces (esta clase):** analítica y didáctica. **Redes de reacciones con miles de reacciones:** las que se usan en modelos reales (S1). **Observaciones de abundancias superficiales:** el contraste observacional.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `N₂` de Poisson para `τ = 2`. *Pasos:* `τ² e^{−τ}/2!`.

<details><summary>Solución comentada</summary>

`4 × 0,13534/2 = 0,2707`.
</details>

**Ejercicio 2 · con una pista.** ¿Cuánto vale `N₁`? *Pista:* `τ e^{−τ}`.

<details><summary>Solución comentada</summary>

`2 × 0,13534 = 0,2707`: igual que `N₂` (los dos máximos coinciden cuando `τ` es entero).
</details>

**Ejercicio 3 · casi autónomo.** ¿Cuánto vale `N₀`?

<details><summary>Solución comentada</summary>

`e^{−2} = 0,1353`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** ¿Qué suman las abundancias de Poisson de todas las especies?

<details><summary>Solución comentada</summary>

`1`: la cadena conserva el número de núcleos (con 12 especies y `τ = 2` la suma es `0,99999…`).
</details>

**Ejercicio 5.** En el flujo estacionario, si `σ₃` se duplicara, ¿cuánto valdría `N₃`?

<details><summary>Solución comentada</summary>

`σ_iN_i` constante: `N₃` se divide por 2, a `5` (8.3).
</details>

**Ejercicio 6.** ¿Qué producto `σ_iN_i` esperas para todas las especies?

<details><summary>Solución comentada</summary>

`σ₀N₀ = 1` (laboratorio: `1,00000` en todas).
</details>

**Ejercicio 7.** Calcula la masa de carbono y de envoltura tras `40` pulsos.

<details><summary>Solución comentada</summary>

`m_C = 0,0015 + 40 × 0,002 × 0,05 = 0,0055 M☉`; `M_env = 0,5 + 40 × 0,002 = 0,58 M☉` (8.4).
</details>

**Ejercicio 8.** ¿Cuál es la fracción de masa de carbono de la envoltura a los 40 pulsos?

<details><summary>Solución comentada</summary>

`0,0055/0,58 = 0,00948`.
</details>

**Ejercicio 9 · transferencia.** ¿Por qué los núcleos con secciones eficaces pequeñas son los de mayor abundancia en el flujo estacionario?

<details><summary>Solución comentada</summary>

Porque `N_i ∝ 1/σ_i`: un núcleo que capta neutrones con dificultad se acumula antes de pasar al siguiente (8.3).
</details>

**Ejercicio 10 · transferencia.** Un compañero dice que «todos los elementos más pesados que el hierro vienen del proceso s». Responde con 8.5 y S1.

<details><summary>Solución comentada</summary>

S1 (resumen) atribuye al proceso s los enriquecimientos de elementos pesados en estrellas de masa baja e intermedia, pero no dice que sea la única vía; otros procesos (de captura rápida y explosivos) se tratan en otros bloques.
</details>

**Ejercicio 11 · transferencia.** Si observas una estrella AGB con `C/O > 1` y bandas moleculares de carbono, ¿qué proceso interior has comprobado?

<details><summary>Solución comentada</summary>

Que ha habido dragados de material procesado por la fusión de helio hasta la superficie (S1); la cifra de dragados no se deduce de una sola observación.
</details>

**Ejercicio 12 · integrador.** Elabora tu *ficha de la fase AGB*: resuelve la cadena de capturas para una exposición a tu elección, compara con Poisson, calcula el flujo estacionario con tus secciones, simula los dragados y señala tres cosas que el modelo omite.

<details><summary>Solución modelo</summary>

`τ = 2`: error `6 × 10⁻¹⁵`; estacionario con `σ = [1; 0,5; 2; 0,1; 1,5; 0,8]` ⇒ `σN = 1`; dragados: `C/O` supera 1 en el pulso 21; omitidos: decaimientos beta, ramificaciones, pérdida de masa. Todo sintético.
</details>

## 17. Laboratorio: capturas lentas y dragados

El script [proceso_s.py](proceso_s.py) integra la cadena con RK4 y **comprueba** que coincide con Poisson (`10⁻⁸`), integra hasta el estado estacionario y **comprueba** que `σ_iN_i` es constante (`10⁻⁴`), y simula `40` dragados **comprobando** la conservación exacta de la masa de carbono y de la envoltura (`10⁻¹²`).

**Datos:** ninguno observado; todos los valores **sintéticos**. **Predice antes de ejecutar:** ¿qué especie tendrá la mayor abundancia en el estado estacionario? (la de sección eficaz más pequeña, `σ₃`.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
cadena igual (tau = 2.0): error maximo frente a Poisson = 6.4e-15 ; maximo en N_2 = 0.2707
flujo estacionario: s0N0=1.00000  s1N1=1.00000  s2N2=1.00000  s3N3=1.00000  s4N4=1.00000  s5N5=1.00000
abundancias N_i = 1.000 2.000 0.500 10.000 0.667 1.250 (mayor abundancia donde la seccion es menor)
C/O inicial = 0.444 ; tras 40 pulsos C/O = 1.497 ; primer pulso con C/O > 1: 21
Pruebas superadas.
```

```bash
python programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/proceso_s.py
```

**Límites:** cadena lineal, sin decaimientos ni ramificaciones; valores sintéticos.

## 18. Errores frecuentes y cómo corregirlos

**Pensar que las abundancias s reflejan las abundancias solares.** Se corrige con el ejercicio 9: dependen de las secciones eficaces.

**Confundir `N_i` de Poisson con las estacionarias.** Se corrige con la tabla de la sección 12.

**Olvidar que el dragado también añade masa a la envoltura.** Se corrige con el ejercicio 7.

**Presentar valores sintéticos como astrofísicos.** Se corrige con la sección 10.

**Atribuir todo al proceso s.** Se corrige con el ejercicio 10.

## 19. Cómo sabrás que vas bien

Tras 8.2: ¿qué es `N_i`? Si dudas, ejercicios 1–3. Tras 8.3: ¿qué producto es constante? Ejercicio 6. Tras el laboratorio: ¿qué comprueba la conservación? (que los dragados no crean ni destruyen carbono).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de la fase AGB** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Pulso, dragado, proceso s | Explica el flujo estacionario |
| Cálculo | Sin unidades | Con errores | Poisson y `C/O` | Deduce el pulso crítico |
| Numérico | Sin comprobar | Un caso | Tres verificaciones | Explica las tolerancias |
| Fuentes | Sin fuente | Sin fecha | S1–S3 con fecha | Declara lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute ramificaciones |

**Condiciones críticas (no se compensan con promedio):** rotular todo valor numérico como sintético; no citar cifras de ciclos AGB sin fuente; citar solo lo consultado y decir que S1–S3 son resúmenes.

## 21. Ética, seguridad y límites

Clase educativa: no sustituye una red de nucleosíntesis con tasas medidas ni un modelo de AGB. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Las capturas lentas de neutrones siguen una distribución de Poisson si las secciones son iguales y un flujo con `σ_iN_i` constante si son distintas; los dragados llevan carbono a la superficie hasta superar `C/O = 1`. Queda una pregunta: ¿qué cambia cuando una estrella no está sola?

**Glosario español–inglés.** rama asintótica de gigantes · *asymptotic giant branch (AGB)*; pulso térmico · *thermal pulse*; dragado · *dredge-up*; proceso s · *s-process*; exposición de neutrones · *neutron exposure*; estrella de carbono · *carbon star*; nebulosa planetaria · *planetary nebula*.

**Continuidad.** [B24-C22](../B24-C22-evolucion-binaria-lobulo-de-roche-y-transferencia-de-masa/CLASE.md) reutiliza la pérdida y transferencia de masa para estudiar estrellas en sistemas binarios.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B24-C20 — Modelo simplificado de estructura estelar](../B24-C20-modelo-simplificado-de-estructura-estelar/CLASE.md) · [📚 Bloque B24](../../../tronco-comun/B24-fisica-y-evolucion-de-estrellas.md) · [Siguiente: B24-C22 — Evolución binaria: lóbulo de Roche y transferencia de masa →](../B24-C22-evolucion-binaria-lobulo-de-roche-y-transferencia-de-masa/CLASE.md)
<!-- /nav -->
