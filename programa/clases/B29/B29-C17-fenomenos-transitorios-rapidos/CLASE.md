# B29-C17 — Fenómenos transitorios rápidos

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B29](../../../tronco-comun/B29-astronomia-temporal-y-exoplanetas.md) · [← Anterior: B29-C16 — Supernovas y curvas de luz](../B29-C16-supernovas-y-curvas-de-luz/CLASE.md) · [Siguiente: B29-C18 — Redes de seguimiento temporal →](../B29-C18-redes-de-seguimiento-temporal/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 17 del bloque B29. Nivel N3. Los estallidos rápidos de radio duran milisegundos y llegan **dispersados** por el plasma: las frecuencias bajas se retrasan respecto de las altas. Aquí calculas la **constante de dispersión** desde constantes fundamentales, el retardo entre dos frecuencias, la **resolución en medida de dispersión**, el ensanchamiento dentro de un canal y recuperas la medida de dispersión de un pulso sintético con una **búsqueda por desdispersión**. Usas la dispersión de [B28-C01](../../B28/B28-C01-fundamentos-de-mensajeros-astronomicos/CLASE.md), estadística de [B12](../../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) y el ajuste de series de [B29-C14](../B29-C14-estrellas-variables-periodicas/CLASE.md). Se simula ruido blanco y un pulso gaussiano.

## 2. Por qué esta clase existe

La medida de dispersión informa de la distancia a la fuente y de la materia que atravesó. Sin desdispersión, un pulso breve se pierde entre canales. La decisión central: **¿qué retardo produce una medida de dispersión dada y con qué precisión se recupera por búsqueda?**

## 3. Lo que podrás hacer al terminar

1. Calcular `k_DM = e²/(8π²ε₀m_ec)` y compararla con `4148,8 s MHz² cm³/pc`.
2. Calcular el retardo entre dos frecuencias.
3. Estimar la resolución en `DM` y el ensanchamiento intra-canal.
4. Desdispersar desplazando canales y sumando.
5. Recuperar `DM` por máximo de la relación señal-ruido.
6. Reconocer las limitaciones de la simulación.

La evidencia es la **ficha de un pulso desdispersado** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es la medida de dispersión?
2. ¿Qué es un canal de frecuencia?
3. ¿Qué es la relación señal-ruido?
4. ¿Qué es la mediana de las desviaciones absolutas?
5. ¿Qué es una rejilla de trials?

<details>
<summary>Ver respuestas</summary>

1. La columna de electrones libres a lo largo de la visual. 2. Un intervalo estrecho de frecuencias. 3. El cociente entre la señal y el ruido. 4. Un estimador robusto de la dispersión. 5. Un conjunto de valores de prueba.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa B28-C01.

## 5. Un caso de contexto y un caso sintético

Lorimer y colaboradores descubrieron un estallido de `30 Jy` y duración menor de `5 ms` cuya dispersión implica una distancia menor de `1 Gpc` (S2, resumen); Petroff revisa los estallidos rápidos de radio (S3, resumen). Esta clase no usa esos datos: simula un pulso de `1,5 ms` con `DM = 300 pc/cm³` en la banda `1200–1500 MHz` con 32 canales. Es el **ejemplo conductor**.

## 6. Vocabulario

La **dispersión** retrasa las frecuencias bajas. La **medida de dispersión** (DM). La **desdispersión** corrige el retardo. El **ensanchamiento intra-canal** es el retardo dentro de un canal. La **resolución en DM** depende de la anchura del pulso. El **trial** es un valor de prueba de DM.

## 7. Modelo mental: una banda de corredores desfasados

Todos los corredores salen a la vez, pero los lentos (baja frecuencia) llegan después. Para ver la salida simultánea hay que adelantar a cada corredor lo que se retrasó: eso es desdispersar.

```mermaid
flowchart LR
    K["k_DM"] --> D["Δt = k DM (1/f₁² − 1/f₂²)"]
    D --> SHIFT["desplazar cada canal"]
    SHIFT --> SUM["sumar canales"]
    SUM --> SNR["SNR del máximo"]
    SNR --> BARR["barrido en DM → máximo"]
```

*Descripción textual:* la constante de dispersión y la medida de dispersión dan el retardo por canal; se desplazan los canales, se suman y se mide la relación señal-ruido; el máximo del barrido en `DM` da la medida recuperada.

Analogía: corredores desfasados. Límite: no se simula el ensanchamiento por dispersión dentro del canal.

## 8. La explicación, paso a paso

### 8.1 Constante y retardos

`k_DM = 4148,81 s MHz² cm³/pc`. Retardo entre `1200` y `1500 MHz`: `103,7 ms` (`DM = 100`), `311,2 ms` (`300`), `1037,2 ms` (`1000`).

### 8.2 Resolución y ensanchamiento

Para un pulso de `1,5 ms` en la banda completa, la resolución en `DM` es `1,45 pc/cm³`. El ensanchamiento intra-canal (`9,38 MHz`, `DM = 300`) sería `9,485 ms`, mayor que el pulso: la simulación no lo incluye, lo que la hace optimista.

### 8.3 Un barrido

Con una realización: la SNR en `DM = 300` es `6,87`; el máximo cae en `DM = 299` con `SNR = 7,56`; sin desdispersar (`DM = 0`) la SNR es `3,25`.

### 8.4 Monte Carlo

En 25 realizaciones: `DM` recuperada `300,64 ± 2,76`, con error máximo menor de `8 pc/cm³`.

### 8.5 Lectura

La desdispersión recupera la medida de dispersión con una incertidumbre de pocos `pc/cm³` y más que duplica la relación señal-ruido. Un pulso real sería más ancho por la dispersión intra-canal, lo que reduce la resolución.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `k_DM` | constante de dispersión | s MHz² cm³/pc | 4148,81 |
| `DM` | medida de dispersión | pc/cm³ | 300 (sintética) |
| banda | frecuencias | MHz | 1200–1500 |
| canales | número | — | 32 |
| ancho | del pulso | ms | 1,5 |
| `δDM` | resolución | pc/cm³ | 1,45 |

## 10. Convenciones y referencias

Retardo respecto de la frecuencia superior; ruido gaussiano blanco; pulso gaussiano; semilla `20261109`; todos los parámetros son **ilustrativos**.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NIST (`c`, `e`, `m_e`, `ε₀`) e IERS TN36 (`au`) | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | constante de dispersión | Consultadas el 2026-11-09 |
| S2 | Lorimer et al., arXiv:0709.4301 | https://arxiv.org/abs/0709.4301 | `30 Jy`; `< 5 ms`; `< 1 Gpc` | Solo resumen, consultado el 2026-11-09 |
| S3 | Petroff et al., arXiv:1904.07947 | https://arxiv.org/abs/1904.07947 | revisión de estallidos rápidos de radio | Solo resumen, consultado el 2026-11-09 |

Límites: S2 y S3 solo resumen; ningún dato real se usa; la simulación omite la dispersión intra-canal.

## 12. Cómo ver el barrido

| DM trial | SNR (una realización) |
|---|---|
| 250–290 | 3–4 |
| 300 | 6,87 |
| 310–350 | 3–4 |

Descripción larga: la SNR forma un pico estrecho alrededor de la `DM` verdadera.

## 13. Ejemplo trabajado: retardo

**Paso 1 · Frecuencias.** `1/1200² − 1/1500² = 6,944 × 10⁻⁷ − 4,444 × 10⁻⁷ = 2,5 × 10⁻⁷ MHz⁻²`.

**Paso 2 · Producto.** `4148,81 × 300 × 2,5 × 10⁻⁷ = 0,3112 s`.

**Paso 3 · Resultado.** `311,2 ms`.

**Paso 4 · Sentido.** Cien veces mayor que la duración del pulso.

## 14. Distintas formas de describir el pulso

**Por retardo:** `Δt`. **Por DM:** columna de electrones. **Por SNR:** tras la desdispersión. **Por resolución:** `δDM`.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Retardo con `DM = 100`. *Pasos:* proporcional.

<details><summary>Solución comentada</summary>

`103,7 ms`.
</details>

**Ejercicio 2 · con una pista.** Retardo con `DM = 1000`.

<details><summary>Solución comentada</summary>

`1037,2 ms`.
</details>

**Ejercicio 3 · casi autónomo.** Resolución en `DM` para un pulso de `3 ms`.

<details><summary>Solución comentada</summary>

`2,9 pc/cm³`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Mejora de la SNR por desdispersar.

<details><summary>Solución comentada</summary>

`7,56/3,25 = 2,3`.
</details>

**Ejercicio 5.** Error de la DM media recuperada.

<details><summary>Solución comentada</summary>

`0,64 pc/cm³`.
</details>

**Ejercicio 6.** Error de la media (`2,76/√25`).

<details><summary>Solución comentada</summary>

`0,55 pc/cm³`; el sesgo `0,64` es `1,2` errores.
</details>

**Ejercicio 7.** Retardo entre `1200` y `1500 MHz` para `DM = 30`.

<details><summary>Solución comentada</summary>

`31,1 ms`.
</details>

**Ejercicio 8.** Ensanchamiento intra-canal con canales de la mitad de ancho.

<details><summary>Solución comentada</summary>

La mitad: `4,74 ms`.
</details>

**Ejercicio 9 · transferencia.** Un compañero dice que la simulación predice la SNR real de un FRB. Responde con 8.2.

<details><summary>Solución comentada</summary>

No: omite el ensanchamiento intra-canal, que es mayor que el pulso, y por tanto es optimista.
</details>

**Ejercicio 10 · transferencia.** ¿Por qué se desplaza cada canal?

<details><summary>Solución comentada</summary>

Para alinear el pulso y sumarlo coherentemente, lo que aumenta la SNR.
</details>

**Ejercicio 11 · transferencia.** ¿Qué valida el Monte Carlo?

<details><summary>Solución comentada</summary>

Que la búsqueda recupera la DM inyectada; no que un estallido real se parezca a la simulación.
</details>

**Ejercicio 12 · integrador.** Elabora tu *ficha de un pulso desdispersado*: constante, retardos, resolución, barrido y recuperación.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4.
</details>

## 17. Laboratorio: desdispersión

El script [desdispersion.py](desdispersion.py) calcula la constante (**comprueba** 0,5 %), sintetiza el pulso y recupera `DM` (**comprueba** 8 pc/cm³).

**Datos:** constantes de NIST/IERS; todo lo demás **ilustrativo**. **Predice antes de ejecutar:** ¿qué DM se recupera? (≈300.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
k_DM = e^2/(8 pi^2 epsilon_0 m_e c) = 4148.81 s MHz^2 cm^3/pc
DM =    100 pc/cm3: retardo entre 1200 y 1500 MHz =    103.7 ms
DM =    300 pc/cm3: retardo entre 1200 y 1500 MHz =    311.2 ms
DM =   1000 pc/cm3: retardo entre 1200 y 1500 MHz =   1037.2 ms
resolucion en DM para un pulso de 1.5 ms en la banda completa: ~1.45 pc/cm3
ensanchamiento intra-canal (9.38 MHz, DM = 300, f centrales): 9.485 ms
 DM trial      SNR
    250.0     4.05
    260.0     3.14
    270.0     3.44
    280.0     3.65
    290.0     4.19
    300.0     6.87
    310.0     4.29
    320.0     3.46
    330.0     3.17
    340.0     3.97
    350.0     3.07
maximo en DM = 299.0 con SNR = 7.56 ; SNR sin desdispersar (DM = 0) = 3.25
25 realizaciones: DM recuperada = 300.64 +/- 2.76 (verdadera 300.0)
Pruebas superadas.
```

```bash
python programa/clases/B29/B29-C17-fenomenos-transitorios-rapidos/desdispersion.py
```

**Límites:** sin dispersión intra-canal, sin dispersión de scattering, ruido blanco.

## 18. Errores frecuentes y cómo corregirlos

**Confundir retardo y DM.** Se corrige con el ejercicio 1.

**Ignorar el ensanchamiento.** Se corrige con el ejercicio 9.

**Usar frecuencias en GHz con la constante en MHz.** Se corrige con la sección 9.

**Esperar resolución mejor que la del pulso.** Se corrige con el ejercicio 3.

**Tomar la simulación por real.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras 8.1: ¿cuánto retrasa `DM = 300`? Si dudas, ejemplo 13. Tras 8.3: ¿cuánto sube la SNR? Ejercicio 4. Tras el laboratorio: ¿qué valida? (la recuperación).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de un pulso desdispersado** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Retardo, DM, desdispersión | Explica el ensanchamiento |
| Cálculo | Sin unidades | Con errores | Tablas completas | Calcula resolución |
| Numérico | Sin comprobar | Un caso | Monte Carlo | Interpreta errores |
| Fuentes | Sin fuente | Sin fecha | S1–S3 con fecha | Declara S2–S3 como resumen |
| Límites | No los nombra | Uno | Tres | Discute scattering |

**Condiciones críticas (no se compensan con promedio):** rotular la simulación como sintética; no usar cifras no consultadas; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: no es una canalización de búsqueda de pulsos. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

El retardo de dispersión es `k_DM DM (1/f₁² − 1/f₂²)` (`311 ms` para `DM = 300` en 1200–1500 MHz) y la desdispersión recupera la medida con `~3 pc/cm³` de error. Queda una pregunta: ¿cómo se organizan los telescopios para seguir estos eventos?

**Glosario español–inglés.** transitorio rápido · *fast transient*; estallido rápido de radio · *fast radio burst*; medida de dispersión · *dispersion measure*; desdispersión · *dedispersion*; ensanchamiento intra-canal · *intra-channel smearing*; barrido en DM · *DM trial search*.

**Continuidad.** [B29-C18](../B29-C18-redes-de-seguimiento-temporal/CLASE.md) estudia las redes de seguimiento temporal.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B29-C16 — Supernovas y curvas de luz](../B29-C16-supernovas-y-curvas-de-luz/CLASE.md) · [📚 Bloque B29](../../../tronco-comun/B29-astronomia-temporal-y-exoplanetas.md) · [Siguiente: B29-C18 — Redes de seguimiento temporal →](../B29-C18-redes-de-seguimiento-temporal/CLASE.md)
<!-- /nav -->
