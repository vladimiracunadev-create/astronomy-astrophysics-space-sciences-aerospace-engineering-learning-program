# B05-C04 — Leyes del movimiento de Newton

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B05](../../../tronco-comun/B05-fisica-fundamental-para-el-espacio.md) · [← Anterior: B05-C03 — Movimiento rectilíneo y circular](../B05-C03-movimiento-rectilineo-y-circular/CLASE.md) · [Siguiente: B05-C05 — Diagramas de cuerpo libre →](../../../tronco-comun/B05-fisica-fundamental-para-el-espacio.md#b05-c05)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Cuarta clase de B05 y cierre de su primer tramo (descripción del movimiento). Hasta aquí describiste cómo se mueve un cuerpo; ahora preguntas **por qué**. Nivel N1. Necesitas vectores como pares de componentes y las fórmulas de C02 y C03. No verás todavía diagramas de fuerzas en detalle (C05), energía (C06) ni la ley de gravitación (C10).

## 2. Por qué esta clase existe

Un satélite no tiene motor encendido y aun así gira. Una nave en el espacio vacío mantiene su velocidad sin esfuerzo. La pregunta motivadora es: **¿qué relación hay entre las fuerzas que actúan sobre un cuerpo y el movimiento que resulta?** La decisión central es plantear, para cada problema, un marco, un cuerpo aislado mentalmente y la suma de fuerzas que actúan sobre él.

Las leyes de Newton son el motor de cálculo de toda la mecánica del bloque: de ellas salen la energía, el momento y la gravitación en las clases siguientes.

## 3. Lo que podrás hacer al terminar

1. Enunciar las tres leyes con sus condiciones de aplicabilidad.
2. Aplicar `ΣF = m a` en forma vectorial a un cuerpo.
3. Distinguir masa, peso y fuerza gravitatoria.
4. Identificar pares de acción y reacción y ver que actúan en cuerpos distintos.
5. Explicar la ingravidez orbital como caída libre.
6. Integrar numéricamente `F = m a` y reconocer cuándo el método introduce error.

La evidencia es el **planteamiento de dinámica** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué aceleración tiene un cuerpo que pasa de 0 a 20 m/s en 4 s?
2. ¿Qué es la aceleración centrípeta de un círculo de radio 100 m a 10 m/s?
3. ¿Qué dimensión tiene el newton? (C01)
4. Suma los vectores `(3, 4)` y `(−1, 2)`.
5. ¿Qué significa «respecto de un marco»?

<details>
<summary>Ver respuestas</summary>

1. 5 m/s². 2. 1 m/s². 3. `M L T⁻²`. 4. `(2, 6)`. 5. Que la posición y la velocidad se miden desde un origen y unos ejes declarados.
</details>

Con cuatro o cinco aciertos, sigue; con menos, repasa C01–C03.

## 5. Un caso real: caer sin llegar al suelo

La ISS pesa unos 419 725 kg según NASA, da 16 órbitas al día y viaja a unos 5 mi/s (S4). Cada astronauta flota, pero la gravedad a esa altura ronda el 88 % de la de la superficie (C02). La explicación newtoniana: la estación y los astronautas **caen juntos** hacia la Tierra con la misma aceleración y, como avanzan lateralmente tan rápido, el suelo se curva por debajo a la misma tasa. Límite: S4 es divulgativa; la cifra de la masa cambia con cada modificación de la estación.

## 6. Vocabulario

La **fuerza** `F` es una interacción que cambia el estado de movimiento; es un vector, con unidad newton (N). La **masa inercial** `m` mide la resistencia de un cuerpo a cambiar su velocidad (kg). La **fuerza neta** `ΣF` es la suma vectorial de todas las fuerzas sobre el cuerpo. Un **marco inercial** es aquel en que se cumple la primera ley. El **peso** es la fuerza gravitatoria sobre un cuerpo, `W = m g`; la masa no cambia con el lugar, el peso sí. Una **caída libre** es un movimiento en que solo actúa la gravedad. Un **par acción–reacción** son dos fuerzas iguales y opuestas entre dos cuerpos diferentes.

## 7. Modelo mental: causa y efecto en cuatro pasos

La mecánica newtoniana es una receta repetible: eliges el cuerpo, enumeras lo que lo empuja o tira, sumas y obtienes la aceleración; luego integras en el tiempo para obtener velocidad y posición.

```mermaid
flowchart LR
    A["Elegir cuerpo y marco inercial"] --> B["Listar fuerzas sobre ese cuerpo"]
    B --> C["Suma vectorial ΣF"]
    C --> D["a = ΣF / m"]
    D --> E["Integrar: v(t), r(t)"]
    E --> F["Comprobar unidades y límites"]
```

*Descripción textual:* seis cajas en cadena; del cuerpo y el marco, a las fuerzas, a su suma, a la aceleración dividiendo por la masa, a la integración en el tiempo y a la comprobación de unidades y límites.

Una analogía: un empujón a un carrito de supermercado: mismo empuje, más carga, menos aceleración. Su límite: en un carrito el rozamiento detiene el movimiento; en el espacio no lo hay y la velocidad se mantiene.

## 8. La explicación, paso a paso

### 8.1 Primera ley: la inercia

Un cuerpo sobre el que la fuerza neta es cero conserva su velocidad (reposo o recta con rapidez constante). Eso solo ocurre en un **marco inercial**; en un marco que gira o acelera aparecen movimientos sin causa aparente. Para el satélite ideal usamos un marco geocéntrico sin rotación, adecuado durante unas pocas órbitas.

### 8.2 Segunda ley: `ΣF = m a`

La aceleración tiene la dirección de la fuerza neta y módulo `|ΣF|/m`. Con unidades del SI, 1 N produce 1 m/s² en 1 kg. Es una ley **vectorial**: se aplica por componentes. Se cumple con masa constante y velocidades mucho menores que `c`.

### 8.3 Tercera ley: acción y reacción

Si el cuerpo A empuja a B con una fuerza `F`, B empuja a A con `−F`. Las dos fuerzas son de la misma clase y actúan sobre cuerpos diferentes, por eso **no se anulan** al calcular la aceleración de un solo cuerpo. Un cohete funciona así: empuja gases hacia atrás y los gases lo empujan hacia delante (C08 lo cuantifica con el momento).

### 8.4 Peso, masa y caída libre

La masa es propiedad del cuerpo; el peso depende de dónde esté. Con `g_n = 9,806 65 m/s²` (S2), 1000 kg pesan 9806,65 N. A 400 km de altura, la fuerza gravitatoria sobre 1000 kg es `m GM/r² = 8675,9 N`. Si no hay otra fuerza, `a = F/m = 8,676 m/s²` hacia el centro: eso es justo la aceleración centrípeta de C03. Gravedad y movimiento circular se corresponden: la órbita es una caída continua alrededor de la Tierra.

### 8.5 Integración numérica y sus límites

Cuando `F` cambia con la posición (como la gravedad), se calcula paso a paso: con la posición se obtiene `a`, con `a` se actualiza `v`, con `v` la posición. El método más simple (Euler) acumula error y, para una órbita, la espiral se abre; el esquema velocity-Verlet, que alterna medios pasos de velocidad, conserva mucho mejor la forma. Lo verás en la sección 17.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Magnitud | Dimensión | Unidad SI | Valor o nota |
|---|---|---|---|---|
| `F`, `ΣF` | fuerza, fuerza neta | M L T⁻² | N | — |
| `m` | masa | M | kg | — |
| `a` | aceleración | L T⁻² | m/s² | `a = ΣF/m` |
| `W` | peso | M L T⁻² | N | `W = m g` |
| `g_n` | aceleración estándar | L T⁻² | m/s² | 9,806 65 (S2) |
| `G` | constante de gravitación | M⁻¹ L³ T⁻² | m³ kg⁻¹ s⁻² | 6,674 30 × 10⁻¹¹ ± 0,000 15 × 10⁻¹¹ (S3, CODATA 2022) |
| `GM` | parámetro gravitatorio | L³ T⁻² | m³/s² | 3,9860 × 10¹⁴ (S1) |

## 10. Convenciones y referencias

Marco geocéntrico no rotante; masa del satélite constante en 1000 kg (dato sintético); solo se considera la gravedad de la Tierra tratada como masa puntual. Un cálculo cruzado: `G × M_Tierra = 6,674 30 × 10⁻¹¹ × 5,9722 × 10²⁴ = 3,9860 × 10¹⁴ m³/s²`, que coincide con el `GM` de S1 (la masa de la Tierra también viene de S1).

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA NSSDC, *Earth Fact Sheet* (act. 15-nov-2024) | https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html | Masa 5,9722 × 10²⁴ kg; GM = 0,39860 × 10⁶ km³/s²; radio ecuatorial 6378,137 km | Página consultada el 2026-11-05 |
| S2 | NIST, CODATA 2022, «standard acceleration of gravity» | https://physics.nist.gov/cgi-bin/cuu/Value?gn | `g_n = 9,806 65 m/s²` exacto | Página consultada el 2026-11-05 |
| S3 | NIST, CODATA 2022, «Newtonian constant of gravitation» | https://physics.nist.gov/cgi-bin/cuu/Value?bg | `G = 6,674 30(15) × 10⁻¹¹ m³ kg⁻¹ s⁻²` | Página consultada el 2026-11-05 |
| S4 | NASA, «Space Station Facts and Figures» | https://www.nasa.gov/international-space-station/space-station-facts-and-figures/ | Masa 419 725 kg; 16 órbitas diarias; ~5 mi/s | Página consultada el 2026-11-05 |

Límites: no se consultó una fuente primaria histórica (los *Principia*); la clase no afirma nada sobre su contexto histórico más allá de nombrar las leyes. Las leyes se enuncian como teoría clásica válida en su dominio.

## 12. Cómo ver las fuerzas

Tabla accesible de las fuerzas sobre el satélite ideal en un instante (datos sintéticos).

| Cuerpo | Fuerza | Dirección | Módulo (N) |
|---|---|---|---|
| Satélite | gravedad de la Tierra | hacia el centro | 8675,9 |
| Satélite | suma de otras fuerzas | — | 0 (modelo ideal) |
| Tierra | gravedad del satélite (reacción) | hacia el satélite | 8675,9 |

Descripción larga: una flecha corta apunta del satélite al centro de la Tierra; otra de igual módulo, en sentido contrario, actúa sobre la Tierra; no se dibujan flechas sobre el mismo cuerpo que se anulen entre sí.

## 13. Ejemplo trabajado: ¿qué fuerza hace girar al satélite?

**Planteamiento.** Hallar la fuerza sobre 1000 kg a 400 km y comprobar que explica `a_c`.

**Paso 1 · Cuerpo y marco.** Satélite; marco geocéntrico no rotante; solo gravedad.

**Paso 2 · Fuerza.** `F = m GM/r² = 1000 × 3,9860 × 10¹⁴ / (6 778 137)² = 8675,9 N`.

**Paso 3 · Aceleración.** `a = F/m = 8,676 m/s²`, hacia el centro.

**Paso 4 · Comprobación con C03.** Si la órbita es circular, `v²/r` debe valer lo mismo: `v = 7668,6 m/s` y `v²/r = 8,676 m/s²`. Coinciden.

**Sentido físico.** La fuerza neta no es cero, pero no cambia la rapidez: cambia la dirección. Y el peso en la superficie, `9806,65 N`, es solo un 13 % mayor que la fuerza a 400 km: la altura no es «salir de la gravedad».

## 14. Comparación de métodos

**Fuerzas y `ΣF = m a`** funcionan siempre en el dominio clásico pero exigen conocer cada fuerza. **Energía** (C06, C07) evita el tiempo y la dirección cuando solo importan estados inicial y final. **Momento** (C08) es ideal para choques y propulsión. La elección depende de lo que pidas: trayectoria, rapidez o intercambio.

## 15. Práctica guiada

**Ejercicio 1.** Una fuerza neta de 30 N actúa sobre 6 kg. ¿Qué aceleración? *Pasos:* sección 8.2.

<details><summary>Solución comentada</summary>

`a = 30/6 = 5 m/s²` en la dirección de la fuerza. Dimensionalmente `N/kg = m/s²`.
</details>

**Ejercicio 2.** ¿Cuánto pesa un cuerpo de 70 kg con `g_n`? ¿Y cuánta masa tiene en otro lugar con distinta `g`? *Pista:* sección 8.4.

<details><summary>Solución comentada</summary>

`W = 70 × 9,806 65 = 686,5 N`. La masa sigue siendo 70 kg; solo el peso cambia con `g`.
</details>

**Ejercicio 3.** Un astronauta empuja una pared de la estación con 50 N. ¿Qué fuerza recibe él? ¿Cómo se mueve si su masa es 80 kg?

<details><summary>Solución comentada</summary>

Recibe 50 N en sentido opuesto (tercera ley). `a = 50/80 = 0,625 m/s²` alejándose de la pared: la fuerza actúa sobre él, no sobre la pared.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Dos fuerzas de 3 N (este) y 4 N (norte) actúan sobre 2 kg. Halla `a` en módulo y dirección.

<details><summary>Solución comentada</summary>

`ΣF = (3, 4)`, módulo 5 N; `a = 2,5 m/s²`, dirección `arctan(4/3) = 53,1°` al norte del este.
</details>

**Ejercicio 5.** Con `G = 6,674 30 × 10⁻¹¹` y `M = 5,9722 × 10²⁴ kg`, calcula `GM` y compáralo con 3,9860 × 10¹⁴.

<details><summary>Solución comentada</summary>

`6,674 30 × 5,9722 = 39,8600…`, es decir `3,9860 × 10¹⁴ m³/s²`. Coincide: dos datos de fuentes distintas son consistentes.
</details>

**Ejercicio 6.** ¿Qué aceleración de caída libre tiene un cuerpo a 400 km de altura?

<details><summary>Solución comentada</summary>

`GM/r² = 3,9860 × 10¹⁴ / (6 778 137)² = 8,676 m/s²`. No depende de la masa del cuerpo; por eso todo cae junto en la estación.
</details>

**Ejercicio 7.** Un motor da 20 kN a una nave de 4000 kg en el vacío, sin otras fuerzas. ¿Qué `Δv` en 10 s?

<details><summary>Solución comentada</summary>

`a = 20 000/4000 = 5 m/s²`; `Δv = 5 × 10 = 50 m/s`. Supone masa constante; un motor real la pierde (C08).
</details>

**Ejercicio 8.** Si una persona se pesa en una báscula dentro de la estación, ¿qué marca? Razona con `ΣF = m a`.

<details><summary>Solución comentada</summary>

Marca casi cero: la báscula y la persona tienen la misma aceleración de caída, así que la báscula no ejerce fuerza de contacto (la normal es cero). La gravedad actúa, pero no se «siente».
</details>

**Ejercicio 9 · transferencia.** Un titular dice: «a 400 km la gravedad es casi cero». Contrasta con la sección 13.

<details><summary>Solución comentada</summary>

La fuerza es 8675,9 N sobre 1000 kg, el 88 % de la del suelo. Lo que cambia es que no hay una superficie que sostenga: ingravidez no es ausencia de gravedad.
</details>

**Ejercicio 10 · transferencia.** Una nave quema combustible a ritmo constante y su masa baja de 4000 a 3000 kg con empuje constante. ¿Qué pasa con `a`? ¿Falla alguna fórmula de C03?

<details><summary>Solución comentada</summary>

`a = F/m` crece de 5 a 6,67 m/s²: no es constante, así que `v = v₀ + at` deja de valer; hay que integrar por tramos (C03, ejercicio 11).
</details>

**Ejercicio 11 · transferencia.** El laboratorio muestra que Euler con 600 pasos «cierra» la órbita con un error de 0,57 de `r`, y Verlet con 2,3 × 10⁻⁴. ¿Qué implicaría usar Euler para predecir una trayectoria?

<details><summary>Solución comentada</summary>

La predicción sería inservible: la nave aparecería a miles de kilómetros de donde está. El método numérico es parte del modelo; se declara y se valida contra un caso analítico.
</details>

**Ejercicio 12 · integrador.** Elabora un *planteamiento de dinámica* (sección 20): para el satélite ideal, define marco, cuerpo, fuerzas, `ΣF = m a`, resultado con unidades, comprobación con la aceleración centrípeta y dominio de validez.

<details><summary>Solución modelo</summary>

Marco geocéntrico no rotante; cuerpo: satélite 1000 kg; fuerza: gravedad 8675,9 N; `a = 8,676 m/s²`; comprobación `v²/r`; límites: masa puntual, sin atmósfera ni achatamiento, velocidades ≪ `c`.
</details>

## 17. Laboratorio: la segunda ley integrada

El script [orbita_newton.py](orbita_newton.py) integra `F = m a` para una órbita completa del satélite ideal con Euler y con velocity-Verlet. Antes comprueba que Verlet vuelva al punto de partida con error < 10⁻³ de `r` y que la fuerza calculada coincida con `m GM/r²`.

**Datos:** GM y R de S1; altitud y masa sintéticas. **Predice antes de ejecutar:** ¿cuál de los dos métodos cierra mejor la órbita? **Resultados (2026-11-05, Python 3.12.9):** fuerza sobre 1000 kg = `8675,9 N` (peso con `g_n`: `9806,6 N`). Euler 600 pasos: error de cierre `5,74 × 10⁻¹`; Euler 6000 pasos: `6,28 × 10⁻²`; Verlet 600 pasos: `2,30 × 10⁻⁴`, con `r_final = 6 778 137 m` y `v_final = 7668,55 m/s`.

```bash
python programa/clases/B05/B05-C04-leyes-del-movimiento-de-newton/orbita_newton.py
```

**Límites:** simulación educativa 2D de un problema de dos cuerpos ideal; no es una herramienta de navegación ni certifica nada sobre vuelo o seguridad.

## 18. Errores frecuentes y cómo corregirlos

**Pensar que la fuerza es necesaria para mantener el movimiento.** Ejercicio 7. **Confundir masa y peso.** Ejercicio 2. **Sumar acción y reacción como si fueran sobre el mismo cuerpo.** Ejercicio 3. **Creer que ingravidez es ausencia de gravedad.** Ejercicios 8 y 9. **Usar un integrador sin validarlo.** Ejercicio 11.

## 19. Cómo sabrás que vas bien

Tras 8.2: ¿por qué `ΣF = m a` es vectorial? Rehaz el ejercicio 4. Tras 8.3: ¿por qué acción y reacción no se anulan? Revisa el ejercicio 3. Tras 8.4: ¿puedes explicar la ingravidez en una frase? Si no, relee. Tras el laboratorio: ¿por qué un método falla? Léelo.

## 20. Qué entregas y cómo se evalúa

El producto es tu **planteamiento de dinámica**: marco, cuerpo, fuerzas, aceleración, comprobación y dominio.

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Marco y cuerpo | Ausentes | Parciales | Declarados | Justifica inercialidad |
| Fuerzas y suma | Incompletas | Con ayuda | Correctas | Distingue pares acción–reacción |
| Cálculo y unidades | Errores | Parcial | Correcto | Comprueba por otra vía |
| Límites | No declara | Con ayuda | Declara | Analiza efecto del método numérico |

**Condiciones críticas:** no presentar la simulación como cálculo de misión; unidades obligatorias; citar solo lo consultado.

## 21. Ética, seguridad y límites

Las leyes de Newton tienen dominio de validez: no describen velocidades cercanas a `c` ni fenómenos atómicos. Esta clase es educativa y su código no certifica vuelo ni seguridad. Accesibilidad: ecuaciones en texto, tablas equivalentes de los diagramas, sin conexión.

## 22. Para cerrar y seguir

La fuerza neta determina la aceleración, la masa mide la inercia, las fuerzas aparecen en pares sobre cuerpos distintos y la órbita es una caída continua. Queda abierto cómo organizar las fuerzas de forma sistemática: C05 lo hace con diagramas de cuerpo libre.

**Glosario español–inglés.** fuerza · *force*; masa · *mass*; peso · *weight*; inercia · *inertia*; caída libre · *free fall*; acción y reacción · *action and reaction*.

**Continuidad.** B05-C05 usa tu capacidad de **plantear `ΣF = m a` con un cuerpo y un marco** para dibujar y descomponer fuerzas en diagramas de cuerpo libre.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B05-C03 — Movimiento rectilíneo y circular](../B05-C03-movimiento-rectilineo-y-circular/CLASE.md) · [📚 Bloque B05](../../../tronco-comun/B05-fisica-fundamental-para-el-espacio.md) · [Siguiente: B05-C05 — Diagramas de cuerpo libre →](../../../tronco-comun/B05-fisica-fundamental-para-el-espacio.md#b05-c05)
<!-- /nav -->
