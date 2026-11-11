# Términos · C (parte 4 de 4)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · **C** · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-c.md) · [2](terminos-c-2.md) · [3](terminos-c-3.md) · **4**

### Cruce de láminas

- El cruce de láminas ocurre cuando `1 − aε = 0`.

💡 **Cómo se explica en la clase [B36-C05](../programa/clases/B36/B36-C05-simulaciones-cosmologicas-de-n-cuerpos-condiciones-iniciales-y-caja-periodica/CLASE.md):**
- En Einstein–de Sitter (`4πGρ̄ = 1,5 H²`) la ecuación de cada lámina es `x'' + (3/2a) x' = (3/2) a⁻² (x − q)` en la variable `a`, donde `q` es la posición lagrangiana del rango (la fuerza en 1D es exacta incluso después del cruce).
- Solo antes del cruce de láminas (`a < 1/ε`); a `a = 1,51` se desvía 3,8 espaciados.
- 🎯 **Por qué importa:** Una simulación sin comprobar contra un caso exacto no es una prueba. La decisión central: ¿converge el integrador al resultado analítico y qué pasa cuando las láminas se cruzan?

📘 **Dónde se aprende** (1 clase): [B36-C05 · Simulaciones cosmológicas de N cuerpos: condiciones iniciales y caja periódica](../programa/clases/B36/B36-C05-simulaciones-cosmologicas-de-n-cuerpos-condiciones-iniciales-y-caja-periodica/CLASE.md).

### Cruce de planos

- El cruce de planos es donde dos planos se intersecan.

🎯 **Por qué importa (clase B118-C15):** La sección 5.5 de la IADC Rev. 4 pide planificar y operar las constelaciones para minimizar la probabilidad de colisión entre sus miembros, en los cruces de planos y con otras constelaciones, y minimizar el riesgo acumulado de reentradas.

📘 **Dónde se aprende** (1 clase): [B118-C15 · Seguimiento de mega constelaciones](../programa/clases/B118/B118-C15-seguimiento-de-mega-constelaciones/CLASE.md).

### Cruce posicional

- Un cruce posicional (*cross-match*) empareja filas de dos catálogos que probablemente son el mismo objeto.

💡 **Cómo se explica en la clase [B14-C05](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md):**
- A["Catálogo A<br/>id, ra, dec, paralaje, procedencia"] --> X["Cruce posicional<br/>vecino más cercano"]
- *Descripción textual:* los dos catálogos entran a un cruce posicional que busca, para cada fuente de B, la más cercana de A.
- 🎯 **Por qué importa:** Un catálogo de estrellas no es una lista de números: cada columna tiene una unidad, algunas filas no tienen paralaje, y la tabla viene de un instrumento, una época y una versión. Si pierdes eso al copiar los datos a un arreglo, pierdes la mitad del significado.

📘 **Dónde se aprende** (1 clase): [B14-C05 · Tablas astronómicas y catálogos](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md).

### Cruda

- La carga ponderada es `Σ valoración × peso / 15`; la cruda, la media simple.

💡 **Cómo se explica en la clase [B111-C03](../programa/clases/B111/B111-C03-carga-cognitiva-y-gestion-de-la-atencion/CLASE.md):**
- Con los pesos de sus 15 comparaciones por pares la carga ponderada es `65,333` frente a `51,667` de la cruda.
- Calcular la carga ponderada y la carga cruda.
- 🎯 **Por qué importa:** Ninguna clase trataba la carga cognitiva ni el diseño de tareas para limitarla. La decisión central: ¿cómo se mide la carga y cómo se rediseña una secuencia para que no haya picos que superen la capacidad?

📘 **Dónde se aprende** (1 clase): [B111-C03 · Carga cognitiva y gestión de la atención](../programa/clases/B111/B111-C03-carga-cognitiva-y-gestion-de-la-atencion/CLASE.md).

### CSI

- El POD es la fracción de eventos detectados, el FAR la de alertas falsas y el CSI la de aciertos sobre todos los casos relevantes.

💡 **Cómo se explica en la clase [B30-C20](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md):**
- Calcular POD, FAR, CSI y la puntuación de Heidke por dos fórmulas.
- El script [alerta.py](alerta.py) clasifica un año sintético, arma la tabla de contingencia y calcula POD, FAR, CSI y Heidke por dos fórmulas (comprueba que las dos fórmulas de Heidke coinciden a `10⁻¹²`).
- 🎯 **Por qué importa:** Una alerta con muchas falsas alarmas se ignora y una con muchos fallos no sirve; medir ambas cosas es parte del oficio. La decisión central: ¿cómo se clasifica un evento y cómo se mide si una regla de alerta tiene habilidad?

📘 **Dónde se aprende** (1 clase): [B30-C20 · Análisis de alerta solar real](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md).

### CSV

- Un archivo CSV (*comma-separated values*) guarda una tabla como líneas de texto con campos separados por un delimitador, normalmente la coma.

💡 **Cómo se explica en la clase [B07-C08](../programa/clases/B07/B07-C08-lectura-de-archivos-csv/CLASE.md):**
- Un CSV sin procedencia no es un dato científico.
- Para `planetas_nssdc.csv` se declara en la cabecera del script y en la sección 11: quién publicó cada valor (NASA NSSDC), qué páginas, cuándo se consultaron y cuáles valores están redondeados (la densidad y la gravedad vienen de la tabla comparativa, con precisión menor).
- 🎯 **Por qué importa:** Un archivo CSV parece trivial y por eso engaña: todo se lee como texto, un decimal con coma rompe una columna, una línea vacía pasa inadvertida, y una codificación equivocada convierte «Júpiter» en símbolos raros. Un análisis hecho sobre datos mal leídos puede ser plausible y erróneo a la vez.

📘 **Dónde se aprende** (1 clase): [B07-C08 · Lectura de archivos CSV](../programa/clases/B07/B07-C08-lectura-de-archivos-csv/CLASE.md).

### CT

- Chick–Watson: inactivación proporcional a `C·t`. CT: concentración por tiempo.

💡 **Cómo se explica en la clase [B106-C26](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md):**
- Una desinfección de 4 log exige `CT = 8 mg·min/L`.
- Ejercicio 6 · autónomo. ¿Qué `CT` da 3 log?
- ⚠️ **Error frecuente:** Olvidar la desinfección. Añade CT (8.3).
- 🎯 **Por qué importa:** Las aguas grises son el mayor volumen del lazo y su carga orgánica hay que destruirla antes de potabilizar. La decisión central: ¿qué volumen de biorreactor y qué desinfección dan la remoción y la reducción de microorganismos requeridas?

📘 **Dónde se aprende** (1 clase): [B106-C26 · Tratamiento de aguas grises en hábitats](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md).

### CTE

- La CTE es la fracción de carga que pasa de un píxel al siguiente.

💡 **Cómo se explica en la clase [B44-C02](../programa/clases/B44/B44-C02-sensores-ccd/CLASE.md):**
- Con `1000 e⁻`, `CTE = 0,9999` y `400` transferencias, el valor analítico es `960,79 e⁻` y el simulado (300 repeticiones, semilla 20261109) `960,75 e⁻`, con error estándar de la media `0,35 e⁻`.
- *Descripción textual:* la carga inicial atraviesa `n` transferencias; la fracción restante es `CTE^n` y la simulación lo confirma.
- ⚠️ **Error frecuente:** Creer que la CTE es irrelevante por ser casi 1. Se corrige con 8.4.
- 🎯 **Por qué importa:** Cada transferencia pierde una pequeña fracción de carga, y un píxel lejano se transfiere miles de veces. La decisión central: ¿qué CTE hace aceptable un sensor de 2048 × 2048?

📘 **Dónde se aprende** (1 clase): [B44-C02 · Sensores CCD](../programa/clases/B44/B44-C02-sensores-ccd/CLASE.md).

### Cuaderno

- Un cuaderno es un documento con celdas de texto y de código, y las salidas de ese código.

💡 **Cómo se explica en la clase [B14-C09](../programa/clases/B14/B14-C09-jupyter-y-experimentos-reproducibles/CLASE.md):**
- El laboratorio construye el cuaderno con `nbformat` y lo valida contra el esquema: sus claves de nivel superior son `cells`, `metadata`, `nbformat` y `nbformat_minor`, con versión 4.5 y cuatro celdas (una de texto y tres de código).
- El texto del cuaderno no cambió, la salida sí.
- 🎯 **Por qué importa:** Alguien te manda un cuaderno con un gráfico que apoya una conclusión. Lo abres, ejecutas las celdas y el gráfico sale distinto.

📘 **Dónde se aprende** (1 clase): [B14-C09 · Jupyter y experimentos reproducibles](../programa/clases/B14/B14-C09-jupyter-y-experimentos-reproducibles/CLASE.md).

### Cuadrada

- Una matriz es cuadrada si `m = n`.

🎯 **Por qué importa (clase B10-C03):** Una estación terrestre está fija respecto de la Tierra, pero la Tierra gira respecto del espacio inercial. Para saber dónde está la estación en el sistema inercial a cada instante hay que aplicar una transformación que depende del tiempo.

📘 **Dónde se aprende** (1 clase): [B10-C03 · Matrices y operadores lineales](../programa/clases/B10/B10-C03-matrices-y-operadores-lineales/CLASE.md).

### Cuadrado

- El cuadrado de `a` es `a²`; el cubo, `a³`.

💡 **Cómo se explica en la clase [B03-C04](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md):**
- Si `√a` es el número que al cuadrado da `a`, entonces `(a^(1/2))² = a^(1/2 · 2) = a`, así que `a^(1/2) = √a` (por la regla 8.2).
- Un cuadrado de lado 3 se llena con `3 × 3 = 9` casillas; un cubo de arista 3, con `3 × 3 × 3 = 27` cajas.
- ⚠️ **Error frecuente:** Sumar al elevar una suma al cuadrado. Ejercicio 8.
- 🎯 **Por qué importa:** En 1619 Johannes Kepler publicó que el cuadrado del período de un planeta es proporcional al cubo del tamaño de su órbita. Hoy esa relación sigue sirviendo para estimar el período de cualquier objeto que orbita otro conocido.

📘 **Dónde se aprende** (1 clase): [B03-C04 · Potencias y raíces](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md).

### Cuadrante

- Un instrumento es un dispositivo para medir la posición del Sol, la Luna o las estrellas; un gnomon es una varilla vertical que proyecta sombra, y un cuadrante mide ángulos con un arco.

💡 **Cómo se explica en la clase [B02-C04](../programa/clases/B02/B02-C04-astronomia-de-india-china-y-mundo-islamico/CLASE.md):**
- Tenía un cuadrante mural de cobre de unos 4 m y un cuadrante azimutal inventado por al-Tusi, y una biblioteca con libros de muchas ciencias.
- 🎯 **Por qué importa:** Contar la historia de la astronomía como una línea recta de Grecia a Europa deja fuera lo que otras sociedades observaron, calcularon y construyeron. La pregunta motivadora es: ¿qué sabemos con precisión de estas tradiciones, qué falta y cómo evitar contar la historia desde un solo lado?

📘 **Dónde se aprende** (1 clase): [B02-C04 · Astronomía de India, China y mundo islámico](../programa/clases/B02/B02-C04-astronomia-de-india-china-y-mundo-islamico/CLASE.md).

### Cuadrática

- Una ecuación es lineal si la incógnita aparece solo a la primera potencia, y cuadrática si el mayor exponente es 2.

💡 **Cómo se explica en la clase [B04-C02](../programa/clases/B04/B04-C02-ecuaciones-lineales-y-cuadraticas/CLASE.md):**
- Para la cuadrática, piensa que `y = ax² + bx + c` dibuja una curva en forma de «U» (o «∩»), una parábola, y las raíces son los puntos donde corta el eje horizontal: dos, uno o ninguno.
- Su límite: en la cuadrática hay dos «pesos» que equilibran, no uno, y hay que decidir cuál es el real.
- 🎯 **Por qué importa:** Una sonda desciende hacia la Luna; un instrumento cae desde una mesa de trabajo; una señal de radio viaja hasta un espejo y vuelve. En cada caso hay un número que no conoces (un tiempo, una distancia) y una relación que lo liga a otros que sí conoces.

📘 **Dónde se aprende** (1 clase): [B04-C02 · Ecuaciones lineales y cuadráticas](../programa/clases/B04/B04-C02-ecuaciones-lineales-y-cuadraticas/CLASE.md).

### Cuadratura

