# Términos · B

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · **B** · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

### B\*

- El movimiento medio de Kozai es el publicado; el de Brouwer es el de la teoría. B\* es el coeficiente de arrastre.

🎯 **Por qué importa (clase B72-C21):** Un error clásico es tomar los elementos de dos líneas como elementos keplerianos y propagarlos con dos cuerpos: el error es de kilómetros en minutos. La decisión central: ¿qué propagador corresponde a un conjunto de elementos y qué transformaciones previas exige antes de usarlo?

📘 **Dónde se aprende** (1 clase): [B72-C21 · Propagador SGP4 y teoría general de perturbaciones](../programa/clases/B72/B72-C21-propagador-sgp4-y-teoria-general-de-perturbaciones/CLASE.md).

### BAC

- El BAC es el presupuesto total.

💡 **Cómo se explica en la clase [B124-C15](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md):**
- La suma de los paquetes coincide con la de los elementos y con el proyecto para BAC, PV, EV y AC (error `0,0e+00`): lo que está en los hijos es todo lo que está en el padre.
- Gastado: `75,0%` del BAC; logrado: `59,6%`.
- 🎯 **Por qué importa:** Un proyecto se descontrola de a poco; el valor ganado convierte «vamos bien» en números comparables. La decisión central: ¿cuánto va a costar el proyecto al terminar si el rendimiento actual se mantiene y qué paquete es el problema?

📘 **Dónde se aprende** (1 clase): [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### Backend

- Un backend es el motor que dibuja;

🎯 **Por qué importa (clase B07-C10):** Un gráfico es una afirmación: dice «mira esta relación». Un gráfico sin unidades, con una escala que esconde la mitad de los datos o sin leyenda puede inducir a error aunque los números sean correctos.

📘 **Dónde se aprende** (1 clase): [B07-C10 · Gráficos bidimensionales iniciales](../programa/clases/B07/B07-C10-graficos-bidimensionales-iniciales/CLASE.md).

### Bajada

- Cada orden viaja por subida y su respuesta por bajada; cada trayecto se pierde con probabilidad `p`.

💡 **Cómo se explica en la clase [B98-C06](../programa/clases/B98/B98-C06-simulacion-de-teleoperacion-con-retardo/CLASE.md):**
- *Descripción textual:* cada orden se reenvía hasta que subida y bajada llegan; los intentos fallidos cuestan el temporizador y el éxito cuesta ejecución y decisión.
- Modelar una orden con subida, bajada, temporizador y retransmisión.
- 🎯 **Por qué importa:** Un promedio oculta la cola: una campaña que «normalmente» dura 8,7 h puede tardar 10,2 h una de cada veinte veces. La decisión central: ¿qué duración debe prometerse a la misión, la media o un percentil, y cómo se comprueba que la simulación es correcta?

📘 **Dónde se aprende** (1 clase): [B98-C06 · Simulación de teleoperación con retardo](../programa/clases/B98/B98-C06-simulacion-de-teleoperacion-con-retardo/CLASE.md).

### Bakeout

- El bakeout es un horneado en vacío para sacar los volátiles.
- Factor de vista: fracción de la emisión de una superficie que alcanza a otra. Bakeout: calentamiento en vacío para expulsar volátiles antes del vuelo.
- Vacío térmico (TVAC): ensayo de temperatura en vacío. Bakeout: calentamiento en vacío para expulsar volátiles.

💡 **Cómo se explica en la clase [B84-C07](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md):**
- *Descripción textual:* las pesadas dan los porcentajes que se comparan con los criterios; la difusión con `D(T)` da la fracción remanente y el tiempo de bakeout, comprobada con diferencias finitas.
- Descripción larga: la silicona B pasa en masa total y falla en condensables; calentar de 20 a 125 °C acorta el bakeout de años a días.
- ⚠️ **Error frecuente:** Ignorar la temperatura en el bakeout. Se corrige con 8.2.
- 🎯 **Por qué importa:** Una película de 10 nm sobre un espejo de telescopio o un sensor estelar degrada la misión; el cribado de desgasificación se hace antes de elegir el adhesivo. La decisión central: ¿pasa un material el cribado de desgasificación y cuántos días de bakeout necesita para limpiarlo?

📘 **Dónde se aprende** (3 clases): [B84-C07 · Desgasificación de materiales](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md); [B90-C04 · Control de contaminación](../programa/clases/B90/B90-C04-control-de-contaminacion/CLASE.md); [B90-C12 · Vacío térmico y ciclos](../programa/clases/B90/B90-C12-vacio-termico-y-ciclos/CLASE.md).

### Balance

- El balance es `dn/dt = P − D n`, con `P` la producción (cm⁻³ s⁻¹) y `D` el coeficiente de destrucción (s⁻¹).
- El balance es `S = M − W − E − (C + R)`, con `M` metabolismo, `W` trabajo externo, `E` evaporación, `C` convección y `R` radiación, en W.

💡 **Cómo se explica en la clase [B55-C04](../programa/clases/B55/B55-C04-quimica-de-nubes-moleculares/CLASE.md):**
- Que `H3+` está siempre en estacionario respecto de las lentas variaciones de la nube; basta el balance algebraico.
- El script [nube_h3plus.py](nube_h3plus.py) integra el balance de `H3+` y comprueba el estacionario analítico (1e-6) y la relajación exponencial (1e-6).
- 🎯 **Por qué importa:** Una nube molecular fría es un reactor lento sostenido por una fuente débil de ionización. Entender el balance de una sola especie clave enseña a leer cualquier red.

📘 **Dónde se aprende** (2 clases): [B55-C04 · Química de nubes moleculares](../programa/clases/B55/B55-C04-quimica-de-nubes-moleculares/CLASE.md); [B105-C23 · Termorregulación humana en vuelo](../programa/clases/B105/B105-C23-termorregulacion-humana-en-vuelo/CLASE.md).

### Balance ambiental

- Balance ambiental: suma de generaciones, retiros y acumulación de cada magnitud.

💡 **Cómo se explica en la clase [B106-C20](../programa/clases/B106/B106-C20-proyecto-de-balance-ambiental-de-habitat/CLASE.md):**
- La evidencia es la informe de balance ambiental con matriz de verificación del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *informe de balance ambiental con matriz de verificación*: modelo y supuestos, tabla de tres escenarios, matriz con los criterios consultados, interpretación de la falla y del respaldo, conservación de masa y qué es ilustrativo.
- 🎯 **Por qué importa:** Los balances de cada clase son sencillos; lo difícil es que actúan a la vez y que fallan. La decisión central: ¿cumple el hábitat sus criterios durante la misión, con y sin una falla, y qué respaldo los salva?

📘 **Dónde se aprende** (1 clase): [B106-C20 · Proyecto de balance ambiental de hábitat](../programa/clases/B106/B106-C20-proyecto-de-balance-ambiental-de-habitat/CLASE.md).

### Balance atómico

- El balance atómico exige el mismo número de cada elemento a ambos lados.

💡 **Cómo se explica en la clase [B56-C02](../programa/clases/B56/B56-C02-bioquimica-y-metabolismo-terrestre/CLASE.md):**
- Ejercicio 12 · integrador. Elabora tu *ficha metabólica*: elige una reacción metabólica distinta (propuesta tuya), comprueba su balance atómico, calcula `ΔG°` con una tabla de tu elección rotulando su procedencia, y dice qué condiciones no estándar la cambiarían.
- Balance atomico: {'C': 6, 'O': 18, 'H': 12}
- 🎯 **Por qué importa:** Para buscar vida hay que saber qué hace la vida conocida con la materia: qué elementos usa y de dónde saca energía. La decisión central: dada una reacción metabólica, ¿está balanceada y cuánta energía libre libera o consume por mol?

📘 **Dónde se aprende** (1 clase): [B56-C02 · Bioquímica y metabolismo terrestre](../programa/clases/B56/B56-C02-bioquimica-y-metabolismo-terrestre/CLASE.md).

### Balance de carga

- El balance de carga es `[Na⁺] + [H⁺] = [HCO₃⁻] + 2[CO₃²⁻] + [OH⁻]`.

💡 **Cómo se explica en la clase [B55-C15](../programa/clases/B55/B55-C15-quimica-de-oceanos-internos/CLASE.md):**
- El residuo del balance de carga es `1,4 × 10⁻¹⁷ mol/kg`.
- NA["[Na⁺] fija"] --> BC["balance de carga"]
- 🎯 **Por qué importa:** El pH de un océano bajo el hielo condiciona qué minerales precipitan y qué química prebiótica es posible. Se calcula con equilibrios acoplados.

📘 **Dónde se aprende** (1 clase): [B55-C15 · Química de océanos internos](../programa/clases/B55/B55-C15-quimica-de-oceanos-internos/CLASE.md).

### Balance de energía

- El balance de energía estacionario de un volumen de control con una entrada y una salida es `Q̇ − Ẇ = ṁ[(h₂ − h₁) + (V₂² − V₁²)/2]`.
- El balance de energía compara el trabajo del resorte con la cinética final más las pérdidas.

💡 **Cómo se explica en la clase [B79-C10](../programa/clases/B79/B79-C10-primera-ley-de-la-termodinamica-en-sistemas-abiertos/CLASE.md):**
- *Descripción textual:* la energía que entra con el flujo más el calor debe igualar la que sale con el flujo más el trabajo; el balance se cierra en cada componente.
- Escribir el balance de energía de un volumen de control estacionario.
- 🎯 **Por qué importa:** B05-C13 ve temperatura y energía térmica, pero no la formulación de volumen de control usada en propulsión. Sin ella no se calcula el trabajo de un compresor ni la velocidad de una tobera.

📘 **Dónde se aprende** (2 clases): [B79-C10 · Primera ley de la termodinámica en sistemas abiertos](../programa/clases/B79/B79-C10-primera-ley-de-la-termodinamica-en-sistemas-abiertos/CLASE.md); [B84-C13 · Mecanismos desplegables](../programa/clases/B84/B84-C13-mecanismos-desplegables/CLASE.md).

### Balance de masa

- El balance de masa reparte la masa total entre estructura y resto.

💡 **Cómo se explica en la clase [B84-C20](../programa/clases/B84/B84-C20-diseno-estructural-de-plataforma-satelital/CLASE.md):**
- *Descripción textual:* el panel da frecuencia y márgenes, el tubo da la frecuencia lateral, y se contrastan con los requisitos y el balance de masa.
- Hacer el balance de masa de la estructura.
- ⚠️ **Error frecuente:** Olvidar el balance de masa. Se corrige con 8.3.
- 🎯 **Por qué importa:** Un diseño estructural se justifica con requisitos, un modelo, márgenes y un balance de masa; sin cualquiera de ellos no se puede revisar. La decisión central: ¿cumple esta estructura preliminar los requisitos de frecuencia y de resistencia con la masa disponible?

📘 **Dónde se aprende** (1 clase): [B84-C20 · Diseño estructural de plataforma satelital](../programa/clases/B84/B84-C20-diseno-estructural-de-plataforma-satelital/CLASE.md).

### Balance de planta

- El balance de planta son tanques, válvulas y gestión del agua.

🎯 **Por qué importa (clase B86-C15):** Una batería guarda la energía y la entrega en la misma masa; una pila separa la potencia (la pila) de la energía (los reactivos). Para misiones largas esa separación puede ser más liviana, pero añade tanques, gestión del agua y complejidad.

📘 **Dónde se aprende** (1 clase): [B86-C15 · Sistemas de combustible como alternativa](../programa/clases/B86/B86-C15-sistemas-de-combustible-como-alternativa/CLASE.md).

### Balance de potencia

- El balance de potencia compara generación y consumo.

💡 **Cómo se explica en la clase [B86-C01](../programa/clases/B86/B86-C01-balance-de-potencia-electrica/CLASE.md):**
- Con la potencia requerida exacta el balance es cero: esa es la definición de «cerrar» el ciclo.
- La evidencia es la hoja de balance de potencia de un satélite sintético del ejercicio 12 (sección 20).
- ⚠️ **Error frecuente:** Dimensionar con la potencia instantánea. Se corrige con 8.2: el balance es de energía por órbita.
- 🎯 **Por qué importa:** Un satélite no consume lo mismo en la luz que en el eclipse, y la batería solo transfiere energía, no la crea. Si se dimensiona con la potencia instantánea y no con la energía por órbita, el ala queda corta o sobrada.

📘 **Dónde se aprende** (1 clase): [B86-C01 · Balance de potencia eléctrica](../programa/clases/B86/B86-C01-balance-de-potencia-electrica/CLASE.md).

### Balance de un nodo

- El balance de un nodo es `Σ G_ij(T_j − T_i) − σ ε_i A_i T_i⁴ + Q_i = 0` (estacionario) o `C_i dT_i/dt = …` (transitorio).

💡 **Cómo se explica en la clase [B85-C18](../programa/clases/B85/B85-C18-modelado-termico-por-nodos/CLASE.md):**
- Plantear el balance de cada nodo con conducción y radiación.
- Ejercicio 1 · con los pasos indicados. Escribe el balance del nodo estructura.
- 🎯 **Por qué importa:** Un modelo por nodos es la herramienta para decidir antes de construir. La decisión central: ¿qué temperatura alcanza cada nodo y qué cambio de diseño (radiador, conductancia, disipación) lo mejora más?

📘 **Dónde se aprende** (1 clase): [B85-C18 · Modelado térmico por nodos](../programa/clases/B85/B85-C18-modelado-termico-por-nodos/CLASE.md).

### Balance de volumen

- El balance de volumen iguala el volumen evacuado con el hueco del hundimiento.

💡 **Cómo se explica en la clase [B70-C03](../programa/clases/B70/B70-C03-calderas-planetarias-formacion-y-colapso/CLASE.md):**
- *Descripción textual:* el volumen evacuado genera subpresión; si supera la resistencia de la falla anular el techo colapsa y el hundimiento sigue del balance de volumen.
- Calcular el hundimiento por balance de volumen.
- 🎯 **Por qué importa:** Evacuar magma no siempre hunde el techo. La decisión central: ¿cuánta subpresión resiste un techo y cuánto magma hay que sacar para vencerla?

📘 **Dónde se aprende** (1 clase): [B70-C03 · Calderas planetarias: formación y colapso](../programa/clases/B70/B70-C03-calderas-planetarias-formacion-y-colapso/CLASE.md).

### Balance detallado

- El balance detallado `πᵢPᵢⱼ = πⱼPⱼᵢ` es una condición suficiente de estacionariedad.
- El balance detallado exige en el estacionario que los flujos de ida y vuelta de cada par se igualen (aquí la red es una cadena).

💡 **Cómo se explica en la clase [B12-C13](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md):**
- Explicar el balance detallado y por qué garantiza la estacionariedad.
- Ejercicio 8. Comprueba el balance detallado entre los estados 1 y 2 del objetivo `(0,2; 0,5; 0,3)`.
- 🎯 **Por qué importa:** Una posterior de diez o veinte parámetros (órbita, calibración, ruido) no se puede tabular. Pero sí se pueden generar muestras que sigan su forma, aunque no se conozca su normalización.

📘 **Dónde se aprende** (2 clases): [B12-C13 · Cadenas de Markov y muestreo](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md); [B55-C20 · Modelo simplificado de red astroquímica](../programa/clases/B55/B55-C20-modelo-simplificado-de-red-astroquimica/CLASE.md).

### Balance geostrófico

- El balance geostrófico iguala la fuerza de presión (pendiente de la superficie) con la de Coriolis: `v = (g/f) ∂η/∂n`.

💡 **Cómo se explica en la clase [B57-C12](../programa/clases/B57/B57-C12-oceanografia-desde-orbita/CLASE.md):**
- El número de Rossby es `0,075`, pequeño: el balance geostrófico es razonable.
- ⚠️ **Error frecuente:** Aplicar el balance geostrófico en el ecuador. `f → 0` (ejercicio 5).
- 🎯 **Por qué importa:** El océano se mueve lento y se eleva más lento aún. La decisión central: ¿qué pendiente de la superficie equivale a una corriente y cuántos años de datos se necesitan para ver una tendencia de pocos milímetros por año entre un ruido de centímetros?

📘 **Dónde se aprende** (1 clase): [B57-C12 · Oceanografía desde órbita](../programa/clases/B57/B57-C12-oceanografia-desde-orbita/CLASE.md).

### Balance neto

- Carga base: consumo de la plataforma. Balance neto: entrada − salida.

💡 **Cómo se explica en la clase [B96-C12](../programa/clases/B96/B96-C12-gestion-de-energia-en-operaciones/CLASE.md):**
- El balance neto por orbita (entrada 41,43 Wh) es +15,92, +11,25, +11,25 y +8,92 Wh: positivo en los cuatro, por eso la batería se recarga.
- Calcular el balance neto de energía por órbita.
- 🎯 **Por qué importa:** Una batería descargada en exceso se degrada y una nave sin energía deja de ser comandable. La decisión central: ¿qué plan de operación mantiene la batería dentro de su criterio de descarga y recupera la carga en cada órbita?

📘 **Dónde se aprende** (1 clase): [B96-C12 · Gestión de energía en operaciones](../programa/clases/B96/B96-C12-gestion-de-energia-en-operaciones/CLASE.md).

### Balance proteico

- El balance proteico es síntesis menos degradación.

💡 **Cómo se explica en la clase [B105-C03](../programa/clases/B105/B105-C03-atrofia-muscular/CLASE.md):**
- C["carga y aporte<br/>reducidos"] --> B["balance proteico<br/>neto negativo"]
- *Descripción textual:* la carga y el aporte reducidos dejan un balance proteico negativo; la reserva decae de forma exponencial, el área baja y la fuerza máxima con ella, y se compara con lo que exige una tarea.
- 🎯 **Por qué importa:** Sin carga y sin aporte adecuado, el músculo se pierde más rápido que en la Tierra. La decisión central: ¿cuánta área y cuánta fuerza quedan tras 30, 90 y 180 días, y cuánto cambia una contramedida?

📘 **Dónde se aprende** (1 clase): [B105-C03 · Atrofia muscular](../programa/clases/B105/B105-C03-atrofia-muscular/CLASE.md).

### Balance radiativo

- El balance radiativo usa un albedo sintético de 0,3.
- El balance radiativo iguala la potencia absorbida más la disipada con la emitida: `ε σ A T⁴ = Q_abs + Q_int`.

💡 **Cómo se explica en la clase [B85-C01](../programa/clases/B85/B85-C01-balance-radiativo-de-satelite/CLASE.md):**
- La evidencia es la ficha de balance radiativo en caso caliente y frío del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de balance radiativo en caso caliente y frío*: términos de potencia, `T` en ambos casos, contraste con bisección y lista de lo consultado e ilustrativo.
- 🎯 **Por qué importa:** Las temperaturas de una nave no se miden primero: se predicen con un balance de energía. Un error de 30 K en el equilibrio decide si una batería sobrevive.

📘 **Dónde se aprende** (2 clases): [B54-C16 · Atmósferas de Titán](../programa/clases/B54/B54-C16-atmosferas-de-titan/CLASE.md); [B85-C01 · Balance radiativo de satélite](../programa/clases/B85/B85-C01-balance-radiativo-de-satelite/CLASE.md).

### Balanceado

- En un diseño balanceado, las medias cuadráticas `MSB` (entre) y `MSW` (dentro) estiman `σ_e² = MSW` y `σ_u² = (MSB − MSW)/n_t`, con `n_t` visitas por unidad.
- El mezclador balanceado cancela la fuga del OL o de la RF.

💡 **Cómo se explica en la clase [B12-C25](../programa/clases/B12/B12-C25-modelos-longitudinales-y-de-efectos-mixtos-para-muestras-pequenas/CLASE.md):**
- Paso 1 · Modelo. Intercepto aleatorio, balanceado.
- Estimar las varianzas dentro y entre unidades en un diseño balanceado y calcular el coeficiente de correlación intraclase (ICC).
- 🎯 **Por qué importa:** Seis personas medidas cuatro veces dan 24 números, pero no 24 piezas de información independientes: las de una misma persona se parecen. Ignorar eso produce intervalos demasiado angostos para el nivel medio y, paradójicamente, demasiado anchos para los cambios dentro de cada persona.

📘 **Dónde se aprende** (2 clases): [B12-C25 · Modelos longitudinales y de efectos mixtos para muestras pequeñas](../programa/clases/B12/B12-C25-modelos-longitudinales-y-de-efectos-mixtos-para-muestras-pequenas/CLASE.md); [B49-C11 · Mezcladores de frecuencia: pérdida de conversión y productos espurios](../programa/clases/B49/B49-C11-mezcladores-de-frecuencia-perdida-de-conversion-y-productos-espurios/CLASE.md).

### Balanceo

- El balanceo (*roll*) es el giro alrededor del eje óptico `z`.
- El cabeceo `θ` es la inclinación longitudinal (morro arriba) y el balanceo `φ` la lateral.
- El balanceo es la oscilación del ángulo.

💡 **Cómo se explica en la clase [B87-C07](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md):**
- El error `ΔA = Â Aᵀ` es una rotación pequeña `φ` cuyos dos primeros componentes son el error transversal y el tercero es el balanceo.
- El balanceo se mide con el brazo de palanca `ρ_rms` (el radio medio de las estrellas, unos `4,3°`), mucho menor que 1 rad: `σ_roll ≈ σ_a/(√N ρ_rms)`, del orden de `14` veces el error transversal con 20 estrellas.
- ⚠️ **Error frecuente:** Dar un solo número de precisión para los tres ejes. Separa transversal y balanceo (8.4)
- 🎯 **Por qué importa:** Para apuntar un telescopio o una antena con precisión de segundos de arco, un sensor solar o un magnetómetro no bastan. La decisión central: ¿cuántas estrellas hacen falta y por qué el giro alrededor del eje óptico (balanceo) es mucho peor que el apuntamiento?

📘 **Dónde se aprende** (3 clases): [B87-C07 · Rastreadores estelares](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md); [B102-C05 · Distribución de cargas y estabilidad ante vuelco](../programa/clases/B102/B102-C05-distribucion-de-cargas-y-estabilidad-ante-vuelco/CLASE.md); [B107-C07 · Rehabilitación vestibular y del equilibrio posterior al vuelo](../programa/clases/B107/B107-C07-rehabilitacion-vestibular-y-del-equilibrio-posterior-al-vuelo/CLASE.md).

### Balancín

- El balancín (rocker) une la rueda delantera con el pivote del cuerpo y con el bogie.

💡 **Cómo se explica en la clase [B102-C04](../programa/clases/B102/B102-C04-suspension-rocker-bogie-y-mecanica-de-rovers/CLASE.md):**
- Si la rueda delantera sube `h`, el balancín gira `θ = asin(h/(x₁ − x_B))` alrededor del bogie; el pivote sube `(x_P − x_B) sin θ`, y el diferencial reparte el movimiento entre los dos lados: el cabeceo del cuerpo es `θ/2` y su subida la mitad.
- F["carga F = M g / 2 en el pivote del cuerpo"] --> R["balancin"]
- ⚠️ **Error frecuente:** Confundir el cabeceo del cuerpo con el del balancín. Se corrige con 8.4
- 🎯 **Por qué importa:** Un rover cruza rocas sin muelles ni amortiguadores. La decisión central: ¿dónde colocar el pivote del cuerpo para repartir la carga, y qué escalón puede subir una rueda con la tracción disponible?

📘 **Dónde se aprende** (1 clase): [B102-C04 · Suspensión rocker-bogie y mecánica de rovers](../programa/clases/B102/B102-C04-suspension-rocker-bogie-y-mecanica-de-rovers/CLASE.md).

### Balanza triangular

- La balanza triangular reparte una fuerza entre tres puntos.

🎯 **Por qué importa (clase B43-C09):** Una celda que no reparte la carga como se diseñó deforma el espejo. La decisión central: ¿cómo se reparte el peso entre los puntos de apoyo y cuánto cambia si el pivote se desplaza unos milímetros?

📘 **Dónde se aprende** (1 clase): [B43-C09 · Celdas y soporte de espejos](../programa/clases/B43/B43-C09-celdas-y-soporte-de-espejos/CLASE.md).

### Balística radial

- Una trayectoria balística radial sube y cae por la sola gravedad.

💡 **Cómo se explica en la clase [B56-C10](../programa/clases/B56/B56-C10-oceanos-de-encelado/CLASE.md):**
- Definir penacho, velocidad de escape, apogeo y balística radial.
- 🎯 **Por qué importa:** El penacho permite muestrear un océano sin aterrizar. Para diseñar un sobrevuelo hace falta saber hasta dónde llegan los granos y cuáles escapan al anillo E.

📘 **Dónde se aprende** (1 clase): [B56-C10 · Océanos de Encélado](../programa/clases/B56/B56-C10-oceanos-de-encelado/CLASE.md).

### Baliza

- Una baliza es un cuerpo de efemérides conocida (clase C20 y C21).
- La baliza es un haz ancho que facilita esa búsqueda.
- Una baliza es un transmisor que da la posición.

💡 **Cómo se explica en la clase [B74-C13](../programa/clases/B74/B74-C13-navegacion-optica/CLASE.md):**
- Cada imagen de una baliza a distancia `ρ` con incertidumbre angular `σ` informa sobre la posición transversal a la línea de visión, con varianza `(ρσ)²`.
- Con balizas separadas 90° a 210°, la mayor incertidumbre por eje es `710,9 km`, con un `σ_3D = 951,9 km`.
- ⚠️ **Error frecuente:** Usar balizas casi alineadas. Pierde un eje; ver 8.3.
- 🎯 **Por qué importa:** Una dirección conocida con un microrradián son cientos de kilómetros a la distancia de un planeta. La decisión central: ¿cuánta incertidumbre de posición produce una cierta incertidumbre angular y cómo depende de la geometría de las balizas?

📘 **Dónde se aprende** (3 clases): [B74-C13 · Navegación óptica](../programa/clases/B74/B74-C13-navegacion-optica/CLASE.md); [B92-C03 · Adquisición, apuntamiento y seguimiento ópticos](../programa/clases/B92/B92-C03-adquisicion-apuntamiento-y-seguimiento-opticos/CLASE.md); [B104-C14 · Supervivencia en entorno terrestre](../programa/clases/B104/B104-C14-supervivencia-en-entorno-terrestre/CLASE.md).

### Balmer

- Una serie espectral es el conjunto de transiciones que terminan en el mismo nivel: la de Lyman termina en `n = 1` y la de Balmer en `n = 2`.
- La serie de Lyman (`n₁ = 1`), Balmer (`n₁ = 2`) y Paschen (`n₁ = 3`).

💡 **Cómo se explica en la clase [B06-C01](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md):**
- Si `n_bajo = 2` se obtiene la serie de Balmer, las únicas líneas del hidrógeno en el visible: H-alfa (3→2), H-beta (4→2), H-gamma (5→2) y H-delta (6→2).
- Cuando `n_alto` crece, las líneas se juntan hacia un límite de la serie: para Balmer, `λ = 4/R_H ≈ 364,7 nm`.
- 🎯 **Por qué importa:** Casi todo lo que sabemos de la composición de una estrella o de una nebulosa lo sabemos porque sus átomos emiten o absorben luz en colores muy precisos. Una línea roja a 656 nm no es «un color cualquiera»: es la firma del hidrógeno.

📘 **Dónde se aprende** (2 clases): [B06-C01 · Estructura atómica](../programa/clases/B06/B06-C01-estructura-atomica/CLASE.md); [B45-C10 · Líneas de emisión](../programa/clases/B45/B45-C10-lineas-de-emision/CLASE.md).

### Banco

- El banco es el conjunto de plantillas.

💡 **Cómo se explica en la clase [B28-C21](../programa/clases/B28/B28-C21-formas-de-onda-gravitacionales-y-filtro-acoplado/CLASE.md):**
- Para `M ≥ 0,97` (pérdida del 3 % de la señal-ruido) con el tiempo de coalescencia fijo, la masa de chirrido debe conocerse con `0,15 %`: el banco necesita plantillas muy próximas.
- Una llave casi igual pierde la mitad del ajuste, así que el banco debe tener llaves muy próximas.
- 🎯 **Por qué importa:** Una plantilla ligeramente errada pierde mucha señal-ruido, porque la fase acumula miles de ciclos. Entender cuánto determina cuántas plantillas hacen falta.

📘 **Dónde se aprende** (1 clase): [B28-C21 · Formas de onda gravitacionales y filtro acoplado](../programa/clases/B28/B28-C21-formas-de-onda-gravitacionales-y-filtro-acoplado/CLASE.md).

### Banco de casos

- El banco de casos: 1000 pares `(r1, r2)` con radios en 0,5–3 UA, ángulos aleatorios (a más de 3° de 0° y 180°) y tiempo de vuelo entre 0,05 y 1,5 veces el periodo de la órbita circular media.

💡 **Cómo se explica en la clase [B82-C07](../programa/clases/B82/B82-C07-benchmark-entre-solucionadores-de-lambert/CLASE.md):**
- B["banco: 1000 casos, semilla 82"] --> S1["universal biseccion"]
- Generar un banco reproducible de casos sintéticos con semilla fija.
- 🎯 **Por qué importa:** Elegir un solucionador sin medirlo es adivinar. La decisión central: ¿qué solucionador conviene para un banco de transferencias, y qué cifras sustentan esa elección?

📘 **Dónde se aprende** (1 clase): [B82-C07 · Benchmark entre solucionadores de Lambert](../programa/clases/B82/B82-C07-benchmark-entre-solucionadores-de-lambert/CLASE.md).

### Banco de datos espectroscópicos

- Un banco de datos espectroscópicos reúne frecuencias, intensidades y niveles con procedencia.

🎯 **Por qué importa (clase B62-C07):** Una identificación depende de una frecuencia, y esa frecuencia viene de un archivo que alguien ajustó y versionó. Si no sabes leer la columna de error, la unidad de la intensidad o la temperatura de referencia, importarás un error silencioso.

📘 **Dónde se aprende** (1 clase): [B62-C07 · Bancos de datos moleculares: CDMS, JPL, HITRAN y LAMDA](../programa/clases/B62/B62-C07-bancos-de-datos-moleculares-cdms-jpl-hitran-y-lamda/CLASE.md).

### Banco HIL

- El banco HIL conecta el hardware real con una planta simulada.

💡 **Cómo se explica en la clase [B88-C19](../programa/clases/B88/B88-C19-simulacion-hardware-in-the-loop/CLASE.md):**
- El banco debe añadir muy poco respecto del retardo que ya tiene la nave real: aquí, mucho menos de los `0,25 s` en que aparece el sobreimpulso.
- Límite: una nave real tiene sus propios retardos que el banco no debe sumar.
- ⚠️ **Error frecuente:** Ignorar el retardo del propio banco. Mídelo y réstalo (8.4)
- 🎯 **Por qué importa:** Si el banco añade retardo, las pruebas pueden mostrar inestabilidad que la nave no tendría, o esconder la que sí tendría. La decisión central: ¿cuánta latencia y jitter tolera el lazo sin perder su comportamiento, y por tanto qué exigirle al banco?

📘 **Dónde se aprende** (1 clase): [B88-C19 · Simulación hardware-in-the-loop](../programa/clases/B88/B88-C19-simulacion-hardware-in-the-loop/CLASE.md).

### Banda

- Una banda es un intervalo de energía.
- La banda es el intervalo de longitudes de onda observado.
- Una banda es una imagen en un intervalo espectral.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B28-C02](../programa/clases/B28/B28-C02-fotones-en-multiples-longitudes-de-onda/CLASE.md):**
- Cada banda es una ventana distinta al mismo objeto: el radio ve gas frío y electrones en campos magnéticos, el óptico ve estrellas, los rayos X ven gas a millones de grados.
- La evidencia es la ficha de bandas y temperaturas del ejercicio 12 (sección 20).
- ⚠️ **Error frecuente:** Tomar las bandas ilustrativas por límites oficiales. Se corrige con la sección 10.
- 🎯 **Por qué importa:** Cada banda revela un proceso distinto; combinarlas exige convertir bien las unidades y saber qué banda corresponde a qué temperatura. La decisión central: ¿en qué banda emite un objeto de temperatura dada y cómo se pasa de una magnitud a otra sin error?

