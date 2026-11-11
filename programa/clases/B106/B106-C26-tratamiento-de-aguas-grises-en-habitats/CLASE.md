# B106-C26 — Tratamiento de aguas grises en hábitats

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B106](../../../tronco-comun/B106-habitats-espaciales-y-soporte-vital.md) · [← Anterior: B106-C25 — Sensores de presión, gases y humedad para monitoreo de hábitat](../B106-C25-sensores-de-presion-gases-y-humedad-para-monitoreo-de-habitat/CLASE.md) · [Siguiente: B106-C27 — Tratamiento de orina y recuperación de agua →](../B106-C27-tratamiento-de-orina-y-recuperacion-de-agua/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 26 del bloque B106 (hábitats espaciales y soporte vital). Nivel N3. Primera de las cuatro clases de agua que siguen a C06: el tratamiento del agua de higiene (aguas grises) con un biorreactor, filtración y desinfección. Todo es un modelo mínimo con parámetros ilustrativos. Todos los datos del laboratorio son **sintéticos o ilustrativos** y se rotulan como tales; solo se tratan como consultados los valores de la sección 11 que dicen «Consultada».

## 2. Por qué esta clase existe

Las aguas grises son el mayor volumen del lazo y su carga orgánica hay que destruirla antes de potabilizar. La decisión central: **¿qué volumen de biorreactor y qué desinfección dan la remoción y la reducción de microorganismos requeridas?**

## 3. Lo que podrás hacer al terminar

1. Calcular el volumen de un biorreactor de mezcla completa para una remoción dada.
2. Comparar mezcla completa, flujo pistón y varios tanques en serie.
3. Verificar la formulación por integración numérica.
4. Calcular el producto concentración por tiempo de una desinfección de Chick–Watson.
5. Sumar reducciones logarítmicas de un tren de tratamiento.
6. Rotular que los parámetros son ilustrativos.

La evidencia es la **dimensionado de un tratamiento de aguas grises** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es la DBO?
2. ¿Qué es un tanque de mezcla completa?
3. ¿Qué es el tiempo de residencia?
4. ¿Qué es una reducción logarítmica?
5. ¿Qué es un oxidante residual?

<details>
<summary>Ver respuestas</summary>

1. La demanda bioquímica de oxígeno: una medida de la carga orgánica. 2. Uno cuyo contenido es uniforme e igual a su salida. 3. `τ = V/F`. 4. `log₁₀(N₀/N)`: 4 log es una reducción de 10 000 veces. 5. Un desinfectante que permanece disuelto en el agua.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Cuatro personas con 20 L/día de agua gris (80 L/día) y DBO de 300 mg/L, con `k = 0,5 h⁻¹` (ilustrativo): una remoción del 90 % exige en mezcla completa `τ = 18,0 h` y **60 L**; en flujo pistón, 4,6 h y 15 L; con 3 tanques, 6,9 h y 23 L. Para el 99 % la mezcla completa necesita 660 L y 3 tanques solo 73 L. Con 18 h totales, 1 tanque deja 30 mg/L y 3 tanques, 4,69 mg/L. Una desinfección de 4 log exige `CT = 8 mg·min/L`. La filtración multietapa y la verificación por conductividad son las de la página consultada de la NASA.

## 6. Vocabulario

**Aguas grises:** agua de higiene sin orina. **Biorreactor:** tanque con microorganismos que consumen materia orgánica. **Mezcla completa (CSTR):** tanque uniforme. **Flujo pistón (PFR):** flujo sin mezcla longitudinal. **Chick–Watson:** inactivación proporcional a `C·t`. **CT:** concentración por tiempo.

## 7. Modelo mental

```mermaid
flowchart LR
    G["aguas grises F, S0"] --> B["biorreactor tau"]
    B --> F["filtracion"]
    F --> D["desinfeccion CT"]
    D --> P["agua para el lazo (C06)"]
```

*Descripción textual:* las aguas grises pasan por un biorreactor que baja la carga orgánica, por filtros y por una desinfección antes de entrar al lazo de agua.

Analogía: lavar platos en una cuba (un tanque) o en una cadena de cubas (en serie): la cadena enjuaga mejor con el mismo volumen. Límite: la actividad biológica real depende de la temperatura, los nutrientes, el oxígeno y las toxinas.

## 8. La explicación, paso a paso

### 8.1 Mezcla completa

`S = S₀/(1 + k τ)`; para remoción `ρ`, `τ = ρ/((1 − ρ) k)`. Al 90 %: `18,0 h`; `V = F τ = 3,33·18 = 60 L`. La integración numérica del tanque da 30,000 mg/L, igual a la fórmula.

### 8.2 Flujo pistón y tanques en serie

Flujo pistón `S = S₀ e^{−kτ}`: al 90 %, `τ = ln 10/k = 4,6 h`, 15 L. `N` tanques en serie: `S = S₀/(1 + kτ/N)^N`; al 90 % con 3 tanques, `6,9 h` y 23 L. Con 18 h totales: 1 tanque 30 mg/L; 2, 9,9; 3, 4,69; 6, 1,23; 20, 0,178; flujo pistón 0,037. Dividir en etapas reduce mucho el volumen.

### 8.3 Desinfección

`log₁₀(N₀/N) = k C t` con `k = 0,5 L/(mg·min)`: 4 log requieren `C t = 8 mg·min/L`: 16 min a 0,5 mg/L, 8 a 1,0 y 4 a 2,0.

### 8.4 El tren

Un filtro de 99 % da 2 log; con 4 log de desinfección, 6 log en total. En el modelo los logaritmos se suman porque las etapas son independientes.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `S₀` | DBO de entrada | mg/L | 300 (ilustrativo) |
| `k` | constante de remoción | 1/h | 0,5 (ilustrativo) |
| `τ` | tiempo de residencia | h | 18,0 (90 %, mezcla completa) |
| `V` | volumen del biorreactor | L | 60 |
| CT | concentración por tiempo | mg·min/L | 8 (4 log) |

## 10. Convenciones y referencias

Caudal de 80 L/día (3,33 L/h); `S₀ = 300 mg/L`; `k = 0,5 h⁻¹`; Chick–Watson con `k = 0,5 L/(mg·min)`; filtro de 99 %. Todo ilustrativo. Tolerancias: remoción exacta de las fórmulas (1e-9); integración dentro de 1e-3 mg/L. Numpy y Python: ver la primera línea de la salida del laboratorio (Python 3.12.9, numpy 2.4.4 en la ejecución del 2026-11-10).

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA, «Environmental Control and Life Support Systems (ECLSS)» — https://www.nasa.gov/reference/environmental-control-and-life-support-systems-eclss/ (consultada 2026-11-10; la página indica actualización del 4 de abril de 2025) | párrafo de agua | el agua pasa por lechos de filtración de varias etapas y un oxidador catalítico, y sensores de conductividad eléctrica verifican su pureza; el agua fuera de norma se reprocesa | Consultada |
| — | Cinética de primer orden, CSTR/PFR, Chick–Watson | — | las verifica el laboratorio | No consultada en una fuente concreta |

Límites: no se consultó ningún dato de biorreactores ni de desinfectantes espaciales; los resúmenes OCHMO sobre agua **no se consultaron**. Todos los parámetros son ilustrativos.

## 12. Cómo ver el resultado

| Resultado | Valor |
|---|---|
| Volumen al 90 % (mezcla completa / pistón / 3 tanques) | 60 / 15 / 23 L |
| Volumen al 99 % (mezcla completa / 3 tanques) | 660 / 73 L |
| DBO con 18 h (1 / 3 tanques) | 30 / 4,69 mg/L |
| CT para 4 log | 8 mg·min/L |
| Reducción total del tren | 6,0 log |

Descripción larga: dividir el biorreactor en etapas reduce el volumen necesario; la desinfección se dimensiona con `C·t` y los logaritmos de las etapas se suman.

## 13. Ejemplo trabajado: volumen del biorreactor

**Paso 1.** `F = 80/24 = 3,33 L/h`.

**Paso 2.** `τ = 0,9/(0,1·0,5) = 18 h`.

**Paso 3.** `V = 3,33·18 = 60 L`.

**Paso 4.** Control: `S = 300/(1 + 0,5·18) = 30 mg/L = 10 %` de `S₀`.

## 14. Distintas formas de describir el problema

**Por fórmula:** `S₀/(1 + kτ)`. **Por volumen:** `F τ`. **Por etapas:** `N` tanques. **Por CT:** Chick–Watson. **Por logaritmos:** suma.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `τ` para remoción 80 % en mezcla completa. *Pasos:* `0,8/(0,2·0,5)`.

<details><summary>Solución comentada</summary>

`8 h`.
</details>

**Ejercicio 2 · con una pista.** Calcula `V` con `F = 3,33 L/h`. *Pista:* `F τ`.

<details><summary>Solución comentada</summary>

`26,7 L`.
</details>

**Ejercicio 3 · casi autónomo.** Calcula `S` con `τ = 6 h`. *Pista:* `300/(1 + 3)`.

<details><summary>Solución comentada</summary>

`75 mg/L`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** ¿Cuánto tarda en pistón para el 99 %?

<details><summary>Solución comentada</summary>

`ln 100/0,5 = 9,2 h`.
</details>

**Ejercicio 5 · autónomo.** ¿Y el volumen?

<details><summary>Solución comentada</summary>

`31 L`.
</details>

**Ejercicio 6 · autónomo.** ¿Qué `CT` da 3 log?

<details><summary>Solución comentada</summary>

`3/0,5 = 6 mg·min/L`.
</details>

**Ejercicio 7 · autónomo.** ¿Cuánta reducción da un filtro de 99,9 %?

<details><summary>Solución comentada</summary>

3 log.
</details>

**Ejercicio 8 · autónomo.** ¿Por qué conviene dividir en etapas?

<details><summary>Solución comentada</summary>

Porque la concentración cae en cada etapa y el volumen total baja.
</details>

**Ejercicio 9 · transferencia.** Se duplica la tripulación (160 L/día). ¿Cómo cambia el volumen?

<details><summary>Solución comentada</summary>

Se duplica a igual `τ` (120 L al 90 %).
</details>

**Ejercicio 10 · transferencia.** `k` baja a la mitad por el frío. ¿Qué pasa con `τ` y `V` al 90 %?

<details><summary>Solución comentada</summary>

Se duplican (36 h; 120 L).
</details>

**Ejercicio 11 · transferencia.** ¿Qué más debería medir un sistema real?

<details><summary>Solución comentada</summary>

Nitrógeno, tensioactivos, toxicidad y microbiología; el modelo solo considera la DBO.
</details>

**Ejercicio 12 · integrador.** Elabora tu *dimensionado de un tratamiento de aguas grises*: caudal y carga, tabla de volumen para tres remociones y tres configuraciones, efecto de dividir en etapas, CT de desinfección, reducción total y qué es ilustrativo.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: biorreactor y desinfección de aguas grises

El script [aguas_grises.py](aguas_grises.py) calcula el volumen y el tiempo de residencia de tres configuraciones, verifica el tanque por integración numérica y calcula el CT de desinfección (**comprueba** la fórmula contra la integración y el orden de las configuraciones).

**Datos:** parámetros **ilustrativos**; sin aleatoriedad. **Predice antes de ejecutar:** ¿Qué configuración necesita menos volumen para la misma remoción: un tanque grande o varios en serie? (varios en serie). **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9; numpy 2.4.4
DATOS: parametros ILUSTRATIVOS; sin datos de un tratamiento real; la filtracion multietapa y la verificacion por conductividad son las de la pagina de la NASA (consultada)
Caudal de aguas grises: 80 L/dia = 3.33 L/h; DBO de entrada 300 mg/L; k = 0.5 1/h
Remocion objetivo y volumen necesario (V = F tau):
   remocion   tau mezcla completa [h]   V [L]   tau piston [h]   V [L]   3 tanques: tau [h]   V [L]
       0.80                     8.0      27              3.2      11                  4.3      14
       0.90                    18.0      60              4.6      15                  6.9      23
       0.99                   198.0     660              9.2      31                 21.8      73
Control: tanque de 60 L con tau = 18 h: integracion 30.000 mg/L frente a 30.000 mg/L por formula
Remocion de N tanques en serie con el mismo tau total de 18 h:
   N =  1: S = 30.0000 mg/L (90.0000 % de remocion)
   N =  2: S =  9.9174 mg/L (96.6942 % de remocion)
   N =  3: S =  4.6875 mg/L (98.4375 % de remocion)
   N =  6: S =  1.2288 mg/L (99.5904 % de remocion)
   N = 20: S =  0.1777 mg/L (99.9408 % de remocion)
   flujo piston (N infinito): S = 0.0370 mg/L
Desinfeccion de Chick-Watson: log10(N0/N) = k C t, k = 0.5 L/(mg min):
   C [mg/L]   t para 4 log [min]   CT [mg min/L]
        0.5                16.0             8.0
        1.0                 8.0             8.0
        2.0                 4.0             8.0
Tren: filtro de 99 % (2.0 log) + desinfeccion de 4 log = 6.0 log de reduccion total
Pruebas superadas.
```

```bash
python programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/aguas_grises.py
```

**Límites:** una sola reacción de primer orden, caudal y carga constantes, sin temperatura ni inhibición, desinfección independiente del pH.

## 18. Errores frecuentes y cómo corregirlos

**Dimensionar con la mezcla completa sin considerar etapas.** Compara (8.2).

**Olvidar la desinfección.** Añade CT (8.3).

**Tomar `k` ilustrativo como dato.** Rotula.

**Medir solo la DBO.** Ver ejercicio 11.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué volumen da el 90 % de remoción en mezcla completa y cuánto el 3 en serie? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **dimensionado de un tratamiento de aguas grises** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Confunde las magnitudes | Parciales | Explica CSTR, etapas y CT | Explica los supuestos y sus límites |
| Cálculo | Sin unidades | Con errores | Calcula con unidades y cifras coherentes | Calcula casos nuevos y los verifica |
| Numérico | Sin comprobación | Un caso | Compara con el control del laboratorio | Interpreta la sensibilidad |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo ilustrativo y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta para un hábitat real |

**Condiciones críticas (no se compensan con promedio):** rotular los datos como sintéticos o ilustrativos; no presentar un valor ilustrativo como límite de una norma; citar solo lo consultado; no usar la clase como consejo médico ni operativo.

## 21. Ética, seguridad y límites

Clase **educativa**: no da consejo médico ni operativo y no sirve para decidir la atmósfera, el agua, la exposición ni la respuesta ante una emergencia de un hábitat o de una persona reales. El agua tratada para beber exige verificación microbiológica y química que esta clase no define. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Un biorreactor de mezcla completa necesita 60 L para el 90 %; tres tanques en serie, 23 L; la desinfección pide un CT de 8 mg·min/L para 4 log. La clase siguiente trata la orina.

**Glosario español–inglés.** aguas grises · *gray water*; biorreactor · *bioreactor*; mezcla completa · *CSTR*; flujo pistón · *plug flow*; desinfección · *disinfection*.

**Continuidad.** Sigue con la clase siguiente del bloque (enlace en la navegación) o vuelve al [bloque B106](../../../tronco-comun/B106-habitats-espaciales-y-soporte-vital.md).

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B106-C25 — Sensores de presión, gases y humedad para monitoreo de hábitat](../B106-C25-sensores-de-presion-gases-y-humedad-para-monitoreo-de-habitat/CLASE.md) · [📚 Bloque B106](../../../tronco-comun/B106-habitats-espaciales-y-soporte-vital.md) · [Siguiente: B106-C27 — Tratamiento de orina y recuperación de agua →](../B106-C27-tratamiento-de-orina-y-recuperacion-de-agua/CLASE.md)
<!-- /nav -->
