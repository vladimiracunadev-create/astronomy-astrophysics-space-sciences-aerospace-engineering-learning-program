# B96-C05 — Estaciones de seguimiento

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B96](../../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) · [← Anterior: B96-C04 — Planificación de contactos](../B96-C04-planificacion-de-contactos/CLASE.md) · [Siguiente: B96-C06 — Telemetría operativa →](../../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md#b96-c06)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 5 del bloque B96. Nivel N3. Una **estación de seguimiento** mide dónde está el satélite (azimut, elevación, distancia) y cómo cambia la frecuencia que recibe (Doppler). Aquí calculas esas magnitudes durante la mejor pasada del día de C04 y las compruebas con tres relaciones independientes. Todo es **sintético**: la órbita, la estación y la portadora de 437,0 MHz son de ejemplo. Todos los datos son **sintéticos** salvo los que se rotulan como consultados.

## 2. Por qué esta clase existe

Para que una antena apunte y un receptor enganche, la estación debe conocer de antemano el azimut, la elevación y el corrimiento de frecuencia. La decisión central: **¿hacia dónde apuntar y qué frecuencia esperar en cada instante?**

## 3. Lo que podrás hacer al terminar

1. Calcular azimut, elevación y rango de una pasada.
2. Calcular la velocidad radial por diferencias centrales y el Doppler.
3. Verificar que el Doppler cruza cero en el punto de mínima distancia.
4. Verificar la cota `|Doppler| ≤ f₀ v/c`.
5. Verificar el rango del borde con la fórmula cerrada.
6. Separar lo consultado de lo sintético.

La evidencia es la **hoja de pasada con Doppler** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es el azimut?
2. ¿Qué es el efecto Doppler?
3. ¿Qué es la velocidad radial?
4. ¿Qué es el ENU?
5. ¿Qué es una diferencia central?

<details>
<summary>Ver respuestas</summary>

1. El ángulo horizontal medido desde el norte hacia el este. 2. El cambio de frecuencia por la velocidad relativa: `Δf = −f₀ v_r/c`. 3. La componente de la velocidad a lo largo de la línea de vista; positiva si se aleja. 4. El marco local este–norte–arriba de la estación. 5. `(f(t+h) − f(t−h))/(2h)`, de segundo orden.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

En la mejor pasada del día sintético (inicio 415 s, fin 840 s, elevación máxima 31,1°), el azimut va de 199° a 327°, la distancia mínima es 968,9 km y el Doppler de una portadora de 437,0 MHz pasa de +8,93 kHz a −8,95 kHz, con cruce por cero en t = 625 s, el mismo instante de la distancia mínima. La cota es de 11,06 kHz.

## 6. Vocabulario

**Estación de seguimiento:** antena, receptor y software que rastrean la nave. **Azimut/elevación:** ángulos de apuntamiento. **Rango:** distancia estación–satélite. **Doppler:** corrimiento de frecuencia. **Velocidad radial:** razón de cambio del rango. **ENU:** marco local este–norte–arriba.

## 7. Modelo mental

```mermaid
flowchart LR
    P["Posicion ECEF del satelite"] --> E["Marco local ENU"]
    E --> A["Azimut, elevacion, rango"]
    A --> V["Velocidad radial"]
    V --> D["Doppler"]
    D --> C["Comprobaciones: cruce, cota, borde"]
```

*Descripción textual:* la posición se expresa en el marco local de la estación; de ahí salen los ángulos y el rango; la derivada del rango da la velocidad radial y con ella el Doppler, que se verifica con tres relaciones.

Analogía: el Doppler es como la sirena de una ambulancia: más aguda al acercarse, más grave al alejarse. Límite: aquí el cambio es de decenas de kHz sobre 437 MHz, una parte en 50 000.

## 8. La explicación, paso a paso

### 8.1 Qué dicen las fuentes

El capítulo de la NASA (S1) trata los enlaces UHF, S, X y Ka y las estaciones con antenas que adquieren el satélite entre 5° y 10° de elevación. Las relaciones de geometría y de Doppler son estándar y las verifica el laboratorio; no se tomaron de una fuente concreta.

### 8.2 Azimut, elevación y rango

Con `d = r_sat − r_est` en ECEF y los vectores unitarios ENU `ê`, `n̂`, `û`: `E = d·ê`, `N = d·n̂`, `U = d·û`; `az = atan2(E, N)`, `el = asen(U/|d|)`, `ρ = |d|`.

### 8.3 Doppler

`v_r = dρ/dt` (diferencia central con ±0,5 s) y `Δf = −f₀ v_r/c`. Valores de la pasada:

| t (s) | az (°) | el (°) | ρ (km) | v_r (m/s) | Doppler (kHz) |
|---|---|---|---|---|---|
| 415 | 199,3 | 10,1 | 1 811,5 | −6 125 | +8,93 |
| 535 | 222,9 | 23,5 | 1 171,3 | −4 093 | +5,97 |
| 595 | 247,3 | 30,0 | 993,8 | −1 621 | +2,36 |
| 655 | 278,2 | 30,0 | 992,7 | +1 587 | −2,31 |
| 775 | 317,5 | 16,2 | 1 457,7 | +5 421 | −7,90 |
| 835 | 326,5 | 10,1 | 1 805,7 | +6 100 | −8,89 |

### 8.4 Tres verificaciones

(1) El Doppler cruza cero a 625 s, igual que la distancia mínima de 968,9 km. (2) `|Δf| ≤ f₀ v/c = 11,06 kHz` con `v = 7,585 km/s`. (3) El rango del borde (1 811,45 km) coincide con la fórmula cerrada a 0,5 km. El receptor debe barrer o seguir un corrimiento de `17,88 kHz`.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `az, el` | azimut y elevación | ° | 199–327; 10–31 |
| `ρ` | distancia | km | 969 a 1 836 |
| `v_r` | velocidad radial | m/s | ±6 100 |
| `f₀` | portadora | MHz | 437,0 (sintética) |
| `Δf` | Doppler | kHz | +8,93 a −8,95 |

## 10. Convenciones y referencias

Marco ECEF con ENU local de la estación (40° N, 0° E); azimut desde el norte hacia el este; Doppler `−f₀ v_r/c` con `c = 299 792,458 km/s`. Datos de órbita y portadora **sintéticos**. Tolerancias: cruce de Doppler y distancia mínima a ≤ 10 s; borde frente a fórmula `< 0,5 km`; cota exacta.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA, «Ground Data Systems and Mission Operations», en State-of-the-Art of Small Spacecraft Technology — https://www.nasa.gov/smallsat-institute/sst-soa/ground-data-systems-and-mission-operations/ (consultada 2026-11-10; leídos los primeros 100 000 caracteres de 215 453) | capítulo (parte inicial) | un centro de operaciones de misión (MOC) comanda la nave y un centro de operaciones científicas (SOC) genera productos; enlaces directos a la Tierra frente a relevos; bandas UHF, S, X y Ka; la licencia tarda meses; las antenas suelen adquirir el satélite con 5–10° de elevación; margen típico de 3 dB para retorno de datos en LEO a 1 500 km de distancia oblicua | Consultada (parte del capítulo) |
| — | Libros de texto de operaciones de misión, comunicaciones espaciales y mecánica orbital (p. ej., Wertz y Larson, Montenbruck y Gill, Vallado) | — | — | No consultada |
| — | Relaciones y algoritmos estándar usados por el laboratorio (geometría ENU, diferencias centrales y Doppler no relativista) | — | los verifica el laboratorio con una segunda vía o con pruebas | No consultada en una fuente concreta |

Límites: sin efectos relativistas, refracción ni deriva del oscilador; el Doppler es de primer orden. Lo simulado no se presenta como dato de vuelo ni como medición.

## 12. Cómo ver los resultados

| Magnitud | Valor |
|---|---|
| Distancia mínima | 968,9 km (t = 625 s) |
| Doppler máximo / mínimo | +8,93 / −8,95 kHz |
| Variación total | 17,88 kHz |
| Cota `f₀ v/c` | 11,06 kHz |

Descripción larga: el Doppler cae casi linealmente de +9 a −9 kHz, con la pendiente más fuerte en el punto de máximo acercamiento.

## 13. Ejemplo trabajado

**Paso 1 · Geometría.** `ρ(415 s) = 1 811,5 km`, `el = 10,1°`.

**Paso 2 · Velocidad radial.** `−6 125 m/s` (se acerca).

**Paso 3 · Doppler.** `−437×10⁶ × (−6,125)/299 792,458 = +8,93 kHz`.

**Paso 4 · Cruce.** `0` en 625 s.

**Paso 5 · Cota.** `11,06 kHz ≥ 8,95 kHz`.

## 14. Distintas formas de describir el problema

**Por simulación:** tabla de la pasada (esta clase). **Por control:** velocidades de la antena (C28). **Por enlace:** potencia recibida (C27). **Por diagnóstico:** residuos de frecuencia (C29).

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula el Doppler de v_r = −5 000 m/s a 437 MHz.

<details><summary>Solución comentada</summary>

`437×10⁶ × 5/299 792,458 = 7,29 kHz`.
</details>

**Ejercicio 2 · con una pista.** ¿Qué signo tiene el Doppler cuando el satélite se aleja?

<details><summary>Solución comentada</summary>

Negativo: la frecuencia recibida es menor.
</details>

**Ejercicio 3 · casi autónomo.** Calcula `f₀ v/c` para `f₀ = 2 200 MHz` y `v = 7,585 km/s`.

<details><summary>Solución comentada</summary>

`2,2×10⁹ × 7,585/299 792,458 = 55,7 kHz`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** ¿Cuánto cambia el rango entre 415 y 535 s?

<details><summary>Solución comentada</summary>

`1 811,5 − 1 171,3 = 640,2 km` (acercándose).
</details>

**Ejercicio 5 · autónomo.** ¿Qué relación tiene el azimut de 199° con la dirección de aparición?

<details><summary>Solución comentada</summary>

Es sur-suroeste: el satélite aparece al sur y sale al noroeste.
</details>

**Ejercicio 6 · autónomo.** ¿Cuántos kHz cambia el Doppler entre 595 s y 655 s?

<details><summary>Solución comentada</summary>

`2,36 − (−2,31) = 4,67 kHz` en 60 s: la pendiente máxima.
</details>

**Ejercicio 7 · autónomo.** Convierte 17,88 kHz a ppm de 437 MHz.

<details><summary>Solución comentada</summary>

`17,88×10³/437×10⁶ = 40,9 ppm`.
</details>

**Ejercicio 8 · autónomo.** ¿Por qué se usa una diferencia central y no una diferencia hacia adelante?

<details><summary>Solución comentada</summary>

Tiene error de segundo orden y no sesga la velocidad en el instante evaluado.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un colega usa 437 MHz y el Doppler de esta clase para su satélite. ¿Qué respondes?

<details><summary>Solución comentada</summary>

Los datos son sintéticos; debe usar efemérides y frecuencias coordinadas propias.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Qué pasa con el Doppler si la portadora se duplica?

<details><summary>Solución comentada</summary>

Se duplica: `Δf` es proporcional a `f₀`.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Cómo usarías la tabla para programar un receptor?

<details><summary>Solución comentada</summary>

Barrer ±9 kHz alrededor de la nominal o corregir con la predicción por tiempo.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *hoja de pasada con Doppler*: ángulos, rango, velocidad radial, Doppler, las tres verificaciones y lista de lo consultado, sintético y no consultado.

<details><summary>Solución comentada</summary>

Secciones 8.2–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: azimut, elevación y Doppler

El script [pasada_con_doppler.py](pasada_con_doppler.py) calcula azimut, elevación, rango, velocidad radial y Doppler de la mejor pasada; usa la biblioteca común [b96_comun.py](../b96_comun.py); **comprueba** el cruce del Doppler, la cota y el rango del borde.

**Datos:** órbita, estación y portadora **sintéticas**. **Predice antes de ejecutar:** ¿en qué instante cruza cero el Doppler? (en la distancia mínima, 625 s). **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9
Datos SINTETICOS: orbita circular de 550 km, i = 97.6 grados; estacion en 40 N, 0 E; portadora 437.0 MHz; c = 299792.458 km/s
Pasada elegida: inicio = 415 s ; fin = 840 s ; elevacion maxima = 31.1 grados
t[s]   az[gr]  el[gr]  d[km]   v_r[m/s]  Doppler[kHz]
   415   199.3    10.1  1811.5   -6125.3      8.93
   475   208.2    16.1  1462.1   -5444.9      7.94
   535   222.9    23.5  1171.3   -4093.1      5.97
   595   247.3    30.0   993.8   -1621.0      2.36
   655   278.2    30.0   992.7    1587.2     -2.31
   715   302.7    23.5  1168.5    4066.4     -5.93
   775   317.5    16.2  1457.7    5421.3     -7.90
   835   326.5    10.1  1805.7    6100.3     -8.89
   840   327.0     9.7  1836.3    6138.7     -8.95
Doppler: maximo = 8.93 kHz ; minimo = -8.95 kHz ; |variacion| = 17.88 kHz
Distancia minima = 968.9 km en t = 625 s ; cruce de Doppler en t = 625 s
Cota |Doppler| <= f0 v/c = 11.06 kHz (v = 7.585 km/s)
Distancia en el borde: simulada = 1811.45 km ; formula = 1811.45 km
Pruebas superadas.
```

```bash
python programa/clases/B96/B96-C05-estaciones-de-seguimiento/pasada_con_doppler.py
```

**Límites:** órbita circular, Tierra esférica, Doppler de primer orden, sin deriva del oscilador.

## 18. Errores frecuentes y cómo corregirlos

**Invertir el signo del Doppler.** Positivo al acercarse (8.3)

**Medir el azimut desde el este.** Desde el norte hacia el este (8.2)

**Tomar la portadora como asignada.** Revisa la sección 10

## 19. Cómo sabrás que vas bien

Tras 8.3: ¿qué signo tiene el Doppler a mitad de pasada? Si dudas, repasa el ejercicio 2. Tras el laboratorio: ¿qué comprueba la cota? (ver sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **hoja de pasada con Doppler** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Explica el método y su dominio | Explica los límites y las alternativas |
| Cálculo | Sin unidades | Con errores | Resultados con unidades y comprobados | Resuelve casos nuevos |
| Numérico | Sin comprobar | Un caso | Verifica con una segunda vía en varios casos | Interpreta las diferencias y los fallos |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo sintético y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular los datos como sintéticos; comprobar cada resultado con una segunda vía; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y los datos son sintéticos; ningún resultado describe una misión real, certifica conformidad con una norma ni sustituye la revisión de especialistas.  Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

La mejor pasada sintética va de 199° a 327° de azimut, tiene 968,9 km de distancia mínima y un Doppler de +8,93 a −8,95 kHz. Queda una pregunta: ¿qué ve la sala de control en la telemetría que llega?

**Glosario español–inglés.** estación de seguimiento · *tracking station*; azimut · *azimuth*; efecto Doppler · *Doppler shift*; velocidad radial · *range rate*; marco local · *topocentric frame*.

**Continuidad.** [B96-C06](../B96-C06-telemetria-operativa/CLASE.md) trata la telemetría operativa.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B96-C04 — Planificación de contactos](../B96-C04-planificacion-de-contactos/CLASE.md) · [📚 Bloque B96](../../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md) · [Siguiente: B96-C06 — Telemetría operativa →](../../../tronco-comun/B96-control-y-operacion-de-misiones-espaciales.md#b96-c06)
<!-- /nav -->
