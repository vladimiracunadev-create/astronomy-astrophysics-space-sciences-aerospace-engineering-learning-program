# Términos · D (parte 2 de 2)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · **D** · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-d.md) · **2**

### Dimensión

- La dimensión de una magnitud indica de qué unidades base depende y con qué exponentes.
- Una dimensión es la naturaleza de la magnitud expresada con las magnitudes base: la dimensión de la velocidad es longitud / tiempo, sea cual sea la unidad que uses.
- La dimensión es el número de vectores de cualquier base.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C06](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md):**
- F --> C{"¿Ambos lados tienen la misma dimensión?"}
- *Descripción textual:* las unidades base generan las derivadas; estas aparecen en una fórmula; una pregunta decide si ambos lados tienen la misma dimensión: si sí, la fórmula es coherente; si no, hay un error.
- 🎯 **Por qué importa:** El 23 de septiembre de 1999 la NASA perdió contacto con la sonda Mars Climate Orbiter. Según la agencia, un error de navegación se debió a no traducir unidades inglesas a métricas: el programa en tierra usaba unas y el de la nave otras, y la sonda pasó demasiado cerca de Marte y se quemó en su atmósfera (S1).

📘 **Dónde se aprende** (5 clases): [B03-C06 · Unidades del Sistema Internacional](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md); [B05-C01 · Magnitudes físicas y dimensiones](../programa/clases/B05/B05-C01-magnitudes-fisicas-y-dimensiones/CLASE.md); [B10-C02 · Bases y dimensión](../programa/clases/B10/B10-C02-bases-y-dimension/CLASE.md); [B13-C02 · Dimensiones y trazabilidad](../programa/clases/B13/B13-C02-dimensiones-y-trazabilidad/CLASE.md); [B14-C04 · Unidades y constantes con Astropy](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md).

### Dimensionalmente consistente

- Una ecuación es dimensionalmente consistente si ambos miembros tienen el mismo vector y solo se suman términos de igual dimensión.

🎯 **Por qué importa (clase B13-C02):** Un satélite recibe un comando con un tiempo de encendido de motor; el ingeniero de tierra usó una fórmula del periodo orbital copiada de una hoja de cálculo. Si la fórmula está mal dimensionada, el resultado sale en «segundos al cuadrado» o en «metros por segundo» sin que nadie lo note.

📘 **Dónde se aprende** (1 clase): [B13-C02 · Dimensiones y trazabilidad](../programa/clases/B13/B13-C02-dimensiones-y-trazabilidad/CLASE.md).

### Dimensiones

- Las dimensiones de una magnitud son sus bases (longitud L, tiempo T, masa M); el análisis dimensional comprueba que ambos lados de una ecuación tengan las mismas dimensiones.

💡 **Cómo se explica en la clase [B01-C08](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md):**
- Antes de calcular, comprueba dimensiones.
- ⚠️ **Error frecuente:** Fórmulas con dimensiones incorrectas. Ejercicios 3 y 10.
- 🎯 **Por qué importa:** En 1999 se perdió la sonda Mars Climate Orbiter por una discrepancia entre unidades inglesas y métricas (C04, fuente NASA). La ciencia estaba bien; la conversión, no.

📘 **Dónde se aprende** (1 clase): [B01-C08 · Mediciones y unidades astronómicas](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md).

### DIMM

- Parámetro de Fried `r₀`: diámetro de coherencia de la turbulencia. DIMM: monitor de movimiento diferencial de imagen.

🎯 **Por qué importa (clase B48-C12):** Sin medir el seeing, no se sabe si una noche sirve para un programa. La decisión central: ¿cuántas medidas hacen falta para que `r₀` tenga una incertidumbre aceptable?

📘 **Dónde se aprende** (1 clase): [B48-C12 · Monitorización de seeing](../programa/clases/B48/B48-C12-monitorizacion-de-seeing/CLASE.md).

### Dinámica

- La dinámica es la de Euler (C17) con tensor de inercia completo.

💡 **Cómo se explica en la clase [B16-C20](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md):**
- La cinemática `q̇ = ½ q ⊗ [0, ω]` conserva la norma de `q` de forma exacta en tiempo continuo; la dinámica es `J ω̇ = −ω × (J ω) + u`.
- 🎯 **Por qué importa:** Un telescopio debe girar desde una orientación a otra y quedarse allí. Con tres ejes acoplados y rotaciones grandes, ni los ángulos de Euler (tienen singularidades y dependen de la secuencia de giros) ni el modelo lineal bastan.

📘 **Dónde se aprende** (1 clase): [B16-C20 · Control de orientación en un simulador](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md).

### Dinamo

- La dinamo es la conversión de energía cinética de un fluido conductor en energía magnética.

💡 **Cómo se explica en la clase [B65-C02](../programa/clases/B65/B65-C02-dinamos-planetarias-y-campos-magneticos-de-origen-interno/CLASE.md):**
- Un dínamo de bicicleta convierte movimiento en electricidad; una dinamo planetaria es un dínamo cuyo campo lo produce el propio fluido en movimiento.
- Límite: son escalas, no una simulación de dinamo.
- ⚠️ **Error frecuente:** Confundir `Rm` grande con la existencia de dinamo. Se corrige con la sección 6: `Rm` es una condición necesaria, no suficiente.
- 🎯 **Por qué importa:** La presencia o ausencia de un campo global dice si un cuerpo tiene un fluido conductor en movimiento. La decisión central: ¿qué intensidad de campo permite un núcleo y cuánto duraría ese campo si el movimiento se detuviera?

📘 **Dónde se aprende** (1 clase): [B65-C02 · Dinamos planetarias y campos magnéticos de origen interno](../programa/clases/B65/B65-C02-dinamos-planetarias-y-campos-magneticos-de-origen-interno/CLASE.md).

### Dioptría

- La dioptría (D) es 1/m.

💡 **Cómo se explica en la clase [B105-C05](../programa/clases/B105/B105-C05-cambios-de-vision/CLASE.md):**
- Equivalente textual: 0,37 mm de acortamiento equivalen a una dioptría.
- 🎯 **Por qué importa:** Una variación de décimas de milímetro puede cambiar la refracción en fracciones de dioptría y comparar eso con el error de medida decide si un cambio es real. La decisión central: ¿cuántos milímetros de acortamiento equivalen a una dioptría y cuántas personas la superarían?

📘 **Dónde se aprende** (1 clase): [B105-C05 · Cambios de visión](../programa/clases/B105/B105-C05-cambios-de-vision/CLASE.md).

### Dipolo

- Un dipolo son dos cargas opuestas muy próximas.
- El dipolo es la anisotropía `1 + d cos θ`.
- El dipolo es el campo de orden más bajo.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C15](../programa/clases/B05/B05-C15-campos-electricos/CLASE.md):**
- Un dipolo de separación `d` y carga `e`, a una distancia `r ≫ d` sobre su eje, da `E ≈ 2 k_e p/r³` con `p = e d`: decae más rápido (`1/r³`) que una carga sola.
- ⚠️ **Error frecuente:** Aplicar `1/r²` a un dipolo. Ejercicio 10.
- 🎯 **Por qué importa:** El espacio está lleno de partículas cargadas que un satélite atraviesa, y un satélite puede acumular carga. La pregunta motivadora es: ¿cómo describir la fuerza eléctrica sobre una carga sin conocer a la vez todas las demás, y cuánto más fuerte es que la gravedad?

📘 **Dónde se aprende** (5 clases): [B05-C15 · Campos eléctricos](../programa/clases/B05/B05-C15-campos-electricos/CLASE.md); [B28-C04 · Rayos cósmicos de alta energía](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md); [B30-C15 · Magnetosfera terrestre](../programa/clases/B30/B30-C15-magnetosfera-terrestre/CLASE.md); [B49-C01 · Antenas de hilo: dipolo, monopolo e impedancia de radiación](../programa/clases/B49/B49-C01-antenas-de-hilo-dipolo-monopolo-e-impedancia-de-radiacion/CLASE.md); [B87-C16 · Detumbling después del despliegue](../programa/clases/B87/B87-C16-detumbling-despues-del-despliegue/CLASE.md).

### Dipolo de enlace

- Un dipolo de enlace es el desplazamiento de carga en un enlace polar, representado como un vector.

💡 **Cómo se explica en la clase [B06-C05](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md):**
- En el agua angular con 104,48°, la suma tiene módulo `2 cos(52,24°) = 1,2247` (en unidades del dipolo de enlace): molécula polar.
- 🎯 **Por qué importa:** El dióxido de carbono es el 95,1 % de la atmósfera de Marte en volumen (S2), y los hielos de las nubes densas del medio interestelar contienen, según un estudio con el telescopio James Webb, agua y CO₂ entre otras especies (S3, que se leyó sólo en resumen).

📘 **Dónde se aprende** (1 clase): [B06-C05 · Moléculas y geometría molecular](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md).

### Dipolo magnético en rotación

- El dipolo magnético en rotación pierde energía por radiación dipolar.

🎯 **Por qué importa (clase B27-C05):** Un púlsar da, a la vez, un reloj de precisión, la medida de su campo magnético y, en una binaria, la masa de las estrellas y una prueba de la relatividad general. La decisión central: dados el periodo y su derivada, ¿qué campo, edad y potencia de frenado tiene el púlsar y qué se aprende de su binaria?

📘 **Dónde se aprende** (1 clase): [B27-C05 · Púlsares y relojes naturales](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md).

### Dipolo residual

- El dipolo residual da `τ_m = m_res B`.

💡 **Cómo se explica en la clase [B87-C18](../programa/clases/B87/B87-C18-estabilidad-ante-perturbaciones/CLASE.md):**
- El dipolo residual domina con estos valores de ejemplo (`m_res = 0,01 A·m²`); si el dipolo fuera diez veces menor, el gradiente de gravedad mandaría.
- A `500 km`, con `I = diag(0,35; 0,40; 0,30)`: gradiente de gravedad `184 nN·m`, resistencia `19,1 nN·m`, presión solar `4,10 nN·m` y dipolo residual `498 nN·m`.
- 🎯 **Por qué importa:** El presupuesto de par decide el tamaño de las ruedas y de los magnetopares. La decisión central: ¿qué perturbación domina, qué error permanente deja en el lazo y se mantiene la estabilidad?

📘 **Dónde se aprende** (1 clase): [B87-C18 · Estabilidad ante perturbaciones](../programa/clases/B87/B87-C18-estabilidad-ante-perturbaciones/CLASE.md).

### Dirección

- Su dirección `φ` se mide desde la velocidad (0 = tangencial).

💡 **Cómo se explica en la clase [B75-C22](../programa/clases/B75/B75-C22-modelos-de-primer-impulso/CLASE.md):**
- *Descripción textual:* El impulso y su dirección dan el vector velocidad; de él salen la energía y el momento, los elementos y el apoapsis; el semieje da el tiempo hasta el apoapsis.
- Analogía: lanzar una piedra a una altura: se alcanza más alto lanzando en la dirección óptima.
- 🎯 **Por qué importa:** Antes de optimizar toda la misión conviene entender el primer impulso. La decisión central: ¿qué módulo y qué dirección del primer impulso alcanzan un radio dado con el menor delta-v y en cuánto tiempo?

📘 **Dónde se aprende** (1 clase): [B75-C22 · Modelos de primer impulso](../programa/clases/B75/B75-C22-modelos-de-primer-impulso/CLASE.md).

### Dirección de azimut

- La dirección de azimut es la de vuelo; el alcance oblicuo `R` es la distancia al blanco.

🎯 **Por qué importa (clase B69-C01):** Sin el principio Doppler, la resolución en azimut de un radar quedaría fijada por el ancho del haz de la antena: a 850 km, una antena de 12 m (λ = 0,0555 m) iluminaría una franja de unos 3,9 km. La decisión central: ¿qué resolución obtiene el sistema, de qué depende y qué hay que muestrear para no perderla?

📘 **Dónde se aprende** (1 clase): [B69-C01 · Principio Doppler y resolución en azimut del SAR](../programa/clases/B69/B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md).

### Dirección de máximo crecimiento

- La dirección de máximo crecimiento es `∇f/|∇f|` y el ritmo máximo es `|∇f|`.

🎯 **Por qué importa (clase B09-C17):** La gravedad no es un número: es un vector que apunta a un lado y tiene una magnitud. En un campo con dos cuerpos, como Tierra–Luna, esa dirección cambia de punto a punto.

📘 **Dónde se aprende** (1 clase): [B09-C17 · Gradiente y derivada direccional](../programa/clases/B09/B09-C17-gradiente-y-derivada-direccional/CLASE.md).

### Direccionamiento por contenido

- El direccionamiento por contenido guarda cada objeto bajo su hash: el nombre *es* el contenido.

🎯 **Por qué importa (clase B14-C11):** Un análisis usó «la tabla de catálogo de octubre». En noviembre alguien reemplazó el archivo por otro con el mismo nombre.

📘 **Dónde se aprende** (1 clase): [B14-C11 · Control de versiones de datos](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md).

### Directa

- Una órbita es directa si `i < 90°` y retrógrada si `i > 90°`.

💡 **Cómo se explica en la clase [B04-C14](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md):**
- La componente `z` es `cos i`: positiva si `i < 90°` (directa) y negativa si `i > 90°` (retrógrada).
- E -->|"> 0"| F["Órbita directa (i < 90°)"]
- 🎯 **Por qué importa:** Una órbita no es solo una forma (C09): es una forma colocada en el espacio con una orientación. ¿Hacia dónde apunta su plano?

📘 **Dónde se aprende** (1 clase): [B04-C14 · Producto vectorial y orientación](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md).

### Directamente proporcionales

- Dos magnitudes son directamente proporcionales si su cociente `y/x` es constante: `y = kx`.

🎯 **Por qué importa (clase B03-C10):** Un panel solar en órbita de Marte no recibe la misma energía que uno en órbita de la Tierra. ¿Cuánta menos?

📘 **Dónde se aprende** (1 clase): [B03-C10 · Proporcionalidad directa e inversa](../programa/clases/B03/B03-C10-proporcionalidad-directa-e-inversa/CLASE.md).

### Directividad

- La directividad `D` es el cociente entre la intensidad máxima y la media.
- La directividad `D` es el cociente entre la intensidad de radiación máxima y la que tendría una fuente isótropa con la misma potencia radiada: `D = 4π U_max/∫U dΩ`.
- La directividad compara con una antena isótropa.

💡 **Cómo se explica en la clase [B46-C03](../programa/clases/B46/B46-C03-antenas-parabolicas/CLASE.md):**
- La directividad numérica es `134522,2` y la analítica `(πD/λ)² = 134522,3`.
- Duplicar el diámetro divide el haz por 2 y multiplica la directividad por 4.
- 🎯 **Por qué importa:** El tamaño de la antena fija a la vez la resolución y la sensibilidad. La decisión central: ¿qué diámetro y qué razón focal dan el haz y la ganancia requeridos?

📘 **Dónde se aprende** (3 clases): [B46-C03 · Antenas parabólicas](../programa/clases/B46/B46-C03-antenas-parabolicas/CLASE.md); [B49-C01 · Antenas de hilo: dipolo, monopolo e impedancia de radiación](../programa/clases/B49/B49-C01-antenas-de-hilo-dipolo-monopolo-e-impedancia-de-radiacion/CLASE.md); [B91-C01 · Fundamentos de teoría de antenas](../programa/clases/B91/B91-C01-fundamentos-de-teoria-de-antenas/CLASE.md).

### Directorio de teselas

- Un directorio de teselas dice dónde empieza cada una y cuántos bytes ocupa.

🎯 **Por qué importa (clase B14-C26):** Una escena de satélite pesa cientos de megabytes y tú necesitas un recuadro de 100 × 120 píxeles. Si el formato obliga a leer todo el archivo, gastas tiempo y ancho de banda.

📘 **Dónde se aprende** (1 clase): [B14-C26 · Formatos de datos ráster geoespaciales: GeoTIFF y COG](../programa/clases/B14/B14-C26-formatos-de-datos-raster-geoespaciales-geotiff-y-cog/CLASE.md).

### Directorio de trabajo

- El directorio de trabajo es la carpeta en la que «estás parado»; los comandos y `open()` relativos se resuelven desde ahí.

💡 **Cómo se explica en la clase [B07-C15](../programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/CLASE.md):**
- El sistema de archivos es un árbol; el directorio de trabajo es un punto marcado en él.
- T["directorio de trabajo<br/>(puede ser cualquiera)"] -.-> R
- 🎯 **Por qué importa:** Una causa muy común de «el programa no encuentra el archivo» es que la ruta funciona en el computador del autor y no en otro: se escribió con `C:\Usuarios\ana\datos\...`, o se asumió que el programa se ejecuta desde cierta carpeta.

📘 **Dónde se aprende** (1 clase): [B07-C15 · Terminal y rutas de archivos](../programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/CLASE.md).

### Directriz

- Todas cumplen la propiedad foco–directriz: hay un punto (el foco) y una recta (la directriz) tales que la distancia de cada punto de la curva al foco es `e` veces su distancia a la directriz;
- Una directriz es una recomendación.

💡 **Cómo se explica en la clase [B04-C18](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md):**
- Con la directriz `x = p/e` (si `e > 0`), todo punto `P = (r cos θ, r sen θ)` cumple `r = e (p/e − r cos θ)`, que reproduce la ecuación común: `r + e r cos θ = p`.
- 🎯 **Por qué importa:** En 2017 se descubrió un objeto que cruzaba el sistema solar con una órbita que no se cerraba: su excentricidad era mayor que 1. Eso significó que no estaba ligado al Sol: venía de fuera y se iba.

📘 **Dónde se aprende** (2 clases): [B04-C18 · Cónicas y secciones orbitales](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md); [B118-C19 · Sostenibilidad y gobernanza orbital](../programa/clases/B118/B118-C19-sostenibilidad-y-gobernanza-orbital/CLASE.md).

### Dirichlet

- Las condiciones pueden ser de Dirichlet (valor de la función), Neumann (valor de la derivada) o mixtas.

🎯 **Por qué importa (clase B11-C12):** En ingeniería espacial las condiciones suelen estar en dos extremos: una aleta térmica con temperaturas conocidas en la raíz y en la punta; una transferencia que debe partir de un punto y llegar a otro en un tiempo dado.

📘 **Dónde se aprende** (1 clase): [B11-C12 · Problemas de frontera](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md).

### Discernibilidad (DM)

- La discernibilidad (DM) mide la pérdida de información.

🎯 **Por qué importa (clase B124-C13):** Abrir datos sin proteger a las personas es un daño, y proteger sin medir es una promesa vacía. La decisión central: ¿cuánto generalizar los datos para que ninguna persona sea identificable y cuánta información se pierde?

📘 **Dónde se aprende** (1 clase): [B124-C13 · Ética de investigación y datos](../programa/clases/B124/B124-C13-etica-de-investigacion-y-datos/CLASE.md).

### Disco

- El disco es el conjunto aplanado de estrellas y gas en rotación, dividido en disco delgado y grueso según la altura y la edad.

💡 **Cómo se explica en la clase [B25-C01](../programa/clases/B25/B25-C01-estructura-de-la-via-lactea/CLASE.md):**
- Es una estimación de orden de magnitud: el disco no es esférico, así que la masa real dentro de `R₀` difiere algo.
- El disco delgado contiene las estrellas jóvenes y el gas; el grueso, estrellas más viejas y a mayor altura (escala de longitud `2,0 ± 0,2 kpc` y masa `6 ± 3 × 10⁹ M☉`, S3); el halo estelar, las más viejas y pobres en metales (C17).
- ⚠️ **Error frecuente:** Pensar que la galaxia es un disco rígido. Se corrige con el ejercicio 11 (periodos) y con C08.
- 🎯 **Por qué importa:** Estamos dentro de la galaxia y no podemos fotografiarla desde fuera: su forma se reconstruye midiendo distancias y velocidades desde un punto que no es el centro. Sin un esquema claro de componentes (bulbo, barra, disco, halo) y de cifras de referencia, el resto del bloque carece de escala.

📘 **Dónde se aprende** (1 clase): [B25-C01 · Estructura de la Vía Láctea](../programa/clases/B25/B25-C01-estructura-de-la-via-lactea/CLASE.md).

### Disco de Airy

- El disco de Airy es la imagen de una fuente puntual de una apertura circular, con FWHM `1,029 λ/D`.
- El disco de Airy es la imagen de un punto limitada por difracción.

💡 **Cómo se explica en la clase [B42-C05](../programa/clases/B42/B42-C05-patrones-de-airy/CLASE.md):**
- Como una piedra en un estanque circular: un pico central y anillos que se apagan; el disco de Airy es el primer anillo oscuro.
- Con `D = 8 m` y `λ = 2,2 µm` (ilustrativos) `λ/D = 0,05672 arcsec`; el primer cero está en `1,2197 λ/D`, el FWHM en `1,0290 λ/D` y el disco de Airy encierra el `83,78 %`.
- 🎯 **Por qué importa:** El patrón de Airy es el límite de resolución de cualquier telescopio sin atmósfera. La decisión central: ¿cuánto vale la resolución de una apertura circular y qué fracción de la luz queda en el disco central?

📘 **Dónde se aprende** (4 clases): [B41-C12 · Difracción y límite de Rayleigh](../programa/clases/B41/B41-C12-difraccion-y-limite-de-rayleigh/CLASE.md); [B42-C05 · Patrones de Airy](../programa/clases/B42/B42-C05-patrones-de-airy/CLASE.md); [B44-C17 · Escala de imagen y muestreo](../programa/clases/B44/B44-C17-escala-de-imagen-y-muestreo/CLASE.md); [B121-C02 · Licenciamiento de actividades de teledetección](../programa/clases/B121/B121-C02-licenciamiento-de-actividades-de-teledeteccion/CLASE.md).

### Disco de Miyamoto–Nagai

- El disco de Miyamoto–Nagai `Φ = −GM/√(R² + (a + √(z² + b²))²)`.

🎯 **Por qué importa (clase B38-C05):** Toda simulación de estrellas necesita una fuerza. La decisión central: ¿qué potencial simple reproduce una curva de rotación plana y cuánto aporta cada componente?

📘 **Dónde se aprende** (1 clase): [B38-C05 · Potenciales galácticos: Plummer, Miyamoto-Nagai y NFW](../programa/clases/B38/B38-C05-potenciales-galacticos-plummer-miyamoto-nagai-y-nfw/CLASE.md).

### Disco delgado

- El disco delgado es geométricamente delgado y estacionario.

🎯 **Por qué importa (clase B27-C10):** Un disco convierte hasta una fracción grande de `Ṁc²` en luz; su temperatura, que baja hacia fuera, decide en qué banda se ve (rayos X en un agujero estelar, ultravioleta en uno supermasivo). La decisión central: ¿cuánto vale la temperatura en cada radio y qué luminosidad produce una tasa de acreción dada?

