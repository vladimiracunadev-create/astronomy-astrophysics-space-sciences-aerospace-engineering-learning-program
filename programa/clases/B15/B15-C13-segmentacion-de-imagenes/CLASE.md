# B15-C13 — Segmentación de imágenes

<!-- nav:top -->
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Decimotercera clase del bloque B15. En [C12](../B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md) buscaste fuentes puntuales; muchos objetos de interés son *extensos*: manchas solares, nubes, cráteres, galaxias, regiones calientes de un mapa térmico. Segmentar es separar la imagen en regiones y decidir qué píxeles pertenecen a cada objeto. Aprenderás la umbralización automática (método de Otsu), el etiquetado de regiones conectadas, las métricas para comparar una segmentación con una referencia (IoU y Dice) y un error típico: aplicar un umbral global a una imagen con fondo que varía. Nivel N3. No verás clasificación supervisada de imágenes (B15-C22, programada).

## 2. Por qué esta clase existe

Medir el área de las manchas solares, el porcentaje de nubes de una escena o el tamaño de un cráter exige delimitar el objeto. La delimitación no es neutra: un umbral distinto cambia el área. Y un umbral aplicado a un fondo que no es uniforme puede marcar como «objeto» parte del propio fondo. Una segmentación sin métrica y sin referencia es una opinión; con métrica, es un resultado comprobable.

La decisión central: **¿cómo delimito el objeto, cómo cuento sus partes y cómo mido si lo hice bien?**

## 3. Lo que podrás hacer al terminar

1. Calcular un umbral de Otsu a partir de un histograma y reconocer cuándo falla.
2. Etiquetar regiones conectadas con conectividad 4 y 8 y entender la diferencia.
3. Calcular IoU y Dice entre una máscara y la referencia, y saber por qué la exactitud por píxel engaña.
4. Aplanar un fondo variable antes de umbralizar.
5. Medir el área de un objeto como fracción de la escena y reportar su incertidumbre.
6. Verificar un segmentador contra casos de respuesta conocida.

La evidencia es la **máscara segmentada con métricas** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

Necesitas el histograma ([C10](../B15-C10-histogramas-y-normalizacion/CLASE.md)), el ruido ([C09](../B15-C09-procesamiento-de-imagenes-digitales/CLASE.md)) y conjuntos. Cinco preguntas:

1. ¿Qué cuenta un histograma?
2. Si dos conjuntos de 100 píxeles se solapan en 60, ¿cuántos píxeles hay en su unión?
3. ¿Qué fracción de un disco de radio 70 ocupa un círculo de radio 6? (`(6/70)²`.)
4. ¿Qué es la mediana?
5. ¿Qué hace un filtro de media 3 × 3?

<details>
<summary>Ver respuestas</summary>

1. Cuántos píxeles caen en cada intervalo de valores. 2. `100 + 100 − 60 = 140`. 3. `0,0073`, es decir, 0,73 %. 4. El valor central de los datos ordenados. 5. Sustituye cada píxel por el promedio de su vecindad de 9, reduciendo el ruido (C07, C08).
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa C09 y C10.

## 5. Un caso real: manchas en un disco solar

Un telescopio solar toma imágenes del disco; las manchas son regiones más oscuras que la fotosfera. Medir su área sigue el mismo problema que cualquier segmentación. Para estudiarlo con verdad conocida usamos un disco **sintético** de 160 × 160 píxeles (radio 70) con oscurecimiento hacia el borde, `I = 1000 (0,4 + 0,6 μ)` con `μ = √(1 − (r/R)²)`, tres manchas con 0,35 de la intensidad local y ruido de 20 unidades. No son datos solares reales ni el contraste de manchas reales: los valores son ficticios. Es el **ejemplo conductor**.

## 6. Vocabulario

