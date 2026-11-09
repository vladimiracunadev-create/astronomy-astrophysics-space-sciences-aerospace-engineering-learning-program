# B24-C20 — Modelo simplificado de estructura estelar

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B24](../../../tronco-comun/B24-fisica-y-evolucion-de-estrellas.md) · [← Anterior: B24-C19 — Cúmulos y edades estelares](../B24-C19-cumulos-y-edades-estelares/CLASE.md) · [Siguiente: B24-C21 — Rama asintótica de gigantes: pulsos térmicos y proceso s →](../../../tronco-comun/B24-fisica-y-evolucion-de-estrellas.md#b24-c21)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 20 del bloque B24, cierre de la malla base. Nivel N3. Reúnes el equilibrio hidrostático ([C04](../B24-C04-equilibrio-hidrostatico-estelar/CLASE.md)), el gas ideal y el solver de Lane–Emden ([C14](../B24-C14-asterosismologia-inicial/CLASE.md), [C18](../B24-C18-etapas-finales-de-evolucion/CLASE.md)) en un **modelo politrópico** completo del Sol, y lo contrastas con valores de referencia. Usas ecuaciones diferenciales ([B11](../../../tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md)) y la validación de software ([B23](../../../tronco-comun/B23-verificacion-y-validacion-de-software-cientifico.md)). Los interiores detallados están en [B37](../../../tronco-comun/B37-interiores-estelares-y-asterosismologia.md).

## 2. Por qué esta clase existe

Un modelo de estructura real resuelve cuatro ecuaciones acopladas con física detallada; un politropo sustituye esa física por una sola relación `P ∝ ρ^{1+1/n}` y permite resolver todo con una ecuación. Es el mejor modo de ver qué se obtiene con poco y qué falta. La decisión central: **¿cuán lejos de los valores de referencia del Sol queda un modelo politrópico de índice 3 y qué dice esa distancia sobre sus supuestos?**

## 3. Lo que podrás hacer al terminar

1. Escribir las ecuaciones de estructura con simetría esférica.
2. Resolver la ecuación de Lane–Emden para `n = 3` y validar el solver.
3. Obtener `ρ_c`, `P_c` y `T_c` de una estrella de masa y radio dados.
4. Verificar internamente el modelo (masa por integral, equilibrio hidrostático).
5. Contrastar el modelo con valores de referencia y explicar las diferencias.
6. Aplicar el modelo a otra estrella por escalas.

La evidencia es el **modelo politrópico validado** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué dice el equilibrio hidrostático (C04)?
2. ¿Qué es un politropo (C14)?
3. ¿Cómo se obtiene la masa interior a partir de la densidad?
4. ¿Qué es la ecuación de estado de un gas ideal?
5. ¿Qué significa validar un código frente a soluciones exactas?

<details>
<summary>Ver respuestas</summary>

1. `dP/dr = −Gmρ/r²`. 2. Un modelo con `P = Kρ^{1+1/n}`. 3. `dm/dr = 4πr²ρ`. 4. `P = ρkT/(μ m_u)`. 5. Comprobar que sus resultados reproducen casos con respuesta conocida (B23).
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa C04, C14 y B23.

## 5. Un caso real: el Sol del modelo estándar de Eddington

El modelo estándar de Eddington es un politropo `n = 3`. Con la masa y el radio nominales del Sol (S2) obtiene una densidad central `54,18` veces la media. El laboratorio lo contrasta con el modelo solar de la NASA, que da `ρ_c = 1,622 × 10⁵ kg/m³`, `P_c = 2,477 × 10¹¹ bar` y `T_c = 1,571 × 10⁷ K` (S3; valores de **modelo**): el politropo obtiene `0,47`, `0,50` y `0,75` de esos valores. Es el **ejemplo conductor**. Los códigos reales como MESA resuelven las ecuaciones completas con ecuación de estado, opacidades y reacciones nucleares (S4, resumen).

## 6. Vocabulario

Las **ecuaciones de estructura estelar** son cuatro: equilibrio hidrostático `dP/dr = −Gmρ/r²`, continuidad de masa `dm/dr = 4πr²ρ`, transporte de energía y generación de energía. El **politropo** de índice `n` cumple `P = Kρ^{1+1/n}`; reduce el problema a Lane–Emden. El **modelo estándar de Eddington** es el politropo `n = 3`. La **escala** `a = R/ξ₁` convierte `ξ` en radio. La **densidad central** es `ρ_c = ρ̄ ξ₁³/(3ω₃)` con `ω₃ = −ξ₁²θ'(ξ₁)`. La **temperatura central** se deduce de la ecuación de estado: `T_c = P_c μ m_u/(ρ_c k)`. La **verificación interna** comprueba que el modelo cumple sus propias ecuaciones. La **validación** compara con datos o referencias externas.

## 7. Modelo mental: sustituir una física difícil por una sola curva

Un politropo fija una relación entre presión y densidad en toda la estrella. Con ella, la estructura queda determinada por la masa y el radio.

```mermaid
flowchart LR
    A["M, R"] --> B["Lane–Emden n=3:<br/>ξ₁, ω₃"]
    B --> C["ρ_c, P_c"]
    C --> D["T_c = P_c μ m_u / (ρ_c k)"]
    D --> E["Contraste con<br/>valores de referencia"]
    E --> F["Qué física falta"]
```

*Descripción textual:* con la masa y el radio, la solución de Lane–Emden da las magnitudes centrales; la temperatura sale de la ecuación de estado; se contrasta con la referencia y la diferencia indica qué física falta.

Analogía: una maqueta a escala 1:1000. Límite: la maqueta reproduce las proporciones, pero no los materiales.

## 8. La explicación, paso a paso

### 8.1 Del problema a Lane–Emden

Con `P = Kρ^{4/3}` (`n = 3`), el equilibrio hidrostático y la continuidad se combinan en `θ'' + 2θ'/ξ + θ³ = 0` con `ρ = ρ_c θ³`, `P = P_c θ⁴`, `r = aξ`. La solución cumple `θ(ξ₁) = 0` con `ξ₁ = 6,89685` y `ω₃ = 2,01824`.

### 8.2 Magnitudes centrales

Con `M = M☉`, `R = R☉` (S2): `ρ̄ = 1410 kg/m³`; `ρ_c = ρ̄ ξ₁³/(3ω₃) = 54,18 ρ̄ = 7,64 × 10⁴ kg/m³`; `P_c = 4πG a² ρ_c²/(n+1) = 1,245 × 10¹⁶ Pa`; y con `μ = 0,6` (estimado), `T_c = 1,176 × 10⁷ K`.

### 8.3 Verificación interna

Se comprueba el solver con casos exactos: `n = 1` (`θ = sen ξ/ξ`, `ξ₁ = π`) y `n = 5` (`θ = (1+ξ²/3)^{−1/2}`). Se integra la masa `∫4πr²ρ dr` y se recupera `M` con error menor de `10⁻³` (el laboratorio: `1,00000`). Se evalúa el equilibrio hidrostático por diferencias finitas a `r = 0,5 R`: `dP/dr` coincide con `−Gmρ/r²` a `0,5 %` (el laboratorio: `1,00000`).

### 8.4 Comparación con la referencia

El politropo da `0,47` de `ρ_c`, `0,50` de `P_c` y `0,75` de `T_c` del modelo solar. Las diferencias son de factor dos en densidad y presión: el Sol real está más concentrado hacia el centro porque su composición cambia con la profundidad (el hidrógeno se ha convertido en helio en el núcleo, C06) y la ecuación de estado no es la politrópica. Es una buena aproximación de orden de magnitud, no un modelo solar.

### 8.5 Escalas a otra estrella

Para otra estrella con `M` y `R`, `ρ_c ∝ M/R³`, `P_c ∝ M²/R⁴` y `T_c ∝ μ M/R`. Una estrella de `0,5 M☉` y `0,5 R☉` tiene `T_c` igual al solar (en el modelo), `ρ_c` cuatro veces mayor y `P_c` cuatro veces mayor.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `ξ₁`, `ω₃` | raíz y masa adimensional (`n = 3`) | — | `6,89685`; `2,01824` |
| `ρ_c/ρ̄` | contraste de densidad | — | `54,18` |
| `ρ_c`, `P_c`, `T_c` | magnitudes centrales (politropo) | `kg m⁻³`; Pa; K | `7,64 × 10⁴`; `1,245 × 10¹⁶`; `1,176 × 10⁷` |
| Referencia (modelo NASA) | magnitudes centrales | `kg m⁻³`; bar; K | `1,622 × 10⁵`; `2,477 × 10¹¹`; `1,571 × 10⁷` (S3) |
| `μ` | masa molecular media | — | `0,6` (estimado) |
| `a` | escala de longitud | m | `R/ξ₁` |

## 10. Convenciones y referencias

Gas ideal; sin presión de radiación explícita; una sola relación `P(ρ)`; `μ = 0,6` **estimado**. Los valores de referencia son de **modelo**, no medidos. `M☉ = GM☉/G`.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NIST, *Fundamental Physical Constants — Complete Listing* (CODATA 2022) | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | `G`, `k`, `m_u` | Consultada el 2026-11-09 |
| S2 | Mamajek et al., *IAU 2015 Resolution B3*, arXiv:1510.07674 | https://arxiv.org/abs/1510.07674 | `GM☉`, `R☉` nominales | Texto del PDF extraído el 2026-11-09 |
| S3 | NASA/NSSDC, *Sun Fact Sheet* (actualizada 2024-05-09) | https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html | `ρ_c`, `P_c`, `T_c` del modelo solar; densidad media | Consultada el 2026-11-09 |
| S4 | Paxton et al., *MESA*, arXiv:1009.1622 | https://arxiv.org/abs/1009.1622 | Código 1-D de evolución con EOS, opacidades y reacciones propias | Solo resumen, consultado el 2026-11-09 |

Límites: S4 solo resumen; las soluciones de Lane–Emden se validan contra casos exactos, no contra una tabla publicada; el contraste con S3 es de orden de magnitud.

## 12. Cómo ver el contraste

| Magnitud | Politropo `n = 3` | Referencia (S3) | Cociente |
|---|---|---|---|
| `ρ_c` (kg/m³) | `7,64 × 10⁴` | `1,622 × 10⁵` | 0,47 |
| `P_c` (Pa) | `1,245 × 10¹⁶` | `2,477 × 10¹⁶` | 0,50 |
| `T_c` (K) | `1,176 × 10⁷` | `1,571 × 10⁷` | 0,75 |

Descripción larga: el politropo subestima la concentración central (densidad y presión a la mitad) y se acerca más en la temperatura.

## 13. Ejemplo trabajado: las magnitudes centrales de una estrella de 0,5 M☉ y 0,5 R☉

**Paso 1 · Datos.** `M = 0,5 M☉`, `R = 0,5 R☉` (ilustrativos).

**Paso 2 · Escalas.** `ρ_c ∝ M/R³ = 0,5/0,125 = 4`; `P_c ∝ M²/R⁴ = 0,25/0,0625 = 4`; `T_c ∝ M/R = 1`.

**Paso 3 · Valores.** `ρ_c = 3,06 × 10⁵ kg/m³`; `P_c = 4,98 × 10¹⁶ Pa`; `T_c = 1,176 × 10⁷ K`.

**Paso 4 · Sentido.** Es un resultado del politropo; la temperatura central de una estrella real de esta masa se obtendría con un modelo completo.

## 14. Distintas formas de modelar una estrella

**Politropo (esta clase):** una ecuación, escalas claras. **Modelo con ecuación de estado completa:** requiere opacidades y reacciones. **Códigos de evolución:** modelan además el cambio de composición con el tiempo (S4, resumen). Se usan en cadena.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `ρ_c/ρ̄` para `n = 3`. *Pasos:* `ξ₁³/(3ω₃)`.

<details><summary>Solución comentada</summary>

`6,89685³ = 328,0`; `/(3 × 2,01824) = 54,18` (8.2).
</details>

**Ejercicio 2 · con una pista.** Calcula `ρ_c` con `ρ̄ = 1410 kg/m³`. *Pista:* multiplica.

<details><summary>Solución comentada</summary>

`54,18 × 1410 = 7,64 × 10⁴ kg/m³`.
</details>

**Ejercicio 3 · casi autónomo.** Calcula el cociente `T_c(modelo)/T_c(referencia)`.

<details><summary>Solución comentada</summary>

`1,176 × 10⁷/1,571 × 10⁷ = 0,75`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** ¿Cuál es la presión central del politropo en bar?

<details><summary>Solución comentada</summary>

`1,245 × 10¹⁶ Pa = 1,245 × 10¹¹ bar`.
</details>

**Ejercicio 5.** ¿Cuántas veces menor es `P_c` del modelo que la de referencia?

<details><summary>Solución comentada</summary>

`2,477/1,245 = 1,99` veces.
</details>

**Ejercicio 6.** Si `μ` fuera `0,85` (gas neutro), ¿cuánto sería `T_c` del politropo?

<details><summary>Solución comentada</summary>

`T_c ∝ μ`: `1,176 × 10⁷ × 0,85/0,6 = 1,67 × 10⁷ K`. Muestra la sensibilidad a la composición; el valor de `μ` correcto para el centro es el del gas ionizado (8.2).
</details>

**Ejercicio 7.** ¿Qué valida el caso `n = 5` del solver?

<details><summary>Solución comentada</summary>

Que el código reproduce `θ = (1+ξ²/3)^{−1/2}`, una solución exacta de Lane–Emden (8.3).
</details>

**Ejercicio 8.** ¿Qué debería dar la integral de masa del modelo?

<details><summary>Solución comentada</summary>

Exactamente `M` (el laboratorio: `1,00000`).
</details>

**Ejercicio 9 · transferencia.** Compara la presión central uniforme de C04 (`1,34 × 10¹⁴ Pa`) con la del politropo.

<details><summary>Solución comentada</summary>

`1,245 × 10¹⁶/1,34 × 10¹⁴ = 93`: el politropo, más concentrado, ya recoge la mitad de la diferencia con la referencia (`184`).
</details>

**Ejercicio 10 · transferencia.** Un compañero dice que el politropo es el modelo solar. Responde con 8.4.

<details><summary>Solución comentada</summary>

No: se queda en factores de dos en la densidad y la presión centrales; omite el cambio de composición, la ecuación de estado detallada y la generación de energía.
</details>

**Ejercicio 11 · transferencia.** Para una estrella de `2 M☉` y `1,6 R☉` (ilustrativa), ¿cuánto vale `T_c` del politropo?

<details><summary>Solución comentada</summary>

`T_c ∝ M/R`: `1,176 × 10⁷ × 2/1,6 = 1,47 × 10⁷ K`.
</details>

**Ejercicio 12 · integrador.** Elabora tu *modelo politrópico validado*: valida el solver con `n = 1` y `n = 5`, calcula `ρ_c`, `P_c` y `T_c` del Sol, verifica la masa y el equilibrio, contrasta con la referencia y explica una diferencia.

<details><summary>Solución modelo</summary>

`ξ₁ = π`; `n = 5` exacto; `ρ_c = 7,64 × 10⁴`, `P_c = 1,245 × 10¹⁶`, `T_c = 1,176 × 10⁷`; masa `1,00000`, equilibrio `1,00000`; cocientes `0,47`, `0,50`, `0,75`; diferencia explicada por la composición y la ecuación de estado.
</details>

## 17. Laboratorio: politropo solar

El script [politropo_solar.py](politropo_solar.py) resuelve Lane–Emden con RK4, **comprueba** `n = 1` (`ξ₁ = π`) y `n = 5` (solución analítica), **verifica** que la masa por integración reproduce `M` (`10⁻³`) y el equilibrio hidrostático por diferencias finitas (`5 × 10⁻³`), y compara con la referencia de la NASA.

**Datos:** `G`, `k`, `m_u` de NIST; `GM☉`, `R☉` de la IAU; referencia de modelo de la NASA; `μ = 0,6` estimado. **Predice antes de ejecutar:** ¿el politropo dará `ρ_c` mayor o menor que la referencia? (menor.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
solver validado: n=1 xi1 = 3.141593 ; n=5 verificado en xi = 5.000
n=3: xi1 = 6.89685 ; omega_3 = 2.01824 ; rho_c/rho_medio = 54.18
masa por integral / M = 1.00000 ; dP/dr / (-G m rho/r^2) a r = 0.50 R = 1.00000
                   politropo  referencia  cociente
rho_c [kg/m3]     7.6385e+04  1.6220e+05      0.47
P_c [Pa]          1.2449e+16  2.4770e+16      0.50
T_c [K]           1.1760e+07  1.5710e+07      0.75
Pruebas superadas.
```

```bash
python programa/clases/B24/B24-C20-modelo-simplificado-de-estructura-estelar/politropo_solar.py
```

**Límites:** una sola relación `P(ρ)`, `μ` uniforme, sin radiación explícita ni reacciones.

## 18. Errores frecuentes y cómo corregirlos

**Tomar el politropo por un modelo solar.** Se corrige con el ejercicio 10.

**Olvidar `ξ₁³` en la densidad central.** Se corrige con el ejercicio 1.

**Mezclar bar y pascal.** Se corrige con el ejercicio 4.

**Creer que `T_c` es independiente de la composición.** Se corrige con el ejercicio 6.

**Validar solo con un caso.** Se corrige con el ejercicio 7.

## 19. Cómo sabrás que vas bien

Tras 8.2: ¿cuánto vale `ρ_c/ρ̄`? Si dudas, ejercicio 1. Tras 8.4: ¿por qué difiere de la referencia? Ejercicio 10. Tras el laboratorio: ¿qué comprueban la masa y el equilibrio? (que el modelo cumple sus propias ecuaciones).

## 20. Qué entregas y cómo se evalúa

El producto es tu **modelo politrópico validado** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Ecuaciones | No las plantea | Parciales | Lane–Emden y magnitudes | Deduce las escalas |
| Cálculo | Sin unidades | Con errores | `ρ_c`, `P_c`, `T_c` | Aplica a otra estrella |
| Verificación | Sin comprobar | Un caso | Solver, masa y equilibrio | Distingue verificación y validación |
| Fuentes | Sin fuente | Sin fecha | S1–S4 con fecha | Rotula modelo frente a medida |
| Interpretación | Sin sentido físico | Parcial | Explica la diferencia | Propone qué añadir |

**Condiciones críticas (no se compensan con promedio):** rotular los valores de referencia como de modelo; no presentar el politropo como modelo solar; citar solo lo consultado y decir que S4 es resumen.

## 21. Ética, seguridad y límites

Clase educativa: no sustituye un código de estructura y evolución estelar. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Un politropo `n = 3` con la masa y el radio del Sol da valores centrales dentro de un factor dos de la referencia; el solver se valida con casos exactos y el modelo, con sus propias ecuaciones. Con esto cierras la malla base del bloque. Quedan dos temas que la malla trataba solo en general: la fase AGB y la evolución en sistemas binarios.

**Glosario español–inglés.** ecuaciones de estructura estelar · *stellar structure equations*; politropo · *polytrope*; modelo estándar de Eddington · *Eddington standard model*; densidad central · *central density*; verificación · *verification*; validación · *validation*.

**Continuidad.** [B24-C21](../B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md) reutiliza la estructura de capas para estudiar los pulsos térmicos de la fase AGB.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B24-C19 — Cúmulos y edades estelares](../B24-C19-cumulos-y-edades-estelares/CLASE.md) · [📚 Bloque B24](../../../tronco-comun/B24-fisica-y-evolucion-de-estrellas.md) · [Siguiente: B24-C21 — Rama asintótica de gigantes: pulsos térmicos y proceso s →](../../../tronco-comun/B24-fisica-y-evolucion-de-estrellas.md#b24-c21)
<!-- /nav -->
