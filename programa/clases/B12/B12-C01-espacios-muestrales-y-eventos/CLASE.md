# B12-C01 — Espacios muestrales y eventos

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B12](../../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) · [← Anterior: B11-C26 — Benchmark de algoritmos numéricos](../../../tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md#b11-c26) · [Siguiente: B12-C02 — Variables aleatorias →](../B12-C02-variables-aleatorias/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Primera clase del bloque B12, que abre el área de incertidumbre del programa. Aquí construyes el lenguaje mínimo de la probabilidad: **espacio muestral**, **evento**, **probabilidad**, **condicional** e **independencia**. Nivel de entrada N1, de salida N2. Usas conteo y fracciones de B09 y de álgebra básica; no necesitas cálculo. No verás aún variables aleatorias (C02) ni distribuciones (C03).

## 2. Por qué esta clase existe

Una nave no sabe si un componente va a fallar; un telescopio no sabe cuántos fotones llegarán. Para decidir con información incompleta hace falta un lenguaje que diga con precisión *qué puede pasar* y *cuánto lo esperamos*. Sin él, frases como «es muy probable» no se pueden comprobar ni combinar.

Pregunta motivadora: **¿con qué probabilidad sigue funcionando un sistema de tres computadores redundantes, y qué cambia si sus fallos no son independientes?** Decisión central: **cuánta redundancia comprar y si el modelo que la justifica es creíble**.

## 3. Lo que podrás hacer al terminar

1. Enumerar el espacio muestral de un experimento sencillo y verificar que sus probabilidades suman 1.
2. Describir un evento como subconjunto del espacio muestral y calcular su probabilidad.
3. Usar complemento, unión y probabilidad condicional, y aplicar la regla de Bayes en un caso de dos eventos.
4. Decidir si dos eventos son independientes comparando `P(A∩B)` con `P(A)P(B)`.
5. Comprobar un cálculo exacto con una simulación y registrar la diferencia.
6. Señalar qué supuesto (independencia, `p` común) sostiene un resultado y cuándo se rompe.

La evidencia es el **informe de redundancia** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

Necesitas fracciones y potencias (B09) y saber contar combinaciones sencillas. Cinco preguntas:

1. ¿Cuánto es `0,9 × 0,9 × 0,1`?
2. ¿Cuántas secuencias de 3 letras, cada una `F` o `X`, existen?
3. ¿Cuánto es `1 − 0,972`?
4. ¿Cuántas formas hay de elegir 2 elementos de 3 (sin orden)?
5. Si `a = 3/4` y `b = 2/3`, ¿cuánto vale `a·b`?

<details>
<summary>Ver respuestas</summary>

1. `0,081`. 2. `8`. 3. `0,028`. 4. `3`. 5. `1/2`.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa fracciones y conteo antes de la sección 8.

## 5. Un caso: tres computadores a bordo

Una sonda **ilustrativa** lleva tres computadores idénticos que votan por mayoría: el sistema funciona si al menos dos funcionan. Cada computador funciona durante toda la misión con probabilidad `p = 0,9` (valor **ilustrativo**, no de una misión real). Este es el **ejemplo conductor**: lo usarás en la explicación, en el ejemplo trabajado, en el laboratorio y en los ejercicios.

## 6. Vocabulario

Un **experimento aleatorio** es un proceso cuyo resultado no se puede predecir con certeza aunque se conozcan sus condiciones. El **espacio muestral** `Ω` es el conjunto de todos los resultados posibles, sin repeticiones ni omisiones. Un **evento** es un subconjunto de `Ω`: «ocurre» si el resultado pertenece a él. La **probabilidad** `P` asigna a cada evento un número entre 0 y 1; el GUM la define como un número de esa escala asociado a un evento aleatorio, interpretable como frecuencia relativa a largo plazo o como grado de creencia (S1, C.2.1). El **complemento** `Aᶜ` son los resultados que no están en `A`. La **unión** `A∪B` ocurre si ocurre `A` o `B`; la **intersección** `A∩B`, si ocurren ambos. La **probabilidad condicional** `P(A|B) = P(A∩B)/P(B)` (con `P(B) > 0`) es la probabilidad de `A` sabiendo que ocurrió `B`. Dos eventos son **independientes** si `P(A∩B) = P(A)P(B)`. Dos eventos son **mutuamente excluyentes** si `A∩B` es vacío; no es lo mismo que independientes.

## 7. Modelo mental: un universo de casos y una regla de peso

Imagina una caja con todas las historias posibles de la misión; cada historia tiene un peso, y los pesos suman 1. Un evento es una etiqueta que pones a un grupo de historias; su probabilidad es la suma de los pesos de ese grupo.

```mermaid
flowchart LR
    A["Experimento:<br/>3 computadores"] --> B["Espacio muestral Ω<br/>8 resultados FFF…XXX"]
    B --> C["Pesos P(w)<br/>suman 1"]
    C --> D["Evento A<br/>≥ 2 funcionan"]
    D --> E["P(A) = suma de pesos<br/>de los resultados de A"]
```

*Descripción textual:* del experimento se deriva la lista de resultados (`Ω`), a cada uno se le asigna un peso, se escoge un evento como subconjunto y su probabilidad es la suma de los pesos de sus elementos.

Analogía: un reparto de pastel en 8 porciones de distinto tamaño; un evento es un subconjunto de porciones. Su límite: en un espacio continuo (C02) no hay porciones contables, sino densidad.

## 8. La explicación, paso a paso

### 8.1 Construir Ω

Cada computador tiene dos estados, `F` (funciona) y `X` (falla). Con tres computadores hay `2 × 2 × 2 = 8` resultados: `FFF, FFX, FXF, FXX, XFF, XFX, XXF, XXX`. Escribir *todos* evita olvidar casos. La **regla de la multiplicación** dice que el número de resultados de etapas sucesivas es el producto de los de cada etapa.

### 8.2 Asignar pesos

Si los computadores son independientes, el peso de un resultado es el producto de sus factores: `FFX` pesa `0,9 · 0,9 · 0,1 = 0,081`. En general, un resultado con `k` computadores funcionando pesa `0,9ᵏ · 0,1³⁻ᵏ`. Comprobación obligatoria: la suma de los 8 pesos debe ser 1.

### 8.3 Un evento es un conjunto

`A = «al menos 2 funcionan» = {FFF, FFX, FXF, XFF}`. Su probabilidad suma `0,729 + 3 · 0,081 = 0,972`. Con la fórmula `3p²(1−p) + p³` da lo mismo. El **complemento** facilita el cálculo: `P(Aᶜ) = 1 − P(A) = 0,028`.

### 8.4 Unión e inclusión–exclusión

Para dos eventos cualquiera, `P(A∪B) = P(A) + P(B) − P(A∩B)`: al sumar `P(A)` y `P(B)` se cuenta dos veces la intersección. Sea `B = «el computador 1 funciona»`, con `P(B) = 0,9`. Entonces `P(A∩B) = 0,729 + 2 · 0,081 = 0,891` y `P(A∪B) = 0,972 + 0,9 − 0,891 = 0,981`.

### 8.5 Probabilidad condicional y Bayes

Sabiendo que el sistema funciona (`A`), ¿qué tan probable es que el computador 1 sea uno de los que funcionan? `P(B|A) = P(A∩B)/P(A) = 0,891/0,972 = 11/12 ≈ 0,9167`, algo más alto que el `0,9` inicial: saber que el sistema funciona es una pista a favor de cada componente. La **regla de Bayes** reescribe lo mismo: `P(B|A) = P(A|B)P(B)/P(A)`, con `P(A|B) = 1 − 0,1² = 0,99` (basta que uno de los otros dos funcione). Comprobación: `0,99 · 0,9/0,972 = 0,9167`. Esta regla es el germen de C12.

### 8.6 Independencia, y cuándo se rompe

`A` y `B` no son independientes aquí: `P(A)P(B) = 0,8748 ≠ 0,891 = P(A∩B)`. Pero hay un problema mayor: el modelo supuso que los fallos de los computadores son independientes. Una tormenta solar o un defecto de fabricación común puede dejarlos fuera a los tres. Con una **causa común** que apaga los tres con probabilidad `q = 0,01`, la probabilidad del sistema baja a `(1 − q) · 0,972 = 0,9623`. La redundancia ayuda menos de lo que sugiere el modelo independiente.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Nota |
|---|---|---|---|
| `Ω` | espacio muestral | — | conjunto de resultados |
| `w` | un resultado | — | p. ej. `FXF` |
| `A, B` | eventos | — | subconjuntos de `Ω` |
| `P(A)` | probabilidad de `A` | adimensional | entre 0 y 1 |
| `p` | prob. de que un computador funcione | adimensional | `0,9` ilustrativo |
| `q` | prob. de fallo de causa común | adimensional | `0,01` ilustrativo |
| `Aᶜ` | complemento de `A` | — | `1 − P(A)` |

## 10. Convenciones y referencias

Probabilidades en forma decimal (coma decimal en el texto, punto en el código). `P(A|B)` se lee «probabilidad de `A` dado `B`». Los resultados se escriben en el orden computador 1, 2, 3. No hay sistema de referencia espacial ni temporal: el experimento es «toda la misión» como un solo ensayo.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Consulta |
|---|---|---|---|---|
| S1 | JCGM 100:2008 (GUM), Anexo C | https://doi.org/10.59161/JCGM100-2008E ; PDF de bipm.org | Definiciones de probabilidad (C.2.1), variable aleatoria (C.2.2) y distribución (C.2.3) | 2026-11-05, PDF abierto y texto extraído |

Límites: los axiomas, la regla de multiplicación, la inclusión–exclusión y la regla de Bayes son resultados estándar de la teoría de la probabilidad que no se atribuyen a una fuente consultada; las cifras de `p` y `q` son **ilustrativas** y los cálculos, propios. Ningún dato de esta clase es observado.

## 12. Cómo ver Ω

Equivalente accesible a un diagrama de árbol de tres niveles (datos **sintéticos**):

| Resultado | Funcionan | Peso | ¿En `A`? |
|---|---|---|---|
| FFF | 3 | 0,729 | sí |
| FFX, FXF, XFF | 2 | 0,081 cada uno | sí |
| FXX, XFX, XXF | 1 | 0,009 cada uno | no |
| XXX | 0 | 0,001 | no |

Descripción larga: el árbol se bifurca dos veces por computador; las ramas `F` pesan 0,9 y las `X` 0,1. Los pesos de las 8 hojas suman 1 (`0,729 + 0,243 + 0,027 + 0,001`).

## 13. Ejemplo trabajado: ¿cuánto aguanta la redundancia?

**Paso 1 · Datos.** `p = 0,9`, tres computadores independientes, decisión por mayoría.

**Paso 2 · Espacio.** Ocho resultados (8.1); sus pesos suman 1.

**Paso 3 · Evento.** `A = {FFF, FFX, FXF, XFF}`.

**Paso 4 · Probabilidad.** `P(A) = 0,729 + 0,243 = 0,972`; exacto como fracción `243/250`.

**Paso 5 · Comparación.** Un solo computador: `0,9`. La triple redundancia reduce la probabilidad de fallo de `0,100` a `0,028`, es decir, 3,6 veces.

**Paso 6 · Supuesto crítico.** Con causa común `q = 0,01`: `0,9623`. La falla pasa de `0,028` a `0,0377`: un 35 % más de lo que dice el modelo independiente.

**Paso 7 · Sentido.** La redundancia sólo protege contra fallos independientes. Cifras **ilustrativas**; no son una evaluación de fiabilidad real.

## 14. Comparación de métodos

Hay tres maneras de obtener `P(A)`: **enumerar** `Ω` (exacto, claro, crece como `2ⁿ`), usar una **fórmula** (exacta y rápida, pero exige reconocer el patrón binomial de C03) y **simular** (aproximada, general, con error que baja como `1/√N`; C14). Enumerar es la mejor opción para verificar las otras dos. Ninguna corrige un modelo equivocado: si la independencia es falsa, las tres dan una respuesta exacta a la pregunta errónea.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Con dos computadores independientes (`p = 0,9`), enumera `Ω` y calcula la probabilidad de que ambos funcionen. *Pasos:* lista, pesos, evento (8.1–8.3).

<details><summary>Solución comentada</summary>

`Ω = {FF, FX, XF, XX}` con pesos `0,81; 0,09; 0,09; 0,01` (suman 1). El evento es `{FF}`: `0,81`.
</details>

**Ejercicio 2 · con una pista.** En el sistema de tres, ¿cuál es la probabilidad de que funcione *exactamente* uno? *Pista:* hay tres resultados con un solo `F`.

<details><summary>Solución comentada</summary>

`3 · 0,9 · 0,1² = 0,027`.
</details>

**Ejercicio 3 · casi autónomo.** Calcula la probabilidad de que el sistema de mayoría falle y compárala con la de un único computador.

<details><summary>Solución comentada</summary>

`P(Aᶜ) = 1 − 0,972 = 0,028` (8.3); un computador falla con `0,1`; la redundancia reduce el fallo 3,6 veces.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Con `p = 0,8`, calcula `P(al menos 2 de 3)`.

<details><summary>Solución comentada</summary>

`3 · 0,8² · 0,2 + 0,8³ = 0,384 + 0,512 = 0,896`.
</details>

**Ejercicio 5.** Si el sistema exigiera que funcionaran los tres (en serie), ¿cuál sería su probabilidad con `p = 0,9`? ¿Qué te dice sobre agregar componentes?

<details><summary>Solución comentada</summary>

`0,9³ = 0,729`. Menos que un solo computador (`0,9`): en serie, más componentes empeoran el resultado.
</details>

**Ejercicio 6.** Sabiendo que *exactamente* dos computadores funcionan, ¿cuál es la probabilidad de que el 1 sea uno de ellos?

<details><summary>Solución comentada</summary>

Los resultados son `FFX, FXF, XFF`, de igual peso; el computador 1 funciona en dos de tres: `2/3` (8.5).
</details>

**Ejercicio 7.** Comprueba si `A` (≥ 2 funcionan) y `B` (el 1 funciona) son independientes.

<details><summary>Solución comentada</summary>

`P(A∩B) = 0,891`; `P(A)P(B) = 0,8748`. Distintos: no son independientes (8.6).
</details>

**Ejercicio 8.** Calcula `P(C1 falla ∪ C2 falla)` con la fórmula de unión y con el complemento.

<details><summary>Solución comentada</summary>

Unión: `0,1 + 0,1 − 0,01 = 0,19`. Complemento: `1 − P(ambos funcionan) = 1 − 0,81 = 0,19`.
</details>

**Ejercicio 9 · transferencia.** Un satélite tiene 4 paneles solares, cada uno operativo con `0,95`, y necesita al menos 3. ¿Probabilidad de cumplir?

<details><summary>Solución comentada</summary>

`4 · 0,95³ · 0,05 + 0,95⁴ = 0,171475 + 0,814506 = 0,985981`. Mismo patrón que 8.3 con otros números y supuesto de independencia.
</details>

**Ejercicio 10 · transferencia.** Un lanzamiento exige clima aceptable (`0,7`) y vehículo listo (`0,9`). Si fueran independientes, ¿cuánto sería? Si el vehículo está listo con `0,95` cuando el clima es aceptable, ¿cuánto?

<details><summary>Solución comentada</summary>

Independientes: `0,7 · 0,9 = 0,63`. Con dependencia: `P(A∩B) = P(clima) P(listo|clima) = 0,7 · 0,95 = 0,665`. La independencia puede subestimar la probabilidad conjunta.
</details>

**Ejercicio 11 · transferencia.** Con `p = 0,9` y causa común `q = 0,02`, calcula `P(A)` y la pérdida respecto del caso independiente.

<details><summary>Solución comentada</summary>

`0,98 · 0,972 = 0,95256`; pérdida `0,972 − 0,95256 = 0,01944`, que sube la probabilidad de fallo un 69 % (`0,028 → 0,04744`).
</details>

**Ejercicio 12 · integrador.** Elabora tu *informe de redundancia*: para 1, 3 y 5 computadores con mayoría, calcula la probabilidad de éxito con `p = 0,9` sin y con causa común `q = 0,01`, verifica por enumeración o simulación y concluye cuántos conviene.

<details><summary>Solución modelo</summary>

Sin causa común: `0,9; 0,972; 0,99144`. Con `q = 0,01`: `0,891; 0,96228; 0,98153`. De 3 a 5 la ganancia es `0,0194` sin causa común y `0,0192` con ella; el tope lo pone `q`. Debe declarar `p` y `q` como ilustrativos, verificar un valor por simulación (como la sección 17) y señalar que la independencia es un supuesto.
</details>

## 17. Laboratorio: enumerar y simular

El script [espacio_muestral_triple.py](espacio_muestral_triple.py) enumera `Ω`, calcula `P(A)` con fracciones exactas, comprueba Bayes y la inclusión–exclusión, y compara con una simulación; falla si alguna igualdad no se cumple.

**Datos:** sintéticos, `p = 0,9` ilustrativo. **Predice antes de ejecutar:** ¿cuánto se desviará la simulación de `0,972`? (menos de `5 × 10⁻⁴`.) **Ejecución del 2026-11-05 (Python 3.12.9, NumPy 2.4.4):**

```text
tamano del espacio muestral: 8
P(A) = 243/250 = 0.972000
P(C1 funciona | A) = 11/12 = 0.916667
P(A U B) = 0.981000
frecuencia simulada de A (N=1000000): 0.971841  diferencia = 1.59e-04
con fallo de causa comun q=0.01: P(A) = 0.962280
Pruebas superadas.
```

```bash
python programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/espacio_muestral_triple.py
```

**Límites:** independencia entre computadores; resultados **simulados** sobre datos **sintéticos**.

## 18. Errores frecuentes y cómo corregirlos

**Olvidar resultados al enumerar.** Se corrige verificando que los pesos suman 1 (8.2).

**Confundir excluyentes con independientes.** Se corrige con los ejercicios 7 y 8: eventos excluyentes con probabilidad positiva son dependientes.

**Usar la independencia sin justificarla.** Se corrige con los ejercicios 10 y 11.

**Invertir la condicional.** `P(A|B) ≠ P(B|A)`; se corrige con 8.5 y el ejercicio 6.

**Pensar que la simulación «prueba» el cálculo.** Sólo lo respalda dentro de su error; se corrige con la sección 17.

## 19. Cómo sabrás que vas bien

Tras 8.2: ¿tus ocho pesos suman 1? Si no, ejercicio 1. Tras 8.5: ¿por qué `P(B|A)` supera a `P(B)`? Si no puedes explicarlo, ejercicio 6. Tras 8.6: ¿qué supuesto sostiene `0,972`? Si dudas, ejercicio 11. Tras el laboratorio: ¿es creíble que la diferencia sea del orden de `1/√N`?

## 20. Qué entregas y cómo se evalúa

El producto es tu **informe de redundancia** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Espacio muestral | Incompleto | Completo sin verificar | Completo y suma 1 | Elige la representación más económica |
| Cálculo de eventos | Errores | Correcto con ayuda | Correcto con complemento/unión | Verifica por dos métodos |
| Independencia | No la menciona | La menciona | La declara y la comprueba | Cuantifica su efecto (causa común) |
| Verificación | Ninguna | Sin comparar | Simulación comparada | Explica la diferencia con `1/√N` |
| Fuentes y rótulo | Sin rótulo | Parcial | Datos rotulados sintéticos/ilustrativos | Declara qué no es válido |

**Condiciones críticas (no se compensan con promedio):** declarar el supuesto de independencia; rotular `p` como ilustrativo; no presentar el resultado como evaluación de fiabilidad real.

## 21. Ética, seguridad y límites

Un cálculo de redundancia con probabilidades inventadas no certifica ninguna nave. En ingeniería real, la fiabilidad se apoya en datos de fallos y en un análisis de modos comunes revisado por especialistas. Accesibilidad: el árbol se ofrece como tabla; todo se resuelve sin conexión.

## 22. Para cerrar y seguir

Un espacio muestral lista lo que puede pasar, los pesos dicen cuánto, un evento es un subconjunto y su probabilidad es la suma de pesos; la condicional actualiza y la independencia es un supuesto que hay que justificar. Queda abierta una pregunta: si lo que importa es *cuántos* computadores funcionan, ¿se puede dar un nombre a ese número y estudiarlo directamente? Es la variable aleatoria.

**Glosario español–inglés.** espacio muestral · *sample space*; evento · *event*; probabilidad condicional · *conditional probability*; independencia · *independence*; complemento · *complement*; regla de Bayes · *Bayes' rule*; causa común · *common cause*.

**Continuidad.** B12-C02 reutiliza tu capacidad de **calcular la probabilidad de un evento sumando pesos** para definir distribuciones.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B11-C26 — Benchmark de algoritmos numéricos](../../../tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md#b11-c26) · [📚 Bloque B12](../../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) · [Siguiente: B12-C02 — Variables aleatorias →](../B12-C02-variables-aleatorias/CLASE.md)
<!-- /nav -->
