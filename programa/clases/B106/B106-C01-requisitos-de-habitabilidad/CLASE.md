# B106-C01 — Requisitos de habitabilidad

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B106](../../../tronco-comun/B106-habitats-espaciales-y-soporte-vital.md) · [← Anterior: B105-C27 — Instrumentos validados y psicometría en investigación](../../../tronco-comun/B105-medicina-y-biologia-espacial.md#b105-c27) · [Siguiente: B106-C02 — Presurización de módulos →](../B106-C02-presurizacion-de-modulos/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 1 del bloque B106 (hábitats espaciales y soporte vital). Nivel N3. Primera clase del bloque: fija **qué necesita y qué emite una persona** y entre qué límites de temperatura y humedad debe vivir. Todo el resto del bloque (atmósfera, agua, calor, residuos) dimensiona sistemas para cubrir estos números. Todos los datos del laboratorio son **sintéticos o ilustrativos** y se rotulan como tales; solo se tratan como consultados los valores de la sección 11 que dicen «Consultada».

## 2. Por qué esta clase existe

Un hábitat se diseña de adentro hacia afuera: primero lo que consume y emite la tripulación, después la máquina que lo repone. Si el balance humano está mal, todo el ECLSS queda mal dimensionado. La decisión central: **¿qué cantidades por persona y por día, y qué zona de temperatura y humedad, hay que garantizar, y con qué fuente?**

## 3. Lo que podrás hacer al terminar

1. Calcular el oxígeno que consume una persona en reposo a partir de su consumo específico y compararlo con el valor consultado.
2. Obtener el CO₂ exhalado con un cociente respiratorio y escalar el balance a una tripulación.
3. Convertir la ingesta de energía en potencia térmica que la cabina debe disipar.
4. Clasificar un par temperatura-humedad como dentro o fuera de las zonas de salud y de desempeño del resumen consultado.
5. Detectar una incoherencia en una fuente (el ejercicio extra de oxígeno) y decidir con qué cifra trabajar.
6. Rotular qué cifra es consultada, cuál es calculada y cuál es ilustrativa.

La evidencia es la **ficha de requisitos con el balance por tripulante** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es el cociente respiratorio?
2. ¿Qué es la ley de los gases ideales?
3. ¿Cuántos vatios son 3000 kcal por día?
4. ¿Qué es la humedad relativa?
5. ¿Qué es un dato ilustrativo?

<details>
<summary>Ver respuestas</summary>

1. El cociente entre el CO₂ producido y el O₂ consumido (mol/mol); aquí vale 0,85. 2. `PV = nRT`; permite pasar de litros a kilogramos. 3. `3000·4184/86400 ≈ 145 W`. 4. El cociente entre la presión de vapor y la de saturación a esa temperatura. 5. Un valor inventado o aproximado para enseñar un cálculo; se rotula y no se presenta como norma.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

El resumen técnico OCHMO-TB-002 (consultado) da, para una persona de 75 kg en reposo, un consumo de 5 ml/kg/min y un total de **0,771 kg de O₂ por día**; para 7 personas, 5,397 kg/día. El laboratorio reproduce esa cifra con la ley de los gases ideales: 540 L/día equivalen a **0,7709 kg/día** (diferencia −0,01 %). El CO₂ exhalado con RQ 0,85 es **0,9013 kg/día**, y la ingesta de 3035 kcal/día se convierte en **147,0 W** de calor por persona. Es el **ejemplo conductor** del bloque; los números son consultados o calculados, no medidos en un hábitat.

## 6. Vocabulario

**Consumo específico de oxígeno:** O₂ por kilogramo y minuto. **Cociente respiratorio (RQ):** mol de CO₂ por mol de O₂. **Normoxia:** oxígeno suficiente sin exceso. **Zona de salud:** intervalo de temperatura y humedad que protege la salud; **zona de desempeño:** el más estrecho en el que el trabajo rutinario no se degrada por estrés térmico. **ECLSS:** sistema de control ambiental y soporte vital.

## 7. Modelo mental

```mermaid
flowchart LR
    P["persona"] -->|"O2, agua, comida"| H["cabina"]
    P -->|"CO2, vapor, calor, residuos"| H
    H --> E["ECLSS repone, recicla, evacua"]
    E --> H
```

*Descripción textual:* la persona toma oxígeno, agua y alimento y emite CO₂, vapor, calor y residuos a la cabina; el ECLSS cierra el lazo reponiendo o reciclando.

Analogía: una persona es una «fuente y sumidero» de caudales fijos, como un electrodoméstico con su ficha técnica. Límite: la ficha cambia con la actividad (ejercicio), la dieta y el tamaño del cuerpo.

## 8. La explicación, paso a paso

### 8.1 Oxígeno y CO₂

El consumo en reposo es `V̇O₂ = 5·10⁻³ L/(kg·min)`; con 75 kg y 1440 min, `V = 540 L/día`. La masa sale de `ρ = P M/(R T)`: a 273,15 K y 101 325 Pa, `ρ = 1,428 kg/m³`, de modo que `m = 0,7709 kg/día`, que coincide con el valor consultado (0,771) dentro del 0,01 %. Con RQ 0,85 salen 20,48 mol/día de CO₂, es decir 0,9013 kg/día.

### 8.2 Escalar a la tripulación

Para 7 personas, `7·0,7709 = 5,397 kg/día`, igual al 5,397 consultado. Los balances son lineales en el número de personas, pero no en la actividad.

### 8.3 Una incoherencia en la fuente

El resumen cita «0,376 kg por sesión de ejercicio», pero sus propios totales (1,083 − 0,771) implican **0,312 kg**, y el cálculo propio con 120 min a 45 ml/kg/min da 0,514 kg. Las tres cifras no coinciden y el laboratorio no las reconcilia: se trabaja con los totales y se anota la discrepancia. Moraleja: una cifra consultada no es una cifra verificada.

### 8.4 Energía y calor

`3035 kcal/día · 4184 J/kcal / 86 400 s = 147,0 W` por persona, que acaban como calor en la cabina (clase C08). Cuatro personas aportan unos 0,6 kW.

### 8.5 Zonas de temperatura y humedad

El resumen consultado da dos zonas: salud (18–27 °C, 25–75 % de humedad relativa) y desempeño (20–25 °C, 30–60 %). El laboratorio las usa como rectángulos, según el texto; el resumen puede dibujarlas con otra forma en su figura. Con 26 °C y 70 % se está dentro de salud pero fuera de desempeño.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `V̇O₂` | consumo específico de O₂ | L/(kg·min) | 5·10⁻³ (consultado) |
| `m_O₂` | masa de O₂ por persona y día | kg/día | 0,7709 (consultado 0,771) |
| RQ | cociente respiratorio | — | 0,85 (consultado) |
| `m_CO₂` | masa de CO₂ exhalado | kg/día | 0,9013 |
| `P_met` | potencia metabólica media | W | 147,0 (de 3035 kcal/día) |
| `T`, HR | temperatura y humedad relativa | °C, % | zonas de la sección 8.5 |

## 10. Convenciones y referencias

Persona de 75 kg; gas ideal a 273,15 K y 101 325 Pa para convertir volumen en masa; masas molares 0,0320 y 0,04401 kg/mol; 1 kcal = 4184 J. Zonas como rectángulos. Tolerancias: O₂ dentro del 1 % de 0,771; 7 personas dentro del 1 % de 5,397; potencia metabólica entre 140 y 155 W. Numpy y Python: ver la primera línea de la salida del laboratorio (Python 3.12.9, numpy 2.4.4 en la ejecución del 2026-11-10).

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S2 | NASA, Oficina del Jefe de Salud y Medicina (OCHMO), OCHMO-TB-002 rev. B (14 de noviembre de 2023), «Environmental Control & Life Support System (ECLSS): Human-Centered Approach», resumen técnico derivado de NASA-STD-3001 vol. 2 rev. D — https://www.nasa.gov/wp-content/uploads/2023/12/ochmo-tb-002-eclss.pdf (consultada 2026-11-10; PDF leído con PyMuPDF) | pp. de balance (entradas y salidas), de oxígeno y de temperatura/humedad | consumo de 5 ml/kg/min con 75 kg, 0,771 kg/día de O₂ en reposo, 5,397 kg/día para 7, RQ 0,85, 3035 kcal/día, 2,5 L/día de agua, zonas 18–27 °C/25–75 % y 20–25 °C/30–60 % | Consultada (resumen técnico; las cifras de ejercicio no son coherentes entre sí) |
| — | Relaciones estándar: gas ideal, conversión kcal–J, escalado lineal | — | las verifica el laboratorio | No consultada en una fuente concreta |

Límites: el resumen es un documento derivado de NASA-STD-3001 y declara que no sustituye a los requisitos del programa; la norma completa (vol. 2 rev. D) no se consultó. La forma exacta de las zonas en su figura no se consultó; aquí son rectángulos tomados del texto.

## 12. Cómo ver el resultado

| Resultado | Valor |
|---|---|
| O₂ por persona y día | 0,7709 kg (consultado 0,771) |
| CO₂ por persona y día (RQ 0,85) | 0,9013 kg |
| O₂ de 7 personas | 5,397 kg/día |
| Potencia metabólica | 147,0 W por persona |
| Puntos de la tabla en zona de salud | 4 de 5 |

Descripción larga: el balance humano se reduce a pocos números por persona que escalan con la tripulación; los límites de temperatura y humedad forman una región, no un valor único.

## 13. Ejemplo trabajado: O₂ y CO₂ de una persona

**Paso 1 · Volumen.** `5·10⁻³·75·1440 = 540 L/día`.

**Paso 2 · Masa.** `ρ = 101325·0,032/(8,314462·273,15) = 1,428 kg/m³`, `m = 0,540 m³·1,428 = 0,771 kg`.

**Paso 3 · Moles y CO₂.** `0,771/0,032 = 24,1 mol`; `0,85·24,1 = 20,5 mol`; `20,5·0,04401 = 0,901 kg`.

**Paso 4 · Control.** El O₂ coincide con el valor consultado dentro del 1 %.

## 14. Distintas formas de describir el problema

**Por masa:** kg/día de cada magnitud. **Por moles:** estequiometría (C05). **Por potencia:** vatios de calor. **Por región:** zona T–HR. **Por escala:** por persona, por tripulación, por misión.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula el O₂ diario de una persona de 80 kg con el mismo consumo específico. *Pasos:* litros, densidad, masa.

<details><summary>Solución comentada</summary>

`5·10⁻³·80·1440 = 576 L`; `576·1,428/1000 = 0,822 kg/día` (escala con la masa corporal).
</details>

**Ejercicio 2 · con una pista.** Calcula el CO₂ de esa persona con RQ 0,85. *Pista:* pasa por moles.

<details><summary>Solución comentada</summary>

`0,822/0,032 = 25,7 mol`; `0,85·25,7 = 21,8 mol`; `·0,04401 = 0,96 kg/día`.
</details>

**Ejercicio 3 · casi autónomo.** ¿Está 23 °C y 55 % en la zona de desempeño? *Pista:* mira los dos intervalos.

<details><summary>Solución comentada</summary>

Sí: 20–25 °C y 30–60 % lo contienen (y también la zona de salud).
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Escala el balance de O₂ a 4 personas durante 30 días.

<details><summary>Solución comentada</summary>

`4·0,771·30 = 92,5 kg`.
</details>

**Ejercicio 5 · autónomo.** Calcula el calor metabólico de 4 personas con 3035 kcal/día.

<details><summary>Solución comentada</summary>

`4·147 = 588 W`.
</details>

**Ejercicio 6 · autónomo.** ¿Cuánta agua mínima para beber necesitan 6 personas en 180 días?

<details><summary>Solución comentada</summary>

`6·180·2,5 = 2700 L`.
</details>

**Ejercicio 7 · autónomo.** El resumen cita 0,376 kg por sesión y sus totales implican 0,312. ¿Qué cifra usas y por qué?

<details><summary>Solución comentada</summary>

Los totales, porque son coherentes entre sí (`7·1,083 = 7,581`); anotas la discrepancia y la reportas a quien mantiene la fuente.
</details>

**Ejercicio 8 · autónomo.** Con RQ 0,80 en lugar de 0,85, ¿cuánto CO₂ por día?

<details><summary>Solución comentada</summary>

`0,80·24,1·0,04401 = 0,849 kg/día`: cambia con la dieta.
</details>

**Ejercicio 9 · transferencia.** Una cabina de 120 m³ con 4 personas: ¿cuánto O₂ consumen por hora?

<details><summary>Solución comentada</summary>

`4·0,771/24 = 0,129 kg/h`; en volumen estándar, 90 L/h por persona (C03 y C05 lo usan).
</details>

**Ejercicio 10 · transferencia.** ¿Qué zona usarías para dimensionar el confort y cuál para el límite de seguridad?

<details><summary>Solución comentada</summary>

Desempeño (20–25 °C, 30–60 %) para el confort nominal; salud (18–27 °C, 25–75 %) como límite que no debe superarse.
</details>

**Ejercicio 11 · transferencia.** Si el consumo sube un 40 % por ejercicio, ¿cómo cambia el CO₂ y el calor?

<details><summary>Solución comentada</summary>

Ambos suben cerca de un 40 %; el diseño debe cubrir el pico, no solo el promedio (C04 y C08).
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de requisitos con el balance por tripulante*: entradas y salidas por persona y día con fuente y estado, escala a la tripulación y a la misión, calor, zonas T–HR con un caso en cada región, la incoherencia de la fuente y qué es consultado o calculado.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.5 y la salida del laboratorio.
</details>

## 17. Laboratorio: balance humano y zonas ambientales

El script [balance_humano.py](balance_humano.py) calcula el O₂ y el CO₂ de una persona con la ley de los gases ideales, escala a 7 personas, convierte kcal en vatios y clasifica pares T–HR (**comprueba** el 0,771 consultado, el 5,397 de 7 personas y el rango de potencia).

**Datos:** valores **consultados** (sección 11) y cálculo propio; no hay medición de un hábitat. Sin aleatoriedad. **Predice antes de ejecutar:** ¿Cuántos kg de O₂ al día consume una persona de 75 kg en reposo? (0,771 kg). **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9; numpy 2.4.4
DATOS: valores consultados de OCHMO-TB-002 y calculo propio; NINGUNA cifra es una medicion de un habitat real
O2 en reposo por persona: 540 L/dia -> 0.7709 kg/dia (consultado: 0.771; diferencia -0.01 %)
CO2 exhalado (RQ 0.85): 20.48 mol/dia = 0.9013 kg/dia
Tripulacion de 7: O2 = 5.397 kg/dia (consultado: 5.397)
Ejercicio (120 min a 45 ml/kg/min): calculo propio 0.514 kg sobre el reposo; el resumen cita 0.376 pero sus totales implican 0.312 -> no se reproduce con estos supuestos
Potencia metabolica media: 3035 kcal/dia = 147.0 W por persona (se disipa como calor en la cabina)
Agua minima para beber (consultada): 2.5 L/dia por persona; tripulacion de 4 en 30 dias: 300 L
Zonas (texto del resumen, como rectangulos): salud 18-27 C / 25-75 %; desempeno 20-25 C / 30-60 %
   T [C]  HR [%]   salud  desempeno
    22.0    45.0      si         si
    26.0    70.0      si         no
    19.0    28.0      si         no
    29.0    40.0      no         no
    24.0    65.0      si         no
Pruebas superadas.
```

```bash
python programa/clases/B106/B106-C01-requisitos-de-habitabilidad/balance_humano.py
```

**Límites:** una persona estándar en reposo, gas ideal a 0 °C, zonas como rectángulos; el ejercicio extra no se reproduce; no incluye variación individual ni dieta.

## 18. Errores frecuentes y cómo corregirlos

**Usar el consumo de una persona de otro peso sin escalar.** El consumo escala con la masa corporal (8.1).

**Confundir masa y volumen de gas.** Usa la densidad a la temperatura y presión indicadas.

**Tomar una cifra consultada como verificada.** Contrasta con otra vía; ver 8.3.

**Presentar un valor ilustrativo como límite de la norma.** Rotula y cita solo lo consultado (sección 11).

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿cuánto O₂ y CO₂ por persona y qué zona T–HR contiene 26 °C y 70 %? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de requisitos con el balance por tripulante** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Confunde las magnitudes | Parciales | Explica entradas, salidas y zonas | Explica los supuestos y sus límites |
| Cálculo | Sin unidades | Con errores | Calcula con unidades y cifras coherentes | Calcula casos nuevos y los verifica |
| Numérico | Sin comprobación | Un caso | Compara con el control del laboratorio | Interpreta la sensibilidad |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo ilustrativo y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta para un hábitat real |

**Condiciones críticas (no se compensan con promedio):** rotular los datos como sintéticos o ilustrativos; no presentar un valor ilustrativo como límite de una norma; citar solo lo consultado; no usar la clase como consejo médico ni operativo.

## 21. Ética, seguridad y límites

Clase **educativa**: no da consejo médico ni operativo y no sirve para decidir la atmósfera, el agua, la exposición ni la respuesta ante una emergencia de un hábitat o de una persona reales. Los límites de temperatura y humedad citados proceden de un resumen técnico y no son una prescripción médica. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

El balance humano son pocos números: **0,771 kg de O₂**, **0,90 kg de CO₂** y **147 W** por persona y día, que escalan con la tripulación. Con ellos se dimensiona el resto del bloque; la clase siguiente muestra cómo mantener la presión que hace respirable ese oxígeno.

**Glosario español–inglés.** cociente respiratorio · *respiratory quotient*; normoxia · *normoxia*; tripulación · *crew*; soporte vital · *life support*; humedad relativa · *relative humidity*.

**Continuidad.** Sigue con la clase siguiente del bloque (enlace en la navegación) o vuelve al [bloque B106](../../../tronco-comun/B106-habitats-espaciales-y-soporte-vital.md).

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B105-C27 — Instrumentos validados y psicometría en investigación](../../../tronco-comun/B105-medicina-y-biologia-espacial.md#b105-c27) · [📚 Bloque B106](../../../tronco-comun/B106-habitats-espaciales-y-soporte-vital.md) · [Siguiente: B106-C02 — Presurización de módulos →](../B106-C02-presurizacion-de-modulos/CLASE.md)
<!-- /nav -->
