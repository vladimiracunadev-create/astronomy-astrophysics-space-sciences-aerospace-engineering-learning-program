# B73-C08 — Sistemas de N cuerpos

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B73](../../../tronco-comun/B73-mecanica-celeste-resonancias-y-caos.md) · [← Anterior: B73-C07 — Constante de Jacobi](../B73-C07-constante-de-jacobi/CLASE.md) · [Siguiente: B73-C09 — Integración de largo plazo →](../B73-C09-integracion-de-largo-plazo/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 8 del bloque B73, que abre el tramo de muchos cuerpos. Nivel N3. Sigue a [B73-C07](../B73-C07-constante-de-jacobi/CLASE.md): sin la restricción de masa despreciable ya no hay constante de Jacobi, y quedan solo la energía, el momento y el momento angular. Aquí integras por suma directa un sistema de cinco cuerpos (Júpiter y los cuatro satélites galileanos) con un leapfrog simpléctico y compruebas esas leyes de conservación, el orden del método y un caso de dos cuerpos con solución analítica. Los `GM` y los semiejes son publicados; las condiciones iniciales son **sintéticas**.

## 2. Por qué esta clase existe

El sistema solar y sus lunas son problemas de N cuerpos, y la calidad de una integración se juzga por lo que conserva. La decisión central: **¿cómo sé que mi suma directa y mi paso de tiempo describen el sistema y no mis errores numéricos?**

## 3. Lo que podrás hacer al terminar

1. Escribir la aceleración de cada cuerpo como suma sobre los demás.
2. Contar el coste de la suma directa, `N(N−1)/2` pares por paso.
3. Implementar un leapfrog kick-drift-kick de orden 2.
4. Medir el error relativo de energía y la conservación del momento angular.
5. Verificar el orden del método al reducir el paso a la mitad.
6. Contrastar con un caso de dos cuerpos de periodo analítico.

La evidencia es la **ficha de conservación de un sistema de cinco cuerpos** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué dice la tercera ley de Newton sobre un par de fuerzas?
2. ¿Qué es la energía de un sistema de partículas?
3. ¿Qué es el momento angular?
4. ¿Qué es un integrador simpléctico?
5. ¿Qué es el orden de un método?

<details>
<summary>Ver respuestas</summary>

1. Que son iguales y opuestas, de modo que conservan el momento total. 2. La suma de energías cinéticas más la energía potencial gravitatoria de todos los pares. 3. El producto vectorial `r × p`, conservado en un sistema aislado. 4. Uno que conserva exactamente la estructura de la dinámica hamiltoniana y mantiene acotado el error de energía. 5. El exponente `p` tal que el error global escala con `dt^p`.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Un sistema de Júpiter y los cuatro satélites galileanos (cinco masas, `10` pares) integrado `16,69 d` con un leapfrog de paso `200 s` (`7210` pasos) tiene un error relativo máximo de energía de `1,46e-08` y una variación del momento angular de `2,2e-16`. Al reducir el paso a la mitad el error baja un factor `3,61`. Es el **ejemplo conductor**. Las condiciones iniciales son **sintéticas** (órbitas circulares coplanares con fases 0°, 90°, 180° y 270°).

## 6. Vocabulario

La **suma directa** calcula la fuerza sobre cada cuerpo como suma de las de los demás: `a_i = Σ_{j≠i} GM_j (r_j − r_i)/|r_j − r_i|³`. El **leapfrog** (kick-drift-kick) hace medio paso de velocidad, un paso de posición y otro medio de velocidad: es de orden 2 y simpléctico. El **error relativo de energía** es `|E(t)/E₀ − 1|`. El **baricentro** es el centro de masa; el marco del baricentro tiene momento total nulo.

## 7. Modelo mental: una pista de baile donde todos tiran de todos

```mermaid
flowchart LR
    C["GM, posiciones, velocidades"] --> F["fuerzas: suma sobre N(N-1)/2 pares"]
    F --> K["kick: v += a dt/2"]
    K --> D["drift: r += v dt"]
    D --> F2["fuerzas nuevas"]
    F2 --> K2["kick: v += a dt/2"]
    K2 --> V["energia, L, momento"]
```

*Descripción textual:* en cada paso se calculan las fuerzas de todos los pares, se actualiza la velocidad medio paso, la posición un paso y la velocidad otro medio paso; luego se miden las cantidades conservadas.

Analogía: en una pista de baile cada persona es empujada por todas las demás; si cada empujón se aplica en dos mitades alrededor del paso, el baile conserva su «energía media» durante muchas vueltas aunque cada paso sea aproximado. Límite: con muchos bailarines el coste crece como el cuadrado de su número.

## 8. La explicación, paso a paso

### 8.1 La suma directa

Con `N = 5` cuerpos hay `N(N−1)/2 = 10` pares; cada par aporta una fuerza a dos cuerpos (por la tercera ley), por lo que el momento total se conserva por construcción. Con `N = 1000` serían `499 500` pares por paso: el coste crece como `N²`.

### 8.2 El leapfrog

Cada paso hace: `v ← v + (dt/2) a(r)`, `r ← r + dt v`, `a ← a(r)`, `v ← v + (dt/2) a`. Es reversible y simpléctico: el error de energía oscila sin crecer sistemáticamente.

### 8.3 Resultados

| `dt` (s) | pasos | error relativo máx. de energía | `|ΔL/L|` |
|---|---|---|---|
| 400 | 3605 | 5,28e-08 | — |
| 200 | 7210 | 1,46e-08 | 2,2e-16 |

El cociente es `3,61`, cercano al 4 de un método de orden 2. El momento total relativo es `2,7e-15`: cero a precisión de máquina.

### 8.4 Segunda vía: dos cuerpos

Para Júpiter–Io en órbita circular de `421 800 km`, el periodo kepleriano es `1,76990 d`; la ficha NASA/NSSDC da `1,769138 d` (`0,04%` menos) y la tabla de elementos del JPL, `1,762732 d` (`0,41%` menos). Esas diferencias no son un error del integrador: el modelo no tiene achatamiento de Júpiter ni interacciones entre satélites y la tabla del JPL es un valor de época; no se verificó aquí la causa. Integrada con leapfrog durante un periodo kepleriano, la separación vuelve al valor inicial con un error relativo de `8,8e-06`.

### 8.5 Qué no es este modelo

Las condiciones iniciales son sintéticas: no representan el estado real de las lunas en ninguna fecha. El modelo no tiene `J2`, mareas ni el Sol, y el paso fijo de `200 s` es adecuado para estas órbitas pero no para un encuentro cercano (se trata en [B73-C21](../B73-C21-pasos-cercanos-a-satelites-naturales-en-integracion-de-n-cuerpos/CLASE.md)).

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `GM_i` | parámetro gravitacional del cuerpo `i` | km³/s² | 126,687×10⁶ (Júpiter); 3202–9888 (lunas) |
| `a_i` | aceleración | km/s² | suma sobre pares |
| `dt` | paso de tiempo | s | 200 y 400 |
| `E` | energía (con `GM` en lugar de masas) | km⁵/s⁴ | relativa |
| `L` | momento angular | km²/s × GM | relativo |

## 10. Convenciones y referencias

Marco del baricentro, plano `xy`, sentido antihorario; las masas se representan por su `GM` (el factor `G` se cancela en la dinámica y en los errores relativos). Leapfrog kick-drift-kick de paso fijo. Las órbitas iniciales son circulares con la velocidad `√((GM_J+GM_i)/a_i)`.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA JPL SSD, Planetary Satellite Physical Parameters — https://ssd.jpl.nasa.gov/sats/phys_par/ (consultada 2026-11-10) | tabla de GM y radio medio; GM de la Luna (DE440), los galileanos (JUP365), Titán, Encélado y Mimas (SAT441) | GM de Io, Europa, Ganymede y Callisto (JUP365) | Consultada |
| S2 | NASA JPL SSD, Planetary Satellite Mean Elements — https://ssd.jpl.nasa.gov/sats/elem/ (consultada 2026-11-10) | tabla de elementos medios, época 2000-01-01.5 TDB; planos de Laplace (galileanos con JUP365, saturnianos con SAT441), eclíptica para la Luna (DE405) | semiejes medios y periodos de los galileanos (J2000, plano de Laplace) | Consultada |
| S5 | NASA/NSSDC, Jovian Satellite Fact Sheet — https://nssdc.gsfc.nasa.gov/planetary/factsheet/joviansatfact.html (consultada 2026-11-10) | ficha leída; actualizada el 2023-12-06 | periodo sidéreo de Io, 1,769138 d | Consultada |
| S3 | NASA/NSSDC, Jupiter Fact Sheet — https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html (consultada 2026-11-10) | ficha leída; actualizada el 2024-10-02 | GM de Júpiter = 126,687×10⁶ km³/s² | Consultada |
| — | Suma directa y leapfrog kick-drift-kick (métodos estándar de la dinámica N-cuerpos) | — | las verifica el laboratorio con una segunda vía | No consultada en una fuente concreta |

Límites: las condiciones iniciales son sintéticas; el modelo no incluye `J2`, mareas ni el Sol; no se consultó una referencia sobre integradores simplécticos.

## 12. Cómo ver que la integración conserva lo que debe

| Magnitud | Valor |
|---|---|
| error de energía (`dt` = 200 s) | 1,46e-08 |
| cociente al bajar `dt` a la mitad | 3,61 |
| `|ΔL/L|` | 2,2e-16 |
| momento total relativo | 2,7e-15 |
| cierre de dos cuerpos | 8,8e-06 |

Descripción larga: las leyes de conservación se cumplen a precisión de máquina (momento y momento angular) o con un error pequeño y de orden 2 (energía).

## 13. Ejemplo trabajado: cuántos pares hay en el sistema

**Paso 1 · Cuerpos.** Júpiter, Io, Europa, Ganymede y Callisto: `N = 5`.

**Paso 2 · Pares.** `5 × 4 / 2 = 10`.

**Paso 3 · Pasos.** `T = 16,69 d` con `dt = 200 s` son `7210` pasos.

**Paso 4 · Evaluaciones.** `10 × 7210` interacciones, unas `72 000`.

## 14. Distintas formas de describir un sistema de N cuerpos

**Por fuerzas:** la suma directa. **Por conservación:** `E`, `L`, momento. **Por orden:** error frente a `dt`. **Por coste:** `N(N−1)/2` pares por paso.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Cuenta los pares de un sistema de 5 cuerpos. *Pasos:* `N(N−1)/2`.

<details><summary>Solución comentada</summary>

`10`.
</details>

**Ejercicio 2 · con una pista.** ¿Cuántos pares tiene un sistema de 1000 cuerpos? *Pista:* mismo cociente.

<details><summary>Solución comentada</summary>

`1000 × 999 / 2 = 499 500`.
</details>

**Ejercicio 3 · casi autónomo.** ¿Por qué el momento total se conserva por construcción?

<details><summary>Solución comentada</summary>

Porque cada par aporta fuerzas iguales y opuestas (tercera ley) y la suma sobre pares las cancela.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** ¿Cuántos pasos hay en una órbita de Io (`152 300 s`) con `dt = 200 s`?

<details><summary>Solución comentada</summary>

`152 300/200 ≈ 762` pasos.
</details>

**Ejercicio 5 · autónomo.** Cociente entre errores al bajar `dt` de 400 a 200 s.

<details><summary>Solución comentada</summary>

`3,61`.
</details>

**Ejercicio 6 · autónomo.** Error de energía esperable si el método fuera de orden 4 al bajar el paso a la mitad.

<details><summary>Solución comentada</summary>

Un factor `2⁴ = 16`.
</details>

**Ejercicio 7 · autónomo.** Diferencia entre el periodo kepleriano de Io y la ficha NASA.

<details><summary>Solución comentada</summary>

`0,04%`.
</details>

**Ejercicio 8 · autónomo.** ¿Qué mide `|P|/Σ|p|`?

<details><summary>Solución comentada</summary>

Cuánto momento neto queda comparado con la suma de los momentos individuales; vale `2,7e-15`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un colega usa las posiciones iniciales del laboratorio como si fueran las de los satélites hoy. ¿Qué le dices?

<details><summary>Solución comentada</summary>

Que son sintéticas: órbitas circulares coplanares con fases arbitrarias; para posiciones reales hay que usar efemérides (JPL Horizons o SPICE).
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** Un colega dice que el leapfrog «conserva exactamente» la energía. ¿Es cierto?

<details><summary>Solución comentada</summary>

No: el error es pequeño y acotado, no nulo (`1,5e-08` aquí); lo que se conserva exactamente es una energía modificada vecina.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Qué pasa con el coste si se pasa de 5 a 10 000 cuerpos con suma directa?

<details><summary>Solución comentada</summary>

Pasa de 10 a `≈ 5×10⁷` pares por paso: hay que usar otros métodos (árboles, multipolos), que esta clase no cubre.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de conservación de un sistema de cinco cuerpos*: tabla de errores para dos pasos, cociente de orden, momento angular, momento total, caso de dos cuerpos y lista de límites.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.5 y la salida del laboratorio.
</details>

## 17. Laboratorio: Júpiter y los galileanos por suma directa

El script [n_cuerpos.py](n_cuerpos.py) integra un sistema de cinco cuerpos con leapfrog en dos pasos y un caso de dos cuerpos (**comprueba** error de energía < `10⁻⁶`, cociente 3–5, `ΔL/L` < `10⁻¹⁰` y cierre del caso de dos cuerpos < `10⁻⁵`).

**Datos:** `GM`, semiejes y periodos de la NASA/JPL (consultados); condiciones iniciales **sintéticas**. **Predice antes de ejecutar:** ¿cuánto bajará el error de energía al reducir el paso a la mitad? (`≈ 4` veces.) **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Cuerpos: Jupiter, Io, Europa, Ganymede, Callisto ; pares por evaluacion de la fuerza = N(N-1)/2 = 10
dt =   400 s, T = 16.69 d (3605 pasos): error relativo maximo de energia = 5.28e-08 ; |dL/L| = 1.44e-15 ; |P|/sum|p| = 3.0e-15
dt =   200 s, T = 16.69 d (7210 pasos): error relativo maximo de energia = 1.46e-08 ; |dL/L| = 2.22e-16 ; |P|/sum|p| = 2.7e-15
Cociente de errores de energia al reducir el paso a la mitad = 3.61 (orden 2 -> 4)
Jupiter-Io: periodo kepleriano de una orbita circular de a = 421 800 km = 1.76990 d ; ficha NASA/NSSDC = 1.769138 d (dif. 0.04%) ; tabla JPL = 1.762732 d (dif. 0.41%)
Dos cuerpos: tras un periodo kepleriano la separacion vuelve al inicio con error relativo = 8.84e-06 (3058 pasos)
Pruebas superadas.
```

```bash
python programa/clases/B73/B73-C08-sistemas-de-n-cuerpos/n_cuerpos.py
```

**Límites:** solo gravedad newtoniana entre masas puntuales, coplanar, sin `J2`, mareas ni Sol; paso fijo.

## 18. Errores frecuentes y cómo corregirlos

**Confundir `GM` con masa en la energía.** Se corrige con la sección 10: los errores relativos no dependen de `G`.

**Creer que error pequeño de energía prueba que la órbita es correcta.** Se corrige con 8.4: hace falta la segunda vía.

**Usar posiciones sintéticas como reales.** Se corrige con la sección 21.

**Ignorar el coste `N²`.** Se corrige con 8.1.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿cuánto bajó el error al reducir el paso y qué esperabas? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de conservación de un sistema de cinco cuerpos** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Implementa la suma directa y mide conservación | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas con unidades | Calcula casos nuevos |
| Comprobación | Sin comprobar | Un caso | Contraste con una segunda vía | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo sintético y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular las condiciones iniciales como sintéticas; no presentar el estado como el real del sistema joviano; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y sus datos son publicados con fuente o sintéticos rotulados; ningún resultado describe una trayectoria real ni sirve para planificar una misión.  Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

La suma directa de cinco cuerpos con leapfrog conserva el momento angular a `2e-16` y la energía a `1,5e-08`, con el orden 2 esperado (cociente `3,61`). Queda una pregunta: ¿qué pasa con ese error cuando se integran millones de órbitas?

**Glosario español–inglés.** problema de N cuerpos · *N-body problem*; suma directa · *direct summation*; leapfrog · *leapfrog*; integrador simpléctico · *symplectic integrator*; baricentro · *barycenter*.

**Continuidad.** [B73-CC09](../B73-C09-integracion-de-largo-plazo/CLASE.md) estudia la integración de largo plazo.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B73-C07 — Constante de Jacobi](../B73-C07-constante-de-jacobi/CLASE.md) · [📚 Bloque B73](../../../tronco-comun/B73-mecanica-celeste-resonancias-y-caos.md) · [Siguiente: B73-C09 — Integración de largo plazo →](../B73-C09-integracion-de-largo-plazo/CLASE.md)
<!-- /nav -->
