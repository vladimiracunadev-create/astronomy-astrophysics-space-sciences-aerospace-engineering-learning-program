# Términos · N

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · **N** · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

### Nadir

- El horizonte local es el círculo máximo que separa la mitad visible de la oculta; el cenit es el punto sobre tu cabeza y el nadir su opuesto.
- El nadir `n` es la dirección al centro terrestre.

💡 **Cómo se explica en la clase [B08-C02](../programa/clases/B08/B08-C02-esfera-celeste-y-horizonte-local/CLASE.md):**
- Nombrar y ubicar cenit, nadir, horizonte, meridiano, polo y ecuador celestes.
- 🎯 **Por qué importa:** Alguien en Punta Arenas ve girar algunas estrellas sin ponerse jamás; alguien en el valle del Elqui las ve rozar el horizonte, y alguien en el hemisferio norte no las ve nunca. Entender por qué evita comprar un telescopio para un objeto que no sale en tu cielo.
- 🔗 **Se estudia junto con:** esfera celeste, horizonte local, cenit, meridiano local.

📘 **Dónde se aprende** (2 clases): [B08-C02 · Esfera celeste y horizonte local](../programa/clases/B08/B08-C02-esfera-celeste-y-horizonte-local/CLASE.md); [B87-C04 · Sensores terrestres](../programa/clases/B87/B87-C04-sensores-terrestres/CLASE.md).

### Nanofulguración

- Una nanofulguración es un evento pequeño.

💡 **Cómo se explica en la clase [B34-C01](../programa/clases/B34/B34-C01-calentamiento-coronal-mecanismos-y-evidencias/CLASE.md):**
- Ejercicio 9 · transferencia. Transferencia. Un compañero afirma que las nanofulguraciones calientan la corona.
- 🎯 **Por qué importa:** Elegir un mecanismo de calentamiento exige saber cuánta energía hay que reponer y de dónde sale. La decisión central: ¿cuánta energía pierde un bucle y qué eventos pueden reponerla?
- 🔗 **Se estudia junto con:** calentamiento coronal, flujo conductivo, pérdida radiativa, ley de potencias.

📘 **Dónde se aprende** (1 clase): [B34-C01 · Calentamiento coronal: mecanismos y evidencias](../programa/clases/B34/B34-C01-calentamiento-coronal-mecanismos-y-evidencias/CLASE.md).

### Natural

- El logaritmo decimal usa `b = 10`; el natural, `ln`, usa `b = e`.

💡 **Cómo se explica en la clase [B04-C05](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md):**
- El logaritmo decimal del flujo (`log f`) es más natural en gráficos científicos modernos.
- 🎯 **Por qué importa:** El ojo y los instrumentos comparan brillos que difieren en factores de un millón. Los astrónomos lo resuelven con una escala logarítmica: la magnitud.
- 🔗 **Se estudia junto con:** función exponencial, número de Euler, logaritmo en base b, logaritmo decimal.

📘 **Dónde se aprende** (1 clase): [B04-C05 · Funciones exponenciales y logarítmicas](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md).

### Navaja de Occam

- La navaja de Occam emerge sola: un modelo con prior amplio reparte su probabilidad en muchos datos posibles y recibe menos evidencia por el que ocurrió.

💡 **Contexto en la clase [B12-C22](../programa/clases/B12/B12-C22-comparacion-de-modelos-evidencia-bayesiana-y-criterios-de-informacion/CLASE.md):**
- **Idea central (modelo mental):** Cada modelo se evalúa por dos cosas: qué tan bien ajusta (verosimilitud máxima) y cuánto «cuesta» su flexibilidad. AIC y BIC ponen un precio fijo por parámetro; la evidencia pone un precio que depende del prior, calculado automáticamente al promediar.
- 🎯 **Por qué importa:** Un modelo más flexible siempre ajusta mejor los datos que uno más sencillo, así que el ajuste solo no sirve para elegir. Hace falta penalizar la complejidad: ¿vale la pena el parámetro extra?
- 🔗 **Se estudia junto con:** evidencia, factor de Bayes, criterio de información de Akaike, bayesiano.

📘 **Dónde se aprende** (1 clase): [B12-C22 · Comparación de modelos: evidencia bayesiana y criterios de información](../programa/clases/B12/B12-C22-comparacion-de-modelos-evidencia-bayesiana-y-criterios-de-informacion/CLASE.md).

### Navegación inercial

- La navegación inercial integra `v̇ = f + g(r)` y `ṙ = v`.

💡 **Cómo se explica en la clase [B80-C01](../programa/clases/B80/B80-C01-principios-de-navegacion-inercial-espacial/CLASE.md):**
- Límite: la navegación inercial real corrige el rumbo con modelos y filtros; aquí se estudia solo la acumulación libre del error.
- Ejercicio 11 · transferencia. Transferencia. Un lanzador necesita error inferior a `200 m` y su navegación inercial tiene `b = 1,0 × 10⁻³ m/s²`.
- 🎯 **Por qué importa:** Una sonda que sale de la cobertura de seguimiento, un lanzador en ascenso o un módulo de aterrizaje en su descenso necesitan saber dónde están sin ayuda externa. B87 trata el giroscopio como sensor de actitud y B74 estima la órbita con observaciones externas; ninguna clase actual enseña cómo se propaga una solución desde una IMU.
- 🔗 **Se estudia junto con:** fuerza específica, sesgo, frecuencia de Schuler, Deriva.

📖 **Explicado a fondo:** [Navegación inercial](esencial/ampliacion-n-z.md#navegación-inercial) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B80-C01 · Principios de navegación inercial espacial](../programa/clases/B80/B80-C01-principios-de-navegacion-inercial-espacial/CLASE.md).

### Navegación óptica

- La navegación óptica triangula esas líneas.

💡 **Cómo se explica en la clase [B74-C13](../programa/clases/B74/B74-C13-navegacion-optica/CLASE.md):**
- python programa/clases/B74/B74-C13-navegacion-optica/laboratorio.py
- 🎯 **Por qué importa:** Una dirección conocida con un microrradián son cientos de kilómetros a la distancia de un planeta. La decisión central: ¿cuánta incertidumbre de posición produce una cierta incertidumbre angular y cómo depende de la geometría de las balizas?
- 🔗 **Se estudia junto con:** línea de visión, matriz de información, geometría, baliza.

📘 **Dónde se aprende** (1 clase): [B74-C13 · Navegación óptica](../programa/clases/B74/B74-C13-navegacion-optica/CLASE.md).

### Navegación sin instrumentos

- La navegación sin instrumentos (*wayfinding*) usa la observación del cielo, las olas, el viento y los seres vivos para encontrar el rumbo y la posición (S1).

💡 **Cómo se explica en la clase [B02-C07](../programa/clases/B02/B02-C07-observaciones-de-polinesia-y-navegacion-oceanica/CLASE.md):**
- La navegación con instrumentos (brújula, GPS) da precisión pero depende de aparatos.
- La navegación sin instrumentos depende de la memoria y la práctica, y es resistente a fallas técnicas, pero exige formación larga y transmisión.
- 🎯 **Por qué importa:** Se discutió durante décadas si los pueblos del Pacífico llegaron a las islas por azar o por navegación deliberada. La pregunta motivadora es: ¿cómo se orienta quien no puede ver tierra, y qué dice su método sobre el valor del conocimiento oral?
- 🔗 **Se estudia junto con:** compás estelar, azimut, declinación, horizonte.

📘 **Dónde se aprende** (1 clase): [B02-C07 · Observaciones de Polinesia y navegación oceánica](../programa/clases/B02/B02-C07-observaciones-de-polinesia-y-navegacion-oceanica/CLASE.md).

### NCC

- La NCC mide la similitud de dos ventanas sin sensibilidad a brillo y contraste.

💡 **Cómo se explica en la clase [B74-C26](../programa/clases/B74/B74-C26-navegacion-por-hitos-y-correlacion-de-terreno/CLASE.md):**
- Para cada desplazamiento de `±12 px` se calcula la NCC de la plantilla de 32 × 32 px con la ventana de la imagen; el máximo se refina con una parábola en cada eje.
- PL["plantilla"] --> NCC["NCC en la ventana"]
- 🎯 **Por qué importa:** Un buen pico de correlación no garantiza un buen emparejamiento: en un terreno repetitivo hay dos picos casi iguales. La decisión central: ¿cuánta precisión da la correlación en un terreno rico, y cuándo el emparejamiento es ambiguo y no debe usarse?
- 🔗 **Se estudia junto con:** plantilla, ventana de búsqueda, refinamiento subpíxel, razón pico/segundo pico.

📘 **Dónde se aprende** (1 clase): [B74-C26 · Navegación por hitos y correlación de terreno](../programa/clases/B74/B74-C26-navegacion-por-hitos-y-correlacion-de-terreno/CLASE.md).

### NCPA

- Las NCPA: aberraciones fuera del camino común.

💡 **Cómo se explica en la clase [B42-C23](../programa/clases/B42/B42-C23-calibracion-de-la-matriz-de-interaccion-y-aberraciones-no-comunes/CLASE.md):**
- La NCPA tiene `0,1526 rad` rms (desenfoque `0,12`, astigmatismos `0,08` y `−0,05`); el Strehl sin corregir es `0,97732` (Maréchal `0,97697`).
- La NCPA de este tamaño cuesta 2,3 % de Strehl y no la ve el sensor: se mide en la imagen.
- ⚠️ **Error frecuente:** Confundir NCPA con aberración atmosférica. Ver sección 7.
- 🎯 **Por qué importa:** Una matriz mal calibrada degrada el lazo y las aberraciones del camino de ciencia no las ve el sensor. La decisión central: ¿con qué amplitud calibrar y cómo corregir lo que el sensor no ve?
- 🔗 **Se estudia junto con:** matriz de interacción, empuje-tirón, matriz de control, valores singulares.

📘 **Dónde se aprende** (1 clase): [B42-C23 · Calibración de la matriz de interacción y aberraciones no comunes](../programa/clases/B42/B42-C23-calibracion-de-la-matriz-de-interaccion-y-aberraciones-no-comunes/CLASE.md).

### NDVI

- El NDVI (*índice de vegetación de diferencia normalizada*) es `(NIR − rojo)/(NIR + rojo)`.
- El NDVI es `(NIR − rojo)/(NIR + rojo)` y va de −1 a +1.

💡 **Cómo se explica en la clase [B15-C22](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md):**
- Con las medias ficticias, el NDVI es `−0,20` (agua), `+0,84` (vegetación) y `+0,17` (suelo).
- El NDVI condensa dos bandas en una; no sustituye al clasificador, pero ilustra por qué las bandas separan clases.
- 🎯 **Por qué importa:** Un mapa de cobertura de suelo parece una verdad; en realidad es una predicción con un error que depende de las muestras elegidas y de cuánto se solapan las clases en el espacio espectral. Cifras como «90 % de exactitud» no significan nada sin decir con qué datos se midieron, ni cómo se reparte el error entre clases.
- 🔗 **Se estudia junto con:** vector espectral, clase, muestras de entrenamiento, muestras de prueba.

📘 **Dónde se aprende** (2 clases): [B15-C22 · Clasificación supervisada de imágenes](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md); [B57-C06 · Índices de vegetación](../programa/clases/B57/B57-C06-indices-de-vegetacion/CLASE.md).

### Nebulosa planetaria

- La nebulosa planetaria es la envoltura expulsada por una estrella de masa baja o media.
- Una nebulosa planetaria es la envoltura expulsada al final de la fase AGB.

💡 **Cómo se explica en la clase [B24-C21](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md):**
- La pérdida de masa en la AGB acaba expulsando la envoltura (nebulosa planetaria) y deja la enana blanca de C18.
- Los diagramas de Gaia incluyen estrellas post-AGB y nebulosas planetarias en el HR (S2, resumen), y los modelos de MESA muestran pulsos térmicos de la fase AGB (S3, resumen).
- 🎯 **Por qué importa:** Las estrellas AGB son una fuente importante de carbono, nitrógeno y elementos pesados del medio interestelar, y sus abundancias superficiales son el registro observable de lo que ocurre en su interior.
- 🔗 **Se estudia junto con:** rama asintótica de gigantes (AGB), pulso térmico, dragado, proceso s.

📘 **Dónde se aprende** (2 clases): [B24-C18 · Etapas finales de evolución](../programa/clases/B24/B24-C18-etapas-finales-de-evolucion/CLASE.md); [B24-C21 · Rama asintótica de gigantes: pulsos térmicos y proceso s](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md).

### Necesidad de misión

- Una necesidad de misión es la carencia que justifica el proyecto, expresada sin elegir la solución.

💡 **Cómo se explica en la clase [B83-C01](../programa/clases/B83/B83-C01-necesidad-de-mision-y-caso-cientifico/CLASE.md):**
- Distinguir una necesidad de misión de una solución técnica.
- La evidencia es la ficha de necesidad de misión con requisito de medición derivado del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Un equipo sabe que quiere «mirar la costa» pero no cuánto debe resolver ni qué objetivo merece el presupuesto. La decisión central: ¿qué requisito de medición se deduce de la pregunta científica y qué objetivo conviene perseguir primero?
- 🔗 **Se estudia junto con:** caso científico, requisito de medición, GSD, criterio de muestreo.

📘 **Dónde se aprende** (1 clase): [B83-C01 · Necesidad de misión y caso científico](../programa/clases/B83/B83-C01-necesidad-de-mision-y-caso-cientifico/CLASE.md).

### NEdL

- El NEdL es el ruido en radiancia equivalente al NEdT.

💡 **Cómo se explica en la clase [B57-C16](../programa/clases/B57/B57-C16-incendios-forestales/CLASE.md):**
- N["ruido NEdL"] --> P["p minima detectable"]
- 🎯 **Por qué importa:** Un incendio pequeño puede ser un desastre en horas, pero un píxel mide cientos de metros. La decisión central: ¿cuál es la fracción de píxel más pequeña que se puede detectar y cuánto sesga la estimación un error en el fondo?
- 🔗 **Se estudia junto con:** detección activa de fuego, fracción de píxel, banda de infrarrojo medio, infrarrojo térmico.

📘 **Dónde se aprende** (1 clase): [B57-C16 · Incendios forestales](../programa/clases/B57/B57-C16-incendios-forestales/CLASE.md).

### NEES

- El NEES (*normalized estimation error squared*) es `eᵀ P⁻¹ e`, con `e` el error real; si el filtro es coherente, su media es la dimensión del estado.
- El NEES es `eᵀ P⁻¹ e` y vale en promedio la dimensión del estado si el filtro es consistente.
- El NEES es `eᵀP⁻¹e` con `e = x̂ − x` (ν = dimensión del estado).
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C17](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md):**
- El NEES medio es `2,066`, cerca del valor ideal 2: el filtro es coherente (su incertidumbre declarada coincide con su error real).
- Si se declara `Q` 10 000 veces menor que la real (se cree que el objeto no acelera), el filtro confía demasiado en su modelo: el RMSE sube a `17,1 m` y el NEES a `5019`, muy por encima de 2.
- ⚠️ **Error frecuente:** No comprobar la coherencia (NEES). Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Un radar mide la distancia a un objeto cada segundo, con 5 m de ruido. Si solo usas la última medida, tu error es de 5 m.
- 🔗 **Se estudia junto con:** estado, matriz de transición, matriz de medida, covarianza del ruido de proceso.

📘 **Dónde se aprende** (5 clases): [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md); [B74-C09 · Filtro de Kalman extendido](../programa/clases/B74/B74-C09-filtro-de-kalman-extendido/CLASE.md); [B74-C23 · Consistencia de filtros: innovaciones y pruebas NEES/NIS](../programa/clases/B74/B74-C23-consistencia-de-filtros-innovaciones-y-pruebas-nees-nis/CLASE.md); [B80-C08 · Filtrado distribuido y descentralizado](../programa/clases/B80/B80-C08-filtrado-distribuido-y-descentralizado/CLASE.md); [B87-C10 · Filtro de actitud](../programa/clases/B87/B87-C10-filtro-de-actitud/CLASE.md).

### Negativa

- La entalpía de reacción `Δ_rH` es el cambio de entalpía por mol de reacción tal como está escrita; es negativa si la reacción libera energía (exotérmica) y positiva si la absorbe (endotérmica).
- Correlación positiva significa que tienden a subir juntas; negativa, que cuando una sube la otra baja.

💡 **Contexto en la clase [B06-C12](../programa/clases/B06/B06-C12-termoquimica-y-energia-de-reaccion/CLASE.md):**
- **Idea central (modelo mental):** Piensa en un valle: los reactivos están en una altura y los productos en otra. Lo que importa para la energía liberada es el desnivel, no el camino. Los elementos puros son el «nivel del mar»; cada compuesto tiene una altura medida desde ahí (su entalpía de formación).
- 🎯 **Por qué importa:** Cualquier combustible, de una hoguera a un cohete, libera energía porque los productos están en un estado más estable que los reactivos. ¿Cuánta energía por kilogramo?
- 🔗 **Se estudia junto con:** entalpía, entalpía de reacción, positiva, entalpía de formación estándar.

📘 **Dónde se aprende** (2 clases): [B06-C12 · Termoquímica y energía de reacción](../programa/clases/B06/B06-C12-termoquimica-y-energia-de-reaccion/CLASE.md); [B12-C05 · Covarianza y correlación](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md).

### Negativo correcto

- Un acierto (`a`), una falsa alarma (`b`), un fallo (`c`) y un negativo correcto (`d`) forman la tabla.

💡 **Cómo se explica en la clase [B30-C20](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md):**
- pares de dias: 364 ; aciertos a = 12, falsas alarmas b = 24, fallos c = 6, negativos correctos d = 322
- 🎯 **Por qué importa:** Una alerta con muchas falsas alarmas se ignora y una con muchos fallos no sirve; medir ambas cosas es parte del oficio. La decisión central: ¿cómo se clasifica un evento y cómo se mide si una regla de alerta tiene habilidad?
- 🔗 **Se estudia junto con:** escala, acierto, falsa alarma, fallo.

📘 **Dónde se aprende** (1 clase): [B30-C20 · Análisis de alerta solar real](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md).

### Negativo (VPN)

- El valor predictivo positivo (VPP) es la fracción de positivos que son verdaderos; el negativo (VPN), la de negativos que son verdaderos.

💡 **Cómo se explica en la clase [B116-C06](../programa/clases/B116/B116-C06-dispositivos-biomedicos-portatiles-ultrasonido-diagnostico/CLASE.md):**
- Calcular el valor predictivo positivo y negativo con el teorema de Bayes y ver el efecto de la prevalencia.
- 🎯 **Por qué importa:** Un equipo no es solo su ficha técnica: lo que ve depende de la frecuencia elegida, quién lo maneja, cuánto entrena y qué retardo tiene el apoyo experto. Y una prueba con buenos números de sensibilidad y especificidad puede dar mayoría de falsos positivos si la condición es rara.
- 🔗 **Se estudia junto con:** ultrasonido, tiempo de ida y vuelta, resolución axial, atenuación.

📘 **Dónde se aprende** (1 clase): [B116-C06 · Dispositivos biomédicos portátiles (ultrasonido, diagnóstico)](../programa/clases/B116/B116-C06-dispositivos-biomedicos-portatiles-ultrasonido-diagnostico/CLASE.md).

### Neumann

- Las condiciones pueden ser de Dirichlet (valor de la función), Neumann (valor de la derivada) o mixtas.

💡 **Contexto en la clase [B11-C12](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md):**
- **Idea central (modelo mental):** El problema de valor inicial es disparar y mirar dónde cae. El de frontera es acertar a un blanco fijo: se dispara, se mide la desviación y se corrige el ángulo. El método de diferencias finitas es distinto: se pide a todos los puntos de la malla que se acomoden a la vez entre las dos paredes.
- 🎯 **Por qué importa:** En ingeniería espacial las condiciones suelen estar en dos extremos: una aleta térmica con temperaturas conocidas en la raíz y en la punta; una transferencia que debe partir de un punto y llegar a otro en un tiempo dado.
- 🔗 **Se estudia junto con:** problema de frontera, Dirichlet, mixtas, malla.

📘 **Dónde se aprende** (1 clase): [B11-C12 · Problemas de frontera](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md).

### Neurovascular

- Tiene una fase de pródromo (náuseas, vómitos, anorexia), y subsíndromes hematopoyético (HSS), gastrointestinal (GIS) y neurovascular o del sistema nervioso central (SNC).

💡 **Cómo se explica en la clase [B112-C03](../programa/clases/B112/B112-C03-efectos-agudos-de-la-radiacion/CLASE.md):**
- Seed (NASA THREE, 2011) describe: el síndrome hematopoyético es el más frecuente y aparece en el intervalo de 0,5 a 8 Gy, tarda semanas en expresarse y, sin tratamiento, a dosis altas puede causar la muerte en 15–60 días; el gastrointestinal exige 4–15 Gy y aparece en días; el neurovascular o del SNC solo tras más de 20–30 Gy, en horas.
- 🎯 **Por qué importa:** Ninguna clase cubre síndromes agudos y umbrales. Un evento solar grande es el único escenario de la exploración que podría producir efectos agudos, y por eso los límites de corto plazo y el blindaje de refugio se diseñan a su medida.
- 🔗 **Se estudia junto con:** síndrome de radiación aguda, pródromo, hematopoyético, gastrointestinal.

📘 **Dónde se aprende** (1 clase): [B112-C03 · Efectos agudos de la radiación](../programa/clases/B112/B112-C03-efectos-agudos-de-la-radiacion/CLASE.md).

### Neutra

- Una disolución es neutra si `[H⁺] = [OH⁻]`, es decir, pH 7 a 25 °C.

💡 **Contexto en la clase [B06-C15](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md):**
- **Idea central (modelo mental):** Un ácido es quien presta un protón y una base, quien lo recibe. El préstamo no es todo o nada: en un ácido fuerte casi todos los protones se prestan; en uno débil, sólo una fracción, y el equilibrio fija cuántos.
- 🎯 **Por qué importa:** El extracto en agua caliente de las muestras de Bennu contiene amoníaco libre en unos 13,6 μmol por gramo y ácido fórmico en 4,106 μmol por gramo (S1). Un ácido y una base en el mismo líquido reaccionan entre sí: el ácido cede un protón, la base lo acepta y se forman iones.
- 🔗 **Se estudia junto con:** disolución, soluto, disolvente, concentración.

📘 **Dónde se aprende** (1 clase): [B06-C15 · Ácidos, bases y soluciones](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md).

### Neutrino

- Un neutrino (`ν`) es una partícula neutra que casi no interacciona y escapa de la estrella.
- El neutrino es una partícula neutra y muy ligera.

💡 **Cómo se explica en la clase [B24-C06](../programa/clases/B24/B24-C06-fusion-de-hidrogeno/CLASE.md):**
- Una pequeña parte de `Q` se la llevan los neutrinos y no calienta la estrella; la fracción exacta depende de la reacción y no se calcula aquí.
- Que los neutrinos *pp*, ⁷Be y *pep* se hayan medido con precisión (S3, resumen) confirma que la fusión ocurre hoy en el núcleo.
- 🎯 **Por qué importa:** Una estrella como el Sol brilla desde hace miles de millones de años; ninguna fuente química ni gravitatoria alcanza (C02). La fusión nuclear sí.
- 🔗 **Se estudia junto con:** fusión nuclear, defecto de masa, protón, partícula alfa.

