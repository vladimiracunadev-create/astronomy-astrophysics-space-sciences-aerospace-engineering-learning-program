# Términos · F (parte 1 de 2)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · **F** · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: **1** · [2](terminos-f-2.md)

### F, d, C

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C14):** El color y el astigmatismo degradan el campo de refractores y espejos. La decisión central: ¿cuánto se separan los focos por color y por plano?

📘 **Dónde se aprende** (1 clase): [B41-C14 · Aberración cromática y astigmatismo](../programa/clases/B41/B41-C14-aberracion-cromatica-y-astigmatismo/CLASE.md).

### F1

- La exactitud es `(TP + TN)/total`; la precisión, `TP/(TP + FP)`; la exhaustividad (*recall*), `TP/(TP + FN)`; el F1, la media armónica de las dos últimas.

🎯 **Por qué importa (clase B25-C20):** Clasificar galaxias a gran escala exige algo más que una regla que parezca razonable: hay que decir qué debe cumplir, probarlo contra casos de respuesta conocida y evaluar con honestidad cómo se comporta donde los datos son malos.

📘 **Dónde se aprende** (1 clase): [B25-C20 · Proyecto de clasificación galáctica](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md).

### Factible

- Es factible si cada objetivo empieza en `t ≥ a`, termina en `t + d ≤ b`, no se solapa con otro y `Σe ≤ E`.

💡 **Cómo se explica en la clase [B98-C01](../programa/clases/B98/B98-C01-planificacion-por-objetivos-a-bordo/CLASE.md):**
- Dado un conjunto y un orden, se avanza el reloj: `inicio = max(t, a)`, `fin = inicio + d`; si `fin > b` el orden no es factible.
- 🎯 **Por qué importa:** Si el vehículo solo ejecuta una secuencia fija de comandos, un fallo a mitad de jornada deja sin sentido el resto del plan y hay que esperar la respuesta de Tierra. La decisión central: ¿qué objetivos conviene ejecutar con la energía y el tiempo disponibles, y qué hace el vehículo cuando la energía disponible baja de golpe?

📘 **Dónde se aprende** (1 clase): [B98-C01 · Planificación por objetivos a bordo](../programa/clases/B98/B98-C01-planificacion-por-objetivos-a-bordo/CLASE.md).

### Factor

- El factor de Cholesky es una «raíz cuadrada» de la matriz.
- El factor `Q_max Z/F → 4,37`.

💡 **Cómo se explica en la clase [B10-C10](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md):**
- Descripción larga: `U` guarda el resultado de la eliminación y `L` guarda los multiplicadores usados; el factor de Cholesky tiene el patrón triangular con una diagonal positiva.
- 🎯 **Por qué importa:** Un filtro de navegación resuelve el mismo sistema con miles de lados derechos distintos; una simulación necesita muestras aleatorias con una covarianza dada; un ajuste de mínimos cuadrados quiere estabilidad. En cada caso el trabajo se hace una vez al factorizar y luego se reutiliza.

📘 **Dónde se aprende** (2 clases): [B10-C10 · Descomposiciones matriciales](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md); [B43-C25 · Rodamientos y apoyos de precisión en telescopios](../programa/clases/B43/B43-C25-rodamientos-y-apoyos-de-precision-en-telescopios/CLASE.md).

### Factor 1,42

- El factor 1,42 relaciona la masa total (con helio y elementos pesados) con la de H: `ρ = 1,42 m_p n`.

🎯 **Por qué importa (clase B25-C03):** Las estrellas nacen del gas y devuelven gas enriquecido; el medio interestelar (MIS) es el almacén y el escenario de ese ciclo. Pero «gas» sirve de poco: un volumen del MIS puede estar a `10 K` o a `10⁶ K`, y su densidad variar un factor 10⁷ de un punto a otro.

📘 **Dónde se aprende** (1 clase): [B25-C03 · Medio interestelar multifásico](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md).

### Factor 5 cos² i − 1

- El factor `5 cos² i − 1` fija el signo de la tasa.

🎯 **Por qué importa (clase B72-C05):** Si el perigeo de una órbita muy excéntrica girara, el satélite dejaría de pasar por la región que interesa. La decisión central: ¿a qué inclinación el perigeo deja de moverse y cuánto se mueve en otras?

📘 **Dónde se aprende** (1 clase): [B72-C05 · Precesión del argumento del periapsis](../programa/clases/B72/B72-C05-precesion-del-argumento-del-periapsis/CLASE.md).

### Factor anamórfico

- El factor anamórfico `cos α / cos β` cambia el ancho del haz.

💡 **Cómo se explica en la clase [B45-C06](../programa/clases/B45/B45-C06-diseno-de-espectrografos/CLASE.md):**
- ⚠️ **Error frecuente:** Olvidar el factor anamórfico. Se corrige con la sección 9.
- 🎯 **Por qué importa:** El diseño se decide con unos pocos parámetros que se compensan entre sí. La decisión central: ¿qué ancho de rendija da la resolución deseada y cuántos píxeles muestrean cada elemento?

📘 **Dónde se aprende** (1 clase): [B45-C06 · Diseño de espectrógrafos](../programa/clases/B45/B45-C06-diseno-de-espectrografos/CLASE.md).

### Factor beta

- El factor beta mide cuánto aumenta el momento transferido por la eyección de material; la fuente [S4] no da un valor numérico.
- El factor beta es la fracción de fallo de causa común.

💡 **Cómo se explica en la clase [B58-C17](../programa/clases/B58/B58-C17-principios-de-mitigacion-y-desviacion/CLASE.md):**
- No se calcula aquí la nave ni el factor beta.
- 🎯 **Por qué importa:** Lo que importa no es el tamaño del empuje sino cuándo se da: el desplazamiento crece con el tiempo de aviso. La decisión central: ¿qué `Δv` y cuántos años de aviso se necesitan para mover un objeto lo suficiente?

📘 **Dónde se aprende** (2 clases): [B58-C17 · Principios de mitigación y desviación](../programa/clases/B58/B58-C17-principios-de-mitigacion-y-desviacion/CLASE.md); [B63-C04 · Misiones de retorno de muestras: salvaguardas históricas y regulatorias](../programa/clases/B63/B63-C04-misiones-de-retorno-de-muestras-salvaguardas-historicas-y-regulatorias/CLASE.md).

### Factor de aceleración (AF)

- Presión límite: `Q_gas/S`. Factor de aceleración (AF): ciclos de servicio por ciclo de ensayo.

💡 **Cómo se explica en la clase [B90-C12](../programa/clases/B90/B90-C12-vacio-termico-y-ciclos/CLASE.md):**
- El coeficiente 1,9, el exponente 1/3 y el 1 414 K del factor de aceleración son valores de la literatura que no se consultaron.
- *Descripción textual:* la órbita aporta amplitud y número de ciclos de servicio; el ensayo, su amplitud, frecuencia y temperatura máxima; el factor de aceleración reduce los ciclos a 485, que ocupan 42,7 días de cámara.
- 🎯 **Por qué importa:** Una nave en órbita baja sufre unos 16 ciclos térmicos por día; no se pueden repetir 5 840 ciclos en tierra. La decisión central: ¿cuántos ciclos de ensayo con mayor amplitud representan un año de órbita y cuánto tarda la campaña?

📘 **Dónde se aprende** (1 clase): [B90-C12 · Vacío térmico y ciclos](../programa/clases/B90/B90-C12-vacio-termico-y-ciclos/CLASE.md).

### Factor de acumulación

- El factor de acumulación es `R = 1/(1 − e^{−kτ})`.

🎯 **Por qué importa (clase B105-C13):** Con un fármaco real, el efecto depende de su concentración en el tiempo. Un cambio de volumen modifica la concentración inicial; uno de aclaramiento, la exposición total.

📘 **Dónde se aprende** (1 clase): [B105-C13 · Farmacología y microgravedad](../programa/clases/B105/B105-C13-farmacologia-y-microgravedad/CLASE.md).

### Factor de amplificación

- `R` es el factor de amplificación.

🎯 **Por qué importa (clase B11-C09):** Un modelo térmico de una nave tiene constantes de tiempo que van de segundos (un sensor fino) a horas (un tanque grande). Un método explícito debe usar un paso comparable al más rápido aunque lo único que interese sea lo lento: pagar por una escala que no se observa.

📘 **Dónde se aprende** (1 clase): [B11-C09 · Análisis de estabilidad numérica](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md).

### Factor de arreglo

- El factor de arreglo es la suma de las contribuciones de los elementos.
- El factor de arreglo `AF(θ) = Σₙ e^{jnψ}` con `ψ = k d (sin θ − sin θ₀)` describe la suma de los `N` elementos con una fase progresiva que dirige el haz a `θ₀`.

💡 **Cómo se explica en la clase [B49-C04](../programa/clases/B49/B49-C04-arreglos-de-antenas-factor-de-arreglo-y-formacion-de-haz/CLASE.md):**
- *Descripción textual:* los pesos y la geometría fijan el factor de arreglo; los nulos, lóbulos y la dirección salen de él.
- 🎯 **Por qué importa:** El arreglo cambia ancho de haz, lóbulos laterales y ganancia según los pesos. La decisión central: ¿qué pesos y qué separación dan el haz y el nivel de lóbulos que se necesitan?

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

📘 **Dónde se aprende** (5 clases): [B12-C22 · Comparación de modelos: evidencia bayesiana y criterios de información](../programa/clases/B12/B12-C22-comparacion-de-modelos-evidencia-bayesiana-y-criterios-de-informacion/CLASE.md); [B19-C07 · Comparación de modelos bayesianos](../programa/clases/B19/B19-C07-comparacion-de-modelos-bayesianos/CLASE.md); [B31-C20 · Evaluación crítica de afirmaciones extraordinarias](../programa/clases/B31/B31-C20-evaluacion-critica-de-afirmaciones-extraordinarias/CLASE.md); [B55-C19 · Interpretación de firmas químicas](../programa/clases/B55/B55-C19-interpretacion-de-firmas-quimicas/CLASE.md); [B132-C05 · Contexto ritual y social de la observación del cielo](../programa/clases/B132/B132-C05-contexto-ritual-y-social-de-la-observacion-del-cielo/CLASE.md).

### Factor de calidad

- El factor de calidad `Q` mide la disipación (cuanto menor, más disipa).
- El factor de calidad `Q(L)` es una función del LET usada en magnitudes operacionales.
- El factor de calidad `Q ≈ 1/(2ζ)`.

💡 **Cómo se explica en la clase [B112-C02](../programa/clases/B112/B112-C02-dosis-equivalente-y-dosis-efectiva/CLASE.md):**
- Además NASA calcula su dosis efectiva con su propio factor de calidad y parámetros de una mujer de 35 años (OCHMO-TB-020, consultado), no con la tabla de ICRP.
- ⚠️ **Error frecuente:** Aplicar los `w_R` de ICRP a un límite que usa otro factor de calidad. Lee la definición de la norma (ejercicio 9).
- 🎯 **Por qué importa:** Ninguna clase trata factores de ponderación y dosis equivalente, y sin ellos un límite en mSv de una norma no se puede leer. La decisión central: ¿cómo se resume en un solo número en sievert una exposición mezclada de varias radiaciones y órganos, y qué no dice ese número?

📘 **Dónde se aprende** (3 clases): [B47-C11 · Aislamiento vibracional](../programa/clases/B47/B47-C11-aislamiento-vibracional/CLASE.md); [B65-C06 · Calentamiento por marea y equilibrio térmico en satélites](../programa/clases/B65/B65-C06-calentamiento-por-marea-y-equilibrio-termico-en-satelites/CLASE.md); [B112-C02 · Dosis equivalente y dosis efectiva](../programa/clases/B112/B112-C02-dosis-equivalente-y-dosis-efectiva/CLASE.md).

### Factor de calidad sin carga

- El factor de calidad sin carga `Q_u` mide las pérdidas del resonador.

🎯 **Por qué importa (clase B49-C10):** Más orden rechaza más, pero también pierde más señal. La decisión central: ¿qué orden y qué ancho de banda dan el rechazo de imagen necesario con una pérdida aceptable?

📘 **Dónde se aprende** (1 clase): [B49-C10 · Filtros de radiofrecuencia pasabanda y rechazo de banda imagen](../programa/clases/B49/B49-C10-filtros-de-radiofrecuencia-pasabanda-y-rechazo-de-banda-imagen/CLASE.md).

### Factor de carga

- El factor de carga `C = k_b/(k_b + k_m)` es la fracción de la carga externa que toma el tornillo.

💡 **Cómo se explica en la clase [B84-C17](../programa/clases/B84/B84-C17-soldadura-y-uniones/CLASE.md):**
- El factor de carga es `C = 0,2902`; con una tracción de `3000 N`, `MS_rotura = 0,248`, `MS_separación = 0,677` y, con cortante de `1500 N`, `MS_deslizamiento = −0,727`: la unión desliza y hacen falta pasadores.
- 🎯 **Por qué importa:** Un tornillo que se separa o desliza falla sin romper: la precarga es lo que mantiene la unión, y su dispersión por el par de apriete es grande. La decisión central: ¿qué precarga mantiene la unión cerrada sin romper el tornillo, y cuándo deslizan las placas?

📘 **Dónde se aprende** (1 clase): [B84-C17 · Soldadura y uniones](../programa/clases/B84/B84-C17-soldadura-y-uniones/CLASE.md).

### Factor de carga φ

- Coeficiente de par `K`: relaciona par y precarga e incluye la fricción. Factor de carga `φ`: fracción de una carga externa que absorbe el perno.

🎯 **Por qué importa (clase B90-C06):** Un perno mal apretado se afloja con la vibración o se rompe por exceso de carga; un centro de masa fuera de rango desvía la nave en el despliegue. La decisión central: ¿qué par de apriete garantiza que la unión no se separe ni se plastifique, y el conjunto queda dentro de los límites de masa?

📘 **Dónde se aprende** (1 clase): [B90-C06 · Integración mecánica de subsistemas](../programa/clases/B90/B90-C06-integracion-mecanica-de-subsistemas/CLASE.md).

### Factor de cobertura k

- El factor de cobertura `k` es el multiplicador de `u_c` que da `U`; suele estar entre 2 y 3 (S1, 2.3.6).

🎯 **Por qué importa (clase B13-C12):** Un telémetro da `1000,004 m` con una incertidumbre típica de `0,017 m`. ¿Cuál es el intervalo dentro del cual el valor verdadero cae «casi seguro»?

📘 **Dónde se aprende** (1 clase): [B13-C12 · Incertidumbre expandida](../programa/clases/B13/B13-C12-incertidumbre-expandida/CLASE.md).

### Factor de compresibilidad

- El factor de compresibilidad `Z = PV/(nRT)` mide la desviación: `Z = 1` es ideal.
- El factor de compresibilidad `Z` mide la desviación de un gas real del ideal (no se calcula aquí).

🎯 **Por qué importa (clase B06-C09):** La NASA publica para Marte, Venus y la Tierra la presión y la temperatura medias en la superficie, la gravedad, el peso molecular de la atmósfera y su densidad (S1, S2, S3). ¿Puedes reproducir esa densidad con sólo lo anterior?

📘 **Dónde se aprende** (2 clases): [B06-C09 · Gases ideales y no ideales](../programa/clases/B06/B06-C09-gases-ideales-y-no-ideales/CLASE.md); [B54-C04 · Presión y densidad](../programa/clases/B54/B54-C04-presion-y-densidad/CLASE.md).

### Factor de conversión

- Un factor de conversión es una razón igual a 1 (por ejemplo, `1 au/149 597 870 700 m`).
- Un factor de conversión es una razón de dos cantidades equivalentes, como `1 km / 1000 m`; vale 1 porque numerador y denominador son la misma cantidad.
- El factor de conversión `X_CO` pasa de `W_CO` a densidad de columna de `H₂`: `N(H₂) = X_CO W_CO`.

💡 **Cómo se explica en la clase [B01-C08](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md):**
- Para pasar de un peldaño a otro multiplicas por un factor de conversión que vale 1.
- Entre cada par se indica el factor de conversión; todos valen 1 porque numerador y denominador son la misma longitud.
- 🎯 **Por qué importa:** En 1999 se perdió la sonda Mars Climate Orbiter por una discrepancia entre unidades inglesas y métricas (C04, fuente NASA). La ciencia estaba bien; la conversión, no.

📘 **Dónde se aprende** (3 clases): [B01-C08 · Mediciones y unidades astronómicas](../programa/clases/B01/B01-C08-mediciones-y-unidades-astronomicas/CLASE.md); [B03-C07 · Conversión de distancia y velocidad](../programa/clases/B03/B03-C07-conversion-de-distancia-y-velocidad/CLASE.md); [B25-C04 · Nubes moleculares y polvo](../programa/clases/B25/B25-C04-nubes-moleculares-y-polvo/CLASE.md).

### Factor de crecimiento

- El factor de crecimiento `D(a)` normalizado a `D = a` en la era de la materia.
- El factor de crecimiento `g = D/a`.

💡 **Cómo se explica en la clase [B40-C09](../programa/clases/B40/B40-C09-efecto-sachs-wolfe-y-efecto-sachs-wolfe-integrado/CLASE.md):**
- Con `A_s = 2,1 × 10⁻⁹` (ilustrativa) y `T₀ = 2,7255 K`, la meseta es `623,98 μK²`; con `Ω_m = 0,315` el factor de crecimiento hoy es `0,7878`.
- 🎯 **Por qué importa:** SW domina las escalas grandes; el ISW es una señal de la energía oscura. La decisión central: ¿qué amplitud tiene la meseta y cuánto decaen los potenciales?

📘 **Dónde se aprende** (2 clases): [B36-C01 · Crecimiento lineal de perturbaciones de densidad](../programa/clases/B36/B36-C01-crecimiento-lineal-de-perturbaciones-de-densidad/CLASE.md); [B40-C09 · Efecto Sachs-Wolfe y efecto Sachs-Wolfe integrado](../programa/clases/B40/B40-C09-efecto-sachs-wolfe-y-efecto-sachs-wolfe-integrado/CLASE.md).

### Factor de crecimiento de masa

- El factor de crecimiento de masa es la masa en órbita dividida entre la masa en superficie.

🎯 **Por qué importa (clase B100-C02):** La masa que llega a la superficie es una fracción pequeña de la que sale de la Tierra, y el volumen puede decidir antes que la masa. La decisión central: ¿cuánta masa y cuánto volumen hay que cargar para N personas durante D días, y cuánta masa hay que lanzar para que esa carga llegue?

📘 **Dónde se aprende** (1 clase): [B100-C02 · Dimensionamiento de carga y volumen de misión](../programa/clases/B100/B100-C02-dimensionamiento-de-carga-y-volumen-de-mision/CLASE.md).

### Factor de derating

- El derating es operar un componente por debajo de su valor nominal; el factor de derating es la fracción del nominal que se permite (`0,6` = hasta el 60 %).

💡 **Cómo se explica en la clase [B93-C02](../programa/clases/B93/B93-C02-seleccion-de-componentes-y-derating/CLASE.md):**
- N["valor nominal"] --> F["x factor de derating"]
- 🎯 **Por qué importa:** Nadie en el tronco trataba la selección de componentes calificados ni el derating. La decisión central: ¿cumple cada pieza de la lista con los factores de derating, con qué margen, y qué se cambia cuando no cumple?

📘 **Dónde se aprende** (1 clase): [B93-C02 · Selección de componentes y derating](../programa/clases/B93/B93-C02-seleccion-de-componentes-y-derating/CLASE.md).

### Factor de descuento

- El factor de descuento `δ` mide la paciencia.

🎯 **Por qué importa (clase B119-C27):** C20 simula la respuesta institucional interna; la diplomacia entre Estados no está cubierta. Esta clase aporta el razonamiento básico de negociación sin pretender describir ninguna práctica.

📘 **Dónde se aprende** (1 clase): [B119-C27 · Diplomacia y comunicación entre Estados ante incidentes espaciales](../programa/clases/B119/B119-C27-diplomacia-y-comunicacion-entre-estados-ante-incidentes-espaciales/CLASE.md).

### Factor de Eddington

- El factor de Eddington `Γ = L/L_Edd` es la fracción del límite que emite la estrella (C09).

💡 **Cómo se explica en la clase [B24-C17](../programa/clases/B24/B24-C17-estrellas-masivas-y-perdida-de-masa/CLASE.md):**
- *Descripción textual:* de la masa y la luminosidad se obtiene el factor de Eddington; cuanto más cercano a 1, más fácil es expulsar gas; la masa disminuye con el tiempo y fija el destino final.
- 🎯 **Por qué importa:** La masa que una estrella conserva hasta su final decide el destino: remanente, tipo de supernova, enriquecimiento del medio. Y las estrellas masivas no la conservan: pierden masa por vientos, erupciones y transferencia a una compañera.

📘 **Dónde se aprende** (1 clase): [B24-C17 · Estrellas masivas y pérdida de masa](../programa/clases/B24/B24-C17-estrellas-masivas-y-perdida-de-masa/CLASE.md).

### Factor de efectividad

- El factor de efectividad `η` es la fracción del consumo ideal que se logra de hecho.

💡 **Cómo se explica en la clase [B64-C06](../programa/clases/B64/B64-C06-biofilms-en-ambientes-extremos/CLASE.md):**
- El factor de efectividad es `η = tanh(φ)/φ` y la longitud de penetración, `1/√(k/D_e)`.
- El factor de efectividad calculado con el flujo en la superficie coincide con `tanh(φ)/φ` a 1 %.
- 🎯 **Por qué importa:** Una película de células y matriz crea su propio microambiente. La pregunta motivadora: ¿hasta qué profundidad llega un nutriente en un biofilm y qué sucede con las células que quedan más adentro?

📘 **Dónde se aprende** (1 clase): [B64-C06 · Biofilms en ambientes extremos](../programa/clases/B64/B64-C06-biofilms-en-ambientes-extremos/CLASE.md).

### Factor de eficiencia

- Sistema socio-técnico: conjunto de personas, procedimientos y equipos interdependientes. Factor de eficiencia: probabilidad de que un subsistema esté disponible.

🎯 **Por qué importa (clase B48-C01):** Sin una visión de sistema, cada equipo optimiza su parte y nadie sabe qué mejora rinde más. La decisión central: ¿en qué factor conviene invertir para recuperar más noches útiles?

📘 **Dónde se aprende** (1 clase): [B48-C01 · Observatorio como sistema socio-técnico](../programa/clases/B48/B48-C01-observatorio-como-sistema-socio-tecnico/CLASE.md).

### Factor de embalaje

- El factor de embalaje multiplica la masa por el envase y los soportes.

🎯 **Por qué importa (clase B100-C02):** La masa que llega a la superficie es una fracción pequeña de la que sale de la Tierra, y el volumen puede decidir antes que la masa. La decisión central: ¿cuánta masa y cuánto volumen hay que cargar para N personas durante D días, y cuánta masa hay que lanzar para que esa carga llegue?

📘 **Dónde se aprende** (1 clase): [B100-C02 · Dimensionamiento de carga y volumen de misión](../programa/clases/B100/B100-C02-dimensionamiento-de-carga-y-volumen-de-mision/CLASE.md).

### Factor de empaque

- El factor de empaque (1,3, ilustrativo) convierte masa de alimento en masa transportada.

🎯 **Por qué importa (clase B105-C12):** Cada kilogramo de alimento que se lanza cuesta; cada kilocaloría que falta se paga con masa corporal. La decisión central: ¿cuánto alimento hay que transportar para una misión y con qué margen frente a la incertidumbre del gasto?

📘 **Dónde se aprende** (1 clase): [B105-C12 · Nutrición espacial](../programa/clases/B105/B105-C12-nutricion-espacial/CLASE.md).

### Factor de encogimiento

- El factor de encogimiento `B_j = σ_j²/(σ_j² + τ²)` es la fracción por la que el sensor `j` se acerca al grupo.

🎯 **Por qué importa (clase B19-C02):** Seis sensores de temperatura de un satélite miden cada uno un desvío de calibración. Tres decisiones ingenuas son posibles: tratar a cada sensor por separado, ignorar las diferencias y promediar todo, o confiar en el sensor más preciso.

📘 **Dónde se aprende** (1 clase): [B19-C02 · Modelos jerárquicos](../programa/clases/B19/B19-C02-modelos-jerarquicos/CLASE.md).

### Factor de ensayos

- El factor de ensayos (*trials factor*) es el número de frecuencias independientes exploradas.

💡 **Cómo se explica en la clase [B15-C06](../programa/clases/B15/B15-C06-analisis-espectral-de-senales/CLASE.md):**
- Si ignoras el factor de ensayos y usas el `z` de un solo bin (`z = 4,6` para 1 %), obtienes unos `M × 1 % ≈ 10` picos falsos.
- ⚠️ **Error frecuente:** Olvidar el factor de ensayos. Se corrige con el ejercicio 8.
- 🎯 **Por qué importa:** Alguien afirma: «hay un periodo de 3,7 días en esta estrella». ¿Cómo se sostiene?

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

📘 **Dónde se aprende** (5 clases): [B03-C20 · Problema integrado de escala del sistema solar](../programa/clases/B03/B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md); [B04-C17 · Proyecciones cartográficas elementales](../programa/clases/B04/B04-C17-proyecciones-cartograficas-elementales/CLASE.md); [B26-C13 · Modelo FLRW — Relatividad y cosmología](../programa/clases/B26/B26-C13-modelo-flrw-relatividad-y-cosmologia/CLASE.md); [B80-C02 · Modelo de error de acelerómetros](../programa/clases/B80/B80-C02-modelo-de-error-de-acelerometros/CLASE.md); [B131-C05 · Demostraciones visuales y modelos para el aula](../programa/clases/B131/B131-C05-demostraciones-visuales-y-modelos-para-el-aula/CLASE.md).

### Factor de escala de volúmenes

- Si `m = n`, `det J` es el factor de escala de volúmenes de la transformación (C04).

🎯 **Por qué importa (clase B10-C19):** Una estación mide la distancia, el azimut y la elevación de un objeto con incertidumbres. Para decir dónde está en coordenadas cartesianas y cuánta incertidumbre tiene esa posición, hay que transformar los números y sus errores.

📘 **Dónde se aprende** (1 clase): [B10-C19 · Jacobianos y linealización](../programa/clases/B10/B10-C19-jacobianos-y-linealizacion/CLASE.md).

### Factor de expansión

- El factor de expansión `f` de las líneas de campo.

🎯 **Por qué importa (clase B33-C10):** Un pronóstico necesita una condición de frontera coronal. La decisión central: ¿cómo cambia la velocidad con la expansión y la distancia al borde?

📘 **Dónde se aprende** (1 clase): [B33-C10 · Modelos de viento solar para pronóstico (Parker y WSA)](../programa/clases/B33/B33-C10-modelos-de-viento-solar-para-pronostico-parker-y-wsa/CLASE.md).

### Factor de fatiga

- La sensibilidad `q = 1/(1 + a_p/r)` da el factor de fatiga `K_f = 1 + q(K_t − 1)`.

🎯 **Por qué importa (clase B84-C29):** Una tensión remota de 100 MPa se triplica a 300 MPa en el borde de un agujero; con `K_f = 2,8` la vida baja de 10¹¹ a 10⁷ ciclos. La decisión central: ¿qué tensión local y qué vida resultan de un agujero en una placa cargada?

📘 **Dónde se aprende** (1 clase): [B84-C29 · Concentraciones de tensión y entallas](../programa/clases/B84/B84-C29-concentraciones-de-tension-y-entallas/CLASE.md).

### Factor de filtro

- Un factor de filtro `fᵢ` es el número entre 0 y 1 que multiplica cada componente de la solución ingenua en la base de la SVD.

💡 **Cómo se explica en la clase [B22-C02](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md):**
- Con `A = Σᵢ σᵢ uᵢ vᵢᵀ` (C01), la solución ingenua es `Σᵢ (uᵢᵀ b / σᵢ) vᵢ`; la de Tikhonov es la misma con cada término multiplicado por un factor de filtro (S2, ec. 5–6):
- Pausa. Con `λ = 0,1`, ¿cuál es el factor de filtro de `σ = 1` y el de `σ = 0,01`?
- 🎯 **Por qué importa:** Si no puedes confiar en `x = A⁻¹ b` y no puedes bajar el ruido a voluntad, necesitas una regla que ignore lo que los datos no pueden decir. Esa regla debe tener una perilla: cuánto ignorar.

📘 **Dónde se aprende** (1 clase): [B22-C02 · Regularización de Tikhonov](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md).

### Factor de fin de vida

- El factor de fin de vida es la potencia final dividida por la inicial.

💡 **Cómo se explica en la clase [B86-C14](../programa/clases/B86/B86-C14-envejecimiento-de-paneles/CLASE.md):**
- *Descripción textual:* el tiempo y los ciclos alimentan cuatro factores que se multiplican en el factor de fin de vida; éste da la potencia a cada año, el margen y el sobredimensionamiento.
- 🎯 **Por qué importa:** Dimensionar un ala con su potencia de inicio de vida deja a la misión sin energía al final. El factor de fin de vida que se usó como `0,85` en la primera clase sale de un cálculo como este.

📘 **Dónde se aprende** (1 clase): [B86-C14 · Envejecimiento de paneles](../programa/clases/B86/B86-C14-envejecimiento-de-paneles/CLASE.md).

### Factor de forma

- El factor de forma `F` es la fracción de la radiación de una superficie que llega a otra.

🎯 **Por qué importa (clase B41-C15):** Un refractor sin color necesita combinar vidrios. La decisión central: ¿cuánto color queda con dos o tres vidrios?

📘 **Dónde se aprende** (2 clases): [B41-C15 · Refractores acromáticos y apocromáticos](../programa/clases/B41/B41-C15-refractores-acromaticos-y-apocromaticos/CLASE.md); [B85-C01 · Balance radiativo de satélite](../programa/clases/B85/B85-C01-balance-radiativo-de-satelite/CLASE.md).

### Factor de Franck-Condon

- El factor de Franck-Condon `FC(v'', v') = |∫ψ''_{v''}ψ'_{v'} dx|²` es la probabilidad relativa de cada banda vibracional.

🎯 **Por qué importa (clase B62-C03):** Las bandas electrónicas aparecen en el ultravioleta y el visible; su forma, una serie de picos, revela cuánto cambia la geometría de la molécula. La decisión central: ¿qué picos de la progresión serán intensos?

📘 **Dónde se aprende** (1 clase): [B62-C03 · Transiciones electrónicas moleculares](../programa/clases/B62/B62-C03-transiciones-electronicas-moleculares/CLASE.md).

### Factor de fricción de Darcy

- El factor de fricción de Darcy `f` da la pérdida de presión de un tubo, `Δp = f (L/D) ½ ρ V²`.

🎯 **Por qué importa (clase B79-C04):** El régimen cambia el arrastre y la transferencia de calor por factores de varios; no distinguirlo lleva a subestimar el calentamiento de una pared o la pérdida de presión de un conducto. El tronco no lo trata.

📘 **Dónde se aprende** (1 clase): [B79-C04 · Regímenes laminar y turbulento](../programa/clases/B79/B79-C04-regimenes-laminar-y-turbulento/CLASE.md).

### Factor de Huang-Rhys

- El factor de Huang-Rhys `S = μωd²/(2ħ)` mide el desplazamiento en unidades de oscilador.

🎯 **Por qué importa (clase B62-C03):** Las bandas electrónicas aparecen en el ultravioleta y el visible; su forma, una serie de picos, revela cuánto cambia la geometría de la molécula. La decisión central: ¿qué picos de la progresión serán intensos?

📘 **Dónde se aprende** (1 clase): [B62-C03 · Transiciones electrónicas moleculares](../programa/clases/B62/B62-C03-transiciones-electronicas-moleculares/CLASE.md).

### Factor de idealidad

- El factor de idealidad `n` ajusta la pendiente exponencial.

🎯 **Por qué importa (clase B86-C02):** La potencia de una celda no es un número fijo: depende de la tensión a la que se la haga trabajar y de su temperatura. Elegir mal el punto de operación o ignorar la temperatura del ala cambia la potencia entregada.

📘 **Dónde se aprende** (1 clase): [B86-C02 · Celdas solares](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md).

### Factor de Landé efectivo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B32-C12):** Medir campos estelares exige saber cuándo el desdoblamiento se resuelve y cuándo basta la polarización. La decisión central: ¿qué campo produce un desdoblamiento comparable al ancho de la línea?

📘 **Dónde se aprende** (2 clases): [B32-C12 · Efecto Zeeman y diagnóstico de campos magnéticos estelares](../programa/clases/B32/B32-C12-efecto-zeeman-y-diagnostico-de-campos-magneticos-estelares/CLASE.md); [B47-C21 · Magnetógrafos y medición de campos solares](../programa/clases/B47/B47-C21-magnetografos-y-medicion-de-campos-solares/CLASE.md).

### Factor de llenado

- El factor de llenado es `FF = P_max/(V_oc I_sc)`.

💡 **Cómo se explica en la clase [B86-C02](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md):**
- El factor de llenado es `0,8179` y la eficiencia `P_max/(G A) = 28,06 %`.
- *Descripción textual:* la luz fija `I_ph`; el diodo y la resistencia en serie dan la curva `I(V)`; de ella salen los extremos, el punto de máxima potencia, el factor de llenado y la eficiencia; la temperatura modifica el diodo.
- 🎯 **Por qué importa:** La potencia de una celda no es un número fijo: depende de la tensión a la que se la haga trabajar y de su temperatura. Elegir mal el punto de operación o ignorar la temperatura del ala cambia la potencia entregada.

📘 **Dónde se aprende** (1 clase): [B86-C02 · Celdas solares](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md).

### Factor de Lorentz

- El factor de Lorentz `Γ` de la capa.

🎯 **Por qué importa (clase B27-C17):** Una explosión que parece de energía enorme puede ser de energía moderada vista de frente, y un retardo de segundos entre dos mensajeros, tras viajar 130 millones de años, es una medición extraordinariamente precisa. La decisión central: ¿qué retardo y qué energía real implican un factor de Lorentz y un ángulo dados?

📘 **Dónde se aprende** (1 clase): [B27-C17 · Explosiones de rayos gamma](../programa/clases/B27/B27-C17-explosiones-de-rayos-gamma/CLASE.md).

### Factor de mentira

- El factor de mentira (definición adoptada aquí) es `LF = efecto en el gráfico / efecto en los datos`, con efecto `(B − A)/A`.

💡 **Cómo se explica en la clase [B130-C01](../programa/clases/B130/B130-C01-infografias-con-fuentes-verificables/CLASE.md):**
- Si el diámetro del círculo es proporcional al dato, el área de la Tierra parece `6,93` veces la de Marte y el factor de mentira vale `3,633`; si el área es proporcional, vale `1,000`.
- 🎯 **Por qué importa:** Comunicar con imágenes exige mantener la fuente y la incertidumbre; la clase de comunicación general no entra en cómo se audita una pieza visual. La decisión central: ¿qué debe llevar cada cifra de una infografía para que otra persona pueda verificarla, y qué diseño la deforma?

📘 **Dónde se aprende** (2 clases): [B130-C01 · Infografías con fuentes verificables](../programa/clases/B130/B130-C01-infografias-con-fuentes-verificables/CLASE.md); [B130-C02 · Visualización de datos para comunicar](../programa/clases/B130/B130-C02-visualizacion-de-datos-para-comunicar/CLASE.md).

### Factor de momento de inercia

- El factor de momento de inercia es `I/(MR²)`.
- El factor de momento de inercia `C/(MR²)` vale `0,4` para una esfera uniforme y menos si la masa se concentra hacia el centro.

💡 **Cómo se explica en la clase [B09-C18](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md):**
- La ficha de la Tierra de la NASA (S2) da la masa `5,9722 × 10²⁴ kg`, el radio medio volumétrico `6371,000 km`, la densidad media `5513 kg/m³` y el factor de momento de inercia polar `I/(MR²) = 0,3308`.
- 🎯 **Por qué importa:** La masa de la Tierra se conoce mucho mejor que la distribución de esa masa en su interior. Un solo número, la densidad media, no basta: el momento de inercia depende de cómo se reparte la masa.

📘 **Dónde se aprende** (3 clases): [B09-C18 · Integrales dobles y triples](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md); [B53-C01 · Interior de planetas rocosos](../programa/clases/B53/B53-C01-interior-de-planetas-rocosos/CLASE.md); [B65-C05 · Inversión geofísica conjunta: validación de modelos interiores](../programa/clases/B65/B65-C05-inversion-geofisica-conjunta-validacion-de-modelos-interiores/CLASE.md).

### Factor de oblicuidad

- El factor de oblicuidad `1/√(1 − (R cos E/(R+h))²)` convierte vertical en oblicuo.

💡 **Cómo se explica en la clase [B89-C21](../programa/clases/B89/B89-C21-efectos-ionosfericos-y-centelleo-en-senales-gnss/CLASE.md):**
- E["elevacion"] --> OBL["factor de oblicuidad"]
- 🎯 **Por qué importa:** La ionosfera es el mayor error de un receptor GNSS de una sola frecuencia y el origen de pérdidas de señal en regiones ecuatoriales y polares; sin entenderla no se puede interpretar un error de posición. La decisión central: ¿cuánto error añade la ionosfera, cómo se elimina y cuándo el centelleo hace perder la señal?

📘 **Dónde se aprende** (1 clase): [B89-C21 · Efectos ionosféricos y centelleo en señales GNSS](../programa/clases/B89/B89-C21-efectos-ionosfericos-y-centelleo-en-senales-gnss/CLASE.md).

### Factor de Occam

- El factor de Occam es la parte del factor de Bayes que penaliza la complejidad: cuanto más se reparte el prior de un modelo en valores que no explican los datos, menor su evidencia.

🎯 **Por qué importa (clase B19-C07):** Miras 10 mediciones de la amplitud de una señal y el promedio es 0,57 con ruido conocido 1. ¿Hay señal (`μ ≠ 0`) o solo ruido (`μ = 0`)?

📘 **Dónde se aprende** (1 clase): [B19-C07 · Comparación de modelos bayesianos](../programa/clases/B19/B19-C07-comparacion-de-modelos-bayesianos/CLASE.md).

### Factor de orientación

- El factor de orientación `g = (1 + cos²ι)/2`.

💡 **Cómo se explica en la clase [B28-C07](../programa/clases/B28/B28-C07-fuentes-compactas-binarias/CLASE.md):**
- *Descripción textual:* la masa fija la frecuencia máxima; el alcance sale de la relación señal-ruido; el volumen y la tasa dan los eventos, reducidos por el factor de orientación.
- 🎯 **Por qué importa:** La tasa de eventos detectados depende del volumen que el detector ve, que crece como el cubo del alcance. Una mejora pequeña en sensibilidad se traduce en muchos más eventos.

📘 **Dónde se aprende** (1 clase): [B28-C07 · Fuentes compactas binarias](../programa/clases/B28/B28-C07-fuentes-compactas-binarias/CLASE.md).

### Factor de pérdida de polarización

- El factor de pérdida de polarización `PLF = |ê_t · ê_r*|²` va de 0 a 1.

