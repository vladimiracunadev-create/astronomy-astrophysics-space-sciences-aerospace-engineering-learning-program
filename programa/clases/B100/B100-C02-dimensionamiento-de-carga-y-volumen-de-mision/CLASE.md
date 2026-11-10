# B100-C02 — Dimensionamiento de carga y volumen de misión

<!-- nav:top -->
[🏠 Programa](../../../../README.md) · [📚 Bloque B100](../../../tronco-comun/B100-logistica-y-cadena-de-suministro-extraterrestre.md) · [← Anterior: B100-C01 — Gestión de inventario de materias primas y piezas](../B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md) · [Siguiente: B100-C03 — Gestión de inventarios y reposición de suministros →](../B100-C03-gestion-de-inventarios-y-reposicion-de-suministros/CLASE.md)
<!-- /nav -->

## 1. Ubicación, nivel y alcance

Clase 2 del bloque B100, nivel N3. Antes de decidir cuándo reponer hay que saber cuánto llevar. Aquí calculas la masa y el volumen de los consumibles de una misión de superficie, añades embalaje y repuestos y trasladas esa carga a masa en órbita con la ecuación ideal del cohete. Parte de la clase [B100-C01](../B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md); el presupuesto de masa del vehículo es de [B83](../../../tronco-comun/B83-ingenieria-de-sistemas-y-diseno-de-misiones.md) y no se repite. Las tasas de consumo son **ilustrativas**.

## 2. Por qué esta clase existe

La masa que llega a la superficie es una fracción pequeña de la que sale de la Tierra, y el volumen puede decidir antes que la masa. La decisión central: **¿cuánta masa y cuánto volumen hay que cargar para N personas durante D días, y cuánta masa hay que lanzar para que esa carga llegue?**

## 3. Lo que podrás hacer al terminar

1. Calcular la masa y el volumen de consumibles por persona y día.
2. Añadir embalaje y repuestos como factores sobre la masa neta.
3. Aplicar la ecuación ideal del cohete por tramos y hacia atrás.
4. Obtener el factor de crecimiento de masa entre la órbita y la superficie.
5. Contar lanzadores o aterrizadores según su capacidad.
6. Rotular lo consultado (ecuación del cohete) y lo ilustrativo (tasas, factores, Δv).

La evidencia es la **ficha de carga de una misión de superficie** del ejercicio 12 (sección 20).

## 4. Con qué llegas y cómo comprobarlo

1. ¿Qué es la densidad aparente?
2. ¿Qué es un logaritmo natural?
3. ¿Qué es el Δv?
4. ¿Qué es la velocidad efectiva de escape?
5. ¿Qué es una fracción estructural?

<details>
<summary>Ver respuestas</summary>

1. La masa dividida por el volumen que ocupa el material, en kg/m³. 2. La función inversa de la exponencial de base e. 3. El cambio de velocidad que debe dar el propulsor para una maniobra, en m/s. 4. La velocidad equivalente de los gases, `ve = Isp · g₀`. 5. La parte de la masa de una etapa que es estructura y no propelente.
</details>

Con cuatro o cinco aciertos, sigue; si no, repasa los prerrequisitos.

## 5. Un caso de contexto y casos de referencia

Cuatro personas durante 30 días en la superficie necesitan `856,2 kg` de carga (consumibles netos `676,8 kg`, embalaje ×1,15 y repuestos del 10 %), que ocupan `71,13 m³` si el oxígeno se guarda como gas a densidad ambiente. Con tres tramos de Δv ilustrativos (3,1 + 0,9 + 1,9 km/s), `Isp = 450 s` y fracción estructural 0,10, hacen falta `3924,7 kg` en órbita baja: un factor `4,584`. Es el **ejemplo conductor**. Todo es **ilustrativo**: ninguna cifra describe una misión real.

## 6. Vocabulario

La **masa neta** es la de los consumibles. El **factor de embalaje** multiplica la masa por el envase y los soportes. Los **repuestos** se expresan como fracción de la masa. La **ecuación ideal del cohete** relaciona el cambio de velocidad con la razón de masas: `Δv = ve ln(m₀/m_f)`. El **factor de crecimiento de masa** es la masa en órbita dividida entre la masa en superficie. La **fracción estructural** `ε` es la estructura sobre el propelente de la etapa en este modelo.

## 7. Modelo mental: una mudanza por tramos

```mermaid
flowchart LR
    C["consumibles<br/>tasa x personas x días"] --> E["embalaje y<br/>repuestos"]
    E --> M["carga en<br/>superficie"]
    M --> T3["tramo 3<br/>LLO a superficie"]
    T3 --> T2["tramo 2<br/>TLI a LLO"]
    T2 --> T1["tramo 1<br/>LEO a TLI"]
    T1 --> L["masa en LEO"]
```

