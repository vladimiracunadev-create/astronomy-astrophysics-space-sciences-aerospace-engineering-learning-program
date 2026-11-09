# B52-C03 — Granulación de polvo y acreción

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B52](../../../tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md) · [← Anterior: B52-C02 — Discos protoplanetarios](../B52-C02-discos-protoplanetarios/CLASE.md) · [Siguiente: B52-C04 — Formación de planetesimales →](../B52-C04-formacion-de-planetesimales/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 3 del bloque B52. Nivel N3. El gas del disco de [B52-C02](../B52-C02-discos-protoplanetarios/CLASE.md) gira un poco más lento que Kepler porque lo sostiene la presión; el polvo, no. Esa diferencia hace que los granos pierdan momento angular y deriven hacia la estrella. Calculas el **número de Stokes**, la **velocidad de deriva radial**, el tiempo de deriva y un crecimiento sencillo acoplado a la deriva. Usas [B11](../../../tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md). Todo ocurre en un disco **sintético**.

## 2. Por qué esta clase existe

Si los granos derivan más rápido de lo que crecen, el polvo se pierde antes de formar planetesimales. La decisión central: **¿a qué tamaño deriva más rápido un grano y cuánto tarda en caer?**

## 3. Lo que podrás hacer al terminar

1. Calcular el parámetro `η` del soporte de presión del gas.
2. Calcular el número de Stokes de un grano en régimen de Epstein.
3. Obtener la velocidad de deriva radial `v_r = −2 St η v_K/(1+St²)`.
4. Verificar esa fórmula integrando las ecuaciones locales con arrastre.
5. Calcular el tiempo de deriva de un grano de tamaño fijo y compararlo con su crecimiento.
6. Reconocer que el máximo de la deriva ocurre en `St = 1`.

La evidencia es la **ficha de la deriva y el crecimiento del polvo** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es el arrastre aerodinámico?
2. ¿Qué es el tiempo de frenado?
3. ¿Qué es un método de Runge–Kutta?
4. ¿Qué es un estado estacionario?
5. ¿Qué es un valor ilustrativo?

<details>
<summary>Ver respuestas</summary>

1. Una fuerza proporcional a la velocidad relativa entre grano y gas. 2. El tiempo en que el arrastre cambia de forma apreciable la velocidad de un grano. 3. Un método numérico para integrar ecuaciones diferenciales ordinarias. 4. Uno en que las derivadas respecto del tiempo son cero. 5. Un valor propuesto para el ejemplo, no medido.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

En el disco sintético de B52-C02, a 5 ua `η = 4.12e-03` y `η v_K = 54.8 m/s`. Un grano de 1 cm tiene `St = 0.258` a 30 ua y `0.00157` a 1 ua, y recorrería de 30 a 1 ua en `45130` años si no creciera. Es el **ejemplo conductor**; no se mide ningún grano real.

## 6. Vocabulario

El **número de Stokes** `St = Ω t_s` compara el tiempo de frenado `t_s` con el periodo orbital. El **régimen de Epstein** vale cuando el grano es menor que el recorrido libre de las moléculas: `St = π a ρ_s/(2Σ)` en el plano medio. El parámetro `η = −½ (h/r)² d ln P/d ln r` mide cuánto menos que Kepler gira el gas. La **deriva radial** es el movimiento hacia adentro del grano.

## 7. Modelo mental

Como una hoja en un río que gira: la hoja chica va con el agua, la grande va por su cuenta y es frenada, y solo la intermedia pierde energía rápido. Límite: arrastre de Epstein, partícula única, sin retroalimentación sobre el gas ni turbulencia.

```mermaid
flowchart LR
    P["gradiente de presión"] --> E["η"]
    A["tamaño a"] --> S["St = π a ρ_s / (2Σ)"]
    E --> V["v_r"]
    S --> V
    V --> T["tiempo de deriva"]
    V --> C["crecimiento acoplado"]
```

*Descripción textual:* el gradiente de presión da `η`; el tamaño y la densidad superficial dan `St`; ambos dan la velocidad de deriva, de la que salen el tiempo de deriva y el crecimiento acoplado.

## 8. La explicación, paso a paso

### 8.1 Soporte de presión

Con `P ∝ Σ c_s Ω ∝ r^(−3,25)` en el disco sintético, `η = ½ (h/r)² · 3,25`. A 5 ua, `η = 4.116e-03`. El gas gira con `v_K (1 − η)`; el polvo sin arrastre giraría con `v_K`.

### 8.2 Deriva

Con `t_s = St/Ω`, las ecuaciones locales para `v_r` y `D = v_φ − v_K` son `dv_r/dt = 2ΩD − v_r/t_s` y `dD/dt = −(Ω/2) v_r − (D + η v_K)/t_s`. Su estado estacionario es `v_r = −2 St η v_K/(1+St²)`. La integración RK4 de las ecuaciones da:

| St | v_r fórmula [m/s] | v_r ecuaciones [m/s] |
|---|---|---|
| 0.001 | -0.10965 | -0.10965 |
| 0.01 | -1.09638 | -1.09638 |
| 0.1 | -10.85637 | -10.85637 |
| 1 | -54.82466 | -54.82466 |
| 10 | -10.85637 | -10.85637 |

El máximo `|v_r| = η v_K = 54.82 m/s` ocurre en `St = 1`; para `St` muy pequeño o muy grande la deriva cae.

### 8.3 Tiempo de deriva

Para un grano de 1 cm de tamaño fijo, `∫ dr/|v_r|` de 30 a 1 ua da `45130 años`. La integral usa la regla del punto medio en `ln r` con 4000 intervalos.

### 8.4 Crecimiento acoplado

Si el grano crece por barrido con `da/dt = ρ_d Δv/(4ρ_s)` (con `Δv = 10 m/s`, `ρ_d = 0,01 ρ_gas`, `ρ_s = 1000 kg/m³`, todo ilustrativo), un grano de 0,1 mm a 30 ua pasa en `2000 años` a `0.02092 cm` y a `29.8164 ua`. Con un paso la mitad de grande el resultado coincide a `10⁻⁶`.

### 8.5 Lectura

Si un grano crece más lento de lo que deriva, desaparece hacia la estrella. Los valores de `Δv` y `ρ_d` son ilustrativos y determinan el resultado; el cálculo no demuestra que el polvo del Sistema Solar creciera así.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `η` | soporte de presión | — | 4.116e-03 a 5 ua |
| `St` | número de Stokes | — | 0.258 (1 cm, 30 ua) |
| `v_K` | velocidad kepleriana | m/s | 13320 a 5 ua |
| `v_r` | deriva radial | m/s | -54.82 para St = 1 |
| `ρ_s` | densidad del grano | kg/m³ | 1000 (ilustrativo) |
| `Δv` | velocidad relativa de colisión | m/s | 10 (ilustrativo) |

## 10. Convenciones y referencias

Unidades SI. Plano medio, simetría axial, régimen de Epstein. Tolerancias: fórmula frente a ecuaciones `10⁻³`; cambio de paso `10⁻⁶`.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NIST, *Fundamental Physical Constants — Complete Listing* (CODATA 2022) | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | `G`, `k_B`, `m_p` | Consultada el 2026-11-09 |
| S2 | Mamajek et al., *IAU 2015 Resolution B3*, arXiv:1510.07674 | https://arxiv.org/abs/1510.07674 | `(GM)☉` nominal | Texto del PDF extraído el 2026-11-09 |
| S3 | Chiang y Youdin, *Forming Planetesimals in Solar and Extrasolar Nebulae*, arXiv:0909.2652 | https://arxiv.org/abs/0909.2652 | Las colisiones no bastan para pasar de granos a cuerpos de más de un kilómetro; la deriva y la autogravedad importan | Solo resumen, consultado el 2026-11-09 |

Límites: de S3 solo se leyó el resumen; la fórmula de la deriva y la ley de Epstein no se consultaron en una fuente: se verifican aquí contra las ecuaciones locales (que comparten su álgebra, de modo que la comprobación valida la integración, no la física); `Δv`, `ρ_d` y `ρ_s` son ilustrativos.

## 12. Cómo verlo

| Magnitud | Valor |
|---|---|
| η a 5 ua | 4.12e-03 |
| deriva máxima | 54.8 m/s |
| St de 1 cm a 30 ua | 0.258 |
| tiempo de deriva 30→1 ua | 45130 años |
| tamaño tras 2000 años | 0.0209 cm |

Descripción larga: la deriva es máxima cuando `St = 1` y un grano de centímetro tarda decenas de miles de años en caer de 30 a 1 ua.

## 13. Ejemplo trabajado

**Paso 1 · Soporte.** `η = 4.116e-03`.

**Paso 2 · Máximo.** `η v_K = 54.82 m/s`.

**Paso 3 · Para St = 0,1.** `v_r = −2·0,1·η v_K/(1+0,01) = -10.856 m/s`.

**Paso 4 · Tiempo.** En 5 ua, recorrer 1 ua a esa velocidad toma `1,496·10¹¹ m / 10.86 m/s ≈ 437 años`.

## 14. Distintas formas de describirlo

**Por fórmula:** `v_r(St)`. **Por tabla:** 8.2. **Por simulación:** RK4. **Por tiempo:** `t_deriva` frente a `t_crecimiento`.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `St` de un grano de 1 mm con `ρ_s = 1000 kg/m³` y `Σ = 100 kg/m²`. *Pasos:* `π·10⁻³·1000/(2·100)`.

<details><summary>Solución comentada</summary>

`0,0157`.
</details>

**Ejercicio 2 · con una pista.** ¿Qué deriva tiene `St = 1`? *Pista:* `η v_K`.

<details><summary>Solución comentada</summary>

`54.8 m/s` hacia adentro a 5 ua.
</details>

**Ejercicio 3 · casi autónomo.** Si `η` se duplica, ¿cómo cambia `v_r`?

<details><summary>Solución comentada</summary>

Se duplica, porque es proporcional a `η`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** `v_r` para `St = 0,01`.

<details><summary>Solución comentada</summary>

`-1.096 m/s`.
</details>

**Ejercicio 5.** `v_r` para `St = 10`.

<details><summary>Solución comentada</summary>

`-10.856 m/s`, igual que para `St = 0,1`.
</details>

**Ejercicio 6.** ¿Por qué `St = 10` y `St = 0,1` derivan igual?

<details><summary>Solución comentada</summary>

Porque `St/(1+St²)` es simétrico bajo `St → 1/St`.
</details>

**Ejercicio 7.** Tiempo de deriva de 1 cm de 30 a 1 ua.

<details><summary>Solución comentada</summary>

`45130 años`.
</details>

**Ejercicio 8.** Tamaño tras 2000 años según el crecimiento acoplado.

<details><summary>Solución comentada</summary>

`0.0209 cm`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** **Transferencia.** Un colega dice que el polvo no puede sobrevivir porque deriva. Responde.

<details><summary>Solución comentada</summary>

La conclusión depende de `Δv`, `ρ_d` y `η`, que son ilustrativos aquí; en un disco real el crecimiento puede ser más rápido, o se forman trampas de presión.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** **Transferencia.** ¿Qué cambia si el disco es más grueso (`h/r` mayor)?

<details><summary>Solución comentada</summary>

`η ∝ (h/r)²` crece y la deriva es mayor.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** **Transferencia.** ¿Qué hipótesis falla para granos mayores que el recorrido libre del gas?

<details><summary>Solución comentada</summary>

Epstein: pasa a régimen de Stokes y `t_s` depende de `a²`.
</details>

**Ejercicio 12 · integrador.** **Integrador.** **Integrador.** Elabora tu *ficha de la deriva y el crecimiento del polvo*: `η`, tabla de 8.2, tiempo de deriva, crecimiento acoplado y límites.

<details><summary>Solución modelo</summary>

Secciones 8.1–8.5 y 12.
</details>

## 17. Laboratorio: deriva radial y crecimiento de un grano

El script [deriva.py](deriva.py) calcula `η`, `St` y la deriva radial, la verifica integrando las ecuaciones locales con RK4 y acopla deriva y crecimiento comprobando el cambio de paso (**comprueba** `10⁻³` y `10⁻⁶`).

**Datos:** `G`, `k_B`, `m_p` de NIST y `(GM)☉` de la IAU 2015, consultados el 2026-11-09; el disco y los granos son **sintéticos**. **Predice antes de ejecutar:** ¿A qué `St` es máxima la deriva? (En `St = 1`.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Disco sintetico de B52-C02; r = 5 ua: eta = 4.116e-03 ; v_K = 13320 m/s ; eta v_K = 54.82 m/s
      St    v_r formula [m/s]   v_r ecuaciones [m/s]  dif. rel.
   1e-03             -0.10965               -0.10965   6.33e-15
   1e-02             -1.09638               -1.09638   8.10e-15
   1e-01            -10.85637              -10.85637   7.11e-15
   1e+00            -54.82466              -54.82466   0.00e+00
   1e+01            -10.85637              -10.85637   7.77e-16
Grano de 1 cm: St = 0.258 a 30 ua y 0.00157 a 1 ua ; tiempo de deriva de 30 a 1 ua (tamano fijo) = 45130 anios
Deriva acoplada con crecimiento (a0 = 0.1 mm, 30 ua, 2000 anios): paso h -> r = 29.816447 ua, a = 0.02092 cm ; paso h/2 -> r = 29.816447 ua, a = 0.02092 cm
Pruebas superadas.
```

```bash
python programa/clases/B52/B52-C03-granulacion-de-polvo-y-acrecion/deriva.py
```

**Límites:** Epstein, partícula única, sin retroalimentación ni turbulencia; la comparación valida la integración, no la física.

## 18. Errores frecuentes y cómo corregirlos

**Creer que los granos más pequeños derivan más rápido.** Se corrige con 8.2: el máximo está en `St = 1`.

**Olvidar que `St` depende de `Σ` local.** Se corrige con 8.3.

**Tomar un resultado de modelo como evidencia de un disco real.** Se corrige con la sección 10.

**Usar un solo paso de integración sin comprobar convergencia.** Se corrige con 8.4.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas y cuál obtuviste? Si dudas, repasa el ejemplo de la sección 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de la deriva y el crecimiento del polvo** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Conceptos de la clase | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con el análisis | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha | Declara lo ilustrativo |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular lo sintético e ilustrativo; no presentar un resultado simulado como observado; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y no sustituyen a la literatura primaria ni a los códigos de producción. Lo simulado no es lo observado. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

La deriva máxima es `η v_K = 54.8 m/s` en `St = 1`, y un grano de 1 cm cruza de 30 a 1 ua en unos `45130` años. Queda una pregunta: ¿qué mecanismo concentra los granos antes de que se pierdan?

**Glosario español–inglés.** número de Stokes · *Stokes number*; deriva radial · *radial drift*; régimen de Epstein · *Epstein regime*; arrastre · *drag*; soporte de presión · *pressure support*.

**Continuidad.** [B52-C04](../B52-C04-formacion-de-planetesimales/CLASE.md) estudia el colapso gravitacional de las concentraciones de partículas.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B52-C02 — Discos protoplanetarios](../B52-C02-discos-protoplanetarios/CLASE.md) · [📚 Bloque B52](../../../tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md) · [Siguiente: B52-C04 — Formación de planetesimales →](../B52-C04-formacion-de-planetesimales/CLASE.md)
<!-- /nav -->