📘 **Dónde se aprende** (6 clases): [B28-C02 · Fotones en múltiples longitudes de onda](../programa/clases/B28/B28-C02-fotones-en-multiples-longitudes-de-onda/CLASE.md); [B40-C14 · Productos de datos de Planck y misiones del CMB](../programa/clases/B40/B40-C14-productos-de-datos-de-planck-y-misiones-del-cmb/CLASE.md); [B43-C23 · Medición de rugosidad y su efecto en la luz dispersa](../programa/clases/B43/B43-C23-medicion-de-rugosidad-y-su-efecto-en-la-luz-dispersa/CLASE.md); [B44-C04 · Eficiencia cuántica espectral](../programa/clases/B44/B44-C04-eficiencia-cuantica-espectral/CLASE.md); [B57-C05 · Imágenes multiespectrales](../programa/clases/B57/B57-C05-imagenes-multiespectrales/CLASE.md); [B75-C29 · Análisis de calendario con gráficos pork-chop](../programa/clases/B75/B75-C29-analisis-de-calendario-con-graficos-pork-chop/CLASE.md).

### Banda alcanzable

- La banda alcanzable es la franja de latitudes `|φ| ≤ i` que sobrevuela la traza de la órbita.

💡 **Cómo se explica en la clase [B119-C02](../programa/clases/B119/B119-C02-acuerdo-de-salvamento/CLASE.md):**
- *Descripción textual:* la inclinación fija la banda alcanzable; de la banda se obtiene la probabilidad de caer en un territorio; con varios eventos se decide qué canales preparar.
- Descripción larga: la banda alcanzable cubre casi cuatro quintos de la superficie; la probabilidad por evento de caer en la banda sintética es pequeña pero crece con el número de eventos.
- ⚠️ **Error frecuente:** Creer que la banda alcanzable es toda la Tierra. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** El tratado de 1967 (C01) menciona la asistencia a los astronautas (art. V, no discutido en la fuente consultada); el Acuerdo de Salvamento la desarrolla, y ninguna otra clase la cubre.

📘 **Dónde se aprende** (1 clase): [B119-C02 · Acuerdo de Salvamento](../programa/clases/B119/B119-C02-acuerdo-de-salvamento/CLASE.md).

### Banda ancha

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B43-C24](../programa/clases/B43/B43-C24-recubrimientos-antirreflectantes-de-capas-multiples/CLASE.md):**
- Comparar la reflectancia media de banda ancha.
- 🎯 **Por qué importa:** Cada reflexión sin tratar pierde luz y añade luz parásita. La decisión central: ¿cuántas capas y con qué índices y espesores se logra baja reflectancia en la banda visible?

📘 **Dónde se aprende** (1 clase): [B43-C24 · Recubrimientos antirreflectantes de capas múltiples](../programa/clases/B43/B43-C24-recubrimientos-antirreflectantes-de-capas-multiples/CLASE.md).

### Banda C óptica

- La banda C óptica de la norma va de 191,3 a 195,9 THz (rejilla de 100 GHz de la UIT-T G.694.1).

💡 **Cómo se explica en la clase [B89-C18](../programa/clases/B89/B89-C18-comunicaciones-opticas-espaciales/CLASE.md):**
- La banda C óptica de la CCSDS 141.0-B-1 (191,3–195,9 THz) corresponde a `1530,33`–`1567,13 nm`.
- Convertir la banda óptica de la CCSDS 141.0-B-1 de frecuencia a longitud de onda.
- 🎯 **Por qué importa:** Las comunicaciones ópticas prometen más tasa por masa y potencia que la radio; entender el presupuesto de fotones y la modulación por posición de pulso explica por qué y a qué costo (apuntamiento, nubes). La decisión central: ¿cuántos fotones por bit llegan y qué error de símbolo implica la modulación PPM elegida?

📘 **Dónde se aprende** (1 clase): [B89-C18 · Comunicaciones ópticas espaciales](../programa/clases/B89/B89-C18-comunicaciones-opticas-espaciales/CLASE.md).

### Banda de absorción

- Ventana: rango de longitudes de onda con transmisión alta. Banda de absorción: rango con transmisión baja.

🎯 **Por qué importa (clase B48-C05):** Sin conocer la extinción, las magnitudes de distintas noches no se comparan. La decisión central: ¿qué extinción y qué incertidumbre tiene una serie de medidas?

📘 **Dónde se aprende** (1 clase): [B48-C05 · Ventanas atmosféricas](../programa/clases/B48/B48-C05-ventanas-atmosfericas/CLASE.md).

### Banda de cobertura

- La banda de cobertura es el rango de alturas con cobertura mínima fija.

💡 **Cómo se explica en la clase [B109-C08](../programa/clases/B109/B109-C08-diseno-inclusivo-en-habitats/CLASE.md):**
- La banda con cobertura `≥ 0,99` va de `820` a `1190 mm`; con `≥ 0,95`, de `780` a `1260`; con `≥ 0,90`, de `760` a `1330`.
- Encontrar la altura que maximiza la cobertura y las bandas con cobertura mínima.
- 🎯 **Por qué importa:** Un control puesto «a la altura normal» deja fuera a quien no la alcanza. La decisión central: ¿a qué altura (o con qué ajuste) un puesto sirve al mayor número de usuarios y a quién deja fuera?

📘 **Dónde se aprende** (1 clase): [B109-C08 · Diseño inclusivo en hábitats](../programa/clases/B109/B109-C08-diseno-inclusivo-en-habitats/CLASE.md).

### Banda de guarda

- Una banda de guarda resta `k u` al límite de aceptación.
- La banda de guarda separa canales vecinos.

💡 **Cómo se explica en la clase [B50-C14](../programa/clases/B50/B50-C14-criterios-de-aceptacion-strehl-error-de-frente-de-onda-y-especificaciones/CLASE.md):**
- La banda de guarda protege al consumidor y cuesta rechazos buenos.
- *Descripción textual:* el Strehl exacto se compara con Maréchal y la medida con incertidumbre se traduce en una decisión con banda de guarda.
- 🎯 **Por qué importa:** Una especificación solo sirve si se puede verificar con una medida que tiene incertidumbre. La decisión central: ¿cuánto margen se deja para que una medida incierta no acepte una unidad mala?

📘 **Dónde se aprende** (2 clases): [B50-C14 · Criterios de aceptación: Strehl, error de frente de onda y especificaciones](../programa/clases/B50/B50-C14-criterios-de-aceptacion-strehl-error-de-frente-de-onda-y-especificaciones/CLASE.md); [B89-C02 · Frecuencia y espectro espacial](../programa/clases/B89/B89-C02-frecuencia-y-espectro-espacial/CLASE.md).

### Banda de guarda w

- Incertidumbre de medida: dispersión asociada a la medida. Banda de guarda `w`: margen que se resta al límite para aceptar.

💡 **Cómo se explica en la clase [B90-C08](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md):**
- Los criterios estadísticos de decisión de esta clase (banda de guarda, PFA, PFR) no se consultaron en una norma; son relaciones estándar que se verifican en el laboratorio.
- Sin banda de guarda se acepta el 0,012 % de unidades malas y se rechaza el 0,019 % de buenas; con guarda `U` la falsa aceptación baja a 0,0003 % y el falso rechazo sube a 0,128 %.
- 🎯 **Por qué importa:** Toda medida tiene incertidumbre. Si se acepta con el límite exacto, algunas unidades malas pasan; si se endurece el criterio, algunas buenas se rechazan y cuesta tiempo.

📘 **Dónde se aprende** (1 clase): [B90-C08 · Procedimientos de prueba funcional](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md).

### Banda de infrarrojo medio

- Una banda de infrarrojo medio (3,9 µm) es muy sensible a temperaturas altas; la de infrarrojo térmico (11 µm) lo es al fondo.

🎯 **Por qué importa (clase B57-C16):** Un incendio pequeño puede ser un desastre en horas, pero un píxel mide cientos de metros. La decisión central: ¿cuál es la fracción de píxel más pequeña que se puede detectar y cuánto sesga la estimación un error en el fondo?

📘 **Dónde se aprende** (1 clase): [B57-C16 · Incendios forestales](../programa/clases/B57/B57-C16-incendios-forestales/CLASE.md).

### Banda espectral

- Una banda espectral es un intervalo de longitudes de onda donde un gas absorbe.
- La banda espectral tiene una respuesta espectral `S(λ)`; su ancho a media altura (FWHM) mide cuán estrecha es.

💡 **Cómo se explica en la clase [B57-C03](../programa/clases/B57/B57-C03-resolucion-radiometrica-y-espectral/CLASE.md):**
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de resoluciones radiométrica y espectral*: la tabla de bits, niveles y SQNR, el paso de cuantización en unidades físicas y el promedio de banda para un espectro lineal y uno con escalón.
- 🎯 **Por qué importa:** Dos sensores con el mismo píxel pueden dar información muy distinta si uno distingue 256 niveles y otro 65.536, o si una banda es ancha y otra estrecha. La decisión central: ¿cuántos bits y qué ancho de banda hacen falta para ver el cambio que me interesa?

📘 **Dónde se aprende** (3 clases): [B47-C20 · Caso comparativo de observatorios espaciales](../programa/clases/B47/B47-C20-caso-comparativo-de-observatorios-espaciales/CLASE.md); [B56-C14 · Biofirmas espectrales](../programa/clases/B56/B56-C14-biofirmas-espectrales/CLASE.md); [B57-C03 · Resolución radiométrica y espectral](../programa/clases/B57/B57-C03-resolucion-radiometrica-y-espectral/CLASE.md).

### Banda imagen

- La banda imagen `f_RF − 2 f_FI` también cae en la FI.

💡 **Cómo se explica en la clase [B49-C10](../programa/clases/B49/B49-C10-filtros-de-radiofrecuencia-pasabanda-y-rechazo-de-banda-imagen/CLASE.md):**
- Con una FI de 20 MHz la imagen cae dentro de la banda y ningún filtro razonable la rechaza: hay que subir la FI o usar un receptor de rechazo de imagen.
- Delta = 0.14085 ; f_FI = 100.0 MHz ; banda imagen en 1220.0 MHz ;
- 🎯 **Por qué importa:** Más orden rechaza más, pero también pierde más señal. La decisión central: ¿qué orden y qué ancho de banda dan el rechazo de imagen necesario con una pérdida aceptable?

📘 **Dónde se aprende** (1 clase): [B49-C10 · Filtros de radiofrecuencia pasabanda y rechazo de banda imagen](../programa/clases/B49/B49-C10-filtros-de-radiofrecuencia-pasabanda-y-rechazo-de-banda-imagen/CLASE.md).

### Banda limitada

- La banda limitada: señal sin potencia sobre cierta frecuencia.

💡 **Cómo se explica en la clase [B51-C08](../programa/clases/B51/B51-C08-compensacion-de-retardo-y-alineacion-temporal-de-flujos-de-antenas/CLASE.md):**
- La parábola está sesgada porque el pico de la correlación de una señal de banda limitada se parece a un seno cardinal y no a una parábola.
- Explicar por qué la parábola es sesgada en señales de banda limitada.
- ⚠️ **Error frecuente:** Usar la parábola con señales de banda limitada. Se corrige con 8.1.
- 🎯 **Por qué importa:** Un retardo mal compensado reduce la coherencia y en VLBI hace perder la detección. La decisión central: ¿cómo se estima y se aplica un retardo con fracción de muestra y qué correlación se espera tras alinear?

📘 **Dónde se aprende** (1 clase): [B51-C08 · Compensación de retardo y alineación temporal de flujos de antenas](../programa/clases/B51/B51-C08-compensacion-de-retardo-y-alineacion-temporal-de-flujos-de-antenas/CLASE.md).

### Banda muerta

- La banda muerta `±θ_db` es la zona sin acción.

💡 **Cómo se explica en la clase [B87-C13](../programa/clases/B87/B87-C13-propulsores-de-control-de-actitud/CLASE.md):**
- Con banda muerta de `±0,5°` y la ley «disparar en la pared si la velocidad no va ya hacia dentro», la velocidad queda en `±Δω` y el periodo es `4 θ_db/Δω`.
- Un ciclo límite sin perturbaciones gasta propergol continuamente; en la práctica se amplía la banda muerta o se usan ruedas y se reserva el propulsor para maniobras y descargas.
- ⚠️ **Error frecuente:** Creer que la banda muerta se reduce sin costo. Revisa el periodo `∝ θ_db` (8.3)
- 🎯 **Por qué importa:** Los propulsores son el actuador de más par y de respuesta rápida, y el único que cambia el momento total del satélite, pero cada pulso gasta masa que no vuelve. La decisión central: ¿cuánto propergol cuesta una maniobra o un año de mantenimiento de actitud, y qué precisión permite el impulso mínimo?

