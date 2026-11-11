# Términos · H

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · **H** · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

### H⁻

- El H⁻ es el ion que domina en atmósferas frías.

🎯 **Por qué importa (clase B32-C03):** La opacidad fija la profundidad desde la que escapa la luz. La decisión central: ¿cómo se promedia una opacidad que depende de la frecuencia?

📘 **Dónde se aprende** (1 clase): [B32-C03 · Opacidad continua: ligado-libre, libre-libre y H-](../programa/clases/B32/B32-C03-opacidad-continua-ligado-libre-libre-libre-y-h/CLASE.md).

### Habituación

- La habituación es la disminución del pico con las exposiciones.

💡 **Cómo se explica en la clase [B113-C02](../programa/clases/B113/B113-C02-ansiedad-y-respuesta-emocional-en-escenarios-simulados/CLASE.md):**
- Por forma: habituación (`k > 0`) o sensibilización (`k < 0`).
- ⚠️ **Error frecuente:** Suponer que la habituación siempre ocurre. Se corrige con 8.4.
- 🎯 **Por qué importa:** Ninguna clase previa trata la respuesta emocional ante simulaciones de riesgo. La decisión central: ¿cuántas repeticiones de un escenario hacen falta para que el pico baje a un nivel de trabajo, y cuándo la repetición deja de ayudar?

📘 **Dónde se aprende** (1 clase): [B113-C02 · Ansiedad y respuesta emocional en escenarios simulados](../programa/clases/B113/B113-C02-ansiedad-y-respuesta-emocional-en-escenarios-simulados/CLASE.md).

### Hadrón

- Un hadrón como protón o pion.

🎯 **Por qué importa (clase B31-C10):** Antes de calcular una sección eficaz, una reacción debe respetar las leyes de conservación. La decisión central: ¿está permitida esta reacción por las reglas de conservación?

📘 **Dónde se aprende** (1 clase): [B31-C10 · Modelo estándar de partículas](../programa/clases/B31/B31-C10-modelo-estandar-de-particulas/CLASE.md).

### HAL

- La HAL es la interfaz.

💡 **Cómo se explica en la clase [B88-C24](../programa/clases/B88/B88-C24-capa-de-abstraccion-de-hardware-hal-y-controladores/CLASE.md):**
- APP["Aplicacion: enviar_paquete"] --> HAL["Interfaz HAL"]
- HAL --> R["Controlador de registros (FIFO 4)"]
- ⚠️ **Error frecuente:** Escribir registros en la aplicación. Usa la HAL (8.1)
- 🎯 **Por qué importa:** Si la aplicación toca registros, no se puede probar sin el hardware y cada cambio de componente la rompe. La decisión central: ¿qué interfaz mínima expone el dispositivo para que la aplicación no dependa de él?

📘 **Dónde se aprende** (1 clase): [B88-C24 · Capa de abstracción de hardware (HAL) y controladores](../programa/clases/B88/B88-C24-capa-de-abstraccion-de-hardware-hal-y-controladores/CLASE.md).

### Hallazgo

- Un hallazgo es una violación detectada.
- Un hallazgo es una excepción distinta del objetivo.

💡 **Cómo se explica en la clase [B88-C37](../programa/clases/B88/B88-C37-fuzzing-autorizado-de-software-embarcado-en-banco-de-pruebas/CLASE.md):**
- Parte de tres semillas válidas y conserva las entradas que abren ramas: `11,0/13` ramas, 2 errores distintos por campaña (20 en total) y primer hallazgo a las `40` ejecuciones.
- Paso 4 · Registro. Hallazgo guardado con la entrada.
- 🎯 **Por qué importa:** Las pruebas diseñadas por una persona no prevén todas las combinaciones. La decisión central: ¿qué estrategia de entradas encuentra más fallos con menos ejecuciones en un banco autorizado?

📘 **Dónde se aprende** (2 clases): [B88-C15 · Análisis estático de código](../programa/clases/B88/B88-C15-analisis-estatico-de-codigo/CLASE.md); [B88-C37 · Fuzzing autorizado de software embarcado en banco de pruebas](../programa/clases/B88/B88-C37-fuzzing-autorizado-de-software-embarcado-en-banco-de-pruebas/CLASE.md).

### Hallazgo mayor

- Un hallazgo mayor afecta un requisito crítico.

🎯 **Por qué importa (clase B88-C40):** No se puede revisar todo; se revisa una muestra. La decisión central: ¿qué tamaño de muestra da una probabilidad aceptable de detectar desviaciones y cómo se protege el registro de lo auditado?

📘 **Dónde se aprende** (1 clase): [B88-C40 · Auditoría de software espacial](../programa/clases/B88/B88-C40-auditoria-de-software-espacial/CLASE.md).

### Halley

- Newton: `x ← x − δ/T'`. Halley: `x ← x − 2δ T'/(2T'² − δ T'')`.

💡 **Cómo se explica en la clase [B82-C06](../programa/clases/B82/B82-C06-algoritmos-iterativos-para-lambert-gooding-izzo/CLASE.md):**
- De las razones de logaritmos, el orden aparente es ≈ 2 en Newton, ≈ 3 en Halley y mayor en Householder (el error llega al redondeo en un paso).
- TX --> P["paso Newton / Halley / Householder"]
- 🎯 **Por qué importa:** La velocidad de un solucionador importa cuando se evalúan millones de transferencias. La decisión central: ¿cuántas iteraciones necesita cada método, de qué depende, y qué garantiza el valor inicial?

📘 **Dónde se aprende** (1 clase): [B82-C06 · Algoritmos iterativos para Lambert (Gooding, Izzo)](../programa/clases/B82/B82-C06-algoritmos-iterativos-para-lambert-gooding-izzo/CLASE.md).

### Halo

- Un halo es la distribución, aproximadamente esférica, de esa materia alrededor de una galaxia.
- Un halo es una distribución casi esférica que envuelve la galaxia.
- Una halo es una familia periódica que sale del plano.

💡 **Cómo se explica en la clase [B25-C15](../programa/clases/B25/B25-C15-materia-oscura-en-galaxias/CLASE.md):**
- La densidad del halo en `R₀` resulta `0,0130 M☉/pc³`, dentro de la barra de `0,013 ± 0,003` que S4 cita para la densidad local de materia oscura.
- No evalúa explicaciones alternativas de las curvas de rotación (C08), no incluye la contracción del halo por los bariones, subestructura ni la forma triaxial.
- ⚠️ **Error frecuente:** Concluir que el halo prueba la materia oscura. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Varias medidas independientes (rotación, dispersión, lentes, fondo cósmico) piden más masa de la que se ve. Un halo con un perfil de densidad concreto permite comparar esas medidas entre sí y con las simulaciones.

📘 **Dónde se aprende** (3 clases): [B25-C15 · Materia oscura en galaxias](../programa/clases/B25/B25-C15-materia-oscura-en-galaxias/CLASE.md); [B26-C18 · Materia oscura y evidencias](../programa/clases/B26/B26-C18-materia-oscura-y-evidencias/CLASE.md); [B76-C04 · Órbitas halo](../programa/clases/B76/B76-C04-orbitas-halo/CLASE.md).

### Halo de materia oscura

- El halo estelar es la envoltura difusa de estrellas muy viejas, y el halo de materia oscura es la masa invisible que domina el potencial a gran radio (C15).

🎯 **Por qué importa (clase B25-C01):** Estamos dentro de la galaxia y no podemos fotografiarla desde fuera: su forma se reconstruye midiendo distancias y velocidades desde un punto que no es el centro. Sin un esquema claro de componentes (bulbo, barra, disco, halo) y de cifras de referencia, el resto del bloque carece de escala.

📘 **Dónde se aprende** (1 clase): [B25-C01 · Estructura de la Vía Láctea](../programa/clases/B25/B25-C01-estructura-de-la-via-lactea/CLASE.md).

### Halo estelar

- El halo estelar es la envoltura difusa de estrellas muy viejas, y el halo de materia oscura es la masa invisible que domina el potencial a gran radio (C15).

💡 **Cómo se explica en la clase [B25-C01](../programa/clases/B25/B25-C01-estructura-de-la-via-lactea/CLASE.md):**
- El disco delgado contiene las estrellas jóvenes y el gas; el grueso, estrellas más viejas y a mayor altura (escala de longitud `2,0 ± 0,2 kpc` y masa `6 ± 3 × 10⁹ M☉`, S3); el halo estelar, las más viejas y pobres en metales (C17).
- 🎯 **Por qué importa:** Estamos dentro de la galaxia y no podemos fotografiarla desde fuera: su forma se reconstruye midiendo distancias y velocidades desde un punto que no es el centro. Sin un esquema claro de componentes (bulbo, barra, disco, halo) y de cifras de referencia, el resto del bloque carece de escala.

📘 **Dónde se aprende** (1 clase): [B25-C01 · Estructura de la Vía Láctea](../programa/clases/B25/B25-C01-estructura-de-la-via-lactea/CLASE.md).

### Halo isotermo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B31-C17):** Una curva plana sin halo es inexplicable con la materia visible; cada candidato predice una escala distinta. La decisión central: ¿qué distingue la curva de rotación con halo y qué escalas predicen los candidatos?

📘 **Dónde se aprende** (1 clase): [B31-C17 · Materias oscuras candidatas](../programa/clases/B31/B31-C17-materias-oscuras-candidatas/CLASE.md).

### Halo NFW

- El halo NFW `Φ = −4πGρ₀ r_s³ ln(1 + r/r_s)/r`.

💡 **Cómo se explica en la clase [B36-C11](../programa/clases/B36/B36-C11-gravedad-modificada-mond-y-relativistas-frente-a-materia-oscura/CLASE.md):**
- Para una galaxia de `5×10¹⁰ M☉` y escala de `3 kpc` (ilustrativa), la curva MOND llega a `191,3 km/s` a 10 kpc frente a `134,8` newtoniana, un halo NFW la reproduce con una desviación de `1,55 km/s`, y la velocidad plana `168,62` coincide con `(G M a₀)^(1/4) = 167,98 km/s` al `0,4 %`.
- 🎯 **Por qué importa:** Una alternativa debe confrontarse con todas las pruebas. La decisión central: ¿qué observación separa la materia oscura de la gravedad modificada?

📘 **Dónde se aprende** (2 clases): [B36-C11 · Gravedad modificada (MOND y relativistas) frente a materia oscura](../programa/clases/B36/B36-C11-gravedad-modificada-mond-y-relativistas-frente-a-materia-oscura/CLASE.md); [B38-C05 · Potenciales galácticos: Plummer, Miyamoto-Nagai y NFW](../programa/clases/B38/B38-C05-potenciales-galacticos-plummer-miyamoto-nagai-y-nfw/CLASE.md).

### Halo pseudo-isotermo

- Un halo pseudo-isotermo tiene velocidad `v² = v_∞²[1 − (r_c/R) arctan(R/r_c)]`, con `r_c` el radio del núcleo y `v_∞` la velocidad asintótica.
- El halo pseudo-isotermo tiene `v²(r) = v_∞²[1 − (r_c/r)arctan(r/r_c)]`.

💡 **Cómo se explica en la clase [B25-C08](../programa/clases/B25/B25-C08-curvas-de-rotacion-de-galaxias/CLASE.md):**
- Con un halo pseudo-isotermo de núcleo `r_c = 5 kpc` (ilustrativo), cuadrar `Θ₀` exige `v_∞ = 304 km/s`.
- 🎯 **Por qué importa:** Si la masa estuviera donde brilla, la velocidad de rotación debería caer en las afueras de una galaxia, como la de los planetas lejanos del Sol. Que una curva de rotación se mantenga plana indica más masa de la que se ve.

📘 **Dónde se aprende** (2 clases): [B25-C08 · Curvas de rotación de galaxias](../programa/clases/B25/B25-C08-curvas-de-rotacion-de-galaxias/CLASE.md); [B26-C18 · Materia oscura y evidencias](../programa/clases/B26/B26-C18-materia-oscura-y-evidencias/CLASE.md).

### Hamiltoniano

- Un sistema hamiltoniano tiene una función de energía `H(q, p)` que determina el movimiento (aquí `q` es la posición y `p` la velocidad por unidad de masa, con `H = v²/2 − GM/r`).
- La energía potencial es `U(q) = −log π(q)` (salvo constante), la cinética `K(p) = ½ pᵀp` y el hamiltoniano `H(q, p) = U(q) + K(p)`.
- El hamiltoniano es el operador de energía.

💡 **Cómo se explica en la clase [B11-C11](../programa/clases/B11/B11-C11-metodos-simplecticos/CLASE.md):**
- A["Sistema hamiltoniano<br/>H = v²/2 − GM/r"] --> B["Método simpléctico<br/>(leapfrog)"]
- *Descripción textual:* un método simpléctico aplicado a un sistema hamiltoniano conserva muy bien una energía modificada, por lo que el error de la energía real queda acotado y oscilante, pero acumula un error de fase; un método no simpléctico como RK4 deriva en energía de forma secular.
- 🎯 **Por qué importa:** Para el sistema solar, anillos planetarios o constelaciones se necesitan integraciones de millones de vueltas. Un método que añade o quita un poco de energía en cada vuelta termina destruyendo la órbita.

📘 **Dónde se aprende** (3 clases): [B11-C11 · Métodos simplécticos](../programa/clases/B11/B11-C11-metodos-simplecticos/CLASE.md); [B19-C03 · Hamiltonian Monte Carlo y NUTS](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md); [B31-C02 · Ecuación de Schrödinger](../programa/clases/B31/B31-C02-ecuacion-de-schrodinger/CLASE.md).

### Hamiltoniano modificado

- El hamiltoniano modificado (o «de sombra») es una energía ligeramente distinta que el método conserva con mucha precisión.

🎯 **Por qué importa (clase B11-C11):** Para el sistema solar, anillos planetarios o constelaciones se necesitan integraciones de millones de vueltas. Un método que añade o quita un poco de energía en cada vuelta termina destruyendo la órbita.

📘 **Dónde se aprende** (1 clase): [B11-C11 · Métodos simplécticos](../programa/clases/B11/B11-C11-metodos-simplecticos/CLASE.md).

### Hamming(7,4)

- Reed–Solomon (255,223) tiene `t = 16`. Hamming(7,4) corrige 1 bit en 7.

💡 **Cómo se explica en la clase [B89-C09](../programa/clases/B89/B89-C09-codificacion-correctora-de-errores/CLASE.md):**
- Un Hamming(7,4) en un canal con `p = 0,02` baja la probabilidad de bloque erróneo a `0,00786` (simulada `0,00786`).
- 🎯 **Por qué importa:** La codificación es la herramienta que permite cerrar enlaces de espacio profundo con potencias modestas: cada decibelio de ganancia de código equivale a una antena más grande o a más potencia. La decisión central: ¿cuánta redundancia añadir y cuánto `Eb/N0` se ahorra con ella?