- La cuadratura es una integral numérica.
- La cuadratura es la suma numérica de la integral.
- La cuadratura suma los cuadrados de los errores.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B26-C12](../programa/clases/B26/B26-C12-escalas-de-distancia-cosmologicas/CLASE.md):**
- El laboratorio genera `10⁵` distancias multiplicando tres factores aleatorios (gaussiano `1,2 %` y dos con `10^{0,2 g}`) y obtiene una desviación de `2,593 %`, a un `0,2 %` de la cuadratura.
- La incertidumbre sistemática (extinción, metalicidad) no entra en la cuadratura estadística.
- 🎯 **Por qué importa:** Una distancia con un error de `2,6 %` produce un `H₀` con un error similar, y la discusión actual sobre `H₀` gira alrededor de esas décimas de punto porcentual. Entender cómo se acumulan los errores en una cadena de pasos evita confiar en una cifra más de lo debido.

📘 **Dónde se aprende** (4 clases): [B26-C12 · Escalas de distancia cosmológicas](../programa/clases/B26/B26-C12-escalas-de-distancia-cosmologicas/CLASE.md); [B32-C06 · Micro y macroturbulencia y granulación estelar](../programa/clases/B32/B32-C06-micro-y-macroturbulencia-y-granulacion-estelar/CLASE.md); [B58-C09 · Probabilidades de impacto](../programa/clases/B58/B58-C09-probabilidades-de-impacto/CLASE.md); [B77-C19 · Seguridad de rango a nivel conceptual](../programa/clases/B77/B77-C19-seguridad-de-rango-a-nivel-conceptual/CLASE.md).

### Cuadro maestro

- El cuadro maestro combina muchos cuadros para reducir ruido.

💡 **Cómo se explica en la clase [B44-C12](../programa/clases/B44/B44-C12-calibracion-con-bias/CLASE.md):**
- La desviación de `cuadro − maestro` es `4,1182 ADU` (analítico `4 √(1 + 1/25) = 4,0792`) con media `+0,0190`.
- Con `N = 25` el maestro agrega solo un 2 % al ruido de un cuadro.
- ⚠️ **Error frecuente:** Usar pocos cuadros para el maestro. Se corrige con 8.3.
- 🎯 **Por qué importa:** Si el bias no se resta, el patrón fijo queda en la imagen. La decisión central: ¿cuántos cuadros se necesitan para que el maestro no añada ruido apreciable?

📘 **Dónde se aprende** (1 clase): [B44-C12 · Calibración con bias](../programa/clases/B44/B44-C12-calibracion-con-bias/CLASE.md).

### Cuádruple

- La cobertura simple es la fracción de tiempo con al menos un satélite visible; la cuádruple, con al menos cuatro.

💡 **Cómo se explica en la clase [B89-C17](../programa/clases/B89/B89-C17-constelaciones-y-cobertura/CLASE.md):**
- La cobertura global simple es `83,7 %` y la cuádruple `0,0 %`.
- Una constelación sintética 55°: 24/6/1 a 1200 km, con máscara de 10°, tiene una huella de semiángulo `24,03°`, `1,04` satélites visibles en promedio (teoría `1,04`), cobertura simple `83,7 %` y cuádruple `0,0 %`.
- 🎯 **Por qué importa:** El número de satélites, su altitud y la inclinación fijan cuánta gente o cuántos usuarios ven al menos uno (o cuatro, para navegar) y cuánto cuesta lograrlo. La decisión central: ¿cuántos satélites y qué geometría dan la cobertura necesaria?

📘 **Dónde se aprende** (1 clase): [B89-C17 · Constelaciones y cobertura](../programa/clases/B89/B89-C17-constelaciones-y-cobertura/CLASE.md).

### Cuadrupolo

- El cuadrupolo `ℓ = 2`.

💡 **Cómo se explica en la clase [B40-C15](../programa/clases/B40/B40-C15-varianza-cosmica-y-limites-de-las-mediciones-del-fondo/CLASE.md):**
- Calcular la probabilidad de un cuadrupolo bajo.
- Ejercicio 9 · transferencia. Transferencia. Un compañero dice que un cuadrupolo bajo prueba física nueva.
- 🎯 **Por qué importa:** La varianza cósmica es el límite fundamental de la medición del fondo. La decisión central: ¿qué precisión máxima permite el número de modos disponibles?

📘 **Dónde se aprende** (1 clase): [B40-C15 · Varianza cósmica y límites de las mediciones del fondo](../programa/clases/B40/B40-C15-varianza-cosmica-y-limites-de-las-mediciones-del-fondo/CLASE.md).

### Cualquier

- Un límite en dos variables exige que el valor sea el mismo por cualquier trayectoria.

🎯 **Por qué importa (clase B09-C15):** Una sonda que viaja de la Tierra a la Luna se mueve en un campo de potencial que depende de dos coordenadas del plano. Dónde están los puntos de equilibrio y qué forma tiene el campo alrededor de ellos se lee en un mapa de curvas de nivel.

📘 **Dónde se aprende** (1 clase): [B09-C15 · Funciones de varias variables](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md).

### Cuantía

- La cuantía es la cifra reclamada.

💡 **Cómo se explica en la clase [B123-C01](../programa/clases/B123/B123-C01-prueba-del-dano-y-cuantificacion-de-la-reparacion/CLASE.md):**
- Con los grados `0,95; 0,85; 0,60; 0,40`, la cuantía ponderada es `171 000 + 357 000 + 180 000 + 100 000 = 808 000` UMF.
- Si el costo de descontaminación varía de forma lognormal con sigma `0,25`, la cuantía ponderada tiene mediana `807 690` UMF y un intervalo P5–P95 de `747 588` a `900 205` UMF (20 000 sorteos, semilla 123).
- 🎯 **Por qué importa:** Un Estado puede tener derecho a reclamar y aun así perder o cobrar poco si no demuestra el daño o no lo cuantifica de forma defendible. La decisión central: ¿qué partidas puedo sostener con pruebas, por cuánto, en qué moneda y con qué margen de error?

📘 **Dónde se aprende** (1 clase): [B123-C01 · Prueba del daño y cuantificación de la reparación](../programa/clases/B123/B123-C01-prueba-del-dano-y-cuantificacion-de-la-reparacion/CLASE.md).

### Cuantil

- Un cuantil `q_α` cumple `F(q_α) = α`; la mediana es `q_0,5`.

💡 **Cómo se explica en la clase [B12-C02](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md):**
- El cuantil del 95 % cumple `F(q) = 0,95`: `(q + 2)/4 = 0,95`, `q = 1,8 m`.
- Los cuantiles son la forma natural de dar límites de aceptación.
- 🎯 **Por qué importa:** Casi nunca interesa *qué* resultado ocurrió, sino *un número* que resume el resultado: cuántos computadores funcionan, qué error tuvo una medición, cuántos fotones llegaron. Poner un número en cada resultado permite sumar, promediar y comparar.

📘 **Dónde se aprende** (1 clase): [B12-C02 · Variables aleatorias](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md).

### Cuantización

- La cuantización es el redondeo del ADC, con varianza `1/12 ADU²`.
- La cuantización reemplaza el valor por el nivel más cercano.
- La cuantización con pérdida.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B44-C06](../programa/clases/B44/B44-C06-ruido-de-lectura/CLASE.md):**
- La cuantización importa solo si el ruido es menor que unos `1 ADU`.
- Ejercicio 2 · con una pista. Cuantización de un ADC.
- ⚠️ **Error frecuente:** Ignorar la cuantización con ruido pequeño. Se corrige con 8.2.
- 🎯 **Por qué importa:** Sin conocer el ruido de lectura no se puede planificar una exposición ni estimar una incertidumbre. La decisión central: ¿cómo medirlo sin que el patrón fijo del sensor lo contamine?

📘 **Dónde se aprende** (9 clases): [B44-C06 · Ruido de lectura](../programa/clases/B44/B44-C06-ruido-de-lectura/CLASE.md); [B46-C09 · Conversión analógica digital](../programa/clases/B46/B46-C09-conversion-analogica-digital/CLASE.md); [B47-C16 · Compresión de datos científicos](../programa/clases/B47/B47-C16-compresion-de-datos-cientificos/CLASE.md); [B51-C12 · Formatos de datos VLBI y geodésicos](../programa/clases/B51/B51-C12-formatos-de-datos-vlbi-y-geodesicos/CLASE.md); [B57-C03 · Resolución radiométrica y espectral](../programa/clases/B57/B57-C03-resolucion-radiometrica-y-espectral/CLASE.md); [B85-C25 · Sensores y telemetría térmica](../programa/clases/B85/B85-C25-sensores-y-telemetria-termica/CLASE.md) y 3 más.

### Cuantización de Sheppard

- La cuantización de Sheppard `1/12` px².

🎯 **Por qué importa (clase B42-C14):** El Shack-Hartmann es el sensor más usado en óptica adaptativa. La decisión central: ¿cuántos fotones hacen falta por subapertura para que el centroide sea preciso?

📘 **Dónde se aprende** (1 clase): [B42-C14 · Sensores Shack-Hartmann](../programa/clases/B42/B42-C14-sensores-shack-hartmann/CLASE.md).

### Cuartos

- La luna nueva ocurre cuando la Luna está entre la Tierra y el Sol (no se ve el lado iluminado); la luna llena, cuando la Tierra está entre la Luna y el Sol; los cuartos, cuando el ángulo Sol–Tierra–Luna es de 90°.

💡 **Cómo se explica en la clase [B01-C12](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md):**
- N["Luna nueva: edad 0"] --> C1["Cuarto creciente: edad ≈ P/4"]
- LL --> C2["Cuarto menguante: edad ≈ 3P/4"]
- 🎯 **Por qué importa:** La Luna es el reloj más a mano del cielo: cada noche cambia, y cada 29,5 días vuelve a empezar. Pero «a mano» no significa «fácil de explicar»: muchas personas creen que las fases son la sombra de la Tierra sobre la Luna.

📘 **Dónde se aprende** (1 clase): [B01-C12 · Fases lunares y ciclos celestes](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md).

### Cuásar

- Un cuásar es un núcleo galáctico activo muy lejano; su movimiento propio esperado es despreciable (S1, cap. 2).

💡 **Cómo se explica en la clase [B13-C21](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md):**
- La IAU recomendó en 1991 que el origen del sistema celeste estuviera en el baricentro del sistema solar y que sus ejes fueran fijos respecto de los cuásares, con plano principal cercano al ecuador medio de J2000.0; en 1997 adoptó el ICRS, que reemplazó al FK5 el 1 de enero de 1998 (S1, cap. 2).
- Las coordenadas de cada cuásar son las marcas del mapa; los ejes salen de ellas.
- 🎯 **Por qué importa:** Para seguir una nave en el espacio profundo hay que decir en qué dirección está respecto de un marco fijo. Si el marco gira aunque sea un poco, todas las direcciones se desplazan.

📘 **Dónde se aprende** (1 clase): [B13-C21 · Sistema de referencia celeste ICRF y cuásares](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md).

### Cuasiespecie

- Una cuasiespecie es la nube de mutantes alrededor de la maestra.

💡 **Cómo se explica en la clase [B56-C03](../programa/clases/B56/B56-C03-origen-de-moleculas-autorreplicantes/CLASE.md):**
- Cuasiespecie completa: resuelve una matriz de mutación; más realista, costosa.
- 🎯 **Por qué importa:** Un replicador que copia mal pierde su información; uno que copia bien necesita una maquinaria que, sin vida previa, aún no existe. Esa tensión limita el tamaño de los primeros genomas.

📘 **Dónde se aprende** (1 clase): [B56-C03 · Origen de moléculas autorreplicantes](../programa/clases/B56/B56-C03-origen-de-moleculas-autorreplicantes/CLASE.md).

### Cuasi-identificador

- El cuasi-identificador combina atributos.

💡 **Cómo se explica en la clase [B105-C19](../programa/clases/B105/B105-C19-bioetica-en-investigacion-tripulada/CLASE.md):**
- Descripción: la salida con la unicidad por esquema de cuasi-identificadores y el error de Laplace por `ε`.
- Medir cómo la generalización de los cuasi-identificadores reduce la unicidad.
- ⚠️ **Error frecuente:** Creer que quitar el nombre anonimiza. Los cuasi-identificadores reidentifican (8.2).
- 🎯 **Por qué importa:** No basta con quitar el nombre: con edad, sexo, profesión y misión, una persona de una cohorte de 6 suele ser única. La decisión central: ¿qué se puede publicar de una cohorte pequeña sin identificar a nadie y cuánta utilidad se pierde al protegerla?

📘 **Dónde se aprende** (1 clase): [B105-C19 · Bioética en investigación tripulada](../programa/clases/B105/B105-C19-bioetica-en-investigacion-tripulada/CLASE.md).

### Cuasi-isótropo

- Un laminado cuasi-isótropo tiene `A` isótropa en el plano.

