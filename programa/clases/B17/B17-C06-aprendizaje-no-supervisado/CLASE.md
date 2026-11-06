# B17-C06 — Aprendizaje no supervisado

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B17](../../../tronco-comun/B17-aprendizaje-automatico-cientifico.md) · [← Anterior: B17-C05 — Detección de anomalías](../B17-C05-deteccion-de-anomalias/CLASE.md) · [Siguiente: B17-C07 — Validación fuera de distribución →](../B17-C07-validacion-fuera-de-distribucion/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Sexta clase del bloque B17. Hasta ahora los datos traían etiquetas (C02) o un modelo de lo normal (C05). Aquí **no hay respuesta conocida**: buscas estructura. Aprendes a reducir la dimensión con componentes principales y a agrupar con k-medias. Nivel N2. Usas SVD y autovalores (B10-C08 y B10-C11), covarianza (B12-C18) y distancias. No verás agrupamiento jerárquico ni modelos de mezclas.

## 2. Por qué esta clase existe

Un catálogo trae miles de objetos medidos en varias bandas y nadie los ha clasificado. ¿Hay poblaciones distintas? ¿Cuántas? Un algoritmo puede proponer grupos, pero **siempre devuelve grupos**, haya o no estructura real. Saber qué supone, cómo se evalúa sin etiquetas y qué no demuestra es la parte científica.

La decisión central: **¿cómo propongo grupos en datos sin etiqueta, cuánto confío en ellos y qué tengo que verificar antes de llamarlos «poblaciones»?**

## 3. Lo que podrás hacer al terminar

1. Calcular componentes principales mediante SVD y verificar que sus varianzas son autovalores de la covarianza.
2. Decidir cuántos componentes conservar según la varianza explicada.
3. Ejecutar k-medias (algoritmo de Lloyd) a mano y comparar con una biblioteca.
4. Evaluar un agrupamiento sin etiquetas con la inercia y el coeficiente de silueta.
5. Explicar por qué se estandarizan las variables antes y por qué k-medias supone grupos esféricos.
6. Distinguir un grupo hallado de una clase física confirmada.

La evidencia es el **informe de agrupamiento** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué autovalores tiene `[[1, 0,8], [0,8, 1]]`?
2. Si una variable está en km y otra en m, ¿cuál domina una distancia euclídea sin escalar?
3. ¿Cuál es el centro (media) de {1, 2}?
4. ¿Qué es la traza de una matriz?
5. ¿Qué relación hay entre los valores singulares `s` de una matriz centrada con `n` filas y las varianzas?

<details>
<summary>Ver respuestas</summary>

1. 1,8 y 0,2. 2. La de metros (números 1000 veces mayores). 3. 1,5. 4. La suma de la diagonal (y de los autovalores). 5. Varianza = `s²/(n − 1)`.
</details>

Con cuatro o cinco aciertos, sigue; con tres o menos, repasa B10-C08 y B10-C11.

## 5. Un caso real: lo que dice la documentación sobre k-medias

La documentación de scikit-learn describe k-medias como la partición de `N` muestras en `K` grupos que minimiza la **inercia** (suma de cuadrados dentro de cada grupo), con `K` fijado de antemano; supone grupos convexos e isótropos, puede quedar en un mínimo local según la inicialización, y en dimensión alta se recomienda reducir antes con componentes principales (S1). Para evaluar sin etiquetas propone el coeficiente de silueta, `s = (b − a)/max(a, b)`, donde `a` es la distancia media a los puntos del mismo grupo y `b` la distancia media al grupo más cercano (S1). También describe DBSCAN, que busca regiones densas sin exigir forma convexa (S1). Son las limitaciones y herramientas que usarás aquí.

## 6. Vocabulario

El **aprendizaje no supervisado** busca estructura en datos sin etiquetas. Un **componente principal** es una dirección del espacio de variables de máxima varianza; los componentes son ortogonales. La **varianza explicada** de un componente es la fracción de la varianza total que concentra. El **agrupamiento** (*clustering*) asigna cada objeto a un grupo. **K-medias** repite dos pasos (algoritmo de Lloyd): asignar cada punto al centro más cercano y recalcular cada centro como la media de sus puntos. La **inercia** es `Σ ‖xᵢ − centro(i)‖²`. El **coeficiente de silueta** de un punto, `s = (b − a)/max(a, b)`, vale cerca de 1 si el punto está bien dentro de su grupo, cerca de 0 si está entre dos y es negativo si probablemente está mal asignado (S1). La **pureza** compara los grupos con clases conocidas (solo existe con datos sintéticos o ya etiquetados).

## 7. Modelo mental: de muchas variables a pocas, y de puntos a grupos

```mermaid
flowchart LR
    A["Datos sin etiqueta<br/>n objetos, p variables"] --> B["Estandarizar<br/>cada variable"]
    B --> C["PCA por SVD<br/>conservar q componentes"]
    C --> D["k-medias<br/>(probar varios k)"]
    D --> E["Silueta, inercia,<br/>estabilidad"]
    E --> F["Interpretar con física<br/>y verificar con datos nuevos"]
```

*Descripción textual:* los datos se estandarizan, se proyectan a pocos componentes con SVD, se agrupan con k-medias probando varios valores de `k`, se evalúan con silueta e inercia, y los grupos se interpretan con física y se verifican con datos nuevos.

Una analogía: ordenar una colección de piedras sin saber de geología, por tamaño, color y brillo. Tus montones son una propuesta. **Límite:** el criterio con que ordenaste (qué variables, qué escala) determina los montones; otra persona con otras variables obtiene otros.

## 8. La explicación, paso a paso

### 8.1 Estandarizar

Cada variable se lleva a media 0 y desviación 1 (C01). Sin eso, una variable con números grandes domina las distancias y los componentes. Es el mismo problema de unidades de C01, ahora con un algoritmo que no tiene etiquetas que corrijan el error.

### 8.2 Componentes principales por SVD

Con la matriz centrada `X` (n×p), la SVD `X = U S Vᵀ` da en las filas de `Vᵀ` las direcciones principales y en `s` los valores singulares; la varianza del componente `j` es `sⱼ²/(n − 1)` y coincide con el `j`-ésimo autovalor de la covarianza (B10-C11). La suma de varianzas es la traza de la covarianza: con 4 variables estandarizadas, igual a 4 (en rigor `4n/(n−1)` si se estandariza con `n` en lugar de `n−1`). Para `[[1, 0,8], [0,8, 1]]`, los autovalores son 1,8 y 0,2, y el primer componente explica `1,8/2 = 90 %`. Se conservan los componentes que acumulan una fracción útil (aquí, dos explican el 91,8 %).

### 8.3 K-medias, paso a paso

Con puntos unidimensionales {1, 2, 9, 10} y centros iniciales 0 y 5: 1 y 2 están más cerca de 0 (distancias 1 y 2 contra 4 y 3); 9 y 10 más cerca de 5. Nuevos centros: 1,5 y 9,5. Inercia: `0,25 + 0,25 + 0,25 + 0,25 = 1,0`. Un segundo paso no cambia nada: convergió. El algoritmo converge siempre, pero a un mínimo que depende del inicio (S1): se repite con varios inicios y se conserva la menor inercia.

### 8.4 ¿Cuántos grupos?

La inercia baja siempre al aumentar `k` (con `k = n` vale 0), así que **no sirve sola** para elegir. La silueta media sí penaliza grupos partidos de más. Si un punto tiene `a = 1` y `b = 8`, `s = (8 − 1)/8 = 0,875`: muy bien asignado. En el laboratorio, la silueta fue 0,568 con `k = 2`, **0,694 con `k = 3`**, 0,581 con `k = 4` y 0,403 con `k = 6`: el máximo está en 3, que coincide con las tres poblaciones fabricadas.

### 8.5 Lo que k-medias no ve

Supone grupos convexos e isótropos (S1). Dos anillos concéntricos no se separan con centros: el centro de cada anillo cae en el mismo punto. Para formas arbitrarias se usan métodos basados en densidad como DBSCAN, que tiene un parámetro `eps` crítico: demasiado pequeño, casi todo es ruido; demasiado grande, los grupos se funden (S1).

### 8.6 Un grupo no es una clase

Que el algoritmo devuelva `k` grupos no prueba que existan `k` poblaciones físicas. Los grupos son una propuesta, y para llamarlos poblaciones hay que mostrar que se reproducen con datos nuevos, con otras variables o con otro método, y que tienen una interpretación física.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Nota |
|---|---|---|---|
| `X` | matriz de datos centrada | variables estandarizadas | n × p |
| `s` | valores singulares | adimensional | de la SVD |
| `sⱼ²/(n−1)` | varianza del componente `j` | adimensional | = autovalor |
| `K` | número de grupos | adimensional | elegido |
| inercia | `Σ ‖xᵢ − centro‖²` | adimensional | baja con `K` |
| silueta | `(b − a)/max(a, b)` | adimensional | −1 a 1 |

## 10. Convenciones y referencias

Datos **sintéticos**: 900 objetos en 4 variables ficticias («colores» estandarizados), tres poblaciones de 300 con centros fijos. Se reduce a 2 componentes antes de agrupar. Con 10 inicios de k-medias y semilla fija.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | scikit-learn, «Clustering» (k-medias, silueta, DBSCAN) | https://scikit-learn.org/stable/modules/clustering.html | Inercia; supuestos de k-medias; mínimo local e inicialización; PCA previo en alta dimensión; fórmula de la silueta; DBSCAN y `eps` | Página consultada el 2026-11-05; se leyeron las primeras 100 000 de 114 271 caracteres (mutable) |

Límites: la relación SVD–varianza es un resultado de álgebra lineal (B10-C11) comprobado en el laboratorio; no se consultó la documentación de PCA de scikit-learn ni literatura astronómica sobre clasificación no supervisada.

## 12. Cómo ver los resultados

| `k` | Silueta media |
|---|---|
| 2 | 0,568 |
| 3 | 0,694 |
| 4 | 0,581 |
| 6 | 0,403 |

Componentes principales (varianzas): 2,506; 1,169; 0,249; 0,081 (el 91,8 % en los dos primeros). Grafica los puntos en el plano de los dos primeros componentes con símbolos distintos por grupo, no solo colores; describe con texto tres nubes bien separadas.

## 13. Ejemplo trabajado: ¿hay tres poblaciones?

**Caso.** 900 objetos con 4 variables ficticias, sin etiqueta. Se quiere saber cuántas poblaciones hay.

**Paso 1 · estandarizar.** Cada columna a media 0 y desviación 1.

**Paso 2 · PCA.** Varianzas 2,506; 1,169; 0,249; 0,081. Los dos primeros explican `3,675/4,004 = 91,8 %`: se conservan dos.

**Paso 3 · k-medias.** Para `k = 2, 3, 4, 6`, siluetas 0,568; 0,694; 0,581; 0,403: se elige 3.

**Paso 4 · verificar.** La inercia de la implementación de scikit-learn (409,52) coincidió con la del algoritmo de Lloyd escrito a mano, tanto partiendo de sus centros como de centros al azar.

**Paso 5 · incertidumbre.** Como los datos son sintéticos, se puede medir la pureza (0,997: 3 de 900 mal asignados). Con datos reales esa verificación no existe; se necesitaría reproducir los grupos con otro método y con datos nuevos, y una interpretación física.

## 14. Comparación de métodos

**K-medias**: rápido, simple, necesita `K` y grupos esféricos. **DBSCAN**: formas arbitrarias y marca ruido, sensible a `eps` (S1). **PCA**: reduce dimensión y ayuda a ver, pero mezcla variables y los componentes pueden no tener significado físico directo. La inercia compara solo dentro del mismo `K`; la silueta compara entre `K` distintos.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Para `Σ = [[1, 0,8], [0,8, 1]]`, ¿qué fracción de la varianza explica el primer componente? *Pasos:* autovalores 1,8 y 0,2 (sección 8.2).

<details><summary>Solución comentada</summary>

`1,8/(1,8 + 0,2) = 0,9`. Con una correlación alta, una sola dirección casi lo resume todo.
</details>

**Ejercicio 2 · con una pista.** Aplica un paso de k-medias a {1, 2, 9, 10} con centros 0 y 5 y calcula la inercia. *Pista:* sección 8.3.

<details><summary>Solución comentada</summary>

Grupos {1, 2} y {9, 10}; centros 1,5 y 9,5; inercia 1,0. Un paso más no cambia: convergió.
</details>

**Ejercicio 3 · casi autónomo.** Un punto tiene `a = 1` y `b = 8`. Calcula su silueta y otro con `a = 4` y `b = 5`.

<details><summary>Solución comentada</summary>

`(8 − 1)/8 = 0,875` y `(5 − 4)/5 = 0,2`. El segundo está cerca de la frontera entre grupos.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Con varianzas 2,5058; 1,1692; 0,2485; 0,0809, calcula la fracción explicada por cada componente.

<details><summary>Solución comentada</summary>

Suma 4,0044: 62,6 %; 29,2 %; 6,2 %; 2,0 %. Acumulado de dos: 91,8 %.
</details>

**Ejercicio 5.** Una variable está en parsecs (0 a 10) y otra en kilómetros (0 a 10⁹). ¿Qué pasa con PCA sin estandarizar?

<details><summary>Solución comentada</summary>

La variable en km tiene una varianza astronómicamente mayor; el primer componente es casi solo esa variable. La estandarización (C01) corrige la dependencia de unidades.
</details>

**Ejercicio 6.** La inercia con `k = 2, 3, 4` baja de 1900 a 410 a 330 (valores ilustrativos del enunciado). ¿Sirve para elegir `K`? ¿Qué usarías?

<details><summary>Solución comentada</summary>

Baja siempre con `K`; el codo entre 2 y 3 sugiere 3, pero es subjetivo. Se complementa con la silueta media (sección 8.4) y con la estabilidad ante datos nuevos.
</details>

**Ejercicio 7.** La pureza fue 0,997 con 900 objetos. ¿Cuántos quedaron mal asignados?

<details><summary>Solución comentada</summary>

`0,003 × 900 = 2,7 ≈ 3`. Esta medida requiere etiquetas; con datos reales no existe.
</details>

**Ejercicio 8.** Tres ejecuciones con centros iniciales distintos dieron inercias 409,52; 409,52 y 457,3 (valores ilustrativos del enunciado). ¿Qué haces?

<details><summary>Solución comentada</summary>

Conservas la de menor inercia (409,52) y notas que la tercera quedó en un mínimo local (sección 8.3). Por eso se usa `n_init > 1`.
</details>

**Ejercicio 9 · transferencia.** Dos anillos concéntricos de puntos. ¿Por qué k-medias con `k = 2` falla y qué método probarías?

<details><summary>Solución comentada</summary>

Ambos anillos tienen el mismo centro, y k-medias separa por distancia a centros, cortando los anillos por la mitad. DBSCAN (regiones densas) puede separarlos si `eps` está bien elegido (sección 8.5).
</details>

**Ejercicio 10 · transferencia.** Cada objeto es un espectro de 2000 valores. ¿Qué haces antes de agrupar y por qué?

<details><summary>Solución comentada</summary>

Reducir con componentes principales (por ejemplo, a 10) y agrupar allí: en alta dimensión las distancias euclídeas pierden contraste (S1). Se verifica que los componentes conservados expliquen una fracción razonable de la varianza.
</details>

**Ejercicio 11 · transferencia.** Un colega llama «población de enanas rojas» a un grupo hallado. ¿Qué verificas?

<details><summary>Solución comentada</summary>

Que el grupo se repite con otras variables, otro método y datos nuevos; que sus propiedades físicas (masa, temperatura) son coherentes con enanas rojas; y que no es un efecto de selección del instrumento. Un grupo es una hipótesis (sección 8.6).
</details>

**Ejercicio 12 · integrador.** Redacta el **informe de agrupamiento** del conjunto sintético: estandarización, varianza explicada y componentes conservados, `k` probados con inercia y silueta, verificación de la implementación contra una biblioteca, pureza (declarando que existe solo por ser sintético) y tres límites.

<details><summary>Solución modelo</summary>

Debe incluir la tabla de siluetas, la comparación de inercias (409,52), la nota sobre la pureza, y los límites: supuesto de grupos esféricos, dependencia de variables y escala, y que un grupo no es una clase. Acepta cualquier informe coherente.
</details>

## 17. Laboratorio: SVD y k-medias contra una referencia

El script [agrupamiento.py](agrupamiento.py) verifica que las varianzas de la SVD coinciden con los autovalores de la covarianza, que la suma coincide con la traza, escribe el algoritmo de Lloyd a mano y lo compara con scikit-learn, y calcula siluetas para varios `k`.

**Datos:** sintéticos. **Predice antes de ejecutar:** ¿qué `k` tendrá la mayor silueta? **Ejecución del 2026-11-05 (Python 3.12.9, NumPy 2.4.4, scikit-learn 1.8.0):**

```text
Varianzas de los componentes (SVD): [2.5058 1.1692 0.2485 0.0809]
Fracción de varianza explicada por los dos primeros: 0.918
Inercia scikit-learn 409.52; Lloyd a mano (desde sus centros) 409.52; (desde centros al azar) 409.52
Silueta con k = 3: 0.694
  silueta con k = 2: 0.568
  silueta con k = 4: 0.581
  silueta con k = 6: 0.403
Pureza frente a las poblaciones verdaderas: 0.997
Pruebas superadas.
```

```bash
python programa/clases/B17/B17-C06-aprendizaje-no-supervisado/agrupamiento.py
```

**Límites:** grupos gaussianos y esféricos, bien separados; la pureza solo existe porque los datos son sintéticos. No muestra el comportamiento con grupos solapados ni de forma irregular.

## 18. Errores frecuentes y cómo corregirlos

**No estandarizar.** Ejercicio 5.

**Elegir `K` solo por la inercia.** Ejercicio 6.

**Fiarse de una sola inicialización.** Ejercicio 8.

**Usar k-medias con formas no convexas.** Ejercicio 9.

**Llamar población física a un grupo.** Ejercicio 11.

## 19. Cómo sabrás que vas bien

Tras 8.2: ¿calculas la varianza explicada de un componente? Si no, ejercicios 1 y 4. Tras 8.3: ¿haces un paso de Lloyd a mano? Si no, ejercicio 2. Tras el laboratorio: ¿por qué coinciden las inercias de dos inicios distintos? Al final: ¿qué verificación mostrarías para llamar «población» a un grupo?

## 20. Qué entregas y cómo se evalúa

El producto es tu **informe de agrupamiento** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Preparación | Sin estandarizar | Estandariza | Estandariza y reduce con PCA | Justifica el número de componentes |
| Elección de `K` | Arbitraria | Por inercia | Por silueta | Verifica estabilidad con datos nuevos |
| Verificación | Ninguna | Compara con biblioteca | Compara inercia y SVD vs autovalores | Prueba con varios inicios |
| Interpretación | Llama «población» | Describe grupos | Distingue grupo de clase | Propone prueba física |

**Condiciones críticas:** rotular los datos como sintéticos; no presentar un grupo como población física sin verificación.

## 21. Ética, seguridad y límites

Los grupos pueden reflejar sesgos de selección del instrumento o del catálogo, y una etiqueta publicada («población») se difunde como hecho. Declara variables, escala y supuestos. Accesibilidad: símbolos y texto, no solo color. Material educativo.

## 22. Para cerrar y seguir

La SVD da componentes cuya varianza son autovalores; k-medias propone grupos minimizando la inercia, y la silueta sirve para elegir `K` sin etiquetas. Un grupo es una hipótesis que hay que verificar. Queda abierta una pregunta: ¿cómo se comporta un agrupamiento cuando los datos nuevos vienen de otro instrumento?

**Glosario español–inglés.** aprendizaje no supervisado · *unsupervised learning*; componente principal · *principal component*; agrupamiento · *clustering*; k-medias · *k-means*; inercia · *inertia*; coeficiente de silueta · *silhouette coefficient*; pureza · *purity*.

**Continuidad.** B17-C07 estudia qué pasa cuando los datos salen de la distribución de entrenamiento.

**Referencias:** ver sección 11. S1 es documentación mutable.

<!-- nav:bottom -->
---

[← Anterior: B17-C05 — Detección de anomalías](../B17-C05-deteccion-de-anomalias/CLASE.md) · [📚 Bloque B17](../../../tronco-comun/B17-aprendizaje-automatico-cientifico.md) · [Siguiente: B17-C07 — Validación fuera de distribución →](../B17-C07-validacion-fuera-de-distribucion/CLASE.md)
<!-- /nav -->
