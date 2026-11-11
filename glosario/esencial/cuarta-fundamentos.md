# Glosario esencial (cuarta tanda) · Fundamentos de observación, matemática y datos

[⬅️ Índice del glosario esencial](README.md) · [Glosario completo](../README.md)

Los conceptos que sostienen las áreas A01 y A02 y que aparecen en casi todas las clases: cómo se ubica algo en el cielo, cómo se miden y se combinan los números y cómo se trabaja con datos. Mismo esquema: **en una frase**, **cómo pensarlo**, **fórmula y unidades**, **ejemplo con números**, **error frecuente**, **relacionados**. Valores redondeados.

---

### Altura y acimut

**En una frase.** Las dos coordenadas con las que se apunta un telescopio o se ubica un astro desde un lugar y un instante: la altura sobre el horizonte y el ángulo medido sobre él.

**Cómo pensarlo.** Son coordenadas «locales»: cambian con la hora y con el lugar. La **altura** va de 0° (horizonte) a 90° (cenit). El **acimut** se mide desde el norte hacia el este (0° N, 90° E, 180° S, 270° O). Para guardar posiciones que no cambian se usan, en cambio, la ascensión recta y la declinación.

**Fórmula.** Altura máxima (al cruzar el meridiano): h = 90° − |φ − δ|, con φ la latitud y δ la declinación.

**Ejemplo.** Sirio (δ = −16,7°) visto desde Santiago (φ = −33,4°): h_máx = 90° − |−33,4° + 16,7°| = **73,3°**.

**Error frecuente.** Dar la posición de un objeto en altura y acimut sin decir la hora y el lugar.

**Relacionados:** ascensión recta y declinación, esfera celeste, tiempo sidéreo.
📘 [B08](../../programa/tronco-comun/B08-observacion-del-cielo-y-astronomia-practica.md "Observación del cielo y astronomía práctica").

---

### Año tropical y año sidéreo

**En una frase.** El año tropical es el tiempo entre dos equinoccios iguales (el de las estaciones); el sidéreo, el que tarda la Tierra en volver a la misma posición respecto de las estrellas.

**Cómo pensarlo.** Por la precesión, el punto vernal se mueve lentamente respecto de las estrellas, así que ambos años difieren en unos 20 minutos. El calendario sigue el tropical para que las estaciones caigan en las mismas fechas.

**Valores.** Tropical ≈ 365,2422 d; sidéreo ≈ 365,2564 d; juliano (convención) = 365,25 d.

**Ejemplo.** La diferencia es 0,0142 d ≈ **20,4 min** por año. Acumulada en 25 800 años (un ciclo de precesión) da un año completo.

**Error frecuente.** Usar 365 días en cálculos de largo plazo.

**Relacionados:** precesión, equinoccio, calendario gregoriano.
📘 [B02](../../programa/tronco-comun/B02-historia-arqueoastronomia-y-culturas-del-cielo.md "Historia, arqueoastronomía y culturas del cielo"), [B13](../../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md "Metrología, tiempo y mediciones científicas").

---

### Bayes (teorema de)

**En una frase.** Regla que dice cómo actualizar la probabilidad de una hipótesis cuando aparece un dato nuevo.

**Cómo pensarlo.** Se parte de lo que se creía (la *a priori*), se pondera por cuán probable es el dato si la hipótesis fuera cierta (la *verosimilitud*) y se obtiene la *a posteriori*. Evita el error de confundir «el dato es raro si la hipótesis es falsa» con «la hipótesis es probable».

**Fórmula.** P(H | D) = P(D | H) P(H) / P(D).

**Ejemplo.** Una prueba detecta una señal con 99 % de acierto y da 1 % de falsos positivos. Si la señal real ocurre en el 1 % de los casos, una prueba positiva implica P = (0,99 × 0,01) / (0,99 × 0,01 + 0,01 × 0,99) = **50 %**, no 99 %.

**Error frecuente.** Ignorar la probabilidad a priori («tasa base»).

**Relacionados:** incertidumbre, falso positivo, inferencia bayesiana.
📘 [B12](../../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md "Probabilidad, estadística e incertidumbre"), [B19](../../programa/tronco-comun/B19-inferencia-bayesiana-y-computacion-probabilistica.md "Inferencia bayesiana y computación probabilística").

