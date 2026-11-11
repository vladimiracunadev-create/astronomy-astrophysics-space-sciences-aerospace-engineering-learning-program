# Términos · M (parte 2 de 2)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · **M** · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-m.md) · **2**

### Método de Euler

- El método de Euler actualiza el estado con la tasa de cambio actual: `x ← x + v·dt`, `v ← v + g·dt`.

💡 **Cómo se explica en la clase [B07-C05](../programa/clases/B07/B07-C05-bucles-y-simulaciones-sencillas/CLASE.md):**
- Una mejora del método (p. ej. pasos más precisos que Euler) se verá en B11.
- Simular una caída libre con el método de Euler.
- 🎯 **Por qué importa:** Una simulación es un bucle: calcula el estado siguiente a partir del actual, una y otra vez. Si el paso es demasiado grande, el resultado se aparta de la realidad; si es demasiado pequeño, tarda.

📘 **Dónde se aprende** (1 clase): [B07-C05 · Bucles y simulaciones sencillas](../programa/clases/B07/B07-C05-bucles-y-simulaciones-sencillas/CLASE.md).

### Método de Euler explícito

- El método de Euler explícito calcula `s_{k+1} = s_k + h F(t_k, s_k)` (también llamado «de las tangentes»).

🎯 **Por qué importa (clase B11-C05):** La mayoría de las ecuaciones del movimiento no tiene solución en forma cerrada. Un computador no resuelve la ecuación: da pasos pequeños, y cada paso usa la pendiente conocida para estimar el estado siguiente.

📘 **Dónde se aprende** (1 clase): [B11-C05 · Método de Euler](../programa/clases/B11/B11-C05-metodo-de-euler/CLASE.md).

### Método de Fisher

- El método de Fisher combina con `−2 Σ ln p`.

🎯 **Por qué importa (clase B28-C13):** Un valor p de `5 × 10⁻⁸` y una tasa de falsas alarmas de uno por 203 000 años no son comparables sin traducirlos a la misma escala. La decisión central: ¿cuántas sigmas equivale un valor p, cómo se corrige por las pruebas realizadas y cómo se combinan evidencias independientes?

📘 **Dónde se aprende** (1 clase): [B28-C13 · Estadística de significancia](../programa/clases/B28/B28-C13-estadistica-de-significancia/CLASE.md).

### Método de Gibbs

- El método de Gibbs halla la velocidad central con tres vectores de posición coplanares.

💡 **Cómo se explica en la clase [B74-C06](../programa/clases/B74/B74-C06-determinacion-inicial-de-orbita/CLASE.md):**
- Aplicar el método de Gibbs a tres posiciones coplanares.
- Hay inconsistencia; el método de Gibbs exige coplanaridad (se comprueba con el triple producto).
- 🎯 **Por qué importa:** Un ajuste por mínimos cuadrados converge solo si parte cerca de la solución. La decisión central: ¿qué método entrega una buena velocidad inicial con las observaciones disponibles, y cuánto empeora con el ruido y con poca separación angular?

📘 **Dónde se aprende** (1 clase): [B74-C06 · Determinación inicial de órbita](../programa/clases/B74/B74-C06-determinacion-inicial-de-orbita/CLASE.md).

### Método de Hamilton

- Sobresuscripción: horas pedidas entre horas disponibles. Método de Hamilton: parte entera y se reparten los restos mayores.

💡 **Cómo se explica en la clase [B48-C02](../programa/clases/B48/B48-C02-concesion-de-tiempo-de-observacion/CLASE.md):**
- Repartir horas enteras con el método de Hamilton.
- 🎯 **Por qué importa:** Un reparto sin regla clara genera conflicto, y uno sin clima genera promesas incumplibles. La decisión central: ¿cuántas horas se asignan y cuántas se esperan efectivas?

📘 **Dónde se aprende** (1 clase): [B48-C02 · Concesión de tiempo de observación](../programa/clases/B48/B48-C02-concesion-de-tiempo-de-observacion/CLASE.md).

### Método de Heun

- El método de Heun da, para `s′ = F(t, s)`: `k₁ = F(t_k, s_k)`;

💡 **Cómo se explica en la clase [B11-C06](../programa/clases/B11/B11-C06-metodo-de-heun/CLASE.md):**
- Aplicar a mano el método de Heun (predictor y corrector).
- python programa/clases/B11/B11-C06-metodo-de-heun/heun_frente_a_euler.py
- 🎯 **Por qué importa:** Una evaluación de `F` en un cálculo de trayectorias es cara cuando incluye gravedad de varios cuerpos o un modelo de atmósfera. La pregunta práctica es siempre cuánta precisión compra cada evaluación.

📘 **Dónde se aprende** (1 clase): [B11-C06 · Método de Heun](../programa/clases/B11/B11-C06-metodo-de-heun/CLASE.md).

### Método de la deriva

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B43-C17):** La alineación polar se corrige midiendo la deriva de una estrella. La decisión central: ¿qué deriva produce un error de acimut o de altura y cómo se invierte para corregirlo?

📘 **Dónde se aprende** (1 clase): [B43-C17 · Alineación polar](../programa/clases/B43/B43-C17-alineacion-polar/CLASE.md).

### Método de Lindstedt–Poincaré

- El método de Lindstedt–Poincaré reescala el tiempo para eliminar términos seculares.

🎯 **Por qué importa (clase B72-C15):** Una fórmula de primer orden se usa mucho tiempo sin preguntar cuándo deja de valer. La decisión central: ¿cómo saber cuándo basta un desarrollo de primer orden y cómo se estima su error?

📘 **Dónde se aprende** (1 clase): [B72-C15 · Aproximaciones perturbativas](../programa/clases/B72/B72-C15-aproximaciones-perturbativas/CLASE.md).

### Método de líneas

- El método de líneas discretiza el espacio y deja el tiempo continuo, de modo que un integrador de EDO resuelve el sistema semidiscreto.

🎯 **Por qué importa (clase B23-C04):** Un modelo de conducción de calor en el regolito, con una fuente variable y una condición de flujo en el borde, no tiene solución cerrada. Pero su código puede estar mal en la frontera, en el término fuente o en el tiempo, y ninguna propiedad global lo delata fácilmente.

📘 **Dónde se aprende** (1 clase): [B23-C04 · Soluciones de referencia y manufactured solutions](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md).

### Método de los cascarones

- El método de los cascarones suma cilindros huecos de radio `r` y altura `h(r)`: `V = ∫ 2π r h(r) dr`.

🎯 **Por qué importa (clase B09-C13):** Un telescopio necesita un espejo con forma de paraboloide. Cuánto vidrio hay que retirar de un disco plano para darle forma, cuánto pesa, y cuánta superficie hay que aluminizar son preguntas de volumen y área.

📘 **Dónde se aprende** (1 clase): [B09-C13 · Áreas y volúmenes por integración](../programa/clases/B09/B09-C13-areas-y-volumenes-por-integracion/CLASE.md).

### Método de los discos

- El método de los discos suma discos de radio `f(x)`: `V = ∫ π f(x)² dx`.

🎯 **Por qué importa (clase B09-C13):** Un telescopio necesita un espejo con forma de paraboloide. Cuánto vidrio hay que retirar de un disco plano para darle forma, cuánto pesa, y cuánta superficie hay que aluminizar son preguntas de volumen y área.

📘 **Dónde se aprende** (1 clase): [B09-C13 · Áreas y volúmenes por integración](../programa/clases/B09/B09-C13-areas-y-volumenes-por-integracion/CLASE.md).

### Método de malla

- Un método de malla divide el espacio en celdas.

💡 **Cómo se explica en la clase [B38-C06](../programa/clases/B38/B38-C06-hidrodinamica-en-simulaciones-sph-y-metodos-de-malla/CLASE.md):**
- Como una fila de coches que frena de golpe: un método sigue cada coche (partículas), el otro mide el tráfico en cada tramo de carretera (malla); ambos ven la onda de frenado, pero la marcan con errores distintos.
- python programa/clases/B38/B38-C06-hidrodinamica-en-simulaciones-sph-y-metodos-de-malla/tubo.py
- 🎯 **Por qué importa:** Cada método tiene errores distintos en choques y discontinuidades de contacto. La decisión central: ¿qué error comete cada método frente a una solución exacta y cómo cambia con la resolución?

📘 **Dónde se aprende** (1 clase): [B38-C06 · Hidrodinámica en simulaciones: SPH y métodos de malla](../programa/clases/B38/B38-C06-hidrodinamica-en-simulaciones-sph-y-metodos-de-malla/CLASE.md).

### Método de momentos

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B33-C03):** Las decisiones de protección se basan en periodos de retorno que superan al registro. La decisión central: ¿qué nivel se espera una vez cada T años y cuán incierto es?

📘 **Dónde se aprende** (1 clase): [B33-C03 · Eventos extremos históricos de clima espacial](../programa/clases/B33/B33-C03-eventos-extremos-historicos-de-clima-espacial/CLASE.md).

### Método de Monte Carlo

- El método de Monte Carlo del JCGM 101 propaga las distribuciones completas de las entradas, evaluando el modelo en muchas combinaciones sorteadas (S2).
- El método de Monte Carlo propaga distribuciones por muestreo.
- El método de Monte Carlo sortea los errores y calcula el resultado de cada sorteo.

💡 **Cómo se explica en la clase [B12-C16](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md):**
- *Descripción textual:* de las entradas con su incertidumbre se parte a dos métodos; el del GUM linealiza el modelo y combina varianzas ponderadas por las sensibilidades; el de Monte Carlo sortea combinaciones y obtiene la distribución de salida; se comparan para decidir si la linealización es suficiente.
- Debe reportarse el intervalo por Monte Carlo y el método.
- 🎯 **Por qué importa:** Casi todo resultado en ciencias espaciales es una función de medidas: una velocidad a partir de un radio, una distancia a partir de una paralaje, una masa a partir de un período. Dar el valor sin su incertidumbre no permite comparar con otros resultados ni decidir si cumple un requisito.

📘 **Dónde se aprende** (3 clases): [B12-C16 · Propagación de incertidumbre](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md); [B13-C13 · Presupuestos de incertidumbre](../programa/clases/B13/B13-C13-presupuestos-de-incertidumbre/CLASE.md); [B50-C13 · Análisis Monte Carlo de tolerancias ópticas](../programa/clases/B50/B50-C13-analisis-monte-carlo-de-tolerancias-opticas/CLASE.md).

### Método de Newton

- El método de Newton mejora una estimación restando el residuo dividido por la derivada.
- El método de Newton para `f(x) = 0` itera `x ← x − f(x)/f′(x)`; para minimizar `g`, se aplica a `g′`.

💡 **Cómo se explica en la clase [B09-C06](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md):**
- El método de Newton converge en pocos pasos si el inicio es razonable (S2 lo propone).
- Resolver la ecuación de Kepler con el método de Newton y verificar el residuo.
- ⚠️ **Error frecuente:** Detener el método de Newton sin comprobar el residuo. Se corrige en el paso 5 del ejemplo trabajado.
- 🎯 **Por qué importa:** Para saber dónde está un planeta en su órbita en un instante dado hay que resolver la ecuación de Kepler, `M = E − e sin E`, que no tiene solución en funciones elementales: no se puede despejar `E`.

📘 **Dónde se aprende** (2 clases): [B09-C06 · Derivación implícita](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md); [B11-C17 · Optimización numérica](../programa/clases/B11/B11-C17-optimizacion-numerica/CLASE.md).

### Método de Otsu

- El método de Otsu elige `T` maximizando la varianza entre clases `σ_b² = ω₀ ω₁ (μ₀ − μ₁)²`, donde `ω₀` y `ω₁` son las fracciones de píxeles de cada clase y `μ₀`, `μ₁` sus medias (no se consultó el artículo original: aquí se define y verifica por su propiedad).

💡 **Cómo se explica en la clase [B15-C13](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md):**
- Ejercicio 12 · integrador. Elabora tu *máscara segmentada con métricas*: genera tu disco con oscurecimiento al borde y tres manchas, segmenta con Otsu global y con el método aplanado, calcula píxeles marcados, IoU, Dice, número de regiones y área como fracción del disco, y comenta por qué difieren.
- Tabla como la de la sección 12: Otsu global con decenas de veces más píxeles que la verdad y IoU muy baja; método aplanado con IoU superior a 0,9, tres regiones y área dentro de pocos por ciento de la verdadera.
- 🎯 **Por qué importa:** Medir el área de las manchas solares, el porcentaje de nubes de una escena o el tamaño de un cráter exige delimitar el objeto. La delimitación no es neutra: un umbral distinto cambia el área.

📘 **Dónde se aprende** (1 clase): [B15-C13 · Segmentación de imágenes](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md).

### Método de potencia mitad

- El método de potencia mitad estima `ζ ≈ (f₂ − f₁)/(2 f_pico)`.

💡 **Cómo se explica en la clase [B84-C33](../programa/clases/B84/B84-C33-respuesta-armonica-y-funciones-de-transferencia-estructural/CLASE.md):**
- Límite: con amortiguamiento no proporcional o modos muy cercanos, el método de potencia mitad falla.
- 🎯 **Por qué importa:** La función de transferencia dice cuánto se amplifica cada frecuencia entre el punto donde se excita y el punto donde se mide; es la herramienta que usan el análisis y el ensayo de barrido sinusoidal. La decisión central: ¿cuánto se amplifica la respuesta en cada frecuencia y cuánto amortiguamiento tiene cada modo?

📘 **Dónde se aprende** (1 clase): [B84-C33 · Respuesta armónica y funciones de transferencia estructural](../programa/clases/B84/B84-C33-respuesta-armonica-y-funciones-de-transferencia-estructural/CLASE.md).

### Método de proyección

- El método de proyección avanza la velocidad sin imponer la incompresibilidad y luego la corrige restando un gradiente.

💡 **Cómo se explica en la clase [B21-C04](../programa/clases/B21/B21-C04-ecuaciones-de-navier-stokes-y-dinamica-de-fluidos-computacional/CLASE.md):**
- El método de proyección separa ambos pasos: primero avanza ignorando la restricción y después proyecta sobre el conjunto de campos sin divergencia.
- Describir el método de proyección y el papel de la ecuación de Poisson de la presión.
- 🎯 **Por qué importa:** Un fluido aparece en casi toda la ingeniería aeroespacial: el aire alrededor de un cohete, el propelente que se mueve en un tanque, el refrigerante de un satélite.

📘 **Dónde se aprende** (1 clase): [B21-C04 · Ecuaciones de Navier-Stokes y dinámica de fluidos computacional](../programa/clases/B21/B21-C04-ecuaciones-de-navier-stokes-y-dinamica-de-fluidos-computacional/CLASE.md).

### Método de Stouffer

- El método de Stouffer combina con `Σ z/√k`.

🎯 **Por qué importa (clase B28-C13):** Un valor p de `5 × 10⁻⁸` y una tasa de falsas alarmas de uno por 203 000 años no son comparables sin traducirlos a la misma escala. La decisión central: ¿cuántas sigmas equivale un valor p, cómo se corrige por las pruebas realizadas y cómo se combinan evidencias independientes?

📘 **Dónde se aprende** (1 clase): [B28-C13 · Estadística de significancia](../programa/clases/B28/B28-C13-estadistica-de-significancia/CLASE.md).

### Método de un paso

- Un método de un paso avanza con `q_{k+1} = Φ(q_k, h)`.

💡 **Cómo se explica en la clase [B10-C20](../programa/clases/B10/B10-C20-cinematica-de-orientacion-satelital/CLASE.md):**
- *Descripción textual:* en cada paso se evalúa la derivada, se avanza con el método elegido, se renormaliza y se repite; al final se compara con la solución exacta mediante el ángulo de la rotación relativa.
- Su límite: Euler se sale del círculo (la norma crece), RK4 casi lo sigue; un paso demasiado grande falla con cualquier método.
- 🎯 **Por qué importa:** Los giróscopos de un satélite miden la velocidad angular en ejes del cuerpo. Para saber hacia dónde apunta una cámara, hay que integrar esa velocidad en el tiempo, miles de veces.

📘 **Dónde se aprende** (1 clase): [B10-C20 · Cinemática de orientación satelital](../programa/clases/B10/B10-C20-cinematica-de-orientacion-satelital/CLASE.md).

### Método de verificación

- Un método de verificación puede ser análisis, prueba, inspección o demostración.

💡 **Cómo se explica en la clase [B118-C24](../programa/clases/B118/B118-C24-directrices-tecnicas-de-mitigacion-de-desechos-iadc-iso-24113/CLASE.md):**
- La edición de la norma, los requisitos aplicados, el método de verificación y la evidencia; la clase no consultó la norma.
- Ejercicio 12 · integrador. Integrador. Elabora tu *matriz de verificación de directrices*: requisito, valor, sección de la IADC Rev. 4, método, resultado de las nueve misiones sintéticas, casos de borde y la lista de qué es consultado, no consultado (ISO 24113) y sintético, con el aviso de que no es asesoría.
- 🎯 **Por qué importa:** B118-C11 enseña diseño para mitigación; ninguna clase trata las directrices de la IADC y de ISO ni su verificación. Un requisito sin criterio de aceptación y sin pruebas de borde se interpreta de distintas maneras.

📘 **Dónde se aprende** (1 clase): [B118-C24 · Directrices técnicas de mitigación de desechos (IADC, ISO 24113)](../programa/clases/B118/B118-C24-directrices-tecnicas-de-mitigacion-de-desechos-iadc-iso-24113/CLASE.md).

### Método de Welch

- El método de Welch divide la serie en segmentos (a veces solapados), calcula el periodograma de cada uno y los promedia (S1).
- El método de Welch promedia segmentos.

💡 **Cómo se explica en la clase [B15-C06](../programa/clases/B15/B15-C06-analisis-espectral-de-senales/CLASE.md):**
- Es el fundamento del método de Welch (S1), que además solapa los segmentos (por defecto la mitad, según S1) para aprovechar mejor los datos.
- El método de Welch lo suaviza con un coste en resolución.
- 🎯 **Por qué importa:** Alguien afirma: «hay un periodo de 3,7 días en esta estrella». ¿Cómo se sostiene?

📘 **Dónde se aprende** (2 clases): [B15-C06 · Análisis espectral de señales](../programa/clases/B15/B15-C06-analisis-espectral-de-senales/CLASE.md); [B28-C14 · Ruidos instrumentales](../programa/clases/B28/B28-C14-ruidos-instrumentales/CLASE.md).

### Método delta

- El método delta propaga la incertidumbre de `b₀, b₁` a `a₉₀`.

💡 **Cómo se explica en la clase [B84-C19](../programa/clases/B84/B84-C19-inspeccion-no-destructiva/CLASE.md):**
- Calcular una cota superior de confianza con el método delta.
- 🎯 **Por qué importa:** Decir «se inspeccionó» no dice qué se puede haber pasado por alto; la POD convierte la inspección en un tamaño de defecto garantizado que alimenta el cálculo de fatiga (C08). La decisión central: ¿qué tamaño de defecto detecta la inspección con 90 % de probabilidad y 95 % de confianza?

📘 **Dónde se aprende** (1 clase): [B84-C19 · Inspección no destructiva](../programa/clases/B84/B84-C19-inspeccion-no-destructiva/CLASE.md).

### Método explícito

- El método explícito calcula el paso nuevo solo con el estado actual; el implícito resuelve una ecuación en el estado nuevo.

🎯 **Por qué importa (clase B60-C03):** Si usas un integrador explícito en una red real, o no termina nunca, o explota. La decisión central: ¿qué integrador usar y con qué tolerancias, para que el resultado sea correcto y el coste razonable?

📘 **Dónde se aprende** (1 clase): [B60-C03 · Integración numérica de redes químicas rígidas](../programa/clases/B60/B60-C03-integracion-numerica-de-redes-quimicas-rigidas/CLASE.md).

### Método iterativo

- Un método iterativo parte de una estimación inicial y la mejora paso a paso.

💡 **Cómo se explica en la clase [B21-C03](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md):**
- Un método directo cuesta mucha memoria y trabajo; los métodos iterativos sacan partido de que cada ecuación es local.
- 🎯 **Por qué importa:** El potencial gravitatorio de una nube de gas, el potencial electrostático alrededor de una nave que se carga en el plasma y la presión en un fluido incompresible obedecen la misma ecuación: la de Poisson. Los códigos de simulación astrofísica la resuelven en cada paso de tiempo;

📘 **Dónde se aprende** (1 clase): [B21-C03 · Ecuación de Poisson: relajación y multigrid](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md).

### Método q

- El método q halla el autovector de mayor autovalor de la matriz `K` de Davenport.

💡 **Cómo se explica en la clase [B87-C09](../programa/clases/B87/B87-C09-estimacion-de-actitud/CLASE.md):**
- El método q arma `K = [[B + Bᵀ − tr B · I, z],[zᵀ, tr B]]` con `z = (B₂₃ − B₃₂, B₃₁ − B₁₃, B₁₂ − B₂₁)` y toma el autovector de mayor autovalor como `q`.
- Paso 5 · Comprobación. El método q da lo mismo: diferencia `2,7e-13°`.
- 🎯 **Por qué importa:** Cada sensor de vector da solo dos grados de libertad; la actitud completa exige combinarlos. La decisión central: ¿qué método usar, cómo ponderar el sensor mejor y cuánto importa el ángulo entre los vectores?

📘 **Dónde se aprende** (1 clase): [B87-C09 · Estimación de actitud](../programa/clases/B87/B87-C09-estimacion-de-actitud/CLASE.md).

### Método RK4 clásico

- El método RK4 clásico calcula cuatro pendientes por paso: `k₁ = F(t_k, s_k)`;

🎯 **Por qué importa (clase B11-C07):** La mayoría de los programas de simulación científica usa, de forma directa o como base, un método de la familia Runge–Kutta. Entender RK4 permite leer cualquier código de propagación, estimar cuántos pasos necesita una órbita y saber en qué punto empieza a ser conveniente algo más sofisticado.

📘 **Dónde se aprende** (1 clase): [B11-C07 · Runge-Kutta de cuarto orden](../programa/clases/B11/B11-C07-runge-kutta-de-cuarto-orden/CLASE.md).

### Método voraz

- El método voraz ordena por ganancia de `ln R` por kg; la enumeración prueba todos los casos.

💡 **Cómo se explica en la clase [B83-C23](../programa/clases/B83/B83-C23-redundancia-y-tolerancia-a-fallos-de-mision/CLASE.md):**
- Con un presupuesto de 3,0 kg el método voraz duplica la rueda y el controlador (2,1 kg) y llega a 61,10 % (+17,59 puntos).
- Asignar redundancia bajo un presupuesto de masa por un método voraz y por enumeración.
- 🎯 **Por qué importa:** Duplicar todo es imposible por masa y a veces contraproducente; no duplicar nada deja una misión frágil. La decisión central: ¿qué unidades duplicar, con qué esquema y cuánta confiabilidad compra cada kilogramo?

📘 **Dónde se aprende** (1 clase): [B83-C23 · Redundancia y tolerancia a fallos de misión](../programa/clases/B83/B83-C23-redundancia-y-tolerancia-a-fallos-de-mision/CLASE.md).

### Métodos

- Los métodos `T` (prueba: ejecutar y medir), `A` (análisis: cálculo o modelo), `I` (inspección: revisar el producto o documento) y `D` (demostración: mostrar una función).

💡 **Cómo se explica en la clase [B88-C20](../programa/clases/B88/B88-C20-plan-de-verificacion-de-computador-de-vuelo/CLASE.md):**
- En el ejemplo, el método usado en cada caso coincide con el previsto para su requisito: lista vacía de incoherencias.
- *Descripción textual:* requisitos y casos se cruzan en la matriz, de la que salen la cobertura, los requisitos sin caso, los huérfanos y la coherencia de métodos.
- 🎯 **Por qué importa:** Un requisito sin caso es una promesa sin evidencia; un caso sin requisito es esfuerzo sin objeto. La decisión central: ¿cada requisito tiene al menos un caso adecuado, y cada caso responde a un requisito?

📘 **Dónde se aprende** (1 clase): [B88-C20 · Plan de verificación de computador de vuelo](../programa/clases/B88/B88-C20-plan-de-verificacion-de-computador-de-vuelo/CLASE.md).

### Métodos de verificación

- Los métodos de verificación son análisis (A), inspección (I), demostración (D) y ensayo (T, *test*).

💡 **Cómo se explica en la clase [B83-C04](../programa/clases/B83/B83-C04-requisitos-verificables/CLASE.md):**
- *Descripción textual:* un enunciado pasa cinco filtros (modal, ambigüedad, atomicidad, valor medible y método de verificación); solo si los supera todos es un requisito verificable.
- Seis cumplen todas las reglas; los otros 14 defectos se reparten así: R1 (sin «deberá») 1, R2 (ambigüedad) 5, R3 (no atómico) 1, R4 (sin valor medible) 5 y R5 (sin método de verificación) 2.
- 🎯 **Por qué importa:** Un requisito vago («resolución adecuada») no puede aprobarse ni suspenderse: bloquea el diseño y siembra disputas. La decisión central: ¿este enunciado se puede comprobar con un método y un criterio de aceptación?

📘 **Dónde se aprende** (1 clase): [B83-C04 · Requisitos verificables](../programa/clases/B83/B83-C04-requisitos-verificables/CLASE.md).

### Métrica

- Una métrica es una regla `ds² = g_{μν} dx^μ dx^ν` que da el intervalo entre eventos cercanos.
- La métrica `g_ab` es un tensor simétrico que da el producto interno.
- Registro (*log*): línea de texto con un evento. Métrica: serie numérica.

💡 **Cómo se explica en la clase [B26-C07](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md):**
- RS --> G["Métrica ds² con factor 1 − r_s/r"]
- *Descripción textual:* la masa fija `r_s`; el factor `1 − r_s/r` aparece en la métrica; la distancia propia radial integra su raíz inversa y resulta mayor que la diferencia de coordenadas.
- 🎯 **Por qué importa:** Medir una distancia cerca de una masa grande no da lo mismo que en el espacio plano: el radio de un círculo y su circunferencia dejan de cumplir `C = 2πR`. Los GPS, las lentes gravitacionales y los agujeros negros dependen de esa diferencia.

📘 **Dónde se aprende** (3 clases): [B26-C07 · Curvatura y métricas](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md); [B39-C01 · Variedades, tensor métrico y geometría diferencial](../programa/clases/B39/B39-C01-variedades-tensor-metrico-y-geometria-diferencial/CLASE.md); [B48-C23 · Observabilidad del software de observatorio: registros, métricas y alertas](../programa/clases/B48/B48-C23-observabilidad-del-software-de-observatorio-registros-metricas-y-alertas/CLASE.md).

### Métrica de campo débil

- La métrica de campo débil es `ds² = −(1+2Φ/c²)c²dt² + (1−2Φ/c²)dx²`.

💡 **Cómo se explica en la clase [B26-C09](../programa/clases/B26/B26-C09-relatividad-general-introductoria/CLASE.md):**
- Con la métrica de campo débil, la velocidad coordenada de la luz es `c(1 + 2Φ/c²)` y el índice efectivo es `n = 1 + 2GM/(c²r)`.
- Escribir la métrica de campo débil en función del potencial.
- 🎯 **Por qué importa:** La luz de una estrella lejana que pasa cerca del Sol, o de una galaxia, se desvía: es la base de las lentes gravitacionales que miden masas de cúmulos (C18) y de las correcciones al seguimiento de naves en el espacio profundo.

📘 **Dónde se aprende** (1 clase): [B26-C09 · Relatividad general introductoria](../programa/clases/B26/B26-C09-relatividad-general-introductoria/CLASE.md).

### Métrica de Schwarzschild

- La métrica de Schwarzschild describe el vacío alrededor de una masa esférica.

💡 **Cómo se explica en la clase [B26-C07](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md):**
- Forma cerrada: exacta para la métrica de Schwarzschild.
- Calcular la distancia propia radial entre dos radios en la métrica de Schwarzschild.
- 🎯 **Por qué importa:** Medir una distancia cerca de una masa grande no da lo mismo que en el espacio plano: el radio de un círculo y su circunferencia dejan de cumplir `C = 2πR`. Los GPS, las lentes gravitacionales y los agujeros negros dependen de esa diferencia.

📘 **Dónde se aprende** (1 clase): [B26-C07 · Curvatura y métricas](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md).

### Métrica de superficie

- Una métrica de superficie mide rasgos del texto, no su comprensión.

💡 **Cómo se explica en la clase [B128-C08](../programa/clases/B128/B128-C08-lenguaje-claro-y-redaccion-accesible/CLASE.md):**
- Límites: las métricas son de superficie; la heurística de pasivas puede fallar; no miden comprensión.
- 🎯 **Por qué importa:** El lenguaje claro ayuda a personas con dificultades de lectura, a quienes leen en una segunda lengua, a quien lee con prisa y a quien usa un lector de pantalla. La decisión central: ¿qué cambios hacen el texto más claro sin perder ninguna cifra ni ningún aviso de seguridad?

📘 **Dónde se aprende** (1 clase): [B128-C08 · Lenguaje claro y redacción accesible](../programa/clases/B128/B128-C08-lenguaje-claro-y-redaccion-accesible/CLASE.md).

### Métrica espacial

- La métrica espacial `γ_ij` es la de cada capa.

💡 **Cómo se explica en la clase [B39-C06](../programa/clases/B39/B39-C06-introduccion-a-la-relatividad-numerica-formalismo-3-1/CLASE.md):**
- *Descripción textual:* la métrica se descompone en lapso, desplazamiento y métrica espacial; las ligaduras se verifican y la evolución se valida por convergencia.
- 🎯 **Por qué importa:** Una simulación necesita un tiempo y un espacio. La decisión central: ¿cómo se separa el espacio-tiempo en capas y cómo se sabe que una evolución converge?

📘 **Dónde se aprende** (1 clase): [B39-C06 · Introducción a la relatividad numérica: formalismo 3+1](../programa/clases/B39/B39-C06-introduccion-a-la-relatividad-numerica-formalismo-3-1/CLASE.md).

### Metro

- El metro es la distancia que recorre la luz en el vacío en `1/299 792 458 s`.

💡 **Cómo se explica en la clase [B13-C06](../programa/clases/B13/B13-C06-patrones-de-longitud-y-tiempo/CLASE.md):**
- La definición del segundo y del metro es exacta (S1, S2).
- Explicar cómo el segundo y el metro se definen con constantes exactas y por qué eso los enlaza.
- ⚠️ **Error frecuente:** Pensar que la definición del metro es una regla. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Cuando un telémetro láser mide la distancia a la Luna, lo que mide es el tiempo que tarda un pulso en ir y volver. Un error de un nanosegundo en ese tiempo equivale a 15 centímetros de distancia.

📘 **Dónde se aprende** (1 clase): [B13-C06 · Patrones de longitud y tiempo](../programa/clases/B13/B13-C06-patrones-de-longitud-y-tiempo/CLASE.md).

### MEV

- La reserva de crecimiento es un porcentaje según madurez (comercial 5 %, modificado 10 %, nuevo 20 %, en desarrollo 30 %, valores de ejemplo). MEV (*maximum expected value*) es CBE más reserva.
- La CBE es la mejor estimación actual; la MEV, la masa máxima esperada, que añade el crecimiento por madurez.

💡 **Cómo se explica en la clase [B83-C09](../programa/clases/B83/B83-C09-presupuestos-de-masa/CLASE.md):**
- La reserva total es 7,910 kg (13,32 % de la CBE) y el MEV seco es 67,310 kg.
- Masa de lanzamiento MEV = 72,156 kg; margen 7,844 kg = 9,80 %.
- ⚠️ **Error frecuente:** Presentar CBE como valor final. Usa MEV y declara la reserva
- 🎯 **Por qué importa:** La masa crece durante el diseño casi siempre; un presupuesto sin reserva se rompe en la revisión crítica. La decisión central: ¿cuánto margen queda frente al límite si cada elemento crece como su madurez sugiere?

