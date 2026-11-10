# B85-C10 — Control térmico activo

<!-- nav:top -->
x
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 10 del bloque B85. Nivel N3. El control térmico activo mantiene una temperatura con un sensor, un controlador y un calentador. Aquí cierras un lazo PI sobre un nodo con capacidad térmica, ves que el error de régimen es nulo, que la potencia de régimen es la que equilibra las pérdidas, y que sin antiwindup la saturación produce un sobreimpulso grande. El nodo y las ganancias son sintéticos.

## 2. Por qué esta clase existe

Un termostato de dos estados oscila; un lazo proporcional-integral mantiene una temperatura sin oscilar, pero se equivoca si el calentador se satura. La decisión central: **¿qué ganancias dan error nulo sin sobreimpulso y qué pasa cuando el calentador se satura?** La decisión central: **¿qué ganancias dan error nulo sin sobreimpulso y qué pasa cuando el calentador se satura?**

## 3. Lo que podrás hacer al terminar

1. Plantear el lazo PI sobre un nodo de primer orden.
2. Calcular la potencia de régimen y verificar el error nulo.
3. Medir sobreimpulso y tiempo de asentamiento.
4. Calcular `ω_n` y `ζ` del lazo lineal.
5. Mostrar el efecto de la saturación con y sin antiwindup.
6. Separar lo consultado (nota de NASA sobre PID) de lo ilustrativo (todo el nodo).

La evidencia es la **ficha de sintonía de un lazo térmico** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es un controlador PI?
2. ¿Qué elimina la parte integral?
3. ¿Qué es la saturación del actuador?
4. ¿Qué es el windup?
5. ¿Qué es una verificación por segunda vía?

<details>
<summary>Ver respuestas</summary>

1. Uno cuya salida es `K_p e + K_i ∫e dt`. 2. El error de régimen ante entradas constantes y perturbaciones constantes. 3. El límite de potencia que el calentador no puede superar. 4. La acumulación de la integral mientras el actuador está saturado. 5. Calcular lo mismo con otro método y comparar.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Un nodo de `1500 J/K` con acoplamiento de `0,3 W/K` a `250 K`, un PI (`K_p = 20 W/K`, `K_i = 0,05 W/(K s)`) y calentador de `30 W` llega a `283 K` con error final `1,7 × 10⁻⁵ K` y potencia `9,93 W` (esperada `9,90 W`). Es el **ejemplo conductor**. Todo es **ilustrativo**.

## 6. Vocabulario

El **lazo PI** calcula `u = K_p e + K_i ∫e dt`. Para el nodo `C Ṫ = −G(T − T_sum) + u` los polos cumplen `C s² + (G + K_p)s + K_i = 0`, con `ω_n = √(K_i/C)` y `ζ = (G + K_p)/(2√(C K_i))`. El **antiwindup** detiene la integral cuando el actuador satura. El **sobreimpulso** es el máximo exceso sobre la consigna.

## 7. Modelo mental

```mermaid
flowchart LR
    R["Consigna 283 K"] --> E["Error e"]
    T["T medida"] --> E
    E --> PI["u = Kp e + Ki ∫e"]
    PI --> SAT["Saturación 0 a 30 W"]
    SAT --> N["Nodo: C dT/dt = −G(T − Tsum) + u"]
    N --> T
```

*Descripción textual:* el error entre consigna y temperatura entra al PI; su salida se satura entre 0 y 30 W y alimenta el nodo, cuya temperatura realimenta.

Analogía: conducir con un acelerador que no puede pasar de cierto tope: si sigues pisando la integral acumula y luego te pasas. Límite: el nodo es lineal y el sensor ideal; un lazo real tiene retardo, ruido y cuantización.

## 8. La explicación, paso a paso

### 8.1 Régimen

En régimen `0 = −G(T_set − T_sum) + u`, de modo que `u = G(T_set − T_sum) = 9,90 W`. Tras `t = 3000 s` el nodo está a `282,9931 K` y entrega `9,932 W`. Al bajar el sumidero `10 K` la potencia final esperada es `12,90 W`; a `6000 s` la simulación da `12,900 W` y un error de `1,7 × 10⁻⁵ K`: la parte integral absorbe la perturbación.

### 8.2 Polos

`ω_n = 0,00577 rad/s` y `ζ = 1,17`: sobreamortiguado; por eso no hay sobreimpulso (`-0,007 K` respecto de la consigna). El tiempo de asentamiento a `±0,5 K` es `2018 s`, limitado por la saturación de `30 W` en el arranque.

### 8.3 Saturación

