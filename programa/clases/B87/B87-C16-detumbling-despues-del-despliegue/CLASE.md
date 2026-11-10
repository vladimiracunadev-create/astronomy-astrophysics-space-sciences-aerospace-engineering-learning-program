# B87-C16 — Detumbling después del despliegue

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B87](../../../tronco-comun/B87-sensores-y-control-de-actitud.md) · [← Anterior: B87-C15 — Apuntamiento de alta precisión](../B87-C15-apuntamiento-de-alta-precision/CLASE.md) · [Siguiente: B87-C17 — Control de tres ejes →](../B87-C17-control-de-tres-ejes/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 16 del bloque B87. Nivel N3. Tras separarse del lanzador, un satélite gira con velocidades de varios grados por segundo. El detumbling reduce esa velocidad hasta un valor manejable. La ley **B-dot** usa solo un magnetómetro y magnetopares: `m = −k Ḃ`. Aquí simulas con RK4 un microsatélite de ejemplo con `ω₀ = (5; −4; 3) °/s` durante 4 órbitas de `500 km`, con el campo dipolar sintético de C05 y un ruido de `50 nT` en la medida. Todo es sintético.

## 2. Por qué esta clase existe

Sin estimador de actitud ni giroscopio calibrado, el satélite recién desplegado necesita detenerse con lo mínimo. La decisión central: **¿cuánto tarda, qué ganancia usar y qué velocidad residual queda?** Una previa: la ley no baja a cero sino a una rotación ligada a la órbita.

## 3. Lo que podrás hacer al terminar

1. Escribir la ley `m = −k dB/dt` y el par `τ = m × B`.
2. Aproximar `Ḃ` por diferencia finita de la medida en el cuerpo.
3. Simular el detumbling y medir el tiempo para `|ω| < 0,5 °/s`.
4. Verificar la disipación de energía cinética.
5. Explicar el papel del límite de dipolo y de la ganancia.
6. Separar lo sintético de lo consultado y de lo no consultado.

La evidencia es la **curva de la velocidad angular frente al tiempo en un detumbling B-dot** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Cómo cambia `B` visto desde un cuerpo que gira?
2. ¿Qué es la energía cinética de rotación?
3. ¿Qué es una diferencia finita?
4. ¿Qué par genera un dipolo?
5. ¿Qué es un detumbling?

<details>
<summary>Ver respuestas</summary>

1. `Ḃ_b = −ω × B_b` (más el cambio del campo inercial). 2. `T = ½ ωᵀ I ω`. 3. `(B_k − B_{k−1})/Δt` como aproximación de la derivada. 4. `τ = m × B`. 5. El frenado de la rotación inicial.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Con `k = 2×10⁵` y `m_max = 0,2 A·m²`, la velocidad baja de `7,07 °/s` a `2,60` (1 órbita), `0,48` (2) y `0,13 °/s` (4 órbitas); cruza `0,5 °/s` a los `187 min` (1,98 órbitas). La energía cae de `2,72 mJ` a `0,99 µJ`. Todo es **sintético**.

## 6. Vocabulario

La **ley B-dot** es `m = −k Ḃ`. La **derivada del campo** `Ḃ` se obtiene de la medida en el cuerpo. El **dipolo** se limita a `m_max`. La **disipación** es `Ṫ = ω·τ_m < 0` en promedio. La **velocidad residual** es la que queda cuando el campo y la rotación se acoplan con la órbita. El **tiempo de captura** es el que tarda en bajar de `0,5 °/s`.

## 7. Modelo mental: frenar usando el campo como freno

```mermaid
flowchart LR
    M["B medido en el cuerpo"] --> D["B-dot por diferencia finita"]
    D --> L["m = -k Bdot (limitado)"]
    L --> T["par m x B"]
    T --> W["w disminuye"]
    W --> M
```

*Descripción textual:* la derivada del campo medido es proporcional a `ω × B`; el dipolo opuesto produce un par que se opone a la rotación y disipa energía.

Analogía: una rueda dentro de un campo magnético con corrientes de Foucault: gira más lenta porque el campo se opone al giro. Límite: el efecto es débil y proporcional al campo, y cuando el campo apenas cambia de dirección (ejes alineados) el freno se vuelve ineficaz.

## 8. La explicación, paso a paso

### 8.1 La ley

Con `Ḃ_b ≈ −ω × B_b`, la ley da `m = k ω × B` y `τ = m × B = k (ω × B) × B = −k |B|² ω_⊥`, con `ω_⊥` la parte de `ω` perpendicular a `B`: el par se opone al giro perpendicular. La energía decrece: `Ṫ = ω·τ = −k |ω × B|² ≤ 0`. Los componentes de `ω` paralelos a `B` no se frenan.

### 8.2 Medida y límite

En el laboratorio `Ḃ` se calcula de la diferencia de dos medidas sucesivas (`Δt = 0,5 s`) con ruido de `50 nT`, lo que añade `≈ 1,4×10⁻⁷ T/s` de ruido en `Ḃ`, pequeño frente a `ω B ≈ 10⁻⁶ T/s` al inicio. El dipolo se limita a `0,2 A·m²` y se satura el `25,6 %` del tiempo.

### 8.3 Resultados (4 órbitas de 94,62 min)

| Instante | `|ω|` (°/s) |
|---|---|
| inicio | 7,072 |
| 1 órbita | 2,597 |
| 2 órbitas | 0,481 |
| 3 órbitas | 0,165 |
| 4 órbitas | 0,128 |

Energía: `2,7187 mJ → 0,992 µJ`; el mayor aumento instantáneo de energía fue `1,5e-08 J/s`, atribuible al ruido de la medida.

### 8.4 Velocidad residual y límites

La ley no lleva a cero, sino cerca de la velocidad orbital (`0,063 °/s`) respecto del campo inercial: con `Ḃ_inercial ≠ 0` la ley también ve la rotación del campo. Un buen detumbling deja `|ω|` del orden de `0,1–0,2 °/s`, suficiente para que el control de actitud (C17) tome el mando. No se modelan el campo de los propios magnetopares sobre el magnetómetro (se alterna medida y actuación), el retardo ni la dinámica con ruedas.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `k` | ganancia B-dot | A·m²·s/T | 2×10⁵ |
| `Ḃ` | derivada del campo en el cuerpo | T/s | ~10⁻⁶ |
| `m` | dipolo | A·m² | máx. 0,2 |
| `ω₀` | velocidad angular inicial | °/s | (5; −4; 3) |
| `T` | energía cinética | J | 2,72 mJ inicial |

## 10. Convenciones y referencias

Satélite `I = diag(0,35; 0,40; 0,30) kg·m²`; campo dipolar **sintético** (C05) fijo en el sistema inercial de ejemplo; magnetómetro con ruido de `50 nT` (semilla 20260522); RK4 con `Δt = 0,5 s`; 4 órbitas. Tolerancias: `|ω_final| < 0,5 °/s` y energía final `< 1 %` de la inicial. Cuaternión `q = [qx, qy, qz, qw]` con la parte escalar al final, `v_B = A(q) v_I`, producto tal que `A(q⊗p) = A(q) A(p)`, cinemática `q̇ = ½ [ω; 0] ⊗ q` con `ω` del cuerpo respecto del sistema inercial expresada en el cuerpo (la biblioteca [adcs_comun.py](../adcs_comun.py) del bloque lo comprueba). Sistema inercial `I` de **ejemplo** (ejes sin relación con J2000), órbita circular de dos cuerpos con radio terrestre `6 378 137 m` y `μ = 3,986004418 × 10¹⁴ m³/s²` como valores adoptados de ejemplo. Satélite **sintético** `I = diag(0,35; 0,40; 0,30) kg·m²` salvo que la clase diga otra cosa. Todo dato es sintético con semilla fija.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NOAA/NCEI, International Geomagnetic Reference Field (IGRF) — https://www.ncei.noaa.gov/products/international-geomagnetic-reference-field (consultada 2026-11-10) | página del producto | el IGRF es un modelo estándar del campo magnético principal terrestre, mantenido por IAGA, expresado como serie truncada de un potencial escalar (grado N = 13) con su variación secular; la generación vigente es IGRF-14 (coeficientes cerrados en noviembre de 2024) | Consultada |
| — | Relaciones estándar de dinámica de actitud, estimación y control usadas en esta clase (ecuaciones de Euler, cinemática de cuaterniones, problema de Wahba, filtro de Kalman multiplicativo, estabilidad de Lyapunov, modelos de sensores y actuadores) | — | las verifica el laboratorio con una segunda vía (conservación, comparación entre métodos, propagación independiente o Monte Carlo) | No consultada en una fuente concreta |
| — | Libros de texto de actitud y control (p. ej. Wertz, Markley–Crassidis, Sidi) y hojas de datos de fabricantes | — | — | No consultada |
| — | Estudios publicados de la ley B-dot (por ejemplo, de Stickler y Alfriend) y datos de misiones reales | — | — | No consultada |

Límites: El IGRF (S1) se consultó solo en su descripción y no se usa; el campo es un dipolo sintético. La ley B-dot y su prueba de disipación no se consultaron en una fuente concreta y las valida la simulación de energía.

## 12. Cómo ver el detumbling

| Magnitud | Valor |
|---|---|
| `|ω|` inicial / final | 7,07 / 0,13 °/s |
| tiempo a `|ω| < 0,5 °/s` | 187 min (1,98 órbitas) |
| energía final / inicial | 3,6e-04 |
| dipolo saturado | 25,6 % |

Descripción larga: la velocidad cae casi a la tercera parte por órbita al principio y se estabiliza cerca de la velocidad orbital.

## 13. Ejemplo trabajado: de 7 °/s a menos de 0,5 °/s

**Paso 1 · Datos.** `ω₀ = (5; −4; 3) °/s`, `|ω₀| = 7,07 °/s`.

**Paso 2 · Ley.** `m = −2×10⁵ Ḃ`, con límite de `0,2 A·m²`.

**Paso 3 · Órbita 1.** `|ω| = 2,60 °/s`.

**Paso 4 · Captura.** `|ω| < 0,5 °/s` a `187 min`.

**Paso 5 · Energía.** `3,6e-04` de la inicial.

## 14. Distintas formas de describir el detumbling

**B-dot** (esta clase): solo magnetómetro y magnetopares. **Con giroscopio:** `m = −k (ω × B)`, más preciso. **Con propulsores:** más rápido, gasta propergol (C13). **Con ruedas:** solo reparte momento, no lo elimina.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula la energía cinética de `ω = (5; −4; 3) °/s` con `I = diag(0,35; 0,40; 0,30)`. *Pasos:* `½ Σ I_i ω_i²` en rad/s.

<details><summary>Solución comentada</summary>

`2,719 mJ`.
</details>

**Ejercicio 2 · con una pista.** ¿Qué par máximo da `m_max = 0,2` con `B = 30 µT`?

<details><summary>Solución comentada</summary>

`6 µN·m`.
</details>

**Ejercicio 3 · casi autónomo.** ¿Cuánto tarda en frenar `0,0866 rad/s` de momento `ΔH = 0,026 N·m·s` con `6 µN·m`?

<details><summary>Solución comentada</summary>

`ΔH/τ = 0,026/6×10⁻⁶ ≈ 72 min` (cota inferior; el par efectivo promedio es menor).
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** ¿Por qué `Ṫ = −k |ω × B|²`?

<details><summary>Solución comentada</summary>

Porque `m = k ω × B` y `τ·ω = ((m × B)·ω) = m·(B × ω) = k (ω × B)·(B × ω) = −k |ω × B|²`, siempre `≤ 0`.
</details>

**Ejercicio 5 · autónomo.** ¿Qué componente de `ω` no frena la ley?

<details><summary>Solución comentada</summary>

La paralela a `B`: `ω × B = 0` para ella.
</details>

**Ejercicio 6 · autónomo.** Si `k` se duplica, ¿se duplica la velocidad de frenado?

<details><summary>Solución comentada</summary>

Solo mientras el dipolo no sature: con saturación el par máximo `m_max B` fija el ritmo (`26 %` del tiempo saturado aquí).
</details>

**Ejercicio 7 · autónomo.** ¿Por qué el ruido de `Ḃ` crece al reducir `Δt`?

<details><summary>Solución comentada</summary>

Porque la diferencia finita divide el ruido por `Δt`: `σ √2/Δt`.
</details>

**Ejercicio 8 · autónomo.** ¿Qué velocidad residual se espera y por qué?

<details><summary>Solución comentada</summary>

Del orden de la velocidad orbital (`0,063 °/s`): el campo gira respecto del inercial con la órbita.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** **Transferencia.** Un colega afirma que un satélite real se detendrá en `187 min`. ¿Es válido?

<details><summary>Solución comentada</summary>

No: el campo, la inercia y la ganancia son sintéticos; el tiempo real depende de la órbita y de los parámetros.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** **Transferencia.** ¿Por qué el B-dot casi no sirve en órbita geoestacionaria?

<details><summary>Solución comentada</summary>

Porque el campo es muy débil (`1/r³`) y casi constante en el cuerpo: `Ḃ` es mínimo y el par despreciable.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** **Transferencia.** ¿Qué pasa si el magnetopar se enciende mientras el magnetómetro mide?

<details><summary>Solución comentada</summary>

El campo de la bobina se suma a `B` y falsea `Ḃ`; se alterna medida y actuación.
</details>

**Ejercicio 12 · integrador.** **Integrador.** **Integrador.** Elabora tu *curva de la velocidad angular en el detumbling*: tabla de 8.3, tiempo de captura, energía y lista de consultado y sintético.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4, 12 y la salida del laboratorio.
</details>

## 17. Laboratorio: detumbling con la ley B-dot

El script [bdot.py](bdot.py) integra con RK4 el cuerpo rígido con la ley `m = −k Ḃ` (ganancia `2×10⁵`, `m_max = 0,2 A·m²`) durante 4 órbitas, mide `|ω|` en cada órbita, el tiempo para `0,5 °/s` y la energía (**comprueba** captura, `|ω_final| < 0,5 °/s` y energía final `< 1 %` de la inicial). Usa la biblioteca común [adcs_comun.py](../adcs_comun.py) del bloque.

**Datos:** satélite, campo y ruido **sintéticos** de semilla 20260522. **Predice antes de ejecutar:** ¿Cuántas órbitas tardará en bajar de `0,5 °/s`? (unas 2.) **Ejecución del 2026-11-10 (Python 3.12.9, numpy 2.4.4):**

```text
Python 3.12.9 | numpy 2.4.4
B87-C16 detumbling B-dot | SINTETICO: w0 = (5,-4,3) deg/s, k = 2e5, m_max = 0.2 A m^2, ruido de B 50 nT (semilla 20260522), 4 orbitas
periodo orbital = 94.62 min ; velocidad orbital = 0.0634 deg/s
|w| inicial = 7.071 deg/s ; final = 0.1280 deg/s
|w| al inicio de cada orbita [deg/s]: 7.072 2.597 0.481 0.165 0.128
tiempo para |w| < 0.5 deg/s = 187.1 min (1.98 orbitas)
energia cinetica: inicial = 2.7187 mJ ; final = 0.992 uJ ; dipolo saturado el 25.6 % del tiempo
mayor aumento instantaneo de energia = 1.51e-08 J/s (el ruido de la medida puede causar aumentos puntuales)
Pruebas superadas.
```

```bash
python programa/clases/B87/B87-C16-detumbling-despues-del-despliegue/bdot.py
```

**Límites:** campo fijo en I sin rotación terrestre, sin retardo, sin dinámica de actuadores, un solo conjunto de condiciones iniciales y semilla.

## 18. Errores frecuentes y cómo corregirlos

**Usar el campo inercial en lugar del medido en el cuerpo.** Usa `Ḃ_b` medido (8.2)

**Subir `k` sin ver la saturación.** Revisa la fracción saturada (8.2)

**Esperar velocidad cero.** Revisa la velocidad residual (8.4)

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué velocidad esperabas al final? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **curva de la velocidad angular frente al tiempo en un detumbling B-dot** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Explica el método y su dominio | Explica los límites y las alternativas |
| Cálculo | Sin unidades | Con errores | Resultados con unidades y comprobados | Resuelve casos nuevos |
| Numérico | Sin comprobar | Un caso | Verifica con una segunda vía en varios casos | Interpreta las diferencias y los fallos |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo sintético y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular los datos como sintéticos; verificar cada resultado con una segunda vía; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y los datos son sintéticos; ningún resultado describe una misión real ni sustituye el diseño y la verificación de un subsistema de actitud con herramientas validadas, ensayos y revisión de especialistas.  Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

La ley B-dot lleva a `|ω₀| = 7,1 °/s` a `0,13 °/s` en 4 órbitas con solo un magnetómetro y magnetopares. Queda una pregunta: ¿cómo se controla la actitud en tres ejes una vez detenido el giro?

**Glosario español–inglés.** detumbling · *detumbling*; B-dot · *B-dot*; velocidad residual · *residual rate*; dipolo · *dipole*; disipación · *dissipation*; diferencia finita · *finite difference*.

**Continuidad.** [B87-C17](../B87-C17-control-de-tres-ejes/CLASE.md) presenta el control de tres ejes en cuaterniones.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B87-C15 — Apuntamiento de alta precisión](../B87-C15-apuntamiento-de-alta-precision/CLASE.md) · [📚 Bloque B87](../../../tronco-comun/B87-sensores-y-control-de-actitud.md) · [Siguiente: B87-C17 — Control de tres ejes →](../B87-C17-control-de-tres-ejes/CLASE.md)
<!-- /nav -->