📘 **Dónde se aprende** (1 clase): [B89-C09 · Codificación correctora de errores](../programa/clases/B89/B89-C09-codificacion-correctora-de-errores/CLASE.md).

### Hann

- Una ventana es una función `w[n]` por la que se multiplica la serie antes de transformarla, para suavizar los bordes; la de Hann es `w[n] = 0,5 − 0,5 cos(2πn/N)` (versión periódica).

💡 **Cómo se explica en la clase [B15-C06](../programa/clases/B15/B15-C06-analisis-espectral-de-senales/CLASE.md):**
- En el laboratorio, un coseno de 64,5 ciclos en 1024 muestras (fuera de bin) tiene, a 30 bins del pico, un nivel de −34,0 dB con ventana rectangular y de −96,6 dB con Hann.
- El precio: la ventana de Hann ensancha el pico principal y reduce su amplitud.
- 🎯 **Por qué importa:** Alguien afirma: «hay un periodo de 3,7 días en esta estrella». ¿Cómo se sostiene?

📘 **Dónde se aprende** (1 clase): [B15-C06 · Análisis espectral de señales](../programa/clases/B15/B15-C06-analisis-espectral-de-senales/CLASE.md).

### Hash

- Fijar una versión es exigir exactamente esa. Hash es la suma de verificación (C11) de cada archivo descargable.
- Un hash (huella) es una función que resume un contenido;
- Un hash es un resumen de tamaño fijo de unos datos.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B23-C07](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md):**
- La verificación numérica dice «reproducida dentro de tolerancia», porque la cifra casi no se mueve; pero el hash de los datos cambia, y la verificación lista «datos».
- Tampoco sustituye el control de versiones de datos ni del código (el hash del script identifica el contenido, no su historia), ni garantiza que un hardware distinto dé el mismo resultado bit a bit.
- 🎯 **Por qué importa:** Un informe dice «el modelo reproduce la posición con un error de 8,21 × 10⁻⁴ au». Seis meses después, nadie sabe con qué versión del código, qué archivo de datos ni qué tolerancia se calculó, y el número no se puede reproducir ni defender.

📘 **Dónde se aprende** (7 clases): [B14-C12 · Ejecución reproducible con uv](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md); [B23-C07 · Trazabilidad científica de resultados](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md); [B63-C03 · Curaduría y cadena de custodia de muestras](../programa/clases/B63/B63-C03-curaduria-y-cadena-de-custodia-de-muestras/CLASE.md); [B88-C13 · Actualización segura de software](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md); [B96-C22 · Transferencia de datos entre estación y centro de datos](../programa/clases/B96/B96-C22-transferencia-de-datos-entre-estacion-y-centro-de-datos/CLASE.md); [B116-C03 · Historia clínica remota y registros médicos de misión](../programa/clases/B116/B116-C03-historia-clinica-remota-y-registros-medicos-de-mision/CLASE.md) y 1 más.

### Hash anclado

- Anexado solo: no se editan entradas previas. Hash anclado: hash final guardado aparte.

💡 **Cómo se explica en la clase [B96-C30](../programa/clases/B96/B96-C30-registro-y-auditoria-de-operaciones/CLASE.md):**
- Descripción larga: la cadena detecta cualquier cambio interno; el truncamiento final exige un hash anclado aparte.
- 🎯 **Por qué importa:** Sin registro verificable no se puede reconstruir un incidente ni demostrar quién aprobó un comando. La decisión central: ¿cómo se registra para que una alteración se detecte y cuánto hay que revisar en una auditoría?

📘 **Dónde se aprende** (1 clase): [B96-C30 · Registro y auditoría de operaciones](../programa/clases/B96/B96-C30-registro-y-auditoria-de-operaciones/CLASE.md).

### Hash encadenado

- Un hash encadenado liga cada entrada a la anterior.

💡 **Cómo se explica en la clase [B104-C23](../programa/clases/B104/B104-C23-ejecucion-de-experimentos-a-bordo-procedimientos-y-registro/CLASE.md):**
- L["lecturas del procedimiento"] --> H["hash encadenado SHA-256"]
- Un registro de cinco entradas con hash encadenado se verifica íntegro y, tras editar la entrada 2, se detecta la rotura en esa entrada.
- 🎯 **Por qué importa:** Las horas de tripulación son escasas y un dato sin registro fiable vale poco. La decisión central: ¿cómo repartir 20 horas entre experimentos para maximizar el valor y cómo asegurar que el registro de lo medido no se altere sin que se note?

📘 **Dónde se aprende** (1 clase): [B104-C23 · Ejecución de experimentos a bordo: procedimientos y registro](../programa/clases/B104/B104-C23-ejecucion-de-experimentos-a-bordo-procedimientos-y-registro/CLASE.md).

### Hash SHA-256

- Un hash SHA-256 es una huella de 256 bits del contenido: cualquier cambio de un carácter cambia la huella.

💡 **Cómo se explica en la clase [B13-C19](../programa/clases/B13/B13-C19-metadatos-y-registros-de-calibracion/CLASE.md):**
- R --> H["Hash SHA-256<br/>del contenido canónico"]
- 🎯 **Por qué importa:** Dentro de un año alguien usará los datos de un fotodiodo calibrado hoy. Necesitará saber con qué patrones, a qué temperatura, con qué incertidumbre y hasta cuándo es válida la calibración.

📘 **Dónde se aprende** (1 clase): [B13-C19 · Metadatos y registros de calibración](../programa/clases/B13/B13-C19-metadatos-y-registros-de-calibracion/CLASE.md).

### Haversine

- La función haversine es `hav(x) = sen²(x/2)`.

💡 **Cómo se explica en la clase [B04-C16](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md):**
- La fórmula del haversine es la elegida en la práctica cuando las separaciones son pequeñas.
- *Descripción textual:* de dos puntos dados por latitud y longitud se obtienen dos caminos: el del coseno, igual al producto escalar de los vectores unitarios, y el del haversine; ambos dan la distancia angular `c`, que multiplicada por el radio da la distancia en longitud; el primero pierde precisión para `c` pequeño y el segundo no.
- 🎯 **Por qué importa:** Para pasar de un lugar a otro de la Tierra, un avión sigue (casi) un círculo máximo. Para decidir cuánto debe girar un telescopio entre dos estrellas, se calcula la distancia angular sobre la esfera celeste.

📘 **Dónde se aprende** (1 clase): [B04-C16 · Geometría de esferas y círculos máximos](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md).

### Haz

- El haz `B_ℓ = exp(−ℓ(ℓ+1)σ_b²/2)`.

💡 **Cómo se explica en la clase [B40-C13](../programa/clases/B40/B40-C13-ruido-haz-y-covarianza-instrumental-en-mapas-del-fondo/CLASE.md):**
- El ruido supera a la señal con haz desde `ℓ = 2009`.
- Como una foto desenfocada con grano: el desenfoque apaga los detalles finos (haz) y el grano los tapa (ruido).
- 🎯 **Por qué importa:** Un espectro sin su barra de error no sirve. La decisión central: ¿cuándo domina el ruido y cuánto vale la dispersión del espectro?

📘 **Dónde se aprende** (1 clase): [B40-C13 · Ruido, haz y covarianza instrumental en mapas del fondo](../programa/clases/B40/B40-C13-ruido-haz-y-covarianza-instrumental-en-mapas-del-fondo/CLASE.md).

### Haz sucio

- El haz sucio `b(l, m)` es la transformada de la función de muestreo.
- El haz sucio: transformada de la cobertura.
- La imagen sucia y el haz sucio.

💡 **Cómo se explica en la clase [B42-C10](../programa/clases/B42/B42-C10-interferometria-de-multiples-telescopios/CLASE.md):**
- Los anchos del haz sucio son `4,500 mas` (x) y `2,300 mas` (y) frente a `λ/B_máx = 3,496 mas`.
- Con pocos telescopios el haz sucio tiene lóbulos laterales grandes (0,56); por eso las imágenes de estos arreglos exigen deconvolución (C19).
- ⚠️ **Error frecuente:** Confundir haz sucio con limpio. El sucio no está deconvolucionado.
- 🎯 **Por qué importa:** La resolución depende de la línea base, no del diámetro de cada telescopio, y la calidad de la imagen de la cobertura uv. La decisión central: ¿qué resolución y qué calidad de imagen da una disposición de telescopios?

📘 **Dónde se aprende** (3 clases): [B42-C10 · Interferometría de múltiples telescopios](../programa/clases/B42/B42-C10-interferometria-de-multiples-telescopios/CLASE.md); [B46-C16 · Síntesis de apertura](../programa/clases/B46/B46-C16-sintesis-de-apertura/CLASE.md); [B51-C06 · Autocalibración iterativa con modelo de cielo](../programa/clases/B51/B51-C06-autocalibracion-iterativa-con-modelo-de-cielo/CLASE.md).

### HAZID

- El HAZID identifica peligros con palabras guía sobre nodos.

💡 **Cómo se explica en la clase [B83-C21](../programa/clases/B83/B83-C21-identificacion-de-peligros-en-sistemas-de-lanzamiento-hazid/CLASE.md):**
- Un HAZID real recorre todas las celdas y descarta las no aplicables con justificación.
- El HAZID sintético recorre 6 nodos con 7 palabras guía (42 celdas) y registra 12 peligros (28,6 % de las celdas): 0 altos, 8 medios y 4 bajos.
- ⚠️ **Error frecuente:** Mezclar HAZID con FMEA. El HAZID identifica peligros del sistema; el FMEA, modos de fallo de componentes
- 🎯 **Por qué importa:** Los peligros que no se identifican no se pueden controlar. La decisión central: ¿qué puede salir mal en cada fase, qué tan grave y probable es, y el riesgo para terceros cabe en el umbral que el proyecto adoptó?

📘 **Dónde se aprende** (1 clase): [B83-C21 · Identificación de peligros en sistemas de lanzamiento (HAZID)](../programa/clases/B83/B83-C21-identificacion-de-peligros-en-sistemas-de-lanzamiento-hazid/CLASE.md).

### HDOP

- El DOP (*dilution of precision*) amplifica el error: `PDOP = √(Q₁₁+Q₂₂+Q₃₃)` con `Q = (GᵀG)⁻¹`. HDOP y VDOP separan lo horizontal de lo vertical.

🎯 **Por qué importa (clase B57-C10):** La geodesia con GNSS mide posiciones de estaciones con precisión de milímetros a centímetros y sirve para ver cómo se mueve la corteza. Pero la precisión depende de la geometría de los satélites.

📘 **Dónde se aprende** (1 clase): [B57-C10 · Geodesia mediante GNSS](../programa/clases/B57/B57-C10-geodesia-mediante-gnss/CLASE.md).

### HDU

- Un HDU (*Header Data Unit*) es una unidad formada por un encabezado y, normalmente, un bloque de datos; el primero del archivo es el HDU primario.
- Una HDU es una unidad de cabecera y datos.

💡 **Cómo se explica en la clase [B44-C19](../programa/clases/B44/B44-C19-formato-fits-y-metadatos/CLASE.md):**
- Límite: una sola HDU sin extensiones ni compresión.
- 🎯 **Por qué importa:** Un cuadro sin metadatos es un arreglo de números sin contexto. La decisión central: ¿qué debe llevar la cabecera para interpretar los datos?

📘 **Dónde se aprende** (2 clases): [B14-C06 · Formato FITS y encabezados](../programa/clases/B14/B14-C06-formato-fits-y-encabezados/CLASE.md); [B44-C19 · Formato FITS y metadatos](../programa/clases/B44/B44-C19-formato-fits-y-metadatos/CLASE.md).

### HDU primario

- Un HDU (*Header Data Unit*) es una unidad formada por un encabezado y, normalmente, un bloque de datos; el primero del archivo es el HDU primario.

🎯 **Por qué importa (clase B14-C06):** Una imagen astronómica es una matriz de números, pero esos números no significan nada sin su encabezado: ¿qué unidad tienen?, ¿cuánto duró la exposición?, ¿a qué punto del cielo apunta el píxel central? Si el encabezado miente o se pierde, la imagen no sirve.

📘 **Dónde se aprende** (1 clase): [B14-C06 · Formato FITS y encabezados](../programa/clases/B14/B14-C06-formato-fits-y-encabezados/CLASE.md).

### Hecho no confirmado

- Un hecho no confirmado se rotula como tal.

🎯 **Por qué importa (clase B122-C08):** B124-C18 trata divulgación; la comunicación de crisis con mensajes oportunos no está cubierta. La decisión central: ¿qué hay que comunicar, a quién y antes de qué plazo?

📘 **Dónde se aprende** (1 clase): [B122-C08 · Comunicación de crisis con operadores, autoridades y público](../programa/clases/B122/B122-C08-comunicacion-de-crisis-con-operadores-autoridades-y-publico/CLASE.md).

### Heidke

- El POD, el FAR y el Heidke.

💡 **Cómo se explica en la clase [B33-C13](../programa/clases/B33/B33-C13-pronostico-de-actividad-geomagnetica/CLASE.md):**
- El ajuste recupera `b = 2,185 ± 0,012` (verdadero 2,2) con `R² = 0,913`; el pronóstico binario de `Kp ≥ 5` (33 de 3000 intervalos) tiene `Heidke = 0,153` en el mejor umbral.
- 🎯 **Por qué importa:** Predecir una tormenta es predecir un evento raro. La decisión central: ¿qué precisión tiene un pronóstico por umbral de un evento raro?

📘 **Dónde se aprende** (1 clase): [B33-C13 · Pronóstico de actividad geomagnética](../programa/clases/B33/B33-C13-pronostico-de-actividad-geomagnetica/CLASE.md).

### Helicidad

- La helicidad `K = ∫A·B dV` mide el enlace del campo.

🎯 **Por qué importa (clase B35-C07):** La conservación del flujo explica por qué el campo se amplifica al comprimirse y por qué la reconexión exige romper la idealidad. La decisión central: ¿cuándo el campo se mueve con el plasma y cuándo se difunde?

📘 **Dónde se aprende** (1 clase): [B35-C07 · Congelamiento del flujo magnético y conservación en MHD ideal](../programa/clases/B35/B35-C07-congelamiento-del-flujo-magnetico-y-conservacion-en-mhd-ideal/CLASE.md).

### Helicidad cruzada

- La helicidad cruzada mide la correlación entre velocidad y campo.

