# B24-C03 — Diagrama de Hertzsprung-Russell

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B24](../../../tronco-comun/B24-fisica-y-evolucion-de-estrellas.md) · [← Anterior: B24-C02 — Formación de protoestrellas](../B24-C02-formacion-de-protoestrellas/CLASE.md) · [Siguiente: B24-C04 — Equilibrio hidrostático estelar →](../B24-C04-equilibrio-hidrostatico-estelar/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 3 del bloque B24. Nivel N3. Ya sabes que una protoestrella se contrae ([C02](../B24-C02-formacion-de-protoestrellas/CLASE.md)); ahora necesitas un mapa donde ubicar estrellas jóvenes, estables y evolucionadas. Ese mapa es el **diagrama de Hertzsprung–Russell (HR)**: luminosidad contra temperatura. Retomas la estrella como cuerpo negro de [B01-C14](../../B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md) y la radiación de [B05-C18](../../B05/B05-C18-electromagnetismo-y-radiacion/CLASE.md). Aquí lees el diagrama y calculas radios; la física de cada región se desarrolla en las clases siguientes.

## 2. Por qué esta clase existe

Casi todas las propiedades de una estrella (tamaño, masa, edad, fase) se resumen en dos medidas: cuánta energía emite y a qué temperatura. El diagrama HR convierte esas dos medidas en un mapa donde cada región corresponde a un estado físico. La decisión central: **dados la luminosidad y la temperatura efectiva de una estrella, ¿qué radio tiene y qué tipo de objeto es?**

## 3. Lo que podrás hacer al terminar

1. Definir temperatura efectiva, luminosidad, diagrama HR y secuencia principal.
2. Calcular el radio de una estrella desde `L` y `T_ef` con `L = 4πR²σT⁴`.
3. Calcular diferencias de magnitud a partir de cocientes de luminosidad.
4. Ubicar enanas, secuencia principal, gigantes y enanas blancas por su `(T_ef, L)`.
5. Explicar por qué en el diagrama la temperatura crece hacia la izquierda.
6. Indicar qué errores de distancia o de temperatura distorsionan el diagrama.

La evidencia es la **tabla HR de cuatro estrellas** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Cómo depende la potencia radiada por un cuerpo negro de su temperatura?
2. ¿Cuánto vale el área de una esfera?
3. ¿Qué es un logaritmo decimal?
4. ¿Qué es una magnitud estelar y en qué sentido va?
5. ¿Qué es una diferencia de `5` magnitudes en brillo?

<details>
<summary>Ver respuestas</summary>

1. Crece con `T⁴` (ley de Stefan–Boltzmann). 2. `4πR²`. 3. El exponente al que hay que elevar 10. 4. Una escala logarítmica del brillo; números menores son más brillantes. 5. Un factor de `100`.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa B01-C14 y B05-C18.

## 5. Un caso real: el diagrama HR de Gaia

La misión Gaia produjo diagramas HR observacionales de precisión y cobertura sin precedentes para estrellas del campo y de cúmulos abiertos y globulares, y mostró que la secuencia de enanas blancas se divide en una de hidrógeno y otra de helio (S3, resumen). El **ejemplo conductor** de esta clase es más simple: cuatro estrellas **sintéticas** (ilustrativas) que representan cuatro regiones del diagrama: una enana roja, una estrella como el Sol, una gigante roja y una enana blanca. El Sol, con `T_ef = 5772 K` y `L = 3,828 × 10²⁶ W` (S2), es el punto de referencia.

## 6. Vocabulario

La **luminosidad** `L` es la energía total que la estrella emite por segundo, en vatios. La **temperatura efectiva** `T_ef` es la temperatura de un cuerpo negro con el mismo radio y la misma luminosidad. La **constante de Stefan–Boltzmann** `σ` liga la emisión de un cuerpo negro con `T⁴`. El **diagrama HR** representa `L` (o la magnitud absoluta) contra `T_ef` (o el tipo espectral), con la temperatura creciente hacia la izquierda por tradición histórica. La **secuencia principal** es la banda diagonal donde las estrellas fusionan hidrógeno en el núcleo. Una **gigante** es una estrella más luminosa y mucho mayor que una de la secuencia principal con la misma temperatura. Una **enana blanca** es un remanente caliente y poco luminoso, de radio pequeño. Una **línea de radio constante** (isorradio) une los puntos del diagrama con el mismo `R`.

## 7. Modelo mental: dos números fijan el tamaño

Piensa en una estufa: a la misma temperatura, la más grande da más calor. La luminosidad es temperatura (a la cuarta) por superficie. Si conoces `L` y `T`, el tamaño sale solo.

```mermaid
flowchart LR
    A["Flujo y distancia"] --> L["Luminosidad L"]
    B["Espectro o color"] --> T["Temperatura T_ef"]
    L --> R["Radio R = √(L/(4πσ)) / T²"]
    T --> R
    L --> HR["Punto en el diagrama HR"]
    T --> HR
    R --> HR
```

*Descripción textual:* de la medida del flujo y la distancia se obtiene la luminosidad; del espectro o el color, la temperatura; juntas dan el radio y el punto del diagrama.

Analogía: dos estufas con la misma potencia pero distinta temperatura de superficie tienen distinto tamaño. Límite: una estrella no es un cuerpo negro perfecto, y `T_ef` es una definición, no la temperatura de un punto concreto.

## 8. La explicación, paso a paso

### 8.1 Luminosidad, radio y temperatura

Un cuerpo negro emite por unidad de superficie `σT⁴`. Sobre toda la esfera, `L = 4πR²σT⁴`. Con `σ = 2π⁵k⁴/(15h³c²) = 5,670 374 × 10⁻⁸ W m⁻² K⁻⁴` (S1) y los valores nominales solares (S2), `L(R☉, T☉) = 3,828 × 10²⁶ W`: la fórmula reproduce la luminosidad nominal. En unidades solares, `R/R☉ = (L/L☉)^{1/2} (T☉/T)²`.

### 8.2 Magnitudes

Una diferencia de magnitud entre dos luminosidades es `ΔM = −2,5 log₁₀(L/L☉)`; un factor 100 en `L` son exactamente 5 magnitudes. (Aquí usamos solo diferencias; el punto cero absoluto se trata en otras clases.)

### 8.3 Las regiones del diagrama

Con el cálculo del laboratorio: una enana roja (`L = 0,01 L☉`, `3200 K`) tiene `R = 0,33 R☉`; una estrella como el Sol, `1 R☉`; una gigante roja (`L = 100 L☉`, `4500 K`), `16,5 R☉`; una enana blanca (`L = 0,003 L☉`, `12 000 K`), `0,013 R☉`, del orden del tamaño de un planeta. Las gigantes quedan arriba a la derecha (grandes y frías), las enanas blancas abajo a la izquierda (pequeñas y calientes) y la secuencia principal en la diagonal.

### 8.4 Qué cambia con la edad y la composición

Los diagramas de cúmulos y del campo cambian con la edad, la metalicidad y la cinemática de la población (S3, resumen). La posición de una estrella en el diagrama depende de su masa, de su composición y de cuánto ha evolucionado. Esto se usa para datar cúmulos (C19).

### 8.5 Qué distorsiona el diagrama

Un error de distancia `d` cambia `L` como `d²`; un error de temperatura cambia `L` como `T⁴` a radio fijo. Una muestra limitada por flujo favorece a las estrellas luminosas. La escala de temperaturas depende del método y del tipo de estrella (S4, resumen para estrellas jóvenes).

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `L` | luminosidad | W; `L☉` | `L☉ = 3,828 × 10²⁶ W` (S2) |
| `T_ef` | temperatura efectiva | K | `T☉ = 5772 K` (S2) |
| `R` | radio | m; `R☉` | `R☉ = 6,957 × 10⁸ m` (S2) |
| `σ` | constante de Stefan–Boltzmann | `W m⁻² K⁻⁴` | `5,670 374 419 × 10⁻⁸` (S1) |
| `ΔM` | diferencia de magnitud | mag | `−2,5 log₁₀(L/L☉)` |

## 10. Convenciones y referencias

Cuerpo negro; unidades solares nominales de la IAU (S2); ejes con temperatura decreciente a la derecha y luminosidad creciente hacia arriba, en escala logarítmica. Las cuatro estrellas son **sintéticas**.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NIST, *Fundamental Physical Constants — Complete Listing* (CODATA 2022) | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | `h`, `k`, `c`, `σ` | Consultada el 2026-11-09 |
| S2 | Mamajek et al., *IAU 2015 Resolution B3*, arXiv:1510.07674 | https://arxiv.org/abs/1510.07674 | `R☉`, `L☉`, `T_ef,☉` nominales | Texto del PDF extraído el 2026-11-09 |
| S3 | Gaia Collaboration, *Gaia Data Release 2: Observational Hertzsprung-Russell diagrams*, arXiv:1804.09378 | https://arxiv.org/abs/1804.09378 | HRD de campo y cúmulos; secuencia de enanas blancas dividida | Solo resumen, consultado el 2026-11-09 |
| S4 | Pecaut y Mamajek, arXiv:1307.2657 | https://arxiv.org/abs/1307.2657 | Escala de temperaturas distinta en estrellas jóvenes | Solo resumen, consultado el 2026-11-09 |

Límites: S3 y S4 solo resumen; las cuatro estrellas de ejemplo son sintéticas.

## 12. Cómo ver el diagrama

Equivalente accesible a un gráfico `L` contra `T`:

| Estrella (sintética) | `T_ef` (K) | `L` (`L☉`) | `R` (`R☉`) | Región |
|---|---|---|---|---|
| Enana roja | 3200 | 0,01 | 0,33 | Abajo a la derecha |
| Tipo solar | 5772 | 1 | 1,00 | Centro de la secuencia |
| Gigante roja | 4500 | 100 | 16,5 | Arriba a la derecha |
| Enana blanca | 12 000 | 0,003 | 0,013 | Abajo a la izquierda |

Descripción larga: los puntos forman una «Z» invertida: la secuencia diagonal, una rama de gigantes por encima y las enanas blancas por debajo.

## 13. Ejemplo trabajado: el radio de una gigante

**Paso 1 · Datos.** `L = 100 L☉`, `T = 4500 K` (sintética).

**Paso 2 · Fórmula.** `R/R☉ = (L/L☉)^{1/2} (T☉/T)²` (8.1).

**Paso 3 · Cálculo.** `√100 = 10`; `(5772/4500)² = 1,645`; `R = 16,45 R☉`.

**Paso 4 · Sentido.** La gigante es unas 16 veces mayor que el Sol; su magnitud difiere en `−5,00` respecto de él. Si estuviera en el lugar del Sol, su radio de `1,14 × 10¹⁰ m` equivale a `0,076 au`. El resultado depende de que el punto sea de la rama de gigantes, no de la secuencia.

## 14. Distintas formas de situar una estrella

**HR con `L` y `T_ef`:** física directa, exige distancia. **Diagrama color–magnitud:** usa observables (color y magnitud aparente) sin pasar a `L`; sirve para cúmulos a una sola distancia. **Tipo espectral y clase de luminosidad:** clasificación cualitativa (C10). Se usan juntos.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `R` de una estrella con `L = 100 L☉` y `T = 4500 K`. *Pasos:* aplica 8.1.

<details><summary>Solución comentada</summary>

`10 × 1,645 = 16,45 R☉` (13).
</details>

**Ejercicio 2 · con una pista.** ¿Qué diferencia de magnitud corresponde a `L = 0,01 L☉`? *Pista:* `−2,5 log₁₀ 0,01`.

<details><summary>Solución comentada</summary>

`−2,5 × (−2) = +5,0` magnitudes, más débil (8.2).
</details>

**Ejercicio 3 · casi autónomo.** Calcula `R` de la enana blanca (`L = 0,003 L☉`, `12 000 K`) en `R☉` y en kilómetros.

<details><summary>Solución comentada</summary>

`√0,003 = 0,0548`; `(5772/12 000)² = 0,2314`; `R = 0,0127 R☉ = 8,8 × 10⁶ m = 8800 km`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Si la temperatura de una estrella se duplica con el radio fijo, ¿cómo cambia `L`?

<details><summary>Solución comentada</summary>

`L ∝ T⁴`: sube `2⁴ = 16` veces (8.1).
</details>

**Ejercicio 5.** Con la misma temperatura, un radio diez veces mayor, ¿cuánto cambia `L`?

<details><summary>Solución comentada</summary>

`L ∝ R²`: cien veces, es decir cinco magnitudes más brillante.
</details>

**Ejercicio 6.** Dos estrellas tienen igual `L`, una a `3200 K` y otra a `6400 K`. ¿Cuál es la razón de radios?

<details><summary>Solución comentada</summary>

`R ∝ T⁻²`: la fría es `(6400/3200)² = 4` veces mayor.
</details>

**Ejercicio 7.** Calcula la diferencia de magnitud entre la gigante (`100 L☉`) y la enana blanca (`0,003 L☉`).

<details><summary>Solución comentada</summary>

`−2,5 log₁₀(100/0,003) = −2,5 × 4,523 = −11,3` mag (la gigante es 11,3 mag más brillante).
</details>

**Ejercicio 8.** Una estrella de `T = 9900 K` y `L = 25 L☉`, ¿qué radio tiene?

<details><summary>Solución comentada</summary>

`5 × (5772/9900)² = 5 × 0,340 = 1,70 R☉` (secuencia principal caliente, valores sintéticos).
</details>

**Ejercicio 9 · transferencia.** Un error del `10 %` en la distancia a una estrella, ¿cuánto cambia su `L`?

<details><summary>Solución comentada</summary>

`L ∝ d²`: `1,1² = 1,21`, un `21 %` (8.5).
</details>

**Ejercicio 10 · transferencia.** ¿Por qué un catálogo limitado por flujo pone más gigantes que enanas rojas en el diagrama, aunque haya más enanas rojas en el cielo?

<details><summary>Solución comentada</summary>

Las gigantes se ven desde muy lejos; las enanas rojas, tenues, solo cerca. La muestra está sesgada hacia las luminosas (8.5).
</details>

**Ejercicio 11 · transferencia.** La división de la secuencia de enanas blancas en hidrógeno y helio que encontró Gaia (S3), ¿qué te dice de la utilidad del diagrama?

<details><summary>Solución comentada</summary>

Que con datos suficientemente precisos el HR separa poblaciones por su composición atmosférica, no solo por masa y edad; el diagrama es una herramienta de diagnóstico.
</details>

**Ejercicio 12 · integrador.** Elabora tu *tabla HR de cuatro estrellas*: elige cuatro puntos `(T, L)` sintéticos, calcula `R` y `ΔM`, indica su región y qué error de distancia desplazaría cada punto.

<details><summary>Solución modelo</summary>

Usa la tabla de la sección 12 como plantilla; para cada punto aplica 8.1 y 8.2; un error del 10 % en `d` cambia `L` un 21 % (ejercicio 9). Rotula como sintéticos.
</details>

## 17. Laboratorio: radios desde el HR

El script [hr_radios.py](hr_radios.py) deriva `σ` de `h`, `k` y `c`, **comprueba** que coincide con el valor de NIST (tolerancia `10⁻⁹`), que `L(R☉, T☉)` reproduce `L☉` nominal (tolerancia `10⁻³`), que 100 veces en `L` son 5 magnitudes y que cada radio calculado devuelve la luminosidad de partida.

**Datos:** constantes de NIST; valores nominales de la IAU; estrellas **sintéticas**. **Predice antes de ejecutar:** ¿qué radio saldrá para la estrella de tipo solar? (1 `R☉`.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
sigma = 5.670374419e-08 W m-2 K-4 ; L(R_sol,T_sol) = 3.8280e+26 W (1.00000 L_sol nominal)
enana roja           L=   0.010 L_sol T=   3200 K -> R =    0.3254 R_sol ; dM = +5.00
secuencia principal  L=   1.000 L_sol T=   5772 K -> R =    1.0000 R_sol ; dM = -0.00
gigante roja         L= 100.000 L_sol T=   4500 K -> R =   16.4523 R_sol ; dM = -5.00
enana blanca         L=   0.003 L_sol T=  12000 K -> R =    0.0127 R_sol ; dM = +6.31
Pruebas superadas.
```

```bash
python programa/clases/B24/B24-C03-diagrama-de-hertzsprung-russell/hr_radios.py
```

**Límites:** cuerpo negro; sin oscurecimiento al limbo, extinción ni correcciones bolométricas.

## 18. Errores frecuentes y cómo corregirlos

**Leer el eje de temperatura al revés.** Se corrige con la sección 7 y 10: crece hacia la izquierda.

**Creer que `T_ef` es la temperatura interna.** Se corrige con la definición de la sección 6.

**Olvidar el cuadrado en `T⁻²` del radio.** Se corrige con el ejercicio 6.

**Ignorar el sesgo por flujo.** Se corrige con el ejercicio 10.

**Mezclar magnitud absoluta con aparente.** Se corrige con el ejercicio 9 y el ejemplo conductor.

## 19. Cómo sabrás que vas bien

Tras 8.1: ¿calculas `R` desde `L` y `T`? Si no, ejercicio 1. Tras 8.3: ¿sabes ubicar una gigante? Ejercicio 5. Tras el laboratorio: ¿qué verifica que `σ` coincida con NIST? (que las constantes definitorias reproducen la ley de Stefan–Boltzmann).

## 20. Qué entregas y cómo se evalúa

El producto es tu **tabla HR de cuatro estrellas** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Definiciones | Las confunde | Parciales | `L`, `T_ef`, `R` | Distingue `T_ef` de la interna |
| Cálculo | Sin unidades | Con errores | `R` y `ΔM` correctos | Propaga el error de `d` |
| Ubicación | Sin región | Una | Cuatro regiones | Explica el sesgo por flujo |
| Numérico | Sin comprobar | Un caso | Pruebas superadas | Cierra el ciclo `L → R → L` |
| Fuentes | Sin fuente | Sin fecha | S1–S4 con fecha | Declara que S3 y S4 son resúmenes |

**Condiciones críticas (no se compensan con promedio):** rotular lo sintético; no tratar `T_ef` como temperatura interna; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los datos de Gaia se citan por su resumen y no se reproducen sus figuras. Los datos reales de una estrella exigen distancia, extinción y calibración (B13). Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Con `L` y `T_ef` obtienes el radio y la región del diagrama; el HR distingue enanas, secuencia principal, gigantes y enanas blancas. Queda una pregunta: ¿qué mantiene a una estrella de la secuencia principal con un tamaño estable?

**Glosario español–inglés.** diagrama de Hertzsprung–Russell · *Hertzsprung–Russell diagram*; luminosidad · *luminosity*; temperatura efectiva · *effective temperature*; secuencia principal · *main sequence*; gigante · *giant*; enana blanca · *white dwarf*; isorradio · *iso-radius line*.

**Continuidad.** [B24-C04](../B24-C04-equilibrio-hidrostatico-estelar/CLASE.md) reutiliza el radio para explicar por qué una estrella no se contrae ni se expande.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B24-C02 — Formación de protoestrellas](../B24-C02-formacion-de-protoestrellas/CLASE.md) · [📚 Bloque B24](../../../tronco-comun/B24-fisica-y-evolucion-de-estrellas.md) · [Siguiente: B24-C04 — Equilibrio hidrostático estelar →](../B24-C04-equilibrio-hidrostatico-estelar/CLASE.md)
<!-- /nav -->
