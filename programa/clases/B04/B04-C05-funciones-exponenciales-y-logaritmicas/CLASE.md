# B04-C05 — Funciones exponenciales y logarítmicas

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B04](../../../tronco-comun/B04-algebra-trigonometria-y-geometria-espacial.md) · [← Anterior: B04-C04 — Funciones y gráficas](../B04-C04-funciones-y-graficas/CLASE.md) · [Siguiente: B04-C06 — Identidades trigonométricas →](../B04-C06-identidades-trigonometricas/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Quinta clase del bloque B04. En [B01-C02](../../B01/B01-C02-escalas-desde-la-tierra-al-cosmos-observable/CLASE.md) usaste `log₁₀` como herramienta para contar órdenes de magnitud; y en la [clase anterior](../B04-C04-funciones-y-graficas/CLASE.md) viste funciones de potencia. Ahora el exponente es la *variable*: `y = bˣ`, y su inversa, el logaritmo. Nivel N1. Verás exponenciales, logaritmos y sus reglas, la escala de magnitudes, el módulo de distancia y la atenuación exponencial de la luz. No verás derivadas ni ecuaciones diferenciales (B09, B11).

## 2. Por qué esta clase existe

El ojo y los instrumentos comparan brillos que difieren en factores de un millón. Los astrónomos lo resuelven con una escala logarítmica: la **magnitud**. Sin entenderla, una diferencia de «cinco magnitudes» parece pequeña cuando en realidad es un factor cien en flujo, y un cálculo de distancia a partir del brillo sale mal.

La decisión central: **¿cómo paso de un cociente de flujos a una diferencia de magnitudes, y de esta a una distancia, sin equivocar el signo ni el factor?** Aprenderás las reglas del logaritmo y las aplicarás a una definición real de la IAU.

## 3. Lo que podrás hacer al terminar

1. Evaluar `bˣ`, `log_b(x)`, `ln x` y pasar de una base a otra.
2. Resolver ecuaciones del tipo `bˣ = y` con logaritmos.
3. Convertir entre cociente de flujos y diferencia de magnitudes (`−2,5 log₁₀`).
4. Usar el módulo de distancia `m − M = 5 log₁₀(d/10 pc)`.
5. Calcular una atenuación exponencial `I = I₀ e^(−τ)` y expresarla en magnitudes.
6. Comprobar una definición publicada con un cálculo independiente.

La evidencia es la **tabla magnitud–flujo–distancia con comprobación** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

Necesitas potencias, notación científica y funciones (C04). Cinco preguntas:

1. ¿Cuánto es `10³` y cuánto `10⁻²`?
2. ¿Qué número `x` cumple `10ˣ = 1000`?
3. Si una cantidad se multiplica por 100, ¿cuántos órdenes de magnitud aumenta?
4. ¿Cuánto es `2⁵`?
5. Escribe el cociente `3,0 × 10⁻⁸ / 3,0 × 10⁻¹⁰`.

<details>
<summary>Ver respuestas</summary>

1. 1000 y 0,01. 2. `x = 3`. 3. 2. 4. 32. 5. 100.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa B01-C02 y C04.

## 5. Un caso real: el brillo del Sol medido en magnitudes

La Unión Astronómica Internacional (IAU) fijó en 2015 el cero de la escala de **magnitud bolométrica** (la que suma todas las longitudes de onda): una fuente de magnitud absoluta 0 tiene una luminosidad de exactamente `3,0128 × 10²⁸ W` (S1). Con la luminosidad nominal del Sol, `3,828 × 10²⁶ W` (S2), su magnitud absoluta sale 4,74. Visto desde la Tierra, con la irradiancia nominal `1361 W/m²` (S2), su magnitud aparente es −26,832 (S1). Ambos números deben ser coherentes con el *módulo de distancia* entre 10 pc y 1 au: esa coherencia es la comprobación que harás en el laboratorio. Es una necesidad concreta: toda comparación de brillos entre estrellas, cometas o satélites usa esta escala.

## 6. Vocabulario

Una **función exponencial** tiene la forma `y = a·bˣ`, con base `b > 0` y `b ≠ 1`; el **número de Euler** `e ≈ 2,71828` es la base natural. El **logaritmo en base `b`** es el exponente al que hay que elevar `b` para obtener el número: `log_b(y) = x` significa `bˣ = y`. El **logaritmo decimal** usa `b = 10`; el **natural**, `ln`, usa `b = e`. La **magnitud aparente** `m` mide cuán brillante *se ve* un objeto desde donde se mide; la **magnitud absoluta** `M` es la que tendría a 10 parsecs; la diferencia `m − M` es el **módulo de distancia**. La **irradiancia** `f` es la potencia por unidad de área que llega (W/m²) y la **luminosidad** `L` la potencia total que emite (W). La **extinción** es la pérdida de luz por absorción y dispersión en el camino; si es exponencial, `I = I₀ e^(−τ)` con `τ` la **profundidad óptica**.

## 7. Modelo mental: sumar exponentes en vez de multiplicar

Multiplicar potencias de la misma base equivale a sumar exponentes: `bᵃ·bᶜ = bᵃ⁺ᶜ`. El logaritmo convierte esa idea en herramienta: `log(xy) = log x + log y`. Una escala logarítmica transforma *cocientes* en *diferencias*: por eso «5 magnitudes» es una diferencia, pero un factor 100 de flujo.

```mermaid
flowchart LR
    A["Flujo f (W/m²)<br/>de 10⁻¹² a 10³"] --> B["Cociente f / f₀"]
    B --> C["−2,5·log₁₀(…)"]
    C --> D["Magnitud m<br/>de ≈ +30 a −27"]
    D --> E["m − M = 5·log₁₀(d/10 pc)"]
    E --> F["Distancia d"]
```

*Descripción textual:* se parte de un flujo, se divide por el flujo de referencia, se aplica `−2,5 log₁₀` para obtener la magnitud, y restando la magnitud absoluta se obtiene el módulo de distancia, de donde sale la distancia.

Analogía: una regla de cálculo, que convierte multiplicaciones en desplazamientos. Su límite: el signo de la magnitud está invertido (más brillante = número menor), por herencia histórica; no es un error de cálculo.

## 8. La explicación, paso a paso

### 8.1 Reglas del logaritmo

Para `x, y > 0`: `log(xy) = log x + log y`; `log(x/y) = log x − log y`; `log(xⁿ) = n log x`; `log_b(b) = 1`; `log_b(1) = 0`. Cambio de base: `log_b(x) = ln x / ln b`. Y la ida y vuelta: `b^(log_b x) = x`.

### 8.2 Resolver `bˣ = y`

Se aplica logaritmo a ambos lados: `x = log_b(y) = ln y / ln b`. Ejemplo: ¿en cuántos periodos se duplica una cantidad que crece 3 % por periodo? `1,03ˣ = 2` → `x = ln 2 / ln 1,03 = 23,45`. El resultado se redondea al contexto: 23,5 periodos.

### 8.3 Magnitudes

La definición (S1): `M = −2,5 log₁₀(L/L₀)` con `L₀ = 3,0128 × 10²⁸ W`, y `m = −2,5 log₁₀(f/f₀)` con `f₀ = 2,518021 × 10⁻⁸ W/m²`. La razón `100^(1/5) = 2,512` se llama **razón de Pogson**: cada magnitud de diferencia es un factor 2,512 en flujo y cinco magnitudes, un factor 100. El signo menos hace que a mayor flujo, menor magnitud.

### 8.4 Módulo de distancia

Si la fuente emite isótropamente, el flujo cae con el cuadrado de la distancia: `f = L/(4πd²)`. La magnitud absoluta es la que daría a `d = 10 pc`, de modo que `m − M = −2,5 log₁₀[(10/d)²] = 5 log₁₀(d/10 pc)`. Con `d` en parsecs, `m − M = 5 log₁₀ d − 5`. Para el Sol, `d = 1 au = 4,848 × 10⁻⁶ pc`: `m − M = 5 log₁₀(4,848 × 10⁻⁷) = −31,57`, y `4,74 − 31,57 = −26,83`, que coincide con S1.

### 8.5 Atenuación exponencial

Si cada capa de atmósfera o de polvo deja pasar la misma fracción, la intensidad decae `I = I₀ e^(−τ)`. En magnitudes, la pérdida es `Δm = −2,5 log₁₀(e^(−τ)) = 1,0857 τ`. Con `τ = 0,25` (valor sintético) la luz baja al 77,9 % y se pierden 0,271 mag.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor o nota |
|---|---|---|---|
| `L` | luminosidad | W | `L_☉ = 3,828 × 10²⁶ W` nominal (S2) |
| `L₀` | cero de magnitud absoluta bolométrica | W | `3,0128 × 10²⁸` exacta (S1) |
| `f` | irradiancia | W/m² | `S_☉ = 1361` nominal (S2) |
| `f₀` | cero de magnitud aparente bolométrica | W/m² | `2,518021002 × 10⁻⁸` (S1) |
| `M`, `m` | magnitud absoluta y aparente | mag (adimensional) | menor = más brillante |
| `d` | distancia | pc | 1 pc = 648 000/π au |
| `τ` | profundidad óptica | adimensional | sintético en esta clase |
| `e` | número de Euler | adimensional | 2,71828… |

## 10. Convenciones y referencias

`log` sin base es decimal en esta clase; `ln` es natural. Las magnitudes de esta clase son **bolométricas** (todas las longitudes de onda); las magnitudes en bandas (V, B…) usan otros cero. La distancia estándar para `M` es 10 pc (S1). El signo de la escala se conserva por convención histórica. Los valores nominales del Sol son factores de conversión, no estimaciones de su valor real (S2).

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | IAU, Resolución B2 de 2015 (magnitudes bolométricas), arXiv:1510.06262 | https://arxiv.org/pdf/1510.06262 | `L₀ = 3,0128 × 10²⁸ W`; `f₀ = 2,518021002 × 10⁻⁸ W/m²`; `M = −2,5 log(L/L₀)`; `m_☉ ≃ −26,832` | Texto leído (extracción de PDF) el 2026-11-05 |
| S2 | IAU, Resolución B3 de 2015 (valores nominales), arXiv:1510.07674 | https://arxiv.org/pdf/1510.07674 | `L_☉ = 3,828 × 10²⁶ W`; `S_☉ = 1361 W/m²` | Texto leído el 2026-11-05 |
| S3 | IERS Conventions (2010), TN36 (tabla de constantes) | https://iers-conventions.obspm.fr/content/tn36.pdf | `1 au = 1,495978707 × 10¹¹ m` | Leída el 2026-11-05 |

Límites: el parsec se toma como `648 000/π` au, definición de la IAU citada en [B01-C02](../../B01/B01-C02-escalas-desde-la-tierra-al-cosmos-observable/CLASE.md) y no releída en esta clase; las cifras de S2 se usan como factores de conversión, no como valores medidos. Los ejemplos de estrellas hipotéticas y la atenuación son **sintéticos**.

## 12. Cómo ver la escala

Tabla de magnitud frente a razón de flujos (equivalente accesible a una gráfica semilogarítmica):

| Diferencia de magnitud `Δm` | Razón de flujos `f₁/f₂ = 10^(0,4 Δm)` |
|---|---|
| 1 | 2,512 |
| 2,5 | 10 |
| 5 | 100 |
| 10 | 10 000 |
| 15 | 1 000 000 |

Descripción larga: en la gráfica de `log f` frente a `m` es una recta de pendiente −0,4; cada 2,5 magnitudes el flujo cambia un orden de magnitud.

## 13. Ejemplo trabajado: ¿coherente el Sol a 1 au?

Datos: `L_☉ = 3,828 × 10²⁶ W`, `L₀ = 3,0128 × 10²⁸ W`, `S_☉ = 1361 W/m²`, `f₀ = 2,518021 × 10⁻⁸ W/m²`, `1 pc = 2,06265 × 10⁵ au`.

**Paso 1 · Magnitud absoluta.** `L_☉/L₀ = 0,012706`; `log₁₀ = −1,8960`; `M = −2,5·(−1,8960) = +4,740`.

**Paso 2 · Magnitud aparente.** `S_☉/f₀ = 1361/2,518021 × 10⁻⁸ = 5,405 × 10¹⁰`; `log₁₀ = 10,7328`; `m = −2,5·10,7328 = −26,832`.

**Paso 3 · Módulo de distancia.** `d = 1 au = 4,848 × 10⁻⁶ pc`; `m − M = 5 log₁₀(4,848 × 10⁻⁷) = 5·(−6,3144) = −31,572`.

**Paso 4 · Comprobar.** `M + (m − M) = 4,740 − 31,572 = −26,832` ✓: la magnitud aparente, la absoluta y la distancia son coherentes entre sí.

**Paso 5 · Comprobación independiente.** El laboratorio calcula `f₀` a partir de `L₀` visto a 10 pc: `2,518021003 × 10⁻⁸ W/m²`, igual al valor publicado en nueve cifras. Resultado con 4 cifras: `M = 4,740`, `m = −26,83`.

## 14. Distintas formas de comparar brillos

El **cociente de flujos** es directo y no tiene signo invertido; sirve cuando solo hay dos objetos. La **magnitud** suma y resta en vez de multiplicar y dividir, y permite tablas largas. El **logaritmo decimal** del flujo (`log f`) es más natural en gráficos científicos modernos. El **módulo de distancia** requiere conocer `M` (luminosidad), y por eso es un método de distancias de la «escalera» (B01-C02). Cada forma es válida si se declara.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Dos fuentes difieren en 5 magnitudes. ¿Cuánto cambia su flujo? Luego, con 2,5 magnitudes. *Pasos:* `f₁/f₂ = 10^(0,4 Δm)`.

<details><summary>Solución comentada</summary>

`Δm = 5` → `10² = 100`. `Δm = 2,5` → `10¹ = 10`. La fuente más débil (magnitud mayor) recibe 1/100 o 1/10 del flujo de la más brillante.
</details>

**Ejercicio 2 · con una pista.** Resuelve `1,03ˣ = 2`. *Pista:* aplica `ln` a ambos lados.

<details><summary>Solución comentada</summary>

`x = ln 2/ln 1,03 = 0,6931/0,02956 = 23,45`. Comprobación: `1,03^23,45 ≈ 2,000`.
</details>

**Ejercicio 3 · casi autónomo.** Una estrella tiene `L = 100 L_☉` y está a 10 pc. Calcula su `M` y su `m`.

<details><summary>Solución comentada</summary>

`M = −2,5 log₁₀(100·3,828 × 10²⁶/3,0128 × 10²⁸) = −2,5 log₁₀(1,2706) = −0,260`. A 10 pc, `m = M = −0,260` (módulo 0). Coincide con el laboratorio (estrella sintética).
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Simplifica `log₁₀(10⁵·10⁻²)` y `log₁₀(1000/10)`.

<details><summary>Solución comentada</summary>

`5 − 2 = 3`; `3 − 1 = 2`. Reglas de la sección 8.1.
</details>

**Ejercicio 5.** La estrella del ejercicio 3 se coloca a 100 pc. Halla `m − M` y `m`. ¿Cuántas veces más débil es?

<details><summary>Solución comentada</summary>

`m − M = 5 log₁₀(100/10) = 5`; `m = −0,260 + 5 = 4,740`. Flujo: `10^(−0,4·5) = 0,01`: cien veces más débil (ley de la inversa del cuadrado: `10² = 100`).
</details>

**Ejercicio 6.** Una fuente tiene `m = 11,0` y otra `m = 6,0`. ¿Cuántas veces es más brillante la segunda?

<details><summary>Solución comentada</summary>

`Δm = 5` → factor 100. La de `m = 6,0`, la de menor número.
</details>

**Ejercicio 7.** Con `m − M = 10`, ¿a qué distancia está el objeto? Despeja `d`.

<details><summary>Solución comentada</summary>

`10 = 5 log₁₀(d/10)` → `log₁₀(d/10) = 2` → `d = 1000 pc`.
</details>

**Ejercicio 8.** Una nube de polvo deja pasar el 60 % de la luz (`I/I₀ = 0,60`). Halla `τ` y la pérdida en magnitudes.

<details><summary>Solución comentada</summary>

`τ = −ln 0,60 = 0,511`; `Δm = 1,0857·0,511 = 0,555` mag (o `−2,5 log₁₀ 0,6 = 0,555`).
</details>

**Ejercicio 9 · transferencia.** Un titular dice: «la estrella A, de magnitud 1, es el doble de brillante que la B, de magnitud 2». Evalúa.

<details><summary>Solución comentada</summary>

`Δm = 1` → factor 2,512, no 2: el titular subestima el cociente en un 20 %. Con `Δm = 5` esa misma intuición diría «cinco veces» cuando son cien. Lo correcto es decir «unas 2,5 veces».
</details>

**Ejercicio 10 · transferencia.** Un compañero calcula la distancia con `m − M = 5 log₁₀ d` (olvida el −5). Con `m − M = 10`, ¿qué error comete?

<details><summary>Solución comentada</summary>

Con la fórmula mal escrita: `d = 10²= 100 pc`; la correcta da 1000 pc. Error de un factor 10, equivalente a olvidar que `d` va en unidades de 10 pc.
</details>

**Ejercicio 11 · transferencia.** Un cometa se desvanece por un factor de 100 en flujo. ¿Cuántas magnitudes? Si luego se multiplica por 10 en distancia con la misma luminosidad, ¿cuántas magnitudes más?

<details><summary>Solución comentada</summary>

Factor 100 → `2,5 log₁₀ 100 = 5` mag. Factor 10 en distancia → flujo `1/100` → otras 5 mag: el módulo cambia `5 log₁₀ 10 = 5`.
</details>

**Ejercicio 12 · integrador.** Elabora tu *tabla magnitud–flujo–distancia con comprobación* (sección 20): elige tres estrellas hipotéticas (rotuladas sintéticas) con distintas `L` y `d`, calcula `M`, `m − M`, `m` y `f`, y comprueba una fila despejando la distancia a partir de `m − M`.

<details><summary>Solución modelo</summary>

Tabla con columnas `L/L_☉`, `M`, `d`, `m − M`, `m`, `f` y la fila de comprobación; fuentes de `L₀`, `f₀` y `L_☉`; una frase que advierta que son sintéticas y bolométricas; verificación de que `L/(4πd²)` coincide con el flujo obtenido de `m`.
</details>

## 17. Laboratorio: comprobar la definición de la IAU

El script [magnitudes_y_logaritmos.py](magnitudes_y_logaritmos.py) calcula magnitudes y antes comprueba: que `f₀` obtenida desde `L₀` a 10 pc coincida con el valor publicado (1 parte en 10⁸), que `M_☉ = 4,74` y `m_☉ = −26,832`, la coherencia `M + (m − M) = m` para el Sol a 1 au, la ida y vuelta de logaritmo y exponencial, y la razón de Pogson.

**Datos:** definiciones publicadas; estrellas sintéticas. **Predice antes de ejecutar:** ¿qué `m` tiene una estrella de 100 `L_☉` a 100 pc? (4,74, igual que el Sol a 10 pc.) **Ejecución del 2026-11-05 (Python 3.12.9):**

```text
f0 calculado desde L0 y 10 pc = 2.518021003e-08 W/m2  (publicado 2.518021002e-08)
M_bol del Sol = 4.7400 mag;  m_bol del Sol = -26.8320 mag
Razón de Pogson 100^(1/5) = 2.511886
   100.00   -0.260    100.0    4.740     3.1993e-10
Extinción: I/I0 = 0.7788;  pérdida = 0.2714 mag (= 1,0857 tau = 0.2714)
Tiempo de duplicación con crecimiento 3 % por periodo: 23.45 periodos
```

```bash
python programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/magnitudes_y_logaritmos.py
```

**Límites:** magnitud bolométrica, sin extinción interestelar ni correcciones bolométricas por banda; las estrellas son sintéticas; no es una herramienta de fotometría.

## 18. Errores frecuentes y cómo corregirlos

**Invertir el signo de la escala.** Se corrige con el ejercicio 6.

**Confundir «5 magnitudes» con «5 veces».** Se corrige con el ejercicio 9.

**Olvidar el −5 del módulo de distancia o usar `d` en au.** Se corrige con el ejercicio 10.

**Aplicar logaritmos a sumas** (`log(x + y) ≠ log x + log y`). Se corrige con la sección 8.1.

**Mezclar bolométrica con banda.** Se corrige leyendo la sección 10.

## 19. Cómo sabrás que vas bien

Tras 8.1: ¿simplificas `log(10⁵·10⁻²)` sin calculadora? Si no, ejercicio 4. Tras 8.3: ¿pasas de `Δm` a razón de flujos? Si no, ejercicio 1. Tras 8.4: ¿obtienes una distancia a partir de `m − M`? Si no, ejercicio 7. Tras el laboratorio: ¿qué comprobación usa una cifra publicada y un cálculo independiente? Si no lo sabes, lee su cabecera.

## 20. Qué entregas y cómo se evalúa

El producto es tu **tabla magnitud–flujo–distancia con comprobación** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Reglas de logaritmo | Errores | Aplica con ayuda | Aplica y simplifica | Cambia de base con soltura |
| Magnitudes | Invierte signo | Convierte parcialmente | Convierte flujo ↔ magnitud | Explica la razón de Pogson |
| Distancia | No usa el módulo | Con error de −5 | Correcto con unidades | Estima la incertidumbre por extinción |
| Comprobación | Ausente | Mental | Cálculo independiente | Compara con valor publicado |
| Fuentes | Sin fuente | Sin fecha | Con localizador y fecha | Rotula sintético y bolométrico |

**Condiciones críticas (no se compensan con promedio):** rotular sintético frente a publicado; declarar que la magnitud es bolométrica; citar solo fuentes consultadas.

## 21. Ética, seguridad y límites

Las escalas logarítmicas comprimen diferencias; presentarlas sin decirlo puede minimizar o exagerar. Aquí la honestidad es declarar que la magnitud es una diferencia de logaritmos. Los valores nominales de la IAU son conversiones, no estimaciones de la física solar. Accesibilidad: fórmulas en texto, tabla equivalente a la gráfica, ejercicios sin conexión.

## 22. Para cerrar y seguir

Un logaritmo convierte cocientes en diferencias; la magnitud usa `−2,5 log₁₀` y el módulo de distancia `5 log₁₀(d/10 pc)`. Una definición publicada se puede comprobar con un cálculo independiente. Queda abierta una pregunta: si la luz atraviesa polvo, ¿cuánto se pierde y cómo se separa de la distancia? Se retoma al estudiar extinción en bloques posteriores. Ahora pasamos a otra herramienta: los ángulos.

**Glosario español–inglés.** exponencial · *exponential*; logaritmo · *logarithm*; magnitud aparente · *apparent magnitude*; magnitud absoluta · *absolute magnitude*; módulo de distancia · *distance modulus*; irradiancia · *irradiance*; luminosidad · *luminosity*; extinción · *extinction*.

**Continuidad.** B04-C06 usa tu capacidad de **trabajar con funciones inversas** para estudiar identidades trigonométricas. B04-C20 retomará el módulo de distancia al comparar con la triangulación.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B04-C04 — Funciones y gráficas](../B04-C04-funciones-y-graficas/CLASE.md) · [📚 Bloque B04](../../../tronco-comun/B04-algebra-trigonometria-y-geometria-espacial.md) · [Siguiente: B04-C06 — Identidades trigonométricas →](../B04-C06-identidades-trigonometricas/CLASE.md)
<!-- /nav -->
