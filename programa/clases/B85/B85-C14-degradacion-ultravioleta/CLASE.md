# B85-C14 — Degradación ultravioleta

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B85](../../../tronco-comun/B85-gestion-termica-y-entorno-espacial.md) · [← Anterior: B85-C13 — Efectos de oxígeno atómico](../B85-C13-efectos-de-oxigeno-atomico/CLASE.md) · [Siguiente: B85-C15 — Electrificación superficial →](../B85-C15-electrificacion-superficial/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 14 del bloque B85. Nivel N3. La radiación ultravioleta del Sol oscurece los recubrimientos: su absortividad `α` crece con las horas de sol equivalente y tiende a saturar, y con ella sube la temperatura. Aquí generas datos sintéticos de `α` frente a la exposición, los ajustas con una ley saturante, extrapolas a cinco años y calculas el efecto en la temperatura. Los datos y la ley son sintéticos; solo se consultó la advertencia de NASA sobre el oscurecimiento.

## 2. Por qué esta clase existe

Un recubrimiento que cumple al inicio puede salirse del intervalo con la exposición. La decisión central: **¿cuánto sube `α` y cuánto sube la temperatura al final de la misión, y qué incertidumbre trae el ajuste?** La decisión central: **¿cuánto sube `α` y cuánto sube la temperatura al final de la misión, y qué incertidumbre trae el ajuste?**

## 3. Lo que podrás hacer al terminar

1. Plantear una ley de degradación saturante `α(ESH)`.
2. Ajustar `Δα_max` y `E₀` a datos sintéticos por mínimos cuadrados.
3. Comparar el ajuste con los parámetros verdaderos del generador.
4. Extrapolar `α` a cinco años y calcular el aumento de temperatura.
5. Calcular las horas para el 90 % del cambio.
6. Separar lo consultado (advertencia de NASA) de lo sintético (datos y ley).

La evidencia es la **ficha de degradación ultravioleta de un recubrimiento** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué son las horas de sol equivalente (ESH)?
2. ¿Qué es una ley saturante?
3. ¿Qué es el ajuste por mínimos cuadrados?
4. ¿Qué es el RMS?
5. ¿Qué es un dato sintético?

<details>
<summary>Ver respuestas</summary>

1. Las horas de exposición normalizadas a la intensidad del Sol. 2. Una que crece y tiende a un valor máximo. 3. Elegir parámetros que minimizan la suma de los residuos al cuadrado. 4. La raíz de la media de los residuos al cuadrado. 5. Un dato generado para el ejemplo, no medido.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Un recubrimiento ilustrativo con `α₀ = 0,20` sube a `0,381` tras cinco años (`25 000 ESH`) y su placa al Sol pasa de `270,25 K` a `317,42 K` (`+47,18 K`). El ajuste recupera `Δα_max = 0,1807` y `E₀ = 1515 h` frente a los verdaderos `0,18` y `1500 h`. Es el **ejemplo conductor**. Datos **sintéticos**.

## 6. Vocabulario

La **ley saturante** `α(ESH) = α₀ + Δα_max (1 − e^(−ESH/E₀))`. `E₀` es la **exposición característica**. El **ajuste** busca `E₀` y, para cada `E₀`, resuelve `Δα_max` por mínimos cuadrados lineales. El **RMS** mide la calidad. La **saturación** `α₀ + Δα_max` es el valor límite.

## 7. Modelo mental

```mermaid
flowchart LR
    ESH["Horas de sol equivalente"] --> A["α(ESH) = α0 + Δα (1 − e^(−ESH/E0))"]
    D["Datos sintéticos + ruido"] --> AJ["Ajuste: Δα, E0"]
    AJ --> A
    A --> T["T = (α S / (ε σ))^¼"]
    T --> V["¿Dentro del intervalo al final?"]
```

*Descripción textual:* los datos sintéticos permiten ajustar los parámetros de la ley saturante; con ella se extrapola `α` y se calcula la temperatura al final de la misión.

Analogía: una tela que se destiñe al sol: al principio cambia rápido y luego se estabiliza. Límite: la ley de la clase es una forma convencional y los parámetros del ajuste dependen del rango de datos; una extrapolación lejos del rango es especulativa.

## 8. La explicación, paso a paso

### 8.1 Los datos

Datos sintéticos con ruido gaussiano de `0,004` y semilla `20261110` a partir de `α₀ = 0,20`, `Δα = 0,18`, `E₀ = 1500 h`:

| ESH (h) | `α` medida |
|---|---|
| 0 | 0,1992 |
| 308 | 0,2357 |
| 615 | 0,2640 |
| 923 | 0,2773 |
| 1231 | 0,3002 |
| 1538 | 0,3116 |
| 1846 | 0,3289 |
| 2154 | 0,3404 |
| 2462 | 0,3456 |
| 2769 | 0,3551 |
| 3077 | 0,3521 |
| 3385 | 0,3598 |
| 3692 | 0,3682 |
| 4000 | 0,3663 |

### 8.2 Ajuste

Se recorre `E₀` entre `205` y `4195 h` y, para cada valor, `Δα_max = Σ g y/Σ g²` con `g = 1 − e^(−ESH/E₀)`. El mínimo da `Δα_max = 0,1807`, `E₀ = 1515 h` y `RMS = 0,0030`, cerca de los verdaderos (`0,18`; `1500 h`) y del ruido sembrado.

### 8.3 Extrapolación y temperatura

Con `5000 ESH` por año (ilustrativo), a cinco años `α = 0,3807` (verdadero `0,3800`), casi la saturación `0,3807`. La placa con `ε = 0,9` pasa de `270,25` a `317,42 K`.

### 8.4 Qué mirar

El 90 % del cambio ocurre en `3488 h`, es decir `0,70` años: lo que importa para el caso caliente es la saturación, no la tasa inicial. La incertidumbre de `Δα_max` se traslada a `T`: un error de `0,01` en `Δα` mueve `T` unos `2,11 K`. NASA indica que los recubrimientos se oscurecen en órbita y que el caso caliente debe usar valores de fin de vida.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `α₀` | absortividad inicial | — | 0,20 (sintética) |
| `Δα_max` | aumento máximo | — | 0,1807 (ajustado) |
| `E₀` | exposición característica | h | 1515 (ajustada) |
| ESH | horas de sol equivalente | h | 0–4000 (datos) |
| RMS | error del ajuste | — | 0,0030 |
| `T` | temperatura de la placa | K | 270,25 → 317,42 |

## 10. Convenciones y referencias

`σ` y `S₀` consultadas. Ley saturante, parámetros y ruido sintéticos (semilla `20261110`); `5000 ESH/año` ilustrativo; placa de `1 m²`, una cara al Sol, `ε = 0,9`, reverso aislado.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NIST, CODATA 2022, Stefan–Boltzmann constant — https://physics.nist.gov/cgi-bin/cuu/Value?sigma (consultada 2026-11-10) | valor de `σ` | `σ` del balance | Consultada |
| S2 | NASA/NSSDC, Earth Fact Sheet — https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html (consultada 2026-11-10) | ficha completa | `S₀ = 1361,0 W/m²` | Consultada |
| S3 | NASA, State-of-the-Art of Small Spacecraft Technology, capítulo Thermal Control — https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/ (consultada 2026-11-10) | sección de coatings | los coatings se oscurecen en órbita; para el caso caliente se usan valores de fin de vida | Consultada |
| — | Ley exponencial saturante y mínimos cuadrados con parámetro lineal | — | las verifica el laboratorio con una segunda vía | No consultada en una fuente concreta |

Límites: los datos de degradación y las ESH por año son sintéticos e ilustrativos; no representan ningún material; la extrapolación depende de la ley supuesta; no se modela el efecto de partículas ni de la contaminación.

## 12. Cómo ver el resultado

| Magnitud | Valor |
|---|---|
| `Δα_max` ajustado | 0,1807 |
| `E₀` ajustado | 1515 h |
| RMS | 0,0030 |
| `α` a 5 años | 0,3807 |
| `ΔT` a 5 años | +47,18 K |

Descripción larga: el ajuste recupera los parámetros verdaderos dentro del ruido; el aumento de `α` eleva 47 K la temperatura de equilibrio.

## 13. Ejemplo trabajado

**Paso 1 · Saturación.** `α_sat = 0,20 + 0,1807 = 0,3807`.

**Paso 2 · Temperatura.** `T = (α S₀/(ε σ))^(1/4) = 317,42 K`.

**Paso 3 · Aumento.** `317,42 − 270,25 = 47,18 K`.

## 14. Distintas formas de describir el problema

**Por ley:** `α(ESH)`. **Por ajuste:** `Δα`, `E₀`. **Por saturación:** `α₀ + Δα`. **Por temperatura:** `T(α)`.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `α` a `1500 ESH` con los parámetros verdaderos. *Pasos:* `0,2 + 0,18(1 − e⁻¹)`.

<details><summary>Solución comentada</summary>

`0,3138`.
</details>

**Ejercicio 2 · con una pista.** Predice si `α` a `3000 ESH` supera `0,35`. *Pista:* `1 − e⁻²`.

<details><summary>Solución comentada</summary>

`α = 0,3556`: sí.
</details>

**Ejercicio 3 · casi autónomo.** ¿Por qué el RMS del ajuste es cercano al ruido sembrado `0,004`? Piensa en qué mide.

<details><summary>Solución comentada</summary>

Los residuos del ajuste son básicamente el ruido; el modelo describe los datos.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** ¿Cuántas ESH dan el 50 % del cambio?

<details><summary>Solución comentada</summary>

`E₀ ln 2 = 1050 h`.
</details>

**Ejercicio 5 · autónomo.** ¿Cuántos años dan el 99 % del cambio?

<details><summary>Solución comentada</summary>

`E₀ ln 100/5000 = 1,40` años.
</details>

**Ejercicio 6 · autónomo.** Calcula `T` si `α = 0,30` y `ε = 0,9`.

<details><summary>Solución comentada</summary>

`299,08 K`.
</details>

**Ejercicio 7 · autónomo.** Calcula `dT/dα` aproximado a `α = 0,38`.

<details><summary>Solución comentada</summary>

`T/(4α) = 208,7 K` por unidad de `α`; `0,01` equivale a `2,09 K`.
</details>

**Ejercicio 8 · autónomo.** Si la exposición anual es `2500 ESH`, ¿cuál es `α` a 5 años?

<details><summary>Solución comentada</summary>

`0,3806`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un ensayo UV acelerado da `α` a `1000 ESH`. ¿Se puede extrapolar a 10 años?

<details><summary>Solución comentada</summary>

No con un solo punto: hace falta cubrir el rango y validar la aceleración respecto de la exposición en órbita.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** Una mejor protección baja `Δα` a `0,10`. ¿Qué efecto en `T`?

<details><summary>Solución comentada</summary>

`α_sat = 0,30`; `T = 299,08 K`, `18,35 K` menos.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** Un colega presenta `47 K` como «el calentamiento observado del satélite». ¿Qué corriges?

<details><summary>Solución comentada</summary>

Es un cálculo con datos sintéticos, no una observación; no existe un satélite medido en esta clase.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de degradación ultravioleta de un recubrimiento*: datos sintéticos, parámetros ajustados con RMS, `α` y `T` a 5 años, horas para el 90 % y lista de lo consultado y sintético.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: ajuste de la degradación ultravioleta

El script [degradacion_uv.py](degradacion_uv.py) genera datos sintéticos con ruido, ajusta `Δα_max` y `E₀`, extrapola a cinco años y calcula la temperatura (**comprueba** `Δα_max` a 0,01, `E₀` a 15 % y RMS < 0,008).

**Datos:** `σ` y `S₀` consultadas; datos, ley, ruido, semilla y ESH por año **sintéticos e ilustrativos**. **Predice antes de ejecutar:** ¿cuánto sube `T` en cinco años? (unos 47 K.) **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Ley ILUSTRATIVA: alfa = 0.2 + 0.18 (1 - exp(-ESH/1500)) ; datos SINTETICOS con ruido gaussiano 0.004 (semilla 20261110)
ESH [h]   alfa medida
       0   0.1992
     308   0.2357
     615   0.2640
     923   0.2773
    1231   0.3002
    1538   0.3116
    1846   0.3289
    2154   0.3404
    2462   0.3456
    2769   0.3551
    3077   0.3521
    3385   0.3598
    3692   0.3682
    4000   0.3663
Ajuste: delta_alfa_max = 0.1807 (verdadero 0.18) ; E0 = 1515 h (verdadero 1500) ; RMS = 0.0030
alfa tras 5 anios (25000 ESH): ajustada 0.3807 ; verdadera 0.3800 ; saturacion 0.3807
Placa al Sol (eps = 0.9): BOL 270.25 K ; 5 anios 317.42 K (+47.18 K) ; saturada 317.42 K
Horas de sol equivalente para el 90 % del cambio: 3488 h = 0.70 anios
Pruebas superadas.
```

```bash
python programa/clases/B85/B85-C14-degradacion-ultravioleta/degradacion_uv.py
```

**Límites:** ley saturante convencional; rango de datos hasta `4000 ESH`; la extrapolación a 25 000 ESH es especulativa.

## 18. Errores frecuentes y cómo corregirlos

**Extrapolar lejos del rango de datos.** la ley supuesta decide (8.4)

**Usar la tasa inicial para el caso caliente.** manda la saturación (8.4)

**Tomar el ajuste como la verdad.** `Δα` tiene incertidumbre (8.4)

**Presentar datos sintéticos como medidos.** se corrige con la sección 10

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué `α` esperabas a cinco años y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de degradación ultravioleta de un recubrimiento** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Ajusta y calcula `α` y `T` | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas con unidades | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con una segunda vía | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo ilustrativo y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular los datos y la ley como sintéticos; no presentar el ajuste como medición de una misión; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y sus datos son sintéticos o ilustrativos; ningún resultado describe una nave real, ni sustituye a los estándares de proyecto, a la verificación con datos de misión ni a una revisión disciplinar. Los valores de este texto no son requisitos de ningún proyecto. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Con datos sintéticos, `α` sube de `0,20` a `0,38` en cinco años y la placa se calienta `47 K`. Queda una pregunta: ¿qué pasa cuando las superficies se cargan eléctricamente?

**Glosario español–inglés.** degradación ultravioleta · *UV degradation*; horas de sol equivalente · *equivalent sun hours*; ajuste · *fit*; saturación · *saturation*; absortividad · *absorptivity*.

**Continuidad.** [B85-C15](../B85-C15-electrificacion-superficial/CLASE.md) estudia la electrificación superficial.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B85-C13 — Efectos de oxígeno atómico](../B85-C13-efectos-de-oxigeno-atomico/CLASE.md) · [📚 Bloque B85](../../../tronco-comun/B85-gestion-termica-y-entorno-espacial.md) · [Siguiente: B85-C15 — Electrificación superficial →](../B85-C15-electrificacion-superficial/CLASE.md)
<!-- /nav -->
