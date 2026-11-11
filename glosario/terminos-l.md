# Términos · L

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · **L** · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

### L

- Una dimensión es la clase física de una magnitud; aquí usamos tres dimensiones base: M (masa), L (longitud) y T (tiempo).

🎯 **Por qué importa (clase B13-C02):** Un satélite recibe un comando con un tiempo de encendido de motor; el ingeniero de tierra usó una fórmula del periodo orbital copiada de una hoja de cálculo. Si la fórmula está mal dimensionada, el resultado sale en «segundos al cuadrado» o en «metros por segundo» sin que nadie lo note.

📘 **Dónde se aprende** (1 clase): [B13-C02 · Dimensiones y trazabilidad](../programa/clases/B13/B13-C02-dimensiones-y-trazabilidad/CLASE.md).

### Lag

- El lag es el retardo de la correlación.

💡 **Cómo se explica en la clase [B46-C15](../programa/clases/B46/B46-C15-correladores-y-visibilidades/CLASE.md):**
- El pico de la correlación está en el lag `5`, igual al retardo impuesto.
- 🎯 **Por qué importa:** La visibilidad es el dato básico de la imagen, y su ruido determina la sensibilidad. La decisión central: ¿cuántas muestras hay que correlacionar para fijar amplitud y fase con la precisión requerida?

📘 **Dónde se aprende** (1 clase): [B46-C15 · Correladores y visibilidades](../programa/clases/B46/B46-C15-correladores-y-visibilidades/CLASE.md).

### Lagrange

- El resto `Rₙ` es la diferencia entre `f` y su polinomio; en la forma de Lagrange, `Rₙ = f^{(n+1)}(ξ) (x − a)^{n+1}/(n + 1)!` para algún `ξ` entre `a` y `x` (S1, §1.4(vi), ecs. 1.4.35–1.4.36).

💡 **Cómo se explica en la clase [B09-C14](../programa/clases/B09/B09-C14-series-y-aproximaciones/CLASE.md):**
- D --> E["Resto Rₙ<br/>(cota de Lagrange)"]
- 🎯 **Por qué importa:** Un cálculo orbital rápido usa `g(h) = g₀(1 − 2h/R)` para una altitud baja; uno más exigente necesita el siguiente término. Sin una cota del error no se sabe cuál usar.

