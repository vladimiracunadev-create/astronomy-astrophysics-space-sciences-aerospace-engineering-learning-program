# B09-C08 — Integrales indefinidas

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B09](../../../tronco-comun/B09-calculo-diferencial-e-integral.md) · [← Anterior: B09-C07 — Optimización con derivadas](../B09-C07-optimizacion-con-derivadas/CLASE.md) · [Siguiente: B09-C09 — Integración por sustitución →](../../../tronco-comun/B09-calculo-diferencial-e-integral.md#b09-c09)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Octava clase del bloque B09. Con [C03](../B09-C03-derivada-como-tasa-de-cambio/CLASE.md)–[C07](../B09-C07-optimizacion-con-derivadas/CLASE.md) pasaste de una cantidad a su tasa de cambio. Ahora haces el camino contrario: dada la tasa, **recuperar la cantidad**. Nivel N2. Verás la antiderivada, la constante de integración, las integrales básicas, las condiciones iniciales y el potencial gravitatorio como antiderivada de la gravedad. No verás técnicas de sustitución o partes (C09–C10) ni integrales definidas (C11).

## 2. Por qué esta clase existe

Un acelerómetro mide aceleración; lo que se necesita es velocidad y posición. Una gravedad `g(r)` se conoce; lo que decide si una sonda escapa es la energía, que sale de «deshacer» esa derivada. Toda navegación inercial y todo cálculo de energía pasan por integrar.

La decisión central: **¿cómo recupero una cantidad a partir de su tasa, qué información extra necesito (la constante) y cómo compruebo mi resultado?**

## 3. Lo que podrás hacer al terminar

1. Definir la antiderivada y la integral indefinida y distinguir la constante `C`.
2. Calcular integrales de potencias, `1/x`, `cos`, `sin` y `sec²`.
3. Fijar la constante con condiciones iniciales.
4. Obtener velocidad y posición a partir de un perfil de aceleración.
5. Interpretar el potencial gravitatorio como antiderivada de `g`.
6. Comprobar cualquier antiderivada derivándola.

La evidencia es la **tabla de antiderivadas verificadas** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

Necesitas derivar potencias y funciones trigonométricas. Cinco preguntas:

1. Deriva `x³`.
2. Deriva `x⁻²`.
3. Deriva `sin(3t)`.
4. ¿Cuál es la derivada de una constante?
5. Si `v(t) = 20t`, ¿cuál es su derivada?

<details>
<summary>Ver respuestas</summary>

1. `3x²`. 2. `−2x⁻³`. 3. `3cos(3t)`. 4. 0. 5. 20.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa C04–C05.

## 5. Un caso real: lo que un acelerómetro no sabe

Un vehículo con un acelerómetro mide su aceleración propia `a(t)`; para saber dónde está debe integrarla dos veces. Un pequeño **sesgo** (error constante) crece: con un sesgo de `10⁻³ m/s²` durante 100 s la velocidad se desvía `0,100 m/s` y la posición, `5,00 m`. Esta es la razón por la que la navegación inercial necesita correcciones externas. El **ejemplo conductor** es un perfil de aceleración **sintético**, `a(t) = 20 + 0,5 t` (m/s², con `t` en s), sin gravedad ni arrastre. Un segundo ejemplo usa el potencial gravitatorio terrestre con los valores nominales de la IAU, `(GM)_E^N = 3,986 004 × 10¹⁴ m³ s⁻²` y `R_eE^N = 6,3781 × 10⁶ m` (S2).

## 6. Vocabulario

Una **antiderivada** de `f` es una función `F` tal que `F′ = f`. La **integral indefinida** `∫ f(x) dx` es la familia de todas las antiderivadas: `F(x) + C` (S1, §1.4(iv)). La **constante de integración** `C` es un número arbitrario: derivar lo elimina. Una **condición inicial** es un dato (por ejemplo, `v(0) = 0`) que fija `C`. El símbolo `dx` indica la variable de integración. El **potencial gravitatorio** `Φ` es la función cuya derivada, cambiada de signo, es la aceleración de la gravedad: `g = −dΦ/dr` para un campo radial atractivo. El **sesgo** es un error constante de un instrumento.

## 7. Modelo mental: rebobinar la derivada

Derivar es «hallar la pendiente de cada punto»; integrar es «hallar una curva con esas pendientes». Hay infinitas curvas con la misma pendiente en cada punto, todas desplazadas verticalmente: por eso la constante.

```mermaid
flowchart LR
    A["Posición x(t)"] -->|"derivar"| B["Velocidad v(t)"]
    B -->|"derivar"| C["Aceleración a(t)"]
    C -->|"integrar + C₁"| B
    B -->|"integrar + C₂"| A
```

*Descripción textual:* derivar baja de posición a velocidad a aceleración; integrar sube en sentido contrario y cada subida añade una constante que se fija con una condición inicial.

Analogía: reconstruir un viaje conociendo solo el velocímetro; sin saber dónde empezaste, no sabes dónde estás. Su límite: la analogía ignora que el velocímetro también tiene error.

## 8. La explicación, paso a paso

### 8.1 Las integrales básicas

Se obtienen invirtiendo las derivadas de C04–C05, y se comprueban derivando:

`∫ xⁿ dx = xⁿ⁺¹/(n + 1) + C` para `n ≠ −1`; `∫ dx/x = ln|x| + C`; `∫ cos(kt) dt = sin(kt)/k + C`; `∫ sin(kt) dt = −cos(kt)/k + C`; `∫ sec² x dx = tan x + C`.

La integral de una suma es la suma de integrales y una constante multiplicativa sale. Para `3x² − 4x + 5`: `x³ − 2x² + 5x + C`. Para `x⁻³`: `−1/(2x²) + C`. Para `√x`: `(2/3) x^{3/2} + C`. Para `1/x`, se usa como dato que `(ln|x|)′ = 1/x` (el caso `n = −1`).

### 8.2 La constante

Si `F` es antiderivada, también lo es `F + C`. Con `f = 2 sin x cos x`, tanto `sin² x` como `−cos² x` son antiderivadas, y difieren en la constante `1`, porque `sin² + cos² = 1`. Dos respuestas distintas pueden ser ambas correctas.

### 8.3 Condiciones iniciales

Si `F(1) = 2` para `F = x³ − 2x² + 5x + C`: `1 − 2 + 5 + C = 2` → `C = −2`. En física, cada integración sucesiva trae su constante: la velocidad inicial y la posición inicial.

### 8.4 De la aceleración a la posición

Con `a(t) = 20 + 0,5 t`, `v(0) = 0`, `x(0) = 0`: `v(t) = 20t + 0,25 t² + C₁`, con `C₁ = 0`; `x(t) = 10t² + t³/12 + C₂`, con `C₂ = 0`. En `t = 10 s`: `a = 25 m/s²`, `v = 225 m/s`, `x = 1083,3 m`. Si hubiera una velocidad inicial `v₀`, aparecería como `+ v₀ t` en la posición.

### 8.5 La caída libre, de regreso

Con `a = −g`, `v(0) = v₀`, `x(0) = 0`: `v = v₀ − g t`; `x = v₀ t − ½ g t²`. Es el resultado de [C03](../B09-C03-derivada-como-tasa-de-cambio/CLASE.md), ahora obtenido integrando.

### 8.6 El potencial como antiderivada

Para una masa puntual, `g(r) = GM/r²` (módulo, hacia el centro). Una función cuya derivada es `g` es `Φ(r) = −GM/r`; se elige `C = 0` para que `Φ → 0` cuando `r → ∞`. En la superficie terrestre nominal, `Φ = −6,25 × 10⁷ J/kg`. A 400 km de altitud, `−5,88 × 10⁷ J/kg`. La diferencia, `3,69 × 10⁶ J/kg`, es la energía por kilogramo para subir esa altura; la aproximación `g h = 3,92 × 10⁶ J/kg` la sobreestima 6 %, porque `g` decrece al subir (C04).

### 8.7 Comprobación obligatoria

Toda antiderivada se valida **derivándola**. El laboratorio lo automatiza con un cociente central y compara con el integrando. Una integral sin comprobación es una hipótesis.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Nota |
|---|---|---|---|
| `a(t)` | aceleración propia | m/s² | `20 + 0,5 t` (sintética) |
| `v(t)`, `x(t)` | velocidad y posición | m/s, m | desde reposo en el origen |
| `C`, `C₁`, `C₂` | constantes de integración | según el caso | fijadas por condiciones iniciales |
| `Φ(r)` | potencial gravitatorio | J/kg = m²/s² | `−GM/r` |
| `g(r)` | aceleración gravitatoria | m/s² | `GM/r²` |
| `GM` | parámetro gravitacional | m³/s² | `3,986 004 × 10¹⁴` (nominal, S2) |
| `b` | sesgo del acelerómetro | m/s² | `10⁻³` (sintético) |

Comprobación dimensional: `∫ a dt` tiene unidad m/s²·s = m/s; `∫ g dr` = (m/s²)·m = m²/s².

## 10. Convenciones y referencias

Eje positivo en el sentido del empuje; sin gravedad en el ejemplo del perfil. En el potencial se elige la referencia `Φ(∞) = 0`, una convención: lo físicamente relevante es la **diferencia** de potencial. Los valores nominales de la IAU son factores de conversión (S2).

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NIST, *Digital Library of Mathematical Functions* §1.4, versión 1.2.8 | https://dlmf.nist.gov/1.4 | Integrales indefinidas e integración (§1.4(iv)) | Consultada el 2026-11-05 mediante extracción automática |
| S2 | IAU, Resolución B3 de 2015, arXiv:1510.07674 | https://arxiv.org/pdf/1510.07674 | `(GM)_E^N` y `R_eE^N` nominales | Texto extraído del PDF el 2026-11-05 |

Límites: las tablas de integrales básicas se justifican invirtiendo derivadas y se comprueban numéricamente; no se citan fila por fila de S1. El sesgo y el perfil son **sintéticos**.

## 12. Cómo ver la integración

Equivalente accesible a una gráfica de `a`, `v` y `x` (valores del laboratorio):

| `t` (s) | `a` (m/s²) | `v` (m/s) | `x` (m) |
|---|---|---|---|
| 0 | 20,000 | 0 | 0 |
| 5 | 22,500 | 106,25 | 260,42 |
| 10 | 25,000 | 225,00 | 1083,33 |

Descripción larga: `a` sube linealmente; `v` crece y se curva hacia arriba; `x` crece aún más rápido; cada curva tiene como pendiente el valor de la anterior.

## 13. Ejemplo trabajado: de la aceleración a la posición

**Paso 1 · Datos.** `a(t) = 20 + 0,5 t`, `v(0) = 0`, `x(0) = 0`.

**Paso 2 · Primera integral.** `v(t) = 20t + 0,25 t² + C₁`.

**Paso 3 · Condición.** `v(0) = 0` → `C₁ = 0`.

**Paso 4 · Segunda integral.** `x(t) = 10t² + t³/12 + C₂`; `x(0) = 0` → `C₂ = 0`.

**Paso 5 · Comprobación y sentido.** `x′ = 20t + 0,25t² = v` ✓ y `v′ = 20 + 0,5t = a` ✓. En 10 s: `225 m/s` y `1083,3 m`. Unidades: `m/s` y `m` ✓. Es un modelo sin gravedad ni arrastre.

## 14. Distintas formas de obtener una cantidad desde su tasa

La **antiderivada simbólica** es exacta cuando existe en términos elementales. La **integración numérica** (C11) sirve cuando solo hay datos o no hay fórmula. Las **tablas** ahorran tiempo pero pueden tener errores de transcripción: se verifican derivando. En navegación real se combinan con otras medidas para acotar el sesgo.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `∫(3x² − 4x + 5) dx` y fija `C` si `F(1) = 2`. *Pasos:* integra término a término; sustituye.

<details><summary>Solución comentada</summary>

`F = x³ − 2x² + 5x + C`; `F(1) = 4 + C = 2` → `C = −2`. Comprobación: `F′ = 3x² − 4x + 5` ✓ (8.1, 8.3).
</details>

**Ejercicio 2 · con una pista.** Calcula `∫ x⁻³ dx` y `∫ √x dx`. *Pista:* escribe `√x = x^{1/2}`.

<details><summary>Solución comentada</summary>

`−x⁻²/2 + C = −1/(2x²) + C`; `(2/3) x^{3/2} + C`. Comprueba derivando.
</details>

**Ejercicio 3 · casi autónomo.** Con `a(t) = 20 + 0,5 t`, `v(0) = 0`, `x(0) = 0`, halla `v(5)` y `x(5)`.

<details><summary>Solución comentada</summary>

`v = 20 · 5 + 0,25 · 25 = 106,25 m/s`; `x = 10 · 25 + 125/12 = 260,42 m` (cuadro de la sección 12).
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Calcula `∫ cos(3t) dt`, `∫ sec² x dx` y `∫ dx/x` para `x > 0`.

<details><summary>Solución comentada</summary>

`sin(3t)/3 + C`; `tan x + C`; `ln x + C`. Cada una se comprueba derivando (8.1).
</details>

**Ejercicio 5.** Obtén, integrando, `v(t)` y `x(t)` de un cuerpo con `a = −g`, `v(0) = 100 m/s`, `x(0) = 0`.

<details><summary>Solución comentada</summary>

`v = 100 − g t`; `x = 100t − ½ g t²`. Coincide con C03 (8.5).
</details>

**Ejercicio 6.** Calcula `Φ(R)` y `Φ(R + 400 km)` con los valores nominales y la energía por kg para subir.

<details><summary>Solución comentada</summary>

`Φ(R) = −3,986 004 × 10¹⁴/6,3781 × 10⁶ = −6,2495 × 10⁷ J/kg`; `Φ(R + 4 × 10⁵) = −5,8807 × 10⁷`; diferencia `3,688 × 10⁶ J/kg` (8.6).
</details>

**Ejercicio 7.** Comprueba que `sin² x` y `−cos² x` son antiderivadas de `2 sin x cos x` y halla su diferencia.

<details><summary>Solución comentada</summary>

`(sin² x)′ = 2 sin x cos x`; `(−cos² x)′ = 2 cos x sin x`. Diferencia: `sin² x + cos² x = 1`. Ambas valen: difieren en una constante (8.2).
</details>

**Ejercicio 8.** Verifica por unidades que `∫ v dt` es una longitud y que `∫ g dr` es una energía por masa.

<details><summary>Solución comentada</summary>

(m/s)·s = m. (m/s²)·m = m²/s² = J/kg, porque `1 J = 1 kg m²/s²`.
</details>

**Ejercicio 9 · transferencia.** Un acelerómetro tiene un sesgo constante de `2 × 10⁻³ m/s²`. ¿Qué error de velocidad y de posición acumula tras 60 s y tras 600 s?

<details><summary>Solución comentada</summary>

`δv = b t`, `δx = b t²/2`. A 60 s: `0,12 m/s` y `3,6 m`. A 600 s: `1,2 m/s` y `360 m`. El error de posición crece con el cuadrado del tiempo: de ahí que la navegación inercial necesite correcciones externas. Cálculo ilustrativo con sesgo sintético.
</details>

**Ejercicio 10 · transferencia.** Un compañero afirma que `∫ x · x dx = (∫ x dx)(∫ x dx)`. Evalúa.

<details><summary>Solución comentada</summary>

`∫ x² dx = x³/3`, pero `(x²/2)² = x⁴/4`. No existe regla del producto para integrales (se verá la integración por partes en C10).
</details>

**Ejercicio 11 · transferencia.** ¿Es correcto escribir `∫ dx/x = ln x + C` para `x < 0`? Corrige.

<details><summary>Solución comentada</summary>

No: `ln x` no está definido para `x < 0`. Con `ln|x|`: para `x < 0`, `|x| = −x` y `(ln(−x))′ = (−1)/(−x) = 1/x` ✓. Por eso se escribe `ln|x|`.
</details>

**Ejercicio 12 · integrador.** Elabora tu *tabla de antiderivadas verificadas*: seis funciones (potencia, raíz, negativa, trigonométrica, suma, `1/x`) con su antiderivada, un punto de comprobación y la diferencia entre `F′(x)` y `f(x)`, más el perfil `a(t)` con `v` y `x` en tres instantes.

<details><summary>Solución modelo</summary>

Tabla con columnas función, antiderivada, `x` de prueba, `F′(x)` por cociente central, `f(x)` y diferencia (< 10⁻⁶ relativa); perfil de aceleración con `v(10) = 225 m/s` y `x(10) = 1083,3 m`; se declara que el perfil es sintético.
</details>

## 17. Laboratorio: antiderivadas y potencial

El script [antiderivadas_y_potencial.py](antiderivadas_y_potencial.py) calcula antiderivadas de polinomios generalizados por la regla de la potencia, las comprueba derivando, integra el perfil de aceleración, muestra que dos antiderivadas difieren en una constante y evalúa el potencial terrestre y el sesgo del acelerómetro.

**Datos:** perfil y sesgo sintéticos; parámetros nominales de la IAU. **Predice antes de ejecutar:** ¿qué dará `x(10)`? (`1083,33 m`.) **Ejecución del 2026-11-05 (Python 3.12.9):**

```text
int [x^-3] dx = {-2: -0.5}  (+ C)  -> comprobada
      5     22.500    106.250    260.417
     10     25.000    225.000   1083.333
sin^2 x - (-cos^2 x) = 1.000000000000 para todo x (constante)
Phi(R) = -6.2495e+07 J/kg;  Phi(R+400 km) = -5.8807e+07 J/kg
Energía por kg para subir 400 km = 3.6881e+06 J/kg;  g(R)*h = 3.9194e+06 J/kg
Sesgo 0.001 m/s2 durante 100 s: error de v = 0.100 m/s; error de x = 5.000 m
Pruebas superadas.
```

```bash
python programa/clases/B09/B09-C08-integrales-indefinidas/antiderivadas_y_potencial.py
```

**Límites:** polinomios con exponentes distintos de −1; perfil sintético; no es un filtro de navegación.

## 18. Errores frecuentes y cómo corregirlos

**Olvidar la constante de integración.** Se corrige con los ejercicios 1 y 7.

**Usar `n = −1` en la regla de la potencia.** Se corrige con el ejercicio 4.

**Integrar un producto como producto de integrales.** Se corrige con el ejercicio 10.

**Escribir `ln x` donde `x` puede ser negativo.** Se corrige con el ejercicio 11.

**No comprobar derivando.** Se corrige con la sección 8.7 y el ejercicio 12.

## 19. Cómo sabrás que vas bien

Tras 8.1: ¿integras `3x² − 4x + 5` y lo compruebas? Si no, ejercicio 1. Tras 8.3: ¿fijas `C`? Si no, ejercicio 1. Tras 8.4: ¿obtienes `v` y `x` desde `a`? Si no, ejercicio 3. Tras el laboratorio: ¿qué cálculo demuestra que dos antiderivadas distintas son ambas correctas? (la diferencia constante).

## 20. Qué entregas y cómo se evalúa

El producto es tu **tabla de antiderivadas verificadas** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Integrales básicas | Errores de regla | Con ayuda | Correctas | Explica los casos especiales |
| Constante | Ausente | La escribe sin fijarla | La fija con una condición | Interpreta su significado físico |
| Comprobación | Ausente | Mental | Derivando | Con cociente numérico |
| Unidades | Omitidas | Parciales | Verificadas | Detecta errores dimensionales |
| Fuentes | Sin fuente | Sin fecha | Con localizador y fecha | Rotula sintético |

**Condiciones críticas (no se compensan con promedio):** comprobar cada antiderivada derivando; incluir la constante; citar solo fuentes consultadas.

## 21. Ética, seguridad y límites

Presentar una posición integrada sin su incertidumbre induce a error: en navegación el error crece con el tiempo y debe informarse. Esta clase no sirve para diseñar un sistema de navegación. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

La integral indefinida deshace la derivada y deja una constante que se fija con una condición inicial; el potencial gravitatorio es una antiderivada de `g`; toda antiderivada se comprueba derivando. Queda abierta una pregunta: ¿qué hacer cuando la expresión no se parece a ninguna integral básica? Se transforma con una sustitución.

**Glosario español–inglés.** antiderivada · *antiderivative*; integral indefinida · *indefinite integral*; constante de integración · *constant of integration*; condición inicial · *initial condition*; potencial gravitatorio · *gravitational potential*; sesgo · *bias*; navegación inercial · *inertial navigation*.

**Continuidad.** B09-C09 reutiliza tu capacidad de **reconocer la derivada de una función compuesta** para integrar por sustitución.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B09-C07 — Optimización con derivadas](../B09-C07-optimizacion-con-derivadas/CLASE.md) · [📚 Bloque B09](../../../tronco-comun/B09-calculo-diferencial-e-integral.md) · [Siguiente: B09-C09 — Integración por sustitución →](../../../tronco-comun/B09-calculo-diferencial-e-integral.md#b09-c09)
<!-- /nav -->
