# Términos · F (parte 1 de 2)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · **F** · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: **1** · [2](terminos-f-2.md)

### F, d, C

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B41-C14](../programa/clases/B41/B41-C14-aberracion-cromatica-y-astigmatismo/CLASE.md):**
- **Idea central (modelo mental):** Como un prisma que abre la luz blanca en colores: la lente es un prisma curvo, cada color enfoca en un punto y el conjunto se desenfoca.
- 🎯 **Por qué importa:** El color y el astigmatismo degradan el campo de refractores y espejos. La decisión central: ¿cuánto se separan los focos por color y por plano?
- 🔗 **Se estudia junto con:** dispersión, número de Abbe, aberración cromática longitudinal, astigmatismo.

📘 **Dónde se aprende** (1 clase): [B41-C14 · Aberración cromática y astigmatismo](../programa/clases/B41/B41-C14-aberracion-cromatica-y-astigmatismo/CLASE.md).

### F1

- La exactitud es `(TP + TN)/total`; la precisión, `TP/(TP + FP)`; la exhaustividad (*recall*), `TP/(TP + FN)`; el F1, la media armónica de las dos últimas.

💡 **Cómo se explica en la clase [B25-C20](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md):**
- G --> H["Exactitud, precisión, recall, F1"]
- Construir la matriz de confusión y calcular exactitud, precisión, exhaustividad y F1.
- 🎯 **Por qué importa:** Clasificar galaxias a gran escala exige algo más que una regla que parezca razonable: hay que decir qué debe cumplir, probarlo contra casos de respuesta conocida y evaluar con honestidad cómo se comporta donde los datos son malos.
- 🔗 **Se estudia junto con:** concentración, descriptor, umbral, matriz de confusión.

📘 **Dónde se aprende** (1 clase): [B25-C20 · Proyecto de clasificación galáctica](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md).

### Factible

- Es factible si cada objetivo empieza en `t ≥ a`, termina en `t + d ≤ b`, no se solapa con otro y `Σe ≤ E`.

💡 **Cómo se explica en la clase [B98-C01](../programa/clases/B98/B98-C01-planificacion-por-objetivos-a-bordo/CLASE.md):**
- Dado un conjunto y un orden, se avanza el reloj: `inicio = max(t, a)`, `fin = inicio + d`; si `fin > b` el orden no es factible.
- Comprobar si un conjunto de objetivos es factible (ventanas y presupuesto de energía).
- 🎯 **Por qué importa:** Si el vehículo solo ejecuta una secuencia fija de comandos, un fallo a mitad de jornada deja sin sentido el resto del plan y hay que esperar la respuesta de Tierra. La decisión central: ¿qué objetivos conviene ejecutar con la energía y el tiempo disponibles, y qué hace el vehículo cuando la energía disponible baja de golpe?
- 🔗 **Se estudia junto con:** objetivo, plan, voraz, replanificación.

📘 **Dónde se aprende** (1 clase): [B98-C01 · Planificación por objetivos a bordo](../programa/clases/B98/B98-C01-planificacion-por-objetivos-a-bordo/CLASE.md).

### Factor

- El factor de Cholesky es una «raíz cuadrada» de la matriz.
- El factor `Q_max Z/F → 4,37`.

💡 **Cómo se explica en la clase [B10-C10](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md):**
- Descripción larga: `U` guarda el resultado de la eliminación y `L` guarda los multiplicadores usados; el factor de Cholesky tiene el patrón triangular con una diagonal positiva.
- Ejercicio 3 · casi autónomo. Calcula el factor de Cholesky de `[[4, 2], [2, 5]]`.
- 🎯 **Por qué importa:** Un filtro de navegación resuelve el mismo sistema con miles de lados derechos distintos; una simulación necesita muestras aleatorias con una covarianza dada; un ajuste de mínimos cuadrados quiere estabilidad. En cada caso el trabajo se hace una vez al factorizar y luego se reutiliza.
- 🔗 **Se estudia junto con:** factorización, LU, matriz de permutación, QR.

📘 **Dónde se aprende** (2 clases): [B10-C10 · Descomposiciones matriciales](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md); [B43-C25 · Rodamientos y apoyos de precisión en telescopios](../programa/clases/B43/B43-C25-rodamientos-y-apoyos-de-precision-en-telescopios/CLASE.md).

### Factor 1,42

- El factor 1,42 relaciona la masa total (con helio y elementos pesados) con la de H: `ρ = 1,42 m_p n`.

💡 **Cómo se explica en la clase [B25-C03](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md):**
- Descripción larga: la temperatura sube cuatro órdenes y la densidad baja cinco, de modo que el producto `nT` varía solo un factor tres.
- 🎯 **Por qué importa:** Las estrellas nacen del gas y devuelven gas enriquecido; el medio interestelar (MIS) es el almacén y el escenario de ese ciclo. Pero «gas» sirve de poco: un volumen del MIS puede estar a `10 K` o a `10⁶ K`, y su densidad variar un factor 10⁷ de un punto a otro.
- 🔗 **Se estudia junto con:** medio interestelar (MIS), fase, medio neutro frío, medio neutro tibio.

📘 **Dónde se aprende** (1 clase): [B25-C03 · Medio interestelar multifásico](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md).

### Factor 5 cos² i − 1

- El factor `5 cos² i − 1` fija el signo de la tasa.

💡 **Cómo se explica en la clase [B72-C05](../programa/clases/B72/B72-C05-precesion-del-argumento-del-periapsis/CLASE.md):**
- *Descripción textual:* el factor `5 cos² i − 1` decide el signo de la tasa y la nulidad en la inclinación crítica; el promedio de Gauss verifica la fórmula.
- 🎯 **Por qué importa:** Si el perigeo de una órbita muy excéntrica girara, el satélite dejaría de pasar por la región que interesa. La decisión central: ¿a qué inclinación el perigeo deja de moverse y cuánto se mueve en otras?
- 🔗 **Se estudia junto con:** precesión del perigeo, inclinación crítica, órbita tipo Molniya, línea de ápsides.

📘 **Dónde se aprende** (1 clase): [B72-C05 · Precesión del argumento del periapsis](../programa/clases/B72/B72-C05-precesion-del-argumento-del-periapsis/CLASE.md).

### Factor anamórfico

- El factor anamórfico `cos α / cos β` cambia el ancho del haz.

💡 **Cómo se explica en la clase [B45-C06](../programa/clases/B45/B45-C06-diseno-de-espectrografos/CLASE.md):**
- Calcular el haz colimado y el factor anamórfico.
- rendija fisica w = 193.9 um ; haz colimado = 50.0 mm ; beta(550 nm) = 8.995 grados ; factor anamorfico = 0.9971
- ⚠️ **Error frecuente:** Olvidar el factor anamórfico. Se corrige con la sección 9.
- 🎯 **Por qué importa:** El diseño se decide con unos pocos parámetros que se compensan entre sí. La decisión central: ¿qué ancho de rendija da la resolución deseada y cuántos píxeles muestrean cada elemento?
- 🔗 **Se estudia junto con:** rendija, colimador, dispersión lineal, elemento de resolución.

📘 **Dónde se aprende** (1 clase): [B45-C06 · Diseño de espectrógrafos](../programa/clases/B45/B45-C06-diseno-de-espectrografos/CLASE.md).

### Factor beta

- El factor beta mide cuánto aumenta el momento transferido por la eyección de material; la fuente [S4] no da un valor numérico.
- El factor beta es la fracción de fallo de causa común.

💡 **Cómo se explica en la clase [B58-C17](../programa/clases/B58/B58-C17-principios-de-mitigacion-y-desviacion/CLASE.md):**
- No se calcula aquí la nave ni el factor beta.
- Ejercicio 8 · autónomo. ¿Qué mide el factor beta?
- 🎯 **Por qué importa:** Lo que importa no es el tamaño del empuje sino cuándo se da: el desplazamiento crece con el tiempo de aviso. La decisión central: ¿qué `Δv` y cuántos años de aviso se necesitan para mover un objeto lo suficiente?
- 🔗 **Se estudia junto con:** impactor cinético, tiempo de aviso, desplazamiento a lo largo de la órbita.

📘 **Dónde se aprende** (2 clases): [B58-C17 · Principios de mitigación y desviación](../programa/clases/B58/B58-C17-principios-de-mitigacion-y-desviacion/CLASE.md); [B63-C04 · Misiones de retorno de muestras: salvaguardas históricas y regulatorias](../programa/clases/B63/B63-C04-misiones-de-retorno-de-muestras-salvaguardas-historicas-y-regulatorias/CLASE.md).

### Factor de aceleración (AF)

- Presión límite: `Q_gas/S`. Factor de aceleración (AF): ciclos de servicio por ciclo de ensayo.

💡 **Cómo se explica en la clase [B90-C12](../programa/clases/B90/B90-C12-vacio-termico-y-ciclos/CLASE.md):**
- El coeficiente 1,9, el exponente 1/3 y el 1 414 K del factor de aceleración son valores de la literatura que no se consultaron.
- O["Orbita: dT 40 K<br/>5840 ciclos/ano"] --> A["Factor de aceleracion<br/>AF = 12.04"]
- 🎯 **Por qué importa:** Una nave en órbita baja sufre unos 16 ciclos térmicos por día; no se pueden repetir 5 840 ciclos en tierra. La decisión central: ¿cuántos ciclos de ensayo con mayor amplitud representan un año de órbita y cuánto tarda la campaña?
- 🔗 **Se estudia junto con:** Vacío térmico (TVAC), Bakeout, Ciclado, Presión límite.

📘 **Dónde se aprende** (1 clase): [B90-C12 · Vacío térmico y ciclos](../programa/clases/B90/B90-C12-vacio-termico-y-ciclos/CLASE.md).

### Factor de acumulación

- El factor de acumulación es `R = 1/(1 − e^{−kτ})`.

💡 **Cómo se explica en la clase [B105-C13](../programa/clases/B105/B105-C13-farmacologia-y-microgravedad/CLASE.md):**
- Calcular el factor de acumulación en estado estacionario `1/(1 − e^{−kτ})`.
- 🎯 **Por qué importa:** Con un fármaco real, el efecto depende de su concentración en el tiempo. Un cambio de volumen modifica la concentración inicial; uno de aclaramiento, la exposición total.
- 🔗 **Se estudia junto con:** modelo de un compartimento, AUC, variabilidad lognormal.

📘 **Dónde se aprende** (1 clase): [B105-C13 · Farmacología y microgravedad](../programa/clases/B105/B105-C13-farmacologia-y-microgravedad/CLASE.md).

### Factor de amplificación

- `R` es el factor de amplificación.

💡 **Cómo se explica en la clase [B11-C09](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md):**
- Escribir el factor de amplificación `R(z)`, `z = h λ`, de un método.
- 🎯 **Por qué importa:** Un modelo térmico de una nave tiene constantes de tiempo que van de segundos (un sensor fino) a horas (un tanque grande). Un método explícito debe usar un paso comparable al más rápido aunque lo único que interese sea lo lento: pagar por una escala que no se observa.
- 🔗 **Se estudia junto con:** ecuación de prueba, estable, región de estabilidad, Euler implícito.

📘 **Dónde se aprende** (1 clase): [B11-C09 · Análisis de estabilidad numérica](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md).

### Factor de arreglo

- El factor de arreglo es la suma de las contribuciones de los elementos.
- El factor de arreglo `AF(θ) = Σₙ e^{jnψ}` con `ψ = k d (sin θ − sin θ₀)` describe la suma de los `N` elementos con una fase progresiva que dirige el haz a `θ₀`.

💡 **Cómo se explica en la clase [B49-C04](../programa/clases/B49/B49-C04-arreglos-de-antenas-factor-de-arreglo-y-formacion-de-haz/CLASE.md):**
- *Descripción textual:* los pesos y la geometría fijan el factor de arreglo; los nulos, lóbulos y la dirección salen de él.
- La evidencia es la ficha del factor de arreglo del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** El arreglo cambia ancho de haz, lóbulos laterales y ganancia según los pesos. La decisión central: ¿qué pesos y qué separación dan el haz y el nivel de lóbulos que se necesitan?
- 🔗 **Se estudia junto con:** peso, nulo, lóbulo lateral, lóbulo de rejilla.

📘 **Dónde se aprende** (2 clases): [B49-C04 · Arreglos de antenas: factor de arreglo y formación de haz](../programa/clases/B49/B49-C04-arreglos-de-antenas-factor-de-arreglo-y-formacion-de-haz/CLASE.md); [B91-C03 · Arreglos de antenas y antenas de barrido electrónico](../programa/clases/B91/B91-C03-arreglos-de-antenas-y-antenas-de-barrido-electronico/CLASE.md).

### Factor de Bayes

- El factor de Bayes `B₀₁ = Z₀/Z₁` compara dos modelos; si los priors de modelo son iguales, es el cociente de sus probabilidades posteriores.
- El factor de Bayes de `M₁` frente a `M₀` es `BF₁₀ = p(y | M₁)/p(y | M₀)`, y `BF₀₁ = 1/BF₁₀`.
- El factor de Bayes `BF = P(x|B)/P(x|A)`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C22](../programa/clases/B12/B12-C22-comparacion-de-modelos-evidencia-bayesiana-y-criterios-de-informacion/CLASE.md):**
- El factor de Bayes es `B₀₁ = 7,319` (`ln B₀₁ = 1,99`): los datos favorecen `p = 0,9` frente a «cualquier `p`», porque `M₀` apostó a un valor concreto y acertó, mientras `M₁` repartió su apuesta.
- C --> E["Factor de Bayes<br/>Z_i / Z_j"]
- 🎯 **Por qué importa:** Un modelo más flexible siempre ajusta mejor los datos que uno más sencillo, así que el ajuste solo no sirve para elegir. Hace falta penalizar la complejidad: ¿vale la pena el parámetro extra?
- 🔗 **Se estudia junto con:** evidencia, navaja de Occam, criterio de información de Akaike, bayesiano.

📘 **Dónde se aprende** (5 clases): [B12-C22 · Comparación de modelos: evidencia bayesiana y criterios de información](../programa/clases/B12/B12-C22-comparacion-de-modelos-evidencia-bayesiana-y-criterios-de-informacion/CLASE.md); [B19-C07 · Comparación de modelos bayesianos](../programa/clases/B19/B19-C07-comparacion-de-modelos-bayesianos/CLASE.md); [B31-C20 · Evaluación crítica de afirmaciones extraordinarias](../programa/clases/B31/B31-C20-evaluacion-critica-de-afirmaciones-extraordinarias/CLASE.md); [B55-C19 · Interpretación de firmas químicas](../programa/clases/B55/B55-C19-interpretacion-de-firmas-quimicas/CLASE.md); [B132-C05 · Contexto ritual y social de la observación del cielo](../programa/clases/B132/B132-C05-contexto-ritual-y-social-de-la-observacion-del-cielo/CLASE.md).

### Factor de calidad

- El factor de calidad `Q` mide la disipación (cuanto menor, más disipa).
- El factor de calidad `Q(L)` es una función del LET usada en magnitudes operacionales.
- El factor de calidad `Q ≈ 1/(2ζ)`.

💡 **Cómo se explica en la clase [B112-C02](../programa/clases/B112/B112-C02-dosis-equivalente-y-dosis-efectiva/CLASE.md):**
- Además NASA calcula su dosis efectiva con su propio factor de calidad y parámetros de una mujer de 35 años (OCHMO-TB-020, consultado), no con la tabla de ICRP.
- No necesariamente: según OCHMO-TB-020 se usa el factor de calidad de NASA (modelo de cáncer de 2012) y parámetros de una mujer de 35 años.
- ⚠️ **Error frecuente:** Aplicar los `w_R` de ICRP a un límite que usa otro factor de calidad. Lee la definición de la norma (ejercicio 9).
- 🎯 **Por qué importa:** Ninguna clase trata factores de ponderación y dosis equivalente, y sin ellos un límite en mSv de una norma no se puede leer. La decisión central: ¿cómo se resume en un solo número en sievert una exposición mezclada de varias radiaciones y órganos, y qué no dice ese número?
- 🔗 **Se estudia junto con:** dosis equivalente, dosis efectiva, detrimento.

📘 **Dónde se aprende** (3 clases): [B47-C11 · Aislamiento vibracional](../programa/clases/B47/B47-C11-aislamiento-vibracional/CLASE.md); [B65-C06 · Calentamiento por marea y equilibrio térmico en satélites](../programa/clases/B65/B65-C06-calentamiento-por-marea-y-equilibrio-termico-en-satelites/CLASE.md); [B112-C02 · Dosis equivalente y dosis efectiva](../programa/clases/B112/B112-C02-dosis-equivalente-y-dosis-efectiva/CLASE.md).

### Factor de calidad sin carga

- El factor de calidad sin carga `Q_u` mide las pérdidas del resonador.

💡 **Contexto en la clase [B49-C10](../programa/clases/B49/B49-C10-filtros-de-radiofrecuencia-pasabanda-y-rechazo-de-banda-imagen/CLASE.md):**
- **Idea central (modelo mental):** Como un colador: deja pasar lo que cabe y detiene lo demás; uno más fino detiene mejor pero deja pasar menos agua.
- 🎯 **Por qué importa:** Más orden rechaza más, pero también pierde más señal. La decisión central: ¿qué orden y qué ancho de banda dan el rechazo de imagen necesario con una pérdida aceptable?
- 🔗 **Se estudia junto con:** filtro de Butterworth, prototipo pasabajos, banda imagen, pérdida de inserción.

📘 **Dónde se aprende** (1 clase): [B49-C10 · Filtros de radiofrecuencia pasabanda y rechazo de banda imagen](../programa/clases/B49/B49-C10-filtros-de-radiofrecuencia-pasabanda-y-rechazo-de-banda-imagen/CLASE.md).

### Factor de carga

- El factor de carga `C = k_b/(k_b + k_m)` es la fracción de la carga externa que toma el tornillo.

💡 **Cómo se explica en la clase [B84-C17](../programa/clases/B84/B84-C17-soldadura-y-uniones/CLASE.md):**
- El factor de carga es `C = 0,2902`; con una tracción de `3000 N`, `MS_rotura = 0,248`, `MS_separación = 0,677` y, con cortante de `1500 N`, `MS_deslizamiento = −0,727`: la unión desliza y hacen falta pasadores.
- Calcular rigideces y el factor de carga `C`.
- 🎯 **Por qué importa:** Un tornillo que se separa o desliza falla sin romper: la precarga es lo que mantiene la unión, y su dispersión por el par de apriete es grande. La decisión central: ¿qué precarga mantiene la unión cerrada sin romper el tornillo, y cuándo deslizan las placas?
- 🔗 **Se estudia junto con:** separación, deslizamiento, garganta.

📘 **Dónde se aprende** (1 clase): [B84-C17 · Soldadura y uniones](../programa/clases/B84/B84-C17-soldadura-y-uniones/CLASE.md).

### Factor de carga φ

- Coeficiente de par `K`: relaciona par y precarga e incluye la fricción. Factor de carga `φ`: fracción de una carga externa que absorbe el perno.

💡 **Cómo se explica en la clase [B90-C06](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md):**
- La carga externa de ejemplo es 4 kg × 50 g / 4 pernos = 490 N y, con factor 1,4: `MS = 1 667/(490 × 1,4) − 1 = 1,43`.
- Calcular la carga de separación de una unión con el factor de carga `φ` y su margen.
- 🎯 **Por qué importa:** Un perno mal apretado se afloja con la vibración o se rompe por exceso de carga; un centro de masa fuera de rango desvía la nave en el despliegue. La decisión central: ¿qué par de apriete garantiza que la unión no se separe ni se plastifique, y el conjunto queda dentro de los límites de masa?
- 🔗 **Se estudia junto con:** Precarga, Coeficiente de par K, Margen de separación, Centro de masa (CG).

📘 **Dónde se aprende** (1 clase): [B90-C06 · Integración mecánica de subsistemas](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md).

### Factor de cobertura k

- El factor de cobertura `k` es el multiplicador de `u_c` que da `U`; suele estar entre 2 y 3 (S1, 2.3.6).

💡 **Cómo se explica en la clase [B13-C12](../programa/clases/B13/B13-C12-incertidumbre-expandida/CLASE.md):**
- La GUM (S1, 7.2.4) ilustra con un ejemplo que, para `ν = 9`, el factor de cobertura para 95 % es `k = 2,26`, basado en la distribución t.
- Definir incertidumbre típica, combinada, expandida y factor de cobertura.
- 🎯 **Por qué importa:** Un telémetro da `1000,004 m` con una incertidumbre típica de `0,017 m`. ¿Cuál es el intervalo dentro del cual el valor verdadero cae «casi seguro»?
- 🔗 **Se estudia junto con:** incertidumbre típica, incertidumbre típica combinada u_c, incertidumbre expandida U, nivel de confianza.

📘 **Dónde se aprende** (1 clase): [B13-C12 · Incertidumbre expandida](../programa/clases/B13/B13-C12-incertidumbre-expandida/CLASE.md).

### Factor de compresibilidad

- El factor de compresibilidad `Z = PV/(nRT)` mide la desviación: `Z = 1` es ideal.
- El factor de compresibilidad `Z` mide la desviación de un gas real del ideal (no se calcula aquí).

💡 **Contexto en la clase [B06-C09](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md):**
- **Idea central (modelo mental):** Imagina bolitas muy pequeñas, lejos unas de otras, que rebotan contra las paredes de una caja. La presión es la fuerza media de esos choques; sube si las bolitas van más rápido (temperatura mayor) o si hay más (mayor densidad). A presión alta, las bolitas ya no están tan lejos y empiezan a notarse su tamaño y sus atracciones.
- 🎯 **Por qué importa:** La NASA publica para Marte, Venus y la Tierra la presión y la temperatura medias en la superficie, la gravedad, el peso molecular de la atmósfera y su densidad (S1, S2, S3). ¿Puedes reproducir esa densidad con sólo lo anterior?
- 🔗 **Se estudia junto con:** ley de los gases ideales, constante molar de los gases, gas ideal, densidad.

📘 **Dónde se aprende** (2 clases): [B06-C09 · Gases ideales y no ideales](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md); [B54-C04 · Presión y densidad](../programa/clases/B54/B54-C04-presion-y-densidad/CLASE.md).

### Factor de conversión

- Un factor de conversión es una razón igual a 1 (por ejemplo, `1 au/149 597 870 700 m`).
- Un factor de conversión es una razón de dos cantidades equivalentes, como `1 km / 1000 m`; vale 1 porque numerador y denominador son la misma cantidad.
- El factor de conversión `X_CO` pasa de `W_CO` a densidad de columna de `H₂`: `N(H₂) = X_CO W_CO`.

💡 **Cómo se explica en la clase [B01-C08](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md):**
- Para pasar de un peldaño a otro multiplicas por un factor de conversión que vale 1.
- Entre cada par se indica el factor de conversión; todos valen 1 porque numerador y denominador son la misma longitud.
- 🎯 **Por qué importa:** En 1999 se perdió la sonda Mars Climate Orbiter por una discrepancia entre unidades inglesas y métricas (C04, fuente NASA). La ciencia estaba bien; la conversión, no.
- 🔗 **Se estudia junto con:** Sistema Internacional (SI), unidades base, unidad derivada, unidad no SI aceptada.

📘 **Dónde se aprende** (3 clases): [B01-C08 · Mediciones y unidades astronómicas](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md); [B03-C07 · Conversión de distancia y velocidad](../programa/clases/B03/B03-C07-conversion-de-distancia-y-velocidad/CLASE.md); [B25-C04 · Nubes moleculares y polvo](../programa/clases/B25/B25-C04-nubes-moleculares-y-polvo/CLASE.md).

### Factor de crecimiento

- El factor de crecimiento `D(a)` normalizado a `D = a` en la era de la materia.
- El factor de crecimiento `g = D/a`.

💡 **Cómo se explica en la clase [B36-C01](../programa/clases/B36/B36-C01-crecimiento-lineal-de-perturbaciones-de-densidad/CLASE.md):**
- Con `Ωm = 0,315` (resumen de Planck 2018) y un universo plano, el crecimiento lineal hasta hoy queda en `D(1) = 0,7878` frente a `1` de un universo de solo materia, y el factor de tasa en `f(0) = 0,527`.
- 🎯 **Por qué importa:** Sin la teoría lineal no se sabe cuánto ha crecido una perturbación entre el CMB y hoy. La decisión central: ¿cuánto frena la constante cosmológica el crecimiento y cómo se comprueba la solución numérica?
- 🔗 **Se estudia junto con:** perturbación, factor de tasa, parámetro de densidad, Einstein–de Sitter.

📘 **Dónde se aprende** (2 clases): [B36-C01 · Crecimiento lineal de perturbaciones de densidad](../programa/clases/B36/B36-C01-crecimiento-lineal-de-perturbaciones-de-densidad/CLASE.md); [B40-C09 · Efecto Sachs-Wolfe y efecto Sachs-Wolfe integrado](../programa/clases/B40/B40-C09-efecto-sachs-wolfe-y-efecto-sachs-wolfe-integrado/CLASE.md).

### Factor de crecimiento de masa

- El factor de crecimiento de masa es la masa en órbita dividida entre la masa en superficie.

💡 **Cómo se explica en la clase [B100-C02](../programa/clases/B100/B100-C02-dimensionamiento-de-carga-y-volumen-de-mision/CLASE.md):**
- Por masa en origen: factor de crecimiento.
- Obtener el factor de crecimiento de masa entre la órbita y la superficie.
- 🎯 **Por qué importa:** La masa que llega a la superficie es una fracción pequeña de la que sale de la Tierra, y el volumen puede decidir antes que la masa. La decisión central: ¿cuánta masa y cuánto volumen hay que cargar para N personas durante D días, y cuánta masa hay que lanzar para que esa carga llegue?
- 🔗 **Se estudia junto con:** masa neta, factor de embalaje, repuestos, ecuación ideal del cohete.

📘 **Dónde se aprende** (1 clase): [B100-C02 · Dimensionamiento de carga y volumen de misión](../programa/clases/B100/B100-C02-dimensionamiento-de-carga-y-volumen-de-mision/CLASE.md).

### Factor de derating

- El derating es operar un componente por debajo de su valor nominal; el factor de derating es la fracción del nominal que se permite (`0,6` = hasta el 60 %).

💡 **Cómo se explica en la clase [B93-C02](../programa/clases/B93/B93-C02-seleccion-de-componentes-y-derating/CLASE.md):**
- N["valor nominal"] --> F["x factor de derating"]
- Aplicar un factor de derating de tensión o de potencia y calcular el margen.
- 🎯 **Por qué importa:** Nadie en el tronco trataba la selección de componentes calificados ni el derating. La decisión central: ¿cumple cada pieza de la lista con los factores de derating, con qué margen, y qué se cambia cuando no cumple?
- 🔗 **Se estudia junto con:** derating, margen, temperatura de unión.

📘 **Dónde se aprende** (1 clase): [B93-C02 · Selección de componentes y derating](../programa/clases/B93/B93-C02-seleccion-de-componentes-y-derating/CLASE.md).

### Factor de descuento

- El factor de descuento `δ` mide la paciencia.

💡 **Cómo se explica en la clase [B119-C27](../programa/clases/B119/B119-C27-diplomacia-y-comunicacion-entre-estados-ante-incidentes-espaciales/CLASE.md):**
- No se consultó práctica diplomática ni arbitral. El ejemplo conductor: un excedente de 100 unidades de utilidad sintéticas a repartir entre dos Estados con puntos de desacuerdo 10 y 20, y factores de descuento 0,90 y 0,80 para las ofertas alternadas.
- 🎯 **Por qué importa:** C20 simula la respuesta institucional interna; la diplomacia entre Estados no está cubierta. Esta clase aporta el razonamiento básico de negociación sin pretender describir ninguna práctica.
- 🔗 **Se estudia junto con:** solución de Nash, ofertas alternadas, inducción hacia atrás.

📘 **Dónde se aprende** (1 clase): [B119-C27 · Diplomacia y comunicación entre Estados ante incidentes espaciales](../programa/clases/B119/B119-C27-diplomacia-y-comunicacion-entre-estados-ante-incidentes-espaciales/CLASE.md).

### Factor de Eddington

- El factor de Eddington `Γ = L/L_Edd` es la fracción del límite que emite la estrella (C09).

💡 **Cómo se explica en la clase [B24-C17](../programa/clases/B24/B24-C17-estrellas-masivas-y-perdida-de-masa/CLASE.md):**
- *Descripción textual:* de la masa y la luminosidad se obtiene el factor de Eddington; cuanto más cercano a 1, más fácil es expulsar gas; la masa disminuye con el tiempo y fija el destino final.
- Calcular el factor de Eddington `Γ = L/L_Edd` de una estrella.
- 🎯 **Por qué importa:** La masa que una estrella conserva hasta su final decide el destino: remanente, tipo de supernova, enriquecimiento del medio. Y las estrellas masivas no la conservan: pierden masa por vientos, erupciones y transferencia a una compañera.
- 🔗 **Se estudia junto con:** viento estelar, pérdida de masa, erupciones, estructura en grumos.

📘 **Dónde se aprende** (1 clase): [B24-C17 · Estrellas masivas y pérdida de masa](../programa/clases/B24/B24-C17-estrellas-masivas-y-perdida-de-masa/CLASE.md).

### Factor de efectividad

- El factor de efectividad `η` es la fracción del consumo ideal que se logra de hecho.

💡 **Cómo se explica en la clase [B64-C06](../programa/clases/B64/B64-C06-biofilms-en-ambientes-extremos/CLASE.md):**
- El factor de efectividad es `η = tanh(φ)/φ` y la longitud de penetración, `1/√(k/D_e)`.
- El factor de efectividad calculado con el flujo en la superficie coincide con `tanh(φ)/φ` a 1 %.
- 🎯 **Por qué importa:** Una película de células y matriz crea su propio microambiente. La pregunta motivadora: ¿hasta qué profundidad llega un nutriente en un biofilm y qué sucede con las células que quedan más adentro?
- 🔗 **Se estudia junto con:** matriz de EPS, difusividad efectiva, constante de consumo, módulo de Thiele.

📘 **Dónde se aprende** (1 clase): [B64-C06 · Biofilms en ambientes extremos](../programa/clases/B64/B64-C06-biofilms-en-ambientes-extremos/CLASE.md).

### Factor de eficiencia

- Sistema socio-técnico: conjunto de personas, procedimientos y equipos interdependientes. Factor de eficiencia: probabilidad de que un subsistema esté disponible.

💡 **Cómo se explica en la clase [B48-C01](../programa/clases/B48/B48-C01-observatorio-como-sistema-socio-tecnico/CLASE.md):**
- Descomponer la eficiencia de un observatorio en factores independientes.
- 🎯 **Por qué importa:** Sin una visión de sistema, cada equipo optimiza su parte y nadie sabe qué mejora rinde más. La decisión central: ¿en qué factor conviene invertir para recuperar más noches útiles?
- 🔗 **Se estudia junto con:** Sistema socio-técnico, Serie, Paralelo, Sensibilidad.

📘 **Dónde se aprende** (1 clase): [B48-C01 · Observatorio como sistema socio-técnico](../programa/clases/B48/B48-C01-observatorio-como-sistema-socio-tecnico/CLASE.md).

### Factor de embalaje

- El factor de embalaje multiplica la masa por el envase y los soportes.

💡 **Cómo se explica en la clase [B100-C02](../programa/clases/B100/B100-C02-dimensionamiento-de-carga-y-volumen-de-mision/CLASE.md):**
- Añadir embalaje y repuestos como factores sobre la masa neta.
- El script [carga.py](carga.py) calcula masa y volumen de tres consumibles, aplica embalaje y repuestos, resuelve la ecuación del cohete hacia atrás en tres tramos (comprueba el producto de factores con `ε = 0` a 1e-9 y la recuperación del Δv).
- 🎯 **Por qué importa:** La masa que llega a la superficie es una fracción pequeña de la que sale de la Tierra, y el volumen puede decidir antes que la masa. La decisión central: ¿cuánta masa y cuánto volumen hay que cargar para N personas durante D días, y cuánta masa hay que lanzar para que esa carga llegue?
- 🔗 **Se estudia junto con:** masa neta, repuestos, ecuación ideal del cohete, factor de crecimiento de masa.

📘 **Dónde se aprende** (1 clase): [B100-C02 · Dimensionamiento de carga y volumen de misión](../programa/clases/B100/B100-C02-dimensionamiento-de-carga-y-volumen-de-mision/CLASE.md).

### Factor de empaque

- El factor de empaque (1,3, ilustrativo) convierte masa de alimento en masa transportada.

💡 **Contexto en la clase [B105-C12](../programa/clases/B105/B105-C12-nutricion-espacial/CLASE.md):**
- 🎯 **Por qué importa:** Cada kilogramo de alimento que se lanza cuesta; cada kilocaloría que falta se paga con masa corporal. La decisión central: ¿cuánto alimento hay que transportar para una misión y con qué margen frente a la incertidumbre del gasto?
- 🔗 **Se estudia junto con:** ecuación de Mifflin–St Jeor, PAL, factores de Atwater.

📘 **Dónde se aprende** (1 clase): [B105-C12 · Nutrición espacial](../programa/clases/B105/B105-C12-nutricion-espacial/CLASE.md).

### Factor de encogimiento

- El factor de encogimiento `B_j = σ_j²/(σ_j² + τ²)` es la fracción por la que el sensor `j` se acerca al grupo.

💡 **Cómo se explica en la clase [B19-C02](../programa/clases/B19/B19-C02-modelos-jerarquicos/CLASE.md):**
- Calcular el factor de encogimiento `B_j` y explicar por qué cambia entre unidades.
- 🎯 **Por qué importa:** Seis sensores de temperatura de un satélite miden cada uno un desvío de calibración. Tres decisiones ingenuas son posibles: tratar a cada sensor por separado, ignorar las diferencias y promediar todo, o confiar en el sensor más preciso.
- 🔗 **Se estudia junto con:** modelo jerárquico, hiperparámetros, hiperprior, Agrupación nula.

📘 **Dónde se aprende** (1 clase): [B19-C02 · Modelos jerárquicos](../programa/clases/B19/B19-C02-modelos-jerarquicos/CLASE.md).

### Factor de ensayos

- El factor de ensayos (*trials factor*) es el número de frecuencias independientes exploradas.

💡 **Cómo se explica en la clase [B15-C06](../programa/clases/B15/B15-C06-analisis-espectral-de-senales/CLASE.md):**
- Si ignoras el factor de ensayos y usas el `z` de un solo bin (`z = 4,6` para 1 %), obtienes unos `M × 1 % ≈ 10` picos falsos.
- ⚠️ **Error frecuente:** Olvidar el factor de ensayos. Se corrige con el ejercicio 8.
- 🎯 **Por qué importa:** Alguien afirma: «hay un periodo de 3,7 días en esta estrella». ¿Cómo se sostiene?
- 🔗 **Se estudia junto con:** periodograma, ventana, Hann, ganancia coherente.

📘 **Dónde se aprende** (1 clase): [B15-C06 · Análisis espectral de señales](../programa/clases/B15/B15-C06-analisis-espectral-de-senales/CLASE.md).

### Factor de escala

- El factor de escala `E` es la razón entre una longitud real y la longitud de la maqueta: `longitud_maqueta = longitud_real / E`.
- El factor de escala `k` en un punto y dirección es la razón entre la longitud en el mapa y la longitud real;
- El factor de escala `a(t)` mide cuánto crecieron las distancias.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C20](../programa/clases/B03/B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md):**
- R["Requisitos: 1 au = 10 m; cabe en 350 m; misma escala para todo"] --> E["Factor de escala E = 1 au / 10 m"]
- *Descripción textual:* de los requisitos se calcula el factor de escala; con él se construye la tabla de maqueta; la tabla pasa por tres verificaciones (razones, Kepler y espacio/tiempo de luz); y todo se resume en un informe con límites y conflictos.
- 🎯 **Por qué importa:** Un ingeniero no recibe un ejercicio con una sola fórmula: recibe requisitos («que quepa en un patio de 350 m», «que se vea el Sol», «que Neptuno esté a su sitio») y debe decidir qué se puede cumplir y qué no.
- 🔗 **Se estudia junto con:** requisito, componente, criterio de comprobación, maqueta a escala.

📘 **Dónde se aprende** (5 clases): [B03-C20 · Problema integrado de escala del sistema solar](../programa/clases/B03/B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md); [B04-C17 · Proyecciones cartográficas elementales](../programa/clases/B04/B04-C17-proyecciones-cartograficas-elementales/CLASE.md); [B26-C13 · Modelo FLRW — Relatividad y cosmología](../programa/clases/B26/B26-C13-modelo-flrw-relatividad-y-cosmologia/CLASE.md); [B80-C02 · Modelo de error de acelerómetros](../programa/clases/B80/B80-C02-modelo-de-error-de-acelerometros/CLASE.md); [B131-C05 · Demostraciones visuales y modelos para el aula](../programa/clases/B131/B131-C05-demostraciones-visuales-y-modelos-para-el-aula/CLASE.md).

### Factor de escala de volúmenes

- Si `m = n`, `det J` es el factor de escala de volúmenes de la transformación (C04).

💡 **Cómo se explica en la clase [B10-C19](../programa/clases/B10/B10-C19-jacobianos-y-linealizacion/CLASE.md):**
- Interpretar `det J` como factor de escala de volúmenes.
- 🎯 **Por qué importa:** Una estación mide la distancia, el azimut y la elevación de un objeto con incertidumbres. Para decir dónde está en coordenadas cartesianas y cuánta incertidumbre tiene esa posición, hay que transformar los números y sus errores.
- 🔗 **Se estudia junto con:** jacobiano, aproximación lineal, cambio de coordenadas, propagación lineal de covarianza.

📘 **Dónde se aprende** (1 clase): [B10-C19 · Jacobianos y linealización](../programa/clases/B10/B10-C19-jacobianos-y-linealizacion/CLASE.md).

### Factor de expansión

- El factor de expansión `f` de las líneas de campo.

💡 **Contexto en la clase [B33-C10](../programa/clases/B33/B33-C10-modelos-de-viento-solar-para-pronostico-parker-y-wsa/CLASE.md):**
- **Idea central (modelo mental):** La relación empírica es una receta que funciona en la práctica; Parker es una ley derivada de principios.
- 🎯 **Por qué importa:** Un pronóstico necesita una condición de frontera coronal. La decisión central: ¿cómo cambia la velocidad con la expansión y la distancia al borde?
- 🔗 **Se estudia junto con:** distancia angular, relación empírica, modelo físico.

📘 **Dónde se aprende** (1 clase): [B33-C10 · Modelos de viento solar para pronóstico (Parker y WSA)](../programa/clases/B33/B33-C10-modelos-de-viento-solar-para-pronostico-parker-y-wsa/CLASE.md).

### Factor de fatiga

- La sensibilidad `q = 1/(1 + a_p/r)` da el factor de fatiga `K_f = 1 + q(K_t − 1)`.

💡 **Cómo se explica en la clase [B84-C29](../programa/clases/B84/B84-C29-concentraciones-de-tension-y-entallas/CLASE.md):**
- Factor de entalla a fatiga: Kf = 1 + q (Kt - 1), q = 1/(1 + a_p/r) con a_p = 0,5 mm (ILUSTRATIVO):
- 🎯 **Por qué importa:** Una tensión remota de 100 MPa se triplica a 300 MPa en el borde de un agujero; con `K_f = 2,8` la vida baja de 10¹¹ a 10⁷ ciclos. La decisión central: ¿qué tensión local y qué vida resultan de un agujero en una placa cargada?
- 🔗 **Se estudia junto con:** solución de Kirsch, factor teórico, sensibilidad.

📘 **Dónde se aprende** (1 clase): [B84-C29 · Concentraciones de tensión y entallas](../programa/clases/B84/B84-C29-concentraciones-de-tension-y-entallas/CLASE.md).

### Factor de filtro

- Un factor de filtro `fᵢ` es el número entre 0 y 1 que multiplica cada componente de la solución ingenua en la base de la SVD.

💡 **Cómo se explica en la clase [B22-C02](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md):**
- Con `A = Σᵢ σᵢ uᵢ vᵢᵀ` (C01), la solución ingenua es `Σᵢ (uᵢᵀ b / σᵢ) vᵢ`; la de Tikhonov es la misma con cada término multiplicado por un factor de filtro (S2, ec. 5–6):
- Pausa. Con `λ = 0,1`, ¿cuál es el factor de filtro de `σ = 1` y el de `σ = 0,01`?
- 🎯 **Por qué importa:** Si no puedes confiar en `x = A⁻¹ b` y no puedes bajar el ruido a voluntad, necesitas una regla que ignore lo que los datos no pueden decir. Esa regla debe tener una perilla: cuánto ignorar.
- 🔗 **Se estudia junto con:** solución regularizada, desajuste, penalización, parámetro de regularización.

📘 **Dónde se aprende** (1 clase): [B22-C02 · Regularización de Tikhonov](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md).

### Factor de fin de vida

- El factor de fin de vida es la potencia final dividida por la inicial.

💡 **Cómo se explica en la clase [B86-C14](../programa/clases/B86/B86-C14-envejecimiento-de-paneles/CLASE.md):**
- *Descripción textual:* el tiempo y los ciclos alimentan cuatro factores que se multiplican en el factor de fin de vida; éste da la potencia a cada año, el margen y el sobredimensionamiento.
- Ejercicio 12 · integrador. Integrador. Elabora tu *curva de potencia de fin de vida con sensibilidad*: factores por año, margen, sobredimensionamiento, Monte Carlo y rótulos.
- 🎯 **Por qué importa:** Dimensionar un ala con su potencia de inicio de vida deja a la misión sin energía al final. El factor de fin de vida que se usó como `0,85` en la primera clase sale de un cálculo como este.
- 🔗 **Se estudia junto con:** degradación, radiación, ciclado térmico, contaminación.

📘 **Dónde se aprende** (1 clase): [B86-C14 · Envejecimiento de paneles](../programa/clases/B86/B86-C14-envejecimiento-de-paneles/CLASE.md).

### Factor de forma

- El factor de forma `F` es la fracción de la radiación de una superficie que llega a otra.

💡 **Cómo se explica en la clase [B41-C15](../programa/clases/B41/B41-C15-refractores-acromaticos-y-apocromaticos/CLASE.md):**
- factores de forma del triplete (k1, k2, k3) = (-3.0533, -0.2394, 6.2841) /1000 mm
- 🎯 **Por qué importa:** Un refractor sin color necesita combinar vidrios. La decisión central: ¿cuánto color queda con dos o tres vidrios?
- 🔗 **Se estudia junto con:** doblete acromático, espectro secundario, triplete apocromático, potencia.

📘 **Dónde se aprende** (2 clases): [B41-C15 · Refractores acromáticos y apocromáticos](../programa/clases/B41/B41-C15-refractores-acromaticos-y-apocromaticos/CLASE.md); [B85-C01 · Balance radiativo de satélite](../programa/clases/B85/B85-C01-balance-radiativo-de-satelite/CLASE.md).

### Factor de Franck-Condon

- El factor de Franck-Condon `FC(v'', v') = |∫ψ''_{v''}ψ'_{v'} dx|²` es la probabilidad relativa de cada banda vibracional.

💡 **Contexto en la clase [B62-C03](../programa/clases/B62/B62-C03-transiciones-electronicas-moleculares/CLASE.md):**
- **Idea central (modelo mental):** Dos hamacas con el mismo balanceo pero colgadas a distancia `d`: lo que sale del solapamiento depende de cuánto se mira de una a otra. Límite: las hamacas reales son anarmónicas y pueden tener distinta forma.
- 🎯 **Por qué importa:** Las bandas electrónicas aparecen en el ultravioleta y el visible; su forma, una serie de picos, revela cuánto cambia la geometría de la molécula. La decisión central: ¿qué picos de la progresión serán intensos?
- 🔗 **Se estudia junto con:** principio de Franck-Condon, aproximación de Condon, factor de Huang-Rhys, progresión.

📘 **Dónde se aprende** (1 clase): [B62-C03 · Transiciones electrónicas moleculares](../programa/clases/B62/B62-C03-transiciones-electronicas-moleculares/CLASE.md).

### Factor de fricción de Darcy

- El factor de fricción de Darcy `f` da la pérdida de presión de un tubo, `Δp = f (L/D) ½ ρ V²`.

💡 **Contexto en la clase [B79-C04](../programa/clases/B79/B79-C04-regimenes-laminar-y-turbulento/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR D["rho, V, L, mu"] --> R["Re"] R -->|"Re bajo"| L["laminar: f = 64/Re ; Cf = 1,328/sqrt(Re)"] R -->|"Re alto"| T["turbulento: Blasius ; Cf = 0,074 Re^-0,2"] L --> A["arrastre y pérdida"] T --> A ``` *Descripción textual:* el número de Reynolds elige la correlación de fricción y de arrastre.
- 🎯 **Por qué importa:** El régimen cambia el arrastre y la transferencia de calor por factores de varios; no distinguirlo lleva a subestimar el calentamiento de una pared o la pérdida de presión de un conducto. El tronco no lo trata.
- 🔗 **Se estudia junto con:** número de Reynolds, laminar, turbulento, coeficiente de arrastre.

📘 **Dónde se aprende** (1 clase): [B79-C04 · Regímenes laminar y turbulento](../programa/clases/B79/B79-C04-regimenes-laminar-y-turbulento/CLASE.md).

### Factor de Huang-Rhys

- El factor de Huang-Rhys `S = μωd²/(2ħ)` mide el desplazamiento en unidades de oscilador.

💡 **Cómo se explica en la clase [B62-C03](../programa/clases/B62/B62-C03-transiciones-electronicas-moleculares/CLASE.md):**
- Obtener FC(0, v') con la fórmula `e^(−S)S^(v')/v'!` y reconocer el factor de Huang-Rhys `S`.
- Caso A: misma frecuencia 2000 cm^-1, desplazamiento 0.1 A -> factor de Huang-Rhys S = 2.03380
- 🎯 **Por qué importa:** Las bandas electrónicas aparecen en el ultravioleta y el visible; su forma, una serie de picos, revela cuánto cambia la geometría de la molécula. La decisión central: ¿qué picos de la progresión serán intensos?
- 🔗 **Se estudia junto con:** principio de Franck-Condon, factor de Franck-Condon, aproximación de Condon, progresión.

📘 **Dónde se aprende** (1 clase): [B62-C03 · Transiciones electrónicas moleculares](../programa/clases/B62/B62-C03-transiciones-electronicas-moleculares/CLASE.md).

### Factor de idealidad

- El factor de idealidad `n` ajusta la pendiente exponencial.

💡 **Contexto en la clase [B86-C02](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md):**
- 🎯 **Por qué importa:** La potencia de una celda no es un número fijo: depende de la tensión a la que se la haga trabajar y de su temperatura. Elegir mal el punto de operación o ignorar la temperatura del ala cambia la potencia entregada.
- 🔗 **Se estudia junto con:** corriente fotogenerada, corriente de saturación, resistencia en serie, punto de máxima potencia.

📘 **Dónde se aprende** (1 clase): [B86-C02 · Celdas solares](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md).

### Factor de Landé efectivo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B32-C12](../programa/clases/B32/B32-C12-efecto-zeeman-y-diagnostico-de-campos-magneticos-estelares/CLASE.md):**
- **Idea central (modelo mental):** Un campo magnético hace que la cuerda del átomo vibre con dos tonos ligeramente distintos según la polarización; la diferencia entre ambos tonos es el signo del campo.
- 🎯 **Por qué importa:** Medir campos estelares exige saber cuándo el desdoblamiento se resuelve y cuándo basta la polarización. La decisión central: ¿qué campo produce un desdoblamiento comparable al ancho de la línea?
- 🔗 **Se estudia junto con:** efecto Zeeman, desdoblamiento, polarización circular, aproximación de campo débil.

📘 **Dónde se aprende** (2 clases): [B32-C12 · Efecto Zeeman y diagnóstico de campos magnéticos estelares](../programa/clases/B32/B32-C12-efecto-zeeman-y-diagnostico-de-campos-magneticos-estelares/CLASE.md); [B47-C21 · Magnetógrafos y medición de campos solares](../programa/clases/B47/B47-C21-magnetografos-y-medicion-de-campos-solares/CLASE.md).

### Factor de llenado

- El factor de llenado es `FF = P_max/(V_oc I_sc)`.

💡 **Cómo se explica en la clase [B86-C02](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md):**
- El factor de llenado es `0,8179` y la eficiencia `P_max/(G A) = 28,06 %`.
- *Descripción textual:* la luz fija `I_ph`; el diodo y la resistencia en serie dan la curva `I(V)`; de ella salen los extremos, el punto de máxima potencia, el factor de llenado y la eficiencia; la temperatura modifica el diodo.
- 🎯 **Por qué importa:** La potencia de una celda no es un número fijo: depende de la tensión a la que se la haga trabajar y de su temperatura. Elegir mal el punto de operación o ignorar la temperatura del ala cambia la potencia entregada.
- 🔗 **Se estudia junto con:** corriente fotogenerada, corriente de saturación, factor de idealidad, resistencia en serie.

📘 **Dónde se aprende** (1 clase): [B86-C02 · Celdas solares](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md).

### Factor de Lorentz

- El factor de Lorentz `Γ` de la capa.

💡 **Contexto en la clase [B27-C17](../programa/clases/B27/B27-C17-explosiones-de-rayos-gamma/CLASE.md):**
- **Idea central (modelo mental):** La capa casi alcanza a su propia luz: un foton emitido en `R` llega unos `R/(2Γ²c)` después que uno emitido en el centro. Para `Γ` grande, un radio enorme produce un retardo de segundos.
- 🎯 **Por qué importa:** Una explosión que parece de energía enorme puede ser de energía moderada vista de frente, y un retardo de segundos entre dos mensajeros, tras viajar 130 millones de años, es una medición extraordinariamente precisa. La decisión central: ¿qué retardo y qué energía real implican un factor de Lorentz y un ángulo dados?
- 🔗 **Se estudia junto con:** destello de rayos gamma, retardo de llegada, energía isótropa, fracción de colimación.

📘 **Dónde se aprende** (1 clase): [B27-C17 · Explosiones de rayos gamma](../programa/clases/B27/B27-C17-explosiones-de-rayos-gamma/CLASE.md).

### Factor de mentira

- El factor de mentira (definición adoptada aquí) es `LF = efecto en el gráfico / efecto en los datos`, con efecto `(B − A)/A`.

💡 **Cómo se explica en la clase [B130-C01](../programa/clases/B130/B130-C01-infografias-con-fuentes-verificables/CLASE.md):**
- Si el diámetro del círculo es proporcional al dato, el área de la Tierra parece `6,93` veces la de Marte y el factor de mentira vale `3,633`; si el área es proporcional, vale `1,000`.
- Calcular el factor de mentira de un par de círculos y escalar por área.
- 🎯 **Por qué importa:** Comunicar con imágenes exige mantener la fuente y la incertidumbre; la clase de comunicación general no entra en cómo se audita una pieza visual. La decisión central: ¿qué debe llevar cada cifra de una infografía para que otra persona pueda verificarla, y qué diseño la deforma?
- 🔗 **Se estudia junto con:** ficha de procedencia, estado, color representativo, crédito.

📘 **Dónde se aprende** (2 clases): [B130-C01 · Infografías con fuentes verificables](../programa/clases/B130/B130-C01-infografias-con-fuentes-verificables/CLASE.md); [B130-C02 · Visualización de datos para comunicar](../programa/clases/B130/B130-C02-visualizacion-de-datos-para-comunicar/CLASE.md).

### Factor de momento de inercia

- El factor de momento de inercia es `I/(MR²)`.
- El factor de momento de inercia `C/(MR²)` vale `0,4` para una esfera uniforme y menos si la masa se concentra hacia el centro.

💡 **Cómo se explica en la clase [B09-C18](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md):**
- La ficha de la Tierra de la NASA (S2) da la masa `5,9722 × 10²⁴ kg`, el radio medio volumétrico `6371,000 km`, la densidad media `5513 kg/m³` y el factor de momento de inercia polar `I/(MR²) = 0,3308`.
- 🎯 **Por qué importa:** La masa de la Tierra se conoce mucho mejor que la distribución de esa masa en su interior. Un solo número, la densidad media, no basta: el momento de inercia depende de cómo se reparte la masa.
- 🔗 **Se estudia junto con:** integral doble, integración iterada, integral triple, teorema de Fubini.

📘 **Dónde se aprende** (3 clases): [B09-C18 · Integrales dobles y triples](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md); [B53-C01 · Interior de planetas rocosos](../programa/clases/B53/B53-C01-interior-de-planetas-rocosos/CLASE.md); [B65-C05 · Inversión geofísica conjunta: validación de modelos interiores](../programa/clases/B65/B65-C05-inversion-geofisica-conjunta-validacion-de-modelos-interiores/CLASE.md).

### Factor de oblicuidad

- El factor de oblicuidad `1/√(1 − (R cos E/(R+h))²)` convierte vertical en oblicuo.

💡 **Cómo se explica en la clase [B89-C21](../programa/clases/B89/B89-C21-efectos-ionosfericos-y-centelleo-en-senales-gnss/CLASE.md):**
- E["elevacion"] --> OBL["factor de oblicuidad"]
- Calcular el factor de oblicuidad con una capa fina.
- 🎯 **Por qué importa:** La ionosfera es el mayor error de un receptor GNSS de una sola frecuencia y el origen de pérdidas de señal en regiones ecuatoriales y polares; sin entenderla no se puede interpretar un error de posición. La decisión central: ¿cuánto error añade la ionosfera, cómo se elimina y cuándo el centelleo hace perder la señal?
- 🔗 **Se estudia junto con:** retardo ionosférico de grupo, combinación libre de ionosfera, índice S4.

📘 **Dónde se aprende** (1 clase): [B89-C21 · Efectos ionosféricos y centelleo en señales GNSS](../programa/clases/B89/B89-C21-efectos-ionosfericos-y-centelleo-en-senales-gnss/CLASE.md).

### Factor de Occam

- El factor de Occam es la parte del factor de Bayes que penaliza la complejidad: cuanto más se reparte el prior de un modelo en valores que no explican los datos, menor su evidencia.

💡 **Cómo se explica en la clase [B19-C07](../programa/clases/B19/B19-C07-comparacion-de-modelos-bayesianos/CLASE.md):**
- El factor `√(1 + r)` crece con el ancho del prior (`τ`) y es la penalización de Occam: M₁ reparte su prior sobre valores que los datos descartan.
- Explicar por qué el factor de Bayes premia la parsimonia (factor de Occam) y depende del prior.
- 🎯 **Por qué importa:** Miras 10 mediciones de la amplitud de una señal y el promedio es 0,57 con ruido conocido 1. ¿Hay señal (`μ ≠ 0`) o solo ruido (`μ = 0`)?
- 🔗 **Se estudia junto con:** evidencia, factor de Bayes, odds posteriores, densidad predictiva logarítmica esperada.

📘 **Dónde se aprende** (1 clase): [B19-C07 · Comparación de modelos bayesianos](../programa/clases/B19/B19-C07-comparacion-de-modelos-bayesianos/CLASE.md).

### Factor de orientación

- El factor de orientación `g = (1 + cos²ι)/2`.

💡 **Cómo se explica en la clase [B28-C07](../programa/clases/B28/B28-C07-fuentes-compactas-binarias/CLASE.md):**
- *Descripción textual:* la masa fija la frecuencia máxima; el alcance sale de la relación señal-ruido; el volumen y la tasa dan los eventos, reducidos por el factor de orientación.
- Verificar por Monte Carlo la razón de volúmenes y el factor de orientación `⟨g³⟩`.
- 🎯 **Por qué importa:** La tasa de eventos detectados depende del volumen que el detector ve, que crece como el cubo del alcance. Una mejora pequeña en sensibilidad se traduce en muchos más eventos.
- 🔗 **Se estudia junto con:** frecuencia ISCO, alcance, volumen, tasa.

📘 **Dónde se aprende** (1 clase): [B28-C07 · Fuentes compactas binarias](../programa/clases/B28/B28-C07-fuentes-compactas-binarias/CLASE.md).

### Factor de pérdida de polarización

- El factor de pérdida de polarización `PLF = |ê_t · ê_r*|²` va de 0 a 1.

💡 **Cómo se explica en la clase [B91-C02](../programa/clases/B91/B91-C02-polarizacion-de-antenas-y-perdidas-por-desadaptacion/CLASE.md):**
- Calcular el factor de pérdida de polarización `PLF = |ê_t · ê_r*|²` entre dos antenas.
- 🎯 **Por qué importa:** Un enlace pierde potencia si las polarizaciones no coinciden, y puede perderla toda si son ortogonales. La decisión central: ¿qué polarización y qué razón axial exigir a las dos antenas para que la desadaptación quede por debajo del margen del enlace?
- 🔗 **Se estudia junto con:** vector de Jones, razón axial, ángulo de inclinación, aislamiento de polarización cruzada.

📘 **Dónde se aprende** (1 clase): [B91-C02 · Polarización de antenas y pérdidas por desadaptación](../programa/clases/B91/B91-C02-polarizacion-de-antenas-y-perdidas-por-desadaptacion/CLASE.md).

### Factor de pérdida por polarización

- El factor de pérdida por polarización (PLF) de dos antenas lineales con desalineación `ψ` es `cos²ψ`.

💡 **Cómo se explica en la clase [B89-C01](../programa/clases/B89/B89-C01-electromagnetismo-aplicado-a-enlaces/CLASE.md):**
- Por polarización: lineal, circular a derecha o a izquierda, con su factor de pérdida.
- 🎯 **Por qué importa:** Todo presupuesto de enlace, toda antena y toda banda parten de la misma onda. Confundir longitud de onda con frecuencia, o potencia con densidad de flujo, rompe los cálculos de las clases siguientes.
- 🔗 **Se estudia junto con:** longitud de onda, densidad de flujo de potencia, ganancia, polarización.

📘 **Dónde se aprende** (1 clase): [B89-C01 · Electromagnetismo aplicado a enlaces](../programa/clases/B89/B89-C01-electromagnetismo-aplicado-a-enlaces/CLASE.md).

### Factor de pruebas

- El factor de pruebas corrige por el número de búsquedas.

💡 **Cómo se explica en la clase [B28-C09](../programa/clases/B28/B28-C09-alertas-cientificas-en-tiempo-real/CLASE.md):**
- *Descripción textual:* las etapas suman la latencia; el FAR se traduce a probabilidad y sigmas; el umbral sale de la cola del ruido y se contrasta por Monte Carlo; el factor de pruebas pasa de p local a global.
- Aplicar el factor de pruebas `1 − (1 − p)^N`.
- ⚠️ **Error frecuente:** Olvidar el factor de pruebas. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Una alerta tardía pierde el evento; una alerta con muchas falsas alarmas agota a los observadores. La decisión central: ¿qué umbral produce una tasa de falsas alarmas aceptable y cuánto tarda la alerta en llegar?
- 🔗 **Se estudia junto con:** latencia, tasa de falsas alarmas, umbral, significancia.

📘 **Dónde se aprende** (2 clases): [B28-C09 · Alertas científicas en tiempo real](../programa/clases/B28/B28-C09-alertas-cientificas-en-tiempo-real/CLASE.md); [B28-C13 · Estadística de significancia](../programa/clases/B28/B28-C13-estadistica-de-significancia/CLASE.md).

### Factor de recuperación de capital

- El factor de recuperación de capital `CRF = r(1+r)ⁿ/((1+r)ⁿ − 1)` convierte un monto inicial en pago anual.

💡 **Cómo se explica en la clase [B124-C24](../programa/clases/B124/B124-C24-capex-y-opex-de-una-instalacion-extraterrestre/CLASE.md):**
- Calcular el factor de recuperación de capital y la anualidad del CapEx.
- El script [capex_opex_instalacion.py](capex_opex_instalacion.py) calcula CapEx, OpEx, el factor de recuperación de capital, el costo nivelado por CRF y por valor actual, la producción de equilibrio y cinco sensibilidades (comprueba igualdad de ambas vías a 1e-9 y el equilibrio por sustitución).
- 🎯 **Por qué importa:** B124 estima costos de misión, pero una instalación que opera años necesita separar el capital de la operación y ponerlos en una misma unidad. La decisión central: ¿a qué costo por kilogramo produce la instalación y desde qué producción conviene frente a traer el producto?
- 🔗 **Se estudia junto con:** CapEx, OpEx, costo nivelado (LCOP), valor actual.

📘 **Dónde se aprende** (1 clase): [B124-C24 · CapEx y OpEx de una instalación extraterrestre](../programa/clases/B124/B124-C24-capex-y-opex-de-una-instalacion-extraterrestre/CLASE.md).

### Factor de redistribución

- El factor de redistribución `f` es `1/4` con redistribución global, `1/2` con redistribución solo en el hemisferio diurno y `1` en el punto subsolar sin redistribución.

💡 **Cómo se explica en la clase [B54-C17](../programa/clases/B54/B54-C17-clima-exoplanetario/CLASE.md):**
- El script [exoclima.py](exoclima.py) calcula `S`, `T_e` con tres factores de redistribución y distancias de igual instalación (comprueba `T_e` solar y la invariancia `S d²`).
- 🎯 **Por qué importa:** La temperatura de equilibrio de un exoplaneta es el primer número que se calcula. La pregunta motivadora: ¿cuánto cambia esa temperatura si el calor se redistribuye o no?
- 🔗 **Se estudia junto con:** instalación, zona habitable, temperatura de equilibrio.

📘 **Dónde se aprende** (1 clase): [B54-C17 · Clima exoplanetario](../programa/clases/B54/B54-C17-clima-exoplanetario/CLASE.md).

### Factor de ruido en exceso

- El factor de ruido en exceso `F²` multiplica la varianza de Poisson.

💡 **Cómo se explica en la clase [B44-C09](../programa/clases/B44/B44-C09-ganancia-electronica/CLASE.md):**
- *Descripción textual:* cada etapa multiplica la carga con probabilidad `p`; tras `N` etapas la media crece como `(1+p)^N` y la varianza da el factor de ruido en exceso.
- Calcular la varianza y el factor de ruido en exceso.
- 🎯 **Por qué importa:** Para señales muy débiles el ruido de lectura domina. La decisión central: ¿cuándo compensa multiplicar la carga a costa del ruido en exceso?
- 🔗 **Se estudia junto con:** etapa de multiplicación, ganancia, proceso de ramificación.

📘 **Dónde se aprende** (1 clase): [B44-C09 · Ganancia electrónica](../programa/clases/B44/B44-C09-ganancia-electronica/CLASE.md).

### Factor de seguridad

- El factor de seguridad `FS` compara resistencia y carga;
- El factor de seguridad multiplica la carga límite para obtener la de diseño.
- El factor de seguridad multiplica la fuerza mínima para el diseño.

💡 **Cómo se explica en la clase [B66-C02](../programa/clases/B66/B66-C02-procesos-de-ladera-y-transporte-de-masa/CLASE.md):**
- En cambio el factor de seguridad, el ángulo crítico, el alcance y `H/L` no dependen de `g`.
- *Descripción textual:* los ángulos y la presión de poros dan el factor de seguridad; si hay falla, el bloque acelera, llega a la base con una velocidad y se detiene tras un alcance.
- 🎯 **Por qué importa:** Un deslizamiento marciano o titaniano parece igual a uno terrestre, pero su velocidad y duración no lo son. La decisión central: ¿qué propiedades de un deslizamiento dependen de la gravedad y cuáles no?
- 🔗 **Se estudia junto con:** pendiente infinita, bloque de Coulomb, razón H/L.

📘 **Dónde se aprende** (3 clases): [B66-C02 · Procesos de ladera y transporte de masa](../programa/clases/B66/B66-C02-procesos-de-ladera-y-transporte-de-masa/CLASE.md); [B77-C10 · Restricciones de cargas estructurales](../programa/clases/B77/B77-C10-restricciones-de-cargas-estructurales/CLASE.md); [B97-C10 · Manipulación de herramientas](../programa/clases/B97/B97-C10-manipulacion-de-herramientas/CLASE.md).

### Factor de seguridad (FS)

- Esfuerzo de aro: esfuerzo circunferencial `σ = P r/t`. Factor de seguridad (FS): cociente entre límite elástico y esfuerzo.

💡 **Cómo se explica en la clase [B106-C02](../programa/clases/B106/B106-C02-presurizacion-de-modulos/CLASE.md):**
- Un cilindro de 2 m de radio a 101,325 kPa necesita, con factor de seguridad 2 y una aleación ilustrativa de 276 MPa, un espesor mínimo de 1,468 mm (51,7 kg de pared por metro); a 34,5 kPa bastan 0,500 mm.
- Calcular el esfuerzo de aro de un cilindro de pared delgada y el espesor mínimo con un factor de seguridad.
- 🎯 **Por qué importa:** La presión interior empuja hacia afuera sobre todo el casco; un espesor insuficiente rompe el recinto y un orificio pequeño lo vacía lentamente. La decisión central: ¿qué espesor mínimo y qué tiempo de respuesta hay que garantizar para una presión y un tamaño de orificio dados?
- 🔗 **Se estudia junto con:** Esfuerzo de aro, Flujo estrangulado, Coeficiente de descarga Cd, Constante de tiempo τ.

📘 **Dónde se aprende** (1 clase): [B106-C02 · Presurización de módulos](../programa/clases/B106/B106-C02-presurizacion-de-modulos/CLASE.md).

### Factor de tasa

- El factor de tasa `f = dlnD/dlna`.

💡 **Cómo se explica en la clase [B36-C01](../programa/clases/B36/B36-C01-crecimiento-lineal-de-perturbaciones-de-densidad/CLASE.md):**
- Con `Ωm = 0,315` (resumen de Planck 2018) y un universo plano, el crecimiento lineal hasta hoy queda en `D(1) = 0,7878` frente a `1` de un universo de solo materia, y el factor de tasa en `f(0) = 0,527`.
- 🎯 **Por qué importa:** Sin la teoría lineal no se sabe cuánto ha crecido una perturbación entre el CMB y hoy. La decisión central: ¿cuánto frena la constante cosmológica el crecimiento y cómo se comprueba la solución numérica?
- 🔗 **Se estudia junto con:** perturbación, factor de crecimiento, parámetro de densidad, Einstein–de Sitter.

📘 **Dónde se aprende** (1 clase): [B36-C01 · Crecimiento lineal de perturbaciones de densidad](../programa/clases/B36/B36-C01-crecimiento-lineal-de-perturbaciones-de-densidad/CLASE.md).

### Factor de temperatura

- El factor de temperatura `π_T` sigue la ley de Arrhenius.

💡 **Cómo se explica en la clase [B93-C04](../programa/clases/B93/B93-C04-analisis-de-confiabilidad-de-electronica-mtbf-y-derating/CLASE.md):**
- Calcular el factor de temperatura de Arrhenius y contrastarlo con la tabla publicada.
- 🎯 **Por qué importa:** Cuantificar la confiabilidad de la electrónica no estaba en el tronco. La decisión central: ¿qué tasa de fallas y qué MTBF tiene la suma de las piezas, qué probabilidad de supervivencia da para una misión, y cuánto la mejoran el derating y la redundancia?
- 🔗 **Se estudia junto con:** tasa de falla, MTBF, método de conteo de partes, redundancia activa.

📘 **Dónde se aprende** (1 clase): [B93-C04 · Análisis de confiabilidad de electrónica (MTBF y derating)](../programa/clases/B93/B93-C04-analisis-de-confiabilidad-de-electronica-mtbf-y-derating/CLASE.md).

### Factor de trabajo

- El factor de trabajo es la fracción de ranuras con pulso: `1/(1,25 M)`.

💡 **Cómo se explica en la clase [B92-C01](../programa/clases/B92/B92-C01-fuentes-laser-y-amplificadores-para-enlaces-espaciales/CLASE.md):**
- P --> D["factor de trabajo<br/>1 / (1,25 M)"]
- *Descripción textual:* la semilla pasa por el amplificador; la potencia media, con el factor de trabajo de PPM, da la potencia de pico y la energía por pulso; con la energía del fotón da la tasa de fotones.
- ⚠️ **Error frecuente:** Olvidar las ranuras de guarda. Se corrige con 8.3: el factor de trabajo es `1/(1,25 M)`.
- 🎯 **Por qué importa:** Un enlace óptico se dimensiona con fotones, no con vatios. La decisión central: ¿cuánta potencia de pico y cuánta energía por pulso debe entregar la fuente para una potencia media dada, y hasta dónde sirve aumentar la ganancia del amplificador?
- 🔗 **Se estudia junto con:** rejilla de frecuencias, energía del fotón, potencia de pico, energía de saturación.

📘 **Dónde se aprende** (1 clase): [B92-C01 · Fuentes láser y amplificadores para enlaces espaciales](../programa/clases/B92/B92-C01-fuentes-laser-y-amplificadores-para-enlaces-espaciales/CLASE.md).

### Factor de uso

- El factor de uso es la fracción de la velocidad máxima que se aprovecha en promedio.

💡 **Cómo se explica en la clase [B97-C01](../programa/clases/B97/B97-C01-robots-rover-y-orbitadores/CLASE.md):**
- Con un factor de uso de `0,5` y `4 h` de conducción, el recorrido es `304,0` m por día de operación, y `5 km` llevan `16,45` días.
- Un orbitador ilustrativo a `300 km` con una franja de `12 km` la cubre con 4,44 min de imagen continua; un rover que debe recorrer `5 km` con un factor de uso `0,5` tarda 16,45 días de operación.
- ⚠️ **Error frecuente:** Usar la velocidad máxima como promedio. El factor de uso lo corrige (8.3)
- 🎯 **Por qué importa:** Elegir entre «ir con un rover» y «mirar desde órbita» es la primera decisión de una misión robótica, y se toma con órdenes de magnitud. Sin ellos, se prometen traslados que tardan meses o coberturas que una órbita no entrega.
- 🔗 **Se estudia junto con:** rover, orbitador, velocidad sobre el suelo, franja.

📘 **Dónde se aprende** (1 clase): [B97-C01 · Robots rover y orbitadores](../programa/clases/B97/B97-C01-robots-rover-y-orbitadores/CLASE.md).

### Factor de velocidad

- El factor de velocidad es `v/c` en el cable.

💡 **Cómo se explica en la clase [B49-C02](../programa/clases/B49/B49-C02-adaptacion-de-impedancias-y-lineas-de-transmision-en-antenas/CLASE.md):**
- Convertir longitud eléctrica en longitud física con el factor de velocidad.
- A 150 MHz con factor de velocidad 0.66: longitud electrica de cuarto de onda = 0.32977 m
- ⚠️ **Error frecuente:** Usar la longitud en el vacío en lugar de la del cable. Se corrige con el factor de velocidad.
- 🎯 **Por qué importa:** Una antena desadaptada devuelve potencia y empeora la sensibilidad. La decisión central: ¿cuánta potencia se refleja y cómo se adapta con un tramo de línea?
- 🔗 **Se estudia junto con:** coeficiente de reflexión, ROE, pérdida de retorno, carta de Smith.

📘 **Dónde se aprende** (1 clase): [B49-C02 · Adaptación de impedancias y líneas de transmisión en antenas](../programa/clases/B49/B49-C02-adaptacion-de-impedancias-y-lineas-de-transmision-en-antenas/CLASE.md).

### Factor de vista

- El factor de vista es la fracción de la emisión de un elemento que llega a otro.
- CVCM: volátiles condensables recogidos, `100 m_col/mᵢ`. Factor de vista: fracción de la emisión de una superficie que alcanza a otra.

💡 **Cómo se explica en la clase [B50-C05](../programa/clases/B50/B50-C05-luz-parasita-y-analisis-de-rayos-dispersos/CLASE.md):**
- P["parche lambertiano"] --> V["factor de vista"]
- *Descripción textual:* la reflectancia fija la potencia del fantasma, el trazado fija su foco y tamaño, y el factor de vista mide la luz dispersa que llega al detector.
- 🎯 **Por qué importa:** El contraste de un instrumento no depende solo de la imagen: depende de cuánta luz llega por caminos no deseados. La decisión central: ¿qué fracción de luz llega por un camino parásito y cómo se reduce?
- 🔗 **Se estudia junto con:** fantasma, reflectancia de Fresnel, lambertiana, deflector.

📘 **Dónde se aprende** (2 clases): [B50-C05 · Luz parásita y análisis de rayos dispersos](../programa/clases/B50/B50-C05-luz-parasita-y-analisis-de-rayos-dispersos/CLASE.md); [B90-C04 · Control de contaminación](../programa/clases/B90/B90-C04-control-de-contaminacion/CLASE.md).

### Factor Doppler

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B27-C11](../programa/clases/B27/B27-C11-chorros-relativistas/CLASE.md):**
- *Descripción textual:* la velocidad y el factor de Lorentz dan la velocidad aparente y el factor Doppler; el máximo de la primera ocurre cuando `cosθ = β`, donde `δ = γ`.
- Calcular el factor Doppler `δ = 1/(γ(1 − β cosθ))`.
- 🎯 **Por qué importa:** Un chorro que se acerca puede parecer más rápido que la luz sin violar nada, y su brillo cambia en órdenes de magnitud según el ángulo. Sin estos efectos no se pueden comparar chorros ni inferir su velocidad.
- 🔗 **Se estudia junto con:** velocidad aparente, movimiento superlumínico aparente, cono de emisión, contrachorro.

📘 **Dónde se aprende** (1 clase): [B27-C11 · Chorros relativistas](../programa/clases/B27/B27-C11-chorros-relativistas/CLASE.md).

### Factor integrante

- El factor integrante `μ(t) = exp(∫ a dt)` convierte el lado izquierdo en `(μ y)′`.

💡 **Cómo se explica en la clase [B11-C03](../programa/clases/B11/B11-C03-ecuaciones-de-primer-orden/CLASE.md):**
- El factor integrante lleva a una integral.
- D -->|sí| E["Factor integrante<br/>μ = exp(∫a dt)"]
- 🎯 **Por qué importa:** Muchos procesos espaciales relajan hacia un equilibrio: una cápsula que cae frena hasta una velocidad terminal, un instrumento se enfría hacia la temperatura de su entorno, una población de partículas decae.
- 🔗 **Se estudia junto con:** separable, lineal, equilibrio, constante de tiempo.

📘 **Dónde se aprende** (1 clase): [B11-C03 · Ecuaciones de primer orden](../programa/clases/B11/B11-C03-ecuaciones-de-primer-orden/CLASE.md).

### Factor preexponencial

- El factor preexponencial `ν` es la frecuencia de intento (en ML s⁻¹ para orden cero, en s⁻¹ para orden uno).

💡 **Contexto en la clase [B68-C01](../programa/clases/B68/B68-C01-desorcion-termica-de-hielos-interestelares/CLASE.md):**
- **Idea central (modelo mental):** Imagina un balde con un agujero que se agranda exponencialmente con la temperatura. En orden cero el agujero deja salir un caudal fijo, sin importar el nivel: el balde se vacía de golpe cuando el agujero es suficiente. En orden uno el caudal baja con el nivel y el vaciado es exponencial.
- 🎯 **Por qué importa:** Un hielo de CO que dura mil millones de años a 15 K desaparece en un segundo a 30 K. Esa sensibilidad exponencial decide dónde está la «línea de nieve» de cada molécula y qué hay en el gas.
- 🔗 **Se estudia junto con:** desorción, energía de enlace, orden cero, orden uno.

📘 **Dónde se aprende** (1 clase): [B68-C01 · Desorción térmica de hielos interestelares](../programa/clases/B68/B68-C01-desorcion-termica-de-hielos-interestelares/CLASE.md).

### Factor Q

- El factor `Q` es `1/(2ζ)` y es la amplificación en resonancia.
- Resonancia: frecuencia a la que un equipo amplifica. Factor `Q`: amplificación en resonancia.

💡 **Cómo se explica en la clase [B84-C11](../programa/clases/B84/B84-C11-vibraciones-y-resonancias/CLASE.md):**
- Un equipo de `f_n = 300 Hz` y `Q = 10` bajo `0,04 g²/Hz` plano responde con `13,729 g rms` por Miles y `13,796 g rms` por integración (0,48 % de diferencia); bajo el perfil de mano de obra mínima del GEVS (`6,784 g rms` de entrada) responde con `13,722 g rms`, un factor de 2,02 en rms.
- 🎯 **Por qué importa:** Un equipo con `Q = 10` en resonancia recibe 10 veces la aceleración de entrada; Miles da la respuesta rms en una línea.
- 🔗 **Se estudia junto con:** transmisibilidad, ecuación de Miles.

📘 **Dónde se aprende** (2 clases): [B84-C11 · Vibraciones y resonancias](../programa/clases/B84/B84-C11-vibraciones-y-resonancias/CLASE.md); [B90-C09 · Ensayos de vibración](../programa/clases/B90/B90-C09-ensayos-de-vibracion/CLASE.md).

### Factor teórico

- El factor teórico `K_t = σ_máx/σ_nom`.

💡 **Cómo se explica en la clase [B84-C29](../programa/clases/B84/B84-C29-concentraciones-de-tension-y-entallas/CLASE.md):**
- *Descripción textual:* Kirsch da el campo y el factor teórico; la integral verifica el equilibrio; con la sensibilidad se pasa a `K_f` y a la vida.
- 🎯 **Por qué importa:** Una tensión remota de 100 MPa se triplica a 300 MPa en el borde de un agujero; con `K_f = 2,8` la vida baja de 10¹¹ a 10⁷ ciclos. La decisión central: ¿qué tensión local y qué vida resultan de un agujero en una placa cargada?
- 🔗 **Se estudia junto con:** solución de Kirsch, sensibilidad, factor de fatiga.

📘 **Dónde se aprende** (1 clase): [B84-C29 · Concentraciones de tensión y entallas](../programa/clases/B84/B84-C29-concentraciones-de-tension-y-entallas/CLASE.md).

### Factor Y

- El factor Y es el cociente de potencias con carga caliente y fría.

💡 **Cómo se explica en la clase [B49-C06](../programa/clases/B49/B49-C06-amplificadores-de-bajo-ruido-lna-tecnologia-ganancia-y-adaptacion/CLASE.md):**
- H["carga caliente/fría"] --> Y["factor Y"]
- El factor Y simulado da `11,795 K`, `3,09 %` de diferencia.
- 🎯 **Por qué importa:** Una décima de decibelio antes del primer amplificador cuesta más que mejorar el mezclador. La decisión central: ¿qué bloque domina la temperatura de ruido y qué pérdidas deben evitarse antes de él?
- 🔗 **Se estudia junto con:** temperatura de ruido, cifra de ruido, fórmula de Friis, ganancia disponible.

📘 **Dónde se aprende** (1 clase): [B49-C06 · Amplificadores de bajo ruido (LNA): tecnología, ganancia y adaptación](../programa/clases/B49/B49-C06-amplificadores-de-bajo-ruido-lna-tecnologia-ganancia-y-adaptacion/CLASE.md).

### Factor β

- El factor β es la fracción de la probabilidad de falla que es de causa común.

💡 **Cómo se explica en la clase [B97-C17](../programa/clases/B97/B97-C17-seguridad-funcional-robotica/CLASE.md):**
- Incorporar la falla de causa común con un factor beta.
- 🎯 **Por qué importa:** Duplicar un canal parece bajar la probabilidad de falla al cuadrado; pero si una causa afecta a ambos, la mejora real es mucho menor. Calcularlo evita sobreestimar la seguridad de una arquitectura redundante.
- 🔗 **Se estudia junto con:** 1oo1, 1oo2, 2oo2, 2oo3.

📘 **Dónde se aprende** (1 clase): [B97-C17 · Seguridad funcional robótica](../programa/clases/B97/B97-C17-seguridad-funcional-robotica/CLASE.md).

### Factores de Atwater

- Los factores de Atwater son 4 kcal/g de proteína y carbohidrato y 9 kcal/g de grasa.

💡 **Cómo se explica en la clase [B105-C12](../programa/clases/B105/B105-C12-nutricion-espacial/CLASE.md):**
- Repartir la energía en gramos de proteína, grasa y carbohidrato con factores de Atwater.
- 🎯 **Por qué importa:** Cada kilogramo de alimento que se lanza cuesta; cada kilocaloría que falta se paga con masa corporal. La decisión central: ¿cuánto alimento hay que transportar para una misión y con qué margen frente a la incertidumbre del gasto?
- 🔗 **Se estudia junto con:** ecuación de Mifflin–St Jeor, PAL, factor de empaque.

📘 **Dónde se aprende** (1 clase): [B105-C12 · Nutrición espacial](../programa/clases/B105/B105-C12-nutricion-espacial/CLASE.md).

### Factores de conversión

- Los factores de conversión son cocientes iguales a 1, por ejemplo `1000 m / 1 km`.

💡 **Cómo se explica en la clase [B05-C01](../programa/clases/B05/B05-C01-magnitudes-fisicas-y-dimensiones/CLASE.md):**
- *Pasos:* aplica factores de conversión (sección 8.3).
- 🎯 **Por qué importa:** La pregunta motivadora es: ¿cómo sé que una fórmula o un cálculo tiene sentido antes de confiar en su resultado? La decisión central es qué declarar junto a cada número (magnitud, unidad y dimensión) y cómo comprobar que las ecuaciones son coherentes.
- 🔗 **Se estudia junto con:** magnitud física, unidad, valor numérico, dimensión.

📘 **Dónde se aprende** (1 clase): [B05-C01 · Magnitudes físicas y dimensiones](../programa/clases/B05/B05-C01-magnitudes-fisicas-y-dimensiones/CLASE.md).

### Factores modificadores

- Una reserva es la parte del recurso que, aplicados los factores modificadores (accesibilidad, recuperación), se puede extraer.

💡 **Cómo se explica en la clase [B67-C04](../programa/clases/B67/B67-C04-estimacion-de-reservas-y-categorias-de-recursos/CLASE.md):**
- *Descripción textual:* las muestras dan la fracción de hielo con su intervalo; junto con área, espesor y densidad se propaga la incertidumbre a la masa; el semiancho define la categoría; solo lo Medido o Indicado se convierte en reserva tras los factores modificadores.
- Por conversión: recurso por factores modificadores igual a reserva.
- 🎯 **Por qué importa:** Decir «hay 330 kt» sin intervalo ni categoría invita a decisiones equivocadas. La decisión central: ¿cuánto del recurso se puede llamar reserva, y qué falta para subir de categoría?
- 🔗 **Se estudia junto con:** recurso, reserva, categorías, semiancho relativo.

📘 **Dónde se aprende** (1 clase): [B67-C04 · Estimación de reservas y categorías de recursos](../programa/clases/B67/B67-C04-estimacion-de-reservas-y-categorias-de-recursos/CLASE.md).

### Factorización

- Una factorización (o descomposición) escribe `A` como producto de factores con estructura.

💡 **Cómo se explica en la clase [B10-C10](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md):**
- La factorización de Cholesky de `P` lo permite.
- Calcular una factorización `P A = L U` y usarla para resolver sistemas.
- 🎯 **Por qué importa:** Un filtro de navegación resuelve el mismo sistema con miles de lados derechos distintos; una simulación necesita muestras aleatorias con una covarianza dada; un ajuste de mínimos cuadrados quiere estabilidad. En cada caso el trabajo se hace una vez al factorizar y luego se reutiliza.
- 🔗 **Se estudia junto con:** LU, matriz de permutación, QR, Cholesky.

📘 **Dónde se aprende** (1 clase): [B10-C10 · Descomposiciones matriciales](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md).

### Factorización de Cholesky

- La factorización de Cholesky `P = L Lᵀ` existe si `P` es definida positiva y sirve para generar muestras.

💡 **Cómo se explica en la clase [B12-C18](../programa/clases/B12/B12-C18-matrices-de-covarianza/CLASE.md):**
- Una «matriz de correlación» con `r₁₂ = 0,9`, `r₁₃ = 0,9`, `r₂₃ = −0,9` parece razonable pero tiene un autovalor `−0,8`: no es semidefinida positiva, y la factorización de Cholesky falla.
- 🎯 **Por qué importa:** El resultado de una determinación de órbita o de un ajuste no es un número sino un vector con una matriz de covarianza; sin ella no se puede propagar, comparar con otro resultado ni calcular probabilidades.
- 🔗 **Se estudia junto con:** matriz de covarianza, simétrica, semidefinida positiva, matriz de correlación.

📘 **Dónde se aprende** (1 clase): [B12-C18 · Matrices de covarianza](../programa/clases/B12/B12-C18-matrices-de-covarianza/CLASE.md).

### Factorización QR

- La factorización QR escribe `A = Q R` con `Q` de columnas ortonormales y `R` triangular superior.

💡 **Contexto en la clase [B10-C07](../programa/clases/B10/B10-C07-proyecciones-y-minimos-cuadrados/CLASE.md):**
- **Idea central (modelo mental):** Ajustar es proyectar el vector de datos sobre el conjunto de todas las curvas que el modelo puede describir; lo que sobra es perpendicular.
- 🎯 **Por qué importa:** Una estación mide la distancia a un satélite cada segundo durante diez segundos. Hay once medidas y solo tres parámetros que describir (posición, velocidad y aceleración radiales).
- 🔗 **Se estudia junto con:** proyección ortogonal, matriz de diseño, mínimos cuadrados, ecuaciones normales.

📘 **Dónde se aprende** (1 clase): [B10-C07 · Proyecciones y mínimos cuadrados](../programa/clases/B10/B10-C07-proyecciones-y-minimos-cuadrados/CLASE.md).

### Factorizar

- La propiedad distributiva dice `a(b + c) = ab + ac`. Factorizar es escribir una suma como un producto (`6a + 9 = 3(2a + 3)`).
- Una raíz es un valor de `x` que hace el polinomio igual a cero. Factorizar es escribir el polinomio como producto de polinomios de menor grado.

💡 **Cómo se explica en la clase [B03-C13](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md):**
- X --> S["Simplificar o factorizar si hace falta"]
- Factorizar un factor común y reconocer una diferencia de cuadrados.
- 🎯 **Por qué importa:** ¿Cuánto tarda una señal en llegar desde la Tierra hasta Marte? Depende de dónde estén los dos planetas.
- 🔗 **Se estudia junto con:** expresión algebraica, término, términos semejantes, coeficiente.

📘 **Dónde se aprende** (2 clases): [B03-C13 · Expresiones algebraicas iniciales](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md); [B04-C01 · Polinomios y factorización](../programa/clases/B04/B04-C01-polinomios-y-factorizacion/CLASE.md).

### FAIR

- La semilla fija la secuencia aleatoria. FAIR son las cuatro propiedades de los datos (localizables, accesibles, interoperables, reutilizables).

💡 **Cómo se explica en la clase [B124-C14](../programa/clases/B124/B124-C14-ciencia-abierta-y-reproducibilidad/CLASE.md):**
- Faltan, por ejemplo, el índice en un repositorio, los vocabularios controlados y los enlaces; los criterios son un ejemplo propio de la clase, no la lista oficial de FAIR.
- M["metadatos y licencia"] --> F["lista FAIR"]
- ⚠️ **Error frecuente:** Tomar los 12 criterios como la norma FAIR. Se corrige con 8.4.
- 🎯 **Por qué importa:** «Es reproducible» suele afirmarse sin evidencia. La decisión central: ¿qué hay que fijar y registrar para que un análisis dé el mismo resultado y se pueda comprobar?
- 🔗 **Se estudia junto con:** reproducibilidad, huella, semilla, procedencia.

📘 **Dónde se aprende** (1 clase): [B124-C14 · Ciencia abierta y reproducibilidad](../programa/clases/B124/B124-C14-ciencia-abierta-y-reproducibilidad/CLASE.md).

### Falla anular

- La falla anular es la fractura vertical que lo rodea.

💡 **Cómo se explica en la clase [B70-C03](../programa/clases/B70/B70-C03-calderas-planetarias-formacion-y-colapso/CLASE.md):**
- Resistencia de la falla anular: `2πR T τ`.
- *Descripción textual:* el volumen evacuado genera subpresión; si supera la resistencia de la falla anular el techo colapsa y el hundimiento sigue del balance de volumen.
- 🎯 **Por qué importa:** Evacuar magma no siempre hunde el techo. La decisión central: ¿cuánta subpresión resiste un techo y cuánto magma hay que sacar para vencerla?
- 🔗 **Se estudia junto con:** pistón, subpresión, balance de volumen.

📘 **Dónde se aprende** (1 clase): [B70-C03 · Calderas planetarias: formación y colapso](../programa/clases/B70/B70-C03-calderas-planetarias-formacion-y-colapso/CLASE.md).

### Falla común

- La falla común afecta igual a ambos núcleos.

💡 **Cómo se explica en la clase [B88-C25](../programa/clases/B88/B88-C25-redundancia-de-procesamiento-y-ejecucion-en-paralelo-lockstep/CLASE.md):**
- Mostrar que una falla común no se detecta.
- Ejercicio 11 · transferencia. Transferencia. ¿Qué falla común mitigarías con un retardo de reloj entre núcleos?
- ⚠️ **Error frecuente:** Ignorar las fallas comunes. Usa diversidad o retardos (ejercicio 11)
- 🎯 **Por qué importa:** Lockstep detecta fallos transitorios de un núcleo, pero no los corrige ni cubre causas comunes. La decisión central: ¿cada cuántos ciclos comparar, y qué fallas escapan?
- 🔗 **Se estudia junto con:** lockstep, intervalo de comparación, latencia.

📘 **Dónde se aprende** (1 clase): [B88-C25 · Redundancia de procesamiento y ejecución en paralelo (lockstep)](../programa/clases/B88/B88-C25-redundancia-de-procesamiento-y-ejecucion-en-paralelo-lockstep/CLASE.md).

### Falla de causa común

- La falla de causa común afecta a varios canales por un mismo motivo.

💡 **Cómo se explica en la clase [B97-C17](../programa/clases/B97/B97-C17-seguridad-funcional-robotica/CLASE.md):**
- Descripción larga: sin causa común, la redundancia reduce la probabilidad de falla en un orden de magnitud; con `β = 0,05` la mejora baja a `7,4` veces porque queda limitada por el piso `β p`.
- Incorporar la falla de causa común con un factor beta.
- 🎯 **Por qué importa:** Duplicar un canal parece bajar la probabilidad de falla al cuadrado; pero si una causa afecta a ambos, la mejora real es mucho menor. Calcularlo evita sobreestimar la seguridad de una arquitectura redundante.
- 🔗 **Se estudia junto con:** 1oo1, 1oo2, 2oo2, 2oo3.

📘 **Dónde se aprende** (1 clase): [B97-C17 · Seguridad funcional robótica](../programa/clases/B97/B97-C17-seguridad-funcional-robotica/CLASE.md).

### Falla de vuelo

- La falla de vuelo es la pérdida del vehículo antes de completar la trayectoria.

💡 **Cómo se explica en la clase [B121-C01](../programa/clases/B121/B121-C01-licencias-y-requisitos-nacionales-para-el-lanzamiento/CLASE.md):**
- Límites: zonas discretas, una sola falla, densidad uniforme; ignora el tiempo de exposición, los refugios y la dispersión real; no es un análisis de seguridad de vuelo.
- 🎯 **Por qué importa:** La autorización de un lanzamiento no es un trámite abstracto: incluye criterios numéricos de riesgo. La decisión central: ¿una trayectoria cumple el criterio de riesgo colectivo e individual que exige la licencia y con qué margen?
- 🔗 **Se estudia junto con:** licencia, riesgo colectivo, riesgo individual, zona de impacto.

📘 **Dónde se aprende** (1 clase): [B121-C01 · Licencias y requisitos nacionales para el lanzamiento](../programa/clases/B121/B121-C01-licencias-y-requisitos-nacionales-para-el-lanzamiento/CLASE.md).

### Falla en grupo

- Una falla en grupo afecta a varios satélites a la vez.

💡 **Cómo se explica en la clase [B124-C08](../programa/clases/B124/B124-C08-seguros-y-riesgo-espacial/CLASE.md):**
- *Descripción textual:* la probabilidad de falla da la pérdida esperada y la prima; la cola de pérdidas, agravada por las fallas en grupo, da la probabilidad de ruina, que se comprueba con una simulación.
- Descripción larga: con la misma pérdida esperada, las fallas en grupo multiplican la probabilidad de ruina y alargan la cola.
- 🎯 **Por qué importa:** El seguro no elimina el riesgo: lo traslada a quien puede juntarlo. La decisión central: ¿cuánto cobrar por cubrir un riesgo y con qué probabilidad el asegurador se queda sin capital?
- 🔗 **Se estudia junto con:** prima, pérdida esperada, recargo, capital.

📘 **Dónde se aprende** (1 clase): [B124-C08 · Seguros y riesgo espacial](../programa/clases/B124/B124-C08-seguros-y-riesgo-espacial/CLASE.md).

### Falla latente

- Resistencia de fuga: camino resistivo que permite disipar la carga lentamente. Falla latente: daño que no se manifiesta hasta después.

💡 **Contexto en la clase [B90-C03](../programa/clases/B90/B90-C03-proteccion-frente-a-esd/CLASE.md):**
- 🎯 **Por qué importa:** Un componente electrónico puede quedar con una falla latente tras una descarga que nadie sintió: una persona percibe una chispa solo por encima de unos miles de voltios (orden de magnitud no consultado), por encima de lo que puede dañar a un componente sensible.
- 🔗 **Se estudia junto con:** ESD, Modelo de cuerpo humano, Carga triboeléctrica, Resistencia de fuga.

📘 **Dónde se aprende** (1 clase): [B90-C03 · Protección frente a ESD](../programa/clases/B90/B90-C03-proteccion-frente-a-esd/CLASE.md).

### Fallo

- Un acierto (*hit*) es encontrar el dato en caché; un fallo (*miss*), tener que ir a un nivel inferior.
- El fallo es la distancia nominal entre centros.
- El fallo es cualquier caso sin solución, con excepción o con residuo mayor.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B30-C20](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md):**
- Un detector de humo muy sensible suena con las tostadas (falsas alarmas) y uno muy duro no suena con el incendio (fallos).
- pares de dias: 364 ; aciertos a = 12, falsas alarmas b = 24, fallos c = 6, negativos correctos d = 322
- 🎯 **Por qué importa:** Una alerta con muchas falsas alarmas se ignora y una con muchos fallos no sirve; medir ambas cosas es parte del oficio. La decisión central: ¿cómo se clasifica un evento y cómo se mide si una regla de alerta tiene habilidad?
- 🔗 **Se estudia junto con:** escala, acierto, falsa alarma, negativo correcto.

📘 **Dónde se aprende** (4 clases): [B18-C03 · Jerarquía y estructuras de memoria](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md); [B30-C20 · Análisis de alerta solar real](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md); [B76-C14 · Evasión de colisión](../programa/clases/B76/B76-C14-evasion-de-colision/CLASE.md); [B82-C07 · Benchmark entre solucionadores de Lambert](../programa/clases/B82/B82-C07-benchmark-entre-solucionadores-de-lambert/CLASE.md).

### Fallo de caché

- Un fallo de caché puede multiplicar el tiempo.

💡 **Cómo se explica en la clase [B88-C30](../programa/clases/B88/B88-C30-analisis-de-peor-caso-de-tiempo-de-ejecucion-wcet/CLASE.md):**
- Con factor de fallos de caché 1,5: `489` ciclos (`4,89 µs` a 100 MHz); con 2,0: `652`.
- Factor de fallos de cache 1.0 -> WCET = 326 ciclos = 3.26 us a 100 MHz
- 🎯 **Por qué importa:** El análisis de planificación (C05) necesita `C` de cada tarea, y medir no basta porque el peor camino puede no ejercitarse. La decisión central: ¿cuál es una cota segura del tiempo de ejecución y cuánto pesimismo trae?
- 🔗 **Se estudia junto con:** WCET, BCET, camino más largo, pesimismo.

📘 **Dónde se aprende** (1 clase): [B88-C30 · Análisis de peor caso de tiempo de ejecución (WCET)](../programa/clases/B88/B88-C30-analisis-de-peor-caso-de-tiempo-de-ejecucion-wcet/CLASE.md).

### Fallo silencioso

- Un fallo silencioso pasa sin detección.

💡 **Contexto en la clase [B88-C34](../programa/clases/B88/B88-C34-pruebas-de-inyeccion-de-fallos/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR O["Objetivo + FDIR"] --> I["Inyectar un bit al azar"] I --> R{"Detectado?"} R -->|si| D["Contar detectado"] R -->|no| S["Contar silencioso"] D --> C["Cobertura + IC de Wilson"] S --> C ``` *Descripción textual:* cada inyección cae en un bit al azar; el FDIR la detecta o no; los conteos dan la cobertura con su intervalo.
- 🎯 **Por qué importa:** Un FDIR no probado es una hipótesis. La decisión central: ¿cuántas inyecciones hacen falta para estimar la cobertura con una incertidumbre aceptable y qué fallas escapan?
- 🔗 **Se estudia junto con:** cobertura, intervalo de Wilson, campaña.

📘 **Dónde se aprende** (1 clase): [B88-C34 · Pruebas de inyección de fallos](../programa/clases/B88/B88-C34-pruebas-de-inyeccion-de-fallos/CLASE.md).

### Falsa aceptación (PFA)

- Banda de guarda `w`: margen que se resta al límite para aceptar. Falsa aceptación (PFA): aceptar una unidad realmente fuera de especificación.

💡 **Cómo se explica en la clase [B90-C08](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md):**
- Sin banda de guarda se acepta el 0,012 % de unidades malas y se rechaza el 0,019 % de buenas; con guarda `U` la falsa aceptación baja a 0,0003 % y el falso rechazo sube a 0,128 %.
- Descripción larga: al subir la banda de guarda la falsa aceptación se acerca a cero y el falso rechazo crece de 0,019 % a 0,37 %.
- 🎯 **Por qué importa:** Toda medida tiene incertidumbre. Si se acepta con el límite exacto, algunas unidades malas pasan; si se endurece el criterio, algunas buenas se rechazan y cuesta tiempo.
- 🔗 **Se estudia junto con:** Procedimiento de prueba, Tolerancia, Incertidumbre de medida, Banda de guarda w.

📘 **Dónde se aprende** (1 clase): [B90-C08 · Procedimientos de prueba funcional](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md).

### Falsa alarma

- Una falsa alarma es una detección que no corresponde a ninguna fuente; su tasa es la fracción de píxeles (o el número por imagen) que superan el umbral solo por ruido.
- Una falsa alarma es un punto normal señalado como anómalo.
- Un falso «seguro» es un peligro declarado transitable; una falsa alarma es una celda segura declarada peligrosa.
- *(y 8 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C12](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md):**
- Paso 6 · Falsas alarmas del umbral. `Q(4) = 3,17 × 10⁻⁵` por píxel: 1,3 por imagen de 40 000 píxeles.
- Predecir la tasa de falsas alarmas y la completitud para un umbral dado.
- ⚠️ **Error frecuente:** Reportar el catálogo sin completitud ni falsas alarmas. Se corrige con el ejercicio 12.
- 🎯 **Por qué importa:** Un catálogo de fuentes es el producto básico de una imagen astronómica, y de él salen cuentas, colores y candidatos a objetos nuevos. Si el umbral es bajo, el catálogo se llena de ruido; si es alto, se pierden las fuentes débiles.
- 🔗 **Se estudia junto con:** fondo, ruido, relación señal–ruido, filtro adaptado.

📘 **Dónde se aprende** (11 clases): [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B17-C05 · Detección de anomalías](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md); [B30-C20 · Análisis de alerta solar real](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md); [B48-C23 · Observabilidad del software de observatorio: registros, métricas y alertas](../programa/clases/B48/B48-C23-observabilidad-del-software-de-observatorio-registros-metricas-y-alertas/CLASE.md); [B88-C12 · Detección aislamiento y recuperación de fallos](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md); [B89-C24 · Recepción de telemetría débil](../programa/clases/B89/B89-C24-recepcion-de-telemetria-debil/CLASE.md) y 5 más.

### Falsa marca

- La falsa marca y la detección.

💡 **Cómo se explica en la clase [B51-C13](../programa/clases/B51/B51-C13-marcado-de-datos-espurios-e-interferencia-en-visibilidades/CLASE.md):**
- Umbral 3,5 σ robusta en 819200 muestras: falsas marcas 0,0426 %; gaussiana `erfc(χ/√2)` = 0,0465 %.
- F --> V["verdad: detección y falsas marcas"]
- ⚠️ **Error frecuente:** Fijar un umbral sin calcular las falsas marcas. Se corrige con 8.1.
- 🎯 **Por qué importa:** Dejar RFI en los datos degrada la imagen; marcar demasiado pierde señal. La decisión central: ¿qué umbral marca la interferencia sin marcar el ruido, y cómo se detecta la interferencia débil y extendida?
- 🔗 **Se estudia junto con:** interferencia, mediana, MAD, σ robusta.

📘 **Dónde se aprende** (1 clase): [B51-C13 · Marcado de datos espurios e interferencia en visibilidades](../programa/clases/B51/B51-C13-marcado-de-datos-espurios-e-interferencia-en-visibilidades/CLASE.md).

### Falsable

- Una hipótesis es falsable si existe al menos un resultado posible que la contradiga.

💡 **Cómo se explica en la clase [B01-C07](../programa/clases/B01/B01-C07-hipotesis-y-predicciones-falsables/CLASE.md):**
- Ejercicio 2 · con una pista. ¿Es falsable «la Luna cambia de tamaño porque sí»?
- Ejercicio 5. Reescribe como hipótesis falsable: «el Sol sale a distinta hora cada día».
- 🎯 **Por qué importa:** Una afirmación que ningún resultado posible contradice no enseña nada. Si dices «la Luna cambia de tamaño aparente» y, ocurra lo que ocurra, tu frase queda a salvo, no has dicho gran cosa.
- 🔗 **Se estudia junto con:** hipótesis, predicción, hipótesis alternativa, criterio de refutación.

📘 **Dónde se aprende** (1 clase): [B01-C07 · Hipótesis y predicciones falsables](../programa/clases/B01/B01-C07-hipotesis-y-predicciones-falsables/CLASE.md).

### Falso color

- Una composición asigna bandas a los canales rojo, verde y azul de la pantalla; la de falso color usa el infrarrojo cercano.

💡 **Cómo se explica en la clase [B57-C05](../programa/clases/B57/B57-C05-imagenes-multiespectrales/CLASE.md):**
- Por color: composiciones RGB y de falso color.
- Ejercicio 7. Describe en una frase qué es una composición de falso color.
- ⚠️ **Error frecuente:** Confundir falso color con color real. Se corrige con 6.
- 🎯 **Por qué importa:** Con una sola banda el agua oscura, la sombra y el asfalto se confunden; con varias, cada cubierta deja una firma distinta. La decisión central: ¿qué combinación de bandas separa las cubiertas que me interesan y cómo recupero detalle espacial sin falsear los colores?
- 🔗 **Se estudia junto con:** banda, composición, razón de bandas, fusión pancromática.

📘 **Dónde se aprende** (1 clase): [B57-C05 · Imágenes multiespectrales](../programa/clases/B57/B57-C05-imagenes-multiespectrales/CLASE.md).

### Falso disparo

- Vigilante (*watchdog*): dispara una parada si faltan latidos. Falso disparo: parada sin falla real.

💡 **Cómo se explica en la clase [B48-C09](../programa/clases/B48/B48-C09-control-remoto-de-telescopios/CLASE.md):**
- Subir `k` de 3 a 4 divide los falsos disparos por 10, pero añade 1 s a la parada.
- *Descripción textual:* el retardo viene de la distancia y el índice; el vigilante dispara tras k pérdidas seguidas y su tasa de falsos disparos y su tiempo de parada dependen de k.
- 🎯 **Por qué importa:** Un vigilante muy sensible detiene la observación sin motivo y uno muy lento no protege. La decisión central: ¿tras cuántos latidos perdidos hay que disparar la parada?
- 🔗 **Se estudia junto con:** Retardo de propagación, Latido, Vigilante, Tiempo de parada.

📘 **Dónde se aprende** (1 clase): [B48-C09 · Control remoto de telescopios](../programa/clases/B48/B48-C09-control-remoto-de-telescopios/CLASE.md).

### Falso negativo

- Un falso positivo es una alarma sin error real; un falso negativo, un error que pasa inadvertido.

💡 **Cómo se explica en la clase [B14-C10](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md):**
- Muy alto, no suena con errores reales (falsos negativos).
- 🎯 **Por qué importa:** Cambias una línea de un propagador orbital «solo para ordenarlo» y el período de una órbita pasa de 5553,624562 s a 5553,627342 s (situación ilustrativa con cifras de esta clase). ¿Es un error o ruido?
- 🔗 **Se estudia junto con:** prueba de regresión, valor de referencia, tolerancia relativa, absoluta.

📘 **Dónde se aprende** (1 clase): [B14-C10 · Pruebas de regresión numérica](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md).

### Falso positivo

- Un falso positivo es una alarma sin error real; un falso negativo, un error que pasa inadvertido.
- Un falso positivo es declarar un efecto que no existe.
- Un falso positivo es un píxel marcado que no es objeto.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C10](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md):**
- Muy bajo, suena con el redondeo (falsos positivos).
- 🎯 **Por qué importa:** Cambias una línea de un propagador orbital «solo para ordenarlo» y el período de una órbita pasa de 5553,624562 s a 5553,627342 s (situación ilustrativa con cifras de esta clase). ¿Es un error o ruido?
- 🔗 **Se estudia junto con:** prueba de regresión, valor de referencia, tolerancia relativa, absoluta.

📘 **Dónde se aprende** (8 clases): [B14-C10 · Pruebas de regresión numérica](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md); [B14-C23 · Protocolo preregistrado de análisis](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md); [B15-C13 · Segmentación de imágenes](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md); [B20-C02 · Diseño de un plan de análisis y preregistro](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md); [B29-C08 · Falsos positivos de tránsito](../programa/clases/B29/B29-C08-falsos-positivos-de-transito/CLASE.md); [B56-C13 · Biofirmas químicas](../programa/clases/B56/B56-C13-biofirmas-quimicas/CLASE.md) y 2 más.

### Falso rechazo (PFR)

- Falsa aceptación (PFA): aceptar una unidad realmente fuera de especificación. Falso rechazo (PFR): rechazar una unidad conforme.

💡 **Cómo se explica en la clase [B90-C08](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md):**
- Sin banda de guarda se acepta el 0,012 % de unidades malas y se rechaza el 0,019 % de buenas; con guarda `U` la falsa aceptación baja a 0,0003 % y el falso rechazo sube a 0,128 %.
- Descripción larga: al subir la banda de guarda la falsa aceptación se acerca a cero y el falso rechazo crece de 0,019 % a 0,37 %.
- 🎯 **Por qué importa:** Toda medida tiene incertidumbre. Si se acepta con el límite exacto, algunas unidades malas pasan; si se endurece el criterio, algunas buenas se rechazan y cuesta tiempo.
- 🔗 **Se estudia junto con:** Procedimiento de prueba, Tolerancia, Incertidumbre de medida, Banda de guarda w.

📘 **Dónde se aprende** (1 clase): [B90-C08 · Procedimientos de prueba funcional](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md).

### Falso «seguro»

- Un falso «seguro» es un peligro declarado transitable; una falsa alarma es una celda segura declarada peligrosa.

💡 **Cómo se explica en la clase [B103-C04](../programa/clases/B103/B103-C04-deteccion-de-obstaculos-y-mapas-de-traversabilidad/CLASE.md):**
- El clasificador bruto produce falsas alarmas del 5,3 % (0–5 m), 45,4 % (5–10 m), 99,4 % (10–15 m) y 100 % (15–20 m), con muy pocos falsos «seguro»: 22, 5, 0 y 0.
- Las falsas alarmas caen a 0,0 %, 0,3 %, 0,6 % y 12,7 %, pero los falsos «seguro» suben a 526, 1937, 4182 y 2477 celdas (8,5 %, 36,6 %, 72,9 % y 50,5 % de los peligros de cada banda).
- ⚠️ **Error frecuente:** Evaluar solo la exactitud global. Mira falsos «seguro» y falsas alarmas por separado y por rango (8.3, 8.4).
- 🎯 **Por qué importa:** El ruido del MDE crece con el cuadrado del rango y, a partir de cierta distancia, la señal de un obstáculo queda por debajo del ruido. La decisión central: ¿hasta qué rango se puede clasificar el terreno de forma útil, y qué política (conservadora o corregida) elegir más allá?
- 🔗 **Se estudia junto con:** pendiente, escalón, rugosidad, traversabilidad.

📘 **Dónde se aprende** (1 clase): [B103-C04 · Detección de obstáculos y mapas de traversabilidad](../programa/clases/B103/B103-C04-deteccion-de-obstaculos-y-mapas-de-traversabilidad/CLASE.md).

### Falsos negativos

- La matriz de confusión cuenta aciertos y errores: verdaderos positivos (TP), falsos positivos (FP), verdaderos negativos (TN) y falsos negativos (FN) (S2).

💡 **Cómo se explica en la clase [B17-C12](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md):**
- Ambos extremos se convierten en un costo (falsos positivos por su costo más falsos negativos por el suyo), y se elige el umbral de costo mínimo.
- Si es muy sensible, suena al tostar pan (falsos positivos); si es poco sensible, no suena en un incendio lento (falsos negativos).
- 🎯 **Por qué importa:** Un modelo marca candidatos a planeta, y cada alerta cuesta horas de revisión. Si el modelo acierta el 99 % en una muestra donde el 99 % son negativos, no dice nada útil.
- 🔗 **Se estudia junto con:** matriz de confusión, verdaderos positivos, falsos positivos, verdaderos negativos.

📘 **Dónde se aprende** (1 clase): [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md).

### Falsos positivos

- La matriz de confusión cuenta aciertos y errores: verdaderos positivos (TP), falsos positivos (FP), verdaderos negativos (TN) y falsos negativos (FN) (S2).

💡 **Cómo se explica en la clase [B17-C12](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md):**
- La curva ROC no cambia con la prevalencia, porque usa tasas dentro de cada clase; la de precisión–exhaustividad sí, y por eso refleja la carga de falsos positivos.
- Si cada falso positivo cuesta 1 unidad y cada real perdido 50, el costo es `FP + 50 FN`.
- 🎯 **Por qué importa:** Un modelo marca candidatos a planeta, y cada alerta cuesta horas de revisión. Si el modelo acierta el 99 % en una muestra donde el 99 % son negativos, no dice nada útil.
- 🔗 **Se estudia junto con:** matriz de confusión, verdaderos positivos, verdaderos negativos, falsos negativos.

📘 **Dónde se aprende** (1 clase): [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md).

### Falta de fusión

- La falta de fusión ocurre con `E_v` bajo y el exceso de energía (ojo de cerradura) con `E_v` alto.

💡 **Cómo se explica en la clase [B84-C15](../programa/clases/B84/B84-C15-manufactura-aditiva/CLASE.md):**
- B --> C["falta de fusion / ventana / exceso"]
- 🎯 **Por qué importa:** Dos piezas idénticas con otra velocidad de barrido pueden salir porosas; una ventana de proceso bien trazada evita el desperdicio, y la rugosidad escalonada decide qué superficies se mecanizan. La decisión central: ¿con qué potencia y velocidad se imprime dentro de la ventana y cuánto tarda y qué acabado deja?
- 🔗 **Se estudia junto con:** densidad de energía volumétrica, exceso de energía, efecto escalera, separación entre pasadas.

📘 **Dónde se aprende** (1 clase): [B84-C15 · Manufactura aditiva](../programa/clases/B84/B84-C15-manufactura-aditiva/CLASE.md).

### Familia Runge–Kutta

- La familia Runge–Kutta agrupa métodos de este tipo con distinto número de etapas.

💡 **Contexto en la clase [B11-C07](../programa/clases/B11/B11-C07-runge-kutta-de-cuarto-orden/CLASE.md):**
- **Idea central (modelo mental):** RK4 sondea la pendiente en el inicio, dos veces en el medio (con dos estimaciones distintas del estado medio) y en el final, y luego pondera: los puntos medios pesan el doble. Es una regla de Simpson aplicada a la dirección del movimiento.
- 🎯 **Por qué importa:** La mayoría de los programas de simulación científica usa, de forma directa o como base, un método de la familia Runge–Kutta. Entender RK4 permite leer cualquier código de propagación, estimar cuántos pasos necesita una órbita y saber en qué punto empieza a ser conveniente algo más sofisticado.
- 🔗 **Se estudia junto con:** método RK4 clásico, etapa, punto medio, orden p.

📘 **Dónde se aprende** (1 clase): [B11-C07 · Runge-Kutta de cuarto orden](../programa/clases/B11/B11-C07-runge-kutta-de-cuarto-orden/CLASE.md).

### Familia tangencial

- La familia tangencial es el conjunto de elipses que salen tangentes.

💡 **Cómo se explica en la clase [B75-C22](../programa/clases/B75/B75-C22-modelos-de-primer-impulso/CLASE.md):**
- Leer la familia tangencial `Δv` → apoapsis → tiempo de vuelo.
- El script [primer_impulso.py](primer_impulso.py) calcula la familia tangencial y comprueba que el `Δv` mínimo coincide con Hohmann por bisección, que `φ = 0` maximiza el apoapsis y que el tiempo coincide con la propagación de Kepler.
- 🎯 **Por qué importa:** Antes de optimizar toda la misión conviene entender el primer impulso. La decisión central: ¿qué módulo y qué dirección del primer impulso alcanzan un radio dado con el menor delta-v y en cuánto tiempo?
- 🔗 **Se estudia junto con:** primer impulso, dirección, apoapsis alcanzado, tiempo hasta el apoapsis.

📘 **Dónde se aprende** (1 clase): [B75-C22 · Modelos de primer impulso](../programa/clases/B75/B75-C22-modelos-de-primer-impulso/CLASE.md).

### Familia variacional

- Una familia variacional es el conjunto de distribuciones permitidas (por ejemplo, gaussianas con media `m` y desviación `s`).

💡 **Cómo se explica en la clase [B19-C05](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md):**
- Imagina la posterior como un objeto en 3D y la familia variacional como una pantalla en la que solo caben ciertas formas.
- *Descripción textual:* la KL mide la distancia entre la familia sencilla y la posterior difícil; se maximiza el ELBO sobre los parámetros variacionales `φ`; el resultado `q*` se somete a comprobaciones de cobertura y de comparación con MCMC.
- 🎯 **Por qué importa:** Con miles de parámetros o millones de datos, un muestreador puede tardar horas o días. La inferencia variacional (VI) elige una familia de distribuciones manejables, por ejemplo gaussianas, y busca dentro de ella la más cercana a la posterior.
- 🔗 **Se estudia junto con:** divergencia de Kullback–Leibler, aproximación variacional, ELBO, campo medio.

📘 **Dónde se aprende** (1 clase): [B19-C05 · Inferencia variacional](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md).

### Fantasma

- Un fantasma es una imagen de un objeto brillante producida por dos reflexiones internas.

💡 **Cómo se explica en la clase [B50-C05](../programa/clases/B50/B50-C05-luz-parasita-y-analisis-de-rayos-dispersos/CLASE.md):**
- El fantasma pasa por dos reflexiones, así que su potencia relativa es `R₁R₂ = 1,60 × 10⁻³` sin recubrir y `1,00 × 10⁻⁴` con `R = 0,01`: el recubrimiento reduce el fantasma 16 veces.
- El foco del fantasma por la matriz paraxial es `z = 15,22505 mm` y por el trazado exacto `15,22505 mm`; la imagen real está en `103,3289 mm`.
- ⚠️ **Error frecuente:** Olvidar que el fantasma está desenfocado. Se corrige con 8.2.
- 🎯 **Por qué importa:** El contraste de un instrumento no depende solo de la imagen: depende de cuánta luz llega por caminos no deseados. La decisión central: ¿qué fracción de luz llega por un camino parásito y cómo se reduce?
- 🔗 **Se estudia junto con:** reflectancia de Fresnel, lambertiana, factor de vista, deflector.

📘 **Dónde se aprende** (1 clase): [B50-C05 · Luz parásita y análisis de rayos dispersos](../programa/clases/B50/B50-C05-luz-parasita-y-analisis-de-rayos-dispersos/CLASE.md).

### FAR

- El POD es la fracción de eventos detectados, el FAR la de alertas falsas y el CSI la de aciertos sobre todos los casos relevantes.
- El POD, el FAR y el Heidke.

💡 **Cómo se explica en la clase [B30-C20](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md):**
- *Descripción textual:* las medidas se convierten en escalas G, S y R; la regla y lo observado forman la tabla de contingencia, de la que salen POD, FAR y Heidke.
- Calcular POD, FAR, CSI y la puntuación de Heidke por dos fórmulas.
- 🎯 **Por qué importa:** Una alerta con muchas falsas alarmas se ignora y una con muchos fallos no sirve; medir ambas cosas es parte del oficio. La decisión central: ¿cómo se clasifica un evento y cómo se mide si una regla de alerta tiene habilidad?
- 🔗 **Se estudia junto con:** escala, acierto, falsa alarma, fallo.

📘 **Dónde se aprende** (2 clases): [B30-C20 · Análisis de alerta solar real](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md); [B33-C13 · Pronóstico de actividad geomagnética](../programa/clases/B33/B33-C13-pronostico-de-actividad-geomagnetica/CLASE.md).

### Fase

- La fase es la parte del disco lunar iluminada que vemos.
- La fase es la fracción del disco lunar que ves iluminada; se da como porcentaje de 0 % (nueva) a 100 % (llena).
- Una fase es un estado del gas con un rango de temperatura y densidad.
- *(y 13 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C12](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md):**
- No es la sombra de la Tierra: esa sombra solo cae sobre la Luna en un eclipse lunar, que es raro, y las fases ocurren todos los meses.
- Paso 6 · Comprobación. Observa la fase cada noche cerca de la fecha; anota la noche en que el disco se ve completo; compara con la predicción y con una tabla publicada que cites.
- ⚠️ **Error frecuente:** Atribuir las fases a la sombra de la Tierra. Ejercicio 8.
- 🎯 **Por qué importa:** La Luna es el reloj más a mano del cielo: cada noche cambia, y cada 29,5 días vuelve a empezar. Pero «a mano» no significa «fácil de explicar»: muchas personas creen que las fases son la sombra de la Tierra sobre la Luna.
- 🔗 **Se estudia junto con:** luna nueva, luna llena, cuartos, edad.

📘 **Dónde se aprende** (17 clases): [B01-C12 · Fases lunares y ciclos celestes](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md); [B05-C11 · Movimiento oscilatorio](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md); [B08-C08 · Fases lunares y libración](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md); [B25-C03 · Medio interestelar multifásico](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md); [B29-C06 · Imagen directa de exoplanetas](../programa/clases/B29/B29-C06-imagen-directa-de-exoplanetas/CLASE.md); [B42-C06 · Función de dispersión puntual](../programa/clases/B42/B42-C06-funcion-de-dispersion-puntual/CLASE.md) y 11 más.

### Fase CC

- La fase CC mantiene la corriente; la fase CV mantiene la tensión máxima.

💡 **Cómo se explica en la clase [B86-C06](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md):**
- La fase CV termina en la corriente de corte y repone `1,314 Ah` de los `1,399 Ah` (quedan `0,084 Ah`, que se recuperan en la órbita siguiente o con un corte más bajo).
- Más corriente acorta la fase CC pero eleva la pérdida `I²R` y deja una fase CV proporcionalmente más larga (`89 %` del tiempo es CC con `1 A`).
- ⚠️ **Error frecuente:** Cargar siempre a tensión máxima sin fase CV. Se corrige con 8.1.
- 🎯 **Por qué importa:** Cargar más rápido reduce el tiempo pero eleva el calor y la tensión sobre la celda; cargar más lento puede no completar el ciclo antes del siguiente eclipse. El perfil de carga decide si la batería vuelve a su estado de carga en cada órbita.
- 🔗 **Se estudia junto con:** fase CV, corriente de corte, tasa C, eficiencia de energía.

📘 **Dónde se aprende** (1 clase): [B86-C06 · Gestión de carga](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md).

### Fase crítica

- La fase crítica es la de menor margen.

💡 **Cómo se explica en la clase [B86-C19](../programa/clases/B86/B86-C19-presupuesto-de-potencia-de-mision/CLASE.md):**
- *Descripción textual:* los subsistemas, con su crecimiento por madurez y la reserva de sistema, dan la demanda por fase y la potencia de ala requerida; con la generación de cada fase resultan los márgenes y la fase crítica; un Monte Carlo del crecimiento estima la probabilidad de exceso.
- Obtener el margen de cada fase y encontrar la fase crítica.
- 🎯 **Por qué importa:** Un presupuesto es un compromiso de ingeniería: cada subsistema promete una potencia que todavía puede crecer. Las reservas por madurez evitan que el ala quede corta cuando una carga nueva consume más de lo previsto.
- 🔗 **Se estudia junto con:** crecimiento por madurez, reserva de sistema, fase, margen.

📘 **Dónde se aprende** (1 clase): [B86-C19 · Presupuesto de potencia de misión](../programa/clases/B86/B86-C19-presupuesto-de-potencia-de-mision/CLASE.md).

### Fase CV

- La fase CC mantiene la corriente; la fase CV mantiene la tensión máxima.

💡 **Cómo se explica en la clase [B86-C06](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md):**
- La fase CV termina en la corriente de corte y repone `1,314 Ah` de los `1,399 Ah` (quedan `0,084 Ah`, que se recuperan en la órbita siguiente o con un corte más bajo).
- Más corriente acorta la fase CC pero eleva la pérdida `I²R` y deja una fase CV proporcionalmente más larga (`89 %` del tiempo es CC con `1 A`).
- ⚠️ **Error frecuente:** Cargar siempre a tensión máxima sin fase CV. Se corrige con 8.1.
- 🎯 **Por qué importa:** Cargar más rápido reduce el tiempo pero eleva el calor y la tensión sobre la celda; cargar más lento puede no completar el ciclo antes del siguiente eclipse. El perfil de carga decide si la batería vuelve a su estado de carga en cada órbita.
- 🔗 **Se estudia junto con:** fase CC, corriente de corte, tasa C, eficiencia de energía.

📘 **Dónde se aprende** (1 clase): [B86-C06 · Gestión de carga](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md).

### Fase de cierre

- La fase de cierre `arg(V_ij V_jk V_ki)`.
- La fase de cierre (suma de fases en un triángulo).

💡 **Cómo se explica en la clase [B46-C17](../programa/clases/B46/B46-C17-calibracion-de-fase/CLASE.md):**
- *Descripción textual:* las ganancias de antena se estiman de un calibrador y se interpolan en el tiempo; el cierre de fase es el invariante de comprobación.
- Con errores de fase de 60° rms y un calibrador de 1 Jy, el cierre sin ruido es `1,7 × 10^-16 rad`; la solución recupera las fases con un error máximo de `2,65°`.
- 🎯 **Por qué importa:** Sin calibrar, la fase de la visibilidad no contiene el cielo. La decisión central: ¿cada cuánto hay que observar el calibrador para que el residuo no destruya la coherencia?
- 🔗 **Se estudia junto con:** ganancia compleja, solución de ganancias, referencia de fase, marcha aleatoria.

📘 **Dónde se aprende** (2 clases): [B46-C17 · Calibración de fase](../programa/clases/B46/B46-C17-calibracion-de-fase/CLASE.md); [B51-C02 · Cantidades de cierre: fase y amplitud de cierre](../programa/clases/B51/B51-C02-cantidades-de-cierre-fase-y-amplitud-de-cierre/CLASE.md).

### Fase de oscilación

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B28-C03](../programa/clases/B28/B28-C03-neutrinos-astrofisicos/CLASE.md):**
- Si la fase total es enorme, solo importa el promedio y desaparecen las oscilaciones finas: queda un reparto fijo entre sabores.
- Para ese `E` y distancias de gigaparsecs, la fase de oscilación solar (con `Δm² = 7,4 × 10⁻⁵ eV²`, ilustrativo) es `~10¹³ rad`: la oscilación se promedia.
- 🎯 **Por qué importa:** Un detector que ve neutrinos muónicos de una fuente lejana no ve lo que salió de ella. Para interpretar la razón de sabores hay que conocer la mezcla.
- 🔗 **Se estudia junto con:** sabor, autoestado de masa, matriz de mezcla, probabilidad promediada.

📘 **Dónde se aprende** (1 clase): [B28-C03 · Neutrinos astrofísicos](../programa/clases/B28/B28-C03-neutrinos-astrofisicos/CLASE.md).

### Fase de recuperación

- La fase de recuperación es el decaimiento.

💡 **Contexto en la clase [B30-C18](../programa/clases/B30/B30-C18-tormentas-geomagneticas/CLASE.md):**
- **Idea central (modelo mental):** Como una bañera con grifo y desagüe: mientras el grifo vierte (inyección) el nivel baja hasta un equilibrio; al cerrarlo, el nivel se recupera exponencialmente.
- 🎯 **Por qué importa:** Prever la profundidad y la duración de una tormenta orienta la protección de redes y satélites. La decisión central: ¿qué mínimo alcanza `Dst*` y cuánto tarda en recuperarse?
- 🔗 **Se estudia junto con:** fase principal, tiempo de decaimiento, mínimo, escala G.

📘 **Dónde se aprende** (1 clase): [B30-C18 · Tormentas geomagnéticas](../programa/clases/B30/B30-C18-tormentas-geomagneticas/CLASE.md).

### Fase geométrica

- Acoplamiento: el movimiento del brazo mueve la base. Fase geométrica: giro neto de un lazo cerrado en el espacio articular.

💡 **Cómo se explica en la clase [B101-C06](../programa/clases/B101/B101-C06-simulacion-de-un-brazo-robotico-espacial/CLASE.md):**
- Reconocer el giro neto de la base por un lazo articular cerrado y que es una fase geométrica (independiente de la velocidad).
- ⚠️ **Error frecuente:** Creer que el giro depende de la velocidad. Es una fase geométrica (8.3)
- 🎯 **Por qué importa:** En una estación o un satélite pesado la base casi no se mueve; en un satélite pequeño, sí. La decisión central: ¿cuánto se mueve la base al mover el brazo y cómo afecta eso a la posición del extremo?
- 🔗 **Se estudia junto con:** Base libre, Acoplamiento, Lazo, RK4.

📘 **Dónde se aprende** (1 clase): [B101-C06 · Simulación de un brazo robótico espacial](../programa/clases/B101/B101-C06-simulacion-de-un-brazo-robotico-espacial/CLASE.md).

### Fase interferométrica

- La fase interferométrica es `φ = 4πd/λ` para un desplazamiento `d` en la LOS (el factor 4π incluye ida y vuelta).

💡 **Cómo se explica en la clase [B57-C08](../programa/clases/B57/B57-C08-interferometria-radar-insar/CLASE.md):**
- Convertir fase interferométrica en desplazamiento en la línea de visión y viceversa.
- 🎯 **Por qué importa:** El radar es la única herramienta orbital que mide movimientos del suelo de milímetros a escala regional, pero la fase solo se conoce módulo `2π`. La decisión central: ¿cuándo se puede reconstruir el desplazamiento y cuándo el desenrollado de la fase deja de ser fiable?
- 🔗 **Se estudia junto con:** franja, desenrollado, coherencia, línea base temporal.

📘 **Dónde se aprende** (1 clase): [B57-C08 · Interferometría radar InSAR](../programa/clases/B57/B57-C08-interferometria-radar-insar/CLASE.md).

### Fase mínima

- La fase mínima `Δφ_min = 1/√N_fot`.

💡 **Cómo se explica en la clase [B28-C06](../programa/clases/B28/B28-C06-interferometros-gravitacionales/CLASE.md):**
- Para `h = 10⁻²¹`: `ΔL = 4 × 10⁻¹⁸ m` y `Δφ = 1,417 × 10⁻⁸ rad`, `328` veces la fase mínima.
- *Descripción textual:* la deformación y los parámetros ópticos dan la fase producida; la potencia y el tiempo dan el número de fotones y la fase mínima; su cociente indica si la señal es detectable y de ahí sale `h_min`.
- 🎯 **Por qué importa:** Un detector que mide `10⁻¹⁹ m` necesita muchos fotones y cavidades que multipliquen el efecto. La decisión central: ¿qué fase produce una onda, qué fase mínima permite el ruido de disparo y cómo se mejora la sensibilidad?
- 🔗 **Se estudia junto con:** puerto oscuro, ruido de disparo, ganancia de cavidad, deformación mínima.

📘 **Dónde se aprende** (1 clase): [B28-C06 · Interferómetros gravitacionales](../programa/clases/B28/B28-C06-interferometros-gravitacionales/CLASE.md).

### Fase principal

- La fase principal es la de inyección.

💡 **Cómo se explica en la clase [B30-C18](../programa/clases/B30/B30-C18-tormentas-geomagneticas/CLASE.md):**
- Con la inyección ilustrativa `Q₀ = 15 nT/h`, `τ = 8 h` y fase principal de `T = 6 h`, el mínimo es `−63,32 nT`.
- 🎯 **Por qué importa:** Prever la profundidad y la duración de una tormenta orienta la protección de redes y satélites. La decisión central: ¿qué mínimo alcanza `Dst*` y cuánto tarda en recuperarse?
- 🔗 **Se estudia junto con:** fase de recuperación, tiempo de decaimiento, mínimo, escala G.

📘 **Dónde se aprende** (1 clase): [B30-C18 · Tormentas geomagnéticas](../programa/clases/B30/B30-C18-tormentas-geomagneticas/CLASE.md).

### Fase requerida

- La fase requerida es `φ = π − n_t t_T`.

💡 **Cómo se explica en la clase [B76-C10](../programa/clases/B76/B76-C10-encuentro-orbital/CLASE.md):**
- *Descripción textual:* de los radios sale el Hohmann y su tiempo; con el tiempo y el movimiento del objetivo sale la fase requerida; la espera se calcula con la diferencia de movimientos medios y la integración comprueba la llegada.
- Ejercicio 7 · autónomo. Convierte la fase requerida a kilómetros de arco a `6778 km`.
- 🎯 **Por qué importa:** Si la fase es incorrecta, la nave llega al lugar correcto cuando el objetivo ya pasó. La decisión central: ¿qué ángulo de fase debe haber al inicio y cuánto hay que esperar para lograrlo?
- 🔗 **Se estudia junto con:** ángulo de fase, periodo sinódico, tiempo de espera.

📘 **Dónde se aprende** (1 clase): [B76-C10 · Encuentro orbital](../programa/clases/B76/B76-C10-encuentro-orbital/CLASE.md).

### Fase vertical

- La fase vertical inicial permite despejar la torre y ganar velocidad.

💡 **Cómo se explica en la clase [B77-C12](../programa/clases/B77/B77-C12-perfil-de-ascenso-orbital/CLASE.md):**
- V["fase vertical 10 s"] --> K["gamma0 = 85 grados"]
- *Descripción textual:* una fase vertical, un giro a `85°`, la etapa 1 en giro de gravedad, la separación y la etapa 2 con desvío del empuje que cierra `γ = 0`; al agotarse, la vis-viva da perigeo y apogeo.
- 🎯 **Por qué importa:** La trayectoria de ascenso decide a la vez las pérdidas, las cargas y la órbita alcanzada. La decisión central: ¿qué perfil de inclinación lleva al vehículo a una órbita casi circular y qué cuesta?
- 🔗 **Se estudia junto con:** giro de gravedad, ángulo de la trayectoria, agotamiento, ecuación vis-viva.

📘 **Dónde se aprende** (1 clase): [B77-C12 · Perfil de ascenso orbital](../programa/clases/B77/B77-C12-perfil-de-ascenso-orbital/CLASE.md).

### Fases

- Las fases de ejemplo son: lanzamiento y primeras órbitas, puesta en servicio, operaciones nominales y fin de vida.

💡 **Cómo se explica en la clase [B83-C03](../programa/clases/B83/B83-C03-concepto-de-operaciones-conops/CLASE.md):**
- El CONOPS de ejemplo tiene cuatro fases: lanzamiento y primeras órbitas (7 d), puesta en servicio (30 d), operaciones nominales (3 años) y fin de vida (90 d).
- F["Fases y modos"] --> O["Orbita y estacion"]
- 🎯 **Por qué importa:** Los requisitos de datos, energía y operaciones dependen de cuántas veces al día se puede hablar con el satélite y por cuánto tiempo. La decisión central: ¿cuánto contacto real ofrece la órbita y cómo se reparte en las fases de la misión?
- 🔗 **Se estudia junto con:** CONOPS, modo, pase, hueco.

📘 **Dónde se aprende** (1 clase): [B83-C03 · Concepto de operaciones CONOPS](../programa/clases/B83/B83-C03-concepto-de-operaciones-conops/CLASE.md).

### Fases de Venus

- Las fases de Venus son los cambios de la porción iluminada de Venus vista desde la Tierra.

💡 **Contexto en la clase [B02-C13](../programa/clases/B02/B02-C13-galileo-y-primeras-observaciones-telescopicas/CLASE.md):**
- **Idea central (modelo mental):** Cada observación de Galileo sigue el mismo ciclo.
- 🎯 **Por qué importa:** Un instrumento nuevo da datos nuevos, pero los datos nuevos no se interpretan solos. La pregunta motivadora es: ¿qué podía concluir Galileo de lo que veía, y qué le faltaba para convencer a quienes no creían?
- 🔗 **Se estudia junto con:** telescopio refractor, ampliación, campo de visión, satélites galileanos.

📘 **Dónde se aprende** (1 clase): [B02-C13 · Galileo y primeras observaciones telescópicas](../programa/clases/B02/B02-C13-galileo-y-primeras-observaciones-telescopicas/CLASE.md).

### Fatiga

- La aptitud es `k₁ Σ w e^(−(t−s)/τ₁)` y la fatiga `k₂ Σ w e^(−(t−s)/τ₂)`.
- La fatiga es la pérdida de profundidad con el tiempo.
- La fatiga sube más por unidad de carga pero decae rápido (`τ2`).

💡 **Cómo se explica en la clase [B104-C04](../programa/clases/B104/B104-C04-acondicionamiento-fisico-general/CLASE.md):**
- Cada sesión suma una exponencial lenta de aptitud y una rápida de fatiga.
- A --> R["rendimiento = aptitud − fatiga"]
- ⚠️ **Error frecuente:** Olvidar que la fatiga decae rápido. Usa `τ₂` (8.2).
- 🎯 **Por qué importa:** Entrenar más no siempre significa rendir más el día que importa. La decisión central: ¿cómo distribuir una misma carga total para llegar con la mejor combinación de aptitud y fatiga?
- 🔗 **Se estudia junto con:** carga, aptitud, rendimiento, TRIMP.

📘 **Dónde se aprende** (3 clases): [B104-C04 · Acondicionamiento físico general](../programa/clases/B104/B104-C04-acondicionamiento-fisico-general/CLASE.md); [B107-C01 · Entrenamiento cardiorrespiratorio y de resistencia de astronautas](../programa/clases/B107/B107-C01-entrenamiento-cardiorrespiratorio-y-de-resistencia-de-astronautas/CLASE.md); [B117-C01 · Primeros auxilios y procedimientos básicos en entorno espacial](../programa/clases/B117/B117-C01-primeros-auxilios-y-procedimientos-basicos-en-entorno-espacial/CLASE.md).

### Fatiga de alarmas

- La fatiga de alarmas es la desensibilización de quien recibe demasiadas alarmas poco útiles.

💡 **Cómo se explica en la clase [B116-C05](../programa/clases/B116/B116-C05-alertas-de-salud-y-umbrales-de-monitorizacion/CLASE.md):**
- Relacionar la fatiga de alarmas con la política y no solo con la persona.
- 🎯 **Por qué importa:** Una alarma que suena por cada artefacto enseña a ignorarla. Una que espera demasiado llega tarde.
- 🔗 **Se estudia junto con:** umbral, persistencia, histéresis, latch.

📘 **Dónde se aprende** (1 clase): [B116-C05 · Alertas de salud y umbrales de monitorización](../programa/clases/B116/B116-C05-alertas-de-salud-y-umbrales-de-monitorizacion/CLASE.md).

### Fatiga de alertas

- La fatiga de alertas es la pérdida de atención ante alertas repetidas que no se cumplen.

💡 **Contexto en la clase [B57-C34](../programa/clases/B57/B57-C34-alertas-tempranas-y-etica-en-el-monitoreo-de-desastres/CLASE.md):**
- **Idea central (modelo mental):** Si el pastor grita «¡lobo!» por cada sombra, nadie le cree cuando llega el lobo; si nunca grita, pierde las ovejas. El umbral decide cuándo gritar.
- 🎯 **Por qué importa:** Un detector excelente puede producir una mayoría de falsas alarmas si el evento es raro, y las alertas repetidas y falsas se ignoran. La decisión central: ¿qué umbral y qué comunicación equilibran el costo de omitir y el de alarmar en falso, y quién decide?
- 🔗 **Se estudia junto con:** tasa de falsa alarma, tasa de detección, valor predictivo positivo, umbral óptimo.

📘 **Dónde se aprende** (1 clase): [B57-C34 · Alertas tempranas y ética en el monitoreo de desastres](../programa/clases/B57/B57-C34-alertas-tempranas-y-etica-en-el-monitoreo-de-desastres/CLASE.md).

### Fayalita

- Un mineral es un sólido cristalino natural de composición química definida: el olivino `(Mg,Fe)₂SiO₄` es una serie entre la forsterita `Mg₂SiO₄` y la fayalita `Fe₂SiO₄`; el piroxeno más sencillo es `MgSiO₃`; la calcita es `CaCO₃`.
- La forsterita (Mg₂SiO₄) y la fayalita (Fe₂SiO₄) son los extremos del olivino; la enstatita (MgSiO₃) es un piroxeno.

💡 **Cómo se explica en la clase [B06-C19](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md):**
- Con los pesos atómicos de la NIST (C03): `H₂O = 18,0153`, `CO₂ = 44,0094`, `NH₃ = 17,0308`, forsterita `Mg₂SiO₄ = 2 × 24,3055 + 28,085 + 4 × 15,9994 = 140,6936`, fayalita `Fe₂SiO₄ = 203,7726`, piroxeno `MgSiO₃ = 100,3887` y calcita `CaCO₃ = 100,0868 g/mol`.
- Un olivino con 90 % de forsterita y 10 % de fayalita (Fo₉₀) tiene una masa formular que es el promedio ponderado de las dos: `0,9 × 140,6936 + 0,1 × 203,7726 = 147,0015 g/mol`.
- 🎯 **Por qué importa:** Los estudios con el telescopio James Webb muestran que las nubes densas del medio interestelar tienen granos de polvo cubiertos de hielos con una variedad de moléculas, y que esos hielos contienen entre el 2 y el 19 % del carbono, oxígeno, nitrógeno y azufre disponibles (S1, resumen).
- 🔗 **Se estudia junto con:** hielo, mineral, olivino, forsterita.

📘 **Dónde se aprende** (2 clases): [B06-C19 · Química de hielos y minerales](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md); [B55-C12 · Geoquímica de meteoritos](../programa/clases/B55/B55-C12-geoquimica-de-meteoritos/CLASE.md).

### FECF

- El FECF es un CRC de 16 bits con polinomio `X¹⁶ + X¹² + X⁵ + 1` y registro inicial a unos.

💡 **Cómo se explica en la clase [B94-C03](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md):**
- El CRC se calcula sobre toda la trama salvo el propio FECF, con registro inicial a unos.
- Al recalcularlo sobre trama + FECF el resultado debe ser cero, y así lo comprueba el receptor.
- 🎯 **Por qué importa:** Un receptor que recibe un flujo de octetos con pérdidas necesita saber qué trama es, si llegó íntegra, si faltan tramas y dónde retomar los paquetes. La decisión central: ¿qué campos de la trama permiten detectar errores y pérdidas y resincronizar sin retransmitir?
- 🔗 **Se estudia junto con:** trama de transferencia de telemetría, SCID, VCID, contador de canal maestro.

📘 **Dónde se aprende** (1 clase): [B94-C03 · Tramas de transferencia de telemetría y telecomando](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md).

### FEFO

- FIFO emite el lote recibido antes; FEFO emite el que caduca antes.

💡 **Cómo se explica en la clase [B100-C01](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md):**
- Caducan `324 u` (15,6 % de lo recibido) en FIFO y `164 u` (7,9 %) en FEFO: 160 u menos, un 49 % menos.
- Para el lote L05 en FEFO hay 26 emisiones, 102 u, entre los días 199 y 262; por consumidor: C1 = 21, C2 = 21, C3 = 23, C4 = 15, C5 = 22 (suma 102).
- ⚠️ **Error frecuente:** Creer que FEFO atiende más demanda. Se corrige con 8.2: atiende la misma y caduca menos
- 🎯 **Por qué importa:** Un inventario que solo sabe «cuántas unidades hay» no puede decir de qué lote vienen, cuándo caducan ni dónde se usaron. La decisión central: ¿qué registro mínimo hace falta para emitir primero lo que caduca antes y para encontrar, si un lote resulta defectuoso, adónde fue?
- 🔗 **Se estudia junto con:** lote, FIFO, Caducado, trazabilidad.

📘 **Dónde se aprende** (1 clase): [B100-C01 · Gestión de inventario de materias primas y piezas](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md).

### Fenómeno de Gibbs

- El fenómeno de Gibbs es la oscilación persistente cerca de un salto.

💡 **Cómo se explica en la clase [B11-C16](../programa/clases/B11/B11-C16-metodos-espectrales-iniciales/CLASE.md):**
- Reconocer el fenómeno de Gibbs en una señal con salto.
- El script [derivada_espectral.py](derivada_espectral.py) calcula derivadas por FFT, las compara con la analítica y con la diferencia central, demuestra el aliasing y el fenómeno de Gibbs, y resuelve el calor periódico por modo; falla si la convergencia o los errores salen de rango.
- 🎯 **Por qué importa:** Cuando la solución es suave y periódica —una señal a lo largo de una órbita, un perfil de temperatura alrededor de un vehículo que gira, el campo en una caja periódica—, un método espectral logra con 24 puntos lo que unas diferencias finitas lograrían con millones.
- 🔗 **Se estudia junto con:** transformada discreta de Fourier, transformada rápida, derivada espectral, convergencia espectral.

📘 **Dónde se aprende** (1 clase): [B11-C16 · Métodos espectrales iniciales](../programa/clases/B11/B11-C16-metodos-espectrales-iniciales/CLASE.md).

### Fenómeno de Runge

- El fenómeno de Runge es la oscilación creciente en los extremos al subir el grado con nodos equiespaciados.

💡 **Cómo se explica en la clase [B11-C18](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md):**
- Reconocer el fenómeno de Runge con nodos equiespaciados.
- 🎯 **Por qué importa:** Si una nave debe saber dónde está un cuerpo en un instante que no figura en la tabla, interpola. Si interpola con un grado equivocado o fuera del rango, el error puede pasar de metros a miles de kilómetros sin que el programa avise.
- 🔗 **Se estudia junto con:** polinomio de Lagrange, polinomio nodal, error, Interpolar.

📘 **Dónde se aprende** (1 clase): [B11-C18 · Interpolación y extrapolación](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md).

### FER

- BER: tasa de error de bit. FER: tasa de error de trama, `1 − (1 − p)^n`.

💡 **Cómo se explica en la clase [B90-C16](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md):**
- Paso 2 · FER. `1 − (1 − 10⁻⁴)^1040 = 1 − e^{−0,104} = 0,0988`.
- Con `BER = 10⁻⁴`, la FER es 0,0988 y cada trama se reintenta en promedio 1,11 veces; con `BER = 10⁻³`, FER 0,647 y 2,83 envíos.
- 🎯 **Por qué importa:** Cada subsistema puede pasar sus pruebas y la cadena fallar: un formato de trama distinto, un retraso mayor que el tiempo de espera, un error de bit no detectado. La decisión central: ¿qué errores detecta la cadena, con qué frecuencia reintenta y cuánto tarda cada acuse?
- 🔗 **Se estudia junto con:** Prueba de extremo a extremo, CRC, BER, Ráfaga.

📘 **Dónde se aprende** (1 clase): [B90-C16 · Pruebas de extremo a extremo](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md).

### Fermi–Dirac

- La distribución de Bose–Einstein, la de Fermi–Dirac y la de Maxwell–Boltzmann.

💡 **Cómo se explica en la clase [B31-C06](../programa/clases/B31/B31-C06-estadisticas-cuanticas/CLASE.md):**
- Bose–Einstein para fotones (con `μ = 0`) y Fermi–Dirac para electrones.
- 🎯 **Por qué importa:** La radiación de las estrellas y la presión de degeneración de los remanentes estelares dependen de estas estadísticas. La decisión central: ¿qué distribución usar y qué constantes se derivan?
- 🔗 **Se estudia junto con:** distribución de Bose–Einstein, Maxwell–Boltzmann, integral de Planck, energía de Fermi.

📘 **Dónde se aprende** (1 clase): [B31-C06 · Estadísticas cuánticas](../programa/clases/B31/B31-C06-estadisticas-cuanticas/CLASE.md).

### Fermión

- Un fermión obedece el principio de exclusión.

💡 **Contexto en la clase [B27-C01](../programa/clases/B27/B27-C01-presion-de-degeneracion/CLASE.md):**
- **Idea central (modelo mental):** Cada butaca (estado) admite dos personas (espines). Aunque la sala esté a temperatura cero, las butacas bajas se llenan y las últimas personas quedan sentadas en niveles altos, con mucha energía y empujando.
- 🎯 **Por qué importa:** Una estrella sin fusión no se desploma porque los electrones (o neutrones) no pueden apretarse más allá de lo que permite el principio de exclusión, aunque la temperatura sea cero. La decisión central: dada la densidad de un gas degenerado, ¿cuánto vale el momento de Fermi, la presión y cuál de los dos límites aplica?
- 🔗 **Se estudia junto con:** momento de Fermi, presión de degeneración, régimen no relativista, ultrarrelativista.

📘 **Dónde se aprende** (1 clase): [B27-C01 · Presión de degeneración](../programa/clases/B27/B27-C01-presion-de-degeneracion/CLASE.md).

### FFT

- La FFT es una familia de algoritmos que calculan la DFT en `O(N log N)`; la versión más usada se atribuye a Cooley y Tukey, como señala la documentación de NumPy (S1).
- La FFT da el espectro.

💡 **Cómo se explica en la clase [B15-C05](../programa/clases/B15/B15-C05-transformada-rapida-de-fourier/CLASE.md):**
- La FFT parte la serie en muestras pares e impares, calcula la DFT de cada mitad (que es más pequeña) y las combina con unos pocos productos.
- Su límite: al ordenar, el orden final es único pero depende de las comparaciones; en la FFT el resultado es exactamente el de la DFT, sin aproximación.
- ⚠️ **Error frecuente:** Aplicar una FFT de base 2 a un `N` que no lo es. La implementación propia debe fallar o rellenar; se declara.
- 🎯 **Por qué importa:** Una curva de luz de 27 días con cadencia de 2 minutos tiene 19 440 muestras. La suma directa de la DFT necesita unos 378 millones de multiplicaciones complejas; una imagen de 1024 × 1024 necesitaría muchísimas más.
- 🔗 **Se estudia junto con:** mariposa, base 2, relleno con ceros, orden estándar.

📘 **Dónde se aprende** (2 clases): [B15-C05 · Transformada rápida de Fourier](../programa/clases/B15/B15-C05-transformada-rapida-de-fourier/CLASE.md); [B46-C10 · Radioastronomía mediante SDR](../programa/clases/B46/B46-C10-radioastronomia-mediante-sdr/CLASE.md).

### FFT bidimensional

- La FFT bidimensional de canal × tiempo.

💡 **Contexto en la clase [B51-C11](../programa/clases/B51/B51-C11-busqueda-de-franjas-vlbi-ajuste-de-retardo-y-tasa/CLASE.md):**
- **Idea central (modelo mental):** Como buscar una nota débil en una sala ruidosa: la transformada ordena el sonido por tono y ritmo, y la nota aparece como un pico; pero entre miles de posiciones algún pico de ruido también sobresale, y hay que saber cuánto.
- 🎯 **Por qué importa:** Declarar una detección sin umbral estadístico es un riesgo de falsos positivos. La decisión central: ¿qué pico es una señal y cuál es ruido, y con qué precisión se estiman retardo y tasa?
- 🔗 **Se estudia junto con:** retardo, tasa, relleno de ceros, pérdida por celda.

📘 **Dónde se aprende** (1 clase): [B51-C11 · Búsqueda de franjas VLBI: ajuste de retardo y tasa](../programa/clases/B51/B51-C11-busqueda-de-franjas-vlbi-ajuste-de-retardo-y-tasa/CLASE.md).

### Fiabilidad

- La fiabilidad `R(t)` es la probabilidad de funcionar hasta `t`.
- La fiabilidad `r` es la proporción de la varianza que es real.
- La fiabilidad `r` es la probabilidad de que una fuente informe correctamente.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B33-C05](../programa/clases/B33/B33-C05-comunicacion-de-riesgo-y-alertas-de-clima-espacial/CLASE.md):**
- *Descripción textual:* el cociente costo/pérdida fija el umbral de decisión, que da el gasto; el Brier y la fiabilidad miden la calidad de las probabilidades.
- Ejercicio 12. Integrador. Elabora tu *ficha del riesgo y las alertas*: umbral, gasto, Brier y fiabilidad.
- 🎯 **Por qué importa:** La mejor comunicación de riesgo da probabilidades calibradas y deja decidir al usuario. La decisión central: ¿cuándo conviene proteger y cuán fiables son las probabilidades?
- 🔗 **Se estudia junto con:** costo, pérdida, umbral de decisión, puntuación de Brier.

📖 **Explicado a fondo:** [Redundancia y fiabilidad](esencial/ampliacion-n-z.md#redundancia-y-fiabilidad) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (7 clases): [B33-C05 · Comunicación de riesgo y alertas de clima espacial](../programa/clases/B33/B33-C05-comunicacion-de-riesgo-y-alertas-de-clima-espacial/CLASE.md); [B59-C18 · Fiabilidad de equipos mineros](../programa/clases/B59/B59-C18-fiabilidad-de-equipos-mineros/CLASE.md); [B88-C01 · Arquitectura de computador de vuelo](../programa/clases/B88/B88-C01-arquitectura-de-computador-de-vuelo/CLASE.md); [B106-C18 · Fiabilidad y redundancia](../programa/clases/B106/B106-C18-fiabilidad-y-redundancia/CLASE.md); [B107-C04 · Evaluación del rendimiento físico y cognitivo de tripulantes](../programa/clases/B107/B107-C04-evaluacion-del-rendimiento-fisico-y-cognitivo-de-tripulantes/CLASE.md); [B118-C11 · Diseño para mitigación de desechos](../programa/clases/B118/B118-C11-diseno-para-mitigacion-de-desechos/CLASE.md) y 1 más.

### Fibra neutra

- La fibra neutra es la línea que no se alarga al doblar.

💡 **Contexto en la clase [B95-C04](../programa/clases/B95/B95-C04-antenas-desplegables-para-satelites-pequenos/CLASE.md):**
- 🎯 **Por qué importa:** Un enlace con la Tierra necesita una antena, y una antena que no se despliega deja el satélite mudo. La decisión central: ¿qué longitud necesita la antena, cómo se pliega sin dañarla y qué riesgo añade el mecanismo?
- 🔗 **Se estudia junto con:** monopolo de cuarto de onda, cinta elástica, hilo de quemado, inhibidor.

📘 **Dónde se aprende** (1 clase): [B95-C04 · Antenas desplegables para satélites pequeños](../programa/clases/B95/B95-C04-antenas-desplegables-para-satelites-pequenos/CLASE.md).

### Ficha de procedencia

- La ficha de procedencia guarda por cada cifra: valor, unidad, fuente, fecha, estado e incertidumbre.

💡 **Cómo se explica en la clase [B130-C01](../programa/clases/B130/B130-C01-infografias-con-fuentes-verificables/CLASE.md):**
- Ejercicio 12 · integrador. Integrador. Elabora tu *auditoría de una infografía de datos planetarios*: ficha de procedencia de al menos cuatro cifras, LF de sus círculos, cifras redondeadas, color representativo (si aplica) y crédito.
- El script [infografia.py](infografia.py) audita las fichas de procedencia, calcula el factor de mentira, redondea según la incertidumbre, asigna colores por orden cromático y valida un crédito CC BY (comprueba 4 de 7 completas, LF área = 1 con 1e-12 y los redondeos esperados).
- 🎯 **Por qué importa:** Comunicar con imágenes exige mantener la fuente y la incertidumbre; la clase de comunicación general no entra en cómo se audita una pieza visual. La decisión central: ¿qué debe llevar cada cifra de una infografía para que otra persona pueda verificarla, y qué diseño la deforma?
- 🔗 **Se estudia junto con:** estado, factor de mentira, color representativo, crédito.

📘 **Dónde se aprende** (1 clase): [B130-C01 · Infografías con fuentes verificables](../programa/clases/B130/B130-C01-infografias-con-fuentes-verificables/CLASE.md).

### Fidelidad

- La fidelidad `q` es la probabilidad de copiar bien una letra.
- La fidelidad de un propagador es cuánto se parece su modelo de fuerzas y su integración a la realidad (o a una referencia).
- La fidelidad es cuánto se parece el simulador al sistema real.

💡 **Cómo se explica en la clase [B56-C03](../programa/clases/B56/B56-C03-origen-de-moleculas-autorreplicantes/CLASE.md):**
- En un mundo real la fidelidad no es una constante.
- Una molécula que se copia a sí misma, como el ARN, necesita copiar con alta fidelidad para no degradarse.
- 🎯 **Por qué importa:** Un replicador que copia mal pierde su información; uno que copia bien necesita una maquinaria que, sin vida previa, aún no existe. Esa tensión limita el tamaño de los primeros genomas.
- 🔗 **Se estudia junto con:** replicador, secuencia maestra, calidad de copia, ventaja selectiva.

📘 **Dónde se aprende** (3 clases): [B56-C03 · Origen de moléculas autorreplicantes](../programa/clases/B56/B56-C03-origen-de-moleculas-autorreplicantes/CLASE.md); [B72-C20 · Comparación de propagadores de fidelidad distinta](../programa/clases/B72/B72-C20-comparacion-de-propagadores-de-fidelidad-distinta/CLASE.md); [B104-C09 · Entrenamiento en simuladores](../programa/clases/B104/B104-C09-entrenamiento-en-simuladores/CLASE.md).

### FIFO

- La clase de servicio del protocolo de paquetes es `bulk`, `normal` o `expedited`, con prioridad 0, 1 y 2. FIFO sirve por orden de llegada.
- Un lote es la unidad de trazabilidad. FIFO emite el lote recibido antes;

💡 **Cómo se explica en la clase [B94-C05](../programa/clases/B94/B94-C05-calidad-de-servicio-y-prioridades-en-redes-espaciales/CLASE.md):**
- FIFO reparte el daño por igual y ni siquiera protege lo urgente.
- S --> P["politica: FIFO,<br/>prioridad estricta,<br/>reparto ponderado"]
- 🎯 **Por qué importa:** Si la demanda supera a la capacidad, alguien espera. La decisión central: ¿qué política de cola garantiza lo urgente sin dejar sin servicio a las demás clases, y a qué coste?
- 🔗 **Se estudia junto con:** clase de servicio, Prioridad estricta, reparto ponderado, inanición.

📘 **Dónde se aprende** (2 clases): [B94-C05 · Calidad de servicio y prioridades en redes espaciales](../programa/clases/B94/B94-C05-calidad-de-servicio-y-prioridades-en-redes-espaciales/CLASE.md); [B100-C01 · Gestión de inventario de materias primas y piezas](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md).

### Figura

- Una figura (`Figure`) es el lienzo completo; los ejes (`Axes`) son la región donde se dibujan los datos, con sus dos ejes de coordenadas (`Axis`) que fijan escala, límites y marcas (S2).
- Una figura es un gráfico o imagen; una tabla, una disposición de valores en filas y columnas.

💡 **Cómo se explica en la clase [B07-C10](../programa/clases/B07/B07-C10-graficos-bidimensionales-iniciales/CLASE.md):**
- En escala lineal, Neptuno (a ≈ 4515, T ≈ 60 189) domina el gráfico y Mercurio, Venus, la Tierra y Marte quedan amontonados cerca del origen (panel izquierdo de la figura).
- *Descripción textual:* los datos (dos arreglos) se dibujan sobre unos ejes que llevan escala, etiquetas y unidades; los ejes forman parte de una figura con título y leyenda, que se guarda como imagen acompañada de una descripción en texto.
- 🎯 **Por qué importa:** Un gráfico es una afirmación: dice «mira esta relación». Un gráfico sin unidades, con una escala que esconde la mitad de los datos o sin leyenda puede inducir a error aunque los números sean correctos.
- 🔗 **Se estudia junto con:** ejes, ejes de coordenadas, interfaz explícita, interfaz implícita.

📘 **Dónde se aprende** (2 clases): [B07-C10 · Gráficos bidimensionales iniciales](../programa/clases/B07/B07-C10-graficos-bidimensionales-iniciales/CLASE.md); [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md).

### Figura de mérito G/T

- La figura de mérito `G/T` mide la sensibilidad de la estación.

💡 **Contexto en la clase [B91-C08](../programa/clases/B91/B91-C08-antenas-de-gran-apertura-y-estaciones-de-espacio-profundo/CLASE.md):**
- 🎯 **Por qué importa:** Un enlace a distancias de unidades astronómicas pierde unos 280 dB: solo se cierra con una estación enorme y de ruido muy bajo. La decisión central: ¿qué antena de estación (una de 70 m, una de 34 m o un arreglo de varias) permite la velocidad de datos pedida, y cuánto cuesta un error de apuntamiento?
- 🔗 **Se estudia junto con:** EIRP, pérdida por apuntamiento, pérdida de espacio libre, arreglo de antenas.

📘 **Dónde se aprende** (1 clase): [B91-C08 · Antenas de gran apertura y estaciones de espacio profundo](../programa/clases/B91/B91-C08-antenas-de-gran-apertura-y-estaciones-de-espacio-profundo/CLASE.md).

### Figura de mérito térmica

- La figura de mérito térmica `k/α` indica cuánto se deforma por un flujo de calor dado.

💡 **Cómo se explica en la clase [B43-C03](../programa/clases/B43/B43-C03-materiales-para-espejos/CLASE.md):**
- Calcular la rigidez específica `E/ρ` y la figura de mérito térmica `k/α`.
- 🎯 **Por qué importa:** Un buen material no es el más duro ni el más estable: es el que deja el menor error de forma para una masa y un presupuesto. La decisión central: ¿qué material y qué espesor mantienen la flexión y la deriva térmica por debajo de la tolerancia?
- 🔗 **Se estudia junto con:** módulo de Young, rigidez específica, placa de Kirchhoff, ecuación biarmónica.

📘 **Dónde se aprende** (1 clase): [B43-C03 · Materiales para espejos](../programa/clases/B43/B43-C03-materiales-para-espejos/CLASE.md).

### Figura de ruido

- La figura de ruido `NF = 10 log₁₀ F`.

💡 **Cómo se explica en la clase [B89-C07](../programa/clases/B89/B89-C07-figura-de-ruido-de-receptor/CLASE.md):**
- La figura de ruido equivalente es `0,626`, `1,620` y `9,00 dB`.
- Convertir figura de ruido en temperatura de ruido y viceversa.
- ⚠️ **Error frecuente:** Sumar figuras de ruido en dB en vez de temperaturas. Se corrige con 8.2.
- 🎯 **Por qué importa:** La primera etapa de una cadena receptora decide casi todo el ruido: un amplificador de bajo ruido bien colocado vale muchos decibelios de `G/T`. La decisión central: ¿qué orden y qué componentes dan la menor temperatura de sistema y el mayor `G/T`?
- 🔗 **Se estudia junto con:** temperatura de ruido, fórmula de Friis para el ruido, temperatura de sistema, G/T.

📘 **Dónde se aprende** (1 clase): [B89-C07 · Figura de ruido de receptor](../programa/clases/B89/B89-C07-figura-de-ruido-de-receptor/CLASE.md).

### Fija

- Una función fija no depende del número de tripulantes; una lineal crece con él; una por pares crece por cada dos tripulantes; una logística crece con tripulantes por días.

💡 **Cómo se explica en la clase [B109-C05](../programa/clases/B109/B109-C05-crecimiento-modular-y-escalabilidad-de-asentamientos/CLASE.md):**
- Fijas: médico, trabajo, ordenadores, cocina, utilización, traslado y esclusa.
- Paso 3 · Logística y fijas. Logística `5,79 × 2 = 11,58`; fijas `47,39 − 8,61 − 4,17 − 5,79 = 28,82`.
- 🎯 **Por qué importa:** Si el primer módulo no admite ampliación, crecer obliga a desechar lo construido. La decisión central: ¿qué funciones se duplican con la tripulación, cuáles no, y cómo se añaden módulos sin rediseñar?
- 🔗 **Se estudia junto con:** módulo, fase, crecimiento aditivo, escalabilidad.

📘 **Dónde se aprende** (1 clase): [B109-C05 · Crecimiento modular y escalabilidad de asentamientos](../programa/clases/B109/B109-C05-crecimiento-modular-y-escalabilidad-de-asentamientos/CLASE.md).

### Fijar

- `uv run` ejecuta un comando dentro del entorno del proyecto, comprobando antes que el bloqueo y el entorno estén al día (S4). Fijar una versión es escribirla con `==`.
- La huella del entorno es el registro de las versiones de Python, plataforma y bibliotecas con que se ejecutó un análisis. Fijar una versión es exigir exactamente esa.

💡 **Cómo se explica en la clase [B14-C12](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md):**
- Para fijar el sistema completo se usan contenedores (C17), con sus propios límites.
- 🎯 **Por qué importa:** Tu análisis dio un período de 5553,624562 s en 2026. Un colega lo ejecuta con otra versión de SciPy y obtiene un cierre distinto; otro usa Python más antiguo y falla al importar. «En mi máquina funciona» no es un resultado científico.
- 🔗 **Se estudia junto con:** proyecto, resolutor, archivo de bloqueo, bloqueo universal.

📘 **Dónde se aprende** (2 clases): [B07-C13 · Entornos y dependencias con uv](../programa/clases/B07/B07-C13-entornos-y-dependencias-con-uv/CLASE.md); [B14-C12 · Ejecución reproducible con uv](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md).

### Fila

- Una fila se llama periodo; una columna, grupo.
- Una tabla es un conjunto de columnas del mismo largo; cada fila describe un objeto y cada columna una propiedad.

💡 **Cómo se explica en la clase [B14-C05](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md):**
- Se calcula sobre los valores no enmascarados y las filas faltantes devuelven `NaN` (no un número).
- Ninguna fila corresponde a una estrella real; el desplazamiento se fijó de antemano para que podamos comprobar el cruce.
- 🎯 **Por qué importa:** Un catálogo de estrellas no es una lista de números: cada columna tiene una unidad, algunas filas no tienen paralaje, y la tabla viene de un instrumento, una época y una versión. Si pierdes eso al copiar los datos a un arreglo, pierdes la mitad del significado.
- 🔗 **Se estudia junto con:** tabla, columna, catálogo, columna enmascarada.

📘 **Dónde se aprende** (2 clases): [B06-C02 · Tabla periódica y abundancias cósmicas](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md); [B14-C05 · Tablas astronómicas y catálogos](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md).

### Filamento

- El filamento o la prominencia.

💡 **Cómo se explica en la clase [B34-C08](../programa/clases/B34/B34-C08-erupciones-de-filamentos-y-prominencias/CLASE.md):**
- A `100 km/s` la cinética es el 61 % de la potencial: lejos de la escape, pero para elevar el filamento basta con mover el equilibrio.
- La evidencia es la ficha de la erupción de un filamento del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Saber a qué altura el campo ya no sostiene al filamento sirve para anticipar erupciones. La decisión central: ¿a qué altura el decaimiento del campo supera el umbral?
- 🔗 **Se estudia junto con:** índice de decaimiento, altura crítica, prominencia, inestabilidad.

📘 **Dónde se aprende** (1 clase): [B34-C08 · Erupciones de filamentos y prominencias](../programa/clases/B34/B34-C08-erupciones-de-filamentos-y-prominencias/CLASE.md).

### Filosofía de modelos

- Unidad de vuelo (FM): la que vuela. Filosofía de modelos: conjunto de modelos que se construye y prueba.

💡 **Cómo se explica en la clase [B90-C24](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md):**
- La evidencia es la comparación de filosofías de modelos del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *comparación de filosofías de modelos*: etapas, detecciones, costos, riesgo residual, costo esperado, sensibilidad a `F` y lista de qué es consultado, no consultado y sintético.
- 🎯 **Por qué importa:** Un modelo de ingeniería cuesta dinero y calendario; un defecto que llega a órbita cuesta la misión. La decisión central: ¿vale la pena construir un modelo previo, o conviene el protovuelo o solo la unidad de vuelo, dado el valor de lo que se arriesga?
- 🔗 **Se estudia junto con:** Prototipo, Modelo de ingeniería (EM), Modelo de calificación (QM), Protovuelo.

📘 **Dónde se aprende** (1 clase): [B90-C24 · Prototipado y modelos de ingeniería de subconjuntos](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md).

### Filtro acoplado

- El filtro acoplado correlaciona los datos con la plantilla.

💡 **Cómo se explica en la clase [B28-C21](../programa/clases/B28/B28-C21-formas-de-onda-gravitacionales-y-filtro-acoplado/CLASE.md):**
- *Descripción textual:* la masa de chirrido da la frecuencia y la fase, de ahí la forma de onda; el filtro acoplado la correlaciona con los datos y el desajuste con plantillas vecinas fija el banco.
- Aplicar el filtro acoplado `ρ = Σ d h/√Σ h²`.
- 🎯 **Por qué importa:** Una plantilla ligeramente errada pierde mucha señal-ruido, porque la fase acumula miles de ciclos. Entender cuánto determina cuántas plantillas hacen falta.
- 🔗 **Se estudia junto con:** chirrido, plantilla, desajuste, banco.

📘 **Dónde se aprende** (1 clase): [B28-C21 · Formas de onda gravitacionales y filtro acoplado](../programa/clases/B28/B28-C21-formas-de-onda-gravitacionales-y-filtro-acoplado/CLASE.md).

### Filtro adaptado

- El filtro adaptado (*matched filter*) es la correlación de la imagen con la propia PSF normalizada `p` (suma 1): maximiza la SNR de una fuente puntual en ruido blanco.
- El filtro adaptado correlaciona el eco con una copia del pulso.

💡 **Cómo se explica en la clase [B15-C12](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md):**
- Un pixel aislado daría `F p₀/σ` con `p₀ = 0,0707` (el valor máximo de la PSF normalizada): el filtro adaptado gana un factor `√(Σp²)/p₀ = 0,1881/0,0707 = 2,66`.
- Buscar una estrella débil es como buscar una nota de flauta en una sala ruidosa: sabes cómo suena (la PSF), así que escuchas selectivamente esa forma (filtro adaptado) en lugar de cada píxel por separado.
- 🎯 **Por qué importa:** Un catálogo de fuentes es el producto básico de una imagen astronómica, y de él salen cuentas, colores y candidatos a objetos nuevos. Si el umbral es bajo, el catálogo se llena de ruido; si es alto, se pierden las fuentes débiles.
- 🔗 **Se estudia junto con:** fondo, ruido, relación señal–ruido, umbral.

📘 **Dónde se aprende** (2 clases): [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B57-C07 · Sistemas radar SAR](../programa/clases/B57/B57-C07-sistemas-radar-sar/CLASE.md).

### Filtro antialias

- El filtro antialias es un filtro aplicado antes de muestrear que elimina lo que está por encima de `f_N`.
- Aliasing: aparición de una frecuencia superior a Nyquist como una menor. Filtro antialias: filtro pasa-bajas antes del muestreo.

💡 **Cómo se explica en la clase [B15-C02](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md):**
- La segunda: filtrar antes de muestrear con un filtro antialias analógico u óptico.
- 🎯 **Por qué importa:** Un detector que mide una estrella cada 2 minutos no puede ver directamente algo que oscila cada 3 minutos con precisión, pero tampoco lo ignora: ese movimiento rápido queda registrado como una oscilación lenta y falsa. Si no sabes que eso ocurre, publicarías un periodo que no existe.
- 🔗 **Se estudia junto con:** muestreo, frecuencia de muestreo, frecuencia de Nyquist, aliasing.

📘 **Dónde se aprende** (2 clases): [B15-C02 · Muestreo y aliasing](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md); [B90-C23 · Instrumentación y adquisición de datos en ensayos](../programa/clases/B90/B90-C23-instrumentacion-y-adquisicion-de-datos-en-ensayos/CLASE.md).

### Filtro de alta eficiencia

- Clase de limpieza: número `N` que fija el límite de partículas por tamaño. Filtro de alta eficiencia: filtro que retiene la fracción `η` de las partículas del aire que lo cruza.

💡 **Contexto en la clase [B90-C02](../programa/clases/B90/B90-C02-buenas-practicas-de-sala-limpia/CLASE.md):**
- 🎯 **Por qué importa:** Una partícula sobre una óptica, un sello o un contacto puede degradar una misión; las partículas llegan con el aire, la ropa y las herramientas. La decisión central: ¿qué clase de sala puede sostener esta actividad con este número de personas, y cuánto hay que esperar tras una perturbación?
- 🔗 **Se estudia junto con:** Sala limpia, Clase de limpieza, Renovaciones por hora (ACH), Mezcla perfecta.

📘 **Dónde se aprende** (1 clase): [B90-C02 · Buenas prácticas de sala limpia](../programa/clases/B90/B90-C02-buenas-practicas-de-sala-limpia/CLASE.md).

### Filtro de apsis

- El filtro de apsis compara las cáscaras `[r_p, r_a]`.

💡 **Cómo se explica en la clase [B118-C18](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md):**
- Límite: el filtro de apsis es el más simple; otros filtros usan planos orbitales y tiempos, y el derecho tiene excepciones que la clase no recorre.
- Descripción larga: el filtro de apsis descarta más de la mitad de los pares y la verificación muestra que no pierde ninguno; con muchas órbitas casi circulares a la misma altitud quedan más pares por evaluar.
- 🎯 **Por qué importa:** Con decenas de miles de objetos, comparar todos los pares es costoso; un buen cribado descarta de entrada los pares imposibles sin perder ninguno posible. Y cuando algo sale mal, los tratados determinan responsabilidad y jurisdicción.
- 🔗 **Se estudia junto con:** cribado, Estado de lanzamiento, Estado de registro, responsabilidad absoluta.

📘 **Dónde se aprende** (1 clase): [B118-C18 · Gestión del tráfico espacial](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md).

### Filtro de Butterworth

- El filtro de Butterworth es el de respuesta plana en la banda.

💡 **Contexto en la clase [B49-C10](../programa/clases/B49/B49-C10-filtros-de-radiofrecuencia-pasabanda-y-rechazo-de-banda-imagen/CLASE.md):**
- **Idea central (modelo mental):** Como un colador: deja pasar lo que cabe y detiene lo demás; uno más fino detiene mejor pero deja pasar menos agua.
- 🎯 **Por qué importa:** Más orden rechaza más, pero también pierde más señal. La decisión central: ¿qué orden y qué ancho de banda dan el rechazo de imagen necesario con una pérdida aceptable?
- 🔗 **Se estudia junto con:** prototipo pasabajos, banda imagen, pérdida de inserción, factor de calidad sin carga.

📘 **Dónde se aprende** (1 clase): [B49-C10 · Filtros de radiofrecuencia pasabanda y rechazo de banda imagen](../programa/clases/B49/B49-C10-filtros-de-radiofrecuencia-pasabanda-y-rechazo-de-banda-imagen/CLASE.md).

### Filtro de Kalman escalar

- El filtro de Kalman escalar estima `s` con el modelo `s_k = s_(k−1) + w`, `z_k = s_k + v`.

💡 **Cómo se explica en la clase [B102-C03](../programa/clases/B102/B102-C03-deslizamiento-y-estimacion-de-patinaje/CLASE.md):**
- Diseñar un filtro de Kalman escalar para un patinaje que varía como paseo aleatorio.
- 🎯 **Por qué importa:** Un rover que cree haber avanzado 315 m cuando solo avanzó 270 m llega al sitio equivocado. La decisión central: ¿cómo se estima el patinaje en línea, con qué incertidumbre y cuánto mejora la distancia corregida?
- 🔗 **Se estudia junto con:** patinaje, referencia independiente, ecuación de Riccati.

📘 **Dónde se aprende** (1 clase): [B102-C03 · Deslizamiento y estimación de patinaje](../programa/clases/B102/B102-C03-deslizamiento-y-estimacion-de-patinaje/CLASE.md).

### Filtro de Kalman extendido

- El filtro de Kalman extendido linealiza la medición no lineal `r = |p − p_b|` con la matriz `H = [(p − p_b)/r, 0, 0, 0, 0]`.

💡 **Contexto en la clase [B80-C04](../programa/clases/B80/B80-C04-fusion-inercial-con-mediciones-externas-acoplamiento-debil-y-fuerte/CLASE.md):**
- 🎯 **Por qué importa:** B74-C08..C10 dan los filtros, pero ninguna clase los aplica a la unión de una IMU con una fuente externa. La decisión central: ¿en qué nivel se funden la inercia y la medición externa, y qué se pierde o se gana al elegirlo?
- 🔗 **Se estudia junto con:** acoplamiento débil, acoplamiento fuerte, innovación.

📘 **Dónde se aprende** (1 clase): [B80-C04 · Fusión inercial con mediciones externas (acoplamiento débil y fuerte)](../programa/clases/B80/B80-C04-fusion-inercial-con-mediciones-externas-acoplamiento-debil-y-fuerte/CLASE.md).

### Filtro de Lee

- El filtro de Lee mezcla la media local y el pixel según el contraste local.

💡 **Cómo se explica en la clase [B69-C03](../programa/clases/B69/B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md):**
- I --> LEE["filtro de Lee: media local + pixel"]
- *Descripción textual:* la intensidad es la reflectividad multiplicada por un speckle exponencial; se reduce promediando vistas o con un filtro adaptativo.
- 🎯 **Por qué importa:** Un valor de píxel aislado de una imagen SAR no mide la reflectividad de la superficie: es una muestra de una distribución muy ancha. La decisión central: ¿cuánto hay que promediar o filtrar para estimar la reflectividad con una incertidumbre dada, y a qué precio en resolución?
- 🔗 **Se estudia junto con:** speckle, intensidad, contraste, ENL.

📘 **Dónde se aprende** (1 clase): [B69-C03 · Ruido speckle y filtrado en imágenes SAR](../programa/clases/B69/B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md).

### Filtro de menor retardo

- Jitter: variación aleatoria del retardo. Filtro de menor retardo: elige el intercambio más rápido.

💡 **Cómo se explica en la clase [B48-C10](../programa/clases/B48/B48-C10-redes-de-instrumentos/CLASE.md):**
- El filtro de menor retardo la baja a 0,533 ms pero deja el sesgo.
- Aplicar el filtro de menor retardo de 8 intercambios.
- 🎯 **Por qué importa:** Si los relojes difieren, los datos de distintos instrumentos no se pueden correlacionar. La decisión central: ¿cómo se reduce el error de un desfase estimado cuando la red es asimétrica?
- 🔗 **Se estudia junto con:** Desfase, Retardo, Asimetría, Jitter.

📘 **Dónde se aprende** (1 clase): [B48-C10 · Redes de instrumentos](../programa/clases/B48/B48-C10-redes-de-instrumentos/CLASE.md).

### Filtro de ocular

- Un filtro de ocular se enrosca atrás: la AAS dice que es peligroso y debe desecharse (S3).

💡 **Cómo se explica en la clase [B08-C16](../programa/clases/B08/B08-C16-observacion-solar-con-filtros-certificados/CLASE.md):**
- Explicar por qué las gafas de sol, los visores de eclipse con óptica y los filtros de ocular son peligrosos.
- Al frente, sobre la apertura, antes de que la luz se concentre (S3); los filtros que se enroscan en el ocular, atrás, reciben luz concentrada y son peligrosos (S3).
- ⚠️ **Error frecuente:** Poner un filtro en el ocular. Ejercicio 3.
- 🎯 **Por qué importa:** Una persona que mira un eclipse parcial con gafas falsas, o enfoca el Sol con un telescopio sin filtro frontal, puede quedar con una lesión permanente. La pregunta motivadora: ¿cómo observo el Sol sin dañarme y sin dañar a otros?
- 🔗 **Se estudia junto con:** ISO 12312-2, visor solar, filtro solar frontal, proyección con orificio.

📘 **Dónde se aprende** (1 clase): [B08-C16 · Observación solar con filtros certificados](../programa/clases/B08/B08-C16-observacion-solar-con-filtros-certificados/CLASE.md).

### Filtro de significancia

- El filtro de significancia es la selección de los resultados con `p < α`: entre ellos, el efecto estimado está sesgado hacia valores grandes.

💡 **Contexto en la clase [B12-C26](../programa/clases/B12/B12-C26-sesgos-y-potencia-estadistica-en-poblaciones-pequenas/CLASE.md):**
- **Idea central (modelo mental):** Una prueba con baja potencia es una red con agujeros grandes: casi todo se escapa, y lo único que queda atrapado son los peces más grandes (los efectos más exagerados por el azar). Lo atrapado no representa lo que había en el agua.
- 🎯 **Por qué importa:** En medicina espacial, en estudios con tripulaciones o en misiones con pocas unidades, los tamaños de muestra son pequeños por necesidad. Con ellos, la mayoría de los efectos reales no se detectan, y los que se detectan suelen estar inflados.
- 🔗 **Se estudia junto con:** potencia, t no central, error tipo M, error tipo S.

📘 **Dónde se aprende** (1 clase): [B12-C26 · Sesgos y potencia estadística en poblaciones pequeñas](../programa/clases/B12/B12-C26-sesgos-y-potencia-estadistica-en-poblaciones-pequenas/CLASE.md).

### Filtro de suelo

- El filtro de suelo clasifica los puntos que están en el terreno.

💡 **Cómo se explica en la clase [B57-C30](../programa/clases/B57/B57-C30-nubes-de-puntos-tridimensionales/CLASE.md):**
- El filtro (plano inicial por mínimo en celdas de 5 m, refinado tres veces con los puntos a menos de 1,2; 0,7 y 0,35 m) clasifica `20003` puntos como suelo con un recall de `1,000` y una contaminación de `0,01%`: los puntos de tronco bajo y de maleza sintética que caen bajo el umbral.
- Descripción larga: el filtro recupera casi todo el suelo con muy poca contaminación, y RANSAC acierta la pendiente con y sin filtro porque el suelo domina la nube.
- 🎯 **Por qué importa:** Un modelo de terreno malo hace que las pendientes y las alturas de los árboles salgan mal. La decisión central: ¿cómo se separa el suelo del resto con la menor contaminación y qué densidad de puntos hace falta?
- 🔗 **Se estudia junto con:** nube de puntos, RANSAC, recall, contaminación.

📘 **Dónde se aprende** (1 clase): [B57-C30 · Nubes de puntos tridimensionales](../programa/clases/B57/B57-C30-nubes-de-puntos-tridimensionales/CLASE.md).

### Filtro de Wiener

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C19](../programa/clases/B42/B42-C19-reconstruccion-de-imagenes/CLASE.md):**
- El filtro inverso y Wiener generan valores negativos (−336 y −213 cuentas) y no resuelven el par;
- 🎯 **Por qué importa:** Deconvolucionar recupera detalle bajo el límite de difracción pero amplifica el ruido. La decisión central: ¿qué método usar y qué se gana y se pierde con cada uno?
- 🔗 **Se estudia junto con:** convolución, filtro inverso, Richardson-Lucy, regularización.

📘 **Dónde se aprende** (1 clase): [B42-C19 · Reconstrucción de imágenes](../programa/clases/B42/B42-C19-reconstruccion-de-imagenes/CLASE.md).

### Filtro digital

- Un filtro digital transforma una serie `x[n]` en otra `y[n]`.

💡 **Cómo se explica en la clase [B15-C07](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md):**
- Su límite: una criba separa objetos en dos montones; un filtro digital atenúa gradualmente y también retrasa o distorsiona la fase.
- python programa/clases/B15/B15-C07-filtrado-digital/filtros.py
- 🎯 **Por qué importa:** Una curva de luz tiene una modulación lenta de la estrella (manchas que rotan) de 2000 partes por millón y, escondido en ella, el paso de un planeta que reduce el brillo 1000 ppm durante tres horas. Para ver el tránsito hay que quitar la modulación; pero si el filtro es demasiado agresivo, también se come parte del tránsito.
- 🔗 **Se estudia junto con:** lineal, invariante, FIR, coeficientes.

📘 **Dónde se aprende** (1 clase): [B15-C07 · Filtrado digital](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md).

### Filtro en la apertura

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B43-C19](../programa/clases/B43/B43-C19-seguridad-y-mantenimiento/CLASE.md):**
- El cociente de áreas entre la apertura y una pupila de 7 mm es `816,3`: sin filtro, el ojo recibiría cientos de veces la irradiancia del Sol.
- Es el ejemplo conductor y ejemplifica por qué el Sol exige un filtro certificado en la apertura.
- 🎯 **Por qué importa:** La seguridad empieza por saber cuán grande es el riesgo. La decisión central: ¿cuánta potencia y qué temperatura aparecen en el foco, cómo se balancea la montura y cuánto polvo es aceptable?
- 🔗 **Se estudia junto con:** irradiancia solar total, concentración, temperatura de equilibrio, contrapeso.

📘 **Dónde se aprende** (1 clase): [B43-C19 · Seguridad y mantenimiento](../programa/clases/B43/B43-C19-seguridad-y-mantenimiento/CLASE.md).

### Filtro inverso

- El filtro inverso divide la DFT de `d` por `Ĥ`.

💡 **Cómo se explica en la clase [B15-C11](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md):**
- I -->|"filtro inverso"| E["Ruido amplificado<br/>(inutilizable)"]
- *Descripción textual:* el objeto se convoluciona con la PSF y se le añade ruido; invertir con el filtro inverso amplifica el ruido hasta inutilizar la imagen, mientras que el método iterativo de Richardson–Lucy, detenido a tiempo, produce una estimación más nítida.
- ⚠️ **Error frecuente:** Aplicar el filtro inverso a datos con ruido. Se corrige con los ejercicios 5 y 6.
- 🎯 **Por qué importa:** Un telescopio con un defecto de enfoque convierte cada estrella en una mancha. Dos estrellas cercanas pueden fundirse en una sola; el brillo de una galaxia, repartirse sobre sus vecinas.
- 🔗 **Se estudia junto con:** PSF, gaussiana, FWHM, desenfoque.

📘 **Dónde se aprende** (2 clases): [B15-C11 · Deconvolución y enfoque](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md); [B42-C19 · Reconstrucción de imágenes](../programa/clases/B42/B42-C19-reconstruccion-de-imagenes/CLASE.md).

### Filtro pasa-altos

- El filtro pasa-altos de primer orden `τ dw_p/dt = −w_p + τ dw/dt` describe el canal.
- Un filtro pasa-altos quita las variaciones lentas.

💡 **Cómo se explica en la clase [B105-C04](../programa/clases/B105/B105-C04-sistema-vestibular/CLASE.md):**
- Modelar un canal semicircular como filtro pasa-altos con constante `τ` y simular su respuesta.
- Porque el filtro pasa-altos responde al cambio de velocidad: el escalón negativo produce una señal de signo opuesto que decae con `τ`.
- 🎯 **Por qué importa:** En la Tierra el cerebro usa la gravedad como referencia de «abajo». En caída libre esa referencia desaparece y el sensor sigue midiendo, pero su señal significa otra cosa.
- 🔗 **Se estudia junto con:** otolitos, canales semicirculares, ambigüedad inclinación–traslación.

📘 **Dónde se aprende** (2 clases): [B37-C13 · Series fotométricas de Kepler, TESS y PLATO para asterosismología](../programa/clases/B37/B37-C13-series-fotometricas-de-kepler-tess-y-plato-para-asterosismologia/CLASE.md); [B105-C04 · Sistema vestibular](../programa/clases/B105/B105-C04-sistema-vestibular/CLASE.md).

### Filtro solar frontal

- Un filtro solar frontal va montado sobre la apertura de telescopios, binoculares o cámaras.

💡 **Cómo se explica en la clase [B08-C16](../programa/clases/B08/B08-C16-observacion-solar-con-filtros-certificados/CLASE.md):**
- Ejercicio 12 · integrador. Elabora un plan de observación solar: objetivo, método elegido (proyección, visor, filtro frontal o datos), verificación del equipo con fuente, las cinco reglas de seguridad aplicables, el cálculo del tamaño de la imagen o la rotación, una alternativa sin riesgo y quién supervisa.
- 🎯 **Por qué importa:** Una persona que mira un eclipse parcial con gafas falsas, o enfoca el Sol con un telescopio sin filtro frontal, puede quedar con una lesión permanente. La pregunta motivadora: ¿cómo observo el Sol sin dañarme y sin dañar a otros?
- 🔗 **Se estudia junto con:** ISO 12312-2, visor solar, filtro de ocular, proyección con orificio.

📘 **Dónde se aprende** (1 clase): [B08-C16 · Observación solar con filtros certificados](../programa/clases/B08/B08-C16-observacion-solar-con-filtros-certificados/CLASE.md).

### Financiamiento necesario

- La caja mínima es el punto más bajo de esa suma y fija el financiamiento necesario.

💡 **Cómo se explica en la clase [B126-C03](../programa/clases/B126/B126-C03-proyeccion-de-flujos-de-caja-de-un-proyecto-espacial/CLASE.md):**
- *Descripción textual:* los ingresos y costos dan el flujo neto de cada año; su suma corrida es la caja, cuyo mínimo es el financiamiento necesario; se repite con escenarios y se verifica con una suma directa.
- Calcular la caja acumulada y su mínimo, que es el financiamiento necesario.
- 🎯 **Por qué importa:** [B124-C05](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) estima costos sin flujos de caja. La decisión central: ¿cuánto dinero hay que levantar y cuándo, y qué tan sensible es esa cifra a un retraso o a un sobrecosto?
- 🔗 **Se estudia junto con:** flujo neto, caja acumulada, caja mínima, margen de seguridad.

📘 **Dónde se aprende** (1 clase): [B126-C03 · Proyección de flujos de caja de un proyecto espacial](../programa/clases/B126/B126-C03-proyeccion-de-flujos-de-caja-de-un-proyecto-espacial/CLASE.md).

### FIR

- Un filtro FIR (respuesta finita al impulso) calcula `y[n] = Σ_{m=0}^{M−1} h[m] x[n − m]`; la lista `h[m]` son los coeficientes.

💡 **Cómo se explica en la clase [B15-C07](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md):**
- Un FIR de coeficientes simétricos y `M` términos retrasa todas las frecuencias por igual, `(M − 1)/2` muestras (en el laboratorio, un pulso con centroide en 150 sale en `165` con `M = 31`: retardo `15,000` exacto).
- (4) retardo del FIR causal (M=31): centroide de 150.000 a 165.000 (retardo 15.000; teoría 15.0)
- 🎯 **Por qué importa:** Una curva de luz tiene una modulación lenta de la estrella (manchas que rotan) de 2000 partes por millón y, escondido en ella, el paso de un planeta que reduce el brillo 1000 ppm durante tres horas. Para ver el tránsito hay que quitar la modulación; pero si el filtro es demasiado agresivo, también se come parte del tránsito.
- 🔗 **Se estudia junto con:** filtro digital, lineal, invariante, coeficientes.

📘 **Dónde se aprende** (1 clase): [B15-C07 · Filtrado digital](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md).

### Firma

- Firma: vector de desviaciones de una causa.

💡 **Cómo se explica en la clase [B96-C29](../programa/clases/B96/B96-C29-diagnostico-de-fallas-de-enlace/CLASE.md):**
- El método es estándar (clasificación por mínima distancia) y lo verifica el laboratorio; las firmas y los ruidos son sintéticos.
- S["Firmas de 6 condiciones"] --> M["Medicion con ruido gaussiano"]
- 🎯 **Por qué importa:** Perder tiempo de contacto buscando la causa equivocada es caro. La decisión central: ¿qué medidas distinguen las causas y cuáles se confunden entre sí?
- 🔗 **Se estudia junto con:** Diccionario de fallas, Mínima distancia, Matriz de confusión, Cota de unión.

📘 **Dónde se aprende** (1 clase): [B96-C29 · Diagnóstico de fallas de enlace](../programa/clases/B96/B96-C29-diagnostico-de-fallas-de-enlace/CLASE.md).

### Firma astrométrica

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B29-C04](../programa/clases/B29/B29-C04-astrometria-de-exoplanetas/CLASE.md):**
- La evidencia es la ficha de firma astrométrica del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *ficha de firma astrométrica*: tabla de firmas, ajuste con covarianza y Monte Carlo, significancia.
- 🎯 **Por qué importa:** La astrometría mide la inclinación y la masa verdadera, pero la señal es diminuta. La decisión central: ¿cuál es la firma de un planeta a una distancia dada y con qué incertidumbre se recupera su órbita junto al paralaje y el movimiento propio?
- 🔗 **Se estudia junto con:** paralaje, movimiento propio, matriz de diseño, covarianza.

📘 **Dónde se aprende** (1 clase): [B29-C04 · Astrometría de exoplanetas](../programa/clases/B29/B29-C04-astrometria-de-exoplanetas/CLASE.md).

### Firn

- El firn es nieve compactada de densidad menor que la del hielo.

💡 **Cómo se explica en la clase [B57-C14](../programa/clases/B57/B57-C14-glaciares-y-criosfera/CLASE.md):**
- Un glaciar de `10⁵ km²` que baja `0,5 m/año` pierde `45,9 Gt/año` si lo perdido es hielo (917 kg/m³, referencia no consultada) y `17,5 Gt/año` si es firn (350 kg/m³).
- Ejercicio 4. ¿Cuánto cambia si fuera firn de 350 kg/m³?
- 🎯 **Por qué importa:** Un glaciar que baja medio metro puede haber perdido mucha o poca masa según lo que se pierda sea hielo o nieve. La decisión central: ¿qué densidad uso para convertir cambios de altura en masa y cuánto cambia el resultado?
- 🔗 **Se estudia junto con:** equivalente en nivel del mar, gravimetría, armónicos esféricos, grado.

📘 **Dónde se aprende** (1 clase): [B57-C14 · Glaciares y criósfera](../programa/clases/B57/B57-C14-glaciares-y-criosfera/CLASE.md).

### FISTA

- La restricción blanda de velocidad se castiga con `ρ max(0, |ω|−ω_max)²`. FISTA es un gradiente proyectado acelerado.

💡 **Cómo se explica en la clase [B87-C21](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md):**
- FISTA con 1500 iteraciones por paso (arranque en caliente) converge: la diferencia máxima entre la solución a 1500 y a 15 000 iteraciones es `0,623 %` del límite y el residuo del gradiente proyectado `7,11e-01`.
- Paso 3 · Solución. FISTA, `0,62 %` de diferencia con la solución casi exacta.
- 🎯 **Por qué importa:** Un PD satura el par y no sabe de límites de velocidad: puede superar el máximo de la rueda o de la carga útil. La decisión central: ¿cómo formular un problema que respete par y velocidad, cuánto cuesta calcularlo y qué se gana?
- 🔗 **Se estudia junto con:** MPC, horizonte, QP condensado, restricción dura.

📘 **Dónde se aprende** (1 clase): [B87-C21 · Control predictivo basado en modelo (MPC) para vehículos espaciales](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md).

### Fisura

- Una fisura es una grieta alargada por la que sale el magma.

💡 **Cómo se explica en la clase [B70-C01](../programa/clases/B70/B70-C01-volcanismo-basaltico-escudos-fisuras-y-llanuras-planetarias/CLASE.md):**
- Para emitir `1 km³` por una fisura de `10 km` con `w = 1 m` tardan `0,71 d` (Tierra), `1,86 d` (Marte) y `4,29 d` (Luna) en este modelo.
- Imagina el escudo como un cuenco invertido cuyo perfil se ajusta con un exponente, y la fisura como una rendija por la que el fluido avanza más rápido en el centro que en las paredes.
- 🎯 **Por qué importa:** Una llanura de lava no dice por sí sola cuánto magma la formó ni cuánto tardó. La decisión central: ¿qué volumen y qué caudal corresponden a este edificio y a esta fisura, y qué cambiaría en otro planeta?
- 🔗 **Se estudia junto con:** escudo, llanura volcánica, flujo de Poiseuille, gradiente de presión.

📘 **Dónde se aprende** (1 clase): [B70-C01 · Volcanismo basáltico: escudos, fisuras y llanuras planetarias](../programa/clases/B70/B70-C01-volcanismo-basaltico-escudos-fisuras-y-llanuras-planetarias/CLASE.md).

### Fit check

- Flujo de ensayos: orden de los ensayos. Fit check: ajuste con el dispensador.

💡 **Cómo se explica en la clase [B90-C20](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md):**
- A["Fit check"] --> B["Funcional<br/>de referencia"]
- Armar el flujo de ensayos de un CubeSat (fit check, funcional, vibración, choque opcional, termovacío con bakeout, funcional posensayo, DITL).
- 🎯 **Por qué importa:** Un calendario de ensayos sin contingencia casi nunca se cumple: cada falla suma retrabajo y repetición. La decisión central: ¿cuánto tiempo reservar para terminar con una confianza dada?
- 🔗 **Se estudia junto con:** Campaña de calificación, Flujo de ensayos, DITL, Contingencia.

📘 **Dónde se aprende** (1 clase): [B90-C20 · Campaña conceptual de calificación de CubeSat](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md).

### FITS

- FITS: bloques de 2880 bytes con tarjetas de 80 caracteres.

💡 **Cómo se explica en la clase [B40-C14](../programa/clases/B40/B40-C14-productos-de-datos-de-planck-y-misiones-del-cmb/CLASE.md):**
- *Descripción textual:* se escribe y se lee un FITS, se convierten unidades y se evalúa una verosimilitud por bandas.
- Escribir y leer cabeceras FITS de 80 caracteres.
- 🎯 **Por qué importa:** Usar un producto sin leer su cabecera es una fuente clásica de errores de unidades y de orden de pixeles. La decisión central: ¿qué dice la cabecera y cómo se convierte y se compara con un modelo?
- 🔗 **Se estudia junto con:** BINTABLE, Centinela, verosimilitud gaussiana, banda.

📘 **Dónde se aprende** (1 clase): [B40-C14 · Productos de datos de Planck y misiones del CMB](../programa/clases/B40/B40-C14-productos-de-datos-de-planck-y-misiones-del-cmb/CLASE.md).

### FK

- Los tipos descritos por NAIF son SPK (posición y velocidad), CK (orientación de nave), PCK (tamaño, forma y orientación de cuerpos), IK (campo de visión de instrumentos), FK (marcos), LSK (segundos intercalares), SCLK (reloj de nave) y DSK (formas).

💡 **Cómo se explica en la clase [B74-C21](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md):**
- Por tipo: SPK, CK, PCK, IK, FK, LSK, SCLK.
- Un CK (actitud de la nave) junto con IK y FK.
- 🎯 **Por qué importa:** Un resultado de navegación depende de qué kernels se cargaron y en qué orden: dos corridas con el mismo código pueden dar trayectorias distintas. La decisión central: ¿cómo declaro, valido y audito el conjunto de kernels de una solución para que sea reproducible?
- 🔗 **Se estudia junto con:** kernel, SPK, CK, PCK.

📘 **Dónde se aprende** (1 clase): [B74-C21 · Kernels SPICE y su uso en navegación](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md).

### Flanco de subida

- La forma de onda es la potencia del eco en función del tiempo; su flanco de subida marca la superficie media.

💡 **Contexto en la clase [B57-C09](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md):**
- **Idea central (modelo mental):** Gritas en un pozo y mides cuánto tarda el eco: la profundidad es la mitad del tiempo por la velocidad. El eco real es borroso; ajustas su inicio promediando muchas veces.
- 🎯 **Por qué importa:** La altura del mar cambia unos milímetros por año, pero el eco de un pulso es ruidoso. La decisión central: ¿cuántos pulsos hay que promediar y cómo se ajusta el eco para que el error de distancia del ajuste se reduzca lo necesario?
- 🔗 **Se estudia junto con:** tiempo de ida y vuelta, distancia, forma de onda, reajuste.

📘 **Dónde se aprende** (1 clase): [B57-C09 · Altimetría satelital](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md).

### Flat

- El flat es un cuadro de campo uniformemente iluminado.

💡 **Cómo se explica en la clase [B44-C14](../programa/clases/B44/B44-C14-calibracion-con-flat/CLASE.md):**
- Sin corregir, la no uniformidad es `0,0386`; con un flat de `80` cuadros, `0,00738`.
- F["N flats"] --> M["mediana y normalización"]
- ⚠️ **Error frecuente:** Aplicar el flat antes del bias y el dark. Se corrige con la sección 11.
- 🎯 **Por qué importa:** Los píxeles no responden igual y el campo se oscurece hacia el borde. La decisión central: ¿cuántos flats hacen falta para que el ruido del flat no domine?
- 🔗 **Se estudia junto con:** PRNU, viñeteo, normalización, no uniformidad residual.

📘 **Dónde se aprende** (1 clase): [B44-C14 · Calibración con flat](../programa/clases/B44/B44-C14-calibracion-con-flat/CLASE.md).

### Flecha

- La flecha (o sagita) es la profundidad del espejo en el borde.
- La flecha es el desplazamiento del centro respecto del borde.

💡 **Cómo se explica en la clase [B09-C13](../programa/clases/B09/B09-C13-areas-y-volumenes-por-integracion/CLASE.md):**
- La flecha en el borde es `R²/(4f) = 15,6 mm`.
- Ejercicio 12 · integrador. Elabora tu *hoja de geometría de un espejo y de un esferoide con verificación*: para el espejo (sintético) la flecha, el volumen del plato, la superficie y la masa retirada; para el esferoide, su volumen por discos y la comparación con el valor de la NASA; añade el área de la elipse orbital.
- 🎯 **Por qué importa:** Un telescopio necesita un espejo con forma de paraboloide. Cuánto vidrio hay que retirar de un disco plano para darle forma, cuánto pesa, y cuánta superficie hay que aluminizar son preguntas de volumen y área.
- 🔗 **Se estudia junto con:** área entre curvas, sólido de revolución, método de los discos, método de los cascarones.

📘 **Dónde se aprende** (2 clases): [B09-C13 · Áreas y volúmenes por integración](../programa/clases/B09/B09-C13-areas-y-volumenes-por-integracion/CLASE.md); [B43-C03 · Materiales para espejos](../programa/clases/B43/B43-C03-materiales-para-espejos/CLASE.md).

### Flecha de voladizo

- La flecha de voladizo `P L³/(3EI)` o `w L⁴/(8EI)`.

💡 **Cómo se explica en la clase [B43-C10](../programa/clases/B43/B43-C10-estructura-de-tubo-optico/CLASE.md):**
- La flecha en voladizo bajo su peso uniforme es de `11,58 µm`.
- Obtener flechas de voladizo con carga puntual y uniforme.
- 🎯 **Por qué importa:** Lo que decolima no es la flexión sino la flexión diferencial entre primario y secundario. La decisión central: ¿qué rigideces hacen que los dos extremos se muevan lo mismo, de modo que el eje óptico solo se desplace en paralelo?
- 🔗 **Se estudia junto con:** cercha Serrurier, rigidez a flexión, descentrado diferencial, tubo delgado.

📘 **Dónde se aprende** (1 clase): [B43-C10 · Estructura de tubo óptico](../programa/clases/B43/B43-C10-estructura-de-tubo-optico/CLASE.md).

### Flexión gravitatoria

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B49-C03](../programa/clases/B49/B49-C03-apuntamiento-y-seguimiento-de-radiotelescopios-modelos-de-apuntado-y-errores/CLASE.md):**
- **Idea central (modelo mental):** Como corregir una brújula con una tabla de desvíos: se mide hacia puntos conocidos y se ajustan las correcciones.
- 🎯 **Por qué importa:** Con un haz estrecho, un error de apuntado pequeño pierde ganancia. La decisión central: ¿qué términos modelar, y cuánto error residual queda frente al ancho del haz?
- 🔗 **Se estudia junto con:** desplazamiento de cero, colimación, no perpendicularidad de ejes, inclinación del eje de azimut.

📘 **Dónde se aprende** (1 clase): [B49-C03 · Apuntamiento y seguimiento de radiotelescopios: modelos de apuntado y errores](../programa/clases/B49/B49-C03-apuntamiento-y-seguimiento-de-radiotelescopios-modelos-de-apuntado-y-errores/CLASE.md).

### Flotabilidad

- La flotabilidad es `g (T_p − T_e)/T_e`.

💡 **Cómo se explica en la clase [B54-C07](../programa/clases/B54/B54-C07-dinamica-de-tormentas/CLASE.md):**
- TP["T de la parcela"] --> B["flotabilidad B"]
- *Descripción textual:* la diferencia de temperatura entre parcela y ambiente da la flotabilidad; su integral es la CAPE y de ella sale la cota de velocidad.
- ⚠️ **Error frecuente:** Sumar también los tramos de flotabilidad negativa. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** La energía convectiva disponible decide si una tormenta tiene vigor o no. La pregunta motivadora: ¿cuánta velocidad puede alcanzar el aire que sube si toda la flotabilidad se convierte en movimiento?
- 🔗 **Se estudia junto con:** CAPE, parcela, arrastre.

📘 **Dónde se aprende** (1 clase): [B54-C07 · Dinámica de tormentas](../programa/clases/B54/B54-C07-dinamica-de-tormentas/CLASE.md).

### Flotabilidad neutra

- La flotabilidad neutra ocurre cuando el empuje iguala al peso.

💡 **Cómo se explica en la clase [B104-C15](../programa/clases/B104/B104-C15-entrenamiento-subacuatico-como-analogia/CLASE.md):**
- *Descripción textual:* del volumen y la masa se obtiene el lastre que da flotabilidad neutra; en el agua, la masa añadida y el arrastre hacen que el movimiento difiera del que habría en el vacío.
- Lastre para flotabilidad neutra: 1,36 kg; presión a 12,2 m: 220,5 kPa.
- 🎯 **Por qué importa:** El agua anula el peso neto, pero también se opone al movimiento. La decisión central: ¿qué aspectos de una tarea espacial se pueden entrenar bien en el agua y cuáles quedan distorsionados por la inercia y el arrastre del fluido?
- 🔗 **Se estudia junto con:** lastre, masa añadida, arrastre, presión absoluta.

📘 **Dónde se aprende** (1 clase): [B104-C15 · Entrenamiento subacuático como analogía](../programa/clases/B104/B104-C15-entrenamiento-subacuatico-como-analogia/CLASE.md).

### Fluctuación

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B32-C07](../programa/clases/B32/B32-C07-modelos-de-atmosferas-estelares-1d-y-3d-hidrodinamicos/CLASE.md):**
- *Descripción textual:* la profundidad óptica define el modelo 1D; las fluctuaciones gaussianas elevan el flujo medio por encima del de la temperatura media.
- Una fluctuación del 10 % aumenta el flujo medio un `6,0 %`.
- 🎯 **Por qué importa:** Las abundancias derivadas con 1D pueden diferir de las 3D por la no linealidad del flujo con la temperatura. La decisión central: ¿cuánto sesga una fluctuación la temperatura inferida?
- 🔗 **Se estudia junto con:** modelo 1D, modelo 3D hidrodinámico, altura de escala, no linealidad.

📘 **Dónde se aprende** (1 clase): [B32-C07 · Modelos de atmósferas estelares 1D y 3D hidrodinámicos](../programa/clases/B32/B32-C07-modelos-de-atmosferas-estelares-1d-y-3d-hidrodinamicos/CLASE.md).

### Fluencia

- La fluencia es el número de neutrinos por unidad de área.
- La fluencia es el flujo integrado en el tiempo.
- La fluencia `Φ` es el número de fotones acumulados por cm².
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B27-C18](../programa/clases/B27/B27-C18-neutrinos-de-supernova/CLASE.md):**
- A `d = 10 kpc = 3,0857 × 10²⁰ m`, la fluencia es `2,1735 × 10¹⁵ m⁻² = 2,1735 × 10¹¹ cm⁻²`.
- *Descripción textual:* de la energía y la energía media se obtiene el número de neutrinos y su fluencia; con la sección eficaz y los protones del detector, los sucesos; el retraso por masa se calcula con una forma algebraica estable.
- 🎯 **Por qué importa:** Los neutrinos de una supernova galáctica serían una señal de cientos de sucesos en unos segundos, mensajera del interior de la estrella. La decisión central: ¿cuántos neutrinos llegan, qué retraso produce su masa y cómo se calcula sin perder precisión?
- 🔗 **Se estudia junto con:** neutrino, sección eficaz, protones libres, retraso por masa.

📘 **Dónde se aprende** (6 clases): [B27-C18 · Neutrinos de supernova](../programa/clases/B27/B27-C18-neutrinos-de-supernova/CLASE.md); [B30-C12 · Erupciones y fulguraciones solares](../programa/clases/B30/B30-C12-erupciones-y-fulguraciones-solares/CLASE.md); [B47-C14 · Radiación y degradación](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md); [B68-C02 · Fotodesorción de hielos interestelares](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md); [B85-C13 · Efectos de oxígeno atómico](../programa/clases/B85/B85-C13-efectos-de-oxigeno-atomico/CLASE.md); [B112-C01 · Magnitudes dosimétricas: dosis absorbida, LET y eficacia biológica](../programa/clases/B112/B112-C01-magnitudes-dosimetricas-dosis-absorbida-let-y-eficacia-biologica/CLASE.md).

### Fluido perfecto

- Un fluido perfecto tiene `T^ab = (ρ + p) u^a u^b + p g^ab`.

💡 **Cómo se explica en la clase [B39-C04](../programa/clases/B39/B39-C04-tensor-de-energia-momento-y-fuentes-de-curvatura/CLASE.md):**
- Límite: un fluido perfecto, sin viscosidad ni flujo de calor.
- 🎯 **Por qué importa:** La fuente de la gravedad es `T^ab`. La decisión central: ¿qué tensor describe la materia y qué condiciones debe cumplir para ser físicamente razonable?
- 🔗 **Se estudia junto con:** densidad, presión, parámetro, condición de energía débil.

📘 **Dónde se aprende** (1 clase): [B39-C04 · Tensor de energía-momento y fuentes de curvatura](../programa/clases/B39/B39-C04-tensor-de-energia-momento-y-fuentes-de-curvatura/CLASE.md).

### Fluido supercrítico

- El punto crítico `(T_c, P_c)` es el extremo de la curva de vaporización: por encima de ambos, la sustancia es un fluido supercrítico, sin diferencia nítida entre líquido y gas.

💡 **Cómo se explica en la clase [B06-C11](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md):**
- Venus (92 bar, 737 K): el CO₂ supera `T_c` y `P_c`: fluido supercrítico; el agua, con `T > 647 K`, no puede ser líquida a ninguna presión.
- ⚠️ **Error frecuente:** Creer que «supercrítico» es una cuarta fase como el plasma. Es un fluido sin transición nítida; se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** La temperatura de ebullición del agua no es una constante de la naturaleza: depende de la presión. En lo alto de una montaña hierve a menos de 100 °C; en Marte, con 6 mb, el agua apenas puede ser líquida; en Venus, a 92 bar y 737 K, el CO₂ no es ni líquido ni gas.
- 🔗 **Se estudia junto con:** diagrama de fases, curvas de equilibrio, fusión, vaporización.

📘 **Dónde se aprende** (1 clase): [B06-C11 · Diagramas de fase](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md).

### Flujo

- El flujo es la energía de luz recibida por unidad de área y tiempo; el brillo aparente es lo que percibimos de él.
- El flujo `F` es la energía recibida por unidad de área y tiempo (W/m²) y cae con el cuadrado de la distancia.
- El flujo `F` es la energía luminosa que llega por unidad de área y tiempo.
- *(y 9 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C09](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md):**
- El brillo da el flujo recibido, pero un objeto débil puede estar lejos o ser intrínsecamente poco luminoso: brillo y distancia están mezclados.
- 🎯 **Por qué importa:** Sobre una galaxia a 43 Mpc solo tienes luz. De esa luz sale su dirección, cuánto brilla, de qué color es y qué líneas aparecen en su espectro; de las líneas sale `z = 0,0101` (C01).
- 🔗 **Se estudia junto con:** longitud de onda, frecuencia, espectro, espectro continuo.

📖 **Explicado a fondo:** [Flujo y luminosidad](esencial/esencial-d-l.md#flujo-y-luminosidad) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (13 clases): [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B01-C14 · Estrellas y sus principales propiedades](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md); [B08-C11 · Magnitudes aparentes y brillo](../programa/clases/B08/B08-C11-magnitudes-aparentes-y-brillo/CLASE.md); [B09-C19 · Cálculo vectorial introductorio](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md); [B21-C01 · Volúmenes finitos y solucionadores de Riemann para leyes de conservación](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md); [B28-C05 · Ondas gravitacionales](../programa/clases/B28/B28-C05-ondas-gravitacionales/CLASE.md) y 7 más.

### Flujo ahogado

- El flujo ahogado (o sónico) ocurre cuando la presión exterior es menos de la mitad de la interior: el caudal depende solo de la presión interior.

💡 **Cómo se explica en la clase [B104-C13](../programa/clases/B104/B104-C13-procedimientos-de-emergencia/CLASE.md):**
- Con el exterior en vacío el flujo está siempre ahogado: `ṁ = C_d A p √(γ/(R T)) · (2/(γ+1))^((γ+1)/(2(γ−1)))`, con `γ = 1,4`, `R = 287,05 J/(kg·K)` y factor `0,5787`.
- factor de flujo ahogado (2/(g+1))^((g+1)/(2(g-1))) = 0.5787
- 🎯 **Por qué importa:** Un procedimiento sirve si se puede ejecutar dentro del tiempo disponible. La decisión central: ¿para qué tamaños de orificio alcanza un tiempo de respuesta de 15 minutos y a partir de cuál ya no?
- 🔗 **Se estudia junto con:** coeficiente de descarga, constante de despresurización, tiempo de respuesta.

📘 **Dónde se aprende** (1 clase): [B104-C13 · Procedimientos de emergencia](../programa/clases/B104/B104-C13-procedimientos-de-emergencia/CLASE.md).

### Flujo conductivo

- El flujo conductivo de Spitzer.

💡 **Cómo se explica en la clase [B34-C01](../programa/clases/B34/B34-C01-calentamiento-coronal-mecanismos-y-evidencias/CLASE.md):**
- Con `T = 2 × 10⁶ K`, `L = 100 Mm` y `n = 10¹⁵ m⁻³` (ilustrativos), el flujo conductivo es `323 W/m²` y la pérdida radiativa `150 W/m²`.
- Calcular el flujo conductivo `(2/7)κ₀T^(7/2)/L`.
- 🎯 **Por qué importa:** Elegir un mecanismo de calentamiento exige saber cuánta energía hay que reponer y de dónde sale. La decisión central: ¿cuánta energía pierde un bucle y qué eventos pueden reponerla?
- 🔗 **Se estudia junto con:** calentamiento coronal, pérdida radiativa, nanofulguración, ley de potencias.

📘 **Dónde se aprende** (1 clase): [B34-C01 · Calentamiento coronal: mecanismos y evidencias](../programa/clases/B34/B34-C01-calentamiento-coronal-mecanismos-y-evidencias/CLASE.md).

### Flujo congelado

- El flujo congelado significa `BR² = const` al contraerse.

💡 **Cómo se explica en la clase [B27-C06](../programa/clases/B27/B27-C06-magnetares-y-campos-extremos/CLASE.md):**
- *Descripción textual:* el campo se compara con `B_Q` para decidir si los efectos cuánticos son relativistas; su energía crece con `B²`; el flujo congelado del progenitor fija el campo de la estrella contraída.
- Ejercicio 12 · integrador. Elabora tu *ficha de campo magnético extremo*: `B_Q`, `ħω_c` y `B/B_Q` para tres campos, `E₁`, energía magnética y rotacional, y flujo congelado.
- 🎯 **Por qué importa:** Los magnetares producen estallidos y llamaradas gigantes que alimenta su campo, no su rotación. Entender la escala del campo y de su energía explica por qué son una familia aparte y cómo se interpretan sus espectros.
- 🔗 **Se estudia junto con:** magnetar, campo crítico cuántico, energía ciclotrónica, niveles de Landau relativistas.

📘 **Dónde se aprende** (2 clases): [B27-C06 · Magnetares y campos extremos](../programa/clases/B27/B27-C06-magnetares-y-campos-extremos/CLASE.md); [B42-C20 · Laboratorio de corrección óptica simulada](../programa/clases/B42/B42-C20-laboratorio-de-correccion-optica-simulada/CLASE.md).

### Flujo cruzado

- Un flujo cruzado es una dependencia entre funciones de subsistemas distintos y es un candidato a interfaz (C08).

💡 **Cómo se explica en la clase [B83-C06](../programa/clases/B83/B83-C06-descomposicion-funcional/CLASE.md):**
- *Descripción textual:* la función de misión se divide en hijas; sus dependencias dan la ruta crítica y las holguras, y su asignación a subsistemas da los flujos cruzados, que se convertirán en interfaces.
- Ejercicio 5 · autónomo. ¿Cuántos flujos cruzados hay en la asignación del laboratorio?
- ⚠️ **Error frecuente:** Olvidar los flujos cruzados. Cuéntalos: son las interfaces futuras
- 🎯 **Por qué importa:** Si se salta a las piezas demasiado pronto, se diseñan cosas que nadie sabe para qué sirven; si se descompone bien, se ve qué función domina el tiempo y dónde se acoplan los subsistemas. La decisión central: ¿qué funciones son críticas para el tiempo y qué subsistemas quedan más acoplados?
- 🔗 **Se estudia junto con:** función, descomposición funcional, diagrama de flujo funcional, ruta crítica.

📘 **Dónde se aprende** (1 clase): [B83-C06 · Descomposición funcional](../programa/clases/B83/B83-C06-descomposicion-funcional/CLASE.md).

### Flujo de calor convectivo de remanso

- El flujo de calor convectivo de remanso es `q̇ = k√(ρ/R_n)V³` con `k = 1,7415·10⁻⁴` (SI, Tierra).

💡 **Contexto en la clase [B77-C15](../programa/clases/B77/B77-C15-calentamiento-aerodinamico/CLASE.md):**
- 🎯 **Por qué importa:** El flujo de calor máximo y la carga total deciden qué material y qué espesor protegen al vehículo, y no se maximizan en el mismo punto que la desaceleración. La decisión central: ¿cuánto vale el flujo de pico, a qué altitud ocurre y cómo escala con el radio de la nariz y el coeficiente balístico?
- 🔗 **Se estudia junto con:** temperatura de equilibrio radiativo, carga térmica, radio de nariz, pared caliente.

📘 **Dónde se aprende** (1 clase): [B77-C15 · Calentamiento aerodinámico](../programa/clases/B77/B77-C15-calentamiento-aerodinamico/CLASE.md).

### Flujo de datos

- Un flujo de datos (*pipeline*) es una cadena de etapas donde la salida de una es la entrada de la siguiente.

💡 **Cómo se explica en la clase [B14-C18](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md):**
- python programa/clases/B14/B14-C18-flujos-de-datos-espaciales/flujo_con_procedencia.py
- 🎯 **Por qué importa:** Un artículo usa «datos de un archivo público filtrados por paralaje y magnitud». Dos años después nadie puede repetir el filtro: el archivo se actualizó, los parámetros no se anotaron y la consulta no se guardó.
- 🔗 **Se estudia junto con:** adquisición, verificación, caché, consulta.

📘 **Dónde se aprende** (1 clase): [B14-C18 · Flujos de datos espaciales](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md).

### Flujo de ensayos

- Campaña de calificación: secuencia de ensayos que demuestra la unidad. Flujo de ensayos: orden de los ensayos.

💡 **Cómo se explica en la clase [B90-C20](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md):**
- Por flujo: orden de ensayos y modelos (C19).
- Armar el flujo de ensayos de un CubeSat (fit check, funcional, vibración, choque opcional, termovacío con bakeout, funcional posensayo, DITL).
- 🎯 **Por qué importa:** Un calendario de ensayos sin contingencia casi nunca se cumple: cada falla suma retrabajo y repetición. La decisión central: ¿cuánto tiempo reservar para terminar con una confianza dada?
- 🔗 **Se estudia junto con:** Campaña de calificación, Fit check, DITL, Contingencia.

📘 **Dónde se aprende** (1 clase): [B90-C20 · Campaña conceptual de calificación de CubeSat](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md).

### Flujo de fotones fotosintéticos (PPFD)

- El flujo de fotones fotosintéticos (PPFD) cuenta los fotones de 400–700 nm que llegan a una superficie (µmol m⁻² s⁻¹).

💡 **Contexto en la clase [B115-C02](../programa/clases/B115/B115-C02-iluminacion-de-cultivos-con-led-y-espectro-de-crecimiento/CLASE.md):**
- 🎯 **Por qué importa:** La luz es el mayor consumo eléctrico de un cultivo cerrado. La decisión central: ¿cuántos fotones por metro cuadrado y día hacen falta, con qué eficacia se producen y qué potencia y calor suponen para el hábitat?
- 🔗 **Se estudia junto con:** integral diaria de luz (DLI), fotoperiodo, eficacia fotónica, eficiencia de uso de la radiación (RUE).

📘 **Dónde se aprende** (1 clase): [B115-C02 · Iluminación de cultivos con LED y espectro de crecimiento](../programa/clases/B115/B115-C02-iluminacion-de-cultivos-con-led-y-espectro-de-crecimiento/CLASE.md).

### Flujo de Hertz–Knudsen

- El flujo de Hertz–Knudsen es `J = p √(M/(2π R T))`.
- El flujo de Hertz–Knudsen `J = m·α·p/√(2π m k_B T)` es la masa que sale por unidad de área y tiempo hacia el vacío;
- El flujo de Hertz–Knudsen es el número de moléculas que golpea una superficie por unidad de área y tiempo.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B47-C12](../programa/clases/B47/B47-C12-optica-en-ambientes-de-vacio/CLASE.md):**
- Calcular el flujo de Hertz-Knudsen y verificarlo con `n⟨v⟩/4`.
- 🎯 **Por qué importa:** La contaminación reduce la reflectancia y la transmisión sin aviso. La decisión central: ¿cuánto tarda en cubrirse una superficie y cuánto cambia la reflectancia por una película?
- 🔗 **Se estudia junto con:** camino libre medio, monocapa, coeficiente de adherencia, desgasificación.

📘 **Dónde se aprende** (4 clases): [B47-C12 · Óptica en ambientes de vacío](../programa/clases/B47/B47-C12-optica-en-ambientes-de-vacio/CLASE.md); [B53-C13 · Geomorfología de hielos](../programa/clases/B53/B53-C13-geomorfologia-de-hielos/CLASE.md); [B67-C03 · Muestreo criogénico y preservación de volátiles en muestras](../programa/clases/B67/B67-C03-muestreo-criogenico-y-preservacion-de-volatiles-en-muestras/CLASE.md); [B68-C04 · Laboratorio de astroquímica de hielos en ultra alto vacío criogénico](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md).

### Flujo de masa

- El flujo de masa `Ṁ = 4πr²ρv`.

💡 **Cómo se explica en la clase [B30-C10](../programa/clases/B30/B30-C10-viento-solar-y-heliosfera/CLASE.md):**
- *Descripción textual:* la temperatura da la velocidad del sonido y el radio crítico; la ecuación de Parker da `v(r)`, del que salen el flujo de masa y la espiral.
- Comprobar que el flujo de masa `r²ρv` es constante.
- ⚠️ **Error frecuente:** Olvidar el flujo de masa constante. Se corrige con 8.3.
- 🎯 **Por qué importa:** El viento solar es el vehículo que lleva la actividad del Sol a la Tierra. La decisión central: ¿cuándo pasa el viento a supersónico y qué velocidad alcanza a 1 au?
- 🔗 **Se estudia junto con:** punto crítico, viento subsónico/supersónico, espiral de Parker, ángulo.

📘 **Dónde se aprende** (1 clase): [B30-C10 · Viento solar y heliosfera](../programa/clases/B30/B30-C10-viento-solar-y-heliosfera/CLASE.md).

### Flujo de micrometeoritos

- El flujo de micrometeoritos `F(≥d) = F₁ (d/0,1 mm)^(−2)`.

💡 **Cómo se explica en la clase [B85-C28](../programa/clases/B85/B85-C28-proteccion-pasiva-frente-al-ambiente-espacial/CLASE.md):**
- MM["Flujo de micrometeoritos + P límite"] --> TP["t_perforación"]
- 🎯 **Por qué importa:** Cada milímetro de blindaje cuesta masa, y el requisito que manda cambia con el entorno. La decisión central: ¿qué espesor y qué material cumplen la dosis y la probabilidad de perforación con la menor masa?
- 🔗 **Se estudia junto con:** atenuación, diámetro crítico, probabilidad de perforación, espesor gobernante.

📘 **Dónde se aprende** (1 clase): [B85-C28 · Protección pasiva frente al ambiente espacial](../programa/clases/B85/B85-C28-proteccion-pasiva-frente-al-ambiente-espacial/CLASE.md).

### Flujo de Poiseuille

- El flujo de Poiseuille es el flujo laminar viscoso entre paredes paralelas.

💡 **Cómo se explica en la clase [B70-C01](../programa/clases/B70/B70-C01-volcanismo-basaltico-escudos-fisuras-y-llanuras-planetarias/CLASE.md):**
- Obtener el caudal por unidad de longitud de una fisura (flujo de Poiseuille).
- 🎯 **Por qué importa:** Una llanura de lava no dice por sí sola cuánto magma la formó ni cuánto tardó. La decisión central: ¿qué volumen y qué caudal corresponden a este edificio y a esta fisura, y qué cambiaría en otro planeta?
- 🔗 **Se estudia junto con:** escudo, fisura, llanura volcánica, gradiente de presión.

📘 **Dónde se aprende** (1 clase): [B70-C01 · Volcanismo basáltico: escudos, fisuras y llanuras planetarias](../programa/clases/B70/B70-C01-volcanismo-basaltico-escudos-fisuras-y-llanuras-planetarias/CLASE.md).

### Flujo de proa

- El flujo de proa es `Φ = n v cosθ`.

💡 **Cómo se explica en la clase [B85-C13](../programa/clases/B85/B85-C13-efectos-de-oxigeno-atomico/CLASE.md):**
- *Descripción textual:* la densidad y la velocidad dan el flujo de proa; integrado en el tiempo es la fluencia; multiplicada por la reactividad da el espesor perdido y la vida de la capa.
- Calcular la velocidad orbital y el flujo de proa `Φ = n v`.
- ⚠️ **Error frecuente:** Aplicar el flujo de proa a todas las caras. depende de `cosθ` (8.2)
- 🎯 **Por qué importa:** Un polímero exterior puede desaparecer en meses en la cara de proa a baja altitud. La decisión central: ¿cuánto espesor pierde una superficie por año según la altitud y la orientación, y qué protección dura la misión?
- 🔗 **Se estudia junto con:** fluencia, erosión, reactividad Re, capa protectora.

📘 **Dónde se aprende** (1 clase): [B85-C13 · Efectos de oxígeno atómico](../programa/clases/B85/B85-C13-efectos-de-oxigeno-atomico/CLASE.md).

### Flujo de puerta

- El flujo de puerta `Q` es el número de personas por segundo que cruza una salida.

💡 **Cómo se explica en la clase [B114-C01](../programa/clases/B114/B114-C01-rutas-de-evacuacion-y-salidas-de-emergencia-en-habitats/CLASE.md):**
- Estimar el tiempo de cola con el flujo de una puerta.
- Ejercicio 7 · autónomo. ¿Qué pasa con el tiempo de cola si la puerta duplica su flujo?
- 🎯 **Por qué importa:** Una salida existe en el plano, pero la evacuación depende de cuánto se tarda en llegar a ella y de qué pasa si el camino principal queda bloqueado. La decisión central: ¿cuánto tarda en salir toda la tripulación y qué ruta queda si falla la principal?
- 🔗 **Se estudia junto con:** ruta de evacuación, ruta alternativa, camino mínimo, cuello de botella.

📘 **Dónde se aprende** (1 clase): [B114-C01 · Rutas de evacuación y salidas de emergencia en hábitats](../programa/clases/B114/B114-C01-rutas-de-evacuacion-y-salidas-de-emergencia-en-habitats/CLASE.md).

### Flujo estacionario

- Un flujo estacionario es aquel en que cada abundancia deja de cambiar.

💡 **Cómo se explica en la clase [B24-C21](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md):**
- Descripción larga: en Poisson, el máximo está cerca de `i = τ`; en el flujo estacionario, la abundancia es inversamente proporcional a la sección eficaz.
- Definir proceso s, exposición de neutrones y flujo estacionario.
- 🎯 **Por qué importa:** Las estrellas AGB son una fuente importante de carbono, nitrógeno y elementos pesados del medio interestelar, y sus abundancias superficiales son el registro observable de lo que ocurre en su interior.
- 🔗 **Se estudia junto con:** rama asintótica de gigantes (AGB), pulso térmico, dragado, proceso s.

📘 **Dónde se aprende** (1 clase): [B24-C21 · Rama asintótica de gigantes: pulsos térmicos y proceso s](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md).

### Flujo estelar efectivo

- El flujo estelar efectivo `S_ef` es el flujo recibido en unidades del terrestre.

💡 **Cómo se explica en la clase [B56-C12](../programa/clases/B56/B56-C12-exoplanetas-potencialmente-habitables/CLASE.md):**
- Definir flujo estelar efectivo, zona habitable, borde interno y externo.
- 🎯 **Por qué importa:** Elegir blancos para buscar biofirmas exige un criterio objetivo. La zona habitable lo ofrece, con limitaciones.
- 🔗 **Se estudia junto con:** zona habitable, borde interno, externo, distancia límite.

📘 **Dónde se aprende** (1 clase): [B56-C12 · Exoplanetas potencialmente habitables](../programa/clases/B56/B56-C12-exoplanetas-potencialmente-habitables/CLASE.md).

### Flujo estrangulado

- El flujo estrangulado es el que alcanza la velocidad del sonido en la garganta y ya no depende de la presión de salida.
- El flujo estrangulado es el máximo caudal másico por un orificio cuando la presión exterior es muy baja.
- El flujo estrangulado alcanza Mach 1 en la garganta.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B70-C06](../programa/clases/B70/B70-C06-criovulcanismo-lavas-heladas-y-emision-de-volatiles/CLASE.md):**
- Para vapor de agua (`M = 0,018015 kg/mol`, `γ = 1,33`, `T₀ = 273,15 K`, ilustrativos), el flujo estrangulado tiene `T* = 2T₀/(γ+1) = 234,5 K` y `v* = √(2γ/(γ+1) · RT₀/M) = 379,4 m/s`; coincide con `√(γRT*/M)` a `10⁻¹²`.
- 🎯 **Por qué importa:** El agua líquida es más densa que el hielo, así que no sube sola. La decisión central: ¿qué presión extra y qué mecanismo hacen falta para que el agua llegue a la superficie?
- 🔗 **Se estudia junto con:** criovulcanismo, criomagma, sobrepresión, velocidad de escape.

📘 **Dónde se aprende** (5 clases): [B70-C06 · Criovulcanismo: lavas heladas y emisión de volátiles](../programa/clases/B70/B70-C06-criovulcanismo-lavas-heladas-y-emision-de-volatiles/CLASE.md); [B78-C10 · Propulsión de gas frío](../programa/clases/B78/B78-C10-propulsion-de-gas-frio/CLASE.md); [B106-C02 · Presurización de módulos](../programa/clases/B106/B106-C02-presurizacion-de-modulos/CLASE.md); [B110-C01 · Despresurización: detección, aislamiento y respuesta](../programa/clases/B110/B110-C01-despresurizacion-deteccion-aislamiento-y-respuesta/CLASE.md); [B114-C02 · Detección, localización y respuesta a fugas de presión](../programa/clases/B114/B114-C02-deteccion-localizacion-y-respuesta-a-fugas-de-presion/CLASE.md).

### Flujo HLL

- El flujo HLL es un solucionador aproximado de Riemann.

💡 **Cómo se explica en la clase [B38-C06](../programa/clases/B38/B38-C06-hidrodinamica-en-simulaciones-sph-y-metodos-de-malla/CLASE.md):**
- Aplicar un esquema de Godunov con flujo HLL.
- Porque el error numérico depende de la velocidad relativa entre el fluido y la malla; una malla que se mueve con el flujo lo evita.
- 🎯 **Por qué importa:** Cada método tiene errores distintos en choques y discontinuidades de contacto. La decisión central: ¿qué error comete cada método frente a una solución exacta y cómo cambia con la resolución?
- 🔗 **Se estudia junto con:** problema de Riemann, onda de rarefacción, discontinuidad de contacto, choque.

📘 **Dónde se aprende** (1 clase): [B38-C06 · Hidrodinámica en simulaciones: SPH y métodos de malla](../programa/clases/B38/B38-C06-hidrodinamica-en-simulaciones-sph-y-metodos-de-malla/CLASE.md).

### Flujo integral

- El flujo integral es el número por área y tiempo sobre una energía.

💡 **Cómo se explica en la clase [B28-C04](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md):**
- Con `γ₁ = 2,7`, `γ₂ = 3,1` y rodilla en `10¹⁵ eV`, el flujo integral analítico y el numérico (Simpson en `ln E`) coinciden a `10⁻⁶`: `1,173684 × 10⁻¹⁹` por encima de `10¹¹ eV` y `4,672165 × 10⁻²³` por encima de `10¹³ eV` (unidades arbitrarias).
- ESP["E^−2,7 → rodilla → E^−3,1"] --> FI["flujo integral"]
- 🎯 **Por qué importa:** El origen de los rayos cósmicos de mayor energía sigue abierto; el criterio de Hillas descarta fuentes y la anisotropía apunta a regiones. La decisión central: ¿qué fuentes pueden alcanzar una energía dada y qué anisotropía se puede detectar con un número dado de eventos?
- 🔗 **Se estudia junto con:** criterio de Hillas, rodilla, dipolo, estimador.

📘 **Dónde se aprende** (1 clase): [B28-C04 · Rayos cósmicos de alta energía](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md).

### Flujo libre

- El flujo libre es el flujo operativo menos la inversión (capex).

💡 **Cómo se explica en la clase [B125-C06](../programa/clases/B125/B125-C06-plan-empresarial-de-una-empresa-espacial/CLASE.md):**
- Flujo libre `= operativo − capex` (`18` M u.m. en los trimestres 1, 2, 9, 10 y 15).
- O --> F["flujo libre = operativo - capex"]
- 🎯 **Por qué importa:** Integrar mercado, finanzas y operación en un plan es el cierre del módulo; el proyecto de B124 es general y no trata una empresa concreta con su caja. La decisión central: ¿cuánta caja necesita la empresa para llegar a su punto de equilibrio y qué supuestos pueden hundir el plan?
- 🔗 **Se estudia junto con:** flujo operativo, caja, brecha de financiación, valor actual.

📘 **Dónde se aprende** (1 clase): [B125-C06 · Plan empresarial de una empresa espacial](../programa/clases/B125/B125-C06-plan-empresarial-de-una-empresa-espacial/CLASE.md).

### Flujo luminoso

- El flujo luminoso se mide en lúmenes con `683 lm/W` a 540 THz.

💡 **Cómo se explica en la clase [B45-C01](../programa/clases/B45/B45-C01-radiometria-y-fotometria/CLASE.md):**
- Ejercicio 8. Flujo luminoso de 100 W con la eficacia calculada.
- 🎯 **Por qué importa:** Todo flujo medido en un telescopio es una cantidad radiométrica o fotométrica con una definición precisa; confundir vatios, lúmenes y fotones arruina la calibración. La decisión central: ¿en qué unidades se expresa lo que llega al detector y cómo se pasa de una a otra?
- 🔗 **Se estudia junto con:** radiancia, exitancia, irradiancia, fotón.

📘 **Dónde se aprende** (1 clase): [B45-C01 · Radiometría y fotometría](../programa/clases/B45/B45-C01-radiometria-y-fotometria/CLASE.md).

### Flujo magnético

- El flujo magnético es `Φ = BA`.
- El flujo magnético es la integral de `B` por una superficie.

💡 **Cómo se explica en la clase [B30-C04](../programa/clases/B30/B30-C04-manchas-solares/CLASE.md):**
- Ejercicio 4. Flujo magnético de una mancha de `r = 5 Mm` con `B = 0,2 T`.
- El script [mancha.py](mancha.py) calcula las presiones, el contraste, el flujo magnético, el área en MSH y el déficit de irradiancia (comprueba la conversión de área y el contraste de la fotosfera).
- 🎯 **Por qué importa:** Las manchas son la huella visible del campo magnético y las más fáciles de contar. Cuantificar su presión, su brillo y su flujo permite relacionarlas con la irradiancia.
- 🔗 **Se estudia junto con:** umbra, penumbra, presión magnética, contraste.

📘 **Dónde se aprende** (2 clases): [B30-C04 · Manchas solares](../programa/clases/B30/B30-C04-manchas-solares/CLASE.md); [B35-C07 · Congelamiento del flujo magnético y conservación en MHD ideal](../programa/clases/B35/B35-C07-congelamiento-del-flujo-magnetico-y-conservacion-en-mhd-ideal/CLASE.md).

### Flujo magnético congelado

- El flujo magnético congelado significa que, en un plasma muy conductor, `Φ = B R²` se mantiene al contraerse.

💡 **Contexto en la clase [B24-C11](../programa/clases/B24/B24-C11-rotacion-y-campos-magneticos/CLASE.md):**
- **Idea central (modelo mental):** Una patinadora que recoge los brazos gira más rápido; un imán que se comprime concentra sus líneas de campo. Una estrella que se contrae hace ambas cosas.
- 🎯 **Por qué importa:** La rotación y el campo explican por qué las estrellas jóvenes son más activas, por qué las enanas blancas y las estrellas de neutrones giran y se magnetizan tanto, y por qué no pueden girar a cualquier velocidad.
- 🔗 **Se estudia junto con:** velocidad de rotación, velocidad crítica, momento de inercia, momento angular.

📘 **Dónde se aprende** (1 clase): [B24-C11 · Rotación y campos magnéticos](../programa/clases/B24/B24-C11-rotacion-y-campos-magneticos/CLASE.md).

### Flujo másico

- El flujo másico es `ṁ = T/(I_sp g₀)`.
- El flujo másico `ṁ = ρ A u` es la masa que cruza una sección por unidad de tiempo.

💡 **Cómo se explica en la clase [B75-C10](../programa/clases/B75/B75-C10-maniobras-impulsivas/CLASE.md):**
- Dos cuerpos con `μ = 398 602,54 km³/s²` (masa de la ficha y `G` del JPL [S1, S2]), empuje constante `T = (T/W₀)·m₀·g₀`, dirección igual a la velocidad, flujo másico `ṁ = T/(I_sp g₀)` con `I_sp = 320 s` (sintético) y `m₀ = 1000 kg`.
- Paso 2 · Flujo másico. `ṁ = 0,5×1000/320 = 1,5625 kg/s`.
- 🎯 **Por qué importa:** El modelo impulsivo es útil, pero ¿cuándo es un buen modelo? La decisión central: ¿cuánto delta-v se pierde por quemar durante un tiempo finito y de qué depende, en particular del cociente empuje/peso?
- 🔗 **Se estudia junto con:** empuje finito, pérdida por empuje finito, cociente empuje/peso, quema prógrada.

📘 **Dónde se aprende** (2 clases): [B75-C10 · Maniobras impulsivas](../programa/clases/B75/B75-C10-maniobras-impulsivas/CLASE.md); [B79-C01 · Conservación de masa en fluidos](../programa/clases/B79/B79-C01-conservacion-de-masa-en-fluidos/CLASE.md).

### Flujo mínimo detectable

- El flujo mínimo detectable es la menor densidad de flujo que supera el umbral de SNR.

💡 **Cómo se explica en la clase [B56-C16](../programa/clases/B56/B56-C16-tecnofirmas-y-busqueda-seti/CLASE.md):**
- Definir tecnofirma, EIRP, flujo mínimo detectable y ecuación del radiómetro.
- 🎯 **Por qué importa:** Buscar tecnología exige saber qué flujo mínimo detecta un receptor y qué potencia debería tener un transmisor a una distancia dada. La decisión central: dados la temperatura del sistema, el área efectiva, el ancho de banda y el tiempo de integración, ¿qué flujo mínimo se detecta y hasta qué distancia llega un transmisor dado?
- 🔗 **Se estudia junto con:** tecnofirma, EIRP, ecuación del radiómetro, señal de banda estrecha.

📘 **Dónde se aprende** (1 clase): [B56-C16 · Tecnofirmas y búsqueda SETI](../programa/clases/B56/B56-C16-tecnofirmas-y-busqueda-seti/CLASE.md).

### Flujo molecular

- El camino libre medio es `λ = k_B T/(√2 π d² P)`. Flujo molecular es el régimen donde `λ` supera las dimensiones del sistema.

💡 **Cómo se explica en la clase [B84-C06](../programa/clases/B84/B84-C06-comportamiento-bajo-vacio/CLASE.md):**
- En órbita las moléculas viajan en línea recta hasta chocar con una pared: flujo molecular.
- Describir el régimen de flujo molecular y calcular el camino libre medio.
- 🎯 **Por qué importa:** Un recubrimiento de cadmio o de zinc que es inocuo en tierra puede desaparecer y contaminar ópticas en el vacío; un cálculo de un minuto lo descarta. La decisión central: ¿qué metales sobreviven sin protección al vacío a la temperatura de trabajo y cuáles se subliman?
- 🔗 **Se estudia junto con:** ley de Langmuir, Clausius–Clapeyron, camino libre medio.

📘 **Dónde se aprende** (1 clase): [B84-C06 · Comportamiento bajo vacío](../programa/clases/B84/B84-C06-comportamiento-bajo-vacio/CLASE.md).

### Flujo neto

- El flujo neto de un radiador es `ε σ (T⁴ − T_f⁴) − q_abs`.
- El flujo neto es ingresos menos costos e inversión de un año.

💡 **Cómo se explica en la clase [B85-C07](../programa/clases/B85/B85-C07-radiadores-espaciales/CLASE.md):**
- Q["Carga Q"] --> A["A = Q / flujo neto"]
- *Descripción textual:* la carga se divide por el flujo neto, que es la emisión menos lo absorbido del entorno; la aleta modifica el área efectiva.
- 🎯 **Por qué importa:** El área del radiador manda en masa, volumen y costo. La decisión central: ¿cuánta área necesita un radiador en el caso caliente de fin de vida y qué la reduce?
- 🔗 **Se estudia junto con:** área requerida, aleta radiante, eficiencia, espacio profundo.

📘 **Dónde se aprende** (2 clases): [B85-C07 · Radiadores espaciales](../programa/clases/B85/B85-C07-radiadores-espaciales/CLASE.md); [B126-C03 · Proyección de flujos de caja de un proyecto espacial](../programa/clases/B126/B126-C03-proyeccion-de-flujos-de-caja-de-un-proyecto-espacial/CLASE.md).

### Flujo numérico

- El flujo numérico `F_{i+½}` es la aproximación del flujo en esa interfaz.

💡 **Cómo se explica en la clase [B21-C01](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md):**
- Eso es conservación discreta, y vale para cualquier flujo numérico que use el mismo valor en la interfaz para las dos celdas vecinas.
- Para la advección `q_t + a q_x = 0` con `a > 0`, la información viene de la izquierda y el flujo numérico es `F_{i+½} = a q_i` (esquema contracorriente o *upwind*).
- 🎯 **Por qué importa:** Casi todo lo que fluye en el espacio —el viento solar, el gas de un disco de acreción, el gas que rodea a una nave en reentrada, la onda de choque de una eyección coronal— obedece leyes de conservación: una cantidad cambia en una región solo porque entra o sale por sus bordes.
- 🔗 **Se estudia junto con:** ley de conservación, vector de estado conservado, flujo, celda.

📘 **Dónde se aprende** (1 clase): [B21-C01 · Volúmenes finitos y solucionadores de Riemann para leyes de conservación](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md).

### Flujo operativo

- El flujo operativo es el margen bruto menos el gasto fijo.

💡 **Cómo se explica en la clase [B125-C06](../programa/clases/B125/B125-C06-plan-empresarial-de-una-empresa-espacial/CLASE.md):**
- Flujo libre `= operativo − capex` (`18` M u.m. en los trimestres 1, 2, 9, 10 y 15).
- El flujo operativo es positivo desde el trimestre `6`; la caja mínima es `−25,7` M u.m. en el trimestre `10`; la brecha de financiación es `25,7` M u.m.
- 🎯 **Por qué importa:** Integrar mercado, finanzas y operación en un plan es el cierre del módulo; el proyecto de B124 es general y no trata una empresa concreta con su caja. La decisión central: ¿cuánta caja necesita la empresa para llegar a su punto de equilibrio y qué supuestos pueden hundir el plan?
- 🔗 **Se estudia junto con:** flujo libre, caja, brecha de financiación, valor actual.

📘 **Dónde se aprende** (1 clase): [B125-C06 · Plan empresarial de una empresa espacial](../programa/clases/B125/B125-C06-plan-empresarial-de-una-empresa-espacial/CLASE.md).

### Flujo pistón (PFR)

- Mezcla completa (CSTR): tanque uniforme. Flujo pistón (PFR): flujo sin mezcla longitudinal.

💡 **Cómo se explica en la clase [B106-C26](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md):**
- Flujo pistón `S = S₀ e^{−kτ}`: al 90 %, `τ = ln 10/k = 4,6 h`, 15 L.
- Con 18 h totales: 1 tanque 30 mg/L; 2, 9,9; 3, 4,69; 6, 1,23; 20, 0,178; flujo pistón 0,037.
- 🎯 **Por qué importa:** Las aguas grises son el mayor volumen del lazo y su carga orgánica hay que destruirla antes de potabilizar. La decisión central: ¿qué volumen de biorreactor y qué desinfección dan la remoción y la reducción de microorganismos requeridas?
- 🔗 **Se estudia junto con:** Aguas grises, Biorreactor, Mezcla completa (CSTR), Chick–Watson.

📘 **Dónde se aprende** (1 clase): [B106-C26 · Tratamiento de aguas grises en hábitats](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md).

### Flujo residual

- Un flujo residual es el que no se aprovecha.

💡 **Cómo se explica en la clase [B59-C23](../programa/clases/B59/B59-C23-subproductos-y-flujos-residuales-de-procesos-isru/CLASE.md):**
- python programa/clases/B59/B59-C23-subproductos-y-flujos-residuales-de-procesos-isru/subproductos.py
- 🎯 **Por qué importa:** Producir un kilogramo de oxígeno genera toneladas de otras cosas. La decisión central: ¿qué masa de residuo o de subproducto aparece por cada kilogramo de producto?
- 🔗 **Se estudia junto con:** subproducto, ilmenita, colas, reducción con hidrógeno.

📘 **Dónde se aprende** (1 clase): [B59-C23 · Subproductos y flujos residuales de procesos ISRU](../programa/clases/B59/B59-C23-subproductos-y-flujos-residuales-de-procesos-isru/CLASE.md).

### Flujo solar

- El flujo solar `S ∝ 1/r²`.

💡 **Cómo se explica en la clase [B47-C22](../programa/clases/B47/B47-C22-misiones-de-fisica-solar-soho-sdo-y-solar-orbiter/CLASE.md):**
- Ejercicio 12. Integrador. Elabora tu *ficha de misiones de física solar*: L1, geosíncrona, órbita de perihelio, flujo y límites.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de misiones de física solar*: L1, geosíncrona, órbita de perihelio, flujo y límites.
- 🎯 **Por qué importa:** Cada órbita compra una ventaja y una dificultad. La decisión central: ¿qué punto o qué órbita da la vista del Sol que necesita el instrumento a un costo térmico y de enlace aceptable?
- 🔗 **Se estudia junto con:** punto de Lagrange L1, aproximación de Hill, órbita geosíncrona, perihelio.

📘 **Dónde se aprende** (1 clase): [B47-C22 · Misiones de física solar: SOHO, SDO y Solar Orbiter](../programa/clases/B47/B47-C22-misiones-de-fisica-solar-soho-sdo-y-solar-orbiter/CLASE.md).

### Flujo térmico superficial

- El flujo térmico superficial `q` es la potencia que atraviesa una superficie por unidad de área (W/m²).

💡 **Contexto en la clase [B65-C04](../programa/clases/B65/B65-C04-flujo-termico-planetario-y-balance-termico-del-interior/CLASE.md):**
- **Idea central (modelo mental):** Una casa pierde calor por las paredes; una parte la repone la calefacción (la producción radiactiva) y el resto la pierde el aire acumulado que se enfría (el enfriamiento secular).
- 🎯 **Por qué importa:** Un planeta se enfría en parte porque pierde calor guardado y en parte vive del que producen sus isótopos radiactivos. La decisión central: ¿qué fracción del calor que sale es producción actual y qué fracción es enfriamiento?
- 🔗 **Se estudia junto con:** geotermo, producción radiactiva, enfriamiento secular, razón de Urey.

📘 **Dónde se aprende** (1 clase): [B65-C04 · Flujo térmico planetario y balance térmico del interior](../programa/clases/B65/B65-C04-flujo-termico-planetario-y-balance-termico-del-interior/CLASE.md).

### FMA

- La FMA calcula `a·b + c` con un solo redondeo.

💡 **Cómo se explica en la clase [B14-C15](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md):**
- Con dos redondeos (multiplicar y redondear, luego sumar) el error máximo es `5,96 × 10⁻⁸`; con un solo redondeo (FMA simulado: se calcula exacto en `float64` y se redondea una vez), es `0`.
- Si una GPU usa FMA y la CPU no, sus resultados diferirán aunque ambas sean correctas (S1).
- 🎯 **Por qué importa:** Un equipo promete que su simulación irá «100 veces más rápido en GPU» y, al compararla con la de CPU, los resultados difieren en el séptimo dígito. ¿Error del código o característica de la máquina?
- 🔗 **Se estudia junto con:** GPU, transferencia, intensidad aritmética, reducción.

📘 **Dónde se aprende** (1 clase): [B14-C15 · Cálculo en GPU y limitaciones](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md).

### Focal

- La focal `f` es la distancia óptica entre la lente y el detector.
- La focal `f = pH/GSD` fija el tamaño de la imagen en el plano focal.

💡 **Cómo se explica en la clase [B57-C24](../programa/clases/B57/B57-C24-diseno-de-una-carga-util-de-observacion-terrestre/CLASE.md):**
- La línea focal mediría `218 mm` si fuera un solo detector (en la práctica se compone de varios).
- G["paso de pixel"] --> F["focal y campo de vision"]
- 🎯 **Por qué importa:** Cada requisito empuja a los demás: más resolución exige más datos, más barrido exige un campo de visión mayor, y el enlace de bajada limita cuánto se puede adquirir. La decisión central: ¿qué requisito se relaja cuando el presupuesto de datos no cierra?
- 🔗 **Se estudia junto con:** carga útil, presupuesto de datos, ciclo de trabajo, campo de visión.

📘 **Dónde se aprende** (2 clases): [B57-C24 · Diseño de una carga útil de observación terrestre](../programa/clases/B57/B57-C24-diseno-de-una-carga-util-de-observacion-terrestre/CLASE.md); [B63-C01 · Instrumentación de sondas y rovers planetarios](../programa/clases/B63/B63-C01-instrumentacion-de-sondas-y-rovers-planetarios/CLASE.md).

### Focal efectiva

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C17](../programa/clases/B41/B41-C17-telescopios-cassegrain-y-derivados/CLASE.md):**
- Como un periscopio que pliega la luz en dos: el secundario convexo la devuelve al primario y la focal efectiva es `m` veces la del primario en un tubo corto.
- La focal efectiva baja a 1600 mm y cambian `d`, `R₂`, `k₂`.
- 🎯 **Por qué importa:** Dos espejos permiten un tubo corto y focal larga, y distintos diseños eligen qué aberración corregir. La decisión central: ¿qué diseño corrige la coma y a qué costo?
- 🔗 **Se estudia junto con:** Cassegrain clásico, Dall-Kirkham, Ritchey-Chrétien, aumento del secundario.

📘 **Dónde se aprende** (1 clase): [B41-C17 · Telescopios Cassegrain y derivados](../programa/clases/B41/B41-C17-telescopios-cassegrain-y-derivados/CLASE.md).

### Foco

- Todas cumplen la propiedad foco–directriz: hay un punto (el foco) y una recta (la directriz) tales que la distancia de cada punto de la curva al foco es `e` veces su distancia a la directriz;

💡 **Cómo se explica en la clase [B04-C18](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md):**
- Fija el foco y el perihelio `q`, y mueve solo `e`: con `e = 0`, una circunferencia; al crecer `e < 1`, una elipse cada vez más estirada; en `e = 1`, la curva se abre y no vuelve (parábola); con `e > 1`, se abre aún más (hipérbola).
- Comprobar la propiedad foco–directriz `|PF| = e·d(P, directriz)`.
- 🎯 **Por qué importa:** En 2017 se descubrió un objeto que cruzaba el sistema solar con una órbita que no se cerraba: su excentricidad era mayor que 1. Eso significó que no estaba ligado al Sol: venía de fuera y se iba.
- 🔗 **Se estudia junto con:** cónica, propiedad foco–directriz, directriz, excentricidad.

📘 **Dónde se aprende** (1 clase): [B04-C18 · Cónicas y secciones orbitales](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md).

### Foco común

- Dos cónicas con foco común se describen con `(p, e, ϖ)` cada una.

💡 **Cómo se explica en la clase [B75-C21](../programa/clases/B75/B75-C21-interseccion-de-conicas-en-transferencias/CLASE.md):**
- Escribir las cónicas con foco común `r = p/(1 + e cos θ)`.
- Dos elipses con foco común se cortan en dos puntos si se solapan en radio (saliente y entrante).
- 🎯 **Por qué importa:** Una transferencia que apunta al radio medio de Marte puede pasar por dentro o por fuera de su órbita real, que es excéntrica. La decisión central: ¿dónde corta una elipse de transferencia a la órbita de Marte, a qué distancia y cuánto tarda en llegar allí?
- 🔗 **Se estudia junto con:** intersección, saliente, entrante.

📘 **Dónde se aprende** (1 clase): [B75-C21 · Intersección de cónicas en transferencias](../programa/clases/B75/B75-C21-interseccion-de-conicas-en-transferencias/CLASE.md).

### Foco objeto

- El foco objeto es el punto del eje conjugado con el infinito imagen.

💡 **Cómo se explica en la clase [B50-C04](../programa/clases/B50/B50-C04-telecentricidad-vineteo-y-diseno-del-campo/CLASE.md):**
- El foco objeto trazado en sentido inverso está en `z = -99,32886 mm`; el diafragma que anula el ángulo de salida, hallado por bisección, en `z = -99,32886 mm`.
- El ángulo de salida cambia de signo al cruzar el foco objeto.
- 🎯 **Por qué importa:** En un detector la luz que llega muy inclinada se pierde o se mezcla; en un espectrógrafo o un mosaico el viñeteo cambia el brillo según el campo. La decisión central: ¿dónde va el diafragma y cuánto campo se acepta con viñeteo?
- 🔗 **Se estudia junto con:** rayo principal, telecéntrico, viñeteo, área de intersección.

📘 **Dónde se aprende** (1 clase): [B50-C04 · Telecentricidad, viñeteo y diseño del campo](../programa/clases/B50/B50-C04-telecentricidad-vineteo-y-diseno-del-campo/CLASE.md).

### Foco paraxial

- El foco paraxial es el límite `h → 0`.
- El foco paraxial `R/2`.

💡 **Cómo se explica en la clase [B41-C04](../programa/clases/B41/B41-C04-espejos-esfericos-y-parabolicos/CLASE.md):**
- La esfera f/5 (`D = 200 mm`) forma en el foco paraxial un disco de unas `250,5 µm` de diámetro (aproximación de rayo marginal), muy por encima del disco de Airy (clase 12).
- En `R = 2000 mm`, el foco paraxial está a `1000 mm`.
- 🎯 **Por qué importa:** El espejo primario de un telescopio reflector es una superficie cónica. La decisión central: ¿por qué se usa un paraboloide y no una esfera?
- 🔗 **Se estudia junto con:** sagita, constante cónica, aberración esférica longitudinal, espejo cóncavo.

📘 **Dónde se aprende** (2 clases): [B41-C04 · Espejos esféricos y parabólicos](../programa/clases/B41/B41-C04-espejos-esfericos-y-parabolicos/CLASE.md); [B50-C01 · Trazado exacto de rayos y aberraciones de orden superior](../programa/clases/B50/B50-C01-trazado-exacto-de-rayos-y-aberraciones-de-orden-superior/CLASE.md).

### Focos

- Una elipse es el conjunto de puntos para los que la suma de las distancias a dos puntos fijos, los focos, es constante.

💡 **Cómo se explica en la clase [B04-C09](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md):**
- Los focos, en `(±c, 0)` con `c = √(a² − b²)`; equivalentemente `b = a√(1 − e²)`.
- Un punto cualquiera puede escribirse como `(a cos t, b sen t)`, y su suma de distancias a los focos vale `2a`: es la propiedad definitoria que el laboratorio comprueba en 52 puntos.
- 🎯 **Por qué importa:** Las órbitas de planetas y cometas son, en buena aproximación, elipses con el Sol en uno de sus focos. Si no sabes qué es un semieje, un foco o la excentricidad, no puedes leer una tabla de elementos orbitales ni distinguir una órbita casi circular, como la de la Tierra, de una muy alargada, como la del cometa Halley.
- 🔗 **Se estudia junto con:** circunferencia, elipse, semieje mayor, semieje menor.

📘 **Dónde se aprende** (1 clase): [B04-C09 · Circunferencias y elipses](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md).

### Focos tangencial y sagital

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C14](../programa/clases/B41/B41-C14-aberracion-cromatica-y-astigmatismo/CLASE.md):**
- Un vidrio ilustrativo tipo crown (`V = 64,14`) con `f = 1000 mm` separa los focos F y C `15,498 mm` (fórmula `f/V` = `15,591`); un espejo esférico de `R = 2000 mm` a `5°` separa los focos sagital y tangencial `7,6251 mm`.
- El script [cromatica.py](cromatica.py) calcula la dispersión, el número de Abbe y los focos tangencial y sagital (comprueba `f/V` a 3 % y los focos a `10⁻⁴`).
- 🎯 **Por qué importa:** El color y el astigmatismo degradan el campo de refractores y espejos. La decisión central: ¿cuánto se separan los focos por color y por plano?
- 🔗 **Se estudia junto con:** dispersión, número de Abbe, aberración cromática longitudinal, F, d, C.

📘 **Dónde se aprende** (1 clase): [B41-C14 · Aberración cromática y astigmatismo](../programa/clases/B41/B41-C14-aberracion-cromatica-y-astigmatismo/CLASE.md).

### Fondo

- El fondo (*background*) es el nivel del cielo sin fuentes; el ruido `σ` su desviación.
- Los conteos oscuros y el fondo son eventos sin señal.
- Un fotón de señal viene del láser reflejado; uno de fondo viene del Sol o del ruido del detector.

💡 **Cómo se explica en la clase [B15-C12](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md):**
- En el laboratorio, 100 fuentes brillantes de flujo 1000 ADU elevan la media del fondo a 102,50 ADU (real 100,0) y la desviación global a 10,34 (real 5,0).
- Ninguno es perfecto: las alas débiles de las fuentes siguen contaminando, por lo que en la práctica se enmascaran las fuentes y se repite (S1 usa un recorte a 3σ para el fondo).
- ⚠️ **Error frecuente:** Estimar el fondo con la media en un campo con fuentes. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Un catálogo de fuentes es el producto básico de una imagen astronómica, y de él salen cuentas, colores y candidatos a objetos nuevos. Si el umbral es bajo, el catálogo se llena de ruido; si es alto, se pierden las fuentes débiles.
- 🔗 **Se estudia junto con:** ruido, relación señal–ruido, filtro adaptado, umbral.

📘 **Dónde se aprende** (6 clases): [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B31-C16 · Astropartículas de alta energía](../programa/clases/B31/B31-C16-astroparticulas-de-alta-energia/CLASE.md); [B31-C18 · Restricciones experimentales de teorías](../programa/clases/B31/B31-C18-restricciones-experimentales-de-teorias/CLASE.md); [B47-C03 · Telescopios ultravioleta](../programa/clases/B47/B47-C03-telescopios-ultravioleta/CLASE.md); [B57-C11 · LiDAR satelital](../programa/clases/B57/B57-C11-lidar-satelital/CLASE.md); [B92-C05 · Receptores y detectores para comunicaciones ópticas](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md).

### Fondo compartido

- El fondo compartido reparte por igual una fracción `q` de la capacidad total.

💡 **Cómo se explica en la clase [B119-C34](../programa/clases/B119/B119-C34-equidad-de-acceso-al-espacio/CLASE.md):**
- El acceso real depende de acuerdos, precios y regulación; un fondo compartido plantea además quién lo financia y cómo se decide (C36).
- Q["Fondo compartido q"] --> N["Acceso nuevo"]
- 🎯 **Por qué importa:** El acceso desigual al espacio es un asunto de gobernanza que el catálogo no trata; esta clase da las herramientas de medición antes de las discusiones de política (C25, C36). La decisión central: ¿qué tan desigual es el acceso y cuánto lo reduce una regla de uso compartido?
- 🔗 **Se estudia junto con:** Gini, curva de Lorenz, índice de Atkinson, equidad.

📘 **Dónde se aprende** (1 clase): [B119-C34 · Equidad de acceso al espacio](../programa/clases/B119/B119-C34-equidad-de-acceso-al-espacio/CLASE.md).

### Fondo cósmico de microondas

- El fondo cósmico de microondas es radiación antigua que llena el cielo; sirve para deducir parámetros cosmológicos bajo un modelo.

💡 **Cómo se explica en la clase [B01-C16](../programa/clases/B01/B01-C16-expansion-del-universo-como-observacion/CLASE.md):**
- El análisis final del satélite Planck del fondo cósmico de microondas, bajo el modelo ΛCDM de seis parámetros, da `H₀ = 67,4 ± 0,5 km/s/Mpc` (S1).
- 🎯 **Por qué importa:** En C01 «medimos» una distancia de 43 Mpc con `H₀ = 70`. Pero ese 70 no es un dato único: Planck 2018 da 67,4 ± 0,5 y SH0ES da 73,04 ± 1,04, ambos en km/s/Mpc (S1, S2).
- 🔗 **Se estudia junto con:** constante de Hubble, ley de Hubble, tiempo de Hubble, expansión.

📘 **Dónde se aprende** (1 clase): [B01-C16 · Expansión del universo como observación](../programa/clases/B01/B01-C16-expansion-del-universo-como-observacion/CLASE.md).

### Fondo cósmico de microondas (CMB)

- El fondo cósmico de microondas (CMB) es la radiación térmica relicta.

💡 **Contexto en la clase [B26-C15](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md):**
- **Idea central (modelo mental):** El universo temprano fue un horno en equilibrio térmico. Cuando se enfrió y se hizo transparente, la radiación quedó con la forma del cuerpo negro y desde entonces solo cambia su temperatura.
- 🎯 **Por qué importa:** El fondo de microondas es la reliquia más antigua observable y da los parámetros del modelo cosmológico. Entender su espectro de cuerpo negro permite calibrar un instrumento, estimar el contenido de fotones y comprender por qué un solo número, la razón barión–fotón, resume tanta física.
- 🔗 **Se estudia junto con:** función de Planck, densidad numérica de fotones, frecuencia del máximo, energía media.

📘 **Dónde se aprende** (1 clase): [B26-C15 · Radiación cósmica de fondo](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md).

### Fondo de cielo B

- El fondo de cielo `B` es la luz de fondo, en `e⁻/s/píxel`.

💡 **Cómo se explica en la clase [B13-C15](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md):**
- El cielo aporta `86 %` de la varianza: aquí el detector está limitado por el fondo, no por la lectura.
- 🎯 **Por qué importa:** Una cámara espacial debe decidir cuánto tiempo exponer para detectar una fuente débil con una relación señal-ruido (SNR) dada. Exponer poco no la detecta; exponer demasiado satura los píxeles brillantes o desperdicia tiempo de misión.
- 🔗 **Se estudia junto con:** ruido de disparo, corriente de oscuridad D, ruido de lectura R, ganancia.

📘 **Dónde se aprende** (1 clase): [B13-C15 · Sensibilidad de detectores](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md).

### Fondo térmico

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C04](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md):**
- *Descripción textual:* la ley de Planck se verifica con dos relaciones y se usa para el fondo térmico y la temperatura de operación.
- Ejercicio 9 · transferencia. Transferencia. ¿Por qué el fondo térmico cae mucho más rápido que `σT⁴`?
- 🎯 **Por qué importa:** Enfriar un telescopio cuesta masa, potencia y complejidad. La decisión central: ¿a qué temperatura el fondo propio deja de dominar sobre el detector?
- 🔗 **Se estudia junto con:** ley de Planck, ley de Wien, ley de Stefan-Boltzmann, emisividad.

📘 **Dónde se aprende** (1 clase): [B47-C04 · Telescopios infrarrojos](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md).

### Forma

- Su forma (`shape`) es la tupla de longitudes por eje; sus ejes se numeran desde 0.

💡 **Cómo se explica en la clase [B14-C02](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md):**
- Primero, escribe las formas alineadas por la derecha: `(6,1,3)` y `(1,5,3)`.
- Tercero, el resultado tiene la forma `(6,5,3)`.
- ⚠️ **Error frecuente:** Predecir mal la forma. Se corrige escribiendo las formas antes de operar (ejercicios 1 y 2).
- 🎯 **Por qué importa:** Una constelación de seis satélites y cinco estaciones en tierra producen treinta distancias. Un catálogo de estrellas produce millones.
- 🔗 **Se estudia junto con:** arreglo, ejes, tipo, pasos.

📘 **Dónde se aprende** (1 clase): [B14-C02 · Arreglos multidimensionales NumPy](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md).

### Forma canónica

- La forma canónica es una serialización con orden y formato fijos (claves ordenadas, sin espacios variables) para que dos registros iguales den la misma huella.
- La forma canónica ordena las claves y fija los separadores.

💡 **Cómo se explica en la clase [B50-C06](../programa/clases/B50/B50-C06-software-de-diseno-optico-modelos-reproducibles-y-verificacion/CLASE.md):**
- Con las claves en otro orden la huella es la misma, porque se serializa en forma canónica.
- M["modelo JSON"] --> H["forma canónica"]
- 🎯 **Por qué importa:** Los programas de diseño óptico son cajas con muchas opciones: lo que hace reproducible un diseño es el archivo, sus unidades, su versión y sus pruebas. La decisión central: ¿cómo se demuestra que un modelo sigue siendo el mismo y sigue dando lo mismo?
- 🔗 **Se estudia junto con:** modelo reproducible, huella, regresión, reversibilidad.

📘 **Dónde se aprende** (2 clases): [B23-C07 · Trazabilidad científica de resultados](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md); [B50-C06 · Software de diseño óptico: modelos reproducibles y verificación](../programa/clases/B50/B50-C06-software-de-diseno-optico-modelos-reproducibles-y-verificacion/CLASE.md).

### Forma de Arrhenius modificada

- La forma de Arrhenius modificada (tipo Kooij) es `k = α (T/300)^β exp(−γ/T)`.

💡 **Contexto en la clase [B60-C02](../programa/clases/B60/B60-C02-coeficientes-de-velocidad-dependientes-de-la-temperatura-y-bases-cineticas/CLASE.md):**
- **Idea central (modelo mental):** Como una receta con tres perillas: `α` pone el nivel, `β` la pendiente suave con la temperatura y `γ` la caída brusca a baja temperatura. Girarlas fuera del rango donde se calibraron es adivinar.
- 🎯 **Por qué importa:** Un modelo de nube a 10 K usa coeficientes que se midieron o calcularon a otras temperaturas. La decisión central: ¿hasta dónde se puede confiar en un ajuste de `k(T)` fuera del intervalo donde se ajustó?
- 🔗 **Se estudia junto con:** base cinética, intervalo de validez.

📘 **Dónde se aprende** (1 clase): [B60-C02 · Coeficientes de velocidad dependientes de la temperatura y bases cinéticas](../programa/clases/B60/B60-C02-coeficientes-de-velocidad-dependientes-de-la-temperatura-y-bases-cineticas/CLASE.md).

### Forma de información

- La forma de información suma las informaciones de las mediciones independientes: `Λ = Σ Λ_i`, y `P = Λ⁻¹`.

💡 **Contexto en la clase [B80-C07](../programa/clases/B80/B80-C07-fusion-radio-optica-en-navegacion-de-espacio-profundo/CLASE.md):**
- 🎯 **Por qué importa:** B74-C04 y B74-C13 tratan la medición radiométrica y la óptica por separado. La decisión central: ¿en qué eje aporta cada sensor y cuánto mejora la incertidumbre al combinarlos?
- 🔗 **Se estudia junto con:** incertidumbre lateral, geometría.

📘 **Dónde se aprende** (1 clase): [B80-C07 · Fusión radio-óptica en navegación de espacio profundo](../programa/clases/B80/B80-C07-fusion-radio-optica-en-navegacion-de-espacio-profundo/CLASE.md).

### Forma de Joseph

- La forma de Joseph conserva la simetría de `P`.
- La forma de Joseph conserva la simetría y la semidefinición positiva de `P` en cada actualización.

💡 **Cómo se explica en la clase [B74-C09](../programa/clases/B74/B74-C09-filtro-de-kalman-extendido/CLASE.md):**
- Corrección: `K = P⁻ Hᵀ (H P⁻ Hᵀ + R)⁻¹`, `x = x⁻ + K (y − h(x⁻))`, y `P` en forma de Joseph.
- Ejercicio 3 · guiado. ¿Por qué se usa la forma de Joseph?
- 🎯 **Por qué importa:** Una órbita no es lineal en el estado, pero a cortos intervalos y con errores pequeños se comporta casi como tal. La decisión central: ¿hasta cuándo es válida la linealización del EKF y cómo me doy cuenta de que dejó de serlo?
- 🔗 **Se estudia junto con:** EKF, matriz de transición, jacobiano de medida, NEES.

📘 **Dónde se aprende** (2 clases): [B74-C09 · Filtro de Kalman extendido](../programa/clases/B74/B74-C09-filtro-de-kalman-extendido/CLASE.md); [B74-C18 · Estimación autónoma a bordo](../programa/clases/B74/B74-C18-estimacion-autonoma-a-bordo/CLASE.md).

### Forma de Newton

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B41-C06](../programa/clases/B41/B41-C06-distancias-focales-y-formacion-de-imagen/CLASE.md):**
- **Idea central (modelo mental):** Como un proyector: al acercar la diapositiva al foco, la imagen se aleja y crece; cuando la diapositiva pasa al interior del foco, la imagen deja de proyectarse (virtual).
- 🎯 **Por qué importa:** El foco de una cámara o de un telescopio decide el tamaño de la imagen. La decisión central: ¿dónde cae la imagen y de qué tamaño es?
- 🔗 **Se estudia junto con:** distancia objeto, distancia imagen, aumento lateral, imagen real.

📘 **Dónde se aprende** (1 clase): [B41-C06 · Distancias focales y formación de imagen](../programa/clases/B41/B41-C06-distancias-focales-y-formacion-de-imagen/CLASE.md).

### Forma de onda

- La forma de onda es la potencia del eco en función del tiempo; su flanco de subida marca la superficie media.

💡 **Cómo se explica en la clase [B57-C09](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md):**
- Formas de onda observadas con procedencia, la órbita precisa y las correcciones del producto.
- 🎯 **Por qué importa:** La altura del mar cambia unos milímetros por año, pero el eco de un pulso es ruidoso. La decisión central: ¿cuántos pulsos hay que promediar y cómo se ajusta el eco para que el error de distancia del ajuste se reduzca lo necesario?
- 🔗 **Se estudia junto con:** tiempo de ida y vuelta, distancia, flanco de subida, reajuste.

📘 **Dónde se aprende** (1 clase): [B57-C09 · Altimetría satelital](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md).

### Forma débil

- La forma débil de `−u″ = f` con `u(0) = u(1) = 0` multiplica por una función de prueba `v` (también nula en los extremos) e integra por partes: `∫ u′ v′ dx = ∫ f v dx` para toda `v`.

💡 **Cómo se explica en la clase [B11-C15](../programa/clases/B11/B11-C15-elementos-finitos-introductorios/CLASE.md):**
- A["−u″ = f, u(0)=u(1)=0"] --> B["Forma débil:<br/>∫ u′v′ = ∫ f v"]
- *Descripción textual:* de la ecuación se pasa a la forma débil; se aproxima la solución con funciones sombrero; se ensambla el sistema `K u = b` sumando las contribuciones de los elementos; se resuelve y se mide el error en las normas `L²` y `H¹`.
- 🎯 **Por qué importa:** Las estructuras y los escudos de una nave no son barras rectas con mallas regulares. El análisis térmico y estructural de ingeniería espacial se hace casi siempre con elementos finitos sobre geometrías reales.
- 🔗 **Se estudia junto con:** función de prueba, malla, elementos, función sombrero.

📘 **Dónde se aprende** (1 clase): [B11-C15 · Elementos finitos introductorios](../programa/clases/B11/B11-C15-elementos-finitos-introductorios/CLASE.md).

### Forma estándar

- La forma estándar es la que usa la norma de `x` sin modificar (en la forma general, se penaliza `‖L (x − x₀)‖` con una matriz `L` y un estimado previo `x₀`;

💡 **Cómo se explica en la clase [B22-C02](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md):**
- Dado `A` (`m × n`) y datos `b`, la solución de Tikhonov en forma estándar es (S2, ec. 1 con `L = I` y `x₀ = 0`):
- 🎯 **Por qué importa:** Si no puedes confiar en `x = A⁻¹ b` y no puedes bajar el ruido a voluntad, necesitas una regla que ignore lo que los datos no pueden decir. Esa regla debe tener una perilla: cuánto ignorar.
- 🔗 **Se estudia junto con:** solución regularizada, desajuste, penalización, parámetro de regularización.

📘 **Dónde se aprende** (1 clase): [B22-C02 · Regularización de Tikhonov](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md).

### Forma general

- La forma general de la cuadrática es `ax² + bx + c = 0` con `a ≠ 0`.

💡 **Contexto en la clase [B04-C02](../programa/clases/B04/B04-C02-ecuaciones-lineales-y-cuadraticas/CLASE.md):**
- **Idea central (modelo mental):** Una ecuación es una balanza en equilibrio: lo que hagas de un lado lo haces del otro. Para la lineal alcanza con deshacer operaciones en orden inverso. Para la cuadrática, piensa que `y = ax² + bx + c` dibuja una curva en forma de «U» (o «∩»), una parábola, y las raíces son los puntos donde corta el eje horizontal: dos, uno o ninguno.
- 🎯 **Por qué importa:** Una sonda desciende hacia la Luna; un instrumento cae desde una mesa de trabajo; una señal de radio viaja hasta un espejo y vuelve. En cada caso hay un número que no conoces (un tiempo, una distancia) y una relación que lo liga a otros que sí conoces.
- 🔗 **Se estudia junto con:** ecuación, resolverla, lineal, cuadrática.

📘 **Dónde se aprende** (1 clase): [B04-C02 · Ecuaciones lineales y cuadráticas](../programa/clases/B04/B04-C02-ecuaciones-lineales-y-cuadraticas/CLASE.md).

### Forma indeterminada

- Una forma indeterminada `0/0` es un cociente cuyo numerador y denominador tienden ambos a 0: no dice nada por sí sola.

💡 **Contexto en la clase [B09-C01](../programa/clases/B09/B09-C01-limites-de-funciones-reales/CLASE.md):**
- **Idea central (modelo mental):** Imagina un túnel horizontal de altura `2ε` alrededor del valor `L`. Decir que el límite es `L` es afirmar que, por pequeño que sea el túnel, existe un intervalo `δ` alrededor de `a` dentro del cual la gráfica no se sale. Importa la vecindad de `a`, no el punto `a`.
- 🎯 **Por qué importa:** Los astrónomos miden distancias a estrellas cercanas por paralaje: un ángulo diminuto, de fracciones de segundo de arco. Con ángulos tan pequeños, `sin t`, `tan t` y `t` casi coinciden, y casi todos los cálculos prácticos los sustituyen.
- 🔗 **Se estudia junto con:** función, límite, sin importar el valor de f en a, límite lateral.

📘 **Dónde se aprende** (1 clase): [B09-C01 · Límites de funciones reales](../programa/clases/B09/B09-C01-limites-de-funciones-reales/CLASE.md).

### Forma molecular

- La geometría electrónica describe cómo se distribuyen todos los dominios; la forma molecular describe sólo dónde están los átomos.

💡 **Cómo se explica en la clase [B06-C05](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md):**
- Distinguir geometría electrónica de forma molecular.
- 🎯 **Por qué importa:** El dióxido de carbono es el 95,1 % de la atmósfera de Marte en volumen (S2), y los hielos de las nubes densas del medio interestelar contienen, según un estudio con el telescopio James Webb, agua y CO₂ entre otras especies (S3, que se leyó sólo en resumen).
- 🔗 **Se estudia junto con:** dominio de electrones, modelo de repulsión de pares de valencia, geometría electrónica, lineal.

📘 **Dónde se aprende** (1 clase): [B06-C05 · Moléculas y geometría molecular](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md).

### Forma suave

- La forma suave reparte el escalón en el costo variable.

💡 **Cómo se explica en la clase [B124-C22](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md):**
- La forma suave `F/(p₀ − v − S/cap) = 1515,2` difiere en `27,8`, menos que un tramo de capacidad: sirve como aproximación, no reemplaza el cálculo exacto.
- Por forma suave: costo variable efectivo `v + S/cap`.
- 🎯 **Por qué importa:** B124 trata financiamiento, pero un servicio sostenible depende de un modelo de costo que explique cómo cambia el costo medio con el volumen. La decisión central: ¿a qué precio y con qué volumen el servicio cubre sus costos, y cuánto riesgo tiene si la demanda varía?
- 🔗 **Se estudia junto con:** costo fijo, variable, escalonado, costo medio.

📘 **Dónde se aprende** (1 clase): [B124-C22 · Modelo de costo de un servicio de datos](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md).

### Forma vectorial de Snell

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B41-C08](../programa/clases/B41/B41-C08-trazado-de-rayos-para-telescopios/CLASE.md):**
- **Idea central (modelo mental):** Como disparar con una mira exacta y otra aproximada: con tiros cerca del eje coinciden; con tiros desviados la aproximación falla, y el error crece con el cuadrado de la desviación.
- 🎯 **Por qué importa:** Los programas de diseño óptico trazan rayos exactos. La decisión central: ¿cuándo se separa el rayo real del paraxial y cómo crece esa diferencia?
- 🔗 **Se estudia junto con:** trazado exacto, aproximación paraxial, distancia focal posterior (BFD), aberración esférica longitudinal.

📘 **Dónde se aprende** (1 clase): [B41-C08 · Trazado de rayos para telescopios](../programa/clases/B41/B41-C08-trazado-de-rayos-para-telescopios/CLASE.md).

### Formación estelar

- La densidad superficial de gas `Σ_gas` y de formación estelar `Σ_SFR` se miden en `M☉ pc⁻²` y `M☉ año⁻¹ kpc⁻²`.

💡 **Cómo se explica en la clase [B25-C05](../programa/clases/B25/B25-C05-regiones-de-formacion-estelar/CLASE.md):**
- Kennicutt (S1) midió, para 61 espirales normales y 36 galaxias con brotes de formación estelar seleccionadas en infrarrojo, la relación entre el ritmo de formación y la densidad de gas, y halló que un índice de Schmidt `N = 1,4 ± 0,15` representa la muestra combinada.
- Estimar una tasa de formación estelar a partir de una eficiencia por tiempo de caída libre.
- 🎯 **Por qué importa:** Una galaxia no convierte todo su gas en estrellas a la vez: lo hace a un ritmo que puede medirse y comparar. Entender las regiones donde nacen las estrellas masivas permite reconocerlas desde lejos, y entender la relación entre gas y ritmo de formación permite saber cuánto tiempo puede una galaxia seguir formando estrellas.
- 🔗 **Se estudia junto con:** región HII, tasa de fotones ionizantes, recombinación, esfera de Strömgren.

📘 **Dónde se aprende** (1 clase): [B25-C05 · Regiones de formación estelar](../programa/clases/B25/B25-C05-regiones-de-formacion-estelar/CLASE.md).

### Formato de texto con metadatos

- Un formato de texto con metadatos guarda también unidades y máscara; el que usamos es ECSV, escrito por Astropy.

💡 **Cómo se explica en la clase [B14-C05](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md):**
- El formato ECSV (texto con cabecera) conserva unidades, máscara y metadatos.
- 🎯 **Por qué importa:** Un catálogo de estrellas no es una lista de números: cada columna tiene una unidad, algunas filas no tienen paralaje, y la tabla viene de un instrumento, una época y una versión. Si pierdes eso al copiar los datos a un arreglo, pierdes la mitad del significado.
- 🔗 **Se estudia junto con:** tabla, fila, columna, catálogo.

📘 **Dónde se aprende** (1 clase): [B14-C05 · Tablas astronómicas y catálogos](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md).

### Fórmula

- Una fórmula es una ecuación entre magnitudes;
- Una fórmula relaciona símbolos con una igualdad.

💡 **Cómo se explica en la clase [B03-C12](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md):**
- Cuando leas una fórmula, clasifica cada símbolo.
- S["Símbolo en una fórmula"] --> V{"¿Cambia dentro del problema?"}
- 🎯 **Por qué importa:** La masa del Sol se conoce con unas cinco cifras. Sin embargo, el producto `GM` del Sol se conoce con diez, y la constante `G` por sí sola con apenas cinco.
- 🔗 **Se estudia junto con:** variable, parámetro, constante, exacta por definición.

📘 **Dónde se aprende** (2 clases): [B03-C12 · Variables y constantes científicas](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md); [B03-C14 · Despeje de ecuaciones elementales](../programa/clases/B03/B03-C14-despeje-de-ecuaciones-elementales/CLASE.md).

### Fórmula de Bethe-Bloch

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B47-C09](../programa/clases/B47/B47-C09-detectores-de-particulas-instrumentacion-y-observatorios-espaciales/CLASE.md):**
- **Idea central (modelo mental):** Una partícula que atraviesa materia es como un coche en barro: frena más cuanto más lento va, y al final se detiene de golpe, depositando casi toda su energía.
- 🎯 **Por qué importa:** Medir ΔE y E permite identificar la partícula. La decisión central: ¿qué espesor de detector y qué energía separan protones de partículas alfa?
- 🔗 **Se estudia junto con:** poder de frenado, alcance CSDA, pico de Bragg, telescopio ΔE–E.

📘 **Dónde se aprende** (1 clase): [B47-C09 · Detectores de partículas — Instrumentación y observatorios espaciales](../programa/clases/B47/B47-C09-detectores-de-particulas-instrumentacion-y-observatorios-espaciales/CLASE.md).

### Fórmula de Bruns

- La fórmula de Bruns es `N = T/g` con `T` el potencial perturbador.

💡 **Contexto en la clase [B53-C04](../programa/clases/B53/B53-C04-geoides-y-elipsoides/CLASE.md):**
- **Idea central (modelo mental):** Analogía: una gota de agua girando: se achata por la rotación y se abomba sobre una piedra pesada que está debajo.
- 🎯 **Por qué importa:** Una altura solo tiene sentido respecto de una superficie de referencia. La decisión central: ¿contra qué superficie se mide la altura y cuánto se aparta el geoide de ella?
- 🔗 **Se estudia junto con:** geoide, elipsoide de referencia, ondulación.

📘 **Dónde se aprende** (1 clase): [B53-C04 · Geoides y elipsoides](../programa/clases/B53/B53-C04-geoides-y-elipsoides/CLASE.md).

### Fórmula de Edelbaum

- La fórmula de Edelbaum da el `Δv` mínimo de una espiral con cambio de inclinación `Δi`: `Δv = √(v₀² − 2 v₀ v₁ cos(π/2 · Δi) + v₁²)`.

💡 **Cómo se explica en la clase [B81-C04](../programa/clases/B81/B81-C04-trayectorias-espirales-de-bajo-empuje/CLASE.md):**
- Con `Δi = 28,5°` la fórmula de Edelbaum da `5783,75 m/s`: 29,4 % más que el caso coplanar, con un tiempo de `66,942 d`.
- Añadir el cambio de plano con la fórmula de Edelbaum.
- 🎯 **Por qué importa:** Una espiral de bajo empuje cuesta más `Δv` que un impulso (Hohmann) pero ahorra propelente por su alto `Isp`. La decisión central: ¿cuánto `Δv` y cuánto tiempo cuesta pasar de una órbita circular a otra, y cuánto más si además hay que cambiar el plano?
- 🔗 **Se estudia junto con:** espiral tangencial, ecuación promediada.

📘 **Dónde se aprende** (1 clase): [B81-C04 · Trayectorias espirales de bajo empuje](../programa/clases/B81/B81-C04-trayectorias-espirales-de-bajo-empuje/CLASE.md).

### Fórmula de Euler

- La fórmula de Euler es `e^{iθ} = cos θ + i sen θ`.

💡 **Contexto en la clase [B15-C04](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md):**
- **Idea central (modelo mental):** Un prisma separa la luz blanca en colores; la DFT separa una serie en frecuencias. Cada `X[k]` es un número complejo: su módulo dice cuánto de la frecuencia `k` hay; su ángulo (la fase) dice cuándo está el máximo de esa oscilación. Analogía: el prisma.
- 🎯 **Por qué importa:** Si una estrella pulsa con una pequeña amplitud en medio del ruido, mirar la curva de luz no la revela, pero su espectro de frecuencias sí: un pico a una frecuencia concreta. Lo mismo ocurre con una vibración en una estructura espacial, una señal de radio o un periodo en un registro geofísico.
- 🔗 **Se estudia junto con:** número complejo, módulo, transformada de Fourier continua, transformada discreta de Fourier (DFT).

📘 **Dónde se aprende** (1 clase): [B15-C04 · Transformada de Fourier](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md).

### Fórmula de Friis

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B49-C06](../programa/clases/B49/B49-C06-amplificadores-de-bajo-ruido-lna-tecnologia-ganancia-y-adaptacion/CLASE.md):**
- **Idea central (modelo mental):** Como una cañería con fugas: una fuga al principio pierde más caudal útil que una al final, donde ya hay mucha presión.
- 🎯 **Por qué importa:** Una décima de decibelio antes del primer amplificador cuesta más que mejorar el mezclador. La decisión central: ¿qué bloque domina la temperatura de ruido y qué pérdidas deben evitarse antes de él?
- 🔗 **Se estudia junto con:** temperatura de ruido, cifra de ruido, ganancia disponible, factor Y.

📘 **Dónde se aprende** (1 clase): [B49-C06 · Amplificadores de bajo ruido (LNA): tecnología, ganancia y adaptación](../programa/clases/B49/B49-C06-amplificadores-de-bajo-ruido-lna-tecnologia-ganancia-y-adaptacion/CLASE.md).

### Fórmula de Friis para el ruido

- La fórmula de Friis para el ruido da `T = T₁ + T₂/G₁ + T₃/(G₁G₂) + …`.

💡 **Cómo se explica en la clase [B89-C07](../programa/clases/B89/B89-C07-figura-de-ruido-de-receptor/CLASE.md):**
- La fórmula de Friis en factores de ruido da lo mismo (diferencia menor que 10⁻⁹ dB).
- El script [ruido.py](ruido.py) calcula la temperatura de ruido de tres cadenas con Friis y la contrasta con la fórmula en factores de ruido (comprueba diferencia < 1e-9 dB); obtiene `T_sis`, `G/T` y `N₀`.
- 🎯 **Por qué importa:** La primera etapa de una cadena receptora decide casi todo el ruido: un amplificador de bajo ruido bien colocado vale muchos decibelios de `G/T`. La decisión central: ¿qué orden y qué componentes dan la menor temperatura de sistema y el mayor `G/T`?
- 🔗 **Se estudia junto con:** temperatura de ruido, figura de ruido, temperatura de sistema, G/T.

📘 **Dónde se aprende** (1 clase): [B89-C07 · Figura de ruido de receptor](../programa/clases/B89/B89-C07-figura-de-ruido-de-receptor/CLASE.md).

### Fórmula de Kasten y Young

- La fórmula de Kasten y Young `X = 1/[cos z + 0,50572 (96,07995 − z)^−1,6364]`.
- La fórmula de Kasten y Young corrige la curvatura.

💡 **Cómo se explica en la clase [B45-C20](../programa/clases/B45/B45-C20-campana-fotometrica-o-espectroscopica/CLASE.md):**
- La fórmula de Kasten-Young (leída en la página de Wikipedia citada) da `0,99971` en el cenit y a 80° vale `5,586` frente a `5,759` de `sec z`.
- 🎯 **Por qué importa:** Una campaña mal planificada gasta noches sin llegar a la precisión pedida. La decisión central: ¿cuánto exponer, durante cuánto tiempo y con qué precisión por punto?
- 🔗 **Se estudia junto con:** masa de aire, ángulo horario, extinción, punto cero.

📘 **Dónde se aprende** (2 clases): [B45-C20 · Campaña fotométrica o espectroscópica](../programa/clases/B45/B45-C20-campana-fotometrica-o-espectroscopica/CLASE.md); [B45-C22 · Extinción atmosférica, masa de aire y coeficientes de color](../programa/clases/B45/B45-C22-extincion-atmosferica-masa-de-aire-y-coeficientes-de-color/CLASE.md).

### Fórmula de Rodrigues

- La fórmula de Rodrigues da la rotación de ángulo `θ` alrededor de `u`: `R = I + sin θ K + (1 − cos θ) K²`.

💡 **Contexto en la clase [B10-C13](../programa/clases/B10/B10-C13-matrices-de-rotacion-tridimensional/CLASE.md):**
- **Idea central (modelo mental):** Una matriz de rotación dice dónde caen los tres ejes del cuerpo: su primera columna es el eje `x` del cuerpo en el sistema inercial, la segunda el `y`, la tercera el `z`.
- 🎯 **Por qué importa:** La actitud de un satélite (hacia dónde apuntan sus ejes) se guarda como una matriz de rotación: sus columnas son los ejes del cuerpo expresados en el sistema inercial. Con ella, un seguidor estelar, un panel o una antena se orientan sin ambigüedad.
- 🔗 **Se estudia junto con:** rotaciones elementales, grupo SO(3), antisimétrica, matriz de transformación de marco.

📘 **Dónde se aprende** (1 clase): [B10-C13 · Matrices de rotación tridimensional](../programa/clases/B10/B10-C13-matrices-de-rotacion-tridimensional/CLASE.md).

### Fórmula de Ruze

- La fórmula de Ruze da la eficiencia por superficie `exp(−(4πε/λ)²)`.

💡 **Cómo se explica en la clase [B91-C04](../programa/clases/B91/B91-C04-antenas-desplegables-y-estructuras-de-gran-apertura/CLASE.md):**
- Calcular la ganancia de un reflector con error de superficie con la fórmula de Ruze.
- 🎯 **Por qué importa:** Una malla desplegable pesa poco y cabe plegada, pero su precisión de forma limita la frecuencia útil. La decisión central: ¿hasta qué frecuencia vale la pena usar un reflector con un error de superficie dado, y qué término del presupuesto de error conviene reducir?
- 🔗 **Se estudia junto con:** error rms de superficie, frecuencia óptima, presupuesto RSS, malla.

📘 **Dónde se aprende** (1 clase): [B91-C04 · Antenas desplegables y estructuras de gran apertura](../programa/clases/B91/B91-C04-antenas-desplegables-y-estructuras-de-gran-apertura/CLASE.md).

### Fórmula empírica

- Una fórmula empírica da la proporción más simple entre los átomos (CH₂ para el eteno y el ciclohexano).

💡 **Cómo se explica en la clase [B06-C07](../programa/clases/B06/B06-C07-estequiometria-elemental/CLASE.md):**
- Deducir una fórmula empírica a partir de porcentajes.
- El script [composicion_atmosferas.py](composicion_atmosferas.py) calcula la masa molar media de las atmósferas de Marte, Venus y la Tierra y las compara con los pesos moleculares de la NASA; también calcula composiciones porcentuales de H₂O y CO₂ y la fórmula empírica del CO₂.
- ⚠️ **Error frecuente:** Pensar que la fórmula empírica es la molecular. Se corrige con el ejercicio 8.
- 🎯 **Por qué importa:** Si quieres saber cuánto pesa una columna de atmósfera de Marte, necesitas su masa molar media, y para eso, su composición. La NASA publica la composición en volumen de las atmósferas de Marte, Venus y la Tierra y también un «peso molecular» medio (S1, S2, S3).
- 🔗 **Se estudia junto con:** fórmula molecular, composición porcentual, fracción molar, masa molar media.

📘 **Dónde se aprende** (1 clase): [B06-C07 · Estequiometría elemental](../programa/clases/B06/B06-C07-estequiometria-elemental/CLASE.md).

### Fórmula molecular

- Una fórmula molecular dice cuántos átomos de cada elemento tiene una molécula (H₂O, CO₂).

💡 **Cómo se explica en la clase [B06-C07](../programa/clases/B06/B06-C07-estequiometria-elemental/CLASE.md):**
- El script [composicion_atmosferas.py](composicion_atmosferas.py) calcula la masa molar media de las atmósferas de Marte, Venus y la Tierra y las compara con los pesos moleculares de la NASA; también calcula composiciones porcentuales de H₂O y CO₂ y la fórmula empírica del CO₂.
- ⚠️ **Error frecuente:** Pensar que la fórmula empírica es la molecular. Se corrige con el ejercicio 8.
- 🎯 **Por qué importa:** Si quieres saber cuánto pesa una columna de atmósfera de Marte, necesitas su masa molar media, y para eso, su composición. La NASA publica la composición en volumen de las atmósferas de Marte, Venus y la Tierra y también un «peso molecular» medio (S1, S2, S3).
- 🔗 **Se estudia junto con:** fórmula empírica, composición porcentual, fracción molar, masa molar media.

📘 **Dónde se aprende** (1 clase): [B06-C07 · Estequiometría elemental](../programa/clases/B06/B06-C07-estequiometria-elemental/CLASE.md).

### Fórmula plana

- La fórmula plana `v² sen 2θ/g` supone gravedad uniforme y superficie plana.

💡 **Cómo se explica en la clase [B59-C17](../programa/clases/B59/B59-C17-impacto-ambiental-extraterrestre/CLASE.md):**
- La fórmula plana falla cuando el alcance es comparable al radio: la superficie se curva y la gravedad cambia con la altura.
- *Descripción textual:* la velocidad y el ángulo se integran con gravedad central; el alcance se compara con la fórmula plana; una distribución de velocidades da fracciones.
- ⚠️ **Error frecuente:** Usar la fórmula plana a alcances grandes. Se corrige con 8.2.
- 🎯 **Por qué importa:** Sin atmósfera, la eyecta viaja lejos y sin frenar. La decisión central: ¿a qué distancia de una zona sensible, como una sombra permanente, hay que operar para que la eyecta no la alcance?
- 🔗 **Se estudia junto con:** eyecta, alcance, deriva de energía, protección planetaria.

📘 **Dónde se aprende** (1 clase): [B59-C17 · Impacto ambiental extraterrestre](../programa/clases/B59/B59-C17-impacto-ambiental-extraterrestre/CLASE.md).

### Forsterita

- Un mineral es un sólido cristalino natural de composición química definida: el olivino `(Mg,Fe)₂SiO₄` es una serie entre la forsterita `Mg₂SiO₄` y la fayalita `Fe₂SiO₄`; el piroxeno más sencillo es `MgSiO₃`; la calcita es `CaCO₃`.
- La forsterita (Mg₂SiO₄) y la fayalita (Fe₂SiO₄) son los extremos del olivino; la enstatita (MgSiO₃) es un piroxeno.

💡 **Cómo se explica en la clase [B06-C19](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md):**
- Con los pesos atómicos de la NIST (C03): `H₂O = 18,0153`, `CO₂ = 44,0094`, `NH₃ = 17,0308`, forsterita `Mg₂SiO₄ = 2 × 24,3055 + 28,085 + 4 × 15,9994 = 140,6936`, fayalita `Fe₂SiO₄ = 203,7726`, piroxeno `MgSiO₃ = 100,3887` y calcita `CaCO₃ = 100,0868 g/mol`.
- El magnesio es el 34,55 % de la masa de la forsterita.
- 🎯 **Por qué importa:** Los estudios con el telescopio James Webb muestran que las nubes densas del medio interestelar tienen granos de polvo cubiertos de hielos con una variedad de moléculas, y que esos hielos contienen entre el 2 y el 19 % del carbono, oxígeno, nitrógeno y azufre disponibles (S1, resumen).
- 🔗 **Se estudia junto con:** hielo, mineral, olivino, fayalita.

📘 **Dónde se aprende** (2 clases): [B06-C19 · Química de hielos y minerales](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md); [B55-C12 · Geoquímica de meteoritos](../programa/clases/B55/B55-C12-geoquimica-de-meteoritos/CLASE.md).

### Fotodesorción

- La fotodesorción es la expulsión de moléculas de un hielo por absorción de fotones.

💡 **Cómo se explica en la clase [B68-C02](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md):**
- Definir el rendimiento de fotodesorción en moléculas por fotón.
- La evidencia es la ficha de la fotodesorción del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Si un hielo de CO a 15 K es estable térmicamente durante millones de años, la presencia de CO gaseoso en regiones frías exige otro mecanismo. La decisión central: ¿cuántas moléculas expulsa cada fotón y de qué depende ese número?
- 🔗 **Se estudia junto con:** rendimiento, fluencia, DIET, fotólisis.

📘 **Dónde se aprende** (1 clase): [B68-C02 · Fotodesorción de hielos interestelares](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md).

### Fotoevaporación

- La fotoevaporación es la pérdida de gas calentado por radiación.

💡 **Cómo se explica en la clase [B52-C09](../programa/clases/B52/B52-C09-dispersion-de-discos-de-gas/CLASE.md):**
- Más tarde la fotoevaporación domina y limpia el disco rápidamente.
- E --> P["Mdot frente a fotoevaporación"]
- 🎯 **Por qué importa:** La vida del gas fija cuánto tiempo hay para formar núcleos, gigantes y migración. La decisión central: ¿cuánto tarda un disco en perder su gas y cómo se comprueba un esquema numérico de difusión?
- 🔗 **Se estudia junto con:** viscosidad, escala viscosa, solución de semejanza, Crank–Nicolson.

📘 **Dónde se aprende** (1 clase): [B52-C09 · Dispersión de discos de gas](../programa/clases/B52/B52-C09-dispersion-de-discos-de-gas/CLASE.md).

### Fotólisis

- La fotólisis es la ruptura de moléculas en el volumen del hielo.

💡 **Cómo se explica en la clase [B68-C02](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md):**
- Öberg y colaboradores ajustan el espesor frente a la fluencia con la suma de una función lineal (orden cero, la desorción de superficie) y una exponencial (primer orden, la fotólisis).
- `Y = 2,7 × 10⁻³`) y ruido gaussiano de 0,02 ML con semilla fija, el ajuste recupera `Y = 2,701 × 10⁻³` y `σ = 0,35`, mientras que una recta sola da `3,182 × 10⁻³`, un sesgo de `+17,9 %` porque atribuye a la desorción la pérdida por fotólisis.
- 🎯 **Por qué importa:** Si un hielo de CO a 15 K es estable térmicamente durante millones de años, la presencia de CO gaseoso en regiones frías exige otro mecanismo. La decisión central: ¿cuántas moléculas expulsa cada fotón y de qué depende ese número?
- 🔗 **Se estudia junto con:** fotodesorción, rendimiento, fluencia, DIET.

📘 **Dónde se aprende** (1 clase): [B68-C02 · Fotodesorción de hielos interestelares](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md).

### Fotometría de apertura

- La fotometría de apertura suma el flujo dentro de un círculo.
- La fotometría de apertura suma el flujo dentro de un círculo y resta el cielo de un anillo.

💡 **Cómo se explica en la clase [B29-C02](../programa/clases/B29/B29-C02-curvas-de-luz-fotometricas/CLASE.md):**
- La evidencia es la ficha de fotometría y apertura óptima del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *ficha de fotometría y apertura óptima*: tabla de SNR, óptimo, tres brillos y el Monte Carlo.
- 🎯 **Por qué importa:** Una apertura pequeña pierde estrella; una grande suma cielo y ruido de lectura. La decisión central: ¿qué apertura maximiza la relación señal-ruido y qué error en magnitud implica?
- 🔗 **Se estudia junto con:** ruido de disparo, ruido de lectura, apertura óptima, error en magnitud.

📘 **Dónde se aprende** (2 clases): [B29-C02 · Curvas de luz fotométricas](../programa/clases/B29/B29-C02-curvas-de-luz-fotometricas/CLASE.md); [B44-C20 · Pipeline inicial de calibración de imágenes](../programa/clases/B44/B44-C20-pipeline-inicial-de-calibracion-de-imagenes/CLASE.md).

### Fotón

- Un fotón es el cuanto de la radiación.
- Un fotón es el paquete de luz que se emite o se absorbe en ese salto.
- El fotón es el cuanto de luz de energía `E = hc/λ`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C18](../programa/clases/B05/B05-C18-electromagnetismo-y-radiacion/CLASE.md):**
- Los fotones de rayos X y gamma, y parte del ultravioleta, tienen energía suficiente para ionizar (S2), y por eso pueden dañar tejidos y componentes electrónicos; las bandas de radio, microondas, infrarrojo y visible no ionizan por fotón, aunque una potencia alta puede calentar.
- La misma radiación tiene dos descripciones: como onda (frecuencia, longitud de onda) y como flujo de fotones (energía por fotón).
- 🎯 **Por qué importa:** Un satélite se comunica con ondas de radio, un telescopio observa luz y rayos X, y la misma radiación a otras energías puede dañar electrónica y tejidos. La pregunta motivadora es: ¿qué es la radiación electromagnética, cómo se ordena por frecuencia y energía, cómo decae con la distancia y qué la hace peligrosa?
- 🔗 **Se estudia junto con:** onda electromagnética, magnitudes, intensidad o flujo, fuente isótropa.

📘 **Dónde se aprende** (5 clases): [B05-C18 · Electromagnetismo y radiación](../programa/clases/B05/B05-C18-electromagnetismo-y-radiacion/CLASE.md); [B06-C01 · Estructura atómica](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md); [B26-C05 · Equivalencia entre masa y energía](../programa/clases/B26/B26-C05-equivalencia-entre-masa-y-energia/CLASE.md); [B44-C01 · Principios fotoeléctricos](../programa/clases/B44/B44-C01-principios-fotoelectricos/CLASE.md); [B45-C01 · Radiometría y fotometría](../programa/clases/B45/B45-C01-radiometria-y-fotometria/CLASE.md).

### Fotón de señal

- Un fotón de señal viene del láser reflejado; uno de fondo viene del Sol o del ruido del detector.

💡 **Cómo se explica en la clase [B57-C11](../programa/clases/B57/B57-C11-lidar-satelital/CLASE.md):**
- Con 3 fotones de señal por pulso hay `423` fotones de señal por segmento.
- Los fotones de fondo caen como copos por todas partes; los de señal se amontonan en la altura de la superficie.
- 🎯 **Por qué importa:** Un láser mide alturas con precisión de centímetros, pero a la luz del día el fondo solar inunda el detector. La decisión central: ¿cuántos fotones de señal hacen falta para distinguir la superficie del ruido y con qué error?
- 🔗 **Se estudia junto con:** conteo de fotones, fondo, espaciado a lo largo de la traza, segmento.

📘 **Dónde se aprende** (1 clase): [B57-C11 · LiDAR satelital](../programa/clases/B57/B57-C11-lidar-satelital/CLASE.md).

### Fotón detectado

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C03](../programa/clases/B47/B47-C03-telescopios-ultravioleta/CLASE.md):**
- tasa de fotones detectados (2000 pasos) = 107.799573 /s ;
- 🎯 **Por qué importa:** En el ultravioleta cada fotón es valioso: las tasas son bajas y el ruido es de Poisson. La decisión central: ¿cuánto hay que exponer para llegar a una relación señal/ruido de 10?
- 🔗 **Se estudia junto con:** ultravioleta, serie de Lyman, constante de Rydberg, estadística de Poisson.

📘 **Dónde se aprende** (1 clase): [B47-C03 · Telescopios ultravioleta](../programa/clases/B47/B47-C03-telescopios-ultravioleta/CLASE.md).

### Fotones por bit

- Los fotones por bit miden la eficiencia energética.

💡 **Cómo se explica en la clase [B89-C18](../programa/clases/B89/B89-C18-comunicaciones-opticas-espaciales/CLASE.md):**
- 16-PPM lleva 4 bits por símbolo; con ranuras de 1 ns y 16 de guarda (ilustrativo), cada símbolo dura 32 ns: `125,0 Mbit/s`, `3,47e+02` fotones por símbolo y `8,68e+01` por bit.
- Sin fondo el símbolo se pierde si el pulso no produce ningún fotón (probabilidad `e^{−n_s}`) y se adivina entre las `M` ranuras: `P = e^{−n_s}(M−1)/M`.
- 🎯 **Por qué importa:** Las comunicaciones ópticas prometen más tasa por masa y potencia que la radio; entender el presupuesto de fotones y la modulación por posición de pulso explica por qué y a qué costo (apuntamiento, nubes). La decisión central: ¿cuántos fotones por bit llegan y qué error de símbolo implica la modulación PPM elegida?
- 🔗 **Se estudia junto con:** banda C óptica, PPM de orden M, detección de fotones, error de símbolo sin fondo.

📘 **Dónde se aprende** (1 clase): [B89-C18 · Comunicaciones ópticas espaciales](../programa/clases/B89/B89-C18-comunicaciones-opticas-espaciales/CLASE.md).

### Fotones por O₂

- Los fotones por O₂ resumen la eficiencia del cultivo, incluida la absorción incompleta.

💡 **Cómo se explica en la clase [B59-C14](../programa/clases/B59/B59-C14-agricultura-y-sustratos-artificiales/CLASE.md):**
- O2["O₂ por persona"] --> F["× fotones por O₂"]
- *Descripción textual:* el oxígeno requerido da los fotones; la luz por m² da el área; el área da la potencia y el agua.
- ⚠️ **Error frecuente:** Confundir PPFD con iluminancia. El PPFD mide fotones útiles; sección 6.
- 🎯 **Por qué importa:** Cultivar exige luz, y la luz eléctrica cuesta potencia. La decisión central: ¿cuántos metros cuadrados y cuántos kilovatios necesita un cultivo para producir el oxígeno de una persona?
- 🔗 **Se estudia junto con:** PPFD, eficacia, evapotranspiración, sustrato.

📘 **Dónde se aprende** (1 clase): [B59-C14 · Agricultura y sustratos artificiales](../programa/clases/B59/B59-C14-agricultura-y-sustratos-artificiales/CLASE.md).

### Fotoperiodo

- El fotoperiodo son las horas de luz por día.

💡 **Cómo se explica en la clase [B115-C02](../programa/clases/B115/B115-C02-iluminacion-de-cultivos-con-led-y-espectro-de-crecimiento/CLASE.md):**
- M["meta de DLI<br/>mol/m2/d"] --> F["PPFD x fotoperiodo"]
- Calcular la integral diaria de luz (DLI) a partir del flujo de fotones y el fotoperiodo.
- 🎯 **Por qué importa:** La luz es el mayor consumo eléctrico de un cultivo cerrado. La decisión central: ¿cuántos fotones por metro cuadrado y día hacen falta, con qué eficacia se producen y qué potencia y calor suponen para el hábitat?
- 🔗 **Se estudia junto con:** flujo de fotones fotosintéticos (PPFD), integral diaria de luz (DLI), eficacia fotónica, eficiencia de uso de la radiación (RUE).

📘 **Dónde se aprende** (1 clase): [B115-C02 · Iluminación de cultivos con LED y espectro de crecimiento](../programa/clases/B115/B115-C02-iluminacion-de-cultivos-con-led-y-espectro-de-crecimiento/CLASE.md).

### Fotopletismografía (PPG)

- La fotopletismografía (PPG) mide con luz los cambios de volumen de sangre en la piel.

💡 **Contexto en la clase [B116-C01](../programa/clases/B116/B116-C01-sensores-fisiologicos-y-wearables-para-vuelo/CLASE.md):**
- 🎯 **Por qué importa:** Una pulsera que da «72 lpm» no dice «72 ± 0,1». Con movimiento puede dar 120 cuando el pulso real es 70.
- 🔗 **Se estudia junto con:** frecuencia cardiaca, artefacto de movimiento, resolución espectral, Bland–Altman.

📘 **Dónde se aprende** (1 clase): [B116-C01 · Sensores fisiológicos y wearables para vuelo](../programa/clases/B116/B116-C01-sensores-fisiologicos-y-wearables-para-vuelo/CLASE.md).

### Fotoquímica

- La fotoquímica es la que inicia una excitación electrónica inducida por un fotón sin ionizar; la química de radiación estudia los cambios por absorción de radiación capaz de ionizar (definiciones de Arumainayagam y colaboradores).
- La fotoquímica estudia las reacciones provocadas por la absorción de luz.

💡 **Cómo se explica en la clase [B06-C18](../programa/clases/B06/B06-C18-fotoquimica-y-radiacion/CLASE.md):**
- python programa/clases/B06/B06-C18-fotoquimica-y-radiacion/fotones.py
- 🎯 **Por qué importa:** El hidrógeno de una nube o de una atmósfera puede ser ionizado por un fotón de longitud de onda menor que 91,2 nm. Un fotón de Lyman-alfa (121,6 nm) no lo ioniza desde el estado fundamental, pero tiene 22 veces la energía necesaria para evaporar una molécula de agua.
- 🔗 **Se estudia junto con:** energía de un fotón, einstein, umbral, longitud de onda umbral.

📘 **Dónde se aprende** (2 clases): [B06-C18 · Fotoquímica y radiación](../programa/clases/B06/B06-C18-fotoquimica-y-radiacion/CLASE.md); [B68-C03 · Irradiación de hielos por rayos cósmicos y UV: radiólisis y productos](../programa/clases/B68/B68-C03-irradiacion-de-hielos-por-rayos-cosmicos-y-uv-radiolisis-y-productos/CLASE.md).

### Fotosfera

- La fotosfera es la capa de donde sale la mayor parte de la luz, `τ ≈ 2/3`.
- La fotosfera es la capa que emite la luz visible; la cromosfera y la corona están encima.
- La fotosfera es donde `τ = 2/3`.

💡 **Cómo se explica en la clase [B24-C09](../programa/clases/B24/B24-C09-atmosferas-y-opacidades/CLASE.md):**
- La composición de la fotosfera es un asunto de actualidad: se ha revisado a la baja la abundancia de carbono, nitrógeno, oxígeno y neón (S4, resumen), con consecuencias para la opacidad del interior.
- 🎯 **Por qué importa:** Toda temperatura o composición que atribuimos a una estrella se infiere de una capa delgada. Saber de qué profundidad viene la luz, cuánto vale la opacidad y cuánto puede brillar una estrella sin expulsar su atmósfera es lo que permite interpretar espectros (C10) y entender los vientos (C17).
- 🔗 **Se estudia junto con:** opacidad, profundidad óptica, atmósfera gris, oscurecimiento al limbo.

📘 **Dónde se aprende** (3 clases): [B24-C09 · Atmósferas y opacidades](../programa/clases/B24/B24-C09-atmosferas-y-opacidades/CLASE.md); [B30-C02 · Fotosfera, cromosfera y corona](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md); [B37-C04 · Condiciones de frontera centrales y superficiales en modelos estelares](../programa/clases/B37/B37-C04-condiciones-de-frontera-centrales-y-superficiales-en-modelos-estelares/CLASE.md).

### FPP

- La FPP es la probabilidad de falso positivo.

💡 **Cómo se explica en la clase [B29-C07](../programa/clases/B29/B29-C07-metodos-de-validacion-planetaria/CLASE.md):**
- Con un solo observable débil, el FPP mínimo es `0,21`: no se puede validar.
- Definir la probabilidad de falso positivo `FPP = 1 − P(planeta)`.
- ⚠️ **Error frecuente:** Dar por validado un FPP alto. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Hay muchos más candidatos que posibilidades de seguimiento. Validar bien exige probabilidades honestas: ni optimistas ni conservadoras en exceso.
- 🔗 **Se estudia junto con:** validación, escenario, prior, calibración.

📘 **Dónde se aprende** (1 clase): [B29-C07 · Métodos de validación planetaria](../programa/clases/B29/B29-C07-metodos-de-validacion-planetaria/CLASE.md).

### Fracción

- La fracción `f` es la parte del píxel cubierta por lava caliente.
- Una fracción `a/b` expresa `a` partes de un todo dividido en `b` partes iguales;

💡 **Cómo se explica en la clase [B03-C02](../programa/clases/B03/B03-C02-fracciones-y-razones-de-magnitudes/CLASE.md):**
- Esto funciona porque dividir numerador y denominador entre `k` equivale a multiplicar la fracción por `(1/k)/(1/k) = 1`, que no la cambia.
- Esto reaparece cuando sumes tiempos o fracciones de órbita.
- 🎯 **Por qué importa:** Una cifra aislada como «69 911 km» no dice si Júpiter es grande o pequeño. Una razón sí: Júpiter tiene un radio unas 11 veces el terrestre.
- 🔗 **Se estudia junto con:** numerador, denominador, equivalentes, Simplificar.

📘 **Dónde se aprende** (2 clases): [B03-C02 · Fracciones y razones de magnitudes](../programa/clases/B03/B03-C02-fracciones-y-razones-de-magnitudes/CLASE.md); [B70-C05 · Actividad volcánica venusina: llanuras, coronas e indicios de actividad reciente](../programa/clases/B70/B70-C05-actividad-volcanica-venusina-llanuras-coronas-e-indicios-de-actividad-reciente/CLASE.md).

### Fracción absorbida

- La fracción absorbida es `1 − T`.

💡 **Cómo se explica en la clase [B54-C12](../programa/clases/B54/B54-C12-interaccion-con-radiacion-solar/CLASE.md):**
- Transmisión y fracción absorbida: `τ = 0,1`, `χ = 0°`: `0,9048` y `0,0952`;
- Interpretar la transmisión y la fracción absorbida.
- 🎯 **Por qué importa:** La radiación solar es la fuente de energía de todo el bloque. La pregunta motivadora: ¿cuánta energía llega a un punto y cuánta alcanza el suelo?
- 🔗 **Se estudia junto con:** irradiancia solar, insolación diaria media, transmisión, masa de aire.

📘 **Dónde se aprende** (1 clase): [B54-C12 · Interacción con radiación solar](../programa/clases/B54/B54-C12-interaccion-con-radiacion-solar/CLASE.md).

### Fracción comestible

- Eficiencia de uso de la luz: g de biomasa por mol de fotones. Fracción comestible: parte aprovechada.

💡 **Contexto en la clase [B106-C12](../programa/clases/B106/B106-C12-agricultura-en-ambiente-controlado/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR L["electricidad"] --> F["fotones PPFD x horas"] F --> B["biomasa seca"] C["CO2"] --> B B --> O["O2"] B --> K["kcal comestibles"] ``` *Descripción textual:* la electricidad se convierte en fotones; con CO₂ y agua dan biomasa, O₂ y calorías comestibles. Analogía: una fábrica de calorías cuyo combustible es la luz.
- 🎯 **Por qué importa:** Cultivar reduce la masa de alimento a lanzar y devuelve oxígeno, pero cuesta mucha área y electricidad. La decisión central: ¿qué fracción de la dieta compensa cultivar dado el costo en área y energía?
- 🔗 **Se estudia junto con:** PPFD, DLI, Eficacia de la lámpara, Eficiencia de uso de la luz.

📘 **Dónde se aprende** (1 clase): [B106-C12 · Agricultura en ambiente controlado](../programa/clases/B106/B106-C12-agricultura-en-ambiente-controlado/CLASE.md).

### Fracción convertida

- La fracción convertida es `V_e²/V_max²`.

💡 **Cómo se explica en la clase [B79-C13](../programa/clases/B79/B79-C13-entalpia-de-flujo-y-entalpia-total/CLASE.md):**
- Ejercicio 4 · autónomo. Fracción convertida a `p_e/p₀ = 0,1`.
- pe/p0 Ve [m/s] Ve/Vmax fraccion de h0 convertida
- 🎯 **Por qué importa:** El concepto de energía de flujo es la base del análisis de motores; ninguna clase del tronco lo trata. Con `h₀` se obtiene el límite de velocidad de escape y se entiende por qué la temperatura total no cambia en un choque.
- 🔗 **Se estudia junto con:** entalpía, entalpía total, velocidad máxima.

📘 **Dónde se aprende** (1 clase): [B79-C13 · Entalpía de flujo y entalpía total](../programa/clases/B79/B79-C13-entalpia-de-flujo-y-entalpia-total/CLASE.md).

### Fracción de área

- La fracción de área `p` es la parte del terreno ocupada por una litología.

💡 **Cómo se explica en la clase [B63-C02](../programa/clases/B63/B63-C02-muestreo-superficial-y-estrategias-de-recoleccion/CLASE.md):**
- *Descripción textual:* las fracciones de área determinan la probabilidad de captura, de ella salen el número mínimo de muestras y las litologías esperadas, y con la masa del testigo se arma el plan.
- Un terreno sintético tiene cuatro litologías con fracciones de área: basalto `0,55`, brecha `0,25`, evaporita `0,15` y veta `0,05`.
- ⚠️ **Error frecuente:** Tomar la fracción de área como fracción de masa. Son cosas distintas.
- 🎯 **Por qué importa:** Un rover tiene un número limitado de tubos. La decisión central: ¿cuántas muestras hacen falta para no perderse una litología rara con una confianza dada?
- 🔗 **Se estudia junto con:** testigo, litología, confianza, tubo testigo.

📘 **Dónde se aprende** (1 clase): [B63-C02 · Muestreo superficial y estrategias de recolección](../programa/clases/B63/B63-C02-muestreo-superficial-y-estrategias-de-recoleccion/CLASE.md).

### Fracción de carga útil

- La fracción de carga útil de una etapa es `(1/r − e)/(1 − e)`.

💡 **Cómo se explica en la clase [B124-C23](../programa/clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md):**
- `e` 0,07 y 0,09) la fracción de carga útil es `0,02413`: de cada 100 kg en la plataforma, menos de `2,4` llegan como carga.
- Calcular la fracción de carga útil con un coeficiente estructural.
- 🎯 **Por qué importa:** El costo por kilogramo a superficie no se puede leer en una lista de precios: depende de una cadena de fracciones de masa que se multiplican. La decisión central: ¿cuánto cuesta llevar un kilogramo a la superficie, de qué depende ese costo y qué lo hace más sensible?
- 🔗 **Se estudia junto con:** ecuación del cohete, razón de masas, coeficiente estructural, reparto óptimo.

📘 **Dónde se aprende** (1 clase): [B124-C23 · Costos de transporte por kilogramo a superficie](../programa/clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md).

### Fracción de Carnot

- La fracción de Carnot `f` mide la calidad del ciclo.
- La fracción de Carnot `η` relaciona la potencia real con la ideal: `P = Q/(η COP)`.

💡 **Cómo se explica en la clase [B85-C17](../programa/clases/B85/B85-C17-criogenia-de-instrumentos/CLASE.md):**
- Límite: las propiedades varían con `T` de forma más compleja y la fracción de Carnot real cae con la temperatura.
- Descripción larga: la MLI reduce la carga unas 300 veces; a 80 K cada vatio parásito cuesta 27 W eléctricos con esta fracción de Carnot.
- 🎯 **Por qué importa:** Cada vatio parásito a `80 K` cuesta decenas de vatios eléctricos. La decisión central: ¿qué carga parásita llega a la punta fría, cuánta potencia eléctrica cuesta quitarla y cuánto tarda el enfriamiento?
- 🔗 **Se estudia junto con:** carga parásita, conductividad integral, capacidad térmica.

📘 **Dónde se aprende** (2 clases): [B85-C17 · Criogenia de instrumentos](../programa/clases/B85/B85-C17-criogenia-de-instrumentos/CLASE.md); [B86-C17 · Energía nuclear espacial conceptual](../programa/clases/B86/B86-C17-energia-nuclear-espacial-conceptual/CLASE.md).

### Fracción de cielo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B40-C12](../programa/clases/B40/B40-C12-analisis-de-mapas-del-cmb-pixelizacion-esferica-y-mascaras/CLASE.md):**
- El error de la fracción de cielo baja unas 8 veces al cuadruplicar `N_side`: el borde de la máscara cae en la discretización por anillos.
- La ida y vuelta es exacta para `N_side = 1…16`, `χ²/gl = 0,958` con 153 600 puntos y la fracción de cielo de un corte de 20° da `0,65755` frente a `0,65798` analítico.
- ⚠️ **Error frecuente:** Contar fracción de cielo con pocos pixeles. Se corrige con 8.3.
- 🎯 **Por qué importa:** Sin una pixelización de área igual, el ruido y las estadísticas dependen de la posición. La decisión central: ¿cuántos pixeles, de qué tamaño, y cómo se cuenta la fracción de cielo de una máscara?
- 🔗 **Se estudia junto con:** orden anillo, casquete polar, máscara.

📘 **Dónde se aprende** (1 clase): [B40-C12 · Análisis de mapas del CMB: pixelización esférica y máscaras](../programa/clases/B40/B40-C12-analisis-de-mapas-del-cmb-pixelizacion-esferica-y-mascaras/CLASE.md).

### Fracción de colimación

- La fracción de colimación `f_b = 1 − cos θ_j`.

💡 **Contexto en la clase [B27-C17](../programa/clases/B27/B27-C17-explosiones-de-rayos-gamma/CLASE.md):**
- **Idea central (modelo mental):** La capa casi alcanza a su propia luz: un foton emitido en `R` llega unos `R/(2Γ²c)` después que uno emitido en el centro. Para `Γ` grande, un radio enorme produce un retardo de segundos.
- 🎯 **Por qué importa:** Una explosión que parece de energía enorme puede ser de energía moderada vista de frente, y un retardo de segundos entre dos mensajeros, tras viajar 130 millones de años, es una medición extraordinariamente precisa. La decisión central: ¿qué retardo y qué energía real implican un factor de Lorentz y un ángulo dados?
- 🔗 **Se estudia junto con:** destello de rayos gamma, factor de Lorentz, retardo de llegada, energía isótropa.

📘 **Dónde se aprende** (1 clase): [B27-C17 · Explosiones de rayos gamma](../programa/clases/B27/B27-C17-explosiones-de-rayos-gamma/CLASE.md).

### Fracción de contaminante

- La fracción de contaminante `f` es la parte de la medida que no es de la muestra.

💡 **Cómo se explica en la clase [B63-C03](../programa/clases/B63/B63-C03-curaduria-y-cadena-de-custodia-de-muestras/CLASE.md):**
- Si el contaminante tiene concentración `c_b` (el blanco), la muestra `c_m` y la medida es `c`, la fracción de contaminante es `f = (c − c_m)/(c_b − c_m)`.
- Calcular la fracción de contaminante de una mezcla con un blanco y corregir la medida.
- 🎯 **Por qué importa:** Una muestra planetaria es irrepetible y se estudia durante décadas. La decisión central: ¿cómo demuestras, años después, qué le pasó a una muestra y cuánto de lo que mides es suyo?
- 🔗 **Se estudia junto con:** curaduría, cadena de custodia, hash, encadenamiento.

📘 **Dónde se aprende** (1 clase): [B63-C03 · Curaduría y cadena de custodia de muestras](../programa/clases/B63/B63-C03-curaduria-y-cadena-de-custodia-de-muestras/CLASE.md).