📘 **Dónde se aprende** (1 clase): [B87-C13 · Propulsores de control de actitud](../programa/clases/B87/B87-C13-propulsores-de-control-de-actitud/CLASE.md).

### Banda prohibida

- La banda prohibida `E_g` es la energía mínima para liberar un electrón en el semiconductor.

💡 **Cómo se explica en la clase [B44-C01](../programa/clases/B44/B44-C01-principios-fotoelectricos/CLASE.md):**
- *Descripción textual:* la longitud de onda fija la energía; si supera la banda prohibida se libera un electrón y el número de eventos sigue una distribución de Poisson.
- El silicio con una banda prohibida de `1,12 eV` (valor ilustrativo) deja de absorber por encima de `1107,0 nm`.
- 🎯 **Por qué importa:** Todo lo que mide un detector parte de un fotón que cede su energía a un electrón. La decisión central: ¿qué fotones puede registrar un material y con qué fluctuación mínima?

📘 **Dónde se aprende** (1 clase): [B44-C01 · Principios fotoeléctricos](../programa/clases/B44/B44-C01-principios-fotoelectricos/CLASE.md).

### Baricentro

- El baricentro es el centro de masas del par.
- El baricentro es el centro de masa; el marco del baricentro tiene momento total nulo.
- El baricentro es el centro de masa común.

💡 **Cómo se explica en la clase [B71-C03](../programa/clases/B71/B71-C03-ecuacion-de-movimiento-de-dos-cuerpos/CLASE.md):**
- El baricentro está a `a m₂/(m₁ + m₂)` del cuerpo 1.
- Para Tierra–Luna, `m_T/m_L = 81.30` y el baricentro queda a `4670793` m del centro de la Tierra, `0.733` radios terrestres: dentro del planeta, pero lejos de ser despreciable.
- 🎯 **Por qué importa:** Casi toda la mecánica orbital parte de esta ecuación; entender qué supone (cuerpos puntuales, sin otras fuerzas) permite saber cuándo falla. La decisión central: ¿qué resuelve exactamente la ecuación de dos cuerpos y cómo compruebas que tu integración numérica es fiable?

📘 **Dónde se aprende** (3 clases): [B71-C03 · Ecuación de movimiento de dos cuerpos](../programa/clases/B71/B71-C03-ecuacion-de-movimiento-de-dos-cuerpos/CLASE.md); [B73-C08 · Sistemas de N cuerpos](../programa/clases/B73/B73-C08-sistemas-de-n-cuerpos/CLASE.md); [B76-C01 · Sistema Tierra-Luna](../programa/clases/B76/B76-C01-sistema-tierra-luna/CLASE.md).

### Baricentro Tierra–Luna

- El geocentro es el centro de la Tierra, distinto del baricentro Tierra–Luna.

💡 **Cómo se explica en la clase [B23-C05](../programa/clases/B23/B23-C05-validacion-con-conjuntos-oficiales/CLASE.md):**
- Se investiga en vez de ensanchar: la Tierra (geocentro) orbita el baricentro Tierra–Luna, y la velocidad del geocentro oscila unos 12 m/s (valor aproximado, de conocimiento general, no consultado); sobre 29,8 km/s, `2·δv/v ≈ 8 × 10⁻⁴`, del orden observado.
- [contexto] oscilación del geocentro respecto del baricentro Tierra-Luna ≈ 3.1e-05 au (valor aproximado, no consultado)
- 🎯 **Por qué importa:** Un modelo kepleriano de la Tierra pasó todas las pruebas de C01–C04, pero eso no dice nada sobre si la Tierra se mueve como una elipse perfecta. La pregunta motivadora es: ¿contra qué contrasto mi modelo, y qué diferencia estoy dispuesto a aceptar?

📘 **Dónde se aprende** (1 clase): [B23-C05 · Validación con conjuntos oficiales](../programa/clases/B23/B23-C05-validacion-con-conjuntos-oficiales/CLASE.md).

### Barlow

- Un reductor y un barlow.

💡 **Cómo se explica en la clase [B41-C11](../programa/clases/B41/B41-C11-campo-visual-y-escala-de-placa/CLASE.md):**
- Un reductor ensancha el campo pero submuestrea (`1,42` píxeles por FWHM de seeing); un barlow sobremuestrea el seeing y no gana detalle real.
- 🎯 **Por qué importa:** Un sensor mal emparejado desperdicia resolución o campo. La decisión central: ¿qué focal y qué píxel dan el campo y el muestreo que busco?

📘 **Dónde se aprende** (1 clase): [B41-C11 · Campo visual y escala de placa](../programa/clases/B41/B41-C11-campo-visual-y-escala-de-placa/CLASE.md).

### Barometría inversa

- La barometría inversa es la respuesta del nivel del mar a la presión: alta presión baja el nivel.

💡 **Cómo se explica en la clase [B57-C29](../programa/clases/B57/B57-C29-correcciones-atmosfericas-en-altimetria/CLASE.md):**
- La barometría inversa da `9,95 mm` de nivel por hPa; 30 hPa de presión equivalen a unos `29,8 cm`.
- Relacionar presión y nivel del mar con la barometría inversa.
- ⚠️ **Error frecuente:** Confundir el retardo con la barometría inversa. Se aclara en 8.4.
- 🎯 **Por qué importa:** Un error de decímetros en la distancia equivale a decímetros de error en la altura del mar, mayor que las señales que se buscan. La decisión central: ¿qué corrección aplicar a cada retardo y cuánto ruido agrega?

📘 **Dónde se aprende** (1 clase): [B57-C29 · Correcciones atmosféricas en altimetría](../programa/clases/B57/B57-C29-correcciones-atmosfericas-en-altimetria/CLASE.md).

### Barorreflejo

- El barorreflejo ajusta frecuencia y resistencia según la presión.

💡 **Cómo se explica en la clase [B105-C01](../programa/clases/B105/B105-C01-respuesta-cardiovascular-a-microgravedad/CLASE.md):**
- *Descripción textual:* la gravedad efectiva fija el gradiente hidrostático; sin él, el líquido se redistribuye hacia la cabeza y cambia el volumen y la precarga; con menos precarga cae el volumen sistólico, el barorreflejo compensa en parte y la presión media en la cabeza de pie queda más cerca del umbral.
- Límite: los vasos se contraen, tienen válvulas y el corazón se adapta; el modelo ignora todo eso salvo un barorreflejo simple.
- 🎯 **Por qué importa:** En la Tierra la gravedad empuja la sangre hacia los pies y el sistema cardiovascular lo compensa en cada postura. En microgravedad esa carga desaparece y el cuerpo se reajusta; al volver, la compensación puede no bastar.

📘 **Dónde se aprende** (1 clase): [B105-C01 · Respuesta cardiovascular a microgravedad](../programa/clases/B105/B105-C01-respuesta-cardiovascular-a-microgravedad/CLASE.md).

### Barra

- El bulbo es la concentración central de estrellas viejas, con forma de caja o cacahuete; la barra es su extensión alargada (C02).
- La barra es una estructura alargada en estrellas, con ángulo `φ` entre su eje mayor y la línea Sol–centro.

💡 **Cómo se explica en la clase [B25-C01](../programa/clases/B25/B25-C01-estructura-de-la-via-lactea/CLASE.md):**
- Eso deja `~1 × 10¹⁰ M☉` para el bulbo y la barra dentro de la masa estelar total de `5 × 10¹⁰`: una consistencia, no una medida.
- Paso 5 · Sentido. La parte estelar del disco ronda un tercio de la masa interior estimada; el resto es bulbo, barra, gas y, sobre todo, un halo oscuro.
- 🎯 **Por qué importa:** Estamos dentro de la galaxia y no podemos fotografiarla desde fuera: su forma se reconstruye midiendo distancias y velocidades desde un punto que no es el centro. Sin un esquema claro de componentes (bulbo, barra, disco, halo) y de cifras de referencia, el resto del bloque carece de escala.

📘 **Dónde se aprende** (2 clases): [B25-C01 · Estructura de la Vía Láctea](../programa/clases/B25/B25-C01-estructura-de-la-via-lactea/CLASE.md); [B25-C02 · Brazos espirales y barra galáctica](../programa/clases/B25/B25-C02-brazos-espirales-y-barra-galactica/CLASE.md).

### Barredor

- El barredor (*pushbroom*) forma la imagen línea a línea con el movimiento del satélite.

🎯 **Por qué importa (clase B57-C04):** Un sensor puede tener muchos píxeles y aun así ser inútil porque cada píxel recoge pocos fotones. La decisión central: ¿cuánta apertura y cuánto tiempo de integración hacen falta para que la señal supere el ruido de fotones?

📘 **Dónde se aprende** (1 clase): [B57-C04 · Satélites ópticos de observación](../programa/clases/B57/B57-C04-satelites-opticos-de-observacion/CLASE.md).

### Barrera

- Una barrera es una medida que impide un paso del material; su probabilidad de fallo `p` es ilustrativa aquí.
- Una barrera es una defensa con probabilidad de falla `q`.
- Una barrera retiene parte del polvo.

💡 **Cómo se explica en la clase [B63-C04](../programa/clases/B63/B63-C04-misiones-de-retorno-de-muestras-salvaguardas-historicas-y-regulatorias/CLASE.md):**
- Con barreras independientes de fallo `pᵢ`, la probabilidad de que el material salga es `P = Π pᵢ`.
- Con las cuatro barreras sintéticas `0,01`, `0,02`, `0,05` y `0,10`, `P = 1,000 × 10⁻⁶`.
- ⚠️ **Error frecuente:** Creer que más barreras siempre bajan la fuga. Con causa común hay un piso.
- 🎯 **Por qué importa:** Traer material de otro cuerpo exige proteger a la Tierra y a la muestra. La decisión central: ¿cuántas barreras independientes hacen falta, y qué pasa si dejan de ser independientes?

📘 **Dónde se aprende** (3 clases): [B63-C04 · Misiones de retorno de muestras: salvaguardas históricas y regulatorias](../programa/clases/B63/B63-C04-misiones-de-retorno-de-muestras-salvaguardas-historicas-y-regulatorias/CLASE.md); [B109-C04 · Mitigación de polvo lunar en accesos y hábitats](../programa/clases/B109/B109-C04-mitigacion-de-polvo-lunar-en-accesos-y-habitats/CLASE.md); [B111-C06 · Gestión del error humano y cultura de seguridad](../programa/clases/B111/B111-C06-gestion-del-error-humano-y-cultura-de-seguridad/CLASE.md).

### Barrera de Coulomb

- La barrera de Coulomb es la repulsión eléctrica entre núcleos.
- La barrera de Coulomb `Z₁Z₂αħc/R`.

🎯 **Por qué importa (clase B24-C07):** Dos protones se repelen con una fuerza eléctrica enorme; a las temperaturas de una estrella casi ninguno tiene energía para acercarse lo suficiente. Aun así la fusión ocurre, por efecto túnel.

📘 **Dónde se aprende** (2 clases): [B24-C07 · Ciclo CNO y cadena protón-protón](../programa/clases/B24/B24-C07-ciclo-cno-y-cadena-proton-proton/CLASE.md); [B31-C07 · Estructura nuclear](../programa/clases/B31/B31-C07-estructura-nuclear/CLASE.md).

### Barrera de rotación

- La barrera de rotación es el periodo mínimo sin cohesión.

💡 **Cómo se explica en la clase [B58-C14](../programa/clases/B58/B58-C14-efectos-yarkovsky-y-yorp/CLASE.md):**
- Barrera de rotacion (rho = 1000 kg/m3): P_min = 3.301 h
- Barrera de rotacion (rho = 2000 kg/m3): P_min = 2.334 h
- 🎯 **Por qué importa:** Una deriva de decenas de kilómetros en un siglo puede decidir si un acercamiento ocurre. La decisión central: ¿cuánto se desplaza un asteroide por empuje térmico y por qué los cuerpos pequeños son más sensibles?

📘 **Dónde se aprende** (1 clase): [B58-C14 · Efectos Yarkovsky y YORP](../programa/clases/B58/B58-C14-efectos-yarkovsky-y-yorp/CLASE.md).

### Barrido

- El barrido es la medición paso a paso.
- El barrido es el ancho de la franja que se imagina en cada pasada.
- El barrido repite el método con resoluciones distintas (`N = 2ᵏ`).
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B11-C26](../programa/clases/B11/B11-C26-benchmark-de-algoritmos-numericos/CLASE.md):**
- Barrido: `N = 2ᵏ` pasos para los fijos y tolerancias `10⁻⁴ … 10⁻¹⁰` para el adaptativo.
- Evaluaciones mínimas del barrido para alcanzar cada error objetivo:
- 🎯 **Por qué importa:** «El método A es mejor que el B» es una afirmación vacía sin el problema, la métrica, la tolerancia y el costo. Una comparación mal diseñada lleva a elegir el algoritmo equivocado para una misión.

📘 **Dónde se aprende** (6 clases): [B11-C26 · Benchmark de algoritmos numéricos](../programa/clases/B11/B11-C26-benchmark-de-algoritmos-numericos/CLASE.md); [B16-C19 · Verificación de lazo cerrado](../programa/clases/B16/B16-C19-verificacion-de-lazo-cerrado/CLASE.md); [B49-C05 · Medición y calibración de patrones de antena](../programa/clases/B49/B49-C05-medicion-y-calibracion-de-patrones-de-antena/CLASE.md); [B57-C02 · Resolución espacial y temporal](../programa/clases/B57/B57-C02-resolucion-espacial-y-temporal/CLASE.md); [B75-C12 · Optimización de trayectoria](../programa/clases/B75/B75-C12-optimizacion-de-trayectoria/CLASE.md); [B88-C04 · Memorias y corrección de errores](../programa/clases/B88/B88-C04-memorias-y-correccion-de-errores/CLASE.md).

### Barrido de períodos

- El barrido de períodos prueba muchos períodos y elige el que mejor apila las caídas.

💡 **Cómo se explica en la clase [B131-C06](../programa/clases/B131/B131-C06-aprendizaje-basado-en-problemas-con-datos-astronomicos/CLASE.md):**
- El barrido de `1,0` a `8,0 d` con paso `0,002 d` da el mejor período `3,202 d` (inyectado `3,2`), con una SNR del barrido de `25,5`.
- Con ruido `0,002`, el período sale `3,200 d` y SNR `24,0`; con `0,010`, `3,200 d` y SNR `7,5`; con `0,030`, el barrido da `3,815 d`, un período falso y SNR `4,4`.
- 🎯 **Por qué importa:** Un problema con datos reales o realistas enseña más que un ejercicio con respuesta única, pero exige diseñar qué se espera. La decisión central: ¿qué sabe el estudiante al empezar, qué datos recibe y cómo comprobará su respuesta?

📘 **Dónde se aprende** (1 clase): [B131-C06 · Aprendizaje basado en problemas con datos astronómicos](../programa/clases/B131/B131-C06-aprendizaje-basado-en-problemas-con-datos-astronomicos/CLASE.md).

### Barrido de ruido

- Un barrido de ruido repite la prueba con distintos niveles de ruido.

💡 **Cómo se explica en la clase [B22-C05](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md):**
- Pido espectros generados con un modelo distinto (otra rejilla, otra física de detalle), un barrido de ruido y la cobertura de los intervalos.
- Ejercicio 12 · integrador. Diseña el protocolo de prueba sintética de una inversión propia: verdad, generador, inversor, ruido, semillas, métrica, barrido, cobertura y declaración de límites.
- 🎯 **Por qué importa:** Con datos reales no conoces la verdad, así que no puedes medir el error de tu inversión. Con datos sintéticos sí: tú fijas la verdad, generas los datos y miras si el método la recupera.

📘 **Dónde se aprende** (1 clase): [B22-C05 · Pruebas de inversión con datos sintéticos](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md).

### Barrido Monte Carlo

- Un barrido Monte Carlo repite una simulación con parámetros aleatorios.

💡 **Cómo se explica en la clase [B16-C16](../programa/clases/B16/B16-C16-control-robusto-inicial/CLASE.md):**
- Cuantificar la dispersión del desempeño con un barrido aleatorio (Monte Carlo).
- Ejercicio 12 · integrador. Entrega un informe de robustez: para un lazo de tu elección, declara la incertidumbre (rango y origen), calcula `Ms` y `Mt`, aplica la ganancia pequeña, compara con el análisis por polos en un barrido y con Routh, y da un Monte Carlo con semilla.
- 🎯 **Por qué importa:** La inercia de un satélite cambia al desplegar paneles, consumir propergol o capturar una carga; el actuador envejece; el sensor tiene un retardo que no se conocía. El lazo diseñado con la inercia nominal debe seguir funcionando.

📘 **Dónde se aprende** (1 clase): [B16-C16 · Control robusto inicial](../programa/clases/B16/B16-C16-control-robusto-inicial/CLASE.md).

### Barrido senoidal de verificación

- Ecuación de Miles: aproximación de la respuesta rms para un oscilador de banda estrecha con PSD plana. Barrido senoidal de verificación: barrido de baja amplitud antes y después que detecta cambios de resonancia.

🎯 **Por qué importa (clase B90-C09):** Un espectro se especifica con una curva; lo que importa al hardware es cuánto se amplifica en sus resonancias. La decisión central: ¿qué nivel y duración de ensayo hay que aplicar y qué carga ve un equipo con una resonancia dada?

📘 **Dónde se aprende** (1 clase): [B90-C09 · Ensayos de vibración](../programa/clases/B90/B90-C09-ensayos-de-vibracion/CLASE.md).

### Base

- La base (o referencia) es la cantidad respecto de la cual se expresa el porcentaje.
- `a` es la base y `n` el exponente.
- El paralaje es el cambio de dirección de un objeto visto desde dos puntos distintos; la base es la distancia entre ellos.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C03](../programa/clases/B03/B03-C03-porcentajes-y-escalas-comparativas/CLASE.md):**
- Los mismos dos valores dan dos porcentajes distintos porque la base cambia.
- No se anulan, porque la segunda operación toma como base el valor ya modificado.
- ⚠️ **Error frecuente:** Olvidar la base. Ejercicios 4 y 11.
- 🎯 **Por qué importa:** La Tierra no gira en un círculo: su distancia al Sol varía a lo largo del año. ¿Mucho o poco?

📘 **Dónde se aprende** (8 clases): [B03-C03 · Porcentajes y escalas comparativas](../programa/clases/B03/B03-C03-porcentajes-y-escalas-comparativas/CLASE.md); [B03-C04 · Potencias y raíces](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md); [B03-C18 · Razones trigonométricas iniciales](../programa/clases/B03/B03-C18-razones-trigonometricas-iniciales/CLASE.md); [B04-C07 · Triángulos y distancias angulares](../programa/clases/B04/B04-C07-triangulos-y-distancias-angulares/CLASE.md); [B04-C20 · Triangulación espacial aplicada](../programa/clases/B04/B04-C20-triangulacion-espacial-aplicada/CLASE.md); [B06-C15 · Ácidos, bases y soluciones](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md) y 2 más.

### Base 2

- La base 2 es el caso `N = 2^m`.

💡 **Cómo se explica en la clase [B15-C05](../programa/clases/B15/B15-C05-transformada-rapida-de-fourier/CLASE.md):**
- La FFT propia de base 2 enseña el mecanismo y exige `N = 2^m`.
- Ejercicio 12 · integrador. Elabora tu *tabla de coste y exactitud*: implementa una FFT de base 2, y para `N = 2³ … 2¹³` (saltando de 2 en 2) tabula mariposas contadas, fórmula, razón con `N²` y diferencia máxima con `numpy.fft.fft`; añade tres tiempos orientativos y la advertencia de que dependen del equipo.
- ⚠️ **Error frecuente:** Aplicar una FFT de base 2 a un `N` que no lo es. La implementación propia debe fallar o rellenar; se declara.
- 🎯 **Por qué importa:** Una curva de luz de 27 días con cadencia de 2 minutos tiene 19 440 muestras. La suma directa de la DFT necesita unos 378 millones de multiplicaciones complejas; una imagen de 1024 × 1024 necesitaría muchísimas más.

📘 **Dónde se aprende** (1 clase): [B15-C05 · Transformada rápida de Fourier](../programa/clases/B15/B15-C05-transformada-rapida-de-fourier/CLASE.md).

### Base cinética

- Una base cinética reúne reacciones con sus parámetros, incertidumbres e intervalos de validez.

💡 **Cómo se explica en la clase [B60-C02](../programa/clases/B60/B60-C02-coeficientes-de-velocidad-dependientes-de-la-temperatura-y-bases-cineticas/CLASE.md):**
- python programa/clases/B60/B60-C02-coeficientes-de-velocidad-dependientes-de-la-temperatura-y-bases-cineticas/coeficientes.py
- 🎯 **Por qué importa:** Un modelo de nube a 10 K usa coeficientes que se midieron o calcularon a otras temperaturas. La decisión central: ¿hasta dónde se puede confiar en un ajuste de `k(T)` fuera del intervalo donde se ajustó?

📘 **Dónde se aprende** (1 clase): [B60-C02 · Coeficientes de velocidad dependientes de la temperatura y bases cinéticas](../programa/clases/B60/B60-C02-coeficientes-de-velocidad-dependientes-de-la-temperatura-y-bases-cineticas/CLASE.md).

### Base conjugada

- Al ceder el protón, un ácido `HA` da su base conjugada `A⁻`; al aceptarlo, una base `B` da su ácido conjugado `BH⁺`.

💡 **Cómo se explica en la clase [B06-C15](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md):**
- A["Ácido HA"] -->|"cede H+"| B["Base conjugada A−"]
- *Descripción textual:* a la izquierda, un ácido que cede un protón y se convierte en su base conjugada; abajo, una base que acepta un protón y se convierte en su ácido conjugado.
- 🎯 **Por qué importa:** El extracto en agua caliente de las muestras de Bennu contiene amoníaco libre en unos 13,6 μmol por gramo y ácido fórmico en 4,106 μmol por gramo (S1). Un ácido y una base en el mismo líquido reaccionan entre sí: el ácido cede un protón, la base lo acepta y se forman iones.

📘 **Dónde se aprende** (1 clase): [B06-C15 · Ácidos, bases y soluciones](../programa/clases/B06/B06-C15-acidos-bases-y-soluciones/CLASE.md).

### Base de datos de telemetría y comandos

- La base de datos de telemetría y comandos (TM/TC) lista cada parámetro con su identificador, unidad, calibración y límites, y cada comando con sus argumentos.