Con ganancias bajas en `K_p` (`2 W/K`) y altas en `K_i` (`0,5 W/(K s)`), el calentador se satura al arrancar. Con antiwindup el sobreimpulso es `0,696 K`; sin él, `12,122 K`: la integral acumulada durante la saturación empuja la temperatura mucho más allá de la consigna.

### 8.4 Elegir ganancias

`K_i` alto acelera pero reduce `ζ`; `K_p` alto aumenta `ζ` pero usa más potencia en el arranque y amplifica el ruido del sensor. La consigna debe estar por encima de `T_sum + P_max/G = 350 K` para que la potencia alcance: con `30 W` el nodo puede llegar como máximo a esa temperatura.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `C` | capacidad térmica | J/K | 1500 |
| `G` | acoplamiento | W/K | 0,3 |
| `K_p` | ganancia proporcional | W/K | 20 |
| `K_i` | ganancia integral | W/(K s) | 0,05 |
| `ζ` | amortiguamiento | — | 1,17 |
| `P_max` | calentador máximo | W | 30 |

## 10. Convenciones y referencias

Nodo isotermo lineal, sensor ideal, paso de `1 s` (Euler). El acoplamiento `G` linealizado representa la radiación hacia el sumidero. Todo ilustrativo.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA, State-of-the-Art of Small Spacecraft Technology, capítulo Thermal Control — https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/ (consultada 2026-11-10) | sección de control activo | el sistema ATA usa un lazo de fluido con calentadores integrados y control PID para el control por zonas; los calentadores se controlan con termostato o sensor | Consultada |
| — | Dinámica de primer orden con control PI y antiwindup por condición de saturación | — | las verifica el laboratorio con una segunda vía | No consultada en una fuente concreta |

Límites: las ganancias, la capacidad, el acoplamiento y la potencia máxima no se consultaron; no se diseña el lazo de una nave real; la fuente consultada no da ganancias.

## 12. Cómo ver el resultado

| Magnitud | Valor |
|---|---|
| potencia de régimen | 9,93 W |
| error final | 1,7 × 10⁻⁵ K |
| `ζ` | 1,17 |
| sobreimpulso con antiwindup | 0,696 K |
| sobreimpulso sin antiwindup | 12,122 K |

Descripción larga: el PI elimina el error y ajusta la potencia ante la perturbación; la saturación sin antiwindup lleva a 12 K de sobreimpulso.

## 13. Ejemplo trabajado

**Paso 1 · Régimen.** `u = 0,3 × (283 − 250) = 9,90 W`.

**Paso 2 · `ζ`.** `(0,3 + 20)/(2 √(1500 × 0,05)) = 1,17`.

**Paso 3 · Perturbación.** El sumidero baja `10 K` y `u = 0,3 × 43 = 12,90 W`.

## 14. Distintas formas de describir el problema

**Por ecuación:** `u = K_p e + K_i ∫e`. **Por polos:** `ω_n`, `ζ`. **Por régimen:** `u = G ΔT`. **Por saturación:** con y sin antiwindup.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula la potencia de régimen para `T_set = 290 K`. *Pasos:* `G (T_set − T_sum)`.

<details><summary>Solución comentada</summary>

`0,3 × 40 = 12 W`.
</details>

**Ejercicio 2 · con una pista.** Predice si `T_set = 300 K` es alcanzable con `30 W`. *Pista:* máximo `T_sum + P_max/G`.

<details><summary>Solución comentada</summary>

Sí: el máximo es `350 K` y `0,3 × 50 = 15 W`.
</details>

**Ejercicio 3 · casi autónomo.** ¿Por qué el error final es casi cero? Piensa en la parte integral.

<details><summary>Solución comentada</summary>

La integral sigue creciendo mientras `e ≠ 0`; en régimen `e = 0`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Calcula `ω_n` si `K_i = 0,2`.

<details><summary>Solución comentada</summary>

`√(0,2/1500) = 0,01155 rad/s`.
</details>

**Ejercicio 5 · autónomo.** Calcula `ζ` con `K_p = 5` y `K_i = 0,05`.

<details><summary>Solución comentada</summary>

`(0,3 + 5)/(2√(1500 × 0,05)) = 0,31`.
</details>

**Ejercicio 6 · autónomo.** ¿Cuál es la constante de tiempo del nodo sin control?

<details><summary>Solución comentada</summary>

`C/G = 5000 s`.
</details>

**Ejercicio 7 · autónomo.** ¿Qué máxima consigna alcanza el nodo con `P_max = 10 W`?

<details><summary>Solución comentada</summary>

