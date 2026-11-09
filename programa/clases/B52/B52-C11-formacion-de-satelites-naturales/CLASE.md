# B52-C11 — Formación de satélites naturales

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B52](../../../tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md) · [← Anterior: B52-C10 — Arquitecturas de sistemas exoplanetarios](../B52-C10-arquitecturas-de-sistemas-exoplanetarios/CLASE.md) · [Siguiente: B52-C12 — Anillos planetarios →](../B52-C12-anillos-planetarios/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 11 del bloque B52. Nivel N3. Un planeta con su propio disco de gas y polvo se comporta como una estrella en miniatura, pero solo dentro de su esfera de Hill. Con datos publicados de la NASA ubicas los satélites galileanos en unidades del radio de Hill de Júpiter, y con una **simulación** del problema de Hill planar buscas hasta qué distancia sobreviven órbitas circulares prógradas y retrógradas. Retoma [B52-C04](../B52-C04-formacion-de-planetesimales/CLASE.md). Usas [B16](../../../tronco-comun/B16-sistemas-dinamicos-y-control-automatico.md).

## 2. Por qué esta clase existe

Los satélites regulares ocupan una pequeña fracción de la esfera de Hill, y el límite exterior de órbitas estables restringe dónde pudo existir el disco circumplanetario. La decisión central: **¿hasta qué fracción del radio de Hill puede haber satélites y dónde están los reales?**

## 3. Lo que podrás hacer al terminar

1. Calcular el radio de Hill de Júpiter por dos vías.
2. Expresar los semiejes de los galileanos en `a/R_H`.
3. Plantear las ecuaciones de Hill planares con `R_H = 1`.
4. Integrar órbitas circulares prógradas y retrógradas con RK4.
5. Obtener el mayor radio inicial que sobrevive en la malla.
6. Distinguir lo simulado (umbral) de lo observado (semiejes).

La evidencia es la **ficha de los satélites en la esfera de Hill** del ejercicio 12 (sección 20).

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

El radio de Hill de Júpiter es `53.15` millones de km. Calisto, el más lejano de los galileanos, está a `0.0354 R_H`. En la simulación, las órbitas prógradas circulares sobreviven hasta `0.475 R_H` y las retrógradas hasta `0.975 R_H`. Es el **ejemplo conductor**: semiejes observados, umbrales simulados.

## 6. Vocabulario

La **esfera de Hill** es la región donde domina la gravedad del planeta. El **problema de Hill** es el límite del problema de tres cuerpos con masa planetaria pequeña, en el sistema que rota con el planeta. Una órbita **prógrada** gira en el mismo sentido que el planeta alrededor del Sol; una **retrógrada**, en sentido contrario. Un **satélite regular** está en órbita prógrada, casi circular y coplanar con el ecuador del planeta.

## 7. Modelo mental

Como una pelota de playa en un remolino: solo se queda cerca del centro la que gira dentro de cierto radio; más lejos, la corriente la arrastra. Límite: modelo planar, sin gas, achatamiento ni otras lunas.

```mermaid
flowchart LR
    M["GM planeta, GM Sol, a_p"] --> H["R_H"]
    H --> U["a / R_H de los satélites"]
    H --> E["ecuaciones de Hill"]
    E --> I["RK4 de órbitas circulares"]
    I --> T["umbral de supervivencia"]
```

*Descripción textual:* las masas y la distancia dan el radio de Hill, con el que se expresan los semiejes; las ecuaciones de Hill se integran para hallar hasta qué radio sobreviven las órbitas.

## 8. La explicación, paso a paso

### 8.1 Radio de Hill

`R_H = a_J ((GM)_J/(3(GM)☉))^(1/3) = 53.149` millones de km; con las masas por separado, el mismo valor (diferencia `0e+00`).

### 8.2 Los satélites

| satélite | a [10³ km] | a/R_H |
|---|---|---|
| Io | 421.8 | 0.0079 |
| Europa | 671.1 | 0.0126 |
| Ganimedes | 1070.4 | 0.0201 |
| Calisto | 1882.7 | 0.0354 |

Todos ocupan menos del 4 % del radio de Hill.

### 8.3 Simulación de Hill

En unidades `R_H = 1`, `Ω = 1`: `x'' = 2y' + 3x − 3x/r³`, `y'' = −2x' − 3y/r³`. Una órbita circular de radio `ρ` alrededor del planeta tiene velocidad rotante `±√(3/ρ) − ρ`. Con RK4 (`h = 0,002`, `t = 100`, escape si `r > 2`) y una malla de `0,025` entre `0,30` y `1,30`:

| sentido | mayor `ρ` que sobrevive | primer escape en la malla |
|---|---|---|
| prógrado | 0.475 | 0.5 |
| retrógrado | 0.975 | 1.0 |

Esto es un resultado de **este modelo y esta malla**; los umbrales de la literatura no se consultaron y el borde real es fractal.

### 8.4 Lectura

Que los satélites estén dentro del 4 % del radio de Hill es compatible con un disco circumplanetario compacto; la simulación muestra solo un límite dinámico externo. La formación a partir de discos extendidos (S5) no se modela.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `R_H` | radio de Hill de Júpiter | m | 5.315e+10 |
| `a/R_H` | semieje relativo | — | 0.0354 (Calisto) |
| `ρ` | radio inicial de la simulación | `R_H` | 0,30 a 1,30 |
| `h` | paso de RK4 | 1/Ω | 0,002 |

## 10. Convenciones y referencias

SI para los semiejes; unidades de Hill (`R_H = Ω = 1`) en la simulación. Tolerancia `10⁻¹²` entre dos fórmulas del radio de Hill; los umbrales se reportan sin tolerancia analítica.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NIST, *Fundamental Physical Constants — Complete Listing* (CODATA 2022) | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | `G`, `k_B`, `m_p` | Consultada el 2026-11-09 |
| S2 | Mamajek et al., *IAU 2015 Resolution B3*, arXiv:1510.07674 | https://arxiv.org/abs/1510.07674 | `(GM)☉`, `(GM)⊕`, `(GM)_J` nominales | Texto del PDF extraído el 2026-11-09 |
| S3 | NASA/NSSDC, *Jovian Satellite Fact Sheet* | https://nssdc.gsfc.nasa.gov/planetary/factsheet/joviansatfact.html | Semiejes de Io, Europa, Ganimedes y Calisto | Consultada el 2026-11-09 |
| S4 | NASA/NSSDC, *Planetary Fact Sheet* (tabla métrica) | https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html | Distancia de Júpiter al Sol (fila «Distance from Sun») | Consultada el 2026-11-09 |
| S5 | Crida y Charnoz, *Formation of Regular Satellites from Ancient Massive Rings in the Solar System*, Science 338 (2012), arXiv:1301.3808 | https://arxiv.org/abs/1301.3808 | Los satélites regulares pueden formarse a partir de discos que se extienden más allá del radio de Roche | Descripción obtenida con un buscador el 2026-11-09; no se leyó el texto |

Límites: las fichas no dan incertidumbres; de S5 no se leyó el texto; los umbrales de supervivencia son de la simulación y no se compararon con la literatura; el modelo es planar.

## 12. Cómo verlo

| Magnitud | Valor |
|---|---|
| R_H de Júpiter | 53.15 millones de km |
| a/R_H de Calisto | 0.0354 |
| límite prógrado (simulado) | 0.475 R_H |
| límite retrógrado (simulado) | 0.975 R_H |

Descripción larga: los satélites galileanos están muy dentro de la esfera de Hill, y la simulación sitúa el límite prógrado cerca de la mitad del radio de Hill.

## 13. Ejemplo trabajado

**Paso 1 · Cociente de masas.** `(GM)_J/(3(GM)☉) = 3.1820e-04`.

**Paso 2 · Raíz cúbica.** `0.06827`.

**Paso 3 · Radio.** `R_H = 778,5·10⁹ m · 0.06827 = 5.3149e+10 m`.

**Paso 4 · Calisto.** `a/R_H = 1882,7·10⁶ m/R_H = 0.0354`.

## 14. Distintas formas de describirlo

**Por fórmula:** `R_H`. **Por tabla:** 8.2. **Por simulación:** umbrales de Hill.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `a/R_H` de Io. *Pasos:* `421,8·10⁶/R_H`.

<details><summary>Solución comentada</summary>

`0.0079`.
</details>

**Ejercicio 2 · con una pista.** Si Júpiter estuviera al doble de distancia del Sol, ¿cómo cambia `R_H`? *Pista:* `R_H ∝ a_p`.

<details><summary>Solución comentada</summary>

Se duplica.
</details>

**Ejercicio 3 · casi autónomo.** ¿Qué satélite está más cerca del borde?

<details><summary>Solución comentada</summary>

Calisto.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** `R_H` en millones de km.

<details><summary>Solución comentada</summary>

`53.15`.
</details>

**Ejercicio 5.** `a/R_H` de Ganimedes.

<details><summary>Solución comentada</summary>

`0.0201`.
</details>

**Ejercicio 6.** Umbral prógrado simulado.

<details><summary>Solución comentada</summary>

`0.475 R_H`.
</details>

**Ejercicio 7.** Umbral retrógrado simulado.

<details><summary>Solución comentada</summary>

`0.975 R_H`.
</details>

**Ejercicio 8.** ¿Cuál es mayor y por qué puede ser?

<details><summary>Solución comentada</summary>

El retrógrado: en el sistema rotante la fuerza de Coriolis estabiliza más las órbitas retrógradas.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** **Transferencia.** Un colega afirma que la simulación demuestra el límite de estabilidad de los satélites reales. Responde.

<details><summary>Solución comentada</summary>

No: es un modelo planar con malla gruesa y tiempo corto; los límites publicados no se consultaron.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** **Transferencia.** ¿Qué cambia si el planeta es menos masivo?

<details><summary>Solución comentada</summary>

`R_H` baja como `m^(1/3)` y los satélites ocupan una fracción mayor.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** **Transferencia.** ¿Qué ignora el modelo?

<details><summary>Solución comentada</summary>

El achatamiento, las otras lunas, el gas y la inclinación.
</details>

**Ejercicio 12 · integrador.** **Integrador.** **Integrador.** Elabora tu *ficha de los satélites en la esfera de Hill*: `R_H`, tabla 8.2, umbrales simulados y límites.

<details><summary>Solución modelo</summary>

Secciones 8.1–8.4 y 12.
</details>

## 17. Laboratorio: satélites y esfera de Hill

El script [hill.py](hill.py) calcula el radio de Hill de Júpiter, ubica los galileanos y busca con RK4 el límite de supervivencia de órbitas circulares en el problema de Hill planar (**comprueba** `10⁻¹²` entre dos fórmulas).

**Datos:** semiejes y distancia de las fichas de la NASA/NSSDC, `(GM)` de la IAU 2015 y `G` de NIST, consultados el 2026-11-09; los umbrales son **simulados**. **Predice antes de ejecutar:** ¿Qué fracción del radio de Hill ocupan los galileanos? (Menos del 4 %.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Radio de Hill de Jupiter = 53.149 millones de km (formula con (GM)) ; con masas = 53.149 ; dif. rel. = 0.0e+00
  satelite  a [1e3 km]   a / R_H
        Io       421.8    0.0079
    Europa       671.1    0.0126
 Ganimedes      1070.4    0.0201
   Calisto      1882.7    0.0354
SIMULACION (problema de Hill planar, no observacion):
  orbita prograda: sobrevive hasta rho = 0.475 R_H ; primer escape en la malla en rho = 0.5
  orbita retrograda: sobrevive hasta rho = 0.975 R_H ; primer escape en la malla en rho = 1.0
Pruebas superadas.
```

```bash
python programa/clases/B52/B52-C11-formacion-de-satelites-naturales/hill.py
```

**Límites:** modelo planar, malla gruesa y tiempo corto; los umbrales no se contrastan con la literatura.

## 18. Errores frecuentes y cómo corregirlos

**Presentar un umbral simulado como observado.** Se corrige con 8.3.

**Confundir `R_H` del planeta con el del satélite.** Se corrige con 8.1.

**Olvidar las unidades de Hill.** Se corrige con la sección 10.

**Dar a los semiejes de la ficha incertidumbre propia.** Se corrige con la sección 11.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas y cuál obtuviste? Si dudas, repasa el ejemplo de la sección 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de los satélites en la esfera de Hill** (ejercicio 12).

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

Los galileanos están a menos de `0.035 R_H`; la simulación limita las órbitas prógradas cerca de `0.47 R_H`. Queda una pregunta: ¿cómo se mantiene un disco de material cerca del planeta?

**Glosario español–inglés.** esfera de Hill · *Hill sphere*; satélite regular · *regular satellite*; órbita prógrada · *prograde orbit*; órbita retrógrada · *retrograde orbit*; disco circumplanetario · *circumplanetary disk*.

**Continuidad.** [B52-C12](../B52-C12-anillos-planetarios/CLASE.md) estudia los anillos.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B52-C10 — Arquitecturas de sistemas exoplanetarios](../B52-C10-arquitecturas-de-sistemas-exoplanetarios/CLASE.md) · [📚 Bloque B52](../../../tronco-comun/B52-formacion-y-dinamica-de-sistemas-planetarios.md) · [Siguiente: B52-C12 — Anillos planetarios →](../B52-C12-anillos-planetarios/CLASE.md)
<!-- /nav -->