📖 **Explicado a fondo:** [Neutrino](esencial/tercera-f-t.md#neutrino) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B24-C06 · Fusión de hidrógeno](../programa/clases/B24/B24-C06-fusion-de-hidrogeno/CLASE.md); [B27-C18 · Neutrinos de supernova](../programa/clases/B27/B27-C18-neutrinos-de-supernova/CLASE.md).

### Neutrinos

- Los neutrinos aportan `Ω_ν = Ω_γ × 0,2271 N_eff`, con `0,2271 = (7/8)(4/11)^{4/3}`.
- Los neutrinos se llevan la mayor parte.

💡 **Cómo se explica en la clase [B26-C14](../programa/clases/B26/B26-C14-evolucion-termica-del-universo/CLASE.md):**
- Con los neutrinos (`N_eff = 2,99`, S3, resumen), `Ω_r = Ω_γ(1 + 0,2271 × 2,99) = 9,14 × 10⁻⁵`.
- Códigos de Boltzmann: incluyen la masa de los neutrinos.
- ⚠️ **Error frecuente:** Olvidar los neutrinos. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** Casi todo lo observable del universo temprano (radiación de fondo, abundancia de helio) depende de su temperatura y de qué componente dominaba la densidad en cada época.
- 🔗 **Se estudia junto con:** radiación de fondo, constante de radiación, densidad de energía de los fotones, parámetro de densidad de fotones.

📘 **Dónde se aprende** (2 clases): [B26-C14 · Evolución térmica del universo](../programa/clases/B26/B26-C14-evolucion-termica-del-universo/CLASE.md); [B27-C15 · Supernovas de colapso](../programa/clases/B27/B27-C15-supernovas-de-colapso/CLASE.md).

### Neutrones

- Tiene un núcleo, minúsculo y denso, formado por protones (carga positiva) y neutrones (sin carga), y a su alrededor electrones (carga negativa).

💡 **Cómo se explica en la clase [B06-C01](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md):**
- Describir el átomo como núcleo (protones y neutrones) y electrones, y distinguir número atómico de número másico.
- 🎯 **Por qué importa:** Casi todo lo que sabemos de la composición de una estrella o de una nebulosa lo sabemos porque sus átomos emiten o absorben luz en colores muy precisos. Una línea roja a 656 nm no es «un color cualquiera»: es la firma del hidrógeno.
- 🔗 **Se estudia junto con:** átomo, núcleo, protones, electrones.

📘 **Dónde se aprende** (1 clase): [B06-C01 · Estructura atómica](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md).

### Neutro–neutro

- Una reacción neutro–neutro suele tener barrera `γ`.

💡 **Cómo se explica en la clase [B55-C03](../programa/clases/B55/B55-C03-reacciones-en-medio-interestelar/CLASE.md):**
- Las reacciones ion–molécula son rápidas incluso en el frío; las neutro–neutro con barrera necesitan calor.
- Dos reacciones ilustrativas: una ion–molécula con `α = 10⁻⁹ cm³ s⁻¹` y sin barrera, y una neutro–neutro con `α = 10⁻¹⁰` y barrera `γ = 1500 K`.
- 🎯 **Por qué importa:** En el espacio la densidad es tan baja que una reacción puede tardar siglos o millones de años, y la temperatura de 10 K cierra casi todas las reacciones con barrera. Saber cuáles ocurren define qué moléculas pueden existir.
- 🔗 **Se estudia junto con:** parametrización de Arrhenius modificada, ion–molécula, escala de tiempo, reacción de pseudo-primer orden.

📘 **Dónde se aprende** (1 clase): [B55-C03 · Reacciones en medio interestelar](../programa/clases/B55/B55-C03-reacciones-en-medio-interestelar/CLASE.md).

### Newton

- El residuo es `f(E)` evaluado en la solución. Newton usa la derivada `1 − e cos E`.
- Las derivadas son `T'`, `T''` y `T'''`. Newton: `x ← x − δ/T'`.
- Trapezoidal: `y_{n+1} = y_n + (h/2)[f(t_n, y_n) + f(t_{n+1}, y_{n+1})]`. Newton resuelve `g(z) = 0` con `z ← z − g(z)/g′(z)`; aquí `g′` incluye el jacobiano `df/dy`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C22](../programa/clases/B11/B11-C22-metodos-implicitos-y-sistemas-rigidos/CLASE.md):**
- El jacobiano es `1 − h ∂f/∂y = 1 + 3 k h z²`, que es muy grande: Newton converge en unas 4 iteraciones por paso (valor medio medido) partiendo de la predicción del paso anterior.
- B --> C["Newton: z ← z − g(z)/g′(z)<br/>con g′ = 1 − h·∂f/∂y"]
- ⚠️ **Error frecuente:** Olvidar el jacobiano o dejar de verificar la convergencia de Newton. Se corrige con los ejercicios 7 y 8.
- 🎯 **Por qué importa:** Los modelos térmicos, de combustión, de propulsión y de química atmosférica mezclan escalas de microsegundos con horas. Un integrador explícito pagaría el paso del más rápido durante toda la simulación.
- 🔗 **Se estudia junto con:** implícito, Euler implícito, BDF2, Trapezoidal.

📘 **Dónde se aprende** (4 clases): [B11-C22 · Métodos implícitos y sistemas rígidos](../programa/clases/B11/B11-C22-metodos-implicitos-y-sistemas-rigidos/CLASE.md); [B71-C14 · Ecuación de Kepler](../programa/clases/B71/B71-C14-ecuacion-de-kepler/CLASE.md); [B82-C06 · Algoritmos iterativos para Lambert (Gooding, Izzo)](../programa/clases/B82/B82-C06-algoritmos-iterativos-para-lambert-gooding-izzo/CLASE.md); [B85-C18 · Modelado térmico por nodos](../programa/clases/B85/B85-C18-modelado-termico-por-nodos/CLASE.md).

### NIEL

- El NIEL es la energía no ionizante depositada por unidad de longitud.

💡 **Contexto en la clase [B85-C24](../programa/clases/B85/B85-C24-efectos-de-la-radiacion-ionizante-en-materiales-y-electronica/CLASE.md):**
- 🎯 **Por qué importa:** Una celda solar o un polímero no fallan de golpe: pierden prestaciones con la exposición. La decisión central: ¿cuánta potencia queda al final de la misión y cuánto cambia con un blindaje que reduce la fluencia?
- 🔗 **Se estudia junto con:** ley de degradación, dosis total ionizante, umbrales, inversa.

📘 **Dónde se aprende** (1 clase): [B85-C24 · Efectos de la radiación ionizante en materiales y electrónica](../programa/clases/B85/B85-C24-efectos-de-la-radiacion-ionizante-en-materiales-y-electronica/CLASE.md).

### Nilpotente

- Un operador nilpotente cumple `Tᵏ = 0` para algún `k`.

💡 **Cómo se explica en la clase [B10-C03](../programa/clases/B10/B10-C03-matrices-y-operadores-lineales/CLASE.md):**
- Derivar cuatro veces da cero: `D⁴ = 0` (nilpotente).
- 🎯 **Por qué importa:** Una estación terrestre está fija respecto de la Tierra, pero la Tierra gira respecto del espacio inercial. Para saber dónde está la estación en el sistema inercial a cada instante hay que aplicar una transformación que depende del tiempo.
- 🔗 **Se estudia junto con:** operador lineal, matriz, matriz de T en una base, producto matricial.

📘 **Dónde se aprende** (1 clase): [B10-C03 · Matrices y operadores lineales](../programa/clases/B10/B10-C03-matrices-y-operadores-lineales/CLASE.md).

### NIS

- El NIS es `νᵀS⁻¹ν` con `ν` la innovación y `S` su covarianza (ν = dimensión de la medida).

💡 **Cómo se explica en la clase [B74-C23](../programa/clases/B74/B74-C23-consistencia-de-filtros-innovaciones-y-pruebas-nees-nis/CLASE.md):**
- Con `N = 100`, `n = 2` los límites del 95 % son `[1,627, 2,411]` (esperado 2), y para el NIS con 1 grado de libertad, `[0,742, 1,296]` (esperado 1).
- Con el `q` verdadero, el NEES medio es `1,997` y el NIS `0,989`; el `0,94` y el `0,94` de los pasos caen dentro de los límites, como se espera para una prueba al 95 % con pasos correlacionados.
- ⚠️ **Error frecuente:** Dar por bueno un filtro por el rms. Aplica NEES/NIS; ver 8.2.
- 🎯 **Por qué importa:** Un filtro optimista presenta covarianzas pequeñas y errores grandes, y no avisa. La decisión central: ¿cómo sé, con una prueba estadística, si mi filtro es consistente y qué estadístico me avisa de qué fallo?
- 🔗 **Se estudia junto con:** NEES, consistente, Optimista, conservador.

📘 **Dónde se aprende** (1 clase): [B74-C23 · Consistencia de filtros: innovaciones y pruebas NEES/NIS](../programa/clases/B74/B74-C23-consistencia-de-filtros-innovaciones-y-pruebas-nees-nis/CLASE.md).

### Nitidez

- La nitidez: maximizar el pico de la PSF.

💡 **Cómo se explica en la clase [B42-C23](../programa/clases/B42/B42-C23-calibracion-de-la-matriz-de-interaccion-y-aberraciones-no-comunes/CLASE.md):**
- La nitidez recupera `(−0,12000; −0,08000; +0,05000)` y el Strehl `1,000000`.
- N["NCPA invisible"] --> S["nitidez: secciones áureas"]
- 🎯 **Por qué importa:** Una matriz mal calibrada degrada el lazo y las aberraciones del camino de ciencia no las ve el sensor. La decisión central: ¿con qué amplitud calibrar y cómo corregir lo que el sensor no ve?
- 🔗 **Se estudia junto con:** matriz de interacción, empuje-tirón, matriz de control, valores singulares.

📘 **Dónde se aprende** (1 clase): [B42-C23 · Calibración de la matriz de interacción y aberraciones no comunes](../programa/clases/B42/B42-C23-calibracion-de-la-matriz-de-interaccion-y-aberraciones-no-comunes/CLASE.md).

### Nivel

- Un nivel `ℓ` es un conjunto de celdas del mismo tamaño `Δx_ℓ = Δx₀/2^ℓ` (razón de refinamiento 2).
- Un nivel es un intervalo de la escala.
- El nivel es la categoría que resulta de los umbrales.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B21-C05](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md):**
- Partiendo de 32 celdas (`Δx = 1/32`), eso son 6 niveles (`1/(32·64) = 4,9 × 10⁻⁴`).
- Los niveles siguientes no se activan, porque el error ya es el tolerado.
- ⚠️ **Error frecuente:** Pensar que más niveles siempre bajan el error. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** Los códigos de referencia en astrofísica, como RAMSES (S1) y Athena++ (S2), usan mallas adaptativas porque los problemas tienen rangos de escala enormes. Pero un esquema adaptativo mal construido no conserva: crea o destruye masa en las interfaces entre niveles, justo donde está el fenómeno interesante.
- 🔗 **Se estudia junto con:** malla adaptativa, criterio de refinamiento, suavizado de malla, restricción.

📘 **Dónde se aprende** (4 clases): [B21-C05 · Mallas adaptativas (AMR)](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md); [B33-C04 · Escalas de severidad de clima espacial](../programa/clases/B33/B33-C04-escalas-de-severidad-de-clima-espacial/CLASE.md); [B119-C35 · Seguridad y gobernanza de datos espaciales](../programa/clases/B119/B119-C35-seguridad-y-gobernanza-de-datos-espaciales/CLASE.md); [B122-C07 · Clasificación de severidad e impacto de incidentes espaciales](../programa/clases/B122/B122-C07-clasificacion-de-severidad-e-impacto-de-incidentes-espaciales/CLASE.md).

### Nivel cognitivo

- El nivel cognitivo ordena la exigencia: recordar, comprender, aplicar, analizar, evaluar, crear.

💡 **Cómo se explica en la clase [B131-C02](../programa/clases/B131/B131-C02-resultados-de-aprendizaje-observables-en-astronomia/CLASE.md):**
- Asignar un nivel cognitivo ilustrativo (1 recordar … 6 crear).
- 🎯 **Por qué importa:** Sin resultados observables, una actividad no se puede evaluar. La decisión central: ¿este enunciado dice algo que pueda verse que el estudiante hace?
- 🔗 **Se estudia junto con:** resultado de aprendizaje, observable, alineación, huérfano.

📘 **Dónde se aprende** (1 clase): [B131-C02 · Resultados de aprendizaje observables en astronomía](../programa/clases/B131/B131-C02-resultados-de-aprendizaje-observables-en-astronomia/CLASE.md).

### Nivel de 1 bar

- El nivel de 1 bar es la referencia de altura de un gigante.

💡 **Cómo se explica en la clase [B54-C15](../programa/clases/B54/B54-C15-atmosferas-de-gigantes-gaseosos/CLASE.md):**
- *Descripción textual:* la composición y la gravedad dan `H`; el balance solar da `T_e` y el exceso del nivel de 1 bar; con `κ` se integra la adiabata hacia dentro.
- Calcular la temperatura de equilibrio solar y el exceso del nivel de 1 bar.
- 🎯 **Por qué importa:** La atmósfera de Júpiter es una capa convectiva muy profunda. La pregunta motivadora: ¿cuánto más caliente es el nivel de 1 bar que el equilibrio solar y cómo crece la temperatura hacia dentro?
- 🔗 **Se estudia junto con:** calor interno, adiabata profunda, supuesto.

📘 **Dónde se aprende** (1 clase): [B54-C15 · Atmósferas de gigantes gaseosos](../programa/clases/B54/B54-C15-atmosferas-de-gigantes-gaseosos/CLASE.md).

### Nivel de acción

- El nivel de acción es la concentración que obliga a intervenir.

💡 **Cómo se explica en la clase [B115-C07](../programa/clases/B115/B115-C07-bioseguridad-e-inocuidad-alimentaria-en-habitats/CLASE.md):**
- Una contaminación de 10 UFC/mL llega al límite de detección (10² UFC/mL) en `t_d = ln 10/r` y al nivel de acción (10⁴) en `t_a = ln 1000/r`.
- C -->|"antes de ser detectada"| N["nivel de acción<br/>alcanzado"]
- 🎯 **Por qué importa:** Una contaminación en un circuito compartido afecta a todos los lotes a la vez. La decisión central: ¿con qué frecuencia se muestrea, qué se mide y qué barreras (desinfección, lavado, temperatura) hacen falta para que una contaminación se detecte antes de llegar a un nivel de acción?
- 🔗 **Se estudia junto con:** inocuidad, bioseguridad, carga microbiana, reducción logarítmica (LR).

📘 **Dónde se aprende** (1 clase): [B115-C07 · Bioseguridad e inocuidad alimentaria en hábitats](../programa/clases/B115/B115-C07-bioseguridad-e-inocuidad-alimentaria-en-habitats/CLASE.md).

### Nivel de bias

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B47-C15](../programa/clases/B47/B47-C15-calibracion-a-bordo/CLASE.md):**
- **Idea central (modelo mental):** Es calibrar una balanza sin pesas patrón: mides el azar de las lecturas y, como el azar de contar fotones es conocido, de ahí se deduce cuánto pesa cada cuenta.
- 🎯 **Por qué importa:** Sin ganancia ni ruido calibrados no se puede convertir cuentas en fotones ni dar incertidumbres. La decisión central: ¿cómo se obtiene la ganancia sin conocerla y cuánto residuo deja la corrección de campo plano?
- 🔗 **Se estudia junto con:** curva de transferencia de fotones, ganancia, ruido de lectura, campo plano.

📘 **Dónde se aprende** (1 clase): [B47-C15 · Calibración a bordo](../programa/clases/B47/B47-C15-calibracion-a-bordo/CLASE.md).

### Nivel de bioseguridad 1

- El nivel de bioseguridad 1 corresponde a organismos no patógenos manejados con buenas prácticas de laboratorio.

💡 **Cómo se explica en la clase [B64-C07](../programa/clases/B64/B64-C07-cultivo-de-extremofilos-no-patogenos-en-condiciones-analogas/CLASE.md):**
- Solo se cultivan organismos no patógenos de nivel de bioseguridad 1, obtenidos de una colección reconocida; no se manipulan muestras ambientales sin análisis de riesgo institucional, y toda cámara se opera con las normas de su laboratorio.
- No procede sin análisis de riesgo institucional, autorización y trabajo en el nivel de bioseguridad que corresponda; en esta clase solo se tratan organismos no patógenos de colección.
- 🎯 **Por qué importa:** Un análogo no es el otro mundo: reproduce algunas variables y deja otras. La pregunta motivadora: ¿qué parte del ambiente real estás imitando, qué parte no y qué puedes concluir de un cultivo en la cámara?
- 🔗 **Se estudia junto con:** cámara análoga, presión parcial, ley de Henry, capacidad de carga.

📘 **Dónde se aprende** (1 clase): [B64-C07 · Cultivo de extremófilos no patógenos en condiciones análogas](../programa/clases/B64/B64-C07-cultivo-de-extremofilos-no-patogenos-en-condiciones-analogas/CLASE.md).

### Nivel de condensación

- El nivel de condensación es la altura en que una parcela ascendente alcanza la saturación.

💡 **Cómo se explica en la clase [B54-C08](../programa/clases/B54/B54-C08-nubes-y-aerosoles/CLASE.md):**
- Con `T = 303 K`, `T_d = 293 K` y gradientes seco `9,76 K/km` y de rocío `1,8 K/km`, el nivel de condensación es `1256 m` (la regla empírica `125 m/K` daría `1250 m`).
- T["T, punto de rocío"] --> LCL["nivel de condensación"]
- 🎯 **Por qué importa:** La condensación libera calor, forma nubes que cambian el albedo y limita cuánto vapor admite el aire. La pregunta motivadora: ¿a qué altura se forma una nube y cuánto tarda una partícula en caer de ella?
- 🔗 **Se estudia junto con:** ecuación de Clausius–Clapeyron, aerosol, velocidad de Stokes, número de Reynolds.

📘 **Dónde se aprende** (1 clase): [B54-C08 · Nubes y aerosoles](../programa/clases/B54/B54-C08-nubes-y-aerosoles/CLASE.md).

### Nivel de confianza

- Un intervalo de confianza bilateral es un par de funciones de los datos `T₁ < T₂` tales que, repetido el experimento, la fracción de veces que el intervalo contiene el parámetro es el nivel de confianza (S1, C.2.27 y C.2.29).
- El nivel de confianza (o probabilidad de cobertura) es la fracción que se atribuye al intervalo; asociarlo a `U` exige suposiciones sobre la distribución (S1, 2.3.5, nota 2).

💡 **Cómo se explica en la clase [B13-C12](../programa/clases/B13/B13-C12-incertidumbre-expandida/CLASE.md):**
- Se reporta `y`, `U`, `k`, la distribución supuesta y el nivel de confianza o los grados de libertad.
- *Descripción textual:* de las lecturas salen la media, `u` y los grados de libertad; con ellos y el nivel de confianza deseado se elige `k`; de `U = k u` sale el intervalo con su cobertura.
- ⚠️ **Error frecuente:** Dar `U` sin `k` ni nivel de confianza. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Un telémetro da `1000,004 m` con una incertidumbre típica de `0,017 m`. ¿Cuál es el intervalo dentro del cual el valor verdadero cae «casi seguro»?
- 🔗 **Se estudia junto con:** incertidumbre típica, incertidumbre típica combinada u_c, incertidumbre expandida U, factor de cobertura k.

📘 **Dónde se aprende** (2 clases): [B12-C08 · Intervalos de confianza](../programa/clases/B12/B12-C08-intervalos-de-confianza/CLASE.md); [B13-C12 · Incertidumbre expandida](../programa/clases/B13/B13-C12-incertidumbre-expandida/CLASE.md).

### Nivel de energía

- Un nivel de energía es uno de los valores permitidos para la energía del electrón en el átomo; se numera con `n = 1, 2, 3…`.

💡 **Cómo se explica en la clase [B06-C01](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md):**
- La analogía de la escalera es útil para entender que la energía está cuantizada, pero tiene un límite: los peldaños de una escalera están en el espacio, mientras que los niveles son valores de energía; el electrón no «sube» físicamente un escalón.
- Puedes calcular `λ` por energías (restar dos niveles y dividir `hc` por la diferencia) o directamente con la fórmula de Rydberg.
- 🎯 **Por qué importa:** Casi todo lo que sabemos de la composición de una estrella o de una nebulosa lo sabemos porque sus átomos emiten o absorben luz en colores muy precisos. Una línea roja a 656 nm no es «un color cualquiera»: es la firma del hidrógeno.
- 🔗 **Se estudia junto con:** átomo, núcleo, protones, neutrones.

📘 **Dónde se aprende** (1 clase): [B06-C01 · Estructura atómica](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md).

### Nivel de ensayo

- El nivel de ensayo es el extremo predicho más el margen.

💡 **Cómo se explica en la clase [B85-C19](../programa/clases/B85/B85-C19-ensayos-de-vacio-termico/CLASE.md):**
- P["Extremos predichos + margen"] --> N["Niveles de ensayo"]
- Fijar los niveles de ensayo como extremos predichos más margen.
- 🎯 **Por qué importa:** Un ensayo mal planificado dura el doble o no cubre el caso extremo. La decisión central: ¿qué temperaturas de pantalla, rampas y dwells cubren los extremos predichos con margen y cuánto dura el ensayo?
- 🔗 **Se estudia junto con:** margen, pantalla, rampa, estabilización.

📘 **Dónde se aprende** (1 clase): [B85-C19 · Ensayos de vacío térmico](../programa/clases/B85/B85-C19-ensayos-de-vacio-termico/CLASE.md).

### Nivel de escalada

- El nivel de escalada es el estado de la tensión.

