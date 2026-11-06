# B16-C04 — Respuesta transitoria y estacionaria

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B16](../../../tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) · [← Anterior: B16-C03 — Sistemas lineales invariantes](../B16-C03-sistemas-lineales-invariantes/CLASE.md) · [Siguiente: B16-C05 — Funciones de transferencia →](../B16-C05-funciones-de-transferencia/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Cuarta clase del bloque B16. Ya sabes modelar un sistema (C01–C02) y conoces sus propiedades LTI (C03). Ahora aprendes a **medir la calidad de su respuesta** a un cambio de orden: cuánto tarda, cuánto se pasa y dónde se queda. Usas exponenciales y funciones trigonométricas (B09) y el sistema de segundo orden.

No verás aún cómo diseñar el lazo que produce esa respuesta (C07 a C12).

## 2. Por qué esta clase existe

Tras girar un telescopio hacia una estrella nueva, los instrumentos no pueden empezar a exponer hasta que el apuntamiento se haya asentado. Cada segundo de espera cuesta tiempo de observación. A la vez, pasarse del blanco puede arrastrar el sensor de guiado fuera de su campo. La pregunta motivadora es: **¿cómo describo con pocos números lo rápido, lo suave y lo preciso que es el movimiento?**

La decisión central: qué especificaciones pedirle a un lazo (tiempo, sobreimpulso, error final) y cómo comprobar que un diseño las cumple.

## 3. Lo que podrás hacer al terminar

1. Distinguir la parte transitoria de la estacionaria de una respuesta.
2. Calcular la constante de tiempo de un sistema de primer orden y los tiempos de 63 % y 95 %.
3. Obtener `ωn` y `ζ` de un sistema de segundo orden y predecir sobreimpulso, tiempo de pico y de asentamiento.
4. Medir esas métricas sobre una respuesta simulada y comparar con las fórmulas.
5. Calcular el error estacionario ante un escalón y una perturbación constante.
6. Convertir un requisito de apuntamiento en especificaciones de lazo.

La evidencia es la **hoja de especificaciones** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Cuánto vale `e^(−3)` aproximadamente?
2. Si `y(t) = 1 − e^(−t/2)`, ¿en qué `t` llega a 0,95?
3. Define máximo de una función en un intervalo.
4. ¿Qué es la frecuencia natural de una masa-resorte con `k = 8`, `m = 2`?
5. ¿Qué significa «error» en un lazo que debe seguir una referencia?

<details>
<summary>Ver respuestas</summary>

1. 0,0498. 2. `e^(−t/2) = 0,05` → `t = 2 ln 20 ≈ 6,0`. 3. El mayor valor que toma en ese intervalo. 4. `√(k/m) = 2 rad/s`. 5. La diferencia entre la referencia deseada y la salida medida.
</details>

Con cuatro o cinco aciertos, sigue.

## 5. Un caso real: asentarse antes de observar

La ficha de la NASA sobre los sensores de guiado fino del Hubble (S1) describe que, una vez apuntado, el telescopio debe quedarse a no más de 0,007″ del objetivo durante al menos 24 horas. Antes de llegar a ese régimen hay una fase de maniobra y asentamiento. Para nuestro estudio, esas dos fases son exactamente la **respuesta transitoria** (cómo llega) y la **respuesta estacionaria** (dónde se queda). La distinción importa porque se les piden cosas distintas: al transitorio, rapidez y suavidad; al estacionario, exactitud.

## 6. Vocabulario

La **respuesta transitoria** es la parte que se extingue con el tiempo; la **estacionaria** es la que queda cuando el transitorio desapareció. La **constante de tiempo** `τ_c` de un sistema de primer orden es el tiempo en el que la respuesta a un escalón alcanza el 63,2 % de su valor final. En un sistema de segundo orden, la **frecuencia natural** `ωn` (rad/s) y el **amortiguamiento** `ζ` (adimensional) fijan la forma: `θ̈ + 2ζωn θ̇ + ωn² θ = ωn² r`. El **sobreimpulso** `Mp` es cuánto excede la respuesta a su valor final (en fracción), el **tiempo de pico** `tp` es cuándo ocurre, el **tiempo de subida** `tr` es el que tarda entre 10 % y 90 % del valor final y el **tiempo de asentamiento** `ts` es el que tarda en quedar dentro de ±2 % para siempre. El **error estacionario** `e_ss` es `lim (r − y)` cuando `t → ∞`.

## 7. Modelo mental: la curva y sus cinco números

Imagina la respuesta como una curva en el tiempo que parte de cero y se acerca al valor final. Cinco números la resumen: `tr`, `tp`, `Mp`, `ts` y `e_ss`.

```mermaid
flowchart LR
    A["Escalón en la referencia"] --> B["Transitorio<br/>tr, tp, Mp, ts"]
    B --> C["Estacionario<br/>e_ss"]
```

*Descripción textual:* un escalón de referencia produce primero un tramo transitorio, que se describe con cuatro tiempos y sobreimpulso, y luego un régimen estacionario, que se describe con el error final.

La analogía de una puerta con cierrapuertas: si el resorte es muy débil se cierra lentamente (sobreamortiguada), si es muy fuerte golpea y rebota (subamortiguada). El límite: una puerta no tiene velocidad inicial ni perturbaciones externas como el viento solar.

## 8. La explicación, paso a paso

### 8.1 Primer orden

Para `τ_c ẏ + y = K r`, con un escalón `r = 1` la salida es `y(t) = K(1 − e^(−t/τ_c))`. A `t = τ_c` vale 63,2 % de `K`; a `3τ_c`, 95 %; a `4τ_c`, 98,2 %. Por eso `ts(2 %) ≈ 4 τ_c`. No hay sobreimpulso: la curva se acerca sin pasarse. La rueda de B16-C01 es de este tipo.

### 8.2 Segundo orden subamortiguado

Para `0 < ζ < 1`, la respuesta a un escalón unitario es

```text
y(t) = 1 − e^(−ζ ωn t) / √(1 − ζ²) · sen(ωd t + φ),   ωd = ωn √(1 − ζ²),   φ = arccos ζ
```

`ωd` es la frecuencia de oscilación amortiguada (rad/s). La envolvente `e^(−ζωn t)` decide cuánto tarda en apagarse: más `ζωn`, más rápido.

### 8.3 Las cuatro fórmulas

Derivando `y(t)` y buscando el primer máximo se obtiene el tiempo de pico `tp = π/ωd` y el sobreimpulso `Mp = exp(−π ζ/√(1 − ζ²))`; solo dependen de `ζ`. El asentamiento al 2 % se aproxima por `ts ≈ 4/(ζ ωn)`, una **aproximación** (la envolvente a ese tiempo vale 2 %, pero la sinusoide fluctúa). Con `ζ = 0,5`: `Mp = 16,3 %`; con `ζ = 0,7`: `4,6 %`; con `ζ = 0,9`: `0,15 %`.

### 8.4 Lo que mueve cada número

Subir `ωn` acelera todo sin cambiar `Mp`. Subir `ζ` reduce `Mp` pero alarga la subida. Un `ζ` entre 0,5 y 0,8 es un compromiso habitual. Estas reglas valen en un sistema que **se parece** a un segundo orden; en uno de orden mayor, los polos dominantes (C09) lo aproximan.

### 8.5 Error estacionario

Un lazo con un integrador (tipo 1) sigue sin error un escalón; uno sin integrador deja un error. Ante una perturbación de par constante `d` en un lazo PD sobre `1/(J s²)` con ganancia proporcional `Kp` (N·m/rad), el estado final cumple `Kp θ = d` y por tanto `e_ss = d/Kp`. Con `d = 0,5 N·m` y `Kp = 20 N·m/rad`, `e_ss = 25 mrad`. Para bajar el error hay que subir `Kp` (tiene un coste) o añadir una acción integral (C11).

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Nota |
|---|---|---|---|
| `τ_c` | constante de tiempo | s | primer orden |
| `ωn` | frecuencia natural | rad/s | |
| `ζ` | amortiguamiento | — | adimensional |
| `ωd` | frecuencia amortiguada | rad/s | `ωn√(1−ζ²)` |
| `Mp` | sobreimpulso | fracción (o %) | |
| `tp, tr, ts` | tiempos de pico, subida y asentamiento | s | |
| `e_ss` | error estacionario | rad | |
| `Kp, Kd` | ganancias proporcional y derivativa | N·m/rad; N·m·s/rad | C11 |

## 10. Convenciones y referencias

`ts` se define con una banda (±2 % aquí; ±5 % es común). `tr` usa 10–90 %; otros textos usan 0–100 %. Declara siempre la convención. El escalón se normaliza a 1; para una maniobra de 0,5 rad todo se escala por 0,5 (superposición, C03).

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA Facts FS-2018-10-285-GSFC, *Hubble Space Telescope: Fine Guidance Sensors* | https://smd-cms.nasa.gov/wp-content/uploads/2023/04/hst_fine_guidance_fact_sheet1_0.pdf | Apuntamiento a no más de 0,007″ durante al menos 24 h | Extraído del PDF el 2026-11-05 |

Límites: las fórmulas de `Mp`, `tp` y `ts` son resultados clásicos del sistema de segundo orden y se verifican numéricamente contra una respuesta simulada. No se verificó ningún requisito de misión. Los parámetros son **sintéticos**.

## 12. Cómo ver la respuesta

Resultados de la simulación (`ωn = 0,5 rad/s`, datos **simulados**):

| `ζ` | `Mp` | `tp` (s) | `ts` (2 %) (s) | `tr` (s) |
|---|---|---|---|---|
| 0,2 | 52,7 % | 6,41 | 39,2 | 2,41 |
| 0,5 | 16,3 % | 7,26 | 16,2 | 3,28 |
| 0,7 | 4,6 % | 8,80 | 12,0 | 4,25 |
| 0,9 | 0,15 % | 14,41 | 9,4 | 5,77 |

Para graficar, dibuja las cuatro curvas con estilos de trazo distintos (continuo, rayas, puntos, mixto), añade una banda gris de ±2 % y rotula cada curva con su `ζ`.

## 13. Ejemplo trabajado: elegir ζ para una maniobra

Se quiere girar el telescopio sintético un escalón de 0,5 rad con `ωn = 0,5 rad/s` sin pasarse más de 0,01 rad y asentarse en menos de 20 s.

**Paso 1 · sobreimpulso permitido.** `Mp ≤ 0,01/0,5 = 2 %`. Despejando, `ζ ≥ 0,78`; con `ζ = 0,8`, `Mp = exp(−π·0,8/0,6) = 1,5 %`.
**Paso 2 · asentamiento.** `ts ≈ 4/(0,8·0,5) = 10 s`, menor que 20 s: cumple.
**Paso 3 · par necesario.** Falta comprobar que las ruedas pueden dar el par que exige esa maniobra; eso se verifica con la saturación en C18, no con estas fórmulas.
**Paso 4 · comprobación.** `ζ = 0,9` da `Mp = 0,15 %` y `ts ≈ 9,4 s` (tabla). Ambos valores cumplen; `ζ = 0,5` no (`Mp = 16 %`).

## 14. Comparar maneras de especificar

Especificar en el **dominio del tiempo** (`Mp`, `ts`, `e_ss`) es intuitivo y se verifica con una simulación. Especificar en **frecuencia** (ancho de banda, margen de fase, C10) generaliza a sistemas de orden alto y ofrece robustez. Especificar con una **norma integral** (error cuadrático acumulado, C15) da una cifra única, pero esconde la forma. Las métricas de este capítulo valen para sistemas dominados por un par de polos complejos; en otros casos, mide sobre la simulación en vez de aplicar la fórmula.

## 15. Práctica guiada

**Ejercicio 1 · con pasos.** Un calentador tiene `τ_c = 12 s`. ¿En qué tiempo alcanza el 95 % y el 98 % de su valor final? *Pasos:* 8.1.

<details><summary>Solución comentada</summary>

`3τ_c = 36 s` (95 %) y `4τ_c = 48 s` (98 %).
</details>

**Ejercicio 2 · con pista.** Calcula `Mp` y `tp` de `ζ = 0,6`, `ωn = 1 rad/s`. *Pista:* 8.3.

<details><summary>Solución comentada</summary>

`√(1−0,36)=0,8`; `Mp = exp(−π·0,6/0,8) = e^(−2,356) = 9,5 %`; `tp = π/0,8 = 3,93 s`.
</details>

**Ejercicio 3 · casi autónomo.** Un lazo PD con `J = 50`, `Kp = 20`, `Kd = 40` tiene `ωn = √(Kp/J)` y `ζ = Kd/(2√(Kp J))`. Calcúlalos.

<details><summary>Solución comentada</summary>

`ωn = √0,4 = 0,6325 rad/s`, `ζ = 40/(2·31,62) = 0,6325`. Coinciden por casualidad con los valores del laboratorio.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** ¿Qué `ζ` da exactamente `Mp = 10 %`? *(Pista: `ln(0,1) = −2,3026`; `ζ = −ln Mp/√(π² + ln² Mp)`.)*

<details><summary>Solución comentada</summary>

`ζ = 2,3026/√(9,8696 + 5,3019) = 2,3026/3,895 = 0,591`.
</details>

**Ejercicio 5.** Con `ωn = 0,8 rad/s` y `ζ = 0,5`, calcula `tp` y estima `ts`.

<details><summary>Solución comentada</summary>

`tp = π/(0,8·0,866) = 4,53 s`; `ts ≈ 4/(0,5·0,8) = 10 s`.
</details>

**Ejercicio 6.** Una perturbación de 0,3 N·m actúa sobre un lazo con `Kp = 15 N·m/rad`. ¿Cuál es `e_ss` y cómo se reduce a la mitad?

<details><summary>Solución comentada</summary>

`e_ss = 0,3/15 = 0,02 rad`. Duplicar `Kp` a 30 N·m/rad (con efectos sobre `ωn` y `ζ`), o añadir acción integral.
</details>

**Ejercicio 7.** Si duplicas `ωn` manteniendo `ζ`, ¿cómo cambian `Mp`, `tp` y `ts`?

<details><summary>Solución comentada</summary>

`Mp` no cambia; `tp` y `ts` se reducen a la mitad (dependen de `1/ωn`).
</details>

**Ejercicio 8.** ¿Por qué `ts = 4/(ζωn)` es una aproximación? Usa la tabla de la sección 12 para el caso `ζ = 0,9`.

<details><summary>Solución comentada</summary>

Porque supone que la envolvente exponencial llega a 2 % y desprecia la oscilación y el factor `1/√(1−ζ²)`. Para `ζ = 0,9` la fórmula da 8,9 s y la medida da 9,4 s (6 % de diferencia).
</details>

**Ejercicio 9 · transferencia.** Un instrumento exige un asentamiento a ±0,01 rad tras una maniobra de 0,2 rad en menos de 15 s con `Mp ≤ 5 %`. Traduce a `ζ` mínimo y a `ωn` mínimo.

<details><summary>Solución comentada</summary>

`Mp = 5 %` pide `ζ ≥ 0,69`. Con `ζ = 0,7`, `ts ≈ 4/(0,7 ωn) ≤ 15` da `ωn ≥ 0,38 rad/s`. (La banda de ±0,01 rad sobre 0,2 rad es 5 %, algo más estricta que 2 %: verifica en simulación.)
</details>

**Ejercicio 10 · transferencia.** Un lazo con un integrador sigue un escalón con error nulo. ¿Sigue sin error una rampa? Justifica con la idea de 8.5.

<details><summary>Solución comentada</summary>

No en general: un tipo 1 deja un error constante ante una rampa; para error nulo ante rampa hace falta tipo 2 (dos integradores). Eso se verá con la función de transferencia en C05 y C11.
</details>

**Ejercicio 11 · transferencia.** Discute por qué subir `ωn` indefinidamente no es una solución, pensando en ruido del sensor y en el par máximo de las ruedas.

<details><summary>Solución comentada</summary>

Mayor `ωn` exige mayor par y amplifica el ruido de medida; además choca con dinámicas no modeladas (modos flexibles, retardos). Es un compromiso (C10, C16, C18).
</details>

**Ejercicio 12 · integrador.** Entrega una **hoja de especificaciones**: para una maniobra de tu elección, define los requisitos (`Mp`, `ts`, `e_ss`), traduce a `ζ`, `ωn` y `Kp`, `Kd`, y comprueba con una simulación y las fórmulas.

<details><summary>Solución modelo</summary>

Un entregable correcto declara la banda de asentamiento, calcula `ζ` y `ωn` con las fórmulas de 8.3, deduce `Kp = J ωn²` y `Kd = 2ζ ωn J`, y muestra que la medida simulada coincide con la fórmula dentro de la tolerancia declarada.
</details>

## 17. Laboratorio: métricas contra fórmulas

El script [metricas_transitorias.py](metricas_transitorias.py) calcula la respuesta exacta a un escalón para cuatro valores de `ζ`, mide `Mp`, `tp`, `ts` y `tr` sobre una rejilla fina y las compara con las fórmulas; también calcula el error estacionario del lazo PD.

**Datos:** sintéticos (simulados). **Predice:** `Mp = 16,3 %` para `ζ = 0,5`. **Ejecución del 2026-11-05 (Python 3.12.9, numpy 2.4.4):**

```text
 zeta |  Mp medido  Mp fórmula | tp medido tp fórmula | ts medido  4/(z wn) | tr (10-90 %)
  0.2 |   0.526621    0.526621 |   6.4127    6.4127 |   39.204    40.000 |   2.407
  0.5 |   0.163034    0.163034 |   7.2552    7.2552 |   16.153    16.000 |   3.275
  0.7 |   0.045988    0.045988 |   8.7982    8.7982 |   11.958    11.429 |   4.252
  0.9 |   0.001524    0.001524 |  14.4146   14.4146 |    9.399     8.889 |   5.766
lazo PD: wn = 0.6325 rad/s, zeta = 0.6325; error estacionario con d = 0.5 N m: d/Kp = 25.0 mrad
Pruebas superadas.
```

```bash
python programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/metricas_transitorias.py
```

**Límites:** sistema exacto de segundo orden sin ceros; `ts` es una medida contra una aproximación; el script detiene la ejecución si `Mp` o `tp` difieren más de 10⁻⁴ de la fórmula.

## 18. Errores frecuentes y cómo corregirlos

**Pensar que `ζ = 1` es lo mejor siempre.** Es lento; se corrige con el ejercicio 4 y la tabla 12.

**Olvidar que `ts` es aproximada.** Se corrige con el ejercicio 8.

**Confundir `ωn` con la frecuencia de oscilación `ωd`.** Se corrige con el ejercicio 2.

**Esperar error nulo sin integrador.** Se corrige con el ejercicio 6.

**Aplicar fórmulas de segundo orden a un sistema de tercer orden sin comprobar.** Se corrige con el ejercicio 11.

## 19. Cómo sabrás que vas bien

Tras 8.3: ¿calculas `Mp` para un `ζ` dado? Ejercicio 2. Tras 8.5: ¿calculas `e_ss`? Ejercicio 6. Tras el ejemplo: ¿eliges `ζ` para una especificación? Ejercicio 9. Al final: ¿tu hoja contrasta fórmula y simulación?

## 20. Qué entregas y cómo se evalúa

El producto es la **hoja de especificaciones** del ejercicio 12.

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Requisitos | Sin números | Números sin banda | Con banda y convención | Justifica el origen del requisito |
| Traducción | No traduce | Traduce con error | `ζ`, `ωn`, ganancias correctas | Analiza la sensibilidad |
| Verificación | Sin simulación | Sólo fórmulas | Simulación y fórmula | Cuantifica la diferencia |
| Fuentes y datos | Sin rótulo | Parcial | Rotula sintético | Cita solo lo consultado |

**Condiciones críticas:** declarar la banda de asentamiento; no extrapolar fórmulas fuera del segundo orden sin comprobar.

## 21. Ética, seguridad y límites

Una especificación mal traducida puede dejar un instrumento fuera de campo. Las cifras son didácticas. Accesibilidad: las curvas se acompañan de tabla; el laboratorio no requiere conexión.

## 22. Para cerrar y seguir

La respuesta de un lazo se resume en `tr`, `tp`, `Mp`, `ts` y `e_ss`. En segundo orden, `Mp` y `tp` dependen de `ζ` y `ωn` por fórmulas exactas, y `ts` por una aproximación. El error estacionario depende del tipo de lazo. Queda abierto: ¿cómo analizar un sistema sin resolver su ecuación diferencial cada vez?

**Glosario español–inglés.** respuesta transitoria · *transient response*; estacionaria · *steady state*; sobreimpulso · *overshoot*; tiempo de asentamiento · *settling time*; tiempo de subida · *rise time*; amortiguamiento · *damping ratio*.

**Continuidad.** B16-C05 introduce la función de transferencia, donde `ωn` y `ζ` se leen directo de los polos. B16-C09 usa los polos dominantes. B16-C11 añade acción integral.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B16-C03 — Sistemas lineales invariantes](../B16-C03-sistemas-lineales-invariantes/CLASE.md) · [📚 Bloque B16](../../../tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) · [Siguiente: B16-C05 — Funciones de transferencia →](../B16-C05-funciones-de-transferencia/CLASE.md)
<!-- /nav -->
