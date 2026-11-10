# B101-C08 — Gemelo digital para ensayo de reparaciones robóticas

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B101](../../../tronco-comun/B101-manipuladores-roboticos-espaciales.md) · [← Anterior: B101-C07 — Control de fuerza e impedancia en manipulación](../B101-C07-control-de-fuerza-e-impedancia-en-manipulacion/CLASE.md) · [Siguiente: B101-C09 — Coordinación visual y cámaras en operaciones con manipulador →](../B101-C09-coordinacion-visual-y-camaras-en-operaciones-con-manipulador/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 8 del bloque B101. Nivel N3. Un **gemelo digital** es un modelo que se mantiene al día con datos del sistema real y se usa para ensayar antes de actuar. Aquí el gemelo es el brazo de B101-C01 con parámetros nominales; la «realidad» es el mismo brazo con errores **inventados**. Ensayas una inserción de precisión, recalibras el gemelo y calculas el margen de la maniobra. Todos los datos son **sintéticos** y ninguno procede de un sistema real.

## 2. Por qué esta clase existe

Una reparación robótica no se improvisa: se ensaya. Pero un ensayo vale solo si el gemelo se parece a la realidad. La decisión central: **¿cuánto se parece mi gemelo a la realidad y qué probabilidad de éxito tiene la maniobra con ese parecido?**

## 3. Lo que podrás hacer al terminar

1. Distinguir el modelo (gemelo) de la realidad y medir su discrepancia.
2. Planificar con el gemelo y ejecutar en la «realidad» sintética.
3. Recalibrar el gemelo con mediciones ruidosas (B101-C05) y comparar el error de la maniobra.
4. Estimar por Monte Carlo la probabilidad de éxito según la calidad del modelo.
5. Usar una prueba de control: un gemelo perfecto no debe fallar.
6. Separar lo consultado de lo sintético y no presentar el gemelo como una validación.

La evidencia es el **informe de ensayo en el gemelo digital** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es la calibración cinemática (B101-C05)?
2. ¿Qué es la cinemática inversa (B101-C02)?
3. ¿Qué es un residuo?
4. ¿Qué es una probabilidad estimada por Monte Carlo?
5. ¿Qué es una comprobación independiente?

<details>
<summary>Ver respuestas</summary>

1. Estimar los parámetros reales del brazo con mediciones. 2. De la pose deseada a los ángulos. 3. Medición menos predicción. 4. La fracción de ensayos aleatorios que cumple una condición. 5. Calcular lo mismo por otro camino y comparar.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa B101-C02 y B101-C05.

## 5. Un caso de contexto y casos de referencia

F1 informa de que el ERA «opera con una precisión de 5 mm» y que se puede preprogramar o controlar en tiempo real. F2 resume la evolución del manipulador de la estación a partir de la experiencia operacional. Ninguno de los dos describe un gemelo digital. En la clase, la tarea es llevar la herramienta a 40 posiciones objetivo con un error menor que **5 mm** (umbral **ilustrativo** de una inserción, no de ningún brazo).

## 6. Vocabulario

**Gemelo digital:** modelo actualizado con datos del sistema real. **Realidad sintética:** el «sistema» simulado con errores inventados. **Discrepancia:** diferencia entre el modelo y la realidad. **Recalibración:** actualizar los parámetros del gemelo. **Éxito de la maniobra:** error menor que el umbral. **Gemelo perfecto:** gemelo con los parámetros exactos (prueba de control).

## 7. Modelo mental: planificar en el gemelo, ejecutar en la realidad

```mermaid
flowchart LR
    G["Gemelo: parametros p_g"] --> P["Planifica q con IK"]
    P --> R["Realidad: parametros p_r"]
    R --> E["Error de posicion"]
    M["Mediciones de la realidad"] --> C["Recalibracion"]
    C --> G
```

*Descripción textual:* el gemelo calcula los ángulos; la realidad los ejecuta con otros parámetros; las mediciones de la realidad actualizan al gemelo.

Analogía: ensayar un viaje con el mapa de ayer: sirve si el mapa se actualiza. Límite: aquí la discrepancia es solo cinemática; en un caso real hay muchas otras.

## 8. La explicación, paso a paso

### 8.1 Qué se sabe de los sistemas reales

Solo F1 (5 mm, control en tiempo real o preprogramado) y F2 (experiencia operacional del manipulador de la estación). No se consultó ningún gemelo digital espacial ni procedimiento de reparación (N7). La clase es una ilustración de método.

### 8.2 Ensayo con tres gemelos

Se planifican 40 objetivos con cada gemelo y se ejecutan en la «realidad» (error de posición de la herramienta, en mm, y cuántos quedan dentro de 5 mm):

| gemelo | error mediano (mm) | error máximo (mm) | dentro de 5 mm |
|---|---|---|---|
| nominal | 35,980 | 53,154 | 1 de 40 |
| perfecto (control) | 0,000 | 0,000 | 40 de 40 |
| recalibrado (60 mediciones, ruido 0,2 mm) | 0,031 | 0,049 | 40 de 40 |

El residuo de modelo (RMS 3D en 40 poses) pasa de 36,227 mm (nominal) a 0,032 mm (recalibrado).

### 8.3 Margen frente al error del modelo

Con errores de parámetros aleatorios de distinta escala (300 ensayos por fila), la probabilidad de caer dentro de 5 mm con el gemelo **nominal** es:

| `σ` de ángulos (grados) | `σ` de longitudes (mm) | probabilidad |
|---|---|---|
| 0,05 | 0,2 | 0,997 |
| 0,10 | 0,5 | 0,833 |
| 0,25 | 1,0 | 0,223 |
| 0,50 | 2,0 | 0,037 |
| 1,00 | 4,0 | 0,003 |

Con un brazo de unos 1,9 m, un error de 0,1° en un solo ángulo mueve la punta `1,9 × 0,001745 = 3,3` mm: por eso el margen de 5 mm se agota con décimas de grado.

### 8.4 Qué demuestra y qué no

Que, **en el modelo sintético**, recalibrar devuelve el margen y que un gemelo exacto no falla. No demuestra nada sobre un brazo real: la «realidad» es el mismo modelo con otros parámetros, sin flexibilidad, holguras, contacto ni visión.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `p_g, p_r` | parámetros del gemelo y de la realidad | rad, m | 10 parámetros (B101-C05) |
| `e` | error de posición de la herramienta | mm | tabla 8.2 |
| umbral | éxito de la inserción | mm | 5 (ilustrativo) |
| `σ_a, σ_d` | error de ángulos y longitudes | grados, mm | tabla 8.3 |
| probabilidad | fracción de éxitos | — | tabla 8.3 |

## 10. Convenciones y referencias

Marcos y D-H como en B101-C01. La inversa usa solo la posición de la herramienta (orientación libre) con Newton amortiguado. Semilla 108. 40 objetivos alcanzables, 60 poses de calibración, ruido de 0,2 mm por eje. Todo dato —errores de la «realidad», ruido, objetivos, umbral— es **sintético**. Python 3.12.9, numpy 2.4.4.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| F1 | Airbus, comunicado «Airbus-built European Robotic Arm ready for Space», Leiden, 5-07-2021 — https://www.airbus.com/sites/g/files/jlcbta136/files/4b7e903e07e8e840d723ad3d1796c9c9_EN-Airbus-SpS-Press-Release-Airbus-built-European-Robotic-Arm-ready-for-Space.pdf (consultada 2026-11-10; texto extraído del PDF con PyMuPDF) | página 1 | el European Robotic Arm (ERA) mide 11,3 m, tiene siete articulaciones, mueve 3 000 kg de forma rutinaria y hasta 8 000 kg en modo lento y opera con una precisión de 5 mm; puede «caminar» de un punto base a otro | Consultada (comunicado de prensa del fabricante: no es una especificación técnica) |
| F2 | Razvi, S. y Burns, S. H. (NASA JSC), «Evolution of the Space Station Robotic Manipulator», NASA NTRS 20070010589, 2007 — https://ntrs.nasa.gov/citations/20070010589 (consultada 2026-11-10) | resumen extendido (solo el resumen) | el manipulador de la estación (Canadarm2) tiene un diseño de 7 grados de libertad, con base cambiable que le permite desplazarse a puntos base | Consultada (solo el resumen; no se consultaron longitud ni carga) |
| — | Textos de robótica (Denavit y Hartenberg, 1955; Craig; Siciliano et al.; Spong et al.) | — | las matrices D-H, el jacobiano, la pseudoinversa y los mínimos cuadrados son resultados estándar que verifica cada laboratorio | No consultada en una fuente concreta |
| — | Normas de ECSS, NASA o de la estación sobre operaciones de brazos, cámaras y seguridad | — | — | No consultada (solo títulos de ECSS en F3) |

Límites: ninguna fuente consultada describe un gemelo digital ni un criterio de aceptación de una reparación.

## 12. Cómo ver el gemelo

| Magnitud | Valor |
|---|---|
| error mediano nominal | 35,980 mm |
| error mediano recalibrado | 0,031 mm |
| éxito nominal frente a recalibrado | 1 de 40 frente a 40 de 40 |
| probabilidad con `σ_a = 0,5°` | 0,037 |

Descripción larga: el error con el modelo nominal es unas 7 veces el umbral; recalibrado, queda 160 veces por debajo.

## 13. Ejemplo trabajado: error de un ángulo

**Paso 1 · Dato.** Un error de `0,1°` en la articulación del hombro.

**Paso 2 · Radián.** `0,1° = 0,001745` rad.

**Paso 3 · Palanca.** Con el extremo a 1,9 m: `1,9 × 0,001745 = 3,3` mm.

**Paso 4 · Decisión.** Es el 66 % del umbral de 5 mm con un solo ángulo: el margen exige calibrar.

## 14. Distintas formas de usar un gemelo

**Ensayo previo (esta clase):** planificar y probar. **Seguimiento:** comparar en línea el modelo con las mediciones. **Predicción:** estimar cuánto margen queda tras un cambio. Cada uso exige que el modelo se haya validado contra datos reales.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** El gemelo nominal tiene un error mediano de 35,980 mm y el umbral es 5 mm. ¿Cuántas veces lo supera? *Pasos:* cociente.

<details><summary>Solución comentada</summary>

`35,980/5 = 7,2` veces.
</details>

**Ejercicio 2 · con una pista.** ¿Qué porcentaje de las 40 inserciones tuvo éxito con el gemelo nominal? *Pista:* 1 de 40.

<details><summary>Solución comentada</summary>

`1/40 = 2,5 %`.
</details>

**Ejercicio 3 · casi autónomo.** ¿Cuántas veces menor es el error mediano del gemelo recalibrado?

<details><summary>Solución comentada</summary>

`35,980/0,031 ≈ 1 160` veces.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** ¿Por qué el gemelo perfecto da error 0 y qué sirve esa prueba?

<details><summary>Solución comentada</summary>

Planifica con los parámetros exactos de la realidad; sirve para comprobar que el código de planificación y ejecución no introduce errores propios.
</details>

**Ejercicio 5 · autónomo.** Con el margen de 5 mm, ¿qué fila de la tabla 8.3 da una probabilidad de éxito mayor que 0,8?

<details><summary>Solución comentada</summary>

Las dos primeras (`σ_a = 0,05°` y `0,10°`: 0,997 y 0,833).
</details>

**Ejercicio 6 · autónomo.** Error en la punta de un ángulo erróneo de 0,3° a 1,9 m.

<details><summary>Solución comentada</summary>

`0,3° = 0,00524` rad; `1,9 × 0,00524 = 9,95` mm.
</details>

**Ejercicio 7 · autónomo.** ¿Entre qué filas de la tabla 8.3 la probabilidad pasa de 50 %?

<details><summary>Solución comentada</summary>

Entre la fila de 0,10° (0,833) y la de 0,25° (0,223).
</details>

**Ejercicio 8 · autónomo.** ¿Cuántas veces baja el residuo de modelo (RMS) tras recalibrar?

<details><summary>Solución comentada</summary>

`36,227/0,032 ≈ 1 130` veces.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Tras una colisión leve, ¿cuándo recalibrarías el gemelo?

<details><summary>Solución comentada</summary>

Cuando el residuo entre lo medido y lo predicho supere un umbral fijado de antemano (por ejemplo, la mitad del margen de la maniobra), y antes de ensayar de nuevo.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** El gemelo muestra 40 de 40. ¿Qué podría fallar aún en el sistema real?

<details><summary>Solución comentada</summary>

Flexibilidad, holguras, contacto, visión, retardos y fallas, que el modelo no incluye.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Basta este gemelo para aprobar una reparación?

<details><summary>Solución comentada</summary>

No: su «realidad» es sintética; un gemelo real necesita validarse contra datos de vuelo y de ensayo y aprobarse por quien tiene la autoridad.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *informe de ensayo en el gemelo digital*: los tres gemelos, el éxito de cada uno, la tabla de margen, el control del gemelo perfecto y qué es consultado, no consultado y sintético.

<details><summary>Solución comentada</summary>

Secciones 8.2–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: ensayo en un gemelo

El script [gemelo_digital.py](gemelo_digital.py) planifica 40 inserciones con tres gemelos (nominal, perfecto y recalibrado), las ejecuta en la «realidad» sintética y calcula la probabilidad de éxito frente a la calidad del modelo; **comprueba** que el gemelo nominal falla, que el perfecto no, que la recalibración devuelve el margen y que la probabilidad decrece. Usa [b101_comun.py](../b101_comun.py).

**Datos:** «realidad», ruido y objetivos **sintéticos**; sin constantes con fuente. **Predice antes de ejecutar:** ¿cuántas de las 40 inserciones acierta el gemelo perfecto? (40.) Ejecución del 2026-11-10 (Python 3.12.9, numpy 2.4.4):

```text
Python 3.12.9 | numpy 2.4.4
Datos SINTETICOS: realidad con errores inventados, ruido 0.2 mm, umbral de insercion de 5 mm (ilustrativo)
Gemelo nominal       : error mediano =  35.980 mm ; maximo =  53.154 mm ; dentro de 5 mm = 1/40
Gemelo perfecto      : error mediano =   0.000 mm ; maximo =   0.000 mm ; dentro de 5 mm = 40/40
Gemelo recalibrado   : error mediano =   0.031 mm ; maximo =   0.049 mm ; dentro de 5 mm = 40/40
Residuo de modelo (RMS 3D sobre 40 poses nuevas): nominal = 36.227 mm ; recalibrado = 0.032 mm
Margen frente al error cinematico: probabilidad de insercion dentro de 5 mm (300 ensayos por fila)
  sigma angulos [grados]  sigma d [mm]  probabilidad
                  0.05           0.2         0.997
                  0.10           0.5         0.833
                  0.25           1.0         0.223
                  0.50           2.0         0.037
                  1.00           4.0         0.003
Pruebas superadas.
```

```bash
python programa/clases/B101/B101-C08-gemelo-digital-para-ensayo-de-reparaciones-roboticas/gemelo_digital.py
```

**Límites:** solo posición; discrepancia solo cinemática; umbral ilustrativo; sin dinámica, contacto ni visión.

## 18. Errores frecuentes y cómo corregirlos

**Tomar el gemelo por la realidad.** Contrástalo con datos (8.4)

**Olvidar la prueba de control.** Un gemelo perfecto no debe fallar (8.2)

**Presentar el umbral de 5 mm como el de una reparación real.** Revisa la sección 5

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué diferencia hay entre el gemelo nominal y el recalibrado? Si dudas, repasa el ejercicio 3. Tras el laboratorio: ¿para qué sirve el gemelo perfecto? (ver sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **informe de ensayo en el gemelo digital** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Explica el método y su dominio | Explica los límites y las alternativas |
| Cálculo | Sin unidades | Con errores | Resultados con unidades y comprobados | Resuelve casos nuevos |
| Numérico | Sin comprobar | Un caso | Verifica con una comprobación independiente en varios casos | Interpreta las diferencias y los fallos |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo sintético y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular los datos como sintéticos; verificar cada resultado con una comprobación independiente; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: el gemelo de la clase se contrasta con una «realidad» inventada: no valida ninguna reparación real ni sustituye la validación contra datos de vuelo. No enseña a operar hardware real. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Con el modelo nominal solo 1 de 40 inserciones cae dentro de 5 mm; recalibrado, las 40. Queda una pregunta: en una operación real, ¿qué ve el operador que dirige el brazo?

**Glosario español–inglés.** gemelo digital · *digital twin*; recalibración · *recalibration*; discrepancia · *discrepancy*; inserción · *insertion*; margen · *margin*; probabilidad de éxito · *success probability*.

**Continuidad.** [B101-C09](../B101-C09-coordinacion-visual-y-camaras-en-operaciones-con-manipulador/CLASE.md) trata la coordinación visual y las cámaras.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B101-C07 — Control de fuerza e impedancia en manipulación](../B101-C07-control-de-fuerza-e-impedancia-en-manipulacion/CLASE.md) · [📚 Bloque B101](../../../tronco-comun/B101-manipuladores-roboticos-espaciales.md) · [Siguiente: B101-C09 — Coordinación visual y cámaras en operaciones con manipulador →](../B101-C09-coordinacion-visual-y-camaras-en-operaciones-con-manipulador/CLASE.md)
<!-- /nav -->
