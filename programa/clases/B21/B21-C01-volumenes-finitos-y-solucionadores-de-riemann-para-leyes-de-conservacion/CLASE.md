# B21-C01 — Volúmenes finitos y solucionadores de Riemann para leyes de conservación

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B21](../../../tronco-comun/B21-metodos-numericos-para-edp-y-fluidos-computacionales.md) · [← Anterior: B20-C04 — Redacción de un artículo científico](../../../tronco-comun/B20-metodologia-de-la-investigacion-cientifica.md#b20-c04) · [Siguiente: B21-C02 — Ecuación de onda: esquemas y dispersión numérica →](../B21-C02-ecuacion-de-onda-esquemas-y-dispersion-numerica/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Primera clase del bloque B21 y puerta de entrada a la simulación de fluidos y plasmas compresibles. En el bloque B11 aprendiste a avanzar en el tiempo una ecuación diferencial ordinaria (por ejemplo, en [B11-C05](../../B11/B11-C05-metodo-de-euler/CLASE.md) el método de Euler); aquí avanzas en el tiempo **una cantidad que además varía en el espacio** y que se conserva. Nivel N3. Verás cómo escribir un esquema que no pierda ni cree masa, momento ni energía (volúmenes finitos), cómo se calcula el flujo entre dos celdas con un solucionador de Riemann aproximado (Rusanov y HLL) y cómo comprobar el resultado contra una solución exacta. No verás esquemas de segundo orden ni limitadores, la ecuación de magnetohidrodinámica completa, ni la teoría general de ondas no lineales: son continuación natural de este tema.

Las clases B11-C13 (ecuaciones en derivadas parciales) y B11-C14 (diferencias finitas) están programadas, pero **todavía no están redactadas**; por eso esta clase define lo que usa y no depende de ellas.

## 2. Por qué esta clase existe

Casi todo lo que fluye en el espacio —el viento solar, el gas de un disco de acreción, el gas que rodea a una nave en reentrada, la onda de choque de una eyección coronal— obedece **leyes de conservación**: una cantidad cambia en una región solo porque entra o sale por sus bordes. Si un programa traduce mal esa idea, produce masa de la nada o choques en el lugar equivocado, y lo hace sin avisar. Los códigos astrofísicos de referencia, como Athena (S1), están construidos sobre este mismo principio.

La pregunta motivadora: **¿cómo se calcula cuánta masa, momento y energía cruza la frontera entre dos celdas cuando a cada lado el gas está en un estado distinto, y cómo se sabe que el resultado es correcto?** La decisión central: **qué flujo numérico usar en cada interfaz, y con qué paso de tiempo**.

## 3. Lo que podrás hacer al terminar

1. Escribir una ley de conservación `q_t + f(q)_x = 0` e identificar el vector de estado y el flujo de las ecuaciones de Euler.
2. Deducir y aplicar a mano la actualización de volúmenes finitos y comprobar que conserva.
3. Calcular el flujo en una interfaz con los métodos de Rusanov y HLL.
4. Acotar el paso de tiempo con la condición CFL.
5. Verificar un esquema contra una solución exacta (advección y tubo de choque de Sod) y medir su orden.
6. Explicar por qué el esquema de primer orden difunde discontinuidades y qué mejoraría el de orden superior.

La evidencia es el **informe de verificación del solucionador** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

Necesitas la idea de derivada parcial (B09) y el cálculo del orden observado de [B11-C05](../../B11/B11-C05-metodo-de-euler/CLASE.md). Cinco preguntas:

1. ¿Qué mide `∂q/∂x` y qué mide `∂q/∂t`?
2. Si una cantidad pasa por una puerta a razón `F` (por segundo) y sale por otra a razón `F′`, ¿cómo cambia la cantidad dentro?
3. ¿Cuánto es `log₂(0,8/0,4)`?
4. Una cantidad `q` tiene densidad `ρ` y velocidad `u`: ¿cuánto vale su flujo de masa `ρu` si `ρ = 2` y `u = 3`?
5. ¿Qué es el error global de un método y cómo se mide su orden?

<details>
<summary>Ver respuestas</summary>

1. La rapidez de cambio con la posición y con el tiempo, respectivamente. 2. Cambia a razón `F − F′` (lo que entra menos lo que sale). 3. `1`. 4. `6`. 5. La diferencia acumulada con la solución exacta; el orden `p` se estima como `log₂(E(h)/E(h/2))`.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa B09 y B11-C05.

## 5. Un caso real: un choque en un tubo, como modelo de una onda de choque

Imagina un tubo largo dividido por una membrana. A la izquierda el gas está denso y a presión alta; a la derecha, enrarecido y a presión baja. Se rompe la membrana. Lo que ocurre a continuación es el **tubo de choque de Sod**, un problema de prueba clásico: una onda de rarefacción viaja hacia la izquierda, una onda de choque hacia la derecha y, entre ambas, una superficie de contacto separa los dos gases originales. Es un modelo mínimo de lo que ocurre cuando una onda de choque interplanetaria barre el viento solar más lento.

Usaremos números **sintéticos y adimensionales**: a la izquierda `ρ = 1`, `u = 0`, `p = 1`; a la derecha `ρ = 0,125`, `u = 0`, `p = 0,1`; razón de calores específicos `γ = 1,4`; tubo de longitud 1 con la membrana en `x = 0,5`. Ninguna cifra de esta clase es una medición del viento solar: el modelo solo conserva su estructura de ondas. Este es el **ejemplo conductor**.

## 6. Vocabulario

Una **ley de conservación** es una ecuación `q_t + f(q)_x = 0` que dice que la cantidad `q` solo cambia por el flujo `f(q)` en las fronteras. El **vector de estado conservado** agrupa las cantidades que se conservan. El **flujo** es cuánto de cada cantidad cruza un punto por unidad de tiempo. Una **celda** es un tramo de longitud `Δx` del dominio; el **promedio de celda** `q_i` es el valor medio de `q` en ella. La **interfaz** `i+½` es el borde entre las celdas `i` e `i+1`. El **flujo numérico** `F_{i+½}` es la aproximación del flujo en esa interfaz. Un **problema de Riemann** es el problema de valor inicial con dos estados constantes separados por una discontinuidad. Un **solucionador de Riemann** calcula (exacta o aproximadamente) la solución de ese problema para obtener el flujo. La **condición CFL** (de Courant, Friedrichs y Lewy) limita el paso de tiempo para que la información no cruce más de una celda por paso. Una **onda de choque** es una discontinuidad que se propaga con compresión irreversible; una **onda de rarefacción** es una expansión continua; la **discontinuidad de contacto** separa dos gases con distinta densidad pero igual presión y velocidad.

## 7. Modelo mental: contabilidad de cajas

Piensa cada celda como una caja con un contador de masa, otro de momento y otro de energía. Entre una caja y la siguiente hay una puerta. Cada paso de tiempo, la puerta deja pasar cierta cantidad hacia un lado y esa misma cantidad **sale** de una caja y **entra** en la otra. Si cada puerta registra un único movimiento y se resta de un lado lo que se suma en el otro, el total en todas las cajas no puede cambiar salvo por las puertas de los extremos.

```mermaid
flowchart LR
    A["Promedios de celda<br/>q_i en el tiempo n"] --> B["Estados a izquierda y derecha<br/>de cada interfaz"]
    B --> C["Solucionador de Riemann<br/>flujo F_{i+½}"]
    C --> D["Actualización<br/>q_i − (Δt/Δx)(F_{i+½} − F_{i−½})"]
    D --> E["Nuevo tiempo n+1<br/>con paso Δt de la CFL"]
    E -->|"repetir"| A
```

*Descripción textual:* se parte de los promedios de celda; en cada interfaz se toman los estados de ambos lados; el solucionador de Riemann entrega el flujo en esa interfaz; cada celda se actualiza restando el flujo que sale y sumando el que entra; el paso de tiempo viene de la condición CFL y el ciclo se repite.

Analogía: la contabilidad de partida doble, donde cada traspaso se anota en las dos cuentas. Su límite: en contabilidad, el traspaso no tiene física detrás; en un fluido, **cuánto** pasa lo decide la dinámica de ondas entre las dos celdas, y ahí está la dificultad.

## 8. La explicación, paso a paso

### 8.1 Leyes de conservación y ecuaciones de Euler

Para una sola variable, `q(x, t)`, la ley de conservación es `∂q/∂t + ∂f(q)/∂x = 0`. Si integras en una celda `[x_{i−½}, x_{i+½}]`, el término del flujo se convierte en la diferencia de flujos en los dos bordes: es la contabilidad de cajas, escrita con símbolos.

Para un gas ideal en una dimensión, las **ecuaciones de Euler** (el límite de las de Navier–Stokes sin viscosidad; S2) tienen tres variables conservadas: la densidad de masa `ρ`, la de momento `ρu` y la de energía total `E`, con

`q = (ρ, ρu, E)`, `f(q) = (ρu, ρu² + p, u(E + p))`, `E = p/(γ − 1) + ½ρu²`,

donde `u` es la velocidad, `p` la presión y `γ` la razón de calores específicos (1,4 para aire). La **velocidad del sonido** es `c = √(γp/ρ)`. Las ondas del sistema viajan a las velocidades `u − c`, `u` y `u + c`. Que Euler sea la versión sin viscosidad de Navier–Stokes lo respalda S2.

### 8.2 De la caja a la fórmula

Si el promedio de celda es `q_i^n` en el instante `t_n`, la actualización de volúmenes finitos es

`q_i^{n+1} = q_i^n − (Δt/Δx)(F_{i+½} − F_{i−½})`.

Es la misma forma que la ecuación (31) del código Athena (S1), con flujos promediados en el tiempo. Suma sobre todas las celdas: los flujos interiores aparecen una vez con signo `+` y otra con `−`, y se cancelan. Solo sobreviven los flujos de los extremos. **Eso** es conservación discreta, y vale para cualquier flujo numérico que use el mismo valor en la interfaz para las dos celdas vecinas.

### 8.3 El flujo más simple: contracorriente

Para la advección `q_t + a q_x = 0` con `a > 0`, la información viene de la izquierda y el flujo numérico es `F_{i+½} = a q_i` (esquema **contracorriente** o *upwind*). La actualización queda `q_i^{n+1} = q_i − ν(q_i − q_{i−1})` con `ν = aΔt/Δx` el **número de Courant**. Es estable para `0 < ν ≤ 1` y de primer orden. Con `ν = 1` copia el valor de la celda vecina y el resultado es exacto.

### 8.4 El problema de Riemann y el flujo en Euler

En cada interfaz hay un salto entre el estado izquierdo `q_L` y el derecho `q_R`. Si se dejara evolucionar solo ese salto, aparecerían las ondas de la sección 5. **Godunov** propuso tomar como flujo numérico el flujo exacto en la posición de la interfaz. Resolver el problema de Riemann exacto en cada interfaz y en cada paso es caro; por eso se usan **solucionadores aproximados**.

### 8.5 Rusanov y HLL

Los dos usan únicamente estimaciones de las velocidades de onda extremas.

**Rusanov** (flujo de Lax–Friedrichs local):

`F = ½[f(q_L) + f(q_R)] − ½ s_max (q_R − q_L)`, con `s_max = máx(|u_L| + c_L, |u_R| + c_R)`.

Es el promedio de los flujos de ambos lados menos un término que difunde, proporcional al salto.

**HLL** (Harten–Lax–van Leer): con `S_L = mín(u_L − c_L, u_R − c_R)` y `S_R = máx(u_L + c_L, u_R + c_R)`, se definen `b⁻ = mín(S_L, 0)` y `b⁺ = máx(S_R, 0)`, y

`F = [b⁺ f(q_L) − b⁻ f(q_R)]/(b⁺ − b⁻) + [b⁺ b⁻/(b⁺ − b⁻)] (q_R − q_L)`.

Esa es la forma de la ecuación (52) de Athena (S1), con las velocidades de onda (53–54) que allí se calculan con la matriz de Roe; esta clase usa las estimaciones más simples `S_L` y `S_R` de arriba, que son una elección distinta y por eso los números no son los de ese código. HLL supone una sola región intermedia entre las ondas extremas, por lo que ignora la discontinuidad de contacto y la difunde (S1 lo señala; para MHD ignora además las ondas de Alfvén y las lentas).

En magnetohidrodinámica el mismo esqueleto sirve: cambia el vector de estado y, en las velocidades extremas, el sonido `c` se sustituye por la velocidad magnetosónica rápida (S1). La estructura —volúmenes finitos, flujo en la interfaz, CFL— no cambia.

### 8.6 Paso de tiempo: CFL

La actualización de una celda solo usa a sus vecinas inmediatas. Si en un paso la información física viaja más que una celda, el esquema no la ve. Por eso `Δt = C Δx / máx(|u| + c)`, con `C ≤ 1` (S1 usa esta forma en la ecuación 34 con el valor extremo sobre todas las celdas). Aquí `C = 0,8`. Como el máximo depende del estado, el paso se recalcula en cada instante.

### 8.7 Orden y difusión

Un esquema de primer orden como los anteriores es el de «seguir la tangente a ciegas» del [método de Euler](../../B11/B11-C05-metodo-de-euler/CLASE.md): su error de truncamiento actúa como una **difusión numérica** que redondea los frentes. Eso estabiliza (no hay oscilaciones) pero emborrona las discontinuidades. Los esquemas modernos reconstruyen una pendiente dentro de cada celda y combinan el flujo con un integrador de orden 2 (S1 usa reconstrucción de orden superior); están fuera del alcance de esta clase.

## 9. Magnitudes, símbolos y unidades

Para un gas real las unidades son SI; el modelo del laboratorio es **adimensional** (los números son proporciones, no tienen unidad física).

| Símbolo | Qué es | Unidad (SI) | Nota |
|---|---|---|---|
| `x, t` | posición, tiempo | m, s | adimensionales en el laboratorio |
| `q` | vector de estado conservado | por m³ | `(ρ, ρu, E)` |
| `ρ` | densidad | kg m⁻³ | |
| `u` | velocidad | m s⁻¹ | |
| `p` | presión | Pa | |
| `E` | energía total por volumen | J m⁻³ | `p/(γ−1) + ½ρu²` |
| `γ` | razón de calores específicos | — | 1,4 en el laboratorio |
| `c` | velocidad del sonido | m s⁻¹ | `√(γp/ρ)` |
| `f(q)` | flujo | por m² por s | `(ρu, ρu²+p, u(E+p))` |
| `Δx, Δt` | ancho de celda, paso de tiempo | m, s | |
| `ν` | número de Courant | — | `aΔt/Δx` |
| `F_{i+½}` | flujo numérico | como `f` | |

## 10. Convenciones y referencias

Malla uniforme con celdas centradas en `x_i = (i + ½)Δx`; índice `i` aumenta hacia la derecha; frontera transmisiva (se copia el valor de la celda extrema). «Estado izquierdo» y «derecho» se refieren a los lados de la interfaz. En el laboratorio, el primer orden se aplica con `q_L = q_i` y `q_R = q_{i+1}`.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | Stone, Gardiner, Teuben, Hawley y Simon, «Athena: a new code for astrophysical MHD» (preprint, 2008) | arXiv:0804.0402, https://arxiv.org/pdf/0804.0402 | Actualización de volúmenes finitos (ec. 31), flujo HLLE (ec. 52–54), paso de tiempo por CFL (ec. 34); uso de la velocidad magnetosónica rápida en MHD | Texto extraído del PDF (versión 1 de arXiv) el 2026-11-05; se cita el preprint por su identificador, sin dato de revista |
| S2 | NASA Glenn, *Euler Equations* (Beginner's Guide to Aeronautics) | https://www.grc.nasa.gov/www/k-12/airplane/eulereqs.html | Las ecuaciones de Euler son la versión sin viscosidad de Navier–Stokes y un conjunto de EDP acopladas | Consultada el 2026-11-05 mediante extracción automática |

Límites: la forma de los flujos de Euler, la velocidad del sonido, las fórmulas de Rusanov y HLL con las estimaciones `S_L`, `S_R` simples y la solución exacta del problema de Riemann son resultados estándar que **no se atribuyen a una fuente consultada**; su validez se comprueba aquí con el laboratorio, que verifica los estados `p*` y `u*` contra los valores tabulados ampliamente (`0,30313` y `0,92745`) y la conservación. Los datos del tubo de Sod son **sintéticos**.

## 12. Cómo ver el choque

Equivalente accesible a una gráfica de la densidad en `t = 0,2` (cálculo propio; posiciones de las ondas con la solución exacta):

| Elemento | Posición `x` | Densidad |
|---|---|---|
| Cabeza de la rarefacción | `0,2634` | `1` (estado izquierdo) |
| Cola de la rarefacción | `0,4859` | `0,4263` |
| Superficie de contacto | `0,6855` | salta de `0,4263` a `0,2656` |
| Choque | `0,8504` | salta de `0,2656` a `0,125` |

Descripción larga: de izquierda a derecha, la densidad es constante en 1, desciende suavemente a través de la rarefacción hasta 0,4263, se mantiene casi plana hasta el contacto, baja bruscamente a 0,2656, permanece plana hasta el choque y vuelve de golpe a 0,125. Con HLL y 400 celdas, el choque se ve casi nítido (pocas celdas de ancho) y el contacto se ve más ancho.

## 13. Ejemplo trabajado: un flujo en la membrana y un paso de tiempo

**Paso 1 · Estados.** Con `γ = 1,4`: a la izquierda `q_L = (1, 0, 2,5)` porque `E = 1/0,4 = 2,5`; a la derecha `q_R = (0,125, 0, 0,25)`. Los flujos son `f(q_L) = (0, 1, 0)` y `f(q_R) = (0, 0,1, 0)`.

**Paso 2 · Velocidades del sonido.** `c_L = √1,4 = 1,18322` y `c_R = √(1,4·0,1/0,125) = 1,05830`.

**Paso 3 · Velocidades extremas.** `S_L = mín(−1,18322, −1,05830) = −1,18322` y `S_R = 1,18322`; luego `b⁻ = −1,18322` y `b⁺ = 1,18322`.

**Paso 4 · Flujo HLL.** Con `b⁺ − b⁻ = 2,36644` y `b⁺b⁻ = −1,4`:

masa: `(0 − 0)/2,36644 + (−1,4/2,36644)(0,125 − 1) = 0,51766`;
momento: `(1,18322·1 + 1,18322·0,1)/2,36644 = 0,55`;
energía: `(−1,4/2,36644)(0,25 − 2,5) = 1,33112`.

**Paso 5 · Rusanov.** Con `s_max = 1,18322` da lo mismo en este caso, porque las velocidades extremas son simétricas.

**Paso 6 · Paso de tiempo.** Con `N = 100` celdas, `Δx = 0,01` y `C = 0,8`: `Δt = 0,8·0,01/1,18322 = 0,006761`, así que `Δt/Δx = 0,6761`.

**Paso 7 · Actualización.** La celda izquierda de la membrana pasa a `ρ = 1 − 0,6761·(0,51766 − 0) = 0,65000`, `ρu = 0 − 0,6761·(0,55 − 1) = 0,30426` y `E = 2,5 − 0,6761·1,33112 = 1,60000`. La derecha, a `ρ = 0,125 − 0,6761·(0 − 0,51766) = 0,47500`, `ρu = 0,30426` y `E = 0,25 + 0,6761·1,33112 = 1,15000`.

**Paso 8 · Comprobación.** La masa que salió de la izquierda (`0,35000`) es la que entró a la derecha (`0,35000`); el momento y la energía también se conservan en el par. Al recuperar las variables físicas, la celda izquierda queda con `u = 0,46809` y `p = 0,6115` (la presión cayó de 1 a 0,61) y la derecha con `u = 0,6406` y `p = 0,4210` (subió de 0,1 a 0,42). Es la señal del primer paso de las ondas. Todo es **simulado**, con datos sintéticos.

## 14. Comparación de métodos

Con 400 celdas, el error L1 de la densidad (promedio del valor absoluto de la diferencia con la solución exacta) fue `1,03 × 10⁻²` con Rusanov y `6,75 × 10⁻³` con HLL; HLL gana en los tres tamaños de malla probados. Para la advección suave de una onda senoidal, el contracorriente tiene error que baja a la mitad al duplicar las celdas (orden 1). El flujo exacto de Godunov costaría iterar en cada interfaz, mientras HLL y Rusanov usan fórmulas cerradas. En cambio, un esquema de orden 2 con limitadores reduciría el emborronamiento de los frentes con una malla más gruesa; es el tema de un curso posterior y no se desarrolla aquí.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Aplica el esquema contracorriente a la advección con `ν = 0,8` y celdas `q = (0, 1, 1, 0)` (la celda a la izquierda del grupo vale 0). Calcula los nuevos valores de las cuatro celdas y comprueba la suma. *Pasos:* regla `q_i − ν(q_i − q_{i−1})` (8.3), valores nuevos, suma antes y después.

<details><summary>Solución comentada</summary>

La primera celda: `0 − 0,8(0 − 0) = 0`. La segunda: `1 − 0,8(1 − 0) = 0,2`. La tercera: `1 − 0,8(1 − 1) = 1`. La cuarta: `0 − 0,8(0 − 1) = 0,8`. Suma antes: `2`; después: `0 + 0,2 + 1 + 0,8 = 2`. Se conserva porque cada celda recibe de su vecina exactamente lo que ésta cede.
</details>

**Ejercicio 2 · con una pista.** Calcula el vector de estado y el flujo de Euler para `ρ = 2`, `u = 3`, `p = 1` con `γ = 1,4`. *Pista:* primero `E`.

<details><summary>Solución comentada</summary>

`E = 1/0,4 + ½·2·9 = 2,5 + 9 = 11,5`. `q = (2, 6, 11,5)`. Flujo: `(ρu, ρu² + p, u(E + p)) = (6, 18 + 1, 3·12,5) = (6, 19, 37,5)`.
</details>

**Ejercicio 3 · casi autónomo.** Calcula el flujo de Rusanov en la membrana de Sod y compáralo con el de HLL (13).

<details><summary>Solución comentada</summary>

`s_max = máx(|0| + 1,18322, |0| + 1,05830) = 1,18322`. Masa: `½(0 + 0) − ½·1,18322·(0,125 − 1) = 0,51766`. Momento: `½(1 + 0,1) − 0 = 0,55`. Energía: `½(0 + 0) − ½·1,18322·(0,25 − 2,5) = 1,33112`. Coincide con HLL porque `S_L = −S_R`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Para `N = 200`, ¿cuántos pasos aproximadamente para llegar a `t = 0,2` con `C = 0,8`, usando la velocidad máxima inicial?

<details><summary>Solución comentada</summary>

`Δx = 0,005`, `Δt = 0,8·0,005/1,18322 = 0,003381`; pasos `≈ 0,2/0,003381 = 59,2`, es decir, unos 60. Es una estimación: la velocidad máxima cambia cuando el flujo se desarrolla (8.6).
</details>

**Ejercicio 5.** Con los errores L1 de HLL `1,676 × 10⁻²` (`N = 100`) y `1,065 × 10⁻²` (`N = 200`), calcula el orden observado.

<details><summary>Solución comentada</summary>

`log₂(1,676/1,065) = 0,654`. Menor que 1 porque hay discontinuidades: el error se concentra en los frentes (8.7).
</details>

**Ejercicio 6.** Con los errores máximos de la advección `3,87 × 10⁻²` (`N = 100`) y `1,95 × 10⁻²` (`N = 200`), calcula el orden y explica la diferencia con el de Sod.

<details><summary>Solución comentada</summary>

`log₂(3,87/1,95) = 0,99`: orden 1. Con una onda suave, el error de truncamiento domina y sigue la ley teórica; con discontinuidades, el error medido en L1 se concentra en unas pocas celdas y decrece más despacio.
</details>

**Ejercicio 7.** Con frontera transmisiva y ondas que no llegan a los bordes, ¿cuánto cambia el momento total del tubo de Sod en `t = 0,2`?

<details><summary>Solución comentada</summary>

El cambio es el flujo de momento que entra por la izquierda menos el que sale por la derecha: `(p_L − p_R)·t = (1 − 0,1)·0,2 = 0,18`. La masa y la energía no cambian, porque el flujo de masa `ρu` y de energía `u(E+p)` son cero en los extremos (`u = 0`). El laboratorio lo verifica a `10⁻¹²`.
</details>

**Ejercicio 8.** Recupera `u` y `p` de la celda izquierda tras el paso del ejemplo 13: `q = (0,65, 0,30426, 1,6)`.

<details><summary>Solución comentada</summary>

`u = 0,30426/0,65 = 0,46809`. `p = (γ − 1)(E − ½ρu²) = 0,4(1,6 − ½·0,65·0,21912) = 0,4(1,6 − 0,07121) = 0,6115`.
</details>

**Ejercicio 9 · transferencia.** La ecuación de Burgers `u_t + (u²/2)_x = 0` tiene un choque entre `u_L = 2` y `u_R = 0`. La velocidad del choque en forma conservativa es `s = [f]/[q]`. Calcúlala y explica por qué un esquema conservativo es la elección segura para reproducirla.

<details><summary>Solución comentada</summary>

`f = u²/2`: `f(2) = 2`, `f(0) = 0`; `s = (2 − 0)/(2 − 0) = 1`. El esquema conservativo respeta la ley integral (lo que sale de una celda entra en la vecina), y de ella sale esa velocidad; una forma no conservativa no ofrece esa garantía. Es la razón de usar volúmenes finitos.
</details>

**Ejercicio 10 · transferencia.** En una simulación de viento solar, una celda mide 1 000 km, `|u| = 400 km/s` y `c = 60 km/s` (valores **ilustrativos**). Calcula el paso máximo con `C = 0,8` y cuántos pasos se necesitan para simular 1 hora.

<details><summary>Solución comentada</summary>

`Δt = 0,8·1 000/(400 + 60) = 1,739 s`. Una hora son 3 600 s: unos 2 070 pasos. Si se refina la malla a la mitad, el paso se reduce a la mitad y los pasos se duplican en cada dirección (8.6).
</details>

**Ejercicio 11 · transferencia.** Un código arroja densidad negativa en el primer paso con `C = 1,3`. ¿Qué lo explica y cómo lo confirmas?

<details><summary>Solución comentada</summary>

`C > 1` viola la CFL: la información sale de la celda vecina y el esquema resta más masa de la que hay. Se confirma repitiendo con `C = 0,8` (si desaparece, era la CFL) y con un paso más pequeño. Un error de signo en el flujo no desaparecería al reducir `Δt`.
</details>

**Ejercicio 12 · integrador.** Elabora el *informe de verificación del solucionador*: ejecuta el laboratorio con tres mallas, tabula el error L1 de Rusanov y HLL, calcula los órdenes observados, verifica la conservación y concluye cuál usarías para un problema con contacto y por qué.

<details><summary>Solución modelo</summary>

Tabla de la sección 17 (errores y órdenes); residuo de conservación `~10⁻¹⁶`; el momento cambia en `0,18`; conclusión: HLL, porque su error es menor en las tres mallas (`6,75 × 10⁻³` frente a `1,03 × 10⁻²` con 400 celdas), con la advertencia de que ninguno resuelve el contacto con nitidez; mencionar que los datos son sintéticos y adimensionales y citar S1 y S2 con su estado.
</details>

## 17. Laboratorio: advección, Rusanov y HLL frente a la solución exacta

El script [volumenes_finitos_sod.py](volumenes_finitos_sod.py) usa volúmenes finitos de primer orden. Primero verifica la advección contra la solución exacta; luego resuelve Euler 1D con Rusanov y HLL, calcula el problema de Riemann exacto de Sod y falla si los estados `p*` y `u*` no coinciden con los valores tabulados, si la conservación se rompe o si HLL no iguala o mejora el error de Rusanov.

**Datos:** sintéticos y adimensionales. **Predice antes de ejecutar:** ¿cuál de los dos métodos tiene menor error y cuál es el orden esperado con discontinuidades? (HLL; menor que 1.) **Ejecución del 2026-11-05 (Python 3.12.9, NumPy 2.4.4):**

```text
Python 3.12.9  NumPy 2.4.4
(a) advección lineal, u0 = sin(2 pi x), a = 1, periodica, t = 1 (una vuelta)
    N=  50  error max = 7.3559e-02
    N= 100  error max = 3.8705e-02
    N= 200  error max = 1.9545e-02
    N= 400  error max = 9.8210e-03
    orden observado: 0.926 0.986 0.993
(b) Sod exacto: p* = 0.30313  u* = 0.92745  rho*_izq = 0.42632  rho*_der = 0.26557
    Rusanov N= 100  L1(densidad) = 2.2788e-02  residuo de conservacion = 2.3e-16
    Rusanov N= 200  L1(densidad) = 1.5612e-02  residuo de conservacion = 2.2e-16
    Rusanov N= 400  L1(densidad) = 1.0322e-02  residuo de conservacion = 2.8e-17
    Rusanov orden observado L1: 0.546 0.597
    HLL     N= 100  L1(densidad) = 1.6760e-02  residuo de conservacion = 8.3e-17
    HLL     N= 200  L1(densidad) = 1.0652e-02  residuo de conservacion = 2.2e-16
    HLL     N= 400  L1(densidad) = 6.7509e-03  residuo de conservacion = 5.6e-17
    HLL     orden observado L1: 0.654 0.658
Pruebas superadas.
```

```bash
python programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/volumenes_finitos_sod.py
```

**Límites:** primer orden, un gas ideal, 1D, frontera transmisiva; el tiempo final es el de las ondas que no han alcanzado los bordes; el «residuo de conservación» es el cambio total menos el flujo de frontera. Los resultados son **simulados**.

## 18. Errores frecuentes y cómo corregirlos

**Usar la forma no conservativa de una ecuación con choques.** Se corrige con el ejercicio 9: la velocidad del choque la decide la forma conservativa.

**Evaluar la CFL con la velocidad del fluido en lugar de `|u| + c`.** Se corrige con los ejercicios 4 y 10.

**Usar en una interfaz un flujo distinto para cada celda vecina.** Rompe la conservación; se detecta con el residuo del ejercicio 7.

**Esperar orden 1 del error con discontinuidades.** Se corrige con los ejercicios 5 y 6.

**Confundir el emborronamiento del primer orden con un error de programa.** Se corrige con la sección 14 y el ejercicio 12.

## 19. Cómo sabrás que vas bien

Tras 8.2: ¿puedes explicar por qué la suma de las celdas solo cambia por los extremos? Si no, ejercicio 1. Tras 8.5: ¿sabes cuándo Rusanov y HLL dan el mismo flujo? Si no, ejercicio 3. Tras 8.6: ¿cuántos pasos necesita una malla el doble de fina? Si no, ejercicio 10. Tras el laboratorio: ¿cómo sabes que el solucionador es correcto y no solo estable? (compara con la solución exacta y comprueba la conservación).

## 20. Qué entregas y cómo se evalúa

El producto es tu **informe de verificación del solucionador** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Esquema conservativo | Sin forma de flujo | Fórmula sin comprobar | Deduce y comprueba la conservación | Relaciona el residuo con el flujo de frontera |
| Flujo numérico | Confunde métodos | Aplica uno | Aplica Rusanov y HLL | Explica cuándo coinciden |
| CFL | Ausente | Sin justificar | Calcula `Δt` correcto | Evalúa el costo al refinar |
| Verificación | Sin comparación | Gráfica sin cifras | Tabla de errores y órdenes | Explica por qué el orden es menor que 1 |
| Fuentes y rotulado | Sin fuentes | Sin fecha | Con localizador y fecha | Rotula sintético, simulado y adimensional |

**Condiciones críticas (no se compensan con promedio):** comparar con una solución exacta o de referencia; comprobar la conservación; rotular lo sintético y lo simulado; citar solo fuentes consultadas.

## 21. Ética, seguridad y límites

Una simulación adimensional de primer orden no sirve para pronosticar el clima espacial ni para diseñar un escudo térmico. Ningún resultado de esta clase es operativo. Un código que no conserva puede parecer plausible y dar masas o energías sin sentido. Accesibilidad: fórmulas en texto, tablas equivalentes a las gráficas, ejercicios sin conexión.

## 22. Para cerrar y seguir

Un esquema de volúmenes finitos conserva porque cada flujo se resta de un lado y se suma al otro; el flujo se obtiene aproximando el problema de Riemann (Rusanov, HLL); el paso de tiempo lo fija la CFL; con discontinuidades el error es menor que de primer orden. Queda abierta una pregunta: cuando la solución es suave pero el esquema es de primer orden y difunde, ¿cómo cambia una onda que viaja muchas longitudes de onda? Es el tema de la ecuación de onda y la dispersión numérica.

**Glosario español–inglés.** ley de conservación · *conservation law*; volumen finito · *finite volume*; flujo numérico · *numerical flux*; problema de Riemann · *Riemann problem*; contracorriente · *upwind*; condición CFL · *CFL condition*; onda de choque · *shock wave*; rarefacción · *rarefaction*; discontinuidad de contacto · *contact discontinuity*; tubo de choque · *shock tube*.

**Continuidad.** B21-C02 reutiliza tu **verificación contra una solución exacta** para medir el error de fase de una onda.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B20-C04 — Redacción de un artículo científico](../../../tronco-comun/B20-metodologia-de-la-investigacion-cientifica.md#b20-c04) · [📚 Bloque B21](../../../tronco-comun/B21-metodos-numericos-para-edp-y-fluidos-computacionales.md) · [Siguiente: B21-C02 — Ecuación de onda: esquemas y dispersión numérica →](../B21-C02-ecuacion-de-onda-esquemas-y-dispersion-numerica/CLASE.md)
<!-- /nav -->
