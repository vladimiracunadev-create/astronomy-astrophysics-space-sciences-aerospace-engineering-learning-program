# B105-C05 — Cambios de visión

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B105](../../../tronco-comun/B105-medicina-y-biologia-espacial.md) · [← Anterior: B105-C04 — Sistema vestibular](../B105-C04-sistema-vestibular/CLASE.md) · [Siguiente: B105-C06 — Radiación ionizante y exposición →](../B105-C06-radiacion-ionizante-y-exposicion/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 5 del bloque B105. Nivel N3. El desplazamiento de líquidos hacia la cabeza (ver [B105-C01](../B105-C01-respuesta-cardiovascular-a-microgravedad/CLASE.md)) puede presionar el globo ocular y alterar la visión. Aquí conviertes un cambio de longitud axial del ojo en dioptrías con un modelo óptico mínimo y estimas cuántos ojos sintéticos superan un cambio dado.

## 2. Por qué esta clase existe

Una variación de décimas de milímetro puede cambiar la refracción en fracciones de dioptría y comparar eso con el error de medida decide si un cambio es real. La decisión central: **¿cuántos milímetros de acortamiento equivalen a una dioptría y cuántas personas la superarían?**

## 3. Lo que podrás hacer al terminar

1. Calcular la potencia del ojo reducido `P = n/L` y su sensibilidad `dD/dL`.
2. Convertir un acortamiento axial en dioptrías con la fórmula lineal y la exacta.
3. Estimar la fracción de una población sintética que supera un desplazamiento dado.
4. Calcular el acortamiento necesario para una dioptría.
5. Comparar un cambio con la incertidumbre de medida.
6. Rotular el modelo como didáctico y no valorar la vista de nadie.

La evidencia es la **ficha de visión con el cambio en dioptrías** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es una dioptría?
2. ¿Qué es la longitud axial del ojo?
3. ¿Qué es la hipermetropía?
4. ¿Qué es una linealización?
5. ¿Qué es un dato sintético?

<details>
<summary>Ver respuestas</summary>

1. El inverso de la distancia focal en metros (1/m). 2. La distancia entre la córnea y la retina (unos 22–24 mm). 3. Un error refractivo en que la imagen cae detrás de la retina. 4. Aproximar una función por su tangente en un punto. 5. Un dato generado para el ejemplo, no medido.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Un ojo reducido con `n = 1,336` y `L = 22,3 mm` tiene 59,91 D y una sensibilidad de 2,687 D por mm. Un acortamiento de 0,10 mm da +0,269 D (lineal) o +0,270 D (exacto); para +1,00 D se necesitan 0,372 mm. En una población **sintética** de 5.000 ojos (semilla 105, acortamiento `N(0,15; 0,08)` mm) el desplazamiento medio es +0,412 D, y el 33,3 % supera +0,50 D y el 0,5 % supera +1,00 D. La NASA indica que el desplazamiento de líquidos hacia la cabeza puede presionar los ojos y causar problemas de visión (consultada el 2026-11-10); la página no usa el término «SANS».

## 6. Vocabulario

El **ojo reducido** es un modelo de una sola superficie refractante con potencia `P = n/L`. El **desplazamiento hipermetrópico** es el error refractivo positivo por acortar el eje. La **dioptría** (D) es 1/m. El **acortamiento axial** `ΔL` es el cambio de longitud. La **presión intracraneal** es la presión del líquido cefalorraquídeo (LCR), cuya columna hidrostática depende de la gravedad.

## 7. Modelo mental

```mermaid
flowchart LR
    F["liquidos hacia<br/>la cabeza"] --> P["presion sobre<br/>el globo"]
    P --> L["acortamiento axial dL"]
    L --> D["dD = n dL / L^2"]
    D --> Pob["fraccion de la poblacion<br/>sobre un umbral"]
```

*Descripción textual:* el desplazamiento de líquidos presiona el globo; el acortamiento axial se convierte en dioptrías con la sensibilidad `n/L²` y se estima cuántas personas de una población sintética superan un umbral.

Analogía: acercar la pantalla al proyector, la imagen deja de enfocarse sobre ella. Límite: el ojo real tiene varias superficies, y la retina, el nervio óptico y el cristalino cambian por otros motivos.

## 8. La explicación, paso a paso

### 8.1 Potencia y sensibilidad

`P = n/L = 1,336/0,0223 = 59,91 D`. Para un ojo emétrope, mover la retina `ΔL` hacia el cristalino da `ΔD = n ΔL/L²` (lineal): 2,687 D por mm.

### 8.2 Lineal frente a exacto

`ΔD_exacto = n/(L − ΔL) − n/L`. Para 0,10 mm: 0,269 (lineal) frente a 0,270 (exacto); para 0,50 mm: 1,343 frente a 1,374. La linealización es buena para acortamientos pequeños.

### 8.3 Una población sintética

Con `ΔL ~ N(0,15; 0,08) mm`, el desplazamiento es +0,412 ± 0,211 D; el 33,3 % supera +0,50 D y el 0,5 %, +1,00 D. El acortamiento para +1,00 D es 0,372 mm.

### 8.4 La columna de líquido

La presión hidrostática de una columna de LCR de 0,20 m (`ρ = 1007 kg/m³`, ilustrativa) es 14,82 mmHg en la Tierra en vertical y 0 en microgravedad. Es un ejemplo del cambio de gradiente, no una medición de presión intracraneal.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `n` | índice del medio | — | 1,336 (didáctico) |
| `L` | longitud axial | mm | 22,3 |
| `P` | potencia | D | 59,91 |
| `ΔL` | acortamiento axial | mm | 0,05 a 0,50 |
| `ΔD` | desplazamiento hipermetrópico | D | +0,27 (0,10 mm) |
| `ρ_LCR` | densidad del LCR | kg/m³ | 1007 (ilustrativa) |

## 10. Convenciones y referencias

Dioptrías positivas = hipermetropía; `ΔL` positivo = acortamiento. Modelo de ojo reducido de una superficie. Datos sintéticos con semilla 105; `ΔL` ilustrativo. Tolerancias del laboratorio: `P = 59,91 ± 0,05 D`; pendiente 2,686 ± 0,01 D/mm; lineal frente a exacto a 0,10 mm dentro de 0,01 D. Numpy 2.4.4, Python 3.12.9.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| 1 | NASA, «Human body in space» (Human Research Program), resumen de la página por WebFetch | https://www.nasa.gov/hrp/bodyinspace/ (consultada el 2026-11-10) | el desplazamiento de líquidos hacia la cabeza puede presionar los ojos y causar problemas de visión; la NASA monitorea la distribución de líquidos (cualitativo) | Consultada (resumen de la página; no usa el término SANS) |
| — | Óptica del ojo reducido, linealización y estadística descriptiva | — | las verifica el laboratorio | No consultada en una fuente concreta (las verifica el laboratorio) |

Límites: la fuente es cualitativa; no se consultó literatura clínica de neuroimagen ni de oftalmología espacial; la distribución de `ΔL` es didáctica y no representa a ninguna tripulación.

## 12. Cómo ver el resultado

Descripción: la tabla de `ΔL` frente a `ΔD` en lineal y exacto, y la fracción poblacional sobre dos umbrales. Equivalente textual: 0,37 mm de acortamiento equivalen a una dioptría.

## 13. Ejemplo trabajado: dioptrías por 0,20 mm de acortamiento

**Paso 1 · Sensibilidad.** `n/L² = 1,336/0,0223² = 2.687 D/m`.

**Paso 2 · Producto.** `2.687·0,0002 = 0,537 D`.

**Paso 3 · Exacto.** `1,336/(0,0223 − 0,0002) − 59,91 = 0,542 D`.

**Paso 4 · Comparación.** La diferencia es 0,005 D: la linealización basta.

## 14. Distintas formas de describir el problema

**Por potencia:** `n/L`. **Por sensibilidad:** D por mm. **Por población:** fracción sobre un umbral. **Por presión:** `ρ g h`. **Por tabla:** `ΔL` frente a `ΔD`.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `ΔD` (lineal) para un acortamiento de 0,30 mm. *Pasos:* `2,687 D/mm·0,30`.

<details><summary>Solución comentada</summary>

`0,806 D`.
</details>

**Ejercicio 2 · con una pista.** ¿Qué acortamiento da +0,25 D? *Pista:* divide por 2,687.

<details><summary>Solución comentada</summary>

`0,093 mm`.
</details>

**Ejercicio 3 · casi autónomo.** Calcula `P` para `L = 22,3 mm` y `n = 1,336`.

<details><summary>Solución comentada</summary>

`59,91 D`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** ¿Cuál es la presión hidrostática de una columna de LCR de 0,15 m en la Tierra (`ρ = 1007 kg/m³`)?

<details><summary>Solución comentada</summary>

`1007·9,81·0,15/133,322 = 11,1 mmHg`.
</details>

**Ejercicio 5 · autónomo.** ¿Cuál es la distancia focal de unas gafas de +1,5 D?

<details><summary>Solución comentada</summary>

`1/1,5 = 0,667 m`.
</details>

**Ejercicio 6 · autónomo.** ¿Por qué lineal y exacto casi coinciden a 0,10 mm?

<details><summary>Solución comentada</summary>

Porque `ΔL/L = 0,45 %` es pequeño y la curvatura de `1/L` apenas se nota (diferencia 0,001 D).
</details>

**Ejercicio 7 · autónomo.** Para un ojo de `L = 24 mm`, ¿cuál es la sensibilidad `n/L²` en D/mm?

<details><summary>Solución comentada</summary>

`1,336/0,024² = 2.319 D/m = 2,319 D/mm`.
</details>

**Ejercicio 8 · autónomo.** ¿Cuál es el error estándar de la fracción 0,333 con `n = 5.000`?

<details><summary>Solución comentada</summary>

`√(0,333·0,667/5000) = 0,0067`.
</details>

**Ejercicio 9 · transferencia.** Una medición de longitud axial tiene incertidumbre de 0,05 mm. ¿A cuántas dioptrías equivale y qué implica para detectar +0,27 D?

<details><summary>Solución comentada</summary>

`0,05·2,687 = 0,134 D`: la incertidumbre es la mitad del efecto; hay que repetir mediciones.
</details>

**Ejercicio 10 · transferencia.** En microgravedad la columna hidrostática desaparece. ¿Por qué eso no implica que la presión intracraneal sea cero?

<details><summary>Solución comentada</summary>

El gradiente de peso desaparece, pero el LCR conserva una presión por el volumen y la distensibilidad del espacio; el laboratorio solo calcula el término `ρ g h`.
</details>

**Ejercicio 11 · transferencia.** De 6 tripulantes sintéticos con probabilidad 0,333 de superar +0,50 D, ¿cuántos se esperan y con qué desviación?

<details><summary>Solución comentada</summary>

`6·0,333 = 2` personas; DE `√(6·0,333·0,667) = 1,15`.
</details>

**Ejercicio 12 · integrador.** Elabora tu *ficha de visión con el cambio en dioptrías*: modelo, tabla `ΔL`→`ΔD`, fracción poblacional sobre dos umbrales, incertidumbre de medida y lista de qué es sintético.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: acortamiento axial y desplazamiento hipermetrópico

El script [vision.py](vision.py) calcula la potencia del ojo reducido, el desplazamiento por acortamiento (lineal y exacto) y la fracción de 5.000 ojos sintéticos sobre dos umbrales (**comprueba** `P = 59,91 D`, la pendiente 2,686 D/mm, la coincidencia lineal/exacta a 0,10 mm y los 0,372 mm por dioptría).

**Datos:** población **sintética** (semilla 105); modelo y `ΔL` **ilustrativos**. **Predice antes de ejecutar:** ¿Cuántas dioptrías da 0,10 mm de acortamiento? (Unas 0,27.) **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9; numpy 2.4.4
DATOS SINTETICOS (semilla 105): modelo de ojo reducido; DL ilustrativo; unica fuente consultada, cualitativa (NASA, 2026-11-10)
Potencia del ojo reducido = 59.91 D; pendiente dD/dL = 2.687 D por mm
Acortamiento axial DL [mm] -> desplazamiento hipermetropico [D] (lineal / exacto):
  0.05 mm -> 0.134 / 0.135 D
  0.10 mm -> 0.269 / 0.270 D
  0.20 mm -> 0.537 / 0.542 D
  0.37 mm -> 0.994 / 1.011 D
  0.50 mm -> 1.343 / 1.374 D
Poblacion sintetica de 5000 ojos: desplazamiento medio 0.412 D (DE 0.211); fraccion >= +0.50 D = 0.3330; fraccion >= +1.00 D = 0.00500
Acortamiento necesario para +1.00 D = 0.372 mm (lineal)
Presion hidrostatica de la columna de LCR a 0.20 m, Tierra, vertical   = 14.82 mmHg
Presion hidrostatica de la columna de LCR a 0.20 m, microgravedad      =  0.00 mmHg
Pruebas superadas.
```

```bash
python programa/clases/B105/B105-C05-cambios-de-vision/vision.py
```

**Límites:** ojo de una superficie, sin cambios del cristalino, del nervio óptico ni de la retina; sin neuroimagen; no diagnostica ni valora la visión de nadie.

## 18. Errores frecuentes y cómo corregirlos

**Confundir el signo del desplazamiento.** Acortar el eje da hipermetropía (positiva).

**Olvidar convertir milímetros a metros.** Usa `L` y `ΔL` en metros en `n ΔL/L²` (8.1).

**Atribuir toda la variación a un solo mecanismo.** El modelo es solo uno de varios posibles.

**Presentar la población sintética como datos de tripulantes.** Se rotula como sintética (sección 10).

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿conviertes un acortamiento en dioptrías? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de visión con el cambio en dioptrías** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Confunde las magnitudes | Parciales | Explica `P`, `ΔL` y `ΔD` | Explica los límites del ojo reducido |
| Cálculo | Sin unidades | Con errores | Calcula con unidades y tolerancias | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Compara con la verdad del generador | Interpreta la sensibilidad |
| Fuentes | Sin fuente | Sin fecha | Cita solo lo consultado, con fecha | Rotula lo sintético y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular los datos como sintéticos; no presentar un resultado simulado como observado; no dar consejo médico ni operativo; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase **educativa**: no es consejo médico, no sustituye la formación, la licencia ni la supervisión de profesionales, y no contiene dosis, tratamientos ni procedimientos para aplicar a una persona real. No se valora la visión de nadie; la evaluación oftalmológica de una persona real corresponde a profesionales con las pruebas adecuadas. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Un acortamiento axial de 0,372 mm basta para +1,00 D; en la población sintética el 33,3 % supera +0,50 D. Queda una pregunta: ¿qué dosis de radiación recibe el cuerpo y cómo se compara con un límite?

**Glosario español–inglés.** ojo reducido · *reduced eye*; dioptría · *diopter*; longitud axial · *axial length*; hipermetropía · *hyperopia*.

**Continuidad.** [B105-C06](../B105-C06-radiacion-ionizante-y-exposicion/CLASE.md) estudia la radiación ionizante y la exposición.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B105-C04 — Sistema vestibular](../B105-C04-sistema-vestibular/CLASE.md) · [📚 Bloque B105](../../../tronco-comun/B105-medicina-y-biologia-espacial.md) · [Siguiente: B105-C06 — Radiación ionizante y exposición →](../B105-C06-radiacion-ionizante-y-exposicion/CLASE.md)
<!-- /nav -->