📘 **Dónde se aprende** (2 clases): [B83-C09 · Presupuestos de masa](../programa/clases/B83/B83-C09-presupuestos-de-masa/CLASE.md); [B124-C19 · Redacción de propuesta de misión](../programa/clases/B124/B124-C19-redaccion-de-propuesta-de-mision/CLASE.md).

### Mezcla

- El ordenamiento por mezcla divide la lista en dos, ordena cada mitad y las mezcla (se escribe con recursión: una función que se llama a sí misma con un problema menor).
- La mezcla (blending) es el solapamiento de PSF.
- Una mezcla combina números de átomos, no valores de `δ`.

💡 **Cómo se explica en la clase [B07-C18](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md):**
- Divide en mitades, las ordena recursivamente y mezcla dos listas ordenadas comparando sus cabezas.
- Con datos sintéticos de semilla 2026: con 100 elementos, inserción hizo 2485 comparaciones (teoría `n(n−1)/4 = 2475`) y mezcla 541; con 5000, inserción hizo 6 270 052 (teoría 6 248 750) y mezcla 55 167.
- 🎯 **Por qué importa:** Un catálogo estelar tiene millones de objetos. Buscar uno a uno es posible con diez planetas y ruinoso con diez millones.

📘 **Dónde se aprende** (3 clases): [B07-C18 · Algoritmos de búsqueda y ordenamiento](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md); [B45-C24 · Fotometría por ajuste de PSF](../programa/clases/B45/B45-C24-fotometria-por-ajuste-de-psf/CLASE.md); [B55-C13 · Isótopos como trazadores](../programa/clases/B55/B55-C13-isotopos-como-trazadores/CLASE.md).

### Mezcla completa (CSTR)

- Biorreactor: tanque con microorganismos que consumen materia orgánica. Mezcla completa (CSTR): tanque uniforme.

💡 **Cómo se explica en la clase [B106-C26](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md):**
- Cuatro personas con 20 L/día de agua gris (80 L/día) y DBO de 300 mg/L, con `k = 0,5 h⁻¹` (ilustrativo): una remoción del 90 % exige en mezcla completa `τ = 18,0 h` y 60 L; en flujo pistón, 4,6 h y 15 L; con 3 tanques, 6,9 h y 23 L.
- Para el 99 % la mezcla completa necesita 660 L y 3 tanques solo 73 L.
- ⚠️ **Error frecuente:** Dimensionar con la mezcla completa sin considerar etapas. Compara (8.2).
- 🎯 **Por qué importa:** Las aguas grises son el mayor volumen del lazo y su carga orgánica hay que destruirla antes de potabilizar. La decisión central: ¿qué volumen de biorreactor y qué desinfección dan la remoción y la reducción de microorganismos requeridas?

📘 **Dónde se aprende** (1 clase): [B106-C26 · Tratamiento de aguas grises en hábitats](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md).

### Mezcla de temperaturas

- Una mezcla de temperaturas es una suma ponderada de cuerpos negros de distintas `T`; sus pesos `wⱼ` son las contribuciones de cada temperatura de una rejilla.

💡 **Cómo se explica en la clase [B22-C04](../programa/clases/B22/B22-C04-inversion-espectral/CLASE.md):**
- Si ajustas un solo cuerpo negro a una mezcla, el optimizador devuelve una temperatura intermedia con una incertidumbre formal diminuta; la señal de alarma no es esa incertidumbre, sino el `χ²` por grado de libertad.
- Eso vale solo si el cuerpo negro puro es el modelo correcto: con una mezcla de temperaturas, la misma cifra sería engañosa (sección 8.5).
- 🎯 **Por qué importa:** Un espectro no trae escritas la temperatura ni la composición: trae un número de fotones por cada longitud de onda. Pasar de ahí a una propiedad física exige un modelo y una inversión.

📘 **Dónde se aprende** (1 clase): [B22-C04 · Inversión espectral](../programa/clases/B22/B22-C04-inversion-espectral/CLASE.md).

### Mezcla eutéctica

- Una mezcla eutéctica es la composición cuyo punto de fusión es el más bajo de la serie de mezclas; añadir un segundo componente baja el punto de fusión.

🎯 **Por qué importa (clase B06-C19):** Los estudios con el telescopio James Webb muestran que las nubes densas del medio interestelar tienen granos de polvo cubiertos de hielos con una variedad de moléculas, y que esos hielos contienen entre el 2 y el 19 % del carbono, oxígeno, nitrógeno y azufre disponibles (S1, resumen).

📘 **Dónde se aprende** (1 clase): [B06-C19 · Química de hielos y minerales](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md).

### Mezcla ideal

- Una mezcla ideal suma por fracción molar.

💡 **Cómo se explica en la clase [B79-C14](../programa/clases/B79/B79-C14-propiedades-de-gases-calientes/CLASE.md):**
- Límite: la mezcla ideal supone que las moléculas no interactúan ni se disocian.
- Límites: mezcla ideal sin disociación; los coeficientes valen solo en el rango publicado; no es un cálculo de equilibrio químico; los gases de combustión reales llevan más especies.
- 🎯 **Por qué importa:** B06-C09 trata gases en general; aquí hacen falta propiedades termofísicas a alta temperatura con fuente. Sin ellas, las toberas y las turbinas se dimensionan con un `γ` que no existe a 2000–3000 K.

📘 **Dónde se aprende** (1 clase): [B79-C14 · Propiedades de gases calientes](../programa/clases/B79/B79-C14-propiedades-de-gases-calientes/CLASE.md).

### Mezcla lineal

- La mezcla lineal supone `y = M a + ruido`.
- Una mezcla lineal pondera por fracción en masa.

💡 **Cómo se explica en la clase [B53-C29](../programa/clases/B53/B53-C29-imagenes-hiperespectrales-de-superficies-planetarias/CLASE.md):**
- Límite de la analogía: las mezclas reales no son siempre lineales: dependen del tamaño de grano y de la geometría.
- Ejercicio 9 · transferencia. Un cubo real tiene mezcla no lineal.
- 🎯 **Por qué importa:** Un píxel gris puede ser una mezcla de tres minerales. La decisión central: ¿qué abundancias explican el espectro de un píxel y con qué error, dado el ruido y la similitud entre miembros extremos?

📘 **Dónde se aprende** (2 clases): [B53-C29 · Imágenes hiperespectrales de superficies planetarias](../programa/clases/B53/B53-C29-imagenes-hiperespectrales-de-superficies-planetarias/CLASE.md); [B55-C14 · Química de regolitos](../programa/clases/B55/B55-C14-quimica-de-regolitos/CLASE.md).

### Mezcla perfecta

- La mezcla perfecta supone concentración uniforme.
- Renovaciones por hora (ACH): `Q·3600/V`. Mezcla perfecta: concentración uniforme en el recinto.
- Estado estacionario: concentración constante. Mezcla perfecta: composición uniforme en toda la cabina.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B63-C05](../programa/clases/B63/B63-C05-contencion-de-muestras-extraterrestres-instalaciones-y-principios/CLASE.md):**
- Con mezcla perfecta, `dC/dt = −ACH·C`, luego `C(t) = C₀ e^(−ACH·t)`.
- Y el modelo de mezcla perfecta es optimista: en una sala real hay zonas con aire estancado y el tiempo de limpieza es mayor.
- 🎯 **Por qué importa:** Contener no es un adjetivo: es un conjunto de diferencias de presión, flujos y filtros que se pueden calcular. La decisión central: ¿qué impide que el aire de la sala salga, y cuánto tarda en limpiarse si se contamina?

📘 **Dónde se aprende** (5 clases): [B63-C05 · Contención de muestras extraterrestres: instalaciones y principios](../programa/clases/B63/B63-C05-contencion-de-muestras-extraterrestres-instalaciones-y-principios/CLASE.md); [B90-C02 · Buenas prácticas de sala limpia](../programa/clases/B90/B90-C02-buenas-practicas-de-sala-limpia/CLASE.md); [B106-C04 · Control de dióxido de carbono](../programa/clases/B106/B106-C04-control-de-dioxido-de-carbono/CLASE.md); [B110-C02 · Protocolos operativos de aislamiento de un tripulante enfermo o contaminado](../programa/clases/B110/B110-C02-protocolos-operativos-de-aislamiento-de-un-tripulante-enfermo-o-contaminado/CLASE.md); [B117-C02 · Contención de riesgos biológicos y químicos en cabina](../programa/clases/B117/B117-C02-contencion-de-riesgos-biologicos-y-quimicos-en-cabina/CLASE.md).

### Mezclador

- El mezclador multiplica la señal por el oscilador local (LO).

💡 **Cómo se explica en la clase [B46-C07](../programa/clases/B46/B46-C07-receptores-superheterodinos/CLASE.md):**
- Señal e imagen son indistinguibles tras la mezcla: hay que filtrarlas antes o rechazarlas con la estructura del mezclador.
- Un mezclador real tiene ruido, pérdidas y espurios.
- 🎯 **Por qué importa:** La mezcla es lo que permite procesar en una banda cómoda, pero trae consigo una segunda frecuencia que cae en la misma FI. La decisión central: ¿qué rechazo de imagen exige el receptor y cómo se logra?

📘 **Dónde se aprende** (1 clase): [B46-C07 · Receptores superheterodinos](../programa/clases/B46/B46-C07-receptores-superheterodinos/CLASE.md).

### Mg#

- La forsterita (Mg₂SiO₄) y la fayalita (Fe₂SiO₄) son los extremos del olivino; la enstatita (MgSiO₃) es un piroxeno. Mg# es `Mg/(Mg+Fe)` en moles.

💡 **Cómo se explica en la clase [B55-C12](../programa/clases/B55/B55-C12-geoquimica-de-meteoritos/CLASE.md):**
- MOL --> RAT["cocientes Mg/Si, Fe/Si, Mg#"]
- Ejercicio 3 · casi autónomo. Calcula Mg# con 1,0241 mol de Mg y 0,09815 mol de Fe (sección 8.4).
- 🎯 **Por qué importa:** Un meteorito se describe por su análisis químico, pero lo que interesa es qué minerales lo forman y cómo se compara con otros materiales. La decisión central: ¿qué mezcla de minerales reproduce una composición de óxidos, y qué dicen sus cocientes frente a una referencia?

📘 **Dónde se aprende** (1 clase): [B55-C12 · Geoquímica de meteoritos](../programa/clases/B55/B55-C12-geoquimica-de-meteoritos/CLASE.md).

### Mg/m³

- ppm: partes por millón en volumen. mg/m³: masa por volumen de aire.

💡 **Cómo se explica en la clase [B106-C24](../programa/clases/B106/B106-C24-calidad-del-aire-y-limites-de-exposicion-en-cabina/CLASE.md):**
- Paso 2. 1 ppm de CO: `10⁻⁶·40,87·28,01·10³ = 1,145 mg/m³`.
- Con límites inventados, la tabla sintética de seis compuestos da `HI = 0,693` (dominante: compuesto E, 0,214), y duplicando E y triplicando D, `HI = 1,007 > 1` aunque ninguno supera su límite por separado. 1 ppm de CO vale 1,1449 mg/m³ a 101,3 kPa y 0,623 mg/m³ a 8 psia.
- 🎯 **Por qué importa:** Evaluar el aire exige límites y una regla para combinar contaminantes; ninguno basta por sí solo. La decisión central: ¿cumple una mezcla de contaminantes su límite combinado y qué compuesto la domina?

📘 **Dónde se aprende** (1 clase): [B106-C24 · Calidad del aire y límites de exposición en cabina](../programa/clases/B106/B106-C24-calidad-del-aire-y-limites-de-exposicion-en-cabina/CLASE.md).

### MHD ideal

- La MHD ideal es el modelo de fluido conductor con campo congelado.

💡 **Cómo se explica en la clase [B30-C09](../programa/clases/B30/B30-C09-magnetohidrodinamica/CLASE.md):**
- En MHD ideal, `∂B/∂t = ∇×(v×B)` (el campo se mueve con el fluido) y `ρ dv/dt = −∇p + (∇×B)×B/μ₀`.
- MHD["ecuaciones de la MHD ideal"] --> ON["ξ_tt = v_A² ξ_xx"]
- 🎯 **Por qué importa:** La velocidad de Alfvén fija cuánto tarda una perturbación en recorrer un lazo coronal o una línea de campo del viento solar. La decisión central: ¿con qué velocidad viaja una perturbación magnética y cómo cambia el tiempo de viaje en un medio estratificado?

📘 **Dónde se aprende** (1 clase): [B30-C09 · Magnetohidrodinámica](../programa/clases/B30/B30-C09-magnetohidrodinamica/CLASE.md).

### Micrometeoroide

- Micrometeoroide: partícula natural de polvo;

🎯 **Por qué importa (clase B106-C15):** Los impactos son raros pero catastróficos; el diseño elige espesor y separación para una probabilidad de no penetración. La decisión central: ¿qué pared y qué separación dan una probabilidad objetivo en la duración y la superficie de la misión?

📘 **Dónde se aprende** (1 clase): [B106-C15 · Protección frente a micrometeoritos](../programa/clases/B106/B106-C15-proteccion-frente-a-micrometeoritos/CLASE.md).

### Micronutrientes

- Los macronutrientes (N, P, K, Ca, Mg, S) se dan en mM; los micronutrientes (B, Mn, Zn, Cu, Mo, Fe) en décimas o centésimas de mg/L.

💡 **Cómo se explica en la clase [B115-C03](../programa/clases/B115/B115-C03-control-de-nutrientes-y-solucion-nutritiva/CLASE.md):**
- Micronutrientes: con las masas del texto (2,86 g/L de H₃BO₃, 1,81 de MnCl₂·4H₂O, 0,22 de ZnSO₄·7H₂O, 0,08 de CuSO₄·5H₂O y 0,09 de H₂MoO₄·H₂O con 85 % de MoO₃) el laboratorio calcula 0,500, 0,502, 0,050, 0,020 y 0,051 mg/L de B, Mn, Zn, Cu y Mo; el texto dice 0,5, 0,5, 0,05, 0,02 y 0,05: coinciden dentro del 2 %.
- Verificar una solución de micronutrientes contra las concentraciones publicadas.
- 🎯 **Por qué importa:** Una solución nutritiva que se repone «por conductividad» puede parecer estable y estar desequilibrada. La decisión central: ¿qué se mide, cada cuánto y qué se repone para que cada ion se mantenga cerca de su objetivo, y cuándo conviene renovar la solución?

📘 **Dónde se aprende** (1 clase): [B115-C03 · Control de nutrientes y solución nutritiva](../programa/clases/B115/B115-C03-control-de-nutrientes-y-solucion-nutritiva/CLASE.md).

### Micropaso

- El paso y el micropaso.

💡 **Cómo se explica en la clase [B43-C15](../programa/clases/B43/B43-C15-motores-paso-a-paso-y-servomotores/CLASE.md):**
- M["200 pasos × micropasos"] --> RES["resolución"]
- *Descripción textual:* las corrientes definen el micropaso; la carga lo desplaza; las ganancias fijan ω_n y ζ y con ellas el sobreimpulso.
- 🎯 **Por qué importa:** El motor fija la resolución, la fuerza útil y la estabilidad del lazo. La decisión central: ¿cuánto se desvía un motor paso a paso bajo carga y qué ganancias dan una respuesta de servo sin sobreimpulso excesivo?

📘 **Dónde se aprende** (1 clase): [B43-C15 · Motores paso a paso y servomotores](../programa/clases/B43/B43-C15-motores-paso-a-paso-y-servomotores/CLASE.md).

### Micropropulsión

- La micropropulsión cubre empujes de micronewton a newton.

💡 **Cómo se explica en la clase [B78-C11](../programa/clases/B78/B78-C11-micropropulsion-para-cubesat/CLASE.md):**
- La evidencia es la presupuesto de micropropulsión de un CubeSat del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *presupuesto de micropropulsión de un CubeSat*: tabla de cinco opciones, impulsos totales consultados, límite por potencia y lista de lo consultado e ilustrativo.
- 🎯 **Por qué importa:** Un propulsor de alto `Isp` ahorra propelente pero empuja poco y tarda semanas; uno de empuje alto gasta más volumen de propelente. La decisión central: ¿qué tecnología cumple un Δv dado con una masa, un volumen y una potencia que un CubeSat sí puede dar?

📘 **Dónde se aprende** (1 clase): [B78-C11 · Micropropulsión para CubeSat](../programa/clases/B78/B78-C11-micropropulsion-para-cubesat/CLASE.md).

### Microtira

- La microtira es una pista en la capa externa sobre un plano de masa con un dieléctrico entre ambos.

💡 **Cómo se explica en la clase [B93-C01](../programa/clases/B93/B93-C01-diseno-de-pcb-espacial-conceptual/CLASE.md):**
- Las notas de curso de la UCSB dan para microtira `W = h` sobre epoxi-vidrio `εr = 4,8`: `ε_eff = 3,4`, `v = 0,54 c`, `Z0 = 68 Ω`.
- Límite: la fórmula de corriente es empírica y no incluye planos de cobre cercanos ni el vacío del espacio; la de `Z0` es una aproximación de la microtira ideal.
- 🎯 **Por qué importa:** El tronco no trataba el diseño de placas: B90 integra y B86 trata potencia, pero nadie calculaba una pista. La decisión central: ¿qué ancho de cobre y qué geometría de microtira necesita una placa para llevar una corriente y una señal dadas, y qué margen queda?

📘 **Dónde se aprende** (1 clase): [B93-C01 · Diseño de PCB espacial (conceptual)](../programa/clases/B93/B93-C01-diseno-de-pcb-espacial-conceptual/CLASE.md).

### Microturbulencia

- La microturbulencia es a escalas menores que el recorrido de un fotón.

💡 **Cómo se explica en la clase [B32-C06](../programa/clases/B32/B32-C06-micro-y-macroturbulencia-y-granulacion-estelar/CLASE.md):**
- *Descripción textual:* la velocidad térmica y la microturbulencia se suman en cuadratura; la macroturbulencia se convoluciona y suma otra varianza sin cambiar el área.
- Una línea de Fe I (525 nm) a 5772 K tiene `v_th = 1,311 km/s`; con microturbulencia de 1 km/s, `1,649 km/s`; con macroturbulencia de 3 km/s, un ancho de `5,995 pm`.
- 🎯 **Por qué importa:** Atribuir mal el ensanchamiento sesga la rotación y la abundancia. La decisión central: ¿cuánto aporta cada efecto al ancho de la línea?

📘 **Dónde se aprende** (1 clase): [B32-C06 · Micro y macroturbulencia y granulación estelar](../programa/clases/B32/B32-C06-micro-y-macroturbulencia-y-granulacion-estelar/CLASE.md).

### Miembro extremo

- El miembro extremo es el espectro de un material puro.
- Un miembro extremo es el espectro de un material puro.
- Un miembro extremo (*endmember*) es el espectro de un mineral puro.

💡 **Cómo se explica en la clase [B53-C29](../programa/clases/B53/B53-C29-imagenes-hiperespectrales-de-superficies-planetarias/CLASE.md):**
- M["miembros extremos (50 bandas)"] --> Y["pixel = M a + ruido"]
- *Descripción textual:* Los miembros extremos y las abundancias forman el espectro del píxel; los mínimos cuadrados las recuperan y se compara su error con la teoría.
- 🎯 **Por qué importa:** Un píxel gris puede ser una mezcla de tres minerales. La decisión central: ¿qué abundancias explican el espectro de un píxel y con qué error, dado el ruido y la similitud entre miembros extremos?

📘 **Dónde se aprende** (3 clases): [B53-C29 · Imágenes hiperespectrales de superficies planetarias](../programa/clases/B53/B53-C29-imagenes-hiperespectrales-de-superficies-planetarias/CLASE.md); [B57-C22 · Espectrómetros de imagen e hiperespectrales](../programa/clases/B57/B57-C22-espectrometros-de-imagen-e-hiperespectrales/CLASE.md); [B59-C05 · Minerales marcianos](../programa/clases/B59/B59-C05-minerales-marcianos/CLASE.md).

### MIFR

- El MIFR es el registro de frecuencias.
- El MIFR es el Registro Internacional de Frecuencias.

💡 **Cómo se explica en la clase [B119-C09](../programa/clases/B119/B119-C09-derecho-y-normas-de-telecomunicaciones/CLASE.md):**
- Describir lo que hace la UIT-R: notificación, coordinación, MIFR e interferencia perjudicial.
- La examina, aplica la coordinación y la inscribe en el MIFR (S4).
- 🎯 **Por qué importa:** Ninguna clase anterior vincula el derecho de telecomunicaciones con el cálculo de interferencia; B120 trata licencias y espectro en detalle y esta clase fija el marco.

📘 **Dónde se aprende** (2 clases): [B119-C09 · Derecho y normas de telecomunicaciones](../programa/clases/B119/B119-C09-derecho-y-normas-de-telecomunicaciones/CLASE.md); [B120-C01 · Licencias satelitales y procedimiento de notificación](../programa/clases/B120/B120-C01-licencias-satelitales-y-procedimiento-de-notificacion/CLASE.md).

### Migración de celda

- La migración de celda es el desplazamiento del eco entre celdas de alcance durante la apertura.

💡 **Cómo se explica en la clase [B69-C02](../programa/clases/B69/B69-C02-formacion-de-imagenes-sar/CLASE.md):**
- En el dominio alcance–Doppler la migración es `ΔR(f_D) = λ²R₀f_D²/(8v²)`; se desplaza cada línea en esa cantidad y luego se comprime con la referencia hiperbólica de cada celda.
- *Descripción textual:* el eco crudo se comprime en alcance, se corrige la migración de celda y se comprime en azimut para obtener la imagen compleja.
- 🎯 **Por qué importa:** Sin procesamiento, un eco crudo parece ruido. La decisión central: ¿qué operaciones convierten el eco crudo en una imagen con la resolución teórica, y cuándo fallan?

📘 **Dónde se aprende** (1 clase): [B69-C02 · Formación de imágenes SAR](../programa/clases/B69/B69-C02-formacion-de-imagenes-sar/CLASE.md).

### Migración de tipo I

- La migración de tipo I es el cambio de órbita de un planeta pequeño por el par de torsión neto del disco.

💡 **Cómo se explica en la clase [B52-C06](../programa/clases/B52/B52-C06-migracion-de-planetas/CLASE.md):**
- Un planeta grande abre un hueco y migra con otra ley (tipo II), que no se trata aquí.
- Migra con la evolución viscosa del disco (tipo II), fuera de este modelo.
- 🎯 **Por qué importa:** La migración explica por qué las órbitas finales no coinciden con los lugares de formación. La decisión central: ¿en cuánto tiempo cae un planeta al interior y cómo depende de su masa?

📘 **Dónde se aprende** (1 clase): [B52-C06 · Migración de planetas](../programa/clases/B52/B52-C06-migracion-de-planetas/CLASE.md).

### Milibar

- Un milibar (mb) es `100 Pa` por definición de bar (`1 bar = 10⁵ Pa`), así que `1014 mb = 101,4 kPa`.

💡 **Cómo se explica en la clase [B05-C14](../programa/clases/B05/B05-C14-gases-y-presion/CLASE.md):**
- Definir presión y convertir entre pascal, milibar y otras unidades.
- 🎯 **Por qué importa:** La cabina de una nave contiene aire a una presión que debe mantenerse, y una escotilla soporta decenas de miles de newtons. La pregunta motivadora es: ¿qué relaciona presión, volumen, temperatura y cantidad de gas, y cómo cambia la presión con la altura en una atmósfera?

📘 **Dónde se aprende** (1 clase): [B05-C14 · Gases y presión](../programa/clases/B05/B05-C14-gases-y-presion/CLASE.md).

### Milisegundo de arco

- Un milisegundo de arco (mas) es `10⁻³″`.

