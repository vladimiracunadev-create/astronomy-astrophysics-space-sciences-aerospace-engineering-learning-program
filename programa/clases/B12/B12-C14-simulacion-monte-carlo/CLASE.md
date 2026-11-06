# B12-C14 — Simulación Monte Carlo

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B12](../../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) · [← Anterior: B12-C13 — Cadenas de Markov y muestreo](../B12-C13-cadenas-de-markov-y-muestreo/CLASE.md) · [Siguiente: B12-C15 — Muestreo de importancia →](../B12-C15-muestreo-de-importancia/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Decimocuarta clase del bloque B12. Ya usaste simulaciones para verificar fórmulas; aquí las conviertes en un método de cálculo: estimar probabilidades, integrales e incertidumbres de salida **generando muestras** del modelo, y cuantificar el error de la propia simulación. Nivel N3. Ejemplo conductor: la probabilidad de que dos objetos pasen a menos de una distancia dada. No verás aún la técnica para sucesos raros (C15) ni la propagación formal GUM–JCGM 101 (C16).

## 2. Por qué esta clase existe

Casi ningún modelo de misión admite una fórmula cerrada para la incertidumbre de su salida: hay no linealidades, restricciones y combinaciones de entradas. La simulación Monte Carlo reemplaza el álgebra por repetición: se sortean entradas, se evalúa el modelo y se resume la salida. Es potente y general, pero produce **estimaciones con error**, y ese error hay que medirlo y reportarlo.

Pregunta motivadora: **¿cuántas simulaciones hacen falta para estimar una probabilidad con una precisión dada, y cómo sé que el resultado no es un accidente de la semilla?** Decisión central: **el número de muestras y el criterio para aceptar el resultado**.

## 3. Lo que podrás hacer al terminar

1. Estimar una probabilidad y una integral con muestras aleatorias.
2. Calcular el error típico de la estimación (`√(p(1−p)/N)`) y un intervalo para ella.
3. Predecir el número de muestras para una precisión relativa dada.
4. Explicar la tasa `1/√N` y su costo.
5. Validar un código de simulación contra una solución exacta y registrar semilla y versiones.
6. Reconocer cuándo el método simple es insuficiente (sucesos raros, alto costo).

La evidencia es el **informe de simulación** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

Necesitas C03 (normal), C04 (varianza), C06 (promedios) y C08 (error típico). Cinco preguntas:

1. ¿Cuál es la varianza de una variable de Bernoulli con probabilidad `p`?
2. ¿Qué desviación tiene el promedio de `N` datos de varianza `σ²`?
3. ¿Cuánto vale `1 − e^{−0,125}`?
4. ¿Qué es una distribución de Rayleigh? (pista: la distancia de un punto normal 2D al origen).
5. ¿Qué es una semilla?

<details>
<summary>Ver respuestas</summary>

1. `p(1−p)`. 2. `σ/√N`. 3. `0,1175`. 4. La distribución de `√(X² + Y²)` con `X, Y` normales independientes de igual `σ`. 5. El valor que inicializa un generador pseudoaleatorio y hace reproducible la secuencia.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa C03, C04 y C06.

## 5. Un caso: la distancia de paso entre dos objetos

En el plano perpendicular al movimiento relativo de dos objetos **ilustrativos**, el error de posición relativa tiene componentes `x` e `y` independientes, normales de media cero y desviación `σ = 100 m`. ¿Con qué probabilidad la distancia de paso queda por debajo de `R = 50 m`? Es el **ejemplo conductor**, con solución exacta para validar el código: la distancia sigue una Rayleigh y `P(d < R) = 1 − e^{−R²/(2σ²)} = 0,117503`. Todos los valores son **sintéticos**; no es un análisis de colisión real.

## 6. Vocabulario

La **simulación Monte Carlo** estima una cantidad como el promedio de una función de muestras aleatorias generadas con un modelo; el suplemento 1 del GUM (JCGM 101) la describe como un método de propagación de distribuciones (S1). El **estimador de una probabilidad** es la frecuencia `p̂ = (aciertos)/N`; su error típico es `√(p(1−p)/N)`. Un **generador pseudoaleatorio** produce una secuencia determinista que imita el azar; fijar su **semilla** hace reproducible la simulación (S1 advierte que los resultados válidos requieren un generador adecuado). El **error de Monte Carlo** es la variabilidad del resultado debida solo al número finito de muestras. Un procedimiento **adaptativo** aumenta el número de pruebas hasta que los resultados se estabilizan en un sentido estadístico (S1, 7.9). La **precisión relativa** es el error típico dividido por el valor de la cantidad.

## 7. Modelo mental: contar impactos al azar para medir un área

Si lanzas dardos al azar sobre una diana de área conocida y cuentas la fracción que cae en una zona, estimas el área de la zona. Cuantos más dardos, mejor, pero con rendimiento decreciente: para dividir el error por 10 hay que lanzar 100 veces más.

```mermaid
flowchart LR
    A["Modelo +<br/>distribución de entradas"] --> B["Sortear N entradas<br/>(semilla fija)"]
    B --> C["Evaluar el modelo"]
    C --> D["Resumir: media,<br/>frecuencia, percentiles"]
    D --> E["Error típico ∝ 1/√N"]
    E -->|"¿suficiente?"| F["Reportar con error,<br/>semilla y versiones"]
    E -->|"no"| B
```

*Descripción textual:* se sortean entradas del modelo, se evalúa la salida, se resume y se calcula el error de la propia simulación; si es demasiado grande, se aumenta `N`; al final se reporta el resultado con su error, la semilla y las versiones.

Analogía: encuestar a una muestra aleatoria de la población; el margen de error baja como `1/√N`. Su límite: la encuesta (la simulación) solo es tan buena como el modelo de la población (las distribuciones de entrada).

## 8. La explicación, paso a paso

### 8.1 Estimar una probabilidad

Con `N = 10³, 10⁴, 10⁵, 10⁶` muestras, las estimaciones de `P(d < 50 m)` son `0,142000`, `0,115000`, `0,118200` y `0,117291`, frente al valor exacto `0,117503`. Los errores `+0,0245`, `−0,0025`, `+0,0007`, `−0,0002` caben dentro de 4 errores típicos teóricos (`0,0102`; `0,0032`; `0,0010`; `0,00032`). Con 1000 muestras, el resultado puede errar en un 20 % relativo; con un millón, en `0,3 %`.

### 8.2 El error de la simulación

El error típico de `p̂` es `√(p(1−p)/N)`. Se verifica repitiendo la simulación 400 veces con `N = 10 000`: la desviación observada es `0,003020` frente a la teórica `0,003220` (6 % de diferencia, dentro de lo esperado para 400 réplicas). Un intervalo aproximado para un resultado con `N = 1000` y `p̂ = 0,142` es `0,142 ± 1,96·√(0,142·0,858/1000) = 0,142 ± 0,022`, es decir `[0,120; 0,164]`: **no** contiene el valor exacto `0,1175`. Es el 1,6 % de casos en que una estimación cae a más de 2,4 errores típicos; con una sola corrida no se distingue de un fallo del código, y por eso se valida contra una solución exacta y con réplicas.

### 8.3 La ley `1/√N`

El error baja como `1/√N`: cien veces más muestras para diez veces menos error. Para un error relativo del 1 % en `p = 0,1175` se necesitan `N = (1−p)/(p·0,01²) ≈ 75 100` muestras. Para un suceso con `p = 10⁻⁶`, el mismo requisito exige `10⁸` (C15).

### 8.4 Integrales por Monte Carlo

`∫₀^π sin x dx = 2`. Se estima como `π · media(sin Xᵢ)` con `Xᵢ` uniformes en `[0, π]`. Con `N = 1000`: `1,99115` (error típico teórico `0,0306`); con `N = 10⁵`: `2,00217` (teórico `0,0031`). La varianza de `sin(πU)` es `1/2 − (2/π)² = 0,0947`, lo que da el error típico teórico. La ventaja del método aparece en muchas dimensiones, donde las rejillas se vuelven inviables, porque su error no depende de la dimensión.

### 8.5 Cuántas muestras: una regla práctica

El suplemento 1 del GUM indica que un valor `M = 10⁶` suele dar un intervalo de cobertura del 95 % con una o dos cifras decimales significativas correctas, y recomienda elegir `M` mucho mayor que `1/(1−p)` (al menos `10⁴` veces mayor) para describir bien los extremos del intervalo (S1, 7.2). También propone un procedimiento adaptativo que detiene la simulación cuando los resultados se estabilizan (S1, 7.9). Es una regla de partida; siempre se comprueba la estabilidad rehaciendo con otra semilla.

### 8.6 Reproducibilidad y límites

Un resultado de Monte Carlo debe poder repetirse: se declaran la semilla, el generador, el número de muestras y las versiones de las bibliotecas. Los límites: (i) el resultado es tan bueno como las distribuciones de entrada; (ii) para sucesos raros el método simple necesita muchas muestras; (iii) con un modelo costoso, `10⁶` evaluaciones pueden ser inviables.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Nota |
|---|---|---|---|
| `x, y` | componentes del error de posición | m | `N(0; 100 m)` |
| `d` | distancia de paso | m | `√(x² + y²)` |
| `R` | umbral | m | 50 |
| `p` | probabilidad exacta | adimensional | `0,117503` |
| `p̂` | estimación | adimensional | |
| `N` | número de muestras | adimensional | |
| `SE` | error típico de Monte Carlo | adimensional | `√(p(1−p)/N)` |
| `σ` | desviación de cada componente | m | 100 |

## 10. Convenciones y referencias

La semilla de este laboratorio es 1414 (generador por defecto de NumPy, PCG64). Los errores se reportan como estimado menos exacto. El plano de encuentro es el perpendicular a la velocidad relativa. Distancias en metros.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Consulta |
|---|---|---|---|---|
| S1 | JCGM 101:2008, *Supplement 1 to the GUM: Propagation of distributions using a Monte Carlo method* | https://doi.org/10.59161/JCGM101-2008; PDF de bipm.org | `M = 10⁶` como valor habitual (7.2.1, nota); `M` mucho mayor que `1/(1−p)` (7.2.2); procedimiento adaptativo (7.2.3, 7.9); validez estadística exige un buen generador (nota de 7.4) | 2026-11-05, PDF abierto y texto extraído |

Límites: la distribución de Rayleigh, el error `√(p(1−p)/N)` y la tasa `1/√N` son resultados estándar no atribuidos a una fuente consultada; los datos son **sintéticos** y el escenario, ilustrativo.

## 12. Cómo ver la convergencia

Equivalente accesible a un gráfico del error contra `N` (resultados del laboratorio):

| `N` | `p̂` | Error | Error típico teórico |
|---|---|---|---|
| 1 000 | 0,142000 | +0,024497 | 0,010183 |
| 10 000 | 0,115000 | −0,002503 | 0,003220 |
| 100 000 | 0,118200 | +0,000697 | 0,001018 |
| 1 000 000 | 0,117291 | −0,000212 | 0,000322 |

Descripción larga: en un gráfico logarítmico, el error absoluto cae como una recta de pendiente −1/2 en `N`, con fluctuaciones por encima y por debajo de cero; el primer punto (`N = 1000`) cae a 2,4 errores típicos, un valor posible pero poco frecuente.

## 13. Ejemplo trabajado: ¿qué precisión necesito?

**Paso 1 · Modelo.** Componentes normales independientes, `σ = 100 m`, umbral `50 m`.

**Paso 2 · Objetivo.** Conocer `p` con un error relativo del 1 %.

**Paso 3 · Tamaño.** `N = (1−p)/(p·10⁻⁴) ≈ 75 100` muestras (con `p` conocido de antemano; en la práctica se usa una estimación piloto).

**Paso 4 · Ejecución.** Con `N = 10⁵`: `p̂ = 0,118200`, error típico teórico `0,0010` (0,87 % relativo).

**Paso 5 · Comprobación.** Con `N = 10⁶`: `0,117291`; ambas estimaciones están dentro de sus errores típicos y entre sí.

**Paso 6 · Reporte.** `p = 0,1182 ± 0,0010` con 10⁵ muestras, semilla 1414, NumPy 2.4.4.

**Paso 7 · Sentido.** Valor exacto conocido solo en este problema didáctico. Datos **sintéticos**.

## 14. Comparación de métodos

La **fórmula cerrada** es exacta pero solo existe en casos simples. La **cuadratura/rejilla** es precisa en pocas dimensiones y se vuelve inviable en muchas. **Monte Carlo** es general y su error no depende de la dimensión, pero converge despacio. Las **variantes** (muestreo por importancia C15, estratificado, cuasi-Monte Carlo) reducen la varianza a cambio de complejidad. Para pocas entradas y un modelo casi lineal, la ley de propagación del GUM (C16) es más barata.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula el error típico de `p̂` con `N = 10 000` y `p = 0,1175`. *Pasos:* `p(1−p)`, dividir, raíz.

<details><summary>Solución comentada</summary>

`0,1175·0,8825 = 0,1037`; `/10⁴ = 1,037 × 10⁻⁵`; raíz `0,00322`.
</details>

**Ejercicio 2 · con una pista.** Con `N = 1000` y `p̂ = 0,142`, calcula un intervalo del 95 %. *Pista:* use `p̂` en el error típico.

<details><summary>Solución comentada</summary>

`SE = √(0,142·0,858/1000) = 0,01104`; `0,142 ± 0,0216 = [0,120; 0,164]`. No contiene `0,1175` (`0,1175 < 0,120`): con esta semilla la estimación quedó a 2,4 errores típicos del exacto, lo que ocurre ~1,6 % de las veces.
</details>

**Ejercicio 3 · casi autónomo.** Calcula la `P(d < 100 m)` exacta para el mismo modelo.

<details><summary>Solución comentada</summary>

`1 − e^{−100²/(2·100²)} = 1 − e^{−0,5} = 0,3935`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** ¿Cuántas muestras para estimar `∫ sin` con error típico `0,001`? (`SE = 0,967/√N`).

<details><summary>Solución comentada</summary>

`N = (0,967/0,001)² ≈ 935 000`.
</details>

**Ejercicio 5.** Si con `N = 10 000` el error es `0,0032`, ¿qué `N` da `0,00032`?

<details><summary>Solución comentada</summary>

Diez veces menos error exige 100 veces más muestras: `10⁶`.
</details>

**Ejercicio 6.** ¿Cuántas muestras exige estimar `p = 10⁻⁶` con 10 % de error relativo?

<details><summary>Solución comentada</summary>

`N = (1−p)/(p·0,1²) ≈ 10⁸`. Motiva el muestreo por importancia (C15).
</details>

**Ejercicio 7.** ¿Qué registras para que otra persona repita tu simulación?

<details><summary>Solución comentada</summary>

Semilla, generador, `N`, versiones de Python y bibliotecas, modelo y distribuciones de entrada con sus parámetros y unidades, y el criterio de estabilidad.
</details>

**Ejercicio 8.** ¿Por qué la precisión de Monte Carlo no depende de la dimensión del problema?

<details><summary>Solución comentada</summary>

El error típico es `σ_f/√N`, con `σ_f` la desviación de la función evaluada; no aparece la dimensión. (Sin embargo `σ_f` puede crecer con la dimensión y el modelo puede ser más caro.)
</details>

**Ejercicio 9 · transferencia.** Un subsistema suma tres cargas independientes, cada una uniforme entre 8 y 12 W. Calcula exactamente `P(total > 33 W)` y plantea cómo lo estimarías por Monte Carlo.

<details><summary>Solución comentada</summary>

Con `S′ = (S − 24)/4`, suma de tres uniformes en `[0,1]`; `P(S > 33) = P(S′ > 2,25) = P(S′ < 0,75) = 0,75³/6 = 0,0703` (por simetría). Monte Carlo: sortear tres cargas, sumar y contar la fracción por encima de 33; con `N = 10⁶` el error típico es `0,00025`.
</details>

**Ejercicio 10 · transferencia.** ¿Por qué un procedimiento adaptativo es preferible a fijar `M = 10⁶` a ciegas?

<details><summary>Solución comentada</summary>

Porque la cantidad de muestras necesaria depende de la forma de la distribución de salida y de la probabilidad de cobertura; se detiene cuando los resultados se estabilizan en un sentido estadístico (S1, 7.2.3 y 7.9), ahorrando cómputo o evitando quedarse corto.
</details>

**Ejercicio 11 · transferencia.** Dos personas obtienen `0,1182` y `0,1173` con semillas distintas y `N = 10⁵`. ¿Hay desacuerdo?

<details><summary>Solución comentada</summary>

No: la diferencia `0,0009` es menor que el error típico de la diferencia `√2 · 0,0010 = 0,0014`. Son consistentes con el mismo valor.
</details>

**Ejercicio 12 · integrador.** Elabora tu *informe de simulación*: elige un problema con solución exacta (probabilidad o integral), estima con cuatro valores de `N`, tabula error y error típico teórico, verifica la ley `1/√N` con réplicas y reporta semilla, versiones y número de muestras para una precisión dada.

<details><summary>Solución modelo</summary>

Tabla de `N`, estimación, error y error típico; réplicas (≥ 200) que confirman la desviación teórica; conclusión sobre el `N` necesario; registro de reproducibilidad; límites (modelo ilustrativo, sin colisiones reales); datos rotulados como sintéticos.
</details>

## 17. Laboratorio: error de Monte Carlo

El script [monte_carlo_error.py](monte_carlo_error.py) estima `P(d < 50 m)` con cuatro tamaños de muestra, verifica que cada error cae dentro de 4 errores típicos, mide la desviación del estimador con 400 réplicas, estima la integral de `sin` y calcula el `N` necesario para 1 % de precisión; falla si algún criterio no se cumple.

**Datos:** sintéticos. **Predice antes de ejecutar:** ¿qué `N` hace falta para un error relativo del 1 %? (≈ 75 000.) **Ejecución del 2026-11-06 (Python 3.12.9, NumPy 2.4.4):**

```text
P(d < 50 m) exacta (Rayleigh) = 0.117503
       N    estimacion   error      desv. teorica sqrt(p(1-p)/N)
    1000    0.142000   +0.024497   0.010183
   10000    0.115000   -0.002503   0.003220
  100000    0.118200   +0.000697   0.001018
 1000000    0.117291   -0.000212   0.000322
N=10000: desviacion observada de 400 replicas = 0.003020; teorica = 0.003220
cada 100 veces mas muestras reducen el error 10 veces: 10x
integral N=  1000: 1.99115 (exacta 2); desv. teorica 0.03057
integral N=100000: 2.00217 (exacta 2); desv. teorica 0.00306
muestras para error relativo de 1 % en p = 0.1175: N = 75,104
Pruebas superadas.
```

```bash
python programa/clases/B12/B12-C14-simulacion-monte-carlo/monte_carlo_error.py
```

**Límites:** modelo didáctico; resultados **simulados**.

## 18. Errores frecuentes y cómo corregirlos

**Reportar una estimación sin su error de Monte Carlo.** Se corrige con 8.2.

**Pensar que más muestras corrigen un modelo equivocado.** Se corrige con 8.6.

**No registrar la semilla.** Se corrige con el ejercicio 7.

**Esperar convergencia rápida.** Se corrige con 8.3 y el ejercicio 5.

**Usar Monte Carlo simple para sucesos raros.** Se corrige con el ejercicio 6.

## 19. Cómo sabrás que vas bien

Tras 8.2: ¿calculas el error típico de una estimación? Si no, ejercicio 1. Tras 8.3: ¿estimas el `N` para otra precisión? Si no, ejercicio 6. Tras 8.6: ¿qué registras para repetir tu corrida? Si dudas, ejercicio 7.

## 20. Qué entregas y cómo se evalúa

El producto es tu **informe de simulación** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Modelo y entradas | Ambiguos | Declarados | Con unidades y fuentes | Con sensibilidad |
| Estimación | Sin error | Con error sin teoría | Con error teórico verificado | Con intervalo de cobertura |
| Validación | Ninguna | Compara un valor | Compara varios `N` | Con réplicas |
| Reproducibilidad | Sin semilla | Con semilla | Semilla y versiones | Registro completo |
| Fuentes y rótulo | Ausente | Parcial | Sintético y fuente | Declara validez |

**Condiciones críticas (no se compensan con promedio):** reportar el error de Monte Carlo; declarar semilla y versiones; rotular datos sintéticos.

## 21. Ética, seguridad y límites

Un resultado de simulación con modelo o entradas inadecuados genera falsa confianza; en seguridad espacial, una probabilidad de paso calculada con incertidumbres mal modeladas puede llevar a omitir o a ejecutar maniobras innecesarias. Ningún resultado de esta clase es operativo. Accesibilidad: los gráficos se ofrecen como tabla; todo funciona sin conexión.

## 22. Para cerrar y seguir

Monte Carlo estima probabilidades e integrales con muestras; su error baja como `1/√N`; el resultado se reporta con ese error, la semilla y las versiones; el método simple es ineficiente para sucesos raros. Queda abierta una pregunta: ¿cómo estimar bien una probabilidad de `10⁻⁶` sin gastar `10⁸` muestras? Con muestreo de importancia (C15).

**Glosario español–inglés.** Monte Carlo · *Monte Carlo*; semilla · *seed*; generador pseudoaleatorio · *pseudo-random number generator*; error de Monte Carlo · *Monte Carlo error*; distribución de Rayleigh · *Rayleigh distribution*; procedimiento adaptativo · *adaptive procedure*.

**Continuidad.** B12-C15 reutiliza tu capacidad de **calcular el error de una estimación** para reducir la varianza en sucesos raros.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B12-C13 — Cadenas de Markov y muestreo](../B12-C13-cadenas-de-markov-y-muestreo/CLASE.md) · [📚 Bloque B12](../../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) · [Siguiente: B12-C15 — Muestreo de importancia →](../B12-C15-muestreo-de-importancia/CLASE.md)
<!-- /nav -->
