# B46-C10 — Radioastronomía mediante SDR

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B46](../../../tronco-comun/B46-radioastronomia-e-interferometria.md) · [← Anterior: B46-C09 — Conversión analógica digital](../B46-C09-conversion-analogica-digital/CLASE.md) · [Siguiente: B46-C11 — Observación de hidrógeno a 21 centímetros →](../B46-C11-observacion-de-hidrogeno-a-21-centimetros/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 10 del bloque B46. Nivel N3. Una radio definida por software (SDR) permite montar un espectrómetro modesto. Aquí simulas muestras I/Q con ruido y un tono, calculas el espectro con una FFT ventaneada de Hann, lo promedias y verificas la caída `1/√M` del ruido y el **ancho de banda equivalente de ruido** de la ventana. Usas [B46-C06](../B46-C06-ruido-de-sistema-y-radiometria/CLASE.md) y [B46-C09](../B46-C09-conversion-analogica-digital/CLASE.md). Los datos son sintéticos.

## 2. Por qué esta clase existe

Promediar espectros es la forma práctica de aplicar la ecuación del radiómetro con un instrumento barato, pero la ventana cambia el ancho de banda efectivo. La decisión central: **¿cuántos espectros promediar para detectar una línea débil?**

## 3. Lo que podrás hacer al terminar

1. Calcular un espectro de potencia con FFT y ventana.
2. Obtener el ENBW de la ventana de Hann.
3. Promediar `M` espectros.
4. Verificar la caída `1/√M`.
5. Medir la relación pico–ruido.
6. Reconocer los límites de un SDR real.

La evidencia es la **ficha del espectrómetro SDR** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es una incertidumbre?
2. ¿Qué es una simulación Monte Carlo?
3. ¿Qué es una tabla de resultados?
4. ¿Qué es un valor ilustrativo?
5. ¿Qué es una verificación?

<details>
<summary>Ver respuestas</summary>

1. Un intervalo en que se espera el valor verdadero. 2. Repetir con números aleatorios de semilla fija. 3. Un resumen ordenado de cálculos. 4. Un valor propuesto para el ejemplo, no medido. 5. Comparar un cálculo con un caso independiente.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Con `fs = 2,4 MHz` y `N = 1024` la resolución es `2343,75 Hz`; el ENBW de Hann vale `1,5000` bines; la dispersión relativa de un canal pasa de `0,963` con `M = 1` a `0,128` con `M = 64`. Es el **ejemplo conductor**; los datos son **sintéticos**.

## 6. Vocabulario

Las muestras **I/Q** son la parte real e imaginaria de la señal en banda base. La **FFT** da el espectro. La **ventana de Hann** reduce la fuga espectral. El **ENBW** es el ancho de un filtro rectangular con el mismo ruido. El **promediado** de `M` espectros reduce la dispersión como `1/√M`.

## 7. Modelo mental: muchas fotos del mismo cielo

Como sumar muchas fotos de exposición corta: cada una es ruidosa, pero la suma deja ver lo constante.

```mermaid
flowchart LR
    IQ["muestras I/Q"] --> W["ventana de Hann"]
    W --> F["FFT 1024"]
    F --> P["|X|2"]
    P --> M["promedio de M espectros"]
    M --> R["sigma/media = 1/sqrt(M)"]
```

*Descripción textual:* las muestras se ventanean, se transforman, se elevan al cuadrado y se promedian, con una dispersión que baja como `1/√M`.

Analogía: muchas fotos del mismo cielo. Límite: ruido blanco, sin desbalance I/Q ni espurios.

## 8. La explicación, paso a paso

### 8.1 Resolución y ventana

`Δf = fs/N = 2343,75 Hz`. El ENBW de la ventana de Hann es `N Σw²/(Σw)² = 1,5000` bines (`3,5 kHz` de ruido por canal).

### 8.2 Promediado

| `M` | media del ruido | `σ/media` | `1/√M` | pico/ruido |
|---|---|---|---|---|
| 1 | 377,20 | 0,9626 | 1,0000 | 199,9 |
| 4 | 384,09 | 0,4992 | 0,5000 | 168,3 |
| 16 | 388,37 | 0,2562 | 0,2500 | 160,0 |
| 64 | 386,45 | 0,1279 | 0,1250 | 160,3 |

El tono (en el canal 51) sobresale `160` veces del ruido medio.

### 8.3 Lectura

El ruido por canal es exponencial (`σ/media = 1` con `M = 1`) y se vuelve gaussiano al promediar. Un SDR real tiene pico de continua, desbalance I/Q, ganancia inestable y espurios que el laboratorio no modela.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `fs` | frecuencia de muestreo | Hz | 2,4 × 10⁶ (ilustrativa) |
| `N` | tamaño de FFT | — | 1024 |
| `M` | espectros promediados | — | 1 a 64 |
| ENBW | ancho de ruido de la ventana | bines | 1,5000 |

## 10. Convenciones y referencias

Muestras **sintéticas** (semilla `20261109`); sin datos externos.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| — | Estándar o texto de radioastronomía no consultado | — | relaciones habituales de la disciplina que el laboratorio verifica por cálculo | No se consultó para esta clase |

Límites: no se midió con ningún SDR real.

## 12. Cómo ver las cifras

| Magnitud | Valor |
|---|---|
| resolución | 2343,75 Hz |
| ENBW Hann | 1,5000 bines |
| `σ/media` (M = 64) | 0,1279 |
| pico/ruido (M = 64) | 160,3 |

Descripción larga: el ruido baja con la raíz del número de espectros.

## 13. Ejemplo trabajado: el promediado

**Paso 1 · Dispersión inicial.** `σ/media = 1`.

**Paso 2 · Promedio.** Con `M = 16` se espera `1/√16 = 0,25`.

**Paso 3 · Simulación.** `0,2562`.

**Paso 4 · Acuerdo.** Dentro del 3 %.

## 14. Distintas formas de describir un espectrómetro

**Por FFT:** canales. **Por ventana:** ENBW. **Por promedio:** `1/√M`. **Por razón:** pico sobre ruido.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Resolución con `fs = 2,4 MHz` y `N = 2048`. *Pasos:* `fs/N`.

<details><summary>Solución comentada</summary>

`1171,88 Hz`.
</details>

**Ejercicio 2 · con una pista.** `σ/media` con `M = 100`. *Pasos:* `1/√100`.

<details><summary>Solución comentada</summary>

`0,1`.
</details>

**Ejercicio 3 · casi autónomo.** `M` para `σ/media = 0,01`. *Pasos:* `1/0,01²`.

<details><summary>Solución comentada</summary>

`10 000`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** ENBW en Hz de Hann con `Δf = 2343,75 Hz`.

<details><summary>Solución comentada</summary>

`3515,6 Hz`.
</details>

**Ejercicio 5.** Tiempo de una FFT de 1024 muestras a 2,4 MHz.

<details><summary>Solución comentada</summary>

`426,7 µs`.
</details>

**Ejercicio 6.** Tiempo para `M = 64` espectros sin solape.

<details><summary>Solución comentada</summary>

`27,31 ms`.
</details>

**Ejercicio 7.** ¿Qué pasa con el ruido si se cuadruplican los espectros?

<details><summary>Solución comentada</summary>

Se reduce a la mitad.
</details>

**Ejercicio 8.** ¿Cuál es el ENBW de la ventana rectangular?

<details><summary>Solución comentada</summary>

1 bin.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** ¿Por qué usar ventana?

<details><summary>Solución comentada</summary>

Para reducir la fuga de un tono fuerte a canales vecinos.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Por qué aparece un pico en el canal central de un SDR real?

<details><summary>Solución comentada</summary>

Por el desfase de continua del convertidor.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Cómo se relaciona con `σ = T_sys/√(Bτ)`?

<details><summary>Solución comentada</summary>

El ENBW por canal y el tiempo total dan el `Bτ`.
</details>

**Ejercicio 12.** **Integrador.** Elabora tu *ficha del espectrómetro SDR*: resolución, ENBW y tabla del promediado.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.2.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha del espectrómetro SDR*: resolución, ENBW y tabla del promediado.

<details><summary>Solución modelo</summary>

Secciones 8.1–8.2.
</details>

## 17. Laboratorio: espectrómetro por promedio

El script [sdr.py](sdr.py) simula I/Q, calcula el espectro y verifica la caída `1/√M` (**comprueba** `ENBW = 1,5` y la dispersión).

**Datos:** muestras **sintéticas**, semilla `20261109`. **Predice antes de ejecutar:** ¿cuánto valdrá `σ/media` con `M = 16`? (≈0,25.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
resolucion = 2343.75 Hz por canal ; ENBW de Hann = 1.5000 bines ; canal del tono = 51
   M  media ruido  sigma/media  1/sqrt(M)  pico/ruido
   1      377.203       0.9626     1.0000       199.9
   4      384.094       0.4992     0.5000       168.3
  16      388.374       0.2562     0.2500       160.0
  64      386.449       0.1279     0.1250       160.3
Pruebas superadas.
```

```bash
python programa/clases/B46/B46-C10-radioastronomia-mediante-sdr/sdr.py
```

**Límites:** ruido blanco, sin defectos de hardware.

## 18. Errores frecuentes y cómo corregirlos

**Olvidar el ENBW.** Se corrige con 8.1.

**Promediar amplitudes en vez de potencias.** Se corrige con 8.2.

**Esperar `1/√M` con deriva de ganancia.** Se corrige con 8.3.

**Presentar los datos como de un SDR real.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha del espectrómetro SDR** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | conceptos de la clase | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con el análisis | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | fuentes con fecha | Declara lo ilustrativo |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular lo sintético; no atribuir sensibilidades a un SDR real; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Con 64 espectros la dispersión baja a 0,128. Queda una pregunta: ¿qué línea espectral merece este instrumento?

**Glosario español–inglés.** SDR · *software-defined radio*; ventana · *window*; promediado · *averaging*; fuga espectral · *spectral leakage*.

**Continuidad.** [B46-C11](../B46-C11-observacion-de-hidrogeno-a-21-centimetros/CLASE.md) estudia la observación de hidrógeno a 21 centímetros.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B46-C09 — Conversión analógica digital](../B46-C09-conversion-analogica-digital/CLASE.md) · [📚 Bloque B46](../../../tronco-comun/B46-radioastronomia-e-interferometria.md) · [Siguiente: B46-C11 — Observación de hidrógeno a 21 centímetros →](../B46-C11-observacion-de-hidrogeno-a-21-centimetros/CLASE.md)
<!-- /nav -->