🎯 **Por qué importa (clase B91-C02):** Un enlace pierde potencia si las polarizaciones no coinciden, y puede perderla toda si son ortogonales. La decisión central: ¿qué polarización y qué razón axial exigir a las dos antenas para que la desadaptación quede por debajo del margen del enlace?

📘 **Dónde se aprende** (1 clase): [B91-C02 · Polarización de antenas y pérdidas por desadaptación](../programa/clases/B91/B91-C02-polarizacion-de-antenas-y-perdidas-por-desadaptacion/CLASE.md).

### Factor de pérdida por polarización

- El factor de pérdida por polarización (PLF) de dos antenas lineales con desalineación `ψ` es `cos²ψ`.

🎯 **Por qué importa (clase B89-C01):** Todo presupuesto de enlace, toda antena y toda banda parten de la misma onda. Confundir longitud de onda con frecuencia, o potencia con densidad de flujo, rompe los cálculos de las clases siguientes.

📘 **Dónde se aprende** (1 clase): [B89-C01 · Electromagnetismo aplicado a enlaces](../programa/clases/B89/B89-C01-electromagnetismo-aplicado-a-enlaces/CLASE.md).

### Factor de pruebas

- El factor de pruebas corrige por el número de búsquedas.

💡 **Cómo se explica en la clase [B28-C09](../programa/clases/B28/B28-C09-alertas-cientificas-en-tiempo-real/CLASE.md):**
- *Descripción textual:* las etapas suman la latencia; el FAR se traduce a probabilidad y sigmas; el umbral sale de la cola del ruido y se contrasta por Monte Carlo; el factor de pruebas pasa de p local a global.
- ⚠️ **Error frecuente:** Olvidar el factor de pruebas. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Una alerta tardía pierde el evento; una alerta con muchas falsas alarmas agota a los observadores. La decisión central: ¿qué umbral produce una tasa de falsas alarmas aceptable y cuánto tarda la alerta en llegar?

📘 **Dónde se aprende** (2 clases): [B28-C09 · Alertas científicas en tiempo real](../programa/clases/B28/B28-C09-alertas-cientificas-en-tiempo-real/CLASE.md); [B28-C13 · Estadística de significancia](../programa/clases/B28/B28-C13-estadistica-de-significancia/CLASE.md).

### Factor de recuperación de capital

- El factor de recuperación de capital `CRF = r(1+r)ⁿ/((1+r)ⁿ − 1)` convierte un monto inicial en pago anual.

🎯 **Por qué importa (clase B124-C24):** B124 estima costos de misión, pero una instalación que opera años necesita separar el capital de la operación y ponerlos en una misma unidad. La decisión central: ¿a qué costo por kilogramo produce la instalación y desde qué producción conviene frente a traer el producto?

📘 **Dónde se aprende** (1 clase): [B124-C24 · CapEx y OpEx de una instalación extraterrestre](../programa/clases/B124/B124-C24-capex-y-opex-de-una-instalacion-extraterrestre/CLASE.md).

### Factor de redistribución

- El factor de redistribución `f` es `1/4` con redistribución global, `1/2` con redistribución solo en el hemisferio diurno y `1` en el punto subsolar sin redistribución.

🎯 **Por qué importa (clase B54-C17):** La temperatura de equilibrio de un exoplaneta es el primer número que se calcula. La pregunta motivadora: ¿cuánto cambia esa temperatura si el calor se redistribuye o no?

📘 **Dónde se aprende** (1 clase): [B54-C17 · Clima exoplanetario](../programa/clases/B54/B54-C17-clima-exoplanetario/CLASE.md).

### Factor de ruido en exceso

- El factor de ruido en exceso `F²` multiplica la varianza de Poisson.

💡 **Cómo se explica en la clase [B44-C09](../programa/clases/B44/B44-C09-ganancia-electronica/CLASE.md):**
- *Descripción textual:* cada etapa multiplica la carga con probabilidad `p`; tras `N` etapas la media crece como `(1+p)^N` y la varianza da el factor de ruido en exceso.
- 🎯 **Por qué importa:** Para señales muy débiles el ruido de lectura domina. La decisión central: ¿cuándo compensa multiplicar la carga a costa del ruido en exceso?

📘 **Dónde se aprende** (1 clase): [B44-C09 · Ganancia electrónica](../programa/clases/B44/B44-C09-ganancia-electronica/CLASE.md).

### Factor de seguridad

- El factor de seguridad `FS` compara resistencia y carga;
- El factor de seguridad multiplica la carga límite para obtener la de diseño.
- El factor de seguridad multiplica la fuerza mínima para el diseño.

💡 **Cómo se explica en la clase [B66-C02](../programa/clases/B66/B66-C02-procesos-de-ladera-y-transporte-de-masa/CLASE.md):**
- En cambio el factor de seguridad, el ángulo crítico, el alcance y `H/L` no dependen de `g`.
- *Descripción textual:* los ángulos y la presión de poros dan el factor de seguridad; si hay falla, el bloque acelera, llega a la base con una velocidad y se detiene tras un alcance.
- 🎯 **Por qué importa:** Un deslizamiento marciano o titaniano parece igual a uno terrestre, pero su velocidad y duración no lo son. La decisión central: ¿qué propiedades de un deslizamiento dependen de la gravedad y cuáles no?

📘 **Dónde se aprende** (3 clases): [B66-C02 · Procesos de ladera y transporte de masa](../programa/clases/B66/B66-C02-procesos-de-ladera-y-transporte-de-masa/CLASE.md); [B77-C10 · Restricciones de cargas estructurales](../programa/clases/B77/B77-C10-restricciones-de-cargas-estructurales/CLASE.md); [B97-C10 · Manipulación de herramientas](../programa/clases/B97/B97-C10-manipulacion-de-herramientas/CLASE.md).

### Factor de seguridad (FS)

- Esfuerzo de aro: esfuerzo circunferencial `σ = P r/t`. Factor de seguridad (FS): cociente entre límite elástico y esfuerzo.

💡 **Cómo se explica en la clase [B106-C02](../programa/clases/B106/B106-C02-presurizacion-de-modulos/CLASE.md):**
- Un cilindro de 2 m de radio a 101,325 kPa necesita, con factor de seguridad 2 y una aleación ilustrativa de 276 MPa, un espesor mínimo de 1,468 mm (51,7 kg de pared por metro); a 34,5 kPa bastan 0,500 mm.
- 🎯 **Por qué importa:** La presión interior empuja hacia afuera sobre todo el casco; un espesor insuficiente rompe el recinto y un orificio pequeño lo vacía lentamente. La decisión central: ¿qué espesor mínimo y qué tiempo de respuesta hay que garantizar para una presión y un tamaño de orificio dados?

📘 **Dónde se aprende** (1 clase): [B106-C02 · Presurización de módulos](../programa/clases/B106/B106-C02-presurizacion-de-modulos/CLASE.md).

### Factor de tasa

- El factor de tasa `f = dlnD/dlna`.

💡 **Cómo se explica en la clase [B36-C01](../programa/clases/B36/B36-C01-crecimiento-lineal-de-perturbaciones-de-densidad/CLASE.md):**
- Con `Ωm = 0,315` (resumen de Planck 2018) y un universo plano, el crecimiento lineal hasta hoy queda en `D(1) = 0,7878` frente a `1` de un universo de solo materia, y el factor de tasa en `f(0) = 0,527`.
- 🎯 **Por qué importa:** Sin la teoría lineal no se sabe cuánto ha crecido una perturbación entre el CMB y hoy. La decisión central: ¿cuánto frena la constante cosmológica el crecimiento y cómo se comprueba la solución numérica?

📘 **Dónde se aprende** (1 clase): [B36-C01 · Crecimiento lineal de perturbaciones de densidad](../programa/clases/B36/B36-C01-crecimiento-lineal-de-perturbaciones-de-densidad/CLASE.md).

### Factor de temperatura

- El factor de temperatura `π_T` sigue la ley de Arrhenius.

🎯 **Por qué importa (clase B93-C04):** Cuantificar la confiabilidad de la electrónica no estaba en el tronco. La decisión central: ¿qué tasa de fallas y qué MTBF tiene la suma de las piezas, qué probabilidad de supervivencia da para una misión, y cuánto la mejoran el derating y la redundancia?

📘 **Dónde se aprende** (1 clase): [B93-C04 · Análisis de confiabilidad de electrónica (MTBF y derating)](../programa/clases/B93/B93-C04-analisis-de-confiabilidad-de-electronica-mtbf-y-derating/CLASE.md).

### Factor de trabajo

- El factor de trabajo es la fracción de ranuras con pulso: `1/(1,25 M)`.

💡 **Cómo se explica en la clase [B92-C01](../programa/clases/B92/B92-C01-fuentes-laser-y-amplificadores-para-enlaces-espaciales/CLASE.md):**
- P --> D["factor de trabajo<br/>1 / (1,25 M)"]
- *Descripción textual:* la semilla pasa por el amplificador; la potencia media, con el factor de trabajo de PPM, da la potencia de pico y la energía por pulso; con la energía del fotón da la tasa de fotones.
- ⚠️ **Error frecuente:** Olvidar las ranuras de guarda. Se corrige con 8.3: el factor de trabajo es `1/(1,25 M)`.
- 🎯 **Por qué importa:** Un enlace óptico se dimensiona con fotones, no con vatios. La decisión central: ¿cuánta potencia de pico y cuánta energía por pulso debe entregar la fuente para una potencia media dada, y hasta dónde sirve aumentar la ganancia del amplificador?

📘 **Dónde se aprende** (1 clase): [B92-C01 · Fuentes láser y amplificadores para enlaces espaciales](../programa/clases/B92/B92-C01-fuentes-laser-y-amplificadores-para-enlaces-espaciales/CLASE.md).

### Factor de uso

- El factor de uso es la fracción de la velocidad máxima que se aprovecha en promedio.

💡 **Cómo se explica en la clase [B97-C01](../programa/clases/B97/B97-C01-robots-rover-y-orbitadores/CLASE.md):**
- Con un factor de uso de `0,5` y `4 h` de conducción, el recorrido es `304,0` m por día de operación, y `5 km` llevan `16,45` días.
- Un orbitador ilustrativo a `300 km` con una franja de `12 km` la cubre con 4,44 min de imagen continua; un rover que debe recorrer `5 km` con un factor de uso `0,5` tarda 16,45 días de operación.
- ⚠️ **Error frecuente:** Usar la velocidad máxima como promedio. El factor de uso lo corrige (8.3)
- 🎯 **Por qué importa:** Elegir entre «ir con un rover» y «mirar desde órbita» es la primera decisión de una misión robótica, y se toma con órdenes de magnitud. Sin ellos, se prometen traslados que tardan meses o coberturas que una órbita no entrega.

📘 **Dónde se aprende** (1 clase): [B97-C01 · Robots rover y orbitadores](../programa/clases/B97/B97-C01-robots-rover-y-orbitadores/CLASE.md).

### Factor de velocidad

- El factor de velocidad es `v/c` en el cable.

💡 **Cómo se explica en la clase [B49-C02](../programa/clases/B49/B49-C02-adaptacion-de-impedancias-y-lineas-de-transmision-en-antenas/CLASE.md):**
- ⚠️ **Error frecuente:** Usar la longitud en el vacío en lugar de la del cable. Se corrige con el factor de velocidad.
- 🎯 **Por qué importa:** Una antena desadaptada devuelve potencia y empeora la sensibilidad. La decisión central: ¿cuánta potencia se refleja y cómo se adapta con un tramo de línea?

📘 **Dónde se aprende** (1 clase): [B49-C02 · Adaptación de impedancias y líneas de transmisión en antenas](../programa/clases/B49/B49-C02-adaptacion-de-impedancias-y-lineas-de-transmision-en-antenas/CLASE.md).

### Factor de vista

- El factor de vista es la fracción de la emisión de un elemento que llega a otro.
- CVCM: volátiles condensables recogidos, `100 m_col/mᵢ`. Factor de vista: fracción de la emisión de una superficie que alcanza a otra.

💡 **Cómo se explica en la clase [B50-C05](../programa/clases/B50/B50-C05-luz-parasita-y-analisis-de-rayos-dispersos/CLASE.md):**
- P["parche lambertiano"] --> V["factor de vista"]
- *Descripción textual:* la reflectancia fija la potencia del fantasma, el trazado fija su foco y tamaño, y el factor de vista mide la luz dispersa que llega al detector.
- 🎯 **Por qué importa:** El contraste de un instrumento no depende solo de la imagen: depende de cuánta luz llega por caminos no deseados. La decisión central: ¿qué fracción de luz llega por un camino parásito y cómo se reduce?

📘 **Dónde se aprende** (2 clases): [B50-C05 · Luz parásita y análisis de rayos dispersos](../programa/clases/B50/B50-C05-luz-parasita-y-analisis-de-rayos-dispersos/CLASE.md); [B90-C04 · Control de contaminación](../programa/clases/B90/B90-C04-control-de-contaminacion/CLASE.md).

### Factor Doppler

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B27-C11](../programa/clases/B27/B27-C11-chorros-relativistas/CLASE.md):**
- *Descripción textual:* la velocidad y el factor de Lorentz dan la velocidad aparente y el factor Doppler; el máximo de la primera ocurre cuando `cosθ = β`, donde `δ = γ`.
- 🎯 **Por qué importa:** Un chorro que se acerca puede parecer más rápido que la luz sin violar nada, y su brillo cambia en órdenes de magnitud según el ángulo. Sin estos efectos no se pueden comparar chorros ni inferir su velocidad.

📘 **Dónde se aprende** (1 clase): [B27-C11 · Chorros relativistas](../programa/clases/B27/B27-C11-chorros-relativistas/CLASE.md).

### Factor integrante

- El factor integrante `μ(t) = exp(∫ a dt)` convierte el lado izquierdo en `(μ y)′`.

💡 **Cómo se explica en la clase [B11-C03](../programa/clases/B11/B11-C03-ecuaciones-de-primer-orden/CLASE.md):**
- El factor integrante lleva a una integral.
- D -->|sí| E["Factor integrante<br/>μ = exp(∫a dt)"]
- 🎯 **Por qué importa:** Muchos procesos espaciales relajan hacia un equilibrio: una cápsula que cae frena hasta una velocidad terminal, un instrumento se enfría hacia la temperatura de su entorno, una población de partículas decae.

📘 **Dónde se aprende** (1 clase): [B11-C03 · Ecuaciones de primer orden](../programa/clases/B11/B11-C03-ecuaciones-de-primer-orden/CLASE.md).

### Factor preexponencial

- El factor preexponencial `ν` es la frecuencia de intento (en ML s⁻¹ para orden cero, en s⁻¹ para orden uno).

🎯 **Por qué importa (clase B68-C01):** Un hielo de CO que dura mil millones de años a 15 K desaparece en un segundo a 30 K. Esa sensibilidad exponencial decide dónde está la «línea de nieve» de cada molécula y qué hay en el gas.

📘 **Dónde se aprende** (1 clase): [B68-C01 · Desorción térmica de hielos interestelares](../programa/clases/B68/B68-C01-desorcion-termica-de-hielos-interestelares/CLASE.md).

### Factor Q

- El factor `Q` es `1/(2ζ)` y es la amplificación en resonancia.
- Resonancia: frecuencia a la que un equipo amplifica. Factor `Q`: amplificación en resonancia.

🎯 **Por qué importa (clase B84-C11):** Un equipo con `Q = 10` en resonancia recibe 10 veces la aceleración de entrada; Miles da la respuesta rms en una línea.

📘 **Dónde se aprende** (2 clases): [B84-C11 · Vibraciones y resonancias](../programa/clases/B84/B84-C11-vibraciones-y-resonancias/CLASE.md); [B90-C09 · Ensayos de vibración](../programa/clases/B90/B90-C09-ensayos-de-vibracion/CLASE.md).

### Factor teórico

- El factor teórico `K_t = σ_máx/σ_nom`.

💡 **Cómo se explica en la clase [B84-C29](../programa/clases/B84/B84-C29-concentraciones-de-tension-y-entallas/CLASE.md):**
- *Descripción textual:* Kirsch da el campo y el factor teórico; la integral verifica el equilibrio; con la sensibilidad se pasa a `K_f` y a la vida.
- 🎯 **Por qué importa:** Una tensión remota de 100 MPa se triplica a 300 MPa en el borde de un agujero; con `K_f = 2,8` la vida baja de 10¹¹ a 10⁷ ciclos. La decisión central: ¿qué tensión local y qué vida resultan de un agujero en una placa cargada?

📘 **Dónde se aprende** (1 clase): [B84-C29 · Concentraciones de tensión y entallas](../programa/clases/B84/B84-C29-concentraciones-de-tension-y-entallas/CLASE.md).

### Factor Y

- El factor Y es el cociente de potencias con carga caliente y fría.

💡 **Cómo se explica en la clase [B49-C06](../programa/clases/B49/B49-C06-amplificadores-de-bajo-ruido-lna-tecnologia-ganancia-y-adaptacion/CLASE.md):**
- H["carga caliente/fría"] --> Y["factor Y"]
- El factor Y simulado da `11,795 K`, `3,09 %` de diferencia.
- 🎯 **Por qué importa:** Una décima de decibelio antes del primer amplificador cuesta más que mejorar el mezclador. La decisión central: ¿qué bloque domina la temperatura de ruido y qué pérdidas deben evitarse antes de él?

📘 **Dónde se aprende** (1 clase): [B49-C06 · Amplificadores de bajo ruido (LNA): tecnología, ganancia y adaptación](../programa/clases/B49/B49-C06-amplificadores-de-bajo-ruido-lna-tecnologia-ganancia-y-adaptacion/CLASE.md).

### Factor β

- El factor β es la fracción de la probabilidad de falla que es de causa común.

🎯 **Por qué importa (clase B97-C17):** Duplicar un canal parece bajar la probabilidad de falla al cuadrado; pero si una causa afecta a ambos, la mejora real es mucho menor. Calcularlo evita sobreestimar la seguridad de una arquitectura redundante.

📘 **Dónde se aprende** (1 clase): [B97-C17 · Seguridad funcional robótica](../programa/clases/B97/B97-C17-seguridad-funcional-robotica/CLASE.md).

### Factores de Atwater

- Los factores de Atwater son 4 kcal/g de proteína y carbohidrato y 9 kcal/g de grasa.

🎯 **Por qué importa (clase B105-C12):** Cada kilogramo de alimento que se lanza cuesta; cada kilocaloría que falta se paga con masa corporal. La decisión central: ¿cuánto alimento hay que transportar para una misión y con qué margen frente a la incertidumbre del gasto?

📘 **Dónde se aprende** (1 clase): [B105-C12 · Nutrición espacial](../programa/clases/B105/B105-C12-nutricion-espacial/CLASE.md).

### Factores de conversión

- Los factores de conversión son cocientes iguales a 1, por ejemplo `1000 m / 1 km`.

🎯 **Por qué importa (clase B05-C01):** La pregunta motivadora es: ¿cómo sé que una fórmula o un cálculo tiene sentido antes de confiar en su resultado? La decisión central es qué declarar junto a cada número (magnitud, unidad y dimensión) y cómo comprobar que las ecuaciones son coherentes.

📘 **Dónde se aprende** (1 clase): [B05-C01 · Magnitudes físicas y dimensiones](../programa/clases/B05/B05-C01-magnitudes-fisicas-y-dimensiones/CLASE.md).

### Factores modificadores

- Una reserva es la parte del recurso que, aplicados los factores modificadores (accesibilidad, recuperación), se puede extraer.

💡 **Cómo se explica en la clase [B67-C04](../programa/clases/B67/B67-C04-estimacion-de-reservas-y-categorias-de-recursos/CLASE.md):**
- *Descripción textual:* las muestras dan la fracción de hielo con su intervalo; junto con área, espesor y densidad se propaga la incertidumbre a la masa; el semiancho define la categoría; solo lo Medido o Indicado se convierte en reserva tras los factores modificadores.
- Por conversión: recurso por factores modificadores igual a reserva.
- 🎯 **Por qué importa:** Decir «hay 330 kt» sin intervalo ni categoría invita a decisiones equivocadas. La decisión central: ¿cuánto del recurso se puede llamar reserva, y qué falta para subir de categoría?

📘 **Dónde se aprende** (1 clase): [B67-C04 · Estimación de reservas y categorías de recursos](../programa/clases/B67/B67-C04-estimacion-de-reservas-y-categorias-de-recursos/CLASE.md).

### Factorización

- Una factorización (o descomposición) escribe `A` como producto de factores con estructura.

💡 **Cómo se explica en la clase [B10-C10](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md):**
- La factorización de Cholesky de `P` lo permite.
- 🎯 **Por qué importa:** Un filtro de navegación resuelve el mismo sistema con miles de lados derechos distintos; una simulación necesita muestras aleatorias con una covarianza dada; un ajuste de mínimos cuadrados quiere estabilidad. En cada caso el trabajo se hace una vez al factorizar y luego se reutiliza.

📘 **Dónde se aprende** (1 clase): [B10-C10 · Descomposiciones matriciales](../programa/clases/B10/B10-C10-descomposiciones-matriciales/CLASE.md).

### Factorización de Cholesky

- La factorización de Cholesky `P = L Lᵀ` existe si `P` es definida positiva y sirve para generar muestras.

💡 **Cómo se explica en la clase [B12-C18](../programa/clases/B12/B12-C18-matrices-de-covarianza/CLASE.md):**
- Una «matriz de correlación» con `r₁₂ = 0,9`, `r₁₃ = 0,9`, `r₂₃ = −0,9` parece razonable pero tiene un autovalor `−0,8`: no es semidefinida positiva, y la factorización de Cholesky falla.
- 🎯 **Por qué importa:** El resultado de una determinación de órbita o de un ajuste no es un número sino un vector con una matriz de covarianza; sin ella no se puede propagar, comparar con otro resultado ni calcular probabilidades.

📘 **Dónde se aprende** (1 clase): [B12-C18 · Matrices de covarianza](../programa/clases/B12/B12-C18-matrices-de-covarianza/CLASE.md).

### Factorización QR

- La factorización QR escribe `A = Q R` con `Q` de columnas ortonormales y `R` triangular superior.

🎯 **Por qué importa (clase B10-C07):** Una estación mide la distancia a un satélite cada segundo durante diez segundos. Hay once medidas y solo tres parámetros que describir (posición, velocidad y aceleración radiales).

📘 **Dónde se aprende** (1 clase): [B10-C07 · Proyecciones y mínimos cuadrados](../programa/clases/B10/B10-C07-proyecciones-y-minimos-cuadrados/CLASE.md).

### Factorizar

- La propiedad distributiva dice `a(b + c) = ab + ac`. Factorizar es escribir una suma como un producto (`6a + 9 = 3(2a + 3)`).
- Una raíz es un valor de `x` que hace el polinomio igual a cero. Factorizar es escribir el polinomio como producto de polinomios de menor grado.

💡 **Cómo se explica en la clase [B03-C13](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md):**
- X --> S["Simplificar o factorizar si hace falta"]
- 🎯 **Por qué importa:** ¿Cuánto tarda una señal en llegar desde la Tierra hasta Marte? Depende de dónde estén los dos planetas.

📘 **Dónde se aprende** (2 clases): [B03-C13 · Expresiones algebraicas iniciales](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md); [B04-C01 · Polinomios y factorización](../programa/clases/B04/B04-C01-polinomios-y-factorizacion/CLASE.md).

### FAIR

- La semilla fija la secuencia aleatoria. FAIR son las cuatro propiedades de los datos (localizables, accesibles, interoperables, reutilizables).

💡 **Cómo se explica en la clase [B124-C14](../programa/clases/B124/B124-C14-ciencia-abierta-y-reproducibilidad/CLASE.md):**
- Faltan, por ejemplo, el índice en un repositorio, los vocabularios controlados y los enlaces; los criterios son un ejemplo propio de la clase, no la lista oficial de FAIR.
- M["metadatos y licencia"] --> F["lista FAIR"]
- ⚠️ **Error frecuente:** Tomar los 12 criterios como la norma FAIR. Se corrige con 8.4.
- 🎯 **Por qué importa:** «Es reproducible» suele afirmarse sin evidencia. La decisión central: ¿qué hay que fijar y registrar para que un análisis dé el mismo resultado y se pueda comprobar?

📘 **Dónde se aprende** (1 clase): [B124-C14 · Ciencia abierta y reproducibilidad](../programa/clases/B124/B124-C14-ciencia-abierta-y-reproducibilidad/CLASE.md).

### Falla anular

- La falla anular es la fractura vertical que lo rodea.

💡 **Cómo se explica en la clase [B70-C03](../programa/clases/B70/B70-C03-calderas-planetarias-formacion-y-colapso/CLASE.md):**
- Resistencia de la falla anular: `2πR T τ`.
- *Descripción textual:* el volumen evacuado genera subpresión; si supera la resistencia de la falla anular el techo colapsa y el hundimiento sigue del balance de volumen.
- 🎯 **Por qué importa:** Evacuar magma no siempre hunde el techo. La decisión central: ¿cuánta subpresión resiste un techo y cuánto magma hay que sacar para vencerla?

📘 **Dónde se aprende** (1 clase): [B70-C03 · Calderas planetarias: formación y colapso](../programa/clases/B70/B70-C03-calderas-planetarias-formacion-y-colapso/CLASE.md).

### Falla común

- La falla común afecta igual a ambos núcleos.

🎯 **Por qué importa (clase B88-C25):** Lockstep detecta fallos transitorios de un núcleo, pero no los corrige ni cubre causas comunes. La decisión central: ¿cada cuántos ciclos comparar, y qué fallas escapan?

📘 **Dónde se aprende** (1 clase): [B88-C25 · Redundancia de procesamiento y ejecución en paralelo (lockstep)](../programa/clases/B88/B88-C25-redundancia-de-procesamiento-y-ejecucion-en-paralelo-lockstep/CLASE.md).

### Falla de causa común

- La falla de causa común afecta a varios canales por un mismo motivo.

🎯 **Por qué importa (clase B97-C17):** Duplicar un canal parece bajar la probabilidad de falla al cuadrado; pero si una causa afecta a ambos, la mejora real es mucho menor. Calcularlo evita sobreestimar la seguridad de una arquitectura redundante.

📘 **Dónde se aprende** (1 clase): [B97-C17 · Seguridad funcional robótica](../programa/clases/B97/B97-C17-seguridad-funcional-robotica/CLASE.md).

### Falla de vuelo

- La falla de vuelo es la pérdida del vehículo antes de completar la trayectoria.

🎯 **Por qué importa (clase B121-C01):** La autorización de un lanzamiento no es un trámite abstracto: incluye criterios numéricos de riesgo. La decisión central: ¿una trayectoria cumple el criterio de riesgo colectivo e individual que exige la licencia y con qué margen?

📘 **Dónde se aprende** (1 clase): [B121-C01 · Licencias y requisitos nacionales para el lanzamiento](../programa/clases/B121/B121-C01-licencias-y-requisitos-nacionales-para-el-lanzamiento/CLASE.md).

### Falla en grupo

- Una falla en grupo afecta a varios satélites a la vez.

🎯 **Por qué importa (clase B124-C08):** El seguro no elimina el riesgo: lo traslada a quien puede juntarlo. La decisión central: ¿cuánto cobrar por cubrir un riesgo y con qué probabilidad el asegurador se queda sin capital?

📘 **Dónde se aprende** (1 clase): [B124-C08 · Seguros y riesgo espacial](../programa/clases/B124/B124-C08-seguros-y-riesgo-espacial/CLASE.md).

### Falla latente

- Resistencia de fuga: camino resistivo que permite disipar la carga lentamente. Falla latente: daño que no se manifiesta hasta después.

🎯 **Por qué importa (clase B90-C03):** Un componente electrónico puede quedar con una falla latente tras una descarga que nadie sintió: una persona percibe una chispa solo por encima de unos miles de voltios (orden de magnitud no consultado), por encima de lo que puede dañar a un componente sensible.

📘 **Dónde se aprende** (1 clase): [B90-C03 · Protección frente a ESD](../programa/clases/B90/B90-C03-proteccion-frente-a-esd/CLASE.md).

### Fallo

- Un acierto (*hit*) es encontrar el dato en caché; un fallo (*miss*), tener que ir a un nivel inferior.
- El fallo es la distancia nominal entre centros.
- El fallo es cualquier caso sin solución, con excepción o con residuo mayor.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B76-C14](../programa/clases/B76/B76-C14-evasion-de-colision/CLASE.md):**
- Para `Pc ≤ 10⁻⁶` se necesita un fallo de `351,6 m`, o sea `231,6 m` más.
- M["fallo nominal, sigma, HBR"] --> Q["cuadratura polar"]
- ⚠️ **Error frecuente:** Comparar la distancia de fallo sin la incertidumbre. Se corrige con 8.1.
- 🎯 **Por qué importa:** Una distancia de fallo pequeña no basta para decidir: importa cuánto vale frente a la incertidumbre. La decisión central: ¿cuál es la probabilidad de colisión y cuánto impulso cuesta bajarla de un umbral?

📘 **Dónde se aprende** (4 clases): [B18-C03 · Jerarquía y estructuras de memoria](../programa/clases/B18/B18-C03-jerarquia-y-estructuras-de-memoria/CLASE.md); [B30-C20 · Análisis de alerta solar real](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md); [B76-C14 · Evasión de colisión](../programa/clases/B76/B76-C14-evasion-de-colision/CLASE.md); [B82-C07 · Benchmark entre solucionadores de Lambert](../programa/clases/B82/B82-C07-benchmark-entre-solucionadores-de-lambert/CLASE.md).

### Fallo de caché

- Un fallo de caché puede multiplicar el tiempo.

🎯 **Por qué importa (clase B88-C30):** El análisis de planificación (C05) necesita `C` de cada tarea, y medir no basta porque el peor camino puede no ejercitarse. La decisión central: ¿cuál es una cota segura del tiempo de ejecución y cuánto pesimismo trae?

📘 **Dónde se aprende** (1 clase): [B88-C30 · Análisis de peor caso de tiempo de ejecución (WCET)](../programa/clases/B88/B88-C30-analisis-de-peor-caso-de-tiempo-de-ejecucion-wcet/CLASE.md).

### Fallo silencioso

- Un fallo silencioso pasa sin detección.

🎯 **Por qué importa (clase B88-C34):** Un FDIR no probado es una hipótesis. La decisión central: ¿cuántas inyecciones hacen falta para estimar la cobertura con una incertidumbre aceptable y qué fallas escapan?

📘 **Dónde se aprende** (1 clase): [B88-C34 · Pruebas de inyección de fallos](../programa/clases/B88/B88-C34-pruebas-de-inyeccion-de-fallos/CLASE.md).

### Falsa aceptación (PFA)

- Banda de guarda `w`: margen que se resta al límite para aceptar. Falsa aceptación (PFA): aceptar una unidad realmente fuera de especificación.

💡 **Cómo se explica en la clase [B90-C08](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md):**
- Sin banda de guarda se acepta el 0,012 % de unidades malas y se rechaza el 0,019 % de buenas; con guarda `U` la falsa aceptación baja a 0,0003 % y el falso rechazo sube a 0,128 %.
- Descripción larga: al subir la banda de guarda la falsa aceptación se acerca a cero y el falso rechazo crece de 0,019 % a 0,37 %.
- 🎯 **Por qué importa:** Toda medida tiene incertidumbre. Si se acepta con el límite exacto, algunas unidades malas pasan; si se endurece el criterio, algunas buenas se rechazan y cuesta tiempo.

📘 **Dónde se aprende** (1 clase): [B90-C08 · Procedimientos de prueba funcional](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md).

### Falsa alarma

- Una falsa alarma es una detección que no corresponde a ninguna fuente; su tasa es la fracción de píxeles (o el número por imagen) que superan el umbral solo por ruido.
- Una falsa alarma es un punto normal señalado como anómalo.
- Un falso «seguro» es un peligro declarado transitable; una falsa alarma es una celda segura declarada peligrosa.
- *(y 8 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B48-C23](../programa/clases/B48/B48-C23-observabilidad-del-software-de-observatorio-registros-metricas-y-alertas/CLASE.md):**
- La regla de una sola muestra detecta en 1,19 muestras, pero con falsa alarma de 2,28 % por muestra, unas 200 veces mayor que la de la regla 3 de 5 por ventana.
- *Descripción textual:* los registros se convierten en métricas; una regla k de m sobre el umbral decide la alerta, y su falsa alarma y su retardo se calculan por binomial y simulación.
- 🎯 **Por qué importa:** Demasiadas falsas alarmas se ignoran; muy pocas dejan las averías sin ver. La decisión central: ¿qué regla de alerta equilibra falsas alarmas y retardo?

📘 **Dónde se aprende** (11 clases): [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B17-C05 · Detección de anomalías](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md); [B30-C20 · Análisis de alerta solar real](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md); [B48-C23 · Observabilidad del software de observatorio: registros, métricas y alertas](../programa/clases/B48/B48-C23-observabilidad-del-software-de-observatorio-registros-metricas-y-alertas/CLASE.md); [B88-C12 · Detección aislamiento y recuperación de fallos](../programa/clases/B88/B88-C12-deteccion-aislamiento-y-recuperacion-de-fallos/CLASE.md); [B89-C24 · Recepción de telemetría débil](../programa/clases/B89/B89-C24-recepcion-de-telemetria-debil/CLASE.md) y 5 más.

### Falsa marca

- La falsa marca y la detección.

🎯 **Por qué importa (clase B51-C13):** Dejar RFI en los datos degrada la imagen; marcar demasiado pierde señal. La decisión central: ¿qué umbral marca la interferencia sin marcar el ruido, y cómo se detecta la interferencia débil y extendida?

📘 **Dónde se aprende** (1 clase): [B51-C13 · Marcado de datos espurios e interferencia en visibilidades](../programa/clases/B51/B51-C13-marcado-de-datos-espurios-e-interferencia-en-visibilidades/CLASE.md).

### Falsable

- Una hipótesis es falsable si existe al menos un resultado posible que la contradiga.

🎯 **Por qué importa (clase B01-C07):** Una afirmación que ningún resultado posible contradice no enseña nada. Si dices «la Luna cambia de tamaño aparente» y, ocurra lo que ocurra, tu frase queda a salvo, no has dicho gran cosa.

📘 **Dónde se aprende** (1 clase): [B01-C07 · Hipótesis y predicciones falsables](../programa/clases/B01/B01-C07-hipotesis-y-predicciones-falsables/CLASE.md).

### Falso color

- Una composición asigna bandas a los canales rojo, verde y azul de la pantalla; la de falso color usa el infrarrojo cercano.

💡 **Cómo se explica en la clase [B57-C05](../programa/clases/B57/B57-C05-imagenes-multiespectrales/CLASE.md):**
- Por color: composiciones RGB y de falso color.
- ⚠️ **Error frecuente:** Confundir falso color con color real. Se corrige con 6.
- 🎯 **Por qué importa:** Con una sola banda el agua oscura, la sombra y el asfalto se confunden; con varias, cada cubierta deja una firma distinta. La decisión central: ¿qué combinación de bandas separa las cubiertas que me interesan y cómo recupero detalle espacial sin falsear los colores?

📘 **Dónde se aprende** (1 clase): [B57-C05 · Imágenes multiespectrales](../programa/clases/B57/B57-C05-imagenes-multiespectrales/CLASE.md).

### Falso disparo

- Vigilante (*watchdog*): dispara una parada si faltan latidos. Falso disparo: parada sin falla real.

🎯 **Por qué importa (clase B48-C09):** Un vigilante muy sensible detiene la observación sin motivo y uno muy lento no protege. La decisión central: ¿tras cuántos latidos perdidos hay que disparar la parada?

📘 **Dónde se aprende** (1 clase): [B48-C09 · Control remoto de telescopios](../programa/clases/B48/B48-C09-control-remoto-de-telescopios/CLASE.md).

### Falso negativo

- Un falso positivo es una alarma sin error real; un falso negativo, un error que pasa inadvertido.

🎯 **Por qué importa (clase B14-C10):** Cambias una línea de un propagador orbital «solo para ordenarlo» y el período de una órbita pasa de 5553,624562 s a 5553,627342 s (situación ilustrativa con cifras de esta clase). ¿Es un error o ruido?

📘 **Dónde se aprende** (1 clase): [B14-C10 · Pruebas de regresión numérica](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md).

### Falso positivo

- Un falso positivo es una alarma sin error real; un falso negativo, un error que pasa inadvertido.
- Un falso positivo es declarar un efecto que no existe.
- Un falso positivo es un píxel marcado que no es objeto.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C23](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md):**
- Si de verdad se hacen 20 pruebas, con Bonferroni se usa `α/20 = 0,0025` por prueba: la probabilidad teórica de al menos un falso positivo pasa a `1 − 0,9975²⁰ = 0,0488`, y la simulada fue `0,0519` (dentro de la tolerancia de cuatro errores estándar).
- En uno decides el análisis, lo fijas y luego miras los datos: la probabilidad de falso positivo es la que declaraste.
- 🎯 **Por qué importa:** Tienes una curva de luz y muchas formas de analizarla: otro filtro, otra ventana, otro modelo, otra prueba. Si pruebas veinte y comunicas la que «sale», el resultado casi seguro parece significativo aunque no haya nada.

📘 **Dónde se aprende** (8 clases): [B14-C10 · Pruebas de regresión numérica](../programa/clases/B14/B14-C10-pruebas-de-regresion-numerica/CLASE.md); [B14-C23 · Protocolo preregistrado de análisis](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md); [B15-C13 · Segmentación de imágenes](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md); [B20-C02 · Diseño de un plan de análisis y preregistro](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md); [B29-C08 · Falsos positivos de tránsito](../programa/clases/B29/B29-C08-falsos-positivos-de-transito/CLASE.md); [B56-C13 · Biofirmas químicas](../programa/clases/B56/B56-C13-biofirmas-quimicas/CLASE.md) y 2 más.

### Falso rechazo (PFR)

- Falsa aceptación (PFA): aceptar una unidad realmente fuera de especificación. Falso rechazo (PFR): rechazar una unidad conforme.

💡 **Cómo se explica en la clase [B90-C08](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md):**
- Sin banda de guarda se acepta el 0,012 % de unidades malas y se rechaza el 0,019 % de buenas; con guarda `U` la falsa aceptación baja a 0,0003 % y el falso rechazo sube a 0,128 %.
- Descripción larga: al subir la banda de guarda la falsa aceptación se acerca a cero y el falso rechazo crece de 0,019 % a 0,37 %.
- 🎯 **Por qué importa:** Toda medida tiene incertidumbre. Si se acepta con el límite exacto, algunas unidades malas pasan; si se endurece el criterio, algunas buenas se rechazan y cuesta tiempo.

📘 **Dónde se aprende** (1 clase): [B90-C08 · Procedimientos de prueba funcional](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md).

### Falso «seguro»

- Un falso «seguro» es un peligro declarado transitable; una falsa alarma es una celda segura declarada peligrosa.