💡 **Cómo se explica en la clase [B84-C03](../programa/clases/B84/B84-C03-materiales-compuestos/CLASE.md):**
- El cuasi-isótropo pierde 61 % del módulo longitudinal del UD y gana igualdad en todas las direcciones.
- En el cuasi-isótropo `|A₁₁ − A₂₂|/A₁₁ = 0` y `|A₆₆ − (A₁₁ − A₁₂)/2|/A₆₆ = 3,6 × 10⁻¹⁶`, y `E = 54,07 GPa`, `ν = 0,311` dan `G = 20,62 GPa`, igual a `A₆₆/h`.
- 🎯 **Por qué importa:** Un panel de fibra con las capas mal orientadas puede ser 14 veces más blando en una dirección que en otra sin que el material cambie. La decisión central: ¿cómo cambia la rigidez efectiva de un laminado según el ángulo de sus capas?

📘 **Dónde se aprende** (1 clase): [B84-C03 · Materiales compuestos](../programa/clases/B84/B84-C03-materiales-compuestos/CLASE.md).

### Cuasineutralidad

- La cuasineutralidad es la neutralidad a escalas mayores que `λ_D`.

🎯 **Por qué importa (clase B30-C07):** Sin apantallamiento no hay plasma, y sin muchas partículas en la esfera de Debye no hay comportamiento colectivo. La decisión central: ¿cuándo un gas ionizado es un plasma?

📘 **Dónde se aprende** (1 clase): [B30-C07 · Longitud de Debye y plasma](../programa/clases/B30/B30-C07-longitud-de-debye-y-plasma/CLASE.md).

### Cuasi-satélite

- El ángulo coorbital `θ = λ_part − λ_Tierra` (sin envolver) distingue: tadpole (`θ` oscila alrededor de `±60°` sin cruzar `0` ni `π`), herradura (`θ` cubre `π` sin cruzar `0` ni `2π`) y cuasi-satélite (`θ` oscila alrededor de `0` con una amplitud pequeña y la partícula se mantiene a unos pocos `R_H`).

💡 **Cómo se explica en la clase [B73-C22](../programa/clases/B73/B73-C22-capturas-temporales-y-cuasi-satelites/CLASE.md):**
- El caso `e = 0,02` se acerca a `0,04 R_H` de la Tierra, es dispersado y sale de la coorbitalidad: no todo estado inicial parecido a un cuasi-satélite lo es.
- Un cuasi-satélite no es un satélite: `θ` libra alrededor de `0` pero la partícula orbita al Sol en un año con `a ≈ 1`; su distancia a la Tierra (`4,7–11,7 R_H`) la deja fuera de la esfera de Hill.
- ⚠️ **Error frecuente:** Tomar un cuasi-satélite por un satélite. Se corrige con 8.5.
- 🎯 **Por qué importa:** Un asteroide puede acompañar a la Tierra durante siglos sin orbitarla: dando vueltas alrededor de L4 (tadpole), de L3–L4–L5 (herradura) o de la propia Tierra (cuasi-satélite); y puede ser capturado temporalmente dentro de su esfera de Hill. Distinguirlos requiere una clasificación operativa y una advertencia: no son satélites.

📘 **Dónde se aprende** (1 clase): [B73-C22 · Capturas temporales y cuasi-satélites](../programa/clases/B73/B73-C22-capturas-temporales-y-cuasi-satelites/CLASE.md).

### Cuaternión

- Un cuaternión es `q = (q₀, q₁, q₂, q₃) = q₀ + q₁ i + q₂ j + q₃ k` con `i² = j² = k² = ijk = −1`.
- El cuaternión `q = (w, x, y, z)` rota del cuerpo al marco de navegación.
- El cuaternión `q = [qv; qw]` tiene norma 1.

💡 **Cómo se explica en la clase [B10-C15](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md):**
- Un cuaternión unitario tiene tres grados de libertad reales (cuatro números, una restricción de norma), igual que una rotación.
- El ángulo del cuaternión es la mitad del de la rotación: `θ = 2 arccos q₀`.
- 🎯 **Por qué importa:** Un seguidor estelar entrega la actitud del satélite varias veces por segundo; el sistema de control la combina con las lecturas de giróscopos, la propaga y la compara con la actitud deseada. Hacerlo con ángulos de Euler es frágil; hacerlo con matrices cuesta más y acumula deriva.

📘 **Dónde se aprende** (3 clases): [B10-C15 · Cuaterniones unitarios](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md); [B80-C03 · Mecanización strapdown e integración de actitud y velocidad](../programa/clases/B80/B80-C03-mecanizacion-strapdown-e-integracion-de-actitud-y-velocidad/CLASE.md); [B87-C02 · Representaciones de orientación](../programa/clases/B87/B87-C02-representaciones-de-orientacion/CLASE.md).

### Cuaternión de error

- El cuaternión de error es `q_e = q_obj⁻¹ ⊗ q`; vale `[1, 0, 0, 0]` (o su opuesto) cuando la orientación alcanzó el objetivo.

💡 **Cómo se explica en la clase [B16-C20](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md):**
- *Descripción textual:* se calcula el cuaternión de error entre la orientación y el objetivo; si su escalar es no negativo se aplica la ley normal, y si es negativo se invierte el signo de la parte proporcional para tomar el camino corto; el par actúa sobre el cuerpo cuya orientación realimenta el error.
- Un error de implementación (un signo, el orden del producto de cuaterniones, una convención) o un paso de integración demasiado grande, pues con 0,02 rad la diferencia entre lineal y no lineal debe ser del orden del cuadrado (4×10⁻⁴ relativo), muy por debajo de 10⁻².
- 🎯 **Por qué importa:** Un telescopio debe girar desde una orientación a otra y quedarse allí. Con tres ejes acoplados y rotaciones grandes, ni los ángulos de Euler (tienen singularidades y dependen de la secuencia de giros) ni el modelo lineal bastan.

📘 **Dónde se aprende** (1 clase): [B16-C20 · Control de orientación en un simulador](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md).

### Cuaternión puro

- Un cuaternión puro `(0, v)` representa un vector.

🎯 **Por qué importa (clase B10-C15):** Un seguidor estelar entrega la actitud del satélite varias veces por segundo; el sistema de control la combina con las lecturas de giróscopos, la propaga y la compara con la actitud deseada. Hacerlo con ángulos de Euler es frágil; hacerlo con matrices cuesta más y acumula deriva.

📘 **Dónde se aprende** (1 clase): [B10-C15 · Cuaterniones unitarios](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md).

### Cuaternión unitario

- Un cuaternión unitario `q = [q0, q_v]` (escalar primero, `q_v` de tres componentes) con `q0² + |q_v|² = 1` representa una rotación; usamos la convención de que lleva componentes del sistema inercial al del cuerpo.

💡 **Cómo se explica en la clase [B16-C20](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md):**
- El espacio de cuaterniones unitarios recubre dos veces el de las orientaciones: cada orientación tiene dos representaciones, `q` y `−q`.
- Usar un cuaternión unitario para representar y componer orientaciones.
- 🎯 **Por qué importa:** Un telescopio debe girar desde una orientación a otra y quedarse allí. Con tres ejes acoplados y rotaciones grandes, ni los ángulos de Euler (tienen singularidades y dependen de la secuencia de giros) ni el modelo lineal bastan.

📘 **Dónde se aprende** (1 clase): [B16-C20 · Control de orientación en un simulador](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md).

### CubeSat 3U

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C25](../programa/clases/B47/B47-C25-diseno-de-cargas-utiles-educativas/CLASE.md):**
- La matriz es un ejemplo de método: los umbrales son ilustrativos y no provienen de ninguna convocatoria ni estándar de CubeSat.
- 🎯 **Por qué importa:** Muchos CubeSat universitarios fracasan por requisitos sin cifra o sin evidencia. La decisión central: ¿qué requisitos medibles se fijan, cómo se verifican y cuáles cumple un diseño preliminar?

📘 **Dónde se aprende** (1 clase): [B47-C25 · Diseño de cargas útiles educativas](../programa/clases/B47/B47-C25-diseno-de-cargas-utiles-educativas/CLASE.md).

### Cubierta

- Regolito: material suelto de la superficie. Cubierta: capa de regolito sobre el habitat.

💡 **Cómo se explica en la clase [B106-C19](../programa/clases/B106/B106-C19-arquitectura-de-asentamiento-lunar-conceptual/CLASE.md):**
- V["cubierta 3 m"] --> X["excavacion y blindaje"]
- *Descripción textual:* la noche fija la energía almacenada; la gravedad baja la presión que ejerce el regolito, de modo que el casco sostiene la presión interior y la cubierta se reserva para blindaje y estabilidad térmica.
- 🎯 **Por qué importa:** La Luna cambia las reglas: noches de dos semanas, gravedad de un sexto y un regolito que protege pero no contiene la presión. La decisión central: ¿qué recursos (energía, masa de cubierta, esfuerzo de excavación) exige un asentamiento enterrado y qué parte soporta cada elemento?

📘 **Dónde se aprende** (1 clase): [B106-C19 · Arquitectura de asentamiento lunar conceptual](../programa/clases/B106/B106-C19-arquitectura-de-asentamiento-lunar-conceptual/CLASE.md).

### Cubo

- El cuadrado de `a` es `a²`; el cubo, `a³`.

💡 **Cómo se explica en la clase [B03-C04](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md):**
- Y `a^(3/2) = (√a)³ = √(a³)`: primero raíz y luego cubo, o al revés.
- Un cuadrado de lado 3 se llena con `3 × 3 = 9` casillas; un cubo de arista 3, con `3 × 3 × 3 = 27` cajas.
- 🎯 **Por qué importa:** En 1619 Johannes Kepler publicó que el cuadrado del período de un planeta es proporcional al cubo del tamaño de su órbita. Hoy esa relación sigue sirviendo para estimar el período de cualquier objeto que orbita otro conocido.

📘 **Dónde se aprende** (1 clase): [B03-C04 · Potencias y raíces](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md).

### Cubo de fichas

- El cubo de fichas tiene capacidad `B` y se rellena a `r` fichas por segundo; cada evento gasta una.

💡 **Cómo se explica en la clase [B88-C10](../programa/clases/B88/B88-C10-gestion-de-eventos/CLASE.md):**
- *Descripción textual:* un evento crítico se registra siempre; uno no crítico solo si el cubo de su identificador tiene una ficha; si no, se suprime y se cuenta.
- El script [eventos.py](eventos.py) genera 1026 eventos con semilla 10, aplica un cubo de fichas por identificador y comprueba que se suprimen 978 del parpadeo y no se suprime ningún crítico.
- 🎯 **Por qué importa:** Un sensor que parpadea puede generar miles de eventos y saturar el registro y el enlace, ocultando el único evento importante. La decisión central: ¿cómo se limita el ruido sin perder lo crítico?

📘 **Dónde se aprende** (1 clase): [B88-C10 · Gestión de eventos](../programa/clases/B88/B88-C10-gestion-de-eventos/CLASE.md).

### Cubo hiperespectral

- El cubo hiperespectral tiene dos dimensiones espaciales y una espectral.

💡 **Cómo se explica en la clase [B57-C22](../programa/clases/B57/B57-C22-espectrometros-de-imagen-e-hiperespectrales/CLASE.md):**
- Describir un cubo hiperespectral y su flujo de datos.
- 🎯 **Por qué importa:** Dos materiales distintos pueden parecer iguales en cuatro bandas anchas y diferenciarse en cientos de bandas estrechas. La decisión central: ¿cuándo vale la pena el costo en datos de un sensor hiperespectral y cómo se separa una mezcla de materiales?

📘 **Dónde se aprende** (1 clase): [B57-C22 · Espectrómetros de imagen e hiperespectrales](../programa/clases/B57/B57-C22-espectrometros-de-imagen-e-hiperespectrales/CLASE.md).

### Cuello

- El cuello es la zona de unión entre dos partículas y `x/a` su razón.
- Un cuello está abierto si `C ≤ C(Li)`.

💡 **Cómo se explica en la clase [B59-C12](../programa/clases/B59/B59-C12-sinterizacion-de-materiales/CLASE.md):**
- Como miel que se espesa al enfriarse: a baja temperatura casi no fluye y el cuello crece muy despacio.
- Límite: la ley de Frenkel supone flujo viscoso newtoniano y cuellos pequeños; el regolito real puede cristalizar.
- ⚠️ **Error frecuente:** Extrapolar Frenkel a cuellos grandes. Se corrige con la sección 14.
- 🎯 **Por qué importa:** Una variación de 50 K en el horno cambia el tiempo de sinterización en un factor 2,6. La decisión central: ¿con qué precisión hay que controlar la temperatura, y cuánta energía cuesta alcanzarla?

