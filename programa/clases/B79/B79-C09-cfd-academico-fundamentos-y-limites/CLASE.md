# B79-C09 — CFD académico: fundamentos y límites

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B79](../../../tronco-comun/B79-fluidos-termodinamica-y-aerotermodinamica-de-propulsion.md) · [← Anterior: B79-C08 — Flujo en toberas convergente-divergentes](../B79-C08-flujo-en-toberas-convergente-divergentes/CLASE.md) · [Siguiente: B79-C10 — Primera ley de la termodinámica en sistemas abiertos →](../B79-C10-primera-ley-de-la-termodinamica-en-sistemas-abiertos/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 9 del bloque B79. Nivel N3. La dinámica de fluidos computacional (CFD) resuelve numéricamente las ecuaciones de Euler y Navier–Stokes que no tienen solución cerrada. Esta clase construye el caso más pequeño posible —advección–difusión estacionaria 1D con solución exacta—, lo resuelve con volúmenes finitos y dos esquemas, mide el orden de convergencia y el índice GCI, y muestra qué prueba una malla y qué no. Usa el tratamiento numérico de [C03](../B79-C03-ecuaciones-de-navier-stokes/CLASE.md) y no requiere más. El problema es sintético.

## 2. Por qué esta clase existe

B11-C14/C15 no construyen simulaciones de flujo ni discuten sus límites. Sin esa discusión, una malla fina y un colorido mapa de campos se confunden con una predicción fiable. La decisión central: **¿qué pruebo cuando refino la malla y qué sigue sin probar?**

## 3. Lo que podrás hacer al terminar

1. Discretizar una ecuación de advección–difusión con volúmenes finitos.
2. Comparar el esquema central y el upwind de primer orden.
3. Calcular el orden de convergencia observado.
4. Calcular un índice de convergencia de malla (GCI).
5. Detectar oscilaciones cuando el número de Péclet de celda supera 2.
6. Distinguir verificación de validación.

La evidencia es la **estudio de convergencia en malla** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es una malla?
2. ¿Qué es un error de truncamiento?
3. ¿Qué es un sistema tridiagonal?
4. ¿Qué es el orden de un método?
5. ¿Qué es una verificación por segunda vía?

<details>
<summary>Ver respuestas</summary>

1. una partición del dominio en celdas o nodos donde se calcula la solución. 2. la diferencia entre la ecuación exacta y su aproximación discreta. 3. uno cuya matriz solo tiene tres diagonales no nulas. 4. el exponente `p` con que el error baja al refinar: `e ∝ hᵖ`. 5. calcular lo mismo con otro método y comparar.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Para `Pe = 40`, el esquema central pasa de un error `3,5 × 10⁻¹` con 10 celdas a `4,8 × 10⁻⁴` con 320 (orden `2,007`) pero oscila por debajo de cero con 10 celdas; el upwind no oscila y llega a un orden `0,932`. Es el **ejemplo conductor**. Todo es **sintético**: no es un flujo real.

## 6. Vocabulario

La **verificación** comprueba que se resuelven bien las ecuaciones; la **validación** comprueba que son las ecuaciones correctas para el fenómeno. El **número de Péclet** `Pe = u L/Γ` compara advección y difusión; el **Péclet de celda** es `Pe/N`. El **orden observado** es `p = log₂(e_h/e_{h/2})`. El **índice de convergencia de malla (GCI)** estima la incertidumbre numérica a partir de tres mallas.

## 7. Modelo mental: una foto con más o menos píxeles

```mermaid
flowchart LR
    P["ecuación + condiciones"] --> D["discretización: central / upwind"]
    D --> S["solución en N celdas"]
    S --> E["error contra exacta"]
    E --> O["orden observado, GCI"]
    O --> V["verificación"]
    V -.->|"no implica"| VA["validación"]
```

*Descripción textual:* el problema se discretiza, se resuelve en mallas sucesivas, se mide el error y el orden, y eso verifica el código sin validar el modelo.

Analogía: una foto con más píxeles define mejor lo que enfoca, pero no corrige si apuntaste a lo equivocado. Límite: la analogía no refleja la inestabilidad de algunos esquemas.

## 8. La explicación, paso a paso

### 8.1 El problema

`u φ' = Γ φ''` en `[0,1]`, `φ(0) = 0`, `φ(1) = 1`, con `Pe = 40` y `u = 1`. La solución exacta es `φ = (e^{Pe x} − 1)/(e^{Pe} − 1)`, una capa fina junto a `x = 1`. El sistema discreto es tridiagonal (Thomas).

### 8.2 Dos esquemas

| `N` | `Pe` celda | error central | orden | error upwind | orden |
|---|---|---|---|---|---|
| 10 | 4,00 | 3,5167 × 10⁻¹ | — | 1,8168 × 10⁻¹ | — |
| 20 | 2,00 | 1,3534 × 10⁻¹ | 1,378 | 1,9800 × 10⁻¹ | −0,124 |
| 40 | 1,00 | 3,4546 × 10⁻² | 1,970 | 1,3212 × 10⁻¹ | 0,584 |
| 80 | 0,50 | 7,8794 × 10⁻³ | 2,132 | 7,6565 × 10⁻² | 0,787 |
| 160 | 0,25 | 1,9291 × 10⁻³ | 2,030 | 4,1721 × 10⁻² | 0,876 |
| 320 | 0,12 | 4,7982 × 10⁻⁴ | 2,007 | 2,1865 × 10⁻² | 0,932 |

Con `Pe` de celda `4`, el central produce `φ_min = −0,33336`: oscilaciones no físicas. El upwind es monótono pero difusivo y su orden tarda en acercarse a 1. En mallas gruesas el error upwind incluso sube de `N = 10` a `20`: aún no está en el régimen asintótico.

### 8.3 GCI

Con la cantidad de interés `φ(0,95)` en tres mallas upwind (80/160/320): `0,197531; 0,167772; 0,151901`, orden `0,907` y `GCI = 14,927 %` (factor de seguridad `1,25`). El valor exacto es `0,135335`, es decir, el error real de la malla fina (`12,2 %`) queda dentro del GCI.

### 8.4 Verificación no es validación

Un modelo equivocado (solo difusión, `φ = x`) converge perfectamente en malla, pero se aleja de la solución exacta en `0,883`. Refinar la malla no detecta que la ecuación está mal. En un flujo real hay además condiciones de contorno, turbulencia y propiedades del gas que solo la validación con medidas puede contrastar; este laboratorio no lo hace.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `Pe` | número de Péclet | — | 40 |
| `N` | número de celdas | — | 10–320 |
| `h` | tamaño de celda | — | `1/N` |
| `e` | error máximo contra la exacta | — | 4,8 × 10⁻⁴–3,5 × 10⁻¹ |
| `p` | orden observado | — | 0,932; 2,007 |
| `GCI` | índice de convergencia de malla | % | 14,927 |

## 10. Convenciones y referencias

Problema adimensional 1D estacionario con `u = 1` y `L = 1`; volúmenes finitos con nodos; condiciones de Dirichlet. Sin turbulencia, sin compresibilidad. Todos los datos son sintéticos. Python 3.12.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA Glenn, «Navier-Stokes Equations» — https://www.grc.nasa.gov/www/k-12/airplane/nseqs.html (consultada 2026-11-10) | página completa | Euler = Navier–Stokes sin términos viscosos; NS son ecuaciones acopladas que se resuelven en general con CFD y un modelo de turbulencia | Consultada |
| — | Relaciones estándar de libro de texto que el laboratorio verifica con una segunda vía | — | las verifica el laboratorio | No consultada en una fuente concreta |

Límites: el problema, los esquemas, el orden observado y el GCI son material estándar no consultado en una fuente concreta; el problema es sintético y no representa un flujo real.

## 12. Cómo ver la convergencia

| Magnitud | Valor |
|---|---|
| orden central | 2,007 |
| orden upwind | 0,932 |
| `φ_min` central, 10 celdas | −0,33336 |
| GCI upwind | 14,927 % |

Descripción larga: el central converge más rápido pero oscila con mallas gruesas; el upwind es estable y lento.

## 13. Ejemplo trabajado: el orden observado del central entre 160 y 320 celdas

**Paso 1 · Errores.** `e₁₆₀ = 1,9291 × 10⁻³`, `e₃₂₀ = 4,7982 × 10⁻⁴`.

**Paso 2 · Cociente.** `1,9291/0,47982 = 4,0204`.

**Paso 3 · Orden.** `log₂ 4,0204 = 2,007`.

## 14. Distintas formas de describir la convergencia

**Por error:** `e(N)`. **Por orden:** `p`. **Por incertidumbre:** `GCI`. **Por monotonía:** `φ_min`.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula el Péclet de celda con `Pe = 40` y `N = 20`. *Pasos:* `Pe/N`.

<details><summary>Solución comentada</summary>

`2`.
</details>

**Ejercicio 2 · con una pista.** ¿Qué orden da pasar de `7,6565 × 10⁻²` a `4,1721 × 10⁻²`? *Pista:* `log₂` del cociente.

<details><summary>Solución comentada</summary>

`log₂ 1,835 = 0,876`.
</details>

**Ejercicio 3 · casi autónomo.** ¿Por qué oscila el central a `N = 10`? *Casi autónomo:* compara `Pe` de celda con 2.

<details><summary>Solución comentada</summary>

Porque `Pe/N = 4 > 2` y los coeficientes dejan de ser positivos.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Orden esperado si el error baja 8 veces al duplicar la malla.

<details><summary>Solución comentada</summary>

`log₂ 8 = 3`.
</details>

**Ejercicio 5 · autónomo.** `Pe` de celda para `N = 80`.

<details><summary>Solución comentada</summary>

`0,5`.
</details>

**Ejercicio 6 · autónomo.** Con orden 2, ¿en qué factor baja el error al triplicar `N`?

<details><summary>Solución comentada</summary>

`3² = 9`.
</details>

**Ejercicio 7 · autónomo.** ¿Cuántas celdas necesita el central para `Pe` de celda `≤ 1`?

<details><summary>Solución comentada</summary>

`N ≥ 40`.
</details>

**Ejercicio 8 · autónomo.** ¿Qué dice el error del modelo equivocado (0,883) sobre el orden?

<details><summary>Solución comentada</summary>

Nada: la malla converge a una solución distinta de la exacta.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un colega afirma que su simulación está «validada» porque convergió en malla. ¿Es correcto?

<details><summary>Solución comentada</summary>

No: eso es verificación; la validación exige comparar con medidas.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Qué haría con un flujo turbulento real en una tobera?

<details><summary>Solución comentada</summary>

Declarar el modelo de turbulencia, verificar con mallas, validar con datos y reportar incertidumbre; el laboratorio no hace nada de esto.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Por qué el GCI no sustituye a la validación?

<details><summary>Solución comentada</summary>

Estima solo el error numérico de discretización, no el error de modelo.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *estudio de convergencia en malla*: tabla de errores y órdenes de ambos esquemas, GCI, comentario de las oscilaciones y distinción entre verificación y validación.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: advección–difusión 1D con volúmenes finitos

El script [cfd1d.py](cfd1d.py) resuelve el problema con esquema central y upwind en seis mallas, mide errores, órdenes, oscilaciones y GCI, y muestra un modelo equivocado convergido (**comprueba** órdenes en rangos y presencia de oscilaciones).

**Datos:** solo se consultó que NASA Glenn presenta las ecuaciones de Navier–Stokes como base del CFD y el papel del modelo de turbulencia; el problema, `Pe` y las mallas son **sintéticos**. **Predice antes de ejecutar:** ¿qué orden observará el esquema upwind? (cercano a 1.) **Ejecución del 2026-11-10:**

```text
Python 3.12.9 (biblioteca estandar)
Problema SINTETICO: u phi' = Gamma phi'' en [0,1], Pe = 40.0, phi(0)=0, phi(1)=1
Esquema central
    N    Pe celda   error max      orden observado   min(phi)
   10     4.00    3.5167e-01            -          -0.33336
   20     2.00    1.3534e-01        1.378          -0.00000
   40     1.00    3.4546e-02        1.970           0.00000
   80     0.50    7.8794e-03        2.132           0.00000
  160     0.25    1.9291e-03        2.030           0.00000
  320     0.12    4.7982e-04        2.007           0.00000
Esquema upwind
    N    Pe celda   error max      orden observado   min(phi)
   10     4.00    1.8168e-01            -           0.00000
   20     2.00    1.9800e-01       -0.124           0.00000
   40     1.00    1.3212e-01        0.584           0.00000
   80     0.50    7.6565e-02        0.787           0.00000
  160     0.25    4.1721e-02        0.876           0.00000
  320     0.12    2.1865e-02        0.932           0.00000
Orden observado en las mallas finas: central = 2.007 ; upwind = 0.932
GCI (upwind, phi(0.95) con 80/160/320 celdas): orden = 0.907 ; GCI fino = 14.927 %
 phi(0.95): mallas = 0.197531, 0.167772, 0.151901 ; exacta = 0.135335
Modelo equivocado (solo difusion, convergido en malla): error max respecto a la exacta = 0.883
Pruebas superadas.
```

```bash
python programa/clases/B79/B79-C09-cfd-academico-fundamentos-y-limites/cfd1d.py
```

**Límites:** problema lineal 1D con solución exacta; no hay choque, turbulencia ni compresibilidad; el GCI es una estimación, no una cota.

## 18. Errores frecuentes y cómo corregirlos

**Confundir verificación con validación.** Se corrige con 8.4.

**Fiarse de un esquema que oscila.** Se corrige con 8.2.

**Calcular el orden con mallas fuera del régimen asintótico.** Se corrige con 8.2.

**Presentar el problema sintético como un flujo real.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué orden esperabas del central y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **estudio de convergencia en malla** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Mide órdenes y distingue verificación de validación | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas con unidades | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con una segunda vía | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo ilustrativo y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular el problema como sintético; no presentar la convergencia en malla como validación; no presentar un cálculo como medición de un motor real; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y sus datos son sintéticos, ilustrativos o coeficientes publicados con fuente; ningún resultado describe un motor o un vehículo reales ni sustituye al análisis de ingeniería, a las normas o a los datos de fabricante.  Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

El central alcanza orden 2,007 y el upwind 0,932, y un modelo equivocado converge igual de bien. Con la parte de flujo cerrada, queda una pregunta: ¿cómo se contabiliza la energía de un flujo a través de un motor? Lo ve C10.

**Glosario español–inglés.** dinámica de fluidos computacional · *computational fluid dynamics*; volúmenes finitos · *finite volumes*; verificación · *verification*; validación · *validation*; número de Péclet · *Péclet number*.

**Continuidad.** [B79-C10](../B79-C10-primera-ley-de-la-termodinamica-en-sistemas-abiertos/CLASE.md) estudia la primera ley en sistemas abiertos.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B79-C08 — Flujo en toberas convergente-divergentes](../B79-C08-flujo-en-toberas-convergente-divergentes/CLASE.md) · [📚 Bloque B79](../../../tronco-comun/B79-fluidos-termodinamica-y-aerotermodinamica-de-propulsion.md) · [Siguiente: B79-C10 — Primera ley de la termodinámica en sistemas abiertos →](../B79-C10-primera-ley-de-la-termodinamica-en-sistemas-abiertos/CLASE.md)
<!-- /nav -->