💡 **Cómo se explica en la clase [B04-C07](../programa/clases/B04/B04-C07-triangulos-y-distancias-angulares/CLASE.md):**
- Para Próxima Centauri, `p = 768,5 ± 0,2 mas` (milisegundos de arco;
- Ejercicio 9 · transferencia. Un compañero calcula `d` con `p` en milisegundos de arco como si fueran segundos y obtiene `d = 1/768,5 = 0,0013 pc`.
- 🎯 **Por qué importa:** Nadie puede llevar una cinta métrica a una estrella. Pero sí se puede observar la misma estrella desde dos puntos separados una distancia conocida y medir cuánto cambia su dirección.

📘 **Dónde se aprende** (1 clase): [B04-C07 · Triángulos y distancias angulares](../programa/clases/B04/B04-C07-triangulos-y-distancias-angulares/CLASE.md).

### Milisegundo de arco (mas)

- Un milisegundo de arco (mas) es `1/3 600 000` de grado;

💡 **Cómo se explica en la clase [B13-C21](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md):**
- Calcular una separación angular de milisegundos de arco sin perder precisión.
- 🎯 **Por qué importa:** Para seguir una nave en el espacio profundo hay que decir en qué dirección está respecto de un marco fijo. Si el marco gira aunque sea un poco, todas las direcciones se desplazan.

📘 **Dónde se aprende** (1 clase): [B13-C21 · Sistema de referencia celeste ICRF y cuásares](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md).

### Millonésima de hemisferio (MSH)

- La millonésima de hemisferio (MSH) es la unidad de área de manchas.

💡 **Cómo se explica en la clase [B30-C04](../programa/clases/B30/B30-C04-manchas-solares/CLASE.md):**
- Una mancha ilustrativa de `r = 10 Mm` y `B = 0,3 T` tiene un área de `3,14 × 10¹⁴ m²` (103 millonésimas de hemisferio) y un flujo de `9,42 × 10¹³ Wb`.
- Convertir áreas a millonésimas de hemisferio.
- 🎯 **Por qué importa:** Las manchas son la huella visible del campo magnético y las más fáciles de contar. Cuantificar su presión, su brillo y su flujo permite relacionarlas con la irradiancia.

📘 **Dónde se aprende** (1 clase): [B30-C04 · Manchas solares](../programa/clases/B30/B30-C04-manchas-solares/CLASE.md).

### Miner

- Goodman: `S_ar = S_a/(1 − S_m/S_u)`. Miner: `D = Σ nᵢ/Nᵢ`; la falla se espera con `D = 1`.

💡 **Cómo se explica en la clase [B84-C08](../programa/clases/B84/B84-C08-fatiga-y-fractura/CLASE.md):**
- Miner es lineal y no ve el orden de las cargas.
- *Descripción textual:* los datos dan el tamaño crítico y los ciclos por dos vías (cerrada y numérica); por separado, Basquin y Miner dan el daño de un espectro.
- 🎯 **Por qué importa:** La mayoría de las fallas estructurales en servicio son por fatiga; saber cuántos ciclos quedan y qué grieta es tolerable decide si una pieza se acepta. La decisión central: ¿cuántos ciclos tarda una grieta inicial en llegar al tamaño crítico y cuánto daño acumula un espectro de cargas?

📘 **Dónde se aprende** (1 clase): [B84-C08 · Fatiga y fractura](../programa/clases/B84/B84-C08-fatiga-y-fractura/CLASE.md).

### Mineral

- Un mineral es un sólido cristalino natural de composición química definida: el olivino `(Mg,Fe)₂SiO₄` es una serie entre la forsterita `Mg₂SiO₄` y la fayalita `Fe₂SiO₄`; el piroxeno más sencillo es `MgSiO₃`; la calcita es `CaCO₃`.

💡 **Cómo se explica en la clase [B06-C19](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md):**
- En un modelo ilustrativo con sólo esos dos minerales, la fracción de silicio en olivino sería `1,23 − 1 = 0,23`: un 23 %.
- Es un ejercicio de aritmética, no una afirmación sobre la mineralogía de ningún cuerpo: faltan otros minerales y el Si y el Mg también están en otras fases.
- 🎯 **Por qué importa:** Los estudios con el telescopio James Webb muestran que las nubes densas del medio interestelar tienen granos de polvo cubiertos de hielos con una variedad de moléculas, y que esos hielos contienen entre el 2 y el 19 % del carbono, oxígeno, nitrógeno y azufre disponibles (S1, resumen).

📘 **Dónde se aprende** (1 clase): [B06-C19 · Química de hielos y minerales](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md).

### Mínima distancia

- Diccionario de fallas: conjunto de firmas. Mínima distancia: clasificar por la firma más cercana.

💡 **Cómo se explica en la clase [B96-C29](../programa/clases/B96/B96-C29-diagnostico-de-fallas-de-enlace/CLASE.md):**
- El método es estándar (clasificación por mínima distancia) y lo verifica el laboratorio; las firmas y los ruidos son sintéticos.
- D --> C["Clasificacion por minima distancia"]
- 🎯 **Por qué importa:** Perder tiempo de contacto buscando la causa equivocada es caro. La decisión central: ¿qué medidas distinguen las causas y cuáles se confunden entre sí?

📘 **Dónde se aprende** (1 clase): [B96-C29 · Diagnóstico de fallas de enlace](../programa/clases/B96/B96-C29-diagnostico-de-fallas-de-enlace/CLASE.md).

### Minimización

- La minimización es recoger solo lo necesario.

💡 **Cómo se explica en la clase [B129-C05](../programa/clases/B129/B129-C05-consentimiento-y-privacidad-de-participantes/CLASE.md):**
- D["Datos recogidos"] --> M["Minimizacion"]
- Aplicar el principio de minimización: recoger solo lo necesario para el fin declarado.
- ⚠️ **Error frecuente:** Pedir más datos «por si acaso». Minimiza según el fin declarado
- 🎯 **Por qué importa:** Cuando un conjunto de datos se publica o se comparte, los datos de las personas pueden permitir reconocerlas aunque se quite el nombre. La decisión central: ¿qué recoger, con qué precisión publicarlo y cómo respetar que alguien retire su consentimiento?

📘 **Dónde se aprende** (1 clase): [B129-C05 · Consentimiento y privacidad de participantes](../programa/clases/B129/B129-C05-consentimiento-y-privacidad-de-participantes/CLASE.md).

### Mínimo

- El mínimo `T*(φ)` es el tiempo de vuelo óptimo.
- Un conjunto de corte es una combinación que causa el evento superior; es mínimo si ningún subconjunto propio lo causa.
- El mínimo de `Dst*`.

💡 **Cómo se explica en la clase [B30-C18](../programa/clases/B30/B30-C18-tormentas-geomagneticas/CLASE.md):**
- El mínimo, en `t = 6 h`, es `−63,32 nT` (fórmula `−Q₀τ(1 − e^(−T/τ))`).
- El mínimo es proporcional a `Q₀` y satura hacia `−Q₀τ = −120 nT` al crecer `T`.
- 🎯 **Por qué importa:** Prever la profundidad y la duración de una tormenta orienta la protección de redes y satélites. La decisión central: ¿qué mínimo alcanza `Dst*` y cuánto tarda en recuperarse?

📘 **Dónde se aprende** (3 clases): [B30-C18 · Tormentas geomagnéticas](../programa/clases/B30/B30-C18-tormentas-geomagneticas/CLASE.md); [B75-C12 · Optimización de trayectoria](../programa/clases/B75/B75-C12-optimizacion-de-trayectoria/CLASE.md); [B83-C24 · Árboles de fallos (FTA) y análisis de causas](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md).

### Mínimo aceptable

- Un mínimo aceptable es el valor por debajo del cual el diseño es inaceptable para una misión dada.

💡 **Cómo se explica en la clase [B109-C07](../programa/clases/B109/B109-C07-asignacion-de-volumenes-habitables-por-tripulante/CLASE.md):**
- El mínimo aceptable depende del tamaño de la tripulación, de la duración y de las tareas.
- 🎯 **Por qué importa:** Una cifra de «metros cúbicos por persona» sin decir qué se descontó no se puede comparar. La decisión central: ¿cuánto volumen utilizable queda por tripulante y qué tan sensible es a lo que se descuenta?

📘 **Dónde se aprende** (1 clase): [B109-C07 · Asignación de volúmenes habitables por tripulante](../programa/clases/B109/B109-C07-asignacion-de-volumenes-habitables-por-tripulante/CLASE.md).

### Mínimo común múltiplo (mcm)

- Un calendario circular combina dos o más ciclos que se repiten juntos tras un número entero de vueltas; ese número es su mínimo común múltiplo (mcm).

💡 **Cómo se explica en la clase [B02-C01](../programa/clases/B02/B02-C01-calendarios-astronomicos-en-civilizaciones-antiguas/CLASE.md):**
- Calcular el mínimo común múltiplo de dos ciclos y explicar qué significa en un calendario circular.
- 🎯 **Por qué importa:** Un calendario es una promesa: «dentro de tantos días ocurrirá tal cosa en el cielo o en la tierra». Esa promesa solo se cumple si el calendario sigue algún ciclo natural.

📘 **Dónde se aprende** (1 clase): [B02-C01 · Calendarios astronómicos en civilizaciones antiguas](../programa/clases/B02/B02-C01-calendarios-astronomicos-en-civilizaciones-antiguas/CLASE.md).

### Mínimo local

- Un mínimo local es un punto donde la función no baja en su entorno; el global, el más bajo de todo el dominio.
- Un mínimo local es una solución que ningún paso del algoritmo mejora aunque exista otra mejor.

💡 **Cómo se explica en la clase [B11-C17](../programa/clases/B11/B11-C17-optimizacion-numerica/CLASE.md):**
- Descripción larga: sube desde 13 hasta un máximo local entre 13 y 50, baja hasta un mínimo en 94 y vuelve a subir porque el tiempo domina.
- Reconocer un mínimo en la frontera, un máximo local y un mínimo local.
- 🎯 **Por qué importa:** Diseñar una transferencia, ajustar un modelo a datos de seguimiento o calibrar un instrumento son problemas de optimización. Un algoritmo de búsqueda siempre devuelve *algún* número: la tarea del ingeniero es saber si es un mínimo, si es el global, si está en una frontera y con qué incertidumbre.

📘 **Dónde se aprende** (2 clases): [B11-C17 · Optimización numérica](../programa/clases/B11/B11-C17-optimizacion-numerica/CLASE.md); [B15-C23 · Clasificación no supervisada y agrupamiento de imágenes](../programa/clases/B15/B15-C23-clasificacion-no-supervisada-y-agrupamiento-de-imagenes/CLASE.md).

### Mínimos cuadrados

- Un residuo es `r_i = y_i − f(x_i; β)`. Mínimos cuadrados elige `β` para minimizar la suma de cuadrados `S(β) = Σ r_i²`; con pesos `1/σ_i²` es el estadístico `χ²` (S2 describe esa minimización con y sin `sigma`).
- Los mínimos cuadrados buscan `x` que minimiza `‖A x − y‖²`.
- El método de Newton para `f(x) = 0` itera `x ← x − f(x)/f′(x)`; para minimizar `g`, se aplica a `g′`. Mínimos cuadrados minimizan `Σ rᵢ²`.

💡 **Cómo se explica en la clase [B10-C07](../programa/clases/B10/B10-C07-proyecciones-y-minimos-cuadrados/CLASE.md):**
- Mínimos cuadrados penaliza los errores grandes al cuadrado y por eso es sensible; las alternativas robustas se verán en B22.
- Reconocer la sensibilidad de mínimos cuadrados a un dato atípico.
- 🎯 **Por qué importa:** Una estación mide la distancia a un satélite cada segundo durante diez segundos. Hay once medidas y solo tres parámetros que describir (posición, velocidad y aceleración radiales).

📘 **Dónde se aprende** (3 clases): [B10-C07 · Proyecciones y mínimos cuadrados](../programa/clases/B10/B10-C07-proyecciones-y-minimos-cuadrados/CLASE.md); [B11-C17 · Optimización numérica](../programa/clases/B11/B11-C17-optimizacion-numerica/CLASE.md); [B15-C16 · Ajuste de curvas](../programa/clases/B15/B15-C16-ajuste-de-curvas/CLASE.md).

### Mínimos cuadrados alternados

- Los mínimos cuadrados alternados (tipo StefCal).

💡 **Cómo se explica en la clase [B51-C03](../programa/clases/B51/B51-C03-ganancias-complejas-por-antena-y-soluciones-de-calibracion/CLASE.md):**
- Resolver `g_i` por mínimos cuadrados alternados (iteración con promedio).
- 🎯 **Por qué importa:** Sin ganancias el conjunto de datos no sirve para formar imágenes. La decisión central: ¿cómo se estiman las ganancias a partir de un modelo de cielo conocido y qué precisión se alcanza?

📘 **Dónde se aprende** (1 clase): [B51-C03 · Ganancias complejas por antena y soluciones de calibración](../programa/clases/B51/B51-C03-ganancias-complejas-por-antena-y-soluciones-de-calibracion/CLASE.md).

### Mínimos cuadrados no negativos

- Una mezcla de temperaturas es una suma ponderada de cuerpos negros de distintas `T`; sus pesos `wⱼ` son las contribuciones de cada temperatura de una rejilla. Mínimos cuadrados no negativos (NNLS) resuelven `min ‖A w − d‖` con `w ≥ 0` (S8).

💡 **Cómo se explica en la clase [B22-C04](../programa/clases/B22/B22-C04-inversion-espectral/CLASE.md):**
- Resolver con Tikhonov y con mínimos cuadrados no negativos, y comparar con la inversión ingenua.
- 🎯 **Por qué importa:** Un espectro no trae escritas la temperatura ni la composición: trae un número de fotones por cada longitud de onda. Pasar de ahí a una propiedad física exige un modelo y una inversión.

📘 **Dónde se aprende** (1 clase): [B22-C04 · Inversión espectral](../programa/clases/B22/B22-C04-inversion-espectral/CLASE.md).

### Mínimos cuadrados no negativos (NNLS)

- Los mínimos cuadrados no negativos (NNLS) buscan las abundancias que mejor ajustan sin salir de `a ≥ 0`.

💡 **Cómo se explica en la clase [B59-C05](../programa/clases/B59/B59-C05-minerales-marcianos/CLASE.md):**
- Resolver con mínimos cuadrados no negativos y contrastar con SciPy.
- 🎯 **Por qué importa:** Antes de excavar hay que saber qué se excava. La decisión central: ¿qué rendimiento de agua se espera de una mezcla y con qué dispersión por el ruido?

📘 **Dónde se aprende** (1 clase): [B59-C05 · Minerales marcianos](../programa/clases/B59/B59-C05-minerales-marcianos/CLASE.md).

### Mínimos cuadrados ordinarios

- Un modelo lineal en los parámetros escribe `y = Xβ + ε`, con `X` la matriz de diseño, `β` los parámetros y `ε` el error; no exige que sea lineal en `t` (un polinomio sigue siéndolo). Mínimos cuadrados ordinarios (OLS) elige `β̂` que minimiza la suma de cuadrados de los residuos; las ecuaciones normales son `XᵀX β̂ = Xᵀ y`.
- Los mínimos cuadrados ordinarios son el método que elige la recta que minimiza la suma de los residuos al cuadrado.

🎯 **Por qué importa (clase B12-C10):** Casi todo en ciencias espaciales es un ajuste: la deriva de un oscilador, la curva de luz de un tránsito, la degradación de una celda solar, la relación período–luminosidad. Un ajuste sin incertidumbre de parámetros ni diagnóstico de residuos es sólo una línea dibujada.

📘 **Dónde se aprende** (2 clases): [B12-C10 · Regresión lineal y no lineal](../programa/clases/B12/B12-C10-regresion-lineal-y-no-lineal/CLASE.md); [B13-C05 · Calibración instrumental](../programa/clases/B13/B13-C05-calibracion-instrumental/CLASE.md).

### Mínimos cuadrados reponderados iterativamente

- Un M-estimador minimiza una suma de pérdidas que crecen más despacio que el cuadrado; el de Huber usa pérdida cuadrática para residuos pequeños y lineal para grandes, y se calcula por mínimos cuadrados reponderados iterativamente (IRLS), con peso `w = 1` si `|r|/σ̂ ≤ k` y `w = k σ̂/|r|` si no (`k = 1,345` es el valor convencional).

🎯 **Por qué importa (clase B12-C11):** Los datos reales traen errores de transmisión, rayos cósmicos en un detector, una lectura perdida o un salto del sensor. Un solo punto muy alejado puede torcer la recta de mínimos cuadrados y producir parámetros y predicciones erróneos con errores típicos pequeños y engañosos.

📘 **Dónde se aprende** (1 clase): [B12-C11 · Regresión robusta](../programa/clases/B12/B12-C11-regresion-robusta/CLASE.md).

### Minuto

- El minuto (min), la hora (h) y el día (d) se aceptan con las equivalencias `1 min = 60 s`, `1 h = 60 min = 3600 s`, `1 d = 24 h = 86 400 s` (S2).

💡 **Cómo se explica en la clase [B03-C08](../programa/clases/B03/B03-C08-tiempo-y-conversiones-astronomicas/CLASE.md):**
- *Descripción textual:* dos entradas (tiempo en horas–minutos–segundos y ángulo en grados–minutos–segundos) se llevan a una unidad decimal; se opera allí; y, si hace falta, se regresa a la forma sexagesimal dividiendo y tomando el resto.
- Convertir entre segundos, minutos, horas y días con las equivalencias del SI.
- ⚠️ **Error frecuente:** Tratar los minutos como decimales (8,19 min por 8 min 19 s).
- 🎯 **Por qué importa:** El período de Neptuno en las fichas de la NASA es 60 189,018 días. Nadie piensa en 60 mil días; se piensa en años.

📘 **Dónde se aprende** (1 clase): [B03-C08 · Tiempo y conversiones astronómicas](../programa/clases/B03/B03-C08-tiempo-y-conversiones-astronomicas/CLASE.md).

### Minuto de arco

- El minuto de arco es 1/60 de grado.
- El grado (°) es `π/180` rad; el minuto de arco (′) es `1/60` de grado y el segundo de arco (″) es `1/60` de minuto de arco, es decir, `π/648 000` rad (S2).

💡 **Cómo se explica en la clase [B02-C12](../programa/clases/B02/B02-C12-tycho-brahe-y-observaciones-sistematicas/CLASE.md):**
- El sitio de la Universidad Rice indica que, antes de Tycho, los astrónomos eran generalmente exactos hasta unos 15 minutos de arco;
- ⚠️ **Error frecuente:** Confundir minuto de arco y de tiempo. Ejercicio 1.
- 🎯 **Por qué importa:** Una teoría solo es tan buena como los datos con que se contrasta. La pregunta motivadora es: ¿qué diferencia hay entre «mirar el cielo» y «observar sistemáticamente», y por qué esa diferencia cambió la astronomía?

📘 **Dónde se aprende** (2 clases): [B02-C12 · Tycho Brahe y observaciones sistemáticas](../programa/clases/B02/B02-C12-tycho-brahe-y-observaciones-sistematicas/CLASE.md); [B03-C08 · Tiempo y conversiones astronómicas](../programa/clases/B03/B03-C08-tiempo-y-conversiones-astronomicas/CLASE.md).

### MIoU

- El mIoU es el promedio de los IoU por clase.

💡 **Cómo se explica en la clase [B103-C05](../programa/clases/B103/B103-C05-segmentacion-semantica-de-superficies-planetarias/CLASE.md):**
- En la prueba del mismo dominio: exactitud 91,14 % (59 732 de 65 536 píxeles), IoU por clase 0,850; 0,871; 0,665 y 0,650, mIoU 0,759.
- Restar la media 31 × 31 y dividir por la desviación local hace las características invariantes a una ganancia y un desplazamiento: el resultado con y sin cambio es idéntico (79,91 %; mIoU 0,567).
- 🎯 **Por qué importa:** Un modelo que acierta el 91 % de los píxeles en el dominio de entrenamiento puede acertar el 45 % cuando cambia la luz. La decisión central: ¿qué métrica y qué prueba demuestran que un segmentador es utilizable en otras condiciones, y no solo en las de entrenamiento?

📘 **Dónde se aprende** (1 clase): [B103-C05 · Segmentación semántica de superficies planetarias](../programa/clases/B103/B103-C05-segmentacion-semantica-de-superficies-planetarias/CLASE.md).

### Misión de sobrevuelos

- Un orbitador se inserta en órbita alrededor de la luna; una misión de sobrevuelos no.

💡 **Cómo se explica en la clase [B75-C20](../programa/clases/B75/B75-C20-diseno-de-una-mision-a-luna-helada/CLASE.md):**
- Misión de sobrevuelos: sin inserción, más ciencia por pasada (C17).
- Ejercicio 9 · transferencia. Una misión de sobrevuelos de Europa (como Clipper) evita la inserción orbital.
- 🎯 **Por qué importa:** Antes de diseñar una misión hay que saber si es viable y qué la hace cara. La decisión central: ¿cuánto delta-v y cuánta masa cuesta ir de la Tierra a una luna de Júpiter, y cuánto se ahorra con una misión de sobrevuelos en lugar de un orbitador?

📘 **Dónde se aprende** (1 clase): [B75-C20 · Diseño de una misión a luna helada](../programa/clases/B75/B75-C20-diseno-de-una-mision-a-luna-helada/CLASE.md).

### Misma

- Dos cuaterniones opuestos, `q` y `−q`, representan la misma orientación.

💡 **Cómo se explica en la clase [B16-C20](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md):**
- A["q y −q<br/>misma orientación"] --> B["q_e = q_obj⁻¹ ⊗ q"]
- Combinando los tres ejes a lo largo de la diagonal, el par útil es hasta `0,5√3 = 0,87 N·m` y la misma estimación da `T ≈ 17 s` (una estimación gruesa, que supone inercia efectiva 40).
- 🎯 **Por qué importa:** Un telescopio debe girar desde una orientación a otra y quedarse allí. Con tres ejes acoplados y rotaciones grandes, ni los ángulos de Euler (tienen singularidades y dependen de la secuencia de giros) ni el modelo lineal bastan.

📘 **Dónde se aprende** (1 clase): [B16-C20 · Control de orientación en un simulador](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md).

### Mitigación

- Un riesgo es un evento posible con consecuencia; se acompaña de una mitigación.
- La mitigación reduce la generación de desechos.

💡 **Cómo se explica en la clase [B08-C20](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md):**
- Riesgos: sol y calor de día, frío y oscuridad de noche, caídas en terreno, vehículos, equipo volcado, fatiga al regresar, pérdida de adaptación a la oscuridad por luces; cada uno con su mitigación.
- 🎯 **Por qué importa:** Una salida sin plan termina en una noche perdida o en un accidente. La pregunta motivadora: ¿cómo preparo una salida de observación para que sea segura, útil, accesible y reproducible?

📘 **Dónde se aprende** (2 clases): [B08-C20 · Proyecto de campaña de observación nocturna](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md); [B118-C19 · Sostenibilidad y gobernanza orbital](../programa/clases/B118/B118-C19-sostenibilidad-y-gobernanza-orbital/CLASE.md).

### Mitigación de detección

- Una mitigación de detección baja `D`; una de diseño baja `O` o `S`.

💡 **Cómo se explica en la clase [B83-C22](../programa/clases/B83/B83-C22-analisis-de-modos-y-efectos-de-fallo-fmea-en-sistemas-espaciales/CLASE.md):**
- Reevaluar el RPN tras una mitigación de detección.
- El script [tabla_fmea.py](tabla_fmea.py) calcula RPN y probabilidades de misión de diez modos, el Pareto del 80 % y el efecto de una mitigación de detección (comprueba que RPN y probabilidades coinciden por dos vías, que las fracciones de modo suman 1 por componente y que mitigar reduce el RPN total).
- 🎯 **Por qué importa:** Los fallos que no se anticipan se descubren en órbita. La decisión central: ¿qué modos de fallo hay que atacar primero, cuánta probabilidad tienen en la vida de la misión y qué cambia si mejoro su detección?

📘 **Dónde se aprende** (1 clase): [B83-C22 · Análisis de modos y efectos de fallo (FMEA) en sistemas espaciales](../programa/clases/B83/B83-C22-analisis-de-modos-y-efectos-de-fallo-fmea-en-sistemas-espaciales/CLASE.md).

### Mixtas

- Las derivadas de segundo orden son `f_xx`, `f_yy` y las mixtas `f_xy = ∂²f/∂y∂x`.
- Las condiciones pueden ser de Dirichlet (valor de la función), Neumann (valor de la derivada) o mixtas.

💡 **Cómo se explica en la clase [B09-C16](../programa/clases/B09/B09-C16-derivadas-parciales/CLASE.md):**
- Comprobar la igualdad de las derivadas mixtas.
- Ejercicio 12 · integrador. Elabora tu *tabla de sensibilidades con propagación de incertidumbre*: parciales de `L`, derivada mixta, propagación lineal y Monte Carlo para dos pares de incertidumbres (sintéticas), y el hessiano del potencial Tierra–Luna en `x*`.
- 🎯 **Por qué importa:** La luminosidad de una estrella calculada con su radio y su temperatura tiene una incertidumbre que viene de las dos. ¿Cuál pesa más?

📘 **Dónde se aprende** (2 clases): [B09-C16 · Derivadas parciales](../programa/clases/B09/B09-C16-derivadas-parciales/CLASE.md); [B11-C12 · Problemas de frontera](../programa/clases/B11/B11-C12-problemas-de-frontera/CLASE.md).

### ML

- Una ML es una monocapa (por convención `10¹⁵` moléculas cm⁻²).

💡 **Cómo se explica en la clase [B68-C02](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md):**
- Para CO₂ a 15–18 K, Öberg y colaboradores dan `Y(x) = 1,2 × 10⁻³ (1 − e^(−x/2,9)) + 1,1 × 10⁻³ (1 − e^(−x/4,6))`, con `x` en ML: dos términos, uno para el CO₂ que sale tras disociarse y recombinarse y otro para el CO que sale.
- El límite es `2,30 × 10⁻³` y se alcanza el 90 % a `x = 8,63 ML`.
- 🎯 **Por qué importa:** Si un hielo de CO a 15 K es estable térmicamente durante millones de años, la presencia de CO gaseoso en regiones frías exige otro mecanismo. La decisión central: ¿cuántas moléculas expulsa cada fotón y de qué depende ese número?

📘 **Dónde se aprende** (1 clase): [B68-C02 · Fotodesorción de hielos interestelares](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md).

### M/M/1

- Incidente: evento que interrumpe la operación normal. M/M/1: cola con llegadas y servicios exponenciales y un servidor.

💡 **Cómo se explica en la clase [B96-C26](../programa/clases/B96/B96-C26-gestion-de-incidentes-en-la-operacion-de-estaciones/CLASE.md):**
- Las fórmulas de la teoría de colas (M/M/1 y la de Cobham para prioridad no expropiativa) son estándar y las verifica el laboratorio.
- Calcular la utilización y la espera media de una cola M/M/1.
- 🎯 **Por qué importa:** Sin un procedimiento de priorización, un incidente leve puede retrasar a uno grave. La decisión central: ¿cuánto esperan los incidentes de alta y de baja prioridad y cuánto mejora la priorización al grave sin colapsar al leve?

📘 **Dónde se aprende** (1 clase): [B96-C26 · Gestión de incidentes en la operación de estaciones](../programa/clases/B96/B96-C26-gestion-de-incidentes-en-la-operacion-de-estaciones/CLASE.md).

### Mochila

- La mochila es el problema de elegir con una capacidad.
- Observación: actividad de la carga útil con valor, energía y datos. Mochila: problema de selección con capacidad.

💡 **Cómo se explica en la clase [B96-C10](../programa/clases/B96/B96-C10-planificacion-de-cargas-utiles/CLASE.md):**
- Plantear la selección de observaciones como una mochila con dos restricciones.
- 🎯 **Por qué importa:** Una observación que no cabe en la energía o en el almacenamiento no se hace, y una elegida a ojo puede dejar valor sin usar. La decisión central: ¿qué conjunto de observaciones da más valor dentro de la energía y los datos disponibles?

📘 **Dónde se aprende** (2 clases): [B96-C10 · Planificación de cargas útiles](../programa/clases/B96/B96-C10-planificacion-de-cargas-utiles/CLASE.md); [B104-C23 · Ejecución de experimentos a bordo: procedimientos y registro](../programa/clases/B104/B104-C23-ejecucion-de-experimentos-a-bordo-procedimientos-y-registro/CLASE.md).

### Mochila 0/1

- La mochila 0/1 es la selección de observaciones completas o nada.

💡 **Cómo se explica en la clase [B97-C21](../programa/clases/B97/B97-C21-clasificacion-y-priorizacion-autonoma-de-muestras-a-bordo/CLASE.md):**
- Analogía: un geólogo que, en una excursión con una mochila pequeña, elige qué muestras llevarse según cuánto le parece que valen y cuánto pesan.
- 🎯 **Por qué importa:** Con enlaces de unos pocos kilobits por segundo y retardo de minutos, enviar solo lo valioso multiplica el rendimiento científico. Hay que saber cuánto confiar en el clasificador y cuánto pierde una regla simple frente al óptimo.

📘 **Dónde se aprende** (1 clase): [B97-C21 · Clasificación y priorización autónoma de muestras a bordo](../programa/clases/B97/B97-C21-clasificacion-y-priorizacion-autonoma-de-muestras-a-bordo/CLASE.md).

### Mock

- Un mock registra llamadas sin hardware.

💡 **Cómo se explica en la clase [B88-C24](../programa/clases/B88/B88-C24-capa-de-abstraccion-de-hardware-hal-y-controladores/CLASE.md):**
- *Descripción textual:* la aplicación solo conoce la interfaz; detrás puede haber el dispositivo virtual o el mock.
- Con el dispositivo con FIFO: 12 enviados, 8 reintentos, 32 accesos; con el mock: 12 enviados, 0 reintentos, 24 accesos.
- 🎯 **Por qué importa:** Si la aplicación toca registros, no se puede probar sin el hardware y cada cambio de componente la rompe. La decisión central: ¿qué interfaz mínima expone el dispositivo para que la aplicación no dependa de él?

📘 **Dónde se aprende** (1 clase): [B88-C24 · Capa de abstracción de hardware (HAL) y controladores](../programa/clases/B88/B88-C24-capa-de-abstraccion-de-hardware-hal-y-controladores/CLASE.md).

### MOC/SOC

- Segmento terrestre: estaciones, MOC, SOC y redes. MOC/SOC: centros de operaciones de misión y científicas.

🎯 **Por qué importa (clase B96-C01):** Quien opera una nave no puede tratarla como un equipo de laboratorio: cada comando viaja a la velocidad de la luz y cada contacto dura minutos. La decisión central: ¿qué segmento hace qué y cuánto tardan en comunicarse?

📘 **Dónde se aprende** (1 clase): [B96-C01 · Segmento espacial y segmento terrestre](../programa/clases/B96/B96-C01-segmento-espacial-y-segmento-terrestre/CLASE.md).

### MOCUS

- Un conjunto de corte es una combinación que causa el evento superior; es mínimo si ningún subconjunto propio lo causa. MOCUS expande el árbol a conjuntos de corte.

🎯 **Por qué importa (clase B83-C24):** Un fallo combinado como «dos sensores fallan a la vez» no aparece en una lista de modos individuales. La decisión central: ¿qué combinaciones de fallos causan el evento no deseado, cuál es su probabilidad y qué evento básico conviene proteger primero?

📘 **Dónde se aprende** (1 clase): [B83-C24 · Árboles de fallos (FTA) y análisis de causas](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md).

### Modal

- El modal «deberá» marca la obligación (en el ejemplo, «podrá» no lo es).

💡 **Cómo se explica en la clase [B83-C04](../programa/clases/B83/B83-C04-requisitos-verificables/CLASE.md):**
- *Descripción textual:* un enunciado pasa cinco filtros (modal, ambigüedad, atomicidad, valor medible y método de verificación); solo si los supera todos es un requisito verificable.
- Redactar un requisito con modal único, valor medible y método de verificación.
- 🎯 **Por qué importa:** Un requisito vago («resolución adecuada») no puede aprobarse ni suspenderse: bloquea el diseño y siembra disputas. La decisión central: ¿este enunciado se puede comprobar con un método y un criterio de aceptación?

📘 **Dónde se aprende** (1 clase): [B83-C04 · Requisitos verificables](../programa/clases/B83/B83-C04-requisitos-verificables/CLASE.md).

### Modelo

- Un modelo es una representación simplificada del mundo, con reglas y parámetros, que sirve para predecir y que sólo vale dentro de ciertos límites.
- Un modelo es una simplificación que permite pasar de datos a magnitudes que no se miden directamente: «la distancia es `v/H₀`».
- El modelo es la función `F(t) = 1 − δ·clip((D/2 − |t − t₀|)/τ, 0, 1)` con `δ` (profundidad), `t₀` (centro), `D` (duración) y `τ = 1000 s` (ingreso, fijo).
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C01](../programa/clases/B01/B01-C01-naturaleza-del-universo/CLASE.md):**
- Fíjate cómo se encadenan las tres capas: Hα en 662,9 nm (observación) → `z` y `v` (inferencia) → `d` con `H₀` (modelo).
- En el modelo ΛCDM la expansión se frenó al principio por la atracción de la materia, y más tarde se aceleró por la llamada energía oscura; ambos efectos se compensan en parte, y por eso `1/H₀` queda cerca de la edad, pero sin igualarla.
- 🎯 **Por qué importa:** Seguramente has leído que «el universo tiene 13 800 millones de años» o que «el universo observable mide 93 000 millones de años luz». Son frases que se repiten con total seguridad.

📘 **Dónde se aprende** (6 clases): [B01-C01 · Naturaleza del universo](../programa/clases/B01/B01-C01-naturaleza-del-universo/CLASE.md); [B01-C05 · Observación frente a interpretación](../programa/clases/B01/B01-C05-observacion-frente-a-interpretacion/CLASE.md); [B14-C20 · Proyecto reproducible de análisis astronómico](../programa/clases/B14/B14-C20-proyecto-reproducible-de-analisis-astronomico/CLASE.md); [B15-C16 · Ajuste de curvas](../programa/clases/B15/B15-C16-ajuste-de-curvas/CLASE.md); [B22-C03 · Identificabilidad de parámetros](../programa/clases/B22/B22-C03-identificabilidad-de-parametros/CLASE.md); [B43-C26 · Modelo de flexiones y de apuntado de una montura](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md).

### Modelo 1D

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B32-C07](../programa/clases/B32/B32-C07-modelos-de-atmosferas-estelares-1d-y-3d-hidrodinamicos/CLASE.md):**
- Una dispersión del 10 % sesga al alza el flujo un 6 % y la temperatura equivalente un 1,5 %: ese es el tipo de efecto por el que los modelos 3D y 1D difieren.
- TAU["τ"] --> M1["modelo 1D: T, P, ρ, H"]
- ⚠️ **Error frecuente:** Presentar el juguete como un modelo 3D. Se corrige con la sección 10.
- 🎯 **Por qué importa:** Las abundancias derivadas con 1D pueden diferir de las 3D por la no linealidad del flujo con la temperatura. La decisión central: ¿cuánto sesga una fluctuación la temperatura inferida?

📘 **Dónde se aprende** (1 clase): [B32-C07 · Modelos de atmósferas estelares 1D y 3D hidrodinámicos](../programa/clases/B32/B32-C07-modelos-de-atmosferas-estelares-1d-y-3d-hidrodinamicos/CLASE.md).

### Modelo 3D hidrodinámico

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B32-C07](../programa/clases/B32/B32-C07-modelos-de-atmosferas-estelares-1d-y-3d-hidrodinamicos/CLASE.md):**
- python programa/clases/B32/B32-C07-modelos-de-atmosferas-estelares-1d-y-3d-hidrodinamicos/modelos.py
- 🎯 **Por qué importa:** Las abundancias derivadas con 1D pueden diferir de las 3D por la no linealidad del flujo con la temperatura. La decisión central: ¿cuánto sesga una fluctuación la temperatura inferida?

📘 **Dónde se aprende** (1 clase): [B32-C07 · Modelos de atmósferas estelares 1D y 3D hidrodinámicos](../programa/clases/B32/B32-C07-modelos-de-atmosferas-estelares-1d-y-3d-hidrodinamicos/CLASE.md).

### Modelo A

- El modelo A usa `a_t = a₀`.

💡 **Cómo se explica en la clase [B81-C07](../programa/clases/B81/B81-C07-modelos-de-aceleracion-para-bajo-empuje/CLASE.md):**
- *Descripción textual:* los tres modelos alimentan la misma ecuación promediada del semieje;
- Para ir de 1,0 a 1,5 UA con `Δv = 5465,59 m/s` y una aceleración de `2 × 10⁻⁴ m/s²` a 1 UA, el modelo A (aceleración constante) tarda `316,3 d`; el B (empuje constante, masa que baja, `Isp = 3000 s`) `288,7 d` y gasta `169,5 kg`; el C (potencia solar, `a ∝ 1/r²`) `481,0 d`.
- 🎯 **Por qué importa:** El modelo de aceleración cambia el tiempo de vuelo en decenas de por ciento. La decisión central: ¿cuánto se equivoca el tiempo de vuelo si se usa un modelo más simple que el real?

📘 **Dónde se aprende** (1 clase): [B81-C07 · Modelos de aceleración para bajo empuje](../programa/clases/B81/B81-C07-modelos-de-aceleracion-para-bajo-empuje/CLASE.md).

### Modelo anidado

- El modelo anidado contiene al otro como caso particular (grado 1 dentro de grado 2).

💡 **Cómo se explica en la clase [B12-C22](../programa/clases/B12/B12-C22-comparacion-de-modelos-evidencia-bayesiana-y-criterios-de-informacion/CLASE.md):**
- Ejercicio 10 · transferencia. Quieres comparar dos modelos físicos no anidados de la curva de luz de una estrella.
- 🎯 **Por qué importa:** Un modelo más flexible siempre ajusta mejor los datos que uno más sencillo, así que el ajuste solo no sirve para elegir. Hace falta penalizar la complejidad: ¿vale la pena el parámetro extra?

📘 **Dónde se aprende** (1 clase): [B12-C22 · Comparación de modelos: evidencia bayesiana y criterios de información](../programa/clases/B12/B12-C22-comparacion-de-modelos-evidencia-bayesiana-y-criterios-de-informacion/CLASE.md).

### Modelo B

- El modelo B usa `T` constante y `m(t) = m₀ − ṁ t`, de modo que `a_t = T/m` crece.

💡 **Cómo se explica en la clase [B81-C07](../programa/clases/B81/B81-C07-modelos-de-aceleracion-para-bajo-empuje/CLASE.md):**
- *Descripción textual:* los tres modelos alimentan la misma ecuación promediada del semieje;
- Para ir de 1,0 a 1,5 UA con `Δv = 5465,59 m/s` y una aceleración de `2 × 10⁻⁴ m/s²` a 1 UA, el modelo A (aceleración constante) tarda `316,3 d`; el B (empuje constante, masa que baja, `Isp = 3000 s`) `288,7 d` y gasta `169,5 kg`; el C (potencia solar, `a ∝ 1/r²`) `481,0 d`.
- 🎯 **Por qué importa:** El modelo de aceleración cambia el tiempo de vuelo en decenas de por ciento. La decisión central: ¿cuánto se equivoca el tiempo de vuelo si se usa un modelo más simple que el real?

📘 **Dónde se aprende** (1 clase): [B81-C07 · Modelos de aceleración para bajo empuje](../programa/clases/B81/B81-C07-modelos-de-aceleracion-para-bajo-empuje/CLASE.md).

### Modelo basado en distancias

- Un modelo basado en distancias (por ejemplo, k vecinos más cercanos) clasifica un punto según los más próximos en el espacio de características.