📘 **Dónde se aprende** (1 clase): [B27-C10 · Discos de acreción](../programa/clases/B27/B27-C10-discos-de-acrecion/CLASE.md).

### Disco exponencial delgado

- Un disco exponencial delgado tiene `Σ(R) = Σ₀e^{−R/R_d}`.

💡 **Cómo se explica en la clase [B25-C08](../programa/clases/B25/B25-C08-curvas-de-rotacion-de-galaxias/CLASE.md):**
- La fórmula de Freeman para un disco exponencial delgado es `v² = 4πGΣ₀R_d y² [I₀(y)K₀(y) − I₁(y)K₁(y)]`, con `y = R/(2R_d)`.
- 🎯 **Por qué importa:** Si la masa estuviera donde brilla, la velocidad de rotación debería caer en las afueras de una galaxia, como la de los planetas lejanos del Sol. Que una curva de rotación se mantenga plana indica más masa de la que se ve.

📘 **Dónde se aprende** (1 clase): [B25-C08 · Curvas de rotación de galaxias](../programa/clases/B25/B25-C08-curvas-de-rotacion-de-galaxias/CLASE.md).

### Disco pequeño

- El disco pequeño es la aproximación en la que la gaussiana es casi constante en el disco.

💡 **Cómo se explica en la clase [B118-C06](../programa/clases/B118/B118-C06-probabilidad-de-colision/CLASE.md):**
- Caso A (miss 200 m, `σ` 150 × 100 m, `R` 10 m): cuadratura `1,3693 × 10⁻³`; disco pequeño `1,3704 × 10⁻³`; relación `0,9992`.
- A --> C["Disco pequeño<br/>R²/(2σxσy) e^(-miss²/2σx²)"]
- ⚠️ **Error frecuente:** Aplicar el disco pequeño cuando `R` no es pequeño frente a `σ`. Se corrige con la comparación de 8.2.
- 🎯 **Por qué importa:** Las alertas se priorizan por `Pc`, pero ese número depende de la covarianza que se suponga. La decisión central: ¿cuándo es fiable una `Pc` y cuándo es baja solo porque la incertidumbre es enorme?

📘 **Dónde se aprende** (1 clase): [B118-C06 · Probabilidad de colisión](../programa/clases/B118/B118-C06-probabilidad-de-colision/CLASE.md).

### Discontinuidad

- Si falla, hay una discontinuidad: removible (el límite existe pero no coincide con `f(a)` o `f(a)` no existe), de salto (existen ambos límites laterales y son distintos) o infinita (la función crece sin cota).

💡 **Cómo se explica en la clase [B09-C02](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md):**
- Aplicar el TVI a un intervalo con discontinuidad produce conclusiones falsas.
- Cada tipo de discontinuidad es una razón para levantarlo: un hueco (removible), un salto de nivel (salto) o una subida al infinito (infinita).
- 🎯 **Por qué importa:** Un vehículo espacial cambia de masa de dos maneras: gradualmente, al quemar propelente, y de golpe, al soltar una etapa vacía. Un modelo de trayectoria que ignore los saltos integra mal; uno que los trate como suaves, también.

📘 **Dónde se aprende** (1 clase): [B09-C02 · Continuidad y discontinuidad](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md).

### Discontinuidad de contacto

- Una onda de choque es una discontinuidad que se propaga con compresión irreversible; una onda de rarefacción es una expansión continua; la discontinuidad de contacto separa dos gases con distinta densidad pero igual presión y velocidad.
- La onda de rarefacción, la discontinuidad de contacto y el choque son las tres ondas del tubo de Sod.

💡 **Cómo se explica en la clase [B21-C01](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md):**
- HLL supone una sola región intermedia entre las ondas extremas, por lo que ignora la discontinuidad de contacto y la difunde (S1 lo señala; para MHD ignora además las ondas de Alfvén y las lentas).
- 🎯 **Por qué importa:** Casi todo lo que fluye en el espacio —el viento solar, el gas de un disco de acreción, el gas que rodea a una nave en reentrada, la onda de choque de una eyección coronal— obedece leyes de conservación: una cantidad cambia en una región solo porque entra o sale por sus bordes.

📘 **Dónde se aprende** (2 clases): [B21-C01 · Volúmenes finitos y solucionadores de Riemann para leyes de conservación](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md); [B38-C06 · Hidrodinámica en simulaciones: SPH y métodos de malla](../programa/clases/B38/B38-C06-hidrodinamica-en-simulaciones-sph-y-metodos-de-malla/CLASE.md).

### Discrepancia

- Realidad sintética: el «sistema» simulado con errores inventados. Discrepancia: diferencia entre el modelo y la realidad.

💡 **Cómo se explica en la clase [B101-C08](../programa/clases/B101/B101-C08-gemelo-digital-para-ensayo-de-reparaciones-roboticas/CLASE.md):**
- Límite: aquí la discrepancia es solo cinemática; en un caso real hay muchas otras.
- 🎯 **Por qué importa:** Una reparación robótica no se improvisa: se ensaya. Pero un ensayo vale solo si el gemelo se parece a la realidad.

📘 **Dónde se aprende** (1 clase): [B101-C08 · Gemelo digital para ensayo de reparaciones robóticas](../programa/clases/B101/B101-C08-gemelo-digital-para-ensayo-de-reparaciones-roboticas/CLASE.md).

### Discrepancia de modelo

- La discrepancia de modelo es la diferencia entre ambos, y en una prueba honesta existe.

💡 **Cómo se explica en la clase [B22-C05](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md):**
- Paso 3 · el suelo. Al subir el ruido a `10⁻²`, el error con crimen sube a `0,19`, casi igual que el honesto (`0,226`): con mucho ruido, la discrepancia de modelo pasa a ser secundaria.
- 🎯 **Por qué importa:** Con datos reales no conoces la verdad, así que no puedes medir el error de tu inversión. Con datos sintéticos sí: tú fijas la verdad, generas los datos y miras si el método la recupera.

📘 **Dónde se aprende** (1 clase): [B22-C05 · Pruebas de inversión con datos sintéticos](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md).

### Discreta

- Es discreta si toma valores aislados y continua si toma cualquier valor de un intervalo (S1, C.2.2, nota 1).

💡 **Cómo se explica en la clase [B12-C02](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md):**
- Paso 1 · Variables. `X` discreta (pmf de 8.1), `Y` continua (8.3); se supone que `X` e `Y` son independientes (el telémetro no depende de los computadores en este modelo).
- Para responder una pregunta con una variable aleatoria hay tres caminos: sumar la pmf (discreta, exacto), integrar la densidad (continua, exacto si hay primitiva) y usar la cdf (ambos; es la más directa para «a lo sumo», «más de» y cuantiles).
- 🎯 **Por qué importa:** Casi nunca interesa *qué* resultado ocurrió, sino *un número* que resume el resultado: cuántos computadores funcionan, qué error tuvo una medición, cuántos fotones llegaron. Poner un número en cada resultado permite sumar, promediar y comparar.

📘 **Dónde se aprende** (1 clase): [B12-C02 · Variables aleatorias](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md).

### Discreto

- Un modelo es lineal si cumple superposición (lo precisa C03), invariante si sus parámetros no cambian con el tiempo, continuo si el tiempo es una variable real `t` y discreto si solo existe en instantes `kT`.

💡 **Cómo se explica en la clase [B16-C01](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md):**
- Un modelo continuo describe el fenómeno; uno discreto describe lo que ve el computador de a bordo, que mide y actúa cada `T` segundos (C02).
- 🎯 **Por qué importa:** Un telescopio espacial tiene que apuntar a una estrella y mantenerse allí. El telescopio Hubble lo hace con una desviación de no más de 0,007 segundos de arco durante al menos 24 horas (fuente S2).

📘 **Dónde se aprende** (1 clase): [B16-C01 · Modelos dinámicos y estados](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md).

### Discriminación

- La discriminación es la correlación entre acertar el ítem y el puntaje en los demás.
- La discriminación `r` mide si quienes aciertan el ítem puntúan mejor en el resto.

💡 **Cómo se explica en la clase [B130-C05](../programa/clases/B130/B130-C05-evaluacion-de-la-comprension-del-publico/CLASE.md):**
- *Descripción textual:* los dos cuestionarios dan la ganancia normalizada; el posterior da además dificultad, discriminación y fiabilidad; el remuestreo da un intervalo que dice si la categoría es estable.
- 🎯 **Por qué importa:** Saber si la divulgación funcionó exige medir la comprensión; ninguna otra clase lo trata. La decisión central: ¿qué número resume la mejora del público, y cuánto se puede confiar en que no sea azar?

📘 **Dónde se aprende** (2 clases): [B130-C05 · Evaluación de la comprensión del público](../programa/clases/B130/B130-C05-evaluacion-de-la-comprension-del-publico/CLASE.md); [B131-C08 · Evaluación formativa en el aula de astronomía](../programa/clases/B131/B131-C08-evaluacion-formativa-en-el-aula-de-astronomia/CLASE.md).

### Discriminante

- El discriminante es `Δ = b² − 4ac`.
- El hessiano es la matriz de segundas derivadas; su discriminante es `D = f_xx f_yy − f_xy²`.

💡 **Cómo se explica en la clase [B04-C02](../programa/clases/B04/B04-C02-ecuaciones-lineales-y-cuadraticas/CLASE.md):**
- El discriminante decide: `Δ > 0` da dos raíces reales distintas;
- *Descripción textual:* diagrama de decisión: plantear la incógnita con su unidad, escribir la ecuación, separar según el grado (despejar o factorizar/fórmula con el discriminante), comprobar por sustitución y unidades, y elegir la raíz con sentido físico.
- 🎯 **Por qué importa:** Una sonda desciende hacia la Luna; un instrumento cae desde una mesa de trabajo; una señal de radio viaja hasta un espejo y vuelve. En cada caso hay un número que no conoces (un tiempo, una distancia) y una relación que lo liga a otros que sí conoces.

📘 **Dónde se aprende** (2 clases): [B04-C02 · Ecuaciones lineales y cuadráticas](../programa/clases/B04/B04-C02-ecuaciones-lineales-y-cuadraticas/CLASE.md); [B09-C16 · Derivadas parciales](../programa/clases/B09/B09-C16-derivadas-parciales/CLASE.md).

### Diseño conceptual

- Un diseño conceptual fija magnitudes y balances, no planos.

🎯 **Por qué importa (clase B59-C20):** Un diseño conceptual no es un número sino un conjunto coherente. La decisión central: ¿qué potencia y qué masa necesita una planta que produce 10 t de agua al año, y qué parámetro la gobierna?

📘 **Dónde se aprende** (1 clase): [B59-C20 · Diseño conceptual de planta ISRU](../programa/clases/B59/B59-C20-diseno-conceptual-de-planta-isru/CLASE.md).

### Diseño de experimentos

- El diseño de experimentos elige los puntos de entrada donde se ejecuta el simulador.

🎯 **Por qué importa (clase B17-C04):** Un simulador de trayectoria, de aerodinámica o de transporte de radiación puede tardar minutos u horas por ejecución. Para explorar miles de combinaciones de parámetros (un análisis de sensibilidad, una propagación de incertidumbre, una optimización) no alcanza el tiempo.

📘 **Dónde se aprende** (1 clase): [B17-C04 · Modelos sustitutos (surrogates)](../programa/clases/B17/B17-C04-modelos-sustitutos-surrogates/CLASE.md).

### Diseño equilibrado

- Un diseño equilibrado tiene el mismo número de medidas por grupo.

🎯 **Por qué importa (clase B13-C14):** Ocho estaciones de seguimiento miden el mismo desfase de un reloj de referencia. Cada una repite su medida cinco veces y obtiene resultados muy parecidos entre sí, pero las estaciones discrepan entre ellas.

📘 **Dónde se aprende** (1 clase): [B13-C14 · Repetibilidad y reproducibilidad](../programa/clases/B13/B13-C14-repetibilidad-y-reproducibilidad/CLASE.md).

### Diseño inclusivo

- El diseño inclusivo busca que un producto o espacio sirva a la mayor diversidad posible de usuarios.

🎯 **Por qué importa (clase B109-C08):** Un control puesto «a la altura normal» deja fuera a quien no la alcanza. La decisión central: ¿a qué altura (o con qué ajuste) un puesto sirve al mayor número de usuarios y a quién deja fuera?

📘 **Dónde se aprende** (1 clase): [B109-C08 · Diseño inclusivo en hábitats](../programa/clases/B109/B109-C08-diseno-inclusivo-en-habitats/CLASE.md).

### Diseño longitudinal

- Un diseño longitudinal mide las mismas unidades repetidamente.

💡 **Cómo se explica en la clase [B12-C25](../programa/clases/B12/B12-C25-modelos-longitudinales-y-de-efectos-mixtos-para-muestras-pequenas/CLASE.md):**
- Aquí ignorar el agrupamiento desperdicia potencia: el diseño longitudinal es mucho más sensible al cambio en el tiempo que al nivel medio.
- 🎯 **Por qué importa:** Seis personas medidas cuatro veces dan 24 números, pero no 24 piezas de información independientes: las de una misma persona se parecen. Ignorar eso produce intervalos demasiado angostos para el nivel medio y, paradójicamente, demasiado anchos para los cambios dentro de cada persona.

📘 **Dónde se aprende** (1 clase): [B12-C25 · Modelos longitudinales y de efectos mixtos para muestras pequeñas](../programa/clases/B12/B12-C25-modelos-longitudinales-y-de-efectos-mixtos-para-muestras-pequenas/CLASE.md).

### Diseño pareado

- El diseño pareado compara a cada persona consigo misma.

🎯 **Por qué importa (clase B105-C20):** Un estudio con 6 personas solo detecta efectos grandes; sin saberlo, se concluye «no hay efecto» cuando solo no había potencia. La decisión central: ¿qué efecto mínimo puede detectar el protocolo con su `n`, y cuántas comparaciones puede permitirse?

📘 **Dónde se aprende** (1 clase): [B105-C20 · Diseño de protocolo médico simulado](../programa/clases/B105/B105-C20-diseno-de-protocolo-medico-simulado/CLASE.md).

### Diseño preliminar

- Un diseño preliminar fija arquitectura, subsistemas y presupuestos con margen.

🎯 **Por qué importa (clase B83-C20):** Cada presupuesto aislado puede cerrar y el conjunto no. La decisión central: ¿existe una masa seca que sea coherente con la potencia, las baterías, la estructura y el propelente que ella misma exige, y cabe en el límite?

📘 **Dónde se aprende** (1 clase): [B83-C20 · Diseño preliminar completo de misión](../programa/clases/B83/B83-C20-diseno-preliminar-completo-de-mision/CLASE.md).

### Diseño sin requisito

- Un requisito huérfano no tiene origen; un requisito no verificado no tiene prueba; el diseño sin requisito es *gold plating* o un requisito faltante.

🎯 **Por qué importa (clase B83-C05):** Cuando cambia un requisito, ¿qué piezas y qué pruebas hay que revisar? Sin trazabilidad, nadie lo sabe y el cambio rompe algo en silencio.

📘 **Dónde se aprende** (1 clase): [B83-C05 · Trazabilidad de requisitos](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md).

### Diseño universal

- El diseño universal busca que el entorno sirva a la mayoría sin adaptaciones posteriores.

🎯 **Por qué importa (clase B128-C01):** Un telescopio apuntado a un objeto alto pone el ocular fuera del alcance de quien está sentado o es de menor estatura, y uno apuntado a un objeto bajo lo pone incómodo para quien está de pie. La barrera no está en la persona sino en el montaje.

📘 **Dónde se aprende** (1 clase): [B128-C01 · Accesibilidad de la observación nocturna](../programa/clases/B128/B128-C01-accesibilidad-de-la-observacion-nocturna/CLASE.md).

### Disimilitud de Bray–Curtis

- La disimilitud de Bray–Curtis `1 − 2Σ mín(p, q)/(Σp + Σq)` va de 0 a 1.

💡 **Cómo se explica en la clase [B105-C11](../programa/clases/B105/B105-C11-microbioma-en-ambientes-cerrados/CLASE.md):**
- Una superficie B recibe la fracción `m` de A y el resto de una comunidad propia C: con `m = 0` la disimilitud de Bray–Curtis es 0,645; con `m = 0,75`, 0,161.
- 🎯 **Por qué importa:** Un índice de diversidad depende de la comunidad y de cuántas lecturas se obtuvieron. La decisión central: ¿qué profundidad de muestreo hace fiable un índice y cómo se cuantifica el parecido entre la piel de la tripulación y las superficies?

📘 **Dónde se aprende** (1 clase): [B105-C11 · Microbioma en ambientes cerrados](../programa/clases/B105/B105-C11-microbioma-en-ambientes-cerrados/CLASE.md).

### Disipación

- La disipación es el calor generado.
- La disipación es `Ṫ = ω·τ_m < 0` en promedio.

🎯 **Por qué importa (clase B86-C12):** Una eficiencia de `92 %` parece alta hasta que se multiplica por las demás etapas y se ve el calor que queda. Cada vatio perdido debe radiarse: el calor decide el tamaño del radiador y la potencia del ala.

📘 **Dónde se aprende** (2 clases): [B86-C12 · Eficiencia y disipación](../programa/clases/B86/B86-C12-eficiencia-y-disipacion/CLASE.md); [B87-C16 · Detumbling después del despliegue](../programa/clases/B87/B87-C16-detumbling-despues-del-despliegue/CLASE.md).

### Disipación del modo

- La disipación del modo es la suma de las unidades.

🎯 **Por qué importa (clase B85-C20):** Un presupuesto sin margen no resiste un cambio de diseño. La decisión central: ¿qué modo gobierna el caso caliente, con cuánto margen cierra y qué calentador pide el frío?

📘 **Dónde se aprende** (1 clase): [B85-C20 · Presupuesto térmico de carga útil](../programa/clases/B85/B85-C20-presupuesto-termico-de-carga-util/CLASE.md).

### Disipativo

- Un método es disipativo si reduce la energía y antidisipativo si la aumenta.

💡 **Cómo se explica en la clase [B11-C10](../programa/clases/B11/B11-C10-conservacion-de-energia-numerica/CLASE.md):**
- También lineal en el número de vueltas, y con signo negativo (disipativo): el análisis de C09 lo anticipaba, porque `|R| = 1 − y⁶/144 < 1` sobre el eje imaginario.
- 🎯 **Por qué importa:** Un análisis de misión puede necesitar propagar un satélite durante años, es decir, decenas de miles de vueltas. Si cada vuelta añade o quita un poco de energía, la altura de la órbita cambia solo por culpa del programa.

📘 **Dónde se aprende** (1 clase): [B11-C10 · Conservación de energía numérica](../programa/clases/B11/B11-C10-conservacion-de-energia-numerica/CLASE.md).

### Disociación

- La disociación es la ruptura de moléculas a muy alta temperatura (no modelada).
- La descomposición exotérmica libera calor; la disociación lo absorbe.

💡 **Cómo se explica en la clase [B78-C04](../programa/clases/B78/B78-C04-propulsion-monopropelente-conceptual/CLASE.md):**
- La disociación baja la masa molar, lo que favorecería el escape, pero baja más la temperatura: en este modelo el máximo está en `a = 0`.
- Descripción larga: el escape baja de forma monótona con la disociación, porque la caída de temperatura pesa más que la de la masa molar.
- ⚠️ **Error frecuente:** Olvidar que la disociación es endotérmica. Se corrige con 8.2.
- 🎯 **Por qué importa:** La descomposición de un monopropelente tiene dos pasos: uno que libera calor y otro que lo absorbe. La decisión central: ¿conviene que el amoníaco intermedio se disocie del todo, por la menor masa molar, o que se conserve, por la mayor temperatura?

📘 **Dónde se aprende** (2 clases): [B78-C04 · Propulsión monopropelente conceptual](../programa/clases/B78/B78-C04-propulsion-monopropelente-conceptual/CLASE.md); [B79-C14 · Propiedades de gases calientes](../programa/clases/B79/B79-C14-propiedades-de-gases-calientes/CLASE.md).

### Disolución

- Una disolución es una mezcla homogénea de un soluto en un disolvente; en esta clase, el disolvente es el agua.

💡 **Cómo se explica en la clase [B06-C15](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md):**
- Una disolución ácida no puede ser básica por mucho que se diluya.
- 🎯 **Por qué importa:** El extracto en agua caliente de las muestras de Bennu contiene amoníaco libre en unos 13,6 μmol por gramo y ácido fórmico en 4,106 μmol por gramo (S1). Un ácido y una base en el mismo líquido reaccionan entre sí: el ácido cede un protón, la base lo acepta y se forman iones.

📘 **Dónde se aprende** (1 clase): [B06-C15 · Ácidos, bases y soluciones](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md).

### Disolvente

- Una disolución es una mezcla homogénea de un soluto en un disolvente; en esta clase, el disolvente es el agua.

🎯 **Por qué importa (clase B06-C15):** El extracto en agua caliente de las muestras de Bennu contiene amoníaco libre en unos 13,6 μmol por gramo y ácido fórmico en 4,106 μmol por gramo (S1). Un ácido y una base en el mismo líquido reaccionan entre sí: el ácido cede un protón, la base lo acepta y se forman iones.

📘 **Dónde se aprende** (1 clase): [B06-C15 · Ácidos, bases y soluciones](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md).

### Disparidad

- La disparidad `d` es la diferencia de posición del punto en las dos imágenes, en píxeles.
- La disparidad `d` es el desplazamiento horizontal de un punto entre las dos imágenes.

💡 **Cómo se explica en la clase [B97-C04](../programa/clases/B97/B97-C04-vision-estereoscopica/CLASE.md):**
- Con `200 000` muestras de disparidad ruidosa (semilla fija), la desviación de `Z` es `0,05944` m frente a `0,05952` m teóricos (diferencia relativa `1,37e-03`).
- *Descripción textual:* de la disparidad y la geometría sale la profundidad; el ruido de disparidad produce un error que crece con `Z²`, y eso define el alcance útil.
- ⚠️ **Error frecuente:** Confundir disparidad con profundidad. Son inversas (8.1)
- 🎯 **Por qué importa:** Un rover decide si un obstáculo está a 3 m o a 8 m con estas cámaras. Sin saber cómo crece el error con la distancia, se confía en una profundidad de 30 m que puede tener varios metros de incertidumbre.

📘 **Dónde se aprende** (2 clases): [B97-C04 · Visión estereoscópica](../programa/clases/B97/B97-C04-vision-estereoscopica/CLASE.md); [B103-C03 · Mapas de profundidad y correspondencia estéreo](../programa/clases/B103/B103-C03-mapas-de-profundidad-y-correspondencia-estereo/CLASE.md).

### Disparo

- El disparo integra desde el centro y ajusta `ω²` para cumplir la frontera.

