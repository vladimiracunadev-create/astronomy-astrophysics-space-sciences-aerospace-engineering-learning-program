# B05-C16 — Corriente y circuitos elementales

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B05](../../../tronco-comun/B05-fisica-fundamental-para-el-espacio.md) · [← Anterior: B05-C15 — Campos eléctricos](../B05-C15-campos-electricos/CLASE.md) · [Siguiente: B05-C17 — Campos magnéticos →](../B05-C17-campos-magneticos/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Decimosexta clase de B05. En C15 las cargas estaban quietas; ahora **fluyen** por un conductor y transportan energía hacia los equipos. Nivel N1. Usas campo y potencial (C15), potencia (C06) y álgebra de primer grado (B04). No verás todavía corriente alterna, semiconductores ni electrónica de potencia.

## 2. Por qué esta clase existe

Un satélite recibe energía del Sol mediante paneles, la guarda en baterías y la reparte a equipos; si el cálculo está mal, la nave se apaga en el eclipse. La pregunta motivadora es: **¿cómo calcular corrientes, tensiones y potencias en una red de componentes y cuánta energía debe guardarse para pasar un eclipse?** La decisión central es plantear las leyes de Kirchhoff y la de Ohm, y comprobar con un balance de potencia que no se creó ni se perdió energía.

## 3. Lo que podrás hacer al terminar

1. Definir corriente, tensión y resistencia, con unidades.
2. Aplicar la ley de Ohm y la potencia `P = V I`.
3. Combinar resistencias en serie y en paralelo.
4. Resolver una red simple con las leyes de Kirchhoff y el análisis nodal.
5. Verificar un resultado con el balance de potencia.
6. Estimar un presupuesto de energía con eclipse para un satélite ideal.

La evidencia es la **hoja de circuito y presupuesto de energía** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué unidad tiene la potencia? (C06)
2. Resuelve `12 = 4 I`.
3. ¿Cuánto es `1/6 + 1/12`?
4. ¿Qué es un flujo de energía por unidad de área? (C13)
5. ¿Qué es una diferencia de potencial? (C15)

<details>
<summary>Ver respuestas</summary>

1. Vatio (J/s). 2. `I = 3`. 3. `0,25`. 4. W/m². 5. La energía por unidad de carga que se gana o se pierde al mover una carga entre dos puntos.
</details>

Con cuatro o cinco aciertos, sigue; con menos, repasa C06 y C15.

## 5. Un caso real: el flujo de energía que llega al panel

Con la luminosidad del Sol, 382,8 × 10²⁴ W (S1), y el semieje mayor de la órbita terrestre, 149,598 × 10⁶ km (S2), el flujo solar a 1 au resulta `1361,2 W/m²` (lo calculas en C13). Un panel solar convierte una fracción de esa potencia en electricidad; con datos **sintéticos** (10 m² y 28 % de eficiencia) producirá unos `3811 W` con el Sol de frente. Pero un satélite en órbita baja pasa parte de cada vuelta en la sombra de la Tierra, y entonces solo funciona con batería. Límite: no se consultaron datos de paneles ni baterías reales; lo único publicado son los datos astronómicos.

## 6. Vocabulario

La **corriente eléctrica** `I` es la carga que atraviesa una sección por unidad de tiempo, `I = ΔQ/Δt`; se mide en amperios (`1 A = 1 C/s`). Con la carga elemental `e` exacta (S3), `1 A` equivale a `1/e = 6,2415 × 10¹⁸` cargas elementales por segundo. La **tensión** o diferencia de potencial `V` (voltios) es la energía por carga. La **resistencia** `R` (ohmios, Ω) mide la oposición al paso de corriente; la **ley de Ohm** dice `V = I R` para un conductor óhmico. La **potencia** eléctrica es `P = V I = I² R = V²/R`. Dos resistencias están **en serie** si las atraviesa la misma corriente y **en paralelo** si soportan la misma tensión. Las **leyes de Kirchhoff**: en un nodo, la suma de corrientes que entran es igual a la que sale; en un lazo cerrado, la suma de tensiones es cero. El **análisis nodal** resuelve las tensiones de los nodos.

## 7. Modelo mental: una red hidráulica

Piensa en tuberías: la tensión es la diferencia de presión, la corriente es el caudal y la resistencia es el estrechamiento. La energía que entrega la fuente se disipa en las resistencias.

```mermaid
flowchart LR
    A["Fuente: V"] --> B["R1 en serie"]
    B --> C["Nodo A"]
    C --> D["R2 a tierra"]
    C --> E["R3 hacia el nodo B"]
    E --> F["R4 a tierra"]
    D --> G["Retorno a la fuente"]
    F --> G
```

*Descripción textual:* la fuente alimenta una resistencia `R1` en serie que llega al nodo A; desde A salen dos ramas: `R2` directa a tierra y `R3` hacia el nodo B, que conecta con `R4` a tierra; ambas vuelven a la fuente.

Una analogía: el caudal de agua en una red de tuberías con distintos diámetros. El límite: en la hidráulica el agua se consume o se acumula; en un circuito estacionario la carga que entra por un nodo sale entera (ley de los nodos).

## 8. La explicación, paso a paso

### 8.1 Corriente, tensión y ley de Ohm

Una corriente de 2 A durante 3600 s transporta `7200 C`, es decir `4,49 × 10²²` cargas elementales. Con `V = 12 V` sobre `R = 4 Ω`, `I = 3 A` y `P = V I = 36 W`. Si la resistencia se duplica con la misma tensión, la corriente y la potencia se reducen a la mitad.

### 8.2 Serie y paralelo

En serie: `R_eq = R₁ + R₂` (misma corriente). En paralelo: `1/R_eq = 1/R₁ + 1/R₂` (misma tensión). Con `6 Ω` y `12 Ω` en paralelo, `R_eq = 4 Ω`, **menor** que la menor de ambas. En un divisor de tensión (4 Ω y 8 Ω en serie con 12 V), la tensión sobre los 8 Ω es `8 V`.

### 8.3 Kirchhoff y análisis nodal

En el circuito de la figura con `V = 12 V`, `R₁ = 4 Ω`, `R₂ = 6 Ω`, `R₃ = 6 Ω`, `R₄ = 12 Ω`, se escriben las ecuaciones de los nodos A y B: `(g₁ + g₂ + g₃) v_A − g₃ v_B = g₁ V` y `−g₃ v_A + (g₃ + g₄) v_B = 0`, con `g = 1/R`. Resolviendo: `v_A = 6,3529 V` y `v_B = 4,2353 V`; las corrientes son `I₁ = 1,4118 A`, `I₂ = 1,0588 A` y `I₃ = I₄ = 0,3529 A`. Comprobación con el método de serie y paralelo: `R₃ + R₄ = 18 Ω`, en paralelo con `R₂` da `4,5 Ω`, `R_eq = 8,5 Ω` y `I₁ = 12/8,5 = 1,4118 A`.

### 8.4 Balance de potencia

La fuente entrega `P = V I₁ = 16,941 W`; las resistencias disipan `I₁² R₁ + I₂² R₂ + I₃² R₃ + I₄² R₄ = 16,941 W`. Que ambas cifras coincidan es una prueba independiente de que las corrientes están bien; si no coinciden, hay un error. En un circuito real aparecen también pérdidas en cables, calor en componentes y eficiencia de convertidores.

### 8.5 Presupuesto de energía con eclipse

En una órbita circular de radio `r` y con el Sol muy lejos, la sombra de la Tierra es aproximadamente un cilindro de radio `R`. Para un plano orbital que contiene al Sol (`β = 0`), la fracción de la órbita en sombra es `f = arcsen(R/r)/π`. Para el satélite ideal (`r = 6 778 137 m`): `f = 0,3901`, es decir, 36,1 min de los 92,6 min de la órbita. Con una carga sintética de 2000 W, la batería debe aportar `4,333 × 10⁶ J = 1,204 kWh` por eclipse; el panel de 3811 W deja `1811 W` de exceso durante la fase iluminada, que suman `6,135 × 10⁶ J` (1,42 veces la energía del eclipse), suficiente en este modelo ideal. Esta cuenta ignora pérdidas de carga y descarga, degradación, orientación del panel y otros planos orbitales.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Magnitud | Dimensión | Unidad SI | Valor o nota |
|---|---|---|---|---|
| `I` | corriente | I | A | `1 A = 1 C/s` |
| `V` | tensión | M L² T⁻³ I⁻¹ | V | `J/C` |
| `R` | resistencia | M L² T⁻³ I⁻² | Ω | `V/I` |
| `g` | conductancia | M⁻¹ L⁻² T³ I² | S | `1/R` |
| `P` | potencia | M L² T⁻³ | W | `V I` |
| `S` | flujo solar | M T⁻³ | W/m² | 1361,2 a 1 au (cálculo con S1, S2) |
| `f` | fracción de la órbita en sombra | 1 | — | `arcsen(R/r)/π` |
| `e` | carga elemental | I T | C | 1,602 176 634 × 10⁻¹⁹ exacta (S3) |

## 10. Convenciones y referencias

Corriente convencional del terminal positivo al negativo por el circuito externo. Elementos óhmicos, régimen estacionario y corriente continua. Resistencias, tensiones, paneles y cargas son **sintéticos**; el flujo solar es un cálculo propio con datos publicados; el eclipse es un resultado de un modelo geométrico **simulado** (sombra cilíndrica, `β = 0`).

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA NSSDC, *Sun Fact Sheet* (act. 9-may-2024) | https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html | Luminosidad 382,8 × 10²⁴ W | Página consultada el 2026-11-05 |
| S2 | NASA NSSDC, *Earth Fact Sheet* (act. 15-nov-2024) | https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html | Semieje mayor 149,598 × 10⁶ km; radio ecuatorial 6378,137 km; GM | Página consultada el 2026-11-05 |
| S3 | BIPM, «SI defining constants» | https://www.bipm.org/en/measurement-units/si-defining-constants | `e = 1,602 176 634 × 10⁻¹⁹ C` exacta | Página consultada el 2026-11-05 |

Límites: las leyes de Ohm y Kirchhoff, el análisis nodal y la geometría de sombra son resultados clásicos que se enuncian o deducen aquí y se verifican con balance de potencia y casos límite; no se cita un texto. No se consultaron datos de paneles solares, baterías ni de ninguna misión.

## 12. Cómo ver el circuito

Tabla accesible de un esquema del circuito de la sección 8.3.

| Rama | Entre | Resistencia (Ω) | Corriente (A) | Tensión (V) |
|---|---|---|---|---|
| R1 | fuente — nodo A | 4 | 1,4118 | 5,6471 |
| R2 | nodo A — tierra | 6 | 1,0588 | 6,3529 |
| R3 | nodo A — nodo B | 6 | 0,3529 | 2,1176 |
| R4 | nodo B — tierra | 12 | 0,3529 | 4,2353 |

Descripción larga: un esquema con la fuente a la izquierda, `R1` en serie hacia el nodo A, y dos ramas desde A; la superior con `R2` a tierra, la inferior con `R3` y luego `R4` a tierra; las corrientes `I₂` e `I₃` suman `I₁` en el nodo A.

## 13. Ejemplo trabajado: ¿cuánta batería necesita el satélite ideal?

**Planteamiento.** Satélite ideal a 400 km con carga de 2000 W (sintética) y un panel de 10 m² al 28 % (sintético). ¿Qué energía debe guardar la batería para el eclipse y alcanza la recarga?

**Paso 1 · Flujo y panel.** `S = 1361,2 W/m²`; `P_panel = S × 10 × 0,28 = 3811 W`.

**Paso 2 · Eclipse.** `f = arcsen(6 378 137/6 778 137)/π = 0,3901`; con `T = 5553,6 s`, el eclipse dura `2166 s = 36,1 min`.

**Paso 3 · Batería.** `E = 2000 × 2166 = 4,333 × 10⁶ J = 1,204 kWh`.

**Paso 4 · Recarga.** En el sol sobran `1811 W` durante `3388 s`: `6,135 × 10⁶ J`, 1,42 veces `E`.

**Sentido físico.** El presupuesto cierra en este modelo ideal, con un 42 % de margen. En un satélite real habría pérdidas, degradación y orientación del panel que lo reducen; el cálculo sirve para ordenar magnitudes, no para diseñar. Comprobación geométrica: si `r → R`, `f → 0,5`; si `r → ∞`, `f → 0`.

## 14. Comparación de métodos

**Serie y paralelo** son rápidos para redes simples; **Kirchhoff y análisis nodal** valen para cualquier red y se programan; **balance de potencia** no resuelve pero verifica; **simulación de circuitos** (herramientas externas) se usa en diseño real. Usa siempre el balance de potencia como comprobación.

## 15. Práctica guiada

**Ejercicio 1.** Calcula la corriente y la potencia de una resistencia de 4 Ω con 12 V. *Pasos:* ley de Ohm (sección 8.1).

<details><summary>Solución comentada</summary>

`I = 12/4 = 3 A`; `P = 12 × 3 = 36 W`. Con `I² R = 9 × 4 = 36 W`: coincide.
</details>

**Ejercicio 2.** Halla `R_eq` de 6 Ω y 12 Ω en paralelo y en serie. *Pista:* sección 8.2.

<details><summary>Solución comentada</summary>

Paralelo: `1/(1/6 + 1/12) = 4 Ω`; serie: `18 Ω`. La paralela es menor que la menor.
</details>

**Ejercicio 3.** Un divisor con 4 Ω y 8 Ω en serie a 12 V. ¿Tensión en la de 8 Ω?

<details><summary>Solución comentada</summary>

`I = 12/12 = 1 A`; `V = 1 × 8 = 8 V`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Una corriente de 2 A circula 1 h. ¿Cuántos culombios y cuántas cargas elementales?

<details><summary>Solución comentada</summary>

`Q = 2 × 3600 = 7200 C`; `N = 7200/1,602 × 10⁻¹⁹ = 4,49 × 10²²`.
</details>

**Ejercicio 5.** Un equipo de 100 W a 28 V. ¿Qué corriente y resistencia equivalente?

<details><summary>Solución comentada</summary>

`I = 100/28 = 3,571 A`; `R = V/I = 7,84 Ω`.
</details>

**Ejercicio 6.** En el circuito de la sección 8.3, ¿cuánta potencia disipa `R₂`?

<details><summary>Solución comentada</summary>

`I₂² R₂ = (1,0588)² × 6 = 6,727 W` (también `v_A²/R₂ = 6,3529²/6 = 6,727 W`).
</details>

**Ejercicio 7.** Con 5,25 m² de panel al 28 % y el Sol de frente, ¿cuánta potencia obtienes?

<details><summary>Solución comentada</summary>

`1361,2 × 5,25 × 0,28 = 2001 W`: justo la carga de 2000 W, **sin** margen ni eclipse.
</details>

**Ejercicio 8.** Si el panel forma 60° con la normal al Sol (potencia ∝ `cos 60°`), ¿qué potencia da el de 10 m² al 28 %?

<details><summary>Solución comentada</summary>

`3811 × 0,5 = 1906 W`, por debajo de la carga de 2000 W. La orientación importa.
</details>

**Ejercicio 9 · transferencia.** Un compañero afirma que el eclipse dura la mitad de la órbita. Evalúa con la sección 8.5.

<details><summary>Solución comentada</summary>

La fracción en sombra para `r = 6778 km` es `0,39` y tiende a `0,5` solo en el límite `r → R`. Con la órbita a 2000 km (`r = 8378 km`) sería `0,275` y duraría unos 35 min de 127. La fracción baja con la altura; depende además de la geometría con el Sol.
</details>

**Ejercicio 10 · transferencia.** En un balance de potencia, la fuente da 17 W y las resistencias disipan 16 W. ¿Qué indica?

<details><summary>Solución comentada</summary>

Un error: o hay una pérdida no modelada o la solución es incorrecta. Se revisan ecuaciones de nodos y corrientes hasta que ambas potencias coincidan dentro de la tolerancia (en el laboratorio, `10⁻¹²`).
</details>

**Ejercicio 11 · transferencia.** Un artículo dice «los satélites tienen energía ilimitada porque usan el Sol». Corrige con el presupuesto de la sección 13.

<details><summary>Solución comentada</summary>

La energía solar es abundante pero el panel entrega una potencia finita y hay eclipses; la batería se dimensiona para cubrir la carga en sombra y recargarse en el sol. El presupuesto debe cerrar con margen.
</details>

**Ejercicio 12 · integrador.** Elabora una *hoja de circuito y presupuesto de energía* (sección 20): resuelve una red sintética de al menos tres resistencias con análisis nodal y compruébala con el balance de potencia; después calcula para una órbita circular circundante a tu elección la fracción de eclipse y la energía de batería para una carga sintética.

<details><summary>Solución modelo</summary>

Debe incluir el esquema (o tabla), las ecuaciones nodales, la solución con unidades, el balance de potencia, `f = arcsen(R/r)/π`, `E_bat = P f T` y los límites (corriente continua, sombra cilíndrica, `β = 0`, datos sintéticos).
</details>

## 17. Laboratorio: circuito y presupuesto de energía

El script [circuitos_y_potencia.py](circuitos_y_potencia.py) resuelve por análisis nodal (eliminación gaussiana) la red de la sección 8.3, comprueba las leyes de Kirchhoff y el balance de potencia, y calcula el presupuesto de energía del satélite ideal. Se detiene si la solución no coincide con la de serie y paralelo (`10⁻¹²`), si la corriente no suma en los nodos o si la fracción de eclipse falla en sus casos límite (`r = R` y `r → ∞`).

**Datos:** circuito, panel y carga sintéticos; flujo solar calculado con S1 y S2. **Predice antes de ejecutar:** ¿qué fracción de la órbita pasa en la sombra? (Un poco menos de 0,4.) **Resultados (2026-11-05, Python 3.12.9):** `v_A = 6,3529 V`, `v_B = 4,2353 V`; `I₁ = 1,4118 A`, `I₂ = 1,0588 A`, `I₃ = I₄ = 0,3529 A`; `R_eq = 8,500 Ω`; `P_fuente = 16,941 W`. Flujo solar `1361,2 W/m²`; panel `3811 W`; órbita a 400 km: `T = 5553,6 s`; fracción en eclipse `0,3901` (36,1 min); energía de batería `4,333 × 10⁶ J` (1,204 kWh); excedente de recarga `6,135 × 10⁶ J` (relación 1,42).

```bash
python programa/clases/B05/B05-C16-corriente-y-circuitos-elementales/circuitos_y_potencia.py
```

**Límites:** circuitos resistivos en corriente continua; sombra cilíndrica con `β = 0`; no es una herramienta de diseño de energía de naves ni certifica nada sobre vuelo o seguridad.

## 18. Errores frecuentes y cómo corregirlos

**Confundir serie y paralelo.** Ejercicio 2. **Olvidar el balance de potencia.** Ejercicio 10. **Suponer que el eclipse es la mitad de la órbita.** Ejercicio 9. **Ignorar la orientación del panel.** Ejercicio 8. **Mezclar tensión y corriente.** Ejercicio 1.

## 19. Cómo sabrás que vas bien

Tras 8.2: ¿por qué la paralela es menor que cada una? Repite el ejercicio 2. Tras 8.4: ¿qué prueba un balance de potencia? Rehaz el ejercicio 10. Tras el laboratorio: ¿qué casos límite comprueba? Léelo.

## 20. Qué entregas y cómo se evalúa

El producto es tu **hoja de circuito y presupuesto de energía**: red resuelta con verificación y presupuesto con eclipse.

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Ecuaciones del circuito | Errores | Con ayuda | Correctas | Dos métodos |
| Verificación | Ninguna | Una | Balance de potencia | Casos límite |
| Presupuesto de energía | Ausente | Parcial | Calcula eclipse y batería | Analiza sensibilidad |
| Alcance | No declara | Parcial | Declara | Distingue sintético de real |

**Condiciones críticas:** no presentar el presupuesto como diseño real; unidades; citar solo lo consultado.

## 21. Ética, seguridad y límites

Las baterías y las altas corrientes pueden provocar calor, incendio o descarga; esta clase es educativa y no sustituye normas de seguridad eléctrica ni análisis de misión. Accesibilidad: ecuaciones en texto, esquemas descritos y tablas equivalentes, sin conexión.

## 22. Para cerrar y seguir

La corriente es carga por tiempo, la ley de Ohm liga `V`, `I` y `R`, las leyes de Kirchhoff resuelven redes y el balance de potencia las verifica; un presupuesto de energía con eclipse convierte esas ideas en una decisión sobre baterías y paneles. Queda abierto cómo las cargas en movimiento generan un nuevo campo: el campo magnético (C17).

**Glosario español–inglés.** corriente · *current*; tensión · *voltage*; resistencia · *resistance*; ley de Ohm · *Ohm's law*; nodo · *node*; paralelo · *parallel*; eclipse · *eclipse*.

**Continuidad.** B05-C17 usa tu capacidad de **calcular la corriente de un conductor** para introducir el campo magnético que esa corriente genera.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B05-C15 — Campos eléctricos](../B05-C15-campos-electricos/CLASE.md) · [📚 Bloque B05](../../../tronco-comun/B05-fisica-fundamental-para-el-espacio.md) · [Siguiente: B05-C17 — Campos magnéticos →](../B05-C17-campos-magneticos/CLASE.md)
<!-- /nav -->
