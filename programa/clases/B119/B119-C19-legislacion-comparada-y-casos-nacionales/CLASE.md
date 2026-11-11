# B119-C19 — Legislación comparada y casos nacionales

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B119](../../../tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md) · [← Anterior: B119-C18 — Ética y derechos en actividades espaciales](../B119-C18-etica-y-derechos-en-actividades-espaciales/CLASE.md) · [Siguiente: B119-C20 — Simulación de respuesta institucional a incidentes →](../B119-C20-simulacion-de-respuesta-institucional-a-incidentes/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 19 del bloque B119. Nivel N3. Cada Estado aplica los tratados mediante su propia ley, y las leyes difieren en lo que exigen. Esta clase aprende a comparar regímenes con una matriz de rasgos y una medida de similitud (Jaccard) usando **cinco regímenes inventados** de 12 rasgos, y verifica que la distancia cumple las propiedades de una métrica. No describe la ley de ningún país real. **Esta clase es educativa: no es asesoría legal, regulatoria ni financiera y no sustituye a un jurista, a una autoridad competente ni a un asesor.**

## 2. Por qué esta clase existe

Los tratados fijan principios y dejan la aplicación a los Estados (art. VI; art. II del Convenio de Registro); comparar leyes exige un método, que ninguna clase del programa enseña. El marco chileno se aborda en B121 con fuentes oficiales. La decisión central: **¿qué tan parecidos son dos regímenes, qué rasgos comparten y cuáles los distinguen?**

## 3. Lo que podrás hacer al terminar

1. Explicar por qué los tratados dejan a los Estados la forma de aplicarse (arts. consultados).
2. Construir una matriz de rasgos binarios de regímenes sintéticos.
3. Calcular la similitud de Jaccard y verificar simetría y desigualdad triangular.
4. Identificar el par más parecido, el más distinto y los rasgos únicos.
5. Separar lo consultado (texto normativo con versión y fecha) de lo sintético o ilustrativo.

La evidencia es la **matriz comparada de cinco regímenes sintéticos** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es una variable binaria?
2. ¿Qué es la intersección de dos conjuntos?
3. ¿Qué es la unión?
4. ¿Qué es una métrica?
5. ¿Qué es la legislación comparada?

<details>
<summary>Ver respuestas</summary>

1. Una que toma 0 o 1. 2. Los elementos comunes. 3. Los elementos que están en alguno. 4. Una distancia con simetría, positividad y desigualdad triangular. 5. El estudio de las diferencias y similitudes entre ordenamientos.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

La nota de la ONU (consultada el 2026-11-11) recoge que las actividades privadas requieren autorización y supervisión continua del Estado (art. VI), y la página de UNOOSA del Convenio de Registro dice que el contenido del registro nacional lo fija cada Estado (art. II): los tratados dejan espacio a la ley nacional. **No se consultó la legislación de ningún Estado.** El **ejemplo conductor** son cinco regímenes **inventados** (Alfa a Epsilon) con 12 rasgos (licencia previa, seguro, tope de responsabilidad, registro, plan de desechos, supervisión, evaluación ambiental, control de exportación, cooperación con reguladores, inspecciones, garantía financiera, reglas de datos).

## 6. Vocabulario

Un **rasgo** es una exigencia que un régimen impone o no. La **similitud de Jaccard** es `|A∩B|/|A∪B|`. La **distancia de Jaccard** es `1 − J`. Una **matriz de rasgos** tabula regímenes por rasgos. Un **rasgo único** solo está en un régimen.

## 7. Modelo mental

```mermaid
flowchart LR
    L["Tratado: principio"] --> N["Ley nacional"]
    N --> M["Matriz de rasgos"]
    M --> J["Jaccard"]
    J --> P["Par más parecido / distinto"]
    M --> U["Rasgos únicos y comunes"]
```

*Descripción textual:* el principio del tratado se concreta en leyes nacionales; estas se tabulan por rasgos y se comparan con Jaccard.

Analogía: comparar menús de restaurantes marcando qué platos ofrece cada uno: se ve en qué se parecen y qué los distingue. Límite: tener un rasgo no dice cómo se aplica; la ley real tiene matices que un 0/1 pierde.

## 8. La explicación, paso a paso

### 8.1 La matriz

Cinco regímenes y 12 rasgos. Delta exige casi todo; Epsilon casi nada (`2` rasgos); Alfa exige `9`.

### 8.2 Similitud

El par más parecido es `Alfa-Delta` (`J = 0.900`); el más distinto, `Delta-Epsilon` (`J = 0.091`). Alfa y Beta tienen `J = 0.636`.

### 8.3 Verificación

La similitud cumple `J(a,a) = 1`, la simetría y la desigualdad triangular de `1 − J` en todas las ternas.

### 8.4 Rasgos únicos

Hay `1` rasgo exigido por un solo régimen (la evaluación ambiental, solo en Beta); el único rasgo común a los cinco es el registro nacional, coherente con que el Convenio de Registro obliga a registrar (S1).

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `n` | rasgos | — | 12 |
| `J` | similitud de Jaccard | — | 0 a 1 |
| `d` | distancia `1 − J` | — | 0 a 1 |
| regímenes | inventados | — | 5 |

## 10. Convenciones y referencias

Rasgo exigido = 1; no exigido = 0. Regímenes inventados; ninguna ley real.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S3 | ONU, Biblioteca Audiovisual de Derecho Internacional, nota introductoria sobre el Tratado del Espacio Ultraterrestre, https://legal.un.org/avl/ha/tos/tos.html (WebFetch, consultada 2026-11-11; no discute los artículos V ni VII) | art. VI | autorización y supervisión de actividades privadas | Consultada |
| S1 | UNOOSA, «Convention on Registration of Objects Launched into Outer Space» (página oficial), https://www.unoosa.org/oosa/en/ourwork/spacelaw/treaties/registration-convention.html (WebFetch, consultada 2026-11-11) | art. II | el contenido del registro nacional lo fija cada Estado | Consultada |
| — | Legislación de cualquier Estado | — | no consultada | No consultado / ilustrativo |
| — | Regímenes y rasgos | — | inventados | No consultado / ilustrativo |

Límites: los regímenes son ficticios y no permiten concluir nada sobre ninguna legislación real. Texto normativo parafraseado de las páginas oficiales en la fecha indicada; el texto vinculante es el de la fuente oficial vigente.

## 12. Cómo ver la situación

| Magnitud | Valor |
|---|---|
| Par más parecido | Alfa-Delta (0.900) |
| Par más distinto | Delta-Epsilon (0.091) |
| Rasgos únicos | 1 (evaluación ambiental) |
| Rasgos de Epsilon | 2 |

Descripción larga: Alfa y Delta son casi iguales y Epsilon se separa de todos por exigir muy poco.

## 13. Ejemplo trabajado: Alfa frente a Beta

**Paso 1.** Alfa y Beta comparten 7 rasgos y la unión tiene 11. **Paso 2.** `J = 7/11 = 0.636`. **Paso 3.** Distancia `1 − J = 0,364`.

## 14. Distintas formas de describirlo

**Por rasgo:** presente o ausente. **Por par:** Jaccard. **Por régimen:** número de rasgos. **Por distancia:** métrica.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `J` entre dos regímenes con 6 rasgos comunes y 10 en la unión.

<details><summary>Solución comentada</summary>

`0,6`.
</details>

**Ejercicio 2 · con una pista.** Calcula la distancia `1 − J` del caso anterior. *Pista:* `1 − 0,6`.

<details><summary>Solución comentada</summary>

`0,4`.
</details>

**Ejercicio 3 · casi autónomo.** ¿Cuánto vale `J(a,a)`?

<details><summary>Solución comentada</summary>

1.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Interpreta `J = 0.091`.

<details><summary>Solución comentada</summary>

Los regímenes tienen muy pocos rasgos en común respecto de los que exigen entre ambos.
</details>

**Ejercicio 5 · autónomo.** ¿Cuántos rasgos exige Epsilon?

<details><summary>Solución comentada</summary>

`2`.
</details>

**Ejercicio 6 · autónomo.** Añade un rasgo exigido solo por Gamma. ¿Cambia el par más parecido?

<details><summary>Solución comentada</summary>

Probablemente no, pero baja `J` entre Gamma y los demás; compruébalo con el script.
</details>

**Ejercicio 7 · autónomo.** ¿Qué rasgo es único en el conjunto?

<details><summary>Solución comentada</summary>

La evaluación ambiental, exigida solo por Beta.
</details>

**Ejercicio 8 · autónomo.** ¿Por qué los regímenes son inventados?

<details><summary>Solución comentada</summary>

Para no atribuir exigencias a ningún país sin haber consultado su ley.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** ¿Qué pierde una comparación binaria?

<details><summary>Solución comentada</summary>

Los grados: un tope de responsabilidad alto o bajo cuenta igual.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Cómo comprobarías un rasgo en una ley real?

<details><summary>Solución comentada</summary>

Leyendo el texto oficial vigente y citando su versión y fecha.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Por qué comparar leyes ayuda a un operador internacional?

<details><summary>Solución comentada</summary>

Muestra las exigencias que debe cumplir en cada jurisdicción y las diferencias de coste regulatorio.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *matriz comparada de cinco regímenes sintéticos*: rasgos, Jaccard, par más parecido y distinto, rasgos únicos y aviso de que es educativa.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: matriz de regímenes y Jaccard

El script [laboratorio.py](laboratorio.py) calcula la matriz de similitud de cinco regímenes inventados (**comprueba** simetría, `J(a,a) = 1` y la desigualdad triangular en todas las ternas).

**Datos:** art. VI y art. II del Convenio de Registro consultados (2026-11-11); regímenes **inventados**. **Predice antes de ejecutar:** ¿cuál será el par más parecido? (Alfa y Delta.) **Ejecución del 2026-11-11 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Regimenes INVENTADOS (Alfa a Epsilon), 12 rasgos binarios; art. VI y art. II del Convenio de Registro consultados 2026-11-11; ninguna ley real consultada.
               Alfa     Beta    Gamma    Delta  Epsilon
Alfa          1.000    0.636    0.300    0.900    0.100
Beta          0.636    1.000    0.300    0.583    0.222
Gamma         0.300    0.300    1.000    0.400    0.200
Delta         0.900    0.583    0.400    1.000    0.091
Epsilon       0.100    0.222    0.200    0.091    1.000
Par mas parecido: Alfa-Delta (J = 0.900) ; par mas distinto: Delta-Epsilon (J = 0.091)
Rasgos exigidos por todos: ['registro_nacional']
Rasgos exigidos por un solo regimen: [('evaluacion_ambiental', 'Beta')]
Numero de rasgos por regimen: {'Alfa': 9, 'Beta': 9, 'Gamma': 4, 'Delta': 10, 'Epsilon': 2}
CLAVES {"jmax": "0.900", "par": "Alfa-Delta", "jmin": "0.091", "lej": "Delta-Epsilon", "nu": 1, "nA": 9, "nE": 2, "ab": "0.636"}
Pruebas superadas.
```

```bash
python programa/clases/B119/B119-C19-legislacion-comparada-y-casos-nacionales/laboratorio.py
```

**Límites:** rasgos binarios sin matices; regímenes ficticios; no describe ninguna ley.

## 18. Errores frecuentes y cómo corregirlos

**Atribuir un rasgo a un país real.** Se corrige con la sección 11.

**Confundir similitud con distancia.** Se corrige con el vocabulario.

**Creer que más rasgos es «mejor».** Se corrige con el ejercicio 9.

**Comparar leyes sin fecha de versión.** Se corrige con el ejercicio 10.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas en el ejemplo trabajado y cuál obtuviste? Si dudas, repasa la sección 13. Tras el laboratorio: ¿qué comprueba cada prueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **matriz comparada de cinco regímenes sintéticos** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Usa el vocabulario con precisión | Explica los límites del modelo |
| Cálculo | Sin unidades | Con errores | Resultados con unidades y tolerancia | Calcula casos nuevos |
| Verificación | Sin comprobar | Un caso | Contraste con una segunda vía | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con versión, fecha y estado | Declara lo sintético y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** citar la versión y la fecha del texto normativo consultado; rotular lo sintético y lo ilustrativo; no presentar un resultado como asesoría legal, regulatoria o financiera.

## 21. Ética, seguridad y límites

Clase educativa: **no es asesoría legal, regulatoria ni financiera**; no sustituye a un abogado, a la autoridad competente ni a un asesor, y ningún resultado debe usarse para decidir sobre una licencia, una reclamación, un contrato o una operación real. Los regímenes son ficticios; no se emite juicio sobre ningún ordenamiento real. Los modelos son simplificados y sus datos son sintéticos o ilustrativos; lo simulado nunca se presenta como observado. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

El par más parecido es `Alfa-Delta` (`J = 0.900`) y el único rasgo común a los cinco es el registro nacional. Queda una pregunta: ¿cómo responde una institución cuando ocurre un incidente?

**Glosario español–inglés.** legislación comparada · *comparative law*; rasgo · *feature*; similitud de Jaccard · *Jaccard similarity*; matriz · *matrix*.

**Continuidad.** [B119-C20](../B119-C20-simulacion-de-respuesta-institucional-a-incidentes/CLASE.md): la simulación de respuesta institucional a incidentes.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B119-C18 — Ética y derechos en actividades espaciales](../B119-C18-etica-y-derechos-en-actividades-espaciales/CLASE.md) · [📚 Bloque B119](../../../tronco-comun/B119-derecho-seguridad-y-geopolitica-espacial.md) · [Siguiente: B119-C20 — Simulación de respuesta institucional a incidentes →](../B119-C20-simulacion-de-respuesta-institucional-a-incidentes/CLASE.md)
<!-- /nav -->
