# B13-C22 — Parámetros de orientación terrestre: precesión, nutación, UT1 y movimiento polar

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B13](../../../tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) · [← Anterior: B13-C21 — Sistema de referencia celeste ICRF y cuásares](../B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md) · [Siguiente: B13-C23 — Estabilidad y deriva temporal de instrumentos →](../B13-C23-estabilidad-y-deriva-temporal-de-instrumentos/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 22 del bloque B13 (ampliación `0.2.0`). [C10](../B13-C10-tiempo-sidereo-local-y-terrestre/CLASE.md) trató el ángulo de rotación terrestre; [C11](../B13-C11-sistemas-de-referencia-terrestres/CLASE.md), el marco terrestre; [C21](../B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md), el celeste. Aquí unes los tres con la cadena de transformación `[GCRS] = Q R W [ITRS]` y estudias los **parámetros de orientación terrestre (EOP)**: UT1−UTC, movimiento polar y movimiento del polo celeste (precesión y nutación). Nivel N2. Construyes las matrices de rotación y mides en metros el efecto de cada parámetro. No implementas el modelo completo de precesión-nutación ni descargas series reales de EOP.

## 2. Por qué esta clase existe

Una estación terrestre apunta a una nave en el sistema celeste. Para ello debe saber cuánto ha girado la Tierra, hacia dónde apunta su eje en el cielo y dónde está ese eje dentro de la corteza. Esas tres cosas cambian de forma que no se puede predecir con una fórmula exacta: hay que **medirlas** y publicarlas. Ignorar una de ellas desplaza la estación en el marco celeste decenas de metros o más.

La decisión central: **¿qué parámetro de orientación domina el error y qué precisión necesito en cada uno?**

## 3. Lo que podrás hacer al terminar

1. Escribir la cadena `[GCRS] = Q(t) R(t) W(t) [ITRS]` y decir qué representa cada matriz.
2. Definir UT1−UTC, movimiento polar y celestial pole offsets.
3. Construir matrices de rotación elementales y comprobar que son ortogonales.
4. Convertir un error de cada parámetro en metros sobre la superficie.
5. Reconocer los periodos del movimiento polar (Chandler y anual) y su batido.
6. Verificar los cálculos con identidades exactas.

La evidencia es la **tabla de efectos de los EOP en metros** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

Necesitas el ERA ([C10](../B13-C10-tiempo-sidereo-local-y-terrestre/CLASE.md)), ejes terrestres ([C11](../B13-C11-sistemas-de-referencia-terrestres/CLASE.md)), el marco celeste ([C21](../B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md)) y matrices de rotación ([B10](../../../tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md)). Cinco preguntas:

1. ¿Qué propiedad cumple una matriz de rotación `R`: `R Rᵀ = ?`
2. ¿Cuánto es `1 mas` en metros a `6 378 137 m`?
3. ¿Cuánto vale `|UT1 − UTC|` como máximo?
4. ¿Qué es un periodo de batido entre dos frecuencias?
5. ¿Cuánto es `0,9 s × 465 m/s`?

<details>
<summary>Ver respuestas</summary>

1. La identidad `I`. 2. `3,09 cm`. 3. Menos de `0,9 s`. 4. El periodo de la diferencia de frecuencias, `1/|1/P₁ − 1/P₂|`. 5. `418,5 m`.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa C10, C21 y B10.

## 5. Un caso real: tres números que cambian cada día

Las convenciones del IERS (S1) relacionan el ITRS y el GCRS por `[GCRS] = Q(t) R(t) W(t) [ITRS]`: `W` es el movimiento polar, `R` la rotación en torno al eje (el ERA, C10) y `Q` el movimiento del polo celeste. Los EOP son las cantidades medidas que alimentan esas matrices: las coordenadas del polo `(x_p, y_p)`, `UT1 − UTC` y los desplazamientos del polo celeste. El IERS afirma que este vínculo está disponible a diario con exactitud de `±0,1 mas` (S1, cap. 2). Este es el **ejemplo conductor**: ¿cuántos metros vale cada error?

## 6. Vocabulario

Los **parámetros de orientación terrestre (EOP)** describen la orientación del Polo Celeste Intermedio (CIP) en el sistema terrestre y en el celeste y la orientación de la Tierra en torno a ese eje (S1, 2.2.2). El **CIP** es el polo de referencia que separa el movimiento del eje en precesión-nutación y en movimiento polar (S1, glosario). El **movimiento polar** `(x_p, y_p)` es el movimiento del CIP respecto de la corteza; está dominado por el bamboleo de Chandler (periodo de unos `435 d`) y una componente anual (S1, glosario y cap. 5). **UT1 − UTC** es la diferencia entre el tiempo de rotación terrestre y el civil; se mantiene por debajo de `0,9 s` con segundos intercalares (C09). La **precesión-nutación** es el movimiento del CIP en el sistema celeste; el IERS publica además desplazamientos del polo celeste (*celestial pole offsets*) respecto del modelo IAU 2006/2000A (S1, glosario). Una **matriz de rotación elemental** `R₁`, `R₂`, `R₃` gira alrededor de `x`, `y` o `z`.

## 7. Modelo mental: tres engranajes en serie

Piensa en tres engranajes encadenados: el primero (`W`) mueve el eje dentro de la Tierra, el segundo (`R`) gira la Tierra alrededor de ese eje, el tercero (`Q`) mueve el eje respecto de las estrellas. El orden importa; cada engranaje tiene su propia incertidumbre y su propio periodo.

```mermaid
flowchart LR
    I["[ITRS]<br/>(ligado a la corteza)"] -->|"W(t): movimiento polar<br/>x_p, y_p"| T["TIRS"]
    T -->|"R(t): ERA = f(UT1)"| C["CIRS"]
    C -->|"Q(t): precesión-nutación<br/>+ offsets del polo celeste"| G["[GCRS]<br/>(ligado a los cuásares)"]
```

*Descripción textual:* un vector en el sistema terrestre se corrige por movimiento polar, se gira por el ángulo de rotación terrestre y se lleva al sistema celeste con la matriz de precesión-nutación.

Analogía: tres engranajes en cadena. Su límite: los tres movimientos no son independientes físicamente (el eje de rotación y el eje de figura interactúan), pero la parametrización del IERS los trata por separado.

## 8. La explicación, paso a paso

### 8.1 La cadena

`[GCRS] = Q(t) R(t) W(t) [ITRS]` (S1, ec. 5.1): `Q(t)` surge del movimiento del polo celeste en el sistema celeste, `R(t)` de la rotación de la Tierra en torno al eje asociado al polo y `W(t)` del movimiento polar. La ecuación vale para cualquier elección de polo y de origen sobre su ecuador (S1, cap. 5). Aquí se calcula `R` y `W`; `Q` se toma igual a la identidad para aislar los otros efectos.

### 8.2 Matrices elementales

`R₃(θ)` gira alrededor de `z`: `[[c, s, 0], [−s, c, 0], [0, 0, 1]]` con `c = cos θ`, `s = sen θ`; `R₁` y `R₂` análogas. Para giros pequeños se usa `W ≈ R₁(−y_p) R₂(−x_p)`, una forma simplificada de esta clase; el IERS (S1, cap. 5) escribe `W` con sus propias convenciones de signo e incluye un pequeño giro adicional `s′`. Toda matriz de rotación cumple `R Rᵀ = I` y `det R = 1`: el laboratorio lo verifica a `10⁻¹⁴`.

### 8.3 UT1 − UTC

El ERA es función de UT1 (C10, S1 ec. 5.14); con `UT1 = UTC + (UT1 − UTC)` hay que sumar el valor publicado. Un error `δ` en `UT1 − UTC` gira la estación en `ω δ` radianes: con `ω = 7,292 115 × 10⁻⁵ rad/s` (S1, Tabla 1.2), `0,9 s` mueven un punto del ecuador `0,9 × 7,292 115 × 10⁻⁵ × 6 378 137 = 418,6 m`.

### 8.4 Movimiento polar

Es pequeño pero grande en metros: `x_p = 0,1″` desplaza el polo terrestre `3,082 m`; `0,5″`, `15,409 m` (el laboratorio coincide con `a θ` a `10⁻⁶`). El IERS indica que los bamboleos chandleriano y anual pueden alcanzar amplitudes del orden de `0,5″` y `0,1″` (S1, cap. 5).

### 8.5 Chandler, anual y batido

El periodo chandleriano es de unos `435 d` (S1, glosario) y el anual `365,25 d`. Dos oscilaciones de periodos `P₁` y `P₂` se suman y se realzan o se cancelan con periodo de batido `1/|1/P₁ − 1/P₂| = 2278 d = 6,24 años`. Con una serie **sintética** (`0,20″` chandleriano y `0,08″` anual) la amplitud máxima es `0,28″`, y esa suma desplaza a una estación de `|r| ≈ 6,4 × 10⁶ m` unos `8,6 m`.

### 8.6 Precisión pedida

Un `1 mas` de error en el polo celeste (precesión-nutación) es `3,09 cm` en la superficie; el vínculo celeste–terrestre del IERS, `±0,1 mas`, equivale a `3,1 mm` en la superficie. Por eso la geodesia espacial y la navegación de espacio profundo exigen EOP publicados a diario; la predicción de UT1 y de movimiento polar se degrada con el tiempo y para operaciones se usan los productos vigentes (C09, C19).

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor o nota |
|---|---|---|---|
| `Q, R, W` | matrices de precesión-nutación, rotación y movimiento polar | — | ortogonales |
| `x_p, y_p` | coordenadas del polo | ″ | amplitudes hasta `0,5″` (Chandler) y `0,1″` (anual) |
| `UT1 − UTC` | diferencia de rotación y tiempo civil | s | `< 0,9` |
| `ω` | velocidad angular de la Tierra | rad/s | `7,292 115 × 10⁻⁵` |
| `P_C`, `P_A`, `P_b` | periodos Chandler, anual, batido | d | `435`; `365,25`; `2278` |
| `ε`, `mas` | error angular | `4,848 × 10⁻⁹ rad` por mas | `1 mas ≈ 3,09 cm` |

## 10. Convenciones y referencias

Las rotaciones se escriben pasivas (`R₃(θ)` transforma coordenadas); se usan giros pequeños para `W` y no se incluye el pequeño giro `s′` (menos de `0,4 mas` en el próximo siglo según S1) ni mareas ni libración. `Q = I` en el laboratorio. Las series de `x_p` son **sintéticas**; no se usan valores reales de EOP.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | IERS, *IERS Conventions (2010)*, TN36: cap. 2 (§2.2.2), cap. 5 (§5.1, §5.5, ec. 5.1 y 5.14), Tabla 1.2, glosario | https://iers-conventions.obspm.fr/content/tn36.pdf | Cadena `Q R W`; EOP y su exactitud `±0,1 mas`; Chandler ~`435 d`; amplitudes `0,5″`/`0,1″`; `|UT1 − UTC| < 0,9 s`; `ω` | Texto extraído del PDF el 2026-11-05 |

Límites: no se consultaron series reales de EOP (boletines del IERS) ni las expresiones de la precesión y la nutación, por lo que no se dan sus tasas ni amplitudes; el modelo de movimiento polar del laboratorio es **sintético**; la ortogonalidad de las matrices es un resultado algebraico.

## 12. Cómo ver los efectos

Equivalente accesible a un gráfico de barras en metros:

| Parámetro | Error o valor | Efecto en la superficie |
|---|---|---|
| `UT1 − UTC` | `0,9 s` | `418,6 m` (ecuador) |
| Movimiento polar | `0,5″` | `15,4 m` |
| Movimiento polar | `0,1″` | `3,08 m` |
| Polo celeste | `1 mas` | `3,09 cm` |
| Vínculo IERS | `0,1 mas` | `3,1 mm` |

Descripción larga: cinco barras en escala logarítmica; la más larga (UT1) supera a la menor (vínculo del IERS) en más de cuatro órdenes de magnitud.

## 13. Ejemplo trabajado: error por ignorar `UT1 − UTC` y el polo

**Paso 1 · Datos.** `UT1 − UTC = 0,4 s` (ejemplo sintético); `x_p = 0,28″` (máximo de la serie sintética).

**Paso 2 · Rotación.** `ω × 0,4 = 2,917 × 10⁻⁵ rad`; en una estación a `r_xy = 4 517 591 m` (45° N): `131,8 m`.

**Paso 3 · Movimiento polar.** `0,28 × 4,848 × 10⁻⁶ = 1,357 × 10⁻⁶ rad`; a `|r| = 6,36 × 10⁶ m`: `8,6 m` (el laboratorio da `8,64 m` para el vector de la estación).

**Paso 4 · Combinación.** En cuadratura (efectos casi ortogonales): `√(131,8² + 8,6²) = 132,1 m`.

**Paso 5 · Sentido.** El error de `UT1 − UTC` domina por un factor 15. Corregirlo exige el valor medido; el polo se corrige con series publicadas. Con dos cifras: `1,3 × 10² m`. Datos sintéticos.

## 14. Distintas formas de obtener los EOP

**Series publicadas por el IERS** (valores medidos): las más fiables, con retraso. **Predicciones:** disponibles en tiempo real, con error creciente. **Estimación con las propias observaciones** (VLBI, láser, GNSS): precisa, exige técnica espacial. **Ignorarlos:** solo válido si el requisito es de cientos de metros. Se elige según el requisito y la fecha de uso.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula cuántos metros mueve un movimiento polar de `0,3″` al polo terrestre (`6 356 752 m`). *Pasos:* `0,3″ × 4,848 × 10⁻⁶`.

<details><summary>Solución comentada</summary>

`1,454 × 10⁻⁶ rad × 6 356 752 = 9,25 m` (8.4).
</details>

**Ejercicio 2 · con una pista.** Calcula el efecto de `UT1 − UTC = 0,3 s` en el ecuador. *Pista:* `ω a`.

<details><summary>Solución comentada</summary>

`0,3 × 465,1 = 139,5 m` (8.3).
</details>

**Ejercicio 3 · casi autónomo.** Calcula el periodo de batido entre `435 d` y `365,25 d`.

<details><summary>Solución comentada</summary>

`1/(1/365,25 − 1/435) = 2278 d = 6,24 años` (8.5).
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** ¿Cuántos centímetros son `1 mas` en la superficie (`a = 6 378 137 m`)?

<details><summary>Solución comentada</summary>

`4,848 × 10⁻⁹ × 6 378 137 = 0,0309 m = 3,09 cm` (8.6).
</details>

**Ejercicio 5.** El vínculo del IERS es de `0,1 mas`. ¿Cuánto es en la superficie?

<details><summary>Solución comentada</summary>

`3,1 mm` (8.6).
</details>

**Ejercicio 6.** Comprueba que `R₃(θ) R₃(−θ) = I`. *Pista:* `cos²θ + sen²θ = 1`.

<details><summary>Solución comentada</summary>

`[[c, s],[−s, c]] · [[c, −s],[s, c]] = [[c² + s², 0],[0, s² + c²]] = I` (8.2).
</details>

**Ejercicio 7.** ¿Qué `UT1 − UTC` produce `1 m` de error en el ecuador?

<details><summary>Solución comentada</summary>

`1/465,1 = 2,15 ms` (8.3). Por eso UT1 se necesita al milisegundo.
</details>

**Ejercicio 8.** ¿Cuántos días separan dos máximos consecutivos de la suma sintética (batido)?

<details><summary>Solución comentada</summary>

`2278 d` (6,24 años) (8.5).
</details>

**Ejercicio 9 · transferencia.** Una antena apunta a un satélite geoestacionario (`a = 4,2164 × 10⁷ m`) usando UTC como UT1 (error `0,9 s`). ¿Qué error de apuntado y qué desviación a esa distancia produce?

<details><summary>Solución comentada</summary>

`ω × 0,9 = 6,56 × 10⁻⁵ rad = 13,5″`; a `4,2164 × 10⁷ m`: `2,77 km`. Para un haz ancho no importa; para seguimiento preciso, sí.
</details>

**Ejercicio 10 · transferencia.** Un compañero omite el movimiento polar porque «es de segundos de arco». ¿Qué le muestras?

<details><summary>Solución comentada</summary>

Un segundo de arco a la distancia terrestre son `31 m`: `0,5″` son `15,4 m`, mucho para geodesia y seguimiento (8.4).
</details>

**Ejercicio 11 · transferencia.** El laboratorio pone `Q = I`. ¿Por qué es solo válido para aislar efectos y no para una estación real?

<details><summary>Solución comentada</summary>

Porque el polo celeste se mueve (precesión y nutación) y esa matriz no es la identidad en ninguna fecha distinta de la época de referencia; omitirla desplaza todas las direcciones. En esta clase no se calcula porque no se consultó su modelo (sección 11).
</details>

**Ejercicio 12 · integrador.** Elabora tu *tabla de efectos de los EOP en metros*: `UT1 − UTC` (0,9 s y 1 ms), movimiento polar (0,1″ y 0,5″), polo celeste (1 mas) y vínculo IERS (0,1 mas), con su cálculo, la comprobación de ortogonalidad de las matrices, el periodo de batido y la nota de lo no consultado.

<details><summary>Solución modelo</summary>

Tabla de la sección 12 más `1 ms → 0,465 m`; ortogonalidad `< 10⁻¹⁴`; batido `2278 d`; no consultados: series reales de EOP y expresiones de precesión-nutación.
</details>

## 17. Laboratorio: matrices y efectos de los EOP

El script [orientacion_terrestre.py](orientacion_terrestre.py) construye `R₁`, `R₂`, `R₃`, el ERA y `W`, **comprueba ortogonalidad y determinante a `10⁻¹⁴`**, que el desplazamiento del polo es `a θ` a `10⁻⁶`, el efecto de `0,9 s` de UT1, el periodo de batido y una serie sintética de `x_p`.

**Datos:** definición del ERA y constantes del IERS; series sintéticas. **Predice antes de ejecutar:** ¿cuántos metros mueven `0,9 s` en el ecuador? (`≈ 419 m`.) **Ejecución del 2026-11-05 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
xp = 0.1 arcsec: el polo terrestre se desplaza 3.082 m (esperado 3.082 m)
xp = 0.5 arcsec: el polo terrestre se desplaza 15.409 m (esperado 15.409 m)
0.9 s de UT1-UTC en el ecuador: 418.6 m
1 mas = 3.09 cm en la superficie
periodo de batido Chandler/anual = 2278 d = 6.24 anios
amplitud maxima sintetica de xp = 0.280 arcsec (suma 0.28)
movimiento polar de 0.28 arcsec mueve la estacion 8.64 m
Pruebas superadas.
```

```bash
python programa/clases/B13/B13-C22-parametros-de-orientacion-terrestre-precesion-nutacion-ut1-y-movimiento-polar/orientacion_terrestre.py
```

**Límites:** `Q = I`; Tierra rígida; sin `s′`, mareas ni libración; series sintéticas; no es un transformador listo para operaciones.

## 18. Errores frecuentes y cómo corregirlos

**Omitir UT1 − UTC.** Se corrige con los ejercicios 2, 7 y 9.

**Despreciar el movimiento polar por «pequeño».** Se corrige con el ejercicio 10.

**Cambiar el orden de las matrices.** Se corrige en 8.1 y 7.

**Usar `Q = I` fuera de un ejercicio de aislamiento.** Se corrige con el ejercicio 11.

**Tomar series sintéticas por datos reales.** Se corrige en las secciones 10 y 11.

## 19. Cómo sabrás que vas bien

Tras 8.1: ¿nombras las tres matrices? Si no, repasa 8.1. Tras 8.3: ¿conviertes un error de UT1 en metros? Si no, ejercicios 2 y 7. Tras 8.5: ¿calculas el batido? Si no, ejercicio 3. Tras el laboratorio: ¿por qué una matriz de rotación es ortogonal? (porque conserva longitudes y ángulos).

## 20. Qué entregas y cómo se evalúa

El producto es tu **tabla de efectos de los EOP en metros** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Cadena | Sin matrices | Incompleta | `Q R W` explicada | Con ortogonalidad verificada |
| Efectos | Sin unidades | Parciales | Cinco efectos en metros | Compara órdenes de magnitud |
| Periodos | Los ignora | Menciona | Chandler, anual y batido | Con serie sintética |
| Límites | Sin ellos | Parciales | Dice lo no consultado | Propone productos oficiales |
| Fuentes | Sin fuente | Sin fecha | Con localizador y fecha | Rotula sintético |

**Condiciones críticas (no se compensan con promedio):** no presentar series sintéticas como reales; decir que `Q = I` es una simplificación; citar solo fuentes consultadas.

## 21. Ética, seguridad y límites

Una orientación terrestre equivocada desvía apuntados y trayectorias; para operaciones se usan los boletines vigentes del IERS y software validado. Esta clase no sustituye esos productos. Accesibilidad: tablas equivalentes al gráfico, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

La orientación de la Tierra se describe con tres matrices (`W`, `R`, `Q`) y con EOP medidos; UT1−UTC domina en metros, el movimiento polar sigue y el polo celeste mide centímetros por mas; el vínculo celeste–terrestre del IERS es de `0,1 mas`. Queda una pregunta: los instrumentos que miden estas cosas también cambian con los años, ¿cómo se sigue su deriva?

**Glosario español–inglés.** parámetros de orientación terrestre · *Earth orientation parameters (EOP)*; movimiento polar · *polar motion*; precesión · *precession*; nutación · *nutation*; polo celeste intermedio · *Celestial Intermediate Pole*; bamboleo de Chandler · *Chandler wobble*; periodo de batido · *beat period*.

**Continuidad.** B13-C23 reutiliza tu capacidad de **declarar la vigencia y la incertidumbre** de un parámetro para seguir la deriva de un instrumento.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B13-C21 — Sistema de referencia celeste ICRF y cuásares](../B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md) · [📚 Bloque B13](../../../tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md) · [Siguiente: B13-C23 — Estabilidad y deriva temporal de instrumentos →](../B13-C23-estabilidad-y-deriva-temporal-de-instrumentos/CLASE.md)
<!-- /nav -->