🎯 **Por qué importa (clase B103-C04):** El ruido del MDE crece con el cuadrado del rango y, a partir de cierta distancia, la señal de un obstáculo queda por debajo del ruido. La decisión central: ¿hasta qué rango se puede clasificar el terreno de forma útil, y qué política (conservadora o corregida) elegir más allá?

📘 **Dónde se aprende** (1 clase): [B103-C04 · Detección de obstáculos y mapas de traversabilidad](../programa/clases/B103/B103-C04-deteccion-de-obstaculos-y-mapas-de-traversabilidad/CLASE.md).

### Falsos negativos

- La matriz de confusión cuenta aciertos y errores: verdaderos positivos (TP), falsos positivos (FP), verdaderos negativos (TN) y falsos negativos (FN) (S2).

💡 **Cómo se explica en la clase [B17-C12](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md):**
- Ambos extremos se convierten en un costo (falsos positivos por su costo más falsos negativos por el suyo), y se elige el umbral de costo mínimo.
- Si es muy sensible, suena al tostar pan (falsos positivos); si es poco sensible, no suena en un incendio lento (falsos negativos).
- 🎯 **Por qué importa:** Un modelo marca candidatos a planeta, y cada alerta cuesta horas de revisión. Si el modelo acierta el 99 % en una muestra donde el 99 % son negativos, no dice nada útil.

📘 **Dónde se aprende** (1 clase): [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md).

### Falsos positivos

- La matriz de confusión cuenta aciertos y errores: verdaderos positivos (TP), falsos positivos (FP), verdaderos negativos (TN) y falsos negativos (FN) (S2).

💡 **Cómo se explica en la clase [B17-C12](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md):**
- La curva ROC no cambia con la prevalencia, porque usa tasas dentro de cada clase; la de precisión–exhaustividad sí, y por eso refleja la carga de falsos positivos.
- Ambos extremos se convierten en un costo (falsos positivos por su costo más falsos negativos por el suyo), y se elige el umbral de costo mínimo.
- 🎯 **Por qué importa:** Un modelo marca candidatos a planeta, y cada alerta cuesta horas de revisión. Si el modelo acierta el 99 % en una muestra donde el 99 % son negativos, no dice nada útil.

📘 **Dónde se aprende** (1 clase): [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md).

### Falta de fusión

- La falta de fusión ocurre con `E_v` bajo y el exceso de energía (ojo de cerradura) con `E_v` alto.

🎯 **Por qué importa (clase B84-C15):** Dos piezas idénticas con otra velocidad de barrido pueden salir porosas; una ventana de proceso bien trazada evita el desperdicio, y la rugosidad escalonada decide qué superficies se mecanizan. La decisión central: ¿con qué potencia y velocidad se imprime dentro de la ventana y cuánto tarda y qué acabado deja?

📘 **Dónde se aprende** (1 clase): [B84-C15 · Manufactura aditiva](../programa/clases/B84/B84-C15-manufactura-aditiva/CLASE.md).

### Familia Runge–Kutta

- La familia Runge–Kutta agrupa métodos de este tipo con distinto número de etapas.

🎯 **Por qué importa (clase B11-C07):** La mayoría de los programas de simulación científica usa, de forma directa o como base, un método de la familia Runge–Kutta. Entender RK4 permite leer cualquier código de propagación, estimar cuántos pasos necesita una órbita y saber en qué punto empieza a ser conveniente algo más sofisticado.

📘 **Dónde se aprende** (1 clase): [B11-C07 · Runge-Kutta de cuarto orden](../programa/clases/B11/B11-C07-runge-kutta-de-cuarto-orden/CLASE.md).

### Familia tangencial

- La familia tangencial es el conjunto de elipses que salen tangentes.

🎯 **Por qué importa (clase B75-C22):** Antes de optimizar toda la misión conviene entender el primer impulso. La decisión central: ¿qué módulo y qué dirección del primer impulso alcanzan un radio dado con el menor delta-v y en cuánto tiempo?

📘 **Dónde se aprende** (1 clase): [B75-C22 · Modelos de primer impulso](../programa/clases/B75/B75-C22-modelos-de-primer-impulso/CLASE.md).

### Familia variacional

- Una familia variacional es el conjunto de distribuciones permitidas (por ejemplo, gaussianas con media `m` y desviación `s`).

💡 **Cómo se explica en la clase [B19-C05](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md):**
- Imagina la posterior como un objeto en 3D y la familia variacional como una pantalla en la que solo caben ciertas formas.
- 🎯 **Por qué importa:** Con miles de parámetros o millones de datos, un muestreador puede tardar horas o días. La inferencia variacional (VI) elige una familia de distribuciones manejables, por ejemplo gaussianas, y busca dentro de ella la más cercana a la posterior.

📘 **Dónde se aprende** (1 clase): [B19-C05 · Inferencia variacional](../programa/clases/B19/B19-C05-inferencia-variacional/CLASE.md).

### Fantasma

- Un fantasma es una imagen de un objeto brillante producida por dos reflexiones internas.

💡 **Cómo se explica en la clase [B50-C05](../programa/clases/B50/B50-C05-luz-parasita-y-analisis-de-rayos-dispersos/CLASE.md):**
- El fantasma pasa por dos reflexiones, así que su potencia relativa es `R₁R₂ = 1,60 × 10⁻³` sin recubrir y `1,00 × 10⁻⁴` con `R = 0,01`: el recubrimiento reduce el fantasma 16 veces.
- El foco del fantasma por la matriz paraxial es `z = 15,22505 mm` y por el trazado exacto `15,22505 mm`; la imagen real está en `103,3289 mm`.
- ⚠️ **Error frecuente:** Olvidar que el fantasma está desenfocado. Se corrige con 8.2.
- 🎯 **Por qué importa:** El contraste de un instrumento no depende solo de la imagen: depende de cuánta luz llega por caminos no deseados. La decisión central: ¿qué fracción de luz llega por un camino parásito y cómo se reduce?

📘 **Dónde se aprende** (1 clase): [B50-C05 · Luz parásita y análisis de rayos dispersos](../programa/clases/B50/B50-C05-luz-parasita-y-analisis-de-rayos-dispersos/CLASE.md).

### FAR

- El POD es la fracción de eventos detectados, el FAR la de alertas falsas y el CSI la de aciertos sobre todos los casos relevantes.
- El POD, el FAR y el Heidke.

💡 **Cómo se explica en la clase [B30-C20](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md):**
- *Descripción textual:* las medidas se convierten en escalas G, S y R; la regla y lo observado forman la tabla de contingencia, de la que salen POD, FAR y Heidke.
- 🎯 **Por qué importa:** Una alerta con muchas falsas alarmas se ignora y una con muchos fallos no sirve; medir ambas cosas es parte del oficio. La decisión central: ¿cómo se clasifica un evento y cómo se mide si una regla de alerta tiene habilidad?

📘 **Dónde se aprende** (2 clases): [B30-C20 · Análisis de alerta solar real](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md); [B33-C13 · Pronóstico de actividad geomagnética](../programa/clases/B33/B33-C13-pronostico-de-actividad-geomagnetica/CLASE.md).

### Fase

- La fase es la parte del disco lunar iluminada que vemos.
- La fase es la fracción del disco lunar que ves iluminada; se da como porcentaje de 0 % (nueva) a 100 % (llena).
- Una fase es un estado del gas con un rango de temperatura y densidad.
- *(y 13 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C12](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md):**
- Paso 6 · Comprobación. Observa la fase cada noche cerca de la fecha; anota la noche en que el disco se ve completo; compara con la predicción y con una tabla publicada que cites.
- 🎯 **Por qué importa:** La Luna es el reloj más a mano del cielo: cada noche cambia, y cada 29,5 días vuelve a empezar. Pero «a mano» no significa «fácil de explicar»: muchas personas creen que las fases son la sombra de la Tierra sobre la Luna.

📘 **Dónde se aprende** (17 clases): [B01-C12 · Fases lunares y ciclos celestes](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md); [B05-C11 · Movimiento oscilatorio](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md); [B08-C08 · Fases lunares y libración](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md); [B25-C03 · Medio interestelar multifásico](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md); [B29-C06 · Imagen directa de exoplanetas](../programa/clases/B29/B29-C06-imagen-directa-de-exoplanetas/CLASE.md); [B42-C06 · Función de dispersión puntual](../programa/clases/B42/B42-C06-funcion-de-dispersion-puntual/CLASE.md) y 11 más.

### Fase CC

- La fase CC mantiene la corriente; la fase CV mantiene la tensión máxima.

💡 **Cómo se explica en la clase [B86-C06](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md):**
- Más corriente acorta la fase CC pero eleva la pérdida `I²R` y deja una fase CV proporcionalmente más larga (`89 %` del tiempo es CC con `1 A`).
- S0["SOC inicial"] --> CC["fase CC: I fija"]
- 🎯 **Por qué importa:** Cargar más rápido reduce el tiempo pero eleva el calor y la tensión sobre la celda; cargar más lento puede no completar el ciclo antes del siguiente eclipse. El perfil de carga decide si la batería vuelve a su estado de carga en cada órbita.

📘 **Dónde se aprende** (1 clase): [B86-C06 · Gestión de carga](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md).

### Fase crítica

- La fase crítica es la de menor margen.

💡 **Cómo se explica en la clase [B86-C19](../programa/clases/B86/B86-C19-presupuesto-de-potencia-de-mision/CLASE.md):**
- *Descripción textual:* los subsistemas, con su crecimiento por madurez y la reserva de sistema, dan la demanda por fase y la potencia de ala requerida; con la generación de cada fase resultan los márgenes y la fase crítica; un Monte Carlo del crecimiento estima la probabilidad de exceso.
- 🎯 **Por qué importa:** Un presupuesto es un compromiso de ingeniería: cada subsistema promete una potencia que todavía puede crecer. Las reservas por madurez evitan que el ala quede corta cuando una carga nueva consume más de lo previsto.

📘 **Dónde se aprende** (1 clase): [B86-C19 · Presupuesto de potencia de misión](../programa/clases/B86/B86-C19-presupuesto-de-potencia-de-mision/CLASE.md).

### Fase CV

- La fase CC mantiene la corriente; la fase CV mantiene la tensión máxima.

💡 **Cómo se explica en la clase [B86-C06](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md):**
- La fase CV termina en la corriente de corte y repone `1,314 Ah` de los `1,399 Ah` (quedan `0,084 Ah`, que se recuperan en la órbita siguiente o con un corte más bajo).
- Más corriente acorta la fase CC pero eleva la pérdida `I²R` y deja una fase CV proporcionalmente más larga (`89 %` del tiempo es CC con `1 A`).
- ⚠️ **Error frecuente:** Cargar siempre a tensión máxima sin fase CV. Se corrige con 8.1.
- 🎯 **Por qué importa:** Cargar más rápido reduce el tiempo pero eleva el calor y la tensión sobre la celda; cargar más lento puede no completar el ciclo antes del siguiente eclipse. El perfil de carga decide si la batería vuelve a su estado de carga en cada órbita.

📘 **Dónde se aprende** (1 clase): [B86-C06 · Gestión de carga](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md).

### Fase de cierre

- La fase de cierre `arg(V_ij V_jk V_ki)`.
- La fase de cierre (suma de fases en un triángulo).

💡 **Cómo se explica en la clase [B51-C02](../programa/clases/B51/B51-C02-cantidades-de-cierre-fase-y-amplitud-de-cierre/CLASE.md):**
- C --> F["fase de cierre = fase del modelo"]
- 🎯 **Por qué importa:** Cuando las ganancias no se pueden calibrar (VLBI con atmósfera rápida, autocalibración), los cierres son los observables robustos. La decisión central: ¿qué información sobrevive a los errores por antena y cuánta se pierde?

📘 **Dónde se aprende** (2 clases): [B46-C17 · Calibración de fase](../programa/clases/B46/B46-C17-calibracion-de-fase/CLASE.md); [B51-C02 · Cantidades de cierre: fase y amplitud de cierre](../programa/clases/B51/B51-C02-cantidades-de-cierre-fase-y-amplitud-de-cierre/CLASE.md).

### Fase de oscilación

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B28-C03](../programa/clases/B28/B28-C03-neutrinos-astrofisicos/CLASE.md):**
- Para ese `E` y distancias de gigaparsecs, la fase de oscilación solar (con `Δm² = 7,4 × 10⁻⁵ eV²`, ilustrativo) es `~10¹³ rad`: la oscilación se promedia.
- 🎯 **Por qué importa:** Un detector que ve neutrinos muónicos de una fuente lejana no ve lo que salió de ella. Para interpretar la razón de sabores hay que conocer la mezcla.

📘 **Dónde se aprende** (1 clase): [B28-C03 · Neutrinos astrofísicos](../programa/clases/B28/B28-C03-neutrinos-astrofisicos/CLASE.md).

### Fase de recuperación

- La fase de recuperación es el decaimiento.

🎯 **Por qué importa (clase B30-C18):** Prever la profundidad y la duración de una tormenta orienta la protección de redes y satélites. La decisión central: ¿qué mínimo alcanza `Dst*` y cuánto tarda en recuperarse?

📘 **Dónde se aprende** (1 clase): [B30-C18 · Tormentas geomagnéticas](../programa/clases/B30/B30-C18-tormentas-geomagneticas/CLASE.md).

### Fase geométrica

- Acoplamiento: el movimiento del brazo mueve la base. Fase geométrica: giro neto de un lazo cerrado en el espacio articular.

💡 **Cómo se explica en la clase [B101-C06](../programa/clases/B101/B101-C06-simulacion-de-un-brazo-robotico-espacial/CLASE.md):**
- ⚠️ **Error frecuente:** Creer que el giro depende de la velocidad. Es una fase geométrica (8.3)
- 🎯 **Por qué importa:** En una estación o un satélite pesado la base casi no se mueve; en un satélite pequeño, sí. La decisión central: ¿cuánto se mueve la base al mover el brazo y cómo afecta eso a la posición del extremo?

📘 **Dónde se aprende** (1 clase): [B101-C06 · Simulación de un brazo robótico espacial](../programa/clases/B101/B101-C06-simulacion-de-un-brazo-robotico-espacial/CLASE.md).

### Fase interferométrica

- La fase interferométrica es `φ = 4πd/λ` para un desplazamiento `d` en la LOS (el factor 4π incluye ida y vuelta).

🎯 **Por qué importa (clase B57-C08):** El radar es la única herramienta orbital que mide movimientos del suelo de milímetros a escala regional, pero la fase solo se conoce módulo `2π`. La decisión central: ¿cuándo se puede reconstruir el desplazamiento y cuándo el desenrollado de la fase deja de ser fiable?

📘 **Dónde se aprende** (1 clase): [B57-C08 · Interferometría radar InSAR](../programa/clases/B57/B57-C08-interferometria-radar-insar/CLASE.md).

### Fase mínima

- La fase mínima `Δφ_min = 1/√N_fot`.

💡 **Cómo se explica en la clase [B28-C06](../programa/clases/B28/B28-C06-interferometros-gravitacionales/CLASE.md):**
- Para `h = 10⁻²¹`: `ΔL = 4 × 10⁻¹⁸ m` y `Δφ = 1,417 × 10⁻⁸ rad`, `328` veces la fase mínima.
- *Descripción textual:* la deformación y los parámetros ópticos dan la fase producida; la potencia y el tiempo dan el número de fotones y la fase mínima; su cociente indica si la señal es detectable y de ahí sale `h_min`.
- 🎯 **Por qué importa:** Un detector que mide `10⁻¹⁹ m` necesita muchos fotones y cavidades que multipliquen el efecto. La decisión central: ¿qué fase produce una onda, qué fase mínima permite el ruido de disparo y cómo se mejora la sensibilidad?

📘 **Dónde se aprende** (1 clase): [B28-C06 · Interferómetros gravitacionales](../programa/clases/B28/B28-C06-interferometros-gravitacionales/CLASE.md).

### Fase principal

- La fase principal es la de inyección.

💡 **Cómo se explica en la clase [B30-C18](../programa/clases/B30/B30-C18-tormentas-geomagneticas/CLASE.md):**
- Con la inyección ilustrativa `Q₀ = 15 nT/h`, `τ = 8 h` y fase principal de `T = 6 h`, el mínimo es `−63,32 nT`.
- 🎯 **Por qué importa:** Prever la profundidad y la duración de una tormenta orienta la protección de redes y satélites. La decisión central: ¿qué mínimo alcanza `Dst*` y cuánto tarda en recuperarse?

📘 **Dónde se aprende** (1 clase): [B30-C18 · Tormentas geomagnéticas](../programa/clases/B30/B30-C18-tormentas-geomagneticas/CLASE.md).

### Fase requerida

- La fase requerida es `φ = π − n_t t_T`.

💡 **Cómo se explica en la clase [B76-C10](../programa/clases/B76/B76-C10-encuentro-orbital/CLASE.md):**
- *Descripción textual:* de los radios sale el Hohmann y su tiempo; con el tiempo y el movimiento del objetivo sale la fase requerida; la espera se calcula con la diferencia de movimientos medios y la integración comprueba la llegada.
- 🎯 **Por qué importa:** Si la fase es incorrecta, la nave llega al lugar correcto cuando el objetivo ya pasó. La decisión central: ¿qué ángulo de fase debe haber al inicio y cuánto hay que esperar para lograrlo?

📘 **Dónde se aprende** (1 clase): [B76-C10 · Encuentro orbital](../programa/clases/B76/B76-C10-encuentro-orbital/CLASE.md).

### Fase vertical

- La fase vertical inicial permite despejar la torre y ganar velocidad.

💡 **Cómo se explica en la clase [B77-C12](../programa/clases/B77/B77-C12-perfil-de-ascenso-orbital/CLASE.md):**
- V["fase vertical 10 s"] --> K["gamma0 = 85 grados"]
- *Descripción textual:* una fase vertical, un giro a `85°`, la etapa 1 en giro de gravedad, la separación y la etapa 2 con desvío del empuje que cierra `γ = 0`; al agotarse, la vis-viva da perigeo y apogeo.
- 🎯 **Por qué importa:** La trayectoria de ascenso decide a la vez las pérdidas, las cargas y la órbita alcanzada. La decisión central: ¿qué perfil de inclinación lleva al vehículo a una órbita casi circular y qué cuesta?

📘 **Dónde se aprende** (1 clase): [B77-C12 · Perfil de ascenso orbital](../programa/clases/B77/B77-C12-perfil-de-ascenso-orbital/CLASE.md).

### Fases

- Las fases de ejemplo son: lanzamiento y primeras órbitas, puesta en servicio, operaciones nominales y fin de vida.

💡 **Cómo se explica en la clase [B83-C03](../programa/clases/B83/B83-C03-concepto-de-operaciones-conops/CLASE.md):**
- El CONOPS de ejemplo tiene cuatro fases: lanzamiento y primeras órbitas (7 d), puesta en servicio (30 d), operaciones nominales (3 años) y fin de vida (90 d).
- F["Fases y modos"] --> O["Orbita y estacion"]
- 🎯 **Por qué importa:** Los requisitos de datos, energía y operaciones dependen de cuántas veces al día se puede hablar con el satélite y por cuánto tiempo. La decisión central: ¿cuánto contacto real ofrece la órbita y cómo se reparte en las fases de la misión?

📘 **Dónde se aprende** (1 clase): [B83-C03 · Concepto de operaciones CONOPS](../programa/clases/B83/B83-C03-concepto-de-operaciones-conops/CLASE.md).

### Fases de Venus

- Las fases de Venus son los cambios de la porción iluminada de Venus vista desde la Tierra.

🎯 **Por qué importa (clase B02-C13):** Un instrumento nuevo da datos nuevos, pero los datos nuevos no se interpretan solos. La pregunta motivadora es: ¿qué podía concluir Galileo de lo que veía, y qué le faltaba para convencer a quienes no creían?

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

📘 **Dónde se aprende** (3 clases): [B104-C04 · Acondicionamiento físico general](../programa/clases/B104/B104-C04-acondicionamiento-fisico-general/CLASE.md); [B107-C01 · Entrenamiento cardiorrespiratorio y de resistencia de astronautas](../programa/clases/B107/B107-C01-entrenamiento-cardiorrespiratorio-y-de-resistencia-de-astronautas/CLASE.md); [B117-C01 · Primeros auxilios y procedimientos básicos en entorno espacial](../programa/clases/B117/B117-C01-primeros-auxilios-y-procedimientos-basicos-en-entorno-espacial/CLASE.md).

### Fatiga de alarmas

- La fatiga de alarmas es la desensibilización de quien recibe demasiadas alarmas poco útiles.

🎯 **Por qué importa (clase B116-C05):** Una alarma que suena por cada artefacto enseña a ignorarla. Una que espera demasiado llega tarde.

📘 **Dónde se aprende** (1 clase): [B116-C05 · Alertas de salud y umbrales de monitorización](../programa/clases/B116/B116-C05-alertas-de-salud-y-umbrales-de-monitorizacion/CLASE.md).

### Fatiga de alertas

- La fatiga de alertas es la pérdida de atención ante alertas repetidas que no se cumplen.

🎯 **Por qué importa (clase B57-C34):** Un detector excelente puede producir una mayoría de falsas alarmas si el evento es raro, y las alertas repetidas y falsas se ignoran. La decisión central: ¿qué umbral y qué comunicación equilibran el costo de omitir y el de alarmar en falso, y quién decide?

📘 **Dónde se aprende** (1 clase): [B57-C34 · Alertas tempranas y ética en el monitoreo de desastres](../programa/clases/B57/B57-C34-alertas-tempranas-y-etica-en-el-monitoreo-de-desastres/CLASE.md).

### Fayalita

- Un mineral es un sólido cristalino natural de composición química definida: el olivino `(Mg,Fe)₂SiO₄` es una serie entre la forsterita `Mg₂SiO₄` y la fayalita `Fe₂SiO₄`; el piroxeno más sencillo es `MgSiO₃`; la calcita es `CaCO₃`.
- La forsterita (Mg₂SiO₄) y la fayalita (Fe₂SiO₄) son los extremos del olivino; la enstatita (MgSiO₃) es un piroxeno.

💡 **Cómo se explica en la clase [B06-C19](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md):**
- Con los pesos atómicos de la NIST (C03): `H₂O = 18,0153`, `CO₂ = 44,0094`, `NH₃ = 17,0308`, forsterita `Mg₂SiO₄ = 2 × 24,3055 + 28,085 + 4 × 15,9994 = 140,6936`, fayalita `Fe₂SiO₄ = 203,7726`, piroxeno `MgSiO₃ = 100,3887` y calcita `CaCO₃ = 100,0868 g/mol`.
- Un olivino con 90 % de forsterita y 10 % de fayalita (Fo₉₀) tiene una masa formular que es el promedio ponderado de las dos: `0,9 × 140,6936 + 0,1 × 203,7726 = 147,0015 g/mol`.
- 🎯 **Por qué importa:** Los estudios con el telescopio James Webb muestran que las nubes densas del medio interestelar tienen granos de polvo cubiertos de hielos con una variedad de moléculas, y que esos hielos contienen entre el 2 y el 19 % del carbono, oxígeno, nitrógeno y azufre disponibles (S1, resumen).

📘 **Dónde se aprende** (2 clases): [B06-C19 · Química de hielos y minerales](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md); [B55-C12 · Geoquímica de meteoritos](../programa/clases/B55/B55-C12-geoquimica-de-meteoritos/CLASE.md).

### FECF

- El FECF es un CRC de 16 bits con polinomio `X¹⁶ + X¹² + X⁵ + 1` y registro inicial a unos.

💡 **Cómo se explica en la clase [B94-C03](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md):**
- El CRC se calcula sobre toda la trama salvo el propio FECF, con registro inicial a unos.
- Al recalcularlo sobre trama + FECF el resultado debe ser cero, y así lo comprueba el receptor.
- 🎯 **Por qué importa:** Un receptor que recibe un flujo de octetos con pérdidas necesita saber qué trama es, si llegó íntegra, si faltan tramas y dónde retomar los paquetes. La decisión central: ¿qué campos de la trama permiten detectar errores y pérdidas y resincronizar sin retransmitir?

📘 **Dónde se aprende** (1 clase): [B94-C03 · Tramas de transferencia de telemetría y telecomando](../programa/clases/B94/B94-C03-tramas-de-transferencia-de-telemetria-y-telecomando/CLASE.md).

### FEFO

- FIFO emite el lote recibido antes; FEFO emite el que caduca antes.

💡 **Cómo se explica en la clase [B100-C01](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md):**
- Caducan `324 u` (15,6 % de lo recibido) en FIFO y `164 u` (7,9 %) en FEFO: 160 u menos, un 49 % menos.
- Para el lote L05 en FEFO hay 26 emisiones, 102 u, entre los días 199 y 262; por consumidor: C1 = 21, C2 = 21, C3 = 23, C4 = 15, C5 = 22 (suma 102).
- ⚠️ **Error frecuente:** Creer que FEFO atiende más demanda. Se corrige con 8.2: atiende la misma y caduca menos
- 🎯 **Por qué importa:** Un inventario que solo sabe «cuántas unidades hay» no puede decir de qué lote vienen, cuándo caducan ni dónde se usaron. La decisión central: ¿qué registro mínimo hace falta para emitir primero lo que caduca antes y para encontrar, si un lote resulta defectuoso, adónde fue?

📘 **Dónde se aprende** (1 clase): [B100-C01 · Gestión de inventario de materias primas y piezas](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md).

### Fenómeno de Gibbs

- El fenómeno de Gibbs es la oscilación persistente cerca de un salto.

🎯 **Por qué importa (clase B11-C16):** Cuando la solución es suave y periódica —una señal a lo largo de una órbita, un perfil de temperatura alrededor de un vehículo que gira, el campo en una caja periódica—, un método espectral logra con 24 puntos lo que unas diferencias finitas lograrían con millones.

📘 **Dónde se aprende** (1 clase): [B11-C16 · Métodos espectrales iniciales](../programa/clases/B11/B11-C16-metodos-espectrales-iniciales/CLASE.md).

### Fenómeno de Runge

- El fenómeno de Runge es la oscilación creciente en los extremos al subir el grado con nodos equiespaciados.

🎯 **Por qué importa (clase B11-C18):** Si una nave debe saber dónde está un cuerpo en un instante que no figura en la tabla, interpola. Si interpola con un grado equivocado o fuera del rango, el error puede pasar de metros a miles de kilómetros sin que el programa avise.

📘 **Dónde se aprende** (1 clase): [B11-C18 · Interpolación y extrapolación](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md).

### FER

- BER: tasa de error de bit. FER: tasa de error de trama, `1 − (1 − p)^n`.

💡 **Cómo se explica en la clase [B90-C16](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md):**
- Paso 2 · FER. `1 − (1 − 10⁻⁴)^1040 = 1 − e^{−0,104} = 0,0988`.
- Con `BER = 10⁻⁴`, la FER es 0,0988 y cada trama se reintenta en promedio 1,11 veces; con `BER = 10⁻³`, FER 0,647 y 2,83 envíos.
- 🎯 **Por qué importa:** Cada subsistema puede pasar sus pruebas y la cadena fallar: un formato de trama distinto, un retraso mayor que el tiempo de espera, un error de bit no detectado. La decisión central: ¿qué errores detecta la cadena, con qué frecuencia reintenta y cuánto tarda cada acuse?

📘 **Dónde se aprende** (1 clase): [B90-C16 · Pruebas de extremo a extremo](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md).

### Fermi–Dirac

- La distribución de Bose–Einstein, la de Fermi–Dirac y la de Maxwell–Boltzmann.

🎯 **Por qué importa (clase B31-C06):** La radiación de las estrellas y la presión de degeneración de los remanentes estelares dependen de estas estadísticas. La decisión central: ¿qué distribución usar y qué constantes se derivan?

📘 **Dónde se aprende** (1 clase): [B31-C06 · Estadísticas cuánticas](../programa/clases/B31/B31-C06-estadisticas-cuanticas/CLASE.md).

### Fermión

- Un fermión obedece el principio de exclusión.

🎯 **Por qué importa (clase B27-C01):** Una estrella sin fusión no se desploma porque los electrones (o neutrones) no pueden apretarse más allá de lo que permite el principio de exclusión, aunque la temperatura sea cero. La decisión central: dada la densidad de un gas degenerado, ¿cuánto vale el momento de Fermi, la presión y cuál de los dos límites aplica?

📘 **Dónde se aprende** (1 clase): [B27-C01 · Presión de degeneración](../programa/clases/B27/B27-C01-presion-de-degeneracion/CLASE.md).

### FFT

- La FFT es una familia de algoritmos que calculan la DFT en `O(N log N)`; la versión más usada se atribuye a Cooley y Tukey, como señala la documentación de NumPy (S1).
- La FFT da el espectro.

💡 **Cómo se explica en la clase [B15-C05](../programa/clases/B15/B15-C05-transformada-rapida-de-fourier/CLASE.md):**
- La FFT parte la serie en muestras pares e impares, calcula la DFT de cada mitad (que es más pequeña) y las combina con unos pocos productos.
- Su límite: al ordenar, el orden final es único pero depende de las comparaciones; en la FFT el resultado es exactamente el de la DFT, sin aproximación.
- ⚠️ **Error frecuente:** Aplicar una FFT de base 2 a un `N` que no lo es. La implementación propia debe fallar o rellenar; se declara.
- 🎯 **Por qué importa:** Una curva de luz de 27 días con cadencia de 2 minutos tiene 19 440 muestras. La suma directa de la DFT necesita unos 378 millones de multiplicaciones complejas; una imagen de 1024 × 1024 necesitaría muchísimas más.

📘 **Dónde se aprende** (2 clases): [B15-C05 · Transformada rápida de Fourier](../programa/clases/B15/B15-C05-transformada-rapida-de-fourier/CLASE.md); [B46-C10 · Radioastronomía mediante SDR](../programa/clases/B46/B46-C10-radioastronomia-mediante-sdr/CLASE.md).

### FFT bidimensional

- La FFT bidimensional de canal × tiempo.

🎯 **Por qué importa (clase B51-C11):** Declarar una detección sin umbral estadístico es un riesgo de falsos positivos. La decisión central: ¿qué pico es una señal y cuál es ruido, y con qué precisión se estiman retardo y tasa?

📘 **Dónde se aprende** (1 clase): [B51-C11 · Búsqueda de franjas VLBI: ajuste de retardo y tasa](../programa/clases/B51/B51-C11-busqueda-de-franjas-vlbi-ajuste-de-retardo-y-tasa/CLASE.md).

### Fiabilidad

- La fiabilidad `R(t)` es la probabilidad de funcionar hasta `t`.
- La fiabilidad `r` es la proporción de la varianza que es real.
- La fiabilidad `r` es la probabilidad de que una fuente informe correctamente.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B33-C05](../programa/clases/B33/B33-C05-comunicacion-de-riesgo-y-alertas-de-clima-espacial/CLASE.md):**
- *Descripción textual:* el cociente costo/pérdida fija el umbral de decisión, que da el gasto; el Brier y la fiabilidad miden la calidad de las probabilidades.
- 🎯 **Por qué importa:** La mejor comunicación de riesgo da probabilidades calibradas y deja decidir al usuario. La decisión central: ¿cuándo conviene proteger y cuán fiables son las probabilidades?

