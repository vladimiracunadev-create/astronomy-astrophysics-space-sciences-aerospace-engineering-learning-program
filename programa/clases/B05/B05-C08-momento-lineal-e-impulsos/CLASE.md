# B05-C08 — Momento lineal e impulsos

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B05](../../../tronco-comun/B05-fisica-fundamental-para-el-espacio.md) · [← Anterior: B05-C07 — Conservación de energía mecánica](../B05-C07-conservacion-de-energia-mecanica/CLASE.md) · [Siguiente: B05-C09 — Momento angular y torque →](../B05-C09-momento-angular-y-torque/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Octava clase de B05 y cierre de su segundo tramo (dinámica y energía de la partícula). La energía te dijo *cuánto*; el momento lineal te dice *cómo se reparte el movimiento* cuando algo se expulsa o dos cuerpos interactúan. Nivel N1; usas `ΣF = m a` (C04) y logaritmos naturales (B04). No verás la relatividad ni los choques en 2D con detalle.

## 2. Por qué esta clase existe

Un cohete en el vacío no tiene nada contra lo que empujar y aun así acelera. La pregunta motivadora es: **¿cómo cambia la velocidad de un cuerpo cuando expulsa masa o cuando choca, si no hay fuerzas externas?** La decisión central es identificar el **sistema** cuyo momento total se conserva y escribir el balance antes y después.

## 3. Lo que podrás hacer al terminar

1. Definir momento lineal e impulso y relacionarlos con `ΣF = m a`.
2. Enunciar la conservación del momento de un sistema aislado.
3. Resolver un acoplamiento (choque perfectamente inelástico) en una recta.
4. Deducir que expulsar masa produce aceleración y obtener `Δv = v_e ln(m₀/m_f)`.
5. Distinguir qué se conserva (momento) de qué no (energía cinética en choques inelásticos).
6. Calcular el cambio de velocidad de un impulso de un propulsor.

La evidencia es la **hoja de momento e impulso** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué aceleración da una fuerza de 50 N a 1000 kg?
2. ¿Cuánto vale `ln(2)`? (≈ 0,693)
3. Si un cuerpo de 3 kg va a 4 m/s, ¿cuánto vale `m v`?
4. ¿Qué dimensión tiene `N·s`? (C01)
5. ¿Qué es un sistema aislado?

<details>
<summary>Ver respuestas</summary>

1. 0,05 m/s². 2. 0,693. 3. 12 kg·m/s. 4. `M L T⁻¹`. 5. Uno sobre el que no actúan fuerzas externas netas.
</details>

Con cuatro o cinco aciertos, sigue; con menos, repasa C01 y C04.

## 5. Un caso real: la masa de la ISS y los acoplamientos

NASA indica que la estación pesa unos 419 725 kg y da 16 órbitas por día (S1). Cuando una nave se acopla a una estación así, la nave llega con una pequeña velocidad relativa y, al unirse, el conjunto adopta una velocidad común dictada por la conservación del momento. Con una masa de 419 725 kg, un aporte de unos cientos de kilogramos cambia la velocidad del conjunto una cantidad minúscula. No usamos aquí datos de un acoplamiento real: el caso sintético del laboratorio lo ilustra con otras masas. Límite: S1 solo proporciona la masa; no describe maniobras.

## 6. Vocabulario

El **momento lineal** (cantidad de movimiento) de un cuerpo es `p = m v`, vector en `kg·m/s`. El **impulso** de una fuerza es `J = ∫ F dt` (o `F Δt` si `F` es constante), en `N·s`; `1 N·s = 1 kg·m/s`. El **teorema impulso–momento** dice `J_neto = Δp`. Un **sistema aislado** no recibe fuerzas externas netas. Un **choque perfectamente inelástico** es aquel en que los cuerpos quedan unidos. La **velocidad de escape de gases** `v_e` es la rapidez con que el propelente sale, medida respecto del cohete. El **empuje** es `E = ṁ v_e`, con `ṁ` el flujo de masa expulsada.

## 7. Modelo mental: lo que no se pierde al repartirse

El momento total de un sistema aislado es una cantidad que solo se reparte. Si algo sale hacia atrás, el resto se mueve hacia delante.

```mermaid
flowchart LR
    A["Antes: m, v"] --> B["Se expulsa una masa dm con velocidad relativa v_e"]
    B --> C["Después: nave (m − dm) con v + dv, gas dm"]
    C --> D["Momento total antes = momento total después"]
    D --> E["dv = v_e dm / m"]
    E --> F["Suma de muchos pasos: Δv = v_e ln(m0 / mf)"]
```

*Descripción textual:* un cohete de masa `m` expulsa una pequeña masa `dm` hacia atrás; se escribe que el momento total antes y después es el mismo; de ahí sale el pequeño aumento de velocidad `dv = v_e dm/m`; al sumar muchos pasos aparece el logaritmo.

Una analogía: un patinador sobre hielo que lanza una mochila pesada hacia atrás y avanza. El límite: el patinador empuja el hielo, que aporta fricción; en el vacío solo cuenta el reparto entre nave y gases.

## 8. La explicación, paso a paso

### 8.1 Momento e impulso

Con `F = m a = m Δv/Δt` y masa constante, `F Δt = m Δv = Δp`. El lado izquierdo es el impulso: **una fuerza pequeña durante mucho tiempo da el mismo cambio de momento que una grande durante poco**. Ejemplo con el satélite ideal: un propulsor de 50 N durante 120 s entrega `J = 6000 N·s`, y a 1000 kg le cambia la velocidad `Δv = 6,0 m/s` (si se desprecia la masa expulsada).

### 8.2 Conservación en un sistema aislado

Si `ΣF_externas = 0`, entonces `Δp_total = 0`: el momento total antes es igual al total después. Dentro del sistema las fuerzas son de acción y reacción (C04), así que el momento que gana un cuerpo lo pierde otro. Es una ley vectorial: se conserva por componentes.

### 8.3 Choque perfectamente inelástico

Dos cuerpos que se unen, en una recta: `m₁v₁ + m₂v₂ = (m₁ + m₂) v_f`. Con `m₁ = 2000 kg` a `+1,0 m/s` y `m₂ = 500 kg` a `−0,5 m/s`: `v_f = (2000 − 250)/2500 = 0,70 m/s`. La energía cinética pasa de `1062,5 J` a `612,5 J`: se pierden `450 J` en deformación y calor. El momento se conserva siempre (en un sistema aislado); la energía cinética, no.

### 8.4 El cohete: expulsar masa

En el instante `t`, la nave de masa `m` va con velocidad `v`. Expulsa `dm` con velocidad `v_e` hacia atrás respecto de ella; su velocidad pasa a `v + dv`. El momento antes es `m v`; después, `(m − dm)(v + dv) + dm (v + dv − v_e)`. Igualando y despejando: `dv = v_e dm/m`. Sumando todos los pasos mientras la masa baja de `m₀` a `m_f`:

`Δv = v_e ln(m₀/m_f)`.

Con `m₀ = 1000 kg`, `m_f = 400 kg` y `v_e = 3000 m/s` (todo **sintético**), `Δv = 2748,9 m/s`. Con un solo paquete expulsado se obtendría solo `1800 m/s`; con 10 000 paquetes se llega a `2748,7`. Dos consecuencias: el `Δv` crece solo **logarítmicamente** con la razón de masas, y es **proporcional** a `v_e`.

### 8.5 Dominio de validez

La fórmula supone una recta, sin gravedad ni atmósfera, `v_e` constante y velocidades mucho menores que `c`. En el espacio real se aplica por tramos a cada maniobra, pero esta clase solo enseña la idea; no sirve para dimensionar un cohete ni una misión.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Magnitud | Dimensión | Unidad SI | Valor o nota |
|---|---|---|---|---|
| `p` | momento lineal | M L T⁻¹ | kg·m/s | `m v` |
| `J` | impulso | M L T⁻¹ | N·s | `F Δt` |
| `v_e` | velocidad de los gases | L T⁻¹ | m/s | sintética: 3000 |
| `ṁ` | flujo de masa | M T⁻¹ | kg/s | — |
| `m₀`, `m_f` | masa inicial y final | M | kg | — |
| `Δv` | cambio de velocidad | L T⁻¹ | m/s | `v_e ln(m₀/m_f)` |

## 10. Convenciones y referencias

Una dimensión (recta), sentido positivo declarado, sistema aislado. Todos los valores numéricos de masa, `v_e` y acoplamiento son **sintéticos**; solo la masa de la ISS se cita (S1) para dar escala. No se comparan con motores reales porque no se consultó una fuente de propulsión.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA, «Space Station Facts and Figures» | https://www.nasa.gov/international-space-station/space-station-facts-and-figures/ | Masa de la ISS 419 725 kg; 16 órbitas diarias | Página consultada el 2026-11-05 |

Límites: la ecuación del cohete y la conservación del momento son resultados clásicos deducidos aquí y verificados numéricamente en el laboratorio; no se cita un texto ni un dato de propulsión real.

## 12. Cómo ver el momento

Tabla accesible de un gráfico de `Δv` frente a la razón de masas con `v_e = 3000 m/s` (datos sintéticos, cálculo propio).

| `m₀/m_f` | `ln(m₀/m_f)` | `Δv` (m/s) |
|---|---|---|
| 1,5 | 0,405 | 1216 |
| 2,5 | 0,916 | 2749 |
| 5 | 1,609 | 4828 |
| 10 | 2,303 | 6908 |

Descripción larga: una curva creciente que se aplana; duplicar la razón de masas añade siempre el mismo `Δv` (`v_e ln 2 = 2079 m/s`), no el doble.

## 13. Ejemplo trabajado: el acoplamiento y el empuje del satélite

**Planteamiento.** (a) Un módulo de 500 kg se acopla a un satélite de 2000 kg; ¿qué velocidad común resulta? (b) El propulsor de 50 N del satélite actúa 120 s; ¿qué `Δv`?

**Paso 1 · Sistema y marco.** (a) Sistema aislado de los dos cuerpos en una recta; sentido positivo el del satélite. (b) El satélite con su propulsor, ignorando la masa expulsada.

**Paso 2 · Acoplamiento.** `v_f = (2000 × 1,0 + 500 × (−0,5))/2500 = 0,7000 m/s`.

**Paso 3 · Impulso.** `J = F Δt = 50 × 120 = 6000 N·s`; con `m = 1000 kg`, `Δv = J/m = 6,0 m/s`.

**Paso 4 · Sentido físico.** En (a) se conservó el momento (`1750 kg·m/s`) y se disipó la energía (`450 J`). En (b) el `Δv` es pequeño frente a los 7668,6 m/s de la órbita (0,08 %), pero basta para cambiar lentamente la trayectoria; la clase C20 retomará esa idea.

## 14. Comparación de métodos

**Impulso–momento** responde «cuánto cambia la velocidad» para fuerzas que actúan un tiempo; **energía** responde por estados y es inútil si hay disipación; **ecuación del cohete** es el caso especial con masa variable. Para choques conviene el momento; para saber cuánta energía se disipó, la diferencia de energías cinéticas.

## 15. Práctica guiada

**Ejercicio 1.** Calcula el momento del satélite ideal (1000 kg, 7668,6 m/s). *Pasos:* `p = m v`.

<details><summary>Solución comentada</summary>

`p = 1000 × 7668,6 = 7,6686 × 10⁶ kg·m/s`, tangente a la órbita. Aunque `|p|` es constante, el vector cambia de dirección, porque la gravedad ejerce un impulso.
</details>

**Ejercicio 2.** Una fuerza de 200 N actúa 3 s sobre 50 kg inicialmente en reposo. ¿Qué velocidad final? *Pista:* `J = Δp`.

<details><summary>Solución comentada</summary>

`J = 600 N·s`; `Δv = 600/50 = 12 m/s`.
</details>

**Ejercicio 3.** Un módulo de 400 kg a 0,5 m/s se acopla a otro de 600 kg en reposo. ¿Velocidad común?

<details><summary>Solución comentada</summary>

`v_f = (400 × 0,5)/(1000) = 0,2 m/s`. Energía inicial `50 J`, final `20 J`: se disipan `30 J`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Convierte `1 N·s` a `kg·m/s` y verifica dimensionalmente `J = Δp`.

<details><summary>Solución comentada</summary>

`N·s = kg·m/s² · s = kg·m/s`. Ambos lados son `M L T⁻¹`.
</details>

**Ejercicio 5.** Con `v_e = 3000 m/s`, ¿qué `Δv` da `m₀/m_f = 2`? ¿Y 4?

<details><summary>Solución comentada</summary>

`3000 ln 2 = 2079 m/s`; `3000 ln 4 = 4159 m/s`: duplicar la razón añade 2079 m/s, no duplica el `Δv`.
</details>

**Ejercicio 6.** ¿Qué razón de masas hace falta para `Δv = 7668,6 m/s` con `v_e = 3000 m/s`?

<details><summary>Solución comentada</summary>

`m₀/m_f = e^{7668,6/3000} = e^{2,556} = 12,9`: casi el 92 % de la masa inicial sería propelente. Es un cálculo sintético que muestra por qué se usan varias etapas, tema posterior.
</details>

**Ejercicio 7.** Dos cuerpos de 1000 kg se acercan a 1,0 m/s cada uno en sentidos opuestos y se unen. ¿Velocidad final y energía disipada?

<details><summary>Solución comentada</summary>

`v_f = 0`; energía inicial `2 × 500 = 1000 J`, final `0`: se disipan `1000 J`.
</details>

**Ejercicio 8.** Un propulsor da 2,0 N durante 1000 s sobre 500 kg. ¿`Δv`?

<details><summary>Solución comentada</summary>

`J = 2000 N·s`, `Δv = 4,0 m/s` (masa constante). Si la masa cambiara, habría que usar la ecuación del cohete.
</details>

**Ejercicio 9 · transferencia.** Un artículo dice «el cohete avanza porque sus gases empujan contra el aire». Corrígelo.

<details><summary>Solución comentada</summary>

Avanza por la conservación del momento: expulsa masa hacia atrás y el resto se mueve hacia delante; funciona en el vacío (sección 8.4). El aire no es necesario.
</details>

**Ejercicio 10 · transferencia.** El laboratorio da `Δv = 1800 m/s` con un solo paquete y `2748,7 m/s` con 10 000. ¿Qué enseña?

<details><summary>Solución comentada</summary>

Que la masa expulsada al principio «pesa» más: los paquetes tardíos mueven una nave más ligera. Expulsar de golpe da menos `Δv` que expulsar gradualmente; el límite continuo es el logaritmo.
</details>

**Ejercicio 11 · transferencia.** Un compañero conserva «energía cinética» en un acoplamiento. ¿Qué error comete?

<details><summary>Solución comentada</summary>

En un choque perfectamente inelástico solo se conserva el momento; la energía cinética disminuye (ejercicio 3). Conserva lo que corresponde al caso, no lo que le resulta más cómodo.
</details>

**Ejercicio 12 · integrador.** Elabora una *hoja de momento e impulso* (sección 20) para una nave sintética que expulsa propelente en un solo `Δv`: datos, razón de masas, `Δv`, verificación numérica con paquetes y límites.

<details><summary>Solución modelo</summary>

Debe fijar `m₀`, `m_f`, `v_e` (rotulados sintéticos), calcular `Δv`, comprobar con 100 y 10 000 paquetes y declarar el dominio (recta, sin gravedad, `v_e` constante).
</details>

## 17. Laboratorio: cohete discreto y acoplamiento

El script [cohete_y_momento.py](cohete_y_momento.py) expulsa la masa en `N` paquetes conservando el momento en cada paso y compara con la ecuación de Tsiolkovsky; calcula también un acoplamiento. Antes comprueba que, con 10 000 paquetes, el error sea menor que 0,1 %, y que el momento se conserve en el acoplamiento.

**Datos:** sintéticos. **Predice antes de ejecutar:** ¿el error baja al aumentar `N`? **Resultados (2026-11-05, Python 3.12.9):** `Δv` analítico `2748,87 m/s` (`m₀/m_f = 2,50`, `v_e = 3000 m/s`). Numérico: `N = 1` → `1800,00` (error 3,45 × 10⁻¹); `N = 10` → `2618,58` (4,74 × 10⁻²); `N = 100` → `2735,42` (4,89 × 10⁻³); `N = 10 000` → `2748,74` (4,91 × 10⁻⁵). Acoplamiento: `v = 0,7000 m/s`; energía cinética de `1062,50 J` a `612,50 J` (se disipan `450,00 J`).

```bash
python programa/clases/B05/B05-C08-momento-lineal-e-impulsos/cohete_y_momento.py
```

**Límites:** modelo unidimensional con datos inventados; no dimensiona cohetes ni valida motores.

## 18. Errores frecuentes y cómo corregirlos

**Pensar que un cohete necesita aire.** Ejercicio 9. **Conservar energía cinética en un choque inelástico.** Ejercicio 11. **Olvidar el signo del sentido.** Ejercicio 3. **Creer que `Δv` crece linealmente con la razón de masas.** Ejercicio 5. **Usar la fórmula con gravedad o atmósfera sin declararlo.** Sección 8.5.

## 19. Cómo sabrás que vas bien

Tras 8.2: ¿puedes escribir el balance de momento de un acoplamiento? Rehaz el ejercicio 3. Tras 8.4: ¿por qué sale un logaritmo? Revisa el ejercicio 10. Tras el laboratorio: ¿qué cambia al aumentar los paquetes? Lee la cabecera.

## 20. Qué entregas y cómo se evalúa

El producto es tu **hoja de momento e impulso**: sistema, balance antes/después, resultado con unidades, verificación y límites.

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Sistema y balance | Ausentes | Parciales | Correctos | Justifica el aislamiento |
| Cálculo y unidades | Errores | Con ayuda | Correcto | Verificación dimensional |
| Verificación | Ninguna | Una | Numérica y analítica | Analiza convergencia |
| Alcance | No declara | Parcial | Declara | Distingue sintético de real |

**Condiciones críticas:** no usar datos sintéticos como reales; unidades; citar solo lo consultado.

## 21. Ética, seguridad y límites

La propulsión real implica riesgos (presión, combustibles, alta energía) que esta clase no cubre; no es una guía de diseño. Los números son sintéticos y la simulación es educativa; no certifica vuelo ni seguridad. Accesibilidad: ecuaciones en texto, tablas equivalentes, sin conexión.

## 22. Para cerrar y seguir

El momento lineal se conserva en sistemas aislados; el impulso cambia el momento; expulsar masa acelera la nave según un logaritmo de la razón de masas; la energía cinética no se conserva en choques inelásticos. Queda abierto cómo aplican estas ideas al *giro*: el momento angular y el torque (C09).

**Glosario español–inglés.** momento lineal · *linear momentum*; impulso · *impulse*; sistema aislado · *isolated system*; choque inelástico · *inelastic collision*; empuje · *thrust*; ecuación del cohete · *rocket equation*.

**Continuidad.** B05-C09 usa tu capacidad de **plantear un balance de una cantidad conservada** para estudiar el momento angular y los giros de un satélite.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B05-C07 — Conservación de energía mecánica](../B05-C07-conservacion-de-energia-mecanica/CLASE.md) · [📚 Bloque B05](../../../tronco-comun/B05-fisica-fundamental-para-el-espacio.md) · [Siguiente: B05-C09 — Momento angular y torque →](../B05-C09-momento-angular-y-torque/CLASE.md)
<!-- /nav -->