📘 **Dónde se aprende** (2 clases): [B59-C12 · Sinterización de materiales](../programa/clases/B59/B59-C12-sinterizacion-de-materiales/CLASE.md); [B76-C08 · Transferencias de baja energía](../programa/clases/B76/B76-C08-transferencias-de-baja-energia/CLASE.md).

### Cuello de botella

- Un cuello de botella es la parte que domina el tiempo.
- Un cuello de botella es la parte que fija el tiempo total.
- El cuello de botella es el eslabón de menor capacidad.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C14](../programa/clases/B14/B14-C14-vectorizacion-y-rendimiento/CLASE.md):**
- Y si el cuello de botella es leer un archivo (C06–C07), vectorizar el cálculo no cambia nada.
- Optimizar es un ciclo de cuatro pasos y el orden importa: medir el tiempo actual, localizar el cuello de botella, cambiar solo eso y verificar que el resultado no cambió y que el tiempo bajó.
- 🎯 **Por qué importa:** Una función que calcula la distancia de 200 000 posiciones tarda medio minuto en tu cuaderno, y alguien propone «comprar un servidor». La pregunta motivadora es: ¿es el cálculo lento por su matemática o por cómo lo escribí, y cuánto puedo ganar sin cambiar el resultado?

📘 **Dónde se aprende** (7 clases): [B14-C14 · Vectorización y rendimiento](../programa/clases/B14/B14-C14-vectorizacion-y-rendimiento/CLASE.md); [B18-C04 · Perfilado de rendimiento](../programa/clases/B18/B18-C04-perfilado-de-rendimiento/CLASE.md); [B89-C20 · Diseño de red de comunicaciones de misión](../programa/clases/B89/B89-C20-diseno-de-red-de-comunicaciones-de-mision/CLASE.md); [B97-C27 · Simulación de productividad de flotas de maquinaria](../programa/clases/B97/B97-C27-simulacion-de-productividad-de-flotas-de-maquinaria/CLASE.md); [B110-C03 · Evacuación y refugio de emergencia](../programa/clases/B110/B110-C03-evacuacion-y-refugio-de-emergencia/CLASE.md); [B114-C01 · Rutas de evacuación y salidas de emergencia en hábitats](../programa/clases/B114/B114-C01-rutas-de-evacuacion-y-salidas-de-emergencia-en-habitats/CLASE.md) y 1 más.

### Cuello de botella del deuterio

- El cuello de botella del deuterio es el retraso hasta que el deuterio deja de fotodisociarse.

💡 **Cómo se explica en la clase [B26-C16](../programa/clases/B26/B26-C16-nucleosintesis-primordial/CLASE.md):**
- Estimar la temperatura del cuello de botella del deuterio.
- cuello de botella del deuterio: kT ~ B_d / ln(1/eta) = 2.2246/21.22 = 0.1048 MeV = 1.217e+09 K (orden de magnitud)
- 🎯 **Por qué importa:** La cuarta parte de la masa bariónica del universo es helio, y la proporción casi no cambió desde los primeros minutos. Su valor da información sobre cuántas especies de neutrinos existen y sobre la densidad de bariones.

📘 **Dónde se aprende** (1 clase): [B26-C16 · Nucleosíntesis primordial](../programa/clases/B26/B26-C16-nucleosintesis-primordial/CLASE.md).

### Cuenca multianillo

- Una cuenca multianillo tiene varios anillos concéntricos.

💡 **Cómo se explica en la clase [B61-C07](../programa/clases/B61/B61-C07-cuencas-multianillo-y-grandes-impactos/CLASE.md):**
- La evidencia es la ficha de la cuenca multianillo del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *ficha de la cuenca multianillo*: la recurrencia de anillos, su contraste con √2, la estimación de `c`, la energía inferida y su incertidumbre, con rótulos de lo sintético.
- 🎯 **Por qué importa:** Las cuencas dejan huella en la corteza entera. La decisión central: ¿cómo se espacian los anillos, qué proyectil implica una cuenca y cuándo excava hasta el manto?

📘 **Dónde se aprende** (1 clase): [B61-C07 · Cuencas multianillo y grandes impactos](../programa/clases/B61/B61-C07-cuencas-multianillo-y-grandes-impactos/CLASE.md).

### Cuenta

- La cuenta `N = f/(presc)·Δt`.
- Parámetro: una magnitud con nombre, unidad y límites. Cuenta: valor entero del conversor.

💡 **Cómo se explica en la clase [B88-C02](../programa/clases/B88/B88-C02-microcontroladores-embarcados/CLASE.md):**
- Límite: los engranajes reales no tienen error de redondeo en cuentas enteras.
- Paso 1 · Cuenta. `16·10⁶/64 · 10⁻³ = 250`.
- 🎯 **Por qué importa:** Un error de configuración (un divisor mal calculado, una resolución insuficiente) no se ve en el escritorio y aparece en órbita. La decisión central: ¿qué valores de registro dan la temporización, la velocidad y la resolución que exige el requisito, con qué error?

📘 **Dónde se aprende** (2 clases): [B88-C02 · Microcontroladores embarcados](../programa/clases/B88/B88-C02-microcontroladores-embarcados/CLASE.md); [B96-C06 · Telemetría operativa](../programa/clases/B96/B96-C06-telemetria-operativa/CLASE.md).

### Cuenta continua

- La cuenta continua es una numeración de segundos sin saltos (aquí desde 1972-01-01 00:00:00 UTC, basada en TAI).

💡 **Cómo se explica en la clase [B13-C09](../programa/clases/B13/B13-C09-segundos-intercalares-y-cronologia/CLASE.md):**
- La cuenta continua es la regla uniforme.
- C --> D["Cuenta continua<br/>de segundos"]
- 🎯 **Por qué importa:** Una nave graba un evento a las `23:59:59` del 31 de diciembre de 2016 y otro a las `00:00:00` del 1 de enero de 2017. ¿Cuánto tiempo pasó?

📘 **Dónde se aprende** (1 clase): [B13-C09 · Segundos intercalares y cronología](../programa/clases/B13/B13-C09-segundos-intercalares-y-cronologia/CLASE.md).

### Cuenta de arranques

- La cuenta de arranques limita los intentos.

💡 **Cómo se explica en la clase [B88-C13](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md):**
- Tras el cambio, el cargador cuenta los arranques.
- 🎯 **Por qué importa:** Una actualización fallida en órbita no se arregla con un cable. La decisión central: ¿qué comprobaciones aceptan solo la imagen correcta y qué mecanismo vuelve a una versión conocida si la nueva no arranca?

📘 **Dónde se aprende** (1 clase): [B88-C13 · Actualización segura de software](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md).

### Cuenta de Coulomb

- La cuenta de Coulomb integra la corriente.

💡 **Cómo se explica en la clase [B86-C06](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md):**
- Simular la carga con cuenta de Coulomb y una OCV con resistencia interna.
- 🎯 **Por qué importa:** Cargar más rápido reduce el tiempo pero eleva el calor y la tensión sobre la celda; cargar más lento puede no completar el ciclo antes del siguiente eclipse. El perfil de carga decide si la batería vuelve a su estado de carga en cada órbita.

📘 **Dónde se aprende** (1 clase): [B86-C06 · Gestión de carga](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md).

### Cuenta integrada

- La cuenta integrada acumula ciclos de Doppler y da la variación de alcance.

🎯 **Por qué importa (clase B74-C04):** Una velocidad radial de `1 mm/s` produce un desplazamiento de decenas de milihercios, medible; por eso el Doppler es el observable más preciso de la navegación en espacio profundo. La decisión central: ¿qué información da el Doppler (velocidad en la línea de visión) y qué no (posición transversal)?

📘 **Dónde se aprende** (1 clase): [B74-C04 · Doppler de navegación](../programa/clases/B74/B74-C04-doppler-de-navegacion/CLASE.md).

### Cuenta regresiva

- Una cuenta regresiva usa T− antes de un instante de referencia y T+ después.

💡 **Cómo se explica en la clase [B03-C09](../programa/clases/B03/B03-C09-operaciones-con-numeros-negativos/CLASE.md):**
- La cuenta regresiva es una recta de tiempo con signos.
- Datos: publicados (NASA, IAU, SI); la cuenta regresiva es sintética.
- 🎯 **Por qué importa:** Cuando observas una llamarada solar a las 12:00:00, el evento ocurrió antes: su tiempo es el observado menos 499 s. Si sumas en vez de restar, afirmas que la llamarada ocurre en el futuro.

📘 **Dónde se aprende** (1 clase): [B03-C09 · Operaciones con números negativos](../programa/clases/B03/B03-C09-operaciones-con-numeros-negativos/CLASE.md).

### Cuentas

- Las cuentas son el número de partículas por canal.
- La línea del disco y las cuentas `4 × líneas`.

💡 **Cómo se explica en la clase [B35-C06](../programa/clases/B35/B35-C06-mediciones-in-situ-de-plasmas-espaciales/CLASE.md):**
- Con `σ = 28,730 km/s` y bins de `5,746 km/s`, 300 realizaciones de 20 000 cuentas dan: `V − V₀ = −11,9 m/s` (error estándar `11,6`), dispersión de `V` de `201,7 m/s` frente a `σ/√N = 203,2 m/s`, `T` media `100 078 K` con sesgo `78 K` (error estándar `53 K`) y dispersión `913 K` frente a `T√(2/N) = 1000 K`.
- El ruido de Poisson se controla con más cuentas (`σ_V ∝ 1/√N`).
- ⚠️ **Error frecuente:** Creer que más cuentas quitan el sesgo. Se corrige con 8.4.
- 🎯 **Por qué importa:** Un momento sin su incertidumbre ni sus sesgos no es una medición. La decisión central: ¿cuántas cuentas hacen falta y qué sesgos introduce el instrumento?

📘 **Dónde se aprende** (2 clases): [B35-C06 · Mediciones in situ de plasmas espaciales](../programa/clases/B35/B35-C06-mediciones-in-situ-de-plasmas-espaciales/CLASE.md); [B43-C16 · Encoders y medición angular](../programa/clases/B43/B43-C16-encoders-y-medicion-angular/CLASE.md).

### Cuerda

- La cuerda entre dos puntos de la esfera unidad es la longitud del segmento que los une, `|u − v|`; se relaciona con el ángulo por `|u − v| = 2 sen(γ/2)`.
- La cuerda `c` es la distancia entre los dos puntos y el semiperímetro `s = (r₁ + r₂ + c)/2`.
- La cuerda `c = |r2 − r1|`.

💡 **Cómo se explica en la clase [B04-C13](../programa/clases/B04/B04-C13-producto-escalar-y-angulo-entre-vectores/CLASE.md):**
- La fórmula por cuerda, `γ = 2 arcsen(|u − v|/2)`, no resta números casi iguales y da `1,000000 × 10⁻³″` en esos casos.
- Regla de la clase: usar la forma por cuerda cuando `γ` sea menor de unos minutos de arco.
- 🎯 **Por qué importa:** Antes de apuntar un telescopio de una estrella a otra, antes de saber si dos objetos caben en el mismo campo de visión, antes de decidir si un planeta está demasiado cerca del Sol para observarlo, hay que saber cuántos grados los separan en el cielo.

📘 **Dónde se aprende** (3 clases): [B04-C13 · Producto escalar y ángulo entre vectores](../programa/clases/B04/B04-C13-producto-escalar-y-angulo-entre-vectores/CLASE.md); [B75-C04 · Ecuación de Lambert](../programa/clases/B75/B75-C04-ecuacion-de-lambert/CLASE.md); [B82-C01 · Lambert de arco corto](../programa/clases/B82/B82-C01-lambert-de-arco-corto/CLASE.md).

### Cuerpo celeste

- Un cuerpo celeste incluye la Luna.

💡 **Cómo se explica en la clase [B119-C11](../programa/clases/B119/B119-C11-uso-pacifico-y-limitaciones-militares/CLASE.md):**
- *Descripción textual:* primero se pregunta por armas de destrucción masiva; luego por el cuerpo celeste; por último por bases o ensayos; el resultado puede ser prohibido, condicionado, permitido o fuera del artículo.
- Paso 1. `loc = cuerpo celeste`, `wmd = 0`, `inst = 0`, `pers = 1`.
- 🎯 **Por qué importa:** C01 reduce el art. IV a una regla booleana; esta clase lo desagrega por ubicación y propósito y conecta con el art. 3 del Acuerdo sobre la Luna, y deja explícito lo no consultado.

📘 **Dónde se aprende** (1 clase): [B119-C11 · Uso pacífico y limitaciones militares](../programa/clases/B119/B119-C11-uso-pacifico-y-limitaciones-militares/CLASE.md).