📖 **Explicado a fondo:** [Redundancia y fiabilidad](esencial/ampliacion-n-z.md#redundancia-y-fiabilidad) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (7 clases): [B33-C05 · Comunicación de riesgo y alertas de clima espacial](../programa/clases/B33/B33-C05-comunicacion-de-riesgo-y-alertas-de-clima-espacial/CLASE.md); [B59-C18 · Fiabilidad de equipos mineros](../programa/clases/B59/B59-C18-fiabilidad-de-equipos-mineros/CLASE.md); [B88-C01 · Arquitectura de computador de vuelo](../programa/clases/B88/B88-C01-arquitectura-de-computador-de-vuelo/CLASE.md); [B106-C18 · Fiabilidad y redundancia](../programa/clases/B106/B106-C18-fiabilidad-y-redundancia/CLASE.md); [B107-C04 · Evaluación del rendimiento físico y cognitivo de tripulantes](../programa/clases/B107/B107-C04-evaluacion-del-rendimiento-fisico-y-cognitivo-de-tripulantes/CLASE.md); [B118-C11 · Diseño para mitigación de desechos](../programa/clases/B118/B118-C11-diseno-para-mitigacion-de-desechos/CLASE.md) y 1 más.

### Fibra neutra

- La fibra neutra es la línea que no se alarga al doblar.

🎯 **Por qué importa (clase B95-C04):** Un enlace con la Tierra necesita una antena, y una antena que no se despliega deja el satélite mudo. La decisión central: ¿qué longitud necesita la antena, cómo se pliega sin dañarla y qué riesgo añade el mecanismo?

📘 **Dónde se aprende** (1 clase): [B95-C04 · Antenas desplegables para satélites pequeños](../programa/clases/B95/B95-C04-antenas-desplegables-para-satelites-pequenos/CLASE.md).

### Ficha de procedencia

- La ficha de procedencia guarda por cada cifra: valor, unidad, fuente, fecha, estado e incertidumbre.

🎯 **Por qué importa (clase B130-C01):** Comunicar con imágenes exige mantener la fuente y la incertidumbre; la clase de comunicación general no entra en cómo se audita una pieza visual. La decisión central: ¿qué debe llevar cada cifra de una infografía para que otra persona pueda verificarla, y qué diseño la deforma?

📘 **Dónde se aprende** (1 clase): [B130-C01 · Infografías con fuentes verificables](../programa/clases/B130/B130-C01-infografias-con-fuentes-verificables/CLASE.md).

### Fidelidad

- La fidelidad `q` es la probabilidad de copiar bien una letra.
- La fidelidad de un propagador es cuánto se parece su modelo de fuerzas y su integración a la realidad (o a una referencia).
- La fidelidad es cuánto se parece el simulador al sistema real.

💡 **Cómo se explica en la clase [B56-C03](../programa/clases/B56/B56-C03-origen-de-moleculas-autorreplicantes/CLASE.md):**
- En un mundo real la fidelidad no es una constante.
- Una molécula que se copia a sí misma, como el ARN, necesita copiar con alta fidelidad para no degradarse.
- 🎯 **Por qué importa:** Un replicador que copia mal pierde su información; uno que copia bien necesita una maquinaria que, sin vida previa, aún no existe. Esa tensión limita el tamaño de los primeros genomas.

📘 **Dónde se aprende** (3 clases): [B56-C03 · Origen de moléculas autorreplicantes](../programa/clases/B56/B56-C03-origen-de-moleculas-autorreplicantes/CLASE.md); [B72-C20 · Comparación de propagadores de fidelidad distinta](../programa/clases/B72/B72-C20-comparacion-de-propagadores-de-fidelidad-distinta/CLASE.md); [B104-C09 · Entrenamiento en simuladores](../programa/clases/B104/B104-C09-entrenamiento-en-simuladores/CLASE.md).

### FIFO

- La clase de servicio del protocolo de paquetes es `bulk`, `normal` o `expedited`, con prioridad 0, 1 y 2. FIFO sirve por orden de llegada.
- Un lote es la unidad de trazabilidad. FIFO emite el lote recibido antes;

💡 **Cómo se explica en la clase [B94-C05](../programa/clases/B94/B94-C05-calidad-de-servicio-y-prioridades-en-redes-espaciales/CLASE.md):**
- FIFO reparte el daño por igual y ni siquiera protege lo urgente.
- S --> P["politica: FIFO,<br/>prioridad estricta,<br/>reparto ponderado"]
- 🎯 **Por qué importa:** Si la demanda supera a la capacidad, alguien espera. La decisión central: ¿qué política de cola garantiza lo urgente sin dejar sin servicio a las demás clases, y a qué coste?

📘 **Dónde se aprende** (2 clases): [B94-C05 · Calidad de servicio y prioridades en redes espaciales](../programa/clases/B94/B94-C05-calidad-de-servicio-y-prioridades-en-redes-espaciales/CLASE.md); [B100-C01 · Gestión de inventario de materias primas y piezas](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md).

### Figura

- Una figura (`Figure`) es el lienzo completo; los ejes (`Axes`) son la región donde se dibujan los datos, con sus dos ejes de coordenadas (`Axis`) que fijan escala, límites y marcas (S2).
- Una figura es un gráfico o imagen; una tabla, una disposición de valores en filas y columnas.

💡 **Cómo se explica en la clase [B07-C10](../programa/clases/B07/B07-C10-graficos-bidimensionales-iniciales/CLASE.md):**
- En escala lineal, Neptuno (a ≈ 4515, T ≈ 60 189) domina el gráfico y Mercurio, Venus, la Tierra y Marte quedan amontonados cerca del origen (panel izquierdo de la figura).
- *Descripción textual:* los datos (dos arreglos) se dibujan sobre unos ejes que llevan escala, etiquetas y unidades; los ejes forman parte de una figura con título y leyenda, que se guarda como imagen acompañada de una descripción en texto.
- 🎯 **Por qué importa:** Un gráfico es una afirmación: dice «mira esta relación». Un gráfico sin unidades, con una escala que esconde la mitad de los datos o sin leyenda puede inducir a error aunque los números sean correctos.

📘 **Dónde se aprende** (2 clases): [B07-C10 · Gráficos bidimensionales iniciales](../programa/clases/B07/B07-C10-graficos-bidimensionales-iniciales/CLASE.md); [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md).

### Figura de mérito G/T

- La figura de mérito `G/T` mide la sensibilidad de la estación.

🎯 **Por qué importa (clase B91-C08):** Un enlace a distancias de unidades astronómicas pierde unos 280 dB: solo se cierra con una estación enorme y de ruido muy bajo. La decisión central: ¿qué antena de estación (una de 70 m, una de 34 m o un arreglo de varias) permite la velocidad de datos pedida, y cuánto cuesta un error de apuntamiento?

📘 **Dónde se aprende** (1 clase): [B91-C08 · Antenas de gran apertura y estaciones de espacio profundo](../programa/clases/B91/B91-C08-antenas-de-gran-apertura-y-estaciones-de-espacio-profundo/CLASE.md).

### Figura de mérito térmica

- La figura de mérito térmica `k/α` indica cuánto se deforma por un flujo de calor dado.

🎯 **Por qué importa (clase B43-C03):** Un buen material no es el más duro ni el más estable: es el que deja el menor error de forma para una masa y un presupuesto. La decisión central: ¿qué material y qué espesor mantienen la flexión y la deriva térmica por debajo de la tolerancia?

📘 **Dónde se aprende** (1 clase): [B43-C03 · Materiales para espejos](../programa/clases/B43/B43-C03-materiales-para-espejos/CLASE.md).

### Figura de ruido

- La figura de ruido `NF = 10 log₁₀ F`.

💡 **Cómo se explica en la clase [B89-C07](../programa/clases/B89/B89-C07-figura-de-ruido-de-receptor/CLASE.md):**
- La figura de ruido equivalente es `0,626`, `1,620` y `9,00 dB`.
- 🎯 **Por qué importa:** La primera etapa de una cadena receptora decide casi todo el ruido: un amplificador de bajo ruido bien colocado vale muchos decibelios de `G/T`. La decisión central: ¿qué orden y qué componentes dan la menor temperatura de sistema y el mayor `G/T`?

📘 **Dónde se aprende** (1 clase): [B89-C07 · Figura de ruido de receptor](../programa/clases/B89/B89-C07-figura-de-ruido-de-receptor/CLASE.md).

### Fija

- Una función fija no depende del número de tripulantes; una lineal crece con él; una por pares crece por cada dos tripulantes; una logística crece con tripulantes por días.

🎯 **Por qué importa (clase B109-C05):** Si el primer módulo no admite ampliación, crecer obliga a desechar lo construido. La decisión central: ¿qué funciones se duplican con la tripulación, cuáles no, y cómo se añaden módulos sin rediseñar?

📘 **Dónde se aprende** (1 clase): [B109-C05 · Crecimiento modular y escalabilidad de asentamientos](../programa/clases/B109/B109-C05-crecimiento-modular-y-escalabilidad-de-asentamientos/CLASE.md).

### Fijar

- `uv run` ejecuta un comando dentro del entorno del proyecto, comprobando antes que el bloqueo y el entorno estén al día (S4). Fijar una versión es escribirla con `==`.
- La huella del entorno es el registro de las versiones de Python, plataforma y bibliotecas con que se ejecutó un análisis. Fijar una versión es exigir exactamente esa.

💡 **Cómo se explica en la clase [B14-C12](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md):**
- Para fijar el sistema completo se usan contenedores (C17), con sus propios límites.
- 🎯 **Por qué importa:** Tu análisis dio un período de 5553,624562 s en 2026. Un colega lo ejecuta con otra versión de SciPy y obtiene un cierre distinto; otro usa Python más antiguo y falla al importar. «En mi máquina funciona» no es un resultado científico.

📘 **Dónde se aprende** (2 clases): [B07-C13 · Entornos y dependencias con uv](../programa/clases/B07/B07-C13-entornos-y-dependencias-con-uv/CLASE.md); [B14-C12 · Ejecución reproducible con uv](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md).

### Fila

- Una fila se llama periodo; una columna, grupo.
- Una tabla es un conjunto de columnas del mismo largo; cada fila describe un objeto y cada columna una propiedad.

💡 **Cómo se explica en la clase [B14-C05](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md):**
- Ninguna fila corresponde a una estrella real; el desplazamiento se fijó de antemano para que podamos comprobar el cruce.
- 🎯 **Por qué importa:** Un catálogo de estrellas no es una lista de números: cada columna tiene una unidad, algunas filas no tienen paralaje, y la tabla viene de un instrumento, una época y una versión. Si pierdes eso al copiar los datos a un arreglo, pierdes la mitad del significado.

📘 **Dónde se aprende** (2 clases): [B06-C02 · Tabla periódica y abundancias cósmicas](../programa/clases/B06/B06-C02-tabla-periodica-y-abundancias-cosmicas/CLASE.md); [B14-C05 · Tablas astronómicas y catálogos](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md).

### Filamento

- El filamento o la prominencia.

💡 **Cómo se explica en la clase [B34-C08](../programa/clases/B34/B34-C08-erupciones-de-filamentos-y-prominencias/CLASE.md):**
- A `100 km/s` la cinética es el 61 % de la potencial: lejos de la escape, pero para elevar el filamento basta con mover el equilibrio.
- 🎯 **Por qué importa:** Saber a qué altura el campo ya no sostiene al filamento sirve para anticipar erupciones. La decisión central: ¿a qué altura el decaimiento del campo supera el umbral?

📘 **Dónde se aprende** (1 clase): [B34-C08 · Erupciones de filamentos y prominencias](../programa/clases/B34/B34-C08-erupciones-de-filamentos-y-prominencias/CLASE.md).

### Filosofía de modelos

- Unidad de vuelo (FM): la que vuela. Filosofía de modelos: conjunto de modelos que se construye y prueba.

🎯 **Por qué importa (clase B90-C24):** Un modelo de ingeniería cuesta dinero y calendario; un defecto que llega a órbita cuesta la misión. La decisión central: ¿vale la pena construir un modelo previo, o conviene el protovuelo o solo la unidad de vuelo, dado el valor de lo que se arriesga?

📘 **Dónde se aprende** (1 clase): [B90-C24 · Prototipado y modelos de ingeniería de subconjuntos](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md).

### Filtro acoplado

- El filtro acoplado correlaciona los datos con la plantilla.

💡 **Cómo se explica en la clase [B28-C21](../programa/clases/B28/B28-C21-formas-de-onda-gravitacionales-y-filtro-acoplado/CLASE.md):**
- *Descripción textual:* la masa de chirrido da la frecuencia y la fase, de ahí la forma de onda; el filtro acoplado la correlaciona con los datos y el desajuste con plantillas vecinas fija el banco.
- 🎯 **Por qué importa:** Una plantilla ligeramente errada pierde mucha señal-ruido, porque la fase acumula miles de ciclos. Entender cuánto determina cuántas plantillas hacen falta.

📘 **Dónde se aprende** (1 clase): [B28-C21 · Formas de onda gravitacionales y filtro acoplado](../programa/clases/B28/B28-C21-formas-de-onda-gravitacionales-y-filtro-acoplado/CLASE.md).

### Filtro adaptado

- El filtro adaptado (*matched filter*) es la correlación de la imagen con la propia PSF normalizada `p` (suma 1): maximiza la SNR de una fuente puntual en ruido blanco.
- El filtro adaptado correlaciona el eco con una copia del pulso.

💡 **Cómo se explica en la clase [B15-C12](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md):**
- Un pixel aislado daría `F p₀/σ` con `p₀ = 0,0707` (el valor máximo de la PSF normalizada): el filtro adaptado gana un factor `√(Σp²)/p₀ = 0,1881/0,0707 = 2,66`.
- Buscar una estrella débil es como buscar una nota de flauta en una sala ruidosa: sabes cómo suena (la PSF), así que escuchas selectivamente esa forma (filtro adaptado) en lugar de cada píxel por separado.
- 🎯 **Por qué importa:** Un catálogo de fuentes es el producto básico de una imagen astronómica, y de él salen cuentas, colores y candidatos a objetos nuevos. Si el umbral es bajo, el catálogo se llena de ruido; si es alto, se pierden las fuentes débiles.

📘 **Dónde se aprende** (2 clases): [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B57-C07 · Sistemas radar SAR](../programa/clases/B57/B57-C07-sistemas-radar-sar/CLASE.md).

### Filtro antialias

- El filtro antialias es un filtro aplicado antes de muestrear que elimina lo que está por encima de `f_N`.
- Aliasing: aparición de una frecuencia superior a Nyquist como una menor. Filtro antialias: filtro pasa-bajas antes del muestreo.

💡 **Cómo se explica en la clase [B15-C02](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md):**
- La segunda: filtrar antes de muestrear con un filtro antialias analógico u óptico.
- 🎯 **Por qué importa:** Un detector que mide una estrella cada 2 minutos no puede ver directamente algo que oscila cada 3 minutos con precisión, pero tampoco lo ignora: ese movimiento rápido queda registrado como una oscilación lenta y falsa. Si no sabes que eso ocurre, publicarías un periodo que no existe.

📘 **Dónde se aprende** (2 clases): [B15-C02 · Muestreo y aliasing](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md); [B90-C23 · Instrumentación y adquisición de datos en ensayos](../programa/clases/B90/B90-C23-instrumentacion-y-adquisicion-de-datos-en-ensayos/CLASE.md).

### Filtro de alta eficiencia

- Clase de limpieza: número `N` que fija el límite de partículas por tamaño. Filtro de alta eficiencia: filtro que retiene la fracción `η` de las partículas del aire que lo cruza.

🎯 **Por qué importa (clase B90-C02):** Una partícula sobre una óptica, un sello o un contacto puede degradar una misión; las partículas llegan con el aire, la ropa y las herramientas. La decisión central: ¿qué clase de sala puede sostener esta actividad con este número de personas, y cuánto hay que esperar tras una perturbación?

📘 **Dónde se aprende** (1 clase): [B90-C02 · Buenas prácticas de sala limpia](../programa/clases/B90/B90-C02-buenas-practicas-de-sala-limpia/CLASE.md).

### Filtro de apsis

- El filtro de apsis compara las cáscaras `[r_p, r_a]`.

💡 **Cómo se explica en la clase [B118-C18](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md):**
- Límite: el filtro de apsis es el más simple; otros filtros usan planos orbitales y tiempos, y el derecho tiene excepciones que la clase no recorre.
- Descripción larga: el filtro de apsis descarta más de la mitad de los pares y la verificación muestra que no pierde ninguno; con muchas órbitas casi circulares a la misma altitud quedan más pares por evaluar.
- 🎯 **Por qué importa:** Con decenas de miles de objetos, comparar todos los pares es costoso; un buen cribado descarta de entrada los pares imposibles sin perder ninguno posible. Y cuando algo sale mal, los tratados determinan responsabilidad y jurisdicción.

📘 **Dónde se aprende** (1 clase): [B118-C18 · Gestión del tráfico espacial](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md).

### Filtro de Butterworth

- El filtro de Butterworth es el de respuesta plana en la banda.

🎯 **Por qué importa (clase B49-C10):** Más orden rechaza más, pero también pierde más señal. La decisión central: ¿qué orden y qué ancho de banda dan el rechazo de imagen necesario con una pérdida aceptable?

📘 **Dónde se aprende** (1 clase): [B49-C10 · Filtros de radiofrecuencia pasabanda y rechazo de banda imagen](../programa/clases/B49/B49-C10-filtros-de-radiofrecuencia-pasabanda-y-rechazo-de-banda-imagen/CLASE.md).

### Filtro de Kalman escalar

- El filtro de Kalman escalar estima `s` con el modelo `s_k = s_(k−1) + w`, `z_k = s_k + v`.

🎯 **Por qué importa (clase B102-C03):** Un rover que cree haber avanzado 315 m cuando solo avanzó 270 m llega al sitio equivocado. La decisión central: ¿cómo se estima el patinaje en línea, con qué incertidumbre y cuánto mejora la distancia corregida?

📘 **Dónde se aprende** (1 clase): [B102-C03 · Deslizamiento y estimación de patinaje](../programa/clases/B102/B102-C03-deslizamiento-y-estimacion-de-patinaje/CLASE.md).

### Filtro de Kalman extendido

- El filtro de Kalman extendido linealiza la medición no lineal `r = |p − p_b|` con la matriz `H = [(p − p_b)/r, 0, 0, 0, 0]`.

🎯 **Por qué importa (clase B80-C04):** B74-C08..C10 dan los filtros, pero ninguna clase los aplica a la unión de una IMU con una fuente externa. La decisión central: ¿en qué nivel se funden la inercia y la medición externa, y qué se pierde o se gana al elegirlo?

📘 **Dónde se aprende** (1 clase): [B80-C04 · Fusión inercial con mediciones externas (acoplamiento débil y fuerte)](../programa/clases/B80/B80-C04-fusion-inercial-con-mediciones-externas-acoplamiento-debil-y-fuerte/CLASE.md).

### Filtro de Lee

- El filtro de Lee mezcla la media local y el pixel según el contraste local.

💡 **Cómo se explica en la clase [B69-C03](../programa/clases/B69/B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md):**
- I --> LEE["filtro de Lee: media local + pixel"]
- Por filtro de Lee: adaptativo, conserva bordes mejor.
- 🎯 **Por qué importa:** Un valor de píxel aislado de una imagen SAR no mide la reflectividad de la superficie: es una muestra de una distribución muy ancha. La decisión central: ¿cuánto hay que promediar o filtrar para estimar la reflectividad con una incertidumbre dada, y a qué precio en resolución?

📘 **Dónde se aprende** (1 clase): [B69-C03 · Ruido speckle y filtrado en imágenes SAR](../programa/clases/B69/B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md).

### Filtro de menor retardo

- Jitter: variación aleatoria del retardo. Filtro de menor retardo: elige el intercambio más rápido.

💡 **Cómo se explica en la clase [B48-C10](../programa/clases/B48/B48-C10-redes-de-instrumentos/CLASE.md):**
- El filtro de menor retardo la baja a 0,533 ms pero deja el sesgo.
- 🎯 **Por qué importa:** Si los relojes difieren, los datos de distintos instrumentos no se pueden correlacionar. La decisión central: ¿cómo se reduce el error de un desfase estimado cuando la red es asimétrica?

📘 **Dónde se aprende** (1 clase): [B48-C10 · Redes de instrumentos](../programa/clases/B48/B48-C10-redes-de-instrumentos/CLASE.md).

### Filtro de ocular

- Un filtro de ocular se enrosca atrás: la AAS dice que es peligroso y debe desecharse (S3).

🎯 **Por qué importa (clase B08-C16):** Una persona que mira un eclipse parcial con gafas falsas, o enfoca el Sol con un telescopio sin filtro frontal, puede quedar con una lesión permanente. La pregunta motivadora: ¿cómo observo el Sol sin dañarme y sin dañar a otros?

📘 **Dónde se aprende** (1 clase): [B08-C16 · Observación solar con filtros certificados](../programa/clases/B08/B08-C16-observacion-solar-con-filtros-certificados/CLASE.md).

### Filtro de significancia

- El filtro de significancia es la selección de los resultados con `p < α`: entre ellos, el efecto estimado está sesgado hacia valores grandes.

🎯 **Por qué importa (clase B12-C26):** En medicina espacial, en estudios con tripulaciones o en misiones con pocas unidades, los tamaños de muestra son pequeños por necesidad. Con ellos, la mayoría de los efectos reales no se detectan, y los que se detectan suelen estar inflados.

📘 **Dónde se aprende** (1 clase): [B12-C26 · Sesgos y potencia estadística en poblaciones pequeñas](../programa/clases/B12/B12-C26-sesgos-y-potencia-estadistica-en-poblaciones-pequenas/CLASE.md).

### Filtro de suelo

- El filtro de suelo clasifica los puntos que están en el terreno.

🎯 **Por qué importa (clase B57-C30):** Un modelo de terreno malo hace que las pendientes y las alturas de los árboles salgan mal. La decisión central: ¿cómo se separa el suelo del resto con la menor contaminación y qué densidad de puntos hace falta?

📘 **Dónde se aprende** (1 clase): [B57-C30 · Nubes de puntos tridimensionales](../programa/clases/B57/B57-C30-nubes-de-puntos-tridimensionales/CLASE.md).

### Filtro de Wiener

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B42-C19):** Deconvolucionar recupera detalle bajo el límite de difracción pero amplifica el ruido. La decisión central: ¿qué método usar y qué se gana y se pierde con cada uno?

📘 **Dónde se aprende** (1 clase): [B42-C19 · Reconstrucción de imágenes](../programa/clases/B42/B42-C19-reconstruccion-de-imagenes/CLASE.md).

### Filtro digital

- Un filtro digital transforma una serie `x[n]` en otra `y[n]`.

💡 **Cómo se explica en la clase [B15-C07](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md):**
- Su límite: una criba separa objetos en dos montones; un filtro digital atenúa gradualmente y también retrasa o distorsiona la fase.
- 🎯 **Por qué importa:** Una curva de luz tiene una modulación lenta de la estrella (manchas que rotan) de 2000 partes por millón y, escondido en ella, el paso de un planeta que reduce el brillo 1000 ppm durante tres horas. Para ver el tránsito hay que quitar la modulación; pero si el filtro es demasiado agresivo, también se come parte del tránsito.

📘 **Dónde se aprende** (1 clase): [B15-C07 · Filtrado digital](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md).

### Filtro en la apertura

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B43-C19):** La seguridad empieza por saber cuán grande es el riesgo. La decisión central: ¿cuánta potencia y qué temperatura aparecen en el foco, cómo se balancea la montura y cuánto polvo es aceptable?

📘 **Dónde se aprende** (1 clase): [B43-C19 · Seguridad y mantenimiento](../programa/clases/B43/B43-C19-seguridad-y-mantenimiento/CLASE.md).

### Filtro inverso

- El filtro inverso divide la DFT de `d` por `Ĥ`.

💡 **Cómo se explica en la clase [B15-C11](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md):**
- I -->|"filtro inverso"| E["Ruido amplificado<br/>(inutilizable)"]
- *Descripción textual:* el objeto se convoluciona con la PSF y se le añade ruido; invertir con el filtro inverso amplifica el ruido hasta inutilizar la imagen, mientras que el método iterativo de Richardson–Lucy, detenido a tiempo, produce una estimación más nítida.
- ⚠️ **Error frecuente:** Aplicar el filtro inverso a datos con ruido. Se corrige con los ejercicios 5 y 6.
- 🎯 **Por qué importa:** Un telescopio con un defecto de enfoque convierte cada estrella en una mancha. Dos estrellas cercanas pueden fundirse en una sola; el brillo de una galaxia, repartirse sobre sus vecinas.

📘 **Dónde se aprende** (2 clases): [B15-C11 · Deconvolución y enfoque](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md); [B42-C19 · Reconstrucción de imágenes](../programa/clases/B42/B42-C19-reconstruccion-de-imagenes/CLASE.md).

### Filtro pasa-altos

- El filtro pasa-altos de primer orden `τ dw_p/dt = −w_p + τ dw/dt` describe el canal.
- Un filtro pasa-altos quita las variaciones lentas.

🎯 **Por qué importa (clase B37-C13):** El análisis sísmico depende de cómo se prepara la serie. La decisión central: ¿qué hace el muestreo, los huecos y el filtro con las frecuencias y amplitudes recuperadas?

📘 **Dónde se aprende** (2 clases): [B37-C13 · Series fotométricas de Kepler, TESS y PLATO para asterosismología](../programa/clases/B37/B37-C13-series-fotometricas-de-kepler-tess-y-plato-para-asterosismologia/CLASE.md); [B105-C04 · Sistema vestibular](../programa/clases/B105/B105-C04-sistema-vestibular/CLASE.md).

### Filtro solar frontal

- Un filtro solar frontal va montado sobre la apertura de telescopios, binoculares o cámaras.

🎯 **Por qué importa (clase B08-C16):** Una persona que mira un eclipse parcial con gafas falsas, o enfoca el Sol con un telescopio sin filtro frontal, puede quedar con una lesión permanente. La pregunta motivadora: ¿cómo observo el Sol sin dañarme y sin dañar a otros?

📘 **Dónde se aprende** (1 clase): [B08-C16 · Observación solar con filtros certificados](../programa/clases/B08/B08-C16-observacion-solar-con-filtros-certificados/CLASE.md).

### Financiamiento necesario

- La caja mínima es el punto más bajo de esa suma y fija el financiamiento necesario.

💡 **Cómo se explica en la clase [B126-C03](../programa/clases/B126/B126-C03-proyeccion-de-flujos-de-caja-de-un-proyecto-espacial/CLASE.md):**
- *Descripción textual:* los ingresos y costos dan el flujo neto de cada año; su suma corrida es la caja, cuyo mínimo es el financiamiento necesario; se repite con escenarios y se verifica con una suma directa.
- 🎯 **Por qué importa:** [B124-C05](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) estima costos sin flujos de caja. La decisión central: ¿cuánto dinero hay que levantar y cuándo, y qué tan sensible es esa cifra a un retraso o a un sobrecosto?

📘 **Dónde se aprende** (1 clase): [B126-C03 · Proyección de flujos de caja de un proyecto espacial](../programa/clases/B126/B126-C03-proyeccion-de-flujos-de-caja-de-un-proyecto-espacial/CLASE.md).

### FIR

- Un filtro FIR (respuesta finita al impulso) calcula `y[n] = Σ_{m=0}^{M−1} h[m] x[n − m]`; la lista `h[m]` son los coeficientes.

💡 **Cómo se explica en la clase [B15-C07](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md):**
- Un FIR de coeficientes simétricos y `M` términos retrasa todas las frecuencias por igual, `(M − 1)/2` muestras (en el laboratorio, un pulso con centroide en 150 sale en `165` con `M = 31`: retardo `15,000` exacto).
- 🎯 **Por qué importa:** Una curva de luz tiene una modulación lenta de la estrella (manchas que rotan) de 2000 partes por millón y, escondido en ella, el paso de un planeta que reduce el brillo 1000 ppm durante tres horas. Para ver el tránsito hay que quitar la modulación; pero si el filtro es demasiado agresivo, también se come parte del tránsito.

📘 **Dónde se aprende** (1 clase): [B15-C07 · Filtrado digital](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md).

### Firma

- Firma: vector de desviaciones de una causa.

💡 **Cómo se explica en la clase [B96-C29](../programa/clases/B96/B96-C29-diagnostico-de-fallas-de-enlace/CLASE.md):**
- M --> D["Distancia normalizada a cada firma"]
- *Descripción textual:* cada causa tiene una firma; una medida con ruido se compara con todas; se elige la más cercana; la matriz de confusión mide el acierto y la cota teórica lo verifica; el par más confundible indica qué medida añadir.
- 🎯 **Por qué importa:** Perder tiempo de contacto buscando la causa equivocada es caro. La decisión central: ¿qué medidas distinguen las causas y cuáles se confunden entre sí?

📘 **Dónde se aprende** (1 clase): [B96-C29 · Diagnóstico de fallas de enlace](../programa/clases/B96/B96-C29-diagnostico-de-fallas-de-enlace/CLASE.md).

### Firma astrométrica

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B29-C04):** La astrometría mide la inclinación y la masa verdadera, pero la señal es diminuta. La decisión central: ¿cuál es la firma de un planeta a una distancia dada y con qué incertidumbre se recupera su órbita junto al paralaje y el movimiento propio?

📘 **Dónde se aprende** (1 clase): [B29-C04 · Astrometría de exoplanetas](../programa/clases/B29/B29-C04-astrometria-de-exoplanetas/CLASE.md).

### Firn

- El firn es nieve compactada de densidad menor que la del hielo.

💡 **Cómo se explica en la clase [B57-C14](../programa/clases/B57/B57-C14-glaciares-y-criosfera/CLASE.md):**
- Un glaciar de `10⁵ km²` que baja `0,5 m/año` pierde `45,9 Gt/año` si lo perdido es hielo (917 kg/m³, referencia no consultada) y `17,5 Gt/año` si es firn (350 kg/m³).
- 🎯 **Por qué importa:** Un glaciar que baja medio metro puede haber perdido mucha o poca masa según lo que se pierda sea hielo o nieve. La decisión central: ¿qué densidad uso para convertir cambios de altura en masa y cuánto cambia el resultado?

📘 **Dónde se aprende** (1 clase): [B57-C14 · Glaciares y criósfera](../programa/clases/B57/B57-C14-glaciares-y-criosfera/CLASE.md).

### FISTA

- La restricción blanda de velocidad se castiga con `ρ max(0, |ω|−ω_max)²`. FISTA es un gradiente proyectado acelerado.

💡 **Cómo se explica en la clase [B87-C21](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md):**
- FISTA con 1500 iteraciones por paso (arranque en caliente) converge: la diferencia máxima entre la solución a 1500 y a 15 000 iteraciones es `0,623 %` del límite y el residuo del gradiente proyectado `7,11e-01`.
- Paso 3 · Solución. FISTA, `0,62 %` de diferencia con la solución casi exacta.
- 🎯 **Por qué importa:** Un PD satura el par y no sabe de límites de velocidad: puede superar el máximo de la rueda o de la carga útil. La decisión central: ¿cómo formular un problema que respete par y velocidad, cuánto cuesta calcularlo y qué se gana?

📘 **Dónde se aprende** (1 clase): [B87-C21 · Control predictivo basado en modelo (MPC) para vehículos espaciales](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md).

### Fisura

- Una fisura es una grieta alargada por la que sale el magma.

💡 **Cómo se explica en la clase [B70-C01](../programa/clases/B70/B70-C01-volcanismo-basaltico-escudos-fisuras-y-llanuras-planetarias/CLASE.md):**
- Para emitir `1 km³` por una fisura de `10 km` con `w = 1 m` tardan `0,71 d` (Tierra), `1,86 d` (Marte) y `4,29 d` (Luna) en este modelo.
- Imagina el escudo como un cuenco invertido cuyo perfil se ajusta con un exponente, y la fisura como una rendija por la que el fluido avanza más rápido en el centro que en las paredes.
- 🎯 **Por qué importa:** Una llanura de lava no dice por sí sola cuánto magma la formó ni cuánto tardó. La decisión central: ¿qué volumen y qué caudal corresponden a este edificio y a esta fisura, y qué cambiaría en otro planeta?

📘 **Dónde se aprende** (1 clase): [B70-C01 · Volcanismo basáltico: escudos, fisuras y llanuras planetarias](../programa/clases/B70/B70-C01-volcanismo-basaltico-escudos-fisuras-y-llanuras-planetarias/CLASE.md).

### Fit check

- Flujo de ensayos: orden de los ensayos. Fit check: ajuste con el dispensador.

💡 **Cómo se explica en la clase [B90-C20](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md):**
- A["Fit check"] --> B["Funcional<br/>de referencia"]
- 🎯 **Por qué importa:** Un calendario de ensayos sin contingencia casi nunca se cumple: cada falla suma retrabajo y repetición. La decisión central: ¿cuánto tiempo reservar para terminar con una confianza dada?

📘 **Dónde se aprende** (1 clase): [B90-C20 · Campaña conceptual de calificación de CubeSat](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md).

### FITS

- FITS: bloques de 2880 bytes con tarjetas de 80 caracteres.

💡 **Cómo se explica en la clase [B40-C14](../programa/clases/B40/B40-C14-productos-de-datos-de-planck-y-misiones-del-cmb/CLASE.md):**
- *Descripción textual:* se escribe y se lee un FITS, se convierten unidades y se evalúa una verosimilitud por bandas.
- 🎯 **Por qué importa:** Usar un producto sin leer su cabecera es una fuente clásica de errores de unidades y de orden de pixeles. La decisión central: ¿qué dice la cabecera y cómo se convierte y se compara con un modelo?

📘 **Dónde se aprende** (1 clase): [B40-C14 · Productos de datos de Planck y misiones del CMB](../programa/clases/B40/B40-C14-productos-de-datos-de-planck-y-misiones-del-cmb/CLASE.md).

### FK

- Los tipos descritos por NAIF son SPK (posición y velocidad), CK (orientación de nave), PCK (tamaño, forma y orientación de cuerpos), IK (campo de visión de instrumentos), FK (marcos), LSK (segundos intercalares), SCLK (reloj de nave) y DSK (formas).

🎯 **Por qué importa (clase B74-C21):** Un resultado de navegación depende de qué kernels se cargaron y en qué orden: dos corridas con el mismo código pueden dar trayectorias distintas. La decisión central: ¿cómo declaro, valido y audito el conjunto de kernels de una solución para que sea reproducible?

📘 **Dónde se aprende** (1 clase): [B74-C21 · Kernels SPICE y su uso en navegación](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md).

### Flanco de subida

- La forma de onda es la potencia del eco en función del tiempo; su flanco de subida marca la superficie media.

🎯 **Por qué importa (clase B57-C09):** La altura del mar cambia unos milímetros por año, pero el eco de un pulso es ruidoso. La decisión central: ¿cuántos pulsos hay que promediar y cómo se ajusta el eco para que el error de distancia del ajuste se reduzca lo necesario?

📘 **Dónde se aprende** (1 clase): [B57-C09 · Altimetría satelital](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md).

### Flat

- El flat es un cuadro de campo uniformemente iluminado.

💡 **Cómo se explica en la clase [B44-C14](../programa/clases/B44/B44-C14-calibracion-con-flat/CLASE.md):**
- Sin corregir, la no uniformidad es `0,0386`; con un flat de `80` cuadros, `0,00738`.
- Límite: iluminación del flat uniforme y sin bias ni dark residuales.
- ⚠️ **Error frecuente:** Aplicar el flat antes del bias y el dark. Se corrige con la sección 11.
- 🎯 **Por qué importa:** Los píxeles no responden igual y el campo se oscurece hacia el borde. La decisión central: ¿cuántos flats hacen falta para que el ruido del flat no domine?

📘 **Dónde se aprende** (1 clase): [B44-C14 · Calibración con flat](../programa/clases/B44/B44-C14-calibracion-con-flat/CLASE.md).

### Flecha

- La flecha (o sagita) es la profundidad del espejo en el borde.
- La flecha es el desplazamiento del centro respecto del borde.

💡 **Cómo se explica en la clase [B09-C13](../programa/clases/B09/B09-C13-areas-y-volumenes-por-integracion/CLASE.md):**
- La flecha en el borde es `R²/(4f) = 15,6 mm`.
- 🎯 **Por qué importa:** Un telescopio necesita un espejo con forma de paraboloide. Cuánto vidrio hay que retirar de un disco plano para darle forma, cuánto pesa, y cuánta superficie hay que aluminizar son preguntas de volumen y área.

📘 **Dónde se aprende** (2 clases): [B09-C13 · Áreas y volúmenes por integración](../programa/clases/B09/B09-C13-areas-y-volumenes-por-integracion/CLASE.md); [B43-C03 · Materiales para espejos](../programa/clases/B43/B43-C03-materiales-para-espejos/CLASE.md).

### Flecha de voladizo

- La flecha de voladizo `P L³/(3EI)` o `w L⁴/(8EI)`.

🎯 **Por qué importa (clase B43-C10):** Lo que decolima no es la flexión sino la flexión diferencial entre primario y secundario. La decisión central: ¿qué rigideces hacen que los dos extremos se muevan lo mismo, de modo que el eje óptico solo se desplace en paralelo?

📘 **Dónde se aprende** (1 clase): [B43-C10 · Estructura de tubo óptico](../programa/clases/B43/B43-C10-estructura-de-tubo-optico/CLASE.md).

### Flexión gravitatoria

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B49-C03):** Con un haz estrecho, un error de apuntado pequeño pierde ganancia. La decisión central: ¿qué términos modelar, y cuánto error residual queda frente al ancho del haz?

📘 **Dónde se aprende** (1 clase): [B49-C03 · Apuntamiento y seguimiento de radiotelescopios: modelos de apuntado y errores](../programa/clases/B49/B49-C03-apuntamiento-y-seguimiento-de-radiotelescopios-modelos-de-apuntado-y-errores/CLASE.md).

### Flotabilidad

- La flotabilidad es `g (T_p − T_e)/T_e`.

💡 **Cómo se explica en la clase [B54-C07](../programa/clases/B54/B54-C07-dinamica-de-tormentas/CLASE.md):**
- TP["T de la parcela"] --> B["flotabilidad B"]
- *Descripción textual:* la diferencia de temperatura entre parcela y ambiente da la flotabilidad; su integral es la CAPE y de ella sale la cota de velocidad.
- ⚠️ **Error frecuente:** Sumar también los tramos de flotabilidad negativa. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** La energía convectiva disponible decide si una tormenta tiene vigor o no. La pregunta motivadora: ¿cuánta velocidad puede alcanzar el aire que sube si toda la flotabilidad se convierte en movimiento?

📘 **Dónde se aprende** (1 clase): [B54-C07 · Dinámica de tormentas](../programa/clases/B54/B54-C07-dinamica-de-tormentas/CLASE.md).

### Flotabilidad neutra

- La flotabilidad neutra ocurre cuando el empuje iguala al peso.

💡 **Cómo se explica en la clase [B104-C15](../programa/clases/B104/B104-C15-entrenamiento-subacuatico-como-analogia/CLASE.md):**
- *Descripción textual:* del volumen y la masa se obtiene el lastre que da flotabilidad neutra; en el agua, la masa añadida y el arrastre hacen que el movimiento difiera del que habría en el vacío.
- Lastre para flotabilidad neutra: 1,36 kg; presión a 12,2 m: 220,5 kPa.
- 🎯 **Por qué importa:** El agua anula el peso neto, pero también se opone al movimiento. La decisión central: ¿qué aspectos de una tarea espacial se pueden entrenar bien en el agua y cuáles quedan distorsionados por la inercia y el arrastre del fluido?

📘 **Dónde se aprende** (1 clase): [B104-C15 · Entrenamiento subacuático como analogía](../programa/clases/B104/B104-C15-entrenamiento-subacuatico-como-analogia/CLASE.md).

### Fluctuación

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B32-C07](../programa/clases/B32/B32-C07-modelos-de-atmosferas-estelares-1d-y-3d-hidrodinamicos/CLASE.md):**
- Una fluctuación del 10 % aumenta el flujo medio un `6,0 %`.
- Descripción larga: la fluctuación del 10 % produce un 6 % más de flujo.
- 🎯 **Por qué importa:** Las abundancias derivadas con 1D pueden diferir de las 3D por la no linealidad del flujo con la temperatura. La decisión central: ¿cuánto sesga una fluctuación la temperatura inferida?

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

📘 **Dónde se aprende** (6 clases): [B27-C18 · Neutrinos de supernova](../programa/clases/B27/B27-C18-neutrinos-de-supernova/CLASE.md); [B30-C12 · Erupciones y fulguraciones solares](../programa/clases/B30/B30-C12-erupciones-y-fulguraciones-solares/CLASE.md); [B47-C14 · Radiación y degradación](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md); [B68-C02 · Fotodesorción de hielos interestelares](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md); [B85-C13 · Efectos de oxígeno atómico](../programa/clases/B85/B85-C13-efectos-de-oxigeno-atomico/CLASE.md); [B112-C01 · Magnitudes dosimétricas: dosis absorbida, LET y eficacia biológica](../programa/clases/B112/B112-C01-magnitudes-dosimetricas-dosis-absorbida-let-y-eficacia-biologica/CLASE.md).

### Fluido perfecto

- Un fluido perfecto tiene `T^ab = (ρ + p) u^a u^b + p g^ab`.

💡 **Cómo se explica en la clase [B39-C04](../programa/clases/B39/B39-C04-tensor-de-energia-momento-y-fuentes-de-curvatura/CLASE.md):**
- Límite: un fluido perfecto, sin viscosidad ni flujo de calor.
- 🎯 **Por qué importa:** La fuente de la gravedad es `T^ab`. La decisión central: ¿qué tensor describe la materia y qué condiciones debe cumplir para ser físicamente razonable?

📘 **Dónde se aprende** (1 clase): [B39-C04 · Tensor de energía-momento y fuentes de curvatura](../programa/clases/B39/B39-C04-tensor-de-energia-momento-y-fuentes-de-curvatura/CLASE.md).

### Fluido supercrítico

- El punto crítico `(T_c, P_c)` es el extremo de la curva de vaporización: por encima de ambos, la sustancia es un fluido supercrítico, sin diferencia nítida entre líquido y gas.

💡 **Cómo se explica en la clase [B06-C11](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md):**
- Venus (92 bar, 737 K): el CO₂ supera `T_c` y `P_c`: fluido supercrítico; el agua, con `T > 647 K`, no puede ser líquida a ninguna presión.
- 🎯 **Por qué importa:** La temperatura de ebullición del agua no es una constante de la naturaleza: depende de la presión. En lo alto de una montaña hierve a menos de 100 °C; en Marte, con 6 mb, el agua apenas puede ser líquida; en Venus, a 92 bar y 737 K, el CO₂ no es ni líquido ni gas.

📘 **Dónde se aprende** (1 clase): [B06-C11 · Diagramas de fase](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md).

### Flujo

- El flujo es la energía de luz recibida por unidad de área y tiempo; el brillo aparente es lo que percibimos de él.
- El flujo `F` es la energía recibida por unidad de área y tiempo (W/m²) y cae con el cuadrado de la distancia.
- El flujo `F` es la energía luminosa que llega por unidad de área y tiempo.
- *(y 9 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C09](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md):**
- El brillo da el flujo recibido, pero un objeto débil puede estar lejos o ser intrínsecamente poco luminoso: brillo y distancia están mezclados.
- 🎯 **Por qué importa:** Sobre una galaxia a 43 Mpc solo tienes luz. De esa luz sale su dirección, cuánto brilla, de qué color es y qué líneas aparecen en su espectro; de las líneas sale `z = 0,0101` (C01).