💡 **Contexto en la clase [B119-C29](../programa/clases/B119/B119-C29-escalada-desescalada-y-medidas-de-fomento-de-la-confianza/CLASE.md):**
- 🎯 **Por qué importa:** C28 y C27 tratan conductas y negociación; ninguna clase muestra la dinámica de escalada ni el valor de las medidas de confianza, que se apoyan en el principio de informar (art. XI) y consultar (art.
- 🔗 **Se estudia junto con:** desescalada, medida de fomento de la confianza, matriz fundamental, absorción.

📘 **Dónde se aprende** (1 clase): [B119-C29 · Escalada, desescalada y medidas de fomento de la confianza](../programa/clases/B119/B119-C29-escalada-desescalada-y-medidas-de-fomento-de-la-confianza/CLASE.md).

### Nivel de evidencia

- El nivel de evidencia va de 2 (texto o tabla leídos) a 0 (sin evidencia hallada).

💡 **Cómo se explica en la clase [B121-C04](../programa/clases/B121/B121-C04-marco-legal-espacial-en-chile/CLASE.md):**
- I -->|no hallado| N0["Nivel 0: sin evidencia"]
- Clasificar cada función regulatoria por nivel de evidencia (2, 1, 0).
- 🎯 **Por qué importa:** Un marco nacional se conoce por sus instrumentos, y cada instrumento debe leerse en su texto vigente. La decisión central: ¿qué funciones regulatorias tienen un instrumento chileno identificado y con qué nivel de evidencia?
- 🔗 **Se estudia junto con:** función regulatoria, instrumento, traducción no oficial, concesión.

📘 **Dónde se aprende** (1 clase): [B121-C04 · Marco legal espacial en Chile](../programa/clases/B121/B121-C04-marco-legal-espacial-en-chile/CLASE.md).

### Nivel de potencia sonora

- El nivel de potencia sonora `Lw` describe la fuente; el nivel de presión `Lp`, lo que se mide en un punto.

💡 **Contexto en la clase [B109-C10](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md):**
- 🎯 **Por qué importa:** El ruido continuo degrada la comunicación, el sueño y el trabajo aunque no dañe el oído. La decisión central: ¿qué fuente reduzco primero y cuánto baja el nivel de la cabina?
- 🔗 **Se estudia junto con:** nivel de presión, campo directo, reverberante, absorción.

📘 **Dónde se aprende** (1 clase): [B109-C10 · Acústica y control de ruido interior](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md).

### Nivel de presión

- El nivel de potencia sonora `Lw` describe la fuente; el nivel de presión `Lp`, lo que se mide en un punto.

💡 **Contexto en la clase [B109-C10](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md):**
- 🎯 **Por qué importa:** El ruido continuo degrada la comunicación, el sueño y el trabajo aunque no dañe el oído. La decisión central: ¿qué fuente reduzco primero y cuánto baja el nivel de la cabina?
- 🔗 **Se estudia junto con:** nivel de potencia sonora, campo directo, reverberante, absorción.

📘 **Dónde se aprende** (1 clase): [B109-C10 · Acústica y control de ruido interior](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md).

### Nivel de presión sonora

- El nivel de presión sonora se mide en dB y, ponderado, en dBA.

💡 **Contexto en la clase [B109-C09](../programa/clases/B109/B109-C09-privacidad-y-espacios-personales/CLASE.md):**
- 🎯 **Por qué importa:** Una división que no se ve a través pero que deja pasar cada palabra no da privacidad. La decisión central: ¿qué masa debe tener una división para que lo que se dice al otro lado quede por debajo del ruido de fondo?
- 🔗 **Se estudia junto con:** privacidad acústica, pérdida de transmisión, ley de masa, ruido de fondo.

📘 **Dónde se aprende** (1 clase): [B109-C09 · Privacidad y espacios personales](../programa/clases/B109/B109-C09-privacidad-y-espacios-personales/CLASE.md).

### Nivel de procesamiento

- Retransmisión: reenvío de faltantes. Nivel de procesamiento: grado de elaboración del dato (L0, L1, L2).

💡 **Cómo se explica en la clase [B96-C16](../programa/clases/B96/B96-C16-gestion-de-datos-cientificos/CLASE.md):**
- Calcular el volumen por nivel de procesamiento.
- ⚠️ **Error frecuente:** Mezclar niveles de procesamiento. Rotula L0, L1 y L2 (8.4)
- 🎯 **Por qué importa:** Un conjunto de datos con huecos no declarados da conclusiones erróneas, y una retransmisión sin plan agota los contactos. La decisión central: ¿qué falta, cuántas pasadas hacen falta para completarlo y qué producto se entrega en cada nivel?
- 🔗 **Se estudia junto con:** Paquete, Hueco, Completitud, Retransmisión.

📘 **Dónde se aprende** (1 clase): [B96-C16 · Gestión de datos científicos](../programa/clases/B96/B96-C16-gestion-de-datos-cientificos/CLASE.md).

### Nivel de retorno

- El nivel de retorno `x_T` es el valor superado en promedio una vez cada `T` años.

💡 **Cómo se explica en la clase [B30-C19](../programa/clases/B30/B30-C19-impactos-del-clima-espacial/CLASE.md):**
- *Descripción textual:* el campo y la longitud dan la corriente por un circuito; el registro da el índice de la cola, el nivel de retorno y su intervalo.
- Calcular el nivel de retorno `x_min(NT)^(1/(α−1))`.
- 🎯 **Por qué importa:** Las infraestructuras se diseñan para eventos raros, que no están en un registro corto. La decisión central: ¿qué corriente induce un campo dado y cuán fiable es extrapolar un nivel de 100 años?
- 🔗 **Se estudia junto con:** GIC, campo geoeléctrico, índice de la cola, extrapolación.

📘 **Dónde se aprende** (2 clases): [B30-C19 · Impactos del clima espacial](../programa/clases/B30/B30-C19-impactos-del-clima-espacial/CLASE.md); [B33-C03 · Eventos extremos históricos de clima espacial](../programa/clases/B33/B33-C03-eventos-extremos-historicos-de-clima-espacial/CLASE.md).

### Nivel de servicio por ciclo

- El nivel de servicio por ciclo es la probabilidad de que la demanda en `T` no supere `S`.

💡 **Cómo se explica en la clase [B100-C03](../programa/clases/B100/B100-C03-gestion-de-inventarios-y-reposicion-de-suministros/CLASE.md):**
- El script [reposicion.py](reposicion.py) calcula `S` y la reserva de dos políticas, simula 3000 ciclos de cada una con demanda normal sintética y compara con el nivel de servicio objetivo (comprueba servicio dentro de 2 puntos y cociente de reservas `√(T_B/T_A)`).
- 🎯 **Por qué importa:** Con una reposición de 10 días basta una reserva pequeña; con una ventana sinódica de Marte la misma demanda exige guardar casi dos años y medio de consumo. La decisión central: ¿hasta qué nivel conviene reponer en cada ventana para que la probabilidad de quedarse sin existencias en el ciclo sea de un 5 %?
- 🔗 **Se estudia junto con:** intervalo de revisión, demora, intervalo de protección, nivel máximo.

📘 **Dónde se aprende** (1 clase): [B100-C03 · Gestión de inventarios y reposición de suministros](../programa/clases/B100/B100-C03-gestion-de-inventarios-y-reposicion-de-suministros/CLASE.md).

### Nivel de significación

- El nivel de significación `α` es la tasa de falsos rechazos que se acepta (error tipo I); el error tipo II (probabilidad `β`) es no rechazar una `H₀` falsa; la potencia `1 − β` es la probabilidad de detectar un efecto real de un tamaño dado.
- El nivel de significación `α` es la probabilidad máxima admitida de rechazar `H₀` cuando es verdadera.
- El nivel de significación `α` es la tasa de falsos positivos aceptada.

💡 **Cómo se explica en la clase [B124-C18](../programa/clases/B124/B124-C18-comunicacion-y-divulgacion/CLASE.md):**
- Comprobar potencia y nivel de significación con una simulación.
- Ejercicio 7 · autónomo. ¿Y el nivel de significación simulado?
- 🎯 **Por qué importa:** Sin medir, la divulgación se evalúa por impresión. La decisión central: ¿cuántas personas hay que observar para saber si un mensaje funciona mejor que otro, y cuánto alcance real tiene una campaña?
- 🔗 **Se estudia junto con:** embudo, prueba A/B, potencia, tamaño de muestra.

📘 **Dónde se aprende** (3 clases): [B12-C09 · Pruebas de hipótesis](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md); [B20-C02 · Diseño de un plan de análisis y preregistro](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md); [B124-C18 · Comunicación y divulgación](../programa/clases/B124/B124-C18-comunicacion-y-divulgacion/CLASE.md).

### Nivel del 95 % de confianza

- El límite de carrera de NASA se fija con un REID del 3 % al nivel del 95 % de confianza, que según el informe de National Academies (2021) corresponde al percentil 97,5 de la distribución de incertidumbre.

💡 **Contexto en la clase [B112-C06](../programa/clases/B112/B112-C06-modelos-de-riesgo-de-radiacion-para-misiones/CLASE.md):**
- 🎯 **Por qué importa:** Falta la clase de estimación de riesgo por misión. Es la que usa un planificador: suma dosis de cada tramo, la convierte en riesgo y decide si cabe dentro de un límite.
- 🔗 **Se estudia junto con:** riesgo de exceso de muerte inducida por exposición, límite de carrera, límite administrativo, ALARA.

📘 **Dónde se aprende** (1 clase): [B112-C06 · Modelos de riesgo de radiación para misiones](../programa/clases/B112/B112-C06-modelos-de-riesgo-de-radiacion-para-misiones/CLASE.md).

### Nivel máximo

- El nivel máximo `S` es el nivel hasta el que se repone.

💡 **Cómo se explica en la clase [B100-C03](../programa/clases/B100/B100-C03-gestion-de-inventarios-y-reposicion-de-suministros/CLASE.md):**
- La reserva crece con `√T`: `152,9/31,2 = 4,90 = √(960/40)`; el nivel máximo crece casi con `T` (`22,6` veces).
- La demora tecnológica `L` (180 d) pesa menos que el intervalo de revisión `R` (780 d): la ventana fija casi todo el nivel máximo.
- 🎯 **Por qué importa:** Con una reposición de 10 días basta una reserva pequeña; con una ventana sinódica de Marte la misma demanda exige guardar casi dos años y medio de consumo. La decisión central: ¿hasta qué nivel conviene reponer en cada ventana para que la probabilidad de quedarse sin existencias en el ciclo sea de un 5 %?
- 🔗 **Se estudia junto con:** intervalo de revisión, demora, intervalo de protección, reserva de seguridad.

📘 **Dónde se aprende** (1 clase): [B100-C03 · Gestión de inventarios y reposición de suministros](../programa/clases/B100/B100-C03-gestion-de-inventarios-y-reposicion-de-suministros/CLASE.md).

### Nivel topológico

- El nivel topológico es la longitud del camino más largo hasta el hardware.

💡 **Cómo se explica en la clase [B88-C23](../programa/clases/B88/B88-C23-arquitectura-de-software-de-vuelo-capas-y-ejecutivo/CLASE.md):**
- Calcular el nivel topológico de cada módulo.
- Nivel topologico: {'uart_hw': 0, 'adc_hw': 0, 'hal_uart': 1, 'hal_adc': 1, 'rtos': 2, 'tm_tc': 3, 'fdir': 3, 'aocs': 4, 'energia': 4}
- 🎯 **Por qué importa:** Las dependencias hacia arriba y los ciclos hacen imposible probar un módulo por separado y convierten un cambio en riesgo global. La decisión central: ¿qué módulo depende de quién, y puede ordenarse el sistema en capas sin ciclos?
- 🔗 **Se estudia junto con:** capa, dependencia hacia arriba, ciclo menor, mayor.

📘 **Dónde se aprende** (1 clase): [B88-C23 · Arquitectura de software de vuelo: capas y ejecutivo](../programa/clases/B88/B88-C23-arquitectura-de-software-de-vuelo-capas-y-ejecutivo/CLASE.md).

### Niveles de Landau relativistas

- Los niveles de Landau relativistas son `E_n = m c²(√(1 + 2nB/B_Q) − 1)`.

💡 **Cómo se explica en la clase [B27-C06](../programa/clases/B27/B27-C06-magnetares-y-campos-extremos/CLASE.md):**
- Calcular los niveles de Landau relativistas.
- 🎯 **Por qué importa:** Los magnetares producen estallidos y llamaradas gigantes que alimenta su campo, no su rotación. Entender la escala del campo y de su energía explica por qué son una familia aparte y cómo se interpretan sus espectros.
- 🔗 **Se estudia junto con:** magnetar, campo crítico cuántico, energía ciclotrónica, energía magnética.

📘 **Dónde se aprende** (1 clase): [B27-C06 · Magnetares y campos extremos](../programa/clases/B27/B27-C06-magnetares-y-campos-extremos/CLASE.md).

### Niveles I, II y III

- Los niveles I, II y III escalan la revisión según actividad, probabilidad de dosis y fisión.

💡 **Cómo se explica en la clase [B86-C18](../programa/clases/B86/B86-C18-seguridad-y-licenciamiento-energetico/CLASE.md):**
- La memoria presidencial NSPM-20 (2019) fija tres niveles de autorización de lanzamiento.
- El Nivel I cubre fuentes radiactivas hasta `100000 × A2` (valor de la tabla 2 de la IAEA SSR-6, Rev.1).
- ⚠️ **Error frecuente:** Decidir el nivel con la actividad inicial en vez de la del lanzamiento. Se corrige con 8.4.
- 🎯 **Por qué importa:** Los límites de la energía nuclear en el espacio son tanto jurídicos y de seguridad como técnicos: quién aprueba, con qué análisis y con qué umbrales. Un ingeniero de potencia debe saber que estas decisiones existen y qué datos las gobiernan.
- 🔗 **Se estudia junto con:** NSPM-20, A2, TED, LEU.

📘 **Dónde se aprende** (1 clase): [B86-C18 · Seguridad y licenciamiento energético](../programa/clases/B86/B86-C18-seguridad-y-licenciamiento-energetico/CLASE.md).

### NMAD

- El NMAD es `1,4826` veces la mediana de las desviaciones absolutas respecto de la mediana; es robusto a atípicos.

💡 **Cómo se explica en la clase [B57-C31](../programa/clases/B57/B57-C31-errores-y-validacion-de-modelos-de-elevacion/CLASE.md):**
- Con 200 000 errores gaussianos de `σ = 2 m`: RMSE `2,002`, NMAD `2,008` y LE90 `3,298` (teoría `1,645σ = 3,290`).
- Los atípicos inflan el RMSE y casi no mueven el NMAD ni el LE90: el RMSE es la métrica más frágil.
- 🎯 **Por qué importa:** Decir «el MDE tiene 4 m de error» sin definir la métrica ni los puntos de control no significa nada. La decisión central: ¿qué métrica y qué intervalo de confianza reporto para que mi validación sea comparable y honesta?
- 🔗 **Se estudia junto con:** sesgo (ME), RMSE, LE90, punto de control.

📘 **Dónde se aprende** (1 clase): [B57-C31 · Errores y validación de modelos de elevación](../programa/clases/B57/B57-C31-errores-y-validacion-de-modelos-de-elevacion/CLASE.md).

### NMSUS

- El NMSUS es el cuestionario modificado de usabilidad de NASA (8 ítems, 1 a 5).

💡 **Cómo se explica en la clase [B109-C12](../programa/clases/B109/B109-C12-evaluacion-de-factores-humanos-de-maquetas-y-distribuciones/CLASE.md):**
- Según la nota técnica de NASA, el NMSUS se puntúa con `NMSUS = 3,125 × ((Q1−1)+(5−Q2)+(Q3−1)+(5−Q4)+(Q5−1)+(5−Q6)+(Q7−1)+(5−Q8))`, con respuestas de `1` a `5`.
- La nota indica que el NMSUS fue tan fiable como el SUS en un estudio con `35` participantes; la nota es un resumen breve que se leyó completo; el estudio completo no se consultó.
- 🎯 **Por qué importa:** Sin medir, «esta distribución es mejor» es una opinión. La decisión central: ¿la diferencia entre dos maquetas es mayor que lo que daría el azar, y las personas que la evalúan coinciden entre sí?
- 🔗 **Se estudia junto con:** evaluación con maqueta, lista de verificación, prueba pareada, kappa de Cohen.

📘 **Dónde se aprende** (1 clase): [B109-C12 · Evaluación de factores humanos de maquetas y distribuciones](../programa/clases/B109/B109-C12-evaluacion-de-factores-humanos-de-maquetas-y-distribuciones/CLASE.md).

### NNLS

- Biblioteca: conjunto de espectros de referencia. NNLS: ajuste con pesos no negativos.

💡 **Cómo se explica en la clase [B106-C22](../programa/clases/B106/B106-C22-fuentes-e-identificacion-de-contaminantes-del-aire-de-cabina/CLASE.md):**
- La mezcla `y = L w + ruido` con 6 espectros sintéticos de 24 canales y pesos `(0; 3; 0; 1,2; 0; 0,6)`: el NNLS da `(0; 3,008; 0,006; 1,196; 0,003; 0,592)` con error máximo 0,008.
- S["espectro medido"] --> N["NNLS con biblioteca"]
- ⚠️ **Error frecuente:** Identificar solo por similitud. Descompón con NNLS (8.3).
- 🎯 **Por qué importa:** Nada sale al exterior de una cabina cerrada: los materiales emiten gases durante meses, los equipos liberan trazas y las personas emiten vapor y CO₂. La decisión central: ¿qué fuentes dominan en cada momento y cómo se identifican los compuestos para decidir qué retirar?
- 🔗 **Se estudia junto con:** Desgasificación, Fuente metabólica, Espectro de masas, Biblioteca.

📘 **Dónde se aprende** (1 clase): [B106-C22 · Fuentes e identificación de contaminantes del aire de cabina](../programa/clases/B106/B106-C22-fuentes-e-identificacion-de-contaminantes-del-aire-de-cabina/CLASE.md).

### No

- Independientes (S1, C.3.7) es más fuerte: la distribución de una no cambia al conocer la otra; independientes ⇒ `Cov = 0`, pero no al revés.
- Intersecar dos cajas es que se solapen con área positiva; cajas que solo comparten un borde no se intersecan en este laboratorio.
- El grado de prueba es aquí una convención didáctica entre 0 y 1, no una regla jurídica.

💡 **Cómo se explica en la clase [B12-C05](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md):**
- Con los eventos de C01, `A` = «al menos 2 computadores funcionan» (`0,972`) y `B` = «el 1 funciona» (`0,9`), y `P(A∩B) = 0,891`: los indicadores `1_A` y `1_B` (vale 1 si ocurre, 0 si no) tienen `E[1_A 1_B] = P(A∩B)`.
- Al crecer `n`, la varianza tiende a `σ²ρ = 4,5 m²`: promediar no puede eliminar la parte común.
- 🎯 **Por qué importa:** En navegación espacial, la posición y la velocidad estimadas por un filtro no tienen errores independientes: un error de posición hacia delante suele ir acompañado de uno de velocidad. Ignorar esa relación da incertidumbres falsas, a veces demasiado optimistas y a veces demasiado pesimistas.
- 🔗 **Se estudia junto con:** covarianza, coeficiente de correlación, no correlacionadas, Independientes.

📘 **Dónde se aprende** (3 clases): [B12-C05 · Covarianza y correlación](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md); [B14-C25 · Catálogos de datos geoespaciales y metadatos (STAC)](../programa/clases/B14/B14-C25-catalogos-de-datos-geoespaciales-y-metadatos-stac/CLASE.md); [B123-C01 · Prueba del daño y cuantificación de la reparación](../programa/clases/B123/B123-C01-prueba-del-dano-y-cuantificacion-de-la-reparacion/CLASE.md).

### No asociatividad

- La no asociatividad es la propiedad de que `(a + b) + c ≠ a + (b + c)` en coma flotante.

💡 **Contexto en la clase [B14-C15](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md):**
- **Idea central (modelo mental):** El tiempo en GPU es el de mover los datos más el de calcular. La GPU hace el cálculo mucho más rápido, pero mover los datos cuesta lo mismo con cualquier cálculo. Si el cálculo es corto frente al movimiento, la ganancia desaparece.
- 🎯 **Por qué importa:** Un equipo promete que su simulación irá «100 veces más rápido en GPU» y, al compararla con la de CPU, los resultados difieren en el séptimo dígito. ¿Error del código o característica de la máquina?
- 🔗 **Se estudia junto con:** GPU, transferencia, intensidad aritmética, reducción.

📘 **Dónde se aprende** (1 clase): [B14-C15 · Cálculo en GPU y limitaciones](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md).

### No conformidad

- Anomalía/discrepancia: variación frente a lo esperado. No conformidad: producto que no cumple su requisito.

💡 **Cómo se explica en la clase [B90-C17](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md):**
- S1: detener, abrir no conformidad y revisar con un comité.
- La evidencia es el informe de no conformidad con su disposición del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Una falla única en 500 horas de ensayo no demuestra que el equipo sea confiable: solo acota la tasa de fallas. Y una anomalía mal registrada se pierde.
- 🔗 **Se estudia junto con:** Anomalía/discrepancia, Disposición, Severidad, Causa raíz.

📘 **Dónde se aprende** (1 clase): [B90-C17 · Gestión de anomalías de prueba](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md).

### No consultadas

- Constantes y fórmula estándar, no consultadas en una fuente.

💡 **Cómo se explica en la clase [B105-C21](../programa/clases/B105/B105-C21-fisiologia-respiratoria-en-microgravedad-y-atmosferas-de-cabina/CLASE.md):**
- Datos: constantes estándar no consultadas; cabinas ilustrativas; sin mediciones.
- 🎯 **Por qué importa:** La misma cantidad de oxígeno inspirado no significa lo mismo a 101 kPa que a 70 kPa: importa la presión parcial. La decisión central: ¿qué presión parcial de oxígeno alveolar resulta de una atmósfera dada y cómo cambia con el CO₂ ambiente y la ventilación?
- 🔗 **Se estudia junto con:** ecuación del gas alveolar, presión inspirada, altitud equivalente, ppm.

📘 **Dónde se aprende** (1 clase): [B105-C21 · Fisiología respiratoria en microgravedad y atmósferas de cabina](../programa/clases/B105/B105-C21-fisiologia-respiratoria-en-microgravedad-y-atmosferas-de-cabina/CLASE.md).

### No correlacionadas

- Si `r = 0` las variables están no correlacionadas: un cambio en una no implica un cambio esperado en la otra (S1, 5.2.2).

💡 **Contexto en la clase [B12-C05](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md):**
- **Idea central (modelo mental):** Imagina cada par `(x, y)` como un punto. Si la nube es una bola redonda, no hay relación; si se estira en diagonal, hay correlación; cuanto más delgada la elipse, más cerca de `±1`. La covarianza es la mitad «sin escala» de esa inclinación, y `r` la normaliza.
- 🎯 **Por qué importa:** En navegación espacial, la posición y la velocidad estimadas por un filtro no tienen errores independientes: un error de posición hacia delante suele ir acompañado de uno de velocidad. Ignorar esa relación da incertidumbres falsas, a veces demasiado optimistas y a veces demasiado pesimistas.
- 🔗 **Se estudia junto con:** covarianza, coeficiente de correlación, Independientes, no.

📘 **Dónde se aprende** (1 clase): [B12-C05 · Covarianza y correlación](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md).

### No determinista

- Lo no determinista es lo que cambia entre ejecuciones sin cambiar el cálculo (fecha, nombre del equipo).

💡 **Cómo se explica en la clase [B23-C07](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md):**
- Construir un registro de procedencia y una huella canónica que excluya lo no determinista.
- Ejercicio 12 · integrador. Entrega un registro de procedencia verificable para una cifra de uno de tus laboratorios: función `registrar` y `verificar`, huella que excluya lo no determinista, pruebas de (a) reproducción, (b) alteración de datos, (c) cambio de parámetro y (d) cita de la cifra.
- 🎯 **Por qué importa:** Un informe dice «el modelo reproduce la posición con un error de 8,21 × 10⁻⁴ au». Seis meses después, nadie sabe con qué versión del código, qué archivo de datos ni qué tolerancia se calculó, y el número no se puede reproducir ni defender.
- 🔗 **Se estudia junto con:** trazabilidad, registro de procedencia, hash, SHA-256.

📘 **Dónde se aprende** (1 clase): [B23-C07 · Trazabilidad científica de resultados](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md).

### No evaluado

- Un criterio crítico bloquea el veredicto si no se cumple. No evaluado es un estado que no cuenta como cumplido.

💡 **Cómo se explica en la clase [B128-C11](../programa/clases/B128/B128-C11-auditoria-de-accesibilidad-de-un-recurso-educativo/CLASE.md):**
- Cumple = 1,0; parcial = 0,5; no cumple = 0,0; no evaluado = excluido.
- `puntaje = Σ(peso × valor)/Σ(peso)` sobre lo evaluado.
- ⚠️ **Error frecuente:** Contar «no evaluado» como cumplido. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Un puntaje alto puede esconder una barrera grave: un video sin subtítulos con todo lo demás perfecto sigue siendo inaccesible para quien no oye. La decisión central: ¿cómo reporto el estado de un recurso sin que el promedio oculte un bloqueo y sin dar por cumplido lo que no se evaluó?
- 🔗 **Se estudia junto con:** criterio, peso, crítico, prioridad.

📘 **Dónde se aprende** (1 clase): [B128-C11 · Auditoría de accesibilidad de un recurso educativo](../programa/clases/B128/B128-C11-auditoria-de-accesibilidad-de-un-recurso-educativo/CLASE.md).

### No exclusiva

- La licencia exclusiva se da a un solo licenciatario; la no exclusiva, a varios.

💡 **Cómo se explica en la clase [B124-C09](../programa/clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md):**
- Exclusiva: un licenciatario con ventas 1,6 veces mayores, regalía de 6 % y cuota de 5 Mum, vale `45,997` Mum para el licenciante.
- No exclusiva: tres licenciatarios, regalía de 4 % y cuota de 1 Mum cada uno, valen `54,247` Mum.
- ⚠️ **Error frecuente:** Suponer que la exclusiva siempre vale más. Se corrige con 8.3–8.4.
- 🎯 **Por qué importa:** La propiedad intelectual es un activo, pero su valor depende de cuánto se vende con ella y de cuánto del margen se queda el que la usa. La decisión central: ¿qué licencia conviene ofrecer y cuántas regalías soporta el licenciatario?
- 🔗 **Se estudia junto con:** licencia, cuota inicial, regalía, valor actual.

📘 **Dónde se aprende** (1 clase): [B124-C09 · Propiedad intelectual y licencias](../programa/clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md).

### No ionizante

- La radiación ionizante es la que tiene energía suficiente para arrancar electrones de átomos o moléculas (del orden de varios a decenas de eV o más); la no ionizante no la tiene.
- La radiación ionizante tiene energía suficiente para arrancar electrones; la no ionizante no.

💡 **Cómo se explica en la clase [B05-C18](../programa/clases/B05/B05-C18-electromagnetismo-y-radiacion/CLASE.md):**
- Distinguir radiación ionizante de no ionizante y explicar por qué importa.
- Ejercicio 12 · integrador. Elabora una *ficha de banda y flujo* (sección 20): elige una banda y una frecuencia, calcula `λ`, `E` (J y eV), el flujo de una fuente isótropa a dos distancias, el retardo y si la banda es ionizante (con la fuente).
- 🎯 **Por qué importa:** Un satélite se comunica con ondas de radio, un telescopio observa luz y rayos X, y la misma radiación a otras energías puede dañar electrónica y tejidos. La pregunta motivadora es: ¿qué es la radiación electromagnética, cómo se ordena por frecuencia y energía, cómo decae con la distancia y qué la hace peligrosa?
- 🔗 **Se estudia junto con:** onda electromagnética, magnitudes, fotón, intensidad o flujo.

📘 **Dónde se aprende** (2 clases): [B05-C18 · Electromagnetismo y radiación](../programa/clases/B05/B05-C18-electromagnetismo-y-radiacion/CLASE.md); [B06-C18 · Fotoquímica y radiación](../programa/clases/B06/B06-C18-fotoquimica-y-radiacion/CLASE.md).

### No ligada

- Una órbita ligada se cierra; una no ligada (parabólica o hiperbólica) no.

💡 **Cómo se explica en la clase [B04-C18](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md):**
- B -. "ligada: se cierra" .-> E["Vuelve"]
- *Descripción textual:* una sola ecuación da cuatro curvas según la excentricidad: circunferencia (0), elipse (entre 0 y 1, con semieje positivo), parábola (1, semieje infinito) e hipérbola (mayor que 1, semieje negativo, con asíntotas a `arccos(−1/e)`); las dos primeras son ligadas y las otras dos no.
- 🎯 **Por qué importa:** En 2017 se descubrió un objeto que cruzaba el sistema solar con una órbita que no se cerraba: su excentricidad era mayor que 1. Eso significó que no estaba ligado al Sol: venía de fuera y se iba.
- 🔗 **Se estudia junto con:** cónica, propiedad foco–directriz, foco, directriz.

📘 **Dónde se aprende** (1 clase): [B04-C18 · Cónicas y secciones orbitales](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md).

### No lineal

- En un modelo no lineal se itera (por ejemplo, Levenberg–Marquardt, el método por defecto de `curve_fit`, S2).

💡 **Cómo se explica en la clase [B15-C16](../programa/clases/B15/B15-C16-ajuste-de-curvas/CLASE.md):**
- Para `y = b₁(1 − e^{−b₂x})`, que no es lineal en `b₂`, se parte de valores iniciales y se itera.
- El intervalo `±1 sd` contiene el valor verdadero el `65,3 %` de las veces para `b₁` y el `65,9 %` para `b₂`, algo menos que el `68,3 %` del caso lineal ideal: la covarianza de un ajuste no lineal con 14 puntos es aproximada.
- ⚠️ **Error frecuente:** Creer que la covarianza es exacta en un modelo no lineal. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** En C01 una recta ajustada a 2,8 periodos de una oscilación dio una pendiente de −2,24 × 10⁻⁴ por día cuando la real era −1,00 × 10⁻⁴: el modelo estaba mal planteado.
- 🔗 **Se estudia junto con:** modelo, parámetros, residuo, Mínimos cuadrados.

📘 **Dónde se aprende** (1 clase): [B15-C16 · Ajuste de curvas](../programa/clases/B15/B15-C16-ajuste-de-curvas/CLASE.md).

### No lineal en parámetros

- Un modelo no lineal en parámetros (como `P₀e^{−kt}`) se ajusta por iteración (Gauss–Newton y variantes).

💡 **Cómo se explica en la clase [B12-C10](../programa/clases/B12/B12-C10-regresion-lineal-y-no-lineal/CLASE.md):**
- Ajustar un modelo no lineal en parámetros con un método iterativo y compararlo con la linealización.
- 🎯 **Por qué importa:** Casi todo en ciencias espaciales es un ajuste: la deriva de un oscilador, la curva de luz de un tránsito, la degradación de una celda solar, la relación período–luminosidad. Un ajuste sin incertidumbre de parámetros ni diagnóstico de residuos es sólo una línea dibujada.
- 🔗 **Se estudia junto con:** modelo lineal en los parámetros, Mínimos cuadrados ordinarios, ecuaciones normales, residuo.

📘 **Dónde se aprende** (1 clase): [B12-C10 · Regresión lineal y no lineal](../programa/clases/B12/B12-C10-regresion-lineal-y-no-lineal/CLASE.md).

### No linealidad

- La no linealidad sesga la media de `ρ`.
- La no linealidad de `T⁴` hace que `<T⁴> > <T>⁴`.

💡 **Cómo se explica en la clase [B29-C10](../programa/clases/B29/B29-C10-masas-y-radios-planetarios/CLASE.md):**
- La media sube `2,8 %` por la no linealidad.
- Descripción larga: con errores grandes el Monte Carlo supera ligeramente a la propagación lineal por la no linealidad de `R⁻³`.
- 🎯 **Por qué importa:** Una densidad con 28 % de incertidumbre no distingue una roca de un mundo con agua. Saber de qué medida depende el error orienta la inversión de observación.
- 🔗 **Se estudia junto con:** densidad media, gravedad superficial, velocidad de escape, propagación lineal.

📘 **Dónde se aprende** (2 clases): [B29-C10 · Masas y radios planetarios](../programa/clases/B29/B29-C10-masas-y-radios-planetarios/CLASE.md); [B32-C07 · Modelos de atmósferas estelares 1D y 3D hidrodinámicos](../programa/clases/B32/B32-C07-modelos-de-atmosferas-estelares-1d-y-3d-hidrodinamicos/CLASE.md).

### No ociosa

- Una disciplina no ociosa nunca deja capacidad sin usar si hay cola.

💡 **Cómo se explica en la clase [B94-C05](../programa/clases/B94/B94-C05-calidad-de-servicio-y-prioridades-en-redes-espaciales/CLASE.md):**
- Quedaría capacidad ociosa al final de cada contacto, el total entregado bajaría y las comparaciones entre políticas se complicarían.
- 🎯 **Por qué importa:** Si la demanda supera a la capacidad, alguien espera. La decisión central: ¿qué política de cola garantiza lo urgente sin dejar sin servicio a las demás clases, y a qué coste?
- 🔗 **Se estudia junto con:** clase de servicio, FIFO, Prioridad estricta, reparto ponderado.

📘 **Dónde se aprende** (1 clase): [B94-C05 · Calidad de servicio y prioridades en redes espaciales](../programa/clases/B94/B94-C05-calidad-de-servicio-y-prioridades-en-redes-espaciales/CLASE.md).

### No paralizable

- Un detector no paralizable ignora los fotones que llegan durante `τ`; uno paralizable reinicia `τ` con cada fotón.

💡 **Cómo se explica en la clase [B92-C05](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md):**
- Con `τ = 20 ns`: una tasa incidente de `10 Mcps` se mide como `8,333 Mcps` (no paralizable) o `8,187` (paralizable); a `50 Mcps`, `25,0` o `18,4`; a `200 Mcps`, `40,0` o `3,66`.
- El detector paralizable se bloquea con tasas altas.
- 🎯 **Por qué importa:** Un detector de imagen integra luz durante milisegundos; uno de comunicaciones decide, en nanosegundos, en qué ranura llegó el pulso. La decisión central: ¿cuántos fotones hacen falta por símbolo y qué detector soporta la tasa de ranuras sin saturarse?
- 🔗 **Se estudia junto con:** detección directa, conteo de fotones, eficiencia de detección, conteos oscuros.

📘 **Dónde se aprende** (1 clase): [B92-C05 · Receptores y detectores para comunicaciones ópticas](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md).

### No perpendicularidad de ejes

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B49-C03](../programa/clases/B49/B49-C03-apuntamiento-y-seguimiento-de-radiotelescopios-modelos-de-apuntado-y-errores/CLASE.md):**
- **Idea central (modelo mental):** Como corregir una brújula con una tabla de desvíos: se mide hacia puntos conocidos y se ajustan las correcciones.
- 🎯 **Por qué importa:** Con un haz estrecho, un error de apuntado pequeño pierde ganancia. La decisión central: ¿qué términos modelar, y cuánto error residual queda frente al ancho del haz?
- 🔗 **Se estudia junto con:** desplazamiento de cero, colimación, inclinación del eje de azimut, flexión gravitatoria.

