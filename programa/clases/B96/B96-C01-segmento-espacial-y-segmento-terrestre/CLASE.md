# B96-C01 — Segmento espacial y segmento terrestre

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B96](../../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) · [← Anterior: B95-C04 — Antenas desplegables para satélites pequeños](../../B95/B95-C04-antenas-desplegables-para-satelites-pequenos/CLASE.md) · [Siguiente: B96-C02 — Concepto de operaciones de misión →](../B96-C02-concepto-de-operaciones-de-mision/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 1 del bloque B96. Nivel N3. Una misión tiene un **segmento espacial** (la nave y su carga útil) y un **segmento terrestre** (estaciones, centro de control, centro de datos y las redes que los unen). Aquí aprendes a describir su relación con tres números: la **distancia**, el **retardo de propagación** y el **volumen de datos** que cabe en una pasada. Los valores son redondeados y **sintéticos**; no usan efemérides reales. Todos los datos son **sintéticos** salvo los que se rotulan como consultados.

## 2. Por qué esta clase existe

Quien opera una nave no puede tratarla como un equipo de laboratorio: cada comando viaja a la velocidad de la luz y cada contacto dura minutos. La decisión central: **¿qué segmento hace qué y cuánto tardan en comunicarse?**

## 3. Lo que podrás hacer al terminar

1. Distinguir las funciones del segmento espacial y del terrestre.
2. Calcular el retardo de propagación y el de ida y vuelta para LEO, GEO, la Luna y Marte.
3. Obtener el rango oblicuo de una estación a una elevación dada y comprobarlo por dos vías.
4. Calcular el volumen de datos de una pasada a una tasa dada.
5. Calcular un ciclo comando–respuesta con tiempos de proceso y de operador.
6. Separar lo consultado de lo sintético.

La evidencia es la **ficha de latencias y geometría de los segmentos** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Cuánto vale la velocidad de la luz en el vacío?
2. ¿Qué es la elevación de un satélite?
3. ¿Qué es un enlace de subida y uno de bajada?
4. ¿Cómo se pasa de bit/s a kB?
5. ¿Qué es una comprobación independiente?

<details>
<summary>Ver respuestas</summary>

1. 299 792,458 km/s, valor exacto del SI. 2. El ángulo sobre el horizonte local de la estación. 3. Subida: tierra→nave (comandos); bajada: nave→tierra (telemetría y datos). 4. Se multiplica por el tiempo y se divide por 8 y por 1000. 5. Calcular lo mismo por otro camino y comparar.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Un satélite **sintético** a 550 km tiene una estación que lo ve a 10° de elevación a 1 815,7 km. La luz tarda 6,06 ms en llegar. Un satélite geoestacionario está a 35 786 km: la ida y vuelta es de 0,239 s. Marte, entre 5,5×10⁷ y 4×10⁸ km, impone de 367 s a 2 669 s de ida y vuelta. Según el capítulo de la NASA sobre sistemas terrestres (S1), un centro de operaciones de misión (MOC) comanda la nave y un centro de operaciones científicas (SOC) genera los productos de datos.

## 6. Vocabulario

**Segmento espacial:** nave y carga útil. **Segmento terrestre:** estaciones, MOC, SOC y redes. **MOC/SOC:** centros de operaciones de misión y científicas. **Retardo de propagación:** `d/c`. **Ida y vuelta (RTT):** `2d/c`. **Rango oblicuo:** distancia estación–satélite según la elevación. **Enlace directo a la Tierra (DTE):** comunicación sin relé.

## 7. Modelo mental

```mermaid
flowchart LR
    N["Segmento espacial<br/>nave y carga util"] <-->|"enlace: retardo d/c"| E["Estacion"]
    E --> M["MOC: comandos y telemetria"]
    M --> S["SOC: productos de datos"]
    S --> U["Usuarios cientificos"]
```

*Descripción textual:* la nave se comunica con una estación; el MOC comanda y vigila, el SOC genera los productos y los usuarios los reciben. El único enlace con retardo físico es el primero.

Analogía: el segmento terrestre es la torre de control de un aeropuerto y la nave es el avión: la torre ve y habla, pero el mensaje tarda. Límite: un avión puede esperar en tierra una respuesta; la nave sigue su órbita mientras tanto.

## 8. La explicación, paso a paso

### 8.1 Qué dicen las fuentes

El capítulo de la NASA (S1) describe el segmento terrestre como las estaciones, redes, centros de control y servicios que envían comandos y recuperan datos; distingue el enlace directo a la Tierra, eficiente para contactos frecuentes y cortos, de los relés, que dan más cobertura pero con tasas bajas (cerca de 9,6 kbit/s según el capítulo). ECSS-E-ST-70-11C (S2) trata las funciones de a bordo que permiten operar la nave en situaciones nominales o de contingencia; solo se consultó su resumen.

### 8.2 Retardo y rango oblicuo

El retardo es `t = d/c`. El rango oblicuo a elevación `ε` y altura `h`, con `r = R + h`, es `d = −R sen ε + √(R² sen² ε + r² − R²)`. A 550 km y 10° da 1 815,652 km; la ley de cosenos con el ángulo central `λ = arccos(R/r · cos ε) − ε` da el mismo valor.

| Caso | `d` (km) | Ida (ms) | Ida y vuelta (s) |
|---|---|---|---|
| LEO cenit | 550,0 | 1,835 | 0,004 |
| LEO 10° | 1 815,7 | 6,056 | 0,012 |
| GEO | 35 786 | 119,369 | 0,239 |
| Luna | 384 400 | 1 282,220 | 2,564 |
| Marte cercano | 5,5×10⁷ | 183 460 | 366,921 |
| Marte lejano | 4×10⁸ | 1 334 256 | 2 668,513 |

### 8.3 Volumen de una pasada

`V = tasa × tiempo / 8`: 9 600 bit/s durante 480 s dan 576 kB. Con ese volumen un MOC no puede esperar bajar imágenes: la tasa y la duración son lo que manda.

### 8.4 Ciclo comando–respuesta

En GEO, con 2 s de proceso y 3 s del operador, el ciclo es `0,239 + 2 + 3 = 5,239 s`: el retardo físico es una fracción pequeña; en Marte sería el término dominante.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `c` | velocidad de la luz | km/s | 299 792,458 (exacta) |
| `d` | distancia | km | ver tabla |
| `R` | radio terrestre (esfera) | km | 6 378,137 |
| `ε` | elevación | ° | 10 |
| `t` | retardo | s | d/c |

## 10. Convenciones y referencias

Distancias en km y tiempos en s. Tierra esférica de radio 6 378,137 km; órbita circular; sin refracción atmosférica ni retardos de equipos. Sistema de referencia: horizonte local de la estación. Tolerancias: cuadrática frente a ley de cosenos `< 10⁻⁶ km`. Las distancias a la Luna y a Marte son redondeadas y **sintéticas**.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA, «Ground Data Systems and Mission Operations», en State-of-the-Art of Small Spacecraft Technology — https://www.nasa.gov/smallsat-institute/sst-soa/ground-data-systems-and-mission-operations/ (consultada 2026-11-10; leídos los primeros 100 000 caracteres de 215 453) | capítulo (parte inicial) | un centro de operaciones de misión (MOC) comanda la nave y un centro de operaciones científicas (SOC) genera productos; enlaces directos a la Tierra frente a relevos; bandas UHF, S, X y Ka; la licencia tarda meses; las antenas suelen adquirir el satélite con 5–10° de elevación; margen típico de 3 dB para retorno de datos en LEO a 1 500 km de distancia oblicua | Consultada (parte del capítulo) |
| S2 | ECSS, «ECSS-E-ST-70-11C — Space segment operability», 31 jul 2008 (cancelada y reemplazada por la Rev.1 del 15 oct 2025) — https://ecss.nl/standard/ecss-e-st-70-11c-space-segment-operability/ (consultada 2026-11-10) | página de la norma (solo el resumen; no el texto de requisitos) | disposiciones de diseño de las funciones de a bordo de un segmento espacial no tripulado para que pueda operarse en vuelo en situaciones nominales o de contingencia predefinidas; excluye la operabilidad específica de cada misión | Consultada (solo la página) |
| — | Libros de texto de operaciones de misión, comunicaciones espaciales y mecánica orbital (p. ej., Wertz y Larson, Montenbruck y Gill, Vallado) | — | — | No consultada |
| — | Relaciones y algoritmos estándar usados por el laboratorio (propagación `d/c` y geometría esférica) | — | los verifica el laboratorio con una segunda vía o con pruebas | No consultada en una fuente concreta |

Límites: del capítulo de la NASA solo se leyó la parte inicial; las distancias interplanetarias no provienen de efemérides. Lo simulado no se presenta como dato de vuelo ni como medición.

## 12. Cómo ver los resultados

| Magnitud | Valor |
|---|---|
| Ida y vuelta GEO | 0,239 s |
| Ida y vuelta Luna | 2,564 s |
| Ida y vuelta Marte (rango) | 367 a 2 669 s |
| Pasada de 480 s a 9 600 bit/s | 576 kB |

Descripción larga: el retardo crece linealmente con la distancia y pasa de milisegundos en LEO a decenas de minutos en Marte; en LEO el límite operativo es la duración del contacto, no la luz.

## 13. Ejemplo trabajado

**Paso 1 · Rango.** `d(10°) = 1 815,652 km`.

**Paso 2 · Retardo.** `1 815,652/299 792,458 = 6,056 ms`.

**Paso 3 · GEO.** `2 × 35 786/299 792,458 = 0,2387 s`.

**Paso 4 · Ciclo.** `0,2387 + 2 + 3 = 5,239 s`.

**Paso 5 · Comprobación.** La ley de cosenos reproduce el rango oblicuo.

## 14. Distintas formas de describir el problema

**Por tiempo:** retardos (esta clase). **Por geometría:** ventanas de visibilidad (C04). **Por enlace:** presupuesto de potencia (C27). Los tres se combinan para decidir qué se puede hacer en una pasada.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula el retardo de ida a 1 000 km.

<details><summary>Solución comentada</summary>

`1 000/299 792,458 = 3,336 ms`.
</details>

**Ejercicio 2 · con una pista.** Calcula la ida y vuelta a la Luna (384 400 km).

<details><summary>Solución comentada</summary>

`2 × 384 400/299 792,458 = 2,564 s`.
</details>

**Ejercicio 3 · casi autónomo.** Calcula el volumen de 300 s a 9 600 bit/s.

<details><summary>Solución comentada</summary>

`9 600 × 300/8 = 360 000 B = 360 kB`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** ¿Cuántas veces mayor es el retardo de Marte lejano que el de GEO?

<details><summary>Solución comentada</summary>

`4×10⁸/35 786 ≈ 11 177`.
</details>

**Ejercicio 5 · autónomo.** Un comando en GEO tarda 0,239 s de ida y vuelta; si el operador tarda 3 s, ¿qué fracción del ciclo es propagación?

<details><summary>Solución comentada</summary>

`0,239/5,239 = 4,6 %`.
</details>

**Ejercicio 6 · autónomo.** ¿Cuánto tarda la luz en recorrer 1 815,652 km?

<details><summary>Solución comentada</summary>

`6,056 ms`.
</details>

**Ejercicio 7 · autónomo.** ¿Qué elevación da el rango oblicuo más corto y por qué?

<details><summary>Solución comentada</summary>

90° (cenit): `d = h`.
</details>

**Ejercicio 8 · autónomo.** Una pasada de 8 min a 2 Mbit/s con eficiencia 85 %: ¿cuántos MB?

<details><summary>Solución comentada</summary>

`2×10⁶ × 480 × 0,85/8 = 102 MB`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un colega afirma que el retardo en Marte es 'unos segundos'. ¿Qué respondes?

<details><summary>Solución comentada</summary>

Es de minutos: 367 s a 2 669 s de ida y vuelta con las distancias sintéticas; no se puede operar en tiempo real.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Por qué un operador de LEO no se preocupa del retardo de propagación pero sí de la duración de la pasada?

<details><summary>Solución comentada</summary>

El retardo es de milisegundos; la ventana, de minutos, limita cuántos comandos y cuántos datos caben.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** Un relé GEO añade dos saltos de 35 786 km para cubrir un LEO: ¿cuánta ida y vuelta añade?

<details><summary>Solución comentada</summary>

Cuatro tramos de 35 786 km: `4 × 35 786/299 792,458 = 0,48 s`.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de latencias y geometría de los segmentos*: tabla de retardos, rango oblicuo comprobado, volumen de una pasada, ciclo comando–respuesta y lista de lo consultado, sintético y no consultado.

<details><summary>Solución comentada</summary>

Secciones 8.2–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: retardos y volumen de una pasada

El script [retardos_de_enlace.py](retardos_de_enlace.py) calcula distancias, retardos de ida y de ida y vuelta, el rango oblicuo a 10° por dos vías, el volumen de una pasada y el ciclo comando–respuesta; **comprueba** el rango y la ida y vuelta de GEO.

**Datos:** distancias **sintéticas** y redondeadas. **Predice antes de ejecutar:** ¿cuánto vale la ida y vuelta a GEO? (≈ 0,24 s). **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9
Datos SINTETICOS: distancias redondeadas, sin efemerides reales
LEO 550 km, cenit              d =          550.0 km ; ida =        1.835 ms ; ida y vuelta =      0.004 s
LEO 550 km, elev 10 grados     d =         1815.7 km ; ida =        6.056 ms ; ida y vuelta =      0.012 s
GEO 35786 km, subsatelite      d =        35786.0 km ; ida =      119.369 ms ; ida y vuelta =      0.239 s
Luna 384400 km                 d =       384400.0 km ; ida =     1282.220 ms ; ida y vuelta =      2.564 s
Marte cercano 5.5e7 km         d =     55000000.0 km ; ida =   183460.252 ms ; ida y vuelta =    366.921 s
Marte lejano 4.0e8 km          d =    400000000.0 km ; ida =  1334256.381 ms ; ida y vuelta =   2668.513 s
Rango oblicuo a 10 grados: cuadratica = 1815.652 km ; ley de cosenos = 1815.652 km
Pasada de 480 s a 9600 bit/s = 576.0 kB (sin sobrecarga)
Ciclo comando-respuesta GEO con 2 s de proceso y 3 s de operador = 5.239 s
Pruebas superadas.
```

```bash
python programa/clases/B96/B96-C01-segmento-espacial-y-segmento-terrestre/retardos_de_enlace.py
```

**Límites:** Tierra esférica, sin refracción, sin retardos de equipos ni de red terrestre, distancias redondeadas.

## 18. Errores frecuentes y cómo corregirlos

**Confundir ida con ida y vuelta.** El ciclo de un comando usa `2d/c` (8.2)

**Calcular el rango con la altura y no con la elevación.** Usa la fórmula oblicua (8.2)

**Presentar las distancias como efemérides.** Revisa la sección 10

## 19. Cómo sabrás que vas bien

Tras 8.2: ¿cuánto tarda un comando en llegar a Marte a 4×10⁸ km? Si dudas, repasa el ejercicio 4. Tras el laboratorio: ¿qué comprueba el rango oblicuo? (ver sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de latencias y geometría de los segmentos** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Explica el método y su dominio | Explica los límites y las alternativas |
| Cálculo | Sin unidades | Con errores | Resultados con unidades y comprobados | Resuelve casos nuevos |
| Numérico | Sin comprobar | Un caso | Verifica con una segunda vía en varios casos | Interpreta las diferencias y los fallos |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo sintético y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular los datos como sintéticos; comprobar cada resultado con una segunda vía; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y los datos son sintéticos; ningún resultado describe una misión real, certifica conformidad con una norma ni sustituye la revisión de especialistas.  Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

El retardo es de 6 ms en LEO a 10°, de 0,24 s de ida y vuelta en GEO y de hasta 2 669 s a Marte; lo que domina en LEO es la duración de la pasada. Queda una pregunta: ¿cómo se organiza el uso de esas pasadas?

**Glosario español–inglés.** segmento espacial · *space segment*; segmento terrestre · *ground segment*; centro de operaciones de misión · *mission operations center (MOC)*; ida y vuelta · *round-trip time*; rango oblicuo · *slant range*.

**Continuidad.** [B96-C02](../B96-C02-concepto-de-operaciones-de-mision/CLASE.md) trata el concepto de operaciones.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B95-C04 — Antenas desplegables para satélites pequeños](../../B95/B95-C04-antenas-desplegables-para-satelites-pequenos/CLASE.md) · [📚 Bloque B96](../../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) · [Siguiente: B96-C02 — Concepto de operaciones de misión →](../B96-C02-concepto-de-operaciones-de-mision/CLASE.md)
<!-- /nav -->
