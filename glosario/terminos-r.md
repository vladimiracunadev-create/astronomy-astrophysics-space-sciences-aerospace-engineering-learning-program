# Términos · R (parte 1 de 3)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · **R** · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: **1** · [2](terminos-r-2.md) · [3](terminos-r-3.md)

### R̂ dividido

- El R̂ dividido (*split-R̂*) divide cada cadena en dos mitades y compara.

💡 **Cómo se explica en la clase [B19-C04](../programa/clases/B19/B19-C04-diagnostico-de-convergencia-de-cadenas/CLASE.md):**
- Calcular a mano el R̂ dividido de varias cadenas cortas.
- El script [diagnosticos.py](diagnosticos.py) implementa `R̂` dividido, ESS y un HMC para el embudo de Neal.
- 🎯 **Por qué importa:** Una cadena que parece haberse estabilizado puede estar atrapada en una región de la posterior, o llevar meses de iteraciones en una sola zona y no haber visto la otra. Con una sola cadena y una mirada al gráfico, la tentación de decir «ya convergió» es fuerte.

📘 **Dónde se aprende** (1 clase): [B19-C04 · Diagnóstico de convergencia de cadenas](../programa/clases/B19/B19-C04-diagnostico-de-convergencia-de-cadenas/CLASE.md).

### R+1

- R+1 es el primer día tras el retorno.
- Holzmann propone, entre otras, R1 flujo simple sin recursión, R2 bucles con cota fija, R3 sin memoria dinámica tras la inicialización, R4 funciones de unas 60 líneas, R5 al menos 2 aserciones por función, R6 alcance mínimo y R7 comprobar los valores devueltos.

💡 **Cómo se explica en la clase [B88-C15](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md):**
- Se toman del texto de Holzmann: flujo simple sin recursión (R1), bucles con cota (R2), unas 60 líneas por función (R4), mínimo de dos aserciones por función (R5) y comprobar valores devueltos (R7).
- Paso 1 · Recursión. `factorial` llama a `factorial`: R1.
- 🎯 **Por qué importa:** Un defecto que el compilador acepta puede costar una misión: recursión sin cota, bucles que no terminan, valores de retorno ignorados. La decisión central: ¿qué reglas simples y verificables mecánicamente reducen esas clases de error?

📘 **Dónde se aprende** (2 clases): [B88-C15 · Análisis estático de código](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md); [B107-C08 · Evaluación funcional posterior al vuelo](../programa/clases/B107/B107-C08-evaluacion-funcional-posterior-al-vuelo/CLASE.md).

### R2

- Holzmann propone, entre otras, R1 flujo simple sin recursión, R2 bucles con cota fija, R3 sin memoria dinámica tras la inicialización, R4 funciones de unas 60 líneas, R5 al menos 2 aserciones por función, R6 alcance mínimo y R7 comprobar los valores devueltos.

💡 **Cómo se explica en la clase [B88-C15](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md):**
- Se toman del texto de Holzmann: flujo simple sin recursión (R1), bucles con cota (R2), unas 60 líneas por función (R4), mínimo de dos aserciones por función (R5) y comprobar valores devueltos (R7).
- Paso 2 · Bucle. `while True` sin `break` ni `return`: R2.
- 🎯 **Por qué importa:** Un defecto que el compilador acepta puede costar una misión: recursión sin cota, bucles que no terminan, valores de retorno ignorados. La decisión central: ¿qué reglas simples y verificables mecánicamente reducen esas clases de error?

📘 **Dónde se aprende** (1 clase): [B88-C15 · Análisis estático de código](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md).

### R3

- Holzmann propone, entre otras, R1 flujo simple sin recursión, R2 bucles con cota fija, R3 sin memoria dinámica tras la inicialización, R4 funciones de unas 60 líneas, R5 al menos 2 aserciones por función, R6 alcance mínimo y R7 comprobar los valores devueltos.

🎯 **Por qué importa (clase B88-C15):** Un defecto que el compilador acepta puede costar una misión: recursión sin cota, bucles que no terminan, valores de retorno ignorados. La decisión central: ¿qué reglas simples y verificables mecánicamente reducen esas clases de error?

📘 **Dónde se aprende** (1 clase): [B88-C15 · Análisis estático de código](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md).

### R4

- Holzmann propone, entre otras, R1 flujo simple sin recursión, R2 bucles con cota fija, R3 sin memoria dinámica tras la inicialización, R4 funciones de unas 60 líneas, R5 al menos 2 aserciones por función, R6 alcance mínimo y R7 comprobar los valores devueltos.

💡 **Cómo se explica en la clase [B88-C15](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md):**
- Se toman del texto de Holzmann: flujo simple sin recursión (R1), bucles con cota (R2), unas 60 líneas por función (R4), mínimo de dos aserciones por función (R5) y comprobar valores devueltos (R7).
- Ejercicio 10 · transferencia. Transferencia. ¿Qué cambia si se aplica R4 con 10 líneas?
- 🎯 **Por qué importa:** Un defecto que el compilador acepta puede costar una misión: recursión sin cota, bucles que no terminan, valores de retorno ignorados. La decisión central: ¿qué reglas simples y verificables mecánicamente reducen esas clases de error?

📘 **Dónde se aprende** (1 clase): [B88-C15 · Análisis estático de código](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md).

### R5

- Holzmann propone, entre otras, R1 flujo simple sin recursión, R2 bucles con cota fija, R3 sin memoria dinámica tras la inicialización, R4 funciones de unas 60 líneas, R5 al menos 2 aserciones por función, R6 alcance mínimo y R7 comprobar los valores devueltos.

💡 **Cómo se explica en la clase [B88-C15](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md):**
- Se toman del texto de Holzmann: flujo simple sin recursión (R1), bucles con cota (R2), unas 60 líneas por función (R4), mínimo de dos aserciones por función (R5) y comprobar valores devueltos (R7).
- Paso 3 · Aserciones. Ninguna función tiene 2: R5 ×4.
- ⚠️ **Error frecuente:** Poner aserciones vacías. Deben comprobar algo real (R5)
- 🎯 **Por qué importa:** Un defecto que el compilador acepta puede costar una misión: recursión sin cota, bucles que no terminan, valores de retorno ignorados. La decisión central: ¿qué reglas simples y verificables mecánicamente reducen esas clases de error?

📘 **Dónde se aprende** (1 clase): [B88-C15 · Análisis estático de código](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md).

### R6

- Holzmann propone, entre otras, R1 flujo simple sin recursión, R2 bucles con cota fija, R3 sin memoria dinámica tras la inicialización, R4 funciones de unas 60 líneas, R5 al menos 2 aserciones por función, R6 alcance mínimo y R7 comprobar los valores devueltos.

🎯 **Por qué importa (clase B88-C15):** Un defecto que el compilador acepta puede costar una misión: recursión sin cota, bucles que no terminan, valores de retorno ignorados. La decisión central: ¿qué reglas simples y verificables mecánicamente reducen esas clases de error?

📘 **Dónde se aprende** (1 clase): [B88-C15 · Análisis estático de código](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md).

### R7

- Holzmann propone, entre otras, R1 flujo simple sin recursión, R2 bucles con cota fija, R3 sin memoria dinámica tras la inicialización, R4 funciones de unas 60 líneas, R5 al menos 2 aserciones por función, R6 alcance mínimo y R7 comprobar los valores devueltos.

💡 **Cómo se explica en la clase [B88-C15](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md):**
- Se toman del texto de Holzmann: flujo simple sin recursión (R1), bucles con cota (R2), unas 60 líneas por función (R4), mínimo de dos aserciones por función (R5) y comprobar valores devueltos (R7).
- Paso 4 · Retorno. `leer(x)` se llama como sentencia y devuelve valor: R7.
- 🎯 **Por qué importa:** Un defecto que el compilador acepta puede costar una misión: recursión sin cota, bucles que no terminan, valores de retorno ignorados. La decisión central: ¿qué reglas simples y verificables mecánicamente reducen esas clases de error?

📘 **Dónde se aprende** (1 clase): [B88-C15 · Análisis estático de código](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md).

### Racémica

- Una mezcla racémica contiene cantidades iguales de dos moléculas que son imágenes especulares una de otra.

🎯 **Por qué importa (clase B06-C16):** El análisis de las muestras de Bennu detectó aminoácidos (incluidos 14 de los 20 usados en la biología terrestre), aminas, formaldehído, ácidos carboxílicos, hidrocarburos aromáticos policíclicos y heterociclos de nitrógeno, entre ellos las cinco nucleobases del ADN y el ARN, además de unas 10 000 especies nitrogenadas (S1).

📘 **Dónde se aprende** (1 clase): [B06-C16 · Química orgánica esencial](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md).

### Radiación

- La radiación daña la red cristalina.

💡 **Cómo se explica en la clase [B86-C14](../programa/clases/B86/B86-C14-envejecimiento-de-paneles/CLASE.md):**
- Con la tasa de radiación duplicada, el factor a diez años baja de `78,40 %` a `67,48 %`: la radiación domina la incertidumbre del modelo.
- T["tiempo t"] --> R["radiación exp(-a t)"]
- 🎯 **Por qué importa:** Dimensionar un ala con su potencia de inicio de vida deja a la misión sin energía al final. El factor de fin de vida que se usó como `0,85` en la primera clase sale de un cálculo como este.

📘 **Dónde se aprende** (1 clase): [B86-C14 · Envejecimiento de paneles](../programa/clases/B86/B86-C14-envejecimiento-de-paneles/CLASE.md).

### Radiación de Cherenkov

- La radiación de Cherenkov ocurre si `β > 1/n`.

🎯 **Por qué importa (clase B31-C14):** Interpretar una señal exige saber qué partículas la producen y con qué precisión se mide su energía. La decisión central: ¿qué umbral y qué resolución tiene un detector?

📘 **Dónde se aprende** (1 clase): [B31-C14 · Detectores de partículas](../programa/clases/B31/B31-C14-detectores-de-particulas/CLASE.md).

### Radiación de fondo

- La radiación de fondo es un cuerpo negro cuya temperatura decae como `T(z) = T₀(1+z)`.

💡 **Cómo se explica en la clase [B26-C14](../programa/clases/B26/B26-C14-evolucion-termica-del-universo/CLASE.md):**
- Fixsen recopiló medidas de la temperatura de la radiación de fondo y obtuvo `T₀ = 2,72548 ± 0,00057 K` (S2, resumen).
- 🎯 **Por qué importa:** Casi todo lo observable del universo temprano (radiación de fondo, abundancia de helio) depende de su temperatura y de qué componente dominaba la densidad en cada época.

📘 **Dónde se aprende** (1 clase): [B26-C14 · Evolución térmica del universo](../programa/clases/B26/B26-C14-evolucion-termica-del-universo/CLASE.md).

### Radiación ionizante

- La radiación ionizante es la que tiene energía suficiente para arrancar electrones de átomos o moléculas (del orden de varios a decenas de eV o más); la no ionizante no la tiene.
- La radiación ionizante es la que produce ionización; incluye partículas energéticas (rayos cósmicos) y fotones muy energéticos.
- La radiación ionizante tiene energía suficiente para arrancar electrones; la no ionizante no.

💡 **Cómo se explica en la clase [B05-C18](../programa/clases/B05/B05-C18-electromagnetismo-y-radiacion/CLASE.md):**
- Distinguir radiación ionizante de no ionizante y explicar por qué importa.
- 🎯 **Por qué importa:** Un satélite se comunica con ondas de radio, un telescopio observa luz y rayos X, y la misma radiación a otras energías puede dañar electrónica y tejidos. La pregunta motivadora es: ¿qué es la radiación electromagnética, cómo se ordena por frecuencia y energía, cómo decae con la distancia y qué la hace peligrosa?

📘 **Dónde se aprende** (3 clases): [B05-C18 · Electromagnetismo y radiación](../programa/clases/B05/B05-C18-electromagnetismo-y-radiacion/CLASE.md); [B06-C18 · Fotoquímica y radiación](../programa/clases/B06/B06-C18-fotoquimica-y-radiacion/CLASE.md); [B68-C03 · Irradiación de hielos por rayos cósmicos y UV: radiólisis y productos](../programa/clases/B68/B68-C03-irradiacion-de-hielos-por-rayos-cosmicos-y-uv-radiolisis-y-productos/CLASE.md).

### Radiación neta (Rn)

- La radiación neta (Rn) es la energía que absorbe la superficie.

🎯 **Por qué importa (clase B115-C06):** El cultivo es el mayor flujo de agua de un hábitat con plantas. La decisión central: ¿cuánta agua transpira el cultivo, cuánta se recupera y cuánta hay que reponer, y con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B115-C06 · Balance de agua y evapotranspiración en cultivos](../programa/clases/B115/B115-C06-balance-de-agua-y-evapotranspiracion-en-cultivos/CLASE.md).

### Radiación sincrotrón

- La radiación sincrotrón es la emitida por electrones relativistas en un campo magnético.

💡 **Cómo se explica en la clase [B27-C12](../programa/clases/B27/B27-C12-radiacion-sincrotron/CLASE.md):**
- La evidencia es la ficha de radiación sincrotrón del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *ficha de radiación sincrotrón*: `U_B`, `P`, `ν_c`, `t` para cuatro `γ`, el índice espectral para tres `p` y la banda en que emite cada `γ`.
- 🎯 **Por qué importa:** El índice espectral de una fuente sincrotrón entrega el índice de energía de sus electrones; la frecuencia crítica entrega `γ²B`. Sin estas relaciones no se puede leer un espectro de radio o rayos X.

📘 **Dónde se aprende** (1 clase): [B27-C12 · Radiación sincrotrón](../programa/clases/B27/B27-C12-radiacion-sincrotron/CLASE.md).

### Radiación térmica

- La radiación térmica es la emisión electromagnética de todo cuerpo con temperatura.

🎯 **Por qué importa (clase B05-C13):** Un satélite recibe luz solar de un lado y emite calor al espacio por el otro, y la electrónica solo trabaja en un rango de temperaturas. La pregunta motivadora es: ¿qué es la temperatura, cómo se relaciona con la energía de las partículas y qué determina la temperatura de equilibrio de un cuerpo en el espacio?

📘 **Dónde se aprende** (1 clase): [B05-C13 · Temperatura y energía térmica](../programa/clases/B05/B05-C13-temperatura-y-energia-termica/CLASE.md).

### Radiador

- El radiador está a la temperatura que iguala su emisión con la carga más lo absorbido.
- El radiador emite `ε σ T⁴` por unidad de área.
- Carga térmica: potencia que hay que evacuar. Radiador: superficie que emite al espacio.

💡 **Cómo se explica en la clase [B85-C16](../programa/clases/B85/B85-C16-polvo-lunar-y-contaminacion/CLASE.md):**
- Con `14 g/m²` de polvo, `α_ef = 0,321` y la temperatura sube `20,38 K` respecto del radiador limpio (`322,22 K`).
- *Descripción textual:* la masa de polvo da el número de granos y la cobertura; junto con la película contaminante, determina la absortividad efectiva y la temperatura del radiador;
- 🎯 **Por qué importa:** Un radiador que se ensucia rechaza menos calor y se calienta; en la Luna la limpieza no es sencilla. La decisión central: ¿qué cobertura de polvo o espesor de película hace subir la temperatura de un radiador por encima de su límite?

📘 **Dónde se aprende** (3 clases): [B85-C16 · Polvo lunar y contaminación](../programa/clases/B85/B85-C16-polvo-lunar-y-contaminacion/CLASE.md); [B86-C17 · Energía nuclear espacial conceptual](../programa/clases/B86/B86-C17-energia-nuclear-espacial-conceptual/CLASE.md); [B106-C08 · Control térmico interior](../programa/clases/B106/B106-C08-control-termico-interior/CLASE.md).

### Radial

- La velocidad transversal es `h/r` y la radial, `μ e sin ν/h`.

💡 **Cómo se explica en la clase [B71-C06](../programa/clases/B71/B71-C06-momento-angular-especifico/CLASE.md):**
- Descomponer la velocidad en componente transversal `h/r` y radial.
- 🎯 **Por qué importa:** Si `h` es constante, el movimiento ocurre en un plano y la velocidad en el periapsis y el apoapsis queda ligada a la distancia. La decisión central: ¿qué dice `h` sobre la forma y la orientación de la órbita y cómo se usa para obtener velocidades?

📘 **Dónde se aprende** (1 clase): [B71-C06 · Momento angular específico](../programa/clases/B71/B71-C06-momento-angular-especifico/CLASE.md).

### Radián

- El radián (rad) es la unidad SI de ángulo plano.
- Un radián es el ángulo cuyo arco mide lo mismo que el radio;
- Un radián (rad) es el ángulo que abarca un arco de longitud igual al radio (S3); por tanto `180° = π rad`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C08](../programa/clases/B03/B03-C08-tiempo-y-conversiones-astronomicas/CLASE.md):**
- Convertir entre grados, minutos y segundos de arco y radianes.
- Ejercicio 9 · transferencia. Convierte `1″` a radianes y explica por qué es una cantidad tan pequeña.
- 🎯 **Por qué importa:** El período de Neptuno en las fichas de la NASA es 60 189,018 días. Nadie piensa en 60 mil días; se piensa en años.

📘 **Dónde se aprende** (5 clases): [B03-C08 · Tiempo y conversiones astronómicas](../programa/clases/B03/B03-C08-tiempo-y-conversiones-astronomicas/CLASE.md); [B03-C18 · Razones trigonométricas iniciales](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md); [B04-C06 · Identidades trigonométricas](../programa/clases/B04/B04-C06-identidades-trigonometricas/CLASE.md); [B05-C03 · Movimiento rectilíneo y circular](../programa/clases/B05/B05-C03-movimiento-rectilineo-y-circular/CLASE.md); [B09-C01 · Límites de funciones reales](../programa/clases/B09/B09-C01-limites-de-funciones-reales/CLASE.md).

### Radiancia

- La radiancia `B` (W m⁻² sr⁻¹) es la potencia por área proyectada y ángulo sólido.
- La radiancia `L` es la potencia por unidad de área proyectada, ángulo sólido y longitud de onda (W m⁻² sr⁻¹ m⁻¹).
- La radiancia `B(λ,T)` de Planck describe la emisión de un cuerpo negro.

💡 **Cómo se explica en la clase [B45-C01](../programa/clases/B45/B45-C01-radiometria-y-fotometria/CLASE.md):**
- Como el agua: la radiancia es el chorro por unidad de sección y ángulo; la exitancia, el caudal total del grifo por área; la irradiancia, lo que cae sobre una hoja de papel a cierta distancia.
- *Descripción textual:* la radiancia de Planck se integra en exitancia, se traslada a luminosidad e irradiancia y se convierte en fotones o lúmenes.
- ⚠️ **Error frecuente:** Olvidar el factor `π` entre radiancia y exitancia. Se corrige con 8.2.
- 🎯 **Por qué importa:** Todo flujo medido en un telescopio es una cantidad radiométrica o fotométrica con una definición precisa; confundir vatios, lúmenes y fotones arruina la calibración. La decisión central: ¿en qué unidades se expresa lo que llega al detector y cómo se pasa de una a otra?

📘 **Dónde se aprende** (3 clases): [B45-C01 · Radiometría y fotometría](../programa/clases/B45/B45-C01-radiometria-y-fotometria/CLASE.md); [B57-C01 · Fundamentos de teledetección](../programa/clases/B57/B57-C01-fundamentos-de-teledeteccion/CLASE.md); [B70-C05 · Actividad volcánica venusina: llanuras, coronas e indicios de actividad reciente](../programa/clases/B70/B70-C05-actividad-volcanica-venusina-llanuras-coronas-e-indicios-de-actividad-reciente/CLASE.md).

### Radiancia de banda

- La radiancia de banda `L_banda` es su integral en un intervalo de longitudes de onda.

💡 **Cómo se explica en la clase [B13-C17](../programa/clases/B13/B13-C17-calibracion-radiometrica/CLASE.md):**
- Integrar la radiancia en una banda espectral.
- Ejercicio 4. ¿Cuánto crece la radiancia de banda de `300` a `380 K`?
- 🎯 **Por qué importa:** Una cámara infrarroja de una nave mide el calor emitido por la superficie de un planeta. Sus cuentas no significan nada hasta saberse cuánta radiancia corresponde a cada una.

📘 **Dónde se aprende** (1 clase): [B13-C17 · Calibración radiométrica](../programa/clases/B13/B13-C17-calibracion-radiometrica/CLASE.md).

### Radiancia espectral

- La radiancia espectral `L_λ(T)` de un cuerpo negro es `2hc²/λ⁵ × 1/(exp(hc/λkT) − 1)`, en W m⁻² sr⁻¹ m⁻¹ (ley de Planck).
- La radiancia espectral `B_ν` es energía por área, tiempo, ángulo sólido y frecuencia.

💡 **Cómo se explica en la clase [B13-C17](../programa/clases/B13/B13-C17-calibracion-radiometrica/CLASE.md):**
- Integrar la radiancia en una banda espectral.
- 🎯 **Por qué importa:** Una cámara infrarroja de una nave mide el calor emitido por la superficie de un planeta. Sus cuentas no significan nada hasta saberse cuánta radiancia corresponde a cada una.

📘 **Dónde se aprende** (2 clases): [B13-C17 · Calibración radiométrica](../programa/clases/B13/B13-C17-calibracion-radiometrica/CLASE.md); [B28-C02 · Fotones en múltiples longitudes de onda](../programa/clases/B28/B28-C02-fotones-en-multiples-longitudes-de-onda/CLASE.md).

### Radiancia espectral de Planck

- La radiancia espectral de Planck `B(λ, T)` es la energía por unidad de tiempo, de área, de ángulo sólido y de longitud de onda que emite un cuerpo negro de temperatura `T` a la longitud de onda `λ`.

🎯 **Por qué importa (clase B22-C04):** Un espectro no trae escritas la temperatura ni la composición: trae un número de fotones por cada longitud de onda. Pasar de ahí a una propiedad física exige un modelo y una inversión.

📘 **Dónde se aprende** (1 clase): [B22-C04 · Inversión espectral](../programa/clases/B22/B22-C04-inversion-espectral/CLASE.md).

### Radiancia mixta

- La radiancia mixta es el promedio ponderado de las radiancias de fuego y fondo.

💡 **Cómo se explica en la clase [B57-C16](../programa/clases/B57/B57-C16-incendios-forestales/CLASE.md):**
- F["fuego 800 K, fraccion p"] --> M["radiancia mixta"]
- *Descripción textual:* la radiancia mixta sube mucho en 3,9 µm y poco en 11 µm, y de ambos canales salen la fracción y la temperatura; el ruido fija la fracción mínima detectable.
- 🎯 **Por qué importa:** Un incendio pequeño puede ser un desastre en horas, pero un píxel mide cientos de metros. La decisión central: ¿cuál es la fracción de píxel más pequeña que se puede detectar y cuánto sesga la estimación un error en el fondo?

📘 **Dónde se aprende** (1 clase): [B57-C16 · Incendios forestales](../programa/clases/B57/B57-C16-incendios-forestales/CLASE.md).

### Radiancia reflejada del cielo

- La radiancia reflejada del cielo es la parte de la radiancia atmosférica que la superficie refleja `(1 − ε)`.

💡 **Cómo se explica en la clase [B57-C21](../programa/clases/B57/B57-C21-sensores-infrarrojos-termicos-para-observacion-terrestre/CLASE.md):**
- Corregir la emisividad y la radiancia reflejada del cielo.
- ⚠️ **Error frecuente:** Ignorar la radiancia del cielo reflejada. Se corrige con 8.2.
- 🎯 **Por qué importa:** Una temperatura de superficie mal estimada engaña a quien estudia islas de calor, estrés hídrico, incendios o volcanes. La decisión central: ¿cuánto error introducen la atmósfera y la emisividad, y cómo se corrigen con dos bandas?

📘 **Dónde se aprende** (1 clase): [B57-C21 · Sensores infrarrojos térmicos para observación terrestre](../programa/clases/B57/B57-C21-sensores-infrarrojos-termicos-para-observacion-terrestre/CLASE.md).

### Radiante

- El radiante es el punto de la esfera celeste del que parecen venir los meteoros de una lluvia, hallado trazando hacia atrás sus trayectorias (S3).

💡 **Cómo se explica en la clase [B08-C18](../programa/clases/B08/B08-C18-introduccion-a-meteoros-y-lluvias/CLASE.md):**
- De la definición de ZHR (S3) se deduce, bajo supuestos declarados, que `ZHR = N · r^(6,5 − lm) / (T · sen h · (1 − c))`, donde `N` es el número de meteoros de la lluvia en `T` horas, `lm` la magnitud límite, `r` el índice de población (aquí 2,5, valor de ejemplo), `h` la altura del radiante y `c` la fracción de cielo cubierta por nubes.
- La corrección por `lm` aumenta el conteo cuando tu cielo es peor que 6,5; la de `h`, cuando el radiante está bajo.
- ⚠️ **Error frecuente:** Mirar al radiante. Sección 8.5 (práctica general).
- 🎯 **Por qué importa:** Cada año, titulares prometen «cientos de estrellas fugaces por hora». Con un cielo contaminado o con el radiante bajo el horizonte, verás muy pocas.

📘 **Dónde se aprende** (1 clase): [B08-C18 · Introducción a meteoros y lluvias](../programa/clases/B08/B08-C18-introduccion-a-meteoros-y-lluvias/CLASE.md).

### Radio

- El radio `R` es el de la superficie visible.
- El radio `R` es cuántos píxeles mira a cada lado (aquí 2).

💡 **Cómo se explica en la clase [B01-C14](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md):**
- Piensa en un triángulo con vértices temperatura, radio y luminosidad: dos de ellos fijan el tercero por Stefan–Boltzmann.
- *Descripción textual:* temperatura y radio determinan la luminosidad; luminosidad y distancia determinan el flujo recibido; la temperatura determina el color por la ley de Wien.
- 🎯 **Por qué importa:** Dos estrellas pueden verse igual de brillantes y ser totalmente distintas: una pequeña y cercana, otra enorme y lejana (C09). Para saber cómo es una estrella necesitas separar lo que ves (flujo) de lo que ella es (luminosidad, temperatura, radio) y de dónde está (distancia).

📘 **Dónde se aprende** (2 clases): [B01-C14 · Estrellas y sus principales propiedades](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md); [B14-C27 · Procesamiento por teselas de grandes volúmenes de imágenes](../programa/clases/B14/B14-C27-procesamiento-por-teselas-de-grandes-volumenes-de-imagenes/CLASE.md).

### Radio angular

- El radio angular `ρ` de la mancha es su tamaño visto desde el centro de la estrella.
- El radio angular `ρ` cumple `sin ρ = R/(R+h)`.

💡 **Cómo se explica en la clase [B24-C12](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md):**
- Si una mancha circular de radio angular `ρ` está en el centro del disco, su área proyectada es la de un disco de radio `R sen ρ`, `π R² sen²ρ`, y el flujo total del disco sin manchas es `π R²` (sin oscurecimiento al limbo).
- Es el ejemplo conductor: una mancha de 10° de radio angular y `4500 K` sobre una estrella de `5772 K` produce una caída máxima del `1,9 %` del flujo.
- ⚠️ **Error frecuente:** Confundir el radio angular con el radio físico. Se corrige con la sección 8.2.
- 🎯 **Por qué importa:** La modulación del brillo por manchas permite medir el periodo de rotación de miles de estrellas sin necesitar espectros, pero también contamina la búsqueda de exoplanetas y limita la precisión de las velocidades radiales.

📘 **Dónde se aprende** (2 clases): [B24-C12 · Manchas y actividad estelar](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md); [B87-C04 · Sensores terrestres](../programa/clases/B87/B87-C04-sensores-terrestres/CLASE.md).

### Radio centrífugo

- El radio centrífugo `r_c = j²/(GM)` es el radio donde una órbita circular tiene ese `j`.

💡 **Cómo se explica en la clase [B52-C01](../programa/clases/B52/B52-C01-colapso-de-nebulosa-protosolar/CLASE.md):**
- *Descripción textual:* la temperatura, la masa media y la densidad dan la masa de Jeans; si la nube la supera, colapsa en un tiempo de caída libre y su rotación fija el radio centrífugo, que se verifica integrando numéricamente.
- Paso 4 · Radio centrífugo. `r_c = j²/(GM) = 5.11 ua`.
- 🎯 **Por qué importa:** Sin colapso no hay protoestrella ni disco, y sin disco no hay planetas. La decisión central: ¿colapsa esta nube y a qué distancia del centro se detiene el material con momento angular?

📘 **Dónde se aprende** (1 clase): [B52-C01 · Colapso de nebulosa protosolar](../programa/clases/B52/B52-C01-colapso-de-nebulosa-protosolar/CLASE.md).

### Radio clásico del electrón

- El radio clásico del electrón `r_e` (S1).

🎯 **Por qué importa (clase B45-C11):** Las líneas de absorción dan abundancias, pero las líneas fuertes no son proporcionales a la cantidad de átomos. La decisión central: ¿en qué régimen está la línea y cómo se obtiene la columna?

📘 **Dónde se aprende** (1 clase): [B45-C11 · Líneas de absorción](../programa/clases/B45/B45-C11-lineas-de-absorcion/CLASE.md).

### Radio combinado

- El radio combinado `R` suma los radios de ambos objetos.

💡 **Cómo se explica en la clase [B118-C06](../programa/clases/B118/B118-C06-probabilidad-de-colision/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. ¿Por qué se usa el radio combinado y no el área de cada objeto por separado?
- Porque la colisión ocurre si los centros están a menos de la suma de los radios; el disco combinado representa esa condición en el plano de encuentro.
- 🎯 **Por qué importa:** Las alertas se priorizan por `Pc`, pero ese número depende de la covarianza que se suponga. La decisión central: ¿cuándo es fiable una `Pc` y cuándo es baja solo porque la incertidumbre es enorme?

📘 **Dónde se aprende** (1 clase): [B118-C06 · Probabilidad de colisión](../programa/clases/B118/B118-C06-probabilidad-de-colision/CLASE.md).

### Radio cuadrático medio

- El radio cuadrático medio `ρ` de los puntos del objeto mide su extensión.

💡 **Cómo se explica en la clase [B103-C07](../programa/clases/B103/B103-C07-estimacion-de-pose-de-objetos-y-objetivos-por-vision/CLASE.md):**
- Con `ρ = 57,74 mm` (radio cuadrático medio de los 9 puntos), `N = 9` y `f = 800 px`: `σ_Z/Z ≈ σ_px Z/(f ρ √N)`.
- rho (radio cuadratico medio de los puntos) = 57.74 mm
- 🎯 **Por qué importa:** A 8 m un marcador de 10 cm mide 10 px y su pose es casi indeterminada; a 1 m, el error de profundidad es de unos 3 mm. La decisión central: ¿hasta qué distancia es fiable la pose estimada con un objeto de cierto tamaño, y cuándo hay que dudar de ella?

📘 **Dónde se aprende** (1 clase): [B103-C07 · Estimación de pose de objetos y objetivos por visión](../programa/clases/B103/B103-C07-estimacion-de-pose-de-objetos-y-objetivos-por-vision/CLASE.md).

### Radio de 1,4 M☉

- La masa máxima `M_max` y el radio de 1,4 `M☉` `R_{1,4}` son los dos resúmenes de una EOS.

💡 **Cómo se explica en la clase [B27-C04](../programa/clases/B27/B27-C04-ecuacion-de-estado-nuclear/CLASE.md):**
- C cumple la de masa pero su radio es de `23 km`, muy lejos de lo medido;
- Una sola EOS por ley de potencias no logra a la vez radios de 12 km y masas de 2 `M☉`: hace falta endurecer a alta densidad.
- 🎯 **Por qué importa:** Las estrellas de neutrones son el único laboratorio de materia más allá de la densidad nuclear. Su EOS no se conoce con precisión; las medidas de masa máxima y de radio la acotan.

📘 **Dónde se aprende** (1 clase): [B27-C04 · Ecuación de estado nuclear](../programa/clases/B27/B27-C04-ecuacion-de-estado-nuclear/CLASE.md).

### Radio de Bohr

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B31-C09](../programa/clases/B31/B31-C09-interacciones-fundamentales/CLASE.md):**
- *Descripción textual:* las constantes dan `α`, el radio de Bohr y la razón de fuerzas; la masa del mediador da el alcance y el apantallamiento.
- radio de Bohr hbar/(m_e c alpha) = 5.291772105e-11 m ;
- 🎯 **Por qué importa:** Saber qué interacción domina en cada escala explica por qué los núcleos, los átomos y las estrellas son como son. La decisión central: ¿cuánto más fuerte es la fuerza eléctrica que la gravitatoria y qué fija el alcance de una fuerza?

📘 **Dónde se aprende** (1 clase): [B31-C09 · Interacciones fundamentales](../programa/clases/B31/B31-C09-interacciones-fundamentales/CLASE.md).

### Radio de Bondi

- El radio de Bondi `R_B = GM/c_s²` es donde la velocidad de escape iguala a la del sonido.

💡 **Cómo se explica en la clase [B52-C08](../programa/clases/B52/B52-C08-formacion-de-gigantes-gaseosos/CLASE.md):**
- *Descripción textual:* el disco da la masa térmica y el radio de Bondi; con el de Hill se obtiene el radio de captura; los guijarros fijan el tiempo de crecimiento.
- Un núcleo de `10 M⊕` captura gas hasta su radio de Bondi (`8.87e+06 km`); uno de `100 M⊕`, hasta su radio de Hill (`3.47e+07 km`).
- 🎯 **Por qué importa:** El orden de magnitud de la masa del núcleo y el tiempo en alcanzarlo deciden si hay gigantes gaseosos. La decisión central: ¿a qué masa un núcleo pasa de capturar gas hasta Bondi a capturarlo hasta Hill, y cuánto tarda en crecer?

📘 **Dónde se aprende** (1 clase): [B52-C08 · Formación de gigantes gaseosos](../programa/clases/B52/B52-C08-formacion-de-gigantes-gaseosos/CLASE.md).

### Radio de convergencia

- El radio de convergencia es la distancia máxima a `a` dentro de la cual la serie converge.

💡 **Cómo se explica en la clase [B09-C14](../programa/clases/B09/B09-C14-series-y-aproximaciones/CLASE.md):**
- Fuera del radio de convergencia (aquí `h > R`), la serie no vale.
- *Descripción textual:* se añaden términos de la serie hasta que la cota del resto sea menor que la tolerancia y se verifica que `x` esté dentro del radio de convergencia.
- ⚠️ **Error frecuente:** Usar la serie fuera de su radio de convergencia. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** Un cálculo orbital rápido usa `g(h) = g₀(1 − 2h/R)` para una altitud baja; uno más exigente necesita el siguiente término. Sin una cota del error no se sabe cuál usar.

📘 **Dónde se aprende** (1 clase): [B09-C14 · Series y aproximaciones](../programa/clases/B09/B09-C14-series-y-aproximaciones/CLASE.md).

### Radio de Einstein

- El radio de Einstein `θ_E` es el ángulo del anillo que se forma cuando la fuente está justo detrás de la lente.

💡 **Cómo se explica en la clase [B25-C14](../programa/clases/B25/B25-C14-lentes-gravitacionales-galacticas/CLASE.md):**
- Es un resultado general: la masa dentro del radio de Einstein sale solo del tamaño del anillo y de las distancias, sin suponer el perfil.
- *Descripción textual:* de la masa y las distancias se obtiene el radio de Einstein; con la posición de la fuente se resuelve la ecuación de la lente (dos imágenes) y se calcula la magnificación; a la inversa, de un anillo medido se deduce la masa interior.
- 🎯 **Por qué importa:** La luz de una galaxia lejana se curva al pasar cerca de una masa, y la masa interior se deduce del tamaño de la distorsión sin importar si es luminosa u oscura ni si está en equilibrio. Por eso las lentes son una prueba directa de la distribución de masa.

📘 **Dónde se aprende** (2 clases): [B25-C14 · Lentes gravitacionales galácticas](../programa/clases/B25/B25-C14-lentes-gravitacionales-galacticas/CLASE.md); [B29-C05 · Microlentes gravitacionales](../programa/clases/B29/B29-C05-microlentes-gravitacionales/CLASE.md).

### Radio de fusión inflado

- El radio de fusión inflado multiplica el radio físico para acelerar la simulación.

💡 **Cómo se explica en la clase [B52-C20](../programa/clases/B52/B52-C20-simulacion-de-formacion-planetaria-simplificada/CLASE.md):**
- Es el ejemplo conductor: una simulación sintética con radios de fusión inflados.
- 🎯 **Por qué importa:** Una simulación de formación sin sus controles de conservación no es evidencia de nada. La decisión central: ¿qué comprobaciones demuestran que la simulación se ejecutó correctamente antes de interpretar su resultado?

📘 **Dónde se aprende** (1 clase): [B52-C20 · Simulación de formación planetaria simplificada](../programa/clases/B52/B52-C20-simulacion-de-formacion-planetaria-simplificada/CLASE.md).

### Radio de giro

- El radio de giro es `r = m v/(|q| B)` y la frecuencia ciclotrónica `f = |q| B/(2π m)`.
- El radio de giro `r = m v⊥/(q B)`.

💡 **Cómo se explica en la clase [B05-C17](../programa/clases/B05/B05-C17-campos-magneticos/CLASE.md):**
- Calcular el radio y la frecuencia de giro de una partícula en un campo uniforme.
- 🎯 **Por qué importa:** La Tierra tiene un campo magnético que un satélite puede medir con un magnetómetro y que actúa sobre las partículas cargadas que lo atraviesan; además, una corriente a bordo crea su propio campo, que puede perturbar esas medidas.

📘 **Dónde se aprende** (2 clases): [B05-C17 · Campos magnéticos](../programa/clases/B05/B05-C17-campos-magneticos/CLASE.md); [B78-C08 · Propulsores Hall](../programa/clases/B78/B78-C08-propulsores-hall/CLASE.md).

### Radio de Hill

- El radio de Hill `R_H` es el límite gravitatorio frente a la estrella.
- El radio de Hill de un planeta es `R_H = a_p (GM_p/(3GM_☉))^{1/3}`.
- El radio de Hill es `R_H = a_p (GM_p/(3GM_☉))^{1/3}`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B52-C08](../programa/clases/B52/B52-C08-formacion-de-gigantes-gaseosos/CLASE.md):**
- *Descripción textual:* el disco da la masa térmica y el radio de Bondi; con el de Hill se obtiene el radio de captura; los guijarros fijan el tiempo de crecimiento.
- Un núcleo de `10 M⊕` captura gas hasta su radio de Bondi (`8.87e+06 km`); uno de `100 M⊕`, hasta su radio de Hill (`3.47e+07 km`).
- 🎯 **Por qué importa:** El orden de magnitud de la masa del núcleo y el tiempo en alcanzarlo deciden si hay gigantes gaseosos. La decisión central: ¿a qué masa un núcleo pasa de capturar gas hasta Bondi a capturarlo hasta Hill, y cuánto tarda en crecer?

📘 **Dónde se aprende** (6 clases): [B52-C08 · Formación de gigantes gaseosos](../programa/clases/B52/B52-C08-formacion-de-gigantes-gaseosos/CLASE.md); [B73-C18 · Satélites irregulares](../programa/clases/B73/B73-C18-satelites-irregulares/CLASE.md); [B73-C19 · Mecánica de sistemas lunares](../programa/clases/B73/B73-C19-mecanica-de-sistemas-lunares/CLASE.md); [B75-C16 · Navegación relativa a lunas](../programa/clases/B75/B75-C16-navegacion-relativa-a-lunas/CLASE.md); [B76-C01 · Sistema Tierra-Luna](../programa/clases/B76/B76-C01-sistema-tierra-luna/CLASE.md); [B76-C03 · Órbitas alrededor de la Luna](../programa/clases/B76/B76-C03-orbitas-alrededor-de-la-luna/CLASE.md).

### Radio de Hill mutuo

- El radio de Hill mutuo es `R_H,m = ((m₁+m₂)/(3M*))^(1/3) (a₁+a₂)/2`.
- El radio de Hill mutuo de dos planetas es `R_H = ((m₁+m₂)/(3M))^{1/3} (a₁+a₂)/2`.

💡 **Cómo se explica en la clase [B52-C10](../programa/clases/B52/B52-C10-arquitecturas-de-sistemas-exoplanetarios/CLASE.md):**
- *Descripción textual:* las masas y los semiejes dan el radio de Hill mutuo y el espaciado; los periodos validan los semiejes; con Δ constante se construye un sistema sintético.
- Paso 1 · Radio de Hill mutuo. Para Júpiter–Saturno, `R_H,m = ((1898+568)·10²⁴/(3·1,989·10³⁰))^(1/3)·(778,5+1432)/2·10⁹ m`.
- 🎯 **Por qué importa:** El espaciado mide cuán «apretado» está un sistema y cuán cerca está de la inestabilidad. La decisión central: ¿cómo se expresa el espaciado entre planetas independientemente de su escala?

📘 **Dónde se aprende** (2 clases): [B52-C10 · Arquitecturas de sistemas exoplanetarios](../programa/clases/B52/B52-C10-arquitecturas-de-sistemas-exoplanetarios/CLASE.md); [B73-C17 · Estabilidad de sistemas exoplanetarios](../programa/clases/B73/B73-C17-estabilidad-de-sistemas-exoplanetarios/CLASE.md).

### Radio de Laplace

- El radio de Laplace `r_L` (aquí definido igualando las dos tasas nodales) es `r_L⁵ = 2 J₂ R² a_p³ GM_p/GM_☉`; otras referencias lo definen con otro factor numérico.

💡 **Cómo se explica en la clase [B73-C19](../programa/clases/B73/B73-C19-mecanica-de-sistemas-lunares/CLASE.md):**
- Con esta definición Jápeto queda fuera del radio de Laplace y Titán dentro; la inclinación observada de Jápeto no se consultó.
- El radio de Hill de Júpiter es `53 147 206 km` y su radio de Laplace `2 324 328 km` (`32,5 R_J`): Calisto, a `0,81 r_L`, está cerca de donde el Sol domina.
- ⚠️ **Error frecuente:** Tomar el radio de Laplace por una frontera exacta. Se corrige con la sección 10: su factor depende de la definición.
- 🎯 **Por qué importa:** Un sistema lunar es un problema de varios perturbadores: el achatamiento del planeta aleja los nodos y los ápsides, el Sol los tira, y las lunas se perturban entre sí. Saber cuál domina a cada distancia decide en qué plano y con qué precesión se mueve una luna.

📘 **Dónde se aprende** (1 clase): [B73-C19 · Mecánica de sistemas lunares](../programa/clases/B73/B73-C19-mecanica-de-sistemas-lunares/CLASE.md).

### Radio de Larmor

- El radio de Larmor es el radio de la órbita circular de una carga en un campo.
- El radio de Larmor `r_L = mv_⊥/(|q|B)`.

💡 **Cómo se explica en la clase [B28-C01](../programa/clases/B28/B28-C01-fundamentos-de-mensajeros-astronomicos/CLASE.md):**
- *Descripción textual:* de la misma fuente salen cuatro mensajeros; la luz se dispersa en el plasma, los neutrinos y las ondas gravitacionales viajan rectos, y los rayos cósmicos se desvían según su radio de Larmor.
- Calcular el radio de Larmor `r_L = E/(Z e B c)` de una partícula cargada.
- 🎯 **Por qué importa:** Un solo evento, como una fusión de estrellas de neutrones, emite varios mensajeros que llegan por caminos y en momentos distintos. Entender por qué unos llegan alineados con la fuente y otros no es el primer paso para combinarlos.

📘 **Dónde se aprende** (2 clases): [B28-C01 · Fundamentos de mensajeros astronómicos](../programa/clases/B28/B28-C01-fundamentos-de-mensajeros-astronomicos/CLASE.md); [B30-C06 · Partículas cargadas y movimientos](../programa/clases/B30/B30-C06-particulas-cargadas-y-movimientos/CLASE.md).

### Radio de Mach 2

- El radio de Mach 2 es un criterio práctico, no un daño.

💡 **Cómo se explica en la clase [B58-C16](../programa/clases/B58/B58-C16-consecuencias-geofisicas-de-impactos/CLASE.md):**
- *Descripción textual:* la energía se reparte en una parte sísmica y otra en la onda; la solución autosemejante da el radio del frente y se busca donde su velocidad cae a Mach 2.
- Descripción larga: el radio de Mach 2 crece de `0.70` a `16.9 km`.
- 🎯 **Por qué importa:** Las consecuencias se miden por zonas: sismo, onda de choque, calor. Las escalas con la energía son lo que permite comparar casos.

📘 **Dónde se aprende** (1 clase): [B58-C16 · Consecuencias geofísicas de impactos](../programa/clases/B58/B58-C16-consecuencias-geofisicas-de-impactos/CLASE.md).

### Radio de marea

- El radio de marea `r_t` es donde la marea iguala la autogravedad.

💡 **Cómo se explica en la clase [B27-C16](../programa/clases/B27/B27-C16-eventos-de-disrupcion-por-marea/CLASE.md):**
- *Descripción textual:* de la estrella y la masa del agujero se obtienen el radio de marea y la dispersión de energía; de ahí salen el tiempo mínimo y la ley de caída; igualar `r_t` con el radio de Schwarzschild da la masa de Hills.
- Para ilustrar la mecánica se usa una estrella solar y un agujero de `10⁶ M☉` (valores sintéticos): el radio de marea es `0,4650 au = 23,56 r_s` y el residuo más ligado vuelve a los `40,95 d`.
- 🎯 **Por qué importa:** Estos eventos iluminan agujeros negros inactivos y permiten estimar su masa. Gezari revisa 56 de ellos (S3, resumen).

📘 **Dónde se aprende** (1 clase): [B27-C16 · Eventos de disrupción por marea](../programa/clases/B27/B27-C16-eventos-de-disrupcion-por-marea/CLASE.md).

### Radio de media luz

- El radio de media luz `r₁/₂` (3D) o `R_e` (2D, proyectado) contiene la mitad de la luz.

💡 **Cómo se explica en la clase [B25-C10](../programa/clases/B25/B25-C10-galaxias-irregulares-y-enanas/CLASE.md):**
- Su límite: el enjambre solo da la masa dentro de un radio concreto, el de media luz, no la masa total.
- *Descripción textual:* de la dispersión y el radio se obtiene la masa dentro del radio de media luz; dividida por la mitad de la luminosidad da la relación masa–luz, y si es mucho mayor que el valor mínimo de S2 domina la materia oscura.
- 🎯 **Por qué importa:** Las galaxias enanas son las más abundantes y las más ricas en materia oscura según su masa dinámica; además son los sitios donde las predicciones del modelo cosmológico se ponen a prueba. Pero con pocas estrellas medidas y sin rotación ordenada, su masa depende de un estimador.

📘 **Dónde se aprende** (1 clase): [B25-C10 · Galaxias irregulares y enanas](../programa/clases/B25/B25-C10-galaxias-irregulares-y-enanas/CLASE.md).

### Radio de media masa

- El radio de media masa `r_h` contiene la mitad de la masa.

💡 **Cómo se explica en la clase [B25-C06](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md):**
- El ejemplo conductor es un cúmulo sintético (no observado) de Plummer con `M = 2 × 10⁴ M☉` y radio de escala `a = 1,5 pc`, con masa media estelar `0,5 M☉` (ilustrativa).
- Describir un cúmulo con el perfil de Plummer: masa interior, radio de media masa, densidad central.
- 🎯 **Por qué importa:** La mayoría de las estrellas nace en grupos. Los cúmulos son laboratorios: sus estrellas comparten edad, distancia y composición.

📘 **Dónde se aprende** (1 clase): [B25-C06 · Cúmulos estelares](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md).

### Radio de nariz

- El radio de nariz `R_n` es el radio de curvatura del punto de remanso.

💡 **Cómo se explica en la clase [B77-C15](../programa/clases/B77/B77-C15-calentamiento-aerodinamico/CLASE.md):**
- *Descripción textual:* la trayectoria da densidad y velocidad en cada altitud; con el radio de nariz se obtiene el flujo, de él el pico, la temperatura de pared y la carga total; el ejemplo publicado valida las unidades.
- Descripción larga: el flujo máximo ocurre a mayor altitud que el de mayor frenado y crece con el cubo de la velocidad y con la inversa de la raíz del radio de nariz.
- 🎯 **Por qué importa:** El flujo de calor máximo y la carga total deciden qué material y qué espesor protegen al vehículo, y no se maximizan en el mismo punto que la desaceleración. La decisión central: ¿cuánto vale el flujo de pico, a qué altitud ocurre y cómo escala con el radio de la nariz y el coeficiente balístico?

📘 **Dónde se aprende** (1 clase): [B77-C15 · Calentamiento aerodinámico](../programa/clases/B77/B77-C15-calentamiento-aerodinamico/CLASE.md).

### Radio de Schwarzschild

- El radio de Schwarzschild es `r_s = 2GM/c²`.

💡 **Cómo se explica en la clase [B26-C07](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md):**
- El Sol, con `GM☉ = 1,327 124 4 × 10²⁰ m³/s²` y `R☉ = 6,957 × 10⁸ m` (S2), tiene un radio de Schwarzschild `r_s = 2GM/c² = 2953,25 m` (con `c` de S1) y una compacidad `r_s/R☉ = 4,245 × 10⁻⁶`.
- Calcular el radio de Schwarzschild de un cuerpo.
- 🎯 **Por qué importa:** Medir una distancia cerca de una masa grande no da lo mismo que en el espacio plano: el radio de un círculo y su circunferencia dejan de cumplir `C = 2πR`. Los GPS, las lentes gravitacionales y los agujeros negros dependen de esa diferencia.

📘 **Dónde se aprende** (1 clase): [B26-C07 · Curvatura y métricas](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md).

### Radio del lóbulo

- El radio del lóbulo `R_L` es el de la esfera de igual volumen.

💡 **Cómo se explica en la clase [B24-C22](../programa/clases/B24/B24-C22-evolucion-binaria-lobulo-de-roche-y-transferencia-de-masa/CLASE.md):**
- El lóbulo del donante pasa de `4,14 R☉` a `3,49 R☉` al transferirse `0,25 M☉` (Eggleton): si el radio del donante no cambia, lo desborda por un `19 %` y la transferencia se acelera.
- *Descripción textual:* con las masas y el semieje se obtiene el lóbulo de Roche; si el radio de la estrella llega al del lóbulo, la masa fluye por L1 y cambia las masas y la órbita.
- 🎯 **Por qué importa:** Una estrella que se expande (C16) o se hincha en una binaria puede llenar la región donde su gravedad domina y verter gas sobre su compañera. Esa transferencia cambia las masas, la órbita y el destino de ambas, y es el camino hacia muchos objetos exóticos.

📘 **Dónde se aprende** (1 clase): [B24-C22 · Evolución binaria: lóbulo de Roche y transferencia de masa](../programa/clases/B24/B24-C22-evolucion-binaria-lobulo-de-roche-y-transferencia-de-masa/CLASE.md).

### Radio efectivo

- El perfil de Sérsic describe el brillo superficial: `I(R) = I_e exp{−b_n [(R/R_e)^{1/n} − 1]}`, donde `R` es el radio proyectado, `R_e` el radio efectivo (contiene la mitad de la luz), `I_e` el brillo en `R_e`, `n` el índice de Sérsic y `b_n` una constante que depende de `n` y que garantiza que `R_e` contiene la mitad de la luz.
- El radio efectivo es donde `τ = 1`.
- El radio efectivo `R_e` contiene la mitad de la luz.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B25-C09](../programa/clases/B25/B25-C09-galaxias-elipticas-y-espirales/CLASE.md):**
- Relacionar el radio efectivo de un disco exponencial con su escala de longitud.
- 🎯 **Por qué importa:** Las galaxias parecen muy distintas: discos con brazos y gas, o bolas suaves de estrellas viejas. Esa diferencia guarda su historia (formación estelar, fusiones) y exige un lenguaje común para compararlas.

📘 **Dónde se aprende** (4 clases): [B25-C09 · Galaxias elípticas y espirales](../programa/clases/B25/B25-C09-galaxias-elipticas-y-espirales/CLASE.md); [B29-C12 · Espectroscopía de transmisión](../programa/clases/B29/B29-C12-espectroscopia-de-transmision/CLASE.md); [B38-C08 · Observaciones sintéticas de galaxias simuladas](../programa/clases/B38/B38-C08-observaciones-sinteticas-de-galaxias-simuladas/CLASE.md); [B58-C09 · Probabilidades de impacto](../programa/clases/B58/B58-C09-probabilidades-de-impacto/CLASE.md).

### Radio espectral

- El radio espectral `ρ(M)` es el mayor módulo de los autovalores de `M`; un mapa discreto `y_{k+1} = M y_k` es estable si `ρ(M) < 1`.
- El radio espectral es el factor con que se reduce el error por iteración en el modo más lento.

💡 **Cómo se explica en la clase [B10-C09](../programa/clases/B10/B10-C09-diagonalizacion-y-estabilidad/CLASE.md):**
- Distinguir estabilidad continua y estabilidad numérica (radio espectral).
- Euler explicito h=0.1: radio espectral = 1.04218; |x| tras 100 pasos = 42.407 (exacta 0.5334)
- 🎯 **Por qué importa:** Un panel solar largo y delgado vibra después de una maniobra. Si la vibración se amortigua, el panel es estable; si crece, hay un problema serio.

📘 **Dónde se aprende** (2 clases): [B10-C09 · Diagonalización y estabilidad](../programa/clases/B10/B10-C09-diagonalizacion-y-estabilidad/CLASE.md); [B21-C03 · Ecuación de Poisson: relajación y multigrid](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md).

### Radio gravitacional

- El radio gravitacional `r_g = GM/c²`.

🎯 **Por qué importa (clase B27-C07):** El espín cambia el ISCO y, con él, cuánta energía se libera: de `5,7 %` a más de `30 %` de la masa en reposo. La decisión central: ¿dónde están el horizonte y el ISCO para un espín dado y qué eficiencia implica?

📘 **Dónde se aprende** (1 clase): [B27-C07 · Métricas de agujeros negros](../programa/clases/B27/B27-C07-metricas-de-agujeros-negros/CLASE.md).

### Radio guía

- Un epiciclo es la pequeña oscilación radial de una estrella alrededor del radio guía `R_g`, el de la órbita circular con su mismo momento angular `L = Θ R_g`.

💡 **Cómo se explica en la clase [B25-C07](../programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/CLASE.md):**
- No hay brazos ni barra que muevan el radio guía, ni movimiento vertical, ni dependencia de la dispersión con la edad.
- Su límite: la «pista» es un potencial continuo y la estrella puede ir cambiando de radio guía por el paso de brazos o nubes, que aquí no se incluyen.
- 🎯 **Por qué importa:** Las estrellas de una galaxia no giran en círculos perfectos: oscilan alrededor de una órbita circular, y su agitación revela la edad y la historia de la población. Además, no nacen todas con la misma masa: la función de masa inicial fija cuántas hay de cada tipo y cuánta luz y metales producirán.

📘 **Dónde se aprende** (1 clase): [B25-C07 · Dinámica de poblaciones estelares](../programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/CLASE.md).

### Radio hidráulico

- El radio hidráulico `R_h = W d/(W + 2d)` es el área mojada dividida por el perímetro mojado.

💡 **Cómo se explica en la clase [B66-C01](../programa/clases/B66/B66-C01-valles-y-canales-morfologia-y-origen-en-superficies-planetarias/CLASE.md):**
- *Descripción textual:* de la geometría salen el radio hidráulico, la velocidad, el caudal, el número de Froude y la tensión de fondo; la velocidad se contrasta con Manning.
- Paso 1 · Radio hidráulico. `R_h = 0,9091 m`.
- 🎯 **Por qué importa:** Un valle visto desde órbita no dice por sí solo cuánta agua (o metano) pasó por él. La decisión central: ¿cuánto caudal transporta un canal de la misma geometría en otro cuerpo, y qué cambia además del caudal?

📘 **Dónde se aprende** (1 clase): [B66-C01 · Valles y canales: morfología y origen en superficies planetarias](../programa/clases/B66/B66-C01-valles-y-canales-morfologia-y-origen-en-superficies-planetarias/CLASE.md).

### Radio medio volumétrico

- Un radio medio volumétrico es el radio de la esfera con el mismo volumen que el cuerpo.
- El radio medio volumétrico es el radio de la esfera con el mismo volumen que el cuerpo (S1).

💡 **Cómo se explica en la clase [B03-C17](../programa/clases/B03/B03-C17-areas-y-volumenes-elementales/CLASE.md):**
- La ficha del Sol de la NASA da una masa de `1,9884 × 10³⁰ kg`, un volumen de `1,412 × 10¹⁸ km³` y una densidad media de 1408 kg/m³, y su radio medio volumétrico es de 695 700 km (S1).
- 🎯 **Por qué importa:** La NASA publica que la densidad media del Sol es 1408 kg/m³ (S1), cerca de una vez y media la del agua. ¿Cómo se obtiene?

📘 **Dónde se aprende** (2 clases): [B03-C17 · Áreas y volúmenes elementales](../programa/clases/B03/B03-C17-areas-y-volumenes-elementales/CLASE.md); [B07-C09 · Cálculos científicos básicos con Python](../programa/clases/B07/B07-C09-calculos-cientificos-basicos-con-python/CLASE.md).

### Radio rms

- El radio rms `ρ_rms` es la distancia angular cuadrática media de las estrellas al eje.

💡 **Cómo se explica en la clase [B87-C07](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md):**
- El balanceo se mide con el brazo de palanca `ρ_rms` (el radio medio de las estrellas, unos `4,3°`), mucho menor que 1 rad: `σ_roll ≈ σ_a/(√N ρ_rms)`, del orden de `14` veces el error transversal con 20 estrellas.
- 🎯 **Por qué importa:** Para apuntar un telescopio o una antena con precisión de segundos de arco, un sensor solar o un magnetómetro no bastan. La decisión central: ¿cuántas estrellas hacen falta y por qué el giro alrededor del eje óptico (balanceo) es mucho peor que el apuntamiento?

📘 **Dónde se aprende** (1 clase): [B87-C07 · Rastreadores estelares](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md).

### Radio síncrono

- El radio síncrono divide a los satélites que se alejan de los que se acercan.

💡 **Cómo se explica en la clase [B72-C16](../programa/clases/B72/B72-C16-modelado-de-mareas/CLASE.md):**
- La Luna (`384 400 km`, ficha de la Luna) está a `9,12 a_sinc`: fuera del radio síncrono, la marea la aleja.
- El signo de `da/dt` lo fija la posición respecto al radio síncrono: positivo fuera, negativo dentro.
- 🎯 **Por qué importa:** La marea alarga el día, aleja a la Luna y calienta a Ío y Europa; en un satélite bajo el radio síncrono (como Fobos) hace lo contrario y lo acerca. La decisión central: ¿hacia dónde y a qué velocidad cambia el semieje por la marea, según esté el satélite dentro o fuera del radio síncrono?

📘 **Dónde se aprende** (1 clase): [B72-C16 · Modelado de mareas](../programa/clases/B72/B72-C16-modelado-de-mareas/CLASE.md).

### Radio sónico

- El radio sónico es donde el flujo de Parker pasa de subsónico a supersónico.

💡 **Cómo se explica en la clase [B30-C02](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md):**
- Calcular la velocidad del sonido y el radio sónico `r_c = GM/(2c_s²)`.
- Ejercicio 7. Radio sónico de la corona en `R_☉`.
- 🎯 **Por qué importa:** La corona caliente es el origen del viento solar y de gran parte de la actividad. Entender por qué no puede estar en reposo conecta el Sol con el medio interplanetario.

📘 **Dónde se aprende** (1 clase): [B30-C02 · Fotosfera, cromosfera y corona](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md).

### Radiólisis

- La radiólisis es la destrucción química por radiación.

🎯 **Por qué importa (clase B55-C17):** Que un compuesto prebiótico llegue intacto hasta nosotros depende de cuánta radiación recibió, y que un exceso entre dos formas quirales sea real depende de cuántas moléculas se contaron. La decisión central: ¿cuánto sobrevive y con qué incertidumbre puedo afirmar un exceso enantiomérico distinto de cero?

📘 **Dónde se aprende** (1 clase): [B55-C17 · Compuestos prebióticos](../programa/clases/B55/B55-C17-compuestos-prebioticos/CLASE.md).

### Radionúclido de vida corta

- Un radionúclido de vida corta (como el 26Al) aporta calor mientras decae.

💡 **Cómo se explica en la clase [B52-C18](../programa/clases/B52/B52-C18-diferenciacion-planetaria/CLASE.md):**
- Calcular el calor específico `H₀` de un radionúclido con vida media corta.
- 🎯 **Por qué importa:** La energía disponible decide si un cuerpo funde y se diferencia o permanece primitivo. La decisión central: ¿cuánto calor aporta un radionúclido sin pérdidas y cuánta energía libera la diferenciación?

📘 **Dónde se aprende** (1 clase): [B52-C18 · Diferenciación planetaria](../programa/clases/B52/B52-C18-diferenciacion-planetaria/CLASE.md).

### Ráfaga

- FER: tasa de error de trama, `1 − (1 − p)^n`. Ráfaga: error en bits consecutivos.

💡 **Cómo se explica en la clase [B90-C16](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md):**
- Resultados medidos: 1 040 de 1 040 errores de 1 bit detectados; 20 000 de 20 000 errores dobles al azar; 20 000 de 20 000 ráfagas de hasta 16 bits.
- El CRC detecta todos los errores de 1 bit, de 2 bits y las ráfagas de hasta 16 bits probadas.
- 🎯 **Por qué importa:** Cada subsistema puede pasar sus pruebas y la cadena fallar: un formato de trama distinto, un retraso mayor que el tiempo de espera, un error de bit no detectado. La decisión central: ¿qué errores detecta la cadena, con qué frecuencia reintenta y cuánto tarda cada acuse?

📘 **Dónde se aprende** (1 clase): [B90-C16 · Pruebas de extremo a extremo](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md).

### RAIRS

- La RAIRS es una espectroscopía infrarroja de reflexión sobre una superficie metálica.

💡 **Cómo se explica en la clase [B68-C04](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md):**
- En RAIRS la calibración del espesor es distinta: Fayolle y colaboradores calibran la absorbancia de 1 ML con una desorción isotérmica monitoreada por RAIRS y la verifican con la TPD y con la exposición (9–10 ML).
- Fayolle y colaboradores (2011) vigilan el hielo con espectroscopía infrarroja de absorción–reflexión (RAIRS) y espectrometría de masas al mismo tiempo, con un flujo de sincrotrón del orden de `10¹⁴` fotones s⁻¹; Öberg y colaboradores (2009) usan una lámpara de hidrógeno de 7–10,5 eV a 15–60 K.
- 🎯 **Por qué importa:** Un hielo de 10 ML de CO sobre una superficie a 10 K se contamina con agua residual en horas si la presión de fondo no es lo bastante baja, y una TPD con bombeo insuficiente deforma el pico que se mide.

📘 **Dónde se aprende** (1 clase): [B68-C04 · Laboratorio de astroquímica de hielos en ultra alto vacío criogénico](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md).

### Raíz

- Una raíz es un valor de `x` que hace el polinomio igual a cero.

💡 **Cómo se explica en la clase [B04-C01](../programa/clases/B04/B04-C01-polinomios-y-factorizacion/CLASE.md):**
- División sintética. Si `r` es raíz de `p(x)`, entonces `(x − r)` es un factor: la división sintética calcula el cociente.
- Regla de las raíces racionales. Si el polinomio tiene coeficientes enteros y una raíz `p/q` en fracción irreducible, `p` divide al término independiente y `q` al coeficiente principal.
- ⚠️ **Error frecuente:** Olvidar un signo al dividir sintéticamente. Con raíz `r`, el factor es `(x − r)`: para la raíz −1, `(x + 1)`.
- 🎯 **Por qué importa:** Cuando un observatorio publica dónde está inclinado el eje de la Tierra, no da un solo número: da una *fórmula* para cada fecha, porque ese eje se mueve lentamente. Esa fórmula es un polinomio.

📘 **Dónde se aprende** (1 clase): [B04-C01 · Polinomios y factorización](../programa/clases/B04/B04-C01-polinomios-y-factorizacion/CLASE.md).

### Raíz cuadrada

- Una raíz cuadrada `√x` es el número positivo que, elevado al cuadrado, da `x`; una raíz cúbica `∛x` es el que, elevado al cubo, da `x`.

💡 **Cómo se explica en la clase [B03-C04](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md):**
- A --> R["Raíz cuadrada: deshace el cuadrado"]
- 🎯 **Por qué importa:** En 1619 Johannes Kepler publicó que el cuadrado del período de un planeta es proporcional al cubo del tamaño de su órbita. Hoy esa relación sigue sirviendo para estimar el período de cualquier objeto que orbita otro conocido.

📘 **Dónde se aprende** (1 clase): [B03-C04 · Potencias y raíces](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md).

### Raíz cúbica

- Una raíz cuadrada `√x` es el número positivo que, elevado al cuadrado, da `x`; una raíz cúbica `∛x` es el que, elevado al cubo, da `x`.

💡 **Cómo se explica en la clase [B03-C04](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md):**
- V --> R2["Raíz cúbica: deshace el cubo"]
- 🎯 **Por qué importa:** En 1619 Johannes Kepler publicó que el cuadrado del período de un planeta es proporcional al cubo del tamaño de su órbita. Hoy esa relación sigue sirviendo para estimar el período de cualquier objeto que orbita otro conocido.

📘 **Dónde se aprende** (1 clase): [B03-C04 · Potencias y raíces](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md).

### Raíz de la suma de cuadrados

- La suma de cuantilas es conservadora; la raíz de la suma de cuadrados (RSS) es optimista para sumar magnitudes.

💡 **Cómo se explica en la clase [B81-C14](../programa/clases/B81/B81-C14-presupuestos-de-maniobras-de-correccion/CLASE.md):**
- Combinar varias correcciones: suma de cuantilas, raíz de la suma de cuadrados y Monte Carlo de la suma.
- 🎯 **Por qué importa:** Un presupuesto muy bajo deja a la nave sin propelente; uno muy alto la lastra. La decisión central: ¿qué cuantila de `Δv` reservar para una o varias correcciones, y cómo se combinan?

📘 **Dónde se aprende** (1 clase): [B81-C14 · Presupuestos de maniobras de corrección](../programa/clases/B81/B81-C14-presupuestos-de-maniobras-de-correccion/CLASE.md).

### Raíz doble

- Una raíz doble ocurre cuando `Δ = 0`.

💡 **Cómo se explica en la clase [B04-C02](../programa/clases/B04/B04-C02-ecuaciones-lineales-y-cuadraticas/CLASE.md):**
- Segunda: `Δ = 0`, una raíz doble `x = 3` (es `(x − 3)²`).
- 🎯 **Por qué importa:** Una sonda desciende hacia la Luna; un instrumento cae desde una mesa de trabajo; una señal de radio viaja hasta un espejo y vuelve. En cada caso hay un número que no conoces (un tiempo, una distancia) y una relación que lo liga a otros que sí conoces.

📘 **Dónde se aprende** (1 clase): [B04-C02 · Ecuaciones lineales y cuadráticas](../programa/clases/B04/B04-C02-ecuaciones-lineales-y-cuadraticas/CLASE.md).

### Rama

- Una rama es cada bloque posible.
- Una rama es un puntero móvil a un commit;
- Una rama es cada mitad de la variedad a un lado del punto.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C04](../programa/clases/B07/B07-C04-condicionales-y-decisiones/CLASE.md):**
- Se evalúa cada condición en orden y solo se ejecuta la primera rama verdadera;
- Límite de la analogía: un cruce físico tiene un solo camino de salida porque el coche solo puede estar en un lugar; en un programa, si las preguntas están mal ordenadas, un dato puede «caer» en una rama que no corresponde.
- ⚠️ **Error frecuente:** Ordenar mal las ramas. Se corrige con el ejercicio 8.
- 🎯 **Por qué importa:** Toda clasificación astronómica es una decisión sobre un dato: ¿esta señal supera el ruido?, ¿esta estrella es más brillante que el umbral?, ¿esta imagen está saturada? Una decisión mal escrita no falla ruidosamente: clasifica mal en silencio, justo en los casos frontera, que son los que importan.

📘 **Dónde se aprende** (4 clases): [B07-C04 · Condicionales y decisiones](../programa/clases/B07/B07-C04-condicionales-y-decisiones/CLASE.md); [B07-C14 · Control de versiones con Git](../programa/clases/B07/B07-C14-control-de-versiones-con-git/CLASE.md); [B73-C06 · Variedades invariantes](../programa/clases/B73/B73-C06-variedades-invariantes/CLASE.md); [B101-C02 · Cinemática inversa y redundancia de manipuladores](../programa/clases/B101/B101-C02-cinematica-inversa-y-redundancia-de-manipuladores/CLASE.md).

### Rama asintótica de gigantes (AGB)

- La rama asintótica de gigantes (AGB) es la fase de masa baja e intermedia con un núcleo inerte de carbono y oxígeno rodeado de dos capas de fusión, de helio y de hidrógeno (descripción cualitativa estándar; las cifras no se consultaron).

💡 **Cómo se explica en la clase [B24-C21](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md):**
- python programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/proceso_s.py
- 🎯 **Por qué importa:** Las estrellas AGB son una fuente importante de carbono, nitrógeno y elementos pesados del medio interestelar, y sus abundancias superficiales son el registro observable de lo que ocurre en su interior.

📘 **Dónde se aprende** (1 clase): [B24-C21 · Rama asintótica de gigantes: pulsos térmicos y proceso s](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md).

### Rama corta

- La rama corta es el arco de menos de 180° y la larga el de más.

🎯 **Por qué importa (clase B75-C12):** No siempre se sale con la fase ideal, y el tiempo de vuelo no es dato sino variable. La decisión central: ¿qué tiempo de vuelo minimiza la suma de excesos hiperbólicos para una fase de salida dada y cuánto empeora el costo al apartarse de la fase ideal?

📘 **Dónde se aprende** (1 clase): [B75-C12 · Optimización de trayectoria](../programa/clases/B75/B75-C12-optimizacion-de-trayectoria/CLASE.md).

### Rama de las gigantes rojas

- La rama de las gigantes rojas es el tramo del diagrama HR donde la estrella sube en luminosidad con `T_ef` casi constante.

🎯 **Por qué importa (clase B24-C16):** Una gigante roja es mucho mayor y más luminosa que su estrella original y tiene una densidad media ínfima. Entender su tamaño, su gravedad y cómo crece su núcleo permite interpretar las gigantes observadas, usarlas como sondas asterosísmicas y anticipar el destino del Sol.

📘 **Dónde se aprende** (1 clase): [B24-C16 · Gigantes rojas](../programa/clases/B24/B24-C16-gigantes-rojas/CLASE.md).

### Rama izquierda

- La rama izquierda (`x < x_min`) corresponde a más energía en la dirección larga; la derecha (`x > x_min`), a la otra.

💡 **Cómo se explica en la clase [B82-C04](../programa/clases/B82/B82-C04-lambert-multirrevolucion/CLASE.md):**
- Distinguir la rama izquierda (`x < x_min`) y la derecha (`x > x_min`).
- Ejercicio 7 · autónomo. ¿Qué signo tiene `x` en la rama izquierda y en la derecha?
- 🎯 **Por qué importa:** Si hay tiempo de sobra, la nave puede dar una o más vueltas. La decisión central: ¿cuántas soluciones hay para un tiempo dado, existe alguna, y cuál se elige?

📘 **Dónde se aprende** (1 clase): [B82-C04 · Lambert multirrevolución](../programa/clases/B82/B82-C04-lambert-multirrevolucion/CLASE.md).

### Rama P

- La rama R reúne las transiciones con `ΔJ = +1`; la rama P, con `ΔJ = −1`.

💡 **Cómo se explica en la clase [B62-C02](../programa/clases/B62/B62-C02-espectros-vibracionales-de-moleculas/CLASE.md):**
- *Descripción textual:* de `ωe` y `ωexe` salen los niveles y el origen; de `Be` y `αe`, los `B_v`; juntos generan las ramas P y R, y las diferencias de líneas devuelven `B`.
- Ejercicio 8. ¿Qué rama se «acumula» si `B₁ > B₀`?
- 🎯 **Por qué importa:** Las bandas del CO a 4,67 µm se observan en el infrarrojo, no en milimétricas. Para interpretarlas necesitas saber de dónde sale el origen de banda, por qué las ramas P y R se separan en dos grupos y qué cambia al pasar a un isotopólogo.

📘 **Dónde se aprende** (1 clase): [B62-C02 · Espectros vibracionales de moléculas](../programa/clases/B62/B62-C02-espectros-vibracionales-de-moleculas/CLASE.md).

### Rama R

- La rama R reúne las transiciones con `ΔJ = +1`; la rama P, con `ΔJ = −1`.

💡 **Cómo se explica en la clase [B62-C02](../programa/clases/B62/B62-C02-espectros-vibracionales-de-moleculas/CLASE.md):**
- *Descripción textual:* de `ωe` y `ωexe` salen los niveles y el origen; de `Be` y `αe`, los `B_v`; juntos generan las ramas P y R, y las diferencias de líneas devuelven `B`.
- Ejercicio 8. ¿Qué rama se «acumula» si `B₁ > B₀`?
- 🎯 **Por qué importa:** Las bandas del CO a 4,67 µm se observan en el infrarrojo, no en milimétricas. Para interpretarlas necesitas saber de dónde sale el origen de banda, por qué las ramas P y R se separan en dos grupos y qué cambia al pasar a un isotopólogo.

📘 **Dónde se aprende** (1 clase): [B62-C02 · Espectros vibracionales de moléculas](../programa/clases/B62/B62-C02-espectros-vibracionales-de-moleculas/CLASE.md).

### Ramberg–Osgood

- El límite elástico al 0,2 % `σ₀,₂` es la tensión a la que la deformación plástica residual sería 0,002. Ramberg–Osgood describe toda la curva con `E`, `σ₀,₂` y el exponente de endurecimiento `n`.

💡 **Cómo se explica en la clase [B84-C02](../programa/clases/B84/B84-C02-propiedades-de-aleaciones/CLASE.md):**
- Límite: el modelo de Ramberg–Osgood ajusta una curva monótona y no describe el ciclo, la fatiga ni la temperatura.
- Evaluar la curva de Ramberg–Osgood `ε = σ/E + 0,002 (σ/σ₀,₂)ⁿ`.
- 🎯 **Por qué importa:** Dos aleaciones con la misma rigidez específica pueden diferir en 7 veces su resistencia específica (Ti frente a acero 304); elegir por una sola propiedad lleva a un mal diseño. La decisión central: ¿qué aleación es mejor según el índice que importa a la pieza, y qué significa el límite elástico al 0,2 %?

📘 **Dónde se aprende** (1 clase): [B84-C02 · Propiedades de aleaciones](../programa/clases/B84/B84-C02-propiedades-de-aleaciones/CLASE.md).

### Rampa

- La rampa es la velocidad de cambio de la pantalla.
- Constante de tiempo `τ`: `m c/G`. Rampa: variación lineal de la temperatura de la cámara.

💡 **Cómo se explica en la clase [B85-C19](../programa/clases/B85/B85-C19-ensayos-de-vacio-termico/CLASE.md):**
- Con rampa de `3 K/min` y criterio `|dT/dt| < 1 K/h`, `τ = 10000 s`:
- *Descripción textual:* los extremos predichos y el margen dan los niveles; de ahí sale la temperatura de la pantalla; rampa y estabilización fijan los tiempos y la duración total.
- 🎯 **Por qué importa:** Un ensayo mal planificado dura el doble o no cubre el caso extremo. La decisión central: ¿qué temperaturas de pantalla, rampas y dwells cubren los extremos predichos con margen y cuánto dura el ensayo?

📘 **Dónde se aprende** (2 clases): [B85-C19 · Ensayos de vacío térmico](../programa/clases/B85/B85-C19-ensayos-de-vacio-termico/CLASE.md); [B90-C11 · Ensayos térmicos](../programa/clases/B90/B90-C11-ensayos-termicos/CLASE.md).

### Rampa de fase

- La rampa de fase `e^{2πikτ/N}`.

💡 **Cómo se explica en la clase [B51-C08](../programa/clases/B51/B51-C08-compensacion-de-retardo-y-alineacion-temporal-de-flujos-de-antenas/CLASE.md):**
- *Descripción textual:* la correlación da el entero; dos métodos independientes dan la fracción; una rampa de fase aplica el retardo completo.
- Aplicar la compensación como rampa de fase en frecuencia.
- 🎯 **Por qué importa:** Un retardo mal compensado reduce la coherencia y en VLBI hace perder la detección. La decisión central: ¿cómo se estima y se aplica un retardo con fracción de muestra y qué correlación se espera tras alinear?

📘 **Dónde se aprende** (1 clase): [B51-C08 · Compensación de retardo y alineación temporal de flujos de antenas](../programa/clases/B51/B51-C08-compensacion-de-retardo-y-alineacion-temporal-de-flujos-de-antenas/CLASE.md).

### Rango

- Un rango es el intervalo de valores mostrado.
- Una función `f` asigna a cada valor `x` de un conjunto (el dominio) un único valor `f(x)`; el conjunto de los resultados es el rango.
- El rango de un conjunto de vectores es la dimensión de su espacio generado; la nulidad es el número de relaciones de dependencia independientes.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C15](../programa/clases/B03/B03-C15-representacion-cartesiana-de-datos/CLASE.md):**
- Elige el rango para incluir todos los datos y dejar un margen.
- Un gráfico honesto: ejes rotulados con unidad, rango y escala declarados, datos y fuente citados, y sin ocultar los puntos que no encajan.
- 🎯 **Por qué importa:** Las fichas de la NASA dan semiejes y períodos de los ocho planetas. En una tabla son 16 números.

📘 **Dónde se aprende** (7 clases): [B03-C15 · Representación cartesiana de datos](../programa/clases/B03/B03-C15-representacion-cartesiana-de-datos/CLASE.md); [B04-C04 · Funciones y gráficas](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md); [B10-C02 · Bases y dimensión](../programa/clases/B10/B10-C02-bases-y-dimension/CLASE.md); [B18-C02 · Paso de mensajes con MPI](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md); [B19-C08 · Calibración probabilística](../programa/clases/B19/B19-C08-calibracion-probabilistica/CLASE.md); [B67-C05 · Modelos geoestadísticos de distribución de volátiles](../programa/clases/B67/B67-C05-modelos-geoestadisticos-de-distribucion-de-volatiles/CLASE.md) y 1 más.

### Rango 1

- Un tensor de la forma `a ⊗ b` tiene rango 1 (en el sentido de matrices, C02).

💡 **Cómo se explica en la clase [B10-C18](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md):**
- Con `a = (1, 2, 3)` y `b = (4, 5, 6)`: `a ⊗ b = [[4, 5, 6], [8, 10, 12], [12, 15, 18]]`, cuyas filas son múltiplos de una sola: rango 1.
- Formar `Tᵢⱼ = aᵢ bⱼ` y reconocer que tiene rango 1.
- 🎯 **Por qué importa:** La gravedad no es uniforme a lo largo de un satélite: lo que está más cerca de la Tierra se acelera más que lo que está lejos, y lo que está a los lados se comprime. Con una sola derivada `dg/dr` solo describes la dirección radial; el tensor de marea describe las tres direcciones a la vez.

📘 **Dónde se aprende** (1 clase): [B10-C18 · Producto tensorial y contracción](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md).

### Rango de incertidumbre

- El rango de incertidumbre (`P10–P90`) resume la dispersión de un resultado simulado.

💡 **Cómo se explica en la clase [B126-C06](../programa/clases/B126/B126-C06-presentacion-financiera-ante-inversionistas-con-evidencia/CLASE.md):**
- La incertidumbre se muestra como rango, no como un valor único.
- Dar un rango de incertidumbre del VPN con una simulación y compararlo con el caso central.
- 🎯 **Por qué importa:** [B124-C19](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) redacta propuestas de misión, no financieras. La decisión central: ¿qué cifra se muestra, con qué rótulo y con qué rango, de modo que un tercero pueda comprobarla?

📘 **Dónde se aprende** (1 clase): [B126-C06 · Presentación financiera ante inversionistas con evidencia](../programa/clases/B126/B126-C06-presentacion-financiera-ante-inversionistas-con-evidencia/CLASE.md).

### Rango de la carga

- El rango de la carga es el intervalo de tensión en que el equipo funciona.

💡 **Cómo se explica en la clase [B83-C08](../programa/clases/B83/B83-C08-interfaz-entre-subsistemas/CLASE.md):**
- Comprobar que la tensión en la carga está dentro del rango admitido.
- Reglas del ejemplo: caida <= 2 %, tension de carga en rango, capacidad >= 1.3 x demanda
- 🎯 **Por qué importa:** La mayoría de los fallos de integración aparecen en las interfaces: un conector mal definido, una tensión fuera de rango o una tasa de datos insuficiente. La decisión central: ¿cada interfaz cumple en su caso más desfavorable, con margen, antes de construir?

📘 **Dónde se aprende** (1 clase): [B83-C08 · Interfaz entre subsistemas](../programa/clases/B83/B83-C08-interfaz-entre-subsistemas/CLASE.md).

### Rango de referencia

- El rango de referencia es el intervalo en el que cae la mayoría de los adultos sanos en reposo.

🎯 **Por qué importa (clase B116-C02):** Un panel que marca en rojo todo lo que sale de «60–100 lpm» genera cientos de marcas por ruido en una persona sana, y puede no ver que un atleta con 52 lpm pasó a 64: sigue «dentro del rango». La decisión central: ¿con respecto a qué se compara una medida y cuánto de la desviación es ruido?

📘 **Dónde se aprende** (1 clase): [B116-C02 · Signos vitales: medición, interpretación y límites](../programa/clases/B116/B116-C02-signos-vitales-medicion-interpretacion-y-limites/CLASE.md).

### Rango de validez

- Partícula secundaria: producida en el blindaje. Rango de validez: intervalo donde vale el modelo.

💡 **Cómo se explica en la clase [B106-C14](../programa/clases/B106/B106-C14-proteccion-contra-radiacion/CLASE.md):**
- Un metro de regolito (150 g/cm²) exigiría más de 538 MeV, fuera del rango de validez.
- Reconocer el rango de validez del modelo y los fenómenos que deja fuera.
- 🎯 **Por qué importa:** Las paredes y el regolito detienen partículas, pero con límites: la masa es costosa y las partículas secundarias complican el panorama. La decisión central: ¿cuánta masa por área detiene qué parte de las partículas, y dónde el modelo deja de valer?

📘 **Dónde se aprende** (1 clase): [B106-C14 · Protección contra radiación](../programa/clases/B106/B106-C14-proteccion-contra-radiacion/CLASE.md).

### Rango dinámico

- El rango dinámico es `pozo / ruido de lectura`.
- El rango dinámico es el cociente entre la mayor y la menor incertidumbre.
- El rango dinámico es la diferencia de nivel que el sistema puede representar.

💡 **Cómo se explica en la clase [B44-C05](../programa/clases/B44/B44-C05-pozo-lleno-y-rango-dinamico/CLASE.md):**
- El vaso grande es el pozo y la cucharita es el ruido de lectura: el número de cucharitas que caben mide el rango dinámico.
- FW["pozo lleno"] --> DR["rango dinámico"]
- 🎯 **Por qué importa:** Una cámara debe medir a la vez estrellas débiles y brillantes sin saturar. La decisión central: ¿hasta qué señal media puedo exponer sin saturar el pozo?

📘 **Dónde se aprende** (3 clases): [B44-C05 · Pozo lleno y rango dinámico](../programa/clases/B44/B44-C05-pozo-lleno-y-rango-dinamico/CLASE.md); [B74-C18 · Estimación autónoma a bordo](../programa/clases/B74/B74-C18-estimacion-autonoma-a-bordo/CLASE.md); [B116-C06 · Dispositivos biomédicos portátiles (ultrasonido, diagnóstico)](../programa/clases/B116/B116-C06-dispositivos-biomedicos-portatiles-ultrasonido-diagnostico/CLASE.md).

### Rango dinámico espectral

- El rango dinámico espectral: razón continuo/línea detectable.

💡 **Cómo se explica en la clase [B51-C14](../programa/clases/B51/B51-C14-calibracion-de-banda-en-la-reduccion-de-datos-de-sintesis/CLASE.md):**
- Relacionar la calidad de la banda con el rango dinámico espectral.
- 🎯 **Por qué importa:** Una línea débil sobre un continuo brillante solo se ve si la banda está calibrada mejor que la razón línea/continuo. La decisión central: ¿cuánto ruido inyecta la solución de banda y por qué no basta con restar un polinomio?

📘 **Dónde se aprende** (1 clase): [B51-C14 · Calibración de banda en la reducción de datos de síntesis](../programa/clases/B51/B51-C14-calibracion-de-banda-en-la-reduccion-de-datos-de-sintesis/CLASE.md).

### Rango efectivo

- El rango efectivo es el número de valores singulares por encima de un umbral relativo.

💡 **Cómo se explica en la clase [B10-C11](../programa/clases/B10/B10-C11-valores-singulares-y-svd/CLASE.md):**
- El tercer valor es nueve órdenes de magnitud menor: rango efectivo `2` (umbral relativo `10⁻⁶`) y `κ = 4,55 × 10⁹`.
- Los valores `≥ 0,2` son los tres primeros: rango efectivo `3`.
- 🎯 **Por qué importa:** Un instrumento entrega una imagen de miles de píxeles; la mayor parte de su estructura se puede describir con muy pocos patrones. Una matriz de medidas puede tener columnas casi redundantes, de modo que un cálculo «técnicamente posible» sea inútil.

📘 **Dónde se aprende** (1 clase): [B10-C11 · Valores singulares y SVD](../programa/clases/B10/B10-C11-valores-singulares-y-svd/CLASE.md).

### Rango espectral

- El rango espectral es el intervalo de longitudes de onda que un detector registra.

💡 **Cómo se explica en la clase [B01-C10](../programa/clases/B01/B01-C10-limitaciones-de-los-sentidos-humanos/CLASE.md):**
- L["Luz del objeto"] --> A["Rango espectral: ¿qué colores detecto?"]
- La luz del objeto pasa por el rango espectral del detector, por la apertura que fija cuánta luz entra, por la resolución que decide qué detalle se separa y por la percepción que interpreta; al final hay un registro o una impresión.
- 🎯 **Por qué importa:** Si el ojo bastara, no habría observatorios. La luz visible es una franja pequeña del espectro electromagnético (S1, S2); además, tu pupila recoge poca luz, separa detalles hasta cierto tamaño y puede engañarte.

📘 **Dónde se aprende** (1 clase): [B01-C10 · Limitaciones de los sentidos humanos](../programa/clases/B01/B01-C10-limitaciones-de-los-sentidos-humanos/CLASE.md).

### Rango intercuartílico

- El rango intercuartílico (IQR) es la diferencia entre los percentiles 75 y 25.

🎯 **Por qué importa (clase B12-C06):** Ningún instrumento tiene ruido exactamente normal, y sin embargo casi todas las incertidumbres se expresan con campanas. La razón es que se reportan promedios y sumas de muchas contribuciones pequeñas.

📘 **Dónde se aprende** (1 clase): [B12-C06 · Teorema central del límite](../programa/clases/B12/B12-C06-teorema-central-del-limite/CLASE.md).

### Rango libre

- El rango libre es el que permite la anatomía.

💡 **Cómo se explica en la clase [B107-C02](../programa/clases/B107/B107-C02-movilidad-articular-flexibilidad-y-postura/CLASE.md):**
- Entrenar el rango no cambia el par disponible; reducir la rigidez no cambia el rango libre.
- R["rango libre"] --> U["rango util = min(libre, tau_max/k)"]
- ⚠️ **Error frecuente:** Confundir rango libre con rango útil. El útil es el mínimo entre el rango y `τ_máx/k` (8.2).
- 🎯 **Por qué importa:** Los fragmentos consultados indican que tras el vuelo hay alteraciones del control postural y locomotor por adaptaciones sensoriomotoras (Macaulay et al., 2021) y que existen baterías funcionales con pruebas y medidas fisiológicas (Mulavara et al., 2018).

📘 **Dónde se aprende** (1 clase): [B107-C02 · Movilidad articular, flexibilidad y postura](../programa/clases/B107/B107-C02-movilidad-articular-flexibilidad-y-postura/CLASE.md).

### Rango libre de espurios

- El rango libre de espurios (SFDR) es la distancia entre el suelo de ruido y el nivel en que la intermodulación lo iguala.

💡 **Cómo se explica en la clase [B49-C09](../programa/clases/B49/B49-C09-linealidad-compresion-e-intermodulacion-de-receptores-de-rf/CLASE.md):**
- Con `B = 1 MHz` y `NF = 2 dB`, el rango libre de espurios es `67,98 dB`.
- 🎯 **Por qué importa:** Un receptor que satura con una señal fuerte arruina la observación de una señal débil cercana. La decisión central: ¿qué potencia máxima admite el receptor y qué productos de intermodulación genera?

📘 **Dónde se aprende** (1 clase): [B49-C09 · Linealidad, compresión e intermodulación de receptores de RF](../programa/clases/B49/B49-C09-linealidad-compresion-e-intermodulacion-de-receptores-de-rf/CLASE.md).

### Rango numérico

- Su rango numérico es el número de direcciones del estado que se pueden determinar.

💡 **Cómo se explica en la clase [B74-C28](../programa/clases/B74/B74-C28-medidas-de-rango-y-doppler-para-determinar-la-orbita/CLASE.md):**
- Determinar el rango numérico y el número de condición de la información.
- Límites: estaciones fijas en el espacio inercial, un solo pase y sin perturbaciones; el rango numérico depende del umbral elegido.
- 🎯 **Por qué importa:** Un único pase desde una única estación puede no determinar la órbita completa, aunque la medida sea muy precisa. La decisión central: ¿qué combinación de observables y de estaciones hace observable el estado y con qué precisión en cada dirección?

📘 **Dónde se aprende** (1 clase): [B74-C28 · Medidas de rango y Doppler para determinar la órbita](../programa/clases/B74/B74-C28-medidas-de-rango-y-doppler-para-determinar-la-orbita/CLASE.md).

### Rango oblicuo

- El rango oblicuo es la distancia radar–blanco; el rango sobre el suelo es su proyección.
- Ida y vuelta (RTT): `2d/c`. Rango oblicuo: distancia estación–satélite según la elevación.

💡 **Cómo se explica en la clase [B96-C01](../programa/clases/B96/B96-C01-segmento-espacial-y-segmento-terrestre/CLASE.md):**
- El rango oblicuo a elevación `ε` y altura `h`, con `r = R + h`, es `d = −R sen ε + √(R² sen² ε + r² − R²)`.
- Paso 5 · Comprobación. La ley de cosenos reproduce el rango oblicuo.
- 🎯 **Por qué importa:** Quien opera una nave no puede tratarla como un equipo de laboratorio: cada comando viaja a la velocidad de la luz y cada contacto dura minutos. La decisión central: ¿qué segmento hace qué y cuánto tardan en comunicarse?

📘 **Dónde se aprende** (2 clases): [B57-C07 · Sistemas radar SAR](../programa/clases/B57/B57-C07-sistemas-radar-sar/CLASE.md); [B96-C01 · Segmento espacial y segmento terrestre](../programa/clases/B96/B96-C01-segmento-espacial-y-segmento-terrestre/CLASE.md).

### Rango sobre el suelo

- El rango oblicuo es la distancia radar–blanco; el rango sobre el suelo es su proyección.

🎯 **Por qué importa (clase B57-C07):** La luz visible no atraviesa nubes ni sirve de noche; las microondas sí. Pero un radar no «fotografía»: mide distancia y fase de ecos.

📘 **Dónde se aprende** (1 clase): [B57-C07 · Sistemas radar SAR](../programa/clases/B57/B57-C07-sistemas-radar-sar/CLASE.md).

### Rango útil

- El rango útil es el que permite el par disponible frente a un par resistivo.

💡 **Cómo se explica en la clase [B107-C02](../programa/clases/B107/B107-C02-movilidad-articular-flexibilidad-y-postura/CLASE.md):**
- R["rango libre"] --> U["rango util = min(libre, tau_max/k)"]
- Un traje ilustrativo de rigidez `0,5 N·m/°` en el hombro y `0,3 N·m/°` en el codo, con pares máximos de 25 y 15 N·m, limita el rango útil a 50° en cada articulación y el espacio cae a `0,034 m²` (−94,0 %).
- ⚠️ **Error frecuente:** Confundir rango libre con rango útil. El útil es el mínimo entre el rango y `τ_máx/k` (8.2).
- 🎯 **Por qué importa:** Los fragmentos consultados indican que tras el vuelo hay alteraciones del control postural y locomotor por adaptaciones sensoriomotoras (Macaulay et al., 2021) y que existen baterías funcionales con pruebas y medidas fisiológicas (Mulavara et al., 2018).

📘 **Dónde se aprende** (1 clase): [B107-C02 · Movilidad articular, flexibilidad y postura](../programa/clases/B107/B107-C02-movilidad-articular-flexibilidad-y-postura/CLASE.md).

### RANSAC

- Un RANSAC (*random sample consensus*) ajusta un modelo a muestras mínimas aleatorias y elige el que más puntos explica.
- Ajuste de cuerpo rígido: transformación `(R, t)` que mejor lleva un conjunto al otro. RANSAC: ajusta con muestras mínimas aleatorias y se queda con el modelo de más inliers.
- Huber / IRLS: pesos `w = min(1, δ/|r|)` reajustados iterativamente (la teoría de M-estimadores no se consultó). RANSAC: ajuste con muestras mínimas aleatorias y recuento de inliers (F6).

💡 **Cómo se explica en la clase [B57-C30](../programa/clases/B57/B57-C30-nubes-de-puntos-tridimensionales/CLASE.md):**
- Sobre el suelo filtrado, RANSAC recupera pendientes `0,1000` y `0,0500` (verdaderas: 0,1000 y 0,0500) con error máximo `0,0000` y `99,6%` de inliers.
- Sobre toda la nube, sin filtrar, el error máximo es `0,0002`: aquí el suelo es el 73 % de los puntos y RANSAC lo encuentra igual; con menos suelo (un bosque denso o una ciudad) fallaría.
- 🎯 **Por qué importa:** Un modelo de terreno malo hace que las pendientes y las alturas de los árboles salgan mal. La decisión central: ¿cómo se separa el suelo del resto con la menor contaminación y qué densidad de puntos hace falta?

📘 **Dónde se aprende** (3 clases): [B57-C30 · Nubes de puntos tridimensionales](../programa/clases/B57/B57-C30-nubes-de-puntos-tridimensionales/CLASE.md); [B99-C01 · Odometría visual](../programa/clases/B99/B99-C01-odometria-visual/CLASE.md); [B99-C07 · Robustez del mapeo ante entornos degradados](../programa/clases/B99/B99-C07-robustez-del-mapeo-ante-entornos-degradados/CLASE.md).

### Ranura

- Eje óptico: recta de apuntado. Ranura: abertura de la cúpula.

💡 **Cómo se explica en la clase [B48-C08](../programa/clases/B48/B48-C08-automatizacion-de-cupulas/CLASE.md):**
- Un seguimiento que copie el azimut del telescopio desalinea la ranura; hay que calcular la geometría.
- *Descripción textual:* se corta la recta del eje con la esfera de la cúpula por dos vías y el azimut del punto de corte es el de la ranura.
- 🎯 **Por qué importa:** Una ranura mal orientada viñetea o bloquea el haz. La decisión central: ¿qué azimut debe tener la cúpula para un telescopio descentrado?

📘 **Dónde se aprende** (1 clase): [B48-C08 · Automatización de cúpulas](../programa/clases/B48/B48-C08-automatizacion-de-cupulas/CLASE.md).

### Ranura de guarda

- La ranura de guarda son `M/4` ranuras vacías tras cada símbolo.

💡 **Cómo se explica en la clase [B92-C06](../programa/clases/B92/B92-C06-modulacion-y-codificacion-en-enlaces-opticos/CLASE.md):**
- El laboratorio construye las ranuras explícitamente (mapeo de bits aleatorios a una posición de pulso más las guardas) y cuenta: `37 920` (`M = 4`), `50 560`, `75 920`, `121 600`, `202 880`, `348 160` y `609 920` (`M = 256`), idénticos a la fórmula, con un pulso por símbolo.
- El ejemplo del CCSDS 141.0-B-1 con ranuras de `1 ns`, 16-PPM y 4 guardas da pulsos separados entre `5` y `35 ns`, es decir `28,57` a `200 MHz` de tasa de repetición de pulsos; el laboratorio lo reproduce.
- ⚠️ **Error frecuente:** Olvidar las ranuras de guarda y el CSM. Se corrige con 8.1.
- 🎯 **Por qué importa:** En un canal con pocos fotones, la eficiencia es bits por fotón, no bits por hercio. La decisión central: ¿qué orden PPM y qué tasa de código elegir para equilibrar tasa de información, fotones por bit y potencia de pico?

📘 **Dónde se aprende** (1 clase): [B92-C06 · Modulación y codificación en enlaces ópticos](../programa/clases/B92/B92-C06-modulacion-y-codificacion-en-enlaces-opticos/CLASE.md).

### Ranuras A/B

- Las ranuras A/B guardan la imagen actual y la nueva.

💡 **Cómo se explica en la clase [B88-C13](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md):**
- La imagen se escribe en la ranura que no está activa.
- Si no hay arranque correcto en 3 intentos, vuelve a la ranura anterior: caso 4 con `activo = A`.
- 🎯 **Por qué importa:** Una actualización fallida en órbita no se arregla con un cable. La decisión central: ¿qué comprobaciones aceptan solo la imagen correcta y qué mecanismo vuelve a una versión conocida si la nueva no arranca?

📘 **Dónde se aprende** (1 clase): [B88-C13 · Actualización segura de software](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md).

### Rapidez

- La rapidez es el módulo de la velocidad.
- La velocidad instantánea `v` es el límite de ese cociente cuando `Δt → 0`; su módulo es la rapidez.
- La rapidez `η` cumple `β = tanh η`.

💡 **Cómo se explica en la clase [B04-C12](../programa/clases/B04/B04-C12-vectores-y-componentes/CLASE.md):**
- Con una órbita circular, la rapidez media es `2πa/P = 29,79 km/s`, aproximadamente.
- Pero esa rapidez es solo el *módulo* de un vector: su dirección cambia a lo largo del año.
- ⚠️ **Error frecuente:** Creer que la rapidez media implica velocidad constante. La velocidad cambia de dirección (ejercicio 10).
- 🎯 **Por qué importa:** Una sonda que sale de la Tierra tiene una velocidad respecto de la Tierra y la Tierra tiene una velocidad respecto del Sol. ¿Cuál es la velocidad de la sonda respecto del Sol?

📘 **Dónde se aprende** (3 clases): [B04-C12 · Vectores y componentes](../programa/clases/B04/B04-C12-vectores-y-componentes/CLASE.md); [B05-C02 · Posición, velocidad y aceleración](../programa/clases/B05/B05-C02-posicion-velocidad-y-aceleracion/CLASE.md); [B26-C01 · Postulados de relatividad especial](../programa/clases/B26/B26-C01-postulados-de-relatividad-especial/CLASE.md).

### Rapidez térmica

- La rapidez térmica es `√(k_B T/m)`.

💡 **Cómo se explica en la clase [B35-C01](../programa/clases/B35/B35-C01-funciones-de-distribucion-de-velocidades-en-plasmas/CLASE.md):**
- Para protones de `T = 10⁵ K` la rapidez térmica `v_t = √(k_B T/m_p)` vale `28,730 km/s`; la rapidez media maxwelliana es `1,5958 v_t = 45,85 km/s`.
- 🎯 **Por qué importa:** Los instrumentos miden distribuciones, y casi todas las fórmulas de fluido son momentos de ellas. La decisión central: ¿basta una maxwelliana o hay que conservar la cola?

📘 **Dónde se aprende** (1 clase): [B35-C01 · Funciones de distribución de velocidades en plasmas](../programa/clases/B35/B35-C01-funciones-de-distribucion-de-velocidades-en-plasmas/CLASE.md).

### Rápido

- El modo rápido y el lento son las dos ondas magnetosónicas.

🎯 **Por qué importa (clase B35-C02):** Las ondas fijan los tiempos de respuesta del plasma y los modos de las fronteras. La decisión central: ¿qué modo y a qué velocidad viaja una perturbación según su dirección?

📘 **Dónde se aprende** (1 clase): [B35-C02 · Ondas de Alfvén y ondas magnetosónicas](../programa/clases/B35/B35-C02-ondas-de-alfven-y-ondas-magnetosonicas/CLASE.md).

### Rarefacción

- La rarefacción submuestrea para comparar a igual profundidad.

💡 **Cómo se explica en la clase [B105-C11](../programa/clases/B105/B105-C11-microbioma-en-ambientes-cerrados/CLASE.md):**
- A --> R["profundidad n<br/>y rarefaccion"]
- Descripción: la tabla de rarefacción de 8.3 y la salida del laboratorio con Bray–Curtis por `m` y Shannon por `g`.
- ⚠️ **Error frecuente:** Comparar muestras de distinta profundidad sin rarefacción. Compara a igual `n` (8.3).
- 🎯 **Por qué importa:** Un índice de diversidad depende de la comunidad y de cuántas lecturas se obtuvieron. La decisión central: ¿qué profundidad de muestreo hace fiable un índice y cómo se cuantifica el parecido entre la piel de la tripulación y las superficies?

📘 **Dónde se aprende** (1 clase): [B105-C11 · Microbioma en ambientes cerrados](../programa/clases/B105/B105-C11-microbioma-en-ambientes-cerrados/CLASE.md).

### Rasgo

- Un rasgo es una exigencia que un régimen impone o no.

💡 **Cómo se explica en la clase [B119-C19](../programa/clases/B119/B119-C19-legislacion-comparada-y-casos-nacionales/CLASE.md):**
- Hay `1` rasgo exigido por un solo régimen (la evaluación ambiental, solo en Beta); el único rasgo común a los cinco es el registro nacional, coherente con que el Convenio de Registro obliga a registrar (S1).
- *Descripción textual:* el principio del tratado se concreta en leyes nacionales; estas se tabulan por rasgos y se comparan con Jaccard.
- ⚠️ **Error frecuente:** Atribuir un rasgo a un país real. Se corrige con la sección 11.
- 🎯 **Por qué importa:** Los tratados fijan principios y dejan la aplicación a los Estados (art. VI; art.

📘 **Dónde se aprende** (1 clase): [B119-C19 · Legislación comparada y casos nacionales](../programa/clases/B119/B119-C19-legislacion-comparada-y-casos-nacionales/CLASE.md).

### Rasgo único

- Un rasgo único solo está en un régimen.

💡 **Cómo se explica en la clase [B119-C19](../programa/clases/B119/B119-C19-legislacion-comparada-y-casos-nacionales/CLASE.md):**
- Hay `1` rasgo exigido por un solo régimen (la evaluación ambiental, solo en Beta); el único rasgo común a los cinco es el registro nacional, coherente con que el Convenio de Registro obliga a registrar (S1).
- Identificar el par más parecido, el más distinto y los rasgos únicos.
- 🎯 **Por qué importa:** Los tratados fijan principios y dejan la aplicación a los Estados (art. VI; art.

📘 **Dónde se aprende** (1 clase): [B119-C19 · Legislación comparada y casos nacionales](../programa/clases/B119/B119-C19-legislacion-comparada-y-casos-nacionales/CLASE.md).

### Ráster

- Un ráster es una cuadrícula de valores.

💡 **Cómo se explica en la clase [B14-C26](../programa/clases/B14/B14-C26-formatos-de-datos-raster-geoespaciales-geotiff-y-cog/CLASE.md):**
- Un ráster plano (filas contiguas) lee rápido todo y mal una esquina.
- El ejemplo conductor es un ráster sintético de 1024 × 1024 `float32` con valores `100 + 0,5·col + 0,25·fila + 10·sen(col/50)`, esquina superior izquierda en `(lon 10,0°; lat 40,0°)` y píxel de 0,001°.
- 🎯 **Por qué importa:** Una escena de satélite pesa cientos de megabytes y tú necesitas un recuadro de 100 × 120 píxeles. Si el formato obliga a leer todo el archivo, gastas tiempo y ancho de banda.

📘 **Dónde se aprende** (1 clase): [B14-C26 · Formatos de datos ráster geoespaciales: GeoTIFF y COG](../programa/clases/B14/B14-C26-formatos-de-datos-raster-geoespaciales-geotiff-y-cog/CLASE.md).

### Rayleigh crítico

- El Rayleigh crítico `Ra_c` es el valor por debajo del cual la capa no convecciona.

💡 **Cómo se explica en la clase [B65-C01](../programa/clases/B65/B65-C01-conveccion-del-manto-y-evolucion-termica-de-interiores-planetarios/CLASE.md):**
- Calcular el número de Rayleigh de una capa de fluido calentada desde abajo y compararlo con el crítico.
- Obtener el número de Rayleigh crítico de fronteras libres como el mínimo de una curva y contrastarlo con `27π⁴/4`.
- 🎯 **Por qué importa:** Sin convección, el interior de un planeta rocoso solo perdería calor por conducción y se enfriaría con una escala de tiempo mucho mayor. La decisión central: ¿cuánto calor saca la convección y a qué temperatura se estabiliza un manto que sigue produciendo calor radiactivo?

📘 **Dónde se aprende** (1 clase): [B65-C01 · Convección del manto y evolución térmica de interiores planetarios](../programa/clases/B65/B65-C01-conveccion-del-manto-y-evolucion-termica-de-interiores-planetarios/CLASE.md).

### Rayleigh–Jeans

- La temperatura de brillo `T_B` es la temperatura de un cuerpo negro con ese brillo a esa frecuencia. Rayleigh–Jeans es el límite `hν ≪ kT`.

💡 **Cómo se explica en la clase [B46-C01](../programa/clases/B46/B46-C01-espectro-radioastronomico/CLASE.md):**
- Con 2,7255 K (valor no consultado en esta clase) la temperatura de brillo de Rayleigh–Jeans es `2,6920 K` a 1,4 GHz y `0,9962 K` a 100 GHz, aunque la de Planck vale 2,7255 K en ambas: a 100 GHz la aproximación subestima la temperatura.
- Rayleigh–Jeans es una regla que mide temperatura con una escala lineal; funciona en el centro de la escala y se deforma al borde, cuando el fotón tiene energía comparable a la térmica.
- 🎯 **Por qué importa:** Casi toda la radioastronomía usa Rayleigh–Jeans porque convierte brillo en temperatura de forma lineal, pero deja de valer cuando `hν` se acerca a `kT`. La decisión central: ¿en qué frecuencia y temperatura es válida la aproximación de Rayleigh–Jeans?

📘 **Dónde se aprende** (1 clase): [B46-C01 · Espectro radioastronómico](../programa/clases/B46/B46-C01-espectro-radioastronomico/CLASE.md).

### Rayo

- El rayo: línea de propagación de la energía.

💡 **Cómo se explica en la clase [B41-C01](../programa/clases/B41/B41-C01-naturaleza-y-propagacion-de-la-luz/CLASE.md):**
- Eso solo vale mientras los rayos sean una buena descripción (clase B42 trata lo contrario).
- Con `n₁ = 1,0003` (aire) y `n₂ = 1,517` (vidrio, ilustrativos), un rayo de `A = (0 ; 0,30 m)` a `B = (0,40 m ; −0,20 m)` cruza la interfaz en `x = 295,5867 mm`: sale a `44,5754°` y entra a `27,5675°`, y tarda `2546,8929 ps`, `31,04 ps` menos que en línea recta.
- 🎯 **Por qué importa:** Sin un modelo de rayos no se puede diseñar un telescopio. La decisión central: ¿cuándo basta con rayos y cuánto tarda la luz en cada medio?

📘 **Dónde se aprende** (1 clase): [B41-C01 · Naturaleza y propagación de la luz](../programa/clases/B41/B41-C01-naturaleza-y-propagacion-de-la-luz/CLASE.md).

### Rayo cósmico

- El rayo cósmico es una partícula que deposita carga en el detector.
- Un rayo cósmico es un pico espurio.

💡 **Cómo se explica en la clase [B44-C16](../programa/clases/B44/B44-C16-ruido-cosmico-e-identificacion/CLASE.md):**
- La evidencia es la ficha de los rayos cósmicos del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha de los rayos cósmicos*: detección y coincidencias.
- 🎯 **Por qué importa:** Un impacto fuerte parece una estrella o un defecto. La decisión central: ¿cuántos cuadros hacen falta para identificar los impactos y cuándo falla la mediana?

📘 **Dónde se aprende** (2 clases): [B44-C16 · Ruido cósmico e identificación](../programa/clases/B44/B44-C16-ruido-cosmico-e-identificacion/CLASE.md); [B45-C18 · Extracción de espectros](../programa/clases/B45/B45-C18-extraccion-de-espectros/CLASE.md).

### Rayo de luz

- Un rayo de luz cumple `ct = ±x`.

💡 **Cómo se explica en la clase [B26-C02](../programa/clases/B26/B26-C02-transformaciones-de-lorentz/CLASE.md):**
- Para un rayo `ct = x`, `ct' = γ(1−β)ct` y `x' = γ(1−β)ct`: son iguales.
- Un *boost* inclina los ejes `ct` y `x` simétricamente hacia el rayo de luz, que queda en su sitio.
- 🎯 **Por qué importa:** Para comparar la hora de un reloj en órbita con la de uno en tierra, o la dirección de una señal vista desde dos naves, hace falta una fórmula que traduzca coordenadas entre marcos. Esa fórmula debe respetar los postulados de C01.

📘 **Dónde se aprende** (1 clase): [B26-C02 · Transformaciones de Lorentz](../programa/clases/B26/B26-C02-transformaciones-de-lorentz/CLASE.md).

### Rayo principal

- El rayo principal pasa por el centro del diafragma.

💡 **Cómo se explica en la clase [B50-C04](../programa/clases/B50/B50-C04-telecentricidad-vineteo-y-diseno-del-campo/CLASE.md):**
- D["diafragma en z"] --> P["rayo principal"]
- *Descripción textual:* el ángulo del rayo principal depende de dónde se ponga el diafragma, y la fracción de haz libre es la intersección de dos círculos desplazados por el campo.
- ⚠️ **Error frecuente:** Creer que cualquier diafragma da rayo principal paralelo. Se corrige con 8.1.
- 🎯 **Por qué importa:** En un detector la luz que llega muy inclinada se pierde o se mezcla; en un espectrógrafo o un mosaico el viñeteo cambia el brillo según el campo. La decisión central: ¿dónde va el diafragma y cuánto campo se acepta con viñeteo?

📘 **Dónde se aprende** (1 clase): [B50-C04 · Telecentricidad, viñeteo y diseño del campo](../programa/clases/B50/B50-C04-telecentricidad-vineteo-y-diseno-del-campo/CLASE.md).

### Razón

- Una razón entre dos magnitudes `A` y `B` de la misma clase es el cociente `A/B`.
- La razón voraz/óptimo mide la calidad.
- La razón entre umbrales.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C02](../programa/clases/B03/B03-C02-fracciones-y-razones-de-magnitudes/CLASE.md):**
- Esa independencia de la unidad es la gran ventaja de la razón.
- Si dos razones son iguales, `a/b = c/d`, puedes hallar uno si conoces tres.
- ⚠️ **Error frecuente:** No decir quién está arriba. «La razón es 109» sin decir de qué a qué.
- 🎯 **Por qué importa:** Una cifra aislada como «69 911 km» no dice si Júpiter es grande o pequeño. Una razón sí: Júpiter tiene un radio unas 11 veces el terrestre.

📘 **Dónde se aprende** (4 clases): [B03-C02 · Fracciones y razones de magnitudes](../programa/clases/B03/B03-C02-fracciones-y-razones-de-magnitudes/CLASE.md); [B29-C18 · Redes de seguimiento temporal](../programa/clases/B29/B29-C18-redes-de-seguimiento-temporal/CLASE.md); [B33-C04 · Escalas de severidad de clima espacial](../programa/clases/B33/B33-C04-escalas-de-severidad-de-clima-espacial/CLASE.md); [B84-C34 · Tratamientos y recubrimientos superficiales de componentes espaciales](../programa/clases/B84/B84-C34-tratamientos-y-recubrimientos-superficiales-de-componentes-espaciales/CLASE.md).

### Razón axial

- La razón axial `AR` (o elipticidad) mide cuánto se aparta una polarización de la circular (`0 dB`) hacia la lineal (`∞`).

💡 **Cómo se explica en la clase [B91-C02](../programa/clases/B91/B91-C02-polarizacion-de-antenas-y-perdidas-por-desadaptacion/CLASE.md):**
- RCP frente a LCP con razón axial `1,0 dB` en ambas da `PLF = 0,0131` (`−18,8 dB` de aislamiento); con `3,0 dB`, `0,110` (`−9,6 dB`).
- *Descripción textual:* la razón axial, la inclinación y el sentido definen el vector de Jones; el producto interno entre el de la onda y el de la antena da el factor de pérdida, que se expresa en dB y se resta del margen.
- ⚠️ **Error frecuente:** Confundir elipticidad con razón axial en razón lineal. La razón axial en dB es `20 log(a/b)`; ver la sección 6.
- 🎯 **Por qué importa:** Un enlace pierde potencia si las polarizaciones no coinciden, y puede perderla toda si son ortogonales. La decisión central: ¿qué polarización y qué razón axial exigir a las dos antenas para que la desadaptación quede por debajo del margen del enlace?

📘 **Dónde se aprende** (1 clase): [B91-C02 · Polarización de antenas y pérdidas por desadaptación](../programa/clases/B91/B91-C02-polarizacion-de-antenas-y-perdidas-por-desadaptacion/CLASE.md).

### Razón bariones–fotones

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B40-C07):** Los picos acústicos fijan la geometría y el contenido del universo. La decisión central: ¿dónde caen los picos (`ℓ_A = π/θ*`) y cómo se pasa del espectro a la correlación y de vuelta?

📘 **Dónde se aprende** (1 clase): [B40-C07 · Espectro angular de potencias del CMB](../programa/clases/B40/B40-C07-espectro-angular-de-potencias-del-cmb/CLASE.md).

### Razón barión–fotón

- La razón barión–fotón `η = n_b/n_γ`.

💡 **Cómo se explica en la clase [B26-C15](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md):**
- *Descripción textual:* la temperatura determina el número de fotones, el máximo espectral y la energía media; con la densidad de bariones del modelo se obtiene la razón barión–fotón.
- 🎯 **Por qué importa:** El fondo de microondas es la reliquia más antigua observable y da los parámetros del modelo cosmológico. Entender su espectro de cuerpo negro permite calibrar un instrumento, estimar el contenido de fotones y comprender por qué un solo número, la razón barión–fotón, resume tanta física.

📘 **Dónde se aprende** (2 clases): [B26-C15 · Radiación cósmica de fondo](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md); [B26-C16 · Nucleosíntesis primordial](../programa/clases/B26/B26-C16-nucleosintesis-primordial/CLASE.md).

### Razón crítica

- La razón crítica `R` es el máximo cociente tolerado entre `p_N₂` en el tejido y la presión ambiente (valores ilustrativos aquí).

💡 **Cómo se explica en la clase [B104-C11](../programa/clases/B104/B104-C11-trajes-espaciales/CLASE.md):**
- Las razones críticas y los tiempos medios son inventados: no usar para ninguna decisión sobre descompresión ni respiración.
- *Descripción textual:* el tejido parte equilibrado con el aire de la cabina; al respirar oxígeno el nitrógeno cae exponencialmente; la razón con la presión del traje determina cuánto tiempo hace falta para bajarla hasta la razón crítica.
- 🎯 **Por qué importa:** Un traje presurizado a una fracción de la presión de la cabina deja al nitrógeno disuelto en sobresaturación si no se elimina antes. La decisión conceptual: ¿cómo depende el tiempo de eliminación del nitrógeno del compartimento, de la razón crítica y de la presión de la cabina?

📘 **Dónde se aprende** (1 clase): [B104-C11 · Trajes espaciales](../programa/clases/B104/B104-C11-trajes-espaciales/CLASE.md).

### Razón de amortiguamiento

- La razón de amortiguamiento `ζ` mide la pérdida de energía por ciclo.
- La razón de amortiguamiento es `ζ = μ_c Kd/(2ω_n)`.

💡 **Cómo se explica en la clase [B10-C09](../programa/clases/B10/B10-C09-diagonalizacion-y-estabilidad/CLASE.md):**
- Un modo de flexión de un panel (modelo sintético, no de un panel real) tiene frecuencia `0,5 Hz` (`ω = π rad/s`) y razón de amortiguamiento `ζ = 0,02`.
- 🎯 **Por qué importa:** Un panel solar largo y delgado vibra después de una maniobra. Si la vibración se amortigua, el panel es estable; si crece, hay un problema serio.

📘 **Dónde se aprende** (2 clases): [B10-C09 · Diagonalización y estabilidad](../programa/clases/B10/B10-C09-diagonalizacion-y-estabilidad/CLASE.md); [B77-C24 · Guiado y control de actitud de lanzadores (TVC)](../programa/clases/B77/B77-C24-guiado-y-control-de-actitud-de-lanzadores-tvc/CLASE.md).

### Razón de bandas

- La razón de bandas es el cociente de dos de ellas.

💡 **Cómo se explica en la clase [B57-C05](../programa/clases/B57/B57-C05-imagenes-multiespectrales/CLASE.md):**
- Como Brovey multiplica todas las bandas por el mismo factor en cada píxel, la razón `NIR/rojo` no cambia: la diferencia máxima es `1,78e-15`.
- Paso 3 · Con la textura. Como la textura multiplica ambas bandas, la razón media es 9,01.
- 🎯 **Por qué importa:** Con una sola banda el agua oscura, la sombra y el asfalto se confunden; con varias, cada cubierta deja una firma distinta. La decisión central: ¿qué combinación de bandas separa las cubiertas que me interesan y cómo recupero detalle espacial sin falsear los colores?

📘 **Dónde se aprende** (1 clase): [B57-C05 · Imágenes multiespectrales](../programa/clases/B57/B57-C05-imagenes-multiespectrales/CLASE.md).

### Razón de Birge

- La razón de Birge `RB = √(χ²/(N − 1))` es cercana a 1 si las incertidumbres son consistentes con la dispersión.

💡 **Cómo se explica en la clase [B13-C18](../programa/clases/B13/B13-C18-intercomparacion-de-instrumentos/CLASE.md):**
- *Descripción textual:* de las medidas con incertidumbre salen los `z` por pares y la media ponderada; con ella se calculan `χ²` y la razón de Birge; si es cercana a 1 se combinan; si no, se investiga un sesgo o una incertidumbre subestimada.
- media ponderada = 1361.876 +/- 0.346 W/m2 ; chi2 = 9.752 ; razon de Birge = 2.208
- 🎯 **Por qué importa:** Tres radiómetros miden la misma irradiancia solar y dan `1361,4`, `1360,1` y `1362,9 W/m²`. Cada uno declara una incertidumbre.

📘 **Dónde se aprende** (1 clase): [B13-C18 · Intercomparación de instrumentos](../programa/clases/B13/B13-C18-intercomparacion-de-instrumentos/CLASE.md).

### Razón de carga útil

- La razón de carga útil de una etapa es `π = (e^(−ΔV/c) − ε)/(1 − ε)`, con `c = Isp·g₀`.

💡 **Cómo se explica en la clase [B77-C01](../programa/clases/B77/B77-C01-sistemas-de-lanzamiento/CLASE.md):**
- *Descripción textual:* el requisito de velocidad se reparte entre las etapas; de cada reparto salen la razón de carga útil, la masa de despegue y el empuje; el óptimo es el mínimo de la masa.
- Calcular la razón de carga útil de una etapa con el coeficiente estructural.
- 🎯 **Por qué importa:** Un requisito de velocidad no dice cuánto pesa el vehículo. La decisión central: ¿cómo se reparte la velocidad entre dos etapas para que la masa de despegue sea mínima, y qué parte de esa masa es carga útil?

📘 **Dónde se aprende** (1 clase): [B77-C01 · Sistemas de lanzamiento](../programa/clases/B77/B77-C01-sistemas-de-lanzamiento/CLASE.md).

### Razón de compresión

- La razón de compresión es el tamaño sin comprimir dividido por el comprimido.
- La razón de compresión `r = ρ₂/ρ₁`.

💡 **Cómo se explica en la clase [B14-C07](../programa/clases/B14/B14-C07-hdf5-y-almacenamiento-cientifico/CLASE.md):**
- La razón de compresión sí cambia mucho según el contenido: el flujo con ruido ocupó `1 373 210` bytes frente a `1 600 000` sin comprimir (razón 1,17); el modelo sin ruido ocupó `8 970` bytes (razón 178,4).
- Las razones de compresión valen solo para estos datos.
- 🎯 **Por qué importa:** Una simulación o un instrumento moderno produce series de millones de muestras con sus metadatos. Guardarlas en texto es lento y pesado; cargarlas enteras en memoria para leer un fragmento es inviable.

📘 **Dónde se aprende** (3 clases): [B14-C07 · HDF5 y almacenamiento científico](../programa/clases/B14/B14-C07-hdf5-y-almacenamiento-cientifico/CLASE.md); [B30-C14 · Choques y aceleración de partículas](../programa/clases/B30/B30-C14-choques-y-aceleracion-de-particulas/CLASE.md); [B47-C16 · Compresión de datos científicos](../programa/clases/B47/B47-C16-compresion-de-datos-cientificos/CLASE.md).

### Razón de consistencia

- La razón de consistencia (CR) mide la coherencia de esas comparaciones.
- La razón de consistencia `CR = CI/RI`, con `CI = (λ_max − n)/(n − 1)`, debe ser menor que 0,10 por convención.

💡 **Cómo se explica en la clase [B57-C19](../programa/clases/B57/B57-C19-sig-y-analisis-de-riesgo/CLASE.md):**
- Calcular pesos AHP y la razón de consistencia.
- El script [riesgo.py](riesgo.py) combina tres capas sintéticas, calcula pesos AHP con razón de consistencia y mide la sensibilidad de las celdas prioritarias (comprueba que los pesos coinciden con la media geométrica a 1e-9 con CR = 0 y que una matriz incoherente tiene CR > 0,10).
- 🎯 **Por qué importa:** Los mapas de riesgo orientan decisiones y presupuestos, pero dependen de supuestos de ponderación que suelen quedar ocultos. La decisión central: ¿cómo combino capas y cuánto cambian las zonas prioritarias si cambio los pesos?

📘 **Dónde se aprende** (2 clases): [B57-C19 · SIG y análisis de riesgo](../programa/clases/B57/B57-C19-sig-y-analisis-de-riesgo/CLASE.md); [B83-C07 · Arquitecturas de sistemas](../programa/clases/B83/B83-C07-arquitecturas-de-sistemas/CLASE.md).

### Razón de contraste

- La razón de contraste de WCAG es `(L1 + 0,05)/(L2 + 0,05)`, con `L1` la luminancia relativa del color más claro y `L2` la del más oscuro.
- La razón de contraste es `(L₁ + 0,05)/(L₂ + 0,05)` con `L₁ ≥ L₂`.
- La razón de contraste `(L₁ + 0,05)/(L₂ + 0,05)` va de 1 a 21.

💡 **Cómo se explica en la clase [B128-C06](../programa/clases/B128/B128-C06-contraste-y-color-accesibles/CLASE.md):**
- Calcular la razón de contraste entre dos colores.
- El script [contraste.py](contraste.py) implementa luminancia y razón WCAG, comprueba valores conocidos y evalúa pares y una leyenda (comprueba 21:1, 1:1, 4,54, 4,48 y simetría).
- 🎯 **Por qué importa:** Un texto gris claro sobre blanco, un azul puro sobre negro o una leyenda donde solo cambia el tono se pierden para quien tiene baja visión, daltonismo o una pantalla poco luminosa. La decisión central: ¿cómo compruebo con números que un par de colores se lee, y cuándo el color no basta?

📘 **Dónde se aprende** (3 clases): [B116-C07 · Diseño de paneles de monitoreo de salud](../programa/clases/B116/B116-C07-diseno-de-paneles-de-monitoreo-de-salud/CLASE.md); [B128-C06 · Contraste y color accesibles](../programa/clases/B128/B128-C06-contraste-y-color-accesibles/CLASE.md); [B130-C02 · Visualización de datos para comunicar](../programa/clases/B130/B130-C02-visualizacion-de-datos-para-comunicar/CLASE.md).

### Razón de distancias

- Descriptor: vector que resume el parche alrededor del punto. Razón de distancias: distancia al vecino más cercano entre la del segundo más cercano (F3).

💡 **Cómo se explica en la clase [B99-C02](../programa/clases/B99/B99-C02-deteccion-y-descriptores-de-caracteristicas/CLASE.md):**
- Paso 2 · Distancias. Un descriptor tiene `d₁ = 0,30` y `d₂ = 0,50`: razón 0,60, se acepta con `τ = 0,8`.
- Emparejar por vecino más cercano y aplicar la prueba de razón de distancias.
- 🎯 **Por qué importa:** Una esquina de una roca puede verse distinta cuando cambian el brillo, el ruido o el punto de vista, y dos rocas parecidas se confunden. La decisión central: ¿qué puntos conviene usar, cómo se describen y cuándo se acepta un emparejamiento?

📘 **Dónde se aprende** (1 clase): [B99-C02 · Detección y descriptores de características](../programa/clases/B99/B99-C02-deteccion-y-descriptores-de-caracteristicas/CLASE.md).

### Razón de duración

- La razón de duración que usaremos es `T_obs / T₀`, donde `T_obs` es la duración medida del tránsito y `T₀` la duración esperada.

💡 **Cómo se explica en la clase [B17-C01](../programa/clases/B17/B17-C01-ingenieria-de-caracteristicas-cientificas/CLASE.md):**
- Segundo, la razón de duración `T_obs / T₀` es adimensional: vale cerca de 1 para un planeta en una estrella como la supuesta y se aleja de 1 si la señal viene de otro fenómeno o de otra estrella (un falso positivo).
- En el laboratorio, un clasificador de vecinos más cercanos sobre columnas crudas con una unidad mezclada llega a 0,51–0,59; estandarizado, 0,76; con la razón de duración y `log₁₀ P`, 0,85.
- 🎯 **Por qué importa:** Un modelo de aprendizaje automático no sabe física: solo ve números. Si le das la duración de un tránsito en segundos y el periodo en días, la columna con números más grandes domina cualquier cálculo de distancias, y la clasificación depende de una elección de unidades que nada tiene que ver con el cielo.

📘 **Dónde se aprende** (1 clase): [B17-C01 · Ingeniería de características científicas](../programa/clases/B17/B17-C01-ingenieria-de-caracteristicas-cientificas/CLASE.md).

### Razón de efectividad de la fuerza

- La razón de efectividad de la fuerza (FER) es la fracción del esfuerzo que va a la tarea prevista.

🎯 **Por qué importa (clase B108-C03):** No hay clase sobre herramientas EVA (torque, reacción, sujeción de herramientas). La decisión central: ¿qué par se logra con una fuerza dada, y cuánto gira o se desplaza quien lo aplica si nada lo sujeta?

📘 **Dónde se aprende** (1 clase): [B108-C03 · Herramientas y equipos de EVA](../programa/clases/B108/B108-C03-herramientas-y-equipos-de-eva/CLASE.md).

### Razón de efectividad de transferencia

- La razón de efectividad de transferencia `TER = (Y₀ − Y(x))/x` mide las horas reales ahorradas por hora simulada.

🎯 **Por qué importa (clase B104-C09):** El simulador es más barato que el vuelo, pero más horas no siempre ahorran más: hay saturación. La decisión central: ¿cuántas horas de simulador conviene programar y cómo se sabe que transfieren al sistema real?

📘 **Dónde se aprende** (1 clase): [B104-C09 · Entrenamiento en simuladores](../programa/clases/B104/B104-C09-entrenamiento-en-simuladores/CLASE.md).

### Razón de enriquecimiento

- La razón de enriquecimiento es la ley del producto sobre la de la alimentación.

💡 **Cómo se explica en la clase [B59-C22](../programa/clases/B59/B59-C22-beneficio-y-separacion-granulometrica-de-regolito/CLASE.md):**
- Ejercicio 2 · con una pista. Razón de enriquecimiento (8.3).
- Recuperacion del mineral objetivo en el fino = 75.88 % ; razon de enriquecimiento = 1.442
- 🎯 **Por qué importa:** Calentar o reducir todo el regolito es caro; separar la fracción rica antes ahorra energía. La decisión central: ¿qué tamaño de corte equilibra la ley del concentrado y la recuperación del mineral?

📘 **Dónde se aprende** (1 clase): [B59-C22 · Beneficio y separación granulométrica de regolito](../programa/clases/B59/B59-C22-beneficio-y-separacion-granulometrica-de-regolito/CLASE.md).

### Razón de frecuencias

- La razón de frecuencias entre un suelo (`R`) y una órbita (`r`) es `√((1 − r_s/R)/(1 − r_s/r))`.
- La razón de frecuencias `r = f/f_n`.

💡 **Cómo se explica en la clase [B26-C10](../programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/CLASE.md):**
- La razón de frecuencias entre el suelo y una órbita de radio `r = 2,6 × 10⁷ m` (ilustrativo) es `0,999 999 999 475`, o sea `1 − f = 5,25 × 10⁻¹⁰`, que coincide con `GM_E(1/R_E − 1/r)/c²` a `10⁻¹⁴`.
- Calcular la razón de frecuencias entre el suelo y una órbita.
- 🎯 **Por qué importa:** El corrimiento gravitacional ajusta los relojes de los satélites de navegación, contamina la medida de velocidades en enanas blancas y revela la compacidad de las estrellas de neutrones. La decisión central: dada la compacidad de un cuerpo, ¿cuánto vale el corrimiento de su luz y cuándo falla la aproximación de campo débil?

📘 **Dónde se aprende** (2 clases): [B26-C10 · Desplazamiento gravitacional al rojo](../programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/CLASE.md); [B47-C11 · Aislamiento vibracional](../programa/clases/B47/B47-C11-aislamiento-vibracional/CLASE.md).

### Razón de masa

- La razón de masa es `m₀/m_f`.

💡 **Cómo se explica en la clase [B75-C09](../programa/clases/B75/B75-C09-presupuestos-de-delta-v/CLASE.md):**
- El producto de las razones de masa de las cuatro fases coincide con la razón del total (error relativo menor que `10⁻¹²`) y una integración numérica de la ecuación del cohete en 200 000 pasos da `5,239168 km/s`, igual al total.
- Por fases (producto de razones de masa): cada fase aporta una razón.
- ⚠️ **Error frecuente:** Sumar masas en lugar de razones de masa. Se corrige con 8.4.
- 🎯 **Por qué importa:** Un presupuesto de delta-v decide el tamaño del cohete. La decisión central: ¿cuánto delta-v hay que reservar en cada fase y cuánta masa de propulsante implica?

📘 **Dónde se aprende** (2 clases): [B75-C09 · Presupuestos de delta-v](../programa/clases/B75/B75-C09-presupuestos-de-delta-v/CLASE.md); [B75-C20 · Diseño de una misión a luna helada](../programa/clases/B75/B75-C20-diseno-de-una-mision-a-luna-helada/CLASE.md).

### Razón de masas

- La razón de masas es `q = M_donante/M_acretor`.
- La razón de masas es `m₀/m_f`.
- La razón de masas `q = Mp/M`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B24-C22](../programa/clases/B24/B24-C22-evolucion-binaria-lobulo-de-roche-y-transferencia-de-masa/CLASE.md):**
- Ejercicio 6. ¿Para qué razón de masas es mínimo el semieje?
- 🎯 **Por qué importa:** Una estrella que se expande (C16) o se hincha en una binaria puede llenar la región donde su gravedad domina y verter gas sobre su compañera. Esa transferencia cambia las masas, la órbita y el destino de ambas, y es el camino hacia muchos objetos exóticos.

📘 **Dónde se aprende** (5 clases): [B24-C22 · Evolución binaria: lóbulo de Roche y transferencia de masa](../programa/clases/B24/B24-C22-evolucion-binaria-lobulo-de-roche-y-transferencia-de-masa/CLASE.md); [B29-C05 · Microlentes gravitacionales](../programa/clases/B29/B29-C05-microlentes-gravitacionales/CLASE.md); [B77-C05 · Ecuación de cohete ideal](../programa/clases/B77/B77-C05-ecuacion-de-cohete-ideal/CLASE.md); [B119-C25 · Derecho y marcos de recursos espaciales](../programa/clases/B119/B119-C25-derecho-y-marcos-de-recursos-espaciales/CLASE.md); [B124-C23 · Costos de transporte por kilogramo a superficie](../programa/clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md).

### Razón de par

- La razón de par (*torque ratio*) es `T_s/(T_f + cω)`.

💡 **Cómo se explica en la clase [B84-C13](../programa/clases/B84/B84-C13-mecanismos-desplegables/CLASE.md):**
- La razón `T_s/(T_f + cω)` baja a lo largo del recorrido y es mínima al final: `1,560` a 90°.
- Subir la precarga a `0,4289 N·m` da razón 2,0 con `3,746 rad/s` y energía de impacto `0,3509 J` (más impacto): se compensan margen y carga de choque.
- ⚠️ **Error frecuente:** Presentar la razón 2,0 como requisito de un estándar. Se corrige con el alcance.
- 🎯 **Por qué importa:** Un mecanismo que se despliega bien en el banco puede quedarse trabado en órbita si la fricción sube o la precarga baja; el margen de par lo cuantifica. La decisión central: ¿qué razón de par tiene el despliegue y qué precarga hace falta para cumplir el requisito?

📘 **Dónde se aprende** (1 clase): [B84-C13 · Mecanismos desplegables](../programa/clases/B84/B84-C13-mecanismos-desplegables/CLASE.md).

### Razón de periodos

- La razón de periodos `P₂/P₁` indica cercanía a una resonancia.

💡 **Cómo se explica en la clase [B52-C10](../programa/clases/B52/B52-C10-arquitecturas-de-sistemas-exoplanetarios/CLASE.md):**
- Construido con `Δ = 12` desde `0,05 ua`, `m = 5 M⊕`, `M* = 0,9 M☉` por bisección: semiejes `0.0500 0.0655 0.0857 0.1122 0.1469` ua, periodos `4.30 6.45 9.66 14.47 21.68` días y razón constante `1.4981` (el espaciado constante en `R_H` implica razón de periodos casi constante).
- Un sistema sintético con `Δ = 12` y cinco planetas de `5 M⊕` alrededor de `0,9 M☉` da razones de periodos de `1.4981`.
- 🎯 **Por qué importa:** El espaciado mide cuán «apretado» está un sistema y cuán cerca está de la inestabilidad. La decisión central: ¿cómo se expresa el espaciado entre planetas independientemente de su escala?

📘 **Dónde se aprende** (1 clase): [B52-C10 · Arquitecturas de sistemas exoplanetarios](../programa/clases/B52/B52-C10-arquitecturas-de-sistemas-exoplanetarios/CLASE.md).

### Razón de presiones

- La razón de presiones `p_c/pₑ` mide cuánto se expande.

💡 **Cómo se explica en la clase [B78-C03](../programa/clases/B78/B78-C03-termodinamica-de-camaras/CLASE.md):**
- *Descripción textual:* la temperatura, la masa molar, `γ` y la razón de presiones dan el escape; el balance de energía lo verifica;
- Ejercicio 12 · integrador. Elabora tu *tabla de escape según cámara y gas*: `Tₑ`, `Vₑ` e `Isp` equivalente para cinco razones de presiones, efecto de `M` y `T_c`, y la cota.
- 🎯 **Por qué importa:** El mismo calor produce chorros distintos según el gas. La decisión central: ¿qué parámetro de cámara gana más escape, subir la temperatura o bajar la masa molar, y hasta dónde se puede expandir el gas?

📘 **Dónde se aprende** (1 clase): [B78-C03 · Termodinámica de cámaras](../programa/clases/B78/B78-C03-termodinamica-de-camaras/CLASE.md).

### Razón de reparto

- La razón de reparto es la parte del desvío que asume cada lado.

🎯 **Por qué importa (clase B124-C10):** El tipo de contrato reparte el riesgo de sobrecosto entre quien compra y quien vende. La decisión central: ¿cuánto riesgo asume cada parte con cada tipo de contrato y cuánto cuesta ese reparto en promedio?

📘 **Dónde se aprende** (1 clase): [B124-C10 · Contratos y compras espaciales](../programa/clases/B124/B124-C10-contratos-y-compras-espaciales/CLASE.md).

### Razón de riesgos

- La razón de riesgos `RR` compara dos cohortes.

💡 **Cómo se explica en la clase [B129-C06](../programa/clases/B129/B129-C06-motivacion-y-permanencia-de-participantes/CLASE.md):**
- Con una segunda cohorte B cuyo riesgo se supuso `0,80` veces el de A, la razón de riesgos estimada es `0,768` con IC aproximado 95 % `[0,670; 0,879]`; con una cohorte C sin efecto se obtiene `1,045` `[0,915; 1,194]`.
- C2["Segunda cohorte"] --> R["Razon de riesgos e IC"]
- 🎯 **Por qué importa:** Los equipos de un proyecto quieren retener voluntarios y a menudo añaden insignias, rachas o clasificaciones sin medir si sirven. La decisión central: ¿cómo medir la permanencia y cuándo se puede decir que algo la mejoró?

📘 **Dónde se aprende** (1 clase): [B129-C06 · Motivación y permanencia de participantes](../programa/clases/B129/B129-C06-motivacion-y-permanencia-de-participantes/CLASE.md).

### Razón de sabores

- La razón de sabores `ν_e:ν_μ:ν_τ`.

💡 **Cómo se explica en la clase [B28-C03](../programa/clases/B28/B28-C03-neutrinos-astrofisicos/CLASE.md):**
- Calcular la razón de sabores en la Tierra.
- Ejercicio 12 · integrador. Elabora tu *ficha de sabores de neutrinos*: `K`, el primer máximo a dos energías, la matriz `P`, la razón para tres fuentes y la fase astrofísica.
- 🎯 **Por qué importa:** Un detector que ve neutrinos muónicos de una fuente lejana no ve lo que salió de ella. Para interpretar la razón de sabores hay que conocer la mezcla.

📘 **Dónde se aprende** (1 clase): [B28-C03 · Neutrinos astrofísicos](../programa/clases/B28/B28-C03-neutrinos-astrofisicos/CLASE.md).

### Razón de Strehl

- La razón de Strehl es la intensidad central del sistema aberrado entre la ideal.

🎯 **Por qué importa (clase B41-C19):** Un buen espejo mal colimado rinde mal. La decisión central: ¿cuánta descolimación y cuánto desenfoque se toleran?

📘 **Dónde se aprende** (2 clases): [B41-C19 · Colimación y prueba de enfoque](../programa/clases/B41/B41-C19-colimacion-y-prueba-de-enfoque/CLASE.md); [B50-C14 · Criterios de aceptación: Strehl, error de frente de onda y especificaciones](../programa/clases/B50/B50-C14-criterios-de-aceptacion-strehl-error-de-frente-de-onda-y-especificaciones/CLASE.md).

### Razón de Urey

- La razón de Urey es el cociente entre la producción radiactiva y el calor total que sale.

💡 **Cómo se explica en la clase [B65-C04](../programa/clases/B65/B65-C04-flujo-termico-planetario-y-balance-termico-del-interior/CLASE.md):**
- Con una producción radiactiva ilustrativa de 20 TW, la razón de Urey es `20/47 = 0,426` y el enfriamiento secular saca `27 TW`, lo que equivale a `dT/dt = −122 K/Ga` con `C = 7×10²⁷ J/K`.
- Calcular una razón de Urey y una tasa de enfriamiento secular.
- 🎯 **Por qué importa:** Un planeta se enfría en parte porque pierde calor guardado y en parte vive del que producen sus isótopos radiactivos. La decisión central: ¿qué fracción del calor que sale es producción actual y qué fracción es enfriamiento?

📘 **Dónde se aprende** (1 clase): [B65-C04 · Flujo térmico planetario y balance térmico del interior](../programa/clases/B65/B65-C04-flujo-termico-planetario-y-balance-termico-del-interior/CLASE.md).

### Razón de verosimilitud

- La razón de verosimilitud es `s/f`.
- La razón de verosimilitud de una fase es `S/F`.
- La razón de verosimilitud mide cuánto favorece una evidencia a una hipótesis.

💡 **Cómo se explica en la clase [B56-C15](../programa/clases/B56/B56-C15-falsos-positivos-de-biofirmas/CLASE.md):**
- Ejercicio 2 · con una pista. Calcula la razón de verosimilitud con `s = 0,9` y `f = 0,05`.
- 🎯 **Por qué importa:** Una detección no es una prueba. Si la señal puede producirse por procesos sin vida, su significado depende de cuán frecuentes son.

📘 **Dónde se aprende** (3 clases): [B56-C15 · Falsos positivos de biofirmas](../programa/clases/B56/B56-C15-falsos-positivos-de-biofirmas/CLASE.md); [B67-C02 · Diseño de un programa de prospección por fases](../programa/clases/B67/B67-C02-diseno-de-un-programa-de-prospeccion-por-fases/CLASE.md); [B119-C30 · Atribución de incidentes y desinformación en el dominio espacial](../programa/clases/B119/B119-C30-atribucion-de-incidentes-y-desinformacion-en-el-dominio-espacial/CLASE.md).

### Razón de verosimilitud positiva

- La razón de verosimilitud positiva es `S/(1 − E)`.

💡 **Cómo se explica en la clase [B116-C06](../programa/clases/B116/B116-C06-dispositivos-biomedicos-portatiles-ultrasonido-diagnostico/CLASE.md):**
- La razón de verosimilitud positiva es 6,00 en todos los casos: la prueba es la misma, pero lo que significa un positivo depende de lo probable que era la condición.
- 🎯 **Por qué importa:** Un equipo no es solo su ficha técnica: lo que ve depende de la frecuencia elegida, quién lo maneja, cuánto entrena y qué retardo tiene el apoyo experto. Y una prueba con buenos números de sensibilidad y especificidad puede dar mayoría de falsos positivos si la condición es rara.

📘 **Dónde se aprende** (1 clase): [B116-C06 · Dispositivos biomédicos portátiles (ultrasonido, diagnóstico)](../programa/clases/B116/B116-C06-dispositivos-biomedicos-portatiles-ultrasonido-diagnostico/CLASE.md).

### Razón focal

- La apertura `D` es el diámetro del objetivo o espejo; la distancia focal `F`, la longitud del camino óptico; la razón focal `N = F/D`.
- La razón focal `N = F/D`.
- La razón focal `f/D`.

💡 **Cómo se explica en la clase [B08-C14](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md):**
- Calcular razón focal, aumento, pupila de salida y campo de un sistema telescopio–ocular.
- Ejercicio 1. Calcula razón focal, aumento y pupila de salida de un reflector de 114 mm y 900 mm de F con un ocular de 25 mm.
- 🎯 **Por qué importa:** Un telescopio de juguete anuncia «600×» y decepciona. La pregunta motivadora: ¿qué telescopio me conviene y qué podré ver con él?

📘 **Dónde se aprende** (3 clases): [B08-C14 · Telescopios de iniciación](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md); [B43-C01 · Requisitos ópticos y mecánicos](../programa/clases/B43/B43-C01-requisitos-opticos-y-mecanicos/CLASE.md); [B46-C03 · Antenas parabólicas](../programa/clases/B46/B46-C03-antenas-parabolicas/CLASE.md).

### Razón H/L

- La razón `H/L` (altura de caída sobre alcance horizontal total) mide la movilidad.

💡 **Cómo se explica en la clase [B66-C02](../programa/clases/B66/B66-C02-procesos-de-ladera-y-transporte-de-masa/CLASE.md):**
- Además `H/L = μ` exactamente en este modelo: la razón de movilidad lee la fricción efectiva.
- Una ladera de `30°` con material de ángulo de fricción `35°` tiene factor de seguridad `1,2128` en seco y `0,6064` con una razón de presión de poros `0,5`.
- 🎯 **Por qué importa:** Un deslizamiento marciano o titaniano parece igual a uno terrestre, pero su velocidad y duración no lo son. La decisión central: ¿qué propiedades de un deslizamiento dependen de la gravedad y cuáles no?

📘 **Dónde se aprende** (1 clase): [B66-C02 · Procesos de ladera y transporte de masa](../programa/clases/B66/B66-C02-procesos-de-ladera-y-transporte-de-masa/CLASE.md).

### Razón H/r

- La razón `H/r` compara la altura de escala con el radio del cuerpo.

💡 **Cómo se explica en la clase [B54-C16](../programa/clases/B54/B54-C16-atmosferas-de-titan/CLASE.md):**
- Ejercicio 7 · autónomo. ¿Cuánto vale la razón `H/r`?
- El script [titan.py](titan.py) calcula `g`, `H`, `ρ` y la columna (comprueba la densidad media frente a la ficha con 1 % y la razón de alturas de escala).
- 🎯 **Por qué importa:** Titán combina gravedad baja, frío extremo y una atmósfera de N₂ con metano. La pregunta motivadora: ¿por qué una luna pequeña retiene una atmósfera más densa que la terrestre?

📘 **Dónde se aprende** (1 clase): [B54-C16 · Atmósferas de Titán](../programa/clases/B54/B54-C16-atmosferas-de-titan/CLASE.md).

### Razón isotópica

- Una razón isotópica es el cociente entre dos isótopos, como ¹²C/¹³C.

💡 **Cómo se explica en la clase [B06-C03](../programa/clases/B06/B06-C03-isotopos-y-masa-atomica/CLASE.md):**
- P --> R["Razón isotópica: x1/x2, δ respecto de una referencia"]
- *Descripción textual:* tres cajas de isótopos con su masa y su abundancia alimentan un promedio ponderado que produce el peso atómico; de las mismas abundancias salen las razones isotópicas.
- 🎯 **Por qué importa:** El carbono del Sol, ¿es igual que el de la Tierra? Una forma de preguntarlo con rigor es comparar cuántos átomos de carbono-12 hay por cada uno de carbono-13.

📘 **Dónde se aprende** (1 clase): [B06-C03 · Isótopos y masa atómica](../programa/clases/B06/B06-C03-isotopos-y-masa-atomica/CLASE.md).

### Razón LEO/carga

- La razón LEO/carga es la masa que sale de órbita baja por cada kilogramo entregado.

💡 **Cómo se explica en la clase [B100-C06](../programa/clases/B100/B100-C06-logistica-cislunar-nodos-depositos-y-rutas-de-reabastecimiento/CLASE.md):**
- Si todo sube con etapas químicas: `m_LEO = m₀(carga + propelente) + m₀(500 kg)/10 = 7779,2 kg`, razón `7,779`: peor que la ruta directa (+53,6 %), porque se transporta propelente de subida que la ruta A no necesita.
- Con un aterrizador reutilizable de 500 kg secos desde un depósito en NRHO hacen falta `2043,6 kg` de propelente por viaje; si la carga y el propelente suben desde órbita baja con etapas químicas, la razón empeora a `7,779`; con un remolcador eléctrico ilustrativo baja a `4,729` con 10 viajes y supera a la ruta directa desde el viaje 2.
- 🎯 **Por qué importa:** Un depósito en órbita lunar parece una ventaja obvia, pero solo lo es si el propelente llega al depósito de una forma más barata que llevarlo directamente. La decisión central: ¿con qué transporte y con cuántos viajes del aterrizador reutilizable un depósito reduce la masa que hay que lanzar desde órbita baja?

📘 **Dónde se aprende** (1 clase): [B100-C06 · Logística cislunar: nodos, depósitos y rutas de reabastecimiento](../programa/clases/B100/B100-C06-logistica-cislunar-nodos-depositos-y-rutas-de-reabastecimiento/CLASE.md).

### Razón LTV/CAC

- La razón LTV/CAC compara ambos.

💡 **Cómo se explica en la clase [B126-C04](../programa/clases/B126/B126-C04-costo-de-adquisicion-de-clientes-y-economia-unitaria/CLASE.md):**
- A 10 % anual (`r = 0,797 %` mensual) el LTV es `630/(1 − 0,98/(1 + r)) = 22 700 USD` y `LTV/CAC = 5,68`: descontar baja la razón cerca de 28 %.
- *Descripción textual:* el gasto y los clientes nuevos dan el CAC; el margen mensual y el abandono dan el LTV y el plazo; la razón LTV/CAC resume el negocio y se verifica con una serie y una simulación.
- ⚠️ **Error frecuente:** Usar la razón sin descontar ni considerar el plazo. Se corrige con 8.3–8.4.
- 🎯 **Por qué importa:** Un negocio espacial debe medir cuánto cuesta ganar un cliente; el catálogo no lo trata. La decisión central: ¿vale la pena el gasto de captación, dado cuánto tiempo se queda el cliente y cuánto margen deja?

📘 **Dónde se aprende** (1 clase): [B126-C04 · Costo de adquisición de clientes y economía unitaria](../programa/clases/B126/B126-C04-costo-de-adquisicion-de-clientes-y-economia-unitaria/CLASE.md).

### Razón media

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B34-C07](../programa/clases/B34/B34-C07-comparacion-de-modelos-coronales-con-observaciones/CLASE.md):**
- Calcular la correlación y la razón media.
- modelo correlacion razon media D (KS) p asintotico p por permutaciones
- 🎯 **Por qué importa:** Una buena correlación puede ocultar un error de escala. La decisión central: ¿qué métrica detecta cada tipo de discrepancia?

📘 **Dónde se aprende** (1 clase): [B34-C07 · Comparación de modelos coronales con observaciones](../programa/clases/B34/B34-C07-comparacion-de-modelos-coronales-con-observaciones/CLASE.md).

### Razón n/p

- La razón `n/p` es el cociente de neutrones y protones.

💡 **Cómo se explica en la clase [B26-C16](../programa/clases/B26/B26-C16-nucleosintesis-primordial/CLASE.md):**
- *Descripción textual:* la diferencia de masa fija la razón de equilibrio; tras la congelación los neutrones se desintegran hasta que el deuterio sobrevive; todos los neutrones restantes forman helio-4 y fijan `Y_p`.
- Calcular la razón `n/p` en equilibrio y tras la desintegración libre.
- 🎯 **Por qué importa:** La cuarta parte de la masa bariónica del universo es helio, y la proporción casi no cambió desde los primeros minutos. Su valor da información sobre cuántas especies de neutrinos existen y sobre la densidad de bariones.

📘 **Dónde se aprende** (1 clase): [B26-C16 · Nucleosíntesis primordial](../programa/clases/B26/B26-C16-nucleosintesis-primordial/CLASE.md).

### Razón O/F

- La razón O/F es la masa de oxidante por masa de combustible.
- La razón O/F de 3,5 es rica en combustible frente a la estequiométrica (3,99).

💡 **Cómo se explica en la clase [B59-C01](../programa/clases/B59/B59-C01-concepto-de-utilizacion-de-recursos-in-situ/CLASE.md):**
- Para el ejemplo, `v_e = 3 530,4 m/s`, `Δv/v_e = 1,1613` y la razón de masas es `3,1942`: `m_p = 5 485,6 kg`.
- La razón `O/F = 3,5` reparte `m_p` en `3,5/4,5 = 77,8 %` de oxidante (`4 266,5 kg`) y `1 219,0 kg` de combustible.
- 🎯 **Por qué importa:** Cada kilogramo que se lanza arrastra consigo más propelente para lanzarlo. La decisión central: ¿cuánta masa de planta de producción compensa el oxidante que dejas de llevar?

📘 **Dónde se aprende** (2 clases): [B59-C01 · Concepto de utilización de recursos in situ](../programa/clases/B59/B59-C01-concepto-de-utilizacion-de-recursos-in-situ/CLASE.md); [B59-C09 · Fabricación de combustibles conceptuales](../programa/clases/B59/B59-C09-fabricacion-de-combustibles-conceptuales/CLASE.md).

### Razón pico/segundo pico

- La razón pico/segundo pico mide la unicidad.

💡 **Cómo se explica en la clase [B74-C26](../programa/clases/B74/B74-C26-navegacion-por-hitos-y-correlacion-de-terreno/CLASE.md):**
- En un terreno periódico de 16 px, el pico (`0,970`) y el segundo (`0,968`) casi coinciden (razón `1,00`): el desplazamiento hallado en `y` es `12,00` frente a `−3,82` verdadero: se confunde un periodo.
- *Descripción textual:* la plantilla se desliza sobre la imagen para calcular la NCC; el pico con su refinamiento da el desplazamiento y la razón pico/segundo pico decide si el emparejamiento es único y aceptable.
- 🎯 **Por qué importa:** Un buen pico de correlación no garantiza un buen emparejamiento: en un terreno repetitivo hay dos picos casi iguales. La decisión central: ¿cuánta precisión da la correlación en un terreno rico, y cuándo el emparejamiento es ambiguo y no debe usarse?

📘 **Dónde se aprende** (1 clase): [B74-C26 · Navegación por hitos y correlación de terreno](../programa/clases/B74/B74-C26-navegacion-por-hitos-y-correlacion-de-terreno/CLASE.md).

### Razón polvo/gas del plano medio

- La razón polvo/gas del plano medio es `ρ_d/ρ_gas`.

💡 **Cómo se explica en la clase [B52-C04](../programa/clases/B52/B52-C04-formacion-de-planetesimales/CLASE.md):**
- Descripción larga: la razón polvo/gas necesaria es de cientos y baja hacia afuera, porque el gas del plano medio se enrarece más rápido hacia afuera que `ρ_H`.
- Calcular la razón polvo/gas del plano medio que alcanza la densidad de Hill.
- 🎯 **Por qué importa:** Si la autogravedad solo gana contra las mareas por encima de cierta densidad, esa densidad fija cuánto debe concentrarse el polvo. La decisión central: ¿qué densidad necesita un cúmulo de partículas para colapsar a una distancia dada?

📘 **Dónde se aprende** (1 clase): [B52-C04 · Formación de planetesimales](../programa/clases/B52/B52-C04-formacion-de-planetesimales/CLASE.md).

### Razón tensor-escalar

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B40-C05):** El espectro es el vínculo entre la inflación y las anisotropías. La decisión central: ¿qué predice el modelo para `n_s` y `r`, y es compatible con los límites publicados?

📘 **Dónde se aprende** (1 clase): [B40-C05 · Perturbaciones primordiales y espectro escalar](../programa/clases/B40/B40-C05-perturbaciones-primordiales-y-espectro-escalar/CLASE.md).

### Razones trigonométricas

- Las razones trigonométricas son: `sen θ = opuesto/hipotenusa`, `cos θ = adyacente/hipotenusa` y `tan θ = opuesto/adyacente`.

💡 **Cómo se explica en la clase [B03-C18](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md):**
- python programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/laboratorio_triangulos.py
- 🎯 **Por qué importa:** El Sol y la Luna se ven en el cielo con tamaños angulares muy parecidos, de alrededor de medio grado. ¿Es casualidad que midan lo mismo en el cielo siendo tan distintos?

📘 **Dónde se aprende** (1 clase): [B03-C18 · Razones trigonométricas iniciales](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md).

### RCMC

- La RCMC es su corrección.

💡 **Cómo se explica en la clase [B69-C02](../programa/clases/B69/B69-C02-formacion-de-imagenes-sar/CLASE.md):**
- RC --> RCMC["corrección de migración (RCMC)"]
- Por el laboratorio: con y sin RCMC se compara la anchura.
- 🎯 **Por qué importa:** Sin procesamiento, un eco crudo parece ruido. La decisión central: ¿qué operaciones convierten el eco crudo en una imagen con la resolución teórica, y cuándo fallan?

📘 **Dónde se aprende** (1 clase): [B69-C02 · Formación de imágenes SAR](../programa/clases/B69/B69-C02-formacion-de-imagenes-sar/CLASE.md).

### RCV

- El RCV es `√2·z·√(CVa² + CVi²)` (fórmula estándar, no consultada aquí).

💡 **Cómo se explica en la clase [B105-C24](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md):**
- I["CVi, CVa"] --> V["RCV = raiz2 z raiz(CVa^2+CVi^2)"]
- *Descripción textual:* el intervalo poblacional y el RCV personal son dos reglas para decidir si un valor es anómalo o ha cambiado; un umbral se evalúa con sensibilidad, especificidad y valor predictivo según la prevalencia.
- ⚠️ **Error frecuente:** Usar solo el intervalo poblacional para vigilar a una persona. Usa la línea base y el RCV (8.2).
- 🎯 **Por qué importa:** Con tripulaciones pequeñas, el intervalo de la población general es poco sensible a los cambios personales, y un umbral con baja prevalencia da más falsas alarmas que aciertos. La decisión central: ¿cuándo un cambio de un indicador es real y qué umbral equilibra sensibilidad y valor predictivo?

📘 **Dónde se aprende** (1 clase): [B105-C24 · Indicadores clínicos y biomarcadores de vuelo](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md).

### RDM

- El RDM (*radiation design margin*) es el cociente exigido entre la dosis tolerada y la de misión.
- El RDM (*radiation design margin*) `= dosis de fallo / dosis de misión`.

💡 **Cómo se explica en la clase [B88-C03](../programa/clases/B88/B88-C03-procesadores-tolerantes-a-radiacion/CLASE.md):**
- D["Dosis de mision y de fallo"] --> M["RDM"]
- La misión acumula 20 krad(Si) y el componente falla a 60 krad(Si): `RDM = 3`.
- 🎯 **Por qué importa:** Un procesador comercial puede fallar en órbita por una sola partícula. La decisión central: ¿cuántos eventos esperar al año y qué margen de dosis hay respecto del fallo del componente?

📘 **Dónde se aprende** (2 clases): [B88-C03 · Procesadores tolerantes a radiación](../programa/clases/B88/B88-C03-procesadores-tolerantes-a-radiacion/CLASE.md); [B95-C02 · Componentes comerciales en vuelo: selección y riesgo](../programa/clases/B95/B95-C02-componentes-comerciales-en-vuelo-seleccion-y-riesgo/CLASE.md).

### Reacción

- La reacción es `R = K u − f` en los GDL restringidos.
- La reacción es el par o la fuerza igual y opuesta sobre quien opera la herramienta.

💡 **Cómo se explica en la clase [B84-C28](../programa/clases/B84/B84-C28-condiciones-de-contorno-y-cargas-en-modelos-de-elementos-finitos/CLASE.md):**
- En ambos casos las reacciones son `−50 N` y `−50 N` (suma `−100 N = −qL`).
- La suma de reacciones iguala la carga total: es la comprobación mínima de cualquier modelo.
- ⚠️ **Error frecuente:** No comprobar reacciones. Se corrige con 8.3.
- 🎯 **Por qué importa:** Una restricción de menos deja la matriz singular; una de más introduce tensiones falsas; una carga mal repartida cambia la flecha 1,25 %: son los errores más frecuentes en los modelos. La decisión central: ¿está el modelo bien restringido y cargado y cómo lo demuestro?

📘 **Dónde se aprende** (2 clases): [B84-C28 · Condiciones de contorno y cargas en modelos de elementos finitos](../programa/clases/B84/B84-C28-condiciones-de-contorno-y-cargas-en-modelos-de-elementos-finitos/CLASE.md); [B108-C03 · Herramientas y equipos de EVA](../programa/clases/B108/B108-C03-herramientas-y-equipos-de-eva/CLASE.md).

### Reacción de pseudo-primer orden

- Una reacción de pseudo-primer orden es una de segundo orden con un reactivo en gran exceso.

🎯 **Por qué importa (clase B55-C03):** En el espacio la densidad es tan baja que una reacción puede tardar siglos o millones de años, y la temperatura de 10 K cierra casi todas las reacciones con barrera. Saber cuáles ocurren define qué moléculas pueden existir.

📘 **Dónde se aprende** (1 clase): [B55-C03 · Reacciones en medio interestelar](../programa/clases/B55/B55-C03-reacciones-en-medio-interestelar/CLASE.md).

### Reacción de Sabatier

- La reacción de Sabatier combina CO₂ e H₂ para dar CH₄ y agua.

💡 **Cómo se explica en la clase [B59-C09](../programa/clases/B59/B59-C09-fabricacion-de-combustibles-conceptuales/CLASE.md):**
- Escribir y balancear la reacción de Sabatier por elementos.
- Entalpia de la reaccion de Sabatier (agua en gas) = -165.01 kJ/mol de CH4 (exotermica)
- 🎯 **Por qué importa:** Un combustible fabricado en destino depende de qué parte del hidrógeno se recicla. La decisión central: ¿cuánto hidrógeno hay que importar para fabricar 1 000 kg de propelente O₂/CH₄?

📘 **Dónde se aprende** (1 clase): [B59-C09 · Fabricación de combustibles conceptuales](../programa/clases/B59/B59-C09-fabricacion-de-combustibles-conceptuales/CLASE.md).

### Reacción máxima

- La reacción máxima `μ m g` es la fuerza que la máquina puede aplicar sin deslizarse.

💡 **Cómo se explica en la clase [B97-C25](../programa/clases/B97/B97-C25-excavacion-y-manejo-de-regolito-con-robots/CLASE.md):**
- *Descripción textual:* la fuerza de corte del suelo y la reacción máxima de la máquina se igualan para dar la profundidad máxima, que fija el volumen y la productividad.
- Descripción larga: la profundidad máxima cae con la gravedad porque la reacción es proporcional a `g` mientras el corte lo es poco; y la productividad está dominada por el acarreo.
- 🎯 **Por qué importa:** Una excavadora diseñada y probada en la Tierra puede ser incapaz de cortar en la Luna por falta de reacción, no por falta de potencia. Es un error de diseño caro que un cálculo de pocos renglones evita.

📘 **Dónde se aprende** (1 clase): [B97-C25 · Excavación y manejo de regolito con robots](../programa/clases/B97/B97-C25-excavacion-y-manejo-de-regolito-con-robots/CLASE.md).

### Reacción química

- Una reacción química es un proceso en el que los átomos se reordenan para formar sustancias distintas.

💡 **Cómo se explica en la clase [B06-C08](../programa/clases/B06/B06-C08-reacciones-y-conservacion-de-masa/CLASE.md):**
- En una reacción química, las piezas son los átomos.
- *Descripción textual:* arriba, una reacción química: los reactivos se transforman en productos con los mismos átomos.
- 🎯 **Por qué importa:** Una vela y el Sol liberan energía, pero lo hacen de maneras radicalmente distintas. En la vela, los átomos de carbono e hidrógeno se reordenan con el oxígeno y todos siguen ahí al terminar.

📘 **Dónde se aprende** (1 clase): [B06-C08 · Reacciones y conservación de masa](../programa/clases/B06/B06-C08-reacciones-y-conservacion-de-masa/CLASE.md).

### Reactividad Re

- La reactividad `Re` se da en cm³/átomo (`1 cm³ = 10⁻⁶ m³`).

💡 **Cómo se explica en la clase [B85-C13](../programa/clases/B85/B85-C13-efectos-de-oxigeno-atomico/CLASE.md):**
- *Descripción textual:* la densidad y la velocidad dan el flujo de proa; integrado en el tiempo es la fluencia; multiplicada por la reactividad da el espesor perdido y la vida de la capa.
- Límite: la reactividad real depende de la energía de impacto, la temperatura y de si hay defectos que permiten socavar la capa protectora.
- 🎯 **Por qué importa:** Un polímero exterior puede desaparecer en meses en la cara de proa a baja altitud. La decisión central: ¿cuánto espesor pierde una superficie por año según la altitud y la orientación, y qué protección dura la misión?

📘 **Dónde se aprende** (1 clase): [B85-C13 · Efectos de oxígeno atómico](../programa/clases/B85/B85-C13-efectos-de-oxigeno-atomico/CLASE.md).

### Reactivo en exceso

- El reactivo en exceso queda sin reaccionar en los productos y baja la temperatura.

💡 **Cómo se explica en la clase [B78-C05](../programa/clases/B78/B78-C05-propulsion-bipropelente-conceptual/CLASE.md):**
- Ejercicio 2 · guiado (con una pista). Predice cuál es el reactivo en exceso si `O/F = 4` en H₂/O₂.
- 🎯 **Por qué importa:** Un motor puede quemar mezclas con exceso de combustible o de oxidante. La decisión central: ¿qué `O/F` maximiza el escape en un modelo sin disociación y por qué los motores reales operan en otro punto?

📘 **Dónde se aprende** (1 clase): [B78-C05 · Propulsión bipropelente conceptual](../programa/clases/B78/B78-C05-propulsion-bipropelente-conceptual/CLASE.md).

### Reactivos

- Los reactivos son H₂ y O₂.
- Los reactivos están a la izquierda y los productos a la derecha de una ecuación química.

💡 **Cómo se explica en la clase [B06-C08](../programa/clases/B06/B06-C08-reacciones-y-conservacion-de-masa/CLASE.md):**
- Se escriben las fórmulas de los reactivos, una flecha y las de los productos: `CH₄ + O₂ → CO₂ + H₂O`.
- R["Reactivos: CH4 + O2"] -->|"átomos se reordenan"| P["Productos: CO2 + H2O"]
- 🎯 **Por qué importa:** Una vela y el Sol liberan energía, pero lo hacen de maneras radicalmente distintas. En la vela, los átomos de carbono e hidrógeno se reordenan con el oxígeno y todos siguen ahí al terminar.

📘 **Dónde se aprende** (2 clases): [B06-C08 · Reacciones y conservación de masa](../programa/clases/B06/B06-C08-reacciones-y-conservacion-de-masa/CLASE.md); [B86-C15 · Sistemas de combustible como alternativa](../programa/clases/B86/B86-C15-sistemas-de-combustible-como-alternativa/CLASE.md).

### README

- Un README es el archivo de entrada de un proyecto: qué es, cómo instalarlo, cómo ejecutarlo y de dónde vienen los datos.

💡 **Cómo se explica en la clase [B07-C19](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md):**
- Un README no sustituye las docstrings: el README describe el proyecto; las docstrings, cada pieza.
- Reproducir exige que otra persona, con tu README y tu registro, llegue al mismo resultado en su máquina.
- 🎯 **Por qué importa:** Un resultado que solo su autor puede obtener, y solo el día en que lo obtuvo, es una anécdota. Cuando pasan seis meses, no sabrás con qué datos, con qué versión ni con qué semilla lo generaste.

📘 **Dónde se aprende** (1 clase): [B07-C19 · Documentación y reproducibilidad](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md).

### Reajuste

- El reajuste (*retracking*) estima `t0` ajustando un modelo.

💡 **Cómo se explica en la clase [B57-C09](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md):**
- Esta clase no las incluye: los ensayos del laboratorio (400 por caso) solo prueban el reajuste.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de altimetría satelital*: la tabla del error del reajuste con 25 y 100 pulsos, la precisión temporal para 1 cm y la lista de correcciones ausentes.
- 🎯 **Por qué importa:** La altura del mar cambia unos milímetros por año, pero el eco de un pulso es ruidoso. La decisión central: ¿cuántos pulsos hay que promediar y cómo se ajusta el eco para que el error de distancia del ajuste se reduzca lo necesario?

📘 **Dónde se aprende** (1 clase): [B57-C09 · Altimetría satelital](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md).

### Real

- Un gas no ideal o real se desvía del modelo: sus moléculas ocupan volumen y se atraen.

💡 **Cómo se explica en la clase [B06-C09](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md):**
- Un gas real se desvía cuando las moléculas están cerca (presión alta) y cuando la temperatura se acerca a la de condensación.
- E -->|"No"| G["Usar Z o un modelo real (van der Waals o datos)"]
- ⚠️ **Error frecuente:** Tomar el modelo isotermo como perfil real. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** La NASA publica para Marte, Venus y la Tierra la presión y la temperatura medias en la superficie, la gravedad, el peso molecular de la atmósfera y su densidad (S1, S2, S3). ¿Puedes reproducir esa densidad con sólo lo anterior?

📘 **Dónde se aprende** (1 clase): [B06-C09 · Gases ideales y no ideales](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md).

### Realidad sintética

- Gemelo digital: modelo actualizado con datos del sistema real. Realidad sintética: el «sistema» simulado con errores inventados.

💡 **Cómo se explica en la clase [B101-C08](../programa/clases/B101/B101-C08-gemelo-digital-para-ensayo-de-reparaciones-roboticas/CLASE.md):**
- Planificar con el gemelo y ejecutar en la «realidad» sintética.
- No: su «realidad» es sintética; un gemelo real necesita validarse contra datos de vuelo y de ensayo y aprobarse por quien tiene la autoridad.
- 🎯 **Por qué importa:** Una reparación robótica no se improvisa: se ensaya. Pero un ensayo vale solo si el gemelo se parece a la realidad.

📘 **Dónde se aprende** (1 clase): [B101-C08 · Gemelo digital para ensayo de reparaciones robóticas](../programa/clases/B101/B101-C08-gemelo-digital-para-ensayo-de-reparaciones-roboticas/CLASE.md).

### Realimentación de estados

- La realimentación de estados es `u = −K x`, que da el lazo cerrado `ẋ = (A − B K) x`.

💡 **Cómo se explica en la clase [B16-C07](../programa/clases/B16/B16-C07-realimentacion-y-estabilidad/CLASE.md):**
- Calcular los polos del lazo cerrado de un sistema con realimentación de estados o PD.
- 🎯 **Por qué importa:** Un lazo de control puede estabilizar un sistema inestable o desestabilizar uno estable. Un telescopio con el lazo mal diseñado no solo apunta mal: oscila, consume propergol o energía de las ruedas y puede perder el objetivo.

📘 **Dónde se aprende** (1 clase): [B16-C07 · Realimentación y estabilidad](../programa/clases/B16/B16-C07-realimentacion-y-estabilidad/CLASE.md).

### Realización

- Una realización es la forma práctica de reproducir una unidad con un instrumento (por ejemplo, un reloj de cesio); no es la definición.
- Una realización del ITRS se llama ITRF (*International Terrestrial Reference Frame*): coordenadas y velocidades de estaciones que materializan el sistema (S1, §4.1.5).

💡 **Cómo se explica en la clase [B13-C06](../programa/clases/B13/B13-C06-patrones-de-longitud-y-tiempo/CLASE.md):**
- La realización es cómo se reproduce la unidad en un laboratorio y siempre tiene incertidumbre.
- Los laboratorios nacionales realizan el segundo con relojes de átomos de cesio; las realizaciones específicas y sus incertidumbres actuales no se consultaron en esta sesión, por lo que aquí solo se usan valores de ejemplo para las desviaciones de frecuencia.
- 🎯 **Por qué importa:** Cuando un telémetro láser mide la distancia a la Luna, lo que mide es el tiempo que tarda un pulso en ir y volver. Un error de un nanosegundo en ese tiempo equivale a 15 centímetros de distancia.

📘 **Dónde se aprende** (2 clases): [B13-C06 · Patrones de longitud y tiempo](../programa/clases/B13/B13-C06-patrones-de-longitud-y-tiempo/CLASE.md); [B13-C11 · Sistemas de referencia terrestres](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md).

### Recálculo hacia atrás

- El recálculo hacia atrás (*back-calculation*) realimenta la diferencia `sat(v) − v` a la integral: `ξ̇ = e + K_aw (sat(v) − v)`.

💡 **Cómo se explica en la clase [B16-C18](../programa/clases/B16/B16-C18-saturacion-y-anti-windup/CLASE.md):**
- S -. "sat(v) − v" .-> AW["recálculo hacia atrás<br/>Kaw"] -.-> I["integral ξ"]
- Recálculo hacia atrás: suave, con un parámetro.
- 🎯 **Por qué importa:** Una rueda de reacción entrega un par máximo y almacena un momento angular máximo (el Hubble usa ruedas de hasta unas 3000 rpm, y magnetopares para gestionar su velocidad, S1). Cuando el controlador pide más de lo que el actuador puede dar, el lazo deja de comportarse como se diseñó.

📘 **Dónde se aprende** (1 clase): [B16-C18 · Saturación y anti-windup](../programa/clases/B16/B16-C18-saturacion-y-anti-windup/CLASE.md).

### Recalentamiento

- El recalentamiento convierte la energía del campo en radiación.

💡 **Cómo se explica en la clase [B40-C02](../programa/clases/B40/B40-C02-recalentamiento-y-transicion-a-la-era-de-radiacion/CLASE.md):**
- La densidad total en la igualdad es `1,006 × 10⁻⁴`, el `0,335` de `3Γ² = 3 × 10⁻⁴`: el recalentamiento no es instantáneo en `H = Γ`.
- El paso a la radiación ocurre en torno a `t ~ 1/Γ`, con un factor de orden uno que depende de la definición de «recalentamiento».
- ⚠️ **Error frecuente:** Creer que el recalentamiento es instantáneo. Se corrige con 8.2.
- 🎯 **Por qué importa:** Sin recalentamiento no habría universo caliente. La decisión central: ¿cuándo domina la radiación y qué temperatura alcanza?

📘 **Dónde se aprende** (1 clase): [B40-C02 · Recalentamiento y transición a la era de radiación](../programa/clases/B40/B40-C02-recalentamiento-y-transicion-a-la-era-de-radiacion/CLASE.md).

### Recalibración

- Discrepancia: diferencia entre el modelo y la realidad. Recalibración: actualizar los parámetros del gemelo.

💡 **Cómo se explica en la clase [B101-C08](../programa/clases/B101/B101-C08-gemelo-digital-para-ensayo-de-reparaciones-roboticas/CLASE.md):**
- M["Mediciones de la realidad"] --> C["Recalibracion"]
- comprueba que el gemelo nominal falla, que el perfecto no, que la recalibración devuelve el margen y que la probabilidad decrece.
- 🎯 **Por qué importa:** Una reparación robótica no se improvisa: se ensaya. Pero un ensayo vale solo si el gemelo se parece a la realidad.

📘 **Dónde se aprende** (1 clase): [B101-C08 · Gemelo digital para ensayo de reparaciones robóticas](../programa/clases/B101/B101-C08-gemelo-digital-para-ensayo-de-reparaciones-roboticas/CLASE.md).

### Recall

- El recall es la fracción del suelo verdadero recuperada; la contaminación es la fracción de lo clasificado como suelo que no lo es.

💡 **Cómo se explica en la clase [B57-C30](../programa/clases/B57/B57-C30-nubes-de-puntos-tridimensionales/CLASE.md):**
- El filtro (plano inicial por mínimo en celdas de 5 m, refinado tres veces con los puntos a menos de 1,2; 0,7 y 0,35 m) clasifica `20003` puntos como suelo con un recall de `1,000` y una contaminación de `0,01%`: los puntos de tronco bajo y de maleza sintética que caen bajo el umbral.
- Aplicar un filtro de suelo (mínimo por celda y refinamiento del plano) y medir su recall y contaminación.
- 🎯 **Por qué importa:** Un modelo de terreno malo hace que las pendientes y las alturas de los árboles salgan mal. La decisión central: ¿cómo se separa el suelo del resto con la menor contaminación y qué densidad de puntos hace falta?

📘 **Dónde se aprende** (1 clase): [B57-C30 · Nubes de puntos tridimensionales](../programa/clases/B57/B57-C30-nubes-de-puntos-tridimensionales/CLASE.md).

### Recargo

- El recargo `L` cubre gastos y margen.
- El recargo cubre gastos, capital y margen.

💡 **Cómo se explica en la clase [B124-C08](../programa/clases/B124/B124-C08-seguros-y-riesgo-espacial/CLASE.md):**
- Por satélite, `p V = 0,04 · 300 = 12` um y la prima con recargo del 35 % es `16,20` um.
- Calcular la pérdida esperada y una prima con recargo.
- 🎯 **Por qué importa:** El seguro no elimina el riesgo: lo traslada a quien puede juntarlo. La decisión central: ¿cuánto cobrar por cubrir un riesgo y con qué probabilidad el asegurador se queda sin capital?

📘 **Dónde se aprende** (2 clases): [B124-C08 · Seguros y riesgo espacial](../programa/clases/B124/B124-C08-seguros-y-riesgo-espacial/CLASE.md); [B127-C01 · Seguros de lanzamiento](../programa/clases/B127/B127-C01-seguros-de-lanzamiento/CLASE.md).

### Receptancia

- La receptancia `H_ij(ω)` es el desplazamiento en `i` por fuerza unitaria en `j`.

💡 **Cómo se explica en la clase [B84-C33](../programa/clases/B84/B84-C33-respuesta-armonica-y-funciones-de-transferencia-estructural/CLASE.md):**
- Integrador. Elabora tu *ficha de función de transferencia estructural*: modos, receptancia directa y modal, picos, fases, `ζ` por potencia mitad y su uso en vibración aleatoria.
- Receptancia |H21| [m/N] y fase en frecuencias seleccionadas:
- 🎯 **Por qué importa:** La función de transferencia dice cuánto se amplifica cada frecuencia entre el punto donde se excita y el punto donde se mide; es la herramienta que usan el análisis y el ensayo de barrido sinusoidal. La decisión central: ¿cuánto se amplifica la respuesta en cada frecuencia y cuánto amortiguamiento tiene cada modo?

📘 **Dónde se aprende** (1 clase): [B84-C33 · Respuesta armónica y funciones de transferencia estructural](../programa/clases/B84/B84-C33-respuesta-armonica-y-funciones-de-transferencia-estructural/CLASE.md).

### Recesión

- La recesión es el espesor eliminado por ablación.

💡 **Cómo se explica en la clase [B77-C16](../programa/clases/B77/B77-C16-proteccion-termica/CLASE.md):**
- Estimar una recesión conceptual con una energía de ablación ilustrativa.
- Ejercicio 8 · autónomo. Recesión para `Q* = 50 MJ/kg`.
- 🎯 **Por qué importa:** La temperatura de la cara trasera es la que decide si la estructura sobrevive. La decisión central: ¿cuánto del calor entrante se re-radia, cuánto se almacena y cuánto sube la temperatura trasera con un espesor dado?

📘 **Dónde se aprende** (1 clase): [B77-C16 · Protección térmica](../programa/clases/B77/B77-C16-proteccion-termica/CLASE.md).

### Rechaza

- El error normalizado `err = máx_i |Δ_i| / sc_i`; el paso se acepta si `err ≤ 1` y se rechaza si no.

💡 **Cómo se explica en la clase [B11-C08](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md):**
- El error normalizado es `1,52 × 10⁻⁵/6,07 × 10⁻⁶ = 2,5 > 1`: se rechaza el paso.
- Su límite: el conductor ve la curva que viene; el integrador solo juzga el tramo que ya intentó, por eso a veces rechaza.
- 🎯 **Por qué importa:** Casi ninguna simulación espacial tiene un ritmo uniforme: una nave que rodea un planeta con un perigeo bajo, una sonda que pasa cerca de una luna, un encuentro cercano entre dos cuerpos. Escoger `h` a mano es adivinar.

📘 **Dónde se aprende** (1 clase): [B11-C08 · Integradores de paso adaptativo](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md).

### Rechazo de calor

- El rechazo de calor es `Q_rej = Q_th − P_e`.

💡 **Cómo se explica en la clase [B86-C17](../programa/clases/B86/B86-C17-energia-nuclear-espacial-conceptual/CLASE.md):**
- El script [fision_conceptual.py](fision_conceptual.py) calcula la eficiencia, el calor rechazado, el área y la masa del radiador y busca la temperatura de rechazo de área mínima (comprueba sección áurea frente a barrido < `0,5 K` y, con `f = 1`, el óptimo `3/4` con diferencia < 1e-6).
- 🎯 **Por qué importa:** En el espacio el único sumidero de calor es la radiación, y el calor rechazado de un ciclo térmico es grande. La temperatura del radiador y la del ciclo determinan la eficiencia y el área, y el área determina la masa.

📘 **Dónde se aprende** (1 clase): [B86-C17 · Energía nuclear espacial conceptual](../programa/clases/B86/B86-C17-energia-nuclear-espacial-conceptual/CLASE.md).

### Rechazo de imagen

- El rechazo de imagen (IRR) compara señal y imagen.

💡 **Cómo se explica en la clase [B46-C07](../programa/clases/B46/B46-C07-receptores-superheterodinos/CLASE.md):**
- *Descripción textual:* señal e imagen se mezclan con el oscilador local y caen en la misma FI, que un mezclador de rechazo separa con errores finitos.
- Calcular el rechazo de imagen con errores.
- 🎯 **Por qué importa:** La mezcla es lo que permite procesar en una banda cómoda, pero trae consigo una segunda frecuencia que cae en la misma FI. La decisión central: ¿qué rechazo de imagen exige el receptor y cómo se logra?

📘 **Dónde se aprende** (1 clase): [B46-C07 · Receptores superheterodinos](../programa/clases/B46/B46-C07-receptores-superheterodinos/CLASE.md).

### Reciclaje instantáneo

- El reciclaje instantáneo supone que las estrellas masivas devuelven sus metales de inmediato.

💡 **Cómo se explica en la clase [B25-C17](../programa/clases/B25/B25-C17-metallicidad-y-evolucion-quimica/CLASE.md):**
- No hay entrada de gas ni mezcla gradual; el reciclaje es instantáneo, lo que falla para elementos producidos por supernovas de tipo Ia o estrellas de baja masa (B24-C21);
- Definir metalicidad `Z`, rendimiento, fracción de gas, reciclaje instantáneo y carga de masa.
- 🎯 **Por qué importa:** Cada generación de estrellas fabrica elementos pesados y los devuelve al gas; la proporción de metales de una galaxia cuenta cuánto se ha procesado su gas. En astronomía, «metales» son todos los elementos más pesados que el helio.

📘 **Dónde se aprende** (1 clase): [B25-C17 · Metalicidad y evolución química](../programa/clases/B25/B25-C17-metallicidad-y-evolucion-quimica/CLASE.md).

### Recíproco

- El recíproco de `a/b` es `b/a`.

🎯 **Por qué importa (clase B03-C02):** Una cifra aislada como «69 911 km» no dice si Júpiter es grande o pequeño. Una razón sí: Júpiter tiene un radio unas 11 veces el terrestre.

📘 **Dónde se aprende** (1 clase): [B03-C02 · Fracciones y razones de magnitudes](../programa/clases/B03/B03-C02-fracciones-y-razones-de-magnitudes/CLASE.md).

### Recombinación

- La recombinación es la captura de un electrón por un protón; su coeficiente `β₂` (en `cm³ s⁻¹`) mide cuántas recombinaciones ocurren por unidad de tiempo y de densidad al cuadrado.
- La recombinación es el paso del plasma a átomos neutros.

💡 **Cómo se explica en la clase [B25-C05](../programa/clases/B25/B25-C05-regiones-de-formacion-estelar/CLASE.md):**
- En una esfera de hidrógeno totalmente ionizado de radio `R` y densidad `n`, el número de recombinaciones por segundo es `(4π/3) R³ n² β₂`.
- Analogía: el aire es la luz ionizante `Q` y las fugas son las recombinaciones.
- 🎯 **Por qué importa:** Una galaxia no convierte todo su gas en estrellas a la vez: lo hace a un ritmo que puede medirse y comparar. Entender las regiones donde nacen las estrellas masivas permite reconocerlas desde lejos, y entender la relación entre gas y ritmo de formación permite saber cuánto tiempo puede una galaxia seguir formando estrellas.

📘 **Dónde se aprende** (2 clases): [B25-C05 · Regiones de formación estelar](../programa/clases/B25/B25-C05-regiones-de-formacion-estelar/CLASE.md); [B26-C14 · Evolución térmica del universo](../programa/clases/B26/B26-C14-evolucion-termica-del-universo/CLASE.md).

### Recombinación disociativa

- La recombinación disociativa es la destrucción de un ion por un electrón.

🎯 **Por qué importa (clase B55-C04):** Una nube molecular fría es un reactor lento sostenido por una fuente débil de ionización. Entender el balance de una sola especie clave enseña a leer cualquier red.

📘 **Dónde se aprende** (1 clase): [B55-C04 · Química de nubes moleculares](../programa/clases/B55/B55-C04-quimica-de-nubes-moleculares/CLASE.md).

### Recomendación

- La recomendación orienta; la obligación se exige.

💡 **Cómo se explica en la clase [B121-C05](../programa/clases/B121/B121-C05-cumplimiento-regulatorio-en-varias-jurisdicciones/CLASE.md):**
- La matriz usa dos jurisdicciones con requisitos consultados el 2026-11-11: las directrices IADC Rev. 4 (25 años, `P ≥ 0,9`, `Ec ≤ 10⁻⁴` en reentrada; recomendaciones) y las normas estadounidenses 47 CFR 25.114 (5 años, `P ≥ 0,9`, `Ec < 10⁻⁴`) y 14 CFR 450.101 (`Ec ≤ 10⁻⁴` en el lanzamiento).
- Lo marcas como recomendación en la matriz y decides si lo adoptas por prudencia; no es un incumplimiento legal.
- ⚠️ **Error frecuente:** Confundir una recomendación con una obligación. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Ninguna clase trata el análisis de cumplimiento. La decisión central: ¿cuál es el requisito más estricto de cada tipo, qué incumple el diseño y cuánto tardan los trámites?

📘 **Dónde se aprende** (1 clase): [B121-C05 · Cumplimiento regulatorio en varias jurisdicciones](../programa/clases/B121/B121-C05-cumplimiento-regulatorio-en-varias-jurisdicciones/CLASE.md).

### Reconciliación

- La reconciliación compara dos mensajes.

💡 **Cómo se explica en la clase [B118-C22](../programa/clases/B118/B118-C22-intercambio-de-datos-de-vigilancia-entre-operadores-y-estados/CLASE.md):**
- Descripción larga: el mismo evento en otras unidades se reconcilia sin diferencias; una unidad errónea produce un factor 1000 y se detecta; los cinco mensajes defectuosos se rechazan.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de intercambio de un mensaje de conjunción*: esquema, mensaje de ejemplo, conversión de unidades, reconciliación con un segundo operador, casos de rechazo y la lista de qué es consultado (la ficha del CDM), propio y no consultado.
- 🎯 **Por qué importa:** B118-C18 trata la gestión del tráfico en general, pero no cubre formatos ni acuerdos de intercambio. Un error de unidades (metros contra kilómetros) puede cambiar una decisión por un factor 1000.

📘 **Dónde se aprende** (1 clase): [B118-C22 · Intercambio de datos de vigilancia entre operadores y Estados](../programa/clases/B118/B118-C22-intercambio-de-datos-de-vigilancia-entre-operadores-y-estados/CLASE.md).

### Reconexión

- La reconexión es el cambio de conectividad del campo.

💡 **Cómo se explica en la clase [B30-C11](../programa/clases/B30/B30-C11-reconexion-magnetica/CLASE.md):**
- Descripción larga: la tasa cae como `S^(−1/2)` y el tiempo de reconexión crece en la misma proporción.
- Calcular el tiempo de reconexión `τ_A S^(1/2)`.
- 🎯 **Por qué importa:** Las erupciones liberan en minutos una energía que el campo guardó durante mucho más tiempo, y el modelo más simple de reconexión es demasiado lento para eso. La decisión central: ¿qué tasa de reconexión hace falta y qué dice el modelo de Sweet–Parker?

📘 **Dónde se aprende** (1 clase): [B30-C11 · Reconexión magnética](../programa/clases/B30/B30-C11-reconexion-magnetica/CLASE.md).

### Reconocimiento ratable

- El reconocimiento ratable reparte el ingreso en partes iguales en el plazo.

🎯 **Por qué importa (clase B125-C02):** El modelo de ingresos define cuándo entra el dinero y cuánto vale un cliente; ninguna clase anterior lo trata. La decisión central: ¿cuánto vale un cliente de suscripción, cuándo se reconoce su ingreso y cuánto abandono puede tolerar el negocio?

📘 **Dónde se aprende** (1 clase): [B125-C02 · Modelos de ingresos: suscripción y servicio](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md).

### Reconstrucción

- La reconstrucción estima los valores que faltan usando un modelo o una restricción.

💡 **Cómo se explica en la clase [B15-C19](../programa/clases/B15/B15-C19-reconstruccion-por-datos-incompletos/CLASE.md):**
- Una reconstrucción que no puede validarse no debería entrar en un análisis cuantitativo.
- Formular los requisitos de una reconstrucción (qué se usa después, qué error es tolerable).
- 🎯 **Por qué importa:** Si falta el 8 % de una serie, ¿se puede rellenar sin contaminar el análisis? Depende de lo que se sepa de la señal: si es suave y se conoce su forma, el relleno es casi exacto; si es un evento breve que cayó en el hueco, no hay método que lo recupere.

📘 **Dónde se aprende** (1 clase): [B15-C19 · Reconstrucción por datos incompletos](../programa/clases/B15/B15-C19-reconstruccion-por-datos-incompletos/CLASE.md).

### Reconstructor modal

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C22](../programa/clases/B42/B42-C22-reconstructores-de-frente-de-onda-zonal-y-modal/CLASE.md):**
- *Descripción textual:* ambos reconstructores invierten el mismo operador de pendientes; el modal restringe la solución y propaga menos ruido pero trunca.
- python programa/clases/B42/B42-C22-reconstructores-de-frente-de-onda-zonal-y-modal/reconstructores.py
- 🎯 **Por qué importa:** El reconstructor decide qué parte del frente se recupera y cuánto ruido se propaga. La decisión central: ¿zonal o modal, y con cuántos modos?

📘 **Dónde se aprende** (1 clase): [B42-C22 · Reconstructores de frente de onda: zonal y modal](../programa/clases/B42/B42-C22-reconstructores-de-frente-de-onda-zonal-y-modal/CLASE.md).

### Reconstructor zonal

- El reconstructor zonal (un valor por nodo).

💡 **Cómo se explica en la clase [B42-C22](../programa/clases/B42/B42-C22-reconstructores-de-frente-de-onda-zonal-y-modal/CLASE.md):**
- python programa/clases/B42/B42-C22-reconstructores-de-frente-de-onda-zonal-y-modal/reconstructores.py
- 🎯 **Por qué importa:** El reconstructor decide qué parte del frente se recupera y cuánto ruido se propaga. La decisión central: ¿zonal o modal, y con cuántos modos?

📘 **Dónde se aprende** (1 clase): [B42-C22 · Reconstructores de frente de onda: zonal y modal](../programa/clases/B42/B42-C22-reconstructores-de-frente-de-onda-zonal-y-modal/CLASE.md).

### Reconstruido

- Un dato reconstruido nunca es un dato medido: debe marcarse con una bandera.

💡 **Cómo se explica en la clase [B15-C19](../programa/clases/B15/B15-C19-reconstruccion-por-datos-incompletos/CLASE.md):**
- Por eso lo reconstruido se marca, no se usa como si fuera independiente y se analiza el efecto de rellenar en el resultado final.
- *Descripción textual:* según lo que se sepa de la señal se elige interpolación, ajuste de modelo o extrapolación de banda limitada; el resultado se verifica con una simulación de hueco conocido y con los residuos en los puntos medidos, y lo reconstruido se marca.
- ⚠️ **Error frecuente:** No marcar lo reconstruido. Sección 8.7.
- 🎯 **Por qué importa:** Si falta el 8 % de una serie, ¿se puede rellenar sin contaminar el análisis? Depende de lo que se sepa de la señal: si es suave y se conoce su forma, el relleno es casi exacto; si es un evento breve que cayó en el hueco, no hay método que lo recupere.

📘 **Dónde se aprende** (1 clase): [B15-C19 · Reconstrucción por datos incompletos](../programa/clases/B15/B15-C19-reconstruccion-por-datos-incompletos/CLASE.md).

### Recorrido libre medio

- El recorrido libre medio `ℓ` es la distancia media que recorre un fotón entre interacciones;

💡 **Cómo se explica en la clase [B24-C05](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md):**
- Con un recorrido libre medio ilustrativo de `1 cm` (el real varía mucho con la profundidad;
- 🎯 **Por qué importa:** La energía generada en el núcleo tarda milenios en salir y el modo de transporte decide la estructura: si el interior de una estrella es convectivo, su composición se mezcla; si es radiativo, no. De ello depende cuánto combustible alcanza el núcleo, y por tanto la vida de la estrella.

📘 **Dónde se aprende** (1 clase): [B24-C05 · Transporte radiativo y convectivo](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md).

### Recorridos

- Los recorridos son las rutas que sigue la tripulación.

💡 **Cómo se explica en la clase [B109-C02](../programa/clases/B109/B109-C02-zonificacion-y-distribucion-funcional-de-modulos-de-un-habitat/CLASE.md):**
- La evidencia es tu plano de zonas con su coste de recorridos del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Un buen plano ahorra pasos, separa lo sucio de lo limpio y deja las zonas tranquilas lejos de las ruidosas. La decisión central: ¿dónde pongo cada zona para que los recorridos frecuentes sean cortos y las zonas incompatibles estén lejos?

📘 **Dónde se aprende** (1 clase): [B109-C02 · Zonificación y distribución funcional de módulos de un hábitat](../programa/clases/B109/B109-C02-zonificacion-y-distribucion-funcional-de-modulos-de-un-habitat/CLASE.md).

### Recorte

- El recorte (*clipping*) lleva a 0 o 1 lo que está fuera de los límites.

🎯 **Por qué importa (clase B15-C10):** Tienes una imagen con un cielo de 50 ADU, una estructura difusa tenue 15 ADU por encima y una estrella de 9000 ADU. Si la muestras con una escala lineal entre mínimo y máximo, el cielo y la estructura quedan en los niveles de gris 1 y 2 de 255: parece una pantalla negra con un punto.

📘 **Dónde se aprende** (1 clase): [B15-C10 · Histogramas y normalización](../programa/clases/B15/B15-C10-histogramas-y-normalizacion/CLASE.md).

### Recorte a 3σ

- El recorte a 3σ descarta residuos grandes.

💡 **Cómo se explica en la clase [B45-C21](../programa/clases/B45/B45-C21-estandares-fotometricos-y-sistemas-de-referencia/CLASE.md):**
- El recorte a 3σ descarta 2 estrellas (3, 17) y da `zp = -3,2057`, `c = 0,0489`.
- recorte a 3 sigma: descarta 2 estrellas [3, 17] ; zp = -3.2057, c = 0.0489, sigma residual 0.0136
- 🎯 **Por qué importa:** Sin estándares la escala de un cielo concreto es arbitraria. La decisión central: ¿qué ecuación de transformación se ajusta y con qué error en la magnitud final?

📘 **Dónde se aprende** (1 clase): [B45-C21 · Estándares fotométricos y sistemas de referencia](../programa/clases/B45/B45-C21-estandares-fotometricos-y-sistemas-de-referencia/CLASE.md).

### Recorte asimétrico

- El recorte asimétrico descarta puntos bajo el ajuste.

💡 **Cómo se explica en la clase [B32-C10](../programa/clases/B32/B32-C10-normalizacion-y-modelado-del-continuo-espectral/CLASE.md):**
- El recorte asimétrico elimina las líneas; el error residual (0,9 %) está en los extremos del intervalo.
- Ejercicio 6. ¿Por qué recorte asimétrico?
- 🎯 **Por qué importa:** Un continuo mal puesto sesga los anchos equivalentes. La decisión central: ¿cómo estimar el continuo ignorando las líneas?

📘 **Dónde se aprende** (1 clase): [B32-C10 · Normalización y modelado del continuo espectral](../programa/clases/B32/B32-C10-normalizacion-y-modelado-del-continuo-espectral/CLASE.md).

### Recorte (clamping)

- Log-odds: `L = ln(p/(1−p))`; la actualización es una suma (F5). Recorte (clamping): límites `l_min`, `l_max` que mantienen la capacidad de cambiar de opinión (F5).

💡 **Cómo se explica en la clase [B99-C05](../programa/clases/B99/B99-C05-mapas-de-ocupacion-y-rejillas-de-elevacion/CLASE.md):**
- Para que el mapa se adapte a cambios proponen una política de recorte que limita `L` entre `l_min` y `l_max`.
- Sin recorte, tras 20 golpes `L = 16,9` y harían falta 42 pasos libres para volver a `L = 0`; con recorte `L = 3,5` y bastan 9.
- 🎯 **Por qué importa:** Un mapa útil para navegar distingue lo ocupado, lo libre y lo que no se sabe, y dice si el terreno es pisable. La decisión central: ¿cómo fusionar medidas ruidosas en cada celda y qué umbrales de pendiente y rugosidad declaran un terreno traversable?

📘 **Dónde se aprende** (1 clase): [B99-C05 · Mapas de ocupación y rejillas de elevación](../programa/clases/B99/B99-C05-mapas-de-ocupacion-y-rejillas-de-elevacion/CLASE.md).

### Recorte iterativo

- El recorte iterativo (*sigma clipping*) estima fondo y ruido descartando valores muy alejados.

💡 **Cómo se explica en la clase [B15-C12](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md):**
- Con recorte iterativo a 3σ, la media baja a 100,53 y la desviación a 5,21.
- El script [deteccion.py](deteccion.py) comprueba que el ruido filtrado mide `σ √Σp²`, que la tasa de falsos píxeles coincide con `Q(k)`, que la completitud coincide con `Φ(SNR − k)` para cinco niveles de SNR (4000 intentos por nivel) y que el recorte iterativo acerca el fondo al valor real mejor que la media o la mediana.
- 🎯 **Por qué importa:** Un catálogo de fuentes es el producto básico de una imagen astronómica, y de él salen cuentas, colores y candidatos a objetos nuevos. Si el umbral es bajo, el catálogo se llena de ruido; si es alto, se pierden las fuentes débiles.

📘 **Dónde se aprende** (1 clase): [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md).

### Recta

- Una recta es `y = mx + b`.

💡 **Cómo se explica en la clase [B03-C16](../programa/clases/B03/B03-C16-pendiente-e-interpretacion-de-graficos/CLASE.md):**
- Si los puntos no caen exactamente sobre una recta, se busca la que mejor los representa.
- Si `T = a^p`, entonces `log T = p · log a`: una recta con pendiente `p` y ordenada 0.
- 🎯 **Por qué importa:** Si sitúas en un gráfico logarítmico el período frente al semieje de los planetas, los puntos forman una recta. Su pendiente es 1,5: ese número es el exponente de la tercera ley de Kepler.

📘 **Dónde se aprende** (1 clase): [B03-C16 · Pendiente e interpretación de gráficos](../programa/clases/B03/B03-C16-pendiente-e-interpretacion-de-graficos/CLASE.md).

### Recta de Bouguer

- Coeficiente `k`: mag por masa de aire. Recta de Bouguer: `m = m₀ + kX`.

🎯 **Por qué importa (clase B48-C05):** Sin conocer la extinción, las magnitudes de distintas noches no se comparan. La decisión central: ¿qué extinción y qué incertidumbre tiene una serie de medidas?

📘 **Dónde se aprende** (1 clase): [B48-C05 · Ventanas atmosféricas](../programa/clases/B48/B48-C05-ventanas-atmosfericas/CLASE.md).

### Recta numérica

- La recta numérica ordena los números de izquierda (menores) a derecha (mayores).

🎯 **Por qué importa (clase B03-C09):** Cuando observas una llamarada solar a las 12:00:00, el evento ocurrió antes: su tiempo es el observado menos 499 s. Si sumas en vez de restar, afirmas que la llamarada ocurre en el futuro.

📘 **Dónde se aprende** (1 clase): [B03-C09 · Operaciones con números negativos](../programa/clases/B03/B03-C09-operaciones-con-numeros-negativos/CLASE.md).

### Recta tangente

- La recta tangente en `x₀` es la que pasa por `(x₀, f(x₀))` con pendiente `f′(x₀)`.

💡 **Cómo se explica en la clase [B09-C03](../programa/clases/B09/B09-C03-derivada-como-tasa-de-cambio/CLASE.md):**
- La recta tangente en `t₀ = 4 s` es `h ≈ 321,613 + 60,806 (t − 4)`.
- Interpretar la derivada como pendiente de la tangente y escribir la recta tangente.
- 🎯 **Por qué importa:** Casi toda cantidad en ciencias espaciales cambia con el tiempo o la posición: la altura de un cohete, la fase de una estrella variable, el brillo de un cometa. Lo que se quiere saber suele ser con qué rapidez cambia, y en qué instante deja de crecer.

📘 **Dónde se aprende** (1 clase): [B09-C03 · Derivada como tasa de cambio](../programa/clases/B09/B09-C03-derivada-como-tasa-de-cambio/CLASE.md).

### Rectificación síncrona

- La rectificación síncrona sustituye el diodo por un MOSFET.

💡 **Cómo se explica en la clase [B86-C09](../programa/clases/B86/B86-C09-electronica-de-potencia/CLASE.md):**
- La rectificación síncrona ahorra `0,541 W`: el diodo disipaba `0,4 V × I` durante `1 − D` del periodo.
- El reductor sintético de la clase anterior pierde `0,959 W` con diodo y `0,419 W` con rectificación síncrona a `200 kHz`: `91,2 %` y `96,0 %` de eficiencia.
- 🎯 **Por qué importa:** La eficiencia no se mejora subiendo o bajando la frecuencia sin más: las pérdidas de conmutación crecen con ella y las de rizado decrecen. La temperatura de unión marca además el límite de fiabilidad del componente.

📘 **Dónde se aprende** (1 clase): [B86-C09 · Electrónica de potencia](../programa/clases/B86/B86-C09-electronica-de-potencia/CLASE.md).

### Recubrimiento en V

- El recubrimiento en V de dos capas.

💡 **Cómo se explica en la clase [B43-C24](../programa/clases/B43/B43-C24-recubrimientos-antirreflectantes-de-capas-multiples/CLASE.md):**
- El recubrimiento de dos capas es excelente en 550 nm pero en 450 nm es peor que una capa (`0,02025` frente a `0,01620`).
- La evidencia es la ficha de recubrimiento antirreflectante del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Cada reflexión sin tratar pierde luz y añade luz parásita. La decisión central: ¿cuántas capas y con qué índices y espesores se logra baja reflectancia en la banda visible?

📘 **Dónde se aprende** (1 clase): [B43-C24 · Recubrimientos antirreflectantes de capas múltiples](../programa/clases/B43/B43-C24-recubrimientos-antirreflectantes-de-capas-multiples/CLASE.md).

### Recuento acumulado

- El recuento acumulado `N(>E)`.

💡 **Cómo se explica en la clase [B29-C15](../programa/clases/B29/B29-C15-eventos-eruptivos-estelares/CLASE.md):**
- Calcular el recuento acumulado y la fracción de energía en la cola.
- Ejercicio 4. Factor entre los recuentos acumulados de dos décadas.
- 🎯 **Por qué importa:** La distribución de energías de las llamaradas determina cuánta energía total reciben los planetas cercanos. Estimar su índice con poco sesgo exige usar el estimador correcto.

📘 **Dónde se aprende** (1 clase): [B29-C15 · Eventos eruptivos estelares](../programa/clases/B29/B29-C15-eventos-eruptivos-estelares/CLASE.md).

### Recuperación

- La recuperación `r` es la fracción de la alimentación que sale como destilado.
- La recuperación es el retorno de una función a su valor previo.
- La recuperación `r` es la fracción de la carga que se disipa cada día.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B54-C18](../programa/clases/B54/B54-C18-medicion-remota-atmosferica/CLASE.md):**
- Interpretar la dispersión de la recuperación con ruido.
- Ejercicio 11 · transferencia. Transferencia. ¿Por qué repetir cinco veces la recuperación?
- 🎯 **Por qué importa:** Cada canal 've' una capa distinta según su absorción. La pregunta motivadora: ¿a qué altura 'mira' cada canal y cómo se recupera la altura de escala con ruido?

📘 **Dónde se aprende** (8 clases): [B54-C18 · Medición remota atmosférica](../programa/clases/B54/B54-C18-medicion-remota-atmosferica/CLASE.md); [B59-C07 · Purificación de agua](../programa/clases/B59/B59-C07-purificacion-de-agua/CLASE.md); [B88-C35 · Reinicio en caliente y persistencia de estado](../programa/clases/B88/B88-C35-reinicio-en-caliente-y-persistencia-de-estado/CLASE.md); [B90-C02 · Buenas prácticas de sala limpia](../programa/clases/B90/B90-C02-buenas-practicas-de-sala-limpia/CLASE.md); [B107-C06 · Estimación y modelado de la recuperación posterior al vuelo](../programa/clases/B107/B107-C06-estimacion-y-modelado-de-la-recuperacion-posterior-al-vuelo/CLASE.md); [B113-C01 · Estrés operacional y estrategias de afrontamiento](../programa/clases/B113/B113-C01-estres-operacional-y-estrategias-de-afrontamiento/CLASE.md) y 2 más.

### Recuperación de gas

- La recuperación de gas (*airsave*) bombea el gas a un depósito antes de ventear.

💡 **Cómo se explica en la clase [B109-C03](../programa/clases/B109/B109-C03-accesos-esclusas-y-transferencia-entre-ambientes-presurizados/CLASE.md):**
- Con recuperación `η = 0,90`, la pérdida neta por ciclo es `m(1 − η)`: `0,883 kg` (13 m³) o `1,018 kg` (15 m³).
- Con `2` EVA por semana (`104` ciclos al año, Stromgren et al.) el consumo sin recuperar es `917,9` y `1059,1 kg/año`; con recuperación, `91,8` y `105,9 kg/año`.
- ⚠️ **Error frecuente:** Creer que la recuperación elimina la pérdida. Se corrige con 8.2.
- 🎯 **Por qué importa:** Un asentamiento con salidas frecuentes pierde aire en cada ciclo. La decisión central: ¿cuánto gas hay que reponer al año y qué ganas recuperándolo?

📘 **Dónde se aprende** (1 clase): [B109-C03 · Accesos, esclusas y transferencia entre ambientes presurizados](../programa/clases/B109/B109-C03-accesos-esclusas-y-transferencia-entre-ambientes-presurizados/CLASE.md).

### Recuperación exponencial

- La recuperación exponencial `D(t) = L e^{−kt}`.

💡 **Cómo se explica en la clase [B105-C17](../programa/clases/B105/B105-C17-rehabilitacion-posterior-al-vuelo/CLASE.md):**
- Límite: la recuperación humana no siempre es exponencial ni llega a la asíntota supuesta.
- 🎯 **Por qué importa:** Prometer una fecha de recuperación sin su incertidumbre es engañoso: unas pocas mediciones ruidosas dan intervalos amplios. La decisión central: ¿cuánto tarda en recuperarse el 95 % y con qué incertidumbre, y cómo cambia para una persona lenta?

📘 **Dónde se aprende** (1 clase): [B105-C17 · Rehabilitación posterior al vuelo](../programa/clases/B105/B105-C17-rehabilitacion-posterior-al-vuelo/CLASE.md).

### Recuperación global

- La recuperación global `ρ` es el producto de las eficiencias de las etapas.

💡 **Cómo se explica en la clase [B59-C15](../programa/clases/B59/B59-C15-ciclo-cerrado-de-materiales/CLASE.md):**
- La recuperación global es `0,87318`; la reposición de régimen, `3,17 kg/día`.
- Calcular la recuperación global como producto de las etapas.
- 🎯 **Por qué importa:** Cerrar el 87 % de un lazo no deja una reposición del 13 % sino una dependencia permanente del 13 %. La decisión central: ¿qué etapa del lazo conviene mejorar para reducir más la reposición?

📘 **Dónde se aprende** (1 clase): [B59-C15 · Ciclo cerrado de materiales](../programa/clases/B59/B59-C15-ciclo-cerrado-de-materiales/CLASE.md).

### Recuperación r

- Recuperación `r`: fracción de agua reutilizada.

💡 **Cómo se explica en la clase [B106-C06](../programa/clases/B106/B106-C06-reciclaje-de-agua/CLASE.md):**
- Si la primera etapa recupera 0,75 y la salmuera pasa a otra que recupera 0,65, `r = 0,75 + 0,25·0,65 = 0,9125`.
- Con recuperación de 0,9 (cifra consultada para la ISS) se reponen 4,0 kg/día; en 180 días el total (agua más sistema ilustrativo) baja de 7200 kg sin reciclar a 2640 kg, y en 900 días de 36000 a 5520 kg.
- ⚠️ **Error frecuente:** Sumar recuperaciones de etapas. Usa `r₁ + (1 − r₁) r₂` (8.3).
- 🎯 **Por qué importa:** Lanzar agua cuesta masa; reciclarla cuesta hardware, energía y repuestos. La decisión central: ¿a partir de qué duración y con qué fracción de recuperación conviene cerrar el lazo del agua?

📘 **Dónde se aprende** (1 clase): [B106-C06 · Reciclaje de agua](../programa/clases/B106/B106-C06-reciclaje-de-agua/CLASE.md).

### Recuperación ε

- UFC: unidad formadora de colonia. Recuperación `ε`: fracción detectada.

💡 **Cómo se explica en la clase [B106-C28](../programa/clases/B106/B106-C28-monitoreo-microbiologico-de-agua-y-superficies-del-habitat/CLASE.md):**
- C["concentracion c"] --> M["muestra v, recuperacion eps"]
- *Descripción textual:* la probabilidad de detección depende del volumen y de la recuperación; el crecimiento fija cuánto puede esperarse entre muestreos.
- ⚠️ **Error frecuente:** Ignorar la recuperación. Ver 8.2.
- 🎯 **Por qué importa:** Una muestra pequeña puede no contener ningún organismo de una contaminación real, y un muestreo espaciado deja crecer la población. La decisión central: ¿qué volumen y qué intervalo de muestreo dan una confianza dada de detectar una contaminación antes de que supere el umbral de acción?

📘 **Dónde se aprende** (1 clase): [B106-C28 · Monitoreo microbiológico de agua y superficies del hábitat](../programa/clases/B106/B106-C28-monitoreo-microbiologico-de-agua-y-superficies-del-habitat/CLASE.md).

### Recurrencia

- La recurrencia repite el valor de hace un periodo.

💡 **Cómo se explica en la clase [B33-C11](../programa/clases/B33/B33-C11-modelos-empiricos-y-de-persistencia-en-clima-espacial/CLASE.md):**
- A 1 día la persistencia explica el 58 %; a 27 días la recurrencia apenas supera a la climatología.
- En 3000 días sintéticos, la persistencia a 1 día tiene `MSSS = 0,580` y la recurrencia a 27 días `0,050`; la persistencia a 14 días es peor que la climatología (`−2,05`).
- 🎯 **Por qué importa:** Un modelo complejo debe superar a la persistencia. La decisión central: ¿qué desfase da el mejor pronóstico simple?

📘 **Dónde se aprende** (1 clase): [B33-C11 · Modelos empíricos y de persistencia en clima espacial](../programa/clases/B33/B33-C11-modelos-empiricos-y-de-persistencia-en-clima-espacial/CLASE.md).

### Recursión

- El ordenamiento por mezcla divide la lista en dos, ordena cada mitad y las mezcla (se escribe con recursión: una función que se llama a sí misma con un problema menor).

🎯 **Por qué importa (clase B07-C18):** Un catálogo estelar tiene millones de objetos. Buscar uno a uno es posible con diez planetas y ruinoso con diez millones.

📘 **Dónde se aprende** (1 clase): [B07-C18 · Algoritmos de búsqueda y ordenamiento](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md).

### Recursión de Lindley

- Espera en cola `W_q`. Recursión de Lindley: `W_{n+1} = máx(0, W_n + S − A)`.

💡 **Cómo se explica en la clase [B48-C16](../programa/clases/B48/B48-C16-procesamiento-de-datos-en-linea/CLASE.md):**
- *Descripción textual:* la ocupación determina la espera de la cola: pequeña con carga baja, divergente cerca de uno; la recursión de Lindley la verifica.
- Verificarla con la recursión de Lindley.
- 🎯 **Por qué importa:** Si la reducción no sigue el ritmo, se acumulan cuadros y el resultado llega tarde. La decisión central: ¿hasta qué ocupación del procesador es tolerable la espera?

📘 **Dónde se aprende** (1 clase): [B48-C16 · Procesamiento de datos en línea](../programa/clases/B48/B48-C16-procesamiento-de-datos-en-linea/CLASE.md).

### Recurso

- Un recurso es una entidad direccionable.
- Un recurso es una acumulación estimada con perspectiva razonable de extracción.

💡 **Cómo se explica en la clase [B14-C31](../programa/clases/B14/B14-C31-apis-de-servicios-de-datos/CLASE.md):**
- La técnica ahorra transferencia cuando el recurso no cambió.
- 🎯 **Por qué importa:** Tu catálogo de escenas tiene 250 000 ítems y un programa ajeno quiere recorrerlos. Si le entregas una lista de golpe, se cae; si cada petición repite lo que ya tiene, desperdicias ancho de banda; si cambia un parámetro y falla sin explicación, nadie sabe qué hizo mal.

📘 **Dónde se aprende** (2 clases): [B14-C31 · APIs de servicios de datos](../programa/clases/B14/B14-C31-apis-de-servicios-de-datos/CLASE.md); [B67-C04 · Estimación de reservas y categorías de recursos](../programa/clases/B67/B67-C04-estimacion-de-reservas-y-categorias-de-recursos/CLASE.md).

### Recurso educativo abierto

- Un recurso educativo abierto (REA) es material de enseñanza en el dominio público o con licencia abierta que permite acceder, reutilizar, adaptar y redistribuir.

🎯 **Por qué importa (clase B130-C06):** Cerrar un proyecto educativo implica publicarlo de forma abierta y verificable; no hay otra clase al respecto. La decisión central: ¿qué debe llevar el paquete para que alguien más lo encuentre, lo reutilice legalmente y detecte una alteración, y qué de eso no puedes comprobar tú solo?

📘 **Dónde se aprende** (1 clase): [B130-C06 · Publicación de un proyecto educativo](../programa/clases/B130/B130-C06-publicacion-de-un-proyecto-educativo/CLASE.md).

### Recurso limitado

- Un recurso limitado es uno cuya cantidad no crece con la demanda.

💡 **Cómo se explica en la clase [B120-C03](../programa/clases/B120/B120-C03-posiciones-orbitales-y-espectro-como-recursos-limitados/CLASE.md):**
- RECURSOS LIMITADOS: Art. 44 UIT y regimenes consultados en documentos UIT 2018/2021 (consulta 2026-11-11); paises, demandas y capacidades SINTETICOS.
- python programa/clases/B120/B120-C03-posiciones-orbitales-y-espectro-como-recursos-limitados/recursos.py
- 🎯 **Por qué importa:** Las posiciones orbitales y el espectro son recursos escasos con reglas de asignación y no están tratados como concepto jurídico. La decisión central: ¿cuánto recurso hay, quién lo obtiene bajo cada régimen y qué mide la desigualdad del reparto?

📘 **Dónde se aprende** (1 clase): [B120-C03 · Posiciones orbitales y espectro como recursos limitados](../programa/clases/B120/B120-C03-posiciones-orbitales-y-espectro-como-recursos-limitados/CLASE.md).

### Recurso limitante

- El recurso limitante es el que se agota primero.

💡 **Cómo se explica en la clase [B104-C20](../programa/clases/B104/B104-C20-mision-tripulada-simulada/CLASE.md):**
- Descripción larga: el éxito cae de 99,5 % a 52,3 % al pasar de 0,05 a 0,20 fallas por día; el agua es el recurso limitante.
- Ejercicio 12 · integrador. Elabora tu *informe de misión simulada con margen*: modelo, tabla de éxito por tasa de fallas, recurso limitante, verificación con Poisson, límites y qué es sintético, ilustrativo y consultado.
- ⚠️ **Error frecuente:** Ignorar el recurso limitante. Identifícalo (8.3).
- 🎯 **Por qué importa:** Cada margen parece suficiente por separado, pero las fallas consumen a la vez agua y tiempo. La decisión central: ¿hasta qué tasa de fallas mantiene la misión una probabilidad de éxito alta, y cuál recurso se agota primero?

📘 **Dónde se aprende** (1 clase): [B104-C20 · Misión tripulada simulada](../programa/clases/B104/B104-C20-mision-tripulada-simulada/CLASE.md).

### Red

- La red es el conjunto de sitios.
- La red de difracción de `N` rendijas.

💡 **Cómo se explica en la clase [B28-C16](../programa/clases/B28/B28-C16-redes-internacionales-de-alertas/CLASE.md):**
- *Descripción textual:* el tiempo sidéreo local y la ascensión recta dan el ángulo horario; con él, la altura; combinada con la noche local da la probabilidad por sitio, y la de la red se compara con la fórmula de independencia.
- Calcular la probabilidad por sitio y la de la red.
- 🎯 **Por qué importa:** La cobertura de una red depende de su distribución geográfica, no solo del número de telescopios. La decisión central: ¿qué probabilidad hay de que, al llegar una alerta, al menos un sitio de la red pueda observar la fuente?

📘 **Dónde se aprende** (2 clases): [B28-C16 · Redes internacionales de alertas](../programa/clases/B28/B28-C16-redes-internacionales-de-alertas/CLASE.md); [B42-C04 · Difracción de aperturas](../programa/clases/B42/B42-C04-difraccion-de-aperturas/CLASE.md).

### Red cósmica

- La red cósmica es la estructura de filamentos, paredes y nodos que rodea a los vacíos.

💡 **Cómo se explica en la clase [B25-C18](../programa/clases/B25/B25-C18-estructura-cosmica-a-gran-escala/CLASE.md):**
- Estadísticas de vacíos y filamentos: describen la red cósmica directamente.
- Definir red cósmica, vacío, función de correlación de dos puntos y catálogo aleatorio.
- 🎯 **Por qué importa:** Las galaxias no se reparten al azar: forman filamentos, paredes, cúmulos y vacíos, la llamada red cósmica. La forma en que se agrupan guarda información de la materia oscura y de la historia del universo.

📘 **Dónde se aprende** (1 clase): [B25-C18 · Estructura cósmica a gran escala](../programa/clases/B25/B25-C18-estructura-cosmica-a-gran-escala/CLASE.md).

### Red de precedencias

- La red de precedencias ordena las tareas según sus dependencias.

💡 **Cómo se explica en la clase [B108-C05](../programa/clases/B108/B108-C05-evaluacion-de-secuencias-y-lineas-de-tiempo-de-eva/CLASE.md):**
- Hallar la ruta crítica de una red de precedencias con dos tripulantes.
- 🎯 **Por qué importa:** Falta evaluar la secuencia de una EVA (tiempos, consumibles, márgenes) antes de ejecutarla. La decisión central: ¿cabe la secuencia en el tiempo y en los consumibles disponibles, con qué probabilidad y con qué margen?

📘 **Dónde se aprende** (1 clase): [B108-C05 · Evaluación de secuencias y líneas de tiempo de EVA](../programa/clases/B108/B108-C05-evaluacion-de-secuencias-y-lineas-de-tiempo-de-eva/CLASE.md).

### Red de una capa oculta

- Una red de una capa oculta con `H` neuronas es `N(t) = c + Σᵢ vᵢ tanh(wᵢ t + bᵢ)`, con parámetros `vᵢ`, `wᵢ`, `bᵢ` y `c`.

💡 **Cómo se explica en la clase [B17-C03](../programa/clases/B17/B17-C03-redes-neuronales-informadas-por-la-fisica-pinn/CLASE.md):**
- Calcular las derivadas de una red de una capa oculta con funciones `tanh` y verificarlas contra diferencias finitas.
- 🎯 **Por qué importa:** Un modelo ajustado solo a datos puede reproducir muy bien lo medido y decir disparates fuera de ese rango: no sabe que una cantidad decae, ni que una oscilación conserva su amplitud. Si ya conoces la ecuación que gobierna el fenómeno, dejarla fuera es desperdiciar información.

📘 **Dónde se aprende** (1 clase): [B17-C03 · Redes neuronales informadas por la física (PINN)](../programa/clases/B17/B17-C03-redes-neuronales-informadas-por-la-fisica-pinn/CLASE.md).

### Redondear

- Una cifra significativa es un dígito que aporta información sobre el valor; cuentan todos los dígitos desde el primero distinto de cero hasta el último que se ha medido o calculado con sentido (`0,00450` tiene 3). Redondear es reemplazar un número por otro con menos cifras; la regla usual es mirar la primera cifra descartada: si es 5 o más, se sube la anterior.

💡 **Cómo se explica en la clase [B03-C11](../programa/clases/B03/B03-C11-estimacion-y-redondeo-responsable/CLASE.md):**
- La guía de metrología sugiere reportar la incertidumbre con a lo sumo dos cifras significativas y redondear el valor para que sea coherente con ella; si `y = 10,057 62 Ω` con `u = 27 mΩ`, se escribe `10,058 Ω` (S2, 7.2.6).
- C --> D["Redondear al final según la calidad de los datos"]
- ⚠️ **Error frecuente:** Redondear antes de operar. Ejercicio 7.
- 🎯 **Por qué importa:** Si te piden el tiempo que tarda la luz del Sol en llegar a la Tierra y respondes «499,004783836 s», parece muy preciso, pero tus datos (1 au y `c`) son exactos; en cambio, si respondes lo mismo para la distancia a la Luna, que varía entre unos 357 000 y 407 000 km, esas cifras serían falsas.

📘 **Dónde se aprende** (1 clase): [B03-C11 · Estimación y redondeo responsable](../programa/clases/B03/B03-C11-estimacion-y-redondeo-responsable/CLASE.md).

### Redondeo al más cercano

- El redondeo al más cercano da un error relativo máximo `ε/2`.

🎯 **Por qué importa (clase B11-C25):** Un programa de ciencias espaciales hace miles de millones de operaciones. Si una resta pierde 16 cifras en una sola operación, el resultado completo es basura sin que el programa se detenga.

📘 **Dónde se aprende** (1 clase): [B11-C25 · Aritmética de punto flotante y errores de redondeo](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md).

### Redondez

- La redondez es el rango de los residuos radiales.

💡 **Cómo se explica en la clase [B84-C18](../programa/clases/B84/B84-C18-control-dimensional/CLASE.md):**
- La redondez (máx − mín de residuos) es `17,08 µm`.
- Calcular redondez y planitud de los residuos.
- 🎯 **Por qué importa:** Una pieza «dentro de tolerancia» con una medida que tiene 5 µm de incertidumbre en una tolerancia de 10 µm no está demostrada. La decisión central: ¿qué diámetro tiene el agujero, con qué incertidumbre y cuántos puntos hacen falta?

📘 **Dónde se aprende** (1 clase): [B84-C18 · Control dimensional](../programa/clases/B84/B84-C18-control-dimensional/CLASE.md).

### Reducción

- La reducción es la disminución del número de satélites autorizados al fallar un hito.
- Una reducción combina muchos valores en uno (una suma).
- La difusión (*broadcast*) copia un dato del proceso raíz a todos; el reparto (*scatter*) divide una colección de la raíz entre los procesos; la reunión (*gather*) hace lo contrario; la reducción (*reduce*) combina valores de todos con una operación (suma, máximo…) y la deja en la raíz, y `allreduce` la deja en todos.

💡 **Cómo se explica en la clase [B14-C15](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md):**
- La suma secuencial en `float32` tiene un error relativo de `1,03 × 10⁻⁵`; la reducción en árbol (por pares, como hacen los núcleos paralelos), `1,27 × 10⁻⁷`.
- Para reducciones largas, acumula en mayor precisión o usa árbol.
- 🎯 **Por qué importa:** Un equipo promete que su simulación irá «100 veces más rápido en GPU» y, al compararla con la de CPU, los resultados difieren en el séptimo dígito. ¿Error del código o característica de la máquina?

📘 **Dónde se aprende** (3 clases): [B14-C15 · Cálculo en GPU y limitaciones](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md); [B18-C02 · Paso de mensajes con MPI](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md); [B120-C05 · Riesgos de incumplimiento regulatorio](../programa/clases/B120/B120-C05-riesgos-de-incumplimiento-regulatorio/CLASE.md).

### Reducción con hidrógeno

- La reducción con hidrógeno quita el oxígeno del óxido y lo saca como agua.

🎯 **Por qué importa (clase B59-C23):** Producir un kilogramo de oxígeno genera toneladas de otras cosas. La decisión central: ¿qué masa de residuo o de subproducto aparece por cada kilogramo de producto?

📘 **Dónde se aprende** (1 clase): [B59-C23 · Subproductos y flujos residuales de procesos ISRU](../programa/clases/B59/B59-C23-subproductos-y-flujos-residuales-de-procesos-isru/CLASE.md).

### Reducción de biocarga

- Reducción de biocarga: disminución del número de microorganismos viables.

💡 **Cómo se explica en la clase [B90-C22](../programa/clases/B90/B90-C22-validacion-de-procesos-de-reduccion-de-biocarga/CLASE.md):**
- La página de protección planetaria de NASA (F5) menciona que, según lo que el hardware tolere, se usan reducción microbiana por calor seco, peróxido de hidrógeno en vapor y exposición a luz ultravioleta, que las superficies expuestas se limpian con alcohol y que, si la biocarga excede el límite, se vuelve a limpiar y a medir.
- python programa/clases/B90/B90-C22-validacion-de-procesos-de-reduccion-de-biocarga/reduccion_biocarga.py
- 🎯 **Por qué importa:** Cada hora de calor consume vida del hardware; poca exposición deja sobrevivientes. La decisión central: ¿cuánta exposición garantiza la reducción pedida con una probabilidad de sobreviviente aceptable, y cómo cambia con la temperatura?

📘 **Dónde se aprende** (1 clase): [B90-C22 · Validación de procesos de reducción de biocarga](../programa/clases/B90/B90-C22-validacion-de-procesos-de-reduccion-de-biocarga/CLASE.md).

### Reducción de orden

- La reducción de orden consiste en dar nombre a cada derivada intermedia como una variable nueva.

🎯 **Por qué importa (clase B11-C04):** Un programa que propaga una trayectoria no entiende `r″ = −GM r/|r|³`: entiende una función que recibe un estado y devuelve su derivada. Si escribes mal ese puente, ningún método, por bueno que sea, te salva.

📘 **Dónde se aprende** (1 clase): [B11-C04 · Sistemas de ecuaciones diferenciales](../programa/clases/B11/B11-C04-sistemas-de-ecuaciones-diferenciales/CLASE.md).

### Reducción en árbol

- Una reducción en árbol suma por pares, luego los resultados por pares, y así hasta uno.

💡 **Cómo se explica en la clase [B14-C15](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md):**
- La suma secuencial en `float32` tiene un error relativo de `1,03 × 10⁻⁵`; la reducción en árbol (por pares, como hacen los núcleos paralelos), `1,27 × 10⁻⁷`.
- Para reducciones largas, acumula en mayor precisión o usa árbol.
- 🎯 **Por qué importa:** Un equipo promete que su simulación irá «100 veces más rápido en GPU» y, al compararla con la de CPU, los resultados difieren en el séptimo dígito. ¿Error del código o característica de la máquina?

📘 **Dónde se aprende** (1 clase): [B14-C15 · Cálculo en GPU y limitaciones](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md).

### Reducción logarítmica

- La reducción logarítmica es `log₁₀(N₀/N)`.
- La reducción logarítmica `LRV` es `−log₁₀(penetración)`.
- Valor z: aumento de temperatura que divide D por 10. Reducción logarítmica: `log₁₀(N₀/N)`.

💡 **Cómo se explica en la clase [B56-C17](../programa/clases/B56/B56-C17-control-de-contaminacion-biologica/CLASE.md):**
- Definir carga biológica, espora (en el sentido de la política), valor D y reducción logarítmica.
- Ejercicio 2 · con una pista. ¿Cuántas reducciones logarítmicas requiere el caso anterior?
- 🎯 **Por qué importa:** Una nave que lleva microorganismos terrestres puede contaminar otro mundo y confundir una futura búsqueda de vida. La política fija límites cuantitativos.

📘 **Dónde se aprende** (3 clases): [B56-C17 · Control de contaminación biológica](../programa/clases/B56/B56-C17-control-de-contaminacion-biologica/CLASE.md); [B63-C05 · Contención de muestras extraterrestres: instalaciones y principios](../programa/clases/B63/B63-C05-contencion-de-muestras-extraterrestres-instalaciones-y-principios/CLASE.md); [B90-C22 · Validación de procesos de reducción de biocarga](../programa/clases/B90/B90-C22-validacion-de-procesos-de-reduccion-de-biocarga/CLASE.md).

### Reducción logarítmica (LR)

- La reducción logarítmica (LR) es cuántos órdenes de magnitud baja un tratamiento.

🎯 **Por qué importa (clase B115-C07):** Una contaminación en un circuito compartido afecta a todos los lotes a la vez. La decisión central: ¿con qué frecuencia se muestrea, qué se mide y qué barreras (desinfección, lavado, temperatura) hacen falta para que una contaminación se detecte antes de llegar a un nivel de acción?

📘 **Dónde se aprende** (1 clase): [B115-C07 · Bioseguridad e inocuidad alimentaria en hábitats](../programa/clases/B115/B115-C07-bioseguridad-e-inocuidad-alimentaria-en-habitats/CLASE.md).

### Reducción relativa

- La reducción relativa `R` multiplica la tasa de pérdida por `(1 − R)`.

💡 **Cómo se explica en la clase [B105-C16](../programa/clases/B105/B105-C16-contramedidas-de-ejercicio/CLASE.md):**
- Traducir una reducción relativa en pérdida ósea a 6 meses.
- 🎯 **Por qué importa:** Más ejercicio ayuda, pero con rendimientos decrecientes y con un costo de energía y tiempo. La decisión central: ¿qué parte de la pérdida se evita con una carga dada y cuánta energía extra exige?

📘 **Dónde se aprende** (1 clase): [B105-C16 · Contramedidas de ejercicio](../programa/clases/B105/B105-C16-contramedidas-de-ejercicio/CLASE.md).

### Reductor

- Un reductor y un barlow.

💡 **Cómo se explica en la clase [B41-C11](../programa/clases/B41/B41-C11-campo-visual-y-escala-de-placa/CLASE.md):**
- Un reductor ensancha el campo pero submuestrea (`1,42` píxeles por FWHM de seeing); un barlow sobremuestrea el seeing y no gana detalle real.
- Ejercicio 9 · transferencia. Transferencia. Con el reductor 0,63×, ¿cuántos píxeles por FWHM del seeing?
- 🎯 **Por qué importa:** Un sensor mal emparejado desperdicia resolución o campo. La decisión central: ¿qué focal y qué píxel dan el campo y el muestreo que busco?

📘 **Dónde se aprende** (1 clase): [B41-C11 · Campo visual y escala de placa](../programa/clases/B41/B41-C11-campo-visual-y-escala-de-placa/CLASE.md).

### Redundancia

- La carga visual es el número de elementos que compiten por la atención a la vez. Redundancia: transmitir un estado por más de un canal (color y texto).
- La redundancia es el número de observadores que ven a la vez.
- La redundancia (respaldo frío, `k` de `n`).
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B33-C09](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md):**
- Porque la causa común anula la redundancia.
- Ejercicio 12. Integrador. Elabora tu *ficha de la continuidad*: redundancia, causa común y disponibilidad.
- 🎯 **Por qué importa:** Una unidad adicional mejora menos que la anterior y las fallas comunes limitan la ganancia. La decisión central: ¿cuántas unidades de respaldo valen la pena?

📖 **Explicado a fondo:** [Redundancia y fiabilidad](esencial/ampliacion-n-z.md#redundancia-y-fiabilidad) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (8 clases): [B33-C09 · Planes de continuidad ante eventos de clima espacial](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md); [B47-C19 · Mantenimiento y vida útil](../programa/clases/B47/B47-C19-mantenimiento-y-vida-util/CLASE.md); [B48-C15 · Gestión de fallas de instrumentos](../programa/clases/B48/B48-C15-gestion-de-fallas-de-instrumentos/CLASE.md); [B101-C02 · Cinemática inversa y redundancia de manipuladores](../programa/clases/B101/B101-C02-cinematica-inversa-y-redundancia-de-manipuladores/CLASE.md); [B116-C07 · Diseño de paneles de monitoreo de salud](../programa/clases/B116/B116-C07-diseno-de-paneles-de-monitoreo-de-salud/CLASE.md); [B118-C11 · Diseño para mitigación de desechos](../programa/clases/B118/B118-C11-diseno-para-mitigacion-de-desechos/CLASE.md) y 2 más.

### Redundancia activa

- La redundancia activa (caliente) y la fría (reserva) se diferencian en si la unidad extra funciona desde el principio.
- La redundancia activa mantiene dos unidades en marcha; la fría enciende la reserva al fallar la primera.

💡 **Cómo se explica en la clase [B93-C04](../programa/clases/B93/B93-C04-analisis-de-confiabilidad-de-electronica-mtbf-y-derating/CLASE.md):**
- Descripción larga: las piezas más débiles (circuitos digitales y conectores) dominan la suma; la redundancia convierte 5,8 % de riesgo en 0,3 % (activa) o 0,17 % (fría).
- Calcular la confiabilidad con redundancia activa y fría, y verificarla con Monte Carlo.
- 🎯 **Por qué importa:** Cuantificar la confiabilidad de la electrónica no estaba en el tronco. La decisión central: ¿qué tasa de fallas y qué MTBF tiene la suma de las piezas, qué probabilidad de supervivencia da para una misión, y cuánto la mejoran el derating y la redundancia?

📘 **Dónde se aprende** (2 clases): [B86-C11 · Redundancia eléctrica](../programa/clases/B86/B86-C11-redundancia-electrica/CLASE.md); [B93-C04 · Análisis de confiabilidad de electrónica (MTBF y derating)](../programa/clases/B93/B93-C04-analisis-de-confiabilidad-de-electronica-mtbf-y-derating/CLASE.md).

### Redundancia caliente

- La redundancia caliente tiene las unidades encendidas a la vez; la fría deja la reserva apagada y sin desgaste hasta conmutar.

💡 **Cómo se explica en la clase [B88-C01](../programa/clases/B88/B88-C01-arquitectura-de-computador-de-vuelo/CLASE.md):**
- Comparar redundancia caliente y fría con conmutación perfecta e imperfecta.
- 🎯 **Por qué importa:** Un computador de vuelo no se puede reparar en órbita, así que su arquitectura se decide con números antes de construirlo. La decisión central: ¿alcanzan la CPU y la memoria con margen, y qué redundancia compra qué fiabilidad?

📘 **Dónde se aprende** (1 clase): [B88-C01 · Arquitectura de computador de vuelo](../programa/clases/B88/B88-C01-arquitectura-de-computador-de-vuelo/CLASE.md).

### Redundancia fría

- Paralelo activo de dos: `2R − R²`. Redundancia fría con conmutador de confiabilidad `Rs`: `e^{−x}(1 + Rs·x)`.

💡 **Cómo se explica en la clase [B83-C23](../programa/clases/B83/B83-C23-redundancia-y-tolerancia-a-fallos-de-mision/CLASE.md):**
- Para una unidad sintética de 8000 FIT en una misión de 5 años (`x = λt = 0,3504`), la confiabilidad es 70,44 % sin redundancia, 91,26 % con paralelo activo, 94,63 % con redundancia fría (conmutador de 0,98) y 78,95 % con 2-de-3.
- Descripción larga: la redundancia fría es la más confiable cuando el conmutador es bueno; el 2-de-3 pesa tres veces y rinde menos que el paralelo para fallas de este tamaño.
- 🎯 **Por qué importa:** Duplicar todo es imposible por masa y a veces contraproducente; no duplicar nada deja una misión frágil. La decisión central: ¿qué unidades duplicar, con qué esquema y cuánta confiabilidad compra cada kilogramo?

📘 **Dónde se aprende** (1 clase): [B83-C23 · Redundancia y tolerancia a fallos de misión](../programa/clases/B83/B83-C23-redundancia-y-tolerancia-a-fallos-de-mision/CLASE.md).

### Redundancia k de n

- Tasa de falla `λ`: fallas por hora. Redundancia k de n: funciona si funcionan `k` de `n`.

💡 **Cómo se explica en la clase [B106-C18](../programa/clases/B106/B106-C18-fiabilidad-y-redundancia/CLASE.md):**
- *Descripción textual:* la tasa de falla da la fiabilidad de una unidad; la redundancia la mejora y la flota esperada de fallas fija los repuestos.
- Con redundancia 1 de 2 sube a 0,9623, con 1 de 3 a 0,9927, y con 2 de 3 (votación) baja a 0,9014.
- 🎯 **Por qué importa:** Ningún equipo es perfecto y una misión larga no se puede reparar con repuestos de la Tierra. La decisión central: ¿qué configuración redundante y cuántos repuestos dan una probabilidad objetivo de cumplir la misión?

📘 **Dónde se aprende** (1 clase): [B106-C18 · Fiabilidad y redundancia](../programa/clases/B106/B106-C18-fiabilidad-y-redundancia/CLASE.md).

### Reefing

- El reefing limita el área inicial.

💡 **Cómo se explica en la clase [B77-C18](../programa/clases/B77/B77-C18-aterrizaje-y-recuperacion/CLASE.md):**
- Con `Cx = 1,3` y área plena, `F = 2390 kN = 81 g`, excesivo; con la fracción de área de 15 % del reefing, `358 kN = 12,2 g`.
- *Descripción textual:* la atmósfera da la velocidad terminal y, con ella, el tiempo de descenso, la deriva y la velocidad de contacto; la presión dinámica de apertura y el reefing dan la carga; el empuje da la altura de encendido del aterrizaje propulsado.
- 🎯 **Por qué importa:** Un paracaídas grande da un aterrizaje suave pero una apertura brusca; un motor da control pero consume propelente. La decisión central: ¿qué velocidad de contacto, qué carga de apertura y qué altura de encendido resultan de cada opción?

📘 **Dónde se aprende** (1 clase): [B77-C18 · Aterrizaje y recuperación](../programa/clases/B77/B77-C18-aterrizaje-y-recuperacion/CLASE.md).

### Reemplazo por edad

- Weibull: distribución de vida con forma `β` y escala `η`. Reemplazo por edad: se cambia a las `T` horas o en la falla.

💡 **Cómo se explica en la clase [B48-C14](../programa/clases/B48/B48-C14-mantenimiento-preventivo/CLASE.md):**
- Escribir el costo por unidad de tiempo del reemplazo por edad.
- 🎯 **Por qué importa:** Reemplazar muy pronto desperdicia vida útil; muy tarde, produce fallas caras. La decisión central: ¿cada cuántas horas conviene reemplazar?

📘 **Dónde se aprende** (1 clase): [B48-C14 · Mantenimiento preventivo](../programa/clases/B48/B48-C14-mantenimiento-preventivo/CLASE.md).

### Reenvío

- Trozo: unidad de transferencia. Reenvío: nuevo intento de un trozo dañado.

💡 **Cómo se explica en la clase [B96-C22](../programa/clases/B96/B96-C22-transferencia-de-datos-entre-estacion-y-centro-de-datos/CLASE.md):**
- Descripción larga: la verificación por trozo convierte un daño silencioso en un reenvío; el costo en tiempo de las pérdidas es pequeño frente al plazo.
- Ejercicio 12 · integrador. Integrador. Elabora tu *plan de transferencia con plazo y verificación*: trozos y hashes, reenvíos, hash final, plazo esperado y lista de lo consultado, sintético y no consultado.
- 🎯 **Por qué importa:** Un dato dañado que se acepta sin verificar contamina los productos científicos; y una transferencia lenta rompe el plazo de entrega. La decisión central: ¿cómo se comprueba la integridad y cuánto tarda la transferencia con reintentos?

📘 **Dónde se aprende** (1 clase): [B96-C22 · Transferencia de datos entre estación y centro de datos](../programa/clases/B96/B96-C22-transferencia-de-datos-entre-estacion-y-centro-de-datos/CLASE.md).

### Reescalado

- El reescalado multiplica por `t₂/t₁`.

🎯 **Por qué importa (clase B44-C13):** La oscuridad depende de la exposición y de la temperatura, y algunos píxeles son muy calientes. La decisión central: ¿se puede reutilizar un dark de otra exposición, y a qué costo en ruido?

📘 **Dónde se aprende** (1 clase): [B44-C13 · Calibración con dark](../programa/clases/B44/B44-C13-calibracion-con-dark/CLASE.md).

### Referencia

- En un lazo cerrado, la referencia `r` es lo que se desea, la salida `y` lo que se tiene, el error `e = r − H y` su diferencia, `d` una perturbación y `n` el ruido de medida.
- La referencia es la clasificación de mayor calidad que se toma como verdad.
- Cadencia: ritmo del movimiento repetitivo. Referencia (*gold standard*): método considerado más exacto, aquí un ECG simulado.

💡 **Cómo se explica en la clase [B16-C06](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md):**
- El ruido de medida `n` llega a `θ` con la misma `T` que la referencia pero con signo contrario: el lazo sigue fielmente tanto la referencia como el ruido, por eso se filtra (C14).
- Entonces la función de la referencia a la salida es `Kp/(J s² + Kd s + Kp)`, sin el cero en `−Kp/Kd`, mientras el lazo tiene los mismos polos.
- ⚠️ **Error frecuente:** Derivar la referencia sin querer. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un sistema de control de actitud tiene sensores, un computador, ruedas y un cuerpo, todos conectados y, sobre todo, con la salida de vuelta a la entrada. Para entender qué hace el conjunto no basta conocer las partes: hay que saber cómo se combinan.

📘 **Dónde se aprende** (3 clases): [B16-C06 · Diagramas de bloques](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md); [B57-C33 · Deforestación y cambio de uso del suelo](../programa/clases/B57/B57-C33-deforestacion-y-cambio-de-uso-del-suelo/CLASE.md); [B116-C01 · Sensores fisiológicos y wearables para vuelo](../programa/clases/B116/B116-C01-sensores-fisiologicos-y-wearables-para-vuelo/CLASE.md).

### Referencia climatológica

- La referencia climatológica pronostica siempre la frecuencia base `ō`, con `BS_ref = ō(1 − ō)`.

💡 **Cómo se explica en la clase [B12-C24](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md):**
- Paso 2 · Brier. `BS = 0,0872`; referencia climatológica `0,0911`.
- 🎯 **Por qué importa:** Un pronóstico de «no habrá llamarada» acierta el 90 % de los días en una época tranquila y no sirve de nada. La exactitud bruta premia lo trivial.

📘 **Dónde se aprende** (1 clase): [B12-C24 · Métricas de habilidad (skill scores) de pronóstico](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md).

### Referencia de fase

- La referencia de fase alterna calibrador y blanco.

💡 **Cómo se explica en la clase [B46-C17](../programa/clases/B46/B46-C17-calibracion-de-fase/CLASE.md):**
- El script [fases.py](fases.py) comprueba el cierre, resuelve las fases y simula la referencia de fase (comprueba el cierre a 10⁻¹² y el residuo al 8 %).
- 🎯 **Por qué importa:** Sin calibrar, la fase de la visibilidad no contiene el cielo. La decisión central: ¿cada cuánto hay que observar el calibrador para que el residuo no destruya la coherencia?

📘 **Dónde se aprende** (1 clase): [B46-C17 · Calibración de fase](../programa/clases/B46/B46-C17-calibracion-de-fase/CLASE.md).

### Referencia exacta

- La referencia exacta es el resultado con aritmética racional.

💡 **Cómo se explica en la clase [B124-C14](../programa/clases/B124/B124-C14-ciencia-abierta-y-reproducibilidad/CLASE.md):**
- Los errores respecto de la referencia exacta son `8,57e-08`, `2,89e-07`, `2,62e-05` y `4,84e-08`.
- El ejemplo conductor es una suma de 100 000 números sintéticos: en cuatro órdenes distintos el resultado varía en `2,65e-05`, mientras `math.fsum` coincide con la referencia exacta; y un registro sintético cumple `8` de `12` criterios.
- 🎯 **Por qué importa:** «Es reproducible» suele afirmarse sin evidencia. La decisión central: ¿qué hay que fijar y registrar para que un análisis dé el mismo resultado y se pueda comprobar?

📘 **Dónde se aprende** (1 clase): [B124-C14 · Ciencia abierta y reproducibilidad](../programa/clases/B124/B124-C14-ciencia-abierta-y-reproducibilidad/CLASE.md).

### Referencia experta

- Una referencia experta es el conjunto de etiquetas contra el que se valida.

💡 **Cómo se explica en la clase [B129-C07](../programa/clases/B129/B129-C07-proyecto-de-ciencia-ciudadana-validable/CLASE.md):**
- *Descripción textual:* los objetos reciben `n` votos que se resumen por mayoría y se comparan con la referencia experta; la exactitud fija el número de votos y el plan se revisa contra la lista de la ECSA para armar el informe.
- Calcular la `κ` de Cohen entre el consenso ciudadano y la referencia experta.
- ⚠️ **Error frecuente:** Transferir el acuerdo de otro proyecto al propio. Valida con tu referencia experta (caso de contexto)
- 🎯 **Por qué importa:** Un proyecto ciudadano que produce datos sin validar es una anécdota; con validación es evidencia. La decisión central: ¿cuántos votos por objeto hacen falta, cómo se sabe que el resultado coincide con el de los expertos y qué le falta al plan para ser una ciencia ciudadana bien hecha?

📘 **Dónde se aprende** (1 clase): [B129-C07 · Proyecto de ciencia ciudadana validable](../programa/clases/B129/B129-C07-proyecto-de-ciencia-ciudadana-validable/CLASE.md).

### Referencia independiente

- Una referencia independiente es un dato o método distinto del que usaste para calcular.
- Una referencia independiente es un cálculo hecho con otro método (aquí, la solución de Kepler).
- Armado: habilitación explícita previa. Referencia independiente: otra implementación de la misma política.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C20](../programa/clases/B11/B11-C20-propagador-reproducible-de-trayectoria/CLASE.md):**
- Probar el programa contra una solución de referencia independiente (Kepler).
- 🎯 **Por qué importa:** Un resultado numérico que nadie puede reproducir no es ciencia. Si dentro de un año hay que saber por qué una trayectoria salió así, hacen falta la configuración exacta, las versiones del software y pruebas que digan si el programa sigue funcionando.

📘 **Dónde se aprende** (4 clases): [B07-C09 · Cálculos científicos básicos con Python](../programa/clases/B07/B07-C09-calculos-cientificos-basicos-con-python/CLASE.md); [B11-C20 · Propagador reproducible de trayectoria](../programa/clases/B11/B11-C20-propagador-reproducible-de-trayectoria/CLASE.md); [B96-C07 · Telecomandos y autorizaciones](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md); [B102-C03 · Deslizamiento y estimación de patinaje](../programa/clases/B102/B102-C03-deslizamiento-y-estimacion-de-patinaje/CLASE.md).

### Refinamiento sub-muestra

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B34-C09):** Combinar instrumentos mal alineados produce conclusiones falsas. La decisión central: ¿cómo se mide el retardo entre dos instrumentos con precisión sub-muestra?

📘 **Dónde se aprende** (1 clase): [B34-C09 · Integración multiinstrumento de datos heliofísicos](../programa/clases/B34/B34-C09-integracion-multiinstrumento-de-datos-heliofisicos/CLASE.md).

### Refinamiento subpixel

- El refinamiento subpíxel ajusta una parábola alrededor del pico.
- El refinamiento subpixel ajusta una parábola al coste alrededor del mínimo.

💡 **Cómo se explica en la clase [B103-C03](../programa/clases/B103/B103-C03-mapas-de-profundidad-y-correspondencia-estereo/CLASE.md):**
- *Descripción textual:* para cada disparidad candidata se calcula un coste en ventana; el mínimo (con refinamiento subpixel) da la disparidad, de ella sale la profundidad y su incertidumbre, y se mide el error por rango contra la verdad conocida.
- Calcular un mapa de disparidad con SAD en ventana, integral de imagen y refinamiento subpixel.
- 🎯 **Por qué importa:** La profundidad estéreo es barata y densa, pero su error crece con el cuadrado de la distancia: a 20 m una incertidumbre de 0,3 px en la disparidad son 71 cm. La decisión central: ¿hasta qué distancia se puede confiar en el mapa de profundidad para decidir si un camino es seguro, y qué línea de base lo permite?

📘 **Dónde se aprende** (2 clases): [B74-C26 · Navegación por hitos y correlación de terreno](../programa/clases/B74/B74-C26-navegacion-por-hitos-y-correlacion-de-terreno/CLASE.md); [B103-C03 · Mapas de profundidad y correspondencia estéreo](../programa/clases/B103/B103-C03-mapas-de-profundidad-y-correspondencia-estereo/CLASE.md).

### Reflectancia

- La reflectancia `ρ` es la fracción de la irradiancia que la superficie devuelve; una superficie lambertiana la devuelve igual en todas las direcciones, con `L = ρ E cos θ / π`.
- La reflectancia `R` y la transmitancia `T`.
- La reflectancia `R = ((n−1)²+k²)/((n+1)²+k²)`.

💡 **Cómo se explica en la clase [B41-C02](../programa/clases/B41/B41-C02-indice-de-refraccion-y-ley-de-snell/CLASE.md):**
- De vidrio a aire el ángulo crítico es `41,2536°`: a `41,1963°` la reflectancia es `0,84580` (s) y `0,67968` (p); a `41,3109°` hay reflexión total (`1,00000`).
- Para aire (`1,0003`) a vidrio (`1,517`), la reflectancia en incidencia normal es `0,042132`, el ángulo de Brewster es `56,5994°` (donde `Rp = 0`) y de vidrio a aire el ángulo crítico es `41,2536°`.
- 🎯 **Por qué importa:** Un telescopio refractor y los recubrimientos dependen de cuánta luz se refleja y a qué ángulo se dobla. La decisión central: ¿qué fracción de luz se pierde por reflexión y cuándo hay reflexión total?

📘 **Dónde se aprende** (4 clases): [B41-C02 · Índice de refracción y ley de Snell](../programa/clases/B41/B41-C02-indice-de-refraccion-y-ley-de-snell/CLASE.md); [B43-C07 · Aluminizado y recubrimientos](../programa/clases/B43/B43-C07-aluminizado-y-recubrimientos/CLASE.md); [B47-C12 · Óptica en ambientes de vacío](../programa/clases/B47/B47-C12-optica-en-ambientes-de-vacio/CLASE.md); [B57-C01 · Fundamentos de teledetección](../programa/clases/B57/B57-C01-fundamentos-de-teledeteccion/CLASE.md).

### Reflectancia de Fresnel

- La reflectancia de Fresnel es la fracción de potencia reflejada en una interfaz.

💡 **Cómo se explica en la clase [B50-C05](../programa/clases/B50/B50-C05-luz-parasita-y-analisis-de-rayos-dispersos/CLASE.md):**
- Calcular la reflectancia de Fresnel a incidencia normal.
- 🎯 **Por qué importa:** El contraste de un instrumento no depende solo de la imagen: depende de cuánta luz llega por caminos no deseados. La decisión central: ¿qué fracción de luz llega por un camino parásito y cómo se reduce?

📘 **Dónde se aprende** (1 clase): [B50-C05 · Luz parásita y análisis de rayos dispersos](../programa/clases/B50/B50-C05-luz-parasita-y-analisis-de-rayos-dispersos/CLASE.md).

### Reflectancia de trayectoria

- La reflectancia de trayectoria `ρ_p` es la luz dispersada por la atmósfera hacia el sensor sin tocar la superficie.

💡 **Cómo se explica en la clase [B57-C26](../programa/clases/B57/B57-C26-correccion-atmosferica-de-imagenes/CLASE.md):**
- La transmitancia total del rojo es `T_d T_u = 0,4704` y la reflectancia de trayectoria `0,01920`: la neblina atmosférica aporta casi la mitad de la señal de una superficie oscura.
- Ejercicio 2 · con una pista. Si `ρ_p = 0,01` y `ρ_TOA = 0,05`, ¿qué reflectancia queda tras restar la trayectoria?
- 🎯 **Por qué importa:** Comparar imágenes de fechas distintas con atmósferas distintas confunde atmósfera con cambio. La decisión central: ¿cuánto sesga la atmósfera y cómo se estima y descuenta con la información disponible?

📘 **Dónde se aprende** (1 clase): [B57-C26 · Corrección atmosférica de imágenes](../programa/clases/B57/B57-C26-correccion-atmosferica-de-imagenes/CLASE.md).

### Reflectancia especular

- La reflectancia especular `R₀ e^(−TIS)`.

💡 **Cómo se explica en la clase [B43-C23](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md):**
- Calcular la reflectancia especular `R₀ e^(−TIS)`.
- 🎯 **Por qué importa:** La luz dispersa reduce el contraste y la reflectancia especular. La decisión central: ¿qué rugosidad RMS, en qué banda de frecuencias espaciales, deja la luz dispersa por debajo del presupuesto?

📘 **Dónde se aprende** (1 clase): [B43-C23 · Medición de rugosidad y su efecto en la luz dispersa](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md).

### Reflectancia mínima

- La reflectancia mínima `((n_s − n₁²)/(n_s + n₁²))²`.

💡 **Cómo se explica en la clase [B43-C24](../programa/clases/B43/B43-C24-recubrimientos-antirreflectantes-de-capas-multiples/CLASE.md):**
- Verificar la reflectancia mínima de una capa de cuarto de onda.
- 🎯 **Por qué importa:** Cada reflexión sin tratar pierde luz y añade luz parásita. La decisión central: ¿cuántas capas y con qué índices y espesores se logra baja reflectancia en la banda visible?

📘 **Dónde se aprende** (1 clase): [B43-C24 · Recubrimientos antirreflectantes de capas múltiples](../programa/clases/B43/B43-C24-recubrimientos-antirreflectantes-de-capas-multiples/CLASE.md).

### Reflectividad

- La reflectividad `ρ` es la fracción reflejada.

💡 **Cómo se explica en la clase [B78-C12](../programa/clases/B78/B78-C12-velas-solares/CLASE.md):**
- Para el caso de LightSail 2, la fuerza ideal de frente (`276 µN`) supera a la estimación de unos `100 µN` de un resultado de búsqueda: en órbita baja la vela no apunta siempre al Sol, hay sombra de la Tierra y la reflectividad real es menor.
- *Descripción textual:* la luminosidad y la distancia dan la irradiancia; con la reflectividad se obtiene la presión; la fuerza depende del área y del ángulo; la aceleración y el Δv diario siguen de la masa; el conteo de fotones verifica la presión.
- 🎯 **Por qué importa:** La vela no gasta propelente, pero su empuje es del orden de los micronewton por metro cuadrado y cae con el cuadrado de la distancia al Sol. La decisión central: ¿cuánta aceleración da una vela real y cómo depende de su orientación y de su distancia?

📘 **Dónde se aprende** (1 clase): [B78-C12 · Velas solares](../programa/clases/B78/B78-C12-velas-solares/CLASE.md).

### Reflectividad de Fresnel

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C05](../programa/clases/B47/B47-C05-instrumentos-de-rayos-x/CLASE.md):**
- Calcular la reflectividad de Fresnel sin absorción.
- 🎯 **Por qué importa:** La reflexión rasante limita la energía y el área útil. La decisión central: ¿cuántas conchas y qué ángulos dan el área efectiva que se necesita a cada energía?

📘 **Dónde se aprende** (1 clase): [B47-C05 · Instrumentos de rayos X](../programa/clases/B47/B47-C05-instrumentos-de-rayos-x/CLASE.md).

### Reflector

- Un refractor reúne la luz con lentes; un reflector usa espejos y puede necesitar ajustar sus espejos (*colimación*); un Dobson es un reflector sobre una montura simple (S3).

💡 **Cómo se explica en la clase [B08-C14](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md):**
- Según Night Sky Network (S3): los refractores usan lentes, necesitan poco mantenimiento y suelen ser más grandes y caros que un reflector de potencia similar; los reflectores usan espejos y pueden requerir colimación; los Dobson son reflectores sobre una montura sencilla, fáciles de sacar y usar, una elección común de principiantes.
- Para reflectores recomienda aperturas de 4,5 a 8 pulgadas (114 a 203 mm), un buen compromiso de calidad de imagen, costo, peso y tamaño.
- 🎯 **Por qué importa:** Un telescopio de juguete anuncia «600×» y decepciona. La pregunta motivadora: ¿qué telescopio me conviene y qué podré ver con él?

📘 **Dónde se aprende** (1 clase): [B08-C14 · Telescopios de iniciación](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md).

### Reflejo

- Un reflejo es un comportamiento reactivo de seguridad (parar, retirarse).

💡 **Cómo se explica en la clase [B98-C05](../programa/clases/B98/B98-C05-autonomia-de-bajo-nivel-y-comportamientos-reactivos/CLASE.md):**
- A esta velocidad el frenado es casi inmediato; el reflejo tiene un margen enorme frente a los 3 m del sensor.
- P -. "sin reflejo" .-> G["Tierra: 2 t + decision"]
- 🎯 **Por qué importa:** Ningún plan, por bueno que sea, protege a un vehículo del peligro que aparece entre dos ciclos de comunicación. La decisión central: ¿qué debe resolver el vehículo por sí mismo y a qué velocidad puede ir para que ese reflejo llegue a tiempo?

📘 **Dónde se aprende** (1 clase): [B98-C05 · Autonomía de bajo nivel y comportamientos reactivos](../programa/clases/B98/B98-C05-autonomia-de-bajo-nivel-y-comportamientos-reactivos/CLASE.md).

### Reflexión

- La reflexión devuelve la luz en la superficie con ángulo igual al de incidencia.
- La reflexión impide que una partícula salga de la superficie.

💡 **Cómo se explica en la clase [B05-C19](../programa/clases/B05/B05-C19-optica-y-velocidad-de-la-luz/CLASE.md):**
- Enunciar la ley de la reflexión y la ley de Snell de la refracción.
- Calcular ángulos de refracción y el ángulo crítico de reflexión total.
- 🎯 **Por qué importa:** Un telescopio espacial o una cámara en órbita baja distinguen detalles hasta cierto límite que no depende de la calidad de la electrónica, y la luz de un objeto lejano llega con retraso. La pregunta motivadora es: ¿qué determina cuán pequeño es el detalle que un instrumento óptico puede resolver y cuánto tarda la luz en llegar?

📘 **Dónde se aprende** (2 clases): [B05-C19 · Óptica y velocidad de la luz](../programa/clases/B05/B05-C19-optica-y-velocidad-de-la-luz/CLASE.md); [B53-C22 · Meteorización espacial: micrometeoritos, viento solar y maduración del regolito](../programa/clases/B53/B53-C22-meteorizacion-espacial-micrometeoritos-viento-solar-y-maduracion-del-regolito/CLASE.md).

### Reflexión rasante

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C05):** La reflexión rasante limita la energía y el área útil. La decisión central: ¿cuántas conchas y qué ángulos dan el área efectiva que se necesita a cada energía?

📘 **Dónde se aprende** (1 clase): [B47-C05 · Instrumentos de rayos X](../programa/clases/B47/B47-C05-instrumentos-de-rayos-x/CLASE.md).

### Reflexión total

- La reflexión total ocurre al pasar a un medio de menor índice con un ángulo mayor que el ángulo crítico `arcsen(n₂/n₁)`.

💡 **Cómo se explica en la clase [B05-C19](../programa/clases/B05/B05-C19-optica-y-velocidad-de-la-luz/CLASE.md):**
- Calcular ángulos de refracción y el ángulo crítico de reflexión total.
- 🎯 **Por qué importa:** Un telescopio espacial o una cámara en órbita baja distinguen detalles hasta cierto límite que no depende de la calidad de la electrónica, y la luz de un objeto lejano llega con retraso. La pregunta motivadora es: ¿qué determina cuán pequeño es el detalle que un instrumento óptico puede resolver y cuánto tarda la luz en llegar?

📘 **Dónde se aprende** (1 clase): [B05-C19 · Óptica y velocidad de la luz](../programa/clases/B05/B05-C19-optica-y-velocidad-de-la-luz/CLASE.md).

### Reflexión total interna

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C02):** Un telescopio refractor y los recubrimientos dependen de cuánta luz se refleja y a qué ángulo se dobla. La decisión central: ¿qué fracción de luz se pierde por reflexión y cuándo hay reflexión total?

📘 **Dónde se aprende** (1 clase): [B41-C02 · Índice de refracción y ley de Snell](../programa/clases/B41/B41-C02-indice-de-refraccion-y-ley-de-snell/CLASE.md).

### Refracción

- La refracción es la desviación de la luz por la atmósfera, que eleva los astros cerca del horizonte.
- La refracción cambia su dirección al pasar de un medio a otro, según la ley de Snell `n₁ sen θ₁ = n₂ sen θ₂` (ángulos medidos respecto de la normal).
- La refracción curva la luz en la atmósfera y eleva el objeto aparente; aquí `R ≈ 58,3″ · tan z`.

💡 **Cómo se explica en la clase [B05-C19](../programa/clases/B05/B05-C19-optica-y-velocidad-de-la-luz/CLASE.md):**
- Enunciar la ley de la reflexión y la ley de Snell de la refracción.
- Calcular ángulos de refracción y el ángulo crítico de reflexión total.
- 🎯 **Por qué importa:** Un telescopio espacial o una cámara en órbita baja distinguen detalles hasta cierto límite que no depende de la calidad de la electrónica, y la luz de un objeto lejano llega con retraso. La pregunta motivadora es: ¿qué determina cuán pequeño es el detalle que un instrumento óptico puede resolver y cuánto tarda la luz en llegar?

📘 **Dónde se aprende** (3 clases): [B05-C19 · Óptica y velocidad de la luz](../programa/clases/B05/B05-C19-optica-y-velocidad-de-la-luz/CLASE.md); [B08-C04 · Altura y acimut](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md); [B132-C02 · Arqueología de observatorios y de instrumentos antiguos](../programa/clases/B132/B132-C02-arqueologia-de-observatorios-y-de-instrumentos-antiguos/CLASE.md).

### Refracción atmosférica

- La refracción atmosférica es la desviación de la luz al atravesar la atmósfera, que eleva aparentemente los astros cerca del horizonte.

💡 **Cómo se explica en la clase [B02-C12](../programa/clases/B02/B02-C12-tycho-brahe-y-observaciones-sistematicas/CLASE.md):**
- Tycho alcanzó unos 2 minutos y, en lo mejor, alrededor de medio minuto, y fue el primero en corregir por refracción atmosférica (S1).
- 🎯 **Por qué importa:** Una teoría solo es tan buena como los datos con que se contrasta. La pregunta motivadora es: ¿qué diferencia hay entre «mirar el cielo» y «observar sistemáticamente», y por qué esa diferencia cambió la astronomía?

📘 **Dónde se aprende** (1 clase): [B02-C12 · Tycho Brahe y observaciones sistemáticas](../programa/clases/B02/B02-C12-tycho-brahe-y-observaciones-sistematicas/CLASE.md).

### Refracción de Bennett

- La refracción de Bennett `R = cot(h + 7,31/(h + 4,4))` en minutos de arco da la elevación aparente.

🎯 **Por qué importa (clase B132-C03):** Una avenida de piedras que mira hacia el noreste «parece» apuntar al solsticio, pero ¿con qué precisión y para qué época? La decisión central: ¿qué declinación tiene el eje, con qué incertidumbre, y es compatible con el Sol solsticial de la época del monumento?

📘 **Dónde se aprende** (1 clase): [B132-C03 · Monumentos megalíticos y astronomía](../programa/clases/B132/B132-C03-monumentos-megaliticos-y-astronomia/CLASE.md).

### Refractor

- Un refractor reúne la luz con lentes; un reflector usa espejos y puede necesitar ajustar sus espejos (*colimación*); un Dobson es un reflector sobre una montura simple (S3).

💡 **Cómo se explica en la clase [B08-C14](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md):**
- Según Night Sky Network (S3): los refractores usan lentes, necesitan poco mantenimiento y suelen ser más grandes y caros que un reflector de potencia similar; los reflectores usan espejos y pueden requerir colimación; los Dobson son reflectores sobre una montura sencilla, fáciles de sacar y usar, una elección común de principiantes.
- Pausa. ¿Qué aumento da el refractor de 700 mm de F con un ocular de 10 mm? <details><summary>Respuesta</summary>`700/10 = 70×`; pupila de salida `70/70 = 1,0 mm`.</details>
- 🎯 **Por qué importa:** Un telescopio de juguete anuncia «600×» y decepciona. La pregunta motivadora: ¿qué telescopio me conviene y qué podré ver con él?

📘 **Dónde se aprende** (1 clase): [B08-C14 · Telescopios de iniciación](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md).

### Refugio

- El refugio es un volumen con aire respirable y acceso libre al vehículo de retorno.
- El refugio es el compartimento más blindado.

💡 **Cómo se explica en la clase [B110-C03](../programa/clases/B110/B110-C03-evacuacion-y-refugio-de-emergencia/CLASE.md):**
- Referencia consultada: la ponencia de la NASA indica que en la ISS se mantiene siempre un camino libre de cada tripulante a su vehículo de retorno, que cualquier módulo puede ser refugio si da acceso libre a ese vehículo y aire respirable, y que en una nave de un solo volumen como Orion no hay vehículo de escape aparte.
- Separar lo consultado (principios de refugio y camino libre) de lo ilustrativo (todos los tiempos).
- 🎯 **Por qué importa:** Ninguna clase anterior trata evacuación, refugio y vehículos de escape. La decisión central: ¿alcanza el margen entre ASET y RSET, y cuánto de ese margen depende de supuestos que no se conocen?

📘 **Dónde se aprende** (2 clases): [B110-C03 · Evacuación y refugio de emergencia](../programa/clases/B110/B110-C03-evacuacion-y-refugio-de-emergencia/CLASE.md); [B114-C04 · Refugio contra tormentas solares y compartimentos de protección](../programa/clases/B114/B114-C04-refugio-contra-tormentas-solares-y-compartimentos-de-proteccion/CLASE.md).

### Regalía

- La regalía `r` es un porcentaje de las ventas.

💡 **Cómo se explica en la clase [B124-C09](../programa/clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md):**
- Con ventas `S_t = 50 (1,15)^(t−1)` y regalía de 5 %, el valor actual de las regalías de 8 años es `21,352837` Mum sumando año a año y `21,352837` con la forma cerrada `r S₀/(1+d) (1 − q^T)/(1 − q)`, con `q = 1,15/1,10`; la diferencia es `1,1e-14`.
- Si el producto necesita tres licencias con regalías de 4, 6 y 5 %, el licenciatario paga `15%` de las ventas.
- ⚠️ **Error frecuente:** Evaluar cada regalía por separado. Se corrige con 8.2.
- 🎯 **Por qué importa:** La propiedad intelectual es un activo, pero su valor depende de cuánto se vende con ella y de cuánto del margen se queda el que la usa. La decisión central: ¿qué licencia conviene ofrecer y cuántas regalías soporta el licenciatario?

📘 **Dónde se aprende** (1 clase): [B124-C09 · Propiedad intelectual y licencias](../programa/clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md).

### Régimen

- El régimen es el nivel de `h` al que la descarga iguala a la perturbación.
- Mezcla perfecta: concentración uniforme en el recinto. Régimen: estado donde la concentración ya no cambia.

💡 **Cómo se explica en la clase [B87-C14](../programa/clases/B87/B87-C14-saturacion-y-descarga-de-momento/CLASE.md):**
- El nivel de régimen `≈ τ_sec/K_efectivo` es una consecuencia de la limitación de par, no de la ganancia.
- Ejercicio 5 · autónomo. ¿Por qué el nivel de régimen queda en 0,023 y no en 0?
- 🎯 **Por qué importa:** Una rueda saturada deja de controlar. La decisión central: ¿en cuánto tiempo se satura, cuánto par magnético hace falta para sostener la descarga y qué nivel de momento queda en régimen?

📘 **Dónde se aprende** (2 clases): [B87-C14 · Saturación y descarga de momento](../programa/clases/B87/B87-C14-saturacion-y-descarga-de-momento/CLASE.md); [B90-C02 · Buenas prácticas de sala limpia](../programa/clases/B90/B90-C02-buenas-practicas-de-sala-limpia/CLASE.md).

### Régimen adiabático

- El régimen adiabático supone que el calor no escapa y da, por eso, una cota superior de la temperatura.

🎯 **Por qué importa (clase B52-C18):** La energía disponible decide si un cuerpo funde y se diferencia o permanece primitivo. La decisión central: ¿cuánto calor aporta un radionúclido sin pérdidas y cuánta energía libera la diferenciación?

📘 **Dónde se aprende** (1 clase): [B52-C18 · Diferenciación planetaria](../programa/clases/B52/B52-C18-diferenciacion-planetaria/CLASE.md).

### Régimen asintótico

- El régimen asintótico es el rango de pasos pequeños donde el error ya sigue la ley `e ≈ C·hᵖ`.

💡 **Cómo se explica en la clase [B23-C03](../programa/clases/B23/B23-C03-casos-analiticos-de-validacion/CLASE.md):**
- RK4 4,35, 4,21, 4,12 (nominal 4; se acerca desde arriba porque aún no entra del todo en el régimen asintótico).
- Para Euler hubo que usar pasos muy finos (`N` de 1600 a 12 800): con `N = 50..400` el error es de ~1 au y el orden observado es 0,5–0,8, porque los pasos aún no están en el régimen asintótico.
- ⚠️ **Error frecuente:** Medir el orden fuera del régimen asintótico. Euler con `N = 50..400` da 0,5–0,8.
- 🎯 **Por qué importa:** Un integrador de órbitas puede conservar la energía, ser reversible e invariante ante rotaciones y aun así describir un Sol con otra masa o una ley de fuerza distinta. Para detectarlo necesitas una referencia con valores: «tras exactamente un período, el planeta vuelve a su punto de partida».

📘 **Dónde se aprende** (1 clase): [B23-C03 · Casos analíticos de validación](../programa/clases/B23/B23-C03-casos-analiticos-de-validacion/CLASE.md).

### Régimen de Epstein

- El régimen de Epstein vale cuando el grano es menor que el recorrido libre de las moléculas: `St = π a ρ_s/(2Σ)` en el plano medio.

💡 **Cómo se explica en la clase [B52-C03](../programa/clases/B52/B52-C03-granulacion-de-polvo-y-acrecion/CLASE.md):**
- Calcular el número de Stokes de un grano en régimen de Epstein.
- Epstein: pasa a régimen de Stokes y `t_s` depende de `a²`.
- 🎯 **Por qué importa:** Si los granos derivan más rápido de lo que crecen, el polvo se pierde antes de formar planetesimales. La decisión central: ¿a qué tamaño deriva más rápido un grano y cuánto tarda en caer?

📘 **Dónde se aprende** (1 clase): [B52-C03 · Granulación de polvo y acreción](../programa/clases/B52/B52-C03-granulacion-de-polvo-y-acrecion/CLASE.md).

### Régimen de gravedad

- El régimen de gravedad es aquel en que el peso del material limita el crecimiento; el de resistencia, aquel en que lo limita la cohesión.

💡 **Cómo se explica en la clase [B61-C01](../programa/clases/B61/B61-C01-dinamica-de-eyeccion-y-escalado-de-crateres/CLASE.md):**
- El régimen de gravedad: a tan baja `g` domina la resistencia del material, y el modelo no es válido.
- ⚠️ **Error frecuente:** Confundir régimen de gravedad con régimen de resistencia. Se corrige con la sección 6.
- 🎯 **Por qué importa:** Para leer un cráter hay que invertir la pregunta: del tamaño observado al proyectil. Sin las leyes de escalado no hay estimación de energía ni de la cantidad de material que sale despedido.

📘 **Dónde se aprende** (1 clase): [B61-C01 · Dinámica de eyección y escalado de cráteres](../programa/clases/B61/B61-C01-dinamica-de-eyeccion-y-escalado-de-crateres/CLASE.md).

### Régimen de Klein–Nishina

- El régimen de Klein–Nishina vale si no.

💡 **Cómo se explica en la clase [B27-C21](../programa/clases/B27/B27-C21-dispersion-compton-inversa-y-emision-de-alta-energia/CLASE.md):**
- Identificar el régimen de Klein–Nishina con `x = ε/mc²`.
- 🎯 **Por qué importa:** Los fotones de TeV que se detectan en algunos objetos proceden de este mecanismo, y la comparación entre la potencia Compton y la sincrotrón permite estimar el campo magnético. La decisión central: ¿qué energía alcanza el fotón dispersado, cuándo deja de valer la aproximación de Thomson y qué razón de potencias se espera?

📘 **Dónde se aprende** (1 clase): [B27-C21 · Dispersión Compton inversa y emisión de alta energía](../programa/clases/B27/B27-C21-dispersion-compton-inversa-y-emision-de-alta-energia/CLASE.md).

### Régimen de Rayleigh

- El régimen de Rayleigh ocurre cuando el objeto es mucho menor que `λ` y `σ ∝ r⁶/λ⁴`.

💡 **Cómo se explica en la clase [B118-C04](../programa/clases/B118/B118-C04-deteccion-por-radar/CLASE.md):**
- Por régimen: Rayleigh, transición, óptico.
- El ejemplo conductor es una esfera de 10 cm a 1,3 GHz, con `λ = 23,06 cm` y `k r = 1,36`, es decir, en la transición entre el régimen de Rayleigh y el óptico.
- 🎯 **Por qué importa:** Para los desechos pequeños en LEO el radar es el sensor más usado, pero su alcance cae rápido con el tamaño. La decisión central: ¿hasta qué distancia ve un radar un objeto de un tamaño dado, y cuánto pierde cuando el objeto se aleja?

📘 **Dónde se aprende** (1 clase): [B118-C04 · Detección por radar](../programa/clases/B118/B118-C04-deteccion-por-radar/CLASE.md).

### Régimen de Thomson

- El régimen de Thomson vale si `4γε ≪ mc²`.

🎯 **Por qué importa (clase B27-C21):** Los fotones de TeV que se detectan en algunos objetos proceden de este mecanismo, y la comparación entre la potencia Compton y la sincrotrón permite estimar el campo magnético. La decisión central: ¿qué energía alcanza el fotón dispersado, cuándo deja de valer la aproximación de Thomson y qué razón de potencias se espera?

📘 **Dónde se aprende** (1 clase): [B27-C21 · Dispersión Compton inversa y emisión de alta energía](../programa/clases/B27/B27-C21-dispersion-compton-inversa-y-emision-de-alta-energia/CLASE.md).

### Régimen internacional

- El régimen internacional es el conjunto de reglas aún por crear para explotar recursos.
- El régimen internacional es el conjunto de reglas por crear (art. 11).

💡 **Cómo se explica en la clase [B119-C25](../programa/clases/B119/B119-C25-derecho-y-marcos-de-recursos-espaciales/CLASE.md):**
- El Acuerdo sobre la Luna (UNOOSA, consultado el 2026-11-11) dice en su art. 11 que la Luna y sus recursos son patrimonio común de la humanidad, que colocar equipo no crea propiedad y que se creará un régimen internacional; la nota de la ONU recoge el art.
- 🎯 **Por qué importa:** B119 trata los tratados en general (C01, C05) y ninguna clase enseña los marcos de recursos ni el razonamiento económico que los motiva. La gobernanza se desarrolla en C36 y los aspectos técnicos en B59.

📘 **Dónde se aprende** (2 clases): [B119-C05 · Acuerdo sobre la Luna y alcance](../programa/clases/B119/B119-C05-acuerdo-sobre-la-luna-y-alcance/CLASE.md); [B119-C25 · Derecho y marcos de recursos espaciales](../programa/clases/B119/B119-C25-derecho-y-marcos-de-recursos-espaciales/CLASE.md).

### Régimen limitado por la estrella

- El régimen limitado por la estrella tiene SNR `≈ √N*`.

🎯 **Por qué importa (clase B29-C02):** Una apertura pequeña pierde estrella; una grande suma cielo y ruido de lectura. La decisión central: ¿qué apertura maximiza la relación señal-ruido y qué error en magnitud implica?

📘 **Dónde se aprende** (1 clase): [B29-C02 · Curvas de luz fotométricas](../programa/clases/B29/B29-C02-curvas-de-luz-fotometricas/CLASE.md).

### Régimen lineal

- El régimen lineal, el saturado y el de amortiguamiento.

💡 **Cómo se explica en la clase [B32-C09](../programa/clases/B32/B32-C09-medicion-de-perfiles-de-linea-ancho-equivalente-y-ajuste/CLASE.md):**
- El script [crecimiento.py](crecimiento.py) integra `W(τ₀)` (comprueba `10⁻⁸` y el régimen lineal al 1 %).
- 🎯 **Por qué importa:** Medir una abundancia exige saber en qué régimen está la línea. La decisión central: ¿cómo depende el ancho equivalente de la columna de absorbedores?

📘 **Dónde se aprende** (1 clase): [B32-C09 · Medición de perfiles de línea: ancho equivalente y ajuste](../programa/clases/B32/B32-C09-medicion-de-perfiles-de-linea-ancho-equivalente-y-ajuste/CLASE.md).

### Régimen no relativista

- El régimen no relativista es `x ≪ 1`; el ultrarrelativista, `x ≫ 1`.

💡 **Cómo se explica en la clase [B27-C01](../programa/clases/B27/B27-C01-presion-de-degeneracion/CLASE.md):**
- Ejercicio 3 · casi autónomo. Si se duplica `n` en el régimen no relativista, ¿cuánto sube `P`?
- 🎯 **Por qué importa:** Una estrella sin fusión no se desploma porque los electrones (o neutrones) no pueden apretarse más allá de lo que permite el principio de exclusión, aunque la temperatura sea cero. La decisión central: dada la densidad de un gas degenerado, ¿cuánto vale el momento de Fermi, la presión y cuál de los dos límites aplica?

📘 **Dónde se aprende** (1 clase): [B27-C01 · Presión de degeneración](../programa/clases/B27/B27-C01-presion-de-degeneracion/CLASE.md).

### Régimen óptico

- El régimen óptico ocurre cuando es mucho mayor y `σ ≈ π r²`.

💡 **Cómo se explica en la clase [B118-C04](../programa/clases/B118/B118-C04-deteccion-por-radar/CLASE.md):**
- Por régimen: Rayleigh, transición, óptico.
- El ejemplo conductor es una esfera de 10 cm a 1,3 GHz, con `λ = 23,06 cm` y `k r = 1,36`, es decir, en la transición entre el régimen de Rayleigh y el óptico.
- 🎯 **Por qué importa:** Para los desechos pequeños en LEO el radar es el sensor más usado, pero su alcance cae rápido con el tamaño. La decisión central: ¿hasta qué distancia ve un radar un objeto de un tamaño dado, y cuánto pierde cuando el objeto se aleja?

📘 **Dónde se aprende** (1 clase): [B118-C04 · Detección por radar](../programa/clases/B118/B118-C04-deteccion-por-radar/CLASE.md).

### Régimen periódico

- El régimen periódico es el SOC que se repite al inicio de cada órbita.

💡 **Cómo se explica en la clase [B86-C13](../programa/clases/B86/B86-C13-energia-durante-eclipse/CLASE.md):**
- La batería parte de `80 %`, se recarga a `100 %` en la primera luz y desde la segunda órbita el régimen es periódico: la variación entre las dos últimas órbitas es `0,0e+00`.
- *Descripción textual:* el eclipse baja el SOC y la luz lo recupera con potencia limitada; el SOC al inicio de la órbita siguiente decide si el ciclo cierra (régimen periódico) o si hay déficit y agotamiento.
- 🎯 **Por qué importa:** Una batería que cubre bien un eclipse puede fallar tras cien porque cada órbita pierde un poco más de lo que recupera. El cierre del ciclo es la prueba de que el diseño es sostenible.

📘 **Dónde se aprende** (1 clase): [B86-C13 · Energía durante eclipse](../programa/clases/B86/B86-C13-energia-durante-eclipse/CLASE.md).

### Régimen regular

- Un régimen regular (`K` pequeño) tiene curvas invariantes que acotan las trayectorias; en el caótico (`K` grande) las trayectorias llenan una región.

💡 **Cómo se explica en la clase [B73-C13](../programa/clases/B73/B73-C13-caos-determinista/CLASE.md):**
- Descripción larga: el régimen regular mantiene la separación pequeña y la reversibilidad; el caótico la amplifica `e^{1,02 n}` y pierde la reversibilidad numérica.
- Iterar el mapa estándar en un régimen regular y en uno caótico.
- 🎯 **Por qué importa:** Un sistema determinista puede ser impredecible a largo plazo: el error de medida se amplifica exponencialmente y fija un horizonte más allá del cual la predicción no vale, por más cómputo que se use. La decisión central: ¿hasta cuándo puedo confiar en una integración y cómo reconozco el régimen caótico?

📘 **Dónde se aprende** (1 clase): [B73-C13 · Caos determinista](../programa/clases/B73/B73-C13-caos-determinista/CLASE.md).

### Régimen relativista

- El régimen relativista ocurre cuando `p_F ≳ m_ec`.

💡 **Cómo se explica en la clase [B31-C06](../programa/clases/B31/B31-C06-estadisticas-cuanticas/CLASE.md):**
- La energía de Fermi de un metal con `n = 8,5 × 10²⁸ m⁻³` (ilustrativo) es `7,05 eV`; para `n = 10³⁶ m⁻³` (tipo enana blanca, ilustrativo) el parámetro `p_F/(m_ec) = 1,19` indica régimen relativista.
- ⚠️ **Error frecuente:** Usar la fórmula no relativista en el régimen relativista. Se corrige con 8.4.
- 🎯 **Por qué importa:** La radiación de las estrellas y la presión de degeneración de los remanentes estelares dependen de estas estadísticas. La decisión central: ¿qué distribución usar y qué constantes se derivan?

📘 **Dónde se aprende** (1 clase): [B31-C06 · Estadísticas cuánticas](../programa/clases/B31/B31-C06-estadisticas-cuanticas/CLASE.md).

### Región conectada

- Una región conectada es un conjunto de píxeles de objeto unidos por vecindad; la conectividad 4 une píxeles que comparten un lado, la 8 también los que comparten una esquina (S1 describe cómo `scipy.ndimage.label` usa por defecto la cruz de 4 vecinos y cómo pedir 8).

💡 **Cómo se explica en la clase [B15-C13](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md):**
- Una región conectada es un grupo de píxeles de objeto que se tocan.
- O --> L["Etiquetado de<br/>regiones conectadas"]
- 🎯 **Por qué importa:** Medir el área de las manchas solares, el porcentaje de nubes de una escena o el tamaño de un cráter exige delimitar el objeto. La delimitación no es neutra: un umbral distinto cambia el área.

📘 **Dónde se aprende** (1 clase): [B15-C13 · Segmentación de imágenes](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md).

### Región creíble

- La región creíble acumula probabilidad.

🎯 **Por qué importa (clase B28-C10):** El área de localización decide cuántas fotos hacen falta para encontrar la contrapartida. Un mapa mal calibrado engaña.

📘 **Dónde se aprende** (1 clase): [B28-C10 · Localización probabilística de eventos](../programa/clases/B28/B28-C10-localizacion-probabilistica-de-eventos/CLASE.md).

### Región crítica

- La región crítica es el conjunto de valores del estadístico que llevan a rechazar; con la `t`, el NIST indica rechazar cuando el valor absoluto del estadístico supera el valor crítico de la tabla (S3).

🎯 **Por qué importa (clase B12-C09):** Muchas preguntas científicas tienen forma de decisión: ¿coinciden dos mediciones de la misma constante?, ¿el sensor sigue calibrado?, ¿es real la señal o es ruido? Sin un procedimiento con error controlado, cada persona decide por intuición.

📘 **Dónde se aprende** (1 clase): [B12-C09 · Pruebas de hipótesis](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md).

### Región de aislamiento

- La región de aislamiento: `r > √2`.

🎯 **Por qué importa (clase B47-C11):** Un aislador mal sintonizado amplifica en vez de atenuar. La decisión central: ¿qué frecuencia natural y qué amortiguamiento aíslan sin amplificar demasiado en la resonancia?

📘 **Dónde se aprende** (1 clase): [B47-C11 · Aislamiento vibracional](../programa/clases/B47/B47-C11-aislamiento-vibracional/CLASE.md).

### Región de estabilidad

- El método es estable para un `z` si `|R(z)| ≤ 1`; la región de estabilidad es el conjunto de `z` donde ocurre.

🎯 **Por qué importa (clase B11-C09):** Un modelo térmico de una nave tiene constantes de tiempo que van de segundos (un sensor fino) a horas (un tanque grande). Un método explícito debe usar un paso comparable al más rápido aunque lo único que interese sea lo lento: pagar por una escala que no se observa.

📘 **Dónde se aprende** (1 clase): [B11-C09 · Análisis de estabilidad numérica](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md).

### Región en banana

- La región en banana es la forma curva que adopta la incertidumbre en coordenadas cartesianas cuando es grande.

🎯 **Por qué importa (clase B118-C08):** La `Pc` de B118-C06 depende de la covarianza en el TCA, que sale de propagar la incertidumbre hasta ese instante. La decisión central: ¿hasta cuándo es válida una covarianza lineal y cuándo hay que propagar muestras?

📘 **Dónde se aprende** (1 clase): [B118-C08 · Propagación de incertidumbre en conjunciones](../programa/clases/B118/B118-C08-propagacion-de-incertidumbre-en-conjunciones/CLASE.md).

### Región HII

- Una región HII es una zona de gas de hidrógeno ionizado por la radiación ultravioleta de estrellas masivas.

💡 **Cómo se explica en la clase [B25-C05](../programa/clases/B25/B25-C05-regiones-de-formacion-estelar/CLASE.md):**
- Su límite: la región real se expande por su propia presión y por los vientos de la estrella, no está congelada en el radio de equilibrio.
- Es un orden de magnitud con un coeficiente de fuente secundaria y una estrella sintética; no es una región observada.
- 🎯 **Por qué importa:** Una galaxia no convierte todo su gas en estrellas a la vez: lo hace a un ritmo que puede medirse y comparar. Entender las regiones donde nacen las estrellas masivas permite reconocerlas desde lejos, y entender la relación entre gas y ritmo de formación permite saber cuánto tiempo puede una galaxia seguir formando estrellas.

📘 **Dónde se aprende** (1 clase): [B25-C05 · Regiones de formación estelar](../programa/clases/B25/B25-C05-regiones-de-formacion-estelar/CLASE.md).

### Región prohibida

- La región prohibida es donde `2Ω < C`, porque pediría `v² < 0`.

💡 **Cómo se explica en la clase [B73-C07](../programa/clases/B73/B73-C07-constante-de-jacobi/CLASE.md):**
- Si `2Ω < C` no hay movimiento posible: es la región prohibida.
- El laboratorio dibuja en texto la curva para `C₂ < C < C₁`: una región prohibida con forma de anillo que rodea a la Tierra y la Luna, con el paso de L1 abierto entre ellas y el de L2 cerrado.
- 🎯 **Por qué importa:** La constante de Jacobi es la única cantidad conservada del CR3BP y decide, sin integrar, si una nave puede ir de la Tierra a la Luna o escapar. La decisión central: ¿qué dice un número `C` sobre las regiones por las que se puede mover una partícula?

📘 **Dónde se aprende** (1 clase): [B73-C07 · Constante de Jacobi](../programa/clases/B73/B73-C07-constante-de-jacobi/CLASE.md).

### Región protegida

- La región protegida es LEO o GEO según la IADC.

💡 **Cómo se explica en la clase [B118-C24](../programa/clases/B118/B118-C24-directrices-tecnicas-de-mitigacion-de-desechos-iadc-iso-24113/CLASE.md):**
- M8 acumula dos incumplimientos y M9 queda fuera de las regiones protegidas.
- Clasificar una órbita según las regiones protegidas (LEO hasta 2000 km;
- 🎯 **Por qué importa:** B118-C11 enseña diseño para mitigación; ninguna clase trata las directrices de la IADC y de ISO ni su verificación. Un requisito sin criterio de aceptación y sin pruebas de borde se interpreta de distintas maneras.

📘 **Dónde se aprende** (1 clase): [B118-C24 · Directrices técnicas de mitigación de desechos (IADC, ISO 24113)](../programa/clases/B118/B118-C24-directrices-tecnicas-de-mitigacion-de-desechos-iadc-iso-24113/CLASE.md).

### Región protegida GEO

- La región protegida GEO abarca ± 200 km y ± 15°.

💡 **Cómo se explica en la clase [B118-C12](../programa/clases/B118/B118-C12-disposicion-al-fin-de-vida/CLASE.md):**
- Ejercicio 3 · casi autónomo. ¿Cuál es el límite de altitud de la región protegida LEO?
- Ejercicio 8 · autónomo. ¿Qué región protegida de GEO define la IADC en latitud?
- 🎯 **Por qué importa:** La disposición es la principal medida de mitigación: en LEO, que la vida residual sea corta; en GEO, que el satélite quede por encima de la región protegida. La decisión central: ¿desde qué altitud se puede dejar un satélite en LEO para que decaiga en 25 años, y cuánta elevación necesita un satélite de GEO?

📘 **Dónde se aprende** (1 clase): [B118-C12 · Disposición al fin de vida](../programa/clases/B118/B118-C12-disposicion-al-fin-de-vida/CLASE.md).

### Región protegida LEO

- La región protegida LEO llega a 2000 km.

💡 **Cómo se explica en la clase [B118-C12](../programa/clases/B118/B118-C12-disposicion-al-fin-de-vida/CLASE.md):**
- Ejercicio 3 · casi autónomo. ¿Cuál es el límite de altitud de la región protegida LEO?
- Ejercicio 8 · autónomo. ¿Qué región protegida de GEO define la IADC en latitud?
- 🎯 **Por qué importa:** La disposición es la principal medida de mitigación: en LEO, que la vida residual sea corta; en GEO, que el satélite quede por encima de la región protegida. La decisión central: ¿desde qué altitud se puede dejar un satélite en LEO para que decaiga en 25 años, y cuánta elevación necesita un satélite de GEO?

📘 **Dónde se aprende** (1 clase): [B118-C12 · Disposición al fin de vida](../programa/clases/B118/B118-C12-disposicion-al-fin-de-vida/CLASE.md).

### Registrador

- El registrador debe cubrir lo producido durante el hueco máximo con margen.

💡 **Cómo se explica en la clase [B83-C11](../programa/clases/B83/B83-C11-presupuestos-de-datos/CLASE.md):**
- En el hueco máximo de 11,49 h se producen 38,66 Gbit; con margen 1,3 el registrador debe tener 50,26 Gbit de los 256 de ejemplo (19,6 %).
- P --> R["Registrador para el hueco maximo"]
- ⚠️ **Error frecuente:** Dimensionar el registrador con el promedio. Usa el hueco máximo con margen
- 🎯 **Por qué importa:** Un satélite que produce más datos de los que puede bajar los pierde o se satura. La decisión central: ¿cabe todo lo que se produce en los minutos de contacto, y qué tamaño de registrador cubre el peor hueco?

📘 **Dónde se aprende** (1 clase): [B83-C11 · Presupuestos de datos](../programa/clases/B83/B83-C11-presupuestos-de-datos/CLASE.md).

### Registro

- Un registro es una observación anotada con fecha.
- Un registro describe un archivo (instrumento, tiempo, banda).
- Un registro es un evento de un mensajero.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B02-C02](../programa/clases/B02/B02-C02-observacion-mesopotamica-y-egipcia/CLASE.md):**
- A["Registro largo<br/>de eclipses"] --> B["Regularidad:<br/>intervalo ≈ 6 585 d"]
- *Descripción textual:* de un registro largo de eclipses sale una regularidad (un intervalo de unos 6 585 días); de ella pueden surgir una explicación por casi-igualdad de tres períodos lunares y un uso predictivo con incertidumbre.
- 🎯 **Por qué importa:** Una predicción necesita una larga memoria. Para decir que un fenómeno volverá, alguien tuvo que anotarlo muchas veces y compararlo.

📘 **Dónde se aprende** (9 clases): [B02-C02 · Observación mesopotámica y egipcia](../programa/clases/B02/B02-C02-observacion-mesopotamica-y-egipcia/CLASE.md); [B08-C17 · Registro sistemático en bitácora](../programa/clases/B08/B08-C17-registro-sistematico-en-bitacora/CLASE.md); [B14-C22 · Acceso a datos heliofísicos abiertos con SunPy](../programa/clases/B14/B14-C22-acceso-a-datos-heliofisicos-abiertos-con-sunpy/CLASE.md); [B14-C30 · Cadenas de procesamiento automatizado de datos](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md); [B15-C14 · Registro y alineación](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md); [B28-C17 · Archivos de eventos multimensajero](../programa/clases/B28/B28-C17-archivos-de-eventos-multimensajero/CLASE.md) y 3 más.

### Registro de calibración

- Un registro de calibración es el documento que recoge una calibración: instrumento, patrones, condiciones, resultado con incertidumbre y vigencia.

💡 **Cómo se explica en la clase [B13-C19](../programa/clases/B13/B13-C19-metadatos-y-registros-de-calibracion/CLASE.md):**
- El registro de ejemplo describe la calibración de C05 (`a = 46,55 DN`, `b = 2,5036 DN/(W/m²)`) con un patrón, condiciones, `k = 2`, `U` y vigencia de un año.
- La evidencia es el registro de calibración validado del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Dentro de un año alguien usará los datos de un fotodiodo calibrado hoy. Necesitará saber con qué patrones, a qué temperatura, con qué incertidumbre y hasta cuándo es válida la calibración.

📘 **Dónde se aprende** (1 clase): [B13-C19 · Metadatos y registros de calibración](../programa/clases/B13/B13-C19-metadatos-y-registros-de-calibracion/CLASE.md).

### Registro de ejecución

- Un registro de ejecución guarda entradas, entorno y resultado.

💡 **Cómo se explica en la clase [B07-C19](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md):**
- Con las mismas entradas y entorno, dos ejecuciones dan un registro igual: se comprueba con `==`.
- *Descripción textual:* cuatro entradas —los datos con su huella, el código identificado por su commit, el entorno fijado y la semilla con los parámetros— alimentan una ejecución que produce el resultado y un registro en JSON; con ese registro, otra persona puede comprobar si obtiene lo mismo.
- 🎯 **Por qué importa:** Un resultado que solo su autor puede obtener, y solo el día en que lo obtuvo, es una anécdota. Cuando pasan seis meses, no sabrás con qué datos, con qué versión ni con qué semilla lo generaste.

📘 **Dónde se aprende** (1 clase): [B07-C19 · Documentación y reproducibilidad](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md).

### Registro de procedencia

- Un registro de procedencia (*provenance record*) es el documento que lo declara.

💡 **Cómo se explica en la clase [B23-C07](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md):**
- Construir un registro de procedencia y una huella canónica que excluya lo no determinista.
- La evidencia es el registro de procedencia verificable del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Un informe dice «el modelo reproduce la posición con un error de 8,21 × 10⁻⁴ au». Seis meses después, nadie sabe con qué versión del código, qué archivo de datos ni qué tolerancia se calculó, y el número no se puede reproducir ni defender.

📘 **Dónde se aprende** (1 clase): [B23-C07 · Trazabilidad científica de resultados](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md).

### Registro de revisión

- Un registro de revisión guarda cada comprobación con su criterio, resultado y fecha.

💡 **Cómo se explica en la clase [B84-C31](../programa/clases/B84/B84-C31-documentacion-y-revision-de-analisis-de-elementos-finitos/CLASE.md):**
- La evidencia es la registro de revisión de un análisis del ejercicio 12 (sección 20).
- Integrador. Elabora tu *registro de revisión de un análisis*: lista de comprobaciones con tolerancias, resultados de cuatro modelos y las acciones que tomarías.
- 🎯 **Por qué importa:** Un error de unidades da una frecuencia de 0,008 Hz o de 258 Hz sin aviso; solo las comprobaciones sistemáticas lo detectan antes de la revisión. La decisión central: ¿qué comprobaciones demuestran que el modelo es correcto antes de revisar sus resultados?

📘 **Dónde se aprende** (1 clase): [B84-C31 · Documentación y revisión de análisis de elementos finitos](../programa/clases/B84/B84-C31-documentacion-y-revision-de-analisis-de-elementos-finitos/CLASE.md).

### Registro de salida

- El registro de salida lee las filas una a una.

🎯 **Por qué importa (clase B44-C02):** Cada transferencia pierde una pequeña fracción de carga, y un píxel lejano se transfiere miles de veces. La decisión central: ¿qué CTE hace aceptable un sensor de 2048 × 2048?

📘 **Dónde se aprende** (1 clase): [B44-C02 · Sensores CCD](../programa/clases/B44/B44-C02-sensores-ccd/CLASE.md).

### Registro de solo añadir

- Un registro de solo añadir no modifica entradas: añade nuevas (una corrección es otra observación).

💡 **Cómo se explica en la clase [B116-C03](../programa/clases/B116/B116-C03-historia-clinica-remota-y-registros-medicos-de-mision/CLASE.md):**
- S["sensores"] --> B["registro a bordo<br/>solo añadir"]
- Sincronizar dos registros de solo añadir con identificador único y comprobar la convergencia.
- 🎯 **Por qué importa:** Si el enlace se corta 40 minutos y al volver los dos registros difieren, ¿cuál es el verdadero? Si un valor cambia en el camino, ¿cómo se enteran?

📘 **Dónde se aprende** (1 clase): [B116-C03 · Historia clínica remota y registros médicos de misión](../programa/clases/B116/B116-C03-historia-clinica-remota-y-registros-medicos-de-mision/CLASE.md).

### Registro externo

- Un registro externo guarda la huella final fuera de tu control.

💡 **Cómo se explica en la clase [B14-C24](../programa/clases/B14/B14-C24-documentacion-de-hipotesis-y-decisiones-de-analisis/CLASE.md):**
- Por eso la huella final debe publicarse o registrarse aparte (un registro externo, un mensaje fechado, un depósito de datos): si no, la cadena demuestra coherencia interna, no antigüedad.
- Debe incluir las entradas con sus campos, la tabla de la sección 12 con tus resultados, el informe que separe lo confirmatorio de lo exploratorio, una declaración de que la cadena no autentica ni prueba antigüedad sin un registro externo, y la propuesta de ese registro.
- 🎯 **Por qué importa:** Seis meses después de un análisis, nadie recuerda por qué se excluyeron tres puntos ni cuándo se cambió el modelo. Y un revisor pregunta si la exclusión estaba prevista.

📘 **Dónde se aprende** (1 clase): [B14-C24 · Documentación de hipótesis y decisiones de análisis](../programa/clases/B14/B14-C24-documentacion-de-hipotesis-y-decisiones-de-analisis/CLASE.md).

### Registro único

- Un registro único (`k = 1`) es identificable.

💡 **Cómo se explica en la clase [B129-C05](../programa/clases/B129/B129-C05-consentimiento-y-privacidad-de-participantes/CLASE.md):**
- Con edad, comuna, equipo y coordenadas, el mínimo es `k = 1` incluso con coordenadas a 0 decimales (`111 km`): hay 185 registros únicos de 300.
- Así no se publica ninguna fila de persona y se evita el registro único.
- 🎯 **Por qué importa:** Cuando un conjunto de datos se publica o se comparte, los datos de las personas pueden permitir reconocerlas aunque se quite el nombre. La decisión central: ¿qué recoger, con qué precisión publicarlo y cómo respetar que alguien retire su consentimiento?

📘 **Dónde se aprende** (1 clase): [B129-C05 · Consentimiento y privacidad de participantes](../programa/clases/B129/B129-C05-consentimiento-y-privacidad-de-participantes/CLASE.md).

### Regla comprobable

- Una regla comprobable es un artículo traducido a una condición verdadera o falsa sobre atributos.

🎯 **Por qué importa (clase B119-C01):** Casi todo el derecho espacial posterior (salvamento, responsabilidad, registro, Luna) desarrolla principios de este tratado, y ninguna otra clase del programa lo estudia como instrumento jurídico. La decisión central: ¿qué obligación del tratado se infringe en una misión dada y qué cambio mínimo la devuelve a la conformidad?

📘 **Dónde se aprende** (1 clase): [B119-C01 · Tratado del Espacio Ultraterrestre](../programa/clases/B119/B119-C01-tratado-del-espacio-ultraterrestre/CLASE.md).

### Regla conjuntiva

- La regla conjuntiva exige todos.

💡 **Cómo se explica en la clase [B107-C09](../programa/clases/B107/B107-C09-progresion-de-recuperacion-y-criterios-de-alta/CLASE.md):**
- Aplicar una regla conjuntiva («todos ≥ umbral») con `k` evaluaciones consecutivas.
- Ejercicio 12 · integrador. Integrador. Integrador. Elabora tu *regla de alta con su tasa de error*: cruces, regla conjuntiva, pase falso teórico y simulado, efecto de `k`, costo en tiempo y lista de qué es sintético, consultado y no consultado.
- 🎯 **Por qué importa:** Los fragmentos consultados indican que la pérdida de fuerza tras misiones largas conlleva riesgos operativos y médicos (English et al., 2015) y que existen baterías de pruebas funcionales y medidas fisiológicas (Mulavara et al., 2018). Una regla de alta combina varios indicadores con ruido.

📘 **Dónde se aprende** (1 clase): [B107-C09 · Progresión de recuperación y criterios de alta](../programa/clases/B107/B107-C09-progresion-de-recuperacion-y-criterios-de-alta/CLASE.md).

### Regla de Arnett

- La regla de Arnett dice que en el máximo `L = Q`.

💡 **Cómo se explica en la clase [B28-C18](../programa/clases/B28/B28-C18-interpretacion-de-kilonovas/CLASE.md):**
- En el máximo `L = Q` exactamente (regla de Arnett); después sí `L > Q`.
- El script [kilonova.py](kilonova.py) integra con sustitución (comprueba `10⁻⁶` frente a Simpson fino), busca el máximo y verifica la regla de Arnett (comprueba `10⁻⁴`).
- 🎯 **Por qué importa:** La escala de tiempo y el brillo de una kilonova dependen de la masa eyectada y de su velocidad. Entender esa relación permite estimar ambos a partir de la curva de luz.

📘 **Dónde se aprende** (1 clase): [B28-C18 · Interpretación de kilonovas](../programa/clases/B28/B28-C18-interpretacion-de-kilonovas/CLASE.md).

### Regla de Born

- La regla de Born da la probabilidad como `|⟨a|ψ⟩|²`.

💡 **Cómo se explica en la clase [B31-C03](../programa/clases/B31/B31-C03-estados-y-observables-cuanticos/CLASE.md):**
- S["|ψ⟩ = cos(θ/2)|0⟩ + e^{iφ} sin(θ/2)|1⟩"] --> B["regla de Born"]
- *Descripción textual:* el estado da probabilidades por la regla de Born y cumple Robertson; el hamiltoniano se integra con RK4 y se compara con la fórmula de Rabi.
- 🎯 **Por qué importa:** Un cúbit, un espín o un átomo de dos niveles obedecen estas reglas, y la medida cambia el estado. La decisión central: ¿cómo se calculan probabilidades y evolución en un sistema de dos niveles?

📘 **Dónde se aprende** (1 clase): [B31-C03 · Estados y observables cuánticos](../programa/clases/B31/B31-C03-estados-y-observables-cuanticos/CLASE.md).

### Regla de categorías

- Una regla de categorías convierte esa medida en una etiqueta; la de esta clase es didáctica.

💡 **Cómo se explica en la clase [B67-C04](../programa/clases/B67/B67-C04-estimacion-de-reservas-y-categorias-de-recursos/CLASE.md):**
- Aplicar una regla de categorías por el semiancho relativo del intervalo al 90 %.
- Datos: bloque, densidad y regla de categorías sintéticos; semilla 6704.
- 🎯 **Por qué importa:** Decir «hay 330 kt» sin intervalo ni categoría invita a decisiones equivocadas. La decisión central: ¿cuánto del recurso se puede llamar reserva, y qué falta para subir de categoría?

📘 **Dónde se aprende** (1 clase): [B67-C04 · Estimación de reservas y categorías de recursos](../programa/clases/B67/B67-C04-estimacion-de-reservas-y-categorias-de-recursos/CLASE.md).

### Regla de Cramer

- La regla de Cramer da cada incógnita de `A x = b` como cociente de dos determinantes.

💡 **Cómo se explica en la clase [B10-C04](../programa/clases/B10/B10-C04-determinantes-y-soluciones/CLASE.md):**
- Resolver un sistema pequeño con la regla de Cramer.
- 🎯 **Por qué importa:** Dos estaciones terrestres miden la dirección hacia un mismo objeto y quieren fijar su posición cruzando las visuales. Si el objeto está cerca y las visuales forman un buen ángulo, el cruce es nítido.

📘 **Dónde se aprende** (1 clase): [B10-C04 · Determinantes y soluciones](../programa/clases/B10/B10-C04-determinantes-y-soluciones/CLASE.md).

### Regla de Dawes

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C12):** La difracción fija el mejor detalle posible. La decisión central: ¿cuándo se resuelven dos estrellas y qué cuesta una obstrucción?

📘 **Dónde se aprende** (1 clase): [B41-C12 · Difracción y límite de Rayleigh](../programa/clases/B41/B41-C12-difraccion-y-limite-de-rayleigh/CLASE.md).

### Regla de decisión

- La regla de decisión dice cómo se combinan los veredictos en una conclusión («apto» solo si todos los criterios marcados como de uso se cumplen).
- Una regla de decisión dice qué hacer según los datos.

💡 **Cómo se explica en la clase [B23-C08](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md):**
- Cada criterio produce un veredicto; la regla de decisión los combina; las advertencias recogen lo que no se cumplió y los límites recogen lo que no se probó.
- Los veredictos alimentan las advertencias y la regla de decisión.
- 🎯 **Por qué importa:** Un conjunto de pruebas que pasan no es un informe. Quien debe decidir si usar el código necesita saber para qué uso se evaluó, con qué criterios, qué falló y qué no se probó.

📘 **Dónde se aprende** (2 clases): [B23-C08 · Informe de verificación y validación](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md); [B131-C08 · Evaluación formativa en el aula de astronomía](../programa/clases/B131/B131-C08-evaluacion-formativa-en-el-aula-de-astronomia/CLASE.md).

### Regla de dos personas

- La regla de dos personas exige que una acción crítica la aprueba otra persona distinta del emisor.

💡 **Cómo se explica en la clase [B122-C05](../programa/clases/B122/B122-C05-control-de-accesos-y-gestion-de-identidades-en-operaciones/CLASE.md):**
- Calcular los pares emisor-aprobador válidos para la regla de dos personas.
- ⚠️ **Error frecuente:** Creer que la regla de dos personas se cumple sola. Requiere pares válidos, ver 8.4.
- 🎯 **Por qué importa:** B96-C07 trata solo la autorización de telecomandos. La decisión central: ¿qué permisos sobran, cuáles se contradicen y quién puede aprobar a quién?

📘 **Dónde se aprende** (1 clase): [B122-C05 · Control de accesos y gestión de identidades en operaciones](../programa/clases/B122/B122-C05-control-de-accesos-y-gestion-de-identidades-en-operaciones/CLASE.md).

### Regla de dureza relativa

- La regla de dureza relativa supone abrasión severa (`k ≈ 10⁻³`) si `H_a/H_s ≥ 1,2` y suave (`k ≈ 10⁻⁶`) si `≤ 0,8`.

💡 **Cómo se explica en la clase [B84-C36](../programa/clases/B84/B84-C36-desgaste-abrasivo-por-regolito-en-mecanismos/CLASE.md):**
- Límite: la regla de dureza relativa es una simplificación; el desgaste real depende de forma, tamaño y fragmentación de los granos.
- Usar la regla de dureza relativa `H_a/H_s` para elegir el coeficiente `k`.
- 🎯 **Por qué importa:** Un sello de acero inoxidable bajo regolito pierde 1,8 mm en 1000 h con un 10 % del área expuesta a polvo, y uno de carburo de volframio pierde 0,18 µm: la elección de dureza decide si el mecanismo vive. La decisión central: ¿qué superficie y qué estrategia de protección permiten que un mecanismo sobreviva al regolito?

📘 **Dónde se aprende** (1 clase): [B84-C36 · Desgaste abrasivo por regolito en mecanismos](../programa/clases/B84/B84-C36-desgaste-abrasivo-por-regolito-en-mecanismos/CLASE.md).

### Regla de la cadena

- La regla de la cadena: si `y = f(u)` y `u = g(x)`, entonces `dy/dx = f′(u) · g′(x)` (S1, §1.4(iii), ecs. 1.4.5–1.4.7 y 1.4.10).

💡 **Cómo se explica en la clase [B09-C04](../programa/clases/B09/B09-C04-reglas-de-derivacion/CLASE.md):**
- La regla de la cadena es una transmisión de engranajes: si la rueda `x` hace girar la `u` a razón `g′` y la `u` hace girar la `y` a razón `f′`, la razón total es el producto.
- Aplicar la regla de la cadena a una composición.
- 🎯 **Por qué importa:** La gravedad que siente un cuerpo depende de su distancia al astro: `g(r) = GM/r²`. La marea nace de que esa gravedad cambia de un lado a otro de un cuerpo extenso.

📘 **Dónde se aprende** (1 clase): [B09-C04 · Reglas de derivación](../programa/clases/B09/B09-C04-reglas-de-derivacion/CLASE.md).

### Regla de la mano derecha

- El producto vectorial `u × v` es el vector perpendicular a `u` y a `v` con módulo `|u||v| sen γ` y sentido dado por la regla de la mano derecha: si los dedos van de `u` hacia `v` por el ángulo menor, el pulgar apunta a `u × v`.

💡 **Cómo se explica en la clase [B04-C14](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md):**
- La regla de la mano derecha dice hacia qué lado apunta ese eje: si los dedos siguen el giro, el pulgar marca la normal.
- Su límite: la regla depende de la convención del sistema (mano derecha o izquierda); en todo este programa se usa la derecha.
- 🎯 **Por qué importa:** Una órbita no es solo una forma (C09): es una forma colocada en el espacio con una orientación. ¿Hacia dónde apunta su plano?

📘 **Dónde se aprende** (1 clase): [B04-C14 · Producto vectorial y orientación](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md).

### Regla de la potencia

- La regla de la potencia: `d(xⁿ)/dx = n xⁿ⁻¹` para cualquier exponente `n` real.

💡 **Cómo se explica en la clase [B09-C04](../programa/clases/B09/B09-C04-reglas-de-derivacion/CLASE.md):**
- *Pasos:* regla de la potencia término a término.
- Ejercicio 7. Deriva `1/x²` con la regla del cociente y compara con la regla de la potencia en `x = 2`.
- 🎯 **Por qué importa:** La gravedad que siente un cuerpo depende de su distancia al astro: `g(r) = GM/r²`. La marea nace de que esa gravedad cambia de un lado a otro de un cuerpo extenso.

📘 **Dónde se aprende** (1 clase): [B09-C04 · Reglas de derivación](../programa/clases/B09/B09-C04-reglas-de-derivacion/CLASE.md).

### Regla de la suma

- La regla de la suma: `(f + g)′ = f′ + g′`.

💡 **Cómo se explica en la clase [B09-C04](../programa/clases/B09/B09-C04-reglas-de-derivacion/CLASE.md):**
- *Descripción textual:* se identifica la estructura exterior de la expresión (suma, producto, cociente o composición) y se aplica la regla correspondiente, repitiendo hacia adentro.
- 🎯 **Por qué importa:** La gravedad que siente un cuerpo depende de su distancia al astro: `g(r) = GM/r²`. La marea nace de que esa gravedad cambia de un lado a otro de un cuerpo extenso.

📘 **Dónde se aprende** (1 clase): [B09-C04 · Reglas de derivación](../programa/clases/B09/B09-C04-reglas-de-derivacion/CLASE.md).

### Regla de lazo cerrado de Ziegler–Nichols

- La regla de lazo cerrado de Ziegler–Nichols es una receta empírica que da, para un PID, `Kp = 0,6 K_u`, `Ti = P_u/2`, `Td = P_u/8`.

💡 **Cómo se explica en la clase [B16-C12](../programa/clases/B16/B16-C12-sintonia-de-controladores-pid/CLASE.md):**
- Aplicar la regla de lazo cerrado de Ziegler–Nichols y evaluar su respuesta.
- 🎯 **Por qué importa:** En un proyecto real, las ganancias iniciales de un lazo se eligen con pocas medidas y bajo presión de calendario: a veces no hay un modelo preciso. Hay reglas que solo piden hacer oscilar el lazo con un controlador proporcional y medir dos números.

📘 **Dónde se aprende** (1 clase): [B16-C12 · Sintonía de controladores PID](../programa/clases/B16/B16-C12-sintonia-de-controladores-pid/CLASE.md).

### Regla de Miner

- La regla de Miner suma el daño `n/N` de cada tramo de carga.

🎯 **Por qué importa (clase B85-C11):** La amplitud térmica de cada ciclo decide la vida por fatiga de soldaduras y uniones, y se reduce con inercia térmica o con calentadores. La decisión central: ¿qué amplitud de ciclo y cuántos ciclos acumula una unión en la misión, y cuánto la reduce la inercia térmica?

📘 **Dónde se aprende** (1 clase): [B85-C11 · Ciclos térmicos](../programa/clases/B85/B85-C11-ciclos-termicos/CLASE.md).

### Regla de palabras clave

- Una regla de palabras clave clasifica con listas de términos.

💡 **Cómo se explica en la clase [B131-C10](../programa/clases/B131/B131-C10-retroalimentacion-efectiva/CLASE.md):**
- La regla de palabras clave acierta `10/12 = 0,833` en el conjunto «antes» y `12/12` en «después».
- El script [comentarios.py](comentarios.py) clasifica 24 comentarios sintéticos con una regla de palabras clave, calcula la exactitud por dos vías (matriz de confusión y conteo directo) y la especificidad (comprueba que ambas exactitudes coinciden y que los comentarios de persona bajan tras reescribir).
- 🎯 **Por qué importa:** Un comentario como «muy bien» o «desastre» no dice qué hacer. La decisión central: ¿qué información da este comentario al estudiante para su próximo paso?

📘 **Dónde se aprende** (1 clase): [B131-C10 · Retroalimentación efectiva](../programa/clases/B131/B131-C10-retroalimentacion-efectiva/CLASE.md).

### Regla de selección

- La regla de selección dice qué transiciones dipolares son posibles: `ΔJ = ±1`.

💡 **Cómo se explica en la clase [B62-C01](../programa/clases/B62/B62-C01-espectros-rotacionales-de-moleculas-niveles-y-reglas-de-seleccion/CLASE.md):**
- *Descripción textual:* la geometría fija `I`, de `I` sale `B`, de `B` los niveles; la regla de selección convierte niveles en frecuencias y la temperatura reparte las poblaciones.
- Aplicar la regla de selección `ΔJ = ±1` y explicar por qué una molécula sin dipolo permanente no tiene espectro rotacional puro.
- 🎯 **Por qué importa:** Una línea de CO a 115,27 GHz no es un dato aislado: es la consecuencia de un momento de inercia. Si entiendes de dónde sale, puedes predecir líneas que nadie ha medido y reconocer cuándo una línea observada no es del CO.

📘 **Dónde se aprende** (1 clase): [B62-C01 · Espectros rotacionales de moléculas: niveles y reglas de selección](../programa/clases/B62/B62-C01-espectros-rotacionales-de-moleculas-niveles-y-reglas-de-seleccion/CLASE.md).

### Regla de Simpson

- La regla de Simpson ajusta parábolas (necesita `n` par).
- La regla de Simpson integra con parábolas.

💡 **Cómo se explica en la clase [B09-C11](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md):**
- Con `a = 30 e^{−t/20}` (exacto `570,128 m/s`) el orden de las reglas simples se ve limpio: izquierda `1,01`, derecha `0,99`, punto medio `2,00`, trapecio `2,00` y Simpson `4,00`.
- Aproximar con las reglas de Riemann, punto medio, trapecio y Simpson.
- 🎯 **Por qué importa:** Un motor entrega una aceleración que cambia con el tiempo; la maniobra cambia la velocidad del vehículo en la integral de esa aceleración durante el encendido. Los datos llegan como muestras de un acelerómetro, no como una fórmula.

📘 **Dónde se aprende** (2 clases): [B09-C11 · Integrales definidas](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md); [B44-C04 · Eficiencia cuántica espectral](../programa/clases/B44/B44-C04-eficiencia-cuantica-espectral/CLASE.md).

### Regla de validación

- Una regla de validación es una condición que un registro debe cumplir.

💡 **Cómo se explica en la clase [B13-C19](../programa/clases/B13/B13-C19-metadatos-y-registros-de-calibracion/CLASE.md):**
- Escribir reglas de validación: campos, fechas, vigencia, patrones, `U = k u`.
- 🎯 **Por qué importa:** Dentro de un año alguien usará los datos de un fotodiodo calibrado hoy. Necesitará saber con qué patrones, a qué temperatura, con qué incertidumbre y hasta cuándo es válida la calibración.

📘 **Dónde se aprende** (1 clase): [B13-C19 · Metadatos y registros de calibración](../programa/clases/B13/B13-C19-metadatos-y-registros-de-calibracion/CLASE.md).

### Regla del cociente

- La regla del cociente: `(f/g)′ = (f′g − fg′)/g²`.

💡 **Cómo se explica en la clase [B09-C04](../programa/clases/B09/B09-C04-reglas-de-derivacion/CLASE.md):**
- *Descripción textual:* se identifica la estructura exterior de la expresión (suma, producto, cociente o composición) y se aplica la regla correspondiente, repitiendo hacia adentro.
- Aplicar las reglas del producto y del cociente.
- 🎯 **Por qué importa:** La gravedad que siente un cuerpo depende de su distancia al astro: `g(r) = GM/r²`. La marea nace de que esa gravedad cambia de un lado a otro de un cuerpo extenso.

📘 **Dónde se aprende** (1 clase): [B09-C04 · Reglas de derivación](../programa/clases/B09/B09-C04-reglas-de-derivacion/CLASE.md).

### Regla del octeto

- La regla del octeto dice que muchos átomos tienden a rodearse de ocho electrones; el hidrógeno, de dos.

🎯 **Por qué importa (clase B06-C04):** Las muestras del asteroide Bennu contienen amoníaco, pero en gran parte no como gas libre: los autores concluyen que la mayor parte probablemente quedó retenida como sales o ligada a minerales arcillosos y a materia orgánica, porque el amoníaco libre es muy volátil y se pierde (S1).

📘 **Dónde se aprende** (1 clase): [B06-C04 · Enlaces iónicos y covalentes](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md).

### Regla del producto

- La regla del producto: `(fg)′ = f′g + fg′`.

💡 **Cómo se explica en la clase [B09-C04](../programa/clases/B09/B09-C04-reglas-de-derivacion/CLASE.md):**
- La regla de la cadena es una transmisión de engranajes: si la rueda `x` hace girar la `u` a razón `g′` y la `u` hace girar la `y` a razón `f′`, la razón total es el producto.
- *Descripción textual:* se identifica la estructura exterior de la expresión (suma, producto, cociente o composición) y se aplica la regla correspondiente, repitiendo hacia adentro.
- 🎯 **Por qué importa:** La gravedad que siente un cuerpo depende de su distancia al astro: `g(r) = GM/r²`. La marea nace de que esa gravedad cambia de un lado a otro de un cuerpo extenso.

📘 **Dónde se aprende** (1 clase): [B09-C04 · Reglas de derivación](../programa/clases/B09/B09-C04-reglas-de-derivacion/CLASE.md).

### Regla del punto izquierdo (derecho)

- La regla del punto izquierdo (derecho) toma `f` en el extremo izquierdo (derecho) de cada subintervalo.

🎯 **Por qué importa (clase B09-C11):** Un motor entrega una aceleración que cambia con el tiempo; la maniobra cambia la velocidad del vehículo en la integral de esa aceleración durante el encendido. Los datos llegan como muestras de un acelerómetro, no como una fórmula.

📘 **Dónde se aprende** (1 clase): [B09-C11 · Integrales definidas](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md).

### Regla del punto medio

- La regla del punto medio la toma en el centro.

💡 **Cómo se explica en la clase [B09-C11](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md):**
- Con `a = 30 sin(πt/60)` y `Δv = 1145,92 m/s` exacto, el error de cada regla con `n = 4, 8, …, 64` baja así: punto medio `29,99 → 0,115`; trapecio `59,52 → 0,230`;
- Con `a = 30 e^{−t/20}` (exacto `570,128 m/s`) el orden de las reglas simples se ve limpio: izquierda `1,01`, derecha `0,99`, punto medio `2,00`, trapecio `2,00` y Simpson `4,00`.
- 🎯 **Por qué importa:** Un motor entrega una aceleración que cambia con el tiempo; la maniobra cambia la velocidad del vehículo en la integral de esa aceleración durante el encendido. Los datos llegan como muestras de un acelerómetro, no como una fórmula.

📘 **Dónde se aprende** (1 clase): [B09-C11 · Integrales definidas](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md).

### Regla del trapecio

- La regla del trapecio une los puntos con rectas.
- La regla del trapecio promedia los extremos de un intervalo;
- La regla del trapecio integra el par en ejes inerciales.

💡 **Cómo se explica en la clase [B09-C11](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md):**
- Con `a = 30 sin(πt/60)` y `Δv = 1145,92 m/s` exacto, el error de cada regla con `n = 4, 8, …, 64` baja así: punto medio `29,99 → 0,115`; trapecio `59,52 → 0,230`;
- Para este pulso, izquierda y derecha dan igual que el trapecio porque `a = 0` en ambos extremos: es un caso particular, no una regla general.
- 🎯 **Por qué importa:** Un motor entrega una aceleración que cambia con el tiempo; la maniobra cambia la velocidad del vehículo en la integral de esa aceleración durante el encendido. Los datos llegan como muestras de un acelerómetro, no como una fórmula.

📘 **Dónde se aprende** (3 clases): [B09-C11 · Integrales definidas](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md); [B11-C06 · Método de Heun](../programa/clases/B11/B11-C06-metodo-de-heun/CLASE.md); [B87-C20 · Simulación ADCS integral](../programa/clases/B87/B87-C20-simulacion-adcs-integral/CLASE.md).

### Regla estándar

- Una regla estándar es una longitud conocida.

💡 **Cómo se explica en la clase [B26-C17](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md):**
- Eisenstein y colaboradores midieron en `46 748` galaxias rojas luminosas de SDSS (`3816 deg²`, `0,16 < z < 0,47`) un pico en la función de correlación a una separación de unos `100 h⁻¹ Mpc`, que usaron como regla estándar para medir distancias con una precisión de unos `4 %` a `z = 0,35` y `z = 1089` (S3, resumen).
- Interpretar el papel de las BAO como regla estándar.
- 🎯 **Por qué importa:** Los grandes sondeos de galaxias miden cómo se agrupan, y de su agrupamiento salen la densidad de materia y la historia de la expansión. Para interpretarlos hace falta saber cómo crece una fluctuación y qué distancia angular corresponde a una escala física.

📘 **Dónde se aprende** (1 clase): [B26-C17 · Estructura cosmológica](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md).

### Regla k de m

- Retardo de detección: muestras hasta alertar. Regla k de m: al menos k de m muestras superan el umbral.

💡 **Cómo se explica en la clase [B48-C23](../programa/clases/B48/B48-C23-observabilidad-del-software-de-observatorio-registros-metricas-y-alertas/CLASE.md):**
- La regla de una sola muestra detecta en 1,19 muestras, pero con falsa alarma de 2,28 % por muestra, unas 200 veces mayor que la de la regla 3 de 5 por ventana.
- La regla 3 de 5 cuesta unas 2,4 muestras de retardo adicional a cambio de reducir las falsas alarmas en dos órdenes de magnitud.
- 🎯 **Por qué importa:** Demasiadas falsas alarmas se ignoran; muy pocas dejan las averías sin ver. La decisión central: ¿qué regla de alerta equilibra falsas alarmas y retardo?

📘 **Dónde se aprende** (1 clase): [B48-C23 · Observabilidad del software de observatorio: registros, métricas y alertas](../programa/clases/B48/B48-C23-observabilidad-del-software-de-observatorio-registros-metricas-y-alertas/CLASE.md).
