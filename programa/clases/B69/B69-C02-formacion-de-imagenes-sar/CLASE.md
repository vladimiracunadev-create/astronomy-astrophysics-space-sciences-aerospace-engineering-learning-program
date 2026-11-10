# B69-C02 — Formación de imágenes SAR

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B69](../../../tronco-comun/B69-radar-de-apertura-sintetica-e-interferometria-profundizacion.md) · [← Anterior: B69-C01 — Principio Doppler y resolución en azimut del SAR](../B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md) · [Siguiente: B69-C03 — Ruido speckle y filtrado en imágenes SAR →](../B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 2 del bloque B69. Nivel N3. Un SAR no registra una imagen: registra ecos crudos que hay que **comprimir** en alcance y en azimut. Aquí simulas los ecos de tres blancos puntuales con un chirp de 56 MHz y la historia de fase de B69-C01, formas la imagen, mides su resolución y su lóbulo lateral, y ves por qué hay que corregir la **migración de celda**. Usas [B69-C01](../B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md). Todo es **sintético**.

## 2. Por qué esta clase existe

Sin procesamiento, un eco crudo parece ruido. La decisión central: **¿qué operaciones convierten el eco crudo en una imagen con la resolución teórica, y cuándo fallan?**

## 3. Lo que podrás hacer al terminar

1. Describir el eco crudo como la suma de réplicas del chirp con fase Doppler.
2. Comprimir en alcance con un filtro adaptado y obtener la resolución `c/2B`.
3. Comprimir en azimut con una referencia hiperbólica por celda de alcance.
4. Calcular la migración de celda y comparar con la celda de alcance.
5. Corregir la migración en el dominio alcance–Doppler y medir su efecto.
6. Medir anchuras a −3 dB y el nivel del lóbulo lateral (PSLR).

La evidencia es la **ficha de la formación de la imagen** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es un chirp?
2. ¿Qué es una convolución o correlación con un filtro adaptado?
3. ¿Qué es la transformada de Fourier discreta?
4. ¿Qué es un pixel y qué es la resolución?
5. ¿Qué es una verificación?

<details>
<summary>Ver respuestas</summary>

1. Un pulso cuya frecuencia varía linealmente con el tiempo. 2. Una operación que concentra la energía de una señal conocida en un pico. 3. Una descomposición de una señal en frecuencias, calculable con la FFT. 4. El pixel es el espaciado de la imagen; la resolución es la separación mínima de dos blancos distinguibles. 5. Comparar un cálculo con un caso independiente.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Con B = 56 MHz, duración 10 µs, fs = 64 MHz y la geometría de B69-C01, la celda de alcance es `c/2B = 2,677 m` y la migración a lo largo de la apertura es 2,273 m (0,85 celdas). La imagen de tres blancos reproduce sus posiciones y su resolución: 2,372 m en alcance y 5,317 m en azimut. Es el **ejemplo conductor**. Todo es **ilustrativo**.

## 6. Vocabulario

El **chirp** es el pulso transmitido. La **compresión en alcance** es el filtro adaptado en el tiempo rápido; la **compresión en azimut** lo es en el tiempo lento. La **migración de celda** es el desplazamiento del eco entre celdas de alcance durante la apertura. La **RCMC** es su corrección. El **PSLR** es la razón entre el mayor lóbulo lateral y el pico principal.

## 7. Modelo mental: dos enfocados sucesivos

Como enfocar una cámara en dos pasos: primero se enfoca en una dirección (alcance), luego en la otra (azimut). Cada paso comprime la energía dispersa de un blanco en un pico.

```mermaid
flowchart LR
    RAW["eco crudo"] --> RC["compresión en alcance"]
    RC --> RCMC["corrección de migración (RCMC)"]
    RCMC --> AC["compresión en azimut"]
    AC --> IMG["imagen compleja"]
```

*Descripción textual:* el eco crudo se comprime en alcance, se corrige la migración de celda y se comprime en azimut para obtener la imagen compleja.

Analogía: enfocar en dos pasos. Límite: aquí los dos ejes son independientes solo porque se corrige la migración.

## 8. La explicación, paso a paso

### 8.1 Eco crudo

Cada blanco devuelve una réplica del chirp con retardo `2R(t)/c` y fase `−4πR(t)/λ`. Los ecos de los tres blancos se suman.

### 8.2 Compresión en alcance

El filtro adaptado en frecuencia da un pico de anchura `0,886 c/(2B) = 2,372 m` a −3 dB; el laboratorio mide 2,372 m.

### 8.3 Migración de celda

Durante la apertura la distancia cambia `ΔR = √(R₀² + (vT/2)²) − R₀ = 2,273 m`, que es 0,85 celdas de alcance. Si no se corrige, la energía de un blanco se reparte en varias celdas y la compresión en azimut integra menos aperturas útiles.

### 8.4 Corrección y compresión en azimut

En el dominio alcance–Doppler la migración es `ΔR(f_D) = λ²R₀f_D²/(8v²)`; se desplaza cada línea en esa cantidad y luego se comprime con la referencia hiperbólica de cada celda. Sin la corrección, la anchura en azimut es 6,502 m; con ella, 5,317 m, que coincide con `0,886 v/Ba = 5,316 m`: la migración ensanchaba la respuesta un 22 %.

### 8.5 Calidad del pico

Sin ventana, la respuesta es un sinc con lóbulo lateral de −13,26 dB; el laboratorio mide −13,27 dB en alcance y −13,23 dB en azimut. Una ventana espectral baja ese nivel a costa de ensanchar el pico (no se verifica en este laboratorio).

### 8.6 Lectura

La imagen reproduce las posiciones (separaciones dentro de 1 pixel) y las amplitudes relativas dentro de un 6 % (0,676 y 0,493 frente a 0,7 y 0,5). Los blancos son puntuales y sin ruido; una escena real tendría blancos distribuidos, ruido y una órbita no ideal.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `B` | ancho de banda del chirp | Hz | 56 × 10⁶ |
| `τ` | duración del chirp | s | 10 × 10⁻⁶ |
| `fs` | muestreo en alcance | Hz | 64 × 10⁶ |
| `c` | velocidad de la luz | m/s | 299 792 458 (definición SI) |
| `ΔR` | migración de celda | m | 2,273 |
| pixel de alcance | `c/2fs` | m | 2,342 |
| pixel de azimut | `v/PRF` | m | 4,176 |
| PSLR | lóbulo lateral | dB | −13,26 (sinc) |

## 10. Convenciones y referencias

Alcance oblicuo `r` respecto del inicio de la ventana; azimut `x = vt` respecto del centro del bloque. Fase `−4πR/λ`. Versiones: Python 3.12.9, numpy 2.4.4. Tolerancias: posiciones 1 pixel; anchuras 5 %; amplitudes 6 %; PSLR ±0,7 dB.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA Earthdata, «Synthetic Aperture Radar (SAR)» | https://www.earthdata.nasa.gov/learn/earth-observation-data-basics/sar | describe en términos generales que un SAR combina adquisiciones sucesivas y distingue la resolución espacial del tamaño del pixel (página divulgativa; consultada completa el 2026-11-09) | Consultada |

Límites: la fuente es divulgativa; el algoritmo (alcance–Doppler con corrección de migración) se verifica en el laboratorio y no se consultó una fuente técnica para él.

## 12. Cómo ver la respuesta del sistema

| Magnitud | Valor |
|---|---|
| anchura en alcance | 2,372 m |
| anchura en azimut con RCMC | 5,317 m |
| anchura en azimut sin RCMC | 6,502 m |
| PSLR alcance / azimut | −13,27 / −13,23 dB |

Descripción larga: tres puntos brillantes en posiciones conocidas; el ensanchamiento en azimut sin RCMC es del 22 %.

## 13. Ejemplo trabajado: la migración en el borde de la apertura

**Paso 1 · Doppler en el borde.** `f_D = Ba/2 = 591,65 Hz`.

**Paso 2 · Migración.** `ΔR = λ²R₀f_D²/(8v²) = 0,0555² × 850 000 × 591,65² /(8 × 7100²) = 2,273 m`.

**Paso 3 · En celdas.** `2,273/2,677 = 0,85` celdas.

## 14. Distintas formas de abordar el problema

**Por separado:** alcance y azimut como dos correlaciones. **Por dominio:** alcance–Doppler con RCMC. **Por el laboratorio:** con y sin RCMC se compara la anchura.

## 15. Práctica guiada

**Ejercicio 1 · guiado.** Calcula la celda de alcance `c/2B`. *Pasos:* sección 8.2.

<details><summary>Solución comentada</summary>

`299 792 458/(2 × 56 × 10⁶) = 2,677 m`.
</details>

**Ejercicio 2 · guiado.** Calcula la anchura a −3 dB en alcance. *Pista:* factor 0,886.

<details><summary>Solución comentada</summary>

`0,886 × 2,677 = 2,372 m`.
</details>

**Ejercicio 3 · guiado.** Calcula el pixel de alcance `c/2fs`. *Casi autónomo.*

<details><summary>Solución comentada</summary>

`299 792 458/(128 × 10⁶) = 2,342 m`.
</details>


## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Calcula el pixel de azimut `v/PRF` y cuántos pixeles hay por resolución.

<details><summary>Solución comentada</summary>

`7100/1700 = 4,176 m`; `5,317/4,176 = 1,27` pixeles.
</details>

**Ejercicio 5 · autónomo.** Calcula la migración en el borde de la apertura.

<details><summary>Solución comentada</summary>

2,273 m (ejemplo 13).
</details>

**Ejercicio 6 · autónomo.** ¿Cuánto ensancha la migración no corregida la respuesta de azimut?

<details><summary>Solución comentada</summary>

`6,502/5,317 = 1,22`: 22 %.
</details>

**Ejercicio 7 · autónomo.** Dos blancos separados 150 m en azimut: ¿cuántos pixeles los separan?

<details><summary>Solución comentada</summary>

`150/4,176 = 35,9` pixeles (el laboratorio mide 36).
</details>

**Ejercicio 8 · autónomo.** ¿A qué amplitud corresponde un PSLR de −13,26 dB?

<details><summary>Solución comentada</summary>

`10^(−13,26/20) = 0,217` del pico.
</details>

**Ejercicio 9 · transferencia.** Si la migración fuera de 3 celdas, ¿qué esperarías sin RCMC?

<details><summary>Solución comentada</summary>

Un ensanchamiento y una pérdida de amplitud mayores, porque la energía de cada blanco se reparte en más celdas; habría que corregirla siempre.
</details>

**Ejercicio 10 · transferencia.** Una referencia de azimut calculada para R₀ pero aplicada a un blanco 1 km más lejos: ¿qué error de fase de segundo orden aparece? Usa `π ΔKa (T/2)²`.

<details><summary>Solución comentada</summary>

`ΔKa/Ka = 1/850 = 1,18 × 10⁻³`, `ΔKa = 2,51 Hz/s`, error `π × 2,51 × 0,0767 = 0,60 rad`: por eso la referencia se calcula por celda de alcance.
</details>

**Ejercicio 11 · transferencia.** Un colega afirma que bajar el lóbulo lateral no cuesta resolución. Responde.

<details><summary>Solución comentada</summary>

Una ventana espectral reduce los lóbulos laterales pero ensancha el pico principal; el sinc sin ventana es el caso de mejor resolución.
</details>

**Ejercicio 12 · integrador.** Elabora tu *ficha de la formación de la imagen*: tabla de celdas, migración, anchuras con y sin RCMC, PSLR y posiciones de los tres blancos.

<details><summary>Solución modelo</summary>

Secciones 8.1–8.6 y los resultados de la sección 17.
</details>


## 17. Laboratorio: simulación de ecos y formación de la imagen

El script [formacion_imagen.py](formacion_imagen.py) simula los ecos crudos de tres blancos, los comprime en alcance y azimut con y sin corrección de migración y mide posiciones, amplitudes, anchuras y PSLR (**comprueba** posiciones a 1 pixel, anchuras al 5 % y PSLR a ±0,7 dB).

**Datos:** sin datos observados; tres blancos **sintéticos** con amplitudes 1, 0,7 y 0,5; semilla no necesaria (sin azar). **Predice antes de ejecutar:** ¿la anchura en azimut con migración sin corregir será mayor o menor que la teórica? (mayor.) **Ejecución del 2026-11-09 (Python 3.12.9, numpy 2.4.4):**

```text
Python 3.12.9 ; numpy 2.4.4
Migracion de celda = 2.273 m ; celda de alcance c/2B = 2.677 m ; cociente = 0.85
Pixel de alcance = 2.342 m ; pixel de azimut = 4.176 m
Picos (indice azimut, indice alcance, amplitud relativa al maximo):
  ( 553,  128)  1.000
  ( 589,  256)  0.707
  ( 505,  192)  0.456
Amplitudes interpoladas relativas: 1.000, 0.676, 0.493
  separacion del pico 2: azimut +36 pix (esperado +35.9) ; alcance +128 pix (esperado +128.1)
  separacion del pico 3: azimut -48 pix (esperado -47.9) ; alcance +64 pix (esperado +64.0)
Anchura a -3 dB en alcance = 2.372 m (teorica 0.886 c/2B = 2.372 m)
Anchura a -3 dB en azimut  = 5.317 m (teorica 0.886 v/Ba = 5.316 m)
Anchura de azimut SIN correccion de migracion = 6.502 m ; CON correccion = 5.317 m
PSLR alcance = -13.27 dB ; azimut = -13.23 dB (sinc teorico -13.26 dB)
Pruebas superadas.
```

```bash
python programa/clases/B69/B69-C02-formacion-de-imagenes-sar/formacion_imagen.py
```

**Límites:** blancos puntuales, sin ruido, antena uniforme y órbita rectilínea.

## 18. Errores frecuentes y cómo corregirlos

**Comprimir en azimut sin corregir la migración.** Se corrige con 8.3–8.4.

**Confundir pixel con resolución.** Se corrige con la sección 9.

**Pensar que el eco crudo ya es una imagen.** Se corrige con 8.1.

**Presentar la simulación como observación.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17). 

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de la formación de la imagen** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Los de la clase, con sus límites | Los aplica a un caso nuevo |
| Cálculo | Sin unidades | Con errores | Tablas completas con unidades | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con la referencia analítica | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha | Declara lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular los datos como sintéticos; no presentar lo simulado como observado; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y los datos, sintéticos; no se interpreta ninguna escena real ni se evalúa el riesgo de ningún terreno. No se procesa ninguna escena real ni se recuperan datos de un sensor concreto. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

La imagen sintética reproduce la resolución teórica en los dos ejes (2,37 m y 5,32 m) con la migración corregida; sin corregirla el azimut se ensancha un 22 %. Queda una pregunta: ¿qué pasa cuando los blancos no son puntuales y el pixel suma muchos dispersores?

**Glosario español–inglés.** chirp · *chirp*; compresión en alcance · *range compression*; migración de celda · *range cell migration*; lóbulo lateral · *sidelobe*; razón de lóbulo lateral · *peak sidelobe ratio (PSLR)*.

**Continuidad.** [B69-C03](../B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md) estudia el speckle.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B69-C01 — Principio Doppler y resolución en azimut del SAR](../B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md) · [📚 Bloque B69](../../../tronco-comun/B69-radar-de-apertura-sintetica-e-interferometria-profundizacion.md) · [Siguiente: B69-C03 — Ruido speckle y filtrado en imágenes SAR →](../B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md)
<!-- /nav -->
