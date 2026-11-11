# Términos · D (parte 2 de 3)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · **D** · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-d.md) · **2** · [3](terminos-d-3.md)

### Desviación no ETL

- Una desviación no ETL es cualquier diferencia respecto de ellas.

💡 **Cómo se explica en la clase [B32-C02](../programa/clases/B32/B32-C02-equilibrio-termodinamico-local-y-desviaciones-no-lte/CLASE.md):**
- python programa/clases/B32/B32-C02-equilibrio-termodinamico-local-y-desviaciones-no-lte/lte.py
- 🎯 **Por qué importa:** Si el ETL falla, las abundancias que se derivan son erróneas. La decisión central: ¿cuánto hidrógeno está ionizado a cada temperatura y densidad?
- 🔗 **Se estudia junto con:** ecuación de Boltzmann, ecuación de Saha, fracción ionizada, ETL.

📘 **Dónde se aprende** (1 clase): [B32-C02 · Equilibrio termodinámico local y desviaciones no LTE](../programa/clases/B32/B32-C02-equilibrio-termodinamico-local-y-desviaciones-no-lte/CLASE.md).

### Desviación relativa de frecuencia

- La desviación relativa de frecuencia `y = (ν − ν₀)/ν₀` es adimensional.

💡 **Cómo se explica en la clase [B13-C06](../programa/clases/B13/B13-C06-patrones-de-longitud-y-tiempo/CLASE.md):**
- Y el reloj que cronometra el viaje debe mantener su frecuencia con una desviación relativa suficientemente pequeña durante el tiempo entre las calibraciones.
- Convertir una desviación relativa de frecuencia en error de tiempo acumulado.
- 🎯 **Por qué importa:** Cuando un telémetro láser mide la distancia a la Luna, lo que mide es el tiempo que tarda un pulso en ir y volver. Un error de un nanosegundo en ese tiempo equivale a 15 centímetros de distancia.
- 🔗 **Se estudia junto con:** segundo, metro, realización, tiempo de vuelo.

📘 **Dónde se aprende** (1 clase): [B13-C06 · Patrones de longitud y tiempo](../programa/clases/B13/B13-C06-patrones-de-longitud-y-tiempo/CLASE.md).

### Desviación residual

- La desviación residual es `s = √(S/(N − p))`, con `p` parámetros.
- La desviación residual `s` estima el ruido a partir de los residuos.

💡 **Cómo se explica en la clase [B13-C05](../programa/clases/B13/B13-C05-calibracion-instrumental/CLASE.md):**
- La desviación residual es `s = √[Σrᵢ²/(n − 2)]` (se pierden dos grados de libertad por estimar `a` y `b`).
- Calcular la desviación residual y las incertidumbres de pendiente y ordenada.
- 🎯 **Por qué importa:** Un sensor solar de una nave devuelve cuentas digitales (DN), no vatios por metro cuadrado. Para saber cuánta luz recibe hay que haberlo expuesto antes a fuentes de irradiancia conocida y haber establecido la relación entre ambas.
- 🔗 **Se estudia junto con:** calibración, indicación, curva de calibración, mínimos cuadrados ordinarios.

📘 **Dónde se aprende** (2 clases): [B13-C05 · Calibración instrumental](../programa/clases/B13/B13-C05-calibracion-instrumental/CLASE.md); [B15-C16 · Ajuste de curvas](../programa/clases/B15/B15-C16-ajuste-de-curvas/CLASE.md).

### Desviación robusta

- La desviación robusta es `1,4826·MAD`.

💡 **Cómo se explica en la clase [B103-C03](../programa/clases/B103/B103-C03-mapas-de-profundidad-y-correspondencia-estereo/CLASE.md):**
- El laboratorio mide `σ_d` en el suelo por rango (0,318; 0,272; 0,296 y 0,229 px) y la desviación robusta de `Z` coincide con la fórmula (cociente 1,00; 0,97; 0,99; 0,99).
- La desviación global de `d` es 1,105 px y la robusta de 0,3 px: la diferencia son las colas.
- ⚠️ **Error frecuente:** Confundir RMSE con desviación robusta. Las colas dominan el RMSE (8.4).
- 🎯 **Por qué importa:** La profundidad estéreo es barata y densa, pero su error crece con el cuadrado de la distancia: a 20 m una incertidumbre de 0,3 px en la disparidad son 71 cm. La decisión central: ¿hasta qué distancia se puede confiar en el mapa de profundidad para decidir si un camino es seguro, y qué línea de base lo permite?
- 🔗 **Se estudia junto con:** disparidad, correspondencia por bloques, línea de base, refinamiento subpixel.

📘 **Dónde se aprende** (1 clase): [B103-C03 · Mapas de profundidad y correspondencia estéreo](../programa/clases/B103/B103-C03-mapas-de-profundidad-y-correspondencia-estereo/CLASE.md).

### Desviación típica

- La desviación típica `σ` es su raíz cuadrada positiva (S1, C.2.12); tiene la unidad de la variable.

💡 **Cómo se explica en la clase [B12-C04](../programa/clases/B12/B12-C04-esperanza-y-varianza/CLASE.md):**
- La constante `b` desplaza pero no cambia la dispersión; el factor `a` la multiplica por `a²` (y la desviación típica por `|a|`).
- Las desviaciones típicas no se suman (serían 7 m): se suman las varianzas, como los lados de un triángulo rectángulo.
- 🎯 **Por qué importa:** Un ingeniero no maneja distribuciones completas; maneja «la medida es 150,0 m con una incertidumbre de 3 m». Esa frase usa exactamente una esperanza y una desviación típica.
- 🔗 **Se estudia junto con:** esperanza, varianza, estimador, desviación típica experimental.

📘 **Dónde se aprende** (1 clase): [B12-C04 · Esperanza y varianza](../programa/clases/B12/B12-C04-esperanza-y-varianza/CLASE.md).

### Desviación típica de la media

- La desviación típica de la media de `n` lecturas independientes es `σ/√n` (S2, 4.2.3).

💡 **Cómo se explica en la clase [B13-C04](../programa/clases/B13/B13-C04-errores-sistematicos-y-aleatorios/CLASE.md):**
- Ejercicio 8. Dos métodos independientes miden el mismo pulso: `12,515 ± 0,003 ms` y `12,500 ± 0,003 ms` (±: desviación típica de la media).
- 🎯 **Por qué importa:** Una estación mide el instante de llegada de un pulso de una baliza. Cada lectura fluctúa por ruido electrónico, y además hay un retardo constante del cable que nadie incluyó.
- 🔗 **Se estudia junto con:** error de medida, error sistemático, error aleatorio, sesgo.

📘 **Dónde se aprende** (1 clase): [B13-C04 · Errores sistemáticos y aleatorios](../programa/clases/B13/B13-C04-errores-sistematicos-y-aleatorios/CLASE.md).

### Desviación típica de las frecuencias

- La desviación típica de las frecuencias `σ_ν = Δν/√12`.

💡 **Contexto en la clase [B51-C04](../programa/clases/B51/B51-C04-respuesta-de-banda-y-errores-dependientes-de-la-frecuencia/CLASE.md):**
- **Idea central (modelo mental):** Como una cuerda tensada que además tiembla: la inclinación general es el retardo y el temblor regular es el eco del cable; cada uno se lee con su propia herramienta.
- 🎯 **Por qué importa:** Un error de banda aparece en las líneas espectrales como una falsa estructura y limita el rango dinámico del continuo. La decisión central: ¿qué parte del error de banda es un retardo, qué parte una ondulación, y con qué precisión se miden?
- 🔗 **Se estudia junto con:** respuesta de banda, retardo residual, ondulación, ancho de banda.

📘 **Dónde se aprende** (1 clase): [B51-C04 · Respuesta de banda y errores dependientes de la frecuencia](../programa/clases/B51/B51-C04-respuesta-de-banda-y-errores-dependientes-de-la-frecuencia/CLASE.md).

### Desviación típica experimental

- Un estimador del valor esperado a partir de `n` observaciones independientes en las mismas condiciones es la media aritmética (S1, 4.2.1); la desviación típica experimental estima `σ` con denominador `n − 1` (S1, 4.2.2).

💡 **Contexto en la clase [B12-C04](../programa/clases/B12/B12-C04-esperanza-y-varianza/CLASE.md):**
- **Idea central (modelo mental):** La esperanza es el punto de equilibrio de la distribución, como el centro de masa de una barra con pesos; la varianza es su momento de inercia respecto de ese centro, y la desviación típica su radio de giro.
- 🎯 **Por qué importa:** Un ingeniero no maneja distribuciones completas; maneja «la medida es 150,0 m con una incertidumbre de 3 m». Esa frase usa exactamente una esperanza y una desviación típica.
- 🔗 **Se estudia junto con:** esperanza, varianza, desviación típica, estimador.

📘 **Dónde se aprende** (1 clase): [B12-C04 · Esperanza y varianza](../programa/clases/B12/B12-C04-esperanza-y-varianza/CLASE.md).

### Desviación típica s

- La desviación típica `s` de `n` lecturas es `√[Σ(xᵢ − x̄)²/(n−1)]`.

💡 **Cómo se explica en la clase [B13-C03](../programa/clases/B13/B13-C03-exactitud-frente-a-precision/CLASE.md):**
- El sesgo responde «¿en promedio, dónde caigo respecto de la referencia?»; la desviación típica responde «¿cuánto se agrupan mis lecturas entre sí?».
- No se escribe «el instrumento tiene una exactitud de 0,05 m» como si la exactitud fuera un número (lo desaconseja la propia definición, S1, 2.13, nota 1); se escribe «sesgo `+0,200 m`, desviación típica `0,005 m` respecto a la referencia, n = 2000».
- 🎯 **Por qué importa:** Un telémetro láser que mide la distancia a un reflector de prueba puede dar lecturas muy agrupadas pero todas desplazadas: es repetible y, aun así, está mal. Otro puede dar lecturas dispersas que, en promedio, caen sobre el valor correcto.
- 🔗 **Se estudia junto con:** exactitud de medida, veracidad, precisión de medida, error de medida.

📘 **Dónde se aprende** (1 clase): [B13-C03 · Exactitud frente a precisión](../programa/clases/B13/B13-C03-exactitud-frente-a-precision/CLASE.md).

### Detección

- Una detección es un máximo local de la imagen filtrada sobre el umbral.
- La tasa de falsa alarma es la probabilidad de marcar un píxel sin cambio; la de detección, la de marcar uno con cambio.
- La detección es que el error se advierta; la corrección, que se acepte y se repare.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C20](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md):**
- (R3) a lo sumo una detección falsa en toda la secuencia;
- (R4) RMSE de la pista menor que el de las detecciones sin filtrar;
- 🎯 **Por qué importa:** Detectar y seguir un objeto móvil —un asteroide, un fragmento de basura espacial, un satélite— combina varios problemas: la cámara no apunta exactamente igual en cada imagen, las estrellas fijas saturan la escena, el objeto es débil y la medida es ruidosa.
- 🔗 **Se estudia junto con:** requisito, prueba de extremo a extremo, mediana temporal, imagen de diferencia.

📘 **Dónde se aprende** (8 clases): [B15-C20 · Proyecto de detección y seguimiento](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md); [B51-C13 · Marcado de datos espurios e interferencia en visibilidades](../programa/clases/B51/B51-C13-marcado-de-datos-espurios-e-interferencia-en-visibilidades/CLASE.md); [B57-C27 · Detección de cambios en series de imágenes](../programa/clases/B57/B57-C27-deteccion-de-cambios-en-series-de-imagenes/CLASE.md); [B88-C40 · Auditoría de software espacial](../programa/clases/B88/B88-C40-auditoria-de-software-espacial/CLASE.md); [B96-C25 · Seguridad física y control de acceso de estaciones terrestres](../programa/clases/B96/B96-C25-seguridad-fisica-y-control-de-acceso-de-estaciones-terrestres/CLASE.md); [B104-C07 · Factores de liderazgo](../programa/clases/B104/B104-C07-factores-de-liderazgo/CLASE.md) y 2 más.

### Detección a 5σ

- La detección a 5σ exige `δ ≥ 5σ/√n`.

💡 **Contexto en la clase [B29-C11](../programa/clases/B29/B29-C11-atmosferas-exoplanetarias/CLASE.md):**
- **Idea central (modelo mental):** Una moneda con un halo borroso tapa un poco más que la moneda sola. El ancho del halo es el espesor de la atmósfera efectiva, de unas cuantas alturas de escala.
- 🎯 **Por qué importa:** Los planetas inflados y calientes tienen señales de cientos de ppm; las Tierras alrededor de estrellas como el Sol, de ~1 ppm, que no se alcanzan. La decisión central: ¿qué señal produce una atmósfera dada y cuántos tránsitos hacen falta para verla?
- 🔗 **Se estudia junto con:** altura de escala, masa molecular media, señal de transmisión, anillo atmosférico.

📘 **Dónde se aprende** (1 clase): [B29-C11 · Atmósferas exoplanetarias](../programa/clases/B29/B29-C11-atmosferas-exoplanetarias/CLASE.md).

### Detección activa de fuego

- Una detección activa de fuego marca un píxel con uno o más focos.

💡 **Contexto en la clase [B57-C16](../programa/clases/B57/B57-C16-incendios-forestales/CLASE.md):**
- **Idea central (modelo mental):** Una vela casi no calienta el salón, pero si miras con una cámara sensible al calor intenso la ves de lejos. El infrarrojo medio es esa cámara.
- 🎯 **Por qué importa:** Un incendio pequeño puede ser un desastre en horas, pero un píxel mide cientos de metros. La decisión central: ¿cuál es la fracción de píxel más pequeña que se puede detectar y cuánto sesga la estimación un error en el fondo?
- 🔗 **Se estudia junto con:** fracción de píxel, banda de infrarrojo medio, infrarrojo térmico, radiancia mixta.

📘 **Dónde se aprende** (1 clase): [B57-C16 · Incendios forestales](../programa/clases/B57/B57-C16-incendios-forestales/CLASE.md).

### Detección de fotones

- La detección de fotones cuenta fotones por ranura.

💡 **Contexto en la clase [B89-C18](../programa/clases/B89/B89-C18-comunicaciones-opticas-espaciales/CLASE.md):**
- 🎯 **Por qué importa:** Las comunicaciones ópticas prometen más tasa por masa y potencia que la radio; entender el presupuesto de fotones y la modulación por posición de pulso explica por qué y a qué costo (apuntamiento, nubes). La decisión central: ¿cuántos fotones por bit llegan y qué error de símbolo implica la modulación PPM elegida?
- 🔗 **Se estudia junto con:** banda C óptica, PPM de orden M, error de símbolo sin fondo, fotones por bit.

📘 **Dónde se aprende** (1 clase): [B89-C18 · Comunicaciones ópticas espaciales](../programa/clases/B89/B89-C18-comunicaciones-opticas-espaciales/CLASE.md).

### Detección directa

- La detección directa convierte la intensidad en señal.

💡 **Contexto en la clase [B92-C05](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md):**
- 🎯 **Por qué importa:** Un detector de imagen integra luz durante milisegundos; uno de comunicaciones decide, en nanosegundos, en qué ranura llegó el pulso. La decisión central: ¿cuántos fotones hacen falta por símbolo y qué detector soporta la tasa de ranuras sin saturarse?
- 🔗 **Se estudia junto con:** conteo de fotones, eficiencia de detección, conteos oscuros, fondo.

📘 **Dónde se aprende** (1 clase): [B92-C05 · Receptores y detectores para comunicaciones ópticas](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md).

### Detección falsa

- Una detección falsa no corresponde al objeto.

💡 **Cómo se explica en la clase [B15-C20](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md):**
- (R3) a lo sumo una detección falsa en toda la secuencia;
- Resultado: `12 de 12` detecciones del objeto y `0` falsas (R2 y R3 cumplidos).
- 🎯 **Por qué importa:** Detectar y seguir un objeto móvil —un asteroide, un fragmento de basura espacial, un satélite— combina varios problemas: la cámara no apunta exactamente igual en cada imagen, las estrellas fijas saturan la escena, el objeto es débil y la medida es ruidosa.
- 🔗 **Se estudia junto con:** requisito, prueba de extremo a extremo, mediana temporal, imagen de diferencia.

📘 **Dónde se aprende** (1 clase): [B15-C20 · Proyecto de detección y seguimiento](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md).

### Detección por FFT

- La detección por FFT integra `N` muestras: el bin de la portadora acumula `N` veces la potencia y el ruido por bin tiene media `σ²N`.

💡 **Cómo se explica en la clase [B89-C24](../programa/clases/B89/B89-C24-recepcion-de-telemetria-debil/CLASE.md):**
- Con una FFT de 1024 muestras (T = 64 s) y falsa alarma de 10⁻³, la detección sintética pasa de `0,02` a −12 dB-Hz a `0,98` a −4 dB-Hz.
- Descripción larga: la detección pasa de casi nula a casi segura en pocos decibelios; estrechar el lazo o integrar más baja el `C/N₀` mínimo.
- 🎯 **Por qué importa:** Cuando una nave está lejos o en emergencia, recibir su portadora a unos pocos dB-Hz marca la diferencia entre confirmar su estado o perderla; el costo es tiempo de integración o un lazo difícil de enganchar. La decisión central: ¿cómo detectar y seguir una portadora muy débil sin tantas falsas alarmas?
- 🔗 **Se estudia junto con:** SNR del lazo, umbral de seguimiento, falsa alarma, tiempo de integración.

📘 **Dónde se aprende** (1 clase): [B89-C24 · Recepción de telemetría débil](../programa/clases/B89/B89-C24-recepcion-de-telemetria-debil/CLASE.md).

### Detector

- Un detector es un sensor que registra luz (ojo, película, sensor digital).

💡 **Cómo se explica en la clase [B01-C10](../programa/clases/B01/B01-C10-limitaciones-de-los-sentidos-humanos/CLASE.md):**
- Por eso la astronomía usa detectores para otras regiones, algunos solo desde el espacio por el bloqueo atmosférico (S1).
- El detector también importa: uno digital puede acumular luz durante segundos o minutos en una exposición, algo que el ojo no hace de la misma manera (explicación nuestra).
- 🎯 **Por qué importa:** Si el ojo bastara, no habría observatorios. La luz visible es una franja pequeña del espectro electromagnético (S1, S2); además, tu pupila recoge poca luz, separa detalles hasta cierto tamaño y puede engañarte.
- 🔗 **Se estudia junto con:** rango espectral, sensibilidad, apertura, resolución angular.

📘 **Dónde se aprende** (1 clase): [B01-C10 · Limitaciones de los sentidos humanos](../programa/clases/B01/B01-C10-limitaciones-de-los-sentidos-humanos/CLASE.md).

### Determinación de órbitas

- La determinación de órbitas estima los elementos a partir de observaciones.

💡 **Cómo se explica en la clase [B58-C07](../programa/clases/B58/B58-C07-determinacion-de-orbitas/CLASE.md):**
- python programa/clases/B58/B58-C07-determinacion-de-orbitas/orbita.py
- 🎯 **Por qué importa:** Una órbita ajustada es el producto central de la defensa planetaria: de ella salen las predicciones y las probabilidades. La decisión central: ¿cuántas observaciones y qué arco hacen falta para que la órbita sea fiable, y cómo se sabe que el ajuste es bueno?
- 🔗 **Se estudia junto con:** Levenberg–Marquardt, arco, residuos, covarianza formal.

📘 **Dónde se aprende** (1 clase): [B58-C07 · Determinación de órbitas](../programa/clases/B58/B58-C07-determinacion-de-orbitas/CLASE.md).

### Determinante

- El determinante de `[[a, b], [c, d]]` es `ad − bc`; el de una matriz `3×3` se obtiene por expansión por cofactores: se desarrolla por una fila sumando cada elemento por el determinante de la submatriz que queda al tachar su fila y columna, con signo alterno (S1, §1.3(i), ecs. 1.3.1–1.3.4).
- Es ortogonal (`Rᵀ R = I`) y tiene determinante `+1`.

💡 **Cómo se explica en la clase [B04-C15](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md):**
- *Descripción textual:* de las componentes ecuatoriales se pasa a las eclípticas con la rotación pasiva `R_x(ε)`; la traspuesta devuelve las ecuatoriales; de las eclípticas salen longitud y latitud con `atan2` y `arcsen`; y la matriz se comprueba con ortogonalidad y determinante 1.
- Comprobar que una matriz es una rotación: ortogonal y con determinante +1.
- ⚠️ **Error frecuente:** No comprobar la matriz. Se corrige con la ortogonalidad y el determinante (ejercicio 2).
- 🎯 **Por qué importa:** El ecuador de la Tierra y el plano de su órbita (la eclíptica) forman un ángulo de unos 23,4°. Los catálogos de estrellas se dan en coordenadas ecuatoriales; el movimiento del Sol, la Luna y los planetas es más simple en coordenadas eclípticas.
- 🔗 **Se estudia junto con:** matriz de rotación, ortogonal, inversa, traspuesta.

📘 **Dónde se aprende** (2 clases): [B04-C15 · Rotación de puntos y ejes](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md); [B10-C04 · Determinantes y soluciones](../programa/clases/B10/B10-C04-determinantes-y-soluciones/CLASE.md).

### Determinismo

- El determinismo exige la misma semilla y el mismo orden de operaciones.

💡 **Cómo se explica en la clase [B97-C23](../programa/clases/B97/B97-C23-diseno-de-simulador-de-mision-robotica/CLASE.md):**
- SEM["semilla fija"] --> D["determinismo"]
- 🎯 **Por qué importa:** Una simulación sin verificar produce números bonitos y erróneos. Cinco pruebas baratas (solución analítica, orden de convergencia, estabilidad, conservación y repetibilidad) detectan casi todos los errores de un integrador antes de poner modelos complejos encima.
- 🔗 **Se estudia junto con:** paso de integración, Euler explícito, RK4, orden.

📘 **Dónde se aprende** (1 clase): [B97-C23 · Diseño de simulador de misión robótica](../programa/clases/B97/B97-C23-diseno-de-simulador-de-mision-robotica/CLASE.md).

### Detrimento

- El detrimento nominal combinado de cáncer y efectos hereditables es de unos 5 % por Sv (ICRP 103).
- El detrimento cuantifica el daño sobre la salud por cáncer y efectos hereditables.

💡 **Cómo se explica en la clase [B112-C04](../programa/clases/B112/B112-C04-efectos-cronicos-y-carcinogenesis-por-radiacion/CLASE.md):**
- ICRP 103 mantiene la hipótesis de respuesta lineal a dosis bajas para cáncer y efectos hereditables y estima un detrimento nominal de alrededor del 5 % por Sv, con un DDREF de 2 para cánceres sólidos (extracto consultado).
- 🎯 **Por qué importa:** Ninguna clase cubre riesgo de cáncer y efectos tardíos. Los límites de carrera de una misión se expresan como riesgo, no como umbral, y sin entender cómo se estima y cuán incierta es esa estimación, un límite en mSv parece más preciso de lo que es.
- 🔗 **Se estudia junto con:** modelo lineal sin umbral, riesgo de exceso, DDREF, efecto estocástico.

📘 **Dónde se aprende** (2 clases): [B112-C02 · Dosis equivalente y dosis efectiva](../programa/clases/B112/B112-C02-dosis-equivalente-y-dosis-efectiva/CLASE.md); [B112-C04 · Efectos crónicos y carcinogénesis por radiación](../programa/clases/B112/B112-C04-efectos-cronicos-y-carcinogenesis-por-radiacion/CLASE.md).

### Detuning

- El detuning es reducir las ganancias respecto de una receta para ganar margen.
- El detuning `Δ` es la desintonía.

💡 **Cómo se explica en la clase [B31-C03](../programa/clases/B31/B31-C03-estados-y-observables-cuanticos/CLASE.md):**
- Con detuning, la población máxima baja a `Ω²/(Ω² + Δ²) = 0,610` y la frecuencia sube a `√(Ω² + Δ²) = 1,281`.
- Descripción larga: sin detuning la población llega a 1; con detuning se queda en 0,61 como máximo.
- 🎯 **Por qué importa:** Un cúbit, un espín o un átomo de dos niveles obedecen estas reglas, y la medida cambia el estado. La decisión central: ¿cómo se calculan probabilidades y evolución en un sistema de dos niveles?
- 🔗 **Se estudia junto con:** matriz de Pauli, regla de Born, oscilación de Rabi, desigualdad de Robertson.

📘 **Dónde se aprende** (2 clases): [B16-C12 · Sintonía de controladores PID](../programa/clases/B16/B16-C12-sintonia-de-controladores-pid/CLASE.md); [B31-C03 · Estados y observables cuánticos](../programa/clases/B31/B31-C03-estados-y-observables-cuanticos/CLASE.md).

### Deuda de sueño

- La deuda de sueño es lo que se deja de dormir respecto de la necesidad.

💡 **Contexto en la clase [B104-C17](../programa/clases/B104/B104-C17-gestion-de-fatiga/CLASE.md):**
- 🎯 **Por qué importa:** NASA reconoce la pérdida de sueño, la desincronización circadiana y la sobrecarga como un riesgo del vuelo. La decisión conceptual: ¿cuánta alerta se pierde en el trabajo diurno al acortar el sueño unas horas, y por qué el modelo no sustituye a la medición?
- 🔗 **Se estudia junto con:** presión de sueño, ritmo circadiano, alerta, desincronización circadiana.

📘 **Dónde se aprende** (1 clase): [B104-C17 · Gestión de fatiga](../programa/clases/B104/B104-C17-gestion-de-fatiga/CLASE.md).

### Devolución

- La devolución es la restitución del personal o del objeto.

💡 **Cómo se explica en la clase [B119-C02](../programa/clases/B119/B119-C02-acuerdo-de-salvamento/CLASE.md):**
- Enunciar los deberes generales de notificación, auxilio y devolución, rotulando que el texto del Acuerdo no se consultó.
- ¿Qué dato del Acuerdo sobre la Luna remite al régimen de devolución?
- 🎯 **Por qué importa:** El tratado de 1967 (C01) menciona la asistencia a los astronautas (art. V, no discutido en la fuente consultada); el Acuerdo de Salvamento la desarrolla, y ninguna otra clase la cubre.
- 🔗 **Se estudia junto con:** autoridad de lanzamiento, notificación, banda alcanzable.

📘 **Dónde se aprende** (1 clase): [B119-C02 · Acuerdo de Salvamento](../programa/clases/B119/B119-C02-acuerdo-de-salvamento/CLASE.md).

### Devolución de resultados

- La devolución de resultados es entregar a la comunidad lo producido, de modo que lo pueda usar.

