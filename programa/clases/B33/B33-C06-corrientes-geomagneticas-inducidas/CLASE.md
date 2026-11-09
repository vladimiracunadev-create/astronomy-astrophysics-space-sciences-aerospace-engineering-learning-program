# B33-C06 — Corrientes geomagnéticas inducidas (GIC)

<!-- nav:top -->
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 6 del bloque B33. Nivel N3. Un campo magnético variable induce un campo eléctrico en el suelo que mueve corrientes por las líneas. Aquí calculas el **campo geoeléctrico** sobre un semiespacio uniforme `|E| = √(ω/(μ₀σ))|B|` por componentes y en el tiempo con una **transformada discreta**, y la **corriente** inducida en una línea. Usas [B05](../../../tronco-comun/B05-fisica-fundamental-para-el-espacio.md) y [B30-C19](../../B30/B30-C19-impactos-del-clima-espacial/CLASE.md). Las amplitudes y la conductividad son ilustrativas.

## 2. Por qué esta clase existe

El campo eléctrico depende de la conductividad y de la frecuencia. La decisión central: **¿cuánto vale el campo geoeléctrico y la corriente en una línea para un campo magnético dado?**

## 3. Lo que podrás hacer al terminar

1. Calcular `|E|` por componente.
2. Calcular `E(t)` por transformada discreta.
3. Compararlo con la suma analítica.
4. Calcular la corriente de la línea.
5. Observar el efecto del periodo.
6. Reconocer los límites.

La evidencia es la **ficha de las corrientes inducidas** del ejercicio 12 (sección 20).

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

Con `σ = 10⁻³ S/m`, un campo de `50 nT` con periodo de 100 s induce `353,6 mV/km`. Es el **ejemplo conductor** (`μ₀` de NIST). Con tres componentes, el máximo es `456,2 mV/km` y la corriente en una línea de 100 km y 6 Ω es `7,60 A`. Todo es **ilustrativo**.

## 6. Vocabulario

El **semiespacio uniforme**. La **impedancia de superficie** `Z = √(iωμ₀/σ)`. El **campo geoeléctrico**. La **corriente inducida**. La **transformada discreta**.

## 7. Modelo mental: un imán que se mueve sobre una chapa

Como mover un imán sobre una chapa conductora: las corrientes inducidas dependen de qué tan rápido varía el campo.

```mermaid
flowchart LR
    B["B(t)"] --> F["B(ω)"]
    F --> Z["E(ω) = Z B/μ₀"]
    Z --> E["E(t)"]
    E --> I["I = E L/R"]
```

*Descripción textual:* el campo magnético se pasa al dominio de la frecuencia, se multiplica por la impedancia y se vuelve al tiempo para dar la corriente.

Analogía: un imán que se mueve sobre una chapa. Límite: semiespacio uniforme e incidencia vertical.

## 8. La explicación, paso a paso

### 8.1 Por componente (`σ = 10⁻³ S/m`)

| `T` (s) | `B` (nT) | `|E|` (mV/km) | `|Z|/μ₀` (m/s) |
|---|---|---|---|
| 100 | 50 | 353,55 | 7071 |
| 300 | 20 | 81,65 | 4082 |
| 1000 | 10 | 22,36 | 2236 |

### 8.2 En el tiempo

`E(t)` máximo `456,19 mV/km`; la diferencia entre el dominio de frecuencia y la suma analítica es `3 × 10⁻¹³` del máximo.

### 8.3 Corriente

Con `L = 100 km` y `R = 5 + 2 × 0,5 = 6 Ω`: `I = 7,60 A`.

### 8.4 Lectura

El campo eléctrico crece con la raíz de la frecuencia: las variaciones rápidas inducen más que las lentas para la misma amplitud.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `σ` | conductividad | S/m | 10⁻³ (ilustrativa) |
| `|E|` | campo geoeléctrico | mV/km | ver 8.1 |
| `I` | corriente | A | 7,60 |

## 10. Convenciones y referencias

Semiespacio uniforme; amplitudes y periodos ilustrativos.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NIST, *Fundamental Physical Constants* (CODATA 2022) | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | constantes citadas en la sección 9 | Consultada el 2026-11-09 |

Límites: no se consultó ninguna conductividad ni medida de campo.

## 12. Cómo ver el campo

| `T` (s) | `|E|` (mV/km) |
|---|---|
| 100 | 353,6 |
| 300 | 81,6 |
| 1000 | 22,4 |

Descripción larga: el campo cae con el periodo.

## 13. Ejemplo trabajado: campo a 100 s

**Paso 1 · `ω`.** `2π/100 = 0,0628 rad/s`.

