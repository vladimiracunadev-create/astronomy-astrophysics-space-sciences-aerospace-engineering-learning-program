# Términos · C (parte 2 de 4)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · **C** · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-c.md) · **2** · [3](terminos-c-3.md) · [4](terminos-c-4.md)

### Centro de masa

- El centro de masa (`x_cg`) es `Σ m x/Σ m`.

💡 **Cómo se explica en la clase [B77-C22](../programa/clases/B77/B77-C22-centro-de-masa-y-su-variacion-con-el-consumo-de-propelente/CLASE.md):**
- El centro de masa no se mueve de forma monótona: se corre hacia la cola hasta `11,27 m` (a `25 %` de propelente) y luego vuelve a `10,60 m`, porque primero se vacía el tanque superior (delante) y después el inferior.
- *Descripción textual:* la fracción de propelente restante fija la masa y la longitud de cada columna de líquido; con los elementos secos se obtienen el centro de masa, la inercia y el margen, y las rebanadas comprueban la forma cerrada.
- ⚠️ **Error frecuente:** Usar el centro de masa inicial para todo el vuelo. Se corrige con 8.3.
- 🎯 **Por qué importa:** El control de actitud se diseña para una masa, un centro de masa y una inercia que ya no son los mismos al final del quemado. La decisión central: ¿cuánto se mueve el centro de masa, cuánto cae la inercia y qué le pasa al margen?
- 🔗 **Se estudia junto con:** momento de inercia de cabeceo, columna de líquido, teorema de ejes paralelos, oleaje.

📘 **Dónde se aprende** (1 clase): [B77-C22 · Centro de masa y su variación con el consumo de propelente](../programa/clases/B77/B77-C22-centro-de-masa-y-su-variacion-con-el-consumo-de-propelente/CLASE.md).

### Centro de masa (CG)

- Margen de separación: margen de que la unión no se abra. Centro de masa (CG): punto promedio de la masa.

💡 **Cómo se explica en la clase [B90-C06](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md):**
- Un CubeSat 3U de siete piezas suma 3,25 kg, con centro de masa en (1,85; −1,11; 22,92) mm, dentro de los límites de ±20, ±20 y ±70 mm.
- Calcular el centro de masa y el tensor de inercia de un ensamble por ejes paralelos.
- 🎯 **Por qué importa:** Un perno mal apretado se afloja con la vibración o se rompe por exceso de carga; un centro de masa fuera de rango desvía la nave en el despliegue. La decisión central: ¿qué par de apriete garantiza que la unión no se separe ni se plastifique, y el conjunto queda dentro de los límites de masa?
- 🔗 **Se estudia junto con:** Precarga, Coeficiente de par K, Factor de carga φ, Margen de separación.

📘 **Dónde se aprende** (1 clase): [B90-C06 · Integración mecánica de subsistemas](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md).

### Centro de masas

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B31-C15](../programa/clases/B31/B31-C15-fisica-de-aceleradores/CLASE.md):**
- El script [aceleradores.py](aceleradores.py) calcula el momento, las pérdidas y la energía en el centro de masas (comprueba el coeficiente a `10⁻¹²` y el cociente de pérdidas a `5 × 10⁻⁴`).
- 🎯 **Por qué importa:** El diseño de un acelerador depende de cuánta energía se pierde por radiación y de cuánta energía útil se obtiene. La decisión central: ¿qué campo y qué radio se necesitan y por qué los electrones pierden tanto?
- 🔗 **Se estudia junto con:** rigidez magnética, pérdida por vuelta, ciclotrón, colisionador.

📘 **Dónde se aprende** (1 clase): [B31-C15 · Física de aceleradores](../programa/clases/B31/B31-C15-fisica-de-aceleradores/CLASE.md).

### Centro del píxel

- El centro del píxel es su punto medio; la esquina su punto superior izquierdo.

💡 **Cómo se explica en la clase [B14-C26](../programa/clases/B14/B14-C26-formatos-de-datos-raster-geoespaciales-geotiff-y-cog/CLASE.md):**
- Con la convención «el píxel `(fila, col)` cubre desde `lon0 + col·dx` hasta `lon0 + (col+1)·dx` y desde `lat0 − (fila+1)·dy` hasta `lat0 − fila·dy`», el centro del píxel `(0, 0)` es `(10,0005°; 39,9995°)` y la esquina `(10,0°; 40,0°)` cae en el píxel `(0, 0)`.
- Esta convención se definió en la clase; no consulté la del estándar GeoTIFF, y confundir esquina y centro desplaza todo medio píxel (0,0005° ≈ 55 m en latitud).
- ⚠️ **Error frecuente:** Confundir esquina y centro del píxel. Se corrige con los ejercicios 6 y 10.
- 🎯 **Por qué importa:** Una escena de satélite pesa cientos de megabytes y tú necesitas un recuadro de 100 × 120 píxeles. Si el formato obliga a leer todo el archivo, gastas tiempo y ancho de banda.
- 🔗 **Se estudia junto con:** ráster, GeoTIFF, tesela, directorio de teselas.

📘 **Dónde se aprende** (1 clase): [B14-C26 · Formatos de datos ráster geoespaciales: GeoTIFF y COG](../programa/clases/B14/B14-C26-formatos-de-datos-raster-geoespaciales-geotiff-y-cog/CLASE.md).

### Centro radial

- El centro radial `x_c = 4x0 + 2ẏ0/n` es constante del movimiento.

💡 **Cómo se explica en la clase [B76-C15](../programa/clases/B76/B76-C15-control-de-formacion-satelital/CLASE.md):**
- El centro radial pasa a `x_c = 4x0 + 2ẏ0/n = −1,0000 m`.
- *Descripción textual:* una elipse de radio `ρ` se cierra sola; un error de semieje equivale a un error de velocidad que desplaza el centro radial y crea una deriva por órbita; un impulso opuesto la anula y su suma anual es el presupuesto.
- 🎯 **Por qué importa:** Un error de un metro en el semieje parece nada y deriva nueve metros por órbita. La decisión central: ¿cuánto se desvía una formación por un error de inserción y cuánto `Δv` cuesta mantenerla?
- 🔗 **Se estudia junto con:** elipse 2:1, deriva por órbita, error de semieje.

📘 **Dónde se aprende** (1 clase): [B76-C15 · Control de formación satelital](../programa/clases/B76/B76-C15-control-de-formacion-satelital/CLASE.md).

### Centro×centro

- Un punto es silla×centro si tiene un par real y un par imaginario, y centro×centro si tiene dos pares imaginarios.

💡 **Cómo se explica en la clase [B73-C04](../programa/clases/B73/B73-C04-estabilidad-local-de-lagrange/CLASE.md):**
- Todos son silla×centro: una perturbación crece como `e^{at}`.
- S -->|"una positiva"| SC["silla x centro: inestable"]
- ⚠️ **Error frecuente:** Concluir estabilidad total de un centro×centro lineal. Se corrige con 8.5.
- 🎯 **Por qué importa:** Que un punto sea de equilibrio no dice si una nave se queda o se va. Los autovalores dicen cuánto tiempo tienes antes de corregir la posición y si un grupo de asteroides puede quedarse en L4.
- 🔗 **Se estudia junto con:** ecuación característica, silla×centro, estabilidad lineal, tiempo de crecimiento.

📘 **Dónde se aprende** (1 clase): [B73-C04 · Estabilidad local de Lagrange](../programa/clases/B73/B73-C04-estabilidad-local-de-lagrange/CLASE.md).

### Centroide

- El centroide tiene ruido `σ_px`; el ruido angular por estrella es `σ_a = atan(σ_px/f)`.
- El centroide de una línea.

💡 **Cómo se explica en la clase [B42-C14](../programa/clases/B42/B42-C14-sensores-shack-hartmann/CLASE.md):**
- Con `0,5 arcsec/px` un centroide de `0,05 px` es `0,025 arcsec = 1,212 × 10⁻⁷ rad` de pendiente y, sobre `0,2 m`, `24,24 nm` de camino óptico.
- Con mancha gaussiana de `σ = 0,85 px`, ventana de 8 × 8 y lectura de 3 e⁻ (ilustrativos) 400 fotones dan un centroide con `0,1461 px` (previsto `0,1446`); un centroide de `0,05 px` es `24,24 nm` de camino óptico en una subapertura de `0,2 m`.
- 🎯 **Por qué importa:** El Shack-Hartmann es el sensor más usado en óptica adaptativa. La decisión central: ¿cuántos fotones hacen falta por subapertura para que el centroide sea preciso?
- 🔗 **Se estudia junto con:** subapertura, ruido de fotones, de lectura, ventana.

📘 **Dónde se aprende** (4 clases): [B42-C14 · Sensores Shack-Hartmann](../programa/clases/B42/B42-C14-sensores-shack-hartmann/CLASE.md); [B45-C08 · Calibración en longitud de onda](../programa/clases/B45/B45-C08-calibracion-en-longitud-de-onda/CLASE.md); [B45-C10 · Líneas de emisión](../programa/clases/B45/B45-C10-lineas-de-emision/CLASE.md); [B87-C07 · Rastreadores estelares](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md).

### Centroide por momentos

- El centroide por momentos es `Σ I x / Σ I`.

💡 **Cómo se explica en la clase [B74-C02](../programa/clases/B74/B74-C02-observacion-angular-y-astrometria/CLASE.md):**
- Límites: solo ruido de Poisson, centroide por momentos sin ventana; no hay catálogo ni distorsión.
- 🎯 **Por qué importa:** Un ángulo de `0,01″` parece pequeño, pero a un millón de kilómetros son decenas de metros. La decisión central: ¿cuánta incertidumbre angular aporta el detector y cuánta es un efecto físico que hay que modelar (aberración)?
- 🔗 **Se estudia junto con:** escala de placa, PSF, aberración, paralaje.

📘 **Dónde se aprende** (1 clase): [B74-C02 · Observación angular y astrometría](../programa/clases/B74/B74-C02-observacion-angular-y-astrometria/CLASE.md).

### CEP

- El CEP es el radio del círculo horizontal con 50 % de probabilidad; el SEP, de la esfera con 50 %.

💡 **Cómo se explica en la clase [B74-C19](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md):**
- Con `σ = (3; 1,2; 2) m`: RMS 3D `3,8000 m` (muestral `3,8012 m`), percentil 95 de la norma 3D `6,493 m`, SEP (50 %) `3,190 m`, CEP (50 %, horizontal) `2,425 m`.
- Con `N = 50`, el RMS 3D es `3,816 ± 0,245 m`, el percentil 95 `6,316 ± 0,634 m` y el CEP `2,457 ± 0,264 m`.
- ⚠️ **Error frecuente:** Comparar un CEP con un 95 %. Son probabilidades distintas; ver 8.1.
- 🎯 **Por qué importa:** Dos informes pueden decir «3 m» y referirse a cosas distintas (RMS, 50 %, 95 %). La decisión central: ¿qué métrica comunica el riesgo que importa, con qué probabilidad y con qué incertidumbre muestral?
- 🔗 **Se estudia junto con:** RMS 3D, SEP, 2DRMS, percentil.

📘 **Dónde se aprende** (1 clase): [B74-C19 · Métricas de precisión de navegación](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md).

### Cercana

- Una variante cercana cambia los números; una media, además el cuerpo central o la magnitud pedida; una lejana, también el contexto y las unidades.

💡 **Cómo se explica en la clase [B131-C07](../programa/clases/B131/B131-C07-ejercicios-de-transferencia/CLASE.md):**
- Cercana (1): cuerpo con `P = 15,9 años` alrededor del Sol, se pide `a` → `6,323 UA`.
- La cercana mide ejecución del procedimiento; la media, si el estudiante reconoce el papel de `M`; la lejana, si entiende la ley como relación entre magnitudes y no como una receta en UA y años.
- 🎯 **Por qué importa:** Resolver bien un problema practicado puede ser memoria. La decisión central: ¿qué debe cambiar para que el ejercicio mida que el estudiante comprendió la ley y no el procedimiento?
- 🔗 **Se estudia junto con:** Transferencia, media, lejana, clave.

📘 **Dónde se aprende** (1 clase): [B131-C07 · Ejercicios de transferencia](../programa/clases/B131/B131-C07-ejercicios-de-transferencia/CLASE.md).

### Cercha Serrurier

- La cercha Serrurier son dos brazos que soportan los extremos.

💡 **Cómo se explica en la clase [B43-C10](../programa/clases/B43/B43-C10-estructura-de-tubo-optico/CLASE.md):**
- Hallar la relación de inercias de una cercha Serrurier.
- 🎯 **Por qué importa:** Lo que decolima no es la flexión sino la flexión diferencial entre primario y secundario. La decisión central: ¿qué rigideces hacen que los dos extremos se muevan lo mismo, de modo que el eje óptico solo se desplace en paralelo?
- 🔗 **Se estudia junto con:** rigidez a flexión, flecha de voladizo, descentrado diferencial, tubo delgado.

📘 **Dónde se aprende** (1 clase): [B43-C10 · Estructura de tubo óptico](../programa/clases/B43/B43-C10-estructura-de-tubo-optico/CLASE.md).

### Cero

- Un espacio vectorial real es un conjunto `V` con una suma `u + v` y un producto por escalares reales `a·u` que cumplen ocho propiedades: la suma es conmutativa y asociativa; existe un vector cero que no cambia nada; todo vector tiene un opuesto; y el producto por escalares es distributivo sobre la suma de vectores y de escalares, asociativo y con `1·u = u` (S1 usa `ℝⁿ` con estas operaciones en §1.2(v)).

💡 **Cómo se explica en la clase [B10-C01](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md):**
- La palabra clave es homogénea (lado derecho cero).
- Con lado derecho distinto de cero no hay subespacio (el origen no es solución).
- ⚠️ **Error frecuente:** Olvidar comprobar el cero. Se corrige con el ejercicio 3.
- 🎯 **Por qué importa:** El estado de un satélite en un instante se describe con seis números: tres de posición y tres de velocidad. Los programas de navegación suman, restan y multiplican por escalares esos «vectores de estado» todo el tiempo: promedian estimaciones, corrigen con un error medido, propagan pequeñas perturbaciones.
- 🔗 **Se estudia junto con:** espacio vectorial real, opuesto, escalar, subespacio.

📘 **Dónde se aprende** (1 clase): [B10-C01 · Espacios vectoriales](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md).

### Ceros

- Sus polos son las raíces del denominador; sus ceros, las del numerador.

💡 **Cómo se explica en la clase [B16-C05](../programa/clases/B16/B16-C05-funciones-de-transferencia/CLASE.md):**
- Un cero cambia los coeficientes de esas exponenciales: no crea movimientos nuevos, pero afecta a cuánto pesan.
- Un sistema de segundo orden sin ceros es `ωn²/(s² + 2ζωn s + ωn²)`.
- 🎯 **Por qué importa:** Un ingeniero que diseña el control de actitud de un telescopio revisa decenas de variantes de ganancias.
- 🔗 **Se estudia junto con:** transformada de Laplace, función de transferencia, polos, orden.

📘 **Dónde se aprende** (1 clase): [B16-C05 · Funciones de transferencia](../programa/clases/B16/B16-C05-funciones-de-transferencia/CLASE.md).

### Cerrojo

- Un cerrojo (*lock*) deja pasar a un solo hilo a la vez por un trozo de código.

💡 **Cómo se explica en la clase [B18-C01](../programa/clases/B18/B18-C01-procesos-hilos-y-concurrencia/CLASE.md):**
- La defensa es un cerrojo (`with cerrojo: cuenta += 1`) o, mejor, no compartir datos mutables: que cada hilo devuelva su resultado y combinarlos al final.
- Reconocer y corregir una condición de carrera con un cerrojo.
- 🎯 **Por qué importa:** Tienes ocho órbitas simuladas que propagar y un portátil con varios núcleos. La tentación es «lanzar ocho hilos y listo».
- 🔗 **Se estudia junto con:** proceso, hilo, comparten, concurrencia.

📘 **Dónde se aprende** (1 clase): [B18-C01 · Procesos, hilos y concurrencia](../programa/clases/B18/B18-C01-procesos-hilos-y-concurrencia/CLASE.md).

### Cesión

- La cesión es la parte del riesgo transferida.

💡 **Contexto en la clase [B127-C07](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md):**
- 🎯 **Por qué importa:** El riesgo espacial se reparte mediante reaseguro; no había clase al respecto. La decisión central: ¿qué parte del riesgo se cede y cuánto cuesta reducir la cola?
- 🔗 **Se estudia junto con:** cuota parte, exceso de pérdida, prioridad, límite.

📘 **Dónde se aprende** (1 clase): [B127-C07 · Reaseguro espacial](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md).

### Chebyshev

- Los nodos equiespaciados están a igual distancia; los de Chebyshev son `cos(π(2i + 1)/(2(n + 1)))` y se acumulan hacia los extremos.

💡 **Cómo se explica en la clase [B11-C18](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md):**
- Con nodos de Chebyshev decrece: `0,40`, `0,17`, `0,069`, `0,033`, `0,015`.
- F -->|Chebyshev| H["Error decrece con n"]
- 🎯 **Por qué importa:** Si una nave debe saber dónde está un cuerpo en un instante que no figura en la tabla, interpola. Si interpola con un grado equivocado o fuera del rango, el error puede pasar de metros a miles de kilómetros sin que el programa avise.
- 🔗 **Se estudia junto con:** polinomio de Lagrange, polinomio nodal, error, Interpolar.

📘 **Dónde se aprende** (1 clase): [B11-C18 · Interpolación y extrapolación](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md).

### Checksum

- El checksum (columna 69) es la suma de los dígitos (el signo menos vale 1) módulo 10.

💡 **Cómo se explica en la clase [B74-C29](../programa/clases/B74/B74-C29-formatos-tle-y-omm-de-elementos-orbitales/CLASE.md):**
- *Descripción textual:* los elementos se escriben en un TLE de columnas fijas, se calcula el checksum, se lee por columnas, se obtienen magnitudes de dos cuerpos y un mensaje tipo OMM; el checksum determina qué errores se detectan.
- Ejercicio 1 · guiado. Calcula el checksum de `1 2 3` (solo cuenta los dígitos).
- ⚠️ **Error frecuente:** Creer que el checksum protege contra todo error. No detecta transposiciones; ver 8.3.
- 🎯 **Por qué importa:** Un TLE mal copiado o mal leído da una órbita equivocada sin avisar. La decisión central: ¿qué errores detecta la suma de verificación, qué resolución tiene cada campo y qué significan realmente esos «elementos medios»?
- 🔗 **Se estudia junto con:** TLE, movimiento medio, OMM, teoría de elementos medios.

📘 **Dónde se aprende** (1 clase): [B74-C29 · Formatos TLE y OMM de elementos orbitales](../programa/clases/B74/B74-C29-formatos-tle-y-omm-de-elementos-orbitales/CLASE.md).

### Chi cuadrado

- El chi cuadrado `χ² = Σ(xᵢ − x_w)²/uᵢ²` mide la dispersión respecto de la media ponderada en unidades de incertidumbre.
- El chi cuadrado mide el ajuste;

💡 **Cómo se explica en la clase [B45-C13](../programa/clases/B45/B45-C13-temperatura-y-espectro-de-cuerpo-negro/CLASE.md):**
- Ajustar `T` y amplitud por mínimos cuadrados.
- 🎯 **Por qué importa:** La temperatura se estima del color o del espectro, y el pico depende de si se mide por unidad de λ o de ν. La decisión central: ¿qué temperatura y con qué error dan unos flujos en banda?
- 🔗 **Se estudia junto con:** ley de Wien, constante, temperatura de color.

📘 **Dónde se aprende** (2 clases): [B13-C18 · Intercomparación de instrumentos](../programa/clases/B13/B13-C18-intercomparacion-de-instrumentos/CLASE.md); [B45-C13 · Temperatura y espectro de cuerpo negro](../programa/clases/B45/B45-C13-temperatura-y-espectro-de-cuerpo-negro/CLASE.md).

### Chi cuadrado de Poisson

- El chi cuadrado de Poisson `Σ (O − E)²/E`.

💡 **Cómo se explica en la clase [B38-C09](../programa/clases/B38/B38-C09-validacion-de-galaxias-simuladas-frente-a-observaciones/CLASE.md):**
- Calcular un chi cuadrado reducido de Poisson.
- 🎯 **Por qué importa:** Una simulación calibrada para coincidir con los datos no queda validada por coincidir con ellos. La decisión central: ¿qué parte del acuerdo es una predicción y qué parte es un ajuste?
- 🔗 **Se estudia junto con:** residuo en dex, función de Schechter, prueba KS, calibración.

📘 **Dónde se aprende** (1 clase): [B38-C09 · Validación de galaxias simuladas frente a observaciones](../programa/clases/B38/B38-C09-validacion-de-galaxias-simuladas-frente-a-observaciones/CLASE.md).

### Chick–Watson

- Flujo pistón (PFR): flujo sin mezcla longitudinal. Chick–Watson: inactivación proporcional a `C·t`.

💡 **Cómo se explica en la clase [B106-C26](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md):**
- Calcular el producto concentración por tiempo de una desinfección de Chick–Watson.
- Desinfeccion de Chick-Watson: log10(N0/N) = k C t, k = 0.5 L/(mg min):
- 🎯 **Por qué importa:** Las aguas grises son el mayor volumen del lazo y su carga orgánica hay que destruirla antes de potabilizar. La decisión central: ¿qué volumen de biorreactor y qué desinfección dan la remoción y la reducción de microorganismos requeridas?
- 🔗 **Se estudia junto con:** Aguas grises, Biorreactor, Mezcla completa (CSTR), Flujo pistón (PFR).

📘 **Dónde se aprende** (1 clase): [B106-C26 · Tratamiento de aguas grises en hábitats](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md).

### Chirp

- El chirp es un pulso cuya frecuencia varía linealmente.
- El chirp es el pulso transmitido.

💡 **Cómo se explica en la clase [B57-C07](../programa/clases/B57/B57-C07-sistemas-radar-sar/CLASE.md):**
- El mayor lóbulo lateral cercano al pico del chirp sin ventana, medido en la simulación, es de `-13,5 dB`; en la práctica se aplican ventanas para bajarlo a costa de ensanchar el pico.
- P["chirp de ancho B y duracion tau"] --> E["eco de un blanco"]
- ⚠️ **Error frecuente:** Presentar el chirp como el de Sentinel-1. Es ilustrativo (sección 5).
- 🎯 **Por qué importa:** La luz visible no atraviesa nubes ni sirve de noche; las microondas sí. Pero un radar no «fotografía»: mide distancia y fase de ecos.
- 🔗 **Se estudia junto con:** filtro adaptado, producto tiempo–ancho de banda, rango oblicuo, rango sobre el suelo.

📘 **Dónde se aprende** (2 clases): [B57-C07 · Sistemas radar SAR](../programa/clases/B57/B57-C07-sistemas-radar-sar/CLASE.md); [B69-C02 · Formación de imágenes SAR](../programa/clases/B69/B69-C02-formacion-de-imagenes-sar/CLASE.md).

### Chirrido

- El chirrido es el aumento conjunto de frecuencia y amplitud.

💡 **Cómo se explica en la clase [B27-C13](../programa/clases/B27/B27-C13-binarias-compactas/CLASE.md):**
- Calcular la masa de chirrido y el tiempo hasta la fusión desde una frecuencia.
- GW170817 (masas iguales 1.37 Msol): masa de chirrido = 1.1927 Msol
- 🎯 **Por qué importa:** La fusión de dos estrellas de neutrones fue el primer evento detectado en ondas gravitacionales y en luz. Saber cuánto falta para una fusión, a qué frecuencia, y cómo la excentricidad la acelera, es la base de toda búsqueda.
- 🔗 **Se estudia junto con:** masa de chirrido, frecuencia gravitacional, tiempo de fusión, orden de cuadrupolo.

📘 **Dónde se aprende** (2 clases): [B27-C13 · Binarias compactas](../programa/clases/B27/B27-C13-binarias-compactas/CLASE.md); [B28-C21 · Formas de onda gravitacionales y filtro acoplado](../programa/clases/B28/B28-C21-formas-de-onda-gravitacionales-y-filtro-acoplado/CLASE.md).

### CHNOPS

- Los elementos CHNOPS (carbono, hidrógeno, nitrógeno, oxígeno, fósforo, azufre) forman la mayor parte de la materia viva conocida.

💡 **Cómo se explica en la clase [B56-C02](../programa/clases/B56/B56-C02-bioquimica-y-metabolismo-terrestre/CLASE.md):**
- Ejercicio 8. Balancea `N₂ + 3 H₂ → 2 NH₃` y di qué elementos de CHNOPS intervienen.
- Ejercicio 10 · transferencia. ¿Por qué la química de CHNOPS no demuestra que toda vida use esos elementos?
- ⚠️ **Error frecuente:** Generalizar CHNOPS a toda la vida posible. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Para buscar vida hay que saber qué hace la vida conocida con la materia: qué elementos usa y de dónde saca energía. La decisión central: dada una reacción metabólica, ¿está balanceada y cuánta energía libre libera o consume por mol?
- 🔗 **Se estudia junto con:** metabolismo, energía libre de Gibbs, energía libre de formación estándar, balance atómico.

📘 **Dónde se aprende** (1 clase): [B56-C02 · Bioquímica y metabolismo terrestre](../programa/clases/B56/B56-C02-bioquimica-y-metabolismo-terrestre/CLASE.md).

### Cholesky

- QR: `A = Q R` con `Q` de columnas ortonormales y `R` triangular superior. Cholesky: `A = L Lᵀ` con `L` triangular inferior de diagonal positiva, para `A` simétrica definida positiva (`xᵀA x > 0` para todo `x ≠ 0`; sus autovalores son positivos, C08).

💡 **Cómo se explica en la clase [B10-C10](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md):**
- Aproximadamente: LU cuesta `2n³/3` operaciones, Cholesky `n³/3` (la mitad, por usar la simetría), QR cerca de `4n³/3` para matrices cuadradas.
- Regla práctica: Cholesky si hay simetría definida positiva;
- ⚠️ **Error frecuente:** Aplicar Cholesky a una matriz que no es definida positiva. Se corrige con los ejercicios 5 y 10.
- 🎯 **Por qué importa:** Un filtro de navegación resuelve el mismo sistema con miles de lados derechos distintos; una simulación necesita muestras aleatorias con una covarianza dada; un ajuste de mínimos cuadrados quiere estabilidad. En cada caso el trabajo se hace una vez al factorizar y luego se reutiliza.
- 🔗 **Se estudia junto con:** factorización, LU, matriz de permutación, QR.

📘 **Dónde se aprende** (1 clase): [B10-C10 · Descomposiciones matriciales](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md).

### Choque

- El choque es una discontinuidad que cruza el flujo.
- La onda de rarefacción, la discontinuidad de contacto y el choque son las tres ondas del tubo de Sod.
- Choque: excitación transitoria breve.

💡 **Cómo se explica en la clase [B30-C14](../programa/clases/B30/B30-C14-choques-y-aceleracion-de-particulas/CLASE.md):**
- Cuanto más fuerte el choque, más duro el espectro (índice menor).
- Límite: partículas de prueba y choque plano.
- 🎯 **Por qué importa:** Las partículas energéticas solares son un riesgo para satélites y astronautas, y los choques de las CME son un origen. La decisión central: ¿qué espectro produce un choque de una compresión dada?
- 🔗 **Se estudia junto con:** razón de compresión, condiciones de Rankine–Hugoniot, aceleración difusiva, índice espectral.

📘 **Dónde se aprende** (3 clases): [B30-C14 · Choques y aceleración de partículas](../programa/clases/B30/B30-C14-choques-y-aceleracion-de-particulas/CLASE.md); [B38-C06 · Hidrodinámica en simulaciones: SPH y métodos de malla](../programa/clases/B38/B38-C06-hidrodinamica-en-simulaciones-sph-y-metodos-de-malla/CLASE.md); [B90-C10 · Ensayos de choque](../programa/clases/B90/B90-C10-ensayos-de-choque/CLASE.md).

### Choque desprendido

- El choque desprendido aparece cuando `θ` supera el máximo.

💡 **Cómo se explica en la clase [B79-C07](../programa/clases/B79/B79-C07-ondas-de-choque-normales-y-oblicuas/CLASE.md):**
- A `M₁ = 2` una deflexión de `30°` supera `θ_máx` y no tiene solución adjunta (choque desprendido).
- Deflexion de 30 grados a M1 = 2: sin solucion oblicua adjunta (choque desprendido)
- 🎯 **Por qué importa:** B30-C14 trata choques astrofísicos, no gasdinámicos. Para tomas de aire, toberas y reentrada hace falta saber cuánto sube la presión y cuánta energía útil se pierde.
- 🔗 **Se estudia junto con:** choque normal, oblicuo, relaciones de Rankine–Hugoniot, débil.

📘 **Dónde se aprende** (1 clase): [B79-C07 · Ondas de choque normales y oblicuas](../programa/clases/B79/B79-C07-ondas-de-choque-normales-y-oblicuas/CLASE.md).

### Choque normal

- Un choque normal es perpendicular al flujo; uno oblicuo está inclinado un ángulo `β` y desvía el flujo un ángulo `θ`.

💡 **Cómo se explica en la clase [B79-C07](../programa/clases/B79/B79-C07-ondas-de-choque-normales-y-oblicuas/CLASE.md):**
- El choque oblicuo se reduce a uno normal con `M_n1 = M₁ sin β`; la componente tangencial se conserva.
- *Descripción textual:* el choque oblicuo se reduce a un choque normal con la componente normal del Mach; las propiedades se verifican con los balances de conservación.
- 🎯 **Por qué importa:** B30-C14 trata choques astrofísicos, no gasdinámicos. Para tomas de aire, toberas y reentrada hace falta saber cuánto sube la presión y cuánta energía útil se pierde.
- 🔗 **Se estudia junto con:** oblicuo, relaciones de Rankine–Hugoniot, débil, fuerte.

📘 **Dónde se aprende** (1 clase): [B79-C07 · Ondas de choque normales y oblicuas](../programa/clases/B79/B79-C07-ondas-de-choque-normales-y-oblicuas/CLASE.md).

### Choque perfectamente inelástico

- Un choque perfectamente inelástico es aquel en que los cuerpos quedan unidos.

💡 **Cómo se explica en la clase [B05-C08](../programa/clases/B05/B05-C08-momento-lineal-e-impulsos/CLASE.md):**
- Resolver un acoplamiento (choque perfectamente inelástico) en una recta.
- En un choque perfectamente inelástico solo se conserva el momento; la energía cinética disminuye (ejercicio 3).
- 🎯 **Por qué importa:** Un cohete en el vacío no tiene nada contra lo que empujar y aun así acelera. La pregunta motivadora es: ¿cómo cambia la velocidad de un cuerpo cuando expulsa masa o cuando choca, si no hay fuerzas externas?
- 🔗 **Se estudia junto con:** momento lineal, impulso, teorema impulso–momento, sistema aislado.

📘 **Dónde se aprende** (1 clase): [B05-C08 · Momento lineal e impulsos](../programa/clases/B05/B05-C08-momento-lineal-e-impulsos/CLASE.md).

### Choque térmico

- El choque térmico crítico es `ΔT = σ_f(1 − ν)/(Eα)`.

💡 **Cómo se explica en la clase [B84-C04](../programa/clases/B84/B84-C04-ceramicos-y-polimeros-espaciales/CLASE.md):**
- Estimar la diferencia de temperatura crítica de choque térmico.
- Transferencia. ¿Por qué una cerámica resiste el calor pero no un choque térmico?
- 🎯 **Por qué importa:** Un metal avisa antes de romper; una cerámica no. Diseñar con la resistencia media de una probeta pequeña sobreestima la de una pieza grande en 40 %.
- 🔗 **Se estudia junto con:** distribución de Weibull, módulo de Weibull, resistencia característica, efecto de tamaño.

📘 **Dónde se aprende** (1 clase): [B84-C04 · Cerámicos y polímeros espaciales](../programa/clases/B84/B84-C04-ceramicos-y-polimeros-espaciales/CLASE.md).

### Chorro estructurado

- El chorro estructurado tiene energía que decrece con el ángulo al eje.

💡 **Contexto en la clase [B28-C12](../programa/clases/B28/B28-C12-modelos-de-emision-conjunta/CLASE.md):**
- **Idea central (modelo mental):** Un foco muy colimado ilumina con intensidad al frente y casi nada a los lados; un halo débil se extiende a mayor ángulo. Quien lo ve de lado recibe poca luz.
- 🎯 **Por qué importa:** Un destello gamma débil puede ser un evento normal visto de lado. Un modelo de emisión conjunta permite relacionar qué se ve en cada mensajero con el ángulo de visión.
- 🔗 **Se estudia junto con:** núcleo, ángulo de visión, exponente Doppler, brillo relativo.

📘 **Dónde se aprende** (1 clase): [B28-C12 · Modelos de emisión conjunta](../programa/clases/B28/B28-C12-modelos-de-emision-conjunta/CLASE.md).

### CI

- Una condrita es un meteorito formado por materiales que no se fundieron del todo; las condritas carbonáceas son ricas en carbono, y las CI son las más primitivas en cuanto a su composición.

💡 **Cómo se explica en la clase [B06-C20](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md):**
- Las CI son las que menos se han modificado, aunque sufrieron alteración por agua y calentamiento, y se les considera una buena aproximación al material no volátil del que se formó el Sistema Solar (S1).
- No se puede concluir que Bennu sea «más rico en carbono que las CI» con tanta seguridad: la comparación mezcla un valor medido en porciones de una muestra (S2) con un cálculo propio a partir de abundancias promedio (S1), con omisiones y sin incertidumbre propagada.
- ⚠️ **Error frecuente:** Tratar la «CI media» como un dato medido. Se corrige con la sección 8.4 y el ejercicio 9.
- 🎯 **Por qué importa:** Hay dos formas de saber de qué está hecho el Sistema Solar. Una es mirar la luz del Sol y deducir su composición; la otra es analizar en laboratorio meteoritos que conservan la composición del material con que se formó.
- 🔗 **Se estudia junto con:** meteorito, condrita, condritas carbonáceas, dex.

📘 **Dónde se aprende** (1 clase): [B06-C20 · Análisis químico introductorio de meteoritos](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md).

### Ciclado

- Bakeout: calentamiento en vacío para expulsar volátiles. Ciclado: repetición de ciclos entre dos temperaturas.

💡 **Cómo se explica en la clase [B90-C12](../programa/clases/B90/B90-C12-vacio-termico-y-ciclos/CLASE.md):**
- Para un año de órbita (5 840 ciclos de −10 a +30 °C), el factor de aceleración de un ciclado de −40 a +60 °C es 12,04, es decir 485 ciclos de ensayo, 42,7 días de cámara.
- Calcular un factor de aceleración de ciclado térmico.
- 🎯 **Por qué importa:** Una nave en órbita baja sufre unos 16 ciclos térmicos por día; no se pueden repetir 5 840 ciclos en tierra. La decisión central: ¿cuántos ciclos de ensayo con mayor amplitud representan un año de órbita y cuánto tarda la campaña?
- 🔗 **Se estudia junto con:** Vacío térmico (TVAC), Bakeout, Presión límite, Factor de aceleración (AF).

📘 **Dónde se aprende** (1 clase): [B90-C12 · Vacío térmico y ciclos](../programa/clases/B90/B90-C12-vacio-termico-y-ciclos/CLASE.md).

### Ciclado térmico

- El ciclado térmico produce fatiga en soldaduras.

💡 **Cómo se explica en la clase [B86-C14](../programa/clases/B86/B86-C14-envejecimiento-de-paneles/CLASE.md):**
- N["ciclos = ciclos/año x t"] --> TH["ciclado térmico"]
- Combinar factores multiplicativos de degradación por radiación, ciclado térmico, contaminación y fallas de cadenas.
- 🎯 **Por qué importa:** Dimensionar un ala con su potencia de inicio de vida deja a la misión sin energía al final. El factor de fin de vida que se usó como `0,85` en la primera clase sale de un cálculo como este.
- 🔗 **Se estudia junto con:** degradación, radiación, contaminación, factor de fin de vida.

📘 **Dónde se aprende** (1 clase): [B86-C14 · Envejecimiento de paneles](../programa/clases/B86/B86-C14-envejecimiento-de-paneles/CLASE.md).

### Cíclico

- El par secular acumula; el cíclico oscila con amplitud `τ_c/n` en `h`.

💡 **Cómo se explica en la clase [B87-C14](../programa/clases/B87/B87-C14-saturacion-y-descarga-de-momento/CLASE.md):**
- Un par cíclico de `20 µN·m` a la frecuencia orbital añade `±0,0181 N·m·s` de oscilación (amplitud `τ_c/n`).
- B87-C14 saturacion y descarga | SINTETICO: par secular (2,-1,4) uN m + 20 uN m ciclico; rueda 0.05 N m s; m_max 0.2 A m^2; 12 orbitas
- 🎯 **Por qué importa:** Una rueda saturada deja de controlar. La decisión central: ¿en cuánto tiempo se satura, cuánto par magnético hace falta para sostener la descarga y qué nivel de momento queda en régimen?
- 🔗 **Se estudia junto con:** saturación, descarga, ley de descarga, par secular.

📘 **Dónde se aprende** (1 clase): [B87-C14 · Saturación y descarga de momento](../programa/clases/B87/B87-C14-saturacion-y-descarga-de-momento/CLASE.md).

### Ciclo

- Un ciclo es un fenómeno que se repite, como una vuelta de la Tierra sobre su eje o de la Luna alrededor de la Tierra.
- Un ciclo es una contradicción.
- Un ciclo es un paso al caliente y al frío.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C04](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md):**
- El tiempo se mide contando ciclos regulares.
- Pero cada ciclo se puede medir de más de una manera, y eso produce unidades distintas.
- 🎯 **Por qué importa:** En 1999 la sonda Mars Climate Orbiter se perdió en la atmósfera de Marte. Según la NASA, el programa en tierra trabajaba en unidades inglesas y el de la sonda en métricas, y esa discrepancia la dirigió demasiado cerca del planeta (S1).
- 🔗 **Se estudia junto con:** período, día solar medio, día sidéreo, año sidéreo.

📘 **Dónde se aprende** (8 clases): [B01-C04 · Espacio y tiempo en ciencia](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md); [B30-C03 · Ciclo de actividad solar](../programa/clases/B30/B30-C03-ciclo-de-actividad-solar/CLASE.md); [B53-C09 · Estratigrafía planetaria](../programa/clases/B53/B53-C09-estratigrafia-planetaria/CLASE.md); [B85-C19 · Ensayos de vacío térmico](../programa/clases/B85/B85-C19-ensayos-de-vacio-termico/CLASE.md); [B97-C25 · Excavación y manejo de regolito con robots](../programa/clases/B97/B97-C25-excavacion-y-manejo-de-regolito-con-robots/CLASE.md); [B109-C03 · Accesos, esclusas y transferencia entre ambientes presurizados](../programa/clases/B109/B109-C03-accesos-esclusas-y-transferencia-entre-ambientes-presurizados/CLASE.md) y 2 más.

### Ciclo anual

- El ciclo anual es la oscilación estacional que se ajusta aparte.

💡 **Cómo se explica en la clase [B57-C12](../programa/clases/B57/B57-C12-oceanografia-desde-orbita/CLASE.md):**
- Un remolino de `0,20 m` de altura y `50 km` de radio característico a `33°` sur (ilustrativo) y una serie mensual de `30` años con una tendencia impuesta de `3 mm/año` (ilustrativa, no es una medición) con ciclo anual de `40 mm` y ruido de `20 mm`.
- ⚠️ **Error frecuente:** Ignorar el ciclo anual. Sesga la pendiente (ejercicio 6).
- 🎯 **Por qué importa:** El océano se mueve lento y se eleva más lento aún. La decisión central: ¿qué pendiente de la superficie equivale a una corriente y cuántos años de datos se necesitan para ver una tendencia de pocos milímetros por año entre un ruido de centímetros?
- 🔗 **Se estudia junto con:** balance geostrófico, anomalía de altura, número de Rossby, tendencia.

📘 **Dónde se aprende** (1 clase): [B57-C12 · Oceanografía desde órbita](../programa/clases/B57/B57-C12-oceanografia-desde-orbita/CLASE.md).

### Ciclo CNO

- El ciclo CNO usa carbono, nitrógeno y oxígeno como catalizadores para el mismo resultado neto.

💡 **Cómo se explica en la clase [B24-C07](../programa/clases/B24/B24-C07-ciclo-cno-y-cadena-proton-proton/CLASE.md):**
- En el ciclo CNO, un protón se une al carbono-12, al nitrógeno-14 y a otros núcleos en secuencia y al final se libera un helio-4 y se recupera el catalizador.
- El ciclo CNO cambia más con la temperatura, de modo que domina en núcleos más calientes (estrellas más masivas) y p–p en núcleos más fríos.
- 🎯 **Por qué importa:** Dos protones se repelen con una fuerza eléctrica enorme; a las temperaturas de una estrella casi ninguno tiene energía para acercarse lo suficiente. Aun así la fusión ocurre, por efecto túnel.
- 🔗 **Se estudia junto con:** cadena protón–protón (p–p), barrera de Coulomb, efecto túnel, energía de Gamow.

📘 **Dónde se aprende** (1 clase): [B24-C07 · Ciclo CNO y cadena protón-protón](../programa/clases/B24/B24-C07-ciclo-cno-y-cadena-proton-proton/CLASE.md).

### Ciclo de 18,6 años

- El ciclo de 18,6 años es la regresión del nodo de la órbita lunar sobre la eclíptica, que hace variar su inclinación al ecuador entre `18,3°` y `28,6°`; no se consultó, se menciona como contexto.

💡 **Cómo se explica en la clase [B72-C10](../programa/clases/B72/B72-C10-perturbaciones-lunares/CLASE.md):**
- Como su plano oscila en el ciclo de `18,6 años`, la contribución lunar real varía por encima y por debajo del valor medio simplificado; para gestionar combustible hay que usar la inclinación lunar de cada año.
- Explicar por qué la contribución lunar varía en el ciclo de 18,6 años.
- 🎯 **Por qué importa:** Un satélite geoestacionario sin maniobras de inclinación deriva de su plano ecuatorial algo menos de un grado por año, y el combustible de ese mantenimiento fija su vida útil. La decisión central: ¿cuánto contribuye cada cuerpo a la deriva de la inclinación y cuánto de ese resultado depende de simplificar la órbita lunar?
- 🔗 **Se estudia junto con:** deriva de inclinación, corrección norte-sur, órbita lunar simplificada.

📘 **Dónde se aprende** (1 clase): [B72-C10 · Perturbaciones lunares](../programa/clases/B72/B72-C10-perturbaciones-lunares/CLASE.md).

### Ciclo de actividad

- El ciclo de actividad es la variación de largo plazo de la actividad.

💡 **Cómo se explica en la clase [B24-C12](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md):**
- Los ciclos de actividad, como el solar, se observan en el largo plazo (S1).
- Monitorización de líneas cromosféricas: ciclos de actividad.
- 🎯 **Por qué importa:** La modulación del brillo por manchas permite medir el periodo de rotación de miles de estrellas sin necesitar espectros, pero también contamina la búsqueda de exoplanetas y limita la precisión de las velocidades radiales.
- 🔗 **Se estudia junto con:** mancha, contraste, modulación rotacional, radio angular.

📘 **Dónde se aprende** (1 clase): [B24-C12 · Manchas y actividad estelar](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md).

### Ciclo de Brayton

- El ciclo de Brayton tiene compresión isentrópica, calentamiento isobaro, expansión isentrópica y enfriamiento isobaro.

💡 **Cómo se explica en la clase [B79-C15](../programa/clases/B79/B79-C15-ciclos-termodinamicos-de-propulsion/CLASE.md):**
- Describir las estaciones del ciclo de Brayton.
- La evidencia es la ficha de un ciclo de Brayton del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** B85-C11 trata ciclos térmicos de ensayo, no termodinámicos. Para entender el rendimiento de una turbina de gas hay que ver el ciclo que lo origina.
- 🔗 **Se estudia junto con:** rendimiento ideal, trabajo neto, relación de presiones de trabajo máximo.

📘 **Dónde se aprende** (1 clase): [B79-C15 · Ciclos termodinámicos de propulsión](../programa/clases/B79/B79-C15-ciclos-termodinamicos-de-propulsion/CLASE.md).

### Ciclo de repetición

- La resolución temporal es el intervalo entre observaciones del mismo punto; el ciclo de repetición es el tiempo tras el cual la traza se repite.

💡 **Cómo se explica en la clase [B57-C02](../programa/clases/B57/B57-C02-resolucion-espacial-y-temporal/CLASE.md):**
- C["ciclo de repeticion"] --> I["imagenes por anio"]
- Traducir un ciclo de repetición en imágenes por año y punto, y reconocer el límite de las nubes.
- ⚠️ **Error frecuente:** Tomar el ciclo de repetición como imágenes útiles. Las nubes reducen los datos válidos (8.4).
- 🎯 **Por qué importa:** Un satélite con píxeles de 30 m no ve una casa y uno que vuelve cada 16 días no ve una tormenta. La decisión central: ¿qué tamaño de píxel, qué ancho de barrido y qué ciclo de repetición necesita el fenómeno que quiero estudiar?
- 🔗 **Se estudia junto con:** GSD, IFOV, barrido, resolución temporal.

📘 **Dónde se aprende** (1 clase): [B57-C02 · Resolución espacial y temporal](../programa/clases/B57/B57-C02-resolucion-espacial-y-temporal/CLASE.md).

### Ciclo de Saros

- El ciclo metónico son 235 meses sinódicos (≈ 19 años); el calípico son cuatro metónicos menos un día; el ciclo de Saros son 223 meses sinódicos.

💡 **Cómo se explica en la clase [B132-C01](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md):**
- Sus inscripciones citan periodos como el 223 del ciclo de Saros y una espiral dividida en 235 secciones (ciclo metónico).
- 🎯 **Por qué importa:** Un relato histórico es tan fiable como las fuentes que lo sostienen, y tres copias de una misma fuente no son tres fuentes. La decisión central: ¿cuánto apoyo da realmente un conjunto de fuentes a una afirmación y cuánto de ese apoyo es robusto ante cambios razonables de criterio?
- 🔗 **Se estudia junto con:** crítica de fuentes, fuente primaria, secundaria, terciaria.

📘 **Dónde se aprende** (1 clase): [B132-C01 · Crítica histórica de fuentes y método historiográfico](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md).

### Ciclo de trabajo

- El ciclo de trabajo es la fracción de muestras válidas.
- El ciclo de trabajo es la fracción de la órbita en que se adquiere.
- El ciclo de trabajo es la fracción del tiempo que el propulsor empuja de forma útil.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B37-C13](../programa/clases/B37/B37-C13-series-fotometricas-de-kepler-tess-y-plato-para-asterosismologia/CLASE.md):**
- Con ciclo de trabajo `0,900` y `σ(A) = 1,76 ppm`:
- Ejercicio 6. Ciclo de trabajo de un hueco de 1 d en 10 d.
- 🎯 **Por qué importa:** El análisis sísmico depende de cómo se prepara la serie. La decisión central: ¿qué hace el muestreo, los huecos y el filtro con las frecuencias y amplitudes recuperadas?
- 🔗 **Se estudia junto con:** cadencia, frecuencia de Nyquist, alias, filtro pasa-altos.

📘 **Dónde se aprende** (5 clases): [B37-C13 · Series fotométricas de Kepler, TESS y PLATO para asterosismología](../programa/clases/B37/B37-C13-series-fotometricas-de-kepler-tess-y-plato-para-asterosismologia/CLASE.md); [B57-C24 · Diseño de una carga útil de observación terrestre](../programa/clases/B57/B57-C24-diseno-de-una-carga-util-de-observacion-terrestre/CLASE.md); [B78-C22 · Ciclos de trabajo y operación de propulsión eléctrica](../programa/clases/B78/B78-C22-ciclos-de-trabajo-y-operacion-de-propulsion-electrica/CLASE.md); [B85-C08 · Calentadores y termostatos](../programa/clases/B85/B85-C08-calentadores-y-termostatos/CLASE.md); [B86-C08 · Convertidores DC-DC](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md).

### Ciclo húmedo–seco

- Un ciclo húmedo–seco alterna agua y secado, favoreciendo la unión por pérdida de agua.

💡 **Cómo se explica en la clase [B56-C21](../programa/clases/B56/B56-C21-polimerizacion-prebiotica-experimental-oligomeros-y-condiciones-de-laboratorio/CLASE.md):**
- (2026, *Scientific Reports*) informa de la síntesis abiótica de polímeros resistentes a la ARNasa a partir de AMP y UMP no activados y de ribosa-5'-fosfato bajo ciclos húmedo–seco simulados;
- Definir monómero, oligómero, extensión de reacción y ciclo húmedo–seco.
- 🎯 **Por qué importa:** C03 trata el origen de autorreplicantes, pero ninguna clase trata la polimerización experimental y sus límites. Antes de que un replicador pueda copiarse, hay que formar cadenas lo bastante largas.
- 🔗 **Se estudia junto con:** monómero, oligómero, extensión de reacción, distribución de Flory.

📘 **Dónde se aprende** (1 clase): [B56-C21 · Polimerización prebiótica experimental: oligómeros y condiciones de laboratorio](../programa/clases/B56/B56-C21-polimerizacion-prebiotica-experimental-oligomeros-y-condiciones-de-laboratorio/CLASE.md).

### Ciclo límite

- El ciclo límite es la oscilación permanente entre las paredes de la banda.

💡 **Cómo se explica en la clase [B87-C13](../programa/clases/B87/B87-C13-propulsores-de-control-de-actitud/CLASE.md):**
- Un ciclo límite sin perturbaciones gasta propergol continuamente; en la práctica se amplía la banda muerta o se usan ruedas y se reserva el propulsor para maniobras y descargas.
- D --> C["ciclo limite en la banda muerta"]
- 🎯 **Por qué importa:** Los propulsores son el actuador de más par y de respuesta rápida, y el único que cambia el momento total del satélite, pero cada pulso gasta masa que no vuelve. La decisión central: ¿cuánto propergol cuesta una maniobra o un año de mantenimiento de actitud, y qué precisión permite el impulso mínimo?
- 🔗 **Se estudia junto con:** par, impulso mínimo, banda muerta, impulso específico.

📘 **Dónde se aprende** (1 clase): [B87-C13 · Propulsores de control de actitud](../programa/clases/B87/B87-C13-propulsores-de-control-de-actitud/CLASE.md).

### Ciclo menor

- El ciclo menor es el `mcd` de los períodos y el mayor el `mcm`.

💡 **Cómo se explica en la clase [B88-C23](../programa/clases/B88/B88-C23-arquitectura-de-software-de-vuelo-capas-y-ejecutivo/CLASE.md):**
- El ejecutivo tiene ciclo menor de 100 ms, mayor de 400 ms y 4 tramas con cargas de 62, 12, 37 y 12 ms.
- El script [capas_software.py](capas_software.py) verifica dependencias, ciclos y niveles de 9 módulos y calcula las tramas de un ejecutivo cíclico, y comprueba una violación única, ausencia de ciclo tras corregir y carga ≤ ciclo menor.
- 🎯 **Por qué importa:** Las dependencias hacia arriba y los ciclos hacen imposible probar un módulo por separado y convierten un cambio en riesgo global. La decisión central: ¿qué módulo depende de quién, y puede ordenarse el sistema en capas sin ciclos?
- 🔗 **Se estudia junto con:** capa, dependencia hacia arriba, nivel topológico, mayor.

📘 **Dónde se aprende** (1 clase): [B88-C23 · Arquitectura de software de vuelo: capas y ejecutivo](../programa/clases/B88/B88-C23-arquitectura-de-software-de-vuelo-capas-y-ejecutivo/CLASE.md).

### Ciclo metónico

- El ciclo metónico es la casi coincidencia entre 19 años trópicos y 235 meses sinódicos, que sirvió de base a calendarios lunisolares de la Antigüedad (la fuente que consultamos lo menciona en el mecanismo de Anticitera, S4).
- El ciclo metónico son 235 meses sinódicos (≈ 19 años); el calípico son cuatro metónicos menos un día; el ciclo de Saros son 223 meses sinódicos.

💡 **Cómo se explica en la clase [B02-C01](../programa/clases/B02/B02-C01-calendarios-astronomicos-en-civilizaciones-antiguas/CLASE.md):**
- Los autores del estudio sobre el mecanismo de Anticitera describen un dial de calendario metónico en ese aparato (S4); es un indicio de que el ciclo se conocía y se usaba, no una descripción general de todos los calendarios griegos.
- Verificar que 19 años trópicos y 235 meses sinódicos casi coinciden (ciclo metónico).
- 🎯 **Por qué importa:** Un calendario es una promesa: «dentro de tantos días ocurrirá tal cosa en el cielo o en la tierra». Esa promesa solo se cumple si el calendario sigue algún ciclo natural.
- 🔗 **Se estudia junto con:** calendario, año trópico, mes sinódico, deriva.

📘 **Dónde se aprende** (2 clases): [B02-C01 · Calendarios astronómicos en civilizaciones antiguas](../programa/clases/B02/B02-C01-calendarios-astronomicos-en-civilizaciones-antiguas/CLASE.md); [B132-C01 · Crítica histórica de fuentes y método historiográfico](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md).

### Ciclo mover y esperar

- El ciclo mover y esperar es: ejecutar, enviar telemetría, decidir y enviar la orden.

💡 **Cómo se explica en la clase [B97-C07](../programa/clases/B97/B97-C07-teleoperacion-con-latencia/CLASE.md):**
- Calcular el tiempo de una tarea con el ciclo mover y esperar.
- 🎯 **Por qué importa:** Con un retardo de unos segundos se puede teleoperar casi en vivo; con minutos, no. La diferencia se traduce en horas o días de tarea y en la necesidad de dar autonomía al robot.
- 🔗 **Se estudia junto con:** retardo de ida, autonomía supervisada, avance ciego.

📘 **Dónde se aprende** (1 clase): [B97-C07 · Teleoperación con latencia](../programa/clases/B97/B97-C07-teleoperacion-con-latencia/CLASE.md).

### Ciclo por día

- Un ciclo por día (c/d) es una unidad de frecuencia: 1 c/d = 11,574 µHz.

💡 **Cómo se explica en la clase [B15-C02](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md):**
- El número `f Δt = f/f_s` es la frecuencia en ciclos por muestra.
- Eso fija dos frecuencias de Nyquist muy distintas: 360 ciclos por día para 2 min y 24 ciclos por día para 30 min.
- 🎯 **Por qué importa:** Un detector que mide una estrella cada 2 minutos no puede ver directamente algo que oscila cada 3 minutos con precisión, pero tampoco lo ignora: ese movimiento rápido queda registrado como una oscilación lenta y falsa. Si no sabes que eso ocurre, publicarías un periodo que no existe.
- 🔗 **Se estudia junto con:** muestreo, frecuencia de muestreo, frecuencia de Nyquist, aliasing.

📘 **Dónde se aprende** (1 clase): [B15-C02 · Muestreo y aliasing](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md).

### Ciclo sísmico

- El ciclo sísmico alterna acumulación lenta de deformación y liberación brusca.

💡 **Contexto en la clase [B57-C20](../programa/clases/B57/B57-C20-caso-de-estudio-climatico-o-geologico-de-chile/CLASE.md):**
- **Idea central (modelo mental):** La zona de subducción acumula deslizamiento como una bañera que se llena despacio y se vacía de golpe. Sabes cuánto cabe (D) y a qué ritmo se llena, pero no cuándo alguien tira el tapón.
- 🎯 **Por qué importa:** Chile vive sobre una zona de subducción activa y las instituciones deben comprender cuánta deformación se acumula y se libera. La decisión central: ¿qué puede decir una cuenta de balance de deslizamiento y qué no puede decir sobre cuándo ocurrirá el próximo terremoto?
- 🔗 **Se estudia junto con:** déficit de deslizamiento, velocidad de convergencia, acoplamiento, tiempo de reposición.

📘 **Dónde se aprende** (1 clase): [B57-C20 · Caso de estudio climático o geológico de Chile](../programa/clases/B57/B57-C20-caso-de-estudio-climatico-o-geologico-de-chile/CLASE.md).

### Ciclo térmico

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C02](../programa/clases/B47/B47-C02-requisitos-de-instrumentos-orbitales/CLASE.md):**
- Casi 5440 ciclos térmicos al año fatigan estructura y pegamentos.
- Obtener la fracción de eclipse y los ciclos térmicos anuales.
- 🎯 **Por qué importa:** Un instrumento sin requisitos cuantificados no se puede diseñar ni verificar. La decisión central: ¿qué cifras de apertura, órbita, datos y masa se derivan de lo que se quiere medir?
- 🔗 **Se estudia junto con:** requisito, órbita circular, período, eclipse.

📘 **Dónde se aprende** (1 clase): [B47-C02 · Requisitos de instrumentos orbitales](../programa/clases/B47/B47-C02-requisitos-de-instrumentos-orbitales/CLASE.md).

### Ciclo V

- Un ciclo V baja de la malla fina a la más gruesa y vuelve a subir.

💡 **Cómo se explica en la clase [B21-C03](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md):**
- Corrección gruesa: resolver `A e = r` en la malla gruesa; para eso se aplica el mismo ciclo, recursivamente, hasta una malla con un solo punto, donde la ecuación se resuelve a mano.
- Cada malla gruesa tiene la cuarta parte de puntos, así que el costo total de un ciclo es una constante por el de la malla fina.
- 🎯 **Por qué importa:** El potencial gravitatorio de una nube de gas, el potencial electrostático alrededor de una nave que se carga en el plasma y la presión en un fluido incompresible obedecen la misma ecuación: la de Poisson. Los códigos de simulación astrofísica la resuelven en cada paso de tiempo;
- 🔗 **Se estudia junto con:** ecuación de Poisson, elíptico, de Dirichlet, estencil de cinco puntos.

📘 **Dónde se aprende** (1 clase): [B21-C03 · Ecuación de Poisson: relajación y multigrid](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md).

### Ciclos por kg de reposición

- Los ciclos por kg de reposición son `1/(1 − ρ)`.

💡 **Cómo se explica en la clase [B59-C15](../programa/clases/B59/B59-C15-ciclo-cerrado-de-materiales/CLASE.md):**
- Ejercicio 3 · casi autónomo. Ciclos por kg de reposición (8.4).
- Ejercicio 12 · integrador. Elabora tu *ficha del ciclo cerrado*: recuperación global, reposición de régimen y de arranque, serie geométrica, mejora por etapa y fugas.
- 🎯 **Por qué importa:** Cerrar el 87 % de un lazo no deja una reposición del 13 % sino una dependencia permanente del 13 %. La decisión central: ¿qué etapa del lazo conviene mejorar para reducir más la reposición?
- 🔗 **Se estudia junto con:** recuperación global, reposición, arranque en frío, retardo.

📘 **Dónde se aprende** (1 clase): [B59-C15 · Ciclo cerrado de materiales](../programa/clases/B59/B59-C15-ciclo-cerrado-de-materiales/CLASE.md).

### Ciclotrón

- El ciclotrón gira a `f = eB/(2πγm)`.

💡 **Cómo se explica en la clase [B31-C15](../programa/clases/B31/B31-C15-fisica-de-aceleradores/CLASE.md):**
- Calcular la frecuencia del ciclotrón relativista.
- Ejercicio 12. Integrador. Elabora tu *ficha de un acelerador*: rigidez, pérdidas, ciclotrón y `√s`.
- 🎯 **Por qué importa:** El diseño de un acelerador depende de cuánta energía se pierde por radiación y de cuánta energía útil se obtiene. La decisión central: ¿qué campo y qué radio se necesitan y por qué los electrones pierden tanto?
- 🔗 **Se estudia junto con:** rigidez magnética, pérdida por vuelta, colisionador, blanco fijo.

📘 **Dónde se aprende** (1 clase): [B31-C15 · Física de aceleradores](../programa/clases/B31/B31-C15-fisica-de-aceleradores/CLASE.md).

### Cielo

- El cielo es un parámetro más.
- El cielo (`B`) y la oscuridad (`D`) añaden fondo.

💡 **Cómo se explica en la clase [B44-C11](../programa/clases/B44/B44-C11-tiempo-de-exposicion/CLASE.md):**
- Con una fuente de `20 e⁻/s`, cielo de `2 e⁻/s/pix`, oscuridad de `0,1 e⁻/s/pix`, lectura de `6 e⁻` y `20` píxeles, un cuadro de `100 s` tiene SNR `24,042`;
- Calcular la SNR de un cuadro con fuente, cielo, oscuridad y lectura.
- 🎯 **Por qué importa:** Exponer poco multiplica el ruido de lectura; exponer mucho arriesga la saturación. La decisión central: ¿cuánto debe durar cada cuadro dentro de un tiempo total dado?
- 🔗 **Se estudia junto con:** SNR, oscuridad, exposición limitada por el cielo, serie de cuadros.

📘 **Dónde se aprende** (2 clases): [B44-C11 · Tiempo de exposición](../programa/clases/B44/B44-C11-tiempo-de-exposicion/CLASE.md); [B45-C24 · Fotometría por ajuste de PSF](../programa/clases/B45/B45-C24-fotometria-por-ajuste-de-psf/CLASE.md).

### Cielo completo

- El cielo completo supone exposición uniforme.

💡 **Cómo se explica en la clase [B28-C04](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md):**
- La significancia típica es `d/σ = 6,5` con cielo completo.
- Reconocer los supuestos de cielo completo.
- 🎯 **Por qué importa:** El origen de los rayos cósmicos de mayor energía sigue abierto; el criterio de Hillas descarta fuentes y la anisotropía apunta a regiones. La decisión central: ¿qué fuentes pueden alcanzar una energía dada y qué anisotropía se puede detectar con un número dado de eventos?
- 🔗 **Se estudia junto con:** criterio de Hillas, rodilla, flujo integral, dipolo.

📘 **Dónde se aprende** (1 clase): [B28-C04 · Rayos cósmicos de alta energía](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md).

### Cielo oscuro

- Un cielo oscuro es un cielo con poca luz artificial.

💡 **Cómo se explica en la clase [B02-C20](../programa/clases/B02/B02-C20-patrimonio-astronomico-y-etica-cultural/CLASE.md):**
- Según S3, el estudio temático de 2017 concluye que los lugares de cielo oscuro no pueden ser por sí mismos una categoría de Patrimonio Mundial, aunque la calidad del cielo oscuro puede reforzar el valor cultural o natural de un sitio; las Reservas Starlight y los Parques de Cielo Oscuro tampoco son categorías de Patrimonio Mundial.
- Ejercicio 3 · casi autónomo. ¿Qué dice S3 sobre los cielos oscuros como categoría?
- ⚠️ **Error frecuente:** Pensar que el cielo oscuro es solo asunto científico. Ejercicio 7.
- 🎯 **Por qué importa:** Los sitios, instrumentos, archivos, saberes y hasta la oscuridad del cielo son patrimonio, y los telescopios, el turismo y las constelaciones de satélites pueden dañarlo. La pregunta motivadora es: ¿qué debo preguntar, a quién y antes de qué, cuando mi trabajo toca un cielo o un lugar que importa a otras personas?
- 🔗 **Se estudia junto con:** patrimonio astronómico, conocimiento tradicional, consentimiento libre, previo e informado, UNDRIP.

📘 **Dónde se aprende** (1 clase): [B02-C20 · Patrimonio astronómico y ética cultural](../programa/clases/B02/B02-C20-patrimonio-astronomico-y-etica-cultural/CLASE.md).

### Cielos oscuros

- Un interferómetro combina varias antenas para actuar como una más grande (ALMA). Cielos oscuros son cielos con poca luz artificial.

💡 **Cómo se explica en la clase [B02-C18](../programa/clases/B02/B02-C18-expansion-de-la-astronomia-en-chile/CLASE.md):**
- C --> D["Preguntas actuales:<br/>territorio, comunidades,<br/>cielos oscuros"]
- *Descripción textual:* tres etapas encadenadas: una expedición que da origen a un observatorio nacional (1849–1853), la búsqueda de sitios y llegada de observatorios internacionales (1958–1974) y la expansión posterior con Paranal, Las Campanas y ALMA; todas conducen a preguntas actuales sobre territorio, comunidades y cielos oscuros.
- 🎯 **Por qué importa:** Chile alberga observatorios de primer nivel porque combina cielos oscuros, aire seco y altitud. Pero un observatorio también es una historia de decisiones, instituciones y territorios.
- 🔗 **Se estudia junto con:** paralaje solar, observatorio nacional, observatorio internacional, sitio astronómico.

📘 **Dónde se aprende** (1 clase): [B02-C18 · Expansión de la astronomía en Chile](../programa/clases/B02/B02-C18-expansion-de-la-astronomia-en-chile/CLASE.md).

### Cierra

- Un diseño cierra cuando todos los presupuestos son coherentes y cumplen sus márgenes.

💡 **Cómo se explica en la clase [B83-C20](../programa/clases/B83/B83-C20-diseno-preliminar-completo-de-mision/CLASE.md):**
- Límite: en un velero el lazo se corta con la experiencia; aquí se cierra con una iteración y un modelo.
- El margen de datos de C11 es 43,38 %: el diseño cierra en masa y datos.
- ⚠️ **Error frecuente:** Resolver cada presupuesto por separado. Cierra el lazo completo
- 🎯 **Por qué importa:** Cada presupuesto aislado puede cerrar y el conjunto no. La decisión central: ¿existe una masa seca que sea coherente con la potencia, las baterías, la estructura y el propelente que ella misma exige, y cabe en el límite?
- 🔗 **Se estudia junto con:** diseño preliminar, lazo de diseño, iteración de punto fijo, bisección.

📘 **Dónde se aprende** (1 clase): [B83-C20 · Diseño preliminar completo de misión](../programa/clases/B83/B83-C20-diseno-preliminar-completo-de-mision/CLASE.md).

### Cierre

- El cierre del balance es que la masa que entra iguale la que sale.
- Arquitectura: combinación de subsistemas. Cierre: fracción reciclada.

💡 **Cómo se explica en la clase [B59-C16](../programa/clases/B59/B59-C16-desechos-y-reciclaje/CLASE.md):**
- Balance de masa y de carbono verifican el cierre de forma independiente.
- Verificar el cierre de masa y de carbono.
- 🎯 **Por qué importa:** Los residuos son una fuente de agua y de dióxido de carbono, pero también consumen oxígeno. La decisión central: ¿cuánto oxígeno cuesta cerrar el residuo y cuánta agua se recupera?
- 🔗 **Se estudia junto con:** oxidación completa, residuo seco, humedad, inerte.

📘 **Dónde se aprende** (2 clases): [B59-C16 · Desechos y reciclaje](../programa/clases/B59/B59-C16-desechos-y-reciclaje/CLASE.md); [B106-C09 · Sistemas ECLSS](../programa/clases/B106/B106-C09-sistemas-eclss/CLASE.md).

### Cierre de bucle

- Un cierre de bucle es la restricción entre dos poses que representan el mismo lugar.
- Cierre de bucle: restricción entre dos poses del mismo lugar (F4, F7).

💡 **Cómo se explica en la clase [B97-C05](../programa/clases/B97/B97-C05-localizacion-y-mapeo-slam/CLASE.md):**
- La odometría pura termina a `0,856` m del punto de partida; con el cierre de bucle (σ = `0,02 m`) queda a `0,003` m.
- Descripción larga: el cierre de bucle reduce el error de cierre en un factor de 251,0 y el RMS de la trayectoria en 2,95.
- 🎯 **Por qué importa:** Sin una corrección, el error de la odometría crece con el recorrido y el mapa se deforma. El cierre de bucle reparte ese error por toda la trayectoria; entender cuánto y cómo evita fiarse de un mapa que se «cierra» solo en apariencia.
- 🔗 **Se estudia junto con:** deriva, grafo de poses, solución de mínimos cuadrados.

📘 **Dónde se aprende** (2 clases): [B97-C05 · Localización y mapeo SLAM](../programa/clases/B97/B97-C05-localizacion-y-mapeo-slam/CLASE.md); [B99-C04 · Cierre de bucles y consistencia global](../programa/clases/B99/B99-C04-cierre-de-bucles-y-consistencia-global/CLASE.md).

### Cierre de energía

- El cierre de energía verifica que lo que entra, sale o se almacena suma cero.

💡 **Cómo se explica en la clase [B85-C08](../programa/clases/B85/B85-C08-calentadores-y-termostatos/CLASE.md):**
- Comprobar el cierre de energía de la simulación.
- Ejercicio 3 · casi autónomo. ¿Por qué el cierre de energía es ~0?
- ⚠️ **Error frecuente:** Tomar el cierre de energía como validación física. valida el código (8.3)
- 🎯 **Por qué importa:** Un calentador pequeño no sostiene la temperatura y uno grande gasta energía que una batería no tiene. La decisión central: ¿cuánta potencia de calentador mantiene la temperatura mínima en el peor eclipse y cuánta energía cuesta por órbita?
- 🔗 **Se estudia junto con:** calentador resistivo, termostato, histéresis, ciclo de trabajo.

📘 **Dónde se aprende** (1 clase): [B85-C08 · Calentadores y termostatos](../programa/clases/B85/B85-C08-calentadores-y-termostatos/CLASE.md).

### Cierre de fase

- El cierre de fase `φ₁₂ + φ₂₃ − φ₁₃` debe ser cero (mod 2π) si el triplete es consistente.

💡 **Cómo se explica en la clase [B69-C07](../programa/clases/B69/B69-C07-evaluacion-de-la-calidad-de-un-interferograma/CLASE.md):**
- T["φ12 + φ23 − φ13"] --> CL["cierre de fase"]
- *Descripción textual:* la cota de fase, los residuos y el cierre alimentan una decisión de aceptar, enmascarar o descartar el interferograma.
- 🎯 **Por qué importa:** Un interferograma bonito puede ser incorrecto. La decisión central: ¿qué números justifican aceptar, enmascarar o descartar un interferograma?
- 🔗 **Se estudia junto con:** desviación de fase, residuo, máscara.

📘 **Dónde se aprende** (1 clase): [B69-C07 · Evaluación de la calidad de un interferograma](../programa/clases/B69/B69-C07-evaluacion-de-la-calidad-de-un-interferograma/CLASE.md).

### Cierre de lazo

- El cierre de lazo es la fracción de un consumible que se recupera.

💡 **Contexto en la clase [B104-C02](../programa/clases/B104/B104-C02-requisitos-de-tripulacion/CLASE.md):**
- 🎯 **Por qué importa:** «La tripulación tendrá agua suficiente» no se puede comprobar; «4 personas, 30 días, 2,5 kg por persona y día más un 10 % de margen» sí. La decisión central: ¿cuánto hay que llevar, y a partir de cuántos días compensa un equipo que recicla?
- 🔗 **Se estudia junto con:** requisito, verificación, trazabilidad, margen.

📘 **Dónde se aprende** (1 clase): [B104-C02 · Requisitos de tripulación](../programa/clases/B104/B104-C02-requisitos-de-tripulacion/CLASE.md).

### Cierre del balance

- El cierre del balance es que el residuo sea cero.

💡 **Cómo se explica en la clase [B86-C20](../programa/clases/B86/B86-C20-simulacion-de-ciclo-energetico-orbital/CLASE.md):**
- *Descripción textual:* `β` fija el eclipse y el coseno del ala; con la degradación da la generación; en cada paso el balance con las cargas determina la batería, la energía descartada y las pérdidas; de ahí salen el SOC mínimo y el cierre del balance.
- El cierre del balance prueba el código, no que el diseño cumpla; hay que mirar el SOC mínimo y los márgenes.
- 🎯 **Por qué importa:** Los cálculos por órbita aislada no ven que `β` cambia día a día ni que la degradación se acumula. Una simulación larga revela el peor día y comprueba que la energía se conserva en todo el recorrido.
- 🔗 **Se estudia junto con:** simulación acoplada, paso de tiempo, generación descartada, SOC mínimo.

📘 **Dónde se aprende** (1 clase): [B86-C20 · Simulación de ciclo energético orbital](../programa/clases/B86/B86-C20-simulacion-de-ciclo-energetico-orbital/CLASE.md).

### Cierre del ciclo

- El cierre del ciclo es que la energía recuperada iguale a la gastada.

💡 **Cómo se explica en la clase [B86-C13](../programa/clases/B86/B86-C13-energia-durante-eclipse/CLASE.md):**
- La evidencia es la verificación de cierre del ciclo energético del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *verificación de cierre del ciclo energético*: energías, tiempos de recarga, régimen periódico, déficit, generación mínima y rótulos.
- 🎯 **Por qué importa:** Una batería que cubre bien un eclipse puede fallar tras cien porque cada órbita pierde un poco más de lo que recupera. El cierre del ciclo es la prueba de que el diseño es sostenible.
- 🔗 **Se estudia junto con:** déficit por órbita, potencia máxima de carga, régimen periódico, generación mínima.

📘 **Dónde se aprende** (1 clase): [B86-C13 · Energía durante eclipse](../programa/clases/B86/B86-C13-energia-durante-eclipse/CLASE.md).

### Cierre del lazo

- Cociente respiratorio: CO₂ por O₂ (0,85). Cierre del lazo: fracción recuperada.

💡 **Contexto en la clase [B106-C05](../programa/clases/B106/B106-C05-suministro-y-generacion-de-oxigeno/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR A["agua"] -->|"electrolisis"| B["O2 a la cabina"] A --> C["H2"] C -->|"Sabatier"| D["agua + CH4"] E["CO2 de la tripulacion"] --> D D --> A ``` *Descripción textual:* la electrólisis da O₂ y H₂ desde el agua; el H₂ reacciona con el CO₂ exhalado y devuelve agua y metano.
- 🎯 **Por qué importa:** Llevar oxígeno comprimido o líquido pesa; electrolizar agua exige energía y reponer agua. La decisión central: ¿cuánta agua, hidrógeno y energía implica producir el oxígeno de una tripulación y qué parte del agua devuelve la reacción de Sabatier?
- 🔗 **Se estudia junto con:** Electrólisis, Sabatier, Entalpía, energía libre.

📘 **Dónde se aprende** (1 clase): [B106-C05 · Suministro y generación de oxígeno](../programa/clases/B106/B106-C05-suministro-y-generacion-de-oxigeno/CLASE.md).

### Cierre independiente

- El cierre independiente: los demás se obtienen de estos.

💡 **Contexto en la clase [B51-C02](../programa/clases/B51/B51-C02-cantidades-de-cierre-fase-y-amplitud-de-cierre/CLASE.md):**
- **Idea central (modelo mental):** Como recorrer un triángulo de calles: no importa en qué esquina empieces ni cuánto se haya movido cada farola (la ganancia), la suma de las vueltas al recorrerlo es la misma.
- 🎯 **Por qué importa:** Cuando las ganancias no se pueden calibrar (VLBI con atmósfera rápida, autocalibración), los cierres son los observables robustos. La decisión central: ¿qué información sobrevive a los errores por antena y cuánta se pierde?
- 🔗 **Se estudia junto con:** fase de cierre, amplitud de cierre, ganancia compleja, modelo de cielo.

📘 **Dónde se aprende** (1 clase): [B51-C02 · Cantidades de cierre: fase y amplitud de cierre](../programa/clases/B51/B51-C02-cantidades-de-cierre-fase-y-amplitud-de-cierre/CLASE.md).

### Cifra de ruido

- La cifra de ruido `NF = 10 log₁₀(1 + T/T₀)` con `T₀ = 290 K`.

💡 **Contexto en la clase [B49-C06](../programa/clases/B49/B49-C06-amplificadores-de-bajo-ruido-lna-tecnologia-ganancia-y-adaptacion/CLASE.md):**
- **Idea central (modelo mental):** Como una cañería con fugas: una fuga al principio pierde más caudal útil que una al final, donde ya hay mucha presión.
- 🎯 **Por qué importa:** Una décima de decibelio antes del primer amplificador cuesta más que mejorar el mezclador. La decisión central: ¿qué bloque domina la temperatura de ruido y qué pérdidas deben evitarse antes de él?
- 🔗 **Se estudia junto con:** temperatura de ruido, fórmula de Friis, ganancia disponible, factor Y.

📘 **Dónde se aprende** (1 clase): [B49-C06 · Amplificadores de bajo ruido (LNA): tecnología, ganancia y adaptación](../programa/clases/B49/B49-C06-amplificadores-de-bajo-ruido-lna-tecnologia-ganancia-y-adaptacion/CLASE.md).

### Cifra derivada

- La cifra derivada se calcula aquí.

💡 **Cómo se explica en la clase [B28-C20](../programa/clases/B28/B28-C20-caso-de-estudio-de-evento-combinado/CLASE.md):**
- PUB --> DER["cifras derivadas (C05, C07, C13)"]
- *Descripción textual:* los resúmenes dan cifras publicadas; se comprueba su coherencia y se calculan magnitudes derivadas; el dossier incluye la lista de lo no consultado y se firma con una huella.
- 🎯 **Por qué importa:** Un caso de estudio sirve si es verificable: cada cifra debe llevar su fuente, y lo calculado debe distinguirse de lo publicado. La decisión central: ¿qué cifras del evento están respaldadas por lo consultado, cuáles se derivan y cuáles quedan fuera?
- 🔗 **Se estudia junto con:** dossier, cifra publicada, coherencia, cifra excluida.

📘 **Dónde se aprende** (1 clase): [B28-C20 · Caso de estudio de evento combinado](../programa/clases/B28/B28-C20-caso-de-estudio-de-evento-combinado/CLASE.md).

### Cifra excluida

- La cifra excluida no se consultó.

💡 **Cómo se explica en la clase [B28-C20](../programa/clases/B28/B28-C20-caso-de-estudio-de-evento-combinado/CLASE.md):**
- Descripción larga: la mitad de las filas del dossier son cifras publicadas y la otra mitad, cálculos propios; las excluidas se listan aparte.
- huella SHA-256 del dossier: 032988a045c269cc... ; cifras no consultadas y excluidas: corrimiento al rojo, curva de luz de la kilonova, constante de Hubble
- 🎯 **Por qué importa:** Un caso de estudio sirve si es verificable: cada cifra debe llevar su fuente, y lo calculado debe distinguirse de lo publicado. La decisión central: ¿qué cifras del evento están respaldadas por lo consultado, cuáles se derivan y cuáles quedan fuera?
- 🔗 **Se estudia junto con:** dossier, cifra publicada, cifra derivada, coherencia.

📘 **Dónde se aprende** (1 clase): [B28-C20 · Caso de estudio de evento combinado](../programa/clases/B28/B28-C20-caso-de-estudio-de-evento-combinado/CLASE.md).

### Cifra publicada

- La cifra publicada viene de una fuente consultada.

💡 **Cómo se explica en la clase [B28-C20](../programa/clases/B28/B28-C20-caso-de-estudio-de-evento-combinado/CLASE.md):**
- S["resúmenes consultados"] --> PUB["cifras publicadas"]
- *Descripción textual:* los resúmenes dan cifras publicadas; se comprueba su coherencia y se calculan magnitudes derivadas; el dossier incluye la lista de lo no consultado y se firma con una huella.
- 🎯 **Por qué importa:** Un caso de estudio sirve si es verificable: cada cifra debe llevar su fuente, y lo calculado debe distinguirse de lo publicado. La decisión central: ¿qué cifras del evento están respaldadas por lo consultado, cuáles se derivan y cuáles quedan fuera?
- 🔗 **Se estudia junto con:** dossier, cifra derivada, coherencia, cifra excluida.

📘 **Dónde se aprende** (1 clase): [B28-C20 · Caso de estudio de evento combinado](../programa/clases/B28/B28-C20-caso-de-estudio-de-evento-combinado/CLASE.md).

### Cifra significativa

- Una cifra significativa es un dígito que aporta información sobre el valor; cuentan todos los dígitos desde el primero distinto de cero hasta el último que se ha medido o calculado con sentido (`0,00450` tiene 3).
- Una cifra significativa es un dígito con información.

💡 **Cómo se explica en la clase [B03-C11](../programa/clases/B03/B03-C11-estimacion-y-redondeo-responsable/CLASE.md):**
- La guía de metrología sugiere reportar la incertidumbre con a lo sumo dos cifras significativas y redondear el valor para que sea coherente con ella; si `y = 10,057 62 Ω` con `u = 27 mΩ`, se escribe `10,058 Ω` (S2, 7.2.6).
- Contar cifras significativas de un número y redondear a `n` cifras.
- 🎯 **Por qué importa:** Si te piden el tiempo que tarda la luz del Sol en llegar a la Tierra y respondes «499,004783836 s», parece muy preciso, pero tus datos (1 au y `c`) son exactos; en cambio, si respondes lo mismo para la distancia a la Luna, que varía entre unos 357 000 y 407 000 km, esas cifras serían falsas.
- 🔗 **Se estudia junto con:** Redondear, estimación, cota, error de redondeo.

📘 **Dónde se aprende** (2 clases): [B03-C11 · Estimación y redondeo responsable](../programa/clases/B03/B03-C11-estimacion-y-redondeo-responsable/CLASE.md); [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md).

### Cifrado autenticado AES en modo Galois/Counter (GCM)

- Su base de interoperabilidad es el cifrado autenticado AES en modo Galois/Counter (GCM) con clave de 256 bits.

💡 **Contexto en la clase [B89-C25](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md):**
- 🎯 **Por qué importa:** Los comandos son la superficie más sensible de una misión; sin autenticación y sin protección contra repetición, una trama capturada podría reutilizarse, y un CRC solo detecta errores, no ataques (C12). La decisión central: ¿cómo garantizar que una trama es auténtica, íntegra y no repetida, y cuánto cuesta en sobrecarga?
- 🔗 **Se estudia junto con:** protocolo de seguridad de enlace de datos (SDLS), asociación de seguridad (SA), SPI, ventana anti-repetición.

📘 **Dónde se aprende** (1 clase): [B89-C25 · Protección criptográfica de enlaces espaciales](../programa/clases/B89/B89-C25-proteccion-criptografica-de-enlaces-espaciales/CLASE.md).

### Cifras significativas

- Las cifras significativas son las que aportan información; el resto sobra.
- Las cifras significativas son las que aporta la medida; la incertidumbre dice dónde cortar.

💡 **Cómo se explica en la clase [B01-C08](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md):**
- Si `d = 43 Mpc` tiene dos cifras significativas, escribe `1,3 × 10²⁴ m`, no `1,3268 × 10²⁴ m`.
- Paso 6 · Cifras. Con dos cifras significativas: `1,3 × 10²⁴ m`, `1,4 × 10⁸ ly`, `8,9 × 10¹² au`.
- 🎯 **Por qué importa:** En 1999 se perdió la sonda Mars Climate Orbiter por una discrepancia entre unidades inglesas y métricas (C04, fuente NASA). La ciencia estaba bien; la conversión, no.
- 🔗 **Se estudia junto con:** Sistema Internacional (SI), unidades base, unidad derivada, unidad no SI aceptada.

📖 **Explicado a fondo:** [Cifras significativas](esencial/cuarta-fundamentos.md#cifras-significativas) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B01-C08 · Mediciones y unidades astronómicas](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md); [B01-C18 · Incertidumbre y errores elementales](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md).

### Cilindro

- Un cilindro de radio `r` y altura `h` tiene volumen `πr²h`.

💡 **Cómo se explica en la clase [B03-C17](../programa/clases/B03/B03-C17-areas-y-volumenes-elementales/CLASE.md):**
- Un cilindro de radio `r` y altura `h` tiene volumen `πr²h`: el área de la base por la altura.
- Calcular el volumen de un cilindro y de un elipsoide achatado.
- 🎯 **Por qué importa:** La NASA publica que la densidad media del Sol es 1408 kg/m³ (S1), cerca de una vez y media la del agua. ¿Cómo se obtiene?
- 🔗 **Se estudia junto con:** perímetro, área, esfera, área superficial.

📘 **Dónde se aprende** (1 clase): [B03-C17 · Áreas y volúmenes elementales](../programa/clases/B03/B03-C17-areas-y-volumenes-elementales/CLASE.md).

### Cinemática

- La cinemática es `q̇ = ½ q ⊗ [0, ω]`, con `ω` la velocidad angular del cuerpo en su propio sistema.
- La cinemática `E_R = (μ² v²/m_N)(1 − cosθ)`.

💡 **Cómo se explica en la clase [B16-C20](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md):**
- La cinemática `q̇ = ½ q ⊗ [0, ω]` conserva la norma de `q` de forma exacta en tiempo continuo; la dinámica es `J ω̇ = −ω × (J ω) + u`.
- D --> F["cuerpo rígido<br/>Euler + cinemática"]
- 🎯 **Por qué importa:** Un telescopio debe girar desde una orientación a otra y quedarse allí. Con tres ejes acoplados y rotaciones grandes, ni los ángulos de Euler (tienen singularidades y dependen de la secuencia de giros) ni el modelo lineal bastan.
- 🔗 **Se estudia junto con:** cuaternión unitario, producto de cuaterniones, cuaternión de error, dinámica.

📘 **Dónde se aprende** (2 clases): [B16-C20 · Control de orientación en un simulador](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md); [B36-C10 · Búsqueda directa de materia oscura en laboratorio](../programa/clases/B36/B36-C10-busqueda-directa-de-materia-oscura-en-laboratorio/CLASE.md).

### Cinemática directa

- La cinemática directa calcula la posición de la punta a partir de los ángulos.
- Parámetros D-H: `a` (longitud), `α` (torsión), `d` (desplazamiento) y `θ` (ángulo articular). Cinemática directa: de los ángulos al extremo.

💡 **Cómo se explica en la clase [B97-C02](../programa/clases/B97/B97-C02-cinematica-de-manipuladores/CLASE.md):**
- Al aplicar la cinemática directa a ambas se recupera el objetivo con error `1,78e-15` m.
- *Descripción textual:* los ángulos dan la posición por cinemática directa y se recuperan por la inversa; el jacobiano relaciona velocidades y su determinante anuncia las singularidades.
- 🎯 **Por qué importa:** Cada vez que un brazo coge una carga o una herramienta alguien resolvió una cinemática inversa y comprobó que el movimiento no pasa por una singularidad. Sin esa comprobación, un movimiento pequeño de la punta exige velocidades articulares enormes.
- 🔗 **Se estudia junto con:** cinemática inversa, espacio de trabajo, jacobiano, singularidad.

📘 **Dónde se aprende** (2 clases): [B97-C02 · Cinemática de manipuladores](../programa/clases/B97/B97-C02-cinematica-de-manipuladores/CLASE.md); [B101-C01 · Transformaciones homogéneas y parametrización de eslabones (Denavit-Hartenberg)](../programa/clases/B101/B101-C01-transformaciones-homogeneas-y-parametrizacion-de-eslabones-denavit-hartenberg/CLASE.md).

### Cinemática inversa

- La cinemática inversa calcula los ángulos para una posición.
- Cinemática inversa: de la pose del extremo a los ángulos.

💡 **Cómo se explica en la clase [B97-C02](../programa/clases/B97/B97-C02-cinematica-de-manipuladores/CLASE.md):**
- *Descripción textual:* los ángulos dan la posición por cinemática directa y se recuperan por la inversa; el jacobiano relaciona velocidades y su determinante anuncia las singularidades.
- Resolver la cinemática inversa con la ley de cosenos e identificar las dos soluciones.
- 🎯 **Por qué importa:** Cada vez que un brazo coge una carga o una herramienta alguien resolvió una cinemática inversa y comprobó que el movimiento no pasa por una singularidad. Sin esa comprobación, un movimiento pequeño de la punta exige velocidades articulares enormes.
- 🔗 **Se estudia junto con:** cinemática directa, espacio de trabajo, jacobiano, singularidad.

📘 **Dónde se aprende** (2 clases): [B97-C02 · Cinemática de manipuladores](../programa/clases/B97/B97-C02-cinematica-de-manipuladores/CLASE.md); [B101-C02 · Cinemática inversa y redundancia de manipuladores](../programa/clases/B101/B101-C02-cinematica-inversa-y-redundancia-de-manipuladores/CLASE.md).

### Cinética

- La energía potencial es `U(q) = −log π(q)` (salvo constante), la cinética `K(p) = ½ pᵀp` y el hamiltoniano `H(q, p) = U(q) + K(p)`.

💡 **Contexto en la clase [B19-C03](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md):**
- **Idea central (modelo mental):** Piensa que `U(q)` es la altura de un terreno y que lanzas una canica con una velocidad aleatoria. La canica rueda, sube las laderas y desacelera, y al cabo de un tiempo la detienes: esa es tu propuesta. En un cuenco alargado, la canica corre a lo largo del eje largo sin tener que vencer las paredes, algo que un paso aleatorio no puede hacer.
- 🎯 **Por qué importa:** Una posterior bidimensional con dos parámetros correlacionados al 95 % tiene forma de un óvalo muy alargado y estrecho. Un Metropolis de paso aleatorio, para no salirse del óvalo, da pasos minúsculos y recorre la distribución a paso de tortuga.
- 🔗 **Se estudia junto con:** posición, momento, energía potencial, hamiltoniano.

📘 **Dónde se aprende** (1 clase): [B19-C03 · Hamiltonian Monte Carlo y NUTS](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md).

### Cinética de reparación

- La cinética de reparación es la evolución del número de roturas con el tiempo.

💡 **Cómo se explica en la clase [B112-C05](../programa/clases/B112/B112-C05-dano-y-reparacion-del-adn-por-radiacion-espacial/CLASE.md):**
- Límite: la cinética de reparación real depende de la fase del ciclo celular, de las proteínas implicadas y de la cromatina, nada de lo cual se modela aquí.
- Simular la cinética de reparación con tasas rápida y lenta y calcular las roturas residuales a 24 h.
- 🎯 **Por qué importa:** Falta la clase de mecanismos moleculares de daño y reparación. Sin ella, la diferencia de eficacia biológica entre fotones e iones pesados (B112-C01, C02) y la incertidumbre del riesgo (C04) parecen cifras arbitrarias.
- 🔗 **Se estudia junto con:** rotura doble, daño agrupado o complejo, reparación, unión de extremos no homólogos.

📘 **Dónde se aprende** (1 clase): [B112-C05 · Daño y reparación del ADN por radiación espacial](../programa/clases/B112/B112-C05-dano-y-reparacion-del-adn-por-radiacion-espacial/CLASE.md).

### Cinta elástica

- Una cinta elástica (*tape spring*) es una lámina curvada que se aplana y enrolla y recupera su forma al soltarse.

💡 **Cómo se explica en la clase [B95-C04](../programa/clases/B95/B95-C04-antenas-desplegables-para-satelites-pequenos/CLASE.md):**
- Límite: el modelo es de flexión elástica con curvatura uniforme; ignora la torsión, la fricción entre vueltas y el comportamiento real de la cinta al desplegarse.
- 🎯 **Por qué importa:** Un enlace con la Tierra necesita una antena, y una antena que no se despliega deja el satélite mudo. La decisión central: ¿qué longitud necesita la antena, cómo se pliega sin dañarla y qué riesgo añade el mecanismo?
- 🔗 **Se estudia junto con:** monopolo de cuarto de onda, hilo de quemado, fibra neutra, inhibidor.

📘 **Dónde se aprende** (1 clase): [B95-C04 · Antenas desplegables para satélites pequeños](../programa/clases/B95/B95-C04-antenas-desplegables-para-satelites-pequenos/CLASE.md).

### Cintura

- La cintura `w₀` es el radio del haz en su punto más estrecho (donde la intensidad cae a `1/e²`).

💡 **Cómo se explica en la clase [B92-C02](../programa/clases/B92/B92-C02-divergencia-del-haz-y-perdidas-por-apuntamiento-optico/CLASE.md):**
- Reducir `θ` a la mitad (duplicar la cintura) suma `6,02 dB`.
- W["cintura w0"] --> T["divergencia theta = lambda/(pi w0)"]
- 🎯 **Por qué importa:** Una antena de radiofrecuencia tolera décimas de grado; un haz óptico, microrradianes. La decisión central: ¿qué divergencia conviene y qué apuntamiento hay que garantizar para que la ganancia ganada no se pierda?
- 🔗 **Se estudia junto con:** divergencia, ganancia, error de apuntamiento, distribución de Rayleigh.

📘 **Dónde se aprende** (1 clase): [B92-C02 · Divergencia del haz y pérdidas por apuntamiento óptico](../programa/clases/B92/B92-C02-divergencia-del-haz-y-perdidas-por-apuntamiento-optico/CLASE.md).

### Cinturón principal

- El cinturón principal es la región entre Marte y Júpiter.

💡 **Contexto en la clase [B52-C14](../programa/clases/B52/B52-C14-cinturones-de-asteroides/CLASE.md):**
- **Idea central (modelo mental):** Como empujar un columpio siempre en el mismo punto del vaivén: las resonancias son los lugares donde los empujes de Júpiter se repiten y se acumulan. Límite: aquí solo se calculan las posiciones; los efectos de la resonancia no se simulan.
- 🎯 **Por qué importa:** Las posiciones de las resonancias fijan dónde mirar en un cinturón. La decisión central: ¿en qué semiejes están las resonancias de Júpiter y cómo se comprueba el cálculo?
- 🔗 **Se estudia junto con:** resonancia p:q, laguna de Kirkwood, partícula de prueba.

📘 **Dónde se aprende** (1 clase): [B52-C14 · Cinturones de asteroides](../programa/clases/B52/B52-C14-cinturones-de-asteroides/CLASE.md).

### Cinturones de Van Allen

- Los cinturones de Van Allen son las regiones de partículas atrapadas.

💡 **Cómo se explica en la clase [B30-C16](../programa/clases/B30/B30-C16-cinturones-de-van-allen/CLASE.md):**
- python programa/clases/B30/B30-C16-cinturones-de-van-allen/cinturones.py
- 🎯 **Por qué importa:** Las partículas con ángulo de paso pequeño se pierden en la atmósfera; las demás quedan atrapadas y dañan satélites. La decisión central: ¿qué partículas quedan atrapadas y con qué periodo rebotan?
- 🔗 **Se estudia junto con:** ángulo de paso ecuatorial, punto de espejo, cono de pérdida, periodo de rebote.

📖 **Explicado a fondo:** [Cinturones de Van Allen](esencial/esencial-a-c.md#cinturones-de-van-allen) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B30-C16 · Cinturones de Van Allen](../programa/clases/B30/B30-C16-cinturones-de-van-allen/CLASE.md).

### CIP

- El CIP es el polo de referencia que separa el movimiento del eje en precesión-nutación y en movimiento polar (S1, glosario).

💡 **Contexto en la clase [B13-C22](../programa/clases/B13/B13-C22-parametros-de-orientacion-terrestre-precesion-nutacion-ut1-y-movimiento-polar/CLASE.md):**
- **Idea central (modelo mental):** Piensa en tres engranajes encadenados: el primero (`W`) mueve el eje dentro de la Tierra, el segundo (`R`) gira la Tierra alrededor de ese eje, el tercero (`Q`) mueve el eje respecto de las estrellas. El orden importa; cada engranaje tiene su propia incertidumbre y su propio periodo.
- 🎯 **Por qué importa:** Una estación terrestre apunta a una nave en el sistema celeste. Para ello debe saber cuánto ha girado la Tierra, hacia dónde apunta su eje en el cielo y dónde está ese eje dentro de la corteza.
- 🔗 **Se estudia junto con:** parámetros de orientación terrestre (EOP), movimiento polar, UT1 − UTC, precesión-nutación.

📘 **Dónde se aprende** (1 clase): [B13-C22 · Parámetros de orientación terrestre: precesión, nutación, UT1 y movimiento polar](../programa/clases/B13/B13-C22-parametros-de-orientacion-terrestre-precesion-nutacion-ut1-y-movimiento-polar/CLASE.md).

### Circulación

- La circulación es la integral de línea sobre una curva cerrada.
- La circulación de la línea de conjunción tiene tasa `|q n₁ − p n₂|`.

💡 **Cómo se explica en la clase [B09-C19](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md):**
- La circulación a lo largo del ecuador es `∮ v·dr = 2π a_E · (ω a_E) = 2π a_E² ω = 1,8639 × 10¹⁰ m²/s`.
- Stokes dice que el total de remolino en una superficie es la circulación en su borde.
- 🎯 **Por qué importa:** La gravedad no tiene fuentes fuera de la masa que la produce, y eso permite calcular la gravedad de un planeta esférico sin sumar cada átomo: basta medir el flujo. La rotación de la Tierra produce un campo de velocidades con circulación no nula, y esa circulación mide cuánto «gira» el campo.
- 🔗 **Se estudia junto con:** campo vectorial, divergencia, rotacional, integral de línea.

📘 **Dónde se aprende** (2 clases): [B09-C19 · Cálculo vectorial introductorio](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md); [B73-C10 · Resonancias de movimiento medio](../programa/clases/B73/B73-C10-resonancias-de-movimiento-medio/CLASE.md).

### Circular

- Es `√2` veces la circular.

💡 **Cómo se explica en la clase [B71-C15](../programa/clases/B71/B71-C15-velocidad-de-escape/CLASE.md):**
- La relación con la circular rasante terrestre (`7905.37 m/s`) cumple `√2 v_c` con diferencia `0e+00`.
- *Descripción textual:* anular la energía da el umbral; es `√2` veces la circular, se contrasta con las fichas, la rotación lo reduce algo y la integración confirma el umbral.
- 🎯 **Por qué importa:** La velocidad de escape es el umbral entre una órbita cerrada y una trayectoria abierta. La decisión central: ¿qué velocidad hay que alcanzar para no volver y cuánto la reduce partir de una altura o de una superficie que gira?
- 🔗 **Se estudia junto con:** velocidad de escape, exceso hiperbólico, velocidad de rotación.

📘 **Dónde se aprende** (1 clase): [B71-C15 · Velocidad de escape](../programa/clases/B71/B71-C15-velocidad-de-escape/CLASE.md).

### Circularización

- La circularización es la pérdida de excentricidad por emisión.

💡 **Contexto en la clase [B27-C13](../programa/clases/B27/B27-C13-binarias-compactas/CLASE.md):**
- **Idea central (modelo mental):** Cada órbita pierde energía, se acerca, orbita más rápido y pierde energía aún más rápido. El tiempo restante cae como `a⁴`, así que la mayor parte de la vida es lenta y los últimos segundos son vertiginosos.
- 🎯 **Por qué importa:** La fusión de dos estrellas de neutrones fue el primer evento detectado en ondas gravitacionales y en luz. Saber cuánto falta para una fusión, a qué frecuencia, y cómo la excentricidad la acelera, es la base de toda búsqueda.
- 🔗 **Se estudia junto con:** masa de chirrido, frecuencia gravitacional, tiempo de fusión, orden de cuadrupolo.

📘 **Dónde se aprende** (1 clase): [B27-C13 · Binarias compactas](../programa/clases/B27/B27-C13-binarias-compactas/CLASE.md).

### Círculo fundamental

- Un sistema de coordenadas esféricas se define por un polo (el eje de la latitud), un círculo fundamental (el «ecuador» del sistema, a 90° del polo) y un origen de longitud sobre él.

💡 **Cómo se explica en la clase [B04-C19](../programa/clases/B04/B04-C19-transformaciones-de-coordenadas-astronomicas/CLASE.md):**
- Describir un sistema de coordenadas por su polo, su círculo fundamental y su origen de longitud.
- 🎯 **Por qué importa:** Un catálogo da las posiciones en ecuatoriales; un estudio de la Vía Láctea necesita galácticas; un análisis del plano del sistema solar usa eclípticas. Cambiar de sistema es rutina, y un error de signo o de matriz mueve el objeto decenas de grados.
- 🔗 **Se estudia junto con:** sistema de coordenadas esféricas, polo, origen de longitud, ecuatorial.

📘 **Dónde se aprende** (1 clase): [B04-C19 · Transformaciones de coordenadas astronómicas](../programa/clases/B04/B04-C19-transformaciones-de-coordenadas-astronomicas/CLASE.md).

### Círculo máximo

- Un círculo máximo es la intersección de la esfera con un plano que pasa por su centro; su radio es `R`.

💡 **Cómo se explica en la clase [B04-C16](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md):**
- Dos puntos a 60° N con `Δλ = 160°` están a un arco de paralelo `R cos 60° × (160° en rad) = 0,5 × 2,7925 × 6371 = 8895,6 km` y a una distancia de círculo máximo `6560,2 km`.
- Si cortas una naranja por un plano que pasa por su centro, el borde del corte es un círculo máximo; es el más grande que cabe en ella.
- 🎯 **Por qué importa:** Para pasar de un lugar a otro de la Tierra, un avión sigue (casi) un círculo máximo. Para decidir cuánto debe girar un telescopio entre dos estrellas, se calcula la distancia angular sobre la esfera celeste.
- 🔗 **Se estudia junto con:** esfera, círculo menor, distancia angular, distancia de círculo máximo.

📘 **Dónde se aprende** (1 clase): [B04-C16 · Geometría de esferas y círculos máximos](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md).

### Círculo menor

- Un círculo menor es la intersección con un plano que no pasa por el centro; los paralelos de latitud (salvo el ecuador) lo son.

💡 **Cómo se explica en la clase [B04-C16](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md):**
- Definir círculo máximo y distinguirlo de un círculo menor (paralelo).
- 🎯 **Por qué importa:** Para pasar de un lugar a otro de la Tierra, un avión sigue (casi) un círculo máximo. Para decidir cuánto debe girar un telescopio entre dos estrellas, se calcula la distancia angular sobre la esfera celeste.
- 🔗 **Se estudia junto con:** esfera, círculo máximo, distancia angular, distancia de círculo máximo.

📘 **Dónde se aprende** (1 clase): [B04-C16 · Geometría de esferas y círculos máximos](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md).

### Círculo unidad

- El círculo unidad es la circunferencia de radio 1 centrada en el origen.

💡 **Cómo se explica en la clase [B04-C06](../programa/clases/B04/B04-C06-identidades-trigonometricas/CLASE.md):**
- Imagina un punto que recorre el círculo unidad.
- A["Ángulo x en radianes"] --> B["Punto (cos x, sen x) en el círculo unidad"]
- 🎯 **Por qué importa:** Casi toda medición astronómica es un ángulo: la posición de una estrella respecto de otra, el tamaño aparente de la Luna, el desplazamiento por paralaje. Y casi todos esos ángulos son diminutos, de segundos de arco.
- 🔗 **Se estudia junto con:** tangente, radián, segundo de arco, identidad.

📘 **Dónde se aprende** (1 clase): [B04-C06 · Identidades trigonométricas](../programa/clases/B04/B04-C06-identidades-trigonometricas/CLASE.md).

### Circumpolar

- Un astro es circumpolar si nunca se pone.
- Un astro circumpolar nunca se pone para ese lugar.

💡 **Cómo se explica en la clase [B01-C11](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md):**
- Por geometría (nuestra), las estrellas de declinación `|δ| > 90° − |φ| = 56,55°`, en el mismo hemisferio que el polo visible, son circumpolares: nunca se ponen.
- Decir si una estrella sale y se pone o es circumpolar para una latitud.
- 🎯 **Por qué importa:** Antes de cualquier telescopio, la humanidad dedujo mucho del cielo a simple vista. Que el Sol «salga» y «se ponga» es una observación; que la Tierra gire es una interpretación (C05) que explica además el movimiento de todas las estrellas.
- 🔗 **Se estudia junto con:** horizonte, cénit, meridiano, altura.

📘 **Dónde se aprende** (2 clases): [B01-C11 · Movimiento aparente del Sol y las estrellas](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md); [B08-C02 · Esfera celeste y horizonte local](../programa/clases/B08/B08-C02-esfera-celeste-y-horizonte-local/CLASE.md).

### Circunferencia

- La circunferencia es la longitud del contorno de un círculo; el estadio es una unidad antigua de longitud cuyo valor exacto se discute.
- Una circunferencia de radio `r` es el conjunto de puntos a distancia `r` de un centro.

💡 **Cómo se explica en la clase [B02-C03](../programa/clases/B02/B02-C03-astronomia-griega-y-helenistica/CLASE.md):**
- La distancia cenital en Alejandría fue de 7°12′ (7,2°, o 1/50 de círculo); con unos 5 000 estadios entre las ciudades la circunferencia sale `5 000 × 50 = 250 000` estadios, la cifra que se le atribuye (S2).
- *Descripción textual:* de dos lugares con distancia conocida y la diferencia de ángulos del Sol sale la fracción del círculo; multiplicando la distancia por la inversa de esa fracción se obtiene la circunferencia, y al convertir la unidad antigua a kilómetros aparece la mayor incertidumbre.
- 🎯 **Por qué importa:** Un modelo geométrico responde a «¿qué figura reproduce estos movimientos?». Es una forma nueva de preguntar frente a la regla puramente numérica.
- 🔗 **Se estudia junto con:** estadio, meridiano, precesión de los equinoccios, catálogo estelar.

📘 **Dónde se aprende** (2 clases): [B02-C03 · Astronomía griega y helenística](../programa/clases/B02/B02-C03-astronomia-griega-y-helenistica/CLASE.md); [B04-C09 · Circunferencias y elipses](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md).

### Cizalla kepleriana

- La cizalla kepleriana es `dΩ/d ln r = −(3/2)Ω`.

💡 **Cómo se explica en la clase [B73-C16](../programa/clases/B73/B73-C16-dinamica-de-anillos/CLASE.md):**
- Calcular la velocidad orbital y la cizalla kepleriana de un anillo.
- Cizalla kepleriana: Omega(r) y tasa de cizalla -(3/2) Omega:
- 🎯 **Por qué importa:** Un anillo existe donde las mareas impiden que las partículas se junten, se ensancha por viscosidad y se estructura por resonancias con las lunas. La decisión central: ¿qué escalas fijan dónde hay un anillo, cuánto dura y dónde lo moldean las lunas?
- 🔗 **Se estudia junto con:** límite de Roche, criterio de Hill, resonancia, ensanchamiento viscoso.

📘 **Dónde se aprende** (1 clase): [B73-C16 · Dinámica de anillos](../programa/clases/B73/B73-C16-dinamica-de-anillos/CLASE.md).

### Cizallamiento tangencial

- El cizallamiento tangencial `γ_t = θ_E/(2θ)`.

💡 **Contexto en la clase [B36-C09](../programa/clases/B36/B36-C09-cumulos-en-colision-como-prueba-de-materia-oscura/CLASE.md):**
- **Idea central (modelo mental):** Es como cruzar una nube de polvo pegajoso con otra de arena: el polvo se frena en el choque y la arena sigue su camino.
- 🎯 **Por qué importa:** Que la masa esté separada del gas es el argumento clave contra explicaciones sin materia oscura. La decisión central: ¿cuánto debe medir el desplazamiento y con qué incertidumbre se localiza la masa?
- 🔗 **Se estudia junto con:** sección eficaz por masa, columna de masa, profundidad óptica, esfera isoterma singular.

📘 **Dónde se aprende** (1 clase): [B36-C09 · Cúmulos en colisión como prueba de materia oscura](../programa/clases/B36/B36-C09-cumulos-en-colision-como-prueba-de-materia-oscura/CLASE.md).

### CK

- Los tipos descritos por NAIF son SPK (posición y velocidad), CK (orientación de nave), PCK (tamaño, forma y orientación de cuerpos), IK (campo de visión de instrumentos), FK (marcos), LSK (segundos intercalares), SCLK (reloj de nave) y DSK (formas).

💡 **Cómo se explica en la clase [B74-C21](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md):**
- Por tipo: SPK, CK, PCK, IK, FK, LSK, SCLK.
- Un CK (actitud de la nave) junto con IK y FK.
- 🎯 **Por qué importa:** Un resultado de navegación depende de qué kernels se cargaron y en qué orden: dos corridas con el mismo código pueden dar trayectorias distintas. La decisión central: ¿cómo declaro, valido y audito el conjunto de kernels de una solución para que sea reproducible?
- 🔗 **Se estudia junto con:** kernel, SPK, PCK, IK.

📘 **Dónde se aprende** (1 clase): [B74-C21 · Kernels SPICE y su uso en navegación](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md).

### Clase

- Una clase es una categoría del mapa.
- La clase es la letra y el número del pico.
- La clase es bajo (`R < 8`), medio (`8 ≤ R < 15`) o alto (`R ≥ 15`) en esta clase.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C22](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md):**
- El laboratorio (400 000 muestras por clase) da `0,15842`.
- Con 30 muestras de entrenamiento por clase y 5000 de prueba por clase, el laboratorio da:
- 🎯 **Por qué importa:** Un mapa de cobertura de suelo parece una verdad; en realidad es una predicción con un error que depende de las muestras elegidas y de cuánto se solapan las clases en el espacio espectral. Cifras como «90 % de exactitud» no significan nada sin decir con qué datos se midieron, ni cómo se reparte el error entre clases.
- 🔗 **Se estudia junto con:** vector espectral, NDVI, muestras de entrenamiento, muestras de prueba.

📘 **Dónde se aprende** (4 clases): [B15-C22 · Clasificación supervisada de imágenes](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md); [B30-C12 · Erupciones y fulguraciones solares](../programa/clases/B30/B30-C12-erupciones-y-fulguraciones-solares/CLASE.md); [B83-C15 · Gestión de configuración](../programa/clases/B83/B83-C15-gestion-de-configuracion/CLASE.md); [B114-C06 · Matriz de riesgo ambiental de un hábitat](../programa/clases/B114/B114-C06-matriz-de-riesgo-ambiental-de-un-habitat/CLASE.md).

### Clase de acciones

- Una clase de acciones agrupa títulos con los mismos derechos.

💡 **Cómo se explica en la clase [B125-C03](../programa/clases/B125/B125-C03-gobierno-corporativo-de-una-empresa-espacial/CLASE.md):**
- Si una fracción `b` de las acciones es Clase B con `k` votos y el resto (`1 − b`) tiene un voto: `poder = k b / (k b + 1 − b)`.
- Calcular el poder de voto de una clase de acciones con `k` votos por acción.
- 🎯 **Por qué importa:** Las decisiones de una empresa se estructuran en su gobierno y, en el espacio, el capital intensivo hace que quien controla la votación controle el rumbo de misiones de años; ninguna clase lo trata.
- 🔗 **Se estudia junto con:** poder de voto, consejo, cuota, índice de Banzhaf.

📘 **Dónde se aprende** (1 clase): [B125-C03 · Gobierno corporativo de una empresa espacial](../programa/clases/B125/B125-C03-gobierno-corporativo-de-una-empresa-espacial/CLASE.md).

### Clase de calidad

- Clase de calidad: categoría por umbrales.

💡 **Contexto en la clase [B48-C11](../programa/clases/B48/B48-C11-calidad-y-clasificacion-de-datos/CLASE.md):**
- **Idea central (modelo mental):** Es clasificar fruta por calibre: los umbrales fijan las cajas y la distribución dice cuántas caen en cada una.
- 🎯 **Por qué importa:** Un programa que exige la mejor calidad espera mucho; uno que acepta cualquiera desperdicia las buenas noches. La decisión central: ¿con qué frecuencia se da cada clase y cuánto hay que esperar?
- 🔗 **Se estudia junto con:** Lognormal, Mediana, Función de distribución, Espera media.

📘 **Dónde se aprende** (1 clase): [B48-C11 · Calidad y clasificación de datos](../programa/clases/B48/B48-C11-calidad-y-clasificacion-de-datos/CLASE.md).

### Clase de limpieza

- Sala limpia: recinto con control de partículas y otros contaminantes. Clase de limpieza: número `N` que fija el límite de partículas por tamaño.

💡 **Cómo se explica en la clase [B90-C02](../programa/clases/B90/B90-C02-buenas-practicas-de-sala-limpia/CLASE.md):**
- ⚠️ **Error frecuente:** Confundir la clase con la limpieza de la superficie. El aire y las superficies se controlan por separado (C04)
- 🎯 **Por qué importa:** Una partícula sobre una óptica, un sello o un contacto puede degradar una misión; las partículas llegan con el aire, la ropa y las herramientas. La decisión central: ¿qué clase de sala puede sostener esta actividad con este número de personas, y cuánto hay que esperar tras una perturbación?
- 🔗 **Se estudia junto con:** Sala limpia, Filtro de alta eficiencia, Renovaciones por hora (ACH), Mezcla perfecta.

📘 **Dónde se aprende** (1 clase): [B90-C02 · Buenas prácticas de sala limpia](../programa/clases/B90/B90-C02-buenas-practicas-de-sala-limpia/CLASE.md).

### Clase de luminosidad

- Una clase de luminosidad distingue enanas, gigantes y supergigantes.

💡 **Cómo se explica en la clase [B24-C10](../programa/clases/B24/B24-C10-espectros-y-clasificacion-estelar/CLASE.md):**
- La escala de temperaturas que corresponde a cada tipo depende de la clase de luminosidad y de la edad: las estrellas pre-secuencia principal de tipos G5 a K6 son unos `250 K` más frías que las enanas (S4, resumen).
- 🎯 **Por qué importa:** La intensidad de una línea espectral no crece simplemente con la temperatura: depende de cuántos átomos están en el nivel adecuado y de cuántos están ionizados. Por eso un mismo elemento domina en estrellas de temperaturas muy distintas.
- 🔗 **Se estudia junto con:** ley de Wien, tipo espectral, ecuación de Boltzmann, ecuación de Saha.

📘 **Dónde se aprende** (1 clase): [B24-C10 · Espectros y clasificación estelar](../programa/clases/B24/B24-C10-espectros-y-clasificacion-estelar/CLASE.md).

### Clase de servicio

- La clase de servicio del protocolo de paquetes es `bulk`, `normal` o `expedited`, con prioridad 0, 1 y 2.

💡 **Cómo se explica en la clase [B94-C05](../programa/clases/B94/B94-C05-calidad-de-servicio-y-prioridades-en-redes-espaciales/CLASE.md):**
- La evidencia es la tabla de latencia por clase de servicio del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *tabla de latencia por clase de servicio*: retardo medio, fracción entregada y cola por clase, política y carga; incluye la conservación y la lista de qué es consultado, propio y sintético.
- 🎯 **Por qué importa:** Si la demanda supera a la capacidad, alguien espera. La decisión central: ¿qué política de cola garantiza lo urgente sin dejar sin servicio a las demás clases, y a qué coste?
- 🔗 **Se estudia junto con:** FIFO, Prioridad estricta, reparto ponderado, inanición.

📘 **Dónde se aprende** (1 clase): [B94-C05 · Calidad de servicio y prioridades en redes espaciales](../programa/clases/B94/B94-C05-calidad-de-servicio-y-prioridades-en-redes-espaciales/CLASE.md).

### Clasificación

- En clasificación la respuesta es una categoría (planeta o no); en regresión, un número (la masa, la temperatura).

💡 **Cómo se explica en la clase [B17-C02](../programa/clases/B17/B17-C02-aprendizaje-supervisado/CLASE.md):**
- Distinguir clasificación y regresión, y entrenamiento, validación y prueba.
- 🎯 **Por qué importa:** Un modelo que clasifica señales como «candidata» o «no candidata» puede acertar el 100 % de los ejemplos con los que se entrenó y fallar la cuarta parte de los nuevos: memorizó. Lo que importa a un equipo científico es el desempeño en datos que el modelo no vio.
- 🔗 **Se estudia junto con:** aprendizaje supervisado, etiquetas, regresión, conjunto de entrenamiento.

📘 **Dónde se aprende** (1 clase): [B17-C02 · Aprendizaje supervisado](../programa/clases/B17/B17-C02-aprendizaje-supervisado/CLASE.md).

### Clasificación a bordo

- La clasificación a bordo decide la clase de una observación sin esperar a la Tierra.

💡 **Cómo se explica en la clase [B97-C21](../programa/clases/B97/B97-C21-clasificacion-y-priorizacion-autonoma-de-muestras-a-bordo/CLASE.md):**
- python programa/clases/B97/B97-C21-clasificacion-y-priorizacion-autonoma-de-muestras-a-bordo/clasificacion_priorizacion.py
- 🎯 **Por qué importa:** Con enlaces de unos pocos kilobits por segundo y retardo de minutos, enviar solo lo valioso multiplica el rendimiento científico. Hay que saber cuánto confiar en el clasificador y cuánto pierde una regla simple frente al óptimo.
- 🔗 **Se estudia junto con:** probabilidad posterior, valor esperado, presupuesto de enlace, mochila 0/1.

📘 **Dónde se aprende** (1 clase): [B97-C21 · Clasificación y priorización autónoma de muestras a bordo](../programa/clases/B97/B97-C21-clasificacion-y-priorizacion-autonoma-de-muestras-a-bordo/CLASE.md).

### Clasificador de dominio

- Un clasificador de dominio se entrena para distinguir datos de entrenamiento de datos de despliegue; si lo logra (AUC mayor que 0,5), las distribuciones difieren.

💡 **Cómo se explica en la clase [B17-C07](../programa/clases/B17/B17-C07-validacion-fuera-de-distribucion/CLASE.md):**
- El mejor clasificador de dominio tiene un AUC igual a la probabilidad de que una muestra de la segunda población supere a una de la primera, `Φ(d/√2) = Φ(0,7071) = 0,760`.
- B -- "KS, clasificador de dominio" --> C["Hay cambio"]
- 🎯 **Por qué importa:** Un modelo se entrena con un catálogo y se despliega sobre otro: otro telescopio, otra época, otro brillo límite. Su exactitud medida en validación cruzada deja de valer, y el modelo no avisa: responde con la misma seguridad.
- 🔗 **Se estudia junto con:** distribución de entrenamiento, despliegue, cambio de covariables, cambio de prevalencia.

📘 **Dónde se aprende** (1 clase): [B17-C07 · Validación fuera de distribución](../programa/clases/B17/B17-C07-validacion-fuera-de-distribucion/CLASE.md).

### Clasto balístico

- Un clasto balístico sigue una trayectoria bajo gravedad y arrastre.

💡 **Cómo se explica en la clase [B70-C07](../programa/clases/B70/B70-C07-flujos-de-lava-y-depositos-piroclasticos/CLASE.md):**
- Alcance balistico de clastos (v0 = 100 m/s, 45 grados, d = 0,2 m, rho_p = 2500; ilustrativos)
- 🎯 **Por qué importa:** La misma lava fluye distinto según la pendiente, el espesor y la reología; los piroclastos llegan más lejos si no hay aire. La decisión central: ¿cuánto fluye una colada y hasta dónde llegan los clastos en cada mundo?
- 🔗 **Se estudia junto con:** colada, modelo de Bingham, espesor crítico, depósito piroclástico.

📘 **Dónde se aprende** (1 clase): [B70-C07 · Flujos de lava y depósitos piroclásticos](../programa/clases/B70/B70-C07-flujos-de-lava-y-depositos-piroclasticos/CLASE.md).

### Clausius–Clapeyron

- La relación de Clausius–Clapeyron es `p = p_t exp[(L/R_v)(1/T_t − 1/T)]`.
- El calor latente de vaporización `L` es la energía por kilogramo para evaporar. Clausius–Clapeyron relaciona `P_v` con `T` mediante `dP/dT = P L M/(R T²)`, con `M` la masa molar y `R` la constante de los gases.
- La ley de Langmuir da el flujo de masa `J = α P √(M/(2πRT))`, con `α = 1` como cota superior. Clausius–Clapeyron: `P(T) = 1 Pa · exp(−H/R (1/T − 1/T₁))`.

💡 **Cómo se explica en la clase [B53-C13](../programa/clases/B53/B53-C13-geomorfologia-de-hielos/CLASE.md):**
- Calcular la presión de vapor del hielo con Clausius–Clapeyron.
- El script [hielo.py](hielo.py) calcula `p`, `J` y la vida del hielo a cuatro temperaturas y verifica la pendiente de Clausius–Clapeyron (comprueba 10⁻⁶ relativa).
- 🎯 **Por qué importa:** Una forma de hielo (un depósito, un glaciar, un cráter sombreado) persiste o desaparece según su temperatura. La decisión central: ¿a qué temperatura el hielo expuesto sobrevive miles de millones de años y a cuál se pierde en días?
- 🔗 **Se estudia junto con:** flujo de Hertz–Knudsen, trampa fría.

📘 **Dónde se aprende** (3 clases): [B53-C13 · Geomorfología de hielos](../programa/clases/B53/B53-C13-geomorfologia-de-hielos/CLASE.md); [B56-C06 · Agua líquida y solventes alternativos](../programa/clases/B56/B56-C06-agua-liquida-y-solventes-alternativos/CLASE.md); [B84-C06 · Comportamiento bajo vacío](../programa/clases/B84/B84-C06-comportamiento-bajo-vacio/CLASE.md).

### Clave

- La clave es la respuesta correcta verificada.

💡 **Cómo se explica en la clase [B131-C07](../programa/clases/B131/B131-C07-ejercicios-de-transferencia/CLASE.md):**
- Verificar la clave de cada variante por dos vías.
- La evidencia es el banco de variantes con clave del ejercicio 12 (sección 20).
- ⚠️ **Error frecuente:** Dar la clave sin verificarla. Se corrige con 8.1.
- 🎯 **Por qué importa:** Resolver bien un problema practicado puede ser memoria. La decisión central: ¿qué debe cambiar para que el ejercicio mida que el estudiante comprendió la ley y no el procedimiento?
- 🔗 **Se estudia junto con:** Transferencia, cercana, media, lejana.

📘 **Dónde se aprende** (1 clase): [B131-C07 · Ejercicios de transferencia](../programa/clases/B131/B131-C07-ejercicios-de-transferencia/CLASE.md).

### Clave de caché

- Una clave de caché identifica un resultado por su entrada.

💡 **Cómo se explica en la clase [B14-C30](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md):**
- La clave debe incluir la versión del código; si no, la caché devolvería resultados del código anterior.
- 🎯 **Por qué importa:** Cada madrugada llegan datos nuevos. Si un humano debe lanzar cada paso, tarde o temprano se olvida uno; si un lote corrupto atraviesa la cadena, contamina el producto final; si un fallo de red detiene todo y al reiniciar se repite desde cero, se pierde tiempo.
- 🔗 **Se estudia junto con:** cadena, grafo acíclico dirigido (DAG), orden topológico, idempotencia.

📘 **Dónde se aprende** (1 clase): [B14-C30 · Cadenas de procesamiento automatizado de datos](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md).

### CLEAN

- El CLEAN de Högbom resta el haz sucio desplazado, con ganancia, en el pico del residuo.
- La imagen sucia y el haz sucio. CLEAN (Högbom): resta iterativa de componentes puntuales.

💡 **Cómo se explica en la clase [B46-C19](../programa/clases/B46/B46-C19-imagenes-de-radio-y-clean/CLASE.md):**
- CLEAN supone fuentes puntuales; las extensas requieren escalas múltiples.
- B["haz sucio"] --> L["CLEAN: pico y resta"]
- 🎯 **Por qué importa:** La imagen sucia no se puede interpretar por los lóbulos del haz. La decisión central: ¿cuándo detener la deconvolución para no ajustar ruido?
- 🔗 **Se estudia junto con:** imagen sucia, componente CLEAN, ganancia del lazo, residuo.

📘 **Dónde se aprende** (2 clases): [B46-C19 · Imágenes de radio y CLEAN](../programa/clases/B46/B46-C19-imagenes-de-radio-y-clean/CLASE.md); [B51-C06 · Autocalibración iterativa con modelo de cielo](../programa/clases/B51/B51-C06-autocalibracion-iterativa-con-modelo-de-cielo/CLASE.md).

### Cliente

- Un cliente es el componente que habla con un proveedor concreto.
- Un cliente es el programa que pide.

💡 **Cómo se explica en la clase [B14-C22](../programa/clases/B14/B14-C22-acceso-a-datos-heliofisicos-abiertos-con-sunpy/CLASE.md):**
- No usé SunPy ni ningún servicio: no sé cómo se comporta cada cliente real, ni sus límites de volumen, ni sus atributos exclusivos.
- Las búsquedas se construyen con atributos: `a.Time(inicio, fin)` para el intervalo, `a.Instrument`, `a.Wavelength`, `a.Sample` para la cadencia, y `a.Level` y `a.Physobs`; los atributos específicos de un cliente viven en submódulos como `attrs.vso` y `attrs.jsoc`; el operador `|` combina búsquedas con «o».
- 🎯 **Por qué importa:** Quieres estudiar una región activa del Sol durante un día usando imágenes ultravioleta. Hay cientos de miles de archivos repartidos en varios proveedores.
- 🔗 **Se estudia junto con:** búsqueda, registro, cadencia, submuestrear.

📘 **Dónde se aprende** (2 clases): [B14-C22 · Acceso a datos heliofísicos abiertos con SunPy](../programa/clases/B14/B14-C22-acceso-a-datos-heliofisicos-abiertos-con-sunpy/CLASE.md); [B14-C29 · Servicios de datos geoespaciales estándar (OGC)](../programa/clases/B14/B14-C29-servicios-de-datos-geoespaciales-estandar-ogc/CLASE.md).

### Climatología

- La climatología es la media.

💡 **Cómo se explica en la clase [B33-C11](../programa/clases/B33/B33-C11-modelos-empiricos-y-de-persistencia-en-clima-espacial/CLASE.md):**
- A 1 día la persistencia explica el 58 %; a 27 días la recurrencia apenas supera a la climatología.
- *Descripción textual:* la serie genera pronósticos simples cuyas métricas se comparan con la climatología.
- ⚠️ **Error frecuente:** Usar solo la climatología como referencia. Se corrige con 8.1.
- 🎯 **Por qué importa:** Un modelo complejo debe superar a la persistencia. La decisión central: ¿qué desfase da el mejor pronóstico simple?
- 🔗 **Se estudia junto con:** persistencia, recurrencia, destreza.

📘 **Dónde se aprende** (1 clase): [B33-C11 · Modelos empíricos y de persistencia en clima espacial](../programa/clases/B33/B33-C11-modelos-empiricos-y-de-persistencia-en-clima-espacial/CLASE.md).

### Clúster

- Un clúster es un conjunto de equipos conectados que se usan como un sistema.

💡 **Cómo se explica en la clase [B14-C16](../programa/clases/B14/B14-C16-computacion-distribuida-y-hpc/CLASE.md):**
- Límite: en un clúster la comunicación depende de la red y del patrón de comunicación, no solo de `log₂ p`.
- En la práctica se mide con casos pequeños en el clúster real antes de decidir.
- 🎯 **Por qué importa:** Una simulación de la población de escombros orbitales requiere cien veces más cálculo del que tu equipo puede dar en una semana. Pides tiempo en un clúster y debes decidir: ¿cuántos procesos pido?
- 🔗 **Se estudia junto con:** planificador, escalado fuerte, escalado débil, ley de Gustafson.

📘 **Dónde se aprende** (1 clase): [B14-C16 · Computación distribuida y HPC](../programa/clases/B14/B14-C16-computacion-distribuida-y-hpc/CLASE.md).

### Clutter

- El clutter son falsas detecciones.

💡 **Cómo se explica en la clase [B74-C30](../programa/clases/B74/B74-C30-asociacion-de-observaciones-y-correlacion-de-pistas/CLASE.md):**
- El límite a `6σ` (`85,4 %`) viene de observaciones verdaderas fuera de compuerta y de clutter cerca de una pista.
- Ejercicio 5 · autónomo. ¿Qué pasa con la fracción de escenas correctas si el clutter se duplica?
- 🎯 **Por qué importa:** Una asociación incorrecta no se ve en el filtro: el estado sigue convergiendo, pero hacia el objeto equivocado. La decisión central: ¿qué compuerta y qué regla de asignación equilibran el riesgo de perder una observación verdadera y el de aceptar una falsa o la de otro objeto?
- 🔗 **Se estudia junto con:** compuerta, asociación de vecino más cercano, asignación global, pista.

📘 **Dónde se aprende** (1 clase): [B74-C30 · Asociación de observaciones y correlación de pistas](../programa/clases/B74/B74-C30-asociacion-de-observaciones-y-correlacion-de-pistas/CLASE.md).

### C/N₀

- Pérdida en espacio libre (FSPL): atenuación por distancia y frecuencia. `C/N₀`: portadora sobre densidad de ruido.

💡 **Cómo se explica en la clase [B96-C27](../programa/clases/B96/B96-C27-operacion-de-equipos-de-radiofrecuencia-en-la-estacion/CLASE.md):**
- `C/N₀ = PIRE − FSPL − L_otras + G/T − 10 log₁₀ k`;
- La comprobación en escala lineal (`C/N₀ = PIRE·G_r/(FSPL·L·k·T)`) coincide a `10⁻⁹` dB y `(4π d/λ)²` reproduce la FSPL a `10⁻⁹`.
- 🎯 **Por qué importa:** Un transmisor con potencia de más interfiere con otros y viola la licencia; con potencia de menos, no cierra el enlace. La decisión central: ¿qué potencia hace falta para un margen suficiente sin exceder el límite autorizado?
- 🔗 **Se estudia junto con:** PIRE, Pérdida en espacio libre (FSPL), Eb/N₀, Margen.

📘 **Dónde se aprende** (1 clase): [B96-C27 · Operación de equipos de radiofrecuencia en la estación](../programa/clases/B96/B96-C27-operacion-de-equipos-de-radiofrecuencia-en-la-estacion/CLASE.md).

### C/N0 = PIRE − L_total + G/T − 10 log₁₀ k

- `G/T` es `G_r − 10 log₁₀ T_sis` (dB/K). `C/N0 = PIRE − L_total + G/T − 10 log₁₀ k` (dB-Hz).

💡 **Contexto en la clase [B89-C05](../programa/clases/B89/B89-C05-presupuesto-de-enlace/CLASE.md):**
- 🎯 **Por qué importa:** El presupuesto de enlace es el documento donde se decide si una misión puede transmitir; un error de 3 dB equivale a duplicar la potencia o el tamaño de la antena. La decisión central: ¿cuánto margen queda y qué tasa de datos máxima admite este enlace?
- 🔗 **Se estudia junto con:** PIRE, pérdida de espacio libre, G/T, Eb/N0 = C/N0 − 10 log₁₀ R_b.

📘 **Dónde se aprende** (1 clase): [B89-C05 · Presupuesto de enlace](../programa/clases/B89/B89-C05-presupuesto-de-enlace/CLASE.md).

### CNR

- La CNR (relación contraste-ruido) es `contraste × SNR × MTF`.

💡 **Cómo se explica en la clase [B83-C17](../programa/clases/B83/B83-C17-verificacion-frente-a-validacion/CLASE.md):**
- La CNR es `0,08 × SNR × 0,614`; con SNR de 105 (albedo 0,3) da 5,15, apenas sobre el umbral 5, y con albedo 0,05 (costa oscura) la SNR baja a `105·√(0,05/0,3)` y la CNR a 2,10: no se detecta.
- Paso 3 · CNR. `0,08 × 42,9 × 0,614 = 2,10`.
- 🎯 **Por qué importa:** Un proyecto puede pasar todas las pruebas de requisitos y fracasar en el uso. La decisión central: ¿además de cumplir los requisitos, el sistema satisface la necesidad en las condiciones reales de uso?
- 🔗 **Se estudia junto con:** Verificación, Validación, MTF, umbral de detección.

📘 **Dónde se aprende** (1 clase): [B83-C17 · Verificación frente a validación](../programa/clases/B83/B83-C17-verificacion-frente-a-validacion/CLASE.md).

### CO₂ supercrítico

- El CO₂ supercrítico es un fluido por encima de su punto crítico (no se trata aquí; el gas ideal es una aproximación).

💡 **Contexto en la clase [B54-C13](../programa/clases/B54/B54-C13-atmosfera-de-venus/CLASE.md):**
- **Idea central (modelo mental):** Bajar por una atmósfera adiabática es bajar una escalera de temperatura regular: cada kilómetro sube la temperatura lo mismo.
- 🎯 **Por qué importa:** Venus es el caso extremo de atmósfera densa y caliente. La pregunta motivadora: ¿cómo se enfría su atmósfera con la altura y cuánto pesa?
- 🔗 **Se estudia junto con:** adiabata, altura sobre la superficie, masa de la atmósfera.

📘 **Dónde se aprende** (1 clase): [B54-C13 · Atmósfera de Venus](../programa/clases/B54/B54-C13-atmosfera-de-venus/CLASE.md).

### Coalición

- Una coalición es un subconjunto de actores.

💡 **Cómo se explica en la clase [B119-C36](../programa/clases/B119/B119-C36-gobernanza-de-los-recursos-espaciales/CLASE.md):**
- V["v(S) para cada coalición"] --> M["Contribuciones marginales"]
- Límite: el valor de cada coalición es un dato inventado y las partes también negocian poder, no solo aportes.
- 🎯 **Por qué importa:** B59 trata los recursos de forma técnica; la gobernanza de la explotación plantea cuestiones de reparto que ninguna clase trata. C25 da el caso económico y C34 las medidas de desigualdad; esta clase cierra el bloque con reglas de reparto.
- 🔗 **Se estudia junto con:** valor de Shapley, núcleo, eficiencia, reparto proporcional.

📘 **Dónde se aprende** (1 clase): [B119-C36 · Gobernanza de los recursos espaciales](../programa/clases/B119/B119-C36-gobernanza-de-los-recursos-espaciales/CLASE.md).

### Coaseguro

- El coaseguro `c` es la fracción de la pérdida que paga el asegurador.

💡 **Cómo se explica en la clase [B127-C04](../programa/clases/B127/B127-C04-exclusiones-deducibles-y-limites-de-polizas/CLASE.md):**
- La exclusión y el coaseguro actúan multiplicando: `0,9 × 0,8 = 0,72` sobre el pago de C.
- Paso 4 · Coaseguro. `0,8 × 25 = 20 MUSD`; el asegurado retiene `10 MUSD`.
- 🎯 **Por qué importa:** Leer una póliza exige entender sus exclusiones, deducibles y límites; el catálogo no lo trataba. La decisión central: ¿qué parte de la pérdida retiene el asegurado y cómo cambia el precio al cambiar las condiciones?
- 🔗 **Se estudia junto con:** deducible, límite, exclusión, valor esperado limitado.

📘 **Dónde se aprende** (1 clase): [B127-C04 · Exclusiones, deducibles y límites de pólizas](../programa/clases/B127/B127-C04-exclusiones-deducibles-y-limites-de-polizas/CLASE.md).

### Cobertura

- La cobertura es la fracción real de intervalos que contienen el parámetro; la cobertura nominal es la que se declara.
- La cobertura de un intervalo es esa fracción.
- La cobertura de un intervalo es la fracción de repeticiones en que contiene la verdad.
- *(y 26 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C08](../programa/clases/B12/B12-C08-intervalos-de-confianza/CLASE.md):**
- Con 100 000 repeticiones del experimento: la cobertura del intervalo `t` es `0,9507`; con `σ` conocida y 1,96, `0,9518`; con `s` estimada pero 1,96 (error común), `0,9199`: un «95 %» que en realidad es 92 %.
- D --> E["Cobertura:<br/>≈ 95 % contienen μ"]
- 🎯 **Por qué importa:** Un número sin rango es una afirmación sin evidencia de su precisión. «La distancia es 148,5 m» no dice si el valor es fiable al metro o al decámetro. Un intervalo con su nivel de confianza lo dice, y permite decidir si una medición cumple un requisito o si hay que tomar más datos.
- 🔗 **Se estudia junto con:** intervalo de confianza, nivel de confianza, distribución t de Student, semiancho.

📘 **Dónde se aprende** (29 clases): [B12-C08 · Intervalos de confianza](../programa/clases/B12/B12-C08-intervalos-de-confianza/CLASE.md); [B19-C08 · Calibración probabilística](../programa/clases/B19/B19-C08-calibracion-probabilistica/CLASE.md); [B22-C05 · Pruebas de inversión con datos sintéticos](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md); [B26-C20 · Límites observacionales de modelos cosmológicos](../programa/clases/B26/B26-C20-limites-observacionales-de-modelos-cosmologicos/CLASE.md); [B28-C10 · Localización probabilística de eventos](../programa/clases/B28/B28-C10-localizacion-probabilistica-de-eventos/CLASE.md); [B31-C18 · Restricciones experimentales de teorías](../programa/clases/B31/B31-C18-restricciones-experimentales-de-teorias/CLASE.md) y 23 más.

### Cobertura 24/7

- Posición: puesto de la sala de control. Cobertura 24/7: presencia en las 168 h semanales.

💡 **Cómo se explica en la clase [B96-C03](../programa/clases/B96/B96-C03-roles-de-control-de-mision/CLASE.md):**
- Paso 4 · Cobertura. 168 horas con exactamente una persona.
- Construir un cronograma de tres turnos y verificar su cobertura hora por hora.
- 🎯 **Por qué importa:** Un rol vacío durante un contacto es un contacto perdido. La decisión central: ¿cuánto personal exige cubrir una posición 24/7 y cómo se comprueba que el cronograma no deja huecos?
- 🔗 **Se estudia junto con:** Posición, Horas efectivas, Turno, Equivalente a tiempo completo (ETC).

📘 **Dónde se aprende** (1 clase): [B96-C03 · Roles de control de misión](../programa/clases/B96/B96-C03-roles-de-control-de-mision/CLASE.md).

### Cobertura de cielo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C21](../programa/clases/B42/B42-C21-estrellas-guia-naturales-y-cobertura-de-cielo/CLASE.md):**
- python programa/clases/B42/B42-C21-estrellas-guia-naturales-y-cobertura-de-cielo/estrellas_guia_naturales.py
- 🎯 **Por qué importa:** La mayoría del cielo no tiene una estrella brillante cerca: la cobertura limita a la óptica adaptativa natural. La decisión central: ¿hasta qué magnitud corrige el lazo y qué fracción del cielo queda cubierta?
- 🔗 **Se estudia junto con:** presupuesto de fotones, punto cero, magnitud límite, ley de cuentas.

📘 **Dónde se aprende** (1 clase): [B42-C21 · Estrellas guía naturales y cobertura de cielo](../programa/clases/B42/B42-C21-estrellas-guia-naturales-y-cobertura-de-cielo/CLASE.md).

### Cobertura de decisión

- La cobertura de decisión exige `D = V` y `D = F`.

💡 **Cómo se explica en la clase [B88-C39](../programa/clases/B88/B88-C39-normas-de-aseguramiento-de-software-ecss-do-178c/CLASE.md):**
- T --> C["Cobertura de decision: 2 pruebas"]
- Analogía: la decisión es una cerradura con tres cerrojos: la cobertura de decisión prueba que abre y que no abre;
- 🎯 **Por qué importa:** Elegir el nivel de cobertura determina el esfuerzo de prueba. La decisión central: ¿qué cobertura piden los distintos niveles y cuánto cuesta cada una en pruebas?
- 🔗 **Se estudia junto con:** MC/DC, tamaño mínimo, exhaustiva.

📘 **Dónde se aprende** (1 clase): [B88-C39 · Normas de aseguramiento de software (ECSS, DO-178C)](../programa/clases/B88/B88-C39-normas-de-aseguramiento-de-software-ecss-do-178c/CLASE.md).

### Cobertura de líneas

- La cobertura de líneas `líneas ejecutadas / ejecutables`.

💡 **Cómo se explica en la clase [B88-C14](../programa/clases/B88/B88-C14-pruebas-de-software-embarcado/CLASE.md):**
- La cobertura de líneas sube con cada prueba, pero solo la mutación mide si las pruebas detectan cambios.
- Ejercicio 6 · autónomo. ¿Por qué la línea `else:` no cuenta en la cobertura?
- 🎯 **Por qué importa:** Una prueba que pasa no prueba nada si pasaría también con el código roto. La decisión central: ¿las pruebas detectan los cambios de comportamiento o solo recorren el código?
- 🔗 **Se estudia junto con:** mutante, muerto, vivo, puntuación de mutación.

📘 **Dónde se aprende** (1 clase): [B88-C14 · Pruebas de software embarcado](../programa/clases/B88/B88-C14-pruebas-de-software-embarcado/CLASE.md).

### Cobertura de polvo

- La cobertura de polvo `1 − exp(−n π d²/4)`.

💡 **Cómo se explica en la clase [B43-C19](../programa/clases/B43/B43-C19-seguridad-y-mantenimiento/CLASE.md):**
- Estimar la cobertura de polvo por dos vías.
- Ejercicio 7. Cobertura de polvo teórica.
- 🎯 **Por qué importa:** La seguridad empieza por saber cuán grande es el riesgo. La decisión central: ¿cuánta potencia y qué temperatura aparecen en el foco, cómo se balancea la montura y cuánto polvo es aceptable?
- 🔗 **Se estudia junto con:** irradiancia solar total, concentración, temperatura de equilibrio, filtro en la apertura.

📘 **Dónde se aprende** (1 clase): [B43-C19 · Seguridad y mantenimiento](../programa/clases/B43/B43-C19-seguridad-y-mantenimiento/CLASE.md).

### Cobertura de ramas

- La cobertura de ramas cuenta ramas distintas ejecutadas.

💡 **Cómo se explica en la clase [B88-C37](../programa/clases/B88/B88-C37-fuzzing-autorizado-de-software-embarcado-en-banco-de-pruebas/CLASE.md):**
- Guiado por cobertura: 2 errores en cada una de las 10 campañas, `11,0` de 13 ramas y primer hallazgo tras `40` ejecuciones.
- guiado por cobertura : bugs distintos por campana (10 semillas) = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ; ramas medias = 11.0/13 ; primer hallazgo medio = 40 ejecuciones
- 🎯 **Por qué importa:** Las pruebas diseñadas por una persona no prevén todas las combinaciones. La decisión central: ¿qué estrategia de entradas encuentra más fallos con menos ejecuciones en un banco autorizado?
- 🔗 **Se estudia junto con:** fuzzing, corpus, mutación, hallazgo.

📘 **Dónde se aprende** (1 clase): [B88-C37 · Fuzzing autorizado de software embarcado en banco de pruebas](../programa/clases/B88/B88-C37-fuzzing-autorizado-de-software-embarcado-en-banco-de-pruebas/CLASE.md).

### Cobertura espectral

- La cobertura espectral es el rango de longitudes de onda de una banda.

💡 **Cómo se explica en la clase [B15-C24](../programa/clases/B15/B15-C24-fusion-de-imagenes-de-distintos-sensores/CLASE.md):**
- Describir la relación de resolución y de cobertura espectral entre una pancromática y las bandas multiespectrales.
- Predecir qué bandas mejoran y cuáles empeoran según la cobertura espectral de la pancromática.
- 🎯 **Por qué importa:** Un mapa de cobertura exige distinguir objetos pequeños (caminos, parcelas) y también su firma espectral (si son vegetación o suelo). Ninguna imagen entrega ambas cosas a la vez.
- 🔗 **Se estudia junto con:** fusión, pansharpening, resolución espacial, inyección de detalle.

📘 **Dónde se aprende** (1 clase): [B15-C24 · Fusión de imágenes de distintos sensores](../programa/clases/B15/B15-C24-fusion-de-imagenes-de-distintos-sensores/CLASE.md).

### Cobertura nominal

- La cobertura es la fracción real de intervalos que contienen el parámetro; la cobertura nominal es la que se declara.

💡 **Cómo se explica en la clase [B12-C08](../programa/clases/B12/B12-C08-intervalos-de-confianza/CLASE.md):**
- Ejercicio 12 · integrador. Elabora tu *informe de cobertura*: simula 20 000 muestras de un modelo conocido para `n = 5` y `n = 20`; calcula la cobertura de los intervalos `t` y de los de 1,96; compara con el nivel nominal y concluye cuántos datos exigirías.
- 🎯 **Por qué importa:** Un número sin rango es una afirmación sin evidencia de su precisión. «La distancia es 148,5 m» no dice si el valor es fiable al metro o al decámetro. Un intervalo con su nivel de confianza lo dice, y permite decidir si una medición cumple un requisito o si hay que tomar más datos.
- 🔗 **Se estudia junto con:** intervalo de confianza, nivel de confianza, distribución t de Student, semiancho.

📘 **Dónde se aprende** (1 clase): [B12-C08 · Intervalos de confianza](../programa/clases/B12/B12-C08-intervalos-de-confianza/CLASE.md).

### Cobertura simple

- La cobertura simple es la fracción de tiempo con al menos un satélite visible; la cuádruple, con al menos cuatro.

💡 **Cómo se explica en la clase [B89-C17](../programa/clases/B89/B89-C17-constelaciones-y-cobertura/CLASE.md):**
- La cobertura global simple es `83,7 %` y la cuádruple `0,0 %`.
- Con 12 satélites (12/3/1) los visibles medios bajan a `0,519` (teoría `0,520`) y la cobertura simple a `47,5 %`: reducir `T` a la mitad reduce los visibles a la mitad, pero la cobertura cae más rápido.
- 🎯 **Por qué importa:** El número de satélites, su altitud y la inclinación fijan cuánta gente o cuántos usuarios ven al menos uno (o cuatro, para navegar) y cuánto cuesta lograrlo. La decisión central: ¿cuántos satélites y qué geometría dan la cobertura necesaria?
- 🔗 **Se estudia junto con:** constelación Walker delta, huella, cuádruple, promedio global de visibles.

📘 **Dónde se aprende** (1 clase): [B89-C17 · Constelaciones y cobertura](../programa/clases/B89/B89-C17-constelaciones-y-cobertura/CLASE.md).

### Cociente

- Si comparas dos cantidades por cociente preguntas «¿cuántas veces más grande?»; si comparas sus logaritmos y los restas preguntas «¿cuántos órdenes de magnitud de diferencia?».
- El cociente `P_IC/P_sync = U_rad/U_B` (Thomson).

💡 **Cómo se explica en la clase [B01-C02](../programa/clases/B01/B01-C02-escalas-desde-la-tierra-al-cosmos-observable/CLASE.md):**
- Por ejemplo, el cociente entre el radio del Sol (6,957 × 10⁸ m) y el de la Tierra (6,371 × 10⁶ m) es `(6,957/6,371) × 10^(8−6) = 1,092 × 10² ≈ 109`.
- Comparar con el cociente da directamente el factor; los exponentes dan una estimación inmediata de orden de magnitud.
- ⚠️ **Error frecuente:** Confundir diferencia y cociente. Alguien dice que 10²⁶ es «cuatro veces» 10²² porque 26 es casi 4 veces 6.
- 🎯 **Por qué importa:** Cuando alguien dice que Próxima Centauri está «a cuatro años luz» y que Andrómeda está «a dos millones y medio», es fácil oír solo «lejos» y «más lejos». Pero entre una y otra hay un factor de casi seis cien mil.
- 🔗 **Se estudia junto con:** orden de magnitud, notación científica, logaritmo decimal, unidad astronómica.

📘 **Dónde se aprende** (2 clases): [B01-C02 · Escalas desde la Tierra al cosmos observable](../programa/clases/B01/B01-C02-escalas-desde-la-tierra-al-cosmos-observable/CLASE.md); [B27-C21 · Dispersión Compton inversa y emisión de alta energía](../programa/clases/B27/B27-C21-dispersion-compton-inversa-y-emision-de-alta-energia/CLASE.md).

### Cociente a/g☉

- El cociente `a/g☉` compara la aceleración con la gravedad solar.

💡 **Cómo se explica en la clase [B75-C11](../programa/clases/B75/B75-C11-propulsion-de-bajo-empuje/CLASE.md):**
- Con `a = 10⁻⁵ m/s²` el cociente `a/g☉` es `0,17 %` y la desviación es `0,19 %`; con `4×10⁻⁴` el cociente es `6,7 %`, la excentricidad final es `0,38` y la desviación es `24 %`.
- Ejercicio 4 · autónomo. Calcula `g☉` a 1 au y el cociente `a/g☉` para `a = 10⁻⁴ m/s²`.
- 🎯 **Por qué importa:** Un motor de alta `I_sp` ahorra propulsante pero tarda mucho. La decisión central: ¿cuánto delta-v y cuánto tiempo cuesta una espiral y cuándo es válida la fórmula de Edelbaum?
- 🔗 **Se estudia junto con:** propulsión de bajo empuje, espiral de Edelbaum, fracción de propulsante.

📘 **Dónde se aprende** (1 clase): [B75-C11 · Propulsión de bajo empuje](../programa/clases/B75/B75-C11-propulsion-de-bajo-empuje/CLASE.md).

### Cociente C/O

- Un cociente C/O es la razón del número de átomos de carbono al de oxígeno.

💡 **Cómo se explica en la clase [B55-C01](../programa/clases/B55/B55-C01-abundancia-quimica-cosmica/CLASE.md):**
- Ejercicio 2 · con una pista. Calcula el cociente C/O en número a partir de los `log ε` (sección 8.4).
- Ejercicio 9 · transferencia. Un artículo presenta `[Fe/H]` = −1,0 (cociente solar).
- 🎯 **Por qué importa:** Cualquier modelo químico del espacio parte de una composición inicial: cuánto hidrógeno, helio, carbono u oxígeno hay. Las fuentes dan esa composición en una escala logarítmica poco intuitiva, y los modelos piden fracciones en número o en masa.
- 🔗 **Se estudia junto con:** abundancia logarítmica, fracción en número, fracción en masa, dex.

📘 **Dónde se aprende** (1 clase): [B55-C01 · Abundancia química cósmica](../programa/clases/B55/B55-C01-abundancia-quimica-cosmica/CLASE.md).

### Cociente de desviaciones

- El cociente de desviaciones es la desviación de una revolución entre la de la anterior.

💡 **Cómo se explica en la clase [B76-C19](../programa/clases/B76/B76-C19-orbitas-de-mantenimiento/CLASE.md):**
- Cociente de desviaciones sucesivas sin control = 1.53, 1.32, 1.69, 1.19
- 🎯 **Por qué importa:** Una órbita periódica inestable no se mantiene sola. La decisión central: ¿con qué frecuencia y qué impulso hay que corregir para que el error no crezca?
- 🔗 **Se estudia junto con:** mantenimiento, apuntamiento, error de ejecución.

📘 **Dónde se aprende** (1 clase): [B76-C19 · Órbitas de mantenimiento](../programa/clases/B76/B76-C19-orbitas-de-mantenimiento/CLASE.md).

### Cociente de diferencias

- El cociente de diferencias de `f` entre `x` y `x + h` es `[f(x + h) − f(x)]/h`: la tasa de cambio media en ese intervalo.

💡 **Cómo se explica en la clase [B09-C03](../programa/clases/B09/B09-C03-derivada-como-tasa-de-cambio/CLASE.md):**
- Calcular un cociente de diferencias e interpretarlo como tasa media.
- Ejercicio 12 · integrador. Elabora tu *tabla de cocientes de diferencia con error y paso óptimo*: para `sin t` en `t = 1`, calcula el cociente progresivo y el central con `h = 10⁻¹, 10⁻², …, 10⁻¹²`, el error frente a `cos 1`, el orden observado y el `h` con menor error.
- 🎯 **Por qué importa:** Casi toda cantidad en ciencias espaciales cambia con el tiempo o la posición: la altura de un cohete, la fase de una estrella variable, el brillo de un cometa. Lo que se quiere saber suele ser con qué rapidez cambia, y en qué instante deja de crecer.
- 🔗 **Se estudia junto con:** media, derivada, recta tangente, tasa de cambio instantánea.

📘 **Dónde se aprende** (1 clase): [B09-C03 · Derivada como tasa de cambio](../programa/clases/B09/B09-C03-derivada-como-tasa-de-cambio/CLASE.md).

### Cociente de ejes

- El cociente de ejes `q = cos i` para un disco delgado.

💡 **Cómo se explica en la clase [B38-C08](../programa/clases/B38/B38-C08-observaciones-sinteticas-de-galaxias-simuladas/CLASE.md):**
- Cada paso del instrumento cambia la medida: el recorte del campo la reduce un 2,5 %, la PSF la aumenta un 3 % y la inclinación aplasta el cociente de ejes.
- El cociente de ejes a 60° es `0,4989` frente a `cos 60° = 0,5`.
- 🎯 **Por qué importa:** La imagen que se compara con el telescopio no es la simulación, sino la simulación vista a través de un instrumento. La decisión central: ¿cuánto cambian la PSF, la inclinación y el ruido lo que mides?
- 🔗 **Se estudia junto con:** observación sintética, PSF, convolución, radio efectivo.

📘 **Dónde se aprende** (1 clase): [B38-C08 · Observaciones sintéticas de galaxias simuladas](../programa/clases/B38/B38-C08-observaciones-sinteticas-de-galaxias-simuladas/CLASE.md).

### Cociente de exposición

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B27-C19](../programa/clases/B27/B27-C19-observatorios-de-rayos-x-y-gamma/CLASE.md):**
- **Idea central (modelo mental):** El fondo fluctúa; la significancia dice cuán improbable es la fluctuación observada. Una fórmula adecuada hace que, sin fuente, `3σ` ocurra con la frecuencia que le corresponde (`1,35 × 10⁻³`).
- 🎯 **Por qué importa:** Decir «detectamos la fuente a 5σ» exige saber qué fórmula se usó y cuántos falsos positivos produce. La decisión central: ¿qué significancia tiene un par de conteos y qué señal mínima se necesita para una detección?
- 🔗 **Se estudia junto con:** conteos «on», conteos «off», significancia, semilla.

📘 **Dónde se aprende** (1 clase): [B27-C19 · Observatorios de rayos X y gamma](../programa/clases/B27/B27-C19-observatorios-de-rayos-x-y-gamma/CLASE.md).

### Cociente de líneas

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B34-C05](../programa/clases/B34/B34-C05-diagnostico-de-densidad-electronica-coronal/CLASE.md):**
- **Idea central (modelo mental):** Un termómetro que marca máximo a partir de cierta temperatura: no distingue entre muy caliente y más caliente.
- 🎯 **Por qué importa:** Un diagnóstico es útil solo en su rango sensible. La decisión central: ¿en qué rango de densidades es fiable un cociente de líneas?
- 🔗 **Se estudia junto con:** densidad crítica, saturación, inversión, sensibilidad.

📘 **Dónde se aprende** (1 clase): [B34-C05 · Diagnóstico de densidad electrónica coronal](../programa/clases/B34/B34-C05-diagnostico-de-densidad-electronica-coronal/CLASE.md).

### Cociente de Rayleigh

- Un cociente de Rayleigh es `vᵀA v/vᵀv`.
- El cociente de Rayleigh es una cota superior del valor propio.
- El cociente de Rayleigh estima `f1` con una forma de prueba y da una cota superior.

💡 **Cómo se explica en la clase [B10-C08](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md):**
- Para `[[2, 1], [1, 2]]` con `v₀ = (1, 0)`: el cociente de Rayleigh vale `2` al inicio, `2,8` tras un paso y `2,976` tras dos, camino del `3`.
- Ejercicio 7. Haz dos pasos de la iteración de la potencia con `[[2,1],[1,2]]` y `v₀ = (1, 0)`; calcula el cociente de Rayleigh en cada uno.
- 🎯 **Por qué importa:** Un satélite que rota libremente no gira igual alrededor de cualquier eje: tiene tres ejes especiales —los ejes principales de inercia— en los que la rotación es simple. Conocerlos permite diseñar su estabilización, decidir dónde colocar instrumentos sensibles al giro y entender por qué ciertos giros se desestabilizan.
- 🔗 **Se estudia junto con:** autovector, autovalor, ecuación característica, polinomio característico.

📘 **Dónde se aprende** (3 clases): [B10-C08 · Autovalores y autovectores](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md); [B37-C07 · Oscilaciones radiales y relación período-densidad media](../programa/clases/B37/B37-C07-oscilaciones-radiales-y-relacion-periodo-densidad-media/CLASE.md); [B86-C03 · Arreglos fotovoltaicos desplegables](../programa/clases/B86/B86-C03-arreglos-fotovoltaicos-desplegables/CLASE.md).

### Cociente de reacción

- El cociente de reacción es `Q = a(CH₄)/(a(CO₂) a(H₂)⁴)`.
- El cociente de reacción `Q` es el cociente de productos y reactivos con las actividades actuales.
- El cociente de reacción `Q` tiene la misma forma que `K` pero con las concentraciones o presiones actuales.

💡 **Cómo se explica en la clase [B06-C13](../programa/clases/B06/B06-C13-equilibrio-quimico/CLASE.md):**
- Abajo, una decisión: si el cociente de reacción es menor que la constante, el sistema avanza hacia productos; si es mayor, hacia reactivos; si es igual, está en equilibrio.
- Calcular el cociente de reacción `Q` y compararlo con `K`.
- 🎯 **Por qué importa:** Según el cálculo de esta clase, el CO₂ de Marte puede condensarse como hielo o volver al gas según la temperatura. Es un equilibrio entre CO₂ sólido y gas: `CO₂(s) ⇌ CO₂(g)`.
- 🔗 **Se estudia junto con:** equilibrio químico, constante de equilibrio, sólidos y líquidos puros, actuales.

📘 **Dónde se aprende** (3 clases): [B06-C13 · Equilibrio químico](../programa/clases/B06/B06-C13-equilibrio-quimico/CLASE.md); [B55-C16 · Procesos hidrotermales extraterrestres](../programa/clases/B55/B55-C16-procesos-hidrotermales-extraterrestres/CLASE.md); [B56-C07 · Energía química para la vida](../programa/clases/B56/B56-C07-energia-quimica-para-la-vida/CLASE.md).

### Cociente de Strehl

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B42-C06](../programa/clases/B42/B42-C06-funcion-de-dispersion-puntual/CLASE.md):**
- **Idea central (modelo mental):** Como la mancha que deja una linterna: cuanto más perfecta la lente, más pequeña y brillante.
- 🎯 **Por qué importa:** Toda imagen es la escena convolucionada con la PSF; si la PSF se degrada, se pierde resolución y contraste. La decisión central: ¿cómo se calcula la PSF de una pupila con aberraciones y cuándo basta el pico?
- 🔗 **Se estudia junto con:** PSF, pupila, fase, muestreo.

📘 **Dónde se aprende** (2 clases): [B42-C06 · Función de dispersión puntual](../programa/clases/B42/B42-C06-funcion-de-dispersion-puntual/CLASE.md); [B42-C24 · Métricas de desempeño de óptica adaptativa: Strehl y energía encerrada](../programa/clases/B42/B42-C24-metricas-de-desempeno-de-optica-adaptativa-strehl-y-energia-encerrada/CLASE.md).

### Cociente empuje/peso

- El cociente empuje/peso `T/W₀ = T/(m₀ g₀)` fija la aceleración inicial.

💡 **Contexto en la clase [B75-C10](../programa/clases/B75/B75-C10-maniobras-impulsivas/CLASE.md):**
- 🎯 **Por qué importa:** El modelo impulsivo es útil, pero ¿cuándo es un buen modelo? La decisión central: ¿cuánto delta-v se pierde por quemar durante un tiempo finito y de qué depende, en particular del cociente empuje/peso?
- 🔗 **Se estudia junto con:** empuje finito, pérdida por empuje finito, quema prógrada, flujo másico.

📘 **Dónde se aprende** (1 clase): [B75-C10 · Maniobras impulsivas](../programa/clases/B75/B75-C10-maniobras-impulsivas/CLASE.md).

### Cociente respiratorio

- El cociente respiratorio `RQ` es CO₂ producido sobre O₂ consumido.
- energía libre: mínimo reversible. Cociente respiratorio: CO₂ por O₂ (0,85).

💡 **Cómo se explica en la clase [B108-C01](../programa/clases/B108/B108-C01-sistemas-portatiles-de-soporte-vital-plss/CLASE.md):**
- Calcular el CO₂ producido con el cociente respiratorio.
- 🎯 **Por qué importa:** B106-C09 trata el soporte vital de hábitat; el del traje no tiene clase. La decisión central: ¿cuánto oxígeno, cuánto calor a rechazar y cuánto CO₂ genera una EVA con un perfil de esfuerzo dado, y qué margen deja el sistema?
- 🔗 **Se estudia junto con:** PLSS, oxígeno, ventilación, térmico.

📘 **Dónde se aprende** (2 clases): [B106-C05 · Suministro y generación de oxígeno](../programa/clases/B106/B106-C05-suministro-y-generacion-de-oxigeno/CLASE.md); [B108-C01 · Sistemas portátiles de soporte vital (PLSS)](../programa/clases/B108/B108-C01-sistemas-portatiles-de-soporte-vital-plss/CLASE.md).

### Cociente respiratorio (RQ)

- Consumo específico de oxígeno: O₂ por kilogramo y minuto. Cociente respiratorio (RQ): mol de CO₂ por mol de O₂.

💡 **Cómo se explica en la clase [B106-C01](../programa/clases/B106/B106-C01-requisitos-de-habitabilidad/CLASE.md):**
- Obtener el CO₂ exhalado con un cociente respiratorio y escalar el balance a una tripulación.
- 🎯 **Por qué importa:** Un hábitat se diseña de adentro hacia afuera: primero lo que consume y emite la tripulación, después la máquina que lo repone. Si el balance humano está mal, todo el ECLSS queda mal dimensionado.
- 🔗 **Se estudia junto con:** Consumo específico de oxígeno, Normoxia, Zona de salud, zona de desempeño.

📘 **Dónde se aprende** (1 clase): [B106-C01 · Requisitos de habitabilidad](../programa/clases/B106/B106-C01-requisitos-de-habitabilidad/CLASE.md).

### Cociente valle/pico

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C19](../programa/clases/B42/B42-C19-reconstruccion-de-imagenes/CLASE.md):**
- RL mantiene positividad, conserva el flujo y baja el cociente valle/pico a `0,702`.
- Medir error relativo y el cociente valle/pico de un par cercano.
- 🎯 **Por qué importa:** Deconvolucionar recupera detalle bajo el límite de difracción pero amplifica el ruido. La decisión central: ¿qué método usar y qué se gana y se pierde con cada uno?
- 🔗 **Se estudia junto con:** convolución, filtro inverso, filtro de Wiener, Richardson-Lucy.

📘 **Dónde se aprende** (1 clase): [B42-C19 · Reconstrucción de imágenes](../programa/clases/B42/B42-C19-reconstruccion-de-imagenes/CLASE.md).

### Cociente α/ε

- El cociente `α/ε` fija `T = (α S/(ε σ))^(1/4)` para una placa al Sol con el reverso aislado.

💡 **Cómo se explica en la clase [B85-C05](../programa/clases/B85/B85-C05-recubrimientos-opticos-termicos/CLASE.md):**
- Paso 1 · Cociente. `α/ε = 0,20/0,90 = 0,222`.
- ⚠️ **Error frecuente:** Elegir por `α` solamente. importa el cociente `α/ε` (8.1)
- 🎯 **Por qué importa:** Cambiar un recubrimiento es la forma más barata de mover la temperatura de una superficie decenas de kelvin. La decisión central: ¿qué recubrimiento mantiene la superficie dentro del intervalo al principio y al final de la vida?
- 🔗 **Se estudia junto con:** espejo solar óptico (OSR), envejecimiento, BOL, EOL.

📘 **Dónde se aprende** (1 clase): [B85-C05 · Recubrimientos ópticos térmicos](../programa/clases/B85/B85-C05-recubrimientos-opticos-termicos/CLASE.md).

### Codificación

- La codificación es la correspondencia entre caracteres y bytes;

💡 **Cómo se explica en la clase [B07-C08](../programa/clases/B07/B07-C08-lectura-de-archivos-csv/CLASE.md):**
- Explicar qué es un CSV y sus puntos débiles (delimitador, decimal, codificación).
- ⚠️ **Error frecuente:** No declarar la codificación. Aparecen símbolos raros.
- 🎯 **Por qué importa:** Un archivo CSV parece trivial y por eso engaña: todo se lee como texto, un decimal con coma rompe una columna, una línea vacía pasa inadvertida, y una codificación equivocada convierte «Júpiter» en símbolos raros. Un análisis hecho sobre datos mal leídos puede ser plausible y erróneo a la vez.
- 🔗 **Se estudia junto con:** CSV, delimitador, encabezado, entre comillas.

📘 **Dónde se aprende** (1 clase): [B07-C08 · Lectura de archivos CSV](../programa/clases/B07/B07-C08-lectura-de-archivos-csv/CLASE.md).

### Codificación de Gray

- La codificación de Gray hace que símbolos vecinos difieran en un bit.

💡 **Contexto en la clase [B89-C08](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md):**
- 🎯 **Por qué importa:** La elección de la modulación fija el `Eb/N0` requerido en el presupuesto de enlace y el ancho de banda ocupado; es la base de la codificación y la sincronización siguientes. La decisión central: ¿qué modulación da la tasa que necesito con el `Eb/N0` que mi enlace puede ofrecer?
- 🔗 **Se estudia junto con:** BPSK, QPSK, 8PSK, 16QAM.

📘 **Dónde se aprende** (1 clase): [B89-C08 · Modulación digital](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md).

### Codificador

- Un codificador asigna categorías.

💡 **Cómo se explica en la clase [B119-C26](../programa/clases/B119/B119-C26-doctrinas-y-politicas-espaciales-declaradas-publicamente/CLASE.md):**
- Cada codificador tiene `κ` de `0.697` y `0.795` frente al tema oculto: en la práctica no se conoce la verdad y solo se mide el acuerdo.
- T["Texto declarado"] --> C1["Codificador A"]
- 🎯 **Por qué importa:** C11 y C12 tratan los límites militares y la historia; ninguna clase enseña a leer doctrinas públicas con rigor. La lectura real de documentos oficiales exige fuentes que no se consultaron aquí.
- 🔗 **Se estudia junto con:** doctrina declarada, acuerdo observado, acuerdo por azar, kappa.

📘 **Dónde se aprende** (1 clase): [B119-C26 · Doctrinas y políticas espaciales declaradas públicamente](../programa/clases/B119/B119-C26-doctrinas-y-politicas-espaciales-declaradas-publicamente/CLASE.md).

### Código convolucional

- Un código convolucional de tasa 1/2 y longitud de restricción `K = 7` emite dos bits por cada bit de entrada con los polinomios `G1 = 171` y `G2 = 133` (octal).

💡 **Contexto en la clase [B94-C02](../programa/clases/B94/B94-C02-entrelazado-y-concatenacion-de-codigos/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR W["I palabras RS"] --> IL["entrelazador"] IL --> CV["convolucional<br/>K=7 r=1/2"] CV --> CH["canal: ruido<br/>y rafagas"] CH --> VT["Viterbi<br/>(errores en rafaga)"] VT --> DI["desentrelazador"] DI --> RD["I decodificadores RS"] ``` *Descripción textual:* las palabras se entrelazan, se codifican en convolucional, cruzan el canal;
- 🎯 **Por qué importa:** El decodificador de Viterbi falla en ráfagas y los desvanecimientos también. La decisión central: ¿qué profundidad de entrelazado hace falta para que una ráfaga de `B` octetos no sature ninguna palabra, y qué ganancia da frente a no entrelazar?
- 🔗 **Se estudia junto con:** entrelazado, concatenación, algoritmo de Viterbi, decisión dura.

📘 **Dónde se aprende** (1 clase): [B94-C02 · Entrelazado y concatenación de códigos](../programa/clases/B94/B94-C02-entrelazado-y-concatenacion-de-codigos/CLASE.md).

### Código de bloque (n,k)

- Un código de bloque (n,k) convierte `k` símbolos en `n`.

💡 **Cómo se explica en la clase [B89-C09](../programa/clases/B89/B89-C09-codificacion-correctora-de-errores/CLASE.md):**
- Con `p = 0,02`, la probabilidad de bloque erróneo teórica es `1 − (1−p)⁷ − 7p(1−p)⁶ = 0,00786`; la simulación con `random.Random(89)` da `0,00786` (z = `0,01`) y la BER de información `0,00336`, frente a 0,02 sin código.
- Calcular la probabilidad de bloque no corregido de un código de bloque con capacidad `t`.
- 🎯 **Por qué importa:** La codificación es la herramienta que permite cerrar enlaces de espacio profundo con potencias modestas: cada decibelio de ganancia de código equivale a una antena más grande o a más potencia. La decisión central: ¿cuánta redundancia añadir y cuánto `Eb/N0` se ahorra con ella?
- 🔗 **Se estudia junto con:** capacidad de corrección, Hamming(7,4), tasa del código, entrelazado de profundidad I.

📘 **Dónde se aprende** (1 clase): [B89-C09 · Codificación correctora de errores](../programa/clases/B89/B89-C09-codificacion-correctora-de-errores/CLASE.md).

### Código de estado

- El código de estado resume el resultado (200, 400, 404).
- Un código de estado resume el resultado: 200 (correcto), 304 (sin cambios), 400 (petición inválida), 404 (no existe) (significados generales).

💡 **Cómo se explica en la clase [B14-C31](../programa/clases/B14/B14-C31-apis-de-servicios-de-datos/CLASE.md):**
- Validar parámetros y devolver códigos de estado con mensajes en JSON.
- Código de estado adecuado, un mensaje legible y, si ayuda, datos del error (el parámetro, el máximo permitido), todo en JSON.
- 🎯 **Por qué importa:** Tu catálogo de escenas tiene 250 000 ítems y un programa ajeno quiere recorrerlos. Si le entregas una lista de golpe, se cae; si cada petición repite lo que ya tiene, desperdicias ancho de banda; si cambia un parámetro y falla sin explicación, nadie sabe qué hizo mal.
- 🔗 **Se estudia junto con:** API, recurso, ruta, Paginar.

📘 **Dónde se aprende** (2 clases): [B14-C29 · Servicios de datos geoespaciales estándar (OGC)](../programa/clases/B14/B14-C29-servicios-de-datos-geoespaciales-estandar-ogc/CLASE.md); [B14-C31 · APIs de servicios de datos](../programa/clases/B14/B14-C31-apis-de-servicios-de-datos/CLASE.md).

### Código de referencia

- Un código de referencia es una segunda implementación, independiente, del mismo problema.

💡 **Cómo se explica en la clase [B23-C04](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md):**
- Un código de referencia es útil cuando existe uno confiable; solo prueba lo que hace distinto: aquí el integrador temporal.
- Usar un código independiente (otro integrador temporal) como referencia y interpretar la diferencia.
- ⚠️ **Error frecuente:** Usar como referencia un código que comparte el esquema. Se corrige con la sección 8.6.
- 🎯 **Por qué importa:** Un modelo de conducción de calor en el regolito, con una fuente variable y una condición de flujo en el borde, no tiene solución cerrada. Pero su código puede estar mal en la frontera, en el término fuente o en el tiempo, y ninguna propiedad global lo delata fácilmente.
- 🔗 **Se estudia junto con:** solución fabricada, término fuente, condiciones de frontera, estudio de refinamiento.

📘 **Dónde se aprende** (1 clase): [B23-C04 · Soluciones de referencia y manufactured solutions](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md).

### Código de Rice

- El código de Rice (unario más `k` bits).

💡 **Cómo se explica en la clase [B47-C16](../programa/clases/B47/B47-C16-compresion-de-datos-cientificos/CLASE.md):**
- *Descripción textual:* la predicción concentra los valores cerca de cero, la entropía da el límite y el código de Rice se acerca a él.
- El código de Rice usa `7,26 bit/píxel`, razón `2,20` respecto de 16 bit, con ida y vuelta idéntica.
- 🎯 **Por qué importa:** La compresión sin pérdida está acotada por la entropía; la con pérdida cambia fidelidad por volumen. La decisión central: ¿cuántos bits por píxel necesita la imagen y cuánto error se acepta a cambio de menos datos?
- 🔗 **Se estudia junto con:** entropía de Shannon, residuo de predicción, plegado, bloque adaptativo.

📘 **Dónde se aprende** (1 clase): [B47-C16 · Compresión de datos científicos](../programa/clases/B47/B47-C16-compresion-de-datos-cientificos/CLASE.md).

### Código Gray

- El código Gray `b xor (b >> 1)`.

💡 **Cómo se explica en la clase [B43-C16](../programa/clases/B43/B43-C16-encoders-y-medicion-angular/CLASE.md):**
- Las 4095 transiciones de un código de 12 bits cambian exactamente un bit en Gray: sí.
- En un código de 12 bits, leer durante una transición puede dar hasta `2047` cuentas de error en binario y `0` en Gray.
- 🎯 **Por qué importa:** El codificador es el ojo de la montura: lo que no mide, no lo corrige. La decisión central: ¿qué resolución, qué código y qué calidad de señal dan un error angular menor que el presupuesto?
- 🔗 **Se estudia junto con:** línea, cuentas, paso, error de cuantización.

📘 **Dónde se aprende** (1 clase): [B43-C16 · Encoders y medición angular](../programa/clases/B43/B43-C16-encoders-y-medicion-angular/CLASE.md).

### Código Hamming

- El código Hamming pone bits de paridad en las posiciones potencia de dos.

💡 **Contexto en la clase [B88-C04](../programa/clases/B88/B88-C04-memorias-y-correccion-de-errores/CLASE.md):**
- 🎯 **Por qué importa:** Sin corrección, un SEU corrompe un dato; con SECDED lo corrige al leerlo, pero si dos errores se acumulan en la misma palabra el código ya no corrige. La decisión central: ¿cada cuánto hay que barrer la memoria para que la probabilidad de doble error sea aceptable?
- 🔗 **Se estudia junto con:** síndrome, paridad global, SECDED, barrido.

📘 **Dónde se aprende** (1 clase): [B88-C04 · Memorias y corrección de errores](../programa/clases/B88/B88-C04-memorias-y-correccion-de-errores/CLASE.md).

### Código LDPC (8160, 7136)

- El código LDPC (8160, 7136) de CCSDS 131.0-B-5 transmite 8160 símbolos por 7136 bits de información (tasa 223/255, aprox. 7/8) y cada palabra va precedida de un ASM de 32 bits: la eficiencia es `7136/(8160+32)`.

💡 **Cómo se explica en la clase [B83-C11](../programa/clases/B83/B83-C11-presupuestos-de-datos/CLASE.md):**
- El código LDPC (8160, 7136) con ASM de 32 bits tiene eficiencia `7136/8192 = 0,871094`; con tramas al 97 % la eficiencia total es 84,50 %.
- Calcular la eficiencia de codificación con el código LDPC y el marcador ASM de CCSDS 131.0-B-5.
- 🎯 **Por qué importa:** Un satélite que produce más datos de los que puede bajar los pierde o se satura. La decisión central: ¿cabe todo lo que se produce en los minutos de contacto, y qué tamaño de registrador cubre el peor hueco?
- 🔗 **Se estudia junto con:** tasa bruta, líneas por segundo, compresión, eficiencia de tramas.

📘 **Dónde se aprende** (1 clase): [B83-C11 · Presupuestos de datos](../programa/clases/B83/B83-C11-presupuestos-de-datos/CLASE.md).

### Código RS(n, k)

- Un código RS(n, k) sobre GF(2⁸) tiene `n = 255` símbolos de 8 bits y `k` de información.

💡 **Cómo se explica en la clase [B94-C01](../programa/clases/B94/B94-C01-codigos-reed-solomon-y-ldpc/CLASE.md):**
- Caer en otra palabra de código válida es posible aunque poco frecuente (no se calculó su probabilidad aquí), y en 600 pruebas no hubo ninguna miscorrección; pero no es cero, y por eso la trama lleva además un CRC (ver [B94-C03](../B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md)).
- El código del estándar es el (8160, 7136), de tasa 223/255 y obtenido de un (8176, 7156) por expurgación, acortamiento y extensión; no se implementa aquí.
- 🎯 **Por qué importa:** Un enlace profundo opera con relaciones señal-ruido bajas y no puede reenviar cada trama. La decisión central: ¿cuántos símbolos erróneos tolera una palabra de código, cuánta redundancia cuesta y qué ocurre cuando se supera esa capacidad?
- 🔗 **Se estudia junto con:** capacidad, polinomio generador, síndrome, localizador de errores.

📘 **Dónde se aprende** (1 clase): [B94-C01 · Códigos Reed-Solomon y LDPC](../programa/clases/B94/B94-C01-codigos-reed-solomon-y-ldpc/CLASE.md).

### Codo

- El codo es el valor de `k` donde la inercia deja de bajar rápido.
- El codo `n* = 1 + Z/S` es el número de camiones en el que la excavadora se satura.

💡 **Cómo se explica en la clase [B15-C23](../programa/clases/B15/B15-C23-clasificacion-no-supervisada-y-agrupamiento-de-imagenes/CLASE.md):**
- El «codo» está en `k = 3`, donde la bajada pasa de 86 y 26 unidades a solo 2 por paso.
- Por eso se busca el codo y se razona con conocimiento externo (8.5).
- 🎯 **Por qué importa:** Un satélite fotografía una región que nadie ha cartografiado. Sin muestras, no se puede entrenar un clasificador, pero sí se puede preguntar cuántos «tipos» de superficie distintos hay en las bandas.
- 🔗 **Se estudia junto con:** agrupamiento, k-medias, inercia, algoritmo de Lloyd.

📘 **Dónde se aprende** (2 clases): [B15-C23 · Clasificación no supervisada y agrupamiento de imágenes](../programa/clases/B15/B15-C23-clasificacion-no-supervisada-y-agrupamiento-de-imagenes/CLASE.md); [B97-C27 · Simulación de productividad de flotas de maquinaria](../programa/clases/B97/B97-C27-simulacion-de-productividad-de-flotas-de-maquinaria/CLASE.md).

### Coeficiente

- Un coeficiente es el número que multiplica a una variable (`3` en `3a`).
- Extinción: pérdida de luz en la atmósfera. Coeficiente `k`: mag por masa de aire.

💡 **Contexto en la clase [B03-C13](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md):**
- **Idea central (modelo mental):** Una expresión es una máquina: entra un valor, sale otro.
- 🎯 **Por qué importa:** ¿Cuánto tarda una señal en llegar desde la Tierra hasta Marte? Depende de dónde estén los dos planetas.
- 🔗 **Se estudia junto con:** expresión algebraica, término, términos semejantes, propiedad distributiva.

📘 **Dónde se aprende** (2 clases): [B03-C13 · Expresiones algebraicas iniciales](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md); [B48-C05 · Ventanas atmosféricas](../programa/clases/B48/B48-C05-ventanas-atmosfericas/CLASE.md).

### Coeficiente balístico

- El coeficiente balístico `B = m/(Cd A)` (kg/m²) mide cuánto resiste un cuerpo al frenado: a mayor `B`, menos arrastre.
- El coeficiente balístico es `β = m/(Cd A)`.
- El coeficiente balístico `m/(Cd·A)` mide qué tan fácil lo frena el aire.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B72-C06](../programa/clases/B72/B72-C06-arrastre-atmosferico/CLASE.md):**
- *Descripción textual:* la densidad y el coeficiente balístico dan la aceleración; esta da el decaimiento por vuelta, corregido por la rotación del aire, y de él sale la vida útil.
- Por coeficiente balístico: `B` en kg/m².
- 🎯 **Por qué importa:** Una estación o una constelación baja debe reimpulsarse y un satélite sin propulsión debe reentrar a tiempo. La decisión central: ¿cuánto baja un satélite por vuelta y en cuántos días reentra, según su masa, su área y la densidad del aire?
- 🔗 **Se estudia junto con:** densidad, viento co-rotante, decaimiento, vida útil orbital.

📘 **Dónde se aprende** (7 clases): [B72-C06 · Arrastre atmosférico](../programa/clases/B72/B72-C06-arrastre-atmosferico/CLASE.md); [B75-C15 · Aerofrenado conceptual](../programa/clases/B75/B75-C15-aerofrenado-conceptual/CLASE.md); [B77-C02 · Movimiento en atmósfera](../programa/clases/B77/B77-C02-movimiento-en-atmosfera/CLASE.md); [B77-C14 · Dinámica de reentrada](../programa/clases/B77/B77-C14-dinamica-de-reentrada/CLASE.md); [B96-C18 · Fin de vida y disposición orbital](../programa/clases/B96/B96-C18-fin-de-vida-y-disposicion-orbital/CLASE.md); [B118-C12 · Disposición al fin de vida](../programa/clases/B118/B118-C12-disposicion-al-fin-de-vida/CLASE.md) y 1 más.

### Coeficiente de adherencia

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B47-C12](../programa/clases/B47/B47-C12-optica-en-ambientes-de-vacio/CLASE.md):**
- **Idea central (modelo mental):** El contaminante cae sobre el espejo como polvo sobre una mesa en una habitación cerrada: lentamente, pero sin pausa, hasta cubrirla.
- 🎯 **Por qué importa:** La contaminación reduce la reflectancia y la transmisión sin aviso. La decisión central: ¿cuánto tarda en cubrirse una superficie y cuánto cambia la reflectancia por una película?
- 🔗 **Se estudia junto con:** camino libre medio, flujo de Hertz-Knudsen, monocapa, desgasificación.

📘 **Dónde se aprende** (1 clase): [B47-C12 · Óptica en ambientes de vacío](../programa/clases/B47/B47-C12-optica-en-ambientes-de-vacio/CLASE.md).

### Coeficiente de arrastre

- El coeficiente de arrastre es `Cd = D/(q·A)` y el de sustentación `CL = L/(q·A)`.
- El coeficiente de arrastre de una placa `C_f = D/(½ ρ V² S)`.

💡 **Cómo se explica en la clase [B79-C04](../programa/clases/B79/B79-C04-regimenes-laminar-y-turbulento/CLASE.md):**
- Calcular el coeficiente de arrastre de una placa en ambos regímenes.
- 🎯 **Por qué importa:** El régimen cambia el arrastre y la transferencia de calor por factores de varios; no distinguirlo lleva a subestimar el calentamiento de una pared o la pérdida de presión de un conducto. El tronco no lo trata.
- 🔗 **Se estudia junto con:** número de Reynolds, laminar, turbulento, factor de fricción de Darcy.

📘 **Dónde se aprende** (2 clases): [B77-C04 · Coeficientes de arrastre y sustentación](../programa/clases/B77/B77-C04-coeficientes-de-arrastre-y-sustentacion/CLASE.md); [B79-C04 · Regímenes laminar y turbulento](../programa/clases/B79/B79-C04-regimenes-laminar-y-turbulento/CLASE.md).

### Coeficiente de color

- El coeficiente de color `k''` hace `k = k' + k'' (B−V)`.

💡 **Contexto en la clase [B45-C22](../programa/clases/B45/B45-C22-extincion-atmosferica-masa-de-aire-y-coeficientes-de-color/CLASE.md):**
- **Idea central (modelo mental):** Como una niebla: cuanto más camino recorre la luz, más se atenúa; la pendiente de la recta es la espesura por unidad de camino.
- 🎯 **Por qué importa:** Sin corregir la extinción, la fotometría terrestre depende de la hora. La decisión central: ¿qué `k` y qué fórmula de masa de aire dan la corrección y con qué error?
- 🔗 **Se estudia junto con:** ley de Bouguer, gráfico de Langley, masa de aire, fórmula de Kasten y Young.

📘 **Dónde se aprende** (1 clase): [B45-C22 · Extinción atmosférica, masa de aire y coeficientes de color](../programa/clases/B45/B45-C22-extincion-atmosferica-masa-de-aire-y-coeficientes-de-color/CLASE.md).

### Coeficiente de coma firmado

- El coeficiente de coma firmado es el del término `x(x² + y²)` del ajuste del frente de onda.

💡 **Contexto en la clase [B50-C11](../programa/clases/B50/B50-C11-errores-de-inclinacion-de-elementos-y-superficies/CLASE.md):**
- **Idea central (modelo mental):** Como un péndulo: girar por el punto de suspensión correcto mueve el extremo sin cambiar su altura; con otro punto, además sube.
- 🎯 **Por qué importa:** Un telescopio se alinea corrigiendo inclinaciones y descentramientos. La decisión central: ¿alrededor de qué punto conviene inclinar el secundario para no generar coma?
- 🔗 **Se estudia junto con:** inclinación, pivote, descentrarlo, pivote libre de coma.

📘 **Dónde se aprende** (1 clase): [B50-C11 · Errores de inclinación de elementos y superficies](../programa/clases/B50/B50-C11-errores-de-inclinacion-de-elementos-y-superficies/CLASE.md).

### Coeficiente de correlación

- El coeficiente de correlación `r(X,Y) = Cov(X,Y)/(σ_X σ_Y)` es adimensional y cumple `−1 ≤ r ≤ +1` (S1, 5.2.2, ecuación 14;
- El coeficiente de correlación es `ρ = C₁₂/√(C₁₁C₂₂)`.

💡 **Cómo se explica en la clase [B12-C05](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md):**
- *Descripción textual:* de los pares se calcula la covarianza; normalizada da el coeficiente de correlación; la covarianza aparece en la varianza de una suma y determina cuánto ayuda promediar;
- Calcular e interpretar el coeficiente de correlación de Pearson `r ∈ [−1, 1]`.
- 🎯 **Por qué importa:** En navegación espacial, la posición y la velocidad estimadas por un filtro no tienen errores independientes: un error de posición hacia delante suele ir acompañado de uno de velocidad. Ignorar esa relación da incertidumbres falsas, a veces demasiado optimistas y a veces demasiado pesimistas.
- 🔗 **Se estudia junto con:** covarianza, no correlacionadas, Independientes, no.

📘 **Dónde se aprende** (3 clases): [B12-C05 · Covarianza y correlación](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md); [B26-C22 · Degeneraciones de parámetros cosmológicos](../programa/clases/B26/B26-C22-degeneraciones-de-parametros-cosmologicos/CLASE.md); [B51-C08 · Compensación de retardo y alineación temporal de flujos de antenas](../programa/clases/B51/B51-C08-compensacion-de-retardo-y-alineacion-temporal-de-flujos-de-antenas/CLASE.md).

### Coeficiente de correlación intraclase

- El coeficiente de correlación intraclase es `ICC = σ_u²/(σ_u² + σ_e²)`: la fracción de la varianza total que es estable por unidad.

💡 **Cómo se explica en la clase [B12-C25](../programa/clases/B12/B12-C25-modelos-longitudinales-y-de-efectos-mixtos-para-muestras-pequenas/CLASE.md):**
- Estimar las varianzas dentro y entre unidades en un diseño balanceado y calcular el coeficiente de correlación intraclase (ICC).
- 🎯 **Por qué importa:** Seis personas medidas cuatro veces dan 24 números, pero no 24 piezas de información independientes: las de una misma persona se parecen. Ignorar eso produce intervalos demasiado angostos para el nivel medio y, paradójicamente, demasiado anchos para los cambios dentro de cada persona.
- 🔗 **Se estudia junto con:** diseño longitudinal, modelo de intercepto aleatorio, efectos fijos, efecto aleatorio.

📘 **Dónde se aprende** (1 clase): [B12-C25 · Modelos longitudinales y de efectos mixtos para muestras pequeñas](../programa/clases/B12/B12-C25-modelos-longitudinales-y-de-efectos-mixtos-para-muestras-pequenas/CLASE.md).

### Coeficiente de descarga

- El coeficiente de descarga `Cd` corrige el caudal por una abertura.
- El coeficiente de descarga `C_d` corrige el área efectiva.

💡 **Cómo se explica en la clase [B104-C13](../programa/clases/B104/B104-C13-procedimientos-de-emergencia/CLASE.md):**
- Una cabina ilustrativa de 30 m³ de aire a 294 K con el exterior en vacío y un orificio de coeficiente de descarga 0,6.
- ⚠️ **Error frecuente:** Olvidar el coeficiente de descarga. Inclúyelo en `τ` (8.2).
- 🎯 **Por qué importa:** Un procedimiento sirve si se puede ejecutar dentro del tiempo disponible. La decisión central: ¿para qué tamaños de orificio alcanza un tiempo de respuesta de 15 minutos y a partir de cuál ya no?
- 🔗 **Se estudia junto con:** flujo ahogado, constante de despresurización, tiempo de respuesta.

📘 **Dónde se aprende** (2 clases): [B63-C05 · Contención de muestras extraterrestres: instalaciones y principios](../programa/clases/B63/B63-C05-contencion-de-muestras-extraterrestres-instalaciones-y-principios/CLASE.md); [B104-C13 · Procedimientos de emergencia](../programa/clases/B104/B104-C13-procedimientos-de-emergencia/CLASE.md).

### Coeficiente de descarga Cd

- Flujo estrangulado: caudal máximo por un orificio. Coeficiente de descarga `Cd`: corrección entre el área geométrica y la efectiva.

💡 **Cómo se explica en la clase [B106-C02](../programa/clases/B106/B106-C02-presurizacion-de-modulos/CLASE.md):**
- Rotular que la aleación y el coeficiente de descarga son ilustrativos.
- 🎯 **Por qué importa:** La presión interior empuja hacia afuera sobre todo el casco; un espesor insuficiente rompe el recinto y un orificio pequeño lo vacía lentamente. La decisión central: ¿qué espesor mínimo y qué tiempo de respuesta hay que garantizar para una presión y un tamaño de orificio dados?
- 🔗 **Se estudia junto con:** Esfuerzo de aro, Factor de seguridad (FS), Flujo estrangulado, Constante de tiempo τ.

📘 **Dónde se aprende** (1 clase): [B106-C02 · Presurización de módulos](../programa/clases/B106/B106-C02-presurizacion-de-modulos/CLASE.md).

### Coeficiente de Dice

- La IoU (intersección sobre unión) es `|A ∩ B|/|A ∪ B|`; el coeficiente de Dice es `2|A ∩ B|/(|A| + |B|)`.
- El coeficiente de Dice es `2|P ∩ V| / (|P| + |V|)`.

💡 **Contexto en la clase [B15-C13](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md):**
- **Idea central (modelo mental):** Recortar un lago en un mapa es sencillo si todos los azules son iguales; pero si el mapa tiene un degradado, la tijera que sigue un nivel de azul recorta también parte del degradado. La solución es quitar el degradado primero. Analogía: tijeras sobre un mapa degradado.
- 🎯 **Por qué importa:** Medir el área de las manchas solares, el porcentaje de nubes de una escena o el tamaño de un cráter exige delimitar el objeto. La delimitación no es neutra: un umbral distinto cambia el área.
- 🔗 **Se estudia junto con:** segmentación, umbralización, método de Otsu, varianza entre clases.

📘 **Dónde se aprende** (2 clases): [B15-C13 · Segmentación de imágenes](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md); [B17-C11 · Redes de segmentación semántica de imágenes](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md).

### Coeficiente de dilatación

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B43-C11](../programa/clases/B43/B43-C11-dilatacion-termica-y-estabilidad/CLASE.md):**
- **Idea central (modelo mental):** Como un helado que se derrite desde la superficie: la capa externa cambia de inmediato y el centro tarda; cuanto más grueso, más lento, con el aire como aislante.
- 🎯 **Por qué importa:** La estabilidad térmica fija cuándo se puede observar y cada cuánto hay que reenfocar. La decisión central: ¿cuánto se mueve el foco por kelvin, cómo se compensa y cuánto tarda el espejo en igualarse al aire?
- 🔗 **Se estudia junto con:** deriva de foco, compensación, número de Biot, constante de tiempo.

📘 **Dónde se aprende** (1 clase): [B43-C11 · Dilatación térmica y estabilidad](../programa/clases/B43/B43-C11-dilatacion-termica-y-estabilidad/CLASE.md).

### Coeficiente de Einstein A

- El coeficiente de Einstein A es la tasa de emisión espontánea (s⁻¹).

💡 **Contexto en la clase [B62-C04](../programa/clases/B62/B62-C04-momentos-dipolares-y-fuerza-de-linea/CLASE.md):**
- **Idea central (modelo mental):** Una molécula con dipolo oscilante es una antena microscópica: irradia más cuanto mayor es la amplitud (`μ²`) y la frecuencia (`ν³`). Límite: la antena clásica no distingue orientaciones; en el modelo cuántico, `S` y la degeneración las cuentan.
- 🎯 **Por qué importa:** Una frecuencia identifica la especie, pero solo la intensidad dice cuánta hay. Y la intensidad contiene `μ²`: un error del 10 % en el dipolo es un 20 % en la cantidad de moléculas.
- 🔗 **Se estudia junto con:** momento dipolar permanente, fuerza de línea, intensidad integrada, vida radiativa.

📘 **Dónde se aprende** (1 clase): [B62-C04 · Momentos dipolares y fuerza de línea](../programa/clases/B62/B62-C04-momentos-dipolares-y-fuerza-de-linea/CLASE.md).

### Coeficiente de empuje

- El coeficiente de empuje es `C_F = F/(p₀ A_t)`.

💡 **Cómo se explica en la clase [B79-C08](../programa/clases/B79/B79-C08-flujo-en-toberas-convergente-divergentes/CLASE.md):**
- *Descripción textual:* la cámara fija el flujo bloqueado; la relación de áreas fija la salida; la salida y la presión ambiente fijan el empuje; dos vías comprueban velocidad, flujo y coeficiente de empuje.
- Calcular el empuje, el coeficiente de empuje y el impulso específico.
- 🎯 **Por qué importa:** B78-C03 trata la cámara pero no el flujo por la tobera. La teoría de expansión es lo que une la presión de cámara con el empuje.
- 🔗 **Se estudia junto con:** bloqueada, relación de expansión, empuje, tobera adaptada.

📘 **Dónde se aprende** (1 clase): [B79-C08 · Flujo en toberas convergente-divergentes](../programa/clases/B79/B79-C08-flujo-en-toberas-convergente-divergentes/CLASE.md).

### Coeficiente de Ledoux

- El coeficiente de Ledoux `C_nl` corrige por la fuerza de Coriolis; para modos g de dipolo vale `1/(l(l+1)) = 1/2`.

💡 **Contexto en la clase [B37-C11](../programa/clases/B37/B37-C11-rotacion-interna-a-partir-del-desdoblamiento-de-frecuencias/CLASE.md):**
- **Idea central (modelo mental):** Es como medir la velocidad de dos discos que giran a distinto ritmo con una luz que ilumina más uno u otro: cada modo es una luz distinta, y combinando varias se separan las dos velocidades.
- 🎯 **Por qué importa:** El desdoblamiento promedia la rotación de las regiones que el modo explora. La decisión central: ¿cuánto giran el núcleo y la envoltura y con qué incertidumbre y correlación?
- 🔗 **Se estudia junto con:** desdoblamiento rotacional, fracción de inercia, rotación diferencial, cuerpo rígido.

📘 **Dónde se aprende** (1 clase): [B37-C11 · Rotación interna a partir del desdoblamiento de frecuencias](../programa/clases/B37/B37-C11-rotacion-interna-a-partir-del-desdoblamiento-de-frecuencias/CLASE.md).

### Coeficiente de par K

- Precarga: fuerza de tracción que el apriete deja en el perno. Coeficiente de par `K`: relaciona par y precarga e incluye la fricción.

💡 **Contexto en la clase [B90-C06](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md):**
- 🎯 **Por qué importa:** Un perno mal apretado se afloja con la vibración o se rompe por exceso de carga; un centro de masa fuera de rango desvía la nave en el despliegue. La decisión central: ¿qué par de apriete garantiza que la unión no se separe ni se plastifique, y el conjunto queda dentro de los límites de masa?
- 🔗 **Se estudia junto con:** Precarga, Factor de carga φ, Margen de separación, Centro de masa (CG).

📘 **Dónde se aprende** (1 clase): [B90-C06 · Integración mecánica de subsistemas](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md).

### Coeficiente de reflectividad

- El coeficiente de reflectividad `Cr` va de `1` (absorbente) a `2` (espejo).

💡 **Contexto en la clase [B72-C08](../programa/clases/B72/B72-C08-presion-de-radiacion-solar/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR L["L, UA"] --> S["S = L/(4 pi UA^2)"] S --> P["P = S/c"] P --> A["a = Cr (A/m) P"] A --> E["de/dt = 1.5 a / (n a)"] U["sombra cilindrica"] --> A ``` *Descripción textual:* la luminosidad y la distancia dan la irradiancia, de ella la presión y la aceleración; esta fuerza la excentricidad, y la sombra interrumpe el empuje.
- 🎯 **Por qué importa:** En órbita geoestacionaria no hay arrastre, y el empuje solar domina las maniobras de mantenimiento de un satélite con paneles grandes; en una vela solar es el propulsor. La decisión central: ¿cuánto vale la aceleración por presión de radiación y cuánto deforma una órbita alta en semanas?
- 🔗 **Se estudia junto con:** irradiancia, presión de radiación, sombra cilíndrica, excentricidad forzada.

📘 **Dónde se aprende** (1 clase): [B72-C08 · Presión de radiación solar](../programa/clases/B72/B72-C08-presion-de-radiacion-solar/CLASE.md).

### Coeficiente de reflexión

- El coeficiente de reflexión `R` es la razón de amplitudes.
- El coeficiente de reflexión es `(√ε₁ − √ε₂)/(√ε₁ + √ε₂)`.
- El coeficiente de reflexión `Γ = (R − Z0)/(R + Z0)` mide la fracción de onda que vuelve.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B53-C30](../programa/clases/B53/B53-C30-radar-de-penetracion-subsuperficial-en-cuerpos-planetarios/CLASE.md):**
- Entre regolito de `ε₁ = 3,0` y roca de `ε₂ = 7,0` (ilustrativas) el coeficiente de reflexión es `-0,209` (`-13,6 dB` en potencia).
- Calcular el coeficiente de reflexión entre dos capas.
- 🎯 **Por qué importa:** Sin conocer la velocidad, un retardo no da profundidad. La decisión central: ¿se puede estimar la velocidad del medio con los propios datos y qué error de profundidad produce suponerla mal?
- 🔗 **Se estudia junto con:** hipérbola de difracción, linealización.

📘 **Dónde se aprende** (4 clases): [B35-C10 · Condiciones de frontera en modelos MHD](../programa/clases/B35/B35-C10-condiciones-de-frontera-en-modelos-mhd/CLASE.md); [B49-C02 · Adaptación de impedancias y líneas de transmisión en antenas](../programa/clases/B49/B49-C02-adaptacion-de-impedancias-y-lineas-de-transmision-en-antenas/CLASE.md); [B53-C30 · Radar de penetración subsuperficial en cuerpos planetarios](../programa/clases/B53/B53-C30-radar-de-penetracion-subsuperficial-en-cuerpos-planetarios/CLASE.md); [B93-C03 · Integridad de señal en electrónica embarcada](../programa/clases/B93/B93-C03-integridad-de-senal-en-electronica-embarcada/CLASE.md).

### Coeficiente de sensibilidad

- Un coeficiente de sensibilidad `c_i = ∂f/∂x_i` mide cuánto cambia el resultado por cambio unitario de la entrada `i`.

💡 **Cómo se explica en la clase [B13-C13](../programa/clases/B13/B13-C13-presupuestos-de-incertidumbre/CLASE.md):**
- ⚠️ **Error frecuente:** Olvidar el coeficiente de sensibilidad. Se corrige con los ejercicios 2 y 6.
- 🎯 **Por qué importa:** Un telémetro láser mide la distancia a un reflector a unos 10 km. Una mejora costosa del cronómetro podría no servir si la mayor parte de la incertidumbre viene del retardo electrónico o del aire.
- 🔗 **Se estudia junto con:** mensurando, modelo de medida, incertidumbre combinada, contribución.

📘 **Dónde se aprende** (1 clase): [B13-C13 · Presupuestos de incertidumbre](../programa/clases/B13/B13-C13-presupuestos-de-incertidumbre/CLASE.md).

### Coeficiente de silueta

- El coeficiente de silueta de un punto, `s = (b − a)/max(a, b)`, vale cerca de 1 si el punto está bien dentro de su grupo, cerca de 0 si está entre dos y es negativo si probablemente está mal asignado (S1).

💡 **Cómo se explica en la clase [B17-C06](../programa/clases/B17/B17-C06-aprendizaje-no-supervisado/CLASE.md):**
- Para evaluar sin etiquetas propone el coeficiente de silueta, `s = (b − a)/max(a, b)`, donde `a` es la distancia media a los puntos del mismo grupo y `b` la distancia media al grupo más cercano (S1).
- Evaluar un agrupamiento sin etiquetas con la inercia y el coeficiente de silueta.
- 🎯 **Por qué importa:** Un catálogo trae miles de objetos medidos en varias bandas y nadie los ha clasificado. ¿Hay poblaciones distintas?
- 🔗 **Se estudia junto con:** aprendizaje no supervisado, componente principal, varianza explicada, agrupamiento.

📘 **Dónde se aprende** (1 clase): [B17-C06 · Aprendizaje no supervisado](../programa/clases/B17/B17-C06-aprendizaje-no-supervisado/CLASE.md).

### Coeficiente de uniformidad

- El coeficiente de uniformidad es `D60/D10`.

💡 **Cómo se explica en la clase [B59-C04](../programa/clases/B59/B59-C04-caracterizacion-de-regolito-lunar/CLASE.md):**
- Calcular `D90/D10` y el coeficiente de uniformidad.
- Ejercicio 4. Calcula el coeficiente de uniformidad `D60/D10` (8.2).
- 🎯 **Por qué importa:** Un tamiz, una tolva o un horno de sinterización se diseñan para una distribución de tamaños, no para un grano. La decisión central: ¿qué fracción de la masa es fina (menor de 20 µm) y cuánto cambia si hablo de número o de masa?
- 🔗 **Se estudia junto con:** desviación geométrica, diámetro de Sauter, superficie específica.

📘 **Dónde se aprende** (1 clase): [B59-C04 · Caracterización de regolito lunar](../programa/clases/B59/B59-C04-caracterizacion-de-regolito-lunar/CLASE.md).

### Coeficiente estructural

- El coeficiente estructural `ε = m_est/(m_est + m_prop)` mide cuánta masa de la etapa no es propelente.
- El coeficiente estructural `e` es la masa de estructura sobre estructura más propelente.

💡 **Cómo se explica en la clase [B77-C01](../programa/clases/B77/B77-C01-sistemas-de-lanzamiento/CLASE.md):**
- Calcular la razón de carga útil de una etapa con el coeficiente estructural.
- 🎯 **Por qué importa:** Un requisito de velocidad no dice cuánto pesa el vehículo. La decisión central: ¿cómo se reparte la velocidad entre dos etapas para que la masa de despegue sea mínima, y qué parte de esa masa es carga útil?
- 🔗 **Se estudia junto con:** etapa, razón de carga útil, masa de despegue, relación empuje–peso.

📘 **Dónde se aprende** (2 clases): [B77-C01 · Sistemas de lanzamiento](../programa/clases/B77/B77-C01-sistemas-de-lanzamiento/CLASE.md); [B124-C23 · Costos de transporte por kilogramo a superficie](../programa/clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md).

### Coeficiente kappa de Cohen

- El coeficiente kappa de Cohen es `(p_o − p_e)/(1 − p_e)`, el acuerdo respecto del esperado por azar.

💡 **Contexto en la clase [B15-C22](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md):**
- **Idea central (modelo mental):** Para separar naranjas, limones y limas por color, miras dónde cae cada fruta en un gráfico de color. Si los tres grupos están lejos, cualquier regla funciona; si se solapan, algunas frutas quedan en tierra de nadie y cualquier regla se equivoca con ellas. Analogía: frutas en un gráfico de color.
- 🎯 **Por qué importa:** Un mapa de cobertura de suelo parece una verdad; en realidad es una predicción con un error que depende de las muestras elegidas y de cuánto se solapan las clases en el espacio espectral. Cifras como «90 % de exactitud» no significan nada sin decir con qué datos se midieron, ni cómo se reparte el error entre clases.
- 🔗 **Se estudia junto con:** vector espectral, NDVI, clase, muestras de entrenamiento.

📘 **Dónde se aprende** (1 clase): [B15-C22 · Clasificación supervisada de imágenes](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md).

### Coeficiente osmótico

- El coeficiente osmótico `φ` mide la desviación de la idealidad.

💡 **Cómo se explica en la clase [B64-C04](../programa/clases/B64/B64-C04-halofilos-y-vida-en-salmueras/CLASE.md):**
- *Descripción textual:* la sal y su coeficiente osmótico fijan la actividad del agua; de ella salen la presión osmótica y la condición de equilibrio que la célula cumple con KCl o con solutos compatibles.
- Por coeficiente osmótico: corrige la idealidad.
- 🎯 **Por qué importa:** En una salmuera concentrada el agua existe pero «no está disponible» del mismo modo. La pregunta motivadora: ¿cuánta sal puede haber en el exterior antes de que el agua deje de bastar para la célula?
- 🔗 **Se estudia junto con:** actividad del agua, molalidad, presión osmótica, «salt-in».

📘 **Dónde se aprende** (1 clase): [B64-C04 · Halófilos y vida en salmueras](../programa/clases/B64/B64-C04-halofilos-y-vida-en-salmueras/CLASE.md).

### Coeficiente radiativo

- El coeficiente radiativo `h_r = 4εσT³` linealiza la radiación para `ΔT` pequeño.

💡 **Cómo se explica en la clase [B85-C03](../programa/clases/B85/B85-C03-conveccion-y-ausencia-de-conveccion-exterior/CLASE.md):**
- Calcular el coeficiente radiativo `h_r = 4εσT³` y compararlo con el convectivo.
- 🎯 **Por qué importa:** Un equipo que se enfría bien sobre la mesa puede sobrecalentarse en vacío y en microgravedad. La decisión central: ¿cuánto del enfriamiento de un equipo se pierde al quitar la convección y qué queda para sustituirla?
- 🔗 **Se estudia junto con:** número de Rayleigh, número de Nusselt, camino libre medio, convección natural.

📘 **Dónde se aprende** (1 clase): [B85-C03 · Convección y ausencia de convección exterior](../programa/clases/B85/B85-C03-conveccion-y-ausencia-de-conveccion-exterior/CLASE.md).

### Coeficiente térmico de la focal

- El coeficiente térmico de la focal es `α_f = α_g − (dn/dT)/(n − 1)`.

💡 **Contexto en la clase [B50-C12](../programa/clases/B50/B50-C12-sensibilidad-termica-del-desempeno-optico-y-atermalizacion/CLASE.md):**
- **Idea central (modelo mental):** Como un puente con vigas de materiales distintos: si una crece más que otra, el conjunto se curva; se elige el material para que crezcan igual.
- 🎯 **Por qué importa:** Un telescopio que se enfría de noche se desenfoca si sus materiales se dilatan distinto. La decisión central: ¿qué dilatación debe tener la estructura para que el foco no se mueva?
- 🔗 **Se estudia junto con:** carcasa atérmica, defocus, profundidad de foco, tubo.

📘 **Dónde se aprende** (1 clase): [B50-C12 · Sensibilidad térmica del desempeño óptico y atermalización](../programa/clases/B50/B50-C12-sensibilidad-termica-del-desempeno-optico-y-atermalizacion/CLASE.md).

### Coeficiente W040

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B41-C13](../programa/clases/B41/B41-C13-aberracion-esferica-y-coma/CLASE.md):**
- **Idea central (modelo mental):** Como un cometa: la estrella fuera del eje se convierte en una cola; la cabeza es el rayo central y la cola crece con la distancia al eje y con la luminosidad del espejo.
- 🎯 **Por qué importa:** Dos defectos limitan el campo y la relación focal. La decisión central: ¿hasta qué f/ sirve una esfera y qué campo tolera un paraboloide?
- 🔗 **Se estudia junto con:** aberración esférica, diferencia de camino óptico, coma, abanico tangencial.

📘 **Dónde se aprende** (1 clase): [B41-C13 · Aberración esférica y coma](../programa/clases/B41/B41-C13-aberracion-esferica-y-coma/CLASE.md).

### Coeficientes

- Los números `aₖ` son los coeficientes;
- Un filtro FIR (respuesta finita al impulso) calcula `y[n] = Σ_{m=0}^{M−1} h[m] x[n − m]`; la lista `h[m]` son los coeficientes.

💡 **Cómo se explica en la clase [B04-C01](../programa/clases/B04/B04-C01-polinomios-y-factorizacion/CLASE.md):**
- En `p(x) = 3x² − x + 5`, el grado es 2; los coeficientes son `a₂ = 3`, `a₁ = −1`, `a₀ = 5`.
- Con coeficientes de tamaños muy distintos, como los de la oblicuidad (de 10⁴ a 10⁻⁸), esto reduce los errores de redondeo.
- 🎯 **Por qué importa:** Cuando un observatorio publica dónde está inclinado el eje de la Tierra, no da un solo número: da una *fórmula* para cada fecha, porque ese eje se mueve lentamente. Esa fórmula es un polinomio.
- 🔗 **Se estudia junto con:** polinomio, término independiente, grado, raíz.

📘 **Dónde se aprende** (2 clases): [B04-C01 · Polinomios y factorización](../programa/clases/B04/B04-C01-polinomios-y-factorizacion/CLASE.md); [B15-C07 · Filtrado digital](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md).

### Coeficientes de Lagrange

- Los coeficientes de Lagrange `f` y `g` dan `v1 = (r2 − f r1)/g`.

💡 **Cómo se explica en la clase [B82-C01](../programa/clases/B82/B82-C01-lambert-de-arco-corto/CLASE.md):**
- Obtener `v1` con los coeficientes de Lagrange `f` y `g`.
- 🎯 **Por qué importa:** Un diseñador de trayectorias conoce dónde está la nave y dónde debe estar, y cuánto tiempo tiene; no conoce la velocidad con que debe salir. La decisión central: ¿qué semieje y qué velocidad inicial hacen que la nave pase por `r2` exactamente a los `t` días?
- 🔗 **Se estudia junto con:** cuerda, semiperímetro, teorema de Lambert, tiempo de mínima energía.

📘 **Dónde se aprende** (1 clase): [B82-C01 · Lambert de arco corto](../programa/clases/B82/B82-C01-lambert-de-arco-corto/CLASE.md).

### Coeficientes de Laplace

- Los coeficientes de Laplace son `b_s^{(j)}(α) = (1/π)∫₀^{2π} cos(jψ)(1 − 2α cos ψ + α²)^{−s} dψ`.

💡 **Cómo se explica en la clase [B73-C11](../programa/clases/B73/B73-C11-resonancias-seculares/CLASE.md):**
- D["GM, a, e de dos planetas"] --> B["coeficientes de Laplace b1, b2"]
- *Descripción textual:* los datos dan los coeficientes de Laplace, éstos las matrices, y de ellas salen las frecuencias propias, la evolución de `e` y la posición de las resonancias seculares.
- 🎯 **Por qué importa:** La excentricidad de una órbita varía durante millones de años por la atracción promediada de los demás planetas, y esa variación se vuelve violenta cuando una frecuencia propia coincide con la de precesión de un asteroide.
- 🔗 **Se estudia junto con:** teoría de Laplace–Lagrange, frecuencias propias, resonancia secular.

📘 **Dónde se aprende** (1 clase): [B73-C11 · Resonancias seculares](../programa/clases/B73/B73-C11-resonancias-seculares/CLASE.md).

### Coeficientes de sensibilidad

- Los coeficientes de sensibilidad son las derivadas parciales `cᵢ = ∂f/∂xᵢ` evaluadas en las estimaciones; describen cómo varía la salida con cada entrada (S1, 5.1.3).

💡 **Cómo se explica en la clase [B12-C16](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md):**
- La ley de propagación del GUM es rápida, analítica y da los coeficientes de sensibilidad, que explican qué entrada domina; falla con no linealidad fuerte o salidas no gaussianas.
- Calcular coeficientes de sensibilidad y la incertidumbre combinada con la ley de propagación.
- 🎯 **Por qué importa:** Casi todo resultado en ciencias espaciales es una función de medidas: una velocidad a partir de un radio, una distancia a partir de una paralaje, una masa a partir de un período. Dar el valor sin su incertidumbre no permite comparar con otros resultados ni decidir si cumple un requisito.
- 🔗 **Se estudia junto con:** modelo de medida, incertidumbre típica, ley de propagación de la incertidumbre, incertidumbre combinada.

📘 **Dónde se aprende** (1 clase): [B12-C16 · Propagación de incertidumbre](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md).

### Coeficientes estequiométricos

- Los coeficientes estequiométricos son los números que multiplican cada fórmula para que la ecuación quede balanceada.

💡 **Contexto en la clase [B06-C08](../programa/clases/B06/B06-C08-reacciones-y-conservacion-de-masa/CLASE.md):**
- **Idea central (modelo mental):** Piensa en piezas de construcción: con las mismas piezas de una torre puedes armar un puente. No hay piezas nuevas ni se pierden. En una reacción química, las piezas son los átomos.
- 🎯 **Por qué importa:** Una vela y el Sol liberan energía, pero lo hacen de maneras radicalmente distintas. En la vela, los átomos de carbono e hidrógeno se reordenan con el oxígeno y todos siguen ahí al terminar.
- 🔗 **Se estudia junto con:** reacción química, reactivos, productos, ecuación química.

📘 **Dónde se aprende** (1 clase): [B06-C08 · Reacciones y conservación de masa](../programa/clases/B06/B06-C08-reacciones-y-conservacion-de-masa/CLASE.md).

### Coffin–Manson

- Factor de aceleración (AF): ciclos de servicio por ciclo de ensayo. Coffin–Manson: relación de ley de potencias entre amplitud térmica y vida.

💡 **Contexto en la clase [B90-C12](../programa/clases/B90/B90-C12-vacio-termico-y-ciclos/CLASE.md):**
- 🎯 **Por qué importa:** Una nave en órbita baja sufre unos 16 ciclos térmicos por día; no se pueden repetir 5 840 ciclos en tierra. La decisión central: ¿cuántos ciclos de ensayo con mayor amplitud representan un año de órbita y cuánto tarda la campaña?
- 🔗 **Se estudia junto con:** Vacío térmico (TVAC), Bakeout, Ciclado, Presión límite.

📘 **Dónde se aprende** (1 clase): [B90-C12 · Vacío térmico y ciclos](../programa/clases/B90/B90-C12-vacio-termico-y-ciclos/CLASE.md).

### Coherencia

- La coherencia es la fase definida entre los dos caminos.
- La coherencia mide cuánto se parecen las dos imágenes en señal; si es baja, la fase es ruidosa.
- La coherencia es la ausencia de contradicciones entre campos.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B28-C20](../programa/clases/B28/B28-C20-caso-de-estudio-de-evento-combinado/CLASE.md):**
- PUB --> COH["comprobaciones de coherencia"]
- *Descripción textual:* los resúmenes dan cifras publicadas; se comprueba su coherencia y se calculan magnitudes derivadas; el dossier incluye la lista de lo no consultado y se firma con una huella.
- 🎯 **Por qué importa:** Un caso de estudio sirve si es verificable: cada cifra debe llevar su fuente, y lo calculado debe distinguirse de lo publicado. La decisión central: ¿qué cifras del evento están respaldadas por lo consultado, cuáles se derivan y cuáles quedan fuera?
- 🔗 **Se estudia junto con:** dossier, cifra publicada, cifra derivada, cifra excluida.

📘 **Dónde se aprende** (5 clases): [B28-C20 · Caso de estudio de evento combinado](../programa/clases/B28/B28-C20-caso-de-estudio-de-evento-combinado/CLASE.md); [B31-C01 · Dualidad onda-partícula](../programa/clases/B31/B31-C01-dualidad-onda-particula/CLASE.md); [B57-C08 · Interferometría radar InSAR](../programa/clases/B57/B57-C08-interferometria-radar-insar/CLASE.md); [B69-C05 · Coherencia interferométrica y decorrelación](../programa/clases/B69/B69-C05-coherencia-interferometrica-y-decorrelacion/CLASE.md); [B120-C04 · Documentación regulatoria de un sistema satelital](../programa/clases/B120/B120-C04-documentacion-regulatoria-de-un-sistema-satelital/CLASE.md).

### Coherencia temporal

- La coherencia temporal: relación entre fases en instantes distintos.

💡 **Cómo se explica en la clase [B42-C03](../programa/clases/B42/B42-C03-interferencia-y-coherencia/CLASE.md):**
- Reconocer el límite de la coherencia temporal frente a la espacial.
- 🎯 **Por qué importa:** Sin coherencia no hay franjas: una fuente ancha en frecuencia o en tamaño borra la interferencia. La decisión central: ¿hasta qué diferencia de camino se ven franjas con una fuente de ancho espectral dado?
- 🔗 **Se estudia junto con:** visibilidad, diferencia de camino, longitud de coherencia, espectro.

📘 **Dónde se aprende** (1 clase): [B42-C03 · Interferencia y coherencia](../programa/clases/B42/B42-C03-interferencia-y-coherencia/CLASE.md).

### Coherente

- Una unidad es coherente si su factor numérico de equivalencia con las base es 1.

💡 **Cómo se explica en la clase [B03-C06](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md):**
- Para saber si una unidad es coherente basta con reconstruirla desde las base.
- C -->|Sí| OK["Coherente: se puede calcular"]
- 🎯 **Por qué importa:** El 23 de septiembre de 1999 la NASA perdió contacto con la sonda Mars Climate Orbiter. Según la agencia, un error de navegación se debió a no traducir unidades inglesas a métricas: el programa en tierra usaba unas y el de la nave otras, y la sonda pasó demasiado cerca de Marte y se quemó en su atmósfera (S1).
- 🔗 **Se estudia junto con:** magnitud, unidad, SI, unidades base.

📘 **Dónde se aprende** (1 clase): [B03-C06 · Unidades del Sistema Internacional](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md).

### Cohesión

- La cohesión `c` es la resistencia al corte sin carga y `φ` el ángulo de fricción.

💡 **Cómo se explica en la clase [B97-C06](../programa/clases/B97/B97-C06-control-de-movilidad-sobre-regolito/CLASE.md):**
- Analogía: caminar sobre arena seca y sobre arena húmeda; la húmeda tiene cohesión y la seca solo fricción.
- Descripción larga: la tracción relativa al peso crece al bajar la gravedad porque la cohesión aporta una fuerza fija; la pendiente máxima aproximada crece también.
- 🎯 **Por qué importa:** Un rover que se atasca puede perder la misión. Estimar cuánta tracción hay disponible en cada gravedad, y cómo varía con el deslizamiento, permite limitar pendientes y planear rutas.
- 🔗 **Se estudia junto con:** empuje, tracción neta, deslizamiento, ángulo de fricción.

📘 **Dónde se aprende** (1 clase): [B97-C06 · Control de movilidad sobre regolito](../programa/clases/B97/B97-C06-control-de-movilidad-sobre-regolito/CLASE.md).

### Cohete térmico

- El cohete térmico calienta un propelente con una fuente externa al propelente.

💡 **Cómo se explica en la clase [B78-C14](../programa/clases/B78/B78-C14-propulsion-nuclear-termica-conceptual/CLASE.md):**
- A igual Δv, el cohete térmico necesita menos propelente.
- Ejercicio 3 · guiado (casi autónomo). ¿Por qué no se usa metano en un cohete térmico?
- 🎯 **Por qué importa:** Un cohete químico limita su `Isp` por la química del propelente; uno térmico lo limita por la temperatura que aguanta el núcleo. La decisión central: ¿cuánto `Isp` puede dar un gas de baja masa molar calentado a una temperatura dada y qué empuje corresponde a una potencia térmica?
- 🔗 **Se estudia junto con:** núcleo, masa molar baja, temperatura del núcleo, empuje por potencia térmica.

📘 **Dónde se aprende** (1 clase): [B78-C14 · Propulsión nuclear térmica conceptual](../programa/clases/B78/B78-C14-propulsion-nuclear-termica-conceptual/CLASE.md).

### Coincidencia

- La coincidencia es un impacto en el mismo píxel de dos cuadros.
- La coincidencia exige tiempo y posición compatibles.

💡 **Cómo se explica en la clase [B28-C11](../programa/clases/B28/B28-C11-coincidencias-entre-observatorios/CLASE.md):**
- Con `P = 2,38 × 10⁻⁸` y `M` eventos por año, las coincidencias fortuitas esperadas por año son `2,38 × 10⁻⁸` (`M = 1`), `2,38 × 10⁻⁷` (`10`) y `2,38 × 10⁻⁶` (`100`).
- La detección de GRB 170817A llegó `1,74 ± 0,05 s` después de GW170817, y la colaboración estimó una probabilidad de coincidencia fortuita de `5 × 10⁻⁸` (S2, resumen);
- 🎯 **Por qué importa:** Que dos señales coincidan no prueba que estén relacionadas: la pregunta es cuán probable es la coincidencia por azar. Una probabilidad fortuita muy baja es lo que convierte una coincidencia en un descubrimiento.
- 🔗 **Se estudia junto con:** probabilidad fortuita, ventana, tasa, fracción del cielo.

📘 **Dónde se aprende** (2 clases): [B28-C11 · Coincidencias entre observatorios](../programa/clases/B28/B28-C11-coincidencias-entre-observatorios/CLASE.md); [B44-C16 · Ruido cósmico e identificación](../programa/clases/B44/B44-C16-ruido-cosmico-e-identificacion/CLASE.md).

### Cola de atención

- La cola de atención es el orden de respuesta.

💡 **Cómo se explica en la clase [B122-C07](../programa/clases/B122/B122-C07-clasificacion-de-severidad-e-impacto-de-incidentes-espaciales/CLASE.md):**
- Cola de atencion (nivel, puntaje, antiguedad): ['I-07', 'I-04', 'I-01', 'I-08', 'I-03', 'I-06', 'I-02', 'I-05']
- 🎯 **Por qué importa:** B58-C10 clasifica solo impactos de asteroides. La decisión central: ¿en qué orden se atienden los incidentes y qué regla fuerza la escalada?
- 🔗 **Se estudia junto con:** severidad, puntaje, nivel, escalada.

📘 **Dónde se aprende** (1 clase): [B122-C07 · Clasificación de severidad e impacto de incidentes espaciales](../programa/clases/B122/B122-C07-clasificacion-de-severidad-e-impacto-de-incidentes-espaciales/CLASE.md).

### Cola de eventos

- Evento: hecho en un instante. Cola de eventos: lista ordenada por tiempo.

💡 **Cómo se explica en la clase [B96-C20](../programa/clases/B96/B96-C20-simulacion-de-jornada-de-control-de-mision/CLASE.md):**
- Una cola de prioridad (`heapq`) ordena eventos AOS, LOS, ANOMALIA y FIN.
- E["Cola de eventos"] --> A["AOS: comandos"]
- 🎯 **Por qué importa:** Un ensayo en frío revela conflictos entre contactos, comandos y datos que no se ven sumando números aislados. La decisión central: ¿la jornada funciona de punta a punta y cuándo se detecta una anomalía?
- 🔗 **Se estudia junto con:** Evento, Buffer, Invariante, Latencia de detección.

📘 **Dónde se aprende** (1 clase): [B96-C20 · Simulación de jornada de control de misión](../programa/clases/B96/B96-C20-simulacion-de-jornada-de-control-de-mision/CLASE.md).

### Cola de iones

- La cola de polvo es el polvo empujado por la radiación; la cola de iones, el gas ionizado arrastrado por el viento solar (no se calcula aquí).

💡 **Cómo se explica en la clase [B58-C04](../programa/clases/B58/B58-C04-nucleos-y-colas-cometarias/CLASE.md):**
- Separar núcleo, coma, cola de polvo y cola de iones.
- Límites: sin conducción, rotación, mezcla de volátiles ni cola de iones; un solo elemento subsolar.
- ⚠️ **Error frecuente:** Confundir cola de polvo y de iones. Se corrige con la sección 6.
- 🎯 **Por qué importa:** La actividad de un cometa cambia su órbita (empujes no gravitacionales) y su brillo, y decide qué se observa. La decisión central: ¿a qué distancia del Sol el hielo empieza a sublimar de forma apreciable y qué tamaño de grano barre la radiación?
- 🔗 **Se estudia junto con:** sublimación, coma, cola de polvo, fuerza no gravitacional.

📘 **Dónde se aprende** (1 clase): [B58-C04 · Núcleos y colas cometarias](../programa/clases/B58/B58-C04-nucleos-y-colas-cometarias/CLASE.md).

### Cola de marea

- Una cola de marea es un chorro de estrellas arrancado por la marea.

💡 **Cómo se explica en la clase [B25-C12](../programa/clases/B25/B25-C12-interacciones-y-fusiones-galacticas/CLASE.md):**
- Definir interacción, fusión, marea, cola de marea y encuentro parabólico.
- Menos perdidas y menos cola: la marea disminuye con la distancia.
- 🎯 **Por qué importa:** Las galaxias no evolucionan aisladas: se atraen, se deforman y a veces se funden. Muchas elípticas masivas pueden provenir de fusiones, y los encuentros llevan gas al centro, alimentando la formación estelar y los núcleos activos de C11.
- 🔗 **Se estudia junto con:** interacción, fusión, fuerza de marea, órbita parabólica.

📘 **Dónde se aprende** (1 clase): [B25-C12 · Interacciones y fusiones galácticas](../programa/clases/B25/B25-C12-interacciones-y-fusiones-galacticas/CLASE.md).

### Cola de polvo

- La cola de polvo es el polvo empujado por la radiación; la cola de iones, el gas ionizado arrastrado por el viento solar (no se calcula aquí).

💡 **Cómo se explica en la clase [B58-C04](../programa/clases/B58/B58-C04-nucleos-y-colas-cometarias/CLASE.md):**
- Separar núcleo, coma, cola de polvo y cola de iones.
- ⚠️ **Error frecuente:** Confundir cola de polvo y de iones. Se corrige con la sección 6.
- 🎯 **Por qué importa:** La actividad de un cometa cambia su órbita (empujes no gravitacionales) y su brillo, y decide qué se observa. La decisión central: ¿a qué distancia del Sol el hielo empieza a sublimar de forma apreciable y qué tamaño de grano barre la radiación?
- 🔗 **Se estudia junto con:** sublimación, coma, cola de iones, fuerza no gravitacional.

📘 **Dónde se aprende** (1 clase): [B58-C04 · Núcleos y colas cometarias](../programa/clases/B58/B58-C04-nucleos-y-colas-cometarias/CLASE.md).

### Cola de potencias

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B33-C04](../programa/clases/B33/B33-C04-escalas-de-severidad-de-clima-espacial/CLASE.md):**
- *Descripción textual:* los umbrales definen niveles; la cola de potencias da conteos esperados que el Monte Carlo verifica.
- Límite: valores independientes con cola de potencias.
- 🎯 **Por qué importa:** Comparar severidades exige conocer cómo se definió cada nivel. La decisión central: ¿cuántos eventos caen en cada nivel y por qué no son comparables entre escalas?
- 🔗 **Se estudia junto con:** escala, nivel, razón, conteos esperados.

📘 **Dónde se aprende** (1 clase): [B33-C04 · Escalas de severidad de clima espacial](../programa/clases/B33/B33-C04-escalas-de-severidad-de-clima-espacial/CLASE.md).

### Cola larga

- Una cola larga es una distribución con valores extremos mucho más grandes que su centro.

💡 **Contexto en la clase [B59-C02](../programa/clases/B59/B59-C02-prospeccion-de-hielo-lunar/CLASE.md):**
- **Idea central (modelo mental):** Como estimar cuánta harina cae de una nube que solo ves de lejos: la báscula mide lo que cae en un plato, y el resto es extrapolación. Límite: aquí no hay un plato; el agua se infiere por su luz.
- 🎯 **Por qué importa:** Un recurso no se planifica con un valor central sino con un rango. La decisión central: ¿cuánto regolito hay que procesar si la abundancia es 2,7 % en vez de 5,6 %?
- 🔗 **Se estudia junto con:** abundancia, masa proyectada, propagación de primer orden, zonas de sombra permanente.

📘 **Dónde se aprende** (1 clase): [B59-C02 · Prospección de hielo lunar](../programa/clases/B59/B59-C02-prospeccion-de-hielo-lunar/CLASE.md).

### Cola M/D/1

- Cola M/D/1: llegadas de Poisson, servicio determinista, un servidor.

💡 **Cómo se explica en la clase [B48-C16](../programa/clases/B48/B48-C16-procesamiento-de-datos-en-linea/CLASE.md):**
- En un programa real los cuadros llegan a cadencia fija (cola D/D/1, sin espera si `D` es menor que la cadencia): el modelo de Poisson sobreestima la espera y sirve para ráfagas, no para el régimen estable.
- *Descripción textual:* la ocupación determina la espera de la cola: pequeña con carga baja, divergente cerca de uno; la recursión de Lindley la verifica.
- ⚠️ **Error frecuente:** Confundir espera en cola con tiempo total. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** Si la reducción no sigue el ritmo, se acumulan cuadros y el resultado llega tarde. La decisión central: ¿hasta qué ocupación del procesador es tolerable la espera?
- 🔗 **Se estudia junto con:** Ocupación, Espera en cola, Recursión de Lindley, Tasa de datos.

📘 **Dónde se aprende** (1 clase): [B48-C16 · Procesamiento de datos en línea](../programa/clases/B48/B48-C16-procesamiento-de-datos-en-linea/CLASE.md).

### Cola pesada

- La cola pesada es la dependencia del total respecto de pocos casos.

💡 **Cómo se explica en la clase [B126-C02](../programa/clases/B126/B126-C02-capital-de-riesgo-en-empresas-espaciales/CLASE.md):**
- Cola pesada: pocos casos de 20x y 100x suben la media; la mayoría de las carteras no los tiene.
- ⚠️ **Error frecuente:** Mirar solo la media de una distribución de cola pesada. Se corrige con 8.4.
- 🎯 **Por qué importa:** El capital de riesgo tiene lógica y condiciones propias que el catálogo no trata. La decisión central: ¿cuánto recibe cada parte en una salida según las condiciones pactadas, y qué retorno cabe esperar de una cartera cuando casi todo el valor viene de pocos casos?
- 🔗 **Se estudia junto con:** preferencia de liquidación, Sin participación, Con participación, salida.

📘 **Dónde se aprende** (1 clase): [B126-C02 · Capital de riesgo en empresas espaciales](../programa/clases/B126/B126-C02-capital-de-riesgo-en-empresas-espaciales/CLASE.md).

### Cola radiactiva

- La cola radiactiva es la caída tardía al ritmo del cobalto.

💡 **Contexto en la clase [B27-C14](../programa/clases/B27/B27-C14-supernovas-termonucleares/CLASE.md):**
- **Idea central (modelo mental):** El níquel se agota rápido y alimenta al cobalto, que se agota despacio. La luz al principio la domina el níquel y después el cobalto, que fija la pendiente final.
- 🎯 **Por qué importa:** La luminosidad tardía de estas supernovas sigue la semivida del cobalto-56, y por eso se usan para medir distancias. La decisión central: ¿cuántos núcleos de cada especie quedan en cada instante y qué luminosidad producen?
- 🔗 **Se estudia junto con:** cadena de Bateman, semivida, vida media, constante de desintegración.

📘 **Dónde se aprende** (1 clase): [B27-C14 · Supernovas termonucleares](../programa/clases/B27/B27-C14-supernovas-termonucleares/CLASE.md).

### Colada

- La colada es un flujo de lava sobre una superficie.

💡 **Cómo se explica en la clase [B70-C07](../programa/clases/B70/B70-C07-flujos-de-lava-y-depositos-piroclasticos/CLASE.md):**
- Si `h ≤ h_c` la colada se detiene (`q = 0`); si no, `q = (G h³/(3η))(1 − 1,5ξ + 0,5ξ³)` con `ξ = h_c/h`.
- La gravedad sola no alarga la colada; en la literatura [S4] el efecto depende de caudales mayores, que este modelo no incluye.
- ⚠️ **Error frecuente:** Creer que menor gravedad alarga la colada. Se corrige en 8.3.
- 🎯 **Por qué importa:** La misma lava fluye distinto según la pendiente, el espesor y la reología; los piroclastos llegan más lejos si no hay aire. La decisión central: ¿cuánto fluye una colada y hasta dónde llegan los clastos en cada mundo?
- 🔗 **Se estudia junto con:** modelo de Bingham, espesor crítico, clasto balístico, depósito piroclástico.

📘 **Dónde se aprende** (1 clase): [B70-C07 · Flujos de lava y depósitos piroclásticos](../programa/clases/B70/B70-C07-flujos-de-lava-y-depositos-piroclasticos/CLASE.md).

### Colapso de tensión

- El colapso de tensión ocurre si la potencia pedida supera `V²/(4R)`.

💡 **Cómo se explica en la clase [B86-C07](../programa/clases/B86/B86-C07-distribucion-de-potencia/CLASE.md):**
- Colapso de tension: con R = 1.376 ohm (2.0 m, 0.05 mm2) a 28 V la potencia maxima de una carga de potencia constante es 142.4 W
- 🎯 **Por qué importa:** Un cable largo y fino desperdicia potencia y baja la tensión que ve el equipo; uno grueso pesa. La tensión del bus cambia la corriente, y por tanto las pérdidas, con el cuadrado.
- 🔗 **Se estudia junto con:** arnés, caída de tensión, carga de potencia constante, bus regulado.

📘 **Dónde se aprende** (1 clase): [B86-C07 · Distribución de potencia](../programa/clases/B86/B86-C07-distribucion-de-potencia/CLASE.md).

### Colapso del núcleo

- El colapso del núcleo es la caída del núcleo de hierro.

💡 **Cómo se explica en la clase [B27-C15](../programa/clases/B27/B27-C15-supernovas-de-colapso/CLASE.md):**
- El colapso del núcleo que la formó se modela aquí con un núcleo de `1,4 M☉` que pasa de `1500 km` a `12 km` (valores ilustrativos): libera `2,565 × 10⁴⁶ J`, el `10,25 %` de `Mc²`, y tarda `149,70 ms` en caída libre.
- 🎯 **Por qué importa:** El colapso libera cerca de un décimo de `Mc²`; casi todo sale en neutrinos y solo una milésima en la explosión visible. La decisión central: ¿cuánta energía libera el colapso, a qué fracción corresponde la explosión y cuánto tarda?
- 🔗 **Se estudia junto con:** energía de ligadura gravitatoria, tiempo de caída libre, energía cinética de la explosión, neutrinos.

📘 **Dónde se aprende** (1 clase): [B27-C15 · Supernovas de colapso](../programa/clases/B27/B27-C15-supernovas-de-colapso/CLASE.md).

### Colas

- Las colas son el regolito tratado.

💡 **Cómo se explica en la clase [B59-C23](../programa/clases/B59/B59-C23-subproductos-y-flujos-residuales-de-procesos-isru/CLASE.md):**
- Con `10 %` de ilmenita en masa (sintética) hay que procesar `9,482/0,10 = 94,8 kg` de regolito y quedan `85,3 kg` de colas por kg de O.
- La suma de residuos sólidos (Fe + TiO₂ + colas) es `93,8 kg`.
- ⚠️ **Error frecuente:** Contar solo el producto y olvidar las colas. Se corrige con 8.3.
- 🎯 **Por qué importa:** Producir un kilogramo de oxígeno genera toneladas de otras cosas. La decisión central: ¿qué masa de residuo o de subproducto aparece por cada kilogramo de producto?
- 🔗 **Se estudia junto con:** subproducto, flujo residual, ilmenita, reducción con hidrógeno.

📘 **Dónde se aprende** (1 clase): [B59-C23 · Subproductos y flujos residuales de procesos ISRU](../programa/clases/B59/B59-C23-subproductos-y-flujos-residuales-de-procesos-isru/CLASE.md).

### Colas pesadas

- Una distribución de colas pesadas tiene valores extremos mucho más frecuentes que la normal; en la de Cauchy no existen la media ni la varianza.

💡 **Cómo se explica en la clase [B12-C06](../programa/clases/B12/B12-C06-teorema-central-del-limite/CLASE.md):**
- En datos reales con colas muy pesadas (por ejemplo, mediciones con fallas ocasionales de gran amplitud), la media puede ser un mal resumen y debe sustituirse por la mediana o por un estimador robusto (C11).
- Para colas pesadas o `n` pequeño, hay que simular (C14) o recurrir a la distribución `t` (C08).
- 🎯 **Por qué importa:** Ningún instrumento tiene ruido exactamente normal, y sin embargo casi todas las incertidumbres se expresan con campanas. La razón es que se reportan promedios y sumas de muchas contribuciones pequeñas.
- 🔗 **Se estudia junto con:** teorema central del límite, Estandarizar, distancia de Kolmogorov–Smirnov, asimetría.

📘 **Dónde se aprende** (1 clase): [B12-C06 · Teorema central del límite](../programa/clases/B12/B12-C06-teorema-central-del-limite/CLASE.md).

### Colección

- Una colección describe un conjunto de datos.

💡 **Cómo se explica en la clase [B14-C25](../programa/clases/B14/B14-C25-catalogos-de-datos-geoespaciales-y-metadatos-stac/CLASE.md):**
- Distinguir catálogo, colección, ítem y activo.
- Ejercicio 8. ¿Qué diferencia hay entre catálogo y colección según S1?
- 🎯 **Por qué importa:** Un satélite produce miles de escenas al día. Para estudiar una inundación necesitas las que cubren una región, en unas fechas, con poca nube.
- 🔗 **Se estudia junto con:** ítem, catálogo, activo, caja envolvente.

📘 **Dónde se aprende** (1 clase): [B14-C25 · Catálogos de datos geoespaciales y metadatos (STAC)](../programa/clases/B14/B14-C25-catalogos-de-datos-geoespaciales-y-metadatos-stac/CLASE.md).

### Colección de placas

- Una colección de placas es un archivo de negativos de vidrio del cielo, como los más de 550 000 de Harvard (S2).

💡 **Cómo se explica en la clase [B02-C17](../programa/clases/B02/B02-C17-nacimiento-de-la-astrofotografia/CLASE.md):**
- La colección de placas del Observatorio de Harvard supera las 550 000 placas de vidrio, y el proyecto DASCH las digitalizó (finalizado en 2024) para estudiar el cielo en escalas de 100 años (S2).
- 🎯 **Por qué importa:** Un dibujo depende de quien lo hace; una placa registra lo que llegó. La pregunta motivadora es: ¿qué cambia cuando la observación puede guardarse, compararse años después y medirse?
- 🔗 **Se estudia junto con:** astrofotografía, daguerrotipo, placa seca de gelatina, exposición.

📘 **Dónde se aprende** (1 clase): [B02-C17 · Nacimiento de la astrofotografía](../programa/clases/B02/B02-C17-nacimiento-de-la-astrofotografia/CLASE.md).

### Colectiva

- Un mensaje punto a punto va de un proceso a otro; una operación colectiva involucra a todo el comunicador.

💡 **Cómo se explica en la clase [B18-C02](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md):**
- Para repartir y combinar datos, una colectiva es más corta, más legible y suele estar mejor optimizada que su equivalente con `send/recv`.
- La comunicación explícita es una ventaja para razonar y una carga para programar: la regla práctica es comunicar lo mínimo, en trozos grandes y con colectivas siempre que se pueda.
- ⚠️ **Error frecuente:** Una colectiva que no llaman todos los rangos. Se corrige revisando que no esté dentro de un `if rango == …`.
- 🎯 **Por qué importa:** Ocho, cuarenta o cuatro mil núcleos de un clúster no comparten memoria. Para que cada uno propague su parte de un catálogo de órbitas y luego se junten los resultados, hay que decir quién envía qué a quién, y cuándo.
- 🔗 **Se estudia junto con:** comunicador, tamaño, rango, SPMD.

📘 **Dónde se aprende** (1 clase): [B18-C02 · Paso de mensajes con MPI](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md).

### Colimación

- La colimación alinea primario, secundario y eje del portaocular.

💡 **Cómo se explica en la clase [B41-C19](../programa/clases/B41/B41-C19-colimacion-y-prueba-de-enfoque/CLASE.md):**
- La evidencia es la ficha de colimación y enfoque del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha de colimación y enfoque*.
- 🎯 **Por qué importa:** Un buen espejo mal colimado rinde mal. La decisión central: ¿cuánta descolimación y cuánto desenfoque se toleran?
- 🔗 **Se estudia junto con:** prueba de Foucault, centro de curvatura, razón de Strehl, profundidad de foco.

📘 **Dónde se aprende** (3 clases): [B41-C19 · Colimación y prueba de enfoque](../programa/clases/B41/B41-C19-colimacion-y-prueba-de-enfoque/CLASE.md); [B43-C18 · Colimación instrumental](../programa/clases/B43/B43-C18-colimacion-instrumental/CLASE.md); [B49-C03 · Apuntamiento y seguimiento de radiotelescopios: modelos de apuntado y errores](../programa/clases/B49/B49-C03-apuntamiento-y-seguimiento-de-radiotelescopios-modelos-de-apuntado-y-errores/CLASE.md).

### Colimador

- El colimador da un haz paralelo.

💡 **Cómo se explica en la clase [B45-C06](../programa/clases/B45/B45-C06-diseno-de-espectrografos/CLASE.md):**
- Con un telescopio de 4 m a f/10, rendija de 1" (`w = 193,9 µm`), colimador de 500 mm, cámara de 250 mm y red de 600 l/mm, la resolución es `R = 864,0` por las tres vías; la imagen de la rendija ocupa `6,45` píxeles.
- 🎯 **Por qué importa:** El diseño se decide con unos pocos parámetros que se compensan entre sí. La decisión central: ¿qué ancho de rendija da la resolución deseada y cuántos píxeles muestrean cada elemento?
- 🔗 **Se estudia junto con:** rendija, factor anamórfico, dispersión lineal, elemento de resolución.

📘 **Dónde se aprende** (1 clase): [B45-C06 · Diseño de espectrógrafos](../programa/clases/B45/B45-C06-diseno-de-espectrografos/CLASE.md).

### Colineales

- Los colineales L1, L2, L3 están sobre el eje que une los primarios; los triangulares L4 y L5 forman con ellos un triángulo equilátero.

💡 **Cómo se explica en la clase [B73-C03](../programa/clases/B73/B73-C03-puntos-de-equilibrio-de-lagrange/CLASE.md):**
- G --> C["colineales: f(x) = 0 en el eje"]
- *Descripción textual:* el gradiente nulo del potencial da una ecuación de una variable para L1–L3 y un triángulo equilátero para L4–L5; los colineales se resuelven por dos métodos y se pasan a kilómetros.
- 🎯 **Por qué importa:** Los puntos de Lagrange son donde se estacionan observatorios y donde se acumulan asteroides troyanos. Un error de signo en la ecuación mueve L2 al otro lado.
- 🔗 **Se estudia junto con:** punto de Lagrange, triangulares, aproximación de Hill.

📘 **Dónde se aprende** (1 clase): [B73-C03 · Puntos de equilibrio de Lagrange](../programa/clases/B73/B73-C03-puntos-de-equilibrio-de-lagrange/CLASE.md).

### Colisión

- CRC-32: código cíclico de 32 bits. Colisión: dos contenidos con el mismo resumen.

💡 **Cómo se explica en la clase [B48-C17](../programa/clases/B48/B48-C17-gestion-de-archivos-observacionales/CLASE.md):**
- Con 24 bits, 4000 archivos ya tienen 38 % de probabilidad de alguna colisión: los hashes cortos sirven para detectar errores, no para identificar archivos.
- *Descripción textual:* el resumen se calcula al archivar y se vuelve a calcular al verificar; con `b` bits, una corrupción aleatoria pasa con probabilidad `2^−b` y las colisiones entre `n` archivos siguen el cumpleaños.
- 🎯 **Por qué importa:** Un archivo que se corrompe en silencio contamina todos los análisis posteriores. La decisión central: ¿qué suma de verificación y con cuántos bits detecta la corrupción?
- 🔗 **Se estudia junto con:** Suma de verificación, SHA-256, CRC-32, Problema del cumpleaños.

📘 **Dónde se aprende** (1 clase): [B48-C17 · Gestión de archivos observacionales](../programa/clases/B48/B48-C17-gestion-de-archivos-observacionales/CLASE.md).

### Colisionador

- El blanco fijo y el colisionador.
- El colisionador enfrenta dos haces.

💡 **Cómo se explica en la clase [B31-C12](../programa/clases/B31/B31-C12-antimateria-y-aniquilacion/CLASE.md):**
- En un colisionador `e⁺e⁻ → μ⁺μ⁻`, cada haz necesita `m_μc² = 105,66 MeV`, 413 veces menos que los 43,69 GeV en blanco fijo.
- Los umbrales de blanco fijo crecen con la masa final al cuadrado; el colisionador evita ese desperdicio.
- 🎯 **Por qué importa:** Producir antimateria o partículas pesadas requiere una energía mínima que depende de la configuración. La decisión central: ¿cuál es la energía umbral de una reacción y por qué un colisionador ahorra energía?
- 🔗 **Se estudia junto con:** masa invariante, umbral, aniquilación, blanco fijo.

📘 **Dónde se aprende** (2 clases): [B31-C12 · Antimateria y aniquilación](../programa/clases/B31/B31-C12-antimateria-y-aniquilacion/CLASE.md); [B31-C15 · Física de aceleradores](../programa/clases/B31/B31-C15-fisica-de-aceleradores/CLASE.md).

### Colocación

- La colocación impone la ecuación en los nodos interiores usando `D²`.
- La colocación asigna el primer instante libre dentro de la ventana.

💡 **Cómo se explica en la clase [B11-C24](../programa/clases/B11/B11-C24-metodos-espectrales-avanzados-chebyshev-y-fourier/CLASE.md):**
- *Descripción textual:* se toman los nodos de Chebyshev en `[−1, 1]`, se construye la matriz `D`, se coloca la ecuación en los nodos interiores con `D²`, se imponen las condiciones de contorno quitando los extremos, y se resuelve un sistema denso; si la solución es analítica, el error decae exponencialmente.
- Con colocación de Chebyshev el error máximo en los nodos es `2,2 × 10⁻⁴` con `N = 8`, `1,1 × 10⁻⁷` con `N = 12` y `1,9 × 10⁻¹¹` con `N = 16`; con `N = 24` llega al nivel del redondeo (`8 × 10⁻¹⁵`).
- 🎯 **Por qué importa:** Cuando la solución es suave, un método espectral reduce un problema que necesita miles de puntos con diferencias a una docena con Chebyshev. Pero tiene un costo: el paso máximo estable de un esquema explícito baja como `1/N⁴`, y funciona mal si la solución no es suave.
- 🔗 **Se estudia junto con:** nodos de Chebyshev–Gauss–Lobatto, matriz de diferenciación, condicionamiento, convergencia exponencial.

📘 **Dónde se aprende** (2 clases): [B11-C24 · Métodos espectrales avanzados (Chebyshev y Fourier)](../programa/clases/B11/B11-C24-metodos-espectrales-avanzados-chebyshev-y-fourier/CLASE.md); [B29-C18 · Redes de seguimiento temporal](../programa/clases/B29/B29-C18-redes-de-seguimiento-temporal/CLASE.md).

### Colocación de polos

- La colocación de polos elige las ganancias para que los polos del lazo cerrado queden en posiciones dadas.

💡 **Cómo se explica en la clase [B16-C12](../programa/clases/B16/B16-C12-sintonia-de-controladores-pid/CLASE.md):**
- A{"¿Conozco el modelo?"} -->|"sí"| B["Colocación de polos<br/>Kp = J wn², Kd = 2 ζ wn J"]
- *Descripción textual:* si hay modelo se coloca polos con fórmulas; si no, se ensaya la ganancia última y se aplica una receta; en ambos casos se simula, se verifican los márgenes y se reduce la ganancia si el margen es corto.
- 🎯 **Por qué importa:** En un proyecto real, las ganancias iniciales de un lazo se eligen con pocas medidas y bajo presión de calendario: a veces no hay un modelo preciso. Hay reglas que solo piden hacer oscilar el lazo con un controlador proporcional y medir dos números.
- 🔗 **Se estudia junto con:** ganancia última, periodo último, regla de lazo cerrado de Ziegler–Nichols, detuning.

📘 **Dónde se aprende** (1 clase): [B16-C12 · Sintonía de controladores PID](../programa/clases/B16/B16-C12-sintonia-de-controladores-pid/CLASE.md).

### Colocación trapezoidal

- La colocación trapezoidal impone en cada tramo `x_{k+1} − x_k = h(v_k + v_{k+1})/2` y la ecuación análoga para `v`.

💡 **Contexto en la clase [B81-C03](../programa/clases/B81/B81-C03-metodos-directos-de-transcripcion/CLASE.md):**
- 🎯 **Por qué importa:** Los métodos directos son los más usados cuando no se tiene un buen punto de partida y hay muchas restricciones. La decisión central: ¿cuántos nodos hacen falta y a qué velocidad converge el coste discreto al continuo?
- 🔗 **Se estudia junto con:** defecto, condiciones KKT, orden.

📘 **Dónde se aprende** (1 clase): [B81-C03 · Métodos directos de transcripción](../programa/clases/B81/B81-C03-metodos-directos-de-transcripcion/CLASE.md).

### Color

- El color es la diferencia de dos magnitudes.

💡 **Cómo se explica en la clase [B45-C02](../programa/clases/B45/B45-C02-magnitudes-y-sistemas-de-filtros/CLASE.md):**
- Los cuerpos calientes son más azules (colores menores).
- Los filtros reales no son rectangulares, de modo que estos colores solo son comparables entre sí.
- ⚠️ **Error frecuente:** Tomar el color sintético como medido. Se corrige con la sección 10.
- 🎯 **Por qué importa:** Los catálogos y las curvas de luz se expresan en magnitudes; sin saber su base, sumarlas o promediarlas da resultados falsos. La decisión central: ¿cómo se convierten flujos en magnitudes, colores y sus errores?
- 🔗 **Se estudia junto con:** magnitud, sistema AB, módulo de distancia.

📘 **Dónde se aprende** (1 clase): [B45-C02 · Magnitudes y sistemas de filtros](../programa/clases/B45/B45-C02-magnitudes-y-sistemas-de-filtros/CLASE.md).

### Color representativo

- El color representativo traduce longitudes de onda invisibles a colores visibles.

💡 **Cómo se explica en la clase [B130-C01](../programa/clases/B130/B130-C01-infografias-con-fuentes-verificables/CLASE.md):**
- La página de ESA/Webb añade que más allá de ese orden la elección es en parte estética; por eso un pie de imagen debe decir «color representativo».
- Explicar el color representativo de una imagen infrarroja sin llamarla «falsa» ni «real».
- ⚠️ **Error frecuente:** Llamar «real» a una imagen de color representativo, o «falsa» sin explicar. Se corrige con 8.4.
- 🎯 **Por qué importa:** Comunicar con imágenes exige mantener la fuente y la incertidumbre; la clase de comunicación general no entra en cómo se audita una pieza visual. La decisión central: ¿qué debe llevar cada cifra de una infografía para que otra persona pueda verificarla, y qué diseño la deforma?
- 🔗 **Se estudia junto con:** ficha de procedencia, estado, factor de mentira, crédito.

📘 **Dónde se aprende** (1 clase): [B130-C01 · Infografías con fuentes verificables](../programa/clases/B130/B130-C01-infografias-con-fuentes-verificables/CLASE.md).

### Columna

- Una fila se llama periodo; una columna, grupo.
- Una tabla es un conjunto de columnas del mismo largo; cada fila describe un objeto y cada columna una propiedad.
- La columna es `N(ρ) = 2∫ n(√(ρ²+z²)) dz`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B06-C02](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md):**
- Se aceptan tablas con cualquier subconjunto de elementos si cada columna declara su base y la fuente es S1 con su edición (2009).
- 🎯 **Por qué importa:** Cuando alguien dice «el universo es casi todo hidrógeno y helio», ¿en qué sentido es cierto? ¿En número de átomos, en masa, en el Sol, en la Tierra?
- 🔗 **Se estudia junto con:** tabla periódica, fila, periodo, grupo.

📘 **Dónde se aprende** (4 clases): [B06-C02 · Tabla periódica y abundancias cósmicas](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md); [B14-C05 · Tablas astronómicas y catálogos](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md); [B55-C11 · Química en cometas](../programa/clases/B55/B55-C11-quimica-en-cometas/CLASE.md); [B84-C05 · Selección de materiales](../programa/clases/B84/B84-C05-seleccion-de-materiales/CLASE.md).

### Columna atmosférica

- La columna atmosférica es la masa de aire por m²: `P/g`.

💡 **Cómo se explica en la clase [B56-C08](../programa/clases/B56/B56-C08-habitabilidad-de-marte/CLASE.md):**
- Definir gravedad superficial, velocidad de escape, temperatura de equilibrio y columna atmosférica.
- El script [ficha_de_marte.py](ficha_de_marte.py) calcula `g`, `v_esc`, el flujo solar por dos vías, `T_eq`, la comparación con −28 °C y la columna atmosférica, y comprueba `g` y `v_esc` con la hoja (< 1 %) y el flujo por `L` y por `S` (< 0,2 %).
- 🎯 **Por qué importa:** Marte es el destino más estudiado en la búsqueda de vida y el que más afecta a las reglas de protección planetaria. Para entender por qué, hace falta ver con números cuánta distancia hay entre su superficie actual y las condiciones de replicación.
- 🔗 **Se estudia junto con:** gravedad superficial, velocidad de escape, irradiancia, albedo de Bond.

📘 **Dónde se aprende** (1 clase): [B56-C08 · Habitabilidad de Marte](../programa/clases/B56/B56-C08-habitabilidad-de-marte/CLASE.md).

### Columna de líquido

- La columna de líquido es el propelente acumulado en el fondo del tanque bajo la aceleración axial.

💡 **Cómo se explica en la clase [B77-C22](../programa/clases/B77/B77-C22-centro-de-masa-y-su-variacion-con-el-consumo-de-propelente/CLASE.md):**
- Con `ρ = 1000 kg/m³` y `A = π·0,75² = 1,767 m²`, un tanque con masa de líquido `m_l` tiene una columna de longitud `L_l = m_l/(ρA)` pegada a su extremo trasero.
- P["fraccion de propelente f"] --> L["columna de liquido: masa, longitud"]
- 🎯 **Por qué importa:** El control de actitud se diseña para una masa, un centro de masa y una inercia que ya no son los mismos al final del quemado. La decisión central: ¿cuánto se mueve el centro de masa, cuánto cae la inercia y qué le pasa al margen?
- 🔗 **Se estudia junto con:** centro de masa, momento de inercia de cabeceo, teorema de ejes paralelos, oleaje.

📘 **Dónde se aprende** (1 clase): [B77-C22 · Centro de masa y su variación con el consumo de propelente](../programa/clases/B77/B77-C22-centro-de-masa-y-su-variacion-con-el-consumo-de-propelente/CLASE.md).

### Columna de masa

- La columna de masa es la masa de gas sobre una unidad de área y vale `P₀/g`.
- La columna de masa `P/g` mide el peso de la atmósfera por m².

💡 **Cómo se explica en la clase [B54-C04](../programa/clases/B54/B54-C04-presion-y-densidad/CLASE.md):**
- P["presión P0"] --> C["columna de masa P0/g"]
- *Descripción textual:* la presión de superficie da la columna de masa y, con `T` y `M`, la densidad; la hidrostática isoterma da `P(z)` y se verifica con RK4.
- 🎯 **Por qué importa:** La densidad del gas fija el empuje, el arrastre, la opacidad y el peso de la atmósfera, y sale de una sola fórmula si el gas es ideal. La pregunta motivadora: ¿cuánto pesa la atmósfera de cada mundo sobre un metro cuadrado, y hasta dónde vale el gas ideal?
- 🔗 **Se estudia junto con:** densidad, gas ideal, factor de compresibilidad, isoterma.

📘 **Dónde se aprende** (3 clases): [B36-C09 · Cúmulos en colisión como prueba de materia oscura](../programa/clases/B36/B36-C09-cumulos-en-colision-como-prueba-de-materia-oscura/CLASE.md); [B54-C04 · Presión y densidad](../programa/clases/B54/B54-C04-presion-y-densidad/CLASE.md); [B54-C16 · Atmósferas de Titán](../programa/clases/B54/B54-C16-atmosferas-de-titan/CLASE.md).

### Columna enmascarada

- Una columna enmascarada lleva, junto a los valores, un indicador de cuáles faltan.

💡 **Cómo se explica en la clase [B14-C05](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md):**
- `MaskedColumn` marca las entradas faltantes, que se muestran como enmascaradas; se pueden adjuntar metadatos a la tabla y a cada columna; se lee y escribe en varios formatos a través de una interfaz unificada; y hay operaciones de agrupación, unión (*join*) y apilado.
- Ejercicio 6. Si a una columna de paralaje enmascarada le aplicas `.mean()`, ¿qué esperas?
- 🎯 **Por qué importa:** Un catálogo de estrellas no es una lista de números: cada columna tiene una unidad, algunas filas no tienen paralaje, y la tabla viene de un instrumento, una época y una versión. Si pierdes eso al copiar los datos a un arreglo, pierdes la mitad del significado.
- 🔗 **Se estudia junto con:** tabla, fila, columna, catálogo.

📘 **Dónde se aprende** (1 clase): [B14-C05 · Tablas astronómicas y catálogos](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md).

### Coma

- El coma es la aberración de campo del paraboloide.
- La coma es una aberración de forma `ρ³ cos φ`.
- La coma es la atmósfera de gas y polvo que rodea al núcleo.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B41-C13](../programa/clases/B41/B41-C13-aberracion-esferica-y-coma/CLASE.md):**
- La coma tangencial vale `21,890 µm`; la fórmula `3θF/(16N²)` da `21,817 µm` (razón `1,0034`).
- Con campo doble la coma es `43,784 µm` (razón `2,0002`): crece con el campo.
- ⚠️ **Error frecuente:** Creer que el paraboloide no tiene aberraciones. Tiene coma y astigmatismo.
- 🎯 **Por qué importa:** Dos defectos limitan el campo y la relación focal. La decisión central: ¿hasta qué f/ sirve una esfera y qué campo tolera un paraboloide?
- 🔗 **Se estudia junto con:** aberración esférica, diferencia de camino óptico, coeficiente W040, abanico tangencial.

📘 **Dónde se aprende** (5 clases): [B41-C13 · Aberración esférica y coma](../programa/clases/B41/B41-C13-aberracion-esferica-y-coma/CLASE.md); [B43-C02 · Selección de geometría instrumental](../programa/clases/B43/B43-C02-seleccion-de-geometria-instrumental/CLASE.md); [B43-C18 · Colimación instrumental](../programa/clases/B43/B43-C18-colimacion-instrumental/CLASE.md); [B50-C10 · Errores de centrado y su efecto en el desempeño](../programa/clases/B50/B50-C10-errores-de-centrado-y-su-efecto-en-el-desempeno/CLASE.md); [B58-C04 · Núcleos y colas cometarias](../programa/clases/B58/B58-C04-nucleos-y-colas-cometarias/CLASE.md).

### Comando de resincronización

- Un comando de resincronización restablece el contador.

💡 **Contexto en la clase [B88-C17](../programa/clases/B88/B88-C17-ciberseguridad-de-avionica/CLASE.md):**
- 🎯 **Por qué importa:** Una orden falsa o repetida puede apagar un subsistema o poner la nave en riesgo. La decisión central: ¿qué comprobaciones aseguran que cada comando viene de quien tiene la clave y no es una repetición?
- 🔗 **Se estudia junto con:** etiqueta, ventana, probabilidad de acierto al azar, STRIDE.

📘 **Dónde se aprende** (1 clase): [B88-C17 · Ciberseguridad de aviónica](../programa/clases/B88/B88-C17-ciberseguridad-de-avionica/CLASE.md).

### Combinación de diferencias

- La combinación de diferencias resta líneas que comparten un nivel para eliminar `ν₀`.

💡 **Cómo se explica en la clase [B62-C02](../programa/clases/B62/B62-C02-espectros-vibracionales-de-moleculas/CLASE.md):**
- L --> D["combinación de diferencias → B"]
- Usar la combinación de diferencias para recuperar `B₀` sin conocer el origen de banda.
- 🎯 **Por qué importa:** Las bandas del CO a 4,67 µm se observan en el infrarrojo, no en milimétricas. Para interpretarlas necesitas saber de dónde sale el origen de banda, por qué las ramas P y R se separan en dos grupos y qué cambia al pasar a un isotopólogo.
- 🔗 **Se estudia junto con:** energía vibracional, origen de banda, constante rotacional del nivel, rama R.

📘 **Dónde se aprende** (1 clase): [B62-C02 · Espectros vibracionales de moléculas](../programa/clases/B62/B62-C02-espectros-vibracionales-de-moleculas/CLASE.md).

### Combinación libre de ionosfera

- La combinación libre de ionosfera es `P_IF = (f₁²P₁ − f₂²P₂)/(f₁² − f₂²)`.
- La combinación libre de ionosfera usa dos frecuencias para anular el término `1/f²`.

💡 **Cómo se explica en la clase [B51-C10](../programa/clases/B51/B51-C10-retardo-troposferico-e-ionosferico-en-vlbi-y-su-modelado/CLASE.md):**
- La combinación libre de ionosfera tiene error 1,7 × 10⁻²⁴ s sin ruido; con ruido de 0,02 ns por banda, la desviación Monte Carlo es 0,0223 ns y la amplificación analítica 1,0841 (0,0217 ns).
- Aplicar la combinación libre de ionosfera `(ν₁²τ₁ − ν₂²τ₂)/(ν₁² − ν₂²)`.
- 🎯 **Por qué importa:** Un error atmosférico de centímetros es un error de posición en geodesia y un error de fase en imagen. La decisión central: ¿cómo se mapea el retardo con la elevación y cómo se separa lo dispersivo de lo no dispersivo?
- 🔗 **Se estudia junto con:** retardo cenital, función de mapeo, elevación, capa delgada.

📘 **Dónde se aprende** (3 clases): [B51-C10 · Retardo troposférico e ionosférico en VLBI y su modelado](../programa/clases/B51/B51-C10-retardo-troposferico-e-ionosferico-en-vlbi-y-su-modelado/CLASE.md); [B57-C29 · Correcciones atmosféricas en altimetría](../programa/clases/B57/B57-C29-correcciones-atmosfericas-en-altimetria/CLASE.md); [B89-C21 · Efectos ionosféricos y centelleo en señales GNSS](../programa/clases/B89/B89-C21-efectos-ionosfericos-y-centelleo-en-senales-gnss/CLASE.md).

### Combinación lineal

- Una combinación lineal de `u₁, …, u_k` es `a₁u₁ + … + a_k u_k`.

💡 **Contexto en la clase [B10-C01](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md):**
- **Idea central (modelo mental):** Imagina una habitación sin puertas: lo que haces con los objetos de adentro (sumarlos, escalarlos) nunca te saca de la habitación. Un espacio vectorial es una «habitación» así.
- 🎯 **Por qué importa:** El estado de un satélite en un instante se describe con seis números: tres de posición y tres de velocidad. Los programas de navegación suman, restan y multiplican por escalares esos «vectores de estado» todo el tiempo: promedian estimaciones, corrigen con un error medido, propagan pequeñas perturbaciones.
- 🔗 **Se estudia junto con:** espacio vectorial real, cero, opuesto, escalar.

📘 **Dónde se aprende** (1 clase): [B10-C01 · Espacios vectoriales](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md).

### Combinado

- El combinado cambia módulo y plano a la vez.

💡 **Cómo se explica en la clase [B75-C13](../programa/clases/B75/B75-C13-cambios-de-plano-interplanetarios/CLASE.md):**
- Combinado entre dos velocidades `v₁` y `v₂` con ángulo `i`: `Δv = √(v₁² + v₂² − 2 v₁ v₂ cos i)`.
- En todos los casos el combinado cuesta menos que hacerlo por separado.
- 🎯 **Por qué importa:** Un cambio de plano puro es caro: `2 v sin(i/2)` a la velocidad de la nave. La decisión central: ¿dónde y cómo conviene girar el plano para gastar lo menos posible?
- 🔗 **Se estudia junto con:** cambio de plano puro, nodo, reparto.

📘 **Dónde se aprende** (1 clase): [B75-C13 · Cambios de plano interplanetarios](../programa/clases/B75/B75-C13-cambios-de-plano-interplanetarios/CLASE.md).

### Combustible

- El combustible es el propelente del impulso.

💡 **Cómo se explica en la clase [B118-C13](../programa/clases/B118/B118-C13-desorbitacion-controlada/CLASE.md):**
- Calcular el combustible con Tsiolkovsky.
- Ejercicio 3 · casi autónomo. ¿Cuánto combustible pide un Δv de 100 m/s con 800 kg e Isp 300 s?
- 🎯 **Por qué importa:** La reentrada controlada dirige los restos a una zona despoblada; la no controlada deja el lugar al azar del arrastre. Pero un impulso con error cambia el ángulo y el punto de entrada.
- 🔗 **Se estudia junto con:** desorbitación controlada, interfaz de reentrada, ángulo de trayectoria, perigeo objetivo.

📘 **Dónde se aprende** (1 clase): [B118-C13 · Desorbitación controlada](../programa/clases/B118/B118-C13-desorbitacion-controlada/CLASE.md).

### Combustión incompleta

- La combustión incompleta produce CO y hollín.

💡 **Cómo se explica en la clase [B119-C23](../programa/clases/B119/B119-C23-proteccion-ambiental-de-las-actividades-de-lanzamiento/CLASE.md):**
- Combustión incompleta, hollín, óxidos de nitrógeno, aluminio de los sólidos, altitud de la emisión y efectos en la estratosfera: se evalúan con estudios formales.
- Listar lo que el modelo no incluye (combustión incompleta, otros contaminantes, efectos en la atmósfera alta).
- 🎯 **Por qué importa:** Ninguna clase de B118, B119 ni B124 trata el impacto ambiental de lanzar; esta fija el cálculo básico y sus límites antes de los estudios formales. La decisión central: ¿cuánto cambia la cota de CO₂ según el combustible y cuántos lanzamientos hacen falta para que la suma importe?
- 🔗 **Se estudia junto con:** estequiometría, cota superior, propergol, masa molar.

📘 **Dónde se aprende** (1 clase): [B119-C23 · Protección ambiental de las actividades de lanzamiento](../programa/clases/B119/B119-C23-proteccion-ambiental-de-las-actividades-de-lanzamiento/CLASE.md).

### Comentario

- Un comentario de YAML empieza con `#`;

💡 **Cómo se explica en la clase [B07-C16](../programa/clases/B07/B07-C16-formatos-json-y-yaml/CLASE.md):**
- Llaves para objetos, corchetes para listas, textos siempre entre comillas dobles, `true`/`false`/`null` en minúscula y sin comentarios (S3).
- El archivo del ejemplo se escribe sin llaves: la sangría (espacios) marca la jerarquía, `clave: valor` define un par, `[a, b]` una lista en línea y `#` un comentario.
- ⚠️ **Error frecuente:** Esperar comentarios en JSON. Se corrige con el ejercicio 4.
- 🎯 **Por qué importa:** Una simulación tiene decenas de parámetros. Si están enterrados en el código, cambiar uno obliga a editar el programa y es fácil olvidar con qué valores se obtuvo cada resultado.
- 🔗 **Se estudia junto con:** JSON, YAML, sangría, Serializar.

📘 **Dónde se aprende** (1 clase): [B07-C16 · Formatos JSON y YAML](../programa/clases/B07/B07-C16-formatos-json-y-yaml/CLASE.md).

### Comentario mayor

- Un comentario mayor cuestiona una conclusión, el método o la validez de los datos; uno menor pide aclaraciones, correcciones de forma o referencias.

💡 **Cómo se explica en la clase [B20-C03](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md):**
- Antes de contestar, numera cada comentario y asígnale una de cuatro clases: mayor (afecta una conclusión), menor (forma, aclaración), malentendido (el texto no era claro o fue mal leído) y fuera de alcance.
- Clasificar un comentario de árbitro como mayor, menor, malentendido o petición fuera de alcance.
- 🎯 **Por qué importa:** Una crítica recibida a las once de la noche se lee con el estómago antes que con la cabeza. La reacción inmediata, defenderse o rendirse, suele empeorar el trabajo y la relación con quien revisa.
- 🔗 **Se estudia junto con:** revisión por pares, autor, árbitro, editor.

📘 **Dónde se aprende** (1 clase): [B20-C03 · Revisión por pares y respuesta a árbitros](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md).

### Cometa

- Un cometa es un cuerpo pequeño que desarrolla una cola cerca del Sol.

💡 **Cómo se explica en la clase [B02-C12](../programa/clases/B02/B02-C12-tycho-brahe-y-observaciones-sistematicas/CLASE.md):**
- Las observaciones de S1 para la supernova de 1572 y el cometa de 1577 no mostraron un paralaje apreciable con la precisión de Tycho, por lo que los objetos estaban más allá de la Luna.
- S1 indica que la supernova y el cometa socavaban la división aristotélica entre lo terrestre y lo celeste, y que el movimiento del cometa mostraba que no podían existir esferas sólidas, idea que fue desapareciendo entre 1575 y 1625.
- 🎯 **Por qué importa:** Una teoría solo es tan buena como los datos con que se contrasta. La pregunta motivadora es: ¿qué diferencia hay entre «mirar el cielo» y «observar sistemáticamente», y por qué esa diferencia cambió la astronomía?
- 🔗 **Se estudia junto con:** observación sistemática, precisión angular, minuto de arco, refracción atmosférica.

📘 **Dónde se aprende** (1 clase): [B02-C12 · Tycho Brahe y observaciones sistemáticas](../programa/clases/B02/B02-C12-tycho-brahe-y-observaciones-sistematicas/CLASE.md).

### Comisión

- La comisión devuelve parte de la prima cedida.

💡 **Cómo se explica en la clase [B127-C07](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md):**
- La cuota parte lo hace barato porque la comisión es generosa (dato sintético); el exceso de pérdida lo hace caro pero solo protege contra siniestros grandes, como los que dominan este tipo de cartera, y deja intacta la frecuencia de los pequeños.
- La comisión y el recargo son parámetros del ejercicio: cambiarlos cambia la conclusión.
- ⚠️ **Error frecuente:** Tomar las comisiones y recargos como precios de mercado. Se corrige con la sección 10.
- 🎯 **Por qué importa:** El riesgo espacial se reparte mediante reaseguro; no había clase al respecto. La decisión central: ¿qué parte del riesgo se cede y cuánto cuesta reducir la cola?
- 🔗 **Se estudia junto con:** cesión, cuota parte, exceso de pérdida, prioridad.

📘 **Dónde se aprende** (1 clase): [B127-C07 · Reaseguro espacial](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md).

### Comisión de reclamaciones

- Una Comisión de Reclamaciones es el órgano del Convenio para disputas entre Estados.
- La comisión de reclamaciones se puede pedir si la negociación diplomática no resuelve en un año (art.

💡 **Cómo se explica en la clase [B123-C03](../programa/clases/B123/B123-C03-mecanismos-de-reclamacion-entre-estados/CLASE.md):**
- N -->|sin acuerdo| C["Comision de reclamaciones"]
- *Descripción textual:* tras el daño se presenta la reclamación; si en un año no hay acuerdo, se puede pedir la comisión, cuya decisión obliga solo si las partes lo acordaron.
- 🎯 **Por qué importa:** Un derecho a reclamar se pierde o se debilita si no se ejerce por la vía y en el plazo previstos. La decisión central: ¿cuándo y cómo se presenta la reclamación, cuándo se puede pedir una comisión y qué valor tiene su decisión?
- 🔗 **Se estudia junto con:** presentación, plazo, costos.

📘 **Dónde se aprende** (2 clases): [B123-C03 · Mecanismos de reclamación entre Estados](../programa/clases/B123/B123-C03-mecanismos-de-reclamacion-entre-estados/CLASE.md); [B127-C06 · Gestión de siniestros espaciales](../programa/clases/B127/B127-C06-gestion-de-siniestros-espaciales/CLASE.md).

### Commit

- Un commit es una instantánea del proyecto con un mensaje, autor y fecha;

💡 **Cómo se explica en la clase [B07-C14](../programa/clases/B07/B07-C14-control-de-versiones-con-git/CLASE.md):**
- Una rama es un puntero ligero a un commit.
- Un commit debe ser una unidad lógica: no mezcles un arreglo de unidades con una figura nueva.
- ⚠️ **Error frecuente:** Olvidar `git add` después de editar. El commit no incluye el último cambio (8.2).
- 🎯 **Por qué importa:** Sin control de versiones, un proyecto científico acumula archivos como `analisis_final.py`, `analisis_final2.py` y `analisis_final_ahora_si.py`, y nadie sabe cuál produjo la figura del artículo. Con Git, cada estado importante queda guardado con un mensaje, una fecha y un autor, y puedes comparar o recuperar cualquier versión.
- 🔗 **Se estudia junto con:** repositorio, modificado, preparado, confirmado.

📘 **Dónde se aprende** (1 clase): [B07-C14 · Control de versiones con Git](../programa/clases/B07/B07-C14-control-de-versiones-con-git/CLASE.md).

### Compacidad

- La compacidad es `r_s/R`.
- La compacidad es `GM/(Rc²)`.

💡 **Cómo se explica en la clase [B26-C07](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md):**
- El Sol, con `GM☉ = 1,327 124 4 × 10²⁰ m³/s²` y `R☉ = 6,957 × 10⁸ m` (S2), tiene un radio de Schwarzschild `r_s = 2GM/c² = 2953,25 m` (con `c` de S1) y una compacidad `r_s/R☉ = 4,245 × 10⁻⁶`.
- La Tierra, con `(GM)_E = 3,986 004 × 10¹⁴ m³/s²` y `R_E = 6,3781 × 10⁶ m` (S2), tiene `r_s = 8,870 mm` y compacidad `1,39 × 10⁻⁹`.
- 🎯 **Por qué importa:** Medir una distancia cerca de una masa grande no da lo mismo que en el espacio plano: el radio de un círculo y su circunferencia dejan de cumplir `C = 2πR`. Los GPS, las lentes gravitacionales y los agujeros negros dependen de esa diferencia.
- 🔗 **Se estudia junto con:** métrica, distancia propia, curvatura gaussiana, exceso angular.

📘 **Dónde se aprende** (3 clases): [B26-C07 · Curvatura y métricas](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md); [B27-C02 · Enanas blancas y límite de Chandrasekhar](../programa/clases/B27/B27-C02-enanas-blancas-y-limite-de-chandrasekhar/CLASE.md); [B27-C03 · Estrellas de neutrones](../programa/clases/B27/B27-C03-estrellas-de-neutrones/CLASE.md).

### Comparación múltiple

- La comparación múltiple aparece cuando se prueban varias ventanas u objetivos.

💡 **Contexto en la clase [B132-C04](../programa/clases/B132/B132-C04-estadistica-de-orientaciones-en-arqueoastronomia/CLASE.md):**
- 🎯 **Por qué importa:** Si se mira un conjunto de ejes y se busca «algo», casi siempre se encuentra. La decisión central: ¿la agrupación observada supera lo esperable por azar, una vez descontado que se probaron varias hipótesis?
- 🔗 **Se estudia junto con:** hipótesis nula, unimodal, prueba binomial.

📘 **Dónde se aprende** (1 clase): [B132-C04 · Estadística de orientaciones en arqueoastronomía](../programa/clases/B132/B132-C04-estadistica-de-orientaciones-en-arqueoastronomia/CLASE.md).

### Comparación no operativa

- La comparación no operativa contrasta rangos y no recomienda ni diseña.

💡 **Cómo se explica en la clase [B78-C20](../programa/clases/B78/B78-C20-comparacion-no-operativa-de-arquitecturas-de-propulsion/CLASE.md):**
- Comparacion NO operativa por RANGOS publicados: m0 = 1000 kg, dv = 3000 m/s, P = 5 kW (ILUSTRATIVOS)
- python programa/clases/B78/B78-C20-comparacion-no-operativa-de-arquitecturas-de-propulsion/comparacion.py
- 🎯 **Por qué importa:** Cada arquitectura gana en una dimensión y pierde en otra. La decisión central: ¿qué opciones no están dominadas por otra en propelente y en tiempo, y cómo cambia el resultado con la potencia disponible?
- 🔗 **Se estudia junto con:** valor representativo, dominancia, frente de Pareto, tope de potencia.

📘 **Dónde se aprende** (1 clase): [B78-C20 · Comparación no operativa de arquitecturas de propulsión](../programa/clases/B78/B78-C20-comparacion-no-operativa-de-arquitecturas-de-propulsion/CLASE.md).

### Comparaciones

- El costo se mide aquí como número de comparaciones.

💡 **Cómo se explica en la clase [B07-C18](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md):**
- El laboratorio cuenta dos comparaciones por vuelta (igualdad y orden), de modo que con 1000 elementos ausentes tarda 18 comparaciones frente a las 1000 de la lineal.
- En una lista ya ordenada hace `n − 1` comparaciones; en una inversa, `n(n−1)/2`; en promedio, unas `n²/4`.
- 🎯 **Por qué importa:** Un catálogo estelar tiene millones de objetos. Buscar uno a uno es posible con diez planetas y ruinoso con diez millones.
- 🔗 **Se estudia junto con:** búsqueda lineal, búsqueda binaria, ordenada, ordenamiento por inserción.

📘 **Dónde se aprende** (1 clase): [B07-C18 · Algoritmos de búsqueda y ordenamiento](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md).

### Comparaciones múltiples

- Las comparaciones múltiples inflan `α`; la corrección de Bonferroni usa `α/m`.

💡 **Cómo se explica en la clase [B105-C20](../programa/clases/B105/B105-C20-diseno-de-protocolo-medico-simulado/CLASE.md):**
- *Descripción textual:* el número de participantes, el tamaño del efecto y `α` fijan la potencia; con ella se calcula el efecto mínimo detectable, y las comparaciones múltiples exigen corregir `α`.
- Calcular la inflación del error por comparaciones múltiples y la corrección de Bonferroni.
- 🎯 **Por qué importa:** Un estudio con 6 personas solo detecta efectos grandes; sin saberlo, se concluye «no hay efecto» cuando solo no había potencia. La decisión central: ¿qué efecto mínimo puede detectar el protocolo con su `n`, y cuántas comparaciones puede permitirse?
- 🔗 **Se estudia junto con:** tamaño del efecto, potencia, error tipo I, efecto mínimo detectable.

📘 **Dónde se aprende** (1 clase): [B105-C20 · Diseño de protocolo médico simulado](../programa/clases/B105/B105-C20-diseno-de-protocolo-medico-simulado/CLASE.md).

### Comparten

- Un hilo es una línea de ejecución dentro de un proceso; los hilos de un mismo proceso comparten su memoria.

💡 **Cómo se explica en la clase [B18-C01](../programa/clases/B18/B18-C01-procesos-hilos-y-concurrencia/CLASE.md):**
- Analogía y su límite. Un proceso es una casa con su cocina; los hilos son cocineros que comparten esa cocina y, con el GIL, hay un único fogón de Python.
- Los hilos solapan esperas y comparten memoria sin copiar, pero no aceleran Python puro de CPU y obligan a cuidar las carreras.
- 🎯 **Por qué importa:** Tienes ocho órbitas simuladas que propagar y un portátil con varios núcleos. La tentación es «lanzar ocho hilos y listo».
- 🔗 **Se estudia junto con:** proceso, hilo, concurrencia, paralelismo.

📘 **Dónde se aprende** (1 clase): [B18-C01 · Procesos, hilos y concurrencia](../programa/clases/B18/B18-C01-procesos-hilos-y-concurrencia/CLASE.md).

### Compartimento

- Un compartimento es un tejido idealizado.
- Un compartimento es un volumen mezclado.

💡 **Cómo se explica en la clase [B104-C11](../programa/clases/B104/B104-C11-trajes-espaciales/CLASE.md):**
- Los compartimentos lentos mandan el tiempo.
- Límite: el modelo de un compartimento no recoge burbujas, perfusión ni la variación de los tejidos.
- 🎯 **Por qué importa:** Un traje presurizado a una fracción de la presión de la cabina deja al nitrógeno disuelto en sobresaturación si no se elimina antes. La decisión conceptual: ¿cómo depende el tiempo de eliminación del nitrógeno del compartimento, de la razón crítica y de la presión de la cabina?
- 🔗 **Se estudia junto con:** tiempo medio, razón crítica, preoxigenación.

📘 **Dónde se aprende** (2 clases): [B104-C11 · Trajes espaciales](../programa/clases/B104/B104-C11-trajes-espaciales/CLASE.md); [B117-C02 · Contención de riesgos biológicos y químicos en cabina](../programa/clases/B117/B117-C02-contencion-de-riesgos-biologicos-y-quimicos-en-cabina/CLASE.md).

### Compás estelar

- El compás estelar es, según S1, una forma de organizar las direcciones mediante puntos de salida y puesta de estrellas; no desarrollamos su estructura porque no la consultamos.

💡 **Cómo se explica en la clase [B02-C07](../programa/clases/B02/B02-C07-observaciones-de-polinesia-y-navegacion-oceanica/CLASE.md):**
- S1 explica que los navegantes usan el compás estelar, el Sol, la Luna, las olas y los seres marinos para encontrar rumbo y posición sin instrumentos, y S4 menciona también el viento, las nubes y las aves.
- 🎯 **Por qué importa:** Se discutió durante décadas si los pueblos del Pacífico llegaron a las islas por azar o por navegación deliberada. La pregunta motivadora es: ¿cómo se orienta quien no puede ver tierra, y qué dice su método sobre el valor del conocimiento oral?
- 🔗 **Se estudia junto con:** navegación sin instrumentos, azimut, declinación, horizonte.

📘 **Dónde se aprende** (1 clase): [B02-C07 · Observaciones de Polinesia y navegación oceánica](../programa/clases/B02/B02-C07-observaciones-de-polinesia-y-navegacion-oceanica/CLASE.md).

### Compatibilidad

- La compatibilidad es `|δ_eje − δ_astro| < 2σ`.

💡 **Cómo se explica en la clase [B132-C03](../programa/clases/B132/B132-C03-monumentos-megaliticos-y-astronomia/CLASE.md):**
- *Descripción textual:* azimut, altura (corregida por refracción) y latitud dan la declinación del eje; la oblicuidad de la época da la declinación solsticial; su diferencia en unidades de `σ` decide la compatibilidad.
- Por estadística: compatibilidad en `σ` (C04).
- ⚠️ **Error frecuente:** Confundir compatibilidad con intención. Se corrige con la sección 1 y el ejercicio 9.
- 🎯 **Por qué importa:** Una avenida de piedras que mira hacia el noreste «parece» apuntar al solsticio, pero ¿con qué precisión y para qué época? La decisión central: ¿qué declinación tiene el eje, con qué incertidumbre, y es compatible con el Sol solsticial de la época del monumento?
- 🔗 **Se estudia junto con:** declinación, azimut de salida, refracción de Bennett.

📘 **Dónde se aprende** (1 clase): [B132-C03 · Monumentos megalíticos y astronomía](../programa/clases/B132/B132-C03-monumentos-megaliticos-y-astronomia/CLASE.md).

### Compatibilidad dimensional

- La compatibilidad dimensional significa que dos unidades miden la misma clase de magnitud (longitud con longitud).

💡 **Contexto en la clase [B07-C11](../programa/clases/B07/B07-C11-gestion-de-unidades-en-programas/CLASE.md):**
- **Idea central (modelo mental):** Imagina que cada número lleva pegada una etiqueta con su unidad, y que las operaciones solo se permiten si las etiquetas son compatibles: puedes sumar metros con kilómetros (el programa convierte), pero no metros con kilogramos.
- 🎯 **Por qué importa:** Un error de unidades no hace fallar el programa: lo hace dar una respuesta distinta de la esperada. En la clase C09 viste que un radio en km en vez de m multiplica la densidad por 10⁹ sin ningún aviso.
- 🔗 **Se estudia junto con:** unidad, cantidad, adimensional, constante.

📘 **Dónde se aprende** (1 clase): [B07-C11 · Gestión de unidades en programas](../programa/clases/B07/B07-C11-gestion-de-unidades-en-programas/CLASE.md).

### Compatibilidad métrica

- La compatibilidad métrica es `∇g = 0`.

💡 **Cómo se explica en la clase [B39-C02](../programa/clases/B39/B39-C02-conexion-afin-y-simbolos-de-christoffel/CLASE.md):**
- La asimetría máxima en los índices inferiores es `0` y la violación máxima de la compatibilidad métrica `0`.
- violacion maxima de la compatibilidad metrica: 0.00e+00
- 🎯 **Por qué importa:** Sin conexión no hay aceleración ni geodésicas. La decisión central: ¿qué símbolos produce una métrica y qué propiedades garantizan que sea la conexión correcta?
- 🔗 **Se estudia junto con:** conexión de Levi-Civita, símbolos de Christoffel, derivada covariante, geodésica.

📘 **Dónde se aprende** (1 clase): [B39-C02 · Conexión afín y símbolos de Christoffel](../programa/clases/B39/B39-C02-conexion-afin-y-simbolos-de-christoffel/CLASE.md).

### Compatible

- Un sistema es compatible si tiene solución e incompatible si no (S1, §1.2(vi): `n` ecuaciones con `n` incógnitas).

💡 **Contexto en la clase [B10-C05](../programa/clases/B10/B10-C05-sistemas-lineales-y-eliminacion/CLASE.md):**
- **Idea central (modelo mental):** Eliminar es convertir el sistema en una escalera; luego bajas escalón por escalón.
- 🎯 **Por qué importa:** Para fijar la posición de un objeto a partir de las distancias a tres estaciones se plantean tres ecuaciones con dos incógnitas (plano). Los sistemas reales tienen decenas o miles de incógnitas: parámetros orbitales, sesgos de relojes, coeficientes de calibración.
- 🔗 **Se estudia junto con:** sistema lineal, matriz ampliada, operación elemental de fila, eliminación gaussiana.

📘 **Dónde se aprende** (1 clase): [B10-C05 · Sistemas lineales y eliminación](../programa/clases/B10/B10-C05-sistemas-lineales-y-eliminacion/CLASE.md).

### Compatible determinado

- Es compatible determinado si tiene una solución, compatible indeterminado si tiene infinitas, incompatible si no tiene ninguna.

💡 **Contexto en la clase [B04-C03](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md):**
- **Idea central (modelo mental):** Cada ecuación lineal con dos incógnitas es una recta en el plano; la solución del sistema es donde se cortan. Si son rectas con distinta inclinación, se cortan en un punto; si son paralelas, no se cortan; si son la misma, se cortan en todos sus puntos.
- 🎯 **Por qué importa:** Un detector no entrega «brillo»: entrega cuentas. Para convertir cuentas en flujo hay que descubrir dos números, una pendiente y un desfase, y para ello se miden dos fuentes de referencia.
- 🔗 **Se estudia junto con:** sistema de ecuaciones, lineal, solución, compatible indeterminado.

📘 **Dónde se aprende** (1 clase): [B04-C03 · Sistemas de ecuaciones elementales](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md).

### Compatible indeterminado

- Es compatible determinado si tiene una solución, compatible indeterminado si tiene infinitas, incompatible si no tiene ninguna.

💡 **Contexto en la clase [B04-C03](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md):**
- **Idea central (modelo mental):** Cada ecuación lineal con dos incógnitas es una recta en el plano; la solución del sistema es donde se cortan. Si son rectas con distinta inclinación, se cortan en un punto; si son paralelas, no se cortan; si son la misma, se cortan en todos sus puntos.
- 🎯 **Por qué importa:** Un detector no entrega «brillo»: entrega cuentas. Para convertir cuentas en flujo hay que descubrir dos números, una pendiente y un desfase, y para ello se miden dos fuentes de referencia.
- 🔗 **Se estudia junto con:** sistema de ecuaciones, lineal, solución, compatible determinado.

📘 **Dónde se aprende** (1 clase): [B04-C03 · Sistemas de ecuaciones elementales](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md).

### Compatibles

- La diferencia normalizada de dos medidas independientes es `z = |x₁ − x₂|/√(u₁² + u₂²)`: su denominador es la incertidumbre de la diferencia (S1, 5.1.2 con coeficientes `+1` y `−1`). Compatibles significa que `z` es pequeño, en esta clase `z ≤ 2` (cobertura aproximada de 95 %, C12).

💡 **Cómo se explica en la clase [B13-C18](../programa/clases/B13/B13-C18-intercomparacion-de-instrumentos/CLASE.md):**
- `z₁₃ = 1,92 ≤ 2`: compatibles; con `N = 2`, `χ² = z₁₃² = 3,69` y `RB = √(3,69/1) = 1,92`.
- Decidir si dos medidas son compatibles con un criterio `z ≤ 2`.
- 🎯 **Por qué importa:** Tres radiómetros miden la misma irradiancia solar y dan `1361,4`, `1360,1` y `1362,9 W/m²`. Cada uno declara una incertidumbre.
- 🔗 **Se estudia junto con:** intercomparación, diferencia normalizada, media ponderada, chi cuadrado.

📘 **Dónde se aprende** (1 clase): [B13-C18 · Intercomparación de instrumentos](../programa/clases/B13/B13-C18-intercomparacion-de-instrumentos/CLASE.md).

### Compensación

- La compensación combina dos materiales.

💡 **Cómo se explica en la clase [B43-C11](../programa/clases/B43/B43-C11-dilatacion-termica-y-estabilidad/CLASE.md):**
- Ejercicio 12. Integrador. Elabora tu *ficha de estabilidad térmica*: deriva, compensación y constante de tiempo.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de estabilidad térmica*: deriva, compensación y constante de tiempo.
- ⚠️ **Error frecuente:** Sumar longitudes sin signo en la compensación. Se corrige con 8.2.
- 🎯 **Por qué importa:** La estabilidad térmica fija cuándo se puede observar y cada cuánto hay que reenfocar. La decisión central: ¿cuánto se mueve el foco por kelvin, cómo se compensa y cuánto tarda el espejo en igualarse al aire?
- 🔗 **Se estudia junto con:** coeficiente de dilatación, deriva de foco, número de Biot, constante de tiempo.

📘 **Dónde se aprende** (1 clase): [B43-C11 · Dilatación térmica y estabilidad](../programa/clases/B43/B43-C11-dilatacion-termica-y-estabilidad/CLASE.md).

### Competencia estratégica

- El día juliano es un conteo continuo de días. Competencia estratégica es la rivalidad entre Estados por ventaja de seguridad, poder o prestigio.

💡 **Cómo se explica en la clase [B119-C12](../programa/clases/B119/B119-C12-historia-de-competencia-estrategica-espacial/CLASE.md):**
- python programa/clases/B119/B119-C12-historia-de-competencia-estrategica-espacial/laboratorio.py
- 🎯 **Por qué importa:** Para leer el derecho vigente conviene saber qué contexto lo produjo; ninguna clase anterior da la cronología comparada entre la tecnología y los instrumentos jurídicos. La decisión central: ¿cuánto tardó el derecho en seguir a la tecnología y por qué importa distinguir fechas verificadas de fechas recordadas?
- 🔗 **Se estudia junto con:** hito, rezago normativo, día juliano, fuente primaria.

📘 **Dónde se aprende** (1 clase): [B119-C12 · Historia de competencia estratégica espacial](../programa/clases/B119/B119-C12-historia-de-competencia-estrategica-espacial/CLASE.md).

### Compilación reproducible

- La compilación reproducible da bytes idénticos.

💡 **Cómo se explica en la clase [B88-C18](../programa/clases/B88/B88-C18-control-de-configuracion-de-firmware/CLASE.md):**
- El script [linea_base.py](linea_base.py) construye manifiestos y IDs de dos versiones, lista las diferencias, compara dos compilaciones con y sin fecha y mide la avalancha, y comprueba las diferencias esperadas y que sin fecha sea reproducible.
- Predice antes de ejecutar: ¿será reproducible la compilación con fecha incrustada?
- 🎯 **Por qué importa:** Si no se sabe exactamente qué firmware vuela, no se puede reproducir un fallo ni comprobar que se probó lo que se lanzó. La decisión central: ¿qué registro identifica de manera única una versión y permite verificarla?
- 🔗 **Se estudia junto con:** manifiesto, ID de línea base, diferencia, efecto avalancha.

📘 **Dónde se aprende** (1 clase): [B88-C18 · Control de configuración de firmware](../programa/clases/B88/B88-C18-control-de-configuracion-de-firmware/CLASE.md).

### Complejidad algorítmica

- La complejidad algorítmica describe cómo crece el trabajo con el tamaño del problema (aquí, `N²/2`).

💡 **Contexto en la clase [B18-C04](../programa/clases/B18/B18-C04-perfilado-de-rendimiento/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR A["1. Línea base<br/>correcta y cronometrada"] --> B["2. Perfilar<br/>¿qué concentra el tiempo?"] B --> C["3.
- 🎯 **Por qué importa:** Casi todo programa científico tiene un cuello de botella que el autor no sospecha. Optimizar a ojo suele mejorar lo que no importa.
- 🔗 **Se estudia junto con:** perfil, perfilador, cuello de botella, perfilado determinista.

📘 **Dónde se aprende** (1 clase): [B18-C04 · Perfilado de rendimiento](../programa/clases/B18/B18-C04-perfilado-de-rendimiento/CLASE.md).

### Complementaria

- La función de sensibilidad es `S = 1/(1 + L)` y la complementaria `T = L/(1+L)`.

💡 **Cómo se explica en la clase [B16-C06](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md):**
- Calcular las funciones de lazo `L`, sensibilidad `S` y sensibilidad complementaria `T`.
- 🎯 **Por qué importa:** Un sistema de control de actitud tiene sensores, un computador, ruedas y un cuerpo, todos conectados y, sobre todo, con la salida de vuelta a la entrada. Para entender qué hace el conjunto no basta conocer las partes: hay que saber cómo se combinan.
- 🔗 **Se estudia junto con:** diagrama de bloques, sumador, punto de bifurcación, lazo cerrado.

📘 **Dónde se aprende** (1 clase): [B16-C06 · Diagramas de bloques](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md).

### Complementariedad

- signo `μ ≥ 0`; y complementariedad `μ (T − T_max) = 0` (o la restricción está activa o su multiplicador es cero).

💡 **Cómo se explica en la clase [B11-C23](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md):**
- Complementariedad: la restricción está activa (`T = T_max`) y `μ > 0` ✓.
- Estacionariedad `Δv′ + μ T′ = 0`; factibilidad `T = T_max`; signo `μ > 0`; complementariedad `μ (T − T_max) = 0` ✓.
- 🎯 **Por qué importa:** Casi todo problema de diseño de trayectorias tiene límites: tiempo máximo, combustible disponible, distancia mínima a un cuerpo. Un optimizador que ignora las restricciones devuelve un resultado imposible; uno que las trata mal da un resultado que parece factible y no es óptimo.
- 🔗 **Se estudia junto con:** con restricción de igualdad, Lagrangiano, multiplicador de Lagrange, desigualdad.

📘 **Dónde se aprende** (1 clase): [B11-C23 · Optimización restringida: Lagrange, KKT y SQP](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md).

### Complemento

- El complemento `Aᶜ` son los resultados que no están en `A`.

💡 **Cómo se explica en la clase [B12-C01](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md):**
- Usar complemento, unión y probabilidad condicional, y aplicar la regla de Bayes en un caso de dos eventos.
- Ejercicio 8. Calcula `P(C1 falla ∪ C2 falla)` con la fórmula de unión y con el complemento.
- 🎯 **Por qué importa:** Una nave no sabe si un componente va a fallar; un telescopio no sabe cuántos fotones llegarán. Para decidir con información incompleta hace falta un lenguaje que diga con precisión *qué puede pasar* y *cuánto lo esperamos*.
- 🔗 **Se estudia junto con:** experimento aleatorio, espacio muestral, evento, probabilidad.

📘 **Dónde se aprende** (1 clase): [B12-C01 · Espacios muestrales y eventos](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md).

### Completamente convectiva

- Una estrella completamente convectiva mezcla todo su interior y puede quemar casi todo su hidrógeno (`f ≈ 1`).

💡 **Cómo se explica en la clase [B24-C15](../programa/clases/B24/B24-C15-estrellas-de-baja-masa/CLASE.md):**
- Una estrella de `0,1 M☉` y `0,2 M☉`, completamente convectivas (`f = 1`), tendrían `6400` y `2600 Gyr`.
- Explicar por qué las estrellas completamente convectivas viven aún más.
- ⚠️ **Error frecuente:** Usar `f = 0,1` para estrellas completamente convectivas. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** La masa decide casi todo en la vida de una estrella: cuánto brilla, cuánto dura y cómo termina. Entender por qué una estrella de la mitad de la masa del Sol vive varias veces más tiempo, y por qué las más pequeñas casi no han evolucionado, explica la composición de las poblaciones estelares y la edad de los cúmulos.
- 🔗 **Se estudia junto con:** secuencia principal, relación masa–luminosidad, tiempo nuclear, enana roja.

📘 **Dónde se aprende** (1 clase): [B24-C15 · Estrellas de baja masa](../programa/clases/B24/B24-C15-estrellas-de-baja-masa/CLASE.md).

### Completitud

- La completitud es la fracción de fuentes reales de un flujo dado que se detectan.
- La completitud es la fracción de los objetos que cumplen el criterio y están en el catálogo.
- La completitud es el diámetro por encima del cual no falta ningún cráter.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C12](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md):**
- La completitud es 50 % cuando la SNR iguala al umbral y sube rápido unas unidades por encima.
- Predecir la tasa de falsas alarmas y la completitud para un umbral dado.
- ⚠️ **Error frecuente:** Reportar el catálogo sin completitud ni falsas alarmas. Se corrige con el ejercicio 12.
- 🎯 **Por qué importa:** Un catálogo de fuentes es el producto básico de una imagen astronómica, y de él salen cuentas, colores y candidatos a objetos nuevos. Si el umbral es bajo, el catálogo se llena de ruido; si es alto, se pierden las fuentes débiles.
- 🔗 **Se estudia junto con:** fondo, ruido, relación señal–ruido, filtro adaptado.

📘 **Dónde se aprende** (9 clases): [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B25-C19 · Catálogos y sesgos de selección](../programa/clases/B25/B25-C19-catalogos-y-sesgos-de-seleccion/CLASE.md); [B53-C08 · Cartografía de cráteres](../programa/clases/B53/B53-C08-cartografia-de-crateres/CLASE.md); [B74-C22 · Informe de navegación verificable](../programa/clases/B74/B74-C22-informe-de-navegacion-verificable/CLASE.md); [B96-C16 · Gestión de datos científicos](../programa/clases/B96/B96-C16-gestion-de-datos-cientificos/CLASE.md); [B118-C21 · Calidad, latencia y trazabilidad de datos de vigilancia espacial](../programa/clases/B118/B118-C21-calidad-latencia-y-trazabilidad-de-datos-de-vigilancia-espacial/CLASE.md) y 3 más.

### Completitud ponderada

- La completitud ponderada es el valor observado entre el total.

💡 **Cómo se explica en la clase [B29-C18](../programa/clases/B29/B29-C18-redes-de-seguimiento-temporal/CLASE.md):**
- Completitud ponderada media: 1 telescopio `0,449`, 2: `0,716`, 3: `0,861`, 5: `0,988`, 8: `1,000`.
- completitud ponderada media con 1 telescopio = 0.459 ; con 3 telescopios = 0.878
- 🎯 **Por qué importa:** La regla de planificación determina cuánto valor científico se recoge. Una regla ingenua puede perder la mitad del valor; añadir telescopios no siempre compensa.
- 🔗 **Se estudia junto con:** blanco, colocación, regla voraz, óptimo.

📘 **Dónde se aprende** (1 clase): [B29-C18 · Redes de seguimiento temporal](../programa/clases/B29/B29-C18-redes-de-seguimiento-temporal/CLASE.md).

### Componente

- Un componente es una parte del sistema (aquí, cada cuerpo con su distancia y su tamaño).
- Una componente es la parte de un vector sobre un eje.
- Un componente es una parte con función propia (sitio, instrumentos, seguridad...).
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C05](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md):**
- Cada componente tiene su unidad (N) y su signo según el sentido del eje.
- Paso 4 · Sentido físico. La componente radial sigue siendo la gravedad: curva la trayectoria.
- 🎯 **Por qué importa:** En un lanzamiento o en una maniobra hay varias fuerzas a la vez: gravedad, empuje, tensiones, rozamiento. La pregunta motivadora es: ¿cómo dejo de olvidar fuerzas y de contar dos veces una misma?
- 🔗 **Se estudia junto con:** diagrama de cuerpo libre (DCL), peso, normal, tensión.

📘 **Dónde se aprende** (4 clases): [B03-C20 · Problema integrado de escala del sistema solar](../programa/clases/B03/B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md); [B05-C05 · Diagramas de cuerpo libre](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md); [B08-C20 · Proyecto de campaña de observación nocturna](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md); [B55-C14 · Química de regolitos](../programa/clases/B55/B55-C14-quimica-de-regolitos/CLASE.md).

### Componente CLEAN

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B46-C19](../programa/clases/B46/B46-C19-imagenes-de-radio-y-clean/CLASE.md):**
- **Idea central (modelo mental):** Se borra la huella del haz pico a pico, con trazos suaves, hasta que lo que queda es solo ruido.
- 🎯 **Por qué importa:** La imagen sucia no se puede interpretar por los lóbulos del haz. La decisión central: ¿cuándo detener la deconvolución para no ajustar ruido?
- 🔗 **Se estudia junto con:** imagen sucia, CLEAN, ganancia del lazo, residuo.

📘 **Dónde se aprende** (1 clase): [B46-C19 · Imágenes de radio y CLEAN](../programa/clases/B46/B46-C19-imagenes-de-radio-y-clean/CLASE.md).

### Componente de línea de visión

- La componente de línea de visión y la transversal son las incertidumbres a lo largo de la dirección de la nave y perpendicular a ella.

💡 **Cómo se explica en la clase [B74-C15](../programa/clases/B74/B74-C15-geometria-de-la-red-de-seguimiento/CLASE.md):**
- *Descripción textual:* las posiciones de estaciones y nave definen las líneas de visión, de ellas sale la matriz de información, su inversa da la covarianza y el DOP; la línea de base domina la componente transversal.
- Descomponer la incertidumbre en componente a lo largo de la línea de visión y transversal.
- 🎯 **Por qué importa:** La precisión de seguimiento no se compra solo con mejores receptores. La decisión central: ¿qué configuración de estaciones y qué observables dan información en las tres direcciones, y cuánto vale la línea de base?
- 🔗 **Se estudia junto con:** dilución de la precisión, línea de base, transversal, número de condición.

📘 **Dónde se aprende** (1 clase): [B74-C15 · Geometría de la red de seguimiento](../programa/clases/B74/B74-C15-geometria-de-la-red-de-seguimiento/CLASE.md).

### Componente principal

- Un componente principal es una dirección del espacio de variables de máxima varianza; los componentes son ortogonales.

💡 **Cómo se explica en la clase [B17-C06](../programa/clases/B17/B17-C06-aprendizaje-no-supervisado/CLASE.md):**
- Con la matriz centrada `X` (n×p), la SVD `X = U S Vᵀ` da en las filas de `Vᵀ` las direcciones principales y en `s` los valores singulares; la varianza del componente `j` es `sⱼ²/(n − 1)` y coincide con el `j`-ésimo autovalor de la covarianza (B10-C11).
- 🎯 **Por qué importa:** Un catálogo trae miles de objetos medidos en varias bandas y nadie los ha clasificado. ¿Hay poblaciones distintas?
- 🔗 **Se estudia junto con:** aprendizaje no supervisado, varianza explicada, agrupamiento, K-medias.

📘 **Dónde se aprende** (1 clase): [B17-C06 · Aprendizaje no supervisado](../programa/clases/B17/B17-C06-aprendizaje-no-supervisado/CLASE.md).

### Componentes

- Sus componentes son los números que lo describen respecto de unos ejes: en el plano, `v = (vₓ, v_y)`.
- Las componentes `B·T` y `B·R` definen el punto de apuntado.

💡 **Cómo se explica en la clase [B04-C12](../programa/clases/B04/B04-C12-vectores-y-componentes/CLASE.md):**
- Un vector es el mismo aunque cambien los ejes; sus componentes, no.
- Los componentes son lo que cada flecha avanza a lo largo de `x` y de `y`.
- ⚠️ **Error frecuente:** Confundir el vector con sus componentes. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Una sonda que sale de la Tierra tiene una velocidad respecto de la Tierra y la Tierra tiene una velocidad respecto del Sol. ¿Cuál es la velocidad de la sonda respecto del Sol?
- 🔗 **Se estudia junto con:** escalar, vector, módulo, suma.

📘 **Dónde se aprende** (2 clases): [B04-C12 · Vectores y componentes](../programa/clases/B04/B04-C12-vectores-y-componentes/CLASE.md); [B75-C24 · Plano B y parámetro de impacto](../programa/clases/B75/B75-C24-plano-b-y-parametro-de-impacto/CLASE.md).

### Comportamiento reactivo

- Un comportamiento reactivo responde a lo percibido en cada ciclo sin planificar.

💡 **Cómo se explica en la clase [B98-C05](../programa/clases/B98/B98-C05-autonomia-de-bajo-nivel-y-comportamientos-reactivos/CLASE.md):**
- python programa/clases/B98/B98-C05-autonomia-de-bajo-nivel-y-comportamientos-reactivos/reflejo.py
- 🎯 **Por qué importa:** Ningún plan, por bueno que sea, protege a un vehículo del peligro que aparece entre dos ciclos de comunicación. La decisión central: ¿qué debe resolver el vehículo por sí mismo y a qué velocidad puede ir para que ese reflejo llegue a tiempo?
- 🔗 **Se estudia junto con:** reflejo, distancia de frenado, velocidad máxima admisible, histéresis.

📘 **Dónde se aprende** (1 clase): [B98-C05 · Autonomía de bajo nivel y comportamientos reactivos](../programa/clases/B98/B98-C05-autonomia-de-bajo-nivel-y-comportamientos-reactivos/CLASE.md).

### Composición

- Una composición es una función dentro de otra.
- La composición de *boosts* es el producto de matrices.
- La composición `g(f(x))` aplica primero `f` y luego `g`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C04](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md):**
- Una composición típica: pasar de `P` en días a años con `g(P) = P/365,25` y luego aplicar otra regla.
- 🎯 **Por qué importa:** Un astrónomo no solo calcula un valor: pregunta «¿qué pasa con el periodo de un planeta si su órbita es el doble de grande?». Responderlo con un solo caso no basta; hace falta la regla que liga ambas magnitudes.
- 🔗 **Se estudia junto con:** función, dominio, rango, variable independiente.

📘 **Dónde se aprende** (6 clases): [B04-C04 · Funciones y gráficas](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md); [B04-C15 · Rotación de puntos y ejes](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md); [B09-C04 · Reglas de derivación](../programa/clases/B09/B09-C04-reglas-de-derivacion/CLASE.md); [B23-C06 · Pruebas metamórficas](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md); [B26-C02 · Transformaciones de Lorentz](../programa/clases/B26/B26-C02-transformaciones-de-lorentz/CLASE.md); [B57-C05 · Imágenes multiespectrales](../programa/clases/B57/B57-C05-imagenes-multiespectrales/CLASE.md).

### Composición de velocidades

- La composición de velocidades es la regla que da la velocidad `w` de un cuerpo respecto de un marco, conocidas `u` (del cuerpo respecto de un segundo marco) y `v` (del segundo marco respecto del primero).

💡 **Cómo se explica en la clase [B26-C01](../programa/clases/B26/B26-C01-postulados-de-relatividad-especial/CLASE.md):**
- Aplicar la composición relativista de velocidades.
- La evidencia es la hoja de composición de velocidades del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Una nave espacial, un satélite de navegación y un rayo gamma comparten un problema: decir cómo se ve el mismo fenómeno desde marcos que se mueven entre sí. Si las velocidades se sumaran siempre como `u + v`, la luz de una nave que viaja al `90 %` de `c` iría más rápido que `c`.
- 🔗 **Se estudia junto con:** marco inercial, principio de relatividad, postulado de la constancia de c, rapidez.

📘 **Dónde se aprende** (1 clase): [B26-C01 · Postulados de relatividad especial](../programa/clases/B26/B26-C01-postulados-de-relatividad-especial/CLASE.md).

### Composición de Yoshida

- La composición de Yoshida combina tres leapfrogs con pasos `w₁h, w₀h, w₁h` (`w₁ = 1/(2 − 2^{1/3})`, `w₀ = −2^{1/3} w₁`) para dar orden 4.

💡 **Contexto en la clase [B73-C09](../programa/clases/B73/B73-C09-integracion-de-largo-plazo/CLASE.md):**
- 🎯 **Por qué importa:** La estabilidad del sistema solar se estudia con integraciones de millones de órbitas, donde un integrador con deriva secular de energía inventa una dinámica que no existe. La decisión central: ¿qué integrador elijo para un horizonte largo y cómo reconozco que ha derivado?
- 🔗 **Se estudia junto con:** error acotado, deriva secular, reversibilidad.

📘 **Dónde se aprende** (1 clase): [B73-C09 · Integración de largo plazo](../programa/clases/B73/B73-C09-integracion-de-largo-plazo/CLASE.md).

### Composición en masa

- Una composición en masa (o «% en peso») es la fracción de la masa total que corresponde a un elemento.

💡 **Cómo se explica en la clase [B06-C06](../programa/clases/B06/B06-C06-cantidad-de-sustancia-y-mol/CLASE.md):**
- Con la composición en masa, la masa de cada elemento es `m_X = m_total × (% / 100)`.
- Puedes dar la composición en masa (% en peso: lo que mide una balanza) o en átomos (razones `N_X/N_Y`: lo que ve un espectro).
- 🎯 **Por qué importa:** La misión OSIRIS-REx trajo a la Tierra 121,6 g de material del asteroide Bennu. Los análisis de laboratorio de una parte de esa muestra encontraron entre 4,5 y 4,7 % de carbono y entre 0,23 y 0,25 % de nitrógeno en masa (S1).
- 🔗 **Se estudia junto con:** cantidad de sustancia, mol, constante de Avogadro, masa molar.

📘 **Dónde se aprende** (1 clase): [B06-C06 · Cantidad de sustancia y mol](../programa/clases/B06/B06-C06-cantidad-de-sustancia-y-mol/CLASE.md).

### Composición porcentual

- La composición porcentual (en masa) de un elemento en un compuesto es `n_átomos × M_elemento / M_compuesto × 100`.

💡 **Cómo se explica en la clase [B06-C07](../programa/clases/B06/B06-C07-estequiometria-elemental/CLASE.md):**
- En el de arriba, una fórmula se convierte en masa por mol y luego en composición porcentual.
- Calcular la composición porcentual en masa de un compuesto.
- 🎯 **Por qué importa:** Si quieres saber cuánto pesa una columna de atmósfera de Marte, necesitas su masa molar media, y para eso, su composición. La NASA publica la composición en volumen de las atmósferas de Marte, Venus y la Tierra y también un «peso molecular» medio (S1, S2, S3).
- 🔗 **Se estudia junto con:** fórmula molecular, fórmula empírica, fracción molar, masa molar media.

📘 **Dónde se aprende** (1 clase): [B06-C07 · Estequiometría elemental](../programa/clases/B06/B06-C07-estequiometria-elemental/CLASE.md).

### Composicionales

- Los datos de secuenciación son composicionales: solo informan proporciones.

💡 **Cómo se explica en la clase [B105-C11](../programa/clases/B105/B105-C11-microbioma-en-ambientes-cerrados/CLASE.md):**
- Ejercicio 11 · transferencia. Los datos de secuenciación son composicionales.
- ⚠️ **Error frecuente:** Interpretar proporciones como cantidades absolutas. Los datos son composicionales (ejercicio 11).
- 🎯 **Por qué importa:** Un índice de diversidad depende de la comunidad y de cuántas lecturas se obtuvieron. La decisión central: ¿qué profundidad de muestreo hace fiable un índice y cómo se cuantifica el parecido entre la piel de la tripulación y las superficies?
- 🔗 **Se estudia junto con:** riqueza, índice de Shannon, Simpson, disimilitud de Bray–Curtis.

📘 **Dónde se aprende** (1 clase): [B105-C11 · Microbioma en ambientes cerrados](../programa/clases/B105/B105-C11-microbioma-en-ambientes-cerrados/CLASE.md).

### Comprar un servicio

- Comprar un servicio es pagar un precio por un resultado, sin poseer el sistema.

💡 **Contexto en la clase [B124-C02](../programa/clases/B124/B124-C02-agencias-cientificas-y-empresas/CLASE.md):**
- 🎯 **Por qué importa:** Las agencias científicas y las empresas cumplen papeles distintos: la agencia fija objetivos y paga; la empresa ofrece capacidad y asume parte del riesgo. La decisión central: ¿cuándo conviene comprar un servicio en vez de poseer el sistema, y con qué probabilidad?
- 🔗 **Se estudia junto con:** Poseer, capex, punto de equilibrio, Precio fijo.

📘 **Dónde se aprende** (1 clase): [B124-C02 · Agencias científicas y empresas](../programa/clases/B124/B124-C02-agencias-cientificas-y-empresas/CLASE.md).

### Compras intermedias

- Las compras intermedias `A` son lo que una etapa compra a otra por unidad producida.

💡 **Cómo se explica en la clase [B124-C01](../programa/clases/B124/B124-C01-cadena-de-valor-de-industria-espacial/CLASE.md):**
- Distinguir producto bruto, compras intermedias, demanda final y valor agregado.
- 🎯 **Por qué importa:** El bloque necesita un mapa común antes de hablar de costos, financiamiento o contratos: ¿quién le compra a quién y dónde queda el valor? Ninguna clase anterior del programa trata la estructura económica de la industria espacial.
- 🔗 **Se estudia junto con:** producto bruto, demanda final, valor agregado, multiplicador.

📘 **Dónde se aprende** (1 clase): [B124-C01 · Cadena de valor de industria espacial](../programa/clases/B124/B124-C01-cadena-de-valor-de-industria-espacial/CLASE.md).

### Comprensión

- En el marco de Endsley (1995), la conciencia situacional tiene tres niveles: percepción de los elementos relevantes, comprensión de su significado y proyección de su estado futuro.

💡 **Cómo se explica en la clase [B111-C04](../programa/clases/B111/B111-C04-conciencia-situacional-en-operaciones-de-vuelo/CLASE.md):**
- Nombrar los tres niveles (percepción, comprensión, proyección).
- Los niveles 2 y 3: cubrir percepción no basta; se revisan la comprensión compartida y la proyección (modelos mentales, información, formación).
- 🎯 **Por qué importa:** Falta la clase que trate la conciencia situacional de la tripulación. La decisión central: ¿cómo se cuantifica lo que el equipo sabe y cada cuánto debe verificarlo para que no se quede desactualizado?
- 🔗 **Se estudia junto con:** conciencia situacional, percepción, proyección, puntuación tipo SAGAT.

📘 **Dónde se aprende** (1 clase): [B111-C04 · Conciencia situacional en operaciones de vuelo](../programa/clases/B111/B111-C04-conciencia-situacional-en-operaciones-de-vuelo/CLASE.md).

### Comprensión de lista

- Una comprensión de lista construye una lista nueva a partir de otra: `[x2 for x in lista if x > 0]`.

💡 **Cómo se explica en la clase [B07-C07](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md):**
- Usar `append`, `sort`/`sorted`, `len`, `in` y las comprensiones de lista.
- 🎯 **Por qué importa:** Una tabla de ocho planetas con tres propiedades cada uno son 24 datos: no cabe en 24 variables sueltas. Necesitas estructuras que agrupen datos, permitan recorrerlos y los mantengan ordenados y consultables.
- 🔗 **Se estudia junto con:** lista, tupla, inmutable, diccionario.

📘 **Dónde se aprende** (1 clase): [B07-C07 · Listas y estructuras de datos](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md).

### Compresión

- La compresión es la salida menor que la ideal.
- La compresión reduce los datos.
- La compresión de las capas añade conducción entre ellas y degrada el aislamiento.

💡 **Cómo se explica en la clase [B44-C10](../programa/clases/B44/B44-C10-no-linealidad-y-saturacion/CLASE.md):**
- X["flujo ideal"] --> R["respuesta con compresión"]
- Invierte la compresión con el coeficiente medido.
- 🎯 **Por qué importa:** Si la respuesta se curva, la fotometría se sesga mucho antes del pozo lleno. La decisión central: ¿hasta qué flujo puedo confiar en la respuesta lineal?
- 🔗 **Se estudia junto con:** linealidad, desviación, umbral de linealidad.

📘 **Dónde se aprende** (3 clases): [B44-C10 · No linealidad y saturación](../programa/clases/B44/B44-C10-no-linealidad-y-saturacion/CLASE.md); [B83-C11 · Presupuestos de datos](../programa/clases/B83/B83-C11-presupuestos-de-datos/CLASE.md); [B85-C06 · Aislamiento multicapa](../programa/clases/B85/B85-C06-aislamiento-multicapa/CLASE.md).

### Compresión de pulso

- La compresión de pulso correlaciona el eco con el pulso emitido.

💡 **Cómo se explica en la clase [B53-C24](../programa/clases/B53/B53-C24-sondeo-radar-de-penetracion-de-hielo/CLASE.md):**
- La compresión de pulso da un ancho a mitad de potencia de `7,44 m` (teórico `7,48 m`).
- 🎯 **Por qué importa:** Un eco sin escala de profundidad no dice nada. La decisión central: ¿a qué profundidad está una interfaz según su retardo y qué separación mínima permite distinguir dos interfaces?
- 🔗 **Se estudia junto con:** profundidad, resolución en rango, ancho a mitad de potencia.

📘 **Dónde se aprende** (1 clase): [B53-C24 · Sondeo radar de penetración de hielo](../programa/clases/B53/B53-C24-sondeo-radar-de-penetracion-de-hielo/CLASE.md).

### Compresión de vapor

- Salmuera: residuo concentrado. Compresión de vapor: destilación con reutilización de calor.

💡 **Contexto en la clase [B106-C27](../programa/clases/B106/B106-C27-tratamiento-de-orina-y-recuperacion-de-agua/CLASE.md):**
- 🎯 **Por qué importa:** Evaporar la orina concentra sales hasta que precipitan y obstruyen el equipo; el límite lo fija la química, no la termodinámica del agua. La decisión central: ¿hasta qué fracción se puede recuperar el agua antes de precipitar y cómo se supera ese límite?
- 🔗 **Se estudia junto con:** Orina pretratada, Producto iónico (IP), K_sp, Salmuera.

📘 **Dónde se aprende** (1 clase): [B106-C27 · Tratamiento de orina y recuperación de agua](../programa/clases/B106/B106-C27-tratamiento-de-orina-y-recuperacion-de-agua/CLASE.md).

### Compresión en alcance

- La compresión en alcance es el filtro adaptado en el tiempo rápido; la compresión en azimut lo es en el tiempo lento.

💡 **Cómo se explica en la clase [B69-C02](../programa/clases/B69/B69-C02-formacion-de-imagenes-sar/CLASE.md):**
- RAW["eco crudo"] --> RC["compresión en alcance"]
- 🎯 **Por qué importa:** Sin procesamiento, un eco crudo parece ruido. La decisión central: ¿qué operaciones convierten el eco crudo en una imagen con la resolución teórica, y cuándo fallan?
- 🔗 **Se estudia junto con:** chirp, compresión en azimut, migración de celda, RCMC.

📘 **Dónde se aprende** (1 clase): [B69-C02 · Formación de imágenes SAR](../programa/clases/B69/B69-C02-formacion-de-imagenes-sar/CLASE.md).

### Compresión en azimut

- La compresión en alcance es el filtro adaptado en el tiempo rápido; la compresión en azimut lo es en el tiempo lento.

💡 **Cómo se explica en la clase [B69-C02](../programa/clases/B69/B69-C02-formacion-de-imagenes-sar/CLASE.md):**
- Si no se corrige, la energía de un blanco se reparte en varias celdas y la compresión en azimut integra menos aperturas útiles.
- 🎯 **Por qué importa:** Sin procesamiento, un eco crudo parece ruido. La decisión central: ¿qué operaciones convierten el eco crudo en una imagen con la resolución teórica, y cuándo fallan?
- 🔗 **Se estudia junto con:** chirp, compresión en alcance, migración de celda, RCMC.

📘 **Dónde se aprende** (1 clase): [B69-C02 · Formación de imágenes SAR](../programa/clases/B69/B69-C02-formacion-de-imagenes-sar/CLASE.md).

### Compresión sin pérdida

- La compresión sin pérdida (aquí `gzip`) reduce el espacio sin cambiar ningún valor.

💡 **Cómo se explica en la clase [B14-C07](../programa/clases/B14/B14-C07-hdf5-y-almacenamiento-cientifico/CLASE.md):**
- Verificar que la compresión sin pérdida devuelve exactamente los mismos datos.
- ⚠️ **Error frecuente:** No declarar una compresión con pérdida. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Una simulación o un instrumento moderno produce series de millones de muestras con sus metadatos. Guardarlas en texto es lento y pesado; cargarlas enteras en memoria para leer un fragmento es inviable.
- 🔗 **Se estudia junto con:** grupo, dataset, atributo, fragmento.

📘 **Dónde se aprende** (1 clase): [B14-C07 · HDF5 y almacenamiento científico](../programa/clases/B14/B14-C07-hdf5-y-almacenamiento-cientifico/CLASE.md).

### Comprobación

- La comprobación es sustituir la solución y verificar que la igualdad se cumple dentro de la tolerancia declarada.

💡 **Cómo se explica en la clase [B04-C02](../programa/clases/B04/B04-C02-ecuaciones-lineales-y-cuadraticas/CLASE.md):**
- Un método por tanteo (probar valores) solo sirve de comprobación.
- 🎯 **Por qué importa:** Una sonda desciende hacia la Luna; un instrumento cae desde una mesa de trabajo; una señal de radio viaja hasta un espejo y vuelve. En cada caso hay un número que no conoces (un tiempo, una distancia) y una relación que lo liga a otros que sí conoces.
- 🔗 **Se estudia junto con:** ecuación, resolverla, lineal, cuadrática.

📘 **Dónde se aprende** (1 clase): [B04-C02 · Ecuaciones lineales y cuadráticas](../programa/clases/B04/B04-C02-ecuaciones-lineales-y-cuadraticas/CLASE.md).

### Comprobación de conservación

- La comprobación de conservación compara magnitudes antes y después de cada evento.

💡 **Cómo se explica en la clase [B52-C20](../programa/clases/B52/B52-C20-simulacion-de-formacion-planetaria-simplificada/CLASE.md):**
- Descripción larga: doce embriones se reducen a cinco y todas las comprobaciones de conservación y de energía por fusión se cumplen a precisión de máquina.
- 🎯 **Por qué importa:** Una simulación de formación sin sus controles de conservación no es evidencia de nada. La decisión central: ¿qué comprobaciones demuestran que la simulación se ejecutó correctamente antes de interpretar su resultado?
- 🔗 **Se estudia junto con:** fusión perfectamente inelástica, espín, radio de fusión inflado.

📘 **Dónde se aprende** (1 clase): [B52-C20 · Simulación de formación planetaria simplificada](../programa/clases/B52/B52-C20-simulacion-de-formacion-planetaria-simplificada/CLASE.md).

### Comprometido

- El comprometido (*obligated*) es dinero ya asignado contractualmente.

💡 **Cómo se explica en la clase [B124-C06](../programa/clases/B124/B124-C06-financiamiento-publico/CLASE.md):**
- El informe IG-20-005 de la OIG de la NASA (14 de noviembre de 2019) cuenta que, en agosto de 2019, el programa de tripulación comercial había comprometido unos 5 500 millones de USD de los 8 500 millones adjudicados (`64,7%`) y llevaba años de retraso.
- Dato consultado (NASA OIG IG-20-005, 2019): comprometido/adjudicado = 5500/8500 = 64.7 %
- 🎯 **Por qué importa:** Un proyecto puede estar bien estimado y aun así fallar porque el dinero no llega al ritmo que necesita. La decisión central: ¿qué tope anual evita el atraso y cuánto cuesta cada año de espera?
- 🔗 **Se estudia junto con:** demanda acumulada, tope, atraso, costo de espera.

📘 **Dónde se aprende** (1 clase): [B124-C06 · Financiamiento público](../programa/clases/B124/B124-C06-financiamiento-publico/CLASE.md).

### Compromiso

- El compromiso cobertura–profundidad.

💡 **Cómo se explica en la clase [B28-C15](../programa/clases/B28/B28-C15-busqueda-de-contrapartidas-opticas/CLASE.md):**
- El script [teselado.py](teselado.py) construye el mapa, aplica el algoritmo voraz (comprueba cociente `≥ 1 − 1/e`) y resuelve el compromiso.
- 🎯 **Por qué importa:** Observar más campos cubre más probabilidad, pero cada campo recibe menos tiempo y es menos profundo. Si la fuente es débil, el exceso de campos hace que no se vea.
- 🔗 **Se estudia junto con:** teselado, algoritmo voraz, garantía 1 − 1/e, profundidad.

📘 **Dónde se aprende** (1 clase): [B28-C15 · Búsqueda de contrapartidas ópticas](../programa/clases/B28/B28-C15-busqueda-de-contrapartidas-opticas/CLASE.md).