*Descripción textual:* la carga neta se infla por el embalaje y los repuestos, y luego se calcula, tramo a tramo y hacia atrás, la masa que debe existir antes de cada maniobra.

Analogía: en una mudanza cada piso que subes exige llevar también la ayuda para subir el resto. Límite: cada tramo usa una etapa nueva con fracción estructural constante; en una misión real las etapas se reutilizan o se dimensionan por separado.

## 8. La explicación, paso a paso

### 8.1 Masa y volumen de consumibles

Con 4 personas y 30 días (120 persona-día): oxígeno `0,84 × 120 = 100,8 kg` (a `1,43 kg/m³`, `70,49 m³`); agua `4,0 × 120 = 480,0 kg` (`0,480 m³`); alimento `0,80 × 120 = 96,0 kg` (`0,160 m³`). Total neto `676,8 kg` y `71,13 m³`. El oxígeno como gas a densidad ambiente domina el volumen aunque pese menos que el agua: el **envase** decide el volumen, no la masa.

### 8.2 Embalaje y repuestos

`676,8 × 1,15 = 778,3 kg`; repuestos `10 % × 778,3 = 77,8 kg`; carga total `856,2 kg`.

### 8.3 Ecuación del cohete hacia atrás

`ve = 450 × 9,80665 = 4413,0 m/s`. Para cada tramo, `r = exp(Δv/ve)` y, con `m_f = m_carga/(1 − ε(r − 1))`, `m₀ = r m_f`. Resultado: antes del tramo LLO→superficie (1,9 km/s) `1391,7 kg`; antes de TLI→LLO (0,9 km/s) `1746,1 kg`; antes de LEO→TLI (3,1 km/s) `3924,7 kg`. El factor de crecimiento es `3924,7/856,2 = 4,584`.

### 8.4 Segunda vía

Con `ε = 0` los factores se multiplican: `exp(3,1/4,413) × exp(0,9/4,413) × exp(1,9/4,413) = 3,807456`, igual que un tramo único de 5,9 km/s. La estructura eleva el factor de 3,807 a 4,584 (+20,4 %). Recuperar el Δv de la razón de masas devuelve `1900,000000 m/s`. Con aterrizadores de 1500 kg de carga bastan **1**.

## 9. Magnitudes, símbolos y unidades

| Símbolo | Qué es | Unidad | Valor / nota |
|---|---|---|---|
| `ṁ` | tasa de consumo | kg/(persona·d) | 0,84; 4,0; 0,80 (ilustrativas) |
| `ρ` | densidad aparente | kg/m³ | 1,43; 1000; 600 (ilustrativas) |
| `ve` | velocidad efectiva | m/s | 4413,0 |
| `Δv` | cambio de velocidad | m/s | 3100; 900; 1900 (ilustrativos) |
| `ε` | fracción estructural | — | 0,10 (ilustrativa) |
| `m_LEO` | masa en órbita baja | kg | 3924,7 |

## 10. Convenciones y referencias

Masas en kg, volúmenes en m³, Δv en m/s, tiempo en días. `g₀ = 9,80665 m/s²` (valor estándar). Modelo de etapa: estructura `= ε ×` propelente; sin pérdidas por gravedad ni resistencia aparte de las contenidas en el Δv ilustrativo. Todos los números de consumo y Δv son ilustrativos.

## 11. De dónde sale lo que afirmamos

| ID | Fuente | Localizador | Respalda | Estado |
|---|---|---|---|---|
| S3 | NASA Glenn, Ideal Rocket Equation — https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/ideal-rocket-equation/ (consultada 2026-11-10) | página completa | Δu = V_eq ln(m_f/m_e) (m_f: masa inicial; m_e: masa final vacía) | Consultada |
| — | Constantes exactas del SI (g₀ = 9,80665 m/s², c = 299 792 458 m/s, R = 8,314462618 J/(mol·K)) | — | valores que usa el laboratorio | No consultada en esta sesión |
| — | Tasas de consumo, eficiencias, Δv de la red cislunar, energías de rodadura, tasas de degradación y masas de equipos | — | todos los números marcados como ilustrativos | No consultados; ilustrativos |

Límites: las tasas de consumo, densidades, factores, Δv, Isp y ε no se consultaron; el resultado no es el presupuesto de una misión real.

## 12. Cómo ver la carga

| Magnitud | Valor |
|---|---|
| consumibles netos | 676,8 kg |
| carga con embalaje y repuestos | 856,2 kg |
| volumen neto | 71,13 m³ |
| masa en LEO | 3924,7 kg |
| factor de crecimiento | 4,584 |

Descripción larga: la carga se infla un 26,5 % por embalaje y repuestos y luego casi se quintuplica por la ecuación del cohete.