La **segmentación** asigna a cada píxel una etiqueta (objeto o fondo, o la región a la que pertenece). La **umbralización** clasifica con una regla `I < T`. El **método de Otsu** elige `T` maximizando la **varianza entre clases** `σ_b² = ω₀ ω₁ (μ₀ − μ₁)²`, donde `ω₀` y `ω₁` son las fracciones de píxeles de cada clase y `μ₀`, `μ₁` sus medias (no se consultó el artículo original: aquí se define y verifica por su propiedad). Una **región conectada** es un conjunto de píxeles de objeto unidos por vecindad; la **conectividad 4** une píxeles que comparten un lado, la **8** también los que comparten una esquina (S1 describe cómo `scipy.ndimage.label` usa por defecto la cruz de 4 vecinos y cómo pedir 8). La **máscara** es la imagen binaria resultante. La **IoU** (intersección sobre unión) es `|A ∩ B|/|A ∪ B|`; el **coeficiente de Dice** es `2|A ∩ B|/(|A| + |B|)`. El **aplanado** (*flat-fielding*, aquí del fondo) divide la imagen por un perfil de fondo. Un **falso positivo** es un píxel marcado que no es objeto.

## 7. Modelo mental: recortar con tijeras un mapa con relieve

Recortar un lago en un mapa es sencillo si todos los azules son iguales; pero si el mapa tiene un degradado, la tijera que sigue un nivel de azul recorta también parte del degradado. La solución es quitar el degradado primero. Analogía: tijeras sobre un mapa degradado. Su límite: en un mapa conoces el degradado de antemano; en una imagen científica hay que estimarlo sin contaminarlo con el propio objeto (por eso se usa la mediana).

```mermaid
flowchart LR
    I["Imagen"] --> P["Perfil de fondo<br/>(mediana por anillos)"]
    P --> R["Razón I / perfil"]
    R --> S["Suavizado 3×3"]
    S --> O["Umbral de Otsu"]
    O --> L["Etiquetado de<br/>regiones conectadas"]
    L --> F["Filtro de tamaño<br/>(≥ 10 px)"]
    F --> M["Máscara + métricas<br/>IoU / Dice / área"]
```

*Descripción textual:* se estima el perfil del fondo con la mediana por anillos, se divide la imagen por él, se suaviza, se calcula el umbral de Otsu, se etiquetan las regiones conectadas, se eliminan las muy pequeñas y se evalúa la máscara con IoU, Dice y área.

## 8. La explicación, paso a paso

### 8.1 Otsu: elegir el umbral por la separación de clases

Para cada umbral candidato `T`, los píxeles se dividen en dos clases y se calcula `σ_b²`. Si la separación es grande (las dos clases tienen medias muy distintas y pesos comparables), `σ_b²` es alta. Otsu toma el `T` que la maximiza. En una mezcla 50/50 de dos gaussianas `N(0,1)` y `N(4,1)`, por simetría el umbral óptimo es 2; el laboratorio da `1,995`.

A mano, con `[1; 1; 2; 2; 8; 9; 9; 10]`: cortando entre 2 y 8, `ω₀ = ω₁ = 0,5`, `μ₀ = 1,5`, `μ₁ = 9`, `σ_b² = 0,25 · 7,5² = 14,06`. Cortando entre 1 y 2, `ω₀ = 0,25`, `μ₀ = 1`, `ω₁ = 0,75`, `μ₁ = 6,667`: `σ_b² = 0,1875 · 5,667² = 6,02`. Gana el corte entre 2 y 8.

### 8.2 Cuándo falla un umbral global

Otsu supone dos grupos de valores. Con oscurecimiento al borde, la fotosfera no es un grupo: va de 1000 en el centro a 400 en el limbo. En el laboratorio, Otsu sobre el disco da un umbral de 759 y marca **5659 píxeles** como «mancha» (la verdad son 179): casi todos son fotosfera cerca del borde. IoU `0,032`. La fotosfera cae bajo 759 cuando `0,4 + 0,6μ < 0,759`, es decir `μ < 0,598` y `r > 56,1` píxeles: el 36 % del disco.

### 8.3 Aplanar el fondo

Para quitar el oscurecimiento, se toma la **mediana por anillos** de radio entero (robusta frente a las manchas, que ocupan pocos píxeles de cada anillo) como perfil de fondo y se divide la imagen por él. La razón es ≈ 1 en la fotosfera y ≈ 0,35 en las manchas, en cualquier radio. Se aplica un filtro de media 3 × 3 para reducir el ruido y luego Otsu sobre la razón: umbral `0,720`, entre las dos clases.

