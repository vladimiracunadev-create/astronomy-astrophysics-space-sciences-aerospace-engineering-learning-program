# B61-C02 — Cráteres simples: morfología y formación

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B61](../../../tronco-comun/B61-crateres-de-impacto-y-geologia-de-impactos.md) · [← Anterior: B61-C01 — Dinámica de eyección y escalado de cráteres](../B61-C01-dinamica-de-eyeccion-y-escalado-de-crateres/CLASE.md) · [Siguiente: B61-C03 — Cráteres complejos: colapso, picos centrales y terrazas →](../B61-C03-crateres-complejos-colapso-picos-centrales-y-terrazas/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 2 del bloque B61. Nivel N3. Un cráter **simple** es un bol en forma de cuenco, sin pico central. Aquí describes su **geometría** (casquete esférico de profundidad `d` y diámetro `D`), calculas su volumen por dos vías (fórmula e integración numérica) y haces un **balance de volumen** entre el cráter transitorio, el cráter aparente y la lente de brecha que lo rellena. Usa la [C01](../B61-C01-dinamica-de-eyeccion-y-escalado-de-crateres/CLASE.md). Todas las razones geométricas son **ilustrativas** (relación `d/D` = 0,2, factor de ensanchamiento 1,25, abultamiento 1,15); no se mide ningún cráter.

## 2. Por qué esta clase existe

Medir un cráter es medir un bol, pero lo que se ve es el bol **después** de colapsar y rellenarse. La decisión central: **¿cuánto volumen tenía la cavidad original y cuánto se perdió en el relleno de brecha?**

## 3. Lo que podrás hacer al terminar

1. Describir un cráter simple con `D`, `d` y el radio de curvatura del casquete.
2. Calcular su volumen con `V = π d (3R² + d²)/6` y con integración numérica.
3. Distinguir el cráter transitorio del aparente y usar el factor de ensanchamiento.
4. Resolver por bisección la profundidad residual tras una lente de brecha.
5. Estimar el volumen mínimo de eyecta por abultamiento.
6. Declarar que las razones geométricas son ilustrativas.

La evidencia es la **ficha de la geometría de un cráter simple** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es un casquete esférico?
2. ¿Qué es una integral numérica?
3. ¿Qué es un cráter transitorio (C01)?
4. ¿Qué es el abultamiento (bulking)?
5. ¿Qué es una bisección?

<details>
<summary>Ver respuestas</summary>

1. Una porción de esfera cortada por un plano. 2. Sumar áreas de rebanadas pequeñas. 3. La cavidad antes del colapso. 4. El aumento de volumen del material excavado por su desorden. 5. Un método que acota una raíz reduciendo a la mitad el intervalo.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Con `d/D` = 0,2, un cráter aparente de 1000 m tiene 200 m de profundidad y un volumen de **8,27×10⁷ m³**; su radio de curvatura vale 1,45 `R`. Si su cavidad transitoria fue de 800 m, la aparente tiene 1,95 veces su volumen. Todo **sintético**.

## 6. Vocabulario

El **casquete esférico** es la forma del suelo. El **ensanchamiento** (factor 1,25 aquí) es el crecimiento del diámetro por el colapso de la pared. La **lente de brecha** es el relleno de fragmentos del fondo. El **abultamiento** es el aumento de volumen del material removido. Un **cráter aparente** es el visible hoy.

## 7. Modelo mental

Un esquema del flujo de cálculo de la clase; el texto equivalente está debajo.

```mermaid
flowchart LR
    T["cráter transitorio D_t, d_t"] --> A["ensanchamiento x1,25"]
    A --> B["bol aparente D_a, d_a"]
    B --> L["lente de brecha f V_a"]
    L --> R["profundidad residual"]
```

*Descripción textual:* la cavidad transitoria se ensancha por colapso de la pared hasta el bol aparente y una lente de brecha lo rellena, dejando una profundidad residual que se calcula por bisección.

Analogía: un hoyo en la arena húmeda que se derrumba por los bordes y se rellena de granos: el hoyo visible es menos hondo y más ancho que el original. Límite: casquete perfecto, sin rampa de borde.

## 8. La explicación, paso a paso

### 8.1 Volumen

| `D` [m] | `d` [m] | `V` analítico [m³] | `V` numérico [m³] | dif. relativa |
|---|---|---|---|---|
| 100 | 20 | 8,272861×10⁴ | 8,272861×10⁴ | 1,3×10⁻⁹ |
| 1000 | 200 | 8,272861×10⁷ | 8,272861×10⁷ | 1,3×10⁻⁹ |
| 10 000 | 2000 | 8,272861×10¹⁰ | 8,272861×10¹⁰ | 1,3×10⁻⁹ |

El volumen escala como `D³` porque `d/D` es constante.

### 8.2 Transitorio y aparente

Con `D_t` = 800 m y `d_t` = 160 m, `V_t` = 4,2357×10⁷ m³. Con `D_a` = 1000 m y `d_a` = 200 m, `V_a` = 8,2729×10⁷ m³ y `V_a/V_t` = 1,9531 (igual a 1,25³). El ensanchamiento aporta 4,0372×10⁷ m³.

### 8.3 Lente de brecha

Una lente que llena el 25 % del bol aparente deja una profundidad residual de **153,21 m** (`d/D` = 0,1532). El balance de volumen cierra a 0 m³.

### 8.4 Abultamiento

Con factor 1,15 y `V_t` = 4,2357×10⁷ m³, el volumen mínimo de eyecta es 6,3536×10⁶ m³.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `D`, `d` | diámetro y profundidad | m | 100–10 000 (sintético) |
| `R` | `D/2` | m | calculado |
| `ρ` | radio de curvatura | m | `(R²+d²)/(2d)` |
| `V` | volumen del casquete | m³ | calculado |
| `f` | fracción de relleno | — | 0,25 (ilustrativo) |
| `b` | abultamiento | — | 1,15 (ilustrativo) |

## 10. Convenciones y referencias

Profundidad medida desde el borde; borde plano a `z` = 0; SI; el casquete es esférico y simétrico.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S3 | Resultado de búsqueda web sobre Holsapple (1993), Annu. Rev. Earth Planet. Sci. 21, 333–373, y trabajos que lo citan | consultada 2026-11-09 | límites μ = 1/3 (momento) y 2/3 (energía); μ = 0,55 para roca blanda; dos regímenes (resistencia y gravedad) | Resumen de terceros; el artículo original no se consultó. El resumen escribía el exponente del volumen como −3μ/(3+μ), que no pude reconciliar con −3μ/(2+μ); se usa esta última por el cálculo del radio y se marca para verificar |
| — | Sin fuente externa | — | los cálculos de la sección 17 y los parámetros marcados como ilustrativos | No consultado |

Límites: la relación `d/D`, el ensanchamiento y el abultamiento no se obtuvieron de una fuente consultada; son parámetros de ejemplo. No se contrasta con ningún cráter real.

## 12. Cómo ver el resultado

| Magnitud | Valor |
|---|---|
| `V` (D = 1000 m) | 8,2729×10⁷ m³ |
| `V_a/V_t` | 1,9531 |
| profundidad residual | 153,21 m |
| eyecta mínima | 6,3536×10⁶ m³ |

Descripción larga: el volumen crece como `D³`; la lente de brecha reduce la profundidad aparente un 23 %.

## 13. Ejemplo trabajado

**Ejemplo: volumen de un bol de 100 m con `d/D` = 0,2.**

**Paso 1.** `R` = 50 m y `d` = 20 m.

**Paso 2.** `V = π·20·(3·2500 + 400)/6 = π·20·7900/6`.

**Paso 3.** `V = 8,2729×10⁴ m³`, igual al laboratorio.

## 14. Distintas formas de describir lo mismo

**Por fórmula:** casquete. **Por integral:** rebanadas de radio `r`. **Por razón:** `V = 0,0827 D³`. **Por balance:** transitorio, aparente y relleno.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `R` y `ρ` de un bol con `D` = 100 m y `d` = 20 m. *Pasos:* `ρ = (R²+d²)/(2d)`.

<details><summary>Solución comentada</summary>

`R` = 50 m; `ρ = (2500+400)/40 = 72,5 m` (1,45 `R`).
</details>

**Ejercicio 2 · con una pista.** Con una pista: ¿cuánto vale `V_a/V_t` si el ensanchamiento es 1,25 y `d/D` es constante?

<details><summary>Solución comentada</summary>

`1,25³ = 1,953`.
</details>

**Ejercicio 3 · casi autónomo.** Casi autónomo: ¿cuánto es 25 % de `V_a`?

<details><summary>Solución comentada</summary>

`0,25×8,2729×10⁷ = 2,068×10⁷ m³`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Calcula `V` de un bol de 200 m con `d/D` = 0,2.

<details><summary>Solución comentada</summary>

`0,0827×200³ = 6,62×10⁵ m³`.
</details>

**Ejercicio 5.** ¿Por qué la diferencia numérica–analítica es 10⁻⁹?

<details><summary>Solución comentada</summary>

Por la regla del punto medio con 20 000 anillos.
</details>

**Ejercicio 6.** ¿Qué profundidad residual deja una lente del 50 %? (planteo)

<details><summary>Solución comentada</summary>

Se resuelve `V(D_a,d_a) − V(D_a,d_r) = 0,5 V_a` por bisección; el valor no se calculó en el laboratorio.
</details>

**Ejercicio 7.** ¿Cuánta eyecta mínima produce un abultamiento de 1,30 con `V_t` = 4,2357×10⁷ m³?

<details><summary>Solución comentada</summary>

`0,30×4,2357×10⁷ = 1,271×10⁷ m³`.
</details>

**Ejercicio 8.** ¿Cómo escala el volumen si `D` se multiplica por 3?

<details><summary>Solución comentada</summary>

Por 27.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un colega mide `d/D` = 0,15 en un cráter y usa 0,20. ¿Qué error de volumen comete?

<details><summary>Solución comentada</summary>

El volumen crece casi con `d`: ≈ +33 % (sobre todo en el término `3R²`).
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Qué hipótesis falla en un cráter con rampa de borde elevada?

<details><summary>Solución comentada</summary>

La referencia `z` = 0 en el borde y el casquete simple.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Cómo sabrías si un cráter real es transitorio o aparente?

<details><summary>Solución comentada</summary>

Midiendo su perfil actual y comparándolo con el modelo; sin datos reales, no se puede afirmar.
</details>

**Ejercicio 12 · integrador.** Elabora tu *ficha de la geometría de un cráter simple*: casquete, volumen analítico y numérico, relación transitorio–aparente, lente de brecha y volumen mínimo de eyecta, con unidades y rótulos.

<details><summary>Solución modelo</summary>

Secciones 8.1–8.4: `V = 0,0827 D³` (8,27×10⁴ m³ para D = 100 m); `V_a/V_t` = 1,9531; profundidad residual 153,21 m con una lente del 25 %; eyecta mínima 6,35×10⁶ m³.
</details>

## 17. Laboratorio: geometría y balance de volumen de un cráter simple

El script [morfologia.py](morfologia.py) calcula el volumen del casquete por fórmula y por integración, resuelve por bisección la profundidad tras una lente de brecha y comprueba el cierre del balance (**comprueba** 1e-6 relativo y 1e-6·V).

**Datos:** razones geométricas **sintéticas**; sin constantes físicas. **Predice antes de ejecutar:** ¿Será la profundidad residual mayor o menor que 200 m? (menor, 153 m.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Datos sinteticos: d/D = 0.20 ; D_aparente = 1.25 D_transitorio ; bulking 1.15 (no medidos)
  D_ap [m]    d [m]    V_analit [m3]       V_num [m3]    dif rel   rho/R
       100     20.0     8.272861e+04     8.272861e+04   1.34e-09  1.4500
      1000    200.0     8.272861e+07     8.272861e+07   1.34e-09  1.4500
     10000   2000.0     8.272861e+10     8.272861e+10   1.34e-09  1.4500
Transitorio: D_t=800 m, d_t=160 m, V_t=4.2357e+07 m3
Aparente: D_a=1000 m, d_a=200 m, V_a=8.2729e+07 m3 ; V_a/V_t=1.9531
Volumen extra por ensanchamiento = 4.0372e+07 m3
Con lente de brecha del 25 % del volumen del bol aparente: profundidad residual = 153.21 m (d/D=0.1532)
Cierre del balance de volumen = 0.000e+00 m3
Volumen minimo de eyecta por abultamiento (bulking 1.15) = 6.3536e+06 m3
Pruebas superadas.
```

```bash
python programa/clases/B61/B61-C02-crateres-simples-morfologia-y-formacion/morfologia.py
```

**Límites:** casquete perfecto; sin rampa de borde ni asimetría; el balance no modela la dinámica del colapso.

## 18. Errores frecuentes y cómo corregirlos

**Confundir cráter transitorio y aparente.** Se corrige con 8.2.

**Calcular el volumen con un perfil cónico.** Se corrige con 8.1.

**Olvidar que `V ∝ D³`.** Se corrige con la tabla de 8.1.

**Presentar `d/D` como medido.** Se corrige con la sección 5.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas y cuál obtuviste? Si dudas, repasa el ejemplo de la sección 13. Tras el laboratorio: ¿qué comprueba cada aserción? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de la geometría de un cráter simple** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Explica los conceptos de la clase | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas con unidades | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con una vía independiente | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular los datos sintéticos e ilustrativos; no presentar lo simulado como observado; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y no sustituyen un código de impactos (hidrocódigo) ni el análisis de datos reales. No se afirma nada sobre cráteres reales. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Un cráter simple es un casquete cuyo volumen cierra un balance entre cavidad, ensanchamiento y relleno. Queda una pregunta: ¿qué pasa cuando el cráter es tan grande que la gravedad lo hace colapsar?

**Glosario español–inglés.** cráter simple · *simple crater*; casquete · *spherical cap*; brecha · *breccia*; abultamiento · *bulking*; ensanchamiento · *widening*.

**Continuidad.** [B61-C03](../B61-C03-crateres-complejos-colapso-picos-centrales-y-terrazas/CLASE.md) estudia los cráteres complejos.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B61-C01 — Dinámica de eyección y escalado de cráteres](../B61-C01-dinamica-de-eyeccion-y-escalado-de-crateres/CLASE.md) · [📚 Bloque B61](../../../tronco-comun/B61-crateres-de-impacto-y-geologia-de-impactos.md) · [Siguiente: B61-C03 — Cráteres complejos: colapso, picos centrales y terrazas →](../B61-C03-crateres-complejos-colapso-picos-centrales-y-terrazas/CLASE.md)
<!-- /nav -->