📘 **Dónde se aprende** (1 clase): [B49-C03 · Apuntamiento y seguimiento de radiotelescopios: modelos de apuntado y errores](../programa/clases/B49/B49-C03-apuntamiento-y-seguimiento-de-radiotelescopios-modelos-de-apuntado-y-errores/CLASE.md).

### No restringida

- La categoría V se añade a las misiones que traen muestras a la Tierra; es restringida o no restringida.

💡 **Contexto en la clase [B56-C18](../programa/clases/B56/B56-C18-proteccion-planetaria-cospar/CLASE.md):**
- **Idea central (modelo mental):** Primero, el tipo de cuerpo; luego, el tipo de misión; la categoría sale de la combinación. ```mermaid flowchart TD A["Cuerpo"] --> B{"Grupo"} B -- "I (p. ej.
- 🎯 **Por qué importa:** La política protege los otros mundos de la contaminación (para no estropear la búsqueda de vida) y la Tierra del material devuelto. Saber en qué categoría cae una misión determina su documentación, su limpieza y sus restricciones.
- 🔗 **Se estudia junto con:** categoría, categoría V, restringida, mundo helado.

📘 **Dónde se aprende** (1 clase): [B56-C18 · Protección planetaria COSPAR](../programa/clases/B56/B56-C18-proteccion-planetaria-cospar/CLASE.md).

### No unicidad

- La no unicidad significa que distintas fuentes producen la misma señal.
- La no unicidad es que varios modelos reproduzcan los mismos datos.
- La no unicidad con pocas vistas.

💡 **Cómo se explica en la clase [B53-C28](../programa/clases/B53/B53-C28-inversion-gravimetrica-y-modelos-de-densidad/CLASE.md):**
- Explicar la no unicidad de la inversión.
- ⚠️ **Error frecuente:** Ignorar la no unicidad. se corrige con 8,4
- 🎯 **Por qué importa:** La gravedad mide masa, no densidad ni forma. La decisión central: ¿qué profundidad y qué masa anómala son compatibles con una anomalía y qué cosas no se pueden distinguir?
- 🔗 **Se estudia junto con:** degeneración.

📘 **Dónde se aprende** (3 clases): [B34-C06 · Tomografía coronal](../programa/clases/B34/B34-C06-tomografia-coronal/CLASE.md); [B53-C28 · Inversión gravimétrica y modelos de densidad](../programa/clases/B53/B53-C28-inversion-gravimetrica-y-modelos-de-densidad/CLASE.md); [B65-C05 · Inversión geofísica conjunta: validación de modelos interiores](../programa/clases/B65/B65-C05-inversion-geofisica-conjunta-validacion-de-modelos-interiores/CLASE.md).

### No uniformidad de respuesta

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B47-C15](../programa/clases/B47/B47-C15-calibracion-a-bordo/CLASE.md):**
- **Idea central (modelo mental):** Es calibrar una balanza sin pesas patrón: mides el azar de las lecturas y, como el azar de contar fotones es conocido, de ahí se deduce cuánto pesa cada cuenta.
- 🎯 **Por qué importa:** Sin ganancia ni ruido calibrados no se puede convertir cuentas en fotones ni dar incertidumbres. La decisión central: ¿cómo se obtiene la ganancia sin conocerla y cuánto residuo deja la corrección de campo plano?
- 🔗 **Se estudia junto con:** curva de transferencia de fotones, ganancia, ruido de lectura, campo plano.

📘 **Dónde se aprende** (1 clase): [B47-C15 · Calibración a bordo](../programa/clases/B47/B47-C15-calibracion-a-bordo/CLASE.md).

### No uniformidad residual

- La no uniformidad residual es la dispersión relativa tras corregir.

💡 **Cómo se explica en la clase [B44-C14](../programa/clases/B44/B44-C14-calibracion-con-flat/CLASE.md):**
- Con una respuesta de `3,77 %` de dispersión (PRNU de `1,5 %` y viñeteo de `15 %`) y `20 000 e⁻` por píxel, un flat de `80` cuadros deja una no uniformidad residual de `0,00738`, frente a `0,0386` sin flat.
- El script [flat.py](flat.py) construye maestros de flat de 5, 20 y 80 cuadros y mide la no uniformidad residual (comprueba el residuo frente al analítico al 4 % y que el flat reduce la no uniformidad al menos 4 veces).
- 🎯 **Por qué importa:** Los píxeles no responden igual y el campo se oscurece hacia el borde. La decisión central: ¿cuántos flats hacen falta para que el ruido del flat no domine?
- 🔗 **Se estudia junto con:** flat, PRNU, viñeteo, normalización.

📘 **Dónde se aprende** (1 clase): [B44-C14 · Calibración con flat](../programa/clases/B44/B44-C14-calibracion-con-flat/CLASE.md).

### No usa ninguno

- Un esquema es el documento que dice qué etiquetas XML son válidas; este laboratorio no usa ninguno.

💡 **Contexto en la clase [B14-C21](../programa/clases/B14/B14-C21-datos-de-misiones-planetarias-pds4-etiquetas-y-spice/CLASE.md):**
- **Idea central (modelo mental):** Los datos sin su descripción no se pueden leer; la descripción sin los datos no sirve. Se comprueba que ambas concuerdan antes de usar nada: el tamaño declarado, el tamaño real y el tamaño que sale de forma y tipo deben coincidir.
- 🎯 **Por qué importa:** Un archivo binario de una sonda planetaria son bytes sin significado: ¿cuántas filas?, ¿enteros o reales?, ¿qué orden de bytes?, ¿qué número indica «no hay dato»?, ¿qué unidad? Y para interpretarlo, hace falta saber dónde estaba la nave y hacia dónde apuntaba.
- 🔗 **Se estudia junto con:** producto, etiqueta, orden de bytes, valor especial.

📘 **Dónde se aprende** (1 clase): [B14-C21 · Datos de misiones planetarias: PDS4, etiquetas y SPICE](../programa/clases/B14/B14-C21-datos-de-misiones-planetarias-pds4-etiquetas-y-spice/CLASE.md).

### Noche astronómica

- La noche astronómica es el período con el Sol a más de 18° bajo el horizonte (S4).

💡 **Cómo se explica en la clase [B08-C12](../programa/clases/B08/B08-C12-limitacion-por-contaminacion-luminica/CLASE.md):**
- Con la posición de la Luna y la del Sol se calcula cuántas horas de noche astronómica transcurren con la Luna bajo el horizonte.
- Con las posiciones de la NASA (S1) y el programa de la sección 17 obtienes: la noche astronómica del 5 al 6 dura 7,67 h (de las 00:37 a las 08:17 UT), pero la Luna, ~99 % iluminada, está sobre el horizonte las 7,67 h completas: 0 horas de cielo oscuro sin Luna.
- 🎯 **Por qué importa:** La mayoría de las personas ya no ve la Vía Láctea desde su casa. La pregunta motivadora: ¿qué tan oscuro es mi cielo, cuánto de eso es culpa de la Luna y cuánto de las luces, y qué puedo hacer?
- 🔗 **Se estudia junto con:** contaminación lumínica, brillo del cielo, magnitud límite, adaptación a la oscuridad.

📘 **Dónde se aprende** (1 clase): [B08-C12 · Limitación por contaminación lumínica](../programa/clases/B08/B08-C12-limitacion-por-contaminacion-luminica/CLASE.md).

### Noche local

- La noche local es el intervalo de horas solares oscuras.

💡 **Cómo se explica en la clase [B28-C16](../programa/clases/B28/B28-C16-redes-internacionales-de-alertas/CLASE.md):**
- *Descripción textual:* el tiempo sidéreo local y la ascensión recta dan el ángulo horario; con él, la altura; combinada con la noche local da la probabilidad por sitio, y la de la red se compara con la fórmula de independencia.
- Se exige altura `> 30°` y noche entre las `20` y las `4` horas solares locales.
- ⚠️ **Error frecuente:** Olvidar la noche local. Se corrige con el ejemplo 13.
- 🎯 **Por qué importa:** La cobertura de una red depende de su distribución geográfica, no solo del número de telescopios. La decisión central: ¿qué probabilidad hay de que, al llegar una alerta, al menos un sitio de la red pueda observar la fuente?
- 🔗 **Se estudia junto con:** red, altura, disponibilidad, probabilidad de la red.

📘 **Dónde se aprende** (1 clase): [B28-C16 · Redes internacionales de alertas](../programa/clases/B28/B28-C16-redes-internacionales-de-alertas/CLASE.md).

### Noche lunar

- La noche lunar es el periodo sin Sol en un punto de la superficie.
- Noche lunar: mitad del mes sinodico sin Sol (en un sitio ecuatorial sin sombras).

💡 **Cómo se explica en la clase [B86-C22](../programa/clases/B86/B86-C22-suministro-de-energia-durante-la-noche-lunar/CLASE.md):**
- La noche lunar equivale a `354,4 h` (`14,77 días`).
- Calcular la duración de la noche lunar desde el periodo sinódico y la energía de supervivencia.
- 🎯 **Por qué importa:** Una batería dimensionada para un eclipse orbital no sirve para una noche lunar: la energía crece unas doscientas veces y la masa de la batería deja de ser razonable. Por eso la estrategia cambia de almacenar a generar de otra manera.
- 🔗 **Se estudia junto con:** carga de supervivencia, masa de la batería, unidad, cruce.

📘 **Dónde se aprende** (2 clases): [B86-C22 · Suministro de energía durante la noche lunar](../programa/clases/B86/B86-C22-suministro-de-energia-durante-la-noche-lunar/CLASE.md); [B106-C19 · Arquitectura de asentamiento lunar conceptual](../programa/clases/B106/B106-C19-arquitectura-de-asentamiento-lunar-conceptual/CLASE.md).

### Nodo

- Una estación de eclipses es el período en que la órbita de la Luna cruza el plano de la órbita de la Tierra; ocurre dos veces al año (S3). Nodo es cada uno de los dos puntos en que la órbita lunar cruza ese plano.
- Un nodo es un cruce con el plano de referencia.
- El nodo es el punto donde el plano orbital corta la eclíptica; el cambio de plano es más barato en un nodo.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B08-C09](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md):**
- Solo cuando la Luna está cerca de un nodo en luna nueva (o llena) hay eclipse (S3).
- Solo cuando está cerca de un nodo su separación del Sol cae bajo el límite.
- 🎯 **Por qué importa:** Un eclipse solar es un fenómeno que reúne a miles de personas y que puede dejar ciegas a quienes lo miran mal. La pregunta motivadora: ¿qué tipo de eclipse ocurrirá, dónde y cómo lo veo sin dañarme?
- 🔗 **Se estudia junto con:** umbra, penumbra, solar, lunar.

📘 **Dónde se aprende** (5 clases): [B08-C09 · Eclipses y geometría de sombras](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md); [B58-C05 · Órbitas cercanas a la Tierra](../programa/clases/B58/B58-C05-orbitas-cercanas-a-la-tierra/CLASE.md); [B75-C13 · Cambios de plano interplanetarios](../programa/clases/B75/B75-C13-cambios-de-plano-interplanetarios/CLASE.md); [B100-C06 · Logística cislunar: nodos, depósitos y rutas de reabastecimiento](../programa/clases/B100/B100-C06-logistica-cislunar-nodos-depositos-y-rutas-de-reabastecimiento/CLASE.md); [B118-C05 · Conjunciones orbitales](../programa/clases/B118/B118-C05-conjunciones-orbitales/CLASE.md).

### Nodo ascendente

- La inclinación `i` es el ángulo entre el plano orbital y el de referencia (de 0° a 180°); el nodo ascendente es el punto donde la órbita cruza el plano de referencia de sur a norte, y su longitud `Ω` se mide en ese plano desde la dirección de referencia.
- La línea de nodos es la intersección de dos círculos fundamentales; el nodo ascendente es el punto donde un plano cruza al otro de sur a norte.
- El nodo ascendente es el punto donde la órbita cruza el ecuador hacia el norte; su longitud es la ascensión recta del nodo ascendente (`Ω` o RAAN).

💡 **Cómo se explica en la clase [B04-C14](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md):**
- La línea de nodos, `ẑ × ĥ`, apunta a lo largo de la dirección del nodo ascendente: su ángulo desde `x` es `Ω`.
- El cometa 1P/Halley tiene, según la solución del JPL del 2025-11-21, una inclinación orbital `i = 162,19°` y una longitud del nodo ascendente `Ω = 59,10°` (S1; estimados, archivo mutable).
- 🎯 **Por qué importa:** Una órbita no es solo una forma (C09): es una forma colocada en el espacio con una orientación. ¿Hacia dónde apunta su plano?
- 🔗 **Se estudia junto con:** producto vectorial, regla de la mano derecha, anticonmutativo, normal a un plano.

📘 **Dónde se aprende** (3 clases): [B04-C14 · Producto vectorial y orientación](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md); [B04-C19 · Transformaciones de coordenadas astronómicas](../programa/clases/B04/B04-C19-transformaciones-de-coordenadas-astronomicas/CLASE.md); [B71-C11 · Inclinación y nodo ascendente](../programa/clases/B71/B71-C11-inclinacion-y-nodo-ascendente/CLASE.md).

### Nodo concentrado

- Nodo concentrado: modelo de una sola temperatura.

💡 **Cómo se explica en la clase [B90-C11](../programa/clases/B90/B90-C11-ensayos-termicos/CLASE.md):**
- Plantear la ecuación de un nodo térmico concentrado y calcular su constante de tiempo.
- 🎯 **Por qué importa:** Una prueba funcional hecha antes de que la unidad se estabilice no demuestra nada sobre la temperatura extrema; una espera excesiva consume cámara y calendario. La decisión central: ¿cuánto debe esperar el ensayo para que la temperatura de la unidad sea la de la prueba?
- 🔗 **Se estudia junto con:** Constante de tiempo τ, Rampa, tiempo a temperatura constante, estado donde la unidad ya no cambia apreciablemente.

📘 **Dónde se aprende** (1 clase): [B90-C11 · Ensayos térmicos](../programa/clases/B90/B90-C11-ensayos-termicos/CLASE.md).

### Nodo fantasma

- El nodo fantasma es un punto ficticio fuera del dominio que permite imponer Neumann con orden 2: `T_{N+1} = T_{N−1} + 2Δz·g`.

💡 **Cómo se explica en la clase [B23-C04](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md):**
- Frontera de Neumann de primer orden (usar `T_N' ≈ (T_N − T_{N−1})/Δz` en vez del nodo fantasma): el orden espacial cae a 0,90; 0,95; 0,98; 0,99 (≈ 1).
- Escribir el esquema. Con el nodo fantasma, la última ecuación es `dT_N/dt = 2κ(T_{N−1} − T_N)/Δz² + 2κ g/Δz + s_N`.
- 🎯 **Por qué importa:** Un modelo de conducción de calor en el regolito, con una fuente variable y una condición de flujo en el borde, no tiene solución cerrada. Pero su código puede estar mal en la frontera, en el término fuente o en el tiempo, y ninguna propiedad global lo delata fácilmente.
- 🔗 **Se estudia junto con:** solución fabricada, término fuente, condiciones de frontera, estudio de refinamiento.

📘 **Dónde se aprende** (1 clase): [B23-C04 · Soluciones de referencia y manufactured solutions](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md).

### Nodos de Chebyshev–Gauss–Lobatto

- Los nodos de Chebyshev–Gauss–Lobatto son `x_j = cos(π j/N)`, `j = 0…N`, con `N + 1` puntos que se agrupan hacia los extremos.

💡 **Contexto en la clase [B11-C24](../programa/clases/B11/B11-C24-metodos-espectrales-avanzados-chebyshev-y-fourier/CLASE.md):**
- **Idea central (modelo mental):** Cerca de los bordes un polinomio de grado alto oscila más; Chebyshev pone más nodos allí, y el error deja de crecer (la solución de Runge, C18). La derivada es exacta para todo polinomio hasta el grado de la malla, y las funciones analíticas se aproximan con coeficientes que decaen geométricamente.
- 🎯 **Por qué importa:** Cuando la solución es suave, un método espectral reduce un problema que necesita miles de puntos con diferencias a una docena con Chebyshev. Pero tiene un costo: el paso máximo estable de un esquema explícito baja como `1/N⁴`, y funciona mal si la solución no es suave.
- 🔗 **Se estudia junto con:** matriz de diferenciación, colocación, condicionamiento, convergencia exponencial.

📘 **Dónde se aprende** (1 clase): [B11-C24 · Métodos espectrales avanzados (Chebyshev y Fourier)](../programa/clases/B11/B11-C24-metodos-espectrales-avanzados-chebyshev-y-fourier/CLASE.md).

### Nodos equiespaciados

- Los nodos equiespaciados están a igual distancia; los de Chebyshev son `cos(π(2i + 1)/(2(n + 1)))` y se acumulan hacia los extremos.

💡 **Cómo se explica en la clase [B11-C18](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md):**
- En el laboratorio, con nodos equiespaciados en `[0, 2π]`: `n = 4`: error `0,181` (cota `0,289`);
- Para `1/(1 + 25 x²)` en `[−1, 1]`, el error máximo con nodos equiespaciados crece con el grado: `0,44` (n = 4), `1,05` (8), `3,66` (12), `14,4` (16), `59,8` (20).
- ⚠️ **Error frecuente:** Subir el grado con nodos equiespaciados. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Si una nave debe saber dónde está un cuerpo en un instante que no figura en la tabla, interpola. Si interpola con un grado equivocado o fuera del rango, el error puede pasar de metros a miles de kilómetros sin que el programa avise.
- 🔗 **Se estudia junto con:** polinomio de Lagrange, polinomio nodal, error, Interpolar.

📘 **Dónde se aprende** (1 clase): [B11-C18 · Interpolación y extrapolación](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md).

### Nombre propio

- Un nombre propio es un nombre de uso tradicional; una designación es un código sistemático.

💡 **Cómo se explica en la clase [B08-C06](../programa/clases/B08/B08-C06-constelaciones-y-catalogos-estelares/CLASE.md):**
- ESO la clasifica oficialmente como la constelación Crux, «la Cruz del Sur», y la presenta como una marca útil para identificar el polo sur celeste (S4); un colega te dice «mira esa estrella» y la nombra con un nombre propio tradicional, y un programa de telescopio acepta solo identificadores de catálogo.
- Interpretar el formato de una designación (nombre propio, letra griega, número de catálogo).
- 🎯 **Por qué importa:** Dos personas dicen «la estrella roja de la Cruz del Sur» y creen hablar de lo mismo; un programa de telescopio pide «HIP 12345». Sin un lenguaje común no puedes repetir una observación ni compartirla.
- 🔗 **Se estudia junto con:** constelación, asterismo, catálogo, identificador.

📘 **Dónde se aprende** (1 clase): [B08-C06 · Constelaciones y catálogos estelares](../programa/clases/B08/B08-C06-constelaciones-y-catalogos-estelares/CLASE.md).

### Nominal

- Una constante es un valor que no cambia: exacta por definición (como `c = 299 792 458 m/s` en el SI, S4), medida (como `G`, con incertidumbre) o nominal (valor de conversión fijado por acuerdo, como el `(GM)☉` de la IAU).
- La tasa real excluye la inflación y la nominal la incluye; se relacionan por `1 + nominal = (1 + real)(1 + π)` (relación de Fisher).

💡 **Cómo se explica en la clase [B03-C12](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md):**
- Para evitar que cada publicación use un valor distinto, la IAU adopta «valores nominales» exactos para convertir unidades solares y planetarias: `R☉ᴺ = 6,957 × 10⁸ m`, `S☉ᴺ = 1361 W m⁻²`, `L☉ᴺ = 3,828 × 10²⁶ W`, `(GM)☉ᴺ = 1,3271244 × 10²⁰ m³ s⁻²` (S1).
- P -->|Universal| K{"¿Exacto, medido o nominal?"}
- ⚠️ **Error frecuente:** Tratar un valor nominal como la mejor estimación. Sección 14.
- 🎯 **Por qué importa:** La masa del Sol se conoce con unas cinco cifras. Sin embargo, el producto `GM` del Sol se conoce con diez, y la constante `G` por sí sola con apenas cinco.
- 🔗 **Se estudia junto con:** variable, parámetro, constante, exacta por definición.

📘 **Dónde se aprende** (2 clases): [B03-C12 · Variables y constantes científicas](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md); [B126-C05 · Evaluación de viabilidad económica de un negocio espacial](../programa/clases/B126/B126-C05-evaluacion-de-viabilidad-economica-de-un-negocio-espacial/CLASE.md).

### Norma

- La norma es `‖u‖ = √⟨u, u⟩`.

💡 **Cómo se explica en la clase [B10-C06](../programa/clases/B10/B10-C06-producto-interno-y-ortogonalidad/CLASE.md):**
- Si `u ⟂ v`, `‖u + v‖² = ‖u‖² + ‖v‖²`: con `(3, 0, 0)` y `(0, 4, 0)` la suma tiene norma `5`.
- `ã₂ = (1, 0, 1) − 0,7071·q₁ = (0,5; −0,5; 1)`, de norma `√1,5 = 1,2247`;
- 🎯 **Por qué importa:** La potencia que recibe un panel solar depende del ángulo entre su normal y la dirección al Sol: más inclinado, menos luz. El control de actitud, la orientación de antenas y de instrumentos usan el mismo cálculo.
- 🔗 **Se estudia junto con:** producto interno, ortogonales, vector unitario, ortonormal.

📘 **Dónde se aprende** (1 clase): [B10-C06 · Producto interno y ortogonalidad](../programa/clases/B10/B10-C06-producto-interno-y-ortogonalidad/CLASE.md).

### Norma 2

- La norma 2 es `σ₁`.

💡 **Cómo se explica en la clase [B10-C11](../programa/clases/B10/B10-C11-valores-singulares-y-svd/CLASE.md):**
- El teorema de Eckart–Young (resultado estándar sin cita específica aquí) dice que la mejor aproximación de rango `k` en norma 2 tiene error exactamente `σ_{k+1}`, y en norma de Frobenius `√(Σ_{i>k} σᵢ²)`.
- Con `k = 3` el error en norma 2 es `0,0115` (= `σ₄`) y en Frobenius `0,0372` (el ruido restante), con un almacenamiento de `k(m + n + 1) = 243` números en lugar de `1600` (15 %).
- 🎯 **Por qué importa:** Un instrumento entrega una imagen de miles de píxeles; la mayor parte de su estructura se puede describir con muy pocos patrones. Una matriz de medidas puede tener columnas casi redundantes, de modo que un cálculo «técnicamente posible» sea inútil.
- 🔗 **Se estudia junto con:** SVD, valores singulares, vectores singulares izquierdos, derechos.