💡 **Contexto en la clase [B133-C03](../programa/clases/B133/B133-C03-colaboracion-con-comunidades-en-investigacion-y-educacion/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR C["consulta"] --> A["acuerdo"] A --> R["recolección"] R --> V["revisión comunitaria"] V --> P["publicación"] V --> D["devolución"] ``` *Descripción textual:* primero se consulta, luego se acuerda, después se recoge; los resultados vuelven a la comunidad para su revisión, y solo entonces se publican o se devuelven en su forma final.
- 🎯 **Por qué importa:** Los saberes del cielo han sido registrados muchas veces sin que las comunidades decidieran qué, cómo ni para qué. La decisión central: ¿qué debe estar acordado, y en qué orden, antes de recoger, usar o enseñar un saber ajeno?
- 🔗 **Se estudia junto con:** consentimiento libre, previo e informado, principios CARE, portador del saber, protocolo.

📘 **Dónde se aprende** (1 clase): [B133-C03 · Colaboración con comunidades en investigación y educación](../programa/clases/B133/B133-C03-colaboracion-con-comunidades-en-investigacion-y-educacion/CLASE.md).

### Dex

- Un dex es una diferencia de un factor 10 en una escala logarítmica.
- Un dex es una unidad logarítmica: una diferencia de 1 dex es un factor 10.
- Un dex es un factor 10 en el logaritmo.

💡 **Cómo se explica en la clase [B01-C14](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md):**
- En logaritmo, `−0,307`; la tabla publica `−0,305`: coincide dentro de 0,002 dex.
- Antes comprueba que `σ` derivada coincide con CODATA 2014 (1 × 10⁻⁵), que la luminosidad solar calculada coincide con la nominal (0,2 %), que el flujo a 1 au es 1 361 W/m² (±2) y que las cinco estrellas coinciden en menos de 0,10 dex; si no, se detiene.
- 🎯 **Por qué importa:** Dos estrellas pueden verse igual de brillantes y ser totalmente distintas: una pequeña y cercana, otra enorme y lejana (C09). Para saber cómo es una estrella necesitas separar lo que ves (flujo) de lo que ella es (luminosidad, temperatura, radio) y de dónde está (distancia).
- 🔗 **Se estudia junto con:** temperatura efectiva, luminosidad, radio, constante de Stefan–Boltzmann.

📘 **Dónde se aprende** (3 clases): [B01-C14 · Estrellas y sus principales propiedades](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md); [B06-C20 · Análisis químico introductorio de meteoritos](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md); [B55-C01 · Abundancia química cósmica](../programa/clases/B55/B55-C01-abundancia-quimica-cosmica/CLASE.md).

### DFT

- La DFT es la transformada de Fourier discreta.

💡 **Cómo se explica en la clase [B31-C04](../programa/clases/B31/B31-C04-principio-de-incertidumbre/CLASE.md):**
- Calcular `σ_x` y `σ_p` de un paquete gaussiano con una DFT.
- Ejercicio 10 · transferencia. Transferencia. ¿Por qué una DFT necesita la malla en 40 unidades?
- 🎯 **Por qué importa:** La incertidumbre explica el tamaño de los átomos y la energía de punto cero. La decisión central: ¿cuánto vale el producto de incertidumbres de un estado y qué energía implica un confinamiento?
- 🔗 **Se estudia junto con:** incertidumbre, paquete gaussiano, caja, energía de punto cero.

📘 **Dónde se aprende** (1 clase): [B31-C04 · Principio de incertidumbre](../programa/clases/B31/B31-C04-principio-de-incertidumbre/CLASE.md).

### Día

- El minuto (min), la hora (h) y el día (d) se aceptan con las equivalencias `1 min = 60 s`, `1 h = 60 min = 3600 s`, `1 d = 24 h = 86 400 s` (S2).

💡 **Cómo se explica en la clase [B03-C08](../programa/clases/B03/B03-C08-tiempo-y-conversiones-astronomicas/CLASE.md):**
- Una vuelta completa son `360°` y un día de rotación `24 h`; por tanto, `360°/24 h = 15°/h`.
- En un día solar de 24 h gira `360,985°`: casi un grado más que una vuelta, que es la razón de fondo por la que el día sidéreo es más corto (B01-C04).
- 🎯 **Por qué importa:** El período de Neptuno en las fichas de la NASA es 60 189,018 días. Nadie piensa en 60 mil días; se piensa en años.
- 🔗 **Se estudia junto con:** segundo, minuto, hora, año juliano.

📘 **Dónde se aprende** (1 clase): [B03-C08 · Tiempo y conversiones astronómicas](../programa/clases/B03/B03-C08-tiempo-y-conversiones-astronomicas/CLASE.md).

### Día 0

- El día 0 es el día ideal de Hohmann del modelo.

💡 **Cómo se explica en la clase [B75-C29](../programa/clases/B75/B75-C29-analisis-de-calendario-con-graficos-pork-chop/CLASE.md):**
- Marte a `44,337°` de la Tierra el día 0 (B75-C02);
- Mínimo de la malla: `8,67 km²/s²` (día 0, `TOF = 260 d`).
- 🎯 **Por qué importa:** El diseño de una misión necesita ver el espacio de soluciones, no un solo punto. La decisión central: ¿qué combinaciones de fecha de salida y tiempo de vuelo dan un `C3` aceptable y cuán ancha es la ventana?
- 🔗 **Se estudia junto con:** gráfico pork-chop, banda, ventana, arco singular.

📘 **Dónde se aprende** (1 clase): [B75-C29 · Análisis de calendario con gráficos pork-chop](../programa/clases/B75/B75-C29-analisis-de-calendario-con-graficos-pork-chop/CLASE.md).

### Día juliano

- El día juliano es un conteo continuo de días.

💡 **Cómo se explica en la clase [B119-C12](../programa/clases/B119/B119-C12-historia-de-competencia-estrategica-espacial/CLASE.md):**
- Paso 4. El método juliano da el mismo número de días.
- Calcular intervalos con `datetime` y con el número de día juliano.
- ⚠️ **Error frecuente:** Contar mal años bisiestos. Se corrige con el método juliano.
- 🎯 **Por qué importa:** Para leer el derecho vigente conviene saber qué contexto lo produjo; ninguna clase anterior da la cronología comparada entre la tecnología y los instrumentos jurídicos. La decisión central: ¿cuánto tardó el derecho en seguir a la tecnología y por qué importa distinguir fechas verificadas de fechas recordadas?
- 🔗 **Se estudia junto con:** hito, rezago normativo, Competencia estratégica, fuente primaria.

📘 **Dónde se aprende** (1 clase): [B119-C12 · Historia de competencia estratégica espacial](../programa/clases/B119/B119-C12-historia-de-competencia-estrategica-espacial/CLASE.md).

### Día juliano (JD)

- El día juliano (JD) es el número de días, con fracción, desde el mediodía de un origen remoto; el JD de J2000 es `2 451 545,0` (S2).

💡 **Cómo se explica en la clase [B13-C09](../programa/clases/B13/B13-C09-segundos-intercalares-y-cronologia/CLASE.md):**
- Convertir una fecha gregoriana en día juliano modificado (MJD) y viceversa.
- 🎯 **Por qué importa:** Una nave graba un evento a las `23:59:59` del 31 de diciembre de 2016 y otro a las `00:00:00` del 1 de enero de 2017. ¿Cuánto tiempo pasó?
- 🔗 **Se estudia junto con:** segundo intercalar, calendario gregoriano, día juliano modificado (MJD), cuenta continua.

📘 **Dónde se aprende** (1 clase): [B13-C09 · Segundos intercalares y cronología](../programa/clases/B13/B13-C09-segundos-intercalares-y-cronologia/CLASE.md).

### Día juliano modificado (MJD)

- El día juliano modificado (MJD) es `JD − 2 400 000,5` y empieza a medianoche.

💡 **Cómo se explica en la clase [B13-C09](../programa/clases/B13/B13-C09-segundos-intercalares-y-cronologia/CLASE.md):**
- Convertir una fecha gregoriana en día juliano modificado (MJD) y viceversa.
- 🎯 **Por qué importa:** Una nave graba un evento a las `23:59:59` del 31 de diciembre de 2016 y otro a las `00:00:00` del 1 de enero de 2017. ¿Cuánto tiempo pasó?
- 🔗 **Se estudia junto con:** segundo intercalar, calendario gregoriano, día juliano (JD), cuenta continua.

📘 **Dónde se aprende** (1 clase): [B13-C09 · Segundos intercalares y cronología](../programa/clases/B13/B13-C09-segundos-intercalares-y-cronologia/CLASE.md).

### Día sidéreo

- El día sidéreo es el intervalo en que la Tierra gira una vez respecto de las estrellas lejanas, y dura 23,9345 horas (S2).
- El día sidéreo es el tiempo entre dos pasos consecutivos de una misma estrella por el meridiano; el valor que da la NASA es de `23,9345 h` (S2).
- Un día sidéreo (aquí, el periodo de rotación respecto del origen celeste) es el tiempo en que el ERA avanza una vuelta.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C04](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md):**
- El día solar dura 24,0000 h porque lo medimos de mediodía a mediodía; el día sidéreo dura 23,9345 h, porque lo medimos respecto de las estrellas (S2).
- Eso significa que en un año sidéreo la Tierra da una vuelta más sobre su eje respecto de las estrellas que días solares ha contado: `365,256 × 24/23,9345 = 366,26` días sidéreos frente a 365,256 días solares.
- ⚠️ **Error frecuente:** Mezclar día solar y sidéreo. Se piensa que las estrellas salen a la misma hora cada noche.
- 🎯 **Por qué importa:** En 1999 la sonda Mars Climate Orbiter se perdió en la atmósfera de Marte. Según la NASA, el programa en tierra trabajaba en unidades inglesas y el de la sonda en métricas, y esa discrepancia la dirigió demasiado cerca del planeta (S1).
- 🔗 **Se estudia junto con:** ciclo, período, día solar medio, año sidéreo.

📘 **Dónde se aprende** (4 clases): [B01-C04 · Espacio y tiempo en ciencia](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md); [B08-C05 · Tiempo sidéreo y solar](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md); [B13-C10 · Tiempo sidéreo local y terrestre](../programa/clases/B13/B13-C10-tiempo-sidereo-local-y-terrestre/CLASE.md); [B71-C16 · Período orbital](../programa/clases/B71/B71-C16-periodo-orbital/CLASE.md).

### Día solar

- El día solar es el tiempo entre dos pasos consecutivos del Sol por el meridiano; el día solar medio dura 24 h.
- El día solar es el intervalo entre dos pasos del Sol por el meridiano.

💡 **Cómo se explica en la clase [B08-C05](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md):**
- La NASA da el día sidéreo de la Tierra en `23,9345 h` y el día solar en `24,0000 h` (S2).
- El laboratorio calcula la duración del día sidéreo a partir de la tasa del tiempo sidéreo medio (1,0027379 vueltas por día solar): `23,93447 h = 23 h 56 min 04 s`, coincidente con la NASA dentro de su redondeo (0,0001 h).
- ⚠️ **Error frecuente:** Mezclar horas sidéreas con solares. Ejercicio 3.
- 🎯 **Por qué importa:** Si una estrella culmina a las 22:00 hoy, culminará a las 21:56 mañana. Quien no lo sabe «pierde» el objeto en pocas semanas.
- 🔗 **Se estudia junto con:** día solar medio, día sidéreo, tiempo sidéreo local (TSL), tiempo sidéreo de Greenwich (GMST).

📘 **Dónde se aprende** (2 clases): [B08-C05 · Tiempo sidéreo y solar](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md); [B113-C04 · Autonomía personal y gestión del tiempo en aislamiento](../programa/clases/B113/B113-C04-autonomia-personal-y-gestion-del-tiempo-en-aislamiento/CLASE.md).

### Día solar medio

- El día solar medio es el intervalo entre dos pasos consecutivos del Sol por el mismo punto del cielo, en promedio, y dura 24 horas.
- El día solar es el tiempo entre dos pasos consecutivos del Sol por el meridiano; el día solar medio dura 24 h.

💡 **Cómo se explica en la clase [B08-C05](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md):**
- El laboratorio calcula la duración del día sidéreo a partir de la tasa del tiempo sidéreo medio (1,0027379 vueltas por día solar): `23,93447 h = 23 h 56 min 04 s`, coincidente con la NASA dentro de su redondeo (0,0001 h).
- 🎯 **Por qué importa:** Si una estrella culmina a las 22:00 hoy, culminará a las 21:56 mañana. Quien no lo sabe «pierde» el objeto en pocas semanas.
- 🔗 **Se estudia junto con:** día solar, día sidéreo, tiempo sidéreo local (TSL), tiempo sidéreo de Greenwich (GMST).

📘 **Dónde se aprende** (2 clases): [B01-C04 · Espacio y tiempo en ciencia](../programa/clases/B01/B01-C04-espacio-y-tiempo-en-ciencia/CLASE.md); [B08-C05 · Tiempo sidéreo y solar](../programa/clases/B08/B08-C05-tiempo-sidereo-y-solar/CLASE.md).

### Diafonía cercana

- La diafonía cercana (*near-end crosstalk*) es la señal acoplada que aparece en el extremo de la línea víctima más próximo a la fuente.

💡 **Cómo se explica en la clase [B93-C03](../programa/clases/B93/B93-C03-integridad-de-senal-en-electronica-embarcada/CLASE.md):**
- Estimar la diafonía cercana y la longitud de saturación.
- Longitud de saturacion = tr v / 2 = 39.6 mm; onda incidente = 1.65 V; diafonia cercana saturada = 95 mV
- 🎯 **Por qué importa:** El tronco no incluía reflexiones, diafonía ni temporización de señales. La decisión central: ¿cuánto se deforma una señal por una terminación mal adaptada, cuánto se acopla a la pista vecina y cuánto margen de reloj queda?
- 🔗 **Se estudia junto con:** coeficiente de reflexión, diagrama de rebotes, longitud de saturación, margen de preparación.

📘 **Dónde se aprende** (1 clase): [B93-C03 · Integridad de señal en electrónica embarcada](../programa/clases/B93/B93-C03-integridad-de-senal-en-electronica-embarcada/CLASE.md).

### Diafragma

- El diafragma limita el haz.

💡 **Cómo se explica en la clase [B50-C03](../programa/clases/B50/B50-C03-sistemas-catadioptricos-schmidt-y-maksutov/CLASE.md):**
- Con el diafragma en el espejo el RMS crece con el campo (coma); en `C` es prácticamente constante.
- E["espejo esférico"] --> D1["diafragma en el espejo: coma"]
- ⚠️ **Error frecuente:** Poner el diafragma en el espejo y esperar campo plano. Se corrige con 8.1.
- 🎯 **Por qué importa:** Combinar espejos y elementos refractivos permite campos amplios con superficies fáciles de fabricar. La decisión central: ¿dónde va el diafragma y qué corrige el elemento refractivo?
- 🔗 **Se estudia junto con:** centro de curvatura, placa de Schmidt, menisco, RMS sin enfoque.

📘 **Dónde se aprende** (1 clase): [B50-C03 · Sistemas catadióptricos: Schmidt y Maksutov](../programa/clases/B50/B50-C03-sistemas-catadioptricos-schmidt-y-maksutov/CLASE.md).

### Diagonalizable

- Una matriz es diagonalizable si existe una matriz invertible `V` cuyas columnas son autovectores y `A = V Λ V⁻¹` con `Λ` diagonal de autovalores (S1, §1.2(vi), ec. 1.2.73: es el caso de las matrices no defectuosas).

💡 **Contexto en la clase [B10-C09](../programa/clases/B10/B10-C09-diagonalizacion-y-estabilidad/CLASE.md):**
- **Idea central (modelo mental):** Al diagonalizar, el sistema se separa en modos independientes: cada autovector evoluciona multiplicado por `e^{λt}`.
- 🎯 **Por qué importa:** Un panel solar largo y delgado vibra después de una maniobra. Si la vibración se amortigua, el panel es estable; si crece, hay un problema serio.
- 🔗 **Se estudia junto con:** semejantes, exponencial matricial, asintóticamente estable, marginalmente estable.

📘 **Dónde se aprende** (1 clase): [B10-C09 · Diagonalización y estabilidad](../programa/clases/B10/B10-C09-diagonalizacion-y-estabilidad/CLASE.md).

### Diagrama de bloques

- Un diagrama de bloques representa cada subsistema con un rectángulo y su función de transferencia, y cada señal con una flecha.

💡 **Cómo se explica en la clase [B16-C06](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md):**
- Se prefiere el espacio de estados cuando hay varias entradas y salidas o cuando se va a simular; el diagrama de bloques, para razonar.
- Dibujar e interpretar un diagrama de bloques con sumadores, bloques y puntos de bifurcación.
- 🎯 **Por qué importa:** Un sistema de control de actitud tiene sensores, un computador, ruedas y un cuerpo, todos conectados y, sobre todo, con la salida de vuelta a la entrada. Para entender qué hace el conjunto no basta conocer las partes: hay que saber cómo se combinan.
- 🔗 **Se estudia junto con:** sumador, punto de bifurcación, lazo cerrado, referencia.

📘 **Dónde se aprende** (1 clase): [B16-C06 · Diagramas de bloques](../programa/clases/B16/B16-C06-diagramas-de-bloques/CLASE.md).

### Diagrama de Bode

- Un diagrama de Bode grafica el módulo en dB y la fase en grados contra `ω` en escala logarítmica.

💡 **Cómo se explica en la clase [B16-C10](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md):**
- python programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/margenes_y_nyquist.py
- 🎯 **Por qué importa:** Los modelos nunca son exactos: la inercia varía, el sensor tarda más de lo supuesto, un modo flexible aparece. La estabilidad nominal no basta; hay que saber cuánto error aguanta el lazo.
- 🔗 **Se estudia junto con:** respuesta en frecuencia, cruce de ganancia, cruce de fase, margen de fase.

📘 **Dónde se aprende** (1 clase): [B16-C10 · Diagramas de Bode y Nyquist](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md).

### Diagrama de cuerpo libre (DCL)

- Un diagrama de cuerpo libre (DCL) es un esquema que muestra un cuerpo aislado y todas las fuerzas externas que actúan sobre él, como flechas desde el cuerpo.

💡 **Cómo se explica en la clase [B05-C05](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md):**
- Dibujar un diagrama de cuerpo libre con ejes y ángulos declarados.
- python programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/equilibrio_de_fuerzas.py
- 🎯 **Por qué importa:** En un lanzamiento o en una maniobra hay varias fuerzas a la vez: gravedad, empuje, tensiones, rozamiento. La pregunta motivadora es: ¿cómo dejo de olvidar fuerzas y de contar dos veces una misma?
- 🔗 **Se estudia junto con:** peso, normal, tensión, empuje.

📘 **Dónde se aprende** (1 clase): [B05-C05 · Diagramas de cuerpo libre](../programa/clases/B05/B05-C05-diagramas-de-cuerpo-libre/CLASE.md).

### Diagrama de fases

- Un diagrama de fases es un mapa presión–temperatura con las regiones donde una sustancia es sólida, líquida o gaseosa.

💡 **Cómo se explica en la clase [B06-C11](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md):**
- Identificar punto triple, punto crítico y las curvas de un diagrama de fases.
- Redactar una ficha de ubicación en el diagrama de fases con sus aproximaciones.
- 🎯 **Por qué importa:** La temperatura de ebullición del agua no es una constante de la naturaleza: depende de la presión. En lo alto de una montaña hierve a menos de 100 °C; en Marte, con 6 mb, el agua apenas puede ser líquida; en Venus, a 92 bar y 737 K, el CO₂ no es ni líquido ni gas.
- 🔗 **Se estudia junto con:** curvas de equilibrio, fusión, vaporización, sublimación.

📘 **Dónde se aprende** (1 clase): [B06-C11 · Diagramas de fase](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md).

### Diagrama de fiabilidad

- Un diagrama de fiabilidad (*reliability diagram*) agrupa pronósticos de probabilidad en casillas y compara la probabilidad media pronosticada con la frecuencia observada del suceso.

💡 **Cómo se explica en la clase [B19-C08](../programa/clases/B19/B19-C08-calibracion-probabilistica/CLASE.md):**
- Diagrama de fiabilidad (pronóstico medio → frecuencia observada; 10 casillas): calibrado: 0,06→0,06; 0,25→0,25; 0,55→0,56; 0,94→0,94.
- El diagrama de fiabilidad hace lo mismo para pronósticos de sucesos.
- 🎯 **Por qué importa:** Un intervalo del 90 % que cubre el valor verdadero solo la mitad de las veces es peor que no tener intervalo: transmite una seguridad falsa. Los diagnósticos de C04 dicen si el cómputo funcionó; los chequeos de C06 si el modelo reproduce los datos.
- 🔗 **Se estudia junto con:** calibrado, cobertura, precisión, SBC.

📘 **Dónde se aprende** (1 clase): [B19-C08 · Calibración probabilística](../programa/clases/B19/B19-C08-calibracion-probabilistica/CLASE.md).

### Diagrama de flujo funcional

- Un diagrama de flujo funcional (FFBD) ordena las funciones por dependencia.

💡 **Contexto en la clase [B83-C06](../programa/clases/B83/B83-C06-descomposicion-funcional/CLASE.md):**
- 🎯 **Por qué importa:** Si se salta a las piezas demasiado pronto, se diseñan cosas que nadie sabe para qué sirven; si se descompone bien, se ve qué función domina el tiempo y dónde se acoplan los subsistemas. La decisión central: ¿qué funciones son críticas para el tiempo y qué subsistemas quedan más acoplados?
- 🔗 **Se estudia junto con:** función, descomposición funcional, ruta crítica, holgura.

📘 **Dónde se aprende** (1 clase): [B83-C06 · Descomposición funcional](../programa/clases/B83/B83-C06-descomposicion-funcional/CLASE.md).

### Diagrama de Nyquist

- Un diagrama de Nyquist traza `L(jω)` en el plano complejo para `ω` de −∞ a ∞.

💡 **Cómo se explica en la clase [B16-C10](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md):**
- Contar vueltas del diagrama de Nyquist y deducir el número de polos inestables.
- python programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/margenes_y_nyquist.py
- 🎯 **Por qué importa:** Los modelos nunca son exactos: la inercia varía, el sensor tarda más de lo supuesto, un modo flexible aparece. La estabilidad nominal no basta; hay que saber cuánto error aguanta el lazo.
- 🔗 **Se estudia junto con:** respuesta en frecuencia, diagrama de Bode, cruce de ganancia, cruce de fase.

📘 **Dónde se aprende** (1 clase): [B16-C10 · Diagramas de Bode y Nyquist](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md).

### Diagrama de radiación

- El diagrama de radiación es la respuesta en potencia según la dirección.

💡 **Cómo se explica en la clase [B46-C04](../programa/clases/B46/B46-C04-diagramas-de-radiacion/CLASE.md):**
- La evidencia es la ficha del diagrama de radiación del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha del diagrama de radiación*: tabla de HPBW, lóbulo y eficiencia, con la elección justificada.
- 🎯 **Por qué importa:** Bajar los lóbulos laterales evita captar emisión de direcciones no deseadas, pero ensancha el haz y reduce la eficiencia. La decisión central: ¿qué iluminación equilibra resolución y rechazo de lóbulos?
- 🔗 **Se estudia junto con:** lóbulo lateral, iluminación, eficiencia de apertura, taper.

📘 **Dónde se aprende** (1 clase): [B46-C04 · Diagramas de radiación](../programa/clases/B46/B46-C04-diagramas-de-radiacion/CLASE.md).

### Diagrama de rebotes

- El diagrama de rebotes suma en el tiempo las ondas que van y vienen.

💡 **Cómo se explica en la clase [B93-C03](../programa/clases/B93/B93-C03-integridad-de-senal-en-electronica-embarcada/CLASE.md):**
- Construir el diagrama de rebotes y leer sobreimpulso y tiempo de establecimiento.
- El script [senal.py](senal.py) calcula el diagrama de rebotes, lo contrasta con una simulación FDTD, estima la diafonía y el margen de reloj (comprueba el valor final con 1e-6, FDTD frente a rebotes dentro de 0,04 V y `K_b` aproximado frente al exacto dentro de 3 %).
- 🎯 **Por qué importa:** El tronco no incluía reflexiones, diafonía ni temporización de señales. La decisión central: ¿cuánto se deforma una señal por una terminación mal adaptada, cuánto se acopla a la pista vecina y cuánto margen de reloj queda?
- 🔗 **Se estudia junto con:** coeficiente de reflexión, diafonía cercana, longitud de saturación, margen de preparación.

📘 **Dónde se aprende** (1 clase): [B93-C03 · Integridad de señal en electrónica embarcada](../programa/clases/B93/B93-C03-integridad-de-senal-en-electronica-embarcada/CLASE.md).

### Diagrama HR

- El diagrama HR representa `L` (o la magnitud absoluta) contra `T_ef` (o el tipo espectral), con la temperatura creciente hacia la izquierda por tradición histórica.

💡 **Cómo se explica en la clase [B24-C03](../programa/clases/B24/B24-C03-diagrama-de-hertzsprung-russell/CLASE.md):**
- Los diagramas de cúmulos y del campo cambian con la edad, la metalicidad y la cinemática de la población (S3, resumen).
- La posición de una estrella en el diagrama depende de su masa, de su composición y de cuánto ha evolucionado.
- 🎯 **Por qué importa:** Casi todas las propiedades de una estrella (tamaño, masa, edad, fase) se resumen en dos medidas: cuánta energía emite y a qué temperatura. El diagrama HR convierte esas dos medidas en un mapa donde cada región corresponde a un estado físico.
- 🔗 **Se estudia junto con:** luminosidad, temperatura efectiva, constante de Stefan–Boltzmann, secuencia principal.

📘 **Dónde se aprende** (1 clase): [B24-C03 · Diagrama de Hertzsprung-Russell](../programa/clases/B24/B24-C03-diagrama-de-hertzsprung-russell/CLASE.md).

### Diagrama trabajo-precisión

- El diagrama trabajo-precisión (*work-precision diagram*) grafica el error alcanzado frente al trabajo gastado.

💡 **Cómo se explica en la clase [B11-C26](../programa/clases/B11/B11-C26-benchmark-de-algoritmos-numericos/CLASE.md):**
- *Descripción textual:* se define el problema y los errores objetivo; cada método se barre con resoluciones crecientes registrando error y evaluaciones; se arma el diagrama trabajo-precisión y se anota el costo mínimo por objetivo; el tiempo de reloj se mide aparte; se repite todo para comprobar que los números coinciden.
- Equivalente accesible a un diagrama trabajo-precisión (evaluaciones, error): la tabla de 8.3.
- 🎯 **Por qué importa:** «El método A es mejor que el B» es una afirmación vacía sin el problema, la métrica, la tolerancia y el costo. Una comparación mal diseñada lleva a elegir el algoritmo equivocado para una misión.
- 🔗 **Se estudia junto con:** benchmark, trabajo, barrido, error objetivo.

📘 **Dónde se aprende** (1 clase): [B11-C26 · Benchmark de algoritmos numéricos](../programa/clases/B11/B11-C26-benchmark-de-algoritmos-numericos/CLASE.md).

### Diámetro

- El diámetro es la mayor distancia mínima entre pares.

💡 **Cómo se explica en la clase [B88-C31](../programa/clases/B88/B88-C31-topologias-de-red-de-datos-a-bordo/CLASE.md):**
- El anillo logra 0 puentes con el menor costo, a cambio de diámetro 3.
- Un anillo es el mínimo con tolerancia a un enlace; la doble estrella reduce el diámetro a 2 con dos concentradores.
- 🎯 **Por qué importa:** Una red con un enlace crítico único pierde un subsistema entero con una sola falla. La decisión central: ¿qué topología da la tolerancia y la latencia necesarias con el menor número de enlaces?
- 🔗 **Se estudia junto con:** topología, saltos medios, puente, malla completa.

📘 **Dónde se aprende** (1 clase): [B88-C31 · Topologías de red de datos a bordo](../programa/clases/B88/B88-C31-topologias-de-red-de-datos-a-bordo/CLASE.md).

### Diámetro angular

- El diámetro angular es el ángulo que ocupa un objeto en el cielo.
- El diámetro angular es el ángulo que subtiende su disco.

💡 **Cómo se explica en la clase [B04-C07](../programa/clases/B04/B04-C07-triangulos-y-distancias-angulares/CLASE.md):**
- Un objeto a distancia `d` con diámetro angular `δ` tiene un diámetro `D = 2 d tan(δ/2) ≈ d δ`.
- Ejercicio 6. La Luna se ve con diámetro angular 0,5179° desde una distancia de 384 400 km.
- 🎯 **Por qué importa:** Nadie puede llevar una cinta métrica a una estrella. Pero sí se puede observar la misma estrella desde dos puntos separados una distancia conocida y medir cuánto cambia su dirección.
- 🔗 **Se estudia junto con:** triángulo rectángulo, hipotenusa, catetos, base.

📘 **Dónde se aprende** (2 clases): [B04-C07 · Triángulos y distancias angulares](../programa/clases/B04/B04-C07-triangulos-y-distancias-angulares/CLASE.md); [B08-C08 · Fases lunares y libración](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md).

### Diámetro crítico

- El diámetro crítico `d_c = t^0,9` (mm).
- desecho orbital: fragmento artificial. Diámetro crítico: el menor proyectil que penetra.

💡 **Cómo se explica en la clase [B106-C15](../programa/clases/B106/B106-C15-proteccion-frente-a-micrometeoritos/CLASE.md):**
- *Descripción textual:* el flujo, la superficie y el tiempo dan el número esperado de impactos sobre el diámetro crítico, que fija la pared y la separación; de ahí sale la PNP.
- Con un flujo sintético `N(>d) = 10⁻⁴ (d/1 mm)^−2,5` por m² y año, 100 m² y una pared de 2 mm con diámetro crítico ilustrativo de 0,60 mm, se esperan 0,036 impactos penetrantes al año: P(sin penetración) = 0,9648 el primer año y 0,8359 en 5 años.
- 🎯 **Por qué importa:** Los impactos son raros pero catastróficos; el diseño elige espesor y separación para una probabilidad de no penetración. La decisión central: ¿qué pared y qué separación dan una probabilidad objetivo en la duración y la superficie de la misión?
- 🔗 **Se estudia junto con:** Micrometeoroide, desecho orbital, Parachoques, Probabilidad de no penetración (PNP).

📘 **Dónde se aprende** (2 clases): [B85-C28 · Protección pasiva frente al ambiente espacial](../programa/clases/B85/B85-C28-proteccion-pasiva-frente-al-ambiente-espacial/CLASE.md); [B106-C15 · Protección frente a micrometeoritos](../programa/clases/B106/B106-C15-proteccion-frente-a-micrometeoritos/CLASE.md).

### Diámetro de Sauter

- El diámetro de Sauter `d₃₂` es el de una esfera con la misma razón volumen/superficie que el conjunto.

💡 **Cómo se explica en la clase [B59-C04](../programa/clases/B59/B59-C04-caracterizacion-de-regolito-lunar/CLASE.md):**
- Obtener el diámetro de Sauter y la superficie específica.
- Diametro de Sauter d32 = 44.3 µm ; superficie especifica de esferas = 45.1 m^2/kg
- ⚠️ **Error frecuente:** Usar el diámetro medio aritmético en lugar del de Sauter para la superficie. Se corrige con 8.4.
- 🎯 **Por qué importa:** Un tamiz, una tolva o un horno de sinterización se diseñan para una distribución de tamaños, no para un grano. La decisión central: ¿qué fracción de la masa es fina (menor de 20 µm) y cuánto cambia si hablo de número o de masa?
- 🔗 **Se estudia junto con:** desviación geométrica, coeficiente de uniformidad, superficie específica.

📘 **Dónde se aprende** (1 clase): [B59-C04 · Caracterización de regolito lunar](../programa/clases/B59/B59-C04-caracterizacion-de-regolito-lunar/CLASE.md).

### Diámetro equivalente

- El diámetro equivalente es `D = 2√(A/π)` por la escala.
- El diámetro equivalente es el del orificio que daría esa tasa.

💡 **Cómo se explica en la clase [B103-C06](../programa/clases/B103/B103-C06-deteccion-y-catalogacion-de-rocas-en-imagenes-de-superficie/CLASE.md):**
- Convertir píxeles en metros con la escala en el terreno y calcular el diámetro equivalente de una región.
- 🎯 **Por qué importa:** Un catálogo de rocas es incompleto justo donde hay más rocas: las pequeñas. Ajustar una ley de potencias con todas las detecciones da un exponente sesgado.
- 🔗 **Se estudia junto con:** distribución tamaño-frecuencia, tamaño mínimo de completitud, máxima verosimilitud, bootstrap.

📘 **Dónde se aprende** (2 clases): [B103-C06 · Detección y catalogación de rocas en imágenes de superficie](../programa/clases/B103/B103-C06-deteccion-y-catalogacion-de-rocas-en-imagenes-de-superficie/CLASE.md); [B114-C02 · Detección, localización y respuesta a fugas de presión](../programa/clases/B114/B114-C02-deteccion-localizacion-y-respuesta-a-fugas-de-presion/CLASE.md).

### Diámetro transitorio

- El diámetro transitorio `D_tc` es el del cráter justo tras la excavación.

💡 **Cómo se explica en la clase [B53-C10](../programa/clases/B53/B53-C10-geologia-de-impacto/CLASE.md):**
- El diámetro transitorio ilustrativo es `2640 m` con `g = 1,62`, `2200 m` con `g = 3,71` y `1776 m` con `g = 9,81`.
- ⚠️ **Error frecuente:** Confundir diámetro transitorio con final. se corrige con la sección 6
- 🎯 **Por qué importa:** Un cráter es una medida indirecta del impacto. La decisión central: ¿cómo cambia el diámetro del cráter con la gravedad y qué incertidumbre tiene un exponente ajustado a pocos experimentos?
- 🔗 **Se estudia junto con:** grupo, adaptación de impedancias.

📘 **Dónde se aprende** (1 clase): [B53-C10 · Geología de impacto](../programa/clases/B53/B53-C10-geologia-de-impacto/CLASE.md).

### Días nominales

- Los días nominales son `⌈D f/d⌉`.

💡 **Cómo se explica en la clase [B97-C20](../programa/clases/B97/B97-C20-mision-robotica-integrada-simulada/CLASE.md):**
- Días nominales con cada cambio de ±20 %: uso +20 %: `14`; uso −20 %: `21`; ruta +20 %: `21`; distancia +20 %: `21`; batería +20 %: `14`; batería −20 %: `21` (frente a `17` nominales).
- *Descripción textual:* la energía y el tiempo fijan las horas útiles; con la velocidad dan la distancia diaria; la distancia por el factor de ruta da los días nominales y las anomalías los alargan.
- ⚠️ **Error frecuente:** Presupuestar solo los días nominales. Las anomalías añaden media y cola (8.3)
- 🎯 **Por qué importa:** Una misión se diseña con un presupuesto de días y de margen. Un modelo integrado, aunque simple, muestra cuál parámetro domina y cuánto margen pide una anomalía, antes de invertir en simulaciones detalladas.
- 🔗 **Se estudia junto con:** distancia diaria, anomalía, percentil 95, sensibilidad.

📘 **Dónde se aprende** (1 clase): [B97-C20 · Misión robótica integrada simulada](../programa/clases/B97/B97-C20-mision-robotica-integrada-simulada/CLASE.md).

### Diccionario

- Un diccionario (`dict`) asocia claves únicas e inmutables a valores, entre llaves (S3).

💡 **Cómo se explica en la clase [B07-C07](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md):**
- Una lista es una fila de cajones numerados; un diccionario es un fichero con etiquetas (claves) para buscar rápido; una tupla es una fila de cajones sellados; un conjunto es una bolsa donde cada cosa entra una vez.
- *Descripción textual:* una lista con ocho posiciones; la posición 0 contiene el diccionario de Mercurio y la 2 el de la Tierra.
- ⚠️ **Error frecuente:** `{}` como conjunto vacío. Es un diccionario.
- 🎯 **Por qué importa:** Una tabla de ocho planetas con tres propiedades cada uno son 24 datos: no cabe en 24 variables sueltas. Necesitas estructuras que agrupen datos, permitan recorrerlos y los mantengan ordenados y consultables.
- 🔗 **Se estudia junto con:** lista, tupla, inmutable, conjunto.

📘 **Dónde se aprende** (1 clase): [B07-C07 · Listas y estructuras de datos](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md).

### Diccionario de fallas

- Firma: vector de desviaciones de una causa. Diccionario de fallas: conjunto de firmas.

💡 **Contexto en la clase [B96-C29](../programa/clases/B96/B96-C29-diagnostico-de-fallas-de-enlace/CLASE.md):**
- 🎯 **Por qué importa:** Perder tiempo de contacto buscando la causa equivocada es caro. La decisión central: ¿qué medidas distinguen las causas y cuáles se confunden entre sí?
- 🔗 **Se estudia junto con:** Firma, Mínima distancia, Matriz de confusión, Cota de unión.

📘 **Dónde se aprende** (1 clase): [B96-C29 · Diagnóstico de fallas de enlace](../programa/clases/B96/B96-C29-diagnostico-de-fallas-de-enlace/CLASE.md).

### Didáctica

- Una regla de categorías convierte esa medida en una etiqueta; la de esta clase es didáctica.

💡 **Contexto en la clase [B67-C04](../programa/clases/B67/B67-C04-estimacion-de-reservas-y-categorias-de-recursos/CLASE.md):**
- **Idea central (modelo mental):** Piensa en estimar cuánto dinero hay en una caja sin abrirla por completo: con pocas monedas contadas, el saldo estimado es poco confiable; con más monedas, y sabiendo bien el tamaño de la caja, se puede decir «entre tanto y tanto».
- 🎯 **Por qué importa:** Decir «hay 330 kt» sin intervalo ni categoría invita a decisiones equivocadas. La decisión central: ¿cuánto del recurso se puede llamar reserva, y qué falta para subir de categoría?
- 🔗 **Se estudia junto con:** recurso, reserva, factores modificadores, categorías.

📘 **Dónde se aprende** (1 clase): [B67-C04 · Estimación de reservas y categorías de recursos](../programa/clases/B67/B67-C04-estimacion-de-reservas-y-categorias-de-recursos/CLASE.md).

### DIET

- La DIET (desorción inducida por transiciones electrónicas) es el mecanismo en que la excitación electrónica de una molécula de la superficie provoca su salida;

💡 **Contexto en la clase [B68-C02](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md):**
- **Idea central (modelo mental):** Piensa en una lluvia de granizo (fotones) sobre una superficie de arena (hielo): cada impacto lanza algunos granos fuera (desorción), y los impactos más profundos rompen granos sin lanzarlos (fotólisis). Pocas veces el granizo lanza algo, pero la lluvia es larga.
- 🎯 **Por qué importa:** Si un hielo de CO a 15 K es estable térmicamente durante millones de años, la presencia de CO gaseoso en regiones frías exige otro mecanismo. La decisión central: ¿cuántas moléculas expulsa cada fotón y de qué depende ese número?
- 🔗 **Se estudia junto con:** fotodesorción, rendimiento, fluencia, fotólisis.

📘 **Dónde se aprende** (1 clase): [B68-C02 · Fotodesorción de hielos interestelares](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md).

### Diez principios

- Los diez principios son los de la ECSA (2015).

💡 **Cómo se explica en la clase [B129-C07](../programa/clases/B129/B129-C07-proyecto-de-ciencia-ciudadana-validable/CLASE.md):**
- Por lista: estado de los diez principios.
- Revisar un plan contra los diez principios de la ECSA y nombrar los pendientes.
- 🎯 **Por qué importa:** Un proyecto ciudadano que produce datos sin validar es una anécdota; con validación es evidencia. La decisión central: ¿cuántos votos por objeto hacen falta, cómo se sabe que el resultado coincide con el de los expertos y qué le falta al plan para ser una ciencia ciudadana bien hecha?
- 🔗 **Se estudia junto con:** voto mayoritario, exactitud, κ de Cohen, objeto difícil.

📘 **Dónde se aprende** (1 clase): [B129-C07 · Proyecto de ciencia ciudadana validable](../programa/clases/B129/B129-C07-proyecto-de-ciencia-ciudadana-validable/CLASE.md).

### Diferencia

- La diferencia lista añadidos, eliminados y modificados.

💡 **Cómo se explica en la clase [B88-C18](../programa/clases/B88/B88-C18-control-de-configuracion-de-firmware/CLASE.md):**
- *Descripción textual:* de los archivos salen el manifiesto, el identificador de línea base y las diferencias; la compilación repetida comprueba la reproducibilidad.
- El laboratorio verifica diferencias y reproducibilidad.
- 🎯 **Por qué importa:** Si no se sabe exactamente qué firmware vuela, no se puede reproducir un fallo ni comprobar que se probó lo que se lanzó. La decisión central: ¿qué registro identifica de manera única una versión y permite verificarla?
- 🔗 **Se estudia junto con:** manifiesto, ID de línea base, compilación reproducible, efecto avalancha.

📘 **Dónde se aprende** (1 clase): [B88-C18 · Control de configuración de firmware](../programa/clases/B88/B88-C18-control-de-configuracion-de-firmware/CLASE.md).

### Diferencia de camino

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C03](../programa/clases/B42/B42-C03-interferencia-y-coherencia/CLASE.md):**
- Con `λ₀ = 600 nm` y un ancho de `10 nm` (ilustrativos) la longitud de coherencia `1/σ_k` es `13,49 µm` y la visibilidad a esa diferencia de camino es `0,6065`.
- Porque la diferencia de camino supera la longitud de coherencia del filtro.
- 🎯 **Por qué importa:** Sin coherencia no hay franjas: una fuente ancha en frecuencia o en tamaño borra la interferencia. La decisión central: ¿hasta qué diferencia de camino se ven franjas con una fuente de ancho espectral dado?
- 🔗 **Se estudia junto con:** visibilidad, coherencia temporal, longitud de coherencia, espectro.

📘 **Dónde se aprende** (2 clases): [B42-C03 · Interferencia y coherencia](../programa/clases/B42/B42-C03-interferencia-y-coherencia/CLASE.md); [B42-C09 · Interferometría de dos haces](../programa/clases/B42/B42-C09-interferometria-de-dos-haces/CLASE.md).

### Diferencia de camino óptico

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B41-C13](../programa/clases/B41/B41-C13-aberracion-esferica-y-coma/CLASE.md):**
- **Idea central (modelo mental):** Como un cometa: la estrella fuera del eje se convierte en una cola; la cabeza es el rayo central y la cola crece con la distancia al eje y con la luminosidad del espejo.
- 🎯 **Por qué importa:** Dos defectos limitan el campo y la relación focal. La decisión central: ¿hasta qué f/ sirve una esfera y qué campo tolera un paraboloide?
- 🔗 **Se estudia junto con:** aberración esférica, coeficiente W040, coma, abanico tangencial.

📘 **Dónde se aprende** (1 clase): [B41-C13 · Aberración esférica y coma](../programa/clases/B41/B41-C13-aberracion-esferica-y-coma/CLASE.md).

### Diferencia de ganancia

- El desfase `o_s` y la diferencia de ganancia `g`.

💡 **Cómo se explica en la clase [B43-C16](../programa/clases/B43/B43-C16-encoders-y-medicion-angular/CLASE.md):**
- Con desfase `o_s = 0,01` el error máximo es `0,2063"` (teoría `0,2063"`); con diferencia de ganancia `g = 0,02` es `0,2042"` (teoría `0,2063"`).
- 🎯 **Por qué importa:** El codificador es el ojo de la montura: lo que no mide, no lo corrige. La decisión central: ¿qué resolución, qué código y qué calidad de señal dan un error angular menor que el presupuesto?
- 🔗 **Se estudia junto con:** línea, cuentas, paso, error de cuantización.

📘 **Dónde se aprende** (1 clase): [B43-C16 · Encoders y medición angular](../programa/clases/B43/B43-C16-encoders-y-medicion-angular/CLASE.md).

### Diferencia de imágenes

- La diferencia de imágenes `d = I₂ − I₁` tiene ruido `σ_d = √2 σ`.

💡 **Contexto en la clase [B57-C27](../programa/clases/B57/B57-C27-deteccion-de-cambios-en-series-de-imagenes/CLASE.md):**
- **Idea central (modelo mental):** El guardia ignora los ruidos normales de la noche y se alarma por los que superan un umbral. Un umbral bajo lo despierta con el viento; uno alto, cuando ya entró el ladrón.
- 🎯 **Por qué importa:** Un umbral bajo llena el mapa de falsas alarmas; uno alto deja pasar cambios reales. La decisión central: ¿qué umbral equilibra falsas alarmas y detecciones para el cambio que me interesa?
- 🔗 **Se estudia junto con:** umbral, tasa de falsa alarma, detección, quiebre.

📘 **Dónde se aprende** (1 clase): [B57-C27 · Detección de cambios en series de imágenes](../programa/clases/B57/B57-C27-deteccion-de-cambios-en-series-de-imagenes/CLASE.md).

### Diferencia de masas

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B31-C11](../programa/clases/B31/B31-C11-neutrinos-y-oscilaciones/CLASE.md):**
- **Idea central (modelo mental):** Como una luz que cambia de color con el tiempo según la distancia recorrida: a cierta distancia vuelve al color inicial.
- 🎯 **Por qué importa:** Detectar neutrinos del Sol, la atmósfera y aceleradores exige saber cuánto oscilan. La decisión central: ¿cuál es la probabilidad de oscilación a cierta distancia y energía?
- 🔗 **Se estudia junto con:** probabilidad de oscilación, ángulo de mezcla, longitud de oscilación, promedio en energía.

📘 **Dónde se aprende** (1 clase): [B31-C11 · Neutrinos y oscilaciones](../programa/clases/B31/B31-C11-neutrinos-y-oscilaciones/CLASE.md).

### Diferencia de órdenes

- La diferencia de órdenes entre `A` y `B` es `eA − eB` y, de forma más fina, `log₁₀(A/B)`.

💡 **Cómo se explica en la clase [B03-C05](../programa/clases/B03/B03-C05-notacion-cientifica-y-ordenes-de-magnitud/CLASE.md):**
- La diferencia de órdenes se lee como cuántas veces hay que multiplicar por diez para pasar de una a otra.
- Asignar a una cantidad su orden de magnitud y comparar dos cantidades por la diferencia de órdenes.
- 🎯 **Por qué importa:** Las fichas de la NASA publican las masas en «10²⁴ kg»: la Tierra es 5,9722, el Sol 1 988 400. Si no sabes leer ese `10²⁴`, tampoco sabrás si 1 988 400 es «un poco más» o «mucho más».
- 🔗 **Se estudia junto con:** notación científica, mantisa, normalizada, exponente.

📘 **Dónde se aprende** (1 clase): [B03-C05 · Notación científica y órdenes de magnitud](../programa/clases/B03/B03-C05-notacion-cientifica-y-ordenes-de-magnitud/CLASE.md).

### Diferencia entre la temperatura de ensayo y la prevista en órbita

- Margen de ensayo: diferencia entre la temperatura de ensayo y la prevista en órbita. Balance térmico: ensayo para correlacionar el modelo térmico.

💡 **Contexto en la clase [B90-C11](../programa/clases/B90/B90-C11-ensayos-termicos/CLASE.md):**
- 🎯 **Por qué importa:** Una prueba funcional hecha antes de que la unidad se estabilice no demuestra nada sobre la temperatura extrema; una espera excesiva consume cámara y calendario. La decisión central: ¿cuánto debe esperar el ensayo para que la temperatura de la unidad sea la de la prueba?
- 🔗 **Se estudia junto con:** Nodo concentrado, Constante de tiempo τ, Rampa, tiempo a temperatura constante.

📘 **Dónde se aprende** (1 clase): [B90-C11 · Ensayos térmicos](../programa/clases/B90/B90-C11-ensayos-termicos/CLASE.md).

### Diferencia finita central

- Una diferencia finita central aproxima `∂f/∂pⱼ ≈ (f(p + h eⱼ) − f(p − h eⱼ))/(2h)` (B09-C03/C04).

💡 **Cómo se explica en la clase [B10-C19](../programa/clases/B10/B10-C19-jacobianos-y-linealizacion/CLASE.md):**
- Diferencias finitas centrales: simple, con error `O(h²)` y ruido de redondeo.
- 🎯 **Por qué importa:** Una estación mide la distancia, el azimut y la elevación de un objeto con incertidumbres. Para decir dónde está en coordenadas cartesianas y cuánta incertidumbre tiene esa posición, hay que transformar los números y sus errores.
- 🔗 **Se estudia junto con:** jacobiano, aproximación lineal, factor de escala de volúmenes, cambio de coordenadas.

📘 **Dónde se aprende** (1 clase): [B10-C19 · Jacobianos y linealización](../programa/clases/B10/B10-C19-jacobianos-y-linealizacion/CLASE.md).

### Diferencia fotosfera–meteorito

- La diferencia fotosfera–meteorito es `Δ = A_fot − A_met`: positiva si el elemento está empobrecido en el meteorito; negativa si está empobrecido en el Sol.

💡 **Cómo se explica en la clase [B06-C20](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md):**
- Para los 45 elementos no volátiles con incertidumbre fotosférica menor que el 25 %, la diferencia media entre la fotosfera y los meteoritos es 0,00 ± 0,05 dex; el litio es una excepción, empobrecido en el Sol (S1).
- Calcular la diferencia fotosfera–meteorito en dex y en factor.
- 🎯 **Por qué importa:** Hay dos formas de saber de qué está hecho el Sistema Solar. Una es mirar la luz del Sol y deducir su composición; la otra es analizar en laboratorio meteoritos que conservan la composición del material con que se formó.
- 🔗 **Se estudia junto con:** meteorito, condrita, condritas carbonáceas, CI.

📘 **Dónde se aprende** (1 clase): [B06-C20 · Análisis químico introductorio de meteoritos](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md).

### Diferencia normalizada

- La diferencia normalizada de dos medidas independientes es `z = |x₁ − x₂|/√(u₁² + u₂²)`: su denominador es la incertidumbre de la diferencia (S1, 5.1.2 con coeficientes `+1` y `−1`).

💡 **Cómo se explica en la clase [B13-C18](../programa/clases/B13/B13-C18-intercomparacion-de-instrumentos/CLASE.md):**
- Calcular la diferencia normalizada `z` entre dos medidas independientes.
- 🎯 **Por qué importa:** Tres radiómetros miden la misma irradiancia solar y dan `1361,4`, `1360,1` y `1362,9 W/m²`. Cada uno declara una incertidumbre.
- 🔗 **Se estudia junto con:** intercomparación, Compatibles, media ponderada, chi cuadrado.

📘 **Dónde se aprende** (1 clase): [B13-C18 · Intercomparación de instrumentos](../programa/clases/B13/B13-C18-intercomparacion-de-instrumentos/CLASE.md).

### Diferencia RTN

- La diferencia RTN descompone `Δr` en los ejes radial, transversal y normal de la referencia.

💡 **Cómo se explica en la clase [B74-C20](../programa/clases/B74/B74-C20-validacion-frente-a-efemerides-de-referencia/CLASE.md):**
- Un ajuste de dos cuerpos a 24 h de posiciones con J2 deja diferencias rms (R, T, N) de `1209`, `286` y `78918 m`, con un máximo 3D de `190035 m`: el modelo no puede acomodar la precesión del plano orbital.
- R["referencia con J2"] --> D["diferencia en RTN"]
- 🎯 **Por qué importa:** Una solución que ajusta bien sus datos puede predecir pésimamente. La decisión central: ¿dentro de qué tolerancia coincide mi solución con la referencia, en qué componente falla y qué modelo falta?
- 🔗 **Se estudia junto con:** efeméride de referencia, arco de ajuste, predicción, J2.

📘 **Dónde se aprende** (1 clase): [B74-C20 · Validación frente a efemérides de referencia](../programa/clases/B74/B74-C20-validacion-frente-a-efemerides-de-referencia/CLASE.md).

### Diferenciación

- La diferenciación es la separación de un cuerpo en capas de distinta densidad.

💡 **Cómo se explica en la clase [B52-C18](../programa/clases/B52/B52-C18-diferenciacion-planetaria/CLASE.md):**
- El máximo es `5575 K`; tras 10 vidas medias, `5569.264 K` (analítico) y `5569.264 K` (RK4, diferencia `5e-14`).
- Son cotas: parte se disipa, parte se pierde, y la diferenciación no es instantánea.
- 🎯 **Por qué importa:** La energía disponible decide si un cuerpo funde y se diferencia o permanece primitivo. La decisión central: ¿cuánto calor aporta un radionúclido sin pérdidas y cuánta energía libera la diferenciación?
- 🔗 **Se estudia junto con:** radionúclido de vida corta, energía de ligadura gravitatoria, régimen adiabático.

📘 **Dónde se aprende** (2 clases): [B52-C18 · Diferenciación planetaria](../programa/clases/B52/B52-C18-diferenciacion-planetaria/CLASE.md); [B53-C01 · Interior de planetas rocosos](../programa/clases/B53/B53-C01-interior-de-planetas-rocosos/CLASE.md).

### Diferenciación automática

- La diferenciación automática calcula derivadas exactas llevando valor y derivada juntos.

💡 **Cómo se explica en la clase [B09-C04](../programa/clases/B09/B09-C04-reglas-de-derivacion/CLASE.md):**
- Con números duales (laboratorio): exacta como las reglas, pero automática; es la base de la diferenciación automática de los programas modernos de simulación.
- 🎯 **Por qué importa:** La gravedad que siente un cuerpo depende de su distancia al astro: `g(r) = GM/r²`. La marea nace de que esa gravedad cambia de un lado a otro de un cuerpo extenso.
- 🔗 **Se estudia junto con:** regla de la potencia, regla de la suma, regla del producto, regla del cociente.

📘 **Dónde se aprende** (1 clase): [B09-C04 · Reglas de derivación](../programa/clases/B09/B09-C04-reglas-de-derivacion/CLASE.md).

### Diferencial

- El diferencial `du = g′(x) dx` es la regla que traduce `dx` a `du`.
- El diferencial conecta ambos balancines con el cuerpo de modo que el cabeceo del cuerpo es el promedio de los de los dos lados.

💡 **Cómo se explica en la clase [B09-C09](../programa/clases/B09/B09-C09-integracion-por-sustitucion/CLASE.md):**
- *Descripción textual:* se nombra la función interior `u`, se traduce el diferencial, se integra en `u` y se devuelve el resultado a `x`.
- 🎯 **Por qué importa:** La densidad del aire decae con la altitud de forma exponencial, y la masa de aire sobre un punto determina la presión y la extinción de la luz. Para obtenerla hay que integrar `e^{−h/H}`, que no es una integral básica: la variable aparece dentro de un exponente.
- 🔗 **Se estudia junto con:** sustitución, función interior, exterior, altura de escala.

📘 **Dónde se aprende** (2 clases): [B09-C09 · Integración por sustitución](../programa/clases/B09/B09-C09-integracion-por-sustitucion/CLASE.md); [B102-C04 · Suspensión rocker-bogie y mecánica de rovers](../programa/clases/B102/B102-C04-suspension-rocker-bogie-y-mecanica-de-rovers/CLASE.md).

### Dificultad

- La dificultad de un ítem es la proporción de respuestas correctas.
- La dificultad `p` es la proporción de aciertos del ítem (más alto = más fácil).

💡 **Cómo se explica en la clase [B130-C05](../programa/clases/B130/B130-C05-evaluacion-de-la-comprension-del-publico/CLASE.md):**
- *Descripción textual:* los dos cuestionarios dan la ganancia normalizada; el posterior da además dificultad, discriminación y fiabilidad; el remuestreo da un intervalo que dice si la categoría es estable.
- Calcular la dificultad y la discriminación de un ítem.
- 🎯 **Por qué importa:** Saber si la divulgación funcionó exige medir la comprensión; ninguna otra clase lo trata. La decisión central: ¿qué número resume la mejora del público, y cuánto se puede confiar en que no sea azar?
- 🔗 **Se estudia junto con:** ganancia normalizada de un grupo, discriminación, KR-20, alfa de Cronbach.

📘 **Dónde se aprende** (2 clases): [B130-C05 · Evaluación de la comprensión del público](../programa/clases/B130/B130-C05-evaluacion-de-la-comprension-del-publico/CLASE.md); [B131-C08 · Evaluación formativa en el aula de astronomía](../programa/clases/B131/B131-C08-evaluacion-formativa-en-el-aula-de-astronomia/CLASE.md).

### Difracción

- La difracción es la dispersión de la luz al pasar por una abertura, que fija un límite mínimo a la resolución.
- La difracción limita la resolución angular de una abertura circular de diámetro `D` a `θ ≈ 1,22 λ/D` (criterio de Rayleigh).

💡 **Cómo se explica en la clase [B01-C10](../programa/clases/B01/B01-C10-limitaciones-de-los-sentidos-humanos/CLASE.md):**
- Calcular el límite de resolución por difracción `θ = 1,22·λ/D` y su detalle lunar.
- 2,6 km es una cota teórica de difracción; la atmósfera, el enfoque y la óptica real la empeoran.
- ⚠️ **Error frecuente:** Tomar la cota de difracción como resolución real. Ejercicio 8.
- 🎯 **Por qué importa:** Si el ojo bastara, no habría observatorios. La luz visible es una franja pequeña del espectro electromagnético (S1, S2); además, tu pupila recoge poca luz, separa detalles hasta cierto tamaño y puede engañarte.
- 🔗 **Se estudia junto con:** rango espectral, sensibilidad, apertura, resolución angular.

📖 **Explicado a fondo:** [Difracción](esencial/esencial-d-l.md#difracción) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B01-C10 · Limitaciones de los sentidos humanos](../programa/clases/B01/B01-C10-limitaciones-de-los-sentidos-humanos/CLASE.md); [B05-C19 · Óptica y velocidad de la luz](../programa/clases/B05/B05-C19-optica-y-velocidad-de-la-luz/CLASE.md).

### Difusión

- La difusión (*broadcasting*) permite combinar arreglos de forma compatible, y falla con `ValueError` si no lo son.
- La difusión es la regla que permite operar arreglos de formas distintas.
- La difusión es la expansión de una práctica.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C02](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md):**
- La difusión es concisa y rápida, pero consume memoria `S·E·3` y puede volverse ilegible.
- La estrategia sensata: bucle para verificar, difusión para trabajar, biblioteca cuando el tamaño lo exija.
- 🎯 **Por qué importa:** Una constelación de seis satélites y cinco estaciones en tierra producen treinta distancias. Un catálogo de estrellas produce millones.
- 🔗 **Se estudia junto con:** arreglo, forma, ejes, tipo.

📘 **Dónde se aprende** (4 clases): [B07-C09 · Cálculos científicos básicos con Python](../programa/clases/B07/B07-C09-calculos-cientificos-basicos-con-python/CLASE.md); [B14-C02 · Arreglos multidimensionales NumPy](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md); [B18-C02 · Paso de mensajes con MPI](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md); [B119-C31 · Práctica estatal y costumbre internacional en el derecho espacial](../programa/clases/B119/B119-C31-practica-estatal-y-costumbre-internacional-en-el-derecho-espacial/CLASE.md).

### Difusión de fotones

- La difusión de fotones es la salida lenta de la radiación por un medio opaco.

💡 **Cómo se explica en la clase [B30-C01](../programa/clases/B30/B30-C01-estructura-interna-del-sol/CLASE.md):**
- *Descripción textual:* la gravedad y el equilibrio dan el politropo, del que salen las condiciones centrales; la gravedad también fija los tiempos de caída libre y de Kelvin–Helmholtz, y la estructura fija la difusión de fotones.
- Los cuatro casos de referencia son el politropo `n = 3`, el tiempo de caída libre, el de difusión de fotones y el de Kelvin–Helmholtz.
- 🎯 **Por qué importa:** Un Sol que pudiera colapsar en media hora, que tardara miles de años en dejar salir su luz y cuya energía no pudiera venir de la gravedad obliga a entender qué sostiene a una estrella. Sin un modelo mínimo de estructura, la actividad de las demás clases queda sin base.
- 🔗 **Se estudia junto con:** politropo, ecuación de Lane–Emden, tiempo de caída libre, tiempo de Kelvin–Helmholtz.

📘 **Dónde se aprende** (1 clase): [B30-C01 · Estructura interna del Sol](../programa/clases/B30/B30-C01-estructura-interna-del-sol/CLASE.md).

### Difusión del momento

- La difusión del momento mide `⟨(p_n − p_0)²⟩ = D n` en el mapa con `p` sin envolver.

💡 **Cómo se explica en la clase [B73-C15](../programa/clases/B73/B73-C15-difusion-orbital/CLASE.md):**
- Que no hay difusión: las curvas invariantes acotan el momento.
- 🎯 **Por qué importa:** Un conjunto de cuerpos en una región caótica no escapa de golpe: su excentricidad o su semieje se esparce como una caminata aleatoria, y el tiempo que tarda en recorrer una región fija la escala de supervivencia de la población. La decisión central: ¿cómo medir un coeficiente de difusión y cuándo no tiene sentido hablar de él?
- 🔗 **Se estudia junto con:** teoría cuasi-lineal, exponente de transporte, modos aceleradores, tiempo de difusión.

📘 **Dónde se aprende** (1 clase): [B73-C15 · Difusión orbital](../programa/clases/B73/B73-C15-difusion-orbital/CLASE.md).

### Difusión resistiva

- La difusión resistiva `η = 1/(μ₀σ)`.

💡 **Contexto en la clase [B30-C11](../programa/clases/B30/B30-C11-reconexion-magnetica/CLASE.md):**
- **Idea central (modelo mental):** Dos bandas elásticas con sentidos opuestos se acercan; en una capa estrecha se cortan y se vuelven a unir cruzadas, y salen disparadas. Cuanto más fina la capa, más lento entra el material.
- 🎯 **Por qué importa:** Las erupciones liberan en minutos una energía que el campo guardó durante mucho más tiempo, y el modelo más simple de reconexión es demasiado lento para eso. La decisión central: ¿qué tasa de reconexión hace falta y qué dice el modelo de Sweet–Parker?
- 🔗 **Se estudia junto con:** reconexión, hoja de corriente, número de Lundquist, tasa de reconexión.

📘 **Dónde se aprende** (1 clase): [B30-C11 · Reconexión magnética](../programa/clases/B30/B30-C11-reconexion-magnetica/CLASE.md).

### Difusividad

- La difusividad `κ = k/(ρ c)`.
- La difusividad `α = k/(ρc)`.

💡 **Cómo se explica en la clase [B77-C16](../programa/clases/B77/B77-C16-proteccion-termica/CLASE.md):**
- Paso 1 · Difusividad. `α = 0,5/(1500 × 1200) = 2,78·10⁻⁷ m²/s`.
- 🎯 **Por qué importa:** La temperatura de la cara trasera es la que decide si la estructura sobrevive. La decisión central: ¿cuánto del calor entrante se re-radia, cuánto se almacena y cuánto sube la temperatura trasera con un espesor dado?
- 🔗 **Se estudia junto con:** ecuación del calor, re-radiación, recesión, cara trasera adiabática.

📘 **Dónde se aprende** (2 clases): [B43-C11 · Dilatación térmica y estabilidad](../programa/clases/B43/B43-C11-dilatacion-termica-y-estabilidad/CLASE.md); [B77-C16 · Protección térmica](../programa/clases/B77/B77-C16-proteccion-termica/CLASE.md).

### Difusividad efectiva

- La difusividad efectiva `D_e` mide qué tan fácil se mueve el soluto en la película.

💡 **Cómo se explica en la clase [B64-C06](../programa/clases/B64/B64-C06-biofilms-en-ambientes-extremos/CLASE.md):**
- Para calcular, usas una película sintética: difusividad efectiva `D_e = 10⁻⁹ m²/s`, concentración superficial `S₀ = 0,25 mol/m³` y espesores de 20 a 500 µm.
- 🎯 **Por qué importa:** Una película de células y matriz crea su propio microambiente. La pregunta motivadora: ¿hasta qué profundidad llega un nutriente en un biofilm y qué sucede con las células que quedan más adentro?
- 🔗 **Se estudia junto con:** matriz de EPS, constante de consumo, módulo de Thiele, factor de efectividad.

📘 **Dónde se aprende** (1 clase): [B64-C06 · Biofilms en ambientes extremos](../programa/clases/B64/B64-C06-biofilms-en-ambientes-extremos/CLASE.md).

### Difusividad magnética

- La difusividad magnética es `η_m = 1/(μ₀σ)`.

💡 **Contexto en la clase [B65-C02](../programa/clases/B65/B65-C02-dinamos-planetarias-y-campos-magneticos-de-origen-interno/CLASE.md):**
- **Idea central (modelo mental):** Un dínamo de bicicleta convierte movimiento en electricidad; una dinamo planetaria es un dínamo cuyo campo lo produce el propio fluido en movimiento. Sin movimiento, el campo se apaga como una rueda que se frena.
- 🎯 **Por qué importa:** La presencia o ausencia de un campo global dice si un cuerpo tiene un fluido conductor en movimiento. La decisión central: ¿qué intensidad de campo permite un núcleo y cuánto duraría ese campo si el movimiento se detuviera?
- 🔗 **Se estudia junto con:** dinamo, número de Reynolds magnético, número de Elsasser, tiempo de decaimiento óhmico.

📘 **Dónde se aprende** (1 clase): [B65-C02 · Dinamos planetarias y campos magnéticos de origen interno](../programa/clases/B65/B65-C02-dinamos-planetarias-y-campos-magneticos-de-origen-interno/CLASE.md).

### Difusividad térmica

- La difusividad térmica `κ` mide qué tan rápido se difunde el calor.

💡 **Contexto en la clase [B52-C17](../programa/clases/B52/B52-C17-colisiones-y-evolucion-termica/CLASE.md):**
- **Idea central (modelo mental):** Como una olla de sopa que se enfría desde la pared: el centro tarda en enterarse. Límite: conducción pura, simetría esférica, `κ` constante y sin fuentes internas.
- 🎯 **Por qué importa:** El calor determina si un cuerpo funde, se diferencia o se enfría rápido. La decisión central: ¿cuánto tarda un cuerpo en perder su calor y cuánto lo calienta un impacto?
- 🔗 **Se estudia junto con:** escala de enfriamiento, energía de impacto específica, fracción termalizada, Crank–Nicolson.

📘 **Dónde se aprende** (1 clase): [B52-C17 · Colisiones y evolución térmica](../programa/clases/B52/B52-C17-colisiones-y-evolucion-termica/CLASE.md).

### Dijkstra

- La heurística octil estima el costo con movimientos ortogonales y diagonales. Dijkstra es A* con `h = 0`.
- El cordón de seguridad ata a la persona a un anclaje; limita la distancia al anclaje. Dijkstra es el algoritmo que halla el camino de menor coste con costes no negativos.

💡 **Cómo se explica en la clase [B97-C08](../programa/clases/B97/B97-C08-planificacion-de-trayectorias-roboticas/CLASE.md):**
- Dijkstra, `1238`: un ahorro de `0,353` (como fracción de los nodos de Dijkstra).
- La diferencia de costo con Dijkstra es `0,00e+00`.
- 🎯 **Por qué importa:** Con retardo de comunicación y poca energía, la ruta debe salir buena a la primera. A* garantiza la ruta de costo mínimo si la heurística es admisible, y ahorra cómputo, que a bordo es escaso.
- 🔗 **Se estudia junto con:** rejilla de costos, A*, heurística octil, óptima.

📘 **Dónde se aprende** (2 clases): [B97-C08 · Planificación de trayectorias robóticas](../programa/clases/B97/B97-C08-planificacion-de-trayectorias-roboticas/CLASE.md); [B108-C02 · Planificación de desplazamientos y rutas de EVA](../programa/clases/B108/B108-C02-planificacion-de-desplazamientos-y-rutas-de-eva/CLASE.md).

### Dilatación

- La dilatación `α` desplaza el pico.

💡 **Cómo se explica en la clase [B36-C07](../programa/clases/B36/B36-C07-oscilaciones-acusticas-barionicas-como-regla-estandar/CLASE.md):**
- Ajustar la dilatación α de un pico sintético.
- 🎯 **Por qué importa:** Una regla estándar permite medir distancias si se conoce su longitud. La decisión central: ¿cuánto mide la regla y cuál es la precisión con que se puede medir su dilatación?
- 🔗 **Se estudia junto con:** horizonte sonoro, velocidad del sonido, carga bariónica, igualdad materia–radiación.

📘 **Dónde se aprende** (1 clase): [B36-C07 · Oscilaciones acústicas bariónicas como regla estándar](../programa/clases/B36/B36-C07-oscilaciones-acusticas-barionicas-como-regla-estandar/CLASE.md).

### Dilatación temporal

- La dilatación temporal relaciona ambos: `t = γτ`.

💡 **Cómo se explica en la clase [B26-C03](../programa/clases/B26/B26-C03-dilatacion-temporal-y-contraccion/CLASE.md):**
- Enunciar la dilatación temporal `Δt = γ Δτ` y la contracción `L = L₀/γ`.
- python programa/clases/B26/B26-C03-dilatacion-temporal-y-contraccion/muon.py
- 🎯 **Por qué importa:** Los muones se producen en la alta atmósfera por rayos cósmicos, viven microsegundos y, sin embargo, llegan al suelo en cantidad. Los relojes de satélites de navegación se ajustan por el mismo efecto.
- 🔗 **Se estudia junto con:** tiempo propio, tiempo coordenado, longitud propia, contracción de longitudes.

📘 **Dónde se aprende** (1 clase): [B26-C03 · Dilatación temporal y contracción](../programa/clases/B26/B26-C03-dilatacion-temporal-y-contraccion/CLASE.md).

### Diligencia debida

- La diligencia debida es la información sobre fabricante y lanzador que prueba que la red se construirá.
- La diligencia debida exige probar que una red será realmente construida.

💡 **Cómo se explica en la clase [B120-C03](../programa/clases/B120/B120-C03-posiciones-orbitales-y-espectro-como-recursos-limitados/CLASE.md):**
- Con diligencia debida, cada país conserva solo lo que usará y lo liberado se reparte de nuevo: 21 países sirven (Gini 0,725).
- El mismo documento describe dos mecanismos: la coordinación «primero en llegar, primero en ser servido» y los planes a priori (Apéndices 30, 30A y 30B), y explica que la diligencia debida administrativa busca evitar reservar capacidad sin uso real.
- 🎯 **Por qué importa:** Las posiciones orbitales y el espectro son recursos escasos con reglas de asignación y no están tratados como concepto jurídico. La decisión central: ¿cuánto recurso hay, quién lo obtiene bajo cada régimen y qué mide la desigualdad del reparto?
- 🔗 **Se estudia junto con:** recurso limitado, acceso equitativo, orden de llegada, planificación a priori.

📘 **Dónde se aprende** (2 clases): [B120-C03 · Posiciones orbitales y espectro como recursos limitados](../programa/clases/B120/B120-C03-posiciones-orbitales-y-espectro-como-recursos-limitados/CLASE.md); [B120-C04 · Documentación regulatoria de un sistema satelital](../programa/clases/B120/B120-C04-documentacion-regulatoria-de-un-sistema-satelital/CLASE.md).

### Dilución

- La dilución es la caída de `Pc` al crecer la incertidumbre muy por encima del tamaño del disco.
- La dilución es la baja del porcentaje por acciones nuevas.
- La dilución reduce la profundidad.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B29-C08](../programa/clases/B29/B29-C08-falsos-positivos-de-transito/CLASE.md):**
- Paso 2 · Dilución. `0,2 × 0,01/1,01 = 1,980 × 10⁻³`.
- Ejercicio 12 · integrador. Elabora tu *ficha de una prueba par–impar*: tabla de dilución, error, falsas alarmas, potencia y eclipses necesarios.
- ⚠️ **Error frecuente:** Olvidar la dilución. Se corrige con el ejemplo 13.
- 🎯 **Por qué importa:** Una pequeña fracción de falsos positivos contamina cualquier muestra de planetas. Conocer qué pruebas los detectan, con qué potencia y con qué falsas alarmas, permite diseñar cribados honestos.
- 🔗 **Se estudia junto con:** falso positivo, prueba par–impar, tasa de falsas alarmas, potencia.

📘 **Dónde se aprende** (5 clases): [B29-C08 · Falsos positivos de tránsito](../programa/clases/B29/B29-C08-falsos-positivos-de-transito/CLASE.md); [B74-C27 · Navegación por púlsares de rayos X como técnica de investigación](../programa/clases/B74/B74-C27-navegacion-por-pulsares-de-rayos-x-como-tecnica-de-investigacion/CLASE.md); [B106-C17 · Prevención y respuesta a incendios](../programa/clases/B106/B106-C17-prevencion-y-respuesta-a-incendios/CLASE.md); [B118-C06 · Probabilidad de colisión](../programa/clases/B118/B118-C06-probabilidad-de-colision/CLASE.md); [B126-C01 · Capital semilla y financiamiento inicial](../programa/clases/B126/B126-C01-capital-semilla-y-financiamiento-inicial/CLASE.md).

### Dilución de la precisión

- La dilución de la precisión `√tr[(HᵀH)⁻¹]` mide la geometría.
- La dilución de la precisión (DOP) es `√tr[(HᵀH)⁻¹]`: cuánto amplifica la geometría el ruido de la medida.
- La dilución de la precisión `DOP` viene de `(GᵀG)⁻¹`;

💡 **Cómo se explica en la clase [B74-C05](../programa/clases/B74/B74-C05-sesgos-de-estaciones-terrestres/CLASE.md):**
- *Descripción textual:* la geometría, el ruido, los sesgos y los errores de posición de estación entran en el ajuste y determinan el error 3D; la geometría fija la dilución de la precisión.
- ⚠️ **Error frecuente:** Ignorar la geometría. Calcula la dilución de la precisión antes, como en 8.1.
- 🎯 **Por qué importa:** Un error sistemático no se promedia: un sesgo de 3 m en cada estación no desaparece con más medidas. La decisión central: ¿qué sesgo conviene estimar, cuál conviene solo reconocer en la covarianza y cuándo el remedio empeora el problema?
- 🔗 **Se estudia junto con:** sesgo de alcance, error de posición de estación, matriz de diseño, de consideración.

📘 **Dónde se aprende** (3 clases): [B74-C05 · Sesgos de estaciones terrestres](../programa/clases/B74/B74-C05-sesgos-de-estaciones-terrestres/CLASE.md); [B74-C15 · Geometría de la red de seguimiento](../programa/clases/B74/B74-C15-geometria-de-la-red-de-seguimiento/CLASE.md); [B89-C16 · GNSS como navegación de satélites](../programa/clases/B89/B89-C16-gnss-como-navegacion-de-satelites/CLASE.md).

### Dilución del haz

- La dilución del haz es la fracción del haz llena por la fuente.

💡 **Cómo se explica en la clase [B46-C05](../programa/clases/B46/B46-C05-ganancia-y-temperatura-de-antena/CLASE.md):**
- Si la linterna ilumina solo parte del cuadro, la lectura promedia la zona luminosa con la oscura; la dilución es esa fracción.
- Ejercicio 12. Integrador. Elabora tu *ficha de la ganancia y la temperatura de antena*: `A_e`, `Γ` y `T_A` con su dilución.
- 🎯 **Por qué importa:** Para saber cuánto flujo hay en una fuente hay que conocer cuánta fracción del haz llena. La decisión central: ¿cuánto vale la temperatura de antena de una fuente extensa en un haz dado?
- 🔗 **Se estudia junto con:** temperatura de antena, área efectiva, sensibilidad, ángulo sólido del haz.

📘 **Dónde se aprende** (1 clase): [B46-C05 · Ganancia y temperatura de antena](../programa/clases/B46/B46-C05-ganancia-y-temperatura-de-antena/CLASE.md).

### Diluyente

- Normoxia: `PIO₂` de 145 a 155 mmHg. Diluyente: gas inerte de la mezcla (al menos 30 %).

💡 **Cómo se explica en la clase [B106-C03](../programa/clases/B106/B106-C03-composicion-atmosferica-respirable/CLASE.md):**
- O₂ puro a 4,3 psia da 175,4 mmHg pero incumple el diluyente y el rango de presión.
- *Descripción textual:* una atmósfera es aceptable si cumple a la vez normoxia, diluyente mínimo y rango de presión total.
- 🎯 **Por qué importa:** El cuerpo no responde a la fracción de oxígeno sino a su presión parcial; bajar la presión total exige subir la fracción, y eso trae riesgo de incendio (C17). La decisión central: ¿qué par presión–composición da normoxia dentro de los límites consultados?
- 🔗 **Se estudia junto con:** Presión parcial inspirada de O₂ (PIO₂), Normoxia, Psia, Ebullismo.

📘 **Dónde se aprende** (1 clase): [B106-C03 · Composición atmosférica respirable](../programa/clases/B106/B106-C03-composicion-atmosferica-respirable/CLASE.md).

### Dimensión

- La dimensión de una magnitud indica de qué unidades base depende y con qué exponentes.
- Una dimensión es la naturaleza de la magnitud expresada con las magnitudes base: la dimensión de la velocidad es longitud / tiempo, sea cual sea la unidad que uses.
- La dimensión es el número de vectores de cualquier base.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C06](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md):**
- F --> C{"¿Ambos lados tienen la misma dimensión?"}
- *Descripción textual:* las unidades base generan las derivadas; estas aparecen en una fórmula; una pregunta decide si ambos lados tienen la misma dimensión: si sí, la fórmula es coherente; si no, hay un error.
- 🎯 **Por qué importa:** El 23 de septiembre de 1999 la NASA perdió contacto con la sonda Mars Climate Orbiter. Según la agencia, un error de navegación se debió a no traducir unidades inglesas a métricas: el programa en tierra usaba unas y el de la nave otras, y la sonda pasó demasiado cerca de Marte y se quemó en su atmósfera (S1).
- 🔗 **Se estudia junto con:** magnitud, unidad, SI, unidades base.

📘 **Dónde se aprende** (5 clases): [B03-C06 · Unidades del Sistema Internacional](../programa/clases/B03/B03-C06-unidades-del-sistema-internacional/CLASE.md); [B05-C01 · Magnitudes físicas y dimensiones](../programa/clases/B05/B05-C01-magnitudes-fisicas-y-dimensiones/CLASE.md); [B10-C02 · Bases y dimensión](../programa/clases/B10/B10-C02-bases-y-dimension/CLASE.md); [B13-C02 · Dimensiones y trazabilidad](../programa/clases/B13/B13-C02-dimensiones-y-trazabilidad/CLASE.md); [B14-C04 · Unidades y constantes con Astropy](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md).

### Dimensionalmente consistente

- Una ecuación es dimensionalmente consistente si ambos miembros tienen el mismo vector y solo se suman términos de igual dimensión.

💡 **Contexto en la clase [B13-C02](../programa/clases/B13/B13-C02-dimensiones-y-trazabilidad/CLASE.md):**
- **Idea central (modelo mental):** El análisis dimensional es un filtro de sentido que se aplica en papel, antes de calcular. La trazabilidad es una cadena de custodia de la confianza: cada eslabón compara un instrumento con otro más preciso hasta llegar a la definición de la unidad.
- 🎯 **Por qué importa:** Un satélite recibe un comando con un tiempo de encendido de motor; el ingeniero de tierra usó una fórmula del periodo orbital copiada de una hoja de cálculo. Si la fórmula está mal dimensionada, el resultado sale en «segundos al cuadrado» o en «metros por segundo» sin que nadie lo note.
- 🔗 **Se estudia junto con:** dimensión, M, L, T.

📘 **Dónde se aprende** (1 clase): [B13-C02 · Dimensiones y trazabilidad](../programa/clases/B13/B13-C02-dimensiones-y-trazabilidad/CLASE.md).

### Dimensiones

- Las dimensiones de una magnitud son sus bases (longitud L, tiempo T, masa M); el análisis dimensional comprueba que ambos lados de una ecuación tengan las mismas dimensiones.

💡 **Cómo se explica en la clase [B01-C08](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md):**
- Antes de calcular, comprueba dimensiones.
- ⚠️ **Error frecuente:** Fórmulas con dimensiones incorrectas. Ejercicios 3 y 10.
- 🎯 **Por qué importa:** En 1999 se perdió la sonda Mars Climate Orbiter por una discrepancia entre unidades inglesas y métricas (C04, fuente NASA). La ciencia estaba bien; la conversión, no.
- 🔗 **Se estudia junto con:** Sistema Internacional (SI), unidades base, unidad derivada, unidad no SI aceptada.

📘 **Dónde se aprende** (1 clase): [B01-C08 · Mediciones y unidades astronómicas](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md).

### DIMM

- Parámetro de Fried `r₀`: diámetro de coherencia de la turbulencia. DIMM: monitor de movimiento diferencial de imagen.

💡 **Contexto en la clase [B48-C12](../programa/clases/B48/B48-C12-monitorizacion-de-seeing/CLASE.md):**
- **Idea central (modelo mental):** Dos corchos en el oleaje: lo que importa no es cuánto sube cada uno sino cuánto cambia su distancia; más turbulencia, más cambio.
- 🎯 **Por qué importa:** Sin medir el seeing, no se sabe si una noche sirve para un programa. La decisión central: ¿cuántas medidas hacen falta para que `r₀` tenga una incertidumbre aceptable?
- 🔗 **Se estudia junto con:** Parámetro de Fried, Varianza longitudinal, Seeing, Kolmogorov.

📘 **Dónde se aprende** (1 clase): [B48-C12 · Monitorización de seeing](../programa/clases/B48/B48-C12-monitorizacion-de-seeing/CLASE.md).

### Dinámica

- La dinámica es la de Euler (C17) con tensor de inercia completo.

💡 **Cómo se explica en la clase [B16-C20](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md):**
- La cinemática `q̇ = ½ q ⊗ [0, ω]` conserva la norma de `q` de forma exacta en tiempo continuo; la dinámica es `J ω̇ = −ω × (J ω) + u`.
- Escribir la cinemática y la dinámica de un cuerpo rígido en tres ejes.
- 🎯 **Por qué importa:** Un telescopio debe girar desde una orientación a otra y quedarse allí. Con tres ejes acoplados y rotaciones grandes, ni los ángulos de Euler (tienen singularidades y dependen de la secuencia de giros) ni el modelo lineal bastan.
- 🔗 **Se estudia junto con:** cuaternión unitario, producto de cuaterniones, cuaternión de error, cinemática.

📘 **Dónde se aprende** (1 clase): [B16-C20 · Control de orientación en un simulador](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md).

### Dinamo

- La dinamo es la conversión de energía cinética de un fluido conductor en energía magnética.

💡 **Cómo se explica en la clase [B65-C02](../programa/clases/B65/B65-C02-dinamos-planetarias-y-campos-magneticos-de-origen-interno/CLASE.md):**
- Un dínamo de bicicleta convierte movimiento en electricidad; una dinamo planetaria es un dínamo cuyo campo lo produce el propio fluido en movimiento.
- Límite: son escalas, no una simulación de dinamo.
- ⚠️ **Error frecuente:** Confundir `Rm` grande con la existencia de dinamo. Se corrige con la sección 6: `Rm` es una condición necesaria, no suficiente.
- 🎯 **Por qué importa:** La presencia o ausencia de un campo global dice si un cuerpo tiene un fluido conductor en movimiento. La decisión central: ¿qué intensidad de campo permite un núcleo y cuánto duraría ese campo si el movimiento se detuviera?
- 🔗 **Se estudia junto con:** número de Reynolds magnético, número de Elsasser, tiempo de decaimiento óhmico, difusividad magnética.

📘 **Dónde se aprende** (1 clase): [B65-C02 · Dinamos planetarias y campos magnéticos de origen interno](../programa/clases/B65/B65-C02-dinamos-planetarias-y-campos-magneticos-de-origen-interno/CLASE.md).

### Dioptría

- La dioptría (D) es 1/m.

💡 **Cómo se explica en la clase [B105-C05](../programa/clases/B105/B105-C05-cambios-de-vision/CLASE.md):**
- *Descripción textual:* el desplazamiento de líquidos presiona el globo; el acortamiento axial se convierte en dioptrías con la sensibilidad `n/L²` y se estima cuántas personas de una población sintética superan un umbral.
- Equivalente textual: 0,37 mm de acortamiento equivalen a una dioptría.
- 🎯 **Por qué importa:** Una variación de décimas de milímetro puede cambiar la refracción en fracciones de dioptría y comparar eso con el error de medida decide si un cambio es real. La decisión central: ¿cuántos milímetros de acortamiento equivalen a una dioptría y cuántas personas la superarían?
- 🔗 **Se estudia junto con:** ojo reducido, desplazamiento hipermetrópico, acortamiento axial, presión intracraneal.

📘 **Dónde se aprende** (1 clase): [B105-C05 · Cambios de visión](../programa/clases/B105/B105-C05-cambios-de-vision/CLASE.md).

### Dipolo

- Un dipolo son dos cargas opuestas muy próximas.
- El dipolo es la anisotropía `1 + d cos θ`.
- El dipolo es el campo de orden más bajo.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C15](../programa/clases/B05/B05-C15-campos-electricos/CLASE.md):**
- Un dipolo de separación `d` y carga `e`, a una distancia `r ≫ d` sobre su eje, da `E ≈ 2 k_e p/r³` con `p = e d`: decae más rápido (`1/r³`) que una carga sola.
- Ejercicio 10 · transferencia. Un compañero afirma que el campo de un dipolo cae como `1/r²`.
- ⚠️ **Error frecuente:** Aplicar `1/r²` a un dipolo. Ejercicio 10.
- 🎯 **Por qué importa:** El espacio está lleno de partículas cargadas que un satélite atraviesa, y un satélite puede acumular carga. La pregunta motivadora es: ¿cómo describir la fuerza eléctrica sobre una carga sin conocer a la vez todas las demás, y cuánto más fuerte es que la gravedad?
- 🔗 **Se estudia junto con:** carga eléctrica, carga elemental, ley de Coulomb, campo eléctrico.

📘 **Dónde se aprende** (5 clases): [B05-C15 · Campos eléctricos](../programa/clases/B05/B05-C15-campos-electricos/CLASE.md); [B28-C04 · Rayos cósmicos de alta energía](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md); [B30-C15 · Magnetosfera terrestre](../programa/clases/B30/B30-C15-magnetosfera-terrestre/CLASE.md); [B49-C01 · Antenas de hilo: dipolo, monopolo e impedancia de radiación](../programa/clases/B49/B49-C01-antenas-de-hilo-dipolo-monopolo-e-impedancia-de-radiacion/CLASE.md); [B87-C16 · Detumbling después del despliegue](../programa/clases/B87/B87-C16-detumbling-despues-del-despliegue/CLASE.md).

### Dipolo de enlace

- Un dipolo de enlace es el desplazamiento de carga en un enlace polar, representado como un vector.

💡 **Cómo se explica en la clase [B06-C05](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md):**
- Si cada enlace tiene un dipolo de la misma magnitud, la suma depende sólo de la geometría.
- En el agua angular con 104,48°, la suma tiene módulo `2 cos(52,24°) = 1,2247` (en unidades del dipolo de enlace): molécula polar.
- 🎯 **Por qué importa:** El dióxido de carbono es el 95,1 % de la atmósfera de Marte en volumen (S2), y los hielos de las nubes densas del medio interestelar contienen, según un estudio con el telescopio James Webb, agua y CO₂ entre otras especies (S3, que se leyó sólo en resumen).
- 🔗 **Se estudia junto con:** dominio de electrones, modelo de repulsión de pares de valencia, geometría electrónica, forma molecular.

📘 **Dónde se aprende** (1 clase): [B06-C05 · Moléculas y geometría molecular](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md).

### Dipolo magnético en rotación

- El dipolo magnético en rotación pierde energía por radiación dipolar.

💡 **Cómo se explica en la clase [B27-C05](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md):**
- Un dipolo magnético de campo ecuatorial `B` y radio `R` que rota con `ω` radia en el vacío `P_rad = (8π/3) B² R⁶ ω⁴/(μ₀c³)`.
- Explicar el modelo del dipolo magnético en rotación.
- 🎯 **Por qué importa:** Un púlsar da, a la vez, un reloj de precisión, la medida de su campo magnético y, en una binaria, la masa de las estrellas y una prueba de la relatividad general. La decisión central: dados el periodo y su derivada, ¿qué campo, edad y potencia de frenado tiene el púlsar y qué se aprende de su binaria?
- 🔗 **Se estudia junto con:** púlsar, periodo, campo ecuatorial, edad característica.

📘 **Dónde se aprende** (1 clase): [B27-C05 · Púlsares y relojes naturales](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md).

### Dipolo residual

- El dipolo residual da `τ_m = m_res B`.

💡 **Cómo se explica en la clase [B87-C18](../programa/clases/B87/B87-C18-estabilidad-ante-perturbaciones/CLASE.md):**
- El dipolo residual domina con estos valores de ejemplo (`m_res = 0,01 A·m²`); si el dipolo fuera diez veces menor, el gradiente de gravedad mandaría.
- A `500 km`, con `I = diag(0,35; 0,40; 0,30)`: gradiente de gravedad `184 nN·m`, resistencia `19,1 nN·m`, presión solar `4,10 nN·m` y dipolo residual `498 nN·m`.
- 🎯 **Por qué importa:** El presupuesto de par decide el tamaño de las ruedas y de los magnetopares. La decisión central: ¿qué perturbación domina, qué error permanente deja en el lazo y se mantiene la estabilidad?
- 🔗 **Se estudia junto con:** gradiente de gravedad, resistencia, presión solar, error permanente.

📘 **Dónde se aprende** (1 clase): [B87-C18 · Estabilidad ante perturbaciones](../programa/clases/B87/B87-C18-estabilidad-ante-perturbaciones/CLASE.md).

### Dirección

- Su dirección `φ` se mide desde la velocidad (0 = tangencial).

💡 **Cómo se explica en la clase [B75-C22](../programa/clases/B75/B75-C22-modelos-de-primer-impulso/CLASE.md):**
- *Descripción textual:* El impulso y su dirección dan el vector velocidad; de él salen la energía y el momento, los elementos y el apoapsis; el semieje da el tiempo hasta el apoapsis.
- Analogía: lanzar una piedra a una altura: se alcanza más alto lanzando en la dirección óptima.
- 🎯 **Por qué importa:** Antes de optimizar toda la misión conviene entender el primer impulso. La decisión central: ¿qué módulo y qué dirección del primer impulso alcanzan un radio dado con el menor delta-v y en cuánto tiempo?
- 🔗 **Se estudia junto con:** primer impulso, familia tangencial, apoapsis alcanzado, tiempo hasta el apoapsis.

📘 **Dónde se aprende** (1 clase): [B75-C22 · Modelos de primer impulso](../programa/clases/B75/B75-C22-modelos-de-primer-impulso/CLASE.md).

### Dirección de azimut

- La dirección de azimut es la de vuelo; el alcance oblicuo `R` es la distancia al blanco.

💡 **Contexto en la clase [B69-C01](../programa/clases/B69/B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md):**
- **Idea central (modelo mental):** Una sirena que se acerca suena más aguda y, al alejarse, más grave; el cambio ocurre más rápido cuanto más cerca pasa. El satélite «oye» lo mismo de cada blanco: una frecuencia que baja de forma casi lineal mientras el blanco cruza el haz. Cuanta más variación de frecuencia se registra, más fino se localiza el blanco.
- 🎯 **Por qué importa:** Sin el principio Doppler, la resolución en azimut de un radar quedaría fijada por el ancho del haz de la antena: a 850 km, una antena de 12 m (λ = 0,0555 m) iluminaría una franja de unos 3,9 km. La decisión central: ¿qué resolución obtiene el sistema, de qué depende y qué hay que muestrear para no perderla?
- 🔗 **Se estudia junto con:** alcance oblicuo, apertura sintética, frecuencia Doppler, tasa Doppler.

📘 **Dónde se aprende** (1 clase): [B69-C01 · Principio Doppler y resolución en azimut del SAR](../programa/clases/B69/B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md).

### Dirección de máximo crecimiento

- La dirección de máximo crecimiento es `∇f/|∇f|` y el ritmo máximo es `|∇f|`.

💡 **Cómo se explica en la clase [B09-C17](../programa/clases/B09/B09-C17-gradiente-y-derivada-direccional/CLASE.md):**
- B --> C["Dirección ∇f/|∇f|:<br/>máximo crecimiento, ritmo |∇f|"]
- Determinar la dirección de máximo y mínimo crecimiento y su valor.
- 🎯 **Por qué importa:** La gravedad no es un número: es un vector que apunta a un lado y tiene una magnitud. En un campo con dos cuerpos, como Tierra–Luna, esa dirección cambia de punto a punto.
- 🔗 **Se estudia junto con:** gradiente, derivada direccional, vector unitario, curva de nivel.

📘 **Dónde se aprende** (1 clase): [B09-C17 · Gradiente y derivada direccional](../programa/clases/B09/B09-C17-gradiente-y-derivada-direccional/CLASE.md).

### Direccionamiento por contenido

- El direccionamiento por contenido guarda cada objeto bajo su hash: el nombre *es* el contenido.

💡 **Cómo se explica en la clase [B14-C11](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md):**
- Explicar el direccionamiento por contenido y por qué deduplica automáticamente.
- 🎯 **Por qué importa:** Un análisis usó «la tabla de catálogo de octubre». En noviembre alguien reemplazó el archivo por otro con el mismo nombre.
- 🔗 **Se estudia junto con:** suma de verificación, función de hash criptográfica, deduplicación, manifiesto.

📘 **Dónde se aprende** (1 clase): [B14-C11 · Control de versiones de datos](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md).

### Directa

- Una órbita es directa si `i < 90°` y retrógrada si `i > 90°`.

💡 **Cómo se explica en la clase [B04-C14](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md):**
- La componente `z` es `cos i`: positiva si `i < 90°` (directa) y negativa si `i > 90°` (retrógrada).
- E -->|"> 0"| F["Órbita directa (i < 90°)"]
- 🎯 **Por qué importa:** Una órbita no es solo una forma (C09): es una forma colocada en el espacio con una orientación. ¿Hacia dónde apunta su plano?
- 🔗 **Se estudia junto con:** producto vectorial, regla de la mano derecha, anticonmutativo, normal a un plano.

📘 **Dónde se aprende** (1 clase): [B04-C14 · Producto vectorial y orientación](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md).

### Directamente proporcionales

- Dos magnitudes son directamente proporcionales si su cociente `y/x` es constante: `y = kx`.

💡 **Cómo se explica en la clase [B03-C10](../programa/clases/B03/B03-C10-proporcionalidad-directa-e-inversa/CLASE.md):**
- Ejercicio 1 · con los pasos indicados. Decide si `x = 1, 2, 3` e `y = 2,5; 5; 7,5` son directamente proporcionales y halla `k`.
- Ejercicio 8. Con `T/a` de la Tierra (1) y de Marte (`1,881/1,5238 = 1,234`), ¿es `T` directamente proporcional a `a`?
- 🎯 **Por qué importa:** Un panel solar en órbita de Marte no recibe la misma energía que uno en órbita de la Tierra. ¿Cuánta menos?
- 🔗 **Se estudia junto con:** inversamente proporcionales, constante de proporcionalidad, lineal, ley del inverso del cuadrado.

📘 **Dónde se aprende** (1 clase): [B03-C10 · Proporcionalidad directa e inversa](../programa/clases/B03/B03-C10-proporcionalidad-directa-e-inversa/CLASE.md).

### Directividad

- La directividad `D` es el cociente entre la intensidad máxima y la media.
- La directividad `D` es el cociente entre la intensidad de radiación máxima y la que tendría una fuente isótropa con la misma potencia radiada: `D = 4π U_max/∫U dΩ`.
- La directividad compara con una antena isótropa.

💡 **Cómo se explica en la clase [B46-C03](../programa/clases/B46/B46-C03-antenas-parabolicas/CLASE.md):**
- La directividad numérica es `134522,2` y la analítica `(πD/λ)² = 134522,3`.
- Duplicar el diámetro divide el haz por 2 y multiplica la directividad por 4.
- 🎯 **Por qué importa:** El tamaño de la antena fija a la vez la resolución y la sensibilidad. La decisión central: ¿qué diámetro y qué razón focal dan el haz y la ganancia requeridos?
- 🔗 **Se estudia junto con:** paraboloide, razón focal, patrón de Airy, ancho a media potencia.

📘 **Dónde se aprende** (3 clases): [B46-C03 · Antenas parabólicas](../programa/clases/B46/B46-C03-antenas-parabolicas/CLASE.md); [B49-C01 · Antenas de hilo: dipolo, monopolo e impedancia de radiación](../programa/clases/B49/B49-C01-antenas-de-hilo-dipolo-monopolo-e-impedancia-de-radiacion/CLASE.md); [B91-C01 · Fundamentos de teoría de antenas](../programa/clases/B91/B91-C01-fundamentos-de-teoria-de-antenas/CLASE.md).

### Directorio de teselas

- Un directorio de teselas dice dónde empieza cada una y cuántos bytes ocupa.

💡 **Cómo se explica en la clase [B14-C26](../programa/clases/B14/B14-C26-formatos-de-datos-raster-geoespaciales-geotiff-y-cog/CLASE.md):**
- El archivo didáctico guarda 64 teselas de 128 × 128 `float32` (65 536 bytes cada una) tras una cabecera y un directorio de 64 pares (desplazamiento, bytes).
- El lector calcula cuáles, lee cabecera y directorio más esas 4 teselas, ensambla la región y lee en total 263 184 bytes, el 6,3 % del archivo (`16 + 16·64 + 4·65 536 = 263 184`).
- 🎯 **Por qué importa:** Una escena de satélite pesa cientos de megabytes y tú necesitas un recuadro de 100 × 120 píxeles. Si el formato obliga a leer todo el archivo, gastas tiempo y ancho de banda.
- 🔗 **Se estudia junto con:** ráster, GeoTIFF, tesela, pirámide.

📘 **Dónde se aprende** (1 clase): [B14-C26 · Formatos de datos ráster geoespaciales: GeoTIFF y COG](../programa/clases/B14/B14-C26-formatos-de-datos-raster-geoespaciales-geotiff-y-cog/CLASE.md).

### Directorio de trabajo

- El directorio de trabajo es la carpeta en la que «estás parado»; los comandos y `open()` relativos se resuelven desde ahí.

💡 **Cómo se explica en la clase [B07-C15](../programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/CLASE.md):**
- El sistema de archivos es un árbol; el directorio de trabajo es un punto marcado en él.
- T["directorio de trabajo<br/>(puede ser cualquiera)"] -.-> R
- 🎯 **Por qué importa:** Una causa muy común de «el programa no encuentra el archivo» es que la ruta funciona en el computador del autor y no en otro: se escribió con `C:\Usuarios\ana\datos\...`, o se asumió que el programa se ejecuta desde cierta carpeta.
- 🔗 **Se estudia junto con:** terminal, intérprete de comandos, ruta, absoluta.

📘 **Dónde se aprende** (1 clase): [B07-C15 · Terminal y rutas de archivos](../programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/CLASE.md).

### Directriz

- Todas cumplen la propiedad foco–directriz: hay un punto (el foco) y una recta (la directriz) tales que la distancia de cada punto de la curva al foco es `e` veces su distancia a la directriz;
- Una directriz es una recomendación.

💡 **Cómo se explica en la clase [B04-C18](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md):**
- Con la directriz `x = p/e` (si `e > 0`), todo punto `P = (r cos θ, r sen θ)` cumple `r = e (p/e − r cos θ)`, que reproduce la ecuación común: `r + e r cos θ = p`.
- Comprobar la propiedad foco–directriz `|PF| = e·d(P, directriz)`.
- 🎯 **Por qué importa:** En 2017 se descubrió un objeto que cruzaba el sistema solar con una órbita que no se cerraba: su excentricidad era mayor que 1. Eso significó que no estaba ligado al Sol: venía de fuera y se iba.
- 🔗 **Se estudia junto con:** cónica, propiedad foco–directriz, foco, excentricidad.

📘 **Dónde se aprende** (2 clases): [B04-C18 · Cónicas y secciones orbitales](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md); [B118-C19 · Sostenibilidad y gobernanza orbital](../programa/clases/B118/B118-C19-sostenibilidad-y-gobernanza-orbital/CLASE.md).

### Dirichlet

- Las condiciones pueden ser de Dirichlet (valor de la función), Neumann (valor de la derivada) o mixtas.

💡 **Contexto en la clase [B11-C12](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md):**
- **Idea central (modelo mental):** El problema de valor inicial es disparar y mirar dónde cae. El de frontera es acertar a un blanco fijo: se dispara, se mide la desviación y se corrige el ángulo. El método de diferencias finitas es distinto: se pide a todos los puntos de la malla que se acomoden a la vez entre las dos paredes.
- 🎯 **Por qué importa:** En ingeniería espacial las condiciones suelen estar en dos extremos: una aleta térmica con temperaturas conocidas en la raíz y en la punta; una transferencia que debe partir de un punto y llegar a otro en un tiempo dado.
- 🔗 **Se estudia junto con:** problema de frontera, Neumann, mixtas, malla.

📘 **Dónde se aprende** (1 clase): [B11-C12 · Problemas de frontera](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md).

### Discernibilidad (DM)

- La discernibilidad (DM) mide la pérdida de información.

💡 **Contexto en la clase [B124-C13](../programa/clases/B124/B124-C13-etica-de-investigacion-y-datos/CLASE.md):**
- 🎯 **Por qué importa:** Abrir datos sin proteger a las personas es un daño, y proteger sin medir es una promesa vacía. La decisión central: ¿cuánto generalizar los datos para que ninguna persona sea identificable y cuánta información se pierde?
- 🔗 **Se estudia junto con:** k-anonimato, generalización, supresión, reticulado.

📘 **Dónde se aprende** (1 clase): [B124-C13 · Ética de investigación y datos](../programa/clases/B124/B124-C13-etica-de-investigacion-y-datos/CLASE.md).

### Disco

- El disco es el conjunto aplanado de estrellas y gas en rotación, dividido en disco delgado y grueso según la altura y la edad.

💡 **Cómo se explica en la clase [B25-C01](../programa/clases/B25/B25-C01-estructura-de-la-via-lactea/CLASE.md):**
- Es una estimación de orden de magnitud: el disco no es esférico, así que la masa real dentro de `R₀` difiere algo.
- El disco delgado contiene las estrellas jóvenes y el gas; el grueso, estrellas más viejas y a mayor altura (escala de longitud `2,0 ± 0,2 kpc` y masa `6 ± 3 × 10⁹ M☉`, S3); el halo estelar, las más viejas y pobres en metales (C17).
- ⚠️ **Error frecuente:** Pensar que la galaxia es un disco rígido. Se corrige con el ejercicio 11 (periodos) y con C08.
- 🎯 **Por qué importa:** Estamos dentro de la galaxia y no podemos fotografiarla desde fuera: su forma se reconstruye midiendo distancias y velocidades desde un punto que no es el centro. Sin un esquema claro de componentes (bulbo, barra, disco, halo) y de cifras de referencia, el resto del bloque carece de escala.
- 🔗 **Se estudia junto con:** Vía Láctea, bulbo, barra, delgado.

📘 **Dónde se aprende** (1 clase): [B25-C01 · Estructura de la Vía Láctea](../programa/clases/B25/B25-C01-estructura-de-la-via-lactea/CLASE.md).

### Disco de Airy

- El disco de Airy es la imagen de una fuente puntual de una apertura circular, con FWHM `1,029 λ/D`.
- El disco de Airy es la imagen de un punto limitada por difracción.

💡 **Cómo se explica en la clase [B42-C05](../programa/clases/B42/B42-C05-patrones-de-airy/CLASE.md):**
- Como una piedra en un estanque circular: un pico central y anillos que se apagan; el disco de Airy es el primer anillo oscuro.
- Con `D = 8 m` y `λ = 2,2 µm` (ilustrativos) `λ/D = 0,05672 arcsec`; el primer cero está en `1,2197 λ/D`, el FWHM en `1,0290 λ/D` y el disco de Airy encierra el `83,78 %`.
- 🎯 **Por qué importa:** El patrón de Airy es el límite de resolución de cualquier telescopio sin atmósfera. La decisión central: ¿cuánto vale la resolución de una apertura circular y qué fracción de la luz queda en el disco central?
- 🔗 **Se estudia junto con:** patrón de Airy, función de Bessel, criterio de Rayleigh, FWHM.

📘 **Dónde se aprende** (4 clases): [B41-C12 · Difracción y límite de Rayleigh](../programa/clases/B41/B41-C12-difraccion-y-limite-de-rayleigh/CLASE.md); [B42-C05 · Patrones de Airy](../programa/clases/B42/B42-C05-patrones-de-airy/CLASE.md); [B44-C17 · Escala de imagen y muestreo](../programa/clases/B44/B44-C17-escala-de-imagen-y-muestreo/CLASE.md); [B121-C02 · Licenciamiento de actividades de teledetección](../programa/clases/B121/B121-C02-licenciamiento-de-actividades-de-teledeteccion/CLASE.md).

### Disco de Miyamoto–Nagai

- El disco de Miyamoto–Nagai `Φ = −GM/√(R² + (a + √(z² + b²))²)`.

💡 **Contexto en la clase [B38-C05](../programa/clases/B38/B38-C05-potenciales-galacticos-plummer-miyamoto-nagai-y-nfw/CLASE.md):**
- **Idea central (modelo mental):** Como un paisaje con tres relieves superpuestos: lo que siente una estrella es la pendiente total, la suma de las pendientes de cada relieve.
- 🎯 **Por qué importa:** Toda simulación de estrellas necesita una fuerza. La decisión central: ¿qué potencial simple reproduce una curva de rotación plana y cuánto aporta cada componente?
- 🔗 **Se estudia junto con:** potencial, velocidad circular, bulbo de Plummer, halo NFW.

📘 **Dónde se aprende** (1 clase): [B38-C05 · Potenciales galácticos: Plummer, Miyamoto-Nagai y NFW](../programa/clases/B38/B38-C05-potenciales-galacticos-plummer-miyamoto-nagai-y-nfw/CLASE.md).

### Disco delgado

- El disco delgado es geométricamente delgado y estacionario.

💡 **Cómo se explica en la clase [B27-C10](../programa/clases/B27/B27-C10-discos-de-acrecion/CLASE.md):**
- Que la cuadratura es correcta; no que el disco real sea delgado ni estacionario.
- 🎯 **Por qué importa:** Un disco convierte hasta una fracción grande de `Ṁc²` en luz; su temperatura, que baja hacia fuera, decide en qué banda se ve (rayos X en un agujero estelar, ultravioleta en uno supermasivo). La decisión central: ¿cuánto vale la temperatura en cada radio y qué luminosidad produce una tasa de acreción dada?
- 🔗 **Se estudia junto con:** borde interno, temperatura efectiva, luminosidad de Eddington, tasa de acreción.

📘 **Dónde se aprende** (1 clase): [B27-C10 · Discos de acreción](../programa/clases/B27/B27-C10-discos-de-acrecion/CLASE.md).

### Disco exponencial delgado

- Un disco exponencial delgado tiene `Σ(R) = Σ₀e^{−R/R_d}`.

💡 **Cómo se explica en la clase [B25-C08](../programa/clases/B25/B25-C08-curvas-de-rotacion-de-galaxias/CLASE.md):**
- La fórmula de Freeman para un disco exponencial delgado es `v² = 4πGΣ₀R_d y² [I₀(y)K₀(y) − I₁(y)K₁(y)]`, con `y = R/(2R_d)`.
- 🎯 **Por qué importa:** Si la masa estuviera donde brilla, la velocidad de rotación debería caer en las afueras de una galaxia, como la de los planetas lejanos del Sol. Que una curva de rotación se mantenga plana indica más masa de la que se ve.
- 🔗 **Se estudia junto con:** curva de rotación, velocidad circular, funciones de Bessel modificadas, halo pseudo-isotermo.

📘 **Dónde se aprende** (1 clase): [B25-C08 · Curvas de rotación de galaxias](../programa/clases/B25/B25-C08-curvas-de-rotacion-de-galaxias/CLASE.md).

### Disco pequeño

- El disco pequeño es la aproximación en la que la gaussiana es casi constante en el disco.

💡 **Cómo se explica en la clase [B118-C06](../programa/clases/B118/B118-C06-probabilidad-de-colision/CLASE.md):**
- Caso A (miss 200 m, `σ` 150 × 100 m, `R` 10 m): cuadratura `1,3693 × 10⁻³`; disco pequeño `1,3704 × 10⁻³`; relación `0,9992`.
- A --> C["Disco pequeño<br/>R²/(2σxσy) e^(-miss²/2σx²)"]
- ⚠️ **Error frecuente:** Aplicar el disco pequeño cuando `R` no es pequeño frente a `σ`. Se corrige con la comparación de 8.2.
- 🎯 **Por qué importa:** Las alertas se priorizan por `Pc`, pero ese número depende de la covarianza que se suponga. La decisión central: ¿cuándo es fiable una `Pc` y cuándo es baja solo porque la incertidumbre es enorme?
- 🔗 **Se estudia junto con:** probabilidad de colisión, radio combinado, covarianza, dilución.

📘 **Dónde se aprende** (1 clase): [B118-C06 · Probabilidad de colisión](../programa/clases/B118/B118-C06-probabilidad-de-colision/CLASE.md).

### Discontinuidad

- Si falla, hay una discontinuidad: removible (el límite existe pero no coincide con `f(a)` o `f(a)` no existe), de salto (existen ambos límites laterales y son distintos) o infinita (la función crece sin cota).

💡 **Cómo se explica en la clase [B09-C02](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md):**
- Aplicar el TVI a un intervalo con discontinuidad produce conclusiones falsas.
- Cada tipo de discontinuidad es una razón para levantarlo: un hueco (removible), un salto de nivel (salto) o una subida al infinito (infinita).
- 🎯 **Por qué importa:** Un vehículo espacial cambia de masa de dos maneras: gradualmente, al quemar propelente, y de golpe, al soltar una etapa vacía. Un modelo de trayectoria que ignore los saltos integra mal; uno que los trate como suaves, también.
- 🔗 **Se estudia junto con:** continua en a, removible, de salto, infinita.

📘 **Dónde se aprende** (1 clase): [B09-C02 · Continuidad y discontinuidad](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md).

### Discontinuidad de contacto

- Una onda de choque es una discontinuidad que se propaga con compresión irreversible; una onda de rarefacción es una expansión continua; la discontinuidad de contacto separa dos gases con distinta densidad pero igual presión y velocidad.
- La onda de rarefacción, la discontinuidad de contacto y el choque son las tres ondas del tubo de Sod.

💡 **Cómo se explica en la clase [B21-C01](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md):**
- HLL supone una sola región intermedia entre las ondas extremas, por lo que ignora la discontinuidad de contacto y la difunde (S1 lo señala; para MHD ignora además las ondas de Alfvén y las lentas).
- 🎯 **Por qué importa:** Casi todo lo que fluye en el espacio —el viento solar, el gas de un disco de acreción, el gas que rodea a una nave en reentrada, la onda de choque de una eyección coronal— obedece leyes de conservación: una cantidad cambia en una región solo porque entra o sale por sus bordes.
- 🔗 **Se estudia junto con:** ley de conservación, vector de estado conservado, flujo, celda.

📘 **Dónde se aprende** (2 clases): [B21-C01 · Volúmenes finitos y solucionadores de Riemann para leyes de conservación](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md); [B38-C06 · Hidrodinámica en simulaciones: SPH y métodos de malla](../programa/clases/B38/B38-C06-hidrodinamica-en-simulaciones-sph-y-metodos-de-malla/CLASE.md).

### Discrepancia

- Realidad sintética: el «sistema» simulado con errores inventados. Discrepancia: diferencia entre el modelo y la realidad.

💡 **Cómo se explica en la clase [B101-C08](../programa/clases/B101/B101-C08-gemelo-digital-para-ensayo-de-reparaciones-roboticas/CLASE.md):**
- Límite: aquí la discrepancia es solo cinemática; en un caso real hay muchas otras.
- Distinguir el modelo (gemelo) de la realidad y medir su discrepancia.
- 🎯 **Por qué importa:** Una reparación robótica no se improvisa: se ensaya. Pero un ensayo vale solo si el gemelo se parece a la realidad.
- 🔗 **Se estudia junto con:** Gemelo digital, Realidad sintética, Recalibración, Éxito de la maniobra.

📘 **Dónde se aprende** (1 clase): [B101-C08 · Gemelo digital para ensayo de reparaciones robóticas](../programa/clases/B101/B101-C08-gemelo-digital-para-ensayo-de-reparaciones-roboticas/CLASE.md).

### Discrepancia de modelo

- La discrepancia de modelo es la diferencia entre ambos, y en una prueba honesta existe.

💡 **Cómo se explica en la clase [B22-C05](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md):**
- Paso 1 · declaración. Verdad: perfil con dos escalones; datos: 30 puntos; modelo del instrumento: gaussiana `w = 0,05`; generador honesto: 1000 celdas; inversor: 30 celdas; método: Tikhonov, `λ` por discrepancia; semilla 5.
- Paso 3 · el suelo. Al subir el ruido a `10⁻²`, el error con crimen sube a `0,19`, casi igual que el honesto (`0,226`): con mucho ruido, la discrepancia de modelo pasa a ser secundaria.
- 🎯 **Por qué importa:** Con datos reales no conoces la verdad, así que no puedes medir el error de tu inversión. Con datos sintéticos sí: tú fijas la verdad, generas los datos y miras si el método la recupera.
- 🔗 **Se estudia junto con:** prueba sintética, modelo generador, modelo de inversión, crimen inverso.

📘 **Dónde se aprende** (1 clase): [B22-C05 · Pruebas de inversión con datos sintéticos](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md).

### Discreta

- Es discreta si toma valores aislados y continua si toma cualquier valor de un intervalo (S1, C.2.2, nota 1).

💡 **Cómo se explica en la clase [B12-C02](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md):**
- Paso 1 · Variables. `X` discreta (pmf de 8.1), `Y` continua (8.3); se supone que `X` e `Y` son independientes (el telémetro no depende de los computadores en este modelo).
- Para responder una pregunta con una variable aleatoria hay tres caminos: sumar la pmf (discreta, exacto), integrar la densidad (continua, exacto si hay primitiva) y usar la cdf (ambos; es la más directa para «a lo sumo», «más de» y cuantiles).
- ⚠️ **Error frecuente:** Mezclar `<` y `≤` en discretas. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Casi nunca interesa *qué* resultado ocurrió, sino *un número* que resume el resultado: cuántos computadores funcionan, qué error tuvo una medición, cuántos fotones llegaron. Poner un número en cada resultado permite sumar, promediar y comparar.
- 🔗 **Se estudia junto con:** variable aleatoria, continua, función de masa de probabilidad, función de distribución acumulada.

📘 **Dónde se aprende** (1 clase): [B12-C02 · Variables aleatorias](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md).

### Discreto

- Un modelo es lineal si cumple superposición (lo precisa C03), invariante si sus parámetros no cambian con el tiempo, continuo si el tiempo es una variable real `t` y discreto si solo existe en instantes `kT`.

💡 **Cómo se explica en la clase [B16-C01](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md):**
- Un modelo continuo describe el fenómeno; uno discreto describe lo que ve el computador de a bordo, que mide y actúa cada `T` segundos (C02).
- Clasificar un modelo como lineal o no lineal, continuo o discreto, invariante o variante.
- 🎯 **Por qué importa:** Un telescopio espacial tiene que apuntar a una estrella y mantenerse allí. El telescopio Hubble lo hace con una desviación de no más de 0,007 segundos de arco durante al menos 24 horas (fuente S2).
- 🔗 **Se estudia junto con:** sistema, entrada, perturbación, salida.

📘 **Dónde se aprende** (1 clase): [B16-C01 · Modelos dinámicos y estados](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md).

### Discriminación

- La discriminación es la correlación entre acertar el ítem y el puntaje en los demás.
- La discriminación `r` mide si quienes aciertan el ítem puntúan mejor en el resto.

💡 **Cómo se explica en la clase [B130-C05](../programa/clases/B130/B130-C05-evaluacion-de-la-comprension-del-publico/CLASE.md):**
- El ítem 2 discrimina poco (`0,10`): acertarlo casi no distingue a quienes entendieron más; se revisa o se reemplaza.
- El ítem 12 es difícil (`0,28` correctas) pero discrimina bien.
- 🎯 **Por qué importa:** Saber si la divulgación funcionó exige medir la comprensión; ninguna otra clase lo trata. La decisión central: ¿qué número resume la mejora del público, y cuánto se puede confiar en que no sea azar?
- 🔗 **Se estudia junto con:** ganancia normalizada de un grupo, dificultad, KR-20, alfa de Cronbach.

📘 **Dónde se aprende** (2 clases): [B130-C05 · Evaluación de la comprensión del público](../programa/clases/B130/B130-C05-evaluacion-de-la-comprension-del-publico/CLASE.md); [B131-C08 · Evaluación formativa en el aula de astronomía](../programa/clases/B131/B131-C08-evaluacion-formativa-en-el-aula-de-astronomia/CLASE.md).

### Discriminante

- El discriminante es `Δ = b² − 4ac`.
- El hessiano es la matriz de segundas derivadas; su discriminante es `D = f_xx f_yy − f_xy²`.

💡 **Cómo se explica en la clase [B04-C02](../programa/clases/B04/B04-C02-ecuaciones-lineales-y-cuadraticas/CLASE.md):**
- El discriminante decide: `Δ > 0` da dos raíces reales distintas;
- *Descripción textual:* diagrama de decisión: plantear la incógnita con su unidad, escribir la ecuación, separar según el grado (despejar o factorizar/fórmula con el discriminante), comprobar por sustitución y unidades, y elegir la raíz con sentido físico.
- 🎯 **Por qué importa:** Una sonda desciende hacia la Luna; un instrumento cae desde una mesa de trabajo; una señal de radio viaja hasta un espejo y vuelve. En cada caso hay un número que no conoces (un tiempo, una distancia) y una relación que lo liga a otros que sí conoces.
- 🔗 **Se estudia junto con:** ecuación, resolverla, lineal, cuadrática.

📘 **Dónde se aprende** (2 clases): [B04-C02 · Ecuaciones lineales y cuadráticas](../programa/clases/B04/B04-C02-ecuaciones-lineales-y-cuadraticas/CLASE.md); [B09-C16 · Derivadas parciales](../programa/clases/B09/B09-C16-derivadas-parciales/CLASE.md).

### Diseño conceptual

- Un diseño conceptual fija magnitudes y balances, no planos.

💡 **Cómo se explica en la clase [B59-C20](../programa/clases/B59/B59-C20-diseno-conceptual-de-planta-isru/CLASE.md):**
- python programa/clases/B59/B59-C20-diseno-conceptual-de-planta-isru/planta.py
- ⚠️ **Error frecuente:** Presentar el diseño como el de una planta real. Es conceptual e ilustrativo.
- 🎯 **Por qué importa:** Un diseño conceptual no es un número sino un conjunto coherente. La decisión central: ¿qué potencia y qué masa necesita una planta que produce 10 t de agua al año, y qué parámetro la gobierna?
- 🔗 **Se estudia junto con:** libro de energía, potencia de diseño, masa específica, sensibilidad.

📘 **Dónde se aprende** (1 clase): [B59-C20 · Diseño conceptual de planta ISRU](../programa/clases/B59/B59-C20-diseno-conceptual-de-planta-isru/CLASE.md).

### Diseño de experimentos

- El diseño de experimentos elige los puntos de entrada donde se ejecuta el simulador.

💡 **Contexto en la clase [B17-C04](../programa/clases/B17/B17-C04-modelos-sustitutos-surrogates/CLASE.md):**
- 🎯 **Por qué importa:** Un simulador de trayectoria, de aerodinámica o de transporte de radiación puede tardar minutos u horas por ejecución. Para explorar miles de combinaciones de parámetros (un análisis de sensibilidad, una propagación de incertidumbre, una optimización) no alcanza el tiempo.
- 🔗 **Se estudia junto con:** simulador, modelo sustituto, secuencia de Sobol, proceso gaussiano.

📘 **Dónde se aprende** (1 clase): [B17-C04 · Modelos sustitutos (surrogates)](../programa/clases/B17/B17-C04-modelos-sustitutos-surrogates/CLASE.md).

### Diseño equilibrado

- Un diseño equilibrado tiene el mismo número de medidas por grupo.

💡 **Cómo se explica en la clase [B13-C14](../programa/clases/B13/B13-C14-repetibilidad-y-reproducibilidad/CLASE.md):**
- Realizar un análisis de varianza de un factor con diseño equilibrado.
- Límites: diseño equilibrado, normalidad e independencia; estaciones como efecto aleatorio; pocos grupos dan estimaciones inestables.
- 🎯 **Por qué importa:** Ocho estaciones de seguimiento miden el mismo desfase de un reloj de referencia. Cada una repite su medida cinco veces y obtiene resultados muy parecidos entre sí, pero las estaciones discrepan entre ellas.
- 🔗 **Se estudia junto con:** condición de repetibilidad, condición de precisión intermedia, condición de reproducibilidad, desviación de repetibilidad s_r.

📘 **Dónde se aprende** (1 clase): [B13-C14 · Repetibilidad y reproducibilidad](../programa/clases/B13/B13-C14-repetibilidad-y-reproducibilidad/CLASE.md).

### Diseño inclusivo

- El diseño inclusivo busca que un producto o espacio sirva a la mayor diversidad posible de usuarios.

💡 **Cómo se explica en la clase [B109-C08](../programa/clases/B109/B109-C08-diseno-inclusivo-en-habitats/CLASE.md):**
- python programa/clases/B109/B109-C08-diseno-inclusivo-en-habitats/inclusivo.py
- 🎯 **Por qué importa:** Un control puesto «a la altura normal» deja fuera a quien no la alcanza. La decisión central: ¿a qué altura (o con qué ajuste) un puesto sirve al mayor número de usuarios y a quién deja fuera?
- 🔗 **Se estudia junto con:** cobertura, prevalencia, banda de cobertura, usuario de pie.

📘 **Dónde se aprende** (1 clase): [B109-C08 · Diseño inclusivo en hábitats](../programa/clases/B109/B109-C08-diseno-inclusivo-en-habitats/CLASE.md).

### Diseño longitudinal

- Un diseño longitudinal mide las mismas unidades repetidamente.

💡 **Cómo se explica en la clase [B12-C25](../programa/clases/B12/B12-C25-modelos-longitudinales-y-de-efectos-mixtos-para-muestras-pequenas/CLASE.md):**
- Aquí ignorar el agrupamiento desperdicia potencia: el diseño longitudinal es mucho más sensible al cambio en el tiempo que al nivel medio.
- 🎯 **Por qué importa:** Seis personas medidas cuatro veces dan 24 números, pero no 24 piezas de información independientes: las de una misma persona se parecen. Ignorar eso produce intervalos demasiado angostos para el nivel medio y, paradójicamente, demasiado anchos para los cambios dentro de cada persona.
- 🔗 **Se estudia junto con:** modelo de intercepto aleatorio, efectos fijos, efecto aleatorio, varianzas.

📘 **Dónde se aprende** (1 clase): [B12-C25 · Modelos longitudinales y de efectos mixtos para muestras pequeñas](../programa/clases/B12/B12-C25-modelos-longitudinales-y-de-efectos-mixtos-para-muestras-pequenas/CLASE.md).

### Diseño pareado

- El diseño pareado compara a cada persona consigo misma.

💡 **Cómo se explica en la clase [B105-C20](../programa/clases/B105/B105-C20-diseno-de-protocolo-medico-simulado/CLASE.md):**
- Ejercicio 6 · autónomo. ¿Por qué el diseño pareado aumenta la potencia?
- Ejercicio 12 · integrador. Elabora tu *protocolo médico simulado con potencia*: hipótesis, diseño pareado, medida principal, `n`, potencia y efecto mínimo, comparaciones y corrección, salvaguardas éticas (B105-C19) y lista de qué es simulado.
- 🎯 **Por qué importa:** Un estudio con 6 personas solo detecta efectos grandes; sin saberlo, se concluye «no hay efecto» cuando solo no había potencia. La decisión central: ¿qué efecto mínimo puede detectar el protocolo con su `n`, y cuántas comparaciones puede permitirse?
- 🔗 **Se estudia junto con:** tamaño del efecto, potencia, error tipo I, efecto mínimo detectable.

📘 **Dónde se aprende** (1 clase): [B105-C20 · Diseño de protocolo médico simulado](../programa/clases/B105/B105-C20-diseno-de-protocolo-medico-simulado/CLASE.md).

### Diseño preliminar

- Un diseño preliminar fija arquitectura, subsistemas y presupuestos con margen.

💡 **Cómo se explica en la clase [B83-C20](../programa/clases/B83/B83-C20-diseno-preliminar-completo-de-mision/CLASE.md):**
- La evidencia es la diseño preliminar integrado con presupuestos cerrados del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *diseño preliminar integrado*: desglose, energía, propelente, margen de masa y de datos, pendientes y matriz de trazabilidad con los requisitos, con lista de qué es consultado y sintético.
- 🎯 **Por qué importa:** Cada presupuesto aislado puede cerrar y el conjunto no. La decisión central: ¿existe una masa seca que sea coherente con la potencia, las baterías, la estructura y el propelente que ella misma exige, y cabe en el límite?
- 🔗 **Se estudia junto con:** lazo de diseño, iteración de punto fijo, bisección, potencia de reposo.

📘 **Dónde se aprende** (1 clase): [B83-C20 · Diseño preliminar completo de misión](../programa/clases/B83/B83-C20-diseno-preliminar-completo-de-mision/CLASE.md).

### Diseño sin requisito

- Un requisito huérfano no tiene origen; un requisito no verificado no tiene prueba; el diseño sin requisito es *gold plating* o un requisito faltante.

💡 **Cómo se explica en la clase [B83-C05](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md):**
- Se definen nodos (N, R, D, V) y aristas dirigidas: de la necesidad al requisito, del requisito al diseño y del requisito a la verificación.
- *Descripción textual:* cada necesidad se enlaza con requisitos; estos, con diseño y verificación; un cambio en un requisito se propaga a lo que cuelga de él, y los huecos de la cadena son los huérfanos y la cobertura.
- 🎯 **Por qué importa:** Cuando cambia un requisito, ¿qué piezas y qué pruebas hay que revisar? Sin trazabilidad, nadie lo sabe y el cambio rompe algo en silencio.
- 🔗 **Se estudia junto con:** trazabilidad, Aguas arriba, aguas abajo, matriz de trazabilidad.

📘 **Dónde se aprende** (1 clase): [B83-C05 · Trazabilidad de requisitos](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md).

### Diseño universal

- El diseño universal busca que el entorno sirva a la mayoría sin adaptaciones posteriores.

💡 **Contexto en la clase [B128-C01](../programa/clases/B128/B128-C01-accesibilidad-de-la-observacion-nocturna/CLASE.md):**
- 🎯 **Por qué importa:** Un telescopio apuntado a un objeto alto pone el ocular fuera del alcance de quien está sentado o es de menor estatura, y uno apuntado a un objeto bajo lo pone incómodo para quien está de pie. La barrera no está en la persona sino en el montaje.
- 🔗 **Se estudia junto con:** altitud, altura del ocular, holgura.

📘 **Dónde se aprende** (1 clase): [B128-C01 · Accesibilidad de la observación nocturna](../programa/clases/B128/B128-C01-accesibilidad-de-la-observacion-nocturna/CLASE.md).

### Disimilitud de Bray–Curtis

- La disimilitud de Bray–Curtis `1 − 2Σ mín(p, q)/(Σp + Σq)` va de 0 a 1.

💡 **Cómo se explica en la clase [B105-C11](../programa/clases/B105/B105-C11-microbioma-en-ambientes-cerrados/CLASE.md):**
- Una superficie B recibe la fracción `m` de A y el resto de una comunidad propia C: con `m = 0` la disimilitud de Bray–Curtis es 0,645; con `m = 0,75`, 0,161.
- Calcular la disimilitud de Bray–Curtis entre dos comunidades.
- 🎯 **Por qué importa:** Un índice de diversidad depende de la comunidad y de cuántas lecturas se obtuvieron. La decisión central: ¿qué profundidad de muestreo hace fiable un índice y cómo se cuantifica el parecido entre la piel de la tripulación y las superficies?
- 🔗 **Se estudia junto con:** riqueza, índice de Shannon, Simpson, profundidad.

📘 **Dónde se aprende** (1 clase): [B105-C11 · Microbioma en ambientes cerrados](../programa/clases/B105/B105-C11-microbioma-en-ambientes-cerrados/CLASE.md).

### Disipación

- La disipación es el calor generado.
- La disipación es `Ṫ = ω·τ_m < 0` en promedio.

💡 **Cómo se explica en la clase [B86-C12](../programa/clases/B86/B86-C12-eficiencia-y-disipacion/CLASE.md):**
- La evidencia es el presupuesto de disipación con área de radiador del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *presupuesto de disipación con área de radiador*: etapas, calor, ciclo de batería, área, sensibilidad y rótulos.
- 🎯 **Por qué importa:** Una eficiencia de `92 %` parece alta hasta que se multiplica por las demás etapas y se ve el calor que queda. Cada vatio perdido debe radiarse: el calor decide el tamaño del radiador y la potencia del ala.
- 🔗 **Se estudia junto con:** eficiencia de cadena, emisividad, sumidero equivalente, flujo.

📘 **Dónde se aprende** (2 clases): [B86-C12 · Eficiencia y disipación](../programa/clases/B86/B86-C12-eficiencia-y-disipacion/CLASE.md); [B87-C16 · Detumbling después del despliegue](../programa/clases/B87/B87-C16-detumbling-despues-del-despliegue/CLASE.md).

### Disipación del modo

- La disipación del modo es la suma de las unidades.

💡 **Cómo se explica en la clase [B85-C20](../programa/clases/B85/B85-C20-presupuesto-termico-de-carga-util/CLASE.md):**
- U["Unidades por modo"] --> D["Disipación y margen 20 %"]
- *Descripción textual:* la disipación por modo con margen se compara con la capacidad del radiador en el caso caliente; en el frío la capacidad define el calentador; el menor margen indica el modo gobernante.
- 🎯 **Por qué importa:** Un presupuesto sin margen no resiste un cambio de diseño. La decisión central: ¿qué modo gobierna el caso caliente, con cuánto margen cierra y qué calentador pide el frío?
- 🔗 **Se estudia junto con:** margen de desarrollo, capacidad del radiador, margen de potencia, modo gobernante.

📘 **Dónde se aprende** (1 clase): [B85-C20 · Presupuesto térmico de carga útil](../programa/clases/B85/B85-C20-presupuesto-termico-de-carga-util/CLASE.md).

### Disipativo

- Un método es disipativo si reduce la energía y antidisipativo si la aumenta.

💡 **Cómo se explica en la clase [B11-C10](../programa/clases/B11/B11-C10-conservacion-de-energia-numerica/CLASE.md):**
- También lineal en el número de vueltas, y con signo negativo (disipativo): el análisis de C09 lo anticipaba, porque `|R| = 1 − y⁶/144 < 1` sobre el eje imaginario.
- 🎯 **Por qué importa:** Un análisis de misión puede necesitar propagar un satélite durante años, es decir, decenas de miles de vueltas. Si cada vuelta añade o quita un poco de energía, la altura de la órbita cambia solo por culpa del programa.
- 🔗 **Se estudia junto con:** cantidad conservada, deriva, secular, acotada u oscilante.

📘 **Dónde se aprende** (1 clase): [B11-C10 · Conservación de energía numérica](../programa/clases/B11/B11-C10-conservacion-de-energia-numerica/CLASE.md).

### Disociación

- La disociación es la ruptura de moléculas a muy alta temperatura (no modelada).
- La descomposición exotérmica libera calor; la disociación lo absorbe.

💡 **Cómo se explica en la clase [B78-C04](../programa/clases/B78/B78-C04-propulsion-monopropelente-conceptual/CLASE.md):**
- La disociación baja la masa molar, lo que favorecería el escape, pero baja más la temperatura: en este modelo el máximo está en `a = 0`.
- Descripción larga: el escape baja de forma monótona con la disociación, porque la caída de temperatura pesa más que la de la masa molar.
- ⚠️ **Error frecuente:** Olvidar que la disociación es endotérmica. Se corrige con 8.2.
- 🎯 **Por qué importa:** La descomposición de un monopropelente tiene dos pasos: uno que libera calor y otro que lo absorbe. La decisión central: ¿conviene que el amoníaco intermedio se disocie del todo, por la menor masa molar, o que se conserve, por la mayor temperatura?
- 🔗 **Se estudia junto con:** monopropelente, fracción disociada, descomposición exotérmica, temperatura adiabática.

📘 **Dónde se aprende** (2 clases): [B78-C04 · Propulsión monopropelente conceptual](../programa/clases/B78/B78-C04-propulsion-monopropelente-conceptual/CLASE.md); [B79-C14 · Propiedades de gases calientes](../programa/clases/B79/B79-C14-propiedades-de-gases-calientes/CLASE.md).

### Disolución

- Una disolución es una mezcla homogénea de un soluto en un disolvente; en esta clase, el disolvente es el agua.

💡 **Cómo se explica en la clase [B06-C15](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md):**
- Una disolución ácida no puede ser básica por mucho que se diluya.
- Para disoluciones muy diluidas ninguna de las dos basta y hay que añadir la autoprotólisis del agua.
- ⚠️ **Error frecuente:** Ignorar el agua en disoluciones muy diluidas. Se corrige con los ejercicios 7 y 11.
- 🎯 **Por qué importa:** El extracto en agua caliente de las muestras de Bennu contiene amoníaco libre en unos 13,6 μmol por gramo y ácido fórmico en 4,106 μmol por gramo (S1). Un ácido y una base en el mismo líquido reaccionan entre sí: el ácido cede un protón, la base lo acepta y se forman iones.
- 🔗 **Se estudia junto con:** soluto, disolvente, concentración, molaridad.

📘 **Dónde se aprende** (1 clase): [B06-C15 · Ácidos, bases y soluciones](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md).

### Disolvente

- Una disolución es una mezcla homogénea de un soluto en un disolvente; en esta clase, el disolvente es el agua.

💡 **Contexto en la clase [B06-C15](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md):**
- **Idea central (modelo mental):** Un ácido es quien presta un protón y una base, quien lo recibe. El préstamo no es todo o nada: en un ácido fuerte casi todos los protones se prestan; en uno débil, sólo una fracción, y el equilibrio fija cuántos.
- 🎯 **Por qué importa:** El extracto en agua caliente de las muestras de Bennu contiene amoníaco libre en unos 13,6 μmol por gramo y ácido fórmico en 4,106 μmol por gramo (S1). Un ácido y una base en el mismo líquido reaccionan entre sí: el ácido cede un protón, la base lo acepta y se forman iones.
- 🔗 **Se estudia junto con:** disolución, soluto, concentración, molaridad.

📘 **Dónde se aprende** (1 clase): [B06-C15 · Ácidos, bases y soluciones](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md).

### Disparidad

- La disparidad `d` es la diferencia de posición del punto en las dos imágenes, en píxeles.
- La disparidad `d` es el desplazamiento horizontal de un punto entre las dos imágenes.

💡 **Cómo se explica en la clase [B97-C04](../programa/clases/B97/B97-C04-vision-estereoscopica/CLASE.md):**
- Con `200 000` muestras de disparidad ruidosa (semilla fija), la desviación de `Z` es `0,05944` m frente a `0,05952` m teóricos (diferencia relativa `1,37e-03`).
- *Descripción textual:* de la disparidad y la geometría sale la profundidad; el ruido de disparidad produce un error que crece con `Z²`, y eso define el alcance útil.
- ⚠️ **Error frecuente:** Confundir disparidad con profundidad. Son inversas (8.1)
- 🎯 **Por qué importa:** Un rover decide si un obstáculo está a 3 m o a 8 m con estas cámaras. Sin saber cómo crece el error con la distancia, se confía en una profundidad de 30 m que puede tener varios metros de incertidumbre.
- 🔗 **Se estudia junto con:** base, profundidad, propagación de errores.

📘 **Dónde se aprende** (2 clases): [B97-C04 · Visión estereoscópica](../programa/clases/B97/B97-C04-vision-estereoscopica/CLASE.md); [B103-C03 · Mapas de profundidad y correspondencia estéreo](../programa/clases/B103/B103-C03-mapas-de-profundidad-y-correspondencia-estereo/CLASE.md).

### Disparo

- El disparo integra desde el centro y ajusta `ω²` para cumplir la frontera.

💡 **Cómo se explica en la clase [B37-C07](../programa/clases/B37/B37-C07-oscilaciones-radiales-y-relacion-periodo-densidad-media/CLASE.md):**
- Todas las cotas variacionales están por encima del valor del disparo y convergen a él.
- E["Sturm-Liouville radial"] --> D["disparo: w(R)=0"]
- 🎯 **Por qué importa:** El período fundamental fija la densidad media. La decisión central: ¿cuánto vale el período de un modo radial y cómo escala con la densidad?
- 🔗 **Se estudia junto con:** modo radial, índice adiabático, cociente de Rayleigh, relación período–densidad.

📘 **Dónde se aprende** (1 clase): [B37-C07 · Oscilaciones radiales y relación período-densidad media](../programa/clases/B37/B37-C07-oscilaciones-radiales-y-relacion-periodo-densidad-media/CLASE.md).

### Disparo múltiple

- El disparo múltiple divide el tiempo en `m` tramos: las incógnitas son `v₀` y los estados de los nodos, y las ecuaciones son los defectos de continuidad (fin de un tramo menos inicio del siguiente) más la condición final.

💡 **Cómo se explica en la clase [B81-C02](../programa/clases/B81/B81-C02-metodo-de-disparo-para-control-optimo/CLASE.md):**
- *Descripción textual:* el disparo simple repite integrar, medir el error final y corregir `v₀` con Newton; el múltiple hace lo mismo sobre `v₀` y los nodos con defectos de continuidad.
- Límite: el disparo múltiple necesita estimar los nodos; con malas semillas también puede fallar.
- 🎯 **Por qué importa:** El disparo simple falla cuando la trayectoria es muy sensible a la velocidad inicial; el múltiple reparte el problema en tramos. La decisión central: ¿cuándo basta un solo disparo y cuándo hay que dividir la trayectoria?
- 🔗 **Se estudia junto con:** disparo simple, defectos de continuidad, número de condición.

📘 **Dónde se aprende** (1 clase): [B81-C02 · Método de disparo para control óptimo](../programa/clases/B81/B81-C02-metodo-de-disparo-para-control-optimo/CLASE.md).

### Disparo simple

- El disparo simple integra desde `v₀` y corrige con Newton usando `∂r_f/∂v₀ = Φ_rv`.

💡 **Cómo se explica en la clase [B81-C02](../programa/clases/B81/B81-C02-metodo-de-disparo-para-control-optimo/CLASE.md):**
- *Descripción textual:* el disparo simple repite integrar, medir el error final y corregir `v₀` con Newton; el múltiple hace lo mismo sobre `v₀` y los nodos con defectos de continuidad.
- Con 120 d el disparo simple converge en 4 iteraciones; con 250 d en 9; con 500 d no converge en 40.
- 🎯 **Por qué importa:** El disparo simple falla cuando la trayectoria es muy sensible a la velocidad inicial; el múltiple reparte el problema en tramos. La decisión central: ¿cuándo basta un solo disparo y cuándo hay que dividir la trayectoria?
- 🔗 **Se estudia junto con:** disparo múltiple, defectos de continuidad, número de condición.

📘 **Dónde se aprende** (1 clase): [B81-C02 · Método de disparo para control óptimo](../programa/clases/B81/B81-C02-metodo-de-disparo-para-control-optimo/CLASE.md).

### Dispensador

- El dispensador es el contenedor que expulsa al CubeSat.

💡 **Cómo se explica en la clase [B95-C01](../programa/clases/B95/B95-C01-unidad-cubesat-dimensiones-y-formatos/CLASE.md):**
- Las masas son valores típicos máximos: masas mayores pueden evaluarse caso por caso y el dispensador puede admitir menos.
- Límite: el CDS fija valores típicos y un dispensador concreto o el proveedor de lanzamiento pueden exigir menos o evaluar más caso por caso.
- 🎯 **Por qué importa:** Un CubeSat que no cumple el estándar no entra en el dispensador, aunque funcione perfectamente. La decisión central: ¿esta configuración cabe, pesa y se equilibra dentro de lo que el estándar permite, y cuándo puede encenderse, desplegar y transmitir?
- 🔗 **Se estudia junto con:** unidad U, centro de gravedad, interruptor de despliegue, inhibidor.

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
- 🔗 **Se estudia junto con:** medida de dispersión, desdispersión, ensanchamiento intra-canal, resolución en DM.

📘 **Dónde se aprende** (5 clases): [B26-C11 · Expansión cósmica y ley de Hubble-Lemaître](../programa/clases/B26/B26-C11-expansion-cosmica-y-ley-de-hubble-lemaitre/CLASE.md); [B29-C17 · Fenómenos transitorios rápidos](../programa/clases/B29/B29-C17-fenomenos-transitorios-rapidos/CLASE.md); [B41-C14 · Aberración cromática y astigmatismo](../programa/clases/B41/B41-C14-aberracion-cromatica-y-astigmatismo/CLASE.md); [B46-C02 · Propagación de ondas de radio](../programa/clases/B46/B46-C02-propagacion-de-ondas-de-radio/CLASE.md); [B118-C13 · Desorbitación controlada](../programa/clases/B118/B118-C13-desorbitacion-controlada/CLASE.md).

### Dispersión angular

- La dispersión angular `dβ/dλ = m/(d cos β)`.
- La dispersión angular `dD/dλ`.

💡 **Cómo se explica en la clase [B45-C04](../programa/clases/B45/B45-C04-redes-de-difraccion/CLASE.md):**
- Calcular la dispersión angular `m/(d cos β)`.
- dispersion angular numerica 6.068661e+05 rad/m ; analitica 6.068661e+05 rad/m (0.6069 mrad/nm)
- 🎯 **Por qué importa:** La red es el elemento dispersor de casi todos los espectrógrafos. La decisión central: ¿en qué ángulo sale cada longitud de onda y qué resolución se obtiene?
- 🔗 **Se estudia junto con:** ecuación de la red, orden, poder de resolución, Littrow.

📘 **Dónde se aprende** (2 clases): [B45-C04 · Redes de difracción](../programa/clases/B45/B45-C04-redes-de-difraccion/CLASE.md); [B45-C05 · Prismas y dispersión](../programa/clases/B45/B45-C05-prismas-y-dispersion/CLASE.md).

### Dispersión Compton

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C06](../programa/clases/B47/B47-C06-instrumentos-de-rayos-gamma/CLASE.md):**
- Muestrear la dispersión Compton por rechazo (semilla fija).
- 🎯 **Por qué importa:** Cada proceso (Compton, pares) domina a una energía distinta y fija el tipo de instrumento. La decisión central: ¿qué proceso usa el detector y con qué incertidumbre angular reconstruye la dirección?
- 🔗 **Se estudia junto con:** sección eficaz de Klein-Nishina, sección eficaz de Thomson, producción de pares, telescopio Compton.

📘 **Dónde se aprende** (1 clase): [B47-C06 · Instrumentos de rayos gamma](../programa/clases/B47/B47-C06-instrumentos-de-rayos-gamma/CLASE.md).

### Dispersión Compton inversa

- La dispersión Compton inversa transfiere energía de un electrón a un fotón.

💡 **Cómo se explica en la clase [B27-C21](../programa/clases/B27/B27-C21-dispersion-compton-inversa-y-emision-de-alta-energia/CLASE.md):**
- La evidencia es la ficha de dispersión Compton inversa del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *ficha de dispersión Compton inversa*: energías exacta y aproximada para tres `γ`, parámetro de KN, `σ_KN/σ_T` para cinco `x` y `P_IC/P_sync`.
- 🎯 **Por qué importa:** Los fotones de TeV que se detectan en algunos objetos proceden de este mecanismo, y la comparación entre la potencia Compton y la sincrotrón permite estimar el campo magnético. La decisión central: ¿qué energía alcanza el fotón dispersado, cuándo deja de valer la aproximación de Thomson y qué razón de potencias se espera?
- 🔗 **Se estudia junto con:** régimen de Thomson, régimen de Klein–Nishina, sección eficaz de Klein–Nishina, cociente.

📘 **Dónde se aprende** (1 clase): [B27-C21 · Dispersión Compton inversa y emisión de alta energía](../programa/clases/B27/B27-C21-dispersion-compton-inversa-y-emision-de-alta-energia/CLASE.md).

### Dispersión de aterrizaje

- La dispersión de aterrizaje es el área donde puede caer la cápsula.

💡 **Cómo se explica en la clase [B104-C14](../programa/clases/B104/B104-C14-supervivencia-en-entorno-terrestre/CLASE.md):**
- *Descripción textual:* la dispersión de aterrizaje da la distancia al equipo de rescate; el tiempo total suma alistamiento, localización (muy distinta con y sin baliza) y traslado; se compara con la autonomía.
- Con un aterrizaje balístico (corto 300 km y dispersión de 120 × 30 km) y baliza la mediana es 3,20 h; sin baliza, 8,72 h y 29,4 % de superar las 12 h.
- 🎯 **Por qué importa:** Si el rescate no llega antes de que se agoten el refugio y las provisiones, la situación se vuelve crítica. La decisión central: ¿cuánto reducen la baliza y la ubicación del rescate la probabilidad de una espera mayor que la autonomía?
- 🔗 **Se estudia junto con:** aterrizaje balístico, baliza, autonomía, tiempo de rescate.

📘 **Dónde se aprende** (1 clase): [B104-C14 · Supervivencia en entorno terrestre](../programa/clases/B104/B104-C14-supervivencia-en-entorno-terrestre/CLASE.md).

### Dispersión de energía

- La dispersión de energía `ΔE = GMR_*/r_t²`.

💡 **Cómo se explica en la clase [B27-C16](../programa/clases/B27/B27-C16-eventos-de-disrupcion-por-marea/CLASE.md):**
- *Descripción textual:* de la estrella y la masa del agujero se obtienen el radio de marea y la dispersión de energía; de ahí salen el tiempo mínimo y la ley de caída; igualar `r_t` con el radio de Schwarzschild da la masa de Hills.
- Calcular la dispersión de energía y el tiempo mínimo de retorno.
- 🎯 **Por qué importa:** Estos eventos iluminan agujeros negros inactivos y permiten estimar su masa. Gezari revisa 56 de ellos (S3, resumen).
- 🔗 **Se estudia junto con:** radio de marea, masa de Hills, tiempo mínimo de retorno, tasa de retorno.

📘 **Dónde se aprende** (1 clase): [B27-C16 · Eventos de disrupción por marea](../programa/clases/B27/B27-C16-eventos-de-disrupcion-por-marea/CLASE.md).

### Dispersión de energía inicial

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B47-C08](../programa/clases/B47/B47-C08-espectrometros-de-masas-orbitales/CLASE.md):**
- **Idea central (modelo mental):** Es una carrera en que todos reciben el mismo empujón: los livianos llegan primero. Si la salida es desordenada, dos corredores casi iguales llegan juntos.
- 🎯 **Por qué importa:** La resolución de masa decide qué especies se separan. La decisión central: ¿qué tiempo de vuelo, qué dispersión y qué resolución permiten distinguir dos iones casi isobáricos?
- 🔗 **Se estudia junto con:** tiempo de vuelo, resolución de masa, anchura del pulso, iones isobáricos.

📘 **Dónde se aprende** (1 clase): [B47-C08 · Espectrómetros de masas orbitales](../programa/clases/B47/B47-C08-espectrometros-de-masas-orbitales/CLASE.md).

### Dispersión de fase

- La dispersión de fase (PDM) mide cuánto varía el brillo dentro de cada bin de fase.

💡 **Cómo se explica en la clase [B29-C14](../programa/clases/B29/B29-C14-estrellas-variables-periodicas/CLASE.md):**
- La dispersión de fase en el periodo verdadero es `θ = 0,0503` y en un periodo erróneo (1,37 veces) `0,8831`: valores bajos indican fase limpia.
- *Descripción textual:* se ajusta una curva armónica para cada frecuencia y se toma el mínimo de `χ²`; la dispersión de fase da un estimador independiente; ambos coinciden y la incertidumbre de una sinusoide sigue una fórmula estándar.
- 🎯 **Por qué importa:** El periodo es la propiedad básica de una variable periódica; de él y de la forma de la curva se deducen la masa, la edad o la distancia en muchos casos. La decisión central: ¿qué periodo y qué incertidumbre da la serie y qué métodos coinciden?
- 🔗 **Se estudia junto con:** armónico, curva de fase, rejilla de frecuencias, amplitud.

📘 **Dónde se aprende** (1 clase): [B29-C14 · Estrellas variables periódicas](../programa/clases/B29/B29-C14-estrellas-variables-periodicas/CLASE.md).

### Dispersión de Thomson

- La dispersión de Thomson es la dispersión de la luz por electrones libres, con sección eficaz `σ_T`.

💡 **Contexto en la clase [B24-C09](../programa/clases/B24/B24-C09-atmosferas-y-opacidades/CLASE.md):**
- **Idea central (modelo mental):** Mirar una estrella es mirar una niebla: solo ves hasta donde la niebla se vuelve transparente. Más adentro, más caliente; más afuera, más frío.
- 🎯 **Por qué importa:** Toda temperatura o composición que atribuimos a una estrella se infiere de una capa delgada. Saber de qué profundidad viene la luz, cuánto vale la opacidad y cuánto puede brillar una estrella sin expulsar su atmósfera es lo que permite interpretar espectros (C10) y entender los vientos (C17).
- 🔗 **Se estudia junto con:** opacidad, profundidad óptica, atmósfera gris, fotosfera.

📘 **Dónde se aprende** (1 clase): [B24-C09 · Atmósferas y opacidades](../programa/clases/B24/B24-C09-atmosferas-y-opacidades/CLASE.md).

### Dispersión de velocidades

- La dispersión de velocidades `σ` mide la agitación de las estrellas.
- La dispersión de velocidades `σ_R` y `σ_φ` mide la agitación radial y azimutal.

💡 **Cómo se explica en la clase [B25-C06](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md):**
- Harris (S1) cataloga `157` objetos clasificados como cúmulos globulares de la Vía Láctea, con coordenadas, metalicidades, parámetros estructurales y dispersión central de velocidades.
- Calcular la dispersión de velocidades y la velocidad de escape.
- 🎯 **Por qué importa:** La mayoría de las estrellas nace en grupos. Los cúmulos son laboratorios: sus estrellas comparten edad, distancia y composición.
- 🔗 **Se estudia junto con:** cúmulo abierto, cúmulo globular, cúmulo masivo joven, perfil de Plummer.

📘 **Dónde se aprende** (2 clases): [B25-C06 · Cúmulos estelares](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md); [B25-C07 · Dinámica de poblaciones estelares](../programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/CLASE.md).

### Dispersión del plasma

- La dispersión del plasma retrasa más las frecuencias bajas.

💡 **Cómo se explica en la clase [B28-C01](../programa/clases/B28/B28-C01-fundamentos-de-mensajeros-astronomicos/CLASE.md):**
- Calcular la constante y el retardo de dispersión del plasma.
- Por la dispersión del plasma interestelar: `Δt ∝ DM/ν²`.
- 🎯 **Por qué importa:** Un solo evento, como una fusión de estrellas de neutrones, emite varios mensajeros que llegan por caminos y en momentos distintos. Entender por qué unos llegan alineados con la fuente y otros no es el primer paso para combinarlos.
- 🔗 **Se estudia junto con:** mensajero, radio de Larmor, medida de dispersión, retraso por masa.

📘 **Dónde se aprende** (1 clase): [B28-C01 · Fundamentos de mensajeros astronómicos](../programa/clases/B28/B28-C01-fundamentos-de-mensajeros-astronomicos/CLASE.md).

### Dispersión en la línea de visión

- La dispersión en la línea de visión `σ_los` es la desviación típica de las velocidades radiales de sus estrellas.

💡 **Contexto en la clase [B25-C10](../programa/clases/B25/B25-C10-galaxias-irregulares-y-enanas/CLASE.md):**
- **Idea central (modelo mental):** Imagina un enjambre cuyo tamaño y agitación conoces: de ellos deduces cuán fuerte es lo que lo mantiene unido. Analogía: la agitación es `σ_los` y lo que sostiene el enjambre es la masa. Su límite: el enjambre solo da la masa dentro de un radio concreto, el de media luz, no la masa total.
- 🎯 **Por qué importa:** Las galaxias enanas son las más abundantes y las más ricas en materia oscura según su masa dinámica; además son los sitios donde las predicciones del modelo cosmológico se ponen a prueba. Pero con pocas estrellas medidas y sin rotación ordenada, su masa depende de un estimador.
- 🔗 **Se estudia junto con:** galaxia irregular, galaxia enana, enanas esferoidales, ultratenues.

📘 **Dónde se aprende** (1 clase): [B25-C10 · Galaxias irregulares y enanas](../programa/clases/B25/B25-C10-galaxias-irregulares-y-enanas/CLASE.md).

### Dispersión intrínseca

- La dispersión intrínseca es el ancho de la relación por la franja de inestabilidad finita.

💡 **Cómo se explica en la clase [B24-C13](../programa/clases/B24/B24-C13-estrellas-variables/CLASE.md):**
- La relación depende de la metalicidad y de la dispersión intrínseca; el ajuste lineal es una aproximación; el punto cero absoluto exige distancias geométricas.
- Nombrar qué limita la calibración (metalicidad, extinción, dispersión intrínseca).
- 🎯 **Por qué importa:** Las cefeidas y otras estrellas pulsantes cumplen que cuanto más largo es el periodo, mayor es la luminosidad. Medir un periodo equivale entonces a conocer la luminosidad intrínseca y, por comparación con el brillo aparente, la distancia.
- 🔗 **Se estudia junto con:** estrella variable pulsante, cefeida clásica, periodo, relación periodo–luminosidad.

📘 **Dónde se aprende** (1 clase): [B24-C13 · Estrellas variables](../programa/clases/B24/B24-C13-estrellas-variables/CLASE.md).

### Dispersión lineal

- La dispersión lineal `d cos β/(m f_cam)` da nm por mm en el detector.

💡 **Cómo se explica en la clase [B45-C06](../programa/clases/B45/B45-C06-diseno-de-espectrografos/CLASE.md):**
- *Descripción textual:* la rendija se proyecta sobre el detector y su ancho dividido por la dispersión lineal da el ancho espectral.
- Obtener la resolución por fórmula, por dispersión lineal y por trazado de rayos.
- 🎯 **Por qué importa:** El diseño se decide con unos pocos parámetros que se compensan entre sí. La decisión central: ¿qué ancho de rendija da la resolución deseada y cuántos píxeles muestrean cada elemento?
- 🔗 **Se estudia junto con:** rendija, colimador, factor anamórfico, elemento de resolución.

📘 **Dónde se aprende** (1 clase): [B45-C06 · Diseño de espectrógrafos](../programa/clases/B45/B45-C06-diseno-de-espectrografos/CLASE.md).

### Dispersivo

- Un medio o un esquema es dispersivo si ondas de distinta `k` viajan a distinta velocidad.

💡 **Contexto en la clase [B21-C02](../programa/clases/B21/B21-C02-ecuacion-de-onda-esquemas-y-dispersion-numerica/CLASE.md):**
- **Idea central (modelo mental):** Reemplazar la cuerda continua por una fila de cuentas unidas por resortes. Cada cuenta acelera según cuánto se aparta de sus dos vecinas. Una onda larga se parece mucho a la cuerda real; una onda cuya longitud es de apenas unas cuentas «ve» la granularidad y viaja más lenta.
- 🎯 **Por qué importa:** Casi toda señal que viaja en el espacio —ondas de radio, ondas de Alfvén en la corona solar, ondas sísmicas en una luna, vibraciones de una estructura— obedece alguna forma de la ecuación de onda.
- 🔗 **Se estudia junto con:** ecuación de onda, onda viajera, onda estacionaria, número de onda.

📘 **Dónde se aprende** (1 clase): [B21-C02 · Ecuación de onda: esquemas y dispersión numérica](../programa/clases/B21/B21-C02-ecuacion-de-onda-esquemas-y-dispersion-numerica/CLASE.md).

### Disponibilidad

- La disponibilidad es la probabilidad de que el sitio funcione.
- La disponibilidad es `MTBF/(MTBF + MTTR)`.
- (Es la convención de este curso, didáctica.) La disponibilidad a una demanda `D` es `P(M ≥ D)`.
- *(y 7 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B28-C16](../programa/clases/B28/B28-C16-redes-internacionales-de-alertas/CLASE.md):**
- Descripción larga: la disponibilidad reduce la cobertura en un cuarto; la distribución en longitud hace casi válida la independencia.
- Incorporar la disponibilidad de cada sitio.
- ⚠️ **Error frecuente:** Ignorar la disponibilidad. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** La cobertura de una red depende de su distribución geográfica, no solo del número de telescopios. La decisión central: ¿qué probabilidad hay de que, al llegar una alerta, al menos un sitio de la red pueda observar la fuente?
- 🔗 **Se estudia junto con:** red, altura, noche local, probabilidad de la red.

📘 **Dónde se aprende** (11 clases): [B28-C16 · Redes internacionales de alertas](../programa/clases/B28/B28-C16-redes-internacionales-de-alertas/CLASE.md); [B33-C09 · Planes de continuidad ante eventos de clima espacial](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md); [B48-C15 · Gestión de fallas de instrumentos](../programa/clases/B48/B48-C15-gestion-de-fallas-de-instrumentos/CLASE.md); [B59-C18 · Fiabilidad de equipos mineros](../programa/clases/B59/B59-C18-fiabilidad-de-equipos-mineros/CLASE.md); [B67-C08 · Informe de disponibilidad de volátiles con incertidumbre](../programa/clases/B67/B67-C08-informe-de-disponibilidad-de-volatiles-con-incertidumbre/CLASE.md); [B78-C22 · Ciclos de trabajo y operación de propulsión eléctrica](../programa/clases/B78/B78-C22-ciclos-de-trabajo-y-operacion-de-propulsion-electrica/CLASE.md) y 5 más.

### Disponibilidad individual

- La disponibilidad individual `p` es la probabilidad de que una persona pueda actuar.

💡 **Cómo se explica en la clase [B122-C10](../programa/clases/B122/B122-C10-planes-de-continuidad-institucional-y-de-operaciones/CLASE.md):**
- El ejemplo conductor es una institución sintética con cuatro funciones esenciales (Control de la misión `k = 3`, Seguridad de las comunicaciones `k = 2`, Comunicación de crisis `k = 1`, Soporte de TI `k = 2`), disponibilidad individual `p = 0,85` y objetivo `0,99`.
- Ver el efecto de la disponibilidad individual `p`.
- 🎯 **Por qué importa:** No hay clase equivalente sobre continuidad de funciones institucionales. La decisión central: ¿qué dotación mínima asegura que cada función esencial se cubra con al menos el 99 %?
- 🔗 **Se estudia junto con:** función esencial, dotación mínima, plantilla, plan de continuidad de operaciones.

📘 **Dónde se aprende** (1 clase): [B122-C10 · Planes de continuidad institucional y de operaciones](../programa/clases/B122/B122-C10-planes-de-continuidad-institucional-y-de-operaciones/CLASE.md).

### Disposición

- No conformidad: producto que no cumple su requisito. Disposición: decisión sobre qué hacer.
- Disposición: retiro de la nave al final de su vida.

💡 **Cómo se explica en la clase [B90-C17](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md):**
- La regla de disposición y la estadística de esta clase son de ejemplo.
- S --> R["Disposicion:<br/>continuar, corregir<br/>o detener"]
- 🎯 **Por qué importa:** Una falla única en 500 horas de ensayo no demuestra que el equipo sea confiable: solo acota la tasa de fallas. Y una anomalía mal registrada se pierde.
- 🔗 **Se estudia junto con:** Anomalía/discrepancia, No conformidad, Severidad, Causa raíz.

📘 **Dónde se aprende** (2 clases): [B90-C17 · Gestión de anomalías de prueba](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md); [B96-C18 · Fin de vida y disposición orbital](../programa/clases/B96/B96-C18-fin-de-vida-y-disposicion-orbital/CLASE.md).

### Disposición a pagar

- La disposición a pagar (DAP) `v` es lo máximo que un cliente pagaría.

💡 **Cómo se explica en la clase [B125-C01](../programa/clases/B125/B125-C01-mercado-de-datos-espaciales/CLASE.md):**
- Modelar la disposición a pagar (DAP) de una población de clientes con una distribución uniforme.
- 🎯 **Por qué importa:** [B124](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) trata los segmentos de la industria en general; ninguna clase explica por qué un dato crudo puede valer cero y aun así sostener empresas.
- 🔗 **Se estudia junto con:** sustituto gratuito, ingreso por cliente, cadena de valor, dato abierto.

📘 **Dónde se aprende** (1 clase): [B125-C01 · Mercado de datos espaciales](../programa/clases/B125/B125-C01-mercado-de-datos-espaciales/CLASE.md).

### Disposición posmisión

- La disposición posmisión (PMD) es el conjunto de acciones para retirar o dejar segura la nave.

💡 **Cómo se explica en la clase [B118-C11](../programa/clases/B118/B118-C11-diseno-para-mitigacion-de-desechos/CLASE.md):**
- Las directrices IADC Rev. 4 (enero de 2025, consultadas) piden que la probabilidad de disposición posmisión exitosa sea al menos del 90 % con un objetivo del 99 % o más, y que en las grandes constelaciones se considere una probabilidad mayor.
- 🎯 **Por qué importa:** Una disposición solo es posible si el satélite sigue funcionando al final de su vida. La probabilidad de éxito de la PMD no es la fiabilidad de la misión, sino la de las funciones necesarias para disponer.
- 🔗 **Se estudia junto con:** fiabilidad, modo de falla, redundancia, presupuesto de fiabilidad.

📘 **Dónde se aprende** (1 clase): [B118-C11 · Diseño para mitigación de desechos](../programa/clases/B118/B118-C11-diseno-para-mitigacion-de-desechos/CLASE.md).

### Dispositivo físico entre una fuente de energía y un peligro

- Inhibidor independiente: dispositivo físico entre una fuente de energía y un peligro. Cronología: secuencia de eventos con sus tiempos.

💡 **Contexto en la clase [B90-C15](../programa/clases/B90/B90-C15-pruebas-de-despliegue/CLASE.md):**
- 🎯 **Por qué importa:** Un mecanismo que despliega en el laboratorio con un margen justo puede quedarse a medio camino con lubricación degradada o arrastre de un arnés. La decisión central: ¿cuánto par sobra frente al arrastre y con qué velocidad llega a la traba?
- 🔗 **Se estudia junto con:** Despliegue, Par de resorte, Arrastre, Margen de par.

📘 **Dónde se aprende** (1 clase): [B90-C15 · Pruebas de despliegue](../programa/clases/B90/B90-C15-pruebas-de-despliegue/CLASE.md).

### Distancia

- El tiempo de ida y vuelta `t` es lo que tarda el pulso; la distancia (*range*) es `R = ct/2`.

💡 **Cómo se explica en la clase [B57-C09](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md):**
- *Descripción textual:* los pulsos se promedian, se ajusta el instante de subida, se convierte en distancia y se resta a la altura del satélite.
- Convertir tiempo de ida y vuelta en distancia (`R = ct/2`) y viceversa.
- 🎯 **Por qué importa:** La altura del mar cambia unos milímetros por año, pero el eco de un pulso es ruidoso. La decisión central: ¿cuántos pulsos hay que promediar y cómo se ajusta el eco para que el error de distancia del ajuste se reduzca lo necesario?
- 🔗 **Se estudia junto con:** tiempo de ida y vuelta, forma de onda, flanco de subida, reajuste.

📘 **Dónde se aprende** (1 clase): [B57-C09 · Altimetría satelital](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md).

### Distancia angular

- La distancia angular `c` entre dos puntos es el ángulo, medido desde el centro, entre las direcciones a ambos; la distancia de círculo máximo es `d = R c` (con `c` en radianes).
- La distancia angular `d` al borde de un agujero coronal.

💡 **Cómo se explica en la clase [B04-C16](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md):**
- *Descripción textual:* de dos puntos dados por latitud y longitud se obtienen dos caminos: el del coseno, igual al producto escalar de los vectores unitarios, y el del haversine; ambos dan la distancia angular `c`, que multiplicada por el radio da la distancia en longitud; el primero pierde precisión para `c` pequeño y el segundo no.
- Calcular la distancia angular entre dos puntos con la fórmula del coseno y con la del haversine.
- ⚠️ **Error frecuente:** Confundir distancia angular con distancia en km. Se corrige con `d = R c` y el ejercicio 1.
- 🎯 **Por qué importa:** Para pasar de un lugar a otro de la Tierra, un avión sigue (casi) un círculo máximo. Para decidir cuánto debe girar un telescopio entre dos estrellas, se calcula la distancia angular sobre la esfera celeste.
- 🔗 **Se estudia junto con:** esfera, círculo máximo, círculo menor, distancia de círculo máximo.

📘 **Dónde se aprende** (2 clases): [B04-C16 · Geometría de esferas y círculos máximos](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md); [B33-C10 · Modelos de viento solar para pronóstico (Parker y WSA)](../programa/clases/B33/B33-C10-modelos-de-viento-solar-para-pronostico-parker-y-wsa/CLASE.md).

### Distancia cenital

- La altura `h` es el ángulo de un astro sobre el horizonte (0° horizonte, 90° cenit); la distancia cenital es `z = 90° − h`.

💡 **Contexto en la clase [B08-C04](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md):**
- **Idea central (modelo mental):** AR y Dec están pegados a las estrellas; altura y acimut están pegados a tu lugar. Con el giro de la Tierra, el punto vernal sube por el este y el cielo completo se desplaza. El ángulo horario es el puente: `H = TSL − α`.
- 🎯 **Por qué importa:** Una tabla dice «Luna: AR 2,14 h, Dec +17,1°». Un telescopio, una cámara o tus ojos necesitan «a 35° de altura, hacia el nornoreste».
- 🔗 **Se estudia junto con:** altura, acimut, ángulo horario, tránsito.

📘 **Dónde se aprende** (1 clase): [B08-C04 · Altura y acimut](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md).

### Distancia comóvil

- La distancia comóvil es `D_C = (c/H₀)∫dz/E`.

💡 **Cómo se explica en la clase [B26-C17](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md):**
- *Descripción textual:* las fluctuaciones crecen como `a` mientras la materia domina y más despacio después; por separado, la regla BAO se convierte en ángulo dividiéndola por la distancia comóvil.
- Calcular una distancia comóvil por cuadratura.
- 🎯 **Por qué importa:** Los grandes sondeos de galaxias miden cómo se agrupan, y de su agrupamiento salen la densidad de materia y la historia de la expansión. Para interpretarlos hace falta saber cómo crece una fluctuación y qué distancia angular corresponde a una escala física.
- 🔗 **Se estudia junto con:** perturbación de densidad, crecimiento lineal, ecuación de crecimiento, supresión.

📘 **Dónde se aprende** (4 clases): [B26-C17 · Estructura cosmológica](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md); [B26-C19 · Energía oscura y parámetros](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md); [B40-C04 · Problemas del horizonte y de la planitud](../programa/clases/B40/B40-C04-problemas-del-horizonte-y-de-la-planitud/CLASE.md); [B40-C07 · Espectro angular de potencias del CMB](../programa/clases/B40/B40-C07-espectro-angular-de-potencias-del-cmb/CLASE.md).

### Distancia comóvil transversal

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B36-C07](../programa/clases/B36/B36-C07-oscilaciones-acusticas-barionicas-como-regla-estandar/CLASE.md):**
- **Idea central (modelo mental):** Es como una regla de longitud conocida colocada a gran distancia: cuanto más pequeña la vemos, más lejos está.
- 🎯 **Por qué importa:** Una regla estándar permite medir distancias si se conoce su longitud. La decisión central: ¿cuánto mide la regla y cuál es la precisión con que se puede medir su dilatación?
- 🔗 **Se estudia junto con:** horizonte sonoro, velocidad del sonido, carga bariónica, igualdad materia–radiación.

📘 **Dónde se aprende** (1 clase): [B36-C07 · Oscilaciones acústicas bariónicas como regla estándar](../programa/clases/B36/B36-C07-oscilaciones-acusticas-barionicas-como-regla-estandar/CLASE.md).

### Distancia crítica

- La distancia crítica es donde el campo directo iguala al reverberante.

💡 **Cómo se explica en la clase [B109-C10](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md):**
- Con `V = 127 m³` (Burke et al., 2022) y una superficie equivalente `6V^(2/3) = 151,6 m²` y `α = 0,20` (ilustrativos): `A = 30,3 m²`, `T60 = 0,161 V/A = 0,67 s`, `R = A/(1 − α) = 37,9 m²` y distancia crítica `√(Q R/16π) = 1,23 m` con `Q = 2`.
- Más allá de la distancia crítica alejarse apenas ayuda: de `1` a `5 m` bajan solo `3,7 dB`.
- ⚠️ **Error frecuente:** Creer que alejarse siempre baja el nivel. Se corrige con 8.3: la distancia crítica.
- 🎯 **Por qué importa:** El ruido continuo degrada la comunicación, el sueño y el trabajo aunque no dañe el oído. La decisión central: ¿qué fuente reduzco primero y cuánto baja el nivel de la cabina?
- 🔗 **Se estudia junto con:** nivel de potencia sonora, nivel de presión, campo directo, reverberante.

📘 **Dónde se aprende** (1 clase): [B109-C10 · Acústica y control de ruido interior](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md).

### Distancia de campo lejano

- La distancia de campo lejano `2D²/λ` es el criterio clásico para medir el patrón.

💡 **Cómo se explica en la clase [B91-C05](../programa/clases/B91/B91-C05-medicion-y-calibracion-de-antenas/CLASE.md):**
- *Descripción textual:* de `D` y `λ` sale la distancia de campo lejano; a distancias menores aparece un error de fase que deforma el patrón; la ganancia se obtiene por comparación con una referencia y su incertidumbre, por suma cuadrática.
- Una antena sintética de `D = 1,2 m` a `8,4 GHz` tiene `λ = 35,69 mm` y una distancia de campo lejano de `80,70 m`.
- ⚠️ **Error frecuente:** Medir a cualquier distancia y asumir que es campo lejano. Ver 8.1.
- 🎯 **Por qué importa:** Una antena se acepta si su ganancia y su patrón medidos cumplen la especificación dentro de una incertidumbre conocida. La decisión central: ¿a qué distancia medir y con qué incertidumbre, para poder afirmar que la antena cumple?
- 🔗 **Se estudia junto con:** error de fase en el borde, transferencia de ganancia, incertidumbre combinada, expandida.

📘 **Dónde se aprende** (1 clase): [B91-C05 · Medición y calibración de antenas](../programa/clases/B91/B91-C05-medicion-y-calibracion-de-antenas/CLASE.md).

### Distancia de círculo máximo

- La distancia angular `c` entre dos puntos es el ángulo, medido desde el centro, entre las direcciones a ambos; la distancia de círculo máximo es `d = R c` (con `c` en radianes).

💡 **Cómo se explica en la clase [B04-C16](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md):**
- Dos puntos a 60° N con `Δλ = 160°` están a un arco de paralelo `R cos 60° × (160° en rad) = 0,5 × 2,7925 × 6371 = 8895,6 km` y a una distancia de círculo máximo `6560,2 km`.
- 🎯 **Por qué importa:** Para pasar de un lugar a otro de la Tierra, un avión sigue (casi) un círculo máximo. Para decidir cuánto debe girar un telescopio entre dos estrellas, se calcula la distancia angular sobre la esfera celeste.
- 🔗 **Se estudia junto con:** esfera, círculo máximo, círculo menor, distancia angular.

📘 **Dónde se aprende** (1 clase): [B04-C16 · Geometría de esferas y círculos máximos](../programa/clases/B04/B04-C16-geometria-de-esferas-y-circulos-maximos/CLASE.md).

### Distancia de coordinación

- La distancia de coordinación `d` es el radio de esa zona en este modelo circular.

💡 **Cómo se explica en la clase [B120-C02](../programa/clases/B120/B120-C02-zonas-de-coordinacion-entre-servicios-radioelectricos/CLASE.md):**
- Calcular una distancia de coordinación con la pérdida de espacio libre y comprobarla con su inversa.
- El script [coordinacion.py](coordinacion.py) calcula `d` con la pérdida de espacio libre, evalúa seis estaciones sintéticas y aplica los plazos (comprueba la inversa a 1e-9 dB, la razón 2:1 y la distancia con dos fórmulas a 0,01 km).
- 🎯 **Por qué importa:** Coordinar con otros servicios define dónde y cómo se puede operar y ninguna clase lo trata. La decisión central: ¿con qué administraciones hay que coordinar una estación terrena y en cuánto tiempo deben responder?
- 🔗 **Se estudia junto con:** zona de coordinación, PIRE, pérdida de espacio libre, potencia permisible.

📘 **Dónde se aprende** (1 clase): [B120-C02 · Zonas de coordinación entre servicios radioeléctricos](../programa/clases/B120/B120-C02-zonas-de-coordinacion-entre-servicios-radioelectricos/CLASE.md).

### Distancia de falla

- La distancia de falla es el módulo del error de llegada.

💡 **Cómo se explica en la clase [B75-C18](../programa/clases/B75/B75-C18-propagacion-de-dispersion-inicial/CLASE.md):**
- Con un error de velocidad de salida de `1 m/s` por eje (sintético), la llegada a Marte se dispersa `35 155 km` en x y `70 958 km` en y (1σ), con una elipsoide de semiejes `78 512` y `10 330 km`; la distancia de falla tiene mediana `53 136 km` y percentil 95 `154 452 km`, el `14,2 %` del radio de Hill de Marte (`1 084 136 km`).
- Distancia de falla (3D): mediana MC = 53136 km ; percentil 95 = 154452 km ; radio de Hill de Marte = 1084136 km ;
- 🎯 **Por qué importa:** Para decidir cuántas correcciones de trayectoria hacen falta hay que saber cuánto se dispersa la llegada. La decisión central: ¿qué dispersión de posición produce un error de velocidad dado en la salida y cuán buena es la aproximación lineal?
- 🔗 **Se estudia junto con:** matriz de transición, covarianza, elipsoide de dispersión, Monte Carlo.

📘 **Dónde se aprende** (1 clase): [B75-C18 · Propagación de dispersión inicial](../programa/clases/B75/B75-C18-propagacion-de-dispersion-inicial/CLASE.md).

### Distancia de Fraunhofer

- La distancia de Fraunhofer es `2D²/λ`.

💡 **Contexto en la clase [B49-C05](../programa/clases/B49/B49-C05-medicion-y-calibracion-de-patrones-de-antena/CLASE.md):**
- **Idea central (modelo mental):** Como iluminar una pared con una linterna: de cerca la mancha tiene franjas deformadas; de lejos adopta su forma definitiva.
- 🎯 **Por qué importa:** Un patrón mal medido o medido demasiado cerca da un haz y unos lóbulos falsos. La decisión central: ¿a qué distancia medir y con qué nivel de ruido, para que el ancho y el lóbulo lateral sean fiables?
- 🔗 **Se estudia junto con:** patrón de Airy, campo lejano, ancho a mitad de potencia, barrido.

📘 **Dónde se aprende** (1 clase): [B49-C05 · Medición y calibración de patrones de antena](../programa/clases/B49/B49-C05-medicion-y-calibracion-de-patrones-de-antena/CLASE.md).

### Distancia de frenado

- La distancia de frenado es `d = v τ + v²/(2a)`, con `τ` la suma del ciclo y la latencia del sensor y `a` la desaceleración.

💡 **Cómo se explica en la clase [B98-C05](../programa/clases/B98/B98-C05-autonomia-de-bajo-nivel-y-comportamientos-reactivos/CLASE.md):**
- *Descripción textual:* el peligro se detecta a la distancia R; el reflejo suma latencia, ciclo y frenado y se detiene antes de R; sin reflejo, el vehículo recorre la velocidad por el viaje de ida y vuelta y la decisión.
- Calcular la distancia de frenado de un reflejo con ciclo, latencia de sensor y desaceleración.
- 🎯 **Por qué importa:** Ningún plan, por bueno que sea, protege a un vehículo del peligro que aparece entre dos ciclos de comunicación. La decisión central: ¿qué debe resolver el vehículo por sí mismo y a qué velocidad puede ir para que ese reflejo llegue a tiempo?
- 🔗 **Se estudia junto con:** comportamiento reactivo, reflejo, velocidad máxima admisible, histéresis.

📘 **Dónde se aprende** (1 clase): [B98-C05 · Autonomía de bajo nivel y comportamientos reactivos](../programa/clases/B98/B98-C05-autonomia-de-bajo-nivel-y-comportamientos-reactivos/CLASE.md).

### Distancia de Hamming

- La distancia de Hamming compara perfiles de obligaciones.

💡 **Cómo se explica en la clase [B119-C33](../programa/clases/B119/B119-C33-matriz-comparativa-de-obligaciones-juridicas-por-actor/CLASE.md):**
- Comparar actores por distancia de Hamming y listar lo no consultado.
- Ejercicio 6 · autónomo. Calcula la distancia de Hamming entre Estado de lanzamiento y Estado de registro.
- 🎯 **Por qué importa:** B119 presenta los instrumentos uno por uno; distinguir qué obligaciones recaen en Estados y en operadores exige compararlos sistemáticamente. Esta clase integra las clases C01 a C11 y es la evidencia de portafolio del bloque.
- 🔗 **Se estudia junto con:** actor, obligación directa, Estado de lanzamiento, Estado de registro.

📘 **Dónde se aprende** (1 clase): [B119-C33 · Matriz comparativa de obligaciones jurídicas por actor](../programa/clases/B119/B119-C33-matriz-comparativa-de-obligaciones-juridicas-por-actor/CLASE.md).

### Distancia de Jaccard

- La distancia de Jaccard es `1 − J`.

💡 **Contexto en la clase [B119-C19](../programa/clases/B119/B119-C19-legislacion-comparada-y-casos-nacionales/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR L["Tratado: principio"] --> N["Ley nacional"] N --> M["Matriz de rasgos"] M --> J["Jaccard"] J --> P["Par más parecido / distinto"] M --> U["Rasgos únicos y comunes"] ``` *Descripción textual:* el principio del tratado se concreta en leyes nacionales; estas se tabulan por rasgos y se comparan con Jaccard.
- 🎯 **Por qué importa:** Los tratados fijan principios y dejan la aplicación a los Estados (art. VI; art.
- 🔗 **Se estudia junto con:** rasgo, similitud de Jaccard, matriz de rasgos, rasgo único.

📘 **Dónde se aprende** (1 clase): [B119-C19 · Legislación comparada y casos nacionales](../programa/clases/B119/B119-C19-legislacion-comparada-y-casos-nacionales/CLASE.md).

### Distancia de Kolmogorov–Smirnov

- La distancia de Kolmogorov–Smirnov (KS) entre la acumulada empírica y la normal es el máximo de la diferencia absoluta de ambas acumuladas.

💡 **Contexto en la clase [B12-C06](../programa/clases/B12/B12-C06-teorema-central-del-limite/CLASE.md):**
- **Idea central (modelo mental):** Sumar variables independientes es mezclar sus formas; en cada mezcla se suavizan las esquinas y las asimetrías. Tras muchas mezclas queda siempre la misma silueta, de la que sólo importan el centro y la dispersión.
- 🎯 **Por qué importa:** Ningún instrumento tiene ruido exactamente normal, y sin embargo casi todas las incertidumbres se expresan con campanas. La razón es que se reportan promedios y sumas de muchas contribuciones pequeñas.
- 🔗 **Se estudia junto con:** teorema central del límite, Estandarizar, asimetría, colas pesadas.

📘 **Dónde se aprende** (1 clase): [B12-C06 · Teorema central del límite](../programa/clases/B12/B12-C06-teorema-central-del-limite/CLASE.md).

### Distancia de luminosidad

- La distancia de luminosidad `D_L` define cuánto flujo llega: `F = L/(4πD_L²)`.

💡 **Cómo se explica en la clase [B26-C19](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md):**
- Definir distancia de luminosidad y módulo de distancia.
- La evidencia es la tabla de distancias de luminosidad del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** La aceleración cósmica se descubrió porque las supernovas Ia lejanas aparecían más débiles de lo esperado. Para reproducir ese razonamiento hay que saber calcular la distancia de luminosidad y ver cuánto cambia con el contenido del universo.
- 🔗 **Se estudia junto con:** distancia comóvil, distancia transversal, módulo de distancia, modelo de Milne.

📘 **Dónde se aprende** (1 clase): [B26-C19 · Energía oscura y parámetros](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md).

### Distancia de Mahalanobis

- La distancia de Mahalanobis al cuadrado, `d² = eᵀP⁻¹e`, mide la distancia en unidades de incertidumbre y, para un vector gaussiano de dimensión `k`, sigue una `χ²` con `k` grados de libertad.
- La distancia de Mahalanobis de un punto `x` a una distribución con media `μ` y covarianza `Σ` es `d² = (x − μ)ᵀ Σ⁻¹ (x − μ)`: mide la distancia en unidades de desviación, tomando en cuenta la correlación.
- La distancia de Mahalanobis `d² = eᵀP⁻¹e` marca atípicos multivariados (C18).

💡 **Cómo se explica en la clase [B12-C18](../programa/clases/B12/B12-C18-matrices-de-covarianza/CLASE.md):**
- La distancia de Mahalanobis mide cuán adentro o afuera de la nube está un punto.
- *Descripción textual:* de la covarianza se obtienen cuatro cosas: la elipse (por autovalores y ejes), la covarianza de una transformación lineal, la distancia de Mahalanobis para decidir compatibilidad con la `χ²`, y un factor de Cholesky para generar muestras con esa covarianza.
- 🎯 **Por qué importa:** El resultado de una determinación de órbita o de un ajuste no es un número sino un vector con una matriz de covarianza; sin ella no se puede propagar, comparar con otro resultado ni calcular probabilidades.
- 🔗 **Se estudia junto con:** matriz de covarianza, simétrica, semidefinida positiva, matriz de correlación.

📘 **Dónde se aprende** (3 clases): [B12-C18 · Matrices de covarianza](../programa/clases/B12/B12-C18-matrices-de-covarianza/CLASE.md); [B12-C19 · Detección de valores atípicos](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md); [B17-C05 · Detección de anomalías](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md).

### Distancia de paso

- La distancia de paso (*miss distance*) es esa mínima distancia.

💡 **Cómo se explica en la clase [B118-C05](../programa/clases/B118/B118-C05-conjunciones-orbitales/CLASE.md):**
- Con `Δt = 4 s` el paso sube a 29,7250 km (cociente 2,0000): la distancia es proporcional al retraso.
- *Descripción textual:* de las dos órbitas se obtienen las posiciones en cada instante; el mínimo de la distancia da el TCA y la distancia de paso, y la velocidad relativa se contrasta con la fórmula analítica.
- ⚠️ **Error frecuente:** Confundir distancia de paso con distancia en el instante de la alerta. Se corrige con 8.3: el TCA es el mínimo.
- 🎯 **Por qué importa:** La alerta de conjunción es el producto básico del tráfico espacial. Su geometría explica por qué los encuentros son tan rápidos y por qué un pequeño desfase en el tiempo produce un cambio grande en la distancia.
- 🔗 **Se estudia junto con:** conjunción, TCA, velocidad relativa, encuentro.

📘 **Dónde se aprende** (1 clase): [B118-C05 · Conjunciones orbitales](../programa/clases/B118/B118-C05-conjunciones-orbitales/CLASE.md).

### Distancia de seguridad

- La distancia de seguridad separa a las personas del lugar de lanzamiento.

💡 **Cómo se explica en la clase [B119-C24](../programa/clases/B119/B119-C24-limites-legales-y-de-seguridad-de-la-experimentacion-educativa/CLASE.md):**
- *Descripción textual:* el impulso y la masa dan la velocidad; de ella el apogeo con y sin arrastre; del apogeo la distancia de seguridad y la decisión de revisar la reglamentación.
- Estimar una distancia de seguridad ilustrativa y el umbral de revisión.
- 🎯 **Por qué importa:** Ninguna clase trata los límites de la experimentación educativa; el art. VI del tratado exige autorización y supervisión de las actividades no gubernamentales, y la escala pequeña no exime de ella.
- 🔗 **Se estudia junto con:** impulso total, apogeo, resistencia, umbral de revisión.

📘 **Dónde se aprende** (1 clase): [B119-C24 · Límites legales y de seguridad de la experimentación educativa](../programa/clases/B119/B119-C24-limites-legales-y-de-seguridad-de-la-experimentacion-educativa/CLASE.md).

### Distancia diaria

- La distancia diaria es velocidad × uso × horas.

💡 **Cómo se explica en la clase [B97-C20](../programa/clases/B97/B97-C20-mision-robotica-integrada-simulada/CLASE.md):**
- El uso y la ruta actúan siempre sobre la distancia diaria; la batería solo mientras limita las horas (aquí limita, porque `E/P` es menor que 4 h).
- *Descripción textual:* la energía y el tiempo fijan las horas útiles; con la velocidad dan la distancia diaria; la distancia por el factor de ruta da los días nominales y las anomalías los alargan.
- 🎯 **Por qué importa:** Una misión se diseña con un presupuesto de días y de margen. Un modelo integrado, aunque simple, muestra cuál parámetro domina y cuánto margen pide una anomalía, antes de invertir en simulaciones detalladas.
- 🔗 **Se estudia junto con:** días nominales, anomalía, percentil 95, sensibilidad.

📘 **Dónde se aprende** (1 clase): [B97-C20 · Misión robótica integrada simulada](../programa/clases/B97/B97-C20-mision-robotica-integrada-simulada/CLASE.md).

### Distancia epicentral

- La distancia epicentral `Δ` es el ángulo en el centro entre fuente y estación.

💡 **Contexto en la clase [B53-C02](../programa/clases/B53/B53-C02-sismologia-planetaria/CLASE.md):**
- **Idea central (modelo mental):** Analogía: el trueno y el relámpago: la luz llega antes que el sonido, y el retraso dice a qué distancia cayó el rayo.
- 🎯 **Por qué importa:** Un solo sismómetro no da la posición completa de un evento. La decisión central: ¿cuánto vale la distancia al evento y con qué incertidumbre, si solo se leen los tiempos de llegada P y S?
- 🔗 **Se estudia junto con:** parámetro de rayo, retraso S−P, fase.

📘 **Dónde se aprende** (1 clase): [B53-C02 · Sismología planetaria](../programa/clases/B53/B53-C02-sismologia-planetaria/CLASE.md).

### Distancia equivalente

- La distancia equivalente es la que da cierta `T_eq`.

💡 **Cómo se explica en la clase [B29-C13](../programa/clases/B29/B29-C13-zonas-de-habitabilidad/CLASE.md):**
- Una estrella más fría tiene la distancia equivalente mucho más corta, a la que la rotación sincrónica y las erupciones pueden ser importantes.
- 🎯 **Por qué importa:** La temperatura de equilibrio es la primera estimación de si un mundo es cálido o helado, pero no es la temperatura de la superficie: depende del albedo y del efecto invernadero. La decisión central: ¿a qué distancias una estrella da una temperatura de equilibrio dada y cuánto cambia con el albedo?
- 🔗 **Se estudia junto con:** zona habitable, temperatura de equilibrio, albedo, flujo.

📘 **Dónde se aprende** (1 clase): [B29-C13 · Zonas de habitabilidad](../programa/clases/B29/B29-C13-zonas-de-habitabilidad/CLASE.md).

### Distancia focal

- La distancia focal `c` es la distancia del centro a cada foco; se cumple `a² = b² + c²`.
- La apertura `D` es el diámetro del objetivo o espejo; la distancia focal `F`, la longitud del camino óptico; la razón focal `N = F/D`.
- La distancia focal `f` de un paraboloide `z = r²/(4f)` es la distancia del vértice al foco.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C09](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md):**
- Paso 2 · Distancia focal. `c = ae = 17,354 au`.
- Antes comprueba: que `e = 0` da una circunferencia con perímetro `2πa`, la elipse 5-4-3 (los semiejes y la distancia focal forman un triángulo 3-4-5), que `d₁ + d₂ = 2a` en 52 puntos, que el perímetro de la elipse 5×3 es 25,52699886 (valor conocido) y que la fórmula de Ramanujan coincide con la integración numérica dentro de 10⁻⁴.
- 🎯 **Por qué importa:** Las órbitas de planetas y cometas son, en buena aproximación, elipses con el Sol en uno de sus focos. Si no sabes qué es un semieje, un foco o la excentricidad, no puedes leer una tabla de elementos orbitales ni distinguir una órbita casi circular, como la de la Tierra, de una muy alargada, como la del cometa Halley.
- 🔗 **Se estudia junto con:** circunferencia, elipse, focos, semieje mayor.

📖 **Explicado a fondo:** [Distancia focal y número f](esencial/esencial-d-l.md#distancia-focal-y-número-f) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (5 clases): [B04-C09 · Circunferencias y elipses](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md); [B08-C14 · Telescopios de iniciación](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md); [B08-C19 · Fotografía astronómica elemental](../programa/clases/B08/B08-C19-fotografia-astronomica-elemental/CLASE.md); [B09-C13 · Áreas y volúmenes por integración](../programa/clases/B09/B09-C13-areas-y-volumenes-por-integracion/CLASE.md); [B71-C08 · Órbitas elípticas](../programa/clases/B71/B71-C08-orbitas-elipticas/CLASE.md).

### Distancia focal posterior

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C05](../programa/clases/B41/B41-C05-lentes-delgadas-y-gruesas/CLASE.md):**
- En la biconvexa gruesa, `f = 103,786 mm`, la distancia focal posterior medida desde el vértice es `89,638 mm` y el plano principal posterior está `14,148 mm` dentro de la lente (fórmula de libro `−14,148 mm`).
- biconvexa gruesa: f = 103.786 mm ; distancia focal posterior (vertice) = 89.638 mm ; plano principal posterior a 14.148 mm dentro del vertice
- 🎯 **Por qué importa:** El objetivo de un refractor es una lente. La decisión central: ¿cuánto se equivoca la fórmula de lente delgada cuando la lente es gruesa?
- 🔗 **Se estudia junto con:** lente delgada, ecuación del fabricante, matriz de rayos, planos principales.

📘 **Dónde se aprende** (1 clase): [B41-C05 · Lentes delgadas y gruesas](../programa/clases/B41/B41-C05-lentes-delgadas-y-gruesas/CLASE.md).

### Distancia focal posterior (BFD)

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C08](../programa/clases/B41/B41-C08-trazado-de-rayos-para-telescopios/CLASE.md):**
- Medir la distancia focal posterior exacta por altura.
- paraxial (matrices): f = 195.0857 mm ; distancia focal posterior (vertice) = 191.7614 mm
- 🎯 **Por qué importa:** Los programas de diseño óptico trazan rayos exactos. La decisión central: ¿cuándo se separa el rayo real del paraxial y cómo crece esa diferencia?
- 🔗 **Se estudia junto con:** trazado exacto, aproximación paraxial, aberración esférica longitudinal, altura del rayo.