💡 **Cómo se explica en la clase [B37-C07](../programa/clases/B37/B37-C07-oscilaciones-radiales-y-relacion-periodo-densidad-media/CLASE.md):**
- Todas las cotas variacionales están por encima del valor del disparo y convergen a él.
- E["Sturm-Liouville radial"] --> D["disparo: w(R)=0"]
- 🎯 **Por qué importa:** El período fundamental fija la densidad media. La decisión central: ¿cuánto vale el período de un modo radial y cómo escala con la densidad?

📘 **Dónde se aprende** (1 clase): [B37-C07 · Oscilaciones radiales y relación período-densidad media](../programa/clases/B37/B37-C07-oscilaciones-radiales-y-relacion-periodo-densidad-media/CLASE.md).

### Disparo múltiple

- El disparo múltiple divide el tiempo en `m` tramos: las incógnitas son `v₀` y los estados de los nodos, y las ecuaciones son los defectos de continuidad (fin de un tramo menos inicio del siguiente) más la condición final.

💡 **Cómo se explica en la clase [B81-C02](../programa/clases/B81/B81-C02-metodo-de-disparo-para-control-optimo/CLASE.md):**
- Límite: el disparo múltiple necesita estimar los nodos; con malas semillas también puede fallar.
- El disparo múltiple con 8 tramos converge en 3, 4 y 5 iteraciones, siempre que los nodos se siembren con un conocimiento previo del 3 % de error.
- 🎯 **Por qué importa:** El disparo simple falla cuando la trayectoria es muy sensible a la velocidad inicial; el múltiple reparte el problema en tramos. La decisión central: ¿cuándo basta un solo disparo y cuándo hay que dividir la trayectoria?

📘 **Dónde se aprende** (1 clase): [B81-C02 · Método de disparo para control óptimo](../programa/clases/B81/B81-C02-metodo-de-disparo-para-control-optimo/CLASE.md).

### Disparo simple

- El disparo simple integra desde `v₀` y corrige con Newton usando `∂r_f/∂v₀ = Φ_rv`.

💡 **Cómo se explica en la clase [B81-C02](../programa/clases/B81/B81-C02-metodo-de-disparo-para-control-optimo/CLASE.md):**
- *Descripción textual:* el disparo simple repite integrar, medir el error final y corregir `v₀` con Newton; el múltiple hace lo mismo sobre `v₀` y los nodos con defectos de continuidad.
- Con 120 d el disparo simple converge en 4 iteraciones; con 250 d en 9; con 500 d no converge en 40.
- 🎯 **Por qué importa:** El disparo simple falla cuando la trayectoria es muy sensible a la velocidad inicial; el múltiple reparte el problema en tramos. La decisión central: ¿cuándo basta un solo disparo y cuándo hay que dividir la trayectoria?

📘 **Dónde se aprende** (1 clase): [B81-C02 · Método de disparo para control óptimo](../programa/clases/B81/B81-C02-metodo-de-disparo-para-control-optimo/CLASE.md).

### Dispensador

- El dispensador es el contenedor que expulsa al CubeSat.

💡 **Cómo se explica en la clase [B95-C01](../programa/clases/B95/B95-C01-unidad-cubesat-dimensiones-y-formatos/CLASE.md):**
- Las masas son valores típicos máximos: masas mayores pueden evaluarse caso por caso y el dispensador puede admitir menos.
- Límite: el CDS fija valores típicos y un dispensador concreto o el proveedor de lanzamiento pueden exigir menos o evaluar más caso por caso.
- 🎯 **Por qué importa:** Un CubeSat que no cumple el estándar no entra en el dispensador, aunque funcione perfectamente. La decisión central: ¿esta configuración cabe, pesa y se equilibra dentro de lo que el estándar permite, y cuándo puede encenderse, desplegar y transmitir?

📘 **Dónde se aprende** (1 clase): [B95-C01 · Unidad CubeSat, dimensiones y formatos](../programa/clases/B95/B95-C01-unidad-cubesat-dimensiones-y-formatos/CLASE.md).

### Dispersión

- La dispersión `σ_v` es su desviación típica.
- La dispersión es la variabilidad del resultado ante un error.
- La dispersión retrasa las frecuencias bajas.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B29-C17](../programa/clases/B29/B29-C17-fenomenos-transitorios-rapidos/CLASE.md):**
- La desdispersión recupera la medida de dispersión con una incertidumbre de pocos `pc/cm³` y más que duplica la relación señal-ruido.
- Un pulso real sería más ancho por la dispersión intra-canal, lo que reduce la resolución.
- 🎯 **Por qué importa:** La medida de dispersión informa de la distancia a la fuente y de la materia que atravesó. Sin desdispersión, un pulso breve se pierde entre canales.

📘 **Dónde se aprende** (5 clases): [B26-C11 · Expansión cósmica y ley de Hubble-Lemaître](../programa/clases/B26/B26-C11-expansion-cosmica-y-ley-de-hubble-lemaitre/CLASE.md); [B29-C17 · Fenómenos transitorios rápidos](../programa/clases/B29/B29-C17-fenomenos-transitorios-rapidos/CLASE.md); [B41-C14 · Aberración cromática y astigmatismo](../programa/clases/B41/B41-C14-aberracion-cromatica-y-astigmatismo/CLASE.md); [B46-C02 · Propagación de ondas de radio](../programa/clases/B46/B46-C02-propagacion-de-ondas-de-radio/CLASE.md); [B118-C13 · Desorbitación controlada](../programa/clases/B118/B118-C13-desorbitacion-controlada/CLASE.md).

### Dispersión angular

- La dispersión angular `dβ/dλ = m/(d cos β)`.
- La dispersión angular `dD/dλ`.

🎯 **Por qué importa (clase B45-C04):** La red es el elemento dispersor de casi todos los espectrógrafos. La decisión central: ¿en qué ángulo sale cada longitud de onda y qué resolución se obtiene?

📘 **Dónde se aprende** (2 clases): [B45-C04 · Redes de difracción](../programa/clases/B45/B45-C04-redes-de-difraccion/CLASE.md); [B45-C05 · Prismas y dispersión](../programa/clases/B45/B45-C05-prismas-y-dispersion/CLASE.md).

### Dispersión Compton

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C06):** Cada proceso (Compton, pares) domina a una energía distinta y fija el tipo de instrumento. La decisión central: ¿qué proceso usa el detector y con qué incertidumbre angular reconstruye la dirección?

📘 **Dónde se aprende** (1 clase): [B47-C06 · Instrumentos de rayos gamma](../programa/clases/B47/B47-C06-instrumentos-de-rayos-gamma/CLASE.md).

### Dispersión Compton inversa

- La dispersión Compton inversa transfiere energía de un electrón a un fotón.

🎯 **Por qué importa (clase B27-C21):** Los fotones de TeV que se detectan en algunos objetos proceden de este mecanismo, y la comparación entre la potencia Compton y la sincrotrón permite estimar el campo magnético. La decisión central: ¿qué energía alcanza el fotón dispersado, cuándo deja de valer la aproximación de Thomson y qué razón de potencias se espera?

📘 **Dónde se aprende** (1 clase): [B27-C21 · Dispersión Compton inversa y emisión de alta energía](../programa/clases/B27/B27-C21-dispersion-compton-inversa-y-emision-de-alta-energia/CLASE.md).

### Dispersión de aterrizaje

- La dispersión de aterrizaje es el área donde puede caer la cápsula.

💡 **Cómo se explica en la clase [B104-C14](../programa/clases/B104/B104-C14-supervivencia-en-entorno-terrestre/CLASE.md):**
- *Descripción textual:* la dispersión de aterrizaje da la distancia al equipo de rescate; el tiempo total suma alistamiento, localización (muy distinta con y sin baliza) y traslado; se compara con la autonomía.
- 🎯 **Por qué importa:** Si el rescate no llega antes de que se agoten el refugio y las provisiones, la situación se vuelve crítica. La decisión central: ¿cuánto reducen la baliza y la ubicación del rescate la probabilidad de una espera mayor que la autonomía?

📘 **Dónde se aprende** (1 clase): [B104-C14 · Supervivencia en entorno terrestre](../programa/clases/B104/B104-C14-supervivencia-en-entorno-terrestre/CLASE.md).

### Dispersión de energía

- La dispersión de energía `ΔE = GMR_*/r_t²`.

💡 **Cómo se explica en la clase [B27-C16](../programa/clases/B27/B27-C16-eventos-de-disrupcion-por-marea/CLASE.md):**
- *Descripción textual:* de la estrella y la masa del agujero se obtienen el radio de marea y la dispersión de energía; de ahí salen el tiempo mínimo y la ley de caída; igualar `r_t` con el radio de Schwarzschild da la masa de Hills.
- 🎯 **Por qué importa:** Estos eventos iluminan agujeros negros inactivos y permiten estimar su masa. Gezari revisa 56 de ellos (S3, resumen).

📘 **Dónde se aprende** (1 clase): [B27-C16 · Eventos de disrupción por marea](../programa/clases/B27/B27-C16-eventos-de-disrupcion-por-marea/CLASE.md).

### Dispersión de energía inicial

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C08):** La resolución de masa decide qué especies se separan. La decisión central: ¿qué tiempo de vuelo, qué dispersión y qué resolución permiten distinguir dos iones casi isobáricos?

📘 **Dónde se aprende** (1 clase): [B47-C08 · Espectrómetros de masas orbitales](../programa/clases/B47/B47-C08-espectrometros-de-masas-orbitales/CLASE.md).

### Dispersión de fase

- La dispersión de fase (PDM) mide cuánto varía el brillo dentro de cada bin de fase.

💡 **Cómo se explica en la clase [B29-C14](../programa/clases/B29/B29-C14-estrellas-variables-periodicas/CLASE.md):**
- La dispersión de fase en el periodo verdadero es `θ = 0,0503` y en un periodo erróneo (1,37 veces) `0,8831`: valores bajos indican fase limpia.
- *Descripción textual:* se ajusta una curva armónica para cada frecuencia y se toma el mínimo de `χ²`; la dispersión de fase da un estimador independiente; ambos coinciden y la incertidumbre de una sinusoide sigue una fórmula estándar.
- 🎯 **Por qué importa:** El periodo es la propiedad básica de una variable periódica; de él y de la forma de la curva se deducen la masa, la edad o la distancia en muchos casos. La decisión central: ¿qué periodo y qué incertidumbre da la serie y qué métodos coinciden?

📘 **Dónde se aprende** (1 clase): [B29-C14 · Estrellas variables periódicas](../programa/clases/B29/B29-C14-estrellas-variables-periodicas/CLASE.md).

### Dispersión de Thomson

- La dispersión de Thomson es la dispersión de la luz por electrones libres, con sección eficaz `σ_T`.

🎯 **Por qué importa (clase B24-C09):** Toda temperatura o composición que atribuimos a una estrella se infiere de una capa delgada. Saber de qué profundidad viene la luz, cuánto vale la opacidad y cuánto puede brillar una estrella sin expulsar su atmósfera es lo que permite interpretar espectros (C10) y entender los vientos (C17).

📘 **Dónde se aprende** (1 clase): [B24-C09 · Atmósferas y opacidades](../programa/clases/B24/B24-C09-atmosferas-y-opacidades/CLASE.md).

### Dispersión de velocidades

- La dispersión de velocidades `σ` mide la agitación de las estrellas.
- La dispersión de velocidades `σ_R` y `σ_φ` mide la agitación radial y azimutal.

🎯 **Por qué importa (clase B25-C06):** La mayoría de las estrellas nace en grupos. Los cúmulos son laboratorios: sus estrellas comparten edad, distancia y composición.

📘 **Dónde se aprende** (2 clases): [B25-C06 · Cúmulos estelares](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md); [B25-C07 · Dinámica de poblaciones estelares](../programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/CLASE.md).

### Dispersión del plasma

- La dispersión del plasma retrasa más las frecuencias bajas.

🎯 **Por qué importa (clase B28-C01):** Un solo evento, como una fusión de estrellas de neutrones, emite varios mensajeros que llegan por caminos y en momentos distintos. Entender por qué unos llegan alineados con la fuente y otros no es el primer paso para combinarlos.

📘 **Dónde se aprende** (1 clase): [B28-C01 · Fundamentos de mensajeros astronómicos](../programa/clases/B28/B28-C01-fundamentos-de-mensajeros-astronomicos/CLASE.md).

### Dispersión en la línea de visión

- La dispersión en la línea de visión `σ_los` es la desviación típica de las velocidades radiales de sus estrellas.

🎯 **Por qué importa (clase B25-C10):** Las galaxias enanas son las más abundantes y las más ricas en materia oscura según su masa dinámica; además son los sitios donde las predicciones del modelo cosmológico se ponen a prueba. Pero con pocas estrellas medidas y sin rotación ordenada, su masa depende de un estimador.

📘 **Dónde se aprende** (1 clase): [B25-C10 · Galaxias irregulares y enanas](../programa/clases/B25/B25-C10-galaxias-irregulares-y-enanas/CLASE.md).

### Dispersión intrínseca

- La dispersión intrínseca es el ancho de la relación por la franja de inestabilidad finita.

💡 **Cómo se explica en la clase [B24-C13](../programa/clases/B24/B24-C13-estrellas-variables/CLASE.md):**
- La relación depende de la metalicidad y de la dispersión intrínseca; el ajuste lineal es una aproximación; el punto cero absoluto exige distancias geométricas.
- 🎯 **Por qué importa:** Las cefeidas y otras estrellas pulsantes cumplen que cuanto más largo es el periodo, mayor es la luminosidad. Medir un periodo equivale entonces a conocer la luminosidad intrínseca y, por comparación con el brillo aparente, la distancia.

📘 **Dónde se aprende** (1 clase): [B24-C13 · Estrellas variables](../programa/clases/B24/B24-C13-estrellas-variables/CLASE.md).

### Dispersión lineal

- La dispersión lineal `d cos β/(m f_cam)` da nm por mm en el detector.

💡 **Cómo se explica en la clase [B45-C06](../programa/clases/B45/B45-C06-diseno-de-espectrografos/CLASE.md):**
- *Descripción textual:* la rendija se proyecta sobre el detector y su ancho dividido por la dispersión lineal da el ancho espectral.
- 🎯 **Por qué importa:** El diseño se decide con unos pocos parámetros que se compensan entre sí. La decisión central: ¿qué ancho de rendija da la resolución deseada y cuántos píxeles muestrean cada elemento?

📘 **Dónde se aprende** (1 clase): [B45-C06 · Diseño de espectrógrafos](../programa/clases/B45/B45-C06-diseno-de-espectrografos/CLASE.md).

### Dispersivo

- Un medio o un esquema es dispersivo si ondas de distinta `k` viajan a distinta velocidad.

🎯 **Por qué importa (clase B21-C02):** Casi toda señal que viaja en el espacio —ondas de radio, ondas de Alfvén en la corona solar, ondas sísmicas en una luna, vibraciones de una estructura— obedece alguna forma de la ecuación de onda.

📘 **Dónde se aprende** (1 clase): [B21-C02 · Ecuación de onda: esquemas y dispersión numérica](../programa/clases/B21/B21-C02-ecuacion-de-onda-esquemas-y-dispersion-numerica/CLASE.md).

### Disponibilidad

- La disponibilidad es la probabilidad de que el sitio funcione.
- La disponibilidad es `MTBF/(MTBF + MTTR)`.
- (Es la convención de este curso, didáctica.) La disponibilidad a una demanda `D` es `P(M ≥ D)`.
- *(y 7 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B28-C16](../programa/clases/B28/B28-C16-redes-internacionales-de-alertas/CLASE.md):**
- Descripción larga: la disponibilidad reduce la cobertura en un cuarto; la distribución en longitud hace casi válida la independencia.
- ⚠️ **Error frecuente:** Ignorar la disponibilidad. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** La cobertura de una red depende de su distribución geográfica, no solo del número de telescopios. La decisión central: ¿qué probabilidad hay de que, al llegar una alerta, al menos un sitio de la red pueda observar la fuente?

📘 **Dónde se aprende** (11 clases): [B28-C16 · Redes internacionales de alertas](../programa/clases/B28/B28-C16-redes-internacionales-de-alertas/CLASE.md); [B33-C09 · Planes de continuidad ante eventos de clima espacial](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md); [B48-C15 · Gestión de fallas de instrumentos](../programa/clases/B48/B48-C15-gestion-de-fallas-de-instrumentos/CLASE.md); [B59-C18 · Fiabilidad de equipos mineros](../programa/clases/B59/B59-C18-fiabilidad-de-equipos-mineros/CLASE.md); [B67-C08 · Informe de disponibilidad de volátiles con incertidumbre](../programa/clases/B67/B67-C08-informe-de-disponibilidad-de-volatiles-con-incertidumbre/CLASE.md); [B78-C22 · Ciclos de trabajo y operación de propulsión eléctrica](../programa/clases/B78/B78-C22-ciclos-de-trabajo-y-operacion-de-propulsion-electrica/CLASE.md) y 5 más.

### Disponibilidad individual

- La disponibilidad individual `p` es la probabilidad de que una persona pueda actuar.

💡 **Cómo se explica en la clase [B122-C10](../programa/clases/B122/B122-C10-planes-de-continuidad-institucional-y-de-operaciones/CLASE.md):**
- El ejemplo conductor es una institución sintética con cuatro funciones esenciales (Control de la misión `k = 3`, Seguridad de las comunicaciones `k = 2`, Comunicación de crisis `k = 1`, Soporte de TI `k = 2`), disponibilidad individual `p = 0,85` y objetivo `0,99`.
- 🎯 **Por qué importa:** No hay clase equivalente sobre continuidad de funciones institucionales. La decisión central: ¿qué dotación mínima asegura que cada función esencial se cubra con al menos el 99 %?

📘 **Dónde se aprende** (1 clase): [B122-C10 · Planes de continuidad institucional y de operaciones](../programa/clases/B122/B122-C10-planes-de-continuidad-institucional-y-de-operaciones/CLASE.md).

### Disposición

- No conformidad: producto que no cumple su requisito. Disposición: decisión sobre qué hacer.
- Disposición: retiro de la nave al final de su vida.

💡 **Cómo se explica en la clase [B90-C17](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md):**
- La regla de disposición y la estadística de esta clase son de ejemplo.
- *Descripción textual:* un hallazgo detiene la actividad y se registra; el análisis decide si el defecto es del producto o del procedimiento; la regla de severidad y repetición propone una disposición y el cierre exige evidencia.
- 🎯 **Por qué importa:** Una falla única en 500 horas de ensayo no demuestra que el equipo sea confiable: solo acota la tasa de fallas. Y una anomalía mal registrada se pierde.

📘 **Dónde se aprende** (2 clases): [B90-C17 · Gestión de anomalías de prueba](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md); [B96-C18 · Fin de vida y disposición orbital](../programa/clases/B96/B96-C18-fin-de-vida-y-disposicion-orbital/CLASE.md).

### Disposición a pagar

- La disposición a pagar (DAP) `v` es lo máximo que un cliente pagaría.

🎯 **Por qué importa (clase B125-C01):** [B124](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) trata los segmentos de la industria en general; ninguna clase explica por qué un dato crudo puede valer cero y aun así sostener empresas.

📘 **Dónde se aprende** (1 clase): [B125-C01 · Mercado de datos espaciales](../programa/clases/B125/B125-C01-mercado-de-datos-espaciales/CLASE.md).

### Disposición posmisión

- La disposición posmisión (PMD) es el conjunto de acciones para retirar o dejar segura la nave.

💡 **Cómo se explica en la clase [B118-C11](../programa/clases/B118/B118-C11-diseno-para-mitigacion-de-desechos/CLASE.md):**
- Las directrices IADC Rev. 4 (enero de 2025, consultadas) piden que la probabilidad de disposición posmisión exitosa sea al menos del 90 % con un objetivo del 99 % o más, y que en las grandes constelaciones se considere una probabilidad mayor.
- 🎯 **Por qué importa:** Una disposición solo es posible si el satélite sigue funcionando al final de su vida. La probabilidad de éxito de la PMD no es la fiabilidad de la misión, sino la de las funciones necesarias para disponer.

📘 **Dónde se aprende** (1 clase): [B118-C11 · Diseño para mitigación de desechos](../programa/clases/B118/B118-C11-diseno-para-mitigacion-de-desechos/CLASE.md).

### Dispositivo físico entre una fuente de energía y un peligro

- Inhibidor independiente: dispositivo físico entre una fuente de energía y un peligro. Cronología: secuencia de eventos con sus tiempos.

🎯 **Por qué importa (clase B90-C15):** Un mecanismo que despliega en el laboratorio con un margen justo puede quedarse a medio camino con lubricación degradada o arrastre de un arnés. La decisión central: ¿cuánto par sobra frente al arrastre y con qué velocidad llega a la traba?

📘 **Dónde se aprende** (1 clase): [B90-C15 · Pruebas de despliegue](../programa/clases/B90/B90-C15-pruebas-de-despliegue/CLASE.md).

### Distancia

- El tiempo de ida y vuelta `t` es lo que tarda el pulso; la distancia (*range*) es `R = ct/2`.

💡 **Cómo se explica en la clase [B57-C09](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md):**
- *Descripción textual:* los pulsos se promedian, se ajusta el instante de subida, se convierte en distancia y se resta a la altura del satélite.
- 🎯 **Por qué importa:** La altura del mar cambia unos milímetros por año, pero el eco de un pulso es ruidoso. La decisión central: ¿cuántos pulsos hay que promediar y cómo se ajusta el eco para que el error de distancia del ajuste se reduzca lo necesario?

📘 **Dónde se aprende** (1 clase): [B57-C09 · Altimetría satelital](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md).

### Distancia angular

- La distancia angular `c` entre dos puntos es el ángulo, medido desde el centro, entre las direcciones a ambos; la distancia de círculo máximo es `d = R c` (con `c` en radianes).
- La distancia angular `d` al borde de un agujero coronal.

💡 **Cómo se explica en la clase [B04-C16](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md):**
- *Descripción textual:* de dos puntos dados por latitud y longitud se obtienen dos caminos: el del coseno, igual al producto escalar de los vectores unitarios, y el del haversine; ambos dan la distancia angular `c`, que multiplicada por el radio da la distancia en longitud; el primero pierde precisión para `c` pequeño y el segundo no.
- ⚠️ **Error frecuente:** Confundir distancia angular con distancia en km. Se corrige con `d = R c` y el ejercicio 1.
- 🎯 **Por qué importa:** Para pasar de un lugar a otro de la Tierra, un avión sigue (casi) un círculo máximo. Para decidir cuánto debe girar un telescopio entre dos estrellas, se calcula la distancia angular sobre la esfera celeste.

📘 **Dónde se aprende** (2 clases): [B04-C16 · Geometría de esferas y círculos máximos](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md); [B33-C10 · Modelos de viento solar para pronóstico (Parker y WSA)](../programa/clases/B33/B33-C10-modelos-de-viento-solar-para-pronostico-parker-y-wsa/CLASE.md).

### Distancia cenital

