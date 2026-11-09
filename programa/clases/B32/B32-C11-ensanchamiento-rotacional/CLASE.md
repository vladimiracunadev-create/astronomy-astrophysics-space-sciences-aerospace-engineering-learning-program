# B32-C11 — Ensanchamiento rotacional y v sin i

<!-- nav:top -->
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 11 del bloque B32. Nivel N3. La rotación estelar ensancha las líneas con un perfil conocido. Aquí evalúas el **kernel rotacional** con oscurecimiento del limbo lineal, verificas su normalización y su FWHM, y recuperas `v sin i` de una línea sintética convolucionada y con ruido. Usas [B12](../../../tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md) y [B32-C06](../B32-C06-micro-y-macroturbulencia/CLASE.md). La línea es sintética.

## 2. Por qué esta clase existe

`v sin i` es la rotación proyectada y da pistas de edad y actividad. La decisión central: **¿cómo se mide `v sin i` de un perfil?**

## 3. Lo que podrás hacer al terminar

1. Calcular `Δλ_L = λ v sin i/c`.
2. Evaluar el kernel de Gray.
3. Verificar `∫G = 1`.
4. Calcular el FWHM.
5. Convolucionar con una línea gaussiana.
6. Recuperar `v sin i`.

La evidencia es la **ficha del ensanchamiento rotacional** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es una intensidad específica?
2. ¿Qué es una temperatura efectiva?
3. ¿Qué es una integral numérica?
4. ¿Qué es una función fuente?
5. ¿Qué es un perfil de línea?

<details>
<summary>Ver respuestas</summary>

1. La energía por área, tiempo, frecuencia y ángulo sólido. 2. La del cuerpo negro que da el mismo flujo. 3. Una suma que aproxima un área. 4. `S = j/κ`. 5. La forma de la absorción en función de la longitud de onda.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Con `v sin i = 20 km/s` en 500 nm, `Δλ_L = 33,36 pm` y el FWHM del kernel es `1,559 Δλ_L`. Es el **ejemplo conductor**. El `v sin i` recuperado de la línea con ruido es `19,50 km/s` (error `2,5 %`). Todo es **sintético**.

## 6. Vocabulario

El **kernel rotacional**. El **oscurecimiento del limbo** `ε`. `v sin i` es la velocidad ecuatorial proyectada. El **ancho de rotación** `Δλ_L`. La **convolución**.

## 7. Modelo mental: un disco de vinilo

Un lado se acerca y otro se aleja: la luz de cada lado se desplaza al azul o al rojo y el borde del disco se mezcla en un perfil acampanado.

```mermaid
flowchart LR
    V["v sin i"] --> D["Δλ_L = λ v sin i/c"]
    D --> K["kernel G(Δλ)"]
    K --> C["⊗ línea gaussiana"]
    C --> F["ajuste"]
    F --> VR["v sin i recuperado"]
```

*Descripción textual:* la velocidad proyectada da el ancho del kernel; se convoluciona con la línea y se invierte por ajuste.

Analogía: un lado se acerca y otro se aleja: la luz de cada lado se desplaza al azul o al rojo y el borde del disco se mezcla en un perfil acampanado. Límite: rotación rígida y limbo lineal.

## 8. La explicación, paso a paso

### 8.1 Kernel

Con `λ = 500 nm` y `20 km/s`: `Δλ_L = 33,3564 pm`; normalización `1,00000006`; FWHM `1,5586 Δλ_L`; valor central `G(0)Δλ_L = 0,6933`.

### 8.2 Recuperación

La línea gaussiana intrínseca de 2 pm convolucionada con el kernel y con ruido de 0,01 se ajusta con una rejilla refinada: `v sin i = 19,50 km/s` (verdadero 20,00).

### 8.3 Lectura

El 2,5 % de error es compatible con el ruido y la resolución de la rejilla. Rotación y macroturbulencia producen perfiles parecidos (B32-C06); separarlos exige el perfil exacto.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `v sin i` | velocidad proyectada | km/s | 20 (ilustrativa) |
| `ε` | oscurecimiento del limbo | — | 0,6 (ilustrativo) |
| `Δλ_L` | ancho de rotación | pm | 33,36 |

## 10. Convenciones y referencias

Rotación rígida, limbo lineal; parámetros ilustrativos; semilla `20261109`.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S1 | NIST, *Fundamental Physical Constants* (CODATA 2022) | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | constantes citadas en la sección 9 | Consultada el 2026-11-09 |

Límites: no se consultó ningún perfil de una estrella real.

## 12. Cómo ver el kernel

| Magnitud | Valor |
|---|---|
| `Δλ_L` | 33,36 pm |
| FWHM | 1,559 `Δλ_L` |
| `v sin i` recuperado | 19,50 km/s |

Descripción larga: el kernel tiene ancho total cercano a `Δλ_L`.

## 13. Ejemplo trabajado: ancho de rotación