### 8.4 Etiquetar regiones

Una región conectada es un grupo de píxeles de objeto que se tocan. Con conectividad 4, dos píxeles en diagonal son dos regiones; con conectividad 8, una. El laboratorio verifica ese conteo, y que un etiquetador propio (búsqueda en anchura) coincide con `scipy.ndimage.label` en una imagen aleatoria de 60 × 60: 335 regiones con conectividad 4 y 33 con 8. En el caso solar, tras Otsu y el filtro de media 3 × 3 aparecen **3 regiones** (con conectividad 8) de al menos 10 píxeles, como las tres manchas. Se aplicó un filtro de tamaño mínimo (10 px) para descartar manchitas de ruido; su coste es perder objetos reales muy pequeños.

### 8.5 Medir el acuerdo: IoU y Dice

Para dos cuadrados de 10 × 10 desplazados 2 columnas, la intersección es de 80 píxeles y la unión de 120: IoU `= 0,6667`, Dice `= 160/200 = 0,8`. Entre ambas hay una relación: `Dice = 2 IoU/(1 + IoU)`. Con la segmentación aplanada, el laboratorio da IoU `0,994` y Dice `0,997`. Con la global, `0,032` y `0,061`.

### 8.6 Cuidado con la exactitud por píxel

Una máscara vacía («no hay manchas») acierta el 98,8 % de los píxeles del disco, porque las manchas ocupan el 1,165 % (179 de 15 361). Su IoU es 0. Cuando el objeto ocupa poco, la exactitud por píxel no sirve; usa IoU o Dice.

### 8.7 De la máscara al número científico

El área medida es la suma de los píxeles de la máscara: 178 px, 1,159 % del disco (verdad: 179, 1,165 %). Para convertirla en una cantidad física, hacen falta la escala de la imagen y la corrección por proyección sobre la esfera; no se trata aquí. La incertidumbre del área depende del borde: un error de ±1 píxel a lo largo del perímetro de una mancha de radio 6 es `2π · 6 · 1 ≈ 38` píxeles, un tercio de su área (113 px). Por eso se reporta el área con el umbral y la conectividad usados.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Nota |
|---|---|---|---|
| `I` | intensidad del píxel | unidades arbitrarias | disco: 400–1000 |
| `μ` | coseno del ángulo heliocéntrico | adimensional | `√(1 − (r/R)²)` |
| `T` | umbral | las de `I` o de la razón | Otsu: 759 (global), 0,720 (razón) |
| `ω₀`, `ω₁`, `μ₀`, `μ₁` | fracciones y medias de clase | — / de `I` | Otsu |
| IoU, Dice | índices de acuerdo | adimensional | 0–1 |
| Área | píxeles de la máscara | px o % del disco | 178 px; 1,159 % |

## 10. Convenciones y referencias

Máscara booleana: `True` = objeto. Conectividad declarada en cada caso (8 en el caso solar). Todo es **sintético**: la intensidad, el contraste de las manchas y el ruido son ficticios; semilla 15013. El oscurecimiento al borde se modela con una ley simple de esta clase.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | SciPy, `scipy.ndimage.label`, manual | https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.label.html | Etiquetado de regiones conectadas; estructura por defecto en cruz (4 vecinos) en 2D; conectividad 8 con una estructura de unos 3×3 | Consultada el 2026-11-05 mediante extracción automática |

Límites: el método de Otsu, IoU y Dice se definen aquí y se verifican por propiedades y casos exactos; el artículo original del método no se consultó. El modelo del disco solar es ficticio y no se usó ningún dato solar. S1 respalda solo el comportamiento del etiquetador.

## 12. Cómo ver la segmentación

Equivalente accesible a las imágenes del laboratorio:

| Método | Píxeles marcados | IoU | Dice |
|---|---|---|---|
| Verdad (tres manchas) | 179 | — | — |
| Otsu global (umbral 759) | 5659 | 0,032 | 0,061 |
| Razón + suavizado + Otsu (0,720) + tamaño ≥ 10 | 178 | 0,994 | 0,997 |

