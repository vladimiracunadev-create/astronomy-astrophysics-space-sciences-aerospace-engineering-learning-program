# B05-C13 — Temperatura y energía térmica

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B05](../../../tronco-comun/B05-fisica-fundamental-para-el-espacio.md) · [← Anterior: B05-C12 — Ondas mecánicas y frecuencia](../B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md) · [Siguiente: B05-C14 — Gases y presión →](../B05-C14-gases-y-presion/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Decimotercera clase de B05 y apertura de su cuarto tramo (termodinámica elemental y electromagnetismo). Hasta aquí la energía era cinética o potencial de un cuerpo; ahora aparece la que reside en el movimiento desordenado de muchas partículas. Nivel N1. Usas energía (C06–C07), `E_c = ½mv²` y potencias de 10. No verás todavía las leyes de la termodinámica en forma general (bloques posteriores).

## 2. Por qué esta clase existe

Un satélite recibe luz solar de un lado y emite calor al espacio por el otro, y la electrónica solo trabaja en un rango de temperaturas. La pregunta motivadora es: **¿qué es la temperatura, cómo se relaciona con la energía de las partículas y qué determina la temperatura de equilibrio de un cuerpo en el espacio?** La decisión central es separar temperatura (un estado), calor (una transferencia) y energía térmica (una cantidad almacenada) y elegir un modelo declarando qué se ignora.

## 3. Lo que podrás hacer al terminar

1. Distinguir temperatura, calor y energía térmica, con unidades.
2. Pasar entre kelvin y Celsius y explicar por qué la escala absoluta importa.
3. Relacionar la temperatura con la energía cinética media de traslación `(3/2) k_B T`.
4. Calcular la energía necesaria para calentar un cuerpo con `Q = m c ΔT`.
5. Calcular la temperatura de equilibrio radiativo de una esfera con Stefan–Boltzmann.
6. Declarar el dominio de validez de un balance térmico simple.

La evidencia es el **balance térmico** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Cuántos kelvin son 15 °C?
2. Calcula `288⁴` (aprox. `6,9 × 10⁹`).
3. ¿Qué dimensión tiene la energía? (C01)
4. ¿Cuánto es `(1361/4)^(1/4)`? (usa una calculadora: ≈ 4,29)
5. ¿Qué es una potencia en vatios? (C06)

<details>
<summary>Ver respuestas</summary>

1. 288,15 K. 2. `6,88 × 10⁹`. 3. `M L² T⁻²`. 4. ≈ 4,29. 5. Energía por unidad de tiempo: J/s.
</details>

Con cuatro o cinco aciertos, sigue; con menos, repasa C01 y C06.

## 5. Un caso real: el Sol como termómetro

NASA da para el Sol una luminosidad de 382,8 × 10²⁴ W, un radio medio de 695 700 km y una temperatura efectiva de 5772 K (S1). Con la ley de Stefan–Boltzmann puedes obtener la temperatura a partir de las otras dos y comprobar que coincide con la publicada. Con el semieje mayor de la órbita terrestre (S2) obtendrás además el flujo solar a 1 au, unos 1361 W/m², y la temperatura de equilibrio de un cuerpo negro esférico a esa distancia. Límite: la «temperatura efectiva» es la de un cuerpo negro que emitiría esa luminosidad; la fotosfera real no es un cuerpo negro perfecto.

## 6. Vocabulario

La **temperatura** `T` mide el estado térmico; en el SI se expresa en kelvin (K), donde `0 K` es el cero absoluto. El SI fija la **constante de Boltzmann** `k_B = 1,380 649 × 10⁻²³ J/K` (S3), que define el kelvin. El **calor** `Q` es energía transferida por una diferencia de temperatura (J). La **energía térmica** es la energía cinética y potencial desordenada de las partículas. La **capacidad calorífica específica** `c` es la energía por kilogramo y por kelvin (J/(kg·K)). La **radiación térmica** es la emisión electromagnética de todo cuerpo con temperatura. Un **cuerpo negro** absorbe toda la radiación incidente y emite según `P = σ A T⁴`, con `σ = 5,670 374 419… × 10⁻⁸ W/(m²·K⁴)` (S4). La **temperatura de equilibrio** es la que iguala potencia absorbida y emitida.

## 7. Modelo mental: lo que entra, lo que sale

La temperatura de un satélite no la fija una «fuente de calor», sino el balance entre lo que absorbe del Sol y lo que irradia al espacio.

```mermaid
flowchart LR
    A["Luz solar: S × área"] --> B["Absorbida por el cuerpo"]
    B --> C["Energía térmica del cuerpo"]
    C --> D["Emisión: σ A T⁴"]
    D --> E["Equilibrio cuando entrada = salida"]
    E --> F["T de equilibrio"]
```

*Descripción textual:* la luz solar de potencia `S × área` es absorbida y aumenta la energía térmica; el cuerpo emite `σ A T⁴`; en el equilibrio, entrada y salida se igualan y eso fija la temperatura.

Una analogía: una bañera con el grifo abierto y el desagüe abierto. El nivel (temperatura) sube hasta que lo que entra iguala lo que sale. El límite: en la bañera la salida crece con el nivel de forma lineal; en la radiación crece como `T⁴`, mucho más rápido.

## 8. La explicación, paso a paso

### 8.1 Temperatura y energía de las partículas

En un gas ideal monoatómico, la energía cinética media de traslación de una partícula es `(3/2) k_B T`; a 288 K es `5,964 × 10⁻²¹ J` (37,2 meV). La rapidez cuadrática media es `v_rms = √(3 k_B T/m) = √(3 R T/M)`. Para un gas de masa molar 0,028 kg/mol (nitrógeno, supuesto no consultado), `v_rms = 506,5 m/s` a 288 K y `576,6 m/s` a 373,15 K. Una temperatura mayor significa partículas más rápidas, no más grandes. Comprobación: `N_A k_B = 8,314 462 618 J/(mol·K)` coincide con `R` (S3, S5, S6).

### 8.2 Calor y capacidad calorífica

Si un cuerpo recibe un calor `Q` sin cambiar de fase, `Q = m c ΔT`. Para 100 kg de un material con `c = 900 J/(kg·K)` (dato sintético), calentarlo de 250 K a 350 K requiere `9,0 × 10⁶ J`. Un cambio de temperatura de 1 K es igual a 1 °C, pero el cero de ambas escalas no coincide: en fórmulas con `T⁴` o `k_B T` solo vale kelvin.

### 8.3 Radiación y ley de Stefan–Boltzmann

Todo cuerpo emite una potencia `P = σ A T⁴` si es negro. Para una esfera de radio `R`, `A = 4π R²`. Aplicada al Sol: `T = [L/(4π R² σ)]^{1/4} = 5772,0 K` con los datos de S1, igual al valor publicado. Duplicar `T` multiplica la potencia emitida por 16.

### 8.4 Flujo solar y temperatura de equilibrio

A distancia `d` de una fuente de luminosidad `L`, el flujo es `S = L/(4π d²)`. A 1 au (`149,598 × 10⁶ km`, S2): `S = 1361,2 W/m²`. Un cuerpo negro esférico de radio `r` intercepta `S π r²` y emite `σ 4π r² T⁴`; igualando: `T = (S/(4σ))^{1/4} = 278,3 K = 5,2 °C`. La Tierra tiene una temperatura media de 288 K (S2): la diferencia (unos 10 K) se debe a que la Tierra no es un cuerpo negro (refleja parte de la luz) y a su atmósfera (que retiene calor). Esas contribuciones no se cuantifican aquí porque no se consultaron datos de albedo ni de composición atmosférica.

### 8.5 Dominio de validez

El modelo vale para un cuerpo isotermo, esférico, con absorción y emisión totales y sin otras fuentes de calor. Un satélite real tiene superficies con distintos acabados, zonas en sombra, electrónica que disipa calor y orientación variable; su análisis térmico requiere modelos más detallados.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Magnitud | Dimensión | Unidad SI | Valor o nota |
|---|---|---|---|---|
| `T` | temperatura | Θ | K | `T/K = t/°C + 273,15` |
| `k_B` | constante de Boltzmann | M L² T⁻² Θ⁻¹ | J/K | 1,380 649 × 10⁻²³ exacto (S3) |
| `N_A` | constante de Avogadro | mol⁻¹ | mol⁻¹ | 6,022 140 76 × 10²³ exacto (S5) |
| `R` | constante molar de los gases | M L² T⁻² mol⁻¹ Θ⁻¹ | J/(mol·K) | 8,314 462 618… exacto (S6) |
| `σ` | constante de Stefan–Boltzmann | M T⁻³ Θ⁻⁴ | W/(m²·K⁴) | 5,670 374 419… × 10⁻⁸ exacto (S4) |
| `Q` | calor | M L² T⁻² | J | `m c ΔT` |
| `S` | flujo de energía | M T⁻³ | W/m² | `L/(4π d²)` |

## 10. Convenciones y referencias

La temperatura se añade como cuarta dimensión (Θ) a las de C01 (M, L, T). Temperaturas en kelvin salvo indicación. Los valores del Sol y de la Tierra son **publicados**; el material con `c = 900 J/(kg·K)` y la masa molar de 0,028 kg/mol son **supuestos/sintéticos**; las temperaturas de equilibrio son **simuladas** con un modelo ideal.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NASA NSSDC, *Sun Fact Sheet* (act. 9-may-2024) | https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html | Luminosidad 382,8 × 10²⁴ W; radio medio 695 700 km; T efectiva 5772 K | Página consultada el 2026-11-05 |
| S2 | NASA NSSDC, *Earth Fact Sheet* (act. 15-nov-2024) | https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html | Semieje mayor 149,598 × 10⁶ km; temperatura media 288 K | Página consultada el 2026-11-05 |
| S3 | NIST, CODATA 2022, «Boltzmann constant» | https://physics.nist.gov/cgi-bin/cuu/Value?k | `k_B = 1,380 649 × 10⁻²³ J/K` exacto | Página consultada el 2026-11-05 |
| S4 | NIST, CODATA 2022, «Stefan-Boltzmann constant» | https://physics.nist.gov/cgi-bin/cuu/Value?sigma | `σ = 5,670 374 419… × 10⁻⁸ W m⁻² K⁻⁴` exacto | Página consultada el 2026-11-05 |
| S5 | NIST, CODATA 2022, «Avogadro constant» | https://physics.nist.gov/cgi-bin/cuu/Value?na | `N_A = 6,022 140 76 × 10²³ mol⁻¹` exacto | Página consultada el 2026-11-05 |
| S6 | NIST, CODATA 2022, «molar gas constant» | https://physics.nist.gov/cgi-bin/cuu/Value?r | `R = 8,314 462 618… J mol⁻¹ K⁻¹` exacto | Página consultada el 2026-11-05 |

Límites: la energía cinética media `(3/2)k_B T` y el balance de equilibrio son resultados clásicos deducidos aquí; no se cita un texto. No se consultaron datos de albedo ni de efecto invernadero.

## 12. Cómo ver el equilibrio

Tabla accesible de un gráfico de potencia emitida frente a temperatura para un metro cuadrado de cuerpo negro (cálculo propio).

| `T` (K) | `σ T⁴` (W/m²) |
|---|---|
| 200 | 90,7 |
| 278,3 | 340,2 |
| 288 | 390,1 |
| 400 | 1451,5 |

Descripción larga: una curva que crece con la cuarta potencia; el valor de unos 340 W/m² es la cuarta parte del flujo solar de 1361,2 W/m², que es el reparto de la luz interceptada por una esfera sobre toda su superficie.

## 13. Ejemplo trabajado: ¿a cuántos grados llega una esfera negra a 1 au?

**Planteamiento.** Una esfera ideal (negra, isoterma) en el espacio a 1 au del Sol, sin otras fuentes de calor. ¿Cuál es su temperatura de equilibrio?

**Paso 1 · Datos.** `L = 382,8 × 10²⁴ W` (S1), `d = 149,598 × 10⁹ m` (S2), `σ` (S4).

**Paso 2 · Flujo.** `S = L/(4π d²) = 1361,2 W/m²`.

**Paso 3 · Equilibrio.** `S π r² = σ 4π r² T⁴` ⇒ `T⁴ = S/(4σ) = 6,001 × 10⁹ K⁴` ⇒ `T = 278,3 K`.

**Paso 4 · Sentido físico.** 5,2 °C. El resultado no depende del radio ni de la masa. La Tierra, a la misma distancia, tiene 288 K (S2): la diferencia se explica por albedo y atmósfera, no cuantificados aquí. Para un satélite real, un acabado superficial distinto cambia mucho este valor.

## 14. Comparación de métodos

**Balance de energía** da la temperatura de equilibrio con muy pocos datos. **`Q = m c ΔT`** da tiempos o energías de calentamiento, pero ignora las pérdidas por radiación. **Modelo de nodos** (varios cuerpos que intercambian calor) es el siguiente paso en ingeniería; supera esta clase. Elige el balance global para estimar, y un modelo detallado para decidir.

## 15. Práctica guiada

**Ejercicio 1.** Convierte 288 K a °C y 25 °C a K. *Pasos:* sumar o restar 273,15.

<details><summary>Solución comentada</summary>

`288 − 273,15 = 14,85 °C`; `25 + 273,15 = 298,15 K`. Una diferencia de 1 K equivale a 1 °C.
</details>

**Ejercicio 2.** Calcula `(3/2) k_B T` a 300 K en julios. *Pista:* sección 8.1.

<details><summary>Solución comentada</summary>

`1,5 × 1,380 649 × 10⁻²³ × 300 = 6,21 × 10⁻²¹ J`.
</details>

**Ejercicio 3.** ¿Cuánta energía hace falta para elevar 50 kg con `c = 900 J/(kg·K)` en 20 K?

<details><summary>Solución comentada</summary>

`Q = 50 × 900 × 20 = 9,0 × 10⁵ J`. Dato sintético.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Si la temperatura de un cuerpo negro pasa de 200 K a 400 K, ¿por cuánto se multiplica su potencia emitida?

<details><summary>Solución comentada</summary>

`(400/200)⁴ = 16`.
</details>

**Ejercicio 5.** Calcula el flujo solar a 1,5 au (`d = 1,5 × 149,598 × 10⁹ m`) con `L` de S1.

<details><summary>Solución comentada</summary>

`S = 1361,2/1,5² = 604,9 W/m²`: cae con el cuadrado de la distancia (como la gravedad, C10).
</details>

**Ejercicio 6.** Calcula la temperatura de equilibrio de una esfera negra a 1,5 au.

<details><summary>Solución comentada</summary>

`T = 278,3 × 1,5^{-1/2} = 227,2 K`: `T ∝ d^{-1/2}`.
</details>

**Ejercicio 7.** Con la fórmula de la sección 8.3 y los datos de S1, calcula la potencia emitida por metro cuadrado de la superficie solar.

<details><summary>Solución comentada</summary>

`σ T⁴ = 5,670 × 10⁻⁸ × 5772⁴ = 6,294 × 10⁷ W/m²`, que coincide con el valor que da la ficha del Sol (62,94 × 10⁶ W/m²).
</details>

**Ejercicio 8.** ¿Por qué un cuerpo blanco y uno negro a 1 au tienen temperaturas de equilibrio distintas aunque el flujo sea el mismo?

<details><summary>Solución comentada</summary>

El blanco refleja parte de la luz y absorbe menos; para emitir lo que absorbe, alcanza una temperatura menor. El modelo de esta clase fija absorción total (albedo 0).
</details>

**Ejercicio 9 · transferencia.** Un artículo dice «en el espacio hace un frío de 0 K en todas partes». Contrasta con el caso de la sección 13.

<details><summary>Solución comentada</summary>

La temperatura de un objeto depende de su balance de radiación; a 1 au una esfera negra se equilibra cerca de 278 K, y lo que está en sombra se enfría más. «El espacio» no tiene una temperatura única para los cuerpos.
</details>

**Ejercicio 10 · transferencia.** Un compañero calcula `T` de equilibrio con grados Celsius en `σ T⁴`. ¿Qué pasa?

<details><summary>Solución comentada</summary>

Con `T = 5,2` (°C) obtendría una potencia absurdamente baja; `σ T⁴` exige kelvin. Se corrige convirtiendo a kelvin antes de elevar a la cuarta.
</details>

**Ejercicio 11 · transferencia.** Un satélite genera 500 W de calor interno. ¿Cómo cambia la temperatura de equilibrio si su área radiante es 4 m²? (modelo sintético: añade 500 W de entrada.)

<details><summary>Solución comentada</summary>

Añade `500/4 = 125 W/m²` a la potencia absorbida por m²; la emisión debe subir de `σ T₀⁴` a `σ T₀⁴ + 125` (con un reparto simplificado). Es un ejercicio de balance, no de diseño térmico.
</details>

**Ejercicio 12 · integrador.** Elabora un *balance térmico* (sección 20): para una esfera negra a una distancia `d` de tu elección (con `d` en au), calcula `S`, `T` de equilibrio, un `Q` de calentamiento sintético y declara qué ignora.

<details><summary>Solución modelo</summary>

Debe usar `L` de S1, `d` con unidades, `S`, `T = (S/4σ)^{1/4}`, un cálculo `Q = m c ΔT` rotulado sintético, la comparación de al menos un valor publicado y los supuestos (albedo 0, isoterma, sin atmósfera).
</details>

## 17. Laboratorio: Stefan–Boltzmann y equilibrio

El script [balance_termico.py](balance_termico.py) calcula la temperatura efectiva del Sol, el flujo a 1 au y la temperatura de equilibrio de una esfera negra; además la energía de traslación media y `v_rms`. Antes comprueba que `N_A k_B = R` (10⁻⁹) y que la temperatura efectiva calculada coincida con la de NASA (0,1 %).

**Datos:** publicados (S1–S6), más supuestos rotulados. **Predice antes de ejecutar:** ¿qué temperatura da el Sol? (5772 K.) **Resultados (2026-11-05, Python 3.12.9):** `N_A k_B = 8,314462618`; `T_efectiva = 5772,0 K`; `S = 1361,2 W/m²`; `T_equilibrio = 278,3 K` (5,2 °C); a 288 K: `(3/2)k_B T = 5,964 × 10⁻²¹ J` (37,23 meV), `v_rms(N₂, supuesto) = 506,5 m/s`; calentar 100 kg de 250 K a 350 K: `9,000 × 10⁶ J`.

```bash
python programa/clases/B05/B05-C13-temperatura-y-energia-termica/balance_termico.py
```

**Límites:** cuerpos negros isotermos; no hay atmósfera, albedo ni conducción; no es un modelo térmico de nave.

## 18. Errores frecuentes y cómo corregirlos

**Usar °C en fórmulas con `T⁴`.** Ejercicio 10. **Confundir calor con temperatura.** Ejercicios 2 y 3. **Pensar que el espacio tiene una sola temperatura.** Ejercicio 9. **Ignorar la dependencia `d⁻²` del flujo.** Ejercicio 5. **Creer que más masa implica otra temperatura de equilibrio.** Sección 13.

## 19. Cómo sabrás que vas bien

Tras 8.1: ¿qué relaciona `T` con la rapidez de las partículas? Repite el ejercicio 2. Tras 8.4: ¿por qué no importa el radio de la esfera? Revisa el ejercicio 6. Tras el laboratorio: ¿qué comprobación valida el modelo con datos del Sol? Léelo.

## 20. Qué entregas y cómo se evalúa

El producto es tu **balance térmico**: datos con fuente, flujo, temperatura de equilibrio, comparación y límites.

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Unidades (K, W/m²) | Errores | Parciales | Correctas | Verificación dimensional |
| Balance | Sin planteamiento | Con ayuda | Correcto | Compara con un valor publicado |
| Interpretación | Ausente | Parcial | Explica | Cuantifica una desviación |
| Alcance | No declara | Parcial | Declara | Distingue ideal de real |

**Condiciones críticas:** kelvin donde corresponda; rotular lo sintético; citar solo lo consultado.

## 21. Ética, seguridad y límites

El calor y el frío extremos dañan equipos y personas; esta clase es educativa y no sustituye el análisis térmico de misión ni normas de seguridad. Accesibilidad: ecuaciones en texto, tablas equivalentes de las gráficas, sin conexión.

## 22. Para cerrar y seguir

La temperatura mide la energía media de traslación de las partículas; el calor es energía en tránsito; un cuerpo se equilibra cuando lo que absorbe iguala lo que irradia, con `σ T⁴`. Queda abierto cómo se comporta el conjunto de partículas que llena un recipiente: gases y presión (C14).

**Glosario español–inglés.** temperatura · *temperature*; calor · *heat*; capacidad calorífica · *heat capacity*; cuerpo negro · *blackbody*; flujo · *flux*; cero absoluto · *absolute zero*; equilibrio radiativo · *radiative equilibrium*.

**Continuidad.** B05-C14 usa tu capacidad de **relacionar `T` con la energía de las partículas** para describir la presión de un gas y la atmósfera.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B05-C12 — Ondas mecánicas y frecuencia](../B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md) · [📚 Bloque B05](../../../tronco-comun/B05-fisica-fundamental-para-el-espacio.md) · [Siguiente: B05-C14 — Gases y presión →](../B05-C14-gases-y-presion/CLASE.md)
<!-- /nav -->