**Paso 1 · Cociente.** `v/c = 20 000/299 792 458 = 6,671 × 10⁻⁵`.

**Paso 2 · Producto.** `500 nm × 6,671 × 10⁻⁵`.

**Paso 3 · Valor.** `0,03336 nm`.

**Paso 4 · Lectura.** `33,36 pm`.

## 14. Distintas formas de describir una estrella que rota

**Por kernel:** Gray. **Por ancho:** `Δλ_L`. **Por ajuste:** `v sin i`.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** `Δλ_L` para 20 km/s a 500 nm. *Pasos:* ejemplo 13.

<details><summary>Solución comentada</summary>

`33,36 pm`.
</details>

**Ejercicio 2 · con una pista.** Para 40 km/s.

<details><summary>Solución comentada</summary>

`66,7 pm`.
</details>

**Ejercicio 3 · casi autónomo.** FWHM en pm.

<details><summary>Solución comentada</summary>

`1,5586 × 33,36 = 52,0 pm`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4.** Error relativo del recuperado.

<details><summary>Solución comentada</summary>

`2,5 %`.
</details>

**Ejercicio 5.** Normalización.

<details><summary>Solución comentada</summary>

1.
</details>

**Ejercicio 6.** `Δλ_L` en 600 nm y 20 km/s.

<details><summary>Solución comentada</summary>

`40,0 pm`.
</details>

**Ejercicio 7.** ¿Qué mide `sin i`?

<details><summary>Solución comentada</summary>

La proyección de la inclinación.
</details>

**Ejercicio 8.** `G(0)Δλ_L`.

<details><summary>Solución comentada</summary>

`0,6933`.
</details>

**Ejercicio 9 · transferencia.** **Transferencia.** Un compañero deriva la rotación real de una estrella con este perfil. Responde.

<details><summary>Solución comentada</summary>

Es sintético.
</details>

**Ejercicio 10 · transferencia.** **Transferencia.** ¿Por qué `sin i`?

<details><summary>Solución comentada</summary>

Porque solo se mide la componente proyectada.
</details>

**Ejercicio 11 · transferencia.** **Transferencia.** ¿Cómo se separa de la macroturbulencia?

<details><summary>Solución comentada</summary>

Con el perfil de Fourier; no se calcula aquí.
</details>

**Ejercicio 12.** **Integrador.** Elabora tu *ficha del ensanchamiento rotacional*: kernel, FWHM y recuperación.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.3.
</details>

**Ejercicio 12 · integrador.** **Integrador.** Elabora tu *ficha del ensanchamiento rotacional*: kernel, FWHM y recuperación.

<details><summary>Solución modelo</summary>

Secciones 8.1–8.3.
</details>

## 17. Laboratorio: kernel rotacional y recuperación

El script [vsini.py](vsini.py) evalúa el kernel y recupera `v sin i` (**comprueba** `10⁻⁶` y 5 %).

**Datos:** `c` de NIST; parámetros **ilustrativos**; semilla `20261109`. **Predice antes de ejecutar:** ¿cuánto vale `Δλ_L`? (≈33 pm.) **Ejecución del 2026-11-09 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Delta lambda_L = lambda v sin i/c = 33.3564 pm (v sin i = 20 km/s a 500 nm)
normalizacion Int G d(lambda) = 1.00000006
FWHM del kernel = 1.5586 Delta lambda_L ; maximo central G(0) dL = 0.6933
v sin i recuperado = 19.50 km/s (verdadero 20.00) ; error relativo = 2.50 %
Pruebas superadas.
```

```bash
python programa/clases/B32/B32-C11-ensanchamiento-rotacional/vsini.py
```

**Límites:** rotación rígida.

## 18. Errores frecuentes y cómo corregirlos

**Confundir `v` y `v sin i`.** Se corrige con la sección 6.

**Olvidar el limbo.** Se corrige con la sección 10.

**Confundir con macroturbulencia.** Se corrige con 8.3.

**Tomar el resultado por real.** Se corrige con la sección 10.

## 19. Cómo sabrás que vas bien

Tras 8: ¿qué resultado esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha del ensanchamiento rotacional** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | conceptos de la clase | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con el análisis | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | fuentes con fecha | Declara lo ilustrativo |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular la línea como sintética; no atribuir `v sin i` a una estrella; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

A 20 km/s y 500 nm el ensanchamiento es de 33 pm y se recupera `v sin i` con 2,5 % de error. Queda una pregunta: ¿cómo se detectan campos magnéticos?

**Glosario español–inglés.** ensanchamiento rotacional · *rotational broadening*; v sin i · *v sin i*; oscurecimiento del limbo · *limb darkening*; kernel · *kernel*; velocidad proyectada · *projected velocity*.

**Continuidad.** [B32-C12](../B32-C12-efecto-zeeman-estelar/CLASE.md) estudia el efecto Zeeman estelar.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

<!-- /nav -->