💡 **Cómo se explica en la clase [B17-C01](../programa/clases/B17/B17-C01-ingenieria-de-caracteristicas-cientificas/CLASE.md):**
- Explicar por qué la escala de una columna altera a los modelos basados en distancias y cómo la estandarización lo corrige.
- 🎯 **Por qué importa:** Un modelo de aprendizaje automático no sabe física: solo ve números. Si le das la duración de un tránsito en segundos y el periodo en días, la columna con números más grandes domina cualquier cálculo de distancias, y la clasificación depende de una elección de unidades que nada tiene que ver con el cielo.

📘 **Dónde se aprende** (1 clase): [B17-C01 · Ingeniería de características científicas](../programa/clases/B17/B17-C01-ingenieria-de-caracteristicas-cientificas/CLASE.md).

### Modelo C

- El modelo C usa `a_t = a₀ (1 UA/r)²` con masa constante.

💡 **Cómo se explica en la clase [B81-C07](../programa/clases/B81/B81-C07-modelos-de-aceleracion-para-bajo-empuje/CLASE.md):**
- *Descripción textual:* los tres modelos alimentan la misma ecuación promediada del semieje;
- Para ir de 1,0 a 1,5 UA con `Δv = 5465,59 m/s` y una aceleración de `2 × 10⁻⁴ m/s²` a 1 UA, el modelo A (aceleración constante) tarda `316,3 d`; el B (empuje constante, masa que baja, `Isp = 3000 s`) `288,7 d` y gasta `169,5 kg`; el C (potencia solar, `a ∝ 1/r²`) `481,0 d`.
- 🎯 **Por qué importa:** El modelo de aceleración cambia el tiempo de vuelo en decenas de por ciento. La decisión central: ¿cuánto se equivoca el tiempo de vuelo si se usa un modelo más simple que el real?

📘 **Dónde se aprende** (1 clase): [B81-C07 · Modelos de aceleración para bajo empuje](../programa/clases/B81/B81-C07-modelos-de-aceleracion-para-bajo-empuje/CLASE.md).

### Modelo científico

- Un modelo científico es una representación simplificada que permite predecir y que se contrasta con datos.

💡 **Cómo se explica en la clase [B01-C17](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md):**
- Límite: un mapa del metro no se contrasta con mediciones, un modelo científico sí; y un mapa puede ser «correcto» sin ser escala, mientras que un modelo cuantitativo se evalúa por sus residuos.
- python programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/contrastar_modelo_y_dato.py
- 🎯 **Por qué importa:** Al final de C13, la tercera ley de Kepler daba `T²/a³ = 1` para siete planetas con error menor al 1,5 %, y 0,975 para Neptuno. ¿Falla el modelo con Neptuno?

📘 **Dónde se aprende** (1 clase): [B01-C17 · Construcción de modelos científicos](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md).

### Modelo circular

- El modelo circular supone órbitas circulares coplanares de 1 UA y 1,524 UA; la distancia es `√(1 + 1,524² − 2·1,524·cos θ)` UA con `θ = 2π t/779,9 d`.

💡 **Cómo se explica en la clase [B105-C15](../programa/clases/B105/B105-C15-telemedicina-espacial/CLASE.md):**
- El script [enlace.py](enlace.py) calcula los retardos de luz a la Luna y a Marte (modelo circular), la fracción del ciclo sobre un umbral y el presupuesto de una consulta con turnos y con almacenar y reenviar (comprueba el retardo lunar de 1,282 s, los extremos del ciclo de Marte y que un solo turno es más corto que seis).
- Ciclo sinodico (modelo circular): distancia entre 0.524 y 2.524 UA; retardo de ida 4.36 a 20.99 min; media 14.08 min
- ⚠️ **Error frecuente:** Tomar la distancia del modelo como la real. Es un modelo circular.
- 🎯 **Por qué importa:** Una conversación en tiempo real es posible a la Luna (2,6 s de ida y vuelta) y deja de serlo a Marte (hasta 42 min). La decisión central: ¿cuánto dura una consulta según el destino y el diseño del intercambio (varios turnos o un paquete completo)?

📘 **Dónde se aprende** (1 clase): [B105-C15 · Telemedicina espacial](../programa/clases/B105/B105-C15-telemedicina-espacial/CLASE.md).

### Modelo de arrastre

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B30-C13):** Saber cuándo llegará una CME determina el margen de alerta. La decisión central: ¿cuánto tarda en llegar y cuánto depende ese tiempo del arrastre?

📘 **Dónde se aprende** (1 clase): [B30-C13 · Eyecciones de masa coronal](../programa/clases/B30/B30-C13-eyecciones-de-masa-coronal/CLASE.md).

### Modelo de Bingham

- El modelo de Bingham describe un material con resistencia a la fluencia `τ_y`.

🎯 **Por qué importa (clase B70-C07):** La misma lava fluye distinto según la pendiente, el espesor y la reología; los piroclastos llegan más lejos si no hay aire. La decisión central: ¿cuánto fluye una colada y hasta dónde llegan los clastos en cada mundo?

📘 **Dónde se aprende** (1 clase): [B70-C07 · Flujos de lava y depósitos piroclásticos](../programa/clases/B70/B70-C07-flujos-de-lava-y-depositos-piroclasticos/CLASE.md).

### Modelo de caja

- Un modelo de caja supone una caída plana.

💡 **Cómo se explica en la clase [B131-C06](../programa/clases/B131/B131-C06-aprendizaje-basado-en-problemas-con-datos-astronomicos/CLASE.md):**
- Límite: el modelo de caja ignora el oscurecimiento al limbo y la forma real del tránsito.
- Curva SINTETICA (modelo de caja + ruido gaussiano, semilla 131); radios nominales IAU 2015 B3 CONSULTADOS; parametros ILUSTRATIVOS.
- 🎯 **Por qué importa:** Un problema con datos reales o realistas enseña más que un ejercicio con respuesta única, pero exige diseñar qué se espera. La decisión central: ¿qué sabe el estudiante al empezar, qué datos recibe y cómo comprobará su respuesta?

📘 **Dónde se aprende** (1 clase): [B131-C06 · Aprendizaje basado en problemas con datos astronómicos](../programa/clases/B131/B131-C06-aprendizaje-basado-en-problemas-con-datos-astronomicos/CLASE.md).

### Modelo de calificación (QM)

- Modelo de ingeniería (EM): modelo funcionalmente representativo para probar el diseño. Modelo de calificación (QM): unidad idéntica a la de vuelo para calificar.

💡 **Cómo se explica en la clase [B90-C24](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md):**
- Distinguir prototipo, modelo de ingeniería, modelo de calificación, protovuelo y unidad de vuelo.
- 🎯 **Por qué importa:** Un modelo de ingeniería cuesta dinero y calendario; un defecto que llega a órbita cuesta la misión. La decisión central: ¿vale la pena construir un modelo previo, o conviene el protovuelo o solo la unidad de vuelo, dado el valor de lo que se arriesga?

📘 **Dónde se aprende** (1 clase): [B90-C24 · Prototipado y modelos de ingeniería de subconjuntos](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md).

### Modelo de cielo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B51-C02](../programa/clases/B51/B51-C02-cantidades-de-cierre-fase-y-amplitud-de-cierre/CLASE.md):**
- Con 6 estaciones, ganancias con fase de 90,7° rms (sintéticas) y un cielo de dos fuentes, la diferencia entre los cierres de los datos corrompidos y los del modelo es de 2,22 × 10⁻¹⁶ rad en fase y 6,66 × 10⁻¹⁶ en amplitud.
- 🎯 **Por qué importa:** Cuando las ganancias no se pueden calibrar (VLBI con atmósfera rápida, autocalibración), los cierres son los observables robustos. La decisión central: ¿qué información sobrevive a los errores por antena y cuánta se pierde?

📘 **Dónde se aprende** (3 clases): [B51-C02 · Cantidades de cierre: fase y amplitud de cierre](../programa/clases/B51/B51-C02-cantidades-de-cierre-fase-y-amplitud-de-cierre/CLASE.md); [B51-C03 · Ganancias complejas por antena y soluciones de calibración](../programa/clases/B51/B51-C03-ganancias-complejas-por-antena-y-soluciones-de-calibracion/CLASE.md); [B51-C06 · Autocalibración iterativa con modelo de cielo](../programa/clases/B51/B51-C06-autocalibracion-iterativa-con-modelo-de-cielo/CLASE.md).

### Modelo de cuerpo humano

- ESD: descarga electrostática. Modelo de cuerpo humano: circuito RC que representa la descarga de una persona.

🎯 **Por qué importa (clase B90-C03):** Un componente electrónico puede quedar con una falla latente tras una descarga que nadie sintió: una persona percibe una chispa solo por encima de unos miles de voltios (orden de magnitud no consultado), por encima de lo que puede dañar a un componente sensible.

📘 **Dónde se aprende** (1 clase): [B90-C03 · Protección frente a ESD](../programa/clases/B90/B90-C03-proteccion-frente-a-esd/CLASE.md).

### Modelo de densidad

- El modelo de densidad da la altura de cada frecuencia.

💡 **Cómo se explica en la clase [B30-C21](../programa/clases/B30/B30-C21-radioemision-solar-estallidos-de-radio-y-su-observacion/CLASE.md):**
- Con una deriva de ≈5 a 20 MHz/s en 100–230 MHz y una densidad dada, la velocidad sale del ajuste con un error de décimas de por ciento, pero solo porque el modelo de densidad es conocido; con una densidad errónea la velocidad saldría mal en la misma proporción.
- Ejercicio 11 · transferencia. Transferencia. ¿Por qué el ajuste depende del modelo de densidad?
- ⚠️ **Error frecuente:** Dar la velocidad sin declarar el modelo de densidad. Se corrige con 8.4.
- 🎯 **Por qué importa:** Una frecuencia es una altura, y la deriva en frecuencia da la velocidad del haz. La decisión central: ¿cómo se convierte un espectro dinámico en la velocidad de los electrones?

📘 **Dónde se aprende** (1 clase): [B30-C21 · Radioemisión solar: estallidos de radio y su observación](../programa/clases/B30/B30-C21-radioemision-solar-estallidos-de-radio-y-su-observacion/CLASE.md).

### Modelo de dos escalas

- Un modelo de dos escalas usa una para tamaños y otra para distancias.

💡 **Cómo se explica en la clase [B131-C05](../programa/clases/B131/B131-C05-demostraciones-visuales-y-modelos-para-el-aula/CLASE.md):**
- Límite: un modelo de fases con linterna y esfera exige una sala oscura y una fuente puntual, y aun así no muestra la escala.
- Calcular el factor de escala a partir del diámetro del Sol del modelo.
- 🎯 **Por qué importa:** Un modelo es útil por lo que conserva y engañoso por lo que deforma. La decisión central: ¿qué propiedad del cielo conserva tu demostración y cuál sacrifica?

📘 **Dónde se aprende** (1 clase): [B131-C05 · Demostraciones visuales y modelos para el aula](../programa/clases/B131/B131-C05-demostraciones-visuales-y-modelos-para-el-aula/CLASE.md).

### Modelo de dos esferas

- El modelo de dos esferas es una simplificación didáctica de un cuerpo extendido.

🎯 **Por qué importa (clase B52-C12):** El límite de Roche separa el régimen de anillos del de satélites. La decisión central: ¿a qué distancia del planeta se separan dos partículas en contacto y cómo depende de la densidad?

📘 **Dónde se aprende** (1 clase): [B52-C12 · Anillos planetarios](../programa/clases/B52/B52-C12-anillos-planetarios/CLASE.md).

### Modelo de electrones libres

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C05](../programa/clases/B47/B47-C05-instrumentos-de-rayos-x/CLASE.md):**
- Se ignoran los bordes de absorción, la rugosidad, el vignetting y la dispersión; el modelo de electrones libres sobrestima `δ` a baja energía.
- Reconocer los límites del modelo de electrones libres.
- 🎯 **Por qué importa:** La reflexión rasante limita la energía y el área útil. La decisión central: ¿cuántas conchas y qué ángulos dan el área efectiva que se necesita a cada energía?

📘 **Dónde se aprende** (1 clase): [B47-C05 · Instrumentos de rayos X](../programa/clases/B47/B47-C05-instrumentos-de-rayos-x/CLASE.md).

### Modelo de Haser

- El modelo de Haser supone expansión esférica a velocidad constante `v` con destrucción de primer orden.

🎯 **Por qué importa (clase B55-C11):** Un telescopio no ve la densidad en cada punto de la coma sino la columna a lo largo de la línea de visión. Para pasar de lo medido a la producción de moléculas por el núcleo hay que modelar la expansión y la destrucción.

📘 **Dónde se aprende** (1 clase): [B55-C11 · Química en cometas](../programa/clases/B55/B55-C11-quimica-en-cometas/CLASE.md).

### Modelo de ingeniería (EM)

- Prototipo: versión temprana para explorar el diseño. Modelo de ingeniería (EM): modelo funcionalmente representativo para probar el diseño.

💡 **Cómo se explica en la clase [B90-C24](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md):**
- D["Defecto de diseno<br/>q = 0.30"] --> E["Modelo de ingenieria<br/>detecta 0.80"]
- *Descripción textual:* un defecto de diseño pasa por el modelo de ingeniería, que detecta la mayoría y lo corrige a bajo costo; los que escapan pasan a la unidad de vuelo, que detecta parte a mayor costo de corrección; los que escapan de ambas llegan a órbita y cuestan la pérdida.
- 🎯 **Por qué importa:** Un modelo de ingeniería cuesta dinero y calendario; un defecto que llega a órbita cuesta la misión. La decisión central: ¿vale la pena construir un modelo previo, o conviene el protovuelo o solo la unidad de vuelo, dado el valor de lo que se arriesga?

📘 **Dónde se aprende** (1 clase): [B90-C24 · Prototipado y modelos de ingeniería de subconjuntos](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md).

### Modelo de intercepto aleatorio

- El modelo de intercepto aleatorio escribe `y_ij = β₀ + β₁ t_j + u_i + e_ij`: `β₀, β₁` son efectos fijos (comunes), `u_i` es el efecto aleatorio de la unidad `i` (su diferencia estable) y `e_ij` el error de medida.

💡 **Cómo se explica en la clase [B12-C25](../programa/clases/B12/B12-C25-modelos-longitudinales-y-de-efectos-mixtos-para-muestras-pequenas/CLASE.md):**
- Paso 1 · Modelo. Intercepto aleatorio, balanceado.
- Escribir el modelo de intercepto aleatorio y nombrar sus componentes de varianza.
- 🎯 **Por qué importa:** Seis personas medidas cuatro veces dan 24 números, pero no 24 piezas de información independientes: las de una misma persona se parecen. Ignorar eso produce intervalos demasiado angostos para el nivel medio y, paradójicamente, demasiado anchos para los cambios dentro de cada persona.

📘 **Dónde se aprende** (1 clase): [B12-C25 · Modelos longitudinales y de efectos mixtos para muestras pequeñas](../programa/clases/B12/B12-C25-modelos-longitudinales-y-de-efectos-mixtos-para-muestras-pequenas/CLASE.md).

### Modelo de inversión

- El modelo generador produce los datos; el modelo de inversión es el que usa el método.

💡 **Cómo se explica en la clase [B22-C05](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md):**
- Si `A_gen = A_inv` (en el laboratorio, `b = A_c x_ver` con la misma matriz gruesa que luego se invierte), la inversión no se ve afectada por ningún error de modelo; solo por ruido y regularización.
- Ambos producen datos con ruido, que entran a la misma inversión con modelo grueso, y de ahí se mide el error frente a la verdad.
- 🎯 **Por qué importa:** Con datos reales no conoces la verdad, así que no puedes medir el error de tu inversión. Con datos sintéticos sí: tú fijas la verdad, generas los datos y miras si el método la recupera.

📘 **Dónde se aprende** (1 clase): [B22-C05 · Pruebas de inversión con datos sintéticos](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md).

### Modelo de Langevin

- El modelo de Langevin describe una colisión ion–neutro dominada por la atracción de carga–dipolo inducido.

🎯 **Por qué importa (clase B60-C01):** Un modelo astroquímico necesita miles de constantes de velocidad. Antes de usar las de una base de datos conviene saber qué hay dentro de una: una colisión, una sección eficaz y un promedio térmico.

📘 **Dónde se aprende** (1 clase): [B60-C01 · Colisiones moleculares y secciones eficaces en gas interestelar](../programa/clases/B60/B60-C01-colisiones-moleculares-y-secciones-eficaces-en-gas-interestelar/CLASE.md).

### Modelo de medida

- El mensurando es la magnitud que se quiere determinar; el modelo de medida expresa el mensurando en función de las magnitudes de entrada (S1, 4.1).
- El modelo de medida expresa la salida como función de las entradas: `Y = f(X₁, …, X_N)` (S1, 4.1).
- El modelo de medida expresa el mensurando en función de las magnitudes de entrada.

💡 **Cómo se explica en la clase [B12-C16](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md):**
- Escribir el modelo de medida `y = f(x₁, …, x_N)` e identificar sus entradas.
- 🎯 **Por qué importa:** Casi todo resultado en ciencias espaciales es una función de medidas: una velocidad a partir de un radio, una distancia a partir de una paralaje, una masa a partir de un período. Dar el valor sin su incertidumbre no permite comparar con otros resultados ni decidir si cumple un requisito.

📘 **Dónde se aprende** (3 clases): [B12-C16 · Propagación de incertidumbre](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md); [B12-C20 · Informe de incertidumbre de una misión](../programa/clases/B12/B12-C20-informe-de-incertidumbre-de-una-mision/CLASE.md); [B13-C13 · Presupuestos de incertidumbre](../programa/clases/B13/B13-C13-presupuestos-de-incertidumbre/CLASE.md).

### Modelo de Milne

- El modelo de Milne es un universo vacío (`Ω_m = Ω_Λ = 0`).

💡 **Cómo se explica en la clase [B26-C19](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md):**
- Ejercicio 12 · integrador. Elabora tu *tabla de distancias de luminosidad*: tres modelos y cuatro corrimientos, verificación con EdS y Milne, diferencia en magnitudes y comparación con el 10–15 % de Riess et al.
- El script [luminosidad.py](luminosidad.py) calcula `D_L` con curvatura general y comprueba las soluciones cerradas de EdS y Milne a `10⁻⁹`; tabula tres modelos y la sensibilidad a `Ω_m`.
- 🎯 **Por qué importa:** La aceleración cósmica se descubrió porque las supernovas Ia lejanas aparecían más débiles de lo esperado. Para reproducir ese razonamiento hay que saber calcular la distancia de luminosidad y ver cuánto cambia con el contenido del universo.

📘 **Dónde se aprende** (1 clase): [B26-C19 · Energía oscura y parámetros](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md).

### Modelo de Milne–Eddington

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B32-C08):** Una inversión sin barras de error no sirve. La decisión central: ¿qué parámetros se recuperan y con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B32-C08 · Síntesis espectral e inversión de perfiles](../programa/clases/B32/B32-C08-sintesis-espectral-e-inversion-de-perfiles/CLASE.md).

### Modelo de observación

- El modelo de observación `h` asigna al estado `x` la medida que se esperaría sin ruido.

💡 **Cómo se explica en la clase [B74-C01](../programa/clases/B74/B74-C01-modelos-de-observacion/CLASE.md):**
- La evidencia es la ficha del modelo de observación de una estación del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha del modelo de observación de una estación*: `h`, jacobiano analítico y numérico, residuo normalizado, error transversal y covarianza de medida, rotulando lo sintético.
- 🎯 **Por qué importa:** Todo método de B74 (mínimos cuadrados, filtros, validación) deriva del par `h` y `H = ∂h/∂x`. La decisión central: ¿qué función y qué derivadas describen la medida, y cómo sé que están bien escritas antes de dárselas a un estimador?

📘 **Dónde se aprende** (1 clase): [B74-C01 · Modelos de observación](../programa/clases/B74/B74-C01-modelos-de-observacion/CLASE.md).

### Modelo de repulsión de pares de valencia

- El modelo de repulsión de pares de valencia (VSEPR, por sus siglas en inglés) dice que los dominios se colocan lo más lejos posible entre sí.

🎯 **Por qué importa (clase B06-C05):** El dióxido de carbono es el 95,1 % de la atmósfera de Marte en volumen (S2), y los hielos de las nubes densas del medio interestelar contienen, según un estudio con el telescopio James Webb, agua y CO₂ entre otras especies (S3, que se leyó sólo en resumen).

📘 **Dónde se aprende** (1 clase): [B06-C05 · Moléculas y geometría molecular](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md).

### Modelo de sistema

- Un modelo de sistema reúne parámetros, relaciones y restricciones en un solo lugar.

💡 **Cómo se explica en la clase [B83-C12](../programa/clases/B83/B83-C12-model-based-systems-engineering/CLASE.md):**
- La evidencia es la modelo de sistema ejecutable con trazas de cambio del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *modelo de sistema con trazas de cambio*: parámetros, ecuaciones, orden, tres casos de GSD y parámetros afectados, con lista de qué es consultado y sintético.
- 🎯 **Por qué importa:** Cuando los presupuestos viven en hojas distintas, un cambio de requisito se propaga a mano y algo se olvida. La decisión central: ¿qué parámetros cambian si cambia este requisito, y siguen cumpliéndose todos los presupuestos?

📘 **Dónde se aprende** (1 clase): [B83-C12 · Model-Based Systems Engineering](../programa/clases/B83/B83-C12-model-based-systems-engineering/CLASE.md).

### Modelo de tres fases

- El modelo de tres fases trata gas, superficie y manto como reservorios distintos; el de dos fases, solo gas y superficie.

💡 **Cómo se explica en la clase [B60-C04](../programa/clases/B60/B60-C04-balance-quimico-gas-grano-modelos-de-tres-fases/CLASE.md):**
- Un modelo de dos fases mantiene 79 monocapas como «superficie activa»; el de tres fases, una.
- Según el resumen consultado de Ruaud, Wakelam y Hersant (2016), su modelo Nautilus de tres fases trata superficie y manto como químicamente activos con reacción, difusión y evaporación, y reporta efectos sobre las abundancias de superficie y gas frente al de dos fases.
- 🎯 **Por qué importa:** Un modelo de dos fases trata todo el hielo como si estuviera expuesto en la superficie; en la realidad la mayor parte queda enterrada bajo capas posteriores. La decisión central: ¿qué cambia en la predicción de cuánto hielo se libera al calentar si se distingue la superficie del manto?

📘 **Dónde se aprende** (1 clase): [B60-C04 · Balance químico gas-grano: modelos de tres fases](../programa/clases/B60/B60-C04-balance-quimico-gas-grano-modelos-de-tres-fases/CLASE.md).

### Modelo de un compartimento

- El modelo de un compartimento trata al cuerpo como un volumen único.

🎯 **Por qué importa (clase B105-C13):** Con un fármaco real, el efecto depende de su concentración en el tiempo. Un cambio de volumen modifica la concentración inicial; uno de aclaramiento, la exposición total.

📘 **Dónde se aprende** (1 clase): [B105-C13 · Farmacología y microgravedad](../programa/clases/B105/B105-C13-farmacologia-y-microgravedad/CLASE.md).

### Modelo del péndulo

- El modelo del péndulo `φ' = q`, `q' = −ε sin φ` tiene energía `E = q²/2 − ε cos φ`; la separatriz es `E = ε`.

🎯 **Por qué importa (clase B73-C12):** Muchas resonancias observadas (satélites, planetas migrantes, asteroides) no son primordiales: los cuerpos entraron en ellas. Saber cuándo una captura es segura y cuándo es improbable, y cuándo un cuerpo atrapado debe escapar, evita explicaciones erróneas.

📘 **Dónde se aprende** (1 clase): [B73-C12 · Captura y escape resonante](../programa/clases/B73/B73-C12-captura-y-escape-resonante/CLASE.md).

### Modelo del sensor

- El modelo del sensor es `m = s ⊙ B + o + n` (producto por eje).

💡 **Cómo se explica en la clase [B87-C08](../programa/clases/B87/B87-C08-calibracion-de-sensores/CLASE.md):**
- No: son datos sintéticos con el modelo exacto con el que se generaron; un sensor real tiene desalineación, hierro blando y variación térmica no modelados.
- ⚠️ **Error frecuente:** Atribuir al sensor el error del modelo de campo. Declara qué referencia usas (8.4)
- 🎯 **Por qué importa:** Un magnetómetro sin calibrar con `3000 nT` de sesgo da errores de dirección de varios grados (C05), mayores que los del ruido. La decisión central: ¿qué error sistemático se puede estimar a bordo sin otro sensor, con qué maniobra y cuánto mejora la medida?

📘 **Dónde se aprende** (1 clase): [B87-C08 · Calibración de sensores](../programa/clases/B87/B87-C08-calibracion-de-sensores/CLASE.md).

### Modelo empírico operativo

- Un modelo empírico operativo ajusta parámetros a datos reales de satélites; este no lo es.

💡 **Cómo se explica en la clase [B72-C07](../programa/clases/B72/B72-C07-modelos-de-densidad-atmosferica/CLASE.md):**
- Los modelos operativos (por ejemplo, los empíricos tipo NRLMSISE) ajustan decenas de parámetros a mediciones; aquí no se usó ninguno y de la *U.S.
- No es operativo: sus parámetros son ilustrativos; hay que usar un modelo empírico y la actividad solar.
- 🎯 **Por qué importa:** El arrastre es tan incierto como la densidad que se le da. La decisión central: ¿cuánto puede variar la densidad a una altitud dada si cambia la temperatura de la termosfera, y qué incertidumbre hereda por eso un cálculo de decaimiento?

📘 **Dónde se aprende** (1 clase): [B72-C07 · Modelos de densidad atmosférica](../programa/clases/B72/B72-C07-modelos-de-densidad-atmosferica/CLASE.md).

### Modelo equivocado

- Un modelo equivocado es uno distinto del que generó los datos.

💡 **Cómo se explica en la clase [B14-C20](../programa/clases/B14/B14-C20-proyecto-reproducible-de-analisis-astronomico/CLASE.md):**
- Una prueba que no fallaría con un modelo equivocado no prueba nada: por eso se incluye este control negativo.
- Modelo equivocado<br/>debe ajustar peor"]
- 🎯 **Por qué importa:** Un análisis reproducible no es un conjunto de herramientas: es una cadena de comprobaciones donde cada eslabón puede fallar a la vista. La pregunta motivadora es: ¿cómo demuestro, con evidencia revisable, que mi resultado se obtuvo de estos datos, con este modelo y este software, y que otra persona lo repetirá?

📘 **Dónde se aprende** (1 clase): [B14-C20 · Proyecto reproducible de análisis astronómico](../programa/clases/B14/B14-C20-proyecto-reproducible-de-analisis-astronomico/CLASE.md).

### Modelo estándar de Eddington

- El modelo estándar de Eddington es el politropo `n = 3`.

💡 **Cómo se explica en la clase [B24-C20](../programa/clases/B24/B24-C20-modelo-simplificado-de-estructura-estelar/CLASE.md):**
- El modelo estándar de Eddington es un politropo `n = 3`.
- 🎯 **Por qué importa:** Un modelo de estructura real resuelve cuatro ecuaciones acopladas con física detallada; un politropo sustituye esa física por una sola relación `P ∝ ρ^{1+1/n}` y permite resolver todo con una ecuación. Es el mejor modo de ver qué se obtiene con poco y qué falta.

📘 **Dónde se aprende** (1 clase): [B24-C20 · Modelo simplificado de estructura estelar](../programa/clases/B24/B24-C20-modelo-simplificado-de-estructura-estelar/CLASE.md).

### Modelo estenopeico

- El modelo estenopeico proyecta `(x, y) = f (bx/bz, by/bz)`.
- El modelo estenopeico proyecta `(x, y, z)` a `u = fx·x/z + cx`, `v = fy·y/z + cy`.

💡 **Cómo se explica en la clase [B87-C07](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md):**
- Proyectar direcciones del cuerpo sobre un detector con un modelo estenopeico (*pinhole*) y su IFOV.
- 🎯 **Por qué importa:** Para apuntar un telescopio o una antena con precisión de segundos de arco, un sensor solar o un magnetómetro no bastan. La decisión central: ¿cuántas estrellas hacen falta y por qué el giro alrededor del eje óptico (balanceo) es mucho peor que el apuntamiento?

📘 **Dónde se aprende** (2 clases): [B87-C07 · Rastreadores estelares](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md); [B103-C01 · Calibración intrínseca de cámaras](../programa/clases/B103/B103-C01-calibracion-intrinseca-de-camaras/CLASE.md).

### Modelo extendido

- Un modelo extendido añade parámetros a ΛCDM.

💡 **Cómo se explica en la clase [B26-C23](../programa/clases/B26/B26-C23-tensiones-observacionales-constante-de-hubble-y-s8/CLASE.md):**
- (S3) señalan que parte de la reducción de la tensión en modelos extendidos viene de incertidumbres mayores.
- 🎯 **Por qué importa:** Decir «hay una tensión» solo tiene sentido con un número: ¿cuántas sigmas?, ¿qué probabilidad de ocurrir por azar?, ¿qué se asume? Sin ese rigor, una discrepancia se exagera o se descarta.

📘 **Dónde se aprende** (1 clase): [B26-C23 · Tensiones observacionales: constante de Hubble y S8](../programa/clases/B26/B26-C23-tensiones-observacionales-constante-de-hubble-y-s8/CLASE.md).

### Modelo físico

- El modelo físico (Parker) resuelve ecuaciones.

🎯 **Por qué importa (clase B33-C10):** Un pronóstico necesita una condición de frontera coronal. La decisión central: ¿cómo cambia la velocidad con la expansión y la distancia al borde?

📘 **Dónde se aprende** (1 clase): [B33-C10 · Modelos de viento solar para pronóstico (Parker y WSA)](../programa/clases/B33/B33-C10-modelos-de-viento-solar-para-pronostico-parker-y-wsa/CLASE.md).

### Modelo generador

- El modelo generador produce los datos; el modelo de inversión es el que usa el método.

💡 **Cómo se explica en la clase [B22-C05](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md):**
- Paso 1 · declaración. Verdad: perfil con dos escalones; datos: 30 puntos; modelo del instrumento: gaussiana `w = 0,05`; generador honesto: 1000 celdas; inversor: 30 celdas; método: Tikhonov, `λ` por discrepancia; semilla 5.
- Diseñar una prueba sintética con verdad, modelo generador, ruido y métrica declarados.
- 🎯 **Por qué importa:** Con datos reales no conoces la verdad, así que no puedes medir el error de tu inversión. Con datos sintéticos sí: tú fijas la verdad, generas los datos y miras si el método la recupera.

📘 **Dónde se aprende** (1 clase): [B22-C05 · Pruebas de inversión con datos sintéticos](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md).

### Modelo generativo

- Hogg, Bovy y Lang señalan que los mínimos cuadrados ponderados solo son apropiados cuando un eje carece de incertidumbre y el otro tiene errores gaussianos de varianza conocida, y proponen partir de un modelo generativo de los datos (S1).

🎯 **Por qué importa (clase B12-C10):** Casi todo en ciencias espaciales es un ajuste: la deriva de un oscilador, la curva de luz de un tránsito, la degradación de una celda solar, la relación período–luminosidad. Un ajuste sin incertidumbre de parámetros ni diagnóstico de residuos es sólo una línea dibujada.

📘 **Dónde se aprende** (1 clase): [B12-C10 · Regresión lineal y no lineal](../programa/clases/B12/B12-C10-regresion-lineal-y-no-lineal/CLASE.md).

### Modelo incompleto

- El modelo incompleto omite componentes reales.

💡 **Cómo se explica en la clase [B15-C19](../programa/clases/B15/B15-C19-reconstruccion-por-datos-incompletos/CLASE.md):**
- La diferencia con 0 en los datos mostró que el modelo era incompleto aunque el hueco no se vea: los residuos en los puntos medidos son la mejor alarma.
- Detectar un modelo incompleto con los residuos en los puntos con datos.
- 🎯 **Por qué importa:** Si falta el 8 % de una serie, ¿se puede rellenar sin contaminar el análisis? Depende de lo que se sepa de la señal: si es suave y se conoce su forma, el relleno es casi exacto; si es un evento breve que cayó en el hueco, no hay método que lo recupere.

