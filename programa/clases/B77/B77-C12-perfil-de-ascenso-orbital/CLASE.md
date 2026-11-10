# B77-C12 — Perfil de ascenso orbital

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B77](../../../tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md) · [← Anterior: B77-C11 — Ventanas de lanzamiento — Dinámica de lanzamiento y reentrada](../B77-C11-ventanas-de-lanzamiento-dinamica-de-lanzamiento-y-reentrada/CLASE.md) · [Siguiente: B77-C13 — Inyección y dispersión orbital →](../B77-C13-inyeccion-y-dispersion-orbital/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 12 del bloque B77. Nivel N3. Un ascenso orbital no sube recto: tras una fase vertical corta el vehículo se inclina y gana velocidad horizontal hasta que, al agotar el motor, su velocidad es casi circular. Aquí integras en el plano orbital un ascenso sintético de dos etapas con un giro de gravedad, ajustas un ángulo para cerrar la órbita y verificas el resultado con la energía y el momento angular. Usas [C08](../B77-C08-perdidas-gravitacionales/CLASE.md) y [C09](../B77-C09-perdidas-aerodinamicas/CLASE.md) para las pérdidas.

## 2. Por qué esta clase existe

La trayectoria de ascenso decide a la vez las pérdidas, las cargas y la órbita alcanzada. La decisión central: **¿qué perfil de inclinación lleva al vehículo a una órbita casi circular y qué cuesta?**

## 3. Lo que podrás hacer al terminar

1. Escribir las ecuaciones del giro de gravedad en coordenadas polares.
2. Integrar el ascenso con RK4 en una Tierra esférica no rotante.
3. Ajustar por bisección un ángulo de empuje para anular `γ` al agotar la etapa 2.
4. Obtener perigeo y apogeo por vis-viva.
5. Verificar con una propagación balística la energía y el momento angular.
6. Separar lo consultado (radio, atmósfera, `g₀`) de lo no consultado (`μ`) y de lo ilustrativo (vehículo).

La evidencia es la **ficha de ascenso orbital** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es el ángulo de la trayectoria `γ`?
2. ¿Qué es la ecuación vis-viva?
3. ¿Qué es un giro de gravedad?
4. ¿Qué es una bisección?
5. ¿Qué se conserva en vuelo balístico?

<details>
<summary>Ver respuestas</summary>

1. El ángulo entre la velocidad y el horizonte local. 2. `v² = μ(2/r − 1/a)`, que liga velocidad, radio y semieje mayor. 3. Un ascenso en que el empuje se alinea con la velocidad y la gravedad inclina la trayectoria. 4. Un método de búsqueda de raíces que reduce a la mitad un intervalo. 5. La energía específica y el momento angular específico.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Un lanzador sintético de dos etapas (`Δv` ideal `9461 m/s`) sube 10 s en vertical, gira a `85°` y sigue un giro de gravedad. La etapa 2 empuja `22,82°` por debajo de la velocidad. Tras `298,1 s` queda a `246,9 km` con `7740 m/s` y `γ = 0,00°`: órbita de `191 × 247 km`. Es el **ejemplo conductor**; es **ilustrativo** y no corresponde a ningún lanzador real.

## 6. Vocabulario

El **giro de gravedad** mantiene el empuje alineado con la velocidad. La **fase vertical** inicial permite despejar la torre y ganar velocidad. El **ángulo de la trayectoria** `γ` se mide sobre el horizonte local. El **agotamiento** (burnout) es el fin del empuje. La **ecuación vis-viva** relaciona `v`, `r` y `a`.

## 7. Modelo mental

```mermaid
flowchart LR
    V["fase vertical 10 s"] --> K["gamma0 = 85 grados"]
    K --> G1["etapa 1: giro de gravedad"]
    G1 --> S["separacion"]
    S --> G2["etapa 2: empuje con desvio delta"]
    G2 --> B["agotamiento: gamma = 0"]
    B --> O["perigeo / apogeo (vis-viva)"]
```

*Descripción textual:* una fase vertical, un giro a `85°`, la etapa 1 en giro de gravedad, la separación y la etapa 2 con desvío del empuje que cierra `γ = 0`; al agotarse, la vis-viva da perigeo y apogeo.

Analogía: lanzar una pelota para que rase la copa de un árbol y siga por el horizonte: hay que subir primero y luego aplanar la trayectoria para no volver a bajar. Límite: la Tierra no rota en este modelo y el control es una ley simple, no un guiado real.

## 8. La explicación, paso a paso

### 8.1 Ecuaciones

En coordenadas polares con `r`, `θ`: `ṙ = v sin γ`, `θ̇ = v cos γ/r`, `v̇ = (F cos δ − D)/m − (μ/r²) sin γ`, `γ̇ = [F sin δ/m − (μ/r² − v²/r) cos γ]/v`. En la etapa 1, `δ = 0` (giro de gravedad). La masa baja con `ṁ = −F/(Isp g₀)`.

### 8.2 Perfil

| `t` (s) | `h` (km) | `v` (m/s) | `γ` (°) |
|---|---|---|---|
| 20 | 1,5 | 156 | 77,7 |
| 40 | 6,2 | 359 | 62,4 |
| 60 | 14,2 | 633 | 49,4 |
| 80 | 25,4 | 1018 | 39,6 |
| 100 | 40,3 | 1562 | 32,7 |
| 120 | 59,5 | 2339 | 27,9 |
| 140 | 85,0 | 3518 | 24,9 |

La separación ocurre a los `147,1 s` con `h = 96,2 km`, `v = 4113 m/s` y `γ = 24,2°`. La presión dinámica máxima es `46,6 kPa`.

### 8.3 Cerrar la órbita

Con `γ₀ = 85°` fijo, la bisección sobre el desvío `δ` del empuje de la etapa 2 da `δ = -22,8186°` para que `γ = 0` al agotarse. Resultado: `h = 246,89 km`, `v = 7740,2 m/s` frente a `7756,7 m/s` circulares. Por vis-viva: perigeo `191,1 km`, apogeo `246,9 km`, `e = 0,0042`.

### 8.4 Verificación

Una propagación balística con RK4 en cartesianas conserva la energía (error `7,3e-15`) y el momento angular (`3,7e-15`), y sus extremos de `r` coinciden con los de la vis-viva (`3,2e-10` y `1,4e-15`). Esto valida la órbita calculada, no el modelo de empuje ni de arrastre. La Tierra no rota aquí: el alcance de `932 km` es respecto de un suelo inmóvil.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `μ` | parámetro gravitacional | m³/s² | 3,986004418·10¹⁴ (no consultado) |
| `R_E` | radio ecuatorial | m | 6 378 137 (NASA/NSSDC) |
| `γ` | ángulo de la trayectoria | ° | 85 → 0,0 |
| `δ` | desvío del empuje en la etapa 2 | ° | -22,82 (ajustado) |
| `h`, `v` | altitud y velocidad al agotarse | km, m/s | 246,9; 7740 |
| `q_max` | presión dinámica máxima | kPa | 46,6 |

## 10. Convenciones y referencias

Plano orbital, Tierra esférica no rotante, `r` desde el centro; `R_E` y atmósfera de la NASA/NSSDC, `g₀` del NIST; `μ` es un valor estándar **no consultado** en esta sesión. Vehículo, vertical, `γ₀` y `δ` ilustrativos.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA/NSSDC, Earth Fact Sheet — https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html (consultada 2026-11-10) | ficha completa leída | radio ecuatorial 6378,137 km, ρ₀ = 1,217 kg/m³ y altura de escala 8,5 km | Consultada |
| S2 | NIST, CODATA 2022, standard acceleration of gravity — https://physics.nist.gov/cgi-bin/cuu/Value?gn (consultada 2026-11-10) | entrada gn | g₀ = 9,80665 m/s² | Consultada |
| S3 | NASA Glenn, Drag Coefficient — https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/drag-coefficient/ (consultada 2026-11-10) | página completa | D = Cd q A | Consultada |
| — | Ecuaciones del giro de gravedad, ecuación vis-viva y valor de μ | — | las verifica el laboratorio con una segunda vía | No consultada en una fuente concreta |

Límites: Tierra no rotante, atmósfera exponencial, `Cd` constante, `μ` no consultado en una fuente; el vehículo y la ley de guiado son sintéticos; no se comparó con ningún vuelo.

## 12. Cómo ver el resultado

| Magnitud | Valor |
|---|---|
| agotamiento | 246,9 km, 7740 m/s |
| órbita | 191 × 247 km |
| `q_max` | 46,6 kPa |
| energía y momento angular | 7e-15; 4e-15 |
| `δ` ajustado | -22,8186° |

Descripción larga: el vehículo sube casi vertical, se inclina progresivamente hasta casi horizontal y al agotarse tiene velocidad cercana a la circular.

## 13. Ejemplo trabajado: la órbita desde el estado de agotamiento

**Paso 1 · Energía.** `ε = v²/2 − μ/r = -3,021e+07 J/kg`.

**Paso 2 · Semieje.** `a = −μ/(2ε) = 6597,1 km`.

**Paso 3 · Excentricidad.** `e = 0,0042`; perigeo `191,1 km`, apogeo `246,9 km`.

## 14. Distintas formas de describir el resultado

**Por tabla:** `t`, `h`, `v`, `γ`. **Por elementos:** `a`, `e`. **Por energía:** `ε`. **Por ángulo:** `γ(t)`. **Por vis-viva:** perigeo y apogeo.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula la velocidad circular a 200 km con `μ = 3,986·10¹⁴` y `R = 6378,137 km`. *Pasos:* `√(μ/r)`.

<details><summary>Solución comentada</summary>

`√(3,986e14/6,578137e6) = 7784 m/s`.
</details>

**Ejercicio 2 · con una pista.** Energía específica de una órbita circular de 7784 m/s a 200 km. *Pista:* `−μ/(2r)`.

<details><summary>Solución comentada</summary>

`−3,03·10⁷ J/kg`.
</details>

**Ejercicio 3 · casi autónomo.** ¿Por qué el giro de gravedad no necesita control de ángulo de ataque?

<details><summary>Solución comentada</summary>

Porque el empuje va alineado con la velocidad y la gravedad es la que inclina la trayectoria.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** ¿Qué le pasa a la órbita si `γ ≠ 0` al agotarse con `v` circular?

<details><summary>Solución comentada</summary>

El punto de agotamiento deja de ser un extremo: el perigeo baja (si `γ < 0`) o el apogeo sube (si `γ > 0`).
</details>

**Ejercicio 5 · autónomo.** Relación entre `h_bo = 246,9 km` y el apogeo.

<details><summary>Solución comentada</summary>

Coinciden porque `γ = 0` y `v` ligeramente menor que la circular: el punto es el apogeo.
</details>

**Ejercicio 6 · autónomo.** Déficit de velocidad respecto de la circular.

<details><summary>Solución comentada</summary>

`16,4 m/s`.
</details>

**Ejercicio 7 · autónomo.** Perigeo si el déficit fuera 100 m/s mayor (aprox., en el apogeo).

<details><summary>Solución comentada</summary>

En el apogeo, `Δr_p ≈ 4 r Δv/v = 4 × 6,62·10⁶ × 100/7740 ≈ 340 km`: el perigeo pasaría de ~191 km a unos −150 km, bajo la superficie.
</details>

**Ejercicio 8 · autónomo.** ¿Qué cambia si la Tierra rota y se lanza hacia el este?

<details><summary>Solución comentada</summary>

La velocidad inicial inercial sube hasta ~460 m/s en el ecuador y se necesita menos `Δv`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un artículo describe un perfil con tres etapas y coast. ¿Es comparable con este laboratorio?

<details><summary>Solución comentada</summary>

No directamente: faltan datos y este laboratorio solo tiene dos etapas y sin coast.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** Un colega extrapola `δ` ajustado a otro vehículo. ¿Qué error comete?

<details><summary>Solución comentada</summary>

`δ` depende de la masa, el empuje y la altitud de cada vehículo; solo es válido para este.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Qué falta para tener un guiado real?

<details><summary>Solución comentada</summary>

Navegación, ley de guiado en lazo cerrado, restricciones de carga y dispersiones.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de ascenso orbital*: perfil `t, h, v, γ`, separación, estado de agotamiento, órbita y lista de qué es consultado, no consultado e ilustrativo.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: ascenso orbital con giro de gravedad

El script [ascenso.py](ascenso.py) integra el ascenso de un lanzador sintético, ajusta por bisección el desvío del empuje de la etapa 2 y verifica la órbita con una propagación balística (**comprueba** energía y momento angular < 1e-8 y perigeo/apogeo < 1e-4).

**Datos:** radio, atmósfera y `g₀` consultados; `μ` **no consultado** (valor estándar); vehículo y guiado **ilustrativos**. **Predice antes de ejecutar:** ¿la velocidad de agotamiento será mayor o menor que la circular? (ligeramente menor: 7740 frente a 7757 m/s.) **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Lanzador SINTETICO de dos etapas; Delta_v ideal total = 9461.3 m/s; vertical 10 s; gamma0 = 85.0 grados; desvio del empuje en la etapa 2 (biseccion) delta = -22.8186 grados
  t [s]   h [km]   v [m/s]  gamma [grados]
    20.0     1.47     155.5    77.661
    30.0     3.41     250.0    69.904
    40.0     6.17     358.6    62.416
    50.0     9.76     484.8    55.539
    60.0    14.16     633.1    49.430
    70.0    19.38     808.9    44.130
    80.0    25.44    1018.0    39.614
    90.0    32.38    1266.6    35.816
   100.0    40.29    1562.2    32.654
   110.0    49.29    1914.9    30.049
   120.0    59.54    2339.3    27.930
   130.0    71.31    2859.6    26.238
   140.0    84.99    3518.4    24.930
Separacion de etapas: t = 147.1 s, h = 96.2 km, v = 4113.4 m/s, gamma = 24.22 grados
Agotamiento (t = 298.1 s): h = 246.89 km, v = 7740.2 m/s (circular a esa altitud: 7756.7), gamma = 0.0000 grados, alcance = 932 km, m = 4500 kg
Presion dinamica maxima = 46.6 kPa
Orbita resultante (vis-viva): perigeo = 191.1 km, apogeo = 246.9 km, e = 0.0042
Propagacion balistica: r minimo/maximo = 191.1 / 246.9 km; errores relativos: perigeo 3.2e-10, apogeo 1.4e-15, energia 7.3e-15, momento angular 3.7e-15
Pruebas superadas.
```

```bash
python programa/clases/B77/B77-C12-perfil-de-ascenso-orbital/ascenso.py
```

**Límites:** Tierra no rotante, sin viento, sin J2, atmósfera exponencial, guiado de dos parámetros.

## 18. Errores frecuentes y cómo corregirlos

**Creer que el vehículo sube recto hasta la altitud final.** Se corrige con 8.2.

**Tomar la conservación de energía como validación del empuje.** Se corrige con 8.4.

**Olvidar que `γ = 0` solo cierra la órbita si `v` es circular.** Se corrige con 8.3.

**Presentar el perfil como el de un lanzador real.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué órbita esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de ascenso orbital** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Aplica el modelo con sus supuestos | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas con unidades | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con una segunda vía | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo ilustrativo y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular el vehículo y el guiado como ilustrativos; declarar que `μ` no se consultó; no presentar el perfil como real; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y sus datos son sintéticos o ilustrativos; ningún resultado describe un vehículo real ni sustituye al análisis de seguridad, a la certificación o a los documentos del operador. Nada de lo simulado se presenta como observado ni como datos de vuelo. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Un lanzador sintético con giro de gravedad llega a una órbita de `191 × 247 km` a los `298 s`. Queda una pregunta: ¿cuánto se desvía esa órbita de la deseada por los errores del ascenso?

**Glosario español–inglés.** giro de gravedad · *gravity turn*; ángulo de la trayectoria · *flight-path angle*; agotamiento · *burnout*; vis-viva · *vis-viva equation*; perigeo · *perigee*.

**Continuidad.** [siguiente]

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B77-C11 — Ventanas de lanzamiento — Dinámica de lanzamiento y reentrada](../B77-C11-ventanas-de-lanzamiento-dinamica-de-lanzamiento-y-reentrada/CLASE.md) · [📚 Bloque B77](../../../tronco-comun/B77-dinamica-de-lanzamiento-y-reentrada.md) · [Siguiente: B77-C13 — Inyección y dispersión orbital →](../B77-C13-inyeccion-y-dispersion-orbital/CLASE.md)
<!-- /nav -->