Descripción larga: en la imagen cruda el disco se oscurece hacia el borde y las manchas se confunden con el limbo; en la razón, el disco es casi uniforme con tres manchas oscuras redondas, una pequeña, una mediana y una grande, distribuidas en la mitad superior y derecha.

## 13. Ejemplo trabajado: ¿qué fracción del disco cubre la mancha mayor?

**Paso 1 · Datos (sintéticos).** Disco de radio `R = 70`; mancha de radio `6` en `(95, 55)`.

**Paso 2 · Áreas.** Disco: `π 70² = 15 394`; mancha: `π 6² = 113,1`.

**Paso 3 · Fracción teórica.** `113,1/15 394 = 0,735 %`.

**Paso 4 · Conteo de píxeles.** El laboratorio cuenta 179 píxeles para las tres manchas sobre un disco de 15 361 (`1,165 %`); las tres áreas teóricas suman `π (16 + 36 + 9) = 191,6`: la discretización da menos (179).

**Paso 5 · Incertidumbre.** Un error de ±1 px en el radio de la mayor cambia su área en `2π · 6 = 37,7` px, un tercio de 113. Reportar el área sin umbral ni conectividad es incompleto.

**Paso 6 · Lectura.** La segmentación aplanada dio 1,159 % (178 px) contra 1,165 % verdadero, un error de 0,6 %. La global dio 36 % de píxeles marcados: ese «resultado» describe el borde del disco, no las manchas.

## 14. Distintas formas de segmentar

**Umbral global** (Otsu): simple, exige dos grupos separados y fondo uniforme. **Umbral local o con fondo aplanado**: se adapta a fondos variables. **Crecimiento de regiones**: parte de semillas y añade vecinos similares. **Bordes** (cambios bruscos de intensidad): útil si las fronteras son nítidas. **Aprendizaje supervisado** (B15-C22, programada): clasifica con muestras etiquetadas. Elige por la forma del problema; evalúa siempre con IoU o Dice frente a una referencia.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Cuenta las regiones del siguiente mapa (1 = objeto) con conectividad 4 y con 8: filas `1100`, `0011`, `1001`, `1100`. *Pasos:* marca los grupos de vecinos.

<details><summary>Solución comentada</summary>

Con conectividad 4: `{(0,0),(0,1)}`, `{(1,2),(1,3),(2,3)}`, `{(2,0),(3,0),(3,1)}` ⇒ 3. Con 8: `(0,1)` y `(1,2)` se tocan en diagonal ⇒ las dos primeras se unen ⇒ 2 (8.4).
</details>

**Ejercicio 2 · con una pista.** Dos máscaras de 100 píxeles se solapan en 60. Calcula IoU y Dice. *Pista:* unión = 140.

<details><summary>Solución comentada</summary>

IoU `= 60/140 = 0,429`; Dice `= 120/200 = 0,6` (8.5). Comprueba la relación `2 · 0,429/1,429 = 0,6`.
</details>

**Ejercicio 3 · casi autónomo.** Para `[1; 1; 2; 2; 8; 9; 9; 10]`, calcula `σ_b²` si cortas entre 2 y 8.

<details><summary>Solución comentada</summary>

`0,5 · 0,5 · (9 − 1,5)² = 14,06` (8.1).
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Calcula la fracción del disco que ocupa una mancha de radio 6 y otra de radio 4 (disco de radio 70).

<details><summary>Solución comentada</summary>

`(6/70)² = 0,735 %`; `(4/70)² = 0,327 %` (13).
</details>

**Ejercicio 5.** ¿Desde qué radio la fotosfera cae por debajo de 759? (Usa `I = 1000(0,4 + 0,6μ)`.)

<details><summary>Solución comentada</summary>

`0,4 + 0,6μ = 0,759` ⇒ `μ = 0,598` ⇒ `r/R = √(1 − 0,358) = 0,801` ⇒ `r = 56,1` px; el área exterior es `1 − 0,801² = 35,8 %` del disco (8.2).
</details>

**Ejercicio 6.** Una mancha a `r/R = 0,9` tiene 0,35 de la intensidad local. Calcula su intensidad y la de la fotosfera vecina, y compara con el umbral global 759.

<details><summary>Solución comentada</summary>