---

### Cifras significativas

**En una frase.** Los dígitos de un número que tienen sentido dado cuánto sabemos de él.

**Cómo pensarlo.** Escribir más cifras de las que sabes da una falsa impresión de precisión. En un producto o cociente, el resultado se da con tantas cifras como el factor menos preciso; en una suma, con los decimales del sumando menos preciso.

**Ejemplo.** (3,0 × 10⁸) × 2,00 = **6,0 × 10⁸**, no 6,000 × 10⁸. Una masa de 1,2 kg + 0,345 kg = **1,5 kg**.

**Error frecuente.** Copiar todos los dígitos de la calculadora.

**Relacionados:** incertidumbre, redondeo, notación científica.
📘 [B03](../../programa/tronco-comun/B03-matematica-elemental-para-ciencias-espaciales.md "Matemática elemental para ciencias espaciales"), [B13](../../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md "Metrología, tiempo y mediciones científicas").

---

### Constelación y asterismo

**En una frase.** Una constelación es una de las 88 regiones oficiales en que se divide el cielo; un asterismo, una figura informal de estrellas.

**Cómo pensarlo.** Las constelaciones son recortes del cielo, como países en un mapa (la Unión Astronómica Internacional fijó sus límites en 1930). Las estrellas que las forman suelen estar a distancias muy distintas: la figura solo existe desde la Tierra. Cada cultura dibuja otras figuras, incluidas las «constelaciones oscuras» andinas.

**Ejemplo.** La Cruz del Sur es una constelación; el «Triángulo de verano» es un asterismo. Las estrellas de la Osa Mayor (el Carro) están a distancias de unos 80 a 120 años luz del Sol, con diferencias de decenas de años luz entre sí.

**Error frecuente.** Creer que las estrellas de una constelación están juntas en el espacio.

**Relacionados:** esfera celeste, arqueoastronomía, cartas del cielo.
📘 [B08](../../programa/tronco-comun/B08-observacion-del-cielo-y-astronomia-practica.md "Observación del cielo y astronomía práctica"), [B02](../../programa/tronco-comun/B02-historia-arqueoastronomia-y-culturas-del-cielo.md "Historia, arqueoastronomía y culturas del cielo"), [B133](../../programa/tronco-comun/B133-saberes-astronomicos-y-educacion-intercultural.md "Saberes astronómicos y educación intercultural").

---

### Derivada

**En una frase.** El ritmo al que cambia una cantidad respecto de otra.

**Cómo pensarlo.** Si x(t) es la posición, su derivada es la velocidad (cuánto cambia la posición por segundo); la derivada de la velocidad es la aceleración. En un gráfico, es la pendiente de la tangente. Sirve para encontrar máximos y mínimos y para escribir las leyes de la física.

**Fórmula.** v = dx/dt = lím (Δx/Δt) cuando Δt → 0.

**Ejemplo.** Si x = 5 t² (m), entonces v = **10 t** (m/s) y a = **10 m/s²**. A t = 3 s: v = 30 m/s.

**Error frecuente.** Confundir el valor de una cantidad con su ritmo de cambio.

**Relacionados:** integral, ecuación diferencial, pendiente.
📘 [B09](../../programa/tronco-comun/B09-calculo-diferencial-e-integral.md "Cálculo diferencial e integral").

---

### Ecuación diferencial y método de Euler

**En una frase.** Una ecuación diferencial relaciona una cantidad con su ritmo de cambio; el método de Euler la resuelve paso a paso de forma aproximada.

**Cómo pensarlo.** Casi todas las leyes del movimiento son ecuaciones diferenciales (la segunda ley de Newton). Como pocas tienen solución exacta, se avanza en el tiempo con pasos pequeños: se usa la pendiente actual para estimar el siguiente valor. El error depende del tamaño del paso.

**Fórmula.** y(t + h) ≈ y(t) + h f(t, y).