📖 **Explicado a fondo:** [Flujo y luminosidad](esencial/esencial-d-l.md#flujo-y-luminosidad) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (13 clases): [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B01-C14 · Estrellas y sus principales propiedades](../programa/clases/B01/B01-C14-estrellas-y-sus-principales-propiedades/CLASE.md); [B08-C11 · Magnitudes aparentes y brillo](../programa/clases/B08/B08-C11-magnitudes-aparentes-y-brillo/CLASE.md); [B09-C19 · Cálculo vectorial introductorio](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md); [B21-C01 · Volúmenes finitos y solucionadores de Riemann para leyes de conservación](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md); [B28-C05 · Ondas gravitacionales](../programa/clases/B28/B28-C05-ondas-gravitacionales/CLASE.md) y 7 más.

### Flujo ahogado

- El flujo ahogado (o sónico) ocurre cuando la presión exterior es menos de la mitad de la interior: el caudal depende solo de la presión interior.

🎯 **Por qué importa (clase B104-C13):** Un procedimiento sirve si se puede ejecutar dentro del tiempo disponible. La decisión central: ¿para qué tamaños de orificio alcanza un tiempo de respuesta de 15 minutos y a partir de cuál ya no?

📘 **Dónde se aprende** (1 clase): [B104-C13 · Procedimientos de emergencia](../programa/clases/B104/B104-C13-procedimientos-de-emergencia/CLASE.md).

### Flujo conductivo

- El flujo conductivo de Spitzer.

💡 **Cómo se explica en la clase [B34-C01](../programa/clases/B34/B34-C01-calentamiento-coronal-mecanismos-y-evidencias/CLASE.md):**
- Con `T = 2 × 10⁶ K`, `L = 100 Mm` y `n = 10¹⁵ m⁻³` (ilustrativos), el flujo conductivo es `323 W/m²` y la pérdida radiativa `150 W/m²`.
- 🎯 **Por qué importa:** Elegir un mecanismo de calentamiento exige saber cuánta energía hay que reponer y de dónde sale. La decisión central: ¿cuánta energía pierde un bucle y qué eventos pueden reponerla?

📘 **Dónde se aprende** (1 clase): [B34-C01 · Calentamiento coronal: mecanismos y evidencias](../programa/clases/B34/B34-C01-calentamiento-coronal-mecanismos-y-evidencias/CLASE.md).

### Flujo congelado

- El flujo congelado significa `BR² = const` al contraerse.

💡 **Cómo se explica en la clase [B27-C06](../programa/clases/B27/B27-C06-magnetares-y-campos-extremos/CLASE.md):**
- *Descripción textual:* el campo se compara con `B_Q` para decidir si los efectos cuánticos son relativistas; su energía crece con `B²`; el flujo congelado del progenitor fija el campo de la estrella contraída.
- 🎯 **Por qué importa:** Los magnetares producen estallidos y llamaradas gigantes que alimenta su campo, no su rotación. Entender la escala del campo y de su energía explica por qué son una familia aparte y cómo se interpretan sus espectros.

📘 **Dónde se aprende** (2 clases): [B27-C06 · Magnetares y campos extremos](../programa/clases/B27/B27-C06-magnetares-y-campos-extremos/CLASE.md); [B42-C20 · Laboratorio de corrección óptica simulada](../programa/clases/B42/B42-C20-laboratorio-de-correccion-optica-simulada/CLASE.md).

### Flujo cruzado

- Un flujo cruzado es una dependencia entre funciones de subsistemas distintos y es un candidato a interfaz (C08).

🎯 **Por qué importa (clase B83-C06):** Si se salta a las piezas demasiado pronto, se diseñan cosas que nadie sabe para qué sirven; si se descompone bien, se ve qué función domina el tiempo y dónde se acoplan los subsistemas. La decisión central: ¿qué funciones son críticas para el tiempo y qué subsistemas quedan más acoplados?

📘 **Dónde se aprende** (1 clase): [B83-C06 · Descomposición funcional](../programa/clases/B83/B83-C06-descomposicion-funcional/CLASE.md).

### Flujo de calor convectivo de remanso

- El flujo de calor convectivo de remanso es `q̇ = k√(ρ/R_n)V³` con `k = 1,7415·10⁻⁴` (SI, Tierra).

🎯 **Por qué importa (clase B77-C15):** El flujo de calor máximo y la carga total deciden qué material y qué espesor protegen al vehículo, y no se maximizan en el mismo punto que la desaceleración. La decisión central: ¿cuánto vale el flujo de pico, a qué altitud ocurre y cómo escala con el radio de la nariz y el coeficiente balístico?

📘 **Dónde se aprende** (1 clase): [B77-C15 · Calentamiento aerodinámico](../programa/clases/B77/B77-C15-calentamiento-aerodinamico/CLASE.md).

### Flujo de datos

- Un flujo de datos (*pipeline*) es una cadena de etapas donde la salida de una es la entrada de la siguiente.

🎯 **Por qué importa (clase B14-C18):** Un artículo usa «datos de un archivo público filtrados por paralaje y magnitud». Dos años después nadie puede repetir el filtro: el archivo se actualizó, los parámetros no se anotaron y la consulta no se guardó.

📘 **Dónde se aprende** (1 clase): [B14-C18 · Flujos de datos espaciales](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md).

### Flujo de ensayos

- Campaña de calificación: secuencia de ensayos que demuestra la unidad. Flujo de ensayos: orden de los ensayos.

🎯 **Por qué importa (clase B90-C20):** Un calendario de ensayos sin contingencia casi nunca se cumple: cada falla suma retrabajo y repetición. La decisión central: ¿cuánto tiempo reservar para terminar con una confianza dada?

📘 **Dónde se aprende** (1 clase): [B90-C20 · Campaña conceptual de calificación de CubeSat](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md).

### Flujo de fotones fotosintéticos (PPFD)

- El flujo de fotones fotosintéticos (PPFD) cuenta los fotones de 400–700 nm que llegan a una superficie (µmol m⁻² s⁻¹).

🎯 **Por qué importa (clase B115-C02):** La luz es el mayor consumo eléctrico de un cultivo cerrado. La decisión central: ¿cuántos fotones por metro cuadrado y día hacen falta, con qué eficacia se producen y qué potencia y calor suponen para el hábitat?

📘 **Dónde se aprende** (1 clase): [B115-C02 · Iluminación de cultivos con LED y espectro de crecimiento](../programa/clases/B115/B115-C02-iluminacion-de-cultivos-con-led-y-espectro-de-crecimiento/CLASE.md).

### Flujo de Hertz–Knudsen

- El flujo de Hertz–Knudsen es `J = p √(M/(2π R T))`.
- El flujo de Hertz–Knudsen `J = m·α·p/√(2π m k_B T)` es la masa que sale por unidad de área y tiempo hacia el vacío;
- El flujo de Hertz–Knudsen es el número de moléculas que golpea una superficie por unidad de área y tiempo.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B68-C04](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md):**
- *Descripción textual:* el flujo de Hertz–Knudsen fija la contaminación y la deposición; el espesor sale del infrarrojo; la TPD entrega una tasa que la cámara con bombeo transforma en la señal del espectrómetro, con un retraso.
- 🎯 **Por qué importa:** Un hielo de 10 ML de CO sobre una superficie a 10 K se contamina con agua residual en horas si la presión de fondo no es lo bastante baja, y una TPD con bombeo insuficiente deforma el pico que se mide.

📘 **Dónde se aprende** (4 clases): [B47-C12 · Óptica en ambientes de vacío](../programa/clases/B47/B47-C12-optica-en-ambientes-de-vacio/CLASE.md); [B53-C13 · Geomorfología de hielos](../programa/clases/B53/B53-C13-geomorfologia-de-hielos/CLASE.md); [B67-C03 · Muestreo criogénico y preservación de volátiles en muestras](../programa/clases/B67/B67-C03-muestreo-criogenico-y-preservacion-de-volatiles-en-muestras/CLASE.md); [B68-C04 · Laboratorio de astroquímica de hielos en ultra alto vacío criogénico](../programa/clases/B68/B68-C04-laboratorio-de-astroquimica-de-hielos-en-ultra-alto-vacio-criogenico/CLASE.md).

### Flujo de masa

- El flujo de masa `Ṁ = 4πr²ρv`.

💡 **Cómo se explica en la clase [B30-C10](../programa/clases/B30/B30-C10-viento-solar-y-heliosfera/CLASE.md):**
- *Descripción textual:* la temperatura da la velocidad del sonido y el radio crítico; la ecuación de Parker da `v(r)`, del que salen el flujo de masa y la espiral.
- ⚠️ **Error frecuente:** Olvidar el flujo de masa constante. Se corrige con 8.3.
- 🎯 **Por qué importa:** El viento solar es el vehículo que lleva la actividad del Sol a la Tierra. La decisión central: ¿cuándo pasa el viento a supersónico y qué velocidad alcanza a 1 au?

📘 **Dónde se aprende** (1 clase): [B30-C10 · Viento solar y heliosfera](../programa/clases/B30/B30-C10-viento-solar-y-heliosfera/CLASE.md).

### Flujo de micrometeoritos

- El flujo de micrometeoritos `F(≥d) = F₁ (d/0,1 mm)^(−2)`.

💡 **Cómo se explica en la clase [B85-C28](../programa/clases/B85/B85-C28-proteccion-pasiva-frente-al-ambiente-espacial/CLASE.md):**
- MM["Flujo de micrometeoritos + P límite"] --> TP["t_perforación"]
- 🎯 **Por qué importa:** Cada milímetro de blindaje cuesta masa, y el requisito que manda cambia con el entorno. La decisión central: ¿qué espesor y qué material cumplen la dosis y la probabilidad de perforación con la menor masa?

📘 **Dónde se aprende** (1 clase): [B85-C28 · Protección pasiva frente al ambiente espacial](../programa/clases/B85/B85-C28-proteccion-pasiva-frente-al-ambiente-espacial/CLASE.md).

### Flujo de Poiseuille

- El flujo de Poiseuille es el flujo laminar viscoso entre paredes paralelas.

🎯 **Por qué importa (clase B70-C01):** Una llanura de lava no dice por sí sola cuánto magma la formó ni cuánto tardó. La decisión central: ¿qué volumen y qué caudal corresponden a este edificio y a esta fisura, y qué cambiaría en otro planeta?

📘 **Dónde se aprende** (1 clase): [B70-C01 · Volcanismo basáltico: escudos, fisuras y llanuras planetarias](../programa/clases/B70/B70-C01-volcanismo-basaltico-escudos-fisuras-y-llanuras-planetarias/CLASE.md).

### Flujo de proa

- El flujo de proa es `Φ = n v cosθ`.

💡 **Cómo se explica en la clase [B85-C13](../programa/clases/B85/B85-C13-efectos-de-oxigeno-atomico/CLASE.md):**
- *Descripción textual:* la densidad y la velocidad dan el flujo de proa; integrado en el tiempo es la fluencia; multiplicada por la reactividad da el espesor perdido y la vida de la capa.
- ⚠️ **Error frecuente:** Aplicar el flujo de proa a todas las caras. depende de `cosθ` (8.2)
- 🎯 **Por qué importa:** Un polímero exterior puede desaparecer en meses en la cara de proa a baja altitud. La decisión central: ¿cuánto espesor pierde una superficie por año según la altitud y la orientación, y qué protección dura la misión?

📘 **Dónde se aprende** (1 clase): [B85-C13 · Efectos de oxígeno atómico](../programa/clases/B85/B85-C13-efectos-de-oxigeno-atomico/CLASE.md).

### Flujo de puerta

- El flujo de puerta `Q` es el número de personas por segundo que cruza una salida.

🎯 **Por qué importa (clase B114-C01):** Una salida existe en el plano, pero la evacuación depende de cuánto se tarda en llegar a ella y de qué pasa si el camino principal queda bloqueado. La decisión central: ¿cuánto tarda en salir toda la tripulación y qué ruta queda si falla la principal?

📘 **Dónde se aprende** (1 clase): [B114-C01 · Rutas de evacuación y salidas de emergencia en hábitats](../programa/clases/B114/B114-C01-rutas-de-evacuacion-y-salidas-de-emergencia-en-habitats/CLASE.md).

### Flujo estacionario

- Un flujo estacionario es aquel en que cada abundancia deja de cambiar.

💡 **Cómo se explica en la clase [B24-C21](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md):**
- Descripción larga: en Poisson, el máximo está cerca de `i = τ`; en el flujo estacionario, la abundancia es inversamente proporcional a la sección eficaz.
- 🎯 **Por qué importa:** Las estrellas AGB son una fuente importante de carbono, nitrógeno y elementos pesados del medio interestelar, y sus abundancias superficiales son el registro observable de lo que ocurre en su interior.

📘 **Dónde se aprende** (1 clase): [B24-C21 · Rama asintótica de gigantes: pulsos térmicos y proceso s](../programa/clases/B24/B24-C21-rama-asintotica-de-gigantes-pulsos-termicos-y-proceso-s/CLASE.md).

### Flujo estelar efectivo

- El flujo estelar efectivo `S_ef` es el flujo recibido en unidades del terrestre.

🎯 **Por qué importa (clase B56-C12):** Elegir blancos para buscar biofirmas exige un criterio objetivo. La zona habitable lo ofrece, con limitaciones.

📘 **Dónde se aprende** (1 clase): [B56-C12 · Exoplanetas potencialmente habitables](../programa/clases/B56/B56-C12-exoplanetas-potencialmente-habitables/CLASE.md).

### Flujo estrangulado

- El flujo estrangulado es el que alcanza la velocidad del sonido en la garganta y ya no depende de la presión de salida.
- El flujo estrangulado es el máximo caudal másico por un orificio cuando la presión exterior es muy baja.
- El flujo estrangulado alcanza Mach 1 en la garganta.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B70-C06](../programa/clases/B70/B70-C06-criovulcanismo-lavas-heladas-y-emision-de-volatiles/CLASE.md):**
- Para vapor de agua (`M = 0,018015 kg/mol`, `γ = 1,33`, `T₀ = 273,15 K`, ilustrativos), el flujo estrangulado tiene `T* = 2T₀/(γ+1) = 234,5 K` y `v* = √(2γ/(γ+1) · RT₀/M) = 379,4 m/s`; coincide con `√(γRT*/M)` a `10⁻¹²`.
- 🎯 **Por qué importa:** El agua líquida es más densa que el hielo, así que no sube sola. La decisión central: ¿qué presión extra y qué mecanismo hacen falta para que el agua llegue a la superficie?

📘 **Dónde se aprende** (5 clases): [B70-C06 · Criovulcanismo: lavas heladas y emisión de volátiles](../programa/clases/B70/B70-C06-criovulcanismo-lavas-heladas-y-emision-de-volatiles/CLASE.md); [B78-C10 · Propulsión de gas frío](../programa/clases/B78/B78-C10-propulsion-de-gas-frio/CLASE.md); [B106-C02 · Presurización de módulos](../programa/clases/B106/B106-C02-presurizacion-de-modulos/CLASE.md); [B110-C01 · Despresurización: detección, aislamiento y respuesta](../programa/clases/B110/B110-C01-despresurizacion-deteccion-aislamiento-y-respuesta/CLASE.md); [B114-C02 · Detección, localización y respuesta a fugas de presión](../programa/clases/B114/B114-C02-deteccion-localizacion-y-respuesta-a-fugas-de-presion/CLASE.md).

### Flujo HLL

- El flujo HLL es un solucionador aproximado de Riemann.

🎯 **Por qué importa (clase B38-C06):** Cada método tiene errores distintos en choques y discontinuidades de contacto. La decisión central: ¿qué error comete cada método frente a una solución exacta y cómo cambia con la resolución?

📘 **Dónde se aprende** (1 clase): [B38-C06 · Hidrodinámica en simulaciones: SPH y métodos de malla](../programa/clases/B38/B38-C06-hidrodinamica-en-simulaciones-sph-y-metodos-de-malla/CLASE.md).

### Flujo integral

- El flujo integral es el número por área y tiempo sobre una energía.

💡 **Cómo se explica en la clase [B28-C04](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md):**
- Con `γ₁ = 2,7`, `γ₂ = 3,1` y rodilla en `10¹⁵ eV`, el flujo integral analítico y el numérico (Simpson en `ln E`) coinciden a `10⁻⁶`: `1,173684 × 10⁻¹⁹` por encima de `10¹¹ eV` y `4,672165 × 10⁻²³` por encima de `10¹³ eV` (unidades arbitrarias).
- ESP["E^−2,7 → rodilla → E^−3,1"] --> FI["flujo integral"]
- 🎯 **Por qué importa:** El origen de los rayos cósmicos de mayor energía sigue abierto; el criterio de Hillas descarta fuentes y la anisotropía apunta a regiones. La decisión central: ¿qué fuentes pueden alcanzar una energía dada y qué anisotropía se puede detectar con un número dado de eventos?

📘 **Dónde se aprende** (1 clase): [B28-C04 · Rayos cósmicos de alta energía](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md).

### Flujo libre

- El flujo libre es el flujo operativo menos la inversión (capex).

💡 **Cómo se explica en la clase [B125-C06](../programa/clases/B125/B125-C06-plan-empresarial-de-una-empresa-espacial/CLASE.md):**
- Flujo libre `= operativo − capex` (`18` M u.m. en los trimestres 1, 2, 9, 10 y 15).
- O --> F["flujo libre = operativo - capex"]
- 🎯 **Por qué importa:** Integrar mercado, finanzas y operación en un plan es el cierre del módulo; el proyecto de B124 es general y no trata una empresa concreta con su caja. La decisión central: ¿cuánta caja necesita la empresa para llegar a su punto de equilibrio y qué supuestos pueden hundir el plan?

📘 **Dónde se aprende** (1 clase): [B125-C06 · Plan empresarial de una empresa espacial](../programa/clases/B125/B125-C06-plan-empresarial-de-una-empresa-espacial/CLASE.md).

### Flujo luminoso

- El flujo luminoso se mide en lúmenes con `683 lm/W` a 540 THz.

🎯 **Por qué importa (clase B45-C01):** Todo flujo medido en un telescopio es una cantidad radiométrica o fotométrica con una definición precisa; confundir vatios, lúmenes y fotones arruina la calibración. La decisión central: ¿en qué unidades se expresa lo que llega al detector y cómo se pasa de una a otra?

📘 **Dónde se aprende** (1 clase): [B45-C01 · Radiometría y fotometría](../programa/clases/B45/B45-C01-radiometria-y-fotometria/CLASE.md).

### Flujo magnético

- El flujo magnético es `Φ = BA`.
- El flujo magnético es la integral de `B` por una superficie.

🎯 **Por qué importa (clase B30-C04):** Las manchas son la huella visible del campo magnético y las más fáciles de contar. Cuantificar su presión, su brillo y su flujo permite relacionarlas con la irradiancia.

📘 **Dónde se aprende** (2 clases): [B30-C04 · Manchas solares](../programa/clases/B30/B30-C04-manchas-solares/CLASE.md); [B35-C07 · Congelamiento del flujo magnético y conservación en MHD ideal](../programa/clases/B35/B35-C07-congelamiento-del-flujo-magnetico-y-conservacion-en-mhd-ideal/CLASE.md).

### Flujo magnético congelado

- El flujo magnético congelado significa que, en un plasma muy conductor, `Φ = B R²` se mantiene al contraerse.

🎯 **Por qué importa (clase B24-C11):** La rotación y el campo explican por qué las estrellas jóvenes son más activas, por qué las enanas blancas y las estrellas de neutrones giran y se magnetizan tanto, y por qué no pueden girar a cualquier velocidad.

📘 **Dónde se aprende** (1 clase): [B24-C11 · Rotación y campos magnéticos](../programa/clases/B24/B24-C11-rotacion-y-campos-magneticos/CLASE.md).

### Flujo másico

- El flujo másico es `ṁ = T/(I_sp g₀)`.
- El flujo másico `ṁ = ρ A u` es la masa que cruza una sección por unidad de tiempo.

💡 **Cómo se explica en la clase [B75-C10](../programa/clases/B75/B75-C10-maniobras-impulsivas/CLASE.md):**
- Dos cuerpos con `μ = 398 602,54 km³/s²` (masa de la ficha y `G` del JPL [S1, S2]), empuje constante `T = (T/W₀)·m₀·g₀`, dirección igual a la velocidad, flujo másico `ṁ = T/(I_sp g₀)` con `I_sp = 320 s` (sintético) y `m₀ = 1000 kg`.
- Paso 2 · Flujo másico. `ṁ = 0,5×1000/320 = 1,5625 kg/s`.
- 🎯 **Por qué importa:** El modelo impulsivo es útil, pero ¿cuándo es un buen modelo? La decisión central: ¿cuánto delta-v se pierde por quemar durante un tiempo finito y de qué depende, en particular del cociente empuje/peso?

📘 **Dónde se aprende** (2 clases): [B75-C10 · Maniobras impulsivas](../programa/clases/B75/B75-C10-maniobras-impulsivas/CLASE.md); [B79-C01 · Conservación de masa en fluidos](../programa/clases/B79/B79-C01-conservacion-de-masa-en-fluidos/CLASE.md).

### Flujo mínimo detectable

- El flujo mínimo detectable es la menor densidad de flujo que supera el umbral de SNR.

🎯 **Por qué importa (clase B56-C16):** Buscar tecnología exige saber qué flujo mínimo detecta un receptor y qué potencia debería tener un transmisor a una distancia dada. La decisión central: dados la temperatura del sistema, el área efectiva, el ancho de banda y el tiempo de integración, ¿qué flujo mínimo se detecta y hasta qué distancia llega un transmisor dado?

📘 **Dónde se aprende** (1 clase): [B56-C16 · Tecnofirmas y búsqueda SETI](../programa/clases/B56/B56-C16-tecnofirmas-y-busqueda-seti/CLASE.md).

### Flujo molecular

- El camino libre medio es `λ = k_B T/(√2 π d² P)`. Flujo molecular es el régimen donde `λ` supera las dimensiones del sistema.

💡 **Cómo se explica en la clase [B84-C06](../programa/clases/B84/B84-C06-comportamiento-bajo-vacio/CLASE.md):**
- En órbita las moléculas viajan en línea recta hasta chocar con una pared: flujo molecular.
- 🎯 **Por qué importa:** Un recubrimiento de cadmio o de zinc que es inocuo en tierra puede desaparecer y contaminar ópticas en el vacío; un cálculo de un minuto lo descarta. La decisión central: ¿qué metales sobreviven sin protección al vacío a la temperatura de trabajo y cuáles se subliman?

📘 **Dónde se aprende** (1 clase): [B84-C06 · Comportamiento bajo vacío](../programa/clases/B84/B84-C06-comportamiento-bajo-vacio/CLASE.md).

### Flujo neto

- El flujo neto de un radiador es `ε σ (T⁴ − T_f⁴) − q_abs`.
- El flujo neto es ingresos menos costos e inversión de un año.

💡 **Cómo se explica en la clase [B85-C07](../programa/clases/B85/B85-C07-radiadores-espaciales/CLASE.md):**
- Q["Carga Q"] --> A["A = Q / flujo neto"]
- *Descripción textual:* la carga se divide por el flujo neto, que es la emisión menos lo absorbido del entorno; la aleta modifica el área efectiva.
- 🎯 **Por qué importa:** El área del radiador manda en masa, volumen y costo. La decisión central: ¿cuánta área necesita un radiador en el caso caliente de fin de vida y qué la reduce?

📘 **Dónde se aprende** (2 clases): [B85-C07 · Radiadores espaciales](../programa/clases/B85/B85-C07-radiadores-espaciales/CLASE.md); [B126-C03 · Proyección de flujos de caja de un proyecto espacial](../programa/clases/B126/B126-C03-proyeccion-de-flujos-de-caja-de-un-proyecto-espacial/CLASE.md).

### Flujo numérico

- El flujo numérico `F_{i+½}` es la aproximación del flujo en esa interfaz.

💡 **Cómo se explica en la clase [B21-C01](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md):**
- Eso es conservación discreta, y vale para cualquier flujo numérico que use el mismo valor en la interfaz para las dos celdas vecinas.
- Para la advección `q_t + a q_x = 0` con `a > 0`, la información viene de la izquierda y el flujo numérico es `F_{i+½} = a q_i` (esquema contracorriente o *upwind*).
- 🎯 **Por qué importa:** Casi todo lo que fluye en el espacio —el viento solar, el gas de un disco de acreción, el gas que rodea a una nave en reentrada, la onda de choque de una eyección coronal— obedece leyes de conservación: una cantidad cambia en una región solo porque entra o sale por sus bordes.

📘 **Dónde se aprende** (1 clase): [B21-C01 · Volúmenes finitos y solucionadores de Riemann para leyes de conservación](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md).

### Flujo operativo

- El flujo operativo es el margen bruto menos el gasto fijo.

💡 **Cómo se explica en la clase [B125-C06](../programa/clases/B125/B125-C06-plan-empresarial-de-una-empresa-espacial/CLASE.md):**
- El flujo operativo es positivo desde el trimestre `6`; la caja mínima es `−25,7` M u.m. en el trimestre `10`; la brecha de financiación es `25,7` M u.m.
- M --> O["flujo operativo = margen - gasto fijo"]
- 🎯 **Por qué importa:** Integrar mercado, finanzas y operación en un plan es el cierre del módulo; el proyecto de B124 es general y no trata una empresa concreta con su caja. La decisión central: ¿cuánta caja necesita la empresa para llegar a su punto de equilibrio y qué supuestos pueden hundir el plan?

📘 **Dónde se aprende** (1 clase): [B125-C06 · Plan empresarial de una empresa espacial](../programa/clases/B125/B125-C06-plan-empresarial-de-una-empresa-espacial/CLASE.md).

### Flujo pistón (PFR)

- Mezcla completa (CSTR): tanque uniforme. Flujo pistón (PFR): flujo sin mezcla longitudinal.

💡 **Cómo se explica en la clase [B106-C26](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md):**
- Flujo pistón `S = S₀ e^{−kτ}`: al 90 %, `τ = ln 10/k = 4,6 h`, 15 L.
- Con 18 h totales: 1 tanque 30 mg/L; 2, 9,9; 3, 4,69; 6, 1,23; 20, 0,178; flujo pistón 0,037.
- 🎯 **Por qué importa:** Las aguas grises son el mayor volumen del lazo y su carga orgánica hay que destruirla antes de potabilizar. La decisión central: ¿qué volumen de biorreactor y qué desinfección dan la remoción y la reducción de microorganismos requeridas?

📘 **Dónde se aprende** (1 clase): [B106-C26 · Tratamiento de aguas grises en hábitats](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md).

### Flujo residual

- Un flujo residual es el que no se aprovecha.

🎯 **Por qué importa (clase B59-C23):** Producir un kilogramo de oxígeno genera toneladas de otras cosas. La decisión central: ¿qué masa de residuo o de subproducto aparece por cada kilogramo de producto?

📘 **Dónde se aprende** (1 clase): [B59-C23 · Subproductos y flujos residuales de procesos ISRU](../programa/clases/B59/B59-C23-subproductos-y-flujos-residuales-de-procesos-isru/CLASE.md).

### Flujo solar

- El flujo solar `S ∝ 1/r²`.

🎯 **Por qué importa (clase B47-C22):** Cada órbita compra una ventaja y una dificultad. La decisión central: ¿qué punto o qué órbita da la vista del Sol que necesita el instrumento a un costo térmico y de enlace aceptable?

📘 **Dónde se aprende** (1 clase): [B47-C22 · Misiones de física solar: SOHO, SDO y Solar Orbiter](../programa/clases/B47/B47-C22-misiones-de-fisica-solar-soho-sdo-y-solar-orbiter/CLASE.md).

### Flujo térmico superficial

- El flujo térmico superficial `q` es la potencia que atraviesa una superficie por unidad de área (W/m²).

🎯 **Por qué importa (clase B65-C04):** Un planeta se enfría en parte porque pierde calor guardado y en parte vive del que producen sus isótopos radiactivos. La decisión central: ¿qué fracción del calor que sale es producción actual y qué fracción es enfriamiento?

📘 **Dónde se aprende** (1 clase): [B65-C04 · Flujo térmico planetario y balance térmico del interior](../programa/clases/B65/B65-C04-flujo-termico-planetario-y-balance-termico-del-interior/CLASE.md).

### FMA

- La FMA calcula `a·b + c` con un solo redondeo.

💡 **Cómo se explica en la clase [B14-C15](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md):**
- Con dos redondeos (multiplicar y redondear, luego sumar) el error máximo es `5,96 × 10⁻⁸`; con un solo redondeo (FMA simulado: se calcula exacto en `float64` y se redondea una vez), es `0`.
- Si una GPU usa FMA y la CPU no, sus resultados diferirán aunque ambas sean correctas (S1).
- 🎯 **Por qué importa:** Un equipo promete que su simulación irá «100 veces más rápido en GPU» y, al compararla con la de CPU, los resultados difieren en el séptimo dígito. ¿Error del código o característica de la máquina?

📘 **Dónde se aprende** (1 clase): [B14-C15 · Cálculo en GPU y limitaciones](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md).

### Focal

- La focal `f` es la distancia óptica entre la lente y el detector.
- La focal `f = pH/GSD` fija el tamaño de la imagen en el plano focal.

💡 **Cómo se explica en la clase [B57-C24](../programa/clases/B57/B57-C24-diseno-de-una-carga-util-de-observacion-terrestre/CLASE.md):**
- La línea focal mediría `218 mm` si fuera un solo detector (en la práctica se compone de varios).
- G["paso de pixel"] --> F["focal y campo de vision"]
- 🎯 **Por qué importa:** Cada requisito empuja a los demás: más resolución exige más datos, más barrido exige un campo de visión mayor, y el enlace de bajada limita cuánto se puede adquirir. La decisión central: ¿qué requisito se relaja cuando el presupuesto de datos no cierra?

📘 **Dónde se aprende** (2 clases): [B57-C24 · Diseño de una carga útil de observación terrestre](../programa/clases/B57/B57-C24-diseno-de-una-carga-util-de-observacion-terrestre/CLASE.md); [B63-C01 · Instrumentación de sondas y rovers planetarios](../programa/clases/B63/B63-C01-instrumentacion-de-sondas-y-rovers-planetarios/CLASE.md).

### Focal efectiva

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C17](../programa/clases/B41/B41-C17-telescopios-cassegrain-y-derivados/CLASE.md):**
- Como un periscopio que pliega la luz en dos: el secundario convexo la devuelve al primario y la focal efectiva es `m` veces la del primario en un tubo corto.
- 🎯 **Por qué importa:** Dos espejos permiten un tubo corto y focal larga, y distintos diseños eligen qué aberración corregir. La decisión central: ¿qué diseño corrige la coma y a qué costo?

📘 **Dónde se aprende** (1 clase): [B41-C17 · Telescopios Cassegrain y derivados](../programa/clases/B41/B41-C17-telescopios-cassegrain-y-derivados/CLASE.md).

### Foco

- Todas cumplen la propiedad foco–directriz: hay un punto (el foco) y una recta (la directriz) tales que la distancia de cada punto de la curva al foco es `e` veces su distancia a la directriz;

💡 **Cómo se explica en la clase [B04-C18](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md):**
- Fija el foco y el perihelio `q`, y mueve solo `e`: con `e = 0`, una circunferencia; al crecer `e < 1`, una elipse cada vez más estirada; en `e = 1`, la curva se abre y no vuelve (parábola); con `e > 1`, se abre aún más (hipérbola).
- 🎯 **Por qué importa:** En 2017 se descubrió un objeto que cruzaba el sistema solar con una órbita que no se cerraba: su excentricidad era mayor que 1. Eso significó que no estaba ligado al Sol: venía de fuera y se iba.

📘 **Dónde se aprende** (1 clase): [B04-C18 · Cónicas y secciones orbitales](../programa/clases/B04/B04-C18-conicas-y-secciones-orbitales/CLASE.md).

### Foco común

- Dos cónicas con foco común se describen con `(p, e, ϖ)` cada una.

🎯 **Por qué importa (clase B75-C21):** Una transferencia que apunta al radio medio de Marte puede pasar por dentro o por fuera de su órbita real, que es excéntrica. La decisión central: ¿dónde corta una elipse de transferencia a la órbita de Marte, a qué distancia y cuánto tarda en llegar allí?

📘 **Dónde se aprende** (1 clase): [B75-C21 · Intersección de cónicas en transferencias](../programa/clases/B75/B75-C21-interseccion-de-conicas-en-transferencias/CLASE.md).

### Foco objeto

- El foco objeto es el punto del eje conjugado con el infinito imagen.

💡 **Cómo se explica en la clase [B50-C04](../programa/clases/B50/B50-C04-telecentricidad-vineteo-y-diseno-del-campo/CLASE.md):**
- El foco objeto trazado en sentido inverso está en `z = -99,32886 mm`; el diafragma que anula el ángulo de salida, hallado por bisección, en `z = -99,32886 mm`.
- El ángulo de salida cambia de signo al cruzar el foco objeto.
- 🎯 **Por qué importa:** En un detector la luz que llega muy inclinada se pierde o se mezcla; en un espectrógrafo o un mosaico el viñeteo cambia el brillo según el campo. La decisión central: ¿dónde va el diafragma y cuánto campo se acepta con viñeteo?

📘 **Dónde se aprende** (1 clase): [B50-C04 · Telecentricidad, viñeteo y diseño del campo](../programa/clases/B50/B50-C04-telecentricidad-vineteo-y-diseno-del-campo/CLASE.md).

### Foco paraxial

- El foco paraxial es el límite `h → 0`.
- El foco paraxial `R/2`.

💡 **Cómo se explica en la clase [B41-C04](../programa/clases/B41/B41-C04-espejos-esfericos-y-parabolicos/CLASE.md):**
- La esfera f/5 (`D = 200 mm`) forma en el foco paraxial un disco de unas `250,5 µm` de diámetro (aproximación de rayo marginal), muy por encima del disco de Airy (clase 12).
- En `R = 2000 mm`, el foco paraxial está a `1000 mm`.
- 🎯 **Por qué importa:** El espejo primario de un telescopio reflector es una superficie cónica. La decisión central: ¿por qué se usa un paraboloide y no una esfera?

📘 **Dónde se aprende** (2 clases): [B41-C04 · Espejos esféricos y parabólicos](../programa/clases/B41/B41-C04-espejos-esfericos-y-parabolicos/CLASE.md); [B50-C01 · Trazado exacto de rayos y aberraciones de orden superior](../programa/clases/B50/B50-C01-trazado-exacto-de-rayos-y-aberraciones-de-orden-superior/CLASE.md).

### Focos

- Una elipse es el conjunto de puntos para los que la suma de las distancias a dos puntos fijos, los focos, es constante.

💡 **Cómo se explica en la clase [B04-C09](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md):**
- Los focos, en `(±c, 0)` con `c = √(a² − b²)`; equivalentemente `b = a√(1 − e²)`.
- Un punto cualquiera puede escribirse como `(a cos t, b sen t)`, y su suma de distancias a los focos vale `2a`: es la propiedad definitoria que el laboratorio comprueba en 52 puntos.
- 🎯 **Por qué importa:** Las órbitas de planetas y cometas son, en buena aproximación, elipses con el Sol en uno de sus focos. Si no sabes qué es un semieje, un foco o la excentricidad, no puedes leer una tabla de elementos orbitales ni distinguir una órbita casi circular, como la de la Tierra, de una muy alargada, como la del cometa Halley.

📘 **Dónde se aprende** (1 clase): [B04-C09 · Circunferencias y elipses](../programa/clases/B04/B04-C09-circunferencias-y-elipses/CLASE.md).

### Focos tangencial y sagital

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C14):** El color y el astigmatismo degradan el campo de refractores y espejos. La decisión central: ¿cuánto se separan los focos por color y por plano?

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

📘 **Dónde se aprende** (6 clases): [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B31-C16 · Astropartículas de alta energía](../programa/clases/B31/B31-C16-astroparticulas-de-alta-energia/CLASE.md); [B31-C18 · Restricciones experimentales de teorías](../programa/clases/B31/B31-C18-restricciones-experimentales-de-teorias/CLASE.md); [B47-C03 · Telescopios ultravioleta](../programa/clases/B47/B47-C03-telescopios-ultravioleta/CLASE.md); [B57-C11 · LiDAR satelital](../programa/clases/B57/B57-C11-lidar-satelital/CLASE.md); [B92-C05 · Receptores y detectores para comunicaciones ópticas](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md).

### Fondo compartido

- El fondo compartido reparte por igual una fracción `q` de la capacidad total.

💡 **Cómo se explica en la clase [B119-C34](../programa/clases/B119/B119-C34-equidad-de-acceso-al-espacio/CLASE.md):**
- El acceso real depende de acuerdos, precios y regulación; un fondo compartido plantea además quién lo financia y cómo se decide (C36).
- Q["Fondo compartido q"] --> N["Acceso nuevo"]
- 🎯 **Por qué importa:** El acceso desigual al espacio es un asunto de gobernanza que el catálogo no trata; esta clase da las herramientas de medición antes de las discusiones de política (C25, C36). La decisión central: ¿qué tan desigual es el acceso y cuánto lo reduce una regla de uso compartido?

📘 **Dónde se aprende** (1 clase): [B119-C34 · Equidad de acceso al espacio](../programa/clases/B119/B119-C34-equidad-de-acceso-al-espacio/CLASE.md).

### Fondo cósmico de microondas

- El fondo cósmico de microondas es radiación antigua que llena el cielo; sirve para deducir parámetros cosmológicos bajo un modelo.

💡 **Cómo se explica en la clase [B01-C16](../programa/clases/B01/B01-C16-expansion-del-universo-como-observacion/CLASE.md):**
- El análisis final del satélite Planck del fondo cósmico de microondas, bajo el modelo ΛCDM de seis parámetros, da `H₀ = 67,4 ± 0,5 km/s/Mpc` (S1).
- 🎯 **Por qué importa:** En C01 «medimos» una distancia de 43 Mpc con `H₀ = 70`. Pero ese 70 no es un dato único: Planck 2018 da 67,4 ± 0,5 y SH0ES da 73,04 ± 1,04, ambos en km/s/Mpc (S1, S2).

📘 **Dónde se aprende** (1 clase): [B01-C16 · Expansión del universo como observación](../programa/clases/B01/B01-C16-expansion-del-universo-como-observacion/CLASE.md).

### Fondo cósmico de microondas (CMB)

- El fondo cósmico de microondas (CMB) es la radiación térmica relicta.

🎯 **Por qué importa (clase B26-C15):** El fondo de microondas es la reliquia más antigua observable y da los parámetros del modelo cosmológico. Entender su espectro de cuerpo negro permite calibrar un instrumento, estimar el contenido de fotones y comprender por qué un solo número, la razón barión–fotón, resume tanta física.

📘 **Dónde se aprende** (1 clase): [B26-C15 · Radiación cósmica de fondo](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md).

### Fondo de cielo B

- El fondo de cielo `B` es la luz de fondo, en `e⁻/s/píxel`.

🎯 **Por qué importa (clase B13-C15):** Una cámara espacial debe decidir cuánto tiempo exponer para detectar una fuente débil con una relación señal-ruido (SNR) dada. Exponer poco no la detecta; exponer demasiado satura los píxeles brillantes o desperdicia tiempo de misión.

📘 **Dónde se aprende** (1 clase): [B13-C15 · Sensibilidad de detectores](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md).

### Fondo térmico

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C04](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md):**
- *Descripción textual:* la ley de Planck se verifica con dos relaciones y se usa para el fondo térmico y la temperatura de operación.
- 🎯 **Por qué importa:** Enfriar un telescopio cuesta masa, potencia y complejidad. La decisión central: ¿a qué temperatura el fondo propio deja de dominar sobre el detector?

📘 **Dónde se aprende** (1 clase): [B47-C04 · Telescopios infrarrojos](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md).

### Forma

- Su forma (`shape`) es la tupla de longitudes por eje; sus ejes se numeran desde 0.

💡 **Cómo se explica en la clase [B14-C02](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md):**
- Tercero, el resultado tiene la forma `(6,5,3)`.
- S["Satélites<br/>forma (6, 3)"] --> S2["sat[:, None, :]<br/>forma (6, 1, 3)"]
- ⚠️ **Error frecuente:** Predecir mal la forma. Se corrige escribiendo las formas antes de operar (ejercicios 1 y 2).
- 🎯 **Por qué importa:** Una constelación de seis satélites y cinco estaciones en tierra producen treinta distancias. Un catálogo de estrellas produce millones.

📘 **Dónde se aprende** (1 clase): [B14-C02 · Arreglos multidimensionales NumPy](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md).

### Forma canónica

- La forma canónica es una serialización con orden y formato fijos (claves ordenadas, sin espacios variables) para que dos registros iguales den la misma huella.
- La forma canónica ordena las claves y fija los separadores.

💡 **Cómo se explica en la clase [B50-C06](../programa/clases/B50/B50-C06-software-de-diseno-optico-modelos-reproducibles-y-verificacion/CLASE.md):**
- Con las claves en otro orden la huella es la misma, porque se serializa en forma canónica.
- M["modelo JSON"] --> H["forma canónica"]
- 🎯 **Por qué importa:** Los programas de diseño óptico son cajas con muchas opciones: lo que hace reproducible un diseño es el archivo, sus unidades, su versión y sus pruebas. La decisión central: ¿cómo se demuestra que un modelo sigue siendo el mismo y sigue dando lo mismo?

📘 **Dónde se aprende** (2 clases): [B23-C07 · Trazabilidad científica de resultados](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md); [B50-C06 · Software de diseño óptico: modelos reproducibles y verificación](../programa/clases/B50/B50-C06-software-de-diseno-optico-modelos-reproducibles-y-verificacion/CLASE.md).

### Forma de Arrhenius modificada

- La forma de Arrhenius modificada (tipo Kooij) es `k = α (T/300)^β exp(−γ/T)`.

🎯 **Por qué importa (clase B60-C02):** Un modelo de nube a 10 K usa coeficientes que se midieron o calcularon a otras temperaturas. La decisión central: ¿hasta dónde se puede confiar en un ajuste de `k(T)` fuera del intervalo donde se ajustó?

📘 **Dónde se aprende** (1 clase): [B60-C02 · Coeficientes de velocidad dependientes de la temperatura y bases cinéticas](../programa/clases/B60/B60-C02-coeficientes-de-velocidad-dependientes-de-la-temperatura-y-bases-cineticas/CLASE.md).