💡 **Cómo se explica en la clase [B83-C19](../programa/clases/B83/B83-C19-aceptacion-y-transferencia-a-operaciones/CLASE.md):**
- Describir qué contiene una base de datos de telemetría y comandos.
- 🎯 **Por qué importa:** Un satélite entregado con una base de datos errónea muestra valores falsos o alarmas inútiles; operadores sin entrenamiento no saben responder. La decisión central: ¿la base de datos, los comandos y las personas están listos, de modo que operaciones pueda recibir el sistema?

📘 **Dónde se aprende** (1 clase): [B83-C19 · Aceptación y transferencia a operaciones](../programa/clases/B83/B83-C19-aceptacion-y-transferencia-a-operaciones/CLASE.md).

### Base libre

- Base libre: base sin fuerzas externas.

💡 **Cómo se explica en la clase [B101-C06](../programa/clases/B101/B101-C06-simulacion-de-un-brazo-robotico-espacial/CLASE.md):**
- Masas, inercias y la dinámica real no se consultaron; el modelo de base libre de la clase es estándar y se verifica con sus conservaciones (N5).
- Plantear la conservación del centro de masa y del momento angular de un sistema con base libre.
- 🎯 **Por qué importa:** En una estación o un satélite pesado la base casi no se mueve; en un satélite pequeño, sí. La decisión central: ¿cuánto se mueve la base al mover el brazo y cómo afecta eso a la posición del extremo?

📘 **Dónde se aprende** (1 clase): [B101-C06 · Simulación de un brazo robótico espacial](../programa/clases/B101/B101-C06-simulacion-de-un-brazo-robotico-espacial/CLASE.md).

### Base ortonormal

- Una base ortonormal tiene vectores perpendiculares entre sí y de longitud 1 (S1: ortogonalidad, ec. 1.2.44).

💡 **Cómo se explica en la clase [B10-C02](../programa/clases/B10/B10-C02-bases-y-dimension/CLASE.md):**
- Si la base es ortonormal, `c_k = b_k · v`: no hay que resolver nada.
- Una base ortonormal es cómoda (coordenadas por producto escalar) y numéricamente estable.
- ⚠️ **Error frecuente:** Usar `c_k = b_k · v` con una base no ortonormal. Se corrige con el ejercicio 2.
- 🎯 **Por qué importa:** Un vector es una entidad geométrica; sus «componentes» dependen de los ejes que elijas. Un operador de estación terrestre describe un satélite con ejes ligados al ecuador; el satélite mismo, con ejes ligados a su órbita; un instrumento, con ejes del instrumento.

📘 **Dónde se aprende** (1 clase): [B10-C02 · Bases y dimensión](../programa/clases/B10/B10-C02-bases-y-dimension/CLASE.md).

### Base polinómica

- La base polinómica `w = Σ c_k ρ^(2k)`.

💡 **Cómo se explica en la clase [B43-C08](../programa/clases/B43/B43-C08-montaje-de-espejo-primario/CLASE.md):**
- E["energía de Kirchhoff"] --> B["base polinómica"]
- Resolver con una base polinómica y un multiplicador de Lagrange.
- 🎯 **Por qué importa:** Un apoyo mal elegido deja un error de forma que ninguna pieza posterior corrige. La decisión central: ¿en qué radio conviene apoyar el espejo para que, tras quitar piston y desenfoque, quede el menor error?

📘 **Dónde se aprende** (1 clase): [B43-C08 · Montaje de espejo primario](../programa/clases/B43/B43-C08-montaje-de-espejo-primario/CLASE.md).

### Base radial (RBF)

- Un proceso gaussiano es un modelo que para cada entrada da una distribución normal; su núcleo (*kernel*) define cuánto se parecen las salidas de dos entradas cercanas, y el de base radial (RBF) tiene una longitud de escala por variable (S1).

🎯 **Por qué importa (clase B17-C04):** Un simulador de trayectoria, de aerodinámica o de transporte de radiación puede tardar minutos u horas por ejecución. Para explorar miles de combinaciones de parámetros (un análisis de sensibilidad, una propagación de incertidumbre, una optimización) no alcanza el tiempo.

📘 **Dónde se aprende** (1 clase): [B17-C04 · Modelos sustitutos (surrogates)](../programa/clases/B17/B17-C04-modelos-sustitutos-surrogates/CLASE.md).

### Basquin

- El tamaño crítico `a_c = (K_Ic/(Y σ_max))²/π` es donde `K = K_Ic`. Basquin: `S_a = S_f′ (2N)^b`.

💡 **Cómo se explica en la clase [B84-C08](../programa/clases/B84/B84-C08-fatiga-y-fractura/CLASE.md):**
- *Descripción textual:* los datos dan el tamaño crítico y los ciclos por dos vías (cerrada y numérica); por separado, Basquin y Miner dan el daño de un espectro.
- Evaluar la vida con Basquin y la corrección de Goodman.
- 🎯 **Por qué importa:** La mayoría de las fallas estructurales en servicio son por fatiga; saber cuántos ciclos quedan y qué grieta es tolerable decide si una pieza se acepta. La decisión central: ¿cuántos ciclos tarda una grieta inicial en llegar al tamaño crítico y cuánto daño acumula un espectro de cargas?

📘 **Dónde se aprende** (1 clase): [B84-C08 · Fatiga y fractura](../programa/clases/B84/B84-C08-fatiga-y-fractura/CLASE.md).

### Batidos

- Los batidos son la variación de amplitud al superponer dos frecuencias cercanas, a la frecuencia diferencia.

💡 **Cómo se explica en la clase [B05-C12](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md):**
- Si suenan a la vez 440 Hz y 444 Hz, se oye una variación de volumen a `|f₁ − f₂| = 4 Hz`: los batidos.
- Interpretar superposición, ondas estacionarias y batidos.
- 🎯 **Por qué importa:** Un sensor de vibración a bordo de una nave registra 30 Hz cuando la estructura vibra a 130 Hz. Un trueno llega segundos después del rayo.

📘 **Dónde se aprende** (1 clase): [B05-C12 · Ondas mecánicas y frecuencia](../programa/clases/B05/B05-C12-ondas-mecanicas-y-frecuencia/CLASE.md).

### Bayesiano

- El criterio de información de Akaike es `AIC = 2k − 2 ln L_max`, con `k` parámetros; el bayesiano es `BIC = k ln n − 2 ln L_max`, con `n` datos.
- El método clásico y el bayesiano.

💡 **Cómo se explica en la clase [B31-C18](../programa/clases/B31/B31-C18-restricciones-experimentales-de-teorias/CLASE.md):**
- Con 0 eventos y fondo 1,2, el método clásico da un límite menor (1,10) que sin fondo (2,30): el efecto se conoce como el problema del fondo, y el bayesiano con a priori uniforme no cambia (2,30).
- N --> BA["bayesiano: a priori uniforme"]
- 🎯 **Por qué importa:** Un límite mal calculado puede excluir una teoría que no estaba excluida. La decisión central: ¿qué señal máxima es compatible con lo observado y cuán fiable es el método?

📘 **Dónde se aprende** (2 clases): [B12-C22 · Comparación de modelos: evidencia bayesiana y criterios de información](../programa/clases/B12/B12-C22-comparacion-de-modelos-evidencia-bayesiana-y-criterios-de-informacion/CLASE.md); [B31-C18 · Restricciones experimentales de teorías](../programa/clases/B31/B31-C18-restricciones-experimentales-de-teorias/CLASE.md).

### BCET

- El BCET es la inferior.

💡 **Cómo se explica en la clase [B88-C30](../programa/clases/B88/B88-C30-analisis-de-peor-caso-de-tiempo-de-ejecucion-wcet/CLASE.md):**
- El script [wcet.py](wcet.py) calcula el WCET y el BCET estáticos, mide 100 000 entradas aleatorias, estima el efecto de la caché y convierte a µs y utilización, y comprueba que el máximo medido no supera la cota.
- 🎯 **Por qué importa:** El análisis de planificación (C05) necesita `C` de cada tarea, y medir no basta porque el peor camino puede no ejercitarse. La decisión central: ¿cuál es una cota segura del tiempo de ejecución y cuánto pesimismo trae?

📘 **Dónde se aprende** (1 clase): [B88-C30 · Análisis de peor caso de tiempo de ejecución (WCET)](../programa/clases/B88/B88-C30-analisis-de-peor-caso-de-tiempo-de-ejecucion-wcet/CLASE.md).

### BDF2

- Euler implícito: `y_{n+1} = y_n + h f(t_{n+1}, y_{n+1})`. BDF2 (fórmula de diferenciación hacia atrás de orden 2): `y_{n+1} = (4 y_n − y_{n−1})/3 + (2h/3) f(t_{n+1}, y_{n+1})`.

💡 **Cómo se explica en la clase [B11-C22](../programa/clases/B11/B11-C22-metodos-implicitos-y-sistemas-rigidos/CLASE.md):**
- BDF2 `1,6 × 10⁻⁸ … 2,5 × 10⁻¹⁰`, órdenes `2,00`; trapezoidal `4,0 × 10⁻⁹ … 6,3 × 10⁻¹¹`, órdenes `2,00`.
- Con una condición inicial fuera de la solución lenta (`y(0) = 3,5`) y `h = 0,01`: BDF2 elimina el transitorio (desvío `4 × 10⁻⁹` en la mitad final);
- 🎯 **Por qué importa:** Los modelos térmicos, de combustión, de propulsión y de química atmosférica mezclan escalas de microsegundos con horas. Un integrador explícito pagaría el paso del más rápido durante toda la simulación.

📘 **Dónde se aprende** (1 clase): [B11-C22 · Métodos implícitos y sistemas rígidos](../programa/clases/B11/B11-C22-metodos-implicitos-y-sistemas-rigidos/CLASE.md).

### Beer–Lambert

- Residuo: diferencia contra una referencia (la mediana). Beer–Lambert: absorción exponencial con la concentración.

💡 **Cómo se explica en la clase [B106-C25](../programa/clases/B106/B106-C25-sensores-de-presion-gases-y-humedad-para-monitoreo-de-habitat/CLASE.md):**
- Calcular la sensibilidad de un sensor de absorción (Beer–Lambert).
- Ejercicio 12 · integrador. Elabora tu *ficha de sensores con falsas alarmas*: calibración con su error, sensibilidad de Beer–Lambert, falsas alarmas de uno y de 2 de 3 con Monte Carlo, detección de deriva y qué es sintético.
- 🎯 **Por qué importa:** Un control sin medición fiable es ciego: un sensor con deriva puede ocultar una subida de CO₂ o disparar falsas alarmas. La decisión central: ¿cómo se calibra, se vota y se vigila la deriva para que la medición sea fiable durante la misión?

📘 **Dónde se aprende** (1 clase): [B106-C25 · Sensores de presión, gases y humedad para monitoreo de hábitat](../programa/clases/B106/B106-C25-sensores-de-presion-gases-y-humedad-para-monitoreo-de-habitat/CLASE.md).

### Benchmark

- Un benchmark es una comparación con protocolo.

💡 **Cómo se explica en la clase [B11-C26](../programa/clases/B11/B11-C26-benchmark-de-algoritmos-numericos/CLASE.md):**
- Es una prueba que el benchmark se pasa a sí mismo: si falla, hay una dependencia oculta (semilla, reloj, orden de ejecución).
- Resultado simulado con datos ilustrativos; el benchmark debe repetirse con el problema real.
- 🎯 **Por qué importa:** «El método A es mejor que el B» es una afirmación vacía sin el problema, la métrica, la tolerancia y el costo. Una comparación mal diseñada lleva a elegir el algoritmo equivocado para una misión.

📘 **Dónde se aprende** (1 clase): [B11-C26 · Benchmark de algoritmos numéricos](../programa/clases/B11/B11-C26-benchmark-de-algoritmos-numericos/CLASE.md).

### Beneficencia

- El informe Belmont nombra tres principios: respeto por las personas (autonomía y protección de quienes tienen autonomía disminuida), beneficencia (no dañar y maximizar beneficios) y justicia (reparto equitativo de cargas y beneficios).

💡 **Cómo se explica en la clase [B105-C19](../programa/clases/B105/B105-C19-bioetica-en-investigacion-tripulada/CLASE.md):**
- Un resumen de búsqueda web (2026-11-10) del informe Belmont indica tres principios: respeto por las personas (voluntariedad e información adecuada; protección de quienes tienen autonomía disminuida), beneficencia (no dañar y maximizar beneficios minimizando daños) y justicia (quién carga con los riesgos y quién recibe los beneficios).
- B["principios Belmont:<br/>respeto, beneficencia,<br/>justicia"] --> D["decisiones del estudio"]
- 🎯 **Por qué importa:** No basta con quitar el nombre: con edad, sexo, profesión y misión, una persona de una cohorte de 6 suele ser única. La decisión central: ¿qué se puede publicar de una cohorte pequeña sin identificar a nadie y cuánta utilidad se pierde al protegerla?

📘 **Dónde se aprende** (1 clase): [B105-C19 · Bioética en investigación tripulada](../programa/clases/B105/B105-C19-bioetica-en-investigacion-tripulada/CLASE.md).

### Beneficio

- El beneficio es lo que vuelve a la comunidad cuando se difunde algo suyo.
- El beneficio `w E[min(N, k)]` pondera por gravedad `w` las veces que el stock `k` cubre la demanda.

💡 **Cómo se explica en la clase [B117-C05](../programa/clases/B117/B117-C05-inventario-y-gestion-del-equipo-medico-a-bordo/CLASE.md):**
- Con 8 artículos, hasta 3 unidades (1 el equipo de reanimación) y pasos de 10 g y 10 cm³, la programación dinámica da un beneficio de `14,827484`, idéntico al de la búsqueda exhaustiva (32 768 combinaciones), con la misma selección.
- D["demanda N ~ Poisson(mu)"] --> B["beneficio w E[min(N,k)]"]
- 🎯 **Por qué importa:** Ninguna clase anterior trata el equipo médico de a bordo. La decisión central: ¿qué embarcar bajo un límite de masa y volumen y qué riesgo de quedarse sin él se acepta?

📘 **Dónde se aprende** (2 clases): [B117-C05 · Inventario y gestión del equipo médico a bordo](../programa/clases/B117/B117-C05-inventario-y-gestion-del-equipo-medico-a-bordo/CLASE.md); [B133-C04 · Riesgos de apropiación cultural en la divulgación](../programa/clases/B133/B133-C04-riesgos-de-apropiacion-cultural-en-la-divulgacion/CLASE.md).

### BER

- La BER de BPSK en AWGN es `Q(√(2Eb/N0)) = ½ erfc(√(Eb/N0))`.
- CRC: código de redundancia cíclica. BER: tasa de error de bit.

💡 **Cómo se explica en la clase [B47-C18](../programa/clases/B47/B47-C18-downlink-de-instrumentos-cientificos/CLASE.md):**
- *Descripción textual:* la potencia radiada, las ganancias y las pérdidas dan `C/N₀`; dividido por la velocidad da `Eb/N₀`, que fija la BER.
- Hallar la `Eb/N₀` requerida para BER 10⁻⁵.
- ⚠️ **Error frecuente:** Tomar la BER teórica como medida. Se corrige con 8.2.
- 🎯 **Por qué importa:** Los datos que no caben en un paso se pierden o se acumulan. La decisión central: ¿cuántos bits por paso admite el enlace con margen suficiente?

📘 **Dónde se aprende** (3 clases): [B47-C18 · Downlink de instrumentos científicos](../programa/clases/B47/B47-C18-downlink-de-instrumentos-cientificos/CLASE.md); [B89-C08 · Modulación digital](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md); [B90-C16 · Pruebas de extremo a extremo](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md).

### BER de BPSK

- La BER de BPSK es `Q(√(2Eb/N₀))`.

💡 **Cómo se explica en la clase [B89-C23](../programa/clases/B89/B89-C23-relacion-c-n0-eb-n0-y-tasa-de-error-de-bit/CLASE.md):**
- Para BER 10⁻³, 10⁻⁵ y 10⁻⁷, BPSK pide `6,790`, `9,588` y `11,309 dB`: pasar de 10⁻³ a 10⁻⁵ cuesta `2,8 dB` y de 10⁻⁵ a 10⁻⁷, `1,7 dB`.
- Límite: el modelo es BPSK ideal con ruido gaussiano; un sistema real tiene pérdidas de implementación y códigos que cambian el requisito.
- 🎯 **Por qué importa:** La tasa de datos es la variable que el ingeniero puede elegir: cada duplicación cuesta 3 dB de `Eb/N₀`. Esta cadena es la forma de decidir cuántos bits por segundo soporta un enlace.

📘 **Dónde se aprende** (1 clase): [B89-C23 · Relación C/N0, Eb/N0 y tasa de error de bit](../programa/clases/B89/B89-C23-relacion-c-n0-eb-n0-y-tasa-de-error-de-bit/CLASE.md).

### Beta

- Eclipse: paso por la sombra. Beta: ángulo Sol–plano orbital.

💡 **Cómo se explica en la clase [B96-C11](../programa/clases/B96/B96-C11-operacion-durante-eclipse/CLASE.md):**
- Con `a = R + h` y beta `β`: el eclipse existe si `|β| < β* = asen(R/a)`; entonces la fracción es `f = (1/π) arccos(√(h² + 2Rh)/(a cos β))`.
- G["Altura h y radio R"] --> B["Beta critico asen R/a"]
- ⚠️ **Error frecuente:** Suponer eclipse con cualquier beta. Compara con `β*` (8.2)
- 🎯 **Por qué importa:** La batería se descarga durante el eclipse y las operaciones que usan energía deben planificarse alrededor de él. La decisión central: ¿cuánto dura el eclipse en cada época del año y cuándo hay luz continua?

📘 **Dónde se aprende** (1 clase): [B96-C11 · Operación durante eclipse](../programa/clases/B96/B96-C11-operacion-durante-eclipse/CLASE.md).

### Beta crítico

- Beta: ángulo Sol–plano orbital. Beta crítico: `asen(R/a)`: sobre él no hay eclipse.

💡 **Cómo se explica en la clase [B96-C11](../programa/clases/B96/B96-C11-operacion-durante-eclipse/CLASE.md):**
- G["Altura h y radio R"] --> B["Beta critico asen R/a"]
- Con `h = 550 km` el periodo es 95,650 min y el ángulo beta crítico, 67,02°.
- 🎯 **Por qué importa:** La batería se descarga durante el eclipse y las operaciones que usan energía deben planificarse alrededor de él. La decisión central: ¿cuánto dura el eclipse en cada época del año y cuándo hay luz continua?

📘 **Dónde se aprende** (1 clase): [B96-C11 · Operación durante eclipse](../programa/clases/B96/B96-C11-operacion-durante-eclipse/CLASE.md).

### Beta del plasma

- El beta del plasma compara presiones.

🎯 **Por qué importa (clase B30-C05):** Que el gas domine al campo en la fotosfera y el campo al gas en la corona explica por qué la corona se estructura en lazos y por qué las erupciones liberan energía magnética. La decisión central: ¿en qué capa manda el campo y cuánta energía guarda?

📘 **Dónde se aprende** (1 clase): [B30-C05 · Campos magnéticos solares](../programa/clases/B30/B30-C05-campos-magneticos-solares/CLASE.md).

### Beta–Binomial

- Un prior es conjugado si la posterior pertenece a su misma familia: Beta–Binomial (prior `Beta(a,b)`, `s` éxitos en `n` ensayos → `Beta(a+s, b+n−s)`) y Poisson–Gamma (prior `Gamma(α,β)` con forma `α` y tasa `β`, conteos con suma `S` en `n` intervalos → `Gamma(α+S, β+n)`).

💡 **Cómo se explica en la clase [B12-C12](../programa/clases/B12/B12-C12-inferencia-bayesiana/CLASE.md):**
- Calcular la posterior en los modelos Beta–Binomial y Poisson–Gamma.
- El script [inferencia_bayes.py](inferencia_bayes.py) calcula posteriores Poisson–Gamma con dos priors, las compara con una rejilla de 100 001 puntos, calcula la Beta–Binomial y resuelve el problema de la alarma con fracciones exactas; falla si la rejilla se aparta más de `10⁻⁶` o si el resultado exacto de Bayes no coincide.
- 🎯 **Por qué importa:** Una misión rara vez parte de cero: hay pruebas en tierra, misiones anteriores y física conocida. Y a menudo el dato es escaso (diez intervalos, treinta pruebas).

📘 **Dónde se aprende** (1 clase): [B12-C12 · Inferencia bayesiana](../programa/clases/B12/B12-C12-inferencia-bayesiana/CLASE.md).

### Bhattacharyya

- La distancia de Bhattacharyya para gaussianas de igual covarianza diagonal es `B = d²/8`.

💡 **Cómo se explica en la clase [B57-C25](../programa/clases/B57/B57-C25-seleccion-de-bandas-espectrales-segun-el-fenomeno/CLASE.md):**
- Paso 2 · Bhattacharyya. `B = 484/8 = 60,5`.
- Calcular la distancia de Bhattacharyya y la de Jeffries–Matusita entre clases gaussianas.
- 🎯 **Por qué importa:** Cada banda cuesta datos, masa y complejidad. La decisión central: ¿con qué menor número de bandas se separan las clases que me interesan y cuál es el par más difícil de distinguir?

📘 **Dónde se aprende** (1 clase): [B57-C25 · Selección de bandas espectrales según el fenómeno](../programa/clases/B57/B57-C25-seleccion-de-bandas-espectrales-segun-el-fenomeno/CLASE.md).

### Bias

- El bias es el desplazamiento electrónico presente en toda lectura (S1).
- El bias es el nivel que lee el sensor con exposición cero.

💡 **Cómo se explica en la clase [B15-C09](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md):**
- Pero cada recipiente ya traía agua de fábrica (bias), recoge goteras (oscuro) y tiene una boca de distinto tamaño (plano).
- R["Imagen cruda"] --> A["− oscuro maestro<br/>(incluye bias)"]
- 🎯 **Por qué importa:** Una cámara de un telescopio no mide «luz de estrellas»: mide un número por píxel que incluye un desplazamiento electrónico, corriente de oscuridad, el cielo, la estrella y una sensibilidad que cambia de un píxel a otro. Si analizas el número crudo, mides la cámara, no el cielo.

📘 **Dónde se aprende** (2 clases): [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md); [B44-C06 · Ruido de lectura](../programa/clases/B44/B44-C06-ruido-de-lectura/CLASE.md).

### Biblioteca

