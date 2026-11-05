# B01-C08 — Mediciones y unidades astronómicas

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B01](../../../tronco-comun/B01-el-universo-y-el-pensamiento-cientifico.md) · [← Anterior: B01-C07 — Hipótesis y predicciones falsables](../B01-C07-hipotesis-y-predicciones-falsables/CLASE.md) · [Siguiente: B01-C09 — Luz como fuente de información →](../../../tronco-comun/B01-el-universo-y-el-pensamiento-cientifico.md#b01-c09)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Octava clase del bloque B01. Has escrito hipótesis con predicciones numéricas (C07); para que esos números se entiendan hay que saber en qué unidades se dan y cómo pasar de unas a otras sin error. Sigues en el nivel N1.

Verás las unidades base del Sistema Internacional, las unidades propias de la astronomía (unidad astronómica, año luz, parsec), las conversiones entre ellas y una técnica para comprobar cualquier fórmula: el análisis dimensional. No verás las incertidumbres de las conversiones (C18) ni coordenadas celestes.

## 2. Por qué esta clase existe

En 1999 se perdió la sonda Mars Climate Orbiter por una discrepancia entre unidades inglesas y métricas (C04, fuente NASA). La ciencia estaba bien; la conversión, no. En astronomía el riesgo es mayor porque se manejan magnitudes que van de metros a 10²⁶ m y se usan unidades distintas según el tema: kilómetros para planetas, unidades astronómicas para el sistema solar, años luz en divulgación, parsecs en la literatura profesional.

La decisión central es: **¿en qué unidad debo expresar esta magnitud y cómo me aseguro de que la conversión es correcta?** Aprenderás a convertir con factores exactos, a comprobar dimensiones y a escribir una hoja de conversiones verificada que otros puedan reutilizar.

## 3. Lo que podrás hacer al terminar

1. Enumerar las siete unidades base del SI y decir cuáles usa esta clase.
2. Definir unidad astronómica, año luz y parsec, y dar sus valores en metros.
3. Convertir longitudes entre metros, kilómetros, au, años luz y parsecs, sin perder cifras significativas.
4. Usar el análisis dimensional para detectar errores en una fórmula o un cálculo.
5. Escribir cada resultado con su unidad y un número de cifras coherente con los datos.
6. Elaborar una **hoja de conversiones verificada**.

La evidencia es la hoja del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

Necesitas C01 y C02 (escalas, au, ly, pc), C04 (SI, tiempo de luz) y C07 (predicciones con unidad). Cinco preguntas:

1. ¿Cuántos metros hay en 1 km?
2. ¿Cuántos segundos tiene un año de 365,25 días?
3. ¿Qué distancia es mayor: 1 au o 1 ly?
4. ¿Qué significa escribir 3,0 × 10⁸ m/s?
5. ¿Qué tiempo tarda la luz en recorrer 1 au?

<details>
<summary>Ver respuestas</summary>

1. 1 000. 2. `365,25 × 86 400 = 31 557 600 s`. 3. 1 ly (unas 63 000 au). 4. Trescientos millones de metros por segundo, con dos cifras significativas. 5. 499,0 s (C04).
</details>

Con cuatro o cinco aciertos, sigue; con tres o menos, repasa C02 y C04.

## 5. Un caso real: la misma galaxia en cuatro unidades

Tu galaxia de la línea Hα (C01) está a unos 43 Mpc. Un artículo profesional la daría así; una nota de prensa diría «140 millones de años luz»; un cálculo de ingeniería la querría en metros; y un modelo del sistema solar la compararía en unidades astronómicas. Son lo mismo con otro nombre. La diferencia es qué se entiende por «Mpc», «año luz» y «au», y de qué constante exacta salen.

Para no equivocarte necesitas dos cosas: factores de conversión **exactos** (los que se definen) y la disciplina de arrastrar la unidad en cada paso. Este es nuestro **ejemplo conductor**: convertir 43 Mpc a metros, años luz y au, y comprobar que el resultado es coherente con el tiempo de luz de C04. Límite: 43 Mpc es un valor **estimado para docencia** (C01), no una distancia medida de un objeto del catálogo.

## 6. Vocabulario

El **Sistema Internacional (SI)** es el conjunto de unidades coherentes acordado por la comunidad internacional; sus siete **unidades base** son segundo, metro, kilogramo, amperio, kelvin, mol y candela (S1, S2). Una **unidad derivada** se forma con las base (m/s). Una **unidad no SI aceptada** es una unidad histórica o práctica reconocida para su uso con el SI; la **unidad astronómica (au)** es una de ellas y vale exactamente 149 597 870 700 m (S2, S3). El **año luz (ly)** es la distancia que recorre la luz en el vacío en un año juliano de 365,25 días. El **parsec (pc)** es la distancia a la que una unidad astronómica subtiende un ángulo de un segundo de arco. Un **factor de conversión** es una razón igual a 1 (por ejemplo, `1 au/149 597 870 700 m`). Las **dimensiones** de una magnitud son sus bases (longitud L, tiempo T, masa M); el **análisis dimensional** comprueba que ambos lados de una ecuación tengan las mismas dimensiones. Las **cifras significativas** son las que aportan información; el resto sobra.

## 7. Modelo mental: la escalera de unidades

Imagina una escalera con peldaños de unidades; el metro está abajo y cada unidad astronómica es un peldaño que se alcanza multiplicando por un factor definido. Para pasar de un peldaño a otro multiplicas por un factor de conversión que vale 1.

```mermaid
flowchart LR
    M["metro (m)"] -->|"× 1 au / 149 597 870 700 m"| AU["unidad astronómica (au)"]
    AU -->|"× 1 ly / 63 241,1 au"| LY["año luz (ly)"]
    LY -->|"× 1 pc / 3,2616 ly"| PC["parsec (pc)"]
    PC -->|"× 10⁶"| MPC["megaparsec (Mpc)"]
```

*Descripción textual:* una cadena de cinco unidades: metro, unidad astronómica, año luz, parsec y megaparsec. Entre cada par se indica el factor de conversión; todos valen 1 porque numerador y denominador son la misma longitud.

Analogía: un cambio de moneda. Límite: las monedas tienen cambio variable; estas unidades tienen factores **definidos y fijos** (salvo el año luz, que depende de la convención del año juliano).

## 8. La explicación, paso a paso

### 8.1 Del metro a la unidad astronómica

El metro se define con la velocidad de la luz fijada en 299 792 458 m/s (C04, S1). La unidad astronómica nació como la distancia media Tierra–Sol, y hoy es una longitud **definida**: `1 au = 149 597 870 700 m` exactamente (S2, S3). Eso significa que no cambia aunque cambie la órbita terrestre ni su medida; la distancia Tierra–Sol puede variar (entre 147,1 y 152,1 millones de km, según la ficha del Sol, S4), pero la unidad no.

### 8.2 El año luz y el parsec

El año luz es `c × 1 año juliano = 299 792 458 m/s × 31 557 600 s = 9 460 730 472 580 800 m`, es decir, `9,4607 × 10¹⁵ m = 63 241,1 au`. El parsec se obtiene de la geometría: si un objeto está tan lejos que 1 au se ve bajo 1″ (`1″ = π/648 000 rad`), su distancia es `1 au/(π/648 000) = (648 000/π) au = 206 264,806 au = 3,0857 × 10¹⁶ m = 3,2616 ly`. El Mpc es un millón de parsecs.

### 8.3 Convertir con factores que valen 1

Convierte 43 Mpc a metros multiplicando por factores que se cancelan:

`43 Mpc × (10⁶ pc/1 Mpc) × (3,0857 × 10¹⁶ m/1 pc) = 1,327 × 10²⁴ m`.

Las unidades Mpc y pc se cancelan y queda m. En años luz: `43 × 10⁶ pc × 3,2616 ly/pc = 1,4025 × 10⁸ ly`: unos 140 millones de años luz, como en C01. En au: `1,327 × 10²⁴ m/1,496 × 10¹¹ m/au = 8,87 × 10¹² au`.

### 8.4 Análisis dimensional

Antes de calcular, comprueba dimensiones. La ley de Hubble `d = v/H₀` tiene `[v] = km/s` y `[H₀] = km/s/Mpc`; al dividir queda `Mpc`, que es una longitud: correcto. Si alguien escribe `d = H₀/v`, queda `1/Mpc`: no es una longitud, así que está mal. Del mismo modo, el tiempo de luz `t = d/c` da `m ÷ m/s = s`. El análisis dimensional **no** garantiza que la fórmula sea correcta, pero detecta una gran parte de los errores.

### 8.5 Cifras significativas

Una conversión exacta no agrega información. Si `d = 43 Mpc` tiene dos cifras significativas, escribe `1,3 × 10²⁴ m`, no `1,3268 × 10²⁴ m`. Reserva las cifras extra para pasos intermedios y redondea al final.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor o nota |
|---|---|---|---|
| `c` | velocidad de la luz en el vacío | m/s | 299 792 458 (exacto; S1) |
| au | unidad astronómica | m | 149 597 870 700 (exacto; S2, S3) |
| ly | año luz | m | 9 460 730 472 580 800 (con año juliano; calculado) |
| pc | parsec | m | 3,0857 × 10¹⁶ (calculado de `(648 000/π) au`) |
| Mpc | megaparsec | m | 3,0857 × 10²² |
| `[v]`, `[H₀]`, `[d]` | dimensiones | — | L/T, 1/T, L |
| 1″ | segundo de arco | rad | π/648 000 = 4,848 × 10⁻⁶ |

## 10. Convenciones y referencias

El año luz depende de la convención del **año juliano** (365,25 d exactos, como en C01, C02 y C04); con otro año (trópico, sidéreo) el valor cambiaría en una parte en 10⁵. Para el parsec usamos la definición de la IAU como `(648 000/π) au`, que citamos de C02 y que **no reconsultamos** para esta clase; la comprobamos con la geometría. Las distancias de las galaxias son **estimadas**; las constantes, **definidas**; las conversiones, **calculadas**.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | BIPM, *The International System of Units (SI)*, 9.ª ed. (2019) | https://www.bipm.org/documents/20126/41483022/SI-Brochure-9.pdf | `Δν_Cs = 9 192 631 770 Hz`; `c = 299 792 458 m/s` | PDF leído (texto extraído) el 2026-11-05 |
| S2 | ídem | tabla de unidades no SI aceptadas | `1 au = 149 597 870 700 m` | PDF leído el 2026-11-05 |
| S3 | Mamajek, E. E. et al. (IAU Inter-Division A-G WG), *IAU 2015 Resolution B3*, arXiv:1510.07674 | https://arxiv.org/abs/1510.07674 | Define el au como unidad convencional de 149 597 870 700 m exactamente; valor nominal `R_⊙ = 6,957 × 10⁸ m` | Texto del PDF leído el 2026-11-05 |
| S4 | NASA NSSDC, *Sun Fact Sheet* (actualizada el 9-may-2024) | https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html | Distancia al Sol: media 149,6, mínima 147,1, máxima 152,1 (10⁶ km) | Página consultada el 2026-11-05 |
| S5 | BIPM, «SI base units» | https://www.bipm.org/en/measurement-units/si-base-units | Las siete unidades base del SI | Página consultada el 2026-11-05 (sin fecha propia; no se leyeron las definiciones allí) |

Límites: el parsec exacto de la IAU se cita de C02; los valores de ly y pc en metros son nuestro cálculo y se comprueban en el laboratorio.

## 12. Cómo ver la escalera

Versión accesible del diagrama:

| De → a | Factor | Valor |
|---|---|---|
| m → au | 1 au / 149 597 870 700 m | 6,684 × 10⁻¹² au/m |
| au → ly | 1 ly / 63 241,1 au | 1,5813 × 10⁻⁵ ly/au |
| ly → pc | 1 pc / 3,2616 ly | 0,30660 pc/ly |
| pc → Mpc | 1 Mpc / 10⁶ pc | 10⁻⁶ Mpc/pc |

Descripción larga: las cuatro conversiones forman una cadena de metros a megaparsecs; cada paso multiplica o divide por un factor definido. Si lo dibujas, usa escala logarítmica y etiqueta cada unidad con texto además de color.

## 13. Ejemplo trabajado: 43 Mpc en tres unidades y comprobación cruzada

**Paso 1 · Dato.** `d = 43 Mpc` (estimado; C01).

**Paso 2 · A metros.** `43 × 10⁶ × 3,0857 × 10¹⁶ = 1,3268 × 10²⁴ m`.

**Paso 3 · A años luz.** `1,3268 × 10²⁴ m ÷ 9,4607 × 10¹⁵ m/ly = 1,4025 × 10⁸ ly`.

**Paso 4 · A au.** `1,3268 × 10²⁴ ÷ 1,49598 × 10¹¹ = 8,869 × 10¹² au`.

**Paso 5 · Comprobación cruzada.** El tiempo de luz en años es igual a la distancia en años luz si se mide con el año juliano: 1,4025 × 10⁸ años. Y `d/c = 1,3268 × 10²⁴ m ÷ 2,998 × 10⁸ m/s = 4,426 × 10¹⁵ s`; dividido por `31 557 600 s/año` da `1,4025 × 10⁸` años: coincide.

**Paso 6 · Cifras.** Con dos cifras significativas: `1,3 × 10²⁴ m`, `1,4 × 10⁸ ly`, `8,9 × 10¹² au`.

**Sentido físico.** Las tres cifras son la misma distancia. Que la comprobación cruzada cierre indica que ninguna conversión tiene un error de potencia de diez, y es la misma disciplina que habría evitado el error de la sonda.

## 14. Distintas formas de convertir

**Factores que valen 1** (esta clase) es transparente y deja rastro. **Reglas de memoria** (1 pc ≈ 3,26 ly) son rápidas pero pierden cifras. **Software** (como el laboratorio) es reproducible, pero hereda errores si las constantes están mal. Usa memoria para estimar, factores para calcular y software para repetir, y verifica siempre con una comprobación cruzada.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Convierte 1 au a km y a años luz. *Pasos:* factores de la sección 8.

<details><summary>Solución comentada</summary>

`1 au = 149 597 870,7 km`; en ly, `1/63 241,1 = 1,5813 × 10⁻⁵ ly`. Si te salió 149 597 870 700 km, no cambiaste la unidad de metro a kilómetro.
</details>

**Ejercicio 2 · con una pista.** ¿A cuántos años luz equivale 1 pc? *Pista:* `1 pc = 3,0857 × 10¹⁶ m`; `1 ly = 9,4607 × 10¹⁵ m`.

<details><summary>Solución comentada</summary>

`3,0857 × 10¹⁶/9,4607 × 10¹⁵ = 3,2616 ly`. El parsec es algo más de tres años luz.
</details>

**Ejercicio 3 · casi autónomo.** Comprueba dimensionalmente `t = d/c` y `t = d·c`, con `d` en m y `c` en m/s.

<details><summary>Solución comentada</summary>

`d/c = m ÷ (m/s) = s`: correcta. `d·c = m²/s`: no es un tiempo; está mal.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Calcula `H₀ = 70 km/s/Mpc` en unidades de 1/s y luego `1/H₀` en años julianos.

<details><summary>Solución comentada</summary>

`1 Mpc = 3,0857 × 10¹⁹ km`; `H₀ = 70/3,0857 × 10¹⁹ = 2,268 × 10⁻¹⁸ s⁻¹`; `1/H₀ = 4,408 × 10¹⁷ s ÷ 31 557 600 = 1,397 × 10¹⁰ años` = 13,97 Gyr, igual que `977,8/70` de C01.
</details>

**Ejercicio 5.** La distancia media Tierra–Sol es 149,6 × 10⁶ km (S4). Exprésala en au y comprueba el resultado.

<details><summary>Solución comentada</summary>

`149,6 × 10⁶/149 597 870,7 = 1,0000` au: coincide con la definición, como era de esperar porque la unidad nació de ese valor.
</details>

**Ejercicio 6.** ¿Cuántas au hay en 1 pc? Comprueba que es `648 000/π`.

<details><summary>Solución comentada</summary>

`648 000/π = 206 264,8 au`, y de la sección 8.2, `3,0857 × 10¹⁶/1,49598 × 10¹¹ = 206 265`: coinciden.
</details>

**Ejercicio 7.** Neptuno está a 4 515 × 10⁶ km (C02). Exprésalo en au, en minutos luz y en parsecs.

<details><summary>Solución comentada</summary>

`4,515 × 10⁹ km/1,49598 × 10⁸ km/au = 30,18 au`; `4,515 × 10¹² m ÷ 2,998 × 10⁸ = 15 061 s = 251 min` (4,18 h); en pc, `30,18/206 265 = 1,463 × 10⁻⁴ pc`.
</details>

**Ejercicio 8.** Un estudiante escribe: «1 Mpc = 3,26 ly». Corrígelo y explica el error.

<details><summary>Solución comentada</summary>

`1 pc = 3,26 ly`; `1 Mpc = 3,26 × 10⁶ ly`. Se omitió el factor 10⁶: error de potencia de diez, típico con prefijos.
</details>

**Ejercicio 9 · transferencia.** Un dato dice «distancia: 8,6». ¿Qué falta? Usa 8,6 ly como ejemplo y calcula en m.

<details><summary>Solución comentada</summary>

Falta la unidad (y la fuente). Si son años luz: `8,6 × 9,4607 × 10¹⁵ = 8,1 × 10¹⁶ m`. Sin unidad el número no significa nada.
</details>

**Ejercicio 10 · transferencia.** Una fórmula propuesta: `E = m·c`. Detecta el error con análisis dimensional.

<details><summary>Solución comentada</summary>

`[m·c] = kg·m/s`, mientras que una energía es `kg·m²/s²`. La fórmula correcta de la que sale la dimensión es `E = m·c²`. El análisis detecta que falta un factor `c`.
</details>

**Ejercicio 11 · transferencia.** Usa el radio solar nominal `6,957 × 10⁸ m` (S3) para decir qué fracción de 1 au es.

<details><summary>Solución comentada</summary>

`6,957 × 10⁸/1,49598 × 10¹¹ = 0,00465`: el radio solar es el 0,47 % de 1 au; el Sol visto desde 1 au ocupa un ángulo de `2 × 0,00465 rad ≈ 0,53°`.
</details>

**Ejercicio 12 · integrador.** Elabora tu **hoja de conversiones verificada**: una tabla con las conversiones de la sección 12, cada factor con su valor, su origen (definido o calculado) y una comprobación cruzada; aplícala a una distancia publicada (con fuente) en tres unidades y verifica con el tiempo de luz.

<details><summary>Solución modelo</summary>

La hoja sigue la sección 13 con otra distancia; muestra factores como razones iguales a 1, comprobación `d/c`, cifras significativas coherentes y rótulo observado/estimado/calculado. Se acepta cualquier distancia con fuente citada.
</details>

## 17. Laboratorio: hoja de conversiones en 50 líneas

El script [conversiones_astronomicas.py](conversiones_astronomicas.py) calcula `ly` en metros (entero exacto), `pc` en au y en metros, el tiempo de luz de 1 au y las conversiones de 43 Mpc. Antes comprueba que `ly` coincide con el entero esperado, que `pc` coincide con la geometría `1 au/tan(1″)` dentro de `10⁻¹⁰` y que el tiempo de luz de 1 au es 499,0048 s; si no, se detiene.

**Datos:** constantes definidas (S1, S2) y distancia estimada de ejemplo. **Predice antes:** ¿cuántos años luz son 43 Mpc? (Cerca de 140 millones.) **Resultados (2026-11-05, Python 3.12.9, Windows):** `1 au = 149 597 870 700 m`, luz en 1 au = 499,0048 s (8,3167 min); `1 ly = 9 460 730 472 580 800 m` = 63 241,1 au; `1 pc = 3,085678 × 10¹⁶ m` = 206 264,806 au = 3,2616 ly; `43 Mpc = 1,3268 × 10²⁴ m = 1,4025 × 10⁸ ly = 8,8694 × 10¹² au`; radio solar nominal / 1 au = 0,00465.

```bash
python programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/conversiones_astronomicas.py
```

**Límites:** no propaga incertidumbres; los 43 Mpc son un ejemplo; el año juliano es una convención.

## 18. Errores frecuentes y cómo corregirlos

**Olvidar el prefijo.** «1 Mpc = 3,26 ly»: ejercicio 8.

**No cancelar unidades.** Se corrige con la sección 8.3 y el ejercicio 1.

**Dar cifras que la medida no sostiene.** Se corrige con la sección 8.5.

**Fórmulas con dimensiones incorrectas.** Ejercicios 3 y 10.

**Mezclar año juliano con trópico.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras 8.2: ¿puedes calcular `pc` en au sin mirar? Si no, ejercicio 6. Tras 8.3: ¿tus unidades se cancelan hasta dejar solo la deseada? Si no, ejercicio 1. Tras 8.4: ¿detectas el error en `E = m·c`? Si no, ejercicio 10. Al final: ¿qué comprobación cruzada usarías para una distancia en años luz? Si dudas, relee la sección 13.

## 20. Qué entregas y cómo se evalúa

El producto es tu **hoja de conversiones verificada**.

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Factores | Sin factores | Valores sueltos | Factores exactos con origen | Distingue definido de calculado |
| Conversión | Con errores | Con ayuda | Correcta con unidades | Con comprobación cruzada |
| Dimensiones | No revisa | Revisa una | Revisa todas | Detecta y corrige una fórmula errónea |
| Cifras | Excesivas | Inconsistentes | Coherentes | Justifica el redondeo |
| Fuentes | Sin cita | Sin fecha | Con fecha | Rotula estado de cada dato |

**Condiciones críticas:** toda cifra con unidad; no mezclar convenciones sin declararlas; citar solo lo consultado.

## 21. Ética, seguridad y límites

Convertir bien es una forma de responsabilidad: los errores de unidades han costado misiones reales (C04). Clase educativa; no sirve para operar naves. Accesibilidad: ecuaciones en texto, diagrama descrito, tablas equivalentes, sin conexión.

## 22. Para cerrar y seguir

Las unidades astronómicas son longitudes definidas o convenidas, y se convierten con factores que valen 1. El análisis dimensional y la comprobación cruzada atrapan la mayoría de los errores. Ahora que sabes expresar cantidades con rigor, falta preguntar cómo llega la información desde los objetos a tu instrumento: por la luz (C09).

**Glosario español–inglés.** unidad astronómica · *astronomical unit*; año luz · *light-year*; parsec · *parsec*; factor de conversión · *conversion factor*; análisis dimensional · *dimensional analysis*; cifras significativas · *significant figures*.

**Continuidad.** B01-C09 usa tu capacidad de **expresar y convertir longitudes, en particular longitudes de onda en nm**, para leer espectros. B01-C13 reutilizará la conversión en au para el modelo a escala.

**Referencias:** ver sección 11. S1 a S4 son datos oficiales consultados; S5 solo lista las unidades base.

<!-- nav:bottom -->
---

[← Anterior: B01-C07 — Hipótesis y predicciones falsables](../B01-C07-hipotesis-y-predicciones-falsables/CLASE.md) · [📚 Bloque B01](../../../tronco-comun/B01-el-universo-y-el-pensamiento-cientifico.md) · [Siguiente: B01-C09 — Luz como fuente de información →](../../../tronco-comun/B01-el-universo-y-el-pensamiento-cientifico.md#b01-c09)
<!-- /nav -->
