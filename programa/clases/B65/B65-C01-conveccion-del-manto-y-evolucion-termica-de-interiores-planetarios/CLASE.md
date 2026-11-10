# B65-C01 — Convección del manto y evolución térmica de interiores planetarios

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B65](../../../tronco-comun/B65-geofisica-de-interiores-planetarios.md) · [← Anterior: B64-C07 — Cultivo de extremófilos no patógenos en condiciones análogas](../../B64/B64-C07-cultivo-de-extremofilos-no-patogenos-en-condiciones-analogas/CLASE.md) · [Siguiente: B65-C02 — Dinamos planetarias y campos magnéticos de origen interno →](../B65-C02-dinamos-planetarias-y-campos-magneticos-de-origen-interno/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 1 del bloque B65. Nivel N3. Un manto rocoso es sólido y, sin embargo, fluye en escalas de millones de años. Aquí calculas el **número de Rayleigh** de un manto ilustrativo, compruebas numéricamente el umbral crítico de la inestabilidad de Rayleigh–Bénard y sigues el **enfriamiento parametrizado** de un manto de una sola capa con una escala `Nu ∝ Ra^β`. La estructura interior que se enseña en B53-C01 es el punto de partida; el cálculo usa [B10](../../../tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) solo para el álgebra. Todos los parámetros del manto son **ilustrativos** y no corresponden a ningún planeta.

## 2. Por qué esta clase existe

Sin convección, el interior de un planeta rocoso solo perdería calor por conducción y se enfriaría con una escala de tiempo mucho mayor. La decisión central: **¿cuánto calor saca la convección y a qué temperatura se estabiliza un manto que sigue produciendo calor radiactivo?**

## 3. Lo que podrás hacer al terminar

1. Calcular el número de Rayleigh de una capa de fluido calentada desde abajo y compararlo con el crítico.
2. Obtener el número de Rayleigh crítico de fronteras libres como el mínimo de una curva y contrastarlo con `27π⁴/4`.
3. Usar la escala `Nu ∝ (Ra/Ra_c)^β` para estimar la potencia que sale del manto.
4. Integrar un balance térmico `C dT/dt = H − Q(T)` y contrastarlo con su estado estacionario.
5. Explicar por qué la viscosidad dependiente de la temperatura estabiliza el enfriamiento.
6. Distinguir lo calculado con parámetros ilustrativos de una evolución térmica real.

La evidencia es la **ficha de la convección del manto** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es la conducción del calor?
2. ¿Qué es la viscosidad?
3. ¿Qué es un estado estacionario?
4. ¿Qué es un valor ilustrativo?
5. ¿Qué es una verificación numérica?

<details>
<summary>Ver respuestas</summary>

1. La transferencia de calor por contacto entre partículas, sin movimiento del material. 2. La resistencia de un fluido a fluir. 3. Un estado en que lo que entra es igual a lo que sale y nada cambia con el tiempo. 4. Un valor propuesto para el ejemplo, no medido. 5. Comparar un cálculo con un resultado analítico o independiente.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Una capa de 2 900 km de espesor, con coeficiente de dilatación `3×10⁻⁵ K⁻¹`, densidad `4 000 kg/m³`, `g = 10 m/s²`, difusividad térmica `10⁻⁶ m²/s`, viscosidad `10²¹ Pa·s` y una diferencia de temperatura de 1 327 K tiene `Ra = 3,884×10⁷`, unas 59 000 veces el crítico. Es el **ejemplo conductor**. Todo es **ilustrativo**, de orden de magnitud terrestre, sin ajuste a datos.

## 6. Vocabulario

El **número de Rayleigh** `Ra = α ρ g ΔT d³ / (κ η)` compara el empuje térmico con la disipación por difusión y viscosidad. El **Rayleigh crítico** `Ra_c` es el valor por debajo del cual la capa no convecciona. El **número de Nusselt** `Nu` es el flujo total dividido por el flujo que habría solo por conducción. La **evolución térmica parametrizada** reemplaza la convección completa por una ley `Nu(Ra)`. La **viscosidad de Arrhenius** crece exponencialmente al bajar la temperatura.

## 7. Modelo mental: una olla con una tapa fría

Como una olla calentada por abajo: mientras el fondo esté poco más caliente que la tapa, el calor sube por conducción; al superar un umbral, el fluido se pone en movimiento y el calor sube mucho más rápido.

```mermaid
flowchart LR
    P["parámetros del manto"] --> RA["Ra = α ρ g ΔT d³ / (κ η)"]
    RA --> C{"Ra > Ra_c ?"}
    C -- sí --> NU["Nu = (Ra/Ra_c)^β"]
    NU --> Q["potencia Q(T)"]
    Q --> B["C dT/dt = H − Q(T)"]
    B --> T["T(t) y estado estacionario"]
```

*Descripción textual:* con los parámetros se calcula `Ra`; si supera el crítico, `Nu` fija la potencia que sale; el balance con el calor radiactivo da la temperatura en el tiempo.

Analogía: una olla con tapa fría. Límite: manto de una sola capa, bien mezclado, sin tapa estancada ni flujo desde el núcleo.

## 8. La explicación, paso a paso

### 8.1 El umbral crítico

Para una capa de fluido con fronteras libres, el modo marginal de número de onda horizontal `k` (adimensional, en unidades de `1/d`) exige `Ra(k) = (π² + k²)³ / k²`. El mínimo de esa curva es `Ra_c`. Se encontró con una búsqueda de sección áurea y se contrastó con la solución cerrada:

| Magnitud | Numérico | Analítico |
|---|---|---|
| `Ra_c` | 657,511364 | `27π⁴/4 = 657,511364` |
| `k` en el mínimo | 2,221441 | `π/√2 = 2,221441` |

El error relativo es de `3,5×10⁻¹⁶`. Esta expresión no se consultó en un libro de texto; la verifica el cálculo.

### 8.2 El manto ilustrativo

Con la viscosidad de Arrhenius `η(T) = η₀ exp[E/R (1/T − 1/T_ref)]`, `E = 300 kJ/mol`, `η₀ = 10²¹ Pa·s` a `T_ref = 1 600 K`:

| `T` (K) | `η` (Pa·s) | potencia `Q` (TW) |
|---|---|---|
| 1 500 | 4,50×10²¹ | 19,84 |
| 1 600 | 1,00×10²¹ | — |
| 1 700 | 2,65×10²⁰ | 62,33 |

Un cambio de 200 K en el manto multiplica por 3,1 la potencia: es el **termostato** de la convección.

### 8.3 Estado estacionario y relajación

Con un calor radiactivo constante de 30 TW (ilustrativo), la temperatura de equilibrio hallada por bisección es `1 566,943 K`. Integrando con Runge–Kutta de cuarto orden desde 2 200 K y desde 1 300 K, ambas trayectorias convergen a ese valor (diferencia de `0,001` y `0,003 K` a los 15 Ga). El tiempo de relajación es del orden de `1 Ga`, por eso hace falta mucho tiempo para que el estado final se alcance. Con un calor radiactivo que decae a la mitad cada 2,5 Ga (ilustrativo), la temperatura a los 4,5 Ga desde 2 200 K es `1 467,6 K`.

### 8.4 Lectura

La convección es un sumidero que se ajusta: si el manto se calienta, baja su viscosidad y saca más calor. Por eso la temperatura final casi no depende de la inicial. Pero todos los valores dependen de parámetros ilustrativos: no son una predicción para la Tierra.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `Ra` | número de Rayleigh | — | `3,884×10⁷` (ilustrativo) |
| `Ra_c` | Rayleigh crítico, fronteras libres | — | 657,511 |
| `α` | dilatación térmica | K⁻¹ | `3×10⁻⁵` (ilustrativo) |
| `κ` | difusividad térmica | m²/s | `10⁻⁶` (ilustrativo) |
| `η` | viscosidad | Pa·s | `10²¹` a 1 600 K (ilustrativo) |
| `β` | exponente de `Nu` | — | 1/3 |
| `C` | capacidad térmica efectiva | J/K | `7×10²⁷` (ilustrativo) |
| `H` | calor radiactivo | W | 30 TW (ilustrativo) |

## 10. Convenciones y referencias

Unidades SI; temperaturas en kelvin; tiempo en segundos, con 1 Ga `= 10⁹ × 3,156×10⁷ s`. El manto es una capa esférica de espesor `d = 2 900 km` y área `4πR²` con `R = 6 371 km`, ilustrativos. Sin sistema de referencia espacial: el modelo es de una sola variable (la temperatura media del manto).

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | Ferrick y Korenaga, *Generalizing scaling laws for mantle convection with mixed heating*, arXiv:2304.07660 | https://arxiv.org/abs/2304.07660 | Existen leyes de escala de flujo de calor basadas en la estabilidad de la capa límite térmica | Solo resumen, consultado el 2026-11-09 |
| S2 | Cálculo de la clase | `conveccion.py` | `Ra_c = 27π⁴/4`, estado estacionario, relajación | Verificado numéricamente; fórmulas clásicas **no consultadas** en un texto |

Límites: los parámetros del manto, la ley `β = 1/3` y la capacidad térmica son ilustrativos; no se consultó ninguna fuente que los fije para un cuerpo.

## 12. Cómo ver la convección del manto

| Magnitud | Valor |
|---|---|
| `Ra_c` numérico | 657,511364 |
| `Ra / Ra_c` | `5,907×10⁴` |
| `T` de equilibrio con 30 TW | 1 566,943 K |
| `T` tras 4,5 Ga con calor decreciente | 1 467,6 K |

Descripción larga: la potencia que sale crece con la temperatura más que linealmente, así que el balance con una fuente de calor siempre tiene una solución estable.

## 13. Ejemplo trabajado: el Rayleigh del manto ilustrativo

**Paso 1 · Empuje.** `α ρ g = 3×10⁻⁵ × 4 000 × 10 = 1,2`.

**Paso 2 · Con la diferencia de temperatura.** `1,2 × 1 327 = 1 592,4`.

**Paso 3 · Con el espesor.** `d³ = (2,9×10⁶)³ = 2,4389×10¹⁹ m³`, luego `1 592,4 × 2,4389×10¹⁹ = 3,884×10²²`.

**Paso 4 · Disipación.** `κ η = 10⁻⁶ × 10²¹ = 10¹⁵`; `Ra = 3,884×10⁷`.

## 14. Distintas formas de describir la convección

**Por umbral:** `Ra` frente a `Ra_c`. **Por flujo:** `Nu`. **Por balance:** `C dT/dt = H − Q`. **Por tiempo:** relajación del orden de 1 Ga.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula el número de onda del mínimo, `k = π/√2`. *Pasos:* divide `π` entre `√2`.

<details><summary>Solución comentada</summary>

`2,2214`, igual al hallado por la búsqueda numérica.
</details>

**Ejercicio 2 · con una pista.** Calcula `Ra/Ra_c` para el manto ilustrativo. *Pista:* divide `3,884×10⁷` entre `657,51`.

<details><summary>Solución comentada</summary>

`5,907×10⁴`: el manto ilustrativo está muy por encima del umbral.
</details>

**Ejercicio 3 · casi autónomo.** Con `β = 1/3`, ¿cuánto vale `Nu`?

<details><summary>Solución comentada</summary>

`(5,907×10⁴)^{1/3} ≈ 38,9`: la convección saca unas 39 veces el calor de la conducción pura.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Razón entre las viscosidades a 1 500 K y a 1 700 K.

<details><summary>Solución comentada</summary>

`4,50×10²¹ / 2,65×10²⁰ ≈ 17`.
</details>

**Ejercicio 5.** Razón entre las potencias a 1 700 K y a 1 500 K.

<details><summary>Solución comentada</summary>

`62,33 / 19,84 ≈ 3,14`.
</details>

**Ejercicio 6.** ¿Qué potencia sale del manto en el estado estacionario con `H = 30 TW`?

<details><summary>Solución comentada</summary>

30 TW: en el estado estacionario, lo que sale iguala lo que se produce.
</details>

**Ejercicio 7.** Estima el tiempo de relajación con la pendiente `(62,33 − 19,84) TW / 200 K` y `C = 7×10²⁷ J/K`.

<details><summary>Solución comentada</summary>

Pendiente `2,1×10¹¹ W/K`; `τ ≈ C/pendiente = 3,3×10¹⁶ s ≈ 1,0 Ga`.
</details>

**Ejercicio 8.** Si el espesor de la capa se duplica, ¿cómo cambia `Ra`?

<details><summary>Solución comentada</summary>

Se multiplica por 8 (`d³`): `3,1×10⁸`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un colega dice que el manto «ya está en estado estacionario» porque su temperatura casi no cambia en 100 Ma. Responde.

<details><summary>Solución comentada</summary>

El tiempo de relajación es del orden de 1 Ga, así que en 100 Ma la temperatura cambia poco aunque el sistema esté lejos del equilibrio. Hay que comparar con `τ`.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** Si el manto de otro cuerpo fuera 10 veces más viscoso, ¿cuánto cambia `Nu`?

<details><summary>Solución comentada</summary>

`Ra` baja 10 veces y `Nu ∝ Ra^{1/3}` baja `10^{1/3} = 2,15` veces.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Por qué no se puede decir que `1 567 K` es la temperatura del manto terrestre?

<details><summary>Solución comentada</summary>

Porque todos los parámetros son ilustrativos y el modelo es de una sola capa sin núcleo ni tapa estancada.
</details>

**Ejercicio 12.** **Integrador.** Elabora tu *ficha de la convección del manto*: `Ra`, `Ra_c`, `Nu`, la temperatura de equilibrio y el tiempo de relajación, con unidades y con lo ilustrativo rotulado.

<details><summary>Solución modelo</summary>

Secciones 8.1–8.4 y los ejercicios 2, 3, 6 y 7.
</details>

## 17. Laboratorio: convección y evolución térmica

El script [conveccion.py](conveccion.py) halla el Rayleigh crítico como un mínimo, compara con `27π⁴/4`, calcula el `Ra` del manto ilustrativo y compara la integración de Runge–Kutta con el estado estacionario (**comprueba** el error relativo < 1e-6 y la diferencia < 0,01 K).

**Datos:** sin constantes consultadas; manto **ilustrativo**. **Predice antes de ejecutar:** ¿qué temperatura de equilibrio habrá con 30 TW? (algo menos de 1 600 K.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Ra critico (fronteras libres): numerico = 657.511364 en k = 2.221441 ; analitico 27 pi^4/4 = 657.511364 en k = 2.221441
Error relativo = 3.46e-16
Ra del manto ilustrativo (T = 1600 K, dT = 1327 K): 3.884e+07 ; Ra/Rac = 5.907e+04
Viscosidad a 1500 K / 1600 K / 1700 K: 4.50e+21 / 1.00e+21 / 2.65e+20 Pa s
Potencia de salida a 1500 K = 19.84 TW ; a 1700 K = 62.33 TW
Estado estacionario con H = 30 TW constante: T_ss = 1566.943 K
RK4 desde 2200 K tras 15 Ga: T = 1566.944 K ; |T - T_ss| = 0.0013 K
RK4 desde 1300 K tras 15 Ga: T = 1566.939 K ; |T - T_ss| = 0.0034 K
Con calor radiactivo decreciente (vida media 2.5 Ga, ilustrativa) tras 4.5 Ga desde 2200 K: T = 1467.6 K
Pruebas superadas.
```

```bash
python programa/clases/B65/B65-C01-conveccion-del-manto-y-evolucion-termica-de-interiores-planetarios/conveccion.py
```

**Límites:** manto de una capa, `β = 1/3`, sin tapa estancada ni calor del núcleo.

## 18. Errores frecuentes y cómo corregirlos

**Pensar que un fluido se mueve apenas `Ra > 0`.** Se corrige con 8.1.

**Mezclar kelvin y celsius en `ΔT` y `T`.** Se corrige con la sección 10.

**Confundir equilibrio con «casi no cambia».** Se corrige con el ejercicio 9.

**Presentar `1 567 K` como la temperatura de un planeta.** Se corrige con la sección 11.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de la convección del manto** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Conceptos de la clase | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con el análisis | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha | Declara lo ilustrativo |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular el manto como ilustrativo; no presentar el resultado como el de un planeta real; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

La convección del manto ilustrativo es unas 59 000 veces supercrítica y regula la temperatura con un tiempo de relajación de unos 1 Ga. Queda una pregunta: ¿qué ocurre en el núcleo líquido, donde el movimiento ya no solo transporta calor sino que puede generar un campo magnético?

**Glosario español–inglés.** número de Rayleigh · *Rayleigh number*; número de Nusselt · *Nusselt number*; convección del manto · *mantle convection*; evolución térmica · *thermal evolution*; estado estacionario · *steady state*.

**Continuidad.** [B65-C02](../B65-C02-dinamos-planetarias-y-campos-magneticos-de-origen-interno/CLASE.md) estudia las dinamos planetarias.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B64-C07 — Cultivo de extremófilos no patógenos en condiciones análogas](../../B64/B64-C07-cultivo-de-extremofilos-no-patogenos-en-condiciones-analogas/CLASE.md) · [📚 Bloque B65](../../../tronco-comun/B65-geofisica-de-interiores-planetarios.md) · [Siguiente: B65-C02 — Dinamos planetarias y campos magnéticos de origen interno →](../B65-C02-dinamos-planetarias-y-campos-magneticos-de-origen-interno/CLASE.md)
<!-- /nav -->
