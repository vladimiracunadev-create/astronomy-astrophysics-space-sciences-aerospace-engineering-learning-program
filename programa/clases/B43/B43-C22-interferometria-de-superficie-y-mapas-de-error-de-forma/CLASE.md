# B43-C22 — Interferometría de superficie y mapas de error de forma

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B43](../../../tronco-comun/B43-construccion-y-mecanica-de-telescopios.md) · [← Anterior: B43-C21 — Selección de vidrios ópticos: catálogos, homogeneidad y diagramas](../B43-C21-seleccion-de-vidrios-opticos-catalogos-homogeneidad-y-diagramas/CLASE.md) · [Siguiente: B43-C23 — Medición de rugosidad y su efecto en la luz dispersa →](../B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 22 del bloque B43. Nivel N3. Un interferómetro mide la forma de una superficie con una fracción de longitud de onda. Con cuatro interferogramas desplazados en fase se recupera el mapa. Aquí lo simulas con una superficie sintética, desenvuelves la fase y ajustas piston, inclinación y desenfoque para obtener el error de forma. Usas [B42](../../../tronco-comun/B42-optica-fisica-y-optica-adaptativa.md), [B15](../../../tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md) y [B10](../../../tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md).

## 2. Por qué esta clase existe

El mapa de error de forma es la prueba de aceptación de un espejo. La decisión central: **¿cómo se recupera la fase, qué se descuenta y qué PV y RMS quedan?**

## 3. Lo que podrás hacer al terminar

1. Generar cuatro interferogramas con desplazamientos de fase de 90°.
2. Recuperar la fase con `atan2(I₄−I₂, I₁−I₃)`.
3. Desenvolverla por filas y alinear las filas.
4. Ajustar piston, inclinación y desenfoque por mínimos cuadrados.
5. Calcular PV y RMS del resto y contarlos en franjas.
6. Comparar con la superficie verdadera.

La evidencia es la **ficha de interferometría de superficie** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es una franja de interferencia?
2. ¿Qué es la fase envuelta?
3. ¿Qué es un ajuste por mínimos cuadrados?
4. ¿Qué es un interferómetro de doble paso?
5. ¿Qué es el PV?

<details>
<summary>Ver respuestas</summary>

1. Una banda brillante u oscura por la suma de dos ondas. 2. La fase módulo `2π`. 3. Minimizar la suma de los cuadrados de los residuos. 4. Uno donde la luz recorre dos veces la superficie. 5. La diferencia entre el máximo y el mínimo.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Superficie **sintética** con inclinación, desenfoque, astigmatismo de 40 nm y esférica de 25 nm, ruido de fase de 0,02 rad y malla 64 × 64. La superficie tiene `14,8` franjas en total; tras ajustar piston, inclinaciones y desenfoque queda un resto de `97,3 nm` PV y `19,90 nm` RMS (`0,0314 λ`). La recuperación da `19,92 nm` RMS. Es el **ejemplo conductor**.

## 6. Vocabulario

El **desplazamiento de fase** (0, 90°, 180°, 270°). La **fase** `φ = 4πh/λ` en doble paso. El **desenvolvimiento** suma múltiplos de `2π`. El **ajuste de modos** quita `1, x, y, r²`. El **mapa de error de forma**. El **PV** y el **RMS** del resto.

## 7. Modelo mental: un mapa topográfico por curvas de nivel

Como un mapa topográfico donde cada curva de nivel es una franja: se cuentan los pasos desde un punto de referencia y se quita la pendiente general para ver el relieve fino.

```mermaid
flowchart LR
    H["superficie h"] --> F["fase 4πh/λ"]
    F --> I["4 interferogramas"]
    I --> W["fase envuelta"]
    W --> U["desenvolvimiento"]
    U --> A["ajuste de modos"]
    A --> M["mapa de error"]
```

*Descripción textual:* cuatro imágenes dan la fase envuelta; el desenvolvimiento la completa y el ajuste de modos deja el error de forma.

Analogía: un mapa topográfico por curvas de nivel. Límite: desplazamientos exactos, sin vibración, gradiente de fase < π por píxel.

## 8. La explicación, paso a paso

### 8.1 Superficie y recuperación

Malla 64 × 64 con `3228` puntos en el círculo de análisis (λ = 632,8 nm, doble paso).

| Magnitud | Superficie verdadera | Recuperada |
|---|---|---|
| RMS del resto (nm) | 19,896 | 19,920 |
| PV del resto (nm) | 97,32 | 100,68 |

La diferencia punto a punto entre ambos restos tiene `1,011 nm` RMS (ruido inyectado de 0,02 rad, equivalente a `0,02 λ/(4π) = 1,01 nm` por píxel).

### 8.2 Franjas

La superficie tiene `14,84` franjas (PV total/(λ/2)); el resto, `0,308`.

### 8.3 Del RMS de superficie al de frente de onda

`RMS_frente ≈ 2 × RMS_superficie = 39,79 nm` (ver C01).

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `λ` | longitud de onda | nm | 632,8 (uso general) |
| `φ` | fase | rad | 4πh/λ |
| `h` | altura de la superficie | nm | sintética |
| `I_k` | interferogramas | — | 4 |

## 10. Convenciones y referencias

Unidades del SI; coma decimal en el texto y punto decimal en las salidas del laboratorio; los ángulos están en radianes salvo que se indique y las longitudes de onda en nanómetros. Los telescopios y materiales de los ejemplos son ilustrativos.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | Algoritmos de desplazamiento de fase | — | algoritmo de cuatro pasos (verificado por simulación, texto no consultado) | No consultado |

Límites: Todo es sintético: ningún interferograma real. El algoritmo de cuatro pasos y el desenvolvimiento sencillo funcionan solo con gradientes de fase moderados; no se modelan vibración ni errores de calibración.

## 12. Cómo ver los resultados

| Magnitud | Valor |
|---|---|
| Franjas totales | 14,8 |
| Resto PV (nm) | 97,3 |
| Resto RMS (nm) | 19,90 |

Descripción larga: casi todas las franjas son inclinación y desenfoque, que se descuentan.

## 13. Ejemplo trabajado: la franja

**Paso 1 · Fase.** `φ = atan2(I₄−I₂, I₁−I₃)`.

**Paso 2 · Altura.** `h = φ λ/(4π)`.

**Paso 3 · Franjas del resto.** `97,3/(632,8/2) = 0,308`.

## 14. Distintas formas de describir la interferometría

**En palabras:** cuatro imágenes dan la fase y se quita lo corregible. **En fórmulas:** `h = φ λ/(4π)`. **En tabla:** PV y RMS. **En código:** `interferometria.py`.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Altura de una superficie con `φ = π` en doble paso.

<details><summary>Solución comentada</summary>

`λ/4 = 158,2 nm`.
</details>

**Ejercicio 2 · con una pista.** Franjas de una superficie de 1 µm PV.

<details><summary>Solución comentada</summary>

`1000/316,4 = 3,16`.
</details>

**Ejercicio 3 · casi autónomo.** RMS del resto verdadero.

<details><summary>Solución comentada</summary>

`19,90 nm`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** PV del resto verdadero.

<details><summary>Solución comentada</summary>

`97,3 nm`.
</details>

**Ejercicio 5.** RMS de frente de onda.

<details><summary>Solución comentada</summary>

`39,8 nm`.
</details>

**Ejercicio 6.** RMS en ondas.

<details><summary>Solución comentada</summary>

`0,0314 λ`.
</details>

**Ejercicio 7.** Ruido de altura por 0,02 rad.

<details><summary>Solución comentada</summary>

`1,01 nm`.
</details>

**Ejercicio 8.** Franjas del resto.

<details><summary>Solución comentada</summary>

`0,308`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** ¿Por qué se quitan inclinación y desenfoque?

<details><summary>Solución comentada</summary>

Porque se corrigen con la posición y el enfoque; no son error de forma.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Por qué falla el desenvolvimiento con ruido grande?

<details><summary>Solución comentada</summary>

Porque saltos de más de `π` entre píxeles se confunden con saltos de `2π`.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Es esta una medición real?

<details><summary>Solución comentada</summary>

No: es sintética.
</details>

**Ejercicio 12.** **Integrador.** Elabora tu *ficha de interferometría de superficie*: fase, desenvolvimiento y resto.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.3.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de interferometría de superficie*: fase, desenvolvimiento y resto.

<details><summary>Solución modelo</summary>

Secciones 8.1–8.3.
</details>

## 17. Laboratorio: cuatro pasos y ajuste de modos

El script [interferometria.py](interferometria.py) simula los interferogramas, recupera la fase y calcula PV y RMS del resto (**comprueba** `1 nm` en el RMS y `2 nm` en la diferencia).

**Datos:** superficie **sintética**; semilla `20261109`. **Predice antes de ejecutar:** ¿cuánto vale el resto? (≈ 20 nm RMS.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
puntos = 3228
rms_verdadero = 19.8958
pv_verdadero = 97.3226
rms_recuperado = 19.9203
pv_recuperado = 100.677
rms_diferencia = 1.01107
franjas_totales = 14.8441
franjas_resto = 0.307593
rms_ondas = 0.0314409
frente_rms_nm = 39.7917
Pruebas superadas.
```

```bash
python programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/interferometria.py
```

**Límites:** sin vibración ni calibración.

## 18. Errores frecuentes y cómo corregirlos

**Medir la altura en lugar de la fase.** Se corrige con 8.1.

**Olvidar el doble paso.** Se corrige con la sección 9.

**No quitar los modos.** Se corrige con 8.1.

**Tomar la simulación por medición.** Se corrige con los límites.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de interferometría de superficie** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | conceptos de la clase | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con el análisis | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | fuentes con fecha | Declara lo ilustrativo |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular todo como sintético; no atribuir el algoritmo a una fuente no leída; no presentar el mapa como de un espejo real.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

El resto de la superficie sintética mide `19,9 nm` RMS y la recuperación acierta a `1,0 nm`. Queda una pregunta: ¿qué pasa con la rugosidad fina?

**Glosario español–inglés.** interferometría · *interferometry*; desenvolvimiento de fase · *phase unwrapping*; franja · *fringe*; error de forma · *figure error*; doble paso · *double pass*.

**Continuidad.** [B43-C23](../B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md) estudia la rugosidad y la luz dispersa.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B43-C21 — Selección de vidrios ópticos: catálogos, homogeneidad y diagramas](../B43-C21-seleccion-de-vidrios-opticos-catalogos-homogeneidad-y-diagramas/CLASE.md) · [📚 Bloque B43](../../../tronco-comun/B43-construccion-y-mecanica-de-telescopios.md) · [Siguiente: B43-C23 — Medición de rugosidad y su efecto en la luz dispersa →](../B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md)
<!-- /nav -->
