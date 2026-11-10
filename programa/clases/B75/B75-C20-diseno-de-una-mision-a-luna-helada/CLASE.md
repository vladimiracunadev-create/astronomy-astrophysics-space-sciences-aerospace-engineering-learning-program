# B75-C20 — Diseño de una misión a luna helada

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B75](../../../tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md) · [← Anterior: B75-C19 — Restricciones de navegación autónoma](../B75-C19-restricciones-de-navegacion-autonoma/CLASE.md) · [Siguiente: B75-C21 — Intersección de cónicas en transferencias →](../B75-C21-interseccion-de-conicas-en-transferencias/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 20 del bloque B75. Nivel N3. Esta clase reúne el bloque: salida de la Tierra, tránsito a Júpiter, captura joviana y llegada a una luna helada, con el presupuesto de delta-v y la masa de cada fase. El destino de ejemplo es Europa. No es una réplica de ninguna misión: es un esbozo preliminar de cónicas empalmadas, con el tour de lunas reducido a un delta-v sintético, que se contrasta con los datos de las misiones consultados en las páginas de la NASA y de la ESA.

## 2. Por qué esta clase existe

Antes de diseñar una misión hay que saber si es viable y qué la hace cara. La decisión central: **¿cuánto delta-v y cuánta masa cuesta ir de la Tierra a una luna de Júpiter, y cuánto se ahorra con una misión de sobrevuelos en lugar de un orbitador?**

## 3. Lo que podrás hacer al terminar

1. Calcular las fases del tránsito: salida, captura joviana e inserción en la órbita de la luna.
2. Calcular el `C3`, los `v∞` y el tiempo de vuelo del Hohmann a Júpiter.
3. Calcular una captura en una elipse de 60 d y el delta-v correspondiente.
4. Armar dos presupuestos (orbitador y sobrevuelos) con margen y masa de propulsante.
5. Contrastar el tránsito del modelo con los datos de la NASA y la ESA consultados.
6. Separar lo consultado, lo calculado y lo sintético (y señalar lo que no se calculó: el tour).

La evidencia es tu **esbozo de misión a Europa en el modelo** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es el `C3`?
2. ¿Qué es una captura en elipse?
3. ¿Qué es un tour de lunas?
4. ¿Qué dice la ecuación del cohete?
5. ¿Qué es un margen de diseño?

<details>
<summary>Ver respuestas</summary>

1. `v∞²` de salida en km²/s² (B75-C23). 2. Un impulso en el periapsis que convierte la hipérbola en una elipse (B75-C14). 3. Una secuencia de sobrevuelos de lunas que modifica la órbita joviana (B75-C26). 4. `m₀/m_f = e^{Δv/(I_sp g₀)}` (B75-C09). 5. Un delta-v adicional por incertidumbre.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Un tránsito de Hohmann a Júpiter dura `997,7 d` (2,73 años) con `C3 = 77,32 km²/s²` y llega con `v∞ = 5,6433 km/s`. Capturarse en una elipse de 60 d con periapsis a `9,5 R_J` cuesta `1,5647 km/s`; insertarse en una órbita circular de 100 km de Europa con `v∞ = 1,5 km/s` (sintético) cuesta `1,0825 km/s`. Es el **ejemplo conductor**. La página de la NASA indica que Europa Clipper se lanzó el 14 de octubre de 2024, llega a Júpiter en abril de 2030 (unos 5,5 años) y hará 49 sobrevuelos de Europa [S5]; la ficha de la ESA dice que Juice se lanzó el 14 de abril de 2023, llega a Júpiter en julio de 2031 y termina en órbita de Ganimedes [S6].

## 6. Vocabulario

Un **orbitador** se inserta en órbita alrededor de la luna; una **misión de sobrevuelos** no. El **tour** es la fase entre la captura joviana y la luna. El **esbozo preliminar** es un diseño de cónicas empalmadas sin efemérides. La **razón de masa** es `m₀/m_f`.

## 7. Modelo mental: un viaje en tres etapas

```mermaid
flowchart LR
    L["Salida LEO: C3, dv_dep"] --> T["Transito: Hohmann 2.73 anios"]
    T --> J["Captura en Jupiter: elipse de 60 d"]
    J --> U["Tour de lunas (sintetico 0.30 km/s)"]
    U --> E["Europa: sobrevuelos u orbita (dv_EOI)"]
    E --> M["presupuesto + margen -> masa"]
```

*Descripción textual:* Cuatro tramos (salida, tránsito, captura joviana, luna) alimentan un presupuesto de delta-v; el margen y la ecuación del cohete dan la masa.

Analogía: una escalera de cuatro peldaños de distinta altura: el peldaño de salida es el más alto. Límite: la escalera real tiene más peldaños (asistencias gravitacionales) y el tour no se calcula aquí.

## 8. La explicación, paso a paso

### 8.1 Tránsito y captura

Con los semiejes y masas de las fichas [S1, S2]: Hohmann a Júpiter, `v∞,sal = 8,7933 km/s`, `C3 = 77,32 km²/s²`, `v∞,lleg = 5,6433 km/s`, `997,7 d`. Salida desde 300 km: `Δv = 6,2995 km/s`. Captura en Júpiter con periapsis `9,5 R_J = 679 174 km` y periodo de 60 d (`a = 4 418 084 km`, apoapsis `8 156 994 km = 114,1 R_J`): `Δv = 1,5647 km/s`.

### 8.2 Europa

Con `GM = 3202,7121 km³/s²` y `R = 1560,80 km` [S4], órbita circular de 100 km (`v_c = 1,3887 km/s`, periodo `125,24 min`) y `v∞ = 1,5 km/s` sintético: `Δv_EOI = 1,0825 km/s`.

### 8.3 Dos presupuestos

| Fase | Orbitador (km/s) | Sobrevuelos (km/s) |
|---|---|---|
| Salida desde 300 km | 6,2995 | 6,2995 |
| Correcciones y tour (sintético) | 0,3000 | 0,3000 |
| Captura en Júpiter (60 d) | 1,5647 | 1,5647 |
| Inserción en órbita de Europa | 1,0825 | — |
| **Determinista** | **9,2467** | **8,1642** |
| Con margen 10 % | 10,1714 | 8,9806 |
| Masa inicial (`m_f = 1000 kg`, `I_sp = 320 s`) | 25 565 kg | 17 492 kg |

La inserción orbital añade un `13 %` al determinista y un `46 %` a la masa inicial. El orbitador pide una razón de masa de `25,6`; esas cifras de una etapa con `I_sp = 320 s` son ilustrativas, no realistas.

### 8.4 Contraste con las misiones consultadas

El Hohmann directo dura `2,73` años; Europa Clipper tarda unos 5,5 años desde su lanzamiento hasta Júpiter según la página de la NASA, y Juice unos 8,2 años (abril 2023–julio 2031) según la ESA [S5, S6]. Ambas usan asistencias gravitacionales, de las que las páginas solo dan detalles parciales (Marte y Tierra para Clipper; Luna–Tierra, Venus y Tierra para Juice). El menor `C3` que permite una trayectoria con asistencias, a cambio de tiempo, es el compromiso de C27.

### 8.5 Verificaciones

El producto de razones de masa por fase coincide con la razón del total (error `10⁻¹²`); la elipse de captura de 60 d, propagada medio periodo con Kepler, llega a `8 156 994,1 km` como esperado; la órbita de Europa de 100 km tiene un periodo de `125,24 min` y la nave vuelve a su posición inicial tras un periodo.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `C3` | energía característica de salida | km²/s² | 77,32 |
| `Δv_dep` | salida desde 300 km | km/s | 6,2995 |
| `Δv_JOI` | captura en Júpiter | km/s | 1,5647 |
| `Δv_EOI` | inserción en Europa | km/s | 1,0825 (v∞ sintético) |
| `m₀` | masa inicial | kg | 25 565 (orbitador) |
| `TOF` | tiempo de vuelo del Hohmann | años | 2,73 |

## 10. Convenciones y referencias

Cónicas empalmadas, órbitas planetarias circulares y coplanares; fichas NASA/NSSDC y tablas del JPL; `G` del JPL; `μ☉`, `g₀` estándar. Sintéticos: `v∞` en Europa, delta-v de tour y correcciones, periodo de 60 d y periapsis de captura, `I_sp`, masa final, margen. El tour de lunas no se calcula (C26).

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA/NSSDC, Earth Fact Sheet — https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html (consultada 2026-11-10) | página leída | semieje 149,598×10⁶ km, periodo sideral 365,256 d, excentricidad 0,0167, velocidad orbital media 29,78 km/s, masa 5,9722×10²⁴ kg, radio medio 6371,000 km, velocidad de escape 11,186 km/s | Consultada |
| S2 | NASA/NSSDC, Jupiter Fact Sheet — https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html (consultada 2026-11-10) | página leída | semieje 778,479×10⁶ km, periodo sideral 4332,589 d, excentricidad 0,0487, inclinación 1,304°, velocidad media 13,06 km/s, masa 1898,13×10²⁴ kg, radio medio 69 911 km | Consultada |
| S3 | NASA JPL SSD, Planetary Physical Parameters — https://ssd.jpl.nasa.gov/planets/phys_par.html (consultada 2026-11-10) | página leída | radios ecuatoriales (Venus 6051,8 km; Tierra 6378,1366 km; Marte 3396,19 km; Júpiter 71 492 km) y la constante G = 6,67430×10⁻¹¹ m³ kg⁻¹ s⁻² citada en su registro de cambios. La página no lista GM: aquí GM = G·M con las masas de las fichas NSSDC | Consultada |
| S4 | NASA JPL SSD, Planetary Satellite Physical Parameters — https://ssd.jpl.nasa.gov/sats/phys_par/ (consultada 2026-11-10) | página leída | GM (km³/s²) y radio medio (km): Ío 5959,91547 y 1821,49; Europa 3202,71210 y 1560,80; Ganimedes 9887,83275 y 2631,20; Calisto 7179,28340 y 2410,30; Titán 8978,13710 y 2574,76; Encélado 7,21037 y 252,10 | Consultada |
| S5 | NASA, Europa Clipper (página de la misión) — https://science.nasa.gov/mission/europa-clipper/ (consultada 2026-11-10) | página leída | lanzamiento el 14 de octubre de 2024 en Falcon Heavy; sobrevuelo de Marte en 2025 y de la Tierra el 3 de diciembre de 2026; llegada a Júpiter en abril de 2030; 49 sobrevuelos cercanos de Europa; unos 2,9 mil millones de km hasta Júpiter | Consultada |
| S6 | ESA, Juice factsheet — https://www.esa.int/Science_Exploration/Space_Science/Juice/Juice_factsheet (consultada 2026-11-10) | página leída | lanzamiento el 14 de abril de 2023 en Ariane 5 desde Kourou; asistencias de la Luna–Tierra, Venus y la Tierra; llegada a Júpiter en julio de 2031; tour que termina en órbita de Ganimedes | Consultada |
| — | Valores estándar (no consultados en una fuente concreta de esta clase) | — | GM☉ = 1,32712440×10¹¹ km³/s² (valor estándar, ver la resolución IAU 2015 B3 de la fila anterior donde se cita); 1 au = 149 597 870,7 km; c = 299 792,458 km/s; g₀ = 9,80665 m/s²; ecuaciones de dos cuerpos | No consultada en una fuente concreta |

Límites: no se consultó ninguna trayectoria real; las páginas de la NASA y de la ESA solo dan fechas y asistencias parciales; el delta-v del tour y el `v∞` en Europa no tienen respaldo; la radiación de Júpiter no se evalúa (C28).

## 12. Cómo ver el presupuesto

| Fase | Δv (km/s) |
|---|---|
| Salida | 6,2995 |
| Correcciones y tour | 0,3000 |
| Captura joviana | 1,5647 |
| Inserción en Europa | 1,0825 |
| Total determinista (orbitador) | 9,2467 |

Descripción larga: más de dos tercios del determinista se gastan en la salida de la Tierra; la inserción orbital en la luna cuesta algo más que la mitad de la captura joviana.

## 13. Ejemplo trabajado: la inserción en Europa

**Paso 1 · Radio.** `r = 1560,80 + 100 = 1660,80 km`.

**Paso 2 · Velocidad hiperbólica.** `√(1,5² + 2×3202,71/1660,80) = 2,4712 km/s`.

**Paso 3 · Velocidad circular.** `√(3202,71/1660,80) = 1,3887 km/s`.

**Paso 4 · Delta-v.** `1,0825 km/s`.

## 14. Distintas formas de abordar el problema

**Orbitador:** inserción en la luna. **Misión de sobrevuelos:** sin inserción, más ciencia por pasada (C17). **Con asistencias:** menor `C3`, más tiempo. **Con propulsión de bajo empuje:** `I_sp` alta, más tiempo (C11).

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `C3` de salida a Júpiter. *Pasos:* `v∞²` con `v∞ = 8,7933`.

<details><summary>Solución comentada</summary>

`77,32 km²/s²`.
</details>

**Ejercicio 2 · con una pista.** Calcula el tiempo de vuelo en años. *Pista:* `997,7 d`.

<details><summary>Solución comentada</summary>

`997,7/365,256 = 2,73` años.
</details>

**Ejercicio 3 · casi autónomo.** Suma las fases del orbitador y aplica el margen del 10 %. *Pista:* ver la tabla 8.3.

<details><summary>Solución comentada</summary>

`9,2467×1,10 = 10,1714 km/s`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** ¿Qué porcentaje del determinista es la salida?

<details><summary>Solución comentada</summary>

`6,2995/9,2467 = 68,1 %`.
</details>

**Ejercicio 5 · autónomo.** ¿Cuánto añade la inserción en Europa a la masa inicial?

<details><summary>Solución comentada</summary>

`25 565 − 17 492 = 8073 kg` (46 %).
</details>

**Ejercicio 6 · autónomo.** Calcula `v_c` de una órbita de 100 km de Europa.

<details><summary>Solución comentada</summary>

`√(3202,71/1660,8) = 1,3887 km/s`.
</details>

**Ejercicio 7 · autónomo.** Compara el tránsito de Hohmann con el de Clipper (unos 5,5 años).

<details><summary>Solución comentada</summary>

`5,5/2,73 = 2,0` veces más lento.
</details>

**Ejercicio 8 · autónomo.** ¿Cuántos años median entre el lanzamiento de Juice (abril 2023) y su llegada a Júpiter (julio 2031)?

<details><summary>Solución comentada</summary>

Unos `8,25` años.
</details>

**Ejercicio 9 · transferencia.** Una misión de sobrevuelos de Europa (como Clipper) evita la inserción orbital. ¿Qué ahorra y qué pierde?

<details><summary>Solución comentada</summary>

Ahorra `1,08 km/s` (46 % de masa en el ejemplo); pierde el tiempo continuo de observación, pero gana pasadas repetidas.
</details>

**Ejercicio 10 · transferencia.** ¿Por qué las misiones reales tardan más que el Hohmann (2,73 años)?

<details><summary>Solución comentada</summary>

Porque usan asistencias gravitacionales para bajar `C3` y así ahorrar masa de lanzamiento (C06, C27).
</details>

**Ejercicio 11 · transferencia.** El tour se supuso de `0,30 km/s`. ¿Cómo cambia el resultado si fuera `0,60 km/s`?

<details><summary>Solución comentada</summary>

Sube el determinista a `9,5467 km/s`; la masa a `1000·exp(9,5467×1,10/3,1381) = 28 400 kg` (+2835 kg).
</details>

**Ejercicio 12 · integrador.** Elabora tu *esbozo de misión a Europa en el modelo*: fases, `C3`, tiempo, captura, inserción, dos presupuestos con margen, masa y lista de qué es consultado, calculado y sintético.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.5 y la salida del laboratorio.
</details>

## 17. Laboratorio: esbozo de misión a Europa

El script [mision_europa.py](mision_europa.py) calcula las fases, los dos presupuestos y las masas, y **comprueba** el producto de razones de masa, la elipse de captura por Kepler y el periodo de la órbita de Europa.

**Datos:** masas, semiejes y radios de fichas NASA/NSSDC y JPL, `GM` de Europa (consultados); datos de misiones de las páginas NASA y ESA (consultadas); el resto **sintético**. **Predice antes de ejecutar:** ¿Cuánto añade la inserción en Europa a la masa inicial? (unos 8 t, 46 %.) **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Hohmann Tierra-Jupiter: TOF = 997.7 d (2.73 anios) ; v_inf salida = 8.7933 km/s (C3 = 77.32 km2/s2) ; v_inf llegada = 5.6433 km/s
Captura joviana: rp = 679174 km (9.5 R_J) ; periodo 60 d -> a = 4418084 km, ra = 8156994 km (114.1 R_J)
Europa: v_inf = 1.5 km/s (SINTETICO) ; orbita circular de 100 km: v_c = 1.3887 km/s

Orbitador de Europa:
   Salida desde 300 km                          6.2995 km/s
   Correcciones y tour (sintetico)              0.3000 km/s
   Captura en Jupiter (60 d)                    1.5647 km/s
   Insercion en orbita de Europa (100 km)       1.0825 km/s
   determinista = 9.2467 km/s ; con margen 10 % = 10.1714 km/s ; masa inicial (m_f = 1000 kg, Isp = 320 s) = 25565 kg ; razon m0/mf = 25.6

Misiones de sobrevuelos (sin insercion en Europa):
   Salida desde 300 km                          6.2995 km/s
   Correcciones y tour (sintetico)              0.3000 km/s
   Captura en Jupiter (60 d)                    1.5647 km/s
   determinista = 8.1642 km/s ; con margen 10 % = 8.9806 km/s ; masa inicial (m_f = 1000 kg, Isp = 320 s) = 17492 kg ; razon m0/mf = 17.5

Comparacion con la pagina de Europa Clipper (consultada): lanzamiento 2024-10-14, llegada a Jupiter en abril de 2030 (unos 5.5 anios), 49 sobrevuelos de Europa.
El Hohmann del modelo dura 2.73 anios: la ruta real es mas larga (usa asistencias gravitacionales; su detalle no se consulto).
Prueba 2: apoapsis de la elipse de 60 d por Kepler (medio periodo) = 8156994.1 km ; esperado 8156994.1 km
Prueba 3: periodo de la orbita circular de Europa de 100 km = 125.24 min ; tras un periodo la nave vuelve a (1660.800000, 0.000000) km
Pruebas superadas.
```

```bash
python programa/clases/B75/B75-C20-diseno-de-una-mision-a-luna-helada/mision_europa.py
```

**Límites:** sin tour, sin asistencias, una sola etapa, sin radiación; las cifras de masa no son realistas.

## 18. Errores frecuentes y cómo corregirlos

**Dar por buena la masa de una sola etapa.** Se corrige con 8.3.

**Olvidar que el tour no se calculó.** Se corrige con la sección 11.

**Comparar el Hohmann con las misiones reales sin las asistencias.** Se corrige con 8.4.

**Presentar el esbozo como el diseño de una misión.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras 8.3: ¿qué fase domina? Tras el laboratorio: ¿qué tres pruebas pasó? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **esbozo de misión a Europa en el modelo** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Confunde fases | Define las fases | Arma ambos presupuestos | Explica el compromiso orbitador–sobrevuelos |
| Cálculo | Sin unidades | Con errores | Tablas completas | Calcula variantes |
| Numérico | Sin comprobar | Una prueba | Tres pruebas | Interpreta los límites |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Distingue consultado, calculado y sintético |
| Límites | No los nombra | Uno | Tres | Discute tour, asistencias y radiación |

**Condiciones críticas (no se compensan con promedio):** rotular lo sintético y el tour no calculado; no presentar el esbozo como una misión real; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados (órbitas planetarias circulares y coplanares, dos cuerpos) y sus datos son consultados, sintéticos o ilustrativos y están rotulados; ningún resultado es una efeméride, una medición ni un diseño de misión real. Un diseño de misión real exige revisión formal, análisis de radiación, de protección planetaria y de riesgo; esta clase no los cubre. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

En el modelo, un orbitador de Europa gasta `9,2467 km/s` y una misión de sobrevuelos `8,1642 km/s`, y las misiones reales consultadas tardan 5,5 y 8,2 años frente a los 2,73 del Hohmann. Queda abierto el bloque de ampliación: intersección de cónicas, `C3`, plano B, resonancias, tours, tiempo, radiación y *pork-chop*.

**Glosario español–inglés.** orbitador · *orbiter*; misión de sobrevuelos · *flyby mission*; tour · *tour*; inserción en órbita · *orbit insertion*; luna helada · *icy moon*.

**Continuidad.** [B75-C21](../B75-C21-interseccion-de-conicas-en-transferencias/CLASE.md) abre la ampliación con la intersección de cónicas.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B75-C19 — Restricciones de navegación autónoma](../B75-C19-restricciones-de-navegacion-autonoma/CLASE.md) · [📚 Bloque B75](../../../tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md) · [Siguiente: B75-C21 — Intersección de cónicas en transferencias →](../B75-C21-interseccion-de-conicas-en-transferencias/CLASE.md)
<!-- /nav -->