**Ejemplo.** dy/dt = −y con y(0) = 1 y h = 0,1: tras 10 pasos, y(1) ≈ 0,9¹⁰ = **0,3487**; la solución exacta es e⁻¹ = 0,3679 (error ≈ 5 %). Con h = 0,01 el error baja a ≈ 0,5 %.

**Error frecuente.** Usar un paso demasiado grande y creer el resultado sin comprobarlo con otro paso.

**Relacionados:** simulación numérica, integración, estabilidad.
📘 [B11](../../programa/tronco-comun/B11-ecuaciones-diferenciales-y-simulacion-numerica.md "Ecuaciones diferenciales y simulación numérica"), [B21](../../programa/tronco-comun/B21-metodos-numericos-para-edp-y-fluidos-computacionales.md "Métodos numéricos para EDP y fluidos computacionales").

---

### Error e incertidumbre

**En una frase.** El error es la diferencia entre una medida y el valor verdadero (que casi nunca se conoce); la incertidumbre es el intervalo en el que razonablemente cae el valor.

**Cómo pensarlo.** Toda medida lleva incertidumbre. Los errores **aleatorios** se promedian; los **sistemáticos** (un instrumento mal calibrado) no. Al combinar medidas, las incertidumbres se propagan.

**Fórmulas.** Suma o resta: σ = √(σ₁² + σ₂²). Producto o cociente: (σ/x)² = (σ₁/x₁)² + (σ₂/x₂)².

**Ejemplo.** L = 10,0 ± 0,3 m y a = 5,0 ± 0,4 m: L + a = 15,0 ± √(0,09 + 0,16) = **15,0 ± 0,5 m**.

**Error frecuente.** Dar un resultado sin incertidumbre o sumar las incertidumbres linealmente cuando son independientes.

**Relacionados:** media y desviación estándar, calibración, propagación.
📘 [B12](../../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md "Probabilidad, estadística e incertidumbre"), [B13](../../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md "Metrología, tiempo y mediciones científicas").

---

### Esfera celeste

**En una frase.** Esfera imaginaria, centrada en el observador, sobre la que se proyectan los astros.

**Cómo pensarlo.** Como no percibimos la profundidad del cielo, es cómodo ubicar los astros por su dirección y olvidar la distancia. La esfera tiene polos, ecuador, un horizonte local y la eclíptica (camino aparente del Sol). Su giro diario refleja la rotación de la Tierra.

**Ejemplo.** En 24 h sidéreas el cielo gira 360°, es decir, **15° por hora**, o 15″ por segundo de tiempo.

**Error frecuente.** Pensar que la esfera existe físicamente o que todos los astros están a la misma distancia.

**Relacionados:** coordenadas, constelación, tiempo sidéreo.
📘 [B08](../../programa/tronco-comun/B08-observacion-del-cielo-y-astronomia-practica.md "Observación del cielo y astronomía práctica").

---

### Fases de la Luna

**En una frase.** Cambios de la parte iluminada de la Luna que vemos, según su posición respecto del Sol y la Tierra.

**Cómo pensarlo.** La Luna siempre está iluminada a medias por el Sol; lo que cambia es cuánto de esa mitad apunta a nosotros. En la Luna nueva está entre la Tierra y el Sol; en la llena, la Tierra queda en medio. El ciclo (mes sinódico) dura 29,53 días; la Luna da una vuelta respecto de las estrellas en 27,32 días, y los 2,2 días extra se deben a que la Tierra avanza en su órbita.

**Ejemplo.** Una fase determinada se repite cada **29,53 d**; en un año hay ≈ 12,37 lunaciones.

**Error frecuente.** Atribuir las fases a la sombra de la Tierra (eso son los eclipses lunares).

**Relacionados:** eclipse, marea, mes sinódico.
📘 [B08](../../programa/tronco-comun/B08-observacion-del-cielo-y-astronomia-practica.md "Observación del cielo y astronomía práctica"), [B02](../../programa/tronco-comun/B02-historia-arqueoastronomia-y-culturas-del-cielo.md "Historia, arqueoastronomía y culturas del cielo").

---

### Fourier (transformada) y periodograma

**En una frase.** Herramienta que descompone una señal en las frecuencias que la forman.