🎯 **Por qué importa (clase B35-C09):** La pendiente de un espectro y su intermitencia distinguen modelos de turbulencia. La decisión central: ¿qué pendiente y qué curtosis tiene la serie y qué modelo sugiere?

📘 **Dónde se aprende** (1 clase): [B35-C09 · Turbulencia en plasmas y MHD](../programa/clases/B35/B35-C09-turbulencia-en-plasmas-y-mhd/CLASE.md).

### Heliocéntrico

- Un modelo geocéntrico pone la Tierra en el centro; uno heliocéntrico pone el Sol.

💡 **Cómo se explica en la clase [B02-C10](../programa/clases/B02/B02-C10-geocentrismo-y-heliocentrismo/CLASE.md):**
- Un planeta parece retroceder; el modelo geocéntrico lo produce con una rueda sobre otra; el heliocéntrico, con el hecho de que la Tierra y el planeta recorren órbitas distintas.
- A --> C["Modelo heliocéntrico:<br/>la Tierra adelanta o es<br/>adelantada por el planeta"]
- 🎯 **Por qué importa:** La pregunta «¿se mueve la Tierra o el cielo?» se puede responder hoy en una línea, pero en 1500 una persona razonable podía defender cualquiera de las dos. La pregunta motivadora es: ¿con qué criterios se elige entre dos modelos que predicen casi lo mismo?

📘 **Dónde se aprende** (1 clase): [B02-C10 · Geocentrismo y heliocentrismo](../programa/clases/B02/B02-C10-geocentrismo-y-heliocentrismo/CLASE.md).

### Hematopoyético

- Tiene una fase de pródromo (náuseas, vómitos, anorexia), y subsíndromes hematopoyético (HSS), gastrointestinal (GIS) y neurovascular o del sistema nervioso central (SNC).

💡 **Cómo se explica en la clase [B112-C03](../programa/clases/B112/B112-C03-efectos-agudos-de-la-radiacion/CLASE.md):**
- Seed (NASA THREE, 2011) describe: el síndrome hematopoyético es el más frecuente y aparece en el intervalo de 0,5 a 8 Gy, tarda semanas en expresarse y, sin tratamiento, a dosis altas puede causar la muerte en 15–60 días; el gastrointestinal exige 4–15 Gy y aparece en días; el neurovascular o del SNC solo tras más de 20–30 Gy, en horas.
- Paso 3 · Intervalo. 1,121 Gy está dentro del hematopoyético (0,5–8 Gy).
- 🎯 **Por qué importa:** Ninguna clase cubre síndromes agudos y umbrales. Un evento solar grande es el único escenario de la exploración que podría producir efectos agudos, y por eso los límites de corto plazo y el blindaje de refugio se diseñan a su medida.

📘 **Dónde se aprende** (1 clase): [B112-C03 · Efectos agudos de la radiación](../programa/clases/B112/B112-C03-efectos-agudos-de-la-radiacion/CLASE.md).

### HEPA

- Aerosol: partículas en suspensión. HEPA: filtro de alta eficiencia.

💡 **Cómo se explica en la clase [B106-C23](../programa/clases/B106/B106-C23-control-de-particulas-y-polvo-respirable-en-cabina/CLASE.md):**
- ⚠️ **Error frecuente:** Tomar la definición de HEPA como consultada. Es de manual.
- 🎯 **Por qué importa:** En 1 g las partículas grandes caen al suelo; en microgravedad no, y en gravedad parcial caen más despacio. La decisión central: ¿qué eficiencia de filtro y qué caudal limpian la cabina en un tiempo dado según la gravedad y el tamaño?

📘 **Dónde se aprende** (1 clase): [B106-C23 · Control de partículas y polvo respirable en cabina](../programa/clases/B106/B106-C23-control-de-particulas-y-polvo-respirable-en-cabina/CLASE.md).

### Herencia

- La herencia pierde nivel si cambia el entorno o la arquitectura (baja a 5, S5).

💡 **Cómo se explica en la clase [B83-C18](../programa/clases/B83/B83-C18-niveles-de-madurez-tecnologica/CLASE.md):**
- D["TRL declarado por elemento"] --> H["Reglas de herencia e integracion"]
- *Descripción textual:* el TRL declarado pasa por las reglas de herencia e integración y da el TRL efectivo; su mínimo es el del sistema; la brecha frente a PDR/CDR y la dificultad de avance dan el esfuerzo y el plan.
- ⚠️ **Error frecuente:** Dar TRL 9 por herencia sin ver el entorno. Reevalúa si cambió el entorno o la arquitectura
- 🎯 **Por qué importa:** Un elemento «con herencia de vuelo» que se usa en otro entorno no es TRL 9. La decisión central: ¿cuál es el TRL real del sistema, qué elementos lo frenan y cuánto cuesta llevarlos al nivel que pide la revisión?

📘 **Dónde se aprende** (1 clase): [B83-C18 · Niveles de madurez tecnológica](../programa/clases/B83/B83-C18-niveles-de-madurez-tecnologica/CLASE.md).

### Herencia de prioridad

- La herencia de prioridad sube temporalmente la prioridad del dueño del mutex a la del que espera.

🎯 **Por qué importa (clase B88-C28):** El caso Pathfinder mostró que un error de concurrencia puede aparecer solo en operación y provocar reinicios por watchdog. La decisión central: ¿cómo se garantiza que una tarea de alta prioridad no quede bloqueada indefinidamente por otras de menor prioridad?

📘 **Dónde se aprende** (1 clase): [B88-C28 · Inversión de prioridad y deadlocks](../programa/clases/B88/B88-C28-inversion-de-prioridad-y-deadlocks/CLASE.md).

### Herradura

- El ángulo coorbital `θ = λ_part − λ_Tierra` (sin envolver) distingue: tadpole (`θ` oscila alrededor de `±60°` sin cruzar `0` ni `π`), herradura (`θ` cubre `π` sin cruzar `0` ni `2π`) y cuasi-satélite (`θ` oscila alrededor de `0` con una amplitud pequeña y la partícula se mantiene a unos pocos `R_H`).

💡 **Cómo se explica en la clase [B73-C22](../programa/clases/B73/B73-C22-capturas-temporales-y-cuasi-satelites/CLASE.md):**
- C -->|"cubre pi, no cruza 0"| H["herradura"]
- Analogía: tres formas de acompañar a un corredor en una pista circular: ir un poco por delante o por detrás oscilando (tadpole), alternar yendo delante y detrás pasando por el lado opuesto (herradura), o rodearlo en pequeños lazos sin alejarse (cuasi-satélite).
- 🎯 **Por qué importa:** Un asteroide puede acompañar a la Tierra durante siglos sin orbitarla: dando vueltas alrededor de L4 (tadpole), de L3–L4–L5 (herradura) o de la propia Tierra (cuasi-satélite); y puede ser capturado temporalmente dentro de su esfera de Hill. Distinguirlos requiere una clasificación operativa y una advertencia: no son satélites.

📘 **Dónde se aprende** (1 clase): [B73-C22 · Capturas temporales y cuasi-satélites](../programa/clases/B73/B73-C22-capturas-temporales-y-cuasi-satelites/CLASE.md).

### Herramienta suelta

- Una herramienta suelta es la que se libera sin amarre y deriva con velocidad constante.

💡 **Cómo se explica en la clase [B108-C03](../programa/clases/B108/B108-C03-herramientas-y-equipos-de-eva/CLASE.md):**
- H["herramienta suelta"] --> D["deriva v t"]
- *Descripción textual:* una fuerza con un brazo da un par; el par reactivo acelera el cuerpo libre; un empuje da un cambio de velocidad y una herramienta suelta deriva a velocidad constante.
- ⚠️ **Error frecuente:** Ignorar la deriva de una herramienta suelta. Se corrige con 8.4.
- 🎯 **Por qué importa:** No hay clase sobre herramientas EVA (torque, reacción, sujeción de herramientas). La decisión central: ¿qué par se logra con una fuerza dada, y cuánto gira o se desplaza quien lo aplica si nada lo sujeta?

📘 **Dónde se aprende** (1 clase): [B108-C03 · Herramientas y equipos de EVA](../programa/clases/B108/B108-C03-herramientas-y-equipos-de-eva/CLASE.md).

### Hessiano

- El hessiano es la matriz de segundas derivadas; su discriminante es `D = f_xx f_yy − f_xy²`.

💡 **Cómo se explica en la clase [B09-C16](../programa/clases/B09/B09-C16-derivadas-parciales/CLASE.md):**
- D --> F["Segundas derivadas<br/>→ hessiano"]
- *Descripción textual:* se calculan las dos derivadas parciales, se combinan en el cambio total aproximado, que sirve para propagar incertidumbres; las segundas derivadas forman el hessiano que clasifica puntos críticos.
- 🎯 **Por qué importa:** La luminosidad de una estrella calculada con su radio y su temperatura tiene una incertidumbre que viene de las dos. ¿Cuál pesa más?

📘 **Dónde se aprende** (1 clase): [B09-C16 · Derivadas parciales](../programa/clases/B09/B09-C16-derivadas-parciales/CLASE.md).

### Heterogeneidad

- La heterogeneidad `τ` se identifica mal con pocos grupos; su posterior suele ser ancha y asimétrica.

💡 **Cómo se explica en la clase [B12-C21](../programa/clases/B12/B12-C21-modelos-jerarquicos-bayesianos/CLASE.md):**
- El error es mayor porque ahora se admite heterogeneidad: la jerarquía no reduce la incertidumbre del conjunto, la hace honesta.
- *Descripción textual:* los hiperparámetros generan los parámetros de cada sensor, que a su vez generan los datos; al observar los datos se calcula la posterior de la heterogeneidad `τ`, y condicionada a `τ` se obtienen `μ` y los `θ_j`, que son normales; integrando sobre `τ` se obtienen las medias posteriores con contracción.
- 🎯 **Por qué importa:** Ocho sensores del mismo tipo miden un mismo desfase con errores distintos. Tratarlos como idénticos (agrupación completa) ignora diferencias reales entre ellos; tratarlos como independientes (sin agrupación) desperdicia lo que cada uno enseña de los demás.

📘 **Dónde se aprende** (1 clase): [B12-C21 · Modelos jerárquicos bayesianos](../programa/clases/B12/B12-C21-modelos-jerarquicos-bayesianos/CLASE.md).

### Heurística octil

- La heurística octil estima el costo con movimientos ortogonales y diagonales.

🎯 **Por qué importa (clase B97-C08):** Con retardo de comunicación y poca energía, la ruta debe salir buena a la primera. A* garantiza la ruta de costo mínimo si la heurística es admisible, y ahorra cómputo, que a bordo es escaso.

📘 **Dónde se aprende** (1 clase): [B97-C08 · Planificación de trayectorias robóticas](../programa/clases/B97/B97-C08-planificacion-de-trayectorias-roboticas/CLASE.md).

### Heurística voraz

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C17):** Sin planificación se desperdicia tiempo de observación. La decisión central: ¿qué blancos observar con un presupuesto de tiempo limitado y cuánto tiempo hay de visibilidad?

📘 **Dónde se aprende** (1 clase): [B47-C17 · Planificación de observaciones](../programa/clases/B47/B47-C17-planificacion-de-observaciones/CLASE.md).

### HFD

- HFD: diámetro de media energía de una estrella.

💡 **Cómo se explica en la clase [B48-C22](../programa/clases/B48/B48-C22-control-automatico-del-enfocador-y-autoenfoque/CLASE.md):**
- Con ruido de 0,15 µm en cada HFD y 4000 repeticiones, la media del mínimo es 1233,999 pasos y la desviación 0,104 pasos (error estándar 0,0016).
- Ajustar el cuadrado del HFD da un estimador sin sesgo apreciable.
- ⚠️ **Error frecuente:** Ajustar una recta al HFD. Se corrige con 8.1.
- 🎯 **Por qué importa:** Un enfoque erróneo pierde resolución en todas las imágenes de la noche. La decisión central: ¿en qué posición del enfocador está el mínimo y con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B48-C22 · Control automático del enfocador y autoenfoque](../programa/clases/B48/B48-C22-control-automatico-del-enfocador-y-autoenfoque/CLASE.md).

### HHI

- El HHI es la suma de los cuadrados de las cuotas en %, entre 0 y 10 000.
- El HHI es la suma de cuotas al cuadrado (aquí en puntos, de 0 a 10 000).

💡 **Cómo se explica en la clase [B122-C01](../programa/clases/B122/B122-C01-dependencias-de-proveedores-y-cadena-de-suministro-de-infraestructura-espacial/CLASE.md):**
- *Descripción textual:* los proveedores abastecen componentes y estos sostienen servicios; del reparto sale el HHI y de la estructura la indisponibilidad con uno o varios proveedores.
- ⚠️ **Error frecuente:** Confundir HHI con la suma de cuotas. Se corrige con 8.1.
- 🎯 **Por qué importa:** B119-C16 solo introduce la infraestructura crítica y no analiza de quién depende. La decisión central: ¿qué proveedor, si cae, daña más servicios, y cuánto baja el riesgo si hay una segunda fuente?

📘 **Dónde se aprende** (2 clases): [B122-C01 · Dependencias de proveedores y cadena de suministro de infraestructura espacial](../programa/clases/B122/B122-C01-dependencias-de-proveedores-y-cadena-de-suministro-de-infraestructura-espacial/CLASE.md); [B124-C03 · Mercados downstream y upstream](../programa/clases/B124/B124-C03-mercados-downstream-y-upstream/CLASE.md).

### Híbrido

- parcial si el Sol, la Luna y la Tierra no están perfectamente alineados; híbrido si cambia de total a anular a lo largo de su trayectoria (S3).

🎯 **Por qué importa (clase B08-C09):** Un eclipse solar es un fenómeno que reúne a miles de personas y que puede dejar ciegas a quienes lo miran mal. La pregunta motivadora: ¿qué tipo de eclipse ocurrirá, dónde y cómo lo veo sin dañarme?

📘 **Dónde se aprende** (1 clase): [B08-C09 · Eclipses y geometría de sombras](../programa/clases/B08/B08-C09-eclipses-y-geometria-de-sombras/CLASE.md).

### Hidrocarburo

- Un hidrocarburo es un compuesto de carbono e hidrógeno, como el metano.
- Un hidrocarburo contiene sólo carbono e hidrógeno: alcano (enlaces simples, `CₙH₂ₙ₊₂`, como el metano `CH₄`), alqueno (un doble enlace, `CₙH₂ₙ`, como el eteno `C₂H₄`), alquino (un triple enlace) y aromático (anillos con enlaces alternados, como el benceno `C₆H₆`).