- La altura `h` es el ángulo de un astro sobre el horizonte (0° horizonte, 90° cenit); la distancia cenital es `z = 90° − h`.

🎯 **Por qué importa (clase B08-C04):** Una tabla dice «Luna: AR 2,14 h, Dec +17,1°». Un telescopio, una cámara o tus ojos necesitan «a 35° de altura, hacia el nornoreste».

📘 **Dónde se aprende** (1 clase): [B08-C04 · Altura y acimut](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md).

### Distancia comóvil

- La distancia comóvil es `D_C = (c/H₀)∫dz/E`.

💡 **Cómo se explica en la clase [B26-C17](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md):**
- *Descripción textual:* las fluctuaciones crecen como `a` mientras la materia domina y más despacio después; por separado, la regla BAO se convierte en ángulo dividiéndola por la distancia comóvil.
- 🎯 **Por qué importa:** Los grandes sondeos de galaxias miden cómo se agrupan, y de su agrupamiento salen la densidad de materia y la historia de la expansión. Para interpretarlos hace falta saber cómo crece una fluctuación y qué distancia angular corresponde a una escala física.

📘 **Dónde se aprende** (4 clases): [B26-C17 · Estructura cosmológica](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md); [B26-C19 · Energía oscura y parámetros](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md); [B40-C04 · Problemas del horizonte y de la planitud](../programa/clases/B40/B40-C04-problemas-del-horizonte-y-de-la-planitud/CLASE.md); [B40-C07 · Espectro angular de potencias del CMB](../programa/clases/B40/B40-C07-espectro-angular-de-potencias-del-cmb/CLASE.md).

### Distancia comóvil transversal

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B36-C07):** Una regla estándar permite medir distancias si se conoce su longitud. La decisión central: ¿cuánto mide la regla y cuál es la precisión con que se puede medir su dilatación?

📘 **Dónde se aprende** (1 clase): [B36-C07 · Oscilaciones acústicas bariónicas como regla estándar](../programa/clases/B36/B36-C07-oscilaciones-acusticas-barionicas-como-regla-estandar/CLASE.md).

### Distancia crítica

- La distancia crítica es donde el campo directo iguala al reverberante.

💡 **Cómo se explica en la clase [B109-C10](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md):**
- Con `V = 127 m³` (Burke et al., 2022) y una superficie equivalente `6V^(2/3) = 151,6 m²` y `α = 0,20` (ilustrativos): `A = 30,3 m²`, `T60 = 0,161 V/A = 0,67 s`, `R = A/(1 − α) = 37,9 m²` y distancia crítica `√(Q R/16π) = 1,23 m` con `Q = 2`.
- Más allá de la distancia crítica alejarse apenas ayuda: de `1` a `5 m` bajan solo `3,7 dB`.
- ⚠️ **Error frecuente:** Creer que alejarse siempre baja el nivel. Se corrige con 8.3: la distancia crítica.
- 🎯 **Por qué importa:** El ruido continuo degrada la comunicación, el sueño y el trabajo aunque no dañe el oído. La decisión central: ¿qué fuente reduzco primero y cuánto baja el nivel de la cabina?

📘 **Dónde se aprende** (1 clase): [B109-C10 · Acústica y control de ruido interior](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md).

### Distancia de campo lejano

- La distancia de campo lejano `2D²/λ` es el criterio clásico para medir el patrón.

💡 **Cómo se explica en la clase [B91-C05](../programa/clases/B91/B91-C05-medicion-y-calibracion-de-antenas/CLASE.md):**
- *Descripción textual:* de `D` y `λ` sale la distancia de campo lejano; a distancias menores aparece un error de fase que deforma el patrón; la ganancia se obtiene por comparación con una referencia y su incertidumbre, por suma cuadrática.
- Una antena sintética de `D = 1,2 m` a `8,4 GHz` tiene `λ = 35,69 mm` y una distancia de campo lejano de `80,70 m`.
- 🎯 **Por qué importa:** Una antena se acepta si su ganancia y su patrón medidos cumplen la especificación dentro de una incertidumbre conocida. La decisión central: ¿a qué distancia medir y con qué incertidumbre, para poder afirmar que la antena cumple?

📘 **Dónde se aprende** (1 clase): [B91-C05 · Medición y calibración de antenas](../programa/clases/B91/B91-C05-medicion-y-calibracion-de-antenas/CLASE.md).

### Distancia de círculo máximo

- La distancia angular `c` entre dos puntos es el ángulo, medido desde el centro, entre las direcciones a ambos; la distancia de círculo máximo es `d = R c` (con `c` en radianes).

💡 **Cómo se explica en la clase [B04-C16](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md):**
- Dos puntos a 60° N con `Δλ = 160°` están a un arco de paralelo `R cos 60° × (160° en rad) = 0,5 × 2,7925 × 6371 = 8895,6 km` y a una distancia de círculo máximo `6560,2 km`.
- 🎯 **Por qué importa:** Para pasar de un lugar a otro de la Tierra, un avión sigue (casi) un círculo máximo. Para decidir cuánto debe girar un telescopio entre dos estrellas, se calcula la distancia angular sobre la esfera celeste.

📘 **Dónde se aprende** (1 clase): [B04-C16 · Geometría de esferas y círculos máximos](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md).

### Distancia de coordinación

- La distancia de coordinación `d` es el radio de esa zona en este modelo circular.

🎯 **Por qué importa (clase B120-C02):** Coordinar con otros servicios define dónde y cómo se puede operar y ninguna clase lo trata. La decisión central: ¿con qué administraciones hay que coordinar una estación terrena y en cuánto tiempo deben responder?

📘 **Dónde se aprende** (1 clase): [B120-C02 · Zonas de coordinación entre servicios radioeléctricos](../programa/clases/B120/B120-C02-zonas-de-coordinacion-entre-servicios-radioelectricos/CLASE.md).

### Distancia de falla

- La distancia de falla es el módulo del error de llegada.

💡 **Cómo se explica en la clase [B75-C18](../programa/clases/B75/B75-C18-propagacion-de-dispersion-inicial/CLASE.md):**
- Con un error de velocidad de salida de `1 m/s` por eje (sintético), la llegada a Marte se dispersa `35 155 km` en x y `70 958 km` en y (1σ), con una elipsoide de semiejes `78 512` y `10 330 km`; la distancia de falla tiene mediana `53 136 km` y percentil 95 `154 452 km`, el `14,2 %` del radio de Hill de Marte (`1 084 136 km`).
- 🎯 **Por qué importa:** Para decidir cuántas correcciones de trayectoria hacen falta hay que saber cuánto se dispersa la llegada. La decisión central: ¿qué dispersión de posición produce un error de velocidad dado en la salida y cuán buena es la aproximación lineal?

📘 **Dónde se aprende** (1 clase): [B75-C18 · Propagación de dispersión inicial](../programa/clases/B75/B75-C18-propagacion-de-dispersion-inicial/CLASE.md).

### Distancia de Fraunhofer

- La distancia de Fraunhofer es `2D²/λ`.

🎯 **Por qué importa (clase B49-C05):** Un patrón mal medido o medido demasiado cerca da un haz y unos lóbulos falsos. La decisión central: ¿a qué distancia medir y con qué nivel de ruido, para que el ancho y el lóbulo lateral sean fiables?

📘 **Dónde se aprende** (1 clase): [B49-C05 · Medición y calibración de patrones de antena](../programa/clases/B49/B49-C05-medicion-y-calibracion-de-patrones-de-antena/CLASE.md).

### Distancia de frenado

- La distancia de frenado es `d = v τ + v²/(2a)`, con `τ` la suma del ciclo y la latencia del sensor y `a` la desaceleración.

🎯 **Por qué importa (clase B98-C05):** Ningún plan, por bueno que sea, protege a un vehículo del peligro que aparece entre dos ciclos de comunicación. La decisión central: ¿qué debe resolver el vehículo por sí mismo y a qué velocidad puede ir para que ese reflejo llegue a tiempo?

📘 **Dónde se aprende** (1 clase): [B98-C05 · Autonomía de bajo nivel y comportamientos reactivos](../programa/clases/B98/B98-C05-autonomia-de-bajo-nivel-y-comportamientos-reactivos/CLASE.md).

### Distancia de Hamming

- La distancia de Hamming compara perfiles de obligaciones.

🎯 **Por qué importa (clase B119-C33):** B119 presenta los instrumentos uno por uno; distinguir qué obligaciones recaen en Estados y en operadores exige compararlos sistemáticamente. Esta clase integra las clases C01 a C11 y es la evidencia de portafolio del bloque.

📘 **Dónde se aprende** (1 clase): [B119-C33 · Matriz comparativa de obligaciones jurídicas por actor](../programa/clases/B119/B119-C33-matriz-comparativa-de-obligaciones-juridicas-por-actor/CLASE.md).

### Distancia de Jaccard

- La distancia de Jaccard es `1 − J`.

🎯 **Por qué importa (clase B119-C19):** Los tratados fijan principios y dejan la aplicación a los Estados (art. VI; art.

📘 **Dónde se aprende** (1 clase): [B119-C19 · Legislación comparada y casos nacionales](../programa/clases/B119/B119-C19-legislacion-comparada-y-casos-nacionales/CLASE.md).

### Distancia de Kolmogorov–Smirnov

- La distancia de Kolmogorov–Smirnov (KS) entre la acumulada empírica y la normal es el máximo de la diferencia absoluta de ambas acumuladas.

🎯 **Por qué importa (clase B12-C06):** Ningún instrumento tiene ruido exactamente normal, y sin embargo casi todas las incertidumbres se expresan con campanas. La razón es que se reportan promedios y sumas de muchas contribuciones pequeñas.

📘 **Dónde se aprende** (1 clase): [B12-C06 · Teorema central del límite](../programa/clases/B12/B12-C06-teorema-central-del-limite/CLASE.md).

### Distancia de luminosidad

- La distancia de luminosidad `D_L` define cuánto flujo llega: `F = L/(4πD_L²)`.

🎯 **Por qué importa (clase B26-C19):** La aceleración cósmica se descubrió porque las supernovas Ia lejanas aparecían más débiles de lo esperado. Para reproducir ese razonamiento hay que saber calcular la distancia de luminosidad y ver cuánto cambia con el contenido del universo.

📘 **Dónde se aprende** (1 clase): [B26-C19 · Energía oscura y parámetros](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md).

### Distancia de Mahalanobis

- La distancia de Mahalanobis al cuadrado, `d² = eᵀP⁻¹e`, mide la distancia en unidades de incertidumbre y, para un vector gaussiano de dimensión `k`, sigue una `χ²` con `k` grados de libertad.
- La distancia de Mahalanobis de un punto `x` a una distribución con media `μ` y covarianza `Σ` es `d² = (x − μ)ᵀ Σ⁻¹ (x − μ)`: mide la distancia en unidades de desviación, tomando en cuenta la correlación.
- La distancia de Mahalanobis `d² = eᵀP⁻¹e` marca atípicos multivariados (C18).

💡 **Cómo se explica en la clase [B12-C18](../programa/clases/B12/B12-C18-matrices-de-covarianza/CLASE.md):**
- La distancia de Mahalanobis mide cuán adentro o afuera de la nube está un punto.
- *Descripción textual:* de la covarianza se obtienen cuatro cosas: la elipse (por autovalores y ejes), la covarianza de una transformación lineal, la distancia de Mahalanobis para decidir compatibilidad con la `χ²`, y un factor de Cholesky para generar muestras con esa covarianza.
- 🎯 **Por qué importa:** El resultado de una determinación de órbita o de un ajuste no es un número sino un vector con una matriz de covarianza; sin ella no se puede propagar, comparar con otro resultado ni calcular probabilidades.

📘 **Dónde se aprende** (3 clases): [B12-C18 · Matrices de covarianza](../programa/clases/B12/B12-C18-matrices-de-covarianza/CLASE.md); [B12-C19 · Detección de valores atípicos](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md); [B17-C05 · Detección de anomalías](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md).

### Distancia de paso

- La distancia de paso (*miss distance*) es esa mínima distancia.

💡 **Cómo se explica en la clase [B118-C05](../programa/clases/B118/B118-C05-conjunciones-orbitales/CLASE.md):**
- *Descripción textual:* de las dos órbitas se obtienen las posiciones en cada instante; el mínimo de la distancia da el TCA y la distancia de paso, y la velocidad relativa se contrasta con la fórmula analítica.
- Analogía: dos autos que cruzan una intersección con dos segundos de diferencia; el tiempo de diferencia por la velocidad da la distancia de paso.
- ⚠️ **Error frecuente:** Confundir distancia de paso con distancia en el instante de la alerta. Se corrige con 8.3: el TCA es el mínimo.
- 🎯 **Por qué importa:** La alerta de conjunción es el producto básico del tráfico espacial. Su geometría explica por qué los encuentros son tan rápidos y por qué un pequeño desfase en el tiempo produce un cambio grande en la distancia.

📘 **Dónde se aprende** (1 clase): [B118-C05 · Conjunciones orbitales](../programa/clases/B118/B118-C05-conjunciones-orbitales/CLASE.md).

### Distancia de seguridad

- La distancia de seguridad separa a las personas del lugar de lanzamiento.

💡 **Cómo se explica en la clase [B119-C24](../programa/clases/B119/B119-C24-limites-legales-y-de-seguridad-de-la-experimentacion-educativa/CLASE.md):**
- *Descripción textual:* el impulso y la masa dan la velocidad; de ella el apogeo con y sin arrastre; del apogeo la distancia de seguridad y la decisión de revisar la reglamentación.
- 🎯 **Por qué importa:** Ninguna clase trata los límites de la experimentación educativa; el art. VI del tratado exige autorización y supervisión de las actividades no gubernamentales, y la escala pequeña no exime de ella.

📘 **Dónde se aprende** (1 clase): [B119-C24 · Límites legales y de seguridad de la experimentación educativa](../programa/clases/B119/B119-C24-limites-legales-y-de-seguridad-de-la-experimentacion-educativa/CLASE.md).

### Distancia diaria

- La distancia diaria es velocidad × uso × horas.

💡 **Cómo se explica en la clase [B97-C20](../programa/clases/B97/B97-C20-mision-robotica-integrada-simulada/CLASE.md):**
- El uso y la ruta actúan siempre sobre la distancia diaria; la batería solo mientras limita las horas (aquí limita, porque `E/P` es menor que 4 h).
- *Descripción textual:* la energía y el tiempo fijan las horas útiles; con la velocidad dan la distancia diaria; la distancia por el factor de ruta da los días nominales y las anomalías los alargan.
- 🎯 **Por qué importa:** Una misión se diseña con un presupuesto de días y de margen. Un modelo integrado, aunque simple, muestra cuál parámetro domina y cuánto margen pide una anomalía, antes de invertir en simulaciones detalladas.

📘 **Dónde se aprende** (1 clase): [B97-C20 · Misión robótica integrada simulada](../programa/clases/B97/B97-C20-mision-robotica-integrada-simulada/CLASE.md).

### Distancia epicentral

- La distancia epicentral `Δ` es el ángulo en el centro entre fuente y estación.

🎯 **Por qué importa (clase B53-C02):** Un solo sismómetro no da la posición completa de un evento. La decisión central: ¿cuánto vale la distancia al evento y con qué incertidumbre, si solo se leen los tiempos de llegada P y S?

📘 **Dónde se aprende** (1 clase): [B53-C02 · Sismología planetaria](../programa/clases/B53/B53-C02-sismologia-planetaria/CLASE.md).

### Distancia equivalente

- La distancia equivalente es la que da cierta `T_eq`.

💡 **Cómo se explica en la clase [B29-C13](../programa/clases/B29/B29-C13-zonas-de-habitabilidad/CLASE.md):**
- Una estrella más fría tiene la distancia equivalente mucho más corta, a la que la rotación sincrónica y las erupciones pueden ser importantes.
- 🎯 **Por qué importa:** La temperatura de equilibrio es la primera estimación de si un mundo es cálido o helado, pero no es la temperatura de la superficie: depende del albedo y del efecto invernadero. La decisión central: ¿a qué distancias una estrella da una temperatura de equilibrio dada y cuánto cambia con el albedo?

📘 **Dónde se aprende** (1 clase): [B29-C13 · Zonas de habitabilidad](../programa/clases/B29/B29-C13-zonas-de-habitabilidad/CLASE.md).

### Distancia focal

- La distancia focal `c` es la distancia del centro a cada foco; se cumple `a² = b² + c²`.
- La apertura `D` es el diámetro del objetivo o espejo; la distancia focal `F`, la longitud del camino óptico; la razón focal `N = F/D`.
- La distancia focal `f` de un paraboloide `z = r²/(4f)` es la distancia del vértice al foco.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C09](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md):**
- Paso 2 · Distancia focal. `c = ae = 17,354 au`.
- 🎯 **Por qué importa:** Las órbitas de planetas y cometas son, en buena aproximación, elipses con el Sol en uno de sus focos. Si no sabes qué es un semieje, un foco o la excentricidad, no puedes leer una tabla de elementos orbitales ni distinguir una órbita casi circular, como la de la Tierra, de una muy alargada, como la del cometa Halley.

📖 **Explicado a fondo:** [Distancia focal y número f](esencial/esencial-d-l.md#distancia-focal-y-número-f) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (5 clases): [B04-C09 · Circunferencias y elipses](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md); [B08-C14 · Telescopios de iniciación](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md); [B08-C19 · Fotografía astronómica elemental](../programa/clases/B08/B08-C19-fotografia-astronomica-elemental/CLASE.md); [B09-C13 · Áreas y volúmenes por integración](../programa/clases/B09/B09-C13-areas-y-volumenes-por-integracion/CLASE.md); [B71-C08 · Órbitas elípticas](../programa/clases/B71/B71-C08-orbitas-elipticas/CLASE.md).

### Distancia focal posterior

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C05](../programa/clases/B41/B41-C05-lentes-delgadas-y-gruesas/CLASE.md):**
- En la biconvexa gruesa, `f = 103,786 mm`, la distancia focal posterior medida desde el vértice es `89,638 mm` y el plano principal posterior está `14,148 mm` dentro de la lente (fórmula de libro `−14,148 mm`).
- 🎯 **Por qué importa:** El objetivo de un refractor es una lente. La decisión central: ¿cuánto se equivoca la fórmula de lente delgada cuando la lente es gruesa?

📘 **Dónde se aprende** (1 clase): [B41-C05 · Lentes delgadas y gruesas](../programa/clases/B41/B41-C05-lentes-delgadas-y-gruesas/CLASE.md).

### Distancia focal posterior (BFD)

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C08):** Los programas de diseño óptico trazan rayos exactos. La decisión central: ¿cuándo se separa el rayo real del paraxial y cómo crece esa diferencia?

📘 **Dónde se aprende** (1 clase): [B41-C08 · Trazado de rayos para telescopios](../programa/clases/B41/B41-C08-trazado-de-rayos-para-telescopios/CLASE.md).

### Distancia imagen

- La distancia objeto `s` y la distancia imagen `s'`.

🎯 **Por qué importa (clase B41-C06):** El foco de una cámara o de un telescopio decide el tamaño de la imagen. La decisión central: ¿dónde cae la imagen y de qué tamaño es?

📘 **Dónde se aprende** (1 clase): [B41-C06 · Distancias focales y formación de imagen](../programa/clases/B41/B41-C06-distancias-focales-y-formacion-de-imagen/CLASE.md).

### Distancia interpupilar

- La distancia interpupilar es la separación de tus ojos que debes igualar con las bisagras; el ajuste dióptrico corrige la diferencia entre tus dos ojos.

💡 **Cómo se explica en la clase [B08-C13](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md):**
- Abre las bisagras hasta que veas un solo círculo (distancia interpupilar).
- 🎯 **Por qué importa:** Unos binoculares multiplican lo que ves, pero también multiplican el riesgo si miras al Sol. La pregunta motivadora: ¿qué binoculares sirven para mi caso y cómo los uso sin hacerme daño?

📘 **Dónde se aprende** (1 clase): [B08-C13 · Uso seguro de binoculares](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md).

### Distancia KS

- La distancia KS entre distribuciones.

🎯 **Por qué importa (clase B34-C07):** Una buena correlación puede ocultar un error de escala. La decisión central: ¿qué métrica detecta cada tipo de discrepancia?

📘 **Dónde se aprende** (1 clase): [B34-C07 · Comparación de modelos coronales con observaciones](../programa/clases/B34/B34-C07-comparacion-de-modelos-coronales-con-observaciones/CLASE.md).

### Distancia límite

- La distancia límite es `d = √(L/S_ef)` con `L` en luminosidades solares y `d` en UA.

🎯 **Por qué importa (clase B56-C12):** Elegir blancos para buscar biofirmas exige un criterio objetivo. La zona habitable lo ofrece, con limitaciones.

📘 **Dónde se aprende** (1 clase): [B56-C12 · Exoplanetas potencialmente habitables](../programa/clases/B56/B56-C12-exoplanetas-potencialmente-habitables/CLASE.md).

### Distancia mínima

- El clasificador de distancia mínima asigna la clase de la media más cercana.

💡 **Cómo se explica en la clase [B15-C22](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md):**
- Las covarianzas de las clases son iguales en la simulación, por lo que la distancia mínima es casi óptima y la máxima verosimilitud (que estima más parámetros con solo 30 muestras) no gana.
- Si el suelo se acerca a la vegetación (media `(0,10; 0,40)` en vez de `(0,20; 0,28)`), la exactitud de distancia mínima baja de `0,910` a `0,765`: ningún clasificador de estas bandas puede mejorarlo mucho porque el solapamiento es propiedad de los datos.
- 🎯 **Por qué importa:** Un mapa de cobertura de suelo parece una verdad; en realidad es una predicción con un error que depende de las muestras elegidas y de cuánto se solapan las clases en el espacio espectral. Cifras como «90 % de exactitud» no significan nada sin decir con qué datos se midieron, ni cómo se reparte el error entre clases.

📘 **Dónde se aprende** (1 clase): [B15-C22 · Clasificación supervisada de imágenes](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md).

### Distancia mínima de paso

- La distancia mínima de paso es la mínima distancia entre el sensor y la trayectoria.

🎯 **Por qué importa (clase B118-C23):** B118-C15 trata solo mega constelaciones; aquí se aporta la comprensión de qué no ve una red. Un catálogo construido con lo detectado subestima los objetos pequeños y lejanos, y las estadísticas que se calculan con él están sesgadas.

📘 **Dónde se aprende** (1 clase): [B118-C23 · Cobertura, sesgos y límites de las redes de vigilancia](../programa/clases/B118/B118-C23-cobertura-sesgos-y-limites-de-las-redes-de-vigilancia/CLASE.md).

### Distancia normalizada

- La distancia normalizada entre dos perfiles de `k` dimensiones en escala 0–100 es `√Σ(Δ)² / (100 √k)`.

