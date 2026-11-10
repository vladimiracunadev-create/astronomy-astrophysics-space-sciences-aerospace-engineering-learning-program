# B96-C16 — Gestión de datos científicos

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B96](../../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) · [← Anterior: B96-C15 — Operaciones de emergencia](../B96-C15-operaciones-de-emergencia/CLASE.md) · [Siguiente: B96-C17 — Coordinación de múltiples estaciones →](../B96-C17-coordinacion-de-multiples-estaciones/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 16 del bloque B96. Nivel N3. Los **datos científicos** llegan en paquetes numerados que pueden perderse en el enlace. Aquí detectas los huecos por número de secuencia, calculas la completitud tras varias pasadas con retransmisión y comparas con la teoría `N·pᵏ`; luego miras cómo el volumen cambia entre niveles de procesamiento (L0, L1, L2). Los 10 000 paquetes y las pérdidas son **sintéticos**. Todos los datos son **sintéticos** salvo los que se rotulan como consultados.

## 2. Por qué esta clase existe

Un conjunto de datos con huecos no declarados da conclusiones erróneas, y una retransmisión sin plan agota los contactos. La decisión central: **¿qué falta, cuántas pasadas hacen falta para completarlo y qué producto se entrega en cada nivel?**

## 3. Lo que podrás hacer al terminar

1. Detectar los paquetes faltantes y agruparlos en rangos por número de secuencia.
2. Simular la retransmisión de faltantes en pasadas sucesivas.
3. Comparar los faltantes con la teoría `N·pᵏ`.
4. Calcular el volumen por nivel de procesamiento.
5. Verificar la agrupación en rangos con un caso construido.
6. Separar lo consultado de lo sintético.

La evidencia es la **informe de completitud de un conjunto de datos** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es un número de secuencia?
2. ¿Qué es la completitud?
3. ¿Qué es la retransmisión?
4. ¿Qué son los niveles L0, L1 y L2?
5. ¿Qué es una pérdida independiente?

<details>
<summary>Ver respuestas</summary>

1. Un contador que identifica el orden de cada paquete. 2. La fracción de paquetes esperados que se recibió. 3. Volver a enviar lo que no llegó. 4. Datos brutos, datos calibrados y productos derivados. 5. Cada paquete se pierde con la misma probabilidad sin depender de los demás.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

10 000 paquetes de 1 kB (10,240 MB) con pérdida del 3 % por pasada: la primera pasada deja 272 faltantes (esperados 300) en 258 rangos; la segunda, 8 (esperados 9); la tercera, 0. La completitud pasa de 97,28 % a 99,92 % y 100 %. De los 10,240 MB brutos, el nivel L1 (calibrado y sin duplicados) ocupa 9,830 MB y el L2 (derivado), 3,072 MB.

## 6. Vocabulario

**Paquete:** unidad de datos con número de secuencia. **Hueco:** rango de números faltantes. **Completitud:** fracción recibida. **Retransmisión:** reenvío de faltantes. **Nivel de procesamiento:** grado de elaboración del dato (L0, L1, L2).

## 7. Modelo mental

```mermaid
flowchart LR
    N["10000 paquetes numerados"] --> R["Recibidos tras la pasada 1"]
    R --> H["Detectar huecos por secuencia"]
    H --> T["Retransmitir faltantes en la pasada 2"]
    T --> C["Completitud"]
    C --> L["L0, L1, L2"]
```

*Descripción textual:* se numeran los paquetes, se detectan los huecos tras cada pasada, se retransmiten los faltantes y, cuando están completos, se procesan en niveles.

Analogía: los huecos son como páginas que faltan en un libro numerado: se sabe cuáles son porque la numeración las delata. Límite: si el contador se reinicia o se repite, la numeración deja de decir qué falta.

## 8. La explicación, paso a paso

### 8.1 Qué dicen las fuentes

El capítulo de la NASA sobre sistemas terrestres (S1) separa el centro de operaciones de misión (MOC) del centro de operaciones científicas (SOC), que genera los productos de datos. ECSS-E-ST-70-41C (S2) trata los paquetes de telemetría y telecomando, con servicios opcionales. Solo se leyó la parte inicial del capítulo y el resumen de la norma. Los niveles L0 a L2 y las fracciones de volumen son **sintéticos** y didácticos.

### 8.2 Huecos y completitud

Con los números de secuencia recibidos, los faltantes son `{0..N−1} \ recibidos`; se agrupan en rangos consecutivos. Si cada paquete se pierde con probabilidad `p` por pasada, tras `k` pasadas faltan en promedio `N·pᵏ`.

| Antes de la pasada | Faltantes | Rangos | Esperados `N pᵏ` |
|---|---|---|---|
| 1 | 272 | 258 | 300 |
| 2 | 8 | 8 | 9 |
| 3 | 0 | 0 | 0,27 |
| 4 | 0 | 0 | 0,01 |

### 8.3 Verificación

Un caso construido (se pierden los múltiplos de 7) da 1 429 faltantes en 1 429 rangos; la suma de longitudes de los rangos es igual al número de faltantes. Las desviaciones de 272 y 8 respecto de 300 y 9 caen dentro de 4√esperado.

### 8.4 Niveles

L0 (brutos) 10,240 MB; L1 (calibrado, sin duplicados) 9,830 MB (96 %); L2 (derivado) 3,072 MB (30 %). La decisión de qué nivel se archiva y cuánto tiempo se retiene es de la misión.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `N` | paquetes | — | 10 000 |
| `L` | tamaño de paquete | B | 1 024 |
| `p` | pérdida por paquete y pasada | — | 0,03 |
| `k` | pasadas | — | 1 a 4 |
| `V` | volumen | MB | 10,240 |

## 10. Convenciones y referencias

Paquetes de 1 024 bytes, MB = 10⁶ bytes; pérdidas independientes y uniformes; sin duplicados ni reordenamiento; semilla 96. Todo **sintético**. Tolerancias: faltantes dentro de `4√esperado + 1`; suma de rangos igual a faltantes.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA, «Ground Data Systems and Mission Operations», en State-of-the-Art of Small Spacecraft Technology — https://www.nasa.gov/smallsat-institute/sst-soa/ground-data-systems-and-mission-operations/ (consultada 2026-11-10; leídos los primeros 100 000 caracteres de 215 453) | capítulo (parte inicial) | un centro de operaciones de misión (MOC) comanda la nave y un centro de operaciones científicas (SOC) genera productos; enlaces directos a la Tierra frente a relevos; bandas UHF, S, X y Ka; la licencia tarda meses; las antenas suelen adquirir el satélite con 5–10° de elevación; margen típico de 3 dB para retorno de datos en LEO a 1 500 km de distancia oblicua | Consultada (parte del capítulo) |
| S2 | ECSS, «ECSS-E-ST-70-41C — Telemetry and telecommand packet utilization», 15 abr 2016 — https://ecss.nl/standard/ecss-e-st-70-41c-space-engineering-telemetry-and-telecommand-packet-utilization-15-april-2016/ (consultada 2026-11-10) | página de la norma (solo el resumen) | cómo se usan los paquetes de telecomando y telemetría para vigilar y controlar subsistemas y cargas útiles; servicios opcionales adaptables por misión; excluye paquetes de datos de carga útil propios de cada misión, audio y vídeo | Consultada (solo la página) |
| — | Libros de texto de operaciones de misión, comunicaciones espaciales y mecánica orbital (p. ej., Wertz y Larson, Montenbruck y Gill, Vallado) | — | — | No consultada |
| — | Relaciones y algoritmos estándar usados por el laboratorio (detección de huecos por secuencia y distribución binomial de pérdidas) | — | los verifica el laboratorio con una segunda vía o con pruebas | No consultada en una fuente concreta |

Límites: el capítulo se leyó solo en parte y la norma solo en su resumen; no hay pérdidas en ráfaga, reordenamiento ni corrupción de bits. Lo simulado no se presenta como dato de vuelo ni como medición.

## 12. Cómo ver los resultados

| Pasada | Completitud |
|---|---|
| 1 | 97,280 % |
| 2 | 99,920 % |
| 3 | 100,000 % |

Descripción larga: cada retransmisión multiplica los faltantes por `p = 0,03`; en tres pasadas el conjunto queda completo.

## 13. Ejemplo trabajado

**Paso 1 · Recibidos.** 9 728 de 10 000.

**Paso 2 · Huecos.** 272 faltantes en 258 rangos.

**Paso 3 · Retransmitir.** Quedan 8.

**Paso 4 · Teoría.** `10 000 × 0,03² = 9`.

**Paso 5 · Volumen.** L1 = `0,96 × 10,240 = 9,830 MB`.

## 14. Distintas formas de describir el problema

**Por secuencia:** huecos (esta clase). **Por transporte:** de la estación al centro (C22). **Por producto:** niveles L0–L2. **Por archivo:** metadatos y retención.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula los faltantes esperados tras la primera pasada con `p = 3 %` y `N = 10 000`.

<details><summary>Solución comentada</summary>

`300`.
</details>

**Ejercicio 2 · con una pista.** Y tras la segunda.

<details><summary>Solución comentada</summary>

`10 000 × 0,03² = 9`.
</details>

**Ejercicio 3 · casi autónomo.** ¿Cuántos MB son 10 000 paquetes de 1 024 B?

<details><summary>Solución comentada</summary>

`10,240 MB`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** ¿Cuál es la completitud con 272 faltantes?

<details><summary>Solución comentada</summary>

`1 − 272/10 000 = 97,28 %`.
</details>

**Ejercicio 5 · autónomo.** Si `p = 10 %`, ¿cuántas pasadas dejan menos de 1 faltante esperado en 10 000?

<details><summary>Solución comentada</summary>

`10 000 × 0,1ᵏ < 1` → `k = 5`.
</details>

**Ejercicio 6 · autónomo.** Si faltan los paquetes 10 a 14 y 30, ¿cuántos rangos hay?

<details><summary>Solución comentada</summary>

2: [10, 14] y [30, 30].
</details>

**Ejercicio 7 · autónomo.** ¿Qué pasa con la agrupación si faltan paquetes consecutivos por una ráfaga?

<details><summary>Solución comentada</summary>

Hay menos rangos que faltantes; el modelo independiente subestima la duración de los huecos.
</details>

**Ejercicio 8 · autónomo.** ¿Cuánto ocupa L2 si es 30 % del bruto?

<details><summary>Solución comentada</summary>

`0,30 × 10,240 = 3,072 MB`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un colega entrega datos con huecos sin declararlos. ¿Qué problema crea?

<details><summary>Solución comentada</summary>

Quien analiza no sabe qué falta y puede sesgar sus resultados; hay que declarar la completitud.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Qué ocurre si un paquete llega duplicado?

<details><summary>Solución comentada</summary>

Hay que descartarlo en L1; por eso L1 es menor que L0.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Qué no modela esta clase respecto a un enlace real?

<details><summary>Solución comentada</summary>

Pérdidas en ráfaga, reordenamiento, corrupción y limitaciones de tiempo de pasada.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *informe de completitud de un conjunto de datos*: huecos, retransmisión, comparación con la teoría, niveles y lista de lo consultado, sintético y no consultado.

<details><summary>Solución comentada</summary>

Secciones 8.2–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: huecos, retransmisión y niveles

El script [completitud_de_datos.py](completitud_de_datos.py) simula la recepción con pérdidas, detecta huecos por número de secuencia, retransmite faltantes en pasadas sucesivas y calcula el volumen por nivel; **comprueba** los faltantes frente a `N·pᵏ` y la agrupación en rangos.

**Datos:** 10 000 paquetes y pérdidas **sintéticos**; semilla 96. **Predice antes de ejecutar:** ¿cuántos faltantes quedan tras la primera pasada? (≈ 300). **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9
Datos SINTETICOS: 10000 paquetes de 1 kB; perdida aleatoria; semilla 96
Pasada  recibidos  faltan  rangos_de_hueco  completitud
     1       9728     272              258      97.280 %
     2       9992       8                8      99.920 %
     3      10000       0                0     100.000 %
     4      10000       0                0     100.000 %
Faltantes por pasada = [272, 8, 0, 0]
Faltantes esperados N p^k = [300.0, 9.0, 0.27, 0.01]
Prueba de huecos con paquetes multiplos de 7 perdidos: 1429 faltantes en 1429 rangos
Nivel                           volumen [MB]
L0 (paquetes brutos)                10.240
L1 (calibrado, sin duplicados)       9.830
L2 (producto derivado)               3.072
Volumen bruto = 10.240 MB (10000 x 1024 B)
Pruebas superadas.
```

```bash
python programa/clases/B96/B96-C16-gestion-de-datos-cientificos/completitud_de_datos.py
```

**Límites:** pérdidas independientes, sin ráfagas, duplicados ni corrupción; sin límite de tiempo de pasada.

## 18. Errores frecuentes y cómo corregirlos

**Confiar en que todo llegó.** Revisa la secuencia (8.2)

**No declarar la completitud.** Informa los huecos (8.3)

**Mezclar niveles de procesamiento.** Rotula L0, L1 y L2 (8.4)

## 19. Cómo sabrás que vas bien

Tras 8.2: ¿cuántos faltantes esperas tras tres pasadas? Si dudas, repasa el ejercicio 5. Tras el laboratorio: ¿qué comprueba la prueba de múltiplos de 7? (ver sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **informe de completitud de un conjunto de datos** (ejercicio 12).

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

Con pérdida de 3 % por pasada, el conjunto sintético de 10 000 paquetes pasa de 97,28 % a 99,92 % y 100 % de completitud en tres pasadas. Queda una pregunta: ¿cómo se reparten las pasadas entre varias estaciones?

**Glosario español–inglés.** paquete · *packet*; número de secuencia · *sequence number*; completitud · *completeness*; retransmisión · *retransmission*; nivel de procesamiento · *processing level*.

**Continuidad.** [B96-C17](../B96-C17-coordinacion-de-multiples-estaciones/CLASE.md) trata la coordinación de múltiples estaciones.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B96-C15 — Operaciones de emergencia](../B96-C15-operaciones-de-emergencia/CLASE.md) · [📚 Bloque B96](../../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) · [Siguiente: B96-C17 — Coordinación de múltiples estaciones →](../B96-C17-coordinacion-de-multiples-estaciones/CLASE.md)
<!-- /nav -->