📘 **Dónde se aprende** (1 clase): [B41-C08 · Trazado de rayos para telescopios](../programa/clases/B41/B41-C08-trazado-de-rayos-para-telescopios/CLASE.md).

### Distancia imagen

- La distancia objeto `s` y la distancia imagen `s'`.

💡 **Cómo se explica en la clase [B41-C06](../programa/clases/B41/B41-C06-distancias-focales-y-formacion-de-imagen/CLASE.md):**
- El producto de las distancias al foco es constante y define imagen real o virtual.
- La evidencia es la ficha de distancias focales e imagen del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** El foco de una cámara o de un telescopio decide el tamaño de la imagen. La decisión central: ¿dónde cae la imagen y de qué tamaño es?
- 🔗 **Se estudia junto con:** distancia objeto, aumento lateral, imagen real, virtual.

📘 **Dónde se aprende** (1 clase): [B41-C06 · Distancias focales y formación de imagen](../programa/clases/B41/B41-C06-distancias-focales-y-formacion-de-imagen/CLASE.md).

### Distancia interpupilar

- La distancia interpupilar es la separación de tus ojos que debes igualar con las bisagras; el ajuste dióptrico corrige la diferencia entre tus dos ojos.

💡 **Cómo se explica en la clase [B08-C13](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md):**
- Abre las bisagras hasta que veas un solo círculo (distancia interpupilar).
- Ajustar distancia interpupilar, enfoque y dioptrías.
- 🎯 **Por qué importa:** Unos binoculares multiplican lo que ves, pero también multiplican el riesgo si miras al Sol. La pregunta motivadora: ¿qué binoculares sirven para mi caso y cómo los uso sin hacerme daño?
- 🔗 **Se estudia junto con:** aumento, objetivo, pupila de salida, campo de visión.

