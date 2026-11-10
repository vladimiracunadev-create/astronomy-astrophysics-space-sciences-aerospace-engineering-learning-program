# B58-C14 — Efectos Yarkovsky y YORP

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B58](../../../tronco-comun/B58-asteroides-cometas-y-defensa-planetaria.md) · [← Anterior: B58-C13 — Caracterización de rotación](../B58-C13-caracterizacion-de-rotacion/CLASE.md) · [Siguiente: B58-C15 — Modelos de impacto planetario →](../B58-C15-modelos-de-impacto-planetario/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 14 del bloque B58 (nivel N3). Un asteroide no solo sigue la gravedad: la luz solar calentada y reemitida lo empuja y hace girar. Aquí verificas la relación de Gauss entre una aceleración tangencial y la deriva del semieje con una integración numérica, estimas el efecto para tres tamaños **sintéticos** y calculas la barrera de rotación de un cúmulo de escombros.

## 2. Por qué esta clase existe

Una deriva de decenas de kilómetros en un siglo puede decidir si un acercamiento ocurre. La decisión central: **¿cuánto se desplaza un asteroide por empuje térmico y por qué los cuerpos pequeños son más sensibles?**

## 3. Lo que podrás hacer al terminar

1. Aplicar la ecuación de Gauss a una aceleración tangencial.
2. Calcular el desplazamiento a lo largo de la órbita por la deriva del semieje.
3. Verificarlo con una integración numérica.
4. Estimar la aceleración térmica según el radio.
5. Calcular la barrera de rotación.
6. Declarar el modelo simple y los datos ilustrativos.

La evidencia es la **ficha de Yarkovsky y YORP** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es una aceleración tangencial?
2. ¿Cómo cambia el periodo con el semieje?
3. ¿Qué es el movimiento medio?
4. ¿Qué es la presión de radiación?
5. ¿Qué es un cúmulo de escombros?

<details>
<summary>Ver respuestas</summary>

1. La componente a lo largo de la velocidad. 2. `P ∝ a^1,5`. 3. `n = 2π/P`. 4. Empuje de los fotones (C04). 5. Un cuerpo de fragmentos unidos por gravedad (C03).
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

El ejemplo conductor es un asteroide sintético circular a 1,3 au con una aceleración tangencial de prueba de `3×10⁻¹⁰ au/día²` (exagerada para que se vea en 50 años). La integración da `Δa = 9.447e-04 au` frente a `9.442e-04` de Gauss (diferencia `0.05 %`) y un retraso angular de `-1.155e-01` frente a `-1.154e-01 rad` de la fórmula (`0.05 %`).

## 6. Vocabulario

El **efecto Yarkovsky** es el empuje por la reemisión térmica anisótropa de un cuerpo que rota. **YORP** es el torque análogo que cambia la rotación. La **ecuación de Gauss** da la variación de los elementos por una fuerza perturbadora; para una órbita circular, `da/dt = 2 a_T / n`. La **barrera de rotación** es el periodo mínimo sin cohesión.

## 7. Modelo mental: empujar un columpio siempre en la misma fase

```mermaid
flowchart LR
    L["luz solar"] --> T["calentamiento y reemisión"]
    T --> F["fuerza tangencial a_T"]
    F --> G["da/dt = 2 a_T / n"]
    G --> S["deriva del semieje"]
    S --> N["cambio del movimiento medio"]
    N --> X["desplazamiento a lo largo de la órbita"]
```

*Descripción textual:* la reemisión térmica produce una fuerza tangencial que, vía Gauss, cambia el semieje y por tanto el movimiento medio, acumulando un desplazamiento cuadrático en el tiempo.

Analogía: Como empujar un columpio en el momento justo: pequeñas dosis acumulan un cambio grande. Límite: el modelo supone órbita circular y aceleración constante; la teoría real depende de la inclinación del eje, la conductividad térmica y el periodo.

## 8. La explicación, paso a paso

### 8.1 Gauss para una órbita circular

Con `a_T` tangencial constante, `da/dt = 2 a_T/n`, con `n = 0.01161 rad/día` para `a = 1,3 au`. En 50 años: `Δa = 9.442e-04 au`.

### 8.2 Desplazamiento a lo largo de la órbita

Como `n ∝ a^(−3/2)`, `Δn = −(3/2)(n/a)Δa` y el ángulo acumulado se retrasa `Δθ = −(3/4)(n/a)(da/dt) t²`. La integración leapfrog da `-1.155e-01 rad` frente a `-1.154e-01` (`0.05 %`). El efecto crece con `t²`.

### 8.3 Estimación física

Con un modelo simple del autor `a_T = η (S/c)·3/(4 R ρ)`, `η = 0,03`, `ρ = 2000 kg/m³`: `R = 50 m → a_T = 6.0e-13 m/s², da/dt = 1.9e-03 au/Myr, desplazamiento en 100 años 9030 km`; `R = 100 m → a_T = 3.0e-13 m/s², da/dt = 9.5e-04 au/Myr, desplazamiento en 100 años 4515 km`; `R = 500 m → a_T = 6.0e-14 m/s², da/dt = 1.9e-04 au/Myr, desplazamiento en 100 años 903 km`. La aceleración crece al disminuir el radio. Todos los parámetros son ilustrativos.

### 8.4 YORP y la barrera de rotación

La barrera se obtiene igualando la aceleración centrífuga ecuatorial y la gravedad: `ω² = 4πGρ/3`, es decir `P_min = √(3π/(Gρ))`: `ρ = 1000 → 3.30 h`; `ρ = 2000 → 2.33 h`; `ρ = 3000 → 1.91 h`. Con un torque ilustrativo de `10⁻³ rad/año²` un cuerpo de 4 h duplicaría su velocidad angular en `13.8` Manios.

### 8.5 Qué falta

La amplitud real depende de la oblicuidad, la conductividad y el periodo; aquí se usa una eficiencia fija y se compara solo la mecánica de Gauss. Los valores publicados de deriva no se consultaron.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `a` | semieje mayor | au | 1,3 |
| `n` | movimiento medio | rad/día | 0.01161 |
| `a_T` | aceleración tangencial | au/día²; m/s² | 3×10⁻¹⁰ (prueba) |
| `da/dt` | deriva del semieje | au/Myr | 9.5e-04 (R = 100 m) |
| `η` | eficiencia térmica | — | 0,03 (ilustrativa) |
| `P_min` | barrera de rotación | h | 2.33 (ρ = 2000) |

## 10. Convenciones y referencias

Órbita circular; aceleración constante en la dirección de la velocidad; constantes recordadas, no consultadas; datos ilustrativos.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| — | Sin fuente externa | — | relaciones estándar que verifica el laboratorio | No se consultó una fuente para esta clase |

No consultado: la teoría de Yarkovsky y YORP de la literatura ni mediciones de derivas; la aceleración física es un modelo simple propio. Las constantes (k de Gauss, G, c, L☉) son recordadas.

Límites: sin fuente externa; la tabla física no estima ningún objeto real.

## 12. Cómo ver la deriva

| Magnitud | Valor |
|---|---|
| Δa integrado | 9.447e-04 au |
| Δa Gauss | 9.442e-04 au |
| Δθ integrado | -1.155e-01 rad |
| P_min (2000 kg/m³) | 2.33 h |

Descripción larga: la integración y las fórmulas coinciden a 0.1 % (semieje) y 0.1 % (ángulo).

## 13. Ejemplo trabajado: el retraso angular

**Paso 1 · Deriva.** `da/dt = 2a_T/n = 5.170e-08 au/día`.

**Paso 2 · Δa en 50 años.** `9.442e-04 au`.

**Paso 3 · Δθ.** `−(3/4)(n/a)(da/dt)t² = -1.154e-01 rad`.

**Paso 4 · Integración.** `-1.155e-01 rad`.

**Paso 5 · Lectura.** El desplazamiento a lo largo de la órbita crece como `t²`.

## 14. Distintas formas de resolver lo mismo

**Fórmula de Gauss:** análisis rápido. **Integración numérica:** valida y admite otras formas de fuerza. La primera justifica la segunda en el límite de fuerza pequeña.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `n` para `a = 1,3 au`. *Pasos:* `k/a^1,5`.

<details><summary>Solución comentada</summary>

`0.01161 rad/día`.
</details>

**Ejercicio 2 · con una pista.** Calcula `da/dt` con `a_T = 3×10⁻¹⁰`.

<details><summary>Solución comentada</summary>

`5.17e-08 au/día`.
</details>

**Ejercicio 3 · casi autónomo.** ¿Cómo escala `Δθ` con el tiempo?

<details><summary>Solución comentada</summary>

Como `t²`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** ¿Qué pasa con `a_T` si el radio se duplica en el modelo simple?

<details><summary>Solución comentada</summary>

Se reduce a la mitad.
</details>

**Ejercicio 5 · autónomo.** Calcula `P_min` con `ρ = 3000`.

<details><summary>Solución comentada</summary>

`1.91 h`.
</details>

**Ejercicio 6 · autónomo.** ¿Y con `ρ = 1000`?

<details><summary>Solución comentada</summary>

`3.30 h`.
</details>

**Ejercicio 7 · autónomo.** ¿Por qué `P_min` no depende del radio?

<details><summary>Solución comentada</summary>

Porque gravedad y centrífuga escalan igual con `R`.
</details>

**Ejercicio 8 · autónomo.** Si `a_T < 0`, ¿qué ocurre con el semieje?

<details><summary>Solución comentada</summary>

Disminuye y el cuerpo se adelanta.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** ¿Por qué la deriva Yarkovsky es más importante en cuerpos pequeños?

<details><summary>Solución comentada</summary>

La aceleración escala como `1/R` y la masa baja con `R³`.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Qué consecuencias tiene para una predicción de impacto en 50 años?

<details><summary>Solución comentada</summary>

El desplazamiento a lo largo de la órbita puede superar el radio terrestre; debe incluirse en el ajuste.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** Un cuerpo con `P = 1,5 h` y `ρ = 2000` sin cohesión, ¿es posible?

<details><summary>Solución comentada</summary>

No: está por debajo de la barrera de 2,33 h; necesita cohesión.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de Yarkovsky y YORP*: comparación integrada–fórmula, tabla física y barrera.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4.
</details>

## 17. Laboratorio: deriva de Gauss y barrera de rotación

El script [yarkovsky.py](yarkovsky.py) integra una órbita con aceleración tangencial y la compara con Gauss, calcula la tabla física y la barrera (**comprueba** 2 % en `Δa`, 5 % en `Δθ` y `P_min = 2,33 ± 0,01 h`).

**Datos:** asteroide **sintético**; aceleración de prueba exagerada; constantes recordadas, no consultadas. **Predice antes de ejecutar:** ¿Qué factor separa Δθ a 50 años de Δθ a 25 años? **Ejecución del 2026-11-09:**

```text
Python 3.12.9 (biblioteca estandar)
Aceleracion tangencial de prueba 3e-10 au/dia^2 durante 50 anios, a0 = 1.3 au
  Delta a: integrado = 9.4467e-04 au ; Gauss = 9.4416e-04 au ; diferencia = 0.05 %
  Delta theta - n t: integrado = -1.1551e-01 rad ; formula = -1.1545e-01 rad ; diferencia = 0.05 %
Tabla fisica ilustrativa (eta = 0.03, rho = 2000 kg/m3, a = 1.3 au):
  R =    50 m : a_T = 6.04e-13 m/s^2 ; da/dt = 1.90e-03 au/Myr ; desplazamiento a lo largo de la orbita en 100 anios = 9030.0 km
  R =   100 m : a_T = 3.02e-13 m/s^2 ; da/dt = 9.49e-04 au/Myr ; desplazamiento a lo largo de la orbita en 100 anios = 4515.0 km
  R =   500 m : a_T = 6.04e-14 m/s^2 ; da/dt = 1.90e-04 au/Myr ; desplazamiento a lo largo de la orbita en 100 anios = 903.0 km
Barrera de rotacion (rho = 1000 kg/m3): P_min = 3.301 h
Barrera de rotacion (rho = 2000 kg/m3): P_min = 2.334 h
Barrera de rotacion (rho = 3000 kg/m3): P_min = 1.906 h
Tiempo para duplicar la velocidad angular con 1e-3 rad/anio^2 desde P = 4 h: 13.77 Manios (valor ilustrativo)
Pruebas superadas.
```

```bash
python programa/clases/B58/B58-C14-efectos-yarkovsky-y-yorp/yarkovsky.py
```

**Límites:** órbita circular, fuerza constante, eficiencia fija; no es la teoría completa.

## 18. Errores frecuentes y cómo corregirlos

**Creer que una fuerza tangencial acelera el cuerpo en la órbita.** Se corrige con 8.2.

**Olvidar que `Δθ ∝ t²`.** Se corrige con 8.2.

**Aplicar la barrera a un cuerpo cohesivo.** Se corrige con 8.4.

**Tomar la tabla física como real.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué esperabas de Δθ y qué obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de Yarkovsky y YORP** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Conceptos de la clase | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con el análisis | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha | Declara lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular los datos como ilustrativos; no atribuir las derivas a un objeto real; declarar lo no consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y los datos, sintéticos; nada de lo calculado evalúa un objeto real ni sustituye a los sistemas oficiales de monitoreo y alerta.  Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

La integración reproduce Gauss a 0.1 % y la barrera es 2.33 h para 2000 kg/m³. Queda una pregunta: ¿qué pasa si el objeto sí impacta?

**Glosario español–inglés.** efecto Yarkovsky · *Yarkovsky effect*; YORP · *YORP effect*; ecuación de Gauss · *Gauss planetary equations*; barrera de rotación · *spin barrier*; movimiento medio · *mean motion*.

**Continuidad.** [B58-C15](../B58-C15-modelos-de-impacto-planetario/CLASE.md) estudia modelos de impacto planetario.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B58-C13 — Caracterización de rotación](../B58-C13-caracterizacion-de-rotacion/CLASE.md) · [📚 Bloque B58](../../../tronco-comun/B58-asteroides-cometas-y-defensa-planetaria.md) · [Siguiente: B58-C15 — Modelos de impacto planetario →](../B58-C15-modelos-de-impacto-planetario/CLASE.md)
<!-- /nav -->
