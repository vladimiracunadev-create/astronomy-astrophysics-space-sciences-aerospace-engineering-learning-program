# B05-C02 — Posición, velocidad y aceleración

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B05](../../../tronco-comun/B05-fisica-fundamental-para-el-espacio.md) · [← Anterior: B05-C01 — Magnitudes físicas y dimensiones](../B05-C01-magnitudes-fisicas-y-dimensiones/CLASE.md) · [Siguiente: B05-C03 — Movimiento rectilíneo y circular →](../B05-C03-movimiento-rectilineo-y-circular/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Segunda clase de B05. Con C01 ya sabes qué unidad y dimensión lleva cada número; ahora describes **dónde está** un cuerpo y **cómo cambia** su posición. Nivel N1. Usas vectores en el plano (B04) solo como pares de componentes, y la idea de cociente de cambios (B03).

Verás posición, desplazamiento, velocidad media e instantánea, rapidez, aceleración y la diferencia entre magnitud escalar y vectorial. No verás todavía por qué ocurre el movimiento (fuerzas, C04) ni sus casos particulares con fórmulas (C03).

## 2. Por qué esta clase existe

Cuando una agencia dice que un satélite «va a 7,7 km/s», ¿respecto de qué y en qué dirección? La pregunta motivadora es: **¿cómo describo un movimiento de forma que otra persona lo reconstruya sin ambigüedad?** La decisión central es elegir un marco de referencia y registrar posición, velocidad y aceleración como vectores con unidad.

Aprenderás a separar lo que es dato de lo que se calcula de él: la velocidad sale de cómo cambia la posición, y la aceleración de cómo cambia la velocidad. Esto sostiene el resto del bloque.

## 3. Lo que podrás hacer al terminar

1. Definir un marco de referencia con origen, ejes, unidad y sentido positivo.
2. Distinguir desplazamiento de distancia recorrida y rapidez de velocidad.
3. Calcular velocidad media y aceleración media a partir de datos.
4. Explicar la velocidad instantánea como el límite de cocientes cada vez más cortos.
5. Reconocer que una trayectoria curva implica aceleración aunque la rapidez no cambie.
6. Estimar derivadas con diferencias finitas y saber cuándo fallan.

La evidencia es la **ficha de movimiento** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. Pasa 90 minutos a segundos.
2. Si algo avanza 300 m en 20 s, ¿cuántos m/s?
3. ¿Cuánto vale `a² + b²` si `a = 3` y `b = 4`, y su raíz?
4. ¿Qué dimensión tiene `m/s²`? (C01)
5. Si un número positivo representa «hacia el este», ¿qué signo tiene «hacia el oeste»?

<details>
<summary>Ver respuestas</summary>

1. 5400 s. 2. 15 m/s. 3. 25 y 5. 4. `L T⁻²`. 5. Negativo.
</details>

Con cuatro o cinco aciertos, sigue; con menos, repasa C01 y B03.

## 5. Un caso real: la ISS, 16 órbitas al día

NASA indica que la Estación Espacial Internacional da unas 16 órbitas cada 24 horas, una cada unos 90 minutos, y que su rapidez es de unos 5 millas por segundo (S3). Esos datos mezclan tiempo y rapidez, pero omiten algo esencial: la **dirección** cambia continuamente. Un cuerpo que mantiene su rapidez y gira, está acelerando.

Este caso lo usaremos como sentido de escala: nuestro satélite ideal tendrá unos 92,6 minutos de período. Límite: S3 es divulgativa y da cifras redondeadas; no sirve para datos orbitales de precisión.

## 6. Vocabulario

La **posición** `r` es el vector que va desde el origen del marco hasta el cuerpo; sus componentes son `(x, y)`. El **desplazamiento** `Δr = r₂ − r₁` es el cambio de posición, y la **distancia recorrida** es la longitud del camino, que puede ser mayor. La **velocidad media** es `Δr/Δt`. La **velocidad instantánea** `v` es el límite de ese cociente cuando `Δt → 0`; su módulo es la **rapidez**. La **aceleración** `a` es el ritmo de cambio de la velocidad: `a = Δv/Δt` en media y su límite en instantánea. Un **escalar** tiene solo valor (masa, tiempo, rapidez); un **vector** tiene valor y dirección (desplazamiento, velocidad, aceleración). Un **marco de referencia inercial** es uno donde un cuerpo libre se mueve en línea recta con rapidez constante; lo definimos con rigor en C04.

## 7. Modelo mental: lo que se mide y lo que se deduce

Solo se mide posición contra tiempo. Todo lo demás se deduce de esa tabla, igual que una película da la rapidez de un coche a partir de fotogramas.

```mermaid
flowchart LR
    A["Marco: origen, ejes, unidad"] --> B["Medida: r(t) en instantes"]
    B --> C["Velocidad: cambio de r por unidad de tiempo"]
    C --> D["Aceleración: cambio de v por unidad de tiempo"]
    D --> E["Comprobación: unidades y signo"]
```

*Descripción textual:* se fija un marco; se miden posiciones en instantes; la velocidad es el cambio de posición dividido por el tiempo; la aceleración es el cambio de velocidad dividido por el tiempo; se comprueban unidades y signos.

Una analogía: el cuentakilómetros y la aguja de un velocímetro. El primero acumula distancia, el segundo da la rapidez de cada instante. El límite: ninguno de los dos informa de la dirección, y por eso en física se usan vectores.

## 8. La explicación, paso a paso

### 8.1 Marco y posición

Dibuja el marco antes que nada: **centro de la Tierra** como origen, ejes `x` e `y` en el plano orbital y metros como unidad. Es un marco que no gira con la Tierra (inercial en esta aproximación, sección 10). Un satélite a 400 km sobre el ecuador está en `r = (6 778 137 m, 0)` en el instante inicial, con `R = 6 378 137 m` tomado de S1.

### 8.2 Velocidad media e instantánea

Si entre `t₁` y `t₂` la posición cambia `Δr`, la velocidad media es `v̄ = Δr/Δt`, con unidad m/s. Cuando haces `Δt` más pequeño, `v̄` se acerca a la velocidad instantánea. Numéricamente, se usa la **diferencia centrada**: `v(t) ≈ [r(t+Δt) − r(t−Δt)] / (2Δt)`, más exacta que la hacia delante.

### 8.3 Aceleración

La aceleración es `a = Δv/Δt`. Con tres posiciones consecutivas puedes estimarla: `a(t) ≈ [r(t+Δt) − 2r(t) + r(t−Δt)] / Δt²`. Su dimensión es `L T⁻²` y su signo depende del sentido positivo del eje. Una consecuencia importante: **frenar y acelerar son lo mismo** en el sentido de que ambos cambian `v`; solo difiere si el cambio apunta con la velocidad o contra ella.

### 8.4 Trayectoria curva: acelerar sin cambiar la rapidez

Si la rapidez es constante pero la dirección cambia, `v` cambia y por tanto hay aceleración. Para una circunferencia de radio `r` con rapidez `v`, la aceleración apunta al centro y vale `a = v²/r`. Para el satélite ideal, con `v = 7668,6 m/s` y `r = 6 778 137 m`, `a = 8,676 m/s²`. Eso es el 88 % de la aceleración estándar `g_n = 9,806 65 m/s²` (S2): a 400 km la gravedad sigue siendo grande. Lo que hace «flotar» a los astronautas no es la ausencia de gravedad, sino estar en caída libre (se explica en C04).

### 8.5 Cuándo fallan las diferencias finitas

Con `Δt` muy grande la diferencia finita ya no representa el instante; con `Δt` muy pequeño, el ruido de la medición domina. En la sección 17 verás que con `Δt = 1000 s` la aceleración calculada tiene un 10 % de error en una órbita de 5554 s, y con `Δt = 1 s` es de 10⁻⁷.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Magnitud | Dimensión | Unidad SI | Valor o nota |
|---|---|---|---|---|
| `r` | posición (vector) | L | m | origen: centro de la Tierra |
| `Δr` | desplazamiento | L | m | — |
| `v` | velocidad (vector) | L T⁻¹ | m/s | rapidez = módulo |
| `a` | aceleración (vector) | L T⁻² | m/s² | — |
| `ω` | velocidad angular | T⁻¹ | rad/s | `v = ω r` en círculo |
| `GM` | parámetro gravitatorio | L³ T⁻² | m³/s² | 3,9860 × 10¹⁴ (S1) |
| `g_n` | aceleración estándar | L T⁻² | m/s² | 9,806 65 (S2) |

## 10. Convenciones y referencias

Tomamos un marco geocéntrico con ejes fijos respecto de las estrellas lejanas; la rotación de la Tierra queda fuera. Es una aproximación válida para describir el movimiento del satélite durante unas órbitas, pero no incluye el movimiento de la Tierra alrededor del Sol. Los ángulos se miden en radianes. Los datos del satélite ideal son **sintéticos**.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA NSSDC, *Earth Fact Sheet* (act. 15-nov-2024) | https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html | Radio ecuatorial 6378,137 km; GM = 0,39860 × 10⁶ km³/s²; gravedad media 9,820 m/s² | Página consultada el 2026-11-05 |
| S2 | NIST, CODATA 2022, «standard acceleration of gravity» | https://physics.nist.gov/cgi-bin/cuu/Value?gn | `g_n = 9,806 65 m/s²` exacto | Página consultada el 2026-11-05 |
| S3 | NASA, «Space Station Facts and Figures» | https://www.nasa.gov/international-space-station/space-station-facts-and-figures/ | 16 órbitas por día, una cada ~90 min; rapidez ~5 mi/s | Página consultada el 2026-11-05 |

Límites: las ecuaciones de las secciones 8.2–8.4 son cinemática estándar y se contrastan numéricamente en el laboratorio contra la solución analítica; no se citan de un texto concreto.

## 12. Cómo ver el movimiento

Esta tabla es la versión accesible de una gráfica de `x(t)` e `y(t)` del satélite ideal (datos sintéticos).

| t (s) | x (m) | y (m) |
|---|---|---|
| 0 | 6 778 137 | 0 |
| T/4 ≈ 1388 | ≈ 0 | 6 778 137 |
| T/2 ≈ 2777 | −6 778 137 | ≈ 0 |
| 3T/4 ≈ 4165 | ≈ 0 | −6 778 137 |

Si graficas, rotula ejes con unidad y usa marcadores distintos para `x` e `y`. Descripción larga: ambas son ondas senoidales desfasadas un cuarto de ciclo; juntas dibujan una circunferencia.

## 13. Ejemplo trabajado: velocidad y aceleración desde posiciones

**Planteamiento.** Con la posición del satélite ideal en `t = 1234,5 s` y a ± 1 s, estimar `v` y `a`.

**Paso 1 · Datos sintéticos.** `r(t) = r₀(cos ωt, sin ωt)`, con `r₀ = 6 778 137 m` y `ω = 1,1314 × 10⁻³ rad/s` (de `ω = √(GM/r₀³)`).

**Paso 2 · Velocidad.** Con la diferencia centrada y `Δt = 1 s`: `v = 7668,552 m/s`. El valor analítico `ω r₀` es `7668,554 m/s`: coinciden a 10⁻⁷ relativo.

**Paso 3 · Aceleración.** Con la segunda diferencia: `a = 8,6759 m/s²`, que coincide con `ω² r₀`.

**Paso 4 · Sentido físico.** La velocidad es perpendicular al vector posición, y la aceleración apunta al origen. Una rapidez constante con aceleración distinta de cero es la huella de una trayectoria curva.

## 14. Comparación de métodos

**Cálculo exacto** (derivar una fórmula) exige conocer `r(t)`. **Diferencias finitas** funcionan con una tabla de datos, pero dependen del paso. **Ajuste de una curva** a muchos puntos reduce el ruido, a costa de suponer una forma. Para datos medidos con ruido, un ajuste suele ser preferible a derivar punto a punto; para datos exactos, bastan las diferencias centradas.

## 15. Práctica guiada

**Ejercicio 1.** Un satélite pasa de `x = 0` a `x = 15 000 m` en 2 s en línea recta. Halla la velocidad media. *Pasos:* `Δx/Δt` (sección 8.2).

<details><summary>Solución comentada</summary>

`15 000 m / 2 s = 7500 m/s`. Su unidad es m/s; el signo positivo indica sentido +x.
</details>

**Ejercicio 2.** Si la velocidad pasa de 100 m/s a 130 m/s en 6 s, ¿cuál es la aceleración media? *Pista:* `Δv/Δt`.

<details><summary>Solución comentada</summary>

`(130 − 100)/6 = 5 m/s²`. Si la velocidad hubiera bajado, saldría negativa; eso indica frenado en el sentido +x.
</details>

**Ejercicio 3.** Un cuerpo recorre una circunferencia de radio 100 m a 20 m/s. ¿Qué aceleración tiene? (sección 8.4)

<details><summary>Solución comentada</summary>

`a = v²/r = 400/100 = 4 m/s²`, dirigida al centro. La rapidez es constante; el vector velocidad no.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Un tren avanza 40 km al este y luego 30 km al norte. ¿Distancia recorrida y módulo del desplazamiento?

<details><summary>Solución comentada</summary>

Recorrido: 70 km. Desplazamiento: `√(40² + 30²) = 50 km`. No son iguales: el camino no es recto.
</details>

**Ejercicio 5.** Convierte 7,67 km/s a km/h (C01) y verifica que ronda los 27 600 km/h.

<details><summary>Solución comentada</summary>

`7,67 × 3600 = 27 612 km/h`. Coherente con «unos 5 mi/s» de S3 (≈ 28 900 km/h con redondeo).
</details>

**Ejercicio 6.** Un satélite ideal recorre `2π r` con `r = 6 778 137 m` en `T = 5553,6 s`. ¿Qué rapidez media tiene? ¿Y su velocidad media vectorial en un período completo?

<details><summary>Solución comentada</summary>

Rapidez: `2π(6 778 137)/5553,6 = 7668,6 m/s`. Velocidad media vectorial: el desplazamiento tras una vuelta es cero, así que `v̄ = 0`. La rapidez media y el módulo de la velocidad media no coinciden.
</details>

**Ejercicio 7.** Con `a = v²/r`, ¿qué fracción de `g_n` es la aceleración del satélite ideal?

<details><summary>Solución comentada</summary>

`8,676/9,806 65 = 0,885`. Ejemplo de por qué «microgravedad» no significa «sin gravedad».
</details>

**Ejercicio 8.** Usa la diferencia centrada con `x(1) = 4,9`, `x(3) = 44,1` (metros) para estimar `v(2)`.

<details><summary>Solución comentada</summary>

`(44,1 − 4,9)/(3 − 1) = 19,6 m/s`. Es la velocidad de un cuerpo en caída libre a 2 s con `g ≈ 9,8`: encaja con `v = g t`.
</details>

**Ejercicio 9 · transferencia.** Un artículo dice «la ISS no acelera porque su rapidez es constante». Corrígelo.

<details><summary>Solución comentada</summary>

Aceleración es cambio de velocidad vectorial; en una órbita circular la dirección cambia, por lo que acelera hacia el centro con `v²/r` (sección 8.4).
</details>

**Ejercicio 10 · transferencia.** Con `Δt = 1000 s` la diferencia finita da `a = 7,79 m/s²` en vez de `8,68`. Explica por qué falla.

<details><summary>Solución comentada</summary>

El paso es una sexta parte del período: la curva ya no se parece a una parábola en ese intervalo, y la segunda diferencia subestima la curvatura. Hay que usar `Δt ≪ T` (sección 8.5).
</details>

**Ejercicio 11 · transferencia.** Un compañero afirma «a 400 km no hay gravedad». ¿Qué dato de esta clase lo contradice?

<details><summary>Solución comentada</summary>

La aceleración centrípeta necesaria para la órbita (8,68 m/s²) es la aceleración debida a la gravedad en ese radio; es el 88 % de `g_n`. La sensación de ingravidez viene de que todo cae a la vez.
</details>

**Ejercicio 12 · integrador.** Elabora una *ficha de movimiento* (sección 20) con una tabla de seis posiciones sintéticas de un cuerpo en un círculo de radio 100 m a 20 m/s; deduce `v`, `a` y su relación `a = v²/r` con unidades y marco.

<details><summary>Solución modelo</summary>

Debe fijar marco (origen en el centro, ejes `x`, `y`), calcular `v` por diferencia centrada, `a` por segunda diferencia, comprobar `a ≈ 4 m/s²` y `v ≈ 20 m/s`, y declarar el paso usado y el error frente al valor analítico.
</details>

## 17. Laboratorio: velocidad y aceleración numéricas

El script [cinematica_numerica.py](cinematica_numerica.py) genera posiciones sintéticas de la órbita ideal y estima `v` y `a` con diferencias finitas. Antes comprueba contra la solución analítica (`ω r`, `ω² r`) con tolerancias de 10⁻⁵ y 10⁻³, y que `v` sea perpendicular a `r` y `a` antiparalela a `r`.

**Datos:** sintéticos, con GM y R de S1. **Predice antes de ejecutar:** ¿con qué paso el error de la aceleración deja de ser despreciable? **Resultados (2026-11-05, Python 3.12.9):** `ω = 1,131366 × 10⁻³ rad/s`, `T = 5553,6 s`; `v = 7668,552 m/s` (analítica 7668,554); `a = 8,6759 m/s²` (analítica igual). Error relativo de `a`: `1,6 × 10⁻⁶` con `Δt = 0,01 s`, `1,1 × 10⁻⁷` con 1 s, `1,1 × 10⁻³` con 100 s y `0,10` con 1000 s.

```bash
python programa/clases/B05/B05-C02-posicion-velocidad-y-aceleracion/cinematica_numerica.py
```

**Límites:** los datos no tienen ruido; con datos reales, el error de medida limita el paso útil.

## 18. Errores frecuentes y cómo corregirlos

**Confundir rapidez y velocidad.** Ejercicio 6. **Creer que sin cambio de rapidez no hay aceleración.** Ejercicio 9. **Mezclar distancia y desplazamiento.** Ejercicio 4. **Olvidar el signo y el marco.** Ejercicio 2. **Derivar con un paso demasiado grande.** Ejercicio 10.

## 19. Cómo sabrás que vas bien

Tras 8.2: ¿diferencias velocidad media e instantánea? Repite el ejercicio 1 con otro intervalo. Tras 8.4: ¿por qué hay aceleración si la rapidez es constante? Si no lo explicas, rehaz el ejercicio 3. Tras el laboratorio: ¿qué paso elegirías y por qué? Si dudas, relee 8.5.

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de movimiento**: marco declarado, tabla de posiciones, `v` y `a` con unidad, comprobación contra una referencia y límites del método.

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Marco y unidades | Ausentes | Parciales | Completos | Verifica dimensionalmente |
| Cálculo de `v` y `a` | Erróneo | Con ayuda | Correcto | Analiza el efecto del paso |
| Interpretación | No interpreta | Describe | Explica `a = v²/r` | Relaciona con ingravidez |
| Fuentes y alcance | Sin fuente | Fuente sin alcance | Con alcance | Distingue sintético de observado |

**Condiciones críticas:** no omitir marco ni unidades; rotular los datos como sintéticos; citar solo lo consultado.

## 21. Ética, seguridad y límites

Una descripción de movimiento sin marco es una invitación al error; es una práctica de honestidad y seguridad. Esta clase es educativa: no sirve para determinar órbitas ni maniobras reales. Accesibilidad: ecuaciones en texto, tablas equivalentes de las gráficas, funciona sin conexión.

## 22. Para cerrar y seguir

Posición, velocidad y aceleración son vectores definidos en un marco; la velocidad es el ritmo de cambio de la posición y la aceleración el de la velocidad; una trayectoria curva implica aceleración. Queda abierto cómo describir los casos más sencillos con fórmulas: lo harás en C03.

**Glosario español–inglés.** posición · *position*; desplazamiento · *displacement*; velocidad · *velocity*; rapidez · *speed*; aceleración · *acceleration*; marco de referencia · *reference frame*.

**Continuidad.** B05-C03 usa tu capacidad de **calcular `v` y `a` en un marco declarado** para escribir las fórmulas del movimiento rectilíneo y del circular.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B05-C01 — Magnitudes físicas y dimensiones](../B05-C01-magnitudes-fisicas-y-dimensiones/CLASE.md) · [📚 Bloque B05](../../../tronco-comun/B05-fisica-fundamental-para-el-espacio.md) · [Siguiente: B05-C03 — Movimiento rectilíneo y circular →](../B05-C03-movimiento-rectilineo-y-circular/CLASE.md)
<!-- /nav -->
