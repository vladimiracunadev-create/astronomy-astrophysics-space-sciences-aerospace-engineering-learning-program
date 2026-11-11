# B105-C01 — Respuesta cardiovascular a microgravedad

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B105](../../../tronco-comun/B105-medicina-y-biologia-espacial.md) · [← Anterior: B104-C23 — Ejecución de experimentos a bordo: procedimientos y registro](../../../tronco-comun/B104-astronautica-y-preparacion-de-astronautas.md#b104-c23) · [Siguiente: B105-C02 — Pérdida de masa ósea →](../B105-C02-perdida-de-masa-osea/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 1 del bloque B105, primera del tramo de sistemas fisiológicos. Nivel N3. Aquí calculas cómo cambia la presión de una columna de sangre cuando desaparece (o se reduce) la gravedad efectiva y cómo un modelo mínimo de gasto cardíaco explica por qué un déficit de volumen empeora la tolerancia a estar de pie. La fisiología respiratoria, la visión y el ejercicio se retoman en [B105-C21](../B105-C21-fisiologia-respiratoria-en-microgravedad-y-atmosferas-de-cabina/CLASE.md), [B105-C05](../B105-C05-cambios-de-vision/CLASE.md) y [B105-C16](../B105-C16-contramedidas-de-ejercicio/CLASE.md).

## 2. Por qué esta clase existe

En la Tierra la gravedad empuja la sangre hacia los pies y el sistema cardiovascular lo compensa en cada postura. En microgravedad esa carga desaparece y el cuerpo se reajusta; al volver, la compensación puede no bastar. La decisión central: **¿cuánta presión de sangre hay en la cabeza de pie, y cuánto margen deja un déficit de volumen?**

## 3. Lo que podrás hacer al terminar

1. Calcular `ρ g h` en pascales y en mmHg para la cabeza y los pies en distintas gravedades.
2. Calcular gasto cardíaco `GC = FC·VS` y presión arterial media `PAM = GC·RVS` con unidades.
3. Explicar el desplazamiento de líquidos hacia la cabeza al desaparecer el gradiente hidrostático.
4. Simular una población sintética y estimar la fracción bajo un umbral didáctico de presión en la cabeza.
5. Distinguir un modelo didáctico de una medición y rotular qué es sintético.
6. Reconocer que nada de esto es consejo médico ni criterio de aptitud.

La evidencia es la **ficha de respuesta cardiovascular con presupuesto de presión** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es la presión hidrostática?
2. ¿Cuántos pascales tiene 1 mmHg?
3. ¿Qué es el gasto cardíaco?
4. ¿Qué es la microgravedad?
5. ¿Qué es un dato sintético?

<details>
<summary>Ver respuestas</summary>

1. La presión que ejerce una columna de fluido por su peso: `ρ g h`. 2. Unos 133,3 Pa. 3. El volumen de sangre que bombea el corazón por minuto (`FC·VS`). 4. Una condición de aceleración aparente casi nula, como en caída libre en órbita. 5. Un dato generado para el ejemplo, no medido.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Una población **sintética** de 2.000 personas con parámetros ilustrativos (semilla 105) se pone de pie con 0,40 L de sangre acumulados en las piernas. Sin déficit de volumen, la presión media en la cabeza es 73,2 mmHg y el 19,9 % queda por debajo del umbral didáctico de 60 mmHg; con un déficit de volumen de 20 %, la media baja a 60,0 mmHg y el 51,7 % queda bajo el umbral. Es el **ejemplo conductor**: todos los valores son **sintéticos** y el umbral es una elección de enseñanza; no describen a ninguna persona ni a ninguna tripulación.

## 6. Vocabulario

La **presión hidrostática** es `P = ρ g h`. El **gasto cardíaco** es `GC = FC·VS` (frecuencia por volumen sistólico). La **presión arterial media** es `PAM = GC·RVS` (resistencia vascular sistémica). La **intolerancia ortostática** es la dificultad para mantener la presión al ponerse de pie (descrita por la NASA como un efecto posvuelo, consultado el 2026-11-10). El **barorreflejo** ajusta frecuencia y resistencia según la presión. La **precarga** es el llenado del corazón antes de contraerse.

## 7. Modelo mental

```mermaid
flowchart LR
    G["g efectivo"] --> P["rho g h<br/>cabeza y pies"]
    P --> L["líquido hacia<br/>la cabeza en 0 g"]
    L --> V["volumen y precarga"]
    V --> S["VS, FC, RVS"]
    S --> A["PAM en la cabeza<br/>de pie"]
```

*Descripción textual:* la gravedad efectiva fija el gradiente hidrostático; sin él, el líquido se redistribuye hacia la cabeza y cambia el volumen y la precarga; con menos precarga cae el volumen sistólico, el barorreflejo compensa en parte y la presión media en la cabeza de pie queda más cerca del umbral.

Analogía: una manguera vertical llena de agua; con la manguera de pie el fondo soporta la columna, tumbada no. Límite: los vasos se contraen, tienen válvulas y el corazón se adapta; el modelo ignora todo eso salvo un barorreflejo simple.

## 8. La explicación, paso a paso

### 8.1 Gradiente hidrostático

Con `ρ = 1060 kg/m³` (sangre, valor de enseñanza) y `g = 9,81 m/s²`, a 0,35 m sobre el corazón: `ρ g h = 3.640 Pa = 27,3 mmHg`, que se **resta** a la presión media del corazón; a 1,30 m bajo el corazón (pies) se **suma**: 101,4 mmHg. En la Luna (1,62 m/s²) la cabeza baja 4,5 mmHg; en Marte (3,71), 10,3 mmHg; en caída libre, 0.

### 8.2 Qué cambia en microgravedad

Sin gradiente, el líquido que en la Tierra se acumula en las piernas se redistribuye hacia el tórax y la cabeza. La NASA describe que la función del corazón puede disminuir en vuelo y que al aterrizar puede haber dificultad para mantener la presión de pie, con mareo o desmayo (página «Human body in space», consultada el 2026-11-10).

### 8.3 Un modelo mínimo

`VS = VS₀ (V_ef/V₀)²` con `V_ef = V₀(1 − déficit) − acumulado en piernas`; el barorreflejo sube `FC` hasta +45 % y `RVS` hasta +30 % en proporción a la caída de `VS`; `PAM = FC·VS·RVS`. Con `FC₀ = 70`, `VS₀ = 0,075 L` y `RVS₀ = 18,5`: `GC = 5,25 L/min` y `PAM ≈ 97 mmHg`.

### 8.4 Resultado de la población sintética

| Escenario | `PAM` corazón (mmHg) | `PAM` cabeza (mmHg) | Fracción bajo 60 mmHg |
|---|---|---|---|
| Sin déficit | 100,5 ± 16,0 | 73,2 | 0,199 |
| Déficit 10 % | 99,2 ± 15,7 | 71,9 | 0,233 |
| Déficit 20 % | 87,3 ± 14,4 | 60,0 | 0,517 |

El déficit de volumen desplaza la distribución hacia abajo; la dispersión grande refleja la variación entre personas **sintéticas**.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `ρ` | densidad de la sangre | kg/m³ | 1060 (didáctico) |
| `g` | gravedad efectiva | m/s² | 9,81; 1,62; 3,71; 0 |
| `h` | altura sobre/bajo el corazón | m | 0,35 (cabeza); 1,30 (pies) |
| `P` | presión hidrostática | Pa o mmHg | 1 mmHg = 133,322 Pa |
| `GC` | gasto cardíaco | L/min | 5,25 (ejemplo) |
| `PAM` | presión arterial media | mmHg | ≈ 97 (ejemplo) |

## 10. Convenciones y referencias

Presiones manométricas en mmHg; alturas medidas desde el nivel del corazón (positivo hacia la cabeza). Referencia: tórax. Datos sintéticos con semilla 105 (numpy `default_rng`); parámetros y umbral de 60 mmHg **ilustrativos**. Tolerancias del laboratorio: `ρ g h` de la cabeza en la Tierra = 27,3 ± 0,2 mmHg; fracción bajo el umbral creciente con el déficit; fracción de referencia < 0,25. Numpy 2.4.4, Python 3.12.9.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| 1 | NASA, «Human body in space» (Human Research Program), resumen de la página por WebFetch | https://www.nasa.gov/hrp/bodyinspace/ (consultada el 2026-11-10) | declaración cualitativa: la función cardíaca puede disminuir en vuelo y puede haber intolerancia ortostática tras el aterrizaje | Consultada (resumen de la página; sin cifras) |
| — | Relaciones físicas y fisiológicas estándar: `ρ g h`, `GC = FC·VS`, `PAM = GC·RVS` | — | las verifica el laboratorio | No consultada en una fuente concreta (las verifica el laboratorio) |

Límites: la fuente de la NASA es cualitativa; los parámetros del modelo (volúmenes, ganancias del barorreflejo, umbral de 60 mmHg) son una elección didáctica y no se compararon con datos de tripulantes ni con literatura clínica.

## 12. Cómo ver el resultado

Descripción: la tabla de 8.4 y la salida del laboratorio muestran el gradiente por gravedad y la fracción bajo el umbral por escenario. Equivalente textual: más déficit de volumen, más personas sintéticas bajo el umbral.

## 13. Ejemplo trabajado: presión en la cabeza de pie

**Paso 1 · Gasto.** `GC = 70·0,075 = 5,25 L/min`.

**Paso 2 · PAM.** `5,25·18,5 = 97,1 mmHg`.

**Paso 3 · Gradiente.** `ρ g h = 1060·9,81·0,35 = 3.640 Pa = 27,3 mmHg`.

**Paso 4 · Cabeza.** `97,1 − 27,3 = 69,8 mmHg`, por encima del umbral didáctico de 60 mmHg.

## 14. Distintas formas de describir el problema

**Por columna:** `ρ g h`. **Por flujo:** `GC`. **Por presión:** `PAM`. **Por distribución:** fracción bajo el umbral. **Por gravedad:** Tierra, Marte, Luna y caída libre. **Por tabla:** el escenario y su fracción.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** ¿Cuántos mmHg de gradiente hay a 0,35 m del corazón en la Luna (1,62 m/s²)? *Pasos:* `ρ g h` en Pa y divide por 133,322.

<details><summary>Solución comentada</summary>

`1060·1,62·0,35 = 601 Pa → 4,5 mmHg`.
</details>

**Ejercicio 2 · con una pista.** ¿Qué presión hidrostática (mmHg) hay a 0,50 m en la Tierra? *Pista:* usa `ρ g h`.

<details><summary>Solución comentada</summary>

`1060·9,81·0,50 = 5.199 Pa = 39,0 mmHg`.
</details>

**Ejercicio 3 · casi autónomo.** Con `FC = 70`, `VS = 0,075 L` y `RVS = 18,5`, calcula `GC` y `PAM`, y la presión en la cabeza de pie.

<details><summary>Solución comentada</summary>

`GC = 5,25 L/min`, `PAM = 97,1 mmHg`, cabeza `69,8 mmHg`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Convierte 100 mmHg a kPa.

<details><summary>Solución comentada</summary>

`100·133,322 = 13.332 Pa = 13,3 kPa`.
</details>

**Ejercicio 5 · autónomo.** `VS` cae 15 % y `FC` sube 12 %. ¿Cómo cambia `GC`?

<details><summary>Solución comentada</summary>

`0,85·1,12 = 0,952`: baja 4,8 %.
</details>

**Ejercicio 6 · autónomo.** ¿Por qué la presión hidrostática de la cabeza es cero en caída libre pero el líquido sigue redistribuido?

<details><summary>Solución comentada</summary>

Sin peso aparente no hay gradiente; el líquido que estaba en las piernas se reparte según presiones locales y la membrana capilar, y no vuelve a acumularse en ellas.
</details>

**Ejercicio 7 · autónomo.** Si se acumulan 0,40 L en las piernas con `V₀ = 5 L`, ¿cuánto cae `VS` con el modelo `VS ∝ (V_ef/V₀)²`?

<details><summary>Solución comentada</summary>

`(0,92)² = 0,846`: cae 15,4 %.
</details>

**Ejercicio 8 · autónomo.** Con déficit 20 % y 0,40 L acumulados, ¿cuánto cae `VS`?

<details><summary>Solución comentada</summary>

`V_ef/V₀ = 0,8 − 0,08 = 0,72`; `0,72² = 0,518`: cae 48 %.
</details>

**Ejercicio 9 · transferencia.** Una centrífuga de brazo corto de 2 m gira a `ω` para dar 1 g (9,81 m/s²) en los pies. ¿Qué `ω` y qué aceleración hay en la cabeza, 0,35 m más cerca del eje (radio 1,65 m)?

<details><summary>Solución comentada</summary>

`ω = √(9,81/2) = 2,215 rad/s = 21,2 rpm`; en la cabeza `ω²·1,65 = 8,09 m/s² = 0,82 g`. *(Radios didácticos.)*
</details>

**Ejercicio 10 · transferencia.** El gradiente hidrostático en los pies de pie es 101 mmHg. ¿Por qué importa tras un vuelo largo?

<details><summary>Solución comentada</summary>

Porque es la presión que favorece la acumulación de sangre en las piernas al ponerse de pie, que el sistema debe compensar con menos volumen circulante.
</details>

**Ejercicio 11 · transferencia.** La fracción 0,199 de 2.000 personas tiene error estándar `√(p(1−p)/n)`. ¿Y con una tripulación de 4?

<details><summary>Solución comentada</summary>

`√(0,199·0,801/2000) = 0,009`; con `n = 4`, `√(0,199·0,801/4) = 0,20`: la estimación es casi inútil con 4 personas.
</details>

**Ejercicio 12 · integrador.** Elabora tu *ficha de respuesta cardiovascular con presupuesto de presión*: gradientes por gravedad, modelo de `GC`/`PAM`, escenarios, fracción bajo el umbral e incertidumbre, y lista de qué es sintético.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: presión hidrostática y tolerancia ortostática

El script [cardiovascular.py](cardiovascular.py) calcula el gradiente `ρ g h` en cuatro gravedades y simula 2.000 personas sintéticas de pie con tres déficits de volumen (**comprueba** el gradiente terrestre de la cabeza (27,3 mmHg), su valor nulo en 0 g, el crecimiento de la fracción con el déficit y la fracción de referencia < 0,25).

**Datos:** población **sintética** (semilla 105); parámetros y umbral **ilustrativos**. **Predice antes de ejecutar:** ¿Qué le pasa a la fracción bajo 60 mmHg al aumentar el déficit de volumen? (Crece.) **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9; numpy 2.4.4
DATOS SINTETICOS (semilla 105): 2000 personas con parametros ilustrativos; no son datos de tripulantes
Presion hidrostatica rho g h (rho = 1060 kg/m3):
  Tierra (g = 9.81)        cabeza - 27.3 mmHg; pies +101.4 mmHg
  Luna (g = 1.62)          cabeza -  4.5 mmHg; pies + 16.7 mmHg
  Marte (g = 3.71)         cabeza - 10.3 mmHg; pies + 38.3 mmHg
  Microgravedad (g = 0)    cabeza -  0.0 mmHg; pies +  0.0 mmHg
referencia (sin deficit)   PAM corazon 100.5 +- 16.0 mmHg; PAM cabeza  73.2 mmHg; fraccion bajo 60 mmHg = 0.199
deficit de volumen 10 %    PAM corazon  99.2 +- 15.7 mmHg; PAM cabeza  71.9 mmHg; fraccion bajo 60 mmHg = 0.233
deficit de volumen 20 %    PAM corazon  87.3 +- 14.4 mmHg; PAM cabeza  60.0 mmHg; fraccion bajo 60 mmHg = 0.517
Pruebas superadas.
```

```bash
python programa/clases/B105/B105-C01-respuesta-cardiovascular-a-microgravedad/cardiovascular.py
```

**Límites:** un solo barorreflejo lineal, sin controles de presión de largo plazo, sin gravedad parcial dinámica ni endotelio; no valida ni sustituye a ningún criterio clínico ni de aptitud; no se comparó con datos de tripulantes.

## 18. Errores frecuentes y cómo corregirlos

**Confundir presión manométrica con presión absoluta.** Aquí todo es manométrico respecto a la presión del corazón.

**Creer que sin gravedad no hay redistribución.** El gradiente desaparece, pero el líquido se redistribuye (8.2).

**Tomar el umbral de 60 mmHg como criterio clínico.** Es una elección didáctica; no es una referencia médica.

**Presentar la población sintética como datos de tripulantes.** Se rotula como sintética (sección 10).

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿puedes calcular `PAM` en la cabeza de pie? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de respuesta cardiovascular con presupuesto de presión** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Confunde las magnitudes | Parciales | Explica `ρ g h`, `GC` y `PAM` | Explica el barorreflejo y sus límites |
| Cálculo | Sin unidades | Con errores | Calcula con unidades y tolerancias | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Compara con la verdad del generador | Interpreta la sensibilidad |
| Fuentes | Sin fuente | Sin fecha | Cita solo lo consultado, con fecha | Rotula lo sintético y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular los datos como sintéticos; no presentar un resultado simulado como observado; no dar consejo médico ni operativo; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase **educativa**: no es consejo médico, no sustituye la formación, la licencia ni la supervisión de profesionales, y no contiene dosis, tratamientos ni procedimientos para aplicar a una persona real. Los umbrales y parámetros son ilustrativos; la valoración de la tolerancia ortostática de una persona real la hacen profesionales con datos clínicos. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Con una población sintética, el gradiente de 27,3 mmHg en la cabeza de pie y un déficit de volumen del 20 % llevan al 51,7 % bajo el umbral didáctico. Queda una pregunta: ¿qué le ocurre al hueso cuando desaparece la carga?

**Glosario español–inglés.** presión hidrostática · *hydrostatic pressure*; gasto cardíaco · *cardiac output*; intolerancia ortostática · *orthostatic intolerance*; barorreflejo · *baroreflex*.

**Continuidad.** [B105-C02](../B105-C02-perdida-de-masa-osea/CLASE.md) estudia la pérdida de masa ósea.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B104-C23 — Ejecución de experimentos a bordo: procedimientos y registro](../../../tronco-comun/B104-astronautica-y-preparacion-de-astronautas.md#b104-c23) · [📚 Bloque B105](../../../tronco-comun/B105-medicina-y-biologia-espacial.md) · [Siguiente: B105-C02 — Pérdida de masa ósea →](../B105-C02-perdida-de-masa-osea/CLASE.md)
<!-- /nav -->