**Cómo pensarlo.** Cualquier señal (la luz de una estrella variable, un sismo, una onda de radio) se puede ver como una suma de ondas simples. El espectro de frecuencias muestra cuáles dominan. El periodograma estima el período de una variación periódica incluso con datos irregulares. La frecuencia máxima que se puede detectar con muestreo regular a f_s es f_s/2 (frecuencia de Nyquist).

**Ejemplo.** Medir con 10 Hz permite detectar frecuencias de hasta **5 Hz**; una oscilación más rápida aparece disfrazada como una más lenta (aliasing).

**Error frecuente.** Interpretar picos del periodograma sin considerar el muestreo y el ruido.

**Relacionados:** curva de luz, señal-ruido, muestreo.
📘 [B15](../../programa/tronco-comun/B15-senales-imagenes-y-estimacion-cientifica.md "Señales, imágenes y estimación científica"), [B29](../../programa/tronco-comun/B29-astronomia-temporal-y-exoplanetas.md "Astronomía temporal y exoplanetas").

---

### Integral

**En una frase.** La acumulación de una cantidad que varía; en un gráfico, el área bajo la curva.

**Cómo pensarlo.** Es la operación inversa de la derivada: si conoces la aceleración en el tiempo, integrándola obtienes el cambio de velocidad; integrando esta, la posición. La navegación inercial y la ecuación del cohete se apoyan en esa idea.

**Fórmula.** Δv = ∫ a dt.

**Ejemplo.** Con a = 2 m/s² constante durante 10 s: Δv = 2 × 10 = **20 m/s**. Con a(t) = 2t: Δv = ∫₀¹⁰ 2t dt = **100 m/s**.

**Error frecuente.** Olvidar la constante de integración (la velocidad inicial).

**Relacionados:** derivada, navegación inercial, ecuación del cohete.
📘 [B09](../../programa/tronco-comun/B09-calculo-diferencial-e-integral.md "Cálculo diferencial e integral"), [B80](../../programa/tronco-comun/B80-navegacion-inercial-y-fusion-multisensorial.md "Navegación inercial y fusión multisensorial").

---

### Logaritmo

**En una frase.** El exponente al que hay que elevar una base para obtener un número.

**Cómo pensarlo.** Convierte multiplicaciones en sumas y comprime rangos enormes en escalas manejables. Por eso se usa en magnitudes estelares, decibelios, la escala sísmica y el pH. log₁₀ cuenta ceros; ln usa la base e.

**Fórmulas.** log₁₀(xy) = log₁₀x + log₁₀y; log₁₀(2) ≈ 0,301; ln x = 2,3026 × log₁₀ x.

**Ejemplo.** Un factor 2 en potencia = 10 log₁₀ 2 = **3,01 dB**. Un factor 100 en brillo = 2,5 log₁₀ 100 = **5 magnitudes**.

**Error frecuente.** Confundir log (base 10) con ln (base e) y olvidar que el logaritmo de un número menor que 1 es negativo.

**Relacionados:** decibelio, magnitud estelar, escala logarítmica.
📘 [B03](../../programa/tronco-comun/B03-matematica-elemental-para-ciencias-espaciales.md "Matemática elemental para ciencias espaciales"), [B09](../../programa/tronco-comun/B09-calculo-diferencial-e-integral.md "Cálculo diferencial e integral").

---

### Media y desviación estándar

**En una frase.** La media es el valor típico de un conjunto de datos; la desviación estándar, cuánto se dispersan alrededor de ella.

**Cómo pensarlo.** Al promediar N medidas independientes, la incertidumbre de la media baja como 1/√N: para ganar un factor 10 de precisión hacen falta 100 veces más datos. La desviación estándar describe los datos; el error estándar de la media describe la precisión del promedio.

**Fórmulas.** σ = √[Σ(xᵢ − x̄)² / (N − 1)]; σ_media = σ / √N.

**Ejemplo.** Medidas con σ = 2,0 y N = 100: σ_media = 2,0 / 10 = **0,2**.

**Error frecuente.** Promediar medidas sesgadas esperando que el error sistemático desaparezca.

