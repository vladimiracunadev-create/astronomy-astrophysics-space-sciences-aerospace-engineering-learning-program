# B81-C05 — Limitaciones de potencia en propulsión eléctrica

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B81](../../../tronco-comun/B81-optimizacion-de-trayectorias-y-diseno-robusto.md) · [← Anterior: B81-C04 — Trayectorias espirales de bajo empuje](../B81-C04-trayectorias-espirales-de-bajo-empuje/CLASE.md) · [Siguiente: B81-C06 — Restricciones de orientación del empuje →](../B81-C06-restricciones-de-orientacion-del-empuje/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 5 del bloque B81 (área A06). Nivel N3. La propulsión eléctrica no tiene un empuje fijo: depende de la potencia que dan los paneles, y esa potencia cae con el cuadrado de la distancia al Sol. Aquí calculas la irradiancia a partir de la luminosidad del Sol, el empuje de un propulsor con saturación y la zona en que se apaga, y ves qué le pasa a la aceleración al alejarse. Usas [B81-C04](../B81-C04-trayectorias-espirales-de-bajo-empuje/CLASE.md) solo para el `Δv` de una espiral. Las cifras de la nave son ilustrativas.

## 2. Por qué esta clase existe

Un diseño de trayectoria que ignore la potencia sobreestima el empuje lejos del Sol. La decisión central: **¿hasta qué distancia mantiene una nave eléctrica su empuje máximo y a partir de dónde pierde capacidad?**

## 3. Lo que podrás hacer al terminar

1. Calcular la irradiancia a 1 UA con `L/(4π UA²)`.
2. Escalar la potencia de paneles con `1/r²`.
3. Calcular el empuje con `T = 2ηP/(g₀ Isp)`.
4. Incluir la saturación del propulsor y el apagado por potencia mínima.
5. Calcular los radios de saturación y de apagado.
6. Contrastar la relación empuje/potencia con el rango publicado por la NASA y separar lo consultado de lo ilustrativo.

La evidencia es la **curva de empuje frente a distancia al Sol** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es la luminosidad de una estrella?
2. ¿Qué es la irradiancia?
3. ¿Qué es el impulso específico `Isp`?
4. ¿Qué es la eficiencia de un propulsor?
5. ¿Qué es un dato ilustrativo?

<details>
<summary>Ver respuestas</summary>

1. La energía que emite por segundo, en vatios. 2. La potencia que llega por unidad de área, en W/m². 3. El empuje por peso de propelente por segundo; `v_e = g₀ Isp`. 4. El cociente entre la potencia del chorro y la potencia eléctrica. 5. Un valor elegido para el ejemplo, no medido ni consultado.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Una nave con paneles de 10 kW a 1 UA, `η = 0,60`, `Isp = 2500 s` y un propulsor que admite 4,5 kW entrega `220,26 mN` hasta 1,49 UA y luego cae: `122,37 mN` a 2 UA, `54,38 mN` a 3 UA, y se apaga más allá de 4,47 UA. Es el **ejemplo conductor**. Las cifras de la nave son **ilustrativas**.

## 6. Vocabulario

La **irradiancia** a 1 UA es `S = L/(4π UA²)`. La **potencia disponible** es `P(r) = P₁ (1 UA/r)²`. El **empuje** de un propulsor eléctrico es `T = 2ηP/(g₀ Isp)`. La **saturación** es el tope `P_max` de potencia que admite el propulsor. El **apagado** ocurre cuando `P < P_min`.

## 7. Modelo mental: un grifo alimentado por una cañería que se ensancha

```mermaid
flowchart LR
    L["luminosidad L"] --> S["irradiancia S(r)"]
    S --> P["potencia P(r)"]
    P --> U["clamp: Pmin, Pmax"]
    U --> T["empuje T = 2 eta P / (g0 Isp)"]
    T --> A["aceleración T / m"]
```

*Descripción textual:* la luminosidad da la irradiancia, esta da la potencia de los paneles, se limita entre el mínimo y el máximo del propulsor y de ahí salen el empuje y la aceleración.

Analogía: un grifo conectado a un depósito que se vacía con el cuadrado de la distancia; el grifo no entrega más que su máximo. Límite: aquí los paneles no se degradan ni se calientan, y la eficiencia `η` es constante; en la realidad dependen de la temperatura y de la potencia.

## 8. La explicación, paso a paso

### 8.1 Irradiancia

Con `L = 382,8 × 10²⁴ W` (NASA/NSSDC) y `UA = 149 597 870,7 km` (JPL SSD): `S = 1361,2 W/m²`. Se calcula; no se consultó un valor publicado de la constante solar.

### 8.2 Empuje por kilovatio

`2η/(g₀ Isp) = 2 · 0,60/(9,80665 · 2500) = 48,95 mN/kW`. La NASA indica que la propulsión eléctrica da «generalmente» menos de 75 mN/kW en los dispositivos de naves pequeñas; el valor ilustrativo cae dentro del rango.

### 8.3 Saturación y apagado

Con `P₁ = 10 kW`, `P_max = 4,5 kW` y `P_min = 0,5 kW`: el radio de saturación es `√(10/4,5) = 1,4907 UA` y el de apagado `√(10/0,5) = 4,4721 UA`.

| `r` (UA) | `P` (W) | `P` útil (W) | `T` (mN) |
|---|---|---|---|
| 0,7 | 20 408,2 | 4500 | 220,26 |
| 1,5 | 4444,4 | 4444,4 | 217,54 |
| 2,0 | 2500 | 2500 | 122,37 |
| 3,0 | 1111,1 | 1111,1 | 54,38 |
| 4,0 | 625 | 625 | 30,59 |
| 5,0 | 400 | 0 | 0 |

### 8.4 Qué cambia al alejarse

Fuera de la zona saturada, `T r²` es constante (desviación `0`). Con una nave de 1000 kg y una velocidad radial de 5 km/s, el `Δv` acumulado entre 1 y 3 UA sería `8176 m/s` si el empuje estuviera siempre disponible; con la curva de este ejemplo el empuje a 2 UA es solo el 56 % del máximo (122,37 frente a 220,26 mN), de modo que ese `Δv` sobreestima lo que se logra.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `L` | luminosidad del Sol | W | 382,8 × 10²⁴ (consultada) |
| `S` | irradiancia a 1 UA | W/m² | 1361,2 (calculada) |
| `P` | potencia de paneles | W | 10 000 a 1 UA (ilustrativa) |
| `η` | eficiencia | — | 0,60 (ilustrativa) |
| `Isp` | impulso específico | s | 2500 (ilustrativo; dentro de 500–3000 s para iones de naves pequeñas) |
| `T` | empuje | mN | 220,26 (máx.) |

## 10. Convenciones y referencias

Luminosidad del Sol de la ficha del NSSDC; UA del JPL SSD; `g₀ = 9,80665 m/s²` es el valor convencional y no se consultó en esta sesión. Paneles perpendiculares al Sol, sin degradación; masa 1000 kg; sin pérdidas de potencia por el resto de la nave.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA/NSSDC, Sun Fact Sheet — https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html (consultada 2026-11-10) | ficha completa leída | luminosidad 382,8 × 10²⁴ W; GM del Sol 132 712 × 10⁶ km³/s²; distancia media Tierra–Sol 149,6 × 10⁶ km; la ficha no da la irradiancia a 1 UA, que se calcula en la clase | Consultada |
| S2 | NASA JPL SSD, Astrodynamic Parameters — https://ssd.jpl.nasa.gov/astro_par.html (consultada 2026-11-10) | tabla completa leída | GM del Sol = 1,32712440041279419 × 10²⁰ m³/s² (132712440041,279419 km³/s²); unidad astronómica = 149 597 870,7 km (IAU 2012 B1); GM de la Tierra = 398600,435507 km³/s²; masas planetarias de DE440 (Park et al., 2021) | Consultada |
| S3 | NASA, State-of-the-Art of Small Spacecraft Technology, capítulo de propulsión — https://www.nasa.gov/smallsat-institute/sst-soa/in-space-propulsion/ (consultada 2026-11-10; leídos los primeros 100 000 de 289 063 caracteres) | tabla 4-1 y texto introductorio | propulsores iónicos de rejilla 0,1–20 mN y 500–3000 s; Hall 0,25–55 mN y 200–1920 s; empuje/potencia generalmente inferior a 75 mN/kW; un sistema de 500 W produce a lo sumo unos 38 mN. Son dispositivos de naves pequeñas, no límites físicos | Consultada (parcialmente) |
| — | Relaciones estándar (relación empuje–potencia `T = 2ηP/(g₀ Isp)`, ley del inverso del cuadrado de la irradiancia) | — | las verifica el laboratorio con una segunda vía | No consultada en una fuente concreta |

Límites: los rangos de la NASA describen dispositivos de naves pequeñas, no límites físicos; la nave de 10 kW, `η`, `Isp` y los topes del propulsor son ilustrativos; se leyeron solo los primeros 100 000 de 289 063 caracteres del capítulo de propulsión.

## 12. Cómo ver el empuje frente a la distancia

| Magnitud | Valor |
|---|---|
| irradiancia a 1 UA | 1361,2 W/m² |
| empuje por kW | 48,95 mN/kW |
| radio de saturación | 1,4907 UA |
| radio de apagado | 4,4721 UA |

Descripción larga: el empuje es constante hasta 1,49 UA, cae como `1/r²` hasta 4,47 UA y se anula después.

## 13. Ejemplo trabajado: el empuje a 3 UA

**Paso 1 · Potencia.** `P = 10 000/3² = 1111,1 W`.

**Paso 2 · Por debajo del tope.** `1111,1 W < 4500 W`: no satura.

**Paso 3 · Empuje.** `T = 2 · 0,60 · 1111,1/(9,80665 · 2500) = 0,05438 N = 54,38 mN`.

**Paso 4 · Aceleración.** `a = 54,38 × 10⁻³/1000 = 5,44 × 10⁻⁵ m/s²`.

## 14. Distintas formas de describir el empuje de una nave eléctrica

**Por distancia:** `T(r)`. **Por potencia:** `T = 2ηP/(g₀ Isp)`. **Por aceleración:** `T/m`. **Por zona:** saturada, proporcional a `1/r²`, apagada.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula la irradiancia a 1 UA con `L = 3,828 × 10²⁶ W`. *Pasos:* `S = L/(4π d²)` con `d = 1,495979 × 10¹¹ m`.

<details><summary>Solución comentada</summary>

`S ≈ 1361 W/m²`.
</details>

**Ejercicio 2 · con una pista.** Calcula el empuje a 2 UA con los datos del ejemplo. *Pista:* `P = 2500 W`.

<details><summary>Solución comentada</summary>

`T = 2·0,6·2500/(9,80665·2500) = 0,1224 N = 122,4 mN`.
</details>

**Ejercicio 3 · casi autónomo.** ¿A qué distancia empieza a caer el empuje? Usa `√(P₁/P_max)`.

<details><summary>Solución comentada</summary>

`1,4907 UA`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** ¿Qué empuje tendría el mismo propulsor a 1,5 UA y a 3 UA y cuál es su cociente?

<details><summary>Solución comentada</summary>

`217,54` y `54,38 mN`; el cociente es 4,0 = (3/1,5)².
</details>

**Ejercicio 5 · autónomo.** ¿Cuánto vale la aceleración a 4 UA para 1000 kg?

<details><summary>Solución comentada</summary>

`30,59 mN/1000 kg = 3,06 × 10⁻⁵ m/s²`.
</details>

**Ejercicio 6 · autónomo.** ¿Qué `Isp` haría que el empuje por kW fuera 75 mN/kW con `η = 0,6`?

<details><summary>Solución comentada</summary>

`75 mN/kW = 7,5 × 10⁻⁵ N/W`, luego `Isp = 2η/(g₀ · 7,5×10⁻⁵) = 1,2/(9,80665 · 7,5×10⁻⁵) ≈ 1632 s`.
</details>

**Ejercicio 7 · autónomo.** Si los paneles se degradan un 20 %, ¿cómo cambia el radio de apagado?

<details><summary>Solución comentada</summary>

`r = √(0,8 P₁/P_min) = 4,0 UA` (baja un 10,6 %).
</details>

**Ejercicio 8 · autónomo.** ¿Qué empuje da un propulsor de 500 W con `η = 0,6` e `Isp = 2500 s`?

<details><summary>Solución comentada</summary>

`T = 2·0,6·500/(9,80665·2500) = 24,5 mN`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** **Transferencia.** Un diseñador compara con el límite de 75 mN/kW de la NASA. ¿Qué precauciones toma?

<details><summary>Solución comentada</summary>

Que el valor describe dispositivos de naves pequeñas relevados, no un límite físico; un propulsor mayor o distinto puede salirse del rango.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** **Transferencia.** Una misión va a 5 UA con paneles de 10 kW a 1 UA. ¿Qué opciones tiene?

<details><summary>Solución comentada</summary>

Paneles mayores, un propulsor con menor `P_min`, otra fuente de energía (nuclear) o aceptar el apagado; la clase calcula que 400 W < 500 W en este ejemplo.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** **Transferencia.** ¿Cómo afecta la eficiencia de los paneles con la temperatura (más alta cerca del Sol)?

<details><summary>Solución comentada</summary>

Reduce `P` cerca del Sol y por tanto el empuje; el modelo ilustrativo no lo incluye.
</details>

**Ejercicio 12 · integrador.** **Integrador.** **Integrador.** Elabora tu *curva de empuje frente a distancia al Sol*: tabla de `P`, `T` y `a` entre 0,7 y 5 UA, radios de saturación y de apagado, y lo consultado frente a lo ilustrativo.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: empuje de un propulsor eléctrico frente a la distancia

El script [potencia.py](potencia.py) calcula la irradiancia, el empuje por kilovatio, la tabla de potencia y empuje entre 0,7 y 5 UA, los radios de saturación y de apagado y un `Δv` acumulado (**comprueba** que la irradiancia está entre 1300 y 1450 W/m², que el empuje por kW es inferior a 75 mN/kW y la escala `1/r²`).

**Datos:** luminosidad (NSSDC) y UA (JPL) consultadas; `P₁`, `η`, `Isp`, topes del propulsor y masa **ilustrativos**. **Predice antes de ejecutar:** ¿qué empuje habrá a 5 UA? (cero: 400 W < 500 W.) **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Irradiancia calculada a 1 UA = L/(4 pi UA^2) = 1361.2 W/m^2
Empuje por kW = 2 eta/(g0 Isp) = 48.95 mN/kW (NASA SST SOA: generalmente < 75 mN/kW)
Datos ILUSTRATIVOS: P1 = 10000 W, eta = 0.6, Isp = 2500 s, Pmax = 4500 W, Pmin = 500 W, masa = 1000 kg
Radio de saturacion = 1.4907 UA ; radio de apagado = 4.4721 UA
 r [UA]   P [W]   P_util [W]   T [mN]   a [um/s^2]   dv en 30 d [m/s]
  0.70  20408.2     4500.0    220.26      220.26      570.911
  1.00  10000.0     4500.0    220.26      220.26      570.911
  1.50   4444.4     4444.4    217.54      217.54      563.862
  2.00   2500.0     2500.0    122.37      122.37      317.173
  3.00   1111.1     1111.1     54.38       54.38      140.966
  4.00    625.0      625.0     30.59       30.59       79.293
  5.00    400.0        0.0      0.00        0.00        0.000
Escala T r^2 constante entre 1,5 y 4 UA (zona sin saturar): desviacion relativa maxima = 0.0e+00
Dv acumulado (ILUSTRATIVO) al alejarse de 1 a 3 UA con velocidad radial 5 km/s, empuje siempre disponible: 8176.2 m/s
Pruebas superadas.
```

```bash
python programa/clases/B81/B81-C05-limitaciones-de-potencia-en-propulsion-electrica/potencia.py
```

**Límites:** paneles sin degradación y siempre perpendiculares al Sol; `η` constante; el `Δv` acumulado supone empuje siempre disponible y no es una trayectoria.

## 18. Errores frecuentes y cómo corregirlos

**Usar el empuje máximo a toda distancia.** Se corrige con 8.3.

**Tomar 75 mN/kW como límite físico.** Se corrige con la sección 11.

**Olvidar el apagado por potencia mínima.** Se corrige con 8.3.

**Presentar la nave ilustrativa como una misión.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué empuje esperabas a 3 UA y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **curva de empuje frente a distancia al Sol** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Calcula `P` y `T` con saturación | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas con unidades | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con una segunda vía | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo ilustrativo y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular la nave y sus topes como ilustrativos; no presentar 75 mN/kW como límite físico; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y sus datos son sintéticos o ilustrativos; ningún resultado describe una misión real ni sustituye a las herramientas de diseño y a la validación de una misión. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Una nave de 10 kW da `220 mN` hasta 1,49 UA, `54 mN` a 3 UA y nada a 5 UA: la potencia manda. Queda una pregunta: ¿hacia dónde hay que apuntar el empuje y los paneles a la vez?

**Glosario español–inglés.** irradiancia · *irradiance*; impulso específico · *specific impulse*; saturación · *saturation*; propulsión eléctrica · *electric propulsion*; luminosidad · *luminosity*.

**Continuidad.** [B81-C06](../B81-C06-restricciones-de-orientacion-del-empuje/CLASE.md) estudia las restricciones de orientación.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B81-C04 — Trayectorias espirales de bajo empuje](../B81-C04-trayectorias-espirales-de-bajo-empuje/CLASE.md) · [📚 Bloque B81](../../../tronco-comun/B81-optimizacion-de-trayectorias-y-diseno-robusto.md) · [Siguiente: B81-C06 — Restricciones de orientación del empuje →](../B81-C06-restricciones-de-orientacion-del-empuje/CLASE.md)
<!-- /nav -->
