# B37-C03 — Opacidad media de Rosseland y tablas de opacidad en interiores

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B37](../../../tronco-comun/B37-interiores-estelares-y-asterosismologia.md) · [← Anterior: B37-C02 — Ecuaciones de estado estelares: gas ideal, radiación y degeneración](../B37-C02-ecuaciones-de-estado-estelares-gas-ideal-radiacion-y-degeneracion/CLASE.md) · [Siguiente: B37-C04 — Condiciones de frontera centrales y superficiales en modelos estelares →](../B37-C04-condiciones-de-frontera-centrales-y-superficiales-en-modelos-estelares/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 3 del bloque B37. Nivel N3. El transporte radiativo usa una opacidad **media** de todas las frecuencias. Aquí calculas la **media de Rosseland** de una opacidad de tipo Kramers `κ_ν ∝ ν⁻³` por cuadratura y por su forma analítica, y usas una **tabla interpolada** en `log ρ, log T` para obtener `∇_rad`. Usas [B05](../../../tronco-comun/B05-fisica-fundamental-para-el-espacio.md) y la convección de B37-C01. Las opacidades son de juguete.

## 2. Por qué esta clase existe

Un código no integra en frecuencia en cada capa: lee una tabla de `κ_R(ρ, T)`. La decisión central: **¿cómo se promedia la opacidad y qué error añade la interpolación de la tabla?**

## 3. Lo que podrás hacer al terminar

1. Definir la media de Rosseland como media armónica ponderada.
2. Evaluar la integral con `n! ζ(n)`.
3. Contrastar la cuadratura con la forma analítica.
4. Interpolar una tabla en `log-log`.
5. Calcular `∇_rad` con la opacidad leída.
6. Nombrar los límites de una opacidad de juguete.

La evidencia es la **ficha de la opacidad media** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es una incertidumbre?
2. ¿Qué es una simulación Monte Carlo?
3. ¿Qué es una tabla de resultados?
4. ¿Qué es un valor ilustrativo?
5. ¿Qué es una verificación?

<details>
<summary>Ver respuestas</summary>

1. Un intervalo en que se espera el valor verdadero. 2. Repetir con números aleatorios de semilla fija. 3. Un resumen ordenado de cálculos. 4. Un valor propuesto para el ejemplo, no medido. 5. Comparar un cálculo con un caso independiente.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Para `κ_ν = κ₀ (ν/ν₀)⁻³`, el coeficiente de la media vale `195,64705` por cuadratura y `195,64705` por el cálculo analítico `7! ζ(7)/(4! ζ(4))`. Con una tabla de malla gruesa, el valor en `ρ = 150 kg/m³` y `T = 1,3 × 10⁷ K` se interpola con un error de `3,394 %`. Es el **ejemplo conductor**; las opacidades son **ilustrativas**.

## 6. Vocabulario

La **opacidad media de Rosseland** `1/κ_R = ∫ (1/κ_ν)(∂B_ν/∂T) dν / ∫ (∂B_ν/∂T) dν`. Una **opacidad gris** es independiente de la frecuencia. La **opacidad de Kramers** decrece como `ν⁻³`. Una **tabla de opacidad** guarda `log κ` en una malla `(log ρ, log T)`. La **interpolación bilineal** completa entre cuatro vecinos.

## 7. Modelo mental: una media armónica

Es como calcular la velocidad media de un viaje con tramos lentos y rápidos: manda el tramo lento. En la media de Rosseland mandan las frecuencias donde el plasma es más transparente, porque por ahí se escapa la luz.

```mermaid
flowchart LR
    K["κ_ν"] --> P["pesar con ∂B/∂T"]
    P --> M["media armónica κ_R"]
    M --> T["tabla κ(ρ,T)"]
    T --> I["interpolar log-log"]
    I --> N["∇_rad"]
```

*Descripción textual:* se promedia la inversa de la opacidad con el peso de la derivada de Planck, se guarda en una tabla y se interpola.

Analogía: una media armónica. Límite: opacidad de juguete sin líneas.

## 8. La explicación, paso a paso

### 8.1 La identidad

Con `u = hν/kT`, la integral `∫ u^n e^u/(e^u − 1)² du` vale `n! ζ(n)`. Por cuadratura: `n = 4` da `25,975758` y `n = 7` da `5082,080358`; los valores analíticos coinciden en seis decimales.

### 8.2 La media de Rosseland

Para `κ_ν ∝ ν⁻³`, `1/κ_R = (1/κ₀)(kT/hν₀)³ · 7! ζ(7)/(4! ζ(4))`. El coeficiente numérico es `195,64705` (cuadratura) y `195,64705` (analítico). Una opacidad gris de `3,0` da una media de `3,000000`.

Con `T = 10⁷ K`, `ν₀ = 10¹⁵ Hz` y `κ₀ = 1 m²/kg` (ilustrativos), `(kT/hν₀)³ = 9,047 × 10⁶` y `κ_R = 5,650 × 10⁻¹⁰ m²/kg`.

### 8.3 La tabla

Una tabla de `9 × 9` puntos (pasos de 0,5 dex en `ρ` y 0,25 dex en `T`) de una opacidad de juguete con curvatura añadida: en `ρ = 150 kg/m³` y `T = 1,3 × 10⁷ K` el valor exacto es `53,247` y el interpolado `51,440`, un error de `3,394 %`.

### 8.4 El gradiente

Con el valor interpolado, `H_P = 4 × 10⁷ m` y un flujo de `4 × 10⁹ W/m²`, `∇_rad = 0,1429`. Duplicar `κ` duplica `∇_rad`.

### 8.5 Lectura

La media armónica castiga a las frecuencias opacas; la tabla gruesa introduce un error que se reduce afinando la malla. Las tablas reales incluyen líneas y composición que este modelo no tiene.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `κ_R` | opacidad media de Rosseland | m²/kg | 5,650 × 10⁻¹⁰ (ilustrativo) |
| `u` | `hν/kT` | — | variable de integración |
| `ζ(n)` | función zeta de Riemann | — | `ζ(4) = π⁴/90` |
| `∇_rad` | gradiente radiativo | — | 0,1429 |
| `h`, `k_B` | constantes | SI | de NIST |

## 10. Convenciones y referencias

Opacidad monocromática `κ₀ (ν/ν₀)⁻³`, sin líneas ni dispersión; tabla `κ = k₀ ρ T⁻³˒⁵/(1 + (T/2 × 10⁷)²)` de juguete; constantes de NIST.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NIST, *Fundamental Physical Constants* (CODATA 2022) | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | `h`, `k_B`, `σ`, `c` | Consultada el 2026-11-09 |
| S2 | Valores y modelo del laboratorio | — | opacidad y tabla de juguete | Ilustrativo o sintético; no consultado |

Límites: no se usó ninguna tabla de opacidad real.

## 12. Cómo ver la media

| Magnitud | Valor |
|---|---|
| coeficiente (cuadratura) | 195,64705 |
| coeficiente (analítico) | 195,64705 |
| error de la tabla | 3,394 % |
| `∇_rad` | 0,1429 |

Descripción larga: cuadratura y análisis coinciden; la tabla gruesa añade un error de 3,4 %.

## 13. Ejemplo trabajado: el coeficiente de Rosseland

**Paso 1 · Numerador.** `7! ζ(7) = 5040 × 1,008349 = 5082,08`.

**Paso 2 · Denominador.** `4! ζ(4) = 24 × 1,082323 = 25,9758`.

**Paso 3 · Cociente.** `5082,08/25,9758 = 195,647`.

**Paso 4 · Media.** `κ_R = κ₀ (hν₀/kT)³/195,647`.

## 14. Distintas formas de describir la opacidad media

**Por definición:** media armónica ponderada. **Por analítica:** `n! ζ(n)`. **Por tabla:** interpolación `log-log`. **Por uso:** `∇_rad`.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Coeficiente de Rosseland desde `5082,080` y `25,9758`. *Pasos:* cociente.

<details><summary>Solución comentada</summary>

`195,647`.
</details>

**Ejercicio 2 · con una pista.** Media de Rosseland de una opacidad gris de 3,0.

<details><summary>Solución comentada</summary>

`3,000`.
</details>

**Ejercicio 3 · casi autónomo.** ¿Qué pasa con `∇_rad` si `κ` se duplica?

<details><summary>Solución comentada</summary>

Se duplica: `0,2858`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Error de la tabla: `51,440` frente a `53,247`.

<details><summary>Solución comentada</summary>

`(53,247 − 51,440)/53,247 = 3,39 %`.
</details>

**Ejercicio 5.** `κ_R` a `10⁷ K` si `(kT/hν₀)³ = 9,047 × 10⁶`.

<details><summary>Solución comentada</summary>

`κ₀/(9,047 × 10⁶ × 195,647)`, que es `5,650 × 10⁻¹⁰`.
</details>

**Ejercicio 6.** ¿Por qué la media es armónica?

<details><summary>Solución comentada</summary>

Porque el flujo se escapa por las frecuencias más transparentes.
</details>

**Ejercicio 7.** ¿Se reduce el error de la tabla afinando la malla?

<details><summary>Solución comentada</summary>

Sí, la interpolación bilineal converge cuadráticamente.
</details>

**Ejercicio 8.** Valor de `n! ζ(n)` para `n = 4`.

<details><summary>Solución comentada</summary>

`25,975758`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un compañero usa `κ_R` del laboratorio para un modelo solar. Responde.

<details><summary>Solución comentada</summary>

No: la opacidad es de juguete.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Por qué una tabla se interpola en `log-log`?

<details><summary>Solución comentada</summary>

Porque la opacidad varía como potencias de `ρ` y `T`.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Qué omite una opacidad sin líneas?

<details><summary>Solución comentada</summary>

El efecto de miles de transiciones atómicas.
</details>

**Ejercicio 12.** **Integrador.** Elabora tu *ficha de la opacidad media*: media, tabla y gradiente.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.5.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha de la opacidad media*: media, tabla y gradiente.

<details><summary>Solución modelo</summary>

Secciones 8.1–8.5.
</details>

## 17. Laboratorio: media de Rosseland y tabla

El script [opacidad_rosseland.py](opacidad_rosseland.py) calcula la media por cuadratura, la compara con la analítica y usa una tabla interpolada (**comprueba** 1e-4 y 5 %).

**Datos:** `h`, `k_B` de NIST; opacidades **ilustrativas**. **Predice antes de ejecutar:** ¿cuánto valdrá el coeficiente? (195,65.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
n = 4: integral numerica = 25.975758 ; n! zeta(n) = 25.975758
n = 7: integral numerica = 5082.080358 ; n! zeta(n) = 5082.080358
coeficiente 1/kappa_R: cuadratura = 195.64705 ; analitico 7! zeta(7)/(4! zeta(4)) = 195.64705
kappa gris = 3,0 -> media de Rosseland = 3.000000
T = 1e7 K: (kT/(h nu0))^3 = 9.047e+06 ; kappa_R = 5.650e-10 m2/kg
tabla en (rho = 150, T = 1,3e7): exacto = 5.3247e+01 ; interpolado = 5.1440e+01 ; error = 3.394 %
nabla_rad = 3 kappa rho H_P F/(4 a c T^4) = 0.1429
Pruebas superadas.
```

```bash
python programa/clases/B37/B37-C03-opacidad-media-de-rosseland-y-tablas-de-opacidad-en-interiores/opacidad_rosseland.py
```

**Límites:** opacidad de juguete.

## 18. Errores frecuentes y cómo corregirlos

**Promediar `κ` directamente.** Se corrige con 8.2.

**Interpolar en escala lineal.** Se corrige con 8.3.

**Olvidar el error de la tabla.** Se corrige con 8.3.

**Usar la opacidad de juguete como real.** Se corrige en la sección 10.

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué resultado esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de la opacidad media** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | conceptos de la clase | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con el análisis | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | fuentes con fecha | Declara lo ilustrativo |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular la opacidad como de juguete; no usarla en un modelo real; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

La media armónica de Rosseland y su tabla alimentan el gradiente radiativo. Queda una pregunta: ¿cómo se cierran las ecuaciones en el centro y en la superficie?

**Glosario español–inglés.** opacidad · *opacity*; media de Rosseland · *Rosseland mean*; opacidad gris · *grey opacity*; interpolación · *interpolation*; gradiente radiativo · *radiative gradient*.

**Continuidad.** [B37-C04](../B37-C04-condiciones-de-frontera-centrales-y-superficiales-en-modelos-estelares/CLASE.md) estudia las condiciones de frontera.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B37-C02 — Ecuaciones de estado estelares: gas ideal, radiación y degeneración](../B37-C02-ecuaciones-de-estado-estelares-gas-ideal-radiacion-y-degeneracion/CLASE.md) · [📚 Bloque B37](../../../tronco-comun/B37-interiores-estelares-y-asterosismologia.md) · [Siguiente: B37-C04 — Condiciones de frontera centrales y superficiales en modelos estelares →](../B37-C04-condiciones-de-frontera-centrales-y-superficiales-en-modelos-estelares/CLASE.md)
<!-- /nav -->
