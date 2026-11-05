# B06-C06 — Cantidad de sustancia y mol

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B06](../../../tronco-comun/B06-quimica-y-materia-del-universo.md) · [← Anterior: B06-C05 — Moléculas y geometría molecular](../B06-C05-moleculas-y-geometria-molecular/CLASE.md) · [Siguiente: B06-C07 — Estequiometría elemental →](../B06-C07-estequiometria-elemental/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Sexta clase del bloque B06. Con C01–C05 sabes cómo es un átomo y una molécula. Pero una muestra real, un puñado de polvo de asteroide o un litro de agua, tiene billones de billones de ellos. Aquí aprendes la unidad que permite contarlos sin escribir ceros: el mol. Sigues en el nivel N1.

Verás cómo se define el mol en el Sistema Internacional, qué es la masa molar y cómo se pasa de gramos a moles y de moles a número de átomos o moléculas. No verás todavía reacciones (C07 y C08) ni gases (C09).

## 2. Por qué esta clase existe

La misión OSIRIS-REx trajo a la Tierra 121,6 g de material del asteroide Bennu. Los análisis de laboratorio de una parte de esa muestra encontraron entre 4,5 y 4,7 % de carbono y entre 0,23 y 0,25 % de nitrógeno en masa (S1). Para comparar con los átomos de una nube o con una reacción química no sirven los gramos: hacen falta cantidades de átomos.

La decisión central es: **dada la masa de una muestra y su composición, ¿cuántos átomos o moléculas hay, con qué incertidumbre, y qué debo declarar para que el cálculo se reproduzca?** Aprenderás a convertir con unidades explícitas, a tratar una composición como un rango y a distinguir una medida de una estimación aplicada a otra muestra. Es la base de C07, C08 y C20.

## 3. Lo que podrás hacer al terminar

1. Enunciar la definición del mol y el valor de la constante de Avogadro.
2. Calcular la masa molar de una sustancia a partir de los pesos atómicos.
3. Convertir entre masa, cantidad de sustancia y número de partículas.
4. Pasar de porcentajes en masa a moles y a razones atómicas.
5. Propagar un rango de composición al resultado.
6. Redactar una hoja de conversión con unidades y supuestos.

La evidencia es la **hoja de conversión masa–mol–átomos** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

Necesitas C03 (pesos atómicos) y notación científica. Cinco preguntas:

1. ¿Cuál es el peso atómico del carbono? ¿Y del oxígeno?
2. Calcula `121,6 × 4,6/100`.
3. ¿Cuánto es `6,022 × 10²³ × 0,5`?
4. Si 5,5 g se reparten en partes de 12 g cada una, ¿qué fracción de una parte es?
5. ¿Qué diferencia hay entre masa y cantidad de átomos?

<details>
<summary>Ver respuestas</summary>

1. 12,011; 15,999. 2. 5,59. 3. 3,011 × 10²³. 4. 0,458. 5. La masa es cuánto pesa; la cantidad de átomos es cuántos hay, y un átomo de oxígeno pesa más que uno de carbono.
</details>

Con cuatro o cinco aciertos, sigue. Con tres o menos, repasa C03.

## 5. Un caso real: ¿cuántos átomos de carbono trajo OSIRIS-REx?

Glavin y colaboradores informan que la muestra total entregada a la Tierra fue de 121,6 g y que los análisis tempranos de laboratorio hallaron C = 4,5–4,7 % y N = 0,23–0,25 % en peso (S1). Si aplicáramos esos porcentajes a los 121,6 g, tendríamos entre 5,47 y 5,72 g de carbono. ¿Cuántos átomos son?

Cuidado con lo que esto significa: los porcentajes se midieron en porciones analizadas, no en la muestra completa, así que el resultado es una **estimación** de la clase, no una medida de los 121,6 g. Aun así es un buen ejercicio de contar. Ten presente el límite: no se conoce la heterogeneidad de la muestra completa.

## 6. Vocabulario

La **cantidad de sustancia** `n` mide cuántas entidades elementales (átomos, moléculas, iones, electrones…) hay en una muestra. Su unidad es el **mol**: un mol contiene exactamente 6,022 140 76 × 10²³ entidades elementales, número que es el valor fijado de la **constante de Avogadro** `N_A` (en mol⁻¹), según la definición vigente del SI (S2). La **masa molar** `M` es la masa de un mol de una sustancia: se mide en g/mol y, para un elemento, coincide numéricamente con su peso atómico (C03). Para una molécula, `M` es la suma de las masas molares de sus átomos.

La **unidad de masa atómica** `u` es la masa de un doceavo del átomo de ¹²C (C03); vale 1,660 539 068 92 × 10⁻²⁷ kg (S3). Una **composición en masa** (o «% en peso») es la fracción de la masa total que corresponde a un elemento.

## 7. Modelo mental: la docena gigante

Una docena es un número fijo de huevos; si sabes lo que pesa un huevo, sabes lo que pesa una docena. El mol es lo mismo pero con 6,022 × 10²³ partículas: si conoces la masa de un átomo en unidades de masa atómica, la masa de un mol en gramos es ese mismo número.

```mermaid
flowchart LR
    M["Masa m (g)"] -->|"dividir entre M (g/mol)"| N["Cantidad n (mol)"]
    N -->|"multiplicar por N_A (1/mol)"| P["Número de entidades N"]
    P -->|"dividir entre N_A"| N
    N -->|"multiplicar por M"| M
```

*Descripción textual:* un rombo de conversión con cuatro flechas. De masa a cantidad se divide entre la masa molar; de cantidad a número de partículas se multiplica por la constante de Avogadro; las flechas inversas deshacen cada paso.

La analogía de la docena sirve para ver que el mol es un número, no un peso; su límite es que 6,022 × 10²³ es tan grande que nunca se cuenta de a uno: se obtiene pesando.

## 8. La explicación, paso a paso

### 8.1 El mol y la constante de Avogadro

Desde 2019, el SI define el mol fijando el valor de `N_A = 6,022 140 76 × 10²³ mol⁻¹`; lo que antes se medía ahora se adopta por definición (S2). Con ese valor exacto y con la unidad de masa atómica `u`, el producto `N_A · u` es muy cercano a 1 g/mol: con los valores CODATA 2022 resulta `1,000 000 001 1 g/mol` (el laboratorio de la sección 17 lo calcula). Por eso «el peso atómico en u» y «la masa molar en g/mol» tienen el mismo número.

### 8.2 Masa molar

Se suman los pesos atómicos de la fórmula. Agua: `2 × 1,007975 + 15,9994 = 18,0153 g/mol`, que coincide con el valor que da el NIST WebBook (S4). Dióxido de carbono: `12,0106 + 2 × 15,9994 = 44,0094 g/mol` (el WebBook da 44,0095, S4).

### 8.3 Ida y vuelta

`n = m/M` y `N = n · N_A`. En un kilogramo de agua hay `1000/18,0153 = 55,51 mol`, es decir, `55,51 × 6,0221 × 10²³ = 3,343 × 10²⁵` moléculas. La masa de una molécula se obtiene dividiendo `M` entre `N_A`: `18,0153 × 10⁻³ kg/mol / 6,0221 × 10²³ = 2,99 × 10⁻²⁶ kg`.

### 8.4 De porcentajes a átomos

Con la composición en masa, la masa de cada elemento es `m_X = m_total × (% / 100)`. Para el carbono de Bennu: `121,6 g × 4,5/100 = 5,472 g` y `121,6 × 4,7/100 = 5,715 g`. Con `M(C) = 12,0106 g/mol`, resultan `0,4556` y `0,4758 mol`, y multiplicando por `N_A`, `2,74 × 10²³` a `2,87 × 10²³` átomos. Para el nitrógeno: `0,280–0,304 g`, `0,0200–0,0217 mol`, `1,20 × 10²²–1,31 × 10²²` átomos (todo en el laboratorio).

### 8.5 La razón atómica no es la razón de masas

Con valores centrales (C 4,6 %, N 0,24 %), la razón de masas C/N es `19,2`, pero la razón de **átomos** es `(4,6/12,0106)/(0,24/14,006855) = 22,4`, porque el carbono pesa menos por átomo. Para comparar con espectros o con abundancias solares (C02) se usa la razón de átomos.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor o nota |
|---|---|---|---|
| `n` | cantidad de sustancia | mol | — |
| `N_A` | constante de Avogadro | mol⁻¹ | 6,022 140 76 × 10²³ (exacta) |
| `M` | masa molar | g/mol | H₂O 18,0153; CO₂ 44,0095 |
| `m` | masa | g | — |
| `N` | número de entidades | — | `n N_A` |
| `u` | unidad de masa atómica | kg | 1,660 539 068 92 × 10⁻²⁷ (CODATA 2022) |
| `N_A u` | producto | g/mol | 1,000 000 001 1 |

## 10. Convenciones y referencias

Los pesos atómicos son los de la NIST, y donde la NIST da un intervalo se usa el punto medio (C03). La composición en masa de Bennu se da como un rango de laboratorio (S1). Los resultados se redondean a tres cifras significativas, porque el rango de partida sólo tiene dos. La constante de Avogadro es exacta: su valor no limita la incertidumbre del cálculo.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | D. P. Glavin et al., *Nature Astronomy* (2025), doi:10.1038/s41550-024-02472-9 | PDF de NASA NTRS, doc. 20250001355 | Muestra total de 121,6 g; C 4,5–4,7 % y N 0,23–0,25 % en peso | PDF leído el 2026-11-05 (PyMuPDF) |
| S2 | BIPM, *The International System of Units (SI)*, 9.ª ed. (2019), definición del mol | Sección 2.3, «The mole» (p. 20 del PDF descargado) | Un mol contiene exactamente 6,022 140 76 × 10²³ entidades; `N_A` exacta | PDF leído el 2026-11-05 |
| S3 | NIST, *CODATA Recommended Values* (2022): `N_A` y `u` | https://physics.nist.gov/cgi-bin/cuu/Value?na (y `?u`) | `N_A` exacta; `u = 1,660 539 068 92 × 10⁻²⁷ kg` | Consulta del 2026-11-05 |
| S4 | NIST Chemistry WebBook, H₂O y CO₂ | https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185 (y `C124389`) | Masas molares 18,0153 y 44,0095 g/mol | Consulta del 2026-11-05 |

Límites: la clasificación en lotes y la heterogeneidad de la muestra de Bennu no se conocen; los porcentajes proceden de análisis de porciones. El número de cifras significativas es una decisión de la clase.

## 12. Cómo ver las conversiones

Esta tabla es la versión accesible del rombo de conversión.

| Quiero | Tengo | Operación | Ejemplo |
|---|---|---|---|
| `n` (mol) | `m` (g) y `M` (g/mol) | `m/M` | 1000 g de agua → 55,51 mol |
| `N` | `n` (mol) | `n N_A` | 55,51 mol → 3,343 × 10²⁵ moléculas |
| `m` (g) | `n` y `M` | `n M` | 0,25 mol de CO₂ → 11,00 g |
| `m` de una molécula | `M` | `M/N_A` | agua → 2,99 × 10⁻²⁶ kg |

Si haces un gráfico de dos variables (masa contra cantidad), la pendiente es la masa molar; rotula ejes con su unidad. Descripción larga: la relación entre `m` y `n` es una recta que pasa por el origen.

## 13. Ejemplo trabajado: carbono y nitrógeno de Bennu

**Datos (observados, análisis de laboratorio de porciones, S1):** masa total 121,6 g; C 4,5–4,7 %; N 0,23–0,25 %. **Estimación de la clase:** aplicar esos porcentajes a los 121,6 g.

**Paso 1 · Masas.** C: `5,472` a `5,715 g`. N: `0,280` a `0,304 g`.

**Paso 2 · Moles.** `n(C) = 5,472/12,0106 = 0,4556 mol` y `5,715/12,0106 = 0,4758 mol`. `n(N) = 0,280/14,0069 = 0,0200` y `0,304/14,0069 = 0,0217 mol`.

**Paso 3 · Átomos.** `N(C) = 0,4556 × 6,0221 × 10²³ = 2,74 × 10²³` a `2,87 × 10²³`. `N(N) = 1,20 × 10²²` a `1,31 × 10²²`.

**Paso 4 · Razón atómica.** Con valores centrales, `C/N = 22,4`.

**Paso 5 · Incertidumbre.** El rango de carbono es ±2,2 % en torno a 4,6 %; el de nitrógeno, ±4,2 % en torno a 0,24 %. La razón C/N hereda ambos: unos ±6 % en total (suma en el peor caso).

**Sentido físico.** Una muestra de 121,6 g de polvo de asteroide contiene del orden de `10²³` átomos de carbono y `10²²` de nitrógeno. El mol permite escribir y comparar esas cantidades sin ceros y relacionarlas con abundancias solares (C02): para el Sol, `N_C/N_N = 10^(8,43−7,83) = 4,0`, mientras Bennu tiene unos 22 (valor central), una razón mucho mayor. La comparación es cualitativa porque la estimación de la clase es una extrapolación.

## 14. Dos formas de expresar una composición

Puedes dar la composición **en masa** (% en peso: lo que mide una balanza) o **en átomos** (razones `N_X/N_Y`: lo que ve un espectro). Las primeras son directas pero engañosas al comparar elementos de pesos distintos; las segundas requieren el paso por el mol. Declara siempre cuál usas. En un laboratorio se mide lo primero; en astronomía se compara lo segundo.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** ¿Cuántos moles hay en 36,03 g de agua? *Pasos:* `n = m/M` con `M = 18,0153 g/mol`.

<details><summary>Solución comentada</summary>

`36,03/18,0153 = 2,000 mol`. Si te dio 0,5, dividiste al revés.
</details>

**Ejercicio 2 · con una pista.** ¿Cuántas moléculas hay en 0,5 mol de agua? *Pista:* multiplica por `N_A`.

<details><summary>Solución comentada</summary>

`0,5 × 6,0221 × 10²³ = 3,011 × 10²³` moléculas.
</details>

**Ejercicio 3 · casi autónomo.** ¿Cuánto pesan 0,25 mol de CO₂?

<details><summary>Solución comentada</summary>

`m = n M = 0,25 × 44,0095 = 11,00 g`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Calcula los moles de carbono si hay 5,472 g de carbono.

<details><summary>Solución comentada</summary>

`5,472/12,0106 = 0,4556 mol`. Con 12 exacto sale 0,4560, igual en las tres primeras cifras.
</details>

**Ejercicio 5.** Calcula el número de átomos de nitrógeno en 0,280 g.

<details><summary>Solución comentada</summary>

`n = 0,280/14,0069 = 0,01999 mol`; `N = 0,01999 × 6,0221 × 10²³ = 1,20 × 10²²`.
</details>

**Ejercicio 6.** Con C 4,6 % y N 0,24 %, calcula la razón de masas y la razón de átomos C/N.

<details><summary>Solución comentada</summary>

Masas: `4,6/0,24 = 19,2`. Átomos: `(4,6/12,0106)/(0,24/14,0069) = 0,3830/0,017135 = 22,4`. Son distintas porque cada átomo de nitrógeno pesa más que uno de carbono.
</details>

**Ejercicio 7.** Calcula la masa de una molécula de agua en kg.

<details><summary>Solución comentada</summary>

`0,0180153 kg/mol / 6,0221 × 10²³ mol⁻¹ = 2,99 × 10⁻²⁶ kg`. Se parece a `18 u = 18 × 1,6605 × 10⁻²⁷ = 2,99 × 10⁻²⁶ kg`: es la misma cuenta por dos caminos.
</details>

**Ejercicio 8.** ¿Cuántas moléculas hay en 1 kg de agua?

<details><summary>Solución comentada</summary>

`n = 55,51 mol`; `N = 3,343 × 10²⁵`. Observa que un kilogramo no es un número «redondo» de moléculas.
</details>

**Ejercicio 9 · transferencia.** Una muestra de 5,0 g de un elemento puro contiene 0,1250 mol. ¿Qué elemento puede ser?

<details><summary>Solución comentada</summary>

`M = 5,0/0,1250 = 40,0 g/mol`. Es compatible con el calcio (40,078) y con el argón (39,948). La masa molar por sí sola no distingue: se necesita otro dato (por ejemplo, que el argón es un gas noble, C02).
</details>

**Ejercicio 10 · transferencia.** ¿Por qué «masa molar en g/mol» y «peso atómico en u» tienen el mismo número? ¿Es exacto?

<details><summary>Solución comentada</summary>

Porque `N_A u ≈ 1 g/mol`. Con CODATA 2022 el producto vale 1,000 000 001 1 g/mol: igual hasta una parte en 10⁹, pero no exacto (S3). Para cualquier cálculo de aula es indistinguible.
</details>

**Ejercicio 11 · transferencia.** Un titular dice: «la muestra de Bennu tiene 5,6 g de carbono». ¿Qué falta en esa afirmación?

<details><summary>Solución comentada</summary>

Falta decir que es una estimación (porcentaje de porciones analizadas aplicado a 121,6 g), que el porcentaje es un rango de 4,5 a 4,7 % (de 5,47 a 5,72 g) y la fuente. Aislada, la cifra parece una medida de la muestra completa y no lo es.
</details>

**Ejercicio 12 · integrador.** Elabora la *hoja de conversión masa–mol–átomos* (sección 20) para una muestra de tu elección con composición publicada: masa total, % en masa de dos elementos como rango, moles, átomos, razón atómica, la incertidumbre propagada y los supuestos.

<details><summary>Solución modelo</summary>

Sigue el ejemplo trabajado de la sección 13 con otra muestra (por ejemplo, un material con composición publicada). La hoja debe distinguir la medida (porcentaje de porción) de la estimación (aplicación a la muestra completa) y dar la fuente con fecha.
</details>

## 17. Laboratorio: de gramos a átomos

El script [mol_y_masa.py](mol_y_masa.py) convierte masas a moles y átomos para el carbono y el nitrógeno de Bennu y para 1 kg de agua. Antes de imprimir comprueba que `N_A u` valga 1 g/mol dentro de 10⁻⁸, que la masa molar del agua sea 18,0153 g/mol (±0,0005) y que la ida y vuelta masa → mol → masa sea exacta; si algo falla, se detiene.

**Datos:** publicados (S1, S2, S3); aplicación a 121,6 g: **estimada**. **Predice antes de ejecutar:** ¿cuántos átomos de carbono, del orden de? (10²³). **Resultados (2026-11-05, Python 3.12.9):** `N_A u = 1,0000000011 g/mol`; C: 5,472–5,715 g → 0,4556–0,4758 mol → 2,744–2,866 × 10²³ átomos; N: 0,280–0,304 g → 0,0200–0,0217 mol → 1,202–1,307 × 10²² átomos; razón atómica C/N = 22,4; 1 kg de agua = 55,51 mol = 3,343 × 10²⁵ moléculas; masa de un átomo de ¹²C = 1,99265 × 10⁻²⁶ kg.

```bash
python programa/clases/B06/B06-C06-cantidad-de-sustancia-y-mol/mol_y_masa.py
```

**Límites:** composición de porciones extrapolada a la muestra completa; pesos atómicos tomados en el punto medio de los intervalos. No sirve para muestras heterogéneas ni para cálculos de pureza.

## 18. Errores frecuentes y cómo corregirlos

**Dividir al revés (`M/m`).** Se corrige con el ejercicio 1.

**Confundir mol con masa.** Un mol es un número de partículas. Se corrige con la sección 7 y el ejercicio 3.

**Comparar razones de masa como si fueran razones de átomos.** Se corrige con el ejercicio 6.

**Dar más cifras que las que permite el dato.** Se corrige con la sección 10 y el ejercicio 11.

**Tratar una estimación como medida.** Se corrige con el ejercicio 11.

## 19. Cómo sabrás que vas bien

Tras 8.1: ¿qué fija la definición del mol? Si no lo sabes, relee. Tras 8.2: ¿puedes calcular la masa molar del CO₂? Si no, haz el ejercicio 3. Tras 8.3: ¿puedes pasar de masa a número de moléculas? Si no, repite los ejercicios 1 y 2. Tras 8.5: ¿por qué la razón de átomos difiere de la de masas? Si dudas, haz el ejercicio 6. Tras el laboratorio: ¿qué dos constantes se contrastan? Si lo ignoras, lee la cabecera del script.

## 20. Qué entregas y cómo se evalúa

El producto es tu **hoja de conversión masa–mol–átomos**: una tabla con masa, `M`, moles, átomos y razón atómica, con un rango de entrada, la incertidumbre propagada y los supuestos.

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conversión | Con errores | Correcta con ayuda | Correcta con unidades | Verifica por dos caminos |
| Razón atómica | La confunde con masa | La calcula con error | Correcta | Compara con abundancias |
| Incertidumbre | Ausente | Cualitativa | Propagada | Justifica la propagación |
| Distinción medida/estimada | No | A veces | Siempre | Explica el riesgo de extrapolar |
| Fuentes | Sin fecha | Con fuente | Con fecha y edición | Contrasta dos fuentes |

**Condiciones críticas:** no presentar una estimación como medida; no mezclar masa y átomos; citar sólo fuentes consultadas.

## 21. Ética, seguridad y límites

Es un cálculo; no hay reactivos. Las muestras de asteroides son material científico irremplazable: se manipulan en instalaciones especiales y no se compran ni se comercian sin procedencia verificada; esta clase sólo usa los datos publicados. Accesibilidad: tablas equivalentes a los diagramas y fórmulas en texto. Una conversión sin unidades es una invitación al error (B01-C04).

## 22. Para cerrar y seguir

El mol es el número fijo 6,022 140 76 × 10²³ de entidades; la masa molar convierte gramos en moles y el producto con `N_A` da el número de partículas. Siempre se distingue la medida de la estimación y la razón de masas de la de átomos. En la próxima clase usarás estas conversiones para saber en qué proporciones se combinan las sustancias.

**Glosario español–inglés.** mol · *mole*; cantidad de sustancia · *amount of substance*; constante de Avogadro · *Avogadro constant*; masa molar · *molar mass*; unidad de masa atómica · *atomic mass unit*; composición en masa · *mass composition*.

**Continuidad.** B06-C07 usa el mol para calcular composiciones y proporciones de combinación. B06-C09 lo retoma en la ley de los gases.

**Referencias:** ver sección 11. S1 a S4 son consultas del 2026-11-05; la aplicación de los porcentajes a 121,6 g es una estimación de la clase.

<!-- nav:bottom -->
---

[← Anterior: B06-C05 — Moléculas y geometría molecular](../B06-C05-moleculas-y-geometria-molecular/CLASE.md) · [📚 Bloque B06](../../../tronco-comun/B06-quimica-y-materia-del-universo.md) · [Siguiente: B06-C07 — Estequiometría elemental →](../B06-C07-estequiometria-elemental/CLASE.md)
<!-- /nav -->