### Forma de información

- La forma de información suma las informaciones de las mediciones independientes: `Λ = Σ Λ_i`, y `P = Λ⁻¹`.

🎯 **Por qué importa (clase B80-C07):** B74-C04 y B74-C13 tratan la medición radiométrica y la óptica por separado. La decisión central: ¿en qué eje aporta cada sensor y cuánto mejora la incertidumbre al combinarlos?

📘 **Dónde se aprende** (1 clase): [B80-C07 · Fusión radio-óptica en navegación de espacio profundo](../programa/clases/B80/B80-C07-fusion-radio-optica-en-navegacion-de-espacio-profundo/CLASE.md).

### Forma de Joseph

- La forma de Joseph conserva la simetría de `P`.
- La forma de Joseph conserva la simetría y la semidefinición positiva de `P` en cada actualización.

💡 **Cómo se explica en la clase [B74-C09](../programa/clases/B74/B74-C09-filtro-de-kalman-extendido/CLASE.md):**
- Corrección: `K = P⁻ Hᵀ (H P⁻ Hᵀ + R)⁻¹`, `x = x⁻ + K (y − h(x⁻))`, y `P` en forma de Joseph.
- 🎯 **Por qué importa:** Una órbita no es lineal en el estado, pero a cortos intervalos y con errores pequeños se comporta casi como tal. La decisión central: ¿hasta cuándo es válida la linealización del EKF y cómo me doy cuenta de que dejó de serlo?

📘 **Dónde se aprende** (2 clases): [B74-C09 · Filtro de Kalman extendido](../programa/clases/B74/B74-C09-filtro-de-kalman-extendido/CLASE.md); [B74-C18 · Estimación autónoma a bordo](../programa/clases/B74/B74-C18-estimacion-autonoma-a-bordo/CLASE.md).

### Forma de Newton

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C06):** El foco de una cámara o de un telescopio decide el tamaño de la imagen. La decisión central: ¿dónde cae la imagen y de qué tamaño es?

📘 **Dónde se aprende** (1 clase): [B41-C06 · Distancias focales y formación de imagen](../programa/clases/B41/B41-C06-distancias-focales-y-formacion-de-imagen/CLASE.md).

### Forma de onda

- La forma de onda es la potencia del eco en función del tiempo; su flanco de subida marca la superficie media.

🎯 **Por qué importa (clase B57-C09):** La altura del mar cambia unos milímetros por año, pero el eco de un pulso es ruidoso. La decisión central: ¿cuántos pulsos hay que promediar y cómo se ajusta el eco para que el error de distancia del ajuste se reduzca lo necesario?

📘 **Dónde se aprende** (1 clase): [B57-C09 · Altimetría satelital](../programa/clases/B57/B57-C09-altimetria-satelital/CLASE.md).

### Forma débil

- La forma débil de `−u″ = f` con `u(0) = u(1) = 0` multiplica por una función de prueba `v` (también nula en los extremos) e integra por partes: `∫ u′ v′ dx = ∫ f v dx` para toda `v`.

💡 **Cómo se explica en la clase [B11-C15](../programa/clases/B11/B11-C15-elementos-finitos-introductorios/CLASE.md):**
- A["−u″ = f, u(0)=u(1)=0"] --> B["Forma débil:<br/>∫ u′v′ = ∫ f v"]
- *Descripción textual:* de la ecuación se pasa a la forma débil; se aproxima la solución con funciones sombrero; se ensambla el sistema `K u = b` sumando las contribuciones de los elementos; se resuelve y se mide el error en las normas `L²` y `H¹`.
- 🎯 **Por qué importa:** Las estructuras y los escudos de una nave no son barras rectas con mallas regulares. El análisis térmico y estructural de ingeniería espacial se hace casi siempre con elementos finitos sobre geometrías reales.

📘 **Dónde se aprende** (1 clase): [B11-C15 · Elementos finitos introductorios](../programa/clases/B11/B11-C15-elementos-finitos-introductorios/CLASE.md).

### Forma estándar

- La forma estándar es la que usa la norma de `x` sin modificar (en la forma general, se penaliza `‖L (x − x₀)‖` con una matriz `L` y un estimado previo `x₀`;

💡 **Cómo se explica en la clase [B22-C02](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md):**
- Dado `A` (`m × n`) y datos `b`, la solución de Tikhonov en forma estándar es (S2, ec. 1 con `L = I` y `x₀ = 0`):
- 🎯 **Por qué importa:** Si no puedes confiar en `x = A⁻¹ b` y no puedes bajar el ruido a voluntad, necesitas una regla que ignore lo que los datos no pueden decir. Esa regla debe tener una perilla: cuánto ignorar.

📘 **Dónde se aprende** (1 clase): [B22-C02 · Regularización de Tikhonov](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md).

### Forma general

- La forma general de la cuadrática es `ax² + bx + c = 0` con `a ≠ 0`.

🎯 **Por qué importa (clase B04-C02):** Una sonda desciende hacia la Luna; un instrumento cae desde una mesa de trabajo; una señal de radio viaja hasta un espejo y vuelve. En cada caso hay un número que no conoces (un tiempo, una distancia) y una relación que lo liga a otros que sí conoces.

📘 **Dónde se aprende** (1 clase): [B04-C02 · Ecuaciones lineales y cuadráticas](../programa/clases/B04/B04-C02-ecuaciones-lineales-y-cuadraticas/CLASE.md).

### Forma indeterminada

- Una forma indeterminada `0/0` es un cociente cuyo numerador y denominador tienden ambos a 0: no dice nada por sí sola.

🎯 **Por qué importa (clase B09-C01):** Los astrónomos miden distancias a estrellas cercanas por paralaje: un ángulo diminuto, de fracciones de segundo de arco. Con ángulos tan pequeños, `sin t`, `tan t` y `t` casi coinciden, y casi todos los cálculos prácticos los sustituyen.

📘 **Dónde se aprende** (1 clase): [B09-C01 · Límites de funciones reales](../programa/clases/B09/B09-C01-limites-de-funciones-reales/CLASE.md).

### Forma molecular

- La geometría electrónica describe cómo se distribuyen todos los dominios; la forma molecular describe sólo dónde están los átomos.

🎯 **Por qué importa (clase B06-C05):** El dióxido de carbono es el 95,1 % de la atmósfera de Marte en volumen (S2), y los hielos de las nubes densas del medio interestelar contienen, según un estudio con el telescopio James Webb, agua y CO₂ entre otras especies (S3, que se leyó sólo en resumen).

📘 **Dónde se aprende** (1 clase): [B06-C05 · Moléculas y geometría molecular](../programa/clases/B06/B06-C05-moleculas-y-geometria-molecular/CLASE.md).

### Forma suave

- La forma suave reparte el escalón en el costo variable.

💡 **Cómo se explica en la clase [B124-C22](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md):**
- La forma suave `F/(p₀ − v − S/cap) = 1515,2` difiere en `27,8`, menos que un tramo de capacidad: sirve como aproximación, no reemplaza el cálculo exacto.
- Por forma suave: costo variable efectivo `v + S/cap`.
- 🎯 **Por qué importa:** B124 trata financiamiento, pero un servicio sostenible depende de un modelo de costo que explique cómo cambia el costo medio con el volumen. La decisión central: ¿a qué precio y con qué volumen el servicio cubre sus costos, y cuánto riesgo tiene si la demanda varía?

📘 **Dónde se aprende** (1 clase): [B124-C22 · Modelo de costo de un servicio de datos](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md).

### Forma vectorial de Snell

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C08):** Los programas de diseño óptico trazan rayos exactos. La decisión central: ¿cuándo se separa el rayo real del paraxial y cómo crece esa diferencia?

📘 **Dónde se aprende** (1 clase): [B41-C08 · Trazado de rayos para telescopios](../programa/clases/B41/B41-C08-trazado-de-rayos-para-telescopios/CLASE.md).

### Formación estelar

- La densidad superficial de gas `Σ_gas` y de formación estelar `Σ_SFR` se miden en `M☉ pc⁻²` y `M☉ año⁻¹ kpc⁻²`.

💡 **Cómo se explica en la clase [B25-C05](../programa/clases/B25/B25-C05-regiones-de-formacion-estelar/CLASE.md):**
- Kennicutt (S1) midió, para 61 espirales normales y 36 galaxias con brotes de formación estelar seleccionadas en infrarrojo, la relación entre el ritmo de formación y la densidad de gas, y halló que un índice de Schmidt `N = 1,4 ± 0,15` representa la muestra combinada.
- 🎯 **Por qué importa:** Una galaxia no convierte todo su gas en estrellas a la vez: lo hace a un ritmo que puede medirse y comparar. Entender las regiones donde nacen las estrellas masivas permite reconocerlas desde lejos, y entender la relación entre gas y ritmo de formación permite saber cuánto tiempo puede una galaxia seguir formando estrellas.

📘 **Dónde se aprende** (1 clase): [B25-C05 · Regiones de formación estelar](../programa/clases/B25/B25-C05-regiones-de-formacion-estelar/CLASE.md).

### Formato de texto con metadatos

- Un formato de texto con metadatos guarda también unidades y máscara; el que usamos es ECSV, escrito por Astropy.

🎯 **Por qué importa (clase B14-C05):** Un catálogo de estrellas no es una lista de números: cada columna tiene una unidad, algunas filas no tienen paralaje, y la tabla viene de un instrumento, una época y una versión. Si pierdes eso al copiar los datos a un arreglo, pierdes la mitad del significado.

📘 **Dónde se aprende** (1 clase): [B14-C05 · Tablas astronómicas y catálogos](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md).

### Fórmula

- Una fórmula es una ecuación entre magnitudes;
- Una fórmula relaciona símbolos con una igualdad.

💡 **Cómo se explica en la clase [B03-C12](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md):**
- Cuando leas una fórmula, clasifica cada símbolo.
- S["Símbolo en una fórmula"] --> V{"¿Cambia dentro del problema?"}
- 🎯 **Por qué importa:** La masa del Sol se conoce con unas cinco cifras. Sin embargo, el producto `GM` del Sol se conoce con diez, y la constante `G` por sí sola con apenas cinco.

📘 **Dónde se aprende** (2 clases): [B03-C12 · Variables y constantes científicas](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md); [B03-C14 · Despeje de ecuaciones elementales](../programa/clases/B03/B03-C14-despeje-de-ecuaciones-elementales/CLASE.md).

### Fórmula de Bethe-Bloch

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C09):** Medir ΔE y E permite identificar la partícula. La decisión central: ¿qué espesor de detector y qué energía separan protones de partículas alfa?

📘 **Dónde se aprende** (1 clase): [B47-C09 · Detectores de partículas — Instrumentación y observatorios espaciales](../programa/clases/B47/B47-C09-detectores-de-particulas-instrumentacion-y-observatorios-espaciales/CLASE.md).

### Fórmula de Bruns

- La fórmula de Bruns es `N = T/g` con `T` el potencial perturbador.

🎯 **Por qué importa (clase B53-C04):** Una altura solo tiene sentido respecto de una superficie de referencia. La decisión central: ¿contra qué superficie se mide la altura y cuánto se aparta el geoide de ella?

📘 **Dónde se aprende** (1 clase): [B53-C04 · Geoides y elipsoides](../programa/clases/B53/B53-C04-geoides-y-elipsoides/CLASE.md).

### Fórmula de Edelbaum

- La fórmula de Edelbaum da el `Δv` mínimo de una espiral con cambio de inclinación `Δi`: `Δv = √(v₀² − 2 v₀ v₁ cos(π/2 · Δi) + v₁²)`.

💡 **Cómo se explica en la clase [B81-C04](../programa/clases/B81/B81-C04-trayectorias-espirales-de-bajo-empuje/CLASE.md):**
- Con `Δi = 28,5°` la fórmula de Edelbaum da `5783,75 m/s`: 29,4 % más que el caso coplanar, con un tiempo de `66,942 d`.
- 🎯 **Por qué importa:** Una espiral de bajo empuje cuesta más `Δv` que un impulso (Hohmann) pero ahorra propelente por su alto `Isp`. La decisión central: ¿cuánto `Δv` y cuánto tiempo cuesta pasar de una órbita circular a otra, y cuánto más si además hay que cambiar el plano?

📘 **Dónde se aprende** (1 clase): [B81-C04 · Trayectorias espirales de bajo empuje](../programa/clases/B81/B81-C04-trayectorias-espirales-de-bajo-empuje/CLASE.md).

### Fórmula de Euler

- La fórmula de Euler es `e^{iθ} = cos θ + i sen θ`.

🎯 **Por qué importa (clase B15-C04):** Si una estrella pulsa con una pequeña amplitud en medio del ruido, mirar la curva de luz no la revela, pero su espectro de frecuencias sí: un pico a una frecuencia concreta. Lo mismo ocurre con una vibración en una estructura espacial, una señal de radio o un periodo en un registro geofísico.

📘 **Dónde se aprende** (1 clase): [B15-C04 · Transformada de Fourier](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md).

### Fórmula de Friis

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B49-C06):** Una décima de decibelio antes del primer amplificador cuesta más que mejorar el mezclador. La decisión central: ¿qué bloque domina la temperatura de ruido y qué pérdidas deben evitarse antes de él?

📘 **Dónde se aprende** (1 clase): [B49-C06 · Amplificadores de bajo ruido (LNA): tecnología, ganancia y adaptación](../programa/clases/B49/B49-C06-amplificadores-de-bajo-ruido-lna-tecnologia-ganancia-y-adaptacion/CLASE.md).

### Fórmula de Friis para el ruido

- La fórmula de Friis para el ruido da `T = T₁ + T₂/G₁ + T₃/(G₁G₂) + …`.

🎯 **Por qué importa (clase B89-C07):** La primera etapa de una cadena receptora decide casi todo el ruido: un amplificador de bajo ruido bien colocado vale muchos decibelios de `G/T`. La decisión central: ¿qué orden y qué componentes dan la menor temperatura de sistema y el mayor `G/T`?

📘 **Dónde se aprende** (1 clase): [B89-C07 · Figura de ruido de receptor](../programa/clases/B89/B89-C07-figura-de-ruido-de-receptor/CLASE.md).

### Fórmula de Kasten y Young

- La fórmula de Kasten y Young `X = 1/[cos z + 0,50572 (96,07995 − z)^−1,6364]`.
- La fórmula de Kasten y Young corrige la curvatura.

🎯 **Por qué importa (clase B45-C20):** Una campaña mal planificada gasta noches sin llegar a la precisión pedida. La decisión central: ¿cuánto exponer, durante cuánto tiempo y con qué precisión por punto?

📘 **Dónde se aprende** (2 clases): [B45-C20 · Campaña fotométrica o espectroscópica](../programa/clases/B45/B45-C20-campana-fotometrica-o-espectroscopica/CLASE.md); [B45-C22 · Extinción atmosférica, masa de aire y coeficientes de color](../programa/clases/B45/B45-C22-extincion-atmosferica-masa-de-aire-y-coeficientes-de-color/CLASE.md).

### Fórmula de Rodrigues

- La fórmula de Rodrigues da la rotación de ángulo `θ` alrededor de `u`: `R = I + sin θ K + (1 − cos θ) K²`.

🎯 **Por qué importa (clase B10-C13):** La actitud de un satélite (hacia dónde apuntan sus ejes) se guarda como una matriz de rotación: sus columnas son los ejes del cuerpo expresados en el sistema inercial. Con ella, un seguidor estelar, un panel o una antena se orientan sin ambigüedad.

📘 **Dónde se aprende** (1 clase): [B10-C13 · Matrices de rotación tridimensional](../programa/clases/B10/B10-C13-matrices-de-rotacion-tridimensional/CLASE.md).

### Fórmula de Ruze

- La fórmula de Ruze da la eficiencia por superficie `exp(−(4πε/λ)²)`.

🎯 **Por qué importa (clase B91-C04):** Una malla desplegable pesa poco y cabe plegada, pero su precisión de forma limita la frecuencia útil. La decisión central: ¿hasta qué frecuencia vale la pena usar un reflector con un error de superficie dado, y qué término del presupuesto de error conviene reducir?

📘 **Dónde se aprende** (1 clase): [B91-C04 · Antenas desplegables y estructuras de gran apertura](../programa/clases/B91/B91-C04-antenas-desplegables-y-estructuras-de-gran-apertura/CLASE.md).

### Fórmula empírica

- Una fórmula empírica da la proporción más simple entre los átomos (CH₂ para el eteno y el ciclohexano).

💡 **Cómo se explica en la clase [B06-C07](../programa/clases/B06/B06-C07-estequiometria-elemental/CLASE.md):**
- ⚠️ **Error frecuente:** Pensar que la fórmula empírica es la molecular. Se corrige con el ejercicio 8.
- 🎯 **Por qué importa:** Si quieres saber cuánto pesa una columna de atmósfera de Marte, necesitas su masa molar media, y para eso, su composición. La NASA publica la composición en volumen de las atmósferas de Marte, Venus y la Tierra y también un «peso molecular» medio (S1, S2, S3).

📘 **Dónde se aprende** (1 clase): [B06-C07 · Estequiometría elemental](../programa/clases/B06/B06-C07-estequiometria-elemental/CLASE.md).

### Fórmula molecular

- Una fórmula molecular dice cuántos átomos de cada elemento tiene una molécula (H₂O, CO₂).

🎯 **Por qué importa (clase B06-C07):** Si quieres saber cuánto pesa una columna de atmósfera de Marte, necesitas su masa molar media, y para eso, su composición. La NASA publica la composición en volumen de las atmósferas de Marte, Venus y la Tierra y también un «peso molecular» medio (S1, S2, S3).

📘 **Dónde se aprende** (1 clase): [B06-C07 · Estequiometría elemental](../programa/clases/B06/B06-C07-estequiometria-elemental/CLASE.md).

### Fórmula plana

- La fórmula plana `v² sen 2θ/g` supone gravedad uniforme y superficie plana.

💡 **Cómo se explica en la clase [B59-C17](../programa/clases/B59/B59-C17-impacto-ambiental-extraterrestre/CLASE.md):**
- La fórmula plana falla cuando el alcance es comparable al radio: la superficie se curva y la gravedad cambia con la altura.
- *Descripción textual:* la velocidad y el ángulo se integran con gravedad central; el alcance se compara con la fórmula plana; una distribución de velocidades da fracciones.
- ⚠️ **Error frecuente:** Usar la fórmula plana a alcances grandes. Se corrige con 8.2.
- 🎯 **Por qué importa:** Sin atmósfera, la eyecta viaja lejos y sin frenar. La decisión central: ¿a qué distancia de una zona sensible, como una sombra permanente, hay que operar para que la eyecta no la alcance?

📘 **Dónde se aprende** (1 clase): [B59-C17 · Impacto ambiental extraterrestre](../programa/clases/B59/B59-C17-impacto-ambiental-extraterrestre/CLASE.md).

### Forsterita

- Un mineral es un sólido cristalino natural de composición química definida: el olivino `(Mg,Fe)₂SiO₄` es una serie entre la forsterita `Mg₂SiO₄` y la fayalita `Fe₂SiO₄`; el piroxeno más sencillo es `MgSiO₃`; la calcita es `CaCO₃`.
- La forsterita (Mg₂SiO₄) y la fayalita (Fe₂SiO₄) son los extremos del olivino; la enstatita (MgSiO₃) es un piroxeno.

💡 **Cómo se explica en la clase [B06-C19](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md):**
- Con los pesos atómicos de la NIST (C03): `H₂O = 18,0153`, `CO₂ = 44,0094`, `NH₃ = 17,0308`, forsterita `Mg₂SiO₄ = 2 × 24,3055 + 28,085 + 4 × 15,9994 = 140,6936`, fayalita `Fe₂SiO₄ = 203,7726`, piroxeno `MgSiO₃ = 100,3887` y calcita `CaCO₃ = 100,0868 g/mol`.
- El magnesio es el 34,55 % de la masa de la forsterita.
- 🎯 **Por qué importa:** Los estudios con el telescopio James Webb muestran que las nubes densas del medio interestelar tienen granos de polvo cubiertos de hielos con una variedad de moléculas, y que esos hielos contienen entre el 2 y el 19 % del carbono, oxígeno, nitrógeno y azufre disponibles (S1, resumen).

📘 **Dónde se aprende** (2 clases): [B06-C19 · Química de hielos y minerales](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md); [B55-C12 · Geoquímica de meteoritos](../programa/clases/B55/B55-C12-geoquimica-de-meteoritos/CLASE.md).

### Fotodesorción

- La fotodesorción es la expulsión de moléculas de un hielo por absorción de fotones.

🎯 **Por qué importa (clase B68-C02):** Si un hielo de CO a 15 K es estable térmicamente durante millones de años, la presencia de CO gaseoso en regiones frías exige otro mecanismo. La decisión central: ¿cuántas moléculas expulsa cada fotón y de qué depende ese número?

📘 **Dónde se aprende** (1 clase): [B68-C02 · Fotodesorción de hielos interestelares](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md).

### Fotoevaporación

- La fotoevaporación es la pérdida de gas calentado por radiación.

💡 **Cómo se explica en la clase [B52-C09](../programa/clases/B52/B52-C09-dispersion-de-discos-de-gas/CLASE.md):**
- Más tarde la fotoevaporación domina y limpia el disco rápidamente.
- E --> P["Mdot frente a fotoevaporación"]
- 🎯 **Por qué importa:** La vida del gas fija cuánto tiempo hay para formar núcleos, gigantes y migración. La decisión central: ¿cuánto tarda un disco en perder su gas y cómo se comprueba un esquema numérico de difusión?

📘 **Dónde se aprende** (1 clase): [B52-C09 · Dispersión de discos de gas](../programa/clases/B52/B52-C09-dispersion-de-discos-de-gas/CLASE.md).

### Fotólisis

- La fotólisis es la ruptura de moléculas en el volumen del hielo.

💡 **Cómo se explica en la clase [B68-C02](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md):**
- Öberg y colaboradores ajustan el espesor frente a la fluencia con la suma de una función lineal (orden cero, la desorción de superficie) y una exponencial (primer orden, la fotólisis).
- `Y = 2,7 × 10⁻³`) y ruido gaussiano de 0,02 ML con semilla fija, el ajuste recupera `Y = 2,701 × 10⁻³` y `σ = 0,35`, mientras que una recta sola da `3,182 × 10⁻³`, un sesgo de `+17,9 %` porque atribuye a la desorción la pérdida por fotólisis.
- 🎯 **Por qué importa:** Si un hielo de CO a 15 K es estable térmicamente durante millones de años, la presencia de CO gaseoso en regiones frías exige otro mecanismo. La decisión central: ¿cuántas moléculas expulsa cada fotón y de qué depende ese número?

📘 **Dónde se aprende** (1 clase): [B68-C02 · Fotodesorción de hielos interestelares](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md).

### Fotometría de apertura

- La fotometría de apertura suma el flujo dentro de un círculo.
- La fotometría de apertura suma el flujo dentro de un círculo y resta el cielo de un anillo.

🎯 **Por qué importa (clase B29-C02):** Una apertura pequeña pierde estrella; una grande suma cielo y ruido de lectura. La decisión central: ¿qué apertura maximiza la relación señal-ruido y qué error en magnitud implica?

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

📘 **Dónde se aprende** (5 clases): [B05-C18 · Electromagnetismo y radiación](../programa/clases/B05/B05-C18-electromagnetismo-y-radiacion/CLASE.md); [B06-C01 · Estructura atómica](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md); [B26-C05 · Equivalencia entre masa y energía](../programa/clases/B26/B26-C05-equivalencia-entre-masa-y-energia/CLASE.md); [B44-C01 · Principios fotoeléctricos](../programa/clases/B44/B44-C01-principios-fotoelectricos/CLASE.md); [B45-C01 · Radiometría y fotometría](../programa/clases/B45/B45-C01-radiometria-y-fotometria/CLASE.md).

### Fotón de señal

- Un fotón de señal viene del láser reflejado; uno de fondo viene del Sol o del ruido del detector.

🎯 **Por qué importa (clase B57-C11):** Un láser mide alturas con precisión de centímetros, pero a la luz del día el fondo solar inunda el detector. La decisión central: ¿cuántos fotones de señal hacen falta para distinguir la superficie del ruido y con qué error?

📘 **Dónde se aprende** (1 clase): [B57-C11 · LiDAR satelital](../programa/clases/B57/B57-C11-lidar-satelital/CLASE.md).

### Fotón detectado

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C03):** En el ultravioleta cada fotón es valioso: las tasas son bajas y el ruido es de Poisson. La decisión central: ¿cuánto hay que exponer para llegar a una relación señal/ruido de 10?

📘 **Dónde se aprende** (1 clase): [B47-C03 · Telescopios ultravioleta](../programa/clases/B47/B47-C03-telescopios-ultravioleta/CLASE.md).

### Fotones por bit

- Los fotones por bit miden la eficiencia energética.

💡 **Cómo se explica en la clase [B89-C18](../programa/clases/B89/B89-C18-comunicaciones-opticas-espaciales/CLASE.md):**
- En un enlace sintético a la Luna (0,5 W, 10 cm y 40 cm, 1550 nm) llegan `1,08e+10 fotones/s`; con 16-PPM y ranuras de 1 ns, la tasa es `125,0 Mbit/s` con `8,68e+01` fotones por bit.
- 🎯 **Por qué importa:** Las comunicaciones ópticas prometen más tasa por masa y potencia que la radio; entender el presupuesto de fotones y la modulación por posición de pulso explica por qué y a qué costo (apuntamiento, nubes). La decisión central: ¿cuántos fotones por bit llegan y qué error de símbolo implica la modulación PPM elegida?

📘 **Dónde se aprende** (1 clase): [B89-C18 · Comunicaciones ópticas espaciales](../programa/clases/B89/B89-C18-comunicaciones-opticas-espaciales/CLASE.md).

### Fotones por O₂

- Los fotones por O₂ resumen la eficiencia del cultivo, incluida la absorción incompleta.

💡 **Cómo se explica en la clase [B59-C14](../programa/clases/B59/B59-C14-agricultura-y-sustratos-artificiales/CLASE.md):**
- O2["O₂ por persona"] --> F["× fotones por O₂"]
- Con `20` fotones por O₂ producido, `400 µmol/(m²·s)` durante `16 h/día` y LED de `2,5 µmol/J`, el área es `22,79 m²`, la potencia instantánea `3,65 kW` (media `2,43 kW`) y el agua evapotranspirada `68,4 kg/día`, de los que solo se repone `3,42 kg/día` con recuperación del `95 %`.
- 🎯 **Por qué importa:** Cultivar exige luz, y la luz eléctrica cuesta potencia. La decisión central: ¿cuántos metros cuadrados y cuántos kilovatios necesita un cultivo para producir el oxígeno de una persona?

📘 **Dónde se aprende** (1 clase): [B59-C14 · Agricultura y sustratos artificiales](../programa/clases/B59/B59-C14-agricultura-y-sustratos-artificiales/CLASE.md).

### Fotoperiodo

- El fotoperiodo son las horas de luz por día.

💡 **Cómo se explica en la clase [B115-C02](../programa/clases/B115/B115-C02-iluminacion-de-cultivos-con-led-y-espectro-de-crecimiento/CLASE.md):**
- M["meta de DLI<br/>mol/m2/d"] --> F["PPFD x fotoperiodo"]
- 🎯 **Por qué importa:** La luz es el mayor consumo eléctrico de un cultivo cerrado. La decisión central: ¿cuántos fotones por metro cuadrado y día hacen falta, con qué eficacia se producen y qué potencia y calor suponen para el hábitat?

📘 **Dónde se aprende** (1 clase): [B115-C02 · Iluminación de cultivos con LED y espectro de crecimiento](../programa/clases/B115/B115-C02-iluminacion-de-cultivos-con-led-y-espectro-de-crecimiento/CLASE.md).

### Fotopletismografía (PPG)

- La fotopletismografía (PPG) mide con luz los cambios de volumen de sangre en la piel.

🎯 **Por qué importa (clase B116-C01):** Una pulsera que da «72 lpm» no dice «72 ± 0,1». Con movimiento puede dar 120 cuando el pulso real es 70.

📘 **Dónde se aprende** (1 clase): [B116-C01 · Sensores fisiológicos y wearables para vuelo](../programa/clases/B116/B116-C01-sensores-fisiologicos-y-wearables-para-vuelo/CLASE.md).

### Fotoquímica

- La fotoquímica es la que inicia una excitación electrónica inducida por un fotón sin ionizar; la química de radiación estudia los cambios por absorción de radiación capaz de ionizar (definiciones de Arumainayagam y colaboradores).
- La fotoquímica estudia las reacciones provocadas por la absorción de luz.

💡 **Cómo se explica en la clase [B68-C03](../programa/clases/B68/B68-C03-irradiacion-de-hielos-por-rayos-cosmicos-y-uv-radiolisis-y-productos/CLASE.md):**
- Arumainayagam y colaboradores (2019) definen la química de radiación como el estudio de los cambios por absorción de radiación con energía suficiente para ionizar y la fotoquímica como la iniciada por excitación electrónica sin ionización.
- 🎯 **Por qué importa:** Un hielo en una nube densa recibe poca luz ultravioleta externa, pero sigue recibiendo partículas energéticas y fotones secundarios. Esas dosis lentas transforman la composición del hielo durante millones de años.

📘 **Dónde se aprende** (2 clases): [B06-C18 · Fotoquímica y radiación](../programa/clases/B06/B06-C18-fotoquimica-y-radiacion/CLASE.md); [B68-C03 · Irradiación de hielos por rayos cósmicos y UV: radiólisis y productos](../programa/clases/B68/B68-C03-irradiacion-de-hielos-por-rayos-cosmicos-y-uv-radiolisis-y-productos/CLASE.md).

### Fotosfera

- La fotosfera es la capa de donde sale la mayor parte de la luz, `τ ≈ 2/3`.
- La fotosfera es la capa que emite la luz visible; la cromosfera y la corona están encima.
- La fotosfera es donde `τ = 2/3`.

💡 **Cómo se explica en la clase [B24-C09](../programa/clases/B24/B24-C09-atmosferas-y-opacidades/CLASE.md):**
- La composición de la fotosfera es un asunto de actualidad: se ha revisado a la baja la abundancia de carbono, nitrógeno, oxígeno y neón (S4, resumen), con consecuencias para la opacidad del interior.
- 🎯 **Por qué importa:** Toda temperatura o composición que atribuimos a una estrella se infiere de una capa delgada. Saber de qué profundidad viene la luz, cuánto vale la opacidad y cuánto puede brillar una estrella sin expulsar su atmósfera es lo que permite interpretar espectros (C10) y entender los vientos (C17).

📘 **Dónde se aprende** (3 clases): [B24-C09 · Atmósferas y opacidades](../programa/clases/B24/B24-C09-atmosferas-y-opacidades/CLASE.md); [B30-C02 · Fotosfera, cromosfera y corona](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md); [B37-C04 · Condiciones de frontera centrales y superficiales en modelos estelares](../programa/clases/B37/B37-C04-condiciones-de-frontera-centrales-y-superficiales-en-modelos-estelares/CLASE.md).

### FPP

- La FPP es la probabilidad de falso positivo.

💡 **Cómo se explica en la clase [B29-C07](../programa/clases/B29/B29-C07-metodos-de-validacion-planetaria/CLASE.md):**
- Con un solo observable débil, el FPP mínimo es `0,21`: no se puede validar.
- ⚠️ **Error frecuente:** Dar por validado un FPP alto. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Hay muchos más candidatos que posibilidades de seguimiento. Validar bien exige probabilidades honestas: ni optimistas ni conservadoras en exceso.

📘 **Dónde se aprende** (1 clase): [B29-C07 · Métodos de validación planetaria](../programa/clases/B29/B29-C07-metodos-de-validacion-planetaria/CLASE.md).

### Fracción

- La fracción `f` es la parte del píxel cubierta por lava caliente.
- Una fracción `a/b` expresa `a` partes de un todo dividido en `b` partes iguales;

💡 **Cómo se explica en la clase [B03-C02](../programa/clases/B03/B03-C02-fracciones-y-razones-de-magnitudes/CLASE.md):**
- Esto funciona porque dividir numerador y denominador entre `k` equivale a multiplicar la fracción por `(1/k)/(1/k) = 1`, que no la cambia.
- 🎯 **Por qué importa:** Una cifra aislada como «69 911 km» no dice si Júpiter es grande o pequeño. Una razón sí: Júpiter tiene un radio unas 11 veces el terrestre.

📘 **Dónde se aprende** (2 clases): [B03-C02 · Fracciones y razones de magnitudes](../programa/clases/B03/B03-C02-fracciones-y-razones-de-magnitudes/CLASE.md); [B70-C05 · Actividad volcánica venusina: llanuras, coronas e indicios de actividad reciente](../programa/clases/B70/B70-C05-actividad-volcanica-venusina-llanuras-coronas-e-indicios-de-actividad-reciente/CLASE.md).

### Fracción absorbida

- La fracción absorbida es `1 − T`.

💡 **Cómo se explica en la clase [B54-C12](../programa/clases/B54/B54-C12-interaccion-con-radiacion-solar/CLASE.md):**
- Transmisión y fracción absorbida: `τ = 0,1`, `χ = 0°`: `0,9048` y `0,0952`;
- 🎯 **Por qué importa:** La radiación solar es la fuente de energía de todo el bloque. La pregunta motivadora: ¿cuánta energía llega a un punto y cuánta alcanza el suelo?

📘 **Dónde se aprende** (1 clase): [B54-C12 · Interacción con radiación solar](../programa/clases/B54/B54-C12-interaccion-con-radiacion-solar/CLASE.md).

### Fracción comestible

- Eficiencia de uso de la luz: g de biomasa por mol de fotones. Fracción comestible: parte aprovechada.

🎯 **Por qué importa (clase B106-C12):** Cultivar reduce la masa de alimento a lanzar y devuelve oxígeno, pero cuesta mucha área y electricidad. La decisión central: ¿qué fracción de la dieta compensa cultivar dado el costo en área y energía?

📘 **Dónde se aprende** (1 clase): [B106-C12 · Agricultura en ambiente controlado](../programa/clases/B106/B106-C12-agricultura-en-ambiente-controlado/CLASE.md).

### Fracción convertida

- La fracción convertida es `V_e²/V_max²`.

🎯 **Por qué importa (clase B79-C13):** El concepto de energía de flujo es la base del análisis de motores; ninguna clase del tronco lo trata. Con `h₀` se obtiene el límite de velocidad de escape y se entiende por qué la temperatura total no cambia en un choque.

📘 **Dónde se aprende** (1 clase): [B79-C13 · Entalpía de flujo y entalpía total](../programa/clases/B79/B79-C13-entalpia-de-flujo-y-entalpia-total/CLASE.md).

### Fracción de área

- La fracción de área `p` es la parte del terreno ocupada por una litología.

💡 **Cómo se explica en la clase [B63-C02](../programa/clases/B63/B63-C02-muestreo-superficial-y-estrategias-de-recoleccion/CLASE.md):**
- ⚠️ **Error frecuente:** Tomar la fracción de área como fracción de masa. Son cosas distintas.
- 🎯 **Por qué importa:** Un rover tiene un número limitado de tubos. La decisión central: ¿cuántas muestras hacen falta para no perderse una litología rara con una confianza dada?

📘 **Dónde se aprende** (1 clase): [B63-C02 · Muestreo superficial y estrategias de recolección](../programa/clases/B63/B63-C02-muestreo-superficial-y-estrategias-de-recoleccion/CLASE.md).

### Fracción de carga útil

- La fracción de carga útil de una etapa es `(1/r − e)/(1 − e)`.

💡 **Cómo se explica en la clase [B124-C23](../programa/clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md):**
- `e` 0,07 y 0,09) la fracción de carga útil es `0,02413`: de cada 100 kg en la plataforma, menos de `2,4` llegan como carga.
- 🎯 **Por qué importa:** El costo por kilogramo a superficie no se puede leer en una lista de precios: depende de una cadena de fracciones de masa que se multiplican. La decisión central: ¿cuánto cuesta llevar un kilogramo a la superficie, de qué depende ese costo y qué lo hace más sensible?

📘 **Dónde se aprende** (1 clase): [B124-C23 · Costos de transporte por kilogramo a superficie](../programa/clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md).

### Fracción de Carnot

- La fracción de Carnot `f` mide la calidad del ciclo.
- La fracción de Carnot `η` relaciona la potencia real con la ideal: `P = Q/(η COP)`.

💡 **Cómo se explica en la clase [B85-C17](../programa/clases/B85/B85-C17-criogenia-de-instrumentos/CLASE.md):**
- Límite: las propiedades varían con `T` de forma más compleja y la fracción de Carnot real cae con la temperatura.
- Descripción larga: la MLI reduce la carga unas 300 veces; a 80 K cada vatio parásito cuesta 27 W eléctricos con esta fracción de Carnot.
- 🎯 **Por qué importa:** Cada vatio parásito a `80 K` cuesta decenas de vatios eléctricos. La decisión central: ¿qué carga parásita llega a la punta fría, cuánta potencia eléctrica cuesta quitarla y cuánto tarda el enfriamiento?

📘 **Dónde se aprende** (2 clases): [B85-C17 · Criogenia de instrumentos](../programa/clases/B85/B85-C17-criogenia-de-instrumentos/CLASE.md); [B86-C17 · Energía nuclear espacial conceptual](../programa/clases/B86/B86-C17-energia-nuclear-espacial-conceptual/CLASE.md).

### Fracción de cielo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B40-C12](../programa/clases/B40/B40-C12-analisis-de-mapas-del-cmb-pixelizacion-esferica-y-mascaras/CLASE.md):**
- El error de la fracción de cielo baja unas 8 veces al cuadruplicar `N_side`: el borde de la máscara cae en la discretización por anillos.
- La ida y vuelta es exacta para `N_side = 1…16`, `χ²/gl = 0,958` con 153 600 puntos y la fracción de cielo de un corte de 20° da `0,65755` frente a `0,65798` analítico.
- ⚠️ **Error frecuente:** Contar fracción de cielo con pocos pixeles. Se corrige con 8.3.
- 🎯 **Por qué importa:** Sin una pixelización de área igual, el ruido y las estadísticas dependen de la posición. La decisión central: ¿cuántos pixeles, de qué tamaño, y cómo se cuenta la fracción de cielo de una máscara?

📘 **Dónde se aprende** (1 clase): [B40-C12 · Análisis de mapas del CMB: pixelización esférica y máscaras](../programa/clases/B40/B40-C12-analisis-de-mapas-del-cmb-pixelizacion-esferica-y-mascaras/CLASE.md).

### Fracción de colimación

- La fracción de colimación `f_b = 1 − cos θ_j`.

🎯 **Por qué importa (clase B27-C17):** Una explosión que parece de energía enorme puede ser de energía moderada vista de frente, y un retardo de segundos entre dos mensajeros, tras viajar 130 millones de años, es una medición extraordinariamente precisa. La decisión central: ¿qué retardo y qué energía real implican un factor de Lorentz y un ángulo dados?