🎯 **Por qué importa (clase B111-C02):** Ninguna clase del programa trataba las diferencias culturales y de idioma en equipos internacionales. La decisión central: ¿cómo se vuelve un riesgo de comunicación cuantificable y cómo se mitiga con procedimientos y no con estereotipos?

📘 **Dónde se aprende** (1 clase): [B111-C02 · Gestión intercultural en tripulaciones multinacionales](../programa/clases/B111/B111-C02-gestion-intercultural-en-tripulaciones-multinacionales/CLASE.md).

### Distancia objeto

- La distancia objeto `s` y la distancia imagen `s'`.

🎯 **Por qué importa (clase B41-C06):** El foco de una cámara o de un telescopio decide el tamaño de la imagen. La decisión central: ¿dónde cae la imagen y de qué tamaño es?

📘 **Dónde se aprende** (1 clase): [B41-C06 · Distancias focales y formación de imagen](../programa/clases/B41/B41-C06-distancias-focales-y-formacion-de-imagen/CLASE.md).

### Distancia por Cefeidas

- Una distancia por Cefeidas usa estrellas variables cuya luminosidad se relaciona con su período (S2); una distancia por fluctuaciones de brillo superficial usa la granularidad de la imagen de una galaxia elíptica (S3).

🎯 **Por qué importa (clase B01-C15):** La galaxia de la línea Hα (C01) está a 43 Mpc, pero ¿qué significa eso comparado con lo que ya conoces? ¿Está más lejos o más cerca que Andrómeda?

📘 **Dónde se aprende** (1 clase): [B01-C15 · Galaxias y agrupaciones cósmicas](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md).

### Distancia por fluctuaciones de brillo superficial

- Una distancia por Cefeidas usa estrellas variables cuya luminosidad se relaciona con su período (S2); una distancia por fluctuaciones de brillo superficial usa la granularidad de la imagen de una galaxia elíptica (S3).

🎯 **Por qué importa (clase B01-C15):** La galaxia de la línea Hα (C01) está a 43 Mpc, pero ¿qué significa eso comparado con lo que ya conoces? ¿Está más lejos o más cerca que Andrómeda?

📘 **Dónde se aprende** (1 clase): [B01-C15 · Galaxias y agrupaciones cósmicas](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md).

### Distancia propia

- La distancia propia es la longitud medida con la métrica a lo largo de un camino.

💡 **Cómo se explica en la clase [B26-C07](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md):**
- G --> D["Distancia propia radial<br/>s = ∫ dr / √(1 − r_s/r)"]
- *Descripción textual:* la masa fija `r_s`; el factor `1 − r_s/r` aparece en la métrica; la distancia propia radial integra su raíz inversa y resulta mayor que la diferencia de coordenadas.
- 🎯 **Por qué importa:** Medir una distancia cerca de una masa grande no da lo mismo que en el espacio plano: el radio de un círculo y su circunferencia dejan de cumplir `C = 2πR`. Los GPS, las lentes gravitacionales y los agujeros negros dependen de esa diferencia.

📘 **Dónde se aprende** (1 clase): [B26-C07 · Curvatura y métricas](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md).

### Distancia proyectada

- La distancia proyectada `ρ` es la distancia al núcleo en el plano del cielo.

🎯 **Por qué importa (clase B55-C11):** Un telescopio no ve la densidad en cada punto de la coma sino la columna a lo largo de la línea de visión. Para pasar de lo medido a la producción de moléculas por el núcleo hay que modelar la expansión y la destrucción.

📘 **Dónde se aprende** (1 clase): [B55-C11 · Química en cometas](../programa/clases/B55/B55-C11-quimica-en-cometas/CLASE.md).

### Distancia recorrida

- El desplazamiento `Δr = r₂ − r₁` es el cambio de posición, y la distancia recorrida es la longitud del camino, que puede ser mayor.

🎯 **Por qué importa (clase B05-C02):** Cuando una agencia dice que un satélite «va a 7,7 km/s», ¿respecto de qué y en qué dirección? La pregunta motivadora es: ¿cómo describo un movimiento de forma que otra persona lo reconstruya sin ambigüedad?

📘 **Dónde se aprende** (1 clase): [B05-C02 · Posición, velocidad y aceleración](../programa/clases/B05/B05-C02-posicion-velocidad-y-aceleracion/CLASE.md).

### Distancia Tierra–Marte

- La distancia Tierra–Marte varía entre un mínimo y un máximo de la ficha de la NASA.

💡 **Cómo se explica en la clase [B113-C03](../programa/clases/B113/B113-C03-comunicacion-diferida-y-soporte-psicologico-a-distancia/CLASE.md):**
- A la mínima distancia Tierra–Marte de la ficha de la NASA (`54,6 × 10⁶ km`), la luz tarda `3,035 min` en ir; a la máxima (`401,4 × 10⁶ km`), `22,315 min`.
- 🎯 **Por qué importa:** Ninguna clase trata el efecto del retardo en el apoyo psicológico. La decisión central: ¿qué formatos de apoyo siguen siendo posibles cuando una respuesta tarda decenas de minutos?

📘 **Dónde se aprende** (1 clase): [B113-C03 · Comunicación diferida y soporte psicológico a distancia](../programa/clases/B113/B113-C03-comunicacion-diferida-y-soporte-psicologico-a-distancia/CLASE.md).

### Distancia transversal

- La distancia transversal `D_M` coincide con `D_C` si no hay curvatura y es `(c/H₀)sinh(√Ω_k D_C H₀/c)/√Ω_k` si `Ω_k > 0`.

🎯 **Por qué importa (clase B26-C19):** La aceleración cósmica se descubrió porque las supernovas Ia lejanas aparecían más débiles de lo esperado. Para reproducir ese razonamiento hay que saber calcular la distancia de luminosidad y ver cuánto cambia con el contenido del universo.

📘 **Dónde se aprende** (1 clase): [B26-C19 · Energía oscura y parámetros](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md).

### Distinguible de cero

- Un exceso es distinguible de cero si `ee/σ` supera ~3.

🎯 **Por qué importa (clase B55-C17):** Que un compuesto prebiótico llegue intacto hasta nosotros depende de cuánta radiación recibió, y que un exceso entre dos formas quirales sea real depende de cuántas moléculas se contaron. La decisión central: ¿cuánto sobrevive y con qué incertidumbre puedo afirmar un exceso enantiomérico distinto de cero?

📘 **Dónde se aprende** (1 clase): [B55-C17 · Compuestos prebióticos](../programa/clases/B55/B55-C17-compuestos-prebioticos/CLASE.md).

### Distorsión

- La distorsión es la desviación de la altura de imagen respecto de `f tan θ`.

💡 **Cómo se explica en la clase [B50-C08](../programa/clases/B50/B50-C08-distorsion-geometrica-y-su-calibracion/CLASE.md):**
- En la esquina (15, 15) mm la distorsión desplaza la estrella `0,2578 mm` y el mapa inverso la recupera con error `2,5 × 10⁻¹⁵ mm`.
- Límite: distorsión radial pura, sin descentrado.
- 🎯 **Por qué importa:** En astrometría y en mosaicos una distorsión de 0,1 % mueve las estrellas decenas de píxeles. La decisión central: ¿qué modelo describe la distorsión y con qué precisión se puede calibrar?

📘 **Dónde se aprende** (1 clase): [B50-C08 · Distorsión geométrica y su calibración](../programa/clases/B50/B50-C08-distorsion-geometrica-y-su-calibracion/CLASE.md).

### Distorsión centrífuga

- La distorsión centrífuga `D` corrige el alargamiento del enlace al girar.

🎯 **Por qué importa (clase B62-C01):** Una línea de CO a 115,27 GHz no es un dato aislado: es la consecuencia de un momento de inercia. Si entiendes de dónde sale, puedes predecir líneas que nadie ha medido y reconocer cuándo una línea observada no es del CO.

📘 **Dónde se aprende** (1 clase): [B62-C01 · Espectros rotacionales de moléculas: niveles y reglas de selección](../programa/clases/B62/B62-C01-espectros-rotacionales-de-moleculas-niveles-y-reglas-de-seleccion/CLASE.md).

### Distorsión centrifugal

- La distorsión centrifugal `D` corrige el estiramiento: `ν = 2 B J − 4 D J³`.

🎯 **Por qué importa (clase B55-C09):** Las moléculas del espacio frío se detectan casi siempre por sus líneas de rotación en milimétrico y submilimétrico. Para identificar una línea hay que saber de dónde sale su frecuencia, qué fracción de niveles está poblada y cómo corregirla por la velocidad de la nube.

📘 **Dónde se aprende** (1 clase): [B55-C09 · Espectros moleculares de radio](../programa/clases/B55/B55-C09-espectros-moleculares-de-radio/CLASE.md).

### Distorsión espectral

- La distorsión espectral es el cambio de los colores respecto al original.

💡 **Cómo se explica en la clase [B15-C24](../programa/clases/B15/B15-C24-fusion-de-imagenes-de-distintos-sensores/CLASE.md):**
- Sustitución de componentes (por ejemplo, de intensidad): rápida, con riesgo de distorsión espectral.
- 🎯 **Por qué importa:** Un mapa de cobertura exige distinguir objetos pequeños (caminos, parcelas) y también su firma espectral (si son vegetación o suelo). Ninguna imagen entrega ambas cosas a la vez.

📘 **Dónde se aprende** (1 clase): [B15-C24 · Fusión de imágenes de distintos sensores](../programa/clases/B15/B15-C24-fusion-de-imagenes-de-distintos-sensores/CLASE.md).

### Distorsión radial

- La distorsión radial multiplica las coordenadas normalizadas por `1 + k1 r² + k2 r⁴`.

💡 **Cómo se explica en la clase [B103-C01](../programa/clases/B103/B103-C01-calibracion-intrinseca-de-camaras/CLASE.md):**
- Una cámara sintética de 1280 × 960 px con `fx = fy = 800 px`, punto principal `(640; 480) px` y distorsión radial `k1 = −0,12`, `k2 = 0,05` mira un tablero de 9 × 6 esquinas con casillas de 25 mm desde 12 poses, con ruido de 0,3 px.
- 🎯 **Por qué importa:** Un rover que mide una distancia con un error de focal del 1 % comete un error del 1 % en la distancia. La decisión central: ¿cuántas vistas y qué modelo de distorsión hacen falta para que la focal y el punto principal sean fiables, y cómo se comprueba?

📘 **Dónde se aprende** (1 clase): [B103-C01 · Calibración intrínseca de cámaras](../programa/clases/B103/B103-C01-calibracion-intrinseca-de-camaras/CLASE.md).

### Distractor diagnóstico

- Un distractor diagnóstico es una opción incorrecta escrita para que la elija quien tiene esa idea.

🎯 **Por qué importa (clase B131-C03):** Enseñar sin saber qué creen ya los estudiantes deja intactas las ideas previas. La decisión central: ¿qué distractor elegiste para atrapar qué idea, y cómo sabrás si el cambio es real?

📘 **Dónde se aprende** (1 clase): [B131-C03 · Conocimientos previos y concepciones alternativas](../programa/clases/B131/B131-C03-conocimientos-previos-y-concepciones-alternativas/CLASE.md).

### Distribución

- Una distribución (S1, C.2.3) es la función que da la probabilidad de cada valor o conjunto de valores de una variable aleatoria.

🎯 **Por qué importa (clase B12-C03):** Cada vez que un detector cuenta fotones, una nave registra impactos o un instrumento mide con ruido, el patrón de la incertidumbre se parece a uno de unos pocos moldes. Reconocer el molde permite calcular probabilidades sin construir todo desde cero y entender qué supuesto físico lo respalda.

📘 **Dónde se aprende** (1 clase): [B12-C03 · Distribuciones de probabilidad](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md).

### Distribución acumulada

- La distribución acumulada `N(>D)` cuenta cráteres mayores que `D`.

🎯 **Por qué importa (clase B53-C08):** Un conteo no es un número, es una distribución con incertidumbre. La decisión central: ¿qué estimador de la pendiente es fiable y a partir de qué diámetro el catálogo es completo?

📘 **Dónde se aprende** (1 clase): [B53-C08 · Cartografía de cráteres](../programa/clases/B53/B53-C08-cartografia-de-crateres/CLASE.md).

### Distribución binomial

- La distribución binomial da la probabilidad de `m` aciertos entre `N` intentos con probabilidad `p`.
- La distribución binomial `B(n, p)` cuenta éxitos en `n` ensayos independientes con probabilidad `p`: `P(K = k) = C(n,k) pᵏ (1−p)ⁿ⁻ᵏ`.

💡 **Cómo se explica en la clase [B02-C09](../programa/clases/B02/B02-C09-alineaciones-arqueologicas-y-sesgos/CLASE.md):**
- El número de aciertos sigue una distribución binomial: `P(≥ 1) = 1 − (1−p)^N = 0,937`, es decir, casi seguro que al menos una estructura «acierta»;
- 🎯 **Por qué importa:** Con suficientes estructuras, suficientes objetivos celestes y una tolerancia generosa, siempre aparece alguna «alineación». La pregunta motivadora es: ¿cuántas alineaciones esperaríamos si nadie hubiese mirado el cielo?

📘 **Dónde se aprende** (2 clases): [B02-C09 · Alineaciones arqueológicas y sesgos](../programa/clases/B02/B02-C09-alineaciones-arqueologicas-y-sesgos/CLASE.md); [B12-C03 · Distribuciones de probabilidad](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md).

### Distribución chi-cuadrado

- La distribución chi-cuadrado con `m` grados de libertad es la de la suma de `m` normales estándar al cuadrado; para datos normales de `m` variables, `d²` la sigue.

🎯 **Por qué importa (clase B17-C05):** El subsistema térmico de un satélite entrega temperatura y corriente. Cada una, por separado, puede estar dentro de su rango normal y sin embargo la pareja ser imposible: la corriente alta con temperatura baja no ocurre nunca en operación sana.

📘 **Dónde se aprende** (1 clase): [B17-C05 · Detección de anomalías](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md).

### Distribución de Bose–Einstein

- La distribución de Bose–Einstein, la de Fermi–Dirac y la de Maxwell–Boltzmann.

🎯 **Por qué importa (clase B31-C06):** La radiación de las estrellas y la presión de degeneración de los remanentes estelares dependen de estas estadísticas. La decisión central: ¿qué distribución usar y qué constantes se derivan?

📘 **Dónde se aprende** (1 clase): [B31-C06 · Estadísticas cuánticas](../programa/clases/B31/B31-C06-estadisticas-cuanticas/CLASE.md).

### Distribución de coseno

- La distribución de coseno `F ∝ cos φ`.

🎯 **Por qué importa (clase B43-C09):** Una celda que no reparte la carga como se diseñó deforma el espejo. La decisión central: ¿cómo se reparte el peso entre los puntos de apoyo y cuánto cambia si el pivote se desplaza unos milímetros?

📘 **Dónde se aprende** (1 clase): [B43-C09 · Celdas y soporte de espejos](../programa/clases/B43/B43-C09-celdas-y-soporte-de-espejos/CLASE.md).

### Distribución de entrenamiento

- La distribución de entrenamiento es la de los datos con que se ajustó el modelo; la de despliegue, la de los datos donde se usa.

🎯 **Por qué importa (clase B17-C07):** Un modelo se entrena con un catálogo y se despliega sobre otro: otro telescopio, otra época, otro brillo límite. Su exactitud medida en validación cruzada deja de valer, y el modelo no avisa: responde con la misma seguridad.

📘 **Dónde se aprende** (1 clase): [B17-C07 · Validación fuera de distribución](../programa/clases/B17/B17-C07-validacion-fuera-de-distribucion/CLASE.md).

### Distribución de Flory

- La distribución de Flory da la fracción de cadenas de longitud `n`: `(1 − p) pⁿ⁻¹`.

🎯 **Por qué importa (clase B56-C21):** C03 trata el origen de autorreplicantes, pero ninguna clase trata la polimerización experimental y sus límites. Antes de que un replicador pueda copiarse, hay que formar cadenas lo bastante largas.

📘 **Dónde se aprende** (1 clase): [B56-C21 · Polimerización prebiótica experimental: oligómeros y condiciones de laboratorio](../programa/clases/B56/B56-C21-polimerizacion-prebiotica-experimental-oligomeros-y-condiciones-de-laboratorio/CLASE.md).

### Distribución de Gumbel

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B33-C03):** Las decisiones de protección se basan en periodos de retorno que superan al registro. La decisión central: ¿qué nivel se espera una vez cada T años y cuán incierto es?

📘 **Dónde se aprende** (1 clase): [B33-C03 · Eventos extremos históricos de clima espacial](../programa/clases/B33/B33-C03-eventos-extremos-historicos-de-clima-espacial/CLASE.md).

### Distribución de Poisson

- La distribución de Poisson de parámetro `λ` cuenta eventos independientes en un intervalo con tasa constante: `P(N = k) = e^{−λ} λᵏ / k!`.
- La distribución de Poisson da `P(k) = e^(−μ) μ^k/k!`.

🎯 **Por qué importa (clase B12-C03):** Cada vez que un detector cuenta fotones, una nave registra impactos o un instrumento mide con ruido, el patrón de la incertidumbre se parece a uno de unos pocos moldes. Reconocer el molde permite calcular probabilidades sin construir todo desde cero y entender qué supuesto físico lo respalda.

📘 **Dónde se aprende** (2 clases): [B12-C03 · Distribuciones de probabilidad](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md); [B97-C12 · Robots de mantenimiento](../programa/clases/B97/B97-C12-robots-de-mantenimiento/CLASE.md).

### Distribución de Rayleigh

- La distribución de Rayleigh describe el módulo del error en 2D.
- La distribución de Rayleigh describe la magnitud de un error 2D con componentes gaussianas independientes de dispersión `σ`.

🎯 **Por qué importa (clase B58-C11):** Una observación de seguimiento solo sirve si el objeto cae en el campo de la cámara. La decisión central: ¿cuándo y con qué arco conviene volver a observar para no perder el objeto?

📘 **Dónde se aprende** (2 clases): [B58-C11 · Observaciones de seguimiento](../programa/clases/B58/B58-C11-observaciones-de-seguimiento/CLASE.md); [B92-C02 · Divergencia del haz y pérdidas por apuntamiento óptico](../programa/clases/B92/B92-C02-divergencia-del-haz-y-perdidas-por-apuntamiento-optico/CLASE.md).

### Distribución de velocidades

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C24):** La energía por carga elegida por el analizador determina qué se mide; la resolución de los canales limita la temperatura que se recupera. La decisión central: ¿cuántos canales y qué corrección dan la velocidad y la temperatura del plasma con error aceptable?

📘 **Dónde se aprende** (1 clase): [B47-C24 · Instrumentos de plasma y campos in situ](../programa/clases/B47/B47-C24-instrumentos-de-plasma-y-campos-in-situ/CLASE.md).

### Distribución de Weibull

- La distribución de Weibull da `P_f = 1 − exp(−(V/V₀)(σ/σ₀)ᵐ)`;

🎯 **Por qué importa (clase B84-C04):** Un metal avisa antes de romper; una cerámica no. Diseñar con la resistencia media de una probeta pequeña sobreestima la de una pieza grande en 40 %.

📘 **Dónde se aprende** (1 clase): [B84-C04 · Cerámicos y polímeros espaciales](../programa/clases/B84/B84-C04-ceramicos-y-polimeros-espaciales/CLASE.md).

### Distribución estacionaria

- La distribución estacionaria `π` cumple `πP = π`: si el estado se distribuye según `π`, lo sigue haciendo.

💡 **Cómo se explica en la clase [B12-C13](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md):**
- La distribución estacionaria es `π = (q/(p+q), p/(p+q)) = (0,8; 0,2)`.
- 🎯 **Por qué importa:** Una posterior de diez o veinte parámetros (órbita, calibración, ruido) no se puede tabular. Pero sí se pueden generar muestras que sigan su forma, aunque no se conozca su normalización.

📘 **Dónde se aprende** (1 clase): [B12-C13 · Cadenas de Markov y muestreo](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md).

### Distribución exponencial

- La distribución exponencial de tasa `r` describe el tiempo de espera entre eventos de un proceso de Poisson: densidad `r e^{−rt}` y `P(T > t) = e^{−rt}`.
- Profundidad de descarga (DoD): fracción usable de la batería. Distribución exponencial: duración sin memoria.

🎯 **Por qué importa (clase B12-C03):** Cada vez que un detector cuenta fotones, una nave registra impactos o un instrumento mide con ruido, el patrón de la incertidumbre se parece a uno de unos pocos moldes. Reconocer el molde permite calcular probabilidades sin construir todo desde cero y entender qué supuesto físico lo respalda.

📘 **Dónde se aprende** (2 clases): [B12-C03 · Distribuciones de probabilidad](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md); [B48-C07 · Seguridad en instalaciones remotas](../programa/clases/B48/B48-C07-seguridad-en-instalaciones-remotas/CLASE.md).

### Distribución fuente

- Una rueda (*wheel*) es un paquete ya compilado para una plataforma; una distribución fuente (*sdist*) es el código sin compilar.

🎯 **Por qué importa (clase B14-C12):** Tu análisis dio un período de 5553,624562 s en 2026. Un colega lo ejecuta con otra versión de SciPy y obtiene un cierre distinto; otro usa Python más antiguo y falla al importar. «En mi máquina funciona» no es un resultado científico.

📘 **Dónde se aprende** (1 clase): [B14-C12 · Ejecución reproducible con uv](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md).

### Distribución kappa

- La distribución kappa tiene una cola de ley de potencias y se acerca a la maxwelliana si `κ → ∞`.

💡 **Cómo se explica en la clase [B35-C01](../programa/clases/B35/B35-C01-funciones-de-distribucion-de-velocidades-en-plasmas/CLASE.md):**
- Con una distribución kappa de igual `T` cinética, la densidad de probabilidad a `5 v_t` es `46,3` veces la maxwelliana si `κ = 5`.
- 🎯 **Por qué importa:** Los instrumentos miden distribuciones, y casi todas las fórmulas de fluido son momentos de ellas. La decisión central: ¿basta una maxwelliana o hay que conservar la cola?

📘 **Dónde se aprende** (1 clase): [B35-C01 · Funciones de distribución de velocidades en plasmas](../programa/clases/B35/B35-C01-funciones-de-distribucion-de-velocidades-en-plasmas/CLASE.md).

### Distribución normal