📖 **Explicado a fondo:** [Lagrange (puntos de)](esencial/esencial-d-l.md#lagrange-puntos-de) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B09-C14 · Series y aproximaciones](../programa/clases/B09/B09-C14-series-y-aproximaciones/CLASE.md).

### Lagrangiano

- Su Lagrangiano es `L = f + λ g`; en el óptimo `∇f + λ ∇g = 0` y `g = 0`;

💡 **Cómo se explica en la clase [B11-C23](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md):**
- En cada iteración se resuelve el sistema lineal `[[W, Aᵀ], [A, 0]] [δz; δλ] = −[∇f + λ∇g; g]`, con `W` la Hessiana del Lagrangiano (aquí `(2 + 2λ) I`) y `A = ∇g`.
- Tres pruebas: la restricción se cumple a la tolerancia; el gradiente del Lagrangiano se anula (residuo KKT `0` en el laboratorio); y un barrido independiente de la región factible no encuentra nada mejor.
- 🎯 **Por qué importa:** Casi todo problema de diseño de trayectorias tiene límites: tiempo máximo, combustible disponible, distancia mínima a un cuerpo. Un optimizador que ignora las restricciones devuelve un resultado imposible; uno que las trata mal da un resultado que parece factible y no es óptimo.

📘 **Dónde se aprende** (1 clase): [B11-C23 · Optimización restringida: Lagrange, KKT y SQP](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md).

### Laguna de Kirkwood

- Una laguna de Kirkwood es una zona con pocos asteroides cerca de una resonancia.

🎯 **Por qué importa (clase B52-C14):** Las posiciones de las resonancias fijan dónde mirar en un cinturón. La decisión central: ¿en qué semiejes están las resonancias de Júpiter y cómo se comprueba el cálculo?

📘 **Dónde se aprende** (1 clase): [B52-C14 · Cinturones de asteroides](../programa/clases/B52/B52-C14-cinturones-de-asteroides/CLASE.md).

### LAI

- El LAI (índice de área foliar) mide el follaje.

💡 **Cómo se explica en la clase [B57-C06](../programa/clases/B57/B57-C06-indices-de-vegetacion/CLASE.md):**
- Entre `LAI 0` y `2` el NDVI gana `0,510`; entre `4` y `6`, solo `0,024`: eso es la saturación.
- Con `LAI = 1`, un suelo claro da `NDVI = 0,544` y uno oscuro `0,622`: diferencia `0,079`.
- 🎯 **Por qué importa:** Un índice facilita comparar fechas y lugares, pero también esconde supuestos. La decisión central: ¿cuándo el NDVI mide de verdad la cantidad de vegetación y cuándo lo engañan la saturación o el suelo?

📘 **Dónde se aprende** (1 clase): [B57-C06 · Índices de vegetación](../programa/clases/B57/B57-C06-indices-de-vegetacion/CLASE.md).

### LAL

- Los esquemas de datos se nombran LAL (lado–ángulo–lado), LLL (tres lados), ALA (ángulo–lado–ángulo) y LLA (lado–lado–ángulo no incluido).

💡 **Cómo se explica en la clase [B04-C08](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md):**
- *Descripción textual:* según los datos (LAL o LLL, ALA o LLA) se usa la ley de cosenos, el tercer ángulo y la de senos, o la de senos con posible ambigüedad; todo termina comprobando que los ángulos suman 180°.
- La ley de cosenos es la más segura: no tiene ambigüedad y sirve con LAL y LLL.
- ⚠️ **Error frecuente:** Usar la ley de senos con LAL. Se corrige con la sección 8.1 y el ejercicio 1.
- 🎯 **Por qué importa:** Cuando una sonda se comunica con la Tierra, el tiempo de la señal depende de la distancia, que cambia de unos 55 millones de km a unos 400 millones según dónde estén ambos planetas en sus órbitas.

📘 **Dónde se aprende** (1 clase): [B04-C08 · Ley de senos y ley de cosenos](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md).

### Lambertiana

- La reflectancia `ρ` es la fracción de la irradiancia que la superficie devuelve; una superficie lambertiana la devuelve igual en todas las direcciones, con `L = ρ E cos θ / π`.
- Una superficie lambertiana dispersa con intensidad proporcional al coseno.

🎯 **Por qué importa (clase B50-C05):** El contraste de un instrumento no depende solo de la imagen: depende de cuánta luz llega por caminos no deseados. La decisión central: ¿qué fracción de luz llega por un camino parásito y cómo se reduce?

📘 **Dónde se aprende** (2 clases): [B50-C05 · Luz parásita y análisis de rayos dispersos](../programa/clases/B50/B50-C05-luz-parasita-y-analisis-de-rayos-dispersos/CLASE.md); [B57-C01 · Fundamentos de teledetección](../programa/clases/B57/B57-C01-fundamentos-de-teledeteccion/CLASE.md).

### LAMDA

- HITRAN reúne parámetros por línea para atmósferas y astrofísica, con intensidad en cm⁻¹/(molécula·cm⁻²) a 296 K. LAMDA (Leiden Atomic and Molecular Database) da niveles, pesos, coeficientes de Einstein y tasas de colisión para códigos de transferencia radiativa.

💡 **Cómo se explica en la clase [B62-C07](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md):**
- LAMDA da las energías de los niveles; la diferencia entre dos niveles debería reproducir la frecuencia de JPL.
- Las frecuencias de transición que LAMDA lista aparte (`230,5380000` y `345,7959899 GHz`) sí coinciden con JPL: la discrepancia está en la precisión de las energías de nivel, no en las frecuencias de línea.
- 🎯 **Por qué importa:** Una identificación depende de una frecuencia, y esa frecuencia viene de un archivo que alguien ajustó y versionó. Si no sabes leer la columna de error, la unidad de la intensidad o la temperatura de referencia, importarás un error silencioso.

📘 **Dónde se aprende** (1 clase): [B62-C07 · Bancos de datos moleculares: CDMS, JPL, HITRAN y LAMDA](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md).

### Lámina

- Una lámina es una masa repartida en un plano.
- La lámina tiene ejes del material 1 (fibra) y 2.

💡 **Cómo se explica en la clase [B36-C05](../programa/clases/B36/B36-C05-simulaciones-cosmologicas-de-n-cuerpos-condiciones-iniciales-y-caja-periodica/CLASE.md):**
- En Einstein–de Sitter (`4πGρ̄ = 1,5 H²`) la ecuación de cada lámina es `x'' + (3/2a) x' = (3/2) a⁻² (x − q)` en la variable `a`, donde `q` es la posición lagrangiana del rango (la fuerza en 1D es exacta incluso después del cruce).
- 🎯 **Por qué importa:** Una simulación sin comprobar contra un caso exacto no es una prueba. La decisión central: ¿converge el integrador al resultado analítico y qué pasa cuando las láminas se cruzan?

📘 **Dónde se aprende** (2 clases): [B36-C05 · Simulaciones cosmológicas de N cuerpos: condiciones iniciales y caja periódica](../programa/clases/B36/B36-C05-simulaciones-cosmologicas-de-n-cuerpos-condiciones-iniciales-y-caja-periodica/CLASE.md); [B84-C03 · Materiales compuestos](../programa/clases/B84/B84-C03-materiales-compuestos/CLASE.md).

### Lámina de Harris

- La lámina de Harris tiene `B = B₀ tanh(z/L)`.

💡 **Cómo se explica en la clase [B35-C08](../programa/clases/B35/B35-C08-flujos-de-plasma-estacionarios-y-balance-de-presiones/CLASE.md):**
- En una lámina de Harris con `B₀ = 10 nT` la presión térmica central es `0,039789 nPa` y la total es constante.
- 🎯 **Por qué importa:** Los equilibrios estacionarios fijan la forma de las fronteras. La decisión central: ¿qué presiones se compensan y qué fuerza es la que equilibra?

📘 **Dónde se aprende** (1 clase): [B35-C08 · Flujos de plasma estacionarios y balance de presiones](../programa/clases/B35/B35-C08-flujos-de-plasma-estacionarios-y-balance-de-presiones/CLASE.md).

### Lámina de retardo

- La lámina de retardo (cuarto y media onda).

🎯 **Por qué importa (clase B42-C08):** La polarización cambia cuánto flujo pasa por un instrumento (espejos, divisores, filtros) y revela procesos físicos de la fuente. La decisión central: ¿cómo se describe y se mide un estado de polarización y cómo lo transforma un elemento óptico?

📘 **Dónde se aprende** (1 clase): [B42-C08 · Polarización de la luz](../programa/clases/B42/B42-C08-polarizacion-de-la-luz/CLASE.md).

### Laminar

- El flujo es laminar si las capas no se mezclan y turbulento si hay mezcla caótica.

💡 **Cómo se explica en la clase [B79-C04](../programa/clases/B79/B79-C04-regimenes-laminar-y-turbulento/CLASE.md):**
- Las dos fórmulas no coinciden en `Re = 2300`: `f` laminar `0,02783` y Blasius `0,04563`.
- Con `Re_L = 2 × 10⁶` el `C_f` turbulento es `4,33` veces el laminar.
- ⚠️ **Error frecuente:** Aplicar la correlación laminar de placa a `Re_L > 5 × 10⁵`. Se corrige con 8.2.
- 🎯 **Por qué importa:** El régimen cambia el arrastre y la transferencia de calor por factores de varios; no distinguirlo lleva a subestimar el calentamiento de una pared o la pérdida de presión de un conducto. El tronco no lo trata.

📘 **Dónde se aprende** (1 clase): [B79-C04 · Regímenes laminar y turbulento](../programa/clases/B79/B79-C04-regimenes-laminar-y-turbulento/CLASE.md).

### Landy–Szalay

- El de Landy–Szalay `(DD − 2DR + RR)/RR`.

💡 **Cómo se explica en la clase [B36-C03](../programa/clases/B36/B36-C03-funciones-de-correlacion-de-galaxias/CLASE.md):**
- Natural y Landy–Szalay difieren como máximo `0,43` en la maqueta 1.
- 🎯 **Por qué importa:** Medir la agrupación exige un estimador sin sesgo y con error conocido. La decisión central: ¿concuerda el estimador con la verdad analítica dentro de su error?

📘 **Dónde se aprende** (1 clase): [B36-C03 · Funciones de correlación de galaxias](../programa/clases/B36/B36-C03-funciones-de-correlacion-de-galaxias/CLASE.md).

### Langmuir

- El langmuir es una unidad de dosis: `10⁻⁶ Torr · s`.

💡 **Cómo se explica en la clase [B47-C12](../programa/clases/B47/B47-C12-optica-en-ambientes-de-vacio/CLASE.md):**
- El N₂ a `10⁻⁶ Torr` (1 langmuir por segundo) tarda `2,58 s`.
- 🎯 **Por qué importa:** La contaminación reduce la reflectancia y la transmisión sin aviso. La decisión central: ¿cuánto tarda en cubrirse una superficie y cuánto cambia la reflectancia por una película?

📘 **Dónde se aprende** (2 clases): [B47-C12 · Óptica en ambientes de vacío](../programa/clases/B47/B47-C12-optica-en-ambientes-de-vacio/CLASE.md); [B68-C04 · Laboratorio de astroquímica de hielos en ultra alto vacío criogénico](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md).

### Laniakea

- Tully y colaboradores definen el supercúmulo local, Laniakea, por la región donde los movimientos de las galaxias convergen una vez restada la expansión media (S4).

💡 **Cómo se explica en la clase [B01-C15](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md):**
- Tully y colaboradores definen Laniakea como la región en que los movimientos peculiares de las galaxias apuntan hacia adentro una vez restada la expansión media; la frontera es una superficie donde los flujos divergen (S4).
- CL --> SC["Supercúmulo: Laniakea (flujos convergentes)"]
- 🎯 **Por qué importa:** La galaxia de la línea Hα (C01) está a 43 Mpc, pero ¿qué significa eso comparado con lo que ya conoces? ¿Está más lejos o más cerca que Andrómeda?

📘 **Dónde se aprende** (1 clase): [B01-C15 · Galaxias y agrupaciones cósmicas](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md).

### Lanzamiento ascendente

- El lanzamiento ascendente va hacia el norte; el descendente, hacia el sur.

🎯 **Por qué importa (clase B77-C11):** Si el vehículo despega fuera de la ventana, el plano que alcanza no es el deseado y corregirlo cuesta `Δv`. La decisión central: ¿a qué hora sideral y con qué acimut se lanza para entrar en un plano dado, y cuánto error produce un retraso?

📘 **Dónde se aprende** (1 clase): [B77-C11 · Ventanas de lanzamiento — Dinámica de lanzamiento y reentrada](../programa/clases/B77/B77-C11-ventanas-de-lanzamiento-dinamica-de-lanzamiento-y-reentrada/CLASE.md).

### Laplaciano

- El laplaciano `∇²Φ = Φ_xx + Φ_yy + Φ_zz` mide la curvatura total del campo.

🎯 **Por qué importa (clase B09-C16):** La luminosidad de una estrella calculada con su radio y su temperatura tiene una incertidumbre que viene de las dos. ¿Cuál pesa más?

📘 **Dónde se aprende** (1 clase): [B09-C16 · Derivadas parciales](../programa/clases/B09/B09-C16-derivadas-parciales/CLASE.md).

### Lapso

- El lapso `α` mide el tiempo propio entre capas.

💡 **Cómo se explica en la clase [B39-C06](../programa/clases/B39/B39-C06-introduccion-a-la-relatividad-numerica-formalismo-3-1/CLASE.md):**
- Como hojear un libro: cada página es una capa espacial y el lapso y el desplazamiento dicen cuánto avanza el tiempo y cómo se alinean las páginas.
- *Descripción textual:* la métrica se descompone en lapso, desplazamiento y métrica espacial; las ligaduras se verifican y la evolución se valida por convergencia.
- ⚠️ **Error frecuente:** Confundir lapso y desplazamiento. Se corrige con la sección 6.
- 🎯 **Por qué importa:** Una simulación necesita un tiempo y un espacio. La decisión central: ¿cómo se separa el espacio-tiempo en capas y cómo se sabe que una evolución converge?

📘 **Dónde se aprende** (1 clase): [B39-C06 · Introducción a la relatividad numérica: formalismo 3+1](../programa/clases/B39/B39-C06-introduccion-a-la-relatividad-numerica-formalismo-3-1/CLASE.md).

### Larga

- La rama corta es el arco de menos de 180° y la larga el de más.

💡 **Cómo se explica en la clase [B75-C12](../programa/clases/B75/B75-C12-optimizacion-de-trayectoria/CLASE.md):**
- Descripción larga: el costo mínimo tiene forma de V redondeada con el fondo en 44° y flancos casi simétricos de unos 0,027 km/s por grado cerca del fondo.
- ⚠️ **Error frecuente:** Ignorar la rama larga. Se corrige con 8.3.
- 🎯 **Por qué importa:** No siempre se sale con la fase ideal, y el tiempo de vuelo no es dato sino variable. La decisión central: ¿qué tiempo de vuelo minimiza la suma de excesos hiperbólicos para una fase de salida dada y cuánto empeora el costo al apartarse de la fase ideal?

📘 **Dónde se aprende** (1 clase): [B75-C12 · Optimización de trayectoria](../programa/clases/B75/B75-C12-optimizacion-de-trayectoria/CLASE.md).

### Larga exposición

- El Strehl instantáneo y el de larga exposición.

💡 **Cómo se explica en la clase [B42-C20](../programa/clases/B42/B42-C20-laboratorio-de-correccion-optica-simulada/CLASE.md):**
- El pico de larga exposición dividido por el Strehl instantáneo medio es `2,63` en lazo abierto (la imagen se mueve: el pico no cae siempre en el origen) y `1,00` con el lazo cerrado.
- Con `D/r₀ = 4`, actuadores a `d/r₀ = 0,5`, viento 20 m/s, 500 Hz y retardo de 2 tramas (ilustrativos), el Strehl de larga exposición pasa de `0,1144` (lazo abierto) a `0,7578` con `g = 0,6` y la varianza residual baja `16,2` veces.
- 🎯 **Por qué importa:** El producto es un informe con evidencia numérica de cuánto corrige un lazo dado, con sus límites. La decisión central: ¿qué ganancia y qué ruido dan el Strehl más alto y cómo se comprueba?

📘 **Dónde se aprende** (1 clase): [B42-C20 · Laboratorio de corrección óptica simulada](../programa/clases/B42/B42-C20-laboratorio-de-correccion-optica-simulada/CLASE.md).

### Lastre

- El lastre es la masa que se añade o quita para lograrla.

💡 **Cómo se explica en la clase [B104-C15](../programa/clases/B104/B104-C15-entrenamiento-subacuatico-como-analogia/CLASE.md):**
- Un cuerpo de 150 kg y 0,152 m³ desplaza `995,8 · 0,152 = 151,36 kg`: hace falta añadir `1,36 kg` de lastre para empuje igual al peso.
- Un traje se adapta con lastre y no se usa un traje de vuelo sin presión.
- ⚠️ **Error frecuente:** Dar el lastre «de memoria». Calcula con el volumen (8.2).
- 🎯 **Por qué importa:** El agua anula el peso neto, pero también se opone al movimiento. La decisión central: ¿qué aspectos de una tarea espacial se pueden entrenar bien en el agua y cuáles quedan distorsionados por la inercia y el arrastre del fluido?

📘 **Dónde se aprende** (1 clase): [B104-C15 · Entrenamiento subacuático como analogía](../programa/clases/B104/B104-C15-entrenamiento-subacuatico-como-analogia/CLASE.md).

### Latch

- La histéresis usa un umbral de disparo y otro más bajo de rearme, con un latch que evita alarmas repetidas durante el mismo evento.

💡 **Cómo se explica en la clase [B116-C05](../programa/clases/B116/B116-C05-alertas-de-salud-y-umbrales-de-monitorizacion/CLASE.md):**
- C lo evita con el latch y deja una alarma por evento (8).
- B --> C["C: + latch hasta que<br/>baje de umbral de rearme"]
- 🎯 **Por qué importa:** Una alarma que suena por cada artefacto enseña a ignorarla. Una que espera demasiado llega tarde.

📘 **Dónde se aprende** (1 clase): [B116-C05 · Alertas de salud y umbrales de monitorización](../programa/clases/B116/B116-C05-alertas-de-salud-y-umbrales-de-monitorizacion/CLASE.md).

### Latencia

- La latencia es el tiempo entre el suceso y la alerta.
- La latencia es `N·Δt` para una falla persistente.
- La latencia es el retardo del lazo.
- *(y 7 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B28-C09](../programa/clases/B28/B28-C09-alertas-cientificas-en-tiempo-real/CLASE.md):**
- ET["etapas: 10+20+10+30 s"] --> L["latencia total = 70 s"]
- *Descripción textual:* las etapas suman la latencia; el FAR se traduce a probabilidad y sigmas; el umbral sale de la cola del ruido y se contrasta por Monte Carlo; el factor de pruebas pasa de p local a global.
- 🎯 **Por qué importa:** Una alerta tardía pierde el evento; una alerta con muchas falsas alarmas agota a los observadores. La decisión central: ¿qué umbral produce una tasa de falsas alarmas aceptable y cuánto tarda la alerta en llegar?

📖 **Explicado a fondo:** [Latencia](esencial/ampliacion-a-m.md#latencia) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (10 clases): [B28-C09 · Alertas científicas en tiempo real](../programa/clases/B28/B28-C09-alertas-cientificas-en-tiempo-real/CLASE.md); [B88-C12 · Detección aislamiento y recuperación de fallos](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md); [B88-C19 · Simulación hardware-in-the-loop](../programa/clases/B88/B88-C19-simulacion-hardware-in-the-loop/CLASE.md); [B88-C22 · Interrupciones y manejo de excepciones en el computador de vuelo](../programa/clases/B88/B88-C22-interrupciones-y-manejo-de-excepciones-en-el-computador-de-vuelo/CLASE.md); [B88-C25 · Redundancia de procesamiento y ejecución en paralelo (lockstep)](../programa/clases/B88/B88-C25-redundancia-de-procesamiento-y-ejecucion-en-paralelo-lockstep/CLASE.md); [B88-C26 · Latencia de interrupciones y jitter](../programa/clases/B88/B88-C26-latencia-de-interrupciones-y-jitter/CLASE.md) y 4 más.

### Latencia de detección

- Invariante: condición siempre verdadera. Latencia de detección: tiempo hasta ver la anomalía.

🎯 **Por qué importa (clase B96-C20):** Un ensayo en frío revela conflictos entre contactos, comandos y datos que no se ven sumando números aislados. La decisión central: ¿la jornada funciona de punta a punta y cuándo se detecta una anomalía?

📘 **Dónde se aprende** (1 clase): [B96-C20 · Simulación de jornada de control de misión](../programa/clases/B96/B96-C20-simulacion-de-jornada-de-control-de-mision/CLASE.md).

### Latencia (RTT)

- La latencia (RTT) es el tiempo de ida y vuelta.

💡 **Cómo se explica en la clase [B128-C10](../programa/clases/B128/B128-C10-acceso-con-baja-conectividad/CLASE.md):**
- La simulación por rondas de 6 peticiones, con el peso repartido y una latencia por ronda, da el mismo tiempo con diferencia menor que `1 × 10⁻⁹ s`.
- *Descripción textual:* el peso, las peticiones, el ancho de banda y la latencia dan el tiempo; se compara con el presupuesto y se reduce el peso, se agrupan las peticiones o se usa la caché.
- 🎯 **Por qué importa:** Una persona sin conexión estable queda fuera de un curso aunque los contenidos sean excelentes. La decisión central: ¿cuánto puede pesar una página para cargar a tiempo en la peor conexión del grupo, y qué se puede guardar para no volver a descargarlo?

📘 **Dónde se aprende** (1 clase): [B128-C10 · Acceso con baja conectividad](../programa/clases/B128/B128-C10-acceso-con-baja-conectividad/CLASE.md).

### Latido

- Retardo de propagación: `d n / c`. Latido: mensaje periódico de vida.

💡 **Cómo se explica en la clase [B48-C09](../programa/clases/B48/B48-C09-control-remoto-de-telescopios/CLASE.md):**
- El retardo de red (≈ 12 ms) es despreciable frente al periodo del latido: lo que manda es `k` por el periodo.
- P["p de pérdida"] --> F["tasa = (1-p) p^k por latido"]
- 🎯 **Por qué importa:** Un vigilante muy sensible detiene la observación sin motivo y uno muy lento no protege. La decisión central: ¿tras cuántos latidos perdidos hay que disparar la parada?

📘 **Dónde se aprende** (1 clase): [B48-C09 · Control remoto de telescopios](../programa/clases/B48/B48-C09-control-remoto-de-telescopios/CLASE.md).

### Latitud

- La latitud `φ` es el ángulo norte–sur del lugar, con signo negativo al sur.
- La latitud `φ` es tu ángulo respecto al ecuador terrestre, negativa en el sur.
- La latitud `φ` va de −90° (sur) a +90° (norte) y la longitud `λ` crece hacia el este.

💡 **Cómo se explica en la clase [B01-C11](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md):**
- Su altura sobre el horizonte es igual a la latitud: `|φ| = 33,45°` para nuestro lugar.
- Versión accesible del diagrama (latitud 33,45° S, ejemplo):
- ⚠️ **Error frecuente:** Olvidar el signo de la latitud. Ejercicio 1.
- 🎯 **Por qué importa:** Antes de cualquier telescopio, la humanidad dedujo mucho del cielo a simple vista. Que el Sol «salga» y «se ponga» es una observación; que la Tierra gire es una interpretación (C05) que explica además el movimiento de todas las estrellas.

📘 **Dónde se aprende** (3 clases): [B01-C11 · Movimiento aparente del Sol y las estrellas](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md); [B04-C16 · Geometría de esferas y círculos máximos](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md); [B08-C01 · Orientación geográfica y puntos cardinales](../programa/clases/B08/B08-C01-orientacion-geografica-y-puntos-cardinales/CLASE.md).

### Latitud geodésica

- La latitud geodésica `φ` es el ángulo de la normal al elipsoide con el plano ecuatorial; la longitud `λ`, el ángulo desde el meridiano origen; la altura elipsoidal `h`, la distancia a lo largo de la normal.

💡 **Cómo se explica en la clase [B13-C11](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md):**
- ⚠️ **Error frecuente:** Confundir latitud geodésica y geocéntrica. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Una estación terrestre transmite a un satélite; el software de seguimiento necesita su posición en X, Y, Z. El técnico de campo tiene su posición en latitud, longitud y altura.

📘 **Dónde se aprende** (1 clase): [B13-C11 · Sistemas de referencia terrestres](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md).

### Latitud planetográfica

- La latitud planetográfica `φg` mide el ángulo de la normal al elipsoide con el plano ecuatorial; la planetocéntrica `φc`, del radio vector.

🎯 **Por qué importa (clase B53-C06):** Una altura de 1 km no significa lo mismo sobre una esfera que sobre un elipsoide. La decisión central: ¿qué latitud y qué referencia usa cada producto, y cuánto difieren?

📘 **Dónde se aprende** (1 clase): [B53-C06 · Geodesia de Marte](../programa/clases/B53/B53-C06-geodesia-de-marte/CLASE.md).

### Latitud subradar

- La latitud subradar es la latitud del punto más cercano al radar.

💡 **Cómo se explica en la clase [B58-C12](../programa/clases/B58/B58-C12-radar-planetario/CLASE.md):**
- Para una esfera, `B = 4πD cos δ/(λ P)`, donde `δ` es la latitud subradar.
- El ejemplo conductor es una esfera sintética de 500 m con periodo de 4 h, vista a latitud subradar 30° con `λ = 3,5 cm`.
- 🎯 **Por qué importa:** El radar aporta lo que la fotometría no da: tamaño directo (sin albedo) y distancias de precisión que reducen la incertidumbre orbital. La decisión central: ¿qué resolución y qué señal se obtienen de un objeto de cierto tamaño a cierta distancia?

📘 **Dónde se aprende** (1 clase): [B58-C12 · Radar planetario](../programa/clases/B58/B58-C12-radar-planetario/CLASE.md).

### Lavado

- El lavado es el retorno a 0.

💡 **Cómo se explica en la clase [B105-C25](../programa/clases/B105/B105-C25-adaptacion-sensoriomotora-y-control-motor-en-microgravedad/CLASE.md):**
- Un modelo con `A = 0,95` (retención) y `B = 0,20` (sensibilidad al error) enfrenta una perturbación de 30° durante 40 ensayos y luego 40 ensayos de lavado.
- 🎯 **Por qué importa:** Quien se adapta a un entorno nuevo comete errores al volver al anterior. Entender el ritmo de adaptación y el postefecto permite diseñar el entrenamiento y anticipar las torpezas.

📘 **Dónde se aprende** (1 clase): [B105-C25 · Adaptación sensoriomotora y control motor en microgravedad](../programa/clases/B105/B105-C25-adaptacion-sensoriomotora-y-control-motor-en-microgravedad/CLASE.md).

### Lazo

- Fase geométrica: giro neto de un lazo cerrado en el espacio articular. Lazo: trayectoria que vuelve al punto de partida.

💡 **Cómo se explica en la clase [B101-C06](../programa/clases/B101/B101-C06-simulacion-de-un-brazo-robotico-espacial/CLASE.md):**
- El giro crece casi con el área del lazo (de 20° a 40°, el área se multiplica por 4 y el giro por 3,87).
- Con el lazo de 40°: el centro de masa del sistema se mantiene en `2,7×10⁻¹⁷` m; el momento angular recalculado con velocidades por diferencias de la trayectoria (independiente de los `Aᵢ`) queda en `1,8×10⁻⁴` kg m²/s como máximo.
- 🎯 **Por qué importa:** En una estación o un satélite pesado la base casi no se mueve; en un satélite pequeño, sí. La decisión central: ¿cuánto se mueve la base al mover el brazo y cómo afecta eso a la posición del extremo?

📘 **Dónde se aprende** (1 clase): [B101-C06 · Simulación de un brazo robótico espacial](../programa/clases/B101/B101-C06-simulacion-de-un-brazo-robotico-espacial/CLASE.md).

### Lazo cerrado

- En un lazo cerrado, la referencia `r` es lo que se desea, la salida `y` lo que se tiene, el error `e = r − H y` su diferencia, `d` una perturbación y `n` el ruido de medida.

💡 **Cómo se explica en la clase [B16-C06](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md):**
- En realimentación negativa, `y = G (u − H y)`, luego `y = G u/(1 + G H)`: la función de transferencia en lazo cerrado es `G/(1 + G H)`.
- 🎯 **Por qué importa:** Un sistema de control de actitud tiene sensores, un computador, ruedas y un cuerpo, todos conectados y, sobre todo, con la salida de vuelta a la entrada. Para entender qué hace el conjunto no basta conocer las partes: hay que saber cómo se combinan.

📘 **Dónde se aprende** (2 clases): [B16-C06 · Diagramas de bloques](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md); [B42-C20 · Laboratorio de corrección óptica simulada](../programa/clases/B42/B42-C20-laboratorio-de-correccion-optica-simulada/CLASE.md).

### Lazo de diseño

- El lazo de diseño es la dependencia circular entre masa y potencia.

🎯 **Por qué importa (clase B83-C20):** Cada presupuesto aislado puede cerrar y el conjunto no. La decisión central: ¿existe una masa seca que sea coherente con la potencia, las baterías, la estructura y el propelente que ella misma exige, y cabe en el límite?

📘 **Dónde se aprende** (1 clase): [B83-C20 · Diseño preliminar completo de misión](../programa/clases/B83/B83-C20-diseno-preliminar-completo-de-mision/CLASE.md).

### Lazo de enganche de fase (PLL)

- El lazo de enganche de fase (PLL) compara la fase de entrada con la de un NCO y corrige.

🎯 **Por qué importa (clase B89-C10):** Un lazo demasiado ancho deja pasar ruido; uno demasiado estrecho pierde el Doppler. Ajustarlo es el equilibrio central de la sincronización y condiciona la recepción de señales débiles (C24).

📘 **Dónde se aprende** (1 clase): [B89-C10 · Sincronización de portadora](../programa/clases/B89/B89-C10-sincronizacion-de-portadora/CLASE.md).

### Lazo del agua

- El lazo del agua electroliza esa agua para recuperar hidrógeno.

🎯 **Por qué importa (clase B59-C09):** Un combustible fabricado en destino depende de qué parte del hidrógeno se recicla. La decisión central: ¿cuánto hidrógeno hay que importar para fabricar 1 000 kg de propelente O₂/CH₄?

📘 **Dónde se aprende** (1 clase): [B59-C09 · Fabricación de combustibles conceptuales](../programa/clases/B59/B59-C09-fabricacion-de-combustibles-conceptuales/CLASE.md).

### Lazo integral

- El lazo integral une dinámica, sensores, estimador, control y actuadores.

💡 **Cómo se explica en la clase [B87-C20](../programa/clases/B87/B87-C20-simulacion-adcs-integral/CLASE.md):**
- Lazo integral de tiempo discreto (esta clase).
- 🎯 **Por qué importa:** Cada pieza funciona sola; juntas pueden interactuar (el ruido del estimador entra al control, el control mueve la actitud que mide el sensor). La decisión central: ¿qué apuntamiento real se logra con el lazo completo y cómo se sabe que la simulación es coherente?

📘 **Dónde se aprende** (1 clase): [B87-C20 · Simulación ADCS integral](../programa/clases/B87/B87-C20-simulacion-adcs-integral/CLASE.md).

### Lazo PI

- El lazo PI calcula `u = K_p e + K_i ∫e dt`.

🎯 **Por qué importa (clase B85-C10):** Un termostato de dos estados oscila; un lazo proporcional-integral mantiene una temperatura sin oscilar, pero se equivoca si el calentador se satura. La decisión central: ¿qué ganancias dan error nulo sin sobreimpulso y qué pasa cuando el calentador se satura?

📘 **Dónde se aprende** (1 clase): [B85-C10 · Control térmico activo](../programa/clases/B85/B85-C10-control-termico-activo/CLASE.md).

### L-BFGS-B

- El escalado divide cada variable por un valor típico. L-BFGS-B es un método cuasi-Newton con cotas.

💡 **Cómo se explica en la clase [B81-C09](../programa/clases/B81/B81-C09-variables-de-diseno-orbital/CLASE.md):**
- Una explicación probable, que el laboratorio no verifica por separado: la derivada por diferencias finitas usa un paso absoluto pequeño; para `r_b ≈ 10⁹ km` el cambio de la función es del orden del redondeo y el gradiente se ve casi nulo, de modo que L-BFGS-B declara convergencia casi sin moverse.
- *Descripción textual:* las variables pueden pasar al optimizador tal cual o escaladas; el `Δv` total se minimiza con L-BFGS-B y se compara con una rejilla.
- 🎯 **Por qué importa:** Un optimizador que se detiene a la primera iteración no ha encontrado nada: puede ser un problema de escala y no de física. La decisión central: ¿qué variables elegir y cómo escalarlas para que el optimizador haga su trabajo?

📘 **Dónde se aprende** (1 clase): [B81-C09 · Variables de diseño orbital](../programa/clases/B81/B81-C09-variables-de-diseno-orbital/CLASE.md).

### Lbf·s

- Lección aprendida: conocimiento extraído de un error para evitarlo. lbf·s: libra-fuerza por segundo (impulso).

💡 **Cómo se explica en la clase [B96-C19](../programa/clases/B96/B96-C19-lecciones-aprendidas-operativas/CLASE.md):**
- Una prueba de aceptación convierte lo entregado a N·s y lo compara con lo esperado: acepta `0,4496 lbf·s` y rechaza `0,4496` declarado como N·s.
- *Descripción textual:* el software de tierra entrega un número en lbf·s y navegación lo lee como N·s, subestimando el impulso; la defensa añade la unidad al dato y una prueba que rechaza lo que no coincide.
- 🎯 **Por qué importa:** Un número sin unidad es una trampa: el programa corre, el valor parece razonable y la nave se pierde. La decisión central: ¿cómo se evita que una conversión de unidades pase inadvertida entre el software de tierra y el de vuelo?

📘 **Dónde se aprende** (1 clase): [B96-C19 · Lecciones aprendidas operativas](../programa/clases/B96/B96-C19-lecciones-aprendidas-operativas/CLASE.md).

### LDPC

- Un código LDPC (*low-density parity-check*) se define por una matriz de paridad `H` con pocos unos; una palabra es válida si `H·c = 0`.

💡 **Cómo se explica en la clase [B94-C01](../programa/clases/B94/B94-C01-codigos-reed-solomon-y-ldpc/CLASE.md):**
- Descripción larga: la corrección es todo o nada alrededor de `E`; el LDPC degrada con suavidad al subir el ruido y gasta más iteraciones.
- ⚠️ **Error frecuente:** Presentar el LDPC de juguete como el del estándar. Se corrige con 8.5 y la sección 10.
- 🎯 **Por qué importa:** Un enlace profundo opera con relaciones señal-ruido bajas y no puede reenviar cada trama. La decisión central: ¿cuántos símbolos erróneos tolera una palabra de código, cuánta redundancia cuesta y qué ocurre cuando se supera esa capacidad?

📘 **Dónde se aprende** (1 clase): [B94-C01 · Códigos Reed-Solomon y LDPC](../programa/clases/B94/B94-C01-codigos-reed-solomon-y-ldpc/CLASE.md).

### LE90

- El LE90 es el error lineal al 90 %: el valor bajo el cual está el 90 % de los errores absolutos.

💡 **Cómo se explica en la clase [B57-C31](../programa/clases/B57/B57-C31-errores-y-validacion-de-modelos-de-elevacion/CLASE.md):**
- Con 200 000 errores gaussianos de `σ = 2 m`: RMSE `2,002`, NMAD `2,008` y LE90 `3,298` (teoría `1,645σ = 3,290`).
- Los atípicos inflan el RMSE y casi no mueven el NMAD ni el LE90: el RMSE es la métrica más frágil.
- ⚠️ **Error frecuente:** Mezclar LE90 y desviación estándar. Son métricas distintas (sección 6).
- 🎯 **Por qué importa:** Decir «el MDE tiene 4 m de error» sin definir la métrica ni los puntos de control no significa nada. La decisión central: ¿qué métrica y qué intervalo de confianza reporto para que mi validación sea comparable y honesta?

📘 **Dónde se aprende** (1 clase): [B57-C31 · Errores y validación de modelos de elevación](../programa/clases/B57/B57-C31-errores-y-validacion-de-modelos-de-elevacion/CLASE.md).

### Leapfrog

- El leapfrog (kick–drift–kick) es el de segundo orden más sencillo.
- El leapfrog (kick–drift–kick) alterna medio paso de velocidad, un paso de posición y otro medio de velocidad; es simpléctico: conserva la estructura hamiltoniana y su energía oscila sin derivar.
- El leapfrog (kick-drift-kick) hace medio paso de velocidad, un paso de posición y otro medio de velocidad: es de orden 2 y simpléctico.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C20](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md):**
- (3) Orden de convergencia: al reducir `dt` a la mitad, el error de cierre de leapfrog debe dividirse por 4 y el de Euler por 2.
- El error de cierre de leapfrog, `1,383 × 10⁻⁴`, es casi toda diferencia de fase: `2π · 689/31 558 289 = 1,37 × 10⁻⁴` rad.
- 🎯 **Por qué importa:** Un simulador es la forma de explorar un fenómeno cuya solución no tienes a mano, y de comprobar que entiendes uno cuya solución sí conoces. Aquí conoces la respuesta (una órbita circular se repite con un período dado por una fórmula), así que puedes verificar el simulador antes de confiar en él para casos que no conoces.

📘 **Dónde se aprende** (5 clases): [B07-C20 · Primer simulador de un movimiento celeste](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md); [B11-C11 · Métodos simplécticos](../programa/clases/B11/B11-C11-metodos-simplecticos/CLASE.md); [B52-C19 · Estabilidad a largo plazo de sistemas](../programa/clases/B52/B52-C19-estabilidad-a-largo-plazo-de-sistemas/CLASE.md); [B58-C02 · Dinámica de asteroides](../programa/clases/B58/B58-C02-dinamica-de-asteroides/CLASE.md); [B73-C08 · Sistemas de N cuerpos](../programa/clases/B73/B73-C08-sistemas-de-n-cuerpos/CLASE.md).

### Lección aprendida

- Lección aprendida: conocimiento extraído de un error para evitarlo.

🎯 **Por qué importa (clase B96-C19):** Un número sin unidad es una trampa: el programa corre, el valor parece razonable y la nave se pierde. La decisión central: ¿cómo se evita que una conversión de unidades pase inadvertida entre el software de tierra y el de vuelo?

📘 **Dónde se aprende** (1 clase): [B96-C19 · Lecciones aprendidas operativas](../programa/clases/B96/B96-C19-lecciones-aprendidas-operativas/CLASE.md).

### Lecciones aprendidas

- La detección es notar el incidente; la contención limita su alcance; la erradicación elimina la causa; la recuperación restablece el servicio; las lecciones aprendidas mejoran el plan.

🎯 **Por qué importa (clase B122-C06):** B96-C15 trata emergencias operativas, no incidentes cibernéticos. La decisión central: ¿cuánto reduce el daño esperado acortar la detección o la contención?

📘 **Dónde se aprende** (1 clase): [B122-C06 · Respuesta a incidentes cibernéticos en operaciones de misión](../programa/clases/B122/B122-C06-respuesta-a-incidentes-ciberneticos-en-operaciones-de-mision/CLASE.md).

### Lecho

- El lecho es el regolito dentro del recipiente.

💡 **Cómo se explica en la clase [B59-C06](../programa/clases/B59/B59-C06-extraccion-y-procesamiento-de-volatiles/CLASE.md):**
- Límite: en el lecho la conducción es lenta y la olla no es uniforme.
- 🎯 **Por qué importa:** Con poco hielo hay que calentar mucha roca. La decisión central: ¿cuánta energía por kilogramo de agua pide una abundancia de 5,6 % frente a 2,7 %?

📘 **Dónde se aprende** (1 clase): [B59-C06 · Extracción y procesamiento de volátiles](../programa/clases/B59/B59-C06-extraccion-y-procesamiento-de-volatiles/CLASE.md).

### Lectura de zona

- La lectura de zona es la posición de la cuchilla para oscurecer una zona.

🎯 **Por qué importa (clase B43-C06):** La prueba convierte una desviación de nanómetros en un desplazamiento de milímetros de la cuchilla. La decisión central: ¿en cuánto debe desplazarse la cuchilla para cada zona del paraboloide y cuántas bandas de Ronchi se esperan?

📘 **Dónde se aprende** (1 clase): [B43-C06 · Pruebas de Ronchi y Foucault](../programa/clases/B43/B43-C06-pruebas-de-ronchi-y-foucault/CLASE.md).

### Lectura por columna

- La lectura por columna usa un amplificador por columna.

🎯 **Por qué importa (clase B44-C03):** El diseño CMOS cambia el ruido y la geometría de la lectura. La decisión central: ¿qué ruido elimina el CDS y qué artefacto introduce el obturador rodante?

📘 **Dónde se aprende** (1 clase): [B44-C03 · Sensores CMOS](../programa/clases/B44/B44-C03-sensores-cmos/CLASE.md).

### Lectura-hacer

- Lectura-hacer (*read-do*): se lee un paso y se ejecuta.

💡 **Cómo se explica en la clase [B110-C05](../programa/clases/B110/B110-C05-checklists-de-emergencia-ejecucion-y-verificacion-cruzada/CLASE.md):**
- Paso 4 · Costo. `20 × 12 s = 240 s`, `120 s` más que lectura-hacer.
- Por modalidad: lectura-hacer, respuesta, verificación cruzada.
- 🎯 **Por qué importa:** Los checklists de emergencia se leen y verifican bajo estrés y no tenían clase propia. La decisión central: ¿cuánta verificación cruzada vale su costo en tiempo, y qué la hace menos eficaz de lo que parece?

📘 **Dónde se aprende** (1 clase): [B110-C05 · Checklists de emergencia: ejecución y verificación cruzada](../programa/clases/B110/B110-C05-checklists-de-emergencia-ejecucion-y-verificacion-cruzada/CLASE.md).

### Lectura-respuesta

- Lectura-hacer (*read-do*): se lee un paso y se ejecuta. Lectura-respuesta (*challenge-response*): uno lee, el otro responde tras comprobar.

🎯 **Por qué importa (clase B110-C05):** Los checklists de emergencia se leen y verifican bajo estrés y no tenían clase propia. La decisión central: ¿cuánta verificación cruzada vale su costo en tiempo, y qué la hace menos eficaz de lo que parece?

📘 **Dónde se aprende** (1 clase): [B110-C05 · Checklists de emergencia: ejecución y verificación cruzada](../programa/clases/B110/B110-C05-checklists-de-emergencia-ejecucion-y-verificacion-cruzada/CLASE.md).

### Ledoux

- Schwarzschild: hay convección si `∇_rad > ∇_ad`. Ledoux: si `∇_rad > ∇_ad + (φ/δ) ∇_μ`.

💡 **Cómo se explica en la clase [B37-C01](../programa/clases/B37/B37-C01-conveccion-longitud-de-mezcla-y-criterios-de-schwarzschild-y-ledoux/CLASE.md):**
- Con `∇_μ = 0,15` y `φ/δ = 1`, la capa con `∇_rad = 0,45` es inestable por Schwarzschild y estable por Ledoux (el umbral sube a `0,55`); con `0,60` y `0,70` ambos criterios dicen inestable.
- 🎯 **Por qué importa:** Sin convección, un modelo de interior calcularía temperaturas imposibles en las capas inestables. La decisión central: ¿la capa es estable, y si no lo es, qué gradiente real `∇` y qué fracción del flujo lleva la convección?

📘 **Dónde se aprende** (1 clase): [B37-C01 · Convección: longitud de mezcla y criterios de Schwarzschild y Ledoux](../programa/clases/B37/B37-C01-conveccion-longitud-de-mezcla-y-criterios-de-schwarzschild-y-ledoux/CLASE.md).

### Leer y hacer

- La lista de comprobación es una secuencia verificable de pasos. Leer y hacer (*read-do*) es leer cada paso y ejecutarlo.

💡 **Cómo se explica en la clase [B104-C22](../programa/clases/B104/B104-C22-diseno-y-uso-de-listas-de-comprobacion-de-cabina/CLASE.md):**
- Una interrupción con probabilidad 0,05 y 50 % de retomar mal agrega 0,025 de omisión: comparable con la de leer y hacer con 10 pasos (0,0393).
- 🎯 **Por qué importa:** Una lista larga con verificación a cada paso consume tiempo justo cuando hay poco. La decisión central: ¿qué formato y qué longitud de lista dan la menor probabilidad de omisión que el tiempo disponible permita, y qué hace una interrupción con todo eso?

📘 **Dónde se aprende** (1 clase): [B104-C22 · Diseño y uso de listas de comprobación de cabina](../programa/clases/B104/B104-C22-diseno-y-uso-de-listas-de-comprobacion-de-cabina/CLASE.md).

### Lejana

- Una variante cercana cambia los números; una media, además el cuerpo central o la magnitud pedida; una lejana, también el contexto y las unidades.

💡 **Cómo se explica en la clase [B131-C07](../programa/clases/B131/B131-C07-ejercicios-de-transferencia/CLASE.md):**
- Lejana (3): satélite a `14,8` radios jovianos nominales de Júpiter, `P` en días → `7,032 días`.
- La cercana mide ejecución del procedimiento; la media, si el estudiante reconoce el papel de `M`; la lejana, si entiende la ley como relación entre magnitudes y no como una receta en UA y años.
- 🎯 **Por qué importa:** Resolver bien un problema practicado puede ser memoria. La decisión central: ¿qué debe cambiar para que el ejercicio mida que el estudiante comprendió la ley y no el procedimiento?

📘 **Dónde se aprende** (1 clase): [B131-C07 · Ejercicios de transferencia](../programa/clases/B131/B131-C07-ejercicios-de-transferencia/CLASE.md).

### Lenguaje claro

- El lenguaje claro es el que el lector encuentra, entiende y usa a la primera.

🎯 **Por qué importa (clase B128-C08):** El lenguaje claro ayuda a personas con dificultades de lectura, a quienes leen en una segunda lengua, a quien lee con prisa y a quien usa un lector de pantalla. La decisión central: ¿qué cambios hacen el texto más claro sin perder ninguna cifra ni ningún aviso de seguridad?

📘 **Dónde se aprende** (1 clase): [B128-C08 · Lenguaje claro y redacción accesible](../programa/clases/B128/B128-C08-lenguaje-claro-y-redaccion-accesible/CLASE.md).

### Lente de brecha

- La lente de brecha es el relleno de fragmentos del fondo.

💡 **Cómo se explica en la clase [B61-C02](../programa/clases/B61/B61-C02-crateres-simples-morfologia-y-formacion/CLASE.md):**
- *Descripción textual:* la cavidad transitoria se ensancha por colapso de la pared hasta el bol aparente y una lente de brecha lo rellena, dejando una profundidad residual que se calcula por bisección.
- Descripción larga: el volumen crece como `D³`; la lente de brecha reduce la profundidad aparente un 23 %.
- 🎯 **Por qué importa:** Medir un cráter es medir un bol, pero lo que se ve es el bol después de colapsar y rellenarse. La decisión central: ¿cuánto volumen tenía la cavidad original y cuánto se perdió en el relleno de brecha?

📘 **Dónde se aprende** (1 clase): [B61-C02 · Cráteres simples: morfología y formación](../programa/clases/B61/B61-C02-crateres-simples-morfologia-y-formacion/CLASE.md).

### Lente delgada

- Una lente delgada de distancia focal `f` cumple `1/f = 1/d_o + 1/d_i`, con `d_o` la distancia del objeto y `d_i` la de la imagen.

💡 **Cómo se explica en la clase [B05-C19](../programa/clases/B05/B05-C19-optica-y-velocidad-de-la-luz/CLASE.md):**
- B -- "dónde se forma la imagen" --> C["Rayos: Snell y lente delgada"]
- 🎯 **Por qué importa:** Un telescopio espacial o una cámara en órbita baja distinguen detalles hasta cierto límite que no depende de la calidad de la electrónica, y la luz de un objeto lejano llega con retraso. La pregunta motivadora es: ¿qué determina cuán pequeño es el detalle que un instrumento óptico puede resolver y cuánto tarda la luz en llegar?

📘 **Dónde se aprende** (2 clases): [B05-C19 · Óptica y velocidad de la luz](../programa/clases/B05/B05-C19-optica-y-velocidad-de-la-luz/CLASE.md); [B41-C05 · Lentes delgadas y gruesas](../programa/clases/B41/B41-C05-lentes-delgadas-y-gruesas/CLASE.md).

### Lente gravitacional

- Una lente gravitacional es una masa que desvía la luz de una fuente más lejana.

💡 **Cómo se explica en la clase [B25-C14](../programa/clases/B25/B25-C14-lentes-gravitacionales-galacticas/CLASE.md):**
- Una lente de vidrio desvía la luz según su forma; una lente gravitacional la desvía según su masa.
- Su límite: el vidrio tiene un foco; la lente gravitacional puntual no (desvía más los rayos cercanos que los lejanos), y su efecto sobre la imagen depende de cómo se reparte la masa.
- 🎯 **Por qué importa:** La luz de una galaxia lejana se curva al pasar cerca de una masa, y la masa interior se deduce del tamaño de la distorsión sin importar si es luminosa u oscura ni si está en equilibrio. Por eso las lentes son una prueba directa de la distribución de masa.

📖 **Explicado a fondo:** [Lente gravitacional](esencial/esencial-d-l.md#lente-gravitacional) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B25-C14 · Lentes gravitacionales galácticas](../programa/clases/B25/B25-C14-lentes-gravitacionales-galacticas/CLASE.md).

### Lente gravitacional débil

- La lente gravitacional débil mide masas por la distorsión de imágenes de fondo.

🎯 **Por qué importa (clase B26-C18):** Si las estrellas y el gas fueran toda la masa, las estrellas de los bordes de una galaxia irían más despacio que las del centro; observaciones de este tipo y de lentes gravitacionales indican que hay mucha más masa que la que se ve.

📘 **Dónde se aprende** (1 clase): [B26-C18 · Materia oscura y evidencias](../programa/clases/B26/B26-C18-materia-oscura-y-evidencias/CLASE.md).

### Lenticular

- Una galaxia espiral tiene un disco con brazos, gas y formación estelar; una elíptica es un sistema de estrellas viejas sin disco notable; una lenticular tiene disco pero sin brazos (S1).

🎯 **Por qué importa (clase B25-C09):** Las galaxias parecen muy distintas: discos con brazos y gas, o bolas suaves de estrellas viejas. Esa diferencia guarda su historia (formación estelar, fusiones) y exige un lenguaje común para compararlas.

📘 **Dónde se aprende** (1 clase): [B25-C09 · Galaxias elípticas y espirales](../programa/clases/B25/B25-C09-galaxias-elipticas-y-espirales/CLASE.md).

### Lento

- El modo rápido y el lento son las dos ondas magnetosónicas.
- Un rotador rápido tiene rotación ordenada comparable a su dispersión; uno lento, poca rotación (S2).

🎯 **Por qué importa (clase B25-C09):** Las galaxias parecen muy distintas: discos con brazos y gas, o bolas suaves de estrellas viejas. Esa diferencia guarda su historia (formación estelar, fusiones) y exige un lenguaje común para compararlas.

📘 **Dónde se aprende** (2 clases): [B25-C09 · Galaxias elípticas y espirales](../programa/clases/B25/B25-C09-galaxias-elipticas-y-espirales/CLASE.md); [B35-C02 · Ondas de Alfvén y ondas magnetosónicas](../programa/clases/B35/B35-C02-ondas-de-alfven-y-ondas-magnetosonicas/CLASE.md).

### LEOP

- Propiedad de seguridad: condición que siempre debe cumplirse. LEOP: fase de lanzamiento y primeras órbitas.

💡 **Cómo se explica en la clase [B96-C08](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md):**
- Búsqueda en anchura desde LEOP: SEGURO y COMISIONADO a 1 paso, NOMINAL a 2, CIENCIA, MANTENIMIENTO y DESORBITANDO a 3, FIN a 4.
- (3) El comando de ciencia solo vale en NOMINAL y CIENCIA: lo rechazan LEOP, SEGURO, COMISIONADO, MANTENIMIENTO, DESORBITANDO y FIN.
- 🎯 **Por qué importa:** Un comando válido en un estado puede ser peligroso en otro; y un modo seguro al que no se puede volver es una trampa. La decisión central: ¿qué transiciones existen y se puede siempre llegar al estado seguro?

📘 **Dónde se aprende** (1 clase): [B96-C08 · Gestión de estados de satélite](../programa/clases/B96/B96-C08-gestion-de-estados-de-satelite/CLASE.md).

### Leptón

- Un leptón como electrón o neutrino.

🎯 **Por qué importa (clase B31-C10):** Antes de calcular una sección eficaz, una reacción debe respetar las leyes de conservación. La decisión central: ¿está permitida esta reacción por las reglas de conservación?

📘 **Dónde se aprende** (1 clase): [B31-C10 · Modelo estándar de partículas](../programa/clases/B31/B31-C10-modelo-estandar-de-particulas/CLASE.md).

### L-estable

- Un método es A-estable si es estable para todo `Re z < 0` y L-estable si además `|R(z)| → 0` cuando `z → −∞`: amortigua del todo los modos muy rápidos.

🎯 **Por qué importa (clase B11-C22):** Los modelos térmicos, de combustión, de propulsión y de química atmosférica mezclan escalas de microsegundos con horas. Un integrador explícito pagaría el paso del más rápido durante toda la simulación.

📘 **Dónde se aprende** (1 clase): [B11-C22 · Métodos implícitos y sistemas rígidos](../programa/clases/B11/B11-C22-metodos-implicitos-y-sistemas-rigidos/CLASE.md).

### LET

- El LET (transferencia lineal de energía) es el cociente `dE/dl` entre la energía que una partícula cargada pierde por colisiones y la distancia recorrida; su unidad es J/m, a menudo keV/µm (definición del glosario de ICRP 103, consultado).

💡 **Cómo se explica en la clase [B112-C01](../programa/clases/B112/B112-C01-magnitudes-dosimetricas-dosis-absorbida-let-y-eficacia-biologica/CLASE.md):**
- Una traza que cruza el núcleo con la cuerda media `2d/3 = 6,67 µm` deja `E = LET × cuerda`.
- Para el hierro ilustrativo de 150 keV/µm son `1000 keV = 1,6 × 10⁻¹³ J`; sobre la masa del núcleo, `0,306 Gy` por un solo impacto, frente a `1,02 mGy` de un protón de 0,5 keV/µm: un factor 300, el cociente de los LET.
- ⚠️ **Error frecuente:** `D = Φ·LET/ρ` las relaciona (8.3).
- 🎯 **Por qué importa:** B105-C06 introduce la exposición a la radiación espacial como un hecho del entorno, pero no define qué se mide ni en qué unidades. Sin esa definición no se puede leer una tasa de dosis de una misión ni entender por qué los iones pesados preocupan más que los protones.

📘 **Dónde se aprende** (1 clase): [B112-C01 · Magnitudes dosimétricas: dosis absorbida, LET y eficacia biológica](../programa/clases/B112/B112-C01-magnitudes-dosimetricas-dosis-absorbida-let-y-eficacia-biologica/CLASE.md).

### LET umbral

- El LET umbral `L₀` es el LET mínimo con que ocurre el evento.

🎯 **Por qué importa (clase B88-C03):** Un procesador comercial puede fallar en órbita por una sola partícula. La decisión central: ¿cuántos eventos esperar al año y qué margen de dosis hay respecto del fallo del componente?

📘 **Dónde se aprende** (1 clase): [B88-C03 · Procesadores tolerantes a radiación](../programa/clases/B88/B88-C03-procesadores-tolerantes-a-radiacion/CLASE.md).

### LEU

- TED es la dosis efectiva total. LEU es uranio poco enriquecido (< 20 % de U-235).

💡 **Cómo se explica en la clase [B86-C18](../programa/clases/B86/B86-C18-seguridad-y-licenciamiento-energetico/CLASE.md):**
- *Descripción textual:* primero se ve si hay fisión (LEU nivel II, otro combustible nivel III); luego la probabilidad de más de 25 rem (nivel III); luego la actividad frente a `100000 × A2` (nivel II) y la probabilidad de 5–25 rem (nivel II); si nada se cumple, es nivel I.
- 🎯 **Por qué importa:** Los límites de la energía nuclear en el espacio son tanto jurídicos y de seguridad como técnicos: quién aprueba, con qué análisis y con qué umbrales. Un ingeniero de potencia debe saber que estas decisiones existen y qué datos las gobiernan.

📘 **Dónde se aprende** (1 clase): [B86-C18 · Seguridad y licenciamiento energético](../programa/clases/B86/B86-C18-seguridad-y-licenciamiento-energetico/CLASE.md).

### Levenberg–Marquardt

- Un residuo es una diferencia con el objetivo. Levenberg–Marquardt mezcla Gauss–Newton con descenso de gradiente mediante un amortiguamiento `λ`.
- La determinación de órbitas estima los elementos a partir de observaciones. Levenberg–Marquardt es un método de mínimos cuadrados que interpola entre Gauss–Newton y descenso de gradiente con un amortiguamiento `λ`.

🎯 **Por qué importa (clase B50-C02):** Un diseñador no ajusta curvaturas a mano: define qué es «bueno» como un número y deja que el cálculo busque. La decisión central: ¿qué mide la función de mérito y qué fija la restricción?

📘 **Dónde se aprende** (2 clases): [B50-C02 · Optimización de superficies: función de mérito y restricciones](../programa/clases/B50/B50-C02-optimizacion-de-superficies-funcion-de-merito-y-restricciones/CLASE.md); [B58-C07 · Determinación de órbitas](../programa/clases/B58/B58-C07-determinacion-de-orbitas/CLASE.md).

### Ley B-dot

- La ley B-dot es `m = −k Ḃ`.

🎯 **Por qué importa (clase B87-C16):** Sin estimador de actitud ni giroscopio calibrado, el satélite recién desplegado necesita detenerse con lo mínimo. La decisión central: ¿cuánto tarda, qué ganancia usar y qué velocidad residual queda?

📘 **Dónde se aprende** (1 clase): [B87-C16 · Detumbling después del despliegue](../programa/clases/B87/B87-C16-detumbling-despues-del-despliegue/CLASE.md).

### Ley d²

- La ley `d²` da la vida de una gota que se evapora.

🎯 **Por qué importa (clase B115-C04):** En un hábitat, cada litro y cada kilogramo cuentan. La decisión central: ¿cuánto tiempo puede pasar entre dos nieblas sin que la raíz se seque, y cómo depende eso de la humedad de la cámara y del tamaño de las gotas?

📘 **Dónde se aprende** (1 clase): [B115-C04 · Sistemas aeropónicos](../programa/clases/B115/B115-C04-sistemas-aeroponicos/CLASE.md).

### Ley de −3

- La ley de −3 es la relación empírica de caída del espesor.

🎯 **Por qué importa (clase B61-C04):** El manto de ejecta es un marcador estratigráfico: cubre lo anterior y es cubierto por lo posterior. La decisión central: ¿cómo decae el espesor con la distancia y cuánto volumen contiene el manto?

📘 **Dónde se aprende** (1 clase): [B61-C04 · Mantos de ejecta y depósitos de impacto](../programa/clases/B61/B61-C04-mantos-de-ejecta-y-depositos-de-impacto/CLASE.md).

### Ley de Amdahl

- La ley de Amdahl dice `S(p) = 1/(s + (1−s)/p) ≤ 1/s`.

🎯 **Por qué importa (clase B14-C13):** Un análisis de miles de simulaciones tarda una noche. Tienes ocho núcleos.

📘 **Dónde se aprende** (1 clase): [B14-C13 · Computación paralela](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md).

### Ley de Archard

- La ley de Archard da la profundidad de desgaste `h = k c p s/H_s`.

🎯 **Por qué importa (clase B84-C36):** Un sello de acero inoxidable bajo regolito pierde 1,8 mm en 1000 h con un 10 % del área expuesta a polvo, y uno de carburo de volframio pierde 0,18 µm: la elección de dureza decide si el mecanismo vive. La decisión central: ¿qué superficie y qué estrategia de protección permiten que un mecanismo sobreviva al regolito?

📘 **Dónde se aprende** (1 clase): [B84-C36 · Desgaste abrasivo por regolito en mecanismos](../programa/clases/B84/B84-C36-desgaste-abrasivo-por-regolito-en-mecanismos/CLASE.md).

### Ley de Arrhenius

- La ley de Arrhenius da `η = η₀ exp(E_a/RT)`.

💡 **Cómo se explica en la clase [B59-C12](../programa/clases/B59/B59-C12-sinterizacion-de-materiales/CLASE.md):**
- ⚠️ **Error frecuente:** Usar ºC en la ley de Arrhenius. Siempre en kelvin; sección 10.
- 🎯 **Por qué importa:** Una variación de 50 K en el horno cambia el tiempo de sinterización en un factor 2,6. La decisión central: ¿con qué precisión hay que controlar la temperatura, y cuánta energía cuesta alcanzarla?

📘 **Dónde se aprende** (1 clase): [B59-C12 · Sinterización de materiales](../programa/clases/B59/B59-C12-sinterizacion-de-materiales/CLASE.md).

### Ley de Beer–Lambert

- La ley de Beer–Lambert da la transmitancia directa `T = e^{−τ/μ}` con `μ = cos(cenital)`.

🎯 **Por qué importa (clase B57-C13):** Un satélite que mira un incendio, un volcán o el mar tiene que descontar la atmósfera, y los aerosoles son lo más variable. La decisión central: ¿cuánto aerosol hay y qué tipo, con qué incertidumbre, a partir de pocas longitudes de onda?

📘 **Dónde se aprende** (1 clase): [B57-C13 · Atmósfera y aerosoles](../programa/clases/B57/B57-C13-atmosfera-y-aerosoles/CLASE.md).

### Ley de Bouguer

- La ley de Bouguer `m = m₀ + kX`.

🎯 **Por qué importa (clase B45-C22):** Sin corregir la extinción, la fotometría terrestre depende de la hora. La decisión central: ¿qué `k` y qué fórmula de masa de aire dan la corrección y con qué error?

📘 **Dónde se aprende** (1 clase): [B45-C22 · Extinción atmosférica, masa de aire y coeficientes de color](../programa/clases/B45/B45-C22-extincion-atmosferica-masa-de-aire-y-coeficientes-de-color/CLASE.md).

### Ley de Boyle

- La ley de Boyle dice que, a temperatura constante, `p V` es constante.

🎯 **Por qué importa (clase B05-C14):** La cabina de una nave contiene aire a una presión que debe mantenerse, y una escotilla soporta decenas de miles de newtons. La pregunta motivadora es: ¿qué relaciona presión, volumen, temperatura y cantidad de gas, y cómo cambia la presión con la altura en una atmósfera?

📘 **Dónde se aprende** (1 clase): [B05-C14 · Gases y presión](../programa/clases/B05/B05-C14-gases-y-presion/CLASE.md).

### Ley de Coffin–Manson

- La ley de Coffin–Manson `N = N₀ (ΔT₀/ΔT)ⁿ` da los ciclos hasta la falla.

💡 **Cómo se explica en la clase [B85-C11](../programa/clases/B85/B85-C11-ciclos-termicos/CLASE.md):**
- Límite: la ley de Coffin–Manson de la clase es un modelo con constantes ilustrativas; la vida real depende del material, la unión y los ensayos.
- 🎯 **Por qué importa:** La amplitud térmica de cada ciclo decide la vida por fatiga de soldaduras y uniones, y se reduce con inercia térmica o con calentadores. La decisión central: ¿qué amplitud de ciclo y cuántos ciclos acumula una unión en la misión, y cuánto la reduce la inercia térmica?

📘 **Dónde se aprende** (1 clase): [B85-C11 · Ciclos térmicos](../programa/clases/B85/B85-C11-ciclos-termicos/CLASE.md).

### Ley de conservación

- Una ley de conservación es una ecuación `q_t + f(q)_x = 0` que dice que la cantidad `q` solo cambia por el flujo `f(q)` en las fronteras.

💡 **Cómo se explica en la clase [B21-C01](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md):**
- Para una sola variable, `q(x, t)`, la ley de conservación es `∂q/∂t + ∂f(q)/∂x = 0`.
- 🎯 **Por qué importa:** Casi todo lo que fluye en el espacio —el viento solar, el gas de un disco de acreción, el gas que rodea a una nave en reentrada, la onda de choque de una eyección coronal— obedece leyes de conservación: una cantidad cambia en una región solo porque entra o sale por sus bordes.

📘 **Dónde se aprende** (1 clase): [B21-C01 · Volúmenes finitos y solucionadores de Riemann para leyes de conservación](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md).

### Ley de conservación de la masa

- La ley de conservación de la masa (Lavoisier) dice que, en una reacción química, la masa total de los reactivos es igual a la de los productos.

🎯 **Por qué importa (clase B06-C08):** Una vela y el Sol liberan energía, pero lo hacen de maneras radicalmente distintas. En la vela, los átomos de carbono e hidrógeno se reordenan con el oxígeno y todos siguen ahí al terminar.

📘 **Dónde se aprende** (1 clase): [B06-C08 · Reacciones y conservación de masa](../programa/clases/B06/B06-C08-reacciones-y-conservacion-de-masa/CLASE.md).

### Ley de cosenos

- En un triángulo plano con lados `a, b, c` y ángulos opuestos `A, B, C`, la ley de cosenos dice `c² = a² + b² − 2ab cos C`; la ley de senos dice `a/sen A = b/sen B = c/sen C`.

💡 **Cómo se explica en la clase [B04-C08](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md):**
- *Descripción textual:* según los datos (LAL o LLL, ALA o LLA) se usa la ley de cosenos, el tercer ángulo y la de senos, o la de senos con posible ambigüedad; todo termina comprobando que los ángulos suman 180°.
- La ley de cosenos es la más segura: no tiene ambigüedad y sirve con LAL y LLL.
- 🎯 **Por qué importa:** Cuando una sonda se comunica con la Tierra, el tiempo de la señal depende de la distancia, que cambia de unos 55 millones de km a unos 400 millones según dónde estén ambos planetas en sus órbitas.

📘 **Dónde se aprende** (1 clase): [B04-C08 · Ley de senos y ley de cosenos](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md).

### Ley de Coulomb

- La ley de Coulomb dice que dos cargas puntuales `q₁` y `q₂` separadas `r` se ejercen una fuerza `F = k_e |q₁ q₂|/r²`, repulsiva si tienen el mismo signo y atractiva si es distinto, con `k_e = 1/(4π ε₀)`.
- La ley de Coulomb da la energía de interacción entre dos cargas puntuales: `E = q₁q₂/(4π ε₀ r)`, con `ε₀` la permitividad del vacío (S2).

🎯 **Por qué importa (clase B05-C15):** El espacio está lleno de partículas cargadas que un satélite atraviesa, y un satélite puede acumular carga. La pregunta motivadora es: ¿cómo describir la fuerza eléctrica sobre una carga sin conocer a la vez todas las demás, y cuánto más fuerte es que la gravedad?

📘 **Dónde se aprende** (2 clases): [B05-C15 · Campos eléctricos](../programa/clases/B05/B05-C15-campos-electricos/CLASE.md); [B06-C04 · Enlaces iónicos y covalentes](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md).

### Ley de cuentas

- La ley de cuentas `ρ(<m)`.

🎯 **Por qué importa (clase B42-C21):** La mayoría del cielo no tiene una estrella brillante cerca: la cobertura limita a la óptica adaptativa natural. La decisión central: ¿hasta qué magnitud corrige el lazo y qué fracción del cielo queda cubierta?

📘 **Dónde se aprende** (1 clase): [B42-C21 · Estrellas guía naturales y cobertura de cielo](../programa/clases/B42/B42-C21-estrellas-guia-naturales-y-cobertura-de-cielo/CLASE.md).

### Ley de Dalton

- La ley de Dalton suma las parciales.

🎯 **Por qué importa (clase B104-C05):** Lo que importa para respirar no es la presión total sino la presión parcial de cada gas. La decisión central: ¿cuánto tiempo hay para actuar si la cabina pierde presión o si se acumula CO₂?

📘 **Dónde se aprende** (1 clase): [B104-C05 · Sistemas de vehículos tripulados](../programa/clases/B104/B104-C05-sistemas-de-vehiculos-tripulados/CLASE.md).

### Ley de degradación

- La ley de degradación `P/P₀ = 1 − C log₁₀(1 + Φ/Φₓ)` (forma convencional de fluencia equivalente).

🎯 **Por qué importa (clase B85-C24):** Una celda solar o un polímero no fallan de golpe: pierden prestaciones con la exposición. La decisión central: ¿cuánta potencia queda al final de la misión y cuánto cambia con un blindaje que reduce la fluencia?

📘 **Dónde se aprende** (1 clase): [B85-C24 · Efectos de la radiación ionizante en materiales y electrónica](../programa/clases/B85/B85-C24-efectos-de-la-radiacion-ionizante-en-materiales-y-electronica/CLASE.md).

### Ley de descarga

- La ley de descarga es `τ_mag = −K h_⊥B`, con `m = −K (B × h)/|B|²`.

🎯 **Por qué importa (clase B87-C14):** Una rueda saturada deja de controlar. La decisión central: ¿en cuánto tiempo se satura, cuánto par magnético hace falta para sostener la descarga y qué nivel de momento queda en régimen?

📘 **Dónde se aprende** (1 clase): [B87-C14 · Saturación y descarga de momento](../programa/clases/B87/B87-C14-saturacion-y-descarga-de-momento/CLASE.md).

### Ley de desplazamiento de Wien

- La ley de desplazamiento de Wien dice que la longitud de onda del máximo de `B` es inversamente proporcional a `T`: `λ_max T = b`, con `b` constante.

🎯 **Por qué importa (clase B22-C04):** Un espectro no trae escritas la temperatura ni la composición: trae un número de fotones por cada longitud de onda. Pasar de ahí a una propiedad física exige un modelo y una inversión.

📘 **Dónde se aprende** (1 clase): [B22-C04 · Inversión espectral](../programa/clases/B22/B22-C04-inversion-espectral/CLASE.md).

### Ley de escalamiento

- La ley de escalamiento relaciona el cráter con las variables del impacto.

🎯 **Por qué importa (clase B58-C15):** Para decidir si una desviación es necesaria hay que saber qué haría el impacto. La decisión central: ¿cómo escalan la energía y el cráter con el tamaño, la velocidad y el ángulo?

📘 **Dónde se aprende** (1 clase): [B58-C15 · Modelos de impacto planetario](../programa/clases/B58/B58-C15-modelos-de-impacto-planetario/CLASE.md).

### Ley de Faraday

- La ley de Faraday dice `n = I t/(z F)`.

💡 **Cómo se explica en la clase [B59-C08](../programa/clases/B59/B59-C08-produccion-de-oxigeno/CLASE.md):**
- *Descripción textual:* la tasa se convierte en moles, luego en corriente por la ley de Faraday, y en potencia con la tensión; el balance de masa cierra la reacción.
- 🎯 **Por qué importa:** Un oxidante producido en destino se mide en gramos por hora, pero el diseñador piensa en amperios y vatios. La decisión central: ¿qué corriente y qué potencia exige una tasa de oxígeno dada?

📘 **Dónde se aprende** (1 clase): [B59-C08 · Producción de oxígeno](../programa/clases/B59/B59-C08-produccion-de-oxigeno/CLASE.md).

### Ley de Fitts

- Captura exitosa: dentro de las tolerancias de posición y velocidad. Ley de Fitts: `MT = a + b log₂(2D/W)`.

💡 **Cómo se explica en la clase [B101-C10](../programa/clases/B101/B101-C10-simulacion-de-una-tarea-tripulada-con-manipulador/CLASE.md):**
- No se consultaron tiempos de reacción, retardos de comunicación, tareas de captura ni la ley de Fitts (N6, N7): sus valores aquí son sintéticos.
- 🎯 **Por qué importa:** Cuanto más tarda en llegar la imagen y la orden, más difícil es corregir. La decisión central: ¿con qué retardo total y qué ganancia el operador puede capturar con éxito y cuándo conviene pasar a «mover y esperar»?

📘 **Dónde se aprende** (1 clase): [B101-C10 · Simulación de una tarea tripulada con manipulador](../programa/clases/B101/B101-C10-simulacion-de-una-tarea-tripulada-con-manipulador/CLASE.md).

### Ley de Frenkel

- La ley de Frenkel da `(x/a)² = 3γt/(2ηa)` para flujo viscoso a pequeños cuellos.

💡 **Cómo se explica en la clase [B59-C12](../programa/clases/B59/B59-C12-sinterizacion-de-materiales/CLASE.md):**
- Límite: la ley de Frenkel supone flujo viscoso newtoniano y cuellos pequeños; el regolito real puede cristalizar.
- *Descripción textual:* la temperatura fija la viscosidad; la ley de Frenkel da el tiempo para un cuello; la regresión del logaritmo del tiempo recupera la energía de activación.
- 🎯 **Por qué importa:** Una variación de 50 K en el horno cambia el tiempo de sinterización en un factor 2,6. La decisión central: ¿con qué precisión hay que controlar la temperatura, y cuánta energía cuesta alcanzarla?

📘 **Dónde se aprende** (1 clase): [B59-C12 · Sinterización de materiales](../programa/clases/B59/B59-C12-sinterizacion-de-materiales/CLASE.md).

### Ley de Glen

- La ley de Glen es `ε̇ = A(T) τⁿ`.

🎯 **Por qué importa (clase B53-C23):** El hielo de una luna fría se comporta como un sólido casi rígido y el de un glaciar templado fluye. La decisión central: ¿cuánto cambia la velocidad de deformación con la temperatura, el espesor y la gravedad?

📘 **Dónde se aprende** (1 clase): [B53-C23 · Mecánica de hielo: reología, fracturas y deformación](../programa/clases/B53/B53-C23-mecanica-de-hielo-reologia-fracturas-y-deformacion/CLASE.md).

### Ley de gravitación

- La ley de gravitación `F = G m₁ m₂/r²`.

🎯 **Por qué importa (clase B71-C02):** La ley de gravitación convierte las leyes de Kepler de reglas empíricas en consecuencias de una fuerza. La decisión central: ¿cuánto vale la aceleración gravitatoria a una distancia dada y qué te dice sobre la masa del cuerpo central?

📘 **Dónde se aprende** (1 clase): [B71-C02 · Ley de gravitación universal](../programa/clases/B71/B71-C02-ley-de-gravitacion-universal/CLASE.md).

### Ley de gravitación universal

- La ley de gravitación universal dice que dos masas puntuales `M` y `m` separadas una distancia `r` se atraen con una fuerza `F = G M m / r²`, a lo largo de la recta que las une.

🎯 **Por qué importa (clase B05-C10):** La misma fuerza que hace caer una manzana mantiene a la Luna en órbita: esa idea unificó el cielo y la Tierra. La pregunta motivadora es: ¿cómo comprobar con números que la gravedad de la superficie y la órbita de la Luna son la misma fuerza?

📘 **Dónde se aprende** (1 clase): [B05-C10 · Gravitación universal](../programa/clases/B05/B05-C10-gravitacion-universal/CLASE.md).

### Ley de Gustafson

- La ley de Gustafson da, para escalado débil ideal, `S(p) = s + (1 − s)·p`.

💡 **Cómo se explica en la clase [B14-C16](../programa/clases/B14/B14-C16-computacion-distribuida-y-hpc/CLASE.md):**
- La ley de Gustafson (sin comunicación) da `S(64) = s + (1−s)·64 = 62,7`.
- 🎯 **Por qué importa:** Una simulación de la población de escombros orbitales requiere cien veces más cálculo del que tu equipo puede dar en una semana. Pides tiempo en un clúster y debes decidir: ¿cuántos procesos pido?

📘 **Dónde se aprende** (1 clase): [B14-C16 · Computación distribuida y HPC](../programa/clases/B14/B14-C16-computacion-distribuida-y-hpc/CLASE.md).

### Ley de Henry

- La ley de Henry relaciona el gas disuelto con su presión parcial: `[CO₂] = k_H p`.

💡 **Cómo se explica en la clase [B64-C07](../programa/clases/B64/B64-C07-cultivo-de-extremofilos-no-patogenos-en-condiciones-analogas/CLASE.md):**
- La ley de Henry usa `k_H = 0,034 mol/(L atm)` (valor ilustrativo, no consultado).
- 🎯 **Por qué importa:** Un análogo no es el otro mundo: reproduce algunas variables y deja otras. La pregunta motivadora: ¿qué parte del ambiente real estás imitando, qué parte no y qué puedes concluir de un cultivo en la cámara?

📘 **Dónde se aprende** (1 clase): [B64-C07 · Cultivo de extremófilos no patógenos en condiciones análogas](../programa/clases/B64/B64-C07-cultivo-de-extremofilos-no-patogenos-en-condiciones-analogas/CLASE.md).

### Ley de Hess

- La ley de Hess dice que la entalpía de una reacción es la misma sea cual sea el camino: `Δ_rH = Σ ν Δ_fH°(productos) − Σ ν Δ_fH°(reactivos)`, con `ν` los coeficientes de la ecuación balanceada.

💡 **Cómo se explica en la clase [B06-C12](../programa/clases/B06/B06-C12-termoquimica-y-energia-de-reaccion/CLASE.md):**
- Puedes medirla (calorimetría, directa pero requiere equipo y cuidado) o calcularla con la ley de Hess a partir de datos tabulados (rápida, sin riesgo, con la incertidumbre de los datos).
- 🎯 **Por qué importa:** Cualquier combustible, de una hoguera a un cohete, libera energía porque los productos están en un estado más estable que los reactivos. ¿Cuánta energía por kilogramo?

📘 **Dónde se aprende** (1 clase): [B06-C12 · Termoquímica y energía de reacción](../programa/clases/B06/B06-C12-termoquimica-y-energia-de-reaccion/CLASE.md).

### Ley de Hick–Hyman

- La ley de Hick–Hyman da el tiempo de elección `TR = c + d·log₂(n + 1)` para `n` opciones equiprobables.

🎯 **Por qué importa (clase B111-C01):** Una interfaz mal diseñada convierte a una tripulación competente en una fuente de errores. La decisión central: ¿qué parte del tiempo y del error es del diseño y no de la persona?

📘 **Dónde se aprende** (1 clase): [B111-C01 · Fundamentos de factores humanos en operaciones espaciales](../programa/clases/B111/B111-C01-fundamentos-de-factores-humanos-en-operaciones-espaciales/CLASE.md).

### Ley de Hooke generalizada

- La ley de Hooke generalizada es `ε = [(1+ν)σ − ν tr(σ) I]/E`.

🎯 **Por qué importa (clase B84-C22):** Una tensión de 120 MPa en una dirección no dice si la pieza cede: la fluencia depende de la combinación de las seis componentes. La decisión central: ¿cede el material en este punto y con qué margen, dado un estado de tensión 3D?

📘 **Dónde se aprende** (1 clase): [B84-C22 · Tensión, deformación y elasticidad lineal](../programa/clases/B84/B84-C22-tension-deformacion-y-elasticidad-lineal/CLASE.md).

### Ley de Hubble

- La ley de Hubble es `v = H₀·d` para objetos que siguen la expansión.

💡 **Cómo se explica en la clase [B01-C16](../programa/clases/B01/B01-C16-expansion-del-universo-como-observacion/CLASE.md):**
- *Descripción textual:* de un corrimiento observado se infiere una velocidad aparente; con la ley de Hubble y un valor de `H₀` se obtiene la distancia; hay dos valores de `H₀` en conflicto, cada uno con su método; de `H₀` se obtiene también el tiempo de Hubble.
- 🎯 **Por qué importa:** En C01 «medimos» una distancia de 43 Mpc con `H₀ = 70`. Pero ese 70 no es un dato único: Planck 2018 da 67,4 ± 0,5 y SH0ES da 73,04 ± 1,04, ambos en km/s/Mpc (S1, S2).

📖 **Explicado a fondo:** [Ley de Hubble y constante H₀](esencial/tercera-f-t.md#ley-de-hubble-y-constante-h₀) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B01-C16 · Expansión del universo como observación](../programa/clases/B01/B01-C16-expansion-del-universo-como-observacion/CLASE.md).

### Ley de Hubble–Lemaître

- La ley de Hubble–Lemaître dice que la velocidad de recesión es proporcional a la distancia: `v = H₀ d`.

🎯 **Por qué importa (clase B26-C11):** `H₀` fija la escala de distancias del universo y su edad aproximada, y hoy su valor depende de cómo se mida (C23). Para entender esa discusión hay que saber ajustar la ley a datos con dispersión, cuándo vale `v = cz` y qué incertidumbre se arrastra.

📘 **Dónde se aprende** (1 clase): [B26-C11 · Expansión cósmica y ley de Hubble-Lemaître](../programa/clases/B26/B26-C11-expansion-cosmica-y-ley-de-hubble-lemaitre/CLASE.md).

### Ley de la reflexión

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C03):** Los espejos planos pliegan el haz de un telescopio y de un periscopio. La decisión central: ¿dónde está la imagen y cuánto gira el haz cuando se mueve el espejo?

📘 **Dónde se aprende** (1 clase): [B41-C03 · Reflexión y espejos planos](../programa/clases/B41/B41-C03-reflexion-y-espejos-planos/CLASE.md).

### Ley de Langmuir

- La ley de Langmuir da el flujo de masa `J = α P √(M/(2πRT))`, con `α = 1` como cota superior.

🎯 **Por qué importa (clase B84-C06):** Un recubrimiento de cadmio o de zinc que es inocuo en tierra puede desaparecer y contaminar ópticas en el vacío; un cálculo de un minuto lo descarta. La decisión central: ¿qué metales sobreviven sin protección al vacío a la temperatura de trabajo y cuáles se subliman?

📘 **Dónde se aprende** (1 clase): [B84-C06 · Comportamiento bajo vacío](../programa/clases/B84/B84-C06-comportamiento-bajo-vacio/CLASE.md).

### Ley de los gases ideales

- La ley de los gases ideales relaciona la presión `P`, el volumen `V`, la cantidad de sustancia `n` y la temperatura absoluta `T`: `PV = nRT`, con `R` la constante molar de los gases.

💡 **Cómo se explica en la clase [B06-C09](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md):**
- La ley de los gases ideales reproduce la cifra publicada con una sola línea de cálculo.
- 🎯 **Por qué importa:** La NASA publica para Marte, Venus y la Tierra la presión y la temperatura medias en la superficie, la gravedad, el peso molecular de la atmósfera y su densidad (S1, S2, S3). ¿Puedes reproducir esa densidad con sólo lo anterior?

📘 **Dónde se aprende** (1 clase): [B06-C09 · Gases ideales y no ideales](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md).

### Ley de Malus

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B42-C08):** La polarización cambia cuánto flujo pasa por un instrumento (espejos, divisores, filtros) y revela procesos físicos de la fuente. La decisión central: ¿cómo se describe y se mide un estado de polarización y cómo lo transforma un elemento óptico?

📘 **Dónde se aprende** (1 clase): [B42-C08 · Polarización de la luz](../programa/clases/B42/B42-C08-polarizacion-de-la-luz/CLASE.md).

### Ley de masa

- La ley de masa dice que `TL` sube `6 dB` al duplicar la masa o la frecuencia.

💡 **Cómo se explica en la clase [B109-C09](../programa/clases/B109/B109-C09-privacidad-y-espacios-personales/CLASE.md):**
- Límite: la ley de masa ignora la rigidez, las fugas por rendijas y los puentes por estructura, que en divisiones ligeras dominan.
- 🎯 **Por qué importa:** Una división que no se ve a través pero que deja pasar cada palabra no da privacidad. La decisión central: ¿qué masa debe tener una división para que lo que se dice al otro lado quede por debajo del ruido de fondo?

📘 **Dónde se aprende** (1 clase): [B109-C09 · Privacidad y espacios personales](../programa/clases/B109/B109-C09-privacidad-y-espacios-personales/CLASE.md).

### Ley de Ohm

- La resistencia `R` (ohmios, Ω) mide la oposición al paso de corriente; la ley de Ohm dice `V = I R` para un conductor óhmico.

🎯 **Por qué importa (clase B05-C16):** Un satélite recibe energía del Sol mediante paneles, la guarda en baterías y la reparte a equipos; si el cálculo está mal, la nave se apaga en el eclipse. La pregunta motivadora es: ¿cómo calcular corrientes, tensiones y potencias en una red de componentes y cuánta energía debe guardarse para pasar un eclipse?

📘 **Dónde se aprende** (1 clase): [B05-C16 · Corriente y circuitos elementales](../programa/clases/B05/B05-C16-corriente-y-circuitos-elementales/CLASE.md).

### Ley de Paris

- La ley de Paris es `da/dN = C (ΔK)^m`.

🎯 **Por qué importa (clase B84-C08):** La mayoría de las fallas estructurales en servicio son por fatiga; saber cuántos ciclos quedan y qué grieta es tolerable decide si una pieza se acepta. La decisión central: ¿cuántos ciclos tarda una grieta inicial en llegar al tamaño crítico y cuánto daño acumula un espectro de cargas?

📘 **Dónde se aprende** (1 clase): [B84-C08 · Fatiga y fractura](../programa/clases/B84/B84-C08-fatiga-y-fractura/CLASE.md).

### Ley de Planck

- La ley de Planck `B_λ(T)`.

💡 **Cómo se explica en la clase [B47-C04](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md):**
- *Descripción textual:* la ley de Planck se verifica con dos relaciones y se usa para el fondo térmico y la temperatura de operación.
- 🎯 **Por qué importa:** Enfriar un telescopio cuesta masa, potencia y complejidad. La decisión central: ¿a qué temperatura el fondo propio deja de dominar sobre el detector?

📘 **Dónde se aprende** (1 clase): [B47-C04 · Telescopios infrarrojos](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md).

### Ley de potencias

- La ley de potencias describe el número de eventos con cada tamaño.
- Una ley de potencias es `y ∝ r^p`.
- Una ley de potencias acumulada es `N(>D) ∝ D^(−q)`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B30-C12](../programa/clases/B30/B30-C12-erupciones-y-fulguraciones-solares/CLASE.md):**
- Como los terremotos: hay muchos pequeños y pocos grandes, y la razón entre ellos sigue una ley de potencias; la escala de clases va por potencias de diez.
- LP["ley de potencias"] --> MLE["α̂ por máxima verosimilitud"]
- 🎯 **Por qué importa:** Para alertar de una erupción hay que saber qué magnitud tiene, con qué frecuencia ocurren eventos grandes y cuánta energía liberan. La decisión central: ¿cómo se clasifica una fulguración y qué dice una ley de potencias sobre la frecuencia de las grandes?