- Espectro de masas: huella de un compuesto. Biblioteca: conjunto de espectros de referencia.

💡 **Cómo se explica en la clase [B106-C22](../programa/clases/B106/B106-C22-fuentes-e-identificacion-de-contaminantes-del-aire-de-cabina/CLASE.md):**
- S["espectro medido"] --> N["NNLS con biblioteca"]
- *Descripción textual:* las fuentes suman una emisión; con depuración dan una concentración; el espectro medido se descompone con una biblioteca para identificar los compuestos.
- 🎯 **Por qué importa:** Nada sale al exterior de una cabina cerrada: los materiales emiten gases durante meses, los equipos liberan trazas y las personas emiten vapor y CO₂. La decisión central: ¿qué fuentes dominan en cada momento y cómo se identifican los compuestos para decidir qué retirar?

📘 **Dónde se aprende** (1 clase): [B106-C22 · Fuentes e identificación de contaminantes del aire de cabina](../programa/clases/B106/B106-C22-fuentes-e-identificacion-de-contaminantes-del-aire-de-cabina/CLASE.md).

### Bielíptica

- La bielíptica usa dos elipses con un apoápside intermedio `r_b`.

💡 **Cómo se explica en la clase [B71-C18](../programa/clases/B71/B71-C18-maniobra-de-hohmann/CLASE.md):**
- En unidades de `r₁ = 1`, `μ = 1`: razón 20, Hohmann `0.53473` frente a bielíptica mínima `0.50747`; razón 50, `0.51370` frente a `0.47350`; para la razón de Marte, Hohmann `0.18783` frente a `0.25635`: aquí la bielíptica pierde.
- El umbral donde la bielíptica con `r_b → ∞` iguala a Hohmann es `11.939`.
- ⚠️ **Error frecuente:** Creer que Hohmann siempre gana a la bielíptica. Se corrige con 8.4.
- 🎯 **Por qué importa:** La Hohmann es la referencia de costo para cualquier cambio de órbita coplanar. La decisión central: ¿cuánto `Δv` y cuánto tiempo cuesta pasar de una circular a otra y cuándo conviene otra estrategia?

📘 **Dónde se aprende** (1 clase): [B71-C18 · Maniobra de Hohmann](../programa/clases/B71/B71-C18-maniobra-de-hohmann/CLASE.md).

### Bien planteada

- Una EDO de primer orden `y′ = f(t, y)` se llama bien planteada si la solución existe, es única y depende de forma continua de los datos.

🎯 **Por qué importa (clase B11-C02):** Una nave no sigue «la» solución de las ecuaciones del movimiento: sigue la que corresponde a *su* posición y velocidad en el instante en que se midieron. Saber cuántos datos exige la ecuación, cuándo garantizan una única trayectoria y cuánto se amplifica su error es la base de toda predicción de trayectoria.

📘 **Dónde se aprende** (1 clase): [B11-C02 · Problemas de valor inicial](../programa/clases/B11/B11-C02-problemas-de-valor-inicial/CLASE.md).

### Bien planteado

- Un problema está bien planteado (*well-posed*, en el sentido de Hadamard) si tiene solución, es única y depende de forma continua de los datos (S1).

💡 **Cómo se explica en la clase [B22-C01](../programa/clases/B22/B22-C01-problemas-directos-e-inversos-y-mal-condicionamiento/CLASE.md):**
- Fíjate en el orden de la cadena: el problema es «bien planteado» según Hadamard (existe, es única y es continua) y, sin embargo, mal condicionado, que es lo que realmente impide usarlo.
- 🎯 **Por qué importa:** Un telescopio nunca entrega la imagen verdadera del cielo: la entrega emborronada por su respuesta óptica y con ruido. Calcular lo que verá el telescopio si conoces el objeto es fácil; el camino contrario, recuperar el objeto desde lo que vio, es el que interesa a la ciencia y el que se complica.

📘 **Dónde se aprende** (1 clase): [B22-C01 · Problemas directos e inversos y mal condicionamiento](../programa/clases/B22/B22-C01-problemas-directos-e-inversos-y-mal-condicionamiento/CLASE.md).

### Bilateral

- Una prueba bilateral rechaza para desviaciones en ambos sentidos; una unilateral, en uno solo.

💡 **Cómo se explica en la clase [B12-C09](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md):**
- El valor `p` bilateral es `2 P(Z > 4,888) = 1,02 × 10⁻⁶`.
- Con un efecto real `δ = 1 m`, `σ = 3 m` y `n = 25`, el estadístico se desplaza `δ√n/σ = 1,667` errores típicos y la potencia de la prueba bilateral al 5 % es `0,385` (simulada `0,387`): la prueba pasa por alto el efecto el 61 % de las veces.
- 🎯 **Por qué importa:** Muchas preguntas científicas tienen forma de decisión: ¿coinciden dos mediciones de la misma constante?, ¿el sensor sigue calibrado?, ¿es real la señal o es ruido? Sin un procedimiento con error controlado, cada persona decide por intuición.

📘 **Dónde se aprende** (1 clase): [B12-C09 · Pruebas de hipótesis](../programa/clases/B12/B12-C09-pruebas-de-hipotesis/CLASE.md).

### Bimodal

- Una curva bimodal tiene dos máximos y dos mínimos por vuelta (cuerpo alargado).

💡 **Cómo se explica en la clase [B58-C13](../programa/clases/B58/B58-C13-caracterizacion-de-rotacion/CLASE.md):**
- Paso 2 · Hipótesis. Curva bimodal: el verdadero periodo es el doble.
- Si la curva es bimodal y si el doble ajusta mejor.
- 🎯 **Por qué importa:** La rotación fija el tamaño máximo de un cuerpo sin cohesión y la acción de los efectos térmicos (C14); además, un cuerpo que rota muy rápido o muy lento ya dice algo de su estructura. La decisión central: ¿cuál es el periodo, el del pico del periodograma o el doble?

📘 **Dónde se aprende** (1 clase): [B58-C13 · Caracterización de rotación](../programa/clases/B58/B58-C13-caracterizacion-de-rotacion/CLASE.md).

### Bin

- Un bin es cada valor de `k`.

💡 **Cómo se explica en la clase [B15-C04](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md):**
- El bin `k` corresponde a la frecuencia `f_k = k/(N Δt) = k f_s/N`.
- Con `N = 64` y `Δt = 120 s`: `Δf = 720/64 = 11,25 c/d`; el bin 5 es `56,25 c/d`.
- ⚠️ **Error frecuente:** Leer un bin como frecuencia sin convertir. Se corrige con el ejercicio 2.
- 🎯 **Por qué importa:** Si una estrella pulsa con una pequeña amplitud en medio del ruido, mirar la curva de luz no la revela, pero su espectro de frecuencias sí: un pico a una frecuencia concreta. Lo mismo ocurre con una vibración en una estructura espacial, una señal de radio o un periodo en un registro geofísico.

📘 **Dónde se aprende** (1 clase): [B15-C04 · Transformada de Fourier](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md).

### Binaria de fondo

- La binaria de fondo y la jerárquica imitan un tránsito.

💡 **Cómo se explica en la clase [B29-C07](../programa/clases/B29/B29-C07-metodos-de-validacion-planetaria/CLASE.md):**
- Esta clase no reproduce ese método: usa tres escenarios sintéticos (planeta `0,30`, binaria de fondo `0,40`, binaria jerárquica `0,30`) y un observable `x` normal en cada uno.
- Ejercicio 2 · con una pista. Prior de la binaria de fondo.
- 🎯 **Por qué importa:** Hay muchos más candidatos que posibilidades de seguimiento. Validar bien exige probabilidades honestas: ni optimistas ni conservadoras en exceso.

📘 **Dónde se aprende** (1 clase): [B29-C07 · Métodos de validación planetaria](../programa/clases/B29/B29-C07-metodos-de-validacion-planetaria/CLASE.md).

### Binaria eclipsante

- Una binaria eclipsante con velocidades radiales da las masas con `M sin³ i = P(K₁ + K₂)² K₂/(2πG)`.

🎯 **Por qué importa (clase B37-C06):** Dos observables fijan dos parámetros, pero con degeneración. La decisión central: ¿qué parámetros se ajustan, con qué incertidumbre y qué correlación entre ellos?

📘 **Dónde se aprende** (1 clase): [B37-C06 · Calibración de modelos estelares con el Sol y binarias](../programa/clases/B37/B37-C06-calibracion-de-modelos-estelares-con-el-sol-y-binarias/CLASE.md).

### Bingham

- Un fluido de Bingham necesita un esfuerzo mínimo `τ_y`; el espesor máximo estable es `h = τ_y/(ρ g sin α)`.

💡 **Cómo se explica en la clase [B53-C11](../programa/clases/B53/B53-C11-vulcanismo-extraterrestre/CLASE.md):**
- Distinguir fluido newtoniano y de Bingham.
- tierra g = 9.81: u = 1.23251 m/s ; razon 1.0000 ; h maximo (Bingham) = 10.818 m
- 🎯 **Por qué importa:** La forma de un edificio volcánico delata la reología de la lava y la gravedad del cuerpo. La decisión central: ¿cómo cambian la velocidad, el espesor y el largo de una colada al cambiar de planeta?

📘 **Dónde se aprende** (1 clase): [B53-C11 · Vulcanismo extraterrestre](../programa/clases/B53/B53-C11-vulcanismo-extraterrestre/CLASE.md).

### Binning

- El binning suma píxeles vecinos.

💡 **Cómo se explica en la clase [B44-C18](../programa/clases/B44/B44-C18-control-electronico-de-camaras/CLASE.md):**
- Binning `2 × 2` en el chip: ruido `4,002 e⁻` (una lectura); por programa: `7,966 e⁻` (cuatro lecturas, esperado `8`).
- El binning reduce el tiempo de lectura y, en el chip, el ruido relativo; por programa se paga `2 RN`.
- 🎯 **Por qué importa:** Leer lento reduce ruido pero desperdicia tiempo de observación. La decisión central: ¿qué modo de lectura equilibra ruido y tiempo muerto?

📘 **Dónde se aprende** (1 clase): [B44-C18 · Control electrónico de cámaras](../programa/clases/B44/B44-C18-control-electronico-de-camaras/CLASE.md).

### Binomial

- Campaña: conjunto de observaciones con un objetivo. Binomial: número de éxitos en n ensayos.

💡 **Cómo se explica en la clase [B48-C20](../programa/clases/B48/B48-C20-diseno-de-una-campana-observacional-profesional/CLASE.md):**
- P["p despejada"] --> B["Binomial: P(X >= k)"]
- *Descripción textual:* la binomial da la probabilidad con noches independientes y la cadena de Markov la rebaja al incluir la persistencia, con la misma fracción media de noches despejadas.
- 🎯 **Por qué importa:** Planificar con el clima medio sin considerar su persistencia da una confianza falsa. La decisión central: ¿qué ventana asegura completar la campaña con 95 % de probabilidad?

📘 **Dónde se aprende** (1 clase): [B48-C20 · Diseño de una campaña observacional profesional](../programa/clases/B48/B48-C20-diseno-de-una-campana-observacional-profesional/CLASE.md).

### BINTABLE

- FITS: bloques de 2880 bytes con tarjetas de 80 caracteres. BINTABLE: tabla binaria.

🎯 **Por qué importa (clase B40-C14):** Usar un producto sin leer su cabecera es una fuente clásica de errores de unidades y de orden de pixeles. La decisión central: ¿qué dice la cabecera y cómo se convierte y se compara con un modelo?

📘 **Dónde se aprende** (1 clase): [B40-C14 · Productos de datos de Planck y misiones del CMB](../programa/clases/B40/B40-C14-productos-de-datos-de-planck-y-misiones-del-cmb/CLASE.md).

### Biocarga

- Biocarga: número de microorganismos viables sobre un objeto.

💡 **Cómo se explica en la clase [B90-C21](../programa/clases/B90/B90-C21-biocarga-de-naves-espaciales-verificacion-y-requisitos-normativos/CLASE.md):**
- Paso 4 · Decisión. Con 95 % de confianza no se puede declarar el cumplimiento: se muestrea más o se reduce la biocarga (C22).
- La evidencia es la verificación de biocarga frente a un límite de ejemplo del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Un hisopo recoge solo una fracción de las esporas de una superficie y se cuentan pocas colonias; el resultado es una estimación con incertidumbre. La decisión central: ¿la biocarga cumple el límite con la confianza exigida o hace falta muestrear más o reducir?

📘 **Dónde se aprende** (1 clase): [B90-C21 · Biocarga de naves espaciales: verificación y requisitos normativos](../programa/clases/B90/B90-C21-biocarga-de-naves-espaciales-verificacion-y-requisitos-normativos/CLASE.md).

### Biofirma

- Una biofirma es una señal que sugiere vida pasada o presente.

💡 **Cómo se explica en la clase [B56-C13](../programa/clases/B56/B56-C13-biofirmas-quimicas/CLASE.md):**
- (2018) revisa las biofirmas remotamente detectables, incluidas las gaseosas y los métodos para detectar desequilibrio químico a distancia (S1, solo resumen, consultado el 2026-11-09).
- Definir biofirma, desequilibrio químico y energía libre disponible.
- 🎯 **Por qué importa:** Una biosfera mantiene en la atmósfera gases que reaccionarían entre sí (como oxígeno y metano) y por eso la composición se aleja del equilibrio. La decisión central: dadas las presiones parciales, ¿cuánta energía libre por mol de CH₄ hay en el desequilibrio CH₄–O₂?

📘 **Dónde se aprende** (1 clase): [B56-C13 · Biofirmas químicas](../programa/clases/B56/B56-C13-biofirmas-quimicas/CLASE.md).

### Biomasa seca

- Fracción comestible: parte aprovechada. Biomasa seca: masa sin agua.

💡 **Cómo se explica en la clase [B106-C12](../programa/clases/B106/B106-C12-agricultura-en-ambiente-controlado/CLASE.md):**
- Por m² y día, el cultivo ilustrativo da 25,9 g de biomasa seca, 44 kcal comestibles, 27,6 g de O₂ y fija 38,0 g de CO₂.
- Por m2 y dia: biomasa seca 25.9 g; comestible 11.7 g = 44 kcal;
- 🎯 **Por qué importa:** Cultivar reduce la masa de alimento a lanzar y devuelve oxígeno, pero cuesta mucha área y electricidad. La decisión central: ¿qué fracción de la dieta compensa cultivar dado el costo en área y energía?

📘 **Dónde se aprende** (1 clase): [B106-C12 · Agricultura en ambiente controlado](../programa/clases/B106/B106-C12-agricultura-en-ambiente-controlado/CLASE.md).

### Biopelícula

- Umbral de acción: nivel que exige respuesta. Biopelícula: capa de microorganismos adherida a una superficie.

💡 **Cómo se explica en la clase [B106-C28](../programa/clases/B106/B106-C28-monitoreo-microbiologico-de-agua-y-superficies-del-habitat/CLASE.md):**
- Límite: aquí los organismos están distribuidos al azar; en la realidad se agrupan en biopelículas.
- Ejercicio 10 · transferencia. La contaminación está en una biopelícula de la tubería.
- 🎯 **Por qué importa:** Una muestra pequeña puede no contener ningún organismo de una contaminación real, y un muestreo espaciado deja crecer la población. La decisión central: ¿qué volumen y qué intervalo de muestreo dan una confianza dada de detectar una contaminación antes de que supere el umbral de acción?

📘 **Dónde se aprende** (1 clase): [B106-C28 · Monitoreo microbiológico de agua y superficies del hábitat](../programa/clases/B106/B106-C28-monitoreo-microbiologico-de-agua-y-superficies-del-habitat/CLASE.md).

### Biorreactor

- Aguas grises: agua de higiene sin orina. Biorreactor: tanque con microorganismos que consumen materia orgánica.

💡 **Cómo se explica en la clase [B106-C26](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md):**
- G["aguas grises F, S0"] --> B["biorreactor tau"]
- *Descripción textual:* las aguas grises pasan por un biorreactor que baja la carga orgánica, por filtros y por una desinfección antes de entrar al lazo de agua.
- 🎯 **Por qué importa:** Las aguas grises son el mayor volumen del lazo y su carga orgánica hay que destruirla antes de potabilizar. La decisión central: ¿qué volumen de biorreactor y qué desinfección dan la remoción y la reducción de microorganismos requeridas?

📘 **Dónde se aprende** (1 clase): [B106-C26 · Tratamiento de aguas grises en hábitats](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md).

### Bioseguridad

- La bioseguridad son las barreras que evitan que un agente entre, se propague o salga.

💡 **Cómo se explica en la clase [B115-C07](../programa/clases/B115/B115-C07-bioseguridad-e-inocuidad-alimentaria-en-habitats/CLASE.md):**
- python programa/clases/B115/B115-C07-bioseguridad-e-inocuidad-alimentaria-en-habitats/inocuidad.py
- 🎯 **Por qué importa:** Una contaminación en un circuito compartido afecta a todos los lotes a la vez. La decisión central: ¿con qué frecuencia se muestrea, qué se mide y qué barreras (desinfección, lavado, temperatura) hacen falta para que una contaminación se detecte antes de llegar a un nivel de acción?

📘 **Dónde se aprende** (1 clase): [B115-C07 · Bioseguridad e inocuidad alimentaria en hábitats](../programa/clases/B115/B115-C07-bioseguridad-e-inocuidad-alimentaria-en-habitats/CLASE.md).

### Bipropelente

- El bipropelente usa combustible y oxidante en tanques separados.

💡 **Cómo se explica en la clase [B78-C05](../programa/clases/B78/B78-C05-propulsion-bipropelente-conceptual/CLASE.md):**
- El script [bipropelente.py](bipropelente.py) calcula productos, temperatura, masa molar y escape para `O/F` de 0,5 a 9, y halla el máximo (comprueba la conservación de la masa, `O/F_st` y la coincidencia del máximo entre sección áurea y malla fina).
- Bipropelente ILUSTRATIVO H2/O2 (valores de manual no consultados; solo tendencia)
- 🎯 **Por qué importa:** Un motor puede quemar mezclas con exceso de combustible o de oxidante. La decisión central: ¿qué `O/F` maximiza el escape en un modelo sin disociación y por qué los motores reales operan en otro punto?

📘 **Dónde se aprende** (1 clase): [B78-C05 · Propulsión bipropelente conceptual](../programa/clases/B78/B78-C05-propulsion-bipropelente-conceptual/CLASE.md).

### Birnbaum

- La aproximación de evento raro suma las probabilidades de los cortes; la cota de cortes mínimos es `1 − Π(1 − P(cᵢ))`. Birnbaum mide `P(top | i falla) − P(top | i no falla)`.

💡 **Cómo se explica en la clase [B83-C24](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md):**
- Birnbaum separa la influencia estructural de la probabilidad: B7 y B5 tienen `B ≈ 0,99` (si fallan, el evento ocurre casi seguro).
- Calcular la importancia de Birnbaum y de Fussell–Vesely y priorizar.
- 🎯 **Por qué importa:** Un fallo combinado como «dos sensores fallan a la vez» no aparece en una lista de modos individuales. La decisión central: ¿qué combinaciones de fallos causan el evento no deseado, cuál es su probabilidad y qué evento básico conviene proteger primero?

📘 **Dónde se aprende** (1 clase): [B83-C24 · Árboles de fallos (FTA) y análisis de causas](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md).

### Bisección

- La bisección es el algoritmo que lo usa: reduce a la mitad el intervalo que contiene la raíz.
- Descentrado: distancia del pivote al centro. Bisección: búsqueda de una raíz por mitades.
- La bisección reduce a la mitad un intervalo que contiene la raíz.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B09-C02](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md):**
- La bisección encuentra lo mismo sin despejar: parte de un intervalo donde `a − 24,517` cambia de signo, lo parte por la mitad y se queda con la mitad que sigue cambiando de signo.
- Paso 4 · Bisección. El laboratorio parte de `[0, 100)` y converge a `t = 77,634054443 s`, igual al exacto en nueve cifras decimales.
- ⚠️ **Error frecuente:** Usar bisección sin verificar la continuidad. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Un vehículo espacial cambia de masa de dos maneras: gradualmente, al quemar propelente, y de golpe, al soltar una etapa vacía. Un modelo de trayectoria que ignore los saltos integra mal; uno que los trate como suaves, también.

📘 **Dónde se aprende** (5 clases): [B09-C02 · Continuidad y discontinuidad](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md); [B48-C08 · Automatización de cúpulas](../programa/clases/B48/B48-C08-automatizacion-de-cupulas/CLASE.md); [B55-C15 · Química de océanos internos](../programa/clases/B55/B55-C15-quimica-de-oceanos-internos/CLASE.md); [B71-C14 · Ecuación de Kepler](../programa/clases/B71/B71-C14-ecuacion-de-kepler/CLASE.md); [B83-C20 · Diseño preliminar completo de misión](../programa/clases/B83/B83-C20-diseno-preliminar-completo-de-mision/CLASE.md).

### Bit a bit

- Normalizar es llevar los archivos a un formato único (fin de línea LF) antes de hashearlos. Bit a bit significa que la cifra coincide exactamente;

💡 **Cómo se explica en la clase [B23-C07](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md):**
- Tampoco sustituye el control de versiones de datos ni del código (el hash del script identifica el contenido, no su historia), ni garantiza que un hardware distinto dé el mismo resultado bit a bit.
- Verificar: reejecutar y obtener «bit a bit».
- 🎯 **Por qué importa:** Un informe dice «el modelo reproduce la posición con un error de 8,21 × 10⁻⁴ au». Seis meses después, nadie sabe con qué versión del código, qué archivo de datos ni qué tolerancia se calculó, y el número no se puede reproducir ni defender.

📘 **Dónde se aprende** (1 clase): [B23-C07 · Trazabilidad científica de resultados](../programa/clases/B23/B23-C07-trazabilidad-cientifica-de-resultados/CLASE.md).

### Bitácora

- La bitácora es el registro cronológico de lo que hiciste y viste, con fecha, hora, escala de tiempo, lugar y condiciones.
- Una bitácora (o cuaderno de campo) es un registro cronológico de observaciones.
- Una bitácora es el registro cronológico de entradas.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C20](../programa/clases/B01/B01-C20-proyecto-de-observacion-cientifica-inicial/CLASE.md):**
- La bitácora es un documento cronológico: no se reescribe; si te equivocas, tachas y anotas la corrección.
- De la bitácora salen los datos observados; lo que calcules a partir de ellos es estimado.
- 🎯 **Por qué importa:** Entender el método no es lo mismo que aplicarlo. Cuando mides de verdad, aparecen problemas que los ejercicios no tienen: el cielo se nubla, el palo no está del todo vertical, la regla se mueve, los datos no coinciden con lo que predijiste.