📘 **Dónde se aprende** (1 clase): [B08-C13 · Uso seguro de binoculares](../programa/clases/B08/B08-C13-uso-seguro-de-binoculares/CLASE.md).

### Distancia KS

- La distancia KS entre distribuciones.

💡 **Cómo se explica en la clase [B34-C07](../programa/clases/B34/B34-C07-comparacion-de-modelos-coronales-con-observaciones/CLASE.md):**
- Calcular la distancia de Kolmogorov–Smirnov.
- 🎯 **Por qué importa:** Una buena correlación puede ocultar un error de escala. La decisión central: ¿qué métrica detecta cada tipo de discrepancia?
- 🔗 **Se estudia junto con:** correlación, razón media, prueba de permutaciones, desplazamiento.

📘 **Dónde se aprende** (1 clase): [B34-C07 · Comparación de modelos coronales con observaciones](../programa/clases/B34/B34-C07-comparacion-de-modelos-coronales-con-observaciones/CLASE.md).

### Distancia límite

- La distancia límite es `d = √(L/S_ef)` con `L` en luminosidades solares y `d` en UA.

💡 **Cómo se explica en la clase [B56-C12](../programa/clases/B56/B56-C12-exoplanetas-potencialmente-habitables/CLASE.md):**
- *Descripción textual:* con la temperatura efectiva se calculan los flujos límite, con la luminosidad se obtienen las distancias, y se compara la órbita del planeta.
- 🎯 **Por qué importa:** Elegir blancos para buscar biofirmas exige un criterio objetivo. La zona habitable lo ofrece, con limitaciones.
- 🔗 **Se estudia junto con:** flujo estelar efectivo, zona habitable, borde interno, externo.