📘 **Dónde se aprende** (5 clases): [B30-C12 · Erupciones y fulguraciones solares](../programa/clases/B30/B30-C12-erupciones-y-fulguraciones-solares/CLASE.md); [B34-C01 · Calentamiento coronal: mecanismos y evidencias](../programa/clases/B34/B34-C01-calentamiento-coronal-mecanismos-y-evidencias/CLASE.md); [B52-C02 · Discos protoplanetarios](../programa/clases/B52/B52-C02-discos-protoplanetarios/CLASE.md); [B52-C13 · Pequeños cuerpos remanentes](../programa/clases/B52/B52-C13-pequenos-cuerpos-remanentes/CLASE.md); [B55-C05 · Granos de polvo interestelar](../programa/clases/B55/B55-C05-granos-de-polvo-interestelar/CLASE.md).

### Ley de potencias de tamaños

- La ley de potencias de tamaños describe cuántos fragmentos hay por encima de un diámetro.

🎯 **Por qué importa (clase B118-C09):** La directriz 5 de la COPUOS dice que la mayor parte de los desechos catalogados proviene de fragmentaciones; entender cuántos fragmentos produce un evento y de qué tamaño es la base de los escenarios futuros. La decisión central: ¿cuántos fragmentos relevantes genera un evento y cuándo es «catastrófico»?

📘 **Dónde se aprende** (1 clase): [B118-C09 · Generación de desechos](../programa/clases/B118/B118-C09-generacion-de-desechos/CLASE.md).

### Ley de práctica

- La ley de práctica dice que el tiempo baja como una potencia del número de repeticiones.

🎯 **Por qué importa (clase B104-C06):** Los procedimientos se practican en tierra y a veces se usan meses después, en el momento crítico. La decisión central: ¿cuándo repasar para que el procedimiento siga disponible sin gastar tiempo de entrenamiento de más?

📘 **Dónde se aprende** (1 clase): [B104-C06 · Entrenamiento de procedimientos](../programa/clases/B104/B104-C06-entrenamiento-de-procedimientos/CLASE.md).

### Ley de presión-hundimiento

- La ley de presión-hundimiento de Bekker es `p = k z^n`.

🎯 **Por qué importa (clase B102-C02):** La tracción de un rover en regolito no sale de un coeficiente de rozamiento único. La decisión central: ¿cuánta fuerza neta de empuje queda para tirar del vehículo, una vez descontada la resistencia que crea el propio hundimiento, y cómo depende del patinaje y de la gravedad?

📘 **Dónde se aprende** (1 clase): [B102-C02 · Terramecánica: tracción y hundimiento en suelos sueltos](../programa/clases/B102/B102-C02-terramecanica-traccion-y-hundimiento-en-suelos-sueltos/CLASE.md).

### Ley de Preston

- La ley de Preston `dZ/dt = k_P P v`.

🎯 **Por qué importa (clase B43-C05):** Pulir es controlar un retiro de décimas de micrón: sin un modelo se oscila entre sobrecorregir y subcorregir. La decisión central: ¿cuánto hay que retirar de la mejor esfera para obtener un paraboloide y cuánto tiempo debe permanecer la herramienta en cada zona?

📘 **Dónde se aprende** (1 clase): [B43-C05 · Pulido óptico](../programa/clases/B43/B43-C05-pulido-optico/CLASE.md).

### Ley de propagación de la incertidumbre

- La ley de propagación de la incertidumbre da la incertidumbre combinada: `u_c²(y) = Σᵢ (∂f/∂xᵢ)² u²(xᵢ)` para entradas independientes (S1, 5.1.2, ecuación 10); con entradas correlacionadas se añade el término `2 ΣΣ (∂f/∂xᵢ)(∂f/∂xⱼ) u(xᵢ, xⱼ)` (S1, 5.2.2, ecuación 13).

🎯 **Por qué importa (clase B12-C16):** Casi todo resultado en ciencias espaciales es una función de medidas: una velocidad a partir de un radio, una distancia a partir de una paralaje, una masa a partir de un período. Dar el valor sin su incertidumbre no permite comparar con otros resultados ni decidir si cumple un requisito.

📘 **Dónde se aprende** (1 clase): [B12-C16 · Propagación de incertidumbre](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md).