**Relacionados:** incertidumbre, ruido, mínimos cuadrados.
📘 [B12](../../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md "Probabilidad, estadística e incertidumbre").

---

### Mínimos cuadrados (ajuste de una recta)

**En una frase.** Método para encontrar la recta (o curva) que mejor se ajusta a un conjunto de puntos minimizando la suma de los cuadrados de las diferencias.

**Cómo pensarlo.** Cada punto se aleja de la recta una distancia (residuo). Se elige la recta que hace mínima la suma de residuos al cuadrado. Es la base de casi todo ajuste de datos, desde la ley de Hubble hasta la calibración de instrumentos.

**Fórmulas.** y = m x + b; m = (NΣxy − ΣxΣy) / (NΣx² − (Σx)²); b = (Σy − mΣx) / N.

**Ejemplo.** Puntos (1,2), (2,4), (3,5): N = 3; Σx = 6; Σy = 11; Σxy = 25; Σx² = 14. m = (75 − 66) / (42 − 36) = **1,5**; b = (11 − 9) / 3 = **0,67**.

**Error frecuente.** Extrapolar fuera del rango de los datos o ignorar las incertidumbres de cada punto.

**Relacionados:** regresión, residuos, incertidumbre.
📘 [B12](../../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md "Probabilidad, estadística e incertidumbre"), [B22](../../programa/tronco-comun/B22-problemas-inversos-y-estimacion-de-modelos.md "Problemas inversos y estimación de modelos").

---

### Monte Carlo (método de)

**En una frase.** Técnica que resuelve un problema repitiendo muchas veces un experimento con números aleatorios.

**Cómo pensarlo.** Cuando un cálculo exacto es difícil, se simula: se generan miles de casos aleatorios y se observa la distribución del resultado. Se usa para propagar incertidumbres, estimar riesgos de misión y simular transporte de radiación. El error baja como 1/√N.

**Ejemplo.** Para estimar π lanzando N puntos al azar en un cuadrado y contando los que caen dentro del círculo inscrito: con N = 10⁶, el error típico es ≈ 4 √(p(1−p)/N) ≈ **0,002**.

**Error frecuente.** Usar pocas muestras o un generador aleatorio de mala calidad.

**Relacionados:** probabilidad, propagación de errores, simulación.
📘 [B12](../../programa/tronco-comun/B12-probabilidad-estadistica-e-incertidumbre.md "Probabilidad, estadística e incertidumbre"), [B19](../../programa/tronco-comun/B19-inferencia-bayesiana-y-computacion-probabilistica.md "Inferencia bayesiana y computación probabilística").

---

### Notación científica y orden de magnitud

**En una frase.** La notación científica escribe un número como a × 10ⁿ; el orden de magnitud es la potencia de 10 más cercana.

**Cómo pensarlo.** En astronomía los números van de 10⁻¹⁹ m (núcleos) a 10²⁶ m (universo observable). Pensar en órdenes de magnitud permite verificar si un resultado es razonable antes de calcular con detalle (estimación de Fermi).

**Ejemplo.** Distancia Tierra–Sol: 1,5 × 10¹¹ m (orden 11). Luz solar: 1,5 × 10¹¹ / 3 × 10⁸ ≈ **500 s**. Si obtienes 5 s o 50 000 s, hay un error.

**Error frecuente.** Mezclar unidades (km y m) y no notar que el resultado se desvía en un factor 1 000.

**Relacionados:** cifras significativas, unidades, estimación.
📘 [B03](../../programa/tronco-comun/B03-matematica-elemental-para-ciencias-espaciales.md "Matemática elemental para ciencias espaciales"), [B13](../../programa/tronco-comun/B13-metrologia-tiempo-y-mediciones-cientificas.md "Metrología, tiempo y mediciones científicas").

---

### Oposición y conjunción

**En una frase.** Una conjunción es cuando dos astros parecen estar muy cerca en el cielo; en oposición, un planeta exterior queda en el lado contrario al Sol.

**Cómo pensarlo.** En oposición, el planeta exterior sale al atardecer, está en el cielo toda la noche y está más cerca de la Tierra: el mejor momento de observarlo. En conjunción con el Sol queda oculto por su brillo.