📘 **Dónde se aprende** (1 clase): [B27-C17 · Explosiones de rayos gamma](../programa/clases/B27/B27-C17-explosiones-de-rayos-gamma/CLASE.md).

### Fracción de contaminante

- La fracción de contaminante `f` es la parte de la medida que no es de la muestra.

💡 **Cómo se explica en la clase [B63-C03](../programa/clases/B63/B63-C03-curaduria-y-cadena-de-custodia-de-muestras/CLASE.md):**
- Si el contaminante tiene concentración `c_b` (el blanco), la muestra `c_m` y la medida es `c`, la fracción de contaminante es `f = (c − c_m)/(c_b − c_m)`.
- 🎯 **Por qué importa:** Una muestra planetaria es irrepetible y se estudia durante décadas. La decisión central: ¿cómo demuestras, años después, qué le pasó a una muestra y cuánto de lo que mides es suyo?

📘 **Dónde se aprende** (1 clase): [B63-C03 · Curaduría y cadena de custodia de muestras](../programa/clases/B63/B63-C03-curaduria-y-cadena-de-custodia-de-muestras/CLASE.md).

### Fracción de eclipse

- La fracción de eclipse es `f = (1/π) arccos(√(h² + 2Rh)/((R + h) cos β))` para `|β|` menor que `β* = asin(R/(R + h))`.
- Sombra cilíndrica: modelo de sombra sin penumbra. Fracción de eclipse: parte de la vuelta en sombra.

💡 **Cómo se explica en la clase [B76-C18](../programa/clases/B76/B76-C18-restricciones-de-iluminacion/CLASE.md):**
- *Descripción textual:* la geometría da la fracción de eclipse y el `β` crítico, que se verifican numéricamente; la fase de la aproximación V-bar y el eclipse dan la fracción de órbita utilizable.
- 🎯 **Por qué importa:** Una aproximación planificada de noche, o con el Sol detrás del objetivo, puede dejar ciego al sensor. La decisión central: ¿qué fracción de la órbita está al sol y con buena fase, según el ángulo `β`?

📘 **Dónde se aprende** (2 clases): [B76-C18 · Restricciones de iluminación](../programa/clases/B76/B76-C18-restricciones-de-iluminacion/CLASE.md); [B96-C11 · Operación durante eclipse](../programa/clases/B96/B96-C11-operacion-durante-eclipse/CLASE.md).

### Fracción de gas

- La fracción de gas es `M_gas/M`.
- La fracción de gas `μ = M_gas/M_total`.

💡 **Cómo se explica en la clase [B25-C13](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md):**
- F["Perfil de gas"] --> G["M_gas(<r)"] --> H["Fracción de gas"]
- 🎯 **Por qué importa:** Los cúmulos de galaxias son las mayores estructuras ligadas por la gravedad. Contienen galaxias, un gas a decenas de millones de kelvin y mucha más masa de la que ambos aportan; por eso sirven para estudiar la materia oscura y poner a prueba el modelo cosmológico.

📘 **Dónde se aprende** (2 clases): [B25-C13 · Cúmulos de galaxias](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md); [B25-C17 · Metalicidad y evolución química](../programa/clases/B25/B25-C17-metallicidad-y-evolucion-quimica/CLASE.md).

### Fracción de helio

- La fracción de helio `Y_p` es la fracción de masa en helio-4.

🎯 **Por qué importa (clase B26-C16):** La cuarta parte de la masa bariónica del universo es helio, y la proporción casi no cambió desde los primeros minutos. Su valor da información sobre cuántas especies de neutrinos existen y sobre la densidad de bariones.

📘 **Dónde se aprende** (1 clase): [B26-C16 · Nucleosíntesis primordial](../programa/clases/B26/B26-C16-nucleosintesis-primordial/CLASE.md).

### Fracción de inercia

- La fracción de inercia `ζ` pesa cada región.

💡 **Cómo se explica en la clase [B37-C11](../programa/clases/B37/B37-C11-rotacion-interna-a-partir-del-desdoblamiento-de-frecuencias/CLASE.md):**
- *Descripción textual:* cada modo promedia la rotación según su fracción de inercia y varios modos permiten separar las dos zonas.
- 🎯 **Por qué importa:** El desdoblamiento promedia la rotación de las regiones que el modo explora. La decisión central: ¿cuánto giran el núcleo y la envoltura y con qué incertidumbre y correlación?

📘 **Dónde se aprende** (1 clase): [B37-C11 · Rotación interna a partir del desdoblamiento de frecuencias](../programa/clases/B37/B37-C11-rotacion-interna-a-partir-del-desdoblamiento-de-frecuencias/CLASE.md).

### Fracción de masa

- La fracción de masa `F(>M) = erfc(ν/√2)`.
- La fracción de masa usa `m ∝ D³`.

💡 **Cómo se explica en la clase [B36-C06](../programa/clases/B36/B36-C06-formacion-de-halos-y-funcion-de-masa/CLASE.md):**
- Es como una piscina con un borde: el agua (la densidad) sube al azar y la fracción de caminos que alguna vez pasan el borde es la fracción de masa en halos.
- *Descripción textual:* el colapso esférico fija el umbral, que junto con σ(M) da la fracción de masa y la función de masa; las caminatas lo verifican.
- ⚠️ **Error frecuente:** Olvidar el factor 2 de Press–Schechter. Se corrige con la fracción de masa.
- 🎯 **Por qué importa:** Contar halos exige un umbral de colapso y una función de masa. La decisión central: ¿cuánta masa del universo está en halos de más de cierta masa?

📘 **Dónde se aprende** (2 clases): [B36-C06 · Formación de halos y función de masa](../programa/clases/B36/B36-C06-formacion-de-halos-y-funcion-de-masa/CLASE.md); [B52-C13 · Pequeños cuerpos remanentes](../programa/clases/B52/B52-C13-pequenos-cuerpos-remanentes/CLASE.md).

### Fracción de masa convertida

- La fracción de masa convertida `ε = Δm/m` indica qué porción de la masa de combustible pasa a energía.
- La fracción de masa convertida `ε` es la porción de masa que se vuelve energía.
- La fracción de masa convertida es `E/(M c²)`.

💡 **Cómo se explica en la clase [B24-C08](../programa/clases/B24/B24-C08-nucleosintesis-estelar/CLASE.md):**
- La fracción de masa convertida es `ε = 6,50 × 10⁻⁴`; la del hidrógeno es `7,12 × 10⁻³`: cociente `10,9`.
- *Descripción textual:* el núcleo quema hidrógeno, luego helio (con una fracción de masa convertida unas once veces menor), luego combustibles más pesados en etapas cada vez más cortas, hasta el grupo del hierro, donde no se libera más energía.
- 🎯 **Por qué importa:** El carbono de tu cuerpo, el oxígeno que respiras y el hierro de tus huesos se forjaron en estrellas. Entender cómo, y cuánta energía rinde cada etapa, explica por qué la vida de una estrella se acorta con cada combustible y por qué el hierro es el final de la cadena.

📘 **Dónde se aprende** (3 clases): [B24-C06 · Fusión de hidrógeno](../programa/clases/B24/B24-C06-fusion-de-hidrogeno/CLASE.md); [B24-C08 · Nucleosíntesis estelar](../programa/clases/B24/B24-C08-nucleosintesis-estelar/CLASE.md); [B78-C16 · Propulsión de fusión como investigación](../programa/clases/B78/B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md).

### Fracción de nubes

- La fracción de nubes `k` descuenta el cielo cubierto.

🎯 **Por qué importa (clase B129-C03):** Cuarenta personas cuentan meteoros una noche: unos con un cielo más oscuro, otros bajo nubes, otros con el radiante bajo. La decisión central: ¿cómo se combinan sus recuentos en una sola tasa comparable, y con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B129-C03 · Seguimiento ciudadano de meteoros](../programa/clases/B129/B129-C03-seguimiento-ciudadano-de-meteoros/CLASE.md).

### Fracción de píxel

- La fracción de píxel `p` es la parte del píxel en llamas.

🎯 **Por qué importa (clase B57-C16):** Un incendio pequeño puede ser un desastre en horas, pero un píxel mide cientos de metros. La decisión central: ¿cuál es la fracción de píxel más pequeña que se puede detectar y cuánto sesga la estimación un error en el fondo?

📘 **Dónde se aprende** (1 clase): [B57-C16 · Incendios forestales](../programa/clases/B57/B57-C16-incendios-forestales/CLASE.md).

### Fracción de propelente

- La fracción de propelente es `1 − m_f/m₀`.

🎯 **Por qué importa (clase B05-C20):** Un problema real no viene etiquetado «esto es de energía» o «esto es de momento». La pregunta motivadora es: ¿cómo planteo, resuelvo y valido un problema físico completo, eligiendo el modelo correcto para cada parte y declarando dónde dejan de valer?

📘 **Dónde se aprende** (1 clase): [B05-C20 · Problema físico integrado de satélite ideal](../programa/clases/B05/B05-C20-problema-fisico-integrado-de-satelite-ideal/CLASE.md).

### Fracción de propergol

- La fracción de propergol es `1 − exp(−Δv/(Isp g0))`.

🎯 **Por qué importa (clase B76-C07):** Un diseño preliminar de misión empieza por el presupuesto de velocidad. La decisión central: ¿cuánto `Δv` cuestan la salida de la Tierra y la captura en la Luna, y cuánto cambia la segunda según la órbita lunar elegida?

📘 **Dónde se aprende** (1 clase): [B76-C07 · Maniobras de inserción cislunar](../programa/clases/B76/B76-C07-maniobras-de-insercion-cislunar/CLASE.md).

### Fracción de propulsante

- La fracción de propulsante es `1 − e^{−Δv/(I_sp g₀)}`.

💡 **Cómo se explica en la clase [B75-C11](../programa/clases/B75/B75-C11-propulsion-de-bajo-empuje/CLASE.md):**
- *Descripción textual:* Se integra la espiral hasta el radio de Marte; el tiempo y la aceleración dan el delta-v; se compara con Edelbaum y se convierte en fracción de propulsante.
- Fracción de propulsante: la ecuación del cohete con `I_sp` alta frente a baja.
- 🎯 **Por qué importa:** Un motor de alta `I_sp` ahorra propulsante pero tarda mucho. La decisión central: ¿cuánto delta-v y cuánto tiempo cuesta una espiral y cuándo es válida la fórmula de Edelbaum?

📘 **Dónde se aprende** (1 clase): [B75-C11 · Propulsión de bajo empuje](../programa/clases/B75/B75-C11-propulsion-de-bajo-empuje/CLASE.md).

### Fracción de reserva

- La fracción de reserva es `(FC − FC_reposo)/(FC_máx − FC_reposo)`.

💡 **Cómo se explica en la clase [B104-C04](../programa/clases/B104/B104-C04-acondicionamiento-fisico-general/CLASE.md):**
- Con FC de reposo 55 y máxima 190 lpm (valores de ejemplo), a 140 lpm la fracción de reserva es `(140−55)/135 = 0,630` y la carga de 30 min `30·0,630·0,64·e^(1,92·0,630) = 40,5` unidades; a 110 lpm, 17,1; a 165 lpm, 74,8.
- Paso 1 · Fracción de reserva. `(140 − 55)/(190 − 55) = 0,630`.
- 🎯 **Por qué importa:** Entrenar más no siempre significa rendir más el día que importa. La decisión central: ¿cómo distribuir una misma carga total para llegar con la mejor combinación de aptitud y fatiga?

📘 **Dónde se aprende** (1 clase): [B104-C04 · Acondicionamiento físico general](../programa/clases/B104/B104-C04-acondicionamiento-fisico-general/CLASE.md).

### Fracción de tanques

- La fracción de tanques `k` es la masa de tanque por kilo de propelente.

💡 **Cómo se explica en la clase [B78-C02](../programa/clases/B78/B78-C02-propulsion-quimica-como-sistema-fisico/CLASE.md):**
- Descripción larga: el Δv crece con el logaritmo de la razón de masas y tiene una cota que depende solo de la fracción de tanques y del `Isp`.
- 🎯 **Por qué importa:** Más propelente da más Δv, pero cada kilo de propelente exige tanques, y esos tanques también se aceleran. La decisión central: ¿cuánto propelente hace falta para un Δv dado y existe un máximo de Δv que ninguna cantidad de propelente supera?

📘 **Dónde se aprende** (2 clases): [B78-C02 · Propulsión química como sistema físico](../programa/clases/B78/B78-C02-propulsion-quimica-como-sistema-fisico/CLASE.md); [B78-C17 · Masa de propelente y presupuesto](../programa/clases/B78/B78-C17-masa-de-propelente-y-presupuesto/CLASE.md).

### Fracción del cielo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B28-C11](../programa/clases/B28/B28-C11-coincidencias-entre-observatorios/CLASE.md):**
- *Descripción textual:* la tasa y la ventana dan el número medio de eventos de fondo; el área da la fracción del cielo; su producto, en una distribución de Poisson, da la probabilidad fortuita, que se verifica por simulación.
- 🎯 **Por qué importa:** Que dos señales coincidan no prueba que estén relacionadas: la pregunta es cuán probable es la coincidencia por azar. Una probabilidad fortuita muy baja es lo que convierte una coincidencia en un descubrimiento.

📘 **Dónde se aprende** (1 clase): [B28-C11 · Coincidencias entre observatorios](../programa/clases/B28/B28-C11-coincidencias-entre-observatorios/CLASE.md).

### Fracción dirigida

- La fracción dirigida `f` es la parte de la energía que queda como energía cinética del escape.

💡 **Cómo se explica en la clase [B78-C16](../programa/clases/B78/B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md):**
- *Descripción textual:* la energía por reacción y la masa de los reactivos dan la energía específica; ésta da la fracción de masa convertida y, con la fracción dirigida, la cota de escape, que se contrasta con la relativista; con una potencia dada se calcula el consumo.
- ⚠️ **Error frecuente:** Olvidar la fracción dirigida. Se corrige con 8.2.
- 🎯 **Por qué importa:** Si la energía por kilo es millones de veces mayor, el escape posible es enorme; pero eso es una cota, no un propulsor. La decisión central: ¿cuánta energía por kilo libera cada reacción y cuánto escape acotaría, según la fracción que se logre dirigir?

📘 **Dónde se aprende** (1 clase): [B78-C16 · Propulsión de fusión como investigación](../programa/clases/B78/B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md).

### Fracción disociada

- La fracción disociada `a` es la parte del amoníaco que se separa en nitrógeno e hidrógeno.

💡 **Cómo se explica en la clase [B78-C04](../programa/clases/B78/B78-C04-propulsion-monopropelente-conceptual/CLASE.md):**
- *Descripción textual:* el propelente se descompone en amoníaco y nitrógeno liberando calor; la fracción disociada fija la temperatura (baja) y la masa molar (baja); ambas determinan el escape.
- 🎯 **Por qué importa:** La descomposición de un monopropelente tiene dos pasos: uno que libera calor y otro que lo absorbe. La decisión central: ¿conviene que el amoníaco intermedio se disocie del todo, por la menor masa molar, o que se conserve, por la mayor temperatura?

📘 **Dónde se aprende** (1 clase): [B78-C04 · Propulsión monopropelente conceptual](../programa/clases/B78/B78-C04-propulsion-monopropelente-conceptual/CLASE.md).

### Fracción en masa

- La fracción en número es `N_i / ΣN`; la fracción en masa es `N_i m_i / ΣN_j m_j`.

💡 **Cómo se explica en la clase [B55-C01](../programa/clases/B55/B55-C01-abundancia-quimica-cosmica/CLASE.md):**
- Por fracción en masa: natural para la dinámica y la estructura.
- ⚠️ **Error frecuente:** Olvidar que la fracción en masa depende de las masas atómicas. Se aplica 8.3.
- 🎯 **Por qué importa:** Cualquier modelo químico del espacio parte de una composición inicial: cuánto hidrógeno, helio, carbono u oxígeno hay. Las fuentes dan esa composición en una escala logarítmica poco intuitiva, y los modelos piden fracciones en número o en masa.

📘 **Dónde se aprende** (1 clase): [B55-C01 · Abundancia química cósmica](../programa/clases/B55/B55-C01-abundancia-quimica-cosmica/CLASE.md).

### Fracción en número

- La fracción en número es `N_i / ΣN`; la fracción en masa es `N_i m_i / ΣN_j m_j`.

💡 **Cómo se explica en la clase [B55-C01](../programa/clases/B55/B55-C01-abundancia-quimica-cosmica/CLASE.md):**
- Paso 3 · Fracción en número de O. `5,012 × 10⁻⁴ / 1,0803 = 4,639 × 10⁻⁴`.
- Por fracción en número: natural para la química (reacciones entre átomos).
- 🎯 **Por qué importa:** Cualquier modelo químico del espacio parte de una composición inicial: cuánto hidrógeno, helio, carbono u oxígeno hay. Las fuentes dan esa composición en una escala logarítmica poco intuitiva, y los modelos piden fracciones en número o en masa.

📘 **Dónde se aprende** (1 clase): [B55-C01 · Abundancia química cósmica](../programa/clases/B55/B55-C01-abundancia-quimica-cosmica/CLASE.md).

### Fracción encerrada

- La fracción encerrada continua es `1 − exp(−r²/2σ²)`.

💡 **Cómo se explica en la clase [B45-C23](../programa/clases/B45/B45-C23-fotometria-de-apertura-y-estimacion-del-cielo/CLASE.md):**
- *Descripción textual:* la fracción encerrada y el ruido del cielo compiten y dan un máximo de S/N en un radio cercano a la FWHM.
- 🎯 **Por qué importa:** Una apertura pequeña pierde flujo y una grande añade ruido de cielo. La decisión central: ¿qué radio da el mejor S/N y cómo se mide el cielo?

📘 **Dónde se aprende** (1 clase): [B45-C23 · Fotometría de apertura y estimación del cielo](../programa/clases/B45/B45-C23-fotometria-de-apertura-y-estimacion-del-cielo/CLASE.md).

### Fracción estacional

- La fracción estacional compara el rango de presión con la media.

💡 **Cómo se explica en la clase [B54-C14](../programa/clases/B54/B54-C14-atmosfera-de-marte/CLASE.md):**
- P["P media, rango"] --> F["fracción estacional"]
- 🎯 **Por qué importa:** La presión marciana varía unas decenas de por ciento durante el año porque parte del CO₂ se condensa en los casquetes polares. La pregunta motivadora: ¿cuánta masa de CO₂ participa en ese ciclo?

📘 **Dónde se aprende** (1 clase): [B54-C14 · Atmósfera de Marte](../programa/clases/B54/B54-C14-atmosfera-de-marte/CLASE.md).

### Fracción estructural

- La fracción estructural `ε` es la estructura sobre el propelente de la etapa en este modelo.

💡 **Cómo se explica en la clase [B100-C02](../programa/clases/B100/B100-C02-dimensionamiento-de-carga-y-volumen-de-mision/CLASE.md):**
- Límite: cada tramo usa una etapa nueva con fracción estructural constante; en una misión real las etapas se reutilizan o se dimensionan por separado.
- Con tres tramos de Δv ilustrativos (3,1 + 0,9 + 1,9 km/s), `Isp = 450 s` y fracción estructural 0,10, hacen falta `3924,7 kg` en órbita baja: un factor `4,584`.
- 🎯 **Por qué importa:** La masa que llega a la superficie es una fracción pequeña de la que sale de la Tierra, y el volumen puede decidir antes que la masa. La decisión central: ¿cuánta masa y cuánto volumen hay que cargar para N personas durante D días, y cuánta masa hay que lanzar para que esa carga llegue?

📘 **Dónde se aprende** (1 clase): [B100-C02 · Dimensionamiento de carga y volumen de misión](../programa/clases/B100/B100-C02-dimensionamiento-de-carga-y-volumen-de-mision/CLASE.md).

### Fracción expuesta

- La fracción expuesta `c` es el área con abrasivo.

💡 **Cómo se explica en la clase [B84-C36](../programa/clases/B84/B84-C36-desgaste-abrasivo-por-regolito-en-mecanismos/CLASE.md):**
- ⚠️ **Error frecuente:** Olvidar la fracción expuesta. Se corrige con el ejercicio 4.
- 🎯 **Por qué importa:** Un sello de acero inoxidable bajo regolito pierde 1,8 mm en 1000 h con un 10 % del área expuesta a polvo, y uno de carburo de volframio pierde 0,18 µm: la elección de dureza decide si el mecanismo vive. La decisión central: ¿qué superficie y qué estrategia de protección permiten que un mecanismo sobreviva al regolito?

📘 **Dónde se aprende** (1 clase): [B84-C36 · Desgaste abrasivo por regolito en mecanismos](../programa/clases/B84/B84-C36-desgaste-abrasivo-por-regolito-en-mecanismos/CLASE.md).

### Fracción iluminada

- La fracción iluminada `f` es la parte del disco que se ve iluminada.
- La fracción iluminada `k` es la parte del disco visible que recibe luz solar.
- La fracción iluminada `k_f` es la parte del disco visible que está iluminada.

💡 **Cómo se explica en la clase [B01-C12](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md):**
- Si la edad es `a`, el ángulo es `2π·a/P` y la fracción iluminada es `f = (1 − cos(2π·a/P))/2`.
- (El cuarto menguante cae en 22,1 d, no exactamente en `3P/4 = 22,15 d`, por el redondeo de la edad.) Descripción larga: la fracción iluminada sube de 0 a 1 en medio ciclo y baja de nuevo.
- 🎯 **Por qué importa:** La Luna es el reloj más a mano del cielo: cada noche cambia, y cada 29,5 días vuelve a empezar. Pero «a mano» no significa «fácil de explicar»: muchas personas creen que las fases son la sombra de la Tierra sobre la Luna.

📘 **Dónde se aprende** (3 clases): [B01-C12 · Fases lunares y ciclos celestes](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md); [B128-C03 · Alternativas a la observación visual](../programa/clases/B128/B128-C03-alternativas-a-la-observacion-visual/CLASE.md); [B131-C05 · Demostraciones visuales y modelos para el aula](../programa/clases/B131/B131-C05-demostraciones-visuales-y-modelos-para-el-aula/CLASE.md).

### Fracción inspirada

- La fracción inspirada `FiO₂` es la proporción de O₂ del aire que se respira.

🎯 **Por qué importa (clase B117-C04):** Ninguna clase anterior simula problemas respiratorios. La decisión central: ¿cuánto margen de oxigenación hay entre la atmósfera nominal de la cabina y una condición peligrosa, y qué variable lo consume más rápido?

📘 **Dónde se aprende** (1 clase): [B117-C04 · Problemas respiratorios simulados](../programa/clases/B117/B117-C04-problemas-respiratorios-simulados/CLASE.md).

### Fracción ionizada

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B32-C02](../programa/clases/B32/B32-C02-equilibrio-termodinamico-local-y-desviaciones-no-lte/CLASE.md):**
- *Descripción textual:* la temperatura da la razón de poblaciones y la constante de Saha, que determina la fracción ionizada y la temperatura del 50 %.
- Descripción larga: la fracción ionizada pasa de casi cero a casi uno en pocas decenas de miles de kelvin.
- 🎯 **Por qué importa:** Si el ETL falla, las abundancias que se derivan son erróneas. La decisión central: ¿cuánto hidrógeno está ionizado a cada temperatura y densidad?

📘 **Dónde se aprende** (1 clase): [B32-C02 · Equilibrio termodinámico local y desviaciones no LTE](../programa/clases/B32/B32-C02-equilibrio-termodinamico-local-y-desviaciones-no-lte/CLASE.md).

### Fracción molar

- La fracción molar `y_i` de un componente de una mezcla es su cantidad de sustancia dividida entre la total; para gases ideales, coincide con la fracción en volumen.

💡 **Cómo se explica en la clase [B06-C07](../programa/clases/B06/B06-C07-estequiometria-elemental/CLASE.md):**
- La fracción molar (o en volumen, en un gas ideal) cuenta moléculas y es la que se mide con un espectrómetro de masas o un cromatógrafo; la fracción en masa cuenta kilos y es la que importa para un balance de masa o una presión parcial.
- 🎯 **Por qué importa:** Si quieres saber cuánto pesa una columna de atmósfera de Marte, necesitas su masa molar media, y para eso, su composición. La NASA publica la composición en volumen de las atmósferas de Marte, Venus y la Tierra y también un «peso molecular» medio (S1, S2, S3).

📘 **Dónde se aprende** (1 clase): [B06-C07 · Estequiometría elemental](../programa/clases/B06/B06-C07-estequiometria-elemental/CLASE.md).

### Fracción no cubierta

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B42-C18](../programa/clases/B42/B42-C18-optica-adaptativa-multiconjugada/CLASE.md):**
- Con dos capas (suelo 60 % y 8 km 40 %), `r₀ = 0,13 m` a 500 nm (ilustrativos) `θ₀ = 1,825 arcsec`; con cuatro guías a ±30 arcsec la fracción no cubierta es `0` hasta 20 arcsec, `0,0021` a 30 y `0,1667` en la diagonal de 50 arcsec.
- 🎯 **Por qué importa:** Una sola corrección solo vale dentro del ángulo isoplanático (unos segundos de arco). La decisión central: ¿cómo se amplía el campo y qué parte de la turbulencia queda sin restricción?

📘 **Dónde se aprende** (1 clase): [B42-C18 · Óptica adaptativa multiconjugada](../programa/clases/B42/B42-C18-optica-adaptativa-multiconjugada/CLASE.md).

### Fracción por volumen

- La fracción por volumen es la proporción de moléculas de una especie.

💡 **Cómo se explica en la clase [B54-C02](../programa/clases/B54/B54-C02-composicion-quimica-atmosferica/CLASE.md):**
- ⚠️ **Error frecuente:** Confundir fracción por volumen con fracción por masa. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** Dos atmósferas con la misma temperatura y gravedad tienen alturas de escala distintas si sus gases pesan distinto. La pregunta motivadora: ¿qué parte de la diferencia entre las atmósferas de los planetas viene solo de la composición?

📘 **Dónde se aprende** (1 clase): [B54-C02 · Composición química atmosférica](../programa/clases/B54/B54-C02-composicion-quimica-atmosferica/CLASE.md).

### Fracción reportada

- La fracción reportada `r(t)` es la proporción de incidentes que se informan.

💡 **Cómo se explica en la clase [B119-C21](../programa/clases/B119/B119-C21-cultura-de-seguridad-aeroespacial-y-aprendizaje-de-incidentes/CLASE.md):**
- *Descripción textual:* los incidentes verdaderos pasan por el filtro de la fracción reportada; corregir por ella permite estimar el aprendizaje real.
- No se consultó ninguna norma de seguridad ni estudio de cultura. El ejemplo conductor: una organización ficticia con 100 unidades de exposición por año, tasa verdadera `λ(t) = 12 t^(−0,30)` incidentes por unidad de exposición (1200 esperados el año 1) y una fracción reportada que crece de 0,35 a 0,90 en 10 años.
- 🎯 **Por qué importa:** B88-C16 cubre la seguridad funcional técnica; ninguna clase trata la dimensión cultural, y los indicadores de reportes se malinterpretan con facilidad. La decisión central: ¿qué indicador permite saber si una organización aprende cuando los reportes dependen de la confianza para informar?

📘 **Dónde se aprende** (1 clase): [B119-C21 · Cultura de seguridad aeroespacial y aprendizaje de incidentes](../programa/clases/B119/B119-C21-cultura-de-seguridad-aeroespacial-y-aprendizaje-de-incidentes/CLASE.md).

### Fracción serial

- La fracción serial `s` es la parte del tiempo en un procesador que no se puede repartir; la paralelizable es `1 − s`.

💡 **Cómo se explica en la clase [B18-C05](../programa/clases/B18/B18-C05-experimentos-de-escalabilidad/CLASE.md):**
- Si `e` es constante al variar `N`, la pérdida se explica por una fracción serial.
- Lectura. `e` no es constante: no es solo una fracción serial.
- 🎯 **Por qué importa:** Un grupo pide tiempo en un clúster para propagar un catálogo grande de órbitas. Antes de pedir mil núcleos hay que saber si el programa los aprovechará.

📘 **Dónde se aprende** (1 clase): [B18-C05 · Experimentos de escalabilidad](../programa/clases/B18/B18-C05-experimentos-de-escalabilidad/CLASE.md).

### Fracción serie

- La fracción serie `s` es la parte del tiempo que no se puede repartir.

💡 **Cómo se explica en la clase [B14-C13](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md):**
- Esa fracción serie incluye el coste de crear el `Pool`, no solo el código serie del programa.
- 🎯 **Por qué importa:** Un análisis de miles de simulaciones tarda una noche. Tienes ocho núcleos.

📘 **Dónde se aprende** (1 clase): [B14-C13 · Computación paralela](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md).

### Fracción sin voltear

- La fracción sin voltear tras `t` es `e^(−λt)`.

💡 **Cómo se explica en la clase [B55-C14](../programa/clases/B55/B55-C14-quimica-de-regolitos/CLASE.md):**
- *Descripción textual:* la tasa de volteo da la fracción sin voltear y los tiempos; la mezcla de componentes se invierte con un sistema lineal cuya precisión depende del ruido.
- Poisson analítico: la fracción sin voltear.
- 🎯 **Por qué importa:** El regolito es el suelo de un cuerpo sin atmósfera y su química depende de qué impactos lo removieron y de qué componentes lo formaron. La decisión central: ¿cuánto tiempo hace falta para que una capa se voltee y qué mezcla de componentes explica la composición medida?

📘 **Dónde se aprende** (1 clase): [B55-C14 · Química de regolitos](../programa/clases/B55/B55-C14-quimica-de-regolitos/CLASE.md).

### Fracción termalizada

- La fracción termalizada `η` es la parte que se convierte en calor.

🎯 **Por qué importa (clase B52-C17):** El calor determina si un cuerpo funde, se diferencia o se enfría rápido. La decisión central: ¿cuánto tarda un cuerpo en perder su calor y cuánto lo calienta un impacto?

📘 **Dónde se aprende** (1 clase): [B52-C17 · Colisiones y evolución térmica](../programa/clases/B52/B52-C17-colisiones-y-evolucion-termica/CLASE.md).

### Fracción térmica

- La fracción térmica `f_th` de la energía que calienta el gas.

💡 **Cómo se explica en la clase [B38-C07](../programa/clases/B38/B38-C07-modelos-submalla-de-formacion-estelar-y-retroalimentacion/CLASE.md):**
- Descripción larga: al aumentar la fracción térmica el gas y la formación de equilibrio bajan.
- 🎯 **Por qué importa:** El gas denso forma estrellas por debajo de la resolución de la simulación y las supernovas devuelven energía. La decisión central: ¿cuánto gas expulsa la retroalimentación y a qué equilibrio llega la zona?

📘 **Dónde se aprende** (1 clase): [B38-C07 · Modelos submalla de formación estelar y retroalimentación](../programa/clases/B38/B38-C07-modelos-submalla-de-formacion-estelar-y-retroalimentacion/CLASE.md).

### Fracción terrestre

- La fracción terrestre es `R/D`.

🎯 **Por qué importa (clase B100-C07):** Reciclar el 90 % del agua no reduce la dependencia en un 90 %: quedan repuestos, fugas y averías, y el equipo pesa. La decisión central: ¿cuánta reposición terrestre queda según la eficiencia del lazo y cuántos días tarda el equipo en compensar su propia masa?

📘 **Dónde se aprende** (1 clase): [B100-C07 · Dependencia de suministros terrestres y cierre de lazos logísticos](../programa/clases/B100/B100-C07-dependencia-de-suministros-terrestres-y-cierre-de-lazos-logisticos/CLASE.md).

### Fracción útil

- La fracción útil `π` es la carga útil entre la masa inicial.
- La fracción útil es la parte de la órbita con la actitud adecuada.
- La fracción útil es la proporción de direcciones con tres celdas dentro del campo.

💡 **Cómo se explica en la clase [B78-C15](../programa/clases/B78/B78-C15-propulsion-nuclear-electrica-conceptual/CLASE.md):**
- Paso 4 · Fracción útil. `π = 1 − 0,1563 − 0,0870 = 0,7567`.
- Para `Δv = 5000 m/s`, el `Isp` óptimo es `3763 s` con una fracción útil de `0,7623`; para `15 000 m/s`, `3219 s` y `0,3794`: el ejemplo conductor.
- 🎯 **Por qué importa:** Subir la velocidad de escape reduce el propelente pero obliga a más potencia, y por tanto a más planta, para el mismo tiempo de empuje. La decisión central: ¿existe un `Isp` que maximice la carga útil y cómo cambia con el Δv y con la masa específica de la planta?

📘 **Dónde se aprende** (3 clases): [B78-C15 · Propulsión nuclear eléctrica conceptual](../programa/clases/B78/B78-C15-propulsion-nuclear-electrica-conceptual/CLASE.md); [B78-C22 · Ciclos de trabajo y operación de propulsión eléctrica](../programa/clases/B78/B78-C22-ciclos-de-trabajo-y-operacion-de-propulsion-electrica/CLASE.md); [B87-C03 · Sensores solares](../programa/clases/B87/B87-C03-sensores-solares/CLASE.md).

### Fraccionamiento dependiente de la masa

- Un fraccionamiento dependiente de la masa sigue `δ'¹⁷ = β δ'¹⁸` con `δ' = 1000 ln(1+δ/1000)`.

🎯 **Por qué importa (clase B55-C13):** Los isótopos son la «huella dactilar» de un reservorio: aguas, minerales y gases de distinto origen tienen razones distintas. Interpretarlas exige saber mezclar y distinguir fraccionamientos de procedencias.

📘 **Dónde se aprende** (1 clase): [B55-C13 · Isótopos como trazadores](../programa/clases/B55/B55-C13-isotopos-como-trazadores/CLASE.md).

### Fraccionario

- El retardo entero y el fraccionario.

🎯 **Por qué importa (clase B51-C08):** Un retardo mal compensado reduce la coherencia y en VLBI hace perder la detección. La decisión central: ¿cómo se estima y se aplica un retardo con fracción de muestra y qué correlación se espera tras alinear?

📘 **Dónde se aprende** (1 clase): [B51-C08 · Compensación de retardo y alineación temporal de flujos de antenas](../programa/clases/B51/B51-C08-compensacion-de-retardo-y-alineacion-temporal-de-flujos-de-antenas/CLASE.md).

### Fragmentación

- Una fragmentación es la ruptura de un objeto en piezas.

🎯 **Por qué importa (clase B118-C09):** La directriz 5 de la COPUOS dice que la mayor parte de los desechos catalogados proviene de fragmentaciones; entender cuántos fragmentos produce un evento y de qué tamaño es la base de los escenarios futuros. La decisión central: ¿cuántos fragmentos relevantes genera un evento y cuándo es «catastrófico»?

📘 **Dónde se aprende** (1 clase): [B118-C09 · Generación de desechos](../programa/clases/B118/B118-C09-generacion-de-desechos/CLASE.md).

### Fragmentación externa

- La fragmentación externa `1 − mayor_libre/total_libre`.

💡 **Cómo se explica en la clase [B88-C29](../programa/clases/B88/B88-C29-gestion-de-memoria-determinista-en-software-de-vuelo/CLASE.md):**
- Primer ajuste sobre 4096 B: 0 fallos en 5000 pasos, pero la fragmentación externa máxima fue `0,239`: casi un cuarto de la memoria libre no era contigua con el mayor hueco.
- En 5000 pasos: el montón no falló pero llegó a `0,239` de fragmentación externa; el pool no falló.
- 🎯 **Por qué importa:** Un montón puede fallar después de horas por fragmentación aunque haya memoria libre; un pool de bloques fijos no. La decisión central: ¿qué esquema de memoria garantiza que una asignación nunca falle en vuelo?

📘 **Dónde se aprende** (1 clase): [B88-C29 · Gestión de memoria determinista en software de vuelo](../programa/clases/B88/B88-C29-gestion-de-memoria-determinista-en-software-de-vuelo/CLASE.md).

### Fragmento

- Un fragmento (*chunk*) es el bloque de un dataset que se guarda y comprime como una unidad.

💡 **Cómo se explica en la clase [B14-C07](../programa/clases/B14/B14-C07-hdf5-y-almacenamiento-cientifico/CLASE.md):**
- ⚠️ **Error frecuente:** Cargar todo para leer un fragmento. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** Una simulación o un instrumento moderno produce series de millones de muestras con sus metadatos. Guardarlas en texto es lento y pesado; cargarlas enteras en memoria para leer un fragmento es inviable.

📘 **Dónde se aprende** (1 clase): [B14-C07 · HDF5 y almacenamiento científico](../programa/clases/B14/B14-C07-hdf5-y-almacenamiento-cientifico/CLASE.md).

### Franja

- Una franja es un ciclo de `2π`, equivalente a `λ/2` de desplazamiento.
- Una franja es un ciclo de 2π.
- La franja es el ancho que cubre la cámara.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B42-C09](../programa/clases/B42/B42-C09-interferometria-de-dos-haces/CLASE.md):**
- ⚠️ **Error frecuente:** Olvidar el factor 2 del camino. Franja cada `λ/2` de espejo.
- 🎯 **Por qué importa:** La medida interferométrica de fase es la base de la metrología óptica (superficies, frentes de onda; C13).

📘 **Dónde se aprende** (4 clases): [B42-C09 · Interferometría de dos haces](../programa/clases/B42/B42-C09-interferometria-de-dos-haces/CLASE.md); [B57-C08 · Interferometría radar InSAR](../programa/clases/B57/B57-C08-interferometria-radar-insar/CLASE.md); [B69-C06 · Deslizamientos y subsidencia medidos con InSAR](../programa/clases/B69/B69-C06-deslizamientos-y-subsidencia-medidos-con-insar/CLASE.md); [B97-C01 · Robots rover y orbitadores](../programa/clases/B97/B97-C01-robots-rover-y-orbitadores/CLASE.md).

### Frecuencia

- La longitud de onda `λ` es la distancia entre dos crestas de la onda; la frecuencia `ν`, cuántas pasan por segundo; se relacionan con `c = λ·ν`.
- El período `T` es el tiempo de una vuelta; la frecuencia `f = 1/T` es el número de vueltas por segundo (hertz, Hz); la velocidad angular `ω = 2π/T` (rad/s) es el ángulo recorrido por unidad de tiempo.
- La longitud de onda `λ` es la distancia entre dos puntos iguales consecutivos (m); la frecuencia `f` (Hz) es el número de ciclos por segundo en un punto; la velocidad de propagación `v` cumple `v = f λ`.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C12](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md):**
- Moraleja: antes de interpretar un espectro, confirma que `f_s` es mayor que el doble de la frecuencia máxima presente.
- A["Fuente oscila con frecuencia f"] --> B["Medio transmite la perturbación con velocidad v"]
- 🎯 **Por qué importa:** Un sensor de vibración a bordo de una nave registra 30 Hz cuando la estructura vibra a 130 Hz. Un trueno llega segundos después del rayo.