- La distribución normal (o de Laplace–Gauss, S1, C.2.14;

🎯 **Por qué importa (clase B12-C03):** Cada vez que un detector cuenta fotones, una nave registra impactos o un instrumento mide con ruido, el patrón de la incertidumbre se parece a uno de unos pocos moldes. Reconocer el molde permite calcular probabilidades sin construir todo desde cero y entender qué supuesto físico lo respalda.

📘 **Dónde se aprende** (1 clase): [B12-C03 · Distribuciones de probabilidad](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md).

### Distribución predictiva posterior

- La distribución predictiva posterior de un dato nuevo `ỹ` es `p(ỹ | y) = ∫ p(ỹ | θ) p(θ | y) dθ`: promedia la predicción para cada valor del parámetro, ponderada por su posterior.

🎯 **Por qué importa (clase B19-C06):** El contador de partículas lleva 12 horas midiendo. Con la posterior de la tasa `λ`, la pregunta práctica es: ¿cuántos eventos esperar en la hora 13, y qué tan sorprendente sería ver 8?

📘 **Dónde se aprende** (1 clase): [B19-C06 · Distribución predictiva posterior](../programa/clases/B19/B19-C06-distribucion-predictiva-posterior/CLASE.md).

### Distribución t de Student

- La distribución `t` de Student con `ν` grados de libertad es la distribución de `(x̄ − μ)/(s/√n)` cuando los datos son normales y `ν = n − 1` (S1, G.3.2 y C.3.8).
- La distribución t de Student describe la media estandarizada con `s` estimada.

🎯 **Por qué importa (clase B12-C08):** Un número sin rango es una afirmación sin evidencia de su precisión. «La distancia es 148,5 m» no dice si el valor es fiable al metro o al decámetro. Un intervalo con su nivel de confianza lo dice, y permite decidir si una medición cumple un requisito o si hay que tomar más datos.

📘 **Dónde se aprende** (2 clases): [B12-C08 · Intervalos de confianza](../programa/clases/B12/B12-C08-intervalos-de-confianza/CLASE.md); [B13-C12 · Incertidumbre expandida](../programa/clases/B13/B13-C12-incertidumbre-expandida/CLASE.md).

### Distribución tamaño-frecuencia

- La distribución tamaño-frecuencia acumulada `N(>D)` cuenta las rocas mayores que `D`.

🎯 **Por qué importa (clase B103-C06):** Un catálogo de rocas es incompleto justo donde hay más rocas: las pequeñas. Ajustar una ley de potencias con todas las detecciones da un exponente sesgado.

📘 **Dónde se aprende** (1 clase): [B103-C06 · Detección y catalogación de rocas en imágenes de superficie](../programa/clases/B103/B103-C06-deteccion-y-catalogacion-de-rocas-en-imagenes-de-superficie/CLASE.md).

### Distribución triangular

- La distribución triangular `(a, m, b)` tiene mínimo `a`, moda `m` y máximo `b`.

🎯 **Por qué importa (clase B108-C05):** Falta evaluar la secuencia de una EVA (tiempos, consumibles, márgenes) antes de ejecutarla. La decisión central: ¿cabe la secuencia en el tiempo y en los consumibles disponibles, con qué probabilidad y con qué margen?

📘 **Dónde se aprende** (1 clase): [B108-C05 · Evaluación de secuencias y líneas de tiempo de EVA](../programa/clases/B108/B108-C05-evaluacion-de-secuencias-y-lineas-de-tiempo-de-eva/CLASE.md).

### Distribución χ²

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B40-C15):** La varianza cósmica es el límite fundamental de la medición del fondo. La decisión central: ¿qué precisión máxima permite el número de modos disponibles?

📘 **Dónde se aprende** (1 clase): [B40-C15 · Varianza cósmica y límites de las mediciones del fondo](../programa/clases/B40/B40-C15-varianza-cosmica-y-limites-de-las-mediciones-del-fondo/CLASE.md).

### DITL

- Fit check: ajuste con el dispensador. DITL: prueba de «día en la vida».

💡 **Cómo se explica en la clase [B90-C20](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md):**
- *CubeSat 101* (F7) añade la prueba DITL, el mínimo contenido de los informes (procedimientos con marcas de tiempo, fotos, gráficas, prueba de que la unidad sobrevivió) y que el integrador debe aprobar el procedimiento antes de la prueba.
- *Descripción textual:* los ensayos se encadenan de la inspección al DITL; cada uno puede fallar y entonces se hace retrabajo y se repite el mismo ensayo antes de pasar al siguiente.
- 🎯 **Por qué importa:** Un calendario de ensayos sin contingencia casi nunca se cumple: cada falla suma retrabajo y repetición. La decisión central: ¿cuánto tiempo reservar para terminar con una confianza dada?

📘 **Dónde se aprende** (1 clase): [B90-C20 · Campaña conceptual de calificación de CubeSat](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md).

### Divergencia

- La divergencia `∇·F = ∂F₁/∂x + ∂F₂/∂y + ∂F₃/∂z` mide cuánto «sale» el campo de un punto (S1, §1.6(iii), ec. 1.6.21).
- Una divergencia es una trayectoria de HMC en la que el error de energía excede un umbral grande (aquí 1000): el integrador no pudo seguir la geometría.
- La divergencia `θ` es el semiángulo del cono en el campo lejano.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C19](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md):**
- Divergencia cero no significa «sin fuente»: la gravedad tiene fuente en el origen, donde el campo no está definido; el flujo la detecta.
- La divergencia es un grifo (o un sumidero) en cada punto: positiva si el campo sale, negativa si entra, cero si lo que entra, sale.
- ⚠️ **Error frecuente:** Confundir divergencia (escalar) con rotacional (vector). Se corrige con los ejercicios 1 y 2.
- 🎯 **Por qué importa:** La gravedad no tiene fuentes fuera de la masa que la produce, y eso permite calcular la gravedad de un planeta esférico sin sumar cada átomo: basta medir el flujo. La rotación de la Tierra produce un campo de velocidades con circulación no nula, y esa circulación mide cuánto «gira» el campo.

📘 **Dónde se aprende** (4 clases): [B09-C19 · Cálculo vectorial introductorio](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md); [B19-C04 · Diagnóstico de convergencia de cadenas](../programa/clases/B19/B19-C04-diagnostico-de-convergencia-de-cadenas/CLASE.md); [B77-C17 · Estabilidad durante descenso](../programa/clases/B77/B77-C17-estabilidad-durante-descenso/CLASE.md); [B92-C02 · Divergencia del haz y pérdidas por apuntamiento óptico](../programa/clases/B92/B92-C02-divergencia-del-haz-y-perdidas-por-apuntamiento-optico/CLASE.md).

### Divergencia cero

- Un campo cuyo gradiente tiene traza nula es de divergencia cero (la divergencia es la traza de su gradiente).

🎯 **Por qué importa (clase B10-C18):** La gravedad no es uniforme a lo largo de un satélite: lo que está más cerca de la Tierra se acelera más que lo que está lejos, y lo que está a los lados se comprime. Con una sola derivada `dg/dr` solo describes la dirección radial; el tensor de marea describe las tres direcciones a la vez.

📘 **Dónde se aprende** (1 clase): [B10-C18 · Producto tensorial y contracción](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md).

### Divergencia de Kullback–Leibler

- La divergencia de Kullback–Leibler de `q` respecto de `p` es `KL(q ‖ p) = E_q[log q(θ) − log p(θ)]`; es ≥ 0 y vale 0 solo si `q = p`.

💡 **Cómo se explica en la clase [B19-C05](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md):**
- Blei, Kucukelbir y McAuliffe (fuente S1) presentan la inferencia variacional como un método de aprendizaje automático que aproxima densidades difíciles, como las posteriores bayesianas, mediante optimización: se escoge una familia de densidades y se busca el miembro más cercano al objetivo en divergencia de Kullback–Leibler.
- 🎯 **Por qué importa:** Con miles de parámetros o millones de datos, un muestreador puede tardar horas o días. La inferencia variacional (VI) elige una familia de distribuciones manejables, por ejemplo gaussianas, y busca dentro de ella la más cercana a la posterior.

📘 **Dónde se aprende** (1 clase): [B19-C05 · Inferencia variacional](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md).

### Divergencia logarítmica

- La divergencia logarítmica es el crecimiento de `t` como `ln(1/δ)` al acercarse a `r_s(1 + δ)`.

🎯 **Por qué importa (clase B27-C08):** Para quien cae, el horizonte se cruza en un tiempo finito y, en un agujero grande, sin marea notable; para quien observa desde lejos, la caída parece no terminar. La decisión central: ¿cuánto dura la caída en cada reloj y qué marea se siente en el horizonte?

📘 **Dónde se aprende** (1 clase): [B27-C08 · Horizonte de sucesos](../programa/clases/B27/B27-C08-horizonte-de-sucesos/CLASE.md).

### Diversidad

- La diversidad cuenta valores distintos del atributo sensible por grupo.

💡 **Cómo se explica en la clase [B124-C13](../programa/clases/B124/B124-C13-etica-de-investigacion-y-datos/CLASE.md):**
- Dentro de un grupo de `k` personas puede haber un solo valor del atributo sensible: la diversidad mínima de ingresos es `2`.
- Por diversidad: valores sensibles distintos por grupo.
- 🎯 **Por qué importa:** Abrir datos sin proteger a las personas es un daño, y proteger sin medir es una promesa vacía. La decisión central: ¿cuánto generalizar los datos para que ninguna persona sea identificable y cuánta información se pierde?

📘 **Dónde se aprende** (1 clase): [B124-C13 · Ética de investigación y datos](../programa/clases/B124/B124-C13-etica-de-investigacion-y-datos/CLASE.md).

### Diversidad de estaciones

- La diversidad de estaciones usa varias estaciones terrestres separadas para que no estén cubiertas a la vez.

🎯 **Por qué importa (clase B92-C04):** Un enlace espacial es perfecto hasta que llega a las últimas decenas de kilómetros. La decisión central: ¿cuánto margen exige la turbulencia y cuántas estaciones exige la nubosidad para cumplir una disponibilidad?

📘 **Dónde se aprende** (1 clase): [B92-C04 · Atmósfera y nubes en enlaces ópticos con la Tierra](../programa/clases/B92/B92-C04-atmosfera-y-nubes-en-enlaces-opticos-con-la-tierra/CLASE.md).

### Dividendo

- El dividendo es lo que se divide y el divisor entre lo que se divide.

🎯 **Por qué importa (clase B03-C01):** Una agencia espacial no «confía» en un cálculo: lo comprueba. Para saber cuánto tarda la Luna en dar una vuelta alrededor de la Tierra basta multiplicar, dividir y respetar el orden de las operaciones; pero un paréntesis mal puesto convierte 27 días en una cifra absurda.

📘 **Dónde se aprende** (1 clase): [B03-C01 · Números y operaciones fundamentales](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md).

### Divisor

- El dividendo es lo que se divide y el divisor entre lo que se divide.
- El divisor entrega `V = V_ref R/(R + R_f)`.
- El divisor de UART `d = f/(16·baud)`.

💡 **Cómo se explica en la clase [B03-C01](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md):**
- Sumar y restar decimales exige alinear la coma; multiplicar, contar las cifras decimales del resultado (la suma de las de los factores); dividir, convertir si hace falta el divisor en entero desplazando la coma en ambos.
- ⚠️ **Error frecuente:** Olvidar paréntesis en el divisor. Se detecta por resultados absurdos.
- 🎯 **Por qué importa:** Una agencia espacial no «confía» en un cálculo: lo comprueba. Para saber cuánto tarda la Luna en dar una vuelta alrededor de la Tierra basta multiplicar, dividir y respetar el orden de las operaciones; pero un paréntesis mal puesto convierte 27 días en una cifra absurda.

📘 **Dónde se aprende** (3 clases): [B03-C01 · Números y operaciones fundamentales](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md); [B85-C25 · Sensores y telemetría térmica](../programa/clases/B85/B85-C25-sensores-y-telemetria-termica/CLASE.md); [B88-C02 · Microcontroladores embarcados](../programa/clases/B88/B88-C02-microcontroladores-embarcados/CLASE.md).

### Divulgación

- Una fuente primaria es un documento de la propia misión o agencia; una de divulgación resume a otras.

🎯 **Por qué importa (clase B104-C01):** Los hitos del vuelo tripulado se citan de memoria y circulan con cifras que difieren entre fuentes (una altitud mínima de 169 km o de 181 km para el primer vuelo orbital). La decisión central: ¿qué cifra histórica puedes usar sin riesgo y cuál debes rotular como no consultada?

📘 **Dónde se aprende** (1 clase): [B104-C01 · Historia de vuelos tripulados](../programa/clases/B104/B104-C01-historia-de-vuelos-tripulados/CLASE.md).

### DLI

- PPFD: flujo de fotones útiles. DLI: mol de fotones por m² y día.

💡 **Cómo se explica en la clase [B106-C12](../programa/clases/B106/B106-C12-agricultura-en-ambiente-controlado/CLASE.md):**
- Paso 1. DLI: `300·10⁻⁶·16·3600 = 17,28 mol/(m² día)`.
- Con 300 µmol/(m² s) durante 16 h, la DLI es 17,28 mol/(m² día) y las lámparas consumen 80 W/m² en promedio.
- 🎯 **Por qué importa:** Cultivar reduce la masa de alimento a lanzar y devuelve oxígeno, pero cuesta mucha área y electricidad. La decisión central: ¿qué fracción de la dieta compensa cultivar dado el costo en área y energía?

📘 **Dónde se aprende** (1 clase): [B106-C12 · Agricultura en ambiente controlado](../programa/clases/B106/B106-C12-agricultura-en-ambiente-controlado/CLASE.md).

### Doble

- El doble reproduce las salidas.

💡 **Cómo se explica en la clase [B88-C42](../programa/clases/B88/B88-C42-simuladores-y-mocks-de-sensores-para-pruebas/CLASE.md):**
- Analogía: un doble de sensor es un actor que imita al sensor y puede «enfermarse» cuando se le pide.
- ⚠️ **Error frecuente:** Presentar el doble como un sensor real. Revisa la sección 10
- 🎯 **Por qué importa:** Para probar el FDIR hace falta provocar fallos que el sensor real no da a pedido. La decisión central: ¿qué características del sensor debe reproducir el doble para que la prueba sea válida?

📘 **Dónde se aprende** (1 clase): [B88-C42 · Simuladores y mocks de sensores para pruebas](../programa/clases/B88/B88-C42-simuladores-y-mocks-de-sensores-para-pruebas/CLASE.md).

### Doble búfer

- El doble búfer alterna entre dos ranuras.

💡 **Cómo se explica en la clase [B88-C35](../programa/clases/B88/B88-C35-reinicio-en-caliente-y-persistencia-de-estado/CLASE.md):**
- El laboratorio prueba el doble búfer y la ranura única.
- Descripción larga: el doble búfer garantiza un estado válido en todos los cortes probados; la ranura única, no.
- 🎯 **Por qué importa:** Un corte durante una escritura deja un registro a medias. La decisión central: ¿qué esquema garantiza que, cortes donde cortes, siempre haya un estado válido recuperable?

📘 **Dónde se aprende** (1 clase): [B88-C35 · Reinicio en caliente y persistencia de estado](../programa/clases/B88/B88-C35-reinicio-en-caliente-y-persistencia-de-estado/CLASE.md).

### Doble cobertura

- La doble cobertura significa que `q` y `−q` representan la misma rotación (S1).
- La doble cobertura dice que `q` y `−q` son la misma actitud.

🎯 **Por qué importa (clase B10-C15):** Un seguidor estelar entrega la actitud del satélite varias veces por segundo; el sistema de control la combina con las lecturas de giróscopos, la propaga y la compara con la actitud deseada. Hacerlo con ángulos de Euler es frágil; hacerlo con matrices cuesta más y acumula deriva.

📘 **Dónde se aprende** (2 clases): [B10-C15 · Cuaterniones unitarios](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md); [B87-C02 · Representaciones de orientación](../programa/clases/B87/B87-C02-representaciones-de-orientacion/CLASE.md).

### Doble precisión

- Un número en doble precisión (IEEE 754 *binary64*) tiene 1 bit de signo, 11 de exponente y 52 de mantisa (53 cifras binarias efectivas), es decir, unas 15 a 17 cifras decimales; la documentación de Python confirma los 53 bits de precisión (S1).

💡 **Cómo se explica en la clase [B11-C25](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md):**
- En doble precisión, `cos(10⁻⁸)` se redondea a `1` exactamente y la resta ingenua da `0`: error relativo del 100 %.
- Equivalente accesible a una tabla de efectos (cálculo, doble precisión):
- ⚠️ **Error frecuente:** Creer que la doble precisión elimina el redondeo. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Un programa de ciencias espaciales hace miles de millones de operaciones. Si una resta pierde 16 cifras en una sola operación, el resultado completo es basura sin que el programa se detenga.

📘 **Dónde se aprende** (1 clase): [B11-C25 · Aritmética de punto flotante y errores de redondeo](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md).

### Doble rendija

- La doble rendija produce franjas de espaciado `λL/d`.
- La doble rendija de separación `d`.

💡 **Cómo se explica en la clase [B31-C01](../programa/clases/B31/B31-C01-dualidad-onda-particula/CLASE.md):**
- El montaje de doble rendija (electrones de 50 keV, `d = 1 µm`, `L = 1 m`) es ilustrativo.
- 🎯 **Por qué importa:** Sin la dualidad no se entiende la difracción de electrones, los microscopios electrónicos ni la estructura atómica. La decisión central: ¿cuándo importa la longitud de onda de un objeto y cómo se ve en un experimento?

📘 **Dónde se aprende** (2 clases): [B31-C01 · Dualidad onda-partícula](../programa/clases/B31/B31-C01-dualidad-onda-particula/CLASE.md); [B42-C04 · Difracción de aperturas](../programa/clases/B42/B42-C04-difraccion-de-aperturas/CLASE.md).

### Doble uso

- Doble uso es el que sirve a fines civiles y militares.
- Un artículo de doble uso sirve para fines civiles y militares.

💡 **Cómo se explica en la clase [B119-C17](../programa/clases/B119/B119-C17-conflictos-y-normas-humanitarias-aplicables/CLASE.md):**
- El ejemplo conductor: 100 000 objetos sintéticos de doble uso (10 % militares) con un indicador observable gaussiano (civil media 0, militar media 2) y costes ilustrativos de error 10 y 1.
- 🎯 **Por qué importa:** C11 trata los límites militares del tratado; esta clase aborda cómo razonar la distinción bajo incertidumbre, un tema que ninguna clase del bloque cubre y que exige cautela jurídica. La decisión central: ¿cómo cambia el umbral de decisión cuando equivocarse en un sentido es mucho más grave que en el otro?

📘 **Dónde se aprende** (2 clases): [B119-C17 · Conflictos y normas humanitarias aplicables](../programa/clases/B119/B119-C17-conflictos-y-normas-humanitarias-aplicables/CLASE.md); [B125-C05 · Control de exportaciones y transferencia de tecnología](../programa/clases/B125/B125-C05-control-de-exportaciones-y-transferencia-de-tecnologia/CLASE.md).

### Doblete acromático

- El doblete acromático anula el cromatismo primario.

🎯 **Por qué importa (clase B41-C15):** Un refractor sin color necesita combinar vidrios. La decisión central: ¿cuánto color queda con dos o tres vidrios?

📘 **Dónde se aprende** (2 clases): [B41-C15 · Refractores acromáticos y apocromáticos](../programa/clases/B41/B41-C15-refractores-acromaticos-y-apocromaticos/CLASE.md); [B43-C21 · Selección de vidrios ópticos: catálogos, homogeneidad y diagramas](../programa/clases/B43/B43-C21-seleccion-de-vidrios-opticos-catalogos-homogeneidad-y-diagramas/CLASE.md).

### Dobson

- Un refractor reúne la luz con lentes; un reflector usa espejos y puede necesitar ajustar sus espejos (*colimación*); un Dobson es un reflector sobre una montura simple (S3).

💡 **Cómo se explica en la clase [B08-C14](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md):**
- Según Night Sky Network (S3): los refractores usan lentes, necesitan poco mantenimiento y suelen ser más grandes y caros que un reflector de potencia similar; los reflectores usan espejos y pueden requerir colimación; los Dobson son reflectores sobre una montura sencilla, fáciles de sacar y usar, una elección común de principiantes.
- Con el Dobson de 200 mm y F = 1200 mm: `N = 1200/200 = 6`.
- 🎯 **Por qué importa:** Un telescopio de juguete anuncia «600×» y decepciona. La pregunta motivadora: ¿qué telescopio me conviene y qué podré ver con él?

📘 **Dónde se aprende** (1 clase): [B08-C14 · Telescopios de iniciación](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md).

### Dockerfile

- Un Dockerfile es el texto con las instrucciones para construirla (`FROM`, `COPY`, `RUN`, `WORKDIR`, `USER`, `CMD`).

💡 **Cómo se explica en la clase [B14-C17](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md):**
- El Dockerfile descuidado (`FROM python:latest`, `COPY . /app`, `RUN pip install numpy scipy`, `CMD python …`) incumple las seis: 6 hallazgos.
- Con la huella encadenada del laboratorio, el Dockerfile revisado tiene 7 instrucciones.
- 🎯 **Por qué importa:** Tu análisis funciona con el bloqueo de C12 en tu equipo, pero en el servidor del laboratorio falla porque falta una biblioteca del sistema. La pregunta motivadora es: ¿cómo entrego el análisis junto con todo lo que necesita para correr, de modo que otra persona lo ejecute igual?

📘 **Dónde se aprende** (1 clase): [B14-C17 · Contenedores y ambientes científicos](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md).

### Docstring

- Una docstring es la cadena al inicio de un módulo, clase o función que lo describe; la primera línea es un resumen corto, y el resto explica argumentos, valores devueltos, efectos y excepciones (S2).
- Una docstring documenta un módulo, función o clase (S4).

💡 **Cómo se explica en la clase [B07-C06](../programa/clases/B07/B07-C06-funciones-y-modularidad/CLASE.md):**
- La docstring es lo que ve quien llame `help(razon_kepler)`.
- 🎯 **Por qué importa:** Copiar y pegar el mismo cálculo en cinco sitios es la forma más rápida de tener cinco versiones distintas y un error corregido solo en una. Una función concentra la lógica en un lugar, le da un nombre que expresa su intención y permite probarla aislada.

📘 **Dónde se aprende** (2 clases): [B07-C06 · Funciones y modularidad](../programa/clases/B07/B07-C06-funciones-y-modularidad/CLASE.md); [B07-C19 · Documentación y reproducibilidad](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md).

### Doctrina declarada

- Una doctrina declarada es una posición publicada.

💡 **Cómo se explica en la clase [B119-C26](../programa/clases/B119/B119-C26-doctrinas-y-politicas-espaciales-declaradas-publicamente/CLASE.md):**
- XI (informar en la mayor medida posible), un marco contra el que puede leerse una doctrina declarada.
- 🎯 **Por qué importa:** C11 y C12 tratan los límites militares y la historia; ninguna clase enseña a leer doctrinas públicas con rigor. La lectura real de documentos oficiales exige fuentes que no se consultaron aquí.

📘 **Dónde se aprende** (1 clase): [B119-C26 · Doctrinas y políticas espaciales declaradas públicamente](../programa/clases/B119/B119-C26-doctrinas-y-politicas-espaciales-declaradas-publicamente/CLASE.md).

### Documentar

