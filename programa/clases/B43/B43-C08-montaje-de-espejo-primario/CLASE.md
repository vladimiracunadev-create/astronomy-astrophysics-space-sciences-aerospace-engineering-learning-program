# B43-C08 — Montaje de espejo primario

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B43](../../../tronco-comun/B43-construccion-y-mecanica-de-telescopios.md) · [← Anterior: B43-C07 — Aluminizado y recubrimientos](../B43-C07-aluminizado-y-recubrimientos/CLASE.md) · [Siguiente: B43-C09 — Celdas y soporte de espejos →](../B43-C09-celdas-y-soporte-de-espejos/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 8 del bloque B43. Nivel N3. El espejo primario se apoya en un anillo o en puntos y se deforma bajo su peso. Lo que importa para la imagen es la flexión que queda después de refocalizar. Aquí resuelves un disco axisimétrico con el método de Ritz y buscas el radio de apoyo que minimiza el error residual, con un espejo ilustrativo. Usas [B05](../../../tronco-comun/B05-fisica-fundamental-para-el-espacio.md), [B10](../../../tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md) y [B11](../../../tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md).

## 2. Por qué esta clase existe

Un apoyo mal elegido deja un error de forma que ninguna pieza posterior corrige. La decisión central: **¿en qué radio conviene apoyar el espejo para que, tras quitar piston y desenfoque, quede el menor error?**

## 3. Lo que podrás hacer al terminar

1. Plantear la energía de una placa axisimétrica.
2. Resolver con una base polinómica y un multiplicador de Lagrange.
3. Verificar con la solución cerrada del apoyo en el borde.
4. Quitar piston y desenfoque por mínimos cuadrados.
5. Buscar el radio de apoyo óptimo.
6. Interpretar el resultado con cautela.

La evidencia es la **ficha del apoyo del primario** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es un multiplicador de Lagrange?
2. ¿Qué es el método de Ritz?
3. ¿Qué es el piston?
4. ¿Qué es el desenfoque?
5. ¿Qué es un sistema lineal?

<details>
<summary>Ver respuestas</summary>

1. Una variable que impone una restricción al minimizar. 2. Minimizar la energía en una base de funciones prefijadas. 3. Un desplazamiento uniforme de toda la superficie. 4. Un término cuadrático `r²` que se corrige moviendo el foco. 5. Un conjunto de ecuaciones lineales `A x = b`.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Disco ilustrativo de borosilicato (`a = 100 mm`, `t = 33,3 mm`). Con apoyo en el borde, la flecha centro-borde es `0,067708` en unidades de `q a⁴/D_f` (cerrada: `0,067708`). El radio de apoyo que minimiza el RMS residual es `b/a = 0,5775`, con `0,101 nm` RMS frente a `0,419 nm` con apoyo en el borde. Es el **ejemplo conductor**.

## 6. Vocabulario

El **anillo de apoyo** de radio `b`. La **energía de Kirchhoff** de la placa. La **base polinómica** `w = Σ c_k ρ^(2k)`. El **sistema KKT** impone `w(b) = 0`. El **error residual** es lo que queda tras quitar `1` y `ρ²`. Las unidades son `q a⁴/D_f`.

## 7. Modelo mental: una tabla sostenida por un aro

Como una mesa de vidrio sobre un aro: si el aro está en el borde el centro cuelga; si se acerca al centro cuelga el borde; en medio las dos flechas se compensan y la forma se aplana.

```mermaid
flowchart LR
    E["energía de Kirchhoff"] --> B["base polinómica"]
    B --> K["KKT con w(b)=0"]
    K --> W["w(ρ)"]
    W --> F["quitar piston y desenfoque"]
    F --> R["RMS residual"]
    R --> O["b/a óptimo"]
```

*Descripción textual:* el apoyo fija el desplazamiento; al quitar piston y desenfoque el residuo depende del radio del anillo.

Analogía: una tabla sostenida por un aro. Límite: axisimétrico, Kirchhoff, apoyo sin fricción.

## 8. La explicación, paso a paso

### 8.1 Verificación

Para `b = a` el método de Ritz con 10 términos da `w(0) − w(a) = 0,0677083` y la solución cerrada `(5+ν)/(1+ν)/64 = 0,0677083`.

### 8.2 Barrido del radio de apoyo

Escala `q a⁴/D_f = 359,898 nm`.

| b/a | RMS residual (nm) | PV (nm) |
|---|---|---|
| 0,300 | 1,0304 | 3,6597 |
| 0,375 | 0,7270 | 2,3455 |
| 0,450 | 0,4342 | 1,4883 |
| 0,525 | 0,1855 | 0,7323 |
| 0,600 | 0,1192 | 0,5863 |
| 0,675 | 0,2472 | 0,9947 |
| 0,750 | 0,3454 | 1,2464 |
| 0,825 | 0,3978 | 1,3688 |
| 0,900 | 0,4164 | 1,4010 |
| 0,975 | 0,4191 | 1,4063 |

### 8.3 Óptimo

El mínimo del barrido está en `b/a = 0,5775` con `0,1009 nm` RMS y `0,4624 nm` PV; con apoyo en el borde el RMS es `0,4191 nm`. La mejora es de un factor `4,15`. Para un disco grueso de `t/a = 1/3` la teoría de Kirchhoff es solo cualitativa.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `b/a` | radio relativo del apoyo | — | 0,577 (óptimo) |
| `q a⁴/D_f` | escala de flecha | nm | 359,90 |
| `ν` | coeficiente de Poisson | — | 0,20 (ilustrativo) |
| `g` | gravedad estándar | m/s² | 9,80665 (NIST) |

## 10. Convenciones y referencias

Unidades del SI; coma decimal en el texto y punto decimal en las salidas del laboratorio; los ángulos están en radianes salvo que se indique y las longitudes de onda en nanómetros. Los telescopios y materiales de los ejemplos son ilustrativos.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NIST, *Fundamental Physical Constants* (CODATA 2022) | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | constantes citadas en la sección 9 | Consultada el 2026-11-09 |
| S2 | Propiedades del borosilicato | — | E, ρ y ν del disco | Ilustrativas, NO consultadas en una hoja de fabricante |

Límites: El método de Ritz se verifica contra la solución cerrada de C03, pero el óptimo es de una placa delgada idealizada y no sustituye a un modelo de elementos finitos.

## 12. Cómo ver el barrido

| b/a | RMS residual (nm) |
|---|---|
| 0,300 | 1,030 |
| 0,375 | 0,727 |
| 0,450 | 0,434 |
| 0,525 | 0,185 |
| 0,600 | 0,119 |
| 0,675 | 0,247 |
| 0,750 | 0,345 |
| 0,825 | 0,398 |
| 0,900 | 0,416 |
| 0,975 | 0,419 |

Descripción larga: el RMS baja hasta un mínimo cerca de b/a = 0,58 y vuelve a subir.

## 13. Ejemplo trabajado: el apoyo en el borde

**Paso 1 · Base.** `w = Σ c_k ρ^(2k)`, `k = 0…9`.

**Paso 2 · KKT.** Se resuelve el sistema con `w(1) = 0`.

**Paso 3 · Centro-borde.** `0,067708` frente a `0,067708`.

## 14. Distintas formas de describir el apoyo

**En palabras:** hay un aro que equilibra la flecha. **En fórmulas:** minimizar la energía con `w(b) = 0`. **En tabla:** barrido. **En código:** `apoyo_axial.py`.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** `(5+ν)/(1+ν)/64` con `ν = 0,2`.

<details><summary>Solución comentada</summary>

`0,067708`.
</details>

**Ejercicio 2 · con una pista.** Escala `q a⁴/D_f`.

<details><summary>Solución comentada</summary>

`359,90 nm`.
</details>

**Ejercicio 3 · casi autónomo.** Flecha centro-borde en nm (apoyo en el borde).

<details><summary>Solución comentada</summary>

`24,368 nm`, que coincide con C03.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** RMS residual con apoyo en el borde.

<details><summary>Solución comentada</summary>

`0,419 nm`.
</details>

**Ejercicio 5.** RMS en el óptimo.

<details><summary>Solución comentada</summary>

`0,101 nm`.
</details>

**Ejercicio 6.** Mejora (factor).

<details><summary>Solución comentada</summary>

`4,15`.
</details>

**Ejercicio 7.** Valor de `b` óptimo en mm.

<details><summary>Solución comentada</summary>

`57,7 mm`.
</details>

**Ejercicio 8.** RMS con `b/a = 0,3`.

<details><summary>Solución comentada</summary>

`1,030 nm`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** ¿Por qué se quita el desenfoque?

<details><summary>Solución comentada</summary>

Porque se corrige enfocando; solo importa lo que no se compensa.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Por qué un anillo no basta en un espejo grande?

<details><summary>Solución comentada</summary>

Porque la flecha crece con `a⁴`; se usan muchos puntos o apoyos activos.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿El óptimo de este modelo vale para un espejo real?

<details><summary>Solución comentada</summary>

No: es una idealización de placa delgada.
</details>

**Ejercicio 12.** **Integrador.** Elabora tu *ficha del apoyo del primario*: verificación, barrido y óptimo.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.3.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha del apoyo del primario*: verificación, barrido y óptimo.

<details><summary>Solución modelo</summary>

Secciones 8.1–8.3.
</details>

## 17. Laboratorio: Ritz con restricción

El script [apoyo_axial.py](apoyo_axial.py) resuelve la placa axisimétrica con Ritz y KKT y barre el radio de apoyo (**comprueba** `1e-5` frente a la solución cerrada).

**Datos:** `g` de NIST; disco **ilustrativo**. **Predice antes de ejecutar:** ¿dónde está el óptimo? (≈ 0,58 a.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
centro_borde_ritz = 0.0677083
centro_borde_cerrado = 0.0677083
escala_nm = 359.898
beta_opt = 0.5775
rms_opt_nm = 0.100948
pv_opt_nm = 0.462367
rms_borde_nm = 0.419131
b/a | RMS residual (nm) | PV (nm)
0.300 | 1.0304 | 3.6597
0.375 | 0.7270 | 2.3455
0.450 | 0.4342 | 1.4883
0.525 | 0.1855 | 0.7323
0.600 | 0.1192 | 0.5863
0.675 | 0.2472 | 0.9947
0.750 | 0.3454 | 1.2464
0.825 | 0.3978 | 1.3688
0.900 | 0.4164 | 1.4010
0.975 | 0.4191 | 1.4063
Pruebas superadas.
```

```bash
python programa/clases/B43/B43-C08-montaje-de-espejo-primario/apoyo_axial.py
```

**Límites:** Kirchhoff, axisimétrico, apoyo ideal.

## 18. Errores frecuentes y cómo corregirlos

**Olvidar la restricción `w(b) = 0`.** Se corrige con 8.1.

**No quitar piston y desenfoque.** Se corrige con 8.2.

**Usar el óptimo de este modelo en un espejo real.** Se corrige con los límites.

**Mezclar `b` y `a`.** Se corrige con la sección 9.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha del apoyo del primario** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | conceptos de la clase | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con el análisis | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | fuentes con fecha | Declara lo ilustrativo |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular el disco como ilustrativo; verificar con la solución cerrada; no presentar el óptimo como diseño.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

El apoyo en un anillo de `b/a = 0,58` reduce el residuo a `0,10 nm` RMS. Queda una pregunta: ¿cómo se reparte la carga en la celda?

**Glosario español–inglés.** anillo de apoyo · *support ring*; método de Ritz · *Ritz method*; multiplicador de Lagrange · *Lagrange multiplier*; desenfoque · *defocus*; residuo · *residual*.

**Continuidad.** [B43-C09](../B43-C09-celdas-y-soporte-de-espejos/CLASE.md) estudia las celdas y soportes de espejos.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B43-C07 — Aluminizado y recubrimientos](../B43-C07-aluminizado-y-recubrimientos/CLASE.md) · [📚 Bloque B43](../../../tronco-comun/B43-construccion-y-mecanica-de-telescopios.md) · [Siguiente: B43-C09 — Celdas y soporte de espejos →](../B43-C09-celdas-y-soporte-de-espejos/CLASE.md)
<!-- /nav -->