📘 **Dónde se aprende** (4 clases): [B01-C20 · Proyecto de observación científica inicial](../programa/clases/B01/B01-C20-proyecto-de-observacion-cientifica-inicial/CLASE.md); [B08-C17 · Registro sistemático en bitácora](../programa/clases/B08/B08-C17-registro-sistematico-en-bitacora/CLASE.md); [B14-C24 · Documentación de hipótesis y decisiones de análisis](../programa/clases/B14/B14-C24-documentacion-de-hipotesis-y-decisiones-de-analisis/CLASE.md); [B96-C30 · Registro y auditoría de operaciones](../programa/clases/B96/B96-C30-registro-y-auditoria-de-operaciones/CLASE.md).

### Biyección

- La biyección entre términos exige que cada término apunte a una sola entrada.

💡 **Cómo se explica en la clase [B128-C09](../programa/clases/B128/B128-C09-apoyo-multilingue-y-glosarios/CLASE.md):**
- G["glosario: id, es, en, pt, definicion"] --> B["biyeccion por idioma"]
- 🎯 **Por qué importa:** Si el mismo concepto aparece como «agujero negro» y «hoyo negro», un estudiante puede creer que son dos cosas, y más si traduce con una herramienta automática. La decisión central: ¿cómo mantengo un vocabulario coherente entre idiomas y dentro de un mismo texto?

📘 **Dónde se aprende** (1 clase): [B128-C09 · Apoyo multilingüe y glosarios](../programa/clases/B128/B128-C09-apoyo-multilingue-y-glosarios/CLASE.md).

### Blanco

- Un blanco (*blank*) es una referencia que mide contaminación.
- El blanco tiene ventana `[s, e]`, duración `d` y peso `w`.

💡 **Cómo se explica en la clase [B29-C18](../programa/clases/B29/B29-C18-redes-de-seguimiento-temporal/CLASE.md):**
- Ocho blancos (inicio, fin, duración, peso) con un telescopio: valor voraz `19,22` (blancos 1 y 3), óptimo `26,44` (blancos 1, 2, 4 y 3), razón `0,727`.
- En 150 instancias de 8 blancos con un telescopio:
- ⚠️ **Error frecuente:** Tomar los blancos por reales. Se corrige con la sección 10.
- 🎯 **Por qué importa:** La regla de planificación determina cuánto valor científico se recoge. Una regla ingenua puede perder la mitad del valor; añadir telescopios no siempre compensa.

📘 **Dónde se aprende** (2 clases): [B29-C18 · Redes de seguimiento temporal](../programa/clases/B29/B29-C18-redes-de-seguimiento-temporal/CLASE.md); [B63-C03 · Curaduría y cadena de custodia de muestras](../programa/clases/B63/B63-C03-curaduria-y-cadena-de-custodia-de-muestras/CLASE.md).

### Blanco de procedimiento

- La contaminación es el material terrestre que altera la muestra; un blanco de procedimiento es una muestra de control que sigue el mismo tratamiento sin la muestra para detectarla.

💡 **Cómo se explica en la clase [B06-C20](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md):**
- (2) Controlar la contaminación y usar blancos de procedimiento: los autores de S2 subrayan que la devolución en condiciones controladas permitió estudiar material sin exposición incontrolada a la biosfera terrestre.
- 🎯 **Por qué importa:** Hay dos formas de saber de qué está hecho el Sistema Solar. Una es mirar la luz del Sol y deducir su composición; la otra es analizar en laboratorio meteoritos que conservan la composición del material con que se formó.

📘 **Dónde se aprende** (1 clase): [B06-C20 · Análisis químico introductorio de meteoritos](../programa/clases/B06/B06-C20-analisis-quimico-introductorio-de-meteoritos/CLASE.md).

### Blanco de referencia

- Un blanco de referencia es un objeto cuya distancia se conoce por un método independiente, con su incertidumbre.

💡 **Cómo se explica en la clase [B13-C20](../programa/clases/B13/B13-C20-validacion-de-una-cadena-de-medida/CLASE.md):**
- Contra blancos de referencia independientes (esta clase): directa; exige referencias.
- Luego se valida con tres blancos de referencia independientes a `500`, `2000` y `8000 m` (`u_ref = 0,003; 0,005; 0,010 m`), con 100 lecturas cada uno.
- 🎯 **Por qué importa:** Un telémetro calibrado, con presupuesto y registro, puede seguir fallando: un error de escala oculto que la calibración en una sola distancia no ve.

📘 **Dónde se aprende** (1 clase): [B13-C20 · Validación de una cadena de medida](../programa/clases/B13/B13-C20-validacion-de-una-cadena-de-medida/CLASE.md).

### Blanco fijo

- El blanco fijo y el colisionador.
- El blanco fijo usa un haz sobre materia en reposo.

💡 **Cómo se explica en la clase [B31-C12](../programa/clases/B31/B31-C12-antimateria-y-aniquilacion/CLASE.md):**
- En un colisionador `e⁺e⁻ → μ⁺μ⁻`, cada haz necesita `m_μc² = 105,66 MeV`, 413 veces menos que los 43,69 GeV en blanco fijo.
- Los umbrales de blanco fijo crecen con la masa final al cuadrado; el colisionador evita ese desperdicio.
- 🎯 **Por qué importa:** Producir antimateria o partículas pesadas requiere una energía mínima que depende de la configuración. La decisión central: ¿cuál es la energía umbral de una reacción y por qué un colisionador ahorra energía?

📘 **Dónde se aprende** (2 clases): [B31-C12 · Antimateria y aniquilación](../programa/clases/B31/B31-C12-antimateria-y-aniquilacion/CLASE.md); [B31-C15 · Física de aceleradores](../programa/clases/B31/B31-C15-fisica-de-aceleradores/CLASE.md).

### Bland–Altman

- Los límites de acuerdo de Bland–Altman son `d̄ ± 1,96 SD_d`.
- El compuesto es la media geométrica de los porcentajes. Bland–Altman compara dos medidas con el sesgo y los límites de acuerdo.
- La resolución espectral es la separación mínima entre dos frecuencias distinguibles, `1/T` Hz o `60/T` lpm. Bland–Altman: gráfico y resumen de las diferencias entre dos métodos, con sesgo y límites de acuerdo `sesgo ± 1,96·DE`.

💡 **Cómo se explica en la clase [B105-C26](../programa/clases/B105/B105-C26-medidas-fisiologicas-y-biomarcadores-en-investigacion-espacial/CLASE.md):**
- Descripción: la tabla de 8.2 y la salida con Bland–Altman y el promedio de sesiones.
- Calcular los límites de acuerdo de Bland–Altman y detectar un sesgo sistemático.
- ⚠️ **Error frecuente:** Ignorar el sesgo sistemático. Usa Bland–Altman (8.3).
- 🎯 **Por qué importa:** Un biomarcador con alta variación interna no detecta cambios pequeños aunque sea «preciso». Con pocos participantes, además, el propio ICC es incierto.

📘 **Dónde se aprende** (3 clases): [B105-C26 · Medidas fisiológicas y biomarcadores en investigación espacial](../programa/clases/B105/B105-C26-medidas-fisiologicas-y-biomarcadores-en-investigacion-espacial/CLASE.md); [B107-C08 · Evaluación funcional posterior al vuelo](../programa/clases/B107/B107-C08-evaluacion-funcional-posterior-al-vuelo/CLASE.md); [B116-C01 · Sensores fisiológicos y wearables para vuelo](../programa/clases/B116/B116-C01-sensores-fisiologicos-y-wearables-para-vuelo/CLASE.md).

### Blando

- El plazo duro no admite incumplimiento; el blando lo tolera con degradación.

💡 **Cómo se explica en la clase [B88-C05](../programa/clases/B88/B88-C05-sistemas-de-tiempo-real/CLASE.md):**
- Ejercicio 11 · transferencia. Transferencia. ¿Qué haces con un plazo blando incumplido a veces?
- 🎯 **Por qué importa:** En una nave, una tarea de control que llega tarde puede ser tan mala como una que da un resultado incorrecto. La decisión central: ¿cada tarea termina siempre antes de su plazo, aun cuando las de mayor prioridad la interrumpen?

📘 **Dónde se aprende** (1 clase): [B88-C05 · Sistemas de tiempo real](../programa/clases/B88/B88-C05-sistemas-de-tiempo-real/CLASE.md).

### Blanqueo

- El blanqueo divide por `√S`.

💡 **Cómo se explica en la clase [B28-C14](../programa/clases/B28/B28-C14-ruidos-instrumentales/CLASE.md):**
- La evidencia es la ficha de ruido y blanqueo del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *ficha de ruido y blanqueo*: la FFT verificada, tabla del periodograma, `ρ` y resultados del filtro.
- 🎯 **Por qué importa:** Entender la forma del ruido explica por qué un detector es sensible solo en una banda y por qué una señal débil puede perderse en baja frecuencia aunque sea fuerte en alta. La decisión central: ¿cómo se estima la densidad espectral del ruido y qué relación señal-ruido da el filtro óptimo?

📘 **Dónde se aprende** (1 clase): [B28-C14 · Ruidos instrumentales](../programa/clases/B28/B28-C14-ruidos-instrumentales/CLASE.md).

### Blaze

- El blaze es el pico de eficiencia de la red.
- El blaze concentra la energía en un orden.

💡 **Cómo se explica en la clase [B45-C04](../programa/clases/B45/B45-C04-redes-de-difraccion/CLASE.md):**
- Reconocer que no se modela la eficiencia de blaze.
- Ejercicio 11 · transferencia. Transferencia. Un compañero dice que la red ideal da la eficiencia de blaze.
- 🎯 **Por qué importa:** La red es el elemento dispersor de casi todos los espectrógrafos. La decisión central: ¿en qué ángulo sale cada longitud de onda y qué resolución se obtiene?

📘 **Dónde se aprende** (2 clases): [B45-C04 · Redes de difracción](../programa/clases/B45/B45-C04-redes-de-difraccion/CLASE.md); [B45-C09 · Calibración de respuesta instrumental](../programa/clases/B45/B45-C09-calibracion-de-respuesta-instrumental/CLASE.md).

### Blindaje

- El blindaje es la cubierta que atenúa la radiación.
- El blindaje atenúa por `e^{−t/λ}` con `t` en g/cm².

💡 **Cómo se explica en la clase [B47-C14](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md):**
- Un blindaje fino no reduce la dosis de un protón de 30 MeV: la aumenta, porque el protón frenado deposita más por unidad de masa.
- Los eventos aislados no se evitan con blindaje: se mitigan con corrección de errores.
- ⚠️ **Error frecuente:** Creer que más blindaje siempre reduce la dosis. Se corrige con 8.3.
- 🎯 **Por qué importa:** El blindaje reduce la dosis hasta que el protón se detiene; los eventos de partícula simple, en cambio, son aleatorios. La decisión central: ¿qué espesor de blindaje y qué probabilidad de eventos son aceptables?

📘 **Dónde se aprende** (3 clases): [B47-C14 · Radiación y degradación](../programa/clases/B47/B47-C14-radiacion-y-degradacion/CLASE.md); [B75-C28 · Restricciones de radiación en trayectorias](../programa/clases/B75/B75-C28-restricciones-de-radiacion-en-trayectorias/CLASE.md); [B97-C14 · Construcción con regolito — Robótica y construcción extraterrestre](../programa/clases/B97/B97-C14-construccion-con-regolito-robotica-y-construccion-extraterrestre/CLASE.md).

### Bloque

- Un bloque es un múltiplo de `2880` bytes.
- Un bloque es un tramo del plan con un tiempo y un tipo (diagnóstico, exposición, actividad, evaluación o cierre).
- El bloque de 2880 bytes.

💡 **Cómo se explica en la clase [B44-C19](../programa/clases/B44/B44-C19-formato-fits-y-metadatos/CLASE.md):**
- Paso 3 · Bloque. `⌈2400/2880⌉ × 2880 = 2880`.
- Ejercicio 5. Tarjetas por bloque de cabecera (80 caracteres).
- 🎯 **Por qué importa:** Un cuadro sin metadatos es un arreglo de números sin contexto. La decisión central: ¿qué debe llevar la cabecera para interpretar los datos?

📘 **Dónde se aprende** (3 clases): [B44-C19 · Formato FITS y metadatos](../programa/clases/B44/B44-C19-formato-fits-y-metadatos/CLASE.md); [B51-C12 · Formatos de datos VLBI y geodésicos](../programa/clases/B51/B51-C12-formatos-de-datos-vlbi-y-geodesicos/CLASE.md); [B131-C11 · Plan completo de una clase de astronomía](../programa/clases/B131/B131-C11-plan-completo-de-una-clase-de-astronomia/CLASE.md).

### Bloque adaptativo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C16):** La compresión sin pérdida está acotada por la entropía; la con pérdida cambia fidelidad por volumen. La decisión central: ¿cuántos bits por píxel necesita la imagen y cuánto error se acepta a cambio de menos datos?

📘 **Dónde se aprende** (1 clase): [B47-C16 · Compresión de datos científicos](../programa/clases/B47/B47-C16-compresion-de-datos-cientificos/CLASE.md).

### Bloque de canal

- El bloque de canal tiene `255 × I` octetos.

💡 **Cómo se explica en la clase [B89-C11](../programa/clases/B89/B89-C11-telemetria-ccsds/CLASE.md):**
- Con `I = 5`, un bloque RS lleva `8920` bits de información (`1115` octetos); con el ASM de 4 octetos ocupa `1279` octetos de canal, de los que `1107` son datos de usuario (`0,8655`).
- Calcular los octetos de información, de bloque y de canal para `I = 1…8`.
- 🎯 **Por qué importa:** El receptor solo puede decodificar si encuentra el comienzo de cada bloque; la elección del marcador, su tolerancia y la profundidad de entrelazado deciden la latencia, el rendimiento y la pérdida de tramas.

📘 **Dónde se aprende** (1 clase): [B89-C11 · Telemetría CCSDS](../programa/clases/B89/B89-C11-telemetria-ccsds/CLASE.md).

### Bloque de Coulomb

- El bloque de Coulomb desliza con aceleración `g(sen β − μ cos β)`.

💡 **Cómo se explica en la clase [B66-C02](../programa/clases/B66/B66-C02-procesos-de-ladera-y-transporte-de-masa/CLASE.md):**
- Calcular la velocidad en la base y el tiempo de caída de un bloque de Coulomb.
- Bloque de Coulomb ILUSTRATIVO: H = 500 m, beta = 30 grados, mu = 0.4
- 🎯 **Por qué importa:** Un deslizamiento marciano o titaniano parece igual a uno terrestre, pero su velocidad y duración no lo son. La decisión central: ¿qué propiedades de un deslizamiento dependen de la gravedad y cuáles no?

📘 **Dónde se aprende** (1 clase): [B66-C02 · Procesos de ladera y transporte de masa](../programa/clases/B66/B66-C02-procesos-de-ladera-y-transporte-de-masa/CLASE.md).

### Bloque de información

- El bloque de información de RS tiene `223 × I` octetos (`I` = profundidad de entrelazado).
- El bloque de información `k` (5006, 7526 o 10046 bits) se amplía con una CRC-32 y 2 bits de terminación hasta `k̂`.

💡 **Cómo se explica en la clase [B89-C11](../programa/clases/B89/B89-C11-telemetria-ccsds/CLASE.md):**
- Paso 1 · Bloque de información. `223 octetos = 1784 bits`.
- Con `I = 5`, un bloque RS lleva `8920` bits de información (`1115` octetos); con el ASM de 4 octetos ocupa `1279` octetos de canal, de los que `1107` son datos de usuario (`0,8655`).
- 🎯 **Por qué importa:** El receptor solo puede decodificar si encuentra el comienzo de cada bloque; la elección del marcador, su tolerancia y la profundidad de entrelazado deciden la latencia, el rendimiento y la pérdida de tramas.

📘 **Dónde se aprende** (2 clases): [B89-C11 · Telemetría CCSDS](../programa/clases/B89/B89-C11-telemetria-ccsds/CLASE.md); [B92-C06 · Modulación y codificación en enlaces ópticos](../programa/clases/B92/B92-C06-modulacion-y-codificacion-en-enlaces-opticos/CLASE.md).

### Bloqueada

- Una tobera bloqueada tiene `M = 1` en la garganta y su flujo másico solo depende de `p₀`, `T₀` y `A_t`.

🎯 **Por qué importa (clase B79-C08):** B78-C03 trata la cámara pero no el flujo por la tobera. La teoría de expansión es lo que une la presión de cámara con el empuje.

📘 **Dónde se aprende** (1 clase): [B79-C08 · Flujo en toberas convergente-divergentes](../programa/clases/B79/B79-C08-flujo-en-toberas-convergente-divergentes/CLASE.md).

### Bloqueante

- Una operación es bloqueante si no devuelve el control hasta que su buffer puede reutilizarse.

💡 **Cómo se explica en la clase [B18-C02](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md):**
- Límite: en el correo real una carta enviada ya salió de tu casa; en MPI una operación bloqueante puede no volver hasta que el receptor la reciba, y eso es lo que causa los bloqueos mutuos.
- 🎯 **Por qué importa:** Ocho, cuarenta o cuatro mil núcleos de un clúster no comparten memoria. Para que cada uno propague su parte de un catálogo de órbitas y luego se junten los resultados, hay que decir quién envía qué a quién, y cuándo.

📘 **Dónde se aprende** (1 clase): [B18-C02 · Paso de mensajes con MPI](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md).

### Bloqueo

- El consenso exige que nadie bloquee. Bloqueo es la objeción que impide el consenso.

💡 **Cómo se explica en la clase [B119-C06](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md):**
- *Descripción textual:* la Asamblea crea COPUOS; este tiene dos subcomités y una secretaría; decide por consenso, lo que da poder de bloqueo a cada miembro.
- Paso 4. Lectura: el comité grande casi siempre tendría algún bloqueo si los miembros fueran independientes.
- 🎯 **Por qué importa:** Quien estudia el derecho espacial necesita saber dónde se negocia y cómo se decide; ninguna clase anterior trata los organismos. La decisión central: ¿cómo cambia la probabilidad de bloqueo cuando crece el número de miembros que deben consentir?

📘 **Dónde se aprende** (1 clase): [B119-C06 · Organismos UNOOSA y COPUOS](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md).

### Bloqueo de cardán

- El bloqueo de cardán es la pérdida de un grado de libertad en `pitch = ±90°`.
- El bloqueo de cardán ocurre cuando el ángulo intermedio hace que el primer y el tercer eje coincidan, de modo que dos giros se confunden y solo importa su suma o diferencia.

💡 **Cómo se explica en la clase [B10-C14](../programa/clases/B10/B10-C14-angulos-de-euler-y-singularidades/CLASE.md):**
- B -->|no| D["Bloqueo de cardán:<br/>solo ψ − φ importa"]
- Su límite: en el polo el problema es del sistema de coordenadas, no del objeto; en el bloqueo de cardán lo mismo, la orientación es perfectamente normal.
- 🎯 **Por qué importa:** Un satélite que apunta una antena al cenit tiene el cabeceo cerca de `90°`; si la actitud se guarda con ángulos de Euler, justo ahí el cálculo se vuelve inestable: ángulos que cambian muy rápido para movimientos pequeños, o dos conjuntos de ángulos distintos para la misma orientación.

📘 **Dónde se aprende** (2 clases): [B10-C14 · Ángulos de Euler y singularidades](../programa/clases/B10/B10-C14-angulos-de-euler-y-singularidades/CLASE.md); [B87-C02 · Representaciones de orientación](../programa/clases/B87/B87-C02-representaciones-de-orientacion/CLASE.md).

### Bloqueo de fase

- El bloqueo de fase ocurre si `|Δω| ≤ K` y `θ* = arcsen(Δω/K)`.

💡 **Cómo se explica en la clase [B105-C08](../programa/clases/B105/B105-C08-sueno-y-ritmos-circadianos/CLASE.md):**
- *Descripción textual:* el periodo de la luz fija el desajuste con el reloj; la ecuación de Adler lo compara con la fuerza de arrastre y da bloqueo de fase o deriva con un periodo de batido.
- Paso 4 · Fase de bloqueo. `θ* = arcsen(0,83) = 56°`, es decir 3,7 h de retraso.
- 🎯 **Por qué importa:** En órbita hay unos 16 amaneceres al día: la luz externa no sirve de reloj. La decisión central: ¿qué ciclo de luz puede sincronizar a un reloj de periodo 24,2 h con una fuerza de arrastre dada y cuánto tarda en realinearse tras un salto?

📘 **Dónde se aprende** (1 clase): [B105-C08 · Sueño y ritmos circadianos](../programa/clases/B105/B105-C08-sueno-y-ritmos-circadianos/CLASE.md).

### Bloqueo mutuo

- El bloqueo mutuo (*deadlock*) es un ciclo de espera.
- Un bloqueo mutuo (*deadlock*) ocurre cuando dos procesos esperan indefinidamente algo que solo el otro puede darles.

💡 **Cómo se explica en la clase [B18-C02](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md):**
- Límite: en el correo real una carta enviada ya salió de tu casa; en MPI una operación bloqueante puede no volver hasta que el receptor la reciba, y eso es lo que causa los bloqueos mutuos.
- Escribir y razonar un intercambio punto a punto sin bloqueo mutuo.
- ⚠️ **Error frecuente:** Bloqueo mutuo por `send` simultáneos. Se corrige con el ejercicio 4.
- 🎯 **Por qué importa:** Ocho, cuarenta o cuatro mil núcleos de un clúster no comparten memoria. Para que cada uno propague su parte de un catálogo de órbitas y luego se junten los resultados, hay que decir quién envía qué a quién, y cuándo.

📘 **Dónde se aprende** (2 clases): [B18-C02 · Paso de mensajes con MPI](../programa/clases/B18/B18-C02-paso-de-mensajes-con-mpi/CLASE.md); [B88-C28 · Inversión de prioridad y deadlocks](../programa/clases/B88/B88-C28-inversion-de-prioridad-y-deadlocks/CLASE.md).

### Bloqueo universal

- Un bloqueo universal vale para varias plataformas a la vez.