## 13. Ejemplo trabajado: el agua de 30 días

**Paso 1 · Persona-días.** `4 × 30 = 120`.

**Paso 2 · Masa.** `4,0 × 120 = 480 kg`.

**Paso 3 · Volumen.** `480/1000 = 0,48 m³`.

**Paso 4 · Con embalaje y repuestos.** `480 × 1,15 × 1,10 = 607,2 kg`.

## 14. Distintas formas de describir una carga

**Por masa neta** y **por volumen**. **Por factores:** embalaje y repuestos. **Por masa en origen:** factor de crecimiento. **Por capacidad:** número de aterrizadores. La masa de una carga depende de dónde se mide: en la superficie o en órbita.

## 15. Práctica guiada

**Ejercicio 1 · con los pasos indicados.** Calcula la masa de oxígeno de 4 personas en 30 días con `0,84 kg/(persona·d)`. *Pasos:* persona-días y producto.

<details><summary>Solución comentada</summary>

`0,84 × 120 = 100,8 kg`.
</details>

**Ejercicio 2 · con una pista.** Calcula `ve` para `Isp = 450 s`. *Pista:* `g₀ = 9,80665 m/s²`.

<details><summary>Solución comentada</summary>

`450 × 9,80665 = 4413,0 m/s`.
</details>

**Ejercicio 3 · casi autónomo.** Calcula la carga total desde `676,8 kg` neta con embalaje 1,15 y repuestos 10 %. *Pasos:* aplica los factores en cadena.

<details><summary>Solución comentada</summary>

`676,8 × 1,15 = 778,3`; `778,3 × 1,10 = 856,2 kg`.
</details>

## 16. Práctica autónoma, transferencia e integrador

**Ejercicio 4 · autónomo.** Volumen del alimento seco a 600 kg/m³.

<details><summary>Solución comentada</summary>

`96,0/600 = 0,160 m³`.
</details>

**Ejercicio 5 · autónomo.** Factor de crecimiento si la masa en LEO es `3924,7 kg` y la de superficie `856,2 kg`.

<details><summary>Solución comentada</summary>

`3924,7/856,2 = 4,584`.
</details>

**Ejercicio 6 · autónomo.** ¿Cuántos aterrizadores de 1500 kg se necesitan para 60 días de misión?

<details><summary>Solución comentada</summary>

Carga `2 × 856,2 = 1712,3 kg`; `⌈1712,3/1500⌉ = 2`.
</details>

**Ejercicio 7 · autónomo.** ¿Cuánto sube el factor de la ecuación por la estructura (3,807 → 4,584)?

<details><summary>Solución comentada</summary>

`4,584/3,807 = 1,204`: un 20,4 % más.
</details>

**Ejercicio 8 · autónomo.** Con 6 personas y 30 días, ¿cuál es la masa neta de consumibles?

<details><summary>Solución comentada</summary>

Proporcional a las personas: `676,8 × 6/4 = 1015,2 kg`.
</details>

**Ejercicio 9 · transferencia.** Si el oxígeno se guardara líquido a unos 1140 kg/m³ (valor ilustrativo, no consultado), ¿qué volumen tendría?

<details><summary>Solución comentada</summary>

`100,8/1140 = 0,088 m³`, frente a `70,49 m³` como gas ambiente: el envase cambia el volumen en un factor ≈800.
</details>

**Ejercicio 10 · transferencia.** Un proveedor ofrece una carga de 10 % menos de masa pero con embalaje 1,30. ¿Conviene?

<details><summary>Solución comentada</summary>

Calcula `0,90 × 1,30 = 1,17` frente a `1,15`: no conviene si el resto es igual; los factores se multiplican.
</details>

**Ejercicio 11 · transferencia.** Si el Δv del último tramo sube de 1,9 a 2,09 km/s (+10 %), ¿cambia `r` en la misma proporción?

<details><summary>Solución comentada</summary>

No: `r = exp(Δv/ve)` pasa de 1,538 a 1,606 (+4,4 %); el efecto es exponencial en el exponente.
</details>

**Ejercicio 12 · integrador.** Elabora tu *ficha de carga de una misión de superficie*: tabla de consumibles con masa y volumen, factores, masa por tramo hacia atrás, factor de crecimiento y rótulo de lo consultado e ilustrativo.

<details><summary>Solución comentada</summary>

Secciones 8.1–8.4 y la salida del laboratorio.
</details>

## 17. Laboratorio: carga de una misión de superficie y masa en órbita

El script [carga.py](carga.py) calcula masa y volumen de tres consumibles, aplica embalaje y repuestos, resuelve la ecuación del cohete hacia atrás en tres tramos (**comprueba** el producto de factores con `ε = 0` a 1e-9 y la recuperación del Δv).

