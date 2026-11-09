# B35-C03 — Inestabilidades de plasma: cinéticas y de fluido

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B35](../../../tronco-comun/B35-fisica-avanzada-de-plasmas-y-mhd-espacial.md) · [← Anterior: B35-C02 — Ondas de Alfvén y ondas magnetosónicas](../B35-C02-ondas-de-alfven-y-ondas-magnetosonicas/CLASE.md) · [Siguiente: B35-C04 — Colisiones, régimen cinético y ecuación de Vlasov →](../B35-C04-colisiones-regimen-cinetico-y-ecuacion-de-vlasov/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 3 del bloque B35. Nivel N3. Una inestabilidad es una perturbación que crece. Aquí obtienes la tasa de crecimiento de la **inestabilidad de dos haces** (cinética) y de **Kelvin–Helmholtz** con campo paralelo (de fluido) por dos vías: la forma cerrada y las raíces numéricas del polinomio de dispersión. Usas [B05](../../../tronco-comun/B05-fisica-fundamental-para-el-espacio.md) y [B35-C02](../B35-C02-ondas-de-alfven-y-ondas-magnetosonicas/CLASE.md). Los parámetros están normalizados.

## 2. Por qué esta clase existe

Las inestabilidades limitan los equilibrios y convierten energía libre en turbulencia. La decisión central: **¿para qué número de onda y para qué cizalladura crece la perturbación y cuánto?**

## 3. Lo que podrás hacer al terminar

1. Escribir la relación de dispersión de dos haces fríos.
2. Obtener su tasa de crecimiento máxima.
3. Resolver el polinomio por raíces numéricas.
4. Obtener el umbral de Kelvin–Helmholtz con campo.
5. Comparar forma cerrada y raíces.
6. Reconocer los límites de las teorías lineales.

La evidencia es la **ficha de las inestabilidades** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es una incertidumbre?
2. ¿Qué es una simulación Monte Carlo?
3. ¿Qué es una tabla de resultados?
4. ¿Qué es un valor ilustrativo?
5. ¿Qué es una verificación?

<details>
<summary>Ver respuestas</summary>

1. Un intervalo en que se espera el valor verdadero. 2. Repetir con números aleatorios de semilla fija. 3. Un resumen ordenado de cálculos. 4. Un valor propuesto para el ejemplo, no medido. 5. Comparar un cálculo con un caso independiente.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Para dos haces fríos simétricos la tasa máxima es `ω_p/(2√2) = 0,353553 ω_p` en `k v₀ = 0,6124 ω_p`. En Kelvin–Helmholtz con campo paralelo la perturbación crece solo si el salto de velocidad supera `2 v_A`: para `U = 3 v_A` la tasa es `1,118 k v_A`. Es el **ejemplo conductor**; todo está normalizado.

## 6. Vocabulario

La **tasa de crecimiento** `γ` es la parte imaginaria de `ω`. La **relación de dispersión** vincula `ω` y `k`. Los **dos haces** son dos poblaciones que se cruzan. **Kelvin–Helmholtz** nace de la cizalladura de velocidad. El **umbral** es el valor que separa estable de inestable.

## 7. Modelo mental: dos corrientes que se cruzan

Dos corrientes de gente que se cruzan se agrupan en cúmulos que refuerzan su propia perturbación; un campo magnético a lo largo del flujo actúa como una banda elástica que frena el crecimiento.

```mermaid
flowchart LR
    D["relación de dispersión"] --> P["polinomio en ω"]
    P --> A["forma cerrada"]
    P --> N["raíces numéricas"]
    A --> G["γ máxima y umbral"]
    N --> G
```

*Descripción textual:* la relación de dispersión se resuelve de dos maneras y ambas dan la misma tasa.

Analogía: dos corrientes que se cruzan. Límite: solo teoría lineal; haces fríos y fluido incompresible.

## 8. La explicación, paso a paso

### 8.1 Dos haces

Con `a = k v₀/ω_p`, `(ω² − a²)² = ω_p²(ω² + a²)`. La raíz inestable es `ω² = [(2a²+1) − √(1+8a²)]/2`.

| `k v₀/ω_p` | `γ/ω_p` forma cerrada | `γ/ω_p` raíces |
|---|---|---|
| 0,2000 | 0,185624 | 0,185624 |
| 0,4000 | 0,308194 | 0,308194 |
| 0,6124 | 0,353553 | 0,353553 |
| 0,8000 | 0,311339 | 0,311339 |
| 0,9500 | 0,176145 | 0,176145 |
| 1,0000 | 0 | 0 |
| 1,2000 | 0 | 0 |

El máximo está en `k v₀ = √(3/8) ω_p = 0,61237` y vale `1/(2√2) = 0,353553`. Para `k v₀ ≥ ω_p` el plasma es estable.

### 8.2 Kelvin–Helmholtz con campo paralelo

Con densidades iguales y `B` paralelo y uniforme, `ω² = k²(v_A² − U²/4)` (relación estándar de la lámina de vorticidad incompresible, no consultada).

| `U/v_A` | `γ/(k v_A)` cerrada | raíces |
|---|---|---|
| 0 a 2,00 | 0 | 0 |
| 2,10 | 0,320156 | 0,320156 |
| 3,00 | 1,118034 | 1,118034 |
| 4,00 | 1,732051 | 1,732051 |

### 8.3 Lectura

El campo estabiliza hasta `U = 2 v_A`. Las dos vías coinciden a `10⁻⁹` en los haces y a `10⁻⁶` en Kelvin–Helmholtz.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `γ` | tasa de crecimiento | `ω_p` | 0,353553 (máx.) |
| `a` | `k v₀/ω_p` | — | 0,6124 |
| `U` | salto de velocidad | `v_A` | 2 (umbral) |
| `v_A` | velocidad de Alfvén | — | 1 (normalizada) |

## 10. Convenciones y referencias

Unidades normalizadas (`ω_p = 1` en los haces, `v_A = 1` en Kelvin–Helmholtz). No se usa ninguna constante. Las relaciones de dispersión son las estándar de la teoría lineal, deducidas en el texto y no consultadas en una fuente.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| — | Sin fuente externa | — | relaciones estándar que verifica el laboratorio | No se consultó una fuente para esta clase |

Límites: las relaciones de dispersión son estándar y no se consultó una fuente para esta clase.

## 12. Cómo ver las tasas

| Magnitud | Valor |
|---|---|
| `γ_max` dos haces | 0,353553 `ω_p` |
| `k v₀` del máximo | 0,6124 `ω_p` |
| umbral K-H | `U = 2 v_A` |
| `γ` a `U = 3 v_A` | 1,118 `k v_A` |

Descripción larga: la tasa de los haces sube hasta un máximo y cae a cero en `k v₀ = ω_p`.

## 13. Ejemplo trabajado: el máximo de los haces

**Paso 1 · Condición.** El máximo está en `a² = 3/8`.

**Paso 2 · Raíz.** `ω² = [(3/4+1) − √(1+3)]/2 = −0,125`.

**Paso 3 · Tasa.** `γ = √0,125 = 0,3536`.

## 14. Distintas formas de describir una inestabilidad

**Por fórmula:** relación de dispersión. **Por tabla:** `γ(k)`. **Por raíces:** polinomio numérico. **Por umbral:** `U = 2 v_A`.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** `γ_max` de los haces. *Pasos:* `a² = 3/8`.

<details><summary>Solución comentada</summary>

`0,3536 ω_p`.
</details>

**Ejercicio 2 · con una pista.** `k v₀` del máximo.

<details><summary>Solución comentada</summary>

`0,6124 ω_p`.
</details>

**Ejercicio 3 · casi autónomo.** `γ` para `a = 0,8`. *Pista:* tabla 8.1.

<details><summary>Solución comentada</summary>

`0,3113 ω_p`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** ¿Es inestable `a = 1,2`?

<details><summary>Solución comentada</summary>

No: `γ = 0`.
</details>

**Ejercicio 5.** `γ/(k v_A)` para `U = 3 v_A`.

<details><summary>Solución comentada</summary>

`√(9/4 − 1) = 1,118`.
</details>

**Ejercicio 6.** Ídem para `U = 4 v_A`.

<details><summary>Solución comentada</summary>

`√3 = 1,732`.
</details>

**Ejercicio 7.** Umbral de estabilidad de Kelvin–Helmholtz.

<details><summary>Solución comentada</summary>

`U = 2 v_A`.
</details>

**Ejercicio 8.** `γ` a `U = 1,9 v_A`.

<details><summary>Solución comentada</summary>

`0`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un colega dice que el campo siempre desestabiliza. Responde.

<details><summary>Solución comentada</summary>

Aquí estabiliza hasta `2 v_A`.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Qué limita una teoría lineal?

<details><summary>Solución comentada</summary>

Solo describe el crecimiento inicial.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Se midió alguna inestabilidad real?

<details><summary>Solución comentada</summary>

No: todo es normalizado.
</details>

**Ejercicio 12.** **Integrador.** Elabora tu *ficha de las inestabilidades*: tasas, máximo y umbral.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.3.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de las inestabilidades*: tasas, máximo y umbral.

<details><summary>Solución modelo</summary>

Secciones 8.1–8.3.
</details>

## 17. Laboratorio: inestabilidades

El script [inestabilidades.py](inestabilidades.py) resuelve las dos relaciones de dispersión por dos vías (**comprueba** el máximo `1/(2√2)` y el umbral `2 v_A`).

**Datos:** sin constantes; parámetros **normalizados**. **Predice antes de ejecutar:** ¿cuál es la tasa máxima? (`0,3536`.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
 k v0/wp  gamma cerrada  gamma Durand-Kerner
  0.2000       0.185624             0.185624
  0.4000       0.308194             0.308194
  0.6124       0.353553             0.353553
  0.8000       0.311339             0.311339
  0.9500       0.176145             0.176145
  1.0000       0.000000             0.000000
  1.2000       0.000000             0.000000
maximo analitico: k v0 = 0.61237 wp, gamma = 0.353553 wp ; maximo del barrido: k v0 = 0.612, gamma = 0.353553
  U/vA  gamma/(k vA) cerrada  gamma Durand-Kerner
  0.00              0.000000             0.000000
  1.00              0.000000             0.000000
  1.90              0.000000             0.000000
  2.00              0.000000             0.000000
  2.10              0.320156             0.320156
  3.00              1.118034             1.118034
  4.00              1.732051             1.732051
Pruebas superadas.
```

```bash
python programa/clases/B35/B35-C03-inestabilidades-de-plasma-cineticas-y-de-fluido/inestabilidades.py
```

**Límites:** lineal; haces fríos; fluido incompresible.

## 18. Errores frecuentes y cómo corregirlos

**Confundir la parte real con la tasa.** Se corrige con la sección 6.

**Olvidar el campo en Kelvin–Helmholtz.** Se corrige con 8.2.

**Usar la teoría lineal tras la saturación.** Se corrige con 8.3.

**Presentar lo normalizado como medición.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de las inestabilidades** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | conceptos de la clase | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con el análisis | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | fuentes con fecha | Declara lo ilustrativo |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular lo normalizado; no presentar el modelo como medición; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

El crecimiento máximo de los haces y el umbral de Kelvin–Helmholtz salen de la relación de dispersión y se confirman por raíces numéricas. Queda una pregunta: ¿cuándo deja de valer la descripción de fluido?

**Glosario español–inglés.** inestabilidad · *instability*; tasa de crecimiento · *growth rate*; dos haces · *two-stream*; cizalladura · *shear*; umbral · *threshold*.

**Continuidad.** [B35-C04](../B35-C04-colisiones-regimen-cinetico-y-ecuacion-de-vlasov/CLASE.md) estudia el régimen cinético.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B35-C02 — Ondas de Alfvén y ondas magnetosónicas](../B35-C02-ondas-de-alfven-y-ondas-magnetosonicas/CLASE.md) · [📚 Bloque B35](../../../tronco-comun/B35-fisica-avanzada-de-plasmas-y-mhd-espacial.md) · [Siguiente: B35-C04 — Colisiones, régimen cinético y ecuación de Vlasov →](../B35-C04-colisiones-regimen-cinetico-y-ecuacion-de-vlasov/CLASE.md)
<!-- /nav -->
