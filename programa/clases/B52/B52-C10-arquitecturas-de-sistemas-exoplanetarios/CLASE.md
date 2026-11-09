# B52-C10 — Arquitecturas de sistemas exoplanetarios

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B52](../../../tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md) · [← Anterior: B52-C09 — Dispersión de discos de gas](../B52-C09-dispersion-de-discos-de-gas/CLASE.md) · [Siguiente: B52-C11 — Formación de satélites naturales →](../../../tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md#b52-c11)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 10 del bloque B52. Nivel N3. La arquitectura de un sistema —cuántos planetas, a qué distancias, con qué razones de periodos— se describe como un problema de ingeniería con requisitos y criterios de comprobación. Mides el **espaciado en radios de Hill mutuos** de los planetas del Sistema Solar con datos de la NASA, lo comparas con un sistema **sintético** de espaciado uniforme y verificas los semiejes con la tercera ley de Kepler. Retoma el radio de Hill de [B52-C04](../B52-C04-formacion-de-planetesimales/CLASE.md). Usas [B29](../../../tronco-comun/B29-astronomia-temporal-y-exoplanetas.md).

## 2. Por qué esta clase existe

El espaciado mide cuán «apretado» está un sistema y cuán cerca está de la inestabilidad. La decisión central: **¿cómo se expresa el espaciado entre planetas independientemente de su escala?**

## 3. Lo que podrás hacer al terminar

1. Calcular el radio de Hill mutuo de dos planetas.
2. Calcular el espaciado `Δ = (a₂ − a₁)/R_H,m` de pares vecinos.
3. Obtener semiejes con la tercera ley de Kepler y compararlos con los de la ficha.
4. Construir un sistema sintético de espaciado constante y obtener sus periodos.
5. Calcular razones de periodos adyacentes.
6. Distinguir datos publicados de un sistema sintético.

La evidencia es la **ficha de la arquitectura de un sistema** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es una tabla de resultados?
2. ¿Qué es una verificación?
3. ¿Qué es una tolerancia numérica?
4. ¿Qué es la tercera ley de Kepler?
5. ¿Qué es un valor ilustrativo?

<details>
<summary>Ver respuestas</summary>

1. Un resumen ordenado de cálculos. 2. Comparar un cálculo con un caso independiente. 3. La diferencia máxima aceptada entre dos resultados. 4. El cuadrado del periodo crece con el cubo del semieje. 5. Un valor propuesto para el ejemplo, no medido.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

En el Sistema Solar, Júpiter–Saturno están a `Δ = 7.9` radios de Hill mutuos; Urano–Neptuno, `14.1`; Venus–Tierra, `26.3`. Un sistema **sintético** con `Δ = 12` y cinco planetas de `5 M⊕` alrededor de `0,9 M☉` da razones de periodos de `1.4981`. Es el **ejemplo conductor**; el sistema sintético no es un sistema observado.

## 6. Vocabulario

El **radio de Hill mutuo** es `R_H,m = ((m₁+m₂)/(3M*))^(1/3) (a₁+a₂)/2`. El **espaciado** `Δ` es la separación en esa unidad. La **razón de periodos** `P₂/P₁` indica cercanía a una resonancia. La **arquitectura** es el conjunto de semiejes, masas y excentricidades de un sistema.

## 7. Modelo mental

Como medir la distancia entre casas en «largos de patio» del vecindario en lugar de metros: permite comparar barrios de tamaños distintos. Límite: órbitas circulares coplanares y masas tomadas de una ficha sin incertidumbres.

```mermaid
flowchart LR
    D["masas, semiejes"] --> R["R_H,m"]
    R --> E["Δ de pares vecinos"]
    P["periodos"] --> K["semieje de Kepler"]
    K --> D
    E --> S["sistema sintético Δ constante"]
```

*Descripción textual:* las masas y los semiejes dan el radio de Hill mutuo y el espaciado; los periodos validan los semiejes; con Δ constante se construye un sistema sintético.

## 8. La explicación, paso a paso

### 8.1 Semiejes

La ficha entrega «distancia al Sol»; el semieje de Kepler con `(GM)☉` y el periodo difiere en menos de `8.4e-03` relativo:

| planeta | ficha [ua] | Kepler [ua] | dif. |
|---|---|---|---|
| Mercurio | 0.3870 | 0.3872 | 3.9e-04 |
| Venus | 0.7233 | 0.7233 | 8.0e-05 |
| Tierra | 1.0000 | 0.9999 | -1.2e-04 |
| Marte | 1.5241 | 1.5237 | -2.4e-04 |
| Jupiter | 5.2040 | 5.1999 | -7.8e-04 |
| Saturno | 9.5723 | 9.5307 | -4.3e-03 |
| Urano | 19.1647 | 19.1416 | -1.2e-03 |
| Neptuno | 30.1809 | 29.9274 | -8.4e-03 |

### 8.2 Espaciado

| par | Δ | P₂/P₁ |
|---|---|---|
| Mercurio–Venus | 63.40 | 2.553 |
| Venus–Tierra | 26.32 | 1.625 |
| Tierra–Marte | 40.12 | 1.881 |
| Marte–Jupiter | 16.02 | 6.304 |
| Jupiter–Saturno | 7.94 | 2.481 |
| Saturno–Urano | 13.94 | 2.846 |
| Urano–Neptuno | 14.12 | 1.955 |

El mínimo es Júpiter–Saturno, `7.9`. El par Marte–Júpiter incluye el cinturón de asteroides (clase C14).

### 8.3 Sistema sintético

Construido con `Δ = 12` desde `0,05 ua`, `m = 5 M⊕`, `M* = 0,9 M☉` por bisección: semiejes `0.0500 0.0655 0.0857 0.1122 0.1469` ua, periodos `4.30 6.45 9.66 14.47 21.68` días y razón constante `1.4981` (el espaciado constante en `R_H` implica razón de periodos casi constante). El `Δ` reconstruido es `12` con error `10⁻⁹`.

### 8.4 Lectura

Que un sistema esté espaciado en torno de una decena de radios de Hill es un dato descriptivo; no demuestra estabilidad. La estabilidad a largo plazo se trata en la clase C19.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `Δ` | espaciado en radios de Hill mutuos | — | 7.9 (Júpiter–Saturno) |
| `R_H,m` | radio de Hill mutuo | m | fórmula 8.1 |
| `P₂/P₁` | razón de periodos | — | 2.481 (J–S) |
| `m` | masa de planeta | kg | ficha de la NASA |

## 10. Convenciones y referencias

SI. Órbitas circulares coplanares aproximadas. Tolerancias: Kepler frente a la ficha `1 %`; `Δ` reconstruido `10⁻⁹`. Sistema sintético: rotulado.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NIST, *Fundamental Physical Constants — Complete Listing* (CODATA 2022) | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | `G`, `k_B`, `m_p` | Consultada el 2026-11-09 |
| S2 | Mamajek et al., *IAU 2015 Resolution B3*, arXiv:1510.07674 | https://arxiv.org/abs/1510.07674 | `(GM)☉`, `(GM)⊕`, `(GM)_J` nominales | Texto del PDF extraído el 2026-11-09 |
| S3 | NASA/NSSDC, *Planetary Fact Sheet* (tabla métrica) | https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html | Masas, distancias al Sol y periodos de Mercurio a Neptuno | Consultada el 2026-11-09 |

Límites: la ficha no da incertidumbres y su fila se rotula «Distance from Sun» (no «semieje mayor»); el sistema sintético no tiene fuente; la estabilidad no se evalúa.

## 12. Cómo verlo

| Magnitud | Valor |
|---|---|
| Δ Júpiter–Saturno | 7.9 |
| Δ Urano–Neptuno | 14.1 |
| Δ Venus–Tierra | 26.3 |
| razón sintética | 1.4981 |

Descripción larga: los planetas gigantes están menos espaciados (en radios de Hill) que los terrestres y el sistema sintético reparte uniformemente `Δ = 12`.

## 13. Ejemplo trabajado

**Paso 1 · Radio de Hill mutuo.** Para Júpiter–Saturno, `R_H,m = ((1898+568)·10²⁴/(3·1,989·10³⁰))^(1/3)·(778,5+1432)/2·10⁹ m`.

**Paso 2 · Separación.** `a₂ − a₁ = 653,5·10⁹ m`.

**Paso 3 · Espaciado.** `Δ = 7.94`.

## 14. Distintas formas de describirlo

**Por fórmula:** `Δ`. **Por tabla:** 8.2. **Por construcción:** sistema sintético.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `P₂/P₁` si `a₂/a₁ = 2`. *Pista:* `(a₂/a₁)^(3/2)`.

<details><summary>Solución comentada</summary>

`2,83`.
</details>

**Ejercicio 2 · con una pista.** Si `Δ` es constante, ¿qué pasa con `a₂/a₁`?

<details><summary>Solución comentada</summary>

Casi constante si las masas son iguales.
</details>

**Ejercicio 3 · casi autónomo.** ¿Qué par es el más apretado?

<details><summary>Solución comentada</summary>

Júpiter–Saturno.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** `Δ` Venus–Tierra.

<details><summary>Solución comentada</summary>

`26.32`.
</details>

**Ejercicio 5.** Razón de periodos Júpiter–Saturno.

<details><summary>Solución comentada</summary>

`2.481`.
</details>

**Ejercicio 6.** Semieje de Kepler de Neptuno.

<details><summary>Solución comentada</summary>

`29.927 ua`.
</details>

**Ejercicio 7.** Periodo del cuarto planeta sintético.

<details><summary>Solución comentada</summary>

`14.47 días`.
</details>

**Ejercicio 8.** Razón sintética.

<details><summary>Solución comentada</summary>

`1.4981`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** **Transferencia.** Un colega usa el sistema sintético como un sistema real. Responde.

<details><summary>Solución comentada</summary>

No: es un artificio; la comparación debería hacerse con datos publicados y citados.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** **Transferencia.** ¿Qué cambia si las masas se duplican?

<details><summary>Solución comentada</summary>

`R_H,m` crece `2^(1/3)` y la separación con `Δ` fija crece.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** **Transferencia.** ¿Por qué Marte–Júpiter, con gran separación, tiene `Δ` moderado (16)?

<details><summary>Solución comentada</summary>

Júpiter es tan masivo que `R_H,m` es grande aun con esa separación; el cinturón de asteroides se estudia en la clase C14.
</details>

**Ejercicio 12 · integrador.** **Integrador.** **Integrador.** Elabora tu *ficha de la arquitectura de un sistema*: tablas 8.1 y 8.2, sistema sintético y límites.

<details><summary>Solución modelo</summary>

Secciones 8.1–8.4 y 12.
</details>

## 17. Laboratorio: espaciado en radios de Hill mutuos

El script [arquitectura.py](arquitectura.py) calcula `Δ` para los planetas del Sistema Solar con datos de la NASA, verifica los semiejes con Kepler y construye un sistema sintético de `Δ` constante (**comprueba** `1 %` y `10⁻⁹`).

**Datos:** masas, distancias y periodos de la ficha de la NASA/NSSDC, `G` de NIST y `(GM)☉` de la IAU 2015, consultados el 2026-11-09; el sistema de cinco planetas es **sintético**. **Predice antes de ejecutar:** ¿Qué par está más apretado? (Júpiter–Saturno.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Sistema Solar (ficha NASA/NSSDC, consulta 2026-11-09; sin incertidumbres en la ficha)
  planeta  dist. ficha [ua]  a Kepler [ua]      dif.
 Mercurio            0.3870         0.3872  3.91e-04
    Venus            0.7233         0.7233  7.96e-05
   Tierra            1.0000         0.9999 -1.18e-04
    Marte            1.5241         1.5237 -2.39e-04
  Jupiter            5.2040         5.1999 -7.83e-04
  Saturno            9.5723         9.5307 -4.35e-03
    Urano           19.1647        19.1416 -1.21e-03
  Neptuno           30.1809        29.9274 -8.40e-03
                 par  Delta (R_H mutuos)    P2/P1
      Mercurio-Venus               63.40    2.553
        Venus-Tierra               26.32    1.625
        Tierra-Marte               40.12    1.881
       Marte-Jupiter               16.02    6.304
     Jupiter-Saturno                7.94    2.481
       Saturno-Urano               13.94    2.846
       Urano-Neptuno               14.12    1.955
Sistema SINTETICO (no observado): 5 planetas de 5 M_Tierra, 0.9 M_sol, Delta = 12
semiejes [ua]: 0.05000 0.06546 0.08571 0.11221 0.14692
periodos [d]: 4.305 6.449 9.661 14.473 21.682
razones de periodos: 1.4981 1.4981 1.4981 1.4981 ; Delta reconstruido: 12.000000000 12.000000000 12.000000000 12.000000000
Pruebas superadas.
```

```bash
python programa/clases/B52/B52-C10-arquitecturas-de-sistemas-exoplanetarios/arquitectura.py
```

**Límites:** órbitas circulares coplanares, datos sin incertidumbre, sin evaluar estabilidad.

## 18. Errores frecuentes y cómo corregirlos

**Confundir distancia a escala absoluta con espaciado.** Se corrige con 8.2.

**Usar la ficha como semieje exacto.** Se corrige con 8.1.

**Interpretar `Δ` como prueba de estabilidad.** Se corrige con 8.4.

**Presentar el sistema sintético como observado.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas y cuál obtuviste? Si dudas, repasa el ejemplo de la sección 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de la arquitectura de un sistema** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Conceptos de la clase | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con el análisis | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha | Declara lo ilustrativo |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular lo sintético e ilustrativo; no presentar un resultado simulado como observado; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y no sustituyen a la literatura primaria ni a los códigos de producción. Lo simulado no es lo observado. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

El espaciado mínimo del Sistema Solar es `7.9` (Júpiter–Saturno) y el sistema sintético usa `Δ = 12`. Queda una pregunta: ¿cómo se forman los satélites que acompañan a los planetas?

**Glosario español–inglés.** arquitectura planetaria · *planetary architecture*; radio de Hill mutuo · *mutual Hill radius*; espaciado · *spacing*; razón de periodos · *period ratio*.

**Continuidad.** [B52-C11](../B52-C11-formacion-de-satelites-naturales/CLASE.md) estudia los satélites naturales.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B52-C09 — Dispersión de discos de gas](../B52-C09-dispersion-de-discos-de-gas/CLASE.md) · [📚 Bloque B52](../../../tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md) · [Siguiente: B52-C11 — Formación de satélites naturales →](../../../tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md#b52-c11)
<!-- /nav -->
