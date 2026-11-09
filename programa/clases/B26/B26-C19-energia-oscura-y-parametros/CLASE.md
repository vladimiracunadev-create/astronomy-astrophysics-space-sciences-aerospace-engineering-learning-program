# B26-C19 — Energía oscura y parámetros

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B26](../../../tronco-comun/B26-relatividad-y-cosmologia.md) · [← Anterior: B26-C18 — Materia oscura y evidencias](../B26-C18-materia-oscura-y-evidencias/CLASE.md) · [Siguiente: B26-C20 — Límites observacionales de modelos cosmológicos →](../B26-C20-limites-observacionales-de-modelos-cosmologicos/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 19 del bloque B26. Nivel N3. En [C13](../B26-C13-modelo-flrw-relatividad-y-cosmologia/CLASE.md) apareció una constante cosmológica que acelera la expansión. Aquí ves cómo se manifiesta en la observación: **la distancia de luminosidad**, que determina cuán débiles se ven las supernovas lejanas. Calculas `D_L(z)` en tres modelos, verificas con soluciones cerradas y conviertes las diferencias en magnitudes. Usas integración numérica ([B11](../../../tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md)), logaritmos y magnitudes ([B24-C03](../../B24/B24-C03-diagrama-de-hertzsprung-russell/CLASE.md)) y el modelo FLRW de C13.

## 2. Por qué esta clase existe

La aceleración cósmica se descubrió porque las supernovas Ia lejanas aparecían más débiles de lo esperado. Para reproducir ese razonamiento hay que saber calcular la distancia de luminosidad y ver cuánto cambia con el contenido del universo. La decisión central: **¿cuánto más lejos se ve una supernova en un universo con constante cosmológica que en uno abierto sin ella y cuánto vale ese cambio en magnitudes?**

## 3. Lo que podrás hacer al terminar

1. Definir distancia de luminosidad y módulo de distancia.
2. Calcular `D_L(z)` por cuadratura en ΛCDM, Einstein–de Sitter y un modelo abierto.
3. Verificar el código con las soluciones cerradas de EdS y de Milne.
4. Convertir el cociente de distancias en diferencia de magnitud.
5. Evaluar la sensibilidad de `D_L` a `Ω_m`.
6. Leer una restricción publicada sobre la ecuación de estado `w`.

La evidencia es la **tabla de distancias de luminosidad** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es el módulo de distancia?
2. ¿Qué es `E(z) = H/H₀`?
3. ¿Qué es una cuadratura?
4. ¿Qué significa «universo abierto»?
5. ¿Cuántos Mpc tiene `c/H₀`?

<details>
<summary>Ver respuestas</summary>

1. `μ = 5 log₁₀(D_L/10 pc)`. 2. `√(Ω_m(1+z)³ + Ω_k(1+z)² + Ω_Λ)`. 3. Una integral calculada numéricamente. 4. Curvatura negativa: `Ω_k > 0`. 5. `4448 Mpc` con `H₀ = 67,4`.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa C13 y B24-C03.

## 5. Un caso real: supernovas 10 a 15 % más lejos

Riess y colaboradores midieron 10 supernovas Ia a `0,16 < z < 0,62` y las combinaron con otras 40: las distantes aparecían, en promedio, un `10` a `15 %` más lejos de lo esperado en un universo de baja densidad sin constante cosmológica, lo que favorecía una constante cosmológica positiva (S3, resumen). Perlmutter y colaboradores, con 42 supernovas a `0,18 < z < 0,83`, encontraron `Ω_m ≈ 0,28` en un universo plano y la constante positiva al `99 %` (S4, resumen). Es el **ejemplo conductor**: el laboratorio reproduce el orden de magnitud, `+9,9 %` a `z = 0,5` y `+11,5 %` a `z = 1`.

## 6. Vocabulario

La **distancia de luminosidad** `D_L` define cuánto flujo llega: `F = L/(4πD_L²)`. La **distancia comóvil** es `D_C = (c/H₀)∫dz/E`. La **distancia transversal** `D_M` coincide con `D_C` si no hay curvatura y es `(c/H₀)sinh(√Ω_k D_C H₀/c)/√Ω_k` si `Ω_k > 0`. `D_L = (1+z)D_M`. El **módulo de distancia** `μ = 5 log₁₀(D_L/10 pc)`. El **modelo de Milne** es un universo vacío (`Ω_m = Ω_Λ = 0`). La **ecuación de estado** `w = p/ρ` de la energía oscura vale `−1` para una constante cosmológica. Las **supernovas Ia** son velas estándar tras la calibración. `w₀`, `w_a` parametrizan `w(a)`.

## 7. Modelo mental: la luz que recorre más camino

Con constante cosmológica el universo se expandió más rápido en el pasado reciente; la luz de una supernova a un `z` dado recorrió más espacio y llega más tenue.

```mermaid
flowchart LR
    M["Modelo (Ω_m, Ω_Λ, Ω_k)"] --> E["E(z)"]
    E --> DC["D_C = (c/H₀) ∫ dz/E"]
    DC --> DL["D_L = (1+z) D_M"]
    DL --> MU["μ = 5 log₁₀(D_L/10 pc)"]
    MU --> C["Δμ entre modelos"]
```

*Descripción textual:* el modelo fija `E(z)`; la integral da la distancia comóvil; con la curvatura se obtiene `D_M`, luego `D_L` y el módulo de distancia; la diferencia entre modelos se lee en magnitudes.

Analogía: dos trayectos con distinta velocidad del suelo. Límite: no es movimiento sobre el espacio sino expansión del espacio.

## 8. La explicación, paso a paso

### 8.1 Cálculo por cuadratura

El laboratorio integra con Simpson `D_C` para `Ω_m`, `Ω_Λ`, `Ω_k` arbitrarios y calcula `D_L = (1+z)D_M`. Con `H₀ = 67,4` y `c = 299 792,458 km/s`, `c/H₀ = 4448 Mpc`.

### 8.2 Verificaciones exactas

Para EdS, `D_L = 2(c/H₀)(1+z)(1 − 1/√(1+z))`. Para Milne, `D_L = (c/H₀)z(1 + z/2)`. El código coincide con ambas a `10⁻⁹` en `z = 0,1; 0,5; 1`.

### 8.3 Tabla de distancias

`D_L` en Mpc: `z = 0,1`: `477,5` (ΛCDM), `455,4` (EdS), `463,4` (abierto sin Λ, `Ω_m = 0,3`); `z = 0,5`: `2927,1`, `2448,6`, `2664,1`; `z = 1`: `6802,5`, `5211,1`, `6098,8`; `z = 1,5`: `11 205,2`, `8174,1`, `10 173,9`.

### 8.4 Cuánto más lejos

La supernova a `z = 0,5` está un `9,9 %` más lejos en ΛCDM que en el modelo abierto sin Λ, que son `+0,204 mag`; a `z = 1`, `+11,5 %` y `+0,237 mag`. Coincide con el orden de «10 a 15 %» del resumen de Riess et al. (S3). Frente a EdS, la diferencia a `z = 0,5` es `μ = 42,332` frente a `41,945`: `0,39 mag`.

### 8.5 Sensibilidad y ecuación de estado

En un universo plano, `D_L(0,5) = 2995,1; 2927,1; 2908,3 Mpc` para `Ω_m = 0,25; 0,315; 0,334`: la distancia baja un `2,9 %` al subir `Ω_m` de `0,25` a `0,334`. Con Pantheon+ (1550 supernovas), `Ω_m = 0,334 ± 0,018` en ΛCDM plano y `w₀ = −0,90 ± 0,14` con supernovas solas, compatible con una constante cosmológica (`w = −1`); combinado con CMB y BAO, `w₀ = −0,978 (+0,024/−0,031)` (S5, resumen). DESI con CMB y SN Ia prefiere `w₀ > −1`, `w_a < 0` con significancia entre `2,5σ` y `3,9σ` según la muestra de supernovas (S6, resumen); es un indicio, no una conclusión.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `D_L` | distancia de luminosidad | Mpc | `2927,1` (ΛCDM, `z = 0,5`) |
| `μ` | módulo de distancia | mag | `42,332` (ΛCDM, `z = 0,5`) |
| `c/H₀` | radio de Hubble | Mpc | `4448,0` |
| `Ω_m`, `Ω_Λ`, `Ω_k` | parámetros | — | según el modelo |
| `w₀` | ecuación de estado | — | `−0,90 ± 0,14` (SN, S5) |

## 10. Convenciones y referencias

Sin radiación; `H₀ = 67,4 km/s/Mpc` y `Ω_m = 0,315` (S2); modelos EdS y abierto son comparaciones **ilustrativas**. `c` de NIST (S1).

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NIST, *Fundamental Physical Constants — Complete Listing* (CODATA 2022) | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | `c` | Consultada el 2026-11-09 |
| S2 | Planck Collaboration, arXiv:1807.06209 | https://arxiv.org/abs/1807.06209 | `H₀ = 67,4`; `Ω_m = 0,315` | Solo resumen, consultado el 2026-11-09 |
| S3 | Riess et al., arXiv:astro-ph/9805201 | https://arxiv.org/abs/astro-ph/9805201 | SNe Ia 10–15 % más lejos sin constante cosmológica | Solo resumen, consultado el 2026-11-09 |
| S4 | Perlmutter et al., arXiv:astro-ph/9812133 | https://arxiv.org/abs/astro-ph/9812133 | 42 SNe; `Ω_m ≈ 0,28`; constante positiva al 99 % | Solo resumen, consultado el 2026-11-09 |
| S5 | Brout et al., *The Pantheon+ Analysis: Cosmological Constraints*, arXiv:2202.04077 | https://arxiv.org/abs/2202.04077 | 1550 SNe Ia; `Ω_m = 0,334 ± 0,018`; `w₀ = −0,90 ± 0,14`; `−0,978 (+0,024/−0,031)` | Solo resumen, consultado el 2026-11-09 |
| S6 | DESI Collaboration, arXiv:2404.03002 | https://arxiv.org/abs/2404.03002 | `w = −0,99 (+0,15/−0,13)` con BAO; preferencia por `w₀ > −1`, `w_a < 0` de 2,5σ a 3,9σ | Solo resumen, consultado el 2026-11-09 |

Límites: S2–S6 solo resumen; las soluciones cerradas de EdS y de Milne y la cuadratura son estándar y se contrastan entre sí; las comparaciones con el modelo abierto son del cálculo propio, no resultados de la fuente.

## 12. Cómo ver las distancias

| `z` | ΛCDM (Mpc) | EdS (Mpc) | Abierto sin Λ (Mpc) | ΛCDM/abierto |
|---|---|---|---|---|
| 0,1 | 477,5 | 455,4 | 463,4 | 1,030 |
| 0,5 | 2927,1 | 2448,6 | 2664,1 | 1,099 |
| 1,0 | 6802,5 | 5211,1 | 6098,8 | 1,115 |
| 1,5 | 11 205,2 | 8174,1 | 10 173,9 | 1,101 |

Descripción larga: las diferencias entre modelos crecen hasta `z ≈ 1`; por eso las supernovas distantes discriminan.

## 13. Ejemplo trabajado: la diferencia en magnitudes a `z = 0,5`

**Paso 1 · Datos.** `D_L(ΛCDM) = 2927,1 Mpc`, `D_L(abierto) = 2664,1 Mpc`.

**Paso 2 · Cociente.** `2927,1/2664,1 = 1,0987`.

**Paso 3 · Magnitudes.** `5 log₁₀ 1,0987 = 0,204 mag`.

**Paso 4 · Sentido.** La supernova a `z = 0,5` se ve `0,2 mag` más débil en ΛCDM que en el modelo abierto sin constante. Los 10–15 % de Riess et al. equivalen a `0,21`–`0,30 mag`.

## 14. Distintas formas de restringir la energía oscura

**Supernovas:** diferencias de distancia. **BAO:** regla estándar (C17). **CMB:** geometría a `z = 1089`. Se combinan para acotar `Ω_m`, `Ω_Λ`, `w`.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `D_L` en EdS a `z = 0,5`. *Pasos:* `2(c/H₀)(1+z)(1 − 1/√(1+z))`.

<details><summary>Solución comentada</summary>

`2 × 4448 × 1,5 × (1 − 0,8165) = 2448,6 Mpc`.
</details>

**Ejercicio 2 · con una pista.** Calcula `D_L` en Milne a `z = 0,5`.

<details><summary>Solución comentada</summary>

`4448 × 0,5 × 1,25 = 2780 Mpc`.
</details>

**Ejercicio 3 · casi autónomo.** Convierte el cociente `1,0987` a magnitudes.

<details><summary>Solución comentada</summary>

`0,204 mag`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** ¿Qué cociente de distancias hay entre ΛCDM y EdS a `z = 0,5`?

<details><summary>Solución comentada</summary>

`2927,1/2448,6 = 1,195`; `0,39 mag`.
</details>

**Ejercicio 5.** ¿Cuánto cambia `D_L(0,5)` al pasar de `Ω_m = 0,25` a `0,334` (plano)?

<details><summary>Solución comentada</summary>

`2908,3/2995,1 − 1 = −2,9 %`.
</details>

**Ejercicio 6.** Convierte un exceso del `10 %` y del `15 %` de distancia en magnitudes.

<details><summary>Solución comentada</summary>

`5 log₁₀ 1,10 = 0,207`; `5 log₁₀ 1,15 = 0,303 mag`.
</details>

**Ejercicio 7.** ¿Cuánto vale `μ` en ΛCDM a `z = 0,5`?

<details><summary>Solución comentada</summary>

`5 log₁₀(2927,1 × 10⁶/10) = 42,332`.
</details>

**Ejercicio 8.** ¿Qué distancia da Milne a `z = 1`?

<details><summary>Solución comentada</summary>

`4448 × 1 × 1,5 = 6672 Mpc`.
</details>

**Ejercicio 9 · transferencia.** Un compañero dice que `w = −0,90 ± 0,14` contradice la constante cosmológica. Responde con 8.5.

<details><summary>Solución comentada</summary>

`w = −1` queda a `0,7σ` de `−0,90 ± 0,14`: es compatible con una constante cosmológica.
</details>

**Ejercicio 10 · transferencia.** ¿Por qué una incertidumbre en `H₀` afecta a `D_L` pero no al cociente entre modelos?

<details><summary>Solución comentada</summary>

`D_L ∝ 1/H₀` para todos los modelos; el cociente de distancias a mismo `H₀` no depende de él (aunque en datos reales se degenera con la calibración de las SNe).
</details>

**Ejercicio 11 · transferencia.** DESI con CMB y SN Ia prefiere `w₀ > −1`, `w_a < 0` con entre `2,5σ` y `3,9σ` (S6). ¿Es un descubrimiento?

<details><summary>Solución comentada</summary>

Es un indicio dependiente de la muestra de supernovas; falta un nivel de significancia mayor y comprobar sistemáticos (C23 ofrece las herramientas para cuantificarlo).
</details>

**Ejercicio 12 · integrador.** Elabora tu *tabla de distancias de luminosidad*: tres modelos y cuatro corrimientos, verificación con EdS y Milne, diferencia en magnitudes y comparación con el 10–15 % de Riess et al.

<details><summary>Solución modelo</summary>

Tabla de la sección 12; EdS y Milne verificados a `10⁻⁹`; `+0,204 mag` a `z = 0,5`.
</details>

## 17. Laboratorio: distancia de luminosidad

El script [luminosidad.py](luminosidad.py) calcula `D_L` con curvatura general y **comprueba** las soluciones cerradas de EdS y Milne a `10⁻⁹`; tabula tres modelos y la sensibilidad a `Ω_m`.

**Datos:** `c` de NIST; `H₀`, `Ω_m` de Planck (resumen). **Predice antes de ejecutar:** ¿qué modelo da la mayor distancia a `z = 1`? (ΛCDM.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
    z   LCDM (0.315,0.685)   EdS (1,0)  abierto (0.3,0)  [D_L en Mpc, H0 = 67.4]
  0.1                477.5       455.4            463.4
  0.5               2927.1      2448.6           2664.1
  1.0               6802.5      5211.1           6098.8
  1.5              11205.2      8174.1          10173.9
z = 0.5: D_L(LCDM)/D_L(abierto sin L) = 1.0987 (+9.9 %) ; delta mu = +0.204 mag
z = 1.0: D_L(LCDM)/D_L(abierto sin L) = 1.1154 (+11.5 %) ; delta mu = +0.237 mag
z = 0.5: mu(LCDM) = 42.332 ; mu(EdS) = 41.945
plano Om = 0.25: D_L(z = 0.5) = 2995.1 Mpc
plano Om = 0.315: D_L(z = 0.5) = 2927.1 Mpc
plano Om = 0.334: D_L(z = 0.5) = 2908.3 Mpc
Pruebas superadas.
```

```bash
python programa/clases/B26/B26-C19-energia-oscura-y-parametros/luminosidad.py
```

**Límites:** sin radiación; `w = −1` fijo.

## 18. Errores frecuentes y cómo corregirlos

**Usar `D_C` en lugar de `D_L`.** Se corrige con el ejercicio 1 (factor `1+z`).

**Olvidar `sinh` con curvatura.** Se corrige con el ejercicio 2.

**Confundir porcentaje y magnitud.** Se corrige con el ejercicio 6.

**Presentar el 10–15 % como valor propio.** Se corrige con la sección 10.

**Dar por probado `w ≠ −1`.** Se corrige con el ejercicio 11.

## 19. Cómo sabrás que vas bien

Tras 8.2: ¿conoces las soluciones exactas? Si dudas, ejercicios 1 y 2. Tras 8.4: ¿cuánto vale la diferencia? Ejercicio 3. Tras el laboratorio: ¿qué verifican EdS y Milne? (la cuadratura y la curvatura).

## 20. Qué entregas y cómo se evalúa

El producto es tu **tabla de distancias de luminosidad** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | `D_C`, `D_M`, `D_L` | Explica la curvatura |
| Cálculo | Sin unidades | Con errores | Tabla correcta | Magnitudes |
| Numérico | Sin comprobar | Un caso | EdS y Milne | Discute tolerancias |
| Fuentes | Sin fuente | Sin fecha | S1–S6 con fecha | Declara resúmenes |
| Límites | No los nombra | Uno | Tres | Discute `w` |

**Condiciones críticas (no se compensan con promedio):** no tratar los modelos de comparación como resultados de las fuentes; rotular lo ilustrativo; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: no es un ajuste de supernovas reales. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Una constante cosmológica aleja la luz de supernovas distantes un 10 % a `z = 0,5` frente a un universo abierto sin ella (`+0,2 mag`); con Pantheon+, `w₀ = −0,90 ± 0,14` es compatible con `−1`. Queda una pregunta: ¿cómo se convierten esas comparaciones en límites cuantitativos?

**Glosario español–inglés.** energía oscura · *dark energy*; distancia de luminosidad · *luminosity distance*; módulo de distancia · *distance modulus*; ecuación de estado · *equation of state*; modelo de Milne · *Milne model*; constante cosmológica · *cosmological constant*.

**Continuidad.** [B26-C20](../B26-C20-limites-observacionales-de-modelos-cosmologicos/CLASE.md) ajusta `Ω_m` con supernovas y calcula intervalos de confianza.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B26-C18 — Materia oscura y evidencias](../B26-C18-materia-oscura-y-evidencias/CLASE.md) · [📚 Bloque B26](../../../tronco-comun/B26-relatividad-y-cosmologia.md) · [Siguiente: B26-C20 — Límites observacionales de modelos cosmológicos →](../B26-C20-limites-observacionales-de-modelos-cosmologicos/CLASE.md)
<!-- /nav -->
