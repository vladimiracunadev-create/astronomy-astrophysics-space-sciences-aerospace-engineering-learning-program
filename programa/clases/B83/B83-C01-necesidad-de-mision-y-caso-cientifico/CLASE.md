# B83-C01 — Necesidad de misión y caso científico

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B83](../../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) · [← Anterior: B82-C07 — Benchmark entre solucionadores de Lambert](../../B82/B82-C07-benchmark-entre-solucionadores-de-lambert/CLASE.md) · [Siguiente: B83-C02 — Partes interesadas y usuarios →](../B83-C02-partes-interesadas-y-usuarios/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 1 del bloque B83. Nivel N3. Toda misión nace de una pregunta que los instrumentos existentes no responden. Aquí conviertes un objetivo científico en un **requisito de medición** (qué hay que medir, con qué resolución y cobertura) y eliges entre objetivos competidores con una matriz ponderada. La misión de ejemplo, **ESTRELLA-S** (un microsatélite de observación a 550 km), es **sintética**: no es una misión real. La necesidad de misión es el primer paso del ciclo de vida descrito en el *NASA Systems Engineering Handbook* (S1).

## 2. Por qué esta clase existe

Un equipo sabe que quiere «mirar la costa» pero no cuánto debe resolver ni qué objetivo merece el presupuesto. La decisión central: **¿qué requisito de medición se deduce de la pregunta científica y qué objetivo conviene perseguir primero?** Sin esa traducción, los requisitos posteriores (C04) se escriben sobre arena.

## 3. Lo que podrás hacer al terminar

1. Distinguir una necesidad de misión de una solución técnica.
2. Derivar la resolución en tierra (GSD) a partir del tamaño del rasgo con un criterio de muestreo explícito.
3. Calcular la apertura mínima por el límite de difracción de Rayleigh y verificarla por una segunda vía.
4. Construir una matriz ponderada de objetivos con pesos y puntajes rotulados.
5. Medir la sensibilidad del ganador a los pesos con una simulación de semilla fija.
6. Separar lo consultado (radio terrestre) de lo sintético (rasgo, pesos, puntajes).

La evidencia es la **ficha de necesidad de misión con requisito de medición derivado** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es el límite de difracción de una apertura circular?
2. ¿Qué es el GSD?
3. ¿Qué relación hay entre ángulo, altura y distancia en tierra?
4. ¿Qué es un peso en una suma ponderada?
5. ¿Qué es una simulación con semilla fija?

<details>
<summary>Ver respuestas</summary>

1. El ángulo mínimo resoluble `θ ≈ 1,22 λ/D`. 2. La distancia en tierra que corresponde a un píxel (*ground sample distance*). 3. `GSD = θ·h` al nadir, con `θ` en radianes. 4. Un factor de importancia; los pesos suman 1. 5. Una simulación aleatoria reproducible: mismo resultado en cada ejecución.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

El equipo de ESTRELLA-S (sintético) quiere observar rasgos de **10 m** en una franja de **30 km** desde **550 km** de altura con luz de **550 nm**. Cuatro objetivos compiten: O1 cobertura de cultivos, O2 cambio de costa, O3 hielo estacional y O4 calidad del aire. Los puntajes (0–10) en tres criterios —valor científico, madurez de la medición y costo inverso— son **inventados** para el ejemplo. Resultado del laboratorio: GSD requerido 5,00 m, apertura mínima 7,38 cm; el mejor objetivo es **O2 Cambio de costa**.

## 6. Vocabulario

Una **necesidad de misión** es la carencia que justifica el proyecto, expresada sin elegir la solución. El **caso científico** argumenta por qué responderla aporta conocimiento. Un **requisito de medición** traduce el objetivo a cantidades medibles (resolución, cobertura, precisión, cadencia). El **GSD** es la resolución en tierra. El **criterio de muestreo** usado aquí (supuesto del ejemplo) pide al menos dos píxeles por rasgo: `GSD ≤ rasgo/2`. El **límite de difracción de Rayleigh** es `θ = 1,22 λ/D`. Una **matriz de decisión ponderada** puntúa alternativas con pesos de criterio.

## 7. Modelo mental: de la pregunta a la medición

```mermaid
flowchart LR
    P["Pregunta cientifica"] --> O["Objetivo medible"]
    O --> R["Requisito de medicion"]
    R --> A["Apertura, altura, franja"]
    O --> M["Matriz ponderada"]
    M --> S["Sensibilidad a los pesos"]
    A --> F["Ficha de necesidad"]
    S --> F
```

*Descripción textual:* de la pregunta se pasa a un objetivo medible; de él salen el requisito de medición (que fija apertura, altura y franja) y la matriz ponderada de objetivos con su sensibilidad; ambos alimentan la ficha de necesidad.

Analogía: elegir una cámara para fotografiar hormigas o elefantes: el tamaño de lo que quieres ver fija la lente. Límite: la analogía no dice cuánto vale cada fotografía; eso lo decide la matriz de objetivos y sus pesos.

## 8. La explicación, paso a paso

### 8.1 De rasgo a resolución

Si el rasgo mide `d = 10 m` y se exigen dos píxeles por rasgo, `GSD ≤ d/2 = 5,00 m`. Con una franja de 30 km hacen falta `30 000/5,00 = 6000` píxeles a través.

### 8.2 De resolución a apertura

Al nadir `GSD = θ·h` y `θ = 1,22 λ/D`; despejando, `D = 1,22 λ h / GSD = 7,38 cm` (con `λ = 550` nm y `h = 550` km). El valor es un **mínimo por difracción**: no incluye aberraciones, ruido ni el movimiento de la imagen (C09–C11).

### 8.3 Elegir el objetivo

Con pesos `(0,5; 0,3; 0,2)` los puntajes ponderados son O1 7,00, O2 7,30, O3 6,70 y O4 5,90. Gana **O2 Cambio de costa**. Con 10 000 pesos aleatorios alrededor de esos valores, O2 queda primero en 84,3 % de los casos y O3 en 15,7 %: el orden es sensible, así que la ficha debe decirlo.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `d` | tamaño del rasgo | m | 10 (sintético) |
| `GSD` | resolución en tierra | m | 5,00 |
| `λ` | longitud de onda | nm | 550 |
| `h` | altura de la órbita | km | 550 (sintético) |
| `D` | apertura mínima | cm | 7,38 |
| `θ` | resolución angular | µrad | 9,091 |

## 10. Convenciones y referencias

Radio terrestre de NASA/NSSDC (S8). Sistema de referencia: geometría al nadir sobre Tierra esférica; sin atmósfera ni inclinación. Unidades SI con km y cm donde se indica. Modelo: difracción de Rayleigh y criterio de muestreo de dos píxeles por rasgo (supuesto). Tolerancia: la segunda vía coincide a `10⁻⁹`. Rasgo, pesos y puntajes **sintéticos**.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA, *NASA Systems Engineering Handbook* (NASA/SP-6105), página principal — https://www.nasa.gov/reference/systems-engineering-handbook/ (consultada 2026-11-10) | página principal; ciclo de vida del proyecto | el manual describe el ciclo de vida de un proyecto y sus procesos de diseño; la necesidad de misión es el punto de partida | Consultada |
| S8 | NASA/NSSDC, Earth Fact Sheet — https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html (consultada 2026-11-10) | ficha de la Tierra | radio ecuatorial 6378,137 km usado en la biblioteca común | Consultada |
| ECSS | ECSS-E-ST-10C, ECSS-M-ST-40C, ECSS-Q-ST-30-02C, ECSS-Q-ST-40-12C y demás estándares (ecss.nl) | — | — | No consultada: la página de estándares no mostró los documentos |
| — | ISO/IEC/IEEE 15288, INCOSE, SysML, MIL-STD-1629, IEC 60812 e IEC 61025 | — | — | No consultada |
| — | Relaciones matemáticas estándar usadas en el laboratorio (AHP, rutas críticas, ley de Stefan, confiabilidad exponencial, cortes mínimos, ecuación del cohete) | — | — | No consultada en una fuente concreta: las verifica el laboratorio por una segunda vía |

Límites: la fórmula de Rayleigh y el criterio de dos píxeles son relaciones estándar que el laboratorio verifica por una segunda vía; no se consultaron en una fuente concreta. No se infiere nada de una misión real.

## 12. Cómo ver el resultado de la ficha

| Magnitud | Valor |
|---|---|
| GSD requerido | 5,00 m |
| Apertura mínima | 7,38 cm |
| Píxeles por franja | 6000 |
| Objetivo ganador | O2 Cambio de costa |
| Estabilidad del ganador | 84,3 % de 10 000 pesos |

Descripción larga: el puntaje de O2 supera al de O1 y O3 con los pesos de ejemplo, pero un cambio de pesos puede dar la primera plaza a O3 en cerca de una de cada seis simulaciones; por eso se informa la frecuencia.

## 13. Ejemplo trabajado: el requisito de medición de ESTRELLA-S

**Paso 1 · Rasgo.** El rasgo de interés mide 10 m.

**Paso 2 · Muestreo.** Dos píxeles por rasgo: `GSD ≤ 5 m`.

**Paso 3 · Difracción.** `θ = GSD/h = 5 / 550 000 = 9,09 µrad`.

**Paso 4 · Apertura.** `D = 1,22 · 550 nm / 9,09 µrad = 7,38 cm`.

**Paso 5 · Comprobación.** `GSD = θ h = 5,000000 m`, igual al requerido a `10⁻⁹`.

## 14. Distintas formas de abordar el problema

**Por la matriz ponderada** (esta clase). **Por la utilidad esperada:** se asigna una probabilidad de éxito a cada objetivo (C16). **Por el valor de la información:** se compara cuánto se aprende por unidad de costo. El laboratorio calcula el puntaje de dos maneras (producto matricial y bucles) y coinciden a `10⁻¹²`.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula el GSD requerido para un rasgo de 20 m con dos píxeles por rasgo. *Pasos:* divide el rasgo entre 2.

<details><summary>Solución comentada</summary>

`GSD = 20/2 = 10 m`.
</details>

**Ejercicio 2 · con una pista.** Halla la apertura mínima para `GSD = 10 m`, `h = 550 km`, `λ = 550 nm`. *Pista:* `D = 1,22 λ h/GSD`.

<details><summary>Solución comentada</summary>

`D = 1,22 · 5,5×10⁻⁷ · 5,5×10⁵ / 10 = 0,0369 m = 3,69 cm`, la mitad de la de 5 m.
</details>

**Ejercicio 3 · casi autónomo.** Con pesos `(0,5; 0,3; 0,2)` y puntajes `(7, 8, 7)`, ¿cuál es el puntaje ponderado?

<details><summary>Solución comentada</summary>

`3,5 + 2,4 + 1,4 = 7,3` (el de O2).
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Si `h` baja a 400 km manteniendo `GSD = 5 m`, ¿cuál es la nueva apertura mínima?

<details><summary>Solución comentada</summary>

`D ∝ h`: `7,38 · 400/550 = 5,37 cm`.
</details>

**Ejercicio 5 · autónomo.** ¿Cuántos píxeles por franja hacen falta para una franja de 60 km con `GSD = 5 m`?

<details><summary>Solución comentada</summary>

`60 000/5 = 12 000` píxeles.
</details>

**Ejercicio 6 · autónomo.** Con `D = 10 cm`, ¿cuál es el mejor GSD por difracción a 550 km y 550 nm?

<details><summary>Solución comentada</summary>

`GSD = 1,22 · 5,5×10⁻⁷ · 5,5×10⁵/0,1 = 3,69 m`.
</details>

**Ejercicio 7 · autónomo.** Explica por qué un objetivo con puntaje alto puede no ser conveniente aunque gane.

<details><summary>Solución comentada</summary>

Porque el orden es sensible a los pesos: si la frecuencia de victoria es baja, la decisión es frágil y hay que discutir los pesos con las partes interesadas (C02).
</details>

**Ejercicio 8 · autónomo.** ¿Qué pasa con el requisito de apertura si el supuesto sube a tres píxeles por rasgo?

<details><summary>Solución comentada</summary>

`GSD = 10/3 = 3,33 m` y `D = 7,38 · 5/3,33 = 11,07 cm`: el supuesto de muestreo cambia el instrumento.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un colega dice que 7,38 cm es la apertura de la cámara de ESTRELLA-S. ¿Es válido?

<details><summary>Solución comentada</summary>

No: es un mínimo por difracción con datos sintéticos; faltan aberraciones, ruido, movimiento y márgenes, y la misión no es real.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** Cambia la longitud de onda a 850 nm (infrarrojo cercano). ¿Qué ocurre con `D`?

<details><summary>Solución comentada</summary>

`D ∝ λ`: `7,38 · 850/550 = 11,40 cm`; resolver con infrarrojo exige una apertura mayor.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Cómo cambia la matriz si se añade un criterio de riesgo de calendario con peso 0,2 y los demás se reescalan?

<details><summary>Solución comentada</summary>

Los pesos deben volver a sumar 1 (`0,4; 0,24; 0,16; 0,2`) y los puntajes se recalculan; conviene repetir la sensibilidad.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de necesidad de misión*: objetivo ganador con su frecuencia, requisito de medición (GSD, apertura, píxeles), supuestos y lista de qué es consultado y sintético.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.3 y la salida del laboratorio; incluye la frecuencia de 84,3 % y los supuestos de muestreo.
</details>

## 17. Laboratorio: del objetivo científico al requisito de medición

El script [necesidad_de_mision.py](necesidad_de_mision.py) calcula el requisito de medición, lo verifica por una segunda vía y puntúa los objetivos con una simulación de sensibilidad (**comprueba** `GSD = θ·h` a `10⁻⁹`, el puntaje por dos vías a `10⁻¹²` y que las frecuencias sumen 100 %). Usa la biblioteca común [sistemas_comun.py](../sistemas_comun.py) del bloque.

**Datos:** constante del radio terrestre de NASA/NSSDC (consultada el 2026-11-10); rasgo, pesos y puntajes **sintéticos**. **Predice antes de ejecutar:** ¿qué objetivo gana con los pesos de ejemplo y qué fracción de las simulaciones lo confirma? (O2; alrededor de cuatro de cada cinco.) **Ejecución del 2026-11-10 (Python 3.12.9 | numpy 2.4.4):**

```text
Python 3.12.9 | numpy 2.4.4
Datos SINTETICOS: rasgo 10 m, ancho de franja 30 km, h = 550 km, lambda = 550 nm; constantes NASA/NSSDC (2026-11-10)
GSD requerido = rasgo/2 = 5.00 m ; apertura minima D = 7.38 cm ; theta = 9.091 urad
segunda via: GSD = theta*h = 5.000000 m ; pixeles por franja = 6000
Puntaje ponderado (pesos 0.5/0.3/0.2):
  O1 Cobertura de cultivos     7.00
  O2 Cambio de costa           7.30
  O3 Hielo estacional          6.70
  O4 Calidad del aire          5.90
Ganador: O2 Cambio de costa
Sensibilidad (10000 pesos Dirichlet, semilla 83001), frecuencia de ser el primero [%]:
  O1 Cobertura de cultivos     0.0
  O2 Cambio de costa           84.3
  O3 Hielo estacional          15.7
  O4 Calidad del aire          0.0
Pruebas superadas.
```

```bash
python programa/clases/B83/B83-C01-necesidad-de-mision-y-caso-cientifico/necesidad_de_mision.py
```

**Límites:** difracción sin aberraciones ni ruido; criterio de muestreo de ejemplo; puntajes inventados; no hay una misión real detrás.

## 18. Errores frecuentes y cómo corregirlos

**Presentar la solución como necesidad.** Escribe la carencia («observar rasgos de 10 m») y no «un telescopio de 7 cm»

**Olvidar el supuesto de muestreo.** Declara cuántos píxeles por rasgo usas; cambia el resultado (ejercicio 8)

**Dar el ganador sin sensibilidad.** Informa la frecuencia de victoria ante cambios de pesos

## 19. Cómo sabrás que vas bien

Tras 8.1: ¿cuántos píxeles por franja esperabas? Tras 8.3: ¿qué fracción de simulaciones confirma al ganador? Si dudas, repasa el ejemplo 13.

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de necesidad de misión con requisito de medición derivado** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Explica el método y su dominio | Explica los límites y las alternativas |
| Cálculo | Sin unidades | Con errores | Resultados con unidades y comprobados | Resuelve casos nuevos |
| Numérico | Sin comprobar | Un caso | Verifica por una segunda vía en varios casos | Interpreta las diferencias y los fallos |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo sintético y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular los datos como sintéticos; verificar el resultado por una segunda vía; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y los datos son sintéticos; ningún resultado describe una misión real, certifica una seguridad ni sustituye a los estándares vigentes y a la revisión de especialistas.  Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Con rasgo de 10 m, ESTRELLA-S necesita al menos 7,38 cm de apertura y 6000 píxeles por franja; O2 gana, pero la decisión es sensible a los pesos. Queda una pregunta: ¿quién decide los pesos? (C02).

**Glosario español–inglés.** necesidad de misión · *mission need*; caso científico · *science case*; resolución en tierra · *ground sample distance*; límite de difracción · *diffraction limit*; matriz de decisión · *decision matrix*.

**Continuidad.** [B83-C02](../B83-C02-partes-interesadas-y-usuarios/CLASE.md) identifica a quienes fijan los pesos y las necesidades.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B82-C07 — Benchmark entre solucionadores de Lambert](../../B82/B82-C07-benchmark-entre-solucionadores-de-lambert/CLASE.md) · [📚 Bloque B83](../../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) · [Siguiente: B83-C02 — Partes interesadas y usuarios →](../B83-C02-partes-interesadas-y-usuarios/CLASE.md)
<!-- /nav -->