📘 **Dónde se aprende** (1 clase): [B15-C19 · Reconstrucción por datos incompletos](../programa/clases/B15/B15-C19-reconstruccion-por-datos-incompletos/CLASE.md).

### Modelo isotermo

- El modelo isotermo supone temperatura constante del gas; el adiabático, ausencia de intercambio de calor.

💡 **Cómo se explica en la clase [B114-C05](../programa/clases/B114/B114-C05-despresurizacion-escenarios-tiempos-y-respuesta/CLASE.md):**
- El modelo adiabático da `1666,5 s`, un `77 %` del isotermo: al enfriarse el gas restante, la presión cae antes.
- Comparar el modelo isotermo con el adiabático.
- ⚠️ **Error frecuente:** Tomar el modelo isotermo como único. Se corrige con 8.3.
- 🎯 **Por qué importa:** Entre una grieta de `1 mm` y una brecha de `100 mm` el tiempo disponible pasa de días a segundos. La decisión central: ¿cuánto tiempo hay hasta un umbral de presión y alcanza para responder?

📘 **Dónde se aprende** (1 clase): [B114-C05 · Despresurización: escenarios, tiempos y respuesta](../programa/clases/B114/B114-C05-despresurizacion-escenarios-tiempos-y-respuesta/CLASE.md).

### Modelo jerárquico

- Un modelo jerárquico describe los datos en niveles.
- Un modelo jerárquico tiene niveles: datos `y_j ~ N(θ_j, σ_j²)`, parámetros de grupo `θ_j ~ N(μ, τ²)` y hiperparámetros `μ` (media del conjunto) y `τ` (heterogeneidad entre grupos), con un hiperprior sobre ellos.

💡 **Cómo se explica en la clase [B12-C21](../programa/clases/B12/B12-C21-modelos-jerarquicos-bayesianos/CLASE.md):**
- Escribir un modelo jerárquico normal–normal con sus niveles y sus hiperparámetros.
- La evidencia es el informe del modelo jerárquico del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Ocho sensores del mismo tipo miden un mismo desfase con errores distintos. Tratarlos como idénticos (agrupación completa) ignora diferencias reales entre ellos; tratarlos como independientes (sin agrupación) desperdicia lo que cada uno enseña de los demás.

📘 **Dónde se aprende** (2 clases): [B12-C21 · Modelos jerárquicos bayesianos](../programa/clases/B12/B12-C21-modelos-jerarquicos-bayesianos/CLASE.md); [B19-C02 · Modelos jerárquicos](../programa/clases/B19/B19-C02-modelos-jerarquicos/CLASE.md).

### Modelo lineal en los parámetros

- Un modelo lineal en los parámetros escribe `y = Xβ + ε`, con `X` la matriz de diseño, `β` los parámetros y `ε` el error; no exige que sea lineal en `t` (un polinomio sigue siéndolo).

💡 **Cómo se explica en la clase [B12-C10](../programa/clases/B12/B12-C10-regresion-lineal-y-no-lineal/CLASE.md):**
- Ajustar un modelo no lineal en parámetros con un método iterativo y compararlo con la linealización.
- 🎯 **Por qué importa:** Casi todo en ciencias espaciales es un ajuste: la deriva de un oscilador, la curva de luz de un tránsito, la degradación de una celda solar, la relación período–luminosidad. Un ajuste sin incertidumbre de parámetros ni diagnóstico de residuos es sólo una línea dibujada.

📘 **Dónde se aprende** (1 clase): [B12-C10 · Regresión lineal y no lineal](../programa/clases/B12/B12-C10-regresion-lineal-y-no-lineal/CLASE.md).

### Modelo lineal sin umbral

- El modelo lineal sin umbral (LNT) supone que el riesgo de exceso crece proporcional a la dosis, sin umbral, también a dosis bajas.

💡 **Cómo se explica en la clase [B112-C04](../programa/clases/B112/B112-C04-efectos-cronicos-y-carcinogenesis-por-radiacion/CLASE.md):**
- Explicar el modelo lineal sin umbral y el papel del DDREF.
- Ejercicio 10 · transferencia. Si el riesgo verdadero tuviera un umbral a 100 mSv, ¿qué haría el modelo lineal sin umbral por debajo de 100 mSv?
- 🎯 **Por qué importa:** Ninguna clase cubre riesgo de cáncer y efectos tardíos. Los límites de carrera de una misión se expresan como riesgo, no como umbral, y sin entender cómo se estima y cuán incierta es esa estimación, un límite en mSv parece más preciso de lo que es.

📘 **Dónde se aprende** (1 clase): [B112-C04 · Efectos crónicos y carcinogénesis por radiación](../programa/clases/B112/B112-C04-efectos-cronicos-y-carcinogenesis-por-radiacion/CLASE.md).

### Modelo radial

- El modelo radial es `r_d = r(1 + k₁r² + k₂r⁴)`.

💡 **Cómo se explica en la clase [B50-C08](../programa/clases/B50/B50-C08-distorsion-geometrica-y-su-calibracion/CLASE.md):**
- *Descripción textual:* se compara la proyección ideal con la real, se ajusta un polinomio radial a una rejilla y se invierte el modelo.
- Ejercicio 11 · transferencia. Transferencia. ¿Qué falta en un modelo radial?
- 🎯 **Por qué importa:** En astrometría y en mosaicos una distorsión de 0,1 % mueve las estrellas decenas de píxeles. La decisión central: ¿qué modelo describe la distorsión y con qué precisión se puede calibrar?

📘 **Dónde se aprende** (1 clase): [B50-C08 · Distorsión geométrica y su calibración](../programa/clases/B50/B50-C08-distorsion-geometrica-y-su-calibracion/CLASE.md).

### Modelo reproducible

- Un modelo reproducible es un archivo de texto con todos los datos necesarios.

💡 **Cómo se explica en la clase [B50-C06](../programa/clases/B50/B50-C06-software-de-diseno-optico-modelos-reproducibles-y-verificacion/CLASE.md):**
- La evidencia es la ficha de un modelo reproducible del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha de un modelo reproducible*: JSON, huella, dos vías y regresión.
- 🎯 **Por qué importa:** Los programas de diseño óptico son cajas con muchas opciones: lo que hace reproducible un diseño es el archivo, sus unidades, su versión y sus pruebas. La decisión central: ¿cómo se demuestra que un modelo sigue siendo el mismo y sigue dando lo mismo?

📘 **Dónde se aprende** (1 clase): [B50-C06 · Software de diseño óptico: modelos reproducibles y verificación](../programa/clases/B50/B50-C06-software-de-diseno-optico-modelos-reproducibles-y-verificacion/CLASE.md).

### Modelo submalla

- El modelo submalla es una regla para procesos no resueltos.

💡 **Cómo se explica en la clase [B38-C07](../programa/clases/B38/B38-C07-modelos-submalla-de-formacion-estelar-y-retroalimentacion/CLASE.md):**
- Nombrar los límites de un modelo submalla.
- La evidencia es la ficha de los modelos submalla del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** El gas denso forma estrellas por debajo de la resolución de la simulación y las supernovas devuelven energía. La decisión central: ¿cuánto gas expulsa la retroalimentación y a qué equilibrio llega la zona?

📘 **Dónde se aprende** (1 clase): [B38-C07 · Modelos submalla de formación estelar y retroalimentación](../programa/clases/B38/B38-C07-modelos-submalla-de-formacion-estelar-y-retroalimentacion/CLASE.md).

### Modelo sustituto

- Un modelo sustituto (*surrogate*, o emulador) es un modelo aprendido de pares (entrada, salida del simulador) que lo aproxima.

💡 **Cómo se explica en la clase [B17-C04](../programa/clases/B17/B17-C04-modelos-sustitutos-surrogates/CLASE.md):**
- Ejercicio 12 · integrador. Redacta la ficha del sustituto: simulador, entradas con unidad y rango, salida, verificación del simulador, diseño de puntos, modelo y núcleo, error medio y máximo en puntos reservados, cobertura de la banda, dominio de validez y uso prohibido.
- python programa/clases/B17/B17-C04-modelos-sustitutos-surrogates/sustituto_cohete.py
- 🎯 **Por qué importa:** Un simulador de trayectoria, de aerodinámica o de transporte de radiación puede tardar minutos u horas por ejecución. Para explorar miles de combinaciones de parámetros (un análisis de sensibilidad, una propagación de incertidumbre, una optimización) no alcanza el tiempo.

📘 **Dónde se aprende** (1 clase): [B17-C04 · Modelos sustitutos (surrogates)](../programa/clases/B17/B17-C04-modelos-sustitutos-surrogates/CLASE.md).

### Modelo wCDM

- El modelo wCDM añade `w` a ΛCDM.

💡 **Cómo se explica en la clase [B26-C22](../programa/clases/B26/B26-C22-degeneraciones-de-parametros-cosmologicos/CLASE.md):**
- Para supernovas con error `σ = 0,15 mag`, modelo wCDM plano y valores fiduciales `Ω_m = 0,315`, `w = −1`, `H₀ = 67,4`: derivadas numéricas centrales `∂μ/∂Ω_m` y `∂μ/∂w`, a las que se resta su media (marginalizar la constante de calibración).
- 🎯 **Por qué importa:** Una incertidumbre marginal puede ser mucho mayor que la que se obtendría si el otro parámetro estuviera fijo, porque ambos se compensan. Sin analizar la degeneración se interpretan mal las barras de error y se desaprovechan las combinaciones de datos.

📘 **Dónde se aprende** (1 clase): [B26-C22 · Degeneraciones de parámetros cosmológicos](../programa/clases/B26/B26-C22-degeneraciones-de-parametros-cosmologicos/CLASE.md).

### Modificado

- Tus archivos pasan por tres estados: modificado (editado, aún no registrado), preparado (*staged*, marcado para el próximo commit) y confirmado (guardado en la base local) (S2).

🎯 **Por qué importa (clase B07-C14):** Sin control de versiones, un proyecto científico acumula archivos como `analisis_final.py`, `analisis_final2.py` y `analisis_final_ahora_si.py`, y nadie sabe cuál produjo la figura del artículo. Con Git, cada estado importante queda guardado con un mensaje, una fecha y un autor, y puedes comparar o recuperar cualquier versión.

📘 **Dónde se aprende** (1 clase): [B07-C14 · Control de versiones con Git](../programa/clases/B07/B07-C14-control-de-versiones-con-git/CLASE.md).

### Modo

- Un modo (nominal, seguro, de eclipse) es una configuración con reglas propias.
- Un modo es una forma `φ` con frecuencia `f = ω/(2π)`.
- El modo es una configuración de la nave con su consumo.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B83-C03](../programa/clases/B83/B83-C03-concepto-de-operaciones-conops/CLASE.md):**
- En operaciones hay tres modos: nominal (carga útil activa), eclipse (carga apagada) y seguro (solo supervivencia).
- F["Fases y modos"] --> O["Orbita y estacion"]
- 🎯 **Por qué importa:** Los requisitos de datos, energía y operaciones dependen de cuántas veces al día se puede hablar con el satélite y por cuánto tiempo. La decisión central: ¿cuánto contacto real ofrece la órbita y cómo se reparte en las fases de la misión?

📘 **Dónde se aprende** (4 clases): [B83-C03 · Concepto de operaciones CONOPS](../programa/clases/B83/B83-C03-concepto-de-operaciones-conops/CLASE.md); [B84-C10 · Análisis modal](../programa/clases/B84/B84-C10-analisis-modal/CLASE.md); [B86-C01 · Balance de potencia eléctrica](../programa/clases/B86/B86-C01-balance-de-potencia-electrica/CLASE.md); [B88-C09 · Telecomandos y estados de misión](../programa/clases/B88/B88-C09-telecomandos-y-estados-de-mision/CLASE.md).

### Modo acústico

- Un modo acústico (modo p) es una onda sonora estacionaria cuyo restablecimiento es la presión.

💡 **Cómo se explica en la clase [B24-C14](../programa/clases/B24/B24-C14-asterosismologia-inicial/CLASE.md):**
- Definir modo acústico, modo de gravedad, separación grande y resolución en frecuencia.
- 🎯 **Por qué importa:** La asterosismología es la única manera de «ver» el interior de estrellas lejanas: da densidad media, masa y radio con una precisión que la fotometría y la espectroscopía no alcanzan, y distingue si una gigante quema hidrógeno en capa o helio en el núcleo.

📘 **Dónde se aprende** (1 clase): [B24-C14 · Asterosismología inicial](../programa/clases/B24/B24-C14-asterosismologia-inicial/CLASE.md).

### Modo B

- El modo E y el modo B.

💡 **Cómo se explica en la clase [B40-C08](../programa/clases/B40/B40-C08-polarizacion-e-y-b-del-fondo-cosmico/CLASE.md):**
- *Descripción textual:* se rota entre `(E, B)` y `(Q, U)` en Fourier, y una máscara en el espacio real mezcla los modos.
- Ejercicio 8. ¿Por qué se anulan los modos de Nyquist?
- 🎯 **Por qué importa:** Un modo B primordial sería una huella de ondas gravitacionales, pero las máscaras filtran E hacia B. La decisión central: ¿cómo se separan E y B y cuánto contamina una máscara?

📘 **Dónde se aprende** (1 clase): [B40-C08 · Polarización E y B del fondo cósmico](../programa/clases/B40/B40-C08-polarizacion-e-y-b-del-fondo-cosmico/CLASE.md).

### Modo común

- El modo común `ρ` es la fracción de errores que comparten ejecutor y verificador.

💡 **Cómo se explica en la clase [B110-C05](../programa/clases/B110/B110-C05-checklists-de-emergencia-ejecucion-y-verificacion-cruzada/CLASE.md):**
- *Descripción textual:* un error ocurre con probabilidad `p`, puede ser notado por quien ejecuta (`s`) y luego por el verificador (`d`, reducido por el modo común `ρ`); lo que sobrevive es `u` y se acumula sobre `N` pasos.
- Incorporar la correlación de modo común entre ejecutor y verificador.
- ⚠️ **Error frecuente:** Creer que verificar siempre divide el riesgo por `d`. El modo común lo limita (8.5).
- 🎯 **Por qué importa:** Los checklists de emergencia se leen y verifican bajo estrés y no tenían clase propia. La decisión central: ¿cuánta verificación cruzada vale su costo en tiempo, y qué la hace menos eficaz de lo que parece?

📘 **Dónde se aprende** (1 clase): [B110-C05 · Checklists de emergencia: ejecución y verificación cruzada](../programa/clases/B110/B110-C05-checklists-de-emergencia-ejecucion-y-verificacion-cruzada/CLASE.md).

### Modo de bajo consumo

- El modo de bajo consumo (*sleep*) reduce la corriente mientras no hay trabajo.

🎯 **Por qué importa (clase B88-C02):** Un error de configuración (un divisor mal calculado, una resolución insuficiente) no se ve en el escritorio y aparece en órbita. La decisión central: ¿qué valores de registro dan la temporización, la velocidad y la resolución que exige el requisito, con qué error?

📘 **Dónde se aprende** (1 clase): [B88-C02 · Microcontroladores embarcados](../programa/clases/B88/B88-C02-microcontroladores-embarcados/CLASE.md).

### Modo de falla

- Un modo de falla es la forma en que una función deja de operar.

💡 **Cómo se explica en la clase [B118-C11](../programa/clases/B118/B118-C11-diseno-para-mitigacion-de-desechos/CLASE.md):**
- Las directrices de la COPUOS (2010, consultadas) piden diseñar para evitar modos de falla que lleven a rupturas accidentales (directriz 2) y agotar o hacer seguras las fuentes de energía almacenada (directriz 5).
- 🎯 **Por qué importa:** Una disposición solo es posible si el satélite sigue funcionando al final de su vida. La probabilidad de éxito de la PMD no es la fiabilidad de la misión, sino la de las funciones necesarias para disponer.

📘 **Dónde se aprende** (1 clase): [B118-C11 · Diseño para mitigación de desechos](../programa/clases/B118/B118-C11-diseno-para-mitigacion-de-desechos/CLASE.md).

### Modo de fallo

- Un modo de fallo es la forma de fallar; su efecto es la consecuencia.

💡 **Cómo se explica en la clase [B83-C22](../programa/clases/B83/B83-C22-analisis-de-modos-y-efectos-de-fallo-fmea-en-sistemas-espaciales/CLASE.md):**
- C["Componente"] --> M["Modos de fallo y efectos"]
- Porque las fracciones reparten todos los fallos del componente entre sus modos.
- 🎯 **Por qué importa:** Los fallos que no se anticipan se descubren en órbita. La decisión central: ¿qué modos de fallo hay que atacar primero, cuánta probabilidad tienen en la vida de la misión y qué cambia si mejoro su detección?

📘 **Dónde se aprende** (1 clase): [B83-C22 · Análisis de modos y efectos de fallo (FMEA) en sistemas espaciales](../programa/clases/B83/B83-C22-analisis-de-modos-y-efectos-de-fallo-fmea-en-sistemas-espaciales/CLASE.md).

### Modo de gravedad

- Un modo de gravedad (modo g) es una onda con la flotabilidad como fuerza restauradora.

💡 **Cómo se explica en la clase [B24-C14](../programa/clases/B24/B24-C14-asterosismologia-inicial/CLASE.md):**
- Definir modo acústico, modo de gravedad, separación grande y resolución en frecuencia.
- Distinguir gigantes por sus modos de gravedad.
- 🎯 **Por qué importa:** La asterosismología es la única manera de «ver» el interior de estrellas lejanas: da densidad media, masa y radio con una precisión que la fotometría y la espectroscopía no alcanzan, y distingue si una gigante quema hidrógeno en capa o helio en el núcleo.

📘 **Dónde se aprende** (1 clase): [B24-C14 · Asterosismología inicial](../programa/clases/B24/B24-C14-asterosismologia-inicial/CLASE.md).

### Modo de operación

- Un modo de operación es una configuración de la nave con su consumo.

💡 **Cómo se explica en la clase [B86-C21](../programa/clases/B86/B86-C21-modos-de-operacion-y-estados-de-bajo-consumo/CLASE.md):**
- python programa/clases/B86/B86-C21-modos-de-operacion-y-estados-de-bajo-consumo/modos_bajo_consumo.py
- 🎯 **Por qué importa:** Cuando la energía escasea, apagar la carga útil a tiempo mantiene viva la nave. Un umbral único hace oscilar al sistema entre modos; la histéresis lo evita.

📘 **Dónde se aprende** (1 clase): [B86-C21 · Modos de operación y estados de bajo consumo](../programa/clases/B86/B86-C21-modos-de-operacion-y-estados-de-bajo-consumo/CLASE.md).

### Modo de sólido rígido

- Un modo de sólido rígido tiene autovalor nulo.

💡 **Cómo se explica en la clase [B84-C28](../programa/clases/B84/B84-C28-condiciones-de-contorno-y-cargas-en-modelos-de-elementos-finitos/CLASE.md):**
- Límite: aquí el modelo es una viga plana; en 3D hay 6 modos de sólido rígido.
- Por autovalores: modos de sólido rígido.
- 🎯 **Por qué importa:** Una restricción de menos deja la matriz singular; una de más introduce tensiones falsas; una carga mal repartida cambia la flecha 1,25 %: son los errores más frecuentes en los modelos. La decisión central: ¿está el modelo bien restringido y cargado y cómo lo demuestro?

📘 **Dónde se aprende** (1 clase): [B84-C28 · Condiciones de contorno y cargas en modelos de elementos finitos](../programa/clases/B84/B84-C28-condiciones-de-contorno-y-cargas-en-modelos-de-elementos-finitos/CLASE.md).

### Modo E

- El modo E y el modo B.

💡 **Cómo se explica en la clase [B40-C08](../programa/clases/B40/B40-C08-polarizacion-e-y-b-del-fondo-cosmico/CLASE.md):**
- *Descripción textual:* se rota entre `(E, B)` y `(Q, U)` en Fourier, y una máscara en el espacio real mezcla los modos.
- Ejercicio 8. ¿Por qué se anulan los modos de Nyquist?
- 🎯 **Por qué importa:** Un modo B primordial sería una huella de ondas gravitacionales, pero las máscaras filtran E hacia B. La decisión central: ¿cómo se separan E y B y cuánto contamina una máscara?

📘 **Dónde se aprende** (1 clase): [B40-C08 · Polarización E y B del fondo cósmico](../programa/clases/B40/B40-C08-polarizacion-e-y-b-del-fondo-cosmico/CLASE.md).

### Modo endotérmico

- En modo endotérmico (`V < E_tn`) la celda absorbe calor; en exotérmico (`V > E_tn`) lo cede.

💡 **Cómo se explica en la clase [B59-C10](../programa/clases/B59/B59-C10-electrolisis-y-balances-energeticos/CLASE.md):**
- Una planta ilustrativa de 10 kW a `0,5 A/cm²` (tensión `1,144 V`) necesita `8 741 A` y `17 481 cm²` y produce `7,495 kg/día` de H₂ y `59,5 kg/día` de O₂; como `1,144 V < 1,2532 V`, trabaja en modo endotérmico: absorbe `406 W` de calor.
- Distinguir los modos endotérmico y exotérmico.
- ⚠️ **Error frecuente:** Ignorar el modo endotérmico. Se corrige con 8.3.
- 🎯 **Por qué importa:** La electrólisis es el mayor consumidor de energía de la planta. La decisión central: ¿a qué densidad de corriente conviene operar, entre una celda pequeña que gasta más electricidad y una grande que gasta menos?

📘 **Dónde se aprende** (1 clase): [B59-C10 · Electrólisis y balances energéticos](../programa/clases/B59/B59-C10-electrolisis-y-balances-energeticos/CLASE.md).

### Modo fundamental

- El modo fundamental `k_f = 2π/L`.

🎯 **Por qué importa (clase B36-C04):** Un espectro estimado sin su error no se puede comparar con un modelo. La decisión central: ¿está la desviación de cada intervalo dentro de la varianza cósmica?

📘 **Dónde se aprende** (1 clase): [B36-C04 · Espectro de potencia de materia](../programa/clases/B36/B36-C04-espectro-de-potencia-de-materia/CLASE.md).

### Modo gobernante

- El modo gobernante es el de menor margen.

💡 **Cómo se explica en la clase [B85-C20](../programa/clases/B85/B85-C20-presupuesto-termico-de-carga-util/CLASE.md):**
- *Descripción textual:* la disipación por modo con margen se compara con la capacidad del radiador en el caso caliente; en el frío la capacidad define el calentador; el menor margen indica el modo gobernante.
- El script [presupuesto_termico.py](presupuesto_termico.py) suma las disipaciones, calcula la capacidad del radiador, los márgenes, el calentador y el área mínima (comprueba área mínima por fórmula frente a bisección (1e-9), suma por dos caminos y modo gobernante).
- 🎯 **Por qué importa:** Un presupuesto sin margen no resiste un cambio de diseño. La decisión central: ¿qué modo gobierna el caso caliente, con cuánto margen cierra y qué calentador pide el frío?

📘 **Dónde se aprende** (1 clase): [B85-C20 · Presupuesto térmico de carga útil](../programa/clases/B85/B85-C20-presupuesto-termico-de-carga-util/CLASE.md).

### Modo invisible

- El modo invisible (piston y tablero).

💡 **Cómo se explica en la clase [B42-C22](../programa/clases/B42/B42-C22-reconstructores-de-frente-de-onda-zonal-y-modal/CLASE.md):**
- Ejercicio 11 · transferencia. Transferencia. ¿Qué es un modo invisible?
- 🎯 **Por qué importa:** El reconstructor decide qué parte del frente se recupera y cuánto ruido se propaga. La decisión central: ¿zonal o modal, y con cuántos modos?

📘 **Dónde se aprende** (1 clase): [B42-C22 · Reconstructores de frente de onda: zonal y modal](../programa/clases/B42/B42-C22-reconstructores-de-frente-de-onda-zonal-y-modal/CLASE.md).

### Modo kink

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B34-C04):** La sismología coronal mide lo que no se ve. La decisión central: ¿qué campo implica un período y con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B34-C04 · Ondas y oscilaciones coronales como sismología solar](../programa/clases/B34/B34-C04-ondas-y-oscilaciones-coronales-como-sismologia-solar/CLASE.md).

### Modo mixto

- Un modo mixto se comporta como p en una zona y g en otra.
- Un modo mixto tiene carácter p en la envoltura y g en el núcleo.

💡 **Cómo se explica en la clase [B37-C08](../programa/clases/B37/B37-C08-oscilaciones-no-radiales-modos-p-g-y-mixtos/CLASE.md):**
- p y g viven en cavidades separadas por una zona evanescente; si esa zona es delgada, los modos se acoplan y se vuelven mixtos (C12).
- python programa/clases/B37/B37-C08-oscilaciones-no-radiales-modos-p-g-y-mixtos/no_radiales.py
- 🎯 **Por qué importa:** Los modos p y g sondean regiones distintas. La decisión central: ¿en qué cavidad se propaga un modo de frecuencia y grado dados?

📘 **Dónde se aprende** (2 clases): [B37-C08 · Oscilaciones no radiales: modos p, g y mixtos](../programa/clases/B37/B37-C08-oscilaciones-no-radiales-modos-p-g-y-mixtos/CLASE.md); [B37-C12 · Gigantes rojas oscilantes y modos mixtos](../programa/clases/B37/B37-C12-gigantes-rojas-oscilantes-y-modos-mixtos/CLASE.md).

### Modo nocturno rojo

- Un modo nocturno rojo reduce el brillo y evita deslumbrar los ojos.

🎯 **Por qué importa (clase B08-C07):** Una herramienta que no entiendes es una caja negra: si la aplicación se equivoca de ubicación o de hora, no lo notarás. La pregunta motivadora: ¿puedo confiar en lo que me muestra la herramienta, y qué hago si no hay batería?

📘 **Dónde se aprende** (1 clase): [B08-C07 · Planisferios y aplicaciones celestes](../programa/clases/B08/B08-C07-planisferios-y-aplicaciones-celestes/CLASE.md).

### Modo p

- El modo p tiene presión como fuerza restauradora; el g, el empuje.

💡 **Cómo se explica en la clase [B37-C08](../programa/clases/B37/B37-C08-oscilaciones-no-radiales-modos-p-g-y-mixtos/CLASE.md):**
- p y g viven en cavidades separadas por una zona evanescente; si esa zona es delgada, los modos se acoplan y se vuelven mixtos (C12).
- *Descripción textual:* la comparación de la frecuencia con `L_l` y `N` decide dónde se propaga cada modo.
- ⚠️ **Error frecuente:** Creer que todo modo llega a la superficie. Se corrige con 8.3.
- 🎯 **Por qué importa:** Los modos p y g sondean regiones distintas. La decisión central: ¿en qué cavidad se propaga un modo de frecuencia y grado dados?

📘 **Dónde se aprende** (1 clase): [B37-C08 · Oscilaciones no radiales: modos p, g y mixtos](../programa/clases/B37/B37-C08-oscilaciones-no-radiales-modos-p-g-y-mixtos/CLASE.md).

### Modo radial

- Un modo radial conserva la simetría esférica (`l = 0`).

💡 **Cómo se explica en la clase [B37-C07](../programa/clases/B37/B37-C07-oscilaciones-radiales-y-relacion-periodo-densidad-media/CLASE.md):**
- Ejercicio 12. Integrador. Elabora tu *ficha de oscilaciones radiales*: modo fundamental y escala.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de oscilaciones radiales*: modo fundamental y escala.
- 🎯 **Por qué importa:** El período fundamental fija la densidad media. La decisión central: ¿cuánto vale el período de un modo radial y cómo escala con la densidad?

📘 **Dónde se aprende** (1 clase): [B37-C07 · Oscilaciones radiales y relación período-densidad media](../programa/clases/B37/B37-C07-oscilaciones-radiales-y-relacion-periodo-densidad-media/CLASE.md).

### Modo seguro

- El modo seguro es el de consumo mínimo.
- Un modo seguro es un estado de baja actividad al que se llega ante un problema.

💡 **Cómo se explica en la clase [B86-C21](../programa/clases/B86/B86-C21-modos-de-operacion-y-estados-de-bajo-consumo/CLASE.md):**
- Con `125 W` en luz el modo nominal pierde energía en cada órbita (`ΔE < 0`), y el reducido y el seguro la ganan.
- *Descripción textual:* el modo nominal baja a reducido con SOC menor de `40 %` y vuelve con SOC mayor de `60 %`; con SOC menor de `25 %` se pasa a seguro, que vuelve a reducido por encima de `45 %`.
- 🎯 **Por qué importa:** Cuando la energía escasea, apagar la carga útil a tiempo mantiene viva la nave. Un umbral único hace oscilar al sistema entre modos; la histéresis lo evita.

📘 **Dónde se aprende** (2 clases): [B86-C21 · Modos de operación y estados de bajo consumo](../programa/clases/B86/B86-C21-modos-de-operacion-y-estados-de-bajo-consumo/CLASE.md); [B98-C02 · Sistemas de decisión autónomos y máquinas de estados de comportamiento](../programa/clases/B98/B98-C02-sistemas-de-decision-autonomos-y-maquinas-de-estados-de-comportamiento/CLASE.md).

### Modos aceleradores

- Los modos aceleradores aparecen cerca de `K = 2πm` y producen `α > 1`.

💡 **Cómo se explica en la clase [B73-C15](../programa/clases/B73/B73-C15-difusion-orbital/CLASE.md):**
- Con `K = 6,5`, cerca de `2π`, el coeficiente de ajuste (`448`) no es un coeficiente de difusión: `α = 1,79` indica transporte anómalo por modos aceleradores.
- Analogía: una multitud que sale de un estadio: si las calles son rectas y ordenadas (régimen regular) casi nadie se aleja; si hay cruces confusos (caos) la gente se dispersa como una caminata aleatoria; si hay un tren expreso (modo acelerador) algunos se alejan mucho más rápido.
- 🎯 **Por qué importa:** Un conjunto de cuerpos en una región caótica no escapa de golpe: su excentricidad o su semieje se esparce como una caminata aleatoria, y el tiempo que tarda en recorrer una región fija la escala de supervivencia de la población. La decisión central: ¿cómo medir un coeficiente de difusión y cuándo no tiene sentido hablar de él?

📘 **Dónde se aprende** (1 clase): [B73-C15 · Difusión orbital](../programa/clases/B73/B73-C15-difusion-orbital/CLASE.md).

### Modos de Zernike

- Los modos de Zernike (base ortonormal en el disco).

🎯 **Por qué importa (clase B42-C13):** La óptica adaptativa solo corrige lo que mide. La decisión central: ¿qué se mide (pendientes o fase), cuántos modos se ajustan y cuánto ruido llega a los coeficientes?

📘 **Dónde se aprende** (1 clase): [B42-C13 · Medición de frente de onda](../programa/clases/B42/B42-C13-medicion-de-frente-de-onda/CLASE.md).

### Modulación anual

- La modulación anual por el movimiento de la Tierra.