### Cuerpo gris

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C04](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md):**
- Cuerpo gris con emisividad constante, sin fondo zodiacal ni emisión del cielo residual.
- Límites: cuerpo gris, sin fondo zodiacal.
- 🎯 **Por qué importa:** Enfriar un telescopio cuesta masa, potencia y complejidad. La decisión central: ¿a qué temperatura el fondo propio deja de dominar sobre el detector?

📘 **Dónde se aprende** (1 clase): [B47-C04 · Telescopios infrarrojos](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md).

### Cuerpo menor

- Un cuerpo menor es un asteroide o cometa.

💡 **Cómo se explica en la clase [B58-C01](../programa/clases/B58/B58-C01-clasificacion-de-cuerpos-menores/CLASE.md):**
- python programa/clases/B58/B58-C01-clasificacion-de-cuerpos-menores/clasificacion.py
- 🎯 **Por qué importa:** La pregunta que organiza el bloque es *¿qué es este objeto y qué tan cerca pasa?* Un mismo punto de luz puede ser un asteroide del cinturón principal sin ningún interés para la defensa planetaria o un objeto cercano a la Tierra.

📘 **Dónde se aprende** (1 clase): [B58-C01 · Clasificación de cuerpos menores](../programa/clases/B58/B58-C01-clasificacion-de-cuerpos-menores/CLASE.md).

### Cuerpo menor del sistema solar

- Un cuerpo menor del sistema solar es cualquier otro objeto que orbita el Sol y no es satélite (la IAU incluye a la mayoría de los asteroides, la mayoría de los objetos transneptunianos y los cometas).

💡 **Cómo se explica en la clase [B01-C03](../programa/clases/B01/B01-C03-objetos-celestes-y-sus-diferencias/CLASE.md):**
- Aplicar los tres criterios de la IAU de 2006 para clasificar un cuerpo del sistema solar como planeta, planeta enano o cuerpo menor.
- Cometa: orbita el Sol, no es casi redondo → cuerpo menor del sistema solar (nota 3 de la B5: los cometas son cuerpos menores).
- 🎯 **Por qué importa:** En 2006 la Asamblea General de la Unión Astronómica Internacional votó una definición de planeta y, desde entonces, Plutón dejó de contarse como el noveno planeta. Muchas personas sintieron que «se había cambiado la realidad».

📘 **Dónde se aprende** (1 clase): [B01-C03 · Objetos celestes y sus diferencias](../programa/clases/B01/B01-C03-objetos-celestes-y-sus-diferencias/CLASE.md).

### Cuerpo negro

- Un cuerpo negro es un emisor ideal cuyo espectro depende solo de su temperatura.
- Un cuerpo negro es un emisor ideal cuyo espectro depende solo de `T`.
- Un cuerpo negro absorbe toda la radiación incidente y emite según `P = σ A T⁴`, con `σ = 5,670 374 419… × 10⁻⁸ W/(m²·K⁴)` (S4).
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C09](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md):**
- Y el cuerpo negro es una aproximación: las estrellas tienen líneas y la temperatura de Wien es solo una estimación del color dominante.
- Sentido físico. La luz permitió identificar un patrón, medir un corrimiento y estimar una temperatura, con tres supuestos declarados: líneas bien identificadas, corrimiento común, cuerpo negro.
- 🎯 **Por qué importa:** Sobre una galaxia a 43 Mpc solo tienes luz. De esa luz sale su dirección, cuánto brilla, de qué color es y qué líneas aparecen en su espectro; de las líneas sale `z = 0,0101` (C01).