- Documentar es escribir lo necesario para entender y usar el código y los datos.

💡 **Cómo se explica en la clase [B07-C19](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md):**
- Documentar no es un adorno: se puede comprobar de forma automática, aunque que exista no garantiza que sea buena.
- 🎯 **Por qué importa:** Un resultado que solo su autor puede obtener, y solo el día en que lo obtuvo, es una anécdota. Cuando pasan seis meses, no sabrás con qué datos, con qué versión ni con qué semilla lo generaste.

📘 **Dónde se aprende** (1 clase): [B07-C19 · Documentación y reproducibilidad](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md).

### DoD

- El DoD es la fracción descargada.
- SOC: estado de carga. DoD: profundidad de descarga.

💡 **Cómo se explica en la clase [B86-C05](../programa/clases/B86/B86-C05-baterias-de-ion-litio/CLASE.md):**
- Con la ley ilustrativa `N = 3000 (0,8/DoD)^1,6`, el DoD que da esa vida es `0,8 (3000/N)^(1/1,6) = 20,15 %` en forma cerrada y por bisección `0,201501` en fracción (diferencia `0,0e+00`).
- La descarga a potencia constante con `OCV = 3,3 + 0,8 s` por celda y `0,05 Ω` por celda da un DoD de `13,95 %` frente al planificado de `15,54 %`: diferencia relativa de `10,20 %`.
- ⚠️ **Error frecuente:** Dimensionar con DoD de `100 %`. Se corrige con 8.1.
- 🎯 **Por qué importa:** Una batería de órbita baja hace unos `5400` ciclos al año. Dimensionarla por la energía de un solo eclipse sin mirar la profundidad de descarga la agota mucho antes del fin de la misión.

📘 **Dónde se aprende** (2 clases): [B86-C05 · Baterías de ion-litio](../programa/clases/B86/B86-C05-baterias-de-ion-litio/CLASE.md); [B96-C12 · Gestión de energía en operaciones](../programa/clases/B96/B96-C12-gestion-de-energia-en-operaciones/CLASE.md).

### Domina

- Un sitio domina a otro si es al menos igual en todo y mejor en algo.
- Un diseño domina a otro si su tiempo es menor o igual y su carga útil es mayor o igual, con una desigualdad estricta.
- Una solución domina a otra si es mejor o igual en todos los criterios y mejor en alguno.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B81-C11](../programa/clases/B81/B81-C11-optimizacion-multicriterio-y-frentes-de-pareto/CLASE.md):**
- Paso 3 · Conclusión. A domina a B: B no está en el frente.
- Paso 4 · Contraste. Un C de 90 d y 600 kg no es dominado por A (más rápido) ni lo domina (menos carga).
- 🎯 **Por qué importa:** Un peso único esconde la decisión; un frente la muestra completa. La decisión central: ¿cuáles diseños son eficientes y cuál se elige si no se conocen de antemano los pesos?

📘 **Dónde se aprende** (4 clases): [B67-C01 · Selección de sitios de extracción con criterios múltiples](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md); [B81-C11 · Optimización multicriterio y frentes de Pareto](../programa/clases/B81/B81-C11-optimizacion-multicriterio-y-frentes-de-pareto/CLASE.md); [B91-C06 · Selección y compromiso de diseño de antenas](../programa/clases/B91/B91-C06-seleccion-y-compromiso-de-diseno-de-antenas/CLASE.md); [B124-C12 · Evaluación de retorno científico](../programa/clases/B124/B124-C12-evaluacion-de-retorno-cientifico/CLASE.md).

### Dominancia

- La dominancia ocurre cuando otra opción es igual o mejor en todos los criterios y estrictamente mejor en uno.
- Una dominancia ocurre cuando una alternativa gana en todos los criterios.

🎯 **Por qué importa (clase B78-C20):** Cada arquitectura gana en una dimensión y pierde en otra. La decisión central: ¿qué opciones no están dominadas por otra en propelente y en tiempo, y cómo cambia el resultado con la potencia disponible?

📘 **Dónde se aprende** (2 clases): [B78-C20 · Comparación no operativa de arquitecturas de propulsión](../programa/clases/B78/B78-C20-comparacion-no-operativa-de-arquitecturas-de-propulsion/CLASE.md); [B83-C07 · Arquitecturas de sistemas](../programa/clases/B83/B83-C07-arquitecturas-de-sistemas/CLASE.md).

### Dominante

- La condición de energía débil pide `ρ ≥ 0` y `ρ + p ≥ 0`; la dominante, `ρ ≥ |p|`; la fuerte, `ρ + 3p ≥ 0`.

🎯 **Por qué importa (clase B39-C04):** La fuente de la gravedad es `T^ab`. La decisión central: ¿qué tensor describe la materia y qué condiciones debe cumplir para ser físicamente razonable?

📘 **Dónde se aprende** (1 clase): [B39-C04 · Tensor de energía-momento y fuentes de curvatura](../programa/clases/B39/B39-C04-tensor-de-energia-momento-y-fuentes-de-curvatura/CLASE.md).

### Dominio

- Una función `f` asigna a cada valor `x` de un conjunto (el dominio) un único valor `f(x)`; el conjunto de los resultados es el rango.
- Una función de dos variables asigna a cada par `(x, y)` de su dominio un número `f(x, y)` (S1, §1.5).

💡 **Cómo se explica en la clase [B04-C04](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md):**
- El dominio de la fórmula y el dominio físico son cosas distintas; esta clase declara el segundo.
- X["Entrada x<br/>(dominio, con unidad)"] --> F["Regla f<br/>y = k x^n"]
- ⚠️ **Error frecuente:** Confundir dominio de la fórmula con dominio físico. Se corrige con el ejercicio 8.
- 🎯 **Por qué importa:** Un astrónomo no solo calcula un valor: pregunta «¿qué pasa con el periodo de un planeta si su órbita es el doble de grande?». Responderlo con un solo caso no basta; hace falta la regla que liga ambas magnitudes.

📘 **Dónde se aprende** (2 clases): [B04-C04 · Funciones y gráficas](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md); [B09-C15 · Funciones de varias variables](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md).

### Dominio de electrones

- Un dominio de electrones es una región alrededor del átomo central donde hay electrones: cada enlace (simple, doble o triple) cuenta como uno, y cada par solitario también.

🎯 **Por qué importa (clase B06-C05):** El dióxido de carbono es el 95,1 % de la atmósfera de Marte en volumen (S2), y los hielos de las nubes densas del medio interestelar contienen, según un estudio con el telescopio James Webb, agua y CO₂ entre otras especies (S3, que se leyó sólo en resumen).

📘 **Dónde se aprende** (1 clase): [B06-C05 · Moléculas y geometría molecular](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md).

### Dominio de entrenamiento

- El dominio de entrenamiento es el rango de entradas cubierto.

🎯 **Por qué importa (clase B17-C04):** Un simulador de trayectoria, de aerodinámica o de transporte de radiación puede tardar minutos u horas por ejecución. Para explorar miles de combinaciones de parámetros (un análisis de sensibilidad, una propagación de incertidumbre, una optimización) no alcanza el tiempo.

📘 **Dónde se aprende** (1 clase): [B17-C04 · Modelos sustitutos (surrogates)](../programa/clases/B17/B17-C04-modelos-sustitutos-surrogates/CLASE.md).

### Dominio de validación

- El dominio de validación es el rango (cuerpo, tiempo, precisión) en que la comparación respalda el uso del modelo.
- El dominio de verificación y el dominio de validación son los rangos en que se comprobó cada cosa.

💡 **Cómo se explica en la clase [B23-C08](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md):**
- Exige mantener un registro del dominio de verificación y del dominio de validación.
- 🎯 **Por qué importa:** Un conjunto de pruebas que pasan no es un informe. Quien debe decidir si usar el código necesita saber para qué uso se evaluó, con qué criterios, qué falló y qué no se probó.

📘 **Dónde se aprende** (2 clases): [B23-C05 · Validación con conjuntos oficiales](../programa/clases/B23/B23-C05-validacion-con-conjuntos-oficiales/CLASE.md); [B23-C08 · Informe de verificación y validación](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md).

### Dominio de validez

- El dominio de validez es el rango en que el modelo se ha comprobado y se puede usar.
- El dominio de validez es el rango de entradas para el que el modelo es correcto.

💡 **Cómo se explica en la clase [B14-C01](../programa/clases/B14/B14-C01-arquitectura-de-software-cientifico/CLASE.md):**
- Y el dominio de validez se verifica y se rechaza con un error explícito, en vez de devolver un número sin sentido.
- 🎯 **Por qué importa:** Un script de 300 líneas que lee un archivo, calcula una órbita, dibuja una figura y escribe un informe funciona hasta el día en que cambias el archivo de entrada. Entonces no sabes si un resultado distinto viene de los datos, de la fórmula o de un error nuevo.

📘 **Dónde se aprende** (2 clases): [B01-C17 · Construcción de modelos científicos](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md); [B14-C01 · Arquitectura de software científico](../programa/clases/B14/B14-C01-arquitectura-de-software-cientifico/CLASE.md).

### Dominio de verificación

- El dominio de verificación y el dominio de validación son los rangos en que se comprobó cada cosa.

💡 **Cómo se explica en la clase [B23-C08](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md):**
- Exige mantener un registro del dominio de verificación y del dominio de validación.
- 🎯 **Por qué importa:** Un conjunto de pruebas que pasan no es un informe. Quien debe decidir si usar el código necesita saber para qué uso se evaluó, con qué criterios, qué falló y qué no se probó.

📘 **Dónde se aprende** (1 clase): [B23-C08 · Informe de verificación y validación](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md).

### Domo

- Un domo es un edificio abovedado de magma muy viscoso.

💡 **Cómo se explica en la clase [B70-C02](../programa/clases/B70/B70-C02-domos-volcanicos-y-vulcanismo-evolucionado/CLASE.md):**
- Límite: un domo real tiene corteza, cristales y enfriamiento.
- El ejemplo conductor es un domo sintético de `R = 1500 m`, `ρ = 2400 kg/m³` y `τ = 10⁵ Pa`: en la Tierra su altura central es `112,9 m` y su volumen `0,4256 km³`; con la gravedad de Marte, `183,1 m` y `0,6901 km³`.
- 🎯 **Por qué importa:** Una colina empinada de lava puede tener una altura que solo depende del material y de `g`. La decisión central: ¿qué altura puede alcanzar un domo de resistencia dada y qué cambiaría en otro mundo?

📘 **Dónde se aprende** (1 clase): [B70-C02 · Domos volcánicos y vulcanismo evolucionado](../programa/clases/B70/B70-C02-domos-volcanicos-y-vulcanismo-evolucionado/CLASE.md).

### DOP

- El DOP (*dilution of precision*) amplifica el error: `PDOP = √(Q₁₁+Q₂₂+Q₃₃)` con `Q = (GᵀG)⁻¹`.

💡 **Cómo se explica en la clase [B57-C10](../programa/clases/B57/B57-C10-geodesia-mediante-gnss/CLASE.md):**
- El error 3D simulado coincide con `PDOP × σ` en ambos casos: el DOP resume cuánto amplifica la geometría el ruido de medición.
- Paso 1 · DOP. `PDOP = 2,80` con ocho satélites repartidos.
- ⚠️ **Error frecuente:** Creer que más satélites siempre mejora el DOP. Depende de la distribución (8.2).
- 🎯 **Por qué importa:** La geodesia con GNSS mide posiciones de estaciones con precisión de milímetros a centímetros y sirve para ver cómo se mueve la corteza. Pero la precisión depende de la geometría de los satélites.

📘 **Dónde se aprende** (1 clase): [B57-C10 · Geodesia mediante GNSS](../programa/clases/B57/B57-C10-geodesia-mediante-gnss/CLASE.md).

### Doppler

- Rango: distancia estación–satélite. Doppler: corrimiento de frecuencia.

💡 **Cómo se explica en la clase [B96-C05](../programa/clases/B96/B96-C05-estaciones-de-seguimiento/CLASE.md):**
- Las relaciones de geometría y de Doppler son estándar y las verifica el laboratorio; no se tomaron de una fuente concreta.
- (1) El Doppler cruza cero a 625 s, igual que la distancia mínima de 968,9 km.
- ⚠️ **Error frecuente:** Invertir el signo del Doppler. Positivo al acercarse (8.3)
- 🎯 **Por qué importa:** Para que una antena apunte y un receptor enganche, la estación debe conocer de antemano el azimut, la elevación y el corrimiento de frecuencia. La decisión central: ¿hacia dónde apuntar y qué frecuencia esperar en cada instante?