💡 **Cómo se explica en la clase [B36-C10](../programa/clases/B36/B36-C10-busqueda-directa-de-materia-oscura-en-laboratorio/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. ¿Por qué se mide la modulación anual?
- 🎯 **Por qué importa:** Un límite de sección eficaz depende de la cinemática, de la exposición y de las cuentas. La decisión central: ¿qué sección eficaz excluye una exposición sin sucesos?

📘 **Dónde se aprende** (1 clase): [B36-C10 · Búsqueda directa de materia oscura en laboratorio](../programa/clases/B36/B36-C10-busqueda-directa-de-materia-oscura-en-laboratorio/CLASE.md).

### Modulación rotacional

- La modulación rotacional es la variación periódica del brillo porque la mancha entra y sale de la vista.

💡 **Cómo se explica en la clase [B24-C12](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md):**
- Definir mancha, contraste y modulación rotacional.
- 🎯 **Por qué importa:** La modulación del brillo por manchas permite medir el periodo de rotación de miles de estrellas sin necesitar espectros, pero también contamina la búsqueda de exoplanetas y limita la precisión de las velocidades radiales.

📘 **Dónde se aprende** (1 clase): [B24-C12 · Manchas y actividad estelar](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md).

### Módulo

- El módulo es su tamaño: `|v| = √(vₓ² + v_y²)`.
- Un módulo es un archivo `.py` cuyos nombres puedes reutilizar con `import` (S3).
- Un número complejo es `z = a + b i`, con `i² = −1`; su módulo es `|z| = √(a² + b²)`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C12](../programa/clases/B04/B04-C12-vectores-y-componentes/CLASE.md):**
- Un vector `v = (vₓ, v_y, v_z)` en tres dimensiones tiene módulo `|v| = √(vₓ² + v_y² + v_z²)`.
- Con `(3; 0)` (radial): `(3; 29,79)`, módulo `√(9 + 887,5) = 29,94 km/s`, cuya componente radial es 3 y la tangencial, 29,79.
- ⚠️ **Error frecuente:** Sumar módulos en lugar de vectores. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Una sonda que sale de la Tierra tiene una velocidad respecto de la Tierra y la Tierra tiene una velocidad respecto del Sol. ¿Cuál es la velocidad de la sonda respecto del Sol?

📘 **Dónde se aprende** (4 clases): [B04-C12 · Vectores y componentes](../programa/clases/B04/B04-C12-vectores-y-componentes/CLASE.md); [B07-C06 · Funciones y modularidad](../programa/clases/B07/B07-C06-funciones-y-modularidad/CLASE.md); [B15-C04 · Transformada de Fourier](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md); [B109-C05 · Crecimiento modular y escalabilidad de asentamientos](../programa/clases/B109/B109-C05-crecimiento-modular-y-escalabilidad-de-asentamientos/CLASE.md).

### Módulo de deformación de corte

- `K` es el módulo de deformación de corte.

🎯 **Por qué importa (clase B97-C06):** Un rover que se atasca puede perder la misión. Estimar cuánta tracción hay disponible en cada gravedad, y cómo varía con el deslizamiento, permite limitar pendientes y planear rutas.

📘 **Dónde se aprende** (1 clase): [B97-C06 · Control de movilidad sobre regolito](../programa/clases/B97/B97-C06-control-de-movilidad-sobre-regolito/CLASE.md).

### Módulo de distancia

- La magnitud aparente `m` mide cuán brillante *se ve* un objeto desde donde se mide; la magnitud absoluta `M` es la que tendría a 10 parsecs; la diferencia `m − M` es el módulo de distancia.
- El módulo de distancia es `m − M = 5 log₁₀(d/10 pc)`.
- El módulo de distancia es `5 log₁₀(d/10 pc)`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C05](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md):**
- *Descripción textual:* se parte de un flujo, se divide por el flujo de referencia, se aplica `−2,5 log₁₀` para obtener la magnitud, y restando la magnitud absoluta se obtiene el módulo de distancia, de donde sale la distancia.
- Paso 3 · Módulo de distancia. `d = 1 au = 4,848 × 10⁻⁶ pc`;
- ⚠️ **Error frecuente:** Olvidar el −5 del módulo de distancia o usar `d` en au. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** El ojo y los instrumentos comparan brillos que difieren en factores de un millón. Los astrónomos lo resuelven con una escala logarítmica: la magnitud.

📘 **Dónde se aprende** (6 clases): [B04-C05 · Funciones exponenciales y logarítmicas](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md); [B24-C13 · Estrellas variables](../programa/clases/B24/B24-C13-estrellas-variables/CLASE.md); [B25-C19 · Catálogos y sesgos de selección](../programa/clases/B25/B25-C19-catalogos-y-sesgos-de-seleccion/CLASE.md); [B26-C19 · Energía oscura y parámetros](../programa/clases/B26/B26-C19-energia-oscura-y-parametros/CLASE.md); [B28-C19 · Limitaciones y sesgos de detección](../programa/clases/B28/B28-C19-limitaciones-y-sesgos-de-deteccion/CLASE.md); [B45-C02 · Magnitudes y sistemas de filtros](../programa/clases/B45/B45-C02-magnitudes-y-sistemas-de-filtros/CLASE.md).

### Módulo de Thiele

- El módulo de Thiele `φ = L √(k/D_e)` compara consumo con difusión.

💡 **Cómo se explica en la clase [B64-C06](../programa/clases/B64/B64-C06-biofilms-en-ambientes-extremos/CLASE.md):**
- *Descripción textual:* los parámetros definen el módulo de Thiele; de él sale el perfil analítico y el factor de efectividad, y el perfil se contrasta con la solución numérica de diferencias finitas.
- Calcular el módulo de Thiele, el perfil de concentración y el factor de efectividad.
- 🎯 **Por qué importa:** Una película de células y matriz crea su propio microambiente. La pregunta motivadora: ¿hasta qué profundidad llega un nutriente en un biofilm y qué sucede con las células que quedan más adentro?

📘 **Dónde se aprende** (1 clase): [B64-C06 · Biofilms en ambientes extremos](../programa/clases/B64/B64-C06-biofilms-en-ambientes-extremos/CLASE.md).

### Módulo de Weibull

- `m` es el módulo de Weibull (menor `m` = más dispersión) y `σ₀` la resistencia característica.

🎯 **Por qué importa (clase B84-C04):** Un metal avisa antes de romper; una cerámica no. Diseñar con la resistencia media de una probeta pequeña sobreestima la de una pieza grande en 40 %.

📘 **Dónde se aprende** (1 clase): [B84-C04 · Cerámicos y polímeros espaciales](../programa/clases/B84/B84-C04-ceramicos-y-polimeros-espaciales/CLASE.md).

### Módulo de Young

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B43-C03):** Un buen material no es el más duro ni el más estable: es el que deja el menor error de forma para una masa y un presupuesto. La decisión central: ¿qué material y qué espesor mantienen la flexión y la deriva térmica por debajo de la tolerancia?

📘 **Dónde se aprende** (1 clase): [B43-C03 · Materiales para espejos](../programa/clases/B43/B43-C03-materiales-para-espejos/CLASE.md).

### MOIC

- El MOIC es el múltiplo de lo recibido sobre lo invertido.

💡 **Cómo se explica en la clase [B124-C07](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md):**
- Se reciben `300` Mum y se invierten `140`: MOIC `2,143`.
- El MOIC no dice cuánto tarda; la TIR sí.
- 🎯 **Por qué importa:** El dinero privado tiene un costo distinto del público: se paga con retorno y con propiedad. La decisión central: ¿qué retorno exige y qué parte del proyecto se cede a cambio?

📘 **Dónde se aprende** (1 clase): [B124-C07 · Financiamiento privado](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md).

### MOID

- El MOID es la distancia mínima entre dos órbitas, no entre los cuerpos.

💡 **Cómo se explica en la clase [B58-C05](../programa/clases/B58/B58-C05-orbitas-cercanas-a-la-tierra/CLASE.md):**
- (iii) Circular inclinada de radio `a`: la distancia al cuadrado es `a² − 2ρ + 1`, mínima en el nodo, donde `ρ = a`, así que `MOID = |a−1|`;
- SINT-A (`H = 21`, MOID `0.080`) no es PHA;
- ⚠️ **Error frecuente:** Confundir MOID con distancia de acercamiento. Se corrige con la sección 7.
- 🎯 **Por qué importa:** Dos órbitas pueden cruzarse en proyección sin que los cuerpos coincidan nunca, y pueden no cruzarse y estar a una distancia pequeña. El MOID separa los casos geométricamente.

📘 **Dónde se aprende** (1 clase): [B58-C05 · Órbitas cercanas a la Tierra](../programa/clases/B58/B58-C05-orbitas-cercanas-a-la-tierra/CLASE.md).

### Mol

- Su unidad es el mol: un mol contiene exactamente 6,022 140 76 × 10²³ entidades elementales, número que es el valor fijado de la constante de Avogadro `N_A` (en mol⁻¹), según la definición vigente del SI (S2).

💡 **Cómo se explica en la clase [B06-C06](../programa/clases/B06/B06-C06-cantidad-de-sustancia-y-mol/CLASE.md):**
- Desde 2019, el SI define el mol fijando el valor de `N_A = 6,022 140 76 × 10²³ mol⁻¹`; lo que antes se medía ahora se adopta por definición (S2).
- Con ese valor exacto y con la unidad de masa atómica `u`, el producto `N_A · u` es muy cercano a 1 g/mol: con los valores CODATA 2022 resulta `1,000 000 001 1 g/mol` (el laboratorio de la sección 17 lo calcula).
- ⚠️ **Error frecuente:** Confundir mol con masa. Un mol es un número de partículas.
- 🎯 **Por qué importa:** La misión OSIRIS-REx trajo a la Tierra 121,6 g de material del asteroide Bennu. Los análisis de laboratorio de una parte de esa muestra encontraron entre 4,5 y 4,7 % de carbono y entre 0,23 y 0,25 % de nitrógeno en masa (S1).

📘 **Dónde se aprende** (1 clase): [B06-C06 · Cantidad de sustancia y mol](../programa/clases/B06/B06-C06-cantidad-de-sustancia-y-mol/CLASE.md).

### Molalidad

- La molalidad `m` se expresa en mol/kg.

💡 **Cómo se explica en la clase [B64-C04](../programa/clases/B64/B64-C04-halofilos-y-vida-en-salmueras/CLASE.md):**
- Para calcular, usas una salmuera de NaCl sintética con molalidades de 0,01 a 6 mol/kg y un coeficiente osmótico `φ` propuesto por fila.
- Descripción larga: al subir la molalidad, `a_w` cae de 1 a 0,76 y la presión osmótica crece de 0,05 a 37 MPa.
- ⚠️ **Error frecuente:** Confundir molaridad y molalidad. Se corrige con la sección 8.1.
- 🎯 **Por qué importa:** En una salmuera concentrada el agua existe pero «no está disponible» del mismo modo. La pregunta motivadora: ¿cuánta sal puede haber en el exterior antes de que el agua deje de bastar para la célula?

📘 **Dónde se aprende** (1 clase): [B64-C04 · Halófilos y vida en salmueras](../programa/clases/B64/B64-C04-halofilos-y-vida-en-salmueras/CLASE.md).

### Molaridad

- La concentración `c` se expresa en mol/L (molaridad) o, para muestras sólidas extraídas, en μmol por gramo.

🎯 **Por qué importa (clase B06-C15):** El extracto en agua caliente de las muestras de Bennu contiene amoníaco libre en unos 13,6 μmol por gramo y ácido fórmico en 4,106 μmol por gramo (S1). Un ácido y una base en el mismo líquido reaccionan entre sí: el ácido cede un protón, la base lo acepta y se forman iones.

📘 **Dónde se aprende** (1 clase): [B06-C15 · Ácidos, bases y soluciones](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md).

### Momento

- El momento `p` es un vector auxiliar de la misma dimensión, sorteado de `N(0, I)` en cada iteración.
- Un momento es la integral de `vⁿ f`.
- El momento es una suma ponderada de las cuentas.

💡 **Cómo se explica en la clase [B19-C03](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md):**
- Es *reversible*: si al final inviertes el signo del momento y repites `L` pasos, vuelves al punto inicial (el laboratorio lo comprueba a 10⁻¹⁰).
- A["Estado q"] --> B["Sortea momento p ~ N(0, I)"]
- 🎯 **Por qué importa:** Una posterior bidimensional con dos parámetros correlacionados al 95 % tiene forma de un óvalo muy alargado y estrecho. Un Metropolis de paso aleatorio, para no salirse del óvalo, da pasos minúsculos y recorre la distribución a paso de tortuga.

📘 **Dónde se aprende** (3 clases): [B19-C03 · Hamiltonian Monte Carlo y NUTS](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md); [B35-C01 · Funciones de distribución de velocidades en plasmas](../programa/clases/B35/B35-C01-funciones-de-distribucion-de-velocidades-en-plasmas/CLASE.md); [B35-C06 · Mediciones in situ de plasmas espaciales](../programa/clases/B35/B35-C06-mediciones-in-situ-de-plasmas-espaciales/CLASE.md).

### Momento almacenado

- El momento almacenado es `h`.

🎯 **Por qué importa (clase B87-C11):** La rueda es el actuador estándar del control fino de tres ejes. La decisión central: ¿cuánto tarda una maniobra con límites de par y de momento, y qué velocidad alcanza la rueda?

📘 **Dónde se aprende** (1 clase): [B87-C11 · Ruedas de reacción](../programa/clases/B87/B87-C11-ruedas-de-reaccion/CLASE.md).

### Momento angular

- El momento angular de una partícula respecto de un punto `O` es `L = r × p = m (r × v)`; en 2D su valor es `L = m (x v_y − y v_x)` y se mide en `kg·m²/s`.
- El momento angular es `H = J ω` (N·m·s); la energía cinética de rotación es `T = ½ ω·J ω` (J).
- El momento angular es `L = m√(GMa)`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C09](../programa/clases/B05/B05-C09-momento-angular-y-torque/CLASE.md):**
- El momento angular es al giro lo que el momento lineal a la traslación; el torque es a `L` lo que la fuerza es a `p`: `τ = dL/dt`.
- *Descripción textual:* una fuerza aplicada en una posición crea un torque; si el torque neto es cero, el momento angular se conserva (caso de la fuerza central, que da `r_p v_p = r_a v_a`); si no, el momento angular cambia a razón del torque (en un rotor, `τ = I α`).
- 🎯 **Por qué importa:** Un satélite en órbita elíptica va más rápido cerca de la Tierra que lejos; un patinador gira más rápido al recoger los brazos. La pregunta motivadora es: ¿qué cantidad se mantiene constante cuando algo gira bajo una fuerza central, y qué hace falta para cambiar un giro?

📖 **Explicado a fondo:** [Momento angular](esencial/esencial-m-z.md#momento-angular) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (5 clases): [B05-C09 · Momento angular y torque](../programa/clases/B05/B05-C09-momento-angular-y-torque/CLASE.md); [B16-C17 · Control no lineal](../programa/clases/B16/B16-C17-control-no-lineal/CLASE.md); [B24-C11 · Rotación y campos magnéticos](../programa/clases/B24/B24-C11-rotacion-y-campos-magneticos/CLASE.md); [B52-C06 · Migración de planetas](../programa/clases/B52/B52-C06-migracion-de-planetas/CLASE.md); [B87-C01 · Dinámica de cuerpo rígido](../programa/clases/B87/B87-C01-dinamica-de-cuerpo-rigido/CLASE.md).

### Momento angular específico

- El momento angular específico es `h = L/m` (m²/s).
- La energía específica (por unidad de masa) es `E = v²/2 − GM/r` y el momento angular específico, `L = x·vy − y·vx`; ambos se conservan en un campo central.
- El momento angular específico `j` es el momento angular por unidad de masa.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C09](../programa/clases/B05/B05-C09-momento-angular-y-torque/CLASE.md):**
- El script [momento_angular_orbita.py](momento_angular_orbita.py) integra una órbita elíptica con velocity-Verlet y comprueba que el momento angular específico no varíe (< 10⁻⁹), que el apoapsis integrado coincida con el analítico (10⁻³) y que `h/2 = área/T` (10⁻⁶).
- 🎯 **Por qué importa:** Un satélite en órbita elíptica va más rápido cerca de la Tierra que lejos; un patinador gira más rápido al recoger los brazos. La pregunta motivadora es: ¿qué cantidad se mantiene constante cuando algo gira bajo una fuerza central, y qué hace falta para cambiar un giro?

📘 **Dónde se aprende** (6 clases): [B05-C09 · Momento angular y torque](../programa/clases/B05/B05-C09-momento-angular-y-torque/CLASE.md); [B07-C20 · Primer simulador de un movimiento celeste](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md); [B23-C02 · Pruebas de propiedades físicas](../programa/clases/B23/B23-C02-pruebas-de-propiedades-fisicas/CLASE.md); [B26-C08 · Geodésicas gravitacionales](../programa/clases/B26/B26-C08-geodesicas-gravitacionales/CLASE.md); [B52-C01 · Colapso de nebulosa protosolar](../programa/clases/B52/B52-C01-colapso-de-nebulosa-protosolar/CLASE.md); [B71-C06 · Momento angular específico](../programa/clases/B71/B71-C06-momento-angular-especifico/CLASE.md).

### Momento angular H

- RK4: integrador de cuarto orden. Momento angular `H`: conservado, aquí nulo.

💡 **Cómo se explica en la clase [B101-C06](../programa/clases/B101/B101-C06-simulacion-de-un-brazo-robotico-espacial/CLASE.md):**
- El momento angular se expresa como `H = A₀θ̇₀ + A₁q̇₁ + A₂q̇₂`, con los `Aᵢ` por derivadas numéricas de las posiciones, y `H = 0` da `θ̇₀`.
- Con el lazo de 40°: el centro de masa del sistema se mantiene en `2,7×10⁻¹⁷` m; el momento angular recalculado con velocidades por diferencias de la trayectoria (independiente de los `Aᵢ`) queda en `1,8×10⁻⁴` kg m²/s como máximo.
- 🎯 **Por qué importa:** En una estación o un satélite pesado la base casi no se mueve; en un satélite pequeño, sí. La decisión central: ¿cuánto se mueve la base al mover el brazo y cómo afecta eso a la posición del extremo?

📘 **Dónde se aprende** (1 clase): [B101-C06 · Simulación de un brazo robótico espacial](../programa/clases/B101/B101-C06-simulacion-de-un-brazo-robotico-espacial/CLASE.md).

### Momento de Fermi

- El momento de Fermi `p_F = h (3n/(8π))^{1/3}` es el momento máximo ocupado.
- El momento de Fermi `p_F` es el mayor momento ocupado a `T = 0`: `n = (8π/3h³)p_F³` (dos espines).

💡 **Cómo se explica en la clase [B24-C18](../programa/clases/B24/B24-C18-etapas-finales-de-evolucion/CLASE.md):**
- A temperatura cero los electrones llenan todos los estados hasta el momento de Fermi `p_F`, con la densidad numérica `n_e = (8π/3)(p_F/h)³`.
- 🎯 **Por qué importa:** El destino de una estrella es una enana blanca, una estrella de neutrones o un agujero negro; hay una masa límite que separa los dos primeros destinos. Calcularla muestra cómo la mecánica cuántica (presión de degeneración) sostiene a una estrella cuando ya no hay fusión.

📘 **Dónde se aprende** (2 clases): [B24-C18 · Etapas finales de evolución](../programa/clases/B24/B24-C18-etapas-finales-de-evolucion/CLASE.md); [B27-C01 · Presión de degeneración](../programa/clases/B27/B27-C01-presion-de-degeneracion/CLASE.md).

### Momento de inercia

- El momento de inercia `I` mide la resistencia de un cuerpo a cambiar su giro: para una masa puntual a distancia `r`, `I = m r²` (kg·m²).
- El momento de inercia `I` mide la resistencia a cambiar el giro; para una esfera uniforme, `I = (2/5) M R²`.
- El momento de inercia `I = ∭ ρ ρ_⊥² dV`, con `ρ_⊥` la distancia al eje.

💡 **Cómo se explica en la clase [B09-C18](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md):**
- El momento de inercia respecto a un eje usa `ρ_⊥² = r² sin²θ`: `I = ∭ ρ r² sin²θ dV = (8π/3) ∫₀^R ρ r⁴ dr`.
- La ficha de la Tierra de la NASA (S2) da la masa `5,9722 × 10²⁴ kg`, el radio medio volumétrico `6371,000 km`, la densidad media `5513 kg/m³` y el factor de momento de inercia polar `I/(MR²) = 0,3308`.
- 🎯 **Por qué importa:** La masa de la Tierra se conoce mucho mejor que la distribución de esa masa en su interior. Un solo número, la densidad media, no basta: el momento de inercia depende de cómo se reparte la masa.

📘 **Dónde se aprende** (3 clases): [B05-C09 · Momento angular y torque](../programa/clases/B05/B05-C09-momento-angular-y-torque/CLASE.md); [B09-C18 · Integrales dobles y triples](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md); [B24-C11 · Rotación y campos magnéticos](../programa/clases/B24/B24-C11-rotacion-y-campos-magneticos/CLASE.md).

### Momento de inercia de cabeceo

- El momento de inercia de cabeceo `I_y` es el respecto de un eje transversal por el centro de masa.

🎯 **Por qué importa (clase B77-C22):** El control de actitud se diseña para una masa, un centro de masa y una inercia que ya no son los mismos al final del quemado. La decisión central: ¿cuánto se mueve el centro de masa, cuánto cae la inercia y qué le pasa al margen?

📘 **Dónde se aprende** (1 clase): [B77-C22 · Centro de masa y su variación con el consumo de propelente](../programa/clases/B77/B77-C22-centro-de-masa-y-su-variacion-con-el-consumo-de-propelente/CLASE.md).

### Momento de inercia I

- Conservación del momento: la suma `Σ m v` no cambia sin fuerzas externas. Momento de inercia `I`: resistencia a girar.

🎯 **Por qué importa (clase B106-C16):** Sin peso ni fricción, toda fuerza tiene una reacción que mueve al operario o a la carga; un diseño de herramientas y de superficies que lo ignore produce maniobras inseguras. La decisión central: ¿qué sujeciones y qué límites de par o de empuje evitan que la reacción mueva al astronauta fuera de la tarea?

📘 **Dónde se aprende** (1 clase): [B106-C16 · Ergonomía en microgravedad](../programa/clases/B106/B106-C16-ergonomia-en-microgravedad/CLASE.md).

### Momento de vuelco

- El momento de vuelco es la fuerza por la desalineación lateral.

💡 **Cómo se explica en la clase [B76-C16](../programa/clases/B76/B76-C16-acoplamiento-y-captura/CLASE.md):**
- *Descripción textual:* las masas y la velocidad dan la masa reducida y la energía; la simulación confirma la conservación del momento, la velocidad común y la fuerza máxima, que con la desalineación da el momento de vuelco.
- Ejercicio 7 · autónomo. Calcula el momento de vuelco con desalineación de `5 cm`.
- 🎯 **Por qué importa:** A velocidades de centímetros por segundo, la captura se decide por la masa, la rigidez y el amortiguamiento. La decisión central: ¿cuánta energía hay que disipar y qué fuerzas aparecen en el contacto?

📘 **Dónde se aprende** (1 clase): [B76-C16 · Acoplamiento y captura](../programa/clases/B76/B76-C16-acoplamiento-y-captura/CLASE.md).

### Momento dipolar

- El momento dipolar `m` (A·m²) es la salida del actuador.

🎯 **Por qué importa (clase B87-C12):** Los magnetopares descargan ruedas (C14) y hacen detumbling (C16) con muy poca masa. La decisión central: ¿qué par se puede generar en cada instante, qué dirección queda inaccesible y basta una órbita para cubrir los tres ejes?

📘 **Dónde se aprende** (1 clase): [B87-C12 · Magnetopares](../programa/clases/B87/B87-C12-magnetopares/CLASE.md).

### Momento dipolar permanente

- El momento dipolar permanente es lo que permite emitir o absorber en rotación pura.
- El momento dipolar permanente `μ` mide la separación de carga de la molécula (en Debye).

💡 **Cómo se explica en la clase [B62-C01](../programa/clases/B62/B62-C01-espectros-rotacionales-de-moleculas-niveles-y-reglas-de-seleccion/CLASE.md):**
- No tiene momento dipolar permanente; la regla de selección dipolar exige uno (8.2).
- 🎯 **Por qué importa:** Una línea de CO a 115,27 GHz no es un dato aislado: es la consecuencia de un momento de inercia. Si entiendes de dónde sale, puedes predecir líneas que nadie ha medido y reconocer cuándo una línea observada no es del CO.

📘 **Dónde se aprende** (2 clases): [B62-C01 · Espectros rotacionales de moléculas: niveles y reglas de selección](../programa/clases/B62/B62-C01-espectros-rotacionales-de-moleculas-niveles-y-reglas-de-seleccion/CLASE.md); [B62-C04 · Momentos dipolares y fuerza de línea](../programa/clases/B62/B62-C04-momentos-dipolares-y-fuerza-de-linea/CLASE.md).

### Momento lineal

- El momento lineal (cantidad de movimiento) de un cuerpo es `p = m v`, vector en `kg·m/s`.

💡 **Cómo se explica en la clase [B05-C08](../programa/clases/B05/B05-C08-momento-lineal-e-impulsos/CLASE.md):**
- Definir momento lineal e impulso y relacionarlos con `ΣF = m a`.
- python programa/clases/B05/B05-C08-momento-lineal-e-impulsos/cohete_y_momento.py
- 🎯 **Por qué importa:** Un cohete en el vacío no tiene nada contra lo que empujar y aun así acelera. La pregunta motivadora es: ¿cómo cambia la velocidad de un cuerpo cuando expulsa masa o cuando choca, si no hay fuerzas externas?

📘 **Dónde se aprende** (1 clase): [B05-C08 · Momento lineal e impulsos](../programa/clases/B05/B05-C08-momento-lineal-e-impulsos/CLASE.md).

### Momento magnético

- El momento magnético `m = M V` es la magnetización por el volumen.
- El momento magnético `μ = mv_⊥²/(2B)` se conserva.

💡 **Cómo se explica en la clase [B30-C06](../programa/clases/B30/B30-C06-particulas-cargadas-y-movimientos/CLASE.md):**
- *Descripción textual:* la fuerza de Lorentz integrada con Boris da el giro, la deriva y el rebote en el espejo, con el momento magnético conservado.
- 🎯 **Por qué importa:** El movimiento de las partículas explica cómo se atrapan en los cinturones, cómo derivan y cómo se aceleran. La decisión central: ¿cuándo queda atrapada una partícula y cuánto vale su radio de giro?

📘 **Dónde se aprende** (2 clases): [B30-C06 · Partículas cargadas y movimientos](../programa/clases/B30/B30-C06-particulas-cargadas-y-movimientos/CLASE.md); [B65-C03 · Magnetismo cortical remanente y anomalías magnéticas](../programa/clases/B65/B65-C03-magnetismo-cortical-remanente-y-anomalias-magneticas/CLASE.md).

### Momento relativista

- El momento relativista es `p = γmv`.

💡 **Cómo se explica en la clase [B26-C05](../programa/clases/B26/B26-C05-equivalencia-entre-masa-y-energia/CLASE.md):**
- Ejercicio 12 · integrador. Elabora tu *balance de energía relativista*: tabla de energía, momento y energía cinética de un protón a cuatro velocidades, la comprobación de la relación energía–momento, el balance de GW150914 y una reflexión sobre por qué `v = c` es inalcanzable.
- 🎯 **Por qué importa:** El Sol, un acelerador de partículas y la fusión de dos agujeros negros son balances de masa y energía. Para calcularlos hay que saber cuánta energía tiene una partícula en reposo y en movimiento, y por qué no puede acelerarse hasta `c`.

📘 **Dónde se aprende** (1 clase): [B26-C05 · Equivalencia entre masa y energía](../programa/clases/B26/B26-C05-equivalencia-entre-masa-y-energia/CLASE.md).

### Momento saturado

- El momento saturado es el límite `h_max = I_w Ω_max` de una rueda.

🎯 **Por qué importa (clase B16-C18):** Una rueda de reacción entrega un par máximo y almacena un momento angular máximo (el Hubble usa ruedas de hasta unas 3000 rpm, y magnetopares para gestionar su velocidad, S1). Cuando el controlador pide más de lo que el actuador puede dar, el lazo deja de comportarse como se diseñó.

📘 **Dónde se aprende** (1 clase): [B16-C18 · Saturación y anti-windup](../programa/clases/B16/B16-C18-saturacion-y-anti-windup/CLASE.md).

### Momento sísmico

- El momento sísmico `M0 = μ A D` mide el tamaño del terremoto (N·m).

💡 **Cómo se explica en la clase [B57-C17](../programa/clases/B57/B57-C17-terremotos-y-deformacion/CLASE.md):**
- Una zona de subducción acumula deformación lentamente y la libera de golpe: el momento sísmico es cuánta regla se rompió, la magnitud es su logaritmo.
- Calcular el momento sísmico desde la magnitud y recuperarla (ida y vuelta).
- 🎯 **Por qué importa:** Medir la deformación permite saber cuánto deslizó la falla y cuánta tensión queda. La decisión central: ¿cómo se pasa de un número de magnitud al deslizamiento y a la deformación que verá un satélite?

📘 **Dónde se aprende** (1 clase): [B57-C17 · Terremotos y deformación](../programa/clases/B57/B57-C17-terremotos-y-deformacion/CLASE.md).

### Momento total

- El momento total `H` se verifica con `ΔH = ∫τ_ext dt`.

💡 **Cómo se explica en la clase [B87-C20](../programa/clases/B87/B87-C20-simulacion-adcs-integral/CLASE.md):**
- *Descripción textual:* la dinámica genera las medidas; el filtro estima la actitud; el control calcula el par de las ruedas; y, aparte, el balance de momento total comprueba que la integración es coherente.
- 🎯 **Por qué importa:** Cada pieza funciona sola; juntas pueden interactuar (el ruido del estimador entra al control, el control mueve la actitud que mide el sensor). La decisión central: ¿qué apuntamiento real se logra con el lazo completo y cómo se sabe que la simulación es coherente?

📘 **Dónde se aprende** (1 clase): [B87-C20 · Simulación ADCS integral](../programa/clases/B87/B87-C20-simulacion-adcs-integral/CLASE.md).

### Momentos principales

- Los ejes principales de un tensor de inercia son sus autovectores; los momentos principales, sus autovalores.

💡 **Cómo se explica en la clase [B10-C08](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md):**
- Los tres momentos principales son `95,858`, `124,142` y `150 kg m²`.
- Los autovalores serán los momentos principales de inercia y los autovectores, los ejes principales.
- 🎯 **Por qué importa:** Un satélite que rota libremente no gira igual alrededor de cualquier eje: tiene tres ejes especiales —los ejes principales de inercia— en los que la rotación es simple. Conocerlos permite diseñar su estabilización, decidir dónde colocar instrumentos sensibles al giro y entender por qué ciertos giros se desestabilizan.

📘 **Dónde se aprende** (1 clase): [B10-C08 · Autovalores y autovectores](../programa/clases/B10/B10-C08-autovalores-y-autovectores/CLASE.md).

### Momios

- Los momios (*odds*) son `P/(1 − P)`.

💡 **Cómo se explica en la clase [B63-C06](../programa/clases/B63/B63-C06-evaluacion-de-riesgos-biologicos-de-muestras-marcos-de-decision/CLASE.md):**
- En forma de momios, cada negativo multiplica los momios por `(1 − s)/e = 0,10/0,95 = 0,1053`.
- La forma de momios coincide con la fórmula directa a menos de `10⁻¹²`.
- 🎯 **Por qué importa:** Ninguna prueba demuestra que no hay peligro; solo reduce la incertidumbre. La decisión central: ¿cuántas pruebas negativas hacen falta antes de que liberar sea preferible a retener, y de qué dependen?

📘 **Dónde se aprende** (1 clase): [B63-C06 · Evaluación de riesgos biológicos de muestras: marcos de decisión](../programa/clases/B63/B63-C06-evaluacion-de-riesgos-biologicos-de-muestras-marcos-de-decision/CLASE.md).

### Moneda del reclamante

- La moneda del reclamante es la de pago por defecto según el artículo XIII, según el resumen consultado.

💡 **Cómo se explica en la clase [B123-C01](../programa/clases/B123/B123-C01-prueba-del-dano-y-cuantificacion-de-la-reparacion/CLASE.md):**
- Según el resumen leído del artículo XIII, el pago se hace en la moneda del reclamante salvo acuerdo distinto o petición de la moneda del Estado de lanzamiento.
- *Descripción textual:* del hecho dañoso salen las partidas con sus pruebas y el plazo de un año; las partidas dan la cuantía ponderada y su incertidumbre; la cuantía se convierte a la moneda del reclamante.
- 🎯 **Por qué importa:** Un Estado puede tener derecho a reclamar y aun así perder o cobrar poco si no demuestra el daño o no lo cuantifica de forma defendible. La decisión central: ¿qué partidas puedo sostener con pruebas, por cuánto, en qué moneda y con qué margen de error?