🎯 **Por qué importa (clase B06-C16):** El análisis de las muestras de Bennu detectó aminoácidos (incluidos 14 de los 20 usados en la biología terrestre), aminas, formaldehído, ácidos carboxílicos, hidrocarburos aromáticos policíclicos y heterociclos de nitrógeno, entre ellos las cinco nucleobases del ADN y el ARN, además de unas 10 000 especies nitrogenadas (S1).

📘 **Dónde se aprende** (2 clases): [B06-C16 · Química orgánica esencial](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md); [B56-C11 · Atmósfera y superficie de Titán](../programa/clases/B56/B56-C11-atmosfera-y-superficie-de-titan/CLASE.md).

### Hidrocarburos aromáticos policíclicos

- Los hidrocarburos aromáticos policíclicos (PAH) tienen varios anillos fusionados, como el naftaleno `C₁₀H₈`.

💡 **Cómo se explica en la clase [B06-C16](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md):**
- Detectaron aminoácidos, aminas, formaldehído, ácidos carboxílicos, hidrocarburos aromáticos policíclicos y heterociclos de nitrógeno, con unas 10 000 especies nitrogenadas, y observaron que los aminoácidos quirales no proteicos eran racémicos o casi (mezcla en partes iguales de las dos imágenes especulares) (S1).
- 🎯 **Por qué importa:** El análisis de las muestras de Bennu detectó aminoácidos (incluidos 14 de los 20 usados en la biología terrestre), aminas, formaldehído, ácidos carboxílicos, hidrocarburos aromáticos policíclicos y heterociclos de nitrógeno, entre ellos las cinco nucleobases del ADN y el ARN, además de unas 10 000 especies nitrogenadas (S1).

📘 **Dónde se aprende** (1 clase): [B06-C16 · Química orgánica esencial](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md).

### Hidrógeno importado

- El hidrógeno importado es el que no se recupera.

🎯 **Por qué importa (clase B59-C09):** Un combustible fabricado en destino depende de qué parte del hidrógeno se recicla. La decisión central: ¿cuánto hidrógeno hay que importar para fabricar 1 000 kg de propelente O₂/CH₄?

📘 **Dónde se aprende** (1 clase): [B59-C09 · Fabricación de combustibles conceptuales](../programa/clases/B59/B59-C09-fabricacion-de-combustibles-conceptuales/CLASE.md).

### Hidroponía

- La hidroponía cultiva con las raíces en solución acuosa o en un sustrato inerte.

🎯 **Por qué importa (clase B115-C01):** Un cultivo sin suelo depende por completo de que el caudal, el oxígeno y el nivel del depósito no fallen. La decisión central: ¿qué caudal y qué volumen hacen falta para que las raíces reciban oxígeno y agua sin que el sistema se vacíe o se inunde, y cómo se comprueba?

📘 **Dónde se aprende** (1 clase): [B115-C01 · Cultivos hidropónicos para hábitats](../programa/clases/B115/B115-C01-cultivos-hidroponicos-para-habitats/CLASE.md).

### Hidroxilo

- El hidroxilo (OH) es el grupo unido a la estructura que, al calentar, produce agua.

💡 **Cómo se explica en la clase [B59-C03](../programa/clases/B59/B59-C03-agua-en-regolito-y-minerales/CLASE.md):**
- Resultado: hielo `2,972 %`, hidrato `1,995 %`, hidroxilo `0,478 %`; diferencias de `−0,028`, `−0,005` y `−0,022` puntos porcentuales.
- El error pequeño del hielo y del hidroxilo viene de que la sigmoide no ha terminado a la temperatura de la meseta.
- 🎯 **Por qué importa:** No toda el agua es igual de fácil de extraer: el hielo sale con poco calor y el hidroxilo exige temperaturas casi de fusión. La decisión central: ¿qué parte del agua total se obtiene calentando solo hasta 300 K?

📘 **Dónde se aprende** (1 clase): [B59-C03 · Agua en regolito y minerales](../programa/clases/B59/B59-C03-agua-en-regolito-y-minerales/CLASE.md).

### Hielo

- Un hielo es un sólido de una sustancia que a temperatura ambiente sería líquida o gaseosa (agua, CO₂, NH₃…).
- El hielo es agua cristalina libre en los poros.

💡 **Cómo se explica en la clase [B06-C19](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md):**
- Con Clausius–Clapeyron (C11) y `ΔH_sub = 26,1 kJ/mol`, el hielo de CO₂ es estable por encima de una presión que depende de la temperatura: a 150 K, 833 Pa; a 170 K, 9773 Pa (97,7 mb); a 194,7 K, 1,017 × 10⁵ Pa (1 atm).
- La energía por molécula de la cohesión del agua (0,456 eV, C10) es 30 veces mayor, lo que explica que el hielo de agua sea estable a temperaturas mucho más altas que las de las nubes frías.
- ⚠️ **Error frecuente:** Creer que un hielo es estable a cualquier presión. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Los estudios con el telescopio James Webb muestran que las nubes densas del medio interestelar tienen granos de polvo cubiertos de hielos con una variedad de moléculas, y que esos hielos contienen entre el 2 y el 19 % del carbono, oxígeno, nitrógeno y azufre disponibles (S1, resumen).

📘 **Dónde se aprende** (2 clases): [B06-C19 · Química de hielos y minerales](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md); [B59-C03 · Agua en regolito y minerales](../programa/clases/B59/B59-C03-agua-en-regolito-y-minerales/CLASE.md).

### HIL

- PIL: en el procesador objetivo o en un modelo de su aritmética. HIL: con el hardware real conectado (C19).

💡 **Cómo se explica en la clase [B88-C41](../programa/clases/B88/B88-C41-pruebas-sil-y-pil-del-software-de-vuelo/CLASE.md):**
- ⚠️ **Error frecuente:** Creer que SIL basta. Hace falta PIL y HIL (8.4)
- 🎯 **Por qué importa:** La aritmética del procesador objetivo puede ser distinta de la del escritorio. La decisión central: ¿cuánto se aparta la respuesta con la precisión del objetivo y cumple la tolerancia?

📘 **Dónde se aprende** (1 clase): [B88-C41 · Pruebas SIL y PIL del software de vuelo](../programa/clases/B88/B88-C41-pruebas-sil-y-pil-del-software-de-vuelo/CLASE.md).

### Hilo

- Un hilo es una línea de ejecución dentro de un proceso; los hilos de un mismo proceso comparten su memoria.
- Un hilo es una serie numerada de publicaciones.
- Un proceso tiene su memoria propia; un hilo comparte la memoria del proceso.

💡 **Cómo se explica en la clase [B18-C01](../programa/clases/B18/B18-C01-procesos-hilos-y-concurrencia/CLASE.md):**
- Cuando un hilo hace E/S, el lock se libera y otro avanza.
- La defensa es un cerrojo (`with cerrojo: cuenta += 1`) o, mejor, no compartir datos mutables: que cada hilo devuelva su resultado y combinarlos al final.
- 🎯 **Por qué importa:** Tienes ocho órbitas simuladas que propagar y un portátil con varios núcleos. La tentación es «lanzar ocho hilos y listo».

📘 **Dónde se aprende** (3 clases): [B14-C13 · Computación paralela](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md); [B18-C01 · Procesos, hilos y concurrencia](../programa/clases/B18/B18-C01-procesos-hilos-y-concurrencia/CLASE.md); [B130-C04 · Divulgación científica en redes sociales](../programa/clases/B130/B130-C04-divulgacion-cientifica-en-redes-sociales/CLASE.md).

### Hilo con corriente

- Un hilo con corriente en un campo `B` siente `F/L = I B` (perpendicular).

🎯 **Por qué importa (clase B05-C17):** La Tierra tiene un campo magnético que un satélite puede medir con un magnetómetro y que actúa sobre las partículas cargadas que lo atraviesan; además, una corriente a bordo crea su propio campo, que puede perturbar esas medidas.

📘 **Dónde se aprende** (1 clase): [B05-C17 · Campos magnéticos](../programa/clases/B05/B05-C17-campos-magneticos/CLASE.md).

### Hilo de quemado

- El hilo de quemado (*burn wire*) es un hilo que sostiene la antena plegada y se funde para liberarla.

🎯 **Por qué importa (clase B95-C04):** Un enlace con la Tierra necesita una antena, y una antena que no se despliega deja el satélite mudo. La decisión central: ¿qué longitud necesita la antena, cómo se pliega sin dañarla y qué riesgo añade el mecanismo?

📘 **Dónde se aprende** (1 clase): [B95-C04 · Antenas desplegables para satélites pequeños](../programa/clases/B95/B95-C04-antenas-desplegables-para-satelites-pequenos/CLASE.md).

### Hipérbola

- En la hipérbola, `1 + e cos θ` se anula en el ángulo `θ∞ = arccos(−1/e)`: allí `r → ∞` y la dirección se llama asíntota.
- La hipérbola `r = p/(1 + e cos f)` con `p = r_p(1+e)` y `e = 1 + r_p v_∞²/GM` da el estado analítico en cada anomalía verdadera `f`; el tiempo de vuelo sale de la ecuación de Kepler hiperbólica `M = e sinh H − H`.

💡 **Cómo se explica en la clase [B04-C18](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md):**
- Se mira `e`: Halley, `0,968 < 1`: elipse. ʻOumuamua, `1,201 > 1`: hipérbola.
- Una órbita con `e = 1,0000` exacto es un caso límite que en la práctica no se puede distinguir de una hipérbola por la incertidumbre de `e`; por eso se reporta `e` con su error.
- ⚠️ **Error frecuente:** Usar `a` positivo para la hipérbola. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** En 2017 se descubrió un objeto que cruzaba el sistema solar con una órbita que no se cerraba: su excentricidad era mayor que 1. Eso significó que no estaba ligado al Sol: venía de fuera y se iba.

📘 **Dónde se aprende** (2 clases): [B04-C18 · Cónicas y secciones orbitales](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md); [B73-C21 · Pasos cercanos a satélites naturales en integración de N cuerpos](../programa/clases/B73/B73-C21-pasos-cercanos-a-satelites-naturales-en-integracion-de-n-cuerpos/CLASE.md).

### Hipérbola de aproximación

- La hipérbola de aproximación es la trayectoria de la nave en el marco del planeta.

🎯 **Por qué importa (clase B75-C07):** Para apuntar una nave a un sobrevuelo hay que saber a qué distancia pasará, a qué velocidad y cuánto tiempo estará bajo la influencia del planeta. La decisión central: ¿qué hipérbola corresponde a un `v∞` y una altitud de periapsis dados, y cuánto cambia la velocidad heliocéntrica?

📘 **Dónde se aprende** (1 clase): [B75-C07 · Sobrevuelos planetarios](../programa/clases/B75/B75-C07-sobrevuelos-planetarios/CLASE.md).

### Hipérbola de difracción

- La hipérbola de difracción es `t(x) = 2√(d² + x²)/v`.

🎯 **Por qué importa (clase B53-C30):** Sin conocer la velocidad, un retardo no da profundidad. La decisión central: ¿se puede estimar la velocidad del medio con los propios datos y qué error de profundidad produce suponerla mal?

📘 **Dónde se aprende** (1 clase): [B53-C30 · Radar de penetración subsuperficial en cuerpos planetarios](../programa/clases/B53/B53-C30-radar-de-penetracion-subsuperficial-en-cuerpos-planetarios/CLASE.md).

### Hiperbólica

- Para `A u_xx + B u_xy + C u_yy + (términos de orden menor) = 0`, el signo de `B² − 4AC` la clasifica: parabólica (`= 0`; ejemplo: calor `u_t = α u_xx`), hiperbólica (`> 0`; ejemplo: onda `u_tt = c² u_xx`) o elíptica (`< 0`; ejemplo: Laplace `u_xx + u_yy = 0`).

💡 **Cómo se explica en la clase [B11-C13](../programa/clases/B11/B11-C13-ecuaciones-en-derivadas-parciales/CLASE.md):**
- Se clasifican con `A, B, C`: calor `(1, 0, 0)` ⇒ `B² − 4AC = 0` (parabólica); onda `(−1, 0, 1)` (al pasar todo a un lado) ⇒ `+4` (hiperbólica);
- En la hiperbólica viaja con velocidad finita sin disiparse.
- 🎯 **Por qué importa:** El calor que atraviesa un escudo, las ondas en una estructura, el potencial gravitatorio de un cuerpo extenso, el transporte de partículas en un plasma: todos son EDP. Antes de discretizar hay que saber *qué tipo de problema es* (qué datos pide, cómo viaja la información) porque de ello depende el método.

📘 **Dónde se aprende** (1 clase): [B11-C13 · Ecuaciones en derivadas parciales](../programa/clases/B11/B11-C13-ecuaciones-en-derivadas-parciales/CLASE.md).

### Hiperparámetros

- Un modelo jerárquico tiene niveles: datos `y_j ~ N(θ_j, σ_j²)`, parámetros de grupo `θ_j ~ N(μ, τ²)` y hiperparámetros `μ` (media del conjunto) y `τ` (heterogeneidad entre grupos), con un hiperprior sobre ellos.
- Los parámetros `μ` y `τ` se llaman hiperparámetros y llevan su propio prior, el hiperprior.

💡 **Cómo se explica en la clase [B12-C21](../programa/clases/B12/B12-C21-modelos-jerarquicos-bayesianos/CLASE.md):**
- A["Hiperparámetros<br/>μ, τ"] --> B["θ₁ … θ₈ ~ N(μ, τ²)"]
- *Descripción textual:* los hiperparámetros generan los parámetros de cada sensor, que a su vez generan los datos; al observar los datos se calcula la posterior de la heterogeneidad `τ`, y condicionada a `τ` se obtienen `μ` y los `θ_j`, que son normales; integrando sobre `τ` se obtienen las medias posteriores con contracción.
- 🎯 **Por qué importa:** Ocho sensores del mismo tipo miden un mismo desfase con errores distintos. Tratarlos como idénticos (agrupación completa) ignora diferencias reales entre ellos; tratarlos como independientes (sin agrupación) desperdicia lo que cada uno enseña de los demás.

📘 **Dónde se aprende** (2 clases): [B12-C21 · Modelos jerárquicos bayesianos](../programa/clases/B12/B12-C21-modelos-jerarquicos-bayesianos/CLASE.md); [B19-C02 · Modelos jerárquicos](../programa/clases/B19/B19-C02-modelos-jerarquicos/CLASE.md).

### Hiperperiodo

- El hiperperiodo `H = mcm(Tᵢ)`.

