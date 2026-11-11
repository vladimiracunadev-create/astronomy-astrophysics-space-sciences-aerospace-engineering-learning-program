# B120-C02 — Zonas de coordinación entre servicios radioeléctricos

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B120](../../../tronco-comun/B120-espectro-licencias-y-regulacion-satelital.md) · [← Anterior: B120-C01 — Licencias satelitales y procedimiento de notificación](../B120-C01-licencias-satelitales-y-procedimiento-de-notificacion/CLASE.md) · [Siguiente: B120-C03 — Posiciones orbitales y espectro como recursos limitados →](../../../tronco-comun/B120-espectro-licencias-y-regulacion-satelital.md#b120-c03)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 2 del bloque B120. Nivel N4. Antes de notificar o poner en servicio una asignación hay que coordinar con las administraciones cuyos servicios pueden verse afectados. En el caso de una estación terrena, esa decisión se apoya en una **zona de coordinación**: la región alrededor de la estación donde otra estación podría recibir interferencia por encima de un nivel permisible. Aquí estimas esa zona con un modelo de pérdida de espacio libre, decides qué administraciones caen dentro y calculas los plazos de respuesta. Retomas el procedimiento de [B120-C01](../B120-C01-licencias-satelitales-y-procedimiento-de-notificacion/CLASE.md). **Esta clase es educativa: no es asesoría legal ni regulatoria y el cálculo de la zona no es el método reglamentario.** Las estaciones y las administraciones son sintéticas.

## 2. Por qué esta clase existe

Coordinar con otros servicios define dónde y cómo se puede operar y ninguna clase lo trata. La decisión central: **¿con qué administraciones hay que coordinar una estación terrena y en cuánto tiempo deben responder?**

## 3. Lo que podrás hacer al terminar

1. Explicar qué es una zona de coordinación y por qué se calcula.
2. Calcular una distancia de coordinación con la pérdida de espacio libre y comprobarla con su inversa.
3. Calcular la distancia de gran círculo entre dos puntos con dos fórmulas.
4. Decidir qué administraciones quedan dentro de la zona.
5. Aplicar los plazos de 30 días y de 4 meses a respuestas sintéticas, incluido el silencio.
6. Separar lo consultado (plazos y concepto) de lo ilustrativo (el modelo de propagación) y de lo no consultado (el método reglamentario).

La evidencia es la **ficha de zona de coordinación de una estación terrena sintética** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es un decibelio?
2. ¿Cuánto cambia la pérdida de espacio libre al duplicar la distancia?
3. ¿Qué es la distancia de gran círculo?
4. ¿Qué es una asignación a una estación terrena?
5. ¿Qué es un dato sintético?

<details>
<summary>Ver respuestas</summary>

1. Una unidad logarítmica de razón de potencias, `10 log10(P2/P1)`. 2. Aumenta 6,02 dB. 3. La distancia más corta entre dos puntos sobre una esfera. 4. La frecuencia, potencia y otras características con que una estación terrena opera. 5. Un dato inventado para el ejemplo, no real.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

El documento de la UIT sobre el marco regulatorio de los servicios espaciales (creado el 2018-01-10; leído el 2026-11-11) explica que, en los casos de estación terrena frente a estación terrenal, la solicitud se envía directamente a las administraciones identificadas, que tienen 30 días para acusar recibo, y que la condición de coordinación se basa generalmente en la zona de coordinación de la estación terrena que cubre el territorio de otra administración (Apéndice 5). En los casos que pasan por la Oficina, la administración afectada dispone de cuatro meses para acordar o discrepar con datos técnicos. El **ejemplo conductor** es una estación terrena sintética en `(−33,00; −70,00)` que transmite a 6 GHz con una PIRE de 40 dBW hacia el horizonte; seis estaciones vecinas inventadas de tres administraciones sintéticas determinan con quién coordinar. Todo el modelo numérico es **ilustrativo**.

## 6. Vocabulario

La **zona de coordinación** es el área dentro de la cual hay que coordinar. La **distancia de coordinación** `d` es el radio de esa zona en este modelo circular. La **PIRE** es la potencia isótropa radiada equivalente, en dBW. La **pérdida de espacio libre** `L` es la atenuación por propagación en el vacío. La **potencia permisible** es el nivel máximo de interferencia aceptado en la estación afectada. **Acusar recibo** es confirmar que se recibió la solicitud.

## 7. Modelo mental: un círculo de cautela

```mermaid
flowchart LR
    P["PIRE + ganancia - permisible"] --> D["distancia d: L(d) = presupuesto"]
    D --> Z["zona: circulo de radio d"]
    Z --> V["vecinas dentro: coordinar"]
    V --> T["30 dias: acuse; 4 meses: respuesta"]
```

*Descripción textual:* el presupuesto de potencia fija un radio; las estaciones dentro de él obligan a coordinar y arrancan los plazos.

Analogía: el radio al que se oye una radio a volumen fijo antes de que moleste al vecino. Límite: el método real usa modos de propagación, relieve y diagramas de antena, no un círculo de espacio libre.

## 8. La explicación, paso a paso

### 8.1 Presupuesto y distancia

La pérdida de espacio libre es `L = 92,45 + 20 log10(f/GHz) + 20 log10(d/km)` dB. La zona termina donde la señal baja al nivel permisible: `PIRE + G − L(d) = P_perm`. Con `PIRE = 40 dBW`, `G = 0 dBi`, `P_perm = −110 dBW` y `f = 6 GHz`, el presupuesto es 150 dB y `d = 125,7 km`.

### 8.2 Efecto de la frecuencia

Duplicar la frecuencia suma 6,02 dB de pérdida y reduce `d` a la mitad: 251,4 km a 3 GHz, 125,7 km a 6 GHz y 62,9 km a 12 GHz. Este modelo suele sobrestimar `d` porque el espacio libre es el caso de menor pérdida; no se consultó cómo el método reglamentario trata otros modos de propagación.

### 8.3 Quién está dentro

Con la distancia de gran círculo de cada estación vecina a la estación terrena: T1 (66,9 km), T3 (64,5 km) y T6 (79,2 km) están dentro; T2 (136,3 km), T4 y T5 están fuera. Por tanto hay que coordinar con las tres administraciones sintéticas.

### 8.4 Plazos

Con solicitud publicada el 2028-01-31: acuse hasta 2028-03-01 (30 días) y respuesta hasta 2028-05-31 (4 meses). T1 acuerda el 2028-03-16; T3 calla y se la considera no afectada; T6 discrepa el 2028-06-29, **fuera de plazo**. Aplicar el silencio como no afectación a todos los casos es una simplificación: el documento lo indica para los casos de Nos. 9.11–9.14 y 9.21.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `PIRE` | potencia isótropa radiada equivalente | dBW | 40 (ilustrativo) |
| `G` | ganancia del receptor afectado | dBi | 0 (ilustrativo) |
| `P_perm` | potencia permisible | dBW | −110 (ilustrativo) |
| `f` | frecuencia | GHz | 6 |
| `d` | distancia de coordinación | km | 125,7 |
| `R` | radio de la esfera | km | 6371 (no consultado) |

## 10. Convenciones y referencias

Latitud y longitud en grados, positivas al norte y al este; esfera de radio 6371 km; distancia por gran círculo. Una estación está dentro si `dist ≤ d`. El nivel permisible es el recibido en la banda de referencia, sin margen. Los plazos y la lógica de silencio son del documento de la UIT de 2018; el Apéndice 5 y el Apéndice 7 no se consultaron.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | UIT, «ITU Radio Regulatory Framework for Space Services» (PDF; metadatos de creación 2018-01-10; refleja el Reglamento hasta la CMR-15) — https://www.itu.int/en/ITU-R/space/snl/Documents/ITU-Space_reg.pdf (consultada 2026-11-11) | secciones 4.3 y 4.4 (4.3.4, 4.3.7, 4.4.1–4.4.2), leído con PyMuPDF | zona de coordinación de estación terrena, 30 días para acusar recibo, 4 meses para responder, silencio como no afectación en Nos. 9.11–9.14 y 9.21 | Consultada (síntesis de la UIT; no es el texto del Reglamento) |
| — | Reglamento de Radiocomunicaciones, Apéndices 5 y 7 | — | umbrales y método de la zona | No consultado |
| — | Pérdida de espacio libre `92,45 + 20 log f + 20 log d` | — | fórmula del laboratorio | Relación estándar, verificada por inversa y por razón, no consultada en una fuente |
| — | Estaciones y administraciones | — | todo el laboratorio | Sintético |

Límites: el modelo no es el método reglamentario; la fuente es de 2018; la fórmula de propagación no se contrastó con una fuente primaria.

## 12. Cómo ver la zona

| f (GHz) | d (km) | Área (km²) |
|---|---|---|
| 3 | 251,4 | 198 567 |
| 6 | 125,7 | 49 642 |
| 12 | 62,9 | 12 410 |

Descripción larga: al duplicar la frecuencia la distancia se reduce a la mitad y el área a la cuarta parte.

## 13. Ejemplo trabajado: la distancia a 6 GHz

**Paso 1 · Presupuesto.** `40 + 0 − (−110) = 150 dB`.

**Paso 2 · Constante.** `92,45 + 20 log10(6) = 92,45 + 15,56 = 108,01 dB`.

**Paso 3 · Término de distancia.** `150 − 108,01 = 41,99 dB`.

**Paso 4 · Distancia.** `d = 10^(41,99/20) = 125,7 km`.

## 14. Distintas formas de describir la coordinación

**Por radio:** `d`. **Por área:** `π d²`. **Por administración:** las que tienen estaciones dentro. **Por plazo:** 30 días y 4 meses. **Por estado:** acuerdo, desacuerdo o no afectada por silencio.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula `d` a 12 GHz con el mismo presupuesto. *Pasos:* constante `92,45 + 20 log10(12) = 114,03`; resta de 150; eleva.

<details><summary>Solución comentada</summary>

`150 − 114,03 = 35,97`; `d = 10^(35,97/20) = 62,9 km`.
</details>

**Ejercicio 2 · con una pista.** ¿Qué `d` resulta si la potencia permisible sube 6 dB (a −104 dBW)? *Pista:* el presupuesto baja 6 dB.

<details><summary>Solución comentada</summary>

`d` se reduce a la mitad: unos 63 km.
</details>

**Ejercicio 3 · casi autónomo.** ¿Por qué T2 (136,3 km) queda fuera si está en la misma administración que T1?

<details><summary>Solución comentada</summary>

La zona se evalúa por estación, no por administración: 136,3 km supera los 125,7 km. La administración se coordina igualmente por T1.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Distancia a 8 GHz con el mismo presupuesto.

<details><summary>Solución comentada</summary>

`125,7 × 6/8 = 94,3 km`.
</details>

**Ejercicio 5 · autónomo.** Área de la zona a 6 GHz.

<details><summary>Solución comentada</summary>

`π × 125,7² ≈ 49 640 km²`.
</details>

**Ejercicio 6 · autónomo.** Fecha límite de respuesta para una solicitud publicada el 2028-10-31.

<details><summary>Solución comentada</summary>

Cuatro meses después, `2029-02-28` (el día se recorta a febrero).
</details>

**Ejercicio 7 · autónomo.** Fecha límite del acuse para esa misma solicitud.

<details><summary>Solución comentada</summary>

`2028-11-30`, 30 días después.
</details>

**Ejercicio 8 · autónomo.** ¿Cuál es la distancia de gran círculo de un grado de longitud en el ecuador?

<details><summary>Solución comentada</summary>

`2π × 6371/360 = 111,19 km`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** ¿Por qué un cálculo con espacio libre no sirve para presentar una coordinación real?

<details><summary>Solución comentada</summary>

Porque el método reglamentario (Apéndice 7, no consultado) considera modos de propagación y parámetros que este modelo omite; solo vale como ejercicio.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** T6 responde fuera de plazo con desacuerdo. ¿Qué analizas antes de concluir que su objeción se ignora?

<details><summary>Solución comentada</summary>

Qué dice el texto vigente (no consultado) sobre respuestas tardías y la obligación de cooperar para resolver dificultades (No. 9.53 en el documento consultado); no se concluye con este modelo.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Qué datos reales necesitarías para sustituir `P_perm`?

<details><summary>Solución comentada</summary>

Los umbrales del Apéndice 5 para el servicio y la banda concretos, la sensibilidad de las estaciones afectadas y los márgenes que fije la administración.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de zona de coordinación de una estación terrena sintética*: parámetros, `d` en tres frecuencias, tabla de vecinas con estado, plazos y lista de qué es consultado, ilustrativo y no consultado, con el aviso de que no es asesoría legal ni regulatoria.

<details><summary>Solución comentada</summary>

Secciones 8 y 12 y la salida del laboratorio.
</details>

## 17. Laboratorio: zona de coordinación y respuestas

El script [coordinacion.py](coordinacion.py) calcula `d` con la pérdida de espacio libre, evalúa seis estaciones sintéticas y aplica los plazos (**comprueba** la inversa a 1e-9 dB, la razón 2:1 y la distancia con dos fórmulas a 0,01 km).

**Datos:** plazos y concepto consultados; parámetros de propagación y estaciones **ilustrativos o sintéticos**. **Predice antes de ejecutar:** ¿cuántas estaciones caen dentro de la zona? (tres.) **Ejecución del 2026-11-11 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
ZONA DE COORDINACION ILUSTRATIVA (espacio libre); plazos de 30 dias y 4 meses del documento UIT 2018-01-10, consultado 2026-11-11. No es asesoria.
Distancia de coordinacion a 6.0 GHz: 125.7 km (area = 49642 km2)
  f =  3.0 GHz -> d =   251.4 km
  f =  6.0 GHz -> d =   125.7 km
  f = 12.0 GHz -> d =    62.9 km
Verificacion inversa |nivel recibido - permisible| = 0.0e+00 dB
Razon d(3 GHz)/d(6 GHz) = 2.0000 (esperada 2.0000)
Solicitud publicada 2028-01-31; plazo de 4 meses hasta 2028-05-31; acuse de recibo en 30 dias hasta 2028-03-01
Est  Adm    dist[km]  dentro  respuesta      estado
T1   ADM-X      66.9  si      2028-03-16     acuerdo
T2   ADM-X     136.3  no      -              fuera de la zona
T3   ADM-Y      64.5  si      ninguna        no afectada por silencio
T4   ADM-Y     429.9  no      -              fuera de la zona
T5   ADM-Z     564.2  no      -              fuera de la zona
T6   ADM-Z      79.2  si      2028-06-29     desacuerdo (fuera de plazo)
Administraciones a coordinar: ['ADM-X', 'ADM-Y', 'ADM-Z']
Maxima diferencia haversine - coseno esferico = 6.5e-11 km
Pruebas superadas.
```

```bash
python programa/clases/B120/B120-C02-zonas-de-coordinacion-entre-servicios-radioelectricos/coordinacion.py
```

**Límites:** modelo circular de espacio libre; sin relieve ni antenas; silencio tratado como no afectación para todos los casos.

## 18. Errores frecuentes y cómo corregirlos

**Tomar el modelo como el método reglamentario.** Se corrige con las secciones 1 y 11.

**Olvidar que la zona se evalúa por estación.** Se corrige con el ejercicio 3.

**Usar el silencio como acuerdo.** Es «no afectada» en ciertos casos, no un acuerdo expreso; se corrige con 8.4.

**Mezclar dBW y dBm.** Se corrige con la sección 9.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué `d` esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de zona de coordinación de una estación terrena sintética** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Explica zona, distancia y plazos | Explica los límites del modelo |
| Cálculo | Sin unidades | Con errores | `d` y áreas con unidades | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Inversa y segunda fórmula | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha, versión y estado | Declara lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** declarar que el cálculo no es el método reglamentario; rotular lo sintético; citar la versión y fecha del texto y declarar que no es asesoría legal ni regulatoria.

## 21. Ética, seguridad y límites

Clase educativa: **no es asesoría legal, regulatoria ni financiera** y ningún resultado debe usarse para coordinar una estación real; para ello corresponde el método vigente del Reglamento y la administración nacional. Los datos son sintéticos y el modelo es simplificado. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Con 40 dBW, −110 dBW y 6 GHz, la zona sintética tiene 125,7 km de radio y obliga a coordinar con tres administraciones; una de ellas responde fuera de plazo. Queda una pregunta: ¿qué recurso escaso se está coordinando en último término?

**Glosario español–inglés.** zona de coordinación · *coordination area*; PIRE · *equivalent isotropically radiated power (e.i.r.p.)*; pérdida de espacio libre · *free-space loss*; potencia permisible · *permissible interference level*; acusar recibo · *acknowledge receipt*.

**Continuidad.** [B120-C03](../B120-C03-posiciones-orbitales-y-espectro-como-recursos-limitados/CLASE.md) estudia las posiciones orbitales y el espectro como recursos limitados.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B120-C01 — Licencias satelitales y procedimiento de notificación](../B120-C01-licencias-satelitales-y-procedimiento-de-notificacion/CLASE.md) · [📚 Bloque B120](../../../tronco-comun/B120-espectro-licencias-y-regulacion-satelital.md) · [Siguiente: B120-C03 — Posiciones orbitales y espectro como recursos limitados →](../../../tronco-comun/B120-espectro-licencias-y-regulacion-satelital.md#b120-c03)
<!-- /nav -->