📖 **Explicado a fondo:** [Cuerpo negro](esencial/esencial-a-c.md#cuerpo-negro) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (5 clases): [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B05-C13 · Temperatura y energía térmica](../programa/clases/B05/B05-C13-temperatura-y-energia-termica/CLASE.md); [B13-C17 · Calibración radiométrica](../programa/clases/B13/B13-C17-calibracion-radiometrica/CLASE.md); [B22-C04 · Inversión espectral](../programa/clases/B22/B22-C04-inversion-espectral/CLASE.md); [B28-C02 · Fotones en múltiples longitudes de onda](../programa/clases/B28/B28-C02-fotones-en-multiples-longitudes-de-onda/CLASE.md).

### Cuerpo rígido

- Un cuerpo rígido tiene un único `Ω`.

💡 **Cómo se explica en la clase [B37-C11](../programa/clases/B37/B37-C11-rotacion-interna-a-partir-del-desdoblamiento-de-frecuencias/CLASE.md):**
- Un cuerpo rígido (`0,25 μHz` en todos los modos) recupera `Ω_c = Ω_e = 0,250000`.
- cuerpo rigido (0,25 uHz en todos los modos): Omega_c = 0.250000 ;
- 🎯 **Por qué importa:** El desdoblamiento promedia la rotación de las regiones que el modo explora. La decisión central: ¿cuánto giran el núcleo y la envoltura y con qué incertidumbre y correlación?

📘 **Dónde se aprende** (1 clase): [B37-C11 · Rotación interna a partir del desdoblamiento de frecuencias](../programa/clases/B37/B37-C11-rotacion-interna-a-partir-del-desdoblamiento-de-frecuencias/CLASE.md).

### Culminación

- La culminación es el paso por el meridiano, el punto más alto del día.
- El ángulo horario `H` es el ángulo, medido hacia el oeste, entre el meridiano y el círculo que pasa por el astro y los polos; vale cero cuando el astro cruza el meridiano (tránsito o culminación, S2).
- La culminación (o tránsito meridiano) es el momento en que el astro cruza el meridiano, con `H = 0`.

💡 **Cómo se explica en la clase [B08-C04](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md):**
- Predecir cuándo un objeto sale, culmina y se pone.
- Ejercicio 1. ¿A qué altura culmina un astro de `δ = −45°` desde `φ = −30°`?
- 🎯 **Por qué importa:** Una tabla dice «Luna: AR 2,14 h, Dec +17,1°». Un telescopio, una cámara o tus ojos necesitan «a 35° de altura, hacia el nornoreste».

📘 **Dónde se aprende** (3 clases): [B01-C11 · Movimiento aparente del Sol y las estrellas](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md); [B08-C04 · Altura y acimut](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md); [B09-C05 · Derivadas trigonométricas](../programa/clases/B09/B09-C05-derivadas-trigonometricas/CLASE.md).

### Cultura de seguridad

- La cultura de seguridad son las actitudes y prácticas compartidas sobre el riesgo.
- La cultura de seguridad se modela como un factor `r` que aumenta la tasa de reporte.

💡 **Cómo se explica en la clase [B111-C06](../programa/clases/B111/B111-C06-gestion-del-error-humano-y-cultura-de-seguridad/CLASE.md):**
- Pero las cifras son sintéticas, el modelo no distingue tipos de daño y la cultura de seguridad real no se reduce a un factor `r`.
- De 1000 casi-eventos se reportan `395` con las tasas sintéticas y `592,5` si una cultura de seguridad las multiplica por `1,5`.
- 🎯 **Por qué importa:** Falta la clase sobre tipos de error, barreras y reporte. La decisión central: ¿dónde se pone el esfuerzo: en culpar al que erró o en reforzar las barreras y las condiciones que dejaron pasar el error?

📘 **Dónde se aprende** (2 clases): [B111-C06 · Gestión del error humano y cultura de seguridad](../programa/clases/B111/B111-C06-gestion-del-error-humano-y-cultura-de-seguridad/CLASE.md); [B119-C21 · Cultura de seguridad aeroespacial y aprendizaje de incidentes](../programa/clases/B119/B119-C21-cultura-de-seguridad-aeroespacial-y-aprendizaje-de-incidentes/CLASE.md).

### Cultura justa

- Una cultura justa protege el reporte honesto.

🎯 **Por qué importa (clase B119-C21):** B88-C16 cubre la seguridad funcional técnica; ninguna clase trata la dimensión cultural, y los indicadores de reportes se malinterpretan con facilidad. La decisión central: ¿qué indicador permite saber si una organización aprende cuando los reportes dependen de la confianza para informar?

📘 **Dónde se aprende** (1 clase): [B119-C21 · Cultura de seguridad aeroespacial y aprendizaje de incidentes](../programa/clases/B119/B119-C21-cultura-de-seguridad-aeroespacial-y-aprendizaje-de-incidentes/CLASE.md).

### Cúmulo

- Un grupo de galaxias tiene unas cien o menos; un cúmulo puede contener miles (S3).
- Un grupo de galaxias reúne típicamente cien o menos (S1); un cúmulo, hasta miles (S1).

💡 **Cómo se explica en la clase [B01-C03](../programa/clases/B01/B01-C03-objetos-celestes-y-sus-diferencias/CLASE.md):**
- Un grupo reúne a unas cien galaxias o menos (la Vía Láctea y Andrómeda pertenecen al Grupo Local, con más de 50 galaxias), y un cúmulo puede reunir miles, como el de Virgo de C02 (S3).
- Los planetas orbitan estrellas; las estrellas forman galaxias; las galaxias forman grupos y cúmulos.
- 🎯 **Por qué importa:** En 2006 la Asamblea General de la Unión Astronómica Internacional votó una definición de planeta y, desde entonces, Plutón dejó de contarse como el noveno planeta. Muchas personas sintieron que «se había cambiado la realidad».

📘 **Dónde se aprende** (2 clases): [B01-C03 · Objetos celestes y sus diferencias](../programa/clases/B01/B01-C03-objetos-celestes-y-sus-diferencias/CLASE.md); [B01-C15 · Galaxias y agrupaciones cósmicas](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md).

### Cúmulo abierto

- Un cúmulo abierto es un grupo ligado de estrellas jóvenes y poco masivo del disco; un cúmulo globular es un grupo masivo, esférico y viejo; un cúmulo masivo joven (S2) tiene menos de ~100 Myr y más de ~10⁴ M☉.

💡 **Cómo se explica en la clase [B25-C06](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md):**
- Los cúmulos abiertos son grupos menos masivos del disco.
- Distinguir cúmulo abierto, globular y masivo joven, y nombrar sus rangos de edad y masa citados.
- 🎯 **Por qué importa:** La mayoría de las estrellas nace en grupos. Los cúmulos son laboratorios: sus estrellas comparten edad, distancia y composición.

📘 **Dónde se aprende** (1 clase): [B25-C06 · Cúmulos estelares](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md).

### Cúmulo de escombros

- Un cúmulo de escombros (*rubble pile*) es un cuerpo hecho de fragmentos unidos por gravedad.

🎯 **Por qué importa (clase B58-C03):** La densidad aparente de un asteroide es casi siempre menor que la de sus rocas: la diferencia es porosidad, y de ella depende cuánta energía hace falta para desviarlo o fragmentarlo (C17). La decisión central: ¿cuánto de lo que parece masa es vacío, y cuánta incertidumbre arrastra la masa?

📘 **Dónde se aprende** (1 clase): [B58-C03 · Composición de asteroides](../programa/clases/B58/B58-C03-composicion-de-asteroides/CLASE.md).

### Cúmulo de galaxias

- Un cúmulo de galaxias es un sistema ligado de cientos a miles de galaxias, gas caliente y materia oscura.

💡 **Cómo se explica en la clase [B25-C13](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md):**
- Los dos métodos coinciden por construcción en este ejemplo sintético: en un cúmulo real, comparar la masa del gas con la de la dispersión de galaxias es una verificación de los supuestos.
- Definir cúmulo de galaxias, medio intracúmulo, equilibrio hidrostático y perfil beta.
- 🎯 **Por qué importa:** Los cúmulos de galaxias son las mayores estructuras ligadas por la gravedad. Contienen galaxias, un gas a decenas de millones de kelvin y mucha más masa de la que ambos aportan; por eso sirven para estudiar la materia oscura y poner a prueba el modelo cosmológico.

📘 **Dónde se aprende** (1 clase): [B25-C13 · Cúmulos de galaxias](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md).

### Cúmulo estelar

- Un cúmulo estelar es un conjunto ligado de estrellas nacidas de la misma nube.

💡 **Cómo se explica en la clase [B24-C19](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md):**
- python programa/clases/B24/B24-C19-cumulos-y-edades-estelares/cumulo.py
- 🎯 **Por qué importa:** La edad de una estrella aislada es difícil de medir; la de un cúmulo se puede leer en su diagrama HR, porque las estrellas más masivas ya han salido de la secuencia principal y el «punto de desvío» marca la edad. Esas edades fijan la cronología de la Galaxia y calibran los modelos.

📘 **Dónde se aprende** (1 clase): [B24-C19 · Cúmulos y edades estelares](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md).

### Cúmulo globular

- Un cúmulo abierto es un grupo ligado de estrellas jóvenes y poco masivo del disco; un cúmulo globular es un grupo masivo, esférico y viejo; un cúmulo masivo joven (S2) tiene menos de ~100 Myr y más de ~10⁴ M☉.

💡 **Cómo se explica en la clase [B25-C06](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md):**
- Harris (S1) cataloga `157` objetos clasificados como cúmulos globulares de la Vía Láctea, con coordenadas, metalicidades, parámetros estructurales y dispersión central de velocidades.
- Distinguir cúmulo abierto, globular y masivo joven, y nombrar sus rangos de edad y masa citados.
- 🎯 **Por qué importa:** La mayoría de las estrellas nace en grupos. Los cúmulos son laboratorios: sus estrellas comparten edad, distancia y composición.

📖 **Explicado a fondo:** [Cúmulo globular](esencial/tercera-a-e.md#cúmulo-globular) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B25-C06 · Cúmulos estelares](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md).

### Cúmulo masivo joven

- Un cúmulo abierto es un grupo ligado de estrellas jóvenes y poco masivo del disco; un cúmulo globular es un grupo masivo, esférico y viejo; un cúmulo masivo joven (S2) tiene menos de ~100 Myr y más de ~10⁴ M☉.

💡 **Cómo se explica en la clase [B25-C06](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md):**
- Portegies Zwart, McMillan y Gieles (S2) revisan los cúmulos jóvenes masivos: más jóvenes que unos `100 Myr` y más masivos que unos `10⁴ M☉`.
- Distinguir cúmulo abierto, globular y masivo joven, y nombrar sus rangos de edad y masa citados.
- 🎯 **Por qué importa:** La mayoría de las estrellas nace en grupos. Los cúmulos son laboratorios: sus estrellas comparten edad, distancia y composición.

📘 **Dónde se aprende** (1 clase): [B25-C06 · Cúmulos estelares](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md).

### Cuota

- La cuota `s_i` es `q_i/Q`.
- La cuota es el peso mínimo para ganar una votación.

💡 **Cómo se explica en la clase [B48-C02](../programa/clases/B48/B48-C02-concesion-de-tiempo-de-observacion/CLASE.md):**
- Ambos métodos coinciden aquí; con otras cuotas pueden diferir en una hora.
- Como repartir una torta en porciones enteras: las cuotas dan trozos con fracciones y alguna regla decide quién recibe las migas sobrantes.
- 🎯 **Por qué importa:** Un reparto sin regla clara genera conflicto, y uno sin clima genera promesas incumplibles. La decisión central: ¿cuántas horas se asignan y cuántas se esperan efectivas?

📘 **Dónde se aprende** (3 clases): [B48-C02 · Concesión de tiempo de observación](../programa/clases/B48/B48-C02-concesion-de-tiempo-de-observacion/CLASE.md); [B124-C03 · Mercados downstream y upstream](../programa/clases/B124/B124-C03-mercados-downstream-y-upstream/CLASE.md); [B125-C03 · Gobierno corporativo de una empresa espacial](../programa/clases/B125/B125-C03-gobierno-corporativo-de-una-empresa-espacial/CLASE.md).

### Cuota inicial

- La cuota inicial `U` se paga al firmar.

💡 **Cómo se explica en la clase [B124-C09](../programa/clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md):**
- Paso 4 · Con cuota. Con una cuota inicial de 1: valor total `2,2434` Mum.
- Distinguir cuota inicial, regalía y valor actual de la licencia.
- 🎯 **Por qué importa:** La propiedad intelectual es un activo, pero su valor depende de cuánto se vende con ella y de cuánto del margen se queda el que la usa. La decisión central: ¿qué licencia conviene ofrecer y cuántas regalías soporta el licenciatario?

📘 **Dónde se aprende** (1 clase): [B124-C09 · Propiedad intelectual y licencias](../programa/clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md).

### Cuota interna

- La cuota interna es la parte final de cada responsable.

💡 **Cómo se explica en la clase [B119-C03](../programa/clases/B119/B119-C03-convenio-de-responsabilidad/CLASE.md):**
- Culpas 0,7 y 0,3: cuotas internas `A = 70.0` y `B = 30.0` u.m.; la víctima puede cobrar los 100 de A o de B.
- Si A no puede pagar, B paga `100.0` u.m. a la víctima; su cuota interna es `30.0`; reclama a A el regreso de `70.0` u.m.
- 🎯 **Por qué importa:** El art. VII del tratado de 1967 (no discutido en la fuente de C01) fundamenta la responsabilidad; el convenio de 1972 la desarrolla, y la cuantificación del daño se trata en el bloque de reclamaciones (B123); esta clase fija la regla de reparto.

📘 **Dónde se aprende** (1 clase): [B119-C03 · Convenio de Responsabilidad](../programa/clases/B119/B119-C03-convenio-de-responsabilidad/CLASE.md).

### Cuota parte

- La cuota parte cede una fracción fija `q` de cada siniestro y de la prima.

💡 **Cómo se explica en la clase [B127-C07](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md):**
- La cuota parte lo hace barato porque la comisión es generosa (dato sintético); el exceso de pérdida lo hace caro pero solo protege contra siniestros grandes, como los que dominan este tipo de cartera, y deja intacta la frecuencia de los pequeños.
- X["siniestro X"] --> Q["cuota parte: reasegurador paga q X"]
- 🎯 **Por qué importa:** El riesgo espacial se reparte mediante reaseguro; no había clase al respecto. La decisión central: ¿qué parte del riesgo se cede y cuánto cuesta reducir la cola?

📘 **Dónde se aprende** (1 clase): [B127-C07 · Reaseguro espacial](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md).

### Curaduría

- La curaduría es el cuidado, registro y distribución de una colección.

💡 **Cómo se explica en la clase [B63-C03](../programa/clases/B63/B63-C03-curaduria-y-cadena-de-custodia-de-muestras/CLASE.md):**
- La página de curaduría no detalla procedimientos de manejo ni de contaminación, y esos procedimientos no se describen aquí como reales.
- python programa/clases/B63/B63-C03-curaduria-y-cadena-de-custodia-de-muestras/custodia.py
- 🎯 **Por qué importa:** Una muestra planetaria es irrepetible y se estudia durante décadas. La decisión central: ¿cómo demuestras, años después, qué le pasó a una muestra y cuánto de lo que mides es suyo?

📘 **Dónde se aprende** (1 clase): [B63-C03 · Curaduría y cadena de custodia de muestras](../programa/clases/B63/B63-C03-curaduria-y-cadena-de-custodia-de-muestras/CLASE.md).

### Curtosis

- La curtosis mide las colas.
- La curtosis mide su carácter impulsivo.
- La curtosis `E[x⁴]/σ⁴` vale 3 en una gaussiana.

💡 **Cómo se explica en la clase [B35-C09](../programa/clases/B35/B35-C09-turbulencia-en-plasmas-y-mhd/CLASE.md):**
- Un campo gaussiano tiene curtosis 3 a todas las escalas; la cascada multiplicativa la hace crecer al disminuir la escala.
- La curtosis de los incrementos gaussianos es `≈ 3`, mientras que una cascada binomial con `p = 0,7` llega a `106,6` en 12 niveles.
- 🎯 **Por qué importa:** La pendiente de un espectro y su intermitencia distinguen modelos de turbulencia. La decisión central: ¿qué pendiente y qué curtosis tiene la serie y qué modelo sugiere?

📘 **Dónde se aprende** (3 clases): [B35-C09 · Turbulencia en plasmas y MHD](../programa/clases/B35/B35-C09-turbulencia-en-plasmas-y-mhd/CLASE.md); [B84-C32 · Vibración aleatoria y densidad espectral de potencia](../programa/clases/B84/B84-C32-vibracion-aleatoria-y-densidad-espectral-de-potencia/CLASE.md); [B97-C26 · Monitoreo de condición de maquinaria extraterrestre](../programa/clases/B97/B97-C26-monitoreo-de-condicion-de-maquinaria-extraterrestre/CLASE.md).

### Curtosis en exceso

- La asimetría y la curtosis en exceso: momentos de la forma de `z`.

💡 **Cómo se explica en la clase [B51-C07](../programa/clases/B51/B51-C07-evaluacion-de-residuos-y-diagnostico-de-calidad-de-calibracion/CLASE.md):**
- desviacion de z = 0.8861 ; asimetria = +0.0226 ; curtosis en exceso = +0.0994
- 🎯 **Por qué importa:** Una calibración mala puede dar una imagen bonita. La decisión central: ¿qué valor de χ² reducido y qué forma de los residuos indican que el modelo es suficiente?

📘 **Dónde se aprende** (1 clase): [B51-C07 · Evaluación de residuos y diagnóstico de calidad de calibración](../programa/clases/B51/B51-C07-evaluacion-de-residuos-y-diagnostico-de-calidad-de-calibracion/CLASE.md).

### Curva

- Una curva tiene pendiente que cambia.

💡 **Cómo se explica en la clase [B03-C16](../programa/clases/B03/B03-C16-pendiente-e-interpretacion-de-graficos/CLASE.md):**
- En escalas lineales, el gráfico `T` frente a `a` de los planetas es una curva.
- Hablar de «la pendiente» de una curva es engañoso: cada tramo tiene la suya.
- ⚠️ **Error frecuente:** Hablar de «la pendiente» de una curva. Ejercicio 8.
- 🎯 **Por qué importa:** Si sitúas en un gráfico logarítmico el período frente al semieje de los planetas, los puntos forman una recta. Su pendiente es 1,5: ese número es el exponente de la tercera ley de Kepler.

📘 **Dónde se aprende** (1 clase): [B03-C16 · Pendiente e interpretación de gráficos](../programa/clases/B03/B03-C16-pendiente-e-interpretacion-de-graficos/CLASE.md).

### Curva de aprendizaje

- Una curva de aprendizaje relaciona el error con el número de sesiones.
- La curva de aprendizaje muestra la baja de la tasa de fallas con la experiencia.
- La curva de aprendizaje de Wright da `T_n = T₁ n^β` con `β = log₂(pendiente)`.

💡 **Cómo se explica en la clase [B107-C03](../programa/clases/B107/B107-C03-entrenamiento-vestibular-y-de-orientacion-espacial/CLASE.md):**
- Una curva de aprendizaje sintética baja de 20,0° a `5,01°` en 20 sesiones;
- Ajustar una curva de aprendizaje `e_k = e∞ + (e0 − e∞) r^k` y calcular sesiones al 95 %.
- 🎯 **Por qué importa:** Los fragmentos consultados indican que tras el vuelo hay alteraciones del control postural y locomotor (Macaulay et al., 2021) y que el equilibrio dinámico, la percepción del tiempo y el tiempo de reacción cambian tras el aterrizaje (Clément et al., 2023). Antes del vuelo la pregunta es cómo preparar la desorientación.

📘 **Dónde se aprende** (3 clases): [B107-C03 · Entrenamiento vestibular y de orientación espacial](../programa/clases/B107/B107-C03-entrenamiento-vestibular-y-de-orientacion-espacial/CLASE.md); [B119-C21 · Cultura de seguridad aeroespacial y aprendizaje de incidentes](../programa/clases/B119/B119-C21-cultura-de-seguridad-aeroespacial-y-aprendizaje-de-incidentes/CLASE.md); [B124-C05 · Estimación de costos de misión](../programa/clases/B124/B124-C05-estimacion-de-costos-de-mision/CLASE.md).

### Curva de calibración

- La curva de calibración es la relación entre indicación y valor de la magnitud.

💡 **Cómo se explica en la clase [B13-C05](../programa/clases/B13/B13-C05-calibracion-instrumental/CLASE.md):**
- La evidencia es la curva de calibración con su incertidumbre del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Un sensor solar de una nave devuelve cuentas digitales (DN), no vatios por metro cuadrado. Para saber cuánta luz recibe hay que haberlo expuesto antes a fuentes de irradiancia conocida y haber establecido la relación entre ambas.

📘 **Dónde se aprende** (1 clase): [B13-C05 · Calibración instrumental](../programa/clases/B13/B13-C05-calibracion-instrumental/CLASE.md).

### Curva de costo

- La curva de costo tiene un mínimo de delta-v en el tiempo de Hohmann.

💡 **Cómo se explica en la clase [B75-C27](../programa/clases/B75/B75-C27-duracion-de-mision-y-tiempo-de-vuelo-como-restriccion/CLASE.md):**
- La evidencia es tu curva de costo total del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *curva de costo total* para un `c_t` que justifiques: tabla de `TOF`, `Δv`, `m₀`, `J`, el óptimo y la comparación con Hohmann.
- 🎯 **Por qué importa:** Un viaje más corto gasta más combustible y uno más largo gasta más tiempo. La decisión central: ¿qué tiempo de vuelo minimiza el costo total cuando se pesan la masa lanzada y la duración?

📘 **Dónde se aprende** (1 clase): [B75-C27 · Duración de misión y tiempo de vuelo como restricción](../programa/clases/B75/B75-C27-duracion-de-mision-y-tiempo-de-vuelo-como-restriccion/CLASE.md).

### Curva de crecimiento

- La curva de crecimiento es `W` frente a la columna.

💡 **Cómo se explica en la clase [B32-C09](../programa/clases/B32/B32-C09-medicion-de-perfiles-de-linea-ancho-equivalente-y-ajuste/CLASE.md):**
- La evidencia es la ficha de la curva de crecimiento del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha de la curva de crecimiento*: tabla y regímenes.
- 🎯 **Por qué importa:** Medir una abundancia exige saber en qué régimen está la línea. La decisión central: ¿cómo depende el ancho equivalente de la columna de absorbedores?

📘 **Dónde se aprende** (2 clases): [B32-C09 · Medición de perfiles de línea: ancho equivalente y ajuste](../programa/clases/B32/B32-C09-medicion-de-perfiles-de-linea-ancho-equivalente-y-ajuste/CLASE.md); [B45-C11 · Líneas de absorción](../programa/clases/B45/B45-C11-lineas-de-absorcion/CLASE.md).

### Curva de fase

- La curva de fase pliega la serie al periodo.

💡 **Cómo se explica en la clase [B29-C14](../programa/clases/B29/B29-C14-estrellas-variables-periodicas/CLASE.md):**
- *Descripción textual:* se ajusta una curva armónica para cada frecuencia y se toma el mínimo de `χ²`; la dispersión de fase da un estimador independiente; ambos coinciden y la incertidumbre de una sinusoide sigue una fórmula estándar.
- 🎯 **Por qué importa:** El periodo es la propiedad básica de una variable periódica; de él y de la forma de la curva se deducen la masa, la edad o la distancia en muchos casos. La decisión central: ¿qué periodo y qué incertidumbre da la serie y qué métodos coinciden?

📘 **Dónde se aprende** (1 clase): [B29-C14 · Estrellas variables periódicas](../programa/clases/B29/B29-C14-estrellas-variables-periodicas/CLASE.md).

### Curva de Hill

- La curva de Hill `R(L) = Rmax L/(L + L50)` satura en `Rmax`;

💡 **Cómo se explica en la clase [B105-C16](../programa/clases/B105/B105-C16-contramedidas-de-ejercicio/CLASE.md):**
- Una curva de Hill `R = Rmax L/(L + L50)` con `Rmax = 0,8` y `L50 = 100` (ilustrativas) reduce la pérdida ósea: con `L = 100`, `R = 0,40` y la pérdida a 6 meses baja de 7,27 % a 4,21 %; con `L = 800`, a 2,15 %.
- Ajustar una curva de Hill de dosis–respuesta a datos sintéticos por mínimos cuadrados.
- 🎯 **Por qué importa:** Más ejercicio ayuda, pero con rendimientos decrecientes y con un costo de energía y tiempo. La decisión central: ¿qué parte de la pérdida se evita con una carga dada y cuánta energía extra exige?

📘 **Dónde se aprende** (1 clase): [B105-C16 · Contramedidas de ejercicio](../programa/clases/B105/B105-C16-contramedidas-de-ejercicio/CLASE.md).

### Curva de la bañera

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C19):** No sirve duplicar un equipo si otro componente falla antes. La decisión central: ¿qué recurso limita la vida de la misión y qué redundancia vale la pena?

📘 **Dónde se aprende** (1 clase): [B47-C19 · Mantenimiento y vida útil](../programa/clases/B47/B47-C19-mantenimiento-y-vida-util/CLASE.md).

### Curva de Lorenz

- La curva de Lorenz la visualiza.

🎯 **Por qué importa (clase B119-C34):** El acceso desigual al espacio es un asunto de gobernanza que el catálogo no trata; esta clase da las herramientas de medición antes de las discusiones de política (C25, C36). La decisión central: ¿qué tan desigual es el acceso y cuánto lo reduce una regla de uso compartido?

📘 **Dónde se aprende** (1 clase): [B119-C34 · Equidad de acceso al espacio](../programa/clases/B119/B119-C34-equidad-de-acceso-al-espacio/CLASE.md).

### Curva de luz

- La curva de luz es el brillo en función del tiempo.
- La curva de luz es el brillo frente al tiempo.
- La curva de luz es la magnitud en función del tiempo.

💡 **Cómo se explica en la clase [B28-C08](../programa/clases/B28/B28-C08-senales-transitorias/CLASE.md):**
- Se genera la curva con 14 épocas entre `1,0` y `18,2 d`.
- *Descripción textual:* la curva de luz se ajusta con una recta en `log t`; el tiempo sobre el límite sale del modelo; la probabilidad de detección depende de la razón entre el tiempo visible y la cadencia.
- ⚠️ **Error frecuente:** Tomar la curva sintética por real. Se corrige con la sección 10.
- 🎯 **Por qué importa:** Un transitorio que dura menos que el intervalo entre visitas se pierde. El índice de caída decide cuánto dura un evento sobre el límite de detección.

📖 **Explicado a fondo:** [Curva de luz](esencial/esencial-a-c.md#curva-de-luz) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (3 clases): [B28-C08 · Señales transitorias](../programa/clases/B28/B28-C08-senales-transitorias/CLASE.md); [B58-C13 · Caracterización de rotación](../programa/clases/B58/B58-C13-caracterizacion-de-rotacion/CLASE.md); [B129-C02 · Fotometría participativa](../programa/clases/B129/B129-C02-fotometria-participativa/CLASE.md).

### Curva de nivel

- Una curva de nivel es el conjunto de puntos donde `f` vale una constante `c`.
- Una curva de nivel es `f = c`; el gradiente es perpendicular a ella.

💡 **Cómo se explica en la clase [B09-C15](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md):**
- Un mapa topográfico dibuja las líneas de igual altura (curvas de nivel): juntas indican pendiente fuerte, separadas indican llanura.
- *Descripción textual:* una función de dos variables se estudia con cortes (funciones de una variable) y con curvas de nivel; ambos permiten clasificar puntos especiales como máximos, mínimos y sillas.
- ⚠️ **Error frecuente:** Creer que dos curvas de nivel distintas se cruzan. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Una sonda que viaja de la Tierra a la Luna se mueve en un campo de potencial que depende de dos coordenadas del plano. Dónde están los puntos de equilibrio y qué forma tiene el campo alrededor de ellos se lee en un mapa de curvas de nivel.

📘 **Dónde se aprende** (2 clases): [B09-C15 · Funciones de varias variables](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md); [B09-C17 · Gradiente y derivada direccional](../programa/clases/B09/B09-C17-gradiente-y-derivada-direccional/CLASE.md).

### Curva de olvido

- La curva de olvido `R = e^(−Δt/S)` da la retención tras `Δt` días con estabilidad `S`.

💡 **Cómo se explica en la clase [B104-C06](../programa/clases/B104/B104-C06-entrenamiento-de-procedimientos/CLASE.md):**
- Calcular la retención con una curva de olvido exponencial.
- ⚠️ **Error frecuente:** Suponer que el dominio es permanente. Aplica la curva de olvido (8.3).
- 🎯 **Por qué importa:** Los procedimientos se practican en tierra y a veces se usan meses después, en el momento crítico. La decisión central: ¿cuándo repasar para que el procedimiento siga disponible sin gastar tiempo de entrenamiento de más?

📘 **Dónde se aprende** (1 clase): [B104-C06 · Entrenamiento de procedimientos](../programa/clases/B104/B104-C06-entrenamiento-de-procedimientos/CLASE.md).

### Curva de partición

- La curva de partición (de Tromp) da la probabilidad de que un grano de tamaño `d` vaya a un producto.

💡 **Cómo se explica en la clase [B59-C22](../programa/clases/B59/B59-C22-beneficio-y-separacion-granulometrica-de-regolito/CLASE.md):**
- Describir una curva de partición con tamaño de corte y agudeza.
- Ejercicio 12 · integrador. Elabora tu *ficha del beneficio*: curva de partición, leyes, recuperación, balance cerrado y compromiso al variar `d50`.
- 🎯 **Por qué importa:** Calentar o reducir todo el regolito es caro; separar la fracción rica antes ahorra energía. La decisión central: ¿qué tamaño de corte equilibra la ley del concentrado y la recuperación del mineral?

📘 **Dónde se aprende** (1 clase): [B59-C22 · Beneficio y separación granulométrica de regolito](../programa/clases/B59/B59-C22-beneficio-y-separacion-granulometrica-de-regolito/CLASE.md).

### Curva de polarización

- La curva de polarización `V(i)` suma el potencial reversible, la caída óhmica y la activación.

💡 **Cómo se explica en la clase [B59-C10](../programa/clases/B59/B59-C10-electrolisis-y-balances-energeticos/CLASE.md):**
- *Descripción textual:* la entalpía fija la tensión termoneutra; la curva de polarización da la tensión de operación; su comparación indica si la celda absorbe o cede calor.
- Leer una curva de polarización y su eficiencia.
- 🎯 **Por qué importa:** La electrólisis es el mayor consumidor de energía de la planta. La decisión central: ¿a qué densidad de corriente conviene operar, entre una celda pequeña que gasta más electricidad y una grande que gasta menos?

📘 **Dónde se aprende** (1 clase): [B59-C10 · Electrólisis y balances energéticos](../programa/clases/B59/B59-C10-electrolisis-y-balances-energeticos/CLASE.md).

### Curva de precisión–exhaustividad

- La curva de precisión–exhaustividad grafica precisión contra exhaustividad, y la precisión promedio resume su área (S2).

💡 **Cómo se explica en la clase [B17-C12](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md):**
- La curva ROC no cambia con la prevalencia, porque usa tasas dentro de cada clase; la de precisión–exhaustividad sí, y por eso refleja la carga de falsos positivos.
- Grafica las dos curvas (ROC y precisión–exhaustividad) en paneles separados con trazos distintos y describe en texto que la primera se acerca a la esquina superior izquierda y la segunda cae pronto.
- 🎯 **Por qué importa:** Un modelo marca candidatos a planeta, y cada alerta cuesta horas de revisión. Si el modelo acierta el 99 % en una muestra donde el 99 % son negativos, no dice nada útil.

📘 **Dónde se aprende** (1 clase): [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md).

### Curva de rotación

- La curva de rotación es la velocidad circular en función del radio.
- La curva de rotación `v(R)` da la velocidad circular en función del radio.

💡 **Cómo se explica en la clase [B25-C08](../programa/clases/B25/B25-C08-curvas-de-rotacion-de-galaxias/CLASE.md):**
- *Descripción textual:* del disco visible se calcula su curva de rotación; la diferencia de cuadrados con la observada indica la masa que falta, que se modela como un halo.
- Rotación y curva de un disco (esta clase): directa y sencilla, pero supone órbitas circulares.
- 🎯 **Por qué importa:** Si la masa estuviera donde brilla, la velocidad de rotación debería caer en las afueras de una galaxia, como la de los planetas lejanos del Sol. Que una curva de rotación se mantenga plana indica más masa de la que se ve.

📘 **Dónde se aprende** (4 clases): [B25-C08 · Curvas de rotación de galaxias](../programa/clases/B25/B25-C08-curvas-de-rotacion-de-galaxias/CLASE.md); [B26-C18 · Materia oscura y evidencias](../programa/clases/B26/B26-C18-materia-oscura-y-evidencias/CLASE.md); [B31-C17 · Materias oscuras candidatas](../programa/clases/B31/B31-C17-materias-oscuras-candidatas/CLASE.md); [B46-C11 · Observación de hidrógeno a 21 centímetros](../programa/clases/B46/B46-C11-observacion-de-hidrogeno-a-21-centimetros/CLASE.md).

### Curva de transferencia

- Plano (*flat*): imagen de iluminación uniforme. Curva de transferencia: varianza contra media.

🎯 **Por qué importa (clase B48-C13):** Sin ganancia ni ruido de lectura, las incertidumbres de cada medida no se pueden calcular. La decisión central: ¿cuánto valen la ganancia y el ruido de lectura del detector?

📘 **Dónde se aprende** (1 clase): [B48-C13 · Calibraciones nocturnas](../programa/clases/B48/B48-C13-calibraciones-nocturnas/CLASE.md).

### Curva de transferencia de fotones

- La curva de transferencia de fotones es `var = media/g + RN²/g²`.
- La curva de transferencia de fotones (PTC): varianza frente a media.

🎯 **Por qué importa (clase B45-C19):** Un flujo sin incertidumbre no es una medida. La decisión central: ¿qué términos dominan el ruido y cómo se estiman ganancia y ruido de lectura?

📘 **Dónde se aprende** (2 clases): [B45-C19 · Reducción e incertidumbre instrumental](../programa/clases/B45/B45-C19-reduccion-e-incertidumbre-instrumental/CLASE.md); [B47-C15 · Calibración a bordo](../programa/clases/B47/B47-C15-calibracion-a-bordo/CLASE.md).

### Curva diferencial

- La curva diferencial es objetivo/comparación.

💡 **Cómo se explica en la clase [B45-C17](../programa/clases/B45/B45-C17-fotometria-diferencial/CLASE.md):**
- Ejercicio 12. Integrador. Elabora tu *ficha de fotometría diferencial*: curvas, ruido previsto, profundidad y límites.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de fotometría diferencial*: curvas, ruido previsto, profundidad y límites.
- 🎯 **Por qué importa:** La atmósfera varía más que la señal; sin una referencia, la curva de luz no sirve. La decisión central: ¿qué comparaciones y qué precisión se necesitan para una profundidad dada?

📘 **Dónde se aprende** (1 clase): [B45-C17 · Fotometría diferencial](../programa/clases/B45/B45-C17-fotometria-diferencial/CLASE.md).

### Curva dosis-profundidad

- La curva dosis-profundidad `D(x) ∝ (1 + x/x₀)^−p`.

💡 **Cómo se explica en la clase [B85-C22](../programa/clases/B85/B85-C22-modelos-de-exposicion-a-radiacion-en-orbita/CLASE.md):**
- *Descripción textual:* la órbita da la posición geográfica en cada instante, el mapa sintético da la tasa local, el promedio sobre un día da la dosis diaria y anual, y la curva dosis-profundidad ajusta el blindaje.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de dosis por órbita (sintética)*: tabla por altitud e inclinación, curva dosis-profundidad, convergencia y lista de lo consultado, sintético y no usado.
- 🎯 **Por qué importa:** La dosis anual decide el blindaje y la vida de la electrónica y los materiales. La decisión central: ¿cuánta dosis acumula una órbita al año y cuánto la reduce un milímetro más de blindaje?

📘 **Dónde se aprende** (1 clase): [B85-C22 · Modelos de exposición a radiación en órbita](../programa/clases/B85/B85-C22-modelos-de-exposicion-a-radiacion-en-orbita/CLASE.md).

### Curva en V

- HFD: diámetro de media energía de una estrella. Curva en V: HFD contra posición.

🎯 **Por qué importa (clase B48-C22):** Un enfoque erróneo pierde resolución en todas las imágenes de la noche. La decisión central: ¿en qué posición del enfocador está el mínimo y con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B48-C22 · Control automático del enfocador y autoenfoque](../programa/clases/B48/B48-C22-control-automatico-del-enfocador-y-autoenfoque/CLASE.md).

### Curva L

- La curva L es la gráfica, en escala log–log, de la norma de la solución frente a la norma del residuo al variar `λ` (S2).

💡 **Cómo se explica en la clase [B22-C02](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md):**
- La curva tiene forma de «L» (S2): con `λ` muy pequeño la norma de la solución explota y el residuo ya casi no baja (rama vertical); con `λ` muy grande el residuo crece y la solución casi no cambia (rama horizontal).
- El vértice de la L es un compromiso: se localiza donde la curvatura de la curva log–log es máxima.
- 🎯 **Por qué importa:** Si no puedes confiar en `x = A⁻¹ b` y no puedes bajar el ruido a voluntad, necesitas una regla que ignore lo que los datos no pueden decir. Esa regla debe tener una perilla: cuánto ignorar.

📘 **Dónde se aprende** (1 clase): [B22-C02 · Regularización de Tikhonov](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md).

### Curva NC

- La curva NC es un límite por bandas de octava.

💡 **Cómo se explica en la clase [B109-C10](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md):**
- El resumen técnico OCHMO-TB-035 de NASA (Rev C, 2023) indica que NASA-STD-3001 Vol. 2 limita el ruido peligroso a menos de `85 dBA` sin importar la duración y el ruido continuo de las áreas de trabajo a la curva NC-50.
- Ejercicio 11 · transferencia. Transferencia. ¿Cumple esta cabina la curva NC-50?
- 🎯 **Por qué importa:** El ruido continuo degrada la comunicación, el sueño y el trabajo aunque no dañe el oído. La decisión central: ¿qué fuente reduzco primero y cuánto baja el nivel de la cabina?

📘 **Dónde se aprende** (1 clase): [B109-C10 · Acústica y control de ruido interior](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md).

### Curva plana

- La curva plana es la velocidad de rotación constante a gran radio.

💡 **Cómo se explica en la clase [B36-C11](../programa/clases/B36/B36-C11-gravedad-modificada-mond-y-relativistas-frente-a-materia-oscura/CLASE.md):**
- Para una galaxia de `5×10¹⁰ M☉` y escala de `3 kpc` (ilustrativa), la curva MOND llega a `191,3 km/s` a 10 kpc frente a `134,8` newtoniana, un halo NFW la reproduce con una desviación de `1,55 km/s`, y la velocidad plana `168,62` coincide con `(G M a₀)^(1/4) = 167,98 km/s` al `0,4 %`.
- Descripción larga: la curva MOND es plana a 180 a 190 km/s y el NFW la reproduce.
- 🎯 **Por qué importa:** Una alternativa debe confrontarse con todas las pruebas. La decisión central: ¿qué observación separa la materia oscura de la gravedad modificada?

📘 **Dónde se aprende** (1 clase): [B36-C11 · Gravedad modificada (MOND y relativistas) frente a materia oscura](../programa/clases/B36/B36-C11-gravedad-modificada-mond-y-relativistas-frente-a-materia-oscura/CLASE.md).

### Curva ROC

- La curva ROC grafica exhaustividad contra tasa de falsos positivos al variar el umbral; su área es el AUC.
- La curva ROC es POD frente a la tasa de falsas alarmas.
- La curva ROC grafica la fracción de anomalías detectadas contra la de falsas alarmas al variar el umbral; su área (AUC) vale 1 si el método separa perfectamente y 0,5 si no distingue (S2).

💡 **Cómo se explica en la clase [B17-C05](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md):**
- Comparar métodos con el área bajo la curva ROC.
- 🎯 **Por qué importa:** El subsistema térmico de un satélite entrega temperatura y corriente. Cada una, por separado, puede estar dentro de su rango normal y sin embargo la pareja ser imposible: la corriente alta con temperatura baja no ocurre nunca en operación sana.

📘 **Dónde se aprende** (3 clases): [B17-C05 · Detección de anomalías](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md); [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md); [B33-C14 · Verificación de alertas con tablas de contingencia](../programa/clases/B33/B33-C14-verificacion-de-alertas-con-tablas-de-contingencia/CLASE.md).

### Curvas de equilibrio

- Las curvas de equilibrio separan regiones: fusión (sólido–líquido), vaporización (líquido–gas) y sublimación (sólido–gas).

💡 **Cómo se explica en la clase [B06-C11](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md):**
- Las fronteras son las curvas de equilibrio.
- 🎯 **Por qué importa:** La temperatura de ebullición del agua no es una constante de la naturaleza: depende de la presión. En lo alto de una montaña hierve a menos de 100 °C; en Marte, con 6 mb, el agua apenas puede ser líquida; en Venus, a 92 bar y 737 K, el CO₂ no es ni líquido ni gas.

📘 **Dónde se aprende** (1 clase): [B06-C11 · Diagramas de fase](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md).

### Curvatura escalar

- La curvatura escalar es `R = g^bd R_bd`.

💡 **Cómo se explica en la clase [B39-C03](../programa/clases/B39/B39-C03-tensor-de-riemann-ricci-y-curvatura-escalar/CLASE.md):**
- La curvatura escalar numérica es `0,50000006` frente a `2/a² = 0,50000000`.
- Descripción larga: la esfera tiene la curvatura escalar esperada y Schwarzschild es vacío con Kretschmann no nulo.
- 🎯 **Por qué importa:** Un espacio-tiempo es curvo si el Riemann no se anula. La decisión central: ¿qué mide cada contracción del Riemann y cómo se comprueba un cálculo de curvatura?

📘 **Dónde se aprende** (1 clase): [B39-C03 · Tensor de Riemann, Ricci y curvatura escalar](../programa/clases/B39/B39-C03-tensor-de-riemann-ricci-y-curvatura-escalar/CLASE.md).

### Curvatura extrínseca

- La curvatura extrínseca `K_ij` mide cómo se curva la capa en el espacio-tiempo.

💡 **Cómo se explica en la clase [B39-C06](../programa/clases/B39/B39-C06-introduccion-a-la-relatividad-numerica-formalismo-3-1/CLASE.md):**
- La rebanada de Painlevé–Gullstrand es plana pero tiene curvatura extrínseca no nula: `K² = K_ij K^ij` hace que la ligadura de vacío se cumpla.
- 🎯 **Por qué importa:** Una simulación necesita un tiempo y un espacio. La decisión central: ¿cómo se separa el espacio-tiempo en capas y cómo se sabe que una evolución converge?

📘 **Dónde se aprende** (1 clase): [B39-C06 · Introducción a la relatividad numérica: formalismo 3+1](../programa/clases/B39/B39-C06-introduccion-a-la-relatividad-numerica-formalismo-3-1/CLASE.md).

### Curvatura gaussiana

- La curvatura gaussiana `K` de una superficie es `1/R²` para una esfera de radio `R`.

🎯 **Por qué importa (clase B26-C07):** Medir una distancia cerca de una masa grande no da lo mismo que en el espacio plano: el radio de un círculo y su circunferencia dejan de cumplir `C = 2πR`. Los GPS, las lentes gravitacionales y los agujeros negros dependen de esa diferencia.

📘 **Dónde se aprende** (1 clase): [B26-C07 · Curvatura y métricas](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md).

### CUSUM

- El CUSUM inferior es `S_t = máx(0, S_{t−1} − z_t − k)` con alarma si `S_t > h` (`k = 0,5`).
- Puntuación robusta: desvío en unidades de MAD. CUSUM: suma acumulada de desvíos.
- El CUSUM acumula `(μ₀ − x)/σ − k` y se reinicia en 0.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B96-C13](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md):**
- (3) CUSUM: `S = max(0, S + (x − μ)/σ − 0,5)` y alarma si `S > 5`, con reinicio.
- CUSUM acumula el exceso y detecta la deriva en 7 muestras, a costa de falsas alarmas y de necesitar μ y σ de referencia.
- 🎯 **Por qué importa:** Un detector que no ve una deriva lenta avisa cuando ya es tarde, y uno que alarma por todo se ignora. La decisión central: ¿qué detector ve cada tipo de anomalía, con qué retraso y a qué costo en falsas alarmas?

