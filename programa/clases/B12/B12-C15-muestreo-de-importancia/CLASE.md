# B12-C15 — Muestreo de importancia

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B12](../../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) · [← Anterior: B12-C14 — Simulación Monte Carlo](../B12-C14-simulacion-monte-carlo/CLASE.md) · [Siguiente: B12-C16 — Propagación de incertidumbre →](../B12-C16-propagacion-de-incertidumbre/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Decimoquinta clase del bloque B12. En [C14](../B12-C14-simulacion-monte-carlo/CLASE.md) viste que estimar una probabilidad de `10⁻⁶` con Monte Carlo simple exige unos `10⁸` ensayos. Esta clase enseña a **sortear donde importa** y a corregir con pesos, para estimar sucesos raros con muchas menos muestras. Nivel N3. Verás la fórmula, la elección de la propuesta, el tamaño muestral efectivo y los modos de fallo. No verás aquí las variantes adaptativas ni el muestreo por subconjuntos.

## 2. Por qué esta clase existe

Los sucesos que más interesan en seguridad espacial —un error de aproximación fuera de límites, una falla simultánea, una colisión— son raros por diseño. Un Monte Carlo simple puede pasar millones de ensayos sin ver un solo acierto y reportar «cero», que no es una estimación útil. El muestreo de importancia dirige el cómputo a la región rara y la compensa matemáticamente.

Pregunta motivadora: **¿cómo estimar con precisión `P(Z > 4)` sin gastar millones de ensayos, y cómo sé que la corrección es válida?** Decisión central: **qué propuesta usar y cómo comprobar que no engaña**.

## 3. Lo que podrás hacer al terminar

1. Enunciar la identidad `E_p[h(X)] = E_q[h(X) w(X)]` con `w = p/q`.
2. Calcular los pesos para una propuesta normal desplazada.
3. Estimar un suceso raro y su error típico con muestreo de importancia.
4. Calcular el tamaño muestral efectivo y la reducción de varianza.
5. Identificar una propuesta inadecuada (mal centrada o con colas livianas).
6. Validar el estimador contra una solución exacta.

La evidencia es el **informe de suceso raro** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

Necesitas C03 (normal), C14 (error de Monte Carlo) y la esperanza de una función (C04). Cinco preguntas:

1. ¿Cuál es el error relativo de Monte Carlo simple para `p` pequeña y `N` muestras?
2. ¿Qué vale `P(|Z| < 2)`?
3. ¿Qué es una densidad de probabilidad?
4. ¿Qué vale `E[1{X > 4}]`?
5. ¿Qué pasa con la media de variables de varianza infinita?

<details>
<summary>Ver respuestas</summary>

1. `≈ 1/√(Np)`. 2. `0,9545`. 3. Una función no negativa con área 1. 4. `P(X > 4)`. 5. No se estabiliza (C06).
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa C03, C04 y C14.

## 5. Un caso: un error de aproximación de 4 sigmas

El error normalizado `Z ~ N(0,1)` de una maniobra de aproximación (**ilustrativo**) debe quedar bajo `4`. ¿Cuál es la probabilidad de que lo supere? El valor exacto es `P(Z > 4) = ½ erfc(4/√2) = 3,167 × 10⁻⁵` (sirve para validar). Con 100 000 sorteos simples se espera ver 3 aciertos; en la corrida del laboratorio aparecieron 5 y la estimación fue `5,0 × 10⁻⁵`, un 58 % de error. Es el **ejemplo conductor**; los datos son **sintéticos**.

## 6. Vocabulario

El **muestreo de importancia** estima `E_p[h(X)]` sorteando de otra densidad `q` (la **propuesta**) y ponderando cada muestra por el **peso** `w(x) = p(x)/q(x)`: `E_p[h] = ∫ h p dx = ∫ h (p/q) q dx = E_q[h w]`. El estimador es `(1/N) Σ h(Xᵢ) w(Xᵢ)` con `Xᵢ ~ q`. Es **insesgado** si `q > 0` donde `h p ≠ 0`. La **varianza** del estimador depende de la propuesta; es mínima cuando `q ∝ |h| p`. El **tamaño muestral efectivo** `ESS = (Σ hᵢwᵢ)²/Σ (hᵢwᵢ)²` mide a cuántas muestras iguales equivale el conjunto ponderado; es `N` si todos los pesos son iguales y vale 1 si uno solo domina. Un **suceso raro** tiene probabilidad muy pequeña. El suplemento 1 del GUM recomienda, para describir bien los extremos de un intervalo de cobertura con Monte Carlo, un número de pruebas muy grande frente a `1/(1−p)` (S1, 7.2.2), lo que da la medida de por qué los extremos de la distribución cuestan caros con muestreo simple.

## 7. Modelo mental: sortear en la cola y pagar con pesos

El Monte Carlo simple reparte las muestras como la distribución: casi todas en el centro, donde no pasa nada. El de importancia las lleva a la región rara, pero así sobrerrepresenta esa región; los pesos (muy pequeños allí) deshacen el exceso.

```mermaid
flowchart LR
    A["Objetivo p(x)<br/>(suceso raro en la cola)"] --> B["Elegir propuesta q(x)<br/>con masa en la cola"]
    B --> C["Sortear Xᵢ ~ q"]
    C --> D["Peso wᵢ = p(Xᵢ)/q(Xᵢ)"]
    D --> E["Estimador:<br/>media de 1{Xᵢ en suceso}·wᵢ"]
    E --> F["Error típico<br/>y ESS"]
```

*Descripción textual:* se elige una propuesta con masa en la región rara; se sortea de ella; cada muestra recibe el peso `p/q`; el estimador es la media del indicador del suceso por el peso; se calcula su error típico y el tamaño muestral efectivo.

Analogía: encuestar con más preguntas a una minoría poco frecuente y luego reponderar para representar a la población. Su límite: si olvidas a un subgrupo relevante en la encuesta, la reponderación no puede inventarlo.

## 8. La explicación, paso a paso

### 8.1 La identidad

`P(Z > 4) = ∫ 1{x > 4} φ(x) dx`, con `φ` la densidad normal estándar. Con propuesta `q = N(4, 1)`, el cociente es `w(x) = φ(x)/φ(x − 4) = exp(−x²/2 + (x−4)²/2) = exp(−4x + 8)`. Entonces `P = E_q[1{X > 4} e^{−4X+8}]`. Para `x = 4,5`, `w = e^{−10} = 4,5 × 10⁻⁵`: las muestras que caen lejos en la cola pesan muy poco, y las cercanas al umbral más.

### 8.2 Resultado en el caso conductor

Con 100 000 muestras de `N(4,1)`: estimación `3,1510 × 10⁻⁵ ± 2,1 × 10⁻⁷` (error típico estimado desde la propia muestra), a `0,5 %` del exacto `3,1671 × 10⁻⁵`, es decir, a `0,8` errores típicos. El Monte Carlo simple con las mismas muestras dio `5,0 × 10⁻⁵` (error relativo teórico `56 %`). La razón de varianzas es `7 035`: igualar la precisión con muestreo simple exigiría unos `7 × 10⁸` sorteos. El `ESS` ponderado es `18 070` de `100 000`.

### 8.3 Una propuesta mal centrada

Con `q = N(2, 1)` el peso es `e^{−2x+2}`. Solo 2 273 de 100 000 muestras caen por encima de 4, así que casi todo el cómputo se desperdicia: estimación `3,19 × 10⁻⁵ ± 7,3 × 10⁻⁷`, `ESS = 1 873` (0,10 del caso anterior). Con `q = N(3,1)`: `3,2164 × 10⁻⁵ ± 3,1 × 10⁻⁷`, también correcta pero menos eficiente que `N(4,1)`. Una buena propuesta tiene masa justo donde está la integranda `h p`; centrarla en el umbral es un punto de partida razonable para colas gaussianas.

### 8.4 Cuándo falla

(i) **Colas livianas**: si `q` decae más rápido que `p` en la región de interés, los pesos crecen sin límite y la varianza del estimador es infinita; la estimación parece estable y luego salta. (ii) **Cobertura incompleta**: si `q` no cubre una región donde `h p ≠ 0`, el estimador es sesgado y no hay aviso. (iii) **Dimensión alta**: los pesos tienden a degenerarse, un solo peso domina y el `ESS` cae. Hay que mirar siempre la distribución de los pesos y el `ESS`.

### 8.5 Error típico estimado

El error típico se calcula con la desviación de los términos `hᵢwᵢ` entre `√N`: `2,1 × 10⁻⁷` aquí. Se compara con el error de Monte Carlo simple `√(p(1−p)/N) = 1,8 × 10⁻⁵` para el mismo `N`: unas 85 veces menor. Como en C14, se debe verificar con réplicas o con una solución exacta cuando existe.

### 8.6 Cuando no hay solución exacta

Se comparan dos propuestas distintas: si ambas coinciden dentro de sus errores típicos (como `N(4,1)` y `N(3,1)` aquí: `3,15` y `3,22 × 10⁻⁵`, diferencia `0,07 × 10⁻⁵` frente a errores de `0,02` y `0,03 × 10⁻⁵`, que son consistentes a ~2 errores típicos), la estimación es creíble; si discrepan, algo falla. Esta verificación cruzada es la defensa práctica cuando se desconoce el valor exacto.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Nota |
|---|---|---|---|
| `p(x)`, `q(x)` | densidades objetivo y propuesta | inversa de `x` | normal estándar y desplazada |
| `w(x)` | peso `p/q` | adimensional | `exp(−4x + 8)` |
| `h(x)` | función a promediar | adimensional | `1{x > 4}` |
| `N` | muestras | adimensional | `10⁵` |
| `ESS` | tamaño muestral efectivo | adimensional | `18 070` |
| `P` | probabilidad del suceso | adimensional | `3,167 × 10⁻⁵` |
| `Z` | error normalizado | adimensional | `(error)/σ` |

## 10. Convenciones y referencias

Se estima la cola superior `P(Z > 4)`; la simétrica es igual. El umbral está en desviaciones típicas. La semilla es 1515. Los pesos se calculan en forma estable (exponencial de un exponente). Todos los números son **sintéticos**.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Consulta |
|---|---|---|---|---|
| S1 | JCGM 101:2008 (Suplemento 1 del GUM) | https://doi.org/10.59161/JCGM101-2008 | Recomendación de un `M` muy grande frente a `1/(1−p)` para describir los extremos de un intervalo de cobertura (7.2.2) | 2026-11-05, PDF abierto y texto extraído |

Límites: la identidad del muestreo de importancia, la expresión de los pesos, el `ESS` y los modos de fallo son resultados estándar no atribuidos a una fuente consultada; el valor exacto `3,167 × 10⁻⁵` se calcula con `erfc` del módulo estándar; el escenario es **ilustrativo** y los datos, **sintéticos**.

## 12. Cómo ver los pesos

Equivalente accesible a un histograma de pesos, en tabla (cálculo propio):

| `x` | `w(x) = e^{−4x+8}` |
|---|---|
| 4,0 | 1 |
| 4,5 | 4,5 × 10⁻⁵ |
| 5,0 | 6,1 × 10⁻⁶ |
| 6,0 | 1,1 × 10⁻⁷ |

Descripción larga: los pesos caen exponencialmente al alejarse del umbral; las muestras de `N(4,1)` que superan 4 tienen pesos desde 1 hacia abajo, de modo que el estimador depende sobre todo de las que están cerca del umbral. Las muestras por debajo de 4 reciben peso pero no cuentan (indicador 0).

## 13. Ejemplo trabajado: estimar `P(Z > 4)` con 10⁵ sorteos

**Paso 1 · Objetivo y suceso.** `P(Z > 4)`, con valor exacto de referencia `3,167 × 10⁻⁵`.

**Paso 2 · Propuesta.** `N(4,1)`, pesos `e^{−4x+8}`.

**Paso 3 · Sorteo.** `N = 100 000` muestras.

**Paso 4 · Estimador.** Media de `1{xᵢ > 4} e^{−4xᵢ+8}`: `3,1510 × 10⁻⁵`.

**Paso 5 · Error.** `2,1 × 10⁻⁷` desde la muestra; la diferencia con el exacto es `1,6 × 10⁻⁷`, menor que un error típico.

**Paso 6 · Comparación.** Monte Carlo simple: 5 aciertos, `5,0 × 10⁻⁵`; reducción de varianza `7 035`.

**Paso 7 · Verificación cruzada.** `N(3,1)` da `3,2164 × 10⁻⁵ ± 3,1 × 10⁻⁷`: consistente. Todo **simulado**, datos **sintéticos**.

## 14. Comparación de métodos

**Monte Carlo simple**: sin diseño, pero inviable para sucesos raros. **Muestreo de importancia**: gran ahorro si la propuesta es buena, riesgo de varianza infinita si no. **Estratificación** y **cuasi-Monte Carlo**: reducen varianza sin cambiar la distribución. **Aproximaciones analíticas** (como la normal de cola): rápidas pero dependen de supuestos. **Métodos de subconjuntos** y secuenciales: para dimensiones altas. La elección depende de lo que se sabe de la región de falla.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Para `p = N(0,1)` y `q = N(4,1)`, calcula `w(4,5)`. *Pasos:* `w = exp(−4x + 8)`.

<details><summary>Solución comentada</summary>

`exp(−18 + 8) = e^{−10} = 4,54 × 10⁻⁵`.
</details>

**Ejercicio 2 · con una pista.** Para `q = N(3,1)` deduce el peso. *Pista:* `φ(x)/φ(x − 3) = exp(−x²/2 + (x−3)²/2)`.

<details><summary>Solución comentada</summary>

`exp(−3x + 4,5)`. En `x = 4`: `e^{−7,5} = 5,53 × 10⁻⁴`.
</details>

**Ejercicio 3 · casi autónomo.** Con `q = N(4,1)` se sortean `x = 4,2; 4,5; 3,9`. Calcula el estimador de `P(Z > 4)` con esas tres muestras.

<details><summary>Solución comentada</summary>

Aportes: `e^{−8,8} = 1,51 × 10⁻⁴`; `e^{−10} = 4,5 × 10⁻⁵`; `3,9` no supera 4: 0. Promedio: `1,96 × 10⁻⁴/3 = 6,5 × 10⁻⁵`. Con tres muestras la estimación es ruidosa; sirve para ver el mecanismo.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** ¿Cuál es el error relativo teórico del Monte Carlo simple con `N = 10⁶` para `p = 3,167 × 10⁻⁵`?

<details><summary>Solución comentada</summary>

`√((1−p)/(pN)) = √(1/31,67) = 0,178` (18 %).
</details>

**Ejercicio 5.** ¿Cuántas muestras exige el Monte Carlo simple para 10 % de error relativo en ese `p`?

<details><summary>Solución comentada</summary>

`N = (1−p)/(p·0,01) ≈ 3,16 × 10⁶`.
</details>

**Ejercicio 6.** Calcula el `ESS` de los pesos `[1; 1; 1; 1]` y de `[4; 0; 0; 0]`.

<details><summary>Solución comentada</summary>

`(Σ)²/Σ²`: `16/4 = 4` y `16/16 = 1`. Pesos iguales: `ESS = N`; un solo peso domina: `ESS = 1`.
</details>

**Ejercicio 7.** Si la reducción de varianza es `7 035`, ¿cuántas muestras de Monte Carlo simple igualan `10⁵` de importancia?

<details><summary>Solución comentada</summary>

`10⁵ · 7 035 ≈ 7 × 10⁸`.
</details>

**Ejercicio 8.** ¿Por qué los pesos de `N(4,1)` caen muy rápido cuando `x` crece más allá de 4?

<details><summary>Solución comentada</summary>

El peso es `e^{−4x+8}`: decrece exponencialmente porque la propuesta `N(4,1)` pone más masa que `p` a la derecha de 4 y hay que quitarla.
</details>

**Ejercicio 9 · transferencia.** La suma de 4 errores independientes `N(0,1)` es `N(0, 2²)`. ¿Cuál es `P(S > 8)`?

<details><summary>Solución comentada</summary>

`P(S > 8) = P(Z > 4) = 3,167 × 10⁻⁵`: es el mismo problema reescalado. Se muestrea `S` con una propuesta centrada en 8 y desviación 2.
</details>

**Ejercicio 10 · transferencia.** Si la falla ocurre con `|Z| > 4` (dos colas), ¿qué sucede si solo sorteas de `N(4,1)`?

<details><summary>Solución comentada</summary>

Cubres solo la cola derecha: estimas la mitad (`3,167 × 10⁻⁵` en vez de `6,334 × 10⁻⁵`), sin aviso. Se corrige con una mezcla de propuestas `½N(4,1) + ½N(−4,1)` o duplicando por simetría. Es el fallo (ii) de 8.4.
</details>

**Ejercicio 11 · transferencia.** Un colega usa la propuesta `N(4, 0,1)` (muy estrecha) y obtiene una estimación estable. ¿Qué cuidados tomas?

<details><summary>Solución comentada</summary>

Los pesos `exp(−x²/2 + (x−4)²/(2·0,01))·0,1` crecen enormemente lejos del centro de la propuesta (colas livianas): la varianza puede ser infinita aunque pocos sorteos lo muestren. Se examinan los pesos máximos, el `ESS` y se compara con otra propuesta más ancha.
</details>

**Ejercicio 12 · integrador.** Elabora tu *informe de suceso raro*: elige un suceso `P(Z > k)` con `k` entre 3 y 5, estima con Monte Carlo simple y con muestreo de importancia (dos propuestas), tabula estimación, error típico, `ESS` y reducción de varianza, y valida con el valor exacto (`erfc`).

<details><summary>Solución modelo</summary>

Tabla por método con estimación, error típico y `ESS`; comparación con el exacto; reducción de varianza; discusión de una propuesta inadecuada; verificación cruzada; semilla y versiones; datos rotulados como sintéticos; advertencias sobre colas livianas y cobertura.
</details>

## 17. Laboratorio: suceso raro con y sin importancia

El script [muestreo_importancia.py](muestreo_importancia.py) estima `P(Z > 4)` con Monte Carlo simple, con `N(4,1)`, con `N(2,1)` y con `N(3,1)`; falla si la estimación de importancia se aparta más de 4 errores típicos del valor exacto, si la reducción de varianza no supera 100 o si la propuesta mal centrada no tiene `ESS` bajo.

**Datos:** sintéticos. **Predice antes de ejecutar:** ¿cuántos aciertos verá el Monte Carlo simple con 100 000 sorteos? (≈ 3.) **Ejecución del 2026-11-06 (Python 3.12.9, NumPy 2.4.4, SciPy 1.17.1):**

```text
P(Z > 4) exacta = 3.167124e-05
MC simple N=100000: aciertos = 5; estimacion = 5.000e-05; error relativo teorico = 0.56
IS q=N(4,1):    estimacion = 3.1510e-05 +/- 2.1e-07; error relativo = 0.508%
reduccion de varianza (MC simple / IS) = 7,035
tamano muestral efectivo (solo pesos >0): 18,070 de 100000
IS q=N(2,1): estimacion = 3.1887e-05 +/- 7.3e-07; muestras en la region = 2273; ESS = 1,873 (0.10 del bueno)
IS q=N(3,1):   estimacion = 3.2164e-05 +/- 3.1e-07
Pruebas superadas.
```

```bash
python programa/clases/B12/B12-C15-muestreo-de-importancia/muestreo_importancia.py
```

**Límites:** una dimensión, pesos analíticos; resultados **simulados**.

## 18. Errores frecuentes y cómo corregirlos

**Olvidar los pesos.** El estimador sin pesos estima otra probabilidad; se corrige con 8.1.

**Propuesta con colas livianas.** Se corrige con 8.4 y el ejercicio 11.

**Cobertura incompleta del suceso.** Se corrige con el ejercicio 10.

**Fiarse de un error típico sin mirar los pesos.** Se corrige con 8.4–8.5 y el ejercicio 6.

**No verificar con una solución exacta o una segunda propuesta.** Se corrige con 8.6.

## 19. Cómo sabrás que vas bien

Tras 8.1: ¿derivas el peso para otra propuesta? Si no, ejercicio 2. Tras 8.2: ¿interpretas `7 035`? Si no, ejercicio 7. Tras 8.4: ¿reconoces el riesgo de colas livianas? Si no, ejercicio 11.

## 20. Qué entregas y cómo se evalúa

El producto es tu **informe de suceso raro** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Pesos | Ausentes o erróneos | Correctos con ayuda | Correctos y estables | Para varias propuestas |
| Estimación y error | Sin error | Con error | Con error y `ESS` | Con réplicas |
| Validación | Ninguna | Con exacto | Con exacto y verificación cruzada | Analiza fallos |
| Propuesta | Arbitraria | Justificada | Justificada y comparada | Mezcla defensiva |
| Fuentes y rótulo | Ausente | Parcial | Sintético y fuente | Declara validez |

**Condiciones críticas (no se compensan con promedio):** incluir los pesos; verificar contra una referencia; rotular datos sintéticos.

## 21. Ética, seguridad y límites

Estimar una probabilidad de falla con una propuesta que omite regiones de falla subestima el riesgo sin aviso. Ningún resultado de esta clase es una evaluación de riesgo real ni una probabilidad de colisión. Accesibilidad: los histogramas se ofrecen como tabla; todo funciona sin conexión.

## 22. Para cerrar y seguir

El muestreo de importancia sortea de una propuesta con masa en la región rara y corrige con pesos `p/q`; con una buena propuesta reduce la varianza en órdenes de magnitud, pero con colas livianas o cobertura incompleta engaña sin avisar; se vigilan el `ESS` y se verifica con una referencia. Queda abierta una pregunta: ¿cómo se propaga la incertidumbre de varias entradas a una salida de forma sistemática? Es la propagación de incertidumbre (C16).

**Glosario español–inglés.** muestreo de importancia · *importance sampling*; propuesta · *proposal distribution*; peso · *weight*; tamaño muestral efectivo · *effective sample size*; suceso raro · *rare event*; reducción de varianza · *variance reduction*; cola · *tail*.

**Continuidad.** B12-C16 reutiliza tu capacidad de **simular y estimar con error** para validar la propagación de incertidumbre.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B12-C14 — Simulación Monte Carlo](../B12-C14-simulacion-monte-carlo/CLASE.md) · [📚 Bloque B12](../../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) · [Siguiente: B12-C16 — Propagación de incertidumbre →](../B12-C16-propagacion-de-incertidumbre/CLASE.md)
<!-- /nav -->