### Ley de proyección

- La ley de proyección `m = (B × τ_d)/|B|²` lo logra.

💡 **Cómo se explica en la clase [B87-C12](../programa/clases/B87/B87-C12-magnetopares/CLASE.md):**
- Ley de proyección (esta clase): par deseado instantáneo.
- 🎯 **Por qué importa:** Los magnetopares descargan ruedas (C14) y hacen detumbling (C16) con muy poca masa. La decisión central: ¿qué par se puede generar en cada instante, qué dirección queda inaccesible y basta una órbita para cubrir los tres ejes?

📘 **Dónde se aprende** (1 clase): [B87-C12 · Magnetopares](../programa/clases/B87/B87-C12-magnetopares/CLASE.md).

### Ley de Schmidt

- La ley de Schmidt es `Σ_SFR ∝ Σ_gas^N`.
- La ley de Schmidt `ψ = ε M_g/t_ff`.

💡 **Cómo se explica en la clase [B25-C05](../programa/clases/B25/B25-C05-regiones-de-formacion-estelar/CLASE.md):**
- *Descripción textual:* el radio sale de igualar fotones emitidos con recombinaciones en el volumen; por otro lado, la ley de Schmidt da el ritmo de formación y de él el tiempo de agotamiento.
- Ley de Schmidt global (S1): relaciona promedios de disco; no resuelve nubes.
- 🎯 **Por qué importa:** Una galaxia no convierte todo su gas en estrellas a la vez: lo hace a un ritmo que puede medirse y comparar. Entender las regiones donde nacen las estrellas masivas permite reconocerlas desde lejos, y entender la relación entre gas y ritmo de formación permite saber cuánto tiempo puede una galaxia seguir formando estrellas.

📘 **Dónde se aprende** (2 clases): [B25-C05 · Regiones de formación estelar](../programa/clases/B25/B25-C05-regiones-de-formacion-estelar/CLASE.md); [B38-C07 · Modelos submalla de formación estelar y retroalimentación](../programa/clases/B38/B38-C07-modelos-submalla-de-formacion-estelar-y-retroalimentacion/CLASE.md).

### Ley de senos

- En un triángulo plano con lados `a, b, c` y ángulos opuestos `A, B, C`, la ley de cosenos dice `c² = a² + b² − 2ab cos C`; la ley de senos dice `a/sen A = b/sen B = c/sen C`.

💡 **Cómo se explica en la clase [B04-C08](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md):**
- Es un caso particular de la ley de senos con un ángulo de 90°.
- B -->|"ALA"| D["Tercer ángulo = 180° − A − B; luego ley de senos"]
- ⚠️ **Error frecuente:** Usar la ley de senos con LAL. Se corrige con la sección 8.1 y el ejercicio 1.
- 🎯 **Por qué importa:** Cuando una sonda se comunica con la Tierra, el tiempo de la señal depende de la distancia, que cambia de unos 55 millones de km a unos 400 millones según dónde estén ambos planetas en sus órbitas.

📘 **Dónde se aprende** (1 clase): [B04-C08 · Ley de senos y ley de cosenos](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md).

### Ley de Snell

- La refracción cambia su dirección al pasar de un medio a otro, según la ley de Snell `n₁ sen θ₁ = n₂ sen θ₂` (ángulos medidos respecto de la normal).

💡 **Cómo se explica en la clase [B41-C02](../programa/clases/B41/B41-C02-indice-de-refraccion-y-ley-de-snell/CLASE.md):**
- *Descripción textual:* la ley de Snell fija el ángulo y los coeficientes de Fresnel el reparto de energía.
- 🎯 **Por qué importa:** Un telescopio refractor y los recubrimientos dependen de cuánta luz se refleja y a qué ángulo se dobla. La decisión central: ¿qué fracción de luz se pierde por reflexión y cuándo hay reflexión total?

📘 **Dónde se aprende** (2 clases): [B05-C19 · Óptica y velocidad de la luz](../programa/clases/B05/B05-C19-optica-y-velocidad-de-la-luz/CLASE.md); [B41-C02 · Índice de refracción y ley de Snell](../programa/clases/B41/B41-C02-indice-de-refraccion-y-ley-de-snell/CLASE.md).

### Ley de Stefan–Boltzmann

- La ley de Stefan–Boltzmann `j = εσT⁴` da la potencia radiada por unidad de superficie de un cuerpo de emisividad `ε`.

💡 **Cómo se explica en la clase [B13-C16](../programa/clases/B13/B13-C16-calibracion-termica/CLASE.md):**
- ⚠️ **Error frecuente:** Usar grados Celsius en la ley de Stefan–Boltzmann. Se corrige en el ejercicio 4 (usa kelvin).
- 🎯 **Por qué importa:** Un sensor de temperatura pegado a un panel de una nave devuelve una resistencia. Convertirla en kelvin exige calibrarlo contra referencias conocidas, y comprobar que la temperatura medida concuerda con un balance térmico previsto.

📘 **Dónde se aprende** (2 clases): [B13-C16 · Calibración térmica](../programa/clases/B13/B13-C16-calibracion-termica/CLASE.md); [B47-C04 · Telescopios infrarrojos](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md).

### Ley de Stokes

- La ley de Stokes `w_s = (ρ_p − ρ) g D²/(18 μ)` vale para Reynolds bajo.

🎯 **Por qué importa (clase B66-C05):** Los deltas marcianos se interpretan como archivo de ambientes pasados, pero un grano cae más despacio con menos gravedad y el mismo flujo puede dejar otra facies. La decisión central: ¿cómo cambia la facies que deja un flujo cuando cambia la gravedad?

📘 **Dónde se aprende** (1 clase): [B66-C05 · Depósitos sedimentarios y sedimentología planetaria](../programa/clases/B66/B66-C05-depositos-sedimentarios-y-sedimentologia-planetaria/CLASE.md).

### Ley de Wien

- La ley de Wien relaciona la longitud de onda del máximo con la temperatura, `λ_max·T = b`.
- La ley de Wien dice que el máximo de `L_λ` está en `λ_max = b/T`, con `b = hc/(k x)` y `x` la solución de `x = 5(1 − e⁻ˣ)`.
- La ley de Wien liga la temperatura de un cuerpo negro con la longitud de onda del máximo: `λ_max T = b`, con `b = 2,897 771 955 × 10⁻³ m·K` (S1).
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

🎯 **Por qué importa (clase B01-C09):** Sobre una galaxia a 43 Mpc solo tienes luz. De esa luz sale su dirección, cuánto brilla, de qué color es y qué líneas aparecen en su espectro; de las líneas sale `z = 0,0101` (C01).

📘 **Dónde se aprende** (7 clases): [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B13-C17 · Calibración radiométrica](../programa/clases/B13/B13-C17-calibracion-radiometrica/CLASE.md); [B24-C10 · Espectros y clasificación estelar](../programa/clases/B24/B24-C10-espectros-y-clasificacion-estelar/CLASE.md); [B28-C02 · Fotones en múltiples longitudes de onda](../programa/clases/B28/B28-C02-fotones-en-multiples-longitudes-de-onda/CLASE.md); [B45-C13 · Temperatura y espectro de cuerpo negro](../programa/clases/B45/B45-C13-temperatura-y-espectro-de-cuerpo-negro/CLASE.md); [B47-C04 · Telescopios infrarrojos](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md) y 1 más.

### Ley del coseno

- La ley del coseno dice que una celda de normal `n` da `I = I₀ max(0, n·s)`.

💡 **Cómo se explica en la clase [B87-C03](../programa/clases/B87/B87-C03-sensores-solares/CLASE.md):**
- Celdas sueltas con ley del coseno (esta clase).
- 🎯 **Por qué importa:** Un satélite que sale de un eclipse o de un modo seguro necesita saber hacia dónde está el Sol para orientar sus paneles. La decisión central: ¿con qué precisión angular se obtiene el vector solar de las corrientes de las fotoceldas y cuánto ruido tolera el diseño?

📘 **Dónde se aprende** (1 clase): [B87-C03 · Sensores solares](../programa/clases/B87/B87-C03-sensores-solares/CLASE.md).

### Ley del cuadrado inverso

- La ley del cuadrado inverso es la dependencia `1/r²`.

🎯 **Por qué importa (clase B05-C10):** La misma fuerza que hace caer una manzana mantiene a la Luna en órbita: esa idea unificó el cielo y la Tierra. La pregunta motivadora es: ¿cómo comprobar con números que la gravedad de la superficie y la órbita de la Luna son la misma fuerza?

📘 **Dónde se aprende** (1 clase): [B05-C10 · Gravitación universal](../programa/clases/B05/B05-C10-gravitacion-universal/CLASE.md).

### Ley del inverso del cuadrado

- La ley del inverso del cuadrado dice que una cantidad es proporcional a `1/d²`.
- Una ley del inverso del cuadrado decae como `1/r²`.

🎯 **Por qué importa (clase B02-C15):** Una ley que describe es útil; una ley que explica unifica. La pregunta motivadora es: ¿es la misma fuerza la que hace caer una piedra y la que mantiene a la Luna en órbita?

📘 **Dónde se aprende** (2 clases): [B02-C15 · Newton y gravitación universal](../programa/clases/B02/B02-C15-newton-y-gravitacion-universal/CLASE.md); [B03-C10 · Proporcionalidad directa e inversa](../programa/clases/B03/B03-C10-proporcionalidad-directa-e-inversa/CLASE.md).

### Ley empírica

- Una ley empírica resume lo observado sin explicarlo (C15 da la explicación).

🎯 **Por qué importa (clase B02-C14):** Para Kepler, como para todos antes, el círculo era la figura natural del cielo. Los datos de Tycho no se dejaban describir con círculos.

📘 **Dónde se aprende** (1 clase): [B02-C14 · Kepler y reconstrucción de órbitas](../programa/clases/B02/B02-C14-kepler-y-reconstruccion-de-orbitas/CLASE.md).

### Ley PD en cuaterniones

- La ley PD en cuaterniones (Wie) es `τ = −K_p sgn(q_{e,w}) q_{e,v} − K_d ω`.

🎯 **Por qué importa (clase B87-C17):** Es el lazo central del subsistema de actitud. La decisión central: ¿cómo se eligen las ganancias para un tiempo de asentamiento dado, cómo se evita el camino largo (el cuaternión doble) y qué pasa cuando el par se satura?

📘 **Dónde se aprende** (1 clase): [B87-C17 · Control de tres ejes](../programa/clases/B87/B87-C17-control-de-tres-ejes/CLASE.md).

### Ley saturante

- La ley saturante `α(ESH) = α₀ + Δα_max (1 − e^(−ESH/E₀))`.

💡 **Cómo se explica en la clase [B85-C14](../programa/clases/B85/B85-C14-degradacion-ultravioleta/CLASE.md):**
- *Descripción textual:* los datos sintéticos permiten ajustar los parámetros de la ley saturante; con ella se extrapola `α` y se calcula la temperatura al final de la misión.
- 🎯 **Por qué importa:** Un recubrimiento que cumple al inicio puede salirse del intervalo con la exposición. La decisión central: ¿cuánto sube `α` y cuánto sube la temperatura al final de la misión, y qué incertidumbre trae el ajuste?

📘 **Dónde se aprende** (1 clase): [B85-C14 · Degradación ultravioleta](../programa/clases/B85/B85-C14-degradacion-ultravioleta/CLASE.md).

### Leyenda

- Una leyenda nombra cada serie.

💡 **Cómo se explica en la clase [B07-C10](../programa/clases/B07/B07-C10-graficos-bidimensionales-iniciales/CLASE.md):**
- También rotula la procedencia: la leyenda dice «datos NASA NSSDC (publicados)» para la serie de puntos y «ajuste» para la recta.
- *Descripción textual:* los datos (dos arreglos) se dibujan sobre unos ejes que llevan escala, etiquetas y unidades; los ejes forman parte de una figura con título y leyenda, que se guarda como imagen acompañada de una descripción en texto.
- 🎯 **Por qué importa:** Un gráfico es una afirmación: dice «mira esta relación». Un gráfico sin unidades, con una escala que esconde la mitad de los datos o sin leyenda puede inducir a error aunque los números sean correctos.

📘 **Dónde se aprende** (1 clase): [B07-C10 · Gráficos bidimensionales iniciales](../programa/clases/B07/B07-C10-graficos-bidimensionales-iniciales/CLASE.md).

### Leyes de Kirchhoff

- Las leyes de Kirchhoff: en un nodo, la suma de corrientes que entran es igual a la que sale; en un lazo cerrado, la suma de tensiones es cero.

🎯 **Por qué importa (clase B05-C16):** Un satélite recibe energía del Sol mediante paneles, la guarda en baterías y la reparte a equipos; si el cálculo está mal, la nave se apaga en el eclipse. La pregunta motivadora es: ¿cómo calcular corrientes, tensiones y potencias en una red de componentes y cuánta energía debe guardarse para pasar un eclipse?

📘 **Dónde se aprende** (1 clase): [B05-C16 · Corriente y circuitos elementales](../programa/clases/B05/B05-C16-corriente-y-circuitos-elementales/CLASE.md).

### Libra

- El argumento resonante es el ángulo `φ = pλ₂ − qλ₁ − …` y libra si oscila alrededor de un valor.

💡 **Cómo se explica en la clase [B73-C10](../programa/clases/B73/B73-C10-resonancias-de-movimiento-medio/CLASE.md):**
- Por argumento resonante: libra o circula.
- 🎯 **Por qué importa:** Una razón de periodos cercana a un número racional es el primer indicio de una resonancia, pero puede engañar si la fuente usa periodos instantáneos en lugar de medios. La decisión central: ¿qué periodos puedo usar para afirmar que hay una resonancia y qué puedo y no puedo concluir?

📘 **Dónde se aprende** (1 clase): [B73-C10 · Resonancias de movimiento medio](../programa/clases/B73/B73-C10-resonancias-de-movimiento-medio/CLASE.md).

### Libración

- La rotación sincrónica es que la Luna gira sobre su eje una vez por cada vuelta alrededor de la Tierra, por lo que muestra siempre la misma cara; la libración son pequeños balanceos que dejan ver algo más de la mitad (S3).

💡 **Cómo se explica en la clase [B08-C08](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md):**
- Esos balanceos (libración) permiten ver unos grados más allá del borde y explican que se vea «un poco más de la mitad» de la superficie (S3).
- 🎯 **Por qué importa:** La Luna es el primer blanco de cualquier observación y el principal enemigo de las observaciones de objetos débiles (C12). Saber su fase y cuándo está en el cielo es parte de toda planificación.

📘 **Dónde se aprende** (1 clase): [B08-C08 · Fases lunares y libración](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md).

### Libre

- Un índice mudo (repetido) puede renombrarse; un índice libre aparece una vez por término y define la componente.

🎯 **Por qué importa (clase B10-C17):** La inercia de un satélite frente a un giro depende de la dirección: se necesita nueve números ordenados en una matriz, y esos nueve números cambian si cambias los ejes del cuerpo, pero de forma que la física no cambie.

📘 **Dónde se aprende** (1 clase): [B10-C17 · Tensores y notación indicial](../programa/clases/B10/B10-C17-tensores-y-notacion-indicial/CLASE.md).

### Libro de energía

- El libro de energía lista cada partida y su fracción.

💡 **Cómo se explica en la clase [B59-C20](../programa/clases/B59/B59-C20-diseno-conceptual-de-planta-isru/CLASE.md):**
- Balance de masa y libro de energía son verificaciones independientes: uno comprueba la materia y el otro cierra las partidas.
- 🎯 **Por qué importa:** Un diseño conceptual no es un número sino un conjunto coherente. La decisión central: ¿qué potencia y qué masa necesita una planta que produce 10 t de agua al año, y qué parámetro la gobierna?

📘 **Dónde se aprende** (1 clase): [B59-C20 · Diseño conceptual de planta ISRU](../programa/clases/B59/B59-C20-diseno-conceptual-de-planta-isru/CLASE.md).

### Licencia

- La licencia es la autorización estatal previa.
- La licencia es la autorización de la autoridad.
- Una licencia define qué usos se permiten.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C19](../programa/clases/B14/B14-C19-publicacion-de-codigo-y-datos/CLASE.md):**
- Un nombre inventado («mi propia licencia») no es un identificador SPDX y la regla lo rechaza.
- Esta clase no da asesoría legal: la elección de licencia depende de tus compromisos con instituciones y financiadores.
- ⚠️ **Error frecuente:** Publicar sin licencia. Se corrige con los ejercicios 1 y 2.
- 🎯 **Por qué importa:** Subes tu código a un repositorio y tus datos a una carpeta compartida. Un año después, alguien quiere usarlos y no sabe si puede, cómo citarte, qué significan las columnas ni si el archivo es el que tú usaste.

📘 **Dónde se aprende** (4 clases): [B14-C19 · Publicación de código y datos](../programa/clases/B14/B14-C19-publicacion-de-codigo-y-datos/CLASE.md); [B121-C01 · Licencias y requisitos nacionales para el lanzamiento](../programa/clases/B121/B121-C01-licencias-y-requisitos-nacionales-para-el-lanzamiento/CLASE.md); [B124-C09 · Propiedad intelectual y licencias](../programa/clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md); [B125-C05 · Control de exportaciones y transferencia de tecnología](../programa/clases/B125/B125-C05-control-de-exportaciones-y-transferencia-de-tecnologia/CLASE.md).

### Lidera quien lo porta

- Una actividad de saber presenta un saber de la comunidad y la lidera quien lo porta.

🎯 **Por qué importa (clase B133-C05):** Enseñar «con» una cultura es más que añadir una diapositiva: exige repartir roles, acordar protocolos y medir bien. La decisión central: ¿cómo se organiza una unidad para que el saber lo presente quien lo porta y la ciencia se enseñe con rigor, en el mismo hilo?

📘 **Dónde se aprende** (1 clase): [B133-C05 · Diseño de una unidad de enseñanza intercultural](../programa/clases/B133/B133-C05-diseno-de-una-unidad-de-ensenanza-intercultural/CLASE.md).

### Ligada

- Una partícula está ligada a una galaxia si su energía relativa a ella es negativa.
- Una órbita ligada se cierra; una no ligada (parabólica o hiperbólica) no.

💡 **Cómo se explica en la clase [B04-C18](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md):**
- B -. "ligada: se cierra" .-> E["Vuelve"]
- 🎯 **Por qué importa:** En 2017 se descubrió un objeto que cruzaba el sistema solar con una órbita que no se cerraba: su excentricidad era mayor que 1. Eso significó que no estaba ligado al Sol: venía de fuera y se iba.

📘 **Dónde se aprende** (2 clases): [B04-C18 · Cónicas y secciones orbitales](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md); [B25-C12 · Interacciones y fusiones galácticas](../programa/clases/B25/B25-C12-interacciones-y-fusiones-galacticas/CLASE.md).

### Ligadura hamiltoniana

- La ligadura hamiltoniana es `R³ + K² − K_ij K^ij = 16πρ`.

💡 **Cómo se explica en la clase [B39-C06](../programa/clases/B39/B39-C06-introduccion-a-la-relatividad-numerica-formalismo-3-1/CLASE.md):**
- En Painlevé–Gullstrand a `r = 4M`, `α = 1`, `β^r = √(2M/r) = 0,707107`, la traza de `K` vale `0,265165` y la ligadura hamiltoniana `−1,2 × 10⁻⁸`.
- 🎯 **Por qué importa:** Una simulación necesita un tiempo y un espacio. La decisión central: ¿cómo se separa el espacio-tiempo en capas y cómo se sabe que una evolución converge?

📘 **Dónde se aprende** (1 clase): [B39-C06 · Introducción a la relatividad numérica: formalismo 3+1](../programa/clases/B39/B39-C06-introduccion-a-la-relatividad-numerica-formalismo-3-1/CLASE.md).

### Limbo

- El limbo es el borde visible del disco.
- El limbo es el borde del disco solar, de semidiámetro `0,2667°`.

💡 **Cómo se explica en la clase [B74-C25](../programa/clases/B74/B74-C25-deteccion-de-limbo-y-bordes-planetarios-en-imagenes-de-navegacion/CLASE.md):**
- Con 180 puntos de limbo el ajuste es muy preciso.
- Límite: el disco sintético es perfectamente circular y sin relieve ni atmósfera; el limbo real de un cuerpo con atmósfera o relieve tiene sesgos que requieren un modelo.
- 🎯 **Por qué importa:** En un disco iluminado a medias, el borde oscuro no existe y un ajuste ingenuo se sesga. La decisión central: ¿qué parte del limbo es utilizable, con qué incertidumbre, y qué sesgo introduce la fase?

📘 **Dónde se aprende** (2 clases): [B74-C25 · Detección de limbo y bordes planetarios en imágenes de navegación](../programa/clases/B74/B74-C25-deteccion-de-limbo-y-bordes-planetarios-en-imagenes-de-navegacion/CLASE.md); [B132-C02 · Arqueología de observatorios y de instrumentos antiguos](../programa/clases/B132/B132-C02-arqueologia-de-observatorios-y-de-instrumentos-antiguos/CLASE.md).

### Limitación

- Una limitación es algo que no se probó.

🎯 **Por qué importa (clase B23-C08):** Un conjunto de pruebas que pasan no es un informe. Quien debe decidir si usar el código necesita saber para qué uso se evaluó, con qué criterios, qué falló y qué no se probó.

📘 **Dónde se aprende** (1 clase): [B23-C08 · Informe de verificación y validación](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md).

### Limitada por CPU

- Una tarea limitada por CPU gasta su tiempo calculando; una limitada por E/S lo gasta esperando (disco, red, espera simulada).

🎯 **Por qué importa (clase B18-C01):** Tienes ocho órbitas simuladas que propagar y un portátil con varios núcleos. La tentación es «lanzar ocho hilos y listo».

📘 **Dónde se aprende** (1 clase): [B18-C01 · Procesos, hilos y concurrencia](../programa/clases/B18/B18-C01-procesos-hilos-y-concurrencia/CLASE.md).

### Limitada por E/S

- Una tarea limitada por CPU gasta su tiempo calculando; una limitada por E/S lo gasta esperando (disco, red, espera simulada).

🎯 **Por qué importa (clase B18-C01):** Tienes ocho órbitas simuladas que propagar y un portátil con varios núcleos. La tentación es «lanzar ocho hilos y listo».

📘 **Dónde se aprende** (1 clase): [B18-C01 · Procesos, hilos y concurrencia](../programa/clases/B18/B18-C01-procesos-hilos-y-concurrencia/CLASE.md).

### Limitada por memoria

- Una tarea limitada por memoria es aquella cuyo tiempo lo fija el ancho de banda y no la aritmética.

💡 **Cómo se explica en la clase [B18-C03](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md):**
- Cuando la intensidad es así de baja, la tarea está limitada por memoria y optimizar la aritmética no ayuda.
- 🎯 **Por qué importa:** Un catálogo con millones de estrellas o una rejilla de simulación pasan cada dato por la CPU una o pocas veces. Cuando las operaciones por dato son pocas, el tiempo no lo fija la CPU sino el viaje de los datos.

📘 **Dónde se aprende** (1 clase): [B18-C03 · Jerarquía y estructuras de memoria](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md).

### Limitado por el cielo

- Suma de flujos: los brillos se suman como flujos. Limitado por el cielo: ruido dominado por el fondo.

🎯 **Por qué importa (clase B48-C18):** Cada fracción de magnitud perdida se paga en tiempo de telescopio. La decisión central: ¿cuánto cuesta en exposición una contaminación luminosa dada?

📘 **Dónde se aprende** (1 clase): [B48-C18 · Protección del cielo oscuro](../programa/clases/B48/B48-C18-proteccion-del-cielo-oscuro/CLASE.md).

### Limitado por potencia

- Un propulsor limitado por potencia da un empuje que depende solo de `P` y `Vₑ`.

🎯 **Por qué importa (clase B78-C06):** Subir el `Isp` ahorra propelente, pero el mismo vatio produce menos empuje y la maniobra tarda más. La decisión central: ¿cuánto empuje da cada kilovatio, cómo cae con el `Isp` y qué pasa con el tiempo de maniobra?

📘 **Dónde se aprende** (1 clase): [B78-C06 · Propulsión eléctrica general](../programa/clases/B78/B78-C06-propulsion-electrica-general/CLASE.md).

### Limitador de corriente

- Un limitador de corriente electrónico cumple la misma función con un umbral y un retardo.

🎯 **Por qué importa (clase B86-C10):** Si el fusible aguas arriba se funde antes que el de la rama averiada, un fallo local deja sin energía a toda la nave. Una protección bien coordinada aísla la rama y conserva el resto.

📘 **Dónde se aprende** (1 clase): [B86-C10 · Protección contra sobrecorriente](../programa/clases/B86/B86-C10-proteccion-contra-sobrecorriente/CLASE.md).

### Límite

- El límite de `f(x)` cuando `x` tiende a `a`, escrito `lim_{x→a} f(x) = L`, significa que `f(x)` se acerca a `L` tanto como se quiera al acercar `x` a `a`, sin importar el valor de `f` en `a` (S1).
- Un intervalo o límite define `lo` y `hi`: mínimo–máximo o por percentiles (el percentil `p` es el valor bajo el cual está `p`% de los datos).
- Una afirmación es lo que el artículo sostiene; la evidencia es lo que la apoya; el límite es lo que la evidencia no permite concluir.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C01](../programa/clases/B09/B09-C01-limites-de-funciones-reales/CLASE.md):**
- Si existen `lim f = L` y `lim g = M`: el límite de una suma, producto o cociente (con `M ≠ 0`) es la suma, el producto o el cociente de los límites (S1, §1.4(ii)).
- El límite matemático es correcto; la fórmula ingenua falla en la máquina.
- ⚠️ **Error frecuente:** Afirmar que el límite existe porque la tabla «se ve» estable. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** Los astrónomos miden distancias a estrellas cercanas por paralaje: un ángulo diminuto, de fracciones de segundo de arco. Con ángulos tan pequeños, `sin t`, `tan t` y `t` casi coinciden, y casi todos los cálculos prácticos los sustituyen.

📘 **Dónde se aprende** (7 clases): [B09-C01 · Límites de funciones reales](../programa/clases/B09/B09-C01-limites-de-funciones-reales/CLASE.md); [B15-C10 · Histogramas y normalización](../programa/clases/B15/B15-C10-histogramas-y-normalizacion/CLASE.md); [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md); [B90-C13 · Compatibilidad electromagnética EMC](../programa/clases/B90/B90-C13-compatibilidad-electromagnetica-emc/CLASE.md); [B96-C06 · Telemetría operativa](../programa/clases/B96/B96-C06-telemetria-operativa/CLASE.md); [B127-C04 · Exclusiones, deducibles y límites de pólizas](../programa/clases/B127/B127-C04-exclusiones-deducibles-y-limites-de-polizas/CLASE.md) y 1 más.

### Límite administrativo

- Un límite administrativo es un valor más estricto que se usa para cumplir el estándar.

💡 **Cómo se explica en la clase [B112-C06](../programa/clases/B112/B112-C06-modelos-de-riesgo-de-radiacion-para-misiones/CLASE.md):**
- National Academies (2021) indica que el nivel del 95 % es el percentil 97,5, que NASA usa un límite administrativo de 1 % de REID y que las misiones largas probablemente superen 600 mSv.
- 🎯 **Por qué importa:** Falta la clase de estimación de riesgo por misión. Es la que usa un planificador: suma dosis de cada tramo, la convierte en riesgo y decide si cabe dentro de un límite.

📘 **Dónde se aprende** (1 clase): [B112-C06 · Modelos de riesgo de radiación para misiones](../programa/clases/B112/B112-C06-modelos-de-riesgo-de-radiacion-para-misiones/CLASE.md).

### Límite capilar

- El límite capilar ocurre cuando la presión capilar máxima `2σ cosθ/r_eff` iguala las caídas de presión: `Q_max = (ΔP_cap − ΔP_g)/(F_l + F_v)`.

💡 **Cómo se explica en la clase [B85-C09](../programa/clases/B85/B85-C09-tubos-de-calor/CLASE.md):**
- *Descripción textual:* el fluido circula en lazo: evapora, viaja como vapor, condensa y vuelve por la mecha; el límite capilar iguala la presión capilar a las pérdidas.
- 🎯 **Por qué importa:** Un tubo de calor es un conductor térmico muy bueno pero tiene un límite de potencia que se descubre tarde: en un ensayo en tierra, o en vuelo con una carga mayor. La decisión central: ¿cuánto calor transporta como máximo un tubo y cuánto pierde en un ensayo con inclinación?

📘 **Dónde se aprende** (1 clase): [B85-C09 · Tubos de calor](../programa/clases/B85/B85-C09-tubos-de-calor/CLASE.md).

### Límite crítico

- El límite crítico `L_C` es el umbral que da 5 % de falsas alarmas con dosis nula; el límite de detección `L_D` es la dosis verdadera detectada con 95 % de probabilidad (formas de Currie, recordadas por el autor y no consultadas aquí).

💡 **Cómo se explica en la clase [B105-C07](../programa/clases/B105/B105-C07-dosimetria-personal/CLASE.md):**
- ⚠️ **Error frecuente:** Declarar «hay dosis» con `N − B` menor que `L_C`. Por debajo del límite crítico no se decide (8.3).
- 🎯 **Por qué importa:** Un número de dosis sin su incertidumbre no es utilizable: cerca del fondo, el dosímetro no distingue una dosis pequeña de cero. La decisión central: ¿desde qué dosis se puede afirmar que el dosímetro vio algo y con qué incertidumbre se informa?

📘 **Dónde se aprende** (1 clase): [B105-C07 · Dosimetría personal](../programa/clases/B105/B105-C07-dosimetria-personal/CLASE.md).

### Límite de campo débil

- El límite de campo débil supone `|Φ|/c² ≪ 1`.

🎯 **Por qué importa (clase B26-C09):** La luz de una estrella lejana que pasa cerca del Sol, o de una galaxia, se desvía: es la base de las lentes gravitacionales que miden masas de cúmulos (C18) y de las correcciones al seguimiento de naves en el espacio profundo.

📘 **Dónde se aprende** (1 clase): [B26-C09 · Relatividad general introductoria](../programa/clases/B26/B26-C09-relatividad-general-introductoria/CLASE.md).

### Límite de carrera

- El límite de carrera de 600 mSv y el de un evento de partículas solares (SPE) de 250 mSv son los citados en un resumen de la NASA.
- El límite de carrera de NASA se fija con un REID del 3 % al nivel del 95 % de confianza, que según el informe de National Academies (2021) corresponde al percentil 97,5 de la distribución de incertidumbre.

💡 **Cómo se explica en la clase [B105-C06](../programa/clases/B105/B105-C06-radiacion-ionizante-y-exposicion/CLASE.md):**
- Un resumen de la NASA indica un límite de carrera de 600 mSv basado en un riesgo de muerte inducida por exposición (REID) de 3 % con 95 % de confianza, y un límite de SPE de 250 mSv.
- La misión consume el 22,5 % del límite de carrera; con 0,75 mSv/día se alcanzan 600 mSv en 800 días (4,44 misiones de 180 días).
- 🎯 **Por qué importa:** La dosis no se «lee»: se calcula a partir de una dosis absorbida, de factores de calidad y de ponderación, y esos factores tienen incertidumbre. La decisión central: ¿qué fracción del límite de carrera consume una misión y con qué probabilidad lo supera una secuencia de misiones?

