# B16-C03 — Sistemas lineales invariantes

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B16](../../../tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) · [← Anterior: B16-C02 — Representaciones en espacio de estados](../B16-C02-representaciones-en-espacio-de-estados/CLASE.md) · [Siguiente: B16-C04 — Respuesta transitoria y estacionaria →](../B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Tercera clase del bloque B16. En [C02](../B16-C02-representaciones-en-espacio-de-estados/CLASE.md) aprendiste a escribir `ẋ = A x + B u`. Ahora precisas qué significa que un sistema sea **lineal** e **invariante en el tiempo** (LTI), por qué esas dos propiedades dan tanto poder y cómo se calcula la salida con la **respuesta al impulso** y la **convolución**. Necesitas integrales definidas (B09) y exponenciales.

No verás aún las métricas de calidad de la respuesta (C04) ni la transformada de Laplace (C05).

## 2. Por qué esta clase existe

Un ingeniero de control no puede ensayar todos los pares posibles en un telescopio de miles de millones de euros. La esperanza es que, con unas pocas pruebas, se pueda predecir la respuesta a **cualquier** par. Eso solo es cierto si el sistema es LTI. La pregunta motivadora es: **¿qué propiedades debe tener un sistema para que baste conocer su reacción a un único golpe para saber su reacción a cualquier entrada?**

La decisión central: ¿puedo tratar este sistema como LTI, y hasta qué amplitud de entrada? Responderla bien separa un diseño que funciona de uno que falla al saturarse.

## 3. Lo que podrás hacer al terminar

1. Enunciar y comprobar numéricamente la superposición y la invariancia en el tiempo.
2. Obtener la respuesta al impulso de un sistema de primer orden.
3. Calcular la salida de un LTI con la integral de convolución.
4. Decidir si un sistema dado es LTI y justificarlo con un contraejemplo cuando no lo es.
5. Leer la estabilidad de un LTI en los autovalores de `A`.
6. Explicar por qué la saturación de un actuador rompe la linealidad.

La evidencia es la **auditoría LTI** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. Si `f(x) = 3x`, ¿cuánto vale `f(2a + 5b)` en función de `f(a)` y `f(b)`?
2. Calcula `∫₀^t e^(−s) ds`.
3. ¿Qué autovalor tiene la ecuación `ẋ = −0,2 x`? ¿Qué constante de tiempo?
4. ¿Qué es un impulso? (Describe con tus palabras un golpe muy corto.)
5. ¿Es `y = u²` lineal en `u`?

<details>
<summary>Ver respuestas</summary>

1. `2 f(a) + 5 f(b)`. 2. `1 − e^(−t)`. 3. `−0,2 s⁻¹`; constante de tiempo `5 s`. 4. Una entrada muy intensa durante un tiempo muy corto con área (efecto total) finita. 5. No: `(2u)² = 4u² ≠ 2u²`.
</details>

## 5. Un caso real: el amortiguamiento de una rueda

Las ruedas de reacción del Hubble, que giran hasta unas 3000 rpm (fuente S1), tienen fricción en sus cojinetes: cuanto más rápido giran, más par de frenado oponen. Un modelo simple y muy usado es el amortiguamiento viscoso, proporcional a la velocidad: `J ω̇ + c ω = τ`. Es lineal. Con las cifras sintéticas de esta clase (`J = 50 kg·m²`, `c = 10 N·m·s/rad`) la constante de tiempo es `J/c = 5 s`. Si el par pedido supera lo que el motor puede dar, aparece una **saturación**, que no es lineal y que rompe todo lo que sigue. Esa es la tensión de la clase.

## 6. Vocabulario

Un sistema es **lineal** si cumple **aditividad** (la respuesta a `u₁ + u₂` es la suma de respuestas) y **homogeneidad** (la respuesta a `a u` es `a` por la respuesta a `u`); juntas, **superposición**. Es **invariante en el tiempo** si retrasar la entrada `d` segundos solo retrasa la salida `d` segundos. La **respuesta al impulso** `h(t)` es la salida cuando la entrada es un impulso (delta de Dirac) en `t = 0` desde reposo. La **convolución** de `h` y `u` es `(h∗u)(t) = ∫₀ᵗ h(t−s) u(s) ds` (fuente S2). Un LTI es **estable** (en el sentido que usaremos) si su respuesta al impulso tiende a cero.

## 7. Modelo mental: una receta que se suma

La respuesta de un LTI a una entrada cualquiera es la suma de las respuestas a muchos pequeños golpes: cada instante `s` aporta `u(s)` veces la respuesta al impulso, retrasada `t−s`. Es como una piscina: cada gota hace ondas iguales, y las ondas se suman.

```mermaid
flowchart LR
    u["entrada u(t)<br/>muchos golpes pequeños"] --> h["respuesta al impulso h(t)<br/>la onda de un golpe"]
    h --> y["salida y(t)<br/>suma de ondas retrasadas"]
```

*Descripción textual:* la entrada se descompone en golpes; cada golpe genera una onda `h`; la salida suma todas las ondas, cada una desplazada al instante de su golpe y escalada por su intensidad.

La analogía de las gotas tiene un límite: en un recipiente real, ondas muy grandes chocan y no se suman (no linealidad), igual que un motor que se satura.

## 8. La explicación, paso a paso

### 8.1 Qué significa cada propiedad

Superposición: si `u₁ → y₁` y `u₂ → y₂`, entonces `a u₁ + b u₂ → a y₁ + b y₂`. Invariancia: si `u(t) → y(t)`, entonces `u(t−d) → y(t−d)`. Ambas se verifican en un LTI como `ẋ = A x + B u`, `y = C x + D u` con `A, B, C, D` constantes (C02), partiendo de reposo.

### 8.2 La respuesta al impulso del eje con fricción

Para `J ω̇ + c ω = τ`, la respuesta al impulso de par es `h(t) = e^(−c t/J)/J` para `t ≥ 0` (el impulso fija `ω(0⁺) = 1/J` y luego decae). Con `J = 50`, `c = 10`: `h(t) = 0,02 e^(−0,2 t)` rad/s por unidad de impulso (N·m·s). El impulso es una idealización útil: lo que se mide en la práctica es un golpe corto.

### 8.3 La integral de convolución

Con `h` conocida, la salida a cualquier par es `ω(t) = ∫₀ᵗ h(t−s) τ(s) ds` (S2: ecuaciones 1.14.30 y 1.14.31 para la convolución y su transformada). Si `τ` es un escalón de 1 N·m, `ω(t) = (1/c)(1 − e^(−c t/J)) = 0,1(1 − e^(−0,2 t))` rad/s. Observa el valor final `1/c = 0,1 rad/s` por N·m: para esta fricción, un par de 1 N·m mantiene al eje a 0,1 rad/s.

### 8.4 Estabilidad: los autovalores de `A`

La respuesta al impulso de un LTI es combinación de exponenciales `e^(λt)`, con `λ` los autovalores de `A` (C02, B10-C08). Si todos tienen parte real negativa, `h(t) → 0` y el sistema es estable. Aquí `λ = −c/J = −0,2 s⁻¹`: estable con constante de tiempo 5 s. El eje sin fricción (C01) tiene dos autovalores cero: no es estable en este sentido (se escapa con un par constante).

### 8.5 Cuándo deja de ser lineal

Un actuador real no entrega cualquier par: tiene un máximo `±τ_max`. La función `sat(τ) = clip(τ, −τ_max, τ_max)` viola la homogeneidad: si `τ_max = 0,2` y pides 0,15, obtienes 0,15; si pides el doble (0,30), obtienes 0,20 y no 0,30. Otros ejemplos: zona muerta, histéresis, parámetros que cambian (variante). Un LTI también supone reposo inicial en esta definición; con condiciones iniciales no nulas se suma la respuesta libre.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Nota |
|---|---|---|---|
| `h(t)` | respuesta al impulso (de par a velocidad) | rad/s por N·m·s | `= e^(−ct/J)/J` |
| `u, τ` | entrada (par) | N·m | |
| `c` | amortiguamiento viscoso | N·m·s/rad | sintético: 10 |
| `J` | inercia | kg·m² | 50 |
| `λ` | autovalor de `A` | s⁻¹ | `−c/J` |
| `τ_max` | par máximo del actuador | N·m | sintético: 0,2 |

## 10. Convenciones y referencias

Se asume reposo en `t = 0` salvo que se diga lo contrario. El impulso se mide en N·m·s (par × tiempo). Se distingue «lineal» (superposición) de «lineal a trozos»: la saturación es lineal a trozos, no lineal. La convolución se escribe con `∗`; no la confundas con el producto.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA GSFC, *Pointing Control System* (archivo del Hubble, actualizada 2021-03-29) | https://asd.gsfc.nasa.gov/archive/hubble/technology/pcs.html | Ruedas de reacción de hasta 3000 rpm; magnetopares que gestionan su velocidad | Consultada el 2026-11-05; archivada |
| S2 | NIST, *Digital Library of Mathematical Functions*, §1.14(iii), versión citada 1.2.0 (2024-03-27) | https://dlmf.nist.gov/1.14 | Convolución `(f∗g)(t)=∫₀ᵗ f(u)g(t−u)du` (1.14.30) y `ℒ(f∗g)=ℒ(f)ℒ(g)` (1.14.31) | Consultada el 2026-11-05 mediante extracción automática (se leyeron los primeros 100 000 caracteres) |

Límites: la definición de superposición, la respuesta al impulso del sistema de primer orden y la relación con los autovalores son resultados estándar de teoría de sistemas, no citados a un texto, y se verifican numéricamente. Las cifras son **sintéticas**; el amortiguamiento viscoso es una idealización de la fricción real.

## 12. Cómo ver la superposición

| Entrada | Salida a los 10 s | Qué se comprueba |
|---|---|---|
| `u₁` (sinusoide de 0,3 N·m) | `y₁` | respuesta simple |
| `u₂` (escalón de 0,1 N·m desde 5 s) | `y₂` | respuesta simple |
| `2u₁ + 3u₂` | `2y₁ + 3y₂` | superposición (error numérico 10⁻¹³) |
| `u₁` retrasada 7 s | `y₁` retrasada 7 s | invariancia (error 10⁻¹³) |

Si lo grafiques, usa una línea continua para `y(2u₁+3u₂)` y marcadores para `2y₁+3y₂`: deben superponerse.

## 13. Ejemplo trabajado: la sinusoide en un eje con fricción

Entrada: `τ(t) = 0,3 sen(0,5 t)` N·m aplicada al eje con `J = 50`, `c = 10` desde reposo. Se pide la velocidad.

**Paso 1 · respuesta al impulso.** `h(t) = 0,02 e^(−0,2 t)`.
**Paso 2 · convolución.** `ω(t) = ∫₀ᵗ 0,02 e^(−0,2 (t−s)) · 0,3 sen(0,5 s) ds`. Se puede integrar a mano con la fórmula de exponencial por seno, o numéricamente.
**Paso 3 · comprobación.** Para `t` grande el régimen permanente es una sinusoide de la misma frecuencia con amplitud `0,3/√(c² + (J·0,5)²) = 0,3/√(100 + 625) = 0,3/26,93 = 0,01114 rad/s` y retraso de fase `arctan(25/10) = 68,2°`. El laboratorio calcula la convolución numérica y la compara con la integración directa de la ecuación: coinciden con error relativo 2×10⁻⁸.
**Paso 4 · lectura.** Una entrada sinusoidal en un LTI produce una salida sinusoidal de **la misma frecuencia**: eso es lo que explotará el análisis de frecuencia (C10).

## 14. Distintos modos de obtener la salida de un LTI

Se puede **integrar la ecuación diferencial** (funciona con cualquier entrada y también con no linealidades), **convolucionar** con `h` (sólo LTI, útil cuando se mide `h`), usar la **exponencial matricial** (C02) o la **transformada** (C05). La convolución es cara cuando `t` es grande; la integración se complica si el paso es pequeño y la dinámica es rápida y lenta a la vez; todas coinciden en un LTI y ninguna basta cuando aparece una saturación.

## 15. Práctica guiada

**Ejercicio 1 · con pasos.** Para `ẏ = −2y + u` con reposo inicial, `u₁ → y₁(1) = 0,3` y `u₂ → y₂(1) = 0,1`. ¿Cuánto vale `y(1)` si `u = 2u₁ − 5u₂`? *Pasos:* aplica la superposición (8.1).

<details><summary>Solución comentada</summary>

`y(1) = 2·0,3 − 5·0,1 = 0,1`. El sistema es lineal; el coeficiente −2 no cambia nada.
</details>

**Ejercicio 2 · con pista.** Halla la respuesta al impulso de `J ω̇ + c ω = τ` para `J = 20`, `c = 4`; calcula `h(5)`. *Pista:* 8.2.

<details><summary>Solución comentada</summary>

`h(t) = e^(−0,2 t)/20`; `h(5) = e^(−1)/20 = 0,01839`.
</details>

**Ejercicio 3 · casi autónomo.** Clasifica como LTI o no: (a) `y = u(t−3)`; (b) `y = u²`; (c) `y = t·u(t)`.

<details><summary>Solución comentada</summary>

(a) Es LTI (un retardo). (b) No es lineal (viola homogeneidad). (c) Es lineal pero variante (el factor `t` depende del tiempo).
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Con la convolución, deduce el valor final de la velocidad ante un escalón de 1 N·m en el eje de `J=50`, `c=10`, y la velocidad a los 5 s. *(8.3.)*

<details><summary>Solución comentada</summary>

Final `1/c = 0,1 rad/s`; a 5 s: `0,1(1 − e^(−1)) = 0,0632 rad/s`.
</details>

**Ejercicio 5.** Retrasa el escalón del ejercicio 4 en 7 s. ¿Cuál es la velocidad a los 12 s?

<details><summary>Solución comentada</summary>

Por invariancia: la misma de 5 s tras el escalón, `0,0632 rad/s`.
</details>

**Ejercicio 6.** Si `y₁(10) = 0,02` ante `u₁` y `y₂(10) = 0,05` ante `u₂`, ¿cuánto vale `y(10)` ante `3u₁ − 2u₂`?

<details><summary>Solución comentada</summary>

`3·0,02 − 2·0,05 = −0,04`.
</details>

**Ejercicio 7.** Con saturación a ±0,2 N·m, muestra que `sat(2u) ≠ 2 sat(u)` para `u = 0,15`.

<details><summary>Solución comentada</summary>

`sat(0,15) = 0,15` y `2·0,15 = 0,30`; pero `sat(0,30) = 0,20 ≠ 0,30`. La homogeneidad falla.
</details>

**Ejercicio 8.** Calcula el autovalor y la constante de tiempo de `J = 20`, `c = 8`. ¿Es estable?

<details><summary>Solución comentada</summary>

`λ = −c/J = −0,4 s⁻¹`; constante `2,5 s`; estable.
</details>

**Ejercicio 9 · transferencia.** Un detector se enfría: `C_t Ṫ = P − (T − T_e)/R`, con capacidad térmica `C_t`, potencia `P` y resistencia térmica `R`. Define `δ = T − T_eq` en torno al equilibrio. ¿Es LTI en `δ` y `δP`?

<details><summary>Solución comentada</summary>

Sí: `C_t δ̇ = δP − δ/R` es lineal e invariante. La temperatura absoluta no cumple superposición (hay término constante), pero las desviaciones sí. Es la idea de linealizar en torno a un punto (C17).
</details>

**Ejercicio 10 · transferencia.** Un panel flexible añade al eje un modo oscilante. ¿Sigue siendo LTI el modelo? ¿Qué cambia en la respuesta al impulso?

<details><summary>Solución comentada</summary>

Sí, mientras sea una masa-resorte lineal (C02, 8.5). La respuesta al impulso suma exponenciales amortiguadas oscilantes; si el amortiguamiento es muy pequeño tarda mucho en desaparecer.
</details>

**Ejercicio 11 · transferencia.** Explica por qué un resultado obtenido con pares pequeños (LTI) no garantiza el comportamiento con maniobras grandes (saturación).

<details><summary>Solución comentada</summary>

Porque la superposición vale mientras el actuador esté dentro de su rango; al saturar, escalar la entrada no escala la salida y todo el análisis lineal pierde validez (C18).
</details>

**Ejercicio 12 · integrador.** Entrega una **auditoría LTI**: para un sistema real que elijas (eje, rueda, detector), lista cada hipótesis que lo haría LTI, qué la rompería (saturación, parámetros variables, retardo), un rango de amplitud donde vale y un ensayo numérico de superposición e invariancia.

<details><summary>Solución modelo</summary>

Una auditoría correcta enumera las hipótesis con valores (por ejemplo `|τ| ≤ 0,2 N·m`), muestra al menos un contraejemplo que rompe la linealidad, y adjunta el ensayo con el error de superposición y de invariancia.
</details>

## 17. Laboratorio: superposición, invariancia y convolución

El script [superposicion_e_invariancia.py](superposicion_e_invariancia.py) integra con `solve_ivp` (Radau) la ecuación con fricción, verifica superposición e invariancia, compara la convolución con la integración directa y muestra que la saturación viola la homogeneidad.

**Datos:** sintéticos (simulados). **Predice:** errores del orden de 10⁻¹³ en las dos primeras pruebas y una violación del orden de 10⁻² con saturación. **Ejecución del 2026-11-05 (Python 3.12.9, numpy 2.4.4, scipy 1.17.1):**

```text
superposición: max|y(2u1+3u2) - (2y1+3y2)| = 2.02e-13 rad/s
invariancia: max|y_retrasada - retraso(y)| = 9.15e-14 rad/s
convolución vs ODE: error relativo máx = 2.26e-08
con saturación a 0.2 N m: max|y(2u) - 2y(u)| = 1.094e-02 rad/s (≠ 0)
Pruebas superadas.
```

```bash
python programa/clases/B16/B16-C03-sistemas-lineales-invariantes/superposicion_e_invariancia.py
```

**Límites:** fricción viscosa ideal; el script detiene la ejecución si la superposición falla por encima de 10⁻⁸.

## 18. Errores frecuentes y cómo corregirlos

**Llamar lineal a cualquier modelo con una recta.** La saturación parece una recta a trozos y no lo es. Se corrige con el ejercicio 7.

**Olvidar las condiciones iniciales.** Superposición exige reposo o separar la respuesta libre. Se corrige releyendo 8.5.

**Confundir convolución con producto.** Se corrige con el ejercicio 4.

**Suponer invariancia con parámetros que cambian.** Se corrige con el ejercicio 3.

**Extrapolar fuera del rango del actuador.** Se corrige con el ejercicio 11.

## 19. Cómo sabrás que vas bien

Tras 8.1: ¿enuncias superposición e invariancia con ejemplos propios? Ejercicio 1. Tras 8.3: ¿obtienes el escalón por convolución? Ejercicio 4. Tras el ejemplo: ¿explicas por qué la salida es sinusoidal con otra fase? Al final: ¿tu auditoría indica el rango de amplitudes?

## 20. Qué entregas y cómo se evalúa

El producto es la **auditoría LTI** del ejercicio 12.

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Hipótesis | No las lista | Las lista sin valores | Las lista con valores | Las vincula con un actuador real |
| Contraejemplo | No hay | Verbal | Numérico | Cuantificado |
| Ensayo | Sin ensayo | Un ensayo | Superposición e invariancia | Con tolerancias justificadas |
| Fuentes y datos | Sin rótulo | Parcial | Rotula sintético | Cita solo lo consultado |

**Condiciones críticas:** declarar el rango de validez; no llamar LTI a un sistema saturado; rotular los datos sintéticos.

## 21. Ética, seguridad y límites

Declarar un sistema LTI sin decir en qué rango es una promesa que el hardware puede romper. Las cifras son didácticas. Accesibilidad: tablas con descripción; laboratorio sin conexión.

## 22. Para cerrar y seguir

Un sistema LTI cumple superposición e invariancia; su salida es la convolución de la entrada con la respuesta al impulso; su estabilidad se lee en los autovalores. La saturación, los parámetros variables y las no linealidades rompen esas propiedades. Queda abierto: ¿cómo se describe la calidad de la respuesta (rapidez, sobreimpulso, error)?

**Glosario español–inglés.** superposición · *superposition*; invariancia temporal · *time invariance*; respuesta al impulso · *impulse response*; convolución · *convolution*; saturación · *saturation*; amortiguamiento viscoso · *viscous damping*.

**Continuidad.** B16-C04 mide la respuesta transitoria y estacionaria. B16-C05 pasa la convolución a un producto con la transformada de Laplace. B16-C18 trata la saturación. Para la convolución en señales, ver B15-C08.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B16-C02 — Representaciones en espacio de estados](../B16-C02-representaciones-en-espacio-de-estados/CLASE.md) · [📚 Bloque B16](../../../tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md) · [Siguiente: B16-C04 — Respuesta transitoria y estacionaria →](../B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md)
<!-- /nav -->