💡 **Cómo se explica en la clase [B88-C05](../programa/clases/B88/B88-C05-sistemas-de-tiempo-real/CLASE.md):**
- T --> S["Simulacion en el hiperperiodo"]
- El tiempo de respuesta de `t3` converge a `10 ms`, menor que su plazo de `13 ms`; el hiperperiodo es 156 ms.
- 🎯 **Por qué importa:** En una nave, una tarea de control que llega tarde puede ser tan mala como una que da un resultado incorrecto. La decisión central: ¿cada tarea termina siempre antes de su plazo, aun cuando las de mayor prioridad la interrumpen?

📘 **Dónde se aprende** (1 clase): [B88-C05 · Sistemas de tiempo real](../programa/clases/B88/B88-C05-sistemas-de-tiempo-real/CLASE.md).

### Hiperprior

- Un modelo jerárquico tiene niveles: datos `y_j ~ N(θ_j, σ_j²)`, parámetros de grupo `θ_j ~ N(μ, τ²)` y hiperparámetros `μ` (media del conjunto) y `τ` (heterogeneidad entre grupos), con un hiperprior sobre ellos.
- Los parámetros `μ` y `τ` se llaman hiperparámetros y llevan su propio prior, el hiperprior.

💡 **Cómo se explica en la clase [B19-C02](../programa/clases/B19/B19-C02-modelos-jerarquicos/CLASE.md):**
- Con `J` pequeño (seis aquí), los datos saben poco de `τ`: su posterior es ancha y depende del hiperprior.
- H["Hiperprior<br/>p(μ), p(τ)"] --> P["Población<br/>θ_j ~ N(μ, τ²)"]
- 🎯 **Por qué importa:** Seis sensores de temperatura de un satélite miden cada uno un desvío de calibración. Tres decisiones ingenuas son posibles: tratar a cada sensor por separado, ignorar las diferencias y promediar todo, o confiar en el sensor más preciso.

📘 **Dónde se aprende** (2 clases): [B12-C21 · Modelos jerárquicos bayesianos](../programa/clases/B12/B12-C21-modelos-jerarquicos-bayesianos/CLASE.md); [B19-C02 · Modelos jerárquicos](../programa/clases/B19/B19-C02-modelos-jerarquicos/CLASE.md).

### Hipertermófilo

- Un termófilo tiene óptimo moderadamente alto y un hipertermófilo muy alto (los intervalos exactos varían por autor; aquí no se fijan).

🎯 **Por qué importa (clase B64-C02):** Un hipertermófilo crece donde casi todo lo demás muere, pero el agua hierve a 100 °C a presión ambiente. La pregunta motivadora: ¿qué fija el límite superior de temperatura de la vida y cómo se mide ese límite?

📘 **Dónde se aprende** (1 clase): [B64-C02 · Termófilos e hipertermófilos](../programa/clases/B64/B64-C02-termofilos-e-hipertermofilos/CLASE.md).

### Hipervolumen

- El hipervolumen es el área dominada por el frente respecto de un punto de referencia.

💡 **Cómo se explica en la clase [B81-C11](../programa/clases/B81/B81-C11-optimizacion-multicriterio-y-frentes-de-pareto/CLASE.md):**
- El hipervolumen compara frentes: uno que domine a otro tiene mayor hipervolumen.
- *Descripción textual:* la muestra de diseños se evalúa en dos objetivos; el frente se obtiene con dos algoritmos que deben coincidir, y de él salen el hipervolumen, la rodilla y las elecciones por pesos.
- 🎯 **Por qué importa:** Un peso único esconde la decisión; un frente la muestra completa. La decisión central: ¿cuáles diseños son eficientes y cuál se elige si no se conocen de antemano los pesos?

📘 **Dónde se aprende** (1 clase): [B81-C11 · Optimización multicriterio y frentes de Pareto](../programa/clases/B81/B81-C11-optimizacion-multicriterio-y-frentes-de-pareto/CLASE.md).

### Hipotenusa

- En un triángulo rectángulo, el cateto opuesto a un ángulo `θ` es el lado frente a él, el cateto adyacente es el lado que lo forma junto con la hipotenusa, y la hipotenusa es el lado mayor, frente al ángulo recto.
- Un triángulo rectángulo tiene un ángulo de 90°; el lado opuesto a él es la hipotenusa y los otros dos son los catetos.

💡 **Cómo se explica en la clase [B03-C18](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md):**
- En un triángulo de lados `3`, `4` y `5` (hipotenusa 5), el ángulo opuesto al lado 3 cumple `sen θ = 3/5 = 0,6`, `cos θ = 4/5 = 0,8` y `tan θ = 3/4 = 0,75`.
- 🎯 **Por qué importa:** El Sol y la Luna se ven en el cielo con tamaños angulares muy parecidos, de alrededor de medio grado. ¿Es casualidad que midan lo mismo en el cielo siendo tan distintos?

📘 **Dónde se aprende** (2 clases): [B03-C18 · Razones trigonométricas iniciales](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md); [B04-C07 · Triángulos y distancias angulares](../programa/clases/B04/B04-C07-triangulos-y-distancias-angulares/CLASE.md).

### Hipótesis

- Una hipótesis es una explicación tentativa que se compromete con algo que puede observarse.
- Una hipótesis es la afirmación que se pone a prueba.

💡 **Cómo se explica en la clase [B01-C07](../programa/clases/B01/B01-C07-hipotesis-y-predicciones-falsables/CLASE.md):**
- Una hipótesis útil dice sobre qué, bajo qué condiciones y con qué variables.
- Esa hipótesis nombra el objeto, la magnitud, el intervalo y el mecanismo propuesto.
- ⚠️ **Error frecuente:** Hipótesis que nada contradice. Ejercicio 2.
- 🎯 **Por qué importa:** Una afirmación que ningún resultado posible contradice no enseña nada. Si dices «la Luna cambia de tamaño aparente» y, ocurra lo que ocurra, tu frase queda a salvo, no has dicho gran cosa.

📘 **Dónde se aprende** (3 clases): [B01-C07 · Hipótesis y predicciones falsables](../programa/clases/B01/B01-C07-hipotesis-y-predicciones-falsables/CLASE.md); [B14-C24 · Documentación de hipótesis y decisiones de análisis](../programa/clases/B14/B14-C24-documentacion-de-hipotesis-y-decisiones-de-analisis/CLASE.md); [B96-C21 · Diagnóstico explicable de anomalías](../programa/clases/B96/B96-C21-diagnostico-explicable-de-anomalias/CLASE.md).

### Hipótesis ad hoc

- Una hipótesis ad hoc es un parche añadido solo para salvar la idea de un resultado adverso.

🎯 **Por qué importa (clase B01-C07):** Una afirmación que ningún resultado posible contradice no enseña nada. Si dices «la Luna cambia de tamaño aparente» y, ocurra lo que ocurra, tu frase queda a salvo, no has dicho gran cosa.

📘 **Dónde se aprende** (1 clase): [B01-C07 · Hipótesis y predicciones falsables](../programa/clases/B01/B01-C07-hipotesis-y-predicciones-falsables/CLASE.md).

### Hipótesis alternativa

- Una hipótesis alternativa (o nula) es la que se espera si la tuya falla: aquí, «no hay cambio».

🎯 **Por qué importa (clase B01-C07):** Una afirmación que ningún resultado posible contradice no enseña nada. Si dices «la Luna cambia de tamaño aparente» y, ocurra lo que ocurra, tu frase queda a salvo, no has dicho gran cosa.

📘 **Dónde se aprende** (1 clase): [B01-C07 · Hipótesis y predicciones falsables](../programa/clases/B01/B01-C07-hipotesis-y-predicciones-falsables/CLASE.md).

### Hipótesis de investigación

- Una hipótesis de investigación es la afirmación sustantiva que quieres evaluar; la hipótesis nula `H₀` es la que niega el efecto, y la alternativa `H₁` la que lo afirma.

🎯 **Por qué importa (clase B20-C02):** Un grupo mide cinco variantes razonables de un mismo análisis y publica la que da «un resultado significativo». Nadie mintió con un número, y sin embargo el resultado ya no significa lo que dice.

📘 **Dónde se aprende** (1 clase): [B20-C02 · Diseño de un plan de análisis y preregistro](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md).

### Hipótesis de pequeños ángulos

- La hipótesis de pequeños ángulos linealiza el modelo y solo vale para ángulos pequeños.

🎯 **Por qué importa (clase B108-C04):** Ninguna clase trata la estabilización del astronauta durante trabajo en microgravedad. La decisión central: ¿cuánto rigidez y amortiguamiento necesita una sujeción para que una fuerza de trabajo no desplace a la persona más allá de lo útil?

📘 **Dónde se aprende** (1 clase): [B108-C04 · Sistemas de sujeción y restricción de pies](../programa/clases/B108/B108-C04-sistemas-de-sujecion-y-restriccion-de-pies/CLASE.md).

### Hipótesis exhaustivas y excluyentes

- Las hipótesis exhaustivas y excluyentes agotan las posibilidades.

🎯 **Por qué importa (clase B55-C19):** Una medición rara vez prueba una hipótesis: la hace más o menos probable frente a otra. Quien interpreta una firma debe declarar qué alternativas considera y qué prior asume.

📘 **Dónde se aprende** (1 clase): [B55-C19 · Interpretación de firmas químicas](../programa/clases/B55/B55-C19-interpretacion-de-firmas-quimicas/CLASE.md).

### Hipótesis nula

- Una hipótesis nula es la suposición de que las orientaciones se distribuyen al azar (S1).
- La hipótesis nula `H₀` es la afirmación que se pone a prueba (aquí: «las dos estimaciones apuntan al mismo valor»); la alternativa `H₁` es su negación.
- Una hipótesis de investigación es la afirmación sustantiva que quieres evaluar; la hipótesis nula `H₀` es la que niega el efecto, y la alternativa `H₁` la que lo afirma.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B02-C08](../programa/clases/B02/B02-C08-arqueoastronomia-y-sus-metodos/CLASE.md):**
- C --> D["Contrastar con el azar:<br/>hipótesis nula uniforme"]
- 🎯 **Por qué importa:** Decir «esta puerta mira al solsticio» es fácil; demostrarlo es difícil. Hay que medir bien, conocer el horizonte, descartar el azar y entender el contexto cultural.

📘 **Dónde se aprende** (5 clases): [B02-C08 · Arqueoastronomía y sus métodos](../programa/clases/B02/B02-C08-arqueoastronomia-y-sus-metodos/CLASE.md); [B02-C09 · Alineaciones arqueológicas y sesgos](../programa/clases/B02/B02-C09-alineaciones-arqueologicas-y-sesgos/CLASE.md); [B12-C09 · Pruebas de hipótesis](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md); [B20-C02 · Diseño de un plan de análisis y preregistro](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md); [B132-C04 · Estadística de orientaciones en arqueoastronomía](../programa/clases/B132/B132-C04-estadistica-de-orientaciones-en-arqueoastronomia/CLASE.md).

### Hipoventilación

- La hipoventilación es una ventilación insuficiente que eleva el CO₂.
- La hipoventilación eleva `PaCO₂` y baja `PAO₂`.

💡 **Cómo se explica en la clase [B117-C04](../programa/clases/B117/B117-C04-problemas-respiratorios-simulados/CLASE.md):**
- Las fugas y la hipoventilación son ilustrativas.
- Descripción larga: la saturación casi no cambia entre los extremos nominales, pero cae mucho cuando se combinan fuga e hipoventilación.
- 🎯 **Por qué importa:** Ninguna clase anterior simula problemas respiratorios. La decisión central: ¿cuánto margen de oxigenación hay entre la atmósfera nominal de la cabina y una condición peligrosa, y qué variable lo consume más rápido?

📘 **Dónde se aprende** (2 clases): [B105-C21 · Fisiología respiratoria en microgravedad y atmósferas de cabina](../programa/clases/B105/B105-C21-fisiologia-respiratoria-en-microgravedad-y-atmosferas-de-cabina/CLASE.md); [B117-C04 · Problemas respiratorios simulados](../programa/clases/B117/B117-C04-problemas-respiratorios-simulados/CLASE.md).

### Histéresis

- La histéresis es el camino distinto de ida y vuelta al variar `S`.
- La histéresis es un segundo umbral más bajo para desactivarla.
- Autocorrelación: dependencia con el pasado. Histéresis: umbrales distintos para cerrar y abrir.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B48-C06](../programa/clases/B48/B48-C06-meteorologia-de-observatorios/CLASE.md):**
- La histéresis reduce los cambios en 30,7 %, pero cuesta 3,3 puntos de tiempo abierto.
- Un termostato que se enciende y apaga en el mismo umbral parpadea; con dos umbrales (histéresis) espera a que el cambio sea claro.
- 🎯 **Por qué importa:** Un cierre que oscila abre y cierra la cúpula cientos de veces y desgasta el equipo. La decisión central: ¿qué regla de cierre evita el parpadeo sin perder tiempo útil?

📘 **Dónde se aprende** (9 clases): [B48-C06 · Meteorología de observatorios](../programa/clases/B48/B48-C06-meteorologia-de-observatorios/CLASE.md); [B54-C19 · Modelos climáticos planetarios](../programa/clases/B54/B54-C19-modelos-climaticos-planetarios/CLASE.md); [B85-C08 · Calentadores y termostatos](../programa/clases/B85/B85-C08-calentadores-y-termostatos/CLASE.md); [B86-C21 · Modos de operación y estados de bajo consumo](../programa/clases/B86/B86-C21-modos-de-operacion-y-estados-de-bajo-consumo/CLASE.md); [B96-C06 · Telemetría operativa](../programa/clases/B96/B96-C06-telemetria-operativa/CLASE.md); [B98-C05 · Autonomía de bajo nivel y comportamientos reactivos](../programa/clases/B98/B98-C05-autonomia-de-bajo-nivel-y-comportamientos-reactivos/CLASE.md) y 3 más.

### Histéresis de reposición

- La histéresis de reposición exige margen antes de volver a encender.

💡 **Cómo se explica en la clase [B86-C23](../programa/clases/B86/B86-C23-priorizacion-y-deslastre-de-cargas-electricas/CLASE.md):**
- En un perfil sintético de `400` pasos (luz de unos `140 W` y eclipse de unos `62 W` con ruido), la política con histéresis de reposición hace `79` transiciones; el relleno aplicado en cada paso sin histéresis hace `181`.
- 🎯 **Por qué importa:** La clase de distribución trató cómo repartir potencia, pero no qué hacer cuando falta. Una política de prioridades bien definida mantiene lo crítico vivo y recupera ciencia cuando vuelve la potencia, sin oscilar entre estados.

