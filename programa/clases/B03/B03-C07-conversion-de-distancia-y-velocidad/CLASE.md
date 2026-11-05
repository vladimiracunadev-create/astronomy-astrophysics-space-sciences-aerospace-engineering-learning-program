# B03-C07 — Conversión de distancia y velocidad

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B03](../../../tronco-comun/B03-matematica-elemental-para-ciencias-espaciales.md) · [← Anterior: B03-C06 — Unidades del Sistema Internacional](../B03-C06-unidades-del-sistema-internacional/CLASE.md) · [Siguiente: B03-C08 — Tiempo y conversiones astronómicas →](../B03-C08-tiempo-y-conversiones-astronomicas/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Séptima clase del bloque B03. En C06 aprendiste que cada número lleva su unidad; aquí aprendes a **cambiar de unidad sin cambiar de cantidad**. Las agencias publican distancias en km, los programas calculan en m y los textos de divulgación hablan de au o de km/h. Pasar de una a otra sin error es una habilidad de uso diario. Nivel N0 → N1.

Verás el método de los factores de conversión (multiplicar por un cociente igual a 1), conversiones de longitud y de rapidez con unidades SI, unidades astronómicas y no SI aceptadas, y cómo comprobar el resultado. El tiempo y los ángulos se tratan en C08.

## 2. Por qué esta clase existe

Una cifra de la NASA como «velocidad de escape 11,186 km/s» no significa lo mismo para quien trabaja en m/s ni para quien piensa en km/h. Si conviertes mal, el error no es de redondeo sino de **factor**: mil, tres mil seiscientos. En C06 viste que un acuerdo de unidades perdió una sonda; esta clase te da la técnica para que tus conversiones se puedan auditar.

La decisión central es: **¿por qué factor multiplico, de modo que las unidades que no quiero se cancelen y la cantidad no cambie?** Aprenderás el método, sus pasos y sus comprobaciones.

## 3. Lo que podrás hacer al terminar

1. Expresar una equivalencia entre unidades como un factor igual a 1.
2. Convertir entre m, km y au, y entre m/s, km/s y km/h, anotando las unidades en cada paso.
3. Usar las equivalencias exactas del SI (1 au, 1 h, 1 km) y las de unidades aceptadas (milla náutica, nudo).
4. Calcular un tiempo de luz a partir de una distancia y comprobar el orden de magnitud.
5. Detectar un error de conversión por el tamaño del resultado y por las unidades que sobran.
6. Documentar una cadena de conversiones para que otra persona la audite.

La evidencia es la **hoja de conversiones verificada** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

Necesitas C01 a C06. Cinco preguntas:

1. ¿Cuántos metros hay en 3 km?
2. ¿Cuántos segundos hay en 2 h?
3. Si dividimos `km` entre `km`, ¿qué queda?
4. ¿Cuánto es `5 × 10³ m` en km?
5. ¿Qué es mayor, `1 km/s` o `1 km/h`?

<details>
<summary>Ver respuestas</summary>

1. 3 000 m. 2. 7 200 s. 3. Nada: es un número puro. 4. 5 km. 5. `1 km/s`: es 3 600 veces mayor.
</details>

Con cuatro o cinco aciertos, sigue; con menos, repasa C06.

## 5. Un caso real: tres cifras de la NASA en tres unidades

Las fichas de la NASA publican la velocidad orbital media de la Luna en 1,022 km/s, la de la Tierra en 29,78 km/s y la velocidad de escape terrestre en 11,186 km/s; el semieje de Neptuno aparece como 4 514,953 millones de km (S1). Una persona habla de «casi 11 mil metros por segundo» y otra de «unos 40 000 km/h» para lo mismo. Esta clase te permite pasar entre esas dos formas sin dudar y saber cuál usar. Límite: son valores medios publicados; la conversión no los mejora.

## 6. Vocabulario

Un **factor de conversión** es una razón de dos cantidades equivalentes, como `1 km / 1000 m`; vale 1 porque numerador y denominador son la misma cantidad. Una **equivalencia exacta** es una relación definida, sin incertidumbre (1 h = 3600 s). Una **unidad astronómica** (au) es una unidad de longitud con valor exacto 149 597 870 700 m (S2). Un **tiempo de luz** es la distancia dividida por `c = 299 792 458 m/s`. Un **nudo** es una milla náutica por hora, es decir, `1852/3600 m/s` (S2). **Cancelar unidades** es dividir una unidad entre sí misma para eliminarla del resultado.

## 7. Modelo mental: multiplicar por 1 con disfraz

Convertir no es cambiar la cantidad: es multiplicarla por un 1 escrito de manera conveniente.

```mermaid
flowchart LR
    A["Cantidad inicial: 11,186 km/s"] --> B["× (1000 m / 1 km): cancela km"]
    B --> C["× (3600 s / 1 h): cambia s por h"]
    C --> D["Resultado: 40 270 km/h tras ordenar los factores"]
    D --> E["Comprobación: unidades finales y orden de magnitud"]
```

*Descripción textual:* una cadena horizontal: se parte de 11,186 km/s, se multiplica por factores que valen 1 para cambiar cada unidad, se llega al resultado y se comprueba que las unidades sean las deseadas y que el tamaño sea razonable.

Analogía: cambiar billetes por monedas. El valor es el mismo, solo cambia la presentación. El límite: en dinero hay comisiones; en las conversiones de unidades definidas no hay pérdida, aunque sí puede haber redondeo si truncas cifras.

## 8. La explicación, paso a paso

### 8.1 Del cociente de equivalencia al factor

Si `1 km = 1000 m`, entonces `1000 m / 1 km = 1` y también `1 km / 1000 m = 1`. Ambos son factores válidos; eliges el que cancela la unidad que quieres quitar. Justificación: multiplicar por 1 no altera una cantidad.

### 8.2 Convertir una longitud

Para pasar `4 514,953 × 10⁶ km` a au: `1 au = 149 597 870,7 km` (porque `149 597 870 700 m / 1000`). Entonces `4 514,953 × 10⁶ km × (1 au / 149 597 870,7 km) = 30,1806 au`. Los km se cancelan. Estimación previa: `4,5 × 10⁹ / 1,5 × 10⁸ ≈ 30`.

### 8.3 Convertir una velocidad

Una velocidad es longitud entre tiempo; hay que convertir ambas unidades. `11,186 km/s × (3600 s / 1 h) = 40 269,6 km/h`: el segundo está abajo en el original, así que el factor lleva `s` arriba. Y para pasar a m/s, `11,186 km/s × (1000 m / 1 km) = 11 186 m/s`. Regla práctica: de km/h a m/s se divide entre 3,6; de m/s a km/h se multiplica por 3,6. Esa regla sale de `1000/3600`.

### 8.4 Unidades no SI aceptadas

El SI admite la hora, el día, la unidad astronómica, la milla náutica y el nudo (S2), cada una con equivalencia definida. Una embarcación que va a 15 nudos recorre `15 × 1852/3600 m/s = 7,717 m/s`. Se declaran siempre con su equivalencia.

### 8.5 Tiempo de luz como conversión

Dividir una distancia por `c` convierte metros en segundos: `149 597 870 700 m / 299 792 458 m/s = 499,005 s`. Para Neptuno, `4,514953 × 10¹² m / 2,99792 × 10⁸ m/s = 1,506 × 10⁴ s = 4,18 h`. Fíjate que el cociente `m / (m/s)` deja `s`.

### 8.6 Cómo comprobar una conversión

Tres pruebas: (1) ¿quedaron las unidades que querías?; (2) ¿el número creció o decreció en el sentido correcto?, porque una unidad más pequeña da un número mayor; (3) ¿convertir de vuelta recupera el valor inicial? Si las tres dan «sí», es muy probable que sea correcta.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor o nota |
|---|---|---|---|
| 1 au | unidad astronómica | m | 149 597 870 700 (exacto, S2) |
| `c` | velocidad de la luz | m/s | 299 792 458 (exacto, S2) |
| 1 h | hora | s | 3 600 (S2) |
| 1 d | día | s | 86 400 (S2) |
| 1 nudo | milla náutica por hora | m/s | 1852/3600 (S2) |
| `v` | rapidez | m/s, km/s, km/h | Luna 1,022; Tierra 29,78; escape 11,186 km/s (S1) |
| `a` | semieje mayor | 10⁶ km, au | Neptuno 4 514,953 (S1) |

## 10. Convenciones y referencias

Se escribe cada factor con sus unidades visibles y se tacha mentalmente lo que se cancela. Se conservan todas las cifras hasta el final y se redondea al terminar (C11). La coma separa decimales en el texto; el punto en el código. Se declara en cada resultado qué equivalencia se usó.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA NSSDC, fichas *Moon*, *Earth* y *Neptune* (act. 11-ene-2024, 15-nov-2024 y 3-oct-2024) | https://nssdc.gsfc.nasa.gov/planetary/factsheet/ | Velocidad orbital media de la Luna 1,022 km/s y de la Tierra 29,78 km/s; velocidad de escape terrestre 11,186 km/s; semieje de Neptuno 4 514,953 × 10⁶ km | Páginas consultadas el 2026-11-05 |
| S2 | BIPM, *The International System of Units (SI)*, 9.ª ed. (2019), tabla 8 y definiciones de segundo y metro | https://doi.org/10.59161/AUEZ1291 | 1 au = 149 597 870 700 m; 1 h = 3600 s; 1 d = 86 400 s; 1 milla náutica = 1852 m; nudo = (1852/3600) m/s; `c` = 299 792 458 m/s | PDF leído el 2026-11-05 |

Límites: son valores medios de fichas divulgativas. El año de 365,25 d usado en el ejercicio 9 es una convención del programa (año juliano), no una medición.

## 12. Cómo ver las equivalencias

Versión accesible de una tabla de cambio.

| De | A | Operación | Ejemplo |
|---|---|---|---|
| km/s | m/s | × 1000 | 1,022 → 1 022 |
| km/s | km/h | × 3600 | 29,78 → 107 208 |
| km/h | m/s | ÷ 3,6 | 36 → 10 |
| km | au | ÷ 149 597 870,7 | 4,515 × 10⁹ → 30,18 |
| m | s (luz) | ÷ 299 792 458 | 1 au → 499,005 s |

Si la dibujas, usa flechas rotuladas con el factor y distingue las magnitudes por forma. Descripción larga: dos columnas de unidades de longitud y de rapidez conectadas por factores; cada flecha lleva el factor y su sentido inverso.

## 13. Ejemplo trabajado: la Tierra y Neptuno en tres unidades

**Pregunta.** La NASA da la rapidez orbital media de la Tierra como 29,78 km/s. Exprésala en m/s, km/h y au/día; y calcula cuánto tarda la luz en llegar a Neptuno.

**Paso 1 · m/s.** `29,78 km/s × 1000 m/km = 29 780 m/s`.
**Paso 2 · km/h.** `29,78 × 3600 = 107 208 km/h`.
**Paso 3 · au/día.** `29,78 km/s × 86 400 s/d = 2 572 992 km/d`; dividir entre `149 597 870,7 km/au`: `0,01720 au/d`.
**Paso 4 · comprobación.** En un año de 365,256 d recorre `0,0172 × 365,256 = 6,28 au ≈ 2π` au: coherente con una órbita de radio 1 au.
**Paso 5 · luz a Neptuno.** `30,1806 au × 499,005 s/au = 15 060 s = 4,18 h`.
**Sentido físico.** Una señal a Neptuno tarda más de cuatro horas: no hay conversación en tiempo real con una sonda allí; el «retardo» no es un fallo del equipo.

## 14. Dos métodos de conversión y cuándo fallan

El **método de factores** es largo pero deja rastro y funciona con cualquier unidad. La **regla rápida** (×3,6 o ÷3,6) es corta pero se invierte con facilidad. Un **programa** elimina el trabajo manual, pero hereda el factor que le des. Para una cadena larga, escribe los factores; para un caso suelto, usa la regla rápida y comprueba con la estimación (8.6). Los tres fallan si el factor de partida está mal.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Expresa 1 au en km. *Pasos:* `1 au = 149 597 870 700 m`; `1 km = 1000 m` (S2).

<details><summary>Solución comentada</summary>

`149 597 870 700 m × (1 km / 1000 m) = 149 597 870,7 km ≈ 1,496 × 10⁸ km`. Los m se cancelan.
</details>

**Ejercicio 2 · con una pista.** Convierte 36 km/h a m/s. *Pista:* divide entre 3,6.

<details><summary>Solución comentada</summary>

`36 / 3,6 = 10 m/s`. Con factores: `36 × 1000 / 3600 = 10`.
</details>

**Ejercicio 3 · casi autónomo.** Convierte la velocidad de escape terrestre, 11,186 km/s, a km/h.

<details><summary>Solución comentada</summary>

`11,186 × 3600 = 40 269,6 km/h ≈ 4,03 × 10⁴ km/h`. Debe ser mayor que el número en km/s porque la hora es más larga que el segundo.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Convierte 1,022 km/s (Luna) a km/h y a m/s.

<details><summary>Solución comentada</summary>

`1,022 × 3600 = 3 679,2 km/h`; `1,022 × 1000 = 1 022 m/s`.
</details>

**Ejercicio 5.** Pasa el semieje de Neptuno, `4 514,953 × 10⁶ km`, a au y comprueba con una estimación.

<details><summary>Solución comentada</summary>

`4,514953 × 10⁹ km ÷ 149 597 870,7 km/au = 30,181 au`. Estimación `4,5 × 10⁹ / 1,5 × 10⁸ = 30`. ✓
</details>

**Ejercicio 6.** Convierte 1 au/día a km/s.

<details><summary>Solución comentada</summary>

`149 597 870,7 km / 86 400 s = 1 731,46 km/s`. Es una rapidez enorme comparada con la de un planeta, pero sigue siendo el 0,58 % de la de la luz (299 792 km/s).
</details>

**Ejercicio 7.** Un barco avanza a 15 nudos. Exprésalo en m/s y en km/h (S2).

<details><summary>Solución comentada</summary>

`15 × 1852/3600 = 7,717 m/s`; en km/h, `15 × 1,852 = 27,78 km/h`.
</details>

**Ejercicio 8.** Un estudiante convierte `36 km/h` a m/s multiplicando por 3,6 y obtiene `129,6`. ¿Cómo lo detectas?

<details><summary>Solución comentada</summary>

Un automóvil a 36 km/h no va a 130 m/s (más de 460 km/h). La prueba de sentido (8.6) la rechaza. Debió dividir: `36/3,6 = 10 m/s`.
</details>

**Ejercicio 9 · transferencia.** Un año luz es la distancia que recorre la luz en un año de 365,25 días (convención). Calcúlalo en metros y en au.

<details><summary>Solución comentada</summary>

`299 792 458 m/s × 365,25 d × 86 400 s/d = 9,4607 × 10¹⁵ m`; dividido entre `1,495978707 × 10¹¹ m/au` da `63 241 au`. Una conversión encadenada con tres factores.
</details>

**Ejercicio 10 · transferencia.** Una sonda hipotética viaja a 17 km/s constantes (valor ilustrativo). ¿Cuánto tarda en cruzar `30,18 au`, en años de 365,25 d?

<details><summary>Solución comentada</summary>

`30,18 au = 4,515 × 10⁹ km`; `÷ 17 km/s = 2,656 × 10⁸ s`; `÷ (365,25 × 86 400 s) = 8,4 años`. Es un modelo grueso (sin gravedad ni trayectoria real).
</details>

**Ejercicio 11 · transferencia.** Comprueba que 29,78 km/s sostenidos durante un año de 365,256 d recorren una longitud cercana a la circunferencia de una órbita de radio 149,598 × 10⁶ km. Da la diferencia relativa.

<details><summary>Solución comentada</summary>

Distancia `29,78 × 365,256 × 86 400 = 9,398 × 10⁸ km`; circunferencia `2π × 149,598 × 10⁶ = 9,400 × 10⁸ km`. Diferencia relativa ≈ 0,02 %. La rapidez publicada y el semieje y período son consistentes entre sí.
</details>

**Ejercicio 12 · integrador.** Elabora tu *hoja de conversiones verificada* (sección 20): cinco cantidades astronómicas con datos citados, cada una convertida a dos unidades con los factores escritos, las tres pruebas de 8.6 y la fuente.

<details><summary>Solución modelo</summary>

Ejemplo de filas: Tierra 29,78 km/s → 107 208 km/h; Luna 1,022 km/s → 1 022 m/s; Neptuno 4 514,953 × 10⁶ km → 30,181 au; 1 au → 499,005 s de luz; escape 11,186 km/s → 40 270 km/h. Cada una con factores, prueba de sentido, ida y vuelta y S1/S2.
</details>

## 17. Laboratorio: conversiones auditables

El script [laboratorio_conversiones.py](laboratorio_conversiones.py) define los factores exactos y las conversiones de la sección 8, y comprueba antes de imprimir que la ida y vuelta km↔au recupera el valor, que 36 km/h son 10 m/s y que 1 au/`c` = 499,0048 s.

**Datos:** factores exactos del SI y valores publicados (NASA). **Predice antes de ejecutar:** ¿cuántas horas tarda la luz en llegar a Neptuno? (Algo más de cuatro.) **Resultados (2026-11-05, Python 3.12.9):** 1 au/c = 499,005 s; Neptuno a 30,1806 au, luz en 15 060 s = 4,18 h; Luna 1,022 km/s = 3 679 km/h; Tierra 29,78 km/s = 107 208 km/h; escape 11,186 km/s = 40 270 km/h; Tierra 0,01720 au/día.

```bash
python programa/clases/B03/B03-C07-conversion-de-distancia-y-velocidad/laboratorio_conversiones.py
```

**Límites:** solo aritmética de factores; no maneja incertidumbre ni escalas de tiempo.

## 18. Errores frecuentes y cómo corregirlos

**Multiplicar cuando había que dividir.** Ejercicio 8.
**Convertir solo una de las dos unidades de una velocidad.** Ejercicio 3.
**Redondear el factor.** Usar 150 millones de km por au distorsiona la tercera cifra. Ejercicio 5.
**Mezclar prefijos.** Ejercicio 1.
**No comprobar el sentido.** Sección 8.6.

## 19. Cómo sabrás que vas bien

Tras 8.1: ¿puedes escribir los dos factores posibles entre km y m? Si no, repite el ejercicio 1. Tras 8.3: ¿conviertes km/s a km/h sin dudar del factor? Si no, haz el 3. Tras 8.6: ¿ejecutas las tres pruebas por reflejo? Si no, vuelve al 8. Al final: ¿sabes escribir una cadena de tres factores? Si dudas, rehaz el 9.

## 20. Qué entregas y cómo se evalúa

El producto es tu **hoja de conversiones verificada**: cinco cantidades convertidas con factores a la vista, pruebas de sentido, ida y vuelta, y fuente.

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Factores | Sin factor escrito | Algunos | Todos escritos | Cadena de más de dos |
| Unidades | Se pierden | Algunas | En cada paso | Detecta un error ajeno |
| Verificación | Ninguna | Una prueba | Las tres | Las automatiza |
| Fuente | Sin cita | Parcial | Completa | Distingue exacto de medido |
| Claridad | Confusa | Entendible | Reproducible | Autoevaluada |

**Condiciones críticas:** no omitir unidades; no truncar los factores exactos; citar solo fuentes consultadas.

## 21. Ética, seguridad y límites

Un factor de conversión equivocado es un error silencioso: parece un número normal. Mostrar los factores permite que otros lo detecten. Esta clase es educativa y no sirve para operar sistemas de navegación. Accesibilidad: factores en texto, tablas equivalentes, sin conexión.

## 22. Para cerrar y seguir

Convertir es multiplicar por factores iguales a 1; una velocidad exige convertir longitud y tiempo; el tiempo de luz es una conversión de distancia en segundos; y tres pruebas (unidades, sentido, ida y vuelta) detectan casi todos los errores. Queda una pregunta: el tiempo y los ángulos tienen unidades con base sesenta o con convenciones históricas. ¿Cómo convertirlos? Es C08.

**Glosario español–inglés.** factor de conversión · *conversion factor*; unidad astronómica · *astronomical unit*; tiempo de luz · *light-travel time*; nudo · *knot*; milla náutica · *nautical mile*; rapidez · *speed*.

**Continuidad.** B03-C08 aplica el mismo método a tiempos y ángulos. B03-C14 lo usa al despejar variables y B03-C20 al construir la maqueta a escala.

**Referencias:** ver sección 11. Todas las fuentes son datos oficiales consultados.

<!-- nav:bottom -->
---

[← Anterior: B03-C06 — Unidades del Sistema Internacional](../B03-C06-unidades-del-sistema-internacional/CLASE.md) · [📚 Bloque B03](../../../tronco-comun/B03-matematica-elemental-para-ciencias-espaciales.md) · [Siguiente: B03-C08 — Tiempo y conversiones astronómicas →](../B03-C08-tiempo-y-conversiones-astronomicas/CLASE.md)
<!-- /nav -->