📘 **Dónde se aprende** (1 clase): [B10-C11 · Valores singulares y SVD](../programa/clases/B10/B10-C11-valores-singulares-y-svd/CLASE.md).

### Norma de Frobenius

- La norma de Frobenius es `‖A‖_F = √(Σ aᵢⱼ²) = √(Σ σᵢ²)`.

💡 **Cómo se explica en la clase [B10-C11](../programa/clases/B10/B10-C11-valores-singulares-y-svd/CLASE.md):**
- El teorema de Eckart–Young (resultado estándar sin cita específica aquí) dice que la mejor aproximación de rango `k` en norma 2 tiene error exactamente `σ_{k+1}`, y en norma de Frobenius `√(Σ_{i>k} σᵢ²)`.
- Con `k = 3` el error en norma 2 es `0,0115` (= `σ₄`) y en Frobenius `0,0372` (el ruido restante), con un almacenamiento de `k(m + n + 1) = 243` números en lugar de `1600` (15 %).
- 🎯 **Por qué importa:** Un instrumento entrega una imagen de miles de píxeles; la mayor parte de su estructura se puede describir con muy pocos patrones. Una matriz de medidas puede tener columnas casi redundantes, de modo que un cálculo «técnicamente posible» sea inútil.
- 🔗 **Se estudia junto con:** SVD, valores singulares, vectores singulares izquierdos, derechos.

📘 **Dónde se aprende** (1 clase): [B10-C11 · Valores singulares y SVD](../programa/clases/B10/B10-C11-valores-singulares-y-svd/CLASE.md).

### Norma euclídea

- La norma euclídea de un vector `v` es `‖v‖ = √(v₁² + v₂² + v₃²)`.

💡 **Contexto en la clase [B14-C02](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md):**
- **Idea central (modelo mental):** Un arreglo es un bloque contiguo de bytes más una etiqueta que dice cómo leerlo: cuántos ejes, cuánto mide cada uno y de qué tipo son los valores. Cambiar la etiqueta (por ejemplo, `reshape` o una rebanada) no mueve los bytes; cambiar el contenido sí.
- 🎯 **Por qué importa:** Una constelación de seis satélites y cinco estaciones en tierra producen treinta distancias. Un catálogo de estrellas produce millones.
- 🔗 **Se estudia junto con:** arreglo, forma, ejes, tipo.

📘 **Dónde se aprende** (1 clase): [B14-C02 · Arreglos multidimensionales NumPy](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md).

### Norma H∞

- La norma H∞ de una función `F(s)` es `‖F‖∞ = máx_ω |F(jω)|`.

💡 **Contexto en la clase [B16-C16](../programa/clases/B16/B16-C16-control-robusto-inicial/CLASE.md):**
- **Idea central (modelo mental):** Imagina un círculo alrededor del punto `−1` en el plano de Nyquist. Cuanto más cerca pasa la curva `L(jω)` del punto, más pequeño es el círculo libre y menos incertidumbre tolera el lazo. Los picos de `S` y `T` miden la cercanía: el pico de `S` es el inverso de la distancia mínima de `L` a `−1`.
- 🎯 **Por qué importa:** La inercia de un satélite cambia al desplegar paneles, consumir propergol o capturar una carga; el actuador envejece; el sensor tiene un retardo que no se conocía. El lazo diseñado con la inercia nominal debe seguir funcionando.
- 🔗 **Se estudia junto con:** incertidumbre paramétrica, incertidumbre multiplicativa, teorema de la ganancia pequeña, suficiente.

📘 **Dónde se aprende** (1 clase): [B16-C16 · Control robusto inicial](../programa/clases/B16/B16-C16-control-robusto-inicial/CLASE.md).

### Norma mineral

- La norma mineral es la mezcla de minerales ideales que reproduce una composición química.

💡 **Cómo se explica en la clase [B55-C12](../programa/clases/B55/B55-C12-geoquimica-de-meteoritos/CLASE.md):**
- Por norma mineral: acerca a lo que se ve al microscopio.
- Resolver la norma mineral con tres minerales y tres óxidos.
- 🎯 **Por qué importa:** Un meteorito se describe por su análisis químico, pero lo que interesa es qué minerales lo forman y cómo se compara con otros materiales. La decisión central: ¿qué mezcla de minerales reproduce una composición de óxidos, y qué dicen sus cocientes frente a una referencia?
- 🔗 **Se estudia junto con:** forsterita, fayalita, enstatita, Mg#.

📘 **Dónde se aprende** (1 clase): [B55-C12 · Geoquímica de meteoritos](../programa/clases/B55/B55-C12-geoquimica-de-meteoritos/CLASE.md).

### Normal

- La normal es la fuerza de contacto perpendicular a una superficie.

💡 **Cómo se explica en la clase [B05-C05](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md):**
- En un plano inclinado, un eje a lo largo de la rampa y otro perpendicular evita descomponer la normal y el rozamiento.
- Si `E < m g_n` no despega (la normal de la plataforma completa el equilibrio); si `E > m g_n`, sube con `a` positiva.
- ⚠️ **Error frecuente:** Olvidar la normal o el peso. Ejercicio 2.
- 🎯 **Por qué importa:** En un lanzamiento o en una maniobra hay varias fuerzas a la vez: gravedad, empuje, tensiones, rozamiento. La pregunta motivadora es: ¿cómo dejo de olvidar fuerzas y de contar dos veces una misma?
- 🔗 **Se estudia junto con:** diagrama de cuerpo libre (DCL), peso, tensión, empuje.

📘 **Dónde se aprende** (2 clases): [B05-C05 · Diagramas de cuerpo libre](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md); [B41-C03 · Reflexión y espejos planos](../programa/clases/B41/B41-C03-reflexion-y-espejos-planos/CLASE.md).

### Normal a un plano

- La normal a un plano es un vector perpendicular a él; su versión de módulo 1 es la normal unitaria.

💡 **Cómo se explica en la clase [B04-C14](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md):**
- Si el plano de referencia es `xy`, el vector normal a una órbita con inclinación `i` y nodo `Ω` es `ĥ = (sen i sen Ω; −sen i cos Ω; cos i)`.
- Con tres puntos del plano: `(P₂ − P₁) × (P₃ − P₁)` da la normal sin velocidades.
- 🎯 **Por qué importa:** Una órbita no es solo una forma (C09): es una forma colocada en el espacio con una orientación. ¿Hacia dónde apunta su plano?
- 🔗 **Se estudia junto con:** producto vectorial, regla de la mano derecha, anticonmutativo, normal unitaria.

📘 **Dónde se aprende** (1 clase): [B04-C14 · Producto vectorial y orientación](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md).

### Normal de movimiento

- La normal de movimiento `n` es el eje alrededor del cual la nave gira en sentido antihorario;

💡 **Cómo se explica en la clase [B82-C02](../programa/clases/B82/B82-C02-lambert-de-arco-largo/CLASE.md):**
- Definir `θ` respecto a la normal `n` del movimiento y decidir si el arco es corto o largo.
- 🎯 **Por qué importa:** Dos puntos no determinan un sentido de giro: se puede ir de `r1` a `r2` recorriendo `θ` en sentido antihorario o `2π − θ` en horario. La decisión central: ¿en qué sentido y por qué plano se ejecuta la transferencia, y cómo lo codifica el algoritmo?
- 🔗 **Se estudia junto con:** prógrada, retrógrada, tangencial.

📘 **Dónde se aprende** (1 clase): [B82-C02 · Lambert de arco largo](../programa/clases/B82/B82-C02-lambert-de-arco-largo/CLASE.md).

### Normal de referencia

- La normal de referencia es un vector que el usuario fija para romper la ambigüedad.

💡 **Cómo se explica en la clase [B82-C05](../programa/clases/B82/B82-C05-singularidades-del-problema-de-lambert/CLASE.md):**
- Tres normales de referencia dan tres soluciones con el mismo `|v1| = 32,7391 km/s` y residuo `4 × 10⁻¹⁶ UA`: la elección es del diseñador (por ejemplo, la normal de la órbita de la nave).
- *Descripción textual:* si `|r1 × r2|` es grande el plano queda definido; si es casi cero el plano es indefinido y se pasa una normal de referencia; cerca de `x = 1` aparece cancelación numérica.
- ⚠️ **Error frecuente:** Ignorar la normal de referencia. Fíjala en 180° exacto (8.2)
- 🎯 **Por qué importa:** Un solucionador que funciona en 99 % de los casos puede dar una respuesta absurda en el 1 % que importa. La decisión central: ¿qué hace el problema cuando la geometría es degenerada y cómo se protege el cálculo?
- 🔗 **Se estudia junto con:** singularidad de 180°, cancelación, tiempo parabólico.

📘 **Dónde se aprende** (1 clase): [B82-C05 · Singularidades del problema de Lambert](../programa/clases/B82/B82-C05-singularidades-del-problema-de-lambert/CLASE.md).

### Normal estándar

- La normal estándar tiene `μ = 0`, `σ = 1` y se denota `Z`.

💡 **Cómo se explica en la clase [B12-C03](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md):**
- La normal estándar deja dentro de `±1σ`, `±2σ` y `±3σ` las probabilidades `0,682689`, `0,954500` y `0,997300`.
- 🎯 **Por qué importa:** Cada vez que un detector cuenta fotones, una nave registra impactos o un instrumento mide con ruido, el patrón de la incertidumbre se parece a uno de unos pocos moldes. Reconocer el molde permite calcular probabilidades sin construir todo desde cero y entender qué supuesto físico lo respalda.
- 🔗 **Se estudia junto con:** distribución, parámetro, distribución binomial, distribución de Poisson.

📘 **Dónde se aprende** (1 clase): [B12-C03 · Distribuciones de probabilidad](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md).

### Normal truncada

- La normal truncada da la media de los detectados.

💡 **Cómo se explica en la clase [B28-C19](../programa/clases/B28/B28-C19-limitaciones-y-sesgos-de-deteccion/CLASE.md):**
- Calcular la media de los detectados con la normal truncada.
- La coherencia de la simulación y de la fórmula de la normal truncada; no el catálogo real.
- 🎯 **Por qué importa:** Si se promedia la luminosidad de los eventos detectados sin corregir, se sobrestima la luminosidad típica de la población. El mismo razonamiento vale para las masas de fusiones de ondas gravitacionales detectadas.
- 🔗 **Se estudia junto con:** sesgo de Malmquist, función de selección, muestra limitada por flujo, módulo de distancia.

📘 **Dónde se aprende** (1 clase): [B28-C19 · Limitaciones y sesgos de detección](../programa/clases/B28/B28-C19-limitaciones-y-sesgos-de-deteccion/CLASE.md).

### Normal unitaria

- La normal a un plano es un vector perpendicular a él; su versión de módulo 1 es la normal unitaria.

💡 **Cómo se explica en la clase [B04-C14](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md):**
- Con estos dos ángulos puedes construir la normal unitaria `ĥ = (0,2624; −0,1571; −0,9521)`.
- Calcular la normal unitaria a una órbita a partir de `i` y `Ω`.
- 🎯 **Por qué importa:** Una órbita no es solo una forma (C09): es una forma colocada en el espacio con una orientación. ¿Hacia dónde apunta su plano?
- 🔗 **Se estudia junto con:** producto vectorial, regla de la mano derecha, anticonmutativo, normal a un plano.

📘 **Dónde se aprende** (1 clase): [B04-C14 · Producto vectorial y orientación](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md).

### Normalización

- La normalización indica con qué factor se escala la transformada; por defecto, NumPy deja la directa sin escalar y escala la inversa por `1/N` (S1).
- La normalización transforma los valores a [0, 1] con `x_n = (x − lo)/(hi − lo)`, recortando lo que queda fuera;
- La normalización divide por el continuo.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C05](../programa/clases/B15/B15-C05-transformada-rapida-de-fourier/CLASE.md):**
- ⚠️ **Error frecuente:** Mezclar normalizaciones al comparar con otro programa. Se corrige con el ejercicio 7 y la sección 10.
- 🎯 **Por qué importa:** Una curva de luz de 27 días con cadencia de 2 minutos tiene 19 440 muestras. La suma directa de la DFT necesita unos 378 millones de multiplicaciones complejas; una imagen de 1024 × 1024 necesitaría muchísimas más.
- 🔗 **Se estudia junto con:** FFT, mariposa, base 2, relleno con ceros.

📘 **Dónde se aprende** (5 clases): [B15-C05 · Transformada rápida de Fourier](../programa/clases/B15/B15-C05-transformada-rapida-de-fourier/CLASE.md); [B15-C10 · Histogramas y normalización](../programa/clases/B15/B15-C10-histogramas-y-normalizacion/CLASE.md); [B32-C10 · Normalización y modelado del continuo espectral](../programa/clases/B32/B32-C10-normalizacion-y-modelado-del-continuo-espectral/CLASE.md); [B44-C14 · Calibración con flat](../programa/clases/B44/B44-C14-calibracion-con-flat/CLASE.md); [B74-C28 · Medidas de rango y Doppler para determinar la órbita](../programa/clases/B74/B74-C28-medidas-de-rango-y-doppler-para-determinar-la-orbita/CLASE.md).

### Normalización a Si

- La normalización a Si consiste en fijar el silicio como referencia común de dos conjuntos de abundancias, de modo que `A_met(Si) = A_fot(Si) = 7,51`.

💡 **Contexto en la clase [B06-C20](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md):**
- **Idea central (modelo mental):** Imagina dos termómetros independientes que miden la misma habitación: uno apunta a la luz que llega de ella (la fotosfera) y otro entra al cuarto a tomar muestras (el meteorito). Si coinciden, confías en la medida.
- 🎯 **Por qué importa:** Hay dos formas de saber de qué está hecho el Sistema Solar. Una es mirar la luz del Sol y deducir su composición; la otra es analizar en laboratorio meteoritos que conservan la composición del material con que se formó.
- 🔗 **Se estudia junto con:** meteorito, condrita, condritas carbonáceas, CI.

📘 **Dónde se aprende** (1 clase): [B06-C20 · Análisis químico introductorio de meteoritos](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md).

### Normalización del flat

- La normalización del flat a su media hace que el flujo quede en unidades de un píxel de respuesta media.

💡 **Cómo se explica en la clase [B44-C20](../programa/clases/B44/B44-C20-pipeline-inicial-de-calibracion-de-imagenes/CLASE.md):**
- La respuesta media del campo es `0,9653`; por la normalización del flat, el flujo de referencia es `40 000 × 0,9653 = 38 612,3 e⁻`.
- 🎯 **Por qué importa:** Cada paso es simple, pero el resultado depende del orden y de cada maestro. La decisión central: ¿recupera el pipeline el flujo verdadero dentro de su incertidumbre?
- 🔗 **Se estudia junto con:** pipeline, fotometría de apertura, máscara.

📘 **Dónde se aprende** (1 clase): [B44-C20 · Pipeline inicial de calibración de imágenes](../programa/clases/B44/B44-C20-pipeline-inicial-de-calibracion-de-imagenes/CLASE.md).

### Normalización min-max

- La normalización min-max lleva cada criterio a `[0, 1]` con 1 = mejor.
- La normalización min-max lleva el mejor valor a 1 y el peor a 0.
- La normalización min–max lleva cada criterio a `[0, 1]`.

💡 **Cómo se explica en la clase [B67-C01](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md):**
- D["datos por sitio"] --> N["normalización min-max"]
- Ejercicio 1 · con los pasos indicados. Normaliza la reserva de S4 (95 kt) con mín 60 y máx 200.
- 🎯 **Por qué importa:** Elegir con una sola cifra (la reserva) lleva a sitios que no se pueden explotar; elegir con una suma de unidades distintas es un error. La decisión central: ¿cuál sitio conviene, y cuánto de esa respuesta depende de los pesos que fija quien decide?
- 🔗 **Se estudia junto con:** criterio, puntaje ponderado, domina, frente de Pareto.

📘 **Dónde se aprende** (3 clases): [B67-C01 · Selección de sitios de extracción con criterios múltiples](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md); [B95-C03 · Selección y comparación de plataformas](../programa/clases/B95/B95-C03-seleccion-y-comparacion-de-plataformas/CLASE.md); [B109-C01 · Selección de emplazamiento para un asentamiento extraterrestre](../programa/clases/B109/B109-C01-seleccion-de-emplazamiento-para-un-asentamiento-extraterrestre/CLASE.md).

### Normalizada

- La mantisa `m` cumple `1 ≤ |m| < 10` en la forma normalizada; el exponente `e` es un entero.

💡 **Cómo se explica en la clase [B03-C05](../programa/clases/B03/B03-C05-notacion-cientifica-y-ordenes-de-magnitud/CLASE.md):**
- Escribir cada masa en notación científica normalizada (`7,346 × 10²² kg`, `1,9884 × 10³⁰ kg`) hace visible esa distancia de un vistazo.
- Escribir un número en notación científica normalizada y recuperarlo en notación decimal.
- 🎯 **Por qué importa:** Las fichas de la NASA publican las masas en «10²⁴ kg»: la Tierra es 5,9722, el Sol 1 988 400. Si no sabes leer ese `10²⁴`, tampoco sabrás si 1 988 400 es «un poco más» o «mucho más».
- 🔗 **Se estudia junto con:** notación científica, mantisa, exponente, orden de magnitud.

📘 **Dónde se aprende** (1 clase): [B03-C05 · Notación científica y órdenes de magnitud](../programa/clases/B03/B03-C05-notacion-cientifica-y-ordenes-de-magnitud/CLASE.md).

### Normalizar

- La forma canónica es una serialización con orden y formato fijos (claves ordenadas, sin espacios variables) para que dos registros iguales den la misma huella. Normalizar es llevar los archivos a un formato único (fin de línea LF) antes de hashearlos.
- Mg# es `Mg/(Mg+Fe)` en moles. Normalizar es dividir por una composición de referencia.

💡 **Cómo se explica en la clase [B23-C07](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md):**
- Hashear datos y código tras normalizar: `981bfbed…` y `5cb054c2…` (primeros ocho caracteres).
- Calcular el SHA-256 de un archivo con la biblioteca estándar y normalizar el fin de línea.
- ⚠️ **Error frecuente:** No normalizar el fin de línea. Se corrige con el ejercicio 2.
- 🎯 **Por qué importa:** Un informe dice «el modelo reproduce la posición con un error de 8,21 × 10⁻⁴ au». Seis meses después, nadie sabe con qué versión del código, qué archivo de datos ni qué tolerancia se calculó, y el número no se puede reproducir ni defender.
- 🔗 **Se estudia junto con:** trazabilidad, registro de procedencia, hash, SHA-256.

📘 **Dónde se aprende** (2 clases): [B23-C07 · Trazabilidad científica de resultados](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md); [B55-C12 · Geoquímica de meteoritos](../programa/clases/B55/B55-C12-geoquimica-de-meteoritos/CLASE.md).

### Normoxia

- Cociente respiratorio (RQ): mol de CO₂ por mol de O₂. Normoxia: oxígeno suficiente sin exceso.
- Presión parcial inspirada de O₂ (`PIO₂`): presión de O₂ en el aire inspirado y saturado de vapor. Normoxia: `PIO₂` de 145 a 155 mmHg.

💡 **Cómo se explica en la clase [B106-C03](../programa/clases/B106/B106-C03-composicion-atmosferica-respirable/CLASE.md):**
- Ninguna alcanza el intervalo de normoxia; el resumen consultado describe que se evalúan compromisos entre estas combinaciones.
- *Descripción textual:* una atmósfera es aceptable si cumple a la vez normoxia, diluyente mínimo y rango de presión total.
- 🎯 **Por qué importa:** El cuerpo no responde a la fracción de oxígeno sino a su presión parcial; bajar la presión total exige subir la fracción, y eso trae riesgo de incendio (C17). La decisión central: ¿qué par presión–composición da normoxia dentro de los límites consultados?
- 🔗 **Se estudia junto con:** Presión parcial inspirada de O₂ (PIO₂), Diluyente, Psia, Ebullismo.

📘 **Dónde se aprende** (2 clases): [B106-C01 · Requisitos de habitabilidad](../programa/clases/B106/B106-C01-requisitos-de-habitabilidad/CLASE.md); [B106-C03 · Composición atmosférica respirable](../programa/clases/B106/B106-C03-composicion-atmosferica-respirable/CLASE.md).

### Norte geográfico (verdadero)

- El norte geográfico (verdadero) es la dirección hacia el polo norte de rotación de la Tierra.

💡 **Cómo se explica en la clase [B08-C01](../programa/clases/B08/B08-C01-orientacion-geografica-y-puntos-cardinales/CLASE.md):**
- Definir norte geográfico (verdadero), norte magnético y declinación magnética, y explicar por qué difieren.
- 🎯 **Por qué importa:** Una persona que llega de noche a un lugar oscuro sin saber dónde está el este no sabe dónde buscar una salida de Luna, ni hacia dónde apuntar un telescopio, ni qué rumbo debe tomar si pierde el sendero. La pregunta motivadora es: ¿cómo sé hacia dónde miro, sin depender de un aparato que se puede descargar o descalibrar?
- 🔗 **Se estudia junto con:** norte magnético, declinación magnética, acimut, orto.

📘 **Dónde se aprende** (1 clase): [B08-C01 · Orientación geográfica y puntos cardinales](../programa/clases/B08/B08-C01-orientacion-geografica-y-puntos-cardinales/CLASE.md).

### Norte magnético

- El norte magnético es la dirección que indica una brújula, ligada al campo magnético terrestre; la declinación magnética es el ángulo entre ambos y varía con el lugar y con el tiempo (S2).

💡 **Cómo se explica en la clase [B08-C01](../programa/clases/B08/B08-C01-orientacion-geografica-y-puntos-cardinales/CLASE.md):**
- Definir norte geográfico (verdadero), norte magnético y declinación magnética, y explicar por qué difieren.
- Ejercicio 3 · casi autónomo. El calculador dice que en tu lugar el norte magnético queda 8° al oeste del verdadero.
- ⚠️ **Error frecuente:** Confundir norte magnético con verdadero. Se corrige con el ejercicio 3.
- 🎯 **Por qué importa:** Una persona que llega de noche a un lugar oscuro sin saber dónde está el este no sabe dónde buscar una salida de Luna, ni hacia dónde apuntar un telescopio, ni qué rumbo debe tomar si pierde el sendero. La pregunta motivadora es: ¿cómo sé hacia dónde miro, sin depender de un aparato que se puede descargar o descalibrar?
- 🔗 **Se estudia junto con:** norte geográfico (verdadero), declinación magnética, acimut, orto.

📘 **Dónde se aprende** (1 clase): [B08-C01 · Orientación geográfica y puntos cardinales](../programa/clases/B08/B08-C01-orientacion-geografica-y-puntos-cardinales/CLASE.md).

### Notación científica

- La notación científica escribe un número como `a × 10ⁿ`, con `1 ≤ a < 10`; el exponente `n` indica el orden de magnitud.
- La notación científica escribe un número como `m × 10ᵉ`.
- La notación científica escribe `m × 10ⁿ` como `mEn`; por ejemplo `5.97e24`.

💡 **Cómo se explica en la clase [B01-C02](../programa/clases/B01/B01-C02-escalas-desde-la-tierra-al-cosmos-observable/CLASE.md):**
- Expresar cualquier distancia astronómica en notación científica y convertirla entre metros, au, años luz y parsecs.
- 🎯 **Por qué importa:** Cuando alguien dice que Próxima Centauri está «a cuatro años luz» y que Andrómeda está «a dos millones y medio», es fácil oír solo «lejos» y «más lejos». Pero entre una y otra hay un factor de casi seis cien mil.
- 🔗 **Se estudia junto con:** orden de magnitud, logaritmo decimal, cociente, unidad astronómica.

📖 **Explicado a fondo:** [Notación científica y orden de magnitud](esencial/cuarta-fundamentos.md#notación-científica-y-orden-de-magnitud) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (3 clases): [B01-C02 · Escalas desde la Tierra al cosmos observable](../programa/clases/B01/B01-C02-escalas-desde-la-tierra-al-cosmos-observable/CLASE.md); [B03-C05 · Notación científica y órdenes de magnitud](../programa/clases/B03/B03-C05-notacion-cientifica-y-ordenes-de-magnitud/CLASE.md); [B07-C02 · Tipos de datos y variables](../programa/clases/B07/B07-C02-tipos-de-datos-y-variables/CLASE.md).

### Notación δ

- La notación δ expresa la desviación relativa de una razón respecto de una referencia: `δ = (R_muestra/R_ref − 1) × 1000` en ‰.

💡 **Contexto en la clase [B06-C03](../programa/clases/B06/B06-C03-isotopos-y-masa-atomica/CLASE.md):**
- **Idea central (modelo mental):** Imagina una bolsa con canicas de dos pesos casi iguales, mezcladas siempre en la misma proporción. Si pesas muchas, el peso medio de una canica depende del peso de cada tipo y de su proporción. Eso es la masa atómica de las tablas: un promedio ponderado.
- 🎯 **Por qué importa:** El carbono del Sol, ¿es igual que el de la Tierra? Una forma de preguntarlo con rigor es comparar cuántos átomos de carbono-12 hay por cada uno de carbono-13.
- 🔗 **Se estudia junto con:** nucleón, número másico, isótopos, masa atómica relativa.

📘 **Dónde se aprende** (1 clase): [B06-C03 · Isótopos y masa atómica](../programa/clases/B06/B06-C03-isotopos-y-masa-atomica/CLASE.md).

### Notificación

- La notificación es el aviso a la autoridad de lanzamiento y al Secretario General de la ONU.
- La notificación es el envío de las características de una asignación para su registro.
- La notificación se emite cuando se superan los umbrales de probabilidad y tamaño.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B58-C18](../programa/clases/B58/B58-C18-marco-internacional-de-defensa-planetaria/CLASE.md):**
- *Descripción textual:* la regla de notificación filtra el catálogo; el tiempo mínimo que exige un `Δv` se compara con el aviso de cada objeto notificado.
- La regla de [S7] (probabilidad mayor que 1 % para más de 10 m) notifica 577 (`2.89 %`), frente a `3.08 %` esperado.
- 🎯 **Por qué importa:** Un umbral de notificación decide cuántos casos entran en el circuito internacional y cuántos tienen tiempo suficiente. La decisión central: ¿qué umbral activa la alerta y qué margen de tiempo deja para actuar?
- 🔗 **Se estudia junto con:** IAWN, SMPAG, tiempo de aviso.