📘 **Dónde se aprende** (5 clases): [B96-C13 · Detección de anomalías](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md); [B97-C22 · Detección autónoma de eventos científicos](../programa/clases/B97/B97-C22-deteccion-autonoma-de-eventos-cientificos/CLASE.md); [B104-C18 · Aislamiento y convivencia](../programa/clases/B104/B104-C18-aislamiento-y-convivencia/CLASE.md); [B105-C09 · Salud mental en aislamiento](../programa/clases/B105/B105-C09-salud-mental-en-aislamiento/CLASE.md); [B107-C10 · Indicadores de rehabilitación y seguimiento](../programa/clases/B107/B107-C10-indicadores-de-rehabilitacion-y-seguimiento/CLASE.md).

### CVCM

- RML `= TML − WVR`; CVCM (*collected volatile condensable material*) es la masa condensada en el colector, en % de la masa inicial.
- TML: pérdida total de masa, `100 (mᵢ − m_f)/mᵢ`. CVCM: volátiles condensables recogidos, `100 m_col/mᵢ`.

💡 **Cómo se explica en la clase [B84-C07](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md):**
- Con `m_i = 500 mg`: `TML = (m_i − m_f)/m_i`, `WVR = (m_h − m_f)/m_i`, `RML = TML − WVR`, `CVCM = Δm_colector/m_i`.
- La silicona B pasa en `TML` y falla en `CVCM`: por eso se exigen ambos criterios.
- 🎯 **Por qué importa:** Una película de 10 nm sobre un espejo de telescopio o un sensor estelar degrada la misión; el cribado de desgasificación se hace antes de elegir el adhesivo. La decisión central: ¿pasa un material el cribado de desgasificación y cuántos días de bakeout necesita para limpiarlo?

📘 **Dónde se aprende** (2 clases): [B84-C07 · Desgasificación de materiales](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md); [B90-C04 · Control de contaminación](../programa/clases/B90/B90-C04-control-de-contaminacion/CLASE.md).