📘 **Dónde se aprende** (2 clases): [B105-C06 · Radiación ionizante y exposición](../programa/clases/B105/B105-C06-radiacion-ionizante-y-exposicion/CLASE.md); [B112-C06 · Modelos de riesgo de radiación para misiones](../programa/clases/B112/B112-C06-modelos-de-riesgo-de-radiacion-para-misiones/CLASE.md).

### Límite de Child–Langmuir

- El límite de Child–Langmuir es el máximo `j` que atraviesa el gap `d` sin que la carga espacial lo frene.

🎯 **Por qué importa (clase B78-C07):** La velocidad de escape iónica crece con la raíz de la tensión, pero la corriente que cabe en una rejilla está limitada por la carga espacial. La decisión central: ¿qué tensión y qué área de rejilla se necesitan para un empuje dado y qué fracción del propelente llega a ser ion?

📘 **Dónde se aprende** (1 clase): [B78-C07 · Motores iónicos](../programa/clases/B78/B78-C07-motores-ionicos/CLASE.md).

### Límite de detección

- El límite crítico `L_C` es el umbral que da 5 % de falsas alarmas con dosis nula; el límite de detección `L_D` es la dosis verdadera detectada con 95 % de probabilidad (formas de Currie, recordadas por el autor y no consultadas aquí).
- El límite de detección es la menor concentración que el ensayo distingue.
- El límite de detección `D_min = (3σ/a)^(1/b)`.

💡 **Cómo se explica en la clase [B85-C23](../programa/clases/B85/B85-C23-dosimetros-y-monitores-de-radiacion-a-bordo/CLASE.md):**
- El límite de detección a `3σ` es `D_min = (3 × 0,002/a)^(1/b) = 0,442 Gy`.
- *Descripción textual:* la dosis produce una señal con ruido; el ajuste da la calibración, el límite de detección y la inversa; el contador pierde cuentas por el tiempo muerto, que se corrige con la fórmula inversa.
- ⚠️ **Error frecuente:** Leer por debajo del límite de detección. no es distinguible del ruido (8.3)
- 🎯 **Por qué importa:** Un monitor mal calibrado no distingue una dosis real del ruido. La decisión central: ¿cuál es la relación señal–dosis, desde qué dosis es fiable y hasta qué tasa de cuentas se puede corregir el tiempo muerto?

📘 **Dónde se aprende** (4 clases): [B28-C08 · Señales transitorias](../programa/clases/B28/B28-C08-senales-transitorias/CLASE.md); [B85-C23 · Dosímetros y monitores de radiación a bordo](../programa/clases/B85/B85-C23-dosimetros-y-monitores-de-radiacion-a-bordo/CLASE.md); [B105-C07 · Dosimetría personal](../programa/clases/B105/B105-C07-dosimetria-personal/CLASE.md); [B115-C07 · Bioseguridad e inocuidad alimentaria en hábitats](../programa/clases/B115/B115-C07-bioseguridad-e-inocuidad-alimentaria-en-habitats/CLASE.md).

### Límite de difracción

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C20):** Un ranking depende de los pesos elegidos. La decisión central: ¿qué conclusión sobrevive cuando los pesos cambian?

📘 **Dónde se aprende** (1 clase): [B47-C20 · Caso comparativo de observatorios espaciales](../programa/clases/B47/B47-C20-caso-comparativo-de-observatorios-espaciales/CLASE.md).

### Límite de difracción de Rayleigh

- El límite de difracción de Rayleigh es `θ = 1,22 λ/D`.

🎯 **Por qué importa (clase B83-C01):** Un equipo sabe que quiere «mirar la costa» pero no cuánto debe resolver ni qué objetivo merece el presupuesto. La decisión central: ¿qué requisito de medición se deduce de la pregunta científica y qué objetivo conviene perseguir primero?

📘 **Dónde se aprende** (1 clase): [B83-C01 · Necesidad de misión y caso científico](../programa/clases/B83/B83-C01-necesidad-de-mision-y-caso-cientifico/CLASE.md).

### Límite de dosis

- El límite de dosis es un tope de misión sintético.

🎯 **Por qué importa (clase B75-C28):** Una trayectoria es también un perfil de exposición. La decisión central: ¿cuánta dosis acumula una nave por órbita y cuántas órbitas aguanta, según el periapsis y el blindaje?

📘 **Dónde se aprende** (1 clase): [B75-C28 · Restricciones de radiación en trayectorias](../programa/clases/B75/B75-C28-restricciones-de-radiacion-en-trayectorias/CLASE.md).

### Límite de flujo

- El límite de flujo es el brillo mínimo para entrar en él (`m ≤ m_lim`).

💡 **Cómo se explica en la clase [B25-C19](../programa/clases/B25/B25-C19-catalogos-y-sesgos-de-seleccion/CLASE.md):**
- Analogía: el alcance de la linterna es el límite de flujo.
- 🎯 **Por qué importa:** Un catálogo limitado por flujo ve las galaxias brillantes a gran distancia y casi solo ellas; si se promedian sus luminosidades sin cuidado, el resultado depende de la distancia del catálogo y no de las galaxias. Saber qué falta es tan importante como saber qué hay.

📘 **Dónde se aprende** (1 clase): [B25-C19 · Catálogos y sesgos de selección](../programa/clases/B25/B25-C19-catalogos-y-sesgos-de-seleccion/CLASE.md).

### Límite de Lyman

- El límite de Lyman es la longitud de onda umbral de ionización del hidrógeno desde `n = 1`.

🎯 **Por qué importa (clase B06-C18):** El hidrógeno de una nube o de una atmósfera puede ser ionizado por un fotón de longitud de onda menor que 91,2 nm. Un fotón de Lyman-alfa (121,6 nm) no lo ioniza desde el estado fundamental, pero tiene 22 veces la energía necesaria para evaporar una molécula de agua.

📘 **Dónde se aprende** (1 clase): [B06-C18 · Fotoquímica y radiación](../programa/clases/B06/B06-C18-fotoquimica-y-radiacion/CLASE.md).

### Límite de magnitud

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B38-C01):** Contar las estrellas que se ven no es contar las que hay: las brillantes se ven desde lejos y las débiles solo de cerca. La decisión central: ¿cómo corrijo la selección para recuperar la densidad real por intervalo de luminosidad?

📘 **Dónde se aprende** (1 clase): [B38-C01 · Funciones de luminosidad estelar](../programa/clases/B38/B38-C01-funciones-de-luminosidad-estelar/CLASE.md).

### Límite de Poisson

- El límite de Poisson a 90 % sin sucesos es `−ln 0,1 = 2,303`.

💡 **Cómo se explica en la clase [B36-C10](../programa/clases/B36/B36-C10-busqueda-directa-de-materia-oscura-en-laboratorio/CLASE.md):**
- *Descripción textual:* la cinemática del halo da el espectro y la tasa; con la exposición se obtiene el límite de Poisson.
- 🎯 **Por qué importa:** Un límite de sección eficaz depende de la cinemática, de la exposición y de las cuentas. La decisión central: ¿qué sección eficaz excluye una exposición sin sucesos?

📘 **Dónde se aprende** (1 clase): [B36-C10 · Búsqueda directa de materia oscura en laboratorio](../programa/clases/B36/B36-C10-busqueda-directa-de-materia-oscura-en-laboratorio/CLASE.md).

### Límite de Rayleigh

- El límite de Rayleigh estima ese mínimo como `θ = 1,22·λ/D`.

🎯 **Por qué importa (clase B01-C10):** Si el ojo bastara, no habría observatorios. La luz visible es una franja pequeña del espectro electromagnético (S1, S2); además, tu pupila recoge poca luz, separa detalles hasta cierto tamaño y puede engañarte.

📘 **Dónde se aprende** (1 clase): [B01-C10 · Limitaciones de los sentidos humanos](../programa/clases/B01/B01-C10-limitaciones-de-los-sentidos-humanos/CLASE.md).

### Límite de replicación

- Un límite de replicación es el valor de una variable por debajo (o encima) del cual no hay división celular.

🎯 **Por qué importa (clase B56-C05):** Decidir si un ambiente es habitable, o si una nave puede contaminarlo, exige umbrales de temperatura y de agua disponible. La decisión central: dada la temperatura y la actividad del agua de un ambiente, ¿está dentro de los límites en que la vida terrestre puede replicarse?

📘 **Dónde se aprende** (1 clase): [B56-C05 · Extremófilos y límites ambientales](../programa/clases/B56/B56-C05-extremofilos-y-limites-ambientales/CLASE.md).

### Límite de Roche

- El límite de Roche es la distancia dentro de la cual la marea supera la autogravedad de un cuerpo.
- El límite de Roche rígido es `1,26 R (ρ_M/ρ_m)^{1/3}` y el fluido `2,456 R (ρ_M/ρ_m)^{1/3}`.

💡 **Cómo se explica en la clase [B73-C16](../programa/clases/B73/B73-C16-dinamica-de-anillos/CLASE.md):**
- Con `GM_Saturno ≈ 3,7931e+07 km³/s²` (deducido) y densidad de partícula ilustrativa de `920 kg/m³`, el límite de Roche es `66 570 km` (rígido) y `129 758 km` (fluido); la resonancia 2:1 de Mimas cae en `r = 116 870 km` (`1,939 R_S`), donde el periodo de una partícula es la mitad del de Mimas.
- 🎯 **Por qué importa:** Un anillo existe donde las mareas impiden que las partículas se junten, se ensancha por viscosidad y se estructura por resonancias con las lunas. La decisión central: ¿qué escalas fijan dónde hay un anillo, cuánto dura y dónde lo moldean las lunas?

📖 **Explicado a fondo:** [Límite de Roche](esencial/ampliacion-a-m.md#límite-de-roche) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B52-C12 · Anillos planetarios](../programa/clases/B52/B52-C12-anillos-planetarios/CLASE.md); [B73-C16 · Dinámica de anillos](../programa/clases/B73/B73-C16-dinamica-de-anillos/CLASE.md).

### Límite de Shannon

- El límite de Shannon `C = B log₂(1+SNR)` es la tasa máxima sin errores.

🎯 **Por qué importa (clase B47-C18):** Los datos que no caben en un paso se pierden o se acumulan. La decisión central: ¿cuántos bits por paso admite el enlace con margen suficiente?

📘 **Dónde se aprende** (2 clases): [B47-C18 · Downlink de instrumentos científicos](../programa/clases/B47/B47-C18-downlink-de-instrumentos-cientificos/CLASE.md); [B89-C02 · Frecuencia y espectro espacial](../programa/clases/B89/B89-C02-frecuencia-y-espectro-espacial/CLASE.md).

### Límite de velocidad

- La saturación y el límite de velocidad son topes del actuador.

🎯 **Por qué importa (clase B77-C24):** El control de un lanzador inestable debe ser lo bastante rápido para estabilizarlo y lo bastante suave para no saturar la tobera. La decisión central: ¿qué ganancias cumplen una especificación dada y qué ocurre cuando la demanda supera los límites del actuador?

📘 **Dónde se aprende** (1 clase): [B77-C24 · Guiado y control de actitud de lanzadores (TVC)](../programa/clases/B77/B77-C24-guiado-y-control-de-actitud-de-lanzadores-tvc/CLASE.md).

### Límite elástico al 0,2 %

- El límite elástico al 0,2 % `σ₀,₂` es la tensión a la que la deformación plástica residual sería 0,002.

🎯 **Por qué importa (clase B84-C02):** Dos aleaciones con la misma rigidez específica pueden diferir en 7 veces su resistencia específica (Ti frente a acero 304); elegir por una sola propiedad lleva a un mal diseño. La decisión central: ¿qué aleación es mejor según el índice que importa a la pieza, y qué significa el límite elástico al 0,2 %?

📘 **Dónde se aprende** (1 clase): [B84-C02 · Propiedades de aleaciones](../programa/clases/B84/B84-C02-propiedades-de-aleaciones/CLASE.md).

### Límite empinado

- El límite empinado (undershoot) está fijado por la carga o el calentamiento.

💡 **Cómo se explica en la clase [B77-C25](../programa/clases/B77/B77-C25-corredores-de-entrada-y-limites-de-trayectoria/CLASE.md):**
- *Descripción textual:* para cada ángulo de entrada se simula el paso por la atmósfera; el máximo de desaceleración da el límite empinado y el apogeo de salida da el somero; su diferencia es el corredor, que la sustentación ensancha.
- 🎯 **Por qué importa:** El corredor es la tolerancia que se le deja a la navegación y a la guía antes de entrar. La decisión central: ¿entre qué ángulos puede entrar el vehículo, cuánto ensancha el corredor la sustentación y cuándo falla la estimación de Allen–Eggers?

📘 **Dónde se aprende** (1 clase): [B77-C25 · Corredores de entrada y límites de trayectoria](../programa/clases/B77/B77-C25-corredores-de-entrada-y-limites-de-trayectoria/CLASE.md).

### Límite en dos variables

- Un límite en dos variables exige que el valor sea el mismo por cualquier trayectoria.

🎯 **Por qué importa (clase B09-C15):** Una sonda que viaja de la Tierra a la Luna se mueve en un campo de potencial que depende de dos coordenadas del plano. Dónde están los puntos de equilibrio y qué forma tiene el campo alrededor de ellos se lee en un mapa de curvas de nivel.

📘 **Dónde se aprende** (1 clase): [B09-C15 · Funciones de varias variables](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md).

### Límite fijo

- Anomalía: desvío de lo esperado. Límite fijo: umbral de 3σ.

💡 **Cómo se explica en la clase [B96-C13](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md):**
- Un límite fijo es excelente para saltos grandes, pero una deriva de 0,8σ solo cruza el umbral por casualidad del ruido (53 muestras).
- Analogía: el límite fijo es como un detector de humo que suena con humo abundante;
- 🎯 **Por qué importa:** Un detector que no ve una deriva lenta avisa cuando ya es tarde, y uno que alarma por todo se ignora. La decisión central: ¿qué detector ve cada tipo de anomalía, con qué retraso y a qué costo en falsas alarmas?

📘 **Dónde se aprende** (1 clase): [B96-C13 · Detección de anomalías](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md).

### Límite galileano

- El límite galileano es el caso `u, v ≪ c`.

🎯 **Por qué importa (clase B26-C01):** Una nave espacial, un satélite de navegación y un rayo gamma comparten un problema: decir cómo se ve el mismo fenómeno desde marcos que se mueven entre sí. Si las velocidades se sumaran siempre como `u + v`, la luz de una nave que viaja al `90 %` de `c` iría más rápido que `c`.

📘 **Dónde se aprende** (1 clase): [B26-C01 · Postulados de relatividad especial](../programa/clases/B26/B26-C01-postulados-de-relatividad-especial/CLASE.md).

### Límite lateral

- El límite lateral por la izquierda (`x → a⁻`) o por la derecha (`x → a⁺`) acerca `x` solo desde un lado.

🎯 **Por qué importa (clase B09-C01):** Los astrónomos miden distancias a estrellas cercanas por paralaje: un ángulo diminuto, de fracciones de segundo de arco. Con ángulos tan pequeños, `sin t`, `tan t` y `t` casi coinciden, y casi todos los cálculos prácticos los sustituyen.

📘 **Dónde se aprende** (1 clase): [B09-C01 · Límites de funciones reales](../programa/clases/B09/B09-C01-limites-de-funciones-reales/CLASE.md).

### Límite newtoniano

- El límite newtoniano es `g_00 ≈ −(1 + 2Φ)` con `∇²Φ = 4πGρ`.

💡 **Cómo se explica en la clase [B39-C05](../programa/clases/B39/B39-C05-ecuaciones-de-campo-de-einstein-y-limite-newtoniano/CLASE.md):**
- *Descripción textual:* se calcula G desde la métrica y se compara con la materia en el límite newtoniano y en FLRW.
- 🎯 **Por qué importa:** Las ecuaciones de campo conectan la geometría con la materia. La decisión central: ¿en qué régimen la gravedad de Einstein se reduce a la de Newton y qué garantiza la consistencia de las ecuaciones?

📘 **Dónde se aprende** (1 clase): [B39-C05 · Ecuaciones de campo de Einstein y límite newtoniano](../programa/clases/B39/B39-C05-ecuaciones-de-campo-de-einstein-y-limite-newtoniano/CLASE.md).

### Límite parabólico

- El límite parabólico es `e → 1`.

💡 **Cómo se explica en la clase [B75-C14](../programa/clases/B75/B75-C14-captura-en-destino/CLASE.md):**
- Por el límite parabólico: cota inferior del delta-v.
- 🎯 **Por qué importa:** Frenar cuesta propulsante; cuanto más baja la órbita final, más cuesta. La decisión central: ¿qué órbita de captura minimiza el delta-v, y qué se paga después por llevarla a la órbita de trabajo?

📘 **Dónde se aprende** (1 clase): [B75-C14 · Captura en destino](../programa/clases/B75/B75-C14-captura-en-destino/CLASE.md).

### Límite somero

- El límite somero (overshoot) está fijado por la captura.

🎯 **Por qué importa (clase B77-C25):** El corredor es la tolerancia que se le deja a la navegación y a la guía antes de entrar. La decisión central: ¿entre qué ángulos puede entrar el vehículo, cuánto ensancha el corredor la sustentación y cuándo falla la estimación de Allen–Eggers?

📘 **Dónde se aprende** (1 clase): [B77-C25 · Corredores de entrada y límites de trayectoria](../programa/clases/B77/B77-C25-corredores-de-entrada-y-limites-de-trayectoria/CLASE.md).

### Límite superior

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B31-C18):** Un límite mal calculado puede excluir una teoría que no estaba excluida. La decisión central: ¿qué señal máxima es compatible con lo observado y cuán fiable es el método?

📘 **Dónde se aprende** (1 clase): [B31-C18 · Restricciones experimentales de teorías](../programa/clases/B31/B31-C18-restricciones-experimentales-de-teorias/CLASE.md).

### Límites

- Los límites son de par de rueda y de momento.
- Los límites dicen qué no cubre el informe.

💡 **Cómo se explica en la clase [B74-C22](../programa/clases/B74/B74-C22-informe-de-navegacion-verificable/CLASE.md):**
- El informe declara: identificador, sistema de referencia, escala de tiempo, unidades, versiones de software, semilla, entradas con huellas, estado, covarianza, métricas y límites.
- 🎯 **Por qué importa:** Cuando dos equipos discrepan en una trayectoria, la primera pregunta es qué entradas y qué versiones usó cada uno. La decisión central: ¿qué debe llevar un informe para que cualquiera pueda reproducirlo y detectar que se alteró un dato?

📘 **Dónde se aprende** (2 clases): [B74-C22 · Informe de navegación verificable](../programa/clases/B74/B74-C22-informe-de-navegacion-verificable/CLASE.md); [B87-C20 · Simulación ADCS integral](../programa/clases/B87/B87-C20-simulacion-adcs-integral/CLASE.md).

### Límites de acuerdo

- Los límites de acuerdo de Bland–Altman son `d̄ ± 1,96 SD_d`.

💡 **Cómo se explica en la clase [B105-C26](../programa/clases/B105/B105-C26-medidas-fisiologicas-y-biomarcadores-en-investigacion-espacial/CLASE.md):**
- Con 50 pares y un sesgo sistemático sintético de +1,5 en la segunda sesión: sesgo estimado 2,08 y límites de acuerdo de −9,96 a 14,13.
- 🎯 **Por qué importa:** Un biomarcador con alta variación interna no detecta cambios pequeños aunque sea «preciso». Con pocos participantes, además, el propio ICC es incierto.

📘 **Dónde se aprende** (1 clase): [B105-C26 · Medidas fisiológicas y biomarcadores en investigación espacial](../programa/clases/B105/B105-C26-medidas-fisiologicas-y-biomarcadores-en-investigacion-espacial/CLASE.md).

### Linaje

- El linaje (*provenance*) es el historial de un dato.

🎯 **Por qué importa (clase B118-C21):** B48-C11 trata la calidad de datos astronómicos; ninguna clase evalúa datos de vigilancia (latencia, cobertura, trazabilidad). Una conjunción se evalúa con datos que ya envejecieron; un dato sin historial no se puede auditar.

📘 **Dónde se aprende** (1 clase): [B118-C21 · Calidad, latencia y trazabilidad de datos de vigilancia espacial](../programa/clases/B118/B118-C21-calidad-latencia-y-trazabilidad-de-datos-de-vigilancia-espacial/CLASE.md).

### Línea

- La línea es el pico de opacidad de una molécula.
- La línea del disco y las cuentas `4 × líneas`.

💡 **Cómo se explica en la clase [B29-C12](../programa/clases/B29/B29-C12-espectroscopia-de-transmision/CLASE.md):**
- En el centro de la línea con `x = 1`, el radio efectivo sube `4,625 H`, frente a `H ln[(σ_c + σ_L)/σ_c] = 4,615 H`.
- Con 40 canales, una línea gaussiana (centro 20, ancho 3), ruido de `20 ppm` por canal y `x = 0,01`, en 300 realizaciones: `log₁₀ x = −2,0000 ± 0,0408` (media y desviación).
- 🎯 **Por qué importa:** La amplitud de una línea mide la abundancia: una línea más fuerte se eleva más sobre el continuo. La decisión central: ¿qué incremento de radio produce una línea y con qué precisión se recupera la abundancia de la molécula?

📘 **Dónde se aprende** (2 clases): [B29-C12 · Espectroscopía de transmisión](../programa/clases/B29/B29-C12-espectroscopia-de-transmision/CLASE.md); [B43-C16 · Encoders y medición angular](../programa/clases/B43/B43-C16-encoders-y-medicion-angular/CLASE.md).

### Línea base

- La línea base (*baseline*) es la versión de referencia contra la que se mide una mejora.
- La línea base es el mejor código serie, no el código paralelo con un proceso.
- La línea base es el nivel sin perturbación.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B18-C04](../programa/clases/B18/B18-C04-perfilado-de-rendimiento/CLASE.md):**
- Línea base<br/>correcta y cronometrada"] --> B["2.
- Se parte de una línea base correcta y cronometrada; se perfila para ver qué concentra el tiempo; se decide qué cambiar (algoritmo, estructura de datos o implementación); se cambia una sola cosa; se verifica que el resultado no cambió y se vuelve a medir, lo que lleva de nuevo a perfilar.
- 🎯 **Por qué importa:** Casi todo programa científico tiene un cuello de botella que el autor no sospecha. Optimizar a ojo suele mejorar lo que no importa.

📘 **Dónde se aprende** (7 clases): [B18-C04 · Perfilado de rendimiento](../programa/clases/B18/B18-C04-perfilado-de-rendimiento/CLASE.md); [B18-C05 · Experimentos de escalabilidad](../programa/clases/B18/B18-C05-experimentos-de-escalabilidad/CLASE.md); [B30-C23 · Índices geomagnéticos Kp y Dst](../programa/clases/B30/B30-C23-indices-geomagneticos-kp-y-dst/CLASE.md); [B42-C10 · Interferometría de múltiples telescopios](../programa/clases/B42/B42-C10-interferometria-de-multiples-telescopios/CLASE.md); [B57-C27 · Detección de cambios en series de imágenes](../programa/clases/B57/B57-C27-deteccion-de-cambios-en-series-de-imagenes/CLASE.md); [B83-C15 · Gestión de configuración](../programa/clases/B83/B83-C15-gestion-de-configuracion/CLASE.md) y 1 más.

### Línea base personal

- La línea base personal es la media y la desviación de los primeros días.
- La línea base personal es la media y la dispersión propias en un periodo de referencia.

💡 **Cómo se explica en la clase [B105-C09](../programa/clases/B105/B105-C09-salud-mental-en-aislamiento/CLASE.md):**
- *Descripción textual:* la serie se estandariza con una línea base personal, el CUSUM acumula las desviaciones bajas y emite una alarma al superar `h`; se mide el compromiso entre falsas alarmas, detección y retraso.
- 🎯 **Por qué importa:** Un umbral bajo detecta pronto pero alarma de más; uno alto alarma poco pero tarda. Con una tripulación pequeña, las falsas alarmas se acumulan.

📘 **Dónde se aprende** (2 clases): [B105-C09 · Salud mental en aislamiento](../programa/clases/B105/B105-C09-salud-mental-en-aislamiento/CLASE.md); [B116-C02 · Signos vitales: medición, interpretación y límites](../programa/clases/B116/B116-C02-signos-vitales-medicion-interpretacion-y-limites/CLASE.md).

### Línea base temporal

- La línea base temporal es el intervalo entre las dos tomas.

🎯 **Por qué importa (clase B57-C08):** El radar es la única herramienta orbital que mide movimientos del suelo de milímetros a escala regional, pero la fase solo se conoce módulo `2π`. La decisión central: ¿cuándo se puede reconstruir el desplazamiento y cuándo el desenrollado de la fase deja de ser fiable?

📘 **Dónde se aprende** (1 clase): [B57-C08 · Interferometría radar InSAR](../programa/clases/B57/B57-C08-interferometria-radar-insar/CLASE.md).

### Línea de absorción

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C21):** El campo solar se infiere de una señal diminuta: una diferencia de polarización circular. La decisión central: ¿cuántas posiciones espectrales y qué ruido permiten medir el campo con una incertidumbre dada, y hasta qué campo vale la aproximación débil?

📘 **Dónde se aprende** (1 clase): [B47-C21 · Magnetógrafos y medición de campos solares](../programa/clases/B47/B47-C21-magnetografos-y-medicion-de-campos-solares/CLASE.md).

### Línea de ápsides

- La línea de ápsides es la que une perigeo y apogeo.

💡 **Cómo se explica en la clase [B72-C05](../programa/clases/B72/B72-C05-precesion-del-argumento-del-periapsis/CLASE.md):**
- Analogía: como una elipse dibujada en un disco que se hace girar despacio, la línea de ápsides puede girar a favor, en contra o quedarse fija según la inclinación del disco.
- Por periodo de rotación de la línea de ápsides: `360/|dω/dt|`.
- 🎯 **Por qué importa:** Si el perigeo de una órbita muy excéntrica girara, el satélite dejaría de pasar por la región que interesa. La decisión central: ¿a qué inclinación el perigeo deja de moverse y cuánto se mueve en otras?

📘 **Dónde se aprende** (1 clase): [B72-C05 · Precesión del argumento del periapsis](../programa/clases/B72/B72-C05-precesion-del-argumento-del-periapsis/CLASE.md).

### Línea de base

- La línea de base es la separación entre dos detectores.
- La línea de base es el vector entre dos antenas.
- La línea de base `B` es la separación entre estaciones.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B46-C14](../programa/clases/B46/B46-C14-lineas-de-base-interferometricas/CLASE.md):**
- Como la sombra de un palo cambia con la hora, la línea de base 'vista' desde la fuente cambia con la rotación de la Tierra y traza una elipse.
- *Descripción textual:* la línea de base local se proyecta con la latitud, la declinación y el ángulo horario para dar el punto `uv` y el retardo.
- 🎯 **Por qué importa:** La línea de base fija la escala angular que se ve y el retardo que hay que compensar. La decisión central: ¿qué punto del plano `uv` y qué retardo corresponden a una línea de base y a una dirección?

📘 **Dónde se aprende** (4 clases): [B28-C10 · Localización probabilística de eventos](../programa/clases/B28/B28-C10-localizacion-probabilistica-de-eventos/CLASE.md); [B46-C14 · Líneas de base interferométricas](../programa/clases/B46/B46-C14-lineas-de-base-interferometricas/CLASE.md); [B74-C15 · Geometría de la red de seguimiento](../programa/clases/B74/B74-C15-geometria-de-la-red-de-seguimiento/CLASE.md); [B103-C03 · Mapas de profundidad y correspondencia estéreo](../programa/clases/B103/B103-C03-mapas-de-profundidad-y-correspondencia-estereo/CLASE.md).

### Línea de base crítica

- La línea de base crítica es la separación de órbitas para la que `n = 1` ciclo de franja cruza la celda.

💡 **Cómo se explica en la clase [B69-C05](../programa/clases/B69/B69-C05-coherencia-interferometrica-y-decorrelacion/CLASE.md):**
- Si las dos órbitas difieren, las fases de los dispersores de una celda se desfasan de forma lineal con su posición; con `n` ciclos de franja a lo largo de la celda, `γ_g = |sinc(n)|`: 0,25 → 0,9009; 0,5 → 0,6383 (modelo 0,6366); en `n = 1` la coherencia geométrica es nula (línea de base crítica).
- 🎯 **Por qué importa:** Un interferograma sin coherencia es ruido con aspecto de franjas. La decisión central: ¿cuánto puedo fiarme de la fase de un pixel y qué la degrada?

📘 **Dónde se aprende** (1 clase): [B69-C05 · Coherencia interferométrica y decorrelación](../programa/clases/B69/B69-C05-coherencia-interferometrica-y-decorrelacion/CLASE.md).

### Línea de caché

- Una línea de caché es el bloque de bytes que se trae de una vez; en CPU de uso general suele ser de 64 bytes (dato general; no consultado en una fuente para esta clase).

🎯 **Por qué importa (clase B18-C03):** Un catálogo con millones de estrellas o una rejilla de simulación pasan cada dato por la CPU una o pocas veces. Cuando las operaciones por dato son pocas, el tiempo no lo fija la CPU sino el viaje de los datos.

📘 **Dónde se aprende** (1 clase): [B18-C03 · Jerarquía y estructuras de memoria](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md).

### Línea de evidencia

- Una línea de evidencia es una observación independiente con razón de verosimilitud `LR`.
- Una línea de evidencia es una fuente independiente de apoyo a una hipótesis.

💡 **Cómo se explica en la clase [B56-C19](../programa/clases/B56/B56-C19-etica-del-descubrimiento-de-vida/CLASE.md):**
- Cada línea de evidencia añade peso (positivo si favorece, negativo si refuta).
- 🎯 **Por qué importa:** Anunciar demasiado pronto un hallazgo puede dañar la ciencia y la confianza pública; ocultarlo puede dañar la transparencia. Hace falta una forma explícita de saber cuánta evidencia hay.

📘 **Dónde se aprende** (2 clases): [B56-C19 · Ética del descubrimiento de vida](../programa/clases/B56/B56-C19-etica-del-descubrimiento-de-vida/CLASE.md); [B132-C05 · Contexto ritual y social de la observación del cielo](../programa/clases/B132/B132-C05-contexto-ritual-y-social-de-la-observacion-del-cielo/CLASE.md).

### Línea de lámpara

- La línea de lámpara con longitud de onda de catálogo.

🎯 **Por qué importa (clase B45-C08):** Un error de calibración es un error de velocidad o de identificación de líneas. La decisión central: ¿qué grado del polinomio es adecuado y cuánto se puede fiar el ajuste fuera de las líneas?

📘 **Dónde se aprende** (1 clase): [B45-C08 · Calibración en longitud de onda](../programa/clases/B45/B45-C08-calibracion-en-longitud-de-onda/CLASE.md).

### Línea de nodos

