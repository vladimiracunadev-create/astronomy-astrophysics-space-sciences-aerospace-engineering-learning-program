# B78-C15 — Propulsión nuclear eléctrica conceptual

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B78](../../../tronco-comun/B78-tecnologias-de-propulsion-espacial.md) · [← Anterior: B78-C14 — Propulsión nuclear térmica conceptual](../B78-C14-propulsion-nuclear-termica-conceptual/CLASE.md) · [Siguiente: B78-C16 — Propulsión de fusión como investigación →](../B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 15 del bloque B78. Nivel N3. En la propulsión nuclear-eléctrica un reactor alimenta propulsores eléctricos. La energía deja de ser un límite del propelente y pasa a ser un límite de masa: la planta de potencia pesa, y cada kilovatio extra le quita carga útil. Aquí tratas, **solo de forma conceptual**, el compromiso entre ahorrar propelente (alto `Isp`) y cargar con una planta mayor, con la masa específica `α` como parámetro ilustrativo. Usas [C06](../B78-C06-propulsion-electrica-general/CLASE.md) para la potencia del chorro. No hay diseño de reactor.

## 2. Por qué esta clase existe

Subir la velocidad de escape reduce el propelente pero obliga a más potencia, y por tanto a más planta, para el mismo tiempo de empuje. La decisión central: **¿existe un `Isp` que maximice la carga útil y cómo cambia con el Δv y con la masa específica de la planta?**

## 3. Lo que podrás hacer al terminar

1. Escribir la fracción útil `π = 1 − f_p(1 + α Vₑ²/(2ηt))`.
2. Calcular la velocidad característica `v_c = √(2ηt/α)`.
3. Encontrar el `Isp` óptimo con sección áurea y con una malla fina.
4. Ver cómo se desplaza el óptimo al subir el Δv.
5. Explicar por qué existe un máximo interior de carga útil.
6. Rotular lo ilustrativo y evitar presentarlo como diseño.

La evidencia es la **curva de carga útil frente a velocidad de escape** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es la masa específica de una planta de potencia?
2. ¿Qué es la ecuación del cohete?
3. ¿Qué es un máximo interior de una función?
4. ¿Qué es un dato sintético?
5. ¿Qué es una verificación por segunda vía?

<details>
<summary>Ver respuestas</summary>

1. Su masa dividida por la potencia que entrega, en kg/kW. 2. `Δv = Vₑ ln(m₀/m_f)`. 3. Un máximo que ocurre dentro del dominio, no en un extremo. 4. Un dato generado para el ejemplo, no medido. 5. Calcular lo mismo con otro método y comparar.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Con una planta ilustrativa de `α = 20 kg/kW`, `η = 0,6` y `300 días` de empuje, la velocidad característica vale `39 436 m/s`. Para `Δv = 5000 m/s`, el `Isp` óptimo es `3763 s` con una fracción útil de `0,7623`; para `15 000 m/s`, `3219 s` y `0,3794`: el **ejemplo conductor**. Dawn tenía paneles de más de 10 kW (consultado), que con ese `α` serían `200 kg`.

## 6. Vocabulario

La **masa específica** `α` es kg de planta por kW. La **fracción útil** `π` es la carga útil entre la masa inicial. La **velocidad característica** `v_c = √(2ηt/α)` es la escala de `Vₑ` a la que la planta pesa como el propelente. El **tiempo de empuje** `t` es el tiempo total de funcionamiento. La **propulsión nuclear-eléctrica** usa un reactor como fuente de potencia (concepto).

## 7. Modelo mental

```mermaid
flowchart LR
    DV["dv, Ve"] --> FP["f_p = 1 - exp(-dv/Ve)"]
    FP --> P["P = f_p m0 Ve^2 / (2 eta t)"]
    P --> MPOW["m_planta = alpha P"]
    FP --> PI["pi = 1 - f_p - m_planta/m0"]
    MPOW --> PI
    PI --> OPT["Ve optimo"]
```

*Descripción textual:* el Δv y el escape dan la fracción de propelente; ésta y el tiempo fijan la potencia y con `α` la masa de la planta; la carga útil es lo que queda y se busca el escape que la maximiza.

Analogía: cargar un camión con combustible o con un motor más grande; un motor pequeño gasta más combustible y uno grande pesa más. Límite: aquí el «combustible» es el propelente y el «motor», la planta de potencia.

## 8. La explicación, paso a paso

### 8.1 El modelo

`f_p = 1 − e^(−Δv/Vₑ)`, `P = f_p m₀ Vₑ²/(2ηt)` y `m_planta = α P`. La fracción útil es `π = 1 − f_p (1 + α Vₑ²/(2ηt))`; se ignoran estructura y tanques. Con `v_c = √(2ηt/α) = 39 436 m/s`, el término de planta vale `(Vₑ/v_c)²`.

### 8.2 Δv de 5000 m/s

| `Isp` (s) | `Vₑ` (m/s) | `f_p` | `m_planta/m₀` | `π` |
|---|---|---|---|---|
| 500 | 4903 | 0,6393 | 0,0099 | 0,3508 |
| 1000 | 9807 | 0,3994 | 0,0247 | 0,5759 |
| 2000 | 19 613 | 0,2250 | 0,0557 | 0,7193 |
| 3000 | 29 420 | 0,1563 | 0,0870 | 0,7567 |
| 5000 | 49 033 | 0,0969 | 0,1499 | 0,7532 |
| 8000 | 78 453 | 0,0617 | 0,2444 | 0,6939 |

El máximo es interior: `Vₑ = 36 906 m/s` (`3763 s`), `π = 0,7623`, `Vₑ/v_c = 0,936`. Por la sección áurea y por la malla fina el óptimo coincide dentro de `0,05 %`, y `π` baja a ambos lados.

### 8.3 Δv de 15 000 m/s

El óptimo baja a `Vₑ = 31 572 m/s` (`3219 s`) con `π = 0,3794` (`Vₑ/v_c = 0,801`): cuanto mayor el Δv, más propelente ahorra cada punto de `Isp` y más conviene bajar un poco el escape para acortar la planta.

### 8.4 Qué no incluye

No hay estructura, radiadores aparte de `α`, degradación de la planta ni tiempo de arranque. La planta de 10 kW de Dawn, con `α = 20 kg/kW`, daría `200 kg`; es un orden de magnitud, no un dato de Dawn.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `α` | masa específica de la planta | kg/kW | 20 (ilustrativa) |
| `η` | eficiencia del propulsor | — | 0,6 (ilustrativa) |
| `t` | tiempo de empuje | días | 300 (ilustrativo) |
| `v_c` | velocidad característica | m/s | 39 436 |
| `π` | fracción útil | — | 0,7623 (óptimo, 5000 m/s) |
| `Vₑ` | escape óptimo | m/s | 36 906 |

## 10. Convenciones y referencias

Empuje continuo equivalente impulsivo, planta de masa proporcional a la potencia, sin estructura ni tanques. Sistema de referencia: la nave. Versiones: NIST CODATA y página de Dawn (consulta del 2026-11-10). `α`, `η`, `t` y los Δv son **ilustrativos**; no hay diseño de reactor.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NIST, CODATA Fundamental Physical Constants (tabla ASCII) — https://physics.nist.gov/cuu/Constants/Table/allascii.txt (consultada 2026-11-10) | fila de `g₀` | `g₀` | Consultada |
| S2 | NASA/JPL, Dawn: Ion Propulsion — https://science.nasa.gov/mission/dawn/technology/ion-propulsion/ (consultada 2026-11-10) | párrafo de paneles solares | paneles de más de 10 kW en la Tierra | Consultada |
| — | Relaciones estándar de la física y la ingeniería de propulsión | — | las verifica el laboratorio con una segunda vía | No consultada en una fuente concreta |

Límites: la masa específica de una planta nuclear-eléctrica real no se consultó; `α = 20 kg/kW` es un valor ilustrativo que no representa ninguna tecnología; no se consultó ninguna fuente sobre sistemas nucleares-eléctricos.

## 12. Cómo ver el resultado

| Magnitud | Valor |
|---|---|
| `v_c` | 39 436 m/s |
| `Isp` óptimo (5000 m/s) | 3763 s |
| `π` óptima (5000 m/s) | 0,7623 |
| `Isp` óptimo (15 000 m/s) | 3219 s |
| `π` óptima (15 000 m/s) | 0,3794 |

Descripción larga: la carga útil sube con el `Isp` hasta un máximo y luego baja porque la planta crece con `Vₑ²`.

## 13. Ejemplo trabajado

**Paso 1 · Escape.** `Isp = 3000 s` → `Vₑ = 29 420 m/s`.

**Paso 2 · Propelente.** `f_p = 1 − e^(−5000/29 420) = 0,1563`.

**Paso 3 · Planta.** `m_planta/m₀ = f_p α Vₑ²/(2ηt) = 0,1563 × 0,02 × 29 420²/(2 × 0,6 × 2,592×10⁷) = 0,0870`.

**Paso 4 · Fracción útil.** `π = 1 − 0,1563 − 0,0870 = 0,7567`.

## 14. Distintas formas de describir el problema

**Por masas:** propelente, planta y carga. **Por escala:** `Vₑ/v_c`. **Por óptimo:** derivada nula. **Por Δv:** el óptimo se desplaza. **Por potencia:** `P/m₀`.

## 15. Práctica guiada

**Ejercicio 1 · guiado (con los pasos indicados).** Calcula `v_c` con `α = 10 kg/kW`, `η = 0,6`, `t = 300 días`. *Pasos:* `√(2ηt/α)`.

<details><summary>Solución comentada</summary>

`√(2 × 0,6 × 2,592×10⁷/0,01) = 55 770 m/s`.
</details>

**Ejercicio 2 · guiado (con una pista).** Predice si el óptimo sube o baja al bajar `α`. *Pista:* `v_c` crece.

<details><summary>Solución comentada</summary>

Sube: se justifica un mayor escape.
</details>

**Ejercicio 3 · guiado (casi autónomo).** ¿Por qué `π` tiene un máximo interior? *Casi autónomo.*

<details><summary>Solución comentada</summary>

Porque `f_p` decrece con `Vₑ` y la planta crece como `Vₑ²`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Calcula `m_planta/m₀` con `Isp = 1000 s` (laboratorio: `f_p = 0,3994`).

<details><summary>Solución comentada</summary>

`0,3994 × 0,02 × 9807²/(2 × 0,6 × 2,592×10⁷) = 0,0247`.
</details>

**Ejercicio 5 · autónomo.** ¿Qué `π` da `Isp = 8000 s` con `Δv = 5000 m/s`?

<details><summary>Solución comentada</summary>

`0,6939`.
</details>

**Ejercicio 6 · autónomo.** ¿Cuánta potencia por kilo de nave requiere `Isp = 3000 s`?

<details><summary>Solución comentada</summary>

`4,35 W/kg`.
</details>

**Ejercicio 7 · autónomo.** Para una nave de 1000 kg, ¿qué potencia en kW?

<details><summary>Solución comentada</summary>

`4,35 kW`.
</details>

**Ejercicio 8 · autónomo.** Si `t` se duplica, ¿qué pasa con `v_c`?

<details><summary>Solución comentada</summary>

Sube ×√2: se justifica más `Isp` con más tiempo.
</details>

**Ejercicio 9 · transferencia.** Un diseñador elige el `Isp` de máxima `π` sin mirar el tiempo. ¿Qué omite?

<details><summary>Solución comentada</summary>

Que `π` se calculó para un tiempo `t` dado; si el plazo es menor, hace falta más potencia.
</details>

**Ejercicio 10 · transferencia.** ¿Es `α = 20 kg/kW` un valor de alguna planta real?

<details><summary>Solución comentada</summary>

No: es ilustrativo.
</details>

**Ejercicio 11 · transferencia.** ¿Por qué no se usa el óptimo de 5000 m/s para 15 000 m/s?

<details><summary>Solución comentada</summary>

El óptimo depende del Δv: 3763 frente a 3219 s.
</details>

**Ejercicio 12 · integrador.** Elabora tu *curva de carga útil frente a velocidad de escape*: tabla para dos Δv, óptimos por dos vías, `v_c` y qué es ilustrativo.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: carga útil óptima con planta de potencia

El script [nep.py](nep.py) calcula la fracción útil para seis `Isp` y dos Δv y halla el óptimo (**comprueba** el óptimo por sección áurea contra la malla fina dentro de `0,05 %` y que `π` es menor a ambos lados).

**Datos:** `g₀` (NIST) y los paneles de Dawn (NASA/JPL) **consultados**; `α`, `η`, `t` y Δv **ilustrativos**. **Predice antes de ejecutar:** ¿baja o sube el `Isp` óptimo al triplicar el Δv? (baja: de 3763 a 3219 s.) **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
NEP ILUSTRATIVO: alpha = 20 kg/kW, eta = 0.6, t = 300 dias -> v_c = sqrt(2 eta t/alpha) = 39436 m/s
Delta-v = 5000 m/s:
   Isp [s]   Ve [m/s]   f_prop    P/m0 [W/kg]  m_planta/m0   fraccion util
       500       4903   0.6393         0.49       0.0099         0.3508
      1000       9807   0.3994         1.23       0.0247         0.5759
      2000      19613   0.2250         2.78       0.0557         0.7193
      3000      29420   0.1563         4.35       0.0870         0.7567
      5000      49033   0.0969         7.49       0.1499         0.7532
      8000      78453   0.0617        12.22       0.2444         0.6939
  Optimo: Ve = 36906 m/s ; Isp = 3763 s ; fraccion util = 0.7623 ; Ve/v_c = 0.936
Delta-v = 15000 m/s:
   Isp [s]   Ve [m/s]   f_prop    P/m0 [W/kg]  m_planta/m0   fraccion util
       500       4903   0.9531         0.74       0.0147         0.0322
      1000       9807   0.7834         2.42       0.0484         0.1682
      2000      19613   0.5346         6.61       0.1322         0.3332
      3000      29420   0.3994        11.11       0.2223         0.3783
      5000      49033   0.2636        20.37       0.4074         0.3290
      8000      78453   0.1740        34.44       0.6887         0.1372
  Optimo: Ve = 31572 m/s ; Isp = 3219 s ; fraccion util = 0.3794 ; Ve/v_c = 0.801
Planta de 10 kW con alpha = 20 kg/kW: 200 kg (ILUSTRATIVO; Dawn: paneles de mas de 10 kW, consultado)
Pruebas superadas.
```

```bash
python programa/clases/B78/B78-C15-propulsion-nuclear-electrica-conceptual/nep.py
```

**Límites:** planta proporcional a la potencia, sin estructura ni tanques, `η` constante; sin diseño de reactor.

## 18. Errores frecuentes y cómo corregirlos

****Ignorar la masa de la planta.** Se corrige con 8.1.**

****Creer que más `Isp` siempre da más carga.** Se corrige con 8.2.**

****Usar el óptimo de otro Δv.** Se corrige con 8.3.**

****Presentar `α` como dato.** Se corrige con la sección 11.**

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué `π` esperabas con 3000 s y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **curva de carga útil frente a velocidad de escape** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Calcula `π` y el óptimo | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas con unidades | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con una segunda vía | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo ilustrativo y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** no describir ningún reactor; rotular `α`, `η` y `t` como ilustrativos; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa y conceptual: los modelos son simplificados, los datos son consultados con fecha o sintéticos rotulados, y ningún resultado es una especificación de diseño, una verificación de hardware ni una instrucción operativa.  Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Con `α = 20 kg/kW`, la máxima carga útil ilustrativa para `5000 m/s` está en `Isp ≈ 3763 s` y para `15 000 m/s`, en `3219 s`. Queda una pregunta: ¿qué da el límite superior de la energía por kilo de combustible?

**Glosario español–inglés.** masa específica · *specific mass*; carga útil · *payload*; propulsión nuclear-eléctrica · *nuclear electric propulsion*; velocidad característica · *characteristic velocity*; planta de potencia · *power plant*.

**Continuidad.** [B78-C16](../B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md) estudia la propulsión de fusión como investigación.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B78-C14 — Propulsión nuclear térmica conceptual](../B78-C14-propulsion-nuclear-termica-conceptual/CLASE.md) · [📚 Bloque B78](../../../tronco-comun/B78-tecnologias-de-propulsion-espacial.md) · [Siguiente: B78-C16 — Propulsión de fusión como investigación →](../B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md)
<!-- /nav -->