💡 **Cómo se explica en la clase [B14-C12](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md):**
- El `uv.lock` registra las versiones exactas resueltas, es un bloqueo universal (cubre sistemas operativos, arquitecturas y versiones de Python) y se debe versionar para que las instalaciones sean consistentes; es TOML legible, pero lo gestiona uv y no se edita a mano.
- Es la forma en que un bloqueo universal sirve a varias máquinas (S1).
- 🎯 **Por qué importa:** Tu análisis dio un período de 5553,624562 s en 2026. Un colega lo ejecuta con otra versión de SciPy y obtiene un cierre distinto; otro usa Python más antiguo y falla al importar. «En mi máquina funciona» no es un resultado científico.

📘 **Dónde se aprende** (1 clase): [B14-C12 · Ejecución reproducible con uv](../programa/clases/B14/B14-C12-ejecucion-reproducible-con-uv/CLASE.md).

### Bloques de transición

- Los bloques de transición son las cuatro submatrices `3 × 3` de la matriz `6 × 6` de HCW.

💡 **Cómo se explica en la clase [B76-C12](../programa/clases/B76/B76-C12-guiado-relativo/CLASE.md):**
- Escribir los bloques `Φ_rr`, `Φ_rv`, `Φ_vr`, `Φ_vv` de la matriz de transición de HCW.
- 🎯 **Por qué importa:** El mismo algoritmo sirve para cientos de maniobras, pero falla en tiempos singulares. La decisión central: ¿cómo se calculan los impulsos y para qué duraciones el problema está mal condicionado?

📘 **Dónde se aprende** (1 clase): [B76-C12 · Guiado relativo](../programa/clases/B76/B76-C12-guiado-relativo/CLASE.md).

### Bogie

- El bogie lleva las ruedas media y trasera.

💡 **Cómo se explica en la clase [B102-C04](../programa/clases/B102/B102-C04-suspension-rocker-bogie-y-mecanica-de-rovers/CLASE.md):**
- Ecuaciones: `N₁ + N₂ + N₃ = F`, momento nulo respecto del pivote del cuerpo y momento nulo del bogie respecto de su pivote.
- Con la rueda delantera en `+0,60 m`, el pivote rocker-bogie en `−0,20 m` y el bogie a `±0,35 m`, la solución cerrada es `N₁ = F (x_P − x_B)/(x₁ − x_B)`; el resto se reparte a partes iguales entre las ruedas del bogie.
- 🎯 **Por qué importa:** Un rover cruza rocas sin muelles ni amortiguadores. La decisión central: ¿dónde colocar el pivote del cuerpo para repartir la carga, y qué escalón puede subir una rueda con la tracción disponible?

📘 **Dónde se aprende** (1 clase): [B102-C04 · Suspensión rocker-bogie y mecánica de rovers](../programa/clases/B102/B102-C04-suspension-rocker-bogie-y-mecanica-de-rovers/CLASE.md).

### BOL

- El envejecimiento eleva `α` por radiación y contaminación. BOL y EOL son los extremos de la vida.

💡 **Cómo se explica en la clase [B85-C05](../programa/clases/B85/B85-C05-recubrimientos-opticos-termicos/CLASE.md):**
- Los que mantienen `250–320 K` en BOL y EOL: pintura blanca.
- Para `293,15 K` al Sol se necesita `α/ε = σT⁴/S₀ = 0,3077`: entre la pintura blanca BOL (`0,222`) y la del coating a medida.
- 🎯 **Por qué importa:** Cambiar un recubrimiento es la forma más barata de mover la temperatura de una superficie decenas de kelvin. La decisión central: ¿qué recubrimiento mantiene la superficie dentro del intervalo al principio y al final de la vida?

📘 **Dónde se aprende** (1 clase): [B85-C05 · Recubrimientos ópticos térmicos](../programa/clases/B85/B85-C05-recubrimientos-opticos-termicos/CLASE.md).

### Bolsa de opciones

- La bolsa de opciones reserva acciones para el equipo.

💡 **Cómo se explica en la clase [B124-C07](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md):**
- Serie A: 10,0 Mum con pre-money 40,0 ⇒ post-money 50,0; el inversionista recibe el 20 %, la bolsa de opciones el 10 % y los existentes quedan con el 70 %: `1785714,3` acciones posteriores y un precio de `28,0000` um por acción.
- El ejemplo conductor es un flujo sintético de 6 años con un VAN al 12 % de `57,640` Mum y una tasa interna de retorno de `23,88` %, y una empresa sintética cuyos fundadores pasan de 100 % a `56,0` % tras una semilla y una serie A con bolsa de opciones.
- ⚠️ **Error frecuente:** Olvidar que la bolsa de opciones diluye a los existentes. Se corrige con 8.4.
- 🎯 **Por qué importa:** El dinero privado tiene un costo distinto del público: se paga con retorno y con propiedad. La decisión central: ¿qué retorno exige y qué parte del proyecto se cede a cambio?

📘 **Dónde se aprende** (1 clase): [B124-C07 · Financiamiento privado](../programa/clases/B124/B124-C07-financiamiento-privado/CLASE.md).

### Boost de Lorentz

- Un boost de Lorentz es la transformación entre dos marcos inerciales con velocidad relativa `v` a lo largo de `x`.

💡 **Cómo se explica en la clase [B26-C02](../programa/clases/B26/B26-C02-transformaciones-de-lorentz/CLASE.md):**
- Escribir el *boost* de Lorentz con `γ` y `β`.
- El script [lorentz.py](lorentz.py) construye los *boosts*, comprueba `det = 1`, el invariante `s²` en cuatro marcos, que `Λ(β₁)Λ(β₂) = Λ(β)` a `10⁻¹²` y que la luz se conserva.
- 🎯 **Por qué importa:** Para comparar la hora de un reloj en órbita con la de uno en tierra, o la dirección de una señal vista desde dos naves, hace falta una fórmula que traduzca coordenadas entre marcos. Esa fórmula debe respetar los postulados de C01.

📘 **Dónde se aprende** (1 clase): [B26-C02 · Transformaciones de Lorentz](../programa/clases/B26/B26-C02-transformaciones-de-lorentz/CLASE.md).

### Bootstrap

- El filtro bootstrap es la versión que propaga con el modelo y pesa con la verosimilitud (S1 lo atribuye a Gordon y colaboradores, 1993).
- Un bootstrap remuestrea los pares (pronóstico, evento) con reemplazo para estimar la variabilidad de una métrica.
- El bootstrap estima la incertidumbre de una métrica remuestreando.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C24](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md):**
- El bootstrap con 1 000 remuestras da un intervalo del 95 % para el BSS de `[0,020; 0,064]`: la habilidad es positiva con la muestra dada, pero pequeña y con un rango relativo amplio.
- *Descripción textual:* de los pronósticos y eventos se calcula el puntaje de Brier y, con una referencia, el BSS; con un umbral se arma la tabla de contingencia y de ella POD, POFD, TSS y HSS; un bootstrap da la incertidumbre de las métricas; el informe declara referencia, umbral, muestra y límites.
- 🎯 **Por qué importa:** Un pronóstico de «no habrá llamarada» acierta el 90 % de los días en una época tranquila y no sirve de nada. La exactitud bruta premia lo trivial.

📘 **Dónde se aprende** (9 clases): [B12-C24 · Métricas de habilidad (skill scores) de pronóstico](../programa/clases/B12/B12-C24-metricas-de-habilidad-skill-scores-de-pronostico/CLASE.md); [B15-C18 · Filtros de partículas iniciales](../programa/clases/B15/B15-C18-filtros-de-particulas-iniciales/CLASE.md); [B57-C31 · Errores y validación de modelos de elevación](../programa/clases/B57/B57-C31-errores-y-validacion-de-modelos-de-elevacion/CLASE.md); [B74-C19 · Métricas de precisión de navegación](../programa/clases/B74/B74-C19-metricas-de-precision-de-navegacion/CLASE.md); [B103-C06 · Detección y catalogación de rocas en imágenes de superficie](../programa/clases/B103/B103-C06-deteccion-y-catalogacion-de-rocas-en-imagenes-de-superficie/CLASE.md); [B103-C08 · Métricas de evaluación de percepción](../programa/clases/B103/B103-C08-metricas-de-evaluacion-de-percepcion/CLASE.md) y 3 más.

### Bootstrap de flujo

- El bootstrap de flujo: transferir la escala de un calibrador a otro.

💡 **Cómo se explica en la clase [B51-C01](../programa/clases/B51/B51-C01-calibracion-de-amplitud-y-escala-de-flujo-con-calibradores-primarios/CLASE.md):**
- Ejercicio 12. Integrador. Elabora tu *ficha de la escala de flujo*: ecuación, ganancias, bootstrap, incertidumbre y límites.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de la escala de flujo*: ecuación, ganancias, bootstrap, incertidumbre y límites.
- 🎯 **Por qué importa:** Sin una escala de flujo, dos observaciones de la misma fuente en días distintos no se pueden comparar. La decisión central: ¿cómo se fija y se propaga una escala absoluta, y con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B51-C01 · Calibración de amplitud y escala de flujo con calibradores primarios](../programa/clases/B51/B51-C01-calibracion-de-amplitud-y-escala-de-flujo-con-calibradores-primarios/CLASE.md).

### Bootstrap paramétrico

- El bootstrap paramétrico simula nuevas mediciones con el modelo ajustado y las reajusta.

💡 **Cómo se explica en la clase [B105-C17](../programa/clases/B105/B105-C17-rehabilitacion-posterior-al-vuelo/CLASE.md):**
- Estimar la incertidumbre por bootstrap paramétrico.
- Bootstrap parametrico: k p2.5-p97.5 = 0.0300-0.0631;
- 🎯 **Por qué importa:** Prometer una fecha de recuperación sin su incertidumbre es engañoso: unas pocas mediciones ruidosas dan intervalos amplios. La decisión central: ¿cuánto tarda en recuperarse el 95 % y con qué incertidumbre, y cómo cambia para una persona lenta?

📘 **Dónde se aprende** (1 clase): [B105-C17 · Rehabilitación posterior al vuelo](../programa/clases/B105/B105-C17-rehabilitacion-posterior-al-vuelo/CLASE.md).

### Borde

- El borde (*halo*) es el contexto adicional de `R` píxeles alrededor de cada tesela que se lee para calcularla.

💡 **Cómo se explica en la clase [B14-C27](../programa/clases/B14/B14-C27-procesamiento-por-teselas-de-grandes-volumenes-de-imagenes/CLASE.md):**
- El borde de la tesela debe ser, como mínimo, `R`.
- Se procesa cada tesela con su borde de 2 píxeles y se recorta el centro.
- ⚠️ **Error frecuente:** Procesar teselas sin borde. Se corrige con la sección 8.3 y el ejercicio 8.
- 🎯 **Por qué importa:** Una cobertura global de imágenes ocupa terabytes y ningún equipo la carga entera. Para suavizarla, calcular un índice o detectar cambios hay que procesarla por pedazos.

📘 **Dónde se aprende** (1 clase): [B14-C27 · Procesamiento por teselas de grandes volúmenes de imágenes](../programa/clases/B14/B14-C27-procesamiento-por-teselas-de-grandes-volumenes-de-imagenes/CLASE.md).

### Borde interno

- El borde interno `r_in` es el ISCO.
- El borde interno es la pérdida de agua; el externo, el máximo invernadero de CO₂.

💡 **Cómo se explica en la clase [B27-C10](../programa/clases/B27/B27-C10-discos-de-acrecion/CLASE.md):**
- *Descripción textual:* la masa, la tasa de acreción y el borde interno dan el perfil de temperatura; integrándolo se obtiene la luminosidad, que equivale a una eficiencia fija por el borde.
- Un agujero de `10 M☉` con borde interno en `6 GM/c²` y luminosidad `0,1 L_Edd` tiene `L_Edd = 1,257 × 10³² W`, `L = 1,257 × 10³¹ W` y una tasa de acreción `Ṁ = 1,678 × 10¹⁵ kg/s = 2,66 × 10⁻⁸ M☉/año`.
- 🎯 **Por qué importa:** Un disco convierte hasta una fracción grande de `Ṁc²` en luz; su temperatura, que baja hacia fuera, decide en qué banda se ve (rayos X en un agujero estelar, ultravioleta en uno supermasivo). La decisión central: ¿cuánto vale la temperatura en cada radio y qué luminosidad produce una tasa de acreción dada?

📘 **Dónde se aprende** (2 clases): [B27-C10 · Discos de acreción](../programa/clases/B27/B27-C10-discos-de-acrecion/CLASE.md); [B56-C12 · Exoplanetas potencialmente habitables](../programa/clases/B56/B56-C12-exoplanetas-potencialmente-habitables/CLASE.md).

### Borde replicado

- Un borde replicado completa los píxeles que caen fuera de la imagen con el valor del borde.

🎯 **Por qué importa (clase B14-C27):** Una cobertura global de imágenes ocupa terabytes y ningún equipo la carga entera. Para suavizarla, calcular un índice o detectar cambios hay que procesarla por pedazos.

📘 **Dónde se aprende** (1 clase): [B14-C27 · Procesamiento por teselas de grandes volúmenes de imágenes](../programa/clases/B14/B14-C27-procesamiento-por-teselas-de-grandes-volumenes-de-imagenes/CLASE.md).

### Borde subpíxel

- El borde subpíxel se localiza con el máximo del gradiente más una interpolación.

💡 **Cómo se explica en la clase [B74-C25](../programa/clases/B74/B74-C25-deteccion-de-limbo-y-bordes-planetarios-en-imagenes-de-navegacion/CLASE.md):**
- *Descripción textual:* se lanzan rayos desde un centro aproximado, en cada uno se localiza el borde con precisión subpíxel, se conservan los puntos fuertes, se ajusta un círculo y de él salen dirección y distancia.
- El script [laboratorio.py](laboratorio.py) genera discos sintéticos completo y en cuarto, detecta el limbo en 180 rayos con borde subpíxel y ajusta un círculo; 300 realizaciones de ruido por caso (comprueba disco completo con error de centro y radio < 0,05 px).
- 🎯 **Por qué importa:** En un disco iluminado a medias, el borde oscuro no existe y un ajuste ingenuo se sesga. La decisión central: ¿qué parte del limbo es utilizable, con qué incertidumbre, y qué sesgo introduce la fase?

📘 **Dónde se aprende** (1 clase): [B74-C25 · Detección de limbo y bordes planetarios en imágenes de navegación](../programa/clases/B74/B74-C25-deteccion-de-limbo-y-bordes-planetarios-en-imagenes-de-navegacion/CLASE.md).

### Borrado temporal

- El borrado temporal presenta como solo pasado lo que sigue vivo.

🎯 **Por qué importa (clase B133-C04):** La divulgación llega a mucha gente y la apropiación suele ocurrir sin mala intención, por falta de método. La decisión central: ¿qué revisas antes de difundir un contenido sobre un saber que no es tuyo, y quién decide si se difunde?

📘 **Dónde se aprende** (1 clase): [B133-C04 · Riesgos de apropiación cultural en la divulgación](../programa/clases/B133/B133-C04-riesgos-de-apropiacion-cultural-en-la-divulgacion/CLASE.md).

### Bosque de aislamiento

- Un bosque de aislamiento divide el espacio con cortes aleatorios; un punto aislado en pocos cortes es anómalo (S1).

💡 **Cómo se explica en la clase [B17-C05](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md):**
- El bosque de aislamiento no supone forma y escala a muchas variables, pero su puntuación solo ordena.
- Menciona, entre otros, la envolvente elíptica (supone datos gaussianos y usa la distancia de Mahalanobis), el bosque de aislamiento (las anomalías tienen caminos más cortos en árboles de partición aleatoria) y el factor de valor atípico local (compara densidades locales) (S1).
- 🎯 **Por qué importa:** El subsistema térmico de un satélite entrega temperatura y corriente. Cada una, por separado, puede estar dentro de su rango normal y sin embargo la pareja ser imposible: la corriente alta con temperatura baja no ocurre nunca en operación sana.

📘 **Dónde se aprende** (1 clase): [B17-C05 · Detección de anomalías](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md).

### BPSK

- BPSK usa 2 fases (1 bit/símbolo);

💡 **Cómo se explica en la clase [B89-C08](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md):**
- BPSK y QPSK: `Q(√(2γ))`, con `γ = Eb/N0`. 8PSK: `erfc(√(3γ) sin(π/8))/3`. 16QAM: `(3/8) erfc(√(0,4γ))` (aproximaciones con Gray, relaciones estándar no consultadas).
- A 8 dB: BPSK `1,91e-04`; 8PSK `6,18e-03`; 16QAM `9,25e-03`.
- 🎯 **Por qué importa:** La elección de la modulación fija el `Eb/N0` requerido en el presupuesto de enlace y el ancho de banda ocupado; es la base de la codificación y la sincronización siguientes. La decisión central: ¿qué modulación da la tasa que necesito con el `Eb/N0` que mi enlace puede ofrecer?

📘 **Dónde se aprende** (1 clase): [B89-C08 · Modulación digital](../programa/clases/B89/B89-C08-modulacion-digital/CLASE.md).

### Brazo de palanca

- El brazo de palanca es la distancia desde el centroide al origen de la traslación; amplifica el error angular.
- El brazo de palanca es la distancia a la que un error angular se convierte en error lineal.

💡 **Cómo se explica en la clase [B15-C14](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md):**
- Calcular la incertidumbre del ángulo y de la traslación y entender el brazo de palanca.
- Ejercicio 7. Con centroide a 500 px del origen y `σ_θ = 0,00445° = 7,8 × 10⁻⁵` rad, ¿qué error de traslación añade el brazo de palanca?
- 🎯 **Por qué importa:** El telescopio apunta con deriva, la nave rota entre tomas y el campo gira un poco. Apilar diez imágenes sin alinearlas emborrona las estrellas; restar dos sin alinear crea falsos «residuos».

📘 **Dónde se aprende** (2 clases): [B15-C14 · Registro y alineación](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md); [B103-C02 · Calibración extrínseca y registro multisensor](../programa/clases/B103/B103-C02-calibracion-extrinseca-y-registro-multisensor/CLASE.md).

### Brazo inestable

- El brazo inestable son las configuraciones con densidad central mayor que la de masa máxima.

💡 **Cómo se explica en la clase [B27-C03](../programa/clases/B27/B27-C03-estrellas-de-neutrones/CLASE.md):**
- Obtener la masa máxima y reconocer el brazo inestable.
- Decrece de `1,055` a `1,013 M☉`: brazo inestable.
- 🎯 **Por qué importa:** Las masas y radios de las estrellas de neutrones son la mejor ventana a la materia a densidades nucleares. Para interpretarlos hay que saber qué cambia la relatividad respecto de Newton y por qué existe una masa máxima.

📘 **Dónde se aprende** (1 clase): [B27-C03 · Estrellas de neutrones](../programa/clases/B27/B27-C03-estrellas-de-neutrones/CLASE.md).

### Brazo material

- Un brazo material sería un brazo formado siempre por las mismas estrellas; una onda de densidad es un patrón que atraviesa a las estrellas.

💡 **Cómo se explica en la clase [B25-C02](../programa/clases/B25/B25-C02-brazos-espirales-y-barra-galactica/CLASE.md):**
- A["Brazo material<br/>(mismas estrellas)"] --> B["Rotación diferencial:<br/>se enrolla"]
- Paso 5 · Sentido. Si los brazos fueran materiales, el patrón observado solo podría durar una vuelta, y la edad de las estrellas del disco es mucho mayor.
- 🎯 **Por qué importa:** Los brazos espirales son lo más llamativo de una galaxia de disco, pero la rotación diferencial debería enrollarlos hasta borrarlos en unas pocas vueltas. Entender esa paradoja es entender qué es un brazo: no un montón fijo de materia, sino un patrón.

📘 **Dónde se aprende** (1 clase): [B25-C02 · Brazos espirales y barra galáctica](../programa/clases/B25/B25-C02-brazos-espirales-y-barra-galactica/CLASE.md).

### Brecha

- La brecha es `(voraz − óptimo)/óptimo`.
- Programación dinámica: solución exacta por subproblemas. Brecha: `(óptimo − obtenido)/óptimo`.
- Peso: valor operativo. Brecha: diferencia con el óptimo.

💡 **Cómo se explica en la clase [B96-C10](../programa/clases/B96/B96-C10-planificacion-de-cargas-utiles/CLASE.md):**
- Una regla voraz buena en este caso (brecha 0) no está garantizada en otros: solo el método exacto lo está.
- Paso 5 · Brecha. Voraz por valor: 3 puntos (10,3 %).
- 🎯 **Por qué importa:** Una observación que no cabe en la energía o en el almacenamiento no se hace, y una elegida a ojo puede dejar valor sin usar. La decisión central: ¿qué conjunto de observaciones da más valor dentro de la energía y los datos disponibles?

📘 **Dónde se aprende** (3 clases): [B96-C10 · Planificación de cargas útiles](../programa/clases/B96/B96-C10-planificacion-de-cargas-utiles/CLASE.md); [B96-C17 · Coordinación de múltiples estaciones](../programa/clases/B96/B96-C17-coordinacion-de-multiples-estaciones/CLASE.md); [B97-C09 · Robótica colaborativa](../programa/clases/B97/B97-C09-robotica-colaborativa/CLASE.md).

### Brecha de financiación

- La brecha de financiación es lo que hay que aportar para que la caja no baje de cero.

💡 **Cómo se explica en la clase [B125-C06](../programa/clases/B125/B125-C06-plan-empresarial-de-una-empresa-espacial/CLASE.md):**
- El flujo operativo es positivo desde el trimestre `6`; la caja mínima es `−25,7` M u.m. en el trimestre `10`; la brecha de financiación es `25,7` M u.m.
- Calcular el punto de equilibrio operativo, la caja mínima y la brecha de financiación.
- 🎯 **Por qué importa:** Integrar mercado, finanzas y operación en un plan es el cierre del módulo; el proyecto de B124 es general y no trata una empresa concreta con su caja. La decisión central: ¿cuánta caja necesita la empresa para llegar a su punto de equilibrio y qué supuestos pueden hundir el plan?

📘 **Dónde se aprende** (1 clase): [B125-C06 · Plan empresarial de una empresa espacial](../programa/clases/B125/B125-C06-plan-empresarial-de-una-empresa-espacial/CLASE.md).

### Bremsstrahlung

- El bremsstrahlung es la emisión por colisiones.

