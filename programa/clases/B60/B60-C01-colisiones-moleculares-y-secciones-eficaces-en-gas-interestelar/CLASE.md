# B60-C01 — Colisiones moleculares y secciones eficaces en gas interestelar

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B60](../../../tronco-comun/B60-cinetica-y-modelado-astroquimico.md) · [← Anterior: B59-C23 — Subproductos y flujos residuales de procesos ISRU](../../B59/B59-C23-subproductos-y-flujos-residuales-de-procesos-isru/CLASE.md) · [Siguiente: B60-C02 — Coeficientes de velocidad dependientes de la temperatura y bases cinéticas →](../B60-C02-coeficientes-de-velocidad-dependientes-de-la-temperatura-y-bases-cineticas/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 1 del bloque B60. Nivel N3. En [B06-C14](../../../tronco-comun/B06-quimica-y-materia-del-universo.md) viste la cinética inicial: una velocidad de reacción es una constante por concentraciones. Aquí bajas un nivel y preguntas **de dónde sale esa constante**: la calculas como el promedio de la sección eficaz por la velocidad relativa sobre una distribución de Maxwell–Boltzmann. Comparas tres modelos de sección eficaz (esfera dura, Langevin y esfera dura con barrera), los contrastas con una simulación Monte Carlo de semilla fija y con una cuadratura numérica. Las moléculas, diámetros y polarizabilidades del laboratorio son **ilustrativos**.

## 2. Por qué esta clase existe

Un modelo astroquímico necesita miles de constantes de velocidad. Antes de usar las de una base de datos conviene saber qué hay dentro de una: una colisión, una sección eficaz y un promedio térmico. La decisión central: **¿cuándo una reacción depende de la temperatura y cuándo no, y por qué?**

## 3. Lo que podrás hacer al terminar

1. Definir la constante de velocidad bimolecular como `k(T) = ⟨σ v⟩`.
2. Calcular la velocidad relativa media con la masa reducida.
3. Obtener `k` de esfera dura y de Langevin, con unidades en cm³ s⁻¹.
4. Explicar por qué la constante de Langevin no depende de `T` y la de esfera dura crece como `√T`.
5. Deducir `k ∝ exp(−E₀/kT)` para una sección eficaz con umbral.
6. Verificar un cálculo analítico con Monte Carlo y con cuadratura, declarando la tolerancia.

La evidencia es la **ficha de la teoría de colisiones** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es una masa reducida?
2. ¿Qué es una distribución de Maxwell–Boltzmann?
3. ¿Qué unidades tiene una constante de velocidad bimolecular?
4. ¿Qué es un valor ilustrativo?
5. ¿Qué es una simulación Monte Carlo con semilla fija?

<details>
<summary>Ver respuestas</summary>

1. `μ = m₁m₂/(m₁+m₂)`. 2. La distribución de velocidades de un gas en equilibrio térmico. 3. cm³ s⁻¹ (volumen por tiempo). 4. Un valor propuesto para el ejemplo, no medido. 5. Un promedio sobre números aleatorios reproducibles.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Un ion de 3 u choca con una molécula de 2 u (masa reducida `1,200 u`). Con un diámetro de colisión de 3 Å, a 10 K la esfera dura da `k = 1,188 × 10⁻¹⁰ cm³ s⁻¹`; la captura de Langevin, con una polarizabilidad de 0,787 Å³, da `1,897 × 10⁻⁹ cm³ s⁻¹`. Es el **ejemplo conductor**. Todo es **ilustrativo**; ningún valor corresponde a una reacción medida.

## 6. Vocabulario

La **sección eficaz** `σ` (m² o cm²) es el área efectiva de colisión. La **constante de velocidad** `k(T)` es el promedio térmico `⟨σ v⟩`. La **masa reducida** `μ` resume las dos masas. El **modelo de Langevin** describe una colisión ion–neutro dominada por la atracción de carga–dipolo inducido. La **energía umbral** `E₀` es la energía mínima para reaccionar.

## 7. Modelo mental: pasar por una puerta

Como cruzar una puerta de un pasillo concurrido: el área de la puerta (sección eficaz) por la rapidez con que pasa la gente (velocidad) da cuántos cruzan por segundo. Una puerta que se agranda con la lentitud (Langevin) compensa la baja velocidad.

```mermaid
flowchart LR
    S["sección eficaz σ(E)"] --> P["promedio de σ·v"]
    M["Maxwell-Boltzmann (μ, T)"] --> P
    P --> K["k(T) en cm³/s"]
    K --> V["Monte Carlo y cuadratura"]
```

*Descripción textual:* la sección eficaz y la distribución de velocidades se promedian para obtener `k(T)`, que se verifica con dos vías independientes.

Analogía: puerta y pasillo. Límite: colisiones binarias en gas diluido, sin estructura interna de las moléculas.

## 8. La explicación, paso a paso

### 8.1 Esfera dura

Con `σ = π d²`, la velocidad relativa media es `v̄ = √(8kT/(πμ))` y `k = σ v̄`. Crece como `√T`.

| `T` (K) | `v̄` (m/s) | `k` esfera dura (cm³/s) | `k_L/k` |
|---|---|---|---|
| 10 | 420,0 | 1,188 × 10⁻¹⁰ | 16,0 |
| 50 | 939,3 | 2,656 × 10⁻¹⁰ | 7,1 |
| 300 | 2300,7 | 6,505 × 10⁻¹⁰ | 2,9 |

### 8.2 Langevin

El potencial de carga–dipolo inducido da una sección eficaz `σ_L(v) = k_L / v`, de modo que `σ v = k_L` es constante: `k_L = (e / 2ε₀) √(α/μ)`, con `α = 4π ε₀ α'` y `α'` la polarizabilidad como volumen. Para `μ = 1,200 u` y `α' = 0,787 Å³`: `k_L = 1,897 × 10⁻⁹ cm³ s⁻¹`, igual a todas las temperaturas.

### 8.3 Verificación con Monte Carlo

Se muestrean 400 000 velocidades relativas (cada componente, normal con desviación `√(kT/μ)`) a 10 K con semilla `60001`: la esfera dura da `1,188 × 10⁻¹⁰` con error de `0,05 %`. El promedio de `σ_L v` da `k_L` con error de `2,6 × 10⁻¹²`: es exacto por construcción, porque `σ_L v` es constante; sirve para probar el código pero no el muestreo.

### 8.4 Sección eficaz con barrera

Con `σ(E) = σ₀(1 − E₀/E)` para `E > E₀` (línea de centros), la integral da `k = σ₀ v̄ exp(−E₀/kT)`: el origen del factor de Arrhenius. Con `E₀/k = 500 K` la cuadratura de Simpson y la forma cerrada coinciden a `1,4 × 10⁻¹²` de diferencia relativa.

| `T` (K) | `k` cuadratura (cm³/s) | `k` cerrada (cm³/s) |
|---|---|---|
| 50 | 1,2057 × 10⁻¹⁴ | 1,2057 × 10⁻¹⁴ |
| 100 | 2,5306 × 10⁻¹² | 2,5306 × 10⁻¹² |
| 300 | 1,2286 × 10⁻¹⁰ | 1,2286 × 10⁻¹⁰ |

De 50 a 300 K, `k` con barrera crece 10 190 veces.

### 8.5 Lectura

Sin barrera, la temperatura casi no importa (Langevin: nada; esfera dura: `√T`). Con barrera, la temperatura lo domina todo. A 10 K una barrera de 500 K da un factor `exp(−50) = 1,9 × 10⁻²²`: la reacción no ocurre en el modelo.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `σ` | sección eficaz | m² (cm²) | `π d²` = 2,83 × 10⁻¹⁹ m² |
| `μ` | masa reducida | kg (u) | 1,200 u |
| `v̄` | velocidad relativa media | m/s | 420,0 a 10 K |
| `k` | constante bimolecular | cm³ s⁻¹ | 1,188 × 10⁻¹⁰ (10 K) |
| `α'` | polarizabilidad como volumen | Å³ | 0,787 (ilustrativa) |
| `E₀/k` | umbral | K | 500 (ilustrativo) |

## 10. Convenciones y referencias

SI en el cálculo; se imprime en cm³ s⁻¹ (1 m³ = 10⁶ cm³). Gas diluido, colisiones binarias, sistema de referencia del centro de masas (velocidad relativa).

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| NIST-CODATA | NIST, constantes CODATA 2022: `k_B`, `u`, `e`, `ε₀` | physics.nist.gov/cgi-bin/cuu/Value (cuatro páginas) | valores de las constantes | Consultadas el 2026-11-09 |
| — | Teoría de colisiones y fórmula de Langevin | — | relaciones estándar que verifica el laboratorio | No se consultó una fuente; se verifican numéricamente |

Límites: diámetros, polarizabilidad, masas y umbral son ilustrativos; ninguna sección eficaz medida o calculada se consultó.

## 12. Cómo ver la constante de velocidad

| Magnitud | Valor |
|---|---|
| `k` esfera dura (10 K) | 1,188 × 10⁻¹⁰ cm³/s |
| `k` Langevin | 1,897 × 10⁻⁹ cm³/s |
| cociente `k(300 K)/k(50 K)` con barrera | 10 190 |

Descripción larga: Langevin es una línea horizontal; la esfera dura sube como `√T`; la barrera sube casi exponencialmente.

## 13. Ejemplo trabajado: esfera dura a 50 K

**Paso 1 · Velocidad.** `v̄ = √(8kT/(πμ))` con `μ = 1,200 u = 1,993 × 10⁻²⁷ kg` da `939,3 m/s`.

**Paso 2 · Sección.** `σ = π(3 × 10⁻¹⁰ m)² = 2,827 × 10⁻¹⁹ m²`.

**Paso 3 · Constante.** `k = σ v̄ = 2,656 × 10⁻¹⁶ m³/s`.

**Paso 4 · Unidades.** `× 10⁶ = 2,656 × 10⁻¹⁰ cm³/s`.

## 14. Distintas formas de describir una constante de velocidad

**Por colisión:** `σ(E)`. **Por promedio:** `⟨σ v⟩`. **Por ley de temperatura:** `√T`, constante o exponencial. **Por simulación:** media de muestras con su error.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `k` de esfera dura a 10 K con `v̄ = 420,0 m/s` y `d = 3 Å`. *Pasos:* `σ = π d²`; multiplica; pasa a cm³/s.

<details><summary>Solución comentada</summary>

`σ = 2,827 × 10⁻¹⁹ m²`; `k = 1,1875 × 10⁻¹⁶ m³/s = 1,188 × 10⁻¹⁰ cm³/s`.
</details>

**Ejercicio 2 · con una pista.** ¿Cuánto vale `k_L/k` de esfera dura a 300 K? *Pista:* divide `1,897 × 10⁻⁹` entre `6,505 × 10⁻¹⁰`.

<details><summary>Solución comentada</summary>

`2,9`: a 300 K la captura de Langevin es solo 2,9 veces la esfera dura de este ejemplo.
</details>

**Ejercicio 3 · casi autónomo.** ¿Por qué `k_L` no depende de `T`?

<details><summary>Solución comentada</summary>

Porque `σ_L ∝ 1/v`, así `σ v` es constante y el promedio térmico no cambia nada.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Obtén `k` de esfera dura a 50 K a partir del valor a 10 K sin recalcular `v̄`.

<details><summary>Solución comentada</summary>

`k ∝ √T`: `1,188 × 10⁻¹⁰ × √5 = 2,656 × 10⁻¹⁰ cm³/s`.
</details>

**Ejercicio 5.** Verifica el cociente 10 190 entre 300 K y 50 K con barrera de 500 K.

<details><summary>Solución comentada</summary>

`√(300/50) · exp(−500/300 + 500/50) = 2,449 · exp(8,333) = 2,449 · 4160 = 10 190`.
</details>

**Ejercicio 6.** Estima `k` con barrera de 500 K a 10 K.

<details><summary>Solución comentada</summary>

`1,188 × 10⁻¹⁰ × exp(−50) = 1,188 × 10⁻¹⁰ × 1,93 × 10⁻²² ≈ 2,3 × 10⁻³² cm³/s`.
</details>

**Ejercicio 7.** El Monte Carlo de Langevin dio un error de `2,6 × 10⁻¹²`. ¿Qué prueba y qué no?

<details><summary>Solución comentada</summary>

Prueba que el código promedia bien y que las unidades son coherentes; no prueba el muestreo, porque `σ_L v` es constante. La prueba del muestreo es la esfera dura (error 0,05 %).
</details>

**Ejercicio 8.** Convierte `k = 1,188 × 10⁻¹⁶ m³/s` a cm³/s.

<details><summary>Solución comentada</summary>

`1 m³ = 10⁶ cm³`: `1,188 × 10⁻¹⁰ cm³/s`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** A 10 K, ¿por qué un modelo de nube fría da más peso a reacciones sin barrera que a las que tienen una?

<details><summary>Solución comentada</summary>

Porque el factor `exp(−E₀/kT)` hace despreciable una barrera de cientos de K a 10 K (aquí `10⁻²²`), mientras que una captura tipo Langevin sigue en `~10⁻⁹ cm³/s` en este ejemplo ilustrativo. No es una afirmación sobre una red real.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** Si el compañero tiene el doble de masa con la misma polarizabilidad, ¿cómo cambia `k_L`?

<details><summary>Solución comentada</summary>

`k_L ∝ μ^(−1/2)`: si `μ` se duplica, `k_L` se divide por `√2` (de `1,897` a `1,34 × 10⁻⁹`).
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** Una tabla da `k = 10⁻⁴⁵ cm³/s` a 10 K para una reacción con barrera. ¿Cómo debe leerse?

<details><summary>Solución comentada</summary>

Como una extrapolación de una ley, no como una medida: ningún experimento resuelve un valor así. Un modelo la trata como nula, salvo efectos que esta clase no incluye (como el túnel).
</details>

**Ejercicio 12.** **Integrador.** Elabora tu *ficha de la teoría de colisiones*: tabla de `k(T)` para esfera dura, valor de Langevin, verificación Monte Carlo y cuadratura con barrera.

<details><summary>Solución modelo</summary>

Secciones 8.1–8.5, con unidades, tolerancias (1 % Monte Carlo; `10⁻⁶` cuadratura) y el rótulo «ilustrativo».
</details>

## 17. Laboratorio: de la sección eficaz a la constante

El script [colisiones.py](colisiones.py) calcula las tres constantes, las verifica con Monte Carlo de semilla `60001` y con una cuadratura de Simpson (**comprueba** el error de Monte Carlo < 1 %, la cuadratura < `10⁻⁶` y que `k_L` esté entre `1,0` y `2,5 × 10⁻⁹ cm³/s`).

**Datos:** CODATA 2022 de NIST, consultadas el 2026-11-09; el resto **ilustrativo**. **Predice antes de ejecutar:** ¿cuál es mayor a 10 K, esfera dura o Langevin? (Langevin, unas 16 veces.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
mu = 1.200 u ; Langevin k_L = 1.897e-09 cm^3 s^-1 (independiente de T)

Esfera dura (d = 3 A) frente a Langevin:
  T [K]   v_media [m/s]   k_dura [cm3/s]   k_L/k_dura
     10         420.0       1.188e-10        16.0
     50         939.3       2.656e-10         7.1
    300        2300.7       6.505e-10         2.9

Monte Carlo a 10 K (N = 400000): esfera dura 1.188e-10 (error 0.05%) ; Langevin 1.897e-09 (error 2.63e-12)

Seccion con barrera E0/k = 500 K (sigma0 = pi d^2): cuadratura frente a forma cerrada
  T [K]   k_cuadratura [cm3/s]   k_cerrada [cm3/s]   dif. relativa
     50           1.2057e-14        1.2057e-14   1.4e-12
    100           2.5306e-12        2.5306e-12   1.4e-12
    300           1.2286e-10        1.2286e-10   1.4e-12
  cociente k(300 K)/k(50 K) con barrera = 10190.5
Pruebas superadas.
```

```bash
python programa/clases/B60/B60-C01-colisiones-moleculares-y-secciones-eficaces-en-gas-interestelar/colisiones.py
```

**Límites:** sin estructura interna, sin sección eficaz medida, sin dependencia de la energía de las moléculas polares.

## 18. Errores frecuentes y cómo corregirlos

**Pensar que toda reacción acelera con la temperatura.** Se corrige con 8.2: Langevin es constante.

**Confundir `m` con la masa reducida.** Se corrige con la sección 9.

**Olvidar la conversión m³ → cm³.** Se corrige con el ejercicio 8.

**Presentar una constante ilustrativa como medida.** Se corrige con la sección 11.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de la teoría de colisiones** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | conceptos de la clase | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con el análisis | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | fuentes con fecha | Declara lo ilustrativo |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular los parámetros como ilustrativos; no presentar lo simulado como observado; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

La constante de velocidad es `⟨σ v⟩`: Langevin da `1,9 × 10⁻⁹ cm³/s` sin depender de `T`, la esfera dura `1,2 × 10⁻¹⁰` a 10 K, y una barrera lo cambia todo con `exp(−E₀/kT)`. Queda una pregunta: ¿cómo se resume esa dependencia de `T` en una fórmula que usan las bases de datos?

**Glosario español–inglés.** sección eficaz · *cross section*; constante de velocidad · *rate coefficient*; masa reducida · *reduced mass*; captura de Langevin · *Langevin capture*; energía umbral · *threshold energy*.

**Continuidad.** [B60-C02](../B60-C02-coeficientes-de-velocidad-dependientes-de-la-temperatura-y-bases-cineticas/CLASE.md) estudia los coeficientes de velocidad dependientes de la temperatura.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B59-C23 — Subproductos y flujos residuales de procesos ISRU](../../B59/B59-C23-subproductos-y-flujos-residuales-de-procesos-isru/CLASE.md) · [📚 Bloque B60](../../../tronco-comun/B60-cinetica-y-modelado-astroquimico.md) · [Siguiente: B60-C02 — Coeficientes de velocidad dependientes de la temperatura y bases cinéticas →](../B60-C02-coeficientes-de-velocidad-dependientes-de-la-temperatura-y-bases-cineticas/CLASE.md)
<!-- /nav -->