📘 **Dónde se aprende** (1 clase): [B56-C12 · Exoplanetas potencialmente habitables](../programa/clases/B56/B56-C12-exoplanetas-potencialmente-habitables/CLASE.md).

### Distancia mínima

- El clasificador de distancia mínima asigna la clase de la media más cercana.

💡 **Cómo se explica en la clase [B15-C22](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md):**
- Las covarianzas de las clases son iguales en la simulación, por lo que la distancia mínima es casi óptima y la máxima verosimilitud (que estima más parámetros con solo 30 muestras) no gana.
- Si el suelo se acerca a la vegetación (media `(0,10; 0,40)` en vez de `(0,20; 0,28)`), la exactitud de distancia mínima baja de `0,910` a `0,765`: ningún clasificador de estas bandas puede mejorarlo mucho porque el solapamiento es propiedad de los datos.
- 🎯 **Por qué importa:** Un mapa de cobertura de suelo parece una verdad; en realidad es una predicción con un error que depende de las muestras elegidas y de cuánto se solapan las clases en el espacio espectral. Cifras como «90 % de exactitud» no significan nada sin decir con qué datos se midieron, ni cómo se reparte el error entre clases.
- 🔗 **Se estudia junto con:** vector espectral, NDVI, clase, muestras de entrenamiento.