📘 **Dónde se aprende** (5 clases): [B58-C18 · Marco internacional de defensa planetaria](../programa/clases/B58/B58-C18-marco-internacional-de-defensa-planetaria/CLASE.md); [B119-C02 · Acuerdo de Salvamento](../programa/clases/B119/B119-C02-acuerdo-de-salvamento/CLASE.md); [B119-C09 · Derecho y normas de telecomunicaciones](../programa/clases/B119/B119-C09-derecho-y-normas-de-telecomunicaciones/CLASE.md); [B120-C01 · Licencias satelitales y procedimiento de notificación](../programa/clases/B120/B120-C01-licencias-satelitales-y-procedimiento-de-notificacion/CLASE.md); [B122-C08 · Comunicación de crisis con operadores, autoridades y público](../programa/clases/B122/B122-C08-comunicacion-de-crisis-con-operadores-autoridades-y-publico/CLASE.md).

### NPAE

- Los términos del modelo: IA y IE (ceros de acimut y altura), CA (colimación), NPAE (no perpendicularidad de ejes), AN y AW (inclinación del eje vertical al norte y al oeste) y TF (flexión del tubo).

💡 **Cómo se explica en la clase [B43-C26](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md):**
- Los errores formales más grandes son los de `CA` y `NPAE`, que están más correlacionados con otros términos.
- Montura sintética con `IA = 120"`, `IE = −80"`, `CA = 45"`, `NPAE = 20"`, `AN = 30"`, `AW = −25"` y `TF = 15"`, con 60 estrellas y ruido gaussiano de `1"` (el ruido realmente inyectado resulta de `1,162"` con la semilla).
- 🎯 **Por qué importa:** El modelo convierte errores de decenas de segundos de arco en residuos de segundos de arco. La decisión central: ¿qué términos incluir, cuántas estrellas medir y con qué incertidumbre se determina cada parámetro?
- 🔗 **Se estudia junto con:** términos, IA, IE, CA.

📘 **Dónde se aprende** (1 clase): [B43-C26 · Modelo de flexiones y de apuntado de una montura](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md).

### NRHO

- La NRHO es la parte casi rectilínea de la familia halo.

💡 **Cómo se explica en la clase [B76-C05](../programa/clases/B76/B76-C05-orbitas-nrho/CLASE.md):**
- La evidencia es la ficha de una NRHO en el modelo CR3BP del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de una NRHO en el modelo CR3BP*: estado inicial, periodo, radios, resonancia, monodromia y comparación con la referencia publicada, con fuentes.
- ⚠️ **Error frecuente:** Presentar la NRHO del CR3BP como la de Gateway. Se corrige con 8.5.
- 🎯 **Por qué importa:** La NRHO es la órbita de referencia publicada para la estación Gateway. La decisión central: ¿cómo se calcula una órbita periódica inestable y qué tan cerca queda un modelo simple de la referencia en un modelo de efemérides?
- 🔗 **Se estudia junto con:** perilune, apolune, corrección diferencial, monodromia.

📘 **Dónde se aprende** (1 clase): [B76-C05 · Órbitas NRHO](../programa/clases/B76/B76-C05-orbitas-nrho/CLASE.md).

### N·s

- lbf·s: libra-fuerza por segundo (impulso). N·s: newton por segundo.

💡 **Cómo se explica en la clase [B96-C19](../programa/clases/B96/B96-C19-lecciones-aprendidas-operativas/CLASE.md):**
- Con conversión explícita, 2 N·s + 2 N·s = 4 N·s.
- Una prueba de aceptación convierte lo entregado a N·s y lo compara con lo esperado: acepta `0,4496 lbf·s` y rechaza `0,4496` declarado como N·s.
- 🎯 **Por qué importa:** Un número sin unidad es una trampa: el programa corre, el valor parece razonable y la nave se pierde. La decisión central: ¿cómo se evita que una conversión de unidades pase inadvertida entre el software de tierra y el de vuelo?
- 🔗 **Se estudia junto con:** Lección aprendida, lbf·s, Interfaz, Tipo con unidad.

📘 **Dónde se aprende** (1 clase): [B96-C19 · Lecciones aprendidas operativas](../programa/clases/B96/B96-C19-lecciones-aprendidas-operativas/CLASE.md).

### NSPM-20

- NSPM-20 es la memoria presidencial de 2019 que fija el proceso de autorización de lanzamientos con sistemas nucleares espaciales.

💡 **Cómo se explica en la clase [B86-C18](../programa/clases/B86/B86-C18-seguridad-y-licenciamiento-energetico/CLASE.md):**
- La memoria presidencial NSPM-20 (2019) fija tres niveles de autorización de lanzamiento.
- Es el ejemplo conductor: la estructura de niveles es de NSPM-20 y los números dependen de un `A2` que no se consultó.
- 🎯 **Por qué importa:** Los límites de la energía nuclear en el espacio son tanto jurídicos y de seguridad como técnicos: quién aprueba, con qué análisis y con qué umbrales. Un ingeniero de potencia debe saber que estas decisiones existen y qué datos las gobiernan.
- 🔗 **Se estudia junto con:** niveles I, II y III, A2, TED, LEU.

📘 **Dónde se aprende** (1 clase): [B86-C18 · Seguridad y licenciamiento energético](../programa/clases/B86/B86-C18-seguridad-y-licenciamiento-energetico/CLASE.md).

### Nube de Oort

- La nube de Oort es el reservorio hipotético de cometas a decenas de miles de ua.

💡 **Cómo se explica en la clase [B52-C16](../programa/clases/B52/B52-C16-nube-de-oort/CLASE.md):**
- La evidencia es la ficha de las perturbaciones de la nube de Oort del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Integrador. Elabora tu *ficha de las perturbaciones de la nube de Oort*: cometa, impulso, integración y límites.
- 🎯 **Por qué importa:** Las perturbaciones estelares explican cómo cometas casi circulares en la nube pasan a órbitas que cruzan el Sistema Solar interior. La decisión central: ¿cuánto cambia la velocidad de un cometa de la nube con el paso de una estrella y qué efecto tiene en su perihelio?
- 🔗 **Se estudia junto con:** aproximación impulsiva, término indirecto, perihelio.

📖 **Explicado a fondo:** [Cinturón de Kuiper y nube de Oort](esencial/tercera-a-e.md#cinturón-de-kuiper-y-nube-de-oort) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B52-C16 · Nube de Oort](../programa/clases/B52/B52-C16-nube-de-oort/CLASE.md).

### Nube de puntos

- Una nube de puntos es un conjunto de posiciones 3D.

💡 **Cómo se explica en la clase [B57-C30](../programa/clases/B57/B57-C30-nubes-de-puntos-tridimensionales/CLASE.md):**
- La nube sintética tiene `27500` puntos en 1 ha (`2,75 puntos/m²`).
- Sobre toda la nube, sin filtrar, el error máximo es `0,0002`: aquí el suelo es el 73 % de los puntos y RANSAC lo encuentra igual; con menos suelo (un bosque denso o una ciudad) fallaría.
- 🎯 **Por qué importa:** Un modelo de terreno malo hace que las pendientes y las alturas de los árboles salgan mal. La decisión central: ¿cómo se separa el suelo del resto con la menor contaminación y qué densidad de puntos hace falta?
- 🔗 **Se estudia junto con:** filtro de suelo, RANSAC, recall, contaminación.

📘 **Dónde se aprende** (1 clase): [B57-C30 · Nubes de puntos tridimensionales](../programa/clases/B57/B57-C30-nubes-de-puntos-tridimensionales/CLASE.md).

### Nube molecular

- Una nube molecular es una nube interestelar fría y densa cuyo gas es sobre todo `H₂`.
- Una nube molecular es una nube interestelar fría y densa donde el hidrógeno es sobre todo molecular.

💡 **Cómo se explica en la clase [B24-C01](../programa/clases/B24/B24-C01-colapso-de-nubes-moleculares/CLASE.md):**
- Las estrellas se forman en el interior de nubes moleculares, regiones frías y densas de gas donde predomina el hidrógeno molecular; la formación estelar se mide en toda la escala, de galaxias enteras a nubes individuales (S3, resumen).
- Definir nube molecular, núcleo denso, velocidad del sonido y criterio de Jeans.
- 🎯 **Por qué importa:** Toda estrella es un trozo de gas interestelar que se contrajo. Sin saber cuándo la gravedad vence a la presión no se entiende por qué las estrellas nacen en nubes frías y densas y no en el gas tenue del medio interestelar, ni por qué la masa de las estrellas depende del entorno.
- 🔗 **Se estudia junto con:** núcleo denso, velocidad del sonido isoterma, longitud de Jeans, masa de Jeans.

📘 **Dónde se aprende** (2 clases): [B24-C01 · Colapso de nubes moleculares](../programa/clases/B24/B24-C01-colapso-de-nubes-moleculares/CLASE.md); [B25-C04 · Nubes moleculares y polvo](../programa/clases/B25/B25-C04-nubes-moleculares-y-polvo/CLASE.md).

### Nubosidad

- La nubosidad es el porcentaje de la escena cubierto por nubes.

💡 **Cómo se explica en la clase [B14-C25](../programa/clases/B14/B14-C25-catalogos-de-datos-geoespaciales-y-metadatos-stac/CLASE.md):**
- Nubosidad `≤ 20 %`: 84 escenas, que coincide con un conteo independiente `sum(1 for i in range(400) if (i·7) mod 100 ≤ 20)`.
- Si la propiedad de nubosidad faltara en algún ítem, el filtro lo descartaría o fallaría: hay que decidir qué hacer con los ausentes (C08).
- ⚠️ **Error frecuente:** Comparar nubosidades de definiciones distintas. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un satélite produce miles de escenas al día. Para estudiar una inundación necesitas las que cubren una región, en unas fechas, con poca nube.
- 🔗 **Se estudia junto con:** ítem, catálogo, colección, activo.

📘 **Dónde se aprende** (1 clase): [B14-C25 · Catálogos de datos geoespaciales y metadatos (STAC)](../programa/clases/B14/B14-C25-catalogos-de-datos-geoespaciales-y-metadatos-stac/CLASE.md).

### Núcleo

- El núcleo es el conjunto de funciones puras que contiene la ciencia.
- Un proceso gaussiano es un modelo que para cada entrada da una distribución normal; su núcleo (*kernel*) define cuánto se parecen las salidas de dos entradas cercanas, y el de base radial (RBF) tiene una longitud de escala por variable (S1).
- El núcleo es la zona donde el gas gana calor.
- *(y 7 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C01](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md):**
- La masa está casi toda en el núcleo: un protón pesa unas 1836 veces más que un electrón (S1).
- Por eso, a la primera aproximación, el electrón se mueve alrededor de un núcleo que apenas se mueve.
- 🎯 **Por qué importa:** Casi todo lo que sabemos de la composición de una estrella o de una nebulosa lo sabemos porque sus átomos emiten o absorben luz en colores muy precisos. Una línea roja a 656 nm no es «un color cualquiera»: es la firma del hidrógeno.
- 🔗 **Se estudia junto con:** átomo, protones, neutrones, electrones.

📘 **Dónde se aprende** (10 clases): [B06-C01 · Estructura atómica](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md); [B14-C01 · Arquitectura de software científico](../programa/clases/B14/B14-C01-arquitectura-de-software-cientifico/CLASE.md); [B17-C04 · Modelos sustitutos (surrogates)](../programa/clases/B17/B17-C04-modelos-sustitutos-surrogates/CLASE.md); [B17-C11 · Redes de segmentación semántica de imágenes](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md); [B27-C12 · Radiación sincrotrón](../programa/clases/B27/B27-C12-radiacion-sincrotron/CLASE.md); [B28-C12 · Modelos de emisión conjunta](../programa/clases/B28/B28-C12-modelos-de-emision-conjunta/CLASE.md) y 4 más.

### Núcleo activo de galaxia (AGN)

- Un núcleo activo de galaxia (AGN) es una región central cuya luminosidad no procede de estrellas sino de la acreción de gas sobre un agujero negro supermasivo.

💡 **Cómo se explica en la clase [B25-C11](../programa/clases/B25/B25-C11-nucleos-activos-de-galaxias/CLASE.md):**
- python programa/clases/B25/B25-C11-nucleos-activos-de-galaxias/agn_basico.py
- 🎯 **Por qué importa:** Algunas galaxias tienen en el centro una fuente que supera a todas sus estrellas, y casi todas las galaxias grandes albergan un agujero negro supermasivo. Entender el AGN une el centro de la galaxia, su gas y su evolución.
- 🔗 **Se estudia junto con:** acreción, eficiencia radiativa, luminosidad de Eddington, tiempo de Salpeter.

📘 **Dónde se aprende** (1 clase): [B25-C11 · Núcleos activos de galaxias](../programa/clases/B25/B25-C11-nucleos-activos-de-galaxias/CLASE.md).

### Núcleo de segundos intercalares (LSK)

- Un núcleo de segundos intercalares (LSK) es el archivo de SPICE con esa tabla (S3).

💡 **Contexto en la clase [B13-C08](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md):**
- **Idea central (modelo mental):** TAI es el reloj continuo. UTC es TAI menos un entero de segundos (con saltos). TT es TAI más una constante.
- 🎯 **Por qué importa:** Una efeméride planetaria se tabula en una escala de tiempo; el reloj civil usa otra; y la hora de una nave, otra distinta. Si usas la escala equivocada, una posición calculada para la Luna se desplaza: un segundo de diferencia son unos mil metros de movimiento orbital lunar.
- 🔗 **Se estudia junto con:** Tiempo Universal Coordinado (UTC), Tiempo Atómico Internacional (TAI), Tiempo Terrestre (TT), Tiempo Dinámico Baricéntrico (TDB).

📘 **Dónde se aprende** (1 clase): [B13-C08 · Escalas UTC, TAI, TT y TDB](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md).

### Núcleo denso

- Un núcleo denso es la región más densa de una nube, de donde saldrán una o pocas estrellas.

💡 **Cómo se explica en la clase [B24-C01](../programa/clases/B24/B24-C01-colapso-de-nubes-moleculares/CLASE.md):**
- Tomaremos como ejemplo conductor un núcleo denso con valores típicos ilustrativos (estimados, no de una nube concreta): temperatura `T = 10 K` y densidad numérica de moléculas `n(H₂) = 10⁴ cm⁻³`.
- Definir nube molecular, núcleo denso, velocidad del sonido y criterio de Jeans.
- 🎯 **Por qué importa:** Toda estrella es un trozo de gas interestelar que se contrajo. Sin saber cuándo la gravedad vence a la presión no se entiende por qué las estrellas nacen en nubes frías y densas y no en el gas tenue del medio interestelar, ni por qué la masa de las estrellas depende del entorno.
- 🔗 **Se estudia junto con:** nube molecular, velocidad del sonido isoterma, longitud de Jeans, masa de Jeans.

📘 **Dónde se aprende** (1 clase): [B24-C01 · Colapso de nubes moleculares](../programa/clases/B24/B24-C01-colapso-de-nubes-moleculares/CLASE.md).

### Núcleo inerte de helio

- El núcleo inerte de helio es la zona central sin fusión que crece.

💡 **Contexto en la clase [B24-C16](../programa/clases/B24/B24-C16-gigantes-rojas/CLASE.md):**
- **Idea central (modelo mental):** El núcleo inerte se contrae y calienta; la capa que lo rodea fusiona más fuerte; la envoltura, empujada por esa energía, se expande.
- 🎯 **Por qué importa:** Una gigante roja es mucho mayor y más luminosa que su estrella original y tiene una densidad media ínfima. Entender su tamaño, su gravedad y cómo crece su núcleo permite interpretar las gigantes observadas, usarlas como sondas asterosísmicas y anticipar el destino del Sol.
- 🔗 **Se estudia junto con:** gigante roja, quemado en capa, rama de las gigantes rojas, gravedad superficial.

📘 **Dónde se aprende** (1 clase): [B24-C16 · Gigantes rojas](../programa/clases/B24/B24-C16-gigantes-rojas/CLASE.md).

### Nucleón

- Un nucleón es un protón o un neutrón.

💡 **Contexto en la clase [B06-C03](../programa/clases/B06/B06-C03-isotopos-y-masa-atomica/CLASE.md):**
- **Idea central (modelo mental):** Imagina una bolsa con canicas de dos pesos casi iguales, mezcladas siempre en la misma proporción. Si pesas muchas, el peso medio de una canica depende del peso de cada tipo y de su proporción. Eso es la masa atómica de las tablas: un promedio ponderado.
- 🎯 **Por qué importa:** El carbono del Sol, ¿es igual que el de la Tierra? Una forma de preguntarlo con rigor es comparar cuántos átomos de carbono-12 hay por cada uno de carbono-13.
- 🔗 **Se estudia junto con:** número másico, isótopos, masa atómica relativa, abundancia isotópica.

📘 **Dónde se aprende** (1 clase): [B06-C03 · Isótopos y masa atómica](../programa/clases/B06/B06-C03-isotopos-y-masa-atomica/CLASE.md).

### Nucleosíntesis estelar

- La nucleosíntesis estelar es la formación de elementos en el interior de las estrellas.

💡 **Cómo se explica en la clase [B24-C08](../programa/clases/B24/B24-C08-nucleosintesis-estelar/CLASE.md):**
- python programa/clases/B24/B24-C08-nucleosintesis-estelar/combustibles.py
- 🎯 **Por qué importa:** El carbono de tu cuerpo, el oxígeno que respiras y el hierro de tus huesos se forjaron en estrellas. Entender cómo, y cuánta energía rinde cada etapa, explica por qué la vida de una estrella se acorta con cada combustible y por qué el hierro es el final de la cadena.
- 🔗 **Se estudia junto con:** triple alfa, partícula alfa, secuencia de quemado, grupo del hierro.

📘 **Dónde se aprende** (1 clase): [B24-C08 · Nucleosíntesis estelar](../programa/clases/B24/B24-C08-nucleosintesis-estelar/CLASE.md).

### Nucleosíntesis primordial

- La nucleosíntesis primordial es la formación de núcleos ligeros en los primeros minutos.

💡 **Cómo se explica en la clase [B26-C16](../programa/clases/B26/B26-C16-nucleosintesis-primordial/CLASE.md):**
- Cyburt, Fields, Olive y Yeh revisan la nucleosíntesis primordial: las observaciones recientes de deuterio concuerdan con el modelo estándar y con la densidad bariónica de Planck; combinadas con ella, acotan el número de especies de neutrinos a `N_ν < 3,2` (2σ); el litio-7 sigue en desacuerdo (S2, resumen).
- python programa/clases/B26/B26-C16-nucleosintesis-primordial/primordial.py
- 🎯 **Por qué importa:** La cuarta parte de la masa bariónica del universo es helio, y la proporción casi no cambió desde los primeros minutos. Su valor da información sobre cuántas especies de neutrinos existen y sobre la densidad de bariones.
- 🔗 **Se estudia junto con:** razón n/p, congelación, vida media del neutrón libre, energía de ligadura del deuterón.

📘 **Dónde se aprende** (1 clase): [B26-C16 · Nucleosíntesis primordial](../programa/clases/B26/B26-C16-nucleosintesis-primordial/CLASE.md).

### Nudo

- Un nudo es una milla náutica por hora, es decir, `1852/3600 m/s` (S2).
- Un nudo (*kink*) es un cambio brusco de ángulo de paso.

💡 **Cómo se explica en la clase [B03-C07](../programa/clases/B03/B03-C07-conversion-de-distancia-y-velocidad/CLASE.md):**
- El SI admite la hora, el día, la unidad astronómica, la milla náutica y el nudo (S2), cada una con equivalencia definida.
- Una embarcación que va a 15 nudos recorre `15 × 1852/3600 m/s = 7,717 m/s`.
- 🎯 **Por qué importa:** Una cifra de la NASA como «velocidad de escape 11,186 km/s» no significa lo mismo para quien trabaja en m/s ni para quien piensa en km/h. Si conviertes mal, el error no es de redondeo sino de factor: mil, tres mil seiscientos.
- 🔗 **Se estudia junto con:** factor de conversión, equivalencia exacta, unidad astronómica, tiempo de luz.

📘 **Dónde se aprende** (2 clases): [B03-C07 · Conversión de distancia y velocidad](../programa/clases/B03/B03-C07-conversion-de-distancia-y-velocidad/CLASE.md); [B25-C02 · Brazos espirales y barra galáctica](../programa/clases/B25/B25-C02-brazos-espirales-y-barra-galactica/CLASE.md).

### Nulidad

- El rango de un conjunto de vectores es la dimensión de su espacio generado; la nulidad es el número de relaciones de dependencia independientes.

💡 **Cómo se explica en la clase [B10-C02](../programa/clases/B10/B10-C02-bases-y-dimension/CLASE.md):**
- Para `{e₁, e₂, e₁ + e₂, e₃}` (cuatro vectores en `ℝ³`) el rango es 3 y la nulidad es 1, porque hay una relación independiente: `e₁ + e₂ − (e₁ + e₂) = 0`.
- Regla: rango + nulidad = número de vectores.
- 🎯 **Por qué importa:** Un vector es una entidad geométrica; sus «componentes» dependen de los ejes que elijas. Un operador de estación terrestre describe un satélite con ejes ligados al ecuador; el satélite mismo, con ejes ligados a su órbita; un instrumento, con ejes del instrumento.
- 🔗 **Se estudia junto con:** linealmente independiente, dependiente, generador, base.

📘 **Dónde se aprende** (1 clase): [B10-C02 · Bases y dimensión](../programa/clases/B10/B10-C02-bases-y-dimension/CLASE.md).

### Nulo

- El nulo es una dirección sin respuesta.
- El nulo: `g(x₀) = 0`.

💡 **Cómo se explica en la clase [B40-C11](../programa/clases/B40/B40-C11-efecto-sunyaev-zeldovich-termico-y-cinematico/CLASE.md):**
- *Descripción textual:* la densidad y la temperatura del gas dan `y`; la función espectral se verifica con Kompaneets y fija el nulo.
- El nulo térmico está en `x₀ = 3,83002` (`217,51 GHz`).
- 🎯 **Por qué importa:** El tSZ no depende del corrimiento al rojo y permite detectar cúmulos lejanos. La decisión central: ¿cuánto vale la distorsión a cada frecuencia y dónde se anula?
- 🔗 **Se estudia junto con:** parámetro de Compton, función espectral, profundidad óptica, operador de Kompaneets.

📘 **Dónde se aprende** (2 clases): [B40-C11 · Efecto Sunyaev-Zeldovich térmico y cinemático](../programa/clases/B40/B40-C11-efecto-sunyaev-zeldovich-termico-y-cinematico/CLASE.md); [B49-C04 · Arreglos de antenas: factor de arreglo y formación de haz](../programa/clases/B49/B49-C04-arreglos-de-antenas-factor-de-arreglo-y-formacion-de-haz/CLASE.md).

### Numerador

- `a` es el numerador y `b` el denominador (nunca cero).

💡 **Cómo se explica en la clase [B03-C02](../programa/clases/B03/B03-C02-fracciones-y-razones-de-magnitudes/CLASE.md):**
- Esto funciona porque dividir numerador y denominador entre `k` equivale a multiplicar la fracción por `(1/k)/(1/k) = 1`, que no la cambia.
- ⚠️ **Error frecuente:** Sumar numeradores y denominadores. Ejercicio 2.
- 🎯 **Por qué importa:** Una cifra aislada como «69 911 km» no dice si Júpiter es grande o pequeño. Una razón sí: Júpiter tiene un radio unas 11 veces el terrestre.
- 🔗 **Se estudia junto con:** fracción, denominador, equivalentes, Simplificar.

📘 **Dónde se aprende** (1 clase): [B03-C02 · Fracciones y razones de magnitudes](../programa/clases/B03/B03-C02-fracciones-y-razones-de-magnitudes/CLASE.md).

### Número atómico

- El número atómico `Z` es el número de protones y define el elemento; el número másico `A` es la suma de protones y neutrones.

💡 **Cómo se explica en la clase [B06-C01](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md):**
- Describir el átomo como núcleo (protones y neutrones) y electrones, y distinguir número atómico de número másico.
- 🎯 **Por qué importa:** Casi todo lo que sabemos de la composición de una estrella o de una nebulosa lo sabemos porque sus átomos emiten o absorben luz en colores muy precisos. Una línea roja a 656 nm no es «un color cualquiera»: es la firma del hidrógeno.
- 🔗 **Se estudia junto con:** átomo, núcleo, protones, neutrones.

📘 **Dónde se aprende** (1 clase): [B06-C01 · Estructura atómica](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md).

### Número bariónico

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B31-C10](../programa/clases/B31/B31-C10-modelo-estandar-de-particulas/CLASE.md):**
- Sumar cargas y números bariónicos de quarks.
- Ejercicio 7. Número bariónico de `p p → p p p p̄`.
- 🎯 **Por qué importa:** Antes de calcular una sección eficaz, una reacción debe respetar las leyes de conservación. La decisión central: ¿está permitida esta reacción por las reglas de conservación?
- 🔗 **Se estudia junto con:** quark, hadrón, leptón, número leptónico.

