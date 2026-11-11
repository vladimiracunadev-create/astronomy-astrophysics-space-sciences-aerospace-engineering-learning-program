# B125-C03 — Gobierno corporativo de una empresa espacial

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B125](../../../tronco-comun/B125-creacion-y-operacion-de-empresas-espaciales.md) · [← Anterior: B125-C02 — Modelos de ingresos: suscripción y servicio](../B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md) · [Siguiente: B125-C04 — Alianzas y cooperación internacional empresarial →](../B125-C04-alianzas-y-cooperacion-internacional-empresarial/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 3 del bloque B125. Nivel N4. El gobierno corporativo es el sistema por el cual se dirige y controla una empresa: quién vota, con cuánto peso y quién decide en el consejo. Aquí calculas el poder de voto de una estructura con dos clases de acciones, la participación económica mínima para controlar y el índice de poder de Banzhaf de un consejo sintético. Usa los costos y ingresos de [B125-C02](../B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md) solo como contexto. **Esta clase es educativa: no es asesoría financiera, legal ni de inversión y no sustituye a un profesional.**

## 2. Por qué esta clase existe

Las decisiones de una empresa se estructuran en su gobierno y, en el espacio, el capital intensivo hace que quien controla la votación controle el rumbo de misiones de años; ninguna clase lo trata. La decisión central: **¿qué participación económica basta para controlar una empresa y cuánto pesa realmente cada miembro de un consejo?**

## 3. Lo que podrás hacer al terminar

1. Calcular el poder de voto de una clase de acciones con `k` votos por acción.
2. Deducir la participación mínima para un poder de voto dado: `b = v / (k(1 − v) + v)`.
3. Calcular el índice de poder de Banzhaf de un consejo con pesos y cuota.
4. Mostrar que el peso nominal y el poder real pueden diferir y que un peso dominante convierte a un miembro en decisor único.
5. Verificar las fórmulas por enumeración de acciones y de coaliciones.
6. Separar lo consultado (estructura de una empresa real) de lo sintético (acciones y consejo).

La evidencia es la **ficha de estructura de gobierno con su índice de poder** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es una acción con derecho a voto?
2. ¿Qué es una mayoría simple?
3. ¿Qué es una coalición ganadora?
4. ¿Qué es un miembro decisivo (pivote)?
5. ¿Qué es una enumeración exhaustiva?

<details>
<summary>Ver respuestas</summary>

1. Un título de propiedad que da derecho a votar en la junta, a veces con distinto número de votos por clase. 2. Más de la mitad de los votos o del peso. 3. Un grupo de miembros cuyos pesos suman al menos la cuota. 4. Uno sin cuyo voto una coalición ganadora deja de ganar. 5. Recorrer todos los casos posibles (aquí, los `2ⁿ` subconjuntos).
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

El Formulario 10-K de Planet Labs PBC (ejercicio cerrado el 2026-01-31, consultado el 2026-11-11 en la SEC) indica que opera como **sociedad de beneficio público de Delaware** (debe equilibrar el interés de los accionistas, el de los afectados por su conducta y el beneficio público fijado en su estatuto), que las acciones **Clase B tienen 20 votos** y las Clase A uno, y que los dos fundadores tienen todas las Clase B y cerca del **62 %** del poder de voto total. El texto leído no da el número de acciones ni la participación económica: **no se conocen**. Los Principios de Gobierno Corporativo G20/OCDE (2023) se conocen solo por un resumen de búsqueda (adoptados por la OCDE en junio de 2023 y respaldados por el G20 en septiembre de 2023); su texto **no** se leyó. El **ejemplo conductor** es sintético: con `k = 20`, basta el `4,76 %` de las acciones para el 50 % del voto.

## 6. Vocabulario

Una **clase de acciones** agrupa títulos con los mismos derechos. El **poder de voto** es la fracción de los votos totales que controla un grupo. El **consejo** es el órgano que dirige la empresa. La **cuota** es el peso mínimo para ganar una votación. El **índice de Banzhaf** es la fracción de veces que un miembro es decisivo. Una **sociedad de beneficio público** debe equilibrar el interés de sus accionistas con un beneficio público declarado.

## 7. Modelo mental: votos frente a propiedad

```mermaid
flowchart LR
    P["fraccion b de acciones B"] --> V["votos = k b"]
    R["resto 1 - b, 1 voto"] --> T["votos totales k b + (1-b)"]
    V --> T
    T --> F["poder = k b / (k b + 1 - b)"]
    F --> M["b minima para poder v"]
```

*Descripción textual:* la fracción de acciones con `k` votos se compara con el resto de las acciones; el cociente da el poder de voto y, despejando, la participación mínima para controlar.

Analogía: una votación en la que algunos asistentes levantan 20 manos y otros una. Límite: el modelo supone que todas las acciones B están en un mismo grupo y no incluye acuerdos de voto, cláusulas de extinción, mayorías cualificadas ni leyes locales.

## 8. La explicación, paso a paso

### 8.1 Poder de voto con dos clases

Si una fracción `b` de las acciones es Clase B con `k` votos y el resto (`1 − b`) tiene un voto: `poder = k b / (k b + 1 − b)`.

| `b` | poder de voto (`k = 20`) |
|---|---|
| 0,0100 | 0,1681 |
| 0,0476 | 0,4999 |
| 0,0750 | 0,6186 |
| 0,1000 | 0,6897 |
| 0,2500 | 0,8696 |

### 8.2 Participación mínima

Despejando: `b = v / (k(1 − v) + v)`. Para `v = 0,5` y `k = 20`: `b = 0,0476` (4,76 % de las acciones). Para `v = 0,62`: `b = 0,0754`; con un millón de acciones son `75 426` acciones B y el voto B es `0,620001` (enumeración). Es un cálculo **ilustrativo**: el 62 % del caso consultado no implica que los fundadores tengan solo el 7,5 % de las acciones, porque pueden tener también acciones A (no consultado).

| `k` | participación mínima para el 50 % del voto |
|---|---|
| 1 | 0,5000 |
| 2 | 0,3333 |
| 10 | 0,0909 |
| 20 | 0,0476 |
| 100 | 0,0099 |

### 8.3 Poder en un consejo

Consejo sintético con pesos `[3, 2, 1, 1, 1, 1, 1]` y cuota `6` de `10`. El índice de Banzhaf cuenta, por miembro, en cuántas coaliciones ganadoras es decisivo y normaliza a suma `1`.

| miembro | peso | Banzhaf | peso relativo |
|---|---|---|---|
| 1 | 3 | 0,3504 | 0,3000 |
| 2 | 2 | 0,1795 | 0,2000 |
| 3 a 7 | 1 | 0,0940 | 0,1000 |

El miembro 1 pesa 30 % pero tiene 35,0 % del poder; el 2, 20 % y 17,9 %. Con pesos `[4, 1, 1, 1]` y cuota `4`, el miembro de peso 4 tiene Banzhaf `1,0`: decide solo, aunque su peso nominal sea `4/7`.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `b` | fracción de acciones Clase B | — | 0,0476 |
| `k` | votos por acción B | votos | 20 (relación del caso consultado) |
| `v` | poder de voto | — | 0,5 |
| cuota | peso para ganar | peso | 6 de 10 |
| Banzhaf | índice de poder | — | suma 1 |

## 10. Convenciones y referencias

Fracciones entre 0 y 1; acciones y pesos sin unidad. La Clase A tiene siempre un voto. El consejo decide por mayoría simple de peso. Semilla no necesaria: el laboratorio es determinista.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | Planet Labs PBC, Formulario 10-K, ejercicio cerrado el 2026-01-31, SEC — https://www.sec.gov/Archives/edgar/data/1836833/000119312526119957/pl-20260131.htm (consultada 2026-11-11; extractos de los caracteres 100 000 a 300 000) | factores de riesgo | sociedad de beneficio público de Delaware; Clase B con 20 votos y Clase A con uno; los fundadores con todas las Clase B y cerca del 62 % del voto | Consultada |
| S2 | OCDE, *G20/OECD Principles of Corporate Governance 2023* — https://doi.org/10.1787/ed750b30-en | — | adopción en junio de 2023 y respaldo del G20 en septiembre de 2023 | Solo por resumen de búsqueda; texto **no consultado** (el servidor rechazó la página) |
| — | Poder de voto, participación mínima, índice de Banzhaf | — | todo el modelo; verificado por enumeración | No consultado en una fuente concreta |
| — | Número de acciones, consejo, pesos | — | todos los números | Sintético |

Límites: no se consultó el estatuto, la participación económica ni la composición del consejo de ninguna empresa; el texto de los principios de la OCDE no se leyó; el derecho societario varía por jurisdicción.

## 12. Cómo ver el poder

| Magnitud | Valor |
|---|---|
| participación mínima para 50 % con `k = 20` | 4,76 % |
| participación para 62 % con `k = 20` | 7,54 % |
| Banzhaf del miembro de peso 3 | 0,3504 |
| Banzhaf en `[4, 1, 1, 1]` con cuota 4 | 1,0 |

Descripción larga: con 20 votos por acción, menos del 5 % de las acciones da la mitad del voto; en un consejo ponderado el poder real se aparta del peso nominal, y un peso dominante lo concentra todo.

## 13. Ejemplo trabajado: la participación mínima con `k = 10`

**Paso 1 · Fórmula.** `b = v/(k(1 − v) + v)` con `v = 0,5` y `k = 10`.

**Paso 2 · Cálculo.** `b = 0,5/(10 × 0,5 + 0,5) = 0,5/5,5 = 0,0909`.

**Paso 3 · Comprobación.** `10 × 0,0909/(10 × 0,0909 + 0,9091) = 0,909/1,818 = 0,5`.

## 14. Distintas formas de describir el poder en una empresa

**Por votos:** poder de voto. **Por propiedad:** fracción de acciones. **Por consejo:** índice de Banzhaf. **Por estatuto:** beneficio público declarado. **Por riesgo:** concentración del control.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula el poder de voto con `b = 0,10` y `k = 20`. *Pasos:* votos B y votos totales.

<details><summary>Solución comentada</summary>

`20 × 0,1/(20 × 0,1 + 0,9) = 2/2,9 = 0,6897`.
</details>

**Ejercicio 2 · con una pista.** Calcula `b` mínima para `v = 0,5` con `k = 2`. *Pista:* `v/(k(1−v)+v)`.

<details><summary>Solución comentada</summary>

`0,5/(1 + 0,5) = 0,3333`.
</details>

**Ejercicio 3 · casi autónomo.** En el consejo `[3, 2, 1, 1, 1, 1, 1]` con cuota 6, ¿pesa lo mismo el miembro 3 que el 7 en poder?

<details><summary>Solución comentada</summary>

Sí: ambos tienen peso 1 y Banzhaf `0,0940`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** ¿Qué `b` da `v = 0,75` con `k = 20`?

<details><summary>Solución comentada</summary>

`0,75/(20 × 0,25 + 0,75) = 0,75/5,75 = 0,1304`.
</details>

**Ejercicio 5 · autónomo.** Con `k = 1`, ¿qué relación hay entre `b` y `v`?

<details><summary>Solución comentada</summary>

`v = b`: sin votos múltiples el voto coincide con la propiedad.
</details>

**Ejercicio 6 · autónomo.** Con pesos `[2, 1, 1]` y cuota 3, calcula Banzhaf.

<details><summary>Solución comentada</summary>

Coaliciones ganadoras: `{1,2}`, `{1,3}`, `{1,2,3}`; el miembro 1 es decisivo en 3, los 2 y 3 en 1 cada uno: `[0,6, 0,2, 0,2]`.
</details>

**Ejercicio 7 · autónomo.** Con 1 000 000 de acciones y `b = 0,0476`, ¿cuántas son B y qué poder dan?

<details><summary>Solución comentada</summary>

`47 600` B; `20 × 47 600 = 952 000` votos; total `952 000 + 952 400 = 1 904 400`; poder `0,49989`.
</details>

**Ejercicio 8 · autónomo.** ¿Por qué el laboratorio comprueba que la suma de los índices de Banzhaf vale 1?

<details><summary>Solución comentada</summary>

Porque están normalizados por el total de decisivos; si no sumara 1 habría un error de conteo.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Los fundadores de la empresa del caso tienen el 62 % del voto. ¿Qué no puedes concluir sobre su participación económica?

<details><summary>Solución comentada</summary>

Nada exacto: depende de cuántas acciones A tengan y del número total; el cálculo `7,54 %` supone que solo tienen B y es ilustrativo.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Qué tensión introduce una sociedad de beneficio público en las decisiones de un consejo?

<details><summary>Solución comentada</summary>

Debe equilibrar el interés de los accionistas, el de los afectados y el beneficio público del estatuto; las decisiones ya no se miden solo por retorno financiero (según el texto consultado; su aplicación legal no se analizó).
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** Una misión lunar exige diez años de inversión. ¿Qué ventaja y qué riesgo trae un control concentrado del voto?

<details><summary>Solución comentada</summary>

Ventaja: estabilidad de rumbo frente a presiones de corto plazo; riesgo: poca rendición de cuentas si el control no refleja la propiedad. Es un argumento, no una medición.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de estructura de gobierno con su índice de poder*: tabla de poder de voto, participación mínima, índice de Banzhaf del consejo y lista de lo consultado, lo sintético y lo no consultado, con el aviso de que es educativa.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.3 y la salida del laboratorio.
</details>

## 17. Laboratorio: votos por acción y poder en el consejo

El script [gobierno.py](gobierno.py) calcula el poder de voto para varias fracciones, la participación mínima, la enumeración con un millón de acciones y el índice de Banzhaf por enumeración de subconjuntos (**comprueba** la fórmula frente a la enumeración a 1e-5, la suma de índices a 1e-12 y el caso `[4, 1, 1, 1]`).

**Datos:** solo la relación 20:1 y el 62 % vienen de un informe consultado, y como contraste; todo lo demás es **sintético**. **Predice antes de ejecutar:** ¿qué fracción de acciones B da el 50 % del voto con `k = 20`? (menos del 5 %.) **Ejecución del 2026-11-11 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Estructura SINTETICA; solo la relacion 20:1 y el 62 % de voto vienen de un informe consultado (como contraste).
Fraccion b de acciones Clase B   poder de voto de la Clase B (k = 20)
                        0.0100   0.1681
                        0.0476   0.4999
                        0.0750   0.6186
                        0.1000   0.6897
                        0.2500   0.8696
Participacion minima para 50 % del voto con k = 20: 0.0476 (4.76 % de las acciones)
Participacion que daria 62 % del voto si TODAS sus acciones fueran B con k = 20: 0.0754 (7.54 % de las acciones; ilustrativo)
Enumeracion con 1000000 acciones: B = 75426, voto B = 0.620001
k (votos por B)   participacion minima para 50 % del voto
              1   0.5000
              2   0.3333
             10   0.0909
             20   0.0476
            100   0.0099
Consejo sintetico pesos [3, 2, 1, 1, 1, 1, 1], cuota 6 de 10
miembro  peso  indice de Banzhaf  peso relativo
      1     3             0.3504         0.3000
      2     2             0.1795         0.2000
      3     1             0.0940         0.1000
      4     1             0.0940         0.1000
      5     1             0.0940         0.1000
      6     1             0.0940         0.1000
      7     1             0.0940         0.1000
Consejo [4, 1, 1, 1] con cuota 4: Banzhaf = [1.0, 0.0, 0.0, 0.0] (el miembro de peso 4 decide solo)
Pruebas superadas.
```

```bash
python programa/clases/B125/B125-C03-gobierno-corporativo-de-una-empresa-espacial/gobierno.py
```

**Límites:** una sola votación por mayoría simple; sin acuerdos de voto, cláusulas de extinción ni mayorías cualificadas; no analiza ningún estatuto real ni el derecho societario.

## 18. Errores frecuentes y cómo corregirlos

**Confundir poder de voto con participación económica.** Se corrige con 8.2 y el ejercicio 9.

**Tomar el peso nominal como poder.** Se corrige con 8.3.

**Concluir la propiedad de los fundadores a partir del 62 %.** Se corrige con el ejercicio 9.

**Tomar la estructura de una empresa como modelo a imitar.** Se corrige con la sección 21.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué poder esperabas con `b = 0,1` y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de estructura de gobierno con su índice de poder** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Calcula poder de voto y Banzhaf | Explica la diferencia entre peso, poder y propiedad |
| Cálculo | Sin unidades | Con errores | Tablas completas con unidades | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con una segunda vía | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo sintético y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular todos los datos de empresas como sintéticos o citados con su fuente; no presentar un resultado como asesoría financiera, legal o de inversión; citar solo lo consultado. No presentar la estructura de una empresa real como recomendación.

## 21. Ética, seguridad y límites

Clase educativa: **no es asesoría financiera, legal, tributaria ni de inversión** y no sustituye a un abogado, un contador, un especialista en cumplimiento ni un asesor financiero; ningún resultado debe usarse para decidir una operación, una constitución societaria, una exportación o una inversión reales. El gobierno de una sociedad real depende de su estatuto y de la ley aplicable; consulta a un abogado societario. Los modelos son simplificados y sus datos son sintéticos o ilustrativos. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Con 20 votos por acción, el `4,76 %` de las acciones da la mitad del voto; en un consejo `[3, 2, 1, 1, 1, 1, 1]` el miembro de peso 3 tiene `35,0 %` del poder. Queda una pregunta: ¿cómo se reparte el valor cuando varias empresas de países distintos deciden cooperar?

**Glosario español–inglés.** gobierno corporativo · *corporate governance*; poder de voto · *voting power*; índice de Banzhaf · *Banzhaf power index*; sociedad de beneficio público · *public benefit corporation*; consejo · *board of directors*.

**Continuidad.** [B125-C04](../B125-C04-alianzas-y-cooperacion-internacional-empresarial/CLASE.md) trata las alianzas y la cooperación internacional.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B125-C02 — Modelos de ingresos: suscripción y servicio](../B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md) · [📚 Bloque B125](../../../tronco-comun/B125-creacion-y-operacion-de-empresas-espaciales.md) · [Siguiente: B125-C04 — Alianzas y cooperación internacional empresarial →](../B125-C04-alianzas-y-cooperacion-internacional-empresarial/CLASE.md)
<!-- /nav -->