💡 **Cómo se explica en la clase [B34-C02](../programa/clases/B34/B34-C02-emision-euv-y-rayos-x-de-la-corona/CLASE.md):**
- Ejercicio 6. Razón de bremsstrahlung 10⁷/10⁶ K.
- bremsstrahlung integrado (n^2 T^(1/2)): cociente 1e7 K / 1e6 K = 3.1623 para igual EM
- 🎯 **Por qué importa:** Cada banda del espectro traza una temperatura. La decisión central: ¿en qué banda emite el plasma a una temperatura dada y cuánta potencia radia?

📘 **Dónde se aprende** (1 clase): [B34-C02 · Emisión EUV y rayos X de la corona](../programa/clases/B34/B34-C02-emision-euv-y-rayos-x-de-la-corona/CLASE.md).

### Brillo

- El flujo es la energía de luz recibida por unidad de área y tiempo; el brillo aparente es lo que percibimos de él.
- El brillo `B_ν` (W m⁻² Hz⁻¹ sr⁻¹).

💡 **Cómo se explica en la clase [B01-C09](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md):**
- El brillo da el flujo recibido, pero un objeto débil puede estar lejos o ser intrínsecamente poco luminoso: brillo y distancia están mezclados.
- Cada propiedad de la luz es un campo del mensaje: de dónde vino (dirección), cuánta llegó (brillo), de qué colores (espectro), si cambia (tiempo) y cómo vibra (polarización).
- ⚠️ **Error frecuente:** Confundir brillo con cercanía. Ejercicio 8.
- 🎯 **Por qué importa:** Sobre una galaxia a 43 Mpc solo tienes luz. De esa luz sale su dirección, cuánto brilla, de qué color es y qué líneas aparecen en su espectro; de las líneas sale `z = 0,0101` (C01).

📘 **Dónde se aprende** (2 clases): [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B46-C01 · Espectro radioastronómico](../programa/clases/B46/B46-C01-espectro-radioastronomico/CLASE.md).

### Brillo del cielo

- El brillo del cielo (*skyglow*) es la luz difusa en la atmósfera.
- Brillo del cielo: mag por arcsec².

💡 **Cómo se explica en la clase [B08-C12](../programa/clases/B08/B08-C12-limitacion-por-contaminacion-luminica/CLASE.md):**
- Falchi y colaboradores (S2) calcularon un atlas mundial del brillo artificial del cielo con datos de satélite de alta resolución y nuevas mediciones.
- Las páginas consultadas no describen el brillo del cielo en números.
- 🎯 **Por qué importa:** La mayoría de las personas ya no ve la Vía Láctea desde su casa. La pregunta motivadora: ¿qué tan oscuro es mi cielo, cuánto de eso es culpa de la Luna y cuánto de las luces, y qué puedo hacer?

📘 **Dónde se aprende** (2 clases): [B08-C12 · Limitación por contaminación lumínica](../programa/clases/B08/B08-C12-limitacion-por-contaminacion-luminica/CLASE.md); [B48-C18 · Protección del cielo oscuro](../programa/clases/B48/B48-C18-proteccion-del-cielo-oscuro/CLASE.md).

### Brillo relativo

- El brillo relativo es el cociente con el visto sobre el eje.

💡 **Cómo se explica en la clase [B28-C12](../programa/clases/B28/B28-C12-modelos-de-emision-conjunta/CLASE.md):**
- I --> R["brillo relativo = ⟨…⟩(θ_v)/⟨…⟩(0)"]
- *Descripción textual:* el perfil de energía y el factor Doppler, que depende del ángulo entre cada elemento y la visual, se integran sobre el chorro; el cociente con el valor sobre el eje da el brillo relativo.
- 🎯 **Por qué importa:** Un destello gamma débil puede ser un evento normal visto de lado. Un modelo de emisión conjunta permite relacionar qué se ve en cada mensajero con el ángulo de visión.

📘 **Dónde se aprende** (1 clase): [B28-C12 · Modelos de emisión conjunta](../programa/clases/B28/B28-C12-modelos-de-emision-conjunta/CLASE.md).

### Brillo superficial

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C10](../programa/clases/B41/B41-C10-apertura-y-relacion-focal/CLASE.md):**
- Calcular el brillo superficial `∝ 1/N²`.
- El f/4 da más brillo superficial; el f/10 una imagen más grande para el mismo ocular.
- 🎯 **Por qué importa:** La relación focal decide si un telescopio es «rápido» o «lento». La decisión central: ¿qué importa más, el diámetro o la relación focal?

📖 **Explicado a fondo:** [Brillo superficial](esencial/esencial-a-c.md#brillo-superficial) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B41-C10 · Apertura y relación focal](../programa/clases/B41/B41-C10-apertura-y-relacion-focal/CLASE.md).

### Brouwer

- El movimiento medio de Kozai es el publicado; el de Brouwer es el de la teoría.

💡 **Cómo se explica en la clase [B72-C21](../programa/clases/B72/B72-C21-propagador-sgp4-y-teoria-general-de-perturbaciones/CLASE.md):**
- *Descripción textual:* el conjunto de dos líneas se lee y valida; el movimiento medio publicado se convierte al de Brouwer; el periodo decide entre SGP4 y SDP4; con el semieje corregido se obtienen las tasas seculares.
- Un conjunto sintético (objeto `99999`, inexistente) con `n = 15,5 rev/día` tiene un semieje de Kozai `a₁ = 6794,865 km` y de Brouwer `a₀″ = 6795,376 km`; su periodo es `92,914 min` (SGP4) y la tasa del nodo con las constantes de SGP4 es `−4,9580 °/día`, `0,0001 °/día` de la de C03.
- ⚠️ **Error frecuente:** Confundir el movimiento medio de Kozai con el de Brouwer. Se corrige con 8.2.
- 🎯 **Por qué importa:** Un error clásico es tomar los elementos de dos líneas como elementos keplerianos y propagarlos con dos cuerpos: el error es de kilómetros en minutos. La decisión central: ¿qué propagador corresponde a un conjunto de elementos y qué transformaciones previas exige antes de usarlo?

📘 **Dónde se aprende** (1 clase): [B72-C21 · Propagador SGP4 y teoría general de perturbaciones](../programa/clases/B72/B72-C21-propagador-sgp4-y-teoria-general-de-perturbaciones/CLASE.md).

### Bucle

- Un bucle repite un bloque.

💡 **Cómo se explica en la clase [B07-C05](../programa/clases/B07/B07-C05-bucles-y-simulaciones-sencillas/CLASE.md):**
- Cada vuelta debe acercarte a que la condición se vuelva falsa; si no, tienes un bucle infinito (ejercicio 7).
- Con `x` (distancia caída) y `v` (rapidez) iniciales en 0, y `g` constante, el bucle de `caida_euler` hace, `t_total/dt` veces: `x = x + v*dt` y `v = v + g*dt`.
- ⚠️ **Error frecuente:** Bucle infinito. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Una simulación es un bucle: calcula el estado siguiente a partir del actual, una y otra vez. Si el paso es demasiado grande, el resultado se aparta de la realidad; si es demasiado pequeño, tarda.

📘 **Dónde se aprende** (1 clase): [B07-C05 · Bucles y simulaciones sencillas](../programa/clases/B07/B07-C05-bucles-y-simulaciones-sencillas/CLASE.md).

### Bucle infinito

- Un bucle infinito nunca termina porque su condición nunca se vuelve falsa.

💡 **Cómo se explica en la clase [B07-C05](../programa/clases/B07/B07-C05-bucles-y-simulaciones-sencillas/CLASE.md):**
- Cada vuelta debe acercarte a que la condición se vuelva falsa; si no, tienes un bucle infinito (ejercicio 7).
- Evitar el bucle infinito y explicar sus causas.
- ⚠️ **Error frecuente:** Bucle infinito. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Una simulación es un bucle: calcula el estado siguiente a partir del actual, una y otra vez. Si el paso es demasiado grande, el resultado se aparta de la realidad; si es demasiado pequeño, tarda.

📘 **Dónde se aprende** (1 clase): [B07-C05 · Bucles y simulaciones sencillas](../programa/clases/B07/B07-C05-bucles-y-simulaciones-sencillas/CLASE.md).

### Buen condicionamiento

- El buen condicionamiento es la propiedad de que un pequeño error en los datos produzca un pequeño error en el resultado (C03).

🎯 **Por qué importa (clase B04-C20):** Las distancias a las estrellas más cercanas se obtienen con un triángulo (el paralaje de C07): la base es la órbita de la Tierra y el ángulo es lo que cambia la dirección de la estrella.

📘 **Dónde se aprende** (1 clase): [B04-C20 · Triangulación espacial aplicada](../programa/clases/B04/B04-C20-triangulacion-espacial-aplicada/CLASE.md).

### Buffer

- Cola de eventos: lista ordenada por tiempo. Buffer: almacén de datos a bordo.

💡 **Cómo se explica en la clase [B96-C20](../programa/clases/B96/B96-C20-simulacion-de-jornada-de-control-de-mision/CLASE.md):**
- (2) `generado − bajado − buffer = 0` con tolerancia `10⁻⁶` relativa;
- La telemetría generada es 21,600 MB, se bajan 20,301 MB y 1,299 MB quedan en el buffer al cierre.
- 🎯 **Por qué importa:** Un ensayo en frío revela conflictos entre contactos, comandos y datos que no se ven sumando números aislados. La decisión central: ¿la jornada funciona de punta a punta y cuándo se detecta una anomalía?

📘 **Dónde se aprende** (1 clase): [B96-C20 · Simulación de jornada de control de misión](../programa/clases/B96/B96-C20-simulacion-de-jornada-de-control-de-mision/CLASE.md).

### Bulbo

- El bulbo es la concentración central de estrellas viejas, con forma de caja o cacahuete; la barra es su extensión alargada (C02).
- El bulbo es la componente central abultada.

💡 **Cómo se explica en la clase [B25-C01](../programa/clases/B25/B25-C01-estructura-de-la-via-lactea/CLASE.md):**
- Eso deja `~1 × 10¹⁰ M☉` para el bulbo y la barra dentro de la masa estelar total de `5 × 10¹⁰`: una consistencia, no una medida.
- Paso 5 · Sentido. La parte estelar del disco ronda un tercio de la masa interior estimada; el resto es bulbo, barra, gas y, sobre todo, un halo oscuro.
- 🎯 **Por qué importa:** Estamos dentro de la galaxia y no podemos fotografiarla desde fuera: su forma se reconstruye midiendo distancias y velocidades desde un punto que no es el centro. Sin un esquema claro de componentes (bulbo, barra, disco, halo) y de cifras de referencia, el resto del bloque carece de escala.

📘 **Dónde se aprende** (2 clases): [B25-C01 · Estructura de la Vía Láctea](../programa/clases/B25/B25-C01-estructura-de-la-via-lactea/CLASE.md); [B25-C09 · Galaxias elípticas y espirales](../programa/clases/B25/B25-C09-galaxias-elipticas-y-espirales/CLASE.md).

### Bulbo de Plummer

- El bulbo de Plummer `Φ = −GM/√(r² + b²)`.

🎯 **Por qué importa (clase B38-C05):** Toda simulación de estrellas necesita una fuerza. La decisión central: ¿qué potencial simple reproduce una curva de rotación plana y cuánto aporta cada componente?

📘 **Dónde se aprende** (1 clase): [B38-C05 · Potenciales galácticos: Plummer, Miyamoto-Nagai y NFW](../programa/clases/B38/B38-C05-potenciales-galacticos-plummer-miyamoto-nagai-y-nfw/CLASE.md).

### Bundle Protocol (BP)

- El Bundle Protocol (BP) crea una red de almacenamiento y reenvío con tolerancia a conectividad intermitente, retransmisión basada en custodia y reportes de estado (CCSDS 734.2-B-1).

💡 **Cómo se explica en la clase [B89-C13](../programa/clases/B89/B89-C13-protocolos-para-espacio-profundo/CLASE.md):**
- Describir el almacenamiento y reenvío del Bundle Protocol.
- 🎯 **Por qué importa:** Sin almacenamiento y reenvío, un rover marciano no podría comunicarse con Tierra: nunca hay una ruta continua. Entender los contactos, las capacidades y el encaminamiento es la base del diseño de redes interplanetarias.

📘 **Dónde se aprende** (1 clase): [B89-C13 · Protocolos para espacio profundo](../programa/clases/B89/B89-C13-protocolos-para-espacio-profundo/CLASE.md).

### Burbuja

- Una burbuja es la región de gas caliente creada por una explosión; su radio sigue `R = ξ (E t²/ρ)^{1/5}` con `E` la energía, `t` el tiempo y `ρ` la densidad del medio;

💡 **Cómo se explica en la clase [B25-C16](../programa/clases/B25/B25-C16-retroalimentacion-estelar/CLASE.md):**
- Resulta `a = 1/5`, `b = −1/5` y `c = 2/5`: `R ∝ (E t²/ρ)^{1/5}`, justo la forma de la burbuja.
- Burbujas de Sedov con enfriamiento: dan cuánto de la energía llega a gas lejano.
- ⚠️ **Error frecuente:** Pensar que la burbuja crece sin pérdidas. Se corrige en 8.5.
- 🎯 **Por qué importa:** Sin retroalimentación, el gas de una galaxia se convertiría en estrellas mucho más deprisa de lo observado. Las supernovas, los vientos y la radiación de las estrellas masivas calientan y expulsan gas, y lo enriquecen con metales (C17).

📘 **Dónde se aprende** (1 clase): [B25-C16 · Retroalimentación estelar](../programa/clases/B25/B25-C16-retroalimentacion-estelar/CLASE.md).

### Bus de potencia

- Bus de potencia: red que distribuye la energía.

💡 **Cómo se explica en la clase [B90-C07](../programa/clases/B90/B90-C07-integracion-electrica-de-buses/CLASE.md):**
- Con `P = 12 W`: `V_c = 8,2042 V`, `I = 1,4627 A`, caída `195,8 mV` y pérdida `I²R = 0,2864 W` (2,4 % de la potencia).
- Límite: aquí el «caudal» sube cuando baja la presión, porque la carga exige potencia constante.
- 🎯 **Por qué importa:** Una carga de potencia constante pide más corriente cuando baja la tensión, de modo que un arnés largo o delgado puede hundir el bus justo cuando más se necesita. Y al conectar una carga con capacitor, la corriente inicial puede ser decenas de amperios.

📘 **Dónde se aprende** (1 clase): [B90-C07 · Integración eléctrica de buses](../programa/clases/B90/B90-C07-integracion-electrica-de-buses/CLASE.md).

### Bus regulado

- El bus regulado mantiene una tensión fija en la fuente.

💡 **Cómo se explica en la clase [B86-C07](../programa/clases/B86/B86-C07-distribucion-de-potencia/CLASE.md):**
- Ejercicio 9 · transferencia. Transferencia. Un equipo opera a `5 V` regulados desde un bus de `28 V` con `5 m` de cable fino.
- 🎯 **Por qué importa:** Un cable largo y fino desperdicia potencia y baja la tensión que ve el equipo; uno grueso pesa. La tensión del bus cambia la corriente, y por tanto las pérdidas, con el cuadrado.

📘 **Dónde se aprende** (1 clase): [B86-C07 · Distribución de potencia](../programa/clases/B86/B86-C07-distribucion-de-potencia/CLASE.md).

### Buscador

- El buscador es un visor pequeño de campo ancho para apuntar.

💡 **Cómo se explica en la clase [B08-C14](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md):**
- Mantén tapa en el buscador y objetivo cuando no lo uses.
- 🎯 **Por qué importa:** Un telescopio de juguete anuncia «600×» y decepciona. La pregunta motivadora: ¿qué telescopio me conviene y qué podré ver con él?

📘 **Dónde se aprende** (1 clase): [B08-C14 · Telescopios de iniciación](../programa/clases/B08/B08-C14-telescopios-de-iniciacion/CLASE.md).

### Búsqueda

- Una búsqueda devuelve una lista de registros sin descargar archivos.

💡 **Cómo se explica en la clase [B14-C22](../programa/clases/B14/B14-C22-acceso-a-datos-heliofisicos-abiertos-con-sunpy/CLASE.md):**
- Antes de ejecutar, calcula cuántos registros esperas. 24 h con cadencia de 12 s: 7200 registros por banda; la búsqueda devuelve 7200.
- Si el proveedor B «no responde», la búsqueda del laboratorio devuelve solo los 600 registros de A y conserva el mensaje «proveedor B no respondió».
- ⚠️ **Error frecuente:** No registrar la fecha de la búsqueda. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Quieres estudiar una región activa del Sol durante un día usando imágenes ultravioleta. Hay cientos de miles de archivos repartidos en varios proveedores.

📘 **Dónde se aprende** (1 clase): [B14-C22 · Acceso a datos heliofísicos abiertos con SunPy](../programa/clases/B14/B14-C22-acceso-a-datos-heliofisicos-abiertos-con-sunpy/CLASE.md).

### Búsqueda binaria

- La búsqueda binaria compara con el elemento del medio de una lista ordenada y descarta la mitad que no puede contener el objetivo; repite con la mitad restante (S3).

💡 **Cómo se explica en la clase [B07-C18](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md):**
- Límite de la analogía: el diccionario está ordenado por construcción; si la lista no está ordenada, la búsqueda binaria da resultados sin sentido y no avisa.
- Para búsquedas repetidas por clave exacta, un diccionario (C07) es más rápido que la búsqueda binaria; la binaria sirve para rangos y posiciones.
- ⚠️ **Error frecuente:** Usar búsqueda binaria en una lista desordenada. Se corrige con el ejercicio 3.
- 🎯 **Por qué importa:** Un catálogo estelar tiene millones de objetos. Buscar uno a uno es posible con diez planetas y ruinoso con diez millones.

📘 **Dónde se aprende** (1 clase): [B07-C18 · Algoritmos de búsqueda y ordenamiento](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md).

### Búsqueda en anchura

- La búsqueda en anchura da el camino más corto en pasos de 4 vecinos.

💡 **Cómo se explica en la clase [B53-C20](../programa/clases/B53/B53-C20-proyecto-sig-de-terreno-extraterrestre/CLASE.md):**
- Buscar un camino con búsqueda en anchura.
- El script [sig.py](sig.py) calcula la pendiente de Horn, la verifica con dos superficies, aplica el umbral y busca el camino con búsqueda en anchura (comprueba 10⁻⁶° en el plano y 0,05° en el paraboloide).
- 🎯 **Por qué importa:** Un derivado sin verificar propaga errores a la decisión. La decisión central: ¿qué parte del terreno cumple un criterio de pendiente y existe un camino que lo respete?

📘 **Dónde se aprende** (1 clase): [B53-C20 · Proyecto SIG de terreno extraterrestre](../programa/clases/B53/B53-C20-proyecto-sig-de-terreno-extraterrestre/CLASE.md).

### Búsqueda en velocidad

- La búsqueda en velocidad barre `v` y cuenta cuántas líneas predichas tienen una observada a menos de `δ`.

💡 **Cómo se explica en la clase [B62-C08](../programa/clases/B62/B62-C08-mezclas-moleculares-y-confusion-de-lineas/CLASE.md):**
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de confusión de líneas*: fracción mezclada, falsas esperadas por `k`, resultado de la búsqueda en velocidad y límites del modelo, rotulando lo sintético.
- 🎯 **Por qué importa:** Una línea que coincide con una frecuencia de catálogo no identifica una molécula: puede ser casualidad. La decisión central: ¿cuántas líneas hacen falta para afirmar una identificación con riesgo bajo de falsa alarma?

📘 **Dónde se aprende** (1 clase): [B62-C08 · Mezclas moleculares y confusión de líneas](../programa/clases/B62/B62-C08-mezclas-moleculares-y-confusion-de-lineas/CLASE.md).

### Búsqueda exhaustiva

- La búsqueda exhaustiva prueba todas las combinaciones.

💡 **Cómo se explica en la clase [B117-C05](../programa/clases/B117/B117-C05-inventario-y-gestion-del-equipo-medico-a-bordo/CLASE.md):**
- Con 8 artículos, hasta 3 unidades (1 el equipo de reanimación) y pasos de 10 g y 10 cm³, la programación dinámica da un beneficio de `14,827484`, idéntico al de la búsqueda exhaustiva (32 768 combinaciones), con la misma selección.
- Resolver la selección bajo dos restricciones con programación dinámica y verificarla con búsqueda exhaustiva.
- 🎯 **Por qué importa:** Ninguna clase anterior trata el equipo médico de a bordo. La decisión central: ¿qué embarcar bajo un límite de masa y volumen y qué riesgo de quedarse sin él se acepta?

📘 **Dónde se aprende** (1 clase): [B117-C05 · Inventario y gestión del equipo médico a bordo](../programa/clases/B117/B117-C05-inventario-y-gestion-del-equipo-medico-a-bordo/CLASE.md).

### Búsqueda lineal

- La búsqueda lineal recorre la lista elemento a elemento hasta hallar el objetivo.

💡 **Cómo se explica en la clase [B07-C18](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md):**
- Implementar la búsqueda lineal y la binaria, y explicar cuándo se puede usar la binaria.
- Ejercicio 11 · transferencia. Un compañero afirma que la búsqueda binaria «siempre es mejor» que la lineal.
- 🎯 **Por qué importa:** Un catálogo estelar tiene millones de objetos. Buscar uno a uno es posible con diez planetas y ruinoso con diez millones.

📘 **Dónde se aprende** (1 clase): [B07-C18 · Algoritmos de búsqueda y ordenamiento](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md).

### Búsqueda voraz

- Una búsqueda voraz agrega en cada paso la banda que más mejora el objetivo.

💡 **Cómo se explica en la clase [B57-C25](../programa/clases/B57/B57-C25-seleccion-de-bandas-espectrales-segun-el-fenomeno/CLASE.md):**
- La búsqueda exhaustiva nunca es peor que la voraz; en este caso la diferencia es `0,0000` con 3 bandas.
- *Descripción textual:* las medias por banda dan una distancia normalizada, de ella la separabilidad JM, y el objetivo mínimo guía la búsqueda exhaustiva o voraz del mejor subconjunto.
- 🎯 **Por qué importa:** Cada banda cuesta datos, masa y complejidad. La decisión central: ¿con qué menor número de bandas se separan las clases que me interesan y cuál es el par más difícil de distinguir?

📘 **Dónde se aprende** (1 clase): [B57-C25 · Selección de bandas espectrales según el fenómeno](../programa/clases/B57/B57-C25-seleccion-de-bandas-espectrales-segun-el-fenomeno/CLASE.md).
