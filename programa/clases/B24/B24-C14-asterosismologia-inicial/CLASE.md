# B24-C14 — Asterosismología inicial

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B24](../../../tronco-comun/B24-fisica-y-evolucion-de-estrellas.md) · [← Anterior: B24-C13 — Estrellas variables](../B24-C13-estrellas-variables/CLASE.md) · [Siguiente: B24-C15 — Estrellas de baja masa →](../B24-C15-estrellas-de-baja-masa/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 14 del bloque B24. Nivel N3. En [C13](../B24-C13-estrellas-variables/CLASE.md) la estrella pulsaba con un gran periodo y gran amplitud. Aquí tratas las **oscilaciones pequeñas** que casi todas las estrellas con envoltura convectiva excitan continuamente, como las del Sol. Esas ondas sonoras viajan por el interior y llevan información de la densidad media. Usas las ondas ([B05-C12](../../B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md)), el análisis de Fourier ([B15](../../../tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md)) y las ecuaciones diferenciales (B11). El tratamiento avanzado de los interiores está en [B37](../../../tronco-comun/B37-interiores-estelares-y-asterosismologia.md).

## 2. Por qué esta clase existe

La asterosismología es la única manera de «ver» el interior de estrellas lejanas: da densidad media, masa y radio con una precisión que la fotometría y la espectroscopía no alcanzan, y distingue si una gigante quema hidrógeno en capa o helio en el núcleo. La decisión central: **dada la separación entre frecuencias de oscilación de una estrella, ¿qué densidad media tiene y qué masa se deduce si se conoce su radio?**

## 3. Lo que podrás hacer al terminar

1. Definir modo acústico, modo de gravedad, separación grande y resolución en frecuencia.
2. Resolver la ecuación de Lane–Emden y verificar el solver con soluciones analíticas.
3. Calcular la separación grande `Δν` de un modelo politrópico.
4. Usar la escala `Δν ∝ √ρ̄` para estimar la masa a partir del radio.
5. Calcular la resolución en frecuencia que da una serie temporal.
6. Distinguir gigantes por sus modos de gravedad.

La evidencia es la **ficha asterosísmica** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es la frecuencia de una onda y cómo se mide en `μHz`?
2. ¿Qué es la velocidad del sonido en un gas?
3. ¿Qué es una transformada de Fourier?
4. ¿Qué es la densidad media de una estrella?
5. ¿Qué es un politropo?

<details>
<summary>Ver respuestas</summary>

1. Ciclos por segundo; `1 μHz = 10⁻⁶ Hz`. 2. `c = √(γP/ρ)`. 3. La descomposición de una señal en frecuencias. 4. `M/(4πR³/3)`. 5. Un modelo con `P ∝ ρ^{1+1/n}`; se desarrolla en C20.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa B05-C12 y B15.

## 5. Un caso real: ¿cuánto oscila el Sol?

Las oscilaciones del Sol tienen una velocidad de unos `23,4 ± 1,4 cm/s` y una amplitud en luminosidad de `4,7 ± 0,3 ppm` a `550 nm` (S2, resumen). En el ejemplo conductor, un modelo politrópico de índice `n = 3` con la masa y el radio nominales da una separación grande `Δν = 123,6 μHz`: es un **modelo**, no la separación observada del Sol. Chaplin y Miglio revisan los resultados de Kepler y CoRoT con oscilaciones tipo solar en estrellas de tipo solar y gigantes rojas (S1, resumen).

## 6. Vocabulario

Un **modo acústico** (modo p) es una onda sonora estacionaria cuyo restablecimiento es la presión. Un **modo de gravedad** (modo g) es una onda con la flotabilidad como fuerza restauradora. La **separación grande** `Δν` es la distancia en frecuencia entre modos consecutivos del mismo grado; en la aproximación de rayos `Δν = 1/(2 τ)` con `τ = ∫₀ᴿ dr/c` el tiempo que tarda el sonido en cruzar el radio. La **velocidad del sonido** es `c = √(γP/ρ)`. La **ecuación de Lane–Emden** describe un politropo: `θ'' + 2θ'/ξ + θⁿ = 0`. La **resolución en frecuencia** de una serie de duración `T` es `1/T`. La **densidad media** es `ρ̄ = M/(4πR³/3)`.

## 7. Modelo mental: un tubo de órgano esférico

Un tubo de órgano tiene frecuencias separadas por `c/(2L)`; una estrella, por `1/(2τ)`, con `τ` el tiempo de cruce. Un tubo más corto o con sonido más rápido suena más agudo, y la estrella densa tiene `Δν` grande.

```mermaid
flowchart LR
    A["Modelo (M, R)"] --> B["c(r) del interior"]
    B --> C["τ = ∫ dr / c"]
    C --> D["Δν = 1 / (2τ)"]
    D --> E["Δν ∝ √ρ̄:<br/>estima M si se conoce R"]
```

*Descripción textual:* el perfil de velocidad del sonido da el tiempo de cruce, cuyo inverso es la separación grande; esta escala con la raíz de la densidad media permite estimar masas.

Analogía: el tubo de órgano. Límite: una estrella no es un tubo uniforme, y el modelo no incluye la superficie ni la rotación.

## 8. La explicación, paso a paso

### 8.1 Solver de Lane–Emden

Un politropo de índice `n` obedece `θ'' + 2θ'/ξ + θⁿ = 0` con `θ(0) = 1` y `θ'(0) = 0`; `θ` cae a cero en `ξ₁`. El laboratorio lo integra con Runge–Kutta y lo valida con casos exactos: para `n = 0`, `ξ₁ = √6 = 2,449 490`; para `n = 1`, `θ = sen ξ/ξ` y `ξ₁ = π = 3,141 593`. Para `n = 3`, `ξ₁ = 6,89685`.

### 8.2 Velocidad del sonido en el politropo

Con `ρ = ρ_c θⁿ` y `P = P_c θ^{n+1}`, `c² = γP/ρ = γ (P_c/ρ_c) θ`. La escala de longitud es `a² = (n+1)P_c/(4πGρ_c²)` y `r = aξ`. La densidad central se obtiene de la masa y el radio: `ρ_c = ρ̄ ξ₁³/(3|ξ₁²θ'(ξ₁)|)`.

### 8.3 La separación grande

El tiempo de cruce es `τ = a ∫₀^{ξ₁} dξ/√(γ(P_c/ρ_c)θ)`. La integral converge porque cerca de la superficie `θ ∼ (ξ₁−ξ)`. Con `γ = 5/3`, `n = 3`, la masa y el radio nominales, el laboratorio da `Δν = 123,6 μHz`, lo que equivale a `τ = 1/(2Δν) = 4045 s`. La escala homóloga `Δν ∝ √(M/R³)` se cumple con exactitud en el código: para `M = 2 M☉`, `R = 1,5 R☉` da `95,2 μHz` y la escala predice lo mismo.

### 8.4 Masa a partir de Δν

Como `Δν ∝ √ρ̄`, `ρ̄/ρ̄_ref = (Δν/Δν_ref)²`. Con `R` conocido de otro modo (por ejemplo, de `L` y `T_ef`, C03), `M = ρ̄ (4π/3) R³`. En el modelo: una estrella con `R = 1,5 R☉` y `Δν = 95,2 μHz` tiene `ρ̄/ρ̄_☉ = (95,2/123,6)² = 0,593` y `M = 0,593 × 1,5³ = 2,0 M☉`. Una gigante de `1,3 M☉` y `11 R☉` (ilustrativa) tiene `Δν = 3,86 μHz`.

### 8.5 Resolución y gravedad

Para resolver dos frecuencias separadas por `δν`, la serie debe durar `T ≳ 1/δν`; una serie de un año (`3,156 × 10⁷ s`) resuelve `0,03 μHz`. En las gigantes rojas los modos g mixtos tienen espaciados de periodo de unos `50 s` en estrellas con hidrógeno en capa y de `100` a `300 s` en estrellas con helio en el núcleo (S3, resumen), lo que separa ambas fases.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `Δν` | separación grande | `μHz` | `123,6` (politropo, **modelo**) |
| `τ` | tiempo de cruce acústico | s | `4045` |
| `ξ₁` | primera raíz de `θ` | — | `6,89685` (`n = 3`) |
| `γ`, `n` | índice adiabático; índice politrópico | — | `5/3`; `3` |
| `ρ̄` | densidad media | `kg m⁻³` | `1410` (Sol) |
| `ΔΠ` | espaciado de periodo de modos g | s | ~`50`; `100–300` (S3) |

## 10. Convenciones y referencias

Aproximación de rayos; gas adiabático ideal; el politropo `n = 3` es un **modelo** y no reproduce la estructura solar real; no se compara `Δν` con un valor observado del Sol porque no se consultó. Las constantes `G`, `GM☉`, `R☉` son nominales.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | Chaplin y Miglio, *Asteroseismology of Solar-Type and Red-Giant Stars*, arXiv:1303.1957 | https://arxiv.org/abs/1303.1957 | Oscilaciones tipo solar; resultados de Kepler y CoRoT | Solo resumen, consultado el 2026-11-09 |
| S2 | Kjeldsen y Bedding, *Amplitudes of Stellar Oscillations*, arXiv:astro-ph/9403015 | https://arxiv.org/abs/astro-ph/9403015 | Velocidad solar `23,4 ± 1,4 cm/s`; amplitud `4,7 ± 0,3 ppm` a 550 nm | Solo resumen, consultado el 2026-11-09 |
| S3 | Bedding et al., arXiv:1103.5805 | https://arxiv.org/abs/1103.5805 | Espaciado de periodo: ~50 s (H en capa) y 100–300 s (He en núcleo) | Solo resumen, consultado el 2026-11-09 |
| S4 | Mamajek et al., *IAU 2015 Resolution B3*, arXiv:1510.07674 | https://arxiv.org/abs/1510.07674 | `GM☉`, `R☉` nominales | Texto del PDF extraído el 2026-11-09 |

Límites: S1–S3 solo resumen; `G` de NIST (2022); la ecuación de Lane–Emden y la aproximación de rayos son resultados estándar verificados con soluciones exactas.

## 12. Cómo ver la escala

| Estrella (modelo) | `ρ̄/ρ̄☉` | `Δν` (μHz) |
|---|---|---|
| Politropo solar | 1 | 123,6 |
| `2 M☉`, `1,5 R☉` | 0,593 | 95,2 |
| Gigante `1,3 M☉`, `11 R☉` | `9,8 × 10⁻⁴` | 3,86 |

Descripción larga: las estrellas poco densas (las gigantes) tienen separaciones muy pequeñas; la escala va con la raíz de la densidad media.

## 13. Ejemplo trabajado: la masa de una estrella con Δν

**Paso 1 · Datos.** `Δν = 95,2 μHz` (modelo) y `R = 1,5 R☉` por otra vía.

**Paso 2 · Densidad.** `ρ̄/ρ̄☉ = (95,2/123,6)² = 0,593`.

**Paso 3 · Masa.** `M = 0,593 × 1,5³ = 2,00 M☉`.

**Paso 4 · Sentido.** Es el valor con que se generó el dato, así que se cierra el ciclo; en una observación real, la incertidumbre de `R` se propaga al cubo en `M`.

## 14. Distintas formas de pesar una estrella

**Binaria eclipsante:** masa dinámica. **Isócrona + color (C19):** indirecta. **Asterosismología:** `Δν` y la frecuencia de máxima potencia dan densidad y gravedad. Se combinan para validar.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `τ` a partir de `Δν = 123,6 μHz`. *Pasos:* `τ = 1/(2Δν)`.

<details><summary>Solución comentada</summary>

`1/(2 × 123,6 × 10⁻⁶) = 4045 s = 67,4 min`.
</details>

**Ejercicio 2 · con una pista.** Calcula `Δν` de la gigante con `ρ̄/ρ̄☉ = 9,77 × 10⁻⁴`. *Pista:* `√ρ̄`.

<details><summary>Solución comentada</summary>

`√(9,77 × 10⁻⁴) = 0,03126`; `0,03126 × 123,6 = 3,86 μHz`.
</details>

**Ejercicio 3 · casi autónomo.** Calcula la duración mínima para resolver `0,1 μHz`.

<details><summary>Solución comentada</summary>

`T = 1/(10⁻⁷ Hz) = 10⁷ s = 116 días`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** ¿Cuánto vale la resolución de una serie de un año?

<details><summary>Solución comentada</summary>

`1/3,156 × 10⁷ s = 3,17 × 10⁻⁸ Hz = 0,032 μHz`.
</details>

**Ejercicio 5.** Si `R` se duplica con la misma masa, ¿cómo cambia `Δν`?

<details><summary>Solución comentada</summary>

`Δν ∝ R^{−3/2}`: se divide por `2^{3/2} = 2,83`.
</details>

**Ejercicio 6.** Si la masa se cuadruplica con el mismo radio, ¿cómo cambia `Δν`?

<details><summary>Solución comentada</summary>

`Δν ∝ M^{1/2}`: se duplica.
</details>

**Ejercicio 7.** ¿Qué espaciado de periodo distingue a las gigantes con helio en el núcleo?

<details><summary>Solución comentada</summary>

`100–300 s`, frente a ~`50 s` para las de hidrógeno en capa (S3).
</details>

**Ejercicio 8.** ¿Cuál es la velocidad solar de oscilación en m/s?

<details><summary>Solución comentada</summary>

`23,4 cm/s = 0,234 m/s` (S2).
</details>

**Ejercicio 9 · transferencia.** Una estrella tiene `Δν = 61,8 μHz` y `R = 2 R☉`. ¿Qué masa tiene (modelo)?

<details><summary>Solución comentada</summary>

`ρ̄/ρ̄☉ = (61,8/123,6)² = 0,25`; `M = 0,25 × 8 = 2,0 M☉`.
</details>

**Ejercicio 10 · transferencia.** Un compañero dice que «se oye el sonido de las estrellas». Responde con 8.3.

<details><summary>Solución comentada</summary>

No hay medio que lleve el sonido hasta nosotros: las ondas viajan dentro de la estrella y modulan su brillo y su velocidad superficial (S2); lo que se mide son esas variaciones, y se pueden convertir a audio con fines de divulgación.
</details>

**Ejercicio 11 · transferencia.** ¿Por qué ayudan las observaciones continuas de meses o años?

<details><summary>Solución comentada</summary>

Porque la resolución es `1/T`: sin una serie larga no se separan los modos (8.5); Kepler y CoRoT lo lograron desde el espacio (S1).
</details>

**Ejercicio 12 · integrador.** Elabora tu *ficha asterosísmica*: valida el solver con `n = 0` y `n = 1`, calcula `Δν` de un politropo para una masa y radio a tu elección, estima la masa a partir de `Δν` y `R`, da la resolución de una serie de 90 días y nombra dos límites.

<details><summary>Solución modelo</summary>

`ξ₁ = 2,449 5` y `3,141 6`; para `M = 2 M☉`, `R = 1,5 R☉`: `Δν = 95,2 μHz`, recupera `2,0 M☉`; 90 días: `0,129 μHz`; límites: politropo y rayos.
</details>

## 17. Laboratorio: Lane–Emden y separación grande

El script [sismologia.py](sismologia.py) integra Lane–Emden con RK4 y **comprueba** que `n = 1` da `ξ₁ = π` (`10⁻⁶`) y `θ = sen ξ/ξ` (`10⁻⁹`) y que `n = 0` da `√6`; calcula `Δν` del politropo `n = 3` y **comprueba** que la escala `Δν ∝ √(M/R³)` se cumple (`10⁻⁹`).

**Datos:** `GM☉`, `R☉` de la IAU; `G` de NIST; modelo **politrópico**, no la estructura solar real. **Predice antes de ejecutar:** ¿qué `Δν` esperas para una estrella 2 veces más masiva y 1,5 veces mayor que el Sol? (menor que el solar.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
solver: n=1 xi1 = 3.141593 (pi = 3.141593) ; n=0 xi1 = 2.449490 ; n=3 xi1 = 6.89685
politropo n=3 'solar': Delta nu = 123.6 uHz
M=2, R=1.5: Delta nu = 95.2 uHz ; esperado por escala = 95.2 uHz
gigante roja (M=1.3, R=11, ilustrativa): Delta nu = 3.86 uHz ; densidad media relativa = 9.77e-04
Pruebas superadas.
```

```bash
python programa/clases/B24/B24-C14-asterosismologia-inicial/sismologia.py
```

**Límites:** un solo politropo, aproximación de rayos, sin superficie ni rotación; el resultado solar es de modelo.

## 18. Errores frecuentes y cómo corregirlos

**Tomar la `Δν` del politropo como la observada.** Se corrige con la sección 10.

**Olvidar que `Δν ∝ √ρ̄`.** Se corrige con los ejercicios 5 y 6.

**Confundir resolución con precisión.** Se corrige con los ejercicios 3 y 4.

**Pensar que se oye el sonido.** Se corrige con el ejercicio 10.

**Propagar mal el radio en la masa.** Se corrige con la sección 13 (va al cubo).

## 19. Cómo sabrás que vas bien

Tras 8.3: ¿qué es `Δν`? Si dudas, ejercicio 1. Tras 8.4: ¿cómo se obtiene la masa? Ejercicio 9. Tras el laboratorio: ¿qué verifica el caso `n = 1`? (que el solver reproduce la solución analítica).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha asterosísmica** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Modos, `Δν`, resolución | Distingue p y g |
| Cálculo | Sin unidades | Con errores | `Δν` y masa | Propaga `R` al cubo |
| Numérico | Sin comprobar | Un caso | Solver validado | Explica la integral cerca de la superficie |
| Fuentes | Sin fuente | Sin fecha | S1–S4 con fecha | Declara resúmenes |
| Límites | No los nombra | Uno | Tres | Discute rotación y superficie |

**Condiciones críticas (no se compensan con promedio):** rotular `Δν = 123,6 μHz` como de modelo; no comparar con valores no consultados; citar solo lo consultado y decir que S1–S3 son resúmenes.

## 21. Ética, seguridad y límites

Clase educativa: no sustituye un análisis de frecuencias con datos reales ni un modelo de estructura detallado. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Las oscilaciones tienen una separación `Δν ∝ √ρ̄` que, con el radio, da la masa; el solver de Lane–Emden se valida con soluciones exactas y la serie temporal fija la resolución. Queda una pregunta: ¿qué camino sigue una estrella de baja masa a lo largo de su vida?

**Glosario español–inglés.** asterosismología · *asteroseismology*; modo acústico · *p mode*; modo de gravedad · *g mode*; separación grande · *large separation*; ecuación de Lane–Emden · *Lane–Emden equation*; resolución en frecuencia · *frequency resolution*; aproximación de rayos · *ray approximation*.

**Continuidad.** [B24-C15](../B24-C15-estrellas-de-baja-masa/CLASE.md) reutiliza la masa y la luminosidad para estudiar la vida de las estrellas de baja masa.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B24-C13 — Estrellas variables](../B24-C13-estrellas-variables/CLASE.md) · [📚 Bloque B24](../../../tronco-comun/B24-fisica-y-evolucion-de-estrellas.md) · [Siguiente: B24-C15 — Estrellas de baja masa →](../B24-C15-estrellas-de-baja-masa/CLASE.md)
<!-- /nav -->
