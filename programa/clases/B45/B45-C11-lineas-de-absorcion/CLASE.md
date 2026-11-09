# B45-C11 — Líneas de absorción

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B45](../../../tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md) · [← Anterior: B45-C10 — Líneas de emisión](../B45-C10-lineas-de-emision/CLASE.md) · [Siguiente: B45-C12 — Efecto Doppler en espectros →](../B45-C12-efecto-doppler-en-espectros/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 11 del bloque B45. Nivel N3. Una línea de absorción mide cuánta materia hay en la línea de visión, pero se **satura**. Aquí calculas el **ancho equivalente** de una línea gaussiana en función de la profundidad óptica (**curva de crecimiento**), el **cociente de un doblete** 2:1 y la **columna de densidad** en el régimen lineal con `r_e` de NIST. Usas [B05](../../../tronco-comun/B05-fisica-fundamental-para-el-espacio.md) y [B31](../../../tronco-comun/B31-fisica-cuantica-nuclear-y-astroparticulas.md).

## 2. Por qué esta clase existe

Las líneas de absorción dan abundancias, pero las líneas fuertes no son proporcionales a la cantidad de átomos. La decisión central: **¿en qué régimen está la línea y cómo se obtiene la columna?**

## 3. Lo que podrás hacer al terminar

1. Calcular `W = ∫(1 − e^(−τ)) dx` numéricamente.
2. Reconocer los regímenes lineal y saturado.
3. Usar un doblete para detectar saturación.
4. Calcular `W = π r_e N f λ²` en el régimen lineal.
5. Recuperar la columna.
6. Reconocer la falta de alas de amortiguamiento.

La evidencia es la **ficha de líneas de absorción** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es la ley de Beer-Lambert?
2. ¿Qué es una integral?
3. ¿Qué es una columna de densidad?
4. ¿Qué es una fuerza de oscilador?
5. ¿Qué es el ancho equivalente?

<details>
<summary>Ver respuestas</summary>

1. `I = I₀ e^(−τ)`. 2. El área bajo una curva. 3. El número de átomos por unidad de área en la línea de visión. 4. La intensidad relativa de una transición. 5. El ancho de un rectángulo de profundidad 1 con la misma área.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Con `τ₀ = 0,01` el ancho equivalente adimensional es `0,01766` (lineal `0,01772`); con `τ₀ = 100`, `4,521`. Una columna de `5 × 10¹⁵ m⁻²` con `f = 0,64` a 589 nm da `W = 9,828 pm`. Es el **ejemplo conductor** (valores ilustrativos).

## 6. Vocabulario

La **profundidad óptica** `τ`. La **transmisión** `e^(−τ)`. El **ancho equivalente** `W`. La **curva de crecimiento** es `W` frente a la columna. La **saturación**: el centro de la línea ya es negro. El **radio clásico del electrón** `r_e` (S1). La **fuerza de oscilador** `f`.

## 7. Modelo mental: una persiana sobre una ventana

Como cerrar una persiana: las primeras láminas oscurecen mucho; cuando ya está casi cerrada, más láminas apenas cambian la luz.

```mermaid
flowchart LR
    N["columna N"] --> T["τ0 ∝ N f λ"]
    T --> P["τ(x) = τ0 e^(−x²)"]
    P --> W["W = ∫(1−e^−τ)dx"]
    W --> L["lineal / saturado"]
    L --> D["doblete 2:1"]
```

*Descripción textual:* la columna fija la profundidad óptica, que a su vez define el ancho equivalente en tres regímenes.

Analogía: una persiana sobre una ventana. Límite: perfil gaussiano puro, una sola componente.

## 8. La explicación, paso a paso

### 8.1 Curva de crecimiento

| τ₀ | W/b | lineal √π τ₀ | W/lineal | 2√(ln τ₀) |
|---|---|---|---|---|
| 0,01 | 0,01766 | 0,01772 | 0,9965 | — |
| 0,05 | 0,08708 | 0,08862 | 0,9826 | — |
| 0,10 | 0,17115 | 0,17725 | 0,9656 | — |
| 0,50 | 0,74877 | 0,88623 | 0,8449 | — |
| 1,00 | 1,28514 | 1,77245 | 0,7251 | — |
| 5,00 | 2,82475 | 8,86227 | 0,3187 | 2,5373 |
| 10,00 | 3,31375 | 17,72454 | 0,1870 | 3,0349 |
| 100,00 | 4,52056 | 177,24539 | 0,0255 | 4,2919 |
| 1000,00 | 5,45287 | 1772,45385 | 0,0031 | 5,2565 |
| 10000,00 | 6,24428 | 17724,53851 | 0,0004 | 6,0697 |

Para `τ₀` pequeño `W/lineal = 1 − τ₀/(2√2)` (con 0,01: 0,99646). A `τ₀ = 10⁴` el límite `2√(ln τ₀)` está a menos de 3 %.

### 8.2 Doblete 2:1

Cociente de anchos (fuerte/débil):τ₀ débil 0,01 → 1,9930; τ₀ débil 0,10 → 1,9325; τ₀ débil 1,00 → 1,5350; τ₀ débil 10,00 → 1,1237; τ₀ débil 100,00 → 1,0665;

### 8.3 Columna

Con `N = 5 × 10¹⁵ m⁻²`, `f = 0,64` y `λ = 589 nm`: `W = 9,8279 pm` (`W/λ = 1,669 × 10⁻⁵`); la columna recuperada es exactamente la inicial (cociente `1,000000`). Con `b = 3 pm`, `τ₀ = 1,848` y `τ₀ = 1` correspondería a `2,705 × 10¹⁵ m⁻²`: la línea ya está fuera del régimen lineal.

### 8.4 Lectura

Un cociente de doblete cercano a 2 indica régimen lineal; cercano a 1, saturación. En la saturación real, las alas de Voigt dominan y la curva sube más lentamente de lo mostrado.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `τ₀` | profundidad óptica central | — | 0,01 a 10⁴ |
| `b` | ancho Doppler | pm | 3 (ilustrativo) |
| `W` | ancho equivalente | pm | 9,828 |
| `r_e` | radio clásico del electrón | m | 2,8179403205 × 10⁻¹⁵ (S1) |
| `N` | columna de densidad | m⁻² | 5 × 10¹⁵ (ilustrativa) |
| `f` | fuerza de oscilador | — | 0,64 (ilustrativa) |

## 10. Convenciones y referencias

Perfil `τ(x) = τ₀ e^(−x²)`; Simpson en ±9; `W = π r_e N f λ²` en el régimen lineal; `f`, `N` y `b` **ilustrativos**.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NIST, *Fundamental Physical Constants* (CODATA 2022) | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | `r_e` (sección 9) | Consultada el 2026-11-09 |
| S2 | Fuerzas de oscilador de laboratorio | — | no consultadas; `f = 0,64` es ilustrativa | No consultado |

Límites: no se consultó ninguna tabla atómica; el perfil carece de alas de amortiguamiento, de modo que la zona saturada es cualitativa.

## 12. Cómo ver la curva de crecimiento

| τ₀ | W/b |
|---|---|
| 0,01 | 0,018 |
| 0,05 | 0,087 |
| 0,10 | 0,171 |
| 0,50 | 0,749 |
| 1,00 | 1,285 |
| 5,00 | 2,825 |
| 10,00 | 3,314 |
| 100,00 | 4,521 |
| 1000,00 | 5,453 |
| 10000,00 | 6,244 |

Descripción larga: W crece linealmente al principio y luego lentamente.

## 13. Ejemplo trabajado: W lineal con τ₀ = 0,01

**Paso 1 · Fórmula.** `W/b = √π τ₀`.

**Paso 2 · Cálculo.** `1,77245 × 0,01 = 0,01772`.

**Paso 3 · Corrección.** `× (1 − 0,01/(2√2)) = 0,01766`.

**Paso 4 · Contraste.** Numérico `0,01766`.

## 14. Distintas formas de describir el resultado

**Por fórmula:** régimen lineal. **Por integral:** Simpson. **Por doblete:** 2:1. **Por código:** `absorcion.py`.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** `W/b` lineal para `τ₀ = 0,01`. *Pasos:* ejemplo 13.

<details><summary>Solución comentada</summary>

`0,01772`.
</details>

**Ejercicio 2 · con una pista.** Transmisión en el centro con `τ₀ = 1`.

<details><summary>Solución comentada</summary>

`0,3679`.
</details>

**Ejercicio 3 · casi autónomo.** `W/b` con `τ₀ = 10`. *Pista:* tabla.

<details><summary>Solución comentada</summary>

`3,3138`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** `W` en pm para la columna dada.

<details><summary>Solución comentada</summary>

`9,828`.
</details>

**Ejercicio 5.** `τ₀` con `b = 3 pm`.

<details><summary>Solución comentada</summary>

`1,848`.
</details>

**Ejercicio 6.** Cociente del doblete con `τ₀ = 0,1`.

<details><summary>Solución comentada</summary>

`1,9325`.
</details>

**Ejercicio 7.** Cociente con `τ₀ = 10`.

<details><summary>Solución comentada</summary>

`1,1237`.
</details>

**Ejercicio 8.** Columna con `τ₀ = 1`.

<details><summary>Solución comentada</summary>

`2,705 × 10¹⁵ m⁻²`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** ¿Por qué un doblete detecta la saturación?

<details><summary>Solución comentada</summary>

Porque en régimen lineal sus anchos están en la razón de las fuerzas (2:1) y saturado tienden a 1.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Qué aporta el amortiguamiento (Voigt)?

<details><summary>Solución comentada</summary>

Alas que hacen crecer `W` en la zona saturada.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** Un compañero invierte `W = π r_e N f λ²` para `τ₀ = 20`. ¿Qué error comete?

<details><summary>Solución comentada</summary>

Subestima la columna: la línea está saturada.
</details>

**Ejercicio 12.** **Integrador.** Elabora tu *ficha de líneas de absorción*: curva, doblete, columna y límites.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de líneas de absorción*: curva, doblete, columna y límites.

<details><summary>Solución modelo</summary>

Secciones 8.1–8.4.
</details>

## 17. Laboratorio: curva de crecimiento

El script [absorcion.py](absorcion.py) integra el ancho equivalente para varios `τ₀`, verifica los límites y recupera la columna (**comprueba** el régimen lineal a `10⁻⁴`).

**Datos:** `r_e` de NIST (S1); `f`, `N`, `b` **ilustrativos**. **Predice antes de ejecutar:** ¿cuándo falla la relación lineal? (desde τ₀ ≈ 0,1.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
    tau0       W/b  lineal sqrt(pi)tau0  W/lineal  2 sqrt(ln tau0)
    0.01   0.01766              0.01772    0.9965              nan
    0.05   0.08708              0.08862    0.9826              nan
    0.10   0.17115              0.17725    0.9656              nan
    0.50   0.74877              0.88623    0.8449              nan
    1.00   1.28514              1.77245    0.7251              nan
    5.00   2.82475              8.86227    0.3187           2.5373
   10.00   3.31375             17.72454    0.1870           3.0349
  100.00   4.52056            177.24539    0.0255           4.2919
 1000.00   5.45287           1772.45385    0.0031           5.2565
10000.00   6.24428          17724.53851    0.0004           6.0697
cociente de anchos del doblete 2:1 (W fuerte / W debil):
  tau0 debil =   0.01 -> 1.9930
  tau0 debil =   0.10 -> 1.9325
  tau0 debil =   1.00 -> 1.5350
  tau0 debil =  10.00 -> 1.1237
  tau0 debil = 100.00 -> 1.0665
transmision en el centro: tau0 0.1 -> 0.9048, tau0 1.0 -> 0.3679, tau0 3.0 -> 0.0498
N = 5e15 m^-2 con f = 0,64 a 589 nm: W = 9.8279 pm (W/lambda = 1.669e-05) ; N recuperada/N = 1.000000
con b = 3 pm: tau0 = 1.8483 ; columna para tau0 = 1: 2.705e+15 m^-2
Pruebas superadas.
```

```bash
python programa/clases/B45/B45-C11-lineas-de-absorcion/absorcion.py
```

**Límites:** gaussiano, sin alas.

## 18. Errores frecuentes y cómo corregirlos

**Aplicar el régimen lineal a una línea saturada.** Se corrige con 8.1.

**Olvidar el cociente del doblete.** Se corrige con 8.2.

**Mezclar `W` en pm y en unidades de `b`.** Se corrige con la sección 9.

**Presentar `f = 0,64` como valor de laboratorio.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de líneas de absorción** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | conceptos de la clase | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con el análisis | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | fuentes con fecha | Declara lo ilustrativo |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular `f`, `N` y `b` como ilustrativos; no dar abundancias; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

El ancho equivalente crece como `√π τ₀` para `τ₀ ≲ 0,1` y luego se satura; un doblete 2:1 baja a 1,12 con `τ₀ = 10`. Queda una pregunta: ¿cómo se mide el corrimiento de las líneas?

**Glosario español–inglés.** línea de absorción · *absorption line*; profundidad óptica · *optical depth*; curva de crecimiento · *curve of growth*; saturación · *saturation*.

**Continuidad.** [B45-C12](../B45-C12-efecto-doppler-en-espectros/CLASE.md) estudia el efecto Doppler en espectros.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B45-C10 — Líneas de emisión](../B45-C10-lineas-de-emision/CLASE.md) · [📚 Bloque B45](../../../tronco-comun/B45-espectroscopia-fotometria-y-polarimetria.md) · [Siguiente: B45-C12 — Efecto Doppler en espectros →](../B45-C12-efecto-doppler-en-espectros/CLASE.md)
<!-- /nav -->