`μ = √(1 − 0,81) = 0,436`; fotosfera `1000(0,4 + 0,262) = 661,6`; mancha `231,6`. Ambas están bajo 759: el umbral global las marca juntas (8.2). La razón mancha/fotosfera, 0,35, sí las separa (8.3).
</details>

**Ejercicio 7.** El filtro de tamaño elimina regiones de menos de 10 píxeles. ¿Cuál es el radio mínimo (en píxeles) de una mancha circular que sobrevive?

<details><summary>Solución comentada</summary>

`π r² ≥ 10` ⇒ `r ≥ 1,78` px. Las manchas menores se pierden: el coste de limpiar el ruido (8.4).
</details>

**Ejercicio 8.** Una IoU de 0,5, ¿qué Dice implica? ¿Y una IoU de 0,9?

<details><summary>Solución comentada</summary>

`Dice = 2 IoU/(1 + IoU)`: 0,5 ⇒ 0,667; 0,9 ⇒ 0,947 (8.5). El Dice siempre es mayor o igual que la IoU.
</details>

**Ejercicio 9 · transferencia.** El ruido de la fotosfera cerca del limbo (intensidad ≈ 400) con σ = 20 da una razón con σ = 0,05. ¿A cuántas σ está el umbral 0,72 de la fotosfera (razón 1,0) y de una mancha (0,35)?

<details><summary>Solución comentada</summary>

Fotosfera: `(1,0 − 0,72)/0,05 = 5,6σ`; mancha: `(0,72 − 0,35)/0,05 = 7,4σ`. Ambos márgenes son amplios, con muy pocos errores por píxel (`Q(5,6) ≈ 10⁻⁸`) incluso sin suavizar (C12, 8.4).
</details>

**Ejercicio 10 · transferencia.** Un colega dice que su algoritmo tiene «98,8 % de aciertos» al segmentar manchas. ¿Qué preguntas le haces?

<details><summary>Solución comentada</summary>

Que dé IoU o Dice: una máscara vacía obtiene 98,8 % porque las manchas ocupan 1,165 % del disco (8.6). Pregunta también por el umbral, la conectividad y el filtro de tamaño.
</details>

**Ejercicio 11 · transferencia.** Dos manchas se tocan solo por una esquina. ¿Las cuentas como una o dos? ¿Qué debes hacer?

<details><summary>Solución comentada</summary>

Depende de la conectividad: 8 ⇒ una; 4 ⇒ dos (8.4). Declara la que usas, y decide según el criterio científico (por ejemplo, si el fenómeno agrupa regiones contiguas).
</details>

**Ejercicio 12 · integrador.** Elabora tu *máscara segmentada con métricas*: genera tu disco con oscurecimiento al borde y tres manchas, segmenta con Otsu global y con el método aplanado, calcula píxeles marcados, IoU, Dice, número de regiones y área como fracción del disco, y comenta por qué difieren.

<details><summary>Solución modelo</summary>

Tabla como la de la sección 12: Otsu global con decenas de veces más píxeles que la verdad y IoU muy baja; método aplanado con IoU superior a 0,9, tres regiones y área dentro de pocos por ciento de la verdadera. Datos sintéticos, semilla, versiones y fuente S1 con fecha; declaración de conectividad y de tamaño mínimo.
</details>

## 17. Laboratorio: Otsu, regiones conectadas e IoU

El script [segmentacion.py](segmentacion.py) verifica Otsu contra el óptimo analítico de una mezcla, el etiquetador propio contra `scipy.ndimage.label` y el conteo con conectividad 4 y 8, las métricas IoU y Dice contra valores exactos, y segmenta el disco solar sintético con y sin aplanado.

**Datos:** sintéticos, semilla 15013. **Predice antes de ejecutar:** ¿funcionará el umbral global en un disco oscurecido? (No.) **Ejecución del 2026-11-05 (Python 3.12.9, NumPy 2.4.4, SciPy 1.17.1):**

