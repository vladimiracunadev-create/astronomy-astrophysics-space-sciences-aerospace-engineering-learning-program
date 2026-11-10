# B87-C05 — Magnetómetros

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B87](../../../tronco-comun/B87-sensores-y-control-de-actitud.md) · [← Anterior: B87-C04 — Sensores terrestres](../B87-C04-sensores-terrestres/CLASE.md) · [Siguiente: B87-C06 — Giroscopios MEMS →](../B87-C06-giroscopios-mems/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 5 del bloque B87. Nivel N3. El magnetómetro mide el vector del campo magnético en el cuerpo; comparado con un modelo del campo en la órbita da una dirección de referencia, y es el sensor de vector más barato y robusto en órbita baja. Aquí modelas el campo como un **dipolo inclinado sintético** (no el IGRF) a lo largo de una órbita de `500 km` y `51,6°`, y un sensor con ruido y sesgo. Todos los datos son sintéticos y de ejemplo.

## 2. Por qué esta clase existe

Un cubesat sin sensores estelares usa el campo magnético para saber hacia dónde apunta y para detumbling (C16). La decisión central: **¿cuánto varía el campo a lo largo de la órbita, cuánto ruido y sesgo tolera la dirección medida y qué parte de la actitud no ve el magnetómetro?** Una previa: el modelo de referencia (IGRF) tiene errores propios.

## 3. Lo que podrás hacer al terminar

1. Calcular el campo de un dipolo inclinado en la posición de una órbita circular.
2. Obtener el rango de `|B|` y la tasa de giro de su dirección a lo largo de una órbita.
3. Modelar un magnetómetro con ruido blanco y sesgo y calcular su error de dirección.
4. Predecir el error de dirección por ruido `σ√2/|B|` y compararlo con Monte Carlo.
5. Explicar por qué un solo vector no basta para la actitud completa.
6. Separar lo sintético (el dipolo) de lo consultado (el IGRF) y de lo no consultado.

La evidencia es la **mapa del campo magnético a lo largo de una órbita y de su error de dirección** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es un dipolo magnético?
2. ¿Cómo decae el campo de un dipolo con la distancia?
3. ¿Qué es el sesgo (*bias*) de un sensor?
4. ¿Qué es el ruido blanco?
5. ¿Qué es el IGRF?

<details>
<summary>Ver respuestas</summary>

1. Un campo `B = (μ₀/4π)(3(m·r̂)r̂ − m)/r³`, el de una espira o un imán pequeño. 2. Como `1/r³`. 3. Un desplazamiento constante de la medida. 4. Ruido no correlacionado entre muestras, de espectro plano. 5. El modelo internacional de referencia del campo geomagnético principal.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

En la órbita de ejemplo (`94,62 min`), `|B|` va de `24,88 µT` a `42,25 µT` (media `34,13 µT`) y su dirección gira `0,111°/s` en el sistema inercial. Un ruido de `100 nT` por eje da `0,249°` de error de dirección; un sesgo de `1000 nT` da `1,32°` en media y `2,30°` como máximo. Todo es **sintético**.

## 6. Vocabulario

El **campo dipolar** es `B = B₀ (R/r)³ [3(m̂·r̂) r̂ − m̂]`, con `B₀` la intensidad ecuatorial y `m̂` el eje del dipolo. La **inclinación del dipolo** respecto del eje de rotación es de `11°` en el ejemplo. El **IGRF** es el modelo estándar de grado 13 que se usaría en lugar del dipolo. El **ruido** `σ` es blanco por eje; el **sesgo** `b` es constante. El **error de dirección** es el ángulo entre `B̂` medido y verdadero. La **intensidad** es `|B|`.

## 7. Modelo mental: del dipolo a la dirección medida

```mermaid
flowchart LR
    O["posicion orbital r(t)"] --> D["campo dipolar B(r)"]
    D --> M["medida m = B + b + n"]
    M --> U["direccion unit(m)"]
    U --> E["error de direccion"]
```

*Descripción textual:* la posición en la órbita da el campo del modelo; el sensor añade sesgo y ruido; la dirección medida se compara con la del modelo y su diferencia es el error.

Analogía: una brújula en un barco: la aguja apunta bien lejos de hierros y se desvía cerca de ellos (sesgo) y tiembla con las olas (ruido). Límite: en órbita el campo cambia de dirección rápidamente y el modelo de referencia también se equivoca.

## 8. La explicación, paso a paso

### 8.1 Campo dipolar en la órbita

`B(r) = B₀ (R/r)³ [3(m̂·r̂) r̂ − m̂]` con `B₀ = 31,2 µT` y el eje del dipolo inclinado `11°`. En el radio orbital (`R + 500 km`) la intensidad ecuatorial vale `24,878 µT` y la polar `49,757 µT`. En la órbita de 51,6°, `|B|` varía de `24,879` a `42,254 µT`: un factor `1,70`.

### 8.2 Cambio de la dirección

La dirección de `B` gira respecto del sistema inercial `0,1112°/s` en media y hasta `0,1508°/s`: unas `1,75` veces la velocidad orbital (`0,0634°/s`). Ese giro es lo que hace que los magnetopares puedan generar par en todas las direcciones a lo largo de la órbita (C12).

### 8.3 Modelo de sensor

`m = B + b + n`. Con ruido blanco `σ` por eje, el error de dirección es `σ√2/|B|`: con `σ = 100 nT` y `|B| = 34,13 µT`, `0,237°` de teoría y `0,249°` simulado (la diferencia se debe a que la media de `1/|B|` supera `1/media(|B|)`). Un sesgo `b` produce un error máximo `asin(|b⊥|/|B|)`: con `1000 nT` en `x`, `1,318°` de media y `2,297°` como máximo (donde `|B|` es mínimo y el sesgo es perpendicular).

### 8.4 Lo que el magnetómetro no ve

Un solo vector deja libre el giro alrededor de `B`: la actitud completa requiere un segundo vector no paralelo (Sol, nadir, C09). Y el IGRF (S1) del que saldría el campo de referencia tiene su propio error y se actualiza cada cinco años; aquí el modelo dipolar es sintético y el sensor ve exactamente ese modelo, por lo que no aparece error de modelo.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `B` | vector de campo | T (µT, nT) | 24,9 a 42,3 µT |
| `B₀` | intensidad ecuatorial del dipolo (ejemplo) | T | 31,2 µT |
| `m̂` | eje del dipolo | — | inclinado 11° |
| `b` | sesgo del sensor | T | 1000 nT en x |
| `σ` | ruido por eje | T | 100 nT |

## 10. Convenciones y referencias

Campo **sintético** dipolar de ejemplo (sin armónicos superiores, sin rotación terrestre, sin variación secular). Tolerancias: `|B|` entre la mitad del ecuatorial y el polar; error de ruido dentro del 6 % de `σ√2/|B_media|`; error de sesgo máximo `>` medio `> 0`. Cuaternión `q = [qx, qy, qz, qw]` con la parte escalar al final, `v_B = A(q) v_I`, producto tal que `A(q⊗p) = A(q) A(p)`, cinemática `q̇ = ½ [ω; 0] ⊗ q` con `ω` del cuerpo respecto del sistema inercial expresada en el cuerpo (la biblioteca [adcs_comun.py](../adcs_comun.py) del bloque lo comprueba). Sistema inercial `I` de **ejemplo** (ejes sin relación con J2000), órbita circular de dos cuerpos con radio terrestre `6 378 137 m` y `μ = 3,986004418 × 10¹⁴ m³/s²` como valores adoptados de ejemplo. Satélite **sintético** `I = diag(0,35; 0,40; 0,30) kg·m²` salvo que la clase diga otra cosa. Todo dato es sintético con semilla fija.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NOAA/NCEI, International Geomagnetic Reference Field (IGRF) — https://www.ncei.noaa.gov/products/international-geomagnetic-reference-field (consultada 2026-11-10) | página del producto | el IGRF es un modelo estándar del campo magnético principal terrestre, mantenido por IAGA, expresado como serie truncada de un potencial escalar (grado N = 13) con su variación secular; la generación vigente es IGRF-14 (coeficientes cerrados en noviembre de 2024) | Consultada |
| — | Relaciones estándar de dinámica de actitud, estimación y control usadas en esta clase (ecuaciones de Euler, cinemática de cuaterniones, problema de Wahba, filtro de Kalman multiplicativo, estabilidad de Lyapunov, modelos de sensores y actuadores) | — | las verifica el laboratorio con una segunda vía (conservación, comparación entre métodos, propagación independiente o Monte Carlo) | No consultada en una fuente concreta |
| — | Libros de texto de actitud y control (p. ej. Wertz, Markley–Crassidis, Sidi) y hojas de datos de fabricantes | — | — | No consultada |

Límites: La página del IGRF (S1) respalda solo que es el modelo estándar (generación 14, grado 13) del campo principal y su variación secular; esta clase no usa sus coeficientes ni los consultó, y el dipolo de ejemplo no representa el campo real. El modelo de sensor no se consultó en una fuente concreta; se valida con la comparación contra `σ√2/|B|`.

## 12. Cómo ver el campo y el error

| Magnitud | Valor |
|---|---|
| `|B|` mínimo / máximo | 24,88 / 42,25 µT |
| giro de la dirección (media) | 0,1112°/s |
| error por ruido (sim / teoría) | 0,249° / 0,237° |
| error por sesgo de 1000 nT (media / máx.) | 1,32° / 2,30° |

Descripción larga: el campo varía casi un factor 1,7 en la órbita y el sesgo de 1000 nT produce un error mayor donde el campo es más débil.

## 13. Ejemplo trabajado: error de dirección por ruido

**Paso 1 · Campo.** `|B|` medio `= 34,13 µT`.

**Paso 2 · Ruido.** `σ = 100 nT` por eje.

**Paso 3 · Error teórico.** `σ√2/|B| = 141,4 nT/34,13 µT = 0,237°`.

**Paso 4 · Simulación.** 20 000 muestras dan `0,249°`.

**Paso 5 · Comprobación.** La diferencia de `5,1 %` es el efecto de los puntos de campo débil.

## 14. Distintas formas de describir la medida del campo

**Dipolo inclinado** (esta clase): sencillo, ve el orden de magnitud. **IGRF de grado 13:** el modelo de referencia real (consultado solo en su descripción). **Medida en el cuerpo:** `m = (I + S) A B + b + n`, con escala y desalineación (C08). El error de un modelo de referencia se suma al del sensor.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula la intensidad ecuatorial de un dipolo con `B₀ = 31,2 µT` a `r = 6878 km`. *Pasos:* `(R/r)³`.

<details><summary>Solución comentada</summary>

`(6378,137/6878,137)³ = 0,7974`; `B = 24,878 µT`.
</details>

**Ejercicio 2 · con una pista.** ¿Cuánto vale el campo polar frente al ecuatorial en un dipolo?

<details><summary>Solución comentada</summary>

El doble: `49,76 µT` frente a `24,88 µT`.
</details>

**Ejercicio 3 · casi autónomo.** Con `σ = 50 nT` por eje y `|B| = 30 µT`, ¿qué error de dirección esperas? *Pista:* `σ√2/|B|`.

<details><summary>Solución comentada</summary>

`0,135°`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** ¿Qué sesgo máximo tolera un magnetómetro si el error de dirección debe ser `< 0,5°` en `|B| = 25 µT`?

<details><summary>Solución comentada</summary>

`b < |B| sin 0,5° = 218 nT`.
</details>

**Ejercicio 5 · autónomo.** ¿Por qué el error por sesgo es máximo donde el campo es débil?

<details><summary>Solución comentada</summary>

Porque el ángulo `≈ b⊥/|B|` crece cuando `|B|` baja: el mínimo de `|B|` (`24,88 µT`) da el máximo (`2,30°`).
</details>

**Ejercicio 6 · autónomo.** Si el sesgo está en la dirección del campo, ¿cuánto vale el error de dirección?

<details><summary>Solución comentada</summary>

Cero a primer orden: solo cambia el módulo, no la dirección (solo cuenta la componente perpendicular).
</details>

**Ejercicio 7 · autónomo.** ¿Qué dirección del cuerpo respecto del campo no se puede estimar con un solo vector?

<details><summary>Solución comentada</summary>

El giro alrededor de `B̂`; hace falta un segundo vector no paralelo.
</details>

**Ejercicio 8 · autónomo.** ¿Cuántos grados giraría la dirección de `B` en 10 minutos con la tasa media?

<details><summary>Solución comentada</summary>

`66,7°`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** **Transferencia.** Un colega usa estos `µT` para dimensionar un magnetopar de una misión. ¿Es válido?

<details><summary>Solución comentada</summary>

No: es un dipolo sintético sin armónicos ni variación temporal; el dimensionamiento requiere el IGRF u otro modelo validado (consultado aquí solo en su descripción) y margen.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** **Transferencia.** ¿Qué cambia en la dirección de `B` si el satélite pasa de 51,6° a una órbita polar?

<details><summary>Solución comentada</summary>

El campo recorre las latitudes magnéticas extremas y su dirección gira más (varía casi 180° entre polos); el rango de `|B|` crece hacia el polar.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** **Transferencia.** ¿Por qué un magnetómetro cerca de un magnetopar debe leerse con el actuador apagado?

<details><summary>Solución comentada</summary>

Porque el campo del actuador (del orden de µT a distancia corta) se suma al ambiental y falsea la medida; se alterna medida y actuación.
</details>

**Ejercicio 12 · integrador.** **Integrador.** **Integrador.** Elabora tu *mapa del campo y su error de dirección*: rango de `|B|`, giro de la dirección, error por ruido y por sesgo, más la lista de consultado y sintético.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4, 12 y la salida del laboratorio.
</details>

## 17. Laboratorio: campo dipolar y magnetómetro con ruido y sesgo

El script [magnetometro.py](magnetometro.py) calcula el campo dipolar en 720 puntos de una órbita de `500 km` y `51,6°`, obtiene el rango de `|B|` y el giro de su dirección, simula 20 000 medidas con ruido de `100 nT` y mide el error de dirección frente a `σ√2/|B|`, y aplica un sesgo de `1000 nT` (**comprueba** acotación de `|B|`, acuerdo del ruido dentro del 6 % y error máximo mayor que el medio). Usa la biblioteca común [adcs_comun.py](../adcs_comun.py) del bloque.

**Datos:** campo, órbita y medidas **sintéticos** (semilla 20260515); `B₀` y la inclinación del dipolo son de ejemplo; no son el IGRF ni datos medidos. **Predice antes de ejecutar:** ¿Dónde es mayor el error por sesgo, en el campo débil o en el fuerte? (En el débil.) **Ejecución del 2026-11-10 (Python 3.12.9, numpy 2.4.4):**

```text
Python 3.12.9 | numpy 2.4.4
B87-C05 magnetometro y campo dipolar | dipolo SINTETICO inclinado 11 deg, B0 = 31.2 uT; orbita de 500 km, 51.6 deg
periodo orbital = 94.62 min
|B| a lo largo de la orbita: min = 24.879 uT ; max = 42.254 uT ; media = 34.131 uT
dipolo en el radio orbital: ecuador = 24.878 uT ; polo = 49.757 uT
giro de la direccion de B (inercial): media = 0.1112 deg/s ; maximo = 0.1508 deg/s
ruido blanco de 100 nT por eje: error de direccion rms = 0.2494 deg (teoria sigma*sqrt(2)/|B| = 0.2374)
sesgo de 1000 nT en x: error de direccion medio = 1.318 deg ; maximo = 2.297 deg
Pruebas superadas.
```

```bash
python programa/clases/B87/B87-C05-magnetometros/magnetometro.py
```

**Límites:** dipolo sin rotación terrestre ni armónicos, sistema inercial de ejemplo, sensor ideal sin escala ni desalineación; el error del modelo de referencia no se incluye.

## 18. Errores frecuentes y cómo corregirlos

**Usar el dipolo como si fuese el IGRF.** Declara qué modelo usas y su error (8.4)

**Ignorar el campo de los propios actuadores.** Mide con el actuador apagado (ejercicio 11)

**Pensar que `B` basta para la actitud completa.** Añade un segundo vector (8.4)

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué rango de `|B|` esperabas? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **mapa del campo magnético a lo largo de una órbita y de su error de dirección** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Explica el método y su dominio | Explica los límites y las alternativas |
| Cálculo | Sin unidades | Con errores | Resultados con unidades y comprobados | Resuelve casos nuevos |
| Numérico | Sin comprobar | Un caso | Verifica con una segunda vía en varios casos | Interpreta las diferencias y los fallos |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo sintético y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular los datos como sintéticos; verificar cada resultado con una segunda vía; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y los datos son sintéticos; ningún resultado describe una misión real ni sustituye el diseño y la verificación de un subsistema de actitud con herramientas validadas, ensayos y revisión de especialistas.  Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

En una órbita de 500 km el campo dipolar de ejemplo va de `24,9` a `42,3 µT`; `100 nT` de ruido dan `0,25°` y `1000 nT` de sesgo hasta `2,3°`. Queda una pregunta: ¿cómo se mide la velocidad angular y cuánto se desvía en el tiempo?

**Glosario español–inglés.** magnetómetro · *magnetometer*; campo dipolar · *dipole field*; sesgo · *bias*; ruido blanco · *white noise*; modelo de referencia · *reference model*; variación secular · *secular variation*.

**Continuidad.** [B87-C06](../B87-C06-giroscopios-mems/CLASE.md) trata los giroscopios MEMS, que miden la velocidad angular y acumulan deriva.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B87-C04 — Sensores terrestres](../B87-C04-sensores-terrestres/CLASE.md) · [📚 Bloque B87](../../../tronco-comun/B87-sensores-y-control-de-actitud.md) · [Siguiente: B87-C06 — Giroscopios MEMS →](../B87-C06-giroscopios-mems/CLASE.md)
<!-- /nav -->