`250 + 10/0,3 = 283,3 K`.
</details>

**Ejercicio 8 · autónomo.** ¿Cómo cambia el régimen si `G` sube a `0,6 W/K`?

<details><summary>Solución comentada</summary>

`u = 0,6 × 33 = 19,8 W`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un lazo PI se satura al arrancar y se pasa 12 K. ¿Qué cambias?

<details><summary>Solución comentada</summary>

Activas el antiwindup o reduces `K_i` y limitas la integral; el sobreimpulso baja a `0,7 K` en este caso.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** Un sensor tiene un retardo de `20 s`. ¿Qué esperas del amortiguamiento efectivo?

<details><summary>Solución comentada</summary>

El retardo reduce el margen de fase y el amortiguamiento efectivo; hay que bajar las ganancias.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** Un colega presenta la sintonía de la clase como «la del control de nuestra nave». ¿Qué corriges?

<details><summary>Solución comentada</summary>

Es una sintonía de un nodo sintético; la nave real tiene otra dinámica y hay que sintonizar con su modelo.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de sintonía de un lazo térmico*: ganancias, `ω_n`, `ζ`, potencia de régimen, error, sobreimpulso con y sin antiwindup y lista de lo ilustrativo.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: lazo PI con calentador

El script [control_activo.py](control_activo.py) simula el lazo PI con saturación y perturbación, calcula `ω_n`, `ζ`, error, sobreimpulso y compara con y sin antiwindup (**comprueba** potencia de régimen a 0,05 W, error < 0,01 K, reducción de sobreimpulso con antiwindup y `u ≤ P_max`).

**Datos:** todo **ilustrativo** (nodo, ganancias, potencia máxima, perturbación). **Predice antes de ejecutar:** ¿hay sobreimpulso con `ζ = 1,17`? (no.) **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Nodo ILUSTRATIVO: C = 1500 J/K, G = 0.3 W/K, sumidero 250 K, consigna 283 K, calentador maximo 30 W
PI: Kp = 20.0 W/K, Ki = 0.05 W/(K s) ; polos lineales: wn = 0.00577 rad/s, zeta = 1.17
Potencia de regimen esperada = G (Tset - Tsum) = 9.90 W ; tras bajar el sumidero 10 K = 12.90 W
Antes de la perturbacion (t = 3000 s): T = 282.9931 K ; P = 9.932 W
Pico = 282.993 K ; sobreimpulso = -0.007 K ; tiempo de asentamiento (+-0.5 K) = 2018 s ; P maxima = 30.00 W
Final (t = 6000 s): T = 283.0000 K ; P = 12.900 W ; error = 1.73e-05 K
Kp = 2, Ki = 0.5 con saturacion: sobreimpulso con antiwindup = 0.696 K ; sin antiwindup = 12.122 K
Pruebas superadas.
```

```bash
python programa/clases/B85/B85-C10-control-termico-activo/control_activo.py
```

**Límites:** nodo lineal, sensor ideal y sin retardo; Euler de `1 s`; no incluye ruido ni cuantización.

## 18. Errores frecuentes y cómo corregirlos

**Elegir una consigna inalcanzable.** `T_sum + P_max/G` es el máximo (8.4)

**Subir `K_i` sin límite.** reduce `ζ` y hay sobreimpulso (8.4)

**Ignorar la saturación.** el antiwindup evita el exceso (8.3)

**Presentar la sintonía como de una nave.** se corrige con la sección 10

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué potencia de régimen esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de sintonía de un lazo térmico** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Calcula la potencia de régimen y `ζ` | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas con unidades | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con una segunda vía | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo ilustrativo y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular el nodo y las ganancias como ilustrativos; no presentar la sintonía como la de una nave; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y sus datos son sintéticos o ilustrativos; ningún resultado describe una nave real, ni sustituye a los estándares de proyecto, a la verificación con datos de misión ni a una revisión disciplinar. Los valores de este texto no son requisitos de ningún proyecto. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Un PI de `K_p = 20` y `K_i = 0,05` mantiene `283 K` con error nulo y `9,9 W` de régimen; sin antiwindup una saturación causa `12,1 K` de sobreimpulso. Queda una pregunta: ¿qué le hacen a la nave los ciclos de temperatura de cada órbita?

**Glosario español–inglés.** lazo PI · *PI loop*; antiwindup · *anti-windup*; saturación · *saturation*; sobreimpulso · *overshoot*; consigna · *setpoint*.

**Continuidad.** [B85-C11](../B85-C11-ciclos-termicos/CLASE.md) estudia los ciclos térmicos.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
x
<!-- /nav -->
