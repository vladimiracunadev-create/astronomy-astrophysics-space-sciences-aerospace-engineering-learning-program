# B87-C07 — Rastreadores estelares

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B87](../../../tronco-comun/B87-sensores-y-control-de-actitud.md) · [← Anterior: B87-C06 — Giroscopios MEMS](../B87-C06-giroscopios-mems/CLASE.md) · [Siguiente: B87-C08 — Calibración de sensores →](../B87-C08-calibracion-de-sensores/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 7 del bloque B87. Nivel N3. Un rastreador estelar (*star tracker*) fotografía el cielo, mide las posiciones de varias estrellas en el detector y, comparándolas con un catálogo, entrega la actitud absoluta con precisión de segundos de arco. Aquí modelas una cámara sintética de `1024 × 1024 px` y `15°` de campo, estrellas sintéticas (direcciones aleatorias, **no** un catálogo real), centroides con ruido de `0,1 px` y la actitud por SVD (problema de Wahba, C09). Mides el error transversal y el de balanceo.

## 2. Por qué esta clase existe

Para apuntar un telescopio o una antena con precisión de segundos de arco, un sensor solar o un magnetómetro no bastan. La decisión central: **¿cuántas estrellas hacen falta y por qué el giro alrededor del eje óptico (balanceo) es mucho peor que el apuntamiento?** Un sensor mide un cono estrecho y el giro alrededor de su eje se ve con un brazo de palanca corto.

## 3. Lo que podrás hacer al terminar

1. Proyectar direcciones del cuerpo sobre un detector con un modelo estenopeico (*pinhole*) y su IFOV.
2. Pasar el ruido de centroide en píxeles a ruido angular por estrella.
3. Estimar la actitud con SVD a partir de las estrellas medidas y separar el error transversal del de balanceo.
4. Predecir el error `σ_a/√N` transversal y `σ_a/(√N ρ_rms)` de balanceo y compararlo con Monte Carlo.
5. Explicar por qué con pocas estrellas la teoría subestima el error.
6. Separar lo sintético (estrellas, ruido) de lo consultado y de lo no consultado.

La evidencia es la **curva de error de actitud del rastreador estelar frente al número de estrellas** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es el IFOV de un detector?
2. ¿Qué es un centroide?
3. ¿Qué es un catálogo estelar?
4. ¿Cuál es el problema de Wahba?
5. ¿Qué es el balanceo (*roll*) respecto del eje óptico?

<details>
<summary>Ver respuestas</summary>

1. El ángulo que subtiende un píxel: `≈ 1/f` en radianes con `f` en píxeles. 2. El centro de brillo de la imagen de una estrella; su precisión baja de 1 px. 3. Una lista de direcciones de estrellas en un sistema inercial. 4. Hallar la rotación que mejor alinea vectores medidos con vectores de referencia. 5. El giro alrededor del eje de la cámara.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

La cámara sintética tiene `f = 3889 px` e IFOV `53,0″/px`. Con `0,1 px` de ruido de centroide (`5,30″` por eje), 20 estrellas dan `1,20″` por eje transversal y `16,3″` de balanceo; con 40, `0,83″` y `11,5″`. Todo es **sintético**: estrellas aleatorias, no un catálogo.

## 6. Vocabulario

El **modelo estenopeico** proyecta `(x, y) = f (bx/bz, by/bz)`. El **IFOV** es `atan(1/f)`. El **centroide** tiene ruido `σ_px`; el **ruido angular** por estrella es `σ_a = atan(σ_px/f)`. El **error transversal** (*cross-boresight*) es el giro alrededor de los ejes `x, y` del sensor. El **balanceo** (*roll*) es el giro alrededor del eje óptico `z`. El **radio rms** `ρ_rms` es la distancia angular cuadrática media de las estrellas al eje.

## 7. Modelo mental: muchas estrellas, una rotación

```mermaid
flowchart LR
    C["catalogo r_k (inercial)"] --> P["b_k = A r_k"]
    P --> Y["proyeccion + centroide con ruido"]
    Y --> W["Wahba por SVD"]
    W --> E["A estimada"]
    E --> X["error transversal y de balanceo"]
```

*Descripción textual:* las direcciones del catálogo, rotadas por la actitud, se proyectan en el detector con ruido de centroide; el SVD de Wahba devuelve la actitud y su error se descompone en transversal y de balanceo.

Analogía: como ver una veleta desde lejos con varios puntos de referencia: saber hacia dónde apunta la cámara es fácil, pero saber cuánto gira alrededor de su eje cuesta más porque los puntos están cerca del eje. Límite: el modelo es de estrellas ideales con ruido uniforme, sin distorsión, magnitud ni identificación.

## 8. La explicación, paso a paso

### 8.1 Geometría del sensor

Con `1024 px` y `15°` de campo: `f = 512/tan 7,5° = 3889,0 px` e `IFOV = 53,04″/px`. El ruido de centroide de `0,1 px` equivale a `σ_a = 5,30″` por estrella y eje.

### 8.2 Estimación por SVD

Para `N` estrellas con vectores medidos `b_k` y de catálogo `r_k`, el `A` que minimiza `Σ|b_k − A r_k|²` sale del SVD de `B = Σ b_k r_kᵀ` con la corrección de signo del determinante (la implementación `wahba_svd` del bloque). El error `ΔA = Â Aᵀ` es una rotación pequeña `φ` cuyos dos primeros componentes son el error transversal y el tercero es el balanceo.

### 8.3 Error frente al número de estrellas (1500 pruebas por fila)

| `N` | Transversal sim (″) | Teoría `σ_a/√N` (″) | Balanceo sim (″) | Teoría (″) |
|---|---|---|---|---|
| 3 | 3,72 | 3,06 | 62,0 | 40,7 |
| 5 | 2,53 | 2,37 | 38,3 | 31,5 |
| 10 | 1,70 | 1,68 | 23,9 | 22,3 |
| 20 | 1,20 | 1,19 | 16,3 | 15,8 |
| 40 | 0,83 | 0,84 | 11,5 | 11,1 |

### 8.4 Por qué el balanceo es peor

El balanceo se mide con el brazo de palanca `ρ_rms` (el radio medio de las estrellas, unos `4,3°`), mucho menor que 1 rad: `σ_roll ≈ σ_a/(√N ρ_rms)`, del orden de `14` veces el error transversal con 20 estrellas. Con 3 estrellas la teoría subestima el error (cociente `1,22` en transversal y `1,52` en balanceo) porque la configuración de pocas estrellas está mal condicionada. Por eso las misiones combinan varios rastreadores en ejes distintos o un giroscopio.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `f` | focal en píxeles | px | 3889,0 |
| `IFOV` | ángulo por píxel | ″ | 53,04 |
| `σ_px` | ruido de centroide | px | 0,1 |
| `σ_a` | ruido angular por estrella y eje | ″ | 5,30 |
| `N` | estrellas usadas | — | 3 a 40 |
| `ρ_rms` | radio angular rms de las estrellas | rad | ver 8.4 |

## 10. Convenciones y referencias

Cámara de `1024 × 1024 px`, campo de `15°` a lo largo del lado, eje óptico `+z` del cuerpo; estrellas **sintéticas** en el 70 % central del campo (sin magnitudes, sin identificación, sin distorsión). Tolerancias: acuerdo con la teoría dentro del 10 % para `N ≥ 10`; relación simulado/teoría entre 1,0 y 1,5 (transversal) y 1,6 (balanceo) para `N < 10`; balanceo `> 5×` el transversal. Cuaternión `q = [qx, qy, qz, qw]` con la parte escalar al final, `v_B = A(q) v_I`, producto tal que `A(q⊗p) = A(q) A(p)`, cinemática `q̇ = ½ [ω; 0] ⊗ q` con `ω` del cuerpo respecto del sistema inercial expresada en el cuerpo (la biblioteca [adcs_comun.py](../adcs_comun.py) del bloque lo comprueba). Sistema inercial `I` de **ejemplo** (ejes sin relación con J2000), órbita circular de dos cuerpos con radio terrestre `6 378 137 m` y `μ = 3,986004418 × 10¹⁴ m³/s²` como valores adoptados de ejemplo. Satélite **sintético** `I = diag(0,35; 0,40; 0,30) kg·m²` salvo que la clase diga otra cosa. Todo dato es sintético con semilla fija.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| — | Relaciones estándar de dinámica de actitud, estimación y control usadas en esta clase (ecuaciones de Euler, cinemática de cuaterniones, problema de Wahba, filtro de Kalman multiplicativo, estabilidad de Lyapunov, modelos de sensores y actuadores) | — | las verifica el laboratorio con una segunda vía (conservación, comparación entre métodos, propagación independiente o Monte Carlo) | No consultada en una fuente concreta |
| — | Libros de texto de actitud y control (p. ej. Wertz, Markley–Crassidis, Sidi) y hojas de datos de fabricantes | — | — | No consultada |
| — | Algoritmos de identificación de estrellas (triángulos, rejilla), catálogos reales (Hipparcos, Tycho) y especificaciones de rastreadores comerciales | — | — | No consultada |

Límites: Esta clase no tiene fuente consultada propia: el modelo de proyección, el SVD de Wahba y la teoría `σ_a/√N` no se consultaron en una fuente concreta; el laboratorio las valida comparando la simulación de Monte Carlo con la teoría.

## 12. Cómo ver el error del rastreador

| Magnitud | Valor |
|---|---|
| IFOV | 53,04″/px |
| transversal con 20 estrellas (sim / teoría) | 1,20″ / 1,19″ |
| balanceo con 20 estrellas (sim / teoría) | 16,3″ / 15,8″ |
| cociente balanceo/transversal (20) | 13,6 |

Descripción larga: el error transversal baja como `1/√N`; el balanceo es unas 14 veces mayor y también baja como `1/√N`.

## 13. Ejemplo trabajado: error de actitud con 20 estrellas

**Paso 1 · Ruido angular.** `σ_a = atan(0,1/3889) = 5,30″`.

**Paso 2 · Transversal.** `σ_a/√20 = 1,19″`; simulado `1,20″`.

**Paso 3 · Balanceo.** `σ_a/(√20 ρ_rms) = 15,8″`; simulado `16,3″`.

**Paso 4 · Cociente.** `13,6` veces.

**Paso 5 · Comprobación.** Con 40 estrellas ambos bajan por `√2`: `0,83″` y `11,5″`.

## 14. Distintas formas de describir la actitud de un rastreador estelar

**SVD de Wahba** (esta clase): óptimo en mínimos cuadrados con pesos iguales. **Método q y QUEST** (C09): equivalentes con otro cómputo. **Seguimiento (*tracking*):** tras la primera solución, se siguen las estrellas cuadro a cuadro y se filtra con el giroscopio (C10). Cada forma parte de las mismas direcciones medidas.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula la focal en píxeles de una cámara de `2048 px` y `20°` de campo. *Pasos:* `(N/2)/tan(FOV/2)`.

<details><summary>Solución comentada</summary>

`1024/tan 10° = 5807,4 px`.
</details>

**Ejercicio 2 · con una pista.** Con `f = 3889 px`, ¿qué ángulo subtiende `0,1 px`?

<details><summary>Solución comentada</summary>

`0,1/3889 = 2,57×10⁻⁵ rad = 5,30″`.
</details>

**Ejercicio 3 · casi autónomo.** Con `σ_a = 5,3″` y `N = 25`, ¿qué error transversal esperas?

<details><summary>Solución comentada</summary>

`5,3/√25 = 1,06″`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** ¿Cuántas estrellas hacen falta para bajar el error transversal a la mitad de `N = 10`?

<details><summary>Solución comentada</summary>

`N = 40` (el error baja como `1/√N`): `0,83″` frente a `1,70″` en el laboratorio.
</details>

**Ejercicio 5 · autónomo.** ¿Por qué el balanceo es mucho peor que el apuntamiento?

<details><summary>Solución comentada</summary>

Porque se mide con el brazo `ρ_rms ≈ 0,1 rad`, mientras el apuntamiento usa el ángulo total de las direcciones: `σ_roll/σ_cross ≈ 1/ρ_rms`.
</details>

**Ejercicio 6 · autónomo.** Si el campo se duplica con el mismo detector, ¿cómo cambia el balanceo?

<details><summary>Solución comentada</summary>

`f` baja a la mitad, `σ_a` se duplica, pero `ρ_rms` también se duplica: el balanceo queda igual en primer orden y el transversal se duplica.
</details>

**Ejercicio 7 · autónomo.** ¿Qué pasa si las estrellas están casi alineadas en el cielo?

<details><summary>Solución comentada</summary>

El SVD está mal condicionado y el balanceo (o un eje transversal) crece mucho; se pide una dispersión mínima.
</details>

**Ejercicio 8 · autónomo.** ¿Por qué con `N = 3` la teoría subestima el error?

<details><summary>Solución comentada</summary>

Porque la teoría asintótica supone muchas estrellas bien distribuidas; con tres, la geometría aleatoria es peor que la media (`1,22` veces).
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** **Transferencia.** Un colega usa `1,2″` como precisión de un rastreador comercial. ¿Es válido?

<details><summary>Solución comentada</summary>

No: el ruido de centroide, las estrellas y el campo son sintéticos y no hay distorsión, magnitud, identificación ni efectos térmicos.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** **Transferencia.** ¿Por qué se instalan dos rastreadores con ejes ópticos separados 90°?

<details><summary>Solución comentada</summary>

Porque el balanceo de uno lo cubre el error transversal del otro: juntos dan precisión pareja en los tres ejes.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** **Transferencia.** ¿Qué ocurre con el rastreador cuando el Sol o la Tierra entran en su campo?

<details><summary>Solución comentada</summary>

Se deslumbra y no entrega actitud; el sistema pasa a giroscopio y otros sensores (C10) hasta recuperarlo.
</details>

**Ejercicio 12 · integrador.** **Integrador.** **Integrador.** Elabora tu *curva de error de actitud frente al número de estrellas*: la tabla de 8.3, el cociente balanceo/transversal y la lista de consultado y sintético.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4, 12 y la salida del laboratorio.
</details>

## 17. Laboratorio: actitud por estrellas sintéticas

El script [rastreador_estelar.py](rastreador_estelar.py) sortea una actitud y `N` estrellas dentro del campo, las proyecta con ruido de centroide de `0,1 px`, estima la actitud con SVD y separa el error transversal del de balanceo en 1500 pruebas por valor de `N` (**comprueba** acuerdo con la teoría dentro del 10 % para `N ≥ 10`, razón controlada para `N < 10` y balanceo `> 5×` el transversal). Usa la biblioteca común [adcs_comun.py](../adcs_comun.py) del bloque.

**Datos:** estrellas y actitudes **sintéticas** de semilla 20260517; sin catálogo real. **Predice antes de ejecutar:** ¿Cuántas veces mayor será el error de balanceo que el transversal con 20 estrellas? (unas 14.) **Ejecución del 2026-11-10 (Python 3.12.9, numpy 2.4.4):**

```text
Python 3.12.9 | numpy 2.4.4
B87-C07 rastreador estelar | estrellas SINTETICAS, sensor 1024x1024 px, campo 15 deg, ruido de centroide 0.1 px (semilla 20260517)
focal = 3889.0 px ; IFOV = 53.04 arcsec/px ; ruido de centroide = 5.30 arcsec por eje
N estrellas | transversal sim [arcsec] | teoria | balanceo sim [arcsec] | teoria
          3 |                     3.72 |   3.06 |                 61.96 |  40.70
          5 |                     2.53 |   2.37 |                 38.26 |  31.52
         10 |                     1.70 |   1.68 |                 23.89 |  22.29
         20 |                     1.20 |   1.19 |                 16.31 |  15.76
         40 |                     0.83 |   0.84 |                 11.48 |  11.14
Pruebas superadas.
```

```bash
python programa/clases/B87/B87-C07-rastreadores-estelares/rastreador_estelar.py
```

**Límites:** estrellas sin magnitud ni identificación, sin distorsión óptica, ruido uniforme, campo cuadrado idealizado; el catálogo real y el emparejamiento no se tratan.

## 18. Errores frecuentes y cómo corregirlos

**Dar un solo número de precisión para los tres ejes.** Separa transversal y balanceo (8.4)

**Creer que más campo siempre mejora todo.** Revisa el efecto sobre `σ_a` y `ρ_rms` (ejercicio 6)

**Extrapolar la teoría a `N` pequeño.** Usa la simulación (8.4)

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué cociente balanceo/transversal esperabas? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **curva de error de actitud del rastreador estelar frente al número de estrellas** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Explica el método y su dominio | Explica los límites y las alternativas |
| Cálculo | Sin unidades | Con errores | Resultados con unidades y comprobados | Resuelve casos nuevos |
| Numérico | Sin comprobar | Un caso | Verifica con una segunda vía en varios casos | Interpreta las diferencias y los fallos |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo sintético y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular los datos como sintéticos; verificar cada resultado con una segunda vía; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y los datos son sintéticos; ningún resultado describe una misión real ni sustituye el diseño y la verificación de un subsistema de actitud con herramientas validadas, ensayos y revisión de especialistas.  Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Con `0,1 px` de ruido y 20 estrellas, el error es `1,20″` transversal y `16″` de balanceo; ambos bajan como `1/√N`. Queda una pregunta: ¿cómo se corrigen los errores sistemáticos de los sensores?

**Glosario español–inglés.** rastreador estelar · *star tracker*; centroide · *centroid*; catálogo · *catalog*; modelo estenopeico · *pinhole model*; balanceo · *roll*; IFOV · *instantaneous field of view*.

**Continuidad.** [B87-C08](../B87-C08-calibracion-de-sensores/CLASE.md) trata la calibración de sensores: sesgo y escala del magnetómetro y sesgo del giroscopio.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B87-C06 — Giroscopios MEMS](../B87-C06-giroscopios-mems/CLASE.md) · [📚 Bloque B87](../../../tronco-comun/B87-sensores-y-control-de-actitud.md) · [Siguiente: B87-C08 — Calibración de sensores →](../B87-C08-calibracion-de-sensores/CLASE.md)
<!-- /nav -->
