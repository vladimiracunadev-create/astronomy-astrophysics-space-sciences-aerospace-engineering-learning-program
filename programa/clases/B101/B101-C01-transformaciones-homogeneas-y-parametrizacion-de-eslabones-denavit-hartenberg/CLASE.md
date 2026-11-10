# B101-C01 — Transformaciones homogéneas y parametrización de eslabones (Denavit-Hartenberg)

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B101](../../../tronco-comun/B101-manipuladores-roboticos-espaciales.md) · [← Anterior: B100-C07 — Dependencia de suministros terrestres y cierre de lazos logísticos](../../B100/B100-C07-dependencia-de-suministros-terrestres-y-cierre-de-lazos-logisticos/CLASE.md) · [Siguiente: B101-C02 — Cinemática inversa y redundancia de manipuladores →](../B101-C02-cinematica-inversa-y-redundancia-de-manipuladores/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 1 del bloque B101. Nivel N3. Aprendes a **describir un brazo como una cadena de transformaciones homogéneas**: una matriz de 4×4 que junta rotación y traslación y la convención de Denavit-Hartenberg (D-H), que reduce cada eslabón a cuatro parámetros. Trabajas con un brazo **sintético** de siete articulaciones rotacionales. Ningún dato es de un brazo real.

## 2. Por qué esta clase existe

Para mover un brazo hay que saber dónde está su extremo. Si el marco de cada eslabón está mal puesto, todo lo que sigue (cinemática inversa, singularidades, calibración) hereda el error. La decisión central: **¿cómo expreso la posición y la orientación del extremo en el marco de la base a partir de los ángulos de las articulaciones?**

## 3. Lo que podrás hacer al terminar

1. Construir una matriz homogénea de 4×4 y componer transformaciones en el orden correcto.
2. Invertir una transformación homogénea con `[Rᵀ, −Rᵀp]`.
3. Escribir la matriz D-H estándar de un eslabón y su descomposición `Rz Tz Tx Rx`.
4. Calcular la cinemática directa de un brazo de 7 articulaciones y verificarla.
5. Cambiar un punto de la herramienta del marco `{E}` al marco `{0}`.
6. Separar lo consultado (que los brazos de la estación tienen siete articulaciones) de lo sintético.

La evidencia es la **tabla D-H con la posición del extremo** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es una matriz de rotación y qué propiedades tiene?
2. ¿Qué es un cambio de marco de referencia?
3. ¿Cuánto vale `Rz(90°)` aplicada a `(0, 1, 0)`?
4. ¿Qué es el producto de matrices y por qué importa el orden?
5. ¿Qué es una comprobación independiente?

<details>
<summary>Ver respuestas</summary>

1. Una matriz ortogonal con determinante 1: `RRᵀ = I`. 2. Expresar las coordenadas de un mismo punto en otra base. 3. `(−1, 0, 0)`. 4. El producto no conmuta: `AB ≠ BA`. 5. Calcular lo mismo por otro camino y comparar.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa rotaciones y cambio de marcos (bloque B10).

## 5. Un caso de contexto y casos de referencia

El comunicado de Airbus del 5 de julio de 2021 (F1) describe el European Robotic Arm (ERA): 11,3 m de longitud, siete articulaciones y una precisión de 5 mm. El resumen de Razvi y Burns (F2) describe el manipulador de la estación con un diseño de 7 grados de libertad. En esta clase **no** usamos sus dimensiones: usamos un brazo sintético de 7 articulaciones con eslabones de 0,4, 0,6, 0,6 y 0,3 m, cuyo alcance con el brazo estirado es de 1,9 m.

## 6. Vocabulario

**Transformación homogénea:** matriz `T = [R p; 0 1]` de 4×4. **Marco `{0}`:** marco de la base. **Marco `{E}`:** marco del extremo. **Parámetros D-H:** `a` (longitud), `α` (torsión), `d` (desplazamiento) y `θ` (ángulo articular). **Cinemática directa:** de los ángulos al extremo. **Grados de libertad:** movimientos independientes.

## 7. Modelo mental: una cadena de marcos

```mermaid
flowchart LR
    B["Marco 0<br/>base"] -->|"T1(q1)"| M1["Marco 1"]
    M1 -->|"T2(q2)"| M2["Marco 2"]
    M2 -->|"..."| M6["Marco 6"]
    M6 -->|"T7(q7)"| E["Marco E<br/>extremo"]
```

*Descripción textual:* la posición del extremo en `{0}` es el producto `T = T1 T2 … T7`; cada factor depende de una sola articulación.

Analogía: un tren de eslabones donde cada vagón se orienta respecto del anterior. Límite: la analogía no muestra que el orden de las matrices importa y que cada giro es sobre el eje de la articulación.

## 8. La explicación, paso a paso

### 8.1 Qué se sabe de los brazos reales

F1 y F2 solo respaldan que el ERA y el manipulador de la estación son brazos de siete articulaciones y que el ERA puede cambiar de punto base. El ECSS-E-ST-10-09C *Reference coordinate system* aparece en el listado de F3: confirma que existe una norma de sistema de referencia, pero no se consultó su texto. La convención D-H y todo lo demás es matemática estándar que no se consultó en un libro concreto (N2) y que verifica el laboratorio.

### 8.2 La matriz homogénea

`T = [R p; 0 1]` aplica a un punto `x` (en coordenadas homogéneas `(x, 1)`) la rotación `R` y luego la traslación `p`. Compone con `T_AC = T_AB T_BC`. Su inversa es `T⁻¹ = [Rᵀ, −Rᵀp; 0 1]`. En el laboratorio, la diferencia entre `inv(T)` y esa fórmula es de 1,67×10⁻¹⁶.

### 8.3 La matriz D-H estándar

`T_i = Rz(θᵢ) Tz(dᵢ) Tx(aᵢ) Rx(αᵢ)`, de modo que el eje de la articulación `i` es `z_{i−1}`. En forma cerrada:

`[cθ  −sθ cα   sθ sα   a cθ; sθ   cθ cα  −cθ sα   a sθ; 0  sα  cα  d; 0 0 0 1]`.

El laboratorio compara la forma cerrada con el producto elemental en 1 000 casos al azar: diferencia máxima 0.

### 8.4 El brazo sintético

| `i` | `α` (grados) | `a` (m) | `d` (m) |
|---|---|---|---|
| 1 | −90 | 0 | 0,40 |
| 2 | 90 | 0 | 0 |
| 3 | −90 | 0 | 0,60 |
| 4 | 90 | 0 | 0 |
| 5 | −90 | 0 | 0,60 |
| 6 | 90 | 0 | 0 |
| 7 | 0 | 0 | 0,30 |

Con `q = 0` el brazo queda estirado a lo largo de `z₀`: `p = (0, 0, 1,9)` m y `R = I`. Con `q = [30, −40, 25, 60, −35, 50, 20]°` el extremo está en `(−0,0628; 0,2068; 1,5291)` m, `R` es ortonormal (`|RRᵀ − I| = 2,2×10⁻¹⁶`, `det R = 1`) y la distancia al origen, 1,5443 m, no supera el alcance de 1,9 m.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `T` | transformación homogénea | — (4×4) | `[R p; 0 1]` |
| `R` | rotación | — (3×3) | `det R = 1` |
| `p` | posición del extremo en `{0}` | m | `(−0,0628; 0,2068; 1,5291)` |
| `a, d` | longitud y desplazamiento D-H | m | tabla 8.4 |
| `α, θ` | torsión y ángulo articular | rad (grados en las tablas) | tabla 8.4 |

## 10. Convenciones y referencias

Sistema de referencia: `{0}` fijo a la base, `z₀` vertical hacia arriba, dextrógiro; `{E}` fijo al extremo. Convención D-H **estándar** (distal). Unidades SI; ángulos en radianes en el código. Tolerancias: matrices `< 10⁻¹²`. Todo dato del brazo (longitudes, torsiones, ángulos de ejemplo) es **sintético**. Versiones: Python 3.12.9, numpy 2.4.4.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| F1 | Airbus, comunicado «Airbus-built European Robotic Arm ready for Space», Leiden, 5-07-2021 — https://www.airbus.com/sites/g/files/jlcbta136/files/4b7e903e07e8e840d723ad3d1796c9c9_EN-Airbus-SpS-Press-Release-Airbus-built-European-Robotic-Arm-ready-for-Space.pdf (consultada 2026-11-10; texto extraído del PDF con PyMuPDF) | página 1 | el European Robotic Arm (ERA) mide 11,3 m, tiene siete articulaciones, mueve 3 000 kg de forma rutinaria y hasta 8 000 kg en modo lento y opera con una precisión de 5 mm; puede «caminar» de un punto base a otro | Consultada (comunicado de prensa del fabricante: no es una especificación técnica) |
| F2 | Razvi, S. y Burns, S. H. (NASA JSC), «Evolution of the Space Station Robotic Manipulator», NASA NTRS 20070010589, 2007 — https://ntrs.nasa.gov/citations/20070010589 (consultada 2026-11-10) | resumen extendido (solo el resumen) | el manipulador de la estación (Canadarm2) tiene un diseño de 7 grados de libertad, con base cambiable que le permite desplazarse a puntos base | Consultada (solo el resumen; no se consultaron longitud ni carga) |
| — | Textos de robótica (Denavit y Hartenberg, 1955; Craig; Siciliano et al.; Spong et al.) | — | las matrices D-H, el jacobiano, la pseudoinversa y los mínimos cuadrados son resultados estándar que verifica cada laboratorio | No consultada en una fuente concreta |
| — | Longitud, masa y carga de Canadarm2; especificaciones de otros brazos (Kibo, Shuttle Arm) | — | — | No consultada |

Límites: ninguna fuente consultada da una tabla D-H ni longitudes de eslabones; el brazo de la clase no representa a ningún brazo real.

## 12. Cómo ver la cadena

| Magnitud | Valor |
|---|---|
| `p` con `q = 0` | `(0, 0, 1,9)` m |
| `p` con `q` de ejemplo | `(−0,0628; 0,2068; 1,5291)` m |
| `det R` | 1,000000000000 |
| diferencia D-H cerrada contra elemental | 0 (1 000 casos) |

Descripción larga: los orígenes sucesivos de los marcos 1 a 7 distan `0,4; 0; 0,6; 0; 0,6; 0; 0,3` m, que son los `dᵢ` porque `aᵢ = 0`.

## 13. Ejemplo trabajado: un brazo planar de dos eslabones

**Paso 1 · Matrices.** Con `l₁ = 0,6`, `l₂ = 0,5`, `q₁ = 0,7` rad y `q₂ = −0,4` rad: `T = T₁ T₂`, con `a = l`, `α = 0`, `d = 0`.

**Paso 2 · Posición.** `x = l₁ cos q₁ + l₂ cos(q₁+q₂) = 0,936574` m; `y = l₁ sin q₁ + l₂ sin(q₁+q₂) = 0,534291` m.

**Paso 3 · Verificación.** El laboratorio compara el producto de matrices con la fórmula: coinciden en seis cifras.

**Paso 4 · Decisión.** Se acepta la parametrización: cada articulación aporta un factor y el orden de los factores sigue el de la cadena.

## 14. Distintas formas de describir la postura

**Matriz homogénea (esta clase):** `T` de 4×4. **D-H modificada:** otra convención con los mismos resultados y otra posición del eje `x`; no se usa aquí. **Cuaternión y vector:** orientación con cuatro números más la posición; se relaciona con B10. Las tres describen la misma postura y se convierten entre sí.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Un marco `B` está rotado 90° sobre `z` y trasladado `(1, 0, 0)` respecto de `A`. ¿Dónde está en `A` el punto `(0, 1, 0)` de `B`? *Pasos:* `R x + t`.

<details><summary>Solución comentada</summary>

`Rz(90°)(0, 1, 0) = (−1, 0, 0)`; sumando `(1, 0, 0)` da `(0, 0, 0)`.
</details>

**Ejercicio 2 · con una pista.** Planar 2R con `l₁ = 0,6`, `l₂ = 0,5`, `q₁ = 90°`, `q₂ = 0`: ¿dónde está el extremo? *Pista:* los dos eslabones apuntan a `y`.

<details><summary>Solución comentada</summary>

`(0; 1,1)` m: `0,6 + 0,5` en `y`.
</details>

**Ejercicio 3 · casi autónomo.** Escribe la matriz D-H con `a = 0,5`, `α = 0`, `d = 0`, `θ = 90°`.

<details><summary>Solución comentada</summary>

`[0 −1 0 0; 1 0 0 0,5; 0 0 1 0; 0 0 0 1]` (`a cos θ = 0`, `a sin θ = 0,5`).
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Calcula `T⁻¹` si `R = Rz(90°)` y `p = (1, 2, 3)`.

<details><summary>Solución comentada</summary>

`Rᵀ = [0 1 0; −1 0 0; 0 0 1]` y `Rᵀp = (2, −1, 3)`, luego `p' = (−2, 1, −3)`.
</details>

**Ejercicio 5 · autónomo.** ¿Por qué con `q = 0` el extremo está en `(0, 0, 1,9)`?

<details><summary>Solución comentada</summary>

Los `αᵢ` alternan −90° y 90° y se cancelan: `R = I`. Como `aᵢ = 0`, el extremo suma los `dᵢ` a lo largo de `z`: `0,4 + 0,6 + 0,6 + 0,3 = 1,9`.
</details>

**Ejercicio 6 · autónomo.** Una transformación rígida general tiene 6 parámetros y D-H usa 4: ¿por qué?

<details><summary>Solución comentada</summary>

La convención fija los marcos (`z` sobre el eje de la articulación, `x` sobre la normal común), lo que elimina dos grados de libertad de la elección.
</details>

**Ejercicio 7 · autónomo.** Cuenta las constantes y las variables de la tabla D-H del brazo sintético.

<details><summary>Solución comentada</summary>

21 constantes (`a, α, d` por 7 eslabones) y 7 variables (`θ`).
</details>

**Ejercicio 8 · autónomo.** Compara el origen de `T_A T_B` y de `T_B T_A` si `T_A` gira 30° sobre `z` y `T_B` traslada `(1, 0, 0)`.

<details><summary>Solución comentada</summary>

`T_A T_B`: `(0,866; 0,5; 0)`; `T_B T_A`: `(1, 0, 0)`. No conmutan.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Una cámara está a `(0,05; 0; 0,10)` m en `{E}` y el brazo está con `q = 0`. ¿Dónde está en `{0}`?

<details><summary>Solución comentada</summary>

Con `q = 0`, `R = I` y `p = (0, 0, 1,9)`: `(0,05; 0; 2,0)` m.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** Un colega usa la tabla de la clase para el brazo real de la estación. ¿Es válido?

<details><summary>Solución comentada</summary>

No: la tabla es sintética. Lo consultado solo respalda las siete articulaciones (F2); las longitudes de un brazo real no se consultaron (N1).
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** Si `d₃` real es 0,602 m en vez de 0,600 m, ¿qué error de posición produce con `q = 0`?

<details><summary>Solución comentada</summary>

Los eslabones están alineados: el error es `2 mm` a lo largo de `z`. Esto motiva la calibración (B101-C05).
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *tabla D-H con la posición del extremo*: la tabla, `p` para `q = 0` y para una configuración tuya, la comprobación de `R` y la lista de qué es consultado, no consultado y sintético.

<details><summary>Solución comentada</summary>

Secciones 8.4 y 12 y la salida del laboratorio.
</details>

## 17. Laboratorio: cinemática directa D-H

El script [dh_cadena.py](dh_cadena.py) verifica la matriz D-H cerrada contra el producto elemental, el brazo planar contra su fórmula, la cinemática directa del brazo de 7 articulaciones y la inversa homogénea; **comprueba** que `R` es de rotación y que el extremo no supera el alcance. Usa la biblioteca común [b101_comun.py](../b101_comun.py).

**Datos:** brazo y ángulos **sintéticos**; sin constantes con fuente. **Predice antes de ejecutar:** ¿cuánto vale `p` con `q = 0`? (`(0, 0, 1,9)`.) Ejecución del 2026-11-10 (Python 3.12.9, numpy 2.4.4):

```text
Python 3.12.9 | numpy 2.4.4
Datos SINTETICOS: brazo de 7 articulaciones, longitudes 0.4/0.6/0.6/0.3 m (didactico)
Tabla D-H estandar: i, alpha [grados], a [m], d [m]
  1   -90.0   0.00   0.40
  2    90.0   0.00   0.00
  3   -90.0   0.00   0.60
  4    90.0   0.00   0.00
  5   -90.0   0.00   0.60
  6    90.0   0.00   0.00
  7     0.0   0.00   0.30
D-H cerrada contra Rz Tz Tx Rx (1000 casos): diferencia maxima = 0.00e+00
Planar 2R: x,y D-H = (0.936574, 0.534291) ; formula = (0.936574, 0.534291)
Extremo con q = 0: p = (0.0000, 0.0000, 1.9000) m (alcance maximo 1.9 m)
Con q = [30 -40 25 60 -35 50 20] grados:
  p [m] = (-0.0628, 0.2068, 1.5291)
  R ortonormal: |R R^T - I| = 2.22e-16 ; det R = 1.000000000000
Inversa: inv(T) contra [R^T, -R^T p]: diferencia = 1.67e-16
Punto de {E} (0.05, 0, 0.10) en {0}: (0.0394, 0.2521, 1.5308) m
Distancia entre origenes sucesivos [m]: 0.400 0.000 0.600 0.000 0.600 0.000 0.300
|p| = 1.5443 m <= 1.9 m
Pruebas superadas.
```

```bash
python programa/clases/B101/B101-C01-transformaciones-homogeneas-y-parametrizacion-de-eslabones-denavit-hartenberg/dh_cadena.py
```

**Límites:** solo rotacionales, sin holguras ni flexión; sin orientación en la salida.

## 18. Errores frecuentes y cómo corregirlos

**Multiplicar en el orden contrario.** `T = T₁ T₂ … T₇`, de la base al extremo (8.2)

**Confundir `a` con `d`.** `a` es la longitud sobre `x`; `d`, el desplazamiento sobre `z` (8.3)

**Presentar el brazo de la clase como uno real.** Revisa la sección 11

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué matriz da la posición del punto de una herramienta en `{0}`? Si dudas, repasa el ejercicio 9. Tras el laboratorio: ¿qué compara la prueba de la forma cerrada? (ver sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **tabla D-H del brazo con su posición del extremo** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Explica el método y su dominio | Explica los límites y las alternativas |
| Cálculo | Sin unidades | Con errores | Resultados con unidades y comprobados | Resuelve casos nuevos |
| Numérico | Sin comprobar | Un caso | Verifica con una comprobación independiente en varios casos | Interpreta las diferencias y los fallos |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo sintético y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular los datos como sintéticos; verificar cada resultado con una comprobación independiente; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: el brazo de siete articulaciones es un modelo didáctico, sin relación con las dimensiones reales de un brazo de vuelo. No enseña a operar hardware real. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

La cinemática directa da el extremo a partir de los ángulos y se verifica por dos caminos. Queda una pregunta: ¿cómo se encuentran los ángulos que llevan el extremo a una posición dada?

**Glosario español–inglés.** transformación homogénea · *homogeneous transformation*; parámetros Denavit-Hartenberg · *Denavit-Hartenberg parameters*; cinemática directa · *forward kinematics*; eslabón · *link*; articulación · *joint*; efector final · *end effector*.

**Continuidad.** [B101-C02](../B101-C02-cinematica-inversa-y-redundancia-de-manipuladores/CLASE.md) trata la cinemática inversa y la redundancia.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B100-C07 — Dependencia de suministros terrestres y cierre de lazos logísticos](../../B100/B100-C07-dependencia-de-suministros-terrestres-y-cierre-de-lazos-logisticos/CLASE.md) · [📚 Bloque B101](../../../tronco-comun/B101-manipuladores-roboticos-espaciales.md) · [Siguiente: B101-C02 — Cinemática inversa y redundancia de manipuladores →](../B101-C02-cinematica-inversa-y-redundancia-de-manipuladores/CLASE.md)
<!-- /nav -->
