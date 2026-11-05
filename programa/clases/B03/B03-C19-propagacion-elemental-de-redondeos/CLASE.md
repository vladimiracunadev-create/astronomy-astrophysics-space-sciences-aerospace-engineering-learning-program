# B03-C19 — Propagación elemental de redondeos

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B03](../../../tronco-comun/B03-matematica-elemental-para-ciencias-espaciales.md) · [← Anterior: B03-C18 — Razones trigonométricas iniciales](../B03-C18-razones-trigonometricas-iniciales/CLASE.md) · [Siguiente: B03-C20 — Problema integrado de escala del sistema solar →](../B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Decimonovena clase del bloque B03. En C11 aprendiste que redondear al final es mejor que redondear antes. Aquí cuantificas cuánto: cada número que usas tiene un pequeño error de redondeo y, cuando los combinas, esos errores se **propagan** al resultado. Saber cuánto vale el error acumulado te permite decir cuántas cifras del resultado son confiables. Nivel N0 → N1.

Verás la cota de un redondeo, el error absoluto y el relativo, cómo se combinan en sumas, restas, productos y cocientes, la diferencia entre la cota de peor caso y la combinación en cuadratura, la pérdida de cifras al restar números casi iguales y cómo verificar todo con una simulación. No verás estadística completa (B12).

## 2. Por qué esta clase existe

Con los datos de la Tierra redondeados a tres cifras (semieje `1,50 × 10⁸ km` y período `365 d`), la rapidez orbital sale `29,89 km/s`. La NASA publica 29,78 km/s. ¿Te equivocaste? No necesariamente: tus datos solo valen ±0,3 % y ±0,14 %, lo que arrastra al resultado una incertidumbre de ±0,06 a ±0,14 km/s. La discrepancia de 0,11 km/s cae dentro. Sin propagar el error, no sabrías si la diferencia es un fallo o un redondeo.

La decisión central es: **¿cuánto error arrastra mi resultado por culpa de los redondeos de mis datos, y cuántas cifras puedo defender?** Aprenderás dos reglas (peor caso y cuadratura) y a comprobarlas con una simulación.

## 3. Lo que podrás hacer al terminar

1. Dar la cota de redondeo de un dato (±media unidad de su última cifra).
2. Calcular el error absoluto y relativo de un valor.
3. Propagar errores en sumas y restas (absolutos) y en productos y cocientes (relativos).
4. Distinguir la cota de peor caso de la incertidumbre estándar en cuadratura, y usar `a/√3` para una distribución uniforme.
5. Reconocer la pérdida de cifras al restar números casi iguales.
6. Reportar un resultado con su incertidumbre en dos cifras y compararlo con un dato publicado.

La evidencia es el **balance de redondeos e incertidumbre** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

Necesitas C01 a C18. Cinco preguntas:

1. ¿Cuántas cifras significativas tiene `1,50 × 10⁸`?
2. ¿Cuánto es la mitad de `0,01`?
3. ¿Cuánto es `√(3² + 4²)`?
4. ¿Cuánto es el 1 % de 30?
5. Si redondeas `365,256` a `365`, ¿qué error cometes?

<details>
<summary>Ver respuestas</summary>

1. Tres. 2. 0,005. 3. 5. 4. 0,3. 5. 0,256 (0,07 %).
</details>

Con cuatro o cinco aciertos, sigue; con menos, repasa C11.

## 5. Un caso real: ¿está bien la rapidez orbital de la Tierra con datos a tres cifras?

La ficha de la Tierra de la NASA publica un semieje de `149,598 × 10⁶ km`, un período sidéreo de `365,256 d` y una velocidad orbital media de `29,78 km/s` (S1). Si redondeas los dos primeros a tres cifras (`1,50 × 10⁸ km` y `365 d`), la fórmula `v = 2πa/T` da `29,886 km/s`. La cota de peor caso, que considera todos los redondeos en la dirección peor, es `[29,745; 30,027] km/s`; la incertidumbre en cuadratura es `0,062 km/s`. El valor publicado, 29,78 km/s, está dentro del intervalo de peor caso y a `1,7 u` del calculado. Límite: los datos de la NASA son valores medios; aquí solo estudiamos el efecto de **nuestro** redondeo.

## 6. Vocabulario

Un **error de redondeo** es la diferencia entre el valor y su redondeo; su **cota** es el máximo posible: ±media unidad de la última cifra conservada (`365` → ±0,5). El **error absoluto** `Δx` tiene la unidad de `x`; el **error relativo** `Δx/|x|` no tiene unidad. La **propagación** es la transmisión de los errores de los datos al resultado. La **cota de peor caso** supone que todos los errores actúan en la dirección más desfavorable. La **incertidumbre estándar** `u` es la desviación típica asociada; para un valor que puede estar con igual probabilidad en `[x − a, x + a]` (distribución uniforme o rectangular), `u = a/√3` (S2, apdo. 4.3.7). La **incertidumbre combinada** de una función es la combinación de las `u` de sus datos (S2, apdo. 5.1.2). La **cancelación** es la pérdida de cifras significativas al restar dos números casi iguales.

## 7. Modelo mental: el error entra con los datos y sale en el resultado

Los errores de los datos se mezclan según la operación.

```mermaid
flowchart TD
    D1["Dato 1: x ± a₁"] --> O{"Operación"}
    D2["Dato 2: y ± a₂"] --> O
    O -->|"suma o resta"| S["Errores absolutos: a₁ + a₂ (peor caso) o √(a₁² + a₂²) (cuadratura)"]
    O -->|"producto o cociente"| P["Errores relativos: r₁ + r₂ (peor caso) o √(r₁² + r₂²) (cuadratura)"]
    S --> R["Resultado ± incertidumbre, con dos cifras en la incertidumbre"]
    P --> R
```

*Descripción textual:* dos datos con su error entran en una operación; si es suma o resta, se combinan los errores absolutos; si es producto o cociente, los relativos; en ambos casos se puede usar la suma (peor caso) o la raíz de la suma de cuadrados (cuadratura) y el resultado se reporta con su incertidumbre.

Analogía: errar el paso al caminar. Si cada paso se equivoca un poco, tras muchos pasos el error total crece, pero menos que la suma de los peores errores, porque unos se compensan con otros. El límite: la analogía supone errores independientes; si los errores están correlacionados, la compensación no ocurre (B12).

## 8. La explicación, paso a paso

### 8.1 Cota de redondeo

Un número escrito con `n` cifras tiene un error de redondeo de a lo sumo media unidad de su última cifra: `1,50 × 10⁸` → ±`0,005 × 10⁸`; `365` → ±0,5; `365,256` → ±0,0005. Si el dato era exacto (como 1 au en el SI), el error es cero.

### 8.2 Error absoluto y relativo

Si `x = 365 ± 0,5`, el error absoluto es 0,5 d y el relativo `0,5/365 = 0,137 %`. Con `a = 1,50 × 10⁸ ± 0,005 × 10⁸`, el relativo es `0,333 %`. El relativo permite comparar errores de magnitudes distintas.

### 8.3 Suma y resta: se combinan los absolutos

Para `s = x + y` o `x − y`, el error absoluto del peor caso es `Δx + Δy`. Con `1,23 ± 0,005` y `4,5 ± 0,05`, la suma `5,73` tiene cota `0,055`. En cuadratura (con distribución uniforme, `u = a/√3`), la incertidumbre es `√(0,0029² + 0,0289²) = 0,029`.

### 8.4 Producto y cociente: se combinan los relativos

Para `p = xy` o `x/y`, el error relativo del peor caso es `r_x + r_y`. En cuadratura es `√(r_x² + r_y²)` (S2, ecuación 12). Para `v = 2πa/T`, `2π` es exacto (error cero): `r_v = r_a + r_T = 0,333 % + 0,137 % = 0,470 %` en el peor caso. Entonces `Δv = 0,0047 × 29,886 = 0,14 km/s`, con intervalo `[29,745; 30,027]`. En cuadratura: `u_r = √(0,333² + 0,137²)/√3 = 0,208 %`, `u = 0,062 km/s`.

### 8.5 Peor caso o cuadratura

El **peor caso** es una garantía: el valor verdadero está seguro dentro. La **cuadratura** da la dispersión probable: es menor porque no es probable que todos los errores sean máximos y en la misma dirección. Para tres redondeos de ±0,05 sumados, el peor caso es 0,15, y la incertidumbre estándar es `√3 · (0,05/√3) = 0,05`. La cuadratura es válida solo si los errores son independientes.

### 8.6 Cancelación

Al restar números casi iguales, el error absoluto no se reduce pero el valor sí. El perihelio y el afelio terrestres son `147,095` y `152,100` (10⁶ km). Con tres cifras, `147` y `152`: `152 − 147 = 5` con cota `±1` (20 %). Con seis cifras: `5,005 ± 0,001` (0,02 %). Restar pierde cifras: si necesitas una diferencia, necesitas más cifras en los datos.

### 8.7 Cómo reportar

El GUM recomienda dar la incertidumbre con a lo sumo dos cifras significativas y redondear el valor de modo coherente (S2, apdo. 7.2.6). Para nuestra rapidez: `v = 29,89 ± 0,06 km/s` (incertidumbre estándar 0,062 → 0,06; el valor se redondea a la misma posición). Compara con 29,78: la diferencia de 0,11 es `1,7 u`, compatible con el redondeo.

### 8.8 Verificar con una simulación

Un modo independiente de comprobar es **simular**: tomar muchos valores al azar de cada dato dentro de su intervalo y calcular el resultado cada vez. La desviación de los resultados debe coincidir con la fórmula. Con 200 000 muestras, el laboratorio obtiene `0,0622 km/s` (relativa `2,080 × 10⁻³`) frente a la fórmula `0,0622` (relativa `2,081 × 10⁻³`). Los resultados son **sintéticos** (simulados), no mediciones.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor o nota |
|---|---|---|---|
| `Δx` | error absoluto (cota) | la de `x` | ±media unidad de la última cifra |
| `r` | error relativo | sin unidad | `Δx/|x|` |
| `a` | semiancho de un intervalo | la de `x` | — |
| `u` | incertidumbre estándar | la de `x` | uniforme: `a/√3` (S2) |
| `u_r` | incertidumbre relativa | sin unidad | `u/|x|` |
| `a_T` | semieje de la Tierra (redondeado) | km | `1,50 × 10⁸ ± 0,005 × 10⁸` |
| `T` | período (redondeado) | d | `365 ± 0,5` |
| `v` | rapidez orbital media | km/s | calculada 29,89; publicada 29,78 (S1) |

## 10. Convenciones y referencias

Los resultados se dan como `valor ± incertidumbre unidad`. La incertidumbre lleva a lo sumo dos cifras significativas y el valor se redondea a la misma posición (S2). Se declara si la incertidumbre es de peor caso o estándar, y qué distribución se supuso. Los datos simulados se marcan «simulado/sintético».

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA NSSDC, *Earth Fact Sheet* (act. 15-nov-2024) | https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html | Semieje 149,598 × 10⁶ km; período sidéreo 365,256 d; velocidad orbital media 29,78 km/s; perihelio 147,095 y afelio 152,100 (10⁶ km) | Página consultada el 2026-11-05 |
| S2 | JCGM 100:2008, *Evaluation of measurement data – Guide to the expression of uncertainty in measurement* (GUM) | https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf | Apdo. 4.3.7: límites a ± y distribución rectangular, `u² = a²/3`; apdo. 5.1.2, ecuaciones (10)–(12): propagación, incluida la forma relativa para productos; apdo. 7.2.6: dos cifras en la incertidumbre y valor coherente | PDF leído el 2026-11-05 |

Límites: la cota de redondeo (±media unidad) y la suposición de distribución uniforme son modelos de esta clase. Las ecuaciones del GUM se aplican a magnitudes independientes y cuando la función es aproximadamente lineal; no se estudian correlaciones ni funciones fuertemente no lineales. No se consultó el suplemento 1 del GUM (simulación Monte Carlo): la simulación es un control propio.

## 12. Cómo ver el balance

Versión accesible de una tabla de contribuciones.

| Dato | Valor | Cota `a` | Error relativo | Contribución a `v` (peor caso) |
|---|---|---|---|---|
| `a_T` (km) | 1,50 × 10⁸ | 0,005 × 10⁸ | 0,333 % | 0,333 % |
| `T` (d) | 365 | 0,5 | 0,137 % | 0,137 % |
| `2π` | exacto | 0 | 0 | 0 |
| **Total** | `v = 29,886` km/s | — | 0,470 % (peor caso); 0,208 % (estándar) | ±0,14 km/s; ±0,062 km/s |

Si la dibujas, usa barras horizontales con cada contribución y una barra total, rotuladas con valores. Descripción larga: la barra de `a_T` es unas 2,4 veces la de `T`; la total en cuadratura (estándar) es menor que la suma (peor caso).

## 13. Ejemplo trabajado: ¿cuánto vale `v` y con qué incertidumbre?

**Pregunta.** Con `a = 1,50 × 10⁸ ± 0,005 × 10⁸ km` y `T = 365 ± 0,5 d`, ¿cuánto vale `v = 2πa/T` y con qué incertidumbre?

**Paso 1 · valor central.** `v = 2π × 1,50 × 10⁸ km / (365 × 86 400 s) = 9,4248 × 10⁸ km / 3,1536 × 10⁷ s = 29,886 km/s`.
**Paso 2 · errores relativos.** `r_a = 0,005/1,50 = 0,333 %`; `r_T = 0,5/365 = 0,137 %`.
**Paso 3 · peor caso.** `r_v = 0,470 %`; `Δv = 0,14 km/s`; intervalo `[29,745; 30,027]` (se comprueba recalculando con `a` mínima y `T` máxima, y al revés).
**Paso 4 · cuadratura.** `u_r = √(0,333² + 0,137²)/√3 = 0,360/1,732 = 0,208 %`; `u = 0,062 km/s`.
**Paso 5 · reporte.** `v = 29,89 ± 0,06 km/s`.
**Paso 6 · comparación.** La NASA publica 29,78: dentro del peor caso y a `1,7 u` del valor.
**Paso 7 · estimación previa (hecha antes del paso 1).** `2π ≈ 6`; `6 × 1,5 × 10⁸ km ÷ (3,65 × 10² d × 8,64 × 10⁴ s/d) ≈ 9 × 10⁸ ÷ 3,2 × 10⁷ ≈ 28 km/s`: del mismo orden que 29,89 ✓.
**Sentido físico.** Los redondeos de entrada explican la diferencia de 0,11 km/s; no hace falta suponer un error de método.

## 14. Peor caso, cuadratura o simulación: cuándo usar cada uno

El **peor caso** es simple y seguro, pero pesimista. La **cuadratura** es realista si los errores son independientes. La **simulación** sirve cuando la función es complicada, pero exige decidir distribuciones y es más lenta; no sustituye comprender el problema. Todas fallan si los datos están correlacionados (por ejemplo, si `a` y `T` se midieron con el mismo reloj) o si el error de entrada no es pequeño frente al dato.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Da la cota de redondeo de `365`, `1,50 × 10⁸` y `365,256`. *Pasos:* media unidad de la última cifra (8.1).

<details><summary>Solución comentada</summary>

±0,5; ±0,005 × 10⁸ (= ±5 × 10⁵); ±0,0005.
</details>

**Ejercicio 2 · con una pista.** Suma `1,23 ± 0,005` y `4,5 ± 0,05`. Da el resultado con la cota de peor caso. *Pista:* se suman los absolutos.

<details><summary>Solución comentada</summary>

`5,73 ± 0,055`. El dato menos preciso (±0,05) domina.
</details>

**Ejercicio 3 · casi autónomo.** Calcula el error relativo de peor caso de `a = 1,50 × 10⁸ ± 0,005 × 10⁸` y de `T = 365 ± 0,5`. Súmalos.

<details><summary>Solución comentada</summary>

`0,333 %` y `0,137 %`; suma `0,470 %`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Con `v = 29,886 km/s` y el error relativo de peor caso `0,470 %`, calcula la cota absoluta y el intervalo.

<details><summary>Solución comentada</summary>

`0,0047 × 29,886 = 0,14 km/s`; intervalo `[29,75; 30,03]`.
</details>

**Ejercicio 5.** Calcula la incertidumbre estándar en cuadratura de `v` (distribución uniforme).

<details><summary>Solución comentada</summary>

`√(0,333² + 0,137²) = 0,360 %`; entre `√3`: `0,208 %`; `u = 0,062 km/s`.
</details>

**Ejercicio 6.** Calcula `152 − 147` con cota ±0,5 en cada dato. ¿Cuál es el error relativo del resultado? Compáralo con `152,100 − 147,095` (cota ±0,0005).

<details><summary>Solución comentada</summary>

`5 ± 1` (20 %) frente a `5,005 ± 0,001` (0,02 %). Restar cantidades próximas agranda el error relativo.
</details>

**Ejercicio 7.** Reporta `v` con su incertidumbre en dos cifras.

<details><summary>Solución comentada</summary>

`v = 29,89 ± 0,06 km/s`. La incertidumbre 0,062 se redondea a 0,06; el valor, a la misma posición decimal.
</details>

**Ejercicio 8.** Un compañero propaga una suma `x + y` sumando los errores **relativos**. ¿Qué error comete?

<details><summary>Solución comentada</summary>

Para una suma se combinan los errores **absolutos**; los relativos son para productos y cocientes. Con `1,23 ± 0,005` y `4,5 ± 0,05`, sumar relativos (0,41 % + 1,1 %) daría 1,5 % de 5,73 = 0,087, que no es la cota (0,055).
</details>

**Ejercicio 9 · transferencia.** El tiempo de luz Sol–Tierra con `d = 1,50 × 10⁸ ± 0,005 × 10⁸ km` y `c = 3,00 × 10⁵ ± 0,005 × 10⁵ km/s`: calcula `t` y su cota de peor caso, y compárala con 499,005 s (S1/SI).

<details><summary>Solución comentada</summary>

`t = 500 s`; `r = 0,333 % + 0,167 % = 0,5 %`; `Δt = 2,5 s`; intervalo `[497,5; 502,5]`. El valor exacto, 499,005 s, cae dentro.
</details>

**Ejercicio 10 · transferencia.** El período lunar `T = 2πa/v` con `a = 3,84 × 10⁵ ± 0,005 × 10⁵ km` y `v = 1,02 ± 0,005 km/s` (datos redondeados a tres cifras). Calcula `T` en días y el intervalo de peor caso. Compara con 27,3217 d.

<details><summary>Solución comentada</summary>

`T = 27,38 d`; el intervalo (extremos recalculados) es `[27,21; 27,55] d`. El valor publicado 27,3217 está dentro. El error de `v` (0,49 %) domina sobre el de `a` (0,13 %).
</details>

**Ejercicio 11 · transferencia.** ¿Por qué la incertidumbre en cuadratura es menor que la suma de los peores casos?

<details><summary>Solución comentada</summary>

Porque es improbable que todos los errores sean máximos y del mismo signo; unos se compensan. Con tres redondeos de ±0,05, el peor caso es 0,15 y la incertidumbre estándar 0,05. Solo vale si los errores son independientes.
</details>

**Ejercicio 12 · integrador.** Elabora tu *balance de redondeos e incertidumbre* (sección 20) para un cálculo de una clase anterior (por ejemplo C01, C07 o C14): datos redondeados a 3 cifras con sus cotas, errores relativos, peor caso y cuadratura, reporte con dos cifras, comparación con el dato publicado y límites.

<details><summary>Solución modelo</summary>

El ejemplo trabajado con otro cuerpo, p. ej. Marte (`a = 2,28 × 10⁸ ± 0,005 × 10⁸ km`, `T = 687 ± 0,5 d`): `v = 24,1 km/s`, `r = 0,22 % + 0,07 % = 0,29 %`, `Δv = 0,07 km/s`; comparar con el cálculo de C13 (24,13 km/s). Se acepta cualquier cálculo con cotas explícitas y fuente.
</details>

## 17. Laboratorio: propagar y simular

El script [laboratorio_propagacion.py](laboratorio_propagacion.py) calcula la rapidez orbital con los datos redondeados, el intervalo de peor caso, la incertidumbre en cuadratura y una **simulación** (200 000 muestras, semilla fija). Antes comprueba que el valor publicado (29,78 km/s) cae en el peor caso, que la desviación simulada coincide con la fórmula a menos del 2 % y que ninguna muestra sale del peor caso.

**Datos:** publicados (NASA), redondeados a propósito; la simulación es **sintética**. **Predice antes de ejecutar:** ¿qué incertidumbre estándar saldrá? (Algo más de 0,06 km/s.) **Resultados (2026-11-05, Python 3.12.9):** `v = 29,8858 km/s`; peor caso `[29,7454; 30,0265]` (semiancho 0,1406 km/s); cuadratura `u_r = 2,081 × 10⁻³` → `u = 0,0622 km/s`; simulación: media `29,8856`, desviación `0,0622 km/s`; tres redondeos de ±0,05: peor caso 0,150 e incertidumbre estándar 0,050.

```bash
python programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/laboratorio_propagacion.py
```

**Límites:** errores independientes y uniformes; no hay correlaciones; el modelo de redondeo es una idealización.

## 18. Errores frecuentes y cómo corregirlos

**Combinar relativos en una suma.** Ejercicio 8.
**Olvidar que restar casi iguales agranda el error relativo.** Ejercicio 6.
**Dar más cifras que la incertidumbre justifica.** Ejercicio 7.
**Aplicar cuadratura con errores correlacionados.** Sección 14.
**Confundir cota de peor caso con incertidumbre estándar.** Ejercicio 11.

## 19. Cómo sabrás que vas bien

Tras 8.3: ¿sumas errores absolutos en una suma? Si no, repite el ejercicio 2. Tras 8.4: ¿obtienes el error relativo de un producto? Si no, haz el 3. Tras 8.6: ¿explicas la cancelación? Si no, rehaz el 6. Al final: ¿reportas con dos cifras en la incertidumbre? Si dudas, vuelve al 7.

## 20. Qué entregas y cómo se evalúa

El producto es tu **balance de redondeos e incertidumbre**: cotas de los datos, errores relativos, peor caso, cuadratura, reporte con dos cifras, comparación con un dato publicado y límites.

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Cotas de los datos | Ausentes | Algunas | Todas | Distingue exactos de redondeados |
| Propagación | Errores de regla | Con ayuda | Correcta | Compara peor caso y cuadratura |
| Reporte | Sin incertidumbre | Con demasiadas cifras | Dos cifras coherentes | Verifica con simulación |
| Comparación | Sin dato | Sin fuente | Con fuente | Interpreta la diferencia en unidades de `u` |
| Límites | No los menciona | Genéricos | Específicos | Discute correlaciones |

**Condiciones críticas:** no afirmar certeza sin incertidumbre; rotular lo simulado como simulado; citar solo fuentes consultadas.

## 21. Ética, seguridad y límites

Un resultado sin incertidumbre no es un resultado completo. Rotular lo simulado como simulado es honestidad científica. Esta clase es educativa y no sirve para decidir márgenes en una misión. Accesibilidad: fórmulas en texto, tablas equivalentes, sin conexión.

## 22. Para cerrar y seguir

Cada dato redondeado arrastra una cota de media unidad; los absolutos se combinan en sumas y los relativos en productos; el peor caso garantiza y la cuadratura estima; restar casi iguales pierde cifras; y se reporta con dos cifras en la incertidumbre. Queda una pregunta: ¿puedes juntar todo lo que sabes en un único problema de ingeniería con requisitos y comprobaciones? Es C20.

**Glosario español–inglés.** error de redondeo · *rounding error*; cota · *bound*; error relativo · *relative error*; propagación · *propagation*; incertidumbre estándar · *standard uncertainty*; distribución uniforme · *uniform distribution*; cancelación · *cancellation*.

**Continuidad.** B03-C20 usa este balance para verificar la maqueta. B12 trata la incertidumbre con rigor estadístico y B13 la metrología.

**Referencias:** ver sección 11. Todas las fuentes son datos oficiales consultados.

<!-- nav:bottom -->
---

[← Anterior: B03-C18 — Razones trigonométricas iniciales](../B03-C18-razones-trigonometricas-iniciales/CLASE.md) · [📚 Bloque B03](../../../tronco-comun/B03-matematica-elemental-para-ciencias-espaciales.md) · [Siguiente: B03-C20 — Problema integrado de escala del sistema solar →](../B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md)
<!-- /nav -->