📘 **Dónde se aprende** (1 clase): [B31-C10 · Modelo estándar de partículas](../programa/clases/B31/B31-C10-modelo-estandar-de-particulas/CLASE.md).

### Número complejo

- Un número complejo es `z = a + b i`, con `i² = −1`; su módulo es `|z| = √(a² + b²)`.

💡 **Cómo se explica en la clase [B15-C04](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md):**
- Cada `X[k]` es un número complejo: su módulo dice cuánto de la frecuencia `k` hay; su ángulo (la fase) dice cuándo está el máximo de esa oscilación.
- *Descripción textual:* la serie de `N` muestras se transforma en `N` números complejos; su módulo da el espectro y su fase la posición temporal; la transformada inversa devuelve la serie original sin pérdida.
- 🎯 **Por qué importa:** Si una estrella pulsa con una pequeña amplitud en medio del ruido, mirar la curva de luz no la revela, pero su espectro de frecuencias sí: un pico a una frecuencia concreta. Lo mismo ocurre con una vibración en una estructura espacial, una señal de radio o un periodo en un registro geofísico.
- 🔗 **Se estudia junto con:** módulo, fórmula de Euler, transformada de Fourier continua, transformada discreta de Fourier (DFT).

📘 **Dónde se aprende** (1 clase): [B15-C04 · Transformada de Fourier](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md).

### Número cuántico rotacional

- El número cuántico rotacional `J` (0, 1, 2…) mide el giro.

💡 **Contexto en la clase [B62-C01](../programa/clases/B62/B62-C01-espectros-rotacionales-de-moleculas-niveles-y-reglas-de-seleccion/CLASE.md):**
- **Idea central (modelo mental):** Imagina dos esferas unidas por una varilla que gira: solo ciertas velocidades de giro están permitidas. Límite de la analogía: la varilla clásica admite cualquier velocidad; aquí el giro está cuantizado y la varilla se estira un poco al girar rápido.
- 🎯 **Por qué importa:** Una línea de CO a 115,27 GHz no es un dato aislado: es la consecuencia de un momento de inercia. Si entiendes de dónde sale, puedes predecir líneas que nadie ha medido y reconocer cuándo una línea observada no es del CO.
- 🔗 **Se estudia junto con:** rotor rígido, constante rotacional, regla de selección, distorsión centrífuga.

📘 **Dónde se aprende** (1 clase): [B62-C01 · Espectros rotacionales de moléculas: niveles y reglas de selección](../programa/clases/B62/B62-C01-espectros-rotacionales-de-moleculas-niveles-y-reglas-de-seleccion/CLASE.md).

### Número de Abbe

- El número de Abbe `V = (n_d − 1)/(n_F − n_C)`.

💡 **Cómo se explica en la clase [B41-C14](../programa/clases/B41/B41-C14-aberracion-cromatica-y-astigmatismo/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. ¿Qué sentido tiene un número de Abbe mayor?
- El script [cromatica.py](cromatica.py) calcula la dispersión, el número de Abbe y los focos tangencial y sagital (comprueba `f/V` a 3 % y los focos a `10⁻⁴`).
- 🎯 **Por qué importa:** El color y el astigmatismo degradan el campo de refractores y espejos. La decisión central: ¿cuánto se separan los focos por color y por plano?
- 🔗 **Se estudia junto con:** dispersión, aberración cromática longitudinal, F, d, C, astigmatismo.

📘 **Dónde se aprende** (3 clases): [B41-C14 · Aberración cromática y astigmatismo](../programa/clases/B41/B41-C14-aberracion-cromatica-y-astigmatismo/CLASE.md); [B43-C21 · Selección de vidrios ópticos: catálogos, homogeneidad y diagramas](../programa/clases/B43/B43-C21-seleccion-de-vidrios-opticos-catalogos-homogeneidad-y-diagramas/CLASE.md); [B45-C05 · Prismas y dispersión](../programa/clases/B45/B45-C05-prismas-y-dispersion/CLASE.md).

### Número de Biot

- El número de Biot `Bi = h L/k`.

💡 **Contexto en la clase [B43-C11](../programa/clases/B43/B43-C11-dilatacion-termica-y-estabilidad/CLASE.md):**
- **Idea central (modelo mental):** Como un helado que se derrite desde la superficie: la capa externa cambia de inmediato y el centro tarda; cuanto más grueso, más lento, con el aire como aislante.
- 🎯 **Por qué importa:** La estabilidad térmica fija cuándo se puede observar y cada cuánto hay que reenfocar. La decisión central: ¿cuánto se mueve el foco por kelvin, cómo se compensa y cuánto tarda el espejo en igualarse al aire?
- 🔗 **Se estudia junto con:** coeficiente de dilatación, deriva de foco, compensación, constante de tiempo.

📘 **Dónde se aprende** (1 clase): [B43-C11 · Dilatación térmica y estabilidad](../programa/clases/B43/B43-C11-dilatacion-termica-y-estabilidad/CLASE.md).

### Número de condición

- El número de condición `κ(A)` mide cuánto puede amplificarse el error relativo (se define con valores singulares en C11).
- El número de condición es `κ = σ₁/σ_r`.
- El número de condición `κ` de una cuadrática `½ xᵀ A x` es la razón entre su mayor y menor valor propio.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B10-C05](../programa/clases/B10/B10-C05-sistemas-lineales-y-eliminacion/CLASE.md):**
- El número de condición es `κ = 1,67`: bien condicionado.
- Estimar la pérdida de cifras con el número de condición.
- ⚠️ **Error frecuente:** Ignorar el número de condición. Se corrige con los ejercicios 9 y 10.
- 🎯 **Por qué importa:** Para fijar la posición de un objeto a partir de las distancias a tres estaciones se plantean tres ecuaciones con dos incógnitas (plano). Los sistemas reales tienen decenas o miles de incógnitas: parámetros orbitales, sesgos de relojes, coeficientes de calibración.
- 🔗 **Se estudia junto con:** sistema lineal, matriz ampliada, operación elemental de fila, eliminación gaussiana.

📘 **Dónde se aprende** (9 clases): [B10-C05 · Sistemas lineales y eliminación](../programa/clases/B10/B10-C05-sistemas-lineales-y-eliminacion/CLASE.md); [B10-C11 · Valores singulares y SVD](../programa/clases/B10/B10-C11-valores-singulares-y-svd/CLASE.md); [B11-C17 · Optimización numérica](../programa/clases/B11/B11-C17-optimizacion-numerica/CLASE.md); [B57-C22 · Espectrómetros de imagen e hiperespectrales](../programa/clases/B57/B57-C22-espectrometros-de-imagen-e-hiperespectrales/CLASE.md); [B59-C05 · Minerales marcianos](../programa/clases/B59/B59-C05-minerales-marcianos/CLASE.md); [B74-C15 · Geometría de la red de seguimiento](../programa/clases/B74/B74-C15-geometria-de-la-red-de-seguimiento/CLASE.md) y 3 más.

### Número de Courant

- El número de Courant es `ν = c Δt/Δx`.
- El número de Courant `ν = cΔt/Δx` compara cuánto avanza la onda en un paso con el ancho de celda.

💡 **Contexto en la clase [B11-C14](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md):**
- **Idea central (modelo mental):** FTCS hace que cada nodo se acerque al promedio de sus vecinos con un peso `r`. Si `r` es pequeño, se acerca despacio; si pasa de `1/2`, se pasa del promedio y el signo se invierte en cada paso, amplificando lo que debería suavizar.
- 🎯 **Por qué importa:** Casi todo código de simulación de calor, fluidos o plasma en una malla regular usa diferencias finitas. Elegir el paso de tiempo equivocado no da un resultado ligeramente malo: da un resultado que explota.
- 🔗 **Se estudia junto con:** malla, esquema FTCS, esquema BTCS, error de truncamiento.

📘 **Dónde se aprende** (2 clases): [B11-C14 · Diferencias finitas](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md); [B21-C02 · Ecuación de onda: esquemas y dispersión numérica](../programa/clases/B21/B21-C02-ecuacion-de-onda-esquemas-y-dispersion-numerica/CLASE.md).

### Número de Elsasser

- El número de Elsasser `Λ = σB²/(ρΩ)` compara la fuerza de Lorentz con la de Coriolis.

💡 **Contexto en la clase [B65-C02](../programa/clases/B65/B65-C02-dinamos-planetarias-y-campos-magneticos-de-origen-interno/CLASE.md):**
- **Idea central (modelo mental):** Un dínamo de bicicleta convierte movimiento en electricidad; una dinamo planetaria es un dínamo cuyo campo lo produce el propio fluido en movimiento. Sin movimiento, el campo se apaga como una rueda que se frena.
- 🎯 **Por qué importa:** La presencia o ausencia de un campo global dice si un cuerpo tiene un fluido conductor en movimiento. La decisión central: ¿qué intensidad de campo permite un núcleo y cuánto duraría ese campo si el movimiento se detuviera?
- 🔗 **Se estudia junto con:** dinamo, número de Reynolds magnético, tiempo de decaimiento óhmico, difusividad magnética.

📘 **Dónde se aprende** (1 clase): [B65-C02 · Dinamos planetarias y campos magnéticos de origen interno](../programa/clases/B65/B65-C02-dinamos-planetarias-y-campos-magneticos-de-origen-interno/CLASE.md).

### Número de enlace

- El número de enlace cuenta cuántas veces se enlazan dos curvas.

💡 **Cómo se explica en la clase [B35-C07](../programa/clases/B35/B35-C07-congelamiento-del-flujo-magnetico-y-conservacion-en-mhd-ideal/CLASE.md):**
- El número de enlace, entero, es invariante bajo deformaciones sin cortes.
- El script [flujo_congelado.py](flujo_congelado.py) integra la inducción y la difusión y calcula el número de enlace (comprueba la deriva del flujo, el error de la difusión y `Lk = ±1`).
- 🎯 **Por qué importa:** La conservación del flujo explica por qué el campo se amplifica al comprimirse y por qué la reconexión exige romper la idealidad. La decisión central: ¿cuándo el campo se mueve con el plasma y cuándo se difunde?
- 🔗 **Se estudia junto con:** flujo magnético, Congelado, resistividad, helicidad.

📘 **Dónde se aprende** (1 clase): [B35-C07 · Congelamiento del flujo magnético y conservación en MHD ideal](../programa/clases/B35/B35-C07-congelamiento-del-flujo-magnetico-y-conservacion-en-mhd-ideal/CLASE.md).

### Número de Euler

- Una función exponencial tiene la forma `y = a·bˣ`, con base `b > 0` y `b ≠ 1`; el número de Euler `e ≈ 2,71828` es la base natural.

💡 **Contexto en la clase [B04-C05](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md):**
- **Idea central (modelo mental):** Multiplicar potencias de la misma base equivale a sumar exponentes: `bᵃ·bᶜ = bᵃ⁺ᶜ`. El logaritmo convierte esa idea en herramienta: `log(xy) = log x + log y`. Una escala logarítmica transforma *cocientes* en *diferencias*: por eso «5 magnitudes» es una diferencia, pero un factor 100 de flujo.
- 🎯 **Por qué importa:** El ojo y los instrumentos comparan brillos que difieren en factores de un millón. Los astrónomos lo resuelven con una escala logarítmica: la magnitud.
- 🔗 **Se estudia junto con:** función exponencial, logaritmo en base b, logaritmo decimal, natural.

📘 **Dónde se aprende** (1 clase): [B04-C05 · Funciones exponenciales y logarítmicas](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md).

### Número de Fresnel

- El número de Fresnel `N_F = a²/(4λz)`.
- El número de Fresnel `a²/(λz)`.

💡 **Cómo se explica en la clase [B42-C02](../programa/clases/B42/B42-C02-principio-de-huygens-fresnel/CLASE.md):**
- El número de Fresnel es la regla práctica: `N_F ≪ 1` autoriza la transformada de Fourier.
- *Descripción textual:* la suma de ondas secundarias de la rendija se compara con la fórmula analítica de campo lejano, y el número de Fresnel decide cuál vale.
- 🎯 **Por qué importa:** Sin este principio no hay un procedimiento para calcular qué le pasa a la luz al pasar por una apertura (la pupila de un telescopio es una). La decisión central: ¿a qué distancia vale la aproximación de campo lejano y cuándo hay que sumar las ondas secundarias una por una?
- 🔗 **Se estudia junto con:** frente de onda secundario, apertura, campo lejano, campo cercano.

📘 **Dónde se aprende** (2 clases): [B42-C02 · Principio de Huygens-Fresnel](../programa/clases/B42/B42-C02-principio-de-huygens-fresnel/CLASE.md); [B47-C07 · Coronógrafos espaciales](../programa/clases/B47/B47-C07-coronografos-espaciales/CLASE.md).

### Número de Froude

- El número de Froude `Fr = v²/(g L)` mide la importancia de la inercia frente a la gravedad; la transición marcha–carrera ocurre cerca de `Fr = 0,5` (valor empírico de enseñanza).
- El número de Froude `Fr = u/√(g d)` compara la velocidad con la de una onda superficial.
- El número de Froude `Fr = v/√(g L)` compara inercia y gravedad.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B66-C01](../programa/clases/B66/B66-C01-valles-y-canales-morfologia-y-origen-en-superficies-planetarias/CLASE.md):**
- *Descripción textual:* de la geometría salen el radio hidráulico, la velocidad, el caudal, el número de Froude y la tensión de fondo; la velocidad se contrasta con Manning.
- Un canal ancho de `W = 20 m` y profundidad `d = 1,0 m` con pendiente `S = 0,01` y factor de fricción `f = 0,05` conduce `75,587 m³/s` en la Tierra, `46,585 m³/s` en Marte y `28,070 m³/s` en Titán, con el mismo número de Froude `1,206`.
- 🎯 **Por qué importa:** Un valle visto desde órbita no dice por sí solo cuánta agua (o metano) pasó por él. La decisión central: ¿cuánto caudal transporta un canal de la misma geometría en otro cuerpo, y qué cambia además del caudal?
- 🔗 **Se estudia junto con:** radio hidráulico, ecuación de Darcy–Weisbach, ecuación de Manning, tensión de fondo.

📘 **Dónde se aprende** (4 clases): [B66-C01 · Valles y canales: morfología y origen en superficies planetarias](../programa/clases/B66/B66-C01-valles-y-canales-morfologia-y-origen-en-superficies-planetarias/CLASE.md); [B97-C18 · Pruebas en entornos análogos](../programa/clases/B97/B97-C18-pruebas-en-entornos-analogos/CLASE.md); [B105-C18 · Investigación de efectos de gravedad parcial](../programa/clases/B105/B105-C18-investigacion-de-efectos-de-gravedad-parcial/CLASE.md); [B115-C01 · Cultivos hidropónicos para hábitats](../programa/clases/B115/B115-C01-cultivos-hidroponicos-para-habitats/CLASE.md).

### Número de Knudsen

- El número de Knudsen `Kn = λ/L`.
- El número de Knudsen `Kn = λ/L` separa continuo (`Kn ≪ 1`) de molecular (`Kn ≫ 1`).

💡 **Cómo se explica en la clase [B35-C04](../programa/clases/B35/B35-C04-colisiones-regimen-cinetico-y-ecuacion-de-vlasov/CLASE.md):**
- Clasificar un plasma por su número de Knudsen.
- 🎯 **Por qué importa:** Saber si un plasma es colisional decide qué modelo usar. La decisión central: ¿es el camino libre medio mayor o menor que la escala del problema?
- 🔗 **Se estudia junto con:** longitud de Debye, parámetro de plasma, camino libre medio, Vlasov.

📘 **Dónde se aprende** (2 clases): [B35-C04 · Colisiones, régimen cinético y ecuación de Vlasov](../programa/clases/B35/B35-C04-colisiones-regimen-cinetico-y-ecuacion-de-vlasov/CLASE.md); [B85-C12 · Entorno de vacío](../programa/clases/B85/B85-C12-entorno-de-vacio/CLASE.md).

### Número de ligereza

- El número de ligereza `β` compara la fuerza de radiación con la gravedad solar.

💡 **Cómo se explica en la clase [B78-C12](../programa/clases/B78/B78-C12-velas-solares/CLASE.md):**
- El número de ligereza de una vela ilustrativa de `1000 m²` y `20 g/m²` es `β = 0,073`, independiente de la distancia (la gravedad también cae con `d⁻²`).
- Calcular el número de ligereza como cociente entre fuerza de radiación y gravitatoria.
- 🎯 **Por qué importa:** La vela no gasta propelente, pero su empuje es del orden de los micronewton por metro cuadrado y cae con el cuadrado de la distancia al Sol. La decisión central: ¿cuánta aceleración da una vela real y cómo depende de su orientación y de su distancia?
- 🔗 **Se estudia junto con:** irradiancia, presión de radiación, reflectividad, vela.

📘 **Dónde se aprende** (1 clase): [B78-C12 · Velas solares](../programa/clases/B78/B78-C12-velas-solares/CLASE.md).

### Número de Love

- El número de Love `k₂` mide la respuesta del cuerpo (cuánto se deforma).

💡 **Contexto en la clase [B65-C06](../programa/clases/B65/B65-C06-calentamiento-por-marea-y-equilibrio-termico-en-satelites/CLASE.md):**
- **Idea central (modelo mental):** Un clip que se dobla y se estira se calienta; un satélite cuya marea sube y baja en cada órbita se calienta igual, y solo si la órbita es excéntrica la marea cambia.
- 🎯 **Por qué importa:** Un satélite pequeño se enfría rápido; si aun así tiene un interior caliente, algo lo calienta. La decisión central: ¿cuánto calor produce una marea y a qué temperatura de equilibrio llevaría la superficie?
- 🔗 **Se estudia junto con:** marea, factor de calidad, excentricidad, equilibrio térmico.

📘 **Dónde se aprende** (1 clase): [B65-C06 · Calentamiento por marea y equilibrio térmico en satélites](../programa/clases/B65/B65-C06-calentamiento-por-marea-y-equilibrio-termico-en-satelites/CLASE.md).

### Número de Lundquist

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B30-C11](../programa/clases/B30/B30-C11-reconexion-magnetica/CLASE.md):**
- Con números de Lundquist grandes, Sweet–Parker es demasiado lento para una erupción de minutos: una tasa de `10⁻⁶` da meses.
- Calcular el número de Lundquist `S = Lv_A/η`.
- 🎯 **Por qué importa:** Las erupciones liberan en minutos una energía que el campo guardó durante mucho más tiempo, y el modelo más simple de reconexión es demasiado lento para eso. La decisión central: ¿qué tasa de reconexión hace falta y qué dice el modelo de Sweet–Parker?
- 🔗 **Se estudia junto con:** reconexión, hoja de corriente, tasa de reconexión, tiempo de Alfvén.

📘 **Dónde se aprende** (1 clase): [B30-C11 · Reconexión magnética](../programa/clases/B30/B30-C11-reconexion-magnetica/CLASE.md).

### Número de Mach

- El número de Mach `M` es la velocidad entre la del sonido y cambia `Cd`.
- El número de Mach `M = |u|/c` compara la velocidad con la del sonido.
- El número de Mach `M = v/c_s`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B21-C04](../programa/clases/B21/B21-C04-ecuaciones-de-navier-stokes-y-dinamica-de-fluidos-computacional/CLASE.md):**
- El criterio habitual es el número de Mach: por debajo de unos 0,3 los cambios de densidad son pequeños y la formulación incompresible es una buena aproximación (regla práctica estándar, no respaldada por una fuente consultada).
- La compresible no necesita resolver Poisson, pero su paso lo fija `|u| + c` (C01), muy pequeño a número de Mach bajo.
- 🎯 **Por qué importa:** Un fluido aparece en casi toda la ingeniería aeroespacial: el aire alrededor de un cohete, el propelente que se mueve en un tanque, el refrigerante de un satélite.
- 🔗 **Se estudia junto con:** ecuaciones de Navier–Stokes, ecuaciones de Euler, incompresible, viscosidad cinemática.

📘 **Dónde se aprende** (5 clases): [B21-C04 · Ecuaciones de Navier-Stokes y dinámica de fluidos computacional](../programa/clases/B21/B21-C04-ecuaciones-de-navier-stokes-y-dinamica-de-fluidos-computacional/CLASE.md); [B35-C08 · Flujos de plasma estacionarios y balance de presiones](../programa/clases/B35/B35-C08-flujos-de-plasma-estacionarios-y-balance-de-presiones/CLASE.md); [B77-C04 · Coeficientes de arrastre y sustentación](../programa/clases/B77/B77-C04-coeficientes-de-arrastre-y-sustentacion/CLASE.md); [B79-C01 · Conservación de masa en fluidos](../programa/clases/B79/B79-C01-conservacion-de-masa-en-fluidos/CLASE.md); [B79-C05 · Dinámica de fluidos compresibles](../programa/clases/B79/B79-C05-dinamica-de-fluidos-compresibles/CLASE.md).

### Número de Mach de salida

- El número de Mach de salida `Mₑ` resume la expansión.

💡 **Contexto en la clase [B78-C10](../programa/clases/B78/B78-C10-propulsion-de-gas-frio/CLASE.md):**
- 🎯 **Por qué importa:** Con la misma temperatura, el gas más liviano escapa más rápido, pero ocupa más volumen almacenado. La decisión central: ¿qué gas da más impulso por kilo y qué cuesta en volumen y en límites físicos de la expansión?
- 🔗 **Se estudia junto con:** gas frío, flujo estrangulado, área de garganta, impulso total.

📘 **Dónde se aprende** (1 clase): [B78-C10 · Propulsión de gas frío](../programa/clases/B78/B78-C10-propulsion-de-gas-frio/CLASE.md).

### Número de manchas

- Las manchas solares son zonas oscuras de la superficie; el número de manchas es un índice de actividad que publica el centro SILSO (S5).
- El número de manchas mide la actividad.

💡 **Cómo se explica en la clase [B08-C16](../programa/clases/B08/B08-C16-observacion-solar-con-filtros-certificados/CLASE.md):**
- SILSO, un centro de datos mundial del Observatorio Real de Bélgica, distribuye el número de manchas, incluido un valor diario estimado (S5).
- Para una persona ciega, los datos abiertos con descripción hablada o el sonido del número de manchas (sonificación de una serie) permiten participar; el calor del Sol y el cambio de luz se pueden sentir y describir sin mirar.
- 🎯 **Por qué importa:** Una persona que mira un eclipse parcial con gafas falsas, o enfoca el Sol con un telescopio sin filtro frontal, puede quedar con una lesión permanente. La pregunta motivadora: ¿cómo observo el Sol sin dañarme y sin dañar a otros?
- 🔗 **Se estudia junto con:** ISO 12312-2, visor solar, filtro solar frontal, filtro de ocular.

📘 **Dónde se aprende** (2 clases): [B08-C16 · Observación solar con filtros certificados](../programa/clases/B08/B08-C16-observacion-solar-con-filtros-certificados/CLASE.md); [B30-C03 · Ciclo de actividad solar](../programa/clases/B30/B30-C03-ciclo-de-actividad-solar/CLASE.md).

### Número de mérito

- El número de mérito `M = ρ_l σ h_fg/μ_l` compara fluidos.

💡 **Cómo se explica en la clase [B85-C09](../programa/clases/B85/B85-C09-tubos-de-calor/CLASE.md):**
- Calcular el número de mérito de un fluido.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de capacidad de un tubo de calor*: `ΔP_cap`, `F_l`, `Q_max` horizontal y con elevación, número de mérito y lista de lo ilustrativo y no consultado.
- 🎯 **Por qué importa:** Un tubo de calor es un conductor térmico muy bueno pero tiene un límite de potencia que se descubre tarde: en un ensayo en tierra, o en vuelo con una carga mayor. La decisión central: ¿cuánto calor transporta como máximo un tubo y cuánto pierde en un ensayo con inclinación?
- 🔗 **Se estudia junto con:** límite capilar, elevación, longitud efectiva.

📘 **Dónde se aprende** (1 clase): [B85-C09 · Tubos de calor](../programa/clases/B85/B85-C09-tubos-de-calor/CLASE.md).

### Número de Nusselt

- El número de Nusselt `Nu` es el flujo total dividido por el flujo que habría solo por conducción.
- El número de Nusselt `Nu = h L/k` compara convección con conducción.

💡 **Contexto en la clase [B65-C01](../programa/clases/B65/B65-C01-conveccion-del-manto-y-evolucion-termica-de-interiores-planetarios/CLASE.md):**
- **Idea central (modelo mental):** Como una olla calentada por abajo: mientras el fondo esté poco más caliente que la tapa, el calor sube por conducción; al superar un umbral, el fluido se pone en movimiento y el calor sube mucho más rápido.
- 🎯 **Por qué importa:** Sin convección, el interior de un planeta rocoso solo perdería calor por conducción y se enfriaría con una escala de tiempo mucho mayor. La decisión central: ¿cuánto calor saca la convección y a qué temperatura se estabiliza un manto que sigue produciendo calor radiactivo?
- 🔗 **Se estudia junto con:** número de Rayleigh, Rayleigh crítico, evolución térmica parametrizada, viscosidad de Arrhenius.

