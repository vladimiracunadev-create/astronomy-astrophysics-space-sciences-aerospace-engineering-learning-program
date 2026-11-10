# B58-C02 — Dinámica de asteroides

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B58](../../../tronco-comun/B58-asteroides-cometas-y-defensa-planetaria.md) · [← Anterior: B58-C01 — Clasificación de cuerpos menores](../B58-C01-clasificacion-de-cuerpos-menores/CLASE.md) · [Siguiente: B58-C03 — Composición de asteroides →](../B58-C03-composicion-de-asteroides/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 2 del bloque B58 (nivel N3). Después de clasificar el objeto, ¿cómo se mueve? Aquí integras numéricamente el problema de dos cuerpos con un esquema simpléctico de segundo orden y lo contrastas con la tercera ley de Kepler; luego calculas dónde caen las resonancias de movimiento medio con Júpiter. Trabajas con una órbita **sintética**.

## 2. Por qué esta clase existe

Predecir la posición de un asteroide dentro de décadas exige un integrador que se pueda **verificar**. Saber que un esquema numérico converge con el orden esperado es lo que da confianza antes de añadir perturbaciones. La decisión central: **¿cuánto error de periodo introduce un paso de tiempo dado y dónde espera uno que Júpiter organice las órbitas?**

## 3. Lo que podrás hacer al terminar

1. Escribir las ecuaciones de movimiento de dos cuerpos en au y días.
2. Integrar con kick–drift–kick y medir el periodo de una órbita.
3. Verificar la tercera ley de Kepler y el orden de convergencia del esquema.
4. Calcular el semieje de una resonancia `p:q` con Júpiter.
5. Distinguir una resonancia de periodos de una dinámica resonante.
6. Declarar los supuestos del modelo de dos cuerpos.

La evidencia es la **ficha de dinámica orbital** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué dice la tercera ley de Kepler?
2. ¿Qué es un integrador numérico de orden 2?
3. ¿Qué es el perihelio?
4. ¿Qué es un periodo orbital?
5. ¿Qué es una resonancia de movimiento medio?

<details>
<summary>Ver respuestas</summary>

1. `P² ∝ a³`; en au y años `P² = a³`. 2. Uno cuyo error global baja como el cuadrado del paso. 3. El punto de la órbita más cercano al Sol. 4. El tiempo de una vuelta completa. 5. Una relación de números enteros pequeños entre dos periodos orbitales.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

El ejemplo conductor es un asteroide sintético con `a = 2,2 au` y `e = 0,3`. Su periodo analítico es `1191.8798 d` (`3.263` años). Con paso `0,05 d` el integrador lo reproduce con un error de `7.94e-05 d`, y cada vez que se divide el paso por dos el error baja con orden `2.00`, el esperado para un esquema de segundo orden. Una resonancia 3:1 con Júpiter cae en `2.502 au`.

## 6. Vocabulario

El problema de **dos cuerpos** describe un punto en el campo de una masa central. El **leapfrog** (kick–drift–kick) alterna medio paso de velocidad, un paso de posición y otro medio de velocidad; es **simpléctico**: conserva la estructura hamiltoniana y su energía oscila sin derivar. El **orden** del esquema indica cómo escala su error con el paso. Una **resonancia de movimiento medio** `p:q` ocurre cuando `P_ast/P_J = q/p`. Un **hueco de Kirkwood** es una región con pocos asteroides cerca de una resonancia.

## 7. Modelo mental: avanzar con pasos de baile

```mermaid
flowchart LR
    X["posición y velocidad"] --> A["aceleración<br/>-GM r / r^3"]
    A --> K["medio kick"]
    K --> D["drift"]
    D --> A2["nueva aceleración"]
    A2 --> K2["medio kick"]
    K2 --> X
```

*Descripción textual:* el estado se actualiza con medio impulso de velocidad, un desplazamiento y otro medio impulso, y el ciclo se repite hasta cerrar la órbita.

Analogía: Como un baile de tres pasos que se repite: medio giro, un paso, medio giro. Límite: el esquema solo conserva la energía en promedio; con pasos grandes en una órbita excéntrica el error se concentra en el perihelio.

## 8. La explicación, paso a paso

### 8.1 Las ecuaciones

Con `GM = k²` y `k = 0,01720209895 au^1,5/día` (constante de Gauss, valor histórico no consultado aquí), la aceleración es `−GM r/r³`. El periodo analítico es `P = 2π a^1,5 / k`.

### 8.2 El esquema kick–drift–kick

En cada paso `dt`: `v ← v + ½ dt a(x)`, `x ← x + dt v`, `a ← a(x)` y `v ← v + ½ dt a`. Es de orden 2 y simpléctico. El laboratorio parte del perihelio y acumula el ángulo hasta `2π` interpolando linealmente en el último paso.

### 8.3 Convergencia

Con `dt = 0,2; 0,1; 0,05 d` los errores del periodo son `1.27e-03`, `3.18e-04` y `7.94e-05 d`. El cociente entre pasos sucesivos da órdenes `2.00` y `2.00`: el esquema converge como `dt²`, el orden teórico de un esquema de segundo orden. Se esperaba ese factor 4 por paso y el laboratorio lo confirma.

### 8.4 Resonancias

Si el asteroide da `p` vueltas mientras Júpiter da `q`, `P_ast/P_J = q/p` y por Kepler `a = a_J (q/p)^(2/3)`. Con `a_J = 5,2044 au` (aproximado, no consultado) se obtiene 3:1 en `2.502 au`, 5:2 en `2.825`, 7:3 en `2.958`, 2:1 en `3.279` y 3:2 en `3.972 au`. El laboratorio integra una órbita circular en cada semieje y mide el cociente de periodos.

### 8.5 Qué no es esta clase

Un cociente de periodos no es dinámica resonante: la resonancia real exige integrar con las perturbaciones de Júpiter y estudiar el ángulo resonante. El modelo de dos cuerpos solo ubica *dónde* mirar.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `GM` | parámetro gravitacional del Sol | au³/día² | `k²` |
| `a` | semieje mayor | au | 2,2 (sintético) |
| `e` | excentricidad | — | 0,3 |
| `P` | periodo | día | 1191.8798 |
| `dt` | paso de tiempo | día | 0,2 – 0,05 |
| `a_J` | semieje de Júpiter | au | 5,2044 (aprox.) |

## 10. Convenciones y referencias

Marco heliocéntrico inercial; coordenadas en el plano orbital; tiempo en días; sin época calendario. Orbitas sintéticas.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| — | Sin fuente externa | — | relaciones estándar que verifica el laboratorio | No se consultó una fuente para esta clase |

No consultado: la constante de Gauss, el semieje de Júpiter y la ubicación del hueco 3:1 proceden de la memoria del autor; el laboratorio verifica solo la coherencia interna (Kepler frente a integración).

Límites: ninguna fuente externa respalda esta clase.

## 12. Cómo ver la convergencia del periodo

| Magnitud | Valor |
|---|---|
| dt = 0,2 d | 1.27e-03 d |
| dt = 0,1 d | 3.18e-04 d |
| dt = 0,05 d | 7.94e-05 d |
| resonancia 3:1 | 2.502 au |

Descripción larga: el error del periodo cae de `1.3e-03` a `7.9e-05 d` al dividir el paso por cuatro.

## 13. Ejemplo trabajado: el periodo de a = 2,2 au

**Paso 1 · Tercera ley.** `P = 2π·2,2^1,5/k = 1191.8798 d`.

**Paso 2 · Integración.** Con `dt = 0,05 d` el laboratorio da `1191.879848 d`.

**Paso 3 · Error.** `7.94e-05 d`, por debajo de `10⁻⁴ d`.

**Paso 4 · Orden.** Entre `dt = 0,1` y `0,05` el orden es `2.00`.

## 14. Distintas formas de resolver lo mismo

**Analítica:** Kepler da el periodo exacto de dos cuerpos. **Numérica:** el integrador sirve cuando se añadan fuerzas. Las dos deben coincidir; si no, hay un error de código. Para resonancias, la vía analítica ubica y la numérica con perturbaciones decidiría.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `P` para `a = 1 au` con `k`. *Pasos:* `2π/k`.

<details><summary>Solución comentada</summary>

`365,2568983 d`.
</details>

**Ejercicio 2 · con una pista.** ¿Qué semieje corresponde a la resonancia 2:1 con Júpiter? *Pista:* `a_J (1/2)^(2/3)`.

<details><summary>Solución comentada</summary>

`3.279 au`.
</details>

**Ejercicio 3 · casi autónomo.** Compara el periodo de `a = 2,2 au` con el de `a = 5,2044 au`.

<details><summary>Solución comentada</summary>

`3.263` frente a `11.873` años; cociente `0.275`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Si el error con `dt = 0,1 d` es `E`, ¿qué se espera con `0,05 d` en un esquema de orden 2?

<details><summary>Solución comentada</summary>

`E/4`; el laboratorio confirma el factor 4 (8.3).
</details>

**Ejercicio 5 · autónomo.** ¿Por qué el leapfrog parte del perihelio en el laboratorio?

<details><summary>Solución comentada</summary>

Para tener una condición inicial analítica sencilla: velocidad perpendicular y `v = √(GM(1+e)/q)`.
</details>

**Ejercicio 6 · autónomo.** Calcula `Q` y `q` de la órbita sintética.

<details><summary>Solución comentada</summary>

`q = 1,54 au`, `Q = 2,86 au`.
</details>

**Ejercicio 7 · autónomo.** ¿Qué resonancia cae más cerca de `a = 2,82 au`?

<details><summary>Solución comentada</summary>

5:2 (`2.825 au`).
</details>

**Ejercicio 8 · autónomo.** ¿Cuántas vueltas da el asteroide en 3:1 mientras Júpiter da 1?

<details><summary>Solución comentada</summary>

Tres.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** ¿Por qué un cociente de periodos 3:1 no basta para afirmar que hay resonancia?

<details><summary>Solución comentada</summary>

Hay que comprobar que el ángulo resonante libra; con perturbaciones los periodos no son constantes.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** Si el paso fuera de 5 d en la órbita sintética, ¿qué esperas del perihelio?

<details><summary>Solución comentada</summary>

Pocos pasos por el tramo rápido; el error de fase crecería y el esquema perdería exactitud.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Qué se necesita para pasar de este modelo a uno para predecir un acercamiento?

<details><summary>Solución comentada</summary>

Perturbaciones de planetas, efectos no gravitacionales (C14) y una incertidumbre inicial (C08).
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de dinámica orbital*: periodo analítico, errores con tres pasos, orden de convergencia y tres resonancias.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4.
</details>

## 17. Laboratorio: integración de dos cuerpos y resonancias

El script [dinamica.py](dinamica.py) integra la órbita con kick–drift–kick, mide el periodo con tres pasos y las resonancias (**comprueba** error < 10⁻⁴ d, orden entre 1,9 y 2,1 y cocientes resonantes con 10⁻⁴).

**Datos:** órbita **sintética**; constante de Gauss y `a_J` no consultadas. **Predice antes de ejecutar:** ¿Cuánto mejora el error al dividir el paso por dos? **Ejecución del 2026-11-09:**

```text
Python 3.12.9 (biblioteca estandar)
Periodo analitico 2 pi a^1.5 / k = 1191.879769 d (3.2632 anios)
dt = 0.20 d : periodo integrado = 1191.881040 d ; error = 1.271e-03 d
dt = 0.10 d : periodo integrado = 1191.880087 d ; error = 3.177e-04 d
dt = 0.05 d : periodo integrado = 1191.879848 d ; error = 7.943e-05 d
Orden de convergencia observado: 2.00 ; 2.00
Periodo de Jupiter (a = 5.2044 au) = 11.873 anios
  res     a [au] P_ast/P_J medido        q/p
  3:1     2.5020         0.333334   0.333333
  5:2     2.8254         0.400000   0.400000
  7:3     2.9584         0.428572   0.428571
  2:1     3.2786         0.500000   0.500000
  3:2     3.9717         0.666667   0.666667
Pruebas superadas.
```

```bash
python programa/clases/B58/B58-C02-dinamica-de-asteroides/dinamica.py
```

**Límites:** solo dos cuerpos; no hay perturbaciones ni efectos relativistas; las resonancias son cocientes de periodo.

## 18. Errores frecuentes y cómo corregirlos

**Confundir paso de tiempo y precisión.** Se corrige con 8.3.

**Usar unidades mezcladas (años con días).** Se corrige con la sección 9.

**Creer que la resonancia se decide solo con periodos.** Se corrige con 8.5.

**Olvidar rotular la órbita como sintética.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué orden esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de dinámica orbital** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Conceptos de la clase | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con el análisis | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha | Declara lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular la órbita como sintética; no presentar una resonancia de periodos como dinámica resonante; declarar lo no consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y los datos, sintéticos; nada de lo calculado evalúa un objeto real ni sustituye a los sistemas oficiales de monitoreo y alerta.  Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

El integrador reproduce Kepler con error de `7.9e-05 d` y la resonancia 3:1 cae en `2.50 au`. Queda una pregunta: ¿de qué están hechos los asteroides?

**Glosario español–inglés.** problema de dos cuerpos · *two-body problem*; leapfrog · *leapfrog*; simpléctico · *symplectic*; resonancia de movimiento medio · *mean-motion resonance*; hueco de Kirkwood · *Kirkwood gap*.

**Continuidad.** [B58-C03](../B58-C03-composicion-de-asteroides/CLASE.md) estudia composición de asteroides.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B58-C01 — Clasificación de cuerpos menores](../B58-C01-clasificacion-de-cuerpos-menores/CLASE.md) · [📚 Bloque B58](../../../tronco-comun/B58-asteroides-cometas-y-defensa-planetaria.md) · [Siguiente: B58-C03 — Composición de asteroides →](../B58-C03-composicion-de-asteroides/CLASE.md)
<!-- /nav -->
