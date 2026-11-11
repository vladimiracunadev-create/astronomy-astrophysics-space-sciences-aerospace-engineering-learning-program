# B104-C15 — Entrenamiento subacuático como analogía

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B104](../../../tronco-comun/B104-astronautica-y-preparacion-de-astronautas.md) · [← Anterior: B104-C14 — Supervivencia en entorno terrestre](../B104-C14-supervivencia-en-entorno-terrestre/CLASE.md) · [Siguiente: B104-C16 — Manejo de conflictos →](../B104-C16-manejo-de-conflictos/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 15 del bloque B104, nivel N3. El entrenamiento subacuático ajusta la flotabilidad de la persona y el traje para que no floten ni se hundan y así ensayar movimientos, tareas y herramientas. Es una **analogía**, no una réplica de la ingravidez. Aquí calculas el lastre de flotabilidad neutra, la masa añadida y el arrastre que el agua impone, y ves qué se parece al espacio y qué no. Sigue a B104-C14 y prepara a B104-C19. Cuerpo y coeficientes **ilustrativos**; dimensiones del tanque de NASA **consultadas**. No es una guía de buceo.

## 2. Por qué esta clase existe

El agua anula el peso neto, pero también se opone al movimiento. La decisión central: **¿qué aspectos de una tarea espacial se pueden entrenar bien en el agua y cuáles quedan distorsionados por la inercia y el arrastre del fluido?**

## 3. Lo que podrás hacer al terminar

1. Calcular el lastre necesario para flotabilidad neutra.
2. Calcular la presión absoluta a una profundidad dada.
3. Estimar la masa añadida y su efecto sobre la aceleración.
4. Simular un empuje en el vacío y en el agua con arrastre cuadrático.
5. Comprobar la coherencia de las dimensiones consultadas del tanque con su volumen.
6. Explicar los límites de la analogía y rotular que no es una guía de buceo.

La evidencia es la **ficha de analogía con límites** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué dice el principio de Arquímedes?
2. ¿Qué es la presión hidrostática?
3. ¿Qué es el arrastre cuadrático?
4. ¿Qué es la masa añadida?
5. ¿Qué es un modelo ilustrativo?

<details>
<summary>Ver respuestas</summary>

1. El empuje es el peso del fluido desplazado. 2. `ρ g h`. 3. Una fuerza de resistencia proporcional al cuadrado de la velocidad. 4. La inercia extra por el fluido que hay que acelerar con el cuerpo. 5. Uno con parámetros inventados.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

La página de NASA sobre el Neutral Buoyancy Laboratory (consultada el 2026-11-10) da un tanque de 61,5 m × 31,1 m × 12,2 m (202 × 102 × 40 ft) con 6,2 millones de galones de agua dulce clorada a 28,9–30 °C, en el Sonny Carter Training Facility del Johnson Space Center, usado para entrenar caminatas espaciales; la flotabilidad se ajusta para simular gravedad total o parcial. Sus dimensiones dan 23 334 m³ y los 6,2 millones de galones, 23 470 m³ (0,58 % de diferencia). En el fondo la presión absoluta es de 220,5 kPa (2,18 atm). Un cuerpo ilustrativo de 150 kg y 0,152 m³ necesita 1,36 kg de lastre; un empuje de 50 N durante 1 s lo lleva a 2,50 m en 8 s en el vacío y a 0,90 m en el agua. Es el **ejemplo conductor**.

## 6. Vocabulario

La **flotabilidad neutra** ocurre cuando el empuje iguala al peso. El **lastre** es la masa que se añade o quita para lograrla. La **masa añadida** `m_a` es la inercia del fluido arrastrado. El **arrastre** es la fuerza `½ ρ C_d A v²`. La **presión absoluta** suma la atmosférica y la hidrostática.

## 7. Modelo mental

```mermaid
flowchart LR
    M["masa 150 kg<br/>volumen 0,152 m³"] --> E["empuje = ρ V g"]
    E --> L["lastre = ρV − m"]
    L --> N["flotabilidad neutra"]
    N --> D["en el agua: masa añadida<br/>+ arrastre cuadrático"]
    D --> C["movimiento distinto al del vacío"]
```

*Descripción textual:* del volumen y la masa se obtiene el lastre que da flotabilidad neutra; en el agua, la masa añadida y el arrastre hacen que el movimiento difiera del que habría en el vacío.

Analogía: empujar a un amigo en una piscina: no pesa, pero tampoco se desliza como en el aire; el agua lo frena. Límite: en el espacio no hay agua que frene ni fluido que acompañe el movimiento.

## 8. La explicación, paso a paso

### 8.1 Lo consultado y su coherencia

De NASA: dimensiones 61,5 × 31,1 × 12,2 m, 6,2 millones de galones, agua dulce clorada a 28,9–30 °C, propósito: planificar, desarrollar procedimientos, comprobar hardware y ensayar tareas de caminatas con flotabilidad ajustada para simular gravedad total o parcial. El laboratorio comprueba que las dimensiones y los galones concuerdan (0,58 %).

### 8.2 Presión y lastre

A 12,2 m: `p = 101 325 + 995,8 · 9,80665 · 12,2 = 220,5 kPa = 2,18 atm` (densidad típica no consultada). Un cuerpo de 150 kg y 0,152 m³ desplaza `995,8 · 0,152 = 151,36 kg`: hace falta añadir `1,36 kg` de lastre para empuje igual al peso.

### 8.3 Masa añadida

Para una esfera, `m_a = ½ ρ V = 75,7 kg`: la masa efectiva es 225,7 kg y la aceleración inicial con 50 N, 0,222 m/s² frente a 0,333 m/s² en el vacío (cociente 0,66). El valor depende de la forma; para un cuerpo humano con traje es mayor y direccional.

### 8.4 Vacío frente a agua

Con 50 N durante 1 s y arrastre cuadrático (`C_d A = 0,6 m²`), tras 8 s: vacío `x = 2,50 m`, `v = 0,333 m/s` (sigue moviéndose); agua `x = 0,90 m`, `v = 0,070 m/s` (casi se detuvo). En el espacio, el movimiento continúa hasta que algo lo frena; en el agua, se detiene solo.

### 8.5 Qué reproduce y qué no

Reproduce la ausencia de peso neto y permite ensayar acceso, secuencias, herramientas y comunicación. No reproduce la ausencia de arrastre, la inercia sin fluido, el vacío ni la temperatura. Un traje se adapta con lastre y no se usa un traje de vuelo sin presión. El buceo tiene sus propios riesgos que esta clase no trata.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `ρ` | densidad del agua | kg/m³ | 995,8 (no consultada) |
| `V` | volumen del cuerpo | m³ | 0,152 (ilustrativo) |
| lastre | masa a añadir | kg | 1,36 |
| `m_a` | masa añadida | kg | 75,7 (esfera) |
| `F` | empuje | N | 50 durante 1 s |
| `p` | presión absoluta a 12,2 m | kPa | 220,5 |

## 10. Convenciones y referencias

Agua dulce a unos 29 °C, `g = 9,80665 m/s²`; movimiento unidimensional con integración de paso 1 ms; arrastre `½ρ C_d A v|v|` con `C_d A = 0,6 m²`. Sin aleatoriedad. Tolerancias: dimensiones frente a galones < 1 %; velocidad en vacío igual a `F t/m` (< 1e-6); en agua, desplazamiento menor que la mitad del de vacío. Numpy 2.4.4, Python 3.12.9.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA, «Neutral Buoyancy Laboratory» — https://www.nasa.gov/johnson/neutral-buoyancy-laboratory/ (consultada 2026-11-10) | página completa | dimensiones 61,5 × 31,1 × 12,2 m; 6,2 millones de galones de agua dulce clorada a 28,9–30 °C; entrenamiento de caminatas; flotabilidad ajustada para simular gravedad total o parcial | Consultada |
| S2 | NASA History, SP-4225, «Training and Operations» — https://www.nasa.gov/history/SP-4225/training/training.htm (consultada 2026-11-10) | sección de simuladores | el centro de Star City tenía un tanque de agua de 5 000 m³ para entrenar caminatas espaciales | Consultada |
| — | Relaciones estándar usadas en el laboratorio | — | las verifica el laboratorio | No consultada en una fuente concreta (las verifica el laboratorio) |

Límites: de las páginas solo se toman las dimensiones, el volumen, la temperatura y el uso; la densidad del agua, la masa añadida de una esfera y el arrastre cuadrático son estándar no consultados; los coeficientes del cuerpo son ilustrativos.

## 12. Cómo ver el resultado

| medio | distancia en 8 s (m) | velocidad a 8 s (m/s) |
|---|---|---|
| vacío | 2,50 | 0,333 |
| agua | 0,90 | 0,070 |

Lastre para flotabilidad neutra: 1,36 kg; presión a 12,2 m: 220,5 kPa. Descripción larga: el agua frena el movimiento y reduce la distancia recorrida a un tercio.

## 13. Ejemplo trabajado: lastre de flotabilidad neutra

**Paso 1 · Masa desplazada.** `995,8 · 0,152 = 151,36 kg`.

**Paso 2 · Masa del cuerpo.** `150 kg`.

**Paso 3 · Lastre.** `151,36 − 150 = +1,36 kg` (añadir).

## 14. Distintas formas de describir el problema

**Por balance:** empuje igual a peso. **Por presión:** `p_atm + ρ g h`. **Por inercia:** `m + m_a`. **Por simulación:** vacío frente a agua.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula la presión absoluta a 12,2 m. *Pasos:* `101 325 + ρ g h`.

<details><summary>Solución comentada</summary>

`220,5 kPa`.
</details>

**Ejercicio 2 · con una pista.** Calcula el volumen del tanque con sus dimensiones.

<details><summary>Solución comentada</summary>

`61,5·31,1·12,2 = 23 334 m³`.
</details>

**Ejercicio 3 · casi autónomo.** Convierte 6,2 millones de galones a m³ y compara.

<details><summary>Solución comentada</summary>

`23 470 m³`; diferencia `0,58 %`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Calcula el lastre de un cuerpo de 148 kg y 0,152 m³.

<details><summary>Solución comentada</summary>

`151,36 − 148 = +3,36 kg`.
</details>

**Ejercicio 5 · autónomo.** Calcula la masa añadida de una esfera de 0,152 m³.

<details><summary>Solución comentada</summary>

`½ · 995,8 · 0,152 = 75,7 kg`.
</details>

**Ejercicio 6 · autónomo.** ¿Cuál es la aceleración inicial con 50 N en el vacío y en el agua?

<details><summary>Solución comentada</summary>

`0,333` y `0,222 m/s²`.
</details>

**Ejercicio 7 · autónomo.** ¿Qué distancia recorre el cuerpo en el vacío en 8 s si se empuja 1 s?

<details><summary>Solución comentada</summary>

`0,5·0,333·1 + 0,333·7 = 2,50 m`.
</details>

**Ejercicio 8 · autónomo.** ¿Por qué en el agua se detiene?

<details><summary>Solución comentada</summary>

Por el arrastre cuadrático, que no existe en el vacío.
</details>

**Ejercicio 9 · transferencia.** ¿Flota o se hunde una herramienta de 20 kg que desplaza 0,018 m³? ¿Qué haces?

<details><summary>Solución comentada</summary>

Desplaza `17,9 kg`: se hunde (+2,1 kg); se le añade flotador o se acepta una fuerza residual.
</details>

**Ejercicio 10 · transferencia.** ¿Qué parte de una tarea de acople no se puede entrenar bien en el agua?

<details><summary>Solución comentada</summary>

Los movimientos rápidos o de gran inercia, donde la masa añadida y el arrastre distorsionan, y los efectos térmicos y del vacío.
</details>

**Ejercicio 11 · transferencia.** Un compañero propone entrenar con el traje sin lastre «para ahorrar tiempo». ¿Qué objetas?

<details><summary>Solución comentada</summary>

Sin flotabilidad neutra el cuerpo cae o flota y no se ensaya la tarea; el lastre se determina con el traje real y por personal capacitado.
</details>

**Ejercicio 12 · integrador.** Elabora tu *ficha de analogía con límites*: lastre, presión, masa añadida, comparación vacío/agua, qué reproduce y qué no, y qué es consultado, estándar e ilustrativo.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.5 y la salida del laboratorio.
</details>

## 17. Laboratorio: flotabilidad neutra, masa añadida y arrastre

El script [flotabilidad.py](flotabilidad.py) comprueba las dimensiones del tanque, calcula presión y lastre y simula un empuje en el vacío y en el agua con masa añadida y arrastre (**comprueba** el volumen, la condición de flotabilidad neutra, la velocidad del vacío y que el agua frene el movimiento). Tarda menos de 1 s.

**Datos:** cuerpo y coeficientes **ilustrativos**; dimensiones del tanque de NASA **consultadas**. Sin aleatoriedad. **Predice antes de ejecutar:** ¿Cuántas veces menos se desplaza el cuerpo en el agua que en el vacío en 8 s? (Casi 3 veces menos.) **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9; numpy 2.4.4
MODELO ILUSTRATIVO: cuerpo de 150 kg y 0,152 m3; coeficientes inventados; tanque de NASA: 61,5 x 31,1 x 12,2 m (consultado)

Volumen por dimensiones: 23,334 m3; 6,2 millones de galones: 23,470 m3; diferencia 0.58 %
Presion absoluta en el fondo (12.2 m): 220.5 kPa = 2.18 atm

Masa desplazada 151.36 kg; masa del cuerpo 150.0 kg; lastre necesario +1.36 kg (+ = anadir, - = quitar)
Masa anadida (esfera, 0,5 rho V) = 75.7 kg; masa efectiva en agua = 225.7 kg

Tras 8 s (empuje de 50 N durante 1 s): vacio -> x = 2.50 m, v = 0.333 m/s; agua -> x = 0.90 m, v = 0.070 m/s
Velocidad en vacio teorica F t/m = 0.3333 m/s
Aceleracion inicial en agua = 0.222 m/s2 frente a 0.333 m/s2 en vacio (cociente 0.66)
Pruebas superadas.
```

```bash
python programa/clases/B104/B104-C15-entrenamiento-subacuatico-como-analogia/flotabilidad.py
```

**Límites:** una dimensión, esfera para la masa añadida, arrastre cuadrático simple, sin buceo ni térmica; no es una guía de buceo.

## 18. Errores frecuentes y cómo corregirlos

**Creer que el agua reproduce la ingravidez.** Reproduce la ausencia de peso neto, no del fluido (8.5).

**Olvidar la masa añadida.** Inclúyela (8.3).

**Dar el lastre «de memoria».** Calcula con el volumen (8.2).

**Usar la clase como guía de buceo.** No lo es (sección 21).

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué lastre esperabas y cuál da el laboratorio? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de analogía con límites** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Confunde los términos | Parciales | Explica flotabilidad neutra, masa añadida y arrastre | Explica qué reproduce y qué no la analogía |
| Cálculo | Sin unidades | Con errores | Calcula con unidades y compara con el laboratorio | Resuelve casos nuevos |
| Numérico | Sin comprobar | Un caso | Compara con una segunda vía de cálculo | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo sintético, lo ilustrativo y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular cuerpo y coeficientes como ilustrativos, no presentar el modelo como guía de buceo ni consejo operativo y citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: **no da consejo médico, de entrenamiento individual ni operativo** y no sustituye a los requisitos, procedimientos y estándares de ninguna agencia. **No** es una guía de buceo ni de entrenamiento subacuático: eso lo imparten profesionales con medidas de seguridad propias. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Con 1,36 kg de lastre el cuerpo ilustrativo queda en flotabilidad neutra, pero tras empujarlo 1 s recorre 0,90 m en el agua frente a 2,50 m en el vacío. Queda una pregunta: ¿qué ocurre al volver a casa?

**Glosario español–inglés.** flotabilidad neutra · *neutral buoyancy*; masa añadida · *added mass*; lastre · *ballast*; arrastre · *drag*; analogía · *analog*.

**Continuidad.** [B104-C16](../B104-C16-manejo-de-conflictos/CLASE.md) trata las operaciones de retorno y la desaceleración del reingreso.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B104-C14 — Supervivencia en entorno terrestre](../B104-C14-supervivencia-en-entorno-terrestre/CLASE.md) · [📚 Bloque B104](../../../tronco-comun/B104-astronautica-y-preparacion-de-astronautas.md) · [Siguiente: B104-C16 — Manejo de conflictos →](../B104-C16-manejo-de-conflictos/CLASE.md)
<!-- /nav -->