- La línea de nodos es la intersección de dos círculos fundamentales; el nodo ascendente es el punto donde un plano cruza al otro de sur a norte.
- La línea de nodos es la intersección del plano orbital con el ecuatorial.
- La línea de nodos es donde se hace el cambio.

💡 **Cómo se explica en la clase [B04-C19](../programa/clases/B04/B04-C19-transformaciones-de-coordenadas-astronomicas/CLASE.md):**
- La línea de nodos del plano galáctico sobre el ecuador es perpendicular a `ẑ` y a `ẑ_G`: `N = ẑ × ẑ_G / |ẑ × ẑ_G|`.
- 🎯 **Por qué importa:** Un catálogo da las posiciones en ecuatoriales; un estudio de la Vía Láctea necesita galácticas; un análisis del plano del sistema solar usa eclípticas. Cambiar de sistema es rutina, y un error de signo o de matriz mueve el objeto decenas de grados.

📘 **Dónde se aprende** (3 clases): [B04-C19 · Transformaciones de coordenadas astronómicas](../programa/clases/B04/B04-C19-transformaciones-de-coordenadas-astronomicas/CLASE.md); [B71-C11 · Inclinación y nodo ascendente](../programa/clases/B71/B71-C11-inclinacion-y-nodo-ascendente/CLASE.md); [B71-C19 · Cambios de plano simples](../programa/clases/B71/B71-C19-cambios-de-plano-simples/CLASE.md).

### Línea de radio constante

- Una línea de radio constante (isorradio) une los puntos del diagrama con el mismo `R`.

🎯 **Por qué importa (clase B24-C03):** Casi todas las propiedades de una estrella (tamaño, masa, edad, fase) se resumen en dos medidas: cuánta energía emite y a qué temperatura. El diagrama HR convierte esas dos medidas en un mapa donde cada región corresponde a un estado físico.

📘 **Dónde se aprende** (1 clase): [B24-C03 · Diagrama de Hertzsprung-Russell](../programa/clases/B24/B24-C03-diagrama-de-hertzsprung-russell/CLASE.md).

### Línea de rumbo constante

- Una línea de rumbo constante (loxodrómica) corta a los meridianos siempre con el mismo ángulo.

🎯 **Por qué importa (clase B04-C17):** Casi todo lo que ves del espacio, de la Tierra o de otro cuerpo, llega en forma de mapa: la superficie de un planeta, el cielo entero, la huella de un satélite. Y un mapa es una proyección.

📘 **Dónde se aprende** (1 clase): [B04-C17 · Proyecciones cartográficas elementales](../programa/clases/B04/B04-C17-proyecciones-cartograficas-elementales/CLASE.md).

### Línea de universo

- Una línea de universo es la sucesión de eventos de un objeto.

💡 **Cómo se explica en la clase [B26-C04](../programa/clases/B26/B26-C04-espacio-tiempo-de-minkowski/CLASE.md):**
- El tiempo que mide un reloj a lo largo de una línea de universo es `τ = ∫ √(1 − β²) dt`, con `β = v/c`.
- La situación no es simétrica porque la viajera cambia de marco inercial al dar la vuelta: su línea de universo es una poligonal de dos tramos.
- 🎯 **Por qué importa:** Comunicar con una sonda, sincronizar relojes de dos estaciones o decidir si un evento puede haber causado otro exige saber cuándo dos sucesos están conectados por una señal. El intervalo lo decide para todos los observadores.

📘 **Dónde se aprende** (1 clase): [B26-C04 · Espacio-tiempo de Minkowski](../programa/clases/B26/B26-C04-espacio-tiempo-de-minkowski/CLASE.md).

### Línea de visión

- La línea de visión de una baliza pasa por su posición con dirección `u`.

💡 **Cómo se explica en la clase [B74-C13](../programa/clases/B74/B74-C13-navegacion-optica/CLASE.md):**
- Cada imagen de una baliza a distancia `ρ` con incertidumbre angular `σ` informa sobre la posición transversal a la línea de visión, con varianza `(ρσ)²`.
- 🎯 **Por qué importa:** Una dirección conocida con un microrradián son cientos de kilómetros a la distancia de un planeta. La decisión central: ¿cuánta incertidumbre de posición produce una cierta incertidumbre angular y cómo depende de la geometría de las balizas?

📘 **Dónde se aprende** (1 clase): [B74-C13 · Navegación óptica](../programa/clases/B74/B74-C13-navegacion-optica/CLASE.md).

### Línea espectral

- Una línea espectral es una longitud de onda concreta donde hay más o menos luz.
- Una línea espectral es un máximo o mínimo estrecho de ese espectro.

🎯 **Por qué importa (clase B01-C09):** Sobre una galaxia a 43 Mpc solo tienes luz. De esa luz sale su dirección, cuánto brilla, de qué color es y qué líneas aparecen en su espectro; de las líneas sale `z = 0,0101` (C01).

📘 **Dónde se aprende** (2 clases): [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B06-C17 · Espectros atómicos y moleculares](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md).

### Línea mezclada

- Una línea mezclada (*blend*) tiene otra a menos de un ancho `w`.

🎯 **Por qué importa (clase B62-C08):** Una línea que coincide con una frecuencia de catálogo no identifica una molécula: puede ser casualidad. La decisión central: ¿cuántas líneas hacen falta para afirmar una identificación con riesgo bajo de falsa alarma?

📘 **Dónde se aprende** (1 clase): [B62-C08 · Mezclas moleculares y confusión de líneas](../programa/clases/B62/B62-C08-mezclas-moleculares-y-confusion-de-lineas/CLASE.md).

### Lineal

- Una relación lineal es `y = kx + b`; es proporcional solo si `b = 0`.
- Una ecuación es lineal si la incógnita aparece solo a la primera potencia, y cuadrática si el mayor exponente es 2.
- Las formas básicas son lineal (2 dominios, 180°), trigonal plana (3, 120°) y tetraédrica (4, 109,47°).
- *(y 9 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C10](../programa/clases/B03/B03-C10-proporcionalidad-directa-e-inversa/CLASE.md):**
- En cambio `y = 3, 5, 7` da `3; 2,5; 2,33`: no es proporcional (es lineal con `b = 1`).
- El límite: en una pizza el reparto es lineal en el número de personas; la luz se reparte sobre una superficie esférica cuya área crece con el cuadrado de la distancia (C17), de ahí `1/d²`.
- 🎯 **Por qué importa:** Un panel solar en órbita de Marte no recibe la misma energía que uno en órbita de la Tierra. ¿Cuánta menos?

📘 **Dónde se aprende** (12 clases): [B03-C10 · Proporcionalidad directa e inversa](../programa/clases/B03/B03-C10-proporcionalidad-directa-e-inversa/CLASE.md); [B04-C02 · Ecuaciones lineales y cuadráticas](../programa/clases/B04/B04-C02-ecuaciones-lineales-y-cuadraticas/CLASE.md); [B04-C03 · Sistemas de ecuaciones elementales](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md); [B06-C05 · Moléculas y geometría molecular](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md); [B11-C01 · Ecuaciones diferenciales ordinarias](../programa/clases/B11/B11-C01-ecuaciones-diferenciales-ordinarias/CLASE.md); [B11-C03 · Ecuaciones de primer orden](../programa/clases/B11/B11-C03-ecuaciones-de-primer-orden/CLASE.md) y 6 más.

### Lineal con coeficientes constantes

- Un sistema es lineal con coeficientes constantes si `s′ = A s` con `A` una matriz fija.

🎯 **Por qué importa (clase B11-C04):** Un programa que propaga una trayectoria no entiende `r″ = −GM r/|r|³`: entiende una función que recibe un estado y devuelve su derivada. Si escribes mal ese puente, ningún método, por bueno que sea, te salva.

📘 **Dónde se aprende** (1 clase): [B11-C04 · Sistemas de ecuaciones diferenciales](../programa/clases/B11/B11-C04-sistemas-de-ecuaciones-diferenciales/CLASE.md).

### Lineal en los parámetros

- Un modelo es lineal en los parámetros si `f = Σ β_j φ_j(x)` (aunque las `φ_j` no sean rectas); entonces la solución es directa.

🎯 **Por qué importa (clase B15-C16):** En C01 una recta ajustada a 2,8 periodos de una oscilación dio una pendiente de −2,24 × 10⁻⁴ por día cuando la real era −1,00 × 10⁻⁴: el modelo estaba mal planteado.

📘 **Dónde se aprende** (1 clase): [B15-C16 · Ajuste de curvas](../programa/clases/B15/B15-C16-ajuste-de-curvas/CLASE.md).

### Linealidad

- La linealidad es la proporcionalidad entre luz y cuentas.
- La linealidad de la respuesta permite propagar covarianzas con la matriz de transición.

💡 **Cómo se explica en la clase [B44-C10](../programa/clases/B44/B44-C10-no-linealidad-y-saturacion/CLASE.md):**
- La desviación respecto del ajuste de la zona baja subestima la no linealidad (el ajuste absorbe parte de la curvatura); respecto del flujo ideal es la correcta.
- En este barrido la salida máxima es `54 600 ADU`, por debajo del recorte de `60 000`: la no linealidad aparece mucho antes de la saturación.
- 🎯 **Por qué importa:** Si la respuesta se curva, la fotometría se sesga mucho antes del pozo lleno. La decisión central: ¿hasta qué flujo puedo confiar en la respuesta lineal?

📘 **Dónde se aprende** (2 clases): [B44-C10 · No linealidad y saturación](../programa/clases/B44/B44-C10-no-linealidad-y-saturacion/CLASE.md); [B72-C19 · Análisis de sensibilidad orbital](../programa/clases/B72/B72-C19-analisis-de-sensibilidad-orbital/CLASE.md).

### Linealización

- La linealización es `t² = 4x²/v² + 4d²/v²`: pendiente `4/v²`, intercepto `4d²/v²`.

🎯 **Por qué importa (clase B53-C30):** Sin conocer la velocidad, un retardo no da profundidad. La decisión central: ¿se puede estimar la velocidad del medio con los propios datos y qué error de profundidad produce suponerla mal?

📘 **Dónde se aprende** (1 clase): [B53-C30 · Radar de penetración subsuperficial en cuerpos planetarios](../programa/clases/B53/B53-C30-radar-de-penetracion-subsuperficial-en-cuerpos-planetarios/CLASE.md).

### Linealmente independiente

- Un conjunto de vectores es linealmente independiente si ninguna combinación lineal no trivial da el cero; si no, es dependiente.

🎯 **Por qué importa (clase B10-C02):** Un vector es una entidad geométrica; sus «componentes» dependen de los ejes que elijas. Un operador de estación terrestre describe un satélite con ejes ligados al ecuador; el satélite mismo, con ejes ligados a su órbita; un instrumento, con ejes del instrumento.

📘 **Dónde se aprende** (1 clase): [B10-C02 · Bases y dimensión](../programa/clases/B10/B10-C02-bases-y-dimension/CLASE.md).

### Líneas

- Las líneas d (587,56 nm), F (486,13 nm) y C (656,27 nm).

🎯 **Por qué importa (clase B43-C21):** Un telescopio refractor o un corrector necesita vidrios que compensen el color. La decisión central: ¿qué par de vidrios, con qué potencias, anula el cromatismo primario de un doblete y qué error aporta la falta de homogeneidad?

📘 **Dónde se aprende** (1 clase): [B43-C21 · Selección de vidrios ópticos: catálogos, homogeneidad y diagramas](../programa/clases/B43/B43-C21-seleccion-de-vidrios-opticos-catalogos-homogeneidad-y-diagramas/CLASE.md).

### Líneas aurorales

- Las líneas aurorales son las emisiones del oxígeno y del nitrógeno.

🎯 **Por qué importa (clase B30-C17):** La aurora y las corrientes ionosféricas son la parte visible y eléctrica del acoplamiento entre la magnetosfera y la atmósfera. La decisión central: ¿dónde se produce la ionización y cuánta energía se disipa por efecto Joule?

📘 **Dónde se aprende** (1 clase): [B30-C17 · Auroras y corrientes ionosféricas](../programa/clases/B30/B30-C17-auroras-y-corrientes-ionosfericas/CLASE.md).

### Líneas de Fraunhofer

- Las líneas de Fraunhofer son las líneas oscuras del espectro solar (S1).

🎯 **Por qué importa (clase B02-C16):** Hasta 1859 se pensaba, con razones, que nunca sabríamos de qué están hechas las estrellas: estaban demasiado lejos para tocarlas. La pregunta motivadora es: ¿cómo se puede conocer la composición de un objeto que solo se ve como luz?

📘 **Dónde se aprende** (1 clase): [B02-C16 · Historia de la espectroscopía astronómica](../programa/clases/B02/B02-C16-historia-de-la-espectroscopia-astronomica/CLASE.md).

### Líneas intrusas

- Las líneas intrusas pertenecen a otra especie.

🎯 **Por qué importa (clase B55-C10):** Casi todas las detecciones de moléculas se basan en coincidencias de frecuencia, y hay catálogos con decenas de miles de líneas: una coincidencia aislada puede ser casualidad. La decisión central: ¿cuántas líneas asignadas, con qué velocidad común y con qué probabilidad de falso positivo se justifica afirmar una especie?

📘 **Dónde se aprende** (1 clase): [B55-C10 · Identificación de moléculas orgánicas](../programa/clases/B55/B55-C10-identificacion-de-moleculas-organicas/CLASE.md).

### Líneas por segundo

- Las líneas por segundo son `v_suelo/GSD`.

🎯 **Por qué importa (clase B83-C11):** Un satélite que produce más datos de los que puede bajar los pierde o se satura. La decisión central: ¿cabe todo lo que se produce en los minutos de contacto, y qué tamaño de registrador cubre el peor hueco?

📘 **Dónde se aprende** (1 clase): [B83-C11 · Presupuestos de datos](../programa/clases/B83/B83-C11-presupuestos-de-datos/CLASE.md).

### Liquidación

- La liquidación es el pago final.

💡 **Cómo se explica en la clase [B127-C06](../programa/clases/B127/B127-C06-gestion-de-siniestros-espaciales/CLASE.md):**
- Por etapas: aviso, peritaje, valoración, liquidación.
- 🎯 **Por qué importa:** Tras una pérdida hay un proceso de reclamación y peritaje que ninguna clase describía. La decisión central: ¿cuándo se considera total una pérdida parcial y cuánto cambia el pago por cruzar ese umbral?

📘 **Dónde se aprende** (1 clase): [B127-C06 · Gestión de siniestros espaciales](../programa/clases/B127/B127-C06-gestion-de-siniestros-espaciales/CLASE.md).

### Líquido

- En un sólido las partículas ocupan posiciones casi fijas; en un líquido están juntas pero se deslizan; en un gas están lejos y se mueven libres; en un plasma el gas está parcialmente o totalmente ionizado, es decir, hay electrones libres e iones.

💡 **Cómo se explica en la clase [B06-C10](../programa/clases/B06/B06-C10-estados-de-la-materia/CLASE.md):**
- Sólido, líquido y gas se distinguen por el orden y la distancia entre partículas.
- La entalpía de vaporización del agua a 298 K se obtiene de las entalpías de formación del NIST: `ΔfH(vapor) = −241,826 kJ/mol` y `ΔfH(líquido) = −285,830 kJ/mol`, de modo que `ΔH_vap = 44,004 kJ/mol` (S2).
- 🎯 **Por qué importa:** En Marte, la temperatura media es 214 K y la presión media en superficie 6,36 mb (S1). Ese valor está casi en el punto triple del agua, la presión mínima a la que puede existir agua líquida (S2).

📘 **Dónde se aprende** (1 clase): [B06-C10 · Estados de la materia](../programa/clases/B06/B06-C10-estados-de-la-materia/CLASE.md).

### Lista

- Una lista es una secuencia ordenada y modificable, entre corchetes (S2).

💡 **Cómo se explica en la clase [B07-C07](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md):**
- Una lista es una fila de cajones numerados; un diccionario es un fichero con etiquetas (claves) para buscar rápido; una tupla es una fila de cajones sellados; un conjunto es una bolsa donde cada cosa entra una vez.
- L["lista PLANETAS<br/>posiciones 0..7"] --> D0["0 → dict Mercurio"]
- ⚠️ **Error frecuente:** `lista = lista.sort()`. Deja `None`.
- 🎯 **Por qué importa:** Una tabla de ocho planetas con tres propiedades cada uno son 24 datos: no cabe en 24 variables sueltas. Necesitas estructuras que agrupen datos, permitan recorrerlos y los mantengan ordenados y consultables.

📘 **Dónde se aprende** (1 clase): [B07-C07 · Listas y estructuras de datos](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md).

### Lista de comprobación

- La lista de comprobación es un conjunto de reglas que se aplican al paquete.
- La lista de comprobación es una secuencia verificable de pasos.

🎯 **Por qué importa (clase B14-C19):** Subes tu código a un repositorio y tus datos a una carpeta compartida. Un año después, alguien quiere usarlos y no sabe si puede, cómo citarte, qué significan las columnas ni si el archivo es el que tú usaste.

📘 **Dónde se aprende** (2 clases): [B14-C19 · Publicación de código y datos](../programa/clases/B14/B14-C19-publicacion-de-codigo-y-datos/CLASE.md); [B104-C22 · Diseño y uso de listas de comprobación de cabina](../programa/clases/B104/B104-C22-diseno-y-uso-de-listas-de-comprobacion-de-cabina/CLASE.md).

### Lista de reglas

- Una lista de reglas evalúa condiciones en orden.

💡 **Cómo se explica en la clase [B119-C11](../programa/clases/B119/B119-C11-uso-pacifico-y-limitaciones-militares/CLASE.md):**
- Paso 4. La lista de reglas da el mismo resultado.
- 🎯 **Por qué importa:** C01 reduce el art. IV a una regla booleana; esta clase lo desagrega por ubicación y propósito y conecta con el art. 3 del Acuerdo sobre la Luna, y deja explícito lo no consultado.

📘 **Dónde se aprende** (1 clase): [B119-C11 · Uso pacífico y limitaciones militares](../programa/clases/B119/B119-C11-uso-pacifico-y-limitaciones-militares/CLASE.md).

### Lista de verificación

- La lista de verificación comprueba funciones o atributos como cumple o no cumple.

💡 **Cómo se explica en la clase [B109-C12](../programa/clases/B109/B109-C12-evaluacion-de-factores-humanos-de-maquetas-y-distribuciones/CLASE.md):**
- *Descripción textual:* cada evaluador puntúa ambas maquetas; la diferencia pareada se contrasta con un test exacto y se acota con un bootstrap; una lista de verificación aparte se evalúa con el acuerdo entre inspectores; todo termina en un informe que rotula qué es simulado.
- 🎯 **Por qué importa:** Sin medir, «esta distribución es mejor» es una opinión. La decisión central: ¿la diferencia entre dos maquetas es mayor que lo que daría el azar, y las personas que la evalúan coinciden entre sí?

📘 **Dónde se aprende** (1 clase): [B109-C12 · Evaluación de factores humanos de maquetas y distribuciones](../programa/clases/B109/B109-C12-evaluacion-de-factores-humanos-de-maquetas-y-distribuciones/CLASE.md).

### Litología

- Una litología es un tipo de roca.

💡 **Cómo se explica en la clase [B63-C02](../programa/clases/B63/B63-C02-muestreo-superficial-y-estrategias-de-recoleccion/CLASE.md):**
- Con `N` muestras independientes, la probabilidad de no capturar una litología de fracción `p` es `(1 − p)^N`.
- Cuando el presupuesto de tubos es menor que `N`, la decisión es elegir qué litología se sacrifica, y eso es una decisión científica, no estadística.
- 🎯 **Por qué importa:** Un rover tiene un número limitado de tubos. La decisión central: ¿cuántas muestras hacen falta para no perderse una litología rara con una confianza dada?

📘 **Dónde se aprende** (1 clase): [B63-C02 · Muestreo superficial y estrategias de recolección](../programa/clases/B63/B63-C02-muestreo-superficial-y-estrategias-de-recoleccion/CLASE.md).

### Littrow

- La configuración Littrow es `α = β`.

💡 **Cómo se explica en la clase [B45-C04](../programa/clases/B45/B45-C04-redes-de-difraccion/CLASE.md):**
- Una red de 600 l/mm (`d = 1666,67 nm`) con 100 mm de ancho (`N = 60 000`) usada en Littrow a `α = 8,627°` para 500 nm da `R = 60 000` en orden 1 (`δλ = 0,00833 nm`).
- 🎯 **Por qué importa:** La red es el elemento dispersor de casi todos los espectrógrafos. La decisión central: ¿en qué ángulo sale cada longitud de onda y qué resolución se obtiene?

📘 **Dónde se aprende** (1 clase): [B45-C04 · Redes de difracción](../programa/clases/B45/B45-C04-redes-de-difraccion/CLASE.md).

### LLA

- Los esquemas de datos se nombran LAL (lado–ángulo–lado), LLL (tres lados), ALA (ángulo–lado–ángulo) y LLA (lado–lado–ángulo no incluido).

💡 **Cómo se explica en la clase [B04-C08](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md):**
- B -->|"LLA"| E["Ley de senos: 0, 1 o 2 soluciones"]
- *Descripción textual:* según los datos (LAL o LLL, ALA o LLA) se usa la ley de cosenos, el tercer ángulo y la de senos, o la de senos con posible ambigüedad; todo termina comprobando que los ángulos suman 180°.
- 🎯 **Por qué importa:** Cuando una sonda se comunica con la Tierra, el tiempo de la señal depende de la distancia, que cambia de unos 55 millones de km a unos 400 millones según dónde estén ambos planetas en sus órbitas.

📘 **Dónde se aprende** (1 clase): [B04-C08 · Ley de senos y ley de cosenos](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md).

### Llamarada

- La llamarada es un aumento brusco de brillo.

💡 **Cómo se explica en la clase [B29-C15](../programa/clases/B29/B29-C15-eventos-eruptivos-estelares/CLASE.md):**
- Cada petardo (llamarada) tiene una energía; en un registro largo hay muchos pequeños y pocos grandes.
- *Descripción textual:* la llamarada tiene energía `L_q A τ`; las energías de una población se generan por transformada inversa de una ley de potencias truncada; el índice se estima por verosimilitud y su dispersión se compara con la teórica.
- 🎯 **Por qué importa:** La distribución de energías de las llamaradas determina cuánta energía total reciben los planetas cercanos. Estimar su índice con poco sesgo exige usar el estimador correcto.

📘 **Dónde se aprende** (1 clase): [B29-C15 · Eventos eruptivos estelares](../programa/clases/B29/B29-C15-eventos-eruptivos-estelares/CLASE.md).

### Llamarada gigante

- La llamarada gigante es un estallido de energía enorme.

🎯 **Por qué importa (clase B27-C06):** Los magnetares producen estallidos y llamaradas gigantes que alimenta su campo, no su rotación. Entender la escala del campo y de su energía explica por qué son una familia aparte y cómo se interpretan sus espectros.

📘 **Dónde se aprende** (1 clase): [B27-C06 · Magnetares y campos extremos](../programa/clases/B27/B27-C06-magnetares-y-campos-extremos/CLASE.md).

### Llanura

- Una llanura volcánica es una extensión de coladas.

🎯 **Por qué importa (clase B70-C05):** Un punto brillante o un vent que cambia no prueba una erupción. La decisión central: ¿cuánta lava caliente hace falta en un píxel para producir un aumento medible de radiancia, y qué otras explicaciones hay que descartar?

📘 **Dónde se aprende** (1 clase): [B70-C05 · Actividad volcánica venusina: llanuras, coronas e indicios de actividad reciente](../programa/clases/B70/B70-C05-actividad-volcanica-venusina-llanuras-coronas-e-indicios-de-actividad-reciente/CLASE.md).

### Llanura volcánica

- Una llanura volcánica es una extensión cubierta por coladas.

🎯 **Por qué importa (clase B70-C01):** Una llanura de lava no dice por sí sola cuánto magma la formó ni cuánto tardó. La decisión central: ¿qué volumen y qué caudal corresponden a este edificio y a esta fisura, y qué cambiaría en otro planeta?

📘 **Dónde se aprende** (1 clase): [B70-C01 · Volcanismo basáltico: escudos, fisuras y llanuras planetarias](../programa/clases/B70/B70-C01-volcanismo-basaltico-escudos-fisuras-y-llanuras-planetarias/CLASE.md).

### Llegada más temprana

- La llegada más temprana es el menor instante de entrega entre todas las rutas.

💡 **Cómo se explica en la clase [B89-C13](../programa/clases/B89/B89-C13-protocolos-para-espacio-profundo/CLASE.md):**
- *Descripción textual:* el paquete se almacena en cada nodo hasta el siguiente contacto; el plan de contactos permite calcular la ruta de llegada más temprana.
- 🎯 **Por qué importa:** Sin almacenamiento y reenvío, un rover marciano no podría comunicarse con Tierra: nunca hay una ruta continua. Entender los contactos, las capacidades y el encaminamiento es la base del diseño de redes interplanetarias.

📘 **Dónde se aprende** (1 clase): [B89-C13 · Protocolos para espacio profundo](../programa/clases/B89/B89-C13-protocolos-para-espacio-profundo/CLASE.md).

### Llenado de depresiones

- El llenado de depresiones elimina sumideros para que todo flujo salga.

💡 **Cómo se explica en la clase [B66-C04](../programa/clases/B66/B66-C04-redes-fluviales-fosiles-y-paleohidrologia-marciana/CLASE.md):**
- Z["terreno sintetico"] --> L["llenado de depresiones"]
- 🎯 **Por qué importa:** Un mapa de valles marcianos invita a decir «hubo un océano» o «hubo lluvia». La decisión central: ¿qué se puede inferir del caudal y de la duración con una red, un volumen y supuestos explícitos, y qué incertidumbre arrastra?

📘 **Dónde se aprende** (1 clase): [B66-C04 · Redes fluviales fósiles y paleohidrología marciana](../programa/clases/B66/B66-C04-redes-fluviales-fosiles-y-paleohidrologia-marciana/CLASE.md).

### LLL

- Los esquemas de datos se nombran LAL (lado–ángulo–lado), LLL (tres lados), ALA (ángulo–lado–ángulo) y LLA (lado–lado–ángulo no incluido).

💡 **Cómo se explica en la clase [B04-C08](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md):**
- *Descripción textual:* según los datos (LAL o LLL, ALA o LLA) se usa la ley de cosenos, el tercer ángulo y la de senos, o la de senos con posible ambigüedad; todo termina comprobando que los ángulos suman 180°.
- La ley de cosenos es la más segura: no tiene ambigüedad y sirve con LAL y LLL.
- 🎯 **Por qué importa:** Cuando una sonda se comunica con la Tierra, el tiempo de la señal depende de la distancia, que cambia de unos 55 millones de km a unos 400 millones según dónde estén ambos planetas en sus órbitas.

📘 **Dónde se aprende** (1 clase): [B04-C08 · Ley de senos y ley de cosenos](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md).

### LLT

- El LLT es el límite inferior de temperatura de replicación, −28 °C.

🎯 **Por qué importa (clase B56-C18):** La política protege los otros mundos de la contaminación (para no estropear la búsqueda de vida) y la Tierra del material devuelto. Saber en qué categoría cae una misión determina su documentación, su limpieza y sus restricciones.

📘 **Dónde se aprende** (1 clase): [B56-C18 · Protección planetaria COSPAR](../programa/clases/B56/B56-C18-proteccion-planetaria-cospar/CLASE.md).

### Lluvia de meteoros

- Una lluvia de meteoros es un aumento de la actividad de meteoros: unos pocos por hora son normales cualquier noche, y una lluvia los eleva mucho; suele nombrarse por una estrella o constelación cercana y ocurre cuando la Tierra atraviesa los restos de un cometa (S1).

🎯 **Por qué importa (clase B08-C18):** Cada año, titulares prometen «cientos de estrellas fugaces por hora». Con un cielo contaminado o con el radiante bajo el horizonte, verás muy pocas.

📘 **Dónde se aprende** (1 clase): [B08-C18 · Introducción a meteoros y lluvias](../programa/clases/B08/B08-C18-introduccion-a-meteoros-y-lluvias/CLASE.md).

### Lóbulo de rejilla

- El lóbulo de rejilla es un máximo principal extra por separación grande.
- Un lóbulo de rejilla es un máximo adicional del mismo nivel que el principal, causado por una separación excesiva.

💡 **Cómo se explica en la clase [B91-C03](../programa/clases/B91/B91-C03-arreglos-de-antenas-y-antenas-de-barrido-electronico/CLASE.md):**
- Paso 2 · Con `d = 0,5`. `0,5 < 0,667`: no hay lóbulo de rejilla.
- Con `d = 0,6 λ` aparece un lóbulo de rejilla a `60°`.
- 🎯 **Por qué importa:** Las antenas de barrido electrónico apuntan en microsegundos y no tienen partes móviles, pero cuestan más y pierden ganancia al desviar el haz. La decisión central: ¿cuántos elementos, qué separación y cuántos bits de fase hacen falta para un haz de cierto ancho y un barrido sin lóbulos de rejilla?

📘 **Dónde se aprende** (2 clases): [B49-C04 · Arreglos de antenas: factor de arreglo y formación de haz](../programa/clases/B49/B49-C04-arreglos-de-antenas-factor-de-arreglo-y-formacion-de-haz/CLASE.md); [B91-C03 · Arreglos de antenas y antenas de barrido electrónico](../programa/clases/B91/B91-C03-arreglos-de-antenas-y-antenas-de-barrido-electronico/CLASE.md).

### Lóbulo de Roche

- El lóbulo de Roche de una estrella es la región encerrada por la equipotencial que pasa por L1.

💡 **Cómo se explica en la clase [B24-C22](../programa/clases/B24/B24-C22-evolucion-binaria-lobulo-de-roche-y-transferencia-de-masa/CLASE.md):**
- *Descripción textual:* con las masas y el semieje se obtiene el lóbulo de Roche; si el radio de la estrella llega al del lóbulo, la masa fluye por L1 y cambia las masas y la órbita.
- Los códigos de evolución, como MESA, ya incluyen el desbordamiento del lóbulo de Roche entre sus casos de demostración (S5, resumen).
- 🎯 **Por qué importa:** Una estrella que se expande (C16) o se hincha en una binaria puede llenar la región donde su gravedad domina y verter gas sobre su compañera. Esa transferencia cambia las masas, la órbita y el destino de ambas, y es el camino hacia muchos objetos exóticos.

📘 **Dónde se aprende** (1 clase): [B24-C22 · Evolución binaria: lóbulo de Roche y transferencia de masa](../programa/clases/B24/B24-C22-evolucion-binaria-lobulo-de-roche-y-transferencia-de-masa/CLASE.md).

### Lóbulo lateral

- Un lóbulo lateral es un máximo secundario.
- El lóbulo lateral es un máximo secundario.
- Un lóbulo lateral es una respuesta fuera del haz principal.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B46-C16](../programa/clases/B46/B46-C16-sintesis-de-apertura/CLASE.md):**
- Además `λ/B_max = 72,2` arcsec y el mayor lóbulo lateral a más de 80 arcsec vale `0,140`.
- 🎯 **Por qué importa:** Un interferómetro con pocas antenas solo muestrea unos puntos del plano `uv`; la rotación de la Tierra los multiplica. La decisión central: ¿qué cobertura `uv` y qué haz sucio da una disposición de antenas?

