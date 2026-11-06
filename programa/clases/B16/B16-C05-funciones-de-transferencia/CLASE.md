# B16-C05 — Funciones de transferencia

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B16](../../../tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) · [← Anterior: B16-C04 — Respuesta transitoria y estacionaria](../B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md) · [Siguiente: B16-C06 — Diagramas de bloques →](../B16-C06-diagramas-de-bloques/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Quinta clase del bloque B16. Hasta ahora has descrito sistemas con ecuaciones diferenciales y matrices ([C01](../B16-C01-modelos-dinamicos-y-estados/CLASE.md) a [C04](../B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md)). Aquí aprendes a describir un sistema LTI por el **cociente de dos polinomios en `s`**, la función de transferencia, donde derivar se vuelve multiplicar y la convolución se vuelve producto. Necesitas álgebra de polinomios, raíces y la transformada de Laplace básica (explicada abajo).

No verás aún cómo combinar bloques (C06) ni la estabilidad del lazo (C07).

## 2. Por qué esta clase existe

Un ingeniero que diseña el control de actitud de un telescopio revisa decenas de variantes de ganancias. Resolver una ecuación diferencial para cada una es lento; en cambio, si cada elemento (rueda, cuerpo, sensor) se resume en un cociente de polinomios, las variantes se evalúan con álgebra y los **polos** (las raíces del denominador) dicen de un vistazo si el sistema oscila, se frena o se escapa. La pregunta motivadora es: **¿cómo resumo el comportamiento de entrada a salida en una expresión que se pueda multiplicar, invertir y leer?**

La decisión central es qué polinomios `N(s)` y `D(s)` representan al sistema y qué información (polos, ceros, ganancia) se extrae de ellos.

## 3. Lo que podrás hacer al terminar

1. Obtener `G(s)` de una ecuación diferencial con condiciones iniciales nulas.
2. Calcular `G(s) = C(sI − A)⁻¹B + D` a partir del espacio de estados.
3. Identificar polos, ceros, orden y ganancia estática de `G(s)`.
4. Relacionar los polos con `ωn`, `ζ` y la respuesta de la clase C04.
5. Usar fracciones simples y el teorema del valor final para obtener una respuesta.
6. Comprobar una función de transferencia contra una simulación.

La evidencia es la **tarjeta de transferencia** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. Factoriza `s² + 0,2 s`.
2. Descompón `1/(s(s+2))` en `A/s + B/(s+2)`.
3. ¿Qué raíces tiene `s² + 0,8 s + 0,4`?
4. ¿Qué es la parte real de `−0,4 + 0,49 j`?
5. ¿Cuál es la respuesta temporal de `ẏ = −2y` con `y(0) = 1`?

<details>
<summary>Ver respuestas</summary>

1. `s(s + 0,2)`. 2. `A = 1/2`, `B = −1/2`. 3. `s = −0,4 ± 0,49 j` (`√(0,16−0,4) = j0,49`). 4. `−0,4`. 5. `y = e^(−2t)`.
</details>

Con cuatro o cinco aciertos, sigue; si fallaste la 3, repasa B09 (raíces) antes.

## 5. Un caso real: de la rueda al ángulo

La página de archivo del sistema de control de apuntamiento del Hubble (S2) describe una cadena: sensores miden, un computador calcula, y cuatro ruedas de reacción (de hasta 3000 rpm) aplican el par. Cada eslabón puede resumirse en una función de transferencia: de par a ángulo para el cuerpo del telescopio, de orden a par para la rueda, de ángulo a señal medida para el sensor. Combinadas (C06), dan el comportamiento del lazo. Nuestro ejemplo sigue siendo sintético: eje con `J = 50 kg·m²`, fricción `c = 10 N·m·s/rad`, lazo PD con `Kp = 20 N·m/rad` y `Kd = 40 N·m·s/rad`.

## 6. Vocabulario

La **transformada de Laplace** de una función `f(t)` definida para `t ≥ 0` es `F(s) = ∫₀^∞ e^(−st) f(t) dt` (S1, ec. 1.14.17), con `s` un número complejo cuya parte real es suficientemente grande para que la integral converja; sus unidades son s⁻¹. Una propiedad clave: la transformada de la derivada es `s F(s) − f(0⁺)` (S1, ec. 1.14.27). La **función de transferencia** `G(s)` es el cociente `Y(s)/U(s)` con condiciones iniciales nulas. Sus **polos** son las raíces del denominador; sus **ceros**, las del numerador. El **orden** es el grado del denominador. La **ganancia estática** es `G(0)`. Es **propia** si el grado del numerador no supera al del denominador.

## 7. Modelo mental: el sistema como un factor

En el dominio del tiempo, la salida es la convolución de la entrada con `h(t)` (C03). La transformada de una convolución es el producto de las transformadas (S1, ec. 1.14.31): `Y(s) = G(s) U(s)`. Es como pasar de multiplicar con una regla de cálculo logarítmica: lo difícil (convolucionar) se vuelve fácil (multiplicar).

```mermaid
flowchart LR
    U["U(s)"] --> G["G(s) = N(s)/D(s)"] --> Y["Y(s) = G(s) U(s)"]
```

*Descripción textual:* una entrada transformada `U(s)` entra en un bloque `G(s)`, cociente de dos polinomios, y sale `Y(s)`, que es el producto de ambos.

El límite de la analogía: la transformada de Laplace es una herramienta para sistemas LTI con condiciones iniciales nulas; una saturación o una condición inicial no nula no se resumen con un solo cociente.

## 8. La explicación, paso a paso

### 8.1 De la ecuación a la función de transferencia

Toma `J ω̇ + c ω = τ` con reposo inicial. Transformando: `J s Ω(s) + c Ω(s) = T(s)`, luego `Ω/T = 1/(J s + c)`. Con `J = 50` y `c = 10`: `0,02/(s + 0,2)`. Como `θ̇ = ω`, el ángulo es `Θ = Ω/s`, de modo que `G(s) = Θ/T = 1/(s(J s + c))`. El eje sin fricción es `1/(J s²)`: un doble integrador.

### 8.2 Desde el espacio de estados

Si `ẋ = A x + B u`, `y = C x + D u` y `x(0) = 0`, la transformación da `s X = A X + B U`, es decir `X = (sI − A)⁻¹ B U`, y entonces `G(s) = C (sI − A)⁻¹ B + D`. Con las matrices de C02 para el eje con fricción, el cálculo da `0,02/(s² + 0,2 s)`. Los **polos** de `G` son autovalores de `A` (salvo cancelaciones): aquí `0` y `−0,2`.

### 8.3 Qué dicen los polos

Cada polo `p` aporta a la respuesta un término `e^(pt)`. Polo real negativo: caída exponencial con constante de tiempo `1/|p|`. Par complejo `−σ ± jωd`: oscilación amortiguada de frecuencia `ωd` con envolvente `e^(−σt)`. Polo en el origen: integrador. Polo con parte real positiva: crecimiento. Un cero cambia los coeficientes de esas exponenciales: no crea movimientos nuevos, pero afecta a cuánto pesan.

### 8.4 La forma estándar de segundo orden

Un sistema de segundo orden sin ceros es `ωn²/(s² + 2ζωn s + ωn²)`. Sus polos son `−ζωn ± jωn√(1−ζ²)`. Eso conecta con C04: `Mp`, `tp` y `ts` salen de la posición de los polos. En nuestro lazo PD (derivada sobre el error), `T(s) = (Kd s + Kp)/(J s² + Kd s + Kp) = (40 s + 20)/(50 s² + 40 s + 20)`: polos `−0,4 ± 0,49 j`, `ωn = 0,632 rad/s`, `ζ = 0,632`, y un cero en `−Kp/Kd = −0,5`.

### 8.5 Fracciones simples y valor final

Para la respuesta al escalón se calcula `Y(s) = G(s)/s` y se descompone en fracciones simples; cada una se invierte con `e^(pt)`. El **teorema del valor final** dice que, si `s Y(s)` tiene todos sus polos en el semiplano izquierdo, `y(∞) = lim_{s→0} s Y(s)`. Para nuestro `T(s)`, el valor final es `T(0) = Kp/Kp = 1`: el lazo sigue una referencia constante sin error.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Nota |
|---|---|---|---|
| `s` | variable de Laplace | s⁻¹ (rad/s) | complejo |
| `G(s)` | función de transferencia | unidades de salida / unidades de entrada | depende de la pareja entrada–salida |
| `Θ, Ω, T` | transformadas de ángulo, velocidad y par | — | mayúsculas |
| `p` | polo | s⁻¹ | |
| `z` | cero | s⁻¹ | |
| `ωn, ζ` | frecuencia natural y amortiguamiento | rad/s; — | C04 |

La función `1/(J s²)` tiene unidades de rad/(N·m).

## 10. Convenciones y referencias

Mayúsculas para transformadas y minúsculas para funciones del tiempo. Se supone siempre `t ≥ 0` y condiciones iniciales nulas, salvo aviso. Un polinomio se escribe con el coeficiente de mayor grado primero. Dos expresiones que difieren por un factor común en numerador y denominador describen la misma función de transferencia, pero una pierde información de estado (C13).

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NIST, *Digital Library of Mathematical Functions*, §1.14(iii) | https://dlmf.nist.gov/1.14 | Definición de la transformada de Laplace (1.14.17), transformada de la derivada (1.14.27), de la convolución (1.14.31) | Consultada el 2026-11-05 mediante extracción automática |
| S2 | NASA GSFC, *Pointing Control System* (archivo del Hubble, actualizada 2021-03-29) | https://asd.gsfc.nasa.gov/archive/hubble/technology/pcs.html | Cadena sensores–computador–ruedas de reacción (hasta 3000 rpm) | Consultada el 2026-11-05; archivada |

Límites: `G(s) = C(sI − A)⁻¹B + D`, las fracciones simples y el teorema del valor final son resultados estándar de teoría de sistemas, no citados a un texto, y se verifican numéricamente. Las cifras son **sintéticas**.

## 12. Cómo ver una función de transferencia

| Sistema | `G(s)` | Polos | Ceros | Ganancia estática |
|---|---|---|---|---|
| Eje sin fricción (ángulo) | `1/(50 s²)` | 0, 0 | ninguno | no definida |
| Eje con fricción (velocidad) | `0,02/(s+0,2)` | −0,2 | ninguno | 0,1 rad/s por N·m |
| Eje con fricción (ángulo) | `0,02/(s(s+0,2))` | 0, −0,2 | ninguno | no definida |
| Lazo PD cerrado | `(40s+20)/(50s²+40s+20)` | −0,4 ± 0,49j | −0,5 | 1 |

Dibuja el plano `s` con una cruz por polo y un círculo por cero; usa marcadores distintos y rotula cada uno con su valor.

## 13. Ejemplo trabajado: del lazo PD a su respuesta

¿Cómo responde el lazo PD al escalón de 1 rad?

**Paso 1.** `Y(s) = T(s)/s = (40 s + 20)/(s(50 s² + 40 s + 20))`.
**Paso 2 · polos.** `s = 0` y `−0,4 ± 0,49 j`. Por el teorema del valor final, `y(∞) = T(0) = 1`.
**Paso 3 · fracciones simples.** Se descompone en un residuo en `s = 0` (el valor final) más dos términos complejos conjugados que forman una sinusoide amortiguada de frecuencia `0,49 rad/s`.
**Paso 4 · comprobación.** El laboratorio de la sección 17 hace la descomposición con `scipy.signal.residue` y la compara con la respuesta de `scipy.signal.step`: el error máximo es 7×10⁻¹⁵ rad. El valor a los 30 s es 1,000008 rad.
**Paso 5 · lectura.** La envolvente `e^(−0,4t)` explica un asentamiento de unos `4/0,4 = 10 s`.

## 14. Distintas descripciones de un mismo sistema

El **espacio de estados** (C02) conserva todos los estados internos y vale para varias entradas y salidas; la **función de transferencia** solo describe la relación de una entrada con una salida, ignora lo que se cancele entre polos y ceros, y es compacta. La **respuesta al impulso** (C03) es lo que se mide directamente en un ensayo. La **respuesta en frecuencia** (C10) es la función de transferencia evaluada en `s = jω`. Elige la función de transferencia para analizar lazos de una entrada y una salida; el espacio de estados para multivariable, observadores y control óptimo (C13–C15).

## 15. Práctica guiada

**Ejercicio 1 · con pasos.** Halla `G(s)` de `20 ω̇ + 4 ω = τ` y su constante de tiempo. *Pasos:* 8.1.

<details><summary>Solución comentada</summary>

`G = 1/(20 s + 4) = 0,05/(s + 0,2)`; polo `−0,2`; constante `5 s`; ganancia estática `0,25 rad/s` por N·m.
</details>

**Ejercicio 2 · con pista.** Para `A = [[0,1],[0,−0,2]]`, `B = [0, 0,02]ᵀ`, `C = [1, 0]` calcula `G(s)`. *Pista:* `(sI−A)⁻¹` para una matriz 2×2.

<details><summary>Solución comentada</summary>

`sI − A = [[s,−1],[0, s+0,2]]`, su inversa es `1/(s(s+0,2)) [[s+0,2, 1],[0, s]]`. `C(sI−A)⁻¹B` toma la fila 1, columna 2 por 0,02: `0,02/(s(s+0,2))`.
</details>

**Ejercicio 3 · casi autónomo.** Para `G(s) = 4/(s² + 2 s + 4)` halla `ωn`, `ζ` y `Mp`.

<details><summary>Solución comentada</summary>

`ωn² = 4` → `ωn = 2`; `2ζωn = 2` → `ζ = 0,5`; `Mp = exp(−π·0,5/0,866) = 16,3 %`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Para `G(s) = (s + 3)/((s + 1)(s + 5))` indica polos, ceros, orden y ganancia estática.

<details><summary>Solución comentada</summary>

Polos −1 y −5; cero −3; orden 2; `G(0) = 3/5 = 0,6`.
</details>

**Ejercicio 5.** Descompón `Y(s) = 1/(s(s+2))` y obtén `y(t)`.

<details><summary>Solución comentada</summary>

`1/(s(s+2)) = 0,5/s − 0,5/(s+2)`, luego `y(t) = 0,5(1 − e^(−2t))`; valor final 0,5.
</details>

**Ejercicio 6.** Con el teorema del valor final calcula `y(∞)` para `Y(s) = 6/(s(s+3))`. ¿Es aplicable?

<details><summary>Solución comentada</summary>

`lim s Y = 6/3 = 2`. Sí: el único polo de `sY` es −3 (estable).
</details>

**Ejercicio 7.** ¿Qué pasa con el teorema del valor final para `Y(s) = 1/(s(s−1))`?

<details><summary>Solución comentada</summary>

La fórmula daría `lim s Y = −1`, pero no es aplicable: hay un polo en `+1` y la respuesta crece sin límite. Siempre se verifica que los polos de `sY` estén en el semiplano izquierdo.
</details>

**Ejercicio 8.** Un lazo tiene polos en `−0,3 ± 0,4 j`. Estima `ωn`, `ζ`, `Mp` y `ts` al 2 %.

<details><summary>Solución comentada</summary>

`ωn = √(0,09+0,16) = 0,5`; `ζ = 0,3/0,5 = 0,6`; `Mp = exp(−π·0,6/0,8) = 9,5 %`; `ts ≈ 4/0,3 = 13,3 s`.
</details>

**Ejercicio 9 · transferencia.** La rueda se modela `W/U = b/(s + a)` con `a = 0,5`, `b = 0,5` (C01) y el par es `τ = k_w w`. Escribe la función de transferencia de la orden `U` al par `T`.

<details><summary>Solución comentada</summary>

`T/U = k_w b/(s + a)`: un retardo de primer orden de ganancia estática `k_w b/a`. Con la planta `1/(J s²)` quedará un sistema de tercer orden (C06).
</details>

**Ejercicio 10 · transferencia.** Un instrumento térmico tiene `C_t Ṫ = P − T/R` (desviación). Escribe `G(s)=T/P` y su constante de tiempo.

<details><summary>Solución comentada</summary>

`G = R/(R C_t s + 1)`; constante `R C_t`. Tiene la misma forma que la rueda: primer orden con ganancia estática `R`.
</details>

**Ejercicio 11 · transferencia.** Explica por qué `(s+1)/((s+1)(s+2))` y `1/(s+2)` coinciden como función de transferencia y por qué eso no siempre es inocuo.

<details><summary>Solución comentada</summary>

Tras cancelar, son idénticas. Pero si el factor cancelado era un polo inestable (por ejemplo `s−1`), la cancelación oculta un modo que sigue vivo en el estado y puede crecer sin que la salida lo muestre (C13).
</details>

**Ejercicio 12 · integrador.** Entrega una **tarjeta de transferencia**: para un sistema real que elijas, escribe las ecuaciones, la `G(s)`, los polos y ceros con su mapa en el plano `s`, la respuesta a un escalón por fracciones simples y una comprobación numérica.

<details><summary>Solución modelo</summary>

Una tarjeta correcta tiene unidades, polinomios explícitos, polos y ceros con su efecto, el valor final con el chequeo del teorema y un cálculo numérico del escalón que coincide con la fórmula.
</details>

## 17. Laboratorio: de estados a transferencia

El script [funcion_de_transferencia.py](funcion_de_transferencia.py) calcula `C(sI−A)⁻¹B` en tres puntos del plano `s` y lo compara con `1/(s(Js+c))`, usa `ss2tf` para el numerador y denominador, calcula los polos del lazo PD y compara la respuesta por fracciones simples con la integración de `scipy.signal`.

**Datos:** sintéticos (simulados). **Predice:** polos del lazo en `−0,4 ± 0,49 j`. **Ejecución del 2026-11-05 (Python 3.12.9, numpy 2.4.4, scipy 1.17.1):**

```text
G(s) = C(sI-A)^-1 B coincide con 1/(s(Js+c)) en 3 puntos
ss2tf: num = [0.   0.   0.02]  den = [1.  0.2 0. ]
polos de G: [-0.2  0. ]
ganancia de velocidad a baja frecuencia 1/c = 0.100 rad/s por N m
T(s): polos -0.4000+0.4899j, -0.4000-0.4899j; wn = 0.6325 rad/s, zeta = 0.6325; cero en -0.500
escalón: residuos vs scipy.signal.step, error máx = 6.66e-15
valor final del escalón = T(0) = 1.0; y(30 s) = 1.000008
Pruebas superadas.
```

```bash
python programa/clases/B16/B16-C05-funciones-de-transferencia/funcion_de_transferencia.py
```

**Límites:** sistema LTI sin retardos puros; el script detiene la ejecución si algún chequeo falla por encima de 10⁻¹².

## 18. Errores frecuentes y cómo corregirlos

**Olvidar las condiciones iniciales nulas.** Se corrige releyendo 6 y 8.1.

**Aplicar el valor final con polos inestables.** Se corrige con el ejercicio 7.

**Cancelar un polo inestable.** Se corrige con el ejercicio 11.

**Confundir `s` con una frecuencia real.** `s` es complejo; en `s = jω` se obtiene la respuesta en frecuencia (C10).

**Mezclar velocidad y ángulo como salida.** Se corrige con la tabla de 12.

## 19. Cómo sabrás que vas bien

Tras 8.1: ¿obtienes `G(s)` de una ecuación? Ejercicio 1. Tras 8.4: ¿pasas de polos a `ωn` y `ζ`? Ejercicio 8. Tras el ejemplo: ¿explicas por qué el valor final es 1? Al final: ¿tu tarjeta compara fórmula y cálculo?

## 20. Qué entregas y cómo se evalúa

El producto es la **tarjeta de transferencia** del ejercicio 12.

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Obtención de `G(s)` | Sin pasos | Con errores | Correcta con unidades | Desde dos caminos (ecuación y estados) |
| Polos y ceros | No los lista | Los lista | Los interpreta | Relaciona con C04 |
| Respuesta temporal | Sin cálculo | Sólo valor final | Fracciones simples | Verifica numéricamente |
| Fuentes y datos | Sin rótulo | Parcial | Rotula sintético | Cita solo lo consultado |

**Condiciones críticas:** condiciones iniciales nulas declaradas; no cancelar polos inestables sin advertirlo.

## 21. Ética, seguridad y límites

Una función de transferencia sin dominio de validez da confianza falsa. Cifras didácticas. Accesibilidad: diagramas con descripción textual y tabla de polos.

## 22. Para cerrar y seguir

La transformada de Laplace convierte derivadas en multiplicaciones por `s` y convoluciones en productos; la función de transferencia es el cociente de polinomios cuyos polos fijan la respuesta. Sale de una ecuación o de `C(sI−A)⁻¹B + D`. Queda abierta una pregunta: ¿cómo se combinan varias funciones de transferencia en un lazo?

**Glosario español–inglés.** función de transferencia · *transfer function*; polo · *pole*; cero · *zero*; ganancia estática · *DC gain*; transformada de Laplace · *Laplace transform*; teorema del valor final · *final value theorem*.

**Continuidad.** B16-C06 combina funciones de transferencia con diagramas de bloques. B16-C10 evalúa `G(jω)`. B16-C13 explica qué se pierde al cancelar polos y ceros.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B16-C04 — Respuesta transitoria y estacionaria](../B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md) · [📚 Bloque B16](../../../tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) · [Siguiente: B16-C06 — Diagramas de bloques →](../B16-C06-diagramas-de-bloques/CLASE.md)
<!-- /nav -->
