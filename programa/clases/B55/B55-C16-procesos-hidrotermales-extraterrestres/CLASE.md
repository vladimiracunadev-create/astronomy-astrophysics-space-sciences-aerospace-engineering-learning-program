# B55-C16 — Procesos hidrotermales extraterrestres

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B55](../../../tronco-comun/B55-astroquimica-y-geoquimica-extraterrestre.md) · [← Anterior: B55-C15 — Química de océanos internos](../B55-C15-quimica-de-oceanos-internos/CLASE.md) · [Siguiente: B55-C17 — Compuestos prebióticos →](../B55-C17-compuestos-prebioticos/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 16 del bloque B55, nivel N3. Calculas con estequiometría cuánto **hidrógeno** puede producir la **serpentinización** de una roca **sintética** rica en olivino y cuánta energía química ofrece ese H₂ a una reacción de metanogénesis, con una energía libre estándar **ilustrativa**. Usas [B55-C12](../B55-C12-geoquimica-de-meteoritos/CLASE.md) para las masas molares y [B55-C15](../B55-C15-quimica-de-oceanos-internos/CLASE.md) para el contexto de un océano.

## 2. Por qué esta clase existe

Donde el agua líquida toca roca rica en hierro puede liberarse H₂, una fuente de energía química. Para saber si importa hay que contar cuánto se produce y si la reacción posterior es favorable a la concentración presente. La decisión central: **¿cuánto H₂ produce una roca dada y a partir de qué concentración la metanogénesis libera energía?**

## 3. Lo que podrás hacer al terminar

1. Comprobar el balance de átomos de la reacción de serpentinización.
2. Calcular el H₂ por kilogramo de fayalita y de una roca de olivino.
3. Ver cómo cambian el H₂ con la fracción de olivino y con el hierro.
4. Calcular `ΔG = ΔG° + RT ln Q` de la metanogénesis.
5. Hallar el H₂ de equilibrio.
6. Situar las lecturas hidrotermales de Encelado como contexto.

La evidencia es la **balance de H₂ de una roca sintética** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es un balance de átomos?
2. ¿Qué es un mol?
3. ¿Qué es una energía libre de reacción?
4. ¿Qué es un cociente de reacción `Q`?
5. ¿Qué es un valor ilustrativo?

<details>
<summary>Ver respuestas</summary>

1. Que cada elemento aparezca igual a ambos lados. 2. Una cantidad con `N_A` entidades. 3. `ΔG`: negativa significa que la reacción es espontánea. 4. Productos sobre reactivos con sus exponentes. 5. Un valor propuesto para el ejemplo, no medido.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Una roca **sintética** con 40 % de olivino de composición Fo90 en masa, donde el hierro(II) reacciona y 2/3 pasa a hierro(III) en magnetita. Es el **ejemplo conductor**. Waite et al. (2017) (S1) y Hsu et al. (2015) (S2), con resúmenes truncados, interpretan el hidrógeno molecular detectado por Cassini y las partículas de sílice del penacho de Encelado como evidencia de procesos hidrotermales; son contexto, no aportan cifras al modelo. La energía libre estándar de la metanogénesis (−130 kJ/mol) es ilustrativa.

## 6. Vocabulario

La **serpentinización** es la reacción del olivino con agua; la parte que oxida Fe(II) libera H₂: `3 Fe₂SiO₄ + 2 H₂O → 2 Fe₃O₄ + 3 SiO₂ + 2 H₂`. La **metanogénesis** `CO₂ + 4 H₂ → CH₄ + 2 H₂O` puede liberar energía si hay suficiente H₂. El **cociente de reacción** es `Q = a(CH₄)/(a(CO₂) a(H₂)⁴)`. `Fo90` significa 90 % de forsterita en moles.

## 7. Modelo mental: una batería química

La roca es una batería: el hierro(II) la carga y, al oxidarse con agua, entrega H₂. Que esa carga sirva de energía depende de qué tan alta sea la concentración de H₂ frente al umbral de equilibrio.

```mermaid
flowchart LR
    OL["olivino Fo90"] --> FE["Fe(II)"]
    FE --> H2["H₂ = ½ por Fe oxidado"]
    H2 --> Q["Q = a(CH₄)/(a(CO₂) a(H₂)⁴)"]
    Q --> DG["ΔG = ΔG° + RT ln Q"]
    DG --> EQ["H₂ de equilibrio (ΔG = 0)"]
```

*Descripción textual:* el olivino aporta Fe(II); al oxidarse produce H₂; el H₂ entra en `Q` y fija el signo de `ΔG` y el umbral de equilibrio.

Analogía: una batería que se descarga al reaccionar con agua. Límite: la cantidad real depende de la temperatura, la presión, la cinética y otras fases (por ejemplo magnetita y serpentina) que el modelo no trata.

## 8. La explicación, paso a paso

### 8.1 Balance de átomos

Fe 6 = 6, Si 3 = 3, O 14 = 14, H 4 = 4: la reacción está balanceada.

### 8.2 H₂ por kilogramo de fayalita

Con `M(Fe₂SiO₄) = 203,773 g/mol` hay 4,907 mol/kg; por la estequiometría salen `2/3` mol de H₂ por mol de fayalita: **3,2716 mol/kg = 6,595 g/kg**. El segundo camino (Fe oxidado × ½) coincide a 1e-12.

### 8.3 Una roca con olivino Fo90

`M(olivino Fo90) = 147,001 g/mol`; 400 g de olivino por kg de roca dan 0,5442 mol de Fe(II); con 2/3 oxidado, **0,1814 mol/kg = 0,366 g/kg de H₂**.

### 8.4 Sensibilidad (H₂ máximo, mol/kg)

| fracción de olivino | Fo95 | Fo90 | Fo80 |
|---|---|---|---|
| 0,2 | 0,0463 | 0,0907 | 0,1739 |
| 0,4 | 0,0927 | 0,1814 | 0,3479 |
| 0,6 | 0,1390 | 0,2721 | 0,5218 |

Más hierro (Fo bajo) y más olivino dan más H₂.

### 8.5 Energía de la metanogénesis

Con `ΔG° = −130 kJ/mol` (ilustrativo), `T = 300 K`, `a(CO₂) = 10⁻³` y `a(CH₄) = 10⁻⁴` mol/kg:

| `a(H₂)` (mol/kg) | `ΔG` (kJ/mol) |
|---|---|
| 10⁻⁸ | +48,05 |
| 10⁻⁶ | +2,10 |
| 10⁻⁴ | −43,85 |
| 10⁻³ | −66,82 |
| 10⁻² | −89,80 |

`ΔG = 0` cuando `a(H₂) = 1,234 × 10⁻⁶ mol/kg`. Por encima de ese umbral la reacción libera energía.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `M` | masa molar | g mol⁻¹ | 203,773 (Fe₂SiO₄) |
| `n(H₂)` | H₂ producido | mol kg⁻¹ | 0,1814 (roca sintética) |
| `ΔG°` | energía libre estándar | kJ mol⁻¹ | −130 (ilustrativa) |
| `R` | constante de los gases | J mol⁻¹ K⁻¹ | 8,314462618… |
| `a` | actividad (≈ concentración) | mol kg⁻¹ | 10⁻³ (CO₂) |

## 10. Convenciones y referencias

Sistema de referencia: sistema cerrado a `T = 300 K` con actividades iguales a concentraciones. Pesos atómicos del NIST consultados el 2026-11-09 (puntos medios de los intervalos de Mg y Si). Roca y `ΔG°` sintéticos/ilustrativos. `R = k_B N_A` exacto en el SI 2019. Versiones: Python 3.12.9, biblioteca estándar. Tolerancias: balance de átomos exacto; H₂ por dos caminos 1e-12.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | Waite et al., «Cassini finds molecular hydrogen in the Enceladus plume: Evidence for hydrothermal processes», *Science* 356, 155 (2017) | PMID 28408597; doi:10.1126/science.aai8703 | contexto: H₂ molecular en el penacho de Encelado (resumen truncado) | Consultada el 2026-11-09; resumen truncado (sin cifras) |
| S2 | Hsu et al., «Ongoing hydrothermal activities within Enceladus», *Nature* 519, 207 (2015) | PMID 25762281; doi:10.1038/nature14262 | contexto: sílice nanométrica y sales en granos del penacho (resumen truncado) | Consultada el 2026-11-09; resumen truncado |
| S3 | NIST, *Atomic Weights and Isotopic Compositions for All Elements* | https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl | pesos atómicos de Mg, Si, Fe y masas isotópicas de H y O | Consultada el 2026-11-09; consultada (tabla de isótopos seleccionados) |
| — | Sin fuente externa para el resto | — | relaciones y valores que verifica el laboratorio con una segunda vía de cálculo; los parámetros de modelo se rotulan ilustrativos | No se consultó una fuente para esta parte |

Límites: no se consultaron valores termodinámicos publicados; los resúmenes truncados no dan cifras; el modelo no se compara con Encelado.

## 12. Cómo ver el H₂ y el umbral energético

| Magnitud | Valor |
|---|---|
| H₂ (roca sintética) | 0,1814 mol/kg |
| umbral `a(H₂)` | 1,234 × 10⁻⁶ mol/kg |
| `ΔG` a 10⁻³ | −66,8 kJ/mol |

Descripción larga: `ΔG` decae linealmente con el logaritmo de `a(H₂)` y cruza cero en 1,2 × 10⁻⁶.

## 13. Ejemplo trabajado: H₂ de una roca

**Paso 1 · Olivino.** 400 g/147,001 = 2,721 mol.

**Paso 2 · Fe(II).** `2 × 0,10 × 2,721 = 0,5442 mol`.

**Paso 3 · H₂.** `0,5442 × (2/3) × 0,5 = 0,1814 mol` (0,366 g).

## 14. Distintas formas de estimar la energía disponible

**Estequiometría:** da la cantidad máxima. **Termodinámica:** dice si la reacción siguiente es favorable. **Cinética:** dice si ocurre en el tiempo disponible, lo que aquí no se trata. Las tres deben considerarse juntas.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula los moles de fayalita en 100 g (sección 8.2).

<details><summary>Solución comentada</summary>

`100/203,773 = 0,4907 mol`.
</details>

**Ejercicio 2 · con una pista.** Calcula el H₂ producido en moles (sección 8.2). *Pista:* `× 2/3`.

<details><summary>Solución comentada</summary>

`0,3271 mol`.
</details>

**Ejercicio 3 · casi autónomo.** Calcula su masa en g (sección 8.2). *Casi autónomo.*

<details><summary>Solución comentada</summary>

`0,3271 × 2,01588 = 0,659 g`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** ¿Cuánto H₂ da una roca con 20 % de olivino Fo90? (sección 8.4).

<details><summary>Solución comentada</summary>

0,0907 mol/kg.
</details>

**Ejercicio 5 · autónomo.** ¿Qué pasa si se oxida solo 1/3 del Fe(II)? (sección 8.3).

<details><summary>Solución comentada</summary>

El H₂ se reduce a la mitad: 0,0907 mol/kg.
</details>

**Ejercicio 6 · autónomo.** Calcula `ΔG` a `a(H₂) = 10⁻⁵` (sección 8.5).

<details><summary>Solución comentada</summary>

Interpolando por `ln`: `ΔG ≈ −20,8 kJ/mol`.
</details>

**Ejercicio 7 · autónomo.** ¿Qué pasa con el umbral si `a(CH₄)` sube a 10⁻³? (sección 8.5).

<details><summary>Solución comentada</summary>

El umbral sube por `10^(1/4) = 1,78`: `2,19 × 10⁻⁶`.
</details>

**Ejercicio 8 · autónomo.** ¿Por qué la fayalita rinde más H₂ por kg que el olivino Fo90? (sección 8.4).

<details><summary>Solución comentada</summary>

Porque tiene más hierro por unidad de masa.
</details>

**Ejercicio 9 · transferencia.** Un océano con `a(H₂) = 10⁻⁸` ¿puede sostener la metanogénesis modelada? (sección 8.5).

<details><summary>Solución comentada</summary>

No: `ΔG = +48 kJ/mol`, desfavorable, en este modelo.
</details>

**Ejercicio 10 · transferencia.** ¿Qué informa el H₂ detectado en un penacho sobre la roca del fondo? (secciones 8.2–8.4).

<details><summary>Solución comentada</summary>

Que pudo haber Fe(II) reaccionando, pero no basta para cuantificar la roca; falta T, pH, tasas.
</details>

**Ejercicio 11 · transferencia.** ¿Qué faltaría para afirmar que hay metanogénesis? (sección 21).

<details><summary>Solución comentada</summary>

Mediciones de CH₄, CO₂, T, pH y cinética; el balance energético solo dice que sería posible.
</details>

**Ejercicio 12 · integrador.** Elabora tu *balance de H₂ de una roca sintética*: balance de átomos, H₂ por kg de roca, la tabla de sensibilidad y el umbral de equilibrio de la metanogénesis.

<details><summary>Solución modelo</summary>

Debe mostrar 8.1–8.5 con unidades, la nota de que roca y `ΔG°` son sintéticos/ilustrativos y que el resultado no prueba procesos en un cuerpo real.
</details>

## 17. Laboratorio: H₂ de serpentinización y energía de metanogénesis

El script [serpentinizacion.py](serpentinizacion.py) comprueba el balance de átomos, calcula el H₂ por dos caminos y el `ΔG` de la metanogénesis, y **comprueba** que el balance es exacto y que `ΔG` es monótono en `a(H₂)`.

**Datos:** pesos atómicos del NIST (S3); roca y `ΔG°` **sintéticos**. **Predice antes de ejecutar:** ¿cuánto H₂ da la roca sintética? (≈ 0,18 mol/kg.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
A. Balance de atomos de 3 Fe2SiO4 + 2 H2O -> 2 Fe3O4 + 3 SiO2 + 2 H2
elemento   reactivos   productos
      Fe           6           6
      Si           3           3
       O          14          14
       H           4           4
B. Masas molares [g/mol]: Fe2SiO4 203.773 ; Mg2SiO4 140.693 ; H2 2.01588
C. H2 por kg de fayalita pura: 3.2716 mol = 6.595 g (segundo camino 3.2716 mol)
D. Roca SINTETICA (40 % olivino Fo90): masa molar del olivino = 147.001 g/mol ; Fe(II) = 0.5442 mol/kg ; H2 maximo = 0.1814 mol/kg = 0.366 g/kg
E. H2 maximo por kg de roca segun la fraccion de olivino y el contenido de Fe (SINTETICO)
fraccion olivino   Fo#   H2 [mol/kg]
            0.2    95      0.0463
            0.2    90      0.0907
            0.2    80      0.1739
            0.4    95      0.0927
            0.4    90      0.1814
            0.4    80      0.3479
            0.6    95      0.1390
            0.6    90      0.2721
            0.6    80      0.5218
F. Energia libre de CO2 + 4 H2 -> CH4 + 2 H2O (DeltaG0 = -130 kJ/mol ILUSTRATIVO, T = 300 K, actividades en mol/kg)
a(H2) [mol/kg]   DeltaG [kJ/mol]
       1e-08         48.046
       1e-06          2.099
       1e-04        -43.849
       1e-03        -66.822
       1e-02        -89.796
G. H2 de equilibrio (DeltaG = 0) con CO2 = 1e-3 y CH4 = 1e-4 mol/kg: a(H2) = 1.234e-06 mol/kg
Pruebas superadas.
```

```bash
python programa/clases/B55/B55-C16-procesos-hidrotermales-extraterrestres/serpentinizacion.py
```

**Límites:** sistema cerrado; sin cinética ni pH; actividades ≈ concentraciones.

## 18. Errores frecuentes y cómo corregirlos

**Confundir moles de fayalita con moles de Fe.** Hay 2 Fe por fayalita (8.2).

**Olvidar que no todo el Fe(II) se oxida.** Se usa 2/3 (8.3).

**Usar `ΔG°` como `ΔG`.** Depende de `Q` (8.5).

**Afirmar metanogénesis a partir de un `ΔG` negativo.** Es solo posibilidad termodinámica.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué H₂ esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **balance de H₂ de una roca sintética** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Distingue estequiometría y termodinámica | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas con unidades | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con el caso analítico | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo sintético e ilustrativo |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular roca y `ΔG°` como sintéticos/ilustrativos; no afirmar actividad biológica ni hidrotermal en un cuerpo real; citar solo lo consultado.

## 21. Ética, seguridad y límites

Una energía disponible no es evidencia de vida; las discusiones astrobiológicas exigen evidencia múltiple y prudencia. Clase educativa: los modelos son simplificados y ningún resultado de esta clase es una observación. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

La roca sintética produce 0,18 mol/kg de H₂ y la metanogénesis modelada libera energía por encima de `1,2 × 10⁻⁶ mol/kg` de H₂. Queda una pregunta: ¿sobrevive la química orgánica a la radiación en el tiempo geológico?

**Glosario español–inglés.** serpentinización · *serpentinization*; metanogénesis · *methanogenesis*; energía libre · *free energy*; hidrotermal · *hydrothermal*; cociente de reacción · *reaction quotient*.

**Continuidad.** [B55-C17](../B55-C17-compuestos-prebioticos/CLASE.md) estudia los compuestos prebióticos y su supervivencia a la radiólisis.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B55-C15 — Química de océanos internos](../B55-C15-quimica-de-oceanos-internos/CLASE.md) · [📚 Bloque B55](../../../tronco-comun/B55-astroquimica-y-geoquimica-extraterrestre.md) · [Siguiente: B55-C17 — Compuestos prebióticos →](../B55-C17-compuestos-prebioticos/CLASE.md)
<!-- /nav -->