📘 **Dónde se aprende** (1 clase): [B86-C23 · Priorización y deslastre de cargas eléctricas](../programa/clases/B86/B86-C23-priorizacion-y-deslastre-de-cargas-electricas/CLASE.md).

### Histograma

- El histograma cuenta cuántos píxeles caen en cada intervalo de valores.

💡 **Cómo se explica en la clase [B15-C10](../programa/clases/B15/B15-C10-histogramas-y-normalizacion/CLASE.md):**
- El histograma dice qué valores existen y cuántos píxeles tienen cada uno.
- La ecualización por función de distribución acumulada reasigna cada valor a su rango: el histograma resultante es casi plano (en el laboratorio, la desviación máxima respecto a un histograma plano de 20 intervalos es `0,0000`, porque casi todos los valores son distintos).
- 🎯 **Por qué importa:** Tienes una imagen con un cielo de 50 ADU, una estructura difusa tenue 15 ADU por encima y una estrella de 9000 ADU. Si la muestras con una escala lineal entre mínimo y máximo, el cielo y la estructura quedan en los niveles de gris 1 y 2 de 255: parece una pantalla negra con un punto.

📘 **Dónde se aprende** (1 clase): [B15-C10 · Histogramas y normalización](../programa/clases/B15/B15-C10-histogramas-y-normalizacion/CLASE.md).

### Histograma de rangos

- Un histograma de rangos con forma de U indica posterior demasiado estrecha (sobreconfianza); con forma de colina, demasiado ancha; con sesgo hacia un lado, posterior corrida.

💡 **Cómo se explica en la clase [B19-C08](../programa/clases/B19/B19-C08-calibracion-probabilistica/CLASE.md):**
- *Descripción textual:* se sortea un parámetro y datos, se hace la inferencia, se calcula el rango del parámetro entre los sorteos posteriores y se repite muchas veces; si el histograma de rangos es uniforme, el procedimiento pasa la prueba, y si no, se revisa.
- El histograma de rangos de SBC mira todos los niveles a la vez y distingue sesgo de sobreconfianza.
- 🎯 **Por qué importa:** Un intervalo del 90 % que cubre el valor verdadero solo la mitad de las veces es peor que no tener intervalo: transmite una seguridad falsa. Los diagnósticos de C04 dicen si el cómputo funcionó; los chequeos de C06 si el modelo reproduce los datos.

📘 **Dónde se aprende** (1 clase): [B19-C08 · Calibración probabilística](../programa/clases/B19/B19-C08-calibracion-probabilistica/CLASE.md).

### Historia de formación estelar

- La historia de formación estelar `ψ(t)` es la tasa de formación en función de la edad.

🎯 **Por qué importa (clase B38-C04):** Los conteos de estrellas son una suma sobre edades y la inversión amplifica el ruido. La decisión central: ¿con qué resolución en edad se puede recuperar la historia con un número dado de estrellas?

📘 **Dónde se aprende** (1 clase): [B38-C04 · Historia de formación estelar a partir de poblaciones resueltas](../programa/clases/B38/B38-C04-historia-de-formacion-estelar-a-partir-de-poblaciones-resueltas/CLASE.md).

### Historial

- El árbol de trabajo es lo que ves y editas; el área de preparación es la lista de lo que irá en el próximo commit; el historial es la cadena de commits.

💡 **Cómo se explica en la clase [B07-C14](../programa/clases/B07/B07-C14-control-de-versiones-con-git/CLASE.md):**
- Lo que entra en el historial es difícil de borrar después.
- A -->|"git commit"| H["historial<br/>cadena de commits"]
- 🎯 **Por qué importa:** Sin control de versiones, un proyecto científico acumula archivos como `analisis_final.py`, `analisis_final2.py` y `analisis_final_ahora_si.py`, y nadie sabe cuál produjo la figura del artículo. Con Git, cada estado importante queda guardado con un mensaje, una fecha y un autor, y puedes comparar o recuperar cualquier versión.

📘 **Dónde se aprende** (1 clase): [B07-C14 · Control de versiones con Git](../programa/clases/B07/B07-C14-control-de-versiones-con-git/CLASE.md).

### Hito

- Un hito es un punto de control del proyecto.
- Un hito es un hecho fechado.
- Un hito es una proporción del sistema que debe estar desplegada en una fecha.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B119-C12](../programa/clases/B119/B119-C12-historia-de-competencia-estrategica-espacial/CLASE.md):**
- *Descripción textual:* cada hito técnico precede a un instrumento jurídico tras un rezago; las fechas se separan en consultadas y no consultadas antes de calcular intervalos.
- 🎯 **Por qué importa:** Para leer el derecho vigente conviene saber qué contexto lo produjo; ninguna clase anterior da la cronología comparada entre la tecnología y los instrumentos jurídicos. La decisión central: ¿cuánto tardó el derecho en seguir a la tecnología y por qué importa distinguir fechas verificadas de fechas recordadas?

📘 **Dónde se aprende** (5 clases): [B01-C20 · Proyecto de observación científica inicial](../programa/clases/B01/B01-C20-proyecto-de-observacion-cientifica-inicial/CLASE.md); [B119-C12 · Historia de competencia estratégica espacial](../programa/clases/B119/B119-C12-historia-de-competencia-estrategica-espacial/CLASE.md); [B120-C05 · Riesgos de incumplimiento regulatorio](../programa/clases/B120/B120-C05-riesgos-de-incumplimiento-regulatorio/CLASE.md); [B120-C06 · Caso de planificación regulatoria de un sistema satelital](../programa/clases/B120/B120-C06-caso-de-planificacion-regulatoria-de-un-sistema-satelital/CLASE.md); [B125-C02 · Modelos de ingresos: suscripción y servicio](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md).

### Hito de evidencia

- El hito de evidencia es la prueba asociada a cada nivel.

🎯 **Por qué importa (clase B78-C19):** Una tecnología con un buen desempeño en papel puede estar lejos de volar. La decisión central: ¿en qué nivel está una tecnología según la evidencia que tiene, y qué nivel tiene un sistema formado por componentes de madureces distintas?

📘 **Dónde se aprende** (1 clase): [B78-C19 · Madurez tecnológica TRL](../programa/clases/B78/B78-C19-madurez-tecnologica-trl/CLASE.md).

### Hito de precio fijo

- Un hito de precio fijo es un pago contra un objetivo cumplido.

🎯 **Por qué importa (clase B126-C03):** [B124-C05](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) estima costos sin flujos de caja. La decisión central: ¿cuánto dinero hay que levantar y cuándo, y qué tan sensible es esa cifra a un retraso o a un sobrecosto?

📘 **Dónde se aprende** (1 clase): [B126-C03 · Proyección de flujos de caja de un proyecto espacial](../programa/clases/B126/B126-C03-proyeccion-de-flujos-de-caja-de-un-proyecto-espacial/CLASE.md).

### HITRAN

- CDMS (Cologne Database for Molecular Spectroscopy) y JPL son catálogos de líneas milimétricas y submilimétricas. HITRAN reúne parámetros por línea para atmósferas y astrofísica, con intensidad en cm⁻¹/(molécula·cm⁻²) a 296 K.

💡 **Cómo se explica en la clase [B62-C07](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md):**
- Para cada banco hay que citar la versión y la fecha de consulta; la portada de HITRAN consultada anuncia HITRAN2024 y recomienda indicar la versión usada.
- L --> HT["HITRAN: ν, S(296 K), γ_air, n_air"]
- 🎯 **Por qué importa:** Una identificación depende de una frecuencia, y esa frecuencia viene de un archivo que alguien ajustó y versionó. Si no sabes leer la columna de error, la unidad de la intensidad o la temperatura de referencia, importarás un error silencioso.

📘 **Dónde se aprende** (1 clase): [B62-C07 · Bancos de datos moleculares: CDMS, JPL, HITRAN y LAMDA](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md).

### HMAC-SHA256

- El HMAC-SHA256 con clave secreta autentica.

🎯 **Por qué importa (clase B88-C13):** Una actualización fallida en órbita no se arregla con un cable. La decisión central: ¿qué comprobaciones aceptan solo la imagen correcta y qué mecanismo vuelve a una versión conocida si la nueva no arranca?

📘 **Dónde se aprende** (1 clase): [B88-C13 · Actualización segura de software](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md).

### Hoja

- Una hoja es una condición básica.

💡 **Cómo se explica en la clase [B119-C14](../programa/clases/B119/B119-C14-amenazas-ciberneticas-a-satelites/CLASE.md):**
- Cada control reduce a la mitad una hoja.
- El más eficaz por separado es la formación y doble verificación (hoja D), con riesgo `0.06861`; la autenticación reforzada da `0.09375`.
- 🎯 **Por qué importa:** La amenaza cibernética conecta el derecho con la seguridad operativa; el modelo defensivo de infraestructura espacial (B122-C03) lo desarrolla, y esta clase fija el razonamiento de riesgo. La decisión central: ¿qué control reduce más el riesgo residual y cuánto se gana al combinarlos?

📘 **Dónde se aprende** (1 clase): [B119-C14 · Amenazas cibernéticas a satélites](../programa/clases/B119/B119-C14-amenazas-ciberneticas-a-satelites/CLASE.md).

### Hoja de corriente

- La hoja de corriente es la capa donde el campo invierte su sentido.

🎯 **Por qué importa (clase B30-C11):** Las erupciones liberan en minutos una energía que el campo guardó durante mucho más tiempo, y el modelo más simple de reconexión es demasiado lento para eso. La decisión central: ¿qué tasa de reconexión hace falta y qué dice el modelo de Sweet–Parker?

📘 **Dónde se aprende** (1 clase): [B30-C11 · Reconexión magnética](../programa/clases/B30/B30-C11-reconexion-magnetica/CLASE.md).

### Holgura

- La holgura es el juego entre dientes.
- La ruta crítica es el camino de mayor duración; la holgura es el margen de una actividad fuera de ella.
- La holgura es el exceso de horas sobre las tareas.
- *(y 13 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B43-C14](../programa/clases/B43/B43-C14-reductores-y-transmisiones/CLASE.md):**
- Una holgura de `0,01 mm` sobre un radio primitivo de `72 mm` equivale a `28,65"`.
- Descripción larga: la resolución por micropaso es sub-segundo de arco y la holgura supera ese valor en dos órdenes.
- ⚠️ **Error frecuente:** Olvidar la holgura. Se corrige con 8.3.
- 🎯 **Por qué importa:** El reductor fija la resolución, la fuerza disponible y el comportamiento dinámico. La decisión central: ¿qué relación, qué rendimiento y qué rigidez permiten apuntar con la resolución pedida sin resonancias?

📘 **Dónde se aprende** (16 clases): [B43-C14 · Reductores y transmisiones](../programa/clases/B43/B43-C14-reductores-y-transmisiones/CLASE.md); [B83-C06 · Descomposición funcional](../programa/clases/B83/B83-C06-descomposicion-funcional/CLASE.md); [B90-C01 · Plan de ensamblaje e integración](../programa/clases/B90/B90-C01-plan-de-ensamblaje-e-integracion/CLASE.md); [B90-C05 · Documentación de interfaces](../programa/clases/B90/B90-C05-documentacion-de-interfaces/CLASE.md); [B96-C09 · Secuencias de misión](../programa/clases/B96/B96-C09-secuencias-de-mision/CLASE.md); [B101-C04 · Límites articulares, espacio de trabajo y evitación de colisiones](../programa/clases/B101/B101-C04-limites-articulares-espacio-de-trabajo-y-evitacion-de-colisiones/CLASE.md) y 10 más.

### Holística

- Una rúbrica analítica puntúa cada criterio por separado; una holística, el trabajo en conjunto.

🎯 **Por qué importa (clase B131-C09):** Una rúbrica sin acuerdo entre evaluadores asigna notas que dependen de quién corrige. La decisión central: ¿dos personas distintas darían el mismo nivel a este trabajo, y cómo lo sabes?

📘 **Dónde se aprende** (1 clase): [B131-C09 · Rúbricas de evaluación](../programa/clases/B131/B131-C09-rubricas-de-evaluacion/CLASE.md).

### Homeostasis

- Metabolismo es el conjunto de transformaciones químicas que mantienen un sistema fuera del equilibrio. Homeostasis es la regulación del medio interno.

💡 **Cómo se explica en la clase [B56-C01](../programa/clases/B56/B56-C01-definiciones-operativas-de-vida/CLASE.md):**
- La mula pasa `D2` y `D3` (metabolismo, homeostasis y crecimiento) pero no `D1` ni `D4`, porque un individuo estéril no reproduce ni evoluciona.
- Paso 1 · Propiedades. Metabolismo 0, reproducción 1, evolución 1, límite 0, homeostasis 0, crecimiento 1 (ilustrativas).
- 🎯 **Por qué importa:** Una misión que busca vida necesita saber qué buscar y qué contará como hallazgo. Si el criterio es vago, cualquier resultado se puede discutir; si es demasiado estrecho, se pasa por alto lo que no se parece a la vida terrestre.

📘 **Dónde se aprende** (1 clase): [B56-C01 · Definiciones operativas de vida](../programa/clases/B56/B56-C01-definiciones-operativas-de-vida/CLASE.md).

### Homogénea

- Es homogénea si todos sus términos contienen la incógnita.

🎯 **Por qué importa (clase B11-C01):** Casi ninguna ley de la mecánica espacial nos dice *dónde está* un satélite; nos dice *cómo cambia* su movimiento: la aceleración depende de la posición. Eso es una ecuación diferencial.

📘 **Dónde se aprende** (1 clase): [B11-C01 · Ecuaciones diferenciales ordinarias](../programa/clases/B11/B11-C01-ecuaciones-diferenciales-ordinarias/CLASE.md).

### Homogeneidad

- Un sistema es lineal si cumple aditividad (la respuesta a `u₁ + u₂` es la suma de respuestas) y homogeneidad (la respuesta a `a u` es `a` por la respuesta a `u`); juntas, superposición.
- La homogeneidad es la variación espacial del índice.

💡 **Cómo se explica en la clase [B16-C03](../programa/clases/B16/B16-C03-sistemas-lineales-invariantes/CLASE.md):**
- La función `sat(τ) = clip(τ, −τ_max, τ_max)` viola la homogeneidad: si `τ_max = 0,2` y pides 0,15, obtienes 0,15; si pides el doble (0,30), obtienes 0,20 y no 0,30.
- 🎯 **Por qué importa:** Un ingeniero de control no puede ensayar todos los pares posibles en un telescopio de miles de millones de euros. La esperanza es que, con unas pocas pruebas, se pueda predecir la respuesta a cualquier par.