📘 **Dónde se aprende** (2 clases): [B65-C01 · Convección del manto y evolución térmica de interiores planetarios](../programa/clases/B65/B65-C01-conveccion-del-manto-y-evolucion-termica-de-interiores-planetarios/CLASE.md); [B85-C03 · Convección y ausencia de convección exterior](../programa/clases/B85/B85-C03-conveccion-y-ausencia-de-conveccion-exterior/CLASE.md).

### Número de onda

- El número de onda `k = 2π/λ` y la frecuencia angular `ω` se relacionan con `ω = ck`: es la relación de dispersión.
- El número de onda `k = 2π/λ`.

💡 **Cómo se explica en la clase [B21-C02](../programa/clases/B21/B21-C02-ecuacion-de-onda-esquemas-y-dispersion-numerica/CLASE.md):**
- Paso 2 · Número de onda. `k = 2π·20 = 125,66`;
- Estimar el número de puntos por longitud de onda para una tolerancia de fase dada.
- 🎯 **Por qué importa:** Casi toda señal que viaja en el espacio —ondas de radio, ondas de Alfvén en la corona solar, ondas sísmicas en una luna, vibraciones de una estructura— obedece alguna forma de la ecuación de onda.
- 🔗 **Se estudia junto con:** ecuación de onda, onda viajera, onda estacionaria, frecuencia angular.

📘 **Dónde se aprende** (2 clases): [B21-C02 · Ecuación de onda: esquemas y dispersión numérica](../programa/clases/B21/B21-C02-ecuacion-de-onda-esquemas-y-dispersion-numerica/CLASE.md); [B42-C01 · Ecuaciones de onda electromagnética](../programa/clases/B42/B42-C01-ecuaciones-de-onda-electromagnetica/CLASE.md).

### Número de Péclet

- El número de Péclet `Pe = u L/Γ` compara advección y difusión; el Péclet de celda es `Pe/N`.

💡 **Cómo se explica en la clase [B79-C09](../programa/clases/B79/B79-C09-cfd-academico-fundamentos-y-limites/CLASE.md):**
- Detectar oscilaciones cuando el número de Péclet de celda supera 2.
- 🎯 **Por qué importa:** B11-C14/C15 no construyen simulaciones de flujo ni discuten sus límites. Sin esa discusión, una malla fina y un colorido mapa de campos se confunden con una predicción fiable.
- 🔗 **Se estudia junto con:** verificación, validación, Péclet de celda, orden observado.

📘 **Dónde se aprende** (1 clase): [B79-C09 · CFD académico: fundamentos y límites](../programa/clases/B79/B79-C09-cfd-academico-fundamentos-y-limites/CLASE.md).

### Número de Rayleigh

- El número de Rayleigh `Ra = ρ g α ΔT H³/(κ η)` mide la tendencia a convectar.
- El número de Rayleigh es `Ra = g β ΔT L³/(ν α)`.
- El número de Rayleigh `Ra = α ρ g ΔT d³ / (κ η)` compara el empuje térmico con la disipación por difusión y viscosidad.

💡 **Cómo se explica en la clase [B53-C14](../programa/clases/B53/B53-C14-geologia-de-europa/CLASE.md):**
- *Descripción textual:* El flujo de calor fija el espesor; el espesor decide el número de Rayleigh y la presión basal.
- Para `20 mW/m²` el número de Rayleigh es `7,64 × 10⁶` con parámetros ilustrativos, y la presión en la base `34,1 MPa`.
- 🎯 **Por qué importa:** El espesor de la capa de hielo controla qué mide un radar, cómo se fractura la superficie y si el océano se comunica con ella. La decisión central: ¿qué espesor corresponde a un flujo de calor dado y si ese espesor sería conductivo o convectivo?
- 🔗 **Se estudia junto con:** conducción, presión basal.

📘 **Dónde se aprende** (3 clases): [B53-C14 · Geología de Europa](../programa/clases/B53/B53-C14-geologia-de-europa/CLASE.md); [B65-C01 · Convección del manto y evolución térmica de interiores planetarios](../programa/clases/B65/B65-C01-conveccion-del-manto-y-evolucion-termica-de-interiores-planetarios/CLASE.md); [B85-C03 · Convección y ausencia de convección exterior](../programa/clases/B85/B85-C03-conveccion-y-ausencia-de-conveccion-exterior/CLASE.md).

### Número de Reynolds

- El número de Reynolds `Re = UL/ν` compara transporte y difusión.
- El número de Reynolds de la partícula `Re = ρ v 2r/μ` debe ser menor que 1 para que valga Stokes.
- El número de Reynolds `Re = ρ V L/μ = V L/ν` compara inercia y viscosidad.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B21-C04](../programa/clases/B21/B21-C04-ecuaciones-de-navier-stokes-y-dinamica-de-fluidos-computacional/CLASE.md):**
- Paso 1 · Número de Reynolds. `Re = UL/ν = 1·1/0,1 = 10`: flujo viscoso, laminar.
- Calcular el número de Reynolds y el paso de tiempo máximo (difusivo y advectivo).
- 🎯 **Por qué importa:** Un fluido aparece en casi toda la ingeniería aeroespacial: el aire alrededor de un cohete, el propelente que se mueve en un tanque, el refrigerante de un satélite.
- 🔗 **Se estudia junto con:** ecuaciones de Navier–Stokes, ecuaciones de Euler, incompresible, viscosidad cinemática.

📘 **Dónde se aprende** (4 clases): [B21-C04 · Ecuaciones de Navier-Stokes y dinámica de fluidos computacional](../programa/clases/B21/B21-C04-ecuaciones-de-navier-stokes-y-dinamica-de-fluidos-computacional/CLASE.md); [B54-C08 · Nubes y aerosoles](../programa/clases/B54/B54-C08-nubes-y-aerosoles/CLASE.md); [B79-C04 · Regímenes laminar y turbulento](../programa/clases/B79/B79-C04-regimenes-laminar-y-turbulento/CLASE.md); [B106-C29 · Almacenamiento y distribución de agua potable en hábitats](../programa/clases/B106/B106-C29-almacenamiento-y-distribucion-de-agua-potable-en-habitats/CLASE.md).

### Número de Reynolds magnético

- El número de Reynolds magnético `Rm = μ₀σuL` compara la inducción por el flujo con la difusión óhmica.

💡 **Cómo se explica en la clase [B65-C02](../programa/clases/B65/B65-C02-dinamos-planetarias-y-campos-magneticos-de-origen-interno/CLASE.md):**
- Calcular el número de Reynolds magnético `Rm = μ₀σuL`.
- 🎯 **Por qué importa:** La presencia o ausencia de un campo global dice si un cuerpo tiene un fluido conductor en movimiento. La decisión central: ¿qué intensidad de campo permite un núcleo y cuánto duraría ese campo si el movimiento se detuviera?
- 🔗 **Se estudia junto con:** dinamo, número de Elsasser, tiempo de decaimiento óhmico, difusividad magnética.

📘 **Dónde se aprende** (1 clase): [B65-C02 · Dinamos planetarias y campos magnéticos de origen interno](../programa/clases/B65/B65-C02-dinamos-planetarias-y-campos-magneticos-de-origen-interno/CLASE.md).

### Número de Rossby

- El número de Rossby `Ro` es el cociente entre el periodo de rotación y el tiempo de vuelco convectivo.
- El número de Rossby `Ro = U/(f L)` compara la inercia con la rotación.
- El número de Rossby compara la aceleración con la fuerza de Coriolis.

💡 **Cómo se explica en la clase [B24-C11](../programa/clases/B24/B24-C11-rotacion-y-campos-magneticos/CLASE.md):**
- Interpretar el número de Rossby y la saturación de la actividad.
- 🎯 **Por qué importa:** La rotación y el campo explican por qué las estrellas jóvenes son más activas, por qué las enanas blancas y las estrellas de neutrones giran y se magnetizan tanto, y por qué no pueden girar a cualquier velocidad.
- 🔗 **Se estudia junto con:** velocidad de rotación, velocidad crítica, momento de inercia, momento angular.

📘 **Dónde se aprende** (3 clases): [B24-C11 · Rotación y campos magnéticos](../programa/clases/B24/B24-C11-rotacion-y-campos-magneticos/CLASE.md); [B54-C06 · Circulación general planetaria](../programa/clases/B54/B54-C06-circulacion-general-planetaria/CLASE.md); [B57-C12 · Oceanografía desde órbita](../programa/clases/B57/B57-C12-oceanografia-desde-orbita/CLASE.md).

### Número de Rouse

- El número de Rouse `P = w_s/(κ u*)` separa carga de fondo (`P > 2,5`), suspensión mixta (`0,8 < P ≤ 2,5`) y suspensión (`P ≤ 0,8`), con umbrales ilustrativos.

💡 **Cómo se explica en la clase [B66-C05](../programa/clases/B66/B66-C05-depositos-sedimentarios-y-sedimentologia-planetaria/CLASE.md):**
- *Descripción textual:* el tamaño de grano y la gravedad dan la velocidad de caída; con la velocidad de fricción sale el número de Rouse y la facies; el caudal de sedimento fija el avance del delta.
- Descripción larga: con menos gravedad los granos caen más despacio y el número de Rouse baja; el delta avanza en proporción al caudal de sedimento.
- 🎯 **Por qué importa:** Los deltas marcianos se interpretan como archivo de ambientes pasados, pero un grano cae más despacio con menos gravedad y el mismo flujo puede dejar otra facies. La decisión central: ¿cómo cambia la facies que deja un flujo cuando cambia la gravedad?
- 🔗 **Se estudia junto con:** velocidad de caída, ley de Stokes, progradación.

📘 **Dónde se aprende** (1 clase): [B66-C05 · Depósitos sedimentarios y sedimentología planetaria](../programa/clases/B66/B66-C05-depositos-sedimentarios-y-sedimentologia-planetaria/CLASE.md).

### Número de Stokes

- El número de Stokes `St = Ω t_s` compara el tiempo de frenado `t_s` con el periodo orbital.
- El número de Stokes `St = τ v/D` compara la inercia de la gota con el tamaño del obstáculo (la raíz).

💡 **Cómo se explica en la clase [B52-C03](../programa/clases/B52/B52-C03-granulacion-de-polvo-y-acrecion/CLASE.md):**
- Calcular el número de Stokes de un grano en régimen de Epstein.
- 🎯 **Por qué importa:** Si los granos derivan más rápido de lo que crecen, el polvo se pierde antes de formar planetesimales. La decisión central: ¿a qué tamaño deriva más rápido un grano y cuánto tarda en caer?
- 🔗 **Se estudia junto con:** régimen de Epstein, deriva radial.

📘 **Dónde se aprende** (2 clases): [B52-C03 · Granulación de polvo y acreción](../programa/clases/B52/B52-C03-granulacion-de-polvo-y-acrecion/CLASE.md); [B115-C04 · Sistemas aeropónicos](../programa/clases/B115/B115-C04-sistemas-aeroponicos/CLASE.md).

### Número de supernovas por masa

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B38-C07](../programa/clases/B38/B38-C07-modelos-submalla-de-formacion-estelar-y-retroalimentacion/CLASE.md):**
- Obtener el número de supernovas por masa estelar de una IMF.
- 🎯 **Por qué importa:** El gas denso forma estrellas por debajo de la resolución de la simulación y las supernovas devuelven energía. La decisión central: ¿cuánto gas expulsa la retroalimentación y a qué equilibrio llega la zona?
- 🔗 **Se estudia junto con:** modelo submalla, ley de Schmidt, eficiencia, fracción térmica.

📘 **Dónde se aprende** (1 clase): [B38-C07 · Modelos submalla de formación estelar y retroalimentación](../programa/clases/B38/B38-C07-modelos-submalla-de-formacion-estelar-y-retroalimentacion/CLASE.md).

### Número efectivo de muestras independientes

- El número efectivo de muestras independientes `N_eff` es el que daría el mismo error de promedio si los datos fueran blancos.

💡 **Cómo se explica en la clase [B15-C03](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md):**
- Estimar el número efectivo de muestras independientes.
- 🎯 **Por qué importa:** Una regla heredada de la física del laboratorio dice que, al promediar `N` mediciones, el error baja como `1/√N`. Esa regla solo vale si los errores de cada medición son independientes.
- 🔗 **Se estudia junto con:** ruido blanco, AR(1), paseo aleatorio, ruido coloreado.

📘 **Dónde se aprende** (1 clase): [B15-C03 · Ruido blanco y coloreado](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md).

### Número esperado de fallas

- El número esperado de fallas es `μ = n λ T`.

💡 **Cómo se explica en la clase [B97-C12](../programa/clases/B97/B97-C12-robots-de-mantenimiento/CLASE.md):**
- *Descripción textual:* de las tasas sale el número esperado de fallas;
- Calcular el número esperado de fallas de cada tipo.
- 🎯 **Por qué importa:** Pocos repuestos dejan la misión sin reparación posible; demasiados cargan masa. La confianza del conjunto, no la de cada pieza, es la que importa, y se obtiene con el producto de las probabilidades.
- 🔗 **Se estudia junto con:** tasa de falla, distribución de Poisson, confianza, unidad reemplazable (ORU).

📘 **Dónde se aprende** (1 clase): [B97-C12 · Robots de mantenimiento](../programa/clases/B97/B97-C12-robots-de-mantenimiento/CLASE.md).

### Número esperado de víctimas

- El número esperado de víctimas `E_c` es la suma de áreas de víctima por la densidad de población.

💡 **Contexto en la clase [B118-C14](../programa/clases/B118/B118-C14-reentrada-y-riesgos-en-superficie/CLASE.md):**
- 🎯 **Por qué importa:** El riesgo en superficie se controla antes de lanzar: limitando los fragmentos que sobreviven o confinando la reentrada a zonas despobladas. La decisión central: ¿cuánta área de víctima se puede aceptar para respetar 10⁻⁴ y cómo influye dónde cae?
- 🔗 **Se estudia junto con:** área de víctima, densidad expuesta, supervivencia, zona de dispersión.

📘 **Dónde se aprende** (1 clase): [B118-C14 · Reentrada y riesgos en superficie](../programa/clases/B118/B118-C14-reentrada-y-riesgos-en-superficie/CLASE.md).

### Número f

- Enfocador: mecanismo que mueve el foco. Número f: foco entre apertura.

💡 **Contexto en la clase [B48-C22](../programa/clases/B48/B48-C22-control-automatico-del-enfocador-y-autoenfoque/CLASE.md):**
- **Idea central (modelo mental):** Es encontrar el fondo de un valle a partir de unos pocos puntos de la ladera: la parábola ajustada indica dónde está el fondo.
- 🎯 **Por qué importa:** Un enfoque erróneo pierde resolución en todas las imágenes de la noche. La decisión central: ¿en qué posición del enfocador está el mínimo y con qué incertidumbre?
- 🔗 **Se estudia junto con:** HFD, Curva en V, Enfocador, Ecuaciones normales.

📖 **Explicado a fondo:** [Distancia focal y número f](esencial/esencial-d-l.md#distancia-focal-y-número-f) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B48-C22 · Control automático del enfocador y autoenfoque](../programa/clases/B48/B48-C22-control-automatico-del-enfocador-y-autoenfoque/CLASE.md).

### Número irracional

- Un número irracional no se puede escribir así;

💡 **Cómo se explica en la clase [B03-C01](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md):**
- Descripción larga: todos los números de la tabla caben sobre la misma recta; los racionales son densos pero dejan «huecos» que ocupan los irracionales.
- Clasificar un número como natural, entero, racional o irracional, y decir por qué.
- 🎯 **Por qué importa:** Una agencia espacial no «confía» en un cálculo: lo comprueba. Para saber cuánto tarda la Luna en dar una vuelta alrededor de la Tierra basta multiplicar, dividir y respetar el orden de las operaciones; pero un paréntesis mal puesto convierte 27 días en una cifra absurda.
- 🔗 **Se estudia junto con:** número natural, entero, número racional, números reales.

📘 **Dónde se aprende** (1 clase): [B03-C01 · Números y operaciones fundamentales](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md).

### Número leptónico

- El número leptónico `L_e`, `L_μ`, `L_τ`.

💡 **Cómo se explica en la clase [B31-C10](../programa/clases/B31/B31-C10-modelo-estandar-de-particulas/CLASE.md):**
- En cambio `μ⁻ → e⁻ + γ` viola los números leptónicos electrónico y muónico.
- 🎯 **Por qué importa:** Antes de calcular una sección eficaz, una reacción debe respetar las leyes de conservación. La decisión central: ¿está permitida esta reacción por las reglas de conservación?
- 🔗 **Se estudia junto con:** quark, hadrón, leptón, número bariónico.

📘 **Dónde se aprende** (1 clase): [B31-C10 · Modelo estándar de partículas](../programa/clases/B31/B31-C10-modelo-estandar-de-particulas/CLASE.md).

### Número másico

- El número atómico `Z` es el número de protones y define el elemento; el número másico `A` es la suma de protones y neutrones.
- El número másico `A` es el número de nucleones.

💡 **Cómo se explica en la clase [B06-C01](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md):**
- Describir el átomo como núcleo (protones y neutrones) y electrones, y distinguir número atómico de número másico.
- 🎯 **Por qué importa:** Casi todo lo que sabemos de la composición de una estrella o de una nebulosa lo sabemos porque sus átomos emiten o absorben luz en colores muy precisos. Una línea roja a 656 nm no es «un color cualquiera»: es la firma del hidrógeno.
- 🔗 **Se estudia junto con:** átomo, núcleo, protones, neutrones.

📘 **Dónde se aprende** (2 clases): [B06-C01 · Estructura atómica](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md); [B06-C03 · Isótopos y masa atómica](../programa/clases/B06/B06-C03-isotopos-y-masa-atomica/CLASE.md).

### Número Mg

- El número Mg de un olivino es la fracción molar de Mg frente a (Mg + Fe).

💡 **Contexto en la clase [B06-C19](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md):**
- **Idea central (modelo mental):** Imagina un grano de roca (un silicato) en una nube fría, cubierto por capas de hielo: primero agua, luego CO₂ y otras moléculas, según las temperaturas de condensación. Si el grano entra en una región más cálida, las capas externas se evaporan primero.
- 🎯 **Por qué importa:** Los estudios con el telescopio James Webb muestran que las nubes densas del medio interestelar tienen granos de polvo cubiertos de hielos con una variedad de moléculas, y que esos hielos contienen entre el 2 y el 19 % del carbono, oxígeno, nitrógeno y azufre disponibles (S1, resumen).
- 🔗 **Se estudia junto con:** hielo, mineral, olivino, forsterita.

📘 **Dónde se aprende** (1 clase): [B06-C19 · Química de hielos y minerales](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md).

### Número natural

- Un número natural sirve para contar: 1, 2, 3… Un entero añade el cero y los negativos: −3, 0, 5.

💡 **Cómo se explica en la clase [B03-C01](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md):**
- Los números naturales cuentan cosas discretas: tres planetas rocosos interiores, cuatro lunas galileanas.
- Clasificar un número como natural, entero, racional o irracional, y decir por qué.
- 🎯 **Por qué importa:** Una agencia espacial no «confía» en un cálculo: lo comprueba. Para saber cuánto tarda la Luna en dar una vuelta alrededor de la Tierra basta multiplicar, dividir y respetar el orden de las operaciones; pero un paréntesis mal puesto convierte 27 días en una cifra absurda.
- 🔗 **Se estudia junto con:** entero, número racional, número irracional, números reales.

📘 **Dónde se aprende** (1 clase): [B03-C01 · Números y operaciones fundamentales](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md).

### Número negativo

- Un número negativo es menor que cero; su opuesto es el positivo del mismo tamaño (`−3` y `3`).

💡 **Cómo se explica en la clase [B03-C09](../programa/clases/B03/B03-C09-operaciones-con-numeros-negativos/CLASE.md):**
- Un número negativo con menor valor absoluto es mayor.
- Sumar un número positivo avanza a la derecha; sumar uno negativo retrocede.
- 🎯 **Por qué importa:** Cuando observas una llamarada solar a las 12:00:00, el evento ocurrió antes: su tiempo es el observado menos 499 s. Si sumas en vez de restar, afirmas que la llamarada ocurre en el futuro.
- 🔗 **Se estudia junto con:** opuesto, valor absoluto, recta numérica, convención de signo.

📘 **Dónde se aprende** (1 clase): [B03-C09 · Operaciones con números negativos](../programa/clases/B03/B03-C09-operaciones-con-numeros-negativos/CLASE.md).

### Número racional

- Un número racional es el que se puede escribir como cociente de dos enteros, como `1/4` o `27,3217` (que es `273 217/10 000`).

💡 **Cómo se explica en la clase [B03-C01](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md):**
- Descripción larga: todos los números de la tabla caben sobre la misma recta; los racionales son densos pero dejan «huecos» que ocupan los irracionales.
- Clasificar un número como natural, entero, racional o irracional, y decir por qué.
- 🎯 **Por qué importa:** Una agencia espacial no «confía» en un cálculo: lo comprueba. Para saber cuánto tarda la Luna en dar una vuelta alrededor de la Tierra basta multiplicar, dividir y respetar el orden de las operaciones; pero un paréntesis mal puesto convierte 27 días en una cifra absurda.
- 🔗 **Se estudia junto con:** número natural, entero, número irracional, números reales.

📘 **Dónde se aprende** (1 clase): [B03-C01 · Números y operaciones fundamentales](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md).

### Número reproductivo

- El número reproductivo `R` es el promedio de reenvíos que provoca cada reenvío;

💡 **Contexto en la clase [B130-C04](../programa/clases/B130/B130-C04-divulgacion-cientifica-en-redes-sociales/CLASE.md):**
- 🎯 **Por qué importa:** Las redes tienen formatos y riesgos propios que no están tratados en la comunicación escrita u oral. La decisión central: ¿cómo se publica un mensaje correcto, con su fuente, de modo que resista el recorte y la difusión?
- 🔗 **Se estudia junto con:** hilo, texto alternativo, cascada, proceso de ramificación.

📘 **Dónde se aprende** (1 clase): [B130-C04 · Divulgación científica en redes sociales](../programa/clases/B130/B130-C04-divulgacion-cientifica-en-redes-sociales/CLASE.md).

### Números reales

- Los racionales y los irracionales forman juntos los números reales, los que ocupan la recta numérica.

💡 **Contexto en la clase [B03-C01](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md):**
- **Idea central (modelo mental):** Piensa en una expresión como una receta con pasos ordenados. Algunos pasos «pesan más» y se hacen antes. ```mermaid flowchart TD A["Expresión escrita"] --> B["1.
- 🎯 **Por qué importa:** Una agencia espacial no «confía» en un cálculo: lo comprueba. Para saber cuánto tarda la Luna en dar una vuelta alrededor de la Tierra basta multiplicar, dividir y respetar el orden de las operaciones; pero un paréntesis mal puesto convierte 27 días en una cifra absurda.
- 🔗 **Se estudia junto con:** número natural, entero, número racional, número irracional.

📘 **Dónde se aprende** (1 clase): [B03-C01 · Números y operaciones fundamentales](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md).

### NumPy

- NumPy es una biblioteca para cálculo numérico; su estructura central es el arreglo (`ndarray`): una rejilla de elementos del mismo tipo con tamaño fijo (S2).

💡 **Cómo se explica en la clase [B07-C09](../programa/clases/B07/B07-C09-calculos-cientificos-basicos-con-python/CLASE.md):**
- Límite de la analogía: una hoja de cálculo mezcla tipos libremente; un arreglo de NumPy tiene un solo `dtype`, y eso lo hace rápido pero obliga a que todos los elementos sean del mismo tipo.
- Para aritmética exacta existen `fractions` y `decimal`; los `float64` de NumPy son suficientes cuando se declara la tolerancia.
- 🎯 **Por qué importa:** Calcular la densidad de ocho planetas con un `for` funciona, pero a escala de millones de datos es lento y verboso. NumPy opera sobre arreglos completos con una sola expresión y es la base de casi toda la ciencia con Python.
- 🔗 **Se estudia junto con:** arreglo, vectorizada, difusión, densidad media.

📘 **Dónde se aprende** (1 clase): [B07-C09 · Cálculos científicos básicos con Python](../programa/clases/B07/B07-C09-calculos-cientificos-basicos-con-python/CLASE.md).

### Nyquist

- Frecuencia de muestreo `fs`: muestras por segundo. Nyquist: `fs/2`.

💡 **Cómo se explica en la clase [B90-C23](../programa/clases/B90/B90-C23-instrumentacion-y-adquisicion-de-datos-en-ensayos/CLASE.md):**
- Para `f₀ = 1 500 Hz`: a 8 192 Hz (Nyquist 4 096) aparece en 1 500; a 2 048 Hz (Nyquist 1 024), en `|1 500 − 2 048| = 548 Hz`; a 2 000 Hz, en 500 Hz.
- Con `fs = 8 192 Hz` lo que está sobre Nyquist (4 096 Hz) llega atenuado al menos 24 dB; con un filtro de orden 4 y `fs` solo 2,5 veces la banda no habría margen suficiente.
- 🎯 **Por qué importa:** Un ensayo de vibración que muestrea a 2 048 Hz un tono de 1 500 Hz lo registra como si fuera de 548 Hz y no se nota. La decisión central: ¿qué frecuencia de muestreo, qué filtro y cuántos bits aseguran que lo que se registra es lo que ocurrió?
- 🔗 **Se estudia junto con:** Frecuencia de muestreo fs, Aliasing, Filtro antialias, Cuantización.

📘 **Dónde se aprende** (1 clase): [B90-C23 · Instrumentación y adquisición de datos en ensayos](../programa/clases/B90/B90-C23-instrumentacion-y-adquisicion-de-datos-en-ensayos/CLASE.md).
