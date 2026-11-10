# B75-C10 — Maniobras impulsivas

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B75](../../../tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md) · [← Anterior: B75-C09 — Presupuestos de delta-v](../B75-C09-presupuestos-de-delta-v/CLASE.md) · [Siguiente: B75-C11 — Propulsión de bajo empuje →](../B75-C11-propulsion-de-bajo-empuje/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 10 del bloque B75. Nivel N3. Todos los cálculos hasta aquí suponían impulsos instantáneos. Un motor real empuja durante minutos u horas, y en ese tiempo la gravedad sigue actuando y la nave se mueve. Aquí integras con RK4 una salida desde órbita baja con empuje finito y mides cuánto delta-v adicional cuesta frente al impulso ideal. El caso es el de salida hacia Marte del modelo de C01 (`v∞ = 2,9452 km/s`).

## 2. Por qué esta clase existe

El modelo impulsivo es útil, pero ¿cuándo es un buen modelo? La decisión central: **¿cuánto delta-v se pierde por quemar durante un tiempo finito y de qué depende, en particular del cociente empuje/peso?**

## 3. Lo que podrás hacer al terminar

1. Distinguir impulso instantáneo y empuje finito.
2. Integrar el movimiento con empuje prógrado y masa variable.
3. Calcular la duración de una quema con la ecuación del cohete.
4. Medir la pérdida de delta-v respecto del impulsivo para varios cocientes empuje/peso.
5. Decidir cuándo el modelo impulsivo es aceptable.
6. Separar lo consultado de lo sintético (empuje, `I_sp`, masa).

La evidencia es tu **curva de pérdida frente a empuje/peso** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es el delta-v impulsivo de salida?
2. ¿Qué dice la ecuación del cohete?
3. ¿Qué es el empuje sobre peso?
4. ¿Qué es una pérdida por gravedad?
5. ¿Qué es RK4?

<details>
<summary>Ver respuestas</summary>

1. `√(v∞² + 2μ/r) − √(μ/r)` (B75-C09). 2. `Δv = I_sp g₀ ln(m₀/m_f)`. 3. La aceleración inicial dividida por `g₀`. 4. Delta-v gastado en vencer la atracción durante la quema. 5. Un integrador de cuarto orden con paso fijo.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

La salida a Marte desde una órbita circular de `300 km` (periodo `90,37 min`) cuesta `3,5916 km/s` en el modelo impulsivo. Quemando con empuje/peso inicial `0,5`, hace falta `3,6135 km/s` en `7,29 min` (pérdida `0,61 %`); con `0,05`, `4,6526 km/s` en `82,45 min` (pérdida `29,5 %`). Es el **ejemplo conductor**. Es un cálculo sintético; no se consultó ningún motor real. La NASA recuerda que la maniobra de Hohmann se describe con un único encendido [S3], una idealización de esta clase.

## 6. Vocabulario

El **empuje finito** es una fuerza constante durante un tiempo. La **pérdida por empuje finito** es la diferencia entre el delta-v real (`I_sp g₀ ln(m₀/m_f)`) y el impulsivo. El **cociente empuje/peso** `T/W₀ = T/(m₀ g₀)` fija la aceleración inicial. La **quema prógrada** empuja en el sentido de la velocidad. El **flujo másico** es `ṁ = T/(I_sp g₀)`.

## 7. Modelo mental: empujar un columpio

```mermaid
flowchart LR
    T["T/W0, Isp, m0"] --> I["integrar r, v, m con RK4"]
    I --> E["parar si energia = v_inf^2/2"]
    E --> D["dv finito = Isp g0 ln(m0/m)"]
    D --> L["perdida = dv finito - dv impulsivo"]
```

*Descripción textual:* Se integra el movimiento con empuje prógrado hasta alcanzar la energía de escape objetivo; el delta-v finito se obtiene de la masa gastada y se compara con el impulsivo.

Analogía: empujar un columpio: un empujón corto equivale a un golpe; empujar mucho tiempo es diferente porque el columpio se mueve mientras se empuja. Límite: la nave no está en un columpio; la gravedad cambia de dirección durante la quema.

## 8. La explicación, paso a paso

### 8.1 El modelo

Dos cuerpos con `μ = 398 602,54 km³/s²` (masa de la ficha y `G` del JPL [S1, S2]), empuje constante `T = (T/W₀)·m₀·g₀`, dirección igual a la velocidad, flujo másico `ṁ = T/(I_sp g₀)` con `I_sp = 320 s` (sintético) y `m₀ = 1000 kg`. Se detiene cuando `ε = v²/2 − μ/r` alcanza `v∞²/2 = 4,3371 km²/s²`.

### 8.2 Resultado

| `T/W₀` | Duración (min) | `Δv` finito (km/s) | Pérdida (km/s) | Pérdida (%) |
|---|---|---|---|---|
| 0,02 | 218,31 | 5,3579 | 1,77 | 49,2 |
| 0,05 | 82,45 | 4,6526 | 1,06 | 29,5 |
| 0,1 | 38,47 | 4,0098 | 0,418 | 11,6 |
| 0,5 | 7,29 | 3,6135 | 0,0219 | 0,61 |
| 5 | 0,73 | 3,5919 | 0,000222 | 0,0062 |
| 500 | 0,01 | 3,5916 | −9×10⁻⁸ | ≈ 0 |

El impulsivo vale `3,5916 km/s`. El valor negativo de la última fila es ruido numérico menor que `10⁻⁶ km/s`.

### 8.3 Duración por la ecuación del cohete

`t = (m₀/ṁ)(1 − e^{−Δv/(I_sp g₀)})` con `ṁ = (T/W₀) m₀/I_sp`. Para `T/W₀ = 0,5`: `t = (320/0,5)(1 − e^{−3,6135/3,1381}) = 640×0,6838 = 437,6 s = 7,29 min`, igual a la integración. Para `0,02`: `13 098 s = 218,3 min`, igual también.

### 8.4 Lectura

La pérdida cae rápido con el empuje: con `T/W₀ ≥ 5` es menor que `0,01 %`. En este modelo, una quema con `T/W₀` de décimas pierde entre 0,6 % y 12 %; con `T/W₀` de milésimas o menos la quema dura tantas órbitas que ya no es una quema única sino una espiral (C11). Los valores de empuje de motores reales no se consultaron.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `T/W₀` | empuje sobre peso inicial | — | 0,02 a 500 |
| `I_sp` | impulso específico | s | 320 (sintético) |
| `ṁ` | flujo másico | kg/s | `(T/W₀) m₀/I_sp` |
| `ε` | energía específica | km²/s² | objetivo 4,3371 |
| `Δv` | delta-v finito | km/s | 3,5916 a 5,3579 |

## 10. Convenciones y referencias

Marco geocéntrico plano; empuje prógrado de módulo constante; `g₀ = 9,80665 m/s²` estándar; paso de integración elegido para tener 20 000 pasos por quema (mínimo 10⁻⁴ s). Altitud 300 km, `I_sp` y masa **sintéticas**. `v∞` del modelo circular y coplanar de B75-C01.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA/NSSDC, Earth Fact Sheet — https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html (consultada 2026-11-10) | página leída | semieje 149,598×10⁶ km, periodo sideral 365,256 d, excentricidad 0,0167, velocidad orbital media 29,78 km/s, masa 5,9722×10²⁴ kg, radio medio 6371,000 km, velocidad de escape 11,186 km/s | Consultada |
| S2 | NASA JPL SSD, Planetary Physical Parameters — https://ssd.jpl.nasa.gov/planets/phys_par.html (consultada 2026-11-10) | página leída | radios ecuatoriales (Venus 6051,8 km; Tierra 6378,1366 km; Marte 3396,19 km; Júpiter 71 492 km) y la constante G = 6,67430×10⁻¹¹ m³ kg⁻¹ s⁻² citada en su registro de cambios. La página no lista GM: aquí GM = G·M con las masas de las fichas NSSDC | Consultada |
| S3 | NASA, Basics of Space Flight, cap. 4 «Interplanetary Trajectories» — https://science.nasa.gov/learn/basics-of-space-flight/chapter4-1/ (consultada 2026-11-10) | página leída | transferencia de Hohmann como ruta de menor propulsante; oportunidades mínimas de energía a Marte cada ~25 meses y a Venus cada ~19 meses; la asistencia gravitacional cambia la velocidad heliocéntrica y deja la relativa en módulo; el vuelo de Galileo por Ío redujo el propulsante de inserción en 90 kg | Consultada |
| — | Valores estándar (no consultados en una fuente concreta de esta clase) | — | GM☉ = 1,32712440×10¹¹ km³/s² (valor estándar, ver la resolución IAU 2015 B3 de la fila anterior donde se cita); 1 au = 149 597 870,7 km; c = 299 792,458 km/s; g₀ = 9,80665 m/s²; ecuaciones de dos cuerpos | No consultada en una fuente concreta |

Límites: no se consultó ningún motor ni perfil de quema real; la dirección de empuje es la de la velocidad, no óptima; no hay atmósfera ni achatamiento terrestre.

## 12. Cómo ver la pérdida

| `T/W₀` | Pérdida (%) |
|---|---|
| 0,02 | 49,2 |
| 0,1 | 11,6 |
| 0,5 | 0,61 |
| 5 | 0,0062 |

Descripción larga: la pérdida cae de 11,6 % a 0,0062 % cuando el empuje sube 50 veces (de 0,1 a 5) y tiende a cero.

## 13. Ejemplo trabajado: T/W₀ = 0,5

**Paso 1 · Delta-v.** `Δv = 3,6135 km/s` (laboratorio).

**Paso 2 · Flujo másico.** `ṁ = 0,5×1000/320 = 1,5625 kg/s`.

**Paso 3 · Duración.** `t = (1000/1,5625)(1 − e^{−1,1515}) = 437,6 s`.

**Paso 4 · Pérdida.** `3,6135 − 3,5916 = 0,0219 km/s`.

## 14. Distintas formas de abordar el problema

**Por el modelo impulsivo:** `Δv = 3,5916` sin duración. **Por integración:** pérdida y duración. **Por fórmula cerrada de duración:** `t = (m₀/ṁ)(1 − e^{−Δv/(I_sp g₀)})`. **Por multi-perigeo:** repartir la quema en varios pasos de perigeo, idea estándar que esta clase no simula.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula el flujo másico para `T/W₀ = 0,5`, `m₀ = 1000 kg` e `I_sp = 320 s`. *Pasos:* `ṁ = (T/W₀) m₀/I_sp`.

<details><summary>Solución comentada</summary>

`1,5625 kg/s`.
</details>

**Ejercicio 2 · con una pista.** Calcula la duración con `Δv = 3,6135 km/s`. *Pista:* `1 − e^{−Δv/(I_sp g₀)}` con `I_sp g₀ = 3,1381 km/s`.

<details><summary>Solución comentada</summary>

`t = 437,6 s = 7,29 min`.
</details>

**Ejercicio 3 · casi autónomo.** Calcula la pérdida relativa.

<details><summary>Solución comentada</summary>

`0,0219/3,5916 = 0,61 %`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Calcula la fracción de masa quemada con `T/W₀ = 0,1`.

<details><summary>Solución comentada</summary>

`1 − e^{−4,0098/3,1381} = 0,7213`.
</details>

**Ejercicio 5 · autónomo.** ¿Cuántas órbitas iniciales (periodo `90,37 min`) dura la quema con `T/W₀ = 0,02`?

<details><summary>Solución comentada</summary>

`218,31/90,37 = 2,4`.
</details>

**Ejercicio 6 · autónomo.** ¿Por qué la duración no escala exactamente como `1/(T/W₀)` entre `0,5` (7,29 min) y `0,1` (38,47 min)?

<details><summary>Solución comentada</summary>

Porque `t ∝ 1/ṁ ∝ 1/T` solo a igual delta-v; aquí el delta-v finito también cambia (de 3,6135 a 4,0098 km/s) y el factor `1 − e^{−Δv/(I_sp g₀)}` crece: `7,29×5 = 36,5 min` frente a `38,47 min`.
</details>

**Ejercicio 7 · autónomo.** Con una pérdida de 11,6 %, ¿cuántos kg extra se queman en `T/W₀ = 0,1` frente al impulsivo (`m₀ = 1000 kg`, `I_sp = 320 s`)?

<details><summary>Solución comentada</summary>

Impulsivo: `1000(1 − e^{−3,5916/3,1381}) = 681,6 kg`; finito: `721,3 kg`; diferencia `39,7 kg`.
</details>

**Ejercicio 8 · autónomo.** ¿Por qué un impulso finito prógrado cuesta más que el impulsivo?

<details><summary>Solución comentada</summary>

Porque durante la quema la gravedad actúa y la velocidad no está alineada con la dirección óptima en cada instante (pérdida de gravedad y de dirección).
</details>

**Ejercicio 9 · transferencia.** Un motor eléctrico entrega `T/W₀ = 10⁻⁴`. ¿Puede hacer esta salida en una quema?

<details><summary>Solución comentada</summary>

No: la quema duraría semanas y la nave no escaparía en una pasada; se usa una espiral (C11).
</details>

**Ejercicio 10 · transferencia.** ¿Basta `T/W₀ = 0,5` para que la pérdida sea menor que 1 %? ¿Y un valor menor?

<details><summary>Solución comentada</summary>

Sí para `0,5` (0,61 %). Para un valor entre `0,1` (11,6 %) y `0,5` hay que repetir el laboratorio con ese valor; la tabla no lo da.
</details>

**Ejercicio 11 · transferencia.** Un equipo reparte la quema en tres pasos por el perigeo. ¿Qué espera?

<details><summary>Solución comentada</summary>

Menos pérdida que una quema única de igual `T/W₀`, a costa de tiempo; el efecto no se calculó aquí.
</details>

**Ejercicio 12 · integrador.** Elabora tu *curva de pérdida frente a empuje/peso* con al menos seis valores de `T/W₀`, la duración por la fórmula y por integración, y una conclusión sobre cuándo es válido el modelo impulsivo.

<details><summary>Solución comentada</summary>

Secciones 8.2–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: quema finita y pérdida

El script [impulso_finito.py](impulso_finito.py) integra con RK4 la salida desde 300 km con seis valores de `T/W₀` y **comprueba** que la pérdida es menor que 0,1 % con `T/W₀ = 500` y que crece al bajar el empuje.

**Datos:** masa y radio terrestres de la ficha NASA/NSSDC y `G` del JPL (consultados); `v∞ = 2,9452 km/s` del modelo de C01; empuje, `I_sp`, masa y altitud **sintéticos**. **Predice antes de ejecutar:** ¿Qué pérdida tendrá `T/W₀ = 0,5`? (0,61 %.) **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Orbita inicial: r = 6671 km ; v_circ = 7.7299 km/s ; periodo = 90.37 min
Impulsivo: dv = 3.5916 km/s
 empuje/peso inicial   duracion [min]   dv finito [km/s]   perdida [km/s]   perdida relativa [%]
          0.020          218.31             5.3579            1.77               49.2
          0.050           82.45             4.6526            1.06               29.5
          0.100           38.47             4.0098           0.418               11.6
          0.500            7.29             3.6135          0.0219               0.61
          5.000            0.73             3.5919        0.000222            0.00619
        500.000            0.01             3.5916       -9.09e-08          -2.53e-06
Pruebas superadas.
```

```bash
python programa/clases/B75/B75-C10-maniobras-impulsivas/impulso_finito.py
```

**Límites:** dos cuerpos, empuje prógrado, sin atmósfera; el resultado a `T/W₀ = 500` tiene ruido numérico de `10⁻⁷ km/s`.

## 18. Errores frecuentes y cómo corregirlos

**Usar el modelo impulsivo con empuje bajo.** Se corrige con 8.2.

**Olvidar que la masa varía durante la quema.** Se corrige con 8.3.

**Confundir `T/W₀` con la aceleración final.** Se corrige con la sección 6.

**Presentar los motores sintéticos como reales.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras 8.2: ¿a partir de qué `T/W₀` es aceptable el modelo impulsivo? Tras el laboratorio: ¿qué dos comprobaciones hace? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **curva de pérdida frente a empuje/peso** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Confunde impulsivo y finito | Define la pérdida | Calcula duración y pérdida | Explica la dependencia |
| Cálculo | Sin unidades | Con errores | Tabla completa | Calcula casos nuevos |
| Numérico | Sin comprobar | Una prueba | Integración y fórmula | Interpreta el ruido |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo sintético |
| Límites | No los nombra | Uno | Tres | Discute el multi-perigeo |

**Condiciones críticas (no se compensan con promedio):** rotular empuje, `I_sp` y masa como sintéticos; no presentar la pérdida como de un motor real; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados (órbitas planetarias circulares y coplanares, dos cuerpos) y sus datos son consultados, sintéticos o ilustrativos y están rotulados; ningún resultado es una efeméride, una medición ni un diseño de misión real. Una quema real se diseña con optimización de dirección y análisis de fallos; esta clase no lo hace. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

La pérdida es `0,61 %` con `T/W₀ = 0,5` y `29,5 %` con `0,05`. Queda una pregunta: ¿qué pasa cuando el empuje es tan bajo que la nave sube en espiral durante meses?

**Glosario español–inglés.** empuje finito · *finite thrust*; pérdida por gravedad · *gravity loss*; empuje sobre peso · *thrust-to-weight ratio*; flujo másico · *mass flow rate*; quema · *burn*.

**Continuidad.** [B75-C11](../B75-C11-propulsion-de-bajo-empuje/CLASE.md) estudia la espiral de bajo empuje.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B75-C09 — Presupuestos de delta-v](../B75-C09-presupuestos-de-delta-v/CLASE.md) · [📚 Bloque B75](../../../tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md) · [Siguiente: B75-C11 — Propulsión de bajo empuje →](../B75-C11-propulsion-de-bajo-empuje/CLASE.md)
<!-- /nav -->
