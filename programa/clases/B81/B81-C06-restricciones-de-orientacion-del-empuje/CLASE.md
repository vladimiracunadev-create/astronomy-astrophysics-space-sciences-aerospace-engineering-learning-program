# B81-C06 — Restricciones de orientación del empuje

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B81](../../../tronco-comun/B81-optimizacion-de-trayectorias-y-diseno-robusto.md) · [← Anterior: B81-C05 — Limitaciones de potencia en propulsión eléctrica](../B81-C05-limitaciones-de-potencia-en-propulsion-electrica/CLASE.md) · [Siguiente: B81-C07 — Modelos de aceleración para bajo empuje →](../B81-C07-modelos-de-aceleracion-para-bajo-empuje/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 6 del bloque B81 (área A06). Nivel N3. Una nave eléctrica tiene dos necesidades que compiten: apuntar el propulsor donde lo pide la trayectoria y apuntar los paneles al Sol. Si los paneles son fijos al cuerpo, desviar el empuje puede ganar potencia y perder dirección. Aquí modelas ese compromiso en el plano con una geometría sintética y adimensional y lo optimizas de forma analítica y por búsqueda. Usas [B81-C05](../B81-C05-limitaciones-de-potencia-en-propulsion-electrica/CLASE.md) solo para saber que el empuje es proporcional a la potencia. No se usaron fuentes externas.

## 2. Por qué esta clase existe

Una trayectoria óptima en el vacío no es necesariamente volable: el guiado debe respetar la orientación de los paneles. La decisión central: **¿cuánto conviene desviar el empuje de la dirección óptima para recuperar potencia, y dentro de qué cono?**

## 3. Lo que podrás hacer al terminar

1. Escribir la eficiencia útil `E(ψ, δ) = cos δ · |sin(ψ − δ)|`.
2. Obtener el óptimo libre `δ* = (ψ − 90°)/2` y `E* = (1 + sin ψ)/2`.
3. Verificarlo con una búsqueda en rejilla.
4. Aplicar un cono de orientación `|δ| ≤ δ_max`.
5. Traducir la eficiencia a un tiempo de misión.
6. Reconocer que el modelo es una geometría sintética, no un diseño de nave.

La evidencia es la **mapa de eficiencia de empuje frente a ángulos** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es el producto escalar de dos vectores unitarios?
2. ¿Qué es la normal de un panel?
3. ¿Por qué la potencia de un panel depende del coseno del ángulo de incidencia?
4. ¿Qué es un cono de restricción?
5. ¿Qué es un dato sintético?

<details>
<summary>Ver respuestas</summary>

1. El coseno del ángulo entre ellos. 2. El vector perpendicular a su superficie. 3. Porque la superficie efectiva frente a los rayos se reduce por ese factor. 4. El conjunto de direcciones que no se alejan más de un ángulo dado de un eje. 5. Un dato generado para el ejemplo, no medido.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

El Sol está a `ψ = 30°` de la dirección de empuje deseada y los paneles son fijos con normal perpendicular al empuje real. Sin desviar, la eficiencia es `0,5`; desviando `−30°` sube a `0,75` (+50 %). Con un cono de 10° llega a `0,633`. Es el **ejemplo conductor**; la geometría es **sintética y adimensional**.

## 6. Vocabulario

La **eficiencia útil** `E(ψ, δ) = cos δ · |sin(ψ − δ)|` combina la proyección del empuje sobre la dirección deseada (`cos δ`) y la fracción de potencia disponible (`|sin(ψ − δ)|`, la incidencia del Sol sobre el panel). El **cono de orientación** limita `|δ|`. `ψ` es el ángulo entre la dirección deseada y el Sol.

## 7. Modelo mental: velero y motor a la vez

```mermaid
flowchart LR
    PSI["angulo Sol-empuje psi"] --> D["desvío delta"]
    D --> P["potencia ~ |sin(psi - delta)|"]
    D --> U["empuje útil ~ cos(delta)"]
    P --> E["E = cos(delta) |sin(psi - delta)|"]
    U --> E
    E --> O["óptimo libre o con cono"]
```

*Descripción textual:* el ángulo entre Sol y empuje y el desvío elegido fijan la potencia y la proyección útil del empuje; su producto es la eficiencia, que se optimiza con o sin cono.

Analogía: un velero con motor que debe ir al norte pero cuyo panel solar prefiere mirar al este; si desvías un poco el rumbo ganas energía pero avanzas menos al norte. Límite: aquí los paneles no tienen gimbal y el modelo es plano; con paneles articulados el problema cambia.

## 8. La explicación, paso a paso

### 8.1 La función

Con los paneles fijos y la normal perpendicular al empuje real, la normal es `n = (−sin δ, cos δ)` y el Sol `s = (cos ψ, sin ψ)`, de modo que `s · n = sin(ψ − δ)`. El empuje es proporcional a la potencia y su proyección útil es `cos δ`: `E = cos δ |sin(ψ − δ)|`.

### 8.2 Óptimo libre

Para `δ` con `ψ − δ` en (0, 180°), `E = [sin ψ − sin(2δ − ψ)]/2`, máximo cuando `2δ − ψ = −90°`, es decir `δ* = (ψ − 90°)/2`, con `E* = (1 + sin ψ)/2`. Con `ψ = 30°`: `δ* = −30°` y `E* = 0,75`. La búsqueda en rejilla (paso 0,01°) da los mismos valores con error máximo `0`.

### 8.3 Tabla

| `ψ` | `E` sin desviar | `δ*` | `E*` |
|---|---|---|---|
| 20° | 0,3420 | −35° | 0,6710 |
| 30° | 0,5000 | −30° | 0,7500 |
| 45° | 0,7071 | −22,5° | 0,8536 |
| 60° | 0,8660 | −15° | 0,9330 |
| 90° | 1,0000 | 0° | 1,0000 |

### 8.4 Con cono y tiempo de misión

Para `ψ = 30°`: cono 5° → `E = 0,5714` (+14,3 %); 10° → `0,6330`; 20° → `0,7198`; 30° o más → `0,75`. Para un `Δv` de 4000 m/s con aceleración nominal de `10⁻³ m/s²` (ilustrativa), el tiempo es `46,3 d` con `E = 1` y `61,7 d` con el óptimo libre a `ψ = 30°`.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `ψ` | ángulo entre Sol y empuje deseado | grados | 20 a 120 |
| `δ` | desvío del empuje | grados | −35 a 15 |
| `E` | eficiencia útil | — | 0,34 a 1 |
| `δ_max` | semiángulo del cono | grados | 0 a 45 |

## 10. Convenciones y referencias

Geometría plana, sintética y adimensional; ángulos en grados. Paneles fijos al cuerpo con normal perpendicular al empuje real; potencia proporcional a la incidencia, sin sombras ni temperatura. Sin fuentes externas.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| — | Relaciones estándar (geometría vectorial plana, proyección del empuje, ley del coseno de la irradiancia sobre un panel) | — | las verifica el laboratorio con una segunda vía | No consultada en una fuente concreta |

Límites: no se consultó ninguna fuente para esta clase; la geometría es inventada y plana; no hay paneles articulados ni restricciones térmicas.

## 12. Cómo ver la eficiencia

| Magnitud | Valor |
|---|---|
| `E` sin desviar (`ψ = 30°`) | 0,500 |
| `E*` libre | 0,750 |
| `E` con cono 10° | 0,633 |
| error rejilla frente a analítico | 0 |

Descripción larga: la eficiencia sube con el desvío hasta el óptimo libre y deja de crecer cuando el cono lo contiene.

## 13. Ejemplo trabajado: el óptimo para ψ = 45°

**Paso 1 · Desvío.** `δ* = (45° − 90°)/2 = −22,5°`.

**Paso 2 · Eficiencia.** `E* = (1 + sin 45°)/2 = 0,8536`.

**Paso 3 · Comparación.** Sin desviar, `E = sin 45° = 0,7071`.

**Paso 4 · Ganancia.** `0,8536/0,7071 = 1,207`.

## 14. Distintas formas de describir la eficiencia de orientación

**Por fórmula:** `E = cos δ |sin(ψ − δ)|`. **Por óptimo:** `(1 + sin ψ)/2`. **Por cono:** máximo restringido. **Por tiempo:** `t = t_nom/E`.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `E` sin desviar para `ψ = 60°`. *Pasos:* `E = |sin ψ|`.

<details><summary>Solución comentada</summary>

`0,8660`.
</details>

**Ejercicio 2 · con una pista.** Calcula `δ*` y `E*` para `ψ = 60°`. *Pista:* fórmulas de 8.2.

<details><summary>Solución comentada</summary>

`δ* = −15°` y `E* = (1 + 0,866)/2 = 0,9330`.
</details>

**Ejercicio 3 · casi autónomo.** ¿Por qué `δ* = 0` cuando `ψ = 90°`?

<details><summary>Solución comentada</summary>

Porque el Sol ya incide perpendicular a los paneles con empuje alineado: `E = 1` sin desvío.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Con cono de 5° y `ψ = 30°`, ¿qué `E` esperas y qué ganancia da?

<details><summary>Solución comentada</summary>

`0,5714` (+14,3 %).
</details>

**Ejercicio 5 · autónomo.** ¿Qué pasa con `E` si `ψ = 0` (Sol detrás del empuje)?

<details><summary>Solución comentada</summary>

Sin desvío `E = 0`; con `δ* = −45°`, `E* = 0,5`.
</details>

**Ejercicio 6 · autónomo.** ¿Cuánto tarda la misión de 4000 m/s con `a = 10⁻³ m/s²` y `E = 0,75`?

<details><summary>Solución comentada</summary>

`46,3 d/0,75 = 61,7 d`.
</details>

**Ejercicio 7 · autónomo.** ¿Por qué la rejilla coincide exactamente con el analítico?

<details><summary>Solución comentada</summary>

El óptimo cae sobre un nodo de la rejilla (múltiplos de 0,01°).
</details>

**Ejercicio 8 · autónomo.** Para `ψ = 120°`, ¿por qué `δ*` es positivo?

<details><summary>Solución comentada</summary>

El Sol está al otro lado del empuje; el desvío óptimo gira hacia el lado contrario: `δ* = +15°`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** **Transferencia.** El guiado óptimo pide un desvío de 35° y el cono de la nave es de 20°. ¿Qué opciones hay?

<details><summary>Solución comentada</summary>

Aceptar `E = 0,72` (para `ψ = 30°`), cambiar la geometría de los paneles (gimbal) o reducir el tiempo con otra trayectoria.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** **Transferencia.** ¿Qué cambiaría con paneles articulados en un eje?

<details><summary>Solución comentada</summary>

La normal podría seguir al Sol y `E` se acercaría a `cos δ` solamente; el problema sería casi independiente de `ψ`.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** **Transferencia.** Un colega usa `E` constante en toda la trayectoria. ¿Qué error comete?

<details><summary>Solución comentada</summary>

`ψ` varía a lo largo de la órbita: `E` y el empuje útil cambian; hay que integrar con `E(t)`.
</details>

**Ejercicio 12 · integrador.** **Integrador.** **Integrador.** Elabora tu *mapa de eficiencia de empuje frente a ángulos*: tabla de `E`, `δ*` y `E*` para varios `ψ`, efecto del cono y tiempo de misión, con lo sintético rotulado.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: eficiencia de orientación con paneles fijos

El script [orientacion.py](orientacion.py) calcula `E(ψ, δ)`, el óptimo analítico y por rejilla, el efecto de un cono de orientación y el tiempo de misión (**comprueba** que la rejilla coincida con el analítico a 1e-6 y `E(30°, 0) = 0,5`).

**Datos:** geometría **sintética y adimensional**; sin datos externos. **Predice antes de ejecutar:** ¿qué `δ*` tendrá `ψ = 30°`? (−30°.) **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Geometria SINTETICA; angulos en grados; E = cos(delta) |sin(psi - delta)|
 psi   E sin desviar   delta* libre   E* analitico   delta* rejilla   E* rejilla
  20         0.3420        -35.00         0.6710           -35.00       0.6710
  30         0.5000        -30.00         0.7500           -30.00       0.7500
  45         0.7071        -22.50         0.8536           -22.50       0.8536
  60         0.8660        -15.00         0.9330           -15.00       0.9330
  90         1.0000          0.00         1.0000             0.00       1.0000
 120         0.8660         15.00         0.9330            15.00       0.9330
Error maximo del optimo libre (rejilla frente a analitico) = 0.00e+00
Con cono de orientacion |delta| <= dmax (psi = 30 grados):
 dmax   delta* [deg]   E*      ganancia sobre sin desviar
    0          0.00   0.5000      1.000
    5         -5.00   0.5714      1.143
   10        -10.00   0.6330      1.266
   20        -20.00   0.7198      1.440
   30        -30.00   0.7500      1.500
   45        -30.00   0.7500      1.500
psi =  30: tiempo con orientacion libre = 61.7 d frente a 46.3 d con E = 1 (acel. nominal ILUSTRATIVA 1e-3 m/s^2, dv 4000 m/s)
psi =  60: tiempo con orientacion libre = 49.6 d frente a 46.3 d con E = 1 (acel. nominal ILUSTRATIVA 1e-3 m/s^2, dv 4000 m/s)
psi =  90: tiempo con orientacion libre = 46.3 d frente a 46.3 d con E = 1 (acel. nominal ILUSTRATIVA 1e-3 m/s^2, dv 4000 m/s)
Pruebas superadas.
```

```bash
python programa/clases/B81/B81-C06-restricciones-de-orientacion-del-empuje/orientacion.py
```

**Límites:** plano; paneles fijos; sin sombras ni efectos térmicos; la aceleración nominal es ilustrativa.

## 18. Errores frecuentes y cómo corregirlos

**Suponer que apuntar el empuje siempre es lo mejor.** Se corrige con 8.2.

**Olvidar que `ψ` cambia con la posición.** Se corrige con el ejercicio 11.

**Usar el cono sin comparar con el óptimo libre.** Se corrige con 8.4.

**Presentar la geometría sintética como una nave real.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué `E*` esperabas a 30° y cuál obtuviste? Si dudas, repasa 8.2. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **mapa de eficiencia de empuje frente a ángulos** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Calcula `E` y su óptimo | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas con unidades | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con una segunda vía | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo ilustrativo y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular la geometría como sintética; no aplicar `E` constante a toda la trayectoria; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y sus datos son sintéticos o ilustrativos; ningún resultado describe una misión real ni sustituye a las herramientas de diseño y a la validación de una misión. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Desviar el empuje 30° sube la eficiencia de 0,5 a 0,75 con paneles fijos, y un cono de 10° recupera algo más de la mitad de esa mejora. Queda una pregunta: ¿qué modelo de aceleración usar cuando se integra una trayectoria completa?

**Glosario español–inglés.** cono de orientación · *pointing cone*; panel solar · *solar array*; ángulo de incidencia · *incidence angle*; eficiencia · *efficiency*; guiado · *guidance*.

**Continuidad.** [B81-C07](../B81-C07-modelos-de-aceleracion-para-bajo-empuje/CLASE.md) compara modelos de aceleración.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B81-C05 — Limitaciones de potencia en propulsión eléctrica](../B81-C05-limitaciones-de-potencia-en-propulsion-electrica/CLASE.md) · [📚 Bloque B81](../../../tronco-comun/B81-optimizacion-de-trayectorias-y-diseno-robusto.md) · [Siguiente: B81-C07 — Modelos de aceleración para bajo empuje →](../B81-C07-modelos-de-aceleracion-para-bajo-empuje/CLASE.md)
<!-- /nav -->