📘 **Dónde se aprende** (4 clases): [B46-C04 · Diagramas de radiación](../programa/clases/B46/B46-C04-diagramas-de-radiacion/CLASE.md); [B46-C16 · Síntesis de apertura](../programa/clases/B46/B46-C16-sintesis-de-apertura/CLASE.md); [B49-C04 · Arreglos de antenas: factor de arreglo y formación de haz](../programa/clases/B49/B49-C04-arreglos-de-antenas-factor-de-arreglo-y-formacion-de-haz/CLASE.md); [B118-C17 · Interferencia radioastronómica](../programa/clases/B118/B118-C17-interferencia-radioastronomica/CLASE.md).

### Local

- El alcance (*scope*) es la región donde un nombre existe: una variable creada dentro de la función es local.

💡 **Cómo se explica en la clase [B07-C06](../programa/clases/B07/B07-C06-funciones-y-modularidad/CLASE.md):**
- Un nombre asignado dentro de una función es local: no altera uno del mismo nombre afuera.
- 🎯 **Por qué importa:** Copiar y pegar el mismo cálculo en cinco sitios es la forma más rápida de tener cinco versiones distintas y un error corregido solo en una. Una función concentra la lógica en un lugar, le da un nombre que expresa su intención y permite probarla aislada.

📘 **Dónde se aprende** (1 clase): [B07-C06 · Funciones y modularidad](../programa/clases/B07/B07-C06-funciones-y-modularidad/CLASE.md).

### Locales

- Casi todas las operaciones de Git son locales, así que funcionan sin red (S2).

🎯 **Por qué importa (clase B07-C14):** Sin control de versiones, un proyecto científico acumula archivos como `analisis_final.py`, `analisis_final2.py` y `analisis_final_ahora_si.py`, y nadie sabe cuál produjo la figura del artículo. Con Git, cada estado importante queda guardado con un mensaje, una fecha y un autor, y puedes comparar o recuperar cualquier versión.

📘 **Dónde se aprende** (1 clase): [B07-C14 · Control de versiones con Git](../programa/clases/B07/B07-C14-control-de-versiones-con-git/CLASE.md).

### Localidad espacial

- La localidad espacial es acceder a datos vecinos; la temporal, repetir el acceso a un mismo dato.

💡 **Cómo se explica en la clase [B18-C03](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md):**
- La caché aprovecha dos hechos: lo que acabas de usar probablemente lo usarás de nuevo (localidad temporal) y lo vecino a lo que usaste probablemente se use pronto (localidad espacial).
- 🎯 **Por qué importa:** Un catálogo con millones de estrellas o una rejilla de simulación pasan cada dato por la CPU una o pocas veces. Cuando las operaciones por dato son pocas, el tiempo no lo fija la CPU sino el viaje de los datos.

📘 **Dónde se aprende** (1 clase): [B18-C03 · Jerarquía y estructuras de memoria](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md).

### Localización

- La localización es la estimación de la posición del origen.

🎯 **Por qué importa (clase B114-C02):** Una fuga pequeña no suena ni se ve, pero decide cuántos días quedan para actuar. La decisión central: ¿con qué rapidez pierde presión el hábitat y dónde está el origen?

📘 **Dónde se aprende** (1 clase): [B114-C02 · Detección, localización y respuesta a fugas de presión](../programa/clases/B114/B114-C02-deteccion-localizacion-y-respuesta-a-fugas-de-presion/CLASE.md).

### Localizador de errores

- El localizador de errores `Λ(x)` tiene por raíces los inversos de las posiciones erróneas.

🎯 **Por qué importa (clase B94-C01):** Un enlace profundo opera con relaciones señal-ruido bajas y no puede reenviar cada trama. La decisión central: ¿cuántos símbolos erróneos tolera una palabra de código, cuánta redundancia cuesta y qué ocurre cuando se supera esa capacidad?

📘 **Dónde se aprende** (1 clase): [B94-C01 · Códigos Reed-Solomon y LDPC](../programa/clases/B94/B94-C01-codigos-reed-solomon-y-ldpc/CLASE.md).

### Lockstep

- El lockstep ejecuta dos copias con el mismo reloj y entradas.

💡 **Cómo se explica en la clase [B88-C25](../programa/clases/B88/B88-C25-redundancia-de-procesamiento-y-ejecucion-en-paralelo-lockstep/CLASE.md):**
- Lockstep no cubre causas comunes (reloj, alimentación, error de diseño).
- ⚠️ **Error frecuente:** Creer que lockstep corrige. Solo detecta (ejercicio 9)
- 🎯 **Por qué importa:** Lockstep detecta fallos transitorios de un núcleo, pero no los corrige ni cubre causas comunes. La decisión central: ¿cada cuántos ciclos comparar, y qué fallas escapan?

📘 **Dónde se aprende** (1 clase): [B88-C25 · Redundancia de procesamiento y ejecución en paralelo (lockstep)](../programa/clases/B88/B88-C25-redundancia-de-procesamiento-y-ejecucion-en-paralelo-lockstep/CLASE.md).

### LOD

- El LOD es `3 s` y el LOQ `10 s`, con `s` la desviación del blanco.

💡 **Cómo se explica en la clase [B55-C18](../programa/clases/B55/B55-C18-contaminacion-de-muestras/CLASE.md):**
- Con `s = 1 ng` la neta apenas iguala el LOD.
- Siempre se propaga la incertidumbre y se informa el LOD.
- ⚠️ **Error frecuente:** Informar un valor bajo el LOD como medición. Se informa «< LOD» (trans. 1).
- 🎯 **Por qué importa:** En muestras extraterrestres la cantidad buscada puede ser del orden de la contaminación que entra al manipularlas. La decisión central: ¿la señal neta supera el límite de detección y con qué incertidumbre, una vez restado el blanco?

📘 **Dónde se aprende** (1 clase): [B55-C18 · Contaminación de muestras](../programa/clases/B55/B55-C18-contaminacion-de-muestras/CLASE.md).

### Logarítmica

- Una escala de un eje indica cuánto vale cada marca; en una escala logarítmica cada marca multiplica por un factor fijo (B01-C02).
- La escala logarítmica es `log₁₀(Z/Z☉)`, en dex.

💡 **Cómo se explica en la clase [B04-C04](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md):**
- Antes de interpretar, lee: ¿qué magnitud hay en cada eje, con qué unidad, con qué escala (lineal o logarítmica), y desde dónde empieza el eje?
- 🎯 **Por qué importa:** Un astrónomo no solo calcula un valor: pregunta «¿qué pasa con el periodo de un planeta si su órbita es el doble de grande?». Responderlo con un solo caso no basta; hace falta la regla que liga ambas magnitudes.

📘 **Dónde se aprende** (2 clases): [B04-C04 · Funciones y gráficas](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md); [B25-C17 · Metalicidad y evolución química](../programa/clases/B25/B25-C17-metallicidad-y-evolucion-quimica/CLASE.md).

### Logaritmo decimal

- El logaritmo decimal `log₁₀(x)` es el exponente al que hay que elevar 10 para obtener `x`: `log₁₀(1000) = 3`.
- El logaritmo decimal usa `b = 10`; el natural, `ln`, usa `b = e`.

💡 **Cómo se explica en la clase [B04-C05](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md):**
- El logaritmo decimal del flujo (`log f`) es más natural en gráficos científicos modernos.
- 🎯 **Por qué importa:** El ojo y los instrumentos comparan brillos que difieren en factores de un millón. Los astrónomos lo resuelven con una escala logarítmica: la magnitud.

📘 **Dónde se aprende** (2 clases): [B01-C02 · Escalas desde la Tierra al cosmos observable](../programa/clases/B01/B01-C02-escalas-desde-la-tierra-al-cosmos-observable/CLASE.md); [B04-C05 · Funciones exponenciales y logarítmicas](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md).

### Logaritmo decimal de la luminosidad

- El logaritmo decimal de la luminosidad (`log L`) expresa `L` en potencias de diez respecto del Sol.

🎯 **Por qué importa (clase B01-C14):** Dos estrellas pueden verse igual de brillantes y ser totalmente distintas: una pequeña y cercana, otra enorme y lejana (C09). Para saber cómo es una estrella necesitas separar lo que ves (flujo) de lo que ella es (luminosidad, temperatura, radio) y de dónde está (distancia).

📘 **Dónde se aprende** (1 clase): [B01-C14 · Estrellas y sus principales propiedades](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md).

### Logaritmo en base b

- El logaritmo en base `b` es el exponente al que hay que elevar `b` para obtener el número: `log_b(y) = x` significa `bˣ = y`.

🎯 **Por qué importa (clase B04-C05):** El ojo y los instrumentos comparan brillos que difieren en factores de un millón. Los astrónomos lo resuelven con una escala logarítmica: la magnitud.

📘 **Dónde se aprende** (1 clase): [B04-C05 · Funciones exponenciales y logarítmicas](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md).

### Logaritmo en base diez

- El logaritmo en base diez de `x`, `log₁₀ x`, es el exponente al que hay que elevar 10 para obtener `x`: `log₁₀ 1000 = 3`.

🎯 **Por qué importa (clase B03-C05):** Las fichas de la NASA publican las masas en «10²⁴ kg»: la Tierra es 5,9722, el Sol 1 988 400. Si no sabes leer ese `10²⁴`, tampoco sabrás si 1 988 400 es «un poco más» o «mucho más».

📘 **Dónde se aprende** (1 clase): [B03-C05 · Notación científica y órdenes de magnitud](../programa/clases/B03/B03-C05-notacion-cientifica-y-ordenes-de-magnitud/CLASE.md).

### Logística

- Una función fija no depende del número de tripulantes; una lineal crece con él; una por pares crece por cada dos tripulantes; una logística crece con tripulantes por días.

💡 **Cómo se explica en la clase [B109-C05](../programa/clases/B109/B109-C05-crecimiento-modular-y-escalabilidad-de-asentamientos/CLASE.md):**
- Logística: sistemas y almacenamiento, proporcional a `N × días/(2 × 30)`.
- Como la fase 3 añade `60` días, la logística crece (`5,79 → 23,16 m²`) aunque la tripulación no cambie.
- ⚠️ **Error frecuente:** Olvidar la logística de una estancia más larga. Se corrige con 8.4.
- 🎯 **Por qué importa:** Si el primer módulo no admite ampliación, crecer obliga a desechar lo construido. La decisión central: ¿qué funciones se duplican con la tripulación, cuáles no, y cómo se añaden módulos sin rediseñar?

📘 **Dónde se aprende** (1 clase): [B109-C05 · Crecimiento modular y escalabilidad de asentamientos](../programa/clases/B109/B109-C05-crecimiento-modular-y-escalabilidad-de-asentamientos/CLASE.md).

### Lognormal

- Clase de calidad: categoría por umbrales. Lognormal: logaritmo normal.

💡 **Cómo se explica en la clase [B48-C11](../programa/clases/B48/B48-C11-calidad-y-clasificacion-de-datos/CLASE.md):**
- S["seeing ~ lognormal"] --> F["F(s) = Phi((ln s - ln m)/sigma)"]
- 🎯 **Por qué importa:** Un programa que exige la mejor calidad espera mucho; uno que acepta cualquiera desperdicia las buenas noches. La decisión central: ¿con qué frecuencia se da cada clase y cuánto hay que esperar?

📘 **Dónde se aprende** (1 clase): [B48-C11 · Calidad y clasificación de datos](../programa/clases/B48/B48-C11-calidad-y-clasificacion-de-datos/CLASE.md).

### Log-odds

- Los log-odds son `ln[p/(1 − p)]`.
- Rejilla de ocupación: malla de celdas con probabilidad de estar ocupadas (F5). Log-odds: `L = ln(p/(1−p))`; la actualización es una suma (F5).

💡 **Cómo se explica en la clase [B56-C19](../programa/clases/B56/B56-C19-etica-del-descubrimiento-de-vida/CLASE.md):**
- *Descripción textual:* se suman los logaritmos de las razones de verosimilitud a los log-odds de la previa, se obtiene la posterior y se compara con los umbrales.
- Log-odds con umbrales (esta clase): explícito.
- 🎯 **Por qué importa:** Anunciar demasiado pronto un hallazgo puede dañar la ciencia y la confianza pública; ocultarlo puede dañar la transparencia. Hace falta una forma explícita de saber cuánta evidencia hay.

📘 **Dónde se aprende** (2 clases): [B56-C19 · Ética del descubrimiento de vida](../programa/clases/B56/B56-C19-etica-del-descubrimiento-de-vida/CLASE.md); [B99-C05 · Mapas de ocupación y rejillas de elevación](../programa/clases/B99/B99-C05-mapas-de-ocupacion-y-rejillas-de-elevacion/CLASE.md).

### Log-parábola

- La log-parábola `log(νF_ν) = a + bx + cx²`, con `x = log ν`.

💡 **Cómo se explica en la clase [B27-C20](../programa/clases/B27/B27-C20-analisis-multibanda-de-evento-extremo/CLASE.md):**
- SED["SED sintética + ruido"] --> LP["ajuste log-parábola por joroba"]
- 🎯 **Por qué importa:** El caso de GW170817 con GRB 170817A mostró el valor de combinar mensajeros y bandas. La decisión central: ¿dónde están los picos de las dos jorobas y qué retardo hay entre dos bandas?

📘 **Dónde se aprende** (1 clase): [B27-C20 · Análisis multibanda de un evento extremo](../programa/clases/B27/B27-C20-analisis-multibanda-de-evento-extremo/CLASE.md).

### Log-verosimilitud

- La verosimilitud `L(θ)` es la probabilidad (o densidad) de los datos observados vista como función del parámetro `θ`; la log-verosimilitud `ℓ(θ) = ln L(θ)` convierte productos en sumas.
- Peso: influencia de cada voto. Log-verosimilitud: `ln(p/(1−p))`, peso óptimo bajo independencia.

💡 **Cómo se explica en la clase [B12-C07](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md):**
- *Descripción textual:* de los datos y del modelo se construye la log-verosimilitud; su máximo es el estimador y su curvatura da el error típico; la calidad del estimador se valida repitiendo el experimento muchas veces.
- Paso 2 · Log-verosimilitud. `ℓ(λ) = 37 ln λ − 10 λ − Σ ln kᵢ!`.
- 🎯 **Por qué importa:** Una misión no «conoce» la tasa de impactos ni el ruido de su sensor: los estima a partir de unas decenas de datos. Un estimador mal elegido, o mal interpretado, da parámetros sesgados o con una confianza injustificada.

📘 **Dónde se aprende** (2 clases): [B12-C07 · Estimación de parámetros](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md); [B48-C19 · Divulgación y ciencia ciudadana](../programa/clases/B48/B48-C19-divulgacion-y-ciencia-ciudadana/CLASE.md).

### Longitud

- La latitud geodésica `φ` es el ángulo de la normal al elipsoide con el plano ecuatorial; la longitud `λ`, el ángulo desde el meridiano origen; la altura elipsoidal `h`, la distancia a lo largo de la normal.
- La latitud `φ` va de −90° (sur) a +90° (norte) y la longitud `λ` crece hacia el este.

💡 **Cómo se explica en la clase [B04-C16](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md):**
- *Descripción textual:* de dos puntos dados por latitud y longitud se obtienen dos caminos: el del coseno, igual al producto escalar de los vectores unitarios, y el del haversine; ambos dan la distancia angular `c`, que multiplicada por el radio da la distancia en longitud; el primero pierde precisión para `c` pequeño y el segundo no.
- 🎯 **Por qué importa:** Para pasar de un lugar a otro de la Tierra, un avión sigue (casi) un círculo máximo. Para decidir cuánto debe girar un telescopio entre dos estrellas, se calcula la distancia angular sobre la esfera celeste.

📘 **Dónde se aprende** (2 clases): [B04-C16 · Geometría de esferas y círculos máximos](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md); [B13-C11 · Sistemas de referencia terrestres](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md).

### Longitud de arco

- La longitud de arco de `y = f(x)` es `∫ √(1 + f′²) dx`; el área de una superficie de revolución es `∫ 2π r ds`, con `ds = √(1 + z′²) dr`.

🎯 **Por qué importa (clase B09-C13):** Un telescopio necesita un espejo con forma de paraboloide. Cuánto vidrio hay que retirar de un disco plano para darle forma, cuánto pesa, y cuánta superficie hay que aluminizar son preguntas de volumen y área.

📘 **Dónde se aprende** (1 clase): [B09-C13 · Áreas y volúmenes por integración](../programa/clases/B09/B09-C13-areas-y-volumenes-por-integracion/CLASE.md).

### Longitud de atenuación

- La longitud de atenuación `λ` es la masa por área que reduce la dosis en un factor `e`.
- La longitud de atenuación `L` es la densidad areal que reduce la dosis en un factor `e`.

🎯 **Por qué importa (clase B33-C08):** La altitud y la profundidad atmosférica determinan cuánta radiación llega. La decisión central: ¿cuánto menos atmósfera hay a la altitud de vuelo?

📘 **Dónde se aprende** (3 clases): [B33-C08 · Dosis de radiación en aviación](../programa/clases/B33/B33-C08-dosis-de-radiacion-en-aviacion/CLASE.md); [B59-C11 · Construcción con regolito](../programa/clases/B59/B59-C11-construccion-con-regolito/CLASE.md); [B114-C04 · Refugio contra tormentas solares y compartimentos de protección](../programa/clases/B114/B114-C04-refugio-contra-tormentas-solares-y-compartimentos-de-proteccion/CLASE.md).

### Longitud de coherencia

- La longitud de coherencia `L = 1/σ_k`.

💡 **Cómo se explica en la clase [B42-C03](../programa/clases/B42/B42-C03-interferencia-y-coherencia/CLASE.md):**
- Como un grupo de corredores que parte junto: al principio van acompasados y luego se desfasan; la longitud de coherencia es el tramo en que aún van en grupo.
- Paso 4 · Lectura. A la longitud de coherencia queda el 61 % del contraste.
- 🎯 **Por qué importa:** Sin coherencia no hay franjas: una fuente ancha en frecuencia o en tamaño borra la interferencia. La decisión central: ¿hasta qué diferencia de camino se ven franjas con una fuente de ancho espectral dado?

📘 **Dónde se aprende** (1 clase): [B42-C03 · Interferencia y coherencia](../programa/clases/B42/B42-C03-interferencia-y-coherencia/CLASE.md).

### Longitud de Compton

- La longitud de Compton `h/(mc)`.

🎯 **Por qué importa (clase B31-C09):** Saber qué interacción domina en cada escala explica por qué los núcleos, los átomos y las estrellas son como son. La decisión central: ¿cuánto más fuerte es la fuerza eléctrica que la gravitatoria y qué fija el alcance de una fuerza?

📘 **Dónde se aprende** (1 clase): [B31-C09 · Interacciones fundamentales](../programa/clases/B31/B31-C09-interacciones-fundamentales/CLASE.md).

### Longitud de de Broglie

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B31-C17):** Una curva plana sin halo es inexplicable con la materia visible; cada candidato predice una escala distinta. La decisión central: ¿qué distingue la curva de rotación con halo y qué escalas predicen los candidatos?

📘 **Dónde se aprende** (1 clase): [B31-C17 · Materias oscuras candidatas](../programa/clases/B31/B31-C17-materias-oscuras-candidatas/CLASE.md).

### Longitud de Debye

- La longitud de Debye es la escala de apantallamiento.
- La longitud de Debye `λ_D` es la escala de apantallamiento.
- La longitud de Debye `λ_D = √(ε₀ k T_e/(n e²))` es la escala de apantallamiento de la carga.

💡 **Cómo se explica en la clase [B30-C07](../programa/clases/B30/B30-C07-longitud-de-debye-y-plasma/CLASE.md):**
- *Descripción textual:* la densidad y la temperatura dan la longitud de Debye, de la que salen el número de partículas, el potencial apantallado y la carga inducida.
- Con entornos ilustrativos (viento solar a 1 au: `5 × 10⁶ m⁻³` y `10⁵ K`; corona: `10¹⁵ m⁻³` y `1,5 × 10⁶ K`; ionosfera F: `10¹² m⁻³` y `1500 K`; laboratorio: `10¹⁸ m⁻³` y `10⁵ K`), la longitud de Debye va de `22 μm` a `9,76 m`.
- 🎯 **Por qué importa:** Sin apantallamiento no hay plasma, y sin muchas partículas en la esfera de Debye no hay comportamiento colectivo. La decisión central: ¿cuándo un gas ionizado es un plasma?

📘 **Dónde se aprende** (4 clases): [B30-C07 · Longitud de Debye y plasma](../programa/clases/B30/B30-C07-longitud-de-debye-y-plasma/CLASE.md); [B35-C04 · Colisiones, régimen cinético y ecuación de Vlasov](../programa/clases/B35/B35-C04-colisiones-regimen-cinetico-y-ecuacion-de-vlasov/CLASE.md); [B47-C24 · Instrumentos de plasma y campos in situ](../programa/clases/B47/B47-C24-instrumentos-de-plasma-y-campos-in-situ/CLASE.md); [B78-C09 · Propulsión por plasma](../programa/clases/B78/B78-C09-propulsion-por-plasma/CLASE.md).

### Longitud de escala

- Un proceso gaussiano es un modelo que para cada entrada da una distribución normal; su núcleo (*kernel*) define cuánto se parecen las salidas de dos entradas cercanas, y el de base radial (RBF) tiene una longitud de escala por variable (S1).

🎯 **Por qué importa (clase B17-C04):** Un simulador de trayectoria, de aerodinámica o de transporte de radiación puede tardar minutos u horas por ejecución. Para explorar miles de combinaciones de parámetros (un análisis de sensibilidad, una propagación de incertidumbre, una optimización) no alcanza el tiempo.

📘 **Dónde se aprende** (1 clase): [B17-C04 · Modelos sustitutos (surrogates)](../programa/clases/B17/B17-C04-modelos-sustitutos-surrogates/CLASE.md).

### Longitud de Jeans

- La longitud de Jeans `λ_J` es la escala por encima de la cual la gravedad vence a la presión.

🎯 **Por qué importa (clase B24-C01):** Toda estrella es un trozo de gas interestelar que se contrajo. Sin saber cuándo la gravedad vence a la presión no se entiende por qué las estrellas nacen en nubes frías y densas y no en el gas tenue del medio interestelar, ni por qué la masa de las estrellas depende del entorno.

📘 **Dónde se aprende** (1 clase): [B24-C01 · Colapso de nubes moleculares](../programa/clases/B24/B24-C01-colapso-de-nubes-moleculares/CLASE.md).

### Longitud de mezcla

- La longitud de mezcla `l = α H_P` es lo que recorre una burbuja antes de disolverse.

💡 **Cómo se explica en la clase [B37-C01](../programa/clases/B37/B37-C01-conveccion-longitud-de-mezcla-y-criterios-de-schwarzschild-y-ledoux/CLASE.md):**
- Para `ρ = 10 kg/m³`, `α = 1,0; 1,8; 2,5` dan `∇ − ∇_ad = 1,609 × 10⁻⁵; 7,347 × 10⁻⁶; 4,741 × 10⁻⁶`: una longitud de mezcla mayor transporta el mismo flujo con menos exceso de gradiente.
- La forma de la longitud de mezcla es una simplificación con coeficientes de orden unidad sin calibrar.
- 🎯 **Por qué importa:** Sin convección, un modelo de interior calcularía temperaturas imposibles en las capas inestables. La decisión central: ¿la capa es estable, y si no lo es, qué gradiente real `∇` y qué fracción del flujo lleva la convección?

📘 **Dónde se aprende** (1 clase): [B37-C01 · Convección: longitud de mezcla y criterios de Schwarzschild y Ledoux](../programa/clases/B37/B37-C01-conveccion-longitud-de-mezcla-y-criterios-de-schwarzschild-y-ledoux/CLASE.md).

### Longitud de onda

- La longitud de onda `λ` es la distancia entre dos crestas de la onda; la frecuencia `ν`, cuántas pasan por segundo; se relacionan con `c = λ·ν`.
- La longitud de onda `λ` es la distancia entre dos puntos iguales consecutivos (m); la frecuencia `f` (Hz) es el número de ciclos por segundo en un punto; la velocidad de propagación `v` cumple `v = f λ`.
- La longitud de onda `λ = c/f` es la distancia entre crestas.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C09](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md):**
- En su página de luz visible indica que el ojo detecta típicamente longitudes de onda de 380 a 700 nm, que los objetos más calientes emiten más luz de longitud de onda corta, y que el Sol, a unos 5 500 °C, se ve amarillo, una estrella de unos 3 000 °C se vería rojiza y una de 12 000 °C, azul (S2).
- ⚠️ **Error frecuente:** Usar la longitud de onda observada como denominador de `z`. Ejercicio 1.
- 🎯 **Por qué importa:** Sobre una galaxia a 43 Mpc solo tienes luz. De esa luz sale su dirección, cuánto brilla, de qué color es y qué líneas aparecen en su espectro; de las líneas sale `z = 0,0101` (C01).

📖 **Explicado a fondo:** [Longitud de onda y frecuencia](esencial/esencial-d-l.md#longitud-de-onda-y-frecuencia) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (4 clases): [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B05-C12 · Ondas mecánicas y frecuencia](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md); [B14-C22 · Acceso a datos heliofísicos abiertos con SunPy](../programa/clases/B14/B14-C22-acceso-a-datos-heliofisicos-abiertos-con-sunpy/CLASE.md); [B89-C01 · Electromagnetismo aplicado a enlaces](../programa/clases/B89/B89-C01-electromagnetismo-aplicado-a-enlaces/CLASE.md).

### Longitud de onda de corte

- La longitud de onda de corte `λ_c = hc/E_g`.

🎯 **Por qué importa (clase B44-C01):** Todo lo que mide un detector parte de un fotón que cede su energía a un electrón. La decisión central: ¿qué fotones puede registrar un material y con qué fluctuación mínima?

📘 **Dónde se aprende** (1 clase): [B44-C01 · Principios fotoeléctricos](../programa/clases/B44/B44-C01-principios-fotoelectricos/CLASE.md).

### Longitud de onda de de Broglie

- La longitud de onda de de Broglie `λ = h/p`.

🎯 **Por qué importa (clase B31-C01):** Sin la dualidad no se entiende la difracción de electrones, los microscopios electrónicos ni la estructura atómica. La decisión central: ¿cuándo importa la longitud de onda de un objeto y cómo se ve en un experimento?

📘 **Dónde se aprende** (1 clase): [B31-C01 · Dualidad onda-partícula](../programa/clases/B31/B31-C01-dualidad-onda-particula/CLASE.md).

### Longitud de onda de pivote

- La longitud de onda de pivote `λ_p² = ∫Tλ dλ / ∫T/λ dλ` no depende de la fuente.

🎯 **Por qué importa (clase B45-C03):** Una banda se describe por su curva completa, no por dos números. La decisión central: ¿cómo se combinan las curvas y qué longitud de onda se asigna a una banda?

📘 **Dónde se aprende** (1 clase): [B45-C03 · Curvas de transmisión](../programa/clases/B45/B45-C03-curvas-de-transmision/CLASE.md).

### Longitud de onda de reposo

- La longitud de onda de reposo `λ_reposo` es la medida en el laboratorio, con la fuente en reposo; la observada, `λ_obs`, es la que llega.

💡 **Cómo se explica en la clase [B06-C17](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md):**
- Si comparas una longitud de onda de reposo en el vacío (656,470 nm para H-alfa) con una observada en aire, el corrimiento aparente se desplaza en `(656,470 − 656,281)/656,281 = 2,9 × 10⁻⁴`, es decir, unos 86 km/s: un error pequeño, pero sistemático y evitable.
- 🎯 **Por qué importa:** En B01-C01 estimaste la velocidad de una galaxia con una sola línea, H-alfa en 662,9 nm. Pero ¿cómo se sabe que esa línea es H-alfa y no otra?

📘 **Dónde se aprende** (1 clase): [B06-C17 · Espectros atómicos y moleculares](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md).

### Longitud de onda efectiva

- La longitud de onda efectiva `λ_eff = ∫λTS dλ / ∫TS dλ` depende de la fuente `S`.

🎯 **Por qué importa (clase B45-C03):** Una banda se describe por su curva completa, no por dos números. La decisión central: ¿cómo se combinan las curvas y qué longitud de onda se asigna a una banda?

📘 **Dónde se aprende** (1 clase): [B45-C03 · Curvas de transmisión](../programa/clases/B45/B45-C03-curvas-de-transmision/CLASE.md).

### Longitud de onda en aire

- La longitud de onda en aire es `λ_vacío/n_aire`.

🎯 **Por qué importa (clase B45-C10):** Las líneas de emisión identifican elementos y miden velocidad y flujo. La decisión central: ¿dónde está cada línea del hidrógeno y con qué precisión se mide su posición?

📘 **Dónde se aprende** (1 clase): [B45-C10 · Líneas de emisión](../programa/clases/B45/B45-C10-lineas-de-emision/CLASE.md).

### Longitud de onda umbral

- Un umbral es la energía mínima para un proceso (ionizar, evaporar, superar una barrera); dado un umbral `E_u`, la longitud de onda umbral es `λ_u = h c/E_u`, y sólo fotones con `λ ≤ λ_u` lo superan.

💡 **Cómo se explica en la clase [B06-C18](../programa/clases/B06/B06-C18-fotoquimica-y-radiacion/CLASE.md):**
- Paso 4 · Longitud de onda umbral. `1239,84/13,5984 = 91,175 nm`: para ionizar desde el nivel fundamental se necesita menos de 91,2 nm.
- 🎯 **Por qué importa:** El hidrógeno de una nube o de una atmósfera puede ser ionizado por un fotón de longitud de onda menor que 91,2 nm. Un fotón de Lyman-alfa (121,6 nm) no lo ioniza desde el estado fundamental, pero tiene 22 veces la energía necesaria para evaporar una molécula de agua.

📘 **Dónde se aprende** (1 clase): [B06-C18 · Fotoquímica y radiación](../programa/clases/B06/B06-C18-fotoquimica-y-radiacion/CLASE.md).

### Longitud de oscilación

- La longitud de oscilación `L_osc = 4πħcE/Δm²`.

💡 **Cómo se explica en la clase [B31-C11](../programa/clases/B31/B31-C11-neutrinos-y-oscilaciones/CLASE.md):**
- *Descripción textual:* las constantes dan el coeficiente, la fase y la probabilidad, de la que salen la longitud de oscilación, las detecciones y el promedio en energía.
- Con valores ilustrativos `sen²2θ = 1` y `Δm² = 2,5 × 10⁻³ eV²`, a 1 GeV el primer máximo de aparición está a `495,9 km` y la longitud de oscilación es `991,9 km`.
- 🎯 **Por qué importa:** Detectar neutrinos del Sol, la atmósfera y aceleradores exige saber cuánto oscilan. La decisión central: ¿cuál es la probabilidad de oscilación a cierta distancia y energía?

📘 **Dónde se aprende** (1 clase): [B31-C11 · Neutrinos y oscilaciones](../programa/clases/B31/B31-C11-neutrinos-y-oscilaciones/CLASE.md).

### Longitud de saltación

- La saltación es el transporte en saltos y la longitud de saltación su alcance típico.

💡 **Cómo se explica en la clase [B66-C03](../programa/clases/B66/B66-C03-procesos-eolicos-dunas-ripples-y-erosion-planetaria/CLASE.md):**
- *Descripción textual:* presión, temperatura y masa molar dan la densidad del gas; con ella, la gravedad y el grano sale el umbral, y de él el Shields y la longitud de saltación.
- 🎯 **Por qué importa:** Marte tiene dunas y una atmósfera cien veces menos densa que la terrestre; Venus, una atmósfera enorme y casi sin viento.

📘 **Dónde se aprende** (1 clase): [B66-C03 · Procesos eólicos: dunas, ripples y erosión planetaria](../programa/clases/B66/B66-C03-procesos-eolicos-dunas-ripples-y-erosion-planetaria/CLASE.md).

### Longitud de saturación

- La longitud de saturación es `t_r v/2`.

🎯 **Por qué importa (clase B93-C03):** El tronco no incluía reflexiones, diafonía ni temporización de señales. La decisión central: ¿cuánto se deforma una señal por una terminación mal adaptada, cuánto se acopla a la pista vecina y cuánto margen de reloj queda?

📘 **Dónde se aprende** (1 clase): [B93-C03 · Integridad de señal en electrónica embarcada](../programa/clases/B93/B93-C03-integridad-de-senal-en-electronica-embarcada/CLASE.md).

### Longitud de una curva

- La longitud de una curva es la integral de su rapidez métrica.

🎯 **Por qué importa (clase B39-C01):** Sin métrica no hay distancias ni tiempo propio. La decisión central: ¿qué representa la métrica y qué cantidades no cambian al cambiar de coordenadas?

📘 **Dónde se aprende** (1 clase): [B39-C01 · Variedades, tensor métrico y geometría diferencial](../programa/clases/B39/B39-C01-variedades-tensor-metrico-y-geometria-diferencial/CLASE.md).

### Longitud efectiva

- La longitud efectiva `L_E` es la longitud de trayecto lluvioso equivalente con lluvia uniforme.
- La longitud efectiva reúne la mitad de evaporador y condensador más la sección adiabática.

💡 **Cómo se explica en la clase [B91-C07](../programa/clases/B91/B91-C07-atenuacion-atmosferica-y-efectos-de-la-lluvia-en-enlaces/CLASE.md):**
- *Descripción textual:* la tasa de lluvia y la frecuencia dan la atenuación específica; la geometría del trayecto da la longitud lluviosa y los factores de reducción dan la longitud efectiva; el producto es la atenuación del `0,01 %`, que se escala a otros porcentajes y se convierte en ruido de cielo.
- Paso 3 · Longitud efectiva. `L_s = 3,4/sin 30° = 6,8 km`; con `r₀,₀₁` y `v₀,₀₁`, `L_E = 4,267 km`.
- 🎯 **Por qué importa:** En bandas altas la lluvia puede quitar decenas de dB durante una fracción pequeña del año. La decisión central: ¿qué margen reservar para una disponibilidad dada, y a partir de qué frecuencia deja de ser razonable un enlace sin reserva ni diversidad?

📘 **Dónde se aprende** (2 clases): [B85-C09 · Tubos de calor](../programa/clases/B85/B85-C09-tubos-de-calor/CLASE.md); [B91-C07 · Atenuación atmosférica y efectos de la lluvia en enlaces](../programa/clases/B91/B91-C07-atenuacion-atmosferica-y-efectos-de-la-lluvia-en-enlaces/CLASE.md).

### Longitud eléctrica

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B49-C02):** Una antena desadaptada devuelve potencia y empeora la sensibilidad. La decisión central: ¿cuánta potencia se refleja y cómo se adapta con un tramo de línea?