📘 **Dónde se aprende** (1 clase): [B123-C01 · Prueba del daño y cuantificación de la reparación](../programa/clases/B123/B123-C01-prueba-del-dano-y-cuantificacion-de-la-reparacion/CLASE.md).

### Monitor

- El monitor compara una medida con un límite.

💡 **Cómo se explica en la clase [B88-C12](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md):**
- Construir una tabla monitor→acción con su persistencia.
- Ejercicio 7 · autónomo. ¿Qué acción asignarías al monitor de tensión baja y por qué `N = 1`?
- 🎯 **Por qué importa:** Un monitor demasiado sensible dispara respuestas innecesarias; uno demasiado lento deja crecer el fallo. La decisión central: ¿qué persistencia equilibra las falsas alarmas y el tiempo de detección?

📘 **Dónde se aprende** (1 clase): [B88-C12 · Detección aislamiento y recuperación de fallos](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md).

### Monoabastecimiento

- El monoabastecimiento es depender de un solo proveedor por componente.

💡 **Cómo se explica en la clase [B122-C01](../programa/clases/B122/B122-C01-dependencias-de-proveedores-y-cadena-de-suministro-de-infraestructura-espacial/CLASE.md):**
- En monoabastecimiento cada componente depende de su primer proveedor.
- Paso 2 · Proveedores principales. P1 y P2 (monoabastecimiento).
- 🎯 **Por qué importa:** B119-C16 solo introduce la infraestructura crítica y no analiza de quién depende. La decisión central: ¿qué proveedor, si cae, daña más servicios, y cuánto baja el riesgo si hay una segunda fuente?

📘 **Dónde se aprende** (1 clase): [B122-C01 · Dependencias de proveedores y cadena de suministro de infraestructura espacial](../programa/clases/B122/B122-C01-dependencias-de-proveedores-y-cadena-de-suministro-de-infraestructura-espacial/CLASE.md).

### Monocapa

- Una monocapa es la cantidad de moléculas que cubre una superficie con una capa (aquí 10¹⁵ cm⁻², ilustrativo).
- La monocapa (ML) es la capacidad de la superficie en cm⁻³ de gas.

💡 **Cómo se explica en la clase [B47-C12](../programa/clases/B47/B47-C12-optica-en-ambientes-de-vacio/CLASE.md):**
- A `10⁻⁶ Pa` el camino libre medio es de `6651 m`; un contaminante de 100 u a `10⁻⁸ Pa` forma una monocapa en `0,75 días`.
- Ejercicio 4. Tiempo de monocapa en días.
- ⚠️ **Error frecuente:** Confundir monocapa con película de 100 nm. Se corrige con 8.3.
- 🎯 **Por qué importa:** La contaminación reduce la reflectancia y la transmisión sin aviso. La decisión central: ¿cuánto tarda en cubrirse una superficie y cuánto cambia la reflectancia por una película?

📘 **Dónde se aprende** (3 clases): [B47-C12 · Óptica en ambientes de vacío](../programa/clases/B47/B47-C12-optica-en-ambientes-de-vacio/CLASE.md); [B55-C06 · Hielos astrofísicos](../programa/clases/B55/B55-C06-hielos-astrofisicos/CLASE.md); [B60-C04 · Balance químico gas-grano: modelos de tres fases](../programa/clases/B60/B60-C04-balance-quimico-gas-grano-modelos-de-tres-fases/CLASE.md).

### Monodromia

- La monodromia `M` y el índice de estabilidad `ν = (λ + 1/λ)/2` miden el crecimiento del error por revolución.

💡 **Cómo se explica en la clase [B76-C05](../programa/clases/B76/B76-C05-orbitas-nrho/CLASE.md):**
- *Descripción textual:* se propaga la semilla hasta el segundo cruce de `y = 0`, se mide el residuo de `vx` y `vz`, Newton corrige `x0` y `vy0` hasta anularlo y con la órbita cerrada se calcula la monodromia.
- Paso 1 · Monodromia. Se propaga cada columna de la perturbación un periodo.
- 🎯 **Por qué importa:** La NRHO es la órbita de referencia publicada para la estación Gateway. La decisión central: ¿cómo se calcula una órbita periódica inestable y qué tan cerca queda un modelo simple de la referencia en un modelo de efemérides?

📘 **Dónde se aprende** (1 clase): [B76-C05 · Órbitas NRHO](../programa/clases/B76/B76-C05-orbitas-nrho/CLASE.md).

### Monodromia plana

- La monodromia plana `M` es la matriz `4 × 4` del estado `(x, y, vx, vy)`.

💡 **Cómo se explica en la clase [B76-C06](../programa/clases/B76/B76-C06-orbitas-dro-dinamica-cislunar-y-operaciones-de-proximidad/CLASE.md):**
- Calcular la monodromia plana y evaluar la estabilidad.
- 🎯 **Por qué importa:** La NRHO es inestable y exige mantenimiento; la DRO es estable. La decisión central: ¿qué se gana y qué se paga al elegir una órbita estable y lejana frente a una NRHO cercana?

📘 **Dónde se aprende** (1 clase): [B76-C06 · Órbitas DRO — Dinámica cislunar y operaciones de proximidad](../programa/clases/B76/B76-C06-orbitas-dro-dinamica-cislunar-y-operaciones-de-proximidad/CLASE.md).

### Monómero

- Un monómero es la unidad; un oligómero, una cadena corta de monómeros.

💡 **Cómo se explica en la clase [B56-C21](../programa/clases/B56/B56-C21-polimerizacion-prebiotica-experimental-oligomeros-y-condiciones-de-laboratorio/CLASE.md):**
- Una simulación de `200 000` monómeros (semilla 31415) da `0,1166; 0,1060; 0,0696; 0,0392` para esos `n` (todas a menos de 0,01 de la fórmula) y una longitud media de `8,446` frente a `8,500` (0,6 %).
- Ejemplo conductor sintético: monómeros con eficiencia de enlace `e = 0,30` por ciclo.
- 🎯 **Por qué importa:** C03 trata el origen de autorreplicantes, pero ninguna clase trata la polimerización experimental y sus límites. Antes de que un replicador pueda copiarse, hay que formar cadenas lo bastante largas.

📘 **Dónde se aprende** (1 clase): [B56-C21 · Polimerización prebiótica experimental: oligómeros y condiciones de laboratorio](../programa/clases/B56/B56-C21-polimerizacion-prebiotica-experimental-oligomeros-y-condiciones-de-laboratorio/CLASE.md).

### Monopolo

- El monopolo es la mitad de un dipolo sobre un plano de tierra.
- El monopolo es el término `−GM/r`.

💡 **Cómo se explica en la clase [B49-C01](../programa/clases/B49/B49-C01-antenas-de-hilo-dipolo-monopolo-e-impedancia-de-radiacion/CLASE.md):**
- El monopolo sobre plano perfecto tiene `36,5395 Ω` y la directividad doble (`3,2818`), porque la misma potencia sale por medio espacio.
- El dipolo de media onda mide `0,99931 m`, tiene `R = 73,079 Ω` y `D = 1,6409` (2,151 dBi); el monopolo de cuarto de onda mide `0,49965 m`, tiene `36,540 Ω` y `D = 3,2818` (5,161 dBi).
- ⚠️ **Error frecuente:** Olvidar el plano de tierra del monopolo. Se corrige con 8.3.
- 🎯 **Por qué importa:** Sin la resistencia de radiación no se sabe qué carga ve la línea ni cuánta potencia se irradia. La decisión central: ¿de qué longitud hacer el hilo y qué impedancia presentará a la línea?

📘 **Dónde se aprende** (2 clases): [B49-C01 · Antenas de hilo: dipolo, monopolo e impedancia de radiación](../programa/clases/B49/B49-C01-antenas-de-hilo-dipolo-monopolo-e-impedancia-de-radiacion/CLASE.md); [B53-C03 · Campo gravitatorio planetario](../programa/clases/B53/B53-C03-campo-gravitatorio-planetario/CLASE.md).

### Monopolo de cuarto de onda

- Un monopolo de cuarto de onda mide `k λ/4`, con `k` el factor de acortamiento.

💡 **Cómo se explica en la clase [B95-C04](../programa/clases/B95/B95-C04-antenas-desplegables-para-satelites-pequenos/CLASE.md):**
- Calcular la longitud de un monopolo de cuarto de onda con factor de acortamiento.
- Referencia teorica: dipolo de media onda 2.15 dBi ; monopolo de cuarto de onda sobre plano ideal 5.15 dBi (modelo ideal, no medido)
- 🎯 **Por qué importa:** Un enlace con la Tierra necesita una antena, y una antena que no se despliega deja el satélite mudo. La decisión central: ¿qué longitud necesita la antena, cómo se pliega sin dañarla y qué riesgo añade el mecanismo?

📘 **Dónde se aprende** (1 clase): [B95-C04 · Antenas desplegables para satélites pequeños](../programa/clases/B95/B95-C04-antenas-desplegables-para-satelites-pequenos/CLASE.md).

### Monopropelente

- Un monopropelente es un líquido que se descompone en gas caliente por catálisis.

💡 **Cómo se explica en la clase [B78-C04](../programa/clases/B78/B78-C04-propulsion-monopropelente-conceptual/CLASE.md):**
- El script [monopropelente.py](monopropelente.py) calcula productos, temperatura, masa molar y escape para `a` de 0 a 1 (comprueba el balance de átomos de N y H para cada `a`, la conservación de la masa y los límites `a = 0` y `a = 1` a mano).
- Monopropelente ILUSTRATIVO (modelo de hidracina; valores de manual no consultados)
- 🎯 **Por qué importa:** La descomposición de un monopropelente tiene dos pasos: uno que libera calor y otro que lo absorbe. La decisión central: ¿conviene que el amoníaco intermedio se disocie del todo, por la menor masa molar, o que se conserve, por la mayor temperatura?

📘 **Dónde se aprende** (1 clase): [B78-C04 · Propulsión monopropelente conceptual](../programa/clases/B78/B78-C04-propulsion-monopropelente-conceptual/CLASE.md).

### Monótona en luminancia

- Una escala es monótona en luminancia si la luminancia no desciende al subir el valor.

💡 **Cómo se explica en la clase [B130-C02](../programa/clases/B130/B130-C02-visualizacion-de-datos-para-comunicar/CLASE.md):**
- Comprobar si una escala de color es monótona en luminancia.
- Su luminancia no es monótona: dos valores distintos pueden salir igual de oscuros o el mayor más oscuro.
- 🎯 **Por qué importa:** Elegir un gráfico honesto para el público es una competencia propia. La decisión central: ¿qué diseño muestra la diferencia que existe en los datos, ni más ni menos, y la puede leer cualquier persona?

📘 **Dónde se aprende** (1 clase): [B130-C02 · Visualización de datos para comunicar](../programa/clases/B130/B130-C02-visualizacion-de-datos-para-comunicar/CLASE.md).

### Monotonía

- La monotonía pide `b ≤ c ⇒ a+b ≤ a+c`.
- Referencia independiente: otra implementación de la misma política. Monotonía: propiedad de orden.

💡 **Cómo se explica en la clase [B88-C36](../programa/clases/B88/B88-C36-codificacion-defensiva-y-estandares-de-codigo-seguro/CLASE.md):**
- En 100 000 casos: rango fuera `0`, monotonía rota `0`, no conmutativa `0`.
- La suma envolvente rompe la monotonía en `25 314` casos (`25,3 %`).
- 🎯 **Por qué importa:** Un desbordamiento silencioso convierte 35 000 en −30 536 y un comando de giro positivo en negativo. La decisión central: ¿qué operaciones aceptan cualquier entrada y devuelven siempre un resultado dentro del rango?

📘 **Dónde se aprende** (2 clases): [B88-C36 · Codificación defensiva y estándares de código seguro](../programa/clases/B88/B88-C36-codificacion-defensiva-y-estandares-de-codigo-seguro/CLASE.md); [B96-C07 · Telecomandos y autorizaciones](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md).

### Monte Carlo

- Una Monte Carlo es una simulación con muestras aleatorias para estimar una distribución.
- La propagación lineal de la covarianza es `P(t) = Φ P₀ Φᵀ`. Monte Carlo propaga muestras.
- La RSS es `√Σtᵢ²`. Monte Carlo muestrea cada dimensión.
- *(y 15 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B10-C19](../programa/clases/B10/B10-C19-jacobianos-y-linealizacion/CLASE.md):**
- No: `r cos(el)` vale `1,75 km`, el jacobiano casi pierde rango (azimut mal definido) y la distribución no es gaussiana; usar Monte Carlo o otra parametrización (8.5).
- Ejercicio 12 · integrador. Elabora tu informe de linealización: una función de tres entradas y tres salidas, su jacobiano analítico verificado con diferencias finitas, la tabla de error de linealización para tres pasos, la propagación de covarianza contrastada con Monte Carlo y los casos en que falla.
- 🎯 **Por qué importa:** Una estación mide la distancia, el azimut y la elevación de un objeto con incertidumbres. Para decir dónde está en coordenadas cartesianas y cuánta incertidumbre tiene esa posición, hay que transformar los números y sus errores.

📘 **Dónde se aprende** (18 clases): [B10-C19 · Jacobianos y linealización](../programa/clases/B10/B10-C19-jacobianos-y-linealizacion/CLASE.md); [B16-C19 · Verificación de lazo cerrado](../programa/clases/B16/B16-C19-verificacion-de-lazo-cerrado/CLASE.md); [B26-C12 · Escalas de distancia cosmológicas](../programa/clases/B26/B26-C12-escalas-de-distancia-cosmologicas/CLASE.md); [B30-C03 · Ciclo de actividad solar](../programa/clases/B30/B30-C03-ciclo-de-actividad-solar/CLASE.md); [B58-C08 · Propagación de incertidumbre orbital](../programa/clases/B58/B58-C08-propagacion-de-incertidumbre-orbital/CLASE.md); [B74-C12 · Propagación de incertidumbre — Estimación de órbitas y navegación espacial](../programa/clases/B74/B74-C12-propagacion-de-incertidumbre-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md) y 12 más.

### Montura

- Una montura sostiene el telescopio y permite apuntarlo.

💡 **Cómo se explica en la clase [B08-C15](../programa/clases/B08/B08-C15-monturas-y-seguimiento-inicial/CLASE.md):**
- Un objeto a 85° de altura y acimut 100° pide `+12,8″/s` en altura y `+18,3″/s` en acimut; cerca del cenit, `tan h` crece sin límite y el acimut debe cambiar muy rápido: la montura altacimutal pierde el objeto («agujero del cenit»).
- Para un grupo, un motor sidéreo facilita compartir el objeto; para las personas con poca fuerza, una montura equilibrada y una barra de empuje ayudan.
- ⚠️ **Error frecuente:** Creer que cualquier montura sigue bien cerca del cenit. Ejercicio 7.
- 🎯 **Por qué importa:** A 120 aumentos, un planeta cruza el ocular en menos de dos minutos y tienes que empujar el tubo constantemente. La pregunta motivadora: ¿qué montura necesito y qué error puedo tolerar al seguir un objeto?

📘 **Dónde se aprende** (1 clase): [B08-C15 · Monturas y seguimiento inicial](../programa/clases/B08/B08-C15-monturas-y-seguimiento-inicial/CLASE.md).

### Montura altacimutal

- Una montura altacimutal mueve el telescopio en altitud y azimut.

🎯 **Por qué importa (clase B09-C05):** Un telescopio con montura altacimutal apunta con dos ejes: altitud y azimut. Para mantener una estrella en el centro del campo, cada eje debe girar a una velocidad que cambia con el tiempo.

📘 **Dónde se aprende** (1 clase): [B09-C05 · Derivadas trigonométricas](../programa/clases/B09/B09-C05-derivadas-trigonometricas/CLASE.md).

### Montura altazimutal

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C18):** La montura decide cuánto tiempo se puede exponer. La decisión central: ¿altazimutal o ecuatorial y qué exposición máxima sin guiado?

📘 **Dónde se aprende** (1 clase): [B41-C18 · Monturas y mecanismos de seguimiento](../programa/clases/B41/B41-C18-monturas-y-mecanismos-de-seguimiento/CLASE.md).

### Montura Dobson

- La montura Dobson (altazimutal sin motor).

🎯 **Por qué importa (clase B41-C16):** El Newton es el reflector más simple y el Dobson su montura más barata. La decisión central: ¿qué tamaño de plano y qué ocular conviene?

📘 **Dónde se aprende** (1 clase): [B41-C16 · Telescopios Newton y Dobson](../programa/clases/B41/B41-C16-telescopios-newton-y-dobson/CLASE.md).

### Montura ecuatorial

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C18):** La montura decide cuánto tiempo se puede exponer. La decisión central: ¿altazimutal o ecuatorial y qué exposición máxima sin guiado?

📖 **Explicado a fondo:** [Montura ecuatorial](esencial/tercera-f-t.md#montura-ecuatorial) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B41-C18 · Monturas y mecanismos de seguimiento](../programa/clases/B41/B41-C18-monturas-y-mecanismos-de-seguimiento/CLASE.md).

### Moteado

- El moteado hace que cada pulso sea ruidoso; se reduce promediando pulsos.

💡 **Cómo se explica en la clase [B57-C09](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md):**
- La razón de errores entre 25 y 100 pulsos es `1,98`, cercana a `√4 = 2`: el promedio de pulsos con moteado independiente reduce el error como `1/√N`.
- El script [altimetria.py](altimetria.py) calcula la relación entre tiempo y distancia, ajusta el instante de subida de un eco sintético con moteado y mide el error (comprueba que el sesgo es compatible con cero a 4 errores estándar y la razón entre errores con 25 y 100 pulsos entre 1,6 y 2,4).
- 🎯 **Por qué importa:** La altura del mar cambia unos milímetros por año, pero el eco de un pulso es ruidoso. La decisión central: ¿cuántos pulsos hay que promediar y cómo se ajusta el eco para que el error de distancia del ajuste se reduzca lo necesario?

📘 **Dónde se aprende** (1 clase): [B57-C09 · Altimetría satelital](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md).

### Motorizada

- Una montura motorizada o con GoTo apunta y sigue con motores;

💡 **Cómo se explica en la clase [B08-C15](../programa/clases/B08/B08-C15-monturas-y-seguimiento-inicial/CLASE.md):**
- Un motor sidéreo en una ecuatorial alineada da seguimiento continuo; en una altacimutal motorizada, el sistema calcula dos movimientos.
- 🎯 **Por qué importa:** A 120 aumentos, un planeta cruza el ocular en menos de dos minutos y tienes que empujar el tubo constantemente. La pregunta motivadora: ¿qué montura necesito y qué error puedo tolerar al seguir un objeto?

📘 **Dónde se aprende** (1 clase): [B08-C15 · Monturas y seguimiento inicial](../programa/clases/B08/B08-C15-monturas-y-seguimiento-inicial/CLASE.md).

### Mover y esperar

- Mover y esperar es mandar un movimiento, esperar la confirmación y seguir.
- En mover y esperar el operador envía una orden corta, espera su efecto (`2t` más proceso) y decide la siguiente.
- Ganancia `K`: velocidad ordenada por metro de error (1/s). Mover y esperar: pasos cortos con espera de la imagen.

💡 **Cómo se explica en la clase [B98-C03](../programa/clases/B98/B98-C03-control-supervisado-y-autonomia-compartida/CLASE.md):**
- Sin retardo, «mover y esperar» (pasos de 1 m, `v = 0,04 m/s`, 30 s de decisión por orden) tarda 1,53 h y el control supervisado (metas de 10 m, `v = 0,02 m/s`, 120 s por meta) 1,72 h: gana el manual.
- Calcular el tiempo de una tarea con «mover y esperar».
- 🎯 **Por qué importa:** Ni siempre conviene más autonomía ni siempre más control manual: sin retardo, el manual puede ser más rápido. La decisión central: ¿a partir de qué retardo compensa pasar de órdenes cortas a metas supervisadas, y qué se pierde al hacerlo?

📘 **Dónde se aprende** (3 clases): [B98-C03 · Control supervisado y autonomía compartida](../programa/clases/B98/B98-C03-control-supervisado-y-autonomia-compartida/CLASE.md); [B101-C10 · Simulación de una tarea tripulada con manipulador](../programa/clases/B101/B101-C10-simulacion-de-una-tarea-tripulada-con-manipulador/CLASE.md); [B104-C12 · Robótica tripulada](../programa/clases/B104/B104-C12-robotica-tripulada/CLASE.md).

### Movimiento armónico simple (MAS)

- El movimiento armónico simple (MAS) es el que sigue `x(t) = A cos(ω t + φ)`.

🎯 **Por qué importa (clase B05-C11):** Una estructura que vibra puede amplificar una excitación hasta romperse; un reloj de péndulo mide tiempo; un átomo vibra en un cristal. La pregunta motivadora es: ¿qué determina la frecuencia a la que algo oscila y qué pasa cuando se le empuja a esa frecuencia?

📘 **Dónde se aprende** (1 clase): [B05-C11 · Movimiento oscilatorio](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md).

### Movimiento circular uniforme (MCU)

- El movimiento circular uniforme (MCU) recorre una circunferencia con rapidez constante.

🎯 **Por qué importa (clase B05-C03):** Un cohete que enciende su motor un tiempo corto y un satélite que da vueltas son, a primera aproximación, estos dos movimientos. La pregunta motivadora es: ¿qué fórmulas valen cuando la aceleración es constante o cuando la rapidez es constante en un círculo, y hasta dónde son confiables?

📘 **Dónde se aprende** (1 clase): [B05-C03 · Movimiento rectilíneo y circular](../programa/clases/B05/B05-C03-movimiento-rectilineo-y-circular/CLASE.md).

### Movimiento medio

- El movimiento medio `n` es la velocidad angular promedio de la órbita (rad/d).
- El movimiento medio `n = 2π/P` es la velocidad angular media.
- El movimiento medio es `n = √(μ/a³)`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C06](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md):**
- Movimiento medio n = 1.990976e-07 rad/s -> periodo 365.258 d
- 🎯 **Por qué importa:** Para saber dónde está un planeta en su órbita en un instante dado hay que resolver la ecuación de Kepler, `M = E − e sin E`, que no tiene solución en funciones elementales: no se puede despejar `E`.

📘 **Dónde se aprende** (6 clases): [B09-C06 · Derivación implícita](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md); [B23-C03 · Casos analíticos de validación](../programa/clases/B23/B23-C03-casos-analiticos-de-validacion/CLASE.md); [B52-C07 · Resonancias orbitales](../programa/clases/B52/B52-C07-resonancias-orbitales/CLASE.md); [B71-C13 · Anomalías orbitales](../programa/clases/B71/B71-C13-anomalias-orbitales/CLASE.md); [B74-C29 · Formatos TLE y OMM de elementos orbitales](../programa/clases/B74/B74-C29-formatos-tle-y-omm-de-elementos-orbitales/CLASE.md); [B75-C02 · Ángulos de fase planetaria](../programa/clases/B75/B75-C02-angulos-de-fase-planetaria/CLASE.md).

### Movimiento medio de Kozai

- El movimiento medio de Kozai es el publicado; el de Brouwer es el de la teoría.

💡 **Cómo se explica en la clase [B72-C21](../programa/clases/B72/B72-C21-propagador-sgp4-y-teoria-general-de-perturbaciones/CLASE.md):**
- Convertir el movimiento medio de Kozai (publicado) a Brouwer con la inicialización de SGP4.
- ⚠️ **Error frecuente:** Confundir el movimiento medio de Kozai con el de Brouwer. Se corrige con 8.2.
- 🎯 **Por qué importa:** Un error clásico es tomar los elementos de dos líneas como elementos keplerianos y propagarlos con dos cuerpos: el error es de kilómetros en minutos. La decisión central: ¿qué propagador corresponde a un conjunto de elementos y qué transformaciones previas exige antes de usarlo?

📘 **Dónde se aprende** (1 clase): [B72-C21 · Propagador SGP4 y teoría general de perturbaciones](../programa/clases/B72/B72-C21-propagador-sgp4-y-teoria-general-de-perturbaciones/CLASE.md).

### Movimiento polar

- El movimiento polar `(x_p, y_p)` es el movimiento del CIP respecto de la corteza; está dominado por el bamboleo de Chandler (periodo de unos `435 d`) y una componente anual (S1, glosario y cap. 5).

💡 **Cómo se explica en la clase [B13-C22](../programa/clases/B13/B13-C22-parametros-de-orientacion-terrestre-precesion-nutacion-ut1-y-movimiento-polar/CLASE.md):**
- Por eso la geodesia espacial y la navegación de espacio profundo exigen EOP publicados a diario; la predicción de UT1 y de movimiento polar se degrada con el tiempo y para operaciones se usan los productos vigentes (C09, C19).
- I["[ITRS]<br/>(ligado a la corteza)"] -->|"W(t): movimiento polar<br/>x_p, y_p"| T["TIRS"]
- ⚠️ **Error frecuente:** Despreciar el movimiento polar por «pequeño». Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Una estación terrestre apunta a una nave en el sistema celeste. Para ello debe saber cuánto ha girado la Tierra, hacia dónde apunta su eje en el cielo y dónde está ese eje dentro de la corteza.

📘 **Dónde se aprende** (1 clase): [B13-C22 · Parámetros de orientación terrestre: precesión, nutación, UT1 y movimiento polar](../programa/clases/B13/B13-C22-parametros-de-orientacion-terrestre-precesion-nutacion-ut1-y-movimiento-polar/CLASE.md).

### Movimiento propio

- El movimiento propio `μ` en mas/año.

💡 **Cómo se explica en la clase [B29-C04](../programa/clases/B29/B29-C04-astrometria-de-exoplanetas/CLASE.md):**
- El Monte Carlo reproduce la covarianza al `1 %`; el paralaje, el movimiento propio y la órbita se separan porque sus funciones base son casi ortogonales.
- La estrella se desplaza en línea recta (movimiento propio), oscila anualmente por el movimiento de la Tierra (paralaje) y, además, traza una pequeña elipse por el planeta.
- 🎯 **Por qué importa:** La astrometría mide la inclinación y la masa verdadera, pero la señal es diminuta. La decisión central: ¿cuál es la firma de un planeta a una distancia dada y con qué incertidumbre se recupera su órbita junto al paralaje y el movimiento propio?

📖 **Explicado a fondo:** [Movimiento propio](esencial/esencial-m-z.md#movimiento-propio) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B29-C04 · Astrometría de exoplanetas](../programa/clases/B29/B29-C04-astrometria-de-exoplanetas/CLASE.md); [B38-C03 · Cinemática estelar con Gaia: movimientos propios y espacio de fase](../programa/clases/B38/B38-C03-cinematica-estelar-con-gaia-movimientos-propios-y-espacio-de-fase/CLASE.md).

### Movimiento rectilíneo uniforme (MRU)

- El movimiento rectilíneo uniforme (MRU) tiene velocidad constante y aceleración cero.

🎯 **Por qué importa (clase B05-C03):** Un cohete que enciende su motor un tiempo corto y un satélite que da vueltas son, a primera aproximación, estos dos movimientos. La pregunta motivadora es: ¿qué fórmulas valen cuando la aceleración es constante o cuando la rapidez es constante en un círculo, y hasta dónde son confiables?

📘 **Dónde se aprende** (1 clase): [B05-C03 · Movimiento rectilíneo y circular](../programa/clases/B05/B05-C03-movimiento-rectilineo-y-circular/CLASE.md).

### Movimiento rectilíneo uniformemente acelerado (MRUA)

- El movimiento rectilíneo uniformemente acelerado (MRUA) tiene aceleración constante.

🎯 **Por qué importa (clase B05-C03):** Un cohete que enciende su motor un tiempo corto y un satélite que da vueltas son, a primera aproximación, estos dos movimientos. La pregunta motivadora es: ¿qué fórmulas valen cuando la aceleración es constante o cuando la rapidez es constante en un círculo, y hasta dónde son confiables?

📘 **Dónde se aprende** (1 clase): [B05-C03 · Movimiento rectilíneo y circular](../programa/clases/B05/B05-C03-movimiento-rectilineo-y-circular/CLASE.md).

### Movimiento relativo

- El movimiento relativo es el de un cuerpo respecto al otro.
- El movimiento relativo es la posición del robot respecto del objetivo.
- El movimiento relativo describe la posición de un satélite respecto de otro.

💡 **Cómo se explica en la clase [B71-C03](../programa/clases/B71/B71-C03-ecuacion-de-movimiento-de-dos-cuerpos/CLASE.md):**
- Escribir la ecuación del movimiento relativo y el papel de `μ = G(m₁ + m₂)`.
- No: el baricentro queda fuera del cuerpo mayor y ambos orbitan en torno a él; hay que usar el movimiento relativo con `μ = G(m₁ + m₂)`.
- 🎯 **Por qué importa:** Casi toda la mecánica orbital parte de esta ecuación; entender qué supone (cuerpos puntuales, sin otras fuerzas) permite saber cuándo falla. La decisión central: ¿qué resuelve exactamente la ecuación de dos cuerpos y cómo compruebas que tu integración numérica es fiable?

📘 **Dónde se aprende** (3 clases): [B71-C03 · Ecuación de movimiento de dos cuerpos](../programa/clases/B71/B71-C03-ecuacion-de-movimiento-de-dos-cuerpos/CLASE.md); [B97-C11 · Robots de inspección orbital](../programa/clases/B97/B97-C11-robots-de-inspeccion-orbital/CLASE.md); [B119-C28 · Normas de comportamiento responsable en el espacio](../programa/clases/B119/B119-C28-normas-de-comportamiento-responsable-en-el-espacio/CLASE.md).

### Movimiento retrógrado

- El movimiento retrógrado es el retroceso aparente de un planeta entre las estrellas.

💡 **Cómo se explica en la clase [B02-C10](../programa/clases/B02/B02-C10-geocentrismo-y-heliocentrismo/CLASE.md):**
- Explicar el movimiento retrógrado en los dos modelos.
- 🎯 **Por qué importa:** La pregunta «¿se mueve la Tierra o el cielo?» se puede responder hoy en una línea, pero en 1500 una persona razonable podía defender cualquiera de las dos. La pregunta motivadora es: ¿con qué criterios se elige entre dos modelos que predicen casi lo mismo?

📘 **Dónde se aprende** (1 clase): [B02-C10 · Geocentrismo y heliocentrismo](../programa/clases/B02/B02-C10-geocentrismo-y-heliocentrismo/CLASE.md).

### Movimiento superlumínico aparente

- El movimiento superlumínico aparente es `β_app > 1`.

🎯 **Por qué importa (clase B27-C11):** Un chorro que se acerca puede parecer más rápido que la luz sin violar nada, y su brillo cambia en órdenes de magnitud según el ángulo. Sin estos efectos no se pueden comparar chorros ni inferir su velocidad.

📘 **Dónde se aprende** (1 clase): [B27-C11 · Chorros relativistas](../programa/clases/B27/B27-C11-chorros-relativistas/CLASE.md).

### MPC

- El MPC minimiza un costo sobre un horizonte `N` con un modelo.

💡 **Cómo se explica en la clase [B87-C21](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md):**
- El MPC lo respeta con una violación de `1,5 %` (restricción blanda); el PD lo excede en `11 %`.
- MPC con QP (esta clase): restricciones explícitas, mayor cómputo.
- ⚠️ **Error frecuente:** Creer que el MPC garantiza la restricción blanda. Revisa la violación residual (8.4)
- 🎯 **Por qué importa:** Un PD satura el par y no sabe de límites de velocidad: puede superar el máximo de la rueda o de la carga útil. La decisión central: ¿cómo formular un problema que respete par y velocidad, cuánto cuesta calcularlo y qué se gana?

📘 **Dónde se aprende** (1 clase): [B87-C21 · Control predictivo basado en modelo (MPC) para vehículos espaciales](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md).

### M/q

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C08](../programa/clases/B47/B47-C08-espectrometros-de-masas-orbitales/CLASE.md):**
- *Descripción textual:* el voltaje acelera los iones, el tiempo de vuelo codifica m/q y la dispersión de arranque fija la resolución.
- ion m/q [u] t formula [us] t energia [us]
- 🎯 **Por qué importa:** La resolución de masa decide qué especies se separan. La decisión central: ¿qué tiempo de vuelo, qué dispersión y qué resolución permiten distinguir dos iones casi isobáricos?