```text
(1) Otsu en mezcla N(0,1)/N(4,1): umbral 1.995 (óptimo 2)
(2) tres cuadrados: 3 regiones; dos píxeles en diagonal: 2 (c4) y 1 (c8)
    imagen aleatoria 60x60, conectividad 4: propio 335, scipy 335
    imagen aleatoria 60x60, conectividad 8: propio 33, scipy 33
(3) cuadrados 10x10 desplazados 2 columnas: IoU 0.6667 (80/120 = 0.6667); Dice 0.8000 (160/200 = 0.8000)
(4) disco de 15361 px; área verdadera de las manchas: 179 px (1.165 % del disco)
    Otsu global (umbral 759): 5659 px; IoU 0.032; Dice 0.061
    razón a la fotosfera + suavizado 3x3 (umbral Otsu 0.720): 3 regiones, 3 con >= 10 px
    tras descartar regiones < 10 px: 178 px; IoU 0.994; Dice 0.997; área medida 1.159 % del disco
Pruebas superadas.
```

```bash
python programa/clases/B15/B15-C13-segmentacion-de-imagenes/segmentacion.py
```

**Límites:** el disco es conocido y circular; el perfil de fondo se estima con la mediana por anillos asumiendo simetría radial; ruido gaussiano; sin corrección geométrica de la proyección.

## 18. Errores frecuentes y cómo corregirlos

**Umbral global sobre un fondo que varía.** Se corrige con los ejercicios 5 y 6.

**Valorar con la exactitud por píxel.** Se corrige con el ejercicio 10.

**No declarar la conectividad.** Se corrige con los ejercicios 1 y 11.

**Dejar manchitas de ruido sin filtro de tamaño, o filtrar objetos reales pequeños.** Se corrige con el ejercicio 7.

**Reportar el área sin umbral ni incertidumbre de borde.** Sección 8.7.

## 19. Cómo sabrás que vas bien

Tras 8.1: ¿calculas `σ_b²` de un corte? Si no, ejercicio 3. Tras 8.4: ¿qué conectividad usas y por qué? Si no lo sabes, ejercicios 1 y 11. Tras 8.5: ¿IoU y Dice de dos máscaras? Si no, ejercicios 2 y 8.

## 20. Qué entregas y cómo se evalúa

El producto es tu **máscara segmentada con métricas** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Umbral | Arbitrario | Otsu sin comprobar | Otsu verificado y su fallo explicado | Aplana el fondo y justifica |
| Regiones | Sin etiquetar | Etiqueta sin declarar conectividad | Conectividad declarada y verificada | Contrasta con otra biblioteca |
| Métricas | Exactitud por píxel | IoU o Dice | IoU y Dice con referencia | Discute el efecto del tamaño del objeto |
| Medida | Sin área | Área sin incertidumbre | Área con umbral y borde | Incertidumbre del perímetro |
| Fuentes y rótulos | Sin fuente | Sin fecha | Con localizador y fecha | Rotula sintético vs observado |

**Condiciones críticas (no se compensan con promedio):** comparar con una referencia mediante IoU o Dice; declarar la conectividad y el umbral; citar solo fuentes consultadas.

## 21. Ética, seguridad y límites

Una segmentación define el número que se reporta: el área de manchas, nubes, hielo o cráteres. Cambiar el umbral para «obtener» un resultado es manipulación; declara el criterio antes. Si observas el Sol, hazlo solo con filtros solares certificados y supervisión; esta clase es educativa y usa datos ficticios (indicación de seguridad sin cita específica). Accesibilidad: las imágenes tienen descripción y tabla; el laboratorio funciona sin conexión.

## 22. Para cerrar y seguir

Segmentar es asignar etiquetas a píxeles; Otsu elige el umbral que mejor separa dos clases, pero falla con fondos que varían; se etiquetan regiones con una conectividad declarada y se evalúa con IoU y Dice; el área depende del borde. Queda abierta una pregunta: ¿cómo se superponen dos imágenes del mismo campo tomadas en momentos distintos?

**Glosario español–inglés.** segmentación · *segmentation*; umbralización · *thresholding*; región conectada · *connected component*; conectividad · *connectivity*; máscara · *mask*; intersección sobre unión · *intersection over union*; coeficiente de Dice · *Dice coefficient*; falso positivo · *false positive*.

**Continuidad.** B15-C14 reutiliza tu manejo de máscaras y regiones para el **registro y la alineación** de imágenes.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
<!-- /nav -->
