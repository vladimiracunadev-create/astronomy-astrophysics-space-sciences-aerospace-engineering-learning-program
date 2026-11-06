# B10-C11 — Valores singulares y SVD

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B10](../../../tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) · [← Anterior: B10-C10 — Descomposiciones matriciales](../B10-C10-descomposiciones-matriciales/CLASE.md) · [Siguiente: B10-C12 — Rotaciones en el plano y espacio →](../B10-C12-rotaciones-en-el-plano-y-espacio/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Undécima clase del bloque B10 y cierre de su segundo tramo. Los autovalores de [C08](../B10-C08-autovalores-y-autovectores/CLASE.md) solo describen bien a las matrices cuadradas y simétricas; las factorizaciones de [C10](../B10-C10-descomposiciones-matriciales/CLASE.md) no revelan el rango. La **descomposición en valores singulares (SVD)** sirve para cualquier matriz rectangular, muestra su rango efectivo, su número de condición y su mejor aproximación de bajo rango. Nivel N3. Verás la SVD, el rango numérico, la condición, el teorema de la aproximación óptima y su uso en la compresión de una imagen sintética. No verás cálculo iterativo de la SVD ni sus variantes aleatorizadas (B17).

## 2. Por qué esta clase existe

Un instrumento entrega una imagen de miles de píxeles; la mayor parte de su estructura se puede describir con muy pocos patrones. Una matriz de medidas puede tener columnas casi redundantes, de modo que un cálculo «técnicamente posible» sea inútil. La SVD responde las dos preguntas: cuántos patrones independientes hay y cuánta información se pierde al descartar los menos importantes.

La decisión central: **¿cuántas direcciones independientes hay realmente en estos datos y qué pierdo si me quedo con las principales?**

## 3. Lo que podrás hacer al terminar

1. Enunciar `A = U Σ Vᵀ` y el significado de sus factores.
2. Calcular valores singulares de una matriz pequeña a partir de `AᵀA`.
3. Determinar el rango efectivo y el número de condición.
4. Aplicar el teorema de Eckart–Young para aproximar con rango `k`.
5. Estimar el almacenamiento y el error de una aproximación de bajo rango.
6. Distinguir valores singulares de autovalores.

La evidencia es el **informe SVD con rango efectivo** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

Necesitas autovalores ([C08](../B10-C08-autovalores-y-autovectores/CLASE.md)), ortogonalidad ([C06](../B10-C06-producto-interno-y-ortogonalidad/CLASE.md)) y rango ([C02](../B10-C02-bases-y-dimension/CLASE.md)). Cinco preguntas:

1. ¿Cuáles son los autovalores de `[[25, 20], [20, 25]]`?
2. ¿Qué es una matriz ortogonal?
3. ¿Cuál es la traza de `[[3, 0], [4, 5]]ᵀ[[3, 0], [4, 5]]`?
4. ¿Qué rango tiene `[[1, 1], [1, 1]]`?
5. ¿Cuánto es `√(9 + 16 + 25)`?

<details>
<summary>Ver respuestas</summary>

1. `45` y `5`. 2. Una `Q` con `QᵀQ = I`. 3. `25 + 25 = 50`. 4. `1`. 5. `7,07`.
</details>

## 5. Un caso real: datos con columnas casi redundantes y una imagen sintética

Dos ejemplos **sintéticos**: (1) una matriz de `6 × 3` de medidas donde la tercera columna es la suma de las dos primeras más un ruido de `10⁻⁹`; (2) una «imagen» de `40 × 40` formada por tres patrones separables más un ruido de `10⁻³`, como podría ser un cuadro de un instrumento sin estructura fina. Ninguno es dato real; sirven para ver qué dice la SVD. Los dos son el ejemplo conductor.

## 6. Vocabulario

La **SVD** de una matriz real `A` de `m × n` es `A = U Σ Vᵀ`, con `U` (`m × m`, o `m × r` en la versión «económica») y `V` (`n × n`) de columnas ortonormales, y `Σ` diagonal con los **valores singulares** `σ₁ ≥ σ₂ ≥ … ≥ 0`. Las columnas de `U` son los **vectores singulares izquierdos**; las de `V`, los **derechos**. Los `σᵢ` son las raíces cuadradas de los autovalores de `AᵀA` (que es simétrica semidefinida positiva, C08). El **rango efectivo** es el número de valores singulares por encima de un umbral relativo. El **número de condición** es `κ = σ₁/σ_r`. La **norma de Frobenius** es `‖A‖_F = √(Σ aᵢⱼ²) = √(Σ σᵢ²)`. La **norma 2** es `σ₁`. La **aproximación de rango `k`** es `A_k = Σ_{i≤k} σᵢ uᵢ vᵢᵀ`.

## 7. Modelo mental: rotar, estirar, rotar

Cualquier matriz hace tres cosas: gira (o refleja) con `Vᵀ`, estira cada eje un factor `σᵢ`, y vuelve a girar con `U`.

```mermaid
flowchart LR
    A["Círculo unidad<br/>en el espacio de entrada"] --> B["Vᵀ: girar"]
    B --> C["Σ: estirar ejes<br/>por σ₁, σ₂, …"]
    C --> D["U: girar"]
    D --> E["Elipse de salida:<br/>semiejes σᵢ, direcciones uᵢ"]
```

*Descripción textual:* el círculo unidad se transforma en una elipse; sus semiejes miden los valores singulares y apuntan en las direcciones de los vectores singulares izquierdos.

Analogía: una masa circular de pan que se estira en una dirección y se encoge en otra. Su límite: en dimensiones mayores, los «ejes» son hiperelipsoides, que no se pueden dibujar.

## 8. La explicación, paso a paso

### 8.1 Un ejemplo a mano

Para `A = [[3, 0], [4, 5]]`: `AᵀA = [[25, 20], [20, 25]]`, con autovalores `45` y `5`. Los valores singulares son `√45 = 6,708` y `√5 = 2,236`. Comprobaciones: `σ₁σ₂ = 15 = |det A|`; `σ₁² + σ₂² = 50 = 9 + 16 + 25 = ‖A‖_F²`; `κ = σ₁/σ₂ = 3`.

### 8.2 Matriz casi de rango menor

Para `[[1, 1], [1, 1]]`: `AᵀA = [[2, 2], [2, 2]]`, autovalores `4` y `0`; `σ = 2` y `0`; rango 1. Una matriz con un valor singular tan pequeño que puede considerarse nulo está **casi** en un rango menor.

### 8.3 Rango efectivo

En la matriz sintética de `6×3` el laboratorio da `σ = 3,2175; 2,6753; 7,07 × 10⁻¹⁰`. El tercer valor es nueve órdenes de magnitud menor: rango efectivo `2` (umbral relativo `10⁻⁶`) y `κ = 4,55 × 10⁹`. El último vector singular derecho apunta, salvo signo, a `(1, 1, −1)/√3`, que es justamente la relación `c₁ + c₂ − c₃ ≈ 0` entre las columnas.

### 8.4 Condición

`κ(A) = σ₁/σ_n` es el factor máximo de amplificación de error relativo al resolver `A x = b` (C05). Además, `κ(AᵀA) = κ(A)²`: para una matriz aleatoria de `8×4` el laboratorio da `κ = 2,754`, `κ² = 7,585` y `κ(AᵀA) = 7,585`. Por eso mínimos cuadrados con ecuaciones normales pierde el doble de cifras (C07).

### 8.5 Aproximación de bajo rango

El **teorema de Eckart–Young** (resultado estándar sin cita específica aquí) dice que la mejor aproximación de rango `k` en norma 2 tiene error exactamente `σ_{k+1}`, y en norma de Frobenius `√(Σ_{i>k} σᵢ²)`. Es la mejor posible: ninguna otra matriz de rango `k` se acerca más.

### 8.6 La imagen sintética

Los primeros valores singulares son `200; 99,97; 66,56` y después `0,0115; 0,0111; 0,0102…` (el ruido). Hay un salto de cuatro órdenes de magnitud entre el tercero y el cuarto: la imagen es, en esencia, de rango 3. Con `k = 3` el error en norma 2 es `0,0115` (= `σ₄`) y en Frobenius `0,0372` (el ruido restante), con un almacenamiento de `k(m + n + 1) = 243` números en lugar de `1600` (15 %). Con `k = 1` el error es `99,97` y con `k = 2`, `66,56`: el patrón faltante.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Nota |
|---|---|---|---|
| `A` | matriz `m × n` | según el caso | datos |
| `U, V` | vectores singulares | adimensional | ortonormales |
| `σᵢ` | valores singulares | misma unidad que `A` | `≥ 0`, ordenados |
| `κ` | número de condición | adimensional | `σ₁/σ_r` |
| `A_k` | aproximación de rango `k` | igual que `A` | |
| `‖·‖₂`, `‖·‖_F` | normas matriciales | igual que `A` | `σ₁`, `√Σσᵢ²` |
| `k(m+n+1)` | almacenamiento de `A_k` | números | |

## 10. Convenciones y referencias

Los valores singulares se ordenan de mayor a menor. La versión «económica» de la SVD guarda solo las columnas necesarias. El umbral de rango efectivo se declara siempre (aquí `10⁻⁶` relativo). Las normas se nombran explícitamente. Las imágenes son sintéticas y sin unidades físicas.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NIST, *DLMF* §1.2(vi), versión vigente en línea al consultar | https://dlmf.nist.gov/1.2 | Autovalores y autovectores (1.2.70–1.2.72), traza (1.2.62–1.2.63), matrices simétricas (1.2.55) que sustentan `AᵀA` | Consultada el 2026-11-05 mediante extracción automática |
| S2 | NIST, *DLMF* §1.3 | https://dlmf.nist.gov/1.3 | Matrices simétricas con autovalores reales y autovectores ortonormales | Consultada el 2026-11-05 mediante extracción automática |

Límites: la SVD, el teorema de Eckart–Young y la relación `κ(AᵀA) = κ(A)²` son resultados estándar de álgebra lineal sin cita específica; ninguna de las dos secciones de DLMF consultadas trata la SVD. Los datos son **sintéticos**.

## 12. Cómo ver los valores singulares

Equivalente accesible a una gráfica de espectro singular de la imagen:

| Índice | Valor singular | Lectura |
|---|---|---|
| 1 | 200 | patrón principal |
| 2 | 99,97 | segundo patrón |
| 3 | 66,56 | tercer patrón |
| 4 | 0,0115 | ruido |
| 5 | 0,0111 | ruido |
| 6 | 0,0102 | ruido |

Descripción larga: tres barras altas seguidas de un escalón de cuatro órdenes de magnitud y de una meseta de valores casi iguales.

## 13. Ejemplo trabajado: ¿cuántos patrones tiene la imagen?

**Paso 1 · Datos.** Espectro singular de la sección 12 (imagen sintética de `40×40`).

**Paso 2 · Umbral.** Con umbral relativo `10⁻³`: `10⁻³ · 200 = 0,2`. Los valores `≥ 0,2` son los tres primeros: rango efectivo `3`.

**Paso 3 · Aproximación.** `A₃ = Σ_{i≤3} σᵢ uᵢ vᵢᵀ`; error en norma 2: `σ₄ = 0,0115`; error relativo `0,0115/200 = 5,7 × 10⁻⁵`.

**Paso 4 · Almacenamiento.** `3 · (40 + 40 + 1) = 243` números frente a `1600`: 15 %.

**Paso 5 · Sentido.** Descartar la meseta pierde el ruido y deja la estructura. Resultado sobre datos **sintéticos** y separables; una imagen astronómica real tiene un espectro singular que decae más despacio y exige juzgar qué pérdida es tolerable.

## 14. Distintas formas de obtener rango y condición

**Por determinante:** inútil (cero solo si es exacto). **Por eliminación:** da el rango en aritmética exacta, es frágil con ruido. **Por SVD:** el método de referencia. **Por QR con pivoteo de columnas:** más barato, menos informativo. La SVD nunca engaña, pero hay que elegir el umbral.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Halla los valores singulares de `[[1, 1], [1, 1]]`. *Pasos:* `AᵀA` y sus autovalores (8.2).

<details><summary>Solución comentada</summary>

`AᵀA = [[2, 2], [2, 2]]`, autovalores `4` y `0`; `σ = 2` y `0`. Rango `1`.
</details>

**Ejercicio 2 · con una pista.** Halla los valores singulares y el `κ` de `[[3, 0], [4, 5]]`. *Pista:* `AᵀA = [[25, 20], [20, 25]]`.

<details><summary>Solución comentada</summary>

`σ = 6,708` y `2,236`; `κ = 3` (8.1).
</details>

**Ejercicio 3 · casi autónomo.** Verifica `σ₁² + σ₂² = ‖A‖_F²` y `σ₁σ₂ = |det A|` para esa matriz.

<details><summary>Solución comentada</summary>

`45 + 5 = 50 = 9 + 0 + 16 + 25`; `6,708 · 2,236 = 15 = |3·5 − 0·4|` ✓.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Con espectro `[200; 100; 66; 0,011; 0,010]` y umbral relativo `10⁻³`, ¿cuál es el rango efectivo?

<details><summary>Solución comentada</summary>

Umbral `0,2`: valores por encima: `200, 100, 66`. Rango `3`.
</details>

**Ejercicio 5.** Para la imagen de 8.6, ¿cuál es el error en norma 2 de la mejor aproximación de rango 1 y qué fracción de `σ₁` representa?

<details><summary>Solución comentada</summary>

`σ₂ = 99,97`, es decir `50 %` de `σ₁ = 200`.
</details>

**Ejercicio 6.** Calcula el almacenamiento de `A_k` para `k = 1, 2, 3, 5` en una imagen de `40×40`.

<details><summary>Solución comentada</summary>

`81; 162; 243; 405` números frente a `1600` (5 %, 10 %, 15 %, 25 %).
</details>

**Ejercicio 7.** Interpreta `κ = 4,55 × 10⁹` de la matriz de `6×3` y su vector singular de menor valor.

<details><summary>Solución comentada</summary>

Casi singular: las columnas son casi dependientes (`c₁ + c₂ ≈ c₃`) y el vector singular derecho `(1,1,−1)/√3` da la relación. Resolver con ella pierde unas 9–10 cifras (C05).
</details>

**Ejercicio 8.** ¿Cuáles son los valores singulares de una matriz ortogonal?

<details><summary>Solución comentada</summary>

Todos valen `1` (`QᵀQ = I`); `κ = 1`: es la matriz mejor condicionada posible.
</details>

**Ejercicio 9 · transferencia.** Un instrumento produce cuadros de `1000×1000` píxeles de rango efectivo `k = 20`. ¿Cuánto se ahorra al almacenar `A_k`?

<details><summary>Solución comentada</summary>

`20 · (1000 + 1000 + 1) = 40 020` números frente a `10⁶`: 4 %, es decir 25 veces menos. Solo vale si el espectro realmente cae (no con ruido de fondo grande).
</details>

**Ejercicio 10 · transferencia.** El ruido de la imagen sintética tiene `σ_ruido = 10⁻³` por píxel y la imagen es de `40×40`. Estima el valor singular típico del ruido y compáralo con `σ₄ = 0,0115`.

<details><summary>Solución comentada</summary>

Para una matriz aleatoria `n×n` de desviación `s`, los valores singulares son del orden de `s√n` hasta `2s√n`: `10⁻³ · 6,3 = 0,0063` a `0,0126`. `0,0115` está en ese rango: es ruido (estimación de orden de magnitud con resultado estándar de matrices aleatorias).
</details>

**Ejercicio 11 · transferencia.** Alguien dice que los valores singulares de `[[0, 1], [0, 0]]` son sus autovalores. ¿Es cierto?

<details><summary>Solución comentada</summary>

No: los autovalores son `0, 0`, y `AᵀA = [[0, 0], [0, 1]]` da valores singulares `1` y `0`. Coinciden solo para matrices simétricas semidefinidas positivas.
</details>

**Ejercicio 12 · integrador.** Elabora tu **informe SVD con rango efectivo**: una matriz o imagen sintética tuya, espectro singular con el umbral declarado, rango efectivo, `κ`, aproximaciones de rango 1 a 5 con error y almacenamiento, y una nota sobre cuándo la aproximación sería inaceptable.

<details><summary>Solución modelo</summary>

Como 13 con tus datos, tabla de errores `σ_{k+1}` y de almacenamiento, verificación `‖A − A_k‖₂ = σ_{k+1}` del laboratorio, y la advertencia sobre imágenes reales.
</details>

## 17. Laboratorio: SVD, rango y compresión

El script [svd_y_rango.py](svd_y_rango.py) calcula la SVD de la matriz casi redundante y de la imagen sintética, verifica identidades y el teorema de aproximación óptima.

**Datos:** sintéticos, semilla fija. **Predice antes de ejecutar:** ¿cuántos valores singulares grandes esperas en la imagen? **Ejecución del 2026-11-05 (Python 3.12.9, numpy 2.4.4):**

```text
valores singulares de A: ['3.2175e+00', '2.6753e+00', '7.0719e-10']
rango efectivo (umbral 1e-6 relativo) = 2 | cond(A) = 4.550e+09
cond(B) = 2.7541; cond(B)^2 = 7.5852; cond(B^T B) = 7.5852
primeros 6 valores singulares de la imagen: ['200', '99.97', '66.56', '0.01146', '0.01105', '0.01016']
k=1: error (norma 2) = 9.9970e+01 = sigma_(k+1) = 9.9970e+01; Frobenius = 1.2010e+02; almacenamiento 81/1600
k=2: error (norma 2) = 6.6557e+01 = sigma_(k+1) = 6.6557e+01; Frobenius = 6.6557e+01; almacenamiento 162/1600
k=3: error (norma 2) = 1.1461e-02 = sigma_(k+1) = 1.1461e-02; Frobenius = 3.7202e-02; almacenamiento 243/1600
k=5: error (norma 2) = 1.0163e-02 = sigma_(k+1) = 1.0163e-02; Frobenius = 3.3623e-02; almacenamiento 405/1600
Pruebas superadas.
```

```bash
python programa/clases/B10/B10-C11-valores-singulares-y-svd/svd_y_rango.py
```

**Límites:** imagen separable y ruido blanco; el teorema se comprueba numéricamente, no se demuestra; sin datos reales.

## 18. Errores frecuentes y cómo corregirlos

**Decidir el rango por el determinante.** Se corrige en la sección 14 y el ejercicio 7.

**Confundir valores singulares con autovalores.** Se corrige con el ejercicio 11.

**Elegir el umbral sin declararlo.** Se corrige en las secciones 10 y 13.

**Creer que comprimir no pierde nada.** Se corrige con los ejercicios 5 y 9.

**Olvidar que `κ(AᵀA) = κ(A)²`.** Se corrige en la sección 8.4.

## 19. Cómo sabrás que vas bien

Tras 8.1: ¿calculas los valores singulares de una `2×2`? Si no, ejercicio 2. Tras 8.3: ¿qué significa un valor singular de `10⁻¹⁰`? Si no, ejercicio 7. Tras 8.5: ¿cuál es el error exacto de una aproximación de rango `k`? Si no, ejercicio 5.

## 20. Qué entregas y cómo se evalúa

El producto es tu **informe SVD con rango efectivo** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Cálculo | Confunde con autovalores | Valores sin comprobar | Valores y identidades verificadas | Con vectores singulares |
| Rango efectivo | Sin umbral | Umbral arbitrario | Umbral declarado | Justificado por el espectro |
| Aproximación | Sin error | Error aproximado | `σ_{k+1}` y almacenamiento | Con discusión de pérdida |
| Interpretación | Sin contexto | Dice «comprime» | Relaciona con ruido y señal | Señala límites del caso real |
| Fuentes y rotulado | Sin fuente | Sin fecha | Con localizador y fecha | Rotula sintético |

**Condiciones críticas:** declarar el umbral del rango; rotular lo sintético; no afirmar compresión sin cuantificar el error; citar solo fuentes consultadas.

## 21. Ética, seguridad y límites

Descartar componentes pequeños también puede descartar señales débiles pero reales (por ejemplo, un planeta tenue en una imagen). Antes de truncar datos científicos hay que decir qué se pierde y para qué. Accesibilidad: tablas equivalentes a las figuras, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

La SVD descompone cualquier matriz en giro–estirón–giro; los valores singulares dan el rango efectivo y la condición; Eckart–Young garantiza que la aproximación truncada es la mejor posible; truncar es una decisión que pierde información. Queda abierta una pregunta: ¿cómo se describe, con matrices, la orientación de un objeto en el espacio, empezando por rotaciones simples?

**Glosario español–inglés.** descomposición en valores singulares · *singular value decomposition (SVD)*; valor singular · *singular value*; vector singular · *singular vector*; rango efectivo · *effective rank*; número de condición · *condition number*; aproximación de bajo rango · *low-rank approximation*; norma de Frobenius · *Frobenius norm*.

**Continuidad.** B10-C12 reutiliza tu capacidad de **interpretar una matriz como giro y estirón** para estudiar las rotaciones del plano y del espacio.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B10-C10 — Descomposiciones matriciales](../B10-C10-descomposiciones-matriciales/CLASE.md) · [📚 Bloque B10](../../../tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) · [Siguiente: B10-C12 — Rotaciones en el plano y espacio →](../B10-C12-rotaciones-en-el-plano-y-espacio/CLASE.md)
<!-- /nav -->
