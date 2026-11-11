# B119-C02 — Acuerdo de Salvamento

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B119](../../../tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md) · [← Anterior: B119-C01 — Tratado del Espacio Ultraterrestre](../B119-C01-tratado-del-espacio-ultraterrestre/CLASE.md) · [Siguiente: B119-C03 — Convenio de Responsabilidad →](../B119-C03-convenio-de-responsabilidad/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 2 del bloque B119. Nivel N3. Cuando una nave tripulada o un objeto espacial regresa a un lugar imprevisto, el derecho impone deberes de notificación, auxilio y devolución. Aquí estudias esas obligaciones como las describe la literatura oficial consultada y calculas con un modelo geométrico la probabilidad de que un retorno de emergencia sintético caiga en el territorio de un Estado, para dimensionar a quién habría que notificar. **Esta clase es educativa: no es asesoría legal, regulatoria ni financiera y no sustituye a un jurista, a una autoridad competente ni a un asesor.**

## 2. Por qué esta clase existe

El tratado de 1967 (C01) menciona la asistencia a los astronautas (art. V, no discutido en la fuente consultada); el Acuerdo de Salvamento la desarrolla, y ninguna otra clase la cubre. La decisión central: **¿a qué Estados conviene tener preparados los canales de notificación según dónde pueda caer un retorno de emergencia?**

## 3. Lo que podrás hacer al terminar

1. Enunciar los deberes generales de notificación, auxilio y devolución, rotulando que el texto del Acuerdo no se consultó.
2. Calcular la fracción de superficie alcanzable desde una inclinación orbital dada.
3. Calcular la probabilidad de aterrizar en una banda de latitud (Estado sintético) y compararla con un Monte Carlo.
4. Calcular la probabilidad de al menos un aterrizaje en `k` eventos independientes.
5. Separar lo consultado (texto normativo con versión y fecha) de lo sintético o ilustrativo.

La evidencia es la **ficha de un caso de salvamento sintético** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es la inclinación orbital?
2. ¿Qué fracción del área de una esfera está entre las latitudes `−φ` y `+φ`?
3. ¿Qué es una probabilidad condicional?
4. ¿Qué es un Monte Carlo?
5. ¿Cómo se calcula P(al menos uno) en `k` eventos independientes?

<details>
<summary>Ver respuestas</summary>

1. El ángulo entre el plano de la órbita y el ecuador. 2. `sin φ`. 3. La de un suceso dado que ocurrió otro. 4. Estimar una probabilidad con muchos sorteos aleatorios reproducibles. 5. `1 − (1 − p)^k`.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

La página de UNOOSA del Acuerdo sobre la Luna (consultada el 2026-11-11) indica que los objetos hallados fuera del lugar previsto se tratan según el art. 5 del Acuerdo de Salvamento. El **texto del Acuerdo de Salvamento no se pudo consultar** (la página devolvió 404): lo que se dice de sus obligaciones (notificar, auxiliar, devolver personal y objetos, con gastos a cargo de la autoridad de lanzamiento) es «no consultado» y debe verificarse en la fuente oficial. El **ejemplo conductor** es un retorno de emergencia sintético desde una órbita de inclinación 51,6°, con un «Estado X» sintético que ocupa la banda 20°–30° N.

## 6. Vocabulario

La **autoridad de lanzamiento** es el Estado u organización responsable del lanzamiento. La **devolución** es la restitución del personal o del objeto. La **notificación** es el aviso a la autoridad de lanzamiento y al Secretario General de la ONU. La **banda alcanzable** es la franja de latitudes `|φ| ≤ i` que sobrevuela la traza de la órbita.

## 7. Modelo mental

```mermaid
flowchart LR
    I["Inclinación i"] --> B["Banda |lat| ≤ i"]
    B --> P["P(caer en banda del Estado X)"]
    P --> K["P(al menos uno en k eventos)"]
    K --> N["Canales de notificación preparados"]
```

*Descripción textual:* la inclinación fija la banda alcanzable; de la banda se obtiene la probabilidad de caer en un territorio; con varios eventos se decide qué canales preparar.

Analogía: el área de un cinturón en una esfera: lo que cae al azar se reparte en proporción al área. Límite: un retorno real no es uniforme (la trayectoria, el viento y la guía lo concentran) y un Estado no es una banda de latitud.

## 8. La explicación, paso a paso

### 8.1 Lo que se afirma de las obligaciones (no consultado)

Se cita el contenido general (notificar, auxiliar, devolver) **sin** texto verificado; la fuente oficial es la página de UNOOSA del Acuerdo, que no se pudo leer. Lo único consultado es la remisión del art. 12 del Acuerdo sobre la Luna al art. 5 del Acuerdo de Salvamento.

### 8.2 Banda alcanzable

Con `i = 51,6°`, la fracción de superficie terrestre en `|φ| ≤ i` es `sin i = 0.7837`.

### 8.3 Probabilidad de caer en el Estado X

Aterrizaje uniforme en la banda: `P = (sin 30° − sin 20°)/(2 sin i) = 0.10079`. El Monte Carlo (400 000 sorteos, semilla 119) da `0.10140`, dentro de tres sigmas binomiales.

### 8.4 Varios eventos

`P(≥1)` en 5 y 10 retornos independientes: `0.4121` y `0.6544`. Una probabilidad pequeña por evento se acumula.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `i` | inclinación orbital | ° | 51,6 (ilustrativo) |
| `φ` | latitud | ° | — |
| `p` | P(caer en X) | — | 0.10079 |
| `k` | número de eventos | — | 1, 5, 10 |

## 10. Convenciones y referencias

Latitudes en grados; probabilidades adimensionales; Estado X sintético. Fecha de consulta: 2026-11-11.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S2 | UNOOSA, «Agreement Governing the Activities of States on the Moon and Other Celestial Bodies» (página oficial), https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/moon-agreement.html (WebFetch, consultada 2026-11-11) | art. 12 | remisión al art. 5 del Acuerdo de Salvamento y uso de equipo ajeno en emergencias | Consultada |
| S3 | ONU, Biblioteca Audiovisual de Derecho Internacional, nota introductoria sobre el Tratado del Espacio Ultraterrestre, https://legal.un.org/avl/ha/tos/tos.html (WebFetch, consultada 2026-11-11; no discute los artículos V ni VII) | art. V no discutido | el tratado de 1967 contiene el principio de asistencia que la nota consultada no desarrolla | Consultada |
| — | Texto del Acuerdo de Salvamento (arts. 1–6) | — | no consultado (404) | No consultado / ilustrativo |
| — | Geometría esférica, Monte Carlo | — | no consultada en una fuente concreta; verificada por dos vías | No consultado / ilustrativo |
| — | Inclinación 51,6° y Estado X | — | ilustrativos / sintéticos | No consultado / ilustrativo |

Límites: el texto del Acuerdo de Salvamento no se consultó; el modelo es geométrico y no representa un retorno real. Texto normativo parafraseado de las páginas oficiales en la fecha indicada; el texto vinculante es el de la fuente oficial vigente.

## 12. Cómo ver la situación

| Magnitud | Valor |
|---|---|
| Fracción alcanzable | 0.7837 |
| `p` analítica | 0.10079 |
| `p` Monte Carlo | 0.10140 |
| `P(≥1)` en 10 eventos | 0.6544 |

Descripción larga: la banda alcanzable cubre casi cuatro quintos de la superficie; la probabilidad por evento de caer en la banda sintética es pequeña pero crece con el número de eventos.

## 13. Ejemplo trabajado: cinco retornos

**Paso 1.** `p = 0.10079`. **Paso 2.** Con `k = 5`: `1 − (1 − p)^5 = 0.4121`. **Paso 3.** Lectura: en cinco retornos hipotéticos hay una probabilidad `0.4121` de que al menos uno caiga en X; esto no predice nada real.

## 14. Distintas formas de describirlo

**Por geometría:** banda y casquete. **Por Monte Carlo:** frecuencia. **Por obligación:** notificar, auxiliar, devolver (no consultado). **Por actor:** autoridad de lanzamiento y Estado de aterrizaje.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `sin 51,6°`.

<details><summary>Solución comentada</summary>

`0.7837`.
</details>

**Ejercicio 2 · con una pista.** Calcula `sin 30° − sin 20°`. *Pista:* `0,5 − 0,3420`.

<details><summary>Solución comentada</summary>

`0,1580`.
</details>

**Ejercicio 3 · casi autónomo.** Divide el resultado anterior por `2 sin i`.

<details><summary>Solución comentada</summary>

`0,1580/1,5674 = 0.10079`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Calcula `P(≥1)` en 5 eventos.

<details><summary>Solución comentada</summary>

`0.4121`.
</details>

**Ejercicio 5 · autónomo.** ¿Cuántos eventos hacen falta para que `P(≥1) > 0,5`?

<details><summary>Solución comentada</summary>

`k > ln 0,5/ln(1 − p)`; con `p = 0.10079`, siete eventos (`1 − 0,8992^7 = 0,528`; con seis queda en 0,471).
</details>

**Ejercicio 6 · autónomo.** Si la inclinación bajara a 28,5°, ¿qué pasa con la fracción alcanzable?

<details><summary>Solución comentada</summary>

`sin 28,5° = 0,4772`: baja de 0,78 a 0,48.
</details>

**Ejercicio 7 · autónomo.** ¿Qué ocurre con `p` si el Estado X se ensancha a 20°–40° N?

<details><summary>Solución comentada</summary>

`(0,6428 − 0,3420)/1,5674 = 0,1919`.
</details>

**Ejercicio 8 · autónomo.** ¿Qué afirmación de la clase es «no consultada»?

<details><summary>Solución comentada</summary>

El contenido de los arts. 1–6 del Acuerdo de Salvamento.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** ¿Por qué el aterrizaje real no es uniforme y qué cambia en el modelo?

<details><summary>Solución comentada</summary>

Porque hay guía, trayectoria y zonas de aterrizaje planificadas; habría que usar una densidad no uniforme.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** Un objeto sin tripulación aparece en un territorio ajeno. ¿Qué dato del Acuerdo sobre la Luna remite al régimen de devolución?

<details><summary>Solución comentada</summary>

El art. 12, que remite al art. 5 del Acuerdo de Salvamento (S2).
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Por qué no sirve esta probabilidad para exigir nada a un Estado real?

<details><summary>Solución comentada</summary>

Es un modelo con territorio sintético; no es una opinión jurídica ni una predicción.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de un caso de salvamento sintético*: obligaciones (con lo no consultado rotulado), banda, probabilidades y aviso de que es educativa.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: aterrizaje sintético y notificación

El script [laboratorio.py](laboratorio.py) calcula la fracción alcanzable, la probabilidad de caer en una banda sintética y la acumulada en `k` eventos (**comprueba** el Monte Carlo contra la fórmula a tres sigmas).

**Datos:** solo la remisión del art. 12 consultada (2026-11-11); el resto **sintético o ilustrativo**. **Predice antes de ejecutar:** ¿cuál será la probabilidad por evento de caer en la banda 20°–30° N? (en torno a un décimo.) **Ejecución del 2026-11-11 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Aterrizaje SINTETICO uniforme en |lat| <= 51.6 deg; Estado X sintetico = banda 20-30 N; Acuerdo de Salvamento NO consultado (404).
Probabilidad de caer en el Estado X: Monte Carlo 0.10140 ; analitica 0.10079 ; sigma 0.00048
   1 retornos de emergencia: P(al menos uno cae en X) = 0.1008
   5 retornos de emergencia: P(al menos uno cae en X) = 0.4121
  10 retornos de emergencia: P(al menos uno cae en X) = 0.6544
Fraccion de la superficie terrestre alcanzable desde i=51.6: 0.7837
CLAVES {"p_mc": "0.10140", "p_an": "0.10079", "p10": "0.6544", "banda": "0.7837", "p5": "0.4121"}
Pruebas superadas.
```

```bash
python programa/clases/B119/B119-C02-acuerdo-de-salvamento/laboratorio.py
```

**Límites:** la distribución uniforme y el Estado en forma de banda son didácticos; el Acuerdo de Salvamento no se consultó.

## 18. Errores frecuentes y cómo corregirlos

**Citar el contenido del Acuerdo como si se hubiera leído.** Se corrige con la sección 8.1.

**Usar `sin φ` en grados en una calculadora en radianes.** Se corrige con la sección 10.

**Sumar probabilidades en lugar de componerlas.** Se corrige con el ejercicio 4.

**Creer que la banda alcanzable es toda la Tierra.** Se corrige con el ejercicio 6.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas en el ejemplo trabajado y cuál obtuviste? Si dudas, repasa la sección 13. Tras el laboratorio: ¿qué comprueba cada prueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de un caso de salvamento sintético** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Usa el vocabulario con precisión | Explica los límites del modelo |
| Cálculo | Sin unidades | Con errores | Resultados con unidades y tolerancia | Calcula casos nuevos |
| Verificación | Sin comprobar | Un caso | Contraste con una segunda vía | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con versión, fecha y estado | Declara lo sintético y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** citar la versión y la fecha del texto normativo consultado; rotular lo sintético y lo ilustrativo; no presentar un resultado como asesoría legal, regulatoria o financiera.

## 21. Ética, seguridad y límites

Clase educativa: **no es asesoría legal, regulatoria ni financiera**; no sustituye a un abogado, a la autoridad competente ni a un asesor, y ningún resultado debe usarse para decidir sobre una licencia, una reclamación, un contrato o una operación real. La clase trata un caso humanitario: la prioridad real es la vida de la tripulación y la decide la autoridad competente, no este modelo. Los modelos son simplificados y sus datos son sintéticos o ilustrativos; lo simulado nunca se presenta como observado. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Con inclinación 51,6° la banda alcanzable cubre `0.7837` de la Tierra y la probabilidad por evento de caer en el Estado sintético es `0.10079`. Queda una pregunta: ¿quién paga el daño cuando lo que cae daña a un tercero?

**Glosario español–inglés.** autoridad de lanzamiento · *launching authority*; devolución · *return*; banda alcanzable · *reachable band*; salvamento · *rescue*.

**Continuidad.** [B119-C03](../B119-C03-convenio-de-responsabilidad/CLASE.md): el Convenio de Responsabilidad.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B119-C01 — Tratado del Espacio Ultraterrestre](../B119-C01-tratado-del-espacio-ultraterrestre/CLASE.md) · [📚 Bloque B119](../../../tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md) · [Siguiente: B119-C03 — Convenio de Responsabilidad →](../B119-C03-convenio-de-responsabilidad/CLASE.md)
<!-- /nav -->
