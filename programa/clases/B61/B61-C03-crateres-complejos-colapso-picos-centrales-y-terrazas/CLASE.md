# B61-C03 — Cráteres complejos: colapso, picos centrales y terrazas

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B61](../../../tronco-comun/B61-crateres-de-impacto-y-geologia-de-impactos.md) · [← Anterior: B61-C02 — Cráteres simples: morfología y formación](../B61-C02-crateres-simples-morfologia-y-formacion/CLASE.md) · [Siguiente: B61-C04 — Mantos de ejecta y depósitos de impacto →](../B61-C04-mantos-de-ejecta-y-depositos-de-impacto/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 3 del bloque B61. Nivel N3. Cuando un cráter supera cierto diámetro, la gravedad vence la resistencia del material y el bol **colapsa**: aparecen terrazas, un fondo plano y un pico central (cráter **complejo**). Aquí planteas un modelo simple de umbral (`D_sc ∝ 1/g`), lo **calibras con un cuerpo y lo contrastas con otro**, y ejecutas una relajación numérica de pendientes que conserva el área. Usa la [C02](../B61-C02-crateres-simples-morfologia-y-formacion/CLASE.md). Los diámetros de transición provienen de una fuente de divulgación; los perfiles son sintéticos.

## 2. Por qué esta clase existe

Sin la transición simple–compleja no se puede interpretar la forma de un cráter grande ni comparar cuerpos. La decisión central: **¿a qué diámetro cambia la morfología y cómo depende de la gravedad?**

## 3. Lo que podrás hacer al terminar

1. Describir la morfología simple y la compleja (terrazas, fondo plano, pico central).
2. Plantear `D_sc = k Y/(ρ g)` y calibrar `k Y` con un cuerpo.
3. Contrastar la predicción con otro cuerpo y declarar el desacuerdo.
4. Estimar un exponente libre de `g` entre dos cuerpos.
5. Relajar un perfil con un ángulo crítico y comprobar la conservación del área.
6. Reconocer qué no captura el modelo (pico central, fluidización).

La evidencia es la **ficha de la transición simple–compleja** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es la presión litostática?
2. ¿Qué es un ángulo de reposo?
3. ¿Qué es calibrar un modelo?
4. ¿Qué es un cráter simple (C02)?
5. ¿Qué es una conservación de área?

<details>
<summary>Ver respuestas</summary>

1. `ρ g z` a la profundidad `z`. 2. El ángulo máximo estable de una pendiente de material granular. 3. Ajustar una constante con un dato. 4. Un bol sin pico central. 5. Que el área del perfil no cambia al redistribuir.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Una entrada de divulgación sitúa la transición en ≈ 16 km en la Luna y ≈ 8 km en Marte. Calibrado con la Luna, `D_sc ∝ 1/g` predice **6,99 km** para Marte, un 13 % menos; un exponente libre da −0,837. Es el **ejemplo conductor**; los números de la fuente son órdenes de magnitud, no valores revisados.

## 6. Vocabulario

La **transición simple–compleja** es el diámetro `D_sc` en que cambia la forma. Un **pico central** es una elevación en el centro; las **terrazas** son escalones de la pared. La **resistencia efectiva** `Y` es la cohesión que sostiene la pared. El **ángulo crítico** es la pendiente máxima estable.

## 7. Modelo mental

Un esquema del flujo de cálculo de la clase; el texto equivalente está debajo.

```mermaid
flowchart LR
    G["gravedad g"] --> U["D_sc = kY/(ρ g)"]
    U --> C["calibrar con la Luna"]
    C --> P["predecir Marte"]
    P --> T["comparar con ≈ 8 km"]
    T --> E["exponente libre"]
```

*Descripción textual:* se calibra el umbral con un cuerpo, se predice el otro, se compara con la fuente y se estima un exponente libre.

Analogía: una pila de arena: hasta cierta altura se sostiene sola, más allá se desmorona; con más gravedad el límite baja. Límite: la arena no tiene pico central.

## 8. La explicación, paso a paso

### 8.1 Calibración y contraste

| cuerpo | `g` [m/s²] | `D_sc` [km] | origen |
|---|---|---|---|
| Luna | 1,62 | 16,00 | divulgación (calibra) |
| Marte | 3,71 | 6,99 | modelo; fuente ≈ 8 |
| `g` = 9,81 | 9,81 | 2,64 | modelo (cuerpo de prueba) |

`D_sc·g` = 25,920 km·m/s². La razón predicción/fuente para Marte es 0,873. El exponente libre es `D_sc ∝ g^(−0,837)`: la gravedad no lo explica todo (otra resistencia, otra roca).

### 8.2 Relajación de pendientes

Perfil sintético de `D` = 20 km y `d` = 5 km (`d/D` = 0,25) con ángulo crítico de 20° (tan = 0,3640). La pendiente máxima baja de 0,9950 a 0,3641; el área se conserva (diferencia relativa 0).

### 8.3 Hallazgo

La profundidad central no cambia (5,000 km): la regla de pendiente no levanta el suelo. El ancho del suelo a más del 90 % de la profundidad baja de 6,30 a 3,60 km. El **pico central** y la fluidización quedan **fuera del modelo**.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `D_sc` | diámetro de transición | km | 16; 6,99; 2,64 |
| `g` | gravedad | m/s² | 1,62; 3,71; 9,81 |
| `k Y/ρ` | constante calibrada | km·m/s² | 25,920 |
| φ | ángulo crítico | grados | 20 (ilustrativo) |
| `d/D` | razón del perfil | — | 0,25 (sintético) |

## 10. Convenciones y referencias

Diámetros en km; `g` en m/s²; el perfil es 1D y simétrico; las alturas negativas son depresiones.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S5 | CosmoQuest (2017), *CQ Science – Post 6: Simple to Complex*, https://cosmoquest.org/x/2017/12/cq-science-post-6-simple-to-complex/ | consultada 2026-11-09 | transición simple–compleja ≈ 16 km en la Luna y ≈ 8 km en Marte; depende de la gravedad | Divulgación; orden de magnitud, no valor revisado |
| — | Sin fuente externa | — | los cálculos de la sección 17 y los parámetros marcados como ilustrativos | No consultado |

Límites: los diámetros de transición vienen de una entrada de divulgación (CosmoQuest, 2017), no de un artículo revisado; la Tierra no se contrasta (no se halló valor en la búsqueda); `g` de la Luna y Marte son valores redondeados no consultados.

## 12. Cómo ver el resultado

| Magnitud | Valor |
|---|---|
| `D_sc` Marte (modelo) | 6,99 km |
| razón con la fuente | 0,873 |
| exponente libre | −0,837 |
| ancho del suelo | 6,30 → 3,60 km |

Descripción larga: el modelo sencillo predice un umbral marciano algo menor que el citado.

## 13. Ejemplo trabajado

**Ejemplo: umbral en un cuerpo de `g` = 3,0 m/s².**

**Paso 1.** `D_sc = 25,92/3,0`.

**Paso 2.** `D_sc = 8,64 km`.

**Paso 3.** Es una predicción del modelo sin contraste con ninguna fuente.

## 14. Distintas formas de describir lo mismo

**Por fórmula:** `D_sc g` constante. **Por tabla:** cuerpos y razones. **Por exponente:** `g^(−0,837)`. **Por simulación:** relajación del perfil.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Con `D_sc g` = 25,92, calcula `D_sc` para `g` = 3,71. *Pasos:* divide.

<details><summary>Solución comentada</summary>

`6,99 km`.
</details>

**Ejercicio 2 · con una pista.** Con una pista: ¿cuánto vale `tan 20°`?

<details><summary>Solución comentada</summary>

`0,3640`.
</details>

**Ejercicio 3 · casi autónomo.** Casi autónomo: ¿qué razón da predicción/fuente para Marte?

<details><summary>Solución comentada</summary>

`6,99/8 = 0,873`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Calcula el exponente libre entre dos cuerpos con `D` 16 y 8 km y `g` 1,62 y 3,71.

<details><summary>Solución comentada</summary>

`ln2/ln(3,71/1,62) = 0,837`.
</details>

**Ejercicio 5.** ¿Qué `D_sc` da el modelo para `g` = 9,81?

<details><summary>Solución comentada</summary>

`2,64 km`.
</details>

**Ejercicio 6.** ¿Qué pasa con el área tras la relajación?

<details><summary>Solución comentada</summary>

Se conserva (diferencia 0).
</details>

**Ejercicio 7.** ¿Cuánto baja la pendiente máxima del perfil sintético?

<details><summary>Solución comentada</summary>

De 0,9950 a 0,3641.
</details>

**Ejercicio 8.** ¿Por qué no baja la profundidad central?

<details><summary>Solución comentada</summary>

La pendiente en el centro es casi nula y la regla solo actúa en pendientes empinadas.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** La predicción para Marte no coincide con ≈ 8 km. ¿Qué hipótesis puedes revisar?

<details><summary>Solución comentada</summary>

La resistencia `Y` (distinta roca o temperatura), la densidad y la fuente misma (divulgación).
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Qué observación necesitarías para validar el modelo en la Tierra?

<details><summary>Solución comentada</summary>

Diámetros de transición de cráteres terrestres conservados, de un artículo revisado; en esta sesión no se consultaron.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Cómo mejorarías la relajación para obtener un pico central?

<details><summary>Solución comentada</summary>

Añadir rebote elástico o un flujo viscoso con fluidización; es un modelo distinto.
</details>

**Ejercicio 12 · integrador.** Elabora tu *ficha de la transición simple–compleja*: el modelo de umbral por gravedad, su calibración con la Luna, el contraste con Marte, el exponente libre y el resultado de la relajación de pendientes, con rótulos.

<details><summary>Solución modelo</summary>

Secciones 8.1–8.3: `D_sc·g` = 25,92 km·m/s²; predicción para Marte 6,99 km frente a ≈ 8 km (razón 0,873); exponente libre −0,837; ancho del suelo 6,30 → 3,60 km con área conservada.
</details>

## 17. Laboratorio: umbral por gravedad y relajación de pendientes

El script [colapso.py](colapso.py) calibra `D_sc g` con la Luna, predice Marte, estima el exponente libre y relaja un perfil sintético (**comprueba** conservación del área 1e-9 y pendiente 1e-3).

**Datos:** diámetros ≈ 16 y 8 km de una fuente de **divulgación**; `g` redondeados; perfil **sintético**. **Predice antes de ejecutar:** ¿Predecirá el modelo más o menos de 8 km para Marte? (menos, 6,99 km.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Modelo A: D_sc * g = 25.920 km m/s2 (calibrado con la Luna: 16 km)
Prediccion para Marte = 6.99 km ; divulgacion ~ 8 km ; razon pred/ref = 0.873
Exponente libre entre ambos cuerpos: D_sc ~ g^(-0.837) (el modelo ingenuo usa -1)
  D_sc(modelo A, Luna) = 16.00 km
  D_sc(modelo A, Marte) = 6.99 km
  D_sc(modelo A, g=9.81 (cuerpo de prueba)) = 2.64 km
Perfil sintetico D=20 km, d=5.0 km (d/D=0.25), angulo critico 20 grados (tan=0.3640)
Pendiente maxima inicial = 0.9950 ; final = 0.3641
Profundidad inicial = 5.000 km ; final = 5.000 km
Conservacion de area (volumen 2D): inicial -66.666875000 ; final -66.666875000 ; dif. relativa 0.00e+00
Ancho del suelo a >90 % de la profundidad: inicial 6.30 km ; final 3.60 km
Hallazgo: la regla de pendiente NO levanta el suelo (profundidad intacta); el pico central requiere rebote/colapso con fluidizacion, fuera de este modelo.
Pruebas superadas.
```

```bash
python programa/clases/B61/B61-C03-crateres-complejos-colapso-picos-centrales-y-terrazas/colapso.py
```

**Límites:** sin pico central, terrazas ni fluidización; la regla de pendiente es cinemática; no se valida con datos reales.

## 18. Errores frecuentes y cómo corregirlos

**Pensar que `D_sc ∝ 1/g` es exacto.** Se corrige con 8.1.

**Confundir calibrar con validar.** Se corrige con la sección 5.

**Tomar la divulgación como medida.** Se corrige con la sección 11.

**Creer que la relajación explica el pico central.** Se corrige con 8.3.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas y cuál obtuviste? Si dudas, repasa el ejemplo de la sección 13. Tras el laboratorio: ¿qué comprueba cada aserción? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de la transición simple–compleja** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Explica los conceptos de la clase | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas con unidades | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con una vía independiente | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular los datos sintéticos e ilustrativos; no presentar lo simulado como observado; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y no sustituyen un código de impactos (hidrocódigo) ni el análisis de datos reales. No se identifica ningún cráter concreto. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

La transición simple–compleja marca el momento en que la gravedad domina la forma, y un modelo mínimo la capta solo en parte. Queda una pregunta: ¿qué ocurre con el material expulsado?

**Glosario español–inglés.** cráter complejo · *complex crater*; pico central · *central peak*; terraza · *terrace*; ángulo crítico · *critical angle*; transición · *transition*.

**Continuidad.** [B61-C04](../B61-C04-mantos-de-ejecta-y-depositos-de-impacto/CLASE.md) estudia los mantos de ejecta.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B61-C02 — Cráteres simples: morfología y formación](../B61-C02-crateres-simples-morfologia-y-formacion/CLASE.md) · [📚 Bloque B61](../../../tronco-comun/B61-crateres-de-impacto-y-geologia-de-impactos.md) · [Siguiente: B61-C04 — Mantos de ejecta y depósitos de impacto →](../B61-C04-mantos-de-ejecta-y-depositos-de-impacto/CLASE.md)
<!-- /nav -->