📘 **Dónde se aprende** (2 clases): [B16-C03 · Sistemas lineales invariantes](../programa/clases/B16/B16-C03-sistemas-lineales-invariantes/CLASE.md); [B43-C21 · Selección de vidrios ópticos: catálogos, homogeneidad y diagramas](../programa/clases/B43/B43-C21-seleccion-de-vidrios-opticos-catalogos-homogeneidad-y-diagramas/CLASE.md).

### Homografía

- Una homografía `H` relaciona el plano del patrón con la imagen.

💡 **Cómo se explica en la clase [B103-C01](../programa/clases/B103/B103-C01-calibracion-intrinseca-de-camaras/CLASE.md):**
- Cada vista da una homografía `H = K [r1 r2 t]` (DLT con las 54 esquinas).
- La homografía supone un modelo estenopeico perfecto; con distorsión queda sesgada.
- 🎯 **Por qué importa:** Un rover que mide una distancia con un error de focal del 1 % comete un error del 1 % en la distancia. La decisión central: ¿cuántas vistas y qué modelo de distorsión hacen falta para que la focal y el punto principal sean fiables, y cómo se comprueba?

📘 **Dónde se aprende** (1 clase): [B103-C01 · Calibración intrínseca de cámaras](../programa/clases/B103/B103-C01-calibracion-intrinseca-de-camaras/CLASE.md).

### Honorario objetivo

- El honorario objetivo es el que se paga si el costo coincide con el objetivo.

💡 **Cómo se explica en la clase [B124-C10](../programa/clases/B124/B124-C10-contratos-y-compras-espaciales/CLASE.md):**
- Paso 1 · Datos. Costo objetivo 100, honorario objetivo 8, reparto 20 % al contratista.
- 🎯 **Por qué importa:** El tipo de contrato reparte el riesgo de sobrecosto entre quien compra y quien vende. La decisión central: ¿cuánto riesgo asume cada parte con cada tipo de contrato y cuánto cuesta ese reparto en promedio?

📘 **Dónde se aprende** (1 clase): [B124-C10 · Contratos y compras espaciales](../programa/clases/B124/B124-C10-contratos-y-compras-espaciales/CLASE.md).

### Hora

- El minuto (min), la hora (h) y el día (d) se aceptan con las equivalencias `1 min = 60 s`, `1 h = 60 min = 3600 s`, `1 d = 24 h = 86 400 s` (S2).

💡 **Cómo se explica en la clase [B03-C08](../programa/clases/B03/B03-C08-tiempo-y-conversiones-astronomicas/CLASE.md):**
- Con las equivalencias del SI, 1 d = 86 400 s (S2), puedes expresar esos períodos en segundos o en años, y calcular que la Tierra gira unos 15,04° por hora respecto de las estrellas.
- Descripción larga: una circunferencia con dos anillos concéntricos; el exterior marca 0 a 360° y el interior 0 a 24 h; cada hora corresponde a 15°.
- 🎯 **Por qué importa:** El período de Neptuno en las fichas de la NASA es 60 189,018 días. Nadie piensa en 60 mil días; se piensa en años.

📘 **Dónde se aprende** (1 clase): [B03-C08 · Tiempo y conversiones astronómicas](../programa/clases/B03/B03-C08-tiempo-y-conversiones-astronomicas/CLASE.md).

### Hora oficial

- La hora oficial es la del reloj civil y no la del cálculo.

🎯 **Por qué importa (clase B08-C07):** Una herramienta que no entiendes es una caja negra: si la aplicación se equivoca de ubicación o de hora, no lo notarás. La pregunta motivadora: ¿puedo confiar en lo que me muestra la herramienta, y qué hago si no hay batería?

📘 **Dónde se aprende** (1 clase): [B08-C07 · Planisferios y aplicaciones celestes](../programa/clases/B08/B08-C07-planisferios-y-aplicaciones-celestes/CLASE.md).

### Hora sidérea

- Tránsito: paso por el meridiano. Hora sidérea: unidad en que avanza el ángulo horario.

🎯 **Por qué importa (clase B48-C04):** Programar un objeto bajo en el cielo desperdicia luz y calidad. La decisión central: ¿cuántas horas al día está un objeto por encima del límite de altitud?

📘 **Dónde se aprende** (1 clase): [B48-C04 · Planificación por visibilidad](../programa/clases/B48/B48-C04-planificacion-por-visibilidad/CLASE.md).

### Hora UT

- La hora UT es el tiempo universal que se usa en el cálculo.

💡 **Cómo se explica en la clase [B08-C05](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md):**
- Se calcula `GMST` a partir de la fecha y hora UT con una fórmula polinómica (coeficientes IAU 1982), y `TSL = GMST + λ`.
- 🎯 **Por qué importa:** Si una estrella culmina a las 22:00 hoy, culminará a las 21:56 mañana. Quien no lo sabe «pierde» el objeto en pocas semanas.

📘 **Dónde se aprende** (1 clase): [B08-C05 · Tiempo sidéreo y solar](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md).

### Horas efectivas

- Método de D'Hondt: asigna cada hora al mayor cociente. Horas efectivas: asignadas por la fracción despejada.
- Cobertura 24/7: presencia en las 168 h semanales. Horas efectivas: jornada menos ausencias.

💡 **Cómo se explica en la clase [B48-C02](../programa/clases/B48/B48-C02-concesion-de-tiempo-de-observacion/CLASE.md):**
- E --> C["x p despejado = horas efectivas"]
- 🎯 **Por qué importa:** Un reparto sin regla clara genera conflicto, y uno sin clima genera promesas incumplibles. La decisión central: ¿cuántas horas se asignan y cuántas se esperan efectivas?

📘 **Dónde se aprende** (2 clases): [B48-C02 · Concesión de tiempo de observación](../programa/clases/B48/B48-C02-concesion-de-tiempo-de-observacion/CLASE.md); [B96-C03 · Roles de control de misión](../programa/clases/B96/B96-C03-roles-de-control-de-mision/CLASE.md).

### Horizonte

- El horizonte es el límite del cielo visible; el cénit, el punto justo encima; el meridiano es la línea imaginaria que une norte, cénit y sur.
- El horizonte es el límite del cielo visto desde el mar.
- El horizonte real es el perfil del paisaje, no una línea plana.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C11](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md):**
- Su altura sobre el horizonte es igual a la latitud: `|φ| = 33,45°` para nuestro lugar.
- La duración del día se obtiene de `cos H₀ = −tan φ · tan δ`, con `H₀` el semiángulo horario del Sol en el horizonte y `día = 2H₀/15° por hora`: da 14,22 h en diciembre, 12,00 h en el equinoccio y 9,78 h en junio.
- 🎯 **Por qué importa:** Antes de cualquier telescopio, la humanidad dedujo mucho del cielo a simple vista. Que el Sol «salga» y «se ponga» es una observación; que la Tierra gire es una interpretación (C05) que explica además el movimiento de todas las estrellas.

📘 **Dónde se aprende** (4 clases): [B01-C11 · Movimiento aparente del Sol y las estrellas](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md); [B02-C07 · Observaciones de Polinesia y navegación oceánica](../programa/clases/B02/B02-C07-observaciones-de-polinesia-y-navegacion-oceanica/CLASE.md); [B02-C08 · Arqueoastronomía y sus métodos](../programa/clases/B02/B02-C08-arqueoastronomia-y-sus-metodos/CLASE.md); [B87-C21 · Control predictivo basado en modelo (MPC) para vehículos espaciales](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md).

### Horizonte de partículas

- El horizonte de partículas comóvil `η = ∫ c dz/H`.

🎯 **Por qué importa (clase B40-C04):** Regiones del fondo separadas más de un grado nunca se comunicaron en el modelo sin inflación, y la curvatura tendría que ser fantásticamente pequeña al principio. La decisión central: ¿qué tan grande es el problema, en números?

📘 **Dónde se aprende** (1 clase): [B40-C04 · Problemas del horizonte y de la planitud](../programa/clases/B40/B40-C04-problemas-del-horizonte-y-de-la-planitud/CLASE.md).

### Horizonte de predicción

- El horizonte de predicción es el tiempo en que un error inicial `δ₀` alcanza una tolerancia `δ_f`: `n_h = ln(δ_f/δ₀)/λ`.

🎯 **Por qué importa (clase B73-C13):** Un sistema determinista puede ser impredecible a largo plazo: el error de medida se amplifica exponencialmente y fija un horizonte más allá del cual la predicción no vale, por más cómputo que se use. La decisión central: ¿hasta cuándo puedo confiar en una integración y cómo reconozco el régimen caótico?

📘 **Dónde se aprende** (1 clase): [B73-C13 · Caos determinista](../programa/clases/B73/B73-C13-caos-determinista/CLASE.md).

### Horizonte de sucesos

- El horizonte de sucesos es la superficie de no retorno.

🎯 **Por qué importa (clase B27-C07):** El espín cambia el ISCO y, con él, cuánta energía se libera: de `5,7 %` a más de `30 %` de la masa en reposo. La decisión central: ¿dónde están el horizonte y el ISCO para un espín dado y qué eficiencia implica?

📘 **Dónde se aprende** (1 clase): [B27-C07 · Métricas de agujeros negros](../programa/clases/B27/B27-C07-metricas-de-agujeros-negros/CLASE.md).

### Horizonte local

- El horizonte local es el círculo máximo que separa la mitad visible de la oculta; el cenit es el punto sobre tu cabeza y el nadir su opuesto.

🎯 **Por qué importa (clase B08-C02):** Alguien en Punta Arenas ve girar algunas estrellas sin ponerse jamás; alguien en el valle del Elqui las ve rozar el horizonte, y alguien en el hemisferio norte no las ve nunca. Entender por qué evita comprar un telescopio para un objeto que no sale en tu cielo.

📘 **Dónde se aprende** (1 clase): [B08-C02 · Esfera celeste y horizonte local](../programa/clases/B08/B08-C02-esfera-celeste-y-horizonte-local/CLASE.md).

### Horizonte sonoro

- El horizonte sonoro `r_s = ∫ c_s da/(a²H)`.

🎯 **Por qué importa (clase B36-C07):** Una regla estándar permite medir distancias si se conoce su longitud. La decisión central: ¿cuánto mide la regla y cuál es la precisión con que se puede medir su dilatación?

📘 **Dónde se aprende** (2 clases): [B36-C07 · Oscilaciones acústicas bariónicas como regla estándar](../programa/clases/B36/B36-C07-oscilaciones-acusticas-barionicas-como-regla-estandar/CLASE.md); [B40-C07 · Espectro angular de potencias del CMB](../programa/clases/B40/B40-C07-espectro-angular-de-potencias-del-cmb/CLASE.md).

### Householder

- Halley: `x ← x − 2δ T'/(2T'² − δ T'')`. Householder de tercer orden usa también `T'''`.

💡 **Cómo se explica en la clase [B82-C06](../programa/clases/B82/B82-C06-algoritmos-iterativos-para-lambert-gooding-izzo/CLASE.md):**
- De las razones de logaritmos, el orden aparente es ≈ 2 en Newton, ≈ 3 en Halley y mayor en Householder (el error llega al redondeo en un paso).
- TX --> P["paso Newton / Halley / Householder"]
- 🎯 **Por qué importa:** La velocidad de un solucionador importa cuando se evalúan millones de transferencias. La decisión central: ¿cuántas iteraciones necesita cada método, de qué depende, y qué garantiza el valor inicial?

📘 **Dónde se aprende** (1 clase): [B82-C06 · Algoritmos iterativos para Lambert (Gooding, Izzo)](../programa/clases/B82/B82-C06-algoritmos-iterativos-para-lambert-gooding-izzo/CLASE.md).

### Huaca

- Una huaca es un lugar sagrado en el mundo andino.

🎯 **Por qué importa (clase B02-C05):** Hablar de «astronomía andina» en singular es un error: los Andes reúnen sociedades de épocas y regiones muy distintas. La pregunta motivadora es: ¿cómo se estudia respetuosamente un cielo que otra cultura leyó de otra manera, sin imponerle nuestras categorías y sin inventar lo que las fuentes no dicen?

📘 **Dónde se aprende** (1 clase): [B02-C05 · Cosmovisiones andinas del cielo](../programa/clases/B02/B02-C05-cosmovisiones-andinas-del-cielo/CLASE.md).

### Huber

- Un M-estimador minimiza una suma de pérdidas que crecen más despacio que el cuadrado; el de Huber usa pérdida cuadrática para residuos pequeños y lineal para grandes, y se calcula por mínimos cuadrados reponderados iterativamente (IRLS), con peso `w = 1` si `|r|/σ̂ ≤ k` y `w = k σ̂/|r|` si no (`k = 1,345` es el valor convencional).

💡 **Cómo se explica en la clase [B12-C11](../programa/clases/B12/B12-C11-regresion-robusta/CLASE.md):**
- Sin atípicos: OLS `b = 0,3855`, Huber `0,3836`, Theil–Sen `0,3827` (el ruido hace que la pendiente de la muestra sea algo menor que `0,40`).
- Con los tres atípicos: OLS `b = 0,7337, a = 2,300` (casi el doble de la pendiente y la mitad del intercepto), Huber `b = 0,4263, a = 4,852` y Theil–Sen `b = 0,4242, a = 4,940`.
- 🎯 **Por qué importa:** Los datos reales traen errores de transmisión, rayos cósmicos en un detector, una lectura perdida o un salto del sensor. Un solo punto muy alejado puede torcer la recta de mínimos cuadrados y producir parámetros y predicciones erróneos con errores típicos pequeños y engañosos.

📘 **Dónde se aprende** (1 clase): [B12-C11 · Regresión robusta](../programa/clases/B12/B12-C11-regresion-robusta/CLASE.md).

### Huber / IRLS

- Atípico: dato que no sigue el modelo. Huber / IRLS: pesos `w = min(1, δ/|r|)` reajustados iterativamente (la teoría de M-estimadores no se consultó).

🎯 **Por qué importa (clase B99-C07):** Un estimador que funciona en el laboratorio puede fallar sin avisar cuando el entorno empeora. La decisión central: ¿qué estimador usar, cómo detectar que el entorno no determina el movimiento y cuándo dejar de confiar en el mapa?

📘 **Dónde se aprende** (1 clase): [B99-C07 · Robustez del mapeo ante entornos degradados](../programa/clases/B99/B99-C07-robustez-del-mapeo-ante-entornos-degradados/CLASE.md).

### Hueco

- Un hueco (*gap*) es un tramo sin datos.
- El hueco es el tiempo sin contacto entre pases.
- Paquete: unidad de datos con número de secuencia. Hueco: rango de números faltantes.

