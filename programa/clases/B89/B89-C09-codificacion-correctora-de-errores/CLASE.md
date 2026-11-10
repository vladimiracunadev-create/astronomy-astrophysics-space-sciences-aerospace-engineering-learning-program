# B89-C09 — Codificación correctora de errores

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B89](../../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) · [← Anterior: B89-C08 — Modulación digital](../B89-C08-modulacion-digital/CLASE.md) · [Siguiente: B89-C10 — Sincronización de portadora →](../B89-C10-sincronizacion-de-portadora/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 9 del bloque B89, nivel N3. Un código corrector añade redundancia para que el receptor detecte y corrija errores; a cambio, cada bit de información cuesta más símbolos. Aquí implementas un Hamming(7,4), calculas la protección de un Reed–Solomon (255,223) y estimas cuántos decibelios de `Eb/N0` ahorra. Usas [B89-C08](../B89-C08-modulacion-digital/CLASE.md) para la BER y [B89-C05](../B89-C05-presupuesto-de-enlace/CLASE.md) para dónde entra la ganancia de código. El canal es sintético; los tamaños de bloque y el entrelazado salen de la CCSDS 131.0-B-5.

## 2. Por qué esta clase existe

La codificación es la herramienta que permite cerrar enlaces de espacio profundo con potencias modestas: cada decibelio de ganancia de código equivale a una antena más grande o a más potencia. La decisión central: **¿cuánta redundancia añadir y cuánto `Eb/N0` se ahorra con ella?**

## 3. Lo que podrás hacer al terminar

1. Codificar y decodificar un Hamming(7,4) y corregir un error.
2. Calcular la probabilidad de bloque no corregido de un código de bloque con capacidad `t`.
3. Calcular la probabilidad de bloque no corregido de RS(255,223) con `t = 16`.
4. Estimar la ganancia de codificación como diferencia de `Eb/N0` requerido.
5. Leer la tabla de bloques y profundidad de entrelazado de la CCSDS 131.0-B-5.
6. Rotular lo consultado (tabla CCSDS) frente a lo sintético (canal) y a la aproximación de BER.

La evidencia es la **curva de decodificación de un código de bloque** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es la redundancia en un código?
2. ¿Qué es la tasa de un código?
3. ¿Qué es un símbolo en Reed–Solomon?
4. ¿Qué es un canal binario simétrico?
5. ¿Qué es la ganancia de codificación?

<details>
<summary>Ver respuestas</summary>

1. Bits adicionales calculados a partir de los de información. 2. La razón entre bits de información y bits codificados. 3. Un grupo de `m` bits (aquí 8, un octeto). 4. Un canal donde cada bit se invierte con probabilidad `p`. 5. La reducción de `Eb/N0` requerido para igual BER gracias al código.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Un Hamming(7,4) en un canal con `p = 0,02` baja la probabilidad de bloque erróneo a `0,00786` (simulada `0,00786`). RS(255,223) corrige hasta 16 octetos por bloque y, con BPSK, baja el `Eb/N0` necesario para BER 10⁻⁵ de `9,59` a `6,29 dB` (ganancia `3,29 dB`, aproximada). Es el **ejemplo conductor**.

## 6. Vocabulario

Un **código de bloque (n,k)** convierte `k` símbolos en `n`. Su **capacidad de corrección** `t` es el número de símbolos erróneos que corrige; Reed–Solomon (255,223) tiene `t = 16`. **Hamming(7,4)** corrige 1 bit en 7. La **tasa del código** `r = k/n`. El **entrelazado de profundidad `I`** reparte los octetos de `I` palabras para dispersar ráfagas de errores. La **ganancia de codificación** es la reducción de `Eb/N0` a BER fija.

## 7. Modelo mental: repetir lo importante para que sobreviva al ruido

```mermaid
flowchart LR
    K["k simbolos de informacion"] --> ENC["codificador (n,k)"]
    ENC --> N["n simbolos"]
    N --> CH["canal: errores p"]
    CH --> DEC["decodificador: corrige hasta t"]
    DEC --> OUT["BER de salida"]
    OUT --> G["ganancia = Eb/N0 sin codigo - con codigo"]
```

*Descripción textual:* el codificador convierte `k` símbolos en `n`; el canal introduce errores; el decodificador corrige hasta `t`; la BER de salida da la ganancia de codificación.

Analogía: deletrear una palabra importante con un «alfa, bravo, charlie»: tardas más, pero se entiende aunque haya ruido. Límite: la redundancia reduce la tasa útil y el decodificador falla bruscamente si se supera `t`.

## 8. La explicación, paso a paso

### 8.1 Hamming(7,4)

Los 4 bits de datos se acompañan de 3 bits de paridad; el síndrome indica la posición del error. En 16 palabras y 7 posiciones, un solo error siempre se corrige (el laboratorio lo comprueba). Con `p = 0,02`, la probabilidad de bloque erróneo teórica es `1 − (1−p)⁷ − 7p(1−p)⁶ = 0,00786`; la simulación con `random.Random(89)` da `0,00786` (z = `0,01`) y la BER de información `0,00336`, frente a 0,02 sin código.

### 8.2 Reed–Solomon (255,223)

Con `t = 16`, un bloque se pierde si hay más de 16 octetos erróneos. La probabilidad cae abruptamente: `p_s = 0,01` → `1,40e-09`; `0,05` → `1,41e-01`; en el umbral `t/n = 0,0627` → `4,33e-01`; `0,10` → `9,75e-01`. La tasa del código es `223/255 = 0,8745`.

### 8.3 Ganancia de codificación

Con BPSK y la BER de salida aproximada, el `Eb/N0` necesario para 10⁻⁵ pasa de `9,59 dB` sin código a `6,29 dB` con RS(255,223): ganancia de `3,29 dB`, descontada la pérdida de tasa. Es un cálculo aproximado (relación estándar no consultada).

### 8.4 Bloques y entrelazado de la CCSDS

La CCSDS 131.0-B-5 (consultada) admite profundidades `I = 1, 2, 3, 4, 5, 8` y fija los bloques de información de 1784, 3568, 7136 y 8920 bits (`223 × 8 × I` con `I = 1, 2, 4, 5`). En el laboratorio, `n = 255 × 8 × I` bits por bloque codificado.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `n`, `k` | longitud y dimensión del código | símbolos | 255, 223 (RS); 7, 4 (Hamming) |
| `t` | capacidad de corrección | símbolos | 16 (RS); 1 (Hamming) |
| `r` | tasa del código | — | 0,8745 |
| `p` | probabilidad de error de bit/símbolo | — | 0,02 (sintético) |
| `I` | profundidad de entrelazado | — | 1, 2, 3, 4, 5, 8 (CCSDS) |
| ganancia | reducción de `Eb/N0` a BER 10⁻⁵ | dB | 3,29 |

## 10. Convenciones y referencias

Canal binario simétrico sin memoria (Hamming) y errores de símbolo independientes (RS), decodificación a distancia acotada. Los tamaños de bloque y las profundidades de entrelazado provienen de CCSDS 131.0-B-5 (septiembre de 2023, leída con PyMuPDF); el canal, `p` y la semilla 89 son sintéticos; la ecuación de BER de salida es una aproximación estándar no consultada.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | CCSDS 131.0-B-5, TM Synchronization and Channel Coding, Blue Book, septiembre de 2023 — https://ccsds.org/Pubs/131x0b5.pdf (PDF leido con PyMuPDF, consultada 2026-11-10) | tablas 6-1, 6-2 y 8-1; secciones 4.3.5 y 8.2 | profundidades de entrelazado I = 1, 2, 3, 4, 5, 8; bloques de informacion de 1784, 3568, 7136 y 8920 bits (223 octetos × I); longitudes de palabra del codigo turbo; marcador ASM 1ACFFC1D (32 bits) y CSM de 64 bits 034776C7272895B0 para LDPC 1/2, 2/3 y 4/5 | Consultada |
| — | Relaciones estándar (síndrome de Hamming, probabilidad de bloque binomial, BER de salida de RS) | — | las verifica el laboratorio con una simulación y un enfoque exhaustivo | No consultada en una fuente concreta |

Límites: de la CCSDS 131.0-B-5 solo se usaron las tablas 6-1 y 6-2 y el entrelazado (4.3.5); no se consultaron los polinomios del código RS ni el codificador; la ganancia estimada no es la del estándar.

## 12. Cómo ver la protección de un código

| Magnitud | Valor |
|---|---|
| P(bloque erróneo) de Hamming, `p = 0,02` | 0,00786 |
| P(bloque) de RS en `p_s = 0,05` | 1,41e-01 |
| `Eb/N0` sin código | 9,59 dB |
| `Eb/N0` con RS(255,223) | 6,29 dB |
| ganancia de código | 3,29 dB |

Descripción larga: el código funciona casi como un umbral: con pocos errores casi nunca falla y cerca de `t/n` la probabilidad de fallo crece de golpe hasta casi 1; la ganancia aparece como un desplazamiento de la curva de BER.

## 13. Ejemplo trabajado: un Hamming con un error

**Paso 1 · Datos.** `d = 1011`: `p₁ = d₁⊕d₂⊕d₄ = 0`, `p₂ = d₁⊕d₃⊕d₄ = 1`, `p₃ = d₂⊕d₃⊕d₄ = 0`; palabra (posiciones 1 a 7) `0 1 1 0 0 1 1`.

**Paso 2 · Error.** Se invierte la posición 5: `0 1 1 0 1 1 1`.

**Paso 3 · Síndrome.** `s₁ = c₁⊕c₃⊕c₅⊕c₇ = 1`, `s₂ = c₂⊕c₃⊕c₆⊕c₇ = 0`, `s₃ = c₄⊕c₅⊕c₆⊕c₇ = 1`; posición `1 + 0 + 4 = 5`.

**Paso 4 · Corrección.** Se invierte la posición 5 y se recuperan los datos `1011` (posiciones 3, 5, 6 y 7).

## 14. Distintas formas de describir un código correctivo

**Por parámetros:** (n,k,t). **Por tasa:** `k/n`. **Por probabilidad de fallo:** `P_bloque(p)`. **Por ganancia:** diferencia de `Eb/N0`. **Por estándar:** tamaños y entrelazado.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula la tasa de RS(255,223). *Pasos:* `223/255`.

<details><summary>Solución comentada</summary>

`0,8745`.
</details>

**Ejercicio 2 · con una pista.** Predice cuántos octetos erróneos soporta un bloque de RS. *Pista:* `t = (n − k)/2`.

<details><summary>Solución comentada</summary>

`(255 − 223)/2 = 16`.
</details>

**Ejercicio 3 · casi autónomo.** ¿Por qué un código de tasa menor puede mejorar el enlace aunque gaste más símbolos?

<details><summary>Solución comentada</summary>

Porque la ganancia de código (menor `Eb/N0` requerido) compensa la menor energía por símbolo codificado; mira el cálculo de la ganancia.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Bits de información `k` para `I = 3` según 223 octetos × I.

<details><summary>Solución comentada</summary>

`5352` bits.
</details>

**Ejercicio 5 · autónomo.** Bits codificados `n` para `I = 5`.

<details><summary>Solución comentada</summary>

`10200` bits.
</details>

**Ejercicio 6 · autónomo.** Probabilidad de bloque erróneo de un Hamming con `p = 0,05`.

<details><summary>Solución comentada</summary>

`1 − 0,95⁷ − 7×0,05×0,95⁶ = 0,04438`.
</details>

**Ejercicio 7 · autónomo.** Sobrecarga de RS(255,223) en porcentaje.

<details><summary>Solución comentada</summary>

`(255 − 223)/223 = 14,3 %`.
</details>

**Ejercicio 8 · autónomo.** Con `I = 5`, ¿cuántos octetos erróneos consecutivos puede dispersar el entrelazado?

<details><summary>Solución comentada</summary>

Hasta `5 × 16 = 80` octetos en ráfaga (16 por palabra) si se reparten por igual.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un enlace pierde 3 dB de margen. ¿Puede un código de ganancia 3 dB recuperarlo?

<details><summary>Solución comentada</summary>

En principio sí, a costa de una tasa útil menor; hay que verificar la BER objetivo y el umbral.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** Una simulación de RS da P_bloque = 10⁻¹⁰ con `p_s = 0,1`. ¿Es plausible?

<details><summary>Solución comentada</summary>

No: la teoría da `9,75e-01`; con `p_s = 0,1`, por encima de `t/n`, el código falla casi siempre.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** Un colega cita la ganancia de este laboratorio como la «del estándar CCSDS». ¿Qué corriges?

<details><summary>Solución comentada</summary>

Que es una estimación aproximada con BPSK ideal; del estándar solo se usaron los tamaños de bloque y el entrelazado.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *curva de decodificación de un código de bloque*: tabla de `P_bloque` para Hamming y RS, la ganancia de código y los bloques de la CCSDS, con qué es consultado y sintético.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: Hamming, Reed–Solomon y ganancia

El script [codigos.py](codigos.py) codifica y decodifica Hamming(7,4), simula `p = 0,02` con `random.Random(89)`, calcula la probabilidad de bloque de RS(255,223) y la ganancia de código, y lista los bloques de la CCSDS (**comprueba** que todo error único se corrige, que la simulación concuerda con la teoría a menos de 4 σ y que los `k` coinciden con la tabla consultada).

**Datos:** tabla 6-1 de CCSDS 131.0-B-5 (consultada); canal, `p` y semilla **sintéticos**. **Predice antes de ejecutar:** ¿cuántos errores corrige un Hamming(7,4)? (Uno.) **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
3.12.9 (biblioteca estandar), random.Random(89)
Hamming(7,4) sobre canal binario simetrico SINTETICO p = 0.02 (100000 bloques)
  P(bloque erroneo) simulada = 0.00786 ; teorica = 0.00786 ; z = 0.01
  BER de informacion = 0.00336 frente a 0.02000 sin codigo
Reed-Solomon (255,223), t = 16 simbolos: probabilidad de bloque no corregido segun p_simbolo
  p_s = 0.0100 -> P_bloque = 1.400e-09
  p_s = 0.0500 -> P_bloque = 1.414e-01
  p_s = 0.0627 -> P_bloque = 4.328e-01
  p_s = 0.0800 -> P_bloque = 8.146e-01
  p_s = 0.1000 -> P_bloque = 9.753e-01
  umbral t/n = 0.0627 ; tasa del codigo = 0.8745
Eb/N0 para BER 1e-5: sin codigo = 9.59 dB ; con RS(255,223) = 6.29 dB ; ganancia = 3.29 dB
CCSDS 131.0-B-5, tabla 6-1: profundidad I -> k bits (223 octetos x I) / n bits (255 octetos x I)
  I = 1: k = 1784 ; n = 2040
  I = 2: k = 3568 ; n = 4080
  I = 3: k = 5352 ; n = 6120
  I = 4: k = 7136 ; n = 8160
  I = 5: k = 8920 ; n = 10200
  I = 8: k = 14272 ; n = 16320
Pruebas superadas.
```

```bash
python programa/clases/B89/B89-C09-codificacion-correctora-de-errores/codigos.py
```

**Límites:** errores independientes, decodificación a distancia acotada, BPSK ideal; la ganancia es una aproximación; no se implementa el codificador RS.

## 18. Errores frecuentes y cómo corregirlos

**Creer que un código siempre ayuda.** Se corrige con 8.2: cerca y por encima de `t/n` falla.

**Ignorar el costo de la tasa en el `Eb/N0`.** Se corrige con 8.3.

**Confundir `n` y `k` al leer una tabla.** Se corrige con 8.4.

**Presentar la ganancia aproximada como la del estándar.** Se corrige con la sección 11.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué ganancia esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **curva de decodificación de un código de bloque** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Calcula `P_bloque` y la ganancia | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas con unidades | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con una segunda vía | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo sintético y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular el canal como sintético; usar solo la tabla CCSDS consultada; no presentar la ganancia aproximada como la del estándar; no presentar un cálculo como una medición; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y sus datos son sintéticos o ilustrativos; ningún resultado describe un enlace, un satélite ni una misión reales, ni sustituye a la documentación oficial de una misión, a un presupuesto de enlace verificado ni a la coordinación regulatoria.  Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

RS(255,223) ahorra unos `3,3 dB` en este modelo y el Hamming(7,4) baja el error de bloque a `0,0079`. Queda una pregunta: ¿cómo sabe el receptor cuándo empieza cada símbolo y dónde está la portadora?

**Glosario español–inglés.** código de bloque · *block code*; Reed–Solomon · *Reed–Solomon code*; entrelazado · *interleaving*; ganancia de codificación · *coding gain*; síndrome · *syndrome*.

**Continuidad.** [B89-C10](../B89-C10-sincronizacion-de-portadora/CLASE.md) estudia la sincronización de portadora.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B89-C08 — Modulación digital](../B89-C08-modulacion-digital/CLASE.md) · [📚 Bloque B89](../../../tronco-comun/B89-comunicaciones-y-navegacion-satelital.md) · [Siguiente: B89-C10 — Sincronización de portadora →](../B89-C10-sincronizacion-de-portadora/CLASE.md)
<!-- /nav -->