**Paso 2 · Cociente.** `ω/(μ₀σ) = 5,00 × 10⁷`.

**Paso 3 · Raíz.** `7071 m/s`.

**Paso 4 · Producto.** `7071 × 50 nT = 353,6 mV/km`.

## 14. Distintas formas de describir un campo inducido

**Por frecuencia:** `√ω`. **Por suelo:** `1/√σ`. **Por tiempo:** transformada. **Por línea:** `I = EL/R`.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** `|E|` con `B = 50 nT` y `T = 100 s`. *Pasos:* ejemplo 13.

<details><summary>Solución comentada</summary>

`353,6 mV/km`.
</details>

**Ejercicio 2 · con una pista.** `|E|` si `σ` se cuadruplica.

<details><summary>Solución comentada</summary>

La mitad.
</details>

**Ejercicio 3 · casi autónomo.** `|E|` si el periodo se cuadruplica.

<details><summary>Solución comentada</summary>

La mitad.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Corriente con `E = 0,456 V/km`.

<details><summary>Solución comentada</summary>

`7,60 A`.
</details>

**Ejercicio 5.** Cociente `E(100 s)/E(1000 s)` con igual `B`.

<details><summary>Solución comentada</summary>

`√10 = 3,16`.
</details>

**Ejercicio 6.** Diferencia entre métodos.

<details><summary>Solución comentada</summary>

`3 × 10⁻¹³`.
</details>

**Ejercicio 7.** `Z/μ₀` a 300 s.

<details><summary>Solución comentada</summary>

`4082 m/s`.
</details>

**Ejercicio 8.** `I` si la línea es de 200 km.

<details><summary>Solución comentada</summary>

`15,2 A`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un compañero usa `σ = 10⁻³` como el de una región. Responde.

<details><summary>Solución comentada</summary>

Es ilustrativa.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Por qué el suelo real no es un semiespacio?

<details><summary>Solución comentada</summary>

Tiene capas.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Qué valida la transformada?

<details><summary>Solución comentada</summary>

La implementación.
</details>

**Ejercicio 12.** **Integrador.** Elabora tu *ficha de las corrientes inducidas*: campo, serie temporal y corriente.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de las corrientes inducidas*: campo, serie temporal y corriente.

<details><summary>Solución modelo</summary>

Secciones 8.1–8.4.
</details>

## 17. Laboratorio: campo geoeléctrico

El script [campo_geoelectrico.py](campo_geoelectrico.py) calcula `E` por componente y en el tiempo y la corriente (**comprueba** `10⁻⁶`).

**Datos:** `μ₀` de NIST; `σ`, `B`, `L`, `R` **ilustrativos**. **Predice antes de ejecutar:** ¿cuánto vale `E` a 100 s? (≈350 mV/km.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
  T [s]   B [nT]  |E| [mV/km]   Z/mu0 [m/s]
    100     50.0     353.5534     7.071e+03
    300     20.0      81.6497     4.082e+03
   1000     10.0      22.3607     2.236e+03
E(t) maximo = 456.192 mV/km ; diferencia maxima entre dominio de frecuencia y suma analitica = 3.25e-13 del maximo
|E| maximo = 0.4562 V/km ; en una linea de 100 km con 6 ohm: I = 7.603 A
Pruebas superadas.
```

```bash
python programa/clases/B33/B33-C06-corrientes-geomagneticas-inducidas/campo_geoelectrico.py
```

**Límites:** semiespacio uniforme.

## 18. Errores frecuentes y cómo corregirlos

**Confundir `B` y `dB/dt`.** Se corrige con 8.4.

**Olvidar la raíz.** Se corrige con el ejemplo 13.

**Tomar `σ` por medida.** Se corrige con la sección 10.

**Extrapolar a otras regiones.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de las corrientes inducidas** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | conceptos de la clase | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con el análisis | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | fuentes con fecha | Declara lo ilustrativo |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular `σ` como ilustrativa; no estimar corrientes reales; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

50 nT a 100 s sobre un suelo de 10⁻³ S/m inducen 354 mV/km y una línea de 100 km recibe unos 7,6 A. Queda una pregunta: ¿cómo se reparte esa corriente por la red?

**Glosario español–inglés.** corriente inducida geomagnéticamente · *geomagnetically induced current*; semiespacio · *half-space*; impedancia de superficie · *surface impedance*; campo geoeléctrico · *geoelectric field*; magnetotelúrica · *magnetotellurics*.

**Continuidad.** [B33-C07](../B33-C07-impactos-en-redes-electricas/CLASE.md) estudia los impactos en redes eléctricas.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

<!-- /nav -->
