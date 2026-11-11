# Términos · R (parte 2 de 3)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · **R** · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-r.md) · **2** · [3](terminos-r-3.md)

### Regla R3

- La regla R3 de Holzmann pide no usar memoria dinámica tras la inicialización.

💡 **Cómo se explica en la clase [B88-C29](../programa/clases/B88/B88-C29-gestion-de-memoria-determinista-en-software-de-vuelo/CLASE.md):**
- Por montón con reglas: reservas al inicio.
- Enunciar la regla de no usar memoria dinámica tras la inicialización.
- 🎯 **Por qué importa:** Un montón puede fallar después de horas por fragmentación aunque haya memoria libre; un pool de bloques fijos no. La decisión central: ¿qué esquema de memoria garantiza que una asignación nunca falle en vuelo?

📘 **Dónde se aprende** (1 clase): [B88-C29 · Gestión de memoria determinista en software de vuelo](../programa/clases/B88/B88-C29-gestion-de-memoria-determinista-en-software-de-vuelo/CLASE.md).

### Regla voraz

- La regla voraz ordena los blancos.
- Una regla voraz asigna cada tarea al robot libre más barato.
- Una regla voraz elige por una razón local.

💡 **Cómo se explica en la clase [B29-C18](../programa/clases/B29/B29-C18-redes-de-seguimiento-temporal/CLASE.md):**
- El script [seguimiento.py](seguimiento.py) compara cuatro reglas con el óptimo exhaustivo y calcula la completitud (comprueba que el voraz nunca supera al óptimo).
- regla voraz razon media razon minima instancias optimas
- 🎯 **Por qué importa:** La regla de planificación determina cuánto valor científico se recoge. Una regla ingenua puede perder la mitad del valor; añadir telescopios no siempre compensa.

📘 **Dónde se aprende** (3 clases): [B29-C18 · Redes de seguimiento temporal](../programa/clases/B29/B29-C18-redes-de-seguimiento-temporal/CLASE.md); [B97-C09 · Robótica colaborativa](../programa/clases/B97/B97-C09-robotica-colaborativa/CLASE.md); [B104-C23 · Ejecución de experimentos a bordo: procedimientos y registro](../programa/clases/B104/B104-C23-ejecucion-de-experimentos-a-bordo-procedimientos-y-registro/CLASE.md).

### Reglamento de Radiocomunicaciones

- El Reglamento de Radiocomunicaciones de la UIT, con ediciones periódicas (la última consultada es la de 2024), contiene los cuadros de atribución y los procedimientos de coordinación y notificación de redes de satélites.

💡 **Cómo se explica en la clase [B89-C19](../programa/clases/B89/B89-C19-coordinacion-del-espectro-ante-itu/CLASE.md):**
- Describir qué coordina la UIT y qué contiene el Reglamento de Radiocomunicaciones.
- 🎯 **Por qué importa:** Sin coordinación no hay licencia ni protección: la separación orbital, la potencia y el diagrama de antena se negocian con números como los de esta clase. La decisión central: ¿qué separación orbital hace aceptable la interferencia de un sistema hacia otro?

📘 **Dónde se aprende** (1 clase): [B89-C19 · Coordinación del espectro ante ITU](../programa/clases/B89/B89-C19-coordinacion-del-espectro-ante-itu/CLASE.md).

### Reglas Opcionales

- Las Reglas Opcionales de la CPA (2011) se aplican cuando las partes acuerdan someter a ellas una controversia sobre una relación jurídica definida; no exige que la controversia sea «espacial» para tener competencia (art. 1).

🎯 **Por qué importa (clase B123-C04):** Elegir la vía condiciona plazo, costo, confidencialidad y fuerza obligatoria de la decisión. La decisión central: ¿qué vía y qué reglas conviene pactar, y con qué compromisos?

📘 **Dónde se aprende** (1 clase): [B123-C04 · Arbitraje y resolución de controversias espaciales](../programa/clases/B123/B123-C04-arbitraje-y-resolucion-de-controversias-espaciales/CLASE.md).

### Regolito

- El regolito es el suelo suelto de la Luna; el polvo es su fracción fina.
- Noche lunar: mitad del mes sinodico sin Sol (en un sitio ecuatorial sin sombras). Regolito: material suelto de la superficie.

💡 **Cómo se explica en la clase [B106-C19](../programa/clases/B106/B106-C19-arquitectura-de-asentamiento-lunar-conceptual/CLASE.md):**
- G["g = 1.62"] --> P["presion del regolito rho g h"]
- *Descripción textual:* la noche fija la energía almacenada; la gravedad baja la presión que ejerce el regolito, de modo que el casco sostiene la presión interior y la cubierta se reserva para blindaje y estabilidad térmica.
- ⚠️ **Error frecuente:** Suponer que el regolito contiene la presión. Ver 8.3.
- 🎯 **Por qué importa:** La Luna cambia las reglas: noches de dos semanas, gravedad de un sexto y un regolito que protege pero no contiene la presión. La decisión central: ¿qué recursos (energía, masa de cubierta, esfuerzo de excavación) exige un asentamiento enterrado y qué parte soporta cada elemento?

📖 **Explicado a fondo:** [Regolito](esencial/tercera-f-t.md#regolito) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B106-C19 · Arquitectura de asentamiento lunar conceptual](../programa/clases/B106/B106-C19-arquitectura-de-asentamiento-lunar-conceptual/CLASE.md); [B109-C04 · Mitigación de polvo lunar en accesos y hábitats](../programa/clases/B109/B109-C04-mitigacion-de-polvo-lunar-en-accesos-y-habitats/CLASE.md).

### Regolito seco

- El regolito seco por kilogramo de hielo es `(1 − x)/x`.

💡 **Cómo se explica en la clase [B59-C06](../programa/clases/B59/B59-C06-extraccion-y-procesamiento-de-volatiles/CLASE.md):**
- X["abundancia x"] --> M["regolito seco por kg de hielo"]
- Por kilogramo de agua hay `16,86 kg` de regolito seco; el calor total es `6,030 MJ` (regolito `3,003`, hielo `0,197`, sublimación `2,830`), o sea `1,675 kWh`; con captura del 50 %, `3,350 kWh/kg`.
- 🎯 **Por qué importa:** Con poco hielo hay que calentar mucha roca. La decisión central: ¿cuánta energía por kilogramo de agua pide una abundancia de 5,6 % frente a 2,7 %?

📘 **Dónde se aprende** (1 clase): [B59-C06 · Extracción y procesamiento de volátiles](../programa/clases/B59/B59-C06-extraccion-y-procesamiento-de-volatiles/CLASE.md).

### Regresión

- En clasificación la respuesta es una categoría (planeta o no); en regresión, un número (la masa, la temperatura).
- Una regresión compara resultados nuevos con valores de referencia.
- La regresión ajusta una tendencia para extrapolar.

💡 **Cómo se explica en la clase [B17-C02](../programa/clases/B17/B17-C02-aprendizaje-supervisado/CLASE.md):**
- Un modelo de regresión logística estima la probabilidad de la clase 1 como
- Distinguir clasificación y regresión, y entrenamiento, validación y prueba.
- 🎯 **Por qué importa:** Un modelo que clasifica señales como «candidata» o «no candidata» puede acertar el 100 % de los ejemplos con los que se entrenó y fallar la cuarta parte de los nuevos: memorizó. Lo que importa a un equipo científico es el desempeño en datos que el modelo no vio.

📘 **Dónde se aprende** (4 clases): [B17-C02 · Aprendizaje supervisado](../programa/clases/B17/B17-C02-aprendizaje-supervisado/CLASE.md); [B33-C13 · Pronóstico de actividad geomagnética](../programa/clases/B33/B33-C13-pronostico-de-actividad-geomagnetica/CLASE.md); [B50-C06 · Software de diseño óptico: modelos reproducibles y verificación](../programa/clases/B50/B50-C06-software-de-diseno-optico-modelos-reproducibles-y-verificacion/CLASE.md); [B97-C26 · Monitoreo de condición de maquinaria extraterrestre](../programa/clases/B97/B97-C26-monitoreo-de-condicion-de-maquinaria-extraterrestre/CLASE.md).

### Regresión de Arrhenius

- La regresión de Arrhenius ajusta `ln t` contra `1/T`.

🎯 **Por qué importa (clase B59-C12):** Una variación de 50 K en el horno cambia el tiempo de sinterización en un factor 2,6. La decisión central: ¿con qué precisión hay que controlar la temperatura, y cuánta energía cuesta alcanzarla?

📘 **Dónde se aprende** (1 clase): [B59-C12 · Sinterización de materiales](../programa/clases/B59/B59-C12-sinterizacion-de-materiales/CLASE.md).

### Regresión de rendimiento

- La regresión de rendimiento es una versión nueva más lenta que la anterior.

🎯 **Por qué importa (clase B18-C04):** Casi todo programa científico tiene un cuello de botella que el autor no sospecha. Optimizar a ojo suele mejorar lo que no importa.

📘 **Dónde se aprende** (1 clase): [B18-C04 · Perfilado de rendimiento](../programa/clases/B18/B18-C04-perfilado-de-rendimiento/CLASE.md).

### Regresión del nodo

- La regresión del nodo es el giro de `Ω` hacia el oeste (`dΩ/dt < 0`) en órbitas progradas.
- La regresión del nodo es `dΩ/dt < 0`.

💡 **Cómo se explica en la clase [B72-C03](../programa/clases/B72/B72-C03-perturbacion-j2-terrestre/CLASE.md):**
- Ejercicio 4 · autónomo. Estima el periodo de regresión del nodo de la órbita baja.
- 🎯 **Por qué importa:** J2 no cambia el semieje mayor ni la inclinación en promedio, pero hace girar el plano y el perigeo; con ello se diseñan órbitas heliosíncronas y Molniya. La decisión central: ¿cuánto se mueven `Ω` y `ω` por día en una órbita dada y cuánto confiar en la fórmula de primer orden?

📘 **Dónde se aprende** (2 clases): [B72-C03 · Perturbación J2 terrestre](../programa/clases/B72/B72-C03-perturbacion-j2-terrestre/CLASE.md); [B72-C04 · Precesión del nodo orbital](../programa/clases/B72/B72-C04-precesion-del-nodo-orbital/CLASE.md).

### Regresión dinámica

- La regresión dinámica modela `y` con sus propios retardos y con retardos de otras series.

💡 **Cómo se explica en la clase [B15-C21](../programa/clases/B15/B15-C21-series-temporales-multivariadas-y-regresion-dinamica/CLASE.md):**
- L --> M["Regresión dinámica<br/>y_t = a y_(t−1) + b x_(t−L) + e"]
- *Descripción textual:* el impulsor retardado y el pasado de la respuesta alimentan una regresión dinámica; se estiman coeficientes con sus errores, se elige el retardo con AIC y se contrasta con Granger si el impulsor ayuda a predecir; con series no estacionarias hay riesgo de regresión espuria.
- 🎯 **Por qué importa:** El índice Kp de actividad geomagnética se publica en intervalos de 3 horas y refleja las perturbaciones del campo magnético terrestre (S1). Un pronosticador quiere saber cuánto y con qué retardo responde ese índice a una variable del viento solar.

📘 **Dónde se aprende** (1 clase): [B15-C21 · Series temporales multivariadas y regresión dinámica](../programa/clases/B15/B15-C21-series-temporales-multivariadas-y-regresion-dinamica/CLASE.md).

### Regresión espuria

- La regresión espuria es la relación aparente entre series no estacionarias independientes.

💡 **Cómo se explica en la clase [B15-C21](../programa/clases/B15/B15-C21-series-temporales-multivariadas-y-regresion-dinamica/CLASE.md):**
- N["Series no estacionarias"] -.-> P["Regresión espuria"]
- *Descripción textual:* el impulsor retardado y el pasado de la respuesta alimentan una regresión dinámica; se estiman coeficientes con sus errores, se elige el retardo con AIC y se contrasta con Granger si el impulsor ayuda a predecir; con series no estacionarias hay riesgo de regresión espuria.
- 🎯 **Por qué importa:** El índice Kp de actividad geomagnética se publica en intervalos de 3 horas y refleja las perturbaciones del campo magnético terrestre (S1). Un pronosticador quiere saber cuánto y con qué retardo responde ese índice a una variable del viento solar.

📘 **Dónde se aprende** (1 clase): [B15-C21 · Series temporales multivariadas y regresión dinámica](../programa/clases/B15/B15-C21-series-temporales-multivariadas-y-regresion-dinamica/CLASE.md).

### Regresión nodal por J₂

- La regresión nodal por `J₂` es `Ω̇ = −(3/2) J₂ (R/a)² n` y la precesión apsidal por `J₂`, `ϖ̇ ≈ 3 J₂ (R/a)² n`.

💡 **Cómo se explica en la clase [B73-C19](../programa/clases/B73/B73-C19-mecanica-de-sistemas-lunares/CLASE.md):**
- Calcular la regresión nodal y la precesión apsidal por `J₂` de una luna.
- Añadir la regresión nodal solar y definir el radio de Laplace.
- 🎯 **Por qué importa:** Un sistema lunar es un problema de varios perturbadores: el achatamiento del planeta aleja los nodos y los ápsides, el Sol los tira, y las lunas se perturban entre sí. Saber cuál domina a cada distancia decide en qué plano y con qué precesión se mueve una luna.

📘 **Dónde se aprende** (1 clase): [B73-C19 · Mecánica de sistemas lunares](../programa/clases/B73/B73-C19-mecanica-de-sistemas-lunares/CLASE.md).

### Regresión nodal solar

- La regresión nodal solar de un perturbador circular es `−(3/4) n_p²/n`.

💡 **Cómo se explica en la clase [B73-C19](../programa/clases/B73/B73-C19-mecanica-de-sistemas-lunares/CLASE.md):**
- Añadir la regresión nodal solar y definir el radio de Laplace.
- 🎯 **Por qué importa:** Un sistema lunar es un problema de varios perturbadores: el achatamiento del planeta aleja los nodos y los ápsides, el Sol los tira, y las lunas se perturban entre sí. Saber cuál domina a cada distancia decide en qué plano y con qué precesión se mueve una luna.

📘 **Dónde se aprende** (1 clase): [B73-C19 · Mecánica de sistemas lunares](../programa/clases/B73/B73-C19-mecanica-de-sistemas-lunares/CLASE.md).

### Regresión softmax

- La regresión softmax modela la probabilidad de cada clase con `p_k = exp(z_k)/Σ exp(z_j)`, `z = x W`.

💡 **Cómo se explica en la clase [B103-C05](../programa/clases/B103/B103-C05-segmentacion-semantica-de-superficies-planetarias/CLASE.md):**
- Seis imágenes sintéticas de 128 × 128 px con cuatro clases (arena 44,2 %, lecho 44,4 %, roca 8,1 %, sombra 3,3 %) entrenan una regresión softmax con seis características por píxel.
- Entrenar una regresión softmax multiclase con descenso de gradiente.
- 🎯 **Por qué importa:** Un modelo que acierta el 91 % de los píxeles en el dominio de entrenamiento puede acertar el 45 % cuando cambia la luz. La decisión central: ¿qué métrica y qué prueba demuestran que un segmentador es utilizable en otras condiciones, y no solo en las de entrenamiento?

📘 **Dónde se aprende** (1 clase): [B103-C05 · Segmentación semántica de superficies planetarias](../programa/clases/B103/B103-C05-segmentacion-semantica-de-superficies-planetarias/CLASE.md).

### Regreso

- El regreso es la reclamación entre responsables.

💡 **Cómo se explica en la clase [B119-C03](../programa/clases/B119/B119-C03-convenio-de-responsabilidad/CLASE.md):**
- Si A no puede pagar, B paga `100.0` u.m. a la víctima; su cuota interna es `30.0`; reclama a A el regreso de `70.0` u.m.
- *Descripción textual:* la víctima cobra el total de cualquier responsable solvente; después los Estados se reparten la carga según su culpa y el que pagó de más reclama el regreso.
- ⚠️ **Error frecuente:** Olvidar el regreso. Se corrige con el ejercicio 4.
- 🎯 **Por qué importa:** El art. VII del tratado de 1967 (no discutido en la fuente de C01) fundamenta la responsabilidad; el convenio de 1972 la desarrolla, y la cuantificación del daño se trata en el bloque de reclamaciones (B123); esta clase fija la regla de reparto.

📘 **Dónde se aprende** (1 clase): [B119-C03 · Convenio de Responsabilidad](../programa/clases/B119/B119-C03-convenio-de-responsabilidad/CLASE.md).

### Regular

- Una matriz es singular si su determinante es 0, y regular en caso contrario.

💡 **Cómo se explica en la clase [B10-C04](../programa/clases/B10/B10-C04-determinantes-y-soluciones/CLASE.md):**
- B -->|"≠ 0"| C["Regular: invertible,<br/>solución única de A x = b"]
- 🎯 **Por qué importa:** Dos estaciones terrestres miden la dirección hacia un mismo objeto y quieren fijar su posición cruzando las visuales. Si el objeto está cerca y las visuales forman un buen ángulo, el cruce es nítido.

📘 **Dónde se aprende** (1 clase): [B10-C04 · Determinantes y soluciones](../programa/clases/B10/B10-C04-determinantes-y-soluciones/CLASE.md).

### Regularidad

- Una regularidad es un patrón que se repite en los registros.

💡 **Cómo se explica en la clase [B02-C02](../programa/clases/B02/B02-C02-observacion-mesopotamica-y-egipcia/CLASE.md):**
- A["Registro largo<br/>de eclipses"] --> B["Regularidad:<br/>intervalo ≈ 6 585 d"]
- *Descripción textual:* de un registro largo de eclipses sale una regularidad (un intervalo de unos 6 585 días); de ella pueden surgir una explicación por casi-igualdad de tres períodos lunares y un uso predictivo con incertidumbre.
- 🎯 **Por qué importa:** Una predicción necesita una larga memoria. Para decir que un fenómeno volverá, alguien tuvo que anotarlo muchas veces y compararlo.

📘 **Dónde se aprende** (1 clase): [B02-C02 · Observación mesopotámica y egipcia](../programa/clases/B02/B02-C02-observacion-mesopotamica-y-egipcia/CLASE.md).

### Regularización

- La regularización limita la solución para controlar el ruido; en RL, el número de iteraciones «hace de regularización» (S2).
- La regularización limita las soluciones posibles para evitar que el relleno invente estructura.
- La regularización con corte exponencial.

💡 **Cómo se explica en la clase [B15-C19](../programa/clases/B15/B15-C19-reconstruccion-por-datos-incompletos/CLASE.md):**
- Gerchberg–Papoulis sin regularización; 300 repeticiones para los errores con ruido.
- 🎯 **Por qué importa:** Si falta el 8 % de una serie, ¿se puede rellenar sin contaminar el análisis? Depende de lo que se sepa de la señal: si es suave y se conoce su forma, el relleno es casi exacto; si es un evento breve que cayó en el hueco, no hay método que lo recupere.

📘 **Dónde se aprende** (5 clases): [B15-C11 · Deconvolución y enfoque](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md); [B15-C19 · Reconstrucción por datos incompletos](../programa/clases/B15/B15-C19-reconstruccion-por-datos-incompletos/CLASE.md); [B31-C19 · Vacío cuántico y límites conceptuales](../programa/clases/B31/B31-C19-vacio-cuantico-y-limites-conceptuales/CLASE.md); [B42-C19 · Reconstrucción de imágenes](../programa/clases/B42/B42-C19-reconstruccion-de-imagenes/CLASE.md); [B42-C22 · Reconstructores de frente de onda: zonal y modal](../programa/clases/B42/B42-C22-reconstructores-de-frente-de-onda-zonal-y-modal/CLASE.md).

### Regularización de Tikhonov

- La regularización de Tikhonov minimiza `‖A f − d‖² + λ‖f‖²`.

🎯 **Por qué importa (clase B37-C10):** Los datos son pocos y ruidosos y las incógnitas muchas. La decisión central: ¿cuánta regularización aplicar para no ajustar el ruido ni borrar la señal?

📘 **Dónde se aprende** (1 clase): [B37-C10 · Inversión asterosísmica de perfiles internos](../programa/clases/B37/B37-C10-inversion-asterosismica-de-perfiles-internos/CLASE.md).

### Reingreso

- El reingreso es el paso por la atmósfera hacia el aterrizaje.

💡 **Cómo se explica en la clase [B104-C19](../programa/clases/B104/B104-C19-operaciones-de-retorno-y-reintegracion/CLASE.md):**
- Nada más sobre reingreso se consultó; la fórmula y la atmósfera son modelos estándar verificados por el laboratorio.
- Una cápsula con sustentación o un reingreso con salto controla el ángulo efectivo; esa guía no se modela aquí.
- ⚠️ **Error frecuente:** Mezclar reingreso y reintegración. Son fases distintas (8.5).
- 🎯 **Por qué importa:** Un ángulo de entrada más empinado reduce el calentamiento total pero aumenta la desaceleración. La decisión central: ¿cuántos g máximos soporta la tripulación según el ángulo de entrada, y por qué ese máximo no depende de la masa de la nave?

📘 **Dónde se aprende** (1 clase): [B104-C19 · Operaciones de retorno y reintegración](../programa/clases/B104/B104-C19-operaciones-de-retorno-y-reintegracion/CLASE.md).

### Reiniciar y ejecutar todo

- El estado oculto es el conjunto de variables que existen en el kernel y que no se ven en el texto del cuaderno: pueden haber sido creadas por celdas borradas o ejecutadas en otro orden. Reiniciar y ejecutar todo (*restart and run all*) borra el estado y ejecuta las celdas de arriba abajo.

💡 **Cómo se explica en la clase [B14-C09](../programa/clases/B14/B14-C09-jupyter-y-experimentos-reproducibles/CLASE.md):**
- Quien lea tu cuaderno después de «reiniciar y ejecutar todo» obtendrá 1,000214, no 1,000193, aunque la pantalla anterior mostrara este último.
- A -->|"reiniciar y ejecutar todo"| L["Kernel nuevo"]
- ⚠️ **Error frecuente:** Compartir sin reiniciar y ejecutar todo. Se corrige con el ejercicio 9 y la sección 13.
- 🎯 **Por qué importa:** Alguien te manda un cuaderno con un gráfico que apoya una conclusión. Lo abres, ejecutas las celdas y el gráfico sale distinto.

📘 **Dónde se aprende** (1 clase): [B14-C09 · Jupyter y experimentos reproducibles](../programa/clases/B14/B14-C09-jupyter-y-experimentos-reproducibles/CLASE.md).

### Reinicio

- El reinicio aplica `δq = [δθ/2; 1]` y pone `δθ = 0`.

💡 **Cómo se explica en la clase [B87-C10](../programa/clases/B87/B87-C10-filtro-de-actitud/CLASE.md):**
- ⚠️ **Error frecuente:** Olvidar el reinicio. Aplica `δq` y pon `δθ = 0` (8.2)
- 🎯 **Por qué importa:** Un giroscopio sin corregir se desvía decenas de grados en minutos; un vector solo da `~1°` por época. La decisión central: ¿cómo se combinan para obtener una actitud mejor que cada uno, y cómo se sabe que el filtro es honesto?

📘 **Dónde se aprende** (1 clase): [B87-C10 · Filtro de actitud](../programa/clases/B87/B87-C10-filtro-de-actitud/CLASE.md).

### Reinicio falso

- El reinicio falso ocurre con el software sano.

💡 **Cómo se explica en la clase [B88-C11](../programa/clases/B88/B88-C11-watchdogs-y-recuperacion/CLASE.md):**
- Con jitter `σ = 5 ms` no hay reinicios falsos en 200 000 ciclos; con `σ = 10 ms` hay 9; con `20 ms`, 9132 (4,57 %); con `30 ms`, 36 481 (18,2 %).
- Descripción larga: la tasa de reinicios falsos crece de forma abrupta cuando el jitter se acerca al margen de la ventana.
- 🎯 **Por qué importa:** Un watchdog mal ajustado reinicia sin necesidad o no reinicia cuando hace falta. La decisión central: ¿qué ventana y qué escalera de acciones recuperan un software colgado sin reinicios falsos?

📘 **Dónde se aprende** (1 clase): [B88-C11 · Watchdogs y recuperación](../programa/clases/B88/B88-C11-watchdogs-y-recuperacion/CLASE.md).

### Reintegración

- La reintegración es repetir la propagación con un método independiente.
- La reintegración es la fase posterior al aterrizaje: recuperación, evaluación y readaptación.

💡 **Cómo se explica en la clase [B75-C30](../programa/clases/B75/B75-C30-validacion-de-maniobras-por-reintegracion/CLASE.md):**
- La evidencia es tu informe de reintegración de una maniobra del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *informe de reintegración de una maniobra* con las cinco comprobaciones, sus resultados y qué demuestra y qué no cada una.
- 🎯 **Por qué importa:** Un número de una hoja de cálculo no es una trayectoria validada. La decisión central: ¿qué comprobaciones demuestran que el impulso y la trayectoria que sigue son coherentes y que el integrador es fiable?

📘 **Dónde se aprende** (2 clases): [B75-C30 · Validación de maniobras por reintegración](../programa/clases/B75/B75-C30-validacion-de-maniobras-por-reintegracion/CLASE.md); [B104-C19 · Operaciones de retorno y reintegración](../programa/clases/B104/B104-C19-operaciones-de-retorno-y-reintegracion/CLASE.md).

### Reintento

- Un reintento repite una etapa tras un fallo transitorio.
- El reintento espera a que `tx_libre()` sea verdadero.
- Percentil: valor de la duración con cierta probabilidad de no ser superado. Reintento: repetir un ensayo tras retrabajo.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B14-C30](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md):**
- Con 2 fallos inyectados en `procesar`, la cadena termina bien tras 2 reintentos (registro: 4 etapas ejecutadas, `reintento 1` y `reintento 2`).
- Cada etapa de cada lote deja una línea: ejecutada, saltada, reintento, detenida por calidad o fallo definitivo.
- 🎯 **Por qué importa:** Cada madrugada llegan datos nuevos. Si un humano debe lanzar cada paso, tarde o temprano se olvida uno; si un lote corrupto atraviesa la cadena, contamina el producto final; si un fallo de red detiene todo y al reiniciar se repite desde cero, se pierde tiempo.

📘 **Dónde se aprende** (4 clases): [B14-C30 · Cadenas de procesamiento automatizado de datos](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md); [B88-C24 · Capa de abstracción de hardware (HAL) y controladores](../programa/clases/B88/B88-C24-capa-de-abstraccion-de-hardware-hal-y-controladores/CLASE.md); [B90-C20 · Campaña conceptual de calificación de CubeSat](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md); [B96-C14 · Procedimientos de recuperación](../programa/clases/B96/B96-C14-procedimientos-de-recuperacion/CLASE.md).

### Rejilla

- La rejilla es el electrodo perforado que extrae y acelera los iones.

💡 **Cómo se explica en la clase [B78-C07](../programa/clases/B78/B78-C07-motores-ionicos/CLASE.md):**
- Descripción larga: la velocidad crece con `V^(1/2)` y la densidad de corriente con `V^(3/2)`; el empuje por unidad de área de rejilla crece con `V`.
- Calcular el área de rejilla mínima para un empuje dado.
- 🎯 **Por qué importa:** La velocidad de escape iónica crece con la raíz de la tensión, pero la corriente que cabe en una rejilla está limitada por la carga espacial. La decisión central: ¿qué tensión y qué área de rejilla se necesitan para un empuje dado y qué fracción del propelente llega a ser ion?

📘 **Dónde se aprende** (1 clase): [B78-C07 · Motores iónicos](../programa/clases/B78/B78-C07-motores-ionicos/CLASE.md).

### Rejilla de costos

- Una rejilla de costos asigna un costo a cada celda.

💡 **Cómo se explica en la clase [B97-C08](../programa/clases/B97/B97-C08-planificacion-de-trayectorias-roboticas/CLASE.md):**
- Representar un terreno como rejilla de costos con obstáculos.
- Límites: rejilla 2D, vehículo puntual sin dinámica ni incertidumbre, costos constantes.
- 🎯 **Por qué importa:** Con retardo de comunicación y poca energía, la ruta debe salir buena a la primera. A* garantiza la ruta de costo mínimo si la heurística es admisible, y ahorra cómputo, que a bordo es escaso.

📘 **Dónde se aprende** (1 clase): [B97-C08 · Planificación de trayectorias robóticas](../programa/clases/B97/B97-C08-planificacion-de-trayectorias-roboticas/CLASE.md).

### Rejilla de elevación (2.5D)

- Recorte (clamping): límites `l_min`, `l_max` que mantienen la capacidad de cambiar de opinión (F5). Rejilla de elevación (2.5D): un valor de altura por celda (F5).

💡 **Cómo se explica en la clase [B99-C05](../programa/clases/B99/B99-C05-mapas-de-ocupacion-y-rejillas-de-elevacion/CLASE.md):**
- En un terreno de 8° con una roca de 0,4 m, la rejilla de elevación de 0,5 m recupera la pendiente en 7,98° y declara no traversables 8 de las 12 celdas de la roca.
- Construir una rejilla de elevación y calcular pendiente y rugosidad por celda.
- ⚠️ **Error frecuente:** Suponer que la rejilla de elevación sirve para cualquier entorno. Solo si hay una superficie por celda (8.1).
- 🎯 **Por qué importa:** Un mapa útil para navegar distingue lo ocupado, lo libre y lo que no se sabe, y dice si el terreno es pisable. La decisión central: ¿cómo fusionar medidas ruidosas en cada celda y qué umbrales de pendiente y rugosidad declaran un terreno traversable?

📘 **Dónde se aprende** (1 clase): [B99-C05 · Mapas de ocupación y rejillas de elevación](../programa/clases/B99/B99-C05-mapas-de-ocupacion-y-rejillas-de-elevacion/CLASE.md).

### Rejilla de Fibonacci

- La rejilla de Fibonacci reparte puntos casi uniformes.

💡 **Cómo se explica en la clase [B28-C10](../programa/clases/B28/B28-C10-localizacion-probabilistica-de-eventos/CLASE.md):**
- Construir una rejilla de Fibonacci sobre la esfera.
- El script [localizacion.py](localizacion.py) construye el posterior en una rejilla de Fibonacci, calcula la región del 90 % y la cobertura en 400 ensayos (comprueba entre 0,84 y 0,96).
- 🎯 **Por qué importa:** El área de localización decide cuántas fotos hacen falta para encontrar la contrapartida. Un mapa mal calibrado engaña.

📘 **Dónde se aprende** (1 clase): [B28-C10 · Localización probabilística de eventos](../programa/clases/B28/B28-C10-localizacion-probabilistica-de-eventos/CLASE.md).

### Rejilla de frecuencias

- La rejilla de frecuencias del CCSDS 141.0-B-1 es `193,1 + n × 0,1 THz` con `n` de −18 a 28.
- La rejilla de frecuencias cubre el rango de búsqueda.

💡 **Cómo se explica en la clase [B29-C14](../programa/clases/B29/B29-C14-estrellas-variables-periodicas/CLASE.md):**
- El script [periodicas.py](periodicas.py) ajusta armónicos en una rejilla de frecuencias, calcula PDM (comprueba `10⁻³`) y simula 60 sinusoides (comprueba 30 % en `σ_P`).
- 🎯 **Por qué importa:** El periodo es la propiedad básica de una variable periódica; de él y de la forma de la curva se deducen la masa, la edad o la distancia en muchos casos. La decisión central: ¿qué periodo y qué incertidumbre da la serie y qué métodos coinciden?

📘 **Dónde se aprende** (2 clases): [B29-C14 · Estrellas variables periódicas](../programa/clases/B29/B29-C14-estrellas-variables-periodicas/CLASE.md); [B92-C01 · Fuentes láser y amplificadores para enlaces espaciales](../programa/clases/B92/B92-C01-fuentes-laser-y-amplificadores-para-enlaces-espaciales/CLASE.md).

### Rejilla de modelos

- Una rejilla de modelos es un conjunto de modelos en un espacio de parámetros.

🎯 **Por qué importa (clase B37-C14):** Las capas superficiales cambian las frecuencias de modo sistemático. La decisión central: ¿se corrige el efecto de superficie y qué parámetros se recuperan con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B37-C14 · Ajuste de modelos estelares a frecuencias sísmicas](../programa/clases/B37/B37-C14-ajuste-de-modelos-estelares-a-frecuencias-sismicas/CLASE.md).

### Rejilla de ocupación

- Rejilla de ocupación: malla de celdas con probabilidad de estar ocupadas (F5).

💡 **Cómo se explica en la clase [B99-C05](../programa/clases/B99/B99-C05-mapas-de-ocupacion-y-rejillas-de-elevacion/CLASE.md):**
- C --> E["Rejilla de ocupacion<br/>log-odds con recorte"]
- *Descripción textual:* cada rayo marca libres las celdas que atraviesa y ocupada la última; las sumas en log-odds forman la rejilla de ocupación; en paralelo, la nube de puntos 3D da una altura media por celda, de la que salen pendiente, rugosidad y traversabilidad; ambos mapas alimentan la planificación.
- 🎯 **Por qué importa:** Un mapa útil para navegar distingue lo ocupado, lo libre y lo que no se sabe, y dice si el terreno es pisable. La decisión central: ¿cómo fusionar medidas ruidosas en cada celda y qué umbrales de pendiente y rugosidad declaran un terreno traversable?

📘 **Dónde se aprende** (1 clase): [B99-C05 · Mapas de ocupación y rejillas de elevación](../programa/clases/B99/B99-C05-mapas-de-ocupacion-y-rejillas-de-elevacion/CLASE.md).

### Rejilla de periodos

- La rejilla de periodos es geométrica.

💡 **Cómo se explica en la clase [B29-C20](../programa/clases/B29/B29-C20-proyecto-de-deteccion-exoplanetaria/CLASE.md):**
- Esta clase no reproduce ese análisis: genera `720` muestras (cadencia de 2 h, 60 d, ruido `400 ppm`) y busca periodos entre `2` y `20 d` con una rejilla de `1153` valores.
- 🎯 **Por qué importa:** Una detección sin completitud no se puede contar: ¿cuántos planetas se perdieron? La inyección y recuperación responde.

📘 **Dónde se aprende** (1 clase): [B29-C20 · Proyecto de detección exoplanetaria](../programa/clases/B29/B29-C20-proyecto-de-deteccion-exoplanetaria/CLASE.md).

### Rejilla de χ²

- La rejilla de χ² busca la posición.

💡 **Cómo se explica en la clase [B45-C24](../programa/clases/B45/B45-C24-fotometria-por-ajuste-de-psf/CLASE.md):**
- La posición de la segunda estrella, ajustada por rejilla y parábola, tiene desplazamiento medio `-0,0031` píxeles y dispersión `0,2511` píxeles: muy mal determinada por la mezcla.
- 🎯 **Por qué importa:** La apertura sesga los flujos de estrellas próximas y el ajuste de PSF los separa. La decisión central: ¿qué sesgo evita el ajuste y con qué incertidumbre y correlación?

📘 **Dónde se aprende** (1 clase): [B45-C24 · Fotometría por ajuste de PSF](../programa/clases/B45/B45-C24-fotometria-por-ajuste-de-psf/CLASE.md).

### Rejilla fina

- La rejilla fina es una discretización con muchos puntos que se usa como «realidad» simulada; la gruesa, la que usa el inversor.

💡 **Cómo se explica en la clase [B22-C05](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md):**
- Generar el espectro con una rejilla de temperaturas más fina (por ejemplo, 70 temperaturas) o con una distribución continua y emisividad ligeramente distinta, e invertir con la rejilla de 15; barrer el ruido y la forma de la distribución; contar si los intervalos cubren.
- 🎯 **Por qué importa:** Con datos reales no conoces la verdad, así que no puedes medir el error de tu inversión. Con datos sintéticos sí: tú fijas la verdad, generas los datos y miras si el método la recupera.

📘 **Dónde se aprende** (1 clase): [B22-C05 · Pruebas de inversión con datos sintéticos](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md).

### Relación área–Mach

- La relación área–Mach es `A/A* = (1/M)[(2/(γ+1))(1 + (γ−1)M²/2)]^((γ+1)/(2(γ−1)))`, donde `A*` es el área donde `M = 1`.

💡 **Cómo se explica en la clase [B79-C06](../programa/clases/B79/B79-C06-flujos-supersonicos/CLASE.md):**
- *Descripción textual:* el Mach supersónico determina la relación de áreas, el ángulo de Mach y la función de Prandtl–Meyer; las dos relaciones se verifican con integrales numéricas.
- Verificar la relación área–Mach integrando su ecuación diferencial.
- 🎯 **Por qué importa:** El comportamiento de un flujo a `M > 1` en toberas y vehículos no lo trata ninguna clase del tronco. Sin él no se entiende por qué una tobera necesita una parte divergente.

📘 **Dónde se aprende** (1 clase): [B79-C06 · Flujos supersónicos](../programa/clases/B79/B79-C06-flujos-supersonicos/CLASE.md).

### Relación asintótica

- La relación asintótica `tan[π(ν − ν_p)/Δν] = q tan[π(1/(νΔΠ₁) − ε_g)]`.

💡 **Cómo se explica en la clase [B37-C12](../programa/clases/B37/B37-C12-gigantes-rojas-oscilantes-y-modos-mixtos/CLASE.md):**
- La relación asintótica es una forma estándar con `q` constante; los espectros reales exigen ajustar también `q`, `ε_g` y el efecto de la rotación (C11).
- 🎯 **Por qué importa:** El espaciado de los períodos mixtos revela el núcleo. La decisión central: ¿cuántos modos mixtos hay por orden p y cómo distingue `ΔΠ₁` la rama de gigantes del núcleo de helio?

📘 **Dónde se aprende** (1 clase): [B37-C12 · Gigantes rojas oscilantes y modos mixtos](../programa/clases/B37/B37-C12-gigantes-rojas-oscilantes-y-modos-mixtos/CLASE.md).

### Relación ciega

- Una relación ciega a un defecto es una que el programa defectuoso sigue cumpliendo.

💡 **Cómo se explica en la clase [B23-C06](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md):**
- Las relaciones metamórficas no necesitan oráculo y se derivan de simetrías y unidades, pero son ciegas a defectos coherentes.
- Construir una matriz «defecto × relación» y reconocer los defectos a los que las relaciones son ciegas.
- 🎯 **Por qué importa:** El movimiento de un satélite con achatamiento terrestre (J2) no tiene solución cerrada, y tu código no tiene un valor correcto con el que compararse.

📘 **Dónde se aprende** (1 clase): [B23-C06 · Pruebas metamórficas](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md).

### Relación C/N₀

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C18):** Los datos que no caben en un paso se pierden o se acumulan. La decisión central: ¿cuántos bits por paso admite el enlace con margen suficiente?

📘 **Dónde se aprende** (1 clase): [B47-C18 · Downlink de instrumentos científicos](../programa/clases/B47/B47-C18-downlink-de-instrumentos-cientificos/CLASE.md).

### Relación de áreas

- La relación de áreas `A_c/A_a` decide la densidad de corriente anódica.

💡 **Cómo se explica en la clase [B84-C21](../programa/clases/B84/B84-C21-compatibilidad-quimica-y-galvanica-de-materiales/CLASE.md):**
- Descripción larga: la corrosión del ánodo crece con la relación de áreas, pero más despacio (saturación) cuando el cátodo ya domina.
- Integrador. Elabora tu *matriz de compatibilidad galvánica de pares*: `ΔV` de seis pares, regla, efecto de la relación de áreas y medidas de aislamiento, rotulando lo ilustrativo.
- ⚠️ **Error frecuente:** Ignorar la relación de áreas. Se corrige con 8.2.
- 🎯 **Por qué importa:** Un tornillo de acero inoxidable en un panel de aluminio puede corroerlo 90 veces más rápido que otro de aluminio, y la corrosión ocurre en tierra, antes del lanzamiento. La decisión central: ¿qué pares de materiales pueden ir en contacto y cómo debe ser la relación de áreas?

📘 **Dónde se aprende** (1 clase): [B84-C21 · Compatibilidad química y galvánica de materiales](../programa/clases/B84/B84-C21-compatibilidad-quimica-y-galvanica-de-materiales/CLASE.md).

### Relación de Bohm–Gross

- La relación de Bohm–Gross `ω² = ω_p² + 3k²v_th²`.

💡 **Cómo se explica en la clase [B30-C08](../programa/clases/B30/B30-C08-frecuencias-y-ondas-de-plasma/CLASE.md):**
- El script [ondas.py](ondas.py) calcula `f_p`, `f_c`, `v_g`, `v_f`, el retardo por cuadratura y por columna y la relación de Bohm–Gross (comprueba el coeficiente a `10⁻³` y el retardo a `10⁻⁴`).
- 🎯 **Por qué importa:** La radiación de las erupciones se emite cerca de la frecuencia de plasma local, de modo que una frecuencia es una altura. La decisión central: ¿qué frecuencia corresponde a cada densidad y cuánto se retrasa una señal?

📘 **Dónde se aprende** (1 clase): [B30-C08 · Frecuencias y ondas de plasma](../programa/clases/B30/B30-C08-frecuencias-y-ondas-de-plasma/CLASE.md).

### Relación de Dessler–Parker–Sckopke

- La relación de Dessler–Parker–Sckopke liga la energía del anillo con la perturbación del campo.

💡 **Cómo se explica en la clase [B30-C22](../programa/clases/B30/B30-C22-anillo-de-corriente-y-corrientes-magnetosfericas/CLASE.md):**
- Es un resultado con `B₀` ilustrativo y la relación de Dessler–Parker–Sckopke, no una medición.
- El script [anillo.py](anillo.py) calcula la energía del dipolo (cerrada y 2D) y aplica Dessler–Parker–Sckopke (comprueba `10⁻⁵` en la integral y `10⁻¹²` en la relación inversa).
- 🎯 **Por qué importa:** El índice Dst (B30-C23) es un indicador de la energía del anillo de corriente. La decisión central: ¿qué energía y qué corriente corresponden a una disminución dada del campo?

📘 **Dónde se aprende** (1 clase): [B30-C22 · Anillo de corriente y corrientes magnetosféricas](../programa/clases/B30/B30-C22-anillo-de-corriente-y-corrientes-magnetosfericas/CLASE.md).

### Relación de dispersión

- El número de onda `k = 2π/λ` y la frecuencia angular `ω` se relacionan con `ω = ck`: es la relación de dispersión.
- La relación de dispersión vincula `ω` y `k`.

💡 **Cómo se explica en la clase [B21-C02](../programa/clases/B21/B21-C02-ecuacion-de-onda-esquemas-y-dispersion-numerica/CLASE.md):**
- C --> D["Relación de dispersión discreta<br/>sin(ωΔt/2) = ν sin(kΔx/2)"]
- *Descripción textual:* de la ecuación continua se pasa a una malla; el esquema de salto de rana se escribe con tres niveles de tiempo; al probar ondas senoidales se obtiene la relación de dispersión discreta, de la que se leen la velocidad de fase numérica y el límite de estabilidad.
- 🎯 **Por qué importa:** Casi toda señal que viaja en el espacio —ondas de radio, ondas de Alfvén en la corona solar, ondas sísmicas en una luna, vibraciones de una estructura— obedece alguna forma de la ecuación de onda.

📘 **Dónde se aprende** (2 clases): [B21-C02 · Ecuación de onda: esquemas y dispersión numérica](../programa/clases/B21/B21-C02-ecuacion-de-onda-esquemas-y-dispersion-numerica/CLASE.md); [B35-C03 · Inestabilidades de plasma: cinéticas y de fluido](../programa/clases/B35/B35-C03-inestabilidades-de-plasma-cineticas-y-de-fluido/CLASE.md).

### Relación de escala

- Una relación de escala da `Δν ∝ M¹ᐟ² R⁻³ᐟ²` y `ν_max ∝ M R⁻² T_ef⁻¹ᐟ²`.

💡 **Cómo se explica en la clase [B37-C09](../programa/clases/B37/B37-C09-frecuencias-caracteristicas-max-y-espaciado-de-periodos/CLASE.md):**
- *Descripción textual:* las relaciones de escala convierten dos observables sísmicos globales en masa y radio.
- Aplicar las relaciones de escala de `Δν` y `ν_max`.
- 🎯 **Por qué importa:** Sin Δν y νmax habría que ajustar modelos para saber masa y radio. La decisión central: ¿qué precisión en masa y radio se obtiene con estos observables y qué supuestos exige?

📘 **Dónde se aprende** (1 clase): [B37-C09 · Frecuencias características: Δν, νmax y espaciado de períodos](../programa/clases/B37/B37-C09-frecuencias-caracteristicas-max-y-espaciado-de-periodos/CLASE.md).

### Relación de estimación de costo (CER)

- Una relación de estimación de costo (CER) es una ecuación que da el costo en función de un atributo.

💡 **Cómo se explica en la clase [B124-C05](../programa/clases/B124/B124-C05-estimacion-de-costos-de-mision/CLASE.md):**
- El NASA Cost Estimating Handbook v4.0 (febrero de 2015) es la guía de la agencia para estimar costos; su apéndice E menciona relaciones de estimación de costo (CER) y reportes de curvas de aprendizaje, y su glosario dice que, en la teoría de la curva de aprendizaje, la primera unidad es la más cara.
- 🎯 **Por qué importa:** Un costo sin banda de incertidumbre parece más preciso de lo que es. La decisión central: ¿cuánto cuesta esta misión, con qué banda y cuánto baja el costo unitario si se fabrican varias unidades?

📘 **Dónde se aprende** (1 clase): [B124-C05 · Estimación de costos de misión](../programa/clases/B124/B124-C05-estimacion-de-costos-de-mision/CLASE.md).

### Relación de expansión

- La relación de expansión `ε = A_e/A_t`.

💡 **Cómo se explica en la clase [B79-C08](../programa/clases/B79/B79-C08-flujo-en-toberas-convergente-divergentes/CLASE.md):**
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de diseño de una tobera*: garganta, tabla de dos relaciones de expansión con `M_e`, `V_e`, `F`, `C_F`, `I_sp`, regímenes por contrapresión y lista de qué es consultado e ilustrativo.
- El script [tobera.py](tobera.py) calcula la garganta, dos relaciones de expansión (Mach de salida, empuje, `C_F`, `I_sp`), las contrapresiones características y las diferencias entre vías (comprueba diferencia < 1e-10).
- 🎯 **Por qué importa:** B78-C03 trata la cámara pero no el flujo por la tobera. La teoría de expansión es lo que une la presión de cámara con el empuje.

📘 **Dónde se aprende** (1 clase): [B79-C08 · Flujo en toberas convergente-divergentes](../programa/clases/B79/B79-C08-flujo-en-toberas-convergente-divergentes/CLASE.md).

### Relación de humedad w

- Punto de rocío: `T` con `e_s(T_d) = p_v`. Relación de humedad `w`: `0,622 p_v/(P − p_v)`.

💡 **Cómo se explica en la clase [B106-C07](../programa/clases/B106/B106-C07-gestion-de-humedad/CLASE.md):**
- El punto de rocío a 22 °C y 50 % es 11,09 °C; la relación de humedad es 8,20 g/kg, a menos del 3 % del valor de tablas de manual (~8,3 g/kg).
- De 45 % a 75 % la relación de humedad sube 5,0 g/kg (0,73 kg de vapor) y con 6 kg/día de vapor (0,25 kg/h) pasan 2,9 h.
- 🎯 **Por qué importa:** Sin convección y con 4 personas, el vapor se acumula, sube la humedad relativa y se condensa en superficies frías. La decisión central: ¿cuánto vapor hay que retirar y con qué superficie fría, sin condensar sobre las paredes?

📘 **Dónde se aprende** (1 clase): [B106-C07 · Gestión de humedad](../programa/clases/B106/B106-C07-gestion-de-humedad/CLASE.md).

### Relación de Laplace

- La relación de Laplace entre los tres galileanos internos es `n₁ − 3n₂ + 2n₃ ≈ 0`.
- La relación de Laplace `n₁ − 3n₂ + 2n₃ = 0` liga tres satélites.

💡 **Cómo se explica en la clase [B72-C11](../programa/clases/B72/B72-C11-resonancias-orbitales-perturbaciones-y-evolucion-de-orbitas/CLASE.md):**
- La relación de Laplace da `−2,9 × 10⁻⁵ °/día`.
- Comprobar la relación de Laplace `n₁ − 3n₂ + 2n₃ ≈ 0`.
- 🎯 **Por qué importa:** Una resonancia mantiene a los satélites de Júpiter en equilibrio dinámico y obliga a gestionar un satélite geoestacionario, que se desplaza hacia dos puntos de equilibrio por el campo no esférico.

📘 **Dónde se aprende** (2 clases): [B72-C11 · Resonancias orbitales — Perturbaciones y evolución de órbitas](../programa/clases/B72/B72-C11-resonancias-orbitales-perturbaciones-y-evolucion-de-orbitas/CLASE.md); [B73-C10 · Resonancias de movimiento medio](../programa/clases/B73/B73-C10-resonancias-de-movimiento-medio/CLASE.md).

### Relación de presiones de trabajo máximo

- La relación de presiones de trabajo máximo es `r = τ^(γ/(2(γ−1)))`.

💡 **Cómo se explica en la clase [B79-C15](../programa/clases/B79/B79-C15-ciclos-termodinamicos-de-propulsion/CLASE.md):**
- Calcular la relación de presiones de trabajo máximo.
- Relacion de presiones de trabajo maximo (ideal): numerica = 15.91 ; analitica = 15.914 ; w_max = 419.99 kJ/kg ; eta en ese punto = 0.5464
- 🎯 **Por qué importa:** B85-C11 trata ciclos térmicos de ensayo, no termodinámicos. Para entender el rendimiento de una turbina de gas hay que ver el ciclo que lo origina.

📘 **Dónde se aprende** (1 clase): [B79-C15 · Ciclos termodinámicos de propulsión](../programa/clases/B79/B79-C15-ciclos-termodinamicos-de-propulsion/CLASE.md).

### Relación de Ryshkewitch

- La relación de Ryshkewitch es `σ = σ₀ exp(−bP)`.

🎯 **Por qué importa (clase B84-C37):** La resistencia de un compuesto cae exponencialmente con la porosidad: pasar de 10 a 25 % de huecos divide la resistencia por 2,4. La decisión central: ¿qué porosidad máxima permite cumplir una resistencia mínima y cuánto ligante hay que transportar?

📘 **Dónde se aprende** (1 clase): [B84-C37 · Compuestos y aglomerantes a base de regolito](../programa/clases/B84/B84-C37-compuestos-y-aglomerantes-a-base-de-regolito/CLASE.md).

### Relación de superposición

- Una relación de superposición `X → Y` dice que `X` es más antigua que `Y`.

💡 **Cómo se explica en la clase [B53-C09](../programa/clases/B53/B53-C09-estratigrafia-planetaria/CLASE.md):**
- Representar las relaciones de superposición como un grafo.
- 🎯 **Por qué importa:** Un mapa geológico es una hipótesis sobre el tiempo. La decisión central: ¿qué parte del orden temporal está fijada por contacto y qué parte solo sugerida por conteos con incertidumbre?

📘 **Dónde se aprende** (1 clase): [B53-C09 · Estratigrafía planetaria](../programa/clases/B53/B53-C09-estratigrafia-planetaria/CLASE.md).

### Relación de Tully–Fisher bariónica

- La relación de Tully–Fisher bariónica `v⁴ ∝ M`.

🎯 **Por qué importa (clase B36-C11):** Una alternativa debe confrontarse con todas las pruebas. La decisión central: ¿qué observación separa la materia oscura de la gravedad modificada?

📘 **Dónde se aprende** (1 clase): [B36-C11 · Gravedad modificada (MOND y relativistas) frente a materia oscura](../programa/clases/B36/B36-C11-gravedad-modificada-mond-y-relativistas-frente-a-materia-oscura/CLASE.md).

### Relación de unidades

- Una relación de unidades compara el programa con las mismas magnitudes en otras unidades.

💡 **Cómo se explica en la clase [B23-C06](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md):**
- Unidades (radio de la Tierra fijo en km aunque el programa trabaje en metros): lo detecta la relación de unidades (`2,8 × 10² km`).
- Signo de J2 invertido y factor mal en `a_z` (`1 − 5z²/r²` en vez de `3 − 5z²/r²`): sobreviven a todas las relaciones, porque siguen siendo axisimétricos, simétricos respecto del ecuador, reversibles y coherentes en unidades.
- ⚠️ **Error frecuente:** No incluir relaciones de unidades. Se corrige con la sección 13.
- 🎯 **Por qué importa:** El movimiento de un satélite con achatamiento terrestre (J2) no tiene solución cerrada, y tu código no tiene un valor correcto con el que compararse.

📘 **Dónde se aprende** (1 clase): [B23-C06 · Pruebas metamórficas](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md).

### Relación de Van Vleck

- La relación de Van Vleck vincula la correlación de 1 bit y la analógica: `ρ = sen(π r₁/2)`.

🎯 **Por qué importa (clase B46-C09):** Muchos correladores usan pocos bits para ahorrar recursos, y eso cambia la correlación medida. La decisión central: ¿cuántos bits hacen falta y cómo se corrige la pérdida de sensibilidad?

📘 **Dónde se aprende** (1 clase): [B46-C09 · Conversión analógica digital](../programa/clases/B46/B46-C09-conversion-analogica-digital/CLASE.md).

### Relación de volúmenes

- La relación de volúmenes es `v₁/v₂`.

💡 **Cómo se explica en la clase [B79-C12](../programa/clases/B79/B79-C12-procesos-adiabaticos-e-isentropicos/CLASE.md):**
- Ejercicio 1 · con los pasos indicados. Calcula `T₂` isentrópica con relación de volúmenes 5.
- 🎯 **Por qué importa:** Las relaciones isentrópicas son el núcleo del análisis de toberas, compresores y turbinas; el tronco no las trata. Aquí se obtienen desde primeros principios y se ve cuándo valen.

📘 **Dónde se aprende** (1 clase): [B79-C12 · Procesos adiabáticos e isentrópicos](../programa/clases/B79/B79-C12-procesos-adiabaticos-e-isentropicos/CLASE.md).

### Relación Eb/N₀

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C18):** Los datos que no caben en un paso se pierden o se acumulan. La decisión central: ¿cuántos bits por paso admite el enlace con margen suficiente?

📘 **Dónde se aprende** (1 clase): [B47-C18 · Downlink de instrumentos científicos](../programa/clases/B47/B47-C18-downlink-de-instrumentos-cientificos/CLASE.md).

### Relación empírica

- Una relación empírica ajusta datos.

💡 **Cómo se explica en la clase [B33-C10](../programa/clases/B33/B33-C10-modelos-de-viento-solar-para-pronostico-parker-y-wsa/CLASE.md):**
- La relación empírica es una receta que funciona en la práctica;
- 🎯 **Por qué importa:** Un pronóstico necesita una condición de frontera coronal. La decisión central: ¿cómo cambia la velocidad con la expansión y la distancia al borde?

📘 **Dónde se aprende** (1 clase): [B33-C10 · Modelos de viento solar para pronóstico (Parker y WSA)](../programa/clases/B33/B33-C10-modelos-de-viento-solar-para-pronostico-parker-y-wsa/CLASE.md).

### Relación empuje–peso

- La relación empuje–peso es `T/W = F/(m g₀)`.
- La relación empuje–peso `T/W` compara el empuje con el peso inicial.

💡 **Cómo se explica en la clase [B77-C01](../programa/clases/B77/B77-C01-sistemas-de-lanzamiento/CLASE.md):**
- Obtener el empuje de despegue a partir de la relación empuje–peso.
- 🎯 **Por qué importa:** Un requisito de velocidad no dice cuánto pesa el vehículo. La decisión central: ¿cómo se reparte la velocidad entre dos etapas para que la masa de despegue sea mínima, y qué parte de esa masa es carga útil?

📘 **Dónde se aprende** (2 clases): [B77-C01 · Sistemas de lanzamiento](../programa/clases/B77/B77-C01-sistemas-de-lanzamiento/CLASE.md); [B77-C06 · Relación masa-impulso](../programa/clases/B77/B77-C06-relacion-masa-impulso/CLASE.md).

### Relación energía–momento

- La relación energía–momento `E² = (pc)² + (mc²)²` es un invariante.

💡 **Cómo se explica en la clase [B26-C05](../programa/clases/B26/B26-C05-equivalencia-entre-masa-y-energia/CLASE.md):**
- Ejercicio 12 · integrador. Elabora tu *balance de energía relativista*: tabla de energía, momento y energía cinética de un protón a cuatro velocidades, la comprobación de la relación energía–momento, el balance de GW150914 y una reflexión sobre por qué `v = c` es inalcanzable.
- 🎯 **Por qué importa:** El Sol, un acelerador de partículas y la fusión de dos agujeros negros son balances de masa y energía. Para calcularlos hay que saber cuánta energía tiene una partícula en reposo y en movimiento, y por qué no puede acelerarse hasta `c`.

📘 **Dónde se aprende** (1 clase): [B26-C05 · Equivalencia entre masa y energía](../programa/clases/B26/B26-C05-equivalencia-entre-masa-y-energia/CLASE.md).

### Relación focal

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C10](../programa/clases/B41/B41-C10-apertura-y-relacion-focal/CLASE.md):**
- La aproximación `1/(4N²)` falla `20 %` en f/1 y es excelente desde f/10: para relaciones focales cortas hay que usar `sen²θ`.
- Como un embudo: la apertura es la boca y la relación focal el ángulo; una boca grande capta más lluvia (fuente puntual), un cono más abierto concentra más sobre cada gota (objeto extenso).
- 🎯 **Por qué importa:** La relación focal decide si un telescopio es «rápido» o «lento». La decisión central: ¿qué importa más, el diámetro o la relación focal?

📘 **Dónde se aprende** (1 clase): [B41-C10 · Apertura y relación focal](../programa/clases/B41/B41-C10-apertura-y-relacion-focal/CLASE.md).

### Relación G/T

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C18):** Los datos que no caben en un paso se pierden o se acumulan. La decisión central: ¿cuántos bits por paso admite el enlace con margen suficiente?

📘 **Dónde se aprende** (1 clase): [B47-C18 · Downlink de instrumentos científicos](../programa/clases/B47/B47-C18-downlink-de-instrumentos-cientificos/CLASE.md).

### Relación J/S

- La relación J/S compara interferencia y señal.

💡 **Cómo se explica en la clase [B119-C15](../programa/clases/B119/B119-C15-interferencias-y-resiliencia-de-comunicaciones/CLASE.md):**
- *Descripción textual:* la relación J/S se compara con la ganancia de procesamiento y el requisito de `E_b/N_0` para dar el margen.
- 🎯 **Por qué importa:** C09 calcula interferencia entre sistemas lícitos; esta clase extiende el cálculo a un escenario de degradación deliberada para razonar sobre resiliencia. La respuesta jurídica se aborda en C17 y C27.

📘 **Dónde se aprende** (1 clase): [B119-C15 · Interferencias y resiliencia de comunicaciones](../programa/clases/B119/B119-C15-interferencias-y-resiliencia-de-comunicaciones/CLASE.md).

### Relación lineal

- Una relación lineal tiene pendiente constante.

💡 **Cómo se explica en la clase [B03-C16](../programa/clases/B03/B03-C16-pendiente-e-interpretacion-de-graficos/CLASE.md):**
- Ambas fallan si la relación no es lineal en la escala elegida (como `T` frente a `a` lineal) o si hay muy pocos puntos.
- Reconocer una relación lineal y escribir su ecuación `y = mx + b`.
- 🎯 **Por qué importa:** Si sitúas en un gráfico logarítmico el período frente al semieje de los planetas, los puntos forman una recta. Su pendiente es 1,5: ese número es el exponente de la tercera ley de Kepler.

📘 **Dónde se aprende** (1 clase): [B03-C16 · Pendiente e interpretación de gráficos](../programa/clases/B03/B03-C16-pendiente-e-interpretacion-de-graficos/CLASE.md).

### Relación masa–luminosidad

- La relación masa–luminosidad liga `L` y `M`; por tramos, `L ∝ M^α`.

💡 **Cómo se explica en la clase [B24-C15](../programa/clases/B24/B24-C15-estrellas-de-baja-masa/CLASE.md):**
- Con una relación masa–luminosidad ilustrativa, una estrella de `0,5 M☉` tiene `L = 0,0625 L☉` y una vida de `59 Gyr`, y una de `0,1 M☉` supera `6000 Gyr`: más tiempo que cualquier edad cósmica razonable.
- Eker y colaboradores determinaron una relación masa–luminosidad empírica con `509` estrellas de la secuencia principal en binarias eclipsantes, entre `0,179` y `31 M☉`, ajustada por seis tramos de ley de potencias (S3, resumen); aquí no se usan sus coeficientes.
- 🎯 **Por qué importa:** La masa decide casi todo en la vida de una estrella: cuánto brilla, cuánto dura y cómo termina. Entender por qué una estrella de la mitad de la masa del Sol vive varias veces más tiempo, y por qué las más pequeñas casi no han evolucionado, explica la composición de las poblaciones estelares y la edad de los cúmulos.

📘 **Dónde se aprende** (1 clase): [B24-C15 · Estrellas de baja masa](../programa/clases/B24/B24-C15-estrellas-de-baja-masa/CLASE.md).

### Relación masa–luz

- La relación masa–luz `M/L` mide cuánta masa hay por unidad de luz.
- La relación masa–luz `Υ` convierte luz en masa estelar;

💡 **Cómo se explica en la clase [B25-C08](../programa/clases/B25/B25-C08-curvas-de-rotacion-de-galaxias/CLASE.md):**
- La relación masa–luz del disco cambia su peso (S3 adopta `0,5` como valor de referencia y analiza `0,2` y `0,7`).
- Prueba que, con gravedad newtoniana y una relación masa–luz razonable, falta masa; el resultado depende de `Υ` (S3 usa `0,2`–`0,7`) y de esas hipótesis.
- 🎯 **Por qué importa:** Si la masa estuviera donde brilla, la velocidad de rotación debería caer en las afueras de una galaxia, como la de los planetas lejanos del Sol. Que una curva de rotación se mantenga plana indica más masa de la que se ve.

📘 **Dónde se aprende** (2 clases): [B25-C08 · Curvas de rotación de galaxias](../programa/clases/B25/B25-C08-curvas-de-rotacion-de-galaxias/CLASE.md); [B25-C10 · Galaxias irregulares y enanas](../programa/clases/B25/B25-C10-galaxias-irregulares-y-enanas/CLASE.md).

### Relación masa–radio

- La relación masa–radio `R(M)` decrece.

💡 **Cómo se explica en la clase [B27-C02](../programa/clases/B27/B27-C02-enanas-blancas-y-limite-de-chandrasekhar/CLASE.md):**
- Obtener la relación masa–radio y su pendiente no relativista.
- 🎯 **Por qué importa:** Las enanas blancas son el destino de la mayoría de las estrellas, sirven de relojes cosmológicos y, al acercarse a su masa límite, pueden explotar. Una relación masa–radio correcta separa masas y radios que la fotometría sola confunde.

📘 **Dónde se aprende** (1 clase): [B27-C02 · Enanas blancas y límite de Chandrasekhar](../programa/clases/B27/B27-C02-enanas-blancas-y-limite-de-chandrasekhar/CLASE.md).

### Relación metamórfica

- Una relación metamórfica es una regla del tipo «si transformo la entrada así, la salida debe transformarse asá».

💡 **Cómo se explica en la clase [B23-C06](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md):**
- Las relaciones metamórficas no necesitan oráculo y se derivan de simetrías y unidades, pero son ciegas a defectos coherentes.
- Definir una relación metamórfica como un par «transformación de la entrada / efecto esperado en la salida».
- 🎯 **Por qué importa:** El movimiento de un satélite con achatamiento terrestre (J2) no tiene solución cerrada, y tu código no tiene un valor correcto con el que compararse.

📘 **Dónde se aprende** (1 clase): [B23-C06 · Pruebas metamórficas](../programa/clases/B23/B23-C06-pruebas-metamorficas/CLASE.md).

### Relación O/F

- La relación `O/F` es la masa de oxidante entre la de combustible.

💡 **Cómo se explica en la clase [B78-C05](../programa/clases/B78/B78-C05-propulsion-bipropelente-conceptual/CLASE.md):**
- Con el modelo ilustrativo H₂/O₂, la relación estequiométrica en masa es `7,936`.
- Calcular la relación estequiométrica `O/F` de H₂/O₂.
- 🎯 **Por qué importa:** Un motor puede quemar mezclas con exceso de combustible o de oxidante. La decisión central: ¿qué `O/F` maximiza el escape en un modelo sin disociación y por qué los motores reales operan en otro punto?

📘 **Dónde se aprende** (1 clase): [B78-C05 · Propulsión bipropelente conceptual](../programa/clases/B78/B78-C05-propulsion-bipropelente-conceptual/CLASE.md).

### Relación período–densidad

- La relación período–densidad `Π √(ρ̄/ρ̄_☉) = Q` es constante.

💡 **Cómo se explica en la clase [B37-C07](../programa/clases/B37/B37-C07-oscilaciones-radiales-y-relacion-periodo-densidad-media/CLASE.md):**
- python programa/clases/B37/B37-C07-oscilaciones-radiales-y-relacion-periodo-densidad-media/radiales.py
- 🎯 **Por qué importa:** El período fundamental fija la densidad media. La decisión central: ¿cuánto vale el período de un modo radial y cómo escala con la densidad?

📘 **Dónde se aprende** (1 clase): [B37-C07 · Oscilaciones radiales y relación período-densidad media](../programa/clases/B37/B37-C07-oscilaciones-radiales-y-relacion-periodo-densidad-media/CLASE.md).

### Relación periodo–luminosidad

- La relación periodo–luminosidad (de Leavitt) liga `log P` con la magnitud absoluta `M`.

💡 **Cómo se explica en la clase [B24-C13](../programa/clases/B24/B24-C13-estrellas-variables/CLASE.md):**
- El ejemplo conductor es una muestra sintética de `60` cefeidas con una relación periodo–luminosidad inyectada (`M = −4,0 − 2,5 (log P − 1)`, dispersión `0,15 mag`, `μ = 18,50`), para que veas cómo se recupera.
- Definir estrella variable pulsante, periodo y relación periodo–luminosidad.
- 🎯 **Por qué importa:** Las cefeidas y otras estrellas pulsantes cumplen que cuanto más largo es el periodo, mayor es la luminosidad. Medir un periodo equivale entonces a conocer la luminosidad intrínseca y, por comparación con el brillo aparente, la distancia.

📘 **Dónde se aprende** (1 clase): [B24-C13 · Estrellas variables](../programa/clases/B24/B24-C13-estrellas-variables/CLASE.md).

### Relación señal/ruido

- La relación señal–ruido (SNR) de una medida es su valor dividido por su incertidumbre.
- La relación señal/ruido (SNR) es señal dividida entre la desviación del ruido.
- La relación señal/ruido (`SNR`) es la señal media dividida por la desviación estándar del ruido.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C12](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md):**
- Calcular la relación señal–ruido de una fuente de flujo conocido.
- 🎯 **Por qué importa:** Un catálogo de fuentes es el producto básico de una imagen astronómica, y de él salen cuentas, colores y candidatos a objetos nuevos. Si el umbral es bajo, el catálogo se llena de ruido; si es alto, se pierden las fuentes débiles.

📘 **Dónde se aprende** (8 clases): [B15-C12 · Detección de fuentes astronómicas](../programa/clases/B15/B15-C12-deteccion-de-fuentes-astronomicas/CLASE.md); [B29-C20 · Proyecto de detección exoplanetaria](../programa/clases/B29/B29-C20-proyecto-de-deteccion-exoplanetaria/CLASE.md); [B47-C03 · Telescopios ultravioleta](../programa/clases/B47/B47-C03-telescopios-ultravioleta/CLASE.md); [B48-C18 · Protección del cielo oscuro](../programa/clases/B48/B48-C18-proteccion-del-cielo-oscuro/CLASE.md); [B56-C14 · Biofirmas espectrales](../programa/clases/B56/B56-C14-biofirmas-espectrales/CLASE.md); [B63-C01 · Instrumentación de sondas y rovers planetarios](../programa/clases/B63/B63-C01-instrumentacion-de-sondas-y-rovers-planetarios/CLASE.md) y 2 más.

### Relación señal-ruido óptima

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B28-C14](../programa/clases/B28/B28-C14-ruidos-instrumentales/CLASE.md):**
- *Descripción textual:* la densidad espectral genera el ruido; el periodograma la recupera; la relación señal-ruido óptima de una señal se contrasta con la media de la salida del filtro acoplado sobre muchas realizaciones.
- relacion senal-ruido optima (teorica) para amplitud 10.0: rho = 7.079
- 🎯 **Por qué importa:** Entender la forma del ruido explica por qué un detector es sensible solo en una banda y por qué una señal débil puede perderse en baja frecuencia aunque sea fuerte en alta. La decisión central: ¿cómo se estima la densidad espectral del ruido y qué relación señal-ruido da el filtro óptimo?

📘 **Dónde se aprende** (1 clase): [B28-C14 · Ruidos instrumentales](../programa/clases/B28/B28-C14-ruidos-instrumentales/CLASE.md).

### Relación señal-ruido (SNR)

- La relación señal-ruido (SNR) es la señal dividida por su incertidumbre típica.

🎯 **Por qué importa (clase B13-C15):** Una cámara espacial debe decidir cuánto tiempo exponer para detectar una fuente débil con una relación señal-ruido (SNR) dada. Exponer poco no la detecta; exponer demasiado satura los píxeles brillantes o desperdicia tiempo de misión.

📘 **Dónde se aprende** (1 clase): [B13-C15 · Sensibilidad de detectores](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md).

### Relación T–τ

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B32-C05](../programa/clases/B32/B32-C05-relacion-t-y-estructura-termica-de-la-fotosfera/CLASE.md):**
- Que la relación cumple el equilibrio radiativo del modelo.
- El script [ttau.py](ttau.py) evalúa la relación y comprueba el flujo (comprueba `10⁻¹²` y `10⁻²`).
- 🎯 **Por qué importa:** La relación T–τ da el gradiente que forma las líneas. La decisión central: ¿cuánto vale la temperatura a cada profundidad óptica?

📘 **Dónde se aprende** (1 clase): [B32-C05 · Relación T-τ y estructura térmica de la fotosfera](../programa/clases/B32/B32-C05-relacion-t-y-estructura-termica-de-la-fotosfera/CLASE.md).

### Relaciones de Rankine–Hugoniot

- Las relaciones de Rankine–Hugoniot unen los estados antes y después del choque.
- Las relaciones de Rankine–Hugoniot unen los estados a ambos lados por conservación de masa, momento y energía.

🎯 **Por qué importa (clase B58-C16):** Las consecuencias se miden por zonas: sismo, onda de choque, calor. Las escalas con la energía son lo que permite comparar casos.

📘 **Dónde se aprende** (2 clases): [B58-C16 · Consecuencias geofísicas de impactos](../programa/clases/B58/B58-C16-consecuencias-geofisicas-de-impactos/CLASE.md); [B79-C07 · Ondas de choque normales y oblicuas](../programa/clases/B79/B79-C07-ondas-de-choque-normales-y-oblicuas/CLASE.md).

### Relaciones isentrópicas

- Las relaciones isentrópicas son `T₀/T = 1 + (γ−1)M²/2`, `p₀/p = (T₀/T)^(γ/(γ−1))` y `ρ₀/ρ = (T₀/T)^(1/(γ−1))`.

💡 **Cómo se explica en la clase [B79-C05](../programa/clases/B79/B79-C05-dinamica-de-fluidos-compresibles/CLASE.md):**
- M["Mach"] --> R["relaciones isentrópicas"]
- Aplicar las relaciones isentrópicas `T/T₀`, `p/p₀`, `ρ/ρ₀`.
- 🎯 **Por qué importa:** B77-C03 trata fuerzas aerodinámicas sin flujo compresible; en propulsión la densidad varía mucho y sin este modelo no se pueden calcular toberas ni tomas de aire. La decisión central: ¿a partir de qué Mach no puedo tratar el gas como incompresible, y qué relación uso entonces?

📘 **Dónde se aprende** (1 clase): [B79-C05 · Dinámica de fluidos compresibles](../programa/clases/B79/B79-C05-dinamica-de-fluidos-compresibles/CLASE.md).

### Relajación

- Jacobi y Gauss–Seidel son métodos de relajación.

💡 **Cómo se explica en la clase [B21-C03](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md):**
- Después de unas relajaciones queda un error suave.
- La relajación hace lo que haría una persona que pasa la mano sobre la tela: cada punto se coloca en el promedio de sus vecinos, más una corrección por el peso.
- ⚠️ **Error frecuente:** Suponer que más relajaciones en la malla fina equivalen a multigrid. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** El potencial gravitatorio de una nube de gas, el potencial electrostático alrededor de una nave que se carga en el plasma y la presión en un fluido incompresible obedecen la misma ecuación: la de Poisson. Los códigos de simulación astrofísica la resuelven en cada paso de tiempo;

📘 **Dónde se aprende** (1 clase): [B21-C03 · Ecuación de Poisson: relajación y multigrid](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md).

### Relativa

- La incertidumbre estándar es la dispersión asociada a un valor medido; la relativa es esa incertidumbre dividida por el valor (S5).
- Una ruta absoluta está completa desde la raíz (`C:\...` o `/home/...`); una relativa se interpreta desde el directorio de trabajo.

💡 **Cómo se explica en la clase [B03-C12](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md):**
- CODATA 2022 da `6,67430 × 10⁻¹¹` con incertidumbre estándar `0,00015 × 10⁻¹¹` (relativa `2,2 × 10⁻⁵`, S2).
- Para `M = (GM)/G`, con `GM` exacto, la incertidumbre relativa de `M` es la de `G`: `2,2 × 10⁻⁵`.
- 🎯 **Por qué importa:** La masa del Sol se conoce con unas cinco cifras. Sin embargo, el producto `GM` del Sol se conoce con diez, y la constante `G` por sí sola con apenas cinco.

📘 **Dónde se aprende** (2 clases): [B03-C12 · Variables y constantes científicas](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md); [B07-C15 · Terminal y rutas de archivos](../programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/CLASE.md).

### Relatividad general

- La relatividad general describe la gravedad como curvatura del espacio-tiempo.

💡 **Cómo se explica en la clase [B26-C09](../programa/clases/B26/B26-C09-relatividad-general-introductoria/CLASE.md):**
- Para un rayo que pasa rasante al limbo solar, `b = R☉ = 6,957 × 10⁸ m` y `GM☉ = 1,327 124 4 × 10²⁰ m³/s²` (S2), con `c` exacta (S1), la relatividad general predice `α = 4GM/(c²b) = 8,490 × 10⁻⁶ rad = 1,7512″`, el doble de lo que sale si solo se considera la parte temporal de la métrica, `0,8756″`.
- Enunciar la idea central de la relatividad general y su límite newtoniano.
- 🎯 **Por qué importa:** La luz de una estrella lejana que pasa cerca del Sol, o de una galaxia, se desvía: es la base de las lentes gravitacionales que miden masas de cúmulos (C18) y de las correcciones al seguimiento de naves en el espacio profundo.

📘 **Dónde se aprende** (1 clase): [B26-C09 · Relatividad general introductoria](../programa/clases/B26/B26-C09-relatividad-general-introductoria/CLASE.md).

### Relativista

- El Doppler clásico `z = v/c`; el relativista `1 + z = √((1+β)/(1−β))`.

💡 **Cómo se explica en la clase [B45-C12](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md):**
- Para `z = 0,1` la velocidad relativista es `β = 0,095023` (el clásico daría 0,1).
- El efecto relativista es del 5 % a 30 000 km/s y del 0,005 % a 3000 km/s.
- ⚠️ **Error frecuente:** Usar la fórmula clásica a velocidades relativistas. Se corrige con 8.1.
- 🎯 **Por qué importa:** Las velocidades radiales descubren planetas, binarias y la expansión del universo. La decisión central: ¿cómo se pasa de un corrimiento a una velocidad y con qué precisión?

📘 **Dónde se aprende** (1 clase): [B45-C12 · Efecto Doppler en espectros](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md).

### Relevo

- El relevo es el cambio de reanimador.
- El relevo reenvía datos de un usuario cercano.

💡 **Cómo se explica en la clase [B89-C20](../programa/clases/B89/B89-C20-diseno-de-red-de-comunicaciones-de-mision/CLASE.md):**
- RELE["relevo rover -> orbitador -> Tierra"] --> CUELLO["cuello de botella"]
- *Descripción textual:* el requisito se compara con el volumen que sale de la tasa máxima y las horas de contacto de cada fase; en el relevo, el eslabón más pequeño fija lo que llega.
- ⚠️ **Error frecuente:** Olvidar el cuello de botella del relevo. Se corrige con 8.3.
- 🎯 **Por qué importa:** Una red de misión se diseña contra requisitos verificables: cuántos datos por día, con qué margen, en cada fase. Un diseño sin esa trazabilidad no se puede verificar ni defender.

📘 **Dónde se aprende** (2 clases): [B89-C20 · Diseño de red de comunicaciones de misión](../programa/clases/B89/B89-C20-diseno-de-red-de-comunicaciones-de-mision/CLASE.md); [B117-C01 · Primeros auxilios y procedimientos básicos en entorno espacial](../programa/clases/B117/B117-C01-primeros-auxilios-y-procedimientos-basicos-en-entorno-espacial/CLASE.md).

### Relevo confirmado

- Un relevo confirmado retiene la autoridad en A hasta que B confirma.

💡 **Cómo se explica en la clase [B98-C08](../programa/clases/B98/B98-C08-protocolos-de-relevo-de-control-entre-operadores/CLASE.md):**
- El confirmado elimina los huecos pero produce `1507` relevos con solapamiento y `3512` órdenes en conflicto.
- 🎯 **Por qué importa:** Los relevos fallan en los bordes: un «es tuyo» que no llega deja el vehículo sin dueño, y un «lo sigo yo» sin confirmar deja a dos operadores dando órdenes. La decisión central: ¿cómo se garantiza que siempre hay exactamente un operador con autoridad, o que las órdenes de uno antiguo no se acepten?

📘 **Dónde se aprende** (1 clase): [B98-C08 · Protocolos de relevo de control entre operadores](../programa/clases/B98/B98-C08-protocolos-de-relevo-de-control-entre-operadores/CLASE.md).

### Relevo estructurado

- Un relevo estructurado incluye el estado del vehículo, los comandos pendientes y las anomalías abiertas (no se modela el contenido del briefing).

🎯 **Por qué importa (clase B98-C08):** Los relevos fallan en los bordes: un «es tuyo» que no llega deja el vehículo sin dueño, y un «lo sigo yo» sin confirmar deja a dos operadores dando órdenes. La decisión central: ¿cómo se garantiza que siempre hay exactamente un operador con autoridad, o que las órdenes de uno antiguo no se acepten?

📘 **Dónde se aprende** (1 clase): [B98-C08 · Protocolos de relevo de control entre operadores](../programa/clases/B98/B98-C08-protocolos-de-relevo-de-control-entre-operadores/CLASE.md).

### Relieve

- El relieve codifica un valor como altura que se toca.
- El relieve o modelo táctil representa un valor como altura.

💡 **Cómo se explica en la clase [B128-C03](../programa/clases/B128/B128-C03-alternativas-a-la-observacion-visual/CLASE.md):**
- El relieve usa `nivel = round(4k)`: niveles 0, 1, 2, 3, 4, 3, 2, 1 para las ocho fases.
- El texto pierde la forma; la tabla pierde la intuición espacial; el relieve pierde la dirección (creciente y menguante coinciden) y la resolución fina (0,1464 y 0,0 quedan a un nivel de diferencia).
- 🎯 **Por qué importa:** «Alternativa» no significa «versión reducida». Si el relieve pierde resolución o el texto omite el lado iluminado, la persona recibe menos información que quien mira.

📘 **Dónde se aprende** (2 clases): [B128-C03 · Alternativas a la observación visual](../programa/clases/B128/B128-C03-alternativas-a-la-observacion-visual/CLASE.md); [B128-C07 · Modelos táctiles y sonificación](../programa/clases/B128/B128-C07-modelos-tactiles-y-sonificacion/CLASE.md).

### Relieve ocular

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C09](../programa/clases/B41/B41-C09-pupilas-y-diafragmas-opticos/CLASE.md):**
- La imagen del objetivo por el ocular está a `s' = 25,6250 mm` (relieve ocular) y mide `2,5000 mm`, igual a `D/M`.
- Ejercicio 2 · con una pista. Relieve ocular con `f_e = 25`.
- ⚠️ **Error frecuente:** Olvidar el relieve ocular. Condiciona el uso con gafas.
- 🎯 **Por qué importa:** La pupila limita la luz y el viñeteo oscurece los bordes. La decisión central: ¿qué diafragma manda y cuánta luz se pierde fuera del eje?

📘 **Dónde se aprende** (1 clase): [B41-C09 · Pupilas y diafragmas ópticos](../programa/clases/B41/B41-C09-pupilas-y-diafragmas-opticos/CLASE.md).

### Relleno

- El relleno añade de la mayor a la menor lo que cabe.

💡 **Cómo se explica en la clase [B86-C23](../programa/clases/B86/B86-C23-priorizacion-y-deslastre-de-cargas-electricas/CLASE.md):**
- Con valor lexicográfico (cada prioridad vale más que todas las menores juntas) el relleno coincide con el óptimo en todas las potencias.
- Con valor aditivo existe al menos una potencia en que el relleno queda por debajo del óptimo.
- ⚠️ **Error frecuente:** Creer que el relleno siempre es óptimo. Se corrige con 8.2.
- 🎯 **Por qué importa:** La clase de distribución trató cómo repartir potencia, pero no qué hacer cuando falta. Una política de prioridades bien definida mantiene lo crítico vivo y recupera ciencia cuando vuelve la potencia, sin oscilar entre estados.

📘 **Dónde se aprende** (1 clase): [B86-C23 · Priorización y deslastre de cargas eléctricas](../programa/clases/B86/B86-C23-priorizacion-y-deslastre-de-cargas-electricas/CLASE.md).

### Relleno con ceros

- El relleno con ceros (*zero padding*) es añadir ceros al final de la serie para alargarla.

💡 **Cómo se explica en la clase [B15-C05](../programa/clases/B15/B15-C05-transformada-rapida-de-fourier/CLASE.md):**
- Explicar qué aporta y qué no aporta el relleno con ceros.
- El script [fft_rapida.py](fft_rapida.py) implementa la FFT por pares e impares, la compara con la DFT directa y con `numpy.fft.fft`, cuenta las mariposas y exige que coincidan con `(N/2) log₂ N`, comprueba el orden de `fftfreq` y muestra el efecto del relleno con ceros en el caso de 27 días.
- ⚠️ **Error frecuente:** Creer que el relleno con ceros mejora la resolución. Se corrige con los ejercicios 8 y 10.
- 🎯 **Por qué importa:** Una curva de luz de 27 días con cadencia de 2 minutos tiene 19 440 muestras. La suma directa de la DFT necesita unos 378 millones de multiplicaciones complejas; una imagen de 1024 × 1024 necesitaría muchísimas más.

📘 **Dónde se aprende** (1 clase): [B15-C05 · Transformada rápida de Fourier](../programa/clases/B15/B15-C05-transformada-rapida-de-fourier/CLASE.md).

### Relleno de bits

- El relleno de bits inserta un bit complementario tras cinco iguales; hay como máximo `⌊(34 + 8n − 1)/4⌋` rellenos.

💡 **Cómo se explica en la clase [B88-C07](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md):**
- El relleno puede añadir hasta `⌊97/4⌋ = 24`: `135` bits, `135 µs` a 1 Mb/s y `0,474 Mb/s` útiles.
- Paso 2 · Relleno máximo. `⌊(34 + 64 − 1)/4⌋ = 24`: `135` bits.
- ⚠️ **Error frecuente:** Olvidar el relleno de bits en CAN. Usa el peor caso (8.2)
- 🎯 **Por qué importa:** El bus fija cuánta telemetría y cuántos comandos caben y con qué retardo. La decisión central: ¿cuál es el caudal útil y el peor tiempo de trama de cada bus para mi carga?

📘 **Dónde se aprende** (1 clase): [B88-C07 · Buses I2C SPI CAN y SpaceWire](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md).

### Relleno de ceros

- El relleno de ceros (*zero padding*).

💡 **Cómo se explica en la clase [B51-C11](../programa/clases/B51/B51-C11-busqueda-de-franjas-vlbi-ajuste-de-retardo-y-tasa/CLASE.md):**
- Hallar el pico de la FFT 2D con relleno de ceros.
- Ejercicio 9 · transferencia. Transferencia. ¿Por qué el relleno de ceros ayuda a ubicar el pico pero no mejora la resolución?
- ⚠️ **Error frecuente:** Confundir resolución con relleno de ceros. Ver el ejercicio 9.
- 🎯 **Por qué importa:** Declarar una detección sin umbral estadístico es un riesgo de falsos positivos. La decisión central: ¿qué pico es una señal y cuál es ruido, y con qué precisión se estiman retardo y tasa?

📘 **Dónde se aprende** (1 clase): [B51-C11 · Búsqueda de franjas VLBI: ajuste de retardo y tasa](../programa/clases/B51/B51-C11-busqueda-de-franjas-vlbi-ajuste-de-retardo-y-tasa/CLASE.md).

### Relocalización

- Compuerta: umbral `3σ` sobre la discrepancia. Relocalización: recuperar la pose tras perderla (F7).

💡 **Cómo se explica en la clase [B99-C04](../programa/clases/B99/B99-C04-cierre-de-bucles-y-consistencia-global/CLASE.md):**
- ORB-SLAM (F7) incluye en su resumen el cierre de bucles de línea base amplia y la relocalización con las mismas características que el seguimiento.
- 🎯 **Por qué importa:** Aceptar un cierre verdadero reduce el error; aceptar uno falso lo multiplica. La decisión central: ¿con qué umbral y con qué prueba geométrica acepto un cierre de bucle?

📘 **Dónde se aprende** (1 clase): [B99-C04 · Cierre de bucles y consistencia global](../programa/clases/B99/B99-C04-cierre-de-bucles-y-consistencia-global/CLASE.md).

### Remolcador eléctrico

- El remolcador eléctrico transporta con un Isp alto y un Δv mayor por la espiral.

💡 **Cómo se explica en la clase [B100-C06](../programa/clases/B100/B100-C06-logistica-cislunar-nodos-depositos-y-rutas-de-reabastecimiento/CLASE.md):**
- Límite: se ignora el tiempo de tránsito, que con un remolcador eléctrico es de meses.
- Con un aterrizador reutilizable de 500 kg secos desde un depósito en NRHO hacen falta `2043,6 kg` de propelente por viaje; si la carga y el propelente suben desde órbita baja con etapas químicas, la razón empeora a `7,779`; con un remolcador eléctrico ilustrativo baja a `4,729` con 10 viajes y supera a la ruta directa desde el viaje 2.
- 🎯 **Por qué importa:** Un depósito en órbita lunar parece una ventaja obvia, pero solo lo es si el propelente llega al depósito de una forma más barata que llevarlo directamente. La decisión central: ¿con qué transporte y con cuántos viajes del aterrizador reutilizable un depósito reduce la masa que hay que lanzar desde órbita baja?

📘 **Dónde se aprende** (1 clase): [B100-C06 · Logística cislunar: nodos, depósitos y rutas de reabastecimiento](../programa/clases/B100/B100-C06-logistica-cislunar-nodos-depositos-y-rutas-de-reabastecimiento/CLASE.md).

### Remote Agent

- El Remote Agent (consultado, solo el resumen) combina planificación con restricciones, ejecución multihilo y reconfiguración basada en modelos para controlar una nave a bordo.

🎯 **Por qué importa (clase B98-C07):** Una arquitectura sin presupuesto de tiempos puede parecer correcta hasta que una tarea lenta retrasa un reflejo. La decisión central: ¿cada capa cumple sus plazos aunque las demás consuman su peor caso, y qué pasa cuando el planificador tarda más de lo previsto?

📘 **Dónde se aprende** (1 clase): [B98-C07 · Arquitectura de autonomía a bordo (percepción-decisión-acción)](../programa/clases/B98/B98-C07-arquitectura-de-autonomia-a-bordo-percepcion-decision-accion/CLASE.md).

### Remoto

- Un remoto es un almacén compartido de objetos.

💡 **Cómo se explica en la clase [B14-C11](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md):**
- `dvc push` copia la caché a un remoto con la misma estructura y `dvc pull` baja lo que falta.
- DVC mueve los datos a una caché por hash y los sincroniza con un remoto.
- 🎯 **Por qué importa:** Un análisis usó «la tabla de catálogo de octubre». En noviembre alguien reemplazó el archivo por otro con el mismo nombre.

📘 **Dónde se aprende** (1 clase): [B14-C11 · Control de versiones de datos](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md).

### Removible

- Si falla, hay una discontinuidad: removible (el límite existe pero no coincide con `f(a)` o `f(a)` no existe), de salto (existen ambos límites laterales y son distintos) o infinita (la función crece sin cota).

💡 **Cómo se explica en la clase [B09-C02](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md):**
- Cada tipo de discontinuidad es una razón para levantarlo: un hueco (removible), un salto de nivel (salto) o una subida al infinito (infinita).
- D --> F["Removible, de salto o infinita"]
- 🎯 **Por qué importa:** Un vehículo espacial cambia de masa de dos maneras: gradualmente, al quemar propelente, y de golpe, al soltar una etapa vacía. Un modelo de trayectoria que ignore los saltos integra mal; uno que los trate como suaves, también.

📘 **Dónde se aprende** (1 clase): [B09-C02 · Continuidad y discontinuidad](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md).

### Remuestreo

- El remuestreo sustituye las partículas de peso despreciable por copias de las de peso alto (S1); el remuestreo sistemático usa un solo número aleatorio y puntos equiespaciados.
- El remuestreo estima la incertidumbre.
- El remuestreo reutiliza los residuos para reajustar.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C18](../programa/clases/B15/B15-C18-filtros-de-particulas-iniciales/CLASE.md):**
- El tamaño efectivo mínimo observado fue 111 de 2000 y se remuestreó 12,2 veces por trayectoria de 60 pasos.
- Las ideas generales —pesos de verosimilitud, remuestreo, degeneración, aptitud para modelos no lineales— son las descritas en S1.
- 🎯 **Por qué importa:** Un sensor mide la distancia oblicua a un objeto que pasa junto a él. Cuando el objeto está justo frente al sensor, un pequeño cambio de posición casi no cambia la distancia: la medida no distingue bien un lado del otro, y la incertidumbre de la posición deja de ser una campana.

📘 **Dónde se aprende** (5 clases): [B15-C18 · Filtros de partículas iniciales](../programa/clases/B15/B15-C18-filtros-de-particulas-iniciales/CLASE.md); [B32-C08 · Síntesis espectral e inversión de perfiles](../programa/clases/B32/B32-C08-sintesis-espectral-e-inversion-de-perfiles/CLASE.md); [B34-C09 · Integración multiinstrumento de datos heliofísicos](../programa/clases/B34/B34-C09-integracion-multiinstrumento-de-datos-heliofisicos/CLASE.md); [B88-C44 · Mantenimiento predictivo y pronóstico de salud de sistemas](../programa/clases/B88/B88-C44-mantenimiento-predictivo-y-pronostico-de-salud-de-sistemas/CLASE.md); [B113-C05 · Intervenciones de apoyo y contramedidas conductuales](../programa/clases/B113/B113-C05-intervenciones-de-apoyo-y-contramedidas-conductuales/CLASE.md).

### Remuestreo paramétrico

- El remuestreo paramétrico regenera datos con el modelo ajustado y el ruido conocido.

💡 **Cómo se explica en la clase [B107-C06](../programa/clases/B107/B107-C06-estimacion-y-modelado-de-la-recuperacion-posterior-al-vuelo/CLASE.md):**
- El remuestreo paramétrico supone que el modelo es correcto y que el ruido es conocido.
- P --> B["remuestreo parametrico x 1000"]
- 🎯 **Por qué importa:** Los fragmentos consultados indican pérdida de fuerza muscular tras misiones largas con riesgos operativos y médicos (English et al., 2015), cambios en tareas funcionales y sus factores fisiológicos (Mulavara et al., 2018) y alteraciones del control postural y locomotor (Macaulay et al., 2021).

📘 **Dónde se aprende** (1 clase): [B107-C06 · Estimación y modelado de la recuperación posterior al vuelo](../programa/clases/B107/B107-C06-estimacion-y-modelado-de-la-recuperacion-posterior-al-vuelo/CLASE.md).

### Remuestreo sistemático

- El remuestreo sustituye las partículas de peso despreciable por copias de las de peso alto (S1); el remuestreo sistemático usa un solo número aleatorio y puntos equiespaciados.

💡 **Cómo se explica en la clase [B15-C18](../programa/clases/B15/B15-C18-filtros-de-particulas-iniciales/CLASE.md):**
- Implementar el remuestreo sistemático y comprobar su propiedad.
- Ejercicio 5. Remuestreo sistemático con `N = 4`, pesos `[0,1; 0,4; 0,3; 0,2]` y `u = 0,3`.
- 🎯 **Por qué importa:** Un sensor mide la distancia oblicua a un objeto que pasa junto a él. Cuando el objeto está justo frente al sensor, un pequeño cambio de posición casi no cambia la distancia: la medida no distingue bien un lado del otro, y la incertidumbre de la posición deja de ser una campana.

📘 **Dónde se aprende** (1 clase): [B15-C18 · Filtros de partículas iniciales](../programa/clases/B15/B15-C18-filtros-de-particulas-iniciales/CLASE.md).

### Rendija

- La rendija de ancho `a`.
- La rendija limita la entrada.

💡 **Cómo se explica en la clase [B42-C04](../programa/clases/B42/B42-C04-difraccion-de-aperturas/CLASE.md):**
- Para dos rendijas, la máxima diferencia con `sinc²·cos²` sobre 22 puntos es `1,32 × 10⁻⁴` y las franjas se separan `1/d = 5000 m⁻¹` (`λ/d = 2,5 mrad`).
- Para una red de 5 rendijas el máximo secundario entre principales es `0,0613` (cota de la fórmula: `0,0611`) y hay `3 = N − 2` secundarios; la diferencia máxima con la fórmula es `1,32 × 10⁻⁴`.
- ⚠️ **Error frecuente:** Pensar que la red cambia la envolvente. La envolvente es la `sinc²` de una rendija.
- 🎯 **Por qué importa:** La pupila de un telescopio es una apertura: su forma fija la imagen de una estrella. La decisión central: ¿cómo cambia el patrón cuando cambia la forma o el número de aberturas?

📘 **Dónde se aprende** (2 clases): [B42-C04 · Difracción de aperturas](../programa/clases/B42/B42-C04-difraccion-de-aperturas/CLASE.md); [B45-C06 · Diseño de espectrógrafos](../programa/clases/B45/B45-C06-diseno-de-espectrografos/CLASE.md).

### Rendimiento

- El rendimiento `y` es la masa de metales producida y liberada por cada unidad de masa que queda en estrellas.
- El rendimiento es el número de fotones por unidad de longitud.
- El rendimiento es la fracción de sistemas que cumple.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B25-C17](../programa/clases/B25/B25-C17-metallicidad-y-evolucion-quimica/CLASE.md):**
- Paso 5 · Sentido. Con ese rendimiento ilustrativo, una caja cerrada que ha convertido el `70 %` de su gas en estrellas alcanza casi el valor solar; con salida de gas `λ = 1` sería la mitad.
- El ejemplo conductor es una galaxia sintética de caja cerrada con rendimiento efectivo `y = 0,010` (ilustrativo) y gas restante `μ = 0,3`.
- 🎯 **Por qué importa:** Cada generación de estrellas fabrica elementos pesados y los devuelve al gas; la proporción de metales de una galaxia cuenta cuánto se ha procesado su gas. En astronomía, «metales» son todos los elementos más pesados que el helio.

📘 **Dónde se aprende** (9 clases): [B25-C17 · Metalicidad y evolución química](../programa/clases/B25/B25-C17-metallicidad-y-evolucion-quimica/CLASE.md); [B31-C14 · Detectores de partículas](../programa/clases/B31/B31-C14-detectores-de-particulas/CLASE.md); [B43-C14 · Reductores y transmisiones](../programa/clases/B43/B43-C14-reductores-y-transmisiones/CLASE.md); [B50-C13 · Análisis Monte Carlo de tolerancias ópticas](../programa/clases/B50/B50-C13-analisis-monte-carlo-de-tolerancias-opticas/CLASE.md); [B64-C01 · Radiotolerancia biológica y reparación del ADN](../programa/clases/B64/B64-C01-radiotolerancia-biologica-y-reparacion-del-adn/CLASE.md); [B68-C02 · Fotodesorción de hielos interestelares](../programa/clases/B68/B68-C02-fotodesorcion-de-hielos-interestelares/CLASE.md) y 3 más.

### Rendimiento de agua

- El rendimiento de agua es la masa de agua extraíble por masa de roca.

💡 **Cómo se explica en la clase [B59-C05](../programa/clases/B59/B59-C05-minerales-marcianos/CLASE.md):**
- *Descripción textual:* el espectro y los miembros extremos dan las abundancias por NNLS; ponderadas por el rendimiento dan el agua; el remuestreo del ruido da su dispersión.
- Se recupera `0,447 / 0,293 / 0,161 / 0,100` (suma `1,001`) y un rendimiento de agua de `5,10 %` frente al `5,00 %` sembrado; el ruido produce una dispersión de `0,30` puntos porcentuales.
- 🎯 **Por qué importa:** Antes de excavar hay que saber qué se excava. La decisión central: ¿qué rendimiento de agua se espera de una mezcla y con qué dispersión por el ruido?

📘 **Dónde se aprende** (1 clase): [B59-C05 · Minerales marcianos](../programa/clases/B59/B59-C05-minerales-marcianos/CLASE.md).

### Rendimiento de extracción

- El rendimiento de extracción `η` es la fracción del hierro del regolito que se recupera.

🎯 **Por qué importa (clase B84-C38):** Un repuesto que llega en 180 días puede producirse en 1,3 días, pero la planta pesa 400 kg y procesa 74 kg de regolito por pieza: el balance dice cuándo compensa. La decisión central: ¿cuántos repuestos hacen que producir in situ sea mejor que transportarlos?

📘 **Dónde se aprende** (1 clase): [B84-C38 · Producción de piezas y repuestos con materia prima in situ](../programa/clases/B84/B84-C38-produccion-de-piezas-y-repuestos-con-materia-prima-in-situ/CLASE.md).

### Rendimiento de pieza

- El rendimiento de pieza es la fracción del metal que acaba en la pieza.

💡 **Cómo se explica en la clase [B84-C38](../programa/clases/B84/B84-C38-produccion-de-piezas-y-repuestos-con-materia-prima-in-situ/CLASE.md):**
- A["pieza 2 kg"] --> B["hierro = m / rendimiento"]
- Un repuesto de `2,0 kg` con rendimiento de pieza `0,80` necesita `2,50 kg` de hierro, que con `f = 0,08` y `η = 0,50` requiere `62,5 kg` de regolito y `53,5 kWh` por intento (`26,8 h` a 2 kW).
- ⚠️ **Error frecuente:** Ignorar el rendimiento de la pieza. Se corrige con 8.1.
- 🎯 **Por qué importa:** Un repuesto que llega en 180 días puede producirse en 1,3 días, pero la planta pesa 400 kg y procesa 74 kg de regolito por pieza: el balance dice cuándo compensa. La decisión central: ¿cuántos repuestos hacen que producir in situ sea mejor que transportarlos?

📘 **Dónde se aprende** (1 clase): [B84-C38 · Producción de piezas y repuestos con materia prima in situ](../programa/clases/B84/B84-C38-produccion-de-piezas-y-repuestos-con-materia-prima-in-situ/CLASE.md).

### Rendimiento decreciente

- Un rendimiento decreciente es cada vez menos efecto por unidad añadida.

🎯 **Por qué importa (clase B105-C16):** Más ejercicio ayuda, pero con rendimientos decrecientes y con un costo de energía y tiempo. La decisión central: ¿qué parte de la pérdida se evita con una carga dada y cuánta energía extra exige?

📘 **Dónde se aprende** (1 clase): [B105-C16 · Contramedidas de ejercicio](../programa/clases/B105/B105-C16-contramedidas-de-ejercicio/CLASE.md).

### Rendimiento ideal

- Su rendimiento ideal es `η = 1 − r^(−(γ−1)/γ)`.

💡 **Cómo se explica en la clase [B79-C15](../programa/clases/B79/B79-C15-ciclos-termodinamicos-de-propulsion/CLASE.md):**
- En el ciclo ideal el trabajo máximo (`419,99 kJ/kg`) está en `r = 15,91` (analítica `15,914`) con `η = 0,5464`, mientras que el rendimiento crece sin límite con `r`.
- Con `T₁ = 288 K` y `T_max = 1400 K`, el ciclo ideal a `r = 20` da `0,5751` de rendimiento y `417,27 kJ/kg`; el ciclo con pérdidas da `0,3238` y `277,55 kJ/kg`; el trabajo máximo ideal está en `r = 15,9`.
- ⚠️ **Error frecuente:** Maximizar solo el rendimiento ideal. Se corrige con 8.2.
- 🎯 **Por qué importa:** B85-C11 trata ciclos térmicos de ensayo, no termodinámicos. Para entender el rendimiento de una turbina de gas hay que ver el ciclo que lo origina.

📘 **Dónde se aprende** (1 clase): [B79-C15 · Ciclos termodinámicos de propulsión](../programa/clases/B79/B79-C15-ciclos-termodinamicos-de-propulsion/CLASE.md).

### Rendimiento isentrópico

- El rendimiento isentrópico compara el proceso real con el ideal adiabático reversible.

💡 **Cómo se explica en la clase [B79-C10](../programa/clases/B79/B79-C10-primera-ley-de-la-termodinamica-en-sistemas-abiertos/CLASE.md):**
- Sin segunda ley no se puede decir que un compresor real consuma más que uno isentrópico (eso lo da el rendimiento, un dato).
- Calcular el trabajo de un compresor y de una turbina con rendimiento isentrópico.
- 🎯 **Por qué importa:** B05-C13 ve temperatura y energía térmica, pero no la formulación de volumen de control usada en propulsión. Sin ella no se calcula el trabajo de un compresor ni la velocidad de una tobera.

📘 **Dónde se aprende** (1 clase): [B79-C10 · Primera ley de la termodinámica en sistemas abiertos](../programa/clases/B79/B79-C10-primera-ley-de-la-termodinamica-en-sistemas-abiertos/CLASE.md).

### Rendimiento másico

- El rendimiento másico es la fracción de la alimentación que forma el producto.

💡 **Cómo se explica en la clase [B59-C22](../programa/clases/B59/B59-C22-beneficio-y-separacion-granulometrica-de-regolito/CLASE.md):**
- Rendimiento masico: fino = 52.61 % ; grueso = 47.39 % (suma 100.00 %)
- 🎯 **Por qué importa:** Calentar o reducir todo el regolito es caro; separar la fracción rica antes ahorra energía. La decisión central: ¿qué tamaño de corte equilibra la ley del concentrado y la recuperación del mineral?

📘 **Dónde se aprende** (1 clase): [B59-C22 · Beneficio y separación granulométrica de regolito](../programa/clases/B59/B59-C22-beneficio-y-separacion-granulometrica-de-regolito/CLASE.md).

### Rendimientos decrecientes

- Los rendimientos decrecientes hacen que la capacidad extra aporte cada vez menos: `v = 1 − exp(−y/τ)`.

💡 **Cómo se explica en la clase [B124-C12](../programa/clases/B124/B124-C12-evaluacion-de-retorno-cientifico/CLASE.md):**
- Definir un valor científico por objetivo con rendimientos decrecientes.
- 🎯 **Por qué importa:** El retorno científico no tiene un precio de mercado, pero se puede razonar con una función de valor explícita y una frontera de eficiencia. La decisión central: ¿qué opciones valen la pena a su costo y cuáles están dominadas?

📘 **Dónde se aprende** (1 clase): [B124-C12 · Evaluación de retorno científico](../programa/clases/B124/B124-C12-evaluacion-de-retorno-cientifico/CLASE.md).

### Renormalización

- La renormalización divide por `|q|` tras cada paso.
- La renormalización reescala las fracciones para que sumen 1.

💡 **Cómo se explica en la clase [B10-C20](../programa/clases/B10/B10-C20-cinematica-de-orientacion-satelital/CLASE.md):**
- *Descripción textual:* en cada paso se evalúa la derivada, se avanza con el método elegido, se renormaliza y se repite; al final se compara con la solución exacta mediante el ángulo de la rotación relativa.
- Paso 1 · Datos. `ω = 0,1 (1,1,1)/√3 rad/s`, `t = 60 s`, `h = 0,1 s`, RK4 con renormalización (sintéticos).
- 🎯 **Por qué importa:** Los giróscopos de un satélite miden la velocidad angular en ejes del cuerpo. Para saber hacia dónde apunta una cámara, hay que integrar esa velocidad en el tiempo, miles de veces.

📘 **Dónde se aprende** (2 clases): [B10-C20 · Cinemática de orientación satelital](../programa/clases/B10/B10-C20-cinematica-de-orientacion-satelital/CLASE.md); [B54-C02 · Composición química atmosférica](../programa/clases/B54/B54-C02-composicion-quimica-atmosferica/CLASE.md).

### Renovación

- Tasa de costo: costo esperado entre tiempo esperado. Renovación: reinicio del ciclo.

💡 **Cómo se explica en la clase [B48-C14](../programa/clases/B48/B48-C14-mantenimiento-preventivo/CLASE.md):**
- Verificarlo con una simulación de renovación.
- 🎯 **Por qué importa:** Reemplazar muy pronto desperdicia vida útil; muy tarde, produce fallas caras. La decisión central: ¿cada cuántas horas conviene reemplazar?

📘 **Dónde se aprende** (1 clase): [B48-C14 · Mantenimiento preventivo](../programa/clases/B48/B48-C14-mantenimiento-preventivo/CLASE.md).

### Renovaciones por hora (ACH)

- Filtro de alta eficiencia: filtro que retiene la fracción `η` de las partículas del aire que lo cruza. Renovaciones por hora (ACH): `Q·3600/V`.

💡 **Cómo se explica en la clase [B90-C02](../programa/clases/B90/B90-C02-buenas-practicas-de-sala-limpia/CLASE.md):**
- Por renovaciones de aire: 36 por hora aquí.
- Una sala de 5 m × 4 m × 3 m (60 m³) recibe 0,60 m³/s de aire filtrado: 36 renovaciones por hora.
- 🎯 **Por qué importa:** Una partícula sobre una óptica, un sello o un contacto puede degradar una misión; las partículas llegan con el aire, la ropa y las herramientas. La decisión central: ¿qué clase de sala puede sostener esta actividad con este número de personas, y cuánto hay que esperar tras una perturbación?

📘 **Dónde se aprende** (1 clase): [B90-C02 · Buenas prácticas de sala limpia](../programa/clases/B90/B90-C02-buenas-practicas-de-sala-limpia/CLASE.md).

### Reparación

- La reparación devuelve la integridad al ADN: la unión de extremos no homólogos (NHEJ) reúne los extremos directamente y puede cometer errores.
- La reparación busca, según el artículo XII leído, compensar «in accordance with international law and the principles of justice and equity».

💡 **Cómo se explica en la clase [B112-C05](../programa/clases/B112/B112-C05-dano-y-reparacion-del-adn-por-radiacion-espacial/CLASE.md):**
- Se cuenta cada par de roturas a menos de 0,5 µm cuando una se repara antes que la otra.
- A --> K["reparación lenta<br/>(tasa 0,05/h)"]
- ⚠️ **Error frecuente:** Pensar que más roturas iniciales explican el mayor daño. El rendimiento inicial es igual; la diferencia está en la reparación (8.3).
- 🎯 **Por qué importa:** Falta la clase de mecanismos moleculares de daño y reparación. Sin ella, la diferencia de eficacia biológica entre fotones e iones pesados (B112-C01, C02) y la incertidumbre del riesgo (C04) parecen cifras arbitrarias.

📘 **Dónde se aprende** (2 clases): [B112-C05 · Daño y reparación del ADN por radiación espacial](../programa/clases/B112/B112-C05-dano-y-reparacion-del-adn-por-radiacion-espacial/CLASE.md); [B123-C01 · Prueba del daño y cuantificación de la reparación](../programa/clases/B123/B123-C01-prueba-del-dano-y-cuantificacion-de-la-reparacion/CLASE.md).

### Reparto

- El reparto es la división del ángulo `i = i₁ + i₂` entre dos impulsos.
- La difusión (*broadcast*) copia un dato del proceso raíz a todos; el reparto (*scatter*) divide una colección de la raíz entre los procesos; la reunión (*gather*) hace lo contrario; la reducción (*reduce*) combina valores de todos con una operación (suma, máximo…) y la deja en la raíz, y `allreduce` la deja en todos.

💡 **Cómo se explica en la clase [B18-C02](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md):**
- Reparto cíclico. El rango `r` suma los índices `r, r+P, …`.
- Elegir entre difusión, reparto, reunión y reducción para un patrón dado.
- 🎯 **Por qué importa:** Ocho, cuarenta o cuatro mil núcleos de un clúster no comparten memoria. Para que cada uno propague su parte de un catálogo de órbitas y luego se junten los resultados, hay que decir quién envía qué a quién, y cuándo.

📘 **Dónde se aprende** (2 clases): [B18-C02 · Paso de mensajes con MPI](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md); [B75-C13 · Cambios de plano interplanetarios](../programa/clases/B75/B75-C13-cambios-de-plano-interplanetarios/CLASE.md).

### Reparto de Stribeck

- El reparto de Stribeck `Q(ψ) = Q_max cos^(3/2) ψ`.

💡 **Cómo se explica en la clase [B43-C25](../programa/clases/B43/B43-C25-rodamientos-y-apoyos-de-precision-en-telescopios/CLASE.md):**
- Plantear el reparto de Stribeck `cos^(3/2) ψ`.
- El script [rodamientos.py](rodamientos.py) calcula Hertz, lo verifica con integrales y calcula el reparto de Stribeck (comprueba `10⁻⁵` y `0,5 %`).
- 🎯 **Por qué importa:** La rigidez del contacto determina cuánto se mueve el eje bajo carga y la frecuencia de resonancia. La decisión central: ¿cuánto se deforma el contacto, cuánta rigidez aporta y qué fracción de la carga soporta la bola más cargada?

📘 **Dónde se aprende** (1 clase): [B43-C25 · Rodamientos y apoyos de precisión en telescopios](../programa/clases/B43/B43-C25-rodamientos-y-apoyos-de-precision-en-telescopios/CLASE.md).

### Reparto óptimo

- El reparto óptimo divide `Δi` entre los dos impulsos.
- El reparto óptimo distribuye `Δv` entre etapas para maximizar la carga.

💡 **Cómo se explica en la clase [B71-C19](../programa/clases/B71/B71-C19-cambios-de-plano-simples/CLASE.md):**
- C --> R["reparto optimo entre dv1 y dv2"]
- *Descripción textual:* el cambio de plano cuesta más cuanto mayor es la velocidad; combinarlo con los impulsos de la Hohmann reparte el costo y un reparto óptimo lo minimiza; cambiar la RAAN es otro cambio de plano.
- 🎯 **Por qué importa:** Un cambio de plano mal ubicado puede costar más que todo el resto de la misión orbital. La decisión central: ¿dónde y cómo conviene cambiar el plano para gastar el mínimo `Δv`?

📘 **Dónde se aprende** (2 clases): [B71-C19 · Cambios de plano simples](../programa/clases/B71/B71-C19-cambios-de-plano-simples/CLASE.md); [B124-C23 · Costos de transporte por kilogramo a superficie](../programa/clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md).

### Reparto ponderado

- El reparto ponderado asigna a cada clase una fracción de la capacidad proporcional a su peso (aquí 4 : 2 : 1) y reparte lo que sobra.

💡 **Cómo se explica en la clase [B94-C05](../programa/clases/B94/B94-C05-calidad-de-servicio-y-prioridades-en-redes-espaciales/CLASE.md):**
- El reparto ponderado protege E, pero perjudica a N: su peso (2/7 de 30 MB ≈ 8,6 MB) es menor que su demanda (18 MB); los pesos deben acompasarse con la demanda.
- El reparto ponderado garantiza a B al menos `30/7 ≈ 4,3` MB por contacto y por eso entrega el 60,8 %.
- 🎯 **Por qué importa:** Si la demanda supera a la capacidad, alguien espera. La decisión central: ¿qué política de cola garantiza lo urgente sin dejar sin servicio a las demás clases, y a qué coste?

📘 **Dónde se aprende** (1 clase): [B94-C05 · Calidad de servicio y prioridades en redes espaciales](../programa/clases/B94/B94-C05-calidad-de-servicio-y-prioridades-en-redes-espaciales/CLASE.md).

### Reparto proporcional

- Un reparto proporcional sigue los aportes individuales.

💡 **Cómo se explica en la clase [B119-C36](../programa/clases/B119/B119-C36-gobernanza-de-los-recursos-espaciales/CLASE.md):**
- Pertenece al núcleo: igual `True`, proporcional `True`, Shapley `True`: con estos valores el núcleo es amplio y los tres repartos son estables.
- Comparar con el reparto igual y el proporcional.
- 🎯 **Por qué importa:** B59 trata los recursos de forma técnica; la gobernanza de la explotación plantea cuestiones de reparto que ninguna clase trata. C25 da el caso económico y C34 las medidas de desigualdad; esta clase cierra el bloque con reglas de reparto.

📘 **Dónde se aprende** (1 clase): [B119-C36 · Gobernanza de los recursos espaciales](../programa/clases/B119/B119-C36-gobernanza-de-los-recursos-espaciales/CLASE.md).

### Repaso espaciado

- El repaso espaciado reparte las repeticiones en el tiempo y aumenta `S`.

💡 **Cómo se explica en la clase [B104-C06](../programa/clases/B104/B104-C06-entrenamiento-de-procedimientos/CLASE.md):**
- V["repasos espaciados"] --> S["S aumenta ×2,5"]
- *Descripción textual:* las repeticiones reducen el tiempo de ejecución con una ley potencial; el olvido lo deteriora con una exponencial; los repasos espaciados alargan la estabilidad de la memoria.
- 🎯 **Por qué importa:** Los procedimientos se practican en tierra y a veces se usan meses después, en el momento crítico. La decisión central: ¿cuándo repasar para que el procedimiento siga disponible sin gastar tiempo de entrenamiento de más?

📘 **Dónde se aprende** (1 clase): [B104-C06 · Entrenamiento de procedimientos](../programa/clases/B104/B104-C06-entrenamiento-de-procedimientos/CLASE.md).

### Repetibilidad

- Razón de distancias: distancia al vecino más cercano entre la del segundo más cercano (F3). Repetibilidad: fracción de puntos de una imagen que se detectan también en la otra.

💡 **Cómo se explica en la clase [B99-C02](../programa/clases/B99/B99-C02-deteccion-y-descriptores-de-caracteristicas/CLASE.md):**
- El parche no está orientado: si B se gira 90°, el detector sigue hallando las esquinas (repetibilidad 100 %) pero los emparejamientos fallan (precisión 0 %).
- Detectar esquinas con el criterio de Harris y medir su repetibilidad entre dos vistas.
- ⚠️ **Error frecuente:** Confundir repetibilidad con precisión de emparejamiento. La primera es del detector; la segunda, del par detector–descriptor–regla (8.4).
- 🎯 **Por qué importa:** Una esquina de una roca puede verse distinta cuando cambian el brillo, el ruido o el punto de vista, y dos rocas parecidas se confunden. La decisión central: ¿qué puntos conviene usar, cómo se describen y cuándo se acepta un emparejamiento?

📘 **Dónde se aprende** (1 clase): [B99-C02 · Detección y descriptores de características](../programa/clases/B99/B99-C02-deteccion-y-descriptores-de-caracteristicas/CLASE.md).

### Repetición de lectura

- La repetición de lectura es devolver lo recibido para confirmarlo.

💡 **Cómo se explica en la clase [B104-C08](../programa/clases/B104/B104-C08-comunicacion-de-tripulacion/CLASE.md):**
- *Descripción textual:* la distancia fija el retardo y el tiempo de cada intercambio; el mensaje tiene un error por palabra; la repetición de lectura reduce el error residual al costo de dos retardos adicionales.
- Un mensaje de 20 palabras con 1 % de error por palabra llega mal el 18,2 % de las veces; con repetición de lectura (detección de 0,95) el error residual baja a 0,9 %.
- 🎯 **Por qué importa:** A 1,28 s de la Luna aún se conversa; a más de 3 minutos de Marte ya no. La decisión central: ¿qué protocolo de mensajes usar cuando cada ida y vuelta cuesta minutos y un error cuesta caro?

📘 **Dónde se aprende** (1 clase): [B104-C08 · Comunicación de tripulación](../programa/clases/B104/B104-C08-comunicacion-de-tripulacion/CLASE.md).

### Repetir

- SHA-256 es una función de huella de 256 bits. Repetir es volver a ejecutar el mismo código con los mismos datos;

💡 **Cómo se explica en la clase [B07-C19](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md):**
- Que tu script dé lo mismo dos veces (repetir) es lo mínimo.
- Límite de la analogía: en la cocina, «repetir» un plato nunca da exactamente lo mismo; en computación, con las mismas entradas el resultado puede ser idéntico bit a bit, pero solo si todas las entradas (incluidas las ocultas, como la versión de una biblioteca o el procesador) coinciden.
- ⚠️ **Error frecuente:** Confundir repetir con validar. Se corrige con el paso final de la sección 13.
- 🎯 **Por qué importa:** Un resultado que solo su autor puede obtener, y solo el día en que lo obtuvo, es una anécdota. Cuando pasan seis meses, no sabrás con qué datos, con qué versión ni con qué semilla lo generaste.

📘 **Dónde se aprende** (1 clase): [B07-C19 · Documentación y reproducibilidad](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md).

### Replanificación

- La replanificación recalcula el plan desde el instante actual con el estado real.

💡 **Cómo se explica en la clase [B98-C01](../programa/clases/B98/B98-C01-planificacion-por-objetivos-a-bordo/CLASE.md):**
- La replanificación usa el mismo código que la planificación; cambian el instante inicial y la energía.
- ¿Qué ventaja da la replanificación a bordo?
- 🎯 **Por qué importa:** Si el vehículo solo ejecuta una secuencia fija de comandos, un fallo a mitad de jornada deja sin sentido el resto del plan y hay que esperar la respuesta de Tierra. La decisión central: ¿qué objetivos conviene ejecutar con la energía y el tiempo disponibles, y qué hace el vehículo cuando la energía disponible baja de golpe?

📘 **Dónde se aprende** (1 clase): [B98-C01 · Planificación por objetivos a bordo](../programa/clases/B98/B98-C01-planificacion-por-objetivos-a-bordo/CLASE.md).

### Réplica

- Una réplica `y_rep` es un conjunto de datos simulado del modelo ajustado, del mismo tamaño que los observados.

💡 **Cómo se explica en la clase [B19-C06](../programa/clases/B19/B19-C06-distribucion-predictiva-posterior/CLASE.md):**
- Para cada réplica `y_rep^(s)` se calcula `T(y_rep^(s))`; la proporción de réplicas con `T(y_rep) ≥ T(y)` es el valor p.
- *Descripción textual:* desde los datos se obtiene la posterior; de ella se sortean parámetros y réplicas; se calcula el estadístico en réplicas y en los datos; si el valor observado cae dentro de la nube de réplicas el modelo capta esa característica, y si no, se revisa.
- 🎯 **Por qué importa:** El contador de partículas lleva 12 horas midiendo. Con la posterior de la tasa `λ`, la pregunta práctica es: ¿cuántos eventos esperar en la hora 13, y qué tan sorprendente sería ver 8?

📘 **Dónde se aprende** (1 clase): [B19-C06 · Distribución predictiva posterior](../programa/clases/B19/B19-C06-distribucion-predictiva-posterior/CLASE.md).

### Replicabilidad

- Reproducibilidad es obtener el mismo resultado con los mismos datos y código; replicabilidad, llegar al mismo resultado con otro código.

🎯 **Por qué importa (clase B11-C20):** Un resultado numérico que nadie puede reproducir no es ciencia. Si dentro de un año hay que saber por qué una trayectoria salió así, hacen falta la configuración exacta, las versiones del software y pruebas que digan si el programa sigue funcionando.

📘 **Dónde se aprende** (1 clase): [B11-C20 · Propagador reproducible de trayectoria](../programa/clases/B11/B11-C20-propagador-reproducible-de-trayectoria/CLASE.md).

### Replicador

- Un replicador es una molécula que dirige su propia copia.

💡 **Cómo se explica en la clase [B56-C03](../programa/clases/B56/B56-C03-origen-de-moleculas-autorreplicantes/CLASE.md):**
- Los valores son ilustrativos: no son tasas medidas de ningún replicador real.
- Definir replicador, secuencia maestra, fidelidad, calidad de copia y umbral de error.
- 🎯 **Por qué importa:** Un replicador que copia mal pierde su información; uno que copia bien necesita una maquinaria que, sin vida previa, aún no existe. Esa tensión limita el tamaño de los primeros genomas.

📘 **Dónde se aprende** (1 clase): [B56-C03 · Origen de moléculas autorreplicantes](../programa/clases/B56/B56-C03-origen-de-moleculas-autorreplicantes/CLASE.md).

### Replicarse

- Sobrevivir es conservar la viabilidad sin dividirse; replicarse es dividirse y propagarse.

💡 **Cómo se explica en la clase [B56-C05](../programa/clases/B56/B56-C05-extremofilos-y-limites-ambientales/CLASE.md):**
- Distinguir sobrevivir, metabolizar y replicarse.
- Ejercicio 6. ¿Qué diferencia hay entre sobrevivir y replicarse en un ambiente a −40 °C?
- ⚠️ **Error frecuente:** Confundir sobrevivir con replicarse. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** Decidir si un ambiente es habitable, o si una nave puede contaminarlo, exige umbrales de temperatura y de agua disponible. La decisión central: dada la temperatura y la actividad del agua de un ambiente, ¿está dentro de los límites en que la vida terrestre puede replicarse?

📘 **Dónde se aprende** (1 clase): [B56-C05 · Extremófilos y límites ambientales](../programa/clases/B56/B56-C05-extremofilos-y-limites-ambientales/CLASE.md).

### Re-ponderación sensorial

- La re-ponderación sensorial es el cambio de esos pesos según la fiabilidad de cada fuente.

📘 **Dónde se aprende** (1 clase): [B107-C07 · Rehabilitación vestibular y del equilibrio posterior al vuelo](../programa/clases/B107/B107-C07-rehabilitacion-vestibular-y-del-equilibrio-posterior-al-vuelo/CLASE.md).

### Reposición

- La reposición (*make-up*) es lo que debe aportarse desde fuera.
- La reposición es lanzar un satélite nuevo cuando otro termina su vida.
- Recuperación `r`: fracción de agua reutilizada. Reposición: agua nueva que hay que aportar.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B59-C15](../programa/clases/B59/B59-C15-ciclo-cerrado-de-materiales/CLASE.md):**
- Si la cola de retorno empieza vacía, durante `τ = 3` días no vuelve nada: la reposición total es `D T − ρ D (T − τ) = 1 650,74 kg`, `65,49 kg` más que en régimen (`ρ D τ`).
- Subir una etapa a `0,999`: la etapa 1 deja `ρ = 0,96923` y una reposición de `0,769 kg/día`; la etapa 2, `2,747 kg/día`; la etapa 3, `2,972 kg/día`.
- 🎯 **Por qué importa:** Cerrar el 87 % de un lazo no deja una reposición del 13 % sino una dependencia permanente del 13 %. La decisión central: ¿qué etapa del lazo conviene mejorar para reducir más la reposición?

📘 **Dónde se aprende** (4 clases): [B59-C15 · Ciclo cerrado de materiales](../programa/clases/B59/B59-C15-ciclo-cerrado-de-materiales/CLASE.md); [B106-C06 · Reciclaje de agua](../programa/clases/B106/B106-C06-reciclaje-de-agua/CLASE.md); [B106-C09 · Sistemas ECLSS](../programa/clases/B106/B106-C09-sistemas-eclss/CLASE.md); [B124-C11 · Sostenibilidad económica de constelaciones](../programa/clases/B124/B124-C11-sostenibilidad-economica-de-constelaciones/CLASE.md).

### Reposición terrestre

- La reposición terrestre es `R = máx(0, D(1 − η) − P) + repuestos`.

💡 **Cómo se explica en la clase [B100-C07](../programa/clases/B100/B100-C07-dependencia-de-suministros-terrestres-y-cierre-de-lazos-logisticos/CLASE.md):**
- *Descripción textual:* del consumo, la parte recuperada vuelve al lazo y la pérdida, menos la producción en el lugar, más los repuestos del equipo, forma la reposición terrestre.
- Con eficiencia 0,80 la reposición terrestre es `3,332 kg/d` (20,8 % del consumo); con 0,90, `1,732 kg/d` (10,8 %); con 0,98, `0,452 kg/d` (2,8 %).
- 🎯 **Por qué importa:** Reciclar el 90 % del agua no reduce la dependencia en un 90 %: quedan repuestos, fugas y averías, y el equipo pesa. La decisión central: ¿cuánta reposición terrestre queda según la eficiencia del lazo y cuántos días tarda el equipo en compensar su propia masa?

📘 **Dónde se aprende** (1 clase): [B100-C07 · Dependencia de suministros terrestres y cierre de lazos logísticos](../programa/clases/B100/B100-C07-dependencia-de-suministros-terrestres-y-cierre-de-lazos-logisticos/CLASE.md).

### Repositorio

- Un repositorio es una carpeta con la historia del proyecto (en `.git`).

💡 **Cómo se explica en la clase [B07-C14](../programa/clases/B07/B07-C14-control-de-versiones-con-git/CLASE.md):**
- El laboratorio ejecuta exactamente esa historia en un repositorio temporal, con una identidad ficticia.
- Explicar qué es un repositorio, un commit y las tres zonas de Git.
- 🎯 **Por qué importa:** Sin control de versiones, un proyecto científico acumula archivos como `analisis_final.py`, `analisis_final2.py` y `analisis_final_ahora_si.py`, y nadie sabe cuál produjo la figura del artículo. Con Git, cada estado importante queda guardado con un mensaje, una fecha y un autor, y puedes comparar o recuperar cualquier versión.

📘 **Dónde se aprende** (1 clase): [B07-C14 · Control de versiones con Git](../programa/clases/B07/B07-C14-control-de-versiones-con-git/CLASE.md).

### Reposo

- El reposo `r` es el tiempo que necesita un reanimador para recuperarse.

💡 **Cómo se explica en la clase [B117-C01](../programa/clases/B117/B117-C01-primeros-auxilios-y-procedimientos-basicos-en-entorno-espacial/CLASE.md):**
- Si cada reanimador trabaja `t*` y necesita `r = 4 min` de reposo, hacen falta `n = ⌈(t* + r)/t*⌉ = ⌈3,77⌉ = 4` reanimadores.
- Separar lo consultado (medianas de maniquí) de lo ilustrativo (fatiga, reposo).
- ⚠️ **Error frecuente:** Olvidar el reposo al contar reanimadores. Se corrige con 8.3.
- 🎯 **Por qué importa:** Ninguna clase anterior trata primeros auxilios en microgravedad. La decisión central: ¿cuánto tiempo puede sostener un reanimador una compresión de calidad y cuándo hay que relevarlo?

📘 **Dónde se aprende** (1 clase): [B117-C01 · Primeros auxilios y procedimientos básicos en entorno espacial](../programa/clases/B117/B117-C01-primeros-auxilios-y-procedimientos-basicos-en-entorno-espacial/CLASE.md).

### Representación en espacio de estados

- La representación en espacio de estados de un sistema lineal e invariante continuo es el par de ecuaciones `ẋ = A x + B u` (ecuación de estado) y `y = C x + D u` (ecuación de salida).

💡 **Cómo se explica en la clase [B16-C02](../programa/clases/B16/B16-C02-representaciones-en-espacio-de-estados/CLASE.md):**
- python programa/clases/B16/B16-C02-representaciones-en-espacio-de-estados/matrices_de_estado.py
- 🎯 **Por qué importa:** El computador de a bordo de un satélite no maneja ecuaciones sueltas: maneja vectores y matrices, y una sola rutina sirve para cualquier eje, rueda o sensor que se le añada.

📘 **Dónde se aprende** (1 clase): [B16-C02 · Representaciones en espacio de estados](../programa/clases/B16/B16-C02-representaciones-en-espacio-de-estados/CLASE.md).

### Reprocesado

- El reprocesado repite el filtro desde un estado guardado con las medidas en orden.

🎯 **Por qué importa (clase B74-C24):** Una medida tardía contiene información valiosa pero tratarla mal puede dañar más que descartarla. La decisión central: ¿qué tratamiento de una medida tardía mejora el estimado sin romper la consistencia, y a qué coste?

📘 **Dónde se aprende** (1 clase): [B74-C24 · Medidas retardadas y fuera de secuencia en filtros de estimación](../programa/clases/B74/B74-C24-medidas-retardadas-y-fuera-de-secuencia-en-filtros-de-estimacion/CLASE.md).

### Reproducibilidad

- La reproducibilidad es la posibilidad de que otra persona repita tu procedimiento y obtenga un resultado compatible.
- La reproducibilidad es la posibilidad de que otra persona repita tu observación o tu cálculo con tus registros.
- Una prueba de regresión vuelve a ejecutar un caso conocido y exige el mismo resultado. Reproducibilidad es obtener el mismo resultado con los mismos datos y código;
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C26](../programa/clases/B11/B11-C26-benchmark-de-algoritmos-numericos/CLASE.md):**
- Paso 5 · Reproducibilidad. Ambos pasaron la repetición exacta.
- Verificar la reproducibilidad del benchmark.
- 🎯 **Por qué importa:** «El método A es mejor que el B» es una afirmación vacía sin el problema, la métrica, la tolerancia y el costo. Una comparación mal diseñada lleva a elegir el algoritmo equivocado para una misión.

📘 **Dónde se aprende** (7 clases): [B01-C20 · Proyecto de observación científica inicial](../programa/clases/B01/B01-C20-proyecto-de-observacion-cientifica-inicial/CLASE.md); [B08-C17 · Registro sistemático en bitácora](../programa/clases/B08/B08-C17-registro-sistematico-en-bitacora/CLASE.md); [B11-C20 · Propagador reproducible de trayectoria](../programa/clases/B11/B11-C20-propagador-reproducible-de-trayectoria/CLASE.md); [B11-C26 · Benchmark de algoritmos numéricos](../programa/clases/B11/B11-C26-benchmark-de-algoritmos-numericos/CLASE.md); [B12-C23 · Diagnóstico de convergencia y reproducibilidad de cadenas MCMC](../programa/clases/B12/B12-C23-diagnostico-de-convergencia-y-reproducibilidad-de-cadenas-mcmc/CLASE.md); [B74-C22 · Informe de navegación verificable](../programa/clases/B74/B74-C22-informe-de-navegacion-verificable/CLASE.md) y 1 más.

### Reproducir

- Repetir es volver a ejecutar el mismo código con los mismos datos; reproducir es obtener el mismo resultado de forma independiente, a partir de la descripción.

💡 **Cómo se explica en la clase [B07-C19](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md):**
- Reproducir exige que otra persona, con tu README y tu registro, llegue al mismo resultado en su máquina.
- 🎯 **Por qué importa:** Un resultado que solo su autor puede obtener, y solo el día en que lo obtuvo, es una anécdota. Cuando pasan seis meses, no sabrás con qué datos, con qué versión ni con qué semilla lo generaste.

📘 **Dónde se aprende** (1 clase): [B07-C19 · Documentación y reproducibilidad](../programa/clases/B07/B07-C19-documentacion-y-reproducibilidad/CLASE.md).

### Repuesto

- Causa común (β): fracción de fallas que afecta a todos. Repuesto: unidad de reemplazo.

💡 **Cómo se explica en la clase [B106-C18](../programa/clases/B106/B106-C18-fiabilidad-y-redundancia/CLASE.md):**
- Con 5 repuestos la cobertura es 0,9515 y con 7, 0,9948.
- *Descripción textual:* la tasa de falla da la fiabilidad de una unidad; la redundancia la mejora y la flota esperada de fallas fija los repuestos.
- ⚠️ **Error frecuente:** Dimensionar repuestos con la media. Usa el percentil de Poisson (8.5).
- 🎯 **Por qué importa:** Ningún equipo es perfecto y una misión larga no se puede reparar con repuestos de la Tierra. La decisión central: ¿qué configuración redundante y cuántos repuestos dan una probabilidad objetivo de cumplir la misión?

📘 **Dónde se aprende** (1 clase): [B106-C18 · Fiabilidad y redundancia](../programa/clases/B106/B106-C18-fiabilidad-y-redundancia/CLASE.md).

### Repuestos

- Los repuestos se expresan como fracción de la masa.

💡 **Cómo se explica en la clase [B100-C02](../programa/clases/B100/B100-C02-dimensionamiento-de-carga-y-volumen-de-mision/CLASE.md):**
- C["consumibles<br/>tasa x personas x días"] --> E["embalaje y<br/>repuestos"]
- *Descripción textual:* la carga neta se infla por el embalaje y los repuestos, y luego se calcula, tramo a tramo y hacia atrás, la masa que debe existir antes de cada maniobra.
- 🎯 **Por qué importa:** La masa que llega a la superficie es una fracción pequeña de la que sale de la Tierra, y el volumen puede decidir antes que la masa. La decisión central: ¿cuánta masa y cuánto volumen hay que cargar para N personas durante D días, y cuánta masa hay que lanzar para que esa carga llegue?

📘 **Dónde se aprende** (1 clase): [B100-C02 · Dimensionamiento de carga y volumen de misión](../programa/clases/B100/B100-C02-dimensionamiento-de-carga-y-volumen-de-mision/CLASE.md).

### Requisito

- Un requisito es una condición que la solución debe cumplir.
- Un requisito es una condición que la campaña debe cumplir; debe ser verificable: tener un criterio de comprobación (un número o un sí/no) y un método de comprobación.
- Un requisito es una condición medible que la cadena debe cumplir.
- *(y 9 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C20](../programa/clases/B03/B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md):**
- Con R1, la Tierra mide 0,85 mm: el requisito de ver los planetas (si se pidiera que fuesen visibles, por ejemplo, de 1 cm) choca con R2.
- R["Requisitos: 1 au = 10 m; cabe en 350 m; misma escala para todo"] --> E["Factor de escala E = 1 au / 10 m"]
- ⚠️ **Error frecuente:** No declarar el conflicto de requisitos. Ejercicio 6.
- 🎯 **Por qué importa:** Un ingeniero no recibe un ejercicio con una sola fórmula: recibe requisitos («que quepa en un patio de 350 m», «que se vea el Sol», «que Neptuno esté a su sitio») y debe decidir qué se puede cumplir y qué no.

📘 **Dónde se aprende** (13 clases): [B03-C20 · Problema integrado de escala del sistema solar](../programa/clases/B03/B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md); [B08-C20 · Proyecto de campaña de observación nocturna](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md); [B15-C20 · Proyecto de detección y seguimiento](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md); [B16-C19 · Verificación de lazo cerrado](../programa/clases/B16/B16-C19-verificacion-de-lazo-cerrado/CLASE.md); [B25-C20 · Proyecto de clasificación galáctica](../programa/clases/B25/B25-C20-proyecto-de-clasificacion-galactica/CLASE.md); [B43-C20 · Proyecto mecánico completo de telescopio](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md) y 7 más.

### Requisito completo

- Un requisito completo nombra valor, eje, índice, estadística, confianza y periodo (S3).

🎯 **Por qué importa (clase B87-C22):** Un requisito de apuntamiento solo se cumple si el diseño lo respalda con números. La decisión central: ¿qué contribuyentes dominan, cómo se combinan (suma lineal o cuadrática), con qué margen se cumple el requisito y qué ocurre con dos ejes?

📘 **Dónde se aprende** (1 clase): [B87-C22 · Presupuesto de error de apuntamiento](../programa/clases/B87/B87-C22-presupuesto-de-error-de-apuntamiento/CLASE.md).

### Requisito de medición

- Un requisito de medición traduce el objetivo a cantidades medibles (resolución, cobertura, precisión, cadencia).

💡 **Cómo se explica en la clase [B83-C01](../programa/clases/B83/B83-C01-necesidad-de-mision-y-caso-cientifico/CLASE.md):**
- *Descripción textual:* de la pregunta se pasa a un objetivo medible; de él salen el requisito de medición (que fija apertura, altura y franja) y la matriz ponderada de objetivos con su sensibilidad; ambos alimentan la ficha de necesidad.
- La evidencia es la ficha de necesidad de misión con requisito de medición derivado del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Un equipo sabe que quiere «mirar la costa» pero no cuánto debe resolver ni qué objetivo merece el presupuesto. La decisión central: ¿qué requisito de medición se deduce de la pregunta científica y qué objetivo conviene perseguir primero?

📘 **Dónde se aprende** (1 clase): [B83-C01 · Necesidad de misión y caso científico](../programa/clases/B83/B83-C01-necesidad-de-mision-y-caso-cientifico/CLASE.md).

### Requisito huérfano

- Un requisito huérfano no tiene origen; un requisito no verificado no tiene prueba; el diseño sin requisito es *gold plating* o un requisito faltante.

💡 **Cómo se explica en la clase [B83-C05](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md):**
- Un requisito huérfano es candidato a eliminarse o a justificarse con una necesidad nueva; una necesidad sin requisito, a convertirse en uno.
- *Descripción textual:* cada necesidad se enlaza con requisitos; estos, con diseño y verificación; un cambio en un requisito se propaga a lo que cuelga de él, y los huecos de la cadena son los huérfanos y la cobertura.
- 🎯 **Por qué importa:** Cuando cambia un requisito, ¿qué piezas y qué pruebas hay que revisar? Sin trazabilidad, nadie lo sabe y el cambio rompe algo en silencio.

📘 **Dónde se aprende** (1 clase): [B83-C05 · Trazabilidad de requisitos](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md).

### Requisito no verificado

- Un requisito huérfano no tiene origen; un requisito no verificado no tiene prueba; el diseño sin requisito es *gold plating* o un requisito faltante.

💡 **Cómo se explica en la clase [B83-C05](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md):**
- Cobertura: necesidades 83,3 %, requisitos con origen 87,5 %, requisitos verificados 87,5 % y diseño con requisito 83,3 %.
- Cobertura: necesidades 83.3 % ; requisitos con origen 87.5 % ; requisitos verificados 87.5 % ; diseno con requisito 83.3 %
- 🎯 **Por qué importa:** Cuando cambia un requisito, ¿qué piezas y qué pruebas hay que revisar? Sin trazabilidad, nadie lo sabe y el cambio rompe algo en silencio.

📘 **Dónde se aprende** (1 clase): [B83-C05 · Trazabilidad de requisitos](../programa/clases/B83/B83-C05-trazabilidad-de-requisitos/CLASE.md).

### Re-radiación

- La re-radiación es la emisión de la superficie, `εσ(T⁴ − T₀⁴)`.

💡 **Cómo se explica en la clase [B77-C16](../programa/clases/B77/B77-C16-proteccion-termica/CLASE.md):**
- Con flujo constante `10⁵ W/m²`, sin radiación y una losa de `5 cm` durante `10 s`: `T_s = T₀ + 2q₀√(αt/π)/k = 676,126 K` (analítico) frente a `675,946 K` (numérico); el error relativo al salto de temperatura es `4,8e-04`.
- La re-radiación evacúa el `86 %` de la energía.
- ⚠️ **Error frecuente:** Tomar el caso sin re-radiación como una predicción. Se corrige con 8.3.
- 🎯 **Por qué importa:** La temperatura de la cara trasera es la que decide si la estructura sobrevive. La decisión central: ¿cuánto del calor entrante se re-radia, cuánto se almacena y cuánto sube la temperatura trasera con un espesor dado?

📘 **Dónde se aprende** (1 clase): [B77-C16 · Protección térmica](../programa/clases/B77/B77-C16-proteccion-termica/CLASE.md).

### Resbalón

- Aquí: el resbalón es un fallo de ejecución (hacer otra cosa de la prevista), el descuido un fallo de memoria, la equivocación un plan equivocado y la violación una desviación deliberada de una regla; esta clasificación se toma como convención didáctica.

💡 **Cómo se explica en la clase [B111-C06](../programa/clases/B111/B111-C06-gestion-del-error-humano-y-cultura-de-seguridad/CLASE.md):**
- Por tipo: resbalón, descuido, equivocación, violación.
- Distinguir resbalón, descuido, equivocación y violación.
- 🎯 **Por qué importa:** Falta la clase sobre tipos de error, barreras y reporte. La decisión central: ¿dónde se pone el esfuerzo: en culpar al que erró o en reforzar las barreras y las condiciones que dejaron pasar el error?

📘 **Dónde se aprende** (1 clase): [B111-C06 · Gestión del error humano y cultura de seguridad](../programa/clases/B111/B111-C06-gestion-del-error-humano-y-cultura-de-seguridad/CLASE.md).

### Reserva

- Una reserva es la parte del recurso que, aplicados los factores modificadores (accesibilidad, recuperación), se puede extraer.
- La reserva es un porcentaje que se suma a las cargas por incertidumbre.
- La reserva es la cantidad de recursos disponibles (unidades arbitrarias).
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B67-C04](../programa/clases/B67/B67-C04-estimacion-de-reservas-y-categorias-de-recursos/CLASE.md):**
- Con accesibilidad `0,6` y recuperación `0,8` y sin convertir lo Inferido: el bloque de `3` muestras aporta `0` kt de reserva; el de `12`, `161,13` kt; el de `48`, `156,14` kt.
- En total hay `1127,55` kt de recurso y `317,27` kt de reserva.
- ⚠️ **Error frecuente:** Contar lo Inferido como reserva. Se corrige con 8.4.
- 🎯 **Por qué importa:** Decir «hay 330 kt» sin intervalo ni categoría invita a decisiones equivocadas. La decisión central: ¿cuánto del recurso se puede llamar reserva, y qué falta para subir de categoría?

📘 **Dónde se aprende** (5 clases): [B67-C04 · Estimación de reservas y categorías de recursos](../programa/clases/B67/B67-C04-estimacion-de-reservas-y-categorias-de-recursos/CLASE.md); [B83-C16 · Gestión de riesgos técnicos](../programa/clases/B83/B83-C16-gestion-de-riesgos-tecnicos/CLASE.md); [B86-C01 · Balance de potencia eléctrica](../programa/clases/B86/B86-C01-balance-de-potencia-electrica/CLASE.md); [B105-C14 · Atención de urgencia remota](../programa/clases/B105/B105-C14-atencion-de-urgencia-remota/CLASE.md); [B106-C29 · Almacenamiento y distribución de agua potable en hábitats](../programa/clases/B106/B106-C29-almacenamiento-y-distribucion-de-agua-potable-en-habitats/CLASE.md).

### Reserva de crecimiento

- La reserva de crecimiento es un porcentaje según madurez (comercial 5 %, modificado 10 %, nuevo 20 %, en desarrollo 30 %, valores de ejemplo).

💡 **Cómo se explica en la clase [B83-C09](../programa/clases/B83/B83-C09-presupuestos-de-masa/CLASE.md):**
- Distinguir CBE, reserva de crecimiento, MEV y margen.
- 🎯 **Por qué importa:** La masa crece durante el diseño casi siempre; un presupuesto sin reserva se rompe en la revisión crítica. La decisión central: ¿cuánto margen queda frente al límite si cada elemento crece como su madurez sugiere?

📘 **Dónde se aprende** (1 clase): [B83-C09 · Presupuestos de masa](../programa/clases/B83/B83-C09-presupuestos-de-masa/CLASE.md).

### Reserva de desorbitación

- La reserva de desorbitación `r` es un porcentaje del costo para retirar satélites al final.

💡 **Cómo se explica en la clase [B124-C11](../programa/clases/B124/B124-C11-sostenibilidad-economica-de-constelaciones/CLASE.md):**
- Calcular el costo anual de reposición con reserva de desorbitación.
- ⚠️ **Error frecuente:** Calcular el equilibrio sin la reserva de desorbitación. Se corrige con 8.2.
- 🎯 **Por qué importa:** Una constelación puede ser técnicamente exitosa y económicamente inviable si la reposición se come el margen. La decisión central: ¿cuántos suscriptores se necesitan para cubrir la reposición y la operación, y qué tan sensible es eso a la vida útil?

📘 **Dónde se aprende** (1 clase): [B124-C11 · Sostenibilidad económica de constelaciones](../programa/clases/B124/B124-C11-sostenibilidad-economica-de-constelaciones/CLASE.md).

### Reserva de seguridad

- La reserva de seguridad es `z σ √T`.

💡 **Cómo se explica en la clase [B100-C03](../programa/clases/B100/B100-C03-gestion-de-inventarios-y-reposicion-de-suministros/CLASE.md):**
- Calcular el nivel máximo `S` y la reserva de seguridad `z σ √T`.
- Ejercicio 2 · con una pista. Calcula la reserva de seguridad del caso A.
- 🎯 **Por qué importa:** Con una reposición de 10 días basta una reserva pequeña; con una ventana sinódica de Marte la misma demanda exige guardar casi dos años y medio de consumo. La decisión central: ¿hasta qué nivel conviene reponer en cada ventana para que la probabilidad de quedarse sin existencias en el ciclo sea de un 5 %?

📘 **Dónde se aprende** (1 clase): [B100-C03 · Gestión de inventarios y reposición de suministros](../programa/clases/B100/B100-C03-gestion-de-inventarios-y-reposicion-de-suministros/CLASE.md).

### Reserva de sistema

- La reserva de sistema se aplica al total.

💡 **Cómo se explica en la clase [B86-C19](../programa/clases/B86/B86-C19-presupuesto-de-potencia-de-mision/CLASE.md):**
- En el modo nominal en luz, cada subsistema crece según su madurez y el total recibe una reserva de sistema del `10 %`:
- La suma con reserva de sistema es `109,45 W` en luz y `65,23 W` en eclipse, con un residuo de la suma de contribuciones de `0,0e+00 W`.
- 🎯 **Por qué importa:** Un presupuesto es un compromiso de ingeniería: cada subsistema promete una potencia que todavía puede crecer. Las reservas por madurez evitan que el ala quede corta cuando una carga nueva consume más de lo previsto.

📘 **Dónde se aprende** (1 clase): [B86-C19 · Presupuesto de potencia de misión](../programa/clases/B86/B86-C19-presupuesto-de-potencia-de-mision/CLASE.md).

### Residual

- El residual es lo que llega al interior.
- El riesgo inherente es `P × I` sin controles; el residual, con controles.
- Tanque con membrana: almacenamiento sin superficie libre, apto para microgravedad. Residual: concentración de desinfectante que permanece.

💡 **Cómo se explica en la clase [B106-C29](../programa/clases/B106/B106-C29-almacenamiento-y-distribucion-de-agua-potable-en-habitats/CLASE.md):**
- Reponerlo o recircular y medir; a los 90 días el residual es de 0,022 mg/L, bajo el mínimo del modelo.
- El muestreo verifica que el residual y la contaminación se mantienen; el residual da el plazo y el muestreo la confianza.
- 🎯 **Por qué importa:** El agua tratada debe llegar a los puntos de uso con presión y con desinfectante residual suficiente. La decisión central: ¿qué reserva, qué diámetro de línea y cuánto tiempo puede almacenarse el agua antes de perder el residual?

📘 **Dónde se aprende** (3 clases): [B106-C29 · Almacenamiento y distribución de agua potable en hábitats](../programa/clases/B106/B106-C29-almacenamiento-y-distribucion-de-agua-potable-en-habitats/CLASE.md); [B109-C04 · Mitigación de polvo lunar en accesos y hábitats](../programa/clases/B109/B109-C04-mitigacion-de-polvo-lunar-en-accesos-y-habitats/CLASE.md); [B122-C03 · Modelo defensivo de riesgos de infraestructura espacial](../programa/clases/B122/B122-C03-modelo-defensivo-de-riesgos-de-infraestructura-espacial/CLASE.md).

### Residuo

- Un residuo es la diferencia entre el dato y la predicción.
- Un residuo es la diferencia entre un dato y el valor de la recta.
- El residuo es `y − A x`.
- *(y 19 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C17](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md):**
- El residuo cuadrático medio de los logaritmos es 0,0051.
- Que Neptuno tenga el mayor residuo no desprestigia al modelo: puede deberse a la magnitud tabulada (C13), y lo correcto es investigarlo.
- 🎯 **Por qué importa:** Al final de C13, la tercera ley de Kepler daba `T²/a³ = 1` para siete planetas con error menor al 1,5 %, y 0,975 para Neptuno. ¿Falla el modelo con Neptuno?

📘 **Dónde se aprende** (23 clases): [B01-C17 · Construcción de modelos científicos](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md); [B03-C16 · Pendiente e interpretación de gráficos](../programa/clases/B03/B03-C16-pendiente-e-interpretacion-de-graficos/CLASE.md); [B10-C07 · Proyecciones y mínimos cuadrados](../programa/clases/B10/B10-C07-proyecciones-y-minimos-cuadrados/CLASE.md); [B11-C01 · Ecuaciones diferenciales ordinarias](../programa/clases/B11/B11-C01-ecuaciones-diferenciales-ordinarias/CLASE.md); [B12-C10 · Regresión lineal y no lineal](../programa/clases/B12/B12-C10-regresion-lineal-y-no-lineal/CLASE.md); [B12-C19 · Detección de valores atípicos](../programa/clases/B12/B12-C19-deteccion-de-valores-atipicos/CLASE.md) y 17 más.

### Residuo de módulo

- El residuo de módulo es `|(m − o)/s| − B`.

💡 **Cómo se explica en la clase [B87-C08](../programa/clases/B87/B87-C08-calibracion-de-sensores/CLASE.md):**
- El residuo de módulo pasa de `2229 nT` a `98 nT` (el ruido por eje es 100 nT) y el error de dirección de `5,30°` a `0,25°`.
- Medir la mejora en el residuo de módulo y en el error de dirección.
- 🎯 **Por qué importa:** Un magnetómetro sin calibrar con `3000 nT` de sesgo da errores de dirección de varios grados (C05), mayores que los del ruido. La decisión central: ¿qué error sistemático se puede estimar a bordo sin otro sensor, con qué maniobra y cuánto mejora la medida?

📘 **Dónde se aprende** (1 clase): [B87-C08 · Calibración de sensores](../programa/clases/B87/B87-C08-calibracion-de-sensores/CLASE.md).

### Residuo de predicción

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C16](../programa/clases/B47/B47-C16-compresion-de-datos-cientificos/CLASE.md):**
- Una imagen sintética de `128 × 128` píxeles de 16 bit tiene entropía de `8,21 bit` por píxel; los residuos de predicción, `6,94 bit`.
- 🎯 **Por qué importa:** La compresión sin pérdida está acotada por la entropía; la con pérdida cambia fidelidad por volumen. La decisión central: ¿cuántos bits por píxel necesita la imagen y cuánto error se acepta a cambio de menos datos?

📘 **Dónde se aprende** (1 clase): [B47-C16 · Compresión de datos científicos](../programa/clases/B47/B47-C16-compresion-de-datos-cientificos/CLASE.md).

### Residuo de segundo orden

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B43-C17](../programa/clases/B43/B43-C17-alineacion-polar/CLASE.md):**
- El caso de error de altura en el meridiano es nulo en primer orden; la simulación muestra un residuo de segundo orden de `0,0003"/s`.
- 🎯 **Por qué importa:** La alineación polar se corrige midiendo la deriva de una estrella. La decisión central: ¿qué deriva produce un error de acimut o de altura y cómo se invierte para corregirlo?

📘 **Dónde se aprende** (1 clase): [B43-C17 · Alineación polar](../programa/clases/B43/B43-C17-alineacion-polar/CLASE.md).

### Residuo en dex

- El residuo en dex `log₁₀(N_sim/N_ref)`.

💡 **Cómo se explica en la clase [B38-C09](../programa/clases/B38/B38-C09-validacion-de-galaxias-simuladas-frente-a-observaciones/CLASE.md):**
- El residuo máximo es `0,219 dex`, mayor que el umbral de ejemplo de 0,2 dex (el resumen de EAGLE habla de ~0,2 dex entre 10⁸ y 10¹¹ M☉ tras calibrar).
- *Descripción textual:* se ajusta el modelo en una mitad de la referencia y se prueba en la otra con residuos, chi cuadrado y KS.
- 🎯 **Por qué importa:** Una simulación calibrada para coincidir con los datos no queda validada por coincidir con ellos. La decisión central: ¿qué parte del acuerdo es una predicción y qué parte es un ajuste?

📘 **Dónde se aprende** (1 clase): [B38-C09 · Validación de galaxias simuladas frente a observaciones](../programa/clases/B38/B38-C09-validacion-de-galaxias-simuladas-frente-a-observaciones/CLASE.md).

### Residuo normal

- El residuo normal `Aᵀ(s−Ac) = 0`.

💡 **Cómo se explica en la clase [B42-C15](../programa/clases/B42/B42-C15-espejos-deformables/CLASE.md):**
- El script [espejo_deformable.py](espejo_deformable.py) ajusta pantallas a 3 pasos y compara los cocientes con `2^{5/3}` (comprueba el residuo normal a `10⁻⁹` y los cocientes a 25 %).
- 🎯 **Por qué importa:** El número de actuadores fija el error de ajuste que ninguna medición mejora. La decisión central: ¿cuántos actuadores se necesitan para un `r₀` dado?

📘 **Dónde se aprende** (1 clase): [B42-C15 · Espejos deformables](../programa/clases/B42/B42-C15-espejos-deformables/CLASE.md).

### Residuo normalizado

- Un residuo normalizado compara con la varianza del modelo.
- El residuo normalizado `z = r/σ`.

💡 **Cómo se explica en la clase [B51-C07](../programa/clases/B51/B51-C07-evaluacion-de-residuos-y-diagnostico-de-calidad-de-calibracion/CLASE.md):**
- *Descripción textual:* los residuos normalizados resumen en un número y en una forma la calidad del modelo y de las ganancias.
- 🎯 **Por qué importa:** Una calibración mala puede dar una imagen bonita. La decisión central: ¿qué valor de χ² reducido y qué forma de los residuos indican que el modelo es suficiente?

📘 **Dónde se aprende** (2 clases): [B45-C18 · Extracción de espectros](../programa/clases/B45/B45-C18-extraccion-de-espectros/CLASE.md); [B51-C07 · Evaluación de residuos y diagnóstico de calidad de calibración](../programa/clases/B51/B51-C07-evaluacion-de-residuos-y-diagnostico-de-calidad-de-calibracion/CLASE.md).

### Residuo seco

- El residuo seco es el sólido sin agua.

💡 **Cómo se explica en la clase [B59-C16](../programa/clases/B59/B59-C16-desechos-y-reciclaje/CLASE.md):**
- *Descripción textual:* el residuo húmedo se seca; el seco se oxida a CO₂, agua y N₂; el agua de humedad y la de la reacción se recuperan.
- Un residuo seco sintético `CH₁,₈O₀,₆N₀,₁` (`24,8253 g` por átomo de C).
- 🎯 **Por qué importa:** Los residuos son una fuente de agua y de dióxido de carbono, pero también consumen oxígeno. La decisión central: ¿cuánto oxígeno cuesta cerrar el residuo y cuánta agua se recupera?

📘 **Dónde se aprende** (1 clase): [B59-C16 · Desechos y reciclaje](../programa/clases/B59/B59-C16-desechos-y-reciclaje/CLASE.md).

### Residuos

- Los residuos son observado menos calculado.

💡 **Cómo se explica en la clase [B58-C07](../programa/clases/B58/B58-C07-determinacion-de-orbitas/CLASE.md):**
- El residuo es observado menos calculado, con la longitud multiplicada por `cos b`.
- *Descripción textual:* los elementos generan posiciones; los residuos frente a las observaciones y el jacobiano dan un paso de corrección; el ciclo se repite hasta que `χ²` deja de bajar.
- 🎯 **Por qué importa:** Una órbita ajustada es el producto central de la defensa planetaria: de ella salen las predicciones y las probabilidades. La decisión central: ¿cuántas observaciones y qué arco hacen falta para que la órbita sea fiable, y cómo se sabe que el ajuste es bueno?

📘 **Dónde se aprende** (1 clase): [B58-C07 · Determinación de órbitas](../programa/clases/B58/B58-C07-determinacion-de-orbitas/CLASE.md).

### Resiliencia

- La rigidez específica es `E/ρ`; la resistencia específica, `σ₀,₂/ρ`; la resiliencia, `σ₀,₂²/(2E)`.
- La resiliencia es la capacidad de seguir operando degradado.

💡 **Cómo se explica en la clase [B84-C02](../programa/clases/B84/B84-C02-propiedades-de-aleaciones/CLASE.md):**
- Calcular rigidez específica, resistencia específica y energía de resiliencia.
- Ejercicio 4 · autónomo Resiliencia del Inconel 718.
- 🎯 **Por qué importa:** Dos aleaciones con la misma rigidez específica pueden diferir en 7 veces su resistencia específica (Ti frente a acero 304); elegir por una sola propiedad lleva a un mal diseño. La decisión central: ¿qué aleación es mejor según el índice que importa a la pieza, y qué significa el límite elástico al 0,2 %?

📘 **Dónde se aprende** (2 clases): [B84-C02 · Propiedades de aleaciones](../programa/clases/B84/B84-C02-propiedades-de-aleaciones/CLASE.md); [B119-C15 · Interferencias y resiliencia de comunicaciones](../programa/clases/B119/B119-C15-interferencias-y-resiliencia-de-comunicaciones/CLASE.md).

### Resistencia

- La resistencia `R` (ohmios, Ω) mide la oposición al paso de corriente; la ley de Ohm dice `V = I R` para un conductor óhmico.
- El régimen de gravedad es aquel en que el peso del material limita el crecimiento; el de resistencia, aquel en que lo limita la cohesión.
- La resistencia da `τ_a = ½ ρ v² C_d A (cp−cg)`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C16](../programa/clases/B05/B05-C16-corriente-y-circuitos-elementales/CLASE.md):**
- Si la resistencia se duplica con la misma tensión, la corriente y la potencia se reducen a la mitad.
- La fuente entrega `P = V I₁ = 16,941 W`; las resistencias disipan `I₁² R₁ + I₂² R₂ + I₃² R₃ + I₄² R₄ = 16,941 W`.
- 🎯 **Por qué importa:** Un satélite recibe energía del Sol mediante paneles, la guarda en baterías y la reparte a equipos; si el cálculo está mal, la nave se apaga en el eclipse. La pregunta motivadora es: ¿cómo calcular corrientes, tensiones y potencias en una red de componentes y cuánta energía debe guardarse para pasar un eclipse?

📘 **Dónde se aprende** (4 clases): [B05-C16 · Corriente y circuitos elementales](../programa/clases/B05/B05-C16-corriente-y-circuitos-elementales/CLASE.md); [B61-C01 · Dinámica de eyección y escalado de cráteres](../programa/clases/B61/B61-C01-dinamica-de-eyeccion-y-escalado-de-crateres/CLASE.md); [B87-C18 · Estabilidad ante perturbaciones](../programa/clases/B87/B87-C18-estabilidad-ante-perturbaciones/CLASE.md); [B119-C24 · Límites legales y de seguridad de la experimentación educativa](../programa/clases/B119/B119-C24-limites-legales-y-de-seguridad-de-la-experimentacion-educativa/CLASE.md).

### Resistencia a la fluencia

- La resistencia a la fluencia `τ` es el esfuerzo por debajo del cual el material no se deforma.

💡 **Cómo se explica en la clase [B70-C02](../programa/clases/B70/B70-C02-domos-volcanicos-y-vulcanismo-evolucionado/CLASE.md):**
- ⚠️ **Error frecuente:** Confundir resistencia a la fluencia con viscosidad. Se corrige en la sección 6.
- 🎯 **Por qué importa:** Una colina empinada de lava puede tener una altura que solo depende del material y de `g`. La decisión central: ¿qué altura puede alcanzar un domo de resistencia dada y qué cambiaría en otro mundo?

📘 **Dónde se aprende** (1 clase): [B70-C02 · Domos volcánicos y vulcanismo evolucionado](../programa/clases/B70/B70-C02-domos-volcanicos-y-vulcanismo-evolucionado/CLASE.md).

### Resistencia a la rodadura

- La resistencia a la rodadura es `F_r = Crr · m g cos θ`.
- La resistencia a la rodadura `c_r` es la fuerza por unidad de carga normal que se pierde en hundir y comprimir.

🎯 **Por qué importa (clase B100-C05):** Mover una tonelada un kilómetro cuesta energía, y esa energía depende de la gravedad, del suelo y de la pendiente. La decisión central: ¿cuánta carga y qué ruta permiten llegar con la batería disponible, y cuánto cambia el costo entre la Luna y Marte?

📘 **Dónde se aprende** (2 clases): [B100-C05 · Transporte de carga sobre superficie planetaria](../programa/clases/B100/B100-C05-transporte-de-carga-sobre-superficie-planetaria/CLASE.md); [B102-C07 · Simulación de movilidad sobre pendientes y terreno](../programa/clases/B102/B102-C07-simulacion-de-movilidad-sobre-pendientes-y-terreno/CLASE.md).

### Resistencia aerodinámica r_a

- La resistencia aerodinámica `r_a` y la superficial `r_s` controlan el paso del vapor.

🎯 **Por qué importa (clase B115-C06):** El cultivo es el mayor flujo de agua de un hábitat con plantas. La decisión central: ¿cuánta agua transpira el cultivo, cuánta se recupera y cuánta hay que reponer, y con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B115-C06 · Balance de agua y evapotranspiración en cultivos](../programa/clases/B115/B115-C06-balance-de-agua-y-evapotranspiracion-en-cultivos/CLASE.md).

### Resistencia característica

- `m` es el módulo de Weibull (menor `m` = más dispersión) y `σ₀` la resistencia característica.

🎯 **Por qué importa (clase B84-C04):** Un metal avisa antes de romper; una cerámica no. Diseñar con la resistencia media de una probeta pequeña sobreestima la de una pieza grande en 40 %.

📘 **Dónde se aprende** (1 clase): [B84-C04 · Cerámicos y polímeros espaciales](../programa/clases/B84/B84-C04-ceramicos-y-polimeros-espaciales/CLASE.md).

### Resistencia de cizalla

- La resistencia de cizalla de Mohr–Coulomb es `τ_máx = c + σ tan φ`; con el desplazamiento de cizalla `j` queda `τ = τ_máx (1 − e^(−j/K))`.

🎯 **Por qué importa (clase B102-C02):** La tracción de un rover en regolito no sale de un coeficiente de rozamiento único. La decisión central: ¿cuánta fuerza neta de empuje queda para tirar del vehículo, una vez descontada la resistencia que crea el propio hundimiento, y cómo depende del patinaje y de la gravedad?

📘 **Dónde se aprende** (1 clase): [B102-C02 · Terramecánica: tracción y hundimiento en suelos sueltos](../programa/clases/B102/B102-C02-terramecanica-traccion-y-hundimiento-en-suelos-sueltos/CLASE.md).

### Resistencia de fuga

- Carga triboeléctrica: carga generada por contacto y separación de materiales. Resistencia de fuga: camino resistivo que permite disipar la carga lentamente.

💡 **Cómo se explica en la clase [B90-C03](../programa/clases/B90/B90-C03-proteccion-frente-a-esd/CLASE.md):**
- Con una resistencia de fuga de 1 MΩ la corriente pico de la tensión corporal cae a 0,67 mA.
- Descripción larga: la corriente salta a `V/R` y decae exponencialmente; con mayor resistencia de fuga el pico baja y la cola se alarga.
- ⚠️ **Error frecuente:** Usar 0 Ω hacia tierra. Limita la corriente con resistencia de fuga (8.4)
- 🎯 **Por qué importa:** Un componente electrónico puede quedar con una falla latente tras una descarga que nadie sintió: una persona percibe una chispa solo por encima de unos miles de voltios (orden de magnitud no consultado), por encima de lo que puede dañar a un componente sensible.

📘 **Dónde se aprende** (1 clase): [B90-C03 · Protección frente a ESD](../programa/clases/B90/B90-C03-proteccion-frente-a-esd/CLASE.md).

### Resistencia de radiación

- La resistencia de radiación es `R = 2P_rad/I²`.

💡 **Cómo se explica en la clase [B49-C01](../programa/clases/B49/B49-C01-antenas-de-hilo-dipolo-monopolo-e-impedancia-de-radiacion/CLASE.md):**
- La resistencia de radiación crece con el cuadrado de la longitud hasta media onda.
- *Descripción textual:* la corriente sinusoidal fija el campo lejano; su integral da la potencia y la resistencia de radiación, que una serie independiente verifica.
- 🎯 **Por qué importa:** Sin la resistencia de radiación no se sabe qué carga ve la línea ni cuánta potencia se irradia. La decisión central: ¿de qué longitud hacer el hilo y qué impedancia presentará a la línea?

📘 **Dónde se aprende** (1 clase): [B49-C01 · Antenas de hilo: dipolo, monopolo e impedancia de radiación](../programa/clases/B49/B49-C01-antenas-de-hilo-dipolo-monopolo-e-impedancia-de-radiacion/CLASE.md).

### Resistencia efectiva

- La resistencia efectiva `Y` es la cohesión que sostiene la pared.

🎯 **Por qué importa (clase B61-C03):** Sin la transición simple–compleja no se puede interpretar la forma de un cráter grande ni comparar cuerpos. La decisión central: ¿a qué diámetro cambia la morfología y cómo depende de la gravedad?

📘 **Dónde se aprende** (1 clase): [B61-C03 · Cráteres complejos: colapso, picos centrales y terrazas](../programa/clases/B61/B61-C03-crateres-complejos-colapso-picos-centrales-y-terrazas/CLASE.md).

### Resistencia en serie

- La resistencia en serie `R_s` reduce la tensión útil.

💡 **Cómo se explica en la clase [B86-C02](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md):**
- *Descripción textual:* la luz fija `I_ph`; el diodo y la resistencia en serie dan la curva `I(V)`; de ella salen los extremos, el punto de máxima potencia, el factor de llenado y la eficiencia; la temperatura modifica el diodo.
- Escribir la ecuación de diodo único con resistencia en serie y resolverla con Newton.
- 🎯 **Por qué importa:** La potencia de una celda no es un número fijo: depende de la tensión a la que se la haga trabajar y de su temperatura. Elegir mal el punto de operación o ignorar la temperatura del ala cambia la potencia entregada.

📘 **Dónde se aprende** (1 clase): [B86-C02 · Celdas solares](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md).

### Resistencia específica

- La rigidez específica es `E/ρ`; la resistencia específica, `σ₀,₂/ρ`; la resiliencia, `σ₀,₂²/(2E)`.

💡 **Cómo se explica en la clase [B84-C02](../programa/clases/B84/B84-C02-propiedades-de-aleaciones/CLASE.md):**
- Cambia la resistencia específica (Ti gana) y el índice de panel (Al gana).
- Descripción larga: la rigidez específica es casi igual en las cuatro aleaciones; la resistencia específica del titanio es casi el doble que la del aluminio.
- 🎯 **Por qué importa:** Dos aleaciones con la misma rigidez específica pueden diferir en 7 veces su resistencia específica (Ti frente a acero 304); elegir por una sola propiedad lleva a un mal diseño. La decisión central: ¿qué aleación es mejor según el índice que importa a la pieza, y qué significa el límite elástico al 0,2 %?

📘 **Dónde se aprende** (1 clase): [B84-C02 · Propiedades de aleaciones](../programa/clases/B84/B84-C02-propiedades-de-aleaciones/CLASE.md).

### Resistencia o circuito que reduce ese pico

- Limitador: resistencia o circuito que reduce ese pico. Presupuesto de potencia: suma de las potencias de las cargas con márgenes.

🎯 **Por qué importa (clase B90-C07):** Una carga de potencia constante pide más corriente cuando baja la tensión, de modo que un arnés largo o delgado puede hundir el bus justo cuando más se necesita. Y al conectar una carga con capacitor, la corriente inicial puede ser decenas de amperios.

📘 **Dónde se aprende** (1 clase): [B90-C07 · Integración eléctrica de buses](../programa/clases/B90/B90-C07-integracion-electrica-de-buses/CLASE.md).

### Resistencia por compactación

- El empuje `H` es la integral de `τ` en el arco; la resistencia por compactación `Rc = b k z₀^(n+1)/(n+1)` es el trabajo de hundir la rueda; el tiro de barra es `DP = H − Rc`.

💡 **Cómo se explica en la clase [B102-C02](../programa/clases/B102/B102-C02-terramecanica-traccion-y-hundimiento-en-suelos-sueltos/CLASE.md):**
- La resistencia por compactación relativa `Rc/W` es `0,261` en la Tierra, `0,175` en Marte y `0,126` en la Luna: se hunde menos y gasta menos en hundirse.
- El peso por rueda escala con `g`, el hundimiento y la compactación no lo hacen proporcionalmente: el cociente `DP/W` apenas cambia (`0,27`–`0,28`), pero la resistencia relativa `Rc/W` cae con `g`.
- ⚠️ **Error frecuente:** Olvidar la resistencia por compactación. Se corrige con 8.2 y 8.3
- 🎯 **Por qué importa:** La tracción de un rover en regolito no sale de un coeficiente de rozamiento único. La decisión central: ¿cuánta fuerza neta de empuje queda para tirar del vehículo, una vez descontada la resistencia que crea el propio hundimiento, y cómo depende del patinaje y de la gravedad?

📘 **Dónde se aprende** (1 clase): [B102-C02 · Terramecánica: tracción y hundimiento en suelos sueltos](../programa/clases/B102/B102-C02-terramecanica-traccion-y-hundimiento-en-suelos-sueltos/CLASE.md).

### Resistencia térmica

- La resistencia térmica de una barra es `R = L/(kA)`; la de una unión, `R_c = 1/(h_c A)`.

🎯 **Por qué importa (clase B85-C02):** El calor generado por un equipo debe llegar al radiador por algún camino; una unión mal conductora puede ser la resistencia dominante. La decisión central: ¿qué parte del camino de conducción limita el flujo y qué cambio lo mejora más?

📘 **Dónde se aprende** (1 clase): [B85-C02 · Conducción térmica en estructuras](../programa/clases/B85/B85-C02-conduccion-termica-en-estructuras/CLASE.md).

### Resistencia vascular sistémica

- La resistencia vascular sistémica `RVS` (mmHg·min/L) es la oposición al flujo.

🎯 **Por qué importa (clase B117-C03):** Ninguna clase anterior simula una emergencia cardiovascular. La decisión central: ¿qué señales de un modelo simple delatan un problema de circulación y cuáles lo esconden?

📘 **Dónde se aprende** (1 clase): [B117-C03 · Emergencia cardiovascular simulada](../programa/clases/B117/B117-C03-emergencia-cardiovascular-simulada/CLASE.md).

### Resistividad

- La resistividad `η` rompe la idealidad.

💡 **Cómo se explica en la clase [B35-C07](../programa/clases/B35/B35-C07-congelamiento-del-flujo-magnetico-y-conservacion-en-mhd-ideal/CLASE.md):**
- Las líneas de campo son hilos cosidos en una tela que es el plasma: al estirar o comprimir la tela, los hilos se mueven con ella; con resistividad, los hilos se disuelven poco a poco.
- R["resistividad η"] --> D["difusión: σ² = σ₀² + 2ηt"]
- 🎯 **Por qué importa:** La conservación del flujo explica por qué el campo se amplifica al comprimirse y por qué la reconexión exige romper la idealidad. La decisión central: ¿cuándo el campo se mueve con el plasma y cuándo se difunde?

📘 **Dónde se aprende** (1 clase): [B35-C07 · Congelamiento del flujo magnético y conservación en MHD ideal](../programa/clases/B35/B35-C07-congelamiento-del-flujo-magnetico-y-conservacion-en-mhd-ideal/CLASE.md).

### Resolución

- La resolución es el cambio más pequeño que el instrumento distingue.
- La resolución `σ/E`.
- La resolución `R = λ/Δλ`, con `Δλ` la FWHM.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B31-C14](../programa/clases/B31/B31-C14-detectores-de-particulas/CLASE.md):**
- Un protón necesita casi 500 MeV para radiar y un electrón apenas 0,26 MeV; la resolución mejora con la energía hasta saturarse en `b`.
- *Descripción textual:* el índice fija el umbral, el ángulo y el rendimiento; los parámetros del calorímetro fijan la resolución, que se comprueba con Monte Carlo.
- 🎯 **Por qué importa:** Interpretar una señal exige saber qué partículas la producen y con qué precisión se mide su energía. La decisión central: ¿qué umbral y qué resolución tiene un detector?

📘 **Dónde se aprende** (5 clases): [B01-C06 · Preguntas investigables en astronomía](../programa/clases/B01/B01-C06-preguntas-investigables-en-astronomia/CLASE.md); [B31-C14 · Detectores de partículas](../programa/clases/B31/B31-C14-detectores-de-particulas/CLASE.md); [B45-C07 · Resolución espectral](../programa/clases/B45/B45-C07-resolucion-espectral/CLASE.md); [B46-C16 · Síntesis de apertura](../programa/clases/B46/B46-C16-sintesis-de-apertura/CLASE.md); [B90-C23 · Instrumentación y adquisición de datos en ensayos](../programa/clases/B90/B90-C23-instrumentacion-y-adquisicion-de-datos-en-ensayos/CLASE.md).

### Resolución angular

- La resolución angular es el menor ángulo entre dos puntos que se ven separados.

💡 **Cómo se explica en la clase [B01-C10](../programa/clases/B01/B01-C10-limitaciones-de-los-sentidos-humanos/CLASE.md):**
- Ejercicio 6. Con la Luna de 1 865″ de diámetro angular, ¿cuántos «elementos de resolución» de 19,8″ caben en su diámetro?
- Ejercicio 12 · integrador. Elabora tu comparación sentido–instrumento: elige un objeto, tres instrumentos (el ojo y dos más) y calcula para cada uno rango, luz relativa, resolución angular y detalle lineal; indica qué sigue sin verse y qué datos son hipotéticos o publicados.
- 🎯 **Por qué importa:** Si el ojo bastara, no habría observatorios. La luz visible es una franja pequeña del espectro electromagnético (S1, S2); además, tu pupila recoge poca luz, separa detalles hasta cierto tamaño y puede engañarte.

📘 **Dónde se aprende** (1 clase): [B01-C10 · Limitaciones de los sentidos humanos](../programa/clases/B01/B01-C10-limitaciones-de-los-sentidos-humanos/CLASE.md).

### Resolución angular de medida

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C06):** Cada proceso (Compton, pares) domina a una energía distinta y fija el tipo de instrumento. La decisión central: ¿qué proceso usa el detector y con qué incertidumbre angular reconstruye la dirección?

📘 **Dónde se aprende** (1 clase): [B47-C06 · Instrumentos de rayos gamma](../programa/clases/B47/B47-C06-instrumentos-de-rayos-gamma/CLASE.md).

### Resolución axial

- La resolución axial es la separación mínima distinguible a lo largo del haz, `≈ N·λ/2` con `N` ciclos por pulso.

💡 **Cómo se explica en la clase [B116-C06](../programa/clases/B116/B116-C06-dispositivos-biomedicos-portatiles-ultrasonido-diagnostico/CLASE.md):**
- Con `N = 2` ciclos por pulso la resolución axial es `λ`.
- Un ecógrafo de 3,5 MHz alcanza 17,1 cm de profundidad máxima con el rango dinámico de 60 dB y la atenuación ilustrativa de 0,5 dB/(cm·MHz), con una resolución axial de 0,44 mm; uno de 7,5 MHz resuelve 0,205 mm pero solo llega a 8,0 cm: a 10 cm perdería 75 dB.
- 🎯 **Por qué importa:** Un equipo no es solo su ficha técnica: lo que ve depende de la frecuencia elegida, quién lo maneja, cuánto entrena y qué retardo tiene el apoyo experto. Y una prueba con buenos números de sensibilidad y especificidad puede dar mayoría de falsos positivos si la condición es rara.

📘 **Dónde se aprende** (1 clase): [B116-C06 · Dispositivos biomédicos portátiles (ultrasonido, diagnóstico)](../programa/clases/B116/B116-C06-dispositivos-biomedicos-portatiles-ultrasonido-diagnostico/CLASE.md).

### Resolución de masa

- La resolución de masa `m/Δm`.

💡 **Cómo se explica en la clase [B47-C08](../programa/clases/B47/B47-C08-espectrometros-de-masas-orbitales/CLASE.md):**
- Ejercicio 12. Integrador. Elabora tu *ficha del espectrómetro de masas*: tiempos, resolución exigida y lograda, y límites.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha del espectrómetro de masas*: tiempos, resolución exigida y lograda, y límites.
- 🎯 **Por qué importa:** La resolución de masa decide qué especies se separan. La decisión central: ¿qué tiempo de vuelo, qué dispersión y qué resolución permiten distinguir dos iones casi isobáricos?

📘 **Dónde se aprende** (1 clase): [B47-C08 · Espectrómetros de masas orbitales](../programa/clases/B47/B47-C08-espectrometros-de-masas-orbitales/CLASE.md).

### Resolución efectiva

- La resolución efectiva es el mayor entre GSD y disco de Airy proyectado (regla simplificada).

💡 **Cómo se explica en la clase [B121-C02](../programa/clases/B121/B121-C02-licenciamiento-de-actividades-de-teledeteccion/CLASE.md):**
- *Descripción textual:* el sensor define GSD y difracción, el mayor de los dos es la resolución efectiva, que cae en un tramo; el GSD se comprueba por otra vía.
- Calcular el límite de difracción `1,22·λ·h/D` y la resolución efectiva.
- 🎯 **Por qué importa:** Ninguna clase anterior trata la regulación de la teledetección. La decisión central: ¿en qué tramo de resolución cae un sensor y qué licencia o condiciones podría implicar?

📘 **Dónde se aprende** (1 clase): [B121-C02 · Licenciamiento de actividades de teledetección](../programa/clases/B121/B121-C02-licenciamiento-de-actividades-de-teledeteccion/CLASE.md).

### Resolución en distancia

- La resolución en distancia `c/(2B_tx)` depende del ancho de banda transmitido.

💡 **Cómo se explica en la clase [B58-C12](../programa/clases/B58/B58-C12-radar-planetario/CLASE.md):**
- T["ancho de banda"] --> RES["resolución en distancia"]
- *Descripción textual:* la rotación y la longitud de onda fijan el ancho Doppler; el ancho de banda fija la resolución en distancia; el tamaño y la distancia fijan la señal.
- ⚠️ **Error frecuente:** Confundir resolución en distancia y Doppler. Se corrige con 8.3.
- 🎯 **Por qué importa:** El radar aporta lo que la fotometría no da: tamaño directo (sin albedo) y distancias de precisión que reducen la incertidumbre orbital. La decisión central: ¿qué resolución y qué señal se obtienen de un objeto de cierto tamaño a cierta distancia?

📘 **Dónde se aprende** (1 clase): [B58-C12 · Radar planetario](../programa/clases/B58/B58-C12-radar-planetario/CLASE.md).

### Resolución en DM

- La resolución en DM depende de la anchura del pulso.

💡 **Cómo se explica en la clase [B29-C17](../programa/clases/B29/B29-C17-fenomenos-transitorios-rapidos/CLASE.md):**
- Para un pulso de `1,5 ms` en la banda completa, la resolución en `DM` es `1,45 pc/cm³`.
- Un pulso real sería más ancho por la dispersión intra-canal, lo que reduce la resolución.
- ⚠️ **Error frecuente:** Esperar resolución mejor que la del pulso. Se corrige con el ejercicio 3.
- 🎯 **Por qué importa:** La medida de dispersión informa de la distancia a la fuente y de la materia que atravesó. Sin desdispersión, un pulso breve se pierde entre canales.

📘 **Dónde se aprende** (1 clase): [B29-C17 · Fenómenos transitorios rápidos](../programa/clases/B29/B29-C17-fenomenos-transitorios-rapidos/CLASE.md).

### Resolución en frecuencia

- La resolución en frecuencia es `Δf = 1/(N Δt)`.
- La resolución en frecuencia de una serie de duración `T` es `1/T`.
- La resolución en frecuencia es `1/T`.

💡 **Cómo se explica en la clase [B24-C14](../programa/clases/B24/B24-C14-asterosismologia-inicial/CLASE.md):**
- Definir modo acústico, modo de gravedad, separación grande y resolución en frecuencia.
- Calcular la resolución en frecuencia que da una serie temporal.
- 🎯 **Por qué importa:** La asterosismología es la única manera de «ver» el interior de estrellas lejanas: da densidad media, masa y radio con una precisión que la fotometría y la espectroscopía no alcanzan, y distingue si una gigante quema hidrógeno en capa o helio en el núcleo.

📘 **Dónde se aprende** (3 clases): [B15-C04 · Transformada de Fourier](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md); [B24-C14 · Asterosismología inicial](../programa/clases/B24/B24-C14-asterosismologia-inicial/CLASE.md); [B30-C03 · Ciclo de actividad solar](../programa/clases/B30/B30-C03-ciclo-de-actividad-solar/CLASE.md).

### Resolución en rango

- La resolución en rango es `c/(2B√ε_r)`.

💡 **Cómo se explica en la clase [B53-C24](../programa/clases/B53/B53-C24-sondeo-radar-de-penetracion-de-hielo/CLASE.md):**
- Con un ancho de banda de `10 MHz` la resolución en rango es `8,45 m`.
- 🎯 **Por qué importa:** Un eco sin escala de profundidad no dice nada. La decisión central: ¿a qué profundidad está una interfaz según su retardo y qué separación mínima permite distinguir dos interfaces?

📘 **Dónde se aprende** (1 clase): [B53-C24 · Sondeo radar de penetración de hielo](../programa/clases/B53/B53-C24-sondeo-radar-de-penetracion-de-hielo/CLASE.md).

### Resolución en velocidad

- La resolución en velocidad es `c/R`.

💡 **Cómo se explica en la clase [B45-C07](../programa/clases/B45/B45-C07-resolucion-espectral/CLASE.md):**
- Ejercicio 3 · casi autónomo. Resolución en velocidad con `R = 3000`.
- 🎯 **Por qué importa:** La resolución limita qué se puede medir (separar un doblete, medir una velocidad). La decisión central: ¿qué `R` se necesita para el objetivo científico y cómo se mide?

📘 **Dónde se aprende** (1 clase): [B45-C07 · Resolución espectral](../programa/clases/B45/B45-C07-resolucion-espectral/CLASE.md).

### Resolución espacial

- La resolución espacial es el tamaño de píxel (aquí 15 m y 30 m).

🎯 **Por qué importa (clase B15-C24):** Un mapa de cobertura exige distinguir objetos pequeños (caminos, parcelas) y también su firma espectral (si son vegetación o suelo). Ninguna imagen entrega ambas cosas a la vez.

📘 **Dónde se aprende** (1 clase): [B15-C24 · Fusión de imágenes de distintos sensores](../programa/clases/B15/B15-C24-fusion-de-imagenes-de-distintos-sensores/CLASE.md).

### Resolución espectral

- La resolución espectral es el ancho de las bandas y su número.
- La resolución espectral es la separación mínima entre dos frecuencias distinguibles, `1/T` Hz o `60/T` lpm.

💡 **Cómo se explica en la clase [B57-C03](../programa/clases/B57/B57-C03-resolucion-radiometrica-y-espectral/CLASE.md):**
- La evidencia es la ficha de resoluciones radiométrica y espectral del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de resoluciones radiométrica y espectral*: la tabla de bits, niveles y SQNR, el paso de cuantización en unidades físicas y el promedio de banda para un espectro lineal y uno con escalón.
- 🎯 **Por qué importa:** Dos sensores con el mismo píxel pueden dar información muy distinta si uno distingue 256 niveles y otro 65.536, o si una banda es ancha y otra estrecha. La decisión central: ¿cuántos bits y qué ancho de banda hacen falta para ver el cambio que me interesa?

📘 **Dónde se aprende** (2 clases): [B57-C03 · Resolución radiométrica y espectral](../programa/clases/B57/B57-C03-resolucion-radiometrica-y-espectral/CLASE.md); [B116-C01 · Sensores fisiológicos y wearables para vuelo](../programa/clases/B116/B116-C01-sensores-fisiologicos-y-wearables-para-vuelo/CLASE.md).

### Resolución limitada por difracción

- La resolución limitada por difracción `1,028 λ/D`.

🎯 **Por qué importa (clase B47-C01):** Un instrumento orbital cuesta mucho más que uno en tierra; la decisión de ir al espacio debe poder defenderse con números. La decisión central: ¿qué parte del rendimiento se pierde por la atmósfera y cuánto cuesta recuperarla?

📘 **Dónde se aprende** (1 clase): [B47-C01 · Ventajas de observación fuera de atmósfera](../programa/clases/B47/B47-C01-ventajas-de-observacion-fuera-de-atmosfera/CLASE.md).

### Resolución lineal

- La resolución lineal es `h·IFOV`.

💡 **Cómo se explica en la clase [B75-C17](../programa/clases/B75/B75-C17-oportunidades-cientificas-de-sobrevuelo/CLASE.md):**
- Calcular la resolución lineal `h·IFOV` y el volumen de datos.
- 🎯 **Por qué importa:** Cada metro de altitud cuesta resolución, y cada segundo de ventana cuesta datos. La decisión central: ¿qué altitud de máxima aproximación equilibra resolución, cobertura y volumen de datos en un sobrevuelo?

📘 **Dónde se aprende** (1 clase): [B75-C17 · Oportunidades científicas de sobrevuelo](../programa/clases/B75/B75-C17-oportunidades-cientificas-de-sobrevuelo/CLASE.md).

### Resolución temporal

- La resolución temporal es el intervalo entre observaciones del mismo punto; el ciclo de repetición es el tiempo tras el cual la traza se repite.

💡 **Cómo se explica en la clase [B57-C02](../programa/clases/B57/B57-C02-resolucion-espacial-y-temporal/CLASE.md):**
- La evidencia es la ficha de resoluciones espacial y temporal del ejercicio 12 (sección 20).
- Resolución temporal: puede pasar sin ser observada; hace falta una constelación o un sensor con otra órbita (clase C23).
- 🎯 **Por qué importa:** Un satélite con píxeles de 30 m no ve una casa y uno que vuelve cada 16 días no ve una tormenta. La decisión central: ¿qué tamaño de píxel, qué ancho de barrido y qué ciclo de repetición necesita el fenómeno que quiero estudiar?

📘 **Dónde se aprende** (1 clase): [B57-C02 · Resolución espacial y temporal](../programa/clases/B57/B57-C02-resolucion-espacial-y-temporal/CLASE.md).

### Resolutor

- Un resolutor elige versiones de todas las dependencias (directas e indirectas) que sean compatibles entre sí.

🎯 **Por qué importa (clase B14-C12):** Tu análisis dio un período de 5553,624562 s en 2026. Un colega lo ejecuta con otra versión de SciPy y obtiene un cierre distinto; otro usa Python más antiguo y falla al importar. «En mi máquina funciona» no es un resultado científico.

📘 **Dónde se aprende** (1 clase): [B14-C12 · Ejecución reproducible con uv](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md).

### Resolver

- Una ecuación es una igualdad con una o más incógnitas. Resolver o despejar una incógnita es aislarla en un lado.
- Un archivo de bloqueo (`uv.lock`) registra las versiones exactas resueltas de todas las dependencias, incluidas las indirectas, y es multiplataforma (S3). Resolver es calcular un conjunto de versiones compatibles entre sí.

💡 **Cómo se explica en la clase [B03-C14](../programa/clases/B03/B03-C14-despeje-de-ecuaciones-elementales/CLASE.md):**
- Sustituir primero y resolver con números es más rápido en un caso, pero pierde la fórmula general y mezcla redondeos.
- 🎯 **Por qué importa:** La fórmula de la velocidad de escape, `v = √(2GM/R)`, aparece en las fichas de la NASA como un número (11,186 km/s). Pero un ingeniero puede necesitar lo contrario: dado `v`, ¿cuál es el radio?

📘 **Dónde se aprende** (2 clases): [B03-C14 · Despeje de ecuaciones elementales](../programa/clases/B03/B03-C14-despeje-de-ecuaciones-elementales/CLASE.md); [B07-C13 · Entornos y dependencias con uv](../programa/clases/B07/B07-C13-entornos-y-dependencias-con-uv/CLASE.md).

### Resolverla

- Una ecuación es una igualdad con una incógnita; resolverla es hallar los valores que la cumplen.

🎯 **Por qué importa (clase B04-C02):** Una sonda desciende hacia la Luna; un instrumento cae desde una mesa de trabajo; una señal de radio viaja hasta un espejo y vuelve. En cada caso hay un número que no conoces (un tiempo, una distancia) y una relación que lo liga a otros que sí conoces.

📘 **Dónde se aprende** (1 clase): [B04-C02 · Ecuaciones lineales y cuadráticas](../programa/clases/B04/B04-C02-ecuaciones-lineales-y-cuadraticas/CLASE.md).

### Resonancia

- La resonancia es la respuesta máxima cuando la frecuencia de una fuerza periódica coincide con `ω₀`.
- La resonancia: `r ≈ 1`.
- Una resonancia `p:q` con una luna de periodo `P` ubica una partícula de periodo `P q/p` en `r = a_luna (q/p)^{2/3}`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C11](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md):**
- En resonancia (`r = 1`) vale `1/(2ζ)`: `50` con `ζ = 0,01`, `10` con `ζ = 0,05` y `2,5` con `ζ = 0,2`.
- D --> G["Con fuerza periódica en ω0: resonancia"]
- ⚠️ **Error frecuente:** Ignorar el amortiguamiento al hablar de resonancia. Ejercicio 7.
- 🎯 **Por qué importa:** Una estructura que vibra puede amplificar una excitación hasta romperse; un reloj de péndulo mide tiempo; un átomo vibra en un cristal. La pregunta motivadora es: ¿qué determina la frecuencia a la que algo oscila y qué pasa cuando se le empuja a esa frecuencia?

📘 **Dónde se aprende** (4 clases): [B05-C11 · Movimiento oscilatorio](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md); [B47-C11 · Aislamiento vibracional](../programa/clases/B47/B47-C11-aislamiento-vibracional/CLASE.md); [B73-C16 · Dinámica de anillos](../programa/clases/B73/B73-C16-dinamica-de-anillos/CLASE.md); [B90-C09 · Ensayos de vibración](../programa/clases/B90/B90-C09-ensayos-de-vibracion/CLASE.md).

### Resonancia 9:2

- Una resonancia 9:2 con el mes sinódico significa `T = 2 P_sin/9`.

💡 **Cómo se explica en la clase [B76-C02](../programa/clases/B76/B76-C02-escalas-sinodicas-de-referencia/CLASE.md):**
- Comprobar la resonancia 9:2 contra el periodo publicado de una NRHO.
- Ejercicio 2 · con una pista. Calcula el periodo de una resonancia 9:2.
- 🎯 **Por qué importa:** Un equipo que mezcla el mes sideral con el sinódico desplaza una resonancia en medio día y pierde una geometría de eclipses. La decisión central: ¿qué escala de tiempo corresponde a cada pregunta y cómo se convierte sin error?

📘 **Dónde se aprende** (1 clase): [B76-C02 · Escalas sinódicas de referencia](../programa/clases/B76/B76-C02-escalas-sinodicas-de-referencia/CLASE.md).

### Resonancia de Laplace

- La resonancia de Laplace liga tres cuerpos: `n₁ − 3n₂ + 2n₃ = 0`.

💡 **Cómo se explica en la clase [B52-C07](../programa/clases/B52/B52-C07-resonancias-orbitales/CLASE.md):**
- La evidencia es la ficha de la resonancia de Laplace del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Integrador. Elabora tu *ficha de la resonancia de Laplace*: tabla 8.1, relación, razones y límites.
- 🎯 **Por qué importa:** Una resonancia protege o desestabiliza órbitas y deja huellas que se pueden medir. La decisión central: ¿cómo se reconoce una resonancia en datos orbitales y con qué cautela?

📘 **Dónde se aprende** (1 clase): [B52-C07 · Resonancias orbitales](../programa/clases/B52/B52-C07-resonancias-orbitales/CLASE.md).

### Resonancia de movimiento medio

- Una resonancia de movimiento medio `p:q` ocurre cuando `p n₁ ≈ q n₂` y el ángulo resonante libra.
- Una resonancia de movimiento medio `p:q` ocurre cuando `P_ast/P_J = q/p`.
- La resonancia de movimiento medio `p:q` cumple `p n₁ ≈ q n₂`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B72-C11](../programa/clases/B72/B72-C11-resonancias-orbitales-perturbaciones-y-evolucion-de-orbitas/CLASE.md):**
- *Descripción textual:* los periodos dan los movimientos medios; su combinación de Laplace prueba la resonancia; el péndulo y su energía clasifican la libración y la circulación.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de resonancias*: movimientos medios, combinación de Laplace, semiejes resonantes con la Tierra, periodos de libración y la lista de lo consultado, lo ilustrativo y lo no consultado.
- 🎯 **Por qué importa:** Una resonancia mantiene a los satélites de Júpiter en equilibrio dinámico y obliga a gestionar un satélite geoestacionario, que se desplaza hacia dos puntos de equilibrio por el campo no esférico.

📘 **Dónde se aprende** (4 clases): [B52-C07 · Resonancias orbitales](../programa/clases/B52/B52-C07-resonancias-orbitales/CLASE.md); [B58-C02 · Dinámica de asteroides](../programa/clases/B58/B58-C02-dinamica-de-asteroides/CLASE.md); [B72-C11 · Resonancias orbitales — Perturbaciones y evolución de órbitas](../programa/clases/B72/B72-C11-resonancias-orbitales-perturbaciones-y-evolucion-de-orbitas/CLASE.md); [B73-C10 · Resonancias de movimiento medio](../programa/clases/B73/B73-C10-resonancias-de-movimiento-medio/CLASE.md).

### Resonancia exterior p:q

- Una resonancia exterior `p:q` liga el periodo del objeto `P = (p/q) P_N`.

💡 **Cómo se explica en la clase [B52-C15](../programa/clases/B52/B52-C15-cinturon-de-kuiper/CLASE.md):**
- Descripción larga: las resonancias exteriores se ubican entre 36 y 55 ua y a 40 ua la temperatura de equilibrio ronda los 40 K.
- Obtener `a_res = a_N (p/q)^(2/3)` para resonancias exteriores.
- ⚠️ **Error frecuente:** Invertir `p/q` en las resonancias exteriores. Se corrige con 8.2.
- 🎯 **Por qué importa:** Las resonancias con Neptuno protegen a cuerpos cuyos perihelios cruzan su órbita, y la temperatura fija qué hielos sobreviven. La decisión central: ¿en qué semiejes están las resonancias exteriores y qué temperatura tiene el cinturón?

📘 **Dónde se aprende** (1 clase): [B52-C15 · Cinturón de Kuiper](../programa/clases/B52/B52-C15-cinturon-de-kuiper/CLASE.md).

### Resonancia k:m

- Una resonancia `k:m` hace que el periodo de la nave sea `(m/k)` años.

💡 **Cómo se explica en la clase [B75-C25](../programa/clases/B75/B75-C25-resonancias-para-sobrevuelos/CLASE.md):**
- Con 3 km/s solo las resonancias casi 1:1 (`1:1` y `3:4`) alcanzan a cruzar la Tierra.
- Para las resonancias viables, tras `m` años la nave propagada con Kepler vuelve a su posición con error relativo menor que `10⁻⁶`.
- ⚠️ **Error frecuente:** Suponer que la resonancia siempre cruza la Tierra. Se corrige con 8.2.
- 🎯 **Por qué importa:** Para volver a un planeta hay que llegar a la misma posición un número entero de años después. La decisión central: ¿qué resonancias `k:m` son alcanzables con un `v∞` dado y cuánto `v∞` hace falta para las demás?

📘 **Dónde se aprende** (1 clase): [B75-C25 · Resonancias para sobrevuelos](../programa/clases/B75/B75-C25-resonancias-para-sobrevuelos/CLASE.md).

### Resonancia p:q

- Una resonancia `p:q` ocurre cuando el asteroide da `p` vueltas por cada `q` de Júpiter.

💡 **Cómo se explica en la clase [B52-C14](../programa/clases/B52/B52-C14-cinturones-de-asteroides/CLASE.md):**
- Cinco resonancias caen dentro del intervalo ilustrativo de 2,0 a 3,3 ua (que no se consultó).
- El cálculo solo localiza las resonancias.
- 🎯 **Por qué importa:** Las posiciones de las resonancias fijan dónde mirar en un cinturón. La decisión central: ¿en qué semiejes están las resonancias de Júpiter y cómo se comprueba el cálculo?

📘 **Dónde se aprende** (1 clase): [B52-C14 · Cinturones de asteroides](../programa/clases/B52/B52-C14-cinturones-de-asteroides/CLASE.md).

### Resonancia secular

- Una resonancia secular ocurre cuando la precesión de un cuerpo iguala una de estas frecuencias.

💡 **Cómo se explica en la clase [B73-C11](../programa/clases/B73/B73-C11-resonancias-seculares/CLASE.md):**
- *Descripción textual:* los datos dan los coeficientes de Laplace, éstos las matrices, y de ellas salen las frecuencias propias, la evolución de `e` y la posición de las resonancias seculares.
- Una resonancia secular con `g₁`: la excentricidad puede crecer; es una ilustración del modelo, no una predicción de ningún objeto real.
- ⚠️ **Error frecuente:** Confundir resonancia secular con resonancia de movimiento medio. Se corrige con la última pregunta de transferencia.
- 🎯 **Por qué importa:** La excentricidad de una órbita varía durante millones de años por la atracción promediada de los demás planetas, y esa variación se vuelve violenta cuando una frecuencia propia coincide con la de precesión de un asteroide.

📘 **Dónde se aprende** (1 clase): [B73-C11 · Resonancias seculares](../programa/clases/B73/B73-C11-resonancias-seculares/CLASE.md).

### Resonancia torsional

- La resonancia torsional `f = √(k/J)/(2π)`.

🎯 **Por qué importa (clase B43-C14):** El reductor fija la resolución, la fuerza disponible y el comportamiento dinámico. La decisión central: ¿qué relación, qué rendimiento y qué rigidez permiten apuntar con la resolución pedida sin resonancias?

📘 **Dónde se aprende** (1 clase): [B43-C14 · Reductores y transmisiones](../programa/clases/B43/B43-C14-reductores-y-transmisiones/CLASE.md).

### Respeto por las personas

- El informe Belmont nombra tres principios: respeto por las personas (autonomía y protección de quienes tienen autonomía disminuida), beneficencia (no dañar y maximizar beneficios) y justicia (reparto equitativo de cargas y beneficios).

💡 **Cómo se explica en la clase [B105-C19](../programa/clases/B105/B105-C19-bioetica-en-investigacion-tripulada/CLASE.md):**
- Un resumen de búsqueda web (2026-11-10) del informe Belmont indica tres principios: respeto por las personas (voluntariedad e información adecuada; protección de quienes tienen autonomía disminuida), beneficencia (no dañar y maximizar beneficios minimizando daños) y justicia (quién carga con los riesgos y quién recibe los beneficios).
- Los tres principios del informe Belmont (respeto por las personas, beneficencia, justicia) se consultaron solo por un resumen de búsqueda web (2026-11-10).
- ⚠️ **Error frecuente:** Dar por cumplido el respeto por las personas con una firma. Exige información y voluntariedad reales.
- 🎯 **Por qué importa:** No basta con quitar el nombre: con edad, sexo, profesión y misión, una persona de una cohorte de 6 suele ser única. La decisión central: ¿qué se puede publicar de una cohorte pequeña sin identificar a nadie y cuánta utilidad se pierde al protegerla?

📘 **Dónde se aprende** (1 clase): [B105-C19 · Bioética en investigación tripulada](../programa/clases/B105/B105-C19-bioetica-en-investigacion-tripulada/CLASE.md).

### Responsabilidad absoluta

- La responsabilidad absoluta no exige culpa.
- La responsabilidad absoluta no exige probar culpa.

💡 **Cómo se explica en la clase [B118-C18](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md):**
- II, responsabilidad absoluta por daños en la superficie de la Tierra o a aeronaves en vuelo; art.
- Por responsabilidad: absoluta o por culpa.
- 🎯 **Por qué importa:** Con decenas de miles de objetos, comparar todos los pares es costoso; un buen cribado descarta de entrada los pares imposibles sin perder ninguno posible. Y cuando algo sale mal, los tratados determinan responsabilidad y jurisdicción.

📘 **Dónde se aprende** (4 clases): [B118-C18 · Gestión del tráfico espacial](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md); [B119-C03 · Convenio de Responsabilidad](../programa/clases/B119/B119-C03-convenio-de-responsabilidad/CLASE.md); [B123-C02 · Causalidad y atribución jurídica del daño](../programa/clases/B123/B123-C02-causalidad-y-atribucion-juridica-del-dano/CLASE.md); [B127-C03 · Seguros de responsabilidad civil espacial](../programa/clases/B127/B127-C03-seguros-de-responsabilidad-civil-espacial/CLASE.md).

### Responsabilidad por culpa

- La responsabilidad por culpa exige que el daño se deba a la culpa del causante.
- II) se aplica al daño en la superficie o a una aeronave en vuelo; la responsabilidad por culpa (art.

💡 **Cómo se explica en la clase [B118-C18](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md):**
- Por responsabilidad: absoluta o por culpa.
- III (responsabilidad por culpa en otras partes);
- 🎯 **Por qué importa:** Con decenas de miles de objetos, comparar todos los pares es costoso; un buen cribado descarta de entrada los pares imposibles sin perder ninguno posible. Y cuando algo sale mal, los tratados determinan responsabilidad y jurisdicción.

📘 **Dónde se aprende** (4 clases): [B118-C18 · Gestión del tráfico espacial](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md); [B119-C03 · Convenio de Responsabilidad](../programa/clases/B119/B119-C03-convenio-de-responsabilidad/CLASE.md); [B123-C02 · Causalidad y atribución jurídica del daño](../programa/clases/B123/B123-C02-causalidad-y-atribucion-juridica-del-dano/CLASE.md); [B127-C03 · Seguros de responsabilidad civil espacial](../programa/clases/B127/B127-C03-seguros-de-responsabilidad-civil-espacial/CLASE.md).

### Respuesta

- La respuesta o sensibilidad `S(λ)` en cuentas por unidad de flujo.

💡 **Cómo se explica en la clase [B45-C09](../programa/clases/B45/B45-C09-calibracion-de-respuesta-instrumental/CLASE.md):**
- El RMS observado excede lo previsto en un factor `1,75`: la media móvil de 11 bins sesga la respuesta donde cambia rápido.
- Límite: respuesta estable, cuentas altas.
- 🎯 **Por qué importa:** Sin respuesta, un espectro en cuentas no es un espectro físico. La decisión central: ¿cómo se pasa de cuentas a flujo y con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B45-C09 · Calibración de respuesta instrumental](../programa/clases/B45/B45-C09-calibracion-de-respuesta-instrumental/CLASE.md).

### Respuesta a un escalón

- La respuesta a un escalón `T(t) = T_eq + (T₀ − T_eq)e^(−t/τ)`.

💡 **Cómo se explica en la clase [B85-C26](../programa/clases/B85/B85-C26-analisis-termico-transitorio-y-casos-extremos/CLASE.md):**
- Obtener la respuesta analítica de un nodo a un escalón.
- 🎯 **Por qué importa:** El peor caso de temperatura casi nunca es el de régimen. La decisión central: ¿qué paso de tiempo y qué esquema dan una respuesta fiable y cuál es la temperatura extrema en el eclipse o en el arranque?

📘 **Dónde se aprende** (1 clase): [B85-C26 · Análisis térmico transitorio y casos extremos](../programa/clases/B85/B85-C26-analisis-termico-transitorio-y-casos-extremos/CLASE.md).

### Respuesta al impulso

- La respuesta al impulso `h(t)` es la salida cuando la entrada es un impulso (delta de Dirac) en `t = 0` desde reposo.

💡 **Cómo se explica en la clase [B16-C03](../programa/clases/B16/B16-C03-sistemas-lineales-invariantes/CLASE.md):**
- Para `J ω̇ + c ω = τ`, la respuesta al impulso de par es `h(t) = e^(−c t/J)/J` para `t ≥ 0` (el impulso fija `ω(0⁺) = 1/J` y luego decae).
- La respuesta al impulso de un LTI es combinación de exponenciales `e^(λt)`, con `λ` los autovalores de `A` (C02, B10-C08).
- 🎯 **Por qué importa:** Un ingeniero de control no puede ensayar todos los pares posibles en un telescopio de miles de millones de euros. La esperanza es que, con unas pocas pruebas, se pueda predecir la respuesta a cualquier par.

📘 **Dónde se aprende** (1 clase): [B16-C03 · Sistemas lineales invariantes](../programa/clases/B16/B16-C03-sistemas-lineales-invariantes/CLASE.md).

### Respuesta de banda

- La respuesta de banda `B(ν)`.

💡 **Cómo se explica en la clase [B51-C04](../programa/clases/B51/B51-C04-respuesta-de-banda-y-errores-dependientes-de-la-frecuencia/CLASE.md):**
- La evidencia es la ficha de la respuesta de banda del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha de la respuesta de banda*: modelo, retardo, ondulación, precisión y límites.
- 🎯 **Por qué importa:** Un error de banda aparece en las líneas espectrales como una falsa estructura y limita el rango dinámico del continuo. La decisión central: ¿qué parte del error de banda es un retardo, qué parte una ondulación, y con qué precisión se miden?

📘 **Dónde se aprende** (1 clase): [B51-C04 · Respuesta de banda y errores dependientes de la frecuencia](../programa/clases/B51/B51-C04-respuesta-de-banda-y-errores-dependientes-de-la-frecuencia/CLASE.md).

### Respuesta en frecuencia

- La respuesta en frecuencia `H(f)` indica cómo cambia cada frecuencia `f`: el módulo `|H|` escala la amplitud y el argumento desfasa.
- La respuesta en frecuencia de `L` es `L(jω)`, con `ω` en rad/s: el módulo es la amplificación de una sinusoide y la fase es su desfase.

💡 **Cómo se explica en la clase [B15-C07](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md):**
- *Descripción textual:* la serie entra en el filtro, que se describe por sus coeficientes `h` o, de forma equivalente, por su respuesta en frecuencia `H(f)`; esta determina cuánto se atenúa cada frecuencia y cuánto se retrasa.
- Descripción larga: la respuesta de la media móvil es un lóbulo central que vale 1 en `f = 0` y cae a cero en `f = 1/M`, seguido de lóbulos laterales pequeños; la del filtro de un polo es una curva suave que baja con la frecuencia.
- 🎯 **Por qué importa:** Una curva de luz tiene una modulación lenta de la estrella (manchas que rotan) de 2000 partes por millón y, escondido en ella, el paso de un planeta que reduce el brillo 1000 ppm durante tres horas. Para ver el tránsito hay que quitar la modulación; pero si el filtro es demasiado agresivo, también se come parte del tránsito.

📘 **Dónde se aprende** (2 clases): [B15-C07 · Filtrado digital](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md); [B16-C10 · Diagramas de Bode y Nyquist](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md).

### Respuesta espectral

- La banda espectral tiene una respuesta espectral `S(λ)`; su ancho a media altura (FWHM) mide cuán estrecha es.

💡 **Cómo se explica en la clase [B57-C03](../programa/clases/B57/B57-C03-resolucion-radiometrica-y-espectral/CLASE.md):**
- Límites: no incluye ruido del detector ni la respuesta espectral real de OLI.
- 🎯 **Por qué importa:** Dos sensores con el mismo píxel pueden dar información muy distinta si uno distingue 256 niveles y otro 65.536, o si una banda es ancha y otra estrecha. La decisión central: ¿cuántos bits y qué ancho de banda hacen falta para ver el cambio que me interesa?

📘 **Dónde se aprende** (1 clase): [B57-C03 · Resolución radiométrica y espectral](../programa/clases/B57/B57-C03-resolucion-radiometrica-y-espectral/CLASE.md).

### Respuesta impulsional

- La respuesta impulsional `h[n]` es la salida del sistema cuando la entrada es `δ[n]`.

💡 **Cómo se explica en la clase [B15-C08](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md):**
- Imagina golpear un tambor: un golpe produce una vibración que se apaga; esa vibración es la respuesta impulsional.
- Explicar por qué la salida de un sistema lineal e invariante es la suma de respuestas impulsionales desplazadas y escaladas.
- 🎯 **Por qué importa:** Un termistor a bordo de una nave no mide la temperatura del instante: mide una versión retrasada y suavizada, porque su cuerpo tarda en calentarse o enfriarse. Si la nave entra en eclipse y el entorno baja 50 K de golpe, el sensor irá bajando poco a poco.

📘 **Dónde se aprende** (1 clase): [B15-C08 · Convolución y respuesta impulsional](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md).

### Respuesta lineal

- Una respuesta lineal crece proporcionalmente al error.

💡 **Cómo se explica en la clase [B50-C10](../programa/clases/B50/B50-C10-errores-de-centrado-y-su-efecto-en-el-desempeno/CLASE.md):**
- La respuesta es lineal (el cociente RMS/d es constante) y simétrica en `±d`.
- Predice antes de ejecutar: ¿será lineal la respuesta?
- 🎯 **Por qué importa:** El descentramiento es una de las tolerancias de montaje que más pesan en un telescopio. La decisión central: ¿cuánto puede desplazarse el secundario antes de degradar la imagen?

📘 **Dónde se aprende** (1 clase): [B50-C10 · Errores de centrado y su efecto en el desempeño](../programa/clases/B50/B50-C10-errores-de-centrado-y-su-efecto-en-el-desempeno/CLASE.md).

### Respuesta relativa

- La respuesta relativa `r(t)` es el cociente entre la indicación y la de la época inicial para una fuente estable.

🎯 **Por qué importa (clase B13-C23):** Un detector espacial lleva años en órbita. Su sensibilidad cambia lentamente por daño de radiación, contaminación y envejecimiento.

📘 **Dónde se aprende** (1 clase): [B13-C23 · Estabilidad y deriva temporal de instrumentos](../programa/clases/B13/B13-C23-estabilidad-y-deriva-temporal-de-instrumentos/CLASE.md).

### Respuesta transitoria

- La respuesta transitoria es la parte que se extingue con el tiempo; la estacionaria es la que queda cuando el transitorio desapareció.

💡 **Cómo se explica en la clase [B16-C04](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md):**
- Para nuestro estudio, esas dos fases son exactamente la respuesta transitoria (cómo llega) y la respuesta estacionaria (dónde se queda).
- Distinguir la parte transitoria de la estacionaria de una respuesta.
- 🎯 **Por qué importa:** Tras girar un telescopio hacia una estrella nueva, los instrumentos no pueden empezar a exponer hasta que el apuntamiento se haya asentado. Cada segundo de espera cuesta tiempo de observación.

📘 **Dónde se aprende** (1 clase): [B16-C04 · Respuesta transitoria y estacionaria](../programa/clases/B16/B16-C04-respuesta-transitoria-y-estacionaria/CLASE.md).

### Resto

- El resto `Rₙ` es la diferencia entre `f` y su polinomio; en la forma de Lagrange, `Rₙ = f^{(n+1)}(ξ) (x − a)^{n+1}/(n + 1)!` para algún `ξ` entre `a` y `x` (S1, §1.4(vi), ecs. 1.4.35–1.4.36).

💡 **Cómo se explica en la clase [B09-C14](../programa/clases/B09/B09-C14-series-y-aproximaciones/CLASE.md):**
- D --> E["Resto Rₙ<br/>(cota de Lagrange)"]
- *Descripción textual:* se añaden términos de la serie hasta que la cota del resto sea menor que la tolerancia y se verifica que `x` esté dentro del radio de convergencia.
- 🎯 **Por qué importa:** Un cálculo orbital rápido usa `g(h) = g₀(1 − 2h/R)` para una altitud baja; uno más exigente necesita el siguiente término. Sin una cota del error no se sabe cuál usar.

📘 **Dónde se aprende** (1 clase): [B09-C14 · Series y aproximaciones](../programa/clases/B09/B09-C14-series-y-aproximaciones/CLASE.md).

### Restricción

- Una restricción es una condición que liga las variables (por ejemplo, un volumen fijo).
- Un ciclo V baja de la malla fina a la más gruesa y vuelve a subir. Restricción es pasar un campo a la malla gruesa;
- Una restricción limita el espacio de soluciones.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C07](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md):**
- Paso 1 · Objetivo y restricción. Minimizar `A = 2πr² + 2πrL` con `π r² L = 10`.
- Sentido: el cilindro óptimo es «tan alto como ancho»; un tanque real tiene casquetes esféricos y otras restricciones.
- ⚠️ **Error frecuente:** Optimizar con dos variables sin usar la restricción. Se corrige en el paso 2 del ejemplo trabajado.
- 🎯 **Por qué importa:** Un tanque de propelente cuesta masa en su pared: dado el volumen que necesita, ¿qué forma usa menos material? Un vehículo que viaja de la Tierra a la Luna pasa por una región donde la atracción de ambos cuerpos se compensa.

📘 **Dónde se aprende** (6 clases): [B03-C20 · Problema integrado de escala del sistema solar](../programa/clases/B03/B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md); [B09-C07 · Optimización con derivadas](../programa/clases/B09/B09-C07-optimizacion-con-derivadas/CLASE.md); [B21-C03 · Ecuación de Poisson: relajación y multigrid](../programa/clases/B21/B21-C03-ecuacion-de-poisson-relajacion-y-multigrid/CLASE.md); [B21-C05 · Mallas adaptativas (AMR)](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md); [B50-C02 · Optimización de superficies: función de mérito y restricciones](../programa/clases/B50/B50-C02-optimizacion-de-superficies-funcion-de-merito-y-restricciones/CLASE.md); [B83-C12 · Model-Based Systems Engineering](../programa/clases/B83/B83-C12-model-based-systems-engineering/CLASE.md).

### Restricción adicional

- Una restricción adicional es un dato independiente que acota la familia.

💡 **Cómo se explica en la clase [B65-C05](../programa/clases/B65/B65-C05-inversion-geofisica-conjunta-validacion-de-modelos-interiores/CLASE.md):**
- Añadir una restricción adicional y propagar las incertidumbres de forma lineal y por Monte Carlo.
- Ejercicio 12. Integrador. Elabora tu *ficha de la inversión conjunta*: familia de modelos, restricción adicional, `σ` lineal y Monte Carlo, y qué dato domina.
- 🎯 **Por qué importa:** Un modelo interior que reproduce los datos no es por eso el correcto. La decisión central: ¿qué datos faltan para elegir un modelo entre los que cumplen los datos que ya tienes?

📘 **Dónde se aprende** (1 clase): [B65-C05 · Inversión geofísica conjunta: validación de modelos interiores](../programa/clases/B65/B65-C05-inversion-geofisica-conjunta-validacion-de-modelos-interiores/CLASE.md).

### Restricción blanda

- La restricción blanda de velocidad se castiga con `ρ max(0, |ω|−ω_max)²`.

💡 **Cómo se explica en la clase [B87-C21](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md):**
- El MPC lo respeta con una violación de `1,5 %` (restricción blanda); el PD lo excede en `11 %`.
- Límite: si el modelo (la carretera) es incorrecto, el plan también lo es; y la restricción de velocidad aquí es blanda.
- ⚠️ **Error frecuente:** Creer que el MPC garantiza la restricción blanda. Revisa la violación residual (8.4)
- 🎯 **Por qué importa:** Un PD satura el par y no sabe de límites de velocidad: puede superar el máximo de la rueda o de la carga útil. La decisión central: ¿cómo formular un problema que respete par y velocidad, cuánto cuesta calcularlo y qué se gana?

📘 **Dónde se aprende** (1 clase): [B87-C21 · Control predictivo basado en modelo (MPC) para vehículos espaciales](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md).

### Restricción de pies

- Una restricción de pies fija los pies del operador a un punto de trabajo.

💡 **Cómo se explica en la clase [B108-C04](../programa/clases/B108/B108-C04-sistemas-de-sujecion-y-restriccion-de-pies/CLASE.md):**
- La evidencia es la comparación con y sin restricción de pies del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *comparación con y sin restricción de pies*: ángulo libre y con restricción a 2 s, barrido de rigidez, sobreimpulso y verificación numérica.
- 🎯 **Por qué importa:** Ninguna clase trata la estabilización del astronauta durante trabajo en microgravedad. La decisión central: ¿cuánto rigidez y amortiguamiento necesita una sujeción para que una fuerza de trabajo no desplace a la persona más allá de lo útil?

📘 **Dónde se aprende** (1 clase): [B108-C04 · Sistemas de sujeción y restricción de pies](../programa/clases/B108/B108-C04-sistemas-de-sujecion-y-restriccion-de-pies/CLASE.md).

### Restricción dura

- Una restricción dura es un requisito que descarta si no se cumple.
- La restricción dura de par `|a| ≤ u_max/I`.

💡 **Cómo se explica en la clase [B87-C21](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md):**
- Ejercicio 8 · autónomo. ¿Qué restricción es dura y cuál blanda en esta clase?
- Como restricción adicional sobre `h_k = h₀ + Σ u` en el QP (blanda o dura); aquí no se modela.
- 🎯 **Por qué importa:** Un PD satura el par y no sabe de límites de velocidad: puede superar el máximo de la rueda o de la carga útil. La decisión central: ¿cómo formular un problema que respete par y velocidad, cuánto cuesta calcularlo y qué se gana?

📘 **Dónde se aprende** (2 clases): [B87-C21 · Control predictivo basado en modelo (MPC) para vehículos espaciales](../programa/clases/B87/B87-C21-control-predictivo-basado-en-modelo-mpc-para-vehiculos-espaciales/CLASE.md); [B95-C03 · Selección y comparación de plataformas](../programa/clases/B95/B95-C03-seleccion-y-comparacion-de-plataformas/CLASE.md).

### Restringida

- La categoría V se añade a las misiones que traen muestras a la Tierra; es restringida o no restringida.

🎯 **Por qué importa (clase B56-C18):** La política protege los otros mundos de la contaminación (para no estropear la búsqueda de vida) y la Tierra del material devuelto. Saber en qué categoría cae una misión determina su documentación, su limpieza y sus restricciones.

📘 **Dónde se aprende** (1 clase): [B56-C18 · Protección planetaria COSPAR](../programa/clases/B56/B56-C18-proteccion-planetaria-cospar/CLASE.md).

### Resuelve

- Un triángulo se resuelve cuando se conocen sus tres lados y sus tres ángulos.

💡 **Cómo se explica en la clase [B04-C08](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md):**
- En la práctica se resuelve con una ley y se verifica con la otra.
- 🎯 **Por qué importa:** Cuando una sonda se comunica con la Tierra, el tiempo de la señal depende de la distancia, que cambia de unos 55 millones de km a unos 400 millones según dónde estén ambos planetas en sus órbitas.

📘 **Dónde se aprende** (1 clase): [B04-C08 · Ley de senos y ley de cosenos](../programa/clases/B04/B04-C08-ley-de-senos-y-ley-de-cosenos/CLASE.md).

### Resultado de aprendizaje

- Un resultado de aprendizaje es un enunciado de lo que el estudiante será capaz de hacer.

💡 **Cómo se explica en la clase [B131-C02](../programa/clases/B131/B131-C02-resultados-de-aprendizaje-observables-en-astronomia/CLASE.md):**
- La evidencia es tu lista revisada de resultados de aprendizaje del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *lista revisada de resultados de aprendizaje*: 8–10 resultados observables de una unidad, su nivel, su actividad, su ítem, el chequeo de huérfanos y de desajustes, y qué es ilustrativo.
- 🎯 **Por qué importa:** Sin resultados observables, una actividad no se puede evaluar. La decisión central: ¿este enunciado dice algo que pueda verse que el estudiante hace?

📘 **Dónde se aprende** (1 clase): [B131-C02 · Resultados de aprendizaje observables en astronomía](../programa/clases/B131/B131-C02-resultados-de-aprendizaje-observables-en-astronomia/CLASE.md).

### Resultado indeterminado

- Falso rechazo (PFR): rechazar una unidad conforme. Resultado indeterminado: medida dentro de la banda de incertidumbre del límite.

💡 **Cómo se explica en la clase [B90-C08](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. ¿Qué hacer con un resultado indeterminado en una prueba de una sola unidad de vuelo?
- 🎯 **Por qué importa:** Toda medida tiene incertidumbre. Si se acepta con el límite exacto, algunas unidades malas pasan; si se endurece el criterio, algunas buenas se rechazan y cuesta tiempo.

📘 **Dónde se aprende** (1 clase): [B90-C08 · Procedimientos de prueba funcional](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md).

### Resumen

- Un resumen (*digest*) identifica una imagen por su contenido.
- El resumen condensa el trabajo en un párrafo.

💡 **Cómo se explica en la clase [B14-C17](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md):**
- El Dockerfile con versiones fijas, el bloqueo, el resumen de la imagen, la versión y huella de los datos, las instrucciones de ejecución y una comprobación de que el resultado coincide dentro de una tolerancia.
- 🎯 **Por qué importa:** Tu análisis funciona con el bloqueo de C12 en tu equipo, pero en el servidor del laboratorio falla porque falta una biblioteca del sistema. La pregunta motivadora es: ¿cómo entrego el análisis junto con todo lo que necesita para correr, de modo que otra persona lo ejecute igual?

📘 **Dónde se aprende** (2 clases): [B14-C17 · Contenedores y ambientes científicos](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md); [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md).

### Resumen de integridad de NIST SP 800-193

- El resumen de integridad de NIST SP 800-193 habla de protección, detección y recuperación del firmware.

🎯 **Por qué importa (clase B88-C18):** Si no se sabe exactamente qué firmware vuela, no se puede reproducir un fallo ni comprobar que se probó lo que se lanzó. La decisión central: ¿qué registro identifica de manera única una versión y permite verificarla?

📘 **Dónde se aprende** (1 clase): [B88-C18 · Control de configuración de firmware](../programa/clases/B88/B88-C18-control-de-configuracion-de-firmware/CLASE.md).

### Retardador

- Un retardador tiene retardancia `δ` y eje rápido `θ`.

💡 **Cómo se explica en la clase [B45-C15](../programa/clases/B45/B45-C15-polarizacion-lineal-y-circular/CLASE.md):**
- Un retardador de 77° con eje a 13° deja `P = 0,229129` igual que antes (`0,229129`).
- Aplicar matrices de Mueller de polarizador y retardador.
- ⚠️ **Error frecuente:** Creer que un retardador despolariza. Se corrige con 8.4.
- 🎯 **Por qué importa:** La polarización informa de campos magnéticos, dispersión y geometría. La decisión central: ¿cómo se calcula el estado de polarización tras cada elemento?

📘 **Dónde se aprende** (1 clase): [B45-C15 · Polarización lineal y circular](../programa/clases/B45/B45-C15-polarizacion-lineal-y-circular/CLASE.md).

### Retardo

- La autocorrelación `r_k` mide cuánto se parece la serie a sí misma desplazada `k` muestras; el número `k` es el retardo (en inglés *lag*).
- El retardo es cuánto desplaza el filtro la señal en el tiempo.
- Un retardo de `d` muestras de periodo `T` es una demora `d·T` entre medir y actuar.
- *(y 10 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C01](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md):**
- Con la media `x̄`, la autocorrelación muestral al retardo `k` es
- Calcular la autocorrelación a un retardo dado y leer qué periodicidad sugiere.
- 🎯 **Por qué importa:** Un telescopio espacial mide el brillo de una estrella cada dos minutos durante semanas. Lo que llega a tierra no es una curva continua, sino una tabla de números.

📘 **Dónde se aprende** (15 clases): [B15-C01 · Series temporales discretas](../programa/clases/B15/B15-C01-series-temporales-discretas/CLASE.md); [B15-C07 · Filtrado digital](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md); [B15-C21 · Series temporales multivariadas y regresión dinámica](../programa/clases/B15/B15-C21-series-temporales-multivariadas-y-regresion-dinamica/CLASE.md); [B16-C07 · Realimentación y estabilidad](../programa/clases/B16/B16-C07-realimentacion-y-estabilidad/CLASE.md); [B27-C20 · Análisis multibanda de un evento extremo](../programa/clases/B27/B27-C20-analisis-multibanda-de-evento-extremo/CLASE.md); [B34-C09 · Integración multiinstrumento de datos heliofísicos](../programa/clases/B34/B34-C09-integracion-multiinstrumento-de-datos-heliofisicos/CLASE.md) y 9 más.

### Retardo cenital

- El retardo cenital (hidrostático y húmedo).

💡 **Cómo se explica en la clase [B51-C10](../programa/clases/B51/B51-C10-retardo-troposferico-e-ionosferico-en-vlbi-y-su-modelado/CLASE.md):**
- El retardo cenital numérico es 2,240000 m frente a `N₀ H₀ = 2,240000` m (analítico).
- A["refractividad N(h) exponencial"] --> Z["retardo cenital"]
- 🎯 **Por qué importa:** Un error atmosférico de centímetros es un error de posición en geodesia y un error de fase en imagen. La decisión central: ¿cómo se mapea el retardo con la elevación y cómo se separa lo dispersivo de lo no dispersivo?

📘 **Dónde se aprende** (1 clase): [B51-C10 · Retardo troposférico e ionosférico en VLBI y su modelado](../programa/clases/B51/B51-C10-retardo-troposferico-e-ionosferico-en-vlbi-y-su-modelado/CLASE.md).

### Retardo de detección

- El retardo de detección es el tiempo desde el inicio del evento hasta la alarma.
- Falsa alarma: alerta sin falla. Retardo de detección: muestras hasta alertar.

💡 **Cómo se explica en la clase [B48-C23](../programa/clases/B48/B48-C23-observabilidad-del-software-de-observatorio-registros-metricas-y-alertas/CLASE.md):**
- Con umbral de 2 sigmas y avería de +3 sigmas, la regla 3 de 5 tiene falsa alarma 1.138e-04 por ventana, detección 0,9690 y retardo medio 3,59 muestras (la regla de una muestra tiene 1,19 pero falsas alarmas 2,28 % por muestra).
- Ejercicio 10 · transferencia. Transferencia. ¿Por qué medir el retardo y no solo la detección?
- 🎯 **Por qué importa:** Demasiadas falsas alarmas se ignoran; muy pocas dejan las averías sin ver. La decisión central: ¿qué regla de alerta equilibra falsas alarmas y retardo?

📘 **Dónde se aprende** (2 clases): [B48-C23 · Observabilidad del software de observatorio: registros, métricas y alertas](../programa/clases/B48/B48-C23-observabilidad-del-software-de-observatorio-registros-metricas-y-alertas/CLASE.md); [B116-C05 · Alertas de salud y umbrales de monitorización](../programa/clases/B116/B116-C05-alertas-de-salud-y-umbrales-de-monitorizacion/CLASE.md).

### Retardo de grupo

- El retardo de grupo es el tiempo extra respecto del vacío.
- El retardo de grupo respecto de la luz.

💡 **Cómo se explica en la clase [B30-C08](../programa/clases/B30/B30-C08-frecuencias-y-ondas-de-plasma/CLASE.md):**
- Calcular el retardo de grupo por cuadratura y por columna.
- 🎯 **Por qué importa:** La radiación de las erupciones se emite cerca de la frecuencia de plasma local, de modo que una frecuencia es una altura. La decisión central: ¿qué frecuencia corresponde a cada densidad y cuánto se retrasa una señal?

📘 **Dónde se aprende** (3 clases): [B30-C08 · Frecuencias y ondas de plasma](../programa/clases/B30/B30-C08-frecuencias-y-ondas-de-plasma/CLASE.md); [B46-C02 · Propagación de ondas de radio](../programa/clases/B46/B46-C02-propagacion-de-ondas-de-radio/CLASE.md); [B46-C18 · VLBI y geodesia](../programa/clases/B46/B46-C18-vlbi-y-geodesia/CLASE.md).

### Retardo de ida

- El retardo de ida es `d/c`.
- El retardo de ida es `d/c`; el de ida y vuelta (RTT), `2d/c`.
- El retardo de ida `L = d/c` es el tiempo que tarda la señal en llegar.

💡 **Cómo se explica en la clase [B97-C07](../programa/clases/B97/B97-C07-teleoperacion-con-latencia/CLASE.md):**
- Con bloques de `10` pasos, Marte a la distancia máxima baja a `11031` s; con un bloque de `40`, a `2938` s: se paga el retardo una sola vez.
- D["distancia d"] --> T["retardo t = d / c"]
- ⚠️ **Error frecuente:** Usar el retardo de ida como si fuera el de ida y vuelta. El ciclo paga `2t` (8.2)
- 🎯 **Por qué importa:** Con un retardo de unos segundos se puede teleoperar casi en vivo; con minutos, no. La diferencia se traduce en horas o días de tarea y en la necesidad de dar autonomía al robot.

📘 **Dónde se aprende** (4 clases): [B97-C07 · Teleoperación con latencia](../programa/clases/B97/B97-C07-teleoperacion-con-latencia/CLASE.md); [B104-C12 · Robótica tripulada](../programa/clases/B104/B104-C12-robotica-tripulada/CLASE.md); [B105-C15 · Telemedicina espacial](../programa/clases/B105/B105-C15-telemedicina-espacial/CLASE.md); [B113-C03 · Comunicación diferida y soporte psicológico a distancia](../programa/clases/B113/B113-C03-comunicacion-diferida-y-soporte-psicologico-a-distancia/CLASE.md).

### Retardo de llegada

- El retardo de llegada es la diferencia de tiempo entre fotones emitidos a distinto radio.

🎯 **Por qué importa (clase B27-C17):** Una explosión que parece de energía enorme puede ser de energía moderada vista de frente, y un retardo de segundos entre dos mensajeros, tras viajar 130 millones de años, es una medición extraordinariamente precisa. La decisión central: ¿qué retardo y qué energía real implican un factor de Lorentz y un ángulo dados?

📘 **Dónde se aprende** (1 clase): [B27-C17 · Explosiones de rayos gamma](../programa/clases/B27/B27-C17-explosiones-de-rayos-gamma/CLASE.md).

### Retardo de luz

- El retardo de luz es `d/c`.

💡 **Cómo se explica en la clase [B89-C04](../programa/clases/B89/B89-C04-propagacion-y-perdidas-de-espacio-libre/CLASE.md):**
- *Descripción textual:* la distancia y la frecuencia dan la pérdida de espacio libre; la distancia sola da el retardo; sumando la atmósfera se obtiene la pérdida total.
- Descripción larga: la pérdida crece 6 dB por cada duplicación de distancia y 20 dB por década de frecuencia, mientras el retardo crece linealmente con la distancia.
- ⚠️ **Error frecuente:** Olvidar el retardo al planear operaciones. Se corrige con 8.3.
- 🎯 **Por qué importa:** La pérdida de espacio libre domina cualquier presupuesto de enlace de espacio profundo y fija la potencia, la ganancia y el tiempo de ida y vuelta que tendrá una misión. La decisión central: ¿cuántos decibelios se pierden entre transmisor y receptor y cuánto tarda la señal en llegar?

📘 **Dónde se aprende** (2 clases): [B89-C04 · Propagación y pérdidas de espacio libre](../programa/clases/B89/B89-C04-propagacion-y-perdidas-de-espacio-libre/CLASE.md); [B104-C08 · Comunicación de tripulación](../programa/clases/B104/B104-C08-comunicacion-de-tripulacion/CLASE.md).

### Retardo de marea

- El retardo de marea es el adelanto del abultamiento respecto al satélite.

🎯 **Por qué importa (clase B72-C16):** La marea alarga el día, aleja a la Luna y calienta a Ío y Europa; en un satélite bajo el radio síncrono (como Fobos) hace lo contrario y lo acerca. La decisión central: ¿hacia dónde y a qué velocidad cambia el semieje por la marea, según esté el satélite dentro o fuera del radio síncrono?

📘 **Dónde se aprende** (1 clase): [B72-C16 · Modelado de mareas](../programa/clases/B72/B72-C16-modelado-de-mareas/CLASE.md).

### Retardo de propagación

- Retardo de propagación: `d n / c`.
- MOC/SOC: centros de operaciones de misión y científicas. Retardo de propagación: `d/c`.

💡 **Cómo se explica en la clase [B48-C09](../programa/clases/B48/B48-C09-control-remoto-de-telescopios/CLASE.md):**
- Calcular el retardo de propagación en una fibra.
- 🎯 **Por qué importa:** Un vigilante muy sensible detiene la observación sin motivo y uno muy lento no protege. La decisión central: ¿tras cuántos latidos perdidos hay que disparar la parada?

📘 **Dónde se aprende** (2 clases): [B48-C09 · Control remoto de telescopios](../programa/clases/B48/B48-C09-control-remoto-de-telescopios/CLASE.md); [B96-C01 · Segmento espacial y segmento terrestre](../programa/clases/B96/B96-C01-segmento-espacial-y-segmento-terrestre/CLASE.md).

### Retardo de Shapiro

- El retardo de Shapiro es el retraso de una señal que pasa cerca de una masa.
- El retardo de Shapiro es el retraso de la señal al pasar cerca de la compañera.

💡 **Cómo se explica en la clase [B27-C03](../programa/clases/B27/B27-C03-estrellas-de-neutrones/CLASE.md):**
- El púlsar PSR J0740+6620 tiene `2,14 (+0,10/−0,09) M☉` por el retardo de Shapiro (S3, resumen);
- 🎯 **Por qué importa:** Las masas y radios de las estrellas de neutrones son la mejor ventana a la materia a densidades nucleares. Para interpretarlos hay que saber qué cambia la relatividad respecto de Newton y por qué existe una masa máxima.

📘 **Dónde se aprende** (2 clases): [B27-C03 · Estrellas de neutrones](../programa/clases/B27/B27-C03-estrellas-de-neutrones/CLASE.md); [B27-C05 · Púlsares y relojes naturales](../programa/clases/B27/B27-C05-pulsares-y-relojes-naturales/CLASE.md).

### Retardo dispersivo

- El retardo dispersivo `τ = K TEC/(c ν²)`.

💡 **Cómo se explica en la clase [B51-C05](../programa/clases/B51/B51-C05-efectos-ionosfericos-en-radioastronomia-retardo-rotacion-de-faraday-y-su-correccion/CLASE.md):**
- El retardo es dispersivo con una sola incógnita; el RM suma una fase periódica con ambigüedad `nπ`.
- 🎯 **Por qué importa:** A frecuencias bajas la ionosfera domina el error de fase y de polarización. La decisión central: ¿cómo se mide y se quita el efecto con las propias frecuencias de la observación?

📘 **Dónde se aprende** (1 clase): [B51-C05 · Efectos ionosféricos en radioastronomía: retardo, rotación de Faraday y su corrección](../programa/clases/B51/B51-C05-efectos-ionosfericos-en-radioastronomia-retardo-rotacion-de-faraday-y-su-correccion/CLASE.md).

### Retardo entero

- El retardo entero y el fraccionario.

💡 **Cómo se explica en la clase [B51-C08](../programa/clases/B51/B51-C08-compensacion-de-retardo-y-alineacion-temporal-de-flujos-de-antenas/CLASE.md):**
- *Descripción textual:* la correlación da el entero; dos métodos independientes dan la fracción; una rampa de fase aplica el retardo completo.
- Con dos flujos de 4096 muestras, un retardo verdadero de 37,30 muestras (sintético) y relaciones señal-ruido de 1,0 y 2,0, el entero es 37, la parábola da 37,2094 y la pendiente de fase 37,2757.
- ⚠️ **Error frecuente:** Quedarse con el retardo entero. Se corrige con 8.2.
- 🎯 **Por qué importa:** Un retardo mal compensado reduce la coherencia y en VLBI hace perder la detección. La decisión central: ¿cómo se estima y se aplica un retardo con fracción de muestra y qué correlación se espera tras alinear?

📘 **Dónde se aprende** (1 clase): [B51-C08 · Compensación de retardo y alineación temporal de flujos de antenas](../programa/clases/B51/B51-C08-compensacion-de-retardo-y-alineacion-temporal-de-flujos-de-antenas/CLASE.md).

### Retardo geométrico

- El retardo geométrico `τ = B·ŝ/c`.

💡 **Cómo se explica en la clase [B51-C09](../programa/clases/B51/B51-C09-fringe-stopping-y-rotacion-de-fase-por-retardo-geometrico/CLASE.md):**
- Con `B = 1000` m, `δ = 30°` y `ν = 1,4` GHz, el retardo geométrico máximo es 2,8887 µs y la tasa de franjas en `H = 0` es -0,294911 Hz.
- B = 1000 m ; dec = 30 grados ; nu = 1.4 GHz ; retardo geometrico maximo = 2.8887 us
- 🎯 **Por qué importa:** Si se promedia sin detener las franjas, la señal se anula. La decisión central: ¿qué tasa de franjas tiene una fuente, cuánto se pierde al promediar y qué precisión pide el modelo?

📘 **Dónde se aprende** (2 clases): [B46-C14 · Líneas de base interferométricas](../programa/clases/B46/B46-C14-lineas-de-base-interferometricas/CLASE.md); [B51-C09 · Fringe stopping y rotación de fase por retardo geométrico](../programa/clases/B51/B51-C09-fringe-stopping-y-rotacion-de-fase-por-retardo-geometrico/CLASE.md).

### Retardo instrumental

- El retardo instrumental es el tiempo que la señal tarda en los equipos.

💡 **Cómo se explica en la clase [B74-C03](../programa/clases/B74/B74-C03-medicion-de-alcance-por-radio/CLASE.md):**
- Paso 4 · Lectura. El ruido del receptor es solo una parte del error: el retardo instrumental y la troposfera suelen dominar (clase C05).
- 🎯 **Por qué importa:** Un nanosegundo son quince centímetros de alcance, y un pulso ancho en ruido se mide con nanosegundos de incertidumbre. La decisión central: ¿cuánta precisión de alcance permite el ancho de banda y la relación señal/ruido, y qué hay que corregir además del retardo?

📘 **Dónde se aprende** (1 clase): [B74-C03 · Medición de alcance por radio](../programa/clases/B74/B74-C03-medicion-de-alcance-por-radio/CLASE.md).

### Retardo ionosférico

- El retardo ionosférico es proporcional al TEC y a `1/f²`.
- El retardo ionosférico `K TEC/(c ν²)`.

💡 **Cómo se explica en la clase [B51-C10](../programa/clases/B51/B51-C10-retardo-troposferico-e-ionosferico-en-vlbi-y-su-modelado/CLASE.md):**
- *Descripción textual:* el retardo troposférico se mapea con la elevación y el ionosférico se elimina con dos frecuencias.
- Calcular el retardo ionosférico con la `K` derivada de NIST.
- 🎯 **Por qué importa:** Un error atmosférico de centímetros es un error de posición en geodesia y un error de fase en imagen. La decisión central: ¿cómo se mapea el retardo con la elevación y cómo se separa lo dispersivo de lo no dispersivo?

📘 **Dónde se aprende** (2 clases): [B51-C10 · Retardo troposférico e ionosférico en VLBI y su modelado](../programa/clases/B51/B51-C10-retardo-troposferico-e-ionosferico-en-vlbi-y-su-modelado/CLASE.md); [B57-C29 · Correcciones atmosféricas en altimetría](../programa/clases/B57/B57-C29-correcciones-atmosfericas-en-altimetria/CLASE.md).

### Retardo ionosférico de grupo

- El retardo ionosférico de grupo de primer orden es `Δ = 40,3·TEC/f²` (m, con TEC en el/m² y `f` en Hz).

💡 **Cómo se explica en la clase [B89-C21](../programa/clases/B89/B89-C21-efectos-ionosfericos-y-centelleo-en-senales-gnss/CLASE.md):**
- ⚠️ **Error frecuente:** Aplicar el retardo ionosférico como de fase en vez de grupo. Se corrige con el vocabulario: aquí es de grupo (el de fase tiene signo opuesto).
- 🎯 **Por qué importa:** La ionosfera es el mayor error de un receptor GNSS de una sola frecuencia y el origen de pérdidas de señal en regiones ecuatoriales y polares; sin entenderla no se puede interpretar un error de posición. La decisión central: ¿cuánto error añade la ionosfera, cómo se elimina y cuándo el centelleo hace perder la señal?

📘 **Dónde se aprende** (1 clase): [B89-C21 · Efectos ionosféricos y centelleo en señales GNSS](../programa/clases/B89/B89-C21-efectos-ionosfericos-y-centelleo-en-senales-gnss/CLASE.md).

### Retardo residual

- El retardo residual `τ₀`: pendiente de fase.

💡 **Cómo se explica en la clase [B51-C04](../programa/clases/B51/B51-C04-respuesta-de-banda-y-errores-dependientes-de-la-frecuencia/CLASE.md):**
- Con 256 canales sobre 128 MHz, un retardo residual inyectado de 3,0 ns y una reflexión de amplitud 0,05 a 40 ns (todo sintético), el ajuste da 3,0213 ns sin ruido y la ondulación aparece con periodo de 25,0 MHz.
- 🎯 **Por qué importa:** Un error de banda aparece en las líneas espectrales como una falsa estructura y limita el rango dinámico del continuo. La decisión central: ¿qué parte del error de banda es un retardo, qué parte una ondulación, y con qué precisión se miden?

📘 **Dónde se aprende** (1 clase): [B51-C04 · Respuesta de banda y errores dependientes de la frecuencia](../programa/clases/B51/B51-C04-respuesta-de-banda-y-errores-dependientes-de-la-frecuencia/CLASE.md).

### Retardo S−P

- El retardo S−P es la diferencia entre las llegadas de la onda S y la onda P.

💡 **Cómo se explica en la clase [B63-C01](../programa/clases/B63/B63-C01-instrumentacion-de-sondas-y-rovers-planetarios/CLASE.md):**
- Las ondas P y S salen juntas del foco y llegan con un retardo `Δt = d/vs − d/vp`.
- Con `vp = 5,0` y `vs = 2,9 km/s`, el factor vale `6,905 km/s`: un retardo de `30 s` da `207,14 km`.
- ⚠️ **Error frecuente:** Usar el retardo como distancia. La distancia es retardo por un factor de velocidades.
- 🎯 **Por qué importa:** Un rover no puede volver a medir lo que midió mal. Antes de elegir qué observar hay que saber qué puede resolver cada instrumento.

📘 **Dónde se aprende** (1 clase): [B63-C01 · Instrumentación de sondas y rovers planetarios](../programa/clases/B63/B63-C01-instrumentacion-de-sondas-y-rovers-planetarios/CLASE.md).

### Retardo total τ

- Retardo total `τ`: reacción más comunicación.

💡 **Cómo se explica en la clase [B101-C10](../programa/clases/B101/B101-C10-simulacion-de-una-tarea-tripulada-con-manipulador/CLASE.md):**
- Ejercicio 9 · transferencia. Transferencia. El retardo total son la reacción y la comunicación.
- 🎯 **Por qué importa:** Cuanto más tarda en llegar la imagen y la orden, más difícil es corregir. La decisión central: ¿con qué retardo total y qué ganancia el operador puede capturar con éxito y cuándo conviene pasar a «mover y esperar»?

📘 **Dónde se aprende** (1 clase): [B101-C10 · Simulación de una tarea tripulada con manipulador](../programa/clases/B101/B101-C10-simulacion-de-una-tarea-tripulada-con-manipulador/CLASE.md).

### Retardo troposférico seco (hidrostático)

- El retardo troposférico seco (hidrostático) es casi proporcional a la presión de superficie.

🎯 **Por qué importa (clase B57-C29):** Un error de decímetros en la distancia equivale a decímetros de error en la altura del mar, mayor que las señales que se buscan. La decisión central: ¿qué corrección aplicar a cada retardo y cuánto ruido agrega?

📘 **Dónde se aprende** (1 clase): [B57-C29 · Correcciones atmosféricas en altimetría](../programa/clases/B57/B57-C29-correcciones-atmosfericas-en-altimetria/CLASE.md).

### Retardo unidireccional

- El retardo unidireccional es `d/c`.

💡 **Cómo se explica en la clase [B75-C19](../programa/clases/B75/B75-C19-restricciones-de-navegacion-autonoma/CLASE.md):**
- En el modelo, la distancia Tierra–Marte va de `78,36` a `377,55×10⁶ km`; el retardo unidireccional de `4,36` a `20,99 min` (medio `14,08 min`) y el de ida y vuelta de `8,71` a `41,98 min`.
- Predice antes de ejecutar: ¿Cuál es el retardo unidireccional medio?
- ⚠️ **Error frecuente:** Confundir retardo unidireccional con RTLT. Se corrige con la sección 6.
- 🎯 **Por qué importa:** No se puede dirigir desde la Tierra lo que sucede en minutos. La decisión central: ¿qué eventos duran menos que el tiempo mínimo de reacción desde tierra y por tanto deben ser autónomos?

📘 **Dónde se aprende** (1 clase): [B75-C19 · Restricciones de navegación autónoma](../programa/clases/B75/B75-C19-restricciones-de-navegacion-autonoma/CLASE.md).

### Retención

- La retención («hold and review») es mantener la muestra contenida mientras se revisa.
- La retención `r` es la probabilidad de que un elemento sobreviva correcto una generación.
- La retención `A` (< 1 olvida) y la sensibilidad al error `B` fijan la tasa `λ = A − B` y el estado estacionario `x* = B p/(1 − A + B)`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B105-C25](../programa/clases/B105/B105-C25-adaptacion-sensoriomotora-y-control-motor-en-microgravedad/CLASE.md):**
- *Descripción textual:* el error entre la perturbación y el estado actualiza el estado con una retención y una sensibilidad; el estado converge a un estado estacionario y deja un postefecto al retirar la perturbación.
- Un modelo con `A = 0,95` (retención) y `B = 0,20` (sensibilidad al error) enfrenta una perturbación de 30° durante 40 ensayos y luego 40 ensayos de lavado.
- 🎯 **Por qué importa:** Quien se adapta a un entorno nuevo comete errores al volver al anterior. Entender el ritmo de adaptación y el postefecto permite diseñar el entrenamiento y anticipar las torpezas.

📘 **Dónde se aprende** (4 clases): [B63-C06 · Evaluación de riesgos biológicos de muestras: marcos de decisión](../programa/clases/B63/B63-C06-evaluacion-de-riesgos-biologicos-de-muestras-marcos-de-decision/CLASE.md); [B105-C25 · Adaptación sensoriomotora y control motor en microgravedad](../programa/clases/B105/B105-C25-adaptacion-sensoriomotora-y-control-motor-en-microgravedad/CLASE.md); [B106-C11 · Almacenamiento de alimentos](../programa/clases/B106/B106-C11-almacenamiento-de-alimentos/CLASE.md); [B133-C02 · Narrativas orales y transmisión del saber del cielo](../programa/clases/B133/B133-C02-narrativas-orales-y-transmision-del-saber-del-cielo/CLASE.md).

### Retenedor de orden cero

- Un retenedor de orden cero (ZOH) mantiene la entrada constante entre dos muestras.

💡 **Cómo se explica en la clase [B16-C02](../programa/clases/B16/B16-C02-representaciones-en-espacio-de-estados/CLASE.md):**
- Discretizar un modelo continuo con retenedor de orden cero y justificar el paso `T`.
- 🎯 **Por qué importa:** El computador de a bordo de un satélite no maneja ecuaciones sueltas: maneja vectores y matrices, y una sola rutina sirve para cualquier eje, rueda o sensor que se le añada.

📘 **Dónde se aprende** (1 clase): [B16-C02 · Representaciones en espacio de estados](../programa/clases/B16/B16-C02-representaciones-en-espacio-de-estados/CLASE.md).

### Reticulado

- El reticulado es el conjunto de combinaciones de niveles de generalización.

💡 **Cómo se explica en la clase [B124-C13](../programa/clases/B124/B124-C13-etica-de-investigacion-y-datos/CLASE.md):**
- El ejemplo conductor es un conjunto sintético de 300 participantes: sin generalizar, `300` registros (`100,0%`) son únicos y por tanto reidentificables; el mejor nodo del reticulado logra `k = 5` con `11` supresiones.
- Explorar un reticulado de generalizaciones de forma exhaustiva.
- 🎯 **Por qué importa:** Abrir datos sin proteger a las personas es un daño, y proteger sin medir es una promesa vacía. La decisión central: ¿cuánto generalizar los datos para que ninguna persona sea identificable y cuánta información se pierde?

📘 **Dónde se aprende** (1 clase): [B124-C13 · Ética de investigación y datos](../programa/clases/B124/B124-C13-etica-de-investigacion-y-datos/CLASE.md).

### Retirada

- La retirada del consentimiento detiene el uso posterior de los datos de esa persona.

💡 **Cómo se explica en la clase [B129-C05](../programa/clases/B129/B129-C05-consentimiento-y-privacidad-de-participantes/CLASE.md):**
- Llevar un registro de consentimiento con estado por defecto «sin consentimiento» y retirada efectiva.
- 🎯 **Por qué importa:** Cuando un conjunto de datos se publica o se comparte, los datos de las personas pueden permitir reconocerlas aunque se quite el nombre. La decisión central: ¿qué recoger, con qué precisión publicarlo y cómo respetar que alguien retire su consentimiento?

📘 **Dónde se aprende** (1 clase): [B129-C05 · Consentimiento y privacidad de participantes](../programa/clases/B129/B129-C05-consentimiento-y-privacidad-de-participantes/CLASE.md).

### Retorno

- El retorno ocurre cuando la nave y la Tierra coinciden de nuevo.

💡 **Cómo se explica en la clase [B75-C25](../programa/clases/B75/B75-C25-resonancias-para-sobrevuelos/CLASE.md):**
- La ficha de la ESA indica que Juice usa asistencias de la Luna–Tierra, Venus y la Tierra [S2]; si usa retornos resonantes no se consultó.
- La evidencia es tu tabla de resonancias de retorno del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Para volver a un planeta hay que llegar a la misma posición un número entero de años después. La decisión central: ¿qué resonancias `k:m` son alcanzables con un `v∞` dado y cuánto `v∞` hace falta para las demás?

📘 **Dónde se aprende** (1 clase): [B75-C25 · Resonancias para sobrevuelos](../programa/clases/B75/B75-C25-resonancias-para-sobrevuelos/CLASE.md).

### Retorno científico

- El retorno científico es el tiempo en modo nominal.

🎯 **Por qué importa (clase B86-C21):** Cuando la energía escasea, apagar la carga útil a tiempo mantiene viva la nave. Un umbral único hace oscilar al sistema entre modos; la histéresis lo evita.

📘 **Dónde se aprende** (1 clase): [B86-C21 · Modos de operación y estados de bajo consumo](../programa/clases/B86/B86-C21-modos-de-operacion-y-estados-de-bajo-consumo/CLASE.md).

### Retorno radial

- El retorno radial corrige la tensión de prueba elástica al límite de fluencia actual.

💡 **Cómo se explica en la clase [B84-C25](../programa/clases/B84/B84-C25-comportamiento-estructural-no-lineal-plasticidad-y-contacto/CLASE.md):**
- El script [nolineal.py](nolineal.py) integra un ciclo elastoplástico con retorno radial y resuelve un contacto con Newton (comprueba `σ` monotónica frente a analítica (< 1e-9) y `u` de contacto exacta).
- 🎯 **Por qué importa:** Un modelo lineal da tensiones de 400 MPa en un material que cedió a 275: el resultado correcto es una deformación permanente y una tensión residual que solo el análisis no lineal muestra. La decisión central: ¿qué deformación permanente y tensión residual deja una carga que excede el límite elástico, y cuándo actúa un contacto?

📘 **Dónde se aprende** (1 clase): [B84-C25 · Comportamiento estructural no lineal: plasticidad y contacto](../programa/clases/B84/B84-C25-comportamiento-estructural-no-lineal-plasticidad-y-contacto/CLASE.md).

### Retorno restringido

- La Categoría V agrupa las misiones de retorno a la Tierra. «Retorno restringido» es la subcategoría de mayor preocupación.

💡 **Cómo se explica en la clase [B63-C04](../programa/clases/B63/B63-C04-misiones-de-retorno-de-muestras-salvaguardas-historicas-y-regulatorias/CLASE.md):**
- Según S1, para el retorno restringido: (1) se prohíbe de forma absoluta el impacto destructivo al regresar;
- Enumerar las exigencias de contención y las revisiones de un retorno restringido.
- 🎯 **Por qué importa:** Traer material de otro cuerpo exige proteger a la Tierra y a la muestra. La decisión central: ¿cuántas barreras independientes hacen falta, y qué pasa si dejan de ser independientes?

📘 **Dónde se aprende** (1 clase): [B63-C04 · Misiones de retorno de muestras: salvaguardas históricas y regulatorias](../programa/clases/B63/B63-C04-misiones-de-retorno-de-muestras-salvaguardas-historicas-y-regulatorias/CLASE.md).

### Retrabajo

- Pasada hacia atrás: calcula fin (`LF`) e inicio (`LS`) más tardíos. Retrabajo: corregir un producto no conforme.

💡 **Cómo se explica en la clase [B90-C01](../programa/clases/B90/B90-C01-plan-de-ensamblaje-e-integracion/CLASE.md):**
- Si la prueba funcional H falla, hay que añadir retrabajo (3 d) y repetirla (2 d).
- Límite: una receta no tiene fallas que obliguen a repetir un paso; el plan sí debe prever retrabajo.
- ⚠️ **Error frecuente:** Planificar sin retrabajo. Reserva contingencia (8.4)
- 🎯 **Por qué importa:** La integración es la fase donde los errores de diseño se vuelven visibles y caros. Un plan que no distingue las tareas críticas de las que tienen holgura gasta esfuerzo en el lugar equivocado.

📘 **Dónde se aprende** (1 clase): [B90-C01 · Plan de ensamblaje e integración](../programa/clases/B90/B90-C01-plan-de-ensamblaje-e-integracion/CLASE.md).

### Retransmisión

- Completitud: fracción recibida. Retransmisión: reenvío de faltantes.

💡 **Cómo se explica en la clase [B96-C16](../programa/clases/B96/B96-C16-gestion-de-datos-cientificos/CLASE.md):**
- Descripción larga: cada retransmisión multiplica los faltantes por `p = 0,03`; en tres pasadas el conjunto queda completo.
- Simular la retransmisión de faltantes en pasadas sucesivas.
- 🎯 **Por qué importa:** Un conjunto de datos con huecos no declarados da conclusiones erróneas, y una retransmisión sin plan agota los contactos. La decisión central: ¿qué falta, cuántas pasadas hacen falta para completarlo y qué producto se entrega en cada nivel?

📘 **Dónde se aprende** (1 clase): [B96-C16 · Gestión de datos científicos](../programa/clases/B96/B96-C16-gestion-de-datos-cientificos/CLASE.md).

### Retraso

- El retraso es el tiempo hasta la primera alarma tras el cambio.

💡 **Cómo se explica en la clase [B105-C09](../programa/clases/B105/B105-C09-salud-mental-en-aislamiento/CLASE.md):**
- Subir `h` baja las falsas alarmas y alarga el retraso.
- A --> M["falsas alarmas,<br/>deteccion, retraso"]
- 🎯 **Por qué importa:** Un umbral bajo detecta pronto pero alarma de más; uno alto alarma poco pero tarda. Con una tripulación pequeña, las falsas alarmas se acumulan.

📘 **Dónde se aprende** (1 clase): [B105-C09 · Salud mental en aislamiento](../programa/clases/B105/B105-C09-salud-mental-en-aislamiento/CLASE.md).

### Retraso de detección

- El retraso de detección es el tiempo entre el inicio del evento (dos anchos antes del centro) y la alarma; una alarma anterior al inicio es una falsa alarma.

💡 **Cómo se explica en la clase [B97-C22](../programa/clases/B97/B97-C22-deteccion-autonoma-de-eventos-cientificos/CLASE.md):**
- Calcular la probabilidad y el retraso de detección de un evento pequeño y uno grande.
- 🎯 **Por qué importa:** Un detector sensible produce falsas alarmas que consumen enlace y energía; uno estricto pierde eventos. La clave es medir ambos efectos con una referencia (ARL₀) y comparar métodos con el mismo costo de falsas alarmas.

📘 **Dónde se aprende** (1 clase): [B97-C22 · Detección autónoma de eventos científicos](../programa/clases/B97/B97-C22-deteccion-autonoma-de-eventos-cientificos/CLASE.md).

### Retraso geométrico

- El retraso geométrico es `Δt = n·Δr/c` para un desplazamiento `Δr` respecto de la referencia.

🎯 **Por qué importa (clase B74-C27):** La idea atrae porque sería autónoma, sin estaciones; la pregunta honesta es cuánta precisión da con una cantidad realista de fotones. La decisión central: ¿cuánto tiempo de observación y cuántos púlsares hacen falta para una cierta precisión, y qué parte de la técnica sigue sin demostrarse en esta clase?

📘 **Dónde se aprende** (1 clase): [B74-C27 · Navegación por púlsares de rayos X como técnica de investigación](../programa/clases/B74/B74-C27-navegacion-por-pulsares-de-rayos-x-como-tecnica-de-investigacion/CLASE.md).

### Retraso por masa

- El retraso por masa `Δt = (d/c)(1 − β)/β`.
- El retraso por masa afecta a partículas con masa en reposo.

💡 **Cómo se explica en la clase [B27-C18](../programa/clases/B27/B27-C18-neutrinos-de-supernova/CLASE.md):**
- *Descripción textual:* de la energía y la energía media se obtiene el número de neutrinos y su fluencia; con la sección eficaz y los protones del detector, los sucesos; el retraso por masa se calcula con una forma algebraica estable.
- Calcular el retraso por masa de forma estable.
- 🎯 **Por qué importa:** Los neutrinos de una supernova galáctica serían una señal de cientos de sucesos en unos segundos, mensajera del interior de la estrella. La decisión central: ¿cuántos neutrinos llegan, qué retraso produce su masa y cómo se calcula sin perder precisión?

📘 **Dónde se aprende** (2 clases): [B27-C18 · Neutrinos de supernova](../programa/clases/B27/B27-C18-neutrinos-de-supernova/CLASE.md); [B28-C01 · Fundamentos de mensajeros astronómicos](../programa/clases/B28/B28-C01-fundamentos-de-mensajeros-astronomicos/CLASE.md).

### Retraso S−P

- El retraso S−P es `t_S − t_P`.

💡 **Cómo se explica en la clase [B53-C02](../programa/clases/B53/B53-C02-sismologia-planetaria/CLASE.md):**
- Analogía: el trueno y el relámpago: la luz llega antes que el sonido, y el retraso dice a qué distancia cayó el rayo.
- T --> D["distancia = retraso / (1/vs - 1/vp)"]
- 🎯 **Por qué importa:** Un solo sismómetro no da la posición completa de un evento. La decisión central: ¿cuánto vale la distancia al evento y con qué incertidumbre, si solo se leen los tiempos de llegada P y S?

📘 **Dónde se aprende** (1 clase): [B53-C02 · Sismología planetaria](../programa/clases/B53/B53-C02-sismologia-planetaria/CLASE.md).

### Retroalimentación estelar

- La retroalimentación estelar es el efecto de las estrellas sobre el gas que las rodea: calentamiento, empuje y enriquecimiento.

💡 **Cómo se explica en la clase [B25-C16](../programa/clases/B25/B25-C16-retroalimentacion-estelar/CLASE.md):**
- Ejercicio 12 · integrador. Elabora la *ficha de presupuesto de retroalimentación*: elige una galaxia (sintética) con `σ` y gas; calcula supernovas por `M☉`, `E_b`, supernovas necesarias, masa estelar, fracción del gas y la sensibilidad a `ε`; indica qué parámetros son convencionales.
- El script [retroalimentacion.py](retroalimentacion.py) calcula las supernovas por masa, la energía de ligadura, la masa estelar necesaria y la burbuja.
- 🎯 **Por qué importa:** Sin retroalimentación, el gas de una galaxia se convertiría en estrellas mucho más deprisa de lo observado. Las supernovas, los vientos y la radiación de las estrellas masivas calientan y expulsan gas, y lo enriquecen con metales (C17).

📘 **Dónde se aprende** (1 clase): [B25-C16 · Retroalimentación estelar](../programa/clases/B25/B25-C16-retroalimentacion-estelar/CLASE.md).

### Retroceso

- El retroceso propaga con `−t`.

🎯 **Por qué importa (clase B71-C20):** Un propagador que «parece funcionar» puede tener un error de tiempo que ningún invariante detecta. La decisión central: ¿qué pruebas, con qué tolerancias y contra qué referencia independiente demuestran que el propagador es correcto?

📘 **Dónde se aprende** (1 clase): [B71-C20 · Propagador kepleriano verificable](../programa/clases/B71/B71-C20-propagador-kepleriano-verificable/CLASE.md).

### Retroceso nuclear

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B36-C10):** Un límite de sección eficaz depende de la cinemática, de la exposición y de las cuentas. La decisión central: ¿qué sección eficaz excluye una exposición sin sucesos?

📘 **Dónde se aprende** (1 clase): [B36-C10 · Búsqueda directa de materia oscura en laboratorio](../programa/clases/B36/B36-C10-busqueda-directa-de-materia-oscura-en-laboratorio/CLASE.md).

### Retrodicción

- La retrodicción propaga el estado hacia atrás: `x_m = F⁻ˡ x_k`.

💡 **Cómo se explica en la clase [B74-C24](../programa/clases/B74/B74-C24-medidas-retardadas-y-fuera-de-secuencia-en-filtros-de-estimacion/CLASE.md):**
- *Descripción textual:* una medida con sello anterior al estado actual puede descartarse, usarse como actual, tratarse con retrodicción aproximada o reprocesarse; cada tratamiento se evalúa con rms, NEES y validez de la covarianza.
- Paso 3 · Retrodicción. `x_m = F⁻⁵ x_k`; con la matriz de movimiento uniforme, la posición retrocede `5 v`.
- 🎯 **Por qué importa:** Una medida tardía contiene información valiosa pero tratarla mal puede dañar más que descartarla. La decisión central: ¿qué tratamiento de una medida tardía mejora el estimado sin romper la consistencia, y a qué coste?

📘 **Dónde se aprende** (1 clase): [B74-C24 · Medidas retardadas y fuera de secuencia en filtros de estimación](../programa/clases/B74/B74-C24-medidas-retardadas-y-fuera-de-secuencia-en-filtros-de-estimacion/CLASE.md).

### Retrodispersión Rayleigh

- La capa de sodio y la retrodispersión Rayleigh.

💡 **Cómo se explica en la clase [B42-C17](../programa/clases/B42/B42-C17-estrellas-guia-artificiales/CLASE.md):**
- La retrodispersión Rayleigh a 10 km tiene densidad relativa `0,2865` (altura de escala 8 km, ilustrativa) y el ultravioleta (355 nm) dispersa `5,04` veces más que 532 nm (`λ⁻⁴`).
- 🎯 **Por qué importa:** Sin estrella guía no hay corrección en casi todo el cielo. La decisión central: ¿a qué altitud conviene crear la estrella y qué error de cono y qué elongación trae?

📘 **Dónde se aprende** (1 clase): [B42-C17 · Estrellas guía artificiales](../programa/clases/B42/B42-C17-estrellas-guia-artificiales/CLASE.md).

### Retrógrada

- Una órbita es directa si `i < 90°` y retrógrada si `i > 90°`.
- Prógrada es `i < 90°`; retrógrada, `i > 90°`.
- Una transferencia es prógrada si `n` apunta hacia el eje de referencia `+z` (`h_z > 0`) y retrógrada si apunta hacia `−z`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C14](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md):**
- La componente `z` es `cos i`: positiva si `i < 90°` (directa) y negativa si `i > 90°` (retrógrada).
- E -->|"< 0"| G["Órbita retrógrada (i > 90°)"]
- 🎯 **Por qué importa:** Una órbita no es solo una forma (C09): es una forma colocada en el espacio con una orientación. ¿Hacia dónde apunta su plano?

📘 **Dónde se aprende** (6 clases): [B04-C14 · Producto vectorial y orientación](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md); [B27-C07 · Métricas de agujeros negros](../programa/clases/B27/B27-C07-metricas-de-agujeros-negros/CLASE.md); [B52-C11 · Formación de satélites naturales](../programa/clases/B52/B52-C11-formacion-de-satelites-naturales/CLASE.md); [B71-C11 · Inclinación y nodo ascendente](../programa/clases/B71/B71-C11-inclinacion-y-nodo-ascendente/CLASE.md); [B76-C03 · Órbitas alrededor de la Luna](../programa/clases/B76/B76-C03-orbitas-alrededor-de-la-luna/CLASE.md); [B82-C02 · Lambert de arco largo](../programa/clases/B82/B82-C02-lambert-de-arco-largo/CLASE.md).

### Reunión

- La difusión (*broadcast*) copia un dato del proceso raíz a todos; el reparto (*scatter*) divide una colección de la raíz entre los procesos; la reunión (*gather*) hace lo contrario; la reducción (*reduce*) combina valores de todos con una operación (suma, máximo…) y la deja en la raíz, y `allreduce` la deja en todos.

💡 **Cómo se explica en la clase [B18-C02](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md):**
- Elegir entre difusión, reparto, reunión y reducción para un patrón dado.
- El script [mensajes_mpi.py](mensajes_mpi.py) ejecuta, con cualquier número de procesos: un anillo con `sendrecv`, una difusión de parámetros, el cálculo de π con `reduce` y `allreduce`, el reparto y reunión de 4 órbitas por proceso, y un eco de 16 MB con objetos y con *buffers*.
- 🎯 **Por qué importa:** Ocho, cuarenta o cuatro mil núcleos de un clúster no comparten memoria. Para que cada uno propague su parte de un catálogo de órbitas y luego se junten los resultados, hay que decir quién envía qué a quién, y cuándo.

📘 **Dónde se aprende** (1 clase): [B18-C02 · Paso de mensajes con MPI](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md).

### Reunión de revisión

- La reunión de revisión es una conversación programada.

🎯 **Por qué importa (clase B104-C16):** Un conflicto abierto cuesta tiempo, errores y confianza; prevenirlo cuesta pequeñas conversaciones continuas. La decisión central: ¿cuánto reduce una intervención temprana la probabilidad de que la tensión llegue al conflicto abierto, frente a no hacer nada o reunirse una vez por semana?

📘 **Dónde se aprende** (1 clase): [B104-C16 · Manejo de conflictos](../programa/clases/B104/B104-C16-manejo-de-conflictos/CLASE.md).

### Reutilizable

- La lista de comprobación es un conjunto de reglas que se aplican al paquete. Reutilizable significa que otra persona puede usarlo legal y técnicamente.

🎯 **Por qué importa (clase B14-C19):** Subes tu código a un repositorio y tus datos a una carpeta compartida. Un año después, alguien quiere usarlos y no sabe si puede, cómo citarte, qué significan las columnas ni si el archivo es el que tú usaste.

📘 **Dónde se aprende** (1 clase): [B14-C19 · Publicación de código y datos](../programa/clases/B14/B14-C19-publicacion-de-codigo-y-datos/CLASE.md).

### Reutilización

- La reutilización reduce el precio efectivo.

💡 **Cómo se explica en la clase [B124-C23](../programa/clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md):**
- Con 550 000 kg de masa inicial, la carga útil es `13346` kg; a 60 Mum el costo es `4496` um/kg, y si la reutilización ahorra el 30 % del precio, `3147` um/kg.
- El descenso desde órbita baja (`Δv = 6 000 m/s`, `Isp` 340 s, `e = 0,12`) deja una fracción de `0,05157`, así que cada kilogramo en superficie exige `1/0,05157` kg en órbita: el costo sube a `87176` um/kg (`19,4` veces); con reutilización, `61024`.
- ⚠️ **Error frecuente:** Creer que la reutilización resuelve todo el costo. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** El costo por kilogramo a superficie no se puede leer en una lista de precios: depende de una cadena de fracciones de masa que se multiplican. La decisión central: ¿cuánto cuesta llevar un kilogramo a la superficie, de qué depende ese costo y qué lo hace más sensible?

📘 **Dónde se aprende** (1 clase): [B124-C23 · Costos de transporte por kilogramo a superficie](../programa/clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md).

### Reverberante

- El campo directo viene de la fuente; el reverberante, de los rebotes.

💡 **Cómo se explica en la clase [B109-C10](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md):**
- El nivel total es `59,2 dBA` a `1 m`, `56,6` a `2 m`, `55,9` a `3 m` y `55,5` a `5 m`; el campo reverberante da `55,2`.
- *Descripción textual:* las fuentes se suman en energía; el recinto aporta absorción y constante; el nivel en un punto mezcla campo directo y reverberante y se compara con el límite y el objetivo para decidir qué fuente bajar.
- 🎯 **Por qué importa:** El ruido continuo degrada la comunicación, el sueño y el trabajo aunque no dañe el oído. La decisión central: ¿qué fuente reduzco primero y cuánto baja el nivel de la cabina?

📘 **Dónde se aprende** (1 clase): [B109-C10 · Acústica y control de ruido interior](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md).

### Reversibilidad

- La reversibilidad es que el trazado de vuelta recupere el rayo de entrada.
- La reversibilidad de un método es `Φ_{−h} ∘ Φ_h = id`.
- La reversibilidad es poder volver al inicio con el mapa inverso.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B50-C06](../programa/clases/B50/B50-C06-software-de-diseno-optico-modelos-reproducibles-y-verificacion/CLASE.md):**
- Comprobar la reversibilidad del trazado.
- Ejercicio 6. ¿Cuál es la desviación de la reversibilidad?
- 🎯 **Por qué importa:** Los programas de diseño óptico son cajas con muchas opciones: lo que hace reproducible un diseño es el archivo, sus unidades, su versión y sus pruebas. La decisión central: ¿cómo se demuestra que un modelo sigue siendo el mismo y sigue dando lo mismo?

📘 **Dónde se aprende** (5 clases): [B50-C06 · Software de diseño óptico: modelos reproducibles y verificación](../programa/clases/B50/B50-C06-software-de-diseno-optico-modelos-reproducibles-y-verificacion/CLASE.md); [B73-C06 · Variedades invariantes](../programa/clases/B73/B73-C06-variedades-invariantes/CLASE.md); [B73-C09 · Integración de largo plazo](../programa/clases/B73/B73-C09-integracion-de-largo-plazo/CLASE.md); [B73-C13 · Caos determinista](../programa/clases/B73/B73-C13-caos-determinista/CLASE.md); [B75-C30 · Validación de maniobras por reintegración](../programa/clases/B75/B75-C30-validacion-de-maniobras-por-reintegracion/CLASE.md).

### Reversibilidad temporal

- Una reversibilidad temporal significa que avanzar y luego invertir la velocidad y avanzar vuelve al inicio.

🎯 **Por qué importa (clase B11-C11):** Para el sistema solar, anillos planetarios o constelaciones se necesitan integraciones de millones de vueltas. Un método que añade o quita un poco de energía en cada vuelta termina destruyendo la órbita.

📘 **Dónde se aprende** (1 clase): [B11-C11 · Métodos simplécticos](../programa/clases/B11/B11-C11-metodos-simplecticos/CLASE.md).

### Reversible

- Es reversible y conserva el volumen, pero no exactamente la energía: su error de energía `ΔH` escala como `ε²`.

💡 **Cómo se explica en la clase [B19-C03](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md):**
- Es *reversible*: si al final inviertes el signo del momento y repites `L` pasos, vuelves al punto inicial (el laboratorio lo comprueba a 10⁻¹⁰).
- 🎯 **Por qué importa:** Una posterior bidimensional con dos parámetros correlacionados al 95 % tiene forma de un óvalo muy alargado y estrecho. Un Metropolis de paso aleatorio, para no salirse del óvalo, da pasos minúsculos y recorre la distribución a paso de tortuga.

📘 **Dónde se aprende** (1 clase): [B19-C03 · Hamiltonian Monte Carlo y NUTS](../programa/clases/B19/B19-C03-hamiltonian-monte-carlo-y-nuts/CLASE.md).

### Reversible en el tiempo

- Un método es reversible en el tiempo si, tras avanzar `N` pasos, invertir la velocidad y avanzar otros `N` pasos devuelve el estado inicial.

💡 **Cómo se explica en la clase [B23-C02](../programa/clases/B23/B23-C02-pruebas-de-propiedades-fisicas/CLASE.md):**
- RK4 (orden 4) da errores de energía mucho menores a corto plazo (`2,7 × 10⁻⁹` frente a `5,0 × 10⁻⁶` con `h = 1 d` en 10 años) pero no es reversible ni conserva `L` exactamente, y su error de energía crece con el tiempo.

📘 **Dónde se aprende** (1 clase): [B23-C02 · Pruebas de propiedades físicas](../programa/clases/B23/B23-C02-pruebas-de-propiedades-fisicas/CLASE.md).

### Reversión

- Una reversión (*rollback*) restaura la anterior.

💡 **Cómo se explica en la clase [B88-C13](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md):**
- (4) imagen buena que no arranca → 3 arranques fallidos y reversión a A.
- Ejercicio 5 · autónomo. ¿Cuántos arranques fallidos provocan la reversión del caso 4?
- 🎯 **Por qué importa:** Una actualización fallida en órbita no se arregla con un cable. La decisión central: ¿qué comprobaciones aceptan solo la imagen correcta y qué mecanismo vuelve a una versión conocida si la nueva no arranca?

📘 **Dónde se aprende** (1 clase): [B88-C13 · Actualización segura de software](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md).

### Revisión por pares

- La revisión por pares (o arbitraje) es la evaluación de un manuscrito por especialistas independientes antes de su publicación.

💡 **Cómo se explica en la clase [B20-C03](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md):**
- La lección: la revisión por pares tiene reglas de conducta para las tres partes.
- Describir las funciones de autor, árbitro y editor en la revisión por pares y sus deberes de confidencialidad y de declaración de conflictos.
- 🎯 **Por qué importa:** Una crítica recibida a las once de la noche se lee con el estómago antes que con la cabeza. La reacción inmediata, defenderse o rendirse, suele empeorar el trabajo y la relación con quien revisa.

📘 **Dónde se aprende** (1 clase): [B20-C03 · Revisión por pares y respuesta a árbitros](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md).

### Revisita

- La revisita es el intervalo entre observaciones de un punto, que puede ser menor que el ciclo si los barridos se solapan o hay varios satélites.

💡 **Cómo se explica en la clase [B57-C23](../programa/clases/B57/B57-C23-diseno-de-orbita-y-revisita-para-observacion-terrestre/CLASE.md):**
- La revisita real es menor que el ciclo si los barridos de trazas vecinas se solapan en latitudes altas o si hay varios satélites.
- Por constelación: menor revisita con más satélites.
- ⚠️ **Error frecuente:** Confundir ciclo con revisita. Pueden diferir (8.4).
- 🎯 **Por qué importa:** Si la órbita no repite sus trazas o el barrido no cubre el espacio entre ellas, quedan huecos. La decisión central: ¿qué altitud e inclinación dan un ciclo de repetición que cubre todo con el barrido disponible?

📘 **Dónde se aprende** (1 clase): [B57-C23 · Diseño de órbita y revisita para observación terrestre](../programa/clases/B57/B57-C23-diseno-de-orbita-y-revisita-para-observacion-terrestre/CLASE.md).

### Rezago normativo

- El rezago normativo es el tiempo entre una tecnología y su regulación.

🎯 **Por qué importa (clase B119-C12):** Para leer el derecho vigente conviene saber qué contexto lo produjo; ninguna clase anterior da la cronología comparada entre la tecnología y los instrumentos jurídicos. La decisión central: ¿cuánto tardó el derecho en seguir a la tecnología y por qué importa distinguir fechas verificadas de fechas recordadas?

📘 **Dónde se aprende** (1 clase): [B119-C12 · Historia de competencia estratégica espacial](../programa/clases/B119/B119-C12-historia-de-competencia-estrategica-espacial/CLASE.md).

### Rica

- Una mezcla rica tiene exceso de combustible; una pobre, de oxidante.

💡 **Cómo se explica en la clase [B78-C05](../programa/clases/B78/B78-C05-propulsion-bipropelente-conceptual/CLASE.md):**
- Con disociación, la temperatura se achata cerca del estequiométrico y la menor masa molar de una mezcla rica pasa a ganar; por eso los motores de H₂/O₂ operan ricos.
- La disociación, que desplaza el óptimo hacia mezclas ricas.
- 🎯 **Por qué importa:** Un motor puede quemar mezclas con exceso de combustible o de oxidante. La decisión central: ¿qué `O/F` maximiza el escape en un modelo sin disociación y por qué los motores reales operan en otro punto?

📘 **Dónde se aprende** (1 clase): [B78-C05 · Propulsión bipropelente conceptual](../programa/clases/B78/B78-C05-propulsion-bipropelente-conceptual/CLASE.md).

### Rica en combustible

- La razón O/F de 3,5 es rica en combustible frente a la estequiométrica (3,99).

🎯 **Por qué importa (clase B59-C09):** Un combustible fabricado en destino depende de qué parte del hidrógeno se recicla. La decisión central: ¿cuánto hidrógeno hay que importar para fabricar 1 000 kg de propelente O₂/CH₄?

📘 **Dónde se aprende** (1 clase): [B59-C09 · Fabricación de combustibles conceptuales](../programa/clases/B59/B59-C09-fabricacion-de-combustibles-conceptuales/CLASE.md).

### Richardson

- El orden observado es `p = ln((f₂ − f₁)/(f₃ − f₂))/ln r` con tres mallas. Richardson: `f_ext = f₃ + (f₃ − f₂)/(r^p − 1)`.

💡 **Cómo se explica en la clase [B84-C26](../programa/clases/B84/B84-C26-generacion-de-mallas-y-convergencia-en-elementos-finitos/CLASE.md):**
- `p = 0,935`, Richardson `25,0367 MPa` (dif `1,5 × 10⁻³`) y GCI `3,14 %`.
- Extrapolar con Richardson al límite de malla infinitamente fina.
- 🎯 **Por qué importa:** Una malla más gruesa puede errar 30 % en tensión sin que el resultado «parezca» mal; la convergencia dice cuánto y cuánto refinar. La decisión central: ¿cuántos elementos hacen falta para que la magnitud de interés cambie menos que una tolerancia dada?

📘 **Dónde se aprende** (1 clase): [B84-C26 · Generación de mallas y convergencia en elementos finitos](../programa/clases/B84/B84-C26-generacion-de-mallas-y-convergencia-en-elementos-finitos/CLASE.md).

### Richardson–Lucy

- El método de Richardson–Lucy (RL) es iterativo, conserva la positividad y es el que implementan bibliotecas como scikit-image (S2).
- La inversión es hallar `ψ` a partir de los conteos. Richardson–Lucy es una iteración multiplicativa de máxima verosimilitud de Poisson.
- El filtro de Wiener. Richardson-Lucy: iteración que conserva flujo y positividad.

💡 **Cómo se explica en la clase [B15-C11](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md):**
- I -->|"Richardson–Lucy<br/>y parar a tiempo"| F["Estimación x̂:<br/>más nítida"]
- *Descripción textual:* el objeto se convoluciona con la PSF y se le añade ruido; invertir con el filtro inverso amplifica el ruido hasta inutilizar la imagen, mientras que el método iterativo de Richardson–Lucy, detenido a tiempo, produce una estimación más nítida.
- 🎯 **Por qué importa:** Un telescopio con un defecto de enfoque convierte cada estrella en una mancha. Dos estrellas cercanas pueden fundirse en una sola; el brillo de una galaxia, repartirse sobre sus vecinas.

📘 **Dónde se aprende** (3 clases): [B15-C11 · Deconvolución y enfoque](../programa/clases/B15/B15-C11-deconvolucion-y-enfoque/CLASE.md); [B38-C04 · Historia de formación estelar a partir de poblaciones resueltas](../programa/clases/B38/B38-C04-historia-de-formacion-estelar-a-partir-de-poblaciones-resueltas/CLASE.md); [B42-C19 · Reconstrucción de imágenes](../programa/clases/B42/B42-C19-reconstruccion-de-imagenes/CLASE.md).

### RID

- Un RID (*review item discrepancy*) es un hallazgo que debe cerrarse. «Lista» significa que pasan todos los criterios críticos; los no críticos se registran.

💡 **Cómo se explica en la clase [B83-C13](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md):**
- Estimar el tiempo para cerrar las acciones de revisión (RID).
- Acciones (RID): 10 en total, 3 criticas, capacidad 2 por semana -> 5 semanas para cerrar todas, 2 para las criticas
- ⚠️ **Error frecuente:** Cerrar RID sin evidencia. Registra la evidencia del cierre
- 🎯 **Por qué importa:** Una revisión aprobada sin criterios es un trámite; una revisión con criterios medibles es una decisión. La decisión central: ¿el proyecto cumple los criterios de entrada de la SRR y de la PDR y qué falta para llegar?

📘 **Dónde se aprende** (1 clase): [B83-C13 · Revisiones SRR y PDR](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md).

### Riesgo

- Un riesgo es un evento posible con consecuencia; se acompaña de una mitigación.
- Un riesgo es un escenario con verosimilitud (L, 1–5) y consecuencia (C, 1–5).
- Un peligro es una fuente de daño; el riesgo combina severidad y verosimilitud.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B08-C20](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md):**
- Riesgos: sol y calor de día, frío y oscuridad de noche, caídas en terreno, vehículos, equipo volcado, fatiga al regresar, pérdida de adaptación a la oscuridad por luces; cada uno con su mitigación.
- 🎯 **Por qué importa:** Una salida sin plan termina en una noche perdida o en un accidente. La pregunta motivadora: ¿cómo preparo una salida de observación para que sea segura, útil, accesible y reproducible?

📘 **Dónde se aprende** (7 clases): [B08-C20 · Proyecto de campaña de observación nocturna](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md); [B83-C16 · Gestión de riesgos técnicos](../programa/clases/B83/B83-C16-gestion-de-riesgos-tecnicos/CLASE.md); [B83-C21 · Identificación de peligros en sistemas de lanzamiento (HAZID)](../programa/clases/B83/B83-C21-identificacion-de-peligros-en-sistemas-de-lanzamiento-hazid/CLASE.md); [B110-C02 · Protocolos operativos de aislamiento de un tripulante enfermo o contaminado](../programa/clases/B110/B110-C02-protocolos-operativos-de-aislamiento-de-un-tripulante-enfermo-o-contaminado/CLASE.md); [B114-C06 · Matriz de riesgo ambiental de un hábitat](../programa/clases/B114/B114-C06-matriz-de-riesgo-ambiental-de-un-habitat/CLASE.md); [B120-C05 · Riesgos de incumplimiento regulatorio](../programa/clases/B120/B120-C05-riesgos-de-incumplimiento-regulatorio/CLASE.md) y 1 más.

### Riesgo colectivo

- El riesgo colectivo `Ec` es el número esperado de bajas.

💡 **Cómo se explica en la clase [B121-C01](../programa/clases/B121/B121-C01-licencias-y-requisitos-nacionales-para-el-lanzamiento/CLASE.md):**
- Un riesgo individual bajo no garantiza un riesgo colectivo bajo: `Ec` suma sobre mucha gente.
- ⚠️ **Error frecuente:** Creer que cumplir el riesgo individual implica cumplir el colectivo. Se corrige con 8.2 y 8.3.
- 🎯 **Por qué importa:** La autorización de un lanzamiento no es un trámite abstracto: incluye criterios numéricos de riesgo. La decisión central: ¿una trayectoria cumple el criterio de riesgo colectivo e individual que exige la licencia y con qué margen?

📘 **Dónde se aprende** (1 clase): [B121-C01 · Licencias y requisitos nacionales para el lanzamiento](../programa/clases/B121/B121-C01-licencias-y-requisitos-nacionales-para-el-lanzamiento/CLASE.md).

### Riesgo de exceso

- El riesgo de exceso es la probabilidad adicional atribuible a la exposición.

💡 **Cómo se explica en la clase [B112-C04](../programa/clases/B112/B112-C04-efectos-cronicos-y-carcinogenesis-por-radiacion/CLASE.md):**
- El riesgo de exceso nominal es `r·E` con `r = 0,05 Sv⁻¹`: 0,050 % a 10 mSv, 0,500 % a 100, 1,250 % a 250, 3,000 % a 600 y 5,000 % a 1000 mSv.
- E["dosis efectiva E [Sv]"] --> R["riesgo de exceso<br/>r · E"]
- 🎯 **Por qué importa:** Ninguna clase cubre riesgo de cáncer y efectos tardíos. Los límites de carrera de una misión se expresan como riesgo, no como umbral, y sin entender cómo se estima y cuán incierta es esa estimación, un límite en mSv parece más preciso de lo que es.

📘 **Dónde se aprende** (1 clase): [B112-C04 · Efectos crónicos y carcinogénesis por radiación](../programa/clases/B112/B112-C04-efectos-cronicos-y-carcinogenesis-por-radiacion/CLASE.md).

### Riesgo de exceso de muerte inducida por exposición

- El riesgo de exceso de muerte inducida por exposición (REID) es la probabilidad de que una persona muera de cáncer a causa de la exposición, en función de la dosis efectiva, la edad y el sexo (NASA THREE).

🎯 **Por qué importa (clase B112-C06):** Falta la clase de estimación de riesgo por misión. Es la que usa un planificador: suma dosis de cada tramo, la convierte en riesgo y decide si cabe dentro de un límite.

📘 **Dónde se aprende** (1 clase): [B112-C06 · Modelos de riesgo de radiación para misiones](../programa/clases/B112/B112-C06-modelos-de-riesgo-de-radiacion-para-misiones/CLASE.md).

### Riesgo del consumidor

- El riesgo del consumidor es aceptar una unidad mala; el del productor, rechazar una buena.

💡 **Cómo se explica en la clase [B50-C14](../programa/clases/B50/B50-C14-criterios-de-aceptacion-strehl-error-de-frente-de-onda-y-especificaciones/CLASE.md):**
- G --> R["riesgos consumidor y productor"]
- Con límite de 0,05 ondas e incertidumbre de medida 0,005, una banda de guarda de 1,645 baja el riesgo del consumidor de `3,51 %` a `0,22 %`.
- 🎯 **Por qué importa:** Una especificación solo sirve si se puede verificar con una medida que tiene incertidumbre. La decisión central: ¿cuánto margen se deja para que una medida incierta no acepte una unidad mala?

📘 **Dónde se aprende** (1 clase): [B50-C14 · Criterios de aceptación: Strehl, error de frente de onda y especificaciones](../programa/clases/B50/B50-C14-criterios-de-aceptacion-strehl-error-de-frente-de-onda-y-especificaciones/CLASE.md).

### Riesgo individual

- El riesgo individual `P_c` es la probabilidad de que una persona resulte víctima.
- El riesgo individual `Pc` es la probabilidad de baja de una persona.

💡 **Cómo se explica en la clase [B77-C19](../programa/clases/B77/B77-C19-seguridad-de-rango-a-nivel-conceptual/CLASE.md):**
- *Descripción textual:* la probabilidad de falla, la distribución de impactos, la población y el área de víctima se combinan en las víctimas esperadas y en el riesgo individual, que se comparan con los umbrales.
- Descripción larga: el riesgo colectivo sube de forma marcada al acercar una zona poblada al eje de la trayectoria; el riesgo individual en un punto es mucho más pequeño que el colectivo.
- ⚠️ **Error frecuente:** Confundir riesgo colectivo con individual. Se corrige con 8.3.
- 🎯 **Por qué importa:** Mover el sitio de impacto un par de decenas de kilómetros cambia el riesgo en un factor de varios. La decisión central: ¿cómo se calculan las víctimas esperadas y cuánto depende de dónde cae lo que cae?

📘 **Dónde se aprende** (2 clases): [B77-C19 · Seguridad de rango a nivel conceptual](../programa/clases/B77/B77-C19-seguridad-de-rango-a-nivel-conceptual/CLASE.md); [B121-C01 · Licencias y requisitos nacionales para el lanzamiento](../programa/clases/B121/B121-C01-licencias-y-requisitos-nacionales-para-el-lanzamiento/CLASE.md).

### Riesgo inherente

- El riesgo inherente es `P × I` sin controles; el residual, con controles.

💡 **Cómo se explica en la clase [B122-C03](../programa/clases/B122/B122-C03-modelo-defensivo-de-riesgos-de-infraestructura-espacial/CLASE.md):**
- *Descripción textual:* activo y amenaza definen un riesgo inherente; los controles reducen la probabilidad y dejan el riesgo residual, que se clasifica.
- Calcular el riesgo inherente y el residual.
- 🎯 **Por qué importa:** B83-C16 trata riesgos técnicos y B119-C14 amenazas sin modelo. La decisión central: ¿qué riesgo residual domina y qué activo carece de controles?

📘 **Dónde se aprende** (1 clase): [B122-C03 · Modelo defensivo de riesgos de infraestructura espacial](../programa/clases/B122/B122-C03-modelo-defensivo-de-riesgos-de-infraestructura-espacial/CLASE.md).

### Riesgo residual

- El riesgo residual es el `R` tras aplicar las medidas.
- El riesgo residual es el que queda.
- Filosofía de modelos: conjunto de modelos que se construye y prueba. Riesgo residual: probabilidad de que un defecto llegue a órbita.

💡 **Cómo se explica en la clase [B90-C24](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md):**
- La mejor filosofía es C porque las correcciones tempranas son baratas y el riesgo residual es 5 veces menor que el de A.
- Descripción larga: el costo esperado de A crece con la pérdida más rápido que el de C porque el riesgo residual de A es mayor.
- 🎯 **Por qué importa:** Un modelo de ingeniería cuesta dinero y calendario; un defecto que llega a órbita cuesta la misión. La decisión central: ¿vale la pena construir un modelo previo, o conviene el protovuelo o solo la unidad de vuelo, dado el valor de lo que se arriesga?

📘 **Dónde se aprende** (3 clases): [B90-C24 · Prototipado y modelos de ingeniería de subconjuntos](../programa/clases/B90/B90-C24-prototipado-y-modelos-de-ingenieria-de-subconjuntos/CLASE.md); [B114-C06 · Matriz de riesgo ambiental de un hábitat](../programa/clases/B114/B114-C06-matriz-de-riesgo-ambiental-de-un-habitat/CLASE.md); [B119-C14 · Amenazas cibernéticas a satélites](../programa/clases/B119/B119-C14-amenazas-ciberneticas-a-satelites/CLASE.md).

### Riesgo retenido

- El riesgo retenido se mide por la desviación y los cuantiles del costo.

💡 **Cómo se explica en la clase [B127-C08](../programa/clases/B127/B127-C08-simulacion-de-cobertura-de-seguros-para-una-mision/CLASE.md):**
- El tercero pasaría a dominar el riesgo retenido en A–C y su prima subiría unas diez veces;
- 🎯 **Por qué importa:** Integrar los seguros de una misión en un caso permite practicar la decisión; no existía tal caso. La decisión central: ¿cuánto se paga de más por reducir el riesgo y qué riesgo se está dispuesto a retener?

📘 **Dónde se aprende** (1 clase): [B127-C08 · Simulación de cobertura de seguros para una misión](../programa/clases/B127/B127-C08-simulacion-de-cobertura-de-seguros-para-una-mision/CLASE.md).

### Rigidez

- La fuerza restauradora apunta al equilibrio y es proporcional al desplazamiento: `F = −k x` (ley de Hooke), con `k` la rigidez (N/m).
- La rigidez de una EOS es cuánto crece `P` con `ρ`.
- La rigidez es el par por grado.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B05-C11](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md):**
- No se consultó un dato de vibración de ninguna misión, así que el caso de esta clase es sintético: un mástil de enseñanza de 50 kg de masa efectiva y rigidez de 2,0 × 10⁵ N/m.
- Ejercicio 12 · integrador. Elabora una *ficha de oscilador* (sección 20): para un sistema sintético (masa y rigidez a tu elección), calcula `ω₀`, `f`, `T`, energía, amplificación en resonancia con dos `ζ`, y compáralo con una integración numérica.
- 🎯 **Por qué importa:** Una estructura que vibra puede amplificar una excitación hasta romperse; un reloj de péndulo mide tiempo; un átomo vibra en un cristal. La pregunta motivadora es: ¿qué determina la frecuencia a la que algo oscila y qué pasa cuando se le empuja a esa frecuencia?

📘 **Dónde se aprende** (5 clases): [B05-C11 · Movimiento oscilatorio](../programa/clases/B05/B05-C11-movimiento-oscilatorio/CLASE.md); [B27-C04 · Ecuación de estado nuclear](../programa/clases/B27/B27-C04-ecuacion-de-estado-nuclear/CLASE.md); [B43-C25 · Rodamientos y apoyos de precisión en telescopios](../programa/clases/B43/B43-C25-rodamientos-y-apoyos-de-precision-en-telescopios/CLASE.md); [B107-C02 · Movilidad articular, flexibilidad y postura](../programa/clases/B107/B107-C02-movilidad-articular-flexibilidad-y-postura/CLASE.md); [B107-C07 · Rehabilitación vestibular y del equilibrio posterior al vuelo](../programa/clases/B107/B107-C07-rehabilitacion-vestibular-y-del-equilibrio-posterior-al-vuelo/CLASE.md).

### Rigidez a flexión

- La rigidez a flexión `E I`.

🎯 **Por qué importa (clase B43-C10):** Lo que decolima no es la flexión sino la flexión diferencial entre primario y secundario. La decisión central: ¿qué rigideces hacen que los dos extremos se muevan lo mismo, de modo que el eje óptico solo se desplace en paralelo?

📘 **Dónde se aprende** (1 clase): [B43-C10 · Estructura de tubo óptico](../programa/clases/B43/B43-C10-estructura-de-tubo-optico/CLASE.md).

### Rigidez de elemento

- La rigidez de elemento es `k = EA/l [[1,−1],[−1,1]]`.

💡 **Cómo se explica en la clase [B84-C12](../programa/clases/B84/B84-C12-analisis-de-elementos-finitos/CLASE.md):**
- *Descripción textual:* se calcula la rigidez de cada elemento, se ensambla `K`, se restringe el empotramiento, se resuelve y se verifican reacción, energía y error.
- Analogía: una barra afilada es una cadena de resortes de rigidez decreciente: cada elemento aporta un resorte con el área en su punto medio.
- 🎯 **Por qué importa:** Un modelo que da un resultado no es un modelo correcto: la verificación contra una solución conocida es lo que lo convierte en una herramienta. La decisión central: ¿cómo demuestras que un modelo de elementos finitos resuelve bien las ecuaciones que dice resolver?

📘 **Dónde se aprende** (1 clase): [B84-C12 · Análisis de elementos finitos](../programa/clases/B84/B84-C12-analisis-de-elementos-finitos/CLASE.md).

### Rigidez del sándwich

- La rigidez del sándwich es `D = E t_f d²/(2(1 − ν²))` con `d = h + t_f`.

💡 **Cómo se explica en la clase [B84-C20](../programa/clases/B84/B84-C20-diseno-estructural-de-plataforma-satelital/CLASE.md):**
- Calcular la rigidez y la frecuencia de un panel sándwich.
- 🎯 **Por qué importa:** Un diseño estructural se justifica con requisitos, un modelo, márgenes y un balance de masa; sin cualquiera de ellos no se puede revisar. La decisión central: ¿cumple esta estructura preliminar los requisitos de frecuencia y de resistencia con la masa disponible?

📘 **Dónde se aprende** (1 clase): [B84-C20 · Diseño estructural de plataforma satelital](../programa/clases/B84/B84-C20-diseno-estructural-de-plataforma-satelital/CLASE.md).

### Rigidez deseada K_d

- Impedancia: relación entre el movimiento y la fuerza. Rigidez deseada `K_d`: N/m.

💡 **Cómo se explica en la clase [B101-C07](../programa/clases/B101/B101-C07-control-de-fuerza-e-impedancia-en-manipulacion/CLASE.md):**
- Menor rigidez deseada, menor fuerza: con `K_d = 200` N/m la fuerza es 13 veces menor que con 5 000 N/m para la misma posición ordenada.
- 🎯 **Por qué importa:** Si un brazo muy rígido empuja una pieza que está 5 mm más lejos de lo que cree, aplica una fuerza grande. La decisión central: ¿qué rigidez y qué amortiguamiento le doy al extremo para que el contacto sea suave y la fuerza predecible?

📘 **Dónde se aprende** (1 clase): [B101-C07 · Control de fuerza e impedancia en manipulación](../programa/clases/B101/B101-C07-control-de-fuerza-e-impedancia-en-manipulacion/CLASE.md).

### Rigidez específica

- La rigidez específica es `E/ρ`; la resistencia específica, `σ₀,₂/ρ`; la resiliencia, `σ₀,₂²/(2E)`.
- La rigidez específica `E/ρ` compara materiales de igual masa.

💡 **Cómo se explica en la clase [B43-C03](../programa/clases/B43/B43-C03-materiales-para-espejos/CLASE.md):**
- Calcular la rigidez específica `E/ρ` y la figura de mérito térmica `k/α`.
- 🎯 **Por qué importa:** Un buen material no es el más duro ni el más estable: es el que deja el menor error de forma para una masa y un presupuesto. La decisión central: ¿qué material y qué espesor mantienen la flexión y la deriva térmica por debajo de la tolerancia?

📘 **Dónde se aprende** (2 clases): [B43-C03 · Materiales para espejos](../programa/clases/B43/B43-C03-materiales-para-espejos/CLASE.md); [B84-C02 · Propiedades de aleaciones](../programa/clases/B84/B84-C02-propiedades-de-aleaciones/CLASE.md).

### Rigidez flexural

- La rigidez flexural es `D = E T³/(12(1 − ν²))`.

💡 **Cómo se explica en la clase [B53-C12](../programa/clases/B53/B53-C12-tectonica-planetaria/CLASE.md):**
- *Descripción textual:* El espesor elástico fija la rigidez y el parámetro flexural, que con la carga dan la deflexión y su abombamiento; aparte, los escarpes dan la contracción.
- 🎯 **Por qué importa:** La flexión revela el espesor elástico de la litosfera y la contracción, el balance térmico global. La decisión central: ¿qué espesor elástico y qué acortamiento explican la deformación observada?

📘 **Dónde se aprende** (1 clase): [B53-C12 · Tectónica planetaria](../programa/clases/B53/B53-C12-tectonica-planetaria/CLASE.md).

### Rigidez magnética

- La rigidez magnética `Bρ = p/e`.

🎯 **Por qué importa (clase B31-C15):** El diseño de un acelerador depende de cuánta energía se pierde por radiación y de cuánta energía útil se obtiene. La decisión central: ¿qué campo y qué radio se necesitan y por qué los electrones pierden tanto?

📘 **Dónde se aprende** (1 clase): [B31-C15 · Física de aceleradores](../programa/clases/B31/B31-C15-fisica-de-aceleradores/CLASE.md).

### Rígido

- Un problema es rígido cuando contiene escalas de tiempo muy distintas y la más rápida obliga a un paso pequeño sin interés por sí misma.
- Un sistema es rígido si tiene componentes que evolucionan en escalas de tiempo muy distintas.

💡 **Cómo se explica en la clase [B11-C09](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md):**
- Implícitos (Euler implícito, y sus relativos de orden alto): resuelven una ecuación por paso, estables en problemas rígidos.
- Un control adaptativo (C08) *reduce* `h` si el error crece, y por tanto también detecta la inestabilidad, pero a un costo enorme en problemas rígidos: el paso baja a `2/k` aunque la solución sea lisa.
- ⚠️ **Error frecuente:** Usar un método explícito para un problema rígido y culpar al código. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Un modelo térmico de una nave tiene constantes de tiempo que van de segundos (un sensor fino) a horas (un tanque grande). Un método explícito debe usar un paso comparable al más rápido aunque lo único que interese sea lo lento: pagar por una escala que no se observa.

📘 **Dónde se aprende** (2 clases): [B11-C09 · Análisis de estabilidad numérica](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md); [B60-C03 · Integración numérica de redes químicas rígidas](../programa/clases/B60/B60-C03-integracion-numerica-de-redes-quimicas-rigidas/CLASE.md).

### Ripples

- Las ripples y dunas son formas que el transporte genera en el lecho.

💡 **Cómo se explica en la clase [B66-C03](../programa/clases/B66/B66-C03-procesos-eolicos-dunas-ripples-y-erosion-planetaria/CLASE.md):**
- python programa/clases/B66/B66-C03-procesos-eolicos-dunas-ripples-y-erosion-planetaria/eolico.py
- 🎯 **Por qué importa:** Marte tiene dunas y una atmósfera cien veces menos densa que la terrestre; Venus, una atmósfera enorme y casi sin viento.

📘 **Dónde se aprende** (1 clase): [B66-C03 · Procesos eólicos: dunas, ripples y erosión planetaria](../programa/clases/B66/B66-C03-procesos-eolicos-dunas-ripples-y-erosion-planetaria/CLASE.md).

### Riqueza

- La riqueza cuenta taxones.

💡 **Cómo se explica en la clase [B105-C11](../programa/clases/B105/B105-C11-microbioma-en-ambientes-cerrados/CLASE.md):**
- Con pocas lecturas, la riqueza y Shannon se subestiman.
- Equivalente textual: más profundidad, más riqueza observada; más mezcla, menor disimilitud; más dominancia, menos diversidad.
- 🎯 **Por qué importa:** Un índice de diversidad depende de la comunidad y de cuántas lecturas se obtuvieron. La decisión central: ¿qué profundidad de muestreo hace fiable un índice y cómo se cuantifica el parecido entre la piel de la tripulación y las superficies?

📘 **Dónde se aprende** (1 clase): [B105-C11 · Microbioma en ambientes cerrados](../programa/clases/B105/B105-C11-microbioma-en-ambientes-cerrados/CLASE.md).

### Ritchey-Chrétien

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C17](../programa/clases/B41/B41-C17-telescopios-cassegrain-y-derivados/CLASE.md):**
- Con `m = 5` y foco `100 mm` tras el primario: `d = 316,667 mm`, `R₂ = 208,333 mm` y `k₂ = −2,25`; el clásico da coma `10,955 µm` a 10', el Dall-Kirkham `135,089 µm` y el Ritchey-Chrétien `0` (`k₁ = −1,02130`, `k₂ = −2,44971`).
- Resolver Ritchey-Chrétien por Newton 2D.
- 🎯 **Por qué importa:** Dos espejos permiten un tubo corto y focal larga, y distintos diseños eligen qué aberración corregir. La decisión central: ¿qué diseño corrige la coma y a qué costo?

📘 **Dónde se aprende** (1 clase): [B41-C17 · Telescopios Cassegrain y derivados](../programa/clases/B41/B41-C17-telescopios-cassegrain-y-derivados/CLASE.md).

### Ritchey-Chrétien (RC)

- El Ritchey-Chrétien (RC) usa dos hiperboloides.

💡 **Cómo se explica en la clase [B43-C02](../programa/clases/B43/B43-C02-seleccion-de-geometria-instrumental/CLASE.md):**
- Obtener las conicidades de un Ritchey-Chrétien resolviendo dos condiciones.
- 🎯 **Por qué importa:** La geometría decide qué aberraciones quedan y cuánto mide el tubo. La decisión central: ¿qué conicidades de primario y secundario anulan la aberración esférica y el coma, y qué se paga en largo y obstrucción?

📘 **Dónde se aprende** (1 clase): [B43-C02 · Selección de geometría instrumental](../programa/clases/B43/B43-C02-seleccion-de-geometria-instrumental/CLASE.md).

### Ritmo circadiano

- El ritmo circadiano `C` es una oscilación de 24 h.
- Ritmo circadiano: oscilación de unas 24 h de procesos fisiológicos.

💡 **Cómo se explica en la clase [B104-C17](../programa/clases/B104/B104-C17-gestion-de-fatiga/CLASE.md):**
- *Descripción textual:* la presión de sueño sube despierto y baja dormido; el ritmo circadiano la compensa o la agrava; la alerta es su diferencia.
- 🎯 **Por qué importa:** NASA reconoce la pérdida de sueño, la desincronización circadiana y la sobrecarga como un riesgo del vuelo. La decisión conceptual: ¿cuánta alerta se pierde en el trabajo diurno al acortar el sueño unas horas, y por qué el modelo no sustituye a la medición?

📘 **Dónde se aprende** (2 clases): [B104-C17 · Gestión de fatiga](../programa/clases/B104/B104-C17-gestion-de-fatiga/CLASE.md); [B106-C13 · Iluminación y ciclos circadianos](../programa/clases/B106/B106-C13-iluminacion-y-ciclos-circadianos/CLASE.md).

### Ritmo libre

- El ritmo libre es el periodo del ciclo sueño–vigilia sin señales externas.

💡 **Cómo se explica en la clase [B113-C04](../programa/clases/B113/B113-C04-autonomia-personal-y-gestion-del-tiempo-en-aislamiento/CLASE.md):**
- Un ritmo libre de `25,0 h` (valor ilustrativo, cercano al del tripulante b de Basner et al.) desplaza el sueño `1 h` por día respecto de un reloj de 24 h: `10 h` tras `10` días y una vuelta completa en `24` días.
- Relacionar el ritmo libre cercano a 25 h con la pérdida de sincronía.
- 🎯 **Por qué importa:** Falta la clase sobre autonomía y rutinas. La decisión central: ¿qué holgura reservar en una jornada y qué reloj seguir cuando el día local no dura 24 horas?

📘 **Dónde se aprende** (1 clase): [B113-C04 · Autonomía personal y gestión del tiempo en aislamiento](../programa/clases/B113/B113-C04-autonomia-personal-y-gestion-del-tiempo-en-aislamiento/CLASE.md).

### Ritmo máximo

- La dirección de máximo crecimiento es `∇f/|∇f|` y el ritmo máximo es `|∇f|`.

💡 **Cómo se explica en la clase [B09-C17](../programa/clases/B09/B09-C17-gradiente-y-derivada-direccional/CLASE.md):**
- B --> C["Dirección ∇f/|∇f|:<br/>máximo crecimiento, ritmo |∇f|"]
- Ejercicio 3 · casi autónomo. Halla la dirección, el ritmo máximo y una dirección de cambio nulo para la misma función.
- 🎯 **Por qué importa:** La gravedad no es un número: es un vector que apunta a un lado y tiene una magnitud. En un campo con dos cuerpos, como Tierra–Luna, esa dirección cambia de punto a punto.

📘 **Dónde se aprende** (1 clase): [B09-C17 · Gradiente y derivada direccional](../programa/clases/B09/B09-C17-gradiente-y-derivada-direccional/CLASE.md).

### Rizado

- El rizado es la variación pico a pico en un periodo.

💡 **Cómo se explica en la clase [B86-C08](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md):**
- *Descripción textual:* el interruptor conecta la entrada a la bobina con ciclo `D`; el diodo conduce en el resto del periodo; la bobina y el condensador filtran y alimentan la carga; de ahí salen el rizado y las pérdidas.
- Paso 4 · Rizado. `ΔI = 23 × 0,965 µs/22 µH = 1,0085 A`.
- ⚠️ **Error frecuente:** Confundir rizado con valor medio. Se corrige con 8.2 y 8.3.
- 🎯 **Por qué importa:** Un convertidor que reduce la tensión con un interruptor y una bobina puede ser mucho más eficiente que un regulador lineal, pero introduce rizado, ruido y pérdidas de conmutación que hay que dimensionar. La decisión central: ¿qué ciclo de trabajo, bobina y condensador dan `5 V` desde `28 V` con rizado y eficiencia aceptables?

📘 **Dónde se aprende** (1 clase): [B86-C08 · Convertidores DC-DC](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md).

### RK4

- La temperatura límite es `T_a − Q/G`. RK4 es un integrador de cuarto orden.
- El baricentro es el centro de masas del par. RK4 es el método de Runge–Kutta de cuarto orden.
- Euler explícito es de orden 1. RK4 es de orden 4.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B44-C08](../programa/clases/B44/B44-C08-enfriamiento-de-detectores/CLASE.md):**
- Con paso de `0,5 s`, el error máximo de Euler es `0,01380 K` y el de RK4 `4,8 × 10⁻¹³ K`.
- Ejercicio 7. Error de Euler frente a RK4.
- 🎯 **Por qué importa:** La cámara no está fría al encenderla. La decisión central: ¿cuánto hay que esperar antes de calibrar y qué temperatura final se alcanza?

📘 **Dónde se aprende** (6 clases): [B44-C08 · Enfriamiento de detectores](../programa/clases/B44/B44-C08-enfriamiento-de-detectores/CLASE.md); [B71-C03 · Ecuación de movimiento de dos cuerpos](../programa/clases/B71/B71-C03-ecuacion-de-movimiento-de-dos-cuerpos/CLASE.md); [B72-C18 · Integración numérica perturbada](../programa/clases/B72/B72-C18-integracion-numerica-perturbada/CLASE.md); [B85-C26 · Análisis térmico transitorio y casos extremos](../programa/clases/B85/B85-C26-analisis-termico-transitorio-y-casos-extremos/CLASE.md); [B97-C23 · Diseño de simulador de misión robótica](../programa/clases/B97/B97-C23-diseno-de-simulador-de-mision-robotica/CLASE.md); [B101-C06 · Simulación de un brazo robótico espacial](../programa/clases/B101/B101-C06-simulacion-de-un-brazo-robotico-espacial/CLASE.md).

### RMF

- La RMF es la matriz de redistribución de energía a canal.

💡 **Cómo se explica en la clase [B27-C22](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md):**
- RMF gaussiana con `σ = 0,1E`, normalizada de modo que cada columna suma 1.
- Con respuesta identidad, el plegado coincide con el cálculo directo a `10⁻⁹`; las columnas de la RMF suman 1;
- 🎯 **Por qué importa:** Ajustar un espectro «de fotones» directamente a las cuentas da resultados engañosos; hay que plegar el modelo con la respuesta y usar la estadística correcta para conteos pequeños. La decisión central: ¿qué parámetros recupera cada estadística y con qué sesgo cuando las cuentas son pocas?

📘 **Dónde se aprende** (1 clase): [B27-C22 · Análisis espectral de rayos X y gamma: ajuste con respuesta instrumental](../programa/clases/B27/B27-C22-analisis-espectral-de-rayos-x-y-gamma/CLASE.md).

### RML

- WVR, el vapor de agua recuperado; RML `= TML − WVR`;

💡 **Cómo se explica en la clase [B84-C07](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md):**
- Con `m_i = 500 mg`: `TML = (m_i − m_f)/m_i`, `WVR = (m_h − m_f)/m_i`, `RML = TML − WVR`, `CVCM = Δm_colector/m_i`.
- A["pesadas mi, mf, mh, dc"] --> B["TML, WVR, RML, CVCM"]
- 🎯 **Por qué importa:** Una película de 10 nm sobre un espejo de telescopio o un sensor estelar degrada la misión; el cribado de desgasificación se hace antes de elegir el adhesivo. La decisión central: ¿pasa un material el cribado de desgasificación y cuántos días de bakeout necesita para limpiarlo?

📘 **Dónde se aprende** (1 clase): [B84-C07 · Desgasificación de materiales](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md).

### RMS

- El RMS mide la calidad.
- El sesgo es el residuo medio; el RMS, su raíz cuadrática media.
- El RMS mide la energía de la señal.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B43-C22](../programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/CLASE.md):**
- La diferencia punto a punto entre ambos restos tiene `1,011 nm` RMS (ruido inyectado de 0,02 rad, equivalente a `0,02 λ/(4π) = 1,01 nm` por píxel).
- La superficie tiene `14,8` franjas en total; tras ajustar piston, inclinaciones y desenfoque queda un resto de `97,3 nm` PV y `19,90 nm` RMS (`0,0314 λ`).
- 🎯 **Por qué importa:** El mapa de error de forma es la prueba de aceptación de un espejo. La decisión central: ¿cómo se recupera la fase, qué se descuenta y qué PV y RMS quedan?

📘 **Dónde se aprende** (6 clases): [B43-C22 · Interferometría de superficie y mapas de error de forma](../programa/clases/B43/B43-C22-interferometria-de-superficie-y-mapas-de-error-de-forma/CLASE.md); [B45-C08 · Calibración en longitud de onda](../programa/clases/B45/B45-C08-calibracion-en-longitud-de-onda/CLASE.md); [B47-C10 · Estabilidad de apuntamiento](../programa/clases/B47/B47-C10-estabilidad-de-apuntamiento/CLASE.md); [B85-C14 · Degradación ultravioleta](../programa/clases/B85/B85-C14-degradacion-ultravioleta/CLASE.md); [B85-C27 · Márgenes y correlación térmica](../programa/clases/B85/B85-C27-margenes-y-correlacion-termica/CLASE.md); [B97-C26 · Monitoreo de condición de maquinaria extraterrestre](../programa/clases/B97/B97-C26-monitoreo-de-condicion-de-maquinaria-extraterrestre/CLASE.md).

### RMS 3D

- El RMS 3D es `√(Σσ²)`.

💡 **Cómo se explica en la clase [B74-C19](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md):**
- Con `σ = (3; 1,2; 2) m`: RMS 3D `3,8000 m` (muestral `3,8012 m`), percentil 95 de la norma 3D `6,493 m`, SEP (50 %) `3,190 m`, CEP (50 %, horizontal) `2,425 m`.
- Con `N = 50`, el RMS 3D es `3,816 ± 0,245 m`, el percentil 95 `6,316 ± 0,634 m` y el CEP `2,457 ± 0,264 m`.
- 🎯 **Por qué importa:** Dos informes pueden decir «3 m» y referirse a cosas distintas (RMS, 50 %, 95 %). La decisión central: ¿qué métrica comunica el riesgo que importa, con qué probabilidad y con qué incertidumbre muestral?

📘 **Dónde se aprende** (1 clase): [B74-C19 · Métricas de precisión de navegación](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md).

### RMS del frente de onda

- El RMS del frente de onda se calcula quitando pistón, inclinación y enfoque.

💡 **Cómo se explica en la clase [B50-C10](../programa/clases/B50/B50-C10-errores-de-centrado-y-su-efecto-en-el-desempeno/CLASE.md):**
- Medir el RMS del frente de onda con el secundario desplazado.
- El script [descentramiento.py](descentramiento.py) desplaza el secundario y mide el RMS del frente de onda (comprueba linealidad a 2 %, simetría a 1e-9 e invariancia a 1e-6 ondas).
- 🎯 **Por qué importa:** El descentramiento es una de las tolerancias de montaje que más pesan en un telescopio. La decisión central: ¿cuánto puede desplazarse el secundario antes de degradar la imagen?

📘 **Dónde se aprende** (1 clase): [B50-C10 · Errores de centrado y su efecto en el desempeño](../programa/clases/B50/B50-C10-errores-de-centrado-y-su-efecto-en-el-desempeno/CLASE.md).

### RMS sin enfoque

- El RMS sin enfoque quita el pistón, la inclinación y el desenfoque.

💡 **Cómo se explica en la clase [B50-C03](../programa/clases/B50/B50-C03-sistemas-catadioptricos-schmidt-y-maksutov/CLASE.md):**
- Con enfoque libre (`a = 6,138 × 10⁻¹¹`, `b = 4,483 × 10⁻⁹`) queda en `0,00311` ondas.
- Un espejo esférico `R = 2000 mm`, `f/5`, tiene un RMS sin enfoque de `0,427` ondas en el eje.
- 🎯 **Por qué importa:** Combinar espejos y elementos refractivos permite campos amplios con superficies fáciles de fabricar. La decisión central: ¿dónde va el diafragma y qué corrige el elemento refractivo?

📘 **Dónde se aprende** (1 clase): [B50-C03 · Sistemas catadióptricos: Schmidt y Maksutov](../programa/clases/B50/B50-C03-sistemas-catadioptricos-schmidt-y-maksutov/CLASE.md).

### RMSE

- El RMSE es la raíz del error cuadrático medio.
- MAE es el error absoluto medio, RMSE el cuadrático medio, AbsRel la media de `|ẑ − z|/z` y delta1 la fracción de puntos con `máx(z/ẑ, ẑ/z) < 1,25`.

💡 **Cómo se explica en la clase [B33-C01](../programa/clases/B33/B33-C01-validacion-de-modelos-mhd-con-eventos-solares-documentados/CLASE.md):**
- Sesgo `−5,22 km/s`, RMSE `39,39 km/s`, correlación `0,8059`, `MSSS` frente a la climatología `0,5907` y frente a la persistencia de 24 h `0,3341`.
- El RMSE por remuestreo tiene mediana `39,48` e intervalo del 5–95 % `[37,73; 41,67] km/s`; el valor observado cae dentro.
- 🎯 **Por qué importa:** Un modelo sin validación no sirve para pronosticar. La decisión central: ¿cuán bien reproduce el modelo la serie y con qué desfase?

📘 **Dónde se aprende** (4 clases): [B33-C01 · Validación de modelos MHD con eventos solares documentados](../programa/clases/B33/B33-C01-validacion-de-modelos-mhd-con-eventos-solares-documentados/CLASE.md); [B33-C12 · Pronóstico de llegada y severidad de CME](../programa/clases/B33/B33-C12-pronostico-de-llegada-y-severidad-de-cme/CLASE.md); [B57-C31 · Errores y validación de modelos de elevación](../programa/clases/B57/B57-C31-errores-y-validacion-de-modelos-de-elevacion/CLASE.md); [B103-C08 · Métricas de evaluación de percepción](../programa/clases/B103/B103-C08-metricas-de-evaluacion-de-percepcion/CLASE.md).

### RMSF

- La RMSF es su respuesta a una fuente puntual.

💡 **Cómo se explica en la clase [B46-C13](../programa/clases/B46/B46-C13-polarimetria-de-radio/CLASE.md):**
- Con una fuente sintética de `RM = 60 rad/m²` y `p = 0,3`, la síntesis da el pico en `59,5 rad/m²` (amplitud `0,297`) y el ajuste `59,54 rad/m²`; la RMSF mide `61,3 rad/m²`.
- Ejercicio 6. ¿Cuánto vale la RMSF para `Δλ² = 0,113 m²`?
- 🎯 **Por qué importa:** El ángulo de polarización gira con `λ²`, y hay que medirlo en varias frecuencias para saber cuánto. La decisión central: ¿cómo se obtiene la medida de rotación sin ambigüedad de `nπ`?

📘 **Dónde se aprende** (1 clase): [B46-C13 · Polarimetría de radio](../programa/clases/B46/B46-C13-polarimetria-de-radio/CLASE.md).

### Robustez

- La robustez es la fracción de pesos aleatorios con que un sitio sigue siendo el primero.

💡 **Cómo se explica en la clase [B67-C01](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md):**
- Ejercicio 12 · integrador. Elabora tu *ficha de selección multicriterio*: tabla de datos, normalización, puntaje, frente de Pareto, robustez y umbral de cambio.
- 🎯 **Por qué importa:** Elegir con una sola cifra (la reserva) lleva a sitios que no se pueden explotar; elegir con una suma de unidades distintas es un error. La decisión central: ¿cuál sitio conviene, y cuánto de esa respuesta depende de los pesos que fija quien decide?

📘 **Dónde se aprende** (1 clase): [B67-C01 · Selección de sitios de extracción con criterios múltiples](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md).

### Roca

- Una roca es una mezcla de minerales.

💡 **Cómo se explica en la clase [B06-C19](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md):**
- Una roca solamente de olivino y piroxeno tiene Mg/Si entre 1 y 2.
- Imagina un grano de roca (un silicato) en una nube fría, cubierto por capas de hielo: primero agua, luego CO₂ y otras moléculas, según las temperaturas de condensación.
- 🎯 **Por qué importa:** Los estudios con el telescopio James Webb muestran que las nubes densas del medio interestelar tienen granos de polvo cubiertos de hielos con una variedad de moléculas, y que esos hielos contienen entre el 2 y el 19 % del carbono, oxígeno, nitrógeno y azufre disponibles (S1, resumen).

📘 **Dónde se aprende** (1 clase): [B06-C19 · Química de hielos y minerales](../programa/clases/B06/B06-C19-quimica-de-hielos-y-minerales/CLASE.md).

### Rodadura lenta

- La rodadura lenta: `φ̈` despreciable.

💡 **Cómo se explica en la clase [B40-C01](../programa/clases/B40/B40-C01-inflacion-cosmica-motivacion-y-dinamica-basica/CLASE.md):**
- La condición `ε = 1` se alcanza en `φ = 1,0062 M_pl` y `t = 18,630/m`, con `N = 64,563` frente a `63,500` de la rodadura lenta (diferencia `+1,063`).
- La rodadura lenta pierde exactitud al final, como muestra la fila `N = 60`.
- ⚠️ **Error frecuente:** Usar rodadura lenta hasta el final. Se corrige con 8.1.
- 🎯 **Por qué importa:** Sin un mecanismo para las condiciones iniciales, el modelo FLRW deja sin explicar la planitud y la homogeneidad. La decisión central: ¿cuántos e-pliegues produce un campo que rueda lentamente y cuándo termina la inflación?

📘 **Dónde se aprende** (1 clase): [B40-C01 · Inflación cósmica: motivación y dinámica básica](../programa/clases/B40/B40-C01-inflacion-cosmica-motivacion-y-dinamica-basica/CLASE.md).

### Rodilla

- La rodilla es el cambio de pendiente del espectro.
- La rodilla es el punto del frente más alejado, hacia el óptimo, de la recta que une los extremos (objetivos normalizados).

💡 **Cómo se explica en la clase [B28-C04](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md):**
- Con `γ₁ = 2,7`, `γ₂ = 3,1` y rodilla en `10¹⁵ eV`, el flujo integral analítico y el numérico (Simpson en `ln E`) coinciden a `10⁻⁶`: `1,173684 × 10⁻¹⁹` por encima de `10¹¹ eV` y `4,672165 × 10⁻²³` por encima de `10¹³ eV` (unidades arbitrarias).
- Por encima de la rodilla, `flujo(>10¹⁶)/flujo(>10¹⁵) = 0,0079 = 10^{−(γ₂−1)}`.
- 🎯 **Por qué importa:** El origen de los rayos cósmicos de mayor energía sigue abierto; el criterio de Hillas descarta fuentes y la anisotropía apunta a regiones. La decisión central: ¿qué fuentes pueden alcanzar una energía dada y qué anisotropía se puede detectar con un número dado de eventos?

📘 **Dónde se aprende** (2 clases): [B28-C04 · Rayos cósmicos de alta energía](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md); [B81-C11 · Optimización multicriterio y frentes de Pareto](../programa/clases/B81/B81-C11-optimizacion-multicriterio-y-frentes-de-pareto/CLASE.md).