**Datos:** ecuación ideal del cohete (NASA Glenn, consultada); tasas, densidades, factores, Δv, Isp y ε **ilustrativos**; `g₀` estándar no consultado. **Predice antes de ejecutar:** ¿el factor de crecimiento será mayor o menor que 3,807? (Mayor: la estructura añade masa.) **Ejecución del 2026-11-10 (Python 3.12.9):**

```text
Python 3.12.9 (biblioteca estandar)
Datos ILUSTRATIVOS: tasas de consumo, densidades, embalaje, repuestos, Isp, fraccion estructural y Delta-v
 consumible   masa [kg]   volumen [m3]
 oxigeno         100.8       70.490
 agua            480.0        0.480
 alimento         96.0        0.160
Consumibles netos 676.8 kg ; con embalaje 778.3 kg ; con repuestos 856.2 kg
Volumen neto de consumibles 71.130 m3
Masa que debe existir antes de cada tramo (hacia atras):
  antes de LLO->superficie      1391.7 kg
  antes de TLI->LLO             1746.1 kg
  antes de LEO->TLI             3924.7 kg
Factor de crecimiento masa en LEO / masa en superficie = 4.584
Con estructura nula: producto por tramo 3.807456 ; tramo unico 3.807456
Delta-v recuperado del tramo final = 1900.000000 m/s (dato 1900)
Aterrizadores de 1500 kg de carga necesarios: 1
Pruebas superadas.
```

```bash
python programa/clases/B100/B100-C02-dimensionamiento-de-carga-y-volumen-de-mision/carga.py
```

**Límites:** etapas con fracción estructural constante, sin pérdidas ni márgenes de misión; las tasas no vienen de una norma.

## 18. Errores frecuentes y cómo corregirlos

**Medir solo la masa y olvidar el volumen.** Se corrige con 8.1

**Sumar los factores en lugar de multiplicarlos.** Se corrige con 8.2

**Suponer que la masa en órbita es proporcional al Δv.** Se corrige con 8.3

**Usar las tasas ilustrativas como requisito.** Se corrige con la sección 10

## 19. Cómo sabrás que vas bien

Tras la sección 8: ¿qué factor de crecimiento esperabas y cuál obtuviste? Si dudas, repasa el ejemplo 13. Tras el laboratorio: ¿qué comprueba? (ver la sección 17).

## 20. Qué entregas y cómo se evalúa

El producto es tu **ficha de carga de una misión de superficie** (ejercicio 12).

| Criterio | Inicial | En desarrollo | Logrado | Destacado |
|---|---|---|---|---|
| Conceptos | Los confunde | Parciales | Calcula masa, volumen y factor de crecimiento | Explica los límites |
| Cálculo | Sin unidades | Con errores | Tablas completas con unidades | Calcula casos nuevos |
| Numérico | Sin comprobar | Un caso | Contraste con una segunda vía | Interpreta las diferencias |
| Fuentes | Sin fuente | Sin fecha | Fuentes con fecha y estado | Declara lo ilustrativo y lo no consultado |
| Límites | No los nombra | Uno | Tres | Discute qué falta del modelo |

**Condiciones críticas (no se compensan con promedio):** rotular tasas, factores y Δv como ilustrativos; no presentar el resultado como el presupuesto de una misión; citar solo lo consultado.

## 21. Ética, seguridad y límites

Clase educativa: los modelos son simplificados y sus datos son sintéticos o ilustrativos; ningún resultado describe una operación real ni sustituye a los requisitos de una misión, a los datos de proveedores ni a las normas de la agencia. Accesibilidad: tablas equivalentes a las gráficas, fórmulas en texto, ejercicios sin conexión.

## 22. Para cerrar y seguir

Cuatro personas durante 30 días llevan `856,2 kg` a la superficie y exigen `3924,7 kg` en órbita (factor `4,584`). Queda una pregunta: ¿cuándo reponer si la próxima ventana tarda más de dos años?

**Glosario español–inglés.** masa neta · *net mass*; embalaje · *packaging*; ecuación del cohete · *rocket equation*; fracción estructural · *structural fraction*; carga útil · *payload*.

**Continuidad.** [B100-C03](../B100-C03-gestion-de-inventarios-y-reposicion-de-suministros/CLASE.md) calcula niveles de reposición y reservas de seguridad.

**Referencias:** ver sección 11.

<!-- nav:bottom -->
---

[← Anterior: B100-C01 — Gestión de inventario de materias primas y piezas](../B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md) · [📚 Bloque B100](../../../tronco-comun/B100-logistica-y-cadena-de-suministro-extraterrestre.md) · [Siguiente: B100-C03 — Gestión de inventarios y reposición de suministros →](../B100-C03-gestion-de-inventarios-y-reposicion-de-suministros/CLASE.md)
<!-- /nav -->