📖 **Explicado a fondo:** [Longitud de onda y frecuencia](esencial/esencial-d-l.md#longitud-de-onda-y-frecuencia) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (5 clases): [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B05-C03 · Movimiento rectilíneo y circular](../programa/clases/B05/B05-C03-movimiento-rectilineo-y-circular/CLASE.md); [B05-C12 · Ondas mecánicas y frecuencia](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md); [B84-C20 · Diseño estructural de plataforma satelital](../programa/clases/B84/B84-C20-diseno-estructural-de-plataforma-satelital/CLASE.md); [B127-C05 · Evaluación actuarial básica del riesgo espacial](../programa/clases/B127/B127-C05-evaluacion-actuarial-basica-del-riesgo-espacial/CLASE.md).

### Frecuencia angular

- El número de onda `k = 2π/λ` y la frecuencia angular `ω` se relacionan con `ω = ck`: es la relación de dispersión.
- `ω` la frecuencia angular (rad/s);
- La frecuencia angular `ω = 2πf`.

🎯 **Por qué importa (clase B05-C11):** Una estructura que vibra puede amplificar una excitación hasta romperse; un reloj de péndulo mide tiempo; un átomo vibra en un cristal. La pregunta motivadora es: ¿qué determina la frecuencia a la que algo oscila y qué pasa cuando se le empuja a esa frecuencia?

📘 **Dónde se aprende** (3 clases): [B05-C11 · Movimiento oscilatorio](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md); [B21-C02 · Ecuación de onda: esquemas y dispersión numérica](../programa/clases/B21/B21-C02-ecuacion-de-onda-esquemas-y-dispersion-numerica/CLASE.md); [B42-C01 · Ecuaciones de onda electromagnética](../programa/clases/B42/B42-C01-ecuaciones-de-onda-electromagnetica/CLASE.md).

### Frecuencia cardiaca

- La frecuencia cardiaca es el número de latidos por minuto (lpm).

🎯 **Por qué importa (clase B116-C01):** Una pulsera que da «72 lpm» no dice «72 ± 0,1». Con movimiento puede dar 120 cuando el pulso real es 70.

📘 **Dónde se aprende** (1 clase): [B116-C01 · Sensores fisiológicos y wearables para vuelo](../programa/clases/B116/B116-C01-sensores-fisiologicos-y-wearables-para-vuelo/CLASE.md).

### Frecuencia ciclotrónica

- El radio de giro es `r = m v/(|q| B)` y la frecuencia ciclotrónica `f = |q| B/(2π m)`.

🎯 **Por qué importa (clase B05-C17):** La Tierra tiene un campo magnético que un satélite puede medir con un magnetómetro y que actúa sobre las partículas cargadas que lo atraviesan; además, una corriente a bordo crea su propio campo, que puede perturbar esas medidas.

📘 **Dónde se aprende** (1 clase): [B05-C17 · Campos magnéticos](../programa/clases/B05/B05-C17-campos-magneticos/CLASE.md).

### Frecuencia crítica

- La frecuencia crítica `ν_c` es la que acota el espectro de un electrón.
- La frecuencia crítica `foF2` es la de plasma en el máximo de la capa F2: una onda vertical de frecuencia mayor la atraviesa.

💡 **Cómo se explica en la clase [B27-C12](../programa/clases/B27/B27-C12-radiacion-sincrotron/CLASE.md):**
- *Descripción textual:* el campo y el factor de Lorentz fijan la potencia, la frecuencia crítica y el tiempo de enfriamiento; el núcleo `F` integrado sobre una población da una ley de potencias.
- 🎯 **Por qué importa:** El índice espectral de una fuente sincrotrón entrega el índice de energía de sus electrones; la frecuencia crítica entrega `γ²B`. Sin estas relaciones no se puede leer un espectro de radio o rayos X.

📘 **Dónde se aprende** (2 clases): [B27-C12 · Radiación sincrotrón](../programa/clases/B27/B27-C12-radiacion-sincrotron/CLASE.md); [B89-C22 · Propagación ionosférica y comunicaciones HF](../programa/clases/B89/B89-C22-propagacion-ionosferica-y-comunicaciones-hf/CLASE.md).

### Frecuencia de Brunt–Väisälä

- La frecuencia de Brunt–Väisälä `N` es la de oscilación de una burbuja estable.
- La frecuencia de Brunt–Väisälä `N` mide la oscilación de una parcela desplazada en una capa estable (`N² > 0`).

🎯 **Por qué importa (clase B37-C08):** Los modos p y g sondean regiones distintas. La decisión central: ¿en qué cavidad se propaga un modo de frecuencia y grado dados?

📘 **Dónde se aprende** (2 clases): [B37-C08 · Oscilaciones no radiales: modos p, g y mixtos](../programa/clases/B37/B37-C08-oscilaciones-no-radiales-modos-p-g-y-mixtos/CLASE.md); [B54-C05 · Transporte convectivo](../programa/clases/B54/B54-C05-transporte-convectivo/CLASE.md).

### Frecuencia de ciclotrón

- La frecuencia de ciclotrón `ω_c = q B/m`.

🎯 **Por qué importa (clase B78-C08):** Sin rejillas no hay límite de Child–Langmuir, pero el propulsor depende de que los electrones giren en un radio pequeño y los iones pasen casi rectos. La decisión central: ¿cuánto vale cada radio de giro frente al largo del canal y qué cambia al subir la tensión?

📘 **Dónde se aprende** (1 clase): [B78-C08 · Propulsores Hall](../programa/clases/B78/B78-C08-propulsores-hall/CLASE.md).

### Frecuencia de corte

- La frecuencia de corte `D/λ`.

🎯 **Por qué importa (clase B42-C07):** La OTF dice qué detalles (frecuencias espaciales) pasan por el sistema y cuáles se pierden; fija el muestreo necesario del detector. La decisión central: ¿hasta qué frecuencia transmite el telescopio y qué muestreo exige?

📘 **Dónde se aprende** (1 clase): [B42-C07 · Función de transferencia óptica](../programa/clases/B42/B42-C07-funcion-de-transferencia-optica/CLASE.md).

### Frecuencia de cruce

- La frecuencia de cruce `f_c` es el ancho de banda del lazo.

💡 **Cómo se explica en la clase [B92-C03](../programa/clases/B92/B92-C03-adquisicion-apuntamiento-y-seguimiento-opticos/CLASE.md):**
- Un lazo de primer orden con frecuencia de cruce `f_c` la reduce a `σ_d² = (A/f_c)[atan(f₂/f_c) − atan(f₁/f_c)]`: `3,82 µrad` con 10 Hz, `1,21 µrad` con 100 Hz y `0,30 µrad` con 900 Hz.
- 🎯 **Por qué importa:** Un satélite conoce su posición y su actitud con una incertidumbre mucho mayor que el haz de comunicaciones. La decisión central: ¿cómo se cubre la incertidumbre en un tiempo razonable y con qué ancho de banda se cierra el lazo para que el jitter no cueste potencia?

📘 **Dónde se aprende** (1 clase): [B92-C03 · Adquisición, apuntamiento y seguimiento ópticos](../programa/clases/B92/B92-C03-adquisicion-apuntamiento-y-seguimiento-opticos/CLASE.md).

### Frecuencia de fondo

- La frecuencia de fondo `f_B = 0,03 E^(−4/5)` da los impactos por año con energía al menos `E` Mt [S2].

💡 **Cómo se explica en la clase [B58-C20](../programa/clases/B58/B58-C20-simulador-de-riesgo-de-impacto-basado-en-datos/CLASE.md):**
- F["frecuencia de fondo"] --> S["impactos de Poisson"]
- 🎯 **Por qué importa:** Un simulador convierte reglas sueltas en un flujo reproducible: leer datos, filtrar, calcular y ordenar. La decisión central: ¿qué objetos del catálogo merecen atención primero y qué número de impactos de fondo es coherente con la ley de frecuencias?

📘 **Dónde se aprende** (1 clase): [B58-C20 · Simulador de riesgo de impacto basado en datos](../programa/clases/B58/B58-C20-simulador-de-riesgo-de-impacto-basado-en-datos/CLASE.md).

### Frecuencia de giro

- La frecuencia de giro `ω = |q|B/m`.

🎯 **Por qué importa (clase B30-C06):** El movimiento de las partículas explica cómo se atrapan en los cinturones, cómo derivan y cómo se aceleran. La decisión central: ¿cuándo queda atrapada una partícula y cuánto vale su radio de giro?

📘 **Dónde se aprende** (1 clase): [B30-C06 · Partículas cargadas y movimientos](../programa/clases/B30/B30-C06-particulas-cargadas-y-movimientos/CLASE.md).

### Frecuencia de la transición hiperfina del cesio-133

- La frecuencia de la transición hiperfina del cesio-133, `Δν_Cs`, es la frecuencia de una radiación atómica concreta que define el segundo.

🎯 **Por qué importa (clase B13-C01):** Una señal de radio o de láser viaja a la Luna y regresa. Para decir «la Luna está a 384 400 km» hay que haber acordado qué es un kilómetro, qué es un segundo y a qué velocidad viaja la señal.

📘 **Dónde se aprende** (1 clase): [B13-C01 · Sistema Internacional y constantes](../programa/clases/B13/B13-C01-sistema-internacional-y-constantes/CLASE.md).

### Frecuencia de Lamb

- La frecuencia de Lamb `L_l = √(l(l+1)) c/r`.

🎯 **Por qué importa (clase B37-C08):** Los modos p y g sondean regiones distintas. La decisión central: ¿en qué cavidad se propaga un modo de frecuencia y grado dados?

📘 **Dónde se aprende** (1 clase): [B37-C08 · Oscilaciones no radiales: modos p, g y mixtos](../programa/clases/B37/B37-C08-oscilaciones-no-radiales-modos-p-g-y-mixtos/CLASE.md).

### Frecuencia de muestreo

- La frecuencia de muestreo `f_s` es cuántas medidas por segundo se toman; la frecuencia de Nyquist es `f_s/2`.
- La frecuencia de muestreo `f_s = 1/Δt` es cuántas muestras hay por unidad de tiempo.
- La frecuencia de muestreo es `f_s = 1/Δt`.

🎯 **Por qué importa (clase B05-C12):** Un sensor de vibración a bordo de una nave registra 30 Hz cuando la estructura vibra a 130 Hz. Un trueno llega segundos después del rayo.

📘 **Dónde se aprende** (3 clases): [B05-C12 · Ondas mecánicas y frecuencia](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md); [B15-C01 · Series temporales discretas](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md); [B15-C02 · Muestreo y aliasing](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md).

### Frecuencia de muestreo fs

- Frecuencia de muestreo `fs`: muestras por segundo.

🎯 **Por qué importa (clase B90-C23):** Un ensayo de vibración que muestrea a 2 048 Hz un tono de 1 500 Hz lo registra como si fuera de 548 Hz y no se nota. La decisión central: ¿qué frecuencia de muestreo, qué filtro y cuántos bits aseguran que lo que se registra es lo que ocurrió?

📘 **Dónde se aprende** (1 clase): [B90-C23 · Instrumentación y adquisición de datos en ensayos](../programa/clases/B90/B90-C23-instrumentacion-y-adquisicion-de-datos-en-ensayos/CLASE.md).

### Frecuencia de Nyquist

- La frecuencia de muestreo `f_s` es cuántas medidas por segundo se toman; la frecuencia de Nyquist es `f_s/2`.
- La frecuencia de Nyquist es `k = N/2`; su modo no tiene derivada bien definida y se anula en la derivada primera.
- La frecuencia de Nyquist es `f_N = f_s/2`, el límite superior de las frecuencias distinguibles; el valor `0,5 ciclos por observación` que describe S2 es el mismo límite expresado en ciclos por muestra.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B37-C13](../programa/clases/B37/B37-C13-series-fotometricas-de-kepler-tess-y-plato-para-asterosismologia/CLASE.md):**
- Con cadencia de `120 s` la frecuencia de Nyquist es `4166,67 μHz` y la resolución `1/T = 1,1574 μHz`; una señal de `4500 μHz` reaparece en `3833,33 μHz` con el signo cambiado (diferencia máxima `1,42 × 10⁻¹²`).
- 🎯 **Por qué importa:** El análisis sísmico depende de cómo se prepara la serie. La decisión central: ¿qué hace el muestreo, los huecos y el filtro con las frecuencias y amplitudes recuperadas?

📘 **Dónde se aprende** (5 clases): [B05-C12 · Ondas mecánicas y frecuencia](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md); [B11-C16 · Métodos espectrales iniciales](../programa/clases/B11/B11-C16-metodos-espectrales-iniciales/CLASE.md); [B15-C02 · Muestreo y aliasing](../programa/clases/B15/B15-C02-muestreo-y-aliasing/CLASE.md); [B37-C13 · Series fotométricas de Kepler, TESS y PLATO para asterosismología](../programa/clases/B37/B37-C13-series-fotometricas-de-kepler-tess-y-plato-para-asterosismologia/CLASE.md); [B42-C11 · Turbulencia atmosférica](../programa/clases/B42/B42-C11-turbulencia-atmosferica/CLASE.md).

### Frecuencia de plasma

- La frecuencia de plasma `ω_p = √(n e²/(ε₀ m))` es la de oscilación colectiva.
- La frecuencia de plasma es `f_p = 8,98√N` Hz (con `N` en m⁻³).

💡 **Cómo se explica en la clase [B30-C08](../programa/clases/B30/B30-C08-frecuencias-y-ondas-de-plasma/CLASE.md):**
- *Descripción textual:* la densidad fija la frecuencia de plasma; de ella salen la relación de dispersión, las velocidades, el retardo y la corrección térmica.
- Con `n = 1 cm⁻³` la frecuencia de plasma es `8978,66 Hz`, que reproduce el coeficiente `8,98 kHz`.
- 🎯 **Por qué importa:** La radiación de las erupciones se emite cerca de la frecuencia de plasma local, de modo que una frecuencia es una altura. La decisión central: ¿qué frecuencia corresponde a cada densidad y cuánto se retrasa una señal?

📘 **Dónde se aprende** (5 clases): [B30-C08 · Frecuencias y ondas de plasma](../programa/clases/B30/B30-C08-frecuencias-y-ondas-de-plasma/CLASE.md); [B46-C02 · Propagación de ondas de radio](../programa/clases/B46/B46-C02-propagacion-de-ondas-de-radio/CLASE.md); [B47-C24 · Instrumentos de plasma y campos in situ](../programa/clases/B47/B47-C24-instrumentos-de-plasma-y-campos-in-situ/CLASE.md); [B78-C09 · Propulsión por plasma](../programa/clases/B78/B78-C09-propulsion-por-plasma/CLASE.md); [B89-C22 · Propagación ionosférica y comunicaciones HF](../programa/clases/B89/B89-C22-propagacion-ionosferica-y-comunicaciones-hf/CLASE.md).

### Frecuencia de Schuler

- La frecuencia de Schuler `ω_s = √(g/R)` es la frecuencia propia de un péndulo de longitud igual al radio de la Tierra; su período es `2π/ω_s`.

🎯 **Por qué importa (clase B80-C01):** Una sonda que sale de la cobertura de seguimiento, un lanzador en ascenso o un módulo de aterrizaje en su descenso necesitan saber dónde están sin ayuda externa. B87 trata el giroscopio como sensor de actitud y B74 estima la órbita con observaciones externas; ninguna clase actual enseña cómo se propaga una solución desde una IMU.

📘 **Dónde se aprende** (1 clase): [B80-C01 · Principios de navegación inercial espacial](../programa/clases/B80/B80-C01-principios-de-navegacion-inercial-espacial/CLASE.md).

### Frecuencia del máximo

- La frecuencia del máximo de `B_ν` es `ν_máx = (5,8789 × 10¹⁰ Hz/K) T` (S1).

🎯 **Por qué importa (clase B26-C15):** El fondo de microondas es la reliquia más antigua observable y da los parámetros del modelo cosmológico. Entender su espectro de cuerpo negro permite calibrar un instrumento, estimar el contenido de fotones y comprender por qué un solo número, la razón barión–fotón, resume tanta física.

📘 **Dónde se aprende** (1 clase): [B26-C15 · Radiación cósmica de fondo](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md).

### Frecuencia Doppler

- La frecuencia Doppler `f_D` varía con el tiempo lento `t`.

💡 **Cómo se explica en la clase [B69-C01](../programa/clases/B69/B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md):**
- La frecuencia Doppler es `f_D = −(1/2π) dφ/dt = 2v²t/(λR)`, que cerca de `t = 0` vale `Ka·t` con `Ka = 2v²/(λR₀)`.
- En ese tiempo la frecuencia Doppler barre `Ba = Ka·T = 2v/L = 1183,3 Hz` (de −591,6 a +591,5 Hz).
- 🎯 **Por qué importa:** Sin el principio Doppler, la resolución en azimut de un radar quedaría fijada por el ancho del haz de la antena: a 850 km, una antena de 12 m (λ = 0,0555 m) iluminaría una franja de unos 3,9 km. La decisión central: ¿qué resolución obtiene el sistema, de qué depende y qué hay que muestrear para no perderla?

📘 **Dónde se aprende** (1 clase): [B69-C01 · Principio Doppler y resolución en azimut del SAR](../programa/clases/B69/B69-C01-principio-doppler-y-resolucion-en-azimut-del-sar/CLASE.md).

### Frecuencia en el plano

- `λ` es el exponente inestable real, `ω` la frecuencia en el plano y `ν = √c2` la frecuencia vertical.

🎯 **Por qué importa (clase B76-C04):** Una órbita halo no es un círculo: es un compromiso entre un modo inestable y dos oscilaciones. La decisión central: ¿qué dicen los modos lineales de `L2` sobre el tiempo de crecimiento de un error y sobre los periodos de la órbita?

📘 **Dónde se aprende** (1 clase): [B76-C04 · Órbitas halo](../programa/clases/B76/B76-C04-orbitas-halo/CLASE.md).

### Frecuencia epicíclica

- La frecuencia epicíclica `κ` es la de esa oscilación radial.

🎯 **Por qué importa (clase B25-C07):** Las estrellas de una galaxia no giran en círculos perfectos: oscilan alrededor de una órbita circular, y su agitación revela la edad y la historia de la población. Además, no nacen todas con la misma masa: la función de masa inicial fija cuántas hay de cada tipo y cuánta luz y metales producirán.

📘 **Dónde se aprende** (1 clase): [B25-C07 · Dinámica de poblaciones estelares](../programa/clases/B25/B25-C07-dinamica-de-poblaciones-estelares/CLASE.md).

### Frecuencia espacial

- La frecuencia espacial `u = sen θ/λ`.

🎯 **Por qué importa (clase B42-C04):** La pupila de un telescopio es una apertura: su forma fija la imagen de una estrella. La decisión central: ¿cómo cambia el patrón cuando cambia la forma o el número de aberturas?

📘 **Dónde se aprende** (1 clase): [B42-C04 · Difracción de aperturas](../programa/clases/B42/B42-C04-difraccion-de-aperturas/CLASE.md).

### Frecuencia estructural

- La frecuencia estructural `f = √(k/m)/(2π)`.

💡 **Cómo se explica en la clase [B43-C20](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md):**
- *Descripción textual:* las fuentes se suman en cuadratura y se contrastan; el Strehl y la frecuencia estructural se comparan con los requisitos.
- 🎯 **Por qué importa:** El proyecto completo exige que los errores se sumen, se verifiquen y se comparen con los requisitos. La decisión central: ¿qué fuente domina el error, cuánto margen queda y la estructura es lo bastante rígida para el servo?

📘 **Dónde se aprende** (1 clase): [B43-C20 · Proyecto mecánico completo de telescopio](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md).

### Frecuencia fraccional

- La frecuencia fraccional `y = dx/dt`.

🎯 **Por qué importa (clase B46-C08):** El tiempo de coherencia de un instrumento depende de cómo se acumula el error de un oscilador. La decisión central: ¿a qué escala de tiempo domina cada tipo de ruido y cuánto se puede integrar?

📘 **Dónde se aprende** (2 clases): [B46-C08 · Osciladores y estabilidad](../programa/clases/B46/B46-C08-osciladores-y-estabilidad/CLASE.md); [B74-C16 · Sincronización temporal](../programa/clases/B74/B74-C16-sincronizacion-temporal/CLASE.md).

### Frecuencia gravitacional

- La frecuencia gravitacional `f_GW = 2/P`.

🎯 **Por qué importa (clase B27-C13):** La fusión de dos estrellas de neutrones fue el primer evento detectado en ondas gravitacionales y en luz. Saber cuánto falta para una fusión, a qué frecuencia, y cómo la excentricidad la acelera, es la base de toda búsqueda.

📘 **Dónde se aprende** (1 clase): [B27-C13 · Binarias compactas](../programa/clases/B27/B27-C13-binarias-compactas/CLASE.md).

### Frecuencia imagen

- La frecuencia imagen es `2f_LO − f_RF`.

🎯 **Por qué importa (clase B46-C07):** La mezcla es lo que permite procesar en una banda cómoda, pero trae consigo una segunda frecuencia que cae en la misma FI. La decisión central: ¿qué rechazo de imagen exige el receptor y cómo se logra?

📘 **Dónde se aprende** (1 clase): [B46-C07 · Receptores superheterodinos](../programa/clases/B46/B46-C07-receptores-superheterodinos/CLASE.md).

### Frecuencia intermedia

- La frecuencia intermedia (FI) es `|f_RF − f_LO|`.

🎯 **Por qué importa (clase B46-C07):** La mezcla es lo que permite procesar en una banda cómoda, pero trae consigo una segunda frecuencia que cae en la misma FI. La decisión central: ¿qué rechazo de imagen exige el receptor y cómo se logra?

📘 **Dónde se aprende** (1 clase): [B46-C07 · Receptores superheterodinos](../programa/clases/B46/B46-C07-receptores-superheterodinos/CLASE.md).

### Frecuencia ISCO

- La frecuencia ISCO es la frecuencia gravitacional en la última órbita estable.

🎯 **Por qué importa (clase B28-C07):** La tasa de eventos detectados depende del volumen que el detector ve, que crece como el cubo del alcance. Una mejora pequeña en sensibilidad se traduce en muchos más eventos.

📘 **Dónde se aprende** (1 clase): [B28-C07 · Fuentes compactas binarias](../programa/clases/B28/B28-C07-fuentes-compactas-binarias/CLASE.md).

### Frecuencia natural

- La frecuencia natural `ω₀ = √(k/m)` es la del sistema libre.
- La frecuencia natural es `ω_n² = −Cm_α q S d/I_y`.
- La frecuencia natural de lazo cerrado es `ω_n² = μ_c Kp − μ_α`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C11](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md):**
- Planteamiento. Hallar la frecuencia natural del mástil, su energía a 10 mm de amplitud y el efecto de una excitación a esa frecuencia.
- Aquí lo calcularás en dos pasos y verás qué pasa si la excitación coincide con la frecuencia natural.
- 🎯 **Por qué importa:** Una estructura que vibra puede amplificar una excitación hasta romperse; un reloj de péndulo mide tiempo; un átomo vibra en un cristal. La pregunta motivadora es: ¿qué determina la frecuencia a la que algo oscila y qué pasa cuando se le empuja a esa frecuencia?

📘 **Dónde se aprende** (7 clases): [B05-C11 · Movimiento oscilatorio](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md); [B16-C04 · Respuesta transitoria y estacionaria](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md); [B47-C11 · Aislamiento vibracional](../programa/clases/B47/B47-C11-aislamiento-vibracional/CLASE.md); [B58-C19 · Comunicación pública del riesgo](../programa/clases/B58/B58-C19-comunicacion-publica-del-riesgo/CLASE.md); [B77-C17 · Estabilidad durante descenso](../programa/clases/B77/B77-C17-estabilidad-durante-descenso/CLASE.md); [B77-C24 · Guiado y control de actitud de lanzadores (TVC)](../programa/clases/B77/B77-C24-guiado-y-control-de-actitud-de-lanzadores-tvc/CLASE.md) y 1 más.

### Frecuencia óptima

- La frecuencia óptima es aquella en la que ganar apertura eléctrica deja de compensar la pérdida.
- La frecuencia óptima `f* = c/(4πσ)` maximiza la ganancia de una parábola con `σ` fija.

🎯 **Por qué importa (clase B89-C06):** Una antena mal apuntada o con la superficie deformada pierde decibelios que ningún amplificador recupera, y esas pérdidas crecen con la frecuencia. La decisión central: ¿qué ganancia efectiva da una antena y a qué frecuencia deja de compensar subir la frecuencia?

📘 **Dónde se aprende** (2 clases): [B89-C06 · Ganancias y pérdidas de antena](../programa/clases/B89/B89-C06-ganancias-y-perdidas-de-antena/CLASE.md); [B91-C04 · Antenas desplegables y estructuras de gran apertura](../programa/clases/B91/B91-C04-antenas-desplegables-y-estructuras-de-gran-apertura/CLASE.md).

### Frecuencia orbital

- La frecuencia orbital `f = c³/(2π (r/r_g)^{3/2} GM)`.

💡 **Cómo se explica en la clase [B27-C09](../programa/clases/B27/B27-C09-orbitas-en-campos-fuertes/CLASE.md):**
- Para `10 M☉`, la frecuencia orbital en el ISCO es `219,9 Hz` y en la esfera de fotones `621,9 Hz` (con `f = c³/(2π (r/r_g)^{3/2} GM)`).
- 🎯 **Por qué importa:** La sombra de un agujero negro no es su horizonte: es la imagen de la esfera de fotones ampliada por la curvatura. Y la fórmula `6πM/p` de la precesión solo vale lejos.

📘 **Dónde se aprende** (1 clase): [B27-C09 · Órbitas en campos fuertes](../programa/clases/B27/B27-C09-orbitas-en-campos-fuertes/CLASE.md).

### Frecuencia vertical

- `λ` es el exponente inestable real, `ω` la frecuencia en el plano y `ν = √c2` la frecuencia vertical.

🎯 **Por qué importa (clase B76-C04):** Una órbita halo no es un círculo: es un compromiso entre un modo inestable y dos oscilaciones. La decisión central: ¿qué dicen los modos lineales de `L2` sobre el tiempo de crecimiento de un error y sobre los periodos de la órbita?

📘 **Dónde se aprende** (1 clase): [B76-C04 · Órbitas halo](../programa/clases/B76/B76-C04-orbitas-halo/CLASE.md).

### Frecuencia ν_max

- La frecuencia `ν_max` es la de máxima potencia.

🎯 **Por qué importa (clase B37-C09):** Sin Δν y νmax habría que ajustar modelos para saber masa y radio. La decisión central: ¿qué precisión en masa y radio se obtiene con estos observables y qué supuestos exige?

📘 **Dónde se aprende** (1 clase): [B37-C09 · Frecuencias características: Δν, νmax y espaciado de períodos](../programa/clases/B37/B37-C09-frecuencias-caracteristicas-max-y-espaciado-de-periodos/CLASE.md).

### Frecuencias propias

- Las frecuencias propias `g_k` son los autovalores de `A` y `f_k` los de `B` (inclinaciones; un modo es nulo).

💡 **Cómo se explica en la clase [B73-C11](../programa/clases/B73/B73-C11-resonancias-seculares/CLASE.md):**
- *Descripción textual:* los datos dan los coeficientes de Laplace, éstos las matrices, y de ellas salen las frecuencias propias, la evolución de `e` y la posición de las resonancias seculares.
- Analogía: dos péndulos unidos por un muelle muy blando intercambian energía lentamente: las frecuencias propias son los modos en que oscilan en conjunto.
- 🎯 **Por qué importa:** La excentricidad de una órbita varía durante millones de años por la atracción promediada de los demás planetas, y esa variación se vuelve violenta cuando una frecuencia propia coincide con la de precesión de un asteroide.

📘 **Dónde se aprende** (1 clase): [B73-C11 · Resonancias seculares](../programa/clases/B73/B73-C11-resonancias-seculares/CLASE.md).

### Frenador

- Un sobrevuelo es acelerador si `v∞` queda más alineado con la velocidad del planeta y frenador si queda menos.

🎯 **Por qué importa (clase B75-C06):** Un cohete que sale de la Tierra no puede llevar combustible para ir a Júpiter con una trayectoria directa de baja energía y además frenar. La decisión central: ¿cuánta velocidad heliocéntrica puede ganar o perder una nave pasando cerca de un planeta, y de qué depende?

📘 **Dónde se aprende** (1 clase): [B75-C06 · Asistencias gravitacionales](../programa/clases/B75/B75-C06-asistencias-gravitacionales/CLASE.md).

### Frente de onda

- El frente de onda `W(x,y)`.

🎯 **Por qué importa (clase B42-C13):** La óptica adaptativa solo corrige lo que mide. La decisión central: ¿qué se mide (pendientes o fase), cuántos modos se ajustan y cuánto ruido llega a los coeficientes?

📘 **Dónde se aprende** (1 clase): [B42-C13 · Medición de frente de onda](../programa/clases/B42/B42-C13-medicion-de-frente-de-onda/CLASE.md).

### Frente de onda secundario

- El frente de onda secundario: onda esférica (aquí cilíndrica, 2D) emitida por cada punto.

🎯 **Por qué importa (clase B42-C02):** Sin este principio no hay un procedimiento para calcular qué le pasa a la luz al pasar por una apertura (la pupila de un telescopio es una). La decisión central: ¿a qué distancia vale la aproximación de campo lejano y cuándo hay que sumar las ondas secundarias una por una?

📘 **Dónde se aprende** (1 clase): [B42-C02 · Principio de Huygens-Fresnel](../programa/clases/B42/B42-C02-principio-de-huygens-fresnel/CLASE.md).

### Frente de Pareto

- El frente de Pareto es el conjunto de sitios no dominados.
- El frente de Pareto es el conjunto de las opciones no dominadas.
- El frente de Pareto es el conjunto de diseños no dominados.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B67-C01](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md):**
- *Descripción textual:* los datos de cada sitio se normalizan; los dominados se descartan con el frente de Pareto; los pesos convierten los datos normalizados en un puntaje y un orden; repetir con pesos aleatorios mide qué tan estable es el primero.
- 🎯 **Por qué importa:** Elegir con una sola cifra (la reserva) lleva a sitios que no se pueden explotar; elegir con una suma de unidades distintas es un error. La decisión central: ¿cuál sitio conviene, y cuánto de esa respuesta depende de los pesos que fija quien decide?

📘 **Dónde se aprende** (4 clases): [B67-C01 · Selección de sitios de extracción con criterios múltiples](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md); [B78-C20 · Comparación no operativa de arquitecturas de propulsión](../programa/clases/B78/B78-C20-comparacion-no-operativa-de-arquitecturas-de-propulsion/CLASE.md); [B81-C11 · Optimización multicriterio y frentes de Pareto](../programa/clases/B81/B81-C11-optimizacion-multicriterio-y-frentes-de-pareto/CLASE.md); [B91-C06 · Selección y compromiso de diseño de antenas](../programa/clases/B91/B91-C06-seleccion-y-compromiso-de-diseno-de-antenas/CLASE.md).

### Fría

- La redundancia activa (caliente) y la fría (reserva) se diferencian en si la unidad extra funciona desde el principio.
- La redundancia caliente tiene las unidades encendidas a la vez; la fría deja la reserva apagada y sin desgaste hasta conmutar.
- La fría `R_f = r + c·λT·r`, con reserva apagada sin desgaste.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B86-C11](../programa/clases/B86/B86-C11-redundancia-electrica/CLASE.md):**
- Un paralelo activo sube a `0,9613`, una reserva fría perfecta a `0,9792`, un 2 de 3 a `0,8991`, y un paralelo con `10 %` de causa común cae a `0,9470`.
- 🎯 **Por qué importa:** Duplicar un equipo no duplica la confiabilidad ni resuelve todas las fallas: depende de cómo se conmuta, de si las unidades comparten una causa común y de cuánto cuesta en masa y en potencia. La decisión central: ¿qué arquitectura redundante da la confiabilidad necesaria sin pagar más masa y potencia de las debidas?

📘 **Dónde se aprende** (4 clases): [B86-C11 · Redundancia eléctrica](../programa/clases/B86/B86-C11-redundancia-electrica/CLASE.md); [B88-C01 · Arquitectura de computador de vuelo](../programa/clases/B88/B88-C01-arquitectura-de-computador-de-vuelo/CLASE.md); [B88-C32 · Redundancia fría y caliente: estrategias y conmutación](../programa/clases/B88/B88-C32-redundancia-fria-y-caliente-estrategias-y-conmutacion/CLASE.md); [B93-C04 · Análisis de confiabilidad de electrónica (MTBF y derating)](../programa/clases/B93/B93-C04-analisis-de-confiabilidad-de-electronica-mtbf-y-derating/CLASE.md).

### Fricción de Coulomb

- La fricción de Coulomb limita la fuerza tangencial a `μ N`.

💡 **Cómo se explica en la clase [B97-C10](../programa/clases/B97/B97-C10-manipulacion-de-herramientas/CLASE.md):**
- Límite: el contacto es puntual con fricción de Coulomb y sin deformación.
- 🎯 **Por qué importa:** Un agarre insuficiente deja caer o gira la herramienta; uno excesivo daña el mango. Saber qué carga domina evita diseñar el agarre solo con el peso, error frecuente cuando se reduce la gravedad.

📘 **Dónde se aprende** (1 clase): [B97-C10 · Manipulación de herramientas](../programa/clases/B97/B97-C10-manipulacion-de-herramientas/CLASE.md).

### Fricción de Hubble

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B40-C06](../programa/clases/B40/B40-C06-campos-escalares-en-cosmologia-potenciales-y-evolucion/CLASE.md):**
- ⚠️ **Error frecuente:** Olvidar la fricción de Hubble. Se corrige con 8.3.
- 🎯 **Por qué importa:** La ecuación de estado de un campo decide cómo se diluye y qué domina el universo. La decisión central: ¿qué `w` promedio y qué ley de dilución tiene un campo que oscila en `V ∝ φⁿ`?

📘 **Dónde se aprende** (1 clase): [B40-C06 · Campos escalares en cosmología: potenciales y evolución](../programa/clases/B40/B40-C06-campos-escalares-en-cosmologia-potenciales-y-evolucion/CLASE.md).

### Fringe stopping

- El fringe stopping: multiplicar por `e^{−iφ_modelo}`.

💡 **Cómo se explica en la clase [B51-C09](../programa/clases/B51/B51-C09-fringe-stopping-y-rotacion-de-fase-por-retardo-geometrico/CLASE.md):**
- P --> S["fringe stopping: quita la fase"]
- 🎯 **Por qué importa:** Si se promedia sin detener las franjas, la señal se anula. La decisión central: ¿qué tasa de franjas tiene una fuente, cuánto se pierde al promediar y qué precisión pide el modelo?

📘 **Dónde se aprende** (1 clase): [B51-C09 · Fringe stopping y rotación de fase por retardo geométrico](../programa/clases/B51/B51-C09-fringe-stopping-y-rotacion-de-fase-por-retardo-geometrico/CLASE.md).

### Frontera

- Una frontera es una celda libre conocida adyacente a una desconocida.

💡 **Cómo se explica en la clase [B97-C16](../programa/clases/B97/B97-C16-autonomia-de-exploracion/CLASE.md):**
- Una frontera es una celda libre conocida con una vecina desconocida; cuando no quedan, la exploración termina.
- Paso 2 · Frontera. La celda libre conocida más cercana con una vecina desconocida.
- ⚠️ **Error frecuente:** Confundir frontera con obstáculo. Es una celda libre junto a lo desconocido (8.1)
- 🎯 **Por qué importa:** Con retardo de comunicación, el robot que decide qué explorar ahorra horas de operación. Medir cuánto ahorra una estrategia frente a otra permite justificar la autonomía a bordo.

📘 **Dónde se aprende** (1 clase): [B97-C16 · Autonomía de exploración](../programa/clases/B97/B97-C16-autonomia-de-exploracion/CLASE.md).

### Frontera de Pareto

- La frontera de Pareto reúne las no dominadas.

💡 **Cómo se explica en la clase [B124-C12](../programa/clases/B124/B124-C12-evaluacion-de-retorno-cientifico/CLASE.md):**
- *Descripción textual:* las capacidades y los pesos dan un valor científico que, junto con el costo, define la frontera de Pareto; esta se comprueba con dos algoritmos y se mide su pendiente marginal.
- 🎯 **Por qué importa:** El retorno científico no tiene un precio de mercado, pero se puede razonar con una función de valor explícita y una frontera de eficiencia. La decisión central: ¿qué opciones valen la pena a su costo y cuáles están dominadas?

📘 **Dónde se aprende** (1 clase): [B124-C12 · Evaluación de retorno científico](../programa/clases/B124/B124-C12-evaluacion-de-retorno-cientifico/CLASE.md).

### FSPL

- La FSPL es la pérdida en espacio libre.

💡 **Cómo se explica en la clase [B119-C09](../programa/clases/B119/B119-C09-derecho-y-normas-de-telecomunicaciones/CLASE.md):**
- Paso 2. Se despeja `FSPL` igual a ese margen.
- Paso 3. `d = 10^((FSPL − 20 log f − 32,45)/20) = 29654 km`.
- 🎯 **Por qué importa:** Ninguna clase anterior vincula el derecho de telecomunicaciones con el cálculo de interferencia; B120 trata licencias y espectro en detalle y esta clase fija el marco.

📘 **Dónde se aprende** (1 clase): [B119-C09 · Derecho y normas de telecomunicaciones](../programa/clases/B119/B119-C09-derecho-y-normas-de-telecomunicaciones/CLASE.md).

### Fuente

- La fuente `S` es la tasa de entrada de objetos.

💡 **Cómo se explica en la clase [B118-C10](../programa/clases/B118/B118-C10-sindrome-de-kessler-como-escenario/CLASE.md):**
- *Descripción textual:* tres términos (entrada, colisiones, reentrada) determinan la derivada de la población; si la fuente es menor que el valor crítico hay dos equilibrios, y si no, la población crece sin cota.
- Paso 1 · Fuente crítica. `S_c = 1/(4 × 5×10⁻⁷ × 625) = 800`.
- ⚠️ **Error frecuente:** Reducir solo la fuente y olvidar la vida orbital. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** El término cuadrático de las colisiones cambia la naturaleza del problema: por debajo de cierta fuente hay un equilibrio estable; por encima, no hay equilibrio. La decisión central: ¿qué parámetro (fuente, vida orbital, tasa de colisión) lleva el sistema al umbral y cómo se lee un escenario sin confundirlo con un pronóstico?

📘 **Dónde se aprende** (1 clase): [B118-C10 · Síndrome de Kessler como escenario](../programa/clases/B118/B118-C10-sindrome-de-kessler-como-escenario/CLASE.md).

### Fuente compacta binaria

- Una fuente compacta binaria es un par de estrellas de neutrones o agujeros negros.

🎯 **Por qué importa (clase B28-C07):** La tasa de eventos detectados depende del volumen que el detector ve, que crece como el cubo del alcance. Una mejora pequeña en sensibilidad se traduce en muchos más eventos.

📘 **Dónde se aprende** (1 clase): [B28-C07 · Fuentes compactas binarias](../programa/clases/B28/B28-C07-fuentes-compactas-binarias/CLASE.md).