📘 **Dónde se aprende** (1 clase): [B49-C02 · Adaptación de impedancias y líneas de transmisión en antenas](../programa/clases/B49/B49-C02-adaptacion-de-impedancias-y-lineas-de-transmision-en-antenas/CLASE.md).

### Longitud este

- La longitud este de un lugar se suma al ERA para obtener el ángulo local.
- La longitud este crece hacia el este.

💡 **Cómo se explica en la clase [B13-C10](../programa/clases/B13/B13-C10-tiempo-sidereo-local-y-terrestre/CLASE.md):**
- El ángulo local es `θ = ERA + λ`, con `λ` la longitud este.
- B --> C["+ longitud este<br/>= ángulo local"]
- 🎯 **Por qué importa:** Un telescopio en el desierto debe saber cuándo un objeto pasa por su meridiano, que es cuando está más alto y se observa mejor. Esa hora no es la del reloj civil: el cielo se adelanta casi cuatro minutos cada día.

📘 **Dónde se aprende** (2 clases): [B13-C10 · Tiempo sidéreo local y terrestre](../programa/clases/B13/B13-C10-tiempo-sidereo-local-y-terrestre/CLASE.md); [B53-C05 · Sistemas de coordenadas lunares](../programa/clases/B53/B53-C05-sistemas-de-coordenadas-lunares/CLASE.md).

### Longitud media

- La longitud media `L(t)` crece linealmente con el tiempo.

🎯 **Por qué importa (clase B75-C03):** Una ventana de lanzamiento no es un capricho de calendario: es el instante en que la geometría de los dos planetas coincide con la de la elipse de transferencia. La decisión central: ¿en qué fechas se cumple la fase de salida y cuánto margen de días da una tolerancia angular?

📘 **Dónde se aprende** (1 clase): [B75-C03 · Ventanas de lanzamiento](../programa/clases/B75/B75-C03-ventanas-de-lanzamiento/CLASE.md).

### Longitud media de carrera

- La longitud media de carrera (ARL) es el número esperado de observaciones hasta la alarma: `ARL₀` sin cambio, `ARL₁` con cambio.

🎯 **Por qué importa (clase B104-C18):** Un seguimiento demasiado sensible cansa por falsas alarmas; uno insensible llega tarde. La decisión central: ¿qué umbral permite detectar un deterioro de una desviación estándar en unos 8 días sin que haya más de una falsa alarma al año?

📘 **Dónde se aprende** (1 clase): [B104-C18 · Aislamiento y convivencia](../programa/clases/B104/B104-C18-aislamiento-y-convivencia/CLASE.md).

### Longitud media en número

- La longitud media en número es `1/(1 − p)`.

🎯 **Por qué importa (clase B56-C21):** C03 trata el origen de autorreplicantes, pero ninguna clase trata la polimerización experimental y sus límites. Antes de que un replicador pueda copiarse, hay que formar cadenas lo bastante largas.

📘 **Dónde se aprende** (1 clase): [B56-C21 · Polimerización prebiótica experimental: oligómeros y condiciones de laboratorio](../programa/clases/B56/B56-C21-polimerizacion-prebiotica-experimental-oligomeros-y-condiciones-de-laboratorio/CLASE.md).

### Longitud propia

- La longitud propia `L₀` es la medida en el marco donde el objeto está en reposo.

💡 **Cómo se explica en la clase [B26-C03](../programa/clases/B26/B26-C03-dilatacion-temporal-y-contraccion/CLASE.md):**
- La distancia de `15 km` es la longitud propia en el marco del laboratorio.
- 🎯 **Por qué importa:** Los muones se producen en la alta atmósfera por rayos cósmicos, viven microsegundos y, sin embargo, llegan al suelo en cantidad. Los relojes de satélites de navegación se ajustan por el mismo efecto.

📘 **Dónde se aprende** (1 clase): [B26-C03 · Dilatación temporal y contracción](../programa/clases/B26/B26-C03-dilatacion-temporal-y-contraccion/CLASE.md).

### Longitudinal

- En una onda transversal, el medio se mueve perpendicular a la propagación (cuerda); en una longitudinal, paralelo (sonido).

🎯 **Por qué importa (clase B05-C12):** Un sensor de vibración a bordo de una nave registra 30 Hz cuando la estructura vibra a 130 Hz. Un trueno llega segundos después del rayo.

📘 **Dónde se aprende** (1 clase): [B05-C12 · Ondas mecánicas y frecuencia](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md).

### LOO

- La densidad predictiva logarítmica esperada (`elpd`) es la suma esperada de `log p(ỹ_i | y)` sobre datos futuros; mayor es mejor. LOO: `elpd_loo = Σ_i log p(y_i | y_{−i})`.

💡 **Cómo se explica en la clase [B19-C07](../programa/clases/B19/B19-C07-comparacion-de-modelos-bayesianos/CLASE.md):**
- LOO deja fuera `y_i`, ajusta con los otros `n − 1` datos y evalúa `log p(y_i | y_{−i})`.
- En este modelo normal, la posterior sin `y_i` es normal, y la predictiva es `N(m_{−i}, σ² + v_{−i})`: LOO exacto, sin aproximaciones.
- 🎯 **Por qué importa:** Miras 10 mediciones de la amplitud de una señal y el promedio es 0,57 con ruido conocido 1. ¿Hay señal (`μ ≠ 0`) o solo ruido (`μ = 0`)?

📘 **Dónde se aprende** (1 clase): [B19-C07 · Comparación de modelos bayesianos](../programa/clases/B19/B19-C07-comparacion-de-modelos-bayesianos/CLASE.md).

### LOQ

- El LOD es `3 s` y el LOQ `10 s`, con `s` la desviación del blanco.

💡 **Cómo se explica en la clase [B55-C18](../programa/clases/B55/B55-C18-contaminacion-de-muestras/CLASE.md):**
- Descripción larga: una recta con las marcas LOD en 1,5, neta en 3,0 y LOQ en 5,0; la neta cae entre el LOD y el LOQ.
- 🎯 **Por qué importa:** En muestras extraterrestres la cantidad buscada puede ser del orden de la contaminación que entra al manipularlas. La decisión central: ¿la señal neta supera el límite de detección y con qué incertidumbre, una vez restado el blanco?

📘 **Dónde se aprende** (1 clase): [B55-C18 · Contaminación de muestras](../programa/clases/B55/B55-C18-contaminacion-de-muestras/CLASE.md).

### Loss ratio

- El *loss ratio* es siniestros divididos por primas.

💡 **Cómo se explica en la clase [B127-C02](../programa/clases/B127/B127-C02-seguros-en-orbita/CLASE.md):**
- El informe de mercado de Gallagher «Space insurance market update Q1 2026» (10 de abril de 2026) señala que el *loss ratio* de suscripción de 2025 pasó de unos `15 %` a unos `75 %` tras un siniestro confirmado (SpainSat NG-2, asegurado por más de `400 MUSD`).
- 🎯 **Por qué importa:** La cobertura durante la vida en órbita difiere de la de lanzamiento y no estaba tratada. La decisión central: ¿cuánto debe costar cada año de cobertura si el riesgo baja con la edad pero el valor asegurado también?

📘 **Dónde se aprende** (1 clase): [B127-C02 · Seguros en órbita](../programa/clases/B127/B127-C02-seguros-en-orbita/CLASE.md).

### Lote

- Un lote es un conjunto de datos procesado de una vez.
- Un lote es la unidad de trazabilidad.
- Un lote es el conjunto de plantas que se siembra y se cosecha a la vez.

💡 **Cómo se explica en la clase [B14-C30](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md):**
- La clave de una etapa es el SHA-256 de `etapa | lote | huella de la entrada` (C11).
- Resultado del laboratorio: en la primera pasada se ejecutaron 17 etapas (4 lotes completos × 4 etapas, más la ingesta del lote 3); en la segunda pasada, 0 ejecutadas y 17 saltadas.
- ⚠️ **Error frecuente:** Dejar pasar un lote sin control de calidad. Se corrige con la sección 8.3 y el ejercicio 7.
- 🎯 **Por qué importa:** Cada madrugada llegan datos nuevos. Si un humano debe lanzar cada paso, tarde o temprano se olvida uno; si un lote corrupto atraviesa la cadena, contamina el producto final; si un fallo de red detiene todo y al reiniciar se repite desde cero, se pierde tiempo.

📘 **Dónde se aprende** (3 clases): [B14-C30 · Cadenas de procesamiento automatizado de datos](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md); [B100-C01 · Gestión de inventario de materias primas y piezas](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md); [B115-C05 · Ciclos de producción y calendarización de cultivos](../programa/clases/B115/B115-C05-ciclos-de-produccion-y-calendarizacion-de-cultivos/CLASE.md).

### LQR

- El LQR es la ley `u = −K x` que minimiza `C`; se obtiene con `K = R⁻¹ Bᵀ P`, donde `P` resuelve la ecuación algebraica de Riccati `AᵀP + PA − P B R⁻¹ Bᵀ P + Q = 0` (S2 la presenta como `X A + AᴴX − X B R⁻¹ Bᴴ X + Q = 0`).

💡 **Cómo se explica en la clase [B16-C15](../programa/clases/B16/B16-C15-control-optimo-lqr/CLASE.md):**
- LQR: con varias entradas y estados, define el compromiso con `Q` y `R`; requiere estado completo.
- MPC (B87-C21): como el LQR, pero con restricciones explícitas.
- ⚠️ **Error frecuente:** Creer que el LQR respeta el par máximo. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Con un PD hay dos perillas, `Kp` y `Kd`, y no es obvio cuánto esfuerzo gasta cada combinación. En un satélite el esfuerzo tiene un costo real: energía de las ruedas, momento almacenado, desgaste.

📘 **Dónde se aprende** (1 clase): [B16-C15 · Control óptimo LQR](../programa/clases/B16/B16-C15-control-optimo-lqr/CLASE.md).

### LSB

- El LSB `= Vref/2ⁿ`.
- El LSB de Q15 con escala 8 vale `8/32768 = 2,44×10⁻⁴`.
- Cuantización: discretización de la amplitud. LSB: escalón del cuantizador.

💡 **Cómo se explica en la clase [B88-C02](../programa/clases/B88/B88-C02-microcontroladores-embarcados/CLASE.md):**
- Con 12 bits y 3,3 V: `LSB = 0,8057 mV` y error de cuantización máximo `±0,4028 mV`. 1,000 V da el código 1241 (0,9998 V).
- A["Vref y bits"] --> L["LSB y cuantizacion"]
- 🎯 **Por qué importa:** Un error de configuración (un divisor mal calculado, una resolución insuficiente) no se ve en el escritorio y aparece en órbita. La decisión central: ¿qué valores de registro dan la temporización, la velocidad y la resolución que exige el requisito, con qué error?

📘 **Dónde se aprende** (3 clases): [B88-C02 · Microcontroladores embarcados](../programa/clases/B88/B88-C02-microcontroladores-embarcados/CLASE.md); [B88-C41 · Pruebas SIL y PIL del software de vuelo](../programa/clases/B88/B88-C41-pruebas-sil-y-pil-del-software-de-vuelo/CLASE.md); [B90-C23 · Instrumentación y adquisición de datos en ensayos](../programa/clases/B90/B90-C23-instrumentacion-y-adquisicion-de-datos-en-ensayos/CLASE.md).

### LSK

- Los tipos descritos por NAIF son SPK (posición y velocidad), CK (orientación de nave), PCK (tamaño, forma y orientación de cuerpos), IK (campo de visión de instrumentos), FK (marcos), LSK (segundos intercalares), SCLK (reloj de nave) y DSK (formas).

💡 **Cómo se explica en la clase [B74-C21](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md):**
- En el laboratorio se resuelven 6 archivos; todos existen y LSK y SCLK están antes que los SPK (las dos comprobaciones valen 1 = sí: `1` y `1`).
- Por tipo: SPK, CK, PCK, IK, FK, LSK, SCLK.
- 🎯 **Por qué importa:** Un resultado de navegación depende de qué kernels se cargaron y en qué orden: dos corridas con el mismo código pueden dar trayectorias distintas. La decisión central: ¿cómo declaro, valido y audito el conjunto de kernels de una solución para que sea reproducible?

📘 **Dónde se aprende** (1 clase): [B74-C21 · Kernels SPICE y su uso en navegación](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md).

### LS/LF

- ES/EF: inicio y fin tempranos. LS/LF: inicio y fin tardíos.

🎯 **Por qué importa (clase B96-C09):** Una secuencia que no cabe en la ventana deja comandos sin ejecutar o telemetría sin confirmar. La decisión central: ¿qué actividades fijan la duración mínima y cuánta holgura queda?

📘 **Dónde se aprende** (1 clase): [B96-C09 · Secuencias de misión](../programa/clases/B96/B96-C09-secuencias-de-mision/CLASE.md).

### LTAN

- La LTAN es la hora local del nodo ascendente.

💡 **Cómo se explica en la clase [B72-C13](../programa/clases/B72/B72-C13-orbitas-heliosincronicas/CLASE.md):**
- Por periodo y LTAN. Por altitud máxima. Por deriva: minutos por año por cada décima de grado.
- 🎯 **Por qué importa:** La misma hora local de paso significa la misma iluminación en cada imagen: es lo que usan las misiones de observación de la Tierra. La decisión central: ¿qué inclinación corresponde a cada altitud y cuánta deriva de hora local produce un error de inclinación?

📘 **Dónde se aprende** (1 clase): [B72-C13 · Órbitas heliosincrónicas](../programa/clases/B72/B72-C13-orbitas-heliosincronicas/CLASE.md).

### LTI

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B15-C08](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md):**
- X["Entrada x[n]<br/>= suma de impulsos<br/>escalados y retrasados"] --> S["Sistema LTI<br/>respuesta h[n]"]
- 🎯 **Por qué importa:** Un termistor a bordo de una nave no mide la temperatura del instante: mide una versión retrasada y suavizada, porque su cuerpo tarda en calentarse o enfriarse. Si la nave entra en eclipse y el entorno baja 50 K de golpe, el sensor irá bajando poco a poco.

📘 **Dónde se aprende** (1 clase): [B15-C08 · Convolución y respuesta impulsional](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md).

### LTV

- El LTV es el margen total que deja un cliente.
- El LTV es el margen total esperado de un cliente.

💡 **Cómo se explica en la clase [B125-C02](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md):**
- Con abandono `c`, la fracción viva tras `k` meses es `(1 − c)^k` y `LTV = Σ ARPU · margen · (1 − c)^k = ARPU · margen / c`.
- Con `ARPU = 1 000`, margen `0,70`, `c = 0,02`: `LTV = 35 000` (la serie simulada da `35 000`).
- ⚠️ **Error frecuente:** Calcular el `LTV` con `c` en lugar de `1/c` como vida media. Se corrige con 8.3.
- 🎯 **Por qué importa:** El modelo de ingresos define cuándo entra el dinero y cuánto vale un cliente; ninguna clase anterior lo trata. La decisión central: ¿cuánto vale un cliente de suscripción, cuándo se reconoce su ingreso y cuánto abandono puede tolerar el negocio?

📘 **Dónde se aprende** (2 clases): [B125-C02 · Modelos de ingresos: suscripción y servicio](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md); [B126-C04 · Costo de adquisición de clientes y economía unitaria](../programa/clases/B126/B126-C04-costo-de-adquisicion-de-clientes-y-economia-unitaria/CLASE.md).

### LU

- Una factorización (o descomposición) escribe `A` como producto de factores con estructura. LU: `P A = L U` con `L` triangular inferior de unos en la diagonal, `U` triangular superior y `P` una matriz de permutación (reordena filas) —es la eliminación gaussiana guardada—.

🎯 **Por qué importa (clase B10-C10):** Un filtro de navegación resuelve el mismo sistema con miles de lados derechos distintos; una simulación necesita muestras aleatorias con una covarianza dada; un ajuste de mínimos cuadrados quiere estabilidad. En cada caso el trabajo se hace una vez al factorizar y luego se reutiliza.

📘 **Dónde se aprende** (1 clase): [B10-C10 · Descomposiciones matriciales](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md).

### Lugar de las raíces

- El lugar de las raíces es el conjunto de raíces de `1 + K·P(s) = 0` (con `P` conocida) cuando `K` varía de 0 a ∞.

💡 **Cómo se explica en la clase [B16-C09](../programa/clases/B16/B16-C09-lugar-de-las-raices/CLASE.md):**
- El lugar de las raíces muestra polos y es ideal con un parámetro.
- 🎯 **Por qué importa:** Subir la ganancia de un lazo hace que responda más rápido, pero también más oscilante, hasta que se desestabiliza. Para decidir cuánta ganancia usar necesitas ver el compromiso de un vistazo.

📘 **Dónde se aprende** (1 clase): [B16-C09 · Lugar de las raíces](../programa/clases/B16/B16-C09-lugar-de-las-raices/CLASE.md).

### Luminancia relativa

- La luminancia relativa es `L = 0,2126 R + 0,7152 G + 0,0722 B` con cada canal sRGB linealizado.
- La luminancia relativa `L` es el brillo percibido de un color, de 0 (negro) a 1 (blanco).
- La luminancia relativa `L = 0,2126 R + 0,7152 G + 0,0722 B` se calcula con canales linealizados.

🎯 **Por qué importa (clase B116-C07):** Un panel que muestra «FC 72» sin decir de cuándo es, o que usa un gris que no se lee, puede ser peor que no tener panel. La decisión central: ¿qué debe mostrar un panel de salud para que quien lo mira sepa qué está pasando, cuán fresco es el dato y a quién atender primero?

📘 **Dónde se aprende** (3 clases): [B116-C07 · Diseño de paneles de monitoreo de salud](../programa/clases/B116/B116-C07-diseno-de-paneles-de-monitoreo-de-salud/CLASE.md); [B128-C06 · Contraste y color accesibles](../programa/clases/B128/B128-C06-contraste-y-color-accesibles/CLASE.md); [B130-C02 · Visualización de datos para comunicar](../programa/clases/B130/B130-C02-visualizacion-de-datos-para-comunicar/CLASE.md).

### Luminaria

- La luminaria es el conjunto de LED, controlador y óptica.

💡 **Cómo se explica en la clase [B115-C02](../programa/clases/B115/B115-C02-iluminacion-de-cultivos-con-led-y-espectro-de-crecimiento/CLASE.md):**
- Analogía: una luminaria de cultivo es un grifo de fotones: el caudal es el PPFD y el recibo de la luz depende de lo eficiente que sea el grifo.
- Una luminaria que cubre 1 m² con un flujo de 500 µmol m⁻² s⁻¹ durante 16 h entrega una DLI de 28,8 mol m⁻² d⁻¹.
- 🎯 **Por qué importa:** La luz es el mayor consumo eléctrico de un cultivo cerrado. La decisión central: ¿cuántos fotones por metro cuadrado y día hacen falta, con qué eficacia se producen y qué potencia y calor suponen para el hábitat?

📘 **Dónde se aprende** (1 clase): [B115-C02 · Iluminación de cultivos con LED y espectro de crecimiento](../programa/clases/B115/B115-C02-iluminacion-de-cultivos-con-led-y-espectro-de-crecimiento/CLASE.md).

### Luminosidad

- La luminosidad `L` es la energía total que emite por segundo (W).
- La irradiancia `f` es la potencia por unidad de área que llega (W/m²) y la luminosidad `L` la potencia total que emite (W).
- La luminosidad es la potencia total radiada.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C14](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md):**
- Piensa en un triángulo con vértices temperatura, radio y luminosidad: dos de ellos fijan el tercero por Stefan–Boltzmann.
- Aparte, la luminosidad y la distancia fijan el flujo por el cuadrado inverso; y la temperatura fija el color por Wien.
- ⚠️ **Error frecuente:** Confundir brillo con luminosidad. Ejercicio 11.
- 🎯 **Por qué importa:** Dos estrellas pueden verse igual de brillantes y ser totalmente distintas: una pequeña y cercana, otra enorme y lejana (C09). Para saber cómo es una estrella necesitas separar lo que ves (flujo) de lo que ella es (luminosidad, temperatura, radio) y de dónde está (distancia).

📖 **Explicado a fondo:** [Flujo y luminosidad](esencial/esencial-d-l.md#flujo-y-luminosidad) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (4 clases): [B01-C14 · Estrellas y sus principales propiedades](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md); [B04-C05 · Funciones exponenciales y logarítmicas](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md); [B09-C15 · Funciones de varias variables](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md); [B24-C03 · Diagrama de Hertzsprung-Russell](../programa/clases/B24/B24-C03-diagrama-de-hertzsprung-russell/CLASE.md).

### Luminosidad de acreción

- La luminosidad de acreción `L_acc` es la energía de caída que se irradia.

🎯 **Por qué importa (clase B24-C02):** Una protoestrella brilla, pero no por el motor que alimenta al Sol. Para saber de dónde sale su energía, cuánto tiempo puede brillar así y cómo distinguirla de una estrella ya estable hay que seguir la energía gravitatoria.

📘 **Dónde se aprende** (1 clase): [B24-C02 · Formación de protoestrellas](../programa/clases/B24/B24-C02-formacion-de-protoestrellas/CLASE.md).

### Luminosidad de Eddington

- La luminosidad de Eddington es la que equilibra la fuerza de radiación con la gravedad.
- La luminosidad de Eddington `L_Edd = 4πGMm_p c/σ_T` es aquella en que la fuerza de la radiación sobre los electrones iguala la atracción gravitatoria sobre los protones (`G` gravitación, `M` masa del agujero, `m_p` masa del protón, `c` velocidad de la luz, `σ_T` sección eficaz de Thomson).

💡 **Cómo se explica en la clase [B25-C11](../programa/clases/B25/B25-C11-nucleos-activos-de-galaxias/CLASE.md):**
- Luminosidad de Eddington: da un mínimo de masa para una luminosidad dada si el núcleo no supera su límite.
- ⚠️ **Error frecuente:** Confundir la luminosidad de Eddington con la luminosidad real. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Algunas galaxias tienen en el centro una fuente que supera a todas sus estrellas, y casi todas las galaxias grandes albergan un agujero negro supermasivo. Entender el AGN une el centro de la galaxia, su gas y su evolución.

📘 **Dónde se aprende** (3 clases): [B24-C09 · Atmósferas y opacidades](../programa/clases/B24/B24-C09-atmosferas-y-opacidades/CLASE.md); [B25-C11 · Núcleos activos de galaxias](../programa/clases/B25/B25-C11-nucleos-activos-de-galaxias/CLASE.md); [B27-C10 · Discos de acreción](../programa/clases/B27/B27-C10-discos-de-acrecion/CLASE.md).

### Luna llena

- La luna nueva ocurre cuando la Luna está entre la Tierra y el Sol (no se ve el lado iluminado); la luna llena, cuando la Tierra está entre la Luna y el Sol; los cuartos, cuando el ángulo Sol–Tierra–Luna es de 90°.

💡 **Cómo se explica en la clase [B01-C12](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md):**
- Con el Sol y la Luna del mismo lado, vemos el lado oscuro (luna nueva); con ángulo de 180°, el lado completo iluminado (luna llena).
- Desde una luna llena de partida, la siguiente es `+29,53 d`, y la `n`-ésima, `+n·29,53 d`.
- 🎯 **Por qué importa:** La Luna es el reloj más a mano del cielo: cada noche cambia, y cada 29,5 días vuelve a empezar. Pero «a mano» no significa «fácil de explicar»: muchas personas creen que las fases son la sombra de la Tierra sobre la Luna.

📘 **Dónde se aprende** (1 clase): [B01-C12 · Fases lunares y ciclos celestes](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md).

### Luna nueva

- La luna nueva ocurre cuando la Luna está entre la Tierra y el Sol (no se ve el lado iluminado); la luna llena, cuando la Tierra está entre la Luna y el Sol; los cuartos, cuando el ángulo Sol–Tierra–Luna es de 90°.

💡 **Cómo se explica en la clase [B01-C12](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md):**
- Con el Sol y la Luna del mismo lado, vemos el lado oscuro (luna nueva); con ángulo de 180°, el lado completo iluminado (luna llena).
- Eso significa que, en luna nueva o llena, la Luna suele quedar *arriba* o *abajo* de la línea Sol–Tierra.
- 🎯 **Por qué importa:** La Luna es el reloj más a mano del cielo: cada noche cambia, y cada 29,5 días vuelve a empezar. Pero «a mano» no significa «fácil de explicar»: muchas personas creen que las fases son la sombra de la Tierra sobre la Luna.

📘 **Dónde se aprende** (1 clase): [B01-C12 · Fases lunares y ciclos celestes](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md).

### Lunar

- Un eclipse solar ocurre cuando la Luna se interpone entre el Sol y la Tierra (Luna nueva); uno lunar, cuando la Tierra se interpone entre el Sol y la Luna (Luna llena).

💡 **Cómo se explica en la clase [B08-C09](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md):**
- La Luna (radio angular ≈ 0,26°) cabe en ella con holgura: por eso la Luna puede quedar completamente dentro de la umbra (la duración de la totalidad lunar no se consultó en esta clase).
- E --> L["Eclipse lunar:<br/>la Luna entra en la umbra"]
- 🎯 **Por qué importa:** Un eclipse solar es un fenómeno que reúne a miles de personas y que puede dejar ciegas a quienes lo miran mal. La pregunta motivadora: ¿qué tipo de eclipse ocurrirá, dónde y cómo lo veo sin dañarme?

📘 **Dónde se aprende** (1 clase): [B08-C09 · Eclipses y geometría de sombras](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md).

### Luz reflejada

- La luz reflejada es la del planeta iluminado.

💡 **Cómo se explica en la clase [B29-C06](../programa/clases/B29/B29-C06-imagen-directa-de-exoplanetas/CLASE.md):**
- Descripción larga: la emisión térmica en el infrarrojo medio es mucho más favorable que la luz reflejada para planetas terrestres.
- 🎯 **Por qué importa:** La imagen directa entrega espectros del planeta y la órbita completa, pero solo es posible con planetas jóvenes, calientes y lejanos de la estrella. La decisión central: ¿qué contraste y qué separación angular hay que alcanzar para ver un planeta dado?

📘 **Dónde se aprende** (1 clase): [B29-C06 · Imagen directa de exoplanetas](../programa/clases/B29/B29-C06-imagen-directa-de-exoplanetas/CLASE.md).

### Luz total

- La luz total es `L = 2π n e^{b_n} b_n^{−2n} Γ(2n) I_e R_e²`.

🎯 **Por qué importa (clase B25-C09):** Las galaxias parecen muy distintas: discos con brazos y gas, o bolas suaves de estrellas viejas. Esa diferencia guarda su historia (formación estelar, fusiones) y exige un lenguaje común para compararlas.

📘 **Dónde se aprende** (1 clase): [B25-C09 · Galaxias elípticas y espirales](../programa/clases/B25/B25-C09-galaxias-elipticas-y-espirales/CLASE.md).

### Lyman

- Una serie espectral es el conjunto de transiciones que terminan en el mismo nivel: la de Lyman termina en `n = 1` y la de Balmer en `n = 2`.

💡 **Cómo se explica en la clase [B06-C01](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md):**
- Si `n_bajo = 1`, la serie de Lyman, toda en el ultravioleta.
- 🎯 **Por qué importa:** Casi todo lo que sabemos de la composición de una estrella o de una nebulosa lo sabemos porque sus átomos emiten o absorben luz en colores muy precisos. Una línea roja a 656 nm no es «un color cualquiera»: es la firma del hidrógeno.

📘 **Dónde se aprende** (1 clase): [B06-C01 · Estructura atómica](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md).