📘 **Dónde se aprende** (1 clase): [B15-C22 · Clasificación supervisada de imágenes](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md).

### Distancia mínima de paso

- La distancia mínima de paso es la mínima distancia entre el sensor y la trayectoria.

💡 **Cómo se explica en la clase [B118-C23](../programa/clases/B118/B118-C23-cobertura-sesgos-y-limites-de-las-redes-de-vigilancia/CLASE.md):**
- *Descripción textual:* cada objeto se detecta si el alcance de la red a su tamaño supera la distancia mínima de su paso; la pendiente estimada con los detectados se compara con la de la población completa.
- Definir un criterio de detección por alcance y distancia mínima de paso.
- 🎯 **Por qué importa:** B118-C15 trata solo mega constelaciones; aquí se aporta la comprensión de qué no ve una red. Un catálogo construido con lo detectado subestima los objetos pequeños y lejanos, y las estadísticas que se calculan con él están sesgadas.
- 🔗 **Se estudia junto con:** cobertura, completitud, sesgo de selección, alcance.

📘 **Dónde se aprende** (1 clase): [B118-C23 · Cobertura, sesgos y límites de las redes de vigilancia](../programa/clases/B118/B118-C23-cobertura-sesgos-y-limites-de-las-redes-de-vigilancia/CLASE.md).

### Distancia normalizada

- La distancia normalizada entre dos perfiles de `k` dimensiones en escala 0–100 es `√Σ(Δ)² / (100 √k)`.

💡 **Cómo se explica en la clase [B111-C02](../programa/clases/B111/B111-C02-gestion-intercultural-en-tripulaciones-multinacionales/CLASE.md):**
- Los perfiles sintéticos (cuatro dimensiones 0–100) dan distancias normalizadas de `0,050` dentro de cada grupo y de `0,217` a `0,349` entre grupos; la máxima es `0,349` (M4–M5).
- Calcular distancias normalizadas entre perfiles y localizar la mayor.
- 🎯 **Por qué importa:** Ninguna clase del programa trataba las diferencias culturales y de idioma en equipos internacionales. La decisión central: ¿cómo se vuelve un riesgo de comunicación cuantificable y cómo se mitiga con procedimientos y no con estereotipos?
- 🔗 **Se estudia junto con:** índice de diversidad de Blau, endogrupo, proficiencia.

📘 **Dónde se aprende** (1 clase): [B111-C02 · Gestión intercultural en tripulaciones multinacionales](../programa/clases/B111/B111-C02-gestion-intercultural-en-tripulaciones-multinacionales/CLASE.md).

### Distancia objeto

- La distancia objeto `s` y la distancia imagen `s'`.

💡 **Contexto en la clase [B41-C06](../programa/clases/B41/B41-C06-distancias-focales-y-formacion-de-imagen/CLASE.md):**
- **Idea central (modelo mental):** Como un proyector: al acercar la diapositiva al foco, la imagen se aleja y crece; cuando la diapositiva pasa al interior del foco, la imagen deja de proyectarse (virtual).
- 🎯 **Por qué importa:** El foco de una cámara o de un telescopio decide el tamaño de la imagen. La decisión central: ¿dónde cae la imagen y de qué tamaño es?
- 🔗 **Se estudia junto con:** distancia imagen, aumento lateral, imagen real, virtual.

📘 **Dónde se aprende** (1 clase): [B41-C06 · Distancias focales y formación de imagen](../programa/clases/B41/B41-C06-distancias-focales-y-formacion-de-imagen/CLASE.md).

### Distancia por Cefeidas

- Una distancia por Cefeidas usa estrellas variables cuya luminosidad se relaciona con su período (S2); una distancia por fluctuaciones de brillo superficial usa la granularidad de la imagen de una galaxia elíptica (S3).

💡 **Cómo se explica en la clase [B01-C15](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md):**
- Para dos objetos concretos hay distancias publicadas con incertidumbre: Andrómeda (M31), 765 kpc con ±28 kpc, medida con estrellas Cefeidas del telescopio espacial Hubble (S2), y el cúmulo de Virgo, 16,5 Mpc con ±0,1 Mpc aleatorio y ±1,1 Mpc sistemático, medida por fluctuaciones de brillo superficial (S3).
- La distancia habría que obtenerla por otro método (Cefeidas, SBF).
- 🎯 **Por qué importa:** La galaxia de la línea Hα (C01) está a 43 Mpc, pero ¿qué significa eso comparado con lo que ya conoces? ¿Está más lejos o más cerca que Andrómeda?
- 🔗 **Se estudia junto con:** galaxia, espiral, elíptica, irregular.

📘 **Dónde se aprende** (1 clase): [B01-C15 · Galaxias y agrupaciones cósmicas](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md).

### Distancia por fluctuaciones de brillo superficial

- Una distancia por Cefeidas usa estrellas variables cuya luminosidad se relaciona con su período (S2); una distancia por fluctuaciones de brillo superficial usa la granularidad de la imagen de una galaxia elíptica (S3).

💡 **Cómo se explica en la clase [B01-C15](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md):**
- Para dos objetos concretos hay distancias publicadas con incertidumbre: Andrómeda (M31), 765 kpc con ±28 kpc, medida con estrellas Cefeidas del telescopio espacial Hubble (S2), y el cúmulo de Virgo, 16,5 Mpc con ±0,1 Mpc aleatorio y ±1,1 Mpc sistemático, medida por fluctuaciones de brillo superficial (S3).
- 🎯 **Por qué importa:** La galaxia de la línea Hα (C01) está a 43 Mpc, pero ¿qué significa eso comparado con lo que ya conoces? ¿Está más lejos o más cerca que Andrómeda?
- 🔗 **Se estudia junto con:** galaxia, espiral, elíptica, irregular.

📘 **Dónde se aprende** (1 clase): [B01-C15 · Galaxias y agrupaciones cósmicas](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md).

### Distancia propia

- La distancia propia es la longitud medida con la métrica a lo largo de un camino.

💡 **Cómo se explica en la clase [B26-C07](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md):**
- G --> D["Distancia propia radial<br/>s = ∫ dr / √(1 − r_s/r)"]
- *Descripción textual:* la masa fija `r_s`; el factor `1 − r_s/r` aparece en la métrica; la distancia propia radial integra su raíz inversa y resulta mayor que la diferencia de coordenadas.
- ⚠️ **Error frecuente:** Confundir `r` con la distancia radial propia. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Medir una distancia cerca de una masa grande no da lo mismo que en el espacio plano: el radio de un círculo y su circunferencia dejan de cumplir `C = 2πR`. Los GPS, las lentes gravitacionales y los agujeros negros dependen de esa diferencia.
- 🔗 **Se estudia junto con:** métrica, curvatura gaussiana, exceso angular, métrica de Schwarzschild.

📘 **Dónde se aprende** (1 clase): [B26-C07 · Curvatura y métricas](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md).

### Distancia proyectada

- La distancia proyectada `ρ` es la distancia al núcleo en el plano del cielo.

💡 **Contexto en la clase [B55-C11](../programa/clases/B55/B55-C11-quimica-en-cometas/CLASE.md):**
- **Idea central (modelo mental):** Imagina el gas saliendo del núcleo como agua de una manguera esférica: se diluye como `1/r²`, y mientras viaja el padre se rompe, alimentando al hijo, que a su vez desaparece más lejos.
- 🎯 **Por qué importa:** Un telescopio no ve la densidad en cada punto de la coma sino la columna a lo largo de la línea de visión. Para pasar de lo medido a la producción de moléculas por el núcleo hay que modelar la expansión y la destrucción.
- 🔗 **Se estudia junto con:** modelo de Haser, densidad del padre, del hijo, columna.

📘 **Dónde se aprende** (1 clase): [B55-C11 · Química en cometas](../programa/clases/B55/B55-C11-quimica-en-cometas/CLASE.md).

### Distancia recorrida

- El desplazamiento `Δr = r₂ − r₁` es el cambio de posición, y la distancia recorrida es la longitud del camino, que puede ser mayor.

💡 **Cómo se explica en la clase [B05-C02](../programa/clases/B05/B05-C02-posicion-velocidad-y-aceleracion/CLASE.md):**
- Distinguir desplazamiento de distancia recorrida y rapidez de velocidad.
- ¿Distancia recorrida y módulo del desplazamiento?
- 🎯 **Por qué importa:** Cuando una agencia dice que un satélite «va a 7,7 km/s», ¿respecto de qué y en qué dirección? La pregunta motivadora es: ¿cómo describo un movimiento de forma que otra persona lo reconstruya sin ambigüedad?
- 🔗 **Se estudia junto con:** posición, desplazamiento, velocidad media, velocidad instantánea.

📘 **Dónde se aprende** (1 clase): [B05-C02 · Posición, velocidad y aceleración](../programa/clases/B05/B05-C02-posicion-velocidad-y-aceleracion/CLASE.md).

### Distancia Tierra–Marte

- La distancia Tierra–Marte varía entre un mínimo y un máximo de la ficha de la NASA.

💡 **Cómo se explica en la clase [B113-C03](../programa/clases/B113/B113-C03-comunicacion-diferida-y-soporte-psicologico-a-distancia/CLASE.md):**
- A la mínima distancia Tierra–Marte de la ficha de la NASA (`54,6 × 10⁶ km`), la luz tarda `3,035 min` en ir; a la máxima (`401,4 × 10⁶ km`), `22,315 min`.
- 🎯 **Por qué importa:** Ninguna clase trata el efecto del retardo en el apoyo psicológico. La decisión central: ¿qué formatos de apoyo siguen siendo posibles cuando una respuesta tarda decenas de minutos?
- 🔗 **Se estudia junto con:** retardo de ida, intercambio, conversación en tiempo real, asincrónico.

📘 **Dónde se aprende** (1 clase): [B113-C03 · Comunicación diferida y soporte psicológico a distancia](../programa/clases/B113/B113-C03-comunicacion-diferida-y-soporte-psicologico-a-distancia/CLASE.md).

### Distancia transversal

- La distancia transversal `D_M` coincide con `D_C` si no hay curvatura y es `(c/H₀)sinh(√Ω_k D_C H₀/c)/√Ω_k` si `Ω_k > 0`.

💡 **Contexto en la clase [B26-C19](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md):**
- **Idea central (modelo mental):** Con constante cosmológica el universo se expandió más rápido en el pasado reciente; la luz de una supernova a un `z` dado recorrió más espacio y llega más tenue.
- 🎯 **Por qué importa:** La aceleración cósmica se descubrió porque las supernovas Ia lejanas aparecían más débiles de lo esperado. Para reproducir ese razonamiento hay que saber calcular la distancia de luminosidad y ver cuánto cambia con el contenido del universo.
- 🔗 **Se estudia junto con:** distancia de luminosidad, distancia comóvil, módulo de distancia, modelo de Milne.

📘 **Dónde se aprende** (1 clase): [B26-C19 · Energía oscura y parámetros](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md).

### Distinguible de cero

- Un exceso es distinguible de cero si `ee/σ` supera ~3.

💡 **Cómo se explica en la clase [B55-C17](../programa/clases/B55/B55-C17-compuestos-prebioticos/CLASE.md):**
- Decidir cuándo `ee` es distinguible de cero.
- 🎯 **Por qué importa:** Que un compuesto prebiótico llegue intacto hasta nosotros depende de cuánta radiación recibió, y que un exceso entre dos formas quirales sea real depende de cuántas moléculas se contaron. La decisión central: ¿cuánto sobrevive y con qué incertidumbre puedo afirmar un exceso enantiomérico distinto de cero?
- 🔗 **Se estudia junto con:** radiólisis, dosis característica, exceso enantiomérico, desviación del conteo.

📘 **Dónde se aprende** (1 clase): [B55-C17 · Compuestos prebióticos](../programa/clases/B55/B55-C17-compuestos-prebioticos/CLASE.md).

### Distorsión

- La distorsión es la desviación de la altura de imagen respecto de `f tan θ`.

💡 **Cómo se explica en la clase [B50-C08](../programa/clases/B50/B50-C08-distorsion-geometrica-y-su-calibracion/CLASE.md):**
- En la esquina (15, 15) mm la distorsión desplaza la estrella `0,2578 mm` y el mapa inverso la recupera con error `2,5 × 10⁻¹⁵ mm`.
- Límite: distorsión radial pura, sin descentrado.
- 🎯 **Por qué importa:** En astrometría y en mosaicos una distorsión de 0,1 % mueve las estrellas decenas de píxeles. La decisión central: ¿qué modelo describe la distorsión y con qué precisión se puede calibrar?
- 🔗 **Se estudia junto con:** de barril, de cojín, modelo radial, calibración.

📘 **Dónde se aprende** (1 clase): [B50-C08 · Distorsión geométrica y su calibración](../programa/clases/B50/B50-C08-distorsion-geometrica-y-su-calibracion/CLASE.md).

### Distorsión centrífuga

- La distorsión centrífuga `D` corrige el alargamiento del enlace al girar.

💡 **Cómo se explica en la clase [B62-C01](../programa/clases/B62/B62-C01-espectros-rotacionales-de-moleculas-niveles-y-reglas-de-seleccion/CLASE.md):**
- Incluir la distorsión centrífuga `D` y medir cuánto mejora el acuerdo con el catálogo.
- 🎯 **Por qué importa:** Una línea de CO a 115,27 GHz no es un dato aislado: es la consecuencia de un momento de inercia. Si entiendes de dónde sale, puedes predecir líneas que nadie ha medido y reconocer cuándo una línea observada no es del CO.
- 🔗 **Se estudia junto con:** rotor rígido, número cuántico rotacional, constante rotacional, regla de selección.