📖 **Explicado a fondo:** [Doppler (efecto)](esencial/esencial-d-l.md#doppler-efecto) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B96-C05 · Estaciones de seguimiento](../programa/clases/B96/B96-C05-estaciones-de-seguimiento/CLASE.md).

### Doppler clásico

- El Doppler clásico `z = v/c`; el relativista `1 + z = √((1+β)/(1−β))`.

🎯 **Por qué importa (clase B45-C12):** Las velocidades radiales descubren planetas, binarias y la expansión del universo. La decisión central: ¿cómo se pasa de un corrimiento a una velocidad y con qué precisión?

📘 **Dónde se aprende** (1 clase): [B45-C12 · Efecto Doppler en espectros](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md).

### Doppler de dos sentidos

- El Doppler de dos sentidos mide la diferencia entre la frecuencia emitida y la recibida tras el viaje de ida y vuelta.

💡 **Cómo se explica en la clase [B74-C04](../programa/clases/B74/B74-C04-doppler-de-navegacion/CLASE.md):**
- Con una portadora ilustrativa de `7,2 GHz` y una velocidad radial de `30 km/s` el Doppler de dos sentidos es `-1440,997 kHz`; la sensibilidad es `48,0332 Hz` por m/s.
- 🎯 **Por qué importa:** Una velocidad radial de `1 mm/s` produce un desplazamiento de decenas de milihercios, medible; por eso el Doppler es el observable más preciso de la navegación en espacio profundo. La decisión central: ¿qué información da el Doppler (velocidad en la línea de visión) y qué no (posición transversal)?

📘 **Dónde se aprende** (1 clase): [B74-C04 · Doppler de navegación](../programa/clases/B74/B74-C04-doppler-de-navegacion/CLASE.md).

### Doppler de ida

- El Doppler de ida es `f_D = −f ṙ/c`, con `ṙ` la velocidad radial (positiva si se aleja).

💡 **Cómo se explica en la clase [B89-C15](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md):**
- Un transpondedor con razón `880/749 = 1,17490` devuelve la portadora ascendente (7,19 GHz, ilustrativa) multiplicada por la razón; el Doppler de ida y vuelta en el TCA es `-0,000 kHz` y en el AOS `376,4 kHz`: más del doble del de ida porque cuenta dos trayectos.
- *Descripción textual:* la geometría da la velocidad radial; con ella se calcula el Doppler, su tasa en el TCA (de donde se estima la distancia mínima) y el Doppler de ida y vuelta con el transpondedor.
- ⚠️ **Error frecuente:** Olvidar que el Doppler de ida y vuelta cuenta dos trayectos. Se corrige con 8.4.
- 🎯 **Por qué importa:** El Doppler es la medida básica de rastreo: se usa para determinar la órbita y obliga a diseñar los lazos de portadora y los planes de frecuencia. La decisión central: ¿cuánto se desplaza la frecuencia durante una pasada y qué información de la órbita contiene?

📘 **Dónde se aprende** (1 clase): [B89-C15 · Rastreo y Doppler](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md).

### Doppler de ida y vuelta

- El Doppler de ida y vuelta coherente recibe `f_rx = (880/749) f_up (1 + …)`: la nave devuelve la portadora multiplicada por la razón de transpondedor (880/749 se usa aquí como ilustración).

💡 **Cómo se explica en la clase [B89-C15](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md):**
- Un transpondedor con razón `880/749 = 1,17490` devuelve la portadora ascendente (7,19 GHz, ilustrativa) multiplicada por la razón; el Doppler de ida y vuelta en el TCA es `-0,000 kHz` y en el AOS `376,4 kHz`: más del doble del de ida porque cuenta dos trayectos.
- *Descripción textual:* la geometría da la velocidad radial; con ella se calcula el Doppler, su tasa en el TCA (de donde se estima la distancia mínima) y el Doppler de ida y vuelta con el transpondedor.
- ⚠️ **Error frecuente:** Olvidar que el Doppler de ida y vuelta cuenta dos trayectos. Se corrige con 8.4.
- 🎯 **Por qué importa:** El Doppler es la medida básica de rastreo: se usa para determinar la órbita y obliga a diseñar los lazos de portadora y los planes de frecuencia. La decisión central: ¿cuánto se desplaza la frecuencia durante una pasada y qué información de la órbita contiene?

📘 **Dónde se aprende** (1 clase): [B89-C15 · Rastreo y Doppler](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md).

### Doppler relativista

- El Doppler relativista de una fuente que se aleja con `β` da `f_r/f_e = √((1−β)/(1+β)) = e^{−atanh β}`.
- El Doppler relativista da `v = c((1+z)²−1)/((1+z)²+1)`.

💡 **Cómo se explica en la clase [B26-C06](../programa/clases/B26/B26-C06-principio-de-equivalencia/CLASE.md):**
- El Doppler relativista da `1 − √((1−β)/(1+β))`.
- 🎯 **Por qué importa:** Los relojes de los satélites de navegación van a un ritmo ligeramente distinto de los terrestres, y un maser en una torre ve su frecuencia cambiar con la altura. Todo eso se deduce de la equivalencia entre aceleración y gravedad.

📘 **Dónde se aprende** (2 clases): [B26-C06 · Principio de equivalencia](../programa/clases/B26/B26-C06-principio-de-equivalencia/CLASE.md); [B26-C11 · Expansión cósmica y ley de Hubble-Lemaître](../programa/clases/B26/B26-C11-expansion-cosmica-y-ley-de-hubble-lemaitre/CLASE.md).

### Dormand–Prince 5(4)

- RK4 es de orden 4. Dormand–Prince 5(4) es un par encajado de órdenes 5 y 4 cuya diferencia estima el error local.

🎯 **Por qué importa (clase B72-C18):** Un integrador mal elegido da una órbita que parece correcta y está equivocada en kilómetros. La decisión central: ¿qué método, paso o tolerancia da el error de posición que necesita la tarea al menor coste, y cómo saber que no engaña?

📘 **Dónde se aprende** (1 clase): [B72-C18 · Integración numérica perturbada](../programa/clases/B72/B72-C18-integracion-numerica-perturbada/CLASE.md).

### Dos corrientes

- La relación de dos corrientes `T_s⁴ = T_e⁴ (1 + 3τ/4)` es la solución gris en equilibrio radiativo.

🎯 **Por qué importa (clase B54-C09):** La diferencia entre la temperatura de equilibrio (B54-C03) y la observada necesita una causa. La pregunta motivadora: ¿qué opacidad infrarroja hace falta para explicar la temperatura de superficie de cada mundo?

📘 **Dónde se aprende** (1 clase): [B54-C09 · Efecto invernadero](../programa/clases/B54/B54-C09-efecto-invernadero/CLASE.md).

### Dos cuerpos

- El problema de dos cuerpos describe un punto en el campo de una masa central.

💡 **Cómo se explica en la clase [B58-C02](../programa/clases/B58/B58-C02-dinamica-de-asteroides/CLASE.md):**
- El modelo de dos cuerpos solo ubica *dónde* mirar.
- Analítica: Kepler da el periodo exacto de dos cuerpos.
- 🎯 **Por qué importa:** Predecir la posición de un asteroide dentro de décadas exige un integrador que se pueda verificar. Saber que un esquema numérico converge con el orden esperado es lo que da confianza antes de añadir perturbaciones.

📘 **Dónde se aprende** (1 clase): [B58-C02 · Dinámica de asteroides](../programa/clases/B58/B58-C02-dinamica-de-asteroides/CLASE.md).

### Dos ejes

- un eje gira para seguir al Sol en el plano; dos ejes lo siguen siempre.

💡 **Cómo se explica en la clase [B86-C04](../programa/clases/B86/B86-C04-orientacion-solar-y-eclipses/CLASE.md):**
- Con dos ejes el coseno medio es `1 − f`; con un eje es `(1 − f) cosβ`; con el ala fija al cenit es mucho menor (`≈ cosβ/π` antes de restar el eclipse).
- 🎯 **Por qué importa:** El eclipse más largo fija el tamaño de la batería y el peor `β` fija el de la ala. Un diseño que mire solo `β = 0` ignora que a `β` alto no hay eclipse pero el coseno cae.

📘 **Dónde se aprende** (1 clase): [B86-C04 · Orientación solar y eclipses](../programa/clases/B86/B86-C04-orientacion-solar-y-eclipses/CLASE.md).

### Dos fases

- El modelo de tres fases trata gas, superficie y manto como reservorios distintos; el de dos fases, solo gas y superficie.

💡 **Cómo se explica en la clase [B60-C04](../programa/clases/B60/B60-C04-balance-quimico-gas-grano-modelos-de-tres-fases/CLASE.md):**
- Un modelo de dos fases mantiene 79 monocapas como «superficie activa»; el de tres fases, una.
- El de dos fases libera todo entre 20 y 25 K; el de tres fases libera la superficie y deja el manto, que sale con la lentitud del intercambio.
- 🎯 **Por qué importa:** Un modelo de dos fases trata todo el hielo como si estuviera expuesto en la superficie; en la realidad la mayor parte queda enterrada bajo capas posteriores. La decisión central: ¿qué cambia en la predicción de cuánto hielo se libera al calentar si se distingue la superficie del manto?

📘 **Dónde se aprende** (1 clase): [B60-C04 · Balance químico gas-grano: modelos de tres fases](../programa/clases/B60/B60-C04-balance-quimico-gas-grano-modelos-de-tres-fases/CLASE.md).

### Dos haces

- Los dos haces son dos poblaciones que se cruzan.

💡 **Cómo se explica en la clase [B35-C03](../programa/clases/B35/B35-C03-inestabilidades-de-plasma-cineticas-y-de-fluido/CLASE.md):**
- Para dos haces fríos simétricos la tasa máxima es `ω_p/(2√2) = 0,353553 ω_p` en `k v₀ = 0,6124 ω_p`.
- 🎯 **Por qué importa:** Las inestabilidades limitan los equilibrios y convierten energía libre en turbulencia. La decisión central: ¿para qué número de onda y para qué cizalladura crece la perturbación y cuánto?

📘 **Dónde se aprende** (1 clase): [B35-C03 · Inestabilidades de plasma: cinéticas y de fluido](../programa/clases/B35/B35-C03-inestabilidades-de-plasma-cineticas-y-de-fluido/CLASE.md).

### Dosis

- Una dosis es la energía absorbida por masa.
- La dosis `D` es la energía depositada por molécula (eV/molécula).
- La dosis es `p ∫ C dt`.

💡 **Cómo se explica en la clase [B33-C08](../programa/clases/B33/B33-C08-dosis-de-radiacion-en-aviacion/CLASE.md):**
- El juguete exagera el crecimiento porque supone un solo componente sin cascada; no debe usarse para estimar dosis.
- ⚠️ **Error frecuente:** Usar el juguete para dosis. Se corrige con 8.3.
- 🎯 **Por qué importa:** La altitud y la profundidad atmosférica determinan cuánta radiación llega. La decisión central: ¿cuánto menos atmósfera hay a la altitud de vuelo?

📘 **Dónde se aprende** (3 clases): [B33-C08 · Dosis de radiación en aviación](../programa/clases/B33/B33-C08-dosis-de-radiacion-en-aviacion/CLASE.md); [B68-C03 · Irradiación de hielos por rayos cósmicos y UV: radiólisis y productos](../programa/clases/B68/B68-C03-irradiacion-de-hielos-por-rayos-cosmicos-y-uv-radiolisis-y-productos/CLASE.md); [B110-C02 · Protocolos operativos de aislamiento de un tripulante enfermo o contaminado](../programa/clases/B110/B110-C02-protocolos-operativos-de-aislamiento-de-un-tripulante-enfermo-o-contaminado/CLASE.md).

### Dosis absorbida

- La dosis absorbida `D` se mide en gray.
- La dosis absorbida `D` (Gy = J/kg) es energía por masa.
- La dosis absorbida `D` es la energía depositada por unidad de masa, `D = E/m`, y su unidad es el gray (1 Gy = 1 J/kg).

💡 **Cómo se explica en la clase [B105-C06](../programa/clases/B105/B105-C06-radiacion-ionizante-y-exposicion/CLASE.md):**
- D["dosis absorbida D<br/>Gy"] --> H["H = w_R D<br/>Sv"]
- *Descripción textual:* la dosis absorbida se pondera por radiación y por tejido para dar la dosis efectiva; se acumula en un presupuesto de misión, se compara con un límite y se acompaña de su incertidumbre.
- 🎯 **Por qué importa:** La dosis no se «lee»: se calcula a partir de una dosis absorbida, de factores de calidad y de ponderación, y esos factores tienen incertidumbre. La decisión central: ¿qué fracción del límite de carrera consume una misión y con qué probabilidad lo supera una secuencia de misiones?

📘 **Dónde se aprende** (3 clases): [B64-C01 · Radiotolerancia biológica y reparación del ADN](../programa/clases/B64/B64-C01-radiotolerancia-biologica-y-reparacion-del-adn/CLASE.md); [B105-C06 · Radiación ionizante y exposición](../programa/clases/B105/B105-C06-radiacion-ionizante-y-exposicion/CLASE.md); [B112-C01 · Magnitudes dosimétricas: dosis absorbida, LET y eficacia biológica](../programa/clases/B112/B112-C01-magnitudes-dosimetricas-dosis-absorbida-let-y-eficacia-biologica/CLASE.md).

### Dosis característica

- La dosis característica `D₀` es la que reduce la población a `1/e`.

💡 **Cómo se explica en la clase [B55-C17](../programa/clases/B55/B55-C17-compuestos-prebioticos/CLASE.md):**
- Un aminoácido hipotético con dosis característica `D₀ = 10⁶ Gy` y tasa de dosis de `10⁻³ Gy/año` (ambas ilustrativas), y una proporción verdadera de forma L de 0,55 (exceso enantiomérico 0,10).
- 🎯 **Por qué importa:** Que un compuesto prebiótico llegue intacto hasta nosotros depende de cuánta radiación recibió, y que un exceso entre dos formas quirales sea real depende de cuántas moléculas se contaron. La decisión central: ¿cuánto sobrevive y con qué incertidumbre puedo afirmar un exceso enantiomérico distinto de cero?

📘 **Dónde se aprende** (1 clase): [B55-C17 · Compuestos prebióticos](../programa/clases/B55/B55-C17-compuestos-prebioticos/CLASE.md).

### Dosis de gravedad

- La dosis de gravedad sería la relación entre `g` y la respuesta biológica: se desconoce en este texto.

🎯 **Por qué importa (clase B105-C18):** Se puede calcular con exactitud cuánto pesa y cómo se mueve un cuerpo en la Luna; no se puede deducir de eso cuánta gravedad hace falta para mantener el hueso. La decisión central: ¿qué parte de la respuesta a la gravedad parcial es física calculable y qué parte es una pregunta de investigación abierta?

📘 **Dónde se aprende** (1 clase): [B105-C18 · Investigación de efectos de gravedad parcial](../programa/clases/B105/B105-C18-investigacion-de-efectos-de-gravedad-parcial/CLASE.md).

### Dosis efectiva

- La dosis efectiva es `E = Σ_T w_T H_T`, con `w_T` el factor de ponderación del tejido, que representa su contribución relativa al detrimento total y cuya suma vale 1 (definiciones del glosario de ICRP 103, consultado).
- La dosis efectiva `E = Σ w_T H_T` (Sv) pondera por tejido; sus factores los fija la ICRP en su Publicación 103 (2007), página consultada el 2026-11-10 en resumen.

💡 **Cómo se explica en la clase [B105-C06](../programa/clases/B105/B105-C06-radiacion-ionizante-y-exposicion/CLASE.md):**
- *Descripción textual:* la dosis absorbida se pondera por radiación y por tejido para dar la dosis efectiva; se acumula en un presupuesto de misión, se compara con un límite y se acompaña de su incertidumbre.
- Analogía: una cuenta en la que cada gasto se multiplica por un tipo de cambio según la moneda; la dosis efectiva es el total convertido.
- 🎯 **Por qué importa:** La dosis no se «lee»: se calcula a partir de una dosis absorbida, de factores de calidad y de ponderación, y esos factores tienen incertidumbre. La decisión central: ¿qué fracción del límite de carrera consume una misión y con qué probabilidad lo supera una secuencia de misiones?

📘 **Dónde se aprende** (2 clases): [B105-C06 · Radiación ionizante y exposición](../programa/clases/B105/B105-C06-radiacion-ionizante-y-exposicion/CLASE.md); [B112-C02 · Dosis equivalente y dosis efectiva](../programa/clases/B112/B112-C02-dosis-equivalente-y-dosis-efectiva/CLASE.md).

### Dosis equivalente

- La dosis equivalente de un tejido es `H_T = Σ_R w_R D_{T,R}`, con `w_R` el factor de ponderación de la radiación (adimensional) que refleja la mayor eficacia biológica del alto LET; su unidad es el sievert.
- La dosis equivalente `H` se mide en mSv.
- La dosis equivalente `H_T = w_R D_T` (Sv) pondera por el tipo de radiación.

💡 **Cómo se explica en la clase [B105-C06](../programa/clases/B105/B105-C06-radiacion-ionizante-y-exposicion/CLASE.md):**
- Paso 1 · Dosis equivalente diaria. `0,30 mGy·2,5 = 0,75 mSv`.
- 🎯 **Por qué importa:** La dosis no se «lee»: se calcula a partir de una dosis absorbida, de factores de calidad y de ponderación, y esos factores tienen incertidumbre. La decisión central: ¿qué fracción del límite de carrera consume una misión y con qué probabilidad lo supera una secuencia de misiones?

📘 **Dónde se aprende** (3 clases): [B105-C06 · Radiación ionizante y exposición](../programa/clases/B105/B105-C06-radiacion-ionizante-y-exposicion/CLASE.md); [B112-C02 · Dosis equivalente y dosis efectiva](../programa/clases/B112/B112-C02-dosis-equivalente-y-dosis-efectiva/CLASE.md); [B114-C04 · Refugio contra tormentas solares y compartimentos de protección](../programa/clases/B114/B114-C04-refugio-contra-tormentas-solares-y-compartimentos-de-proteccion/CLASE.md).

### Dosis ionizante total

- La dosis ionizante total (TID, en Gy).

🎯 **Por qué importa (clase B47-C14):** El blindaje reduce la dosis hasta que el protón se detiene; los eventos de partícula simple, en cambio, son aleatorios. La decisión central: ¿qué espesor de blindaje y qué probabilidad de eventos son aceptables?

📘 **Dónde se aprende** (1 clase): [B47-C14 · Radiación y degradación](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md).

### Dosis por órbita

- La dosis por órbita es `∫ D dt`.

💡 **Cómo se explica en la clase [B75-C28](../programa/clases/B75/B75-C28-restricciones-de-radiacion-en-trayectorias/CLASE.md):**
- La dosis por órbita es `D₀ R_J³/(86 400)·2π/(h p)` en `u` (con `h` en km²/s y `p` en km).
- Blindaje (`λ = 10 g/cm²`, sintético): factor `0,9048` con 1 g/cm², `0,6065` con 5, `0,3679` con 10 y `0,1353` con 20; la dosis por órbita de la primera órbita baja de `4624` a `4184`, `2805`, `1701` y `626 u`.
- 🎯 **Por qué importa:** Una trayectoria es también un perfil de exposición. La decisión central: ¿cuánta dosis acumula una nave por órbita y cuántas órbitas aguanta, según el periapsis y el blindaje?

📘 **Dónde se aprende** (1 clase): [B75-C28 · Restricciones de radiación en trayectorias](../programa/clases/B75/B75-C28-restricciones-de-radiacion-en-trayectorias/CLASE.md).

### Dosis total ionizante

- La dosis total ionizante acumulada se compara con umbrales de material.

🎯 **Por qué importa (clase B85-C24):** Una celda solar o un polímero no fallan de golpe: pierden prestaciones con la exposición. La decisión central: ¿cuánta potencia queda al final de la misión y cuánto cambia con un blindaje que reduce la fluencia?

📘 **Dónde se aprende** (1 clase): [B85-C24 · Efectos de la radiación ionizante en materiales y electrónica](../programa/clases/B85/B85-C24-efectos-de-la-radiacion-ionizante-en-materiales-y-electronica/CLASE.md).

### Dossier

- El dossier reúne cifras, fuentes y derivaciones.
- El dossier documenta requisitos, cálculos y verificación.

💡 **Cómo se explica en la clase [B28-C20](../programa/clases/B28/B28-C20-caso-de-estudio-de-evento-combinado/CLASE.md):**
- La huella SHA-256 del dossier empieza por `032988a045c269cc`; es estable al reserializar el mismo contenido.
- *Descripción textual:* los resúmenes dan cifras publicadas; se comprueba su coherencia y se calculan magnitudes derivadas; el dossier incluye la lista de lo no consultado y se firma con una huella.
- 🎯 **Por qué importa:** Un caso de estudio sirve si es verificable: cada cifra debe llevar su fuente, y lo calculado debe distinguirse de lo publicado. La decisión central: ¿qué cifras del evento están respaldadas por lo consultado, cuáles se derivan y cuáles quedan fuera?

📘 **Dónde se aprende** (2 clases): [B28-C20 · Caso de estudio de evento combinado](../programa/clases/B28/B28-C20-caso-de-estudio-de-evento-combinado/CLASE.md); [B43-C20 · Proyecto mecánico completo de telescopio](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md).

### Dotación mínima

- La dotación mínima `k` es el número de personas que necesita.

🎯 **Por qué importa (clase B122-C10):** No hay clase equivalente sobre continuidad de funciones institucionales. La decisión central: ¿qué dotación mínima asegura que cada función esencial se cubra con al menos el 99 %?

📘 **Dónde se aprende** (1 clase): [B122-C10 · Planes de continuidad institucional y de operaciones](../programa/clases/B122/B122-C10-planes-de-continuidad-institucional-y-de-operaciones/CLASE.md).

### Dragado

- El dragado (*dredge-up*) es la mezcla convectiva que lleva a la superficie material procesado.

💡 **Cómo se explica en la clase [B24-C21](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md):**
- Tras cada pulso, la convección puede arrastrar material procesado a la envoltura (dragado).
- Si en cada pulso un dragado lleva `ΔM` de material con fracción de masa de carbono `X_C,dr` y de oxígeno `X_O,dr` a la envoltura, la masa de carbono crece en `ΔM X_C,dr` y la envoltura en `ΔM`.
- ⚠️ **Error frecuente:** Olvidar que el dragado también añade masa a la envoltura. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Las estrellas AGB son una fuente importante de carbono, nitrógeno y elementos pesados del medio interestelar, y sus abundancias superficiales son el registro observable de lo que ocurre en su interior.

📘 **Dónde se aprende** (1 clase): [B24-C21 · Rama asintótica de gigantes: pulsos térmicos y proceso s](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md).

### DRO

- Una DRO es una órbita periódica retrógrada y plana alrededor de la Luna.

💡 **Cómo se explica en la clase [B76-C06](../programa/clases/B76/B76-C06-orbitas-dro-dinamica-cislunar-y-operaciones-de-proximidad/CLASE.md):**
- Una DRO de `70.000 km` supera el radio de Hill (`61.274 km`) y permanece ligada porque es periódica y retrógrada.
- Una DRO que cruza `y = 0` a `70.000 km` de la Luna tiene `vy0 = 0,519364` (adimensional), periodo `13,916 d` y `C = 2,92852`; su máxima separación al otro lado es `73.434 km`.
- ⚠️ **Error frecuente:** Buscar la DRO sin continuación. Se corrige con 8.2.
- 🎯 **Por qué importa:** La NRHO es inestable y exige mantenimiento; la DRO es estable. La decisión central: ¿qué se gana y qué se paga al elegir una órbita estable y lejana frente a una NRHO cercana?

📘 **Dónde se aprende** (1 clase): [B76-C06 · Órbitas DRO — Dinámica cislunar y operaciones de proximidad](../programa/clases/B76/B76-C06-orbitas-dro-dinamica-cislunar-y-operaciones-de-proximidad/CLASE.md).

### DSK

- Los tipos descritos por NAIF son SPK (posición y velocidad), CK (orientación de nave), PCK (tamaño, forma y orientación de cuerpos), IK (campo de visión de instrumentos), FK (marcos), LSK (segundos intercalares), SCLK (reloj de nave) y DSK (formas).

🎯 **Por qué importa (clase B74-C21):** Un resultado de navegación depende de qué kernels se cargaron y en qué orden: dos corridas con el mismo código pueden dar trayectorias distintas. La decisión central: ¿cómo declaro, valido y audito el conjunto de kernels de una solución para que sea reproducible?

📘 **Dónde se aprende** (1 clase): [B74-C21 · Kernels SPICE y su uso en navegación](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md).

### Dunas

- Las ripples y dunas son formas que el transporte genera en el lecho.

🎯 **Por qué importa (clase B66-C03):** Marte tiene dunas y una atmósfera cien veces menos densa que la terrestre; Venus, una atmósfera enorme y casi sin viento.

📘 **Dónde se aprende** (1 clase): [B66-C03 · Procesos eólicos: dunas, ripples y erosión planetaria](../programa/clases/B66/B66-C03-procesos-eolicos-dunas-ripples-y-erosion-planetaria/CLASE.md).

### Duplicación de paso

- La duplicación de paso compara un paso de tamaño `h` con dos de tamaño `h/2`; para un método de orden 4, el error del resultado de dos pasos medios es aproximadamente `|s₂ − s₁|/15` (extrapolación de Richardson).

🎯 **Por qué importa (clase B11-C08):** Casi ninguna simulación espacial tiene un ritmo uniforme: una nave que rodea un planeta con un perigeo bajo, una sonda que pasa cerca de una luna, un encuentro cercano entre dos cuerpos. Escoger `h` a mano es adivinar.

📘 **Dónde se aprende** (1 clase): [B11-C08 · Integradores de paso adaptativo](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md).

### Duplicado

- Un duplicado es la misma obra registrada más de una vez, por ejemplo la versión de un manuscrito y la del artículo publicado.
- Un duplicado repite una clave.

💡 **Cómo se explica en la clase [B129-C04](../programa/clases/B129/B129-C04-contribucion-de-medidas-voluntarias-con-control-de-calidad/CLASE.md):**
- El resultado con `k = 4` es: 47 aciertos, 2 falsos positivos y 1 falso negativo (el duplicado artefacto): precisión `0,959`, exhaustividad `0,979`, y se retiene `0,994` de los registros limpios.
- Un lote sintético de 400 registros de la variable VS-S (la de C02) lleva 48 errores sembrados, 8 de cada tipo: magnitud con el decimal desplazado, desplazada 0,8 a 2,5 mag, duplicado exacto, fecha futura, campo ausente y filtro no válido.
- 🎯 **Por qué importa:** Un lote de contribuciones trae errores de tecleo, duplicados, fechas imposibles y mediciones erróneas. La decisión central: ¿qué filtro aplicar para atrapar los errores sin tirar datos buenos, y cómo se sabe que funciona?

📘 **Dónde se aprende** (2 clases): [B20-C01 · Búsqueda bibliográfica sistemática y gestión de referencias](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md); [B129-C04 · Contribución de medidas voluntarias con control de calidad](../programa/clases/B129/B129-C04-contribucion-de-medidas-voluntarias-con-control-de-calidad/CLASE.md).

### Duplicado exacto

- Un duplicado exacto es una fila repetida en todas sus columnas, incluido su identificador.

🎯 **Por qué importa (clase B14-C08):** Una bitácora de observación real tiene errores: alguien escribió `-99` donde faltaba un dato, el mismo objeto aparece con tres grafías, una fila se copió dos veces, un valor tiene un dígito de más. Si calculas una media sin limpiar, el resultado es otro número.

📘 **Dónde se aprende** (1 clase): [B14-C08 · Pandas y limpieza de datos](../programa/clases/B14/B14-C08-pandas-y-limpieza-de-datos/CLASE.md).

### Duración

- La duración es el tiempo del tránsito.
- La duración `T₁₄` va del primer al último contacto.

💡 **Cómo se explica en la clase [B29-C01](../programa/clases/B29/B29-C01-transitos-planetarios/CLASE.md):**
- El radio se infiere de la profundidad, pero hay que corregir por oscurecimiento al limbo y por el parámetro de impacto; la duración, a su vez, depende de `a`, `b` y `k`.
- *Descripción textual:* los radios dan la profundidad; el periodo y la masa estelar dan el semieje, y con el parámetro de impacto la duración, que se verifica con una búsqueda numérica; el oscurecimiento al limbo modifica la profundidad central.
- 🎯 **Por qué importa:** El tránsito es el método con más planetas descubiertos. Su profundidad da el radio del planeta y su duración informa del semieje y el parámetro de impacto.

📘 **Dónde se aprende** (2 clases): [B29-C01 · Tránsitos planetarios](../programa/clases/B29/B29-C01-transitos-planetarios/CLASE.md); [B131-C06 · Aprendizaje basado en problemas con datos astronómicos](../programa/clases/B131/B131-C06-aprendizaje-basado-en-problemas-con-datos-astronomicos/CLASE.md).

### Duración cenital

- La duración cenital `2λ_max/n` es la máxima.

💡 **Cómo se explica en la clase [B89-C14](../programa/clases/B89/B89-C14-estaciones-terrestres/CLASE.md):**
- *Descripción textual:* la altura y la máscara dan el semiángulo central y la duración cenital; la simulación de un día da las pasadas reales; con la tasa se obtiene el volumen de datos.
- ⚠️ **Error frecuente:** Usar la duración cenital como típica. Se corrige con 8.4.
- 🎯 **Por qué importa:** El tiempo de contacto es el recurso más escaso de un satélite de órbita baja: define cuántos datos bajan por día y cuántas estaciones se necesitan. La decisión central: ¿cuánto contacto y cuántos datos da una estación a un satélite de órbita baja?

📘 **Dónde se aprende** (1 clase): [B89-C14 · Estaciones terrestres](../programa/clases/B89/B89-C14-estaciones-terrestres/CLASE.md).

### Duración del vuelo

- La duración del vuelo es el tiempo total de una misión; el período orbital es el de una sola vuelta.

💡 **Cómo se explica en la clase [B02-C19](../programa/clases/B02/B02-C19-historia-de-la-exploracion-espacial/CLASE.md):**
- Cuidado: los 108 minutos son la duración del vuelo (ascenso, una vuelta, descenso), no el período orbital; por eso no sirven para el cálculo de la tercera ley.
- ⚠️ **Error frecuente:** Usar la duración del vuelo como período. Ejercicio 6.
- 🎯 **Por qué importa:** La exploración espacial es una historia científica y también política. La pregunta motivadora es: ¿qué cambió, para la astronomía y para la sociedad, cuando los instrumentos y las personas empezaron a salir de la atmósfera, y qué reglas se acordaron?

📘 **Dónde se aprende** (1 clase): [B02-C19 · Historia de la exploración espacial](../programa/clases/B02/B02-C19-historia-de-la-exploracion-espacial/CLASE.md).

### Duración mínima

- La duración mínima `T = V/(C_s Q)` supone caudal de banca llena continuo.

💡 **Cómo se explica en la clase [B66-C04](../programa/clases/B66/B66-C04-redes-fluviales-fosiles-y-paleohidrologia-marciana/CLASE.md):**
- *Descripción textual:* el terreno se rellena, se calculan direcciones y acumulación, se definen canales con un umbral y del área mayor sale el caudal y la duración mínima.
- 🎯 **Por qué importa:** Un mapa de valles marcianos invita a decir «hubo un océano» o «hubo lluvia». La decisión central: ¿qué se puede inferir del caudal y de la duración con una red, un volumen y supuestos explícitos, y qué incertidumbre arrastra?

📘 **Dónde se aprende** (1 clase): [B66-C04 · Redes fluviales fósiles y paleohidrología marciana](../programa/clases/B66/B66-C04-redes-fluviales-fosiles-y-paleohidrologia-marciana/CLASE.md).

### Duración nominal

- Reintento: repetición de un paso fallido. Duración nominal: suma sin fallos.

💡 **Cómo se explica en la clase [B96-C14](../programa/clases/B96/B96-C14-procedimientos-de-recuperacion/CLASE.md):**
- Duración nominal `= 30 + 25 + 60 + 40 + 35 + 30 = 220 s`.
- 🎯 **Por qué importa:** Una recuperación que no cabe en la pasada o que falla en un paso sin reintento deja a la nave a medias hasta el siguiente contacto. La decisión central: ¿cabe el procedimiento en la ventana y qué probabilidad tiene de completarse con reintentos?

📘 **Dónde se aprende** (1 clase): [B96-C14 · Procedimientos de recuperación](../programa/clases/B96/B96-C14-procedimientos-de-recuperacion/CLASE.md).

### Duración singular

- Una duración singular es un `T` en que `det Φ_rv` es casi nulo.

🎯 **Por qué importa (clase B76-C12):** El mismo algoritmo sirve para cientos de maniobras, pero falla en tiempos singulares. La decisión central: ¿cómo se calculan los impulsos y para qué duraciones el problema está mal condicionado?

📘 **Dónde se aprende** (1 clase): [B76-C12 · Guiado relativo](../programa/clases/B76/B76-C12-guiado-relativo/CLASE.md).
