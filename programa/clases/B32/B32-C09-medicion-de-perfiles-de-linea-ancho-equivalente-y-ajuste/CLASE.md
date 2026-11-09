# B32-C09 — Medición de perfiles de línea: ancho equivalente y ajuste

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B32](../../../tronco-comun/B32-atmosferas-estelares-y-espectroscopia-estelar-cuantitativa.md) · [← Anterior: B32-C08 — Síntesis espectral e inversión de perfiles](../B32-C08-sintesis-espectral-e-inversion-de-perfiles/CLASE.md) · [Siguiente: B32-C10 — Normalización y modelado del continuo espectral →](../B32-C10-normalizacion-y-modelado-del-continuo-espectral/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 9 del bloque B32. Nivel N3. El ancho equivalente `W` condensa una línea en un número, y la **curva de crecimiento** muestra cómo `W` crece con la columna de absorbedores. Aquí integras el ancho equivalente de una línea gaussiana y calculas `W(τ₀)` en los regímenes **lineal**, **saturado** y de transición. Usas [B05](../../../tronco-comun/B05-fisica-fundamental-para-el-espacio.md) y [B09-C11](../../B09/B09-C11-integrales-definidas/CLASE.md). Se supone un perfil Doppler puro.

## 2. Por qué esta clase existe

Medir una abundancia exige saber en qué régimen está la línea. La decisión central: **¿cómo depende el ancho equivalente de la columna de absorbedores?**

## 3. Lo que podrás hacer al terminar

1. Calcular `W = ∫(1 − I/I_c)dx`.
2. Verificar `W = A s√(2π)` para una gaussiana.
3. Calcular `W(τ₀)` por Simpson.
4. Reconocer el régimen lineal `√π τ₀`.
5. Reconocer el saturado `2√(ln τ₀)`.
6. Reconocer la transición.

La evidencia es la **ficha de la curva de crecimiento** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es una intensidad específica?
2. ¿Qué es una temperatura efectiva?
3. ¿Qué es una integral numérica?
4. ¿Qué es una función fuente?
5. ¿Qué es un perfil de línea?

<details>
<summary>Ver respuestas</summary>

1. La energía por área, tiempo, frecuencia y ángulo sólido. 2. La del cuerpo negro que da el mismo flujo. 3. Una suma que aproxima un área. 4. `S = j/κ`. 5. La forma de la absorción en función de la longitud de onda.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Una línea gaussiana de profundidad `0,6` y `s = 0,05` tiene `W = 0,07519885`, igual a `A s√(2π)`. Es el **ejemplo conductor**. Para `τ₀ = 0,01`, `W = 0,017662` (lineal); para `τ₀ = 1000`, `W = 5,4529` (saturado).

## 6. Vocabulario

El **ancho equivalente** `W`. La **profundidad óptica central** `τ₀`. La **curva de crecimiento**. El **régimen lineal**, el **saturado** y el **de amortiguamiento**.

## 7. Modelo mental: pintar con una brocha

Al principio, más pintura da más color; después de cubrir el centro, más pintura solo ensancha un poco los bordes.

```mermaid
flowchart LR
    TAU["τ₀"] --> W["W = ∫(1 − e^(−τ₀φ))dx"]
    W --> L["τ₀ pequeña: √π τ₀"]
    W --> S["τ₀ grande: 2√ln τ₀"]
```

*Descripción textual:* la profundidad óptica determina el ancho equivalente, que crece linealmente al principio y luego se satura.

Analogía: al principio, más pintura da más color; después de cubrir el centro, más pintura solo ensancha un poco los bordes. Límite: perfil Doppler puro.

## 8. La explicación, paso a paso

### 8.1 Curva de crecimiento (unidades Doppler)

| `τ₀` | `W` | `√π τ₀` | `2√(ln τ₀)` | régimen |
|---|---|---|---|---|
| 0,01 | 0,017662 | 0,017725 | — | lineal |
| 0,1 | 0,171146 | 0,177245 | — | lineal |
| 1 | 1,285145 | 1,772454 | — | transición |
| 10 | 3,313753 | 17,7245 | 3,0349 | saturado |
| 100 | 4,520558 | 177,245 | 4,2919 | saturado |
| 1000 | 5,452873 | 1772,45 | 5,2565 | saturado |

### 8.2 Lectura

Entre `τ₀ = 0,01` y `1000` (factor `10⁵`), `W` solo crece un factor 309: la saturación hace que `W` pierda sensibilidad a la columna. La asíntota `2√(ln τ₀)` subestima `W` un 9 %, 5 % y 4 % en `τ₀ = 10, 100, 1000`.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `W` | ancho equivalente | unid. Doppler | ver 8.1 |
| `τ₀` | profundidad óptica central | — | 0,01–1000 (ilustrativa) |
| `A`, `s` | profundidad y ancho de la gaussiana | — | 0,6; 0,05 |

## 10. Convenciones y referencias

Perfil gaussiano; parámetros ilustrativos.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| — | Sin fuente externa | — | relaciones estándar que verifica el laboratorio | No se consultó una fuente para esta clase |

Límites: no se consultó ninguna curva de crecimiento publicada.

## 12. Cómo ver la curva

| `τ₀` | `W` |
|---|---|
| 0,01 | 0,0177 |
| 1 | 1,285 |
| 100 | 4,52 |
| 1000 | 5,45 |

Descripción larga: `W` crece linealmente y luego casi se aplana.

## 13. Ejemplo trabajado: ancho equivalente de una gaussiana

**Paso 1 · Profundidad.** `A = 0,6`.

**Paso 2 · Ancho.** `s = 0,05`.

**Paso 3 · Producto.** `0,6 × 0,05 × √(2π)`.

**Paso 4 · Valor.** `0,07520`.

## 14. Distintas formas de describir una línea

**Por área:** `W`. **Por régimen:** lineal, saturado. **Por columna:** `τ₀`.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** `W` de la gaussiana. *Pasos:* ejemplo 13.

<details><summary>Solución comentada</summary>

`0,0752`.
</details>

**Ejercicio 2 · con una pista.** `W` lineal para `τ₀ = 0,05`.

<details><summary>Solución comentada</summary>

`√π × 0,05 = 0,0886`.
</details>

**Ejercicio 3 · casi autónomo.** `W/(√π τ₀)` para `τ₀ = 0,1`.

<details><summary>Solución comentada</summary>

`0,966`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Cociente `W(1000)/W(10)`.

<details><summary>Solución comentada</summary>

`1,65`.
</details>

**Ejercicio 5.** ¿Qué `τ₀` se saturó?

<details><summary>Solución comentada</summary>

Del orden de 10.
</details>

**Ejercicio 6.** Aumento de `W` entre 100 y 1000.

<details><summary>Solución comentada</summary>

`20,6 %`.
</details>

**Ejercicio 7.** `2√(ln 100)`.

<details><summary>Solución comentada</summary>

`4,29`.
</details>

**Ejercicio 8.** ¿Por qué la abundancia es incierta en el régimen saturado?

<details><summary>Solución comentada</summary>

Porque `W` casi no cambia con `τ₀`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un compañero deduce abundancias de una sola línea saturada. Responde.

<details><summary>Solución comentada</summary>

Es poco fiable por la insensibilidad.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Qué agrega el amortiguamiento?

<details><summary>Solución comentada</summary>

Un régimen en que `W ∝ √τ₀`.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Qué verifica Simpson?

<details><summary>Solución comentada</summary>

La implementación.
</details>

**Ejercicio 12.** **Integrador.** Elabora tu *ficha de la curva de crecimiento*: tabla y regímenes.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.2.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de la curva de crecimiento*: tabla y regímenes.

<details><summary>Solución modelo</summary>

Secciones 8.1–8.2.
</details>

## 17. Laboratorio: ancho equivalente y curva de crecimiento

El script [crecimiento.py](crecimiento.py) integra `W(τ₀)` (**comprueba** `10⁻⁸` y el régimen lineal al 1 %).

**Datos:** sin constantes; parámetros **ilustrativos**. **Predice antes de ejecutar:** ¿cómo crece `W`? (lineal y luego saturado.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
linea gaussiana A = 0.6, s = 0.05: W numerico = 0.07519885 ; A s sqrt(2 pi) = 0.07519885
    tau0  W (unidades Doppler)  sqrt(pi) tau0  2 sqrt(ln tau0)    regimen
    0.01              0.017662       0.017725              nan     lineal
     0.1              0.171146       0.177245              nan     lineal
       1              1.285145       1.772454              nan transicion
      10              3.313753      17.724539         3.034854   saturado
     100              4.520558     177.245385         4.291932   saturado
    1000              5.452873    1772.453851         5.256522   saturado
Pruebas superadas.
```

```bash
python programa/clases/B32/B32-C09-medicion-de-perfiles-de-linea-ancho-equivalente-y-ajuste/crecimiento.py
```

**Límites:** perfil Doppler puro.

## 18. Errores frecuentes y cómo corregirlos

**Esperar `W ∝ τ₀` siempre.** Se corrige con 8.1.

**Confundir `W` y profundidad.** Se corrige con la sección 6.

**Usar una sola línea saturada.** Se corrige con el ejercicio 9.

**Ignorar el amortiguamiento.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras 8: ¿qué resultado esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de la curva de crecimiento** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | conceptos de la clase | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con el análisis | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | fuentes con fecha | Declara lo ilustrativo |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular los parámetros como ilustrativos; no derivar abundancias reales; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Una gaussiana de profundidad 0,6 tiene `W = 0,0752` y la curva de crecimiento pasa de `W ≈ 0,018` a 5,45 al subir `τ₀` cien mil veces. Queda una pregunta: ¿cómo se define el continuo?

**Glosario español–inglés.** ancho equivalente · *equivalent width*; curva de crecimiento · *curve of growth*; régimen saturado · *saturated regime*; profundidad óptica central · *central optical depth*; columna · *column density*.

**Continuidad.** [B32-C10](../B32-C10-normalizacion-y-modelado-del-continuo-espectral/CLASE.md) estudia la normalización del continuo.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B32-C08 — Síntesis espectral e inversión de perfiles](../B32-C08-sintesis-espectral-e-inversion-de-perfiles/CLASE.md) · [📚 Bloque B32](../../../tronco-comun/B32-atmosferas-estelares-y-espectroscopia-estelar-cuantitativa.md) · [Siguiente: B32-C10 — Normalización y modelado del continuo espectral →](../B32-C10-normalizacion-y-modelado-del-continuo-espectral/CLASE.md)
<!-- /nav -->