📘 **Dónde se aprende** (1 clase): [B62-C01 · Espectros rotacionales de moléculas: niveles y reglas de selección](../programa/clases/B62/B62-C01-espectros-rotacionales-de-moleculas-niveles-y-reglas-de-seleccion/CLASE.md).

### Distorsión centrifugal

- La distorsión centrifugal `D` corrige el estiramiento: `ν = 2 B J − 4 D J³`.

💡 **Cómo se explica en la clase [B55-C09](../programa/clases/B55/B55-C09-espectros-moleculares-de-radio/CLASE.md):**
- Ajustar una constante de distorsión centrifugal con el catálogo.
- 🎯 **Por qué importa:** Las moléculas del espacio frío se detectan casi siempre por sus líneas de rotación en milimétrico y submilimétrico. Para identificar una línea hay que saber de dónde sale su frecuencia, qué fracción de niveles está poblada y cómo corregirla por la velocidad de la nube.
- 🔗 **Se estudia junto con:** rotor rígido, constante rotacional, estructura hiperfina, catálogo JPL.

📘 **Dónde se aprende** (1 clase): [B55-C09 · Espectros moleculares de radio](../programa/clases/B55/B55-C09-espectros-moleculares-de-radio/CLASE.md).

### Distorsión espectral

- La distorsión espectral es el cambio de los colores respecto al original.

💡 **Cómo se explica en la clase [B15-C24](../programa/clases/B15/B15-C24-fusion-de-imagenes-de-distintos-sensores/CLASE.md):**
- Sustitución de componentes (por ejemplo, de intensidad): rápida, con riesgo de distorsión espectral.
- 🎯 **Por qué importa:** Un mapa de cobertura exige distinguir objetos pequeños (caminos, parcelas) y también su firma espectral (si son vegetación o suelo). Ninguna imagen entrega ambas cosas a la vez.
- 🔗 **Se estudia junto con:** fusión, pansharpening, resolución espacial, cobertura espectral.

📘 **Dónde se aprende** (1 clase): [B15-C24 · Fusión de imágenes de distintos sensores](../programa/clases/B15/B15-C24-fusion-de-imagenes-de-distintos-sensores/CLASE.md).

### Distorsión radial

- La distorsión radial multiplica las coordenadas normalizadas por `1 + k1 r² + k2 r⁴`.

💡 **Cómo se explica en la clase [B103-C01](../programa/clases/B103/B103-C01-calibracion-intrinseca-de-camaras/CLASE.md):**
- Una cámara sintética de 1280 × 960 px con `fx = fy = 800 px`, punto principal `(640; 480) px` y distorsión radial `k1 = −0,12`, `k2 = 0,05` mira un tablero de 9 × 6 esquinas con casillas de 25 mm desde 12 poses, con ruido de 0,3 px.
- Proyectar un punto 3D a píxeles con el modelo estenopeico y la distorsión radial `k1`, `k2`.
- 🎯 **Por qué importa:** Un rover que mide una distancia con un error de focal del 1 % comete un error del 1 % en la distancia. La decisión central: ¿cuántas vistas y qué modelo de distorsión hacen falta para que la focal y el punto principal sean fiables, y cómo se comprueba?
- 🔗 **Se estudia junto con:** modelo estenopeico, matriz intrínseca, homografía, error de reproyección.

📘 **Dónde se aprende** (1 clase): [B103-C01 · Calibración intrínseca de cámaras](../programa/clases/B103/B103-C01-calibracion-intrinseca-de-camaras/CLASE.md).

### Distractor diagnóstico

- Un distractor diagnóstico es una opción incorrecta escrita para que la elija quien tiene esa idea.

💡 **Cómo se explica en la clase [B131-C03](../programa/clases/B131/B131-C03-conocimientos-previos-y-concepciones-alternativas/CLASE.md):**
- Límite: elegir un distractor es un indicio, no un diagnóstico de la idea de una persona.
- Diseñar un ítem con distractores diagnósticos y leer sus frecuencias.
- 🎯 **Por qué importa:** Enseñar sin saber qué creen ya los estudiantes deja intactas las ideas previas. La decisión central: ¿qué distractor elegiste para atrapar qué idea, y cómo sabrás si el cambio es real?
- 🔗 **Se estudia junto con:** concepción alternativa, ganancia normalizada, perihelio, afelio.

📘 **Dónde se aprende** (1 clase): [B131-C03 · Conocimientos previos y concepciones alternativas](../programa/clases/B131/B131-C03-conocimientos-previos-y-concepciones-alternativas/CLASE.md).

### Distribución

- Una distribución (S1, C.2.3) es la función que da la probabilidad de cada valor o conjunto de valores de una variable aleatoria.

💡 **Cómo se explica en la clase [B12-C03](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md):**
- La evidencia es la ficha de elección de distribución del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *ficha de elección de distribución*: para tres fenómenos de tu elección (un conteo, una espera, un error de medida), nombra la familia, el parámetro con su unidad, el supuesto físico que la sostiene, una probabilidad calculada y cómo detectarías que el supuesto falla.
- 🎯 **Por qué importa:** Cada vez que un detector cuenta fotones, una nave registra impactos o un instrumento mide con ruido, el patrón de la incertidumbre se parece a uno de unos pocos moldes. Reconocer el molde permite calcular probabilidades sin construir todo desde cero y entender qué supuesto físico lo respalda.
- 🔗 **Se estudia junto con:** parámetro, distribución binomial, distribución de Poisson, distribución exponencial.

📘 **Dónde se aprende** (1 clase): [B12-C03 · Distribuciones de probabilidad](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md).

### Distribución acumulada

- La distribución acumulada `N(>D)` cuenta cráteres mayores que `D`.

💡 **Contexto en la clase [B53-C08](../programa/clases/B53/B53-C08-cartografia-de-crateres/CLASE.md):**
- **Idea central (modelo mental):** Analogía: contar cuántas piedras hay mayores que cada tamaño en un río: si no se ven las pequeñas, la pendiente sale mal.
- 🎯 **Por qué importa:** Un conteo no es un número, es una distribución con incertidumbre. La decisión central: ¿qué estimador de la pendiente es fiable y a partir de qué diámetro el catálogo es completo?
- 🔗 **Se estudia junto con:** pendiente, estimador de Hill, completitud.

📘 **Dónde se aprende** (1 clase): [B53-C08 · Cartografía de cráteres](../programa/clases/B53/B53-C08-cartografia-de-crateres/CLASE.md).

### Distribución binomial

- La distribución binomial da la probabilidad de `m` aciertos entre `N` intentos con probabilidad `p`.
- La distribución binomial `B(n, p)` cuenta éxitos en `n` ensayos independientes con probabilidad `p`: `P(K = k) = C(n,k) pᵏ (1−p)ⁿ⁻ᵏ`.

💡 **Cómo se explica en la clase [B02-C09](../programa/clases/B02/B02-C09-alineaciones-arqueologicas-y-sesgos/CLASE.md):**
- El número de aciertos sigue una distribución binomial: `P(≥ 1) = 1 − (1−p)^N = 0,937`, es decir, casi seguro que al menos una estructura «acierta»;
- 🎯 **Por qué importa:** Con suficientes estructuras, suficientes objetivos celestes y una tolerancia generosa, siempre aparece alguna «alineación». La pregunta motivadora es: ¿cuántas alineaciones esperaríamos si nadie hubiese mirado el cielo?
- 🔗 **Se estudia junto con:** ventana de tolerancia, objetivo, probabilidad por azar, aciertos.

📘 **Dónde se aprende** (2 clases): [B02-C09 · Alineaciones arqueológicas y sesgos](../programa/clases/B02/B02-C09-alineaciones-arqueologicas-y-sesgos/CLASE.md); [B12-C03 · Distribuciones de probabilidad](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md).

### Distribución chi-cuadrado

- La distribución chi-cuadrado con `m` grados de libertad es la de la suma de `m` normales estándar al cuadrado; para datos normales de `m` variables, `d²` la sigue.

💡 **Cómo se explica en la clase [B17-C05](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md):**
- Calcular la distancia de Mahalanobis y su umbral con la distribución chi-cuadrado.
- 🎯 **Por qué importa:** El subsistema térmico de un satélite entrega temperatura y corriente. Cada una, por separado, puede estar dentro de su rango normal y sin embargo la pareja ser imposible: la corriente alta con temperatura baja no ocurre nunca en operación sana.
- 🔗 **Se estudia junto con:** anomalía, distancia de Mahalanobis, bosque de aislamiento, falsa alarma.

📘 **Dónde se aprende** (1 clase): [B17-C05 · Detección de anomalías](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md).

### Distribución de Bose–Einstein

- La distribución de Bose–Einstein, la de Fermi–Dirac y la de Maxwell–Boltzmann.

💡 **Contexto en la clase [B31-C06](../programa/clases/B31/B31-C06-estadisticas-cuanticas/CLASE.md):**
- **Idea central (modelo mental):** Los fermiones son personas que no comparten asiento: ocupan los más bajos hasta llenar el nivel de Fermi. Los bosones se agolpan en el mismo asiento, sobre todo con baja energía.
- 🎯 **Por qué importa:** La radiación de las estrellas y la presión de degeneración de los remanentes estelares dependen de estas estadísticas. La decisión central: ¿qué distribución usar y qué constantes se derivan?
- 🔗 **Se estudia junto con:** Fermi–Dirac, Maxwell–Boltzmann, integral de Planck, energía de Fermi.

📘 **Dónde se aprende** (1 clase): [B31-C06 · Estadísticas cuánticas](../programa/clases/B31/B31-C06-estadisticas-cuanticas/CLASE.md).

### Distribución de coseno

- La distribución de coseno `F ∝ cos φ`.

💡 **Contexto en la clase [B43-C09](../programa/clases/B43/B43-C09-celdas-y-soporte-de-espejos/CLASE.md):**
- **Idea central (modelo mental):** Como una balanza de mercado de tres platos: si el punto de apoyo no está en el centro, un plato carga más que los otros, en proporción directa al desplazamiento.
- 🎯 **Por qué importa:** Una celda que no reparte la carga como se diseñó deforma el espejo. La decisión central: ¿cómo se reparte el peso entre los puntos de apoyo y cuánto cambia si el pivote se desplaza unos milímetros?
- 🔗 **Se estudia junto con:** balanza triangular, pivote, desbalance, soporte lateral.

📘 **Dónde se aprende** (1 clase): [B43-C09 · Celdas y soporte de espejos](../programa/clases/B43/B43-C09-celdas-y-soporte-de-espejos/CLASE.md).

### Distribución de entrenamiento

- La distribución de entrenamiento es la de los datos con que se ajustó el modelo; la de despliegue, la de los datos donde se usa.

💡 **Cómo se explica en la clase [B17-C07](../programa/clases/B17/B17-C07-validacion-fuera-de-distribucion/CLASE.md):**
- Ejercicio 6. Con prevalencia 0,3 y frontera en 0, calcula la función de distribución del despliegue en 0 (`F_desp(0)`) y compárala con la de entrenamiento (0,5).
- Ejercicio 12 · integrador. Redacta el plan de monitoreo de un clasificador desplegado: distribución de entrenamiento y despliegue, detectores (KS y dominio) con umbrales, muestra etiquetada periódica con su tamaño y el intervalo esperado, métricas (exactitud, precisión), y acciones.
- 🎯 **Por qué importa:** Un modelo se entrena con un catálogo y se despliega sobre otro: otro telescopio, otra época, otro brillo límite. Su exactitud medida en validación cruzada deja de valer, y el modelo no avisa: responde con la misma seguridad.
- 🔗 **Se estudia junto con:** despliegue, cambio de covariables, cambio de prevalencia, cambio de concepto.

📘 **Dónde se aprende** (1 clase): [B17-C07 · Validación fuera de distribución](../programa/clases/B17/B17-C07-validacion-fuera-de-distribucion/CLASE.md).

### Distribución de Flory

- La distribución de Flory da la fracción de cadenas de longitud `n`: `(1 − p) pⁿ⁻¹`.

💡 **Contexto en la clase [B56-C21](../programa/clases/B56/B56-C21-polimerizacion-prebiotica-experimental-oligomeros-y-condiciones-de-laboratorio/CLASE.md):**
- **Idea central (modelo mental):** Cada extremo se engancha al siguiente con probabilidad `p`. Las cadenas largas son raras pero existen; al subir `p` el promedio sube muy rápido.
- 🎯 **Por qué importa:** C03 trata el origen de autorreplicantes, pero ninguna clase trata la polimerización experimental y sus límites. Antes de que un replicador pueda copiarse, hay que formar cadenas lo bastante largas.
- 🔗 **Se estudia junto con:** monómero, oligómero, extensión de reacción, ciclo húmedo–seco.

📘 **Dónde se aprende** (1 clase): [B56-C21 · Polimerización prebiótica experimental: oligómeros y condiciones de laboratorio](../programa/clases/B56/B56-C21-polimerizacion-prebiotica-experimental-oligomeros-y-condiciones-de-laboratorio/CLASE.md).

### Distribución de Gumbel

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B33-C03](../programa/clases/B33/B33-C03-eventos-extremos-historicos-de-clima-espacial/CLASE.md):**
- **Idea central (modelo mental):** Como la crecida de cada cien años de un río: con 60 años de registro se estima, pero con incertidumbre.
- 🎯 **Por qué importa:** Las decisiones de protección se basan en periodos de retorno que superan al registro. La decisión central: ¿qué nivel se espera una vez cada T años y cuán incierto es?
- 🔗 **Se estudia junto con:** nivel de retorno, periodo de retorno, máxima verosimilitud, método de momentos.

📘 **Dónde se aprende** (1 clase): [B33-C03 · Eventos extremos históricos de clima espacial](../programa/clases/B33/B33-C03-eventos-extremos-historicos-de-clima-espacial/CLASE.md).

### Distribución de Poisson

- La distribución de Poisson de parámetro `λ` cuenta eventos independientes en un intervalo con tasa constante: `P(N = k) = e^{−λ} λᵏ / k!`.
- La distribución de Poisson da `P(k) = e^(−μ) μ^k/k!`.

💡 **Cómo se explica en la clase [B97-C12](../programa/clases/B97/B97-C12-robots-de-mantenimiento/CLASE.md):**
- Calcular la probabilidad de cubrir las fallas con `s` repuestos con la distribución de Poisson.
- 🎯 **Por qué importa:** Pocos repuestos dejan la misión sin reparación posible; demasiados cargan masa. La confianza del conjunto, no la de cada pieza, es la que importa, y se obtiene con el producto de las probabilidades.
- 🔗 **Se estudia junto con:** tasa de falla, número esperado de fallas, confianza, unidad reemplazable (ORU).

📘 **Dónde se aprende** (2 clases): [B12-C03 · Distribuciones de probabilidad](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md); [B97-C12 · Robots de mantenimiento](../programa/clases/B97/B97-C12-robots-de-mantenimiento/CLASE.md).

### Distribución de Rayleigh

- La distribución de Rayleigh describe el módulo del error en 2D.
- La distribución de Rayleigh describe la magnitud de un error 2D con componentes gaussianas independientes de dispersión `σ`.

💡 **Contexto en la clase [B58-C11](../programa/clases/B58/B58-C11-observaciones-de-seguimiento/CLASE.md):**
- 🎯 **Por qué importa:** Una observación de seguimiento solo sirve si el objeto cae en el campo de la cámara. La decisión central: ¿cuándo y con qué arco conviene volver a observar para no perder el objeto?
- 🔗 **Se estudia junto con:** predicción, arco, campo de visión, seguimiento.

📘 **Dónde se aprende** (2 clases): [B58-C11 · Observaciones de seguimiento](../programa/clases/B58/B58-C11-observaciones-de-seguimiento/CLASE.md); [B92-C02 · Divergencia del haz y pérdidas por apuntamiento óptico](../programa/clases/B92/B92-C02-divergencia-del-haz-y-perdidas-por-apuntamiento-optico/CLASE.md).

### Distribución de velocidades

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B47-C24](../programa/clases/B47/B47-C24-instrumentos-de-plasma-y-campos-in-situ/CLASE.md):**
- **Idea central (modelo mental):** El analizador es una criba que deja pasar solo las partículas de una energía por carga; barriendo la criba se cuenta cuántas hay de cada energía y de ahí se deducen la velocidad media y la dispersión.
- 🎯 **Por qué importa:** La energía por carga elegida por el analizador determina qué se mide; la resolución de los canales limita la temperatura que se recupera. La decisión central: ¿cuántos canales y qué corrección dan la velocidad y la temperatura del plasma con error aceptable?
- 🔗 **Se estudia junto con:** analizador electrostático, energía por carga, copa de Faraday, velocidad térmica.

📘 **Dónde se aprende** (1 clase): [B47-C24 · Instrumentos de plasma y campos in situ](../programa/clases/B47/B47-C24-instrumentos-de-plasma-y-campos-in-situ/CLASE.md).

### Distribución de Weibull

- La distribución de Weibull da `P_f = 1 − exp(−(V/V₀)(σ/σ₀)ᵐ)`;

💡 **Contexto en la clase [B84-C04](../programa/clases/B84/B84-C04-ceramicos-y-polimeros-espaciales/CLASE.md):**
- 🎯 **Por qué importa:** Un metal avisa antes de romper; una cerámica no. Diseñar con la resistencia media de una probeta pequeña sobreestima la de una pieza grande en 40 %.
- 🔗 **Se estudia junto con:** módulo de Weibull, resistencia característica, efecto de tamaño, choque térmico.

📘 **Dónde se aprende** (1 clase): [B84-C04 · Cerámicos y polímeros espaciales](../programa/clases/B84/B84-C04-ceramicos-y-polimeros-espaciales/CLASE.md).

### Distribución estacionaria

- La distribución estacionaria `π` cumple `πP = π`: si el estado se distribuye según `π`, lo sigue haciendo.

💡 **Cómo se explica en la clase [B12-C13](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md):**
- La distribución estacionaria es `π = (q/(p+q), p/(p+q)) = (0,8; 0,2)`.
- Hallar la distribución estacionaria de una cadena finita por tres caminos.
- 🎯 **Por qué importa:** Una posterior de diez o veinte parámetros (órbita, calibración, ruido) no se puede tabular. Pero sí se pueden generar muestras que sigan su forma, aunque no se conozca su normalización.
- 🔗 **Se estudia junto con:** cadena de Markov, matriz de transición, irreducible, aperiódica.

📘 **Dónde se aprende** (1 clase): [B12-C13 · Cadenas de Markov y muestreo](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md).

### Distribución exponencial

- La distribución exponencial de tasa `r` describe el tiempo de espera entre eventos de un proceso de Poisson: densidad `r e^{−rt}` y `P(T > t) = e^{−rt}`.
- Profundidad de descarga (DoD): fracción usable de la batería. Distribución exponencial: duración sin memoria.

💡 **Cómo se explica en la clase [B48-C07](../programa/clases/B48/B48-C07-seguridad-en-instalaciones-remotas/CLASE.md):**
- La exponencial subestima las colas: se necesita otra distribución.
- 🎯 **Por qué importa:** Un respaldo mal dimensionado deja la cúpula abierta con lluvia. La decisión central: ¿qué autonomía cubre la mayoría de los cortes?
- 🔗 **Se estudia junto con:** Autonomía, Profundidad de descarga, Proceso de Poisson, Carga crítica.

📘 **Dónde se aprende** (2 clases): [B12-C03 · Distribuciones de probabilidad](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md); [B48-C07 · Seguridad en instalaciones remotas](../programa/clases/B48/B48-C07-seguridad-en-instalaciones-remotas/CLASE.md).

### Distribución fuente

- Una rueda (*wheel*) es un paquete ya compilado para una plataforma; una distribución fuente (*sdist*) es el código sin compilar.

💡 **Cómo se explica en la clase [B14-C12](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md):**
- Hay una por cada archivo descargable: la distribución fuente y una rueda por plataforma, versión de Python y arquitectura.
- 🎯 **Por qué importa:** Tu análisis dio un período de 5553,624562 s en 2026. Un colega lo ejecuta con otra versión de SciPy y obtiene un cierre distinto; otro usa Python más antiguo y falla al importar. «En mi máquina funciona» no es un resultado científico.
- 🔗 **Se estudia junto con:** proyecto, resolutor, archivo de bloqueo, bloqueo universal.

📘 **Dónde se aprende** (1 clase): [B14-C12 · Ejecución reproducible con uv](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md).

### Distribución kappa

- La distribución kappa tiene una cola de ley de potencias y se acerca a la maxwelliana si `κ → ∞`.

💡 **Cómo se explica en la clase [B35-C01](../programa/clases/B35/B35-C01-funciones-de-distribucion-de-velocidades-en-plasmas/CLASE.md):**
- Con una distribución kappa de igual `T` cinética, la densidad de probabilidad a `5 v_t` es `46,3` veces la maxwelliana si `κ = 5`.
- Definir la distribución kappa con temperatura cinética `T`.
- 🎯 **Por qué importa:** Los instrumentos miden distribuciones, y casi todas las fórmulas de fluido son momentos de ellas. La decisión central: ¿basta una maxwelliana o hay que conservar la cola?
- 🔗 **Se estudia junto con:** función de distribución, maxwelliana, momento, rapidez térmica.

📘 **Dónde se aprende** (1 clase): [B35-C01 · Funciones de distribución de velocidades en plasmas](../programa/clases/B35/B35-C01-funciones-de-distribucion-de-velocidades-en-plasmas/CLASE.md).

### Distribución normal

- La distribución normal (o de Laplace–Gauss, S1, C.2.14;

💡 **Contexto en la clase [B12-C03](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md):**
- **Idea central (modelo mental):** La familia no se elige por su forma, sino por el mecanismo que genera el dato.
- 🎯 **Por qué importa:** Cada vez que un detector cuenta fotones, una nave registra impactos o un instrumento mide con ruido, el patrón de la incertidumbre se parece a uno de unos pocos moldes. Reconocer el molde permite calcular probabilidades sin construir todo desde cero y entender qué supuesto físico lo respalda.
- 🔗 **Se estudia junto con:** distribución, parámetro, distribución binomial, distribución de Poisson.

📘 **Dónde se aprende** (1 clase): [B12-C03 · Distribuciones de probabilidad](../programa/clases/B12/B12-C03-distribuciones-de-probabilidad/CLASE.md).

### Distribución predictiva posterior

- La distribución predictiva posterior de un dato nuevo `ỹ` es `p(ỹ | y) = ∫ p(ỹ | θ) p(θ | y) dθ`: promedia la predicción para cada valor del parámetro, ponderada por su posterior.

💡 **Cómo se explica en la clase [B19-C06](../programa/clases/B19/B19-C06-distribucion-predictiva-posterior/CLASE.md):**
- Escribir la distribución predictiva posterior como una integral sobre la posterior.
- python programa/clases/B19/B19-C06-distribucion-predictiva-posterior/predictiva_posterior.py
- 🎯 **Por qué importa:** El contador de partículas lleva 12 horas midiendo. Con la posterior de la tasa `λ`, la pregunta práctica es: ¿cuántos eventos esperar en la hora 13, y qué tan sorprendente sería ver 8?
- 🔗 **Se estudia junto con:** réplica, predictiva a priori, estadístico de chequeo, valor p predictivo posterior.

📘 **Dónde se aprende** (1 clase): [B19-C06 · Distribución predictiva posterior](../programa/clases/B19/B19-C06-distribucion-predictiva-posterior/CLASE.md).

### Distribución t de Student

- La distribución `t` de Student con `ν` grados de libertad es la distribución de `(x̄ − μ)/(s/√n)` cuando los datos son normales y `ν = n − 1` (S1, G.3.2 y C.3.8).
- La distribución t de Student describe la media estandarizada con `s` estimada.

💡 **Contexto en la clase [B12-C08](../programa/clases/B12/B12-C08-intervalos-de-confianza/CLASE.md):**
- **Idea central (modelo mental):** Cada muestra produce una red (un intervalo) que se lanza para atrapar un pez (el parámetro) que no se mueve. Un procedimiento del 95 % es uno cuyas redes atrapan el pez en 95 de cada 100 lanzamientos. Una vez lanzada una red, el pez está o no está dentro; la probabilidad del 95 % describe el procedimiento, no ese intervalo concreto.
- 🎯 **Por qué importa:** Un número sin rango es una afirmación sin evidencia de su precisión. «La distancia es 148,5 m» no dice si el valor es fiable al metro o al decámetro. Un intervalo con su nivel de confianza lo dice, y permite decidir si una medición cumple un requisito o si hay que tomar más datos.
- 🔗 **Se estudia junto con:** intervalo de confianza, nivel de confianza, semiancho, cobertura.

📘 **Dónde se aprende** (2 clases): [B12-C08 · Intervalos de confianza](../programa/clases/B12/B12-C08-intervalos-de-confianza/CLASE.md); [B13-C12 · Incertidumbre expandida](../programa/clases/B13/B13-C12-incertidumbre-expandida/CLASE.md).

### Distribución tamaño-frecuencia

- La distribución tamaño-frecuencia acumulada `N(>D)` cuenta las rocas mayores que `D`.

💡 **Contexto en la clase [B103-C06](../programa/clases/B103/B103-C06-deteccion-y-catalogacion-de-rocas-en-imagenes-de-superficie/CLASE.md):**
- 🎯 **Por qué importa:** Un catálogo de rocas es incompleto justo donde hay más rocas: las pequeñas. Ajustar una ley de potencias con todas las detecciones da un exponente sesgado.
- 🔗 **Se estudia junto con:** diámetro equivalente, tamaño mínimo de completitud, máxima verosimilitud, bootstrap.

📘 **Dónde se aprende** (1 clase): [B103-C06 · Detección y catalogación de rocas en imágenes de superficie](../programa/clases/B103/B103-C06-deteccion-y-catalogacion-de-rocas-en-imagenes-de-superficie/CLASE.md).

### Distribución triangular

- La distribución triangular `(a, m, b)` tiene mínimo `a`, moda `m` y máximo `b`.

💡 **Cómo se explica en la clase [B108-C05](../programa/clases/B108/B108-C05-evaluacion-de-secuencias-y-lineas-de-tiempo-de-eva/CLASE.md):**
- Modelar duraciones con una distribución triangular.
- 🎯 **Por qué importa:** Falta evaluar la secuencia de una EVA (tiempos, consumibles, márgenes) antes de ejecutarla. La decisión central: ¿cabe la secuencia en el tiempo y en los consumibles disponibles, con qué probabilidad y con qué margen?
- 🔗 **Se estudia junto con:** red de precedencias, holgura, Monte Carlo, margen.

📘 **Dónde se aprende** (1 clase): [B108-C05 · Evaluación de secuencias y líneas de tiempo de EVA](../programa/clases/B108/B108-C05-evaluacion-de-secuencias-y-lineas-de-tiempo-de-eva/CLASE.md).

### Distribución χ²

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B40-C15](../programa/clases/B40/B40-C15-varianza-cosmica-y-limites-de-las-mediciones-del-fondo/CLASE.md):**
- **Idea central (modelo mental):** Como estimar la media de un dado lanzándolo pocas veces: con `2ℓ + 1` lanzamientos la estimación fluctúa por azar, por buena que sea la balanza.
- 🎯 **Por qué importa:** La varianza cósmica es el límite fundamental de la medición del fondo. La decisión central: ¿qué precisión máxima permite el número de modos disponibles?
- 🔗 **Se estudia junto con:** varianza cósmica, grados de libertad, precisión de una amplitud, percentil.

📘 **Dónde se aprende** (1 clase): [B40-C15 · Varianza cósmica y límites de las mediciones del fondo](../programa/clases/B40/B40-C15-varianza-cosmica-y-limites-de-las-mediciones-del-fondo/CLASE.md).

### DITL

- Fit check: ajuste con el dispensador. DITL: prueba de «día en la vida».

💡 **Cómo se explica en la clase [B90-C20](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md):**
- *CubeSat 101* (F7) añade la prueba DITL, el mínimo contenido de los informes (procedimientos con marcas de tiempo, fotos, gráficas, prueba de que la unidad sobrevivió) y que el integrador debe aprobar el procedimiento antes de la prueba.
- *Descripción textual:* los ensayos se encadenan de la inspección al DITL; cada uno puede fallar y entonces se hace retrabajo y se repite el mismo ensayo antes de pasar al siguiente.
- 🎯 **Por qué importa:** Un calendario de ensayos sin contingencia casi nunca se cumple: cada falla suma retrabajo y repetición. La decisión central: ¿cuánto tiempo reservar para terminar con una confianza dada?
- 🔗 **Se estudia junto con:** Campaña de calificación, Flujo de ensayos, Fit check, Contingencia.

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
- 🔗 **Se estudia junto con:** campo vectorial, rotacional, integral de línea, conservativo.

📘 **Dónde se aprende** (4 clases): [B09-C19 · Cálculo vectorial introductorio](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md); [B19-C04 · Diagnóstico de convergencia de cadenas](../programa/clases/B19/B19-C04-diagnostico-de-convergencia-de-cadenas/CLASE.md); [B77-C17 · Estabilidad durante descenso](../programa/clases/B77/B77-C17-estabilidad-durante-descenso/CLASE.md); [B92-C02 · Divergencia del haz y pérdidas por apuntamiento óptico](../programa/clases/B92/B92-C02-divergencia-del-haz-y-perdidas-por-apuntamiento-optico/CLASE.md).

### Divergencia cero

- Un campo cuyo gradiente tiene traza nula es de divergencia cero (la divergencia es la traza de su gradiente).

💡 **Cómo se explica en la clase [B10-C18](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md):**
- La divergencia del campo es cero: al primer orden el volumen no cambia; se estira en una dirección y se comprime en las otras (8.3).
- 🎯 **Por qué importa:** La gravedad no es uniforme a lo largo de un satélite: lo que está más cerca de la Tierra se acelera más que lo que está lejos, y lo que está a los lados se comprime. Con una sola derivada `dg/dr` solo describes la dirección radial; el tensor de marea describe las tres direcciones a la vez.
- 🔗 **Se estudia junto con:** producto tensorial, rango 1, contracción, traza.

📘 **Dónde se aprende** (1 clase): [B10-C18 · Producto tensorial y contracción](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md).

### Divergencia de Kullback–Leibler

- La divergencia de Kullback–Leibler de `q` respecto de `p` es `KL(q ‖ p) = E_q[log q(θ) − log p(θ)]`; es ≥ 0 y vale 0 solo si `q = p`.

💡 **Cómo se explica en la clase [B19-C05](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md):**
- Blei, Kucukelbir y McAuliffe (fuente S1) presentan la inferencia variacional como un método de aprendizaje automático que aproxima densidades difíciles, como las posteriores bayesianas, mediante optimización: se escoge una familia de densidades y se busca el miembro más cercano al objetivo en divergencia de Kullback–Leibler.
- 🎯 **Por qué importa:** Con miles de parámetros o millones de datos, un muestreador puede tardar horas o días. La inferencia variacional (VI) elige una familia de distribuciones manejables, por ejemplo gaussianas, y busca dentro de ella la más cercana a la posterior.
- 🔗 **Se estudia junto con:** familia variacional, aproximación variacional, ELBO, campo medio.

📘 **Dónde se aprende** (1 clase): [B19-C05 · Inferencia variacional](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md).

### Divergencia logarítmica

- La divergencia logarítmica es el crecimiento de `t` como `ln(1/δ)` al acercarse a `r_s(1 + δ)`.

💡 **Contexto en la clase [B27-C08](../programa/clases/B27/B27-C08-horizonte-de-sucesos/CLASE.md):**
- **Idea central (modelo mental):** Quien cae lleva un reloj que marca un tiempo finito hasta el centro. El observador lejano ve las señales llegar cada vez más espaciadas: el reloj de quien cae parece detenerse al acercarse al horizonte.
- 🎯 **Por qué importa:** Para quien cae, el horizonte se cruza en un tiempo finito y, en un agujero grande, sin marea notable; para quien observa desde lejos, la caída parece no terminar. La decisión central: ¿cuánto dura la caída en cada reloj y qué marea se siente en el horizonte?
- 🔗 **Se estudia junto con:** tiempo propio, tiempo coordenado, caída libre radial, aceleración de marea.

📘 **Dónde se aprende** (1 clase): [B27-C08 · Horizonte de sucesos](../programa/clases/B27/B27-C08-horizonte-de-sucesos/CLASE.md).

### Diversidad

- La diversidad cuenta valores distintos del atributo sensible por grupo.

💡 **Cómo se explica en la clase [B124-C13](../programa/clases/B124/B124-C13-etica-de-investigacion-y-datos/CLASE.md):**
- Dentro de un grupo de `k` personas puede haber un solo valor del atributo sensible: la diversidad mínima de ingresos es `2`.
- Por diversidad: valores sensibles distintos por grupo.
- 🎯 **Por qué importa:** Abrir datos sin proteger a las personas es un daño, y proteger sin medir es una promesa vacía. La decisión central: ¿cuánto generalizar los datos para que ninguna persona sea identificable y cuánta información se pierde?
- 🔗 **Se estudia junto con:** k-anonimato, generalización, supresión, reticulado.

📘 **Dónde se aprende** (1 clase): [B124-C13 · Ética de investigación y datos](../programa/clases/B124/B124-C13-etica-de-investigacion-y-datos/CLASE.md).

### Diversidad de estaciones

- La diversidad de estaciones usa varias estaciones terrestres separadas para que no estén cubiertas a la vez.

💡 **Contexto en la clase [B92-C04](../programa/clases/B92/B92-C04-atmosfera-y-nubes-en-enlaces-opticos-con-la-tierra/CLASE.md):**
- 🎯 **Por qué importa:** Un enlace espacial es perfecto hasta que llega a las últimas decenas de kilómetros. La decisión central: ¿cuánto margen exige la turbulencia y cuántas estaciones exige la nubosidad para cumplir una disponibilidad?
- 🔗 **Se estudia junto con:** constante de estructura, parámetro de Fried, varianza de Rytov, desvanecimiento.

📘 **Dónde se aprende** (1 clase): [B92-C04 · Atmósfera y nubes en enlaces ópticos con la Tierra](../programa/clases/B92/B92-C04-atmosfera-y-nubes-en-enlaces-opticos-con-la-tierra/CLASE.md).

### Dividendo

- El dividendo es lo que se divide y el divisor entre lo que se divide.

