# B76-C07 — Maniobras de inserción cislunar

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B76](../../../tronco-comun/B76-dinamica-cislunar-y-operaciones-de-proximidad.md) · [← Anterior: B76-C06 — Órbitas DRO — Dinámica cislunar y operaciones de proximidad](../B76-C06-orbitas-dro-dinamica-cislunar-y-operaciones-de-proximidad/CLASE.md) · [Siguiente: B76-C08 — Transferencias de baja energía →](../B76-C08-transferencias-de-baja-energia/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 7 del bloque B76, nivel N3. Llegar a una órbita lunar exige dos maniobras grandes: la inyección translunar que saca la nave de la órbita baja terrestre y la inserción lunar que la captura. Aquí las calculas con cónicas empalmadas y las pones en un presupuesto de propergol. Usa [B76-C01](../B76-C01-sistema-tierra-luna/CLASE.md) para las constantes. Es un cálculo coplanar sin inclinación ni Sol.

## 2. Por qué esta clase existe

Un diseño preliminar de misión empieza por el presupuesto de velocidad. La decisión central: **¿cuánto `Δv` cuestan la salida de la Tierra y la captura en la Luna, y cuánto cambia la segunda según la órbita lunar elegida?**

## 3. Lo que podrás hacer al terminar

1. Calcular el `Δv` de inyección translunar con una elipse de Hohmann hasta la distancia lunar.
2. Obtener la velocidad de llegada relativa a la Luna `v_inf` y la excentricidad hiperbólica.
3. Calcular el `Δv` de inserción lunar en función de la altitud de la órbita final.
4. Convertir el `Δv` en fracción de propergol con la ecuación de Tsiolkovsky.
5. Verificar el empalme con la conservación de energía en la hipérbola.
6. Rotular el motor y las altitudes como ilustrativos.

La evidencia es la **presupuesto de `Δv` de una inserción** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es una transferencia de Hohmann?
2. ¿Qué es `v_inf`?
3. ¿Qué es la ecuación vis-viva?
4. ¿Qué es la ecuación de Tsiolkovsky?
5. ¿Qué es una cónica empalmada?

<details>
<summary>Ver respuestas</summary>

1. La elipse tangente a dos órbitas circulares coplanares. 2. La velocidad relativa lejos del cuerpo, en una trayectoria hiperbólica. 3. `v² = GM (2/r − 1/a)`. 4. `Δv = Isp g0 ln(m0/mf)`. 5. Un modelo que une trayectorias de dos cuerpos en la frontera de cada esfera de influencia.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Desde una órbita circular de `200 km` el `Δv` de inyección es `3,1313 km/s` y el vuelo dura `4,978 d`. La nave llega a la Luna con `v_inf = 0,8378 km/s`; capturarla en una órbita circular de `100 km` cuesta `0,8238 km/s`. El total es `3,9552 km/s`, que con un motor ilustrativo de `320 s` es `71,6 %` de la masa inicial. Es el **ejemplo conductor**.

## 6. Vocabulario

La **inyección translunar (TLI)** es el impulso en el perigeo. La **inserción en órbita lunar (LOI)** es el impulso en el perilune de la hipérbola. `v_inf = v_Luna − v_apogeo` es la **velocidad de llegada**. La **excentricidad hiperbólica** es `e = 1 + r v_inf²/GM_L`. La **fracción de propergol** es `1 − exp(−Δv/(Isp g0))`.

## 7. Modelo mental: lanzar una pelota para que alcance a una cinta transportadora

```mermaid
flowchart LR
    L["orbita baja terrestre"] --> T["TLI: dv1"]
    T --> E["elipse a distancia lunar"]
    E --> V["v_inf en la Luna"]
    V --> H["hiperbola"]
    H --> O["LOI: dv2"]
    O --> P["presupuesto y propergol"]
```

*Descripción textual:* el impulso en el perigeo lleva la nave por una elipse hasta la distancia lunar, la velocidad relativa a la Luna define la hipérbola y el impulso en el perilune la captura; la suma da el presupuesto.

Analogía: lanzar una pelota a una cinta transportadora que se mueve; llega con la diferencia de velocidades y hay que frenarla. Límite: la Tierra y la Luna no son puntos aislados; el empalme es una aproximación y la inyección real busca ventanas y trayectorias de retorno libre.

## 8. La explicación, paso a paso

### 8.1 Inyección translunar

En `r1 = 6578,137 km`: `v_circ = 7,7843 km/s`; en el perigeo de la elipse hasta `a = 384.400 km`, `v_p = 10,9156 km/s`; `Δv_TLI = 3,1313 km/s`. El semieje es `195.489 km` y el vuelo `π √(a³/GM_T) = 4,978 d`.

### 8.2 Llegada

En el apogeo la velocidad es `v_a = 0,1868 km/s`; la Luna se mueve a `n a = 1,0245 km/s`, así que `v_inf = 0,8378 km/s`.

### 8.3 Inserción

Con `r = 1837,4 km` (altitud `100 km`): `v_hip = √(v_inf² + 2 GM_L/r) = 2,4573 km/s`; `v_circ,L = 1,6335 km/s`; `Δv_LOI = 0,8238 km/s`; `e = 1,2630`. La energía de la hipérbola, `v_inf²/2`, coincide con la del perilune a `1,6 × 10⁻¹⁶`.

### 8.4 Sensibilidad a la órbita final

| Altitud lunar (km) | `Δv_LOI` (km/s) |
|---|---|
| 50 | 0,8313 |
| 100 | 0,8238 |
| 500 | 0,7746 |
| 2000 | 0,6782 |

Una órbita más alta cuesta menos, pero también deja a la nave más lejos de la superficie.

### 8.5 Propergol

`Δv_total = 3,9552 km/s` y `Isp = 320 s` (ilustrativo): `1 − exp(−3955,2/(320 × 9,80665)) = 0,7164`. Es una cota con impulsos instantáneos y sin pérdidas.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `Δv_TLI` | inyección translunar | km/s | 3,1313 |
| `t` | tiempo de vuelo | d | 4,978 |
| `v_inf` | velocidad de llegada | km/s | 0,8378 |
| `Δv_LOI` | inserción a 100 km | km/s | 0,8238 |
| `e` | excentricidad hiperbólica | — | 1,2630 |
| fracción | propergol (Isp 320 s, ilustrativo) | — | 0,7164 |

## 10. Convenciones y referencias

`GM_T`, `GM_L` (JPL, DE440), radio ecuatorial terrestre (NASA/NSSDC), `a` (NASA/NSSDC). Impulsos instantáneos, coplanar, Tierra puntual y Luna en círculo; `g0 = 9,80665 m/s²` (valor convencional no consultado); `Isp = 320 s` y altitudes ilustrativas.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA JPL SSD, Astrodynamic Parameters — https://ssd.jpl.nasa.gov/astro_par.html (consultada 2026-11-10) | tabla de GM y constantes | GM de la Tierra = 398600,435507 km³/s²; GM de la Luna = 4902,800118 km³/s² (DE440, Park et al. 2021); UA = 149597870700 m | Consultada |
| S2 | NASA/NSSDC, Moon Fact Sheet — https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html (consultada 2026-11-10) | ficha completa leída | semieje mayor 0,3844×10⁶ km; periodo sideral 27,3217 d; periodo sinódico 29,53 d; excentricidad 0,0549; radio medio 1737,4 km; gravedad superficial 1,62 m/s² | Consultada |
| S3 | NASA/NSSDC, Earth Fact Sheet — https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html (consultada 2026-11-10) | ficha leída | masa 5,9722×10²⁴ kg; radio medio volumétrico 6371,000 km; radio ecuatorial 6378,137 km | Consultada |
| — | Relaciones estándar: Hohmann, vis-viva, cónicas empalmadas, Tsiolkovsky | — | las verifica el laboratorio (energía de la hipérbola) | No consultada en una fuente concreta |

Límites: no se consultó ningún presupuesto real de misión ni el valor de `g0`; la Luna se trata en círculo y sin inclinación; el resultado es una cota inferior de diseño.

## 12. Cómo ver el presupuesto

| Magnitud | Valor |
|---|---|
| `Δv_TLI` | 3,1313 km/s |
| `Δv_LOI` a 100 km | 0,8238 km/s |
| Total | 3,9552 km/s |
| Fracción de propergol | 0,7164 |

Descripción larga: la salida de la Tierra pesa cuatro veces más que la captura en la Luna.

## 13. Ejemplo trabajado: la inserción lunar

**Paso 1 · Llegada.** `v_inf = 1,0245 − 0,1868 = 0,8378 km/s`.

**Paso 2 · Perilune.** `v_hip = √(0,7019 + 2 × 4902,8/1837,4) = 2,4573 km/s`.

**Paso 3 · Circular.** `v_c = √(4902,8/1837,4) = 1,6335 km/s`.

**Paso 4 · Impulso.** `Δv_LOI = 2,4573 − 1,6335 = 0,8238 km/s`.

## 14. Distintas formas de expresar el costo

**En velocidad:** `Δv`. **En energía:** `v_inf²/2`. **En masa:** fracción de propergol. **En tiempo:** días de vuelo. **Por órbita final:** `Δv_LOI(h)`.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `Δv_TLI`. *Pasos:* `v_p − v_circ` con los valores de 8.1.

<details><summary>Solución comentada</summary>

`10,9156 − 7,7843 = 3,1313 km/s`.
</details>

**Ejercicio 2 · con una pista.** Calcula el tiempo de vuelo. *Pista:* semiperiodo de la elipse.

<details><summary>Solución comentada</summary>

`a = 195.489 km`; `π √(a³/GM_T) = 430.100 s = 4,978 d`.
</details>

**Ejercicio 3 · casi autónomo.** Calcula `e` de la hipérbola de llegada.

<details><summary>Solución comentada</summary>

`1 + 1837,4 × 0,7019/4902,8 = 1,2630`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Calcula la fracción de propergol solo de la LOI.

<details><summary>Solución comentada</summary>

`1 − exp(−823,8/3138,1) = 0,2308`.
</details>

**Ejercicio 5 · autónomo.** Calcula la fracción de propergol solo de la TLI.

<details><summary>Solución comentada</summary>

`1 − exp(−3131,3/3138,1) = 0,6314`; no es aditiva con la LOI.
</details>

**Ejercicio 6 · autónomo.** Si `v_inf` sube a `0,9 km/s`, ¿cuánto cambia `Δv_LOI`?

<details><summary>Solución comentada</summary>

`v_hip = √(0,81 + 5,3367) = 2,4793`; `Δv = 0,8458`: `+0,022 km/s`.
</details>

**Ejercicio 7 · autónomo.** ¿Cuánto ahorra una órbita final de `2000 km` frente a una de `100 km`?

<details><summary>Solución comentada</summary>

`0,8238 − 0,6782 = 0,1456 km/s`.
</details>

**Ejercicio 8 · autónomo.** Calcula la velocidad de escape lunar a `r = 1837,4 km`.

<details><summary>Solución comentada</summary>

`√2 × 1,6335 = 2,3101 km/s`; `v_hip = 2,4573` la supera, como corresponde a una hipérbola.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un colega propone usar `Isp = 450 s` sin más. ¿Qué cambia y qué objetas?

<details><summary>Solución comentada</summary>

La fracción baja a `1 − exp(−3955,2/4413) = 0,592`, pero el `Isp` es una hipótesis del motor que debe citarse.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** Un informe da `Δv = 3,95 km/s` como «el costo de ir a la Luna». ¿Qué falta?

<details><summary>Solución comentada</summary>

Precisar órbita inicial, final, modelo (Hohmann coplanar, impulsos instantáneos) y que excluye correcciones, pérdidas y ventana.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** Se propone entrar directamente en una NRHO sin frenar. ¿Qué parte del cálculo cambia?

<details><summary>Solución comentada</summary>

La LOI se sustituye por una inserción en la NRHO; `Δv` y excentricidad deben recalcularse (no se consultó ese presupuesto).
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *presupuesto de `Δv` de una inserción*: TLI, tiempo, `v_inf`, LOI, total y fracción de propergol, con fuentes.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.5 y la salida del laboratorio.
</details>

## 17. Laboratorio: inyección translunar e inserción lunar

El script [insercion.py](insercion.py) calcula la TLI, la llegada, la LOI para cuatro altitudes y la fracción de propergol Usa la biblioteca común [cislunar_lib.py](../cislunar_lib.py) del bloque (**comprueba** energía de la hipérbola < 1e-9, TLI entre 3,0 y 3,3 km/s y vuelo entre 4,5 y 5,5 d).

**Datos:** `GM_T`, `GM_L`, radios y `a` **consultados** el 2026-11-10; altitudes, `Isp` y `g0` son **ilustrativos** o convencionales. **Predice antes de ejecutar:** ¿cuál es mayor, la TLI o la LOI? (la TLI, `3,13` frente a `0,82 km/s`.) **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
TLI desde 200 km: v_circ = 7.7843 km/s ; v_perigeo = 10.9156 km/s ; dv_TLI = 3.1313 km/s
Tiempo de vuelo (semi-elipse) = 4.978 d ; v_apogeo = 0.1868 km/s ; v_Luna = 1.0245 km/s
Llegada: v_inf = 0.8378 km/s ; excentricidad hiperbolica = 1.2630
LOI a 100 km: v_perilune = 2.4573 km/s ; v_circ lunar = 1.6335 km/s ; dv_LOI = 0.8238 km/s
Delta-v total = 3.9552 km/s ; fraccion de propergol (Isp 320 s ILUSTRATIVO) = 0.7164
Error de energia hiperbolica = 1.58e-16
  LOI a h =     50 km : dv = 0.8313 km/s
  LOI a h =    100 km : dv = 0.8238 km/s
  LOI a h =    500 km : dv = 0.7746 km/s
  LOI a h =   2000 km : dv = 0.6782 km/s
Pruebas superadas.
```

```bash
python programa/clases/B76/B76-C07-maniobras-de-insercion-cislunar/insercion.py
```

**Límites:** Coplanar, impulsos instantáneos, Luna en círculo, sin Sol ni ventanas.

## 18. Errores frecuentes y cómo corregirlos

**Sumar fracciones de propergol.** No son aditivas. Se corrige con los ejercicios 4 y 5.

**Usar la velocidad de la Luna como `v_inf`.** Hay que restar la del apogeo. Se corrige con 8.2.

**Olvidar el radio lunar en `r`.** Se corrige con 8.3.

**Presentar el total como presupuesto de misión.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué `Δv_LOI` esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba la energía? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **presupuesto de `Δv` de una inserción** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Distingue TLI, `v_inf` y LOI | Explica la sensibilidad a la órbita final |
| Cálculo | Sin unidades | Con errores | Tablas completas con unidades | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Energía de la hipérbola comprobada | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara `Isp` y `g0` |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular `Isp` y altitudes como ilustrativos; no presentar el total como presupuesto de misión; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y sus datos son sintéticos, ilustrativos o publicados con fuente; ningún resultado es una efeméride, una telemetría ni una recomendación operativa, y lo simulado nunca se presenta como observado.  Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

La TLI cuesta `3,13 km/s` y la LOI a `100 km`, `0,82 km/s`; el total pide `71,6 %` de propergol con un motor de `320 s`. Queda una pregunta: ¿se puede llegar gastando menos energía?

**Glosario español–inglés.** inyección translunar · *trans-lunar injection (TLI)*; inserción en órbita lunar · *lunar orbit insertion (LOI)*; velocidad hiperbólica de exceso · *hyperbolic excess speed*; cónicas empalmadas · *patched conics*; propergol · *propellant*.

**Continuidad.** [B76-C08](../B76-C08-transferencias-de-baja-energia/CLASE.md) estudia las transferencias de baja energía.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B76-C06 — Órbitas DRO — Dinámica cislunar y operaciones de proximidad](../B76-C06-orbitas-dro-dinamica-cislunar-y-operaciones-de-proximidad/CLASE.md) · [📚 Bloque B76](../../../tronco-comun/B76-dinamica-cislunar-y-operaciones-de-proximidad.md) · [Siguiente: B76-C08 — Transferencias de baja energía →](../B76-C08-transferencias-de-baja-energia/CLASE.md)
<!-- /nav -->
