# Términos · T (parte 1 de 2)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · **T** · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: **1** · [2](terminos-t-2.md)

### T

- Una dimensión es la clase física de una magnitud; aquí usamos tres dimensiones base: M (masa), L (longitud) y T (tiempo).

🎯 **Por qué importa (clase B13-C02):** Un satélite recibe un comando con un tiempo de encendido de motor; el ingeniero de tierra usó una fórmula del periodo orbital copiada de una hoja de cálculo. Si la fórmula está mal dimensionada, el resultado sale en «segundos al cuadrado» o en «metros por segundo» sin que nadie lo note.

📘 **Dónde se aprende** (1 clase): [B13-C02 · Dimensiones y trazabilidad](../programa/clases/B13/B13-C02-dimensiones-y-trazabilidad/CLASE.md).

### T no central

- Para la prueba `t` de dos muestras con `n` por grupo, el estadístico bajo la alternativa sigue una `t` no central con `2n − 2` grados de libertad y parámetro de no centralidad `d√(n/2)`.

💡 **Cómo se explica en la clase [B12-C26](../programa/clases/B12/B12-C26-sesgos-y-potencia-estadistica-en-poblaciones-pequenas/CLASE.md):**
- Con `α = 0,05` bilateral, la potencia exacta por la `t` no central y la simulada (100 000 réplicas) son:
- Calcular la potencia exacta de una prueba `t` de dos muestras con la `t` no central.
- 🎯 **Por qué importa:** En medicina espacial, en estudios con tripulaciones o en misiones con pocas unidades, los tamaños de muestra son pequeños por necesidad. Con ellos, la mayoría de los efectos reales no se detectan, y los que se detectan suelen estar inflados.

📘 **Dónde se aprende** (1 clase): [B12-C26 · Sesgos y potencia estadística en poblaciones pequeñas](../programa/clases/B12/B12-C26-sesgos-y-potencia-estadistica-en-poblaciones-pequenas/CLASE.md).

### Tabla

- Una tabla es un conjunto de columnas del mismo largo; cada fila describe un objeto y cada columna una propiedad.
- Una figura es un gráfico o imagen; una tabla, una disposición de valores en filas y columnas.

💡 **Cómo se explica en la clase [B14-C05](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md):**
- Los metadatos de la tabla guardan la procedencia («sintético»).
- Cada columna lleva su unidad y su máscara; la tabla lleva su procedencia.
- 🎯 **Por qué importa:** Un catálogo de estrellas no es una lista de números: cada columna tiene una unidad, algunas filas no tienen paralaje, y la tabla viene de un instrumento, una época y una versión. Si pierdes eso al copiar los datos a un arreglo, pierdes la mitad del significado.

📘 **Dónde se aprende** (2 clases): [B14-C05 · Tablas astronómicas y catálogos](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md); [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md).

### Tabla de capitalización

- La tabla de capitalización lista quién tiene cuántas acciones.
- La tabla de capitalización lista quién tiene qué acciones.

💡 **Cómo se explica en la clase [B124-C07](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md):**
- Construir una tabla de capitalización con acciones, precio y valoraciones.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de flujo, retorno y dilución sintéticos*: VAN, TIR con su verificación, MOIC, tabla de capitalización de dos rondas con su comprobación y lista de qué es sintético, con el aviso de que no es asesoría de inversión.
- 🎯 **Por qué importa:** El dinero privado tiene un costo distinto del público: se paga con retorno y con propiedad. La decisión central: ¿qué retorno exige y qué parte del proyecto se cede a cambio?

📘 **Dónde se aprende** (2 clases): [B124-C07 · Financiamiento privado](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md); [B126-C01 · Capital semilla y financiamiento inicial](../programa/clases/B126/B126-C01-capital-semilla-y-financiamiento-inicial/CLASE.md).

### Tabla de contingencia

- La tabla de contingencia (con un umbral de probabilidad) cuenta aciertos `a` (alarma y evento), falsas alarmas `b`, omisiones `c` y rechazos correctos `d`.

💡 **Cómo se explica en la clase [B12-C24](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md):**
- *Descripción textual:* de los pronósticos y eventos se calcula el puntaje de Brier y, con una referencia, el BSS; con un umbral se arma la tabla de contingencia y de ella POD, POFD, TSS y HSS; un bootstrap da la incertidumbre de las métricas; el informe declara referencia, umbral, muestra y límites.
- Equivalente accesible a la tabla de contingencia (datos sintéticos, umbral `0,2`):
- 🎯 **Por qué importa:** Un pronóstico de «no habrá llamarada» acierta el 90 % de los días en una época tranquila y no sirve de nada. La exactitud bruta premia lo trivial.

📘 **Dónde se aprende** (1 clase): [B12-C24 · Métricas de habilidad (skill scores) de pronóstico](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md).

### Tabla de opacidad

- Una tabla de opacidad guarda `log κ` en una malla `(log ρ, log T)`.

💡 **Cómo se explica en la clase [B37-C03](../programa/clases/B37/B37-C03-opacidad-media-de-rosseland-y-tablas-de-opacidad-en-interiores/CLASE.md):**
- Una tabla de `9 × 9` puntos (pasos de 0,5 dex en `ρ` y 0,25 dex en `T`) de una opacidad de juguete con curvatura añadida: en `ρ = 150 kg/m³` y `T = 1,3 × 10⁷ K` el valor exacto es `53,247` y el interpolado `51,440`, un error de `3,394 %`.
- *Descripción textual:* se promedia la inversa de la opacidad con el peso de la derivada de Planck, se guarda en una tabla y se interpola.
- 🎯 **Por qué importa:** Un código no integra en frecuencia en cada capa: lee una tabla de `κ_R(ρ, T)`. La decisión central: ¿cómo se promedia la opacidad y qué error añade la interpolación de la tabla?

📘 **Dónde se aprende** (1 clase): [B37-C03 · Opacidad media de Rosseland y tablas de opacidad en interiores](../programa/clases/B37/B37-C03-opacidad-media-de-rosseland-y-tablas-de-opacidad-en-interiores/CLASE.md).

### Tabla de respuestas

- La tabla de respuestas asocia cada monitor con una acción.

🎯 **Por qué importa (clase B88-C12):** Un monitor demasiado sensible dispara respuestas innecesarias; uno demasiado lento deja crecer el fallo. La decisión central: ¿qué persistencia equilibra las falsas alarmas y el tiempo de detección?

📘 **Dónde se aprende** (1 clase): [B88-C12 · Detección aislamiento y recuperación de fallos](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md).

### Tabla ICE

- La tabla ICE (inicial, cambio, equilibrio) organiza el cálculo.

💡 **Cómo se explica en la clase [B06-C13](../programa/clases/B06/B06-C13-equilibrio-quimico/CLASE.md):**
- Esta tabla es la versión accesible de una gráfica de `K` frente a la temperatura.
- Resolver una tabla ICE para un equilibrio sencillo.
- 🎯 **Por qué importa:** Según el cálculo de esta clase, el CO₂ de Marte puede condensarse como hielo o volver al gas según la temperatura. Es un equilibrio entre CO₂ sólido y gas: `CO₂(s) ⇌ CO₂(g)`.

📘 **Dónde se aprende** (1 clase): [B06-C13 · Equilibrio químico](../programa/clases/B06/B06-C13-equilibrio-quimico/CLASE.md).

### Tabla periódica

- La tabla periódica ordena los elementos por número atómico `Z` creciente.

💡 **Cómo se explica en la clase [B06-C02](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md):**
- python programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/abundancias_solares.py
- 🎯 **Por qué importa:** Cuando alguien dice «el universo es casi todo hidrógeno y helio», ¿en qué sentido es cierto? ¿En número de átomos, en masa, en el Sol, en la Tierra?

📘 **Dónde se aprende** (1 clase): [B06-C02 · Tabla periódica y abundancias cósmicas](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md).

### Tabla virtual

- Una tabla virtual es una tabla que el motor implementa con un módulo (aquí, `rtree`).

💡 **Cómo se explica en la clase [B14-C28](../programa/clases/B14/B14-C28-bases-de-datos-espaciales/CLASE.md):**
- El laboratorio crea una tabla `escenas(id, nombre)` y una tabla virtual `idx` con `rtree(id, minX, maxX, minY, maxY)`, e inserta 50 000 huellas en ambas (con SQLite 3.45.3).
- Crea la tabla de escenas y la tabla virtual del índice.
- 🎯 **Por qué importa:** Un archivo tiene 50 000 huellas de escenas y tu aplicación pregunta «¿qué escenas cubren este punto?» miles de veces. Recorrerlas todas cada vez desperdicia tiempo.

📘 **Dónde se aprende** (1 clase): [B14-C28 · Bases de datos espaciales](../programa/clases/B14/B14-C28-bases-de-datos-espaciales/CLASE.md).

### Tadpole

- El ángulo coorbital `θ = λ_part − λ_Tierra` (sin envolver) distingue: tadpole (`θ` oscila alrededor de `±60°` sin cruzar `0` ni `π`), herradura (`θ` cubre `π` sin cruzar `0` ni `2π`) y cuasi-satélite (`θ` oscila alrededor de `0` con una amplitud pequeña y la partícula se mantiene a unos pocos `R_H`).

💡 **Cómo se explica en la clase [B73-C22](../programa/clases/B73/B73-C22-capturas-temporales-y-cuasi-satelites/CLASE.md):**
- Analogía: tres formas de acompañar a un corredor en una pista circular: ir un poco por delante o por detrás oscilando (tadpole), alternar yendo delante y detrás pasando por el lado opuesto (herradura), o rodearlo en pequeños lazos sin alejarse (cuasi-satélite).
- Por ángulo: tadpole, herradura, cuasi-satélite.
- 🎯 **Por qué importa:** Un asteroide puede acompañar a la Tierra durante siglos sin orbitarla: dando vueltas alrededor de L4 (tadpole), de L3–L4–L5 (herradura) o de la propia Tierra (cuasi-satélite); y puede ser capturado temporalmente dentro de su esfera de Hill. Distinguirlos requiere una clasificación operativa y una advertencia: no son satélites.

📘 **Dónde se aprende** (1 clase): [B73-C22 · Capturas temporales y cuasi-satélites](../programa/clases/B73/B73-C22-capturas-temporales-y-cuasi-satelites/CLASE.md).

### TAG

- El TAG identifica la especie; su signo negativo indica frecuencia medida.

💡 **Cómo se explica en la clase [B62-C07](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md):**
- El laboratorio las lee con ancho fijo y comprueba, para las seis líneas, que `GUP = 2J'+1`, que `TAG = −28001` (negativo: frecuencia medida en laboratorio) y que `DR = 2`.
- Leer los campos de una línea JPL (`FREQ`, `ERR`, `LGINT`, `DR`, `ELO`, `GUP`, `TAG`, `QNFMT`, cuantos).
- 🎯 **Por qué importa:** Una identificación depende de una frecuencia, y esa frecuencia viene de un archivo que alguien ajustó y versionó. Si no sabes leer la columna de error, la unidad de la intensidad o la temperatura de referencia, importarás un error silencioso.

📘 **Dónde se aprende** (1 clase): [B62-C07 · Bancos de datos moleculares: CDMS, JPL, HITRAN y LAMDA](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md).

### Tamaño

- El tamaño es cuántos procesos hay y el rango (*rank*) es el número de cada uno, de 0 a tamaño−1.

💡 **Cómo se explica en la clase [B18-C02](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md):**
- Con mayúsculas, le entregas el bloque de memoria de un arreglo (`[datos, MPI.DOUBLE]`) y el receptor debe haber preparado un arreglo del tamaño y tipo correctos.
- Explicar el modelo SPMD, el rango y el tamaño de un comunicador.
- 🎯 **Por qué importa:** Ocho, cuarenta o cuatro mil núcleos de un clúster no comparten memoria. Para que cada uno propague su parte de un catálogo de órbitas y luego se junten los resultados, hay que decir quién envía qué a quién, y cuándo.

📘 **Dónde se aprende** (1 clase): [B18-C02 · Paso de mensajes con MPI](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md).

### Tamaño angular

- Un tamaño angular `θ` es el ángulo que un objeto ocupa en el cielo, y el tamaño físico `s` es su longitud real.
- El tamaño angular de un objeto es el ángulo que subtiende visto desde un punto.
- El tamaño angular es `2R/d` y da la distancia.

💡 **Cómo se explica en la clase [B01-C03](../programa/clases/B01/B01-C03-objetos-celestes-y-sus-diferencias/CLASE.md):**
- Pasar de un tamaño angular y una distancia a un tamaño físico, y usarlo para decidir qué clase de objeto es.
- 🎯 **Por qué importa:** En 2006 la Asamblea General de la Unión Astronómica Internacional votó una definición de planeta y, desde entonces, Plutón dejó de contarse como el noveno planeta. Muchas personas sintieron que «se había cambiado la realidad».

📘 **Dónde se aprende** (3 clases): [B01-C03 · Objetos celestes y sus diferencias](../programa/clases/B01/B01-C03-objetos-celestes-y-sus-diferencias/CLASE.md); [B03-C18 · Razones trigonométricas iniciales](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md); [B74-C25 · Detección de limbo y bordes planetarios en imágenes de navegación](../programa/clases/B74/B74-C25-deteccion-de-limbo-y-bordes-planetarios-en-imagenes-de-navegacion/CLASE.md).

### Tamaño crítico

- El tamaño crítico `a_c = (K_Ic/(Y σ_max))²/π` es donde `K = K_Ic`.

💡 **Cómo se explica en la clase [B84-C08](../programa/clases/B84/B84-C08-fatiga-y-fractura/CLASE.md):**
- *Descripción textual:* los datos dan el tamaño crítico y los ciclos por dos vías (cerrada y numérica); por separado, Basquin y Miner dan el daño de un espectro.
- Hallar el tamaño crítico de grieta `a_c` con `K_Ic`.
- 🎯 **Por qué importa:** La mayoría de las fallas estructurales en servicio son por fatiga; saber cuántos ciclos quedan y qué grieta es tolerable decide si una pieza se acepta. La decisión central: ¿cuántos ciclos tarda una grieta inicial en llegar al tamaño crítico y cuánto daño acumula un espectro de cargas?

📘 **Dónde se aprende** (1 clase): [B84-C08 · Fatiga y fractura](../programa/clases/B84/B84-C08-fatiga-y-fractura/CLASE.md).

### Tamaño de celda

- El tamaño de celda depende de la latitud: un segundo de arco mide unos 31 m en latitud y menos en longitud lejos del ecuador.

💡 **Cómo se explica en la clase [B57-C28](../programa/clases/B57/B57-C28-modelos-digitales-de-elevacion/CLASE.md):**
- *Descripción textual:* la rejilla y el tamaño de celda alimentan el operador de Horn, que da pendiente y orientación; un paso mayor las subestima, y los objetos sobre el terreno distinguen el MDS del MDT.
- Calcular el tamaño de celda en metros de una rejilla en grados.
- 🎯 **Por qué importa:** La pendiente decide dónde se produce un deslizamiento, cómo corre el agua o si una antena ve el horizonte. La decisión central: ¿qué resolución y qué tipo de modelo necesito para la pendiente que me importa?

📘 **Dónde se aprende** (1 clase): [B57-C28 · Modelos digitales de elevación](../programa/clases/B57/B57-C28-modelos-digitales-de-elevacion/CLASE.md).

### Tamaño de corte

- El tamaño de corte `d50` es el tamaño con probabilidad 0,5.

💡 **Cómo se explica en la clase [B59-C22](../programa/clases/B59/B59-C22-beneficio-y-separacion-granulometrica-de-regolito/CLASE.md):**
- Describir una curva de partición con tamaño de corte y agudeza.
- Tamano de corte d50 = 75 µm ; agudeza k = 4
- 🎯 **Por qué importa:** Calentar o reducir todo el regolito es caro; separar la fracción rica antes ahorra energía. La decisión central: ¿qué tamaño de corte equilibra la ley del concentrado y la recuperación del mineral?

📘 **Dónde se aprende** (1 clase): [B59-C22 · Beneficio y separación granulométrica de regolito](../programa/clases/B59/B59-C22-beneficio-y-separacion-granulometrica-de-regolito/CLASE.md).

### Tamaño de grano

- El tamaño de grano `a` es su radio.

💡 **Cómo se explica en la clase [B55-C05](../programa/clases/B55/B55-C05-granos-de-polvo-interestelar/CLASE.md):**
- Ejercicio 11 · transferencia. ¿Por qué no basta `π a²` para la extinción de luz de granos de tamaño comparable a la longitud de onda?
- Ejercicio 12 · integrador. Elabora tu *ficha de la población de granos*: define `q`, `a_min`, `a_max`, `ρ` y el cociente de masa, calcula `K`, número, área y sección por H, el reparto por tamaño y el tiempo de adsorción a cuatro temperaturas.
- 🎯 **Por qué importa:** Los granos de polvo son la superficie donde ocurren muchas reacciones que en fase gaseosa no ocurren (C07) y donde se acumulan hielos (C06). Saber cuánta superficie hay por átomo de H determina cuánta química de superficie es posible.

📘 **Dónde se aprende** (1 clase): [B55-C05 · Granos de polvo interestelar](../programa/clases/B55/B55-C05-granos-de-polvo-interestelar/CLASE.md).

### Tamaño de muestra

- El tamaño de muestra `n` es el número de personas por brazo.
- El tamaño de muestra `n = ⌈ln 0,05 / ln(1 − p)⌉`.

💡 **Cómo se explica en la clase [B88-C40](../programa/clases/B88/B88-C40-auditoria-de-software-espacial/CLASE.md):**
- Calcular el tamaño de muestra para confianza dada.
- El script [auditoria_muestreo.py](auditoria_muestreo.py) calcula tamaños de muestra y detección hipergeométrica, la verifica por Monte Carlo y encadena un registro con SHA-256, y comprueba que la alteración se detecta desde su entrada.
- 🎯 **Por qué importa:** No se puede revisar todo; se revisa una muestra. La decisión central: ¿qué tamaño de muestra da una probabilidad aceptable de detectar desviaciones y cómo se protege el registro de lo auditado?

📘 **Dónde se aprende** (2 clases): [B88-C40 · Auditoría de software espacial](../programa/clases/B88/B88-C40-auditoria-de-software-espacial/CLASE.md); [B124-C18 · Comunicación y divulgación](../programa/clases/B124/B124-C18-comunicacion-y-divulgacion/CLASE.md).

### Tamaño de muestra equivalente

- El tamaño de muestra equivalente de un Gamma(a, b) es el de «a eventos vistos en b horas».

💡 **Cómo se explica en la clase [B19-C01](../programa/clases/B19/B19-C01-priors-fisicamente-informados/CLASE.md):**
- Halla `a` y `b` del prior Gamma y su tamaño de muestra equivalente.
- 🎯 **Por qué importa:** Un contador de partículas a bordo de un CubeSat registra 3 eventos en 1 hora. ¿Cuál es la tasa verdadera `λ`, en eventos por hora?

📘 **Dónde se aprende** (1 clase): [B19-C01 · Priors físicamente informados](../programa/clases/B19/B19-C01-priors-fisicamente-informados/CLASE.md).

### Tamaño de pixel en el objeto (GSD)

- Punto ciego: punto que ninguna cámara ve. Tamaño de pixel en el objeto (GSD): `2 d tan(θ)/N`.

💡 **Cómo se explica en la clase [B101-C09](../programa/clases/B101/B101-C09-coordinacion-visual-y-camaras-en-operaciones-con-manipulador/CLASE.md):**
- Con 1 920 pixeles y 60° de campo, el tamaño de pixel en el objeto `2 d tan 30°/1 920` es 0,601 mm a 1 m; 1,203 mm a 2 m; 3,007 mm a 5 m y 6,014 mm a 10 m.
- Calcular el tamaño de pixel en el objeto y el ángulo de triangulación entre cámaras.
- 🎯 **Por qué importa:** Si el operador no ve el punto de contacto, depende de la imaginación. La decisión central: ¿qué cámaras necesito y dónde para que la zona de trabajo se vea, con qué resolución y sin puntos ciegos críticos?

📘 **Dónde se aprende** (1 clase): [B101-C09 · Coordinación visual y cámaras en operaciones con manipulador](../programa/clases/B101/B101-C09-coordinacion-visual-y-camaras-en-operaciones-con-manipulador/CLASE.md).

### Tamaño del efecto

- El tamaño del efecto `d` es la diferencia que quieres poder detectar, medida en unidades de la desviación típica `σ`.
- El tamaño del efecto `d = (m₂ − m₁)/s_p` es la diferencia de medias en unidades de desviación típica combinada.
- El tamaño del efecto `d = diferencia media / DE de la diferencia`.

💡 **Cómo se explica en la clase [B20-C02](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md):**
- Paso 3 · Efecto y tamaño de muestra. El menor efecto que importa: `d = 0,5` (media de `Δ` igual a media desviación típica).
- 🎯 **Por qué importa:** Un grupo mide cinco variantes razonables de un mismo análisis y publica la que da «un resultado significativo». Nadie mintió con un número, y sin embargo el resultado ya no significa lo que dice.

📘 **Dónde se aprende** (3 clases): [B20-C02 · Diseño de un plan de análisis y preregistro](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md); [B105-C20 · Diseño de protocolo médico simulado](../programa/clases/B105/B105-C20-diseno-de-protocolo-medico-simulado/CLASE.md); [B113-C05 · Intervenciones de apoyo y contramedidas conductuales](../programa/clases/B113/B113-C05-intervenciones-de-apoyo-y-contramedidas-conductuales/CLASE.md).

### Tamaño del píxel

- La distancia focal `f` del objetivo (mm) y el tamaño del píxel `p` (µm) fijan la escala de placa: `escala = 206 265 · p / f` en segundos de arco por píxel (con `p` en mm).

🎯 **Por qué importa (clase B08-C19):** Un teléfono o una cámara réflex puede captar la Vía Láctea o la Luna con detalle, pero una exposición demasiado larga convierte las estrellas en rayas. La pregunta motivadora: ¿cuánto puedo exponer y con qué focal para obtener estrellas puntuales, y qué debo anotar para que la foto sirva como dato?

📘 **Dónde se aprende** (1 clase): [B08-C19 · Fotografía astronómica elemental](../programa/clases/B08/B08-C19-fotografia-astronomica-elemental/CLASE.md).

### Tamaño efectivo de muestra

- El tamaño efectivo de muestra es `ESS = 1/Σ w_i²`: vale `N` con pesos uniformes y 1 con un solo peso no nulo.
- El tamaño efectivo de muestra `ESS = M n/(1 + 2 Σ ρ_t)` donde `ρ_t` es la autocorrelación a retardo `t`.

💡 **Cómo se explica en la clase [B15-C18](../programa/clases/B15/B15-C18-filtros-de-particulas-iniciales/CLASE.md):**
- Calcular el tamaño efectivo de muestra y decidir cuándo remuestrear.
- 🎯 **Por qué importa:** Un sensor mide la distancia oblicua a un objeto que pasa junto a él. Cuando el objeto está justo frente al sensor, un pequeño cambio de posición casi no cambia la distancia: la medida no distingue bien un lado del otro, y la incertidumbre de la posición deja de ser una campana.

📘 **Dónde se aprende** (2 clases): [B15-C18 · Filtros de partículas iniciales](../programa/clases/B15/B15-C18-filtros-de-particulas-iniciales/CLASE.md); [B19-C04 · Diagnóstico de convergencia de cadenas](../programa/clases/B19/B19-C04-diagnostico-de-convergencia-de-cadenas/CLASE.md).

### Tamaño físico

- Un tamaño angular `θ` es el ángulo que un objeto ocupa en el cielo, y el tamaño físico `s` es su longitud real.

💡 **Cómo se explica en la clase [B01-C03](../programa/clases/B01/B01-C03-objetos-celestes-y-sus-diferencias/CLASE.md):**
- Pasar de un tamaño angular y una distancia a un tamaño físico, y usarlo para decidir qué clase de objeto es.
- Calcula su tamaño físico si está a 43 Mpc y a 1,3 pc, y clasifícala en cada caso.
- 🎯 **Por qué importa:** En 2006 la Asamblea General de la Unión Astronómica Internacional votó una definición de planeta y, desde entonces, Plutón dejó de contarse como el noveno planeta. Muchas personas sintieron que «se había cambiado la realidad».

📘 **Dónde se aprende** (1 clase): [B01-C03 · Objetos celestes y sus diferencias](../programa/clases/B01/B01-C03-objetos-celestes-y-sus-diferencias/CLASE.md).

### Tamaño mínimo

- El tamaño mínimo es `n + 1`.

💡 **Cómo se explica en la clase [B88-C39](../programa/clases/B88/B88-C39-normas-de-aseguramiento-de-software-ecss-do-178c/CLASE.md):**
- Hallar el tamaño mínimo de un conjunto MC/DC.
- Ejercicio 11 · transferencia. Transferencia. ¿Cuál es el valor de calcular el tamaño mínimo?
- 🎯 **Por qué importa:** Elegir el nivel de cobertura determina el esfuerzo de prueba. La decisión central: ¿qué cobertura piden los distintos niveles y cuánto cuesta cada una en pruebas?

📘 **Dónde se aprende** (1 clase): [B88-C39 · Normas de aseguramiento de software (ECSS, DO-178C)](../programa/clases/B88/B88-C39-normas-de-aseguramiento-de-software-ecss-do-178c/CLASE.md).

### Tamaño mínimo de completitud

- El tamaño mínimo de completitud `D_min` es el diámetro a partir del cual el catálogo detecta casi todas las rocas.

💡 **Cómo se explica en la clase [B103-C06](../programa/clases/B103/B103-C06-deteccion-y-catalogacion-de-rocas-en-imagenes-de-superficie/CLASE.md):**
- Ajustar `N(>D) ∝ D^−b` por máxima verosimilitud sobre un tamaño mínimo de completitud, con incertidumbre y bootstrap.
- 🎯 **Por qué importa:** Un catálogo de rocas es incompleto justo donde hay más rocas: las pequeñas. Ajustar una ley de potencias con todas las detecciones da un exponente sesgado.

📘 **Dónde se aprende** (1 clase): [B103-C06 · Detección y catalogación de rocas en imágenes de superficie](../programa/clases/B103/B103-C06-deteccion-y-catalogacion-de-rocas-en-imagenes-de-superficie/CLASE.md).

### Tamaño muestral efectivo

- El tamaño muestral efectivo `ESS = (Σ hᵢwᵢ)²/Σ (hᵢwᵢ)²` mide a cuántas muestras iguales equivale el conjunto ponderado; es `N` si todos los pesos son iguales y vale 1 si uno solo domina.
- El tiempo de autocorrelación integrado `τ = 1 + 2 Σ_{t≥1} ρ_t` mide cuántos pasos equivalen a una muestra independiente; el tamaño muestral efectivo es `ESS = N/τ`.

💡 **Cómo se explica en la clase [B12-C15](../programa/clases/B12/B12-C15-muestreo-de-importancia/CLASE.md):**
- *Descripción textual:* se elige una propuesta con masa en la región rara; se sortea de ella; cada muestra recibe el peso `p/q`; el estimador es la media del indicador del suceso por el peso; se calcula su error típico y el tamaño muestral efectivo.
- Calcular el tamaño muestral efectivo y la reducción de varianza.
- 🎯 **Por qué importa:** Los sucesos que más interesan en seguridad espacial —un error de aproximación fuera de límites, una falla simultánea, una colisión— son raros por diseño. Un Monte Carlo simple puede pasar millones de ensayos sin ver un solo acierto y reportar «cero», que no es una estimación útil.

📘 **Dónde se aprende** (2 clases): [B12-C15 · Muestreo de importancia](../programa/clases/B12/B12-C15-muestreo-de-importancia/CLASE.md); [B12-C23 · Diagnóstico de convergencia y reproducibilidad de cadenas MCMC](../programa/clases/B12/B12-C23-diagnostico-de-convergencia-y-reproducibilidad-de-cadenas-mcmc/CLASE.md).

### Tamaños

- La escala de distancias y la de tamaños pueden ser distintas en un modelo, pero entonces hay que declararlo.

💡 **Cómo se explica en la clase [B01-C13](../programa/clases/B01/B01-C13-sistema-solar-como-sistema-fisico/CLASE.md):**
- Entonces un tamaño `L` en km se vuelve `L/149 597 870,7` m.
- Por eso los dibujos escolares cambian la escala de tamaños y la de distancias, y deben decirlo.
- ⚠️ **Error frecuente:** Mezclar la escala de tamaños con la de distancias. Ejercicio 9.
- 🎯 **Por qué importa:** Se dice que el sistema solar «está vacío», y es verdad en un sentido preciso: si el Sol midiera 9 mm, la Tierra sería un grano de 0,085 mm a un metro de distancia, y la estrella más cercana quedaría a más de 260 km. Pero esa imagen solo se entiende si la construyes tú con números.

📘 **Dónde se aprende** (1 clase): [B01-C13 · Sistema solar como sistema físico](../programa/clases/B01/B01-C13-sistema-solar-como-sistema-fisico/CLASE.md).

### Tangencial

- El foco tangencial está en el plano del campo; el sagital, perpendicular a él.
- La dirección tangencial `t̂ = n × r̂` da el sentido del movimiento en cada extremo.

💡 **Cómo se explica en la clase [B50-C07](../programa/clases/B50/B50-C07-curvatura-de-campo-y-aplanadores/CLASE.md):**
- Calcular los focos tangencial y sagital de un espejo esférico fuera de eje.
- ⚠️ **Error frecuente:** Olvidar que el foco sagital y el tangencial difieren. Se corrige con 8.1.
- 🎯 **Por qué importa:** Un detector plano mal enfocado en el borde pierde resolución: hay que decidir si se acepta, se curva el detector o se agrega un aplanador. La decisión central: ¿cuánto se hunde el foco en el borde y qué lo corrige?

📘 **Dónde se aprende** (2 clases): [B50-C07 · Curvatura de campo y aplanadores](../programa/clases/B50/B50-C07-curvatura-de-campo-y-aplanadores/CLASE.md); [B82-C02 · Lambert de arco largo](../programa/clases/B82/B82-C02-lambert-de-arco-largo/CLASE.md).

### Tangente

- Si un punto de esa circunferencia está en la dirección que forma un ángulo `x` con el eje horizontal, medido en sentido antihorario, su coordenada horizontal es `cos x` y la vertical es `sen x`; la tangente es `tan x = sen x / cos x`.

💡 **Cómo se explica en la clase [B04-C06](../programa/clases/B04/B04-C06-identidades-trigonometricas/CLASE.md):**
- Calcular seno, coseno y tangente a partir del círculo unidad y de valores notables.
- 🎯 **Por qué importa:** Casi toda medición astronómica es un ángulo: la posición de una estrella respecto de otra, el tamaño aparente de la Luna, el desplazamiento por paralaje. Y casi todos esos ángulos son diminutos, de segundos de arco.

📘 **Dónde se aprende** (1 clase): [B04-C06 · Identidades trigonométricas](../programa/clases/B04/B04-C06-identidades-trigonometricas/CLASE.md).

### Tanque con membrana

- Número de Reynolds: régimen del flujo. Tanque con membrana: almacenamiento sin superficie libre, apto para microgravedad.

💡 **Cómo se explica en la clase [B106-C29](../programa/clases/B106/B106-C29-almacenamiento-y-distribucion-de-agua-potable-en-habitats/CLASE.md):**
- R["reserva V = n d D"] --> T["tanque con membrana de gas"]
- Calcular la presión de entrega de un tanque con membrana de gas.
- 🎯 **Por qué importa:** El agua tratada debe llegar a los puntos de uso con presión y con desinfectante residual suficiente. La decisión central: ¿qué reserva, qué diámetro de línea y cuánto tiempo puede almacenarse el agua antes de perder el residual?

📘 **Dónde se aprende** (1 clase): [B106-C29 · Almacenamiento y distribución de agua potable en hábitats](../programa/clases/B106/B106-C29-almacenamiento-y-distribucion-de-agua-potable-en-habitats/CLASE.md).

### TAP

- ADQL es el lenguaje de consultas astronómicas del IVOA y TAP el protocolo para enviarlas (S1).

💡 **Cómo se explica en la clase [B14-C18](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md):**
- Consultar en el servidor (TAP/ADQL) reduce lo transferido pero depende de la disponibilidad y del servicio.
- La Alianza Internacional del Observatorio Virtual (IVOA) define el Table Access Protocol (TAP), un protocolo de servicio para acceder a datos de tablas generales: catálogos astronómicos y tablas de bases de datos, con acceso a los metadatos y a los datos (S1).
- 🎯 **Por qué importa:** Un artículo usa «datos de un archivo público filtrados por paralaje y magnitud». Dos años después nadie puede repetir el filtro: el archivo se actualizó, los parámetros no se anotaron y la consulta no se guardó.

📘 **Dónde se aprende** (1 clase): [B14-C18 · Flujos de datos espaciales](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md).

### Taper

- Un taper reduce la iluminación hacia el borde.

💡 **Cómo se explica en la clase [B46-C04](../programa/clases/B46/B46-C04-diagramas-de-radiacion/CLASE.md):**
- Ejercicio 9 · transferencia. Transferencia. ¿Por qué los radiotelescopios iluminan con taper?
- Ejercicio 10 · transferencia. Transferencia. ¿Qué pierde el taper?
- 🎯 **Por qué importa:** Bajar los lóbulos laterales evita captar emisión de direcciones no deseadas, pero ensancha el haz y reduce la eficiencia. La decisión central: ¿qué iluminación equilibra resolución y rechazo de lóbulos?

📘 **Dónde se aprende** (1 clase): [B46-C04 · Diagramas de radiación](../programa/clases/B46/B46-C04-diagramas-de-radiacion/CLASE.md).

### Tardías

- Las fechas tempranas (ES, EF) salen del paso hacia adelante; las tardías (LS, LF), del paso hacia atrás.

💡 **Cómo se explica en la clase [B124-C16](../programa/clases/B124/B124-C16-planificacion-de-cronograma-y-entregables/CLASE.md):**
- Calcular fechas tempranas y tardías de una red de actividades.
- 🎯 **Por qué importa:** Un plazo prometido sin ruta crítica ni incertidumbre es una apuesta. La decisión central: ¿qué actividades controlan el plazo y con qué probabilidad se cumple?

📘 **Dónde se aprende** (1 clase): [B124-C16 · Planificación de cronograma y entregables](../programa/clases/B124/B124-C16-planificacion-de-cronograma-y-entregables/CLASE.md).

### Tarea

- Una tarea tiene duración y predecesoras.

💡 **Cómo se explica en la clase [B97-C13](../programa/clases/B97/B97-C13-ensamblaje-de-estructuras-en-orbita/CLASE.md):**
- Hacia adelante, el fin más tardío es `118` min; hacia atrás, el mayor camino desde cualquier tarea da el mismo valor (diferencia `0,00e+00` min).
- En cada paso se elige, entre las tareas listas, la de mayor camino restante y se asigna al robot que se libera antes.
- ⚠️ **Error frecuente:** Optimizar tareas fuera de la ruta crítica. No cambia el tiempo (ejercicio 6)
- 🎯 **Por qué importa:** Añadir robots no acorta el trabajo indefinidamente: hay un punto en que la ruta crítica manda. Conocerlo evita lanzar una flota de robots que quedan esperando.

📘 **Dónde se aprende** (1 clase): [B97-C13 · Ensamblaje de estructuras en órbita](../programa/clases/B97/B97-C13-ensamblaje-de-estructuras-en-orbita/CLASE.md).

### Tarjeta

- Una tarjeta es una línea de 80 caracteres `CLAVE = valor / comentario`.

💡 **Cómo se explica en la clase [B44-C19](../programa/clases/B44/B44-C19-formato-fits-y-metadatos/CLASE.md):**
- Se leen `12` tarjetas antes de `END`: `NAXIS1 = 40`, `NAXIS2 = 30`, `BITPIX = 16`, `EXPTIME = 30,0`.
- H["tarjetas de 80 caracteres"] --> B["relleno a 2880"]
- 🎯 **Por qué importa:** Un cuadro sin metadatos es un arreglo de números sin contexto. La decisión central: ¿qué debe llevar la cabecera para interpretar los datos?

📘 **Dónde se aprende** (1 clase): [B44-C19 · Formato FITS y metadatos](../programa/clases/B44/B44-C19-formato-fits-y-metadatos/CLASE.md).

### Tarjeta de cabecera

- La tarjeta de cabecera de 80 caracteres.

💡 **Cómo se explica en la clase [B51-C12](../programa/clases/B51/B51-C12-formatos-de-datos-vlbi-y-geodesicos/CLASE.md):**
- La cabecera de tarjetas ocupa 2880 bytes (un bloque) y las tarjetas se leen de vuelta (True).
- Construir y leer tarjetas de cabecera de 80 caracteres en bloques de 2880 bytes.
- 🎯 **Por qué importa:** La elección de bits y de formato fija cuánta sensibilidad se pierde y cuánto disco y red se necesitan. La decisión central: ¿cuántos bits por muestra, qué eficiencia se obtiene y cómo se empaqueta sin perder información?

📘 **Dónde se aprende** (1 clase): [B51-C12 · Formatos de datos VLBI y geodésicos](../programa/clases/B51/B51-C12-formatos-de-datos-vlbi-y-geodesicos/CLASE.md).

### Tarjetas

- Un encabezado es una lista de tarjetas (registros de 80 caracteres) con una palabra clave, un valor y un comentario.

💡 **Cómo se explica en la clase [B14-C06](../programa/clases/B14/B14-C06-formato-fits-y-encabezados/CLASE.md):**
- Los primeros nueve bytes son `SIMPLE =`; el bloque de encabezado se parte en 36 tarjetas de 80 bytes y hay exactamente una tarjeta `END`, en la posición 24.
- Las 12 tarjetas siguientes están rellenas con espacios (S2: las tarjetas sin información después de `END` se rellenan con espacios).
- 🎯 **Por qué importa:** Una imagen astronómica es una matriz de números, pero esos números no significan nada sin su encabezado: ¿qué unidad tienen?, ¿cuánto duró la exposición?, ¿a qué punto del cielo apunta el píxel central? Si el encabezado miente o se pierde, la imagen no sirve.

📘 **Dónde se aprende** (1 clase): [B14-C06 · Formato FITS y encabezados](../programa/clases/B14/B14-C06-formato-fits-y-encabezados/CLASE.md).

### Tasa

- Una tasa es un cociente de magnitudes de clases distintas (km/s).
- Una falsa alarma es una detección que no corresponde a ninguna fuente; su tasa es la fracción de píxeles (o el número por imagen) que superan el umbral solo por ruido.
- La tasa `R` es el número de fusiones por volumen y año.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C02](../programa/clases/B03/B03-C02-fracciones-y-razones-de-magnitudes/CLASE.md):**
- Distinguir una razón (adimensional) de una tasa (con unidades, como km/s).
- 🎯 **Por qué importa:** Una cifra aislada como «69 911 km» no dice si Júpiter es grande o pequeño. Una razón sí: Júpiter tiene un radio unas 11 veces el terrestre.

📘 **Dónde se aprende** (9 clases): [B03-C02 · Fracciones y razones de magnitudes](../programa/clases/B03/B03-C02-fracciones-y-razones-de-magnitudes/CLASE.md); [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B28-C07 · Fuentes compactas binarias](../programa/clases/B28/B28-C07-fuentes-compactas-binarias/CLASE.md); [B28-C11 · Coincidencias entre observatorios](../programa/clases/B28/B28-C11-coincidencias-entre-observatorios/CLASE.md); [B51-C11 · Búsqueda de franjas VLBI: ajuste de retardo y tasa](../programa/clases/B51/B51-C11-busqueda-de-franjas-vlbi-ajuste-de-retardo-y-tasa/CLASE.md); [B105-C10 · Respuesta inmune](../programa/clases/B105/B105-C10-respuesta-inmune/CLASE.md) y 3 más.

### Tasa base

- La tasa base es la fracción de aptos.

💡 **Cómo se explica en la clase [B104-C03](../programa/clases/B104/B104-C03-seleccion-y-aptitud/CLASE.md):**
- La tasa base baja manda: un resultado «positivo» sigue siendo improbable de ser realmente apto.
- Aplicar el teorema de Bayes con la tasa base de aptos.
- ⚠️ **Error frecuente:** Olvidar la tasa base. Aplica Bayes (8.4).
- 🎯 **Por qué importa:** Si una prueba tiene ruido, ¿cuántos de los elegidos serán de verdad aptos? La decisión central: ¿cuánto ruido tolera un embudo antes de que la elección se parezca a un sorteo?

📘 **Dónde se aprende** (1 clase): [B104-C03 · Selección y aptitud](../programa/clases/B104/B104-C03-seleccion-y-aptitud/CLASE.md).

### Tasa bruta

- La tasa bruta es `píxeles × líneas/s × bits × bandas`.

💡 **Cómo se explica en la clase [B83-C11](../programa/clases/B83/B83-C11-presupuestos-de-datos/CLASE.md):**
- La tasa bruta es `6000 × 1396,6 × 12 × 4 = 402,22 Mbit/s`.
- C["Camara: pixeles, bits, bandas"] --> B["Tasa bruta"]
- 🎯 **Por qué importa:** Un satélite que produce más datos de los que puede bajar los pierde o se satura. La decisión central: ¿cabe todo lo que se produce en los minutos de contacto, y qué tamaño de registrador cubre el peor hueco?

📘 **Dónde se aprende** (1 clase): [B83-C11 · Presupuestos de datos](../programa/clases/B83/B83-C11-presupuestos-de-datos/CLASE.md).

### Tasa C

- La tasa C es la corriente dividida por la capacidad.

💡 **Cómo se explica en la clase [B86-C06](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md):**
- Ejercicio 4 · autónomo. Tasa C de `3 A` en `9 Ah`.
- 🎯 **Por qué importa:** Cargar más rápido reduce el tiempo pero eleva el calor y la tensión sobre la celda; cargar más lento puede no completar el ciclo antes del siguiente eclipse. El perfil de carga decide si la batería vuelve a su estado de carga en cada órbita.

📘 **Dónde se aprende** (1 clase): [B86-C06 · Gestión de carga](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md).

### Tasa de aceptación

- La tasa de aceptación es la fracción de propuestas aceptadas.
- La tasa de aceptación es la fracción de validaciones simuladas que cumplen el criterio.

💡 **Cómo se explica en la clase [B12-C13](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md):**
- Resultado: tasa de aceptación `0,628`; media `3,7617` (exacta `3,7624`); varianza `0,3746` (exacta `0,3725`); intervalo 95 % `[2,661; 5,052]` (exacto `[2,662; 5,049]`).
- La tasa de aceptación global fue `0,628`.
- ⚠️ **Error frecuente:** Elegir el paso por la tasa de aceptación sola. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Una posterior de diez o veinte parámetros (órbita, calibración, ruido) no se puede tabular. Pero sí se pueden generar muestras que sigan su forma, aunque no se conozca su normalización.

📘 **Dónde se aprende** (2 clases): [B12-C13 · Cadenas de Markov y muestreo](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md); [B13-C20 · Validación de una cadena de medida](../programa/clases/B13/B13-C20-validacion-de-una-cadena-de-medida/CLASE.md).

### Tasa de acreción

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B27-C10](../programa/clases/B27/B27-C10-discos-de-acrecion/CLASE.md):**
- *Descripción textual:* la masa, la tasa de acreción y el borde interno dan el perfil de temperatura; integrándolo se obtiene la luminosidad, que equivale a una eficiencia fija por el borde.
- Un agujero de `10 M☉` con borde interno en `6 GM/c²` y luminosidad `0,1 L_Edd` tiene `L_Edd = 1,257 × 10³² W`, `L = 1,257 × 10³¹ W` y una tasa de acreción `Ṁ = 1,678 × 10¹⁵ kg/s = 2,66 × 10⁻⁸ M☉/año`.
- 🎯 **Por qué importa:** Un disco convierte hasta una fracción grande de `Ṁc²` en luz; su temperatura, que baja hacia fuera, decide en qué banda se ve (rayos X en un agujero estelar, ultravioleta en uno supermasivo). La decisión central: ¿cuánto vale la temperatura en cada radio y qué luminosidad produce una tasa de acreción dada?

📘 **Dónde se aprende** (1 clase): [B27-C10 · Discos de acreción](../programa/clases/B27/B27-C10-discos-de-acrecion/CLASE.md).

### Tasa de cambio instantánea

- La tasa de cambio instantánea es la derivada interpretada con unidades.

🎯 **Por qué importa (clase B09-C03):** Casi toda cantidad en ciencias espaciales cambia con el tiempo o la posición: la altura de un cohete, la fase de una estrella variable, el brillo de un cometa. Lo que se quiere saber suele ser con qué rapidez cambia, y en qué instante deja de crecer.

📘 **Dónde se aprende** (1 clase): [B09-C03 · Derivada como tasa de cambio](../programa/clases/B09/B09-C03-derivada-como-tasa-de-cambio/CLASE.md).

### Tasa de cobertura

- La tasa de cobertura es franja por velocidad sobre el suelo.

💡 **Cómo se explica en la clase [B97-C01](../programa/clases/B97/B97-C01-robots-rover-y-orbitadores/CLASE.md):**
- *Descripción textual:* de la gravedad y el radio se obtiene `GM`, de ahí la órbita y la tasa de cobertura; de la velocidad máxima y el uso sale el recorrido diario; ambas se comparan.
- Calcular la tasa de cobertura de una cámara de franja `w`.
- 🎯 **Por qué importa:** Elegir entre «ir con un rover» y «mirar desde órbita» es la primera decisión de una misión robótica, y se toma con órdenes de magnitud. Sin ellos, se prometen traslados que tardan meses o coberturas que una órbita no entrega.

📘 **Dónde se aprende** (1 clase): [B97-C01 · Robots rover y orbitadores](../programa/clases/B97/B97-C01-robots-rover-y-orbitadores/CLASE.md).

### Tasa de código

- La tasa de código `r` (1/3, 1/2 o 2/3) es la de un código convolucional concatenado con el modulador (SCPPM).

💡 **Cómo se explica en la clase [B92-C06](../programa/clases/B92/B92-C06-modulacion-y-codificacion-en-enlaces-opticos/CLASE.md):**
- *Descripción textual:* un bloque de información se codifica en `15120` símbolos de código, se agrupan en símbolos PPM, se antepone el CSM y cada símbolo ocupa `1,25 M` ranuras; la tasa es `k` entre la duración.
- Con ranuras de `1 ns`, PPM-16 y código de tasa `1/2`, el bloque de `7526` bits de información ocupa `75 920` ranuras y da `99,131 Mbps`; con orden 256 la tasa baja a `12,339 Mbps` y la potencia de pico sube a `320` veces la media.
- 🎯 **Por qué importa:** En un canal con pocos fotones, la eficiencia es bits por fotón, no bits por hercio. La decisión central: ¿qué orden PPM y qué tasa de código elegir para equilibrar tasa de información, fotones por bit y potencia de pico?

📘 **Dónde se aprende** (1 clase): [B92-C06 · Modulación y codificación en enlaces ópticos](../programa/clases/B92/B92-C06-modulacion-y-codificacion-en-enlaces-opticos/CLASE.md).

### Tasa de conteo

- La tasa de conteo `λ` es el número medio de eventos por unidad de tiempo.

🎯 **Por qué importa (clase B09-C10):** Un detector cuenta fotones que llegan al azar. Cuánto hay que esperar, en promedio, entre uno y el siguiente, y cuánto varía esa espera, decide el tiempo de exposición, el tiempo muerto aceptable y el ruido.

📘 **Dónde se aprende** (1 clase): [B09-C10 · Integración por partes](../programa/clases/B09/B09-C10-integracion-por-partes/CLASE.md).

### Tasa de costo

- Reemplazo por edad: se cambia a las `T` horas o en la falla. Tasa de costo: costo esperado entre tiempo esperado.

🎯 **Por qué importa (clase B48-C14):** Reemplazar muy pronto desperdicia vida útil; muy tarde, produce fallas caras. La decisión central: ¿cada cuántas horas conviene reemplazar?

📘 **Dónde se aprende** (1 clase): [B48-C14 · Mantenimiento preventivo](../programa/clases/B48/B48-C14-mantenimiento-preventivo/CLASE.md).

### Tasa de crecimiento

- La tasa de crecimiento `γ` es la parte imaginaria de `ω`.

🎯 **Por qué importa (clase B35-C03):** Las inestabilidades limitan los equilibrios y convierten energía libre en turbulencia. La decisión central: ¿para qué número de onda y para qué cizalladura crece la perturbación y cuánto?

📘 **Dónde se aprende** (1 clase): [B35-C03 · Inestabilidades de plasma: cinéticas y de fluido](../programa/clases/B35/B35-C03-inestabilidades-de-plasma-cineticas-y-de-fluido/CLASE.md).

### Tasa de cumplimiento

- La tasa de cumplimiento es la fracción de casos que cumplen.
- Una tasa de cumplimiento es una proporción.

💡 **Cómo se explica en la clase [B87-C19](../programa/clases/B87/B87-C19-verificacion-de-ley-de-control/CLASE.md):**
- Montar un Monte Carlo con inercia y ruido inciertos y calcular la tasa de cumplimiento.
- La evidencia es la matriz de verificación con márgenes y tasa de cumplimiento del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Una ley que funciona en el caso nominal puede fallar con un retardo o con una inercia distinta. La decisión central: ¿cuánto retardo e incertidumbre tolera y con qué tasa de cumplimiento se cumple el requisito?

📘 **Dónde se aprende** (2 clases): [B87-C19 · Verificación de ley de control](../programa/clases/B87/B87-C19-verificacion-de-ley-de-control/CLASE.md); [B118-C19 · Sostenibilidad y gobernanza orbital](../programa/clases/B118/B118-C19-sostenibilidad-y-gobernanza-orbital/CLASE.md).

### Tasa de datos

- Recursión de Lindley: `W_{n+1} = máx(0, W_n + S − A)`. Tasa de datos: bytes por segundo.

💡 **Cómo se explica en la clase [B48-C16](../programa/clases/B48/B48-C16-procesamiento-de-datos-en-linea/CLASE.md):**
- Calcular la tasa de datos de una cámara.
- Ejercicio 12. Integrador. Elabora tu *ficha del procesamiento en línea*: tasa de datos, ocupación, espera y límites.
- 🎯 **Por qué importa:** Si la reducción no sigue el ritmo, se acumulan cuadros y el resultado llega tarde. La decisión central: ¿hasta qué ocupación del procesador es tolerable la espera?

📘 **Dónde se aprende** (2 clases): [B48-C16 · Procesamiento de datos en línea](../programa/clases/B48/B48-C16-procesamiento-de-datos-en-linea/CLASE.md); [B51-C12 · Formatos de datos VLBI y geodésicos](../programa/clases/B51/B51-C12-formatos-de-datos-vlbi-y-geodesicos/CLASE.md).

### Tasa de decaimiento

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B40-C02):** Sin recalentamiento no habría universo caliente. La decisión central: ¿cuándo domina la radiación y qué temperatura alcanza?

📘 **Dónde se aprende** (1 clase): [B40-C02 · Recalentamiento y transición a la era de radiación](../programa/clases/B40/B40-C02-recalentamiento-y-transicion-a-la-era-de-radiacion/CLASE.md).

### Tasa de deposición

- La tasa de deposición es kg impresos por hora.

💡 **Cómo se explica en la clase [B97-C15](../programa/clases/B97/B97-C15-impresion-3d-espacial/CLASE.md):**
- *Descripción textual:* el calor específico y la fracción fundida dan la energía por kg; con la potencia útil se obtiene la tasa de deposición y el tiempo de impresión.
- Calcular la tasa de deposición a partir de la potencia útil y el acoplamiento.
- 🎯 **Por qué importa:** La impresión 3D parece barata en masa (se usa material local), pero cuesta energía y tiempo. Sin un presupuesto, no se sabe si la fuente de energía alcanza ni cuántas horas se necesitan para un muro.

📘 **Dónde se aprende** (1 clase): [B97-C15 · Impresión 3D espacial](../programa/clases/B97/B97-C15-impresion-3d-espacial/CLASE.md).

### Tasa de desorción

- La tasa de desorción `k_d = ν exp(−E_d/T)`.

💡 **Cómo se explica en la clase [B55-C07](../programa/clases/B55/B55-C07-catalisis-en-superficies/CLASE.md):**
- *Descripción textual:* la temperatura fija las tasas de salto y desorción; la ventana de formación se da cuando el átomo escanea el grano antes de desorberse y antes de que lleguen otros.
- Calcular tasas de salto y desorción de tipo Arrhenius.
- 🎯 **Por qué importa:** En fase gaseosa dos átomos de H casi nunca forman H₂ al chocar (no pueden disipar la energía), y sin embargo el H₂ es la molécula más abundante: se forma en la superficie de los granos. La decisión central: ¿en qué intervalo de temperatura un grano puede formar H₂, y qué lo limita por debajo y por encima?

📘 **Dónde se aprende** (1 clase): [B55-C07 · Catálisis en superficies](../programa/clases/B55/B55-C07-catalisis-en-superficies/CLASE.md).

### Tasa de detección

- La tasa de falsa alarma (FPR) es la fracción de ventanas sin evento con alerta; la tasa de detección (TPR), la de ventanas con evento con alerta.

💡 **Cómo se explica en la clase [B57-C34](../programa/clases/B57/B57-C34-alertas-tempranas-y-etica-en-el-monitoreo-de-desastres/CLASE.md):**
- Calcular las tasas de falsa alarma y de detección de una regla de umbral.
- El script [alertas.py](alertas.py) calcula el umbral óptimo con costos asimétricos, las tasas de detección y falsa alarma, el valor predictivo y la carga anual de falsas alarmas (comprueba el umbral numérico frente al analítico (0,01) y el PPV simulado frente al analítico (5 %)).
- 🎯 **Por qué importa:** Un detector excelente puede producir una mayoría de falsas alarmas si el evento es raro, y las alertas repetidas y falsas se ignoran. La decisión central: ¿qué umbral y qué comunicación equilibran el costo de omitir y el de alarmar en falso, y quién decide?

📘 **Dónde se aprende** (1 clase): [B57-C34 · Alertas tempranas y ética en el monitoreo de desastres](../programa/clases/B57/B57-C34-alertas-tempranas-y-etica-en-el-monitoreo-de-desastres/CLASE.md).

### Tasa de diseño

- La tasa de diseño es la que cumple un requisito de misión.

💡 **Cómo se explica en la clase [B72-C04](../programa/clases/B72/B72-C04-precesion-del-nodo-orbital/CLASE.md):**
- *Descripción textual:* la tasa depende de J2, del movimiento medio y de `cos i`; se tabula para el diseño y se verifica con el promedio numérico de Gauss.
- Tasa del nodo [deg/dia], e = 0 (tabla de diseno)
- 🎯 **Por qué importa:** El nodo decide a qué hora local pasa un satélite sobre un lugar y cuándo su plano apunta al Sol. La decisión central: ¿qué altitud e inclinación hacen que el nodo avance o retroceda lo que necesita la misión?

📘 **Dónde se aprende** (1 clase): [B72-C04 · Precesión del nodo orbital](../programa/clases/B72/B72-C04-precesion-del-nodo-orbital/CLASE.md).

### Tasa de Doppler

- La tasa de Doppler `ḟ_D` es su derivada.

💡 **Cómo se explica en la clase [B89-C15](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md):**
- FD --> TASA["tasa de Doppler en el TCA"]
- *Descripción textual:* la geometría da la velocidad radial; con ella se calcula el Doppler, su tasa en el TCA (de donde se estima la distancia mínima) y el Doppler de ida y vuelta con el transpondedor.
- 🎯 **Por qué importa:** El Doppler es la medida básica de rastreo: se usa para determinar la órbita y obliga a diseñar los lazos de portadora y los planes de frecuencia. La decisión central: ¿cuánto se desplaza la frecuencia durante una pasada y qué información de la órbita contiene?

📘 **Dónde se aprende** (1 clase): [B89-C15 · Rastreo y Doppler](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md).

### Tasa de dosis

- La tasa de dosis sintética es `D(r) = D₀ (R_J/r)³`.
- El umbral es la dosis por debajo de la cual no se observa el efecto; tasa de dosis es la dosis por tiempo.

💡 **Cómo se explica en la clase [B75-C28](../programa/clases/B75/B75-C28-restricciones-de-radiacion-en-trayectorias/CLASE.md):**
- *Descripción textual:* La órbita da `h`, `p` y el periodo; con la tasa sintética la integral analítica da la dosis por órbita; el blindaje y el límite dan el número de órbitas posibles.
- Descripción larga: la dosis por órbita cae con el periapsis, pero no tanto como la tasa instantánea, porque la nave pasa más tiempo lejos.
- 🎯 **Por qué importa:** Una trayectoria es también un perfil de exposición. La decisión central: ¿cuánta dosis acumula una nave por órbita y cuántas órbitas aguanta, según el periapsis y el blindaje?

📘 **Dónde se aprende** (2 clases): [B75-C28 · Restricciones de radiación en trayectorias](../programa/clases/B75/B75-C28-restricciones-de-radiacion-en-trayectorias/CLASE.md); [B112-C03 · Efectos agudos de la radiación](../programa/clases/B112/B112-C03-efectos-agudos-de-la-radiacion/CLASE.md).

### Tasa de eliminación

- La tasa de eliminación `λ` suma renovación, filtración e inactivación (1/h).

💡 **Cómo se explica en la clase [B110-C02](../programa/clases/B110/B110-C02-protocolos-operativos-de-aislamiento-de-un-tripulante-enfermo-o-contaminado/CLASE.md):**
- Calcular la tasa de eliminación de aire de una cabina y su constante de tiempo.
- 🎯 **Por qué importa:** Aislar a alguien en una cabina cuesta espacio, tiempo y trabajo de la tripulación; no aislar cuesta exposición. La decisión central: ¿cuánta exposición evita cada barrera y con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B110-C02 · Protocolos operativos de aislamiento de un tripulante enfermo o contaminado](../programa/clases/B110/B110-C02-protocolos-operativos-de-aislamiento-de-un-tripulante-enfermo-o-contaminado/CLASE.md).

### Tasa de elongación

- La tasa de elongación es el cambio de `X_max` por década.

💡 **Cómo se explica en la clase [B31-C13](../programa/clases/B31/B31-C13-rayos-cosmicos-y-cascadas/CLASE.md):**
- Tasa de elongación: `85,20 g/cm²` por década (`λ_r ln 10`).
- Calcular `X_max = λ_r ln(E₀/ξ_c)` y la tasa de elongación.
- 🎯 **Por qué importa:** La energía y la composición de un rayo cósmico se infieren de la forma de su cascada, y el fondo de microondas limita la energía que llega. La decisión central: ¿qué profundidad y tamaño tiene una cascada y a qué energía aparece un corte?

📘 **Dónde se aprende** (1 clase): [B31-C13 · Rayos cósmicos y cascadas](../programa/clases/B31/B31-C13-rayos-cosmicos-y-cascadas/CLASE.md).

### Tasa de error de símbolo

- La tasa de error de símbolo (*SER*) es la probabilidad de elegir una ranura equivocada.

💡 **Cómo se explica en la clase [B92-C05](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md):**
- *Descripción textual:* la ranura con pulso recibe señal y fondo, las otras solo fondo; el receptor elige la ranura de mayor conteo, de ahí sale el error de símbolo y los fotones necesarios; el tiempo muerto limita la tasa medible.
- Calcular la tasa de error de símbolo de un receptor PPM de conteo de fotones con fondo.
- 🎯 **Por qué importa:** Un detector de imagen integra luz durante milisegundos; uno de comunicaciones decide, en nanosegundos, en qué ranura llegó el pulso. La decisión central: ¿cuántos fotones hacen falta por símbolo y qué detector soporta la tasa de ranuras sin saturarse?

📘 **Dónde se aprende** (1 clase): [B92-C05 · Receptores y detectores para comunicaciones ópticas](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md).

### Tasa de error por familia

- La tasa de error por familia es la probabilidad de al menos un falso positivo en `k` pruebas.

💡 **Cómo se explica en la clase [B14-C23](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md):**
- Si exploras, etiquétalo exploratorio y, si haces 20 pruebas, corrige con Bonferroni o declara la tasa de error por familia: 64 % sin corregir.
- 🎯 **Por qué importa:** Tienes una curva de luz y muchas formas de analizarla: otro filtro, otra ventana, otro modelo, otra prueba. Si pruebas veinte y comunicas la que «sale», el resultado casi seguro parece significativo aunque no haya nada.

📘 **Dónde se aprende** (1 clase): [B14-C23 · Protocolo preregistrado de análisis](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md).

### Tasa de error por palabra

- Una tasa de error por palabra es la probabilidad de que una palabra se reciba mal.

💡 **Cómo se explica en la clase [B104-C08](../programa/clases/B104/B104-C08-comunicacion-de-tripulacion/CLASE.md):**
- Calcular la probabilidad de error de un mensaje con una tasa por palabra.
- 🎯 **Por qué importa:** A 1,28 s de la Luna aún se conversa; a más de 3 minutos de Marte ya no. La decisión central: ¿qué protocolo de mensajes usar cuando cada ida y vuelta cuesta minutos y un error cuesta caro?

📘 **Dónde se aprende** (1 clase): [B104-C08 · Comunicación de tripulación](../programa/clases/B104/B104-C08-comunicacion-de-tripulacion/CLASE.md).

### Tasa de eventos

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C14](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md):**
- Corrige eventos aislados sin reducir su tasa.
- 🎯 **Por qué importa:** El blindaje reduce la dosis hasta que el protón se detiene; los eventos de partícula simple, en cambio, son aleatorios. La decisión central: ¿qué espesor de blindaje y qué probabilidad de eventos son aceptables?

📘 **Dónde se aprende** (1 clase): [B47-C14 · Radiación y degradación](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md).

### Tasa de falla

- La tasa de falla `λ` es la probabilidad de falla por hora.
- La tasa de falla `λ` es la probabilidad de fallar por unidad de tiempo; el MTBF es `1/λ` con tasa constante.
- La tasa de falla `λ` es el número de fallas por hora.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B47-C19](../programa/clases/B47/B47-C19-mantenimiento-y-vida-util/CLASE.md):**
- Límite: tasa constante, fallas independientes.
- 🎯 **Por qué importa:** No sirve duplicar un equipo si otro componente falla antes. La decisión central: ¿qué recurso limita la vida de la misión y qué redundancia vale la pena?

📘 **Dónde se aprende** (5 clases): [B47-C19 · Mantenimiento y vida útil](../programa/clases/B47/B47-C19-mantenimiento-y-vida-util/CLASE.md); [B83-C22 · Análisis de modos y efectos de fallo (FMEA) en sistemas espaciales](../programa/clases/B83/B83-C22-analisis-de-modos-y-efectos-de-fallo-fmea-en-sistemas-espaciales/CLASE.md); [B86-C11 · Redundancia eléctrica](../programa/clases/B86/B86-C11-redundancia-electrica/CLASE.md); [B93-C04 · Análisis de confiabilidad de electrónica (MTBF y derating)](../programa/clases/B93/B93-C04-analisis-de-confiabilidad-de-electronica-mtbf-y-derating/CLASE.md); [B97-C12 · Robots de mantenimiento](../programa/clases/B97/B97-C12-robots-de-mantenimiento/CLASE.md).

### Tasa de falla λ

- Fiabilidad: probabilidad de funcionar durante la misión. Tasa de falla `λ`: fallas por hora.

💡 **Cómo se explica en la clase [B106-C18](../programa/clases/B106/B106-C18-fiabilidad-y-redundancia/CLASE.md):**
- *Descripción textual:* la tasa de falla da la fiabilidad de una unidad; la redundancia la mejora y la flota esperada de fallas fija los repuestos.
- Rotular que tasas de falla, β y conmutador son ilustrativos.
- 🎯 **Por qué importa:** Ningún equipo es perfecto y una misión larga no se puede reparar con repuestos de la Tierra. La decisión central: ¿qué configuración redundante y cuántos repuestos dan una probabilidad objetivo de cumplir la misión?

📘 **Dónde se aprende** (1 clase): [B106-C18 · Fiabilidad y redundancia](../programa/clases/B106/B106-C18-fiabilidad-y-redundancia/CLASE.md).

### Tasa de fallo

- La tasa de fallo `λ` es la probabilidad de fallo por año.
- La tasa de fallo es la probabilidad de fallar por unidad de tiempo.

💡 **Cómo se explica en la clase [B95-C02](../programa/clases/B95/B95-C02-componentes-comerciales-en-vuelo-seleccion-y-riesgo/CLASE.md):**
- *Descripción textual:* la dosis y la TID declarada dan un margen que se compara con el RDM; las tasas de fallo dan la supervivencia en serie, que mejora duplicando el eslabón más débil; ambos criterios alimentan la selección.
- Los valores de TID de los candidatos provienen de la tabla del informe de la NASA y son declarados por los fabricantes; la dosis, las tasas de fallo y el RDM son ilustrativos.
- 🎯 **Por qué importa:** Un componente comercial puede funcionar bien en tierra y degradarse o fallar en órbita. La decisión central: ¿qué componente comercial se puede usar en esta misión, con qué margen de radiación y con qué fiabilidad del conjunto?

📘 **Dónde se aprende** (2 clases): [B95-C02 · Componentes comerciales en vuelo: selección y riesgo](../programa/clases/B95/B95-C02-componentes-comerciales-en-vuelo-seleccion-y-riesgo/CLASE.md); [B127-C02 · Seguros en órbita](../programa/clases/B127/B127-C02-seguros-en-orbita/CLASE.md).

### Tasa de falsa alarma

- La tasa de falsa alarma es la probabilidad de marcar un píxel sin cambio; la de detección, la de marcar uno con cambio.
- La tasa de falsa alarma (FPR) es la fracción de ventanas sin evento con alerta; la tasa de detección (TPR), la de ventanas con evento con alerta.

💡 **Cómo se explica en la clase [B57-C27](../programa/clases/B57/B57-C27-deteccion-de-cambios-en-series-de-imagenes/CLASE.md):**
- Ejercicio 2 · con una pista. ¿Qué tasa de falsa alarma tiene `k = 3`?
- 🎯 **Por qué importa:** Un umbral bajo llena el mapa de falsas alarmas; uno alto deja pasar cambios reales. La decisión central: ¿qué umbral equilibra falsas alarmas y detecciones para el cambio que me interesa?

📘 **Dónde se aprende** (2 clases): [B57-C27 · Detección de cambios en series de imágenes](../programa/clases/B57/B57-C27-deteccion-de-cambios-en-series-de-imagenes/CLASE.md); [B57-C34 · Alertas tempranas y ética en el monitoreo de desastres](../programa/clases/B57/B57-C34-alertas-tempranas-y-etica-en-el-monitoreo-de-desastres/CLASE.md).

### Tasa de falsas alarmas

- La probabilidad de detección es `POD = a/(a+c)`; la tasa de falsas alarmas (probabilidad de detección falsa) `POFD = b/(b+d)`.
- La tasa de falsas alarmas (FAR) es el número de disparos por ruido por unidad de tiempo.
- La tasa de falsas alarmas es la probabilidad de rechazar una hipótesis cierta.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B28-C09](../programa/clases/B28/B28-C09-alertas-cientificas-en-tiempo-real/CLASE.md):**
- El umbral equilibra ambos y se calibra con la tasa de falsas alarmas que se tolera.
- GW150914 tuvo una tasa de falsas alarmas estimada menor que `1` por `203 000 años` (S2, resumen).
- 🎯 **Por qué importa:** Una alerta tardía pierde el evento; una alerta con muchas falsas alarmas agota a los observadores. La decisión central: ¿qué umbral produce una tasa de falsas alarmas aceptable y cuánto tarda la alerta en llegar?

📘 **Dónde se aprende** (4 clases): [B12-C24 · Métricas de habilidad (skill scores) de pronóstico](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md); [B28-C09 · Alertas científicas en tiempo real](../programa/clases/B28/B28-C09-alertas-cientificas-en-tiempo-real/CLASE.md); [B29-C08 · Falsos positivos de tránsito](../programa/clases/B29/B29-C08-falsos-positivos-de-transito/CLASE.md); [B105-C09 · Salud mental en aislamiento](../programa/clases/B105/B105-C09-salud-mental-en-aislamiento/CLASE.md).

### Tasa de falsos positivos

- La tasa de falsos positivos es la fracción de series limpias que la regla marca.
- La tasa de falsos positivos es `FP/(FP + TN)`.
- La sensibilidad `S` es `P(positivo | recurso)`; la tasa de falsos positivos `F`, `P(positivo | no recurso)`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C19](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md):**
- Medir por simulación la tasa de falsos positivos de una regla.
- Se calibra el umbral con datos limpios del propio sensor (simulación o histórico), se modela la distribución del ruido y se informa la tasa de falsos positivos.
- ⚠️ **Error frecuente:** Ignorar la tasa de falsos positivos. Se corrige con 8.3 y los ejercicios 4 y 11.
- 🎯 **Por qué importa:** Un dato aberrante puede ser un error del instrumento, una pérdida de sincronía o el primer indicio de un fenómeno real. Eliminarlo sin criterio esconde información; conservarlo sin revisar contamina el resultado.

📘 **Dónde se aprende** (4 clases): [B12-C19 · Detección de valores atípicos](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md); [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md); [B56-C15 · Falsos positivos de biofirmas](../programa/clases/B56/B56-C15-falsos-positivos-de-biofirmas/CLASE.md); [B67-C02 · Diseño de un programa de prospección por fases](../programa/clases/B67/B67-C02-diseno-de-un-programa-de-prospeccion-por-fases/CLASE.md).

### Tasa de fotodisociación

- La tasa de fotodisociación `k` (s⁻¹) es la probabilidad por segundo de que una molécula se rompa por absorber un fotón.

💡 **Cómo se explica en la clase [B55-C08](../programa/clases/B55/B55-C08-fotoquimica-cosmica/CLASE.md):**
- Heays, Bosman y van Dishoeck (2017) (S1) calculan en su resumen secciones eficaces y tasas de fotodisociación y fotoionización de unas 100 especies, con incertidumbres, y modelan la reducción por polvo y por apantallamiento; ninguna cifra suya se usa aquí.
- 🎯 **Por qué importa:** La luz ultravioleta del campo estelar destruye moléculas, y el polvo la apaga: por eso las moléculas sobreviven en el interior de las nubes y no en su superficie. La decisión central: ¿a qué profundidad de nube una molécula deja de ser destruida más rápido de lo que dura la nube?

📘 **Dónde se aprende** (1 clase): [B55-C08 · Fotoquímica cósmica](../programa/clases/B55/B55-C08-fotoquimica-cosmica/CLASE.md).

### Tasa de fotólisis

- La tasa de fotólisis `J = σ F e^{−τ}` es la probabilidad por segundo de romper una molécula.

💡 **Cómo se explica en la clase [B54-C10](../programa/clases/B54/B54-C10-fotoquimica-atmosferica/CLASE.md):**
- *Descripción textual:* el flujo, la densidad y la profundidad óptica determinan la producción; su máximo cae donde `τ = 1`, y de la tasa de fotólisis sale la vida fotoquímica.
- Calcular la tasa de fotólisis `J` y la vida `1/J`.
- 🎯 **Por qué importa:** La capa de producción fotoquímica explica por qué hay capas de ozono, ionosferas y neblinas a ciertas alturas. La pregunta motivadora: ¿a qué altura se rompen más moléculas y cómo cambia con el ángulo del Sol?

📘 **Dónde se aprende** (1 clase): [B54-C10 · Fotoquímica atmosférica](../programa/clases/B54/B54-C10-fotoquimica-atmosferica/CLASE.md).

### Tasa de fotones ionizantes

- La tasa de fotones ionizantes `Q` (en `s⁻¹`) es el número de fotones por segundo capaces de ionizar H (por encima de 13,6 eV).

💡 **Cómo se explica en la clase [B25-C05](../programa/clases/B25/B25-C05-regiones-de-formacion-estelar/CLASE.md):**
- Definir región HII, tasa de fotones ionizantes, recombinación, esfera de Strömgren y ley de Schmidt.
- 🎯 **Por qué importa:** Una galaxia no convierte todo su gas en estrellas a la vez: lo hace a un ritmo que puede medirse y comparar. Entender las regiones donde nacen las estrellas masivas permite reconocerlas desde lejos, y entender la relación entre gas y ritmo de formación permite saber cuánto tiempo puede una galaxia seguir formando estrellas.

📘 **Dónde se aprende** (1 clase): [B25-C05 · Regiones de formación estelar](../programa/clases/B25/B25-C05-regiones-de-formacion-estelar/CLASE.md).

### Tasa de franjas

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B51-C09](../programa/clases/B51/B51-C09-fringe-stopping-y-rotacion-de-fase-por-retardo-geometrico/CLASE.md):**
- Como un estroboscopio que se sincroniza con la rueda que gira: si la luz parpadea a la tasa de franjas, la rueda parece quieta y puedes promediar sin que se borre.
- Con `B = 1000` m, `δ = 30°` y `ν = 1,4` GHz, el retardo geométrico máximo es 2,8887 µs y la tasa de franjas en `H = 0` es -0,294911 Hz.
- ⚠️ **Error frecuente:** Confundir tasa de franjas con tasa de retardo. Difieren en el factor `ν`.
- 🎯 **Por qué importa:** Si se promedia sin detener las franjas, la señal se anula. La decisión central: ¿qué tasa de franjas tiene una fuente, cuánto se pierde al promediar y qué precisión pide el modelo?

📘 **Dónde se aprende** (1 clase): [B51-C09 · Fringe stopping y rotación de fase por retardo geométrico](../programa/clases/B51/B51-C09-fringe-stopping-y-rotacion-de-fase-por-retardo-geometrico/CLASE.md).

### Tasa de fuga

- La tasa de fuga es la pérdida de presión o de masa por unidad de tiempo.

💡 **Cómo se explica en la clase [B114-C02](../programa/clases/B114/B114-C02-deteccion-localizacion-y-respuesta-a-fugas-de-presion/CLASE.md):**
- Convertir `τ` en tasa de fuga (Pa/s y kg/día).
- La evidencia es el informe de fuga con tasa, origen e incertidumbre del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Una fuga pequeña no suena ni se ve, pero decide cuántos días quedan para actuar. La decisión central: ¿con qué rapidez pierde presión el hábitat y dónde está el origen?

📘 **Dónde se aprende** (1 clase): [B114-C02 · Detección, localización y respuesta a fugas de presión](../programa/clases/B114/B114-C02-deteccion-localizacion-y-respuesta-a-fugas-de-presion/CLASE.md).

### Tasa de habituación

- `k` es la tasa de habituación por exposición.

🎯 **Por qué importa (clase B113-C02):** Ninguna clase previa trata la respuesta emocional ante simulaciones de riesgo. La decisión central: ¿cuántas repeticiones de un escenario hacen falta para que el pico baje a un nivel de trabajo, y cuándo la repetición deja de ayudar?

📘 **Dónde se aprende** (1 clase): [B113-C02 · Ansiedad y respuesta emocional en escenarios simulados](../programa/clases/B113/B113-C02-ansiedad-y-respuesta-emocional-en-escenarios-simulados/CLASE.md).

### Tasa de llegada

- La tasa de llegada `λ` y la de servicio `μ` se miden en solicitudes por mes.

🎯 **Por qué importa (clase B119-C08):** C01 enuncia el art. VI como regla; esta clase lo convierte en un proceso con tiempos y cobertura, lo que ninguna clase del bloque hace.

📘 **Dónde se aprende** (1 clase): [B119-C08 · Autorización y supervisión de operadores](../programa/clases/B119/B119-C08-autorizacion-y-supervision-de-operadores/CLASE.md).

### Tasa de muestreo

- La tasa de muestreo es 10 Hz.

🎯 **Por qué importa (clase B87-C06):** Entre dos medidas de un sensor de vector, la actitud se propaga integrando el giroscopio, y esa integración se desvía. La decisión central: ¿cada cuánto hay que corregir con otro sensor, y qué parte de la deriva es ruido blanco y cuál sesgo?

📘 **Dónde se aprende** (1 clase): [B87-C06 · Giroscopios MEMS](../programa/clases/B87/B87-C06-giroscopios-mems/CLASE.md).

### Tasa de neutrones epitérmicos

- La tasa de neutrones epitérmicos baja donde el hidrógeno los modera.

💡 **Cómo se explica en la clase [B67-C07](../programa/clases/B67/B67-C07-sensores-para-volatiles-espectrometria-de-neutrones-y-de-masas/CLASE.md):**
- Modelar la tasa de neutrones epitérmicos como función decreciente de la abundancia de hidrógeno.
- 🎯 **Por qué importa:** Un sensor no mide «agua»: mide cuentas, y de ellas se infiere la abundancia con un modelo. La decisión central: ¿cuánto tiempo de medición y qué canales hacen falta para detectar y separar un volátil con la incertidumbre requerida?

📘 **Dónde se aprende** (1 clase): [B67-C07 · Sensores para volátiles: espectrometría de neutrones y de masas](../programa/clases/B67/B67-C07-sensores-para-volatiles-espectrometria-de-neutrones-y-de-masas/CLASE.md).

### Tasa de reacción

- La tasa de reacción `r` mide la rapidez del triple alfa por unidad de abundancia al cubo.

💡 **Cómo se explica en la clase [B24-C08](../programa/clases/B24/B24-C08-nucleosintesis-estelar/CLASE.md):**
- Red de reacciones con cientos de isótopos: la usan los códigos reales; exige tasas medidas y un integrador rígido (B11-C22).
- Ejercicio 7. Si `Y` se reduce a la mitad, ¿cuánto baja la tasa de reacción?
- 🎯 **Por qué importa:** El carbono de tu cuerpo, el oxígeno que respiras y el hierro de tus huesos se forjaron en estrellas. Entender cómo, y cuánta energía rinde cada etapa, explica por qué la vida de una estrella se acorta con cada combustible y por qué el hierro es el final de la cadena.

📘 **Dónde se aprende** (1 clase): [B24-C08 · Nucleosíntesis estelar](../programa/clases/B24/B24-C08-nucleosintesis-estelar/CLASE.md).

### Tasa de reconexión

- La tasa de reconexión `v_in/v_A`.

💡 **Cómo se explica en la clase [B30-C11](../programa/clases/B30/B30-C11-reconexion-magnetica/CLASE.md):**
- Descripción larga: la tasa cae como `S^(−1/2)` y el tiempo de reconexión crece en la misma proporción.
- Ejercicio 2 · con una pista. Tasa de reconexión con `S = 10⁸`.
- 🎯 **Por qué importa:** Las erupciones liberan en minutos una energía que el campo guardó durante mucho más tiempo, y el modelo más simple de reconexión es demasiado lento para eso. La decisión central: ¿qué tasa de reconexión hace falta y qué dice el modelo de Sweet–Parker?

📘 **Dónde se aprende** (1 clase): [B30-C11 · Reconexión magnética](../programa/clases/B30/B30-C11-reconexion-magnetica/CLASE.md).

### Tasa de remoción

- La tasa de remoción `λ` (1/h) es la fracción del contaminante que se elimina por hora.

💡 **Cómo se explica en la clase [B117-C02](../programa/clases/B117/B117-C02-contencion-de-riesgos-biologicos-y-quimicos-en-cabina/CLASE.md):**
- *Descripción textual:* la masa liberada y el volumen dan la concentración inicial; la tasa de remoción da el tiempo al límite; con dos compartimentos se verifica que la masa se conserve.
- Calcular la tasa de remoción `λ = η Q_s/V` de un depurador.
- 🎯 **Por qué importa:** Ninguna clase anterior trata la contención de riesgos biológicos o químicos. La decisión central: ¿conviene aislar el módulo donde ocurre el derrame o dejar que se diluya en toda la cabina?

📘 **Dónde se aprende** (1 clase): [B117-C02 · Contención de riesgos biológicos y químicos en cabina](../programa/clases/B117/B117-C02-contencion-de-riesgos-biologicos-y-quimicos-en-cabina/CLASE.md).

### Tasa de renovación

- La tasa de renovación en régimen es `N/L`.

🎯 **Por qué importa (clase B124-C11):** Una constelación puede ser técnicamente exitosa y económicamente inviable si la reposición se come el margen. La decisión central: ¿cuántos suscriptores se necesitan para cubrir la reposición y la operación, y qué tan sensible es eso a la vida útil?

📘 **Dónde se aprende** (1 clase): [B124-C11 · Sostenibilidad económica de constelaciones](../programa/clases/B124/B124-C11-sostenibilidad-economica-de-constelaciones/CLASE.md).

### Tasa de retorno

- La tasa de retorno `dM/dt ∝ t^{−5/3}`.

🎯 **Por qué importa (clase B27-C16):** Estos eventos iluminan agujeros negros inactivos y permiten estimar su masa. Gezari revisa 56 de ellos (S3, resumen).

📘 **Dónde se aprende** (1 clase): [B27-C16 · Eventos de disrupción por marea](../programa/clases/B27/B27-C16-eventos-de-disrupcion-por-marea/CLASE.md).

### Tasa de salto

- La tasa de salto `k_s = ν exp(−E_b/T)` es la frecuencia con que un átomo cambia de sitio.

💡 **Cómo se explica en la clase [B55-C07](../programa/clases/B55/B55-C07-catalisis-en-superficies/CLASE.md):**
- *Descripción textual:* la temperatura fija las tasas de salto y desorción; la ventana de formación se da cuando el átomo escanea el grano antes de desorberse y antes de que lleguen otros.
- Calcular tasas de salto y desorción de tipo Arrhenius.
- 🎯 **Por qué importa:** En fase gaseosa dos átomos de H casi nunca forman H₂ al chocar (no pueden disipar la energía), y sin embargo el H₂ es la molécula más abundante: se forma en la superficie de los granos. La decisión central: ¿en qué intervalo de temperatura un grano puede formar H₂, y qué lo limita por debajo y por encima?

📘 **Dónde se aprende** (1 clase): [B55-C07 · Catálisis en superficies](../programa/clases/B55/B55-C07-catalisis-en-superficies/CLASE.md).

### Tasa de símbolos

- La tasa de símbolos `Rs = Rb/(r·m)` es el número de símbolos por segundo, con `r` la tasa del código y `m` los bits por símbolo.

💡 **Cómo se explica en la clase [B89-C02](../programa/clases/B89/B89-C02-frecuencia-y-espectro-espacial/CLASE.md):**
- *Descripción textual:* la tasa de bits, el código y la modulación dan la tasa de símbolos; con el roll-off, el ancho ocupado; este decide cuántos canales caben y la capacidad de Shannon; el Doppler se suma por separado.
- Paso 1 · Tasa de símbolos. Con `Rb = 10 Mbit/s`, tasa 1/2 y QPSK: `Rs = 10/(0,5×2) = 10 Msímb/s`.
- ⚠️ **Error frecuente:** Confundir tasa de bits con tasa de símbolos. Se corrige con 8.1.
- 🎯 **Por qué importa:** Sin una idea cuantitativa del ancho de banda no se puede decidir cuántos enlaces caben en una banda ni cuánta tasa de datos es posible. La regulación (C19) trabaja con exactamente estas magnitudes.

📘 **Dónde se aprende** (1 clase): [B89-C02 · Frecuencia y espectro espacial](../programa/clases/B89/B89-C02-frecuencia-y-espectro-espacial/CLASE.md).

### Tasa de volteo

- La tasa de volteo `λ` es la frecuencia con que una celda se remueve.

💡 **Cómo se explica en la clase [B55-C14](../programa/clases/B55/B55-C14-quimica-de-regolitos/CLASE.md):**
- *Descripción textual:* la tasa de volteo da la fracción sin voltear y los tiempos; la mezcla de componentes se invierte con un sistema lineal cuya precisión depende del ruido.
- Una capa de 1 cm con tasa de volteo ilustrativa `λ = 1/10⁸ años` y tres componentes sintéticos (basáltico, de tierras altas y enriquecido) caracterizados por %MgO, %FeO y %Al₂O₃.
- 🎯 **Por qué importa:** El regolito es el suelo de un cuerpo sin atmósfera y su química depende de qué impactos lo removieron y de qué componentes lo formaron. La decisión central: ¿cuánto tiempo hace falta para que una capa se voltee y qué mezcla de componentes explica la composición medida?

📘 **Dónde se aprende** (1 clase): [B55-C14 · Química de regolitos](../programa/clases/B55/B55-C14-quimica-de-regolitos/CLASE.md).

### Tasa del código

- La tasa del código `r = k/n`.

💡 **Cómo se explica en la clase [B89-C09](../programa/clases/B89/B89-C09-codificacion-correctora-de-errores/CLASE.md):**
- La tasa del código es `223/255 = 0,8745`.
- Con BPSK y la BER de salida aproximada, el `Eb/N0` necesario para 10⁻⁵ pasa de `9,59 dB` sin código a `6,29 dB` con RS(255,223): ganancia de `3,29 dB`, descontada la pérdida de tasa.
- 🎯 **Por qué importa:** La codificación es la herramienta que permite cerrar enlaces de espacio profundo con potencias modestas: cada decibelio de ganancia de código equivale a una antena más grande o a más potencia. La decisión central: ¿cuánta redundancia añadir y cuánto `Eb/N0` se ahorra con ella?

📘 **Dónde se aprende** (1 clase): [B89-C09 · Codificación correctora de errores](../programa/clases/B89/B89-C09-codificacion-correctora-de-errores/CLASE.md).

### Tasa Doppler

- La tasa Doppler `Ka` es la pendiente de esa variación.

💡 **Cómo se explica en la clase [B69-C01](../programa/clases/B69/B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md):**
- Paso 2 · Tasa Doppler. `Ka = 2v²/(λR₀) = 2 × 7100² /(0,0555 × 850 000) = 2137,1 Hz/s`.
- Con λ = 0,0555 m, v = 7100 m/s, R₀ = 850 km y una antena de L = 12 m (todo ilustrativo), el tiempo de iluminación es `T = 0,5537 s`, la tasa Doppler `Ka = 2137,15 Hz/s` y el ancho de banda `Ba = 1183,3 Hz`.
- 🎯 **Por qué importa:** Sin el principio Doppler, la resolución en azimut de un radar quedaría fijada por el ancho del haz de la antena: a 850 km, una antena de 12 m (λ = 0,0555 m) iluminaría una franja de unos 3,9 km. La decisión central: ¿qué resolución obtiene el sistema, de qué depende y qué hay que muestrear para no perderla?

📘 **Dónde se aprende** (1 clase): [B69-C01 · Principio Doppler y resolución en azimut del SAR](../programa/clases/B69/B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md).

### Tasa máxima

- La tasa máxima es la que deja un margen dado: `R = 10^{(C/N₀ − (Eb/N₀)_req − M)/10}`.
- La tasa máxima con margen `M` es `R_b = 10^{(C/N₀ − (Eb/N₀)_req − M)/10}`.

💡 **Cómo se explica en la clase [B89-C20](../programa/clases/B89/B89-C20-diseno-de-red-de-comunicaciones-de-mision/CLASE.md):**
- FASE["fase: distancia, contacto"] --> TASA["tasa maxima con margen"]
- *Descripción textual:* el requisito se compara con el volumen que sale de la tasa máxima y las horas de contacto de cada fase; en el relevo, el eslabón más pequeño fija lo que llega.
- 🎯 **Por qué importa:** Una red de misión se diseña contra requisitos verificables: cuántos datos por día, con qué margen, en cada fase. Un diseño sin esa trazabilidad no se puede verificar ni defender.

📘 **Dónde se aprende** (2 clases): [B89-C20 · Diseño de red de comunicaciones de misión](../programa/clases/B89/B89-C20-diseno-de-red-de-comunicaciones-de-mision/CLASE.md); [B89-C23 · Relación C/N0, Eb/N0 y tasa de error de bit](../programa/clases/B89/B89-C23-relacion-c-n0-eb-n0-y-tasa-de-error-de-bit/CLASE.md).

### Tasa metabólica

- La tasa metabólica es la potencia que gasta el cuerpo.

💡 **Cómo se explica en la clase [B104-C10](../programa/clases/B104/B104-C10-actividades-extravehiculares-eva/CLASE.md):**
- Convertir una tasa metabólica en consumo de oxígeno en litros y en kilogramos.
- Ejercicio 5 · autónomo. ¿Cuál es la tasa metabólica media ponderada?
- 🎯 **Por qué importa:** El oxígeno de un traje es finito y el trabajo manual consume más que el reposo. La decisión central: ¿cuánto margen queda sobre el consumo esperado si la tasa metabólica de cada tarea varía?

📘 **Dónde se aprende** (1 clase): [B104-C10 · Actividades extravehiculares EVA](../programa/clases/B104/B104-C10-actividades-extravehiculares-eva/CLASE.md).

### Tasa por bit

- La tasa por bit es `∫σ(L) dΦ/dL dL`.

💡 **Cómo se explica en la clase [B85-C21](../programa/clases/B85/B85-C21-efectos-de-particulas-energeticas-en-electronica-y-materiales/CLASE.md):**
- Subir el umbral a `L₀ = 10` reduce la tasa al `16,1 %`; bajar `σ_sat` a la mitad la reduce al `50 %`.
- TB --> TD["× bits = tasa del dispositivo"]
- ⚠️ **Error frecuente:** Esperar tasa cero con un umbral alto. la tasa baja pero no se anula (8.3)
- 🎯 **Por qué importa:** Un upset en un procesador o en una memoria puede reiniciar un instrumento o corromper un dato. La decisión central: ¿con qué frecuencia ocurre un evento único en un dispositivo dado y cuánto cambia si se elige un componente de mayor umbral de LET?

📘 **Dónde se aprende** (1 clase): [B85-C21 · Efectos de partículas energéticas en electrónica y materiales](../programa/clases/B85/B85-C21-efectos-de-particulas-energeticas-en-electronica-y-materiales/CLASE.md).

### Tasa real

- La tasa real excluye la inflación y la nominal la incluye; se relacionan por `1 + nominal = (1 + real)(1 + π)` (relación de Fisher).

💡 **Cómo se explica en la clase [B126-C05](../programa/clases/B126/B126-C05-evaluacion-de-viabilidad-economica-de-un-negocio-espacial/CLASE.md):**
- Con tasa real de 10 % e inflación de 3 %, la tasa nominal es `13,3 %`.
- Descontar flujos nominales con la tasa real da `108,77` y sobrestima el VPN en `26,13`.
- ⚠️ **Error frecuente:** Mezclar flujos nominales con una tasa real. Se corrige con 8.3.
- 🎯 **Por qué importa:** [B124-C12](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) evalúa retorno científico, no viabilidad económica. La decisión central: ¿vale hoy más lo que el negocio devolverá que lo que cuesta, y cuánto pueden equivocarse los supuestos antes de que deje de valer?

📘 **Dónde se aprende** (1 clase): [B126-C05 · Evaluación de viabilidad económica de un negocio espacial](../programa/clases/B126/B126-C05-evaluacion-de-viabilidad-economica-de-un-negocio-espacial/CLASE.md).

### Tasa relacionada

- Una tasa relacionada es un problema en el que dos cantidades cambian en el tiempo y se relacionan por una ecuación.

💡 **Cómo se explica en la clase [B09-C06](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md):**
- Resolver un problema de tasas relacionadas.
- 🎯 **Por qué importa:** Para saber dónde está un planeta en su órbita en un instante dado hay que resolver la ecuación de Kepler, `M = E − e sin E`, que no tiene solución en funciones elementales: no se puede despejar `E`.

📘 **Dónde se aprende** (1 clase): [B09-C06 · Derivación implícita](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md).

### Tasa relativa

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B33-C08](../programa/clases/B33/B33-C08-dosis-de-radiacion-en-aviacion/CLASE.md):**
- *Descripción textual:* la temperatura y la gravedad dan la altura de escala y la profundidad; esta, con la atenuación, da la tasa relativa.
- Ejercicio 12. Integrador. Elabora tu *ficha de la radiación en aviación*: profundidad, tasa relativa y límites.
- 🎯 **Por qué importa:** La altitud y la profundidad atmosférica determinan cuánta radiación llega. La decisión central: ¿cuánto menos atmósfera hay a la altitud de vuelo?

📘 **Dónde se aprende** (1 clase): [B33-C08 · Dosis de radiación en aviación](../programa/clases/B33/B33-C08-dosis-de-radiacion-en-aviacion/CLASE.md).

### Tasa secular

- La tasa secular es la variación media por unidad de tiempo, sin las oscilaciones.

💡 **Cómo se explica en la clase [B72-C03](../programa/clases/B72/B72-C03-perturbacion-j2-terrestre/CLASE.md):**
- Escribir las tasas seculares de `Ω`, `ω` y de la anomalía media por J2.
- La evidencia es la tabla de tasas seculares J2 del ejercicio 12 (sección 20).
- ⚠️ **Error frecuente:** Creer que J2 cambia el semieje mayor en promedio. Se corrige con 8.1: `a` e `i` no tienen tasa secular de primer orden.
- 🎯 **Por qué importa:** J2 no cambia el semieje mayor ni la inclinación en promedio, pero hace girar el plano y el perigeo; con ello se diseñan órbitas heliosíncronas y Molniya. La decisión central: ¿cuánto se mueven `Ω` y `ω` por día en una órbita dada y cuánto confiar en la fórmula de primer orden?

📘 **Dónde se aprende** (1 clase): [B72-C03 · Perturbación J2 terrestre](../programa/clases/B72/B72-C03-perturbacion-j2-terrestre/CLASE.md).

### TCA

- El TCA es el instante de mínima distancia `ρ_min`; allí `ṙ = 0`.
- El TCA es el instante de mínima distancia.

💡 **Cómo se explica en la clase [B89-C15](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md):**
- Un transpondedor con razón `880/749 = 1,17490` devuelve la portadora ascendente (7,19 GHz, ilustrativa) multiplicada por la razón; el Doppler de ida y vuelta en el TCA es `-0,000 kHz` y en el AOS `376,4 kHz`: más del doble del de ida porque cuenta dos trayectos.
- FD --> TASA["tasa de Doppler en el TCA"]
- 🎯 **Por qué importa:** El Doppler es la medida básica de rastreo: se usa para determinar la órbita y obliga a diseñar los lazos de portadora y los planes de frecuencia. La decisión central: ¿cuánto se desplaza la frecuencia durante una pasada y qué información de la órbita contiene?

📘 **Dónde se aprende** (2 clases): [B89-C15 · Rastreo y Doppler](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md); [B118-C05 · Conjunciones orbitales](../programa/clases/B118/B118-C05-conjunciones-orbitales/CLASE.md).

### TCPI

- El TCPI es el rendimiento de costo que se necesita para terminar en el BAC.

💡 **Cómo se explica en la clase [B124-C15](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md):**
- El TCPI necesario para terminar en el BAC es `1,615`, mucho más que el rendimiento actual.
- Paso 4 · TCPI. `(100 − 30)/(100 − 45) = 1,273`.
- 🎯 **Por qué importa:** Un proyecto se descontrola de a poco; el valor ganado convierte «vamos bien» en números comparables. La decisión central: ¿cuánto va a costar el proyecto al terminar si el rendimiento actual se mantiene y qué paquete es el problema?

📘 **Dónde se aprende** (1 clase): [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### Techo

- Los prismas pueden ser porro (más anchos, a menudo con mejor campo) o de techo (más compactos) (S2).
- El techo limita el pago total.

💡 **Cómo se explica en la clase [B124-C10](../programa/clases/B124/B124-C10-contratos-y-compras-espaciales/CLASE.md):**
- El comprador paga en promedio `110,78` con dispersión `12,53`; el contratista gana en promedio `3,53` y pierde solo si el techo se alcanza: `0,1933`.
- La probabilidad de que `c + honorario` pase del techo de 125 es `0,2378`.
- 🎯 **Por qué importa:** El tipo de contrato reparte el riesgo de sobrecosto entre quien compra y quien vende. La decisión central: ¿cuánto riesgo asume cada parte con cada tipo de contrato y cuánto cuesta ese reparto en promedio?

📘 **Dónde se aprende** (2 clases): [B08-C13 · Uso seguro de binoculares](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md); [B124-C10 · Contratos y compras espaciales](../programa/clases/B124/B124-C10-contratos-y-compras-espaciales/CLASE.md).

### Tecnofirma

- Una tecnofirma es una señal que indicaría tecnología.

💡 **Cómo se explica en la clase [B56-C16](../programa/clases/B56/B56-C16-tecnofirmas-y-busqueda-seti/CLASE.md):**
- Búsquedas en infrarrojo (calor residual): otro tipo de tecnofirma.
- Definir tecnofirma, EIRP, flujo mínimo detectable y ecuación del radiómetro.
- 🎯 **Por qué importa:** Buscar tecnología exige saber qué flujo mínimo detecta un receptor y qué potencia debería tener un transmisor a una distancia dada. La decisión central: dados la temperatura del sistema, el área efectiva, el ancho de banda y el tiempo de integración, ¿qué flujo mínimo se detecta y hasta qué distancia llega un transmisor dado?

📘 **Dónde se aprende** (1 clase): [B56-C16 · Tecnofirmas y búsqueda SETI](../programa/clases/B56/B56-C16-tecnofirmas-y-busqueda-seti/CLASE.md).

### TECU

- Un TECU es `10¹⁶` electrones por metro cuadrado.

💡 **Cómo se explica en la clase [B57-C29](../programa/clases/B57/B57-C29-correcciones-atmosfericas-en-altimetria/CLASE.md):**
- Con 50 TECU el retardo es `0,1093 m` en Ku y `0,6885 m` en C; con 20 TECU, `0,0437` y `0,2754 m`.
- Un altímetro ilustrativo mide a `13,575 GHz` (Ku) y `5,41 GHz` (C) con un ruido de `2 cm` por frecuencia, con un contenido electrónico de `50 TECU` y presiones de `1013,25`, `1000` y `700 hPa`.
- 🎯 **Por qué importa:** Un error de decímetros en la distancia equivale a decímetros de error en la altura del mar, mayor que las señales que se buscan. La decisión central: ¿qué corrección aplicar a cada retardo y cuánto ruido agrega?

📘 **Dónde se aprende** (1 clase): [B57-C29 · Correcciones atmosféricas en altimetría](../programa/clases/B57/B57-C29-correcciones-atmosfericas-en-altimetria/CLASE.md).

### TED

- A2 es el valor de actividad de la tabla de la IAEA SSR-6. TED es la dosis efectiva total.

🎯 **Por qué importa (clase B86-C18):** Los límites de la energía nuclear en el espacio son tanto jurídicos y de seguridad como técnicos: quién aprueba, con qué análisis y con qué umbrales. Un ingeniero de potencia debe saber que estas decisiones existen y qué datos las gobiernan.

📘 **Dónde se aprende** (1 clase): [B86-C18 · Seguridad y licenciamiento energético](../programa/clases/B86/B86-C18-seguridad-y-licenciamiento-energetico/CLASE.md).

### Telecéntrico

- Un sistema es telecéntrico si ese rayo es paralelo al eje (en el espacio objeto, imagen o ambos).

💡 **Cómo se explica en la clase [B50-C04](../programa/clases/B50/B50-C04-telecentricidad-vineteo-y-diseno-del-campo/CLASE.md):**
- Hallar el diafragma telecéntrico por dos vías.
- Ejercicio 9 · transferencia. Transferencia. ¿Qué ventaja tiene un sistema telecéntrico en el espacio imagen para un detector?
- 🎯 **Por qué importa:** En un detector la luz que llega muy inclinada se pierde o se mezcla; en un espectrógrafo o un mosaico el viñeteo cambia el brillo según el campo. La decisión central: ¿dónde va el diafragma y cuánto campo se acepta con viñeteo?

📘 **Dónde se aprende** (1 clase): [B50-C04 · Telecentricidad, viñeteo y diseño del campo](../programa/clases/B50/B50-C04-telecentricidad-vineteo-y-diseno-del-campo/CLASE.md).

### Telemetría

- Telemetría: valores medidos en la nave.

💡 **Cómo se explica en la clase [B96-C06](../programa/clases/B96/B96-C06-telemetria-operativa/CLASE.md):**
- ECSS-E-ST-70-41C (S1) define cómo se usan los paquetes de telemetría y telecomando para vigilar y controlar subsistemas y cargas útiles, con servicios opcionales adaptables a cada misión.
- Por paquetes: servicios de telemetría (ECSS-E-ST-70-41C, solo resumen).
- 🎯 **Por qué importa:** Un límite mal definido llena la pantalla de alarmas que nadie atiende o calla ante un fallo real. La decisión central: ¿cómo se convierte una cuenta en una magnitud y cuándo se levanta o se baja una alarma?

📖 **Explicado a fondo:** [Telemetría y telecomando](esencial/ampliacion-n-z.md#telemetría-y-telecomando) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B96-C06 · Telemetría operativa](../programa/clases/B96/B96-C06-telemetria-operativa/CLASE.md).

### Telémetro

- El telémetro mide `r = c t/2`.

💡 **Cómo se explica en la clase [B76-C13](../programa/clases/B76/B76-C13-sensores-de-proximidad/CLASE.md):**
- El Monte Carlo coincide con la teoría dentro del `3 %` (telémetro) y del `6 %` (cámara y fusión).
- *Descripción textual:* el telémetro tiene un error fijo; el error de la cámara crece con la distancia; ambos se fusionan y se comprueban por Monte Carlo; existe una distancia de cruce.
- 🎯 **Por qué importa:** Un sensor que funciona a diez metros puede ser inútil a quinientos. La decisión central: ¿a qué distancia conviene cada sensor y cuánto mejora combinarlos?

📘 **Dónde se aprende** (1 clase): [B76-C13 · Sensores de proximidad](../programa/clases/B76/B76-C13-sensores-de-proximidad/CLASE.md).

### Teleobjetivo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C06](../programa/clases/B41/B41-C06-distancias-focales-y-formacion-de-imagen/CLASE.md):**
- Un teleobjetivo `f₁ = 200`, `f₂ = −100`, `d = 150` da `f = 400,000 mm` con el foco a `100,000 mm` de la segunda lente: longitud total `250,000 mm`.
- El teleobjetivo tiene una focal de 400 mm en 250 mm de largo: es la idea de los telescopios compactos (clase 17).
- 🎯 **Por qué importa:** El foco de una cámara o de un telescopio decide el tamaño de la imagen. La decisión central: ¿dónde cae la imagen y de qué tamaño es?

📘 **Dónde se aprende** (1 clase): [B41-C06 · Distancias focales y formación de imagen](../programa/clases/B41/B41-C06-distancias-focales-y-formacion-de-imagen/CLASE.md).

### Teleoperación

- La teleoperación es operar a distancia.

💡 **Cómo se explica en la clase [B104-C12](../programa/clases/B104/B104-C12-robotica-tripulada/CLASE.md):**
- El script [teleoperacion.py](teleoperacion.py) calcula el tiempo de una tarea sintética en dos modos para cinco retardos y simula las correcciones en Marte cercano (comprueba la media Monte Carlo contra la fórmula, el orden de los tiempos y la ventaja del modo supervisado).
- python programa/clases/B104/B104-C12-robotica-tripulada/teleoperacion.py
- 🎯 **Por qué importa:** Con 0 s de retardo se opera en tiempo real; con 3 minutos cada movimiento tarda mucho más. La decisión central: ¿hasta qué retardo conviene teleoperar paso a paso y a partir de cuándo hay que delegar autonomía supervisada?

📘 **Dónde se aprende** (1 clase): [B104-C12 · Robótica tripulada](../programa/clases/B104/B104-C12-robotica-tripulada/CLASE.md).

### Telescopio Compton

- El telescopio Compton: dispersor y absorbedor.

🎯 **Por qué importa (clase B47-C06):** Cada proceso (Compton, pares) domina a una energía distinta y fija el tipo de instrumento. La decisión central: ¿qué proceso usa el detector y con qué incertidumbre angular reconstruye la dirección?

📘 **Dónde se aprende** (1 clase): [B47-C06 · Instrumentos de rayos gamma](../programa/clases/B47/B47-C06-instrumentos-de-rayos-gamma/CLASE.md).

### Telescopio de Kepler

- El telescopio de Kepler (imagen invertida, ocular positivo) y el de Galileo (derecho, ocular negativo).

🎯 **Por qué importa (clase B41-C07):** El aumento decide qué se ve. La decisión central: ¿qué ocular da el aumento y la pupila de salida adecuados?

📘 **Dónde se aprende** (1 clase): [B41-C07 · Aumentos y sistemas afocales](../programa/clases/B41/B41-C07-aumentos-y-sistemas-afocales/CLASE.md).

### Telescopio refractor

- El telescopio refractor usa lentes; el de Galileo combinaba una lente convexa y una cóncava (S2).

🎯 **Por qué importa (clase B02-C13):** Un instrumento nuevo da datos nuevos, pero los datos nuevos no se interpretan solos. La pregunta motivadora es: ¿qué podía concluir Galileo de lo que veía, y qué le faltaba para convencer a quienes no creían?

📘 **Dónde se aprende** (1 clase): [B02-C13 · Galileo y primeras observaciones telescópicas](../programa/clases/B02/B02-C13-galileo-y-primeras-observaciones-telescopicas/CLASE.md).

### Telescopio ΔE–E

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C09):** Medir ΔE y E permite identificar la partícula. La decisión central: ¿qué espesor de detector y qué energía separan protones de partículas alfa?

📘 **Dónde se aprende** (1 clase): [B47-C09 · Detectores de partículas — Instrumentación y observatorios espaciales](../programa/clases/B47/B47-C09-detectores-de-particulas-instrumentacion-y-observatorios-espaciales/CLASE.md).

### Temperatura

- La temperatura `T` mide el estado térmico; en el SI se expresa en kelvin (K), donde `0 K` es el cero absoluto.
- La temperatura `kT` se expresa en keV: `1 keV = 1,602 177 × 10⁻¹⁶ J`.

💡 **Cómo se explica en la clase [B05-C13](../programa/clases/B05/B05-C13-temperatura-y-energia-termica/CLASE.md):**
- Una temperatura mayor significa partículas más rápidas, no más grandes.
- Un cambio de temperatura de 1 K es igual a 1 °C, pero el cero de ambas escalas no coincide: en fórmulas con `T⁴` o `k_B T` solo vale kelvin.
- ⚠️ **Error frecuente:** Confundir calor con temperatura. Ejercicios 2 y 3.
- 🎯 **Por qué importa:** Un satélite recibe luz solar de un lado y emite calor al espacio por el otro, y la electrónica solo trabaja en un rango de temperaturas. La pregunta motivadora es: ¿qué es la temperatura, cómo se relaciona con la energía de las partículas y qué determina la temperatura de equilibrio de un cuerpo en el espacio?

📘 **Dónde se aprende** (2 clases): [B05-C13 · Temperatura y energía térmica](../programa/clases/B05/B05-C13-temperatura-y-energia-termica/CLASE.md); [B25-C13 · Cúmulos de galaxias](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md).

### Temperatura absoluta

- La temperatura absoluta se mide en kelvin (K), con 0 K como cero absoluto;

💡 **Cómo se explica en la clase [B06-C09](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md):**
- ⚠️ **Error frecuente:** Usar grados Celsius en `PV = nRT`. La temperatura debe ser absoluta; se corrige con la sección 6.
- 🎯 **Por qué importa:** La NASA publica para Marte, Venus y la Tierra la presión y la temperatura medias en la superficie, la gravedad, el peso molecular de la atmósfera y su densidad (S1, S2, S3). ¿Puedes reproducir esa densidad con sólo lo anterior?

📘 **Dónde se aprende** (1 clase): [B06-C09 · Gases ideales y no ideales](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md).

### Temperatura adiabática

- La temperatura adiabática sale de dividir el calor neto entre `n C_p`.

💡 **Cómo se explica en la clase [B78-C04](../programa/clases/B78/B78-C04-propulsion-monopropelente-conceptual/CLASE.md):**
- Estimar la temperatura adiabática con un balance de energía de calor específico constante.
- 🎯 **Por qué importa:** La descomposición de un monopropelente tiene dos pasos: uno que libera calor y otro que lo absorbe. La decisión central: ¿conviene que el amoníaco intermedio se disocie del todo, por la menor masa molar, o que se conserve, por la mayor temperatura?

📘 **Dónde se aprende** (1 clase): [B78-C04 · Propulsión monopropelente conceptual](../programa/clases/B78/B78-C04-propulsion-monopropelente-conceptual/CLASE.md).

### Temperatura cardinal

- La temperatura cardinal son las tres temperaturas del crecimiento: mínima `T_min`, óptima `T_opt` y máxima `T_max`.

💡 **Cómo se explica en la clase [B56-C05](../programa/clases/B56/B56-C05-extremofilos-y-limites-ambientales/CLASE.md):**
- Definir extremófilo, actividad del agua, temperatura cardinal y límite de replicación.
- Ajustar un modelo de temperatura cardinal a datos y recuperar `T_min`.
- 🎯 **Por qué importa:** Decidir si un ambiente es habitable, o si una nave puede contaminarlo, exige umbrales de temperatura y de agua disponible. La decisión central: dada la temperatura y la actividad del agua de un ambiente, ¿está dentro de los límites en que la vida terrestre puede replicarse?

📘 **Dónde se aprende** (1 clase): [B56-C05 · Extremófilos y límites ambientales](../programa/clases/B56/B56-C05-extremofilos-y-limites-ambientales/CLASE.md).

### Temperatura central

- La temperatura central se deduce de la ecuación de estado: `T_c = P_c μ m_u/(ρ_c k)`.

💡 **Cómo se explica en la clase [B24-C20](../programa/clases/B24/B24-C20-modelo-simplificado-de-estructura-estelar/CLASE.md):**
- *Descripción textual:* con la masa y el radio, la solución de Lane–Emden da las magnitudes centrales; la temperatura sale de la ecuación de estado; se contrasta con la referencia y la diferencia indica qué física falta.
- Paso 4 · Sentido. Es un resultado del politropo; la temperatura central de una estrella real de esta masa se obtendría con un modelo completo.
- 🎯 **Por qué importa:** Un modelo de estructura real resuelve cuatro ecuaciones acopladas con física detallada; un politropo sustituye esa física por una sola relación `P ∝ ρ^{1+1/n}` y permite resolver todo con una ecuación. Es el mejor modo de ver qué se obtiene con poco y qué falta.

📘 **Dónde se aprende** (1 clase): [B24-C20 · Modelo simplificado de estructura estelar](../programa/clases/B24/B24-C20-modelo-simplificado-de-estructura-estelar/CLASE.md).

### Temperatura de antena

- La temperatura de antena `T_A` es la temperatura equivalente a la potencia recibida.

💡 **Cómo se explica en la clase [B46-C05](../programa/clases/B46/B46-C05-ganancia-y-temperatura-de-antena/CLASE.md):**
- *Descripción textual:* el área efectiva da la sensibilidad y la integral de la fuente con el haz da la temperatura de antena, que se compara con la fórmula.
- Integrar la temperatura de antena en dos dimensiones.
- 🎯 **Por qué importa:** Para saber cuánto flujo hay en una fuente hay que conocer cuánta fracción del haz llena. La decisión central: ¿cuánto vale la temperatura de antena de una fuente extensa en un haz dado?

📘 **Dónde se aprende** (1 clase): [B46-C05 · Ganancia y temperatura de antena](../programa/clases/B46/B46-C05-ganancia-y-temperatura-de-antena/CLASE.md).

### Temperatura de brillo

- La temperatura de brillo es la de un cuerpo negro que produciría la misma radiancia.
- La temperatura de brillo `T_B` es la temperatura de un cuerpo negro con ese brillo a esa frecuencia.
- La temperatura de brillo `T_b` es la de un cuerpo negro que daría la misma radiancia.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B13-C17](../programa/clases/B13/B13-C17-calibracion-radiometrica/CLASE.md):**
- Una cuenta de `250 DN` da `L = (250 − 119,2)/0,7981 = 163,9 W m⁻² sr⁻¹` y, resolviendo `L_banda(T) = 163,9`, una temperatura de brillo de `422,5 K`.
- Además, la temperatura de brillo coincide con la real solo si `ε = 1`.
- 🎯 **Por qué importa:** Una cámara infrarroja de una nave mide el calor emitido por la superficie de un planeta. Sus cuentas no significan nada hasta saberse cuánta radiancia corresponde a cada una.

📘 **Dónde se aprende** (4 clases): [B13-C17 · Calibración radiométrica](../programa/clases/B13/B13-C17-calibracion-radiometrica/CLASE.md); [B46-C01 · Espectro radioastronómico](../programa/clases/B46/B46-C01-espectro-radioastronomico/CLASE.md); [B51-C01 · Calibración de amplitud y escala de flujo con calibradores primarios](../programa/clases/B51/B51-C01-calibracion-de-amplitud-y-escala-de-flujo-con-calibradores-primarios/CLASE.md); [B57-C21 · Sensores infrarrojos térmicos para observación terrestre](../programa/clases/B57/B57-C21-sensores-infrarrojos-termicos-para-observacion-terrestre/CLASE.md).

### Temperatura de cámara

- La temperatura de cámara `T_c` es la del gas antes de la tobera.

💡 **Cómo se explica en la clase [B78-C03](../programa/clases/B78/B78-C03-termodinamica-de-camaras/CLASE.md):**
- Efecto de la temperatura de camara (pc/pe = 100, M = 22 g/mol):
- 🎯 **Por qué importa:** El mismo calor produce chorros distintos según el gas. La decisión central: ¿qué parámetro de cámara gana más escape, subir la temperatura o bajar la masa molar, y hasta dónde se puede expandir el gas?

📘 **Dónde se aprende** (1 clase): [B78-C03 · Termodinámica de cámaras](../programa/clases/B78/B78-C03-termodinamica-de-camaras/CLASE.md).

### Temperatura de color

- La temperatura de color viene de la razón de dos bandas.

💡 **Cómo se explica en la clase [B45-C13](../programa/clases/B45/B45-C13-temperatura-y-espectro-de-cuerpo-negro/CLASE.md):**
- La temperatura de color por razón 400/700 nm sin ruido es `6500,00 K`.
- Como un horno: al subir la temperatura pasa del rojo al blanco; el color (la razón de dos bandas) mide la temperatura aunque no conozcas el tamaño.
- 🎯 **Por qué importa:** La temperatura se estima del color o del espectro, y el pico depende de si se mide por unidad de λ o de ν. La decisión central: ¿qué temperatura y con qué error dan unos flujos en banda?

📘 **Dónde se aprende** (1 clase): [B45-C13 · Temperatura y espectro de cuerpo negro](../programa/clases/B45/B45-C13-temperatura-y-espectro-de-cuerpo-negro/CLASE.md).

### Temperatura de Curie

- La temperatura de Curie es aquella por encima de la cual un mineral pierde su magnetización.

🎯 **Por qué importa (clase B65-C03):** La corteza magnetizada permite reconstruir campos de cuerpos que hoy no tienen dinamo. La decisión central: ¿qué parte de un mapa de anomalías es información sobre la magnetización y qué parte es ambigüedad geométrica?

📘 **Dónde se aprende** (1 clase): [B65-C03 · Magnetismo cortical remanente y anomalías magnéticas](../programa/clases/B65/B65-C03-magnetismo-cortical-remanente-y-anomalias-magneticas/CLASE.md).

### Temperatura de duplicación

- La temperatura de duplicación es el aumento que la duplica.

🎯 **Por qué importa (clase B44-C07):** La oscuridad añade señal y ruido; saber cómo escala permite elegir temperatura y exposición. La decisión central: ¿cuánto hay que enfriar para que la corriente oscura deje de importar?

📘 **Dónde se aprende** (1 clase): [B44-C07 · Corriente oscura](../programa/clases/B44/B44-C07-corriente-oscura/CLASE.md).

### Temperatura de ebullición

- La temperatura de ebullición a una presión `P` es la `T` con `P_v(T) = P`.

💡 **Cómo se explica en la clase [B56-C06](../programa/clases/B56/B56-C06-agua-liquida-y-solventes-alternativos/CLASE.md):**
- Definir punto triple, presión de vapor, temperatura de ebullición y calor latente.
- Hallar la temperatura de ebullición a una presión dada.
- 🎯 **Por qué importa:** «Sigue el agua» es una consigna de la exploración, pero tener hielo o vapor no es tener un líquido. La presión y la temperatura mandan.

📘 **Dónde se aprende** (1 clase): [B56-C06 · Agua líquida y solventes alternativos](../programa/clases/B56/B56-C06-agua-liquida-y-solventes-alternativos/CLASE.md).

### Temperatura de equilibrio

- La temperatura de equilibrio es la que iguala potencia absorbida y emitida.
- La temperatura de equilibrio es aquella en que la potencia absorbida iguala a la radiada.
- La temperatura de equilibrio `T = [L(1−A)/(16πσd²)]^(1/4)` es la de un cuerpo esférico de rotación rápida.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C13](../programa/clases/B05/B05-C13-temperatura-y-energia-termica/CLASE.md):**
- *Descripción textual:* la luz solar de potencia `S × área` es absorbida y aumenta la energía térmica; el cuerpo emite `σ A T⁴`; en el equilibrio, entrada y salida se igualan y eso fija la temperatura.
- Balance de energía da la temperatura de equilibrio con muy pocos datos.
- ⚠️ **Error frecuente:** Creer que más masa implica otra temperatura de equilibrio. Sección 13.
- 🎯 **Por qué importa:** Un satélite recibe luz solar de un lado y emite calor al espacio por el otro, y la electrónica solo trabaja en un rango de temperaturas. La pregunta motivadora es: ¿qué es la temperatura, cómo se relaciona con la energía de las partículas y qué determina la temperatura de equilibrio de un cuerpo en el espacio?

📘 **Dónde se aprende** (11 clases): [B05-C13 · Temperatura y energía térmica](../programa/clases/B05/B05-C13-temperatura-y-energia-termica/CLASE.md); [B13-C16 · Calibración térmica](../programa/clases/B13/B13-C16-calibracion-termica/CLASE.md); [B29-C13 · Zonas de habitabilidad](../programa/clases/B29/B29-C13-zonas-de-habitabilidad/CLASE.md); [B43-C19 · Seguridad y mantenimiento](../programa/clases/B43/B43-C19-seguridad-y-mantenimiento/CLASE.md); [B47-C22 · Misiones de física solar: SOHO, SDO y Solar Orbiter](../programa/clases/B47/B47-C22-misiones-de-fisica-solar-soho-sdo-y-solar-orbiter/CLASE.md); [B52-C15 · Cinturón de Kuiper](../programa/clases/B52/B52-C15-cinturon-de-kuiper/CLASE.md) y 5 más.

### Temperatura de equilibrio radiativo

- La temperatura de equilibrio radiativo es `T_w = (q̇/(εσ))^(1/4)`.

💡 **Cómo se explica en la clase [B77-C15](../programa/clases/B77/B77-C15-calentamiento-aerodinamico/CLASE.md):**
- Obtener la temperatura de equilibrio radiativo `T_w = (q̇/(εσ))^(1/4)`.
- 🎯 **Por qué importa:** El flujo de calor máximo y la carga total deciden qué material y qué espesor protegen al vehículo, y no se maximizan en el mismo punto que la desaceleración. La decisión central: ¿cuánto vale el flujo de pico, a qué altitud ocurre y cómo escala con el radio de la nariz y el coeficiente balístico?

📘 **Dónde se aprende** (1 clase): [B77-C15 · Calentamiento aerodinámico](../programa/clases/B77/B77-C15-calentamiento-aerodinamico/CLASE.md).

### Temperatura de escarcha

- La temperatura de escarcha es aquella en que el CO₂ se condensa a la presión dada.

💡 **Cómo se explica en la clase [B54-C14](../programa/clases/B54/B54-C14-atmosfera-de-marte/CLASE.md):**
- CC["Clausius-Clapeyron"] --> TF["temperatura de escarcha"]
- Clausius–Clapeyron da la temperatura de escarcha.
- 🎯 **Por qué importa:** La presión marciana varía unas decenas de por ciento durante el año porque parte del CO₂ se condensa en los casquetes polares. La pregunta motivadora: ¿cuánta masa de CO₂ participa en ese ciclo?

📘 **Dónde se aprende** (1 clase): [B54-C14 · Atmósfera de Marte](../programa/clases/B54/B54-C14-atmosfera-de-marte/CLASE.md).

### Temperatura de excitación

- La temperatura de excitación de la línea.

🎯 **Por qué importa (clase B46-C12):** Qué transición observar depende de la temperatura del gas, porque la población de cada nivel cambia. La decisión central: ¿qué línea es la más intensa a una temperatura dada?

📘 **Dónde se aprende** (1 clase): [B46-C12 · Emisiones moleculares](../programa/clases/B46/B46-C12-emisiones-moleculares/CLASE.md).

### Temperatura de Fermi

- La temperatura de Fermi es `T_F = E_F/k`.

💡 **Cómo se explica en la clase [B27-C01](../programa/clases/B27/B27-C01-presion-de-degeneracion/CLASE.md):**
- La energía cinética de Fermi vale `143,6 keV`, equivalente a `1,7 × 10⁹ K`: a las temperaturas de un núcleo estelar (decenas de millones de kelvin) el gas está profundamente degenerado.
- 🎯 **Por qué importa:** Una estrella sin fusión no se desploma porque los electrones (o neutrones) no pueden apretarse más allá de lo que permite el principio de exclusión, aunque la temperatura sea cero. La decisión central: dada la densidad de un gas degenerado, ¿cuánto vale el momento de Fermi, la presión y cuál de los dos límites aplica?

📘 **Dónde se aprende** (2 clases): [B27-C01 · Presión de degeneración](../programa/clases/B27/B27-C01-presion-de-degeneracion/CLASE.md); [B31-C06 · Estadísticas cuánticas](../programa/clases/B31/B31-C06-estadisticas-cuanticas/CLASE.md).

### Temperatura de recalentamiento

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B40-C02):** Sin recalentamiento no habría universo caliente. La decisión central: ¿cuándo domina la radiación y qué temperatura alcanza?

📘 **Dónde se aprende** (1 clase): [B40-C02 · Recalentamiento y transición a la era de radiación](../programa/clases/B40/B40-C02-recalentamiento-y-transicion-a-la-era-de-radiacion/CLASE.md).

### Temperatura de ruido

- La temperatura de ruido de un dispositivo es `T = T₀(F − 1)` con `T₀ = 290 K`.
- La temperatura de ruido de un componente.
- La temperatura de ruido `T_e` de una etapa.

💡 **Cómo se explica en la clase [B46-C06](../programa/clases/B46/B46-C06-ruido-de-sistema-y-radiometria/CLASE.md):**
- Calcular la temperatura de ruido de una cascada.
- 🎯 **Por qué importa:** La señal de una fuente astronómica es mucho menor que el ruido, y solo el promedio la hace visible. La decisión central: ¿cuánto tiempo y ancho de banda se necesitan para alcanzar una sensibilidad dada?

📘 **Dónde se aprende** (3 clases): [B46-C06 · Ruido de sistema y radiometría](../programa/clases/B46/B46-C06-ruido-de-sistema-y-radiometria/CLASE.md); [B49-C06 · Amplificadores de bajo ruido (LNA): tecnología, ganancia y adaptación](../programa/clases/B49/B49-C06-amplificadores-de-bajo-ruido-lna-tecnologia-ganancia-y-adaptacion/CLASE.md); [B89-C07 · Figura de ruido de receptor](../programa/clases/B89/B89-C07-figura-de-ruido-de-receptor/CLASE.md).

### Temperatura de ruido de cielo

- La temperatura de ruido de cielo por una atenuación `A` es `T = T_m(1 − 10^{−A/10})`, con `T_m` la temperatura media física del medio.

💡 **Cómo se explica en la clase [B91-C07](../programa/clases/B91/B91-C07-atenuacion-atmosferica-y-efectos-de-la-lluvia-en-enlaces/CLASE.md):**
- En banda X, con `3 dB` de atenuación, la temperatura de ruido de cielo sube a `137 K` y la `G/T` de la antena de 70 m (calculada de valores publicados) cae de `62,33` a `52,68 dB/K`: en total, `12,65 dB` menos de `C/N₀`.
- 🎯 **Por qué importa:** En bandas altas la lluvia puede quitar decenas de dB durante una fracción pequeña del año. La decisión central: ¿qué margen reservar para una disponibilidad dada, y a partir de qué frecuencia deja de ser razonable un enlace sin reserva ni diversidad?

📘 **Dónde se aprende** (1 clase): [B91-C07 · Atenuación atmosférica y efectos de la lluvia en enlaces](../programa/clases/B91/B91-C07-atenuacion-atmosferica-y-efectos-de-la-lluvia-en-enlaces/CLASE.md).

### Temperatura de sistema

- La temperatura de sistema es `T_sis = T_ant + T_rx`.

💡 **Cómo se explica en la clase [B89-C07](../programa/clases/B89/B89-C07-figura-de-ruido-de-receptor/CLASE.md):**
- Calcular la temperatura de sistema y `G/T`.
- 🎯 **Por qué importa:** La primera etapa de una cadena receptora decide casi todo el ruido: un amplificador de bajo ruido bien colocado vale muchos decibelios de `G/T`. La decisión central: ¿qué orden y qué componentes dan la menor temperatura de sistema y el mayor `G/T`?

📘 **Dónde se aprende** (2 clases): [B46-C06 · Ruido de sistema y radiometría](../programa/clases/B46/B46-C06-ruido-de-sistema-y-radiometria/CLASE.md); [B89-C07 · Figura de ruido de receptor](../programa/clases/B89/B89-C07-figura-de-ruido-de-receptor/CLASE.md).

### Temperatura de superficie

- La temperatura de superficie `T_s` es la real, corregida por emisividad y atmósfera.

💡 **Cómo se explica en la clase [B57-C21](../programa/clases/B57/B57-C21-sensores-infrarrojos-termicos-para-observacion-terrestre/CLASE.md):**
- *Descripción textual:* la superficie emite, la atmósfera absorbe y reemite, el sensor mide radiancia que se convierte en temperatura de brillo en dos bandas, y la diferencia entre ambas corrige el efecto atmosférico.
- La evidencia es la ficha de temperatura de superficie del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Una temperatura de superficie mal estimada engaña a quien estudia islas de calor, estrés hídrico, incendios o volcanes. La decisión central: ¿cuánto error introducen la atmósfera y la emisividad, y cómo se corrigen con dos bandas?

📘 **Dónde se aprende** (1 clase): [B57-C21 · Sensores infrarrojos térmicos para observación terrestre](../programa/clases/B57/B57-C21-sensores-infrarrojos-termicos-para-observacion-terrestre/CLASE.md).

### Temperatura de unión

- La temperatura de unión es `T_j = T_placa + R_θ P`.
- La temperatura de unión `Tj = Ta + θ_ja P` es la del semiconductor.

💡 **Cómo se explica en la clase [B86-C09](../programa/clases/B86/B86-C09-electronica-de-potencia/CLASE.md):**
- *Descripción textual:* la frecuencia sube las pérdidas de conmutación y baja las de rizado y núcleo; su suma tiene un mínimo; la pérdida del MOSFET fija su temperatura de unión, que se compara con un límite de derating.
- Calcular la temperatura de unión con una resistencia térmica y compararla con un límite de derating.
- 🎯 **Por qué importa:** La eficiencia no se mejora subiendo o bajando la frecuencia sin más: las pérdidas de conmutación crecen con ella y las de rizado decrecen. La temperatura de unión marca además el límite de fiabilidad del componente.

📘 **Dónde se aprende** (2 clases): [B86-C09 · Electrónica de potencia](../programa/clases/B86/B86-C09-electronica-de-potencia/CLASE.md); [B93-C02 · Selección de componentes y derating](../programa/clases/B93/B93-C02-seleccion-de-componentes-y-derating/CLASE.md).

### Temperatura del núcleo

- La temperatura del núcleo está limitada por los materiales.

🎯 **Por qué importa (clase B78-C14):** Un cohete químico limita su `Isp` por la química del propelente; uno térmico lo limita por la temperatura que aguanta el núcleo. La decisión central: ¿cuánto `Isp` puede dar un gas de baja masa molar calentado a una temperatura dada y qué empuje corresponde a una potencia térmica?

📘 **Dónde se aprende** (1 clase): [B78-C14 · Propulsión nuclear térmica conceptual](../programa/clases/B78/B78-C14-propulsion-nuclear-termica-conceptual/CLASE.md).

### Temperatura efectiva

- La temperatura efectiva `T_eff` es la temperatura de un cuerpo negro que emitiría la misma energía por unidad de superficie que la estrella.
- La temperatura efectiva `T_ef` es la temperatura de un cuerpo negro con el mismo radio y la misma luminosidad.
- La temperatura efectiva `T(r)` es la de un cuerpo negro con el flujo local.

💡 **Cómo se explica en la clase [B01-C14](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md):**
- El NASA Exoplanet Archive publica, para estrellas que tienen planetas conocidos, su temperatura efectiva, radio, masa, luminosidad y distancia (S1).
- Definir temperatura efectiva, radio, luminosidad y distancia de una estrella.
- 🎯 **Por qué importa:** Dos estrellas pueden verse igual de brillantes y ser totalmente distintas: una pequeña y cercana, otra enorme y lejana (C09). Para saber cómo es una estrella necesitas separar lo que ves (flujo) de lo que ella es (luminosidad, temperatura, radio) y de dónde está (distancia).

📖 **Explicado a fondo:** [Temperatura efectiva](esencial/esencial-m-z.md#temperatura-efectiva) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (4 clases): [B01-C14 · Estrellas y sus principales propiedades](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md); [B24-C03 · Diagrama de Hertzsprung-Russell](../programa/clases/B24/B24-C03-diagrama-de-hertzsprung-russell/CLASE.md); [B27-C10 · Discos de acreción](../programa/clases/B27/B27-C10-discos-de-acrecion/CLASE.md); [B32-C05 · Relación T-τ y estructura térmica de la fotosfera](../programa/clases/B32/B32-C05-relacion-t-y-estructura-termica-de-la-fotosfera/CLASE.md).

### Temperatura equivalente

- La temperatura equivalente `E/k_B` compara una energía con una temperatura.

💡 **Cómo se explica en la clase [B28-C02](../programa/clases/B28/B28-C02-fotones-en-multiples-longitudes-de-onda/CLASE.md):**
- La temperatura equivalente dice cuán caliente tendría que estar un cuerpo negro para emitir su máximo allí.
- Ejercicio 4. Temperatura equivalente de `1 keV`.
- 🎯 **Por qué importa:** Cada banda revela un proceso distinto; combinarlas exige convertir bien las unidades y saber qué banda corresponde a qué temperatura. La decisión central: ¿en qué banda emite un objeto de temperatura dada y cómo se pasa de una magnitud a otra sin error?

📘 **Dónde se aprende** (1 clase): [B28-C02 · Fotones en múltiples longitudes de onda](../programa/clases/B28/B28-C02-fotones-en-multiples-longitudes-de-onda/CLASE.md).

### Temperatura exosférica

- La temperatura exosférica `T∞` es el valor asintótico de la temperatura.

💡 **Cómo se explica en la clase [B72-C07](../programa/clases/B72/B72-C07-modelos-de-densidad-atmosferica/CLASE.md):**
- Descripción larga: Con las mismas condiciones en 120 km, duplicar la temperatura exosférica multiplica por más de cien la densidad a 400 km y por más de treinta mil a 800 km.
- Medir la sensibilidad de la densidad a la temperatura exosférica.
- 🎯 **Por qué importa:** El arrastre es tan incierto como la densidad que se le da. La decisión central: ¿cuánto puede variar la densidad a una altitud dada si cambia la temperatura de la termosfera, y qué incertidumbre hereda por eso un cálculo de decaimiento?

📘 **Dónde se aprende** (1 clase): [B72-C07 · Modelos de densidad atmosférica](../programa/clases/B72/B72-C07-modelos-de-densidad-atmosferica/CLASE.md).

### Temperatura límite

- La temperatura límite es `T_a − Q/G`.

💡 **Cómo se explica en la clase [B44-C08](../programa/clases/B44/B44-C08-enfriamiento-de-detectores/CLASE.md):**
- Con `C = 200 J/K`, `G = 0,5 W/K`, `Q = 30 W` y `T_a = 293 K`, la temperatura límite es `233 K` y `τ = 400 s`.
- Hallar la temperatura límite y la constante de tiempo.
- 🎯 **Por qué importa:** La cámara no está fría al encenderla. La decisión central: ¿cuánto hay que esperar antes de calibrar y qué temperatura final se alcanza?

📘 **Dónde se aprende** (1 clase): [B44-C08 · Enfriamiento de detectores](../programa/clases/B44/B44-C08-enfriamiento-de-detectores/CLASE.md).

### Temperatura operacional

- La temperatura operacional `T_op` incluye el receptor y el cielo.

💡 **Cómo se explica en la clase [B91-C08](../programa/clases/B91/B91-C08-antenas-de-gran-apertura-y-estaciones-de-espacio-profundo/CLASE.md):**
- La antena de 70 m de la DSN (DSS-14) tiene en recepción de banda X una ganancia publicada de `74,55 dBi`, un ancho de haz de `0,032°` y una temperatura operacional de `16,69 K` en zenit con cielo claro al 25 %: `G/T = 62,33 dB/K` (calculado).
- Calcular `G/T` de la estación a partir de la ganancia y la temperatura operacional publicadas.
- 🎯 **Por qué importa:** Un enlace a distancias de unidades astronómicas pierde unos 280 dB: solo se cierra con una estación enorme y de ruido muy bajo. La decisión central: ¿qué antena de estación (una de 70 m, una de 34 m o un arreglo de varias) permite la velocidad de datos pedida, y cuánto cuesta un error de apuntamiento?

📘 **Dónde se aprende** (1 clase): [B91-C08 · Antenas de gran apertura y estaciones de espacio profundo](../programa/clases/B91/B91-C08-antenas-de-gran-apertura-y-estaciones-de-espacio-profundo/CLASE.md).

### Temperaturas cardinales

- Las temperaturas cardinales son la mínima, la óptima y la máxima de crecimiento.

💡 **Cómo se explica en la clase [B64-C02](../programa/clases/B64/B64-C02-termofilos-e-hipertermofilos/CLASE.md):**
- *Descripción textual:* la temperatura entra en un modelo cardinal que da la tasa; de la rama ascendente sale la energía de activación aparente, del máximo la temperatura óptima, y por separado la temperatura fija la presión de saturación que exige el medio.
- Definir las temperaturas cardinales y los intervalos térmicos de termófilos e hipertermófilos.
- 🎯 **Por qué importa:** Un hipertermófilo crece donde casi todo lo demás muere, pero el agua hierve a 100 °C a presión ambiente. La pregunta motivadora: ¿qué fija el límite superior de temperatura de la vida y cómo se mide ese límite?

📘 **Dónde se aprende** (1 clase): [B64-C02 · Termófilos e hipertermófilos](../programa/clases/B64/B64-C02-termofilos-e-hipertermofilos/CLASE.md).

### Temporal

- La localidad espacial es acceder a datos vecinos; la temporal, repetir el acceso a un mismo dato.

💡 **Cómo se explica en la clase [B18-C03](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md):**
- La caché aprovecha dos hechos: lo que acabas de usar probablemente lo usarás de nuevo (localidad temporal) y lo vecino a lo que usaste probablemente se use pronto (localidad espacial).
- Los métodos por bloques (procesar la matriz en teselas que caben en caché) mejoran la localidad temporal, a cambio de código más complejo.
- 🎯 **Por qué importa:** Un catálogo con millones de estrellas o una rejilla de simulación pasan cada dato por la CPU una o pocas veces. Cuando las operaciones por dato son pocas, el tiempo no lo fija la CPU sino el viaje de los datos.

📘 **Dónde se aprende** (1 clase): [B18-C03 · Jerarquía y estructuras de memoria](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md).

### Tempranas

- Las fechas tempranas (ES, EF) salen del paso hacia adelante; las tardías (LS, LF), del paso hacia atrás.

💡 **Cómo se explica en la clase [B124-C16](../programa/clases/B124/B124-C16-planificacion-de-cronograma-y-entregables/CLASE.md):**
- Calcular fechas tempranas y tardías de una red de actividades.
- 🎯 **Por qué importa:** Un plazo prometido sin ruta crítica ni incertidumbre es una apuesta. La decisión central: ¿qué actividades controlan el plazo y con qué probabilidad se cumple?

📘 **Dónde se aprende** (1 clase): [B124-C16 · Planificación de cronograma y entregables](../programa/clases/B124/B124-C16-planificacion-de-cronograma-y-entregables/CLASE.md).

### Tendencia

- La tendencia es el ajuste lineal `r(t) = c + m t`;
- Una tendencia es una variación lenta de fondo, no periódica.
- La tendencia es la pendiente de una recta ajustada a una serie.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B13-C23](../programa/clases/B13/B13-C23-estabilidad-y-deriva-temporal-de-instrumentos/CLASE.md):**
- Ajustar una tendencia lineal a medidas de una referencia estable.
- Corregir la serie dividiendo por la tendencia ajustada.
- 🎯 **Por qué importa:** Un detector espacial lleva años en órbita. Su sensibilidad cambia lentamente por daño de radiación, contaminación y envejecimiento.

📘 **Dónde se aprende** (4 clases): [B13-C23 · Estabilidad y deriva temporal de instrumentos](../programa/clases/B13/B13-C23-estabilidad-y-deriva-temporal-de-instrumentos/CLASE.md); [B15-C01 · Series temporales discretas](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md); [B57-C12 · Oceanografía desde órbita](../programa/clases/B57/B57-C12-oceanografia-desde-orbita/CLASE.md); [B57-C14 · Glaciares y criósfera](../programa/clases/B57/B57-C14-glaciares-y-criosfera/CLASE.md).

### Tensión

- La tensión es la fuerza que ejerce una cuerda o cable tirando.
- La tensión o diferencia de potencial `V` (voltios) es la energía por carga.
- La tensión es una variable ilustrativa de malestar interpersonal.

💡 **Cómo se explica en la clase [B05-C05](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md):**
- Hay tres fuerzas: dos tensiones `T` y el peso `m g_n` (S1).
- Cuando se levanta una carga con dos cables, cada cable tira con una tensión que depende del ángulo; cuanto más horizontales, más tensión.
- 🎯 **Por qué importa:** En un lanzamiento o en una maniobra hay varias fuerzas a la vez: gravedad, empuje, tensiones, rozamiento. La pregunta motivadora es: ¿cómo dejo de olvidar fuerzas y de contar dos veces una misma?

📘 **Dónde se aprende** (3 clases): [B05-C05 · Diagramas de cuerpo libre](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md); [B05-C16 · Corriente y circuitos elementales](../programa/clases/B05/B05-C16-corriente-y-circuitos-elementales/CLASE.md); [B104-C16 · Manejo de conflictos](../programa/clases/B104/B104-C16-manejo-de-conflictos/CLASE.md).

### Tensión crítica de placa

- La tensión crítica de placa es `σ_cr = kπ²E/(12(1 − ν²))(t/b)²`.

💡 **Cómo se explica en la clase [B84-C23](../programa/clases/B84/B84-C23-vigas-y-placas-flexion-y-pandeo/CLASE.md):**
- El script [pandeo.py](pandeo.py) calcula flechas, cargas críticas de Euler, tensión crítica de placa y el pandeo por autovalores (comprueba `P_cr` FE con 8 elementos a menos del 0,5 % de Euler).
- Tension critica de la placa = 27.64 MPa ; fuerza critica por ancho = 55.3 kN/m
- 🎯 **Por qué importa:** Una columna de aluminio de 30 × 10 mm y 0,5 m se pandea a 6810 N, cuando su sección podría soportar 82 500 N en compresión simple: el 8 %. La decisión central: ¿a qué carga pandea un elemento esbelto y cómo cambia con los apoyos y con el espesor?

📘 **Dónde se aprende** (1 clase): [B84-C23 · Vigas y placas: flexión y pandeo](../programa/clases/B84/B84-C23-vigas-y-placas-flexion-y-pandeo/CLASE.md).

### Tensión de circuito abierto

- La tensión de circuito abierto (OCV) depende del SOC.

🎯 **Por qué importa (clase B86-C05):** Una batería de órbita baja hace unos `5400` ciclos al año. Dimensionarla por la energía de un solo eclipse sin mirar la profundidad de descarga la agota mucho antes del fin de la misión.

📘 **Dónde se aprende** (1 clase): [B86-C05 · Baterías de ion-litio](../programa/clases/B86/B86-C05-baterias-de-ion-litio/CLASE.md).

### Tensión de fondo

- La tensión de fondo es `τ = ρ g R_h S`.

💡 **Cómo se explica en la clase [B66-C01](../programa/clases/B66/B66-C01-valles-y-canales-morfologia-y-origen-en-superficies-planetarias/CLASE.md):**
- *Descripción textual:* de la geometría salen el radio hidráulico, la velocidad, el caudal, el número de Froude y la tensión de fondo; la velocidad se contrasta con Manning.
- Descripción larga: el caudal cae con la raíz de la gravedad, el Froude no cambia y la tensión de fondo cae en proporción a `g`.
- 🎯 **Por qué importa:** Un valle visto desde órbita no dice por sí solo cuánta agua (o metano) pasó por él. La decisión central: ¿cuánto caudal transporta un canal de la misma geometría en otro cuerpo, y qué cambia además del caudal?

📘 **Dónde se aprende** (1 clase): [B66-C01 · Valles y canales: morfología y origen en superficies planetarias](../programa/clases/B66/B66-C01-valles-y-canales-morfologia-y-origen-en-superficies-planetarias/CLASE.md).

### Tensión de haz

- La tensión de haz `V` acelera los iones.

💡 **Cómo se explica en la clase [B78-C07](../programa/clases/B78/B78-C07-motores-ionicos/CLASE.md):**
- *Descripción textual:* la tensión y la masa del ion dan su velocidad; el empuje fija el caudal de iones y la corriente; la ley de Child–Langmuir da la densidad máxima y con ella el área mínima; el caudal total da la utilización de masa.
- Analogía: una escalera mecánica con límite de pasajeros por escalón; la tensión es la altura que sube cada persona y la carga espacial, cuántos caben.
- 🎯 **Por qué importa:** La velocidad de escape iónica crece con la raíz de la tensión, pero la corriente que cabe en una rejilla está limitada por la carga espacial. La decisión central: ¿qué tensión y qué área de rejilla se necesitan para un empuje dado y qué fracción del propelente llega a ser ion?

📘 **Dónde se aprende** (1 clase): [B78-C07 · Motores iónicos](../programa/clases/B78/B78-C07-motores-ionicos/CLASE.md).

### Tensión de Hubble

- La tensión de Hubble es la discrepancia entre los valores de `H₀` de dos métodos.
- La tensión de Hubble es la discrepancia entre el `H₀` local y el del fondo cósmico.

💡 **Cómo se explica en la clase [B26-C23](../programa/clases/B26/B26-C23-tensiones-observacionales-constante-de-hubble-y-s8/CLASE.md):**
- (S3) analizan modelos que reducen la tensión de Hubble a `1`–`2σ` con grados de libertad adicionales; observan que parte de la reducción proviene de incertidumbres mayores por degeneraciones, no solo de un desplazamiento de `H₀`, y no encuentran una solución claramente mejor (resumen).
- Descripción larga: la tensión de Hubble supera los 4σ y la de `S₈`, calculada de forma gruesa, ronda los 2,7σ.
- 🎯 **Por qué importa:** Decir «hay una tensión» solo tiene sentido con un número: ¿cuántas sigmas?, ¿qué probabilidad de ocurrir por azar?, ¿qué se asume? Sin ese rigor, una discrepancia se exagera o se descarta.

📘 **Dónde se aprende** (2 clases): [B01-C16 · Expansión del universo como observación](../programa/clases/B01/B01-C16-expansion-del-universo-como-observacion/CLASE.md); [B26-C23 · Tensiones observacionales: constante de Hubble y S8](../programa/clases/B26/B26-C23-tensiones-observacionales-constante-de-hubble-y-s8/CLASE.md).

### Tensión de von Mises

- La tensión de von Mises es `σ_vm = √(3 J₂)`.

💡 **Cómo se explica en la clase [B84-C22](../programa/clases/B84/B84-C22-tension-deformacion-y-elasticidad-lineal/CLASE.md):**
- El tensor `[[120,40,0],[40,−30,20],[0,20,60]] MPa` tiene tensiones principales `130,345; 63,292; −43,637 MPa`, cortante máximo `86,991 MPa` y von Mises `151,987 MPa`.
- Descripción larga: von Mises (152 MPa) supera la mayor tensión normal inicial (120 MPa) porque suma las componentes.
- 🎯 **Por qué importa:** Una tensión de 120 MPa en una dirección no dice si la pieza cede: la fluencia depende de la combinación de las seis componentes. La decisión central: ¿cede el material en este punto y con qué margen, dado un estado de tensión 3D?

📘 **Dónde se aprende** (1 clase): [B84-C22 · Tensión, deformación y elasticidad lineal](../programa/clases/B84/B84-C22-tension-deformacion-y-elasticidad-lineal/CLASE.md).

### Tensión específica

- La tensión específica `σ` es la fuerza por área, y la fuerza máxima es `F = σ A`.

💡 **Cómo se explica en la clase [B105-C03](../programa/clases/B105/B105-C03-atrofia-muscular/CLASE.md):**
- Un músculo grande de 70 cm² con tensión específica de 25 N/cm² (ambos ilustrativos) desarrolla 1.750 N.
- Convertir sección transversal en fuerza máxima con una tensión específica.
- 🎯 **Por qué importa:** Sin carga y sin aporte adecuado, el músculo se pierde más rápido que en la Tierra. La decisión central: ¿cuánta área y cuánta fuerza quedan tras 30, 90 y 180 días, y cuánto cambia una contramedida?

📘 **Dónde se aprende** (1 clase): [B105-C03 · Atrofia muscular](../programa/clases/B105/B105-C03-atrofia-muscular/CLASE.md).

### Tensión por pares

- La tensión por pares es `|μ_i − μ_j|/√(σ_i² + σ_j²)`.

💡 **Cómo se explica en la clase [B26-C21](../programa/clases/B26/B26-C21-verosimilitud-cosmologica-con-datos-combinados/CLASE.md):**
- Ejercicio 12 · integrador. Elabora tu *combinación de restricciones de `Ω_m`*: pesos, media ponderada, `σ`, `χ²`, p-valor, tensiones por pares y el efecto de una correlación, con una advertencia sobre las hipótesis.
- El script [combinar.py](combinar.py) calcula la media ponderada, la comprueba con una rejilla de `50 000` puntos (`10⁻⁴`), el `χ²` y el p-valor, las tensiones por pares y el efecto de la correlación (comprueba que `ρ = 0` reproduce la forma cerrada).
- 🎯 **Por qué importa:** Ninguna sonda fija sola todos los parámetros; combinarlas reduce la incertidumbre, pero solo si son compatibles entre sí y si se tratan bien sus correlaciones. La decisión central: dadas tres restricciones sobre `Ω_m`, ¿cuál es el valor combinado, qué incertidumbre tiene y son consistentes entre sí?

📘 **Dónde se aprende** (1 clase): [B26-C21 · Verosimilitud cosmológica con datos combinados](../programa/clases/B26/B26-C21-verosimilitud-cosmologica-con-datos-combinados/CLASE.md).

### Tensión reversible

- La tensión reversible `E₀ = −ΔG/(2F)` es el máximo de una celda ideal.

💡 **Cómo se explica en la clase [B86-C15](../programa/clases/B86/B86-C15-sistemas-de-combustible-como-alternativa/CLASE.md):**
- Calcular la tensión reversible y la eficiencia de una celda H₂/O₂ con la constante de Faraday.
- Tension reversible E0 = 1.2287 V ; tension termoneutra = 1.4811 V (valores de manual NO consultados, ilustrativos)
- 🎯 **Por qué importa:** Una batería guarda la energía y la entrega en la misma masa; una pila separa la potencia (la pila) de la energía (los reactivos). Para misiones largas esa separación puede ser más liviana, pero añade tanques, gestión del agua y complejidad.

📘 **Dónde se aprende** (1 clase): [B86-C15 · Sistemas de combustible como alternativa](../programa/clases/B86/B86-C15-sistemas-de-combustible-como-alternativa/CLASE.md).

### Tensión térmica

- La tensión térmica impedida es `σ = −EαΔT`.

💡 **Cómo se explica en la clase [B84-C28](../programa/clases/B84/B84-C28-condiciones-de-contorno-y-cargas-en-modelos-de-elementos-finitos/CLASE.md):**
- Calcular la tensión térmica de un elemento sobrerrestringido.
- El script [contorno.py](contorno.py) cuenta los modos de sólido rígido, compara cargas equivalentes, verifica reacciones y calcula la tensión térmica (comprueba 2, 1 y 0 modos rígidos, flecha consistente exacta (< 1e-9) y `σ_t = −EαΔT`).
- 🎯 **Por qué importa:** Una restricción de menos deja la matriz singular; una de más introduce tensiones falsas; una carga mal repartida cambia la flecha 1,25 %: son los errores más frecuentes en los modelos. La decisión central: ¿está el modelo bien restringido y cargado y cómo lo demuestro?

📘 **Dónde se aprende** (1 clase): [B84-C28 · Condiciones de contorno y cargas en modelos de elementos finitos](../programa/clases/B84/B84-C28-condiciones-de-contorno-y-cargas-en-modelos-de-elementos-finitos/CLASE.md).

### Tensión termoneutra

- La tensión termoneutra `E_tn = |ΔH|/(2F)` es aquella a la que la celda no intercambia calor con el entorno.
- La tensión termoneutra `−ΔH/(2F)` equivale al poder calorífico superior.

💡 **Cómo se explica en la clase [B59-C10](../programa/clases/B59/B59-C10-electrolisis-y-balances-energeticos/CLASE.md):**
- Como subir una cuesta: la tensión termoneutra es la altura de la cima; por debajo hay que tomar calor del entorno (viento a favor) y por encima se disipa calor (esfuerzo).
- *Descripción textual:* la entalpía fija la tensión termoneutra; la curva de polarización da la tensión de operación; su comparación indica si la celda absorbe o cede calor.
- 🎯 **Por qué importa:** La electrólisis es el mayor consumidor de energía de la planta. La decisión central: ¿a qué densidad de corriente conviene operar, entre una celda pequeña que gasta más electricidad y una grande que gasta menos?

📘 **Dónde se aprende** (2 clases): [B59-C10 · Electrólisis y balances energéticos](../programa/clases/B59/B59-C10-electrolisis-y-balances-energeticos/CLASE.md); [B86-C15 · Sistemas de combustible como alternativa](../programa/clases/B86/B86-C15-sistemas-de-combustible-como-alternativa/CLASE.md).

### Tensión viscosa

- La tensión viscosa es `τ = μ du/dy`.

🎯 **Por qué importa (clase B79-C03):** Casi todo flujo de ingeniería tiene paredes, y en ellas la viscosidad impone velocidad cero. Sin Navier–Stokes no hay arrastre ni fricción ni calentamiento por pared.

📘 **Dónde se aprende** (1 clase): [B79-C03 · Ecuaciones de Navier-Stokes](../programa/clases/B79/B79-C03-ecuaciones-de-navier-stokes/CLASE.md).

### Tensiones principales

- Las tensiones principales son los autovalores del tensor.

💡 **Cómo se explica en la clase [B84-C22](../programa/clases/B84/B84-C22-tension-deformacion-y-elasticidad-lineal/CLASE.md):**
- El tensor `[[120,40,0],[40,−30,20],[0,20,60]] MPa` tiene tensiones principales `130,345; 63,292; −43,637 MPa`, cortante máximo `86,991 MPa` y von Mises `151,987 MPa`.
- Obtener las tensiones principales de un tensor.
- 🎯 **Por qué importa:** Una tensión de 120 MPa en una dirección no dice si la pieza cede: la fluencia depende de la combinación de las seis componentes. La decisión central: ¿cede el material en este punto y con qué margen, dado un estado de tensión 3D?

📘 **Dónde se aprende** (1 clase): [B84-C22 · Tensión, deformación y elasticidad lineal](../programa/clases/B84/B84-C22-tension-deformacion-y-elasticidad-lineal/CLASE.md).

### Tensor cartesiano de rango 2

- Un tensor cartesiano de rango 2 es una colección `Tᵢⱼ` que, al girar los ejes con `R`, se transforma `T′ᵢⱼ = Rᵢₐ Rⱼ_b Tₐ_b`; un vector es de rango 1 y un escalar de rango 0.

🎯 **Por qué importa (clase B10-C17):** La inercia de un satélite frente a un giro depende de la dirección: se necesita nueve números ordenados en una matriz, y esos nueve números cambian si cambias los ejes del cuerpo, pero de forma que la física no cambie.

📘 **Dónde se aprende** (1 clase): [B10-C17 · Tensores y notación indicial](../programa/clases/B10/B10-C17-tensores-y-notacion-indicial/CLASE.md).

### Tensor de Einstein

- El tensor de Einstein es `G_ab = R_ab − R g_ab/2`.

🎯 **Por qué importa (clase B39-C05):** Las ecuaciones de campo conectan la geometría con la materia. La decisión central: ¿en qué régimen la gravedad de Einstein se reduce a la de Newton y qué garantiza la consistencia de las ecuaciones?

📘 **Dónde se aprende** (1 clase): [B39-C05 · Ecuaciones de campo de Einstein y límite newtoniano](../programa/clases/B39/B39-C05-ecuaciones-de-campo-de-einstein-y-limite-newtoniano/CLASE.md).

### Tensor de estructura

- Esquina: punto donde la intensidad varía en dos direcciones. Tensor de estructura: matriz `M` de productos de gradientes promediados en una ventana.

🎯 **Por qué importa (clase B99-C02):** Una esquina de una roca puede verse distinta cuando cambian el brillo, el ruido o el punto de vista, y dos rocas parecidas se confunden. La decisión central: ¿qué puntos conviene usar, cómo se describen y cuándo se acepta un emparejamiento?

📘 **Dónde se aprende** (1 clase): [B99-C02 · Detección y descriptores de características](../programa/clases/B99/B99-C02-deteccion-y-descriptores-de-caracteristicas/CLASE.md).

### Tensor de inercia

- El tensor de inercia es `Iᵢⱼ = Σₙ mₙ (rₙ·rₙ δᵢⱼ − rₙᵢ rₙⱼ)`.
- El tensor de inercia `I` (3×3, simétrico) reúne los momentos de inercia.
- Centro de masa (CG): punto promedio de la masa. Tensor de inercia: matriz de momentos y productos de inercia.

💡 **Cómo se explica en la clase [B10-C17](../programa/clases/B10/B10-C17-tensores-y-notacion-indicial/CLASE.md):**
- Su tensor de inercia permite calcular cuánta energía cuesta girarlo según el eje.
- Calcular el tensor de inercia de masas puntuales.
- 🎯 **Por qué importa:** La inercia de un satélite frente a un giro depende de la dirección: se necesita nueve números ordenados en una matriz, y esos nueve números cambian si cambias los ejes del cuerpo, pero de forma que la física no cambie.

📘 **Dónde se aprende** (3 clases): [B10-C17 · Tensores y notación indicial](../programa/clases/B10/B10-C17-tensores-y-notacion-indicial/CLASE.md); [B87-C01 · Dinámica de cuerpo rígido](../programa/clases/B87/B87-C01-dinamica-de-cuerpo-rigido/CLASE.md); [B90-C06 · Integración mecánica de subsistemas](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md).

### Tensor de marea

- El tensor de marea es el gradiente del campo gravitatorio: `Tᵢⱼ = ∂gᵢ/∂xⱼ = (GM/r³)(3 nᵢ nⱼ − δᵢⱼ)` con `n̂ = x/|x|`.

💡 **Cómo se explica en la clase [B10-C18](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md):**
- Un cuerpo alargado (inercia distinta según el eje) sometido a este tensor de marea tiende a alinear su eje de menor inercia con la vertical local.
- Construir el tensor de marea `T = (GM/r³)(3 n̂ n̂ − I)`.
- 🎯 **Por qué importa:** La gravedad no es uniforme a lo largo de un satélite: lo que está más cerca de la Tierra se acelera más que lo que está lejos, y lo que está a los lados se comprime. Con una sola derivada `dg/dr` solo describes la dirección radial; el tensor de marea describe las tres direcciones a la vez.

📘 **Dónde se aprende** (1 clase): [B10-C18 · Producto tensorial y contracción](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md).

### Tensor de Ricci

- El tensor de Ricci es `R_bd = R^a_bad`.

💡 **Cómo se explica en la clase [B39-C03](../programa/clases/B39/B39-C03-tensor-de-riemann-ricci-y-curvatura-escalar/CLASE.md):**
- python programa/clases/B39/B39-C03-tensor-de-riemann-ricci-y-curvatura-escalar/curvatura.py
- 🎯 **Por qué importa:** Un espacio-tiempo es curvo si el Riemann no se anula. La decisión central: ¿qué mide cada contracción del Riemann y cómo se comprueba un cálculo de curvatura?

📘 **Dónde se aprende** (1 clase): [B39-C03 · Tensor de Riemann, Ricci y curvatura escalar](../programa/clases/B39/B39-C03-tensor-de-riemann-ricci-y-curvatura-escalar/CLASE.md).

### Tensor de Riemann

- El tensor de Riemann `R^a_bcd` mide la no conmutación de las derivadas covariantes.

💡 **Cómo se explica en la clase [B39-C03](../programa/clases/B39/B39-C03-tensor-de-riemann-ricci-y-curvatura-escalar/CLASE.md):**
- python programa/clases/B39/B39-C03-tensor-de-riemann-ricci-y-curvatura-escalar/curvatura.py
- 🎯 **Por qué importa:** Un espacio-tiempo es curvo si el Riemann no se anula. La decisión central: ¿qué mide cada contracción del Riemann y cómo se comprueba un cálculo de curvatura?

📘 **Dónde se aprende** (1 clase): [B39-C03 · Tensor de Riemann, Ricci y curvatura escalar](../programa/clases/B39/B39-C03-tensor-de-riemann-ricci-y-curvatura-escalar/CLASE.md).

### Teorema central del límite

- El teorema central del límite afirma que, para variables independientes con varianza finita, la distribución de su suma (o promedio) se aproxima a una normal cuando el número de términos crece; el GUM lo enuncia así: la distribución de una combinación lineal de variables independientes es aproximadamente normal aunque las variables no lo sean (S1, G.2).

💡 **Cómo se explica en la clase [B12-C06](../programa/clases/B12/B12-C06-teorema-central-del-limite/CLASE.md):**
- Enunciar el teorema central del límite (TCL) con sus hipótesis.
- python programa/clases/B12/B12-C06-teorema-central-del-limite/tcl_promedios.py
- 🎯 **Por qué importa:** Ningún instrumento tiene ruido exactamente normal, y sin embargo casi todas las incertidumbres se expresan con campanas. La razón es que se reportan promedios y sumas de muchas contribuciones pequeñas.

📘 **Dónde se aprende** (1 clase): [B12-C06 · Teorema central del límite](../programa/clases/B12/B12-C06-teorema-central-del-limite/CLASE.md).

### Teorema de Bayes

- El teorema de Bayes es `P(H|x) = P(x|H)P(H)/ΣP(x|H')P(H')`.
- El teorema de Bayes dice que `P(θ | datos) = P(datos | θ) P(θ) / P(datos)`.

💡 **Cómo se explica en la clase [B12-C12](../programa/clases/B12/B12-C12-inferencia-bayesiana/CLASE.md):**
- Enunciar el teorema de Bayes y aplicarlo a eventos y a parámetros.
- 🎯 **Por qué importa:** Una misión rara vez parte de cero: hay pruebas en tierra, misiones anteriores y física conocida. Y a menudo el dato es escaso (diez intervalos, treinta pruebas).

📘 **Dónde se aprende** (2 clases): [B12-C12 · Inferencia bayesiana](../programa/clases/B12/B12-C12-inferencia-bayesiana/CLASE.md); [B55-C19 · Interpretación de firmas químicas](../programa/clases/B55/B55-C19-interpretacion-de-firmas-quimicas/CLASE.md).

### Teorema de Bussgang

- El teorema de Bussgang iguala `P_gm = b P_mm` para una transformación local de un campo gaussiano.

🎯 **Por qué importa (clase B36-C08):** Si se ignora el sesgo, la amplitud de la materia se sobreestima. La decisión central: ¿qué sesgo corresponde a un trazador y cómo se mide?

📘 **Dónde se aprende** (1 clase): [B36-C08 · Sesgo de galaxias y trazadores de la materia](../programa/clases/B36/B36-C08-sesgo-de-galaxias-y-trazadores-de-la-materia/CLASE.md).

### Teorema de ejecución exitosa

- El teorema de ejecución exitosa da `n = ln(1 − C)/ln R` para cero fallas.

🎯 **Por qué importa (clase B97-C18):** Declarar «el robot funciona» tras diez pruebas buenas no dice nada sin una confiabilidad y una confianza; y una prueba en la Tierra con el robot completo solo se parece a una en Marte si se corrige el peso.

📘 **Dónde se aprende** (1 clase): [B97-C18 · Pruebas en entornos análogos](../programa/clases/B97/B97-C18-pruebas-en-entornos-analogos/CLASE.md).

### Teorema de ejes paralelos

- El teorema de ejes paralelos traslada inercias.

💡 **Cómo se explica en la clase [B77-C22](../programa/clases/B77/B77-C22-centro-de-masa-y-su-variacion-con-el-consumo-de-propelente/CLASE.md):**
- Calcular la inercia de cabeceo con el teorema de ejes paralelos.
- ⚠️ **Error frecuente:** Olvidar el teorema de ejes paralelos. Se corrige con 8.2.
- 🎯 **Por qué importa:** El control de actitud se diseña para una masa, un centro de masa y una inercia que ya no son los mismos al final del quemado. La decisión central: ¿cuánto se mueve el centro de masa, cuánto cae la inercia y qué le pasa al margen?

📘 **Dónde se aprende** (1 clase): [B77-C22 · Centro de masa y su variación con el consumo de propelente](../programa/clases/B77/B77-C22-centro-de-masa-y-su-variacion-con-el-consumo-de-propelente/CLASE.md).

### Teorema de Fubini

- El teorema de Fubini permite cambiar el orden si `f` es continua (ec. 1.5.35).

🎯 **Por qué importa (clase B09-C18):** La masa de la Tierra se conoce mucho mejor que la distribución de esa masa en su interior. Un solo número, la densidad media, no basta: el momento de inercia depende de cómo se reparte la masa.

📘 **Dónde se aprende** (1 clase): [B09-C18 · Integrales dobles y triples](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md).

### Teorema de Gauss (divergencia)

- El teorema de Gauss (divergencia): `∭_V ∇·F dV = ∯_S F·n dA` (ec. 1.6.58).

💡 **Cómo se explica en la clase [B09-C19](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md):**
- Y los teoremas requieren campos diferenciables en toda la región: la superficie de Gauss no debe pasar por una singularidad.
- Enunciar y usar el teorema de Gauss con la gravedad: flujo `= −4πGM`.
- 🎯 **Por qué importa:** La gravedad no tiene fuentes fuera de la masa que la produce, y eso permite calcular la gravedad de un planeta esférico sin sumar cada átomo: basta medir el flujo. La rotación de la Tierra produce un campo de velocidades con circulación no nula, y esa circulación mide cuánto «gira» el campo.

📘 **Dónde se aprende** (1 clase): [B09-C19 · Cálculo vectorial introductorio](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md).

### Teorema de la capa

- El teorema de la capa (Newton): una capa esférica uniforme atrae a un punto exterior como si toda su masa estuviera en el centro y no atrae a un punto interior.

💡 **Cómo se explica en la clase [B09-C20](../programa/clases/B09/B09-C20-aplicaciones-a-campos-gravitatorios/CLASE.md):**
- Teorema de la capa y masa encerrada: sirve para esferas con perfil radial.
- Enunciar y verificar el teorema de la capa por integración.
- 🎯 **Por qué importa:** Una sonda en órbita, un satélite geodésico o un gravímetro en una montaña reciben la atracción de un cuerpo que no es un punto: tiene tamaño, forma achatada, rotación y estructura interna. Reducirlo a un punto es correcto fuera de una esfera homogénea, pero deja de serlo cuando importa el achatamiento o el interior.

📘 **Dónde se aprende** (1 clase): [B09-C20 · Aplicaciones a campos gravitatorios](../programa/clases/B09/B09-C20-aplicaciones-a-campos-gravitatorios/CLASE.md).

### Teorema de la ganancia pequeña

- El teorema de la ganancia pequeña dice que, si el lazo nominal es estable y `|Δ|·‖T‖∞ < 1` (para `Δ` constante o con `|Δ(jω)| ≤ δ`), el lazo con incertidumbre multiplicativa sigue estable: es una condición suficiente.

💡 **Cómo se explica en la clase [B16-C16](../programa/clases/B16/B16-C16-control-robusto-inicial/CLASE.md):**
- Aplicar el teorema de la ganancia pequeña y reconocer que es suficiente, no necesario.
- 🎯 **Por qué importa:** La inercia de un satélite cambia al desplegar paneles, consumir propergol o capturar una carga; el actuador envejece; el sensor tiene un retardo que no se conocía. El lazo diseñado con la inercia nominal debe seguir funcionando.

📘 **Dónde se aprende** (1 clase): [B16-C16 · Control robusto inicial](../programa/clases/B16/B16-C16-control-robusto-inicial/CLASE.md).

### Teorema de Lambert

- El teorema de Lambert dice que el tiempo de vuelo depende solo de `a`, `s` y `c` (no de la forma exacta de la elipse).

🎯 **Por qué importa (clase B82-C01):** Un diseñador de trayectorias conoce dónde está la nave y dónde debe estar, y cuánto tiempo tiene; no conoce la velocidad con que debe salir. La decisión central: ¿qué semieje y qué velocidad inicial hacen que la nave pase por `r2` exactamente a los `t` días?

📘 **Dónde se aprende** (1 clase): [B82-C01 · Lambert de arco corto](../programa/clases/B82/B82-C01-lambert-de-arco-corto/CLASE.md).

### Teorema de las derivadas mixtas

- El teorema de las derivadas mixtas dice que `f_xy = f_yx` si son continuas (ec. 1.5.6).

🎯 **Por qué importa (clase B09-C16):** La luminosidad de una estrella calculada con su radio y su temperatura tiene una incertidumbre que viene de las dos. ¿Cuál pesa más?

📘 **Dónde se aprende** (1 clase): [B09-C16 · Derivadas parciales](../programa/clases/B09/B09-C16-derivadas-parciales/CLASE.md).

### Teorema de Parseval

- El teorema de Parseval iguala la varianza en el espacio real y el de Fourier.

💡 **Cómo se explica en la clase [B36-C04](../programa/clases/B36/B36-C04-espectro-de-potencia-de-materia/CLASE.md):**
- La FFT propia coincide con una DFT directa de 16 puntos con error `4,24 × 10⁻¹⁴`, y el teorema de Parseval se cumple con error relativo `2,17 × 10⁻¹⁶`.
- 🎯 **Por qué importa:** Un espectro estimado sin su error no se puede comparar con un modelo. La decisión central: ¿está la desviación de cada intervalo dentro de la varianza cósmica?

📘 **Dónde se aprende** (1 clase): [B36-C04 · Espectro de potencia de materia](../programa/clases/B36/B36-C04-espectro-de-potencia-de-materia/CLASE.md).

### Teorema de Stokes

- El teorema de Stokes: `∬_S (∇×F)·n dA = ∮_{∂S} F·dr` (ec. 1.6.57).

💡 **Cómo se explica en la clase [B09-C19](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md):**
- Enunciar y usar el teorema de Stokes con la rotación terrestre.
- 🎯 **Por qué importa:** La gravedad no tiene fuentes fuera de la masa que la produce, y eso permite calcular la gravedad de un planeta esférico sin sumar cada átomo: basta medir el flujo. La rotación de la Tierra produce un campo de velocidades con circulación no nula, y esa circulación mide cuánto «gira» el campo.

📘 **Dónde se aprende** (1 clase): [B09-C19 · Cálculo vectorial introductorio](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md).

### Teorema del desplazamiento

- El teorema del desplazamiento: un término lineal en la fase mueve la PSF.

💡 **Cómo se explica en la clase [B42-C06](../programa/clases/B42/B42-C06-funcion-de-dispersion-puntual/CLASE.md):**
- Aplicar el teorema del desplazamiento a una inclinación.
- 🎯 **Por qué importa:** Toda imagen es la escena convolucionada con la PSF; si la PSF se degrada, se pierde resolución y contraste. La decisión central: ¿cómo se calcula la PSF de una pupila con aberraciones y cuándo basta el pico?

📘 **Dónde se aprende** (1 clase): [B42-C06 · Función de dispersión puntual](../programa/clases/B42/B42-C06-funcion-de-dispersion-puntual/CLASE.md).

### Teorema del valor intermedio

- El teorema del valor intermedio (TVI) dice que una función continua en `[a, b]` toma todos los valores entre `f(a)` y `f(b)`.

💡 **Cómo se explica en la clase [B09-C02](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md):**
- Aplicar el teorema del valor intermedio y localizar una raíz por bisección.
- 🎯 **Por qué importa:** Un vehículo espacial cambia de masa de dos maneras: gradualmente, al quemar propelente, y de golpe, al soltar una etapa vacía. Un modelo de trayectoria que ignore los saltos integra mal; uno que los trate como suaves, también.

📘 **Dónde se aprende** (1 clase): [B09-C02 · Continuidad y discontinuidad](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md).

### Teorema del virial

- El teorema del virial dice que, para un gas en equilibrio, `2K + Ω = 0`, con `K` la energía térmica total.
- El teorema del virial (C02) liga la energía térmica y la gravitatoria.
- El teorema del virial: `⟨K⟩ = (n/2)⟨V⟩`.

💡 **Cómo se explica en la clase [B24-C02](../programa/clases/B24/B24-C02-formacion-de-protoestrellas/CLASE.md):**
- Definir protoestrella, energía gravitatoria, teorema del virial y tiempo de Kelvin–Helmholtz.
- 🎯 **Por qué importa:** Una protoestrella brilla, pero no por el motor que alimenta al Sol. Para saber de dónde sale su energía, cuánto tiempo puede brillar así y cómo distinguirla de una estrella ya estable hay que seguir la energía gravitatoria.

📘 **Dónde se aprende** (3 clases): [B24-C02 · Formación de protoestrellas](../programa/clases/B24/B24-C02-formacion-de-protoestrellas/CLASE.md); [B24-C04 · Equilibrio hidrostático estelar](../programa/clases/B24/B24-C04-equilibrio-hidrostatico-estelar/CLASE.md); [B40-C06 · Campos escalares en cosmología: potenciales y evolución](../programa/clases/B40/B40-C06-campos-escalares-en-cosmologia-potenciales-y-evolucion/CLASE.md).

### Teorema fundamental del cálculo, parte 1

- El teorema fundamental del cálculo, parte 1: si `f` es continua en `[a, b]` y `F′ = f`, entonces `∫_a^b f dx = F(b) − F(a)` (S1, §1.4(v), ec. 1.4.26).

🎯 **Por qué importa (clase B09-C12):** Para que una sonda abandone la Tierra hay que darle energía suficiente para vencer la gravedad hasta una distancia infinita. Esa energía es una integral de la fuerza sobre una distancia sin cota superior.

📘 **Dónde se aprende** (1 clase): [B09-C12 · Teorema fundamental del cálculo](../programa/clases/B09/B09-C12-teorema-fundamental-del-calculo/CLASE.md).

### Teorema impulso–momento

- El teorema impulso–momento dice `J_neto = Δp`.

🎯 **Por qué importa (clase B05-C08):** Un cohete en el vacío no tiene nada contra lo que empujar y aun así acelera. La pregunta motivadora es: ¿cómo cambia la velocidad de un cuerpo cuando expulsa masa o cuando choca, si no hay fuerzas externas?

📘 **Dónde se aprende** (1 clase): [B05-C08 · Momento lineal e impulsos](../programa/clases/B05/B05-C08-momento-lineal-e-impulsos/CLASE.md).

### Teoría cuasi-lineal

- La teoría cuasi-lineal supone fases aleatorias y da `D_ql = K²/2`.

💡 **Cómo se explica en la clase [B73-C15](../programa/clases/B73/B73-C15-difusion-orbital/CLASE.md):**
- Descripción larga: la difusión es nula, normal o anómala según `K`; donde la teoría cuasi-lineal es exacta (fases aleatorias) el Monte Carlo la reproduce.
- Compararlo con la teoría cuasi-lineal `K²/2`.
- 🎯 **Por qué importa:** Un conjunto de cuerpos en una región caótica no escapa de golpe: su excentricidad o su semieje se esparce como una caminata aleatoria, y el tiempo que tarda en recorrer una región fija la escala de supervivencia de la población. La decisión central: ¿cómo medir un coeficiente de difusión y cuándo no tiene sentido hablar de él?

📘 **Dónde se aprende** (1 clase): [B73-C15 · Difusión orbital](../programa/clases/B73/B73-C15-difusion-orbital/CLASE.md).

### Teoría de elementos medios

- La teoría de elementos medios debe declararse: los elementos de un TLE solo son válidos con la teoría para la que se generaron.

💡 **Cómo se explica en la clase [B74-C29](../programa/clases/B74/B74-C29-formatos-tle-y-omm-de-elementos-orbitales/CLASE.md):**
- Límite: el TLE es un formato de elementos medios para una teoría de propagación; leer sus números como elementos osculadores de dos cuerpos es solo una aproximación de magnitud.
- 🎯 **Por qué importa:** Un TLE mal copiado o mal leído da una órbita equivocada sin avisar. La decisión central: ¿qué errores detecta la suma de verificación, qué resolución tiene cada campo y qué significan realmente esos «elementos medios»?

📘 **Dónde se aprende** (1 clase): [B74-C29 · Formatos TLE y OMM de elementos orbitales](../programa/clases/B74/B74-C29-formatos-tle-y-omm-de-elementos-orbitales/CLASE.md).

### Teoría de Laplace–Lagrange

- La teoría de Laplace–Lagrange promedia la perturbación y la linealiza en `e` e `I`; para el vector `z_j = e_j exp(iϖ_j)`, `dz/dt = i A z`.

🎯 **Por qué importa (clase B73-C11):** La excentricidad de una órbita varía durante millones de años por la atracción promediada de los demás planetas, y esa variación se vuelve violenta cuando una frecuencia propia coincide con la de precesión de un asteroide.

📘 **Dónde se aprende** (1 clase): [B73-C11 · Resonancias seculares](../programa/clases/B73/B73-C11-resonancias-seculares/CLASE.md).

### Teoría general de perturbaciones

- Una teoría general de perturbaciones resuelve analíticamente las perturbaciones con constantes ajustadas.

💡 **Cómo se explica en la clase [B72-C21](../programa/clases/B72/B72-C21-propagador-sgp4-y-teoria-general-de-perturbaciones/CLASE.md):**
- SGP4 es una teoría general de perturbaciones: aplica fórmulas analíticas con constantes fijadas, y por eso los elementos y el propagador forman un par inseparable.
- python programa/clases/B72/B72-C21-propagador-sgp4-y-teoria-general-de-perturbaciones/sgp4_elementos_medios.py
- 🎯 **Por qué importa:** Un error clásico es tomar los elementos de dos líneas como elementos keplerianos y propagarlos con dos cuerpos: el error es de kilómetros en minutos. La decisión central: ¿qué propagador corresponde a un conjunto de elementos y qué transformaciones previas exige antes de usarlo?

📘 **Dónde se aprende** (1 clase): [B72-C21 · Propagador SGP4 y teoría general de perturbaciones](../programa/clases/B72/B72-C21-propagador-sgp4-y-teoria-general-de-perturbaciones/CLASE.md).

### Tercer orden

- El tercer orden es el término en `h²`; el quinto orden, el de `h⁴`.

💡 **Cómo se explica en la clase [B50-C01](../programa/clases/B50/B50-C01-trazado-exacto-de-rayos-y-aberraciones-de-orden-superior/CLASE.md):**
- La LSA a `h = 4` es `4,004` veces la de `h = 2` (la teoría de tercer orden da 4) y a `h = 10`, `25,19` veces (la de tercer orden daría 25): la diferencia es el orden superior.
- 🎯 **Por qué importa:** Un diseño que solo se calcula en aproximación paraxial es optimista: ignora lo que ocurre lejos del eje. La decisión central: ¿cuánta de la aberración de una lente es de tercer orden y cuánta es de orden superior?

📘 **Dónde se aprende** (1 clase): [B50-C01 · Trazado exacto de rayos y aberraciones de orden superior](../programa/clases/B50/B50-C01-trazado-exacto-de-rayos-y-aberraciones-de-orden-superior/CLASE.md).

### Tercera ley de Kepler

- La tercera ley de Kepler dice que `T²` es proporcional a `a³` para todos los cuerpos que orbitan el mismo astro.
- La tercera ley de Kepler afirma que, para los cuerpos que orbitan el mismo astro, `T²/a³` es constante.
- La tercera ley de Kepler (versión circular) afirma que `T²/r³ = 4π²/GM` es constante para todos los cuerpos que orbitan el mismo astro.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C10](../programa/clases/B05/B05-C10-gravitacion-universal/CLASE.md):**
- Deducir la tercera ley de Kepler para órbitas circulares.
- 🎯 **Por qué importa:** La misma fuerza que hace caer una manzana mantiene a la Luna en órbita: esa idea unificó el cielo y la Tierra. La pregunta motivadora es: ¿cómo comprobar con números que la gravedad de la superficie y la órbita de la Luna son la misma fuerza?

📘 **Dónde se aprende** (4 clases): [B01-C13 · Sistema solar como sistema físico](../programa/clases/B01/B01-C13-sistema-solar-como-sistema-fisico/CLASE.md); [B03-C04 · Potencias y raíces](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md); [B05-C10 · Gravitación universal](../programa/clases/B05/B05-C10-gravitacion-universal/CLASE.md); [B52-C07 · Resonancias orbitales](../programa/clases/B52/B52-C07-resonancias-orbitales/CLASE.md).

### Terciaria

- Una fuente primaria es contemporánea del hecho; una secundaria lo relata desde otra; una terciaria compila secundarias.

💡 **Cómo se explica en la clase [B132-C01](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md):**
- Se asigna `peso = tipo × exp(−distancia/τ) × (1 − sesgo)`, con tipo 1,0 (primaria), 0,6 (secundaria) y 0,3 (terciaria).
- Por tipo: primaria, secundaria o terciaria.
- 🎯 **Por qué importa:** Un relato histórico es tan fiable como las fuentes que lo sostienen, y tres copias de una misma fuente no son tres fuentes. La decisión central: ¿cuánto apoyo da realmente un conjunto de fuentes a una afirmación y cuánto de ese apoyo es robusto ante cambios razonables de criterio?

📘 **Dónde se aprende** (1 clase): [B132-C01 · Crítica histórica de fuentes y método historiográfico](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md).

### Termalización

- La termalización es la fracción de la energía que se convierte en luz.

💡 **Cómo se explica en la clase [B28-C18](../programa/clases/B28/B28-C18-interpretacion-de-kilonovas/CLASE.md):**
- ⚠️ **Error frecuente:** Olvidar la termalización. Se corrige con el ejercicio 1.
- 🎯 **Por qué importa:** La escala de tiempo y el brillo de una kilonova dependen de la masa eyectada y de su velocidad. Entender esa relación permite estimar ambos a partir de la curva de luz.

📘 **Dónde se aprende** (1 clase): [B28-C18 · Interpretación de kilonovas](../programa/clases/B28/B28-C18-interpretacion-de-kilonovas/CLASE.md).

### Térmica

- La eficiencia óptica y la térmica miran las pérdidas de la óptica y del absorbedor.

💡 **Cómo se explica en la clase [B78-C13](../programa/clases/B78/B78-C13-propulsion-solar-termica/CLASE.md):**
- *Descripción textual:* la irradiancia y el área dan la potencia térmica; con la temperatura fija el caudal; la temperatura y la masa molar fijan el escape; caudal y escape dan el empuje y el balance exige que la potencia del chorro no supere la térmica.
- Límite: el gas se expande en una tobera y la energía térmica se convierte en cinética con pérdidas.
- 🎯 **Por qué importa:** La energía llega por la óptica y el propelente solo la transporta; el escape depende de la temperatura que resistan los materiales y de la masa molar. La decisión central: ¿qué empuje e `Isp` da un colector de área dada y cómo se compara con un propulsor eléctrico alimentado con la misma potencia?

📘 **Dónde se aprende** (1 clase): [B78-C13 · Propulsión solar térmica](../programa/clases/B78/B78-C13-propulsion-solar-termica/CLASE.md).

### Térmico

- Tiene tres subsistemas: oxígeno (suministro y regulación de presión), ventilación (circula gas, retira CO₂ y vapor) y térmico (rechaza el calor, en la prueba con un evaporador de membrana, SWME).

💡 **Cómo se explica en la clase [B108-C01](../programa/clases/B108/B108-C01-sistemas-portatiles-de-soporte-vital-plss/CLASE.md):**
- Límite: se supone que todo el calor metabólico se rechaza por el sistema térmico, sin pérdidas por el traje.
- Nombrar los tres subsistemas de un PLSS: oxígeno, ventilación y térmico.
- 🎯 **Por qué importa:** B106-C09 trata el soporte vital de hábitat; el del traje no tiene clase. La decisión central: ¿cuánto oxígeno, cuánto calor a rechazar y cuánto CO₂ genera una EVA con un perfil de esfuerzo dado, y qué margen deja el sistema?

📘 **Dónde se aprende** (1 clase): [B108-C01 · Sistemas portátiles de soporte vital (PLSS)](../programa/clases/B108/B108-C01-sistemas-portatiles-de-soporte-vital-plss/CLASE.md).

### Terminador

- El terminador es el límite entre el día y la noche de un cuerpo.

🎯 **Por qué importa (clase B131-C05):** Un modelo es útil por lo que conserva y engañoso por lo que deforma. La decisión central: ¿qué propiedad del cielo conserva tu demostración y cuál sacrifica?

📘 **Dónde se aprende** (1 clase): [B131-C05 · Demostraciones visuales y modelos para el aula](../programa/clases/B131/B131-C05-demostraciones-visuales-y-modelos-para-el-aula/CLASE.md).

### Terminal

- La terminal (o consola) es un programa donde escribes comandos de texto; el intérprete de comandos (*shell*), como bash o PowerShell, los ejecuta.

💡 **Cómo se explica en la clase [B07-C15](../programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/CLASE.md):**
- Ejemplo real de esta clase, en la carpeta C15 de un equipo Windows: bash mostró una ruta con barras `/c/dev/.../B07-C15-terminal-y-rutas-de-archivos` y PowerShell, la misma carpeta como `C:\dev\...\B07-C15-terminal-y-rutas-de-archivos`.
- Paso 1. Desde la raíz del repositorio: `python programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/rutas_pathlib.py`.
- 🎯 **Por qué importa:** Una causa muy común de «el programa no encuentra el archivo» es que la ruta funciona en el computador del autor y no en otro: se escribió con `C:\Usuarios\ana\datos\...`, o se asumió que el programa se ejecuta desde cierta carpeta.

📘 **Dónde se aprende** (1 clase): [B07-C15 · Terminal y rutas de archivos](../programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/CLASE.md).

### Terminan

- Las ramas parten de los polos de `P` (con `K=0`) y terminan en los ceros de `P` o van al infinito siguiendo asíntotas.

💡 **Cómo se explica en la clase [B16-C09](../programa/clases/B16/B16-C09-lugar-de-las-raices/CLASE.md):**
- Para `K` muy grande, las `n − m` ramas que no terminan en ceros (aquí 3, porque `P` no tiene ceros) se alinean con rectas desde el centroide `σ = (Σ polos − Σ ceros)/(n − m) = (0 − 1 − 2)/3 = −1`, con ángulos `(2k+1)·180°/(n − m) = 60°, 180°, 300°`.
- No: las asíntotas son verticales en `−1,25`, en el semiplano izquierdo, así que todas las ramas terminan en el semiplano izquierdo.
- 🎯 **Por qué importa:** Subir la ganancia de un lazo hace que responda más rápido, pero también más oscilante, hasta que se desestabiliza. Para decidir cuánta ganancia usar necesitas ver el compromiso de un vistazo.

📘 **Dónde se aprende** (1 clase): [B16-C09 · Lugar de las raíces](../programa/clases/B16/B16-C09-lugar-de-las-raices/CLASE.md).

### Término

- Un término es cada sumando (`3a`, `−5`).

💡 **Cómo se explica en la clase [B03-C13](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md):**
- Reducir términos semejantes y aplicar la propiedad distributiva.
- ⚠️ **Error frecuente:** Olvidar el término cruzado `2ab`. Ejercicios 6 y 8.
- 🎯 **Por qué importa:** ¿Cuánto tarda una señal en llegar desde la Tierra hasta Marte? Depende de dónde estén los dos planetas.

📘 **Dónde se aprende** (1 clase): [B03-C13 · Expresiones algebraicas iniciales](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md).

### Término acotado uniforme

- Un término acotado uniforme `±a` tiene `σ = a/√3`.

💡 **Cómo se explica en la clase [B87-C22](../programa/clases/B87/B87-C22-presupuesto-de-error-de-apuntamiento/CLASE.md):**
- Verificar la combinación por Monte Carlo, incluido un término uniforme acotado.
- 🎯 **Por qué importa:** Un requisito de apuntamiento solo se cumple si el diseño lo respalda con números. La decisión central: ¿qué contribuyentes dominan, cómo se combinan (suma lineal o cuadrática), con qué margen se cumple el requisito y qué ocurre con dos ejes?

📘 **Dónde se aprende** (1 clase): [B87-C22 · Presupuesto de error de apuntamiento](../programa/clases/B87/B87-C22-presupuesto-de-error-de-apuntamiento/CLASE.md).

### Término cuadrático

- El término cuadrático `aN²` representa los fragmentos por colisión.

💡 **Cómo se explica en la clase [B118-C10](../programa/clases/B118/B118-C10-sindrome-de-kessler-como-escenario/CLASE.md):**
- Con `S = 150` el equilibrio estable baja a 3944 (menos de la mitad: el término cuadrático también se reduce).
- 🎯 **Por qué importa:** El término cuadrático de las colisiones cambia la naturaleza del problema: por debajo de cierta fuente hay un equilibrio estable; por encima, no hay equilibrio. La decisión central: ¿qué parámetro (fuente, vida orbital, tasa de colisión) lleva el sistema al umbral y cómo se lee un escenario sin confundirlo con un pronóstico?

📘 **Dónde se aprende** (1 clase): [B118-C10 · Síndrome de Kessler como escenario](../programa/clases/B118/B118-C10-sindrome-de-kessler-como-escenario/CLASE.md).

### Término de color

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B45-C21](../programa/clases/B45/B45-C21-estandares-fotometricos-y-sistemas-de-referencia/CLASE.md):**
- Con `v = 17,654` y `B−V = 0,80`: `V = 20,820`; sin el término de color sería `20,860` (diferencia `0,041 mag`).
- Reconocer el efecto de ignorar el término de color.
- ⚠️ **Error frecuente:** Ignorar el término de color. Se corrige con 8.3.
- 🎯 **Por qué importa:** Sin estándares la escala de un cielo concreto es arbitraria. La decisión central: ¿qué ecuación de transformación se ajusta y con qué error en la magnitud final?

📘 **Dónde se aprende** (1 clase): [B45-C21 · Estándares fotométricos y sistemas de referencia](../programa/clases/B45/B45-C21-estandares-fotometricos-y-sistemas-de-referencia/CLASE.md).

### Término de transporte

- El término de transporte `ω × r` es la velocidad de arrastre de un marco giratorio.

🎯 **Por qué importa (clase B10-C16):** Una estación terrestre tiene coordenadas fijas en la Tierra. Un satélite se propaga en un sistema inercial, donde las leyes de Newton valen.

📘 **Dónde se aprende** (1 clase): [B10-C16 · Transformación de marcos de referencia](../programa/clases/B10/B10-C16-transformacion-de-marcos-de-referencia/CLASE.md).

### Término dominante

- El término dominante es el que más contribuye al error.

🎯 **Por qué importa (clase B29-C10):** Una densidad con 28 % de incertidumbre no distingue una roca de un mundo con agua. Saber de qué medida depende el error orienta la inversión de observación.

📘 **Dónde se aprende** (1 clase): [B29-C10 · Masas y radios planetarios](../programa/clases/B29/B29-C10-masas-y-radios-planetarios/CLASE.md).

### Término fuente

- El término fuente `s(z,t)` es lo que hay que añadir a la ecuación para que la función elegida sea solución: `s = T*_t − κ T*_zz`.

💡 **Cómo se explica en la clase [B23-C04](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md):**
- Detectar defectos de frontera o de término fuente por la caída del orden.
- 🎯 **Por qué importa:** Un modelo de conducción de calor en el regolito, con una fuente variable y una condición de flujo en el borde, no tiene solución cerrada. Pero su código puede estar mal en la frontera, en el término fuente o en el tiempo, y ninguna propiedad global lo delata fácilmente.

📘 **Dónde se aprende** (1 clase): [B23-C04 · Soluciones de referencia y manufactured solutions](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md).

### Término independiente

- `a₀` es el término independiente (el valor cuando `x = 0`).

💡 **Cómo se explica en la clase [B04-C01](../programa/clases/B04/B04-C01-polinomios-y-factorizacion/CLASE.md):**
- Para `x³ − 6x² + 11x − 6`: se prueban divisores del término independiente (±1, ±2, ±3, ±6);
- Regla de las raíces racionales. Si el polinomio tiene coeficientes enteros y una raíz `p/q` en fracción irreducible, `p` divide al término independiente y `q` al coeficiente principal.
- 🎯 **Por qué importa:** Cuando un observatorio publica dónde está inclinado el eje de la Tierra, no da un solo número: da una *fórmula* para cada fecha, porque ese eje se mueve lentamente. Esa fórmula es un polinomio.

📘 **Dónde se aprende** (1 clase): [B04-C01 · Polinomios y factorización](../programa/clases/B04/B04-C01-polinomios-y-factorizacion/CLASE.md).

### Término indirecto

- El término indirecto es la aceleración del Sol por la estrella, que debe restarse en el marco heliocéntrico.

💡 **Cómo se explica en la clase [B52-C16](../programa/clases/B52/B52-C16-nube-de-oort/CLASE.md):**
- Integrarlo con RK4 incluyendo el término indirecto y comparar.
- El script [oort.py](oort.py) calcula el periodo y la velocidad de afelio, el impulso impulsivo y lo contrasta con una integración RK4 con término indirecto (comprueba `5 %`).
- ⚠️ **Error frecuente:** Olvidar el término indirecto. Se corrige con 8.2.
- 🎯 **Por qué importa:** Las perturbaciones estelares explican cómo cometas casi circulares en la nube pasan a órbitas que cruzan el Sistema Solar interior. La decisión central: ¿cuánto cambia la velocidad de un cometa de la nube con el paso de una estrella y qué efecto tiene en su perihelio?

📘 **Dónde se aprende** (1 clase): [B52-C16 · Nube de Oort](../programa/clases/B52/B52-C16-nube-de-oort/CLASE.md).

### Términos

- Los términos del modelo: IA y IE (ceros de acimut y altura), CA (colimación), NPAE (no perpendicularidad de ejes), AN y AW (inclinación del eje vertical al norte y al oeste) y TF (flexión del tubo).

💡 **Cómo se explica en la clase [B43-C26](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md):**
- Los errores formales más grandes son los de `CA` y `NPAE`, que están más correlacionados con otros términos.
- *Descripción textual:* el modelo lineal se ajusta a los desvíos medidos; la covarianza da la incertidumbre de cada término.
- ⚠️ **Error frecuente:** Omitir términos. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** El modelo convierte errores de decenas de segundos de arco en residuos de segundos de arco. La decisión central: ¿qué términos incluir, cuántas estrellas medir y con qué incertidumbre se determina cada parámetro?

📘 **Dónde se aprende** (1 clase): [B43-C26 · Modelo de flexiones y de apuntado de una montura](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md).

### Términos semejantes

- Los términos semejantes tienen la misma parte literal y se pueden reducir (`3a + 2a = 5a`).

💡 **Cómo se explica en la clase [B03-C13](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md):**
- Reducir términos semejantes y aplicar la propiedad distributiva.
- ⚠️ **Error frecuente:** Sumar términos no semejantes. Sección 8.3.
- 🎯 **Por qué importa:** ¿Cuánto tarda una señal en llegar desde la Tierra hasta Marte? Depende de dónde estén los dos planetas.

📘 **Dónde se aprende** (1 clase): [B03-C13 · Expresiones algebraicas iniciales](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md).

### Termófilo

- Un termófilo tiene óptimo moderadamente alto y un hipertermófilo muy alto (los intervalos exactos varían por autor; aquí no se fijan).

💡 **Cómo se explica en la clase [B64-C02](../programa/clases/B64/B64-C02-termofilos-e-hipertermofilos/CLASE.md):**
- Definir las temperaturas cardinales y los intervalos térmicos de termófilos e hipertermófilos.
- El script [termofilos.py](termofilos.py) genera datos sintéticos con ruido, ajusta `Eₐ` por dos vías, halla `T_opt` por sección áurea y barrido, e integra Clausius–Clapeyron con RK4 (comprueba 3 %, 0,05 K y 1e-6).
- 🎯 **Por qué importa:** Un hipertermófilo crece donde casi todo lo demás muere, pero el agua hierve a 100 °C a presión ambiente. La pregunta motivadora: ¿qué fija el límite superior de temperatura de la vida y cómo se mide ese límite?

📘 **Dónde se aprende** (1 clase): [B64-C02 · Termófilos e hipertermófilos](../programa/clases/B64/B64-C02-termofilos-e-hipertermofilos/CLASE.md).

### Termogravimetría (TGA)

- La termogravimetría (TGA) mide la masa de una muestra mientras sube la temperatura.

🎯 **Por qué importa (clase B59-C03):** No toda el agua es igual de fácil de extraer: el hielo sale con poco calor y el hidroxilo exige temperaturas casi de fusión. La decisión central: ¿qué parte del agua total se obtiene calentando solo hasta 300 K?

📘 **Dónde se aprende** (1 clase): [B59-C03 · Agua en regolito y minerales](../programa/clases/B59/B59-C03-agua-en-regolito-y-minerales/CLASE.md).

### Termómetro de resistencia de platino patrón

- Un termómetro de resistencia de platino patrón mide de `−200 °C` a `1000 °C` tras calibrarse en esos puntos (S2).

🎯 **Por qué importa (clase B13-C16):** Un sensor de temperatura pegado a un panel de una nave devuelve una resistencia. Convertirla en kelvin exige calibrarlo contra referencias conocidas, y comprobar que la temperatura medida concuerda con un balance térmico previsto.

📘 **Dónde se aprende** (1 clase): [B13-C16 · Calibración térmica](../programa/clases/B13/B13-C16-calibracion-termica/CLASE.md).

### Termostato

- El termostato conmuta con histéresis: enciende a `T_on` y apaga a `T_off`.

💡 **Cómo se explica en la clase [B85-C08](../programa/clases/B85/B85-C08-calentadores-y-termostatos/CLASE.md):**
- T["T del nodo"] --> S["Termostato: ON ≤ 278 K, OFF ≥ 283 K"]
- *Descripción textual:* la temperatura del nodo realimenta al termostato, que decide la potencia; el nodo integra el balance.
- ⚠️ **Error frecuente:** Olvidar la histéresis. sin ella el termostato conmuta sin parar (8.2)
- 🎯 **Por qué importa:** Un calentador pequeño no sostiene la temperatura y uno grande gasta energía que una batería no tiene. La decisión central: ¿cuánta potencia de calentador mantiene la temperatura mínima en el peor eclipse y cuánta energía cuesta por órbita?

📘 **Dónde se aprende** (1 clase): [B85-C08 · Calentadores y termostatos](../programa/clases/B85/B85-C08-calentadores-y-termostatos/CLASE.md).

### Terrazas

- Un pico central es una elevación en el centro; las terrazas son escalones de la pared.

💡 **Cómo se explica en la clase [B61-C03](../programa/clases/B61/B61-C03-crateres-complejos-colapso-picos-centrales-y-terrazas/CLASE.md):**
- Describir la morfología simple y la compleja (terrazas, fondo plano, pico central).
- python programa/clases/B61/B61-C03-crateres-complejos-colapso-picos-centrales-y-terrazas/colapso.py
- 🎯 **Por qué importa:** Sin la transición simple–compleja no se puede interpretar la forma de un cráter grande ni comparar cuerpos. La decisión central: ¿a qué diámetro cambia la morfología y cómo depende de la gravedad?

📘 **Dónde se aprende** (1 clase): [B61-C03 · Cráteres complejos: colapso, picos centrales y terrazas](../programa/clases/B61/B61-C03-crateres-complejos-colapso-picos-centrales-y-terrazas/CLASE.md).

### Terreno periódico

- Un terreno periódico produce picos repetidos.

💡 **Cómo se explica en la clase [B74-C26](../programa/clases/B74/B74-C26-navegacion-por-hitos-y-correlacion-de-terreno/CLASE.md):**
- En un terreno periódico de 16 px, el pico (`0,970`) y el segundo (`0,968`) casi coinciden (razón `1,00`): el desplazamiento hallado en `y` es `12,00` frente a `−3,82` verdadero: se confunde un periodo.
- En un terreno periódico, la razón pico/segundo pico es `1,00` y el desplazamiento hallado (`(5,37, 12,00)`) falla en `y` por un periodo.
- ⚠️ **Error frecuente:** Fiarse del valor del pico. En terreno periódico es alto y engañoso; ver 8.4.
- 🎯 **Por qué importa:** Un buen pico de correlación no garantiza un buen emparejamiento: en un terreno repetitivo hay dos picos casi iguales. La decisión central: ¿cuánta precisión da la correlación en un terreno rico, y cuándo el emparejamiento es ambiguo y no debe usarse?

📘 **Dónde se aprende** (1 clase): [B74-C26 · Navegación por hitos y correlación de terreno](../programa/clases/B74/B74-C26-navegacion-por-hitos-y-correlacion-de-terreno/CLASE.md).

### Territorio

- El territorio, en esta clase, es el lugar concreto desde el que se mira; para quienes lo habitan puede significar mucho más de lo que una geometría recoge.

💡 **Cómo se explica en la clase [B133-C01](../programa/clases/B133/B133-C01-relaciones-entre-cielo-y-territorio-en-los-saberes-tradicionales/CLASE.md):**
- Describir un saber ligado a un territorio sin generalizarlo a otros pueblos.
- python programa/clases/B133/B133-C01-relaciones-entre-cielo-y-territorio-en-los-saberes-tradicionales/orto_solar.py
- 🎯 **Por qué importa:** Los saberes del cielo se enseñan a menudo como listas de constelaciones o de relatos sueltos, sin el territorio que los sostiene. La decisión central: ¿qué puede decir una geometría astronómica sobre una práctica ligada a un lugar, y qué le corresponde decir solo a quienes la portan?

📘 **Dónde se aprende** (1 clase): [B133-C01 · Relaciones entre cielo y territorio en los saberes tradicionales](../programa/clases/B133/B133-C01-relaciones-entre-cielo-y-territorio-en-los-saberes-tradicionales/CLASE.md).

### Tesela

- Una tesela (*tile*) es un bloque rectangular del ráster guardado de forma contigua.

💡 **Cómo se explica en la clase [B14-C26](../programa/clases/B14/B14-C26-formatos-de-datos-raster-geoespaciales-geotiff-y-cog/CLASE.md):**
- El archivo didáctico guarda 64 teselas de 128 × 128 `float32` (65 536 bytes cada una) tras una cabecera y un directorio de 64 pares (desplazamiento, bytes).
- La región filas 200–299 y columnas 700–819 cubre las teselas de fila 1 y 2 y de columna 5 y 6: 4 teselas.
- ⚠️ **Error frecuente:** Ignorar el tamaño de tesela. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Una escena de satélite pesa cientos de megabytes y tú necesitas un recuadro de 100 × 120 píxeles. Si el formato obliga a leer todo el archivo, gastas tiempo y ancho de banda.

📘 **Dónde se aprende** (1 clase): [B14-C26 · Formatos de datos ráster geoespaciales: GeoTIFF y COG](../programa/clases/B14/B14-C26-formatos-de-datos-raster-geoespaciales-geotiff-y-cog/CLASE.md).

### Teselado

- El teselado es la elección de los campos.

💡 **Cómo se explica en la clase [B28-C15](../programa/clases/B28/B28-C15-busqueda-de-contrapartidas-opticas/CLASE.md):**
- La evidencia es el plan de teselado con su cobertura del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *plan de teselado con su cobertura*: tabla de cobertura, profundidad y detectabilidad para siete valores de `k` y el plan elegido.
- 🎯 **Por qué importa:** Observar más campos cubre más probabilidad, pero cada campo recibe menos tiempo y es menos profundo. Si la fuente es débil, el exceso de campos hace que no se vea.

📘 **Dónde se aprende** (1 clase): [B28-C15 · Búsqueda de contrapartidas ópticas](../programa/clases/B28/B28-C15-busqueda-de-contrapartidas-opticas/CLASE.md).

### Testigo

- Un testigo es un cilindro de roca extraído con una broca.

💡 **Cómo se explica en la clase [B63-C02](../programa/clases/B63/B63-C02-muestreo-superficial-y-estrategias-de-recoleccion/CLASE.md):**
- *Descripción textual:* las fracciones de área determinan la probabilidad de captura, de ella salen el número mínimo de muestras y las litologías esperadas, y con la masa del testigo se arma el plan.
- Un testigo ilustrativo mide `13 mm` de diámetro y `60 mm` de largo y la roca tiene `2,7 g/cm³`.
- 🎯 **Por qué importa:** Un rover tiene un número limitado de tubos. La decisión central: ¿cuántas muestras hacen falta para no perderse una litología rara con una confianza dada?

📘 **Dónde se aprende** (1 clase): [B63-C02 · Muestreo superficial y estrategias de recolección](../programa/clases/B63/B63-C02-muestreo-superficial-y-estrategias-de-recoleccion/CLASE.md).

### Tetraédrica

- Las formas básicas son lineal (2 dominios, 180°), trigonal plana (3, 120°) y tetraédrica (4, 109,47°).

💡 **Cómo se explica en la clase [B06-C05](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md):**
- Con 4, la geometría electrónica es tetraédrica; si todos son enlaces, la forma también lo es (109,47°); si hay un par solitario, la forma es piramidal; si hay dos, angular.
- D3 --> D4["4 dominios: tetraédrica, 109,47°"]
- 🎯 **Por qué importa:** El dióxido de carbono es el 95,1 % de la atmósfera de Marte en volumen (S2), y los hielos de las nubes densas del medio interestelar contienen, según un estudio con el telescopio James Webb, agua y CO₂ entre otras especies (S3, que se leyó sólo en resumen).

📘 **Dónde se aprende** (1 clase): [B06-C05 · Moléculas y geometría molecular](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md).

### Texto alternativo

- Un texto alternativo describe el gráfico a quien no lo ve.
- El texto alternativo es la descripción de la imagen para quien no la ve.
- El texto alternativo (`alt`) es la descripción de una imagen.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C15](../programa/clases/B03/B03-C15-representacion-cartesiana-de-datos/CLASE.md):**
- Un gráfico accesible: no depende solo del color (usa forma y etiqueta), lleva un texto alternativo, y se acompaña de una tabla con los mismos datos.
- Texto alternativo propuesto: «Gráfico de dispersión con ejes logarítmicos.
- 🎯 **Por qué importa:** Las fichas de la NASA dan semiejes y períodos de los ocho planetas. En una tabla son 16 números.

📘 **Dónde se aprende** (4 clases): [B03-C15 · Representación cartesiana de datos](../programa/clases/B03/B03-C15-representacion-cartesiana-de-datos/CLASE.md); [B07-C10 · Gráficos bidimensionales iniciales](../programa/clases/B07/B07-C10-graficos-bidimensionales-iniciales/CLASE.md); [B128-C04 · Documentos y contenidos para lectores de pantalla](../programa/clases/B128/B128-C04-documentos-y-contenidos-para-lectores-de-pantalla/CLASE.md); [B130-C04 · Divulgación científica en redes sociales](../programa/clases/B130/B130-C04-divulgacion-cientifica-en-redes-sociales/CLASE.md).

### Texto de enlace

- El texto de enlace es lo que se lee al recorrer los enlaces.

💡 **Cómo se explica en la clase [B128-C04](../programa/clases/B128/B128-C04-documentos-y-contenidos-para-lectores-de-pantalla/CLASE.md):**
- enlace con texto generico ('haz clic aqui')
- enlace con texto generico ('mas informacion')
- 🎯 **Por qué importa:** Una imagen sin texto alternativo, una tabla sin encabezados o un enlace «haz clic aquí» no se ven como problema a simple vista pero dejan a una persona sin la información. La decisión central: ¿qué comprobaciones mínimas puedo automatizar y qué debo revisar a mano?

📘 **Dónde se aprende** (1 clase): [B128-C04 · Documentos y contenidos para lectores de pantalla](../programa/clases/B128/B128-C04-documentos-y-contenidos-para-lectores-de-pantalla/CLASE.md).

### Texto grande

- La razón de contraste `(L₁ + 0,05)/(L₂ + 0,05)` va de 1 a 21. Texto grande es de al menos 18 pt, o 14 pt en negrita.

💡 **Cómo se explica en la clase [B128-C06](../programa/clases/B128/B128-C06-contraste-y-color-accesibles/CLASE.md):**
- Texto normal: 4,5:1; texto grande: 3:1; componentes gráficos y estados necesarios: 3:1 (criterio 1.4.11).
- Aplicar los umbrales de 4,5:1 (texto) y 3:1 (texto grande y gráficos).
- 🎯 **Por qué importa:** Un texto gris claro sobre blanco, un azul puro sobre negro o una leyenda donde solo cambia el tono se pierden para quien tiene baja visión, daltonismo o una pantalla poco luminosa. La decisión central: ¿cómo compruebo con números que un par de colores se lee, y cuándo el color no basta?

📘 **Dónde se aprende** (1 clase): [B128-C06 · Contraste y color accesibles](../programa/clases/B128/B128-C06-contraste-y-color-accesibles/CLASE.md).

### TF

- Los términos del modelo: IA y IE (ceros de acimut y altura), CA (colimación), NPAE (no perpendicularidad de ejes), AN y AW (inclinación del eje vertical al norte y al oeste) y TF (flexión del tubo).

💡 **Cómo se explica en la clase [B43-C26](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md):**
- Montura sintética con `IA = 120"`, `IE = −80"`, `CA = 45"`, `NPAE = 20"`, `AN = 30"`, `AW = −25"` y `TF = 15"`, con 60 estrellas y ruido gaussiano de `1"` (el ruido realmente inyectado resulta de `1,162"` con la semilla).
- 🎯 **Por qué importa:** El modelo convierte errores de decenas de segundos de arco en residuos de segundos de arco. La decisión central: ¿qué términos incluir, cuántas estrellas medir y con qué incertidumbre se determina cada parámetro?

📘 **Dónde se aprende** (1 clase): [B43-C26 · Modelo de flexiones y de apuntado de una montura](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md).

### TID

- La TID es la dosis ionizante total.

💡 **Cómo se explica en la clase [B88-C03](../programa/clases/B88/B88-C03-procesadores-tolerantes-a-radiacion/CLASE.md):**
- Ejercicio 11 · transferencia. Transferencia. ¿Qué diferencia hay entre SEU y TID?
- TID es acumulativa y degrada el componente.
- ⚠️ **Error frecuente:** Confundir SEU con TID. SEU es instantáneo y TID acumulativo (ejercicio 11)
- 🎯 **Por qué importa:** Un procesador comercial puede fallar en órbita por una sola partícula. La decisión central: ¿cuántos eventos esperar al año y qué margen de dosis hay respecto del fallo del componente?

📘 **Dónde se aprende** (2 clases): [B88-C03 · Procesadores tolerantes a radiación](../programa/clases/B88/B88-C03-procesadores-tolerantes-a-radiacion/CLASE.md); [B95-C02 · Componentes comerciales en vuelo: selección y riesgo](../programa/clases/B95/B95-C02-componentes-comerciales-en-vuelo-seleccion-y-riesgo/CLASE.md).

### Tiempo

- El tiempo es `t = Δv/a`.

💡 **Cómo se explica en la clase [B81-C10](../programa/clases/B81/B81-C10-funciones-objetivo-de-diseno-de-trayectorias/CLASE.md):**
- Si el único criterio fuera el tiempo con tope de potencia de 5 kW, `a = 2,04 × 10⁻⁴`, `t = 227,0 d` y 747,88 kg.
- *Descripción textual:* la aceleración fija la potencia (y con ella la masa del sistema) y el tiempo; ambos entran en un objetivo compuesto cuyo mínimo es el diseño óptimo.
- 🎯 **Por qué importa:** Optimizar mal es optimizar el objetivo equivocado: mínimo `Δv` no es mínimo costo ni mínimo tiempo. La decisión central: ¿qué objetivo refleja lo que la misión valora y cómo cambia el diseño al cambiar sus pesos?

📘 **Dónde se aprende** (1 clase): [B81-C10 · Funciones objetivo de diseño de trayectorias](../programa/clases/B81/B81-C10-funciones-objetivo-de-diseno-de-trayectorias/CLASE.md).

### Tiempo a temperatura constante

- Meseta (*dwell*): tiempo a temperatura constante. Estabilización: estado donde la unidad ya no cambia apreciablemente.

🎯 **Por qué importa (clase B90-C11):** Una prueba funcional hecha antes de que la unidad se estabilice no demuestra nada sobre la temperatura extrema; una espera excesiva consume cámara y calendario. La decisión central: ¿cuánto debe esperar el ensayo para que la temperatura de la unidad sea la de la prueba?

📘 **Dónde se aprende** (1 clase): [B90-C11 · Ensayos térmicos](../programa/clases/B90/B90-C11-ensayos-termicos/CLASE.md).

### Tiempo acumulado

- El tiempo acumulado incluye las funciones llamadas; el propio (*tottime*) no.

💡 **Cómo se explica en la clase [B14-C14](../programa/clases/B14/B14-C14-vectorizacion-y-rendimiento/CLASE.md):**
- perfilado (cProfile): 200 000 llamadas a append (0,047 s) y a math.sqrt (0,042 s), tiempo acumulado del bucle 0,219 s con sobrecarga del perfilador
- 🎯 **Por qué importa:** Una función que calcula la distancia de 200 000 posiciones tarda medio minuto en tu cuaderno, y alguien propone «comprar un servidor». La pregunta motivadora es: ¿es el cálculo lento por su matemática o por cómo lo escribí, y cuánto puedo ganar sin cambiar el resultado?

📘 **Dónde se aprende** (1 clase): [B14-C14 · Vectorización y rendimiento](../programa/clases/B14/B14-C14-vectorizacion-y-rendimiento/CLASE.md).

### Tiempo al p %

- El tiempo al `p` % es `ln(L/(100 − p))/k`.

💡 **Cómo se explica en la clase [B105-C17](../programa/clases/B105/B105-C17-rehabilitacion-posterior-al-vuelo/CLASE.md):**
- Bootstrap de 2.000 repeticiones: `k` entre 0,0300 y 0,0631 (p2,5–p97,5) y `L` entre 23,5 y 32,3; tiempo al 95 %: mediana 38,7 d, intervalo 29,0–52,5 d.
- *Descripción textual:* las mediciones dan el déficit; su logaritmo es lineal en el tiempo; la recta da `L` y `k`, de ahí la semivida y los tiempos de recuperación, y el bootstrap cuantifica su incertidumbre.
- ⚠️ **Error frecuente:** Informar un tiempo sin su intervalo. Da el bootstrap (8.3).
- 🎯 **Por qué importa:** Prometer una fecha de recuperación sin su incertidumbre es engañoso: unas pocas mediciones ruidosas dan intervalos amplios. La decisión central: ¿cuánto tarda en recuperarse el 95 % y con qué incertidumbre, y cómo cambia para una persona lenta?

📘 **Dónde se aprende** (1 clase): [B105-C17 · Rehabilitación posterior al vuelo](../programa/clases/B105/B105-C17-rehabilitacion-posterior-al-vuelo/CLASE.md).

### Tiempo Atómico Internacional (TAI)

- El Tiempo Atómico Internacional (TAI) es una cuenta continua de segundos del SI desde un origen (medianoche del 1 de enero de 1958 según S3).

🎯 **Por qué importa (clase B13-C08):** Una efeméride planetaria se tabula en una escala de tiempo; el reloj civil usa otra; y la hora de una nave, otra distinta. Si usas la escala equivocada, una posición calculada para la Luna se desplaza: un segundo de diferencia son unos mil metros de movimiento orbital lunar.

📘 **Dónde se aprende** (1 clase): [B13-C08 · Escalas UTC, TAI, TT y TDB](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md).

### Tiempo coordenado

- El tiempo coordenado `t` es el de un marco respecto del cual el objeto se mueve.
- El tiempo coordenado `t` es el del observador lejano.

💡 **Cómo se explica en la clase [B26-C03](../programa/clases/B26/B26-C03-dilatacion-temporal-y-contraccion/CLASE.md):**
- Distinguir tiempo propio de tiempo coordenado.
- 🎯 **Por qué importa:** Los muones se producen en la alta atmósfera por rayos cósmicos, viven microsegundos y, sin embargo, llegan al suelo en cantidad. Los relojes de satélites de navegación se ajustan por el mismo efecto.

📘 **Dónde se aprende** (2 clases): [B26-C03 · Dilatación temporal y contracción](../programa/clases/B26/B26-C03-dilatacion-temporal-y-contraccion/CLASE.md); [B27-C08 · Horizonte de sucesos](../programa/clases/B27/B27-C08-horizonte-de-sucesos/CLASE.md).

### Tiempo de agotamiento

- El tiempo de agotamiento es `t_dep = Σ_gas/Σ_SFR`.

💡 **Cómo se explica en la clase [B25-C05](../programa/clases/B25/B25-C05-regiones-de-formacion-estelar/CLASE.md):**
- Con `Σ_SFR ∝ Σ_gas^N` y `N = 1,4` (S1), el tiempo de agotamiento `t_dep ∝ Σ_gas^{1−N} = Σ_gas^{−0,4}`: un gas diez veces más denso se agota `10^{0,4} = 2,5` veces antes, a `0,40` del tiempo.
- *Descripción textual:* el radio sale de igualar fotones emitidos con recombinaciones en el volumen; por otro lado, la ley de Schmidt da el ritmo de formación y de él el tiempo de agotamiento.
- 🎯 **Por qué importa:** Una galaxia no convierte todo su gas en estrellas a la vez: lo hace a un ritmo que puede medirse y comparar. Entender las regiones donde nacen las estrellas masivas permite reconocerlas desde lejos, y entender la relación entre gas y ritmo de formación permite saber cuánto tiempo puede una galaxia seguir formando estrellas.

📘 **Dónde se aprende** (1 clase): [B25-C05 · Regiones de formación estelar](../programa/clases/B25/B25-C05-regiones-de-formacion-estelar/CLASE.md).

### Tiempo de Alfvén

- El tiempo de Alfvén `τ_A = L/v_A`.

💡 **Cómo se explica en la clase [B30-C11](../programa/clases/B30/B30-C11-reconexion-magnetica/CLASE.md):**
- Con una hoja ilustrativa de `L = 10⁷ m` y `v_A = 10⁶ m/s`, el tiempo de Alfvén vale `τ_A = 10 s`.
- 🎯 **Por qué importa:** Las erupciones liberan en minutos una energía que el campo guardó durante mucho más tiempo, y el modelo más simple de reconexión es demasiado lento para eso. La decisión central: ¿qué tasa de reconexión hace falta y qué dice el modelo de Sweet–Parker?

📘 **Dónde se aprende** (1 clase): [B30-C11 · Reconexión magnética](../programa/clases/B30/B30-C11-reconexion-magnetica/CLASE.md).

### Tiempo de asentamiento

- El sobreimpulso `Mp` es cuánto excede la respuesta a su valor final (en fracción), el tiempo de pico `tp` es cuándo ocurre, el tiempo de subida `tr` es el que tarda entre 10 % y 90 % del valor final y el tiempo de asentamiento `ts` es el que tarda en quedar dentro de ±2 % para siempre.
- El tiempo de asentamiento es el último instante fuera de ±2 %.
- El sobreimpulso, el tiempo de pico y el tiempo de asentamiento.

💡 **Cómo se explica en la clase [B16-C04](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md):**
- El asentamiento al 2 % se aproxima por `ts ≈ 4/(ζ ωn)`, una aproximación (la envolvente a ese tiempo vale 2 %, pero la sinusoide fluctúa).
- Obtener `ωn` y `ζ` de un sistema de segundo orden y predecir sobreimpulso, tiempo de pico y de asentamiento.
- 🎯 **Por qué importa:** Tras girar un telescopio hacia una estrella nueva, los instrumentos no pueden empezar a exponer hasta que el apuntamiento se haya asentado. Cada segundo de espera cuesta tiempo de observación.

📘 **Dónde se aprende** (3 clases): [B16-C04 · Respuesta transitoria y estacionaria](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md); [B43-C15 · Motores paso a paso y servomotores](../programa/clases/B43/B43-C15-motores-paso-a-paso-y-servomotores/CLASE.md); [B88-C19 · Simulación hardware-in-the-loop](../programa/clases/B88/B88-C19-simulacion-hardware-in-the-loop/CLASE.md).

### Tiempo de asentamiento al 95 %

- El tiempo de asentamiento al 95 % es `τ ln 20`.

💡 **Cómo se explica en la clase [B85-C26](../programa/clases/B85/B85-C26-analisis-termico-transitorio-y-casos-extremos/CLASE.md):**
- Ejercicio 4 · autónomo. Calcula el tiempo de asentamiento al `99 %`.
- 🎯 **Por qué importa:** El peor caso de temperatura casi nunca es el de régimen. La decisión central: ¿qué paso de tiempo y qué esquema dan una respuesta fiable y cuál es la temperatura extrema en el eclipse o en el arranque?

📘 **Dónde se aprende** (1 clase): [B85-C26 · Análisis térmico transitorio y casos extremos](../programa/clases/B85/B85-C26-analisis-termico-transitorio-y-casos-extremos/CLASE.md).

### Tiempo de autocorrelación integrado

- El tiempo de autocorrelación integrado `τ = 1 + 2 Σ_{t≥1} ρ_t` mide cuántos pasos equivalen a una muestra independiente; el tamaño muestral efectivo es `ESS = N/τ`.

💡 **Cómo se explica en la clase [B12-C23](../programa/clases/B12/B12-C23-diagnostico-de-convergencia-y-reproducibilidad-de-cadenas-mcmc/CLASE.md):**
- Calcular el tiempo de autocorrelación integrado y el `ESS`.
- 🎯 **Por qué importa:** Un análisis MCMC cuya cadena no convergió da intervalos falsos con apariencia de precisión; y uno que no se puede repetir es irrevisable. En una misión, un parámetro estimado con cadenas defectuosas puede determinar una maniobra o un diagnóstico de salud de un instrumento.

📘 **Dónde se aprende** (1 clase): [B12-C23 · Diagnóstico de convergencia y reproducibilidad de cadenas MCMC](../programa/clases/B12/B12-C23-diagnostico-de-convergencia-y-reproducibilidad-de-cadenas-mcmc/CLASE.md).

### Tiempo de aviso

- El tiempo de aviso es el intervalo entre la alerta y el evento.
- El tiempo de aviso es el intervalo hasta el posible impacto.
- El tiempo de aviso es el margen hasta el posible impacto.

💡 **Cómo se explica en la clase [B58-C17](../programa/clases/B58/B58-C17-principios-de-mitigacion-y-desviacion/CLASE.md):**
- *Descripción textual:* un cambio de velocidad tangencial cambia el semieje, el periodo y el movimiento medio; el desplazamiento acumulado crece con el tiempo de aviso.
- Calcular el `Δv` necesario según el tiempo de aviso.
- 🎯 **Por qué importa:** Lo que importa no es el tamaño del empuje sino cuándo se da: el desplazamiento crece con el tiempo de aviso. La decisión central: ¿qué `Δv` y cuántos años de aviso se necesitan para mover un objeto lo suficiente?

📘 **Dónde se aprende** (3 clases): [B57-C34 · Alertas tempranas y ética en el monitoreo de desastres](../programa/clases/B57/B57-C34-alertas-tempranas-y-etica-en-el-monitoreo-de-desastres/CLASE.md); [B58-C17 · Principios de mitigación y desviación](../programa/clases/B58/B58-C17-principios-de-mitigacion-y-desviacion/CLASE.md); [B58-C18 · Marco internacional de defensa planetaria](../programa/clases/B58/B58-C18-marco-internacional-de-defensa-planetaria/CLASE.md).

### Tiempo de caída libre

- El tiempo de caída libre `t_ff` es lo que tarda una esfera uniforme en colapsar si la presión desaparece.
- El tiempo de caída libre es el de colapso sin presión.
- El tiempo de caída libre `t_ff` es lo que tarda en colapsar una esfera uniforme sin presión.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B24-C01](../programa/clases/B24/B24-C01-colapso-de-nubes-moleculares/CLASE.md):**
- Con ellos el laboratorio da una densidad de `4,68 × 10⁻¹⁷ kg/m³`, una velocidad del sonido de `188 m/s`, una masa de Jeans de `2,6 M☉` y un tiempo de caída libre de `0,31 Myr`.
- Calcular el tiempo de caída libre y explicar por qué solo depende de la densidad.
- 🎯 **Por qué importa:** Toda estrella es un trozo de gas interestelar que se contrajo. Sin saber cuándo la gravedad vence a la presión no se entiende por qué las estrellas nacen en nubes frías y densas y no en el gas tenue del medio interestelar, ni por qué la masa de las estrellas depende del entorno.

📘 **Dónde se aprende** (4 clases): [B24-C01 · Colapso de nubes moleculares](../programa/clases/B24/B24-C01-colapso-de-nubes-moleculares/CLASE.md); [B27-C15 · Supernovas de colapso](../programa/clases/B27/B27-C15-supernovas-de-colapso/CLASE.md); [B30-C01 · Estructura interna del Sol](../programa/clases/B30/B30-C01-estructura-interna-del-sol/CLASE.md); [B52-C01 · Colapso de nebulosa protosolar](../programa/clases/B52/B52-C01-colapso-de-nebulosa-protosolar/CLASE.md).

### Tiempo de calidad

- El tiempo de calidad `t*` es el tiempo hasta que la profundidad media cae al 80 % de la inicial (criterio ilustrativo).

💡 **Cómo se explica en la clase [B117-C01](../programa/clases/B117/B117-C01-primeros-auxilios-y-procedimientos-basicos-en-entorno-espacial/CLASE.md):**
- *Descripción textual:* de la profundidad inicial y la fatiga sale el tiempo de calidad, de él los turnos de relevo y el número de reanimadores; el dispositivo se compara aparte.
- Calcular el tiempo de calidad `t*` con una fórmula y comprobarlo numéricamente.
- 🎯 **Por qué importa:** Ninguna clase anterior trata primeros auxilios en microgravedad. La decisión central: ¿cuánto tiempo puede sostener un reanimador una compresión de calidad y cuándo hay que relevarlo?

📘 **Dónde se aprende** (1 clase): [B117-C01 · Primeros auxilios y procedimientos básicos en entorno espacial](../programa/clases/B117/B117-C01-primeros-auxilios-y-procedimientos-basicos-en-entorno-espacial/CLASE.md).

### Tiempo de captura

- El tiempo de captura es el que tarda en bajar de `0,5 °/s`.

💡 **Cómo se explica en la clase [B87-C16](../programa/clases/B87/B87-C16-detumbling-despues-del-despliegue/CLASE.md):**
- Ejercicio 12 · integrador. Integrador. Integrador. Elabora tu *curva de la velocidad angular en el detumbling*: tabla de 8.3, tiempo de captura, energía y lista de consultado y sintético.
- El script [bdot.py](bdot.py) integra con RK4 el cuerpo rígido con la ley `m = −k Ḃ` (ganancia `2×10⁵`, `m_max = 0,2 A·m²`) durante 4 órbitas, mide `|ω|` en cada órbita, el tiempo para `0,5 °/s` y la energía (comprueba captura, `|ω_final| < 0,5 °/s` y energía final `< 1 %` de la inicial).
- 🎯 **Por qué importa:** Sin estimador de actitud ni giroscopio calibrado, el satélite recién desplegado necesita detenerse con lo mínimo. La decisión central: ¿cuánto tarda, qué ganancia usar y qué velocidad residual queda?

📘 **Dónde se aprende** (1 clase): [B87-C16 · Detumbling después del despliegue](../programa/clases/B87/B87-C16-detumbling-despues-del-despliegue/CLASE.md).

### Tiempo de carga

- El tiempo de carga `t = C |V|/J`.

💡 **Cómo se explica en la clase [B85-C15](../programa/clases/B85/B85-C15-electrificacion-superficial/CLASE.md):**
- Estimar la capacidad y el tiempo de carga de un dieléctrico.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de potencial de una superficie*: corrientes, `V` en LEO y GEO con segunda vía, tiempo de carga, campo y lista de lo consultado, ilustrativo y no consultado.
- 🎯 **Por qué importa:** Una carga diferencial de kilovoltios entre superficies puede producir una descarga que daña la electrónica. La decisión central: ¿a qué potencial flota una superficie en un plasma dado y es probable que alcance un umbral de riesgo?

📘 **Dónde se aprende** (1 clase): [B85-C15 · Electrificación superficial](../programa/clases/B85/B85-C15-electrificacion-superficial/CLASE.md).

### Tiempo de coherencia

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C12](../programa/clases/B42/B42-C12-parametro-de-fried/CLASE.md):**
- *Descripción textual:* un perfil de turbulencia integrado produce `r₀`, de donde salen seeing, escalado, tiempo de coherencia y varianza de fase.
- 🎯 **Por qué importa:** `r₀` decide cuántos actuadores y qué tasa de muestreo necesita la óptica adaptativa. La decisión central: ¿cómo se obtiene `r₀`, cómo escala con `λ` y qué implica para la apertura y el lazo?

📘 **Dónde se aprende** (1 clase): [B42-C12 · Parámetro de Fried](../programa/clases/B42/B42-C12-parametro-de-fried/CLASE.md).

### Tiempo de combustión

- El tiempo de combustión `t_b` es la masa de propelente dividida por el gasto másico.
- El tiempo de combustión `t_b` es la duración del empuje.

💡 **Cómo se explica en la clase [B77-C05](../programa/clases/B77/B77-C05-ecuacion-de-cohete-ideal/CLASE.md):**
- Delta_v ideal = 7903.226 m/s; tiempo de combustion = 205.94 s; perdida g0 tb = 2019.58 m/s
- 🎯 **Por qué importa:** El propelente es casi toda la masa de un lanzador porque la velocidad crece solo con el logaritmo de la razón de masas. La decisión central: ¿qué razón de masas y qué `Isp` hacen falta para un `ΔV` dado, y qué parte se pierde por gravedad?

📘 **Dónde se aprende** (2 clases): [B77-C05 · Ecuación de cohete ideal](../programa/clases/B77/B77-C05-ecuacion-de-cohete-ideal/CLASE.md); [B77-C08 · Pérdidas gravitacionales](../programa/clases/B77/B77-C08-perdidas-gravitacionales/CLASE.md).

### Tiempo de correlación

- El tiempo de correlación es el número de muestras tras el cual la autocorrelación cae por debajo de un umbral.

💡 **Cómo se explica en la clase [B15-C03](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md):**
- El «tiempo de correlación» para `r_k < 0,1` es `k > ln 0,1/ln φ`; con `φ = 0,9`, `k ≥ 22` muestras.
- El AR(1) queda un 5,5 % por debajo de la teoría asintótica porque `N = 256` no es «grande» frente al tiempo de correlación (~20 muestras) y porque con 400 realizaciones la propia desviación tiene un error relativo de unos 3,5 %.
- 🎯 **Por qué importa:** Una regla heredada de la física del laboratorio dice que, al promediar `N` mediciones, el error baja como `1/√N`. Esa regla solo vale si los errores de cada medición son independientes.

📘 **Dónde se aprende** (1 clase): [B15-C03 · Ruido blanco y coloreado](../programa/clases/B15/B15-C03-ruido-blanco-y-coloreado/CLASE.md).

### Tiempo de crecimiento

- El tiempo de crecimiento (e-folding) es `1/λ` en unidades de tiempo del sistema.

💡 **Cómo se explica en la clase [B73-C04](../programa/clases/B73/B73-C04-estabilidad-local-de-lagrange/CLASE.md):**
- Convertir un autovalor en un tiempo de crecimiento en días.
- Ejercicio 4 · autónomo. Tiempo de crecimiento de L2 Sol–Tierra.
- 🎯 **Por qué importa:** Que un punto sea de equilibrio no dice si una nave se queda o se va. Los autovalores dicen cuánto tiempo tienes antes de corregir la posición y si un grupo de asteroides puede quedarse en L4.

📘 **Dónde se aprende** (1 clase): [B73-C04 · Estabilidad local de Lagrange](../programa/clases/B73/B73-C04-estabilidad-local-de-lagrange/CLASE.md).

### Tiempo de cruce

- El tiempo de cruce es `r/σ`.
- El tiempo de cruce es el número de órbitas interiores hasta el primer encuentro.

💡 **Cómo se explica en la clase [B25-C13](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md):**
- El tiempo de cruce de `1,09 Gyr` indica que el sistema ha podido cruzarse varias veces, pero no que esté relajado.
- Calcular una fracción de gas y un tiempo de cruce.
- 🎯 **Por qué importa:** Los cúmulos de galaxias son las mayores estructuras ligadas por la gravedad. Contienen galaxias, un gas a decenas de millones de kelvin y mucha más masa de la que ambos aportan; por eso sirven para estudiar la materia oscura y poner a prueba el modelo cosmológico.

📘 **Dónde se aprende** (2 clases): [B25-C13 · Cúmulos de galaxias](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md); [B73-C17 · Estabilidad de sistemas exoplanetarios](../programa/clases/B73/B73-C17-estabilidad-de-sistemas-exoplanetarios/CLASE.md).

### Tiempo de decaimiento

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B30-C18):** Prever la profundidad y la duración de una tormenta orienta la protección de redes y satélites. La decisión central: ¿qué mínimo alcanza `Dst*` y cuánto tarda en recuperarse?

📘 **Dónde se aprende** (1 clase): [B30-C18 · Tormentas geomagnéticas](../programa/clases/B30/B30-C18-tormentas-geomagneticas/CLASE.md).

### Tiempo de decaimiento óhmico

- El tiempo de decaimiento óhmico es la escala en que un campo desaparece si no se regenera.

🎯 **Por qué importa (clase B65-C02):** La presencia o ausencia de un campo global dice si un cuerpo tiene un fluido conductor en movimiento. La decisión central: ¿qué intensidad de campo permite un núcleo y cuánto duraría ese campo si el movimiento se detuviera?

📘 **Dónde se aprende** (1 clase): [B65-C02 · Dinamos planetarias y campos magnéticos de origen interno](../programa/clases/B65/B65-C02-dinamos-planetarias-y-campos-magneticos-de-origen-interno/CLASE.md).

### Tiempo de detección

- El tiempo de detección es el mínimo de seguimiento para que `|m|/u(m)` supere un umbral (aquí `3`).

💡 **Cómo se explica en la clase [B13-C23](../programa/clases/B13/B13-C23-estabilidad-y-deriva-temporal-de-instrumentos/CLASE.md):**
- Calcular la incertidumbre de la pendiente y el tiempo de detección a 3σ.
- El script [deriva_instrumental.py](deriva_instrumental.py) genera la serie de diez años, ajusta la tendencia, comprueba que sin ruido la recta se recupera a `10⁻¹²`, calcula la relación `|m|/u(m)` por duración, el tiempo de detección a 3σ y verifica que la cobertura 1σ simulada coincide con `0,683`.
- 🎯 **Por qué importa:** Un detector espacial lleva años en órbita. Su sensibilidad cambia lentamente por daño de radiación, contaminación y envejecimiento.

📘 **Dónde se aprende** (1 clase): [B13-C23 · Estabilidad y deriva temporal de instrumentos](../programa/clases/B13/B13-C23-estabilidad-y-deriva-temporal-de-instrumentos/CLASE.md).

### Tiempo de difusión

- El tiempo de difusión es `L²/α` salvo un factor numérico.
- El tiempo de difusión `t = R²/(ℓ c)` es lo que tarda un fotón en salir de una región de tamaño `R`.
- El tiempo de difusión para recorrer `Δ` es `τ = Δ²/D`.

💡 **Cómo se explica en la clase [B11-C13](../programa/clases/B11/B11-C13-ecuaciones-en-derivadas-parciales/CLASE.md):**
- Obtener el tiempo característico de difusión de una placa.
- tiempo de difusión del modo fundamental tau = L^2/(pi^2 alpha) = 253.3 s ; u(L/2, tau) = 0.36788 (1/e = 0.36788)
- 🎯 **Por qué importa:** El calor que atraviesa un escudo, las ondas en una estructura, el potencial gravitatorio de un cuerpo extenso, el transporte de partículas en un plasma: todos son EDP. Antes de discretizar hay que saber *qué tipo de problema es* (qué datos pide, cómo viaja la información) porque de ello depende el método.

📘 **Dónde se aprende** (4 clases): [B11-C13 · Ecuaciones en derivadas parciales](../programa/clases/B11/B11-C13-ecuaciones-en-derivadas-parciales/CLASE.md); [B24-C05 · Transporte radiativo y convectivo](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md); [B28-C18 · Interpretación de kilonovas](../programa/clases/B28/B28-C18-interpretacion-de-kilonovas/CLASE.md); [B73-C15 · Difusión orbital](../programa/clases/B73/B73-C15-difusion-orbital/CLASE.md).

### Tiempo de Einstein

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B29-C05):** La microlente detecta planetas fríos y lejanos que ni el tránsito ni la velocidad radial alcanzan, aunque cada evento no se repite. La decisión central: ¿cuánto vale la escala de un evento, con qué precisión se recuperan sus parámetros y qué duración tendría el efecto de un planeta?

📘 **Dónde se aprende** (1 clase): [B29-C05 · Microlentes gravitacionales](../programa/clases/B29/B29-C05-microlentes-gravitacionales/CLASE.md).

### Tiempo de empuje

- El tiempo de empuje es `m Δv/F`.
- El tiempo de empuje `t` es el tiempo total de funcionamiento.

💡 **Cómo se explica en la clase [B78-C11](../programa/clases/B78/B78-C11-micropropulsion-para-cubesat/CLASE.md):**
- *Descripción textual:* el Δv y la masa del satélite con el `Isp` dan el propelente; el empuje elegido da el tiempo; la potencia disponible limita el empuje eléctrico; el propelente fija masa y volumen.
- Descripción larga: el propelente baja una decena de veces del gas frío al eléctrico, pero el tiempo de empuje pasa de horas a días.
- ⚠️ **Error frecuente:** Olvidar el tiempo de empuje. Se corrige con 8.1.
- 🎯 **Por qué importa:** Un propulsor de alto `Isp` ahorra propelente pero empuja poco y tarda semanas; uno de empuje alto gasta más volumen de propelente. La decisión central: ¿qué tecnología cumple un Δv dado con una masa, un volumen y una potencia que un CubeSat sí puede dar?

📘 **Dónde se aprende** (2 clases): [B78-C11 · Micropropulsión para CubeSat](../programa/clases/B78/B78-C11-micropropulsion-para-cubesat/CLASE.md); [B78-C15 · Propulsión nuclear eléctrica conceptual](../programa/clases/B78/B78-C15-propulsion-nuclear-electrica-conceptual/CLASE.md).

### Tiempo de enfriamiento

- El tiempo de enfriamiento `γ m_e c²/P`.
- El tiempo de enfriamiento `t_c` limita el largo: `L = ū t_c`.

💡 **Cómo se explica en la clase [B27-C12](../programa/clases/B27/B27-C12-radiacion-sincrotron/CLASE.md):**
- *Descripción textual:* el campo y el factor de Lorentz fijan la potencia, la frecuencia crítica y el tiempo de enfriamiento; el núcleo `F` integrado sobre una población da una ley de potencias.
- Con `B = 10⁻⁹ T` (`U_B = 3,979 × 10⁻¹³ J/m³`) y `γ = 10⁷`, `P = 1,058 × 10⁻¹⁸ W`, `ν_c = 4,199 × 10¹⁵ Hz` y un tiempo de enfriamiento de `2,45 × 10⁴ años`.
- 🎯 **Por qué importa:** El índice espectral de una fuente sincrotrón entrega el índice de energía de sus electrones; la frecuencia crítica entrega `γ²B`. Sin estas relaciones no se puede leer un espectro de radio o rayos X.

📘 **Dónde se aprende** (2 clases): [B27-C12 · Radiación sincrotrón](../programa/clases/B27/B27-C12-radiacion-sincrotron/CLASE.md); [B53-C11 · Vulcanismo extraterrestre](../programa/clases/B53/B53-C11-vulcanismo-extraterrestre/CLASE.md).

### Tiempo de escaneo

- El tiempo de escaneo `t_esc ≈ N_s ln N_s / k_s` es una estimación heurística del tiempo para recorrer un grano.

💡 **Cómo se explica en la clase [B55-C07](../programa/clases/B55/B55-C07-catalisis-en-superficies/CLASE.md):**
- Estimar el tiempo de escaneo de un grano.
- Ejercicio 7 · autónomo. ¿Por qué el tiempo de escaneo crece con `N_s`?
- 🎯 **Por qué importa:** En fase gaseosa dos átomos de H casi nunca forman H₂ al chocar (no pueden disipar la energía), y sin embargo el H₂ es la molécula más abundante: se forma en la superficie de los granos. La decisión central: ¿en qué intervalo de temperatura un grano puede formar H₂, y qué lo limita por debajo y por encima?

📘 **Dónde se aprende** (1 clase): [B55-C07 · Catálisis en superficies](../programa/clases/B55/B55-C07-catalisis-en-superficies/CLASE.md).

### Tiempo de espera

- El tiempo de espera es el intervalo entre dos eventos consecutivos.
- El tiempo de espera es el ángulo que falta dividido entre `n_c − n_t`.

💡 **Cómo se explica en la clase [B09-C10](../programa/clases/B09/B09-C10-integracion-por-partes/CLASE.md):**
- Si las llegadas son independientes y la tasa no cambia, el tiempo de espera entre una y la siguiente sigue una distribución exponencial con densidad `f(t) = λ e^{−λt}` para `t ≥ 0`; es el caso `μ = 0`, `β = 1/λ` de la densidad que recoge el *e-Handbook of Statistical Methods* de NIST (S2), cuya media es `μ + β`.
- Los tiempos de espera que se muestran están simulados; no son observaciones.
- 🎯 **Por qué importa:** Un detector cuenta fotones que llegan al azar. Cuánto hay que esperar, en promedio, entre uno y el siguiente, y cuánto varía esa espera, decide el tiempo de exposición, el tiempo muerto aceptable y el ruido.

📘 **Dónde se aprende** (2 clases): [B09-C10 · Integración por partes](../programa/clases/B09/B09-C10-integracion-por-partes/CLASE.md); [B76-C10 · Encuentro orbital](../programa/clases/B76/B76-C10-encuentro-orbital/CLASE.md).

### Tiempo de establecimiento al 2 %

- El tiempo de establecimiento al 2 % es el último instante fuera de ±2 % del valor final.

💡 **Cómo se explica en la clase [B97-C24](../programa/clases/B97/B97-C24-modelos-de-actuadores-virtuales-e-integracion-en-simulacion/CLASE.md):**
- Aquí el sobreimpulso baja a `0,3368` (la aceleración inicial es menor), pero el tiempo de pico se alarga a `0,756` s y el establecimiento es `2,33` s frente a `2,24` s.
- Descripción larga: cada efecto modifica la respuesta de forma distinta: la saturación alarga el tiempo de pico, el retardo aumenta el sobreimpulso y la zona muerta deja un error final y alarga el establecimiento.
- 🎯 **Por qué importa:** Un controlador que funciona en simulación con un actuador ideal puede oscilar o no llegar al objetivo con uno real. Conocer qué efecto causa cada fenómeno evita sorpresas al integrar el control con el hardware.

📘 **Dónde se aprende** (1 clase): [B97-C24 · Modelos de actuadores virtuales e integración en simulación](../programa/clases/B97/B97-C24-modelos-de-actuadores-virtuales-e-integracion-en-simulacion/CLASE.md).

### Tiempo de exposición

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C10):** La relación focal decide si un telescopio es «rápido» o «lento». La decisión central: ¿qué importa más, el diámetro o la relación focal?

📘 **Dónde se aprende** (1 clase): [B41-C10 · Apertura y relación focal](../programa/clases/B41/B41-C10-apertura-y-relacion-focal/CLASE.md).

### Tiempo de fusión

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B27-C13](../programa/clases/B27/B27-C13-binarias-compactas/CLASE.md):**
- *Descripción textual:* las masas y el semieje dan la potencia gravitacional y el tiempo de fusión; la solución es una potencia fraccionaria del tiempo restante; la excentricidad acorta el tiempo.
- Con eso, el semieje es `0,8317 Gm` y el tiempo de fusión por ondas gravitacionales, `406,7 Ma`.
- 🎯 **Por qué importa:** La fusión de dos estrellas de neutrones fue el primer evento detectado en ondas gravitacionales y en luz. Saber cuánto falta para una fusión, a qué frecuencia, y cómo la excentricidad la acelera, es la base de toda búsqueda.

📘 **Dónde se aprende** (1 clase): [B27-C13 · Binarias compactas](../programa/clases/B27/B27-C13-binarias-compactas/CLASE.md).

### Tiempo de Hubble

- El tiempo de Hubble es `t_H = 1/H₀`.
- El tiempo de Hubble es `1/H₀`.

💡 **Cómo se explica en la clase [B01-C16](../programa/clases/B01/B01-C16-expansion-del-universo-como-observacion/CLASE.md):**
- *Descripción textual:* de un corrimiento observado se infiere una velocidad aparente; con la ley de Hubble y un valor de `H₀` se obtiene la distancia; hay dos valores de `H₀` en conflicto, cada uno con su método; de `H₀` se obtiene también el tiempo de Hubble.
- Nuestro ejemplo conductor es la galaxia de Hα de C01: calcularemos su distancia y el tiempo de Hubble con cada `H₀`.
- 🎯 **Por qué importa:** En C01 «medimos» una distancia de 43 Mpc con `H₀ = 70`. Pero ese 70 no es un dato único: Planck 2018 da 67,4 ± 0,5 y SH0ES da 73,04 ± 1,04, ambos en km/s/Mpc (S1, S2).

📘 **Dónde se aprende** (2 clases): [B01-C16 · Expansión del universo como observación](../programa/clases/B01/B01-C16-expansion-del-universo-como-observacion/CLASE.md); [B26-C11 · Expansión cósmica y ley de Hubble-Lemaître](../programa/clases/B26/B26-C11-expansion-cosmica-y-ley-de-hubble-lemaitre/CLASE.md).

### Tiempo de ida y vuelta

- El tiempo de ida y vuelta `t` es lo que tarda el pulso; la distancia (*range*) es `R = ct/2`.
- El tiempo de ida y vuelta (RTLT) es `2ρ/c` en el caso ideal.
- El tiempo de ida y vuelta (RTT) es el doble del retardo.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B57-C09](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md):**
- Convertir tiempo de ida y vuelta en distancia (`R = ct/2`) y viceversa.
- 1 cm de distancia = 66.7 ps de tiempo de ida y vuelta ; 1 ns = 14.99 cm
- ⚠️ **Error frecuente:** Olvidar el factor 2. El tiempo es de ida y vuelta (8.1).
- 🎯 **Por qué importa:** La altura del mar cambia unos milímetros por año, pero el eco de un pulso es ruidoso. La decisión central: ¿cuántos pulsos hay que promediar y cómo se ajusta el eco para que el error de distancia del ajuste se reduzca lo necesario?

📘 **Dónde se aprende** (4 clases): [B57-C09 · Altimetría satelital](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md); [B74-C03 · Medición de alcance por radio](../programa/clases/B74/B74-C03-medicion-de-alcance-por-radio/CLASE.md); [B89-C04 · Propagación y pérdidas de espacio libre](../programa/clases/B89/B89-C04-propagacion-y-perdidas-de-espacio-libre/CLASE.md); [B116-C06 · Dispositivos biomédicos portátiles (ultrasonido, diagnóstico)](../programa/clases/B116/B116-C06-dispositivos-biomedicos-portatiles-ultrasonido-diagnostico/CLASE.md).

### Tiempo de integración

- El tiempo de integración es lo que el satélite tarda en avanzar un GSD.
- El tiempo de integración `T = N/f_s` fija la resolución `1/T`.

💡 **Cómo se explica en la clase [B57-C04](../programa/clases/B57/B57-C04-satelites-opticos-de-observacion/CLASE.md):**
- Calcular el tiempo de integración de un sensor de barrido y la étendue de un píxel.
- Ejercicio 2 · con una pista. ¿Cuál es el tiempo de integración con `v = 6,8 km/s` y `GSD = 30 m`?
- 🎯 **Por qué importa:** Un sensor puede tener muchos píxeles y aun así ser inútil porque cada píxel recoge pocos fotones. La decisión central: ¿cuánta apertura y cuánto tiempo de integración hacen falta para que la señal supere el ruido de fotones?

📘 **Dónde se aprende** (2 clases): [B57-C04 · Satélites ópticos de observación](../programa/clases/B57/B57-C04-satelites-opticos-de-observacion/CLASE.md); [B89-C24 · Recepción de telemetría débil](../programa/clases/B89/B89-C24-recepcion-de-telemetria-debil/CLASE.md).

### Tiempo de Kelvin–Helmholtz

- El tiempo de Kelvin–Helmholtz `t_KH` es cuánto brillaría el objeto con la mitad de `|Ω|` a su luminosidad `L`.
- El tiempo de Kelvin–Helmholtz es el de radiar la energía gravitatoria a la luminosidad actual.

💡 **Cómo se explica en la clase [B24-C02](../programa/clases/B24/B24-C02-formacion-de-protoestrellas/CLASE.md):**
- Definir protoestrella, energía gravitatoria, teorema del virial y tiempo de Kelvin–Helmholtz.
- Calcular el tiempo de Kelvin–Helmholtz de una estrella.
- 🎯 **Por qué importa:** Una protoestrella brilla, pero no por el motor que alimenta al Sol. Para saber de dónde sale su energía, cuánto tiempo puede brillar así y cómo distinguirla de una estrella ya estable hay que seguir la energía gravitatoria.

📘 **Dónde se aprende** (2 clases): [B24-C02 · Formación de protoestrellas](../programa/clases/B24/B24-C02-formacion-de-protoestrellas/CLASE.md); [B30-C01 · Estructura interna del Sol](../programa/clases/B30/B30-C01-estructura-interna-del-sol/CLASE.md).

### Tiempo de llegada

- El tiempo de llegada `t_i = t₀ − r_i·n/c`.
- El tiempo de llegada (TOA) de un pulso se estima ajustando un perfil.

💡 **Cómo se explica en la clase [B28-C10](../programa/clases/B28/B28-C10-localizacion-probabilistica-de-eventos/CLASE.md):**
- Ejercicio 8. Tiempo máximo de llegada entre A y C.
- 🎯 **Por qué importa:** El área de localización decide cuántas fotos hacen falta para encontrar la contrapartida. Un mapa mal calibrado engaña.

📘 **Dónde se aprende** (2 clases): [B28-C10 · Localización probabilística de eventos](../programa/clases/B28/B28-C10-localizacion-probabilistica-de-eventos/CLASE.md); [B74-C27 · Navegación por púlsares de rayos X como técnica de investigación](../programa/clases/B74/B74-C27-navegacion-por-pulsares-de-rayos-x-como-tecnica-de-investigacion/CLASE.md).

### Tiempo de llegada (TOA)

- El tiempo de llegada (TOA) es el instante de un pulso.

💡 **Cómo se explica en la clase [B27-C05](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md):**
- En el púlsar binario PSR B1913+16, `9257` tiempos de llegada durante unos `35` años dieron masas de `1,438` y `1,390 M☉` y un decaimiento orbital que coincide con la relatividad general con razón `0,9983 ± 0,0016` (S4, resumen).
- Interpretar una prueba de la radiación gravitacional con tiempos de llegada.
- 🎯 **Por qué importa:** Un púlsar da, a la vez, un reloj de precisión, la medida de su campo magnético y, en una binaria, la masa de las estrellas y una prueba de la relatividad general. La decisión central: dados el periodo y su derivada, ¿qué campo, edad y potencia de frenado tiene el púlsar y qué se aprende de su binaria?

📘 **Dónde se aprende** (1 clase): [B27-C05 · Púlsares y relojes naturales](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md).

### Tiempo de luz

- El tiempo de luz es el que tarda la luz en recorrer una distancia (C01).
- Un tiempo de luz es la distancia dividida por `c = 299 792 458 m/s`.
- El tiempo de luz `t = d/c` es lo que tarda una señal en recorrer una distancia.

💡 **Cómo se explica en la clase [B01-C04](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md):**
- El tiempo se mide contando ciclos regulares.
- La razón es la misma que antes: mientras la Luna da su vuelta, la Tierra se desplaza en su órbita, y la Luna necesita un poco más de tiempo para alcanzar de nuevo la misma posición respecto del Sol.
- 🎯 **Por qué importa:** En 1999 la sonda Mars Climate Orbiter se perdió en la atmósfera de Marte. Según la NASA, el programa en tierra trabajaba en unidades inglesas y el de la sonda en métricas, y esa discrepancia la dirigió demasiado cerca del planeta (S1).

📘 **Dónde se aprende** (3 clases): [B01-C04 · Espacio y tiempo en ciencia](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md); [B03-C07 · Conversión de distancia y velocidad](../programa/clases/B03/B03-C07-conversion-de-distancia-y-velocidad/CLASE.md); [B92-C07 · Enlaces ópticos de espacio profundo](../programa/clases/B92/B92-C07-enlaces-opticos-de-espacio-profundo/CLASE.md).

### Tiempo de luz de una vía

- El tiempo de luz de una vía es `t = d/c`.

💡 **Cómo se explica en la clase [B98-C03](../programa/clases/B98/B98-C03-control-supervisado-y-autonomia-compartida/CLASE.md):**
- Aun así, a distancia máxima el supervisado dedica el 81 % del tiempo a esperar: más autonomía (metas mayores) reduciría esa fracción.
- Descripción larga: el manual gana sin retardo y pierde de forma creciente con él; el supervisado reduce los ciclos y, con ello, la fracción de tiempo perdida esperando la luz.
- 🎯 **Por qué importa:** Ni siempre conviene más autonomía ni siempre más control manual: sin retardo, el manual puede ser más rápido. La decisión central: ¿a partir de qué retardo compensa pasar de órdenes cortas a metas supervisadas, y qué se pierde al hacerlo?

📘 **Dónde se aprende** (1 clase): [B98-C03 · Control supervisado y autonomía compartida](../programa/clases/B98/B98-C03-control-supervisado-y-autonomia-compartida/CLASE.md).

### Tiempo de Lyapunov

- El tiempo de Lyapunov es `T_L = 1/λ`.

💡 **Cómo se explica en la clase [B73-C14](../programa/clases/B73/B73-C14-exponentes-de-lyapunov/CLASE.md):**
- El tiempo de Lyapunov con `K = 5` es de `1,03` iteraciones, `1,82` d en la escala ilustrativa de un periodo de Io.
- Convertir un tiempo de Lyapunov a una escala de tiempo física ilustrativa.
- 🎯 **Por qué importa:** El exponente de Lyapunov es el número que cuantifica el caos: fija el horizonte de predicción y distingue una trayectoria regular de una caótica. En un espacio de fases mixto, un solo exponente no basta.

📘 **Dónde se aprende** (1 clase): [B73-C14 · Exponentes de Lyapunov](../programa/clases/B73/B73-C14-exponentes-de-lyapunov/CLASE.md).

### Tiempo de mínima energía

- El tiempo de mínima energía corresponde a `a = s/2`.

💡 **Cómo se explica en la clase [B82-C01](../programa/clases/B82/B82-C01-lambert-de-arco-corto/CLASE.md):**
- Con `μ = 1` y la unidad de tiempo `TU = 58,13244 d`, el tiempo de mínima energía vale `212,709 d` y el parabólico `88,000 d`.
- Si `t` es menor que el tiempo de mínima energía se usa `α = α₀` (rama corta); si es mayor, `α = 2π − α₀` (rama larga).
- ⚠️ **Error frecuente:** Confundir las ramas. Compara `t` con el tiempo de mínima energía (8.2)
- 🎯 **Por qué importa:** Un diseñador de trayectorias conoce dónde está la nave y dónde debe estar, y cuánto tiempo tiene; no conoce la velocidad con que debe salir. La decisión central: ¿qué semieje y qué velocidad inicial hacen que la nave pase por `r2` exactamente a los `t` días?

📘 **Dónde se aprende** (1 clase): [B82-C01 · Lambert de arco corto](../programa/clases/B82/B82-C01-lambert-de-arco-corto/CLASE.md).

### Tiempo de movimiento

- El tiempo de movimiento es `MT = a + b·ID`.

💡 **Cómo se explica en la clase [B111-C01](../programa/clases/B111/B111-C01-fundamentos-de-factores-humanos-en-operaciones-espaciales/CLASE.md):**
- *Descripción textual:* la tarea fija distancia, ancho y número de opciones; el movimiento y la elección suman su tiempo; el diseño puede acortarlo agrandando objetivos o reduciendo opciones.
- Calcular el índice de dificultad de Fitts y el tiempo de movimiento.
- 🎯 **Por qué importa:** Una interfaz mal diseñada convierte a una tripulación competente en una fuente de errores. La decisión central: ¿qué parte del tiempo y del error es del diseño y no de la persona?

📘 **Dónde se aprende** (1 clase): [B111-C01 · Fundamentos de factores humanos en operaciones espaciales](../programa/clases/B111/B111-C01-fundamentos-de-factores-humanos-en-operaciones-espaciales/CLASE.md).

### Tiempo de parada

- Falso disparo: parada sin falla real. Tiempo de parada: desde la falla hasta que actúa la protección.

💡 **Cómo se explica en la clase [B48-C09](../programa/clases/B48/B48-C09-control-remoto-de-telescopios/CLASE.md):**
- *Descripción textual:* el retardo viene de la distancia y el índice; el vigilante dispara tras k pérdidas seguidas y su tasa de falsos disparos y su tiempo de parada dependen de k.
- Estimar el tiempo de parada de emergencia.
- 🎯 **Por qué importa:** Un vigilante muy sensible detiene la observación sin motivo y uno muy lento no protege. La decisión central: ¿tras cuántos latidos perdidos hay que disparar la parada?

📘 **Dónde se aprende** (1 clase): [B48-C09 · Control remoto de telescopios](../programa/clases/B48/B48-C09-control-remoto-de-telescopios/CLASE.md).

### Tiempo de pared

- El tiempo de pared es el que mide un reloj externo.

🎯 **Por qué importa (clase B18-C01):** Tienes ocho órbitas simuladas que propagar y un portátil con varios núcleos. La tentación es «lanzar ocho hilos y listo».

📘 **Dónde se aprende** (1 clase): [B18-C01 · Procesos, hilos y concurrencia](../programa/clases/B18/B18-C01-procesos-hilos-y-concurrencia/CLASE.md).

### Tiempo de pérdida de la capa

- El tiempo de pérdida de la capa `t_capa = e/(Re Φ)`.

🎯 **Por qué importa (clase B85-C29):** La vida de un recubrimiento depende de varios efectos que se suman y de parámetros inciertos. La decisión central: ¿cuál es la probabilidad de que la temperatura supere el límite al final de la vida y qué incertidumbre la domina?

📘 **Dónde se aprende** (1 clase): [B85-C29 · Evaluación y modelado de la degradación en órbita](../programa/clases/B85/B85-C29-evaluacion-y-modelado-de-la-degradacion-en-orbita/CLASE.md).

### Tiempo de permanencia

- El tiempo de permanencia `t(x) ≥ 0`.

💡 **Cómo se explica en la clase [B43-C05](../programa/clases/B43/B43-C05-pulido-optico/CLASE.md):**
- *Descripción textual:* la tasa de Preston y la función de influencia convierten un mapa de error en tiempos de permanencia no negativos.
- Resolver tiempos de permanencia no negativos por descenso proyectado.
- 🎯 **Por qué importa:** Pulir es controlar un retiro de décimas de micrón: sin un modelo se oscila entre sobrecorregir y subcorregir. La decisión central: ¿cuánto hay que retirar de la mejor esfera para obtener un paraboloide y cuánto tiempo debe permanecer la herramienta en cada zona?

📘 **Dónde se aprende** (1 clase): [B43-C05 · Pulido óptico](../programa/clases/B43/B43-C05-pulido-optico/CLASE.md).

### Tiempo de pico

- El sobreimpulso `Mp` es cuánto excede la respuesta a su valor final (en fracción), el tiempo de pico `tp` es cuándo ocurre, el tiempo de subida `tr` es el que tarda entre 10 % y 90 % del valor final y el tiempo de asentamiento `ts` es el que tarda en quedar dentro de ±2 % para siempre.
- El sobreimpulso, el tiempo de pico y el tiempo de asentamiento.

💡 **Cómo se explica en la clase [B16-C04](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md):**
- Derivando `y(t)` y buscando el primer máximo se obtiene el tiempo de pico `tp = π/ωd` y el sobreimpulso `Mp = exp(−π ζ/√(1 − ζ²))`; solo dependen de `ζ`.
- Obtener `ωn` y `ζ` de un sistema de segundo orden y predecir sobreimpulso, tiempo de pico y de asentamiento.
- 🎯 **Por qué importa:** Tras girar un telescopio hacia una estrella nueva, los instrumentos no pueden empezar a exponer hasta que el apuntamiento se haya asentado. Cada segundo de espera cuesta tiempo de observación.

📘 **Dónde se aprende** (2 clases): [B16-C04 · Respuesta transitoria y estacionaria](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md); [B43-C15 · Motores paso a paso y servomotores](../programa/clases/B43/B43-C15-motores-paso-a-paso-y-servomotores/CLASE.md).

### Tiempo de reacción

- El tiempo de reacción desde tierra es `RTLT + proceso`.

💡 **Cómo se explica en la clase [B75-C19](../programa/clases/B75/B75-C19-restricciones-de-navegacion-autonoma/CLASE.md):**
- *Descripción textual:* La geometría da la distancia; la distancia da el retardo; el retardo más el proceso da el tiempo de reacción; comparado con la duración del evento decide si hace falta autonomía.
- Por comparación: duración del evento frente al tiempo de reacción.
- 🎯 **Por qué importa:** No se puede dirigir desde la Tierra lo que sucede en minutos. La decisión central: ¿qué eventos duran menos que el tiempo mínimo de reacción desde tierra y por tanto deben ser autónomos?

📘 **Dónde se aprende** (1 clase): [B75-C19 · Restricciones de navegación autónoma](../programa/clases/B75/B75-C19-restricciones-de-navegacion-autonoma/CLASE.md).

### Tiempo de relajación

- El tiempo de relajación `t_rh` es el tiempo en que los encuentros entre estrellas cambian sus velocidades en una fracción grande de la inicial.
- El tiempo de relajación es `τ = C/(4 ε σ T³)`.
- El tiempo de relajación `τ = ρ d²/(18 μ)` es lo que tarda una gota en ajustarse a la velocidad del aire.

💡 **Cómo se explica en la clase [B25-C06](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md):**
- *Descripción textual:* de la masa y la escala se obtiene la densidad; de ella, la dispersión por la ecuación de Jeans; el virial comprueba el equilibrio; el tiempo dinámico y la relajación dan las escalas temporales.
- Paso 5 · Sentido. Un cúmulo de 10 Myr está lejos de la relajación (`10 ≪ 165`), pero uno de 10 Gyr habría vivido unos 60 tiempos de relajación.
- 🎯 **Por qué importa:** La mayoría de las estrellas nace en grupos. Los cúmulos son laboratorios: sus estrellas comparten edad, distancia y composición.

📘 **Dónde se aprende** (3 clases): [B25-C06 · Cúmulos estelares](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md); [B54-C19 · Modelos climáticos planetarios](../programa/clases/B54/B54-C19-modelos-climaticos-planetarios/CLASE.md); [B115-C04 · Sistemas aeropónicos](../programa/clases/B115/B115-C04-sistemas-aeroponicos/CLASE.md).

### Tiempo de reloj

- El tiempo de reloj depende del equipo; se reporta como mediana de varias repeticiones y se declara el entorno.

💡 **Cómo se explica en la clase [B11-C26](../programa/clases/B11/B11-C26-benchmark-de-algoritmos-numericos/CLASE.md):**
- B --> F["Tiempo de reloj<br/>(mediana de 5)"]
- *Descripción textual:* se define el problema y los errores objetivo; cada método se barre con resoluciones crecientes registrando error y evaluaciones; se arma el diagrama trabajo-precisión y se anota el costo mínimo por objetivo; el tiempo de reloj se mide aparte; se repite todo para comprobar que los números coinciden.
- 🎯 **Por qué importa:** «El método A es mejor que el B» es una afirmación vacía sin el problema, la métrica, la tolerancia y el costo. Una comparación mal diseñada lleva a elegir el algoritmo equivocado para una misión.

📘 **Dónde se aprende** (1 clase): [B11-C26 · Benchmark de algoritmos numéricos](../programa/clases/B11/B11-C26-benchmark-de-algoritmos-numericos/CLASE.md).

### Tiempo de renovación

- Un tiempo de renovación es lo que tarda en renovarse una unidad de carbono celular.

💡 **Cómo se explica en la clase [B64-C03](../programa/clases/B64/B64-C03-psicrofilos-y-vida-en-frio/CLASE.md):**
- *Descripción textual:* la energía de activación y la temperatura dan el factor de Arrhenius; de él salen el Q10 y, combinado con el régimen de actividad, el tiempo de renovación.
- Convertir un factor de lentitud en un tiempo de renovación.
- ⚠️ **Error frecuente:** Tomar el tiempo de renovación como medida. Es sintético (sección 8.4).
- 🎯 **Por qué importa:** El frío no detiene la vida de golpe: la ralentiza. La pregunta motivadora: ¿cuánto más lento es el metabolismo a −40 °C que a 25 °C, y qué significa «vivir» a esa velocidad?

📘 **Dónde se aprende** (1 clase): [B64-C03 · Psicrófilos y vida en frío](../programa/clases/B64/B64-C03-psicrofilos-y-vida-en-frio/CLASE.md).

### Tiempo de reposición

- El tiempo de reposición es `D/(χ v)`.

💡 **Cómo se explica en la clase [B57-C20](../programa/clases/B57/B57-C20-caso-de-estudio-climatico-o-geologico-de-chile/CLASE.md):**
- *Descripción textual:* la magnitud da el deslizamiento, la convergencia y el acoplamiento dan la tasa, y su cociente es el tiempo de reposición, con incertidumbre por Monte Carlo y un déficit acumulado hasta hoy.
- Calcular el tiempo de reposición del deslizamiento con una tasa de acumulación dada.
- ⚠️ **Error frecuente:** Leer el tiempo de reposición como pronóstico. Es una escala (8.4).
- 🎯 **Por qué importa:** Chile vive sobre una zona de subducción activa y las instituciones deben comprender cuánta deformación se acumula y se libera. La decisión central: ¿qué puede decir una cuenta de balance de deslizamiento y qué no puede decir sobre cuándo ocurrirá el próximo terremoto?

📘 **Dónde se aprende** (1 clase): [B57-C20 · Caso de estudio climático o geológico de Chile](../programa/clases/B57/B57-C20-caso-de-estudio-climatico-o-geologico-de-chile/CLASE.md).

### Tiempo de rescate

- El tiempo de rescate suma alistamiento, localización y traslado.

💡 **Cómo se explica en la clase [B104-C14](../programa/clases/B104/B104-C14-supervivencia-en-entorno-terrestre/CLASE.md):**
- *Descripción textual:* la dispersión de aterrizaje da la distancia al equipo de rescate; el tiempo total suma alistamiento, localización (muy distinta con y sin baliza) y traslado; se compara con la autonomía.
- Aterrizajes sintéticos (semilla 104, 200 000 casos): con dispersión nominal (25 km en la dirección del vuelo y 10 km transversal) y baliza, el rescate llega en una mediana de 2,08 h; sin baliza, el tiempo de localización es log-normal de mediana 6 h y la mediana sube a 7,59 h con 24,6 % de probabilidad de superar 12 h.
- 🎯 **Por qué importa:** Si el rescate no llega antes de que se agoten el refugio y las provisiones, la situación se vuelve crítica. La decisión central: ¿cuánto reducen la baliza y la ubicación del rescate la probabilidad de una espera mayor que la autonomía?

📘 **Dónde se aprende** (1 clase): [B104-C14 · Supervivencia en entorno terrestre](../programa/clases/B104/B104-C14-supervivencia-en-entorno-terrestre/CLASE.md).

### Tiempo de reserva

- El tiempo de reserva `T_Res = (P/|dP/dt|) ln(P/P_min)` es el tiempo hasta la presión mínima.

💡 **Cómo se explica en la clase [B110-C01](../programa/clases/B110/B110-C01-despresurizacion-deteccion-aislamiento-y-respuesta/CLASE.md):**
- *Descripción textual:* el orificio y el volumen fijan la constante de tiempo; la presión decae de forma exponencial y de ahí sale el tiempo de reserva con el que se decide.
- Descripción larga: el tiempo de reserva cae con el cuadrado del diámetro y es proporcional al volumen; medir poco tiempo da una estimación muy dispersa.
- 🎯 **Por qué importa:** Un módulo presurizado siempre pierde algo de aire; lo grave es la fuga por encima de lo especificado. La decisión central: ¿cuánto tiempo queda antes de la presión mínima y qué se hace con ese tiempo (medir, aislar o retirarse)?

📘 **Dónde se aprende** (1 clase): [B110-C01 · Despresurización: detección, aislamiento y respuesta](../programa/clases/B110/B110-C01-despresurizacion-deteccion-aislamiento-y-respuesta/CLASE.md).

### Tiempo de residencia

- El tiempo de residencia es el inverso de la tasa.

💡 **Cómo se explica en la clase [B68-C01](../programa/clases/B68/B68-C01-desorcion-termica-de-hielos-interestelares/CLASE.md):**
- Para una película de `N₀` ML a temperatura constante, el tiempo de residencia de orden cero es `t = N₀ / k₀`.
- Isotérmica: tiempo de residencia a `T` fija.
- 🎯 **Por qué importa:** Un hielo de CO que dura mil millones de años a 15 K desaparece en un segundo a 30 K. Esa sensibilidad exponencial decide dónde está la «línea de nieve» de cada molécula y qué hay en el gas.

📘 **Dónde se aprende** (1 clase): [B68-C01 · Desorción térmica de hielos interestelares](../programa/clases/B68/B68-C01-desorcion-termica-de-hielos-interestelares/CLASE.md).

### Tiempo de respuesta

- El tiempo de respuesta es `fin − llegada`.
- El tiempo de respuesta `R_i = C_i + Σ_j ⌈R_i/T_j⌉ C_j` (j de mayor prioridad) es exacto.
- El tiempo de respuesta es el que se tarda en detectar, decidir y actuar.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B88-C05](../programa/clases/B88/B88-C05-sistemas-de-tiempo-real/CLASE.md):**
- Con paso de 1 ms sobre 3 hiperperiodos (468 ms), el tiempo de respuesta máximo observado es 1, 3 y 10 ms: igual al analítico, con 0 plazos incumplidos.
- *Descripción textual:* de las tareas y sus prioridades sale el tiempo de respuesta por iteración; la simulación lo comprueba; ambos alimentan el veredicto.
- 🎯 **Por qué importa:** En una nave, una tarea de control que llega tarde puede ser tan mala como una que da un resultado incorrecto. La decisión central: ¿cada tarea termina siempre antes de su plazo, aun cuando las de mayor prioridad la interrumpen?

📘 **Dónde se aprende** (6 clases): [B88-C05 · Sistemas de tiempo real](../programa/clases/B88/B88-C05-sistemas-de-tiempo-real/CLASE.md); [B88-C22 · Interrupciones y manejo de excepciones en el computador de vuelo](../programa/clases/B88/B88-C22-interrupciones-y-manejo-de-excepciones-en-el-computador-de-vuelo/CLASE.md); [B96-C15 · Operaciones de emergencia](../programa/clases/B96/B96-C15-operaciones-de-emergencia/CLASE.md); [B96-C25 · Seguridad física y control de acceso de estaciones terrestres](../programa/clases/B96/B96-C25-seguridad-fisica-y-control-de-acceso-de-estaciones-terrestres/CLASE.md); [B98-C07 · Arquitectura de autonomía a bordo (percepción-decisión-acción)](../programa/clases/B98/B98-C07-arquitectura-de-autonomia-a-bordo-percepcion-decision-accion/CLASE.md); [B104-C13 · Procedimientos de emergencia](../programa/clases/B104/B104-C13-procedimientos-de-emergencia/CLASE.md).

### Tiempo de reverberación

- El tiempo de reverberación `T60` mide cuánto dura el eco.

💡 **Cómo se explica en la clase [B109-C10](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md):**
- Calcular absorción, tiempo de reverberación y constante del recinto con la fórmula de Sabine.
- 🎯 **Por qué importa:** El ruido continuo degrada la comunicación, el sueño y el trabajo aunque no dañe el oído. La decisión central: ¿qué fuente reduzco primero y cuánto baja el nivel de la cabina?

📘 **Dónde se aprende** (1 clase): [B109-C10 · Acústica y control de ruido interior](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md).

### Tiempo de Salpeter

- El tiempo de Salpeter `t_S` es el tiempo de e-pliegue del crecimiento a Eddington.

💡 **Cómo se explica en la clase [B25-C11](../programa/clases/B25/B25-C11-nucleos-activos-de-galaxias/CLASE.md):**
- Calcular el tiempo de crecimiento (tiempo de Salpeter) y los e-pliegues necesarios.
- 🎯 **Por qué importa:** Algunas galaxias tienen en el centro una fuente que supera a todas sus estrellas, y casi todas las galaxias grandes albergan un agujero negro supermasivo. Entender el AGN une el centro de la galaxia, su gas y su evolución.

📘 **Dónde se aprende** (1 clase): [B25-C11 · Núcleos activos de galaxias](../programa/clases/B25/B25-C11-nucleos-activos-de-galaxias/CLASE.md).

### Tiempo de subida

- El sobreimpulso `Mp` es cuánto excede la respuesta a su valor final (en fracción), el tiempo de pico `tp` es cuándo ocurre, el tiempo de subida `tr` es el que tarda entre 10 % y 90 % del valor final y el tiempo de asentamiento `ts` es el que tarda en quedar dentro de ±2 % para siempre.

🎯 **Por qué importa (clase B16-C04):** Tras girar un telescopio hacia una estrella nueva, los instrumentos no pueden empezar a exponer hasta que el apuntamiento se haya asentado. Cada segundo de espera cuesta tiempo de observación.

📘 **Dónde se aprende** (1 clase): [B16-C04 · Respuesta transitoria y estacionaria](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md).

### Tiempo de transferencia

- El tiempo de transferencia es `MB·8/Mbps`.

💡 **Cómo se explica en la clase [B105-C15](../programa/clases/B105/B105-C15-telemedicina-espacial/CLASE.md):**
- *Descripción textual:* la distancia fija el retardo de ida y vuelta; el volumen y el ancho de banda fijan el tiempo de transferencia; el tiempo de consulta suma turnos por RTT, transferencia y procesamiento, y se compara un diseño por turnos con uno de un solo paquete.
- Calcular el tiempo de transferencia `MB·8/Mbps` y el presupuesto de una consulta.
- 🎯 **Por qué importa:** Una conversación en tiempo real es posible a la Luna (2,6 s de ida y vuelta) y deja de serlo a Marte (hasta 42 min). La decisión central: ¿cuánto dura una consulta según el destino y el diseño del intercambio (varios turnos o un paquete completo)?

📘 **Dónde se aprende** (1 clase): [B105-C15 · Telemedicina espacial](../programa/clases/B105/B105-C15-telemedicina-espacial/CLASE.md).

### Tiempo de tránsito

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B30-C13](../programa/clases/B30/B30-C13-eyecciones-de-masa-coronal/CLASE.md):**
- Calcular el tiempo de tránsito por bisección.
- 🎯 **Por qué importa:** Saber cuándo llegará una CME determina el margen de alerta. La decisión central: ¿cuánto tarda en llegar y cuánto depende ese tiempo del arrastre?

📘 **Dónde se aprende** (1 clase): [B30-C13 · Eyecciones de masa coronal](../programa/clases/B30/B30-C13-eyecciones-de-masa-coronal/CLASE.md).

### Tiempo de vuelo

- El tiempo de vuelo es el intervalo que tarda una señal en recorrer una distancia.
- El tiempo de vuelo es medio período de la elipse.
- El tiempo de vuelo (`TOF`) es medio periodo de la elipse.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B47-C08](../programa/clases/B47/B47-C08-espectrometros-de-masas-orbitales/CLASE.md):**
- *Descripción textual:* el voltaje acelera los iones, el tiempo de vuelo codifica m/q y la dispersión de arranque fija la resolución.
- 🎯 **Por qué importa:** La resolución de masa decide qué especies se separan. La decisión central: ¿qué tiempo de vuelo, qué dispersión y qué resolución permiten distinguir dos iones casi isobáricos?

📘 **Dónde se aprende** (5 clases): [B13-C06 · Patrones de longitud y tiempo](../programa/clases/B13/B13-C06-patrones-de-longitud-y-tiempo/CLASE.md); [B47-C08 · Espectrómetros de masas orbitales](../programa/clases/B47/B47-C08-espectrometros-de-masas-orbitales/CLASE.md); [B71-C18 · Maniobra de Hohmann](../programa/clases/B71/B71-C18-maniobra-de-hohmann/CLASE.md); [B75-C01 · Geometría de transferencias heliocéntricas](../programa/clases/B75/B75-C01-geometria-de-transferencias-heliocentricas/CLASE.md); [B84-C19 · Inspección no destructiva](../programa/clases/B84/B84-C19-inspeccion-no-destructiva/CLASE.md).

### Tiempo de vuelo adimensional

- El tiempo de vuelo adimensional `T = t √(2μ/s³)`.

💡 **Cómo se explica en la clase [B82-C04](../programa/clases/B82/B82-C04-lambert-multirrevolucion/CLASE.md):**
- Incluir `M` en el tiempo de vuelo adimensional `T(x, λ, M)`.
- 🎯 **Por qué importa:** Si hay tiempo de sobra, la nave puede dar una o más vueltas. La decisión central: ¿cuántas soluciones hay para un tiempo dado, existe alguna, y cuál se elige?

📘 **Dónde se aprende** (1 clase): [B82-C04 · Lambert multirrevolución](../programa/clases/B82/B82-C04-lambert-multirrevolucion/CLASE.md).

### Tiempo dinámico

- El tiempo dinámico `√(R³/GM)` es la escala en que la estrella reaccionaría a una ruptura del equilibrio.
- El tiempo dinámico es `√(R³/GM)`.
- El tiempo dinámico `t_din = √(r_h³/(GM))` es el tiempo característico de una órbita.

💡 **Cómo se explica en la clase [B24-C04](../programa/clases/B24/B24-C04-equilibrio-hidrostatico-estelar/CLASE.md):**
- El tiempo dinámico del Sol es `√(R³/GM) = 1593 s ≈ 26,5 min`, y el de caída libre `√(3π/(32Gρ̄)) ≈ 29,5 min` (con `ρ̄ = 1410 kg/m³`).
- D -- "no" --> F["Se contrae o expande<br/>en ~ tiempo dinámico"]
- ⚠️ **Error frecuente:** Confundir tiempo dinámico con la vida de la estrella. Se corrige con el ejercicio 8.
- 🎯 **Por qué importa:** Una estrella es una bola de gas que lleva miles de millones de años sin cambiar de tamaño. Eso exige que, en cada capa, la presión hacia fuera compense el peso del gas de encima.

📘 **Dónde se aprende** (3 clases): [B24-C04 · Equilibrio hidrostático estelar](../programa/clases/B24/B24-C04-equilibrio-hidrostatico-estelar/CLASE.md); [B24-C16 · Gigantes rojas](../programa/clases/B24/B24-C16-gigantes-rojas/CLASE.md); [B25-C06 · Cúmulos estelares](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md).

### Tiempo Dinámico Baricéntrico (TDB)

- El Tiempo Dinámico Baricéntrico (TDB) es la escala uniforme de las efemérides del sistema solar; en SPICE, `ET` significa TDB (S3).

🎯 **Por qué importa (clase B13-C08):** Una efeméride planetaria se tabula en una escala de tiempo; el reloj civil usa otra; y la hora de una nave, otra distinta. Si usas la escala equivocada, una posición calculada para la Luna se desplaza: un segundo de diferencia son unos mil metros de movimiento orbital lunar.

📘 **Dónde se aprende** (1 clase): [B13-C08 · Escalas UTC, TAI, TT y TDB](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md).

### Tiempo efectivo

- El tiempo efectivo `T` descuenta las pausas.

💡 **Cómo se explica en la clase [B129-C03](../programa/clases/B129/B129-C03-seguimiento-ciudadano-de-meteoros/CLASE.md):**
- Calcular el factor de corrección de un observador por magnitud límite, altura del radiante, nubosidad y tiempo efectivo.
- Corregir por `lm`, altura, nubes y tiempo efectivo: el conjunto sin corregir dio 44,8 frente a una verdad de 100; una diferencia así puede venir solo del cielo.
- 🎯 **Por qué importa:** Cuarenta personas cuentan meteoros una noche: unos con un cielo más oscuro, otros bajo nubes, otros con el radiante bajo. La decisión central: ¿cómo se combinan sus recuentos en una sola tasa comparable, y con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B129-C03 · Seguimiento ciudadano de meteoros](../programa/clases/B129/B129-C03-seguimiento-ciudadano-de-meteoros/CLASE.md).

### Tiempo en el sistema

- El tiempo en el sistema `W` incluye espera y servicio.

🎯 **Por qué importa (clase B119-C08):** C01 enuncia el art. VI como regla; esta clase lo convierte en un proceso con tiempos y cobertura, lo que ninguna clase del bloque hace.

📘 **Dónde se aprende** (1 clase): [B119-C08 · Autorización y supervisión de operadores](../programa/clases/B119/B119-C08-autorizacion-y-supervision-de-operadores/CLASE.md).

### Tiempo hasta el apoapsis

- El tiempo hasta el apoapsis es medio periodo.

💡 **Cómo se explica en la clase [B75-C22](../programa/clases/B75/B75-C22-modelos-de-primer-impulso/CLASE.md):**
- *Descripción textual:* El impulso y su dirección dan el vector velocidad; de él salen la energía y el momento, los elementos y el apoapsis; el semieje da el tiempo hasta el apoapsis.
- Familia tangencial: dv, apoapsis y tiempo hasta el apoapsis
- 🎯 **Por qué importa:** Antes de optimizar toda la misión conviene entender el primer impulso. La decisión central: ¿qué módulo y qué dirección del primer impulso alcanzan un radio dado con el menor delta-v y en cuánto tiempo?

📘 **Dónde se aprende** (1 clase): [B75-C22 · Modelos de primer impulso](../programa/clases/B75/B75-C22-modelos-de-primer-impulso/CLASE.md).

### Tiempo hasta el criterio

- El tiempo hasta el criterio es el tiempo en alcanzar un umbral.

💡 **Cómo se explica en la clase [B107-C10](../programa/clases/B107/B107-C10-indicadores-de-rehabilitacion-y-seguimiento/CLASE.md):**
- Una cohorte inventada de 40 personas con tiempo hasta el criterio exponencial de media 30 d y seguimiento de 45 d: 30 alcanzan el criterio y 10 quedan censuradas.
- Estimar la curva de supervivencia (tiempo hasta el criterio) con Kaplan–Meier con datos censurados.
- 🎯 **Por qué importa:** Los fragmentos consultados describen el entrenamiento en la ISS (Loehr et al., 2015) y baterías funcionales con medidas fisiológicas (Mulavara et al., 2018), pero un seguimiento necesita indicadores bien definidos y bien calculados.

📘 **Dónde se aprende** (1 clase): [B107-C10 · Indicadores de rehabilitación y seguimiento](../programa/clases/B107/B107-C10-indicadores-de-rehabilitacion-y-seguimiento/CLASE.md).

### Tiempo hasta lo crítico

- Emergencia: situación que exige acción inmediata. Tiempo hasta lo crítico: `ΔE/(P_carga − P_gen)`.

💡 **Cómo se explica en la clase [B96-C15](../programa/clases/B96/B96-C15-operaciones-de-emergencia/CLASE.md):**
- S["SOC 80 %, limite 20 %"] --> T["Tiempo hasta lo critico"]
- *Descripción textual:* el tiempo hasta lo crítico se calcula con la energía disponible y la descarga neta; se compara con el tiempo de respuesta; el margen indica si hay tiempo y la generación mínima indica cuánto falta.
- 🎯 **Por qué importa:** Cuando falta el contacto, esperar tiene un costo medible. La decisión central: ¿alcanza el tiempo de respuesta antes del límite crítico y qué se puede hacer para ganar margen?

📘 **Dónde se aprende** (1 clase): [B96-C15 · Operaciones de emergencia](../programa/clases/B96/B96-C15-operaciones-de-emergencia/CLASE.md).

### Tiempo hasta resolver

- Prioridad no expropiativa: no interrumpe al que se atiende. Tiempo hasta resolver: espera más servicio.

💡 **Cómo se explica en la clase [B96-C26](../programa/clases/B96/B96-C26-gestion-de-incidentes-en-la-operacion-de-estaciones/CLASE.md):**
- Tiempo medio hasta resolver: 102,4 min (alta) y 165,9 min (baja).
- El tiempo medio hasta resolver es 102,4 min (alta) y 165,9 min (baja).
- 🎯 **Por qué importa:** Sin un procedimiento de priorización, un incidente leve puede retrasar a uno grave. La decisión central: ¿cuánto esperan los incidentes de alta y de baja prioridad y cuánto mejora la priorización al grave sin colapsar al leve?

📘 **Dónde se aprende** (1 clase): [B96-C26 · Gestión de incidentes en la operación de estaciones](../programa/clases/B96/B96-C26-gestion-de-incidentes-en-la-operacion-de-estaciones/CLASE.md).

### Tiempo integral

- El tiempo integral es `Ti = Kp/Ki` (s) y el derivativo `Td = Kd/Kp` (s).

🎯 **Por qué importa (clase B16-C11):** En el espacio actúan pares pequeños pero persistentes: presión de radiación solar, gradiente de gravedad, fugas de un propulsor. Un lazo PD termina con un error constante `d/Kp` (C04).

📘 **Dónde se aprende** (1 clase): [B16-C11 · Control proporcional integral derivativo](../programa/clases/B16/B16-C11-control-proporcional-integral-derivativo/CLASE.md).

### Tiempo límite

- El tiempo límite evita esperas infinitas.
- Ejecutor: programa que corre una secuencia. Tiempo límite: plazo de un paso.

💡 **Cómo se explica en la clase [B88-C24](../programa/clases/B88/B88-C24-capa-de-abstraccion-de-hardware-hal-y-controladores/CLASE.md):**
- Límite: un enchufe no evita que la central falle; por eso el tiempo límite.
- Tratar un dispositivo colgado con tiempo límite.
- ⚠️ **Error frecuente:** Esperar sin límite. Define un tiempo límite (8.4)
- 🎯 **Por qué importa:** Si la aplicación toca registros, no se puede probar sin el hardware y cada cambio de componente la rompe. La decisión central: ¿qué interfaz mínima expone el dispositivo para que la aplicación no dependa de él?

📘 **Dónde se aprende** (2 clases): [B88-C24 · Capa de abstracción de hardware (HAL) y controladores](../programa/clases/B88/B88-C24-capa-de-abstraccion-de-hardware-hal-y-controladores/CLASE.md); [B96-C24 · Operación remota y automatizada de estaciones](../programa/clases/B96/B96-C24-operacion-remota-y-automatizada-de-estaciones/CLASE.md).

### Tiempo luz

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C22](../programa/clases/B47/B47-C22-misiones-de-fisica-solar-soho-sdo-y-solar-orbiter/CLASE.md):**
- Tiempo luz de 1 au: `499,00 s`; de 0,72 au: `359,28 s`.
- *Descripción textual:* la gravedad de dos cuerpos fija los puntos y las órbitas útiles, y el flujo y el tiempo luz fijan las condiciones de la nave.
- 🎯 **Por qué importa:** Cada órbita compra una ventaja y una dificultad. La decisión central: ¿qué punto o qué órbita da la vista del Sol que necesita el instrumento a un costo térmico y de enlace aceptable?

📘 **Dónde se aprende** (1 clase): [B47-C22 · Misiones de física solar: SOHO, SDO y Solar Orbiter](../programa/clases/B47/B47-C22-misiones-de-fisica-solar-soho-sdo-y-solar-orbiter/CLASE.md).

### Tiempo medio

- El tiempo medio `T½` es el que tarda un compartimento en eliminar la mitad de su exceso.

💡 **Cómo se explica en la clase [B104-C11](../programa/clases/B104/B104-C11-trajes-espaciales/CLASE.md):**
- Las razones críticas y los tiempos medios son inventados: no usar para ninguna decisión sobre descompresión ni respiración.
- Descripción larga: el tiempo crece con el tiempo medio y disminuye al aflojar la razón o la presión de cabina.
- 🎯 **Por qué importa:** Un traje presurizado a una fracción de la presión de la cabina deja al nitrógeno disuelto en sobresaturación si no se elimina antes. La decisión conceptual: ¿cómo depende el tiempo de eliminación del nitrógeno del compartimento, de la razón crítica y de la presión de la cabina?

📘 **Dónde se aprende** (1 clase): [B104-C11 · Trajes espaciales](../programa/clases/B104/B104-C11-trajes-espaciales/CLASE.md).

### Tiempo mínimo

- El tiempo mínimo con cota `U` para recorrer `d` en reposo es `T_min = 2√(d/U)`.
- El tiempo mínimo `T_min(M)` es el mínimo de esa curva, en `x = x_min`.

💡 **Cómo se explica en la clase [B81-C12](../programa/clases/B81/B81-C12-restricciones-dinamicas-en-optimizacion/CLASE.md):**
- Hallar la cota mínima factible con el tiempo mínimo bang-bang.
- Tiempo minimo T_min = 2 sqrt(d/U): U = 4 -> 1.0000 ;
- 🎯 **Por qué importa:** Ignorar una cota produce un control irrealizable; imponerla mal produce un problema sin solución. La decisión central: ¿cuánto cuesta una cota de control y cuál es el mínimo valor para el que el problema aún tiene solución?

📘 **Dónde se aprende** (2 clases): [B81-C12 · Restricciones dinámicas en optimización](../programa/clases/B81/B81-C12-restricciones-dinamicas-en-optimizacion/CLASE.md); [B82-C04 · Lambert multirrevolución](../programa/clases/B82/B82-C04-lambert-multirrevolucion/CLASE.md).

### Tiempo mínimo de retorno

- El tiempo mínimo de retorno `t_min` es el del residuo más ligado.

💡 **Cómo se explica en la clase [B27-C16](../programa/clases/B27/B27-C16-eventos-de-disrupcion-por-marea/CLASE.md):**
- Calcular la dispersión de energía y el tiempo mínimo de retorno.
- 🎯 **Por qué importa:** Estos eventos iluminan agujeros negros inactivos y permiten estimar su masa. Gezari revisa 56 de ellos (S3, resumen).

📘 **Dónde se aprende** (1 clase): [B27-C16 · Eventos de disrupción por marea](../programa/clases/B27/B27-C16-eventos-de-disrupcion-por-marea/CLASE.md).

### Tiempo muerto

- El tiempo muerto es el intervalo tras un evento durante el cual el detector no registra otro.
- El tiempo muerto es el que no se expone.
- El tiempo muerto `τ` es el intervalo ciego tras un conteo.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C10](../programa/clases/B09/B09-C10-integracion-por-partes/CLASE.md):**
- Ejercicio 9 · transferencia. Si el detector tiene un tiempo muerto de 1 ms, ¿qué fracción de los intervalos entre fotones (con `λ = 100 s⁻¹`, sintética) son más cortos que 1 ms?
- Límites: llegadas independientes; sin tiempo muerto ni ruido; datos simulados; no es análisis de un detector real.
- 🎯 **Por qué importa:** Un detector cuenta fotones que llegan al azar. Cuánto hay que esperar, en promedio, entre uno y el siguiente, y cuánto varía esa espera, decide el tiempo de exposición, el tiempo muerto aceptable y el ruido.

📘 **Dónde se aprende** (4 clases): [B09-C10 · Integración por partes](../programa/clases/B09/B09-C10-integracion-por-partes/CLASE.md); [B44-C18 · Control electrónico de cámaras](../programa/clases/B44/B44-C18-control-electronico-de-camaras/CLASE.md); [B86-C09 · Electrónica de potencia](../programa/clases/B86/B86-C09-electronica-de-potencia/CLASE.md); [B92-C05 · Receptores y detectores para comunicaciones ópticas](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md).

### Tiempo muerto no paralizable

- El tiempo muerto no paralizable `m = n/(1 + nτ)` se corrige con `n = m/(1 − mτ)`.

💡 **Cómo se explica en la clase [B85-C23](../programa/clases/B85/B85-C23-dosimetros-y-monitores-de-radiacion-a-bordo/CLASE.md):**
- Límites: respuesta de potencia, sin dependencia de tasa de dosis ni temperatura, tiempo muerto no paralizable.
- 🎯 **Por qué importa:** Un monitor mal calibrado no distingue una dosis real del ruido. La decisión central: ¿cuál es la relación señal–dosis, desde qué dosis es fiable y hasta qué tasa de cuentas se puede corregir el tiempo muerto?

📘 **Dónde se aprende** (1 clase): [B85-C23 · Dosímetros y monitores de radiación a bordo](../programa/clases/B85/B85-C23-dosimetros-y-monitores-de-radiacion-a-bordo/CLASE.md).

### Tiempo nuclear

- El tiempo nuclear es lo que dura el combustible a la luminosidad actual.
- El tiempo nuclear `t_MS = f X M ε c²/L` es la vida en la secuencia principal, con `f` la fracción de masa que llega a quemarse y `X` la fracción de hidrógeno.

💡 **Cómo se explica en la clase [B24-C06](../programa/clases/B24/B24-C06-fusion-de-hidrogeno/CLASE.md):**
- El tiempo nuclear es `t = f X M ε c² / L`: `7,4 Gyr` con `X = 0,7` y `10,5 Gyr` con `X = 1`.
- Estimar el tiempo nuclear de una estrella.
- 🎯 **Por qué importa:** Una estrella como el Sol brilla desde hace miles de millones de años; ninguna fuente química ni gravitatoria alcanza (C02). La fusión nuclear sí.

📘 **Dónde se aprende** (2 clases): [B24-C06 · Fusión de hidrógeno](../programa/clases/B24/B24-C06-fusion-de-hidrogeno/CLASE.md); [B24-C15 · Estrellas de baja masa](../programa/clases/B24/B24-C15-estrellas-de-baja-masa/CLASE.md).

### Tiempo parabólico

- El tiempo parabólico `t_p = (√2/3)(s^(3/2) − (s−c)^(3/2))` separa elipses de hipérbolas para `θ < 180°`.
- El tiempo parabólico (`x = 1`) se calcula aparte: `T(1) = (2/3)(1 − λ³)`.

💡 **Cómo se explica en la clase [B82-C01](../programa/clases/B82/B82-C01-lambert-de-arco-corto/CLASE.md):**
- Con `μ = 1` y la unidad de tiempo `TU = 58,13244 d`, el tiempo de mínima energía vale `212,709 d` y el parabólico `88,000 d`.
- Calcular el tiempo de mínima energía y el tiempo parabólico (Euler) de una transferencia.
- 🎯 **Por qué importa:** Un diseñador de trayectorias conoce dónde está la nave y dónde debe estar, y cuánto tiempo tiene; no conoce la velocidad con que debe salir. La decisión central: ¿qué semieje y qué velocidad inicial hacen que la nave pase por `r2` exactamente a los `t` días?

📘 **Dónde se aprende** (2 clases): [B82-C01 · Lambert de arco corto](../programa/clases/B82/B82-C01-lambert-de-arco-corto/CLASE.md); [B82-C05 · Singularidades del problema de Lambert](../programa/clases/B82/B82-C05-singularidades-del-problema-de-lambert/CLASE.md).

### Tiempo por llamada

- El tiempo por llamada se mide con `perf_counter` y depende del equipo.

💡 **Cómo se explica en la clase [B82-C07](../programa/clases/B82/B82-C07-benchmark-entre-solucionadores-de-lambert/CLASE.md):**
- Los tiempos por llamada fueron de 3378, 2833, 2458, 1964 y 2082 µs en este equipo, con otros procesos en ejecución: varían entre ejecuciones y no son una medida absoluta.
- Paso 4. El tiempo por llamada (1964 µs) se anota como dependiente del equipo.
- 🎯 **Por qué importa:** Elegir un solucionador sin medirlo es adivinar. La decisión central: ¿qué solucionador conviene para un banco de transferencias, y qué cifras sustentan esa elección?

📘 **Dónde se aprende** (1 clase): [B82-C07 · Benchmark entre solucionadores de Lambert](../programa/clases/B82/B82-C07-benchmark-entre-solucionadores-de-lambert/CLASE.md).

### Tiempo propio

- El tiempo propio `τ` es el medido por un reloj que viaja con el objeto.
- El tiempo propio a lo largo de una línea de universo es `τ = ∫ √(1 − v²/c²) dt`.
- El tiempo propio `τ` lo mide el reloj del cuerpo que cae.

💡 **Cómo se explica en la clase [B26-C03](../programa/clases/B26/B26-C03-dilatacion-temporal-y-contraccion/CLASE.md):**
- En el marco del muón: tiempo propio `2116/(0,99c) = 7,13 μs`; en unidades de `τ`: `3,245`; el mismo `S`.
- *Descripción textual:* en ambos marcos el tiempo propio del recorrido es `d/(γβc)`, y la supervivencia es la exponencial de ese tiempo entre la vida media.
- 🎯 **Por qué importa:** Los muones se producen en la alta atmósfera por rayos cósmicos, viven microsegundos y, sin embargo, llegan al suelo en cantidad. Los relojes de satélites de navegación se ajustan por el mismo efecto.

📘 **Dónde se aprende** (3 clases): [B26-C03 · Dilatación temporal y contracción](../programa/clases/B26/B26-C03-dilatacion-temporal-y-contraccion/CLASE.md); [B26-C04 · Espacio-tiempo de Minkowski](../programa/clases/B26/B26-C04-espacio-tiempo-de-minkowski/CLASE.md); [B27-C08 · Horizonte de sucesos](../programa/clases/B27/B27-C08-horizonte-de-sucesos/CLASE.md).

### Tiempo real

- El tiempo real (RTT menor que 1 s, umbral ilustrativo) permite conversación.

🎯 **Por qué importa (clase B105-C15):** Una conversación en tiempo real es posible a la Luna (2,6 s de ida y vuelta) y deja de serlo a Marte (hasta 42 min). La decisión central: ¿cuánto dura una consulta según el destino y el diseño del intercambio (varios turnos o un paquete completo)?

📘 **Dónde se aprende** (1 clase): [B105-C15 · Telemedicina espacial](../programa/clases/B105/B105-C15-telemedicina-espacial/CLASE.md).

### Tiempo sideral local

- El tiempo sideral local `θ` es el ángulo entre el equinoccio y el meridiano del sitio.

💡 **Cómo se explica en la clase [B77-C11](../programa/clases/B77/B77-C11-ventanas-de-lanzamiento-dinamica-de-lanzamiento-y-reentrada/CLASE.md):**
- Para un sitio sintético a `28,5°` de latitud y un plano de `i = 51,6°` y `RAAN = 120°`, la ventana ascendente se abre cuando el tiempo sideral local es `145,489°` con acimut `44,975°`; la descendente a `274,511°` con acimut `135,025°`.
- Hallar el tiempo sideral local de las dos ventanas diarias.
- 🎯 **Por qué importa:** Si el vehículo despega fuera de la ventana, el plano que alcanza no es el deseado y corregirlo cuesta `Δv`. La decisión central: ¿a qué hora sideral y con qué acimut se lanza para entrar en un plano dado, y cuánto error produce un retraso?

📘 **Dónde se aprende** (1 clase): [B77-C11 · Ventanas de lanzamiento — Dinámica de lanzamiento y reentrada](../programa/clases/B77/B77-C11-ventanas-de-lanzamiento-dinamica-de-lanzamiento-y-reentrada/CLASE.md).

### Tiempo sidéreo de Greenwich (GMST)

- El tiempo sidéreo de Greenwich (GMST) es el TSL en longitud 0°;

🎯 **Por qué importa (clase B08-C05):** Si una estrella culmina a las 22:00 hoy, culminará a las 21:56 mañana. Quien no lo sabe «pierde» el objeto en pocas semanas.

📘 **Dónde se aprende** (1 clase): [B08-C05 · Tiempo sidéreo y solar](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md).

### Tiempo sidéreo local

- El tiempo sidéreo local (TSL) es el ángulo horario del punto vernal en tu lugar; se verá en C05.

💡 **Cómo se explica en la clase [B08-C04](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md):**
- *Descripción textual:* se combinan la ascensión recta del astro con el tiempo sidéreo local para obtener el ángulo horario, y con él, la latitud y la declinación se calculan altura y acimut.
- 🎯 **Por qué importa:** Una tabla dice «Luna: AR 2,14 h, Dec +17,1°». Un telescopio, una cámara o tus ojos necesitan «a 35° de altura, hacia el nornoreste».

📘 **Dónde se aprende** (1 clase): [B08-C04 · Altura y acimut](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md).

### Tiempo sidéreo local (TSL)

- El tiempo sidéreo local (TSL) es el ángulo horario del punto vernal en tu lugar, expresado en horas; en el meridiano, el TSL es igual a la AR del astro que culmina.

💡 **Cómo se explica en la clase [B08-C05](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md):**
- A las 00:00 UT del 5 de noviembre, el tiempo sidéreo local fue `22,25 h` (laboratorio, simulado).
- Calcular el tiempo sidéreo local a una hora UT y usarlo para ubicar el tránsito de un objeto.
- 🎯 **Por qué importa:** Si una estrella culmina a las 22:00 hoy, culminará a las 21:56 mañana. Quien no lo sabe «pierde» el objeto en pocas semanas.

📘 **Dónde se aprende** (1 clase): [B08-C05 · Tiempo sidéreo y solar](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md).

### Tiempo Terrestre (TT)

- El Tiempo Terrestre (TT) avanza al mismo ritmo que TAI con un desfase fijo `TT = TAI + 32,184 s` (S2, S3).

🎯 **Por qué importa (clase B13-C08):** Una efeméride planetaria se tabula en una escala de tiempo; el reloj civil usa otra; y la hora de una nave, otra distinta. Si usas la escala equivocada, una posición calculada para la Luna se desplaza: un segundo de diferencia son unos mil metros de movimiento orbital lunar.

📘 **Dónde se aprende** (1 clase): [B13-C08 · Escalas UTC, TAI, TT y TDB](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md).

### Tiempo total

- El tiempo total es la suma de etapas secuenciales.

💡 **Cómo se explica en la clase [B119-C20](../programa/clases/B119/B119-C20-simulacion-de-respuesta-institucional-a-incidentes/CLASE.md):**
- Descripción larga: paralelizar una etapa independiente reduce la media y la cola del tiempo total.
- 🎯 **Por qué importa:** Las clases anteriores estudian reglas; esta pone a prueba si una cadena de respuesta es suficientemente rápida. Es la clase integradora del bloque junto con la matriz de obligaciones (C33).

📘 **Dónde se aprende** (1 clase): [B119-C20 · Simulación de respuesta institucional a incidentes](../programa/clases/B119/B119-C20-simulacion-de-respuesta-institucional-a-incidentes/CLASE.md).

### Tiempo Universal Coordinado (UTC)

- El Tiempo Universal Coordinado (UTC) es una forma de nombrar instantes con fecha y hora civil que sigue a TAI con saltos de un segundo para mantenerse a menos de `0,9 s` de UT1 (S3); no es una escala continua.

🎯 **Por qué importa (clase B13-C08):** Una efeméride planetaria se tabula en una escala de tiempo; el reloj civil usa otra; y la hora de una nave, otra distinta. Si usas la escala equivocada, una posición calculada para la Luna se desplaza: un segundo de diferencia son unos mil metros de movimiento orbital lunar.

📘 **Dónde se aprende** (1 clase): [B13-C08 · Escalas UTC, TAI, TT y TDB](../programa/clases/B13/B13-C08-escalas-utc-tai-tt-y-tdb/CLASE.md).

### Tiempo visible

- El tiempo visible `T_vis` es el que pasa sobre el límite.

💡 **Cómo se explica en la clase [B28-C08](../programa/clases/B28/B28-C08-senales-transitorias/CLASE.md):**
- Cada magnitud más profunda alarga el tiempo visible en un factor `10^{0,4/α} = 2,03`.
- La cadencia debe ser menor que el tiempo visible para garantizar la detección: `17 d` o menos en este ejemplo.
- 🎯 **Por qué importa:** Un transitorio que dura menos que el intervalo entre visitas se pierde. El índice de caída decide cuánto dura un evento sobre el límite de detección.

📘 **Dónde se aprende** (1 clase): [B28-C08 · Señales transitorias](../programa/clases/B28/B28-C08-senales-transitorias/CLASE.md).

### Tierra esférica

- La Tierra esférica es un modelo sin achatamiento ni atmósfera.

💡 **Cómo se explica en la clase [B87-C04](../programa/clases/B87/B87-C04-sensores-terrestres/CLASE.md):**
- B87-C04 sensor de horizonte | Tierra esferica; limbo medido con sigma = 0.05 deg por eje (SINTETICO, semilla 20260514)
- Límites: Tierra esférica, limbo puntual, sin atmósfera, achatamiento ni ruido de escala; el eje de giro alrededor del nadir no se observa.
- 🎯 **Por qué importa:** Para apuntar una antena o una cámara hacia la Tierra hace falta el nadir. La decisión central: ¿cuántos puntos del limbo y qué precisión se necesitan, y cuánto cambia el resultado con la altitud y con un error en el radio angular supuesto?

📘 **Dónde se aprende** (1 clase): [B87-C04 · Sensores terrestres](../programa/clases/B87/B87-C04-sensores-terrestres/CLASE.md).

### Tierra plana

- La Tierra plana supone `g` constante y horizonte fijo.

💡 **Cómo se explica en la clase [B77-C08](../programa/clases/B77/B77-C08-perdidas-gravitacionales/CLASE.md):**
- Límites: Tierra plana, `g` constante, sin aire; el cabeceo y la aceleración a lo largo de la velocidad son simplificaciones.
- 🎯 **Por qué importa:** Un `Δv` ideal alto no garantiza velocidad alta al final. La decisión central: ¿cuánto del `Δv` se pierde por gravedad y cómo se reduce con más empuje o con una trayectoria más inclinada?

📘 **Dónde se aprende** (1 clase): [B77-C08 · Pérdidas gravitacionales](../programa/clases/B77/B77-C08-perdidas-gravitacionales/CLASE.md).

### Timoshenko

- La de Timoshenko añade el giro de la sección independiente, con cortante `κ G A`.

💡 **Cómo se explica en la clase [B84-C27](../programa/clases/B84/B84-C27-tipos-de-elementos-finitos-viga-placa-y-solido/CLASE.md):**
- El Timoshenko FE (8 elementos, error < 2 % en todos los casos) sigue a Timoshenko.
- Un voladizo de `0,50 m` con `b = 20 mm` y `P = 100 N` con `L/h = 5` tiene flecha de Euler `0,0362 mm` y de Timoshenko `0,0374 mm`: el cortante aporta `3,19 %`; con `L/h = 2` la flecha de Euler `0,0023 mm` queda `16,6 %` por debajo de la de Timoshenko `0,0028`.
- 🎯 **Por qué importa:** Una viga corta modelada con Euler subestima la flecha en 17 %; no es un error de malla sino de hipótesis. La decisión central: ¿para qué esbeltez es válido el elemento de Euler y cuándo hace falta cortante?

📘 **Dónde se aprende** (1 clase): [B84-C27 · Tipos de elementos finitos: viga, placa y sólido](../programa/clases/B84/B84-C27-tipos-de-elementos-finitos-viga-placa-y-solido/CLASE.md).

### Tipo

- Un tipo es la clase de valor, que fija qué operaciones valen.
- El tipo de un lazo es el número de integradores en `L`; el tipo determina el error ante escalón y rampa.
- Su tipo (`dtype`) fija cómo se guarda cada valor (`float64`, `float32`, `int64`).

💡 **Cómo se explica en la clase [B07-C02](../programa/clases/B07/B07-C02-tipos-de-datos-y-variables/CLASE.md):**
- Cinco tipos distintos en una sola ficha, más la ausencia de un dato.
- La forma accesible es la tabla de la sección 9 y la salida impresa del laboratorio, que lista cada variable con su valor y su tipo.
- 🎯 **Por qué importa:** Un dato sin tipo es ambiguo: «12756» puede ser un número con el que calculas o un texto que lees de un archivo. Si el programa los confunde, falla o, peor, da un resultado plausible pero erróneo.

📘 **Dónde se aprende** (3 clases): [B07-C02 · Tipos de datos y variables](../programa/clases/B07/B07-C02-tipos-de-datos-y-variables/CLASE.md); [B14-C02 · Arreglos multidimensionales NumPy](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md); [B16-C11 · Control proporcional integral derivativo](../programa/clases/B16/B16-C11-control-proporcional-integral-derivativo/CLASE.md).

### Tipo A

- La evaluación de tipo A de una incertidumbre típica se obtiene del análisis estadístico de observaciones repetidas; la de tipo B, por otros medios: datos previos, especificaciones, certificados, juicio científico (S1, 4.2–4.3).

💡 **Cómo se explica en la clase [B12-C20](../programa/clases/B12/B12-C20-informe-de-incertidumbre-de-una-mision/CLASE.md):**
- Componentes: altitud (tipo A, 9 lecturas, `s = 300 m`), radio de referencia (tipo B, rectangular ±500 m), `GM` (tipo B, `10⁻⁹` relativa, hipotético).
- Clasificar componentes en tipo A (estadísticos) y tipo B (otros) y evaluar cada uno.
- 🎯 **Por qué importa:** Una cifra sin incertidumbre es una opinión; una incertidumbre sin presupuesto es una cifra sin respaldo. Quien revise la misión —otro ingeniero, un cliente o uno mismo dentro de un año— debe poder ver qué componentes se consideraron, cómo se evaluó cada uno, cuál domina y si el requisito se cumple.

📘 **Dónde se aprende** (1 clase): [B12-C20 · Informe de incertidumbre de una misión](../programa/clases/B12/B12-C20-informe-de-incertidumbre-de-una-mision/CLASE.md).

### Tipo B

- La evaluación tipo A estima `u` de una serie de lecturas (S1, 2.3.2); la tipo B, de información como certificados, hojas técnicas o juicio (S1, 2.3.3).
- La evaluación de tipo A de una incertidumbre típica se obtiene del análisis estadístico de observaciones repetidas; la de tipo B, por otros medios: datos previos, especificaciones, certificados, juicio científico (S1, 4.2–4.3).
- La incertidumbre tipo A viene del ruido y del ajuste; la tipo B de la fuerza de referencia (masas y gravedad local).

💡 **Cómo se explica en la clase [B01-C18](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md):**
- Si el espectrógrafo tiene una calibración que desplaza todas las longitudes 0,05 nm, la media no lo detecta: hay que tener información externa (la incertidumbre de calibración, de tipo B).
- Por eso un reporte serio declara ambos: la repetibilidad (tipo A) y la calibración (tipo B).
- 🎯 **Por qué importa:** En C05 dijiste que un resultado de OPERA estaba «a unas 6 incertidumbres de cero» y otro «a menos de una». En C07 dijiste que dos intervalos de ±2σ no debían solaparse.

📘 **Dónde se aprende** (3 clases): [B01-C18 · Incertidumbre y errores elementales](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md); [B12-C20 · Informe de incertidumbre de una misión](../programa/clases/B12/B12-C20-informe-de-incertidumbre-de-una-mision/CLASE.md); [B102-C06 · Dinamometría y medición de fuerzas de tracción](../programa/clases/B102/B102-C06-dinamometria-y-medicion-de-fuerzas-de-traccion/CLASE.md).

### Tipo con unidad

- Interfaz: frontera entre dos sistemas que intercambian datos. Tipo con unidad: valor que lleva su unidad.

💡 **Cómo se explica en la clase [B96-C19](../programa/clases/B96/B96-C19-lecciones-aprendidas-operativas/CLASE.md):**
- Ejercicio 8 · autónomo. ¿Qué rechaza el tipo con unidad?
- Límites: deriva lineal, sin geometría de trayectoria; un solo tipo de unidad de impulso.
- 🎯 **Por qué importa:** Un número sin unidad es una trampa: el programa corre, el valor parece razonable y la nave se pierde. La decisión central: ¿cómo se evita que una conversión de unidades pase inadvertida entre el software de tierra y el de vuelo?

📘 **Dónde se aprende** (1 clase): [B96-C19 · Lecciones aprendidas operativas](../programa/clases/B96/B96-C19-lecciones-aprendidas-operativas/CLASE.md).

### Tipo espectral

- El tipo espectral (O, B, A, F, G, K, M, de caliente a frío) es una clasificación por las líneas.

💡 **Cómo se explica en la clase [B24-C10](../programa/clases/B24/B24-C10-espectros-y-clasificacion-estelar/CLASE.md):**
- Por las líneas (tipo espectral): casi independiente del enrojecimiento.
- 🎯 **Por qué importa:** La intensidad de una línea espectral no crece simplemente con la temperatura: depende de cuántos átomos están en el nivel adecuado y de cuántos están ionizados. Por eso un mismo elemento domina en estrellas de temperaturas muy distintas.

📘 **Dónde se aprende** (1 clase): [B24-C10 · Espectros y clasificación estelar](../programa/clases/B24/B24-C10-espectros-y-clasificacion-estelar/CLASE.md).

### Tipo I

- El nivel de significación `α` es la tasa de falsos rechazos que se acepta (error tipo I); el error tipo II (probabilidad `β`) es no rechazar una `H₀` falsa; la potencia `1 − β` es la probabilidad de detectar un efecto real de un tamaño dado.

💡 **Cómo se explica en la clase [B12-C09](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md):**
- Distinguir error tipo I, error tipo II y potencia, y calcular la potencia en un caso.
- Debe incluir: hipótesis y supuestos; estadístico y `p` comprobado por dos caminos; simulación del error tipo I; potencia y `n` necesario; sensibilidad (correlación, colas); conclusión acotada; datos rotulados como observados/estimados/sintéticos y fuentes con fecha.
- 🎯 **Por qué importa:** Muchas preguntas científicas tienen forma de decisión: ¿coinciden dos mediciones de la misma constante?, ¿el sensor sigue calibrado?, ¿es real la señal o es ruido? Sin un procedimiento con error controlado, cada persona decide por intuición.

📘 **Dónde se aprende** (1 clase): [B12-C09 · Pruebas de hipótesis](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md).

### Tipo Tait–Bryan

- Una secuencia de tipo Tait–Bryan usa tres ejes distintos (3‑2‑1: `z`, `y`, `x`); una de Euler propio repite el primero y el tercero (3‑1‑3: `z`, `x`, `z`).

🎯 **Por qué importa (clase B10-C14):** Un satélite que apunta una antena al cenit tiene el cabeceo cerca de `90°`; si la actitud se guarda con ángulos de Euler, justo ahí el cálculo se vuelve inestable: ángulos que cambian muy rápido para movimientos pequeños, o dos conjuntos de ángulos distintos para la misma orientación.

📘 **Dónde se aprende** (1 clase): [B10-C14 · Ángulos de Euler y singularidades](../programa/clases/B10/B10-C14-angulos-de-euler-y-singularidades/CLASE.md).

### TIR

- La TIR es la `r` con VAN igual a cero.
- La TIR es la tasa que hace el VPN igual a cero.

💡 **Cómo se explica en la clase [B124-C07](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md):**
- La TIR por bisección es `23,8799` %; por Newton, `23,8799` %; el error de `VAN(TIR)` es `8,2e-14`.
- Este flujo cambia de signo una sola vez, así que la TIR es única; con varios cambios de signo puede haber varias.
- ⚠️ **Error frecuente:** Reportar la TIR sin el flujo. Se corrige con 8.1.
- 🎯 **Por qué importa:** El dinero privado tiene un costo distinto del público: se paga con retorno y con propiedad. La decisión central: ¿qué retorno exige y qué parte del proyecto se cede a cambio?

📘 **Dónde se aprende** (2 clases): [B124-C07 · Financiamiento privado](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md); [B126-C05 · Evaluación de viabilidad económica de un negocio espacial](../programa/clases/B126/B126-C05-evaluacion-de-viabilidad-economica-de-un-negocio-espacial/CLASE.md).

### Tirante

- El índice de panel es `E^(1/3)/ρ`; el de tirante, `σ_y/ρ`; el de columna, `E^(1/2)/ρ`.

💡 **Cómo se explica en la clase [B84-C05](../programa/clases/B84/B84-C05-seleccion-de-materiales/CLASE.md):**
- Derivar índices de mérito para panel, tirante y columna.
- 🎯 **Por qué importa:** Un ganador que cambia con pequeñas variaciones de pesos no es una decisión: es una opinión. La sensibilidad dice si la elección es robusta.

📘 **Dónde se aprende** (1 clase): [B84-C05 · Selección de materiales](../programa/clases/B84/B84-C05-seleccion-de-materiales/CLASE.md).

### Tiro

- El tiro (*shooting*) convierte el BVP en un IVP: se adivina la condición inicial que falta, se integra y se corrige hasta cumplir la condición del otro extremo.

💡 **Cómo se explica en la clase [B11-C12](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md):**
- Tiro: simple de programar sobre un integrador ya validado; puede ser muy sensible si el problema es inestable (pequeños cambios en `v₀` producen grandes cambios en el extremo).
- B -->|"Tiro"| E["Adivinar la condición<br/>inicial que falta"]
- ⚠️ **Error frecuente:** Aceptar el tiro sin verificar con otro paso. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** En ingeniería espacial las condiciones suelen estar en dos extremos: una aleta térmica con temperaturas conocidas en la raíz y en la punta; una transferencia que debe partir de un punto y llegar a otro en un tiempo dado.

📘 **Dónde se aprende** (1 clase): [B11-C12 · Problemas de frontera](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md).

### Tiro de barra

- El empuje `H` es la integral de `τ` en el arco; la resistencia por compactación `Rc = b k z₀^(n+1)/(n+1)` es el trabajo de hundir la rueda; el tiro de barra es `DP = H − Rc`.

💡 **Cómo se explica en la clase [B102-C02](../programa/clases/B102/B102-C02-terramecanica-traccion-y-hundimiento-en-suelos-sueltos/CLASE.md):**
- *Descripción textual:* la carga fija el hundimiento y este el arco de contacto; con el patinaje se obtiene el empuje; restando la resistencia por compactación queda el tiro de barra.
- Paso 4 · Tiro de barra. `DP = 223,958 − 108,961 = 114,997 N`, `DP/W = 0,185`.
- 🎯 **Por qué importa:** La tracción de un rover en regolito no sale de un coeficiente de rozamiento único. La decisión central: ¿cuánta fuerza neta de empuje queda para tirar del vehículo, una vez descontada la resistencia que crea el propio hundimiento, y cómo depende del patinaje y de la gravedad?

📘 **Dónde se aprende** (1 clase): [B102-C02 · Terramecánica: tracción y hundimiento en suelos sueltos](../programa/clases/B102/B102-C02-terramecanica-traccion-y-hundimiento-en-suelos-sueltos/CLASE.md).

### TIS

- La TIS `(4πσ cos θ/λ)²`.

💡 **Cómo se explica en la clase [B43-C23](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md):**
- A igual `σ`, la TIS cambia por `(λ₂/λ₁)² = 4,0` entre 400 y 800 nm.
- *Descripción textual:* una PSD fija la rugosidad en una banda; la TIS la convierte en luz dispersa por la fórmula escalar.
- 🎯 **Por qué importa:** La luz dispersa reduce el contraste y la reflectancia especular. La decisión central: ¿qué rugosidad RMS, en qué banda de frecuencias espaciales, deja la luz dispersa por debajo del presupuesto?

📘 **Dónde se aprende** (1 clase): [B43-C23 · Medición de rugosidad y su efecto en la luz dispersa](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md).

### Tisserand

- El Tisserand respecto a una luna se conserva en cada sobrevuelo de esa luna.

💡 **Cómo se explica en la clase [B75-C26](../programa/clases/B75/B75-C26-sobrevuelos-de-lunas-y-tours-de-sistemas-planetarios/CLASE.md):**
- (3) El `v∞` calculado en el cruce con Ganimedes para la familia de Tisserand coincide con el pedido con error menor que `10⁻⁶ km/s`.
- La evidencia es tu esbozo de tour por Tisserand del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Cada luna es un peldaño de energía en torno a Júpiter. La decisión central: ¿qué órbitas jovianas puede alcanzar una nave con un sobrevuelo de Ganimedes de `v∞` dado y cuánto cambia la energía en un solo paso?

📘 **Dónde se aprende** (1 clase): [B75-C26 · Sobrevuelos de lunas y tours de sistemas planetarios](../programa/clases/B75/B75-C26-sobrevuelos-de-lunas-y-tours-de-sistemas-planetarios/CLASE.md).

### TLE

- El TLE son dos líneas de 69 columnas con elementos medios para el modelo SGP4.
- Una TLE (*two-line element set*) es un formato de dos líneas con elementos medios.

💡 **Cómo se explica en la clase [B74-C29](../programa/clases/B74/B74-C29-formatos-tle-y-omm-de-elementos-orbitales/CLASE.md):**
- El TLE sintético da `5` (línea 1) y `1` (línea 2).
- EL["elementos"] --> TLE["TLE: 2 lineas de 69 columnas"]
- ⚠️ **Error frecuente:** Leer un TLE como elementos osculadores. Son medios para SGP4; ver 8.4.
- 🎯 **Por qué importa:** Un TLE mal copiado o mal leído da una órbita equivocada sin avisar. La decisión central: ¿qué errores detecta la suma de verificación, qué resolución tiene cada campo y qué significan realmente esos «elementos medios»?

📘 **Dónde se aprende** (2 clases): [B74-C29 · Formatos TLE y OMM de elementos orbitales](../programa/clases/B74/B74-C29-formatos-tle-y-omm-de-elementos-orbitales/CLASE.md); [B118-C02 · Catálogos de objetos espaciales](../programa/clases/B118/B118-C02-catalogos-de-objetos-espaciales/CLASE.md).

### TML

- TML (*total mass loss*) es la pérdida total de masa;
- Desgasificación: liberación de gases de un material en vacío. TML: pérdida total de masa, `100 (mᵢ − m_f)/mᵢ`.

💡 **Cómo se explica en la clase [B84-C07](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md):**
- Con `m_i = 500 mg`: `TML = (m_i − m_f)/m_i`, `WVR = (m_h − m_f)/m_i`, `RML = TML − WVR`, `CVCM = Δm_colector/m_i`.
- La silicona B pasa en `TML` y falla en `CVCM`: por eso se exigen ambos criterios.
- ⚠️ **Error frecuente:** Usar solo TML. Se corrige con 8.1.
- 🎯 **Por qué importa:** Una película de 10 nm sobre un espejo de telescopio o un sensor estelar degrada la misión; el cribado de desgasificación se hace antes de elegir el adhesivo. La decisión central: ¿pasa un material el cribado de desgasificación y cuántos días de bakeout necesita para limpiarlo?

📘 **Dónde se aprende** (2 clases): [B84-C07 · Desgasificación de materiales](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md); [B90-C04 · Control de contaminación](../programa/clases/B90/B90-C04-control-de-contaminacion/CLASE.md).

### Tobera adaptada

- La tobera adaptada es la que expande hasta la presión ambiente.
- La tobera adaptada tiene `p_e = p_a`;

💡 **Cómo se explica en la clase [B78-C03](../programa/clases/B78/B78-C03-termodinamica-de-camaras/CLASE.md):**
- Ejercicio 10 · transferencia. ¿Por qué una tobera adaptada elimina el término de presión del empuje?
- Límites: gas ideal, `γ` y `M` constantes, sin disociación, sin pérdidas, tobera adaptada.
- 🎯 **Por qué importa:** El mismo calor produce chorros distintos según el gas. La decisión central: ¿qué parámetro de cámara gana más escape, subir la temperatura o bajar la masa molar, y hasta dónde se puede expandir el gas?

📘 **Dónde se aprende** (2 clases): [B78-C03 · Termodinámica de cámaras](../programa/clases/B78/B78-C03-termodinamica-de-camaras/CLASE.md); [B79-C08 · Flujo en toberas convergente-divergentes](../programa/clases/B79/B79-C08-flujo-en-toberas-convergente-divergentes/CLASE.md).

### Tobera magnética

- La tobera magnética guía y expande el plasma con un campo divergente.

💡 **Cómo se explica en la clase [B78-C09](../programa/clases/B78/B78-C09-propulsion-por-plasma/CLASE.md):**
- CS --> TOB["tobera magnetica: v^2 = cs^2 (1 + 2 ln(n0/n))"]
- Calcular la velocidad de Bohm y la expansión isoterma en una tobera magnética.
- 🎯 **Por qué importa:** Un plasma solo es un plasma si es mucho mayor que su longitud de Debye. La decisión central: ¿cuándo un gas ionizado se comporta como plasma y cuánta velocidad de escape puede ganar al expandirse en una tobera magnética?

📘 **Dónde se aprende** (1 clase): [B78-C09 · Propulsión por plasma](../programa/clases/B78/B78-C09-propulsion-por-plasma/CLASE.md).

### Tolerancia

- La tolerancia combina una parte relativa `rtol` y una absoluta `atol`: la escala de cada componente es `sc_i = atol + rtol |s_i|`.
- La tolerancia es la diferencia máxima que aceptas entre lo obtenido y lo esperado; se compone de una parte relativa `rtol` y una absoluta `atol`.
- La tolerancia `w` es el semiancho aceptado en frecuencia.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C08](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md):**
- La tolerancia controla el error local de cada paso.
- Para un error global dado hay que reducir la tolerancia y verificar con una referencia (C19).
- ⚠️ **Error frecuente:** Confundir tolerancia local con error global. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Casi ninguna simulación espacial tiene un ritmo uniforme: una nave que rodea un planeta con un perigeo bajo, una sonda que pasa cerca de una luna, un encuentro cercano entre dos cuerpos. Escoger `h` a mano es adivinar.

📘 **Dónde se aprende** (6 clases): [B11-C08 · Integradores de paso adaptativo](../programa/clases/B11/B11-C08-integradores-de-paso-adaptativo/CLASE.md); [B23-C01 · Pruebas unitarias numéricas con tolerancias](../programa/clases/B23/B23-C01-pruebas-unitarias-numericas-con-tolerancias/CLASE.md); [B55-C10 · Identificación de moléculas orgánicas](../programa/clases/B55/B55-C10-identificacion-de-moleculas-organicas/CLASE.md); [B62-C08 · Mezclas moleculares y confusión de líneas](../programa/clases/B62/B62-C08-mezclas-moleculares-y-confusion-de-lineas/CLASE.md); [B72-C18 · Integración numérica perturbada](../programa/clases/B72/B72-C18-integracion-numerica-perturbada/CLASE.md); [B90-C08 · Procedimientos de prueba funcional](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md).