**Ejemplo.** Marte está en oposición cada ≈ 26 meses (el período sinódico de ≈ 780 días). Su distancia mínima puede bajar de 0,4 UA, y su brillo aumenta mucho.

**Error frecuente.** Pensar que en una conjunción los astros están realmente cerca: solo coinciden en la dirección.

**Relacionados:** período sinódico, elongación, retrogradación.
📘 [B08](../../programa/tronco-comun/B08-observacion-del-cielo-y-astronomia-practica.md "Observación del cielo y astronomía práctica"), [B75](../../programa/tronco-comun/B75-trayectorias-y-misiones-interplanetarias.md "Trayectorias y misiones interplanetarias").

---

### Punto flotante y precisión numérica

**En una frase.** Forma en que los computadores guardan los números reales, con un número finito de cifras.

**Cómo pensarlo.** Un número en doble precisión conserva unas 15–16 cifras decimales. No todos los decimales se representan exactamente (0,1 no tiene representación binaria finita), y al restar números casi iguales se pierden cifras. En cálculos largos, estos errores se acumulan.

**Ejemplo.** En Python, `0.1 + 0.2` da **0.30000000000000004**. El épsilon de máquina de doble precisión es ≈ 2,2 × 10⁻¹⁶. Por eso se comparan los números con una tolerancia, no con ==.

**Error frecuente.** Comparar decimales con == o restar números gigantes casi iguales.

**Relacionados:** método numérico, estabilidad, verificación de software.
📘 [B07](../../programa/tronco-comun/B07-informatica-cientifica-desde-cero.md "Informática científica desde cero"), [B14](../../programa/tronco-comun/B14-computacion-cientifica-y-ciencia-abierta.md "Computación científica y ciencia abierta"), [B23](../../programa/tronco-comun/B23-verificacion-y-validacion-de-software-cientifico.md "Verificación y validación de software científico").

---

### Retrogradación (movimiento retrógrado aparente)

**En una frase.** Tramo en que un planeta parece retroceder sobre el fondo de estrellas.

**Cómo pensarlo.** Es un efecto de perspectiva: cuando la Tierra, más rápida, «adelanta» a un planeta exterior (como Marte), este parece ir hacia atrás durante un tiempo, como un auto que ves retroceder al adelantarlo en la carretera. Los antiguos lo explicaban con epiciclos; el modelo heliocéntrico lo explica de forma simple.

**Ejemplo.** Marte retrograda unos **72 días** cada ≈ 26 meses, alrededor de la oposición.

**Error frecuente.** Creer que el planeta realmente invierte su órbita.

**Relacionados:** oposición, modelo heliocéntrico, Copérnico.
📘 [B02](../../programa/tronco-comun/B02-historia-arqueoastronomia-y-culturas-del-cielo.md "Historia, arqueoastronomía y culturas del cielo"), [B08](../../programa/tronco-comun/B08-observacion-del-cielo-y-astronomia-practica.md "Observación del cielo y astronomía práctica").

---

### Vector y producto escalar

**En una frase.** Un vector es una cantidad con magnitud y dirección; el producto escalar mide cuánto se alinean dos vectores.

**Cómo pensarlo.** Posición, velocidad, fuerza y campo son vectores. Se suman componente a componente. El producto escalar a·b = |a||b| cos θ sirve para hallar ángulos y proyecciones.

**Ejemplo.** a = (3, 4) y b = (4, 3): |a| = |b| = 5; a·b = 24; cos θ = 24/25 = 0,96 → θ ≈ **16,3°**. Comprobación: `calc "degrees(acos(24/25))"`.

**Error frecuente.** Sumar magnitudes de vectores sin tener en cuenta su dirección.

**Relacionados:** momento angular, torque, sistemas de referencia.
📘 [B04](../../programa/tronco-comun/B04-algebra-trigonometria-y-geometria-espacial.md "Álgebra, trigonometría y geometría espacial"), [B10](../../programa/tronco-comun/B10-algebra-lineal-y-matematicas-geometricas.md "Álgebra lineal y matemáticas geométricas").

---

[← Tercera tanda F – T](tercera-f-t.md) · [Índice](README.md)