💡 **Cómo se explica en la clase [B15-C01](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md):**
- En el laboratorio, la pendiente real es `−1,000 × 10⁻⁴` por día y el ajuste da `−2,238 × 10⁻⁴`: la modulación de 2,5 días contamina una ventana de 7 días (2,8 periodos) y el hueco empeora el efecto.
- Lo que no debe hacerse es olvidar el hueco y tratar la serie como equiespaciada.
- 🎯 **Por qué importa:** Un telescopio espacial mide el brillo de una estrella cada dos minutos durante semanas. Lo que llega a tierra no es una curva continua, sino una tabla de números.

📘 **Dónde se aprende** (4 clases): [B15-C01 · Series temporales discretas](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md); [B15-C19 · Reconstrucción por datos incompletos](../programa/clases/B15/B15-C19-reconstruccion-por-datos-incompletos/CLASE.md); [B83-C03 · Concepto de operaciones CONOPS](../programa/clases/B83/B83-C03-concepto-de-operaciones-conops/CLASE.md); [B96-C16 · Gestión de datos científicos](../programa/clases/B96/B96-C16-gestion-de-datos-cientificos/CLASE.md).

### Hueco de autoridad

- Un hueco de autoridad es un intervalo en el que nadie puede comandar.

🎯 **Por qué importa (clase B98-C08):** Los relevos fallan en los bordes: un «es tuyo» que no llega deja el vehículo sin dueño, y un «lo sigo yo» sin confirmar deja a dos operadores dando órdenes. La decisión central: ¿cómo se garantiza que siempre hay exactamente un operador con autoridad, o que las órdenes de uno antiguo no se acepten?

📘 **Dónde se aprende** (1 clase): [B98-C08 · Protocolos de relevo de control entre operadores](../programa/clases/B98/B98-C08-protocolos-de-relevo-de-control-entre-operadores/CLASE.md).

### Hueco de Kirkwood

- Un hueco de Kirkwood es una región con pocos asteroides cerca de una resonancia.

🎯 **Por qué importa (clase B58-C02):** Predecir la posición de un asteroide dentro de décadas exige un integrador que se pueda verificar. Saber que un esquema numérico converge con el orden esperado es lo que da confianza antes de añadir perturbaciones.

📘 **Dónde se aprende** (1 clase): [B58-C02 · Dinámica de asteroides](../programa/clases/B58/B58-C02-dinamica-de-asteroides/CLASE.md).

### Hueco de purga

- Un hueco de purga es un margen entre entrenamiento y prueba al menos tan largo como el tiempo de correlación.

💡 **Cómo se explica en la clase [B17-C09](../programa/clases/B17/B17-C09-prevencion-de-fuga-de-datos/CLASE.md):**
- Si serán de épocas futuras, parte por tiempo (`TimeSeriesSplit` o bloques) con hueco de purga.
- 🎯 **Por qué importa:** Un equipo anuncia una exactitud del 95 % para clasificar señales; al aplicarlo a datos de una campaña nueva, baja al 55 %. Nadie mintió: la validación estaba mal hecha.

📘 **Dónde se aprende** (1 clase): [B17-C09 · Prevención de fuga de datos](../programa/clases/B17/B17-C09-prevencion-de-fuga-de-datos/CLASE.md).

### Huecos

- Los huecos son espacios sin uso por la forma de lo instalado.

💡 **Cómo se explica en la clase [B109-C07](../programa/clases/B109/B109-C07-asignacion-de-volumenes-habitables-por-tripulante/CLASE.md):**
- Según el informe del HRP, el NHV es el volumen que queda tras descontar el equipo desplegado, el almacenamiento, la basura y los huecos que reducen el volumen funcional.
- Con `V = 127 m³` (Burke et al.) y descuentos ilustrativos de `25 %` (equipo, `31,75 m³`), `12 %` (almacenamiento, `15,24`), `10 %` (huecos, `12,70`) y `2 %` (basura, `2,54`), la suma es `49 %` y el NHV es `64,77 m³`.
- 🎯 **Por qué importa:** Una cifra de «metros cúbicos por persona» sin decir qué se descontó no se puede comparar. La decisión central: ¿cuánto volumen utilizable queda por tripulante y qué tan sensible es a lo que se descuenta?

📘 **Dónde se aprende** (1 clase): [B109-C07 · Asignación de volúmenes habitables por tripulante](../programa/clases/B109/B109-C07-asignacion-de-volumenes-habitables-por-tripulante/CLASE.md).

### Huella

- Una huella (*hash*) es un número de longitud fija calculado a partir del contenido de un archivo; si el contenido cambia, la huella cambia.
- Una huella (*hash*) es un resumen criptográfico (aquí SHA-256) de la configuración y de la trayectoria redondeada; si cualquier cosa cambia, cambia la huella.
- Una huella (*hash*) es un resumen que cambia si cambia el contenido.
- *(y 11 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C19](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md):**
- Por ejemplo: `"""Devuelve la huella SHA-256 (hexadecimal) del contenido de un archivo."""`.
- (fuente, fecha, huella y licencia), ¿qué resultados produce y cómo se comprueban?
- 🎯 **Por qué importa:** Un resultado que solo su autor puede obtener, y solo el día en que lo obtuvo, es una anécdota. Cuando pasan seis meses, no sabrás con qué datos, con qué versión ni con qué semilla lo generaste.

📘 **Dónde se aprende** (14 clases): [B07-C19 · Documentación y reproducibilidad](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md); [B11-C20 · Propagador reproducible de trayectoria](../programa/clases/B11/B11-C20-propagador-reproducible-de-trayectoria/CLASE.md); [B12-C23 · Diagnóstico de convergencia y reproducibilidad de cadenas MCMC](../programa/clases/B12/B12-C23-diagnostico-de-convergencia-y-reproducibilidad-de-cadenas-mcmc/CLASE.md); [B28-C17 · Archivos de eventos multimensajero](../programa/clases/B28/B28-C17-archivos-de-eventos-multimensajero/CLASE.md); [B28-C20 · Caso de estudio de evento combinado](../programa/clases/B28/B28-C20-caso-de-estudio-de-evento-combinado/CLASE.md); [B42-C17 · Estrellas guía artificiales](../programa/clases/B42/B42-C17-estrellas-guia-artificiales/CLASE.md) y 8 más.

### Huella del cálculo

- La huella del cálculo es el hash del registro canónico.

💡 **Cómo se explica en la clase [B23-C07](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md):**
- R --> H["Huella del cálculo<br/>(SHA-256)"]
- 🎯 **Por qué importa:** Un informe dice «el modelo reproduce la posición con un error de 8,21 × 10⁻⁴ au». Seis meses después, nadie sabe con qué versión del código, qué archivo de datos ni qué tolerancia se calculó, y el número no se puede reproducir ni defender.

📘 **Dónde se aprende** (1 clase): [B23-C07 · Trazabilidad científica de resultados](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md).

### Huella del entorno

- La huella del entorno es el registro de las versiones de Python, plataforma y bibliotecas con que se ejecutó un análisis.

💡 **Cómo se explica en la clase [B14-C12](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md):**
- Registra la huella del entorno junto al resultado del análisis.
- 🎯 **Por qué importa:** Tu análisis dio un período de 5553,624562 s en 2026. Un colega lo ejecuta con otra versión de SciPy y obtiene un cierre distinto; otro usa Python más antiguo y falla al importar. «En mi máquina funciona» no es un resultado científico.

📘 **Dónde se aprende** (1 clase): [B14-C12 · Ejecución reproducible con uv](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md).

### Huella del protocolo

- La huella del protocolo es el SHA-256 de su texto normalizado.

🎯 **Por qué importa (clase B14-C23):** Tienes una curva de luz y muchas formas de analizarla: otro filtro, otra ventana, otro modelo, otra prueba. Si pruebas veinte y comunicas la que «sale», el resultado casi seguro parece significativo aunque no haya nada.

📘 **Dónde se aprende** (1 clase): [B14-C23 · Protocolo preregistrado de análisis](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md).

### Huella encadenada

- La huella encadenada liga cada registro con el anterior.

🎯 **Por qué importa (clase B118-C21):** B48-C11 trata la calidad de datos astronómicos; ninguna clase evalúa datos de vigilancia (latencia, cobertura, trazabilidad). Una conjunción se evalúa con datos que ya envejecieron; un dato sin historial no se puede auditar.

📘 **Dónde se aprende** (1 clase): [B118-C21 · Calidad, latencia y trazabilidad de datos de vigilancia espacial](../programa/clases/B118/B118-C21-calidad-latencia-y-trazabilidad-de-datos-de-vigilancia-espacial/CLASE.md).

### Huérfano

- Un huérfano es un caso sin requisito válido.
- Un resultado huérfano no tiene actividad o no tiene ítem.

🎯 **Por qué importa (clase B88-C20):** Un requisito sin caso es una promesa sin evidencia; un caso sin requisito es esfuerzo sin objeto. La decisión central: ¿cada requisito tiene al menos un caso adecuado, y cada caso responde a un requisito?

📘 **Dónde se aprende** (2 clases): [B88-C20 · Plan de verificación de computador de vuelo](../programa/clases/B88/B88-C20-plan-de-verificacion-de-computador-de-vuelo/CLASE.md); [B131-C02 · Resultados de aprendizaje observables en astronomía](../programa/clases/B131/B131-C02-resultados-de-aprendizaje-observables-en-astronomia/CLASE.md).

### Hugoniot

- La Hugoniot relaciona la velocidad del choque con la de partícula.

💡 **Cómo se explica en la clase [B61-C05](../programa/clases/B61/B61-C05-fusion-por-impacto-y-metamorfismo-de-choque/CLASE.md):**
- ⚠️ **Error frecuente:** Presentar la Hugoniot ilustrativa como medida. Se corrige con la sección 9.
- 🎯 **Por qué importa:** Las rocas con rasgos de choque son la evidencia de un impacto. La decisión central: ¿qué presión produce cada efecto y cuánta roca se funde?

📘 **Dónde se aprende** (1 clase): [B61-C05 · Fusión por impacto y metamorfismo de choque](../programa/clases/B61/B61-C05-fusion-por-impacto-y-metamorfismo-de-choque/CLASE.md).

### Humedad

- La humedad es la fracción de agua del residuo húmedo.

💡 **Cómo se explica en la clase [B59-C16](../programa/clases/B59/B59-C16-desechos-y-reciclaje/CLASE.md):**
- Humedad más agua de reacción: `5,973 kg/día`, es decir `89,6 %` del residuo húmedo.
- *Descripción textual:* el residuo húmedo se seca; el seco se oxida a CO₂, agua y N₂; el agua de humedad y la de la reacción se recuperan.
- 🎯 **Por qué importa:** Los residuos son una fuente de agua y de dióxido de carbono, pero también consumen oxígeno. La decisión central: ¿cuánto oxígeno cuesta cerrar el residuo y cuánta agua se recupera?

📘 **Dónde se aprende** (1 clase): [B59-C16 · Desechos y reciclaje](../programa/clases/B59/B59-C16-desechos-y-reciclaje/CLASE.md).

### Humedad relativa

- Presión de saturación `e_s(T)`: presión de vapor del aire saturado. Humedad relativa: `p_v/e_s`.

💡 **Cómo se explica en la clase [B106-C07](../programa/clases/B106/B106-C07-gestion-de-humedad/CLASE.md):**
- ⚠️ **Error frecuente:** Confundir humedad relativa con humedad absoluta. Usa `w` o `p_v` (8.1).
- 🎯 **Por qué importa:** Sin convección y con 4 personas, el vapor se acumula, sube la humedad relativa y se condensa en superficies frías. La decisión central: ¿cuánto vapor hay que retirar y con qué superficie fría, sin condensar sobre las paredes?

📘 **Dónde se aprende** (1 clase): [B106-C07 · Gestión de humedad](../programa/clases/B106/B106-C07-gestion-de-humedad/CLASE.md).

### Humo

- Umbral de alarma: concentración que activa el detector. Humo: partículas de la pirólisis o la combustión.

💡 **Cómo se explica en la clase [B106-C17](../programa/clases/B106/B106-C17-prevencion-y-respuesta-a-incendios/CLASE.md):**
- (2018) midieron en la ISS el humo de cinco materiales espaciales y dos detectores: ninguno detectó todos los humos, de modo que los detectores futuros deben probarse con humo de materiales reales de uso espacial.
- *Descripción textual:* el combustible libera calor, produce gases y humo; el humo se diluye con la ventilación y suena la alarma si supera el umbral.
- 🎯 **Por qué importa:** Un incendio en una cabina cerrada no puede salir al exterior: calienta, sube la presión, consume oxígeno y produce CO₂ y humo. La decisión central: ¿qué efectos tiene una cantidad dada de combustible y con qué tiempo y ventilación se puede detectar?

📘 **Dónde se aprende** (1 clase): [B106-C17 · Prevención y respuesta a incendios](../programa/clases/B106/B106-C17-prevencion-y-respuesta-a-incendios/CLASE.md).

### Hurwitz

- La condición de Hurwitz dice que, para que todas las raíces tengan parte real negativa, todos los coeficientes deben ser del mismo signo y distintos de cero (condición necesaria, no suficiente).

💡 **Cómo se explica en la clase [B16-C08](../programa/clases/B16/B16-C08-criterio-de-routh-hurwitz/CLASE.md):**
- Routh–Hurwitz dice cuántas raíces están a la derecha, pero no dónde están ni cuánto margen de ganancia o fase tienes.
- Routh–Hurwitz da el rango simbólico y el número de raíces inestables sin hallarlas.
- 🎯 **Por qué importa:** Al diseñar un lazo, la ganancia `K` es una incógnita que quieres elegir. Calcular las raíces para cada `K` es posible con un computador, pero no da la frontera: el valor exacto de `K` por encima del cual el sistema se desestabiliza.

📘 **Dónde se aprende** (1 clase): [B16-C08 · Criterio de Routh-Hurwitz](../programa/clases/B16/B16-C08-criterio-de-routh-hurwitz/CLASE.md).

### Hα

- Un astrónomo apunta un espectrógrafo a una galaxia y registra que una línea característica del hidrógeno, llamada Hα, aparece en 662,9 nm.

🎯 **Por qué importa (clase B01-C01):** Seguramente has leído que «el universo tiene 13 800 millones de años» o que «el universo observable mide 93 000 millones de años luz». Son frases que se repiten con total seguridad.

📘 **Dónde se aprende** (1 clase): [B01-C01 · Naturaleza del universo](../programa/clases/B01/B01-C01-naturaleza-del-universo/CLASE.md).
