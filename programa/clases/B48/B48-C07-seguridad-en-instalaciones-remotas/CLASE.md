# B48-C07 — Seguridad en instalaciones remotas

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B48](../../../tronco-comun/B48-operaciones-de-observatorios-cientificos.md) · [← Anterior: B48-C06 — Meteorología de observatorios](../B48-C06-meteorologia-de-observatorios/CLASE.md) · [Siguiente: B48-C08 — Automatización de cúpulas →](../B48-C08-automatizacion-de-cupulas/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 7 del bloque B48. Nivel N3. Una instalación remota debe sobrevivir a cortes sin que nadie esté presente. Aquí calculas la autonomía de un respaldo de energía y la probabilidad de que un corte la supere. Usas [B12](../../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md). Es un ejercicio de probabilidad, no una norma de seguridad eléctrica.

## 2. Por qué esta clase existe

Un respaldo mal dimensionado deja la cúpula abierta con lluvia. La decisión central: **¿qué autonomía cubre la mayoría de los cortes?**

## 3. Lo que podrás hacer al terminar

1. Calcular la energía útil de un banco de baterías.
2. Obtener la autonomía con una carga dada.
3. Calcular la probabilidad de un corte más largo con la exponencial.
4. Obtener los cortes largos esperados por año con Poisson.
5. Dimensionar para cubrir el 95 % de los cortes.
6. Reconocer lo que el modelo no cubre.

La evidencia es la **ficha de seguridad en instalaciones remotas** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es una incertidumbre?
2. ¿Qué es una simulación Monte Carlo?
3. ¿Qué es una tabla de resultados?
4. ¿Qué es un valor ilustrativo?
5. ¿Qué es una verificación?

<details>
<summary>Ver respuestas</summary>

1. Un intervalo en que se espera el valor verdadero. 2. Repetir con números aleatorios de semilla fija. 3. Un resumen ordenado de cálculos. 4. Un valor propuesto para el ejemplo, no medido. 5. Comparar un cálculo con un caso independiente.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Un banco de 12 V y 100 Ah, con 50 % de descarga permitida y rendimiento 0,9, entrega 540,0 Wh; con 150 W dura 3,60 h. Con cortes de media 2,0 h, la probabilidad de superar la autonomía es 0,1653. Es el **ejemplo conductor** (ilustrativo).

## 6. Vocabulario

**Autonomía**: tiempo que el respaldo sostiene la carga. **Profundidad de descarga** (DoD): fracción usable de la batería. **Distribución exponencial**: duración sin memoria. **Proceso de Poisson**: llegada aleatoria de cortes. **Carga crítica**: lo que no puede apagarse.

## 7. Modelo mental: un depósito de agua

El respaldo es un depósito: dura según su volumen útil y el consumo, y los cortes largos son las sequías que lo vacían.

```mermaid
flowchart LR
    B["V Ah DoD eta"] --> E["Energía útil"]
    E --> A["Autonomía = E/P"]
    A --> Q["P(corte > t) = exp(-t/mu)"]
    Q --> Y["Cortes largos por año"]
```

*Descripción textual:* la energía útil entre la carga da la autonomía; la exponencial da la probabilidad de superarla y Poisson da cuántos cortes largos ocurren por año.

Analogía: un depósito de agua. Límite: carga constante, batería nueva y cortes independientes.

## 8. La explicación, paso a paso

### 8.1 Autonomía y cortes

| Magnitud | Valor |
|---|---|
| Energía útil | 540,0 Wh |
| Autonomía | 3,60 h |
| P(corte > autonomía), analítica | 0,1653 |
| P(corte > autonomía), simulada | 0,1658 (sigma 0,0008) |
| Cortes largos por año, esperados | 0,992 |
| Cortes largos por año, simulados | 0,989 |
| P(al menos uno en el año), analítica | 0,6291 |
| P(al menos uno en el año), simulada | 0,6260 |

### 8.2 Dimensionar para el 95 %

Para cubrir el 95 % de los cortes se necesitan `−2,0 ln 0,05 = 5,99` h, o sea 166 Ah con la misma carga.

### 8.3 Lectura

En cerca de dos de cada tres años habrá un corte que supere la autonomía de 3,6 h: el respaldo solo compra tiempo para un **apagado ordenado**, no para seguir observando. Un procedimiento de cierre automático es parte del diseño. El modelo omite envejecimiento, temperatura y fallas del propio respaldo.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `E` | energía útil | Wh | 540,0 |
| `P` | carga crítica | W | 150 |
| `t_a` | autonomía | h | 3,60 |
| `μ` | duración media del corte | h | 2,0 |
| `λ` | cortes por año | 1/año | 6 |

## 10. Convenciones y referencias

Unidades del SI salvo donde se indique; coma decimal en el texto y punto decimal en las salidas del laboratorio; semilla 20261109; todo valor que no esté citado en la sección 11 es ilustrativo o sintético.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| — | Sin fuente externa | — | relaciones estándar que verifica el laboratorio | No se consultó una fuente para esta clase |

Límites: no se consultó ninguna fuente externa para esta clase; los valores son ilustrativos o sintéticos y las relaciones son de libro, verificadas solo por el laboratorio.

## 12. Cómo ver los resultados

| Autonomía (h) | P(corte mayor) |
|---|---|
| 1,0 | 0,6065 |
| 3,60 | 0,1653 |
| 5,99 | 0,0500 |

Descripción larga: la probabilidad de un corte más largo cae exponencialmente con la autonomía.

## 13. Ejemplo trabajado: la autonomía

**Paso 1.** Energía: `12 × 100 × 0,5 × 0,9 = 540` Wh.

**Paso 2.** Autonomía: `540/150 = 3,6` h.

**Paso 3.** `P = e^(−3,6/2) = e^(−1,8) = 0,1653`.

**Paso 4.** Cortes largos por año: `6 × 0,1653 = 0,992`.

## 14. Distintas formas de describir el resultado

**Por fórmula:** sección 8. **Por tabla:** sección 12. **Por código:** `respaldo_energia.py`. **Por contraste:** el laboratorio compara dos vías independientes.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Energía útil de 12 V, 100 Ah, DoD 0,5, η 0,9. *Pasos:* producto.

<details><summary>Solución comentada</summary>

`540` Wh.
</details>

**Ejercicio 2 · con una pista.** Autonomía con una carga de 90 W. *Pista:* `540/90`.

<details><summary>Solución comentada</summary>

`6` h.
</details>

**Ejercicio 3 · casi autónomo.** Probabilidad de un corte mayor que 6 h con media 2 h.

<details><summary>Solución comentada</summary>

`e^−3 = 0,0498`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Cortes largos esperados al año con la autonomía base.

<details><summary>Solución comentada</summary>

`0,992`.
</details>

**Ejercicio 5.** P(ninguno en el año).

<details><summary>Solución comentada</summary>

`1 − 0,6291 = 0,3709`.
</details>

**Ejercicio 6.** Autonomía para cubrir el 95 %.

<details><summary>Solución comentada</summary>

`5,99` h.
</details>

**Ejercicio 7.** Ah necesarios para eso.

<details><summary>Solución comentada</summary>

`166` Ah.
</details>

**Ejercicio 8.** Diferencia simulada − analítica de la probabilidad.

<details><summary>Solución comentada</summary>

`0,0005`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** ¿Por qué no usar el 100 % de la batería?

<details><summary>Solución comentada</summary>

La descarga profunda acorta su vida; por eso se fija un DoD.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Basta un respaldo para la seguridad de las personas?

<details><summary>Solución comentada</summary>

No: la seguridad de las personas exige procedimientos y normas que este curso no da.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Y si los cortes duran más cuando hay tormenta?

<details><summary>Solución comentada</summary>

La exponencial subestima las colas: se necesita otra distribución.
</details>

**Ejercicio 12.** **Integrador.** Elabora tu *ficha de seguridad en instalaciones remotas*: autonomía, probabilidades y apagado ordenado.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.3.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de seguridad en instalaciones remotas*: autonomía, probabilidades y apagado ordenado.

<details><summary>Solución modelo</summary>

Secciones 8.1–8.3.
</details>

## 17. Laboratorio: respaldo y cortes

El script [respaldo_energia.py](respaldo_energia.py) calcula la autonomía y compara la probabilidad analítica con la simulada (**comprueba** a 4 sigmas).

**Datos:** baterías, carga y cortes **ilustrativos**. **Predice antes de ejecutar:** ¿cuánto dura el respaldo? (3,6 h.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Energía útil = 540.0 Wh; autonomía = 3.60 h
P(corte > autonomía): analítica 0.1653 | simulada 0.1658 (sigma 0.0008)
Cortes largos por año: esperados 0.992 | simulados 0.989
P(al menos uno en el año): analítica 0.6291 | simulada 0.6260
Para cubrir el 95 % de los cortes: 5.99 h, o sea 166 Ah
Pruebas superadas.
```

```bash
python programa/clases/B48/B48-C07-seguridad-en-instalaciones-remotas/respaldo_energia.py
```

**Límites:** el modelo es de libro y sus parámetros son ilustrativos; no describe ningún observatorio ni instrumento real.

## 18. Errores frecuentes y cómo corregirlos

**Usar la energía nominal en vez de la útil.** Se corrige con 8.1.

**Creer que el respaldo permite seguir observando.** Se corrige con 8.3.

**Tratar este ejercicio como norma eléctrica.** Se corrige con la sección 21.

**Olvidar que los cortes son aleatorios.** Se corrige con 8.1.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de seguridad en instalaciones remotas** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | conceptos de la clase | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con el análisis | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | fuentes con fecha | Declara lo ilustrativo |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular lo ilustrativo y lo sintético; no presentar el modelo como práctica de un observatorio real; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Con 3,6 h de autonomía, un corte la supera con probabilidad 0,165. Queda una pregunta: ¿cómo se automatiza la protección de la cúpula?

**Glosario español–inglés.** autonomía · *runtime*; respaldo · *backup power*; corte · *outage*; carga · *load*; apagado ordenado · *graceful shutdown*.

**Continuidad.** [B48-C08](../B48-C08-automatizacion-de-cupulas/CLASE.md) estudia la automatización de cúpulas.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B48-C06 — Meteorología de observatorios](../B48-C06-meteorologia-de-observatorios/CLASE.md) · [📚 Bloque B48](../../../tronco-comun/B48-operaciones-de-observatorios-cientificos.md) · [Siguiente: B48-C08 — Automatización de cúpulas →](../B48-C08-automatizacion-de-cupulas/CLASE.md)
<!-- /nav -->
