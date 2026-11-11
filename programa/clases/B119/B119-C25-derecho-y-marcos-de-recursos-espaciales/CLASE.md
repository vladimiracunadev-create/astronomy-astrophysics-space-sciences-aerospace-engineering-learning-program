# B119-C25 — Derecho y marcos de recursos espaciales

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B119](../../../tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md) · [← Anterior: B119-C24 — Límites legales y de seguridad de la experimentación educativa](../B119-C24-limites-legales-y-de-seguridad-de-la-experimentacion-educativa/CLASE.md) · [Siguiente: B119-C26 — Doctrinas y políticas espaciales declaradas públicamente →](../B119-C26-doctrinas-y-politicas-espaciales-declaradas-publicamente/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 25 del bloque B119. Nivel N3. Si hay agua o minerales útiles fuera de la Tierra, ¿quién puede extraerlos y venderlos? El art. 11 del Acuerdo sobre la Luna los declara patrimonio común y el art. II del tratado de 1967 excluye la apropiación nacional; las leyes y acuerdos posteriores interpretan esto de maneras distintas (no consultadas). Aquí calculas con la ecuación del cohete qué ahorro daría un propergol obtenido en el espacio y cuál sería su precio máximo, en un caso de negocio **sintético**. **Esta clase es educativa: no es asesoría legal, regulatoria ni financiera y no sustituye a un jurista, a una autoridad competente ni a un asesor.**

## 2. Por qué esta clase existe

B119 trata los tratados en general (C01, C05) y ninguna clase enseña los marcos de recursos ni el razonamiento económico que los motiva. La gobernanza se desarrolla en C36 y los aspectos técnicos en B59. La decisión central: **¿cuánto valdría un propergol obtenido en el espacio y qué preguntas jurídicas abre su venta?**

## 3. Lo que podrás hacer al terminar

1. Citar el art. 11 del Acuerdo sobre la Luna y el art. II del tratado, y rotular lo no consultado (Acuerdos Artemis, leyes nacionales).
2. Calcular la razón de masas y el propergol necesario con la ecuación del cohete, incluida la fracción estructural.
3. Calcular el ahorro de lanzamiento y el precio máximo del propergol en el depósito.
4. Medir la sensibilidad al impulso específico.
5. Separar lo consultado (texto normativo con versión y fecha) de lo sintético o ilustrativo.

La evidencia es la **caso de negocio sintético de un recurso** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es el impulso específico?
2. ¿Qué dice la ecuación de Tsiolkovsky?
3. ¿Qué es la masa seca?
4. ¿Qué es un punto de equilibrio?
5. ¿Qué es un depósito de propergol?

<details>
<summary>Ver respuestas</summary>

1. La eficiencia del propergol, en segundos. 2. `Δv = Isp g₀ ln(m₀/m_f)`. 3. La masa del vehículo sin propergol. 4. El valor en que ingresos y costes se igualan. 5. Un almacén en órbita que provee combustible a otros vehículos.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

El Acuerdo sobre la Luna (UNOOSA, consultado el 2026-11-11) dice en su art. 11 que la Luna y sus recursos son patrimonio común de la humanidad, que colocar equipo no crea propiedad y que se creará un régimen internacional; la nota de la ONU recoge el art. II del tratado (sin apropiación nacional). **No se consultaron** los Acuerdos Artemis ni las leyes nacionales sobre recursos, ni su interpretación. El **ejemplo conductor**: una carga útil de 1000 kg que requiere `Δv = 3800 m/s` con `I_sp = 450 s`, un coste sintético de lanzar 2500 u.m./kg y una estructura del 10 % del propergol.

## 6. Vocabulario

La **utilización de recursos in situ** (ISRU) obtiene insumos fuera de la Tierra. El **propergol** es combustible más oxidante. La **razón de masas** es `m₀/m_f`. El **precio máximo** es el que iguala el ahorro. El **régimen internacional** es el conjunto de reglas por crear (art. 11).

## 7. Modelo mental

```mermaid
flowchart LR
    R["Recurso (agua)"] --> P["Propergol en el espacio"]
    P --> D["Depósito"]
    D --> A["Ahorro de lanzamiento"]
    A --> V["Precio máximo"]
    L["Marco legal"] -.-> R
```

*Descripción textual:* el recurso produce propergol en un depósito, lo que ahorra lanzamientos; el ahorro fija el precio máximo; el marco legal condiciona el acceso al recurso.

Analogía: comprar combustible en una gasolinera del camino en vez de cargarlo todo desde el punto de partida: ahorras peso, pero dependes de que la gasolinera exista y sea legal. Límite: aquí el marco jurídico no se resuelve.

## 8. La explicación, paso a paso

### 8.1 Ecuación del cohete

Razón de masas `2.3657`. Con estructura del 10 % del propergol, el propergol es `1582 kg` y la masa inicial `2740 kg`. La recomposición de la razón de masas coincide a `10⁻⁹`.

### 8.2 Coste y ahorro

Lanzar todo: `6.85 M u.m.`. Si el propergol se obtiene en el espacio, el ahorro es `3.95 M u.m.`, es decir `2500 u.m./kg` de propergol: es el precio máximo del propergol en el depósito.

### 8.3 Sensibilidad

Con `I_sp` bajo, el propergol necesario crece y el ahorro también. Con valores aún menores la misión se vuelve inviable con esa fracción estructural.

### 8.4 Lo jurídico

El modelo supone que el vendedor puede extraer y vender sin objeciones; eso depende de marcos (art. 11, art. II, leyes nacionales, acuerdos) que no se resuelven aquí (C36).

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `Δv` | incremento de velocidad | m/s | 3800 (ilustrativo) |
| `I_sp` | impulso específico | s | 450 |
| `m₀/m_f` | razón de masas | — | 2.3657 |
| precio máx. | ahorro por kg de propergol | u.m./kg | 2500 |

## 10. Convenciones y referencias

SI; `g₀ = 9,80665 m/s²`; u.m. = unidades monetarias sintéticas.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S2 | UNOOSA, «Agreement Governing the Activities of States on the Moon and Other Celestial Bodies» (página oficial), https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/moon-agreement.html (WebFetch, consultada 2026-11-11) | art. 11 | patrimonio común, ausencia de propiedad en el lugar y régimen internacional futuro | Consultada |
| S3 | ONU, Biblioteca Audiovisual de Derecho Internacional, nota introductoria sobre el Tratado del Espacio Ultraterrestre, https://legal.un.org/avl/ha/tos/tos.html (WebFetch, consultada 2026-11-11; no discute los artículos V ni VII) | art. II | sin apropiación nacional | Consultada |
| — | Acuerdos Artemis, leyes nacionales sobre recursos espaciales y su interpretación | — | no consultados | No consultado / ilustrativo |
| — | Ecuación de Tsiolkovsky | — | no consultada en una fuente concreta; verificada por recomposición | No consultado / ilustrativo |
| — | Δv, costes y carga | — | sintéticos | No consultado / ilustrativo |

Límites: no se consultó ningún marco de recursos posterior a 1979; los valores económicos son sintéticos. Texto normativo parafraseado de las páginas oficiales en la fecha indicada; el texto vinculante es el de la fuente oficial vigente.

## 12. Cómo ver la situación

| Magnitud | Valor |
|---|---|
| Razón de masas | 2.3657 |
| Propergol | 1582 kg |
| Ahorro | 3.95 M u.m. |
| Precio máximo | 2500 u.m./kg |

Descripción larga: el propergol pesa más de la mitad de la masa inicial; el ahorro por kg coincide con el coste de lanzamiento.

## 13. Ejemplo trabajado: la razón de masas

**Paso 1.** `Δv/(I_sp g₀) = 3800/(450 × 9,80665) = 0,8611`. **Paso 2.** `m₀/m_f = e^0,8611 = 2.3657`. **Paso 3.** Propergol `(r − 1) m_c/(1 − (r − 1) f) = 1582 kg`.

## 14. Distintas formas de describirlo

**Por física:** razón de masas. **Por economía:** ahorro y precio máximo. **Por derecho:** patrimonio común, no apropiación. **Por riesgo:** disponibilidad y regímenes.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `Δv/(I_sp g₀)`.

<details><summary>Solución comentada</summary>

`0,8611`.
</details>

**Ejercicio 2 · con una pista.** Calcula `e^0,8611`. *Pista:* `e^0,86 ≈ 2,36`.

<details><summary>Solución comentada</summary>

`2.3657`.
</details>

**Ejercicio 3 · casi autónomo.** Calcula el propergol con la fórmula del ejemplo.

<details><summary>Solución comentada</summary>

`1582 kg`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Calcula el coste de lanzar la masa inicial.

<details><summary>Solución comentada</summary>

`6.85 M u.m.`.
</details>

**Ejercicio 5 · autónomo.** ¿Cuál es el ahorro si el propergol se obtiene en el espacio?

<details><summary>Solución comentada</summary>

`3.95 M u.m.`.
</details>

**Ejercicio 6 · autónomo.** ¿Cuál es el precio máximo?

<details><summary>Solución comentada</summary>

`2500 u.m./kg`.
</details>

**Ejercicio 7 · autónomo.** ¿Qué pasa con el ahorro si el coste de lanzamiento se reduce a la mitad?

<details><summary>Solución comentada</summary>

Se reduce a la mitad.
</details>

**Ejercicio 8 · autónomo.** ¿Qué dice el art. 11 sobre la propiedad de los recursos en el lugar?

<details><summary>Solución comentada</summary>

Que no hay propiedad en el lugar por colocar equipo; los recursos son patrimonio común.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** ¿Por qué el ahorro depende del coste de lanzamiento?

<details><summary>Solución comentada</summary>

Porque el recurso espacial compite con lanzar el propergol desde la Tierra.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Qué pregunta jurídica plantea vender un recurso extraído?

<details><summary>Solución comentada</summary>

Si la extracción y venta equivalen a apropiación o están permitidas por el marco aplicable; no se resuelve aquí.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Por qué un modelo económico no zanja el debate?

<details><summary>Solución comentada</summary>

Porque la viabilidad económica no determina la licitud.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *caso de negocio sintético de un recurso*: física, ahorro, precio máximo, sensibilidad y aviso de que no es asesoría financiera ni legal.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: propergol espacial y precio máximo

El script [laboratorio.py](laboratorio.py) resuelve la ecuación del cohete con fracción estructural, calcula el ahorro y el precio máximo y varía el impulso específico (**comprueba** la razón de masas recompuesta a `10⁻⁹`).

**Datos:** art. 11 del Acuerdo sobre la Luna y art. II consultados (2026-11-11); `Δv`, costes y carga **sintéticos**. **Predice antes de ejecutar:** ¿cuánto pesa el propergol respecto de la carga útil? (más de una vez y media la carga.) **Ejecución del 2026-11-11 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Caso SINTETICO; arts. 11 (Luna) y II (tratado) consultados 2026-11-11; Acuerdos Artemis y leyes nacionales NO consultados.
Razon de masas exp(dv/(Isp g0)) = 2.3657 ; propergol 1582 kg ; masa inicial 2740 kg ; masa seca 1158 kg
Lanzar todo desde la Tierra: 6.85 M u.m.
Con el propergol obtenido en el espacio, se lanza solo 1158 kg: ahorro 3.95 M u.m. = 2500 u.m. por kg de propergol
   precio del propergol en el deposito    500 u.m./kg -> ahorro neto   3.16 M u.m. (conviene)
   precio del propergol en el deposito   1500 u.m./kg -> ahorro neto   1.58 M u.m. (conviene)
   precio del propergol en el deposito   2500 u.m./kg -> ahorro neto   0.00 M u.m. (no conviene)
   precio del propergol en el deposito   3500 u.m./kg -> ahorro neto  -1.58 M u.m. (no conviene)
   Isp   350 s: propergol    2540 kg
   Isp   450 s: propergol    1582 kg
   Isp   465 s: propergol    1495 kg
CLAVES {"r": "2.3657", "prop": "1582", "m0": "2740", "ct": "6.85", "ah": "3.95", "pk": "2500", "mf": "1158"}
Pruebas superadas.
```

```bash
python programa/clases/B119/B119-C25-derecho-y-marcos-de-recursos-espaciales/laboratorio.py
```

**Límites:** sin transporte, producción, tiempos ni riesgo; no es una valoración ni asesoría financiera.

## 18. Errores frecuentes y cómo corregirlos

**Confundir ahorro con rentabilidad.** Se corrige con 8.2.

**Olvidar la masa estructural.** Se corrige con el ejemplo trabajado.

**Dar por resuelto el marco legal.** Se corrige con 8.4.

**Tomar el precio máximo como precio de mercado.** Se corrige con el ejercicio 11.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas en el ejemplo trabajado y cuál obtuviste? Si dudas, repasa la sección 13. Tras el laboratorio: ¿qué comprueba cada prueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **caso de negocio sintético de un recurso** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Usa el vocabulario con precisión | Explica los límites del modelo |
| Cálculo | Sin unidades | Con errores | Resultados con unidades y tolerancia | Calcula casos nuevos |
| Verificación | Sin comprobar | Un caso | Contraste con una segunda vía | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con versión, fecha y estado | Declara lo sintético y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** citar la versión y la fecha del texto normativo consultado; rotular lo sintético y lo ilustrativo; no presentar un resultado como asesoría legal, regulatoria o financiera.

## 21. Ética, seguridad y límites

Clase educativa: **no es asesoría legal, regulatoria ni financiera**; no sustituye a un abogado, a la autoridad competente ni a un asesor, y ningún resultado debe usarse para decidir sobre una licencia, una reclamación, un contrato o una operación real. Los recursos espaciales plantean cuestiones de equidad y gobernanza (C34, C36); esta clase no toma partido. Los modelos son simplificados y sus datos son sintéticos o ilustrativos; lo simulado nunca se presenta como observado. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

El precio máximo sintético del propergol es `2500` u.m./kg y la razón de masas `2.3657`. Queda una pregunta: ¿qué dicen los Estados públicamente sobre sus políticas espaciales?

**Glosario español–inglés.** recursos espaciales · *space resources*; ecuación del cohete · *rocket equation*; razón de masas · *mass ratio*; depósito de propergol · *propellant depot*.

**Continuidad.** [B119-C26](../B119-C26-doctrinas-y-politicas-espaciales-declaradas-publicamente/CLASE.md): las doctrinas y políticas espaciales declaradas públicamente.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B119-C24 — Límites legales y de seguridad de la experimentación educativa](../B119-C24-limites-legales-y-de-seguridad-de-la-experimentacion-educativa/CLASE.md) · [📚 Bloque B119](../../../tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md) · [Siguiente: B119-C26 — Doctrinas y políticas espaciales declaradas públicamente →](../B119-C26-doctrinas-y-politicas-espaciales-declaradas-publicamente/CLASE.md)
<!-- /nav -->
