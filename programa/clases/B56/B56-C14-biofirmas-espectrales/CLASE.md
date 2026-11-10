# B56-C14 — Biofirmas espectrales

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B56](../../../tronco-comun/B56-astrobiologia-y-vida-extraterrestre.md) · [← Anterior: B56-C13 — Biofirmas químicas](../B56-C13-biofirmas-quimicas/CLASE.md) · [Siguiente: B56-C15 — Falsos positivos de biofirmas →](../B56-C15-falsos-positivos-de-biofirmas/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 14 del bloque B56. Nivel N3. Tomas el tránsito planetario y la estadística del ruido ([B12](../../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md)) para calcular **cuán grande es la señal de una atmósfera en un tránsito y cuántos tránsitos hacen falta para detectarla**. Es una estimación de primer orden: no analizas espectros reales ni usas datos de ningún telescopio. La química de las biofirmas se vio en [C13](../B56-C13-biofirmas-quimicas/CLASE.md).

## 2. Por qué esta clase existe

Detectar un gas en la atmósfera de un planeta lejano exige acumular muchos tránsitos porque la señal es una fracción diminuta de la luz estelar. La decisión central: **dados el tamaño de la estrella y del planeta, la altura de escala y el ruido por tránsito, ¿cuántos tránsitos se necesitan para una relación señal/ruido dada?**

## 3. Lo que podrás hacer al terminar

1. Definir tránsito, profundidad, altura de escala y relación señal/ruido.
2. Calcular la profundidad `δ = (R_p/R_s)²` y verificarla por cuadratura.
3. Calcular la altura de escala `H = kT/(μ m_u g)` y la señal atmosférica `2 R_p n H/R_s²`.
4. Estimar el número de tránsitos con `N = (SNR σ/señal)²`.
5. Comprobar la ley `1/√N` con una simulación de semilla fija.
6. Nombrar qué deja fuera el modelo (nubes, manchas, ruido correlacionado).

La evidencia es el **presupuesto de señal a ruido** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es el radio de una estrella respecto del Sol?
2. ¿Qué es la desviación estándar de una media de `N` datos?
3. ¿Qué es la altura de escala (C11)?
4. ¿Qué es una cuadratura (regla de Simpson)?
5. ¿Qué es una ppm?

<details>
<summary>Ver respuestas</summary>

1. Un múltiplo del radio solar, `6,957 × 10⁸ m`. 2. `σ/√N`. 3. La altura en que la presión cae un factor `e`. 4. Una integral numérica. 5. Una parte por millón, `10⁻⁶`.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa B12 y [C11](../B56-C11-atmosfera-y-superficie-de-titan/CLASE.md).

## 5. Un caso real: el marco de las biofirmas

Schwieterman et al. (2018) revisan las biofirmas gaseosas, de superficie y temporales detectables remotamente, y herramientas para estimar la biomasa mínima que produce una señal (S1, solo resumen, consultado el 2026-11-09). Nuestro **ejemplo conductor sintético**: una enana M de `0,12 R☉`, un planeta de `1 R_⊕` con atmósfera de 29 g/mol a 250 K y `g = 9,8 m/s²`, una banda de 5 alturas de escala efectivas y ruido de 100 ppm por tránsito. No es un sistema real.

## 6. Vocabulario

El **tránsito** es el paso de un planeta frente a su estrella. La **profundidad** es la fracción de luz bloqueada. La **altura de escala** `H` mide el grosor de la atmósfera. La **señal atmosférica** es el exceso de profundidad por la luz que atraviesa la atmósfera. La **relación señal/ruido** (SNR) es señal dividida entre la desviación del ruido. Una **banda espectral** es un intervalo de longitudes de onda donde un gas absorbe.

## 7. Modelo mental: una moneda sobre una linterna

El planeta es una moneda que tapa una pequeña fracción de la linterna. La atmósfera es un anillo fino alrededor de la moneda; ese anillo es la señal.

```mermaid
flowchart LR
    A["R_s, R_p, T, μ, g"] --> B["δ y H"]
    B --> C["señal = 2 R_p n H / R_s²"]
    C --> D["N = (SNR·σ / señal)²"]
    D --> E["Tránsitos necesarios"]
```

*Descripción textual:* con los radios y la altura de escala se obtiene la señal atmosférica; con el ruido por tránsito y la SNR deseada, el número de tránsitos.

Analogía: oír un susurro en una fiesta repitiendo la pregunta varias veces. Su límite: el ruido real no siempre es blanco.

## 8. La explicación, paso a paso

### 8.1 Profundidad

`δ = (R_p/R_s)² = 5824 ppm` para `R_p = 6,371 × 10⁶ m` (valor **no consultado**, ilustrativo) y `R_s = 0,12 × 6,957 × 10⁸ m` (IAU, S2). La cuadratura da `5824 ppm` (diferencia < `10⁻⁴`).

### 8.2 Altura de escala

`H = kT/(μ m_u g) = 7,31 km` con `μ = 29`, `T = 250 K`, `g = 9,8 m/s²` (ilustrativos; `k` y `m_u` de NIST, S3).

### 8.3 Señal atmosférica

`2 R_p n H/R_s² = 66,9 ppm` con `n = 5` alturas de escala efectivas (ilustrativo). Es el 1,1 % de la profundidad total.

### 8.4 Número de tránsitos

Con ruido blanco de `σ = 100 ppm` por tránsito, `SNR = señal √N/σ`. Para SNR 3: `N = 21`; para SNR 5: `N = 56` tránsitos.

### 8.5 Ley `1/√N`

La simulación con semilla 2024 da desviaciones de la media de `100,7 ppm` (N = 1) y `20,2 ppm` (N = 25); el cociente es `4,99` (esperado 5, tolerancia 3 %). Lo que el modelo omite: nubes, manchas estelares, ruido correlacionado y oscurecimiento al limbo.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `R_s` | radio estelar | m | `0,12 × 6,957 × 10⁸` (S2; sintético) |
| `R_p` | radio planetario | m | `6,371 × 10⁶` (ilustrativo) |
| `δ` | profundidad | ppm | 5824 |
| `H` | altura de escala | km | 7,31 |
| `σ` | ruido por tránsito | ppm | 100 (sintético) |
| `N` | tránsitos | — | 21 (SNR 3); 56 (SNR 5) |

## 10. Convenciones y referencias

Ruido blanco gaussiano; estrella sin oscurecimiento al limbo; semilla 2024. Estrella, planeta, atmósfera y ruido **sintéticos**.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | Schwieterman et al., *Exoplanet Biosignatures: A Review of Remotely Detectable Signs of Life*, arXiv:1705.05791 | https://arxiv.org/abs/1705.05791 | Marco: biofirmas gaseosas, de superficie y temporales | Solo resumen, consultado el 2026-11-09 |
| S2 | Mamajek et al., *IAU 2015 Resolution B3*, arXiv:1510.07674 | https://arxiv.org/abs/1510.07674 | Radio solar nominal `6,957 × 10⁸ m` | Texto del PDF extraído el 2026-11-09 |
| S3 | NIST, *Fundamental Physical Constants — Complete Listing* (CODATA 2022) | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | `k`, unidad de masa atómica | Consultada el 2026-11-09 |

Límites: el radio terrestre no se consultó; todos los parámetros del sistema son sintéticos; no se usa ningún espectro real ni se afirma detectabilidad de ningún planeta.

## 12. Cómo ver el presupuesto

Equivalente accesible a una tabla:

| SNR objetivo | Tránsitos (σ = 100 ppm, señal 66,9 ppm) |
|---|---|
| 3 | 21 |
| 5 | 56 |

Descripción larga: duplicar la SNR objetivo cuadruplica el número de tránsitos.

## 13. Ejemplo trabajado: tránsitos para SNR 5 con ruido de 50 ppm

**Paso 1 · Datos.** Señal 66,9 ppm, `σ = 50 ppm`, SNR 5.

**Paso 2 · Razón.** `5 × 50/66,9 = 3,737`.

**Paso 3 · `N`.** `3,737² = 13,97`; `N = 14`.

**Paso 4 · Sentido.** Mitad de ruido, cuarta parte de tránsitos. Resultado sintético.

## 14. Distintos enfoques

**Estimación analítica (esta clase):** rápida. **Simulación con ruido correlacionado:** más realista. **Recuperación atmosférica con modelos:** infiere abundancias. Para dimensionar sirve la primera.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `R_p/R_s`. *Pasos:* `R_s = 8,348 × 10⁷ m`.

<details><summary>Solución comentada</summary>

`6,371 × 10⁶/8,348 × 10⁷ = 0,0763`; `δ = 5824 ppm` (8.1).
</details>

**Ejercicio 2 · con una pista.** Calcula `H` si `T = 300 K`. *Pista:* proporcional a `T`.

<details><summary>Solución comentada</summary>

`7,31 × 300/250 = 8,77 km`.
</details>

**Ejercicio 3 · casi autónomo.** Calcula la señal con `n = 3` alturas.

<details><summary>Solución comentada</summary>

`66,9 × 3/5 = 40,1 ppm`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Calcula `N` para SNR 3 con la señal del ejercicio 3.

<details><summary>Solución comentada</summary>

`(3 × 100/40,1)² = 56` tránsitos.
</details>

**Ejercicio 5.** ¿Por qué la señal crece con `H`?

<details><summary>Solución comentada</summary>

Porque una atmósfera más extensa bloquea una corona más gruesa (8.3).
</details>

**Ejercicio 6.** Si la estrella fuera como el Sol (`R_s = R☉`), ¿qué `δ`?

<details><summary>Solución comentada</summary>

`(6,371 × 10⁶/6,957 × 10⁸)² = 8,39 × 10⁻⁵ = 84 ppm`; la señal baja `1/0,12² = 69` veces.
</details>

**Ejercicio 7.** ¿Qué verifica la simulación de la ley `1/√N`?

<details><summary>Solución comentada</summary>

Que promediar `N` tránsitos reduce el ruido como `σ/√N` (8.5).
</details>

**Ejercicio 8.** ¿Qué pasa si hay un ruido sistemático de 30 ppm?

<details><summary>Solución comentada</summary>

No baja con `√N`; limita la SNR máxima (`señal/30 = 2,2` con 66,9 ppm).
</details>

**Ejercicio 9 · transferencia.** Un titular dice: «con unos pocos tránsitos se detectará vida en planetas como la Tierra». Respóndele.

<details><summary>Solución comentada</summary>

Depende del ruido, la estrella y las nubes; con los supuestos de la clase hacen falta decenas de tránsitos y el modelo omite sistemáticos (8.5).
</details>

**Ejercicio 10 · transferencia.** ¿Por qué se favorecen las enanas M?

<details><summary>Solución comentada</summary>

Su radio pequeño aumenta `δ` y la señal (ejercicio 6).
</details>

**Ejercicio 11 · transferencia.** ¿Qué cambia con una atmósfera de hidrógeno?

<details><summary>Solución comentada</summary>

`μ` baja y `H` sube mucho; la señal es mayor, pero no es el caso del ejemplo.
</details>

**Ejercicio 12 · integrador.** Elabora tu *presupuesto de señal a ruido*: elige radios, `T`, `μ`, `g`, `n` y `σ` (sintéticos), calcula `δ`, `H`, señal y `N` para SNR 3 y 5, y lista dos efectos omitidos.

<details><summary>Solución modelo</summary>

Con los del ejemplo: `δ = 5824`, `H = 7,31 km`, señal 66,9 ppm, `N = 21` y 56. Omitidos: nubes y ruido estelar correlacionado. Rotulado como sintético.
</details>

## 17. Laboratorio: señal de tránsito

El script [senal_de_transito.py](senal_de_transito.py) calcula `δ`, la cuadratura de la profundidad (`10⁻⁴`), `H`, la señal, `N` y la ley `1/√N` por simulación (semilla 2024, 3 %).

**Datos:** `k`, `m_u` de NIST; `R☉` de la IAU; todo lo demás sintético. **Predice antes de ejecutar:** ¿qué cociente de desviaciones da N = 1 frente a N = 25? (5.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Profundidad del tránsito = 5824 ppm ; por cuadratura = 5824 ppm
H = 7.31 km ; senal atmosferica (5 H) = 66.9 ppm
SNR 3 con ruido 100 ppm/transito -> N = 21 transitos
SNR 5 con ruido 100 ppm/transito -> N = 56 transitos
Desviacion de la media: N=1 -> 100.7 ppm ; N=25 -> 20.2 ppm ; cociente = 4.99 (esperado 5)
Pruebas superadas.
```

```bash
python programa/clases/B56/B56-C14-biofirmas-espectrales/senal_de_transito.py
```

**Límites:** ruido blanco, sin nubes ni manchas; no es la observación de ningún sistema.

## 18. Errores frecuentes y cómo corregirlos

**Confundir profundidad total y señal atmosférica.** Se corrige con la sección 8.3.

**Olvidar el cuadrado en `N`.** Se corrige con el ejemplo 13.

**Ignorar ruido sistemático.** Se corrige con el ejercicio 8.

**Presentar el sistema como real.** Se corrige con la sección 10.

**Usar `R_p/R_s` sin elevar al cuadrado.** Se corrige con el ejercicio 1.

## 19. Cómo sabrás que vas bien

Tras 8.3: ¿cuánto vale la señal? Ejercicios 3 y 4. Tras 8.4: ¿cómo escala `N`? Ejemplo 13. Tras el laboratorio: ¿qué verifica la simulación? (la ley `1/√N`).

## 20. Qué entregas y cómo se evalúa

El producto es tu **presupuesto de señal a ruido** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | `δ`, `H`, SNR claros | Discute sistemáticos |
| Cálculo | Sin unidades | Con errores | `N` correcto | Con simulación |
| Límites | Ninguno | Uno | Dos efectos | Cuantifica su efecto |
| Rótulos | Sin rotular | Parciales | Sintético rotulado | Declara lo no consultado |
| Fuentes | Sin fuente | Sin fecha | S1–S3 con fecha | Declara «solo resumen» |

**Condiciones críticas (no se compensan con promedio):** rotular todo el sistema como sintético; no afirmar detectabilidad real; citar solo lo consultado.

## 21. Ética, seguridad y límites

La clase es educativa; no analiza datos de ningún telescopio ni afirma detectar vida. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

La atmósfera de un planeta terrestre ante una enana M da una señal de unas decenas de ppm y exige decenas de tránsitos con ruido blanco; la realidad añade sistemáticos. Queda una pregunta: si se detecta una señal, ¿cómo se descarta que no sea vida?

**Glosario español–inglés.** tránsito · *transit*; profundidad · *transit depth*; altura de escala · *scale height*; relación señal/ruido · *signal-to-noise ratio*; banda espectral · *spectral band*.

**Continuidad.** [B56-C15](../B56-C15-falsos-positivos-de-biofirmas/CLASE.md) razona con probabilidades sobre los falsos positivos.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B56-C13 — Biofirmas químicas](../B56-C13-biofirmas-quimicas/CLASE.md) · [📚 Bloque B56](../../../tronco-comun/B56-astrobiologia-y-vida-extraterrestre.md) · [Siguiente: B56-C15 — Falsos positivos de biofirmas →](../B56-C15-falsos-positivos-de-biofirmas/CLASE.md)
<!-- /nav -->
