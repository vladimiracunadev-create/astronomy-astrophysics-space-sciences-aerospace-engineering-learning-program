# B114-C03 — Alarmas y procedimientos ante desviaciones atmosféricas

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B114](../../../tronco-comun/B114-seguridad-y-respuesta-a-emergencias-en-habitats.md) · [← Anterior: B114-C02 — Detección, localización y respuesta a fugas de presión](../B114-C02-deteccion-localizacion-y-respuesta-a-fugas-de-presion/CLASE.md) · [Siguiente: B114-C04 — Refugio contra tormentas solares y compartimentos de protección →](../B114-C04-refugio-contra-tormentas-solares-y-compartimentos-de-proteccion/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 3 del bloque B114. Nivel N3. Una alarma es una regla que convierte una señal ruidosa en una decisión: si el umbral es bajo suena sin motivo, si es alto suena tarde. Aquí calculas cuánto tarda en subir el CO₂ en un volumen cerrado, diseñas una alarma con confirmación e histéresis y mides sus falsas alarmas y su desfase con series **sintéticas**. El único umbral consultado es el de `3 mmHg` de ppCO₂ de NASA-STD-3001; los demás son ilustrativos. Usa [C02](../B114-C02-deteccion-localizacion-y-respuesta-a-fugas-de-presion/CLASE.md) para la lógica de presión.

## 2. Por qué esta clase existe

Un sensor correcto con una regla mala produce alarmas inútiles o tardías. La decisión central: **¿qué umbral, qué confirmación y qué histéresis dan pocas falsas alarmas sin perder tiempo de respuesta?**

## 3. Lo que podrás hacer al terminar

1. Calcular el aumento de ppCO₂ por tripulante y hora en un volumen cerrado.
2. Convertir mmHg, kPa y fracción molar.
3. Implementar una alarma con confirmación «m de n» e histéresis.
4. Medir falsas alarmas en régimen nominal y desfase ante una rampa.
5. Explicar por qué la histéresis evita activaciones repetidas.
6. Separar el umbral consultado de los parámetros ilustrativos.

La evidencia es la **tabla de umbrales y desempeño de alarma** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es una presión parcial?
2. ¿Cuántos Pa tiene un mmHg?
3. ¿Qué es una falsa alarma?
4. ¿Qué es un dato sintético?
5. ¿Qué es una verificación por segunda vía?

<details>
<summary>Ver respuestas</summary>

1. La presión que ejercería un gas de la mezcla si ocupara solo el volumen. 2. Unos 133,3 Pa. 3. Una alarma sin que exista la condición. 4. Un dato generado para el ejemplo, no medido. 5. Calcular lo mismo con otro método y comparar.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Cuatro personas (sintéticas) producen `1 kg/día` de CO₂ cada una en `100 m³` a `295,15 K`: sin eliminación, la ppCO₂ sube `0,697 mmHg/h` y alcanza `3 mmHg` en `4,3 h`. Con ruido de `0,15 mmHg`, una alarma simple da `176` falsas alarmas en 30 días de régimen nominal y la confirmada `3 de 5`, cero. Es el **ejemplo conductor**. Todo es **ilustrativo** salvo el umbral citado de `3 mmHg`.

## 6. Vocabulario

La **presión parcial** `ppCO₂` es la contribución del CO₂ a la presión total, en mmHg. El **umbral** es el valor que dispara la alarma. La **histéresis** es un segundo umbral más bajo para desactivarla. La **confirmación «m de n»** exige `m` muestras sobre el umbral entre las últimas `n`. La **falsa alarma** es una activación sin condición real.

## 7. Modelo mental: el termostato de una casa

```mermaid
flowchart LR
    S["sensor + ruido"] --> C["confirmacion m de n"]
    C --> U["umbral 3 mmHg"]
    U --> A["alarma activa"]
    A --> H["histeresis 2,7 mmHg"]
    H --> D["desactiva"]
```

*Descripción textual:* la señal con ruido pasa por la confirmación y el umbral y activa la alarma, que solo se desactiva al bajar del umbral de histéresis.

Analogía: un termostato no enciende y apaga la calefacción en cada fluctuación de `0,1 °C`, sino que tiene una banda. Límite: el modelo usa ruido gaussiano independiente; un sensor real tiene deriva, retrasos y fallos.

## 8. La explicación, paso a paso

### 8.1 Cuánto sube el CO₂

La masa generada `Δm` se convierte en presión parcial con la ley del gas ideal: `ppCO₂ = (Δm/M) R T/V`, con `M = 0,04401 kg/mol` y `R = 8,314 462 618 J/(mol K)`. Cuatro personas en una hora: `Δm = 0,1667 kg`, `ppCO₂ = 92,9 Pa = 0,697 mmHg`.

### 8.2 Dos vías

La segunda vía es la fracción molar `n_CO₂/n_aire` por `760 mmHg`: da `0,6971 mmHg`, la misma cifra. Con una persona, `+0,174 mmHg/h` y `17,2 h` hasta `3 mmHg`.

### 8.3 Falsas alarmas y desfase

En régimen nominal sintético (media `2,6 mmHg`, `σ = 0,15`), el umbral está a `2,67 σ`: la alarma simple se activa `176` veces en 30 días y la «3 de 5», ninguna. Ante una rampa de `0,0116 mmHg/min` desde `2,2 mmHg` (cruce teórico a los `68,9 min`), la alarma simple suena en el minuto `51` y la «3 de 5» en el `64`: ambas **antes** del cruce por el ruido, y la confirmada es menos precoz.

### 8.4 Histéresis

Una señal que oscila `±0,12 mmHg` alrededor de `3 mmHg` produce `98` activaciones sin histéresis y `1` con ella (umbral de desactivación `2,7 mmHg`). La confirmación y la histéresis **no son gratuitas**: añaden retraso y hay que ajustarlas con datos reales.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `ppCO₂` | presión parcial de CO₂ | mmHg | umbral 3 (NASA) |
| `V` | volumen | m³ | 100 (ilustrativo) |
| `T` | temperatura | K | 295,15 (ilustrativa) |
| `σ` | ruido del sensor | mmHg | 0,15 (sintético) |
| `G` | generación por persona | kg/día | 1,0 (ilustrativa) |
| `R` | constante molar de los gases | J/(mol K) | 8,314 462 618 |

## 10. Convenciones y referencias

`1 mmHg = 133,322 368 Pa`; `1 atm = 760 mmHg`. Mezcla homogénea, sin eliminación de CO₂ en la rampa, 1 muestra por minuto, ruido gaussiano. Python 3.12, biblioteca estándar.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA OCHMO, OCHMO-TB-004 «Carbon Dioxide», derivada de NASA-STD-3001 Vol. 2 Rev D — https://www.nasa.gov/wp-content/uploads/2023/12/ochmo-tb-004-carbon-dioxide.pdf (consultada 2026-11-10, PyMuPDF) | texto de `[V2 6004]` | ppCO₂ medio de 1 h ≤ 3 mmHg en el volumen habitable; 0,5 % CO₂ = 3,8 mmHg; cefaleas a 2,8–4,5 mmHg | Consultada |
| S2 | NASA OCHMO, OCHMO-TB-003 «Habitable Atmosphere», Rev A (2023) — https://www.nasa.gov/wp-content/uploads/2023/12/ochmo-tb-003-habitable-atmosphere.pdf (consultada 2026-11-10) | requisitos `[V1 6020]`–`[V1 6022]` | la norma exige registrar, mostrar y alertar cuando presión, ppO₂ y ppCO₂ salen de límites seguros | Consultada |
| S3 | NIST, CODATA 2022 — https://physics.nist.gov/cgi-bin/cuu/Value?r (consultada 2026-11-10) | `R` | 8,314 462 618… J mol⁻¹ K⁻¹ | Consultada |
| — | Rangos numéricos de ppO₂ (`[V2 6003]`) y límites de emergencia | — | umbrales de O₂ | No consultada |

Límites: `2,7 mmHg`, `m` y `n`, el ruido y la generación son ilustrativos; no se fija ningún umbral operativo.

## 12. Cómo ver una alarma

| Magnitud | Valor |
|---|---|
| ppCO₂ por hora (4 personas) | +0,697 mmHg |
| tiempo a 3 mmHg desde cero | 4,3 h |
| falsas alarmas simple / 3 de 5 | 176 / 0 |
| activaciones con y sin histéresis | 1 / 98 |

Descripción larga: la confirmación elimina las falsas alarmas del régimen nominal y la histéresis evita el parpadeo, a costa de algo de retraso.

## 13. Ejemplo trabajado: tiempo a 3 mmHg desde 2,2 mmHg

**Paso 1 · Pendiente.** `0,697 mmHg/h = 0,01162 mmHg/min`.

**Paso 2 · Margen.** `3,0 − 2,2 = 0,8 mmHg`.

**Paso 3 · Tiempo.** `0,8/0,01162 = 68,9 min`.

**Paso 4 · Lectura.** Es el tiempo teórico sin ruido; el laboratorio muestra que el ruido adelanta la alarma simple.

## 14. Distintas formas de describir una alarma

**Por umbral:** valor que la dispara. **Por confirmación:** `m` de `n`. **Por histéresis:** banda. **Por desempeño:** falsas alarmas y desfase. **Por tiempo:** margen hasta el límite.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Convierte `3 mmHg` a kPa. *Pasos:* multiplica por `133,322 Pa/mmHg` y divide por 1000.

<details><summary>Solución comentada</summary>

`3 × 133,322 = 399,97 Pa = 0,400 kPa`.
</details>

**Ejercicio 2 · con una pista.** ¿Qué fracción molar de CO₂ es `3,8 mmHg` a 1 atm? *Pista:* divide por `760`.

<details><summary>Solución comentada</summary>

`3,8/760 = 0,005 = 0,5 %`; coincide con el dato citado por la NASA.
</details>

**Ejercicio 3 · casi autónomo.** ¿Por qué la alarma «3 de 5» tiene cero falsas alarmas en el régimen nominal?

<details><summary>Solución comentada</summary>

Una excursión aislada sobre `3 mmHg` rara vez se repite tres veces en cinco minutos con ruido independiente.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** ¿Cuántas horas tardan dos personas en subir el CO₂ `1 mmHg` en `100 m³`?

<details><summary>Solución comentada</summary>

`0,1743 × 2 = 0,3486 mmHg/h`; `1/0,3486 = 2,87 h`.
</details>

**Ejercicio 5 · autónomo.** ¿A cuántas desviaciones típicas está el umbral de la media nominal `2,6 mmHg` con `σ = 0,15`?

<details><summary>Solución comentada</summary>

`(3,0 − 2,6)/0,15 = 2,67 σ`.
</details>

**Ejercicio 6 · autónomo.** ¿Qué pasa con el tiempo a `3 mmHg` si el volumen se duplica a `200 m³`?

<details><summary>Solución comentada</summary>

La pendiente se divide por 2 y el tiempo se duplica: `8,6 h` desde cero con cuatro personas.
</details>

**Ejercicio 7 · autónomo.** ¿Por qué `m = n` elimina el beneficio de la confirmación?

<details><summary>Solución comentada</summary>

Exigir todas las muestras equivale a un retraso fijo de `n` muestras y no filtra el ruido de forma gradual.
</details>

**Ejercicio 8 · autónomo.** Si el umbral de histéresis sube a `2,95 mmHg`, ¿qué pasa con el parpadeo?

<details><summary>Solución comentada</summary>

La banda se estrecha y reaparecen activaciones repetidas; hay que ajustarla al ruido (`≈ 2σ` de ancho como orientación).
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un colega propone bajar el umbral a `2,0 mmHg` «por seguridad». ¿Qué le responderías?

<details><summary>Solución comentada</summary>

Con ruido y media nominal cercanos, sonaría casi siempre; una alarma que suena sin cesar se ignora, y eso es una pérdida de seguridad.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Qué cambia si la señal es la presión total y no el CO₂?

<details><summary>Solución comentada</summary>

La alarma debería mirar también la tasa de caída (`dP/dt`), como en C02, porque una fuga lenta no cruza un umbral absoluto durante días.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Qué te falta para fijar umbrales reales de O₂?

<details><summary>Solución comentada</summary>

El rango de `[V2 6003]` y el procedimiento del programa, que no se consultaron; esta clase no los trae.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *tabla de umbrales y desempeño de alarma*: umbral, histéresis, `m` de `n`, falsas alarmas, desfase ante rampa, y lista de qué es consultado, sintético y no consultado.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: alarma de CO₂ en un hábitat sintético

El script [alarmas.py](alarmas.py) calcula la acumulación de CO₂, la verifica con la fracción molar, simula 30 días nominales y una rampa con semillas `114` y `115`, y compara alarma simple, confirmada e histéresis (**comprueba** acuerdo de dos vías < 1 % y menos activaciones con histéresis).

**Datos:** todos **sintéticos** salvo el umbral de 3 mmHg. **Predice antes de ejecutar:** ¿cuántas activaciones esperas con histéresis? (una.) **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Habitat SINTETICO: V = 100 m3, T = 295.15 K, 1.0 kg CO2/dia/persona (ilustrativo)
ppCO2 por persona y hora sin eliminacion:
  1 persona(s): +0.1743 mmHg/h ; 3 mmHg en 17.2 h
  4 persona(s): +0.6971 mmHg/h ; 3 mmHg en 4.3 h
  segunda via (fraccion molar x 760 mmHg), 4 personas, 1 h: 0.6971 mmHg
Regimen nominal 30 dias (sintetico), ppCO2 media 2.6 mmHg, sigma = 0.15:
  simple (1 de 1)        falsas alarmas = 176
  confirmada (3 de 5)    falsas alarmas = 0
Rampa (4 personas, sin eliminacion): cruce teorico a los 68.9 min
  alarma simple  dispara en el minuto 51 (desfase = -18 min; negativo = antes del cruce, por ruido)
  alarma 3 de 5  dispara en el minuto 64 (desfase = -5 min; negativo = antes del cruce, por ruido)
Senal oscilante en el umbral: activaciones sin histeresis = 98 ; con = 1
Pruebas superadas.
```

```bash
python programa/clases/B114/B114-C03-alarmas-y-procedimientos-ante-desviaciones-atmosfericas/alarmas.py
```

**Límites:** ruido gaussiano independiente, un solo gas, mezcla homogénea y sin fallos del sensor; el desfase negativo muestra que el ruido adelanta la alarma, no que el sistema sea mejor.

## 18. Errores frecuentes y cómo corregirlos

**Bajar el umbral «por seguridad».** Se corrige con el ejercicio 9.

**Ignorar el ruido al elegir el umbral.** Se corrige con 8.3.

**Quitar la histéresis y tener parpadeo.** Se corrige con 8.4.

**Tomar el umbral ilustrativo como norma.** Se corrige con la sección 11.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿cuántas horas esperabas hasta `3 mmHg` y cuántas obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **tabla de umbrales y desempeño de alarma** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Distingue umbral, confirmación e histéresis | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas con unidades | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Dos vías para el CO₂ | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo sintético y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular lo ilustrativo y sintético; no presentar un umbral como procedimiento operativo; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: no es consejo médico ni operativo y no sustituye a las normas ni a los procedimientos de ningún programa. Los umbrales de CO₂ y O₂ de una nave o un hábitat reales los fija la norma vigente y la autoridad médica del programa. Los datos son sintéticos y los modelos simplificados. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Cuatro personas elevan el CO₂ `0,7 mmHg` por hora en `100 m³` sin eliminación, y una alarma «3 de 5» con histéresis evita `176` falsas alarmas en 30 días. Queda una pregunta: ¿cómo se protege la tripulación de una tormenta solar?

**Glosario español–inglés.** presión parcial · *partial pressure*; histéresis · *hysteresis*; falsa alarma · *false alarm*; umbral · *threshold*; confirmación · *confirmation (m-of-n)*.

**Continuidad.** [B114-C04](../B114-C04-refugio-contra-tormentas-solares-y-compartimentos-de-proteccion/CLASE.md) estudia los refugios contra tormentas solares.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B114-C02 — Detección, localización y respuesta a fugas de presión](../B114-C02-deteccion-localizacion-y-respuesta-a-fugas-de-presion/CLASE.md) · [📚 Bloque B114](../../../tronco-comun/B114-seguridad-y-respuesta-a-emergencias-en-habitats.md) · [Siguiente: B114-C04 — Refugio contra tormentas solares y compartimentos de protección →](../B114-C04-refugio-contra-tormentas-solares-y-compartimentos-de-proteccion/CLASE.md)
<!-- /nav -->