💡 **Contexto en la clase [B03-C01](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md):**
- **Idea central (modelo mental):** Piensa en una expresión como una receta con pasos ordenados. Algunos pasos «pesan más» y se hacen antes. ```mermaid flowchart TD A["Expresión escrita"] --> B["1.
- 🎯 **Por qué importa:** Una agencia espacial no «confía» en un cálculo: lo comprueba. Para saber cuánto tarda la Luna en dar una vuelta alrededor de la Tierra basta multiplicar, dividir y respetar el orden de las operaciones; pero un paréntesis mal puesto convierte 27 días en una cifra absurda.
- 🔗 **Se estudia junto con:** número natural, entero, número racional, número irracional.

📘 **Dónde se aprende** (1 clase): [B03-C01 · Números y operaciones fundamentales](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md).

### Divisor

- El dividendo es lo que se divide y el divisor entre lo que se divide.
- El divisor entrega `V = V_ref R/(R + R_f)`.
- El divisor de UART `d = f/(16·baud)`.

💡 **Cómo se explica en la clase [B03-C01](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md):**
- Sumar y restar decimales exige alinear la coma; multiplicar, contar las cifras decimales del resultado (la suma de las de los factores); dividir, convertir si hace falta el divisor en entero desplazando la coma en ambos.
- ⚠️ **Error frecuente:** Olvidar paréntesis en el divisor. Se detecta por resultados absurdos.
- 🎯 **Por qué importa:** Una agencia espacial no «confía» en un cálculo: lo comprueba. Para saber cuánto tarda la Luna en dar una vuelta alrededor de la Tierra basta multiplicar, dividir y respetar el orden de las operaciones; pero un paréntesis mal puesto convierte 27 días en una cifra absurda.
- 🔗 **Se estudia junto con:** número natural, entero, número racional, número irracional.

📘 **Dónde se aprende** (3 clases): [B03-C01 · Números y operaciones fundamentales](../programa/clases/B03/B03-C01-numeros-y-operaciones-fundamentales/CLASE.md); [B85-C25 · Sensores y telemetría térmica](../programa/clases/B85/B85-C25-sensores-y-telemetria-termica/CLASE.md); [B88-C02 · Microcontroladores embarcados](../programa/clases/B88/B88-C02-microcontroladores-embarcados/CLASE.md).

### Divulgación

- Una fuente primaria es un documento de la propia misión o agencia; una de divulgación resume a otras.

💡 **Cómo se explica en la clase [B104-C01](../programa/clases/B104/B104-C01-historia-de-vuelos-tripulados/CLASE.md):**
- Reconocer la diferencia entre fuentes primarias, institucionales y de divulgación.
- 🎯 **Por qué importa:** Los hitos del vuelo tripulado se citan de memoria y circulan con cifras que difieren entre fuentes (una altitud mínima de 169 km o de 181 km para el primer vuelo orbital). La decisión central: ¿qué cifra histórica puedes usar sin riesgo y cuál debes rotular como no consultada?
- 🔗 **Se estudia junto con:** periodo, semieje mayor, vis-viva, cronología.

📘 **Dónde se aprende** (1 clase): [B104-C01 · Historia de vuelos tripulados](../programa/clases/B104/B104-C01-historia-de-vuelos-tripulados/CLASE.md).

### DLI

- PPFD: flujo de fotones útiles. DLI: mol de fotones por m² y día.

💡 **Cómo se explica en la clase [B106-C12](../programa/clases/B106/B106-C12-agricultura-en-ambiente-controlado/CLASE.md):**
- Paso 1. DLI: `300·10⁻⁶·16·3600 = 17,28 mol/(m² día)`.
- Con 300 µmol/(m² s) durante 16 h, la DLI es 17,28 mol/(m² día) y las lámparas consumen 80 W/m² en promedio.
- 🎯 **Por qué importa:** Cultivar reduce la masa de alimento a lanzar y devuelve oxígeno, pero cuesta mucha área y electricidad. La decisión central: ¿qué fracción de la dieta compensa cultivar dado el costo en área y energía?
- 🔗 **Se estudia junto con:** PPFD, Eficacia de la lámpara, Eficiencia de uso de la luz, Fracción comestible.

📘 **Dónde se aprende** (1 clase): [B106-C12 · Agricultura en ambiente controlado](../programa/clases/B106/B106-C12-agricultura-en-ambiente-controlado/CLASE.md).

### Doble

- El doble reproduce las salidas.

💡 **Cómo se explica en la clase [B88-C42](../programa/clases/B88/B88-C42-simuladores-y-mocks-de-sensores-para-pruebas/CLASE.md):**
- Analogía: un doble de sensor es un actor que imita al sensor y puede «enfermarse» cuando se le pide.
- Verificar las propiedades estadísticas del doble.
- ⚠️ **Error frecuente:** Presentar el doble como un sensor real. Revisa la sección 10
- 🎯 **Por qué importa:** Para probar el FDIR hace falta provocar fallos que el sensor real no da a pedido. La decisión central: ¿qué características del sensor debe reproducir el doble para que la prueba sea válida?
- 🔗 **Se estudia junto con:** atasco, pérdida de dato, desviación de Allan.

📘 **Dónde se aprende** (1 clase): [B88-C42 · Simuladores y mocks de sensores para pruebas](../programa/clases/B88/B88-C42-simuladores-y-mocks-de-sensores-para-pruebas/CLASE.md).

### Doble búfer

- El doble búfer alterna entre dos ranuras.

💡 **Cómo se explica en la clase [B88-C35](../programa/clases/B88/B88-C35-reinicio-en-caliente-y-persistencia-de-estado/CLASE.md):**
- El laboratorio prueba el doble búfer y la ranura única.
- Descripción larga: el doble búfer garantiza un estado válido en todos los cortes probados; la ranura única, no.
- 🎯 **Por qué importa:** Un corte durante una escritura deja un registro a medias. La decisión central: ¿qué esquema garantiza que, cortes donde cortes, siempre haya un estado válido recuperable?
- 🔗 **Se estudia junto con:** secuencia, CRC-16, recuperación, corte de energía.

📘 **Dónde se aprende** (1 clase): [B88-C35 · Reinicio en caliente y persistencia de estado](../programa/clases/B88/B88-C35-reinicio-en-caliente-y-persistencia-de-estado/CLASE.md).

### Doble cobertura

- La doble cobertura significa que `q` y `−q` representan la misma rotación (S1).
- La doble cobertura dice que `q` y `−q` son la misma actitud.

💡 **Cómo se explica en la clase [B87-C02](../programa/clases/B87/B87-C02-representaciones-de-orientacion/CLASE.md):**
- Explicar la doble cobertura (`q` y `−q`) y la singularidad de los ángulos de Euler (bloqueo de cardán).
- La misma `R`: doble cobertura; las dos dan la misma matriz (el laboratorio mide `0,0e+00` de diferencia).
- 🎯 **Por qué importa:** Casi todos los errores de actitud en software vienen de convenciones mezcladas: orden de ejes, sentido de la rotación, posición de la parte escalar. La decisión central: ¿qué representación uso para integrar, cuál para filtrar y cuál para mostrar?
- 🔗 **Se estudia junto con:** matriz de actitud, ángulos de Euler 3-2-1, cuaternión, eje-ángulo.

📘 **Dónde se aprende** (2 clases): [B10-C15 · Cuaterniones unitarios](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md); [B87-C02 · Representaciones de orientación](../programa/clases/B87/B87-C02-representaciones-de-orientacion/CLASE.md).

### Doble precisión

- Un número en doble precisión (IEEE 754 *binary64*) tiene 1 bit de signo, 11 de exponente y 52 de mantisa (53 cifras binarias efectivas), es decir, unas 15 a 17 cifras decimales; la documentación de Python confirma los 53 bits de precisión (S1).

💡 **Cómo se explica en la clase [B11-C25](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md):**
- En doble precisión, `cos(10⁻⁸)` se redondea a `1` exactamente y la resta ingenua da `0`: error relativo del 100 %.
- Equivalente accesible a una tabla de efectos (cálculo, doble precisión):
- ⚠️ **Error frecuente:** Creer que la doble precisión elimina el redondeo. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Un programa de ciencias espaciales hace miles de millones de operaciones. Si una resta pierde 16 cifras en una sola operación, el resultado completo es basura sin que el programa se detenga.
- 🔗 **Se estudia junto con:** épsilon de máquina, ulp, redondeo al más cercano, cancelación catastrófica.

📘 **Dónde se aprende** (1 clase): [B11-C25 · Aritmética de punto flotante y errores de redondeo](../programa/clases/B11/B11-C25-aritmetica-de-punto-flotante-y-errores-de-redondeo/CLASE.md).

### Doble rendija

- La doble rendija produce franjas de espaciado `λL/d`.
- La doble rendija de separación `d`.

💡 **Cómo se explica en la clase [B31-C01](../programa/clases/B31/B31-C01-dualidad-onda-particula/CLASE.md):**
- El montaje de doble rendija (electrones de 50 keV, `d = 1 µm`, `L = 1 m`) es ilustrativo.
- El script [dualidad.py](dualidad.py) calcula `λ` para varios objetos y recupera el espaciado de franjas de un experimento de doble rendija simulado (comprueba `λ√T` a `10⁻¹²` y el espaciado al 1,5 %).
- 🎯 **Por qué importa:** Sin la dualidad no se entiende la difracción de electrones, los microscopios electrónicos ni la estructura atómica. La decisión central: ¿cuándo importa la longitud de onda de un objeto y cómo se ve en un experimento?
- 🔗 **Se estudia junto con:** longitud de onda de de Broglie, envolvente, impacto, coherencia.

📘 **Dónde se aprende** (2 clases): [B31-C01 · Dualidad onda-partícula](../programa/clases/B31/B31-C01-dualidad-onda-particula/CLASE.md); [B42-C04 · Difracción de aperturas](../programa/clases/B42/B42-C04-difraccion-de-aperturas/CLASE.md).

### Doble uso

- Doble uso es el que sirve a fines civiles y militares.
- Un artículo de doble uso sirve para fines civiles y militares.

💡 **Cómo se explica en la clase [B119-C17](../programa/clases/B119/B119-C17-conflictos-y-normas-humanitarias-aplicables/CLASE.md):**
- El ejemplo conductor: 100 000 objetos sintéticos de doble uso (10 % militares) con un indicador observable gaussiano (civil media 0, militar media 2) y costes ilustrativos de error 10 y 1.
- 🎯 **Por qué importa:** C11 trata los límites militares del tratado; esta clase aborda cómo razonar la distinción bajo incertidumbre, un tema que ninguna clase del bloque cubre y que exige cautela jurídica. La decisión central: ¿cómo cambia el umbral de decisión cuando equivocarse en un sentido es mucho más grave que en el otro?
- 🔗 **Se estudia junto con:** umbral, falso positivo, presunción protectora, coste asimétrico.

📘 **Dónde se aprende** (2 clases): [B119-C17 · Conflictos y normas humanitarias aplicables](../programa/clases/B119/B119-C17-conflictos-y-normas-humanitarias-aplicables/CLASE.md); [B125-C05 · Control de exportaciones y transferencia de tecnología](../programa/clases/B125/B125-C05-control-de-exportaciones-y-transferencia-de-tecnologia/CLASE.md).

### Doblete acromático

- El doblete acromático anula el cromatismo primario.

💡 **Cómo se explica en la clase [B41-C15](../programa/clases/B41/B41-C15-refractores-acromaticos-y-apocromaticos/CLASE.md):**
- El script [acromatico.py](acromatico.py) resuelve doblete y triplete por sistema lineal y mide el desenfoque en el espectro (comprueba `P₁` a 2 % de la fórmula y focales iguales en F y C a `10⁻⁶`).
- 🎯 **Por qué importa:** Un refractor sin color necesita combinar vidrios. La decisión central: ¿cuánto color queda con dos o tres vidrios?
- 🔗 **Se estudia junto con:** espectro secundario, triplete apocromático, potencia, factor de forma.

📘 **Dónde se aprende** (2 clases): [B41-C15 · Refractores acromáticos y apocromáticos](../programa/clases/B41/B41-C15-refractores-acromaticos-y-apocromaticos/CLASE.md); [B43-C21 · Selección de vidrios ópticos: catálogos, homogeneidad y diagramas](../programa/clases/B43/B43-C21-seleccion-de-vidrios-opticos-catalogos-homogeneidad-y-diagramas/CLASE.md).

### Dobson

- Un refractor reúne la luz con lentes; un reflector usa espejos y puede necesitar ajustar sus espejos (*colimación*); un Dobson es un reflector sobre una montura simple (S3).

💡 **Cómo se explica en la clase [B08-C14](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md):**
- Según Night Sky Network (S3): los refractores usan lentes, necesitan poco mantenimiento y suelen ser más grandes y caros que un reflector de potencia similar; los reflectores usan espejos y pueden requerir colimación; los Dobson son reflectores sobre una montura sencilla, fáciles de sacar y usar, una elección común de principiantes.
- Con el Dobson de 200 mm y F = 1200 mm: `N = 1200/200 = 6`.
- 🎯 **Por qué importa:** Un telescopio de juguete anuncia «600×» y decepciona. La pregunta motivadora: ¿qué telescopio me conviene y qué podré ver con él?
- 🔗 **Se estudia junto con:** refractor, reflector, apertura, distancia focal.

📘 **Dónde se aprende** (1 clase): [B08-C14 · Telescopios de iniciación](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md).

### Dockerfile

- Un Dockerfile es el texto con las instrucciones para construirla (`FROM`, `COPY`, `RUN`, `WORKDIR`, `USER`, `CMD`).

💡 **Cómo se explica en la clase [B14-C17](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md):**
- El Dockerfile descuidado (`FROM python:latest`, `COPY . /app`, `RUN pip install numpy scipy`, `CMD python …`) incumple las seis: 6 hallazgos.
- Con la huella encadenada del laboratorio, el Dockerfile revisado tiene 7 instrucciones.
- 🎯 **Por qué importa:** Tu análisis funciona con el bloqueo de C12 en tu equipo, pero en el servidor del laboratorio falla porque falta una biblioteca del sistema. La pregunta motivadora es: ¿cómo entrego el análisis junto con todo lo que necesita para correr, de modo que otra persona lo ejecute igual?
- 🔗 **Se estudia junto con:** imagen, contenedor, capa, caché de capas.

📘 **Dónde se aprende** (1 clase): [B14-C17 · Contenedores y ambientes científicos](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md).

### Docstring

- Una docstring es la cadena al inicio de un módulo, clase o función que lo describe; la primera línea es un resumen corto, y el resto explica argumentos, valores devueltos, efectos y excepciones (S2).
- Una docstring documenta un módulo, función o clase (S4).

💡 **Cómo se explica en la clase [B07-C06](../programa/clases/B07/B07-C06-funciones-y-modularidad/CLASE.md):**
- La docstring es lo que ve quien llame `help(razon_kepler)`.
- Escribir docstrings y separar un módulo reutilizable de un script que lo usa.
- 🎯 **Por qué importa:** Copiar y pegar el mismo cálculo en cinco sitios es la forma más rápida de tener cinco versiones distintas y un error corregido solo en una. Una función concentra la lógica en un lugar, le da un nombre que expresa su intención y permite probarla aislada.
- 🔗 **Se estudia junto con:** función, parámetro, argumento, valor devuelto.

📘 **Dónde se aprende** (2 clases): [B07-C06 · Funciones y modularidad](../programa/clases/B07/B07-C06-funciones-y-modularidad/CLASE.md); [B07-C19 · Documentación y reproducibilidad](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md).

### Doctrina declarada

- Una doctrina declarada es una posición publicada.

💡 **Cómo se explica en la clase [B119-C26](../programa/clases/B119/B119-C26-doctrinas-y-politicas-espaciales-declaradas-publicamente/CLASE.md):**
- XI (informar en la mayor medida posible), un marco contra el que puede leerse una doctrina declarada.
- python programa/clases/B119/B119-C26-doctrinas-y-politicas-espaciales-declaradas-publicamente/laboratorio.py
- 🎯 **Por qué importa:** C11 y C12 tratan los límites militares y la historia; ninguna clase enseña a leer doctrinas públicas con rigor. La lectura real de documentos oficiales exige fuentes que no se consultaron aquí.
- 🔗 **Se estudia junto con:** codificador, acuerdo observado, acuerdo por azar, kappa.

📘 **Dónde se aprende** (1 clase): [B119-C26 · Doctrinas y políticas espaciales declaradas públicamente](../programa/clases/B119/B119-C26-doctrinas-y-politicas-espaciales-declaradas-publicamente/CLASE.md).

### Documentar

- Documentar es escribir lo necesario para entender y usar el código y los datos.

💡 **Cómo se explica en la clase [B07-C19](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md):**
- Documentar no es un adorno: se puede comprobar de forma automática, aunque que exista no garantiza que sea buena.
- 🎯 **Por qué importa:** Un resultado que solo su autor puede obtener, y solo el día en que lo obtuvo, es una anécdota. Cuando pasan seis meses, no sabrás con qué datos, con qué versión ni con qué semilla lo generaste.
- 🔗 **Se estudia junto con:** docstring, README, semilla, huella.

📘 **Dónde se aprende** (1 clase): [B07-C19 · Documentación y reproducibilidad](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md).

### DoD

- El DoD es la fracción descargada.
- SOC: estado de carga. DoD: profundidad de descarga.

💡 **Cómo se explica en la clase [B86-C05](../programa/clases/B86/B86-C05-baterias-de-ion-litio/CLASE.md):**
- Con la ley ilustrativa `N = 3000 (0,8/DoD)^1,6`, el DoD que da esa vida es `0,8 (3000/N)^(1/1,6) = 20,15 %` en forma cerrada y por bisección `0,201501` en fracción (diferencia `0,0e+00`).
- La descarga a potencia constante con `OCV = 3,3 + 0,8 s` por celda y `0,05 Ω` por celda da un DoD de `13,95 %` frente al planificado de `15,54 %`: diferencia relativa de `10,20 %`.
- ⚠️ **Error frecuente:** Dimensionar con DoD de `100 %`. Se corrige con 8.1.
- 🎯 **Por qué importa:** Una batería de órbita baja hace unos `5400` ciclos al año. Dimensionarla por la energía de un solo eclipse sin mirar la profundidad de descarga la agota mucho antes del fin de la misión.
- 🔗 **Se estudia junto con:** capacidad, energía, estado de carga, tensión de circuito abierto.

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
- 🔗 **Se estudia junto con:** frente de Pareto, hipervolumen, rodilla.

📘 **Dónde se aprende** (4 clases): [B67-C01 · Selección de sitios de extracción con criterios múltiples](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md); [B81-C11 · Optimización multicriterio y frentes de Pareto](../programa/clases/B81/B81-C11-optimizacion-multicriterio-y-frentes-de-pareto/CLASE.md); [B91-C06 · Selección y compromiso de diseño de antenas](../programa/clases/B91/B91-C06-seleccion-y-compromiso-de-diseno-de-antenas/CLASE.md); [B124-C12 · Evaluación de retorno científico](../programa/clases/B124/B124-C12-evaluacion-de-retorno-cientifico/CLASE.md).

### Dominancia

- La dominancia ocurre cuando otra opción es igual o mejor en todos los criterios y estrictamente mejor en uno.
- Una dominancia ocurre cuando una alternativa gana en todos los criterios.

💡 **Cómo se explica en la clase [B78-C20](../programa/clases/B78/B78-C20-comparacion-no-operativa-de-arquitecturas-de-propulsion/CLASE.md):**
- Las dominancias cambiarían con otros valores representativos, con varios propulsores o con otros criterios (madurez, vida útil, masa).
- 🎯 **Por qué importa:** Cada arquitectura gana en una dimensión y pierde en otra. La decisión central: ¿qué opciones no están dominadas por otra en propelente y en tiempo, y cómo cambia el resultado con la potencia disponible?
- 🔗 **Se estudia junto con:** comparación no operativa, valor representativo, frente de Pareto, tope de potencia.

📘 **Dónde se aprende** (2 clases): [B78-C20 · Comparación no operativa de arquitecturas de propulsión](../programa/clases/B78/B78-C20-comparacion-no-operativa-de-arquitecturas-de-propulsion/CLASE.md); [B83-C07 · Arquitecturas de sistemas](../programa/clases/B83/B83-C07-arquitecturas-de-sistemas/CLASE.md).

### Dominante

- La condición de energía débil pide `ρ ≥ 0` y `ρ + p ≥ 0`; la dominante, `ρ ≥ |p|`; la fuerte, `ρ + 3p ≥ 0`.

💡 **Cómo se explica en la clase [B39-C04](../programa/clases/B39/B39-C04-tensor-de-energia-momento-y-fuentes-de-curvatura/CLASE.md):**
- ecuacion de estado w = p/rho debil dominante fuerte
- 🎯 **Por qué importa:** La fuente de la gravedad es `T^ab`. La decisión central: ¿qué tensor describe la materia y qué condiciones debe cumplir para ser físicamente razonable?
- 🔗 **Se estudia junto con:** fluido perfecto, densidad, presión, parámetro.

📘 **Dónde se aprende** (1 clase): [B39-C04 · Tensor de energía-momento y fuentes de curvatura](../programa/clases/B39/B39-C04-tensor-de-energia-momento-y-fuentes-de-curvatura/CLASE.md).

### Dominio

- Una función `f` asigna a cada valor `x` de un conjunto (el dominio) un único valor `f(x)`; el conjunto de los resultados es el rango.
- Una función de dos variables asigna a cada par `(x, y)` de su dominio un número `f(x, y)` (S1, §1.5).

💡 **Cómo se explica en la clase [B04-C04](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md):**
- El dominio de la fórmula y el dominio físico son cosas distintas; esta clase declara el segundo.
- X["Entrada x<br/>(dominio, con unidad)"] --> F["Regla f<br/>y = k x^n"]
- ⚠️ **Error frecuente:** Confundir dominio de la fórmula con dominio físico. Se corrige con el ejercicio 8.
- 🎯 **Por qué importa:** Un astrónomo no solo calcula un valor: pregunta «¿qué pasa con el periodo de un planeta si su órbita es el doble de grande?». Responderlo con un solo caso no basta; hace falta la regla que liga ambas magnitudes.
- 🔗 **Se estudia junto con:** función, rango, variable independiente, dependiente.

📘 **Dónde se aprende** (2 clases): [B04-C04 · Funciones y gráficas](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md); [B09-C15 · Funciones de varias variables](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md).

### Dominio de electrones

- Un dominio de electrones es una región alrededor del átomo central donde hay electrones: cada enlace (simple, doble o triple) cuenta como uno, y cada par solitario también.

💡 **Cómo se explica en la clase [B06-C05](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md):**
- Contar dominios de electrones alrededor de un átomo central y predecir la geometría.
- 🎯 **Por qué importa:** El dióxido de carbono es el 95,1 % de la atmósfera de Marte en volumen (S2), y los hielos de las nubes densas del medio interestelar contienen, según un estudio con el telescopio James Webb, agua y CO₂ entre otras especies (S3, que se leyó sólo en resumen).
- 🔗 **Se estudia junto con:** modelo de repulsión de pares de valencia, geometría electrónica, forma molecular, lineal.

📘 **Dónde se aprende** (1 clase): [B06-C05 · Moléculas y geometría molecular](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md).

### Dominio de entrenamiento

- El dominio de entrenamiento es el rango de entradas cubierto.

💡 **Cómo se explica en la clase [B17-C04](../programa/clases/B17/B17-C04-modelos-sustitutos-surrogates/CLASE.md):**
- Mostrar qué ocurre fuera del dominio de entrenamiento.
- Que todas las combinaciones están dentro del dominio de entrenamiento, que el error en puntos reservados es pequeño frente a la dispersión que quieres medir, y que la cobertura de la banda es adecuada.
- 🎯 **Por qué importa:** Un simulador de trayectoria, de aerodinámica o de transporte de radiación puede tardar minutos u horas por ejecución. Para explorar miles de combinaciones de parámetros (un análisis de sensibilidad, una propagación de incertidumbre, una optimización) no alcanza el tiempo.
- 🔗 **Se estudia junto con:** simulador, modelo sustituto, diseño de experimentos, secuencia de Sobol.

📘 **Dónde se aprende** (1 clase): [B17-C04 · Modelos sustitutos (surrogates)](../programa/clases/B17/B17-C04-modelos-sustitutos-surrogates/CLASE.md).

### Dominio de validación

- El dominio de validación es el rango (cuerpo, tiempo, precisión) en que la comparación respalda el uso del modelo.
- El dominio de verificación y el dominio de validación son los rangos en que se comprobó cada cosa.

💡 **Cómo se explica en la clase [B23-C05](../programa/clases/B23/B23-C05-validacion-con-conjuntos-oficiales/CLASE.md):**
- Registrar el dominio de validación del modelo.
- Ejercicio 12 · integrador. Entrega un informe de validación del modelo kepleriano con otra época inicial o con otro cuerpo (a tu elección y con datos que consultes): declaración del conjunto, criterios previos, verificación de datos, veredictos, interpretación y dominio de validación.
- 🎯 **Por qué importa:** Un modelo kepleriano de la Tierra pasó todas las pruebas de C01–C04, pero eso no dice nada sobre si la Tierra se mueve como una elipse perfecta. La pregunta motivadora es: ¿contra qué contrasto mi modelo, y qué diferencia estoy dispuesto a aceptar?
- 🔗 **Se estudia junto con:** conjunto de referencia, efeméride, elementos osculadores, criterio de aceptación.

📘 **Dónde se aprende** (2 clases): [B23-C05 · Validación con conjuntos oficiales](../programa/clases/B23/B23-C05-validacion-con-conjuntos-oficiales/CLASE.md); [B23-C08 · Informe de verificación y validación](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md).

### Dominio de validez

- El dominio de validez es el rango en que el modelo se ha comprobado y se puede usar.
- El dominio de validez es el rango de entradas para el que el modelo es correcto.

💡 **Cómo se explica en la clase [B01-C17](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md):**
- Definir modelo, variable, parámetro, supuesto y dominio de validez con un ejemplo astronómico.
- 🎯 **Por qué importa:** Al final de C13, la tercera ley de Kepler daba `T²/a³ = 1` para siete planetas con error menor al 1,5 %, y 0,975 para Neptuno. ¿Falla el modelo con Neptuno?
- 🔗 **Se estudia junto con:** modelo científico, variable, parámetro, supuesto.

📘 **Dónde se aprende** (2 clases): [B01-C17 · Construcción de modelos científicos](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md); [B14-C01 · Arquitectura de software científico](../programa/clases/B14/B14-C01-arquitectura-de-software-cientifico/CLASE.md).

### Dominio de verificación

- El dominio de verificación y el dominio de validación son los rangos en que se comprobó cada cosa.

💡 **Cómo se explica en la clase [B23-C08](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md):**
- Exige mantener un registro del dominio de verificación y del dominio de validación.
- 🎯 **Por qué importa:** Un conjunto de pruebas que pasan no es un informe. Quien debe decidir si usar el código necesita saber para qué uso se evaluó, con qué criterios, qué falló y qué no se probó.
- 🔗 **Se estudia junto con:** uso previsto, criterio de aceptación, regla de decisión, advertencia.

📘 **Dónde se aprende** (1 clase): [B23-C08 · Informe de verificación y validación](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md).

### Domo

- Un domo es un edificio abovedado de magma muy viscoso.

💡 **Cómo se explica en la clase [B70-C02](../programa/clases/B70/B70-C02-domos-volcanicos-y-vulcanismo-evolucionado/CLASE.md):**
- Límite: un domo real tiene corteza, cristales y enfriamiento.
- El ejemplo conductor es un domo sintético de `R = 1500 m`, `ρ = 2400 kg/m³` y `τ = 10⁵ Pa`: en la Tierra su altura central es `112,9 m` y su volumen `0,4256 km³`; con la gravedad de Marte, `183,1 m` y `0,6901 km³`.
- 🎯 **Por qué importa:** Una colina empinada de lava puede tener una altura que solo depende del material y de `g`. La decisión central: ¿qué altura puede alcanzar un domo de resistencia dada y qué cambiaría en otro mundo?
- 🔗 **Se estudia junto con:** resistencia a la fluencia, plástico perfecto, vulcanismo evolucionado.

📘 **Dónde se aprende** (1 clase): [B70-C02 · Domos volcánicos y vulcanismo evolucionado](../programa/clases/B70/B70-C02-domos-volcanicos-y-vulcanismo-evolucionado/CLASE.md).

### DOP

- El DOP (*dilution of precision*) amplifica el error: `PDOP = √(Q₁₁+Q₂₂+Q₃₃)` con `Q = (GᵀG)⁻¹`.

💡 **Cómo se explica en la clase [B57-C10](../programa/clases/B57/B57-C10-geodesia-mediante-gnss/CLASE.md):**
- El error 3D simulado coincide con `PDOP × σ` en ambos casos: el DOP resume cuánto amplifica la geometría el ruido de medición.
- Paso 1 · DOP. `PDOP = 2,80` con ocho satélites repartidos.
- ⚠️ **Error frecuente:** Creer que más satélites siempre mejora el DOP. Depende de la distribución (8.2).
- 🎯 **Por qué importa:** La geodesia con GNSS mide posiciones de estaciones con precisión de milímetros a centímetros y sirve para ver cómo se mueve la corteza. Pero la precisión depende de la geometría de los satélites.
- 🔗 **Se estudia junto con:** pseudodistancia, matriz de geometría, HDOP, VDOP.

📘 **Dónde se aprende** (1 clase): [B57-C10 · Geodesia mediante GNSS](../programa/clases/B57/B57-C10-geodesia-mediante-gnss/CLASE.md).

### Doppler

- Rango: distancia estación–satélite. Doppler: corrimiento de frecuencia.

💡 **Cómo se explica en la clase [B96-C05](../programa/clases/B96/B96-C05-estaciones-de-seguimiento/CLASE.md):**
- Las relaciones de geometría y de Doppler son estándar y las verifica el laboratorio; no se tomaron de una fuente concreta.
- (1) El Doppler cruza cero a 625 s, igual que la distancia mínima de 968,9 km.
- ⚠️ **Error frecuente:** Invertir el signo del Doppler. Positivo al acercarse (8.3)
- 🎯 **Por qué importa:** Para que una antena apunte y un receptor enganche, la estación debe conocer de antemano el azimut, la elevación y el corrimiento de frecuencia. La decisión central: ¿hacia dónde apuntar y qué frecuencia esperar en cada instante?
- 🔗 **Se estudia junto con:** Estación de seguimiento, Azimut/elevación, Rango, Velocidad radial.

📖 **Explicado a fondo:** [Doppler (efecto)](esencial/esencial-d-l.md#doppler-efecto) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B96-C05 · Estaciones de seguimiento](../programa/clases/B96/B96-C05-estaciones-de-seguimiento/CLASE.md).

### Doppler clásico

- El Doppler clásico `z = v/c`; el relativista `1 + z = √((1+β)/(1−β))`.

💡 **Contexto en la clase [B45-C12](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md):**
- **Idea central (modelo mental):** Como la sirena de una ambulancia: el tono sube al acercarse y baja al alejarse; el corrimiento de las líneas es proporcional a la velocidad.
- 🎯 **Por qué importa:** Las velocidades radiales descubren planetas, binarias y la expansión del universo. La decisión central: ¿cómo se pasa de un corrimiento a una velocidad y con qué precisión?
- 🔗 **Se estudia junto con:** corrimiento, relativista, correlación cruzada, paso en velocidad.

📘 **Dónde se aprende** (1 clase): [B45-C12 · Efecto Doppler en espectros](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md).

### Doppler de dos sentidos

- El Doppler de dos sentidos mide la diferencia entre la frecuencia emitida y la recibida tras el viaje de ida y vuelta.

💡 **Cómo se explica en la clase [B74-C04](../programa/clases/B74/B74-C04-doppler-de-navegacion/CLASE.md):**
- Con una portadora ilustrativa de `7,2 GHz` y una velocidad radial de `30 km/s` el Doppler de dos sentidos es `-1440,997 kHz`; la sensibilidad es `48,0332 Hz` por m/s.
- Calcular el Doppler de dos sentidos `f_D = −2 f_t ρ̇/c` con su signo.
- 🎯 **Por qué importa:** Una velocidad radial de `1 mm/s` produce un desplazamiento de decenas de milihercios, medible; por eso el Doppler es el observable más preciso de la navegación en espacio profundo. La decisión central: ¿qué información da el Doppler (velocidad en la línea de visión) y qué no (posición transversal)?
- 🔗 **Se estudia junto con:** velocidad radial, cuenta integrada, sensibilidad.

📘 **Dónde se aprende** (1 clase): [B74-C04 · Doppler de navegación](../programa/clases/B74/B74-C04-doppler-de-navegacion/CLASE.md).

### Doppler de ida

- El Doppler de ida es `f_D = −f ṙ/c`, con `ṙ` la velocidad radial (positiva si se aleja).

💡 **Cómo se explica en la clase [B89-C15](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md):**
- Invirtiendo este modelo desde la pendiente se recupera `ρ_min = 685,7 km` (real `694,1 km`): el Doppler contiene información de la órbita.
- Un transpondedor con razón `880/749 = 1,17490` devuelve la portadora ascendente (7,19 GHz, ilustrativa) multiplicada por la razón; el Doppler de ida y vuelta en el TCA es `-0,000 kHz` y en el AOS `376,4 kHz`: más del doble del de ida porque cuenta dos trayectos.
- ⚠️ **Error frecuente:** Confundir el signo del Doppler. Se corrige con 8.2.
- 🎯 **Por qué importa:** El Doppler es la medida básica de rastreo: se usa para determinar la órbita y obliga a diseñar los lazos de portadora y los planes de frecuencia. La decisión central: ¿cuánto se desplaza la frecuencia durante una pasada y qué información de la órbita contiene?
- 🔗 **Se estudia junto con:** tasa de Doppler, TCA, Doppler de ida y vuelta.

📘 **Dónde se aprende** (1 clase): [B89-C15 · Rastreo y Doppler](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md).

### Doppler de ida y vuelta

- El Doppler de ida y vuelta coherente recibe `f_rx = (880/749) f_up (1 + …)`: la nave devuelve la portadora multiplicada por la razón de transpondedor (880/749 se usa aquí como ilustración).

💡 **Cómo se explica en la clase [B89-C15](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md):**
- Un transpondedor con razón `880/749 = 1,17490` devuelve la portadora ascendente (7,19 GHz, ilustrativa) multiplicada por la razón; el Doppler de ida y vuelta en el TCA es `-0,000 kHz` y en el AOS `376,4 kHz`: más del doble del de ida porque cuenta dos trayectos.
- *Descripción textual:* la geometría da la velocidad radial; con ella se calcula el Doppler, su tasa en el TCA (de donde se estima la distancia mínima) y el Doppler de ida y vuelta con el transpondedor.
- ⚠️ **Error frecuente:** Olvidar que el Doppler de ida y vuelta cuenta dos trayectos. Se corrige con 8.4.
- 🎯 **Por qué importa:** El Doppler es la medida básica de rastreo: se usa para determinar la órbita y obliga a diseñar los lazos de portadora y los planes de frecuencia. La decisión central: ¿cuánto se desplaza la frecuencia durante una pasada y qué información de la órbita contiene?
- 🔗 **Se estudia junto con:** Doppler de ida, tasa de Doppler, TCA.

📘 **Dónde se aprende** (1 clase): [B89-C15 · Rastreo y Doppler](../programa/clases/B89/B89-C15-rastreo-y-doppler/CLASE.md).

### Doppler relativista

- El Doppler relativista de una fuente que se aleja con `β` da `f_r/f_e = √((1−β)/(1+β)) = e^{−atanh β}`.
- El Doppler relativista da `v = c((1+z)²−1)/((1+z)²+1)`.

💡 **Cómo se explica en la clase [B26-C06](../programa/clases/B26/B26-C06-principio-de-equivalencia/CLASE.md):**
- El Doppler relativista da `1 − √((1−β)/(1+β))`.
- Verificarlo con el Doppler relativista en un cohete acelerado.
- 🎯 **Por qué importa:** Los relojes de los satélites de navegación van a un ritmo ligeramente distinto de los terrestres, y un maser en una torre ve su frecuencia cambiar con la altura. Todo eso se deduce de la equivalencia entre aceleración y gravedad.
- 🔗 **Se estudia junto con:** principio de equivalencia (débil), principio de equivalencia de Einstein (local), marco en caída libre, corrimiento gravitacional al rojo.

📘 **Dónde se aprende** (2 clases): [B26-C06 · Principio de equivalencia](../programa/clases/B26/B26-C06-principio-de-equivalencia/CLASE.md); [B26-C11 · Expansión cósmica y ley de Hubble-Lemaître](../programa/clases/B26/B26-C11-expansion-cosmica-y-ley-de-hubble-lemaitre/CLASE.md).

### Dormand–Prince 5(4)

- RK4 es de orden 4. Dormand–Prince 5(4) es un par encajado de órdenes 5 y 4 cuya diferencia estima el error local.

💡 **Cómo se explica en la clase [B72-C18](../programa/clases/B72/B72-C18-integracion-numerica-perturbada/CLASE.md):**
- Descripción larga: Euler falla por miles de kilómetros, RK4 converge con orden cuatro hasta centímetros con 4320 pasos y Dormand–Prince alcanza un centímetro con 1738 pasos aceptados.
- Implementar Euler, RK4 y Dormand–Prince 5(4).
- 🎯 **Por qué importa:** Un integrador mal elegido da una órbita que parece correcta y está equivocada en kilómetros. La decisión central: ¿qué método, paso o tolerancia da el error de posición que necesita la tarea al menor coste, y cómo saber que no engaña?
- 🔗 **Se estudia junto con:** método de Cowell, Euler explícito, RK4, integrales de movimiento.

📘 **Dónde se aprende** (1 clase): [B72-C18 · Integración numérica perturbada](../programa/clases/B72/B72-C18-integracion-numerica-perturbada/CLASE.md).

### Dos corrientes

- La relación de dos corrientes `T_s⁴ = T_e⁴ (1 + 3τ/4)` es la solución gris en equilibrio radiativo.

💡 **Contexto en la clase [B54-C09](../programa/clases/B54/B54-C09-efecto-invernadero/CLASE.md):**
- **Idea central (modelo mental):** Una manta sobre una estufa no añade energía: obliga a la estufa a calentarse más para que el calor pueda salir.
- 🎯 **Por qué importa:** La diferencia entre la temperatura de equilibrio (B54-C03) y la observada necesita una causa. La pregunta motivadora: ¿qué opacidad infrarroja hace falta para explicar la temperatura de superficie de cada mundo?
- 🔗 **Se estudia junto con:** atmósfera gris, profundidad óptica infrarroja, capa isoterma.

📘 **Dónde se aprende** (1 clase): [B54-C09 · Efecto invernadero](../programa/clases/B54/B54-C09-efecto-invernadero/CLASE.md).

### Dos cuerpos

- El problema de dos cuerpos describe un punto en el campo de una masa central.

💡 **Cómo se explica en la clase [B58-C02](../programa/clases/B58/B58-C02-dinamica-de-asteroides/CLASE.md):**
- El modelo de dos cuerpos solo ubica *dónde* mirar.
- Analítica: Kepler da el periodo exacto de dos cuerpos.
- 🎯 **Por qué importa:** Predecir la posición de un asteroide dentro de décadas exige un integrador que se pueda verificar. Saber que un esquema numérico converge con el orden esperado es lo que da confianza antes de añadir perturbaciones.
- 🔗 **Se estudia junto con:** leapfrog, simpléctico, orden, resonancia de movimiento medio.

📘 **Dónde se aprende** (1 clase): [B58-C02 · Dinámica de asteroides](../programa/clases/B58/B58-C02-dinamica-de-asteroides/CLASE.md).

### Dos ejes

- un eje gira para seguir al Sol en el plano; dos ejes lo siguen siempre.

💡 **Cómo se explica en la clase [B86-C04](../programa/clases/B86/B86-C04-orientacion-solar-y-eclipses/CLASE.md):**
- Con dos ejes el coseno medio es `1 − f`; con un eje es `(1 − f) cosβ`; con el ala fija al cenit es mucho menor (`≈ cosβ/π` antes de restar el eclipse).
- BETA --> C["coseno medio: fija, 1 eje, 2 ejes"]
- 🎯 **Por qué importa:** El eclipse más largo fija el tamaño de la batería y el peor `β` fija el de la ala. Un diseño que mire solo `β = 0` ignora que a `β` alto no hay eclipse pero el coseno cae.
- 🔗 **Se estudia junto con:** ángulo beta, β crítico, sombra cilíndrica, ala fija.

📘 **Dónde se aprende** (1 clase): [B86-C04 · Orientación solar y eclipses](../programa/clases/B86/B86-C04-orientacion-solar-y-eclipses/CLASE.md).

### Dos fases

- El modelo de tres fases trata gas, superficie y manto como reservorios distintos; el de dos fases, solo gas y superficie.

💡 **Cómo se explica en la clase [B60-C04](../programa/clases/B60/B60-C04-balance-quimico-gas-grano-modelos-de-tres-fases/CLASE.md):**
- Un modelo de dos fases mantiene 79 monocapas como «superficie activa»; el de tres fases, una.
- El de dos fases libera todo entre 20 y 25 K; el de tres fases libera la superficie y deja el manto, que sale con la lentitud del intercambio.
- 🎯 **Por qué importa:** Un modelo de dos fases trata todo el hielo como si estuviera expuesto en la superficie; en la realidad la mayor parte queda enterrada bajo capas posteriores. La decisión central: ¿qué cambia en la predicción de cuánto hielo se libera al calentar si se distingue la superficie del manto?
- 🔗 **Se estudia junto con:** acreción, desorción térmica, superficie, manto.

📘 **Dónde se aprende** (1 clase): [B60-C04 · Balance químico gas-grano: modelos de tres fases](../programa/clases/B60/B60-C04-balance-quimico-gas-grano-modelos-de-tres-fases/CLASE.md).

### Dos haces

- Los dos haces son dos poblaciones que se cruzan.

💡 **Cómo se explica en la clase [B35-C03](../programa/clases/B35/B35-C03-inestabilidades-de-plasma-cineticas-y-de-fluido/CLASE.md):**
- Las dos vías coinciden a `10⁻⁹` en los haces y a `10⁻⁶` en Kelvin–Helmholtz.
- Límite: solo teoría lineal; haces fríos y fluido incompresible.
- 🎯 **Por qué importa:** Las inestabilidades limitan los equilibrios y convierten energía libre en turbulencia. La decisión central: ¿para qué número de onda y para qué cizalladura crece la perturbación y cuánto?
- 🔗 **Se estudia junto con:** tasa de crecimiento, relación de dispersión, Kelvin–Helmholtz, umbral.

📘 **Dónde se aprende** (1 clase): [B35-C03 · Inestabilidades de plasma: cinéticas y de fluido](../programa/clases/B35/B35-C03-inestabilidades-de-plasma-cineticas-y-de-fluido/CLASE.md).

### Dosis

- Una dosis es la energía absorbida por masa.
- La dosis `D` es la energía depositada por molécula (eV/molécula).
- La dosis es `p ∫ C dt`.

💡 **Cómo se explica en la clase [B33-C08](../programa/clases/B33/B33-C08-dosis-de-radiacion-en-aviacion/CLASE.md):**
- El juguete exagera el crecimiento porque supone un solo componente sin cascada; no debe usarse para estimar dosis.
- Ejercicio 5. Dosis ilustrativa de 8 h a 5 µSv/h.
- ⚠️ **Error frecuente:** Usar el juguete para dosis. Se corrige con 8.3.
- 🎯 **Por qué importa:** La altitud y la profundidad atmosférica determinan cuánta radiación llega. La decisión central: ¿cuánto menos atmósfera hay a la altitud de vuelo?
- 🔗 **Se estudia junto con:** profundidad atmosférica, altura de escala, longitud de atenuación, tasa relativa.

📘 **Dónde se aprende** (3 clases): [B33-C08 · Dosis de radiación en aviación](../programa/clases/B33/B33-C08-dosis-de-radiacion-en-aviacion/CLASE.md); [B68-C03 · Irradiación de hielos por rayos cósmicos y UV: radiólisis y productos](../programa/clases/B68/B68-C03-irradiacion-de-hielos-por-rayos-cosmicos-y-uv-radiolisis-y-productos/CLASE.md); [B110-C02 · Protocolos operativos de aislamiento de un tripulante enfermo o contaminado](../programa/clases/B110/B110-C02-protocolos-operativos-de-aislamiento-de-un-tripulante-enfermo-o-contaminado/CLASE.md).