📘 **Dónde se aprende** (1 clase): [B47-C08 · Espectrómetros de masas orbitales](../programa/clases/B47/B47-C08-espectrometros-de-masas-orbitales/CLASE.md).

### MTBF

- El MTBF (o MTTF) es `1/λ` en el modelo exponencial.
- Cota superior de confianza: valor que, con probabilidad `CL`, no es inferior a la tasa verdadera. MTBF: tiempo medio entre fallas.
- La tasa de falla `λ` es la probabilidad de fallar por unidad de tiempo; el MTBF es `1/λ` con tasa constante.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B33-C09](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md):**
- M["MTBF, MTTR"] --> A["A = MTBF/(MTBF+MTTR)"]
- Ejercicio 5. `A` con MTBF = 2000 h y MTTR = 24 h.
- 🎯 **Por qué importa:** Una unidad adicional mejora menos que la anterior y las fallas comunes limitan la ganancia. La decisión central: ¿cuántas unidades de respaldo valen la pena?

📘 **Dónde se aprende** (6 clases): [B33-C09 · Planes de continuidad ante eventos de clima espacial](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md); [B48-C15 · Gestión de fallas de instrumentos](../programa/clases/B48/B48-C15-gestion-de-fallas-de-instrumentos/CLASE.md); [B86-C11 · Redundancia eléctrica](../programa/clases/B86/B86-C11-redundancia-electrica/CLASE.md); [B90-C17 · Gestión de anomalías de prueba](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md); [B93-C04 · Análisis de confiabilidad de electrónica (MTBF y derating)](../programa/clases/B93/B93-C04-analisis-de-confiabilidad-de-electronica-mtbf-y-derating/CLASE.md); [B122-C02 · Continuidad de servicio: impacto y objetivos de recuperación](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md).

### MTBF/MTTR

- MTBF/MTTR: tiempo medio entre fallas y de reparación.

💡 **Cómo se explica en la clase [B96-C23](../programa/clases/B96/B96-C23-continuidad-y-redundancia-de-las-operaciones-terrestres/CLASE.md):**
- Solo se leyó la parte inicial; no da MTBF ni MTTR.
- Calcular la disponibilidad `A = MTBF/(MTBF + MTTR)` de un componente.
- ⚠️ **Error frecuente:** Usar MTBF sin MTTR. Calcula `A` (8.2)
- 🎯 **Por qué importa:** Redundancia no es solo tener más estaciones: si comparten la causa de falla (red, energía, software) el beneficio desaparece. La decisión central: ¿cuántas estaciones y qué independencia hacen falta para que la probabilidad de perder un contacto sea aceptable?

📘 **Dónde se aprende** (1 clase): [B96-C23 · Continuidad y redundancia de las operaciones terrestres](../programa/clases/B96/B96-C23-continuidad-y-redundancia-de-las-operaciones-terrestres/CLASE.md).

### MTD

- El RTO es el tiempo objetivo para restablecer el servicio; el WRT es el tiempo adicional para recuperar el trabajo; el MTD es el tiempo máximo tolerable de interrupción.

💡 **Cómo se explica en la clase [B122-C02](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md):**
- Se esperan `(8760/724) e^(−8/4) = 1,637` cortes por año que superen el MTD.
- *Descripción textual:* desde el fallo corren el RTO y el WRT, cuya suma no debe pasar del MTD, mientras el costo crece; el RPO limita el intervalo entre copias.
- 🎯 **Por qué importa:** B96-C14 trata procedimientos y no enseña a fijar objetivos de recuperación a partir del impacto. La decisión central: ¿cuál debe ser el RTO para no superar el tiempo máximo tolerable y qué frecuencia de copias exige el RPO?

📘 **Dónde se aprende** (1 clase): [B122-C02 · Continuidad de servicio: impacto y objetivos de recuperación](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md).

### MTF

- La MTF mide el contraste conservado.
- La MTF: su módulo.

💡 **Cómo se explica en la clase [B42-C07](../programa/clases/B42/B42-C07-funcion-de-transferencia-optica/CLASE.md):**
- Si la PSF se toma cada 4 píxeles (1 por `λ/D`) la OTF medida suma `MTF(v) + MTF(1 − v)`:
- Paso 1 · Fórmula. `MTF = (2/π)[acos v − v√(1−v²)]`.
- 🎯 **Por qué importa:** La OTF dice qué detalles (frecuencias espaciales) pasan por el sistema y cuáles se pierden; fija el muestreo necesario del detector. La decisión central: ¿hasta qué frecuencia transmite el telescopio y qué muestreo exige?

📘 **Dónde se aprende** (2 clases): [B42-C07 · Función de transferencia óptica](../programa/clases/B42/B42-C07-funcion-de-transferencia-optica/CLASE.md); [B83-C17 · Verificación frente a validación](../programa/clases/B83/B83-C17-verificacion-frente-a-validacion/CLASE.md).

### MTTR

- El MTTR es el tiempo medio de reparación.
- El MTBF es el tiempo medio entre fallas y el MTTR el tiempo medio de reparación.
- El MTBF y el MTTR.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B33-C09](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md):**
- M["MTBF, MTTR"] --> A["A = MTBF/(MTBF+MTTR)"]
- Ejercicio 5. `A` con MTBF = 2000 h y MTTR = 24 h.
- 🎯 **Por qué importa:** Una unidad adicional mejora menos que la anterior y las fallas comunes limitan la ganancia. La decisión central: ¿cuántas unidades de respaldo valen la pena?

📘 **Dónde se aprende** (4 clases): [B33-C09 · Planes de continuidad ante eventos de clima espacial](../programa/clases/B33/B33-C09-planes-de-continuidad-ante-eventos-de-clima-espacial/CLASE.md); [B48-C15 · Gestión de fallas de instrumentos](../programa/clases/B48/B48-C15-gestion-de-fallas-de-instrumentos/CLASE.md); [B59-C18 · Fiabilidad de equipos mineros](../programa/clases/B59/B59-C18-fiabilidad-de-equipos-mineros/CLASE.md); [B122-C02 · Continuidad de servicio: impacto y objetivos de recuperación](../programa/clases/B122/B122-C02-continuidad-de-servicio-impacto-y-objetivos-de-recuperacion/CLASE.md).

### Mudo

- Un índice mudo (repetido) puede renombrarse; un índice libre aparece una vez por término y define la componente.

💡 **Cómo se explica en la clase [B10-C17](../programa/clases/B10/B10-C17-tensores-y-notacion-indicial/CLASE.md):**
- Leer y escribir expresiones con índices libres y mudos y la convención de suma.
- 🎯 **Por qué importa:** La inercia de un satélite frente a un giro depende de la dirección: se necesita nueve números ordenados en una matriz, y esos nueve números cambian si cambias los ejes del cuerpo, pero de forma que la física no cambie.

📘 **Dónde se aprende** (1 clase): [B10-C17 · Tensores y notación indicial](../programa/clases/B10/B10-C17-tensores-y-notacion-indicial/CLASE.md).

### Muerto

- Un mutante es una copia de la IUT con un defecto inyectado; está muerto si alguna prueba falla y sobrevive si todas pasan.
- El píxel caliente da más señal que el vecino; el muerto, menos o ninguna.
- Un mutante muerto hace fallar alguna prueba; uno vivo, no.

💡 **Cómo se explica en la clase [B44-C15](../programa/clases/B44/B44-C15-pixeles-defectuosos/CLASE.md):**
- En un cuadro de `64 × 64` con `30` calientes (+300 ADU) y `20` muertos (valor 0), la sigma robusta es `10,10 ADU` (verdadera `10`) frente a una desviación habitual de `75,07`.
- El script [defectuosos.py](defectuosos.py) detecta calientes y muertos con la MAD y los repara con la mediana de los vecinos (comprueba que se detectan los 50 y que hay menos de 3 falsos positivos).
- 🎯 **Por qué importa:** La media y la desviación habituales se distorsionan con los defectos. La decisión central: ¿qué umbral detecta todos los defectos sin falsos positivos?

📘 **Dónde se aprende** (3 clases): [B44-C15 · Píxeles defectuosos](../programa/clases/B44/B44-C15-pixeles-defectuosos/CLASE.md); [B88-C14 · Pruebas de software embarcado](../programa/clases/B88/B88-C14-pruebas-de-software-embarcado/CLASE.md); [B94-C06 · Validación y conformidad de protocolos de enlace](../programa/clases/B94/B94-C06-validacion-y-conformidad-de-protocolos-de-enlace/CLASE.md).

### Muestra de auditoría

- Hash anclado: hash final guardado aparte. Muestra de auditoría: entradas revisadas.

💡 **Cómo se explica en la clase [B96-C30](../programa/clases/B96/B96-C30-registro-y-auditoria-de-operaciones/CLASE.md):**
- Consultar la bitácora y calcular una muestra de auditoría.
- Ejercicio 12 · integrador. Integrador. Elabora tu *bitácora verificable con prueba de manipulación*: entrada, cadena, manipulaciones probadas, límite del truncamiento, muestra de auditoría y lista de lo consultado, sintético y no consultado.
- 🎯 **Por qué importa:** Sin registro verificable no se puede reconstruir un incidente ni demostrar quién aprobó un comando. La decisión central: ¿cómo se registra para que una alteración se detecte y cuánto hay que revisar en una auditoría?

📘 **Dónde se aprende** (1 clase): [B96-C30 · Registro y auditoría de operaciones](../programa/clases/B96/B96-C30-registro-y-auditoria-de-operaciones/CLASE.md).

### Muestra limitada por flujo

- La muestra limitada por flujo detecta lo más brillante que `m_lim`.

🎯 **Por qué importa (clase B28-C19):** Si se promedia la luminosidad de los eventos detectados sin corregir, se sobrestima la luminosidad típica de la población. El mismo razonamiento vale para las masas de fusiones de ondas gravitacionales detectadas.

📘 **Dónde se aprende** (1 clase): [B28-C19 · Limitaciones y sesgos de detección](../programa/clases/B28/B28-C19-limitaciones-y-sesgos-de-deteccion/CLASE.md).

### Muestra sintética

- La muestra sintética es un conjunto de datos simulados.

💡 **Cómo se explica en la clase [B26-C20](../programa/clases/B26/B26-C20-limites-observacionales-de-modelos-cosmologicos/CLASE.md):**
- En esta clase se ajusta una muestra sintética de `100` supernovas con `Ω_m = 0,315` verdadero y ruido de `0,15 mag`.
- Datos: ninguno observado; muestra sintética;
- 🎯 **Por qué importa:** Una cifra cosmológica sin incertidumbre no significa nada. Para decidir si dos resultados concuerdan, o si un modelo queda excluido, hay que saber construir y leer un intervalo de confianza.

📘 **Dónde se aprende** (1 clase): [B26-C20 · Límites observacionales de modelos cosmológicos](../programa/clases/B26/B26-C20-limites-observacionales-de-modelos-cosmologicos/CLASE.md).

### Muestras de entrenamiento

- Las muestras de entrenamiento son píxeles con clase conocida usados para estimar el clasificador; las muestras de prueba son píxeles independientes con clase conocida para evaluarlo.

💡 **Cómo se explica en la clase [B15-C22](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md):**
- Con 30 muestras de entrenamiento por clase y 5000 de prueba por clase, el laboratorio da:
- Su límite: en el gráfico ves los grupos; en una imagen real, las clases no son gaussianas ni están bien definidas, y las muestras de entrenamiento pueden estar sesgadas.
- ⚠️ **Error frecuente:** Muestras de prueba correlacionadas con las de entrenamiento. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un mapa de cobertura de suelo parece una verdad; en realidad es una predicción con un error que depende de las muestras elegidas y de cuánto se solapan las clases en el espacio espectral. Cifras como «90 % de exactitud» no significan nada sin decir con qué datos se midieron, ni cómo se reparte el error entre clases.

📘 **Dónde se aprende** (1 clase): [B15-C22 · Clasificación supervisada de imágenes](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md).

### Muestras de prueba

- Las muestras de entrenamiento son píxeles con clase conocida usados para estimar el clasificador; las muestras de prueba son píxeles independientes con clase conocida para evaluarlo.

💡 **Cómo se explica en la clase [B15-C22](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md):**
- Con 30 muestras de entrenamiento por clase y 5000 de prueba por clase, el laboratorio da:
- La evaluación honesta exige muestras de prueba separadas (o validación cruzada).
- ⚠️ **Error frecuente:** Muestras de prueba correlacionadas con las de entrenamiento. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un mapa de cobertura de suelo parece una verdad; en realidad es una predicción con un error que depende de las muestras elegidas y de cuánto se solapan las clases en el espacio espectral. Cifras como «90 % de exactitud» no significan nada sin decir con qué datos se midieron, ni cómo se reparte el error entre clases.

📘 **Dónde se aprende** (1 clase): [B15-C22 · Clasificación supervisada de imágenes](../programa/clases/B15/B15-C22-clasificacion-supervisada-de-imagenes/CLASE.md).

### Muestreo

- El muestreo es tomar valores de una señal continua a intervalos regulares `Δt`.
- El muestreo: píxeles por `λ/D`.

💡 **Cómo se explica en la clase [B15-C02](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md):**
- A["Señal continua<br/>frecuencia f"] --> B["Muestreo<br/>f_s = 1/Δt"]
- Paso 2 · Muestreo. `f_s = 86 400/120 = 720 c/d`;
- 🎯 **Por qué importa:** Un detector que mide una estrella cada 2 minutos no puede ver directamente algo que oscila cada 3 minutos con precisión, pero tampoco lo ignora: ese movimiento rápido queda registrado como una oscilación lenta y falsa. Si no sabes que eso ocurre, publicarías un periodo que no existe.

📘 **Dónde se aprende** (2 clases): [B15-C02 · Muestreo y aliasing](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md); [B42-C06 · Función de dispersión puntual](../programa/clases/B42/B42-C06-funcion-de-dispersion-puntual/CLASE.md).

### Muestreo de importancia

- El muestreo de importancia estima `E_p[h(X)]` sorteando de otra densidad `q` (la propuesta) y ponderando cada muestra por el peso `w(x) = p(x)/q(x)`: `E_p[h] = ∫ h p dx = ∫ h (p/q) q dx = E_q[h w]`.
- El muestreo de importancia pondera muestras de la previa con la verosimilitud para aproximar la posterior de Bayes.

💡 **Cómo se explica en la clase [B12-C15](../programa/clases/B12/B12-C15-muestreo-de-importancia/CLASE.md):**
- Muestreo de importancia: gran ahorro si la propuesta es buena, riesgo de varianza infinita si no.
- Estimar un suceso raro y su error típico con muestreo de importancia.
- 🎯 **Por qué importa:** Los sucesos que más interesan en seguridad espacial —un error de aproximación fuera de límites, una falla simultánea, una colisión— son raros por diseño. Un Monte Carlo simple puede pasar millones de ensayos sin ver un solo acierto y reportar «cero», que no es una estimación útil.

📘 **Dónde se aprende** (2 clases): [B12-C15 · Muestreo de importancia](../programa/clases/B12/B12-C15-muestreo-de-importancia/CLASE.md); [B74-C10 · Filtro de Kalman no lineal](../programa/clases/B74/B74-C10-filtro-de-kalman-no-lineal/CLASE.md).

### Muestreo de Nyquist

- El muestreo de Nyquist: al menos 2 píxeles por `λ/D`.
- El muestreo de Nyquist pide al menos dos píxeles por elemento resoluble.
- El muestreo de Nyquist pide al menos `2` píxeles por FWHM.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B43-C01](../programa/clases/B43/B43-C01-requisitos-opticos-y-mecanicos/CLASE.md):**
- Decidir el tamaño de píxel por muestreo de Nyquist.
- 🎯 **Por qué importa:** Sin requisitos escritos, cada pieza del telescopio se fabrica «lo mejor posible» y no se sabe cuándo basta. La decisión central: ¿qué error de frente de onda, qué escala de imagen y qué tolerancia mecánica hay que pedir, y cómo se reparte el error entre las piezas?

📘 **Dónde se aprende** (6 clases): [B41-C11 · Campo visual y escala de placa](../programa/clases/B41/B41-C11-campo-visual-y-escala-de-placa/CLASE.md); [B42-C07 · Función de transferencia óptica](../programa/clases/B42/B42-C07-funcion-de-transferencia-optica/CLASE.md); [B43-C01 · Requisitos ópticos y mecánicos](../programa/clases/B43/B43-C01-requisitos-opticos-y-mecanicos/CLASE.md); [B44-C17 · Escala de imagen y muestreo](../programa/clases/B44/B44-C17-escala-de-imagen-y-muestreo/CLASE.md); [B45-C06 · Diseño de espectrógrafos](../programa/clases/B45/B45-C06-diseno-de-espectrografos/CLASE.md); [B46-C09 · Conversión analógica digital](../programa/clases/B46/B46-C09-conversion-analogica-digital/CLASE.md).

### Muestreo descendente

- El muestreo descendente reduce la resolución (p. ej., agrupando 2 × 2) para captar contexto; el ascendente la restituye.

🎯 **Por qué importa (clase B17-C11):** Delimitar una mancha solar, una nube o un cráter a mano en miles de imágenes no escala. Un umbral por píxel falla cuando el ruido es comparable al contraste.

📘 **Dónde se aprende** (1 clase): [B17-C11 · Redes de segmentación semántica de imágenes](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md).

### Muestreo estroboscópico

- El muestreo estroboscópico toma una medida por vuelta en la misma fase.

🎯 **Por qué importa (clase B72-C15):** Una fórmula de primer orden se usa mucho tiempo sin preguntar cuándo deja de valer. La decisión central: ¿cómo saber cuándo basta un desarrollo de primer orden y cómo se estima su error?

📘 **Dónde se aprende** (1 clase): [B72-C15 · Aproximaciones perturbativas](../programa/clases/B72/B72-C15-aproximaciones-perturbativas/CLASE.md).

### MUF

- La MUF (frecuencia máxima utilizable) para un salto de distancia `D` es `foF2/cos φ`, con `φ` el ángulo de incidencia en la capa.

💡 **Cómo se explica en la clase [B89-C22](../programa/clases/B89/B89-C22-propagacion-ionosferica-y-comunicaciones-hf/CLASE.md):**
- Con la densidad en `4×10¹¹` la MUF baja a `63 %` de la diurna (misma razón en todas las distancias, `√(N₂/N₁)`): a 2000 km, de `25,3` a `16,0 MHz`.
- *Descripción textual:* la densidad da la frecuencia crítica; la distancia y la altura dan el ángulo de incidencia; juntos dan la MUF; una tormenta cambia la densidad y por tanto la MUF.
- ⚠️ **Error frecuente:** Confundir `foF2` con la MUF. Se corrige con 8.3.
- 🎯 **Por qué importa:** En un apagón de enlaces por satélite o en regiones remotas, el HF sigue siendo un medio de comunicación; saber qué frecuencia usar a cada hora y distancia, y cómo la perturba una tormenta, decide si el enlace existe.

📘 **Dónde se aprende** (1 clase): [B89-C22 · Propagación ionosférica y comunicaciones HF](../programa/clases/B89/B89-C22-propagacion-ionosferica-y-comunicaciones-hf/CLASE.md).

### Multigrid

- El multigrid combina relajaciones en una jerarquía de mallas.

💡 **Cómo se explica en la clase [B21-C03](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md):**
- Esa asimetría es la propiedad de suavizado, y es la clave del multigrid.
- Si el número de ciclos para una tolerancia dada no depende de `N`, el trabajo total es proporcional al número de incógnitas: Athena++ lo dice con la notación `O(N)` del multigrid completo frente a `O(N log N)` de la FFT (S2).
- ⚠️ **Error frecuente:** Suponer que más relajaciones en la malla fina equivalen a multigrid. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** El potencial gravitatorio de una nube de gas, el potencial electrostático alrededor de una nave que se carga en el plasma y la presión en un fluido incompresible obedecen la misma ecuación: la de Poisson. Los códigos de simulación astrofísica la resuelven en cada paso de tiempo;

📘 **Dónde se aprende** (1 clase): [B21-C03 · Ecuación de Poisson: relajación y multigrid](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md).

### Multiplicador

- El multiplicador es la producción total que genera una um de demanda final de una etapa.

💡 **Cómo se explica en la clase [B124-C01](../programa/clases/B124/B124-C01-cadena-de-valor-de-industria-espacial/CLASE.md):**
- El multiplicador de la etapa `j` es la suma de la columna `j` de `(I − A)⁻¹`.
- Las etapas aguas abajo tienen mayor multiplicador porque compran a varias etapas; los materiales, que no compran a nadie de la cadena, tienen 1.
- ⚠️ **Error frecuente:** Pensar que más multiplicador es siempre mejor. Se corrige con 8.4: el multiplicador no dice cuánto valor queda en la etapa.
- 🎯 **Por qué importa:** El bloque necesita un mapa común antes de hablar de costos, financiamiento o contratos: ¿quién le compra a quién y dónde queda el valor? Ninguna clase anterior del programa trata la estructura económica de la industria espacial.

📘 **Dónde se aprende** (1 clase): [B124-C01 · Cadena de valor de industria espacial](../programa/clases/B124/B124-C01-cadena-de-valor-de-industria-espacial/CLASE.md).

### Multiplicador de Lagrange

- `λ` es el multiplicador de Lagrange.
- El multiplicador de Lagrange convierte un problema con restricción en uno sin ella.

🎯 **Por qué importa (clase B11-C23):** Casi todo problema de diseño de trayectorias tiene límites: tiempo máximo, combustible disponible, distancia mínima a un cuerpo. Un optimizador que ignora las restricciones devuelve un resultado imposible; uno que las trata mal da un resultado que parece factible y no es óptimo.

📘 **Dónde se aprende** (2 clases): [B11-C23 · Optimización restringida: Lagrange, KKT y SQP](../programa/clases/B11/B11-C23-optimizacion-restringida-lagrange-kkt-y-sqp/CLASE.md); [B50-C09 · Asignación y balance de tolerancias ópticas](../programa/clases/B50/B50-C09-asignacion-y-balance-de-tolerancias-opticas/CLASE.md).

### Múltiplo de cartera

- El múltiplo de cartera es el valor devuelto entre el invertido.

💡 **Cómo se explica en la clase [B126-C02](../programa/clases/B126/B126-C02-capital-de-riesgo-en-empresas-espaciales/CLASE.md):**
- Percentiles del múltiplo de cartera: `P10 = 0,86x`, `P50 = 1,86x`, `P90 = 4,88x`.
- Por cartera: múltiplo esperado y percentiles.
- 🎯 **Por qué importa:** El capital de riesgo tiene lógica y condiciones propias que el catálogo no trata. La decisión central: ¿cuánto recibe cada parte en una salida según las condiciones pactadas, y qué retorno cabe esperar de una cartera cuando casi todo el valor viene de pocos casos?

📘 **Dónde se aprende** (1 clase): [B126-C02 · Capital de riesgo en empresas espaciales](../programa/clases/B126/B126-C02-capital-de-riesgo-en-empresas-espaciales/CLASE.md).

### Multipolo

- El multipolo de orden `n` cae como `(a/r)ⁿ`.

🎯 **Por qué importa (clase B53-C03):** Las trayectorias de una sonda dependen del campo. La decisión central: ¿hasta qué término de la serie hay que llegar a una distancia dada?

📘 **Dónde se aprende** (1 clase): [B53-C03 · Campo gravitatorio planetario](../programa/clases/B53/B53-C03-campo-gravitatorio-planetario/CLASE.md).

### Multivista

- El multivista promedia `L` vistas independientes.

💡 **Cómo se explica en la clase [B69-C03](../programa/clases/B69/B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md):**
- La página de NASA Earthdata (S1) cuenta que el speckle aparece cuando la resolución no separa los dispersores y que el multivista lo reduce.
- Ejercicio 12 · integrador. Elabora tu *ficha del speckle y su filtrado*: estadística de una vista, tabla multivista, resultados de Lee y lectura del borde.
- 🎯 **Por qué importa:** Un valor de píxel aislado de una imagen SAR no mide la reflectividad de la superficie: es una muestra de una distribución muy ancha. La decisión central: ¿cuánto hay que promediar o filtrar para estimar la reflectividad con una incertidumbre dada, y a qué precio en resolución?

📘 **Dónde se aprende** (1 clase): [B69-C03 · Ruido speckle y filtrado en imágenes SAR](../programa/clases/B69/B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md).

### Mundo de ARN

- El mundo de ARN es la hipótesis de que una etapa temprana usó ARN como información y catalizador.

🎯 **Por qué importa (clase B56-C04):** Las hipótesis (mundo de ARN, metabolismo primero, ventilas hidrotermales, charcas con ciclos húmedo–seco, aporte meteorítico) se discuten a menudo con palabras. Una cuenta de espacio de secuencias permite saber cuándo una afirmación es plausible por números y cuándo exige un mecanismo de selección.

📘 **Dónde se aprende** (1 clase): [B56-C04 · Hipótesis de abiogénesis](../programa/clases/B56/B56-C04-hipotesis-de-abiogenesis/CLASE.md).

### Mundo helado

- Un mundo helado es el definido en 5.

💡 **Cómo se explica en la clase [B56-C18](../programa/clases/B56/B56-C18-proteccion-planetaria-cospar/CLASE.md):**
- Europa, Encélado y Titán, mundos helados (III orbitador, IV aterrizador por defecto;
- Para Marte y mundos helados el retorno es restringido; para la Luna es no restringido.
- ⚠️ **Error frecuente:** Suponer que los mundos helados son II. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** La política protege los otros mundos de la contaminación (para no estropear la búsqueda de vida) y la Tierra del material devuelto. Saber en qué categoría cae una misión determina su documentación, su limpieza y sus restricciones.

📘 **Dónde se aprende** (1 clase): [B56-C18 · Protección planetaria COSPAR](../programa/clases/B56/B56-C18-proteccion-planetaria-cospar/CLASE.md).

### MUSD

- La ventana de cobertura es el periodo en que el seguro responde. MUSD son millones de dólares ficticios.

💡 **Cómo se explica en la clase [B127-C01](../programa/clases/B127/B127-C01-seguros-de-lanzamiento/CLASE.md):**
- El Monte Carlo (200 000 lanzamientos, semilla 127) da una pérdida media de `7,103 MUSD`, error relativo `0,75 %`.
- Paso 3 · Prima pura. `200 × 0,03525 = 7,050 MUSD`.
- 🎯 **Por qué importa:** B124-C08 presenta el riesgo y los seguros en general; el seguro de lanzamiento tiene estructura y coberturas propias. La decisión central: ¿qué prima es coherente con la probabilidad de fallo y qué parte de ella es recargo?

📘 **Dónde se aprende** (1 clase): [B127-C01 · Seguros de lanzamiento](../programa/clases/B127/B127-C01-seguros-de-lanzamiento/CLASE.md).

### Mutación

- Una mutación es un defecto introducido a propósito para ver si las pruebas lo detectan.
- La mutación cambia, invierte o inserta bytes.

💡 **Cómo se explica en la clase [B71-C20](../programa/clases/B71/B71-C20-propagador-kepleriano-verificable/CLASE.md):**
- *Descripción textual:* los elementos se propagan con Kepler; seis pruebas con tolerancias fijadas de antemano decidieron si se acepta; la mutación demuestra que la comparación con un integrador independiente detecta lo que los invariantes no.
- Mostrar con una mutación que los invariantes no detectan un error de tiempo.
- 🎯 **Por qué importa:** Un propagador que «parece funcionar» puede tener un error de tiempo que ningún invariante detecta. La decisión central: ¿qué pruebas, con qué tolerancias y contra qué referencia independiente demuestran que el propagador es correcto?

📘 **Dónde se aprende** (2 clases): [B71-C20 · Propagador kepleriano verificable](../programa/clases/B71/B71-C20-propagador-kepleriano-verificable/CLASE.md); [B88-C37 · Fuzzing autorizado de software embarcado en banco de pruebas](../programa/clases/B88/B88-C37-fuzzing-autorizado-de-software-embarcado-en-banco-de-pruebas/CLASE.md).

### Mutante

- Un mutante es una copia del código con un defecto inyectado a propósito; si tus pruebas no lo detectan, la batería es débil.
- Un mutante es el programa con un defecto inyectado (C01).
- Un mutante es un defecto inyectado (C01).
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B23-C01](../programa/clases/B23/B23-C01-pruebas-unitarias-numericas-con-tolerancias/CLASE.md):**
- Chequeo de sensibilidad. El mutante de primer orden `E ≈ M + e·sin M` se equivoca en 1,3 × 10⁻⁴ rad para este caso: una tolerancia de 1e-9 lo detecta, una de 1e-3 no.
- Se acepta cualquier solución que justifique cada tolerancia y muestre qué `rtol` mata a cada mutante.
- 🎯 **Por qué importa:** Una prueba con tolerancia muy holgada pasa siempre y no protege nada; una con tolerancia demasiado estricta falla por ruido de redondeo y se termina desactivando. La pregunta motivadora es: ¿cómo elijo una tolerancia que sea lo bastante estricta para detectar un error real y lo bastante amplia para no fallar por redondeo?

📘 **Dónde se aprende** (5 clases): [B23-C01 · Pruebas unitarias numéricas con tolerancias](../programa/clases/B23/B23-C01-pruebas-unitarias-numericas-con-tolerancias/CLASE.md); [B23-C02 · Pruebas de propiedades físicas](../programa/clases/B23/B23-C02-pruebas-de-propiedades-fisicas/CLASE.md); [B23-C06 · Pruebas metamórficas](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md); [B88-C14 · Pruebas de software embarcado](../programa/clases/B88/B88-C14-pruebas-de-software-embarcado/CLASE.md); [B94-C06 · Validación y conformidad de protocolos de enlace](../programa/clases/B94/B94-C06-validacion-y-conformidad-de-protocolos-de-enlace/CLASE.md).

### Mutex

- El mutex permite un solo dueño.

💡 **Cómo se explica en la clase [B88-C27](../programa/clases/B88/B88-C27-exclusion-mutua-y-semaforos/CLASE.md):**
- Sin mutex, en 200 corridas hubo pérdida en las 200.
- Con mutex, nadie lee entre lectura y escritura de otro: `x = 100` siempre; pérdida 0 en 200 corridas.
- ⚠️ **Error frecuente:** Olvidar liberar el mutex. Libéralo siempre
- 🎯 **Por qué importa:** Una carrera no falla siempre: falla de vez en cuando y no se reproduce. La decisión central: ¿qué mecanismo garantiza que el acceso a un dato compartido sea exclusivo y que un buffer no se desborde ni se vacíe?

📘 **Dónde se aprende** (1 clase): [B88-C27 · Exclusión mutua y semáforos](../programa/clases/B88/B88-C27-exclusion-mutua-y-semaforos/CLASE.md).

### Mutuamente excluyentes

- Dos eventos son mutuamente excluyentes si `A∩B` es vacío; no es lo mismo que independientes.

🎯 **Por qué importa (clase B12-C01):** Una nave no sabe si un componente va a fallar; un telescopio no sabe cuántos fotones llegarán. Para decidir con información incompleta hace falta un lenguaje que diga con precisión *qué puede pasar* y *cuánto lo esperamos*.

📘 **Dónde se aprende** (1 clase): [B12-C01 · Espacios muestrales y eventos](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md).
