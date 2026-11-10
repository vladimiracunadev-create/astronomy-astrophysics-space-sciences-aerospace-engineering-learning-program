# B92-C06 — Modulación y codificación en enlaces ópticos

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B92](../../../tronco-comun/B92-comunicaciones-opticas-espaciales-profundizacion.md) · [← Anterior: B92-C05 — Receptores y detectores para comunicaciones ópticas](../B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md) · [Siguiente: B92-C07 — Enlaces ópticos de espacio profundo →](../B92-C07-enlaces-opticos-de-espacio-profundo/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 6 del bloque B92. Nivel N3. Los enlaces ópticos de potencia limitada usan modulación por posición de pulso (PPM) con un código convolucional concatenado: el CCSDS 142.0-B-1 fija sus órdenes, tasas de código, ranuras de guarda y marcador de sincronización. Aquí calculas cuántas ranuras ocupa una palabra de código, qué tasa de información resulta, qué potencia de pico exige y cuántos bits caben por fotón. La modulación de radiofrecuencia se trató en [B89](../../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md); la óptica difiere porque el receptor cuenta fotones. Usas [C05](../B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md) para el receptor. El enlace es sintético.

## 2. Por qué esta clase existe

En un canal con pocos fotones, la eficiencia es bits por fotón, no bits por hercio. La decisión central: **¿qué orden PPM y qué tasa de código elegir para equilibrar tasa de información, fotones por bit y potencia de pico?**

## 3. Lo que podrás hacer al terminar

1. Calcular cuántos símbolos PPM y ranuras tiene una palabra de código del CCSDS 142.0-B-1.
2. Verificar ese conteo construyendo las ranuras explícitamente.
3. Calcular la tasa de información del bloque para cada orden PPM y tasa de código.
4. Calcular la razón entre potencia de pico y media.
5. Calcular la capacidad de un canal PPM sin fondo y los bits por fotón.
6. Separar lo consultado (estructura del CCSDS) de lo ilustrativo (ranura de 1 ns, fotones por símbolo).

La evidencia es la **tabla de tasas por orden PPM y tasa de código** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es PPM?
2. ¿Qué es una tasa de código `r`?
3. ¿Cuántos bits transporta un símbolo de orden `M`?
4. ¿Qué es una ranura de guarda?
5. ¿Qué es una verificación por segunda vía?

<details>
<summary>Ver respuestas</summary>

1. Un símbolo se envía como un pulso en una de `M` ranuras. 2. El cociente entre bits de información y bits de código. 3. `log₂ M`. 4. Una ranura vacía tras el símbolo para separar símbolos y absorber la respuesta del detector. 5. Calcular lo mismo con otro método y comparar.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Con ranuras de `1 ns`, PPM-16 y código de tasa `1/2`, el bloque de `7526` bits de información ocupa `75 920` ranuras y da `99,131 Mbps`; con orden 256 la tasa baja a `12,339 Mbps` y la potencia de pico sube a `320` veces la media. En el límite de pocos fotones, PPM-16 sin fondo transporta hasta `4` bits por fotón detectado. Es el **ejemplo conductor**. La estructura es la del CCSDS 142.0-B-1; la ranura de `1 ns` y los fotones por símbolo son **ilustrativos**.

## 6. Vocabulario

El **orden PPM** `M` es el número de ranuras de un símbolo, con `m = log₂ M` bits. La **ranura de guarda** son `M/4` ranuras vacías tras cada símbolo. La **tasa de código** `r` (1/3, 1/2 o 2/3) es la de un código convolucional concatenado con el modulador (SCPPM). El **bloque de información** `k` (5006, 7526 o 10046 bits) se amplía con una CRC-32 y 2 bits de terminación hasta `k̂`. El **marcador de sincronización de palabra** (CSM) son `W` símbolos PPM antepuestos a cada palabra. La **capacidad** de un canal sin fondo es `(1 − e^{−n_s}) log₂ M` bits por símbolo.

## 7. Modelo mental: contar monedas en un tablero con casillas vacías

```mermaid
flowchart LR
    B["bloque k"] --> C["código r: 15120 símbolos"]
    C --> P["símbolos PPM: 15120/m"]
    P --> S["+ CSM (W símbolos)"]
    S --> G["ranuras: (15120/m + W) · 1,25 M"]
    G --> R["tasa = k / (ranuras · T)"]
```

*Descripción textual:* un bloque de información se codifica en `15120` símbolos de código, se agrupan en símbolos PPM, se antepone el CSM y cada símbolo ocupa `1,25 M` ranuras; la tasa es `k` entre la duración.

Analogía: cada símbolo es una casilla marcada en una fila de `M` casillas más una cuarta parte vacía; cuantas más casillas por símbolo, más bits por marca pero más fila por bit. Límite: la tasa calculada es la del bloque de información, sin el ASM, los encabezados ni los marcos de transferencia.

## 8. La explicación, paso a paso

### 8.1 Estructura de la palabra

El CCSDS 142.0-B-1 define bloques `k = 5006, 7526, 10046` con `k̂ = k + 34` (CRC-32 más 2 bits de terminación) para `r = 1/3, 1/2, 2/3`; en los tres casos `k̂/r = 15120` símbolos binarios de código. Con `m = log₂ M` se agrupan en `15120/m` símbolos PPM y se añaden `W` del CSM (16 para `M ≥ 8`, 24 para `M = 4`). Cada símbolo ocupa `M + M/4` ranuras. Para `M = 16`: `3780 + 16 = 3796` símbolos y `75 920` ranuras.

### 8.2 Conteo de ranuras verificado

El laboratorio construye las ranuras explícitamente (mapeo de bits aleatorios a una posición de pulso más las guardas) y cuenta: `37 920` (`M = 4`), `50 560`, `75 920`, `121 600`, `202 880`, `348 160` y `609 920` (`M = 256`), idénticos a la fórmula, con un pulso por símbolo. La comprobación valida la aritmética del modelo y no la conformidad con el estándar.

### 8.3 Tasa de información

Con ranura de `T = 1 ns`, `R = k/(ranuras · T)`. Para `r = 1/2` (`k = 7526`): `198,470 Mbps` con `M = 4`, `99,131` con `M = 16`, `37,096` con `M = 64` y `12,339` con `M = 256`. Para `M = 16`: `65,938`, `99,131` y `132,323 Mbps` con `r = 1/3, 1/2, 2/3`; el cociente `2,007` entre `r = 2/3` y `1/3` es `10046/5006`.

### 8.4 Potencia de pico y ancho de banda

Un pulso por cada `1,25 M` ranuras da `P_pico/P_media = 1,25 M`: `5`, `20`, `80` y `320` para `M = 4, 16, 64, 256`. Subir `M` abarata los fotones por bit (C05) pero exige un transmisor de más potencia de pico (C01) y ranuras más estrechas para la misma tasa. El ejemplo del CCSDS 141.0-B-1 con ranuras de `1 ns`, 16-PPM y 4 guardas da pulsos separados entre `5` y `35 ns`, es decir `28,57` a `200 MHz` de tasa de repetición de pulsos; el laboratorio lo reproduce.

### 8.5 Capacidad y bits por fotón

Sin fondo, el canal PPM es un canal de borrado: si no se detecta ningún fotón (probabilidad `e^{−n_s}`) se pierde el símbolo. `C = (1 − e^{−n_s}) log₂ M`. Con `M = 16`: `1,5739` bits/símbolo para `n_s = 0,5` (`3,148` bits por fotón), `2,5285` para `1` (`2,5285` por fotón), `3,4587` para `2` y `3,9267` para `4` (`0,98` por fotón). Con pocos fotones por símbolo se aproxima a `log₂ M = 4` bits por fotón; con muchos, la eficiencia cae.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `M` | orden PPM | — | 4 a 256 |
| `m` | bits por símbolo | bit | `log₂ M` |
| `r` | tasa de código | — | 1/3, 1/2, 2/3 |
| `k` | bloque de información | bit | 5006; 7526; 10046 |
| `W` | símbolos del CSM | — | 16 (`M ≥ 8`); 24 (`M = 4`) |
| `T` | ancho de ranura | ns | 1 (ilustrativo) |
| `R` | tasa de información del bloque | Mbps | 12,3–264,9 |

## 10. Convenciones y referencias

Estructura según CCSDS 142.0-B-1 (tabla 3-1 y secciones 3.8.5, 3.10.2 y 3.13) y ranuras según CCSDS 141.0-B-1 (sección 3.9). La palabra de código se toma de `15120` símbolos binarios porque el texto consultado señala que ese número es múltiplo de `m`; no se verificó la definición completa del codificador, el entrelazador ni el ASM. La tasa es la del bloque de información, no la de usuario. `T = 1 ns` y los fotones por símbolo son ilustrativos. Tolerancia: conteo de ranuras exacto; `PRR` `10⁻¹²` relativa.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | CCSDS 142.0-B-1, *Optical Communications Coding and Synchronization*, agosto de 2019 — https://ccsds.org/Pubs/142x0b1.pdf (leído con PyMuPDF el 2026-11-10) | tabla 3-1; secciones 3.8.5, 3.10.2.1, 3.13 | `k` y `k̂` por tasa de código; órdenes PPM; `M/4` guardas; `W` del CSM | Consultada |
| S2 | CCSDS 141.0-B-1, *Optical Communications Physical Layer*, agosto de 2019 — https://ccsds.org/Pubs/141x0b1.pdf (leído con PyMuPDF el 2026-11-10) | secciones 3.7, 3.9 y 3.10 | OOK en la capa física; ranuras de 0,125 a 512 ns; ejemplo de 28,57 a 200 MHz | Consultada |
| S3 | Israel et al., *NASA's LCRD experiment program*, SPIE, 2024 — https://ntrs.nasa.gov/api/citations/20230018608/downloads/SPIE%20West%202024%20final.pdf (leído con PyMuPDF el 2026-11-10) | sección 6.3 | LCRD admite DPSK (2880 a 72 Mbps) y PPM (720 a 240 Mbps) con código y entrelazado de canal; contexto, no entra en el cálculo | Consultada |
| — | Capacidad del canal de borrado PPM y bits por fotón | — | los verifica el laboratorio con el límite `log₂ M` | No consultada en una fuente concreta |

Límites: no se consultó el codificador SCPPM completo ni sus curvas de desempeño; no se calcula ninguna ganancia de código.

## 12. Cómo ver la tasa por orden PPM

| Magnitud | Valor |
|---|---|
| ranuras por palabra (`M = 16`) | 75 920 |
| tasa (`M = 16`, `r = 1/2`) | 99,131 Mbps |
| tasa (`M = 256`, `r = 1/2`) | 12,339 Mbps |
| `P_pico/P_media` (`M = 256`) | 320 |
| bits por fotón (límite, `M = 16`) | 4 |

Descripción larga: al subir el orden PPM cae la tasa en proporción casi inversa a `M/log₂ M`, sube la potencia de pico en proporción a `M` y aumenta el límite de bits por fotón.

## 13. Ejemplo trabajado: tasa con M = 64 y r = 2/3

**Paso 1 · Bits por símbolo.** `m = 6`; `15120/6 = 2520` símbolos más `16` del CSM: `2536`.

**Paso 2 · Ranuras.** `2536 × 1,25 × 64 = 202 880`.

**Paso 3 · Duración.** `202 880 × 1 ns = 202,88 µs`.

**Paso 4 · Tasa.** `10046/202,88 µs = 49,517 Mbps`.

## 14. Distintas formas de describir un enlace PPM

**Por orden:** `M`, `m`. **Por código:** `r`, `k`. **Por ranuras:** `1,25 M` por símbolo. **Por tasa:** `R`. **Por potencia:** `P_pico/P_media`. **Por fotones:** bits por fotón.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Símbolos PPM por palabra con `M = 16`. *Pasos:* `m = 4`; `15120/m`; suma el CSM.

<details><summary>Solución comentada</summary>

`3780 + 16 = 3796`.
</details>

**Ejercicio 2 · con una pista.** Ranuras por palabra con `M = 16`. *Pista:* `1,25 M = 20` ranuras por símbolo.

<details><summary>Solución comentada</summary>

`3796 × 20 = 75 920`.
</details>

**Ejercicio 3 · casi autónomo.** Tasa con `M = 16`, `r = 1/2`, `T = 1 ns`.

<details><summary>Solución comentada</summary>

`7526/75 920 ns = 99,131 Mbps`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Tasa con `M = 256` y `r = 2/3`.

<details><summary>Solución comentada</summary>

`16,471 Mbps`.
</details>

**Ejercicio 5 · autónomo.** Tasa con `M = 4` y `r = 1/3`.

<details><summary>Solución comentada</summary>

`132,015 Mbps`.
</details>

**Ejercicio 6 · autónomo.** `P_pico/P_media` con `M = 64`.

<details><summary>Solución comentada</summary>

`1,25 × 64 = 80`.
</details>

**Ejercicio 7 · autónomo.** Bits por fotón detectado con `M = 16` y `n_s = 1`.

<details><summary>Solución comentada</summary>

`(1 − e^{−1}) × 4 = 2,5285` bits por símbolo y por fotón.
</details>

**Ejercicio 8 · autónomo.** Cociente entre las tasas de `r = 2/3` y `r = 1/3`.

<details><summary>Solución comentada</summary>

`10046/5006 = 2,007`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Con ranuras de `0,125 ns`, `M = 16` y 4 guardas, ¿qué tasa de repetición de pulsos hay entre los casos extremos?

<details><summary>Solución comentada</summary>

Separación mínima de `5 × 0,125 = 0,625 ns` (`1600 MHz`) y máxima de `35 × 0,125 = 4,375 ns` (`228,57 MHz`).
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** Pasar de `M = 16` a `M = 256` con `r = 1/2` y ranuras de `1 ns`: ¿qué se gana y qué se pierde?

<details><summary>Solución comentada</summary>

La tasa cae de `99,131` a `12,339 Mbps` (`÷ 8,03`) y la potencia de pico sube `16` veces; se ganan fotones por bit (de `2,732` a `1,639` incidentes, C05) y mejor sensibilidad.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Por qué un estándar ofrece tres tasas de código?

<details><summary>Solución comentada</summary>

Para elegir en cada enlace entre robustez (`r` baja: menos información por símbolo y más corrección) y tasa (`r` alta): con el mismo `M` la tasa se duplica entre `1/3` y `2/3`.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *tabla de tasas por orden PPM y tasa de código*: estructura de la palabra, ranuras, tasas para cuatro `M` y tres `r`, `P_pico/P_media`, capacidad sin fondo y lista de qué es consultado e ilustrativo.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.5 y la salida del laboratorio.
</details>

## 17. Laboratorio: estructura SCPPM y tasa de información

El script [codificacion.py](codificacion.py) construye las ranuras de una palabra para los siete órdenes PPM, calcula la tasa de información para tres tasas de código, reproduce la tasa de repetición de pulsos del ejemplo del CCSDS y calcula la capacidad sin fondo (**comprueba** conteo de ranuras exacto, `k̂/r = 15120`, el rango de `28,57` a `200 MHz` y bits por fotón decrecientes).

**Datos:** tabla 3-1, guardas, CSM y ranuras del CCSDS (consultados); ranura de `1 ns` y fotones por símbolo **ilustrativos**. **Predice antes de ejecutar:** ¿qué tasa da `M = 16` con `r = 1/2`? (≈99 Mbps.) **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Comprobacion de la estructura de la palabra (formula frente a construccion explicita de ranuras):
   M  m  simbolos/palabra  ranuras formula  ranuras construidas  pulsos
   4  2             7584            37920                37920    7584
   8  3             5056            50560                50560    5056
  16  4             3796            75920                75920    3796
  32  5             3040           121600               121600    3040
  64  6             2536           202880               202880    2536
 128  7             2176           348160               348160    2176
 256  8             1906           609920               609920    1906
Bloques: k/k^ = 1/3: 5006/5040, 1/2: 7526/7560, 2/3: 10046/10080 ; control: k^ / r = 15120
Tasa de informacion del bloque [Mbps], ranura de 1 ns:
   M   r=1/3     r=1/2     r=2/3   bits por ranura (r=1/2)  P_pico/P_media
   4  132.015   198.470   264.926           0.19847                5.0
  16   65.938    99.131   132.323           0.09913               20.0
  64   24.675    37.096    49.517           0.03710               80.0
 256    8.208    12.339    16.471           0.01234              320.0
PRR del ejemplo CCSDS (1 ns, 16-PPM, 4 guardas): 28.57 a 200 MHz (publicado: 28.57 a 200 MHz)
Capacidad del canal PPM sin fondo (borrado), M = 16:
  ns detectados  bits/simbolo  bits por foton detectado
           0.5        1.5739        3.1478
           1.0        2.5285        2.5285
           2.0        3.4587        1.7293
           4.0        3.9267        0.9817
  limite ns -> 0: 4.0000 bits por foton = log2 M
Pruebas superadas.
```

```bash
python programa/clases/B92/B92-C06-modulacion-y-codificacion-en-enlaces-opticos/codificacion.py
```

**Límites:** el conteo de ranuras construye la estructura que el propio modelo supone, por lo que valida la aritmética y no la conformidad con el estándar; no se implementa el codificador ni el decodificador; la tasa es la del bloque de información.

## 18. Errores frecuentes y cómo corregirlos

**Olvidar las ranuras de guarda y el CSM.** Se corrige con 8.1.

**Confundir tasa de bloque con tasa de usuario.** Se corrige con la sección 10.

**Creer que más `M` es siempre mejor.** Se corrige con 8.4.

**Presentar la ranura de 1 ns como la de una misión.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué tasa esperabas con `M = 16` y `r = 1/2`, y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **tabla de tasas por orden PPM y tasa de código** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Relaciona `M`, `r`, ranuras y tasa | Explica el compromiso tasa, pico y fotones |
| Cálculo | Sin unidades | Con errores | Tablas completas con unidades | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con la construcción de ranuras | Interpreta los límites de la comprobación |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo ilustrativo y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular ranura y fotones como ilustrativos; no presentar la tasa de bloque como tasa de usuario; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: el modelo cuenta ranuras y no implementa el estándar; su lectura no sustituye al documento completo ni a las pruebas de interoperabilidad. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

PPM-16 con código de tasa `1/2` ocupa `75 920` ranuras por palabra y da `99,131 Mbps` con ranuras de `1 ns`; subir el orden baja la tasa, sube la potencia de pico y baja los fotones por bit. Queda una pregunta: ¿qué cambia cuando el enlace cruza decenas de millones de kilómetros?

**Glosario español–inglés.** modulación por posición de pulso · *pulse position modulation*; ranura de guarda · *guard slot*; tasa de código · *code rate*; marcador de sincronización · *synchronization marker*; fotones por bit · *photons per bit*.

**Continuidad.** [B92-C07](../B92-C07-enlaces-opticos-de-espacio-profundo/CLASE.md) estudia los enlaces de espacio profundo.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B92-C05 — Receptores y detectores para comunicaciones ópticas](../B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md) · [📚 Bloque B92](../../../tronco-comun/B92-comunicaciones-opticas-espaciales-profundizacion.md) · [Siguiente: B92-C07 — Enlaces ópticos de espacio profundo →](../B92-C07-enlaces-opticos-de-espacio-profundo/CLASE.md)
<!-- /nav -->
