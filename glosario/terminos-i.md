# Términos · I

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · [C](terminos-c.md) · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · **I** · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

### IA

- Los términos del modelo: IA y IE (ceros de acimut y altura), CA (colimación), NPAE (no perpendicularidad de ejes), AN y AW (inclinación del eje vertical al norte y al oeste) y TF (flexión del tubo).

🎯 **Por qué importa (clase B43-C26):** El modelo convierte errores de decenas de segundos de arco en residuos de segundos de arco. La decisión central: ¿qué términos incluir, cuántas estrellas medir y con qué incertidumbre se determina cada parámetro?

📘 **Dónde se aprende** (1 clase): [B43-C26 · Modelo de flexiones y de apuntado de una montura](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md).

### IAE

- El IAE es `∫|r − y| dt`, un resumen de la calidad de la respuesta.

💡 **Cómo se explica en la clase [B16-C12](../programa/clases/B16/B16-C12-sintonia-de-controladores-pid/CLASE.md):**
- La respuesta al escalón de este lazo, con filtro derivativo `N = 10`, da un sobreimpulso de 42,7 %, un asentamiento (2 %) de 9,19 y un IAE de 1,76.
- Reducir `Kp` a la mitad (2,4) con los mismos `Ti` y `Td` baja el sobreimpulso a 26,4 % y el asentamiento a 7,85, con un IAE de 1,85 (algo peor).
- ⚠️ **Error frecuente:** Creer que un IAE menor es siempre mejor. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** En un proyecto real, las ganancias iniciales de un lazo se eligen con pocas medidas y bajo presión de calendario: a veces no hay un modelo preciso. Hay reglas que solo piden hacer oscilar el lazo con un controlador proporcional y medir dos números.

📘 **Dónde se aprende** (1 clase): [B16-C12 · Sintonía de controladores PID](../programa/clases/B16/B16-C12-sintonia-de-controladores-pid/CLASE.md).

### IAWN

- IAWN es la red internacional de alerta de asteroides, coordinada por NASA, creada por recomendación de un grupo de trabajo de la ONU [S7].

💡 **Cómo se explica en la clase [B58-C18](../programa/clases/B58/B58-C18-marco-internacional-de-defensa-planetaria/CLASE.md):**
- Según [S7], IAWN es una colaboración mundial de astrónomos y modeladores coordinada por NASA, establecida por recomendación del grupo de trabajo sobre objetos cercanos a la Tierra de la subcomisión científica de la COPUOS, endosada en febrero de 2013 y reconocida por la Asamblea General de la ONU.
- ⚠️ **Error frecuente:** Atribuir a IAWN la decisión de desviar. Se corrige con 8.1.
- 🎯 **Por qué importa:** Un umbral de notificación decide cuántos casos entran en el circuito internacional y cuántos tienen tiempo suficiente. La decisión central: ¿qué umbral activa la alerta y qué margen de tiempo deja para actuar?

📘 **Dónde se aprende** (1 clase): [B58-C18 · Marco internacional de defensa planetaria](../programa/clases/B58/B58-C18-marco-internacional-de-defensa-planetaria/CLASE.md).

### IC 95 %

- El IC 95 % son los percentiles 2,5 y 97,5.

💡 **Cómo se explica en la clase [B107-C06](../programa/clases/B107/B107-C06-estimacion-y-modelado-de-la-recuperacion-posterior-al-vuelo/CLASE.md):**
- El ajuste da `τ = 22,8 d` y `D = 18,9 %`; el remuestreo da `τ = 23,0 ± 3,2 d` (IC 95 %: 17,5–29,3) y `t95 = 68,2 d` (IC 52,4–87,6), frente al verdadero 74,9 d.
- 🎯 **Por qué importa:** Los fragmentos consultados indican pérdida de fuerza muscular tras misiones largas con riesgos operativos y médicos (English et al., 2015), cambios en tareas funcionales y sus factores fisiológicos (Mulavara et al., 2018) y alteraciones del control postural y locomotor (Macaulay et al., 2021).

📘 **Dónde se aprende** (1 clase): [B107-C06 · Estimación y modelado de la recuperación posterior al vuelo](../programa/clases/B107/B107-C06-estimacion-y-modelado-de-la-recuperacion-posterior-al-vuelo/CLASE.md).

### ICC(1,1)

- El ICC(1,1) es `(MSB − MSW)/(MSB + (k − 1) MSW)`.

💡 **Cómo se explica en la clase [B105-C26](../programa/clases/B105/B105-C26-medidas-fisiologicas-y-biomarcadores-en-investigacion-espacial/CLASE.md):**
- Con pocos participantes el ICC es muy incierto y el intervalo cubre menos del 95 %.
- V["variacion entre (10) y<br/>dentro (4)"] --> I["ICC = 100/(100+16)"]
- ⚠️ **Error frecuente:** Confiar en un ICC estimado con pocos participantes. Da su incertidumbre (8.2).
- 🎯 **Por qué importa:** Un biomarcador con alta variación interna no detecta cambios pequeños aunque sea «preciso». Con pocos participantes, además, el propio ICC es incierto.

📘 **Dónde se aprende** (1 clase): [B105-C26 · Medidas fisiológicas y biomarcadores en investigación espacial](../programa/clases/B105/B105-C26-medidas-fisiologicas-y-biomarcadores-en-investigacion-espacial/CLASE.md).

### ICD

- El ICD es el contrato entre productor y consumidor.
- Un ICD (*interface control document*) lo especifica.
- ICD: documento de control de interfaces.

💡 **Cómo se explica en la clase [B83-C08](../programa/clases/B83/B83-C08-interfaz-entre-subsistemas/CLASE.md):**
- I["Interfaz"] --> P["Parametros del ICD"]
- 🎯 **Por qué importa:** La mayoría de los fallos de integración aparecen en las interfaces: un conector mal definido, una tensión fuera de rango o una tasa de datos insuficiente. La decisión central: ¿cada interfaz cumple en su caso más desfavorable, con margen, antes de construir?

📘 **Dónde se aprende** (3 clases): [B83-C08 · Interfaz entre subsistemas](../programa/clases/B83/B83-C08-interfaz-entre-subsistemas/CLASE.md); [B88-C21 · Interfaces y documentos de control de software de vuelo](../programa/clases/B88/B88-C21-interfaces-y-documentos-de-control-de-software-de-vuelo/CLASE.md); [B90-C05 · Documentación de interfaces](../programa/clases/B90/B90-C05-documentacion-de-interfaces/CLASE.md).

### ICRS

- El ICRS es el sistema de referencia celeste de la IAU, que realiza el ecuatorial en la práctica.

💡 **Cómo se explica en la clase [B04-C19](../programa/clases/B04/B04-C19-transformaciones-de-coordenadas-astronomicas/CLASE.md):**
- Su límite: los sistemas aquí tratados son fijos en el ICRS; en cuanto el sistema depende del tiempo (precesión) o del observador, se necesitan más piezas.
- Depende de que `(α, δ)` esté en el marco ICRS (hipótesis didáctica: la documentación del archivo no declara el marco) y no incluye movimiento propio.
- 🎯 **Por qué importa:** Un catálogo da las posiciones en ecuatoriales; un estudio de la Vía Láctea necesita galácticas; un análisis del plano del sistema solar usa eclípticas. Cambiar de sistema es rutina, y un error de signo o de matriz mueve el objeto decenas de grados.

📘 **Dónde se aprende** (1 clase): [B04-C19 · Transformaciones de coordenadas astronómicas](../programa/clases/B04/B04-C19-transformaciones-de-coordenadas-astronomicas/CLASE.md).

### ID de línea base

- El ID de línea base es el hash del manifiesto.

🎯 **Por qué importa (clase B88-C18):** Si no se sabe exactamente qué firmware vuela, no se puede reproducir un fallo ni comprobar que se probó lo que se lanzó. La decisión central: ¿qué registro identifica de manera única una versión y permite verificarla?

📘 **Dónde se aprende** (1 clase): [B88-C18 · Control de configuración de firmware](../programa/clases/B88/B88-C18-control-de-configuracion-de-firmware/CLASE.md).

### Ida y vuelta

- El retardo de ida es `d/c`; el de ida y vuelta (RTT), `2d/c`.

💡 **Cómo se explica en la clase [B105-C15](../programa/clases/B105/B105-C15-telemedicina-espacial/CLASE.md):**
- *Descripción textual:* la distancia fija el retardo de ida y vuelta; el volumen y el ancho de banda fijan el tiempo de transferencia; el tiempo de consulta suma turnos por RTT, transferencia y procesamiento, y se compara un diseño por turnos con uno de un solo paquete.
- ⚠️ **Error frecuente:** Usar `d/c` como ida y vuelta. El RTT es `2d/c`.
- 🎯 **Por qué importa:** Una conversación en tiempo real es posible a la Luna (2,6 s de ida y vuelta) y deja de serlo a Marte (hasta 42 min). La decisión central: ¿cuánto dura una consulta según el destino y el diseño del intercambio (varios turnos o un paquete completo)?

📘 **Dónde se aprende** (1 clase): [B105-C15 · Telemedicina espacial](../programa/clases/B105/B105-C15-telemedicina-espacial/CLASE.md).

### Ida y vuelta de serialización

- La ida y vuelta de serialización es escribir el cuaderno a texto y leerlo de nuevo sin perder nada.

🎯 **Por qué importa (clase B14-C09):** Alguien te manda un cuaderno con un gráfico que apoya una conclusión. Lo abres, ejecutas las celdas y el gráfico sale distinto.

📘 **Dónde se aprende** (1 clase): [B14-C09 · Jupyter y experimentos reproducibles](../programa/clases/B14/B14-C09-jupyter-y-experimentos-reproducibles/CLASE.md).

### Ida y vuelta (RTT)

- Retardo de propagación: `d/c`. Ida y vuelta (RTT): `2d/c`.

💡 **Cómo se explica en la clase [B96-C01](../programa/clases/B96/B96-C01-segmento-espacial-y-segmento-terrestre/CLASE.md):**
- Un satélite geoestacionario está a 35 786 km: la ida y vuelta es de 0,239 s.
- Marte, entre 5,5×10⁷ y 4×10⁸ km, impone de 367 s a 2 669 s de ida y vuelta.
- ⚠️ **Error frecuente:** Confundir ida con ida y vuelta. El ciclo de un comando usa `2d/c` (8.2)
- 🎯 **Por qué importa:** Quien opera una nave no puede tratarla como un equipo de laboratorio: cada comando viaja a la velocidad de la luz y cada contacto dura minutos. La decisión central: ¿qué segmento hace qué y cuánto tardan en comunicarse?

📘 **Dónde se aprende** (1 clase): [B96-C01 · Segmento espacial y segmento terrestre](../programa/clases/B96/B96-C01-segmento-espacial-y-segmento-terrestre/CLASE.md).

### Idempotencia

- La idempotencia es que repetir no cambia el resultado.

💡 **Cómo se explica en la clase [B14-C30](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md):**
- Es la única fuente consultada: la idempotencia, el control de calidad y los reintentos son técnicas generales que aquí se demuestran con un experimento, no se atribuyen a una fuente.
- 🎯 **Por qué importa:** Cada madrugada llegan datos nuevos. Si un humano debe lanzar cada paso, tarde o temprano se olvida uno; si un lote corrupto atraviesa la cadena, contamina el producto final; si un fallo de red detiene todo y al reiniciar se repite desde cero, se pierde tiempo.

📘 **Dónde se aprende** (1 clase): [B14-C30 · Cadenas de procesamiento automatizado de datos](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md).

### Identidad

- Una identidad es una igualdad válida para cualquier valor (`(a + b)² = a² + 2ab + b²`).
- Una identidad es una igualdad que se cumple para todos los valores donde está definida (a diferencia de una ecuación, que se cumple solo para algunos).
- Una identidad es la cuenta que representa a una persona.

💡 **Cómo se explica en la clase [B04-C06](../programa/clases/B04/B04-C06-identidades-trigonometricas/CLASE.md):**
- Una identidad se puede *comprobar* sin demostrarla: se evalúa en varios ángulos distintos y se verifica que ambos lados coincidan dentro de la tolerancia.
- Como el punto está siempre a distancia 1 del centro, el teorema de Pitágoras da `sen²x + cos²x = 1`: es la identidad fundamental.
- 🎯 **Por qué importa:** Casi toda medición astronómica es un ángulo: la posición de una estrella respecto de otra, el tamaño aparente de la Luna, el desplazamiento por paralaje. Y casi todos esos ángulos son diminutos, de segundos de arco.

📘 **Dónde se aprende** (3 clases): [B03-C13 · Expresiones algebraicas iniciales](../programa/clases/B03/B03-C13-expresiones-algebraicas-iniciales/CLASE.md); [B04-C06 · Identidades trigonométricas](../programa/clases/B04/B04-C06-identidades-trigonometricas/CLASE.md); [B122-C05 · Control de accesos y gestión de identidades en operaciones](../programa/clases/B122/B122-C05-control-de-accesos-y-gestion-de-identidades-en-operaciones/CLASE.md).

### Identidad contable

- La identidad contable del `Δv` es `V_eq ln(MR) = v_f + L_g + L_d`.

🎯 **Por qué importa (clase B77-C09):** La velocidad final de un ascenso es el `Δv` ideal menos dos pérdidas. La decisión central: ¿cuánto vale la pérdida aerodinámica frente a la gravitacional y de qué depende?

📘 **Dónde se aprende** (1 clase): [B77-C09 · Pérdidas aerodinámicas](../programa/clases/B77/B77-C09-perdidas-aerodinamicas/CLASE.md).

### Identidad de Bianchi contraída

- La identidad de Bianchi contraída implica `∇^a G_ab = 0`.

🎯 **Por qué importa (clase B39-C05):** Las ecuaciones de campo conectan la geometría con la materia. La decisión central: ¿en qué régimen la gravedad de Einstein se reduce a la de Newton y qué garantiza la consistencia de las ecuaciones?

📘 **Dónde se aprende** (1 clase): [B39-C05 · Ecuaciones de campo de Einstein y límite newtoniano](../programa/clases/B39/B39-C05-ecuaciones-de-campo-de-einstein-y-limite-newtoniano/CLASE.md).

### Identidad de la energía

- La identidad de la energía `Δε = V_m Δv_t` relaciona el cambio de energía con el de la componente tangencial.

🎯 **Por qué importa (clase B75-C26):** Cada luna es un peldaño de energía en torno a Júpiter. La decisión central: ¿qué órbitas jovianas puede alcanzar una nave con un sobrevuelo de Ganimedes de `v∞` dado y cuánto cambia la energía en un solo paso?

📘 **Dónde se aprende** (1 clase): [B75-C26 · Sobrevuelos de lunas y tours de sistemas planetarios](../programa/clases/B75/B75-C26-sobrevuelos-de-lunas-y-tours-de-sistemas-planetarios/CLASE.md).

### Identidad de Parseval

- La identidad de Parseval dice que la energía total es la misma en el tiempo y en la frecuencia.

🎯 **Por qué importa (clase B15-C04):** Si una estrella pulsa con una pequeña amplitud en medio del ruido, mirar la curva de luz no la revela, pero su espectro de frecuencias sí: un pico a una frecuencia concreta. Lo mismo ocurre con una vibración en una estructura espacial, una señal de radio o un periodo en un registro geofísico.

📘 **Dónde se aprende** (1 clase): [B15-C04 · Transformada de Fourier](../programa/clases/B15/B15-C04-transformada-de-fourier/CLASE.md).

### Identidad exacta

- La identidad exacta `|⟨e^{iφ}⟩|²`.

🎯 **Por qué importa (clase B42-C24):** Sin una métrica estandarizada no se pueden comparar sistemas ni lazos. La decisión central: ¿qué métrica usar para cada pregunta y qué dice cada una?

📘 **Dónde se aprende** (1 clase): [B42-C24 · Métricas de desempeño de óptica adaptativa: Strehl y energía encerrada](../programa/clases/B42/B42-C24-metricas-de-desempeno-de-optica-adaptativa-strehl-y-energia-encerrada/CLASE.md).

### Identificable

- Gauss-Newton: iteración que linealiza el modelo. Identificable: parámetro que cambia las mediciones.

💡 **Cómo se explica en la clase [B101-C05](../programa/clases/B101/B101-C05-calibracion-cinematica-de-manipuladores/CLASE.md):**
- Si la herramienta estuviera sobre el eje, `dθ₇` no cambiaría la posición (efecto `0` m): no sería identificable.
- 🎯 **Por qué importa:** Un error de 0,5° en un ángulo cero produce centímetros en el extremo de un brazo de casi 2 m. La decisión central: ¿qué parámetros puedo estimar con las mediciones que tengo y con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B101-C05 · Calibración cinemática de manipuladores](../programa/clases/B101/B101-C05-calibracion-cinematica-de-manipuladores/CLASE.md).

### Identificable en la práctica

- Un parámetro es identificable estructuralmente si datos perfectos (sin ruido) lo determinan; identificable en la práctica si los datos reales, con su ruido y su cantidad, lo acotan por ambos lados.

🎯 **Por qué importa (clase B22-C03):** Un ajuste siempre devuelve números. Que el programa converja no demuestra que esos números signifiquen algo: si dos parámetros se compensan, el ajuste elige uno cualquiera de infinitas combinaciones igual de buenas.

📘 **Dónde se aprende** (1 clase): [B22-C03 · Identificabilidad de parámetros](../programa/clases/B22/B22-C03-identificabilidad-de-parametros/CLASE.md).

### Identificable estructuralmente

- Un parámetro es identificable estructuralmente si datos perfectos (sin ruido) lo determinan;

🎯 **Por qué importa (clase B22-C03):** Un ajuste siempre devuelve números. Que el programa converja no demuestra que esos números signifiquen algo: si dos parámetros se compensan, el ajuste elige uno cualquiera de infinitas combinaciones igual de buenas.

📘 **Dónde se aprende** (1 clase): [B22-C03 · Identificabilidad de parámetros](../programa/clases/B22/B22-C03-identificabilidad-de-parametros/CLASE.md).

### Identificador

- Un identificador es el código único de un objeto en un catálogo.
- El identificador lo distingue.

💡 **Cómo se explica en la clase [B08-C06](../programa/clases/B08/B08-C06-constelaciones-y-catalogos-estelares/CLASE.md):**
- ⚠️ **Error frecuente:** Usar el nombre de una estrella como identificador único. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Dos personas dicen «la estrella roja de la Cruz del Sur» y creen hablar de lo mismo; un programa de telescopio pide «HIP 12345». Sin un lenguaje común no puedes repetir una observación ni compartirla.

📘 **Dónde se aprende** (2 clases): [B08-C06 · Constelaciones y catálogos estelares](../programa/clases/B08/B08-C06-constelaciones-y-catalogos-estelares/CLASE.md); [B28-C17 · Archivos de eventos multimensajero](../programa/clases/B28/B28-C17-archivos-de-eventos-multimensajero/CLASE.md).

### Identificador persistente

- Un identificador persistente es un código único y estable que permite volver a encontrar la obra; los principios FAIR piden que los datos y sus metadatos lo tengan (S5).
- Un identificador persistente (por ejemplo, un DOI) apunta siempre al mismo objeto.
- Un identificador persistente (DOI, número de preprint) permite volver a encontrar una obra o un conjunto de datos (S4).

💡 **Cómo se explica en la clase [B14-C19](../programa/clases/B14/B14-C19-publicacion-de-codigo-y-datos/CLASE.md):**
- En el ejemplo, el identificador está pendiente: no se acuñó ninguno, y F1 y F4 (identificador persistente y registro en un recurso de búsqueda) quedan sin cumplir.
- P --> I["identificador persistente<br/>¿cómo lo encuentro siempre?"]
- 🎯 **Por qué importa:** Subes tu código a un repositorio y tus datos a una carpeta compartida. Un año después, alguien quiere usarlos y no sabe si puede, cómo citarte, qué significan las columnas ni si el archivo es el que tú usaste.

📘 **Dónde se aprende** (3 clases): [B14-C19 · Publicación de código y datos](../programa/clases/B14/B14-C19-publicacion-de-codigo-y-datos/CLASE.md); [B20-C01 · Búsqueda bibliográfica sistemática y gestión de referencias](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md); [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md).

### Identificador SPDX

- Un identificador SPDX es el nombre corto estándar de una licencia.

💡 **Cómo se explica en la clase [B14-C19](../programa/clases/B14/B14-C19-publicacion-de-codigo-y-datos/CLASE.md):**
- Un nombre inventado («mi propia licencia») no es un identificador SPDX y la regla lo rechaza.
- 🎯 **Por qué importa:** Subes tu código a un repositorio y tus datos a una carpeta compartida. Un año después, alguien quiere usarlos y no sabe si puede, cómo citarte, qué significan las columnas ni si el archivo es el que tú usaste.

📘 **Dónde se aprende** (1 clase): [B14-C19 · Publicación de código y datos](../programa/clases/B14/B14-C19-publicacion-de-codigo-y-datos/CLASE.md).

### Identificador único

- Un identificador único (`id_obs`) distingue observaciones distintas con valores iguales.

🎯 **Por qué importa (clase B14-C08):** Una bitácora de observación real tiene errores: alguien escribió `-99` donde faltaba un dato, el mismo objeto aparece con tres grafías, una fila se copió dos veces, un valor tiene un dígito de más. Si calculas una media sin limpiar, el resultado es otro número.

📘 **Dónde se aprende** (1 clase): [B14-C08 · Pandas y limpieza de datos](../programa/clases/B14/B14-C08-pandas-y-limpieza-de-datos/CLASE.md).

### Idioma

- El idioma (`lang`) permite pronunciar bien.

💡 **Cómo se explica en la clase [B128-C04](../programa/clases/B128/B128-C04-documentos-y-contenidos-para-lectores-de-pantalla/CLASE.md):**
- Las siete reglas son del curso, inspiradas en el criterio 1.1.1 de WCAG 2.2 (contenido no textual con alternativa): idioma declarado, título, un solo `h1`, sin saltos de nivel, `alt` presente y no pobre, enlaces no genéricos y tablas con `th`.
- El idioma declarado hace que el lector use la pronunciación correcta.
- 🎯 **Por qué importa:** Una imagen sin texto alternativo, una tabla sin encabezados o un enlace «haz clic aquí» no se ven como problema a simple vista pero dejan a una persona sin la información. La decisión central: ¿qué comprobaciones mínimas puedo automatizar y qué debo revisar a mano?

📘 **Dónde se aprende** (1 clase): [B128-C04 · Documentos y contenidos para lectores de pantalla](../programa/clases/B128/B128-C04-documentos-y-contenidos-para-lectores-de-pantalla/CLASE.md).

### IE

- Los términos del modelo: IA y IE (ceros de acimut y altura), CA (colimación), NPAE (no perpendicularidad de ejes), AN y AW (inclinación del eje vertical al norte y al oeste) y TF (flexión del tubo).

🎯 **Por qué importa (clase B43-C26):** El modelo convierte errores de decenas de segundos de arco en residuos de segundos de arco. La decisión central: ¿qué términos incluir, cuántas estrellas medir y con qué incertidumbre se determina cada parámetro?

📘 **Dónde se aprende** (1 clase): [B43-C26 · Modelo de flexiones y de apuntado de una montura](../programa/clases/B43/B43-C26-modelo-de-flexiones-y-de-apuntado-de-una-montura/CLASE.md).

### IFOV

- El IFOV es el ángulo que subtiende un píxel visto desde el sensor.
- El IFOV es `atan(1/f)`.
- El IFOV es el ángulo que ve un píxel.

💡 **Cómo se explica en la clase [B57-C02](../programa/clases/B57/B57-C02-resolucion-espacial-y-temporal/CLASE.md):**
- Con `H = 705 km` y `GSD = 30 m`, `IFOV = 42,553 µrad`.
- *Descripción textual:* la altitud y el IFOV fijan el GSD; de él salen los píxeles por línea, el límite de Nyquist y el volumen, mientras el ciclo fija las imágenes por año.
- 🎯 **Por qué importa:** Un satélite con píxeles de 30 m no ve una casa y uno que vuelve cada 16 días no ve una tormenta. La decisión central: ¿qué tamaño de píxel, qué ancho de barrido y qué ciclo de repetición necesita el fenómeno que quiero estudiar?

📘 **Dónde se aprende** (3 clases): [B57-C02 · Resolución espacial y temporal](../programa/clases/B57/B57-C02-resolucion-espacial-y-temporal/CLASE.md); [B87-C07 · Rastreadores estelares](../programa/clases/B87/B87-C07-rastreadores-estelares/CLASE.md); [B121-C02 · Licenciamiento de actividades de teledetección](../programa/clases/B121/B121-C02-licenciamiento-de-actividades-de-teledeteccion/CLASE.md).

### IGRF

- El IGRF es el modelo estándar de grado 13 que se usaría en lugar del dipolo.

💡 **Cómo se explica en la clase [B87-C05](../programa/clases/B87/B87-C05-magnetometros/CLASE.md):**
- Y el IGRF (S1) del que saldría el campo de referencia tiene su propio error y se actualiza cada cinco años; aquí el modelo dipolar es sintético y el sensor ve exactamente ese modelo, por lo que no aparece error de modelo.
- IGRF de grado 13: el modelo de referencia real (consultado solo en su descripción).
- ⚠️ **Error frecuente:** Usar el dipolo como si fuese el IGRF. Declara qué modelo usas y su error (8.4)
- 🎯 **Por qué importa:** Un cubesat sin sensores estelares usa el campo magnético para saber hacia dónde apunta y para detumbling (C16). La decisión central: ¿cuánto varía el campo a lo largo de la órbita, cuánto ruido y sesgo tolera la dirección medida y qué parte de la actitud no ve el magnetómetro?

📘 **Dónde se aprende** (1 clase): [B87-C05 · Magnetómetros](../programa/clases/B87/B87-C05-magnetometros/CLASE.md).

### Igualdad materia–radiación

- La igualdad materia–radiación ocurre cuando `Ω_m(1+z)³ = Ω_r(1+z)⁴`.

🎯 **Por qué importa (clase B26-C14):** Casi todo lo observable del universo temprano (radiación de fondo, abundancia de helio) depende de su temperatura y de qué componente dominaba la densidad en cada época.

📘 **Dónde se aprende** (2 clases): [B26-C14 · Evolución térmica del universo](../programa/clases/B26/B26-C14-evolucion-termica-del-universo/CLASE.md); [B36-C07 · Oscilaciones acústicas bariónicas como regla estándar](../programa/clases/B36/B36-C07-oscilaciones-acusticas-barionicas-como-regla-estandar/CLASE.md).

### IIR

- Un filtro IIR (respuesta infinita) reutiliza salidas anteriores, como `y[n] = α x[n] + (1 − α) y[n − 1]` (S2 escribe la forma general).

💡 **Cómo se explica en la clase [B15-C07](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md):**
- Un IIR suele retrasar de forma desigual según la frecuencia pero necesita pocos coeficientes.
- 🎯 **Por qué importa:** Una curva de luz tiene una modulación lenta de la estrella (manchas que rotan) de 2000 partes por millón y, escondido en ella, el paso de un planeta que reduce el brillo 1000 ppm durante tres horas. Para ver el tránsito hay que quitar la modulación; pero si el filtro es demasiado agresivo, también se come parte del tránsito.

📘 **Dónde se aprende** (1 clase): [B15-C07 · Filtrado digital](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md).

### IK

- Los tipos descritos por NAIF son SPK (posición y velocidad), CK (orientación de nave), PCK (tamaño, forma y orientación de cuerpos), IK (campo de visión de instrumentos), FK (marcos), LSK (segundos intercalares), SCLK (reloj de nave) y DSK (formas).

🎯 **Por qué importa (clase B74-C21):** Un resultado de navegación depende de qué kernels se cargaron y en qué orden: dos corridas con el mismo código pueden dar trayectorias distintas. La decisión central: ¿cómo declaro, valido y audito el conjunto de kernels de una solución para que sea reproducible?

📘 **Dónde se aprende** (1 clase): [B74-C21 · Kernels SPICE y su uso en navegación](../programa/clases/B74/B74-C21-kernels-spice-y-su-uso-en-navegacion/CLASE.md).

### Ilmenita

- La ilmenita (FeTiO₃) es un óxido de hierro y titanio.

💡 **Cómo se explica en la clase [B59-C23](../programa/clases/B59/B59-C23-subproductos-y-flujos-residuales-de-procesos-isru/CLASE.md):**
- Con `10 %` de ilmenita en masa (sintética) hay que procesar `9,482/0,10 = 94,8 kg` de regolito y quedan `85,3 kg` de colas por kg de O.
- Límite: la ilmenita es un recurso modesto; la ley real depende del sitio y no se conoce aquí.
- ⚠️ **Error frecuente:** Dar la ley de ilmenita como real. Es sintética.
- 🎯 **Por qué importa:** Producir un kilogramo de oxígeno genera toneladas de otras cosas. La decisión central: ¿qué masa de residuo o de subproducto aparece por cada kilogramo de producto?

📘 **Dónde se aprende** (1 clase): [B59-C23 · Subproductos y flujos residuales de procesos ISRU](../programa/clases/B59/B59-C23-subproductos-y-flujos-residuales-de-procesos-isru/CLASE.md).

### Iluminación

- La iluminación es la distribución del campo en la apertura.

💡 **Cómo se explica en la clase [B46-C04](../programa/clases/B46/B46-C04-diagramas-de-radiacion/CLASE.md):**
- La iluminación uniforme reproduce los valores analíticos `0,886 λ/D` y `−13,26 dB`.
- *Descripción textual:* la iluminación se transforma en un patrón del que se miden ancho, lóbulo y eficiencia.
- 🎯 **Por qué importa:** Bajar los lóbulos laterales evita captar emisión de direcciones no deseadas, pero ensancha el haz y reduce la eficiencia. La decisión central: ¿qué iluminación equilibra resolución y rechazo de lóbulos?

📘 **Dónde se aprende** (1 clase): [B46-C04 · Diagramas de radiación](../programa/clases/B46/B46-C04-diagramas-de-radiacion/CLASE.md).

### Ilustrativo

- La función inicial de masa `dN/dM ∝ M^{−α}` da el reparto de masas al nacer; la pendiente `α` es aquí `2,3`, un parámetro ilustrativo (Kroupa señala cambios de pendiente hacia `0,5` y `0,08 M☉`, S3).

🎯 **Por qué importa (clase B24-C19):** La edad de una estrella aislada es difícil de medir; la de un cúmulo se puede leer en su diagrama HR, porque las estrellas más masivas ya han salido de la secuencia principal y el «punto de desvío» marca la edad. Esas edades fijan la cronología de la Galaxia y calibran los modelos.

📘 **Dónde se aprende** (1 clase): [B24-C19 · Cúmulos y edades estelares](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md).

### Imagen

- Una imagen es el paquete inmutable; un contenedor es una instancia en ejecución de una imagen.
- La imagen es la otra frecuencia que cae en la FI.
- Una imagen con `θ < 0` queda al otro lado de la lente (paridad invertida).

💡 **Cómo se explica en la clase [B14-C17](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md):**
- Reproduce el sistema de archivos y la configuración de la imagen: sistema base, bibliotecas, paquetes, código.
- El laboratorio aplica seis reglas, convenciones de esta clase: imagen base con versión fija (no `latest` ni sin etiqueta);
- ⚠️ **Error frecuente:** Meter datos en la imagen. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Tu análisis funciona con el bloqueo de C12 en tu equipo, pero en el servidor del laboratorio falla porque falta una biblioteca del sistema. La pregunta motivadora es: ¿cómo entrego el análisis junto con todo lo que necesita para correr, de modo que otra persona lo ejecute igual?

📘 **Dónde se aprende** (3 clases): [B14-C17 · Contenedores y ambientes científicos](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md); [B25-C14 · Lentes gravitacionales galácticas](../programa/clases/B25/B25-C14-lentes-gravitacionales-galacticas/CLASE.md); [B49-C11 · Mezcladores de frecuencia: pérdida de conversión y productos espurios](../programa/clases/B49/B49-C11-mezcladores-de-frecuencia-perdida-de-conversion-y-productos-espurios/CLASE.md).

### Imagen base

- La imagen base es la que se declara con `FROM`.

💡 **Cómo se explica en la clase [B14-C17](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md):**
- El laboratorio aplica seis reglas, convenciones de esta clase: imagen base con versión fija (no `latest` ni sin etiqueta);
- *Descripción textual:* una pila de capas, de arriba abajo: imagen base, directorio de trabajo, copia de los archivos de bloqueo, instalación de paquetes (la capa lenta), copia del script de análisis y, por último, usuario y orden de arranque.
- 🎯 **Por qué importa:** Tu análisis funciona con el bloqueo de C12 en tu equipo, pero en el servidor del laboratorio falla porque falta una biblioteca del sistema. La pregunta motivadora es: ¿cómo entrego el análisis junto con todo lo que necesita para correr, de modo que otra persona lo ejecute igual?

📘 **Dónde se aprende** (1 clase): [B14-C17 · Contenedores y ambientes científicos](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md).

### Imagen de diferencia

- La imagen de diferencia resulta de restarla de cada imagen.

💡 **Cómo se explica en la clase [B15-C20](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md):**
- Se correlaciona la imagen de diferencia con la PSF y se estima `σ_T` con la mediana de las desviaciones absolutas (C12, 8.1): `0,94 ADU` (teoría `σ√Σp² · 1,06 = 1,00`).
- 🎯 **Por qué importa:** Detectar y seguir un objeto móvil —un asteroide, un fragmento de basura espacial, un satélite— combina varios problemas: la cámara no apunta exactamente igual en cada imagen, las estrellas fijas saturan la escena, el objeto es débil y la medida es ruidosa.

📘 **Dónde se aprende** (1 clase): [B15-C20 · Proyecto de detección y seguimiento](../programa/clases/B15/B15-C20-proyecto-de-deteccion-y-seguimiento/CLASE.md).

### Imagen digital

- Una imagen digital es una matriz `I[y, x]`: `y` indexa filas (hacia abajo en la mayoría de los programas) y `x` columnas.

🎯 **Por qué importa (clase B15-C09):** Una cámara de un telescopio no mide «luz de estrellas»: mide un número por píxel que incluye un desplazamiento electrónico, corriente de oscuridad, el cielo, la estrella y una sensibilidad que cambia de un píxel a otro. Si analizas el número crudo, mides la cámara, no el cielo.

📘 **Dónde se aprende** (1 clase): [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md).

### Imagen real

- La imagen real y la virtual.

💡 **Cómo se explica en la clase [B41-C06](../programa/clases/B41/B41-C06-distancias-focales-y-formacion-de-imagen/CLASE.md):**
- Con `f = 200 mm` y un objeto de 10 mm a `s = 600 mm`, la imagen real está a `300 mm` con `m = −0,5` (altura `−5 mm`); a `s = 100 mm` la imagen es virtual, a `−200 mm`, con `m = +2`.
- El producto de las distancias al foco es constante y define imagen real o virtual.
- 🎯 **Por qué importa:** El foco de una cámara o de un telescopio decide el tamaño de la imagen. La decisión central: ¿dónde cae la imagen y de qué tamaño es?

📘 **Dónde se aprende** (1 clase): [B41-C06 · Distancias focales y formación de imagen](../programa/clases/B41/B41-C06-distancias-focales-y-formacion-de-imagen/CLASE.md).

### Imagen sucia

- La imagen sucia y el haz sucio.

💡 **Cómo se explica en la clase [B46-C19](../programa/clases/B46/B46-C19-imagenes-de-radio-y-clean/CLASE.md):**
- La imagen sucia calculada desde las visibilidades coincide con la suma de haces desplazados: diferencia máxima `1,4 × 10^-16 Jy/haz`.
- El pico de la imagen sucia es `0,984 Jy/haz`.
- 🎯 **Por qué importa:** La imagen sucia no se puede interpretar por los lóbulos del haz. La decisión central: ¿cuándo detener la deconvolución para no ajustar ruido?

📘 **Dónde se aprende** (2 clases): [B46-C19 · Imágenes de radio y CLEAN](../programa/clases/B46/B46-C19-imagenes-de-radio-y-clean/CLASE.md); [B51-C06 · Autocalibración iterativa con modelo de cielo](../programa/clases/B51/B51-C06-autocalibracion-iterativa-con-modelo-de-cielo/CLASE.md).

### Imagen virtual

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C03](../programa/clases/B41/B41-C03-reflexion-y-espejos-planos/CLASE.md):**
- Los rayos reflejados, prolongados hacia atrás, se cortan en `(−0,500000 ; 0,200000) m`: la imagen virtual está a la misma distancia detrás del espejo y a la misma altura.
- R["d' = d - 2 (d.n) n"] --> I["imagen virtual"]
- 🎯 **Por qué importa:** Los espejos planos pliegan el haz de un telescopio y de un periscopio. La decisión central: ¿dónde está la imagen y cuánto gira el haz cuando se mueve el espejo?

📘 **Dónde se aprende** (1 clase): [B41-C03 · Reflexión y espejos planos](../programa/clases/B41/B41-C03-reflexion-y-espejos-planos/CLASE.md).

### IMF

- La IMF `ξ(m) = dN/dm`.

💡 **Cómo se explica en la clase [B38-C02](../programa/clases/B38/B38-C02-funcion-inicial-de-masa-y-su-universalidad/CLASE.md):**
- Un cúmulo de 50 estrellas por encima de 1 M☉ da una pendiente con ±0,18 solo por azar: diferencias de ese tamaño entre cúmulos no prueban una IMF distinta.
- Límite: la misma IMF para todas las muestras y estrellas independientes.
- 🎯 **Por qué importa:** Casi todo lo que se infiere de una población (luminosidad, supernovas, masa) depende de la IMF. La decisión central: ¿cuándo una diferencia de pendiente entre dos muestras es real y cuándo es ruido de Poisson?

📘 **Dónde se aprende** (1 clase): [B38-C02 · Función inicial de masa y su universalidad](../programa/clases/B38/B38-C02-funcion-inicial-de-masa-y-su-universalidad/CLASE.md).

### IMF universal

- Una IMF universal es la misma en todos los entornos.

🎯 **Por qué importa (clase B38-C02):** Casi todo lo que se infiere de una población (luminosidad, supernovas, masa) depende de la IMF. La decisión central: ¿cuándo una diferencia de pendiente entre dos muestras es real y cuándo es ruido de Poisson?

📘 **Dónde se aprende** (1 clase): [B38-C02 · Función inicial de masa y su universalidad](../programa/clases/B38/B38-C02-funcion-inicial-de-masa-y-su-universalidad/CLASE.md).

### Imitación

- La imitación es adoptar porque otros adoptan.

💡 **Cómo se explica en la clase [B119-C31](../programa/clases/B119/B119-C31-practica-estatal-y-costumbre-internacional-en-el-derecho-espacial/CLASE.md):**
- Con imitación débil (`β = 0,05`) se tardan `50` años; con fuerte (`β = 0,40`), `13`.
- *Descripción textual:* la adopción espontánea y la imitación hacen crecer la fracción de adoptantes hasta cruzar un umbral ilustrativo de generalidad.
- 🎯 **Por qué importa:** B119 presenta los tratados; no enseña la costumbre ni la práctica estatal, que complementan a los tratados en un campo donde los Estados no son partes de todos ellos. La decisión central: ¿qué factores aceleran o frenan que una práctica se vuelva general?

📘 **Dónde se aprende** (1 clase): [B119-C31 · Práctica estatal y costumbre internacional en el derecho espacial](../programa/clases/B119/B119-C31-practica-estatal-y-costumbre-internacional-en-el-derecho-espacial/CLASE.md).

### IMM

- El IMM es el modelo probabilístico de riesgo médico de la NASA.

🎯 **Por qué importa (clase B117-C05):** Ninguna clase anterior trata el equipo médico de a bordo. La decisión central: ¿qué embarcar bajo un límite de masa y volumen y qué riesgo de quedarse sin él se acepta?

📘 **Dónde se aprende** (1 clase): [B117-C05 · Inventario y gestión del equipo médico a bordo](../programa/clases/B117/B117-C05-inventario-y-gestion-del-equipo-medico-a-bordo/CLASE.md).

### Impacta

- Un punto con `r_p` menor que el radio impacta.

🎯 **Por qué importa (clase B75-C24):** Los equipos de navegación expresan los errores de llegada en el plano B. La decisión central: ¿en qué punto del plano B hay que apuntar para obtener una distancia de periapsis y un plano de sobrevuelo dados, y qué pasa si el punto cae dentro del planeta?

📘 **Dónde se aprende** (1 clase): [B75-C24 · Plano B y parámetro de impacto](../programa/clases/B75/B75-C24-plano-b-y-parametro-de-impacto/CLASE.md).

### Impacto

- Un impacto es la detección de una partícula.
- Una traza es el camino de una partícula; el impacto es la travesía de un núcleo por una traza.

💡 **Cómo se explica en la clase [B31-C01](../programa/clases/B31/B31-C01-dualidad-onda-particula/CLASE.md):**
- Un solo impacto no revela nada; el patrón surge de miles.
- ⚠️ **Error frecuente:** Pensar que un impacto muestra la onda. Se corrige con 8.4.
- 🎯 **Por qué importa:** Sin la dualidad no se entiende la difracción de electrones, los microscopios electrónicos ni la estructura atómica. La decisión central: ¿cuándo importa la longitud de onda de un objeto y cómo se ve en un experimento?

📘 **Dónde se aprende** (2 clases): [B31-C01 · Dualidad onda-partícula](../programa/clases/B31/B31-C01-dualidad-onda-particula/CLASE.md); [B112-C01 · Magnitudes dosimétricas: dosis absorbida, LET y eficacia biológica](../programa/clases/B112/B112-C01-magnitudes-dosimetricas-dosis-absorbida-let-y-eficacia-biologica/CLASE.md).

### Impactor cinético

- Un impactor cinético transfiere momento por colisión.

🎯 **Por qué importa (clase B58-C17):** Lo que importa no es el tamaño del empuje sino cuándo se da: el desplazamiento crece con el tiempo de aviso. La decisión central: ¿qué `Δv` y cuántos años de aviso se necesitan para mover un objeto lo suficiente?

📘 **Dónde se aprende** (1 clase): [B58-C17 · Principios de mitigación y desviación](../programa/clases/B58/B58-C17-principios-de-mitigacion-y-desviacion/CLASE.md).

### Impedancia

- La impedancia es `ρ₀(C + s up)`.
- Impedancia: relación entre el movimiento y la fuerza.

💡 **Cómo se explica en la clase [B101-C07](../programa/clases/B101/B101-C07-control-de-fuerza-e-impedancia-en-manipulacion/CLASE.md):**
- La teoría de impedancia (N4) es estándar y se verifica con las soluciones analíticas del laboratorio.
- Impedancia (esta clase): se regula la relación movimiento–fuerza.
- 🎯 **Por qué importa:** Si un brazo muy rígido empuja una pieza que está 5 mm más lejos de lo que cree, aplica una fuerza grande. La decisión central: ¿qué rigidez y qué amortiguamiento le doy al extremo para que el contacto sea suave y la fuerza predecible?

📘 **Dónde se aprende** (2 clases): [B61-C05 · Fusión por impacto y metamorfismo de choque](../programa/clases/B61/B61-C05-fusion-por-impacto-y-metamorfismo-de-choque/CLASE.md); [B101-C07 · Control de fuerza e impedancia en manipulación](../programa/clases/B101/B101-C07-control-de-fuerza-e-impedancia-en-manipulacion/CLASE.md).

### Impedancia característica

- La impedancia característica `Z0` y la velocidad de fase `v = c/√ε_eff` salen de ella.

🎯 **Por qué importa (clase B93-C01):** El tronco no trataba el diseño de placas: B90 integra y B86 trata potencia, pero nadie calculaba una pista. La decisión central: ¿qué ancho de cobre y qué geometría de microtira necesita una placa para llevar una corriente y una señal dadas, y qué margen queda?

📘 **Dónde se aprende** (1 clase): [B93-C01 · Diseño de PCB espacial (conceptual)](../programa/clases/B93/B93-C01-diseno-de-pcb-espacial-conceptual/CLASE.md).

### Impedancia de superficie

- La impedancia de superficie `Z = √(iωμ₀/σ)`.

🎯 **Por qué importa (clase B33-C06):** El campo eléctrico depende de la conductividad y de la frecuencia. La decisión central: ¿cuánto vale el campo geoeléctrico y la corriente en una línea para un campo magnético dado?

📘 **Dónde se aprende** (1 clase): [B33-C06 · Corrientes geomagnéticas inducidas (GIC)](../programa/clases/B33/B33-C06-corrientes-geomagneticas-inducidas-gic/CLASE.md).

### Impedancia del vacío

- La impedancia del vacío `Z₀ = √(μ₀/ε₀)`.

🎯 **Por qué importa (clase B42-C01):** Sin una descripción ondulatoria no hay fase, y sin fase no hay difracción, interferencia ni óptica adaptativa. La decisión central: ¿qué parte de la luz se puede tratar como una onda escalar con amplitud y fase y qué parte exige el campo vectorial completo?

📘 **Dónde se aprende** (1 clase): [B42-C01 · Ecuaciones de onda electromagnética](../programa/clases/B42/B42-C01-ecuaciones-de-onda-electromagnetica/CLASE.md).

### Imperfección

- La imperfección es `I = (d25 − d75)/(2 d50)`.

🎯 **Por qué importa (clase B59-C22):** Calentar o reducir todo el regolito es caro; separar la fracción rica antes ahorra energía. La decisión central: ¿qué tamaño de corte equilibra la ley del concentrado y la recuperación del mineral?

📘 **Dónde se aprende** (1 clase): [B59-C22 · Beneficio y separación granulométrica de regolito](../programa/clases/B59/B59-C22-beneficio-y-separacion-granulometrica-de-regolito/CLASE.md).

### Implementación bajo prueba

- La implementación bajo prueba (IUT) es lo que se verifica.

🎯 **Por qué importa (clase B94-C06):** Una implementación que «funciona con la mía» puede fallar con otra. La decisión central: ¿qué pruebas demuestran que cada requisito se cumple y cómo sabes que tu suite detectaría un defecto?

📘 **Dónde se aprende** (1 clase): [B94-C06 · Validación y conformidad de protocolos de enlace](../programa/clases/B94/B94-C06-validacion-y-conformidad-de-protocolos-de-enlace/CLASE.md).

### Implícita

- La probabilidad implícita es la que tiene el diseño si resistencia y carga siguen los modelos supuestos.
- Una relación explícita da `y` en función de `x`; una implícita la define mediante `F(x, y) = 0` (S1, §1.5(i)).

💡 **Cómo se explica en la clase [B09-C06](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md):**
- B -->|"M = E − e sin E<br/>(implícita)"| C["E"]
- *Descripción textual:* el tiempo determina la anomalía media; esta, mediante la ecuación implícita, determina la anomalía excéntrica; esta, la posición.
- 🎯 **Por qué importa:** Para saber dónde está un planeta en su órbita en un instante dado hay que resolver la ecuación de Kepler, `M = E − e sin E`, que no tiene solución en funciones elementales: no se puede despejar `E`.

📘 **Dónde se aprende** (2 clases): [B09-C06 · Derivación implícita](../programa/clases/B09/B09-C06-derivacion-implicita/CLASE.md); [B84-C24 · Factores de seguridad y márgenes estructurales](../programa/clases/B84/B84-C24-factores-de-seguridad-y-margenes-estructurales/CLASE.md).

### Implícito

- Un método implícito define el nuevo estado mediante una ecuación que lo contiene;
- El método explícito calcula el paso nuevo solo con el estado actual; el implícito resuelve una ecuación en el estado nuevo.

💡 **Cómo se explica en la clase [B11-C09](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md):**
- E --> G["Reducir h o usar<br/>método implícito"]
- *Descripción textual:* la ecuación de prueba reduce cada paso a una multiplicación por `R(hλ)`; si su módulo es menor o igual que uno el método es estable y se pasa a comprobar la precisión; si no, hay que reducir el paso o cambiar a un método implícito.
- 🎯 **Por qué importa:** Un modelo térmico de una nave tiene constantes de tiempo que van de segundos (un sensor fino) a horas (un tanque grande). Un método explícito debe usar un paso comparable al más rápido aunque lo único que interese sea lo lento: pagar por una escala que no se observa.

📘 **Dónde se aprende** (3 clases): [B11-C09 · Análisis de estabilidad numérica](../programa/clases/B11/B11-C09-analisis-de-estabilidad-numerica/CLASE.md); [B11-C22 · Métodos implícitos y sistemas rígidos](../programa/clases/B11/B11-C22-metodos-implicitos-y-sistemas-rigidos/CLASE.md); [B60-C03 · Integración numérica de redes químicas rígidas](../programa/clases/B60/B60-C03-integracion-numerica-de-redes-quimicas-rigidas/CLASE.md).

### Importancia de Birnbaum

- La importancia de Birnbaum `I_k = P(tope | k falla) − P(tope | k no falla)`.

🎯 **Por qué importa (clase B88-C16):** Una nave tolera fallos si ninguno solo provoca la pérdida y las combinaciones peligrosas son improbables. La decisión central: ¿qué combinaciones mínimas de fallos causan la pérdida y cuál elemento merece más protección?

📘 **Dónde se aprende** (1 clase): [B88-C16 · Ingeniería de seguridad funcional](../programa/clases/B88/B88-C16-ingenieria-de-seguridad-funcional/CLASE.md).

### Importancia por permutación

- La importancia por permutación de la variable `j` es `s − s̃ⱼ`, donde `s` es el desempeño del modelo en datos de referencia y `s̃ⱼ` el promedio del desempeño tras permutar la columna `j` varias veces (S1).

💡 **Cómo se explica en la clase [B17-C08](../programa/clases/B17/B17-C08-interpretabilidad-con-consistencia-fisica/CLASE.md):**
- A["Modelo entrenado"] --> B["¿De qué depende?<br/>Importancia por permutación"]
- *Descripción textual:* un modelo entrenado se somete a dos revisiones paralelas: la importancia por permutación (de qué depende, con atención a variables espurias y duplicadas) y la consistencia física (exponentes, monotonía y extrapolación).
- 🎯 **Por qué importa:** Dos modelos pueden tener el mismo error en validación y haber aprendido cosas muy distintas: uno la ley física, otro un atajo que funciona en el rango visto. Si solo miras la métrica, no los distingues, y el atajo falla al primer dato fuera de rango.

📘 **Dónde se aprende** (1 clase): [B17-C08 · Interpretabilidad con consistencia física](../programa/clases/B17/B17-C08-interpretabilidad-con-consistencia-fisica/CLASE.md).

### Impropio

- Un prior impropio no integra 1 (por ejemplo, el plano en `λ > 0`); sirve si la posterior sí es propia.

💡 **Cómo se explica en la clase [B19-C01](../programa/clases/B19/B19-C01-priors-fisicamente-informados/CLASE.md):**
- El prior plano en `λ` corresponde a Gamma(1, 0) (impropio).
- Uno de Jeffreys es invariante a la reparametrización, pero no codifica escala física y puede ser impropio.
- 🎯 **Por qué importa:** Un contador de partículas a bordo de un CubeSat registra 3 eventos en 1 hora. ¿Cuál es la tasa verdadera `λ`, en eventos por hora?

📘 **Dónde se aprende** (1 clase): [B19-C01 · Priors físicamente informados](../programa/clases/B19/B19-C01-priors-fisicamente-informados/CLASE.md).

### Impulso

- El impulso de una fuerza es `J = ∫ F dt` (o `F Δt` si `F` es constante), en `N·s`;
- Un impulso es un cambio de velocidad `Δv` que se supone instantáneo.
- El impulso discreto `δ[n]` vale 1 en `n = 0` y 0 en los demás.

💡 **Cómo se explica en la clase [B05-C08](../programa/clases/B05/B05-C08-momento-lineal-e-impulsos/CLASE.md):**
- El lado izquierdo es el impulso: una fuerza pequeña durante mucho tiempo da el mismo cambio de momento que una grande durante poco.
- Paso 3 · Impulso. `J = F Δt = 50 × 120 = 6000 N·s`; con `m = 1000 kg`, `Δv = J/m = 6,0 m/s`.
- 🎯 **Por qué importa:** Un cohete en el vacío no tiene nada contra lo que empujar y aun así acelera. La pregunta motivadora es: ¿cómo cambia la velocidad de un cuerpo cuando expulsa masa o cuando choca, si no hay fuerzas externas?

📘 **Dónde se aprende** (4 clases): [B05-C08 · Momento lineal e impulsos](../programa/clases/B05/B05-C08-momento-lineal-e-impulsos/CLASE.md); [B05-C20 · Problema físico integrado de satélite ideal](../programa/clases/B05/B05-C20-problema-fisico-integrado-de-satelite-ideal/CLASE.md); [B15-C08 · Convolución y respuesta impulsional](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md); [B106-C16 · Ergonomía en microgravedad](../programa/clases/B106/B106-C16-ergonomia-en-microgravedad/CLASE.md).

### Impulso combinado

- El impulso combinado cambia módulo y dirección a la vez.

🎯 **Por qué importa (clase B71-C19):** Un cambio de plano mal ubicado puede costar más que todo el resto de la misión orbital. La decisión central: ¿dónde y cómo conviene cambiar el plano para gastar el mínimo `Δv`?

📘 **Dónde se aprende** (1 clase): [B71-C19 · Cambios de plano simples](../programa/clases/B71/B71-C19-cambios-de-plano-simples/CLASE.md).

### Impulso específico

- El impulso específico `I_sp` mide la eficiencia del propulsor, en segundos.
- El impulso específico `Isp = I/(m_p g₀)` mide la eficiencia del propelente.
- El impulso específico `Isp = F/(ṁ g₀)` se mide en segundos y compara motores por el empuje obtenido por cada newton de propelente consumido por segundo.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B78-C01](../programa/clases/B78/B78-C01-empuje-e-impulso-especifico/CLASE.md):**
- Paso 3 · Impulso específico. `Isp = 28 000/9,80665 = 2855,2 s`.
- ⚠️ **Error frecuente:** Confundir empuje con impulso específico. Se corrige con 8.2.
- 🎯 **Por qué importa:** Dos motores con el mismo empuje pueden gastar propelente a ritmos muy distintos, y dos con el mismo consumo pueden empujar muy distinto según la presión ambiente. La decisión central: ¿qué mide el impulso específico, qué no mide, y por qué el mismo motor tiene un `Isp` distinto en el mar y en el vacío?

📖 **Explicado a fondo:** [Impulso específico (Isp)](esencial/esencial-d-l.md#impulso-específico-isp) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (5 clases): [B05-C20 · Problema físico integrado de satélite ideal](../programa/clases/B05/B05-C20-problema-fisico-integrado-de-satelite-ideal/CLASE.md); [B75-C09 · Presupuestos de delta-v](../programa/clases/B75/B75-C09-presupuestos-de-delta-v/CLASE.md); [B77-C06 · Relación masa-impulso](../programa/clases/B77/B77-C06-relacion-masa-impulso/CLASE.md); [B78-C01 · Empuje e impulso específico](../programa/clases/B78/B78-C01-empuje-e-impulso-especifico/CLASE.md); [B87-C13 · Propulsores de control de actitud](../programa/clases/B87/B87-C13-propulsores-de-control-de-actitud/CLASE.md).

### Impulso mínimo

- El impulso mínimo (*minimum impulse bit*) es `F t_min`.

🎯 **Por qué importa (clase B87-C13):** Los propulsores son el actuador de más par y de respuesta rápida, y el único que cambia el momento total del satélite, pero cada pulso gasta masa que no vuelve. La decisión central: ¿cuánto propergol cuesta una maniobra o un año de mantenimiento de actitud, y qué precisión permite el impulso mínimo?

📘 **Dónde se aprende** (1 clase): [B87-C13 · Propulsores de control de actitud](../programa/clases/B87/B87-C13-propulsores-de-control-de-actitud/CLASE.md).

### Impulso tangente

- Un impulso tangente cambia el módulo de la velocidad sin girarla.

🎯 **Por qué importa (clase B71-C18):** La Hohmann es la referencia de costo para cualquier cambio de órbita coplanar. La decisión central: ¿cuánto `Δv` y cuánto tiempo cuesta pasar de una circular a otra y cuándo conviene otra estrategia?

📘 **Dónde se aprende** (1 clase): [B71-C18 · Maniobra de Hohmann](../programa/clases/B71/B71-C18-maniobra-de-hohmann/CLASE.md).

### Impulso total

- El impulso total es `I = ∫F dt = m_p·Isp·g₀`.
- El impulso total `I = ∫F dt` se mide en N·s.
- El impulso total `I` es el empuje por el tiempo.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B78-C01](../programa/clases/B78/B78-C01-empuje-e-impulso-especifico/CLASE.md):**
- Con una rampa de empuje del 50 % al 100 % en `120 s`, el impulso total es `0,75 × 420 kN × 120 s = 37,8 MN·s`; la regla del trapecio coincide con la fórmula analítica.
- *Descripción textual:* el caudal, la velocidad de escape y el término de presión dan el empuje; el empuje entre el caudal da la velocidad equivalente, que dividida por `g₀` es el `Isp`; la integral del empuje es el impulso total.
- 🎯 **Por qué importa:** Dos motores con el mismo empuje pueden gastar propelente a ritmos muy distintos, y dos con el mismo consumo pueden empujar muy distinto según la presión ambiente. La decisión central: ¿qué mide el impulso específico, qué no mide, y por qué el mismo motor tiene un `Isp` distinto en el mar y en el vacío?

📘 **Dónde se aprende** (6 clases): [B77-C06 · Relación masa-impulso](../programa/clases/B77/B77-C06-relacion-masa-impulso/CLASE.md); [B78-C01 · Empuje e impulso específico](../programa/clases/B78/B78-C01-empuje-e-impulso-especifico/CLASE.md); [B78-C10 · Propulsión de gas frío](../programa/clases/B78/B78-C10-propulsion-de-gas-frio/CLASE.md); [B78-C11 · Micropropulsión para CubeSat](../programa/clases/B78/B78-C11-micropropulsion-para-cubesat/CLASE.md); [B78-C21 · Erosión y vida útil de propulsores eléctricos](../programa/clases/B78/B78-C21-erosion-y-vida-util-de-propulsores-electricos/CLASE.md); [B119-C24 · Límites legales y de seguridad de la experimentación educativa](../programa/clases/B119/B119-C24-limites-legales-y-de-seguridad-de-la-experimentacion-educativa/CLASE.md).

### IMRaD

- Su estructura habitual se abrevia IMRaD: Introducción, Métodos, Resultados y Discusión (S1).

🎯 **Por qué importa (clase B20-C04):** Un resultado correcto mal comunicado se pierde: nadie sabe qué se midió, con qué incertidumbre ni qué supuestos hay detrás, y no puede reproducirse ni usarse.

📘 **Dónde se aprende** (1 clase): [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md).

### I/N

- Piso de ruido: `k T B`. I/N: relación interferencia a ruido.

💡 **Cómo se explica en la clase [B90-C14](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md):**
- Con `I/N = −6 dB` la degradación es de solo 1 dB; con `I/N = 0 dB`, 3 dB.
- Para `I/N = −6 dB`, `I ≤ N − 6 = −137,6 dBm`, así que hacen falta `−30 − (−137,6) = 107,6 dB`.
- 🎯 **Por qué importa:** Un transmisor de 1 W deja un armónico de −30 dBm; el piso de ruido de un receptor estrecho está cerca de −132 dBm. La diferencia de más de 100 dB se pierde con facilidad en un chasis de 10 cm.

📘 **Dónde se aprende** (1 clase): [B90-C14 · Interferencias electromagnéticas EMI](../programa/clases/B90/B90-C14-interferencias-electromagneticas-emi/CLASE.md).

### Inanición

- La inanición es la espera indefinida de una clase.

💡 **Cómo se explica en la clase [B94-C05](../programa/clases/B94/B94-C05-calidad-de-servicio-y-prioridades-en-redes-espaciales/CLASE.md):**
- La carga E + N (36 MB) supera los 30 MB del contacto, y la prioridad estricta no deja nada a B: inanición total.
- 🎯 **Por qué importa:** Si la demanda supera a la capacidad, alguien espera. La decisión central: ¿qué política de cola garantiza lo urgente sin dejar sin servicio a las demás clases, y a qué coste?

📘 **Dónde se aprende** (1 clase): [B94-C05 · Calidad de servicio y prioridades en redes espaciales](../programa/clases/B94/B94-C05-calidad-de-servicio-y-prioridades-en-redes-espaciales/CLASE.md).

### Incertidumbre

- Y la incertidumbre es la forma honesta de decir cuánto conocemos un valor: un intervalo asociado a la medida, no un defecto de la medida.
- La incertidumbre es la estimación de qué tan lejos puede estar el valor medido del verdadero.
- Un error de redondeo es la diferencia entre el número y su redondeo. Incertidumbre es la duda sobre el valor; el SI y la guía de la metrología recomiendan reportarla con a lo sumo dos cifras significativas (S2).
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C01](../programa/clases/B01/B01-C01-naturaleza-del-universo/CLASE.md):**
- El análisis completo de Planck publica 13,797 ± 0,023 Gyr (fuente S1, Tabla 1): nuestro cálculo simplificado coincide con él dentro de esa incertidumbre.
- Cada resultado depende de datos con incertidumbre, y esa incertidumbre se traslada al resultado.
- ⚠️ **Error frecuente:** Dar una cifra sin unidad ni incertidumbre. Se copia de un titular tal cual.
- 🎯 **Por qué importa:** Seguramente has leído que «el universo tiene 13 800 millones de años» o que «el universo observable mide 93 000 millones de años luz». Son frases que se repiten con total seguridad.

📘 **Dónde se aprende** (7 clases): [B01-C01 · Naturaleza del universo](../programa/clases/B01/B01-C01-naturaleza-del-universo/CLASE.md); [B01-C18 · Incertidumbre y errores elementales](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md); [B03-C11 · Estimación y redondeo responsable](../programa/clases/B03/B03-C11-estimacion-y-redondeo-responsable/CLASE.md); [B20-C04 · Redacción de un artículo científico](../programa/clases/B20/B20-C04-redaccion-de-un-articulo-cientifico/CLASE.md); [B31-C04 · Principio de incertidumbre](../programa/clases/B31/B31-C04-principio-de-incertidumbre/CLASE.md); [B71-C02 · Ley de gravitación universal](../programa/clases/B71/B71-C02-ley-de-gravitacion-universal/CLASE.md) y 1 más.

### Incertidumbre a lo largo de la traza

- La incertidumbre a lo largo de la traza (*along-track*) crece más que la transversal porque un error en el periodo se acumula con el tiempo.
- La incertidumbre a lo largo de la traza domina porque un error en el semieje cambia el periodo.

💡 **Cómo se explica en la clase [B118-C08](../programa/clases/B118/B118-C08-propagacion-de-incertidumbre-en-conjunciones/CLASE.md):**
- El ejemplo conductor es un objeto sintético con `σ_s0 = 0,1 km` y `σ_a = 0,02 km` cuya incertidumbre a lo largo de la traza pasa de 0,1 a unos 20 km en una semana.
- 🎯 **Por qué importa:** La `Pc` de B118-C06 depende de la covarianza en el TCA, que sale de propagar la incertidumbre hasta ese instante. La decisión central: ¿hasta cuándo es válida una covarianza lineal y cuándo hay que propagar muestras?

📘 **Dónde se aprende** (2 clases): [B58-C08 · Propagación de incertidumbre orbital](../programa/clases/B58/B58-C08-propagacion-de-incertidumbre-orbital/CLASE.md); [B118-C08 · Propagación de incertidumbre en conjunciones](../programa/clases/B118/B118-C08-propagacion-de-incertidumbre-en-conjunciones/CLASE.md).

### Incertidumbre angular

- La incertidumbre angular `σθ` es la desviación típica de la medida de cada ángulo.

🎯 **Por qué importa (clase B04-C20):** Las distancias a las estrellas más cercanas se obtienen con un triángulo (el paralaje de C07): la base es la órbita de la Tierra y el ángulo es lo que cambia la dirección de la estrella.

📘 **Dónde se aprende** (1 clase): [B04-C20 · Triangulación espacial aplicada](../programa/clases/B04/B04-C20-triangulacion-espacial-aplicada/CLASE.md).

### Incertidumbre combinada

- La incertidumbre combinada de una función es la combinación de las `u` de sus datos (S2, apdo. 5.1.2).
- La incertidumbre combinada `u_c(y)` es la raíz cuadrada de `Σ c_i² u²(x_i)` cuando las entradas son independientes (S1, 2.3.4 y 5.1.2).
- La incertidumbre combinada de errores independientes es la raíz de la suma de sus cuadrados.
- *(y 5 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C16](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md):**
- Su signo puede aumentar o disminuir la incertidumbre combinada (C05).
- 🎯 **Por qué importa:** Casi todo resultado en ciencias espaciales es una función de medidas: una velocidad a partir de un radio, una distancia a partir de una paralaje, una masa a partir de un período. Dar el valor sin su incertidumbre no permite comparar con otros resultados ni decidir si cumple un requisito.

📘 **Dónde se aprende** (8 clases): [B01-C18 · Incertidumbre y errores elementales](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md); [B03-C19 · Propagación elemental de redondeos](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md); [B12-C16 · Propagación de incertidumbre](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md); [B13-C13 · Presupuestos de incertidumbre](../programa/clases/B13/B13-C13-presupuestos-de-incertidumbre/CLASE.md); [B57-C32 · Sitios de calibración terrestres](../programa/clases/B57/B57-C32-sitios-de-calibracion-terrestres/CLASE.md); [B91-C05 · Medición y calibración de antenas](../programa/clases/B91/B91-C05-medicion-y-calibracion-de-antenas/CLASE.md) y 2 más.

### Incertidumbre de la cámara

- La incertidumbre de la cámara es `σ_r/r = σ_p/p`, con `p = f L/(r · pix)` píxeles.

🎯 **Por qué importa (clase B76-C13):** Un sensor que funciona a diez metros puede ser inútil a quinientos. La decisión central: ¿a qué distancia conviene cada sensor y cuánto mejora combinarlos?

📘 **Dónde se aprende** (1 clase): [B76-C13 · Sensores de proximidad](../programa/clases/B76/B76-C13-sensores-de-proximidad/CLASE.md).

### Incertidumbre de la media

- La media es la suma dividida por el número de lecturas; la desviación estándar experimental `s` mide su dispersión; la incertidumbre de la media es `s/√n`.
- La incertidumbre de la media `s/√n` resume la repetición de una medición.

💡 **Cómo se explica en la clase [B104-C23](../programa/clases/B104/B104-C23-ejecucion-de-experimentos-a-bordo-procedimientos-y-registro/CLASE.md):**
- Cinco lecturas sintéticas de 5,00 ± 0,05: media 5,0203; desviación muestral 0,0477; incertidumbre de la media `0,0477/√5 = 0,0213`.
- Paso 3 · Incertidumbre de la media. `0,0477/√5 = 0,0213`.
- 🎯 **Por qué importa:** Las horas de tripulación son escasas y un dato sin registro fiable vale poco. La decisión central: ¿cómo repartir 20 horas entre experimentos para maximizar el valor y cómo asegurar que el registro de lo medido no se altere sin que se note?

📘 **Dónde se aprende** (2 clases): [B01-C18 · Incertidumbre y errores elementales](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md); [B104-C23 · Ejecución de experimentos a bordo: procedimientos y registro](../programa/clases/B104/B104-C23-ejecucion-de-experimentos-a-bordo-procedimientos-y-registro/CLASE.md).

### Incertidumbre de la pendiente

- La incertidumbre de la pendiente es `u(m) = s/√Sxx` (C05).

💡 **Cómo se explica en la clase [B13-C23](../programa/clases/B13/B13-C23-estabilidad-y-deriva-temporal-de-instrumentos/CLASE.md):**
- Descripción larga: la incertidumbre de la pendiente cae rápidamente al principio (`÷ 2,4` de 1 a 2 años) y cada vez más despacio; la relación señal–ruido de la deriva cruza `3` entre 4 y 5 años.
- 🎯 **Por qué importa:** Un detector espacial lleva años en órbita. Su sensibilidad cambia lentamente por daño de radiación, contaminación y envejecimiento.

📘 **Dónde se aprende** (1 clase): [B13-C23 · Estabilidad y deriva temporal de instrumentos](../programa/clases/B13/B13-C23-estabilidad-y-deriva-temporal-de-instrumentos/CLASE.md).

### Incertidumbre de medida

- Tolerancia: variación admisible del valor. Incertidumbre de medida: dispersión asociada a la medida.

🎯 **Por qué importa (clase B90-C08):** Toda medida tiene incertidumbre. Si se acepta con el límite exacto, algunas unidades malas pasan; si se endurece el criterio, algunas buenas se rechazan y cuesta tiempo.

📘 **Dónde se aprende** (1 clase): [B90-C08 · Procedimientos de prueba funcional](../programa/clases/B90/B90-C08-procedimientos-de-prueba-funcional/CLASE.md).

### Incertidumbre de Poisson

- La incertidumbre de Poisson es `1/√N`.

🎯 **Por qué importa (clase B85-C23):** Un monitor mal calibrado no distingue una dosis real del ruido. La decisión central: ¿cuál es la relación señal–dosis, desde qué dosis es fiable y hasta qué tasa de cuentas se puede corregir el tiempo muerto?

📘 **Dónde se aprende** (1 clase): [B85-C23 · Dosímetros y monitores de radiación a bordo](../programa/clases/B85/B85-C23-dosimetros-y-monitores-de-radiacion-a-bordo/CLASE.md).

### Incertidumbre del periodo

- La incertidumbre del periodo `σ_P = P²σ_f`.

🎯 **Por qué importa (clase B29-C14):** El periodo es la propiedad básica de una variable periódica; de él y de la forma de la curva se deducen la masa, la edad o la distancia en muchos casos. La decisión central: ¿qué periodo y qué incertidumbre da la serie y qué métodos coinciden?

📘 **Dónde se aprende** (1 clase): [B29-C14 · Estrellas variables periódicas](../programa/clases/B29/B29-C14-estrellas-variables-periodicas/CLASE.md).

### Incertidumbre estándar

- La incertidumbre estándar es la dispersión asociada a un valor medido; la relativa es esa incertidumbre dividida por el valor (S5).
- La incertidumbre estándar `u` es la desviación típica asociada; para un valor que puede estar con igual probabilidad en `[x − a, x + a]` (distribución uniforme o rectangular), `u = a/√3` (S2, apdo. 4.3.7).
- La incertidumbre estándar `u` se expresa como una desviación estándar (S1, 2.3.1).

💡 **Cómo se explica en la clase [B01-C18](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md):**
- Se declara si `±` es una incertidumbre estándar (`k = 1`) o expandida (`k = 2`): `0,01003 ± 0,00017 (k = 2)`.
- 🎯 **Por qué importa:** En C05 dijiste que un resultado de OPERA estaba «a unas 6 incertidumbres de cero» y otro «a menos de una». En C07 dijiste que dos intervalos de ±2σ no debían solaparse.

📘 **Dónde se aprende** (3 clases): [B01-C18 · Incertidumbre y errores elementales](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md); [B03-C12 · Variables y constantes científicas](../programa/clases/B03/B03-C12-variables-y-constantes-cientificas/CLASE.md); [B03-C19 · Propagación elemental de redondeos](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md).

### Incertidumbre expandida

- El intervalo de cobertura contiene la salida con una probabilidad dada (típicamente 95 %); la incertidumbre expandida es `U = k u_c` con factor de cobertura `k`.
- La incertidumbre expandida es `U = k u_c(y)`, con `k` el factor de cobertura (S1, 6.2.1, ec. 18); el GUM restringe el uso de la palabra «confianza» para el intervalo `y ± U` a ciertas condiciones (S1, 6.2.2).
- La incertidumbre expandida `U = k·u_c`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C18](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md):**
- La guía también permite una incertidumbre expandida `U = k·u_c`, con `k` un factor de cobertura (S1, 3.3.7), y da la ley de propagación para una función de varias entradas (S1, 5.1.2).
- 🎯 **Por qué importa:** En C05 dijiste que un resultado de OPERA estaba «a unas 6 incertidumbres de cero» y otro «a menos de una». En C07 dijiste que dos intervalos de ±2σ no debían solaparse.

📘 **Dónde se aprende** (4 clases): [B01-C18 · Incertidumbre y errores elementales](../programa/clases/B01/B01-C18-incertidumbre-y-errores-elementales/CLASE.md); [B12-C16 · Propagación de incertidumbre](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md); [B12-C20 · Informe de incertidumbre de una misión](../programa/clases/B12/B12-C20-informe-de-incertidumbre-de-una-mision/CLASE.md); [B84-C18 · Control dimensional](../programa/clases/B84/B84-C18-control-dimensional/CLASE.md).

### Incertidumbre expandida U

- La incertidumbre expandida `U` define un intervalo en torno al resultado que se espera abarque una fracción grande de los valores razonablemente atribuibles al mensurando (S1, 2.3.5).

🎯 **Por qué importa (clase B13-C12):** Un telémetro da `1000,004 m` con una incertidumbre típica de `0,017 m`. ¿Cuál es el intervalo dentro del cual el valor verdadero cae «casi seguro»?

📘 **Dónde se aprende** (1 clase): [B13-C12 · Incertidumbre expandida](../programa/clases/B13/B13-C12-incertidumbre-expandida/CLASE.md).

### Incertidumbre fusionada

- La incertidumbre fusionada es `1/√(Σ 1/σᵢ²)`.

🎯 **Por qué importa (clase B97-C03):** Un sensor con ruido bajo parece suficiente hasta que se ensucia, se descalibra o falla; entonces el robot necesita saber cuánto confiar en cada lectura. La fusión da la respuesta de forma cuantitativa, y también muestra su punto débil.

📘 **Dónde se aprende** (1 clase): [B97-C03 · Sensores y percepción robótica](../programa/clases/B97/B97-C03-sensores-y-percepcion-robotica/CLASE.md).

### Incertidumbre lateral

- La incertidumbre lateral de una medición angular es `d σ_θ`.

🎯 **Por qué importa (clase B80-C07):** B74-C04 y B74-C13 tratan la medición radiométrica y la óptica por separado. La decisión central: ¿en qué eje aporta cada sensor y cuánto mejora la incertidumbre al combinarlos?

📘 **Dónde se aprende** (1 clase): [B80-C07 · Fusión radio-óptica en navegación de espacio profundo](../programa/clases/B80/B80-C07-fusion-radio-optica-en-navegacion-de-espacio-profundo/CLASE.md).

### Incertidumbre marginal

- La incertidumbre marginal `σ_i = √(F⁻¹)_ii` incluye la incertidumbre de los demás parámetros.

💡 **Cómo se explica en la clase [B26-C22](../programa/clases/B26/B26-C22-degeneraciones-de-parametros-cosmologicos/CLASE.md):**
- ⚠️ **Error frecuente:** Confundir incertidumbre marginal con condicional. Se corrige con los ejercicios 4 y 9.
- 🎯 **Por qué importa:** Una incertidumbre marginal puede ser mucho mayor que la que se obtendría si el otro parámetro estuviera fijo, porque ambos se compensan. Sin analizar la degeneración se interpretan mal las barras de error y se desaprovechan las combinaciones de datos.

📘 **Dónde se aprende** (1 clase): [B26-C22 · Degeneraciones de parámetros cosmológicos](../programa/clases/B26/B26-C22-degeneraciones-de-parametros-cosmologicos/CLASE.md).

### Incertidumbre multiplicativa

- La incertidumbre multiplicativa escribe la planta real como `G_real = G (1 + Δ)`, con `Δ` el error relativo.

🎯 **Por qué importa (clase B16-C16):** La inercia de un satélite cambia al desplegar paneles, consumir propergol o capturar una carga; el actuador envejece; el sensor tiene un retardo que no se conocía. El lazo diseñado con la inercia nominal debe seguir funcionando.

📘 **Dónde se aprende** (1 clase): [B16-C16 · Control robusto inicial](../programa/clases/B16/B16-C16-control-robusto-inicial/CLASE.md).

### Incertidumbre neta

- La incertidumbre neta es `√(σ_med² + s²/n)`.

🎯 **Por qué importa (clase B55-C18):** En muestras extraterrestres la cantidad buscada puede ser del orden de la contaminación que entra al manipularlas. La decisión central: ¿la señal neta supera el límite de detección y con qué incertidumbre, una vez restado el blanco?

📘 **Dónde se aprende** (1 clase): [B55-C18 · Contaminación de muestras](../programa/clases/B55/B55-C18-contaminacion-de-muestras/CLASE.md).

### Incertidumbre paramétrica

- La incertidumbre paramétrica es no conocer el valor exacto de un parámetro (aquí `κ`).

🎯 **Por qué importa (clase B16-C16):** La inercia de un satélite cambia al desplegar paneles, consumir propergol o capturar una carga; el actuador envejece; el sensor tiene un retardo que no se conocía. El lazo diseñado con la inercia nominal debe seguir funcionando.

📘 **Dónde se aprende** (1 clase): [B16-C16 · Control robusto inicial](../programa/clases/B16/B16-C16-control-robusto-inicial/CLASE.md).

### Incertidumbre sistemática

- La incertidumbre sistemática afecta a todos los datos del mismo método por igual; la aleatoria varía de un dato a otro.

🎯 **Por qué importa (clase B01-C15):** La galaxia de la línea Hα (C01) está a 43 Mpc, pero ¿qué significa eso comparado con lo que ya conoces? ¿Está más lejos o más cerca que Andrómeda?

📘 **Dónde se aprende** (1 clase): [B01-C15 · Galaxias y agrupaciones cósmicas](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md).

### Incertidumbre típica

- La incertidumbre típica `u(xᵢ)` es la desviación típica asociada a la estimación `xᵢ` (S1, 4.2–4.3).
- La incertidumbre típica es la incertidumbre de un resultado expresada como una desviación típica (S1, 2.3.1).

💡 **Cómo se explica en la clase [B12-C16](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md):**
- Una tolerancia de ±1 500 m aporta *menos* incertidumbre típica que una desviación de 1 000 m, aunque «parezca» mayor, porque no tiene cola.
- El resultado va como: valor, incertidumbre típica combinada, factor de cobertura o intervalo, método y supuestos.
- 🎯 **Por qué importa:** Casi todo resultado en ciencias espaciales es una función de medidas: una velocidad a partir de un radio, una distancia a partir de una paralaje, una masa a partir de un período. Dar el valor sin su incertidumbre no permite comparar con otros resultados ni decidir si cumple un requisito.

📘 **Dónde se aprende** (2 clases): [B12-C16 · Propagación de incertidumbre](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md); [B13-C12 · Incertidumbre expandida](../programa/clases/B13/B13-C12-incertidumbre-expandida/CLASE.md).

### Incertidumbre típica combinada

- La incertidumbre típica combinada `u_c(y)` es la raíz de la suma ponderada de las varianzas (S1, 5.1.2).

💡 **Cómo se explica en la clase [B12-C20](../programa/clases/B12/B12-C20-informe-de-incertidumbre-de-una-mision/CLASE.md):**
- Paso 6 · Redacción. «`v = 7 668,579 m/s` con una incertidumbre típica combinada `u_c = 0,173 m/s` (`u_c/v = 2,3 × 10⁻⁵`); incertidumbre expandida `U = 0,339 m/s` con `k = 1,96` (≈ 95 %, `ν_eff ≈ 700`).
- 🎯 **Por qué importa:** Una cifra sin incertidumbre es una opinión; una incertidumbre sin presupuesto es una cifra sin respaldo. Quien revise la misión —otro ingeniero, un cliente o uno mismo dentro de un año— debe poder ver qué componentes se consideraron, cómo se evaluó cada uno, cuál domina y si el requisito se cumple.

📘 **Dónde se aprende** (1 clase): [B12-C20 · Informe de incertidumbre de una misión](../programa/clases/B12/B12-C20-informe-de-incertidumbre-de-una-mision/CLASE.md).

### Incertidumbre típica combinada u_c

- La incertidumbre típica combinada `u_c` es la de un resultado obtenido a partir de otras magnitudes, raíz de una suma de varianzas ponderadas (S1, 2.3.4;

🎯 **Por qué importa (clase B13-C12):** Un telémetro da `1000,004 m` con una incertidumbre típica de `0,017 m`. ¿Cuál es el intervalo dentro del cual el valor verdadero cae «casi seguro»?

📘 **Dónde se aprende** (1 clase): [B13-C12 · Incertidumbre expandida](../programa/clases/B13/B13-C12-incertidumbre-expandida/CLASE.md).

### Incertidumbre tipo A

- La incertidumbre tipo A viene del ruido y del ajuste; la tipo B de la fuerza de referencia (masas y gravedad local).

💡 **Cómo se explica en la clase [B102-C06](../programa/clases/B102/B102-C06-dinamometria-y-medicion-de-fuerzas-de-traccion/CLASE.md):**
- La incertidumbre tipo A de la predicción inversa con una lectura por punto de calibración y `m = 4` lecturas de la medida es `u_A = (σ/b) √(1/m + 1/n + (F − F̄)²/S_xx)`; la tipo B es `u_B = F u_ref` con `u_ref = 5,8 × 10⁻⁴`.
- 🎯 **Por qué importa:** Un tiro de barra de `176,8 N` sin incertidumbre no se puede comparar con un modelo. La decisión central: ¿con qué incertidumbre se mide una fuerza de tracción y qué parte viene del ruido, de la calibración y de la referencia?

📘 **Dónde se aprende** (1 clase): [B102-C06 · Dinamometría y medición de fuerzas de tracción](../programa/clases/B102/B102-C06-dinamometria-y-medicion-de-fuerzas-de-traccion/CLASE.md).

### Incertidumbre U

- Margen: `L − E − U`. Incertidumbre `U`: dispersión de la medida.

🎯 **Por qué importa (clase B90-C13):** Un convertidor de potencia emite armónicos que viajan por el arnés y pueden perturbar a otro equipo. El margen de 2 dB que pasa hoy puede ser negativo mañana si cambia la incertidumbre.

📘 **Dónde se aprende** (1 clase): [B90-C13 · Compatibilidad electromagnética EMC](../programa/clases/B90/B90-C13-compatibilidad-electromagnetica-emc/CLASE.md).

### Incidencia

- Una incidencia es lo que se desvió del protocolo (nubes, movimiento del soporte).

💡 **Cómo se explica en la clase [B01-C20](../programa/clases/B01/B01-C20-proyecto-de-observacion-cientifica-inicial/CLASE.md):**
- Descripción larga: cinco entradas cronológicas, cada una con hora, lectura, unidad e incidencia; la lectura 3 tiene una incidencia que el protocolo debería tratar (criterio de rechazo).
- 🎯 **Por qué importa:** Entender el método no es lo mismo que aplicarlo. Cuando mides de verdad, aparecen problemas que los ejercicios no tienen: el cielo se nubla, el palo no está del todo vertical, la regla se mueve, los datos no coinciden con lo que predijiste.

📘 **Dónde se aprende** (1 clase): [B01-C20 · Proyecto de observación científica inicial](../programa/clases/B01/B01-C20-proyecto-de-observacion-cientifica-inicial/CLASE.md).

### Incidente

- Incidente: evento que interrumpe la operación normal.

🎯 **Por qué importa (clase B96-C26):** Sin un procedimiento de priorización, un incidente leve puede retrasar a uno grave. La decisión central: ¿cuánto esperan los incidentes de alta y de baja prioridad y cuánto mejora la priorización al grave sin colapsar al leve?

📘 **Dónde se aprende** (1 clase): [B96-C26 · Gestión de incidentes en la operación de estaciones](../programa/clases/B96/B96-C26-gestion-de-incidentes-en-la-operacion-de-estaciones/CLASE.md).

### Inclinación

- La inclinación orbital es el ángulo entre dos planos de órbita.
- La inclinación `i` es el ángulo entre el plano orbital y el de referencia (de 0° a 180°); el nodo ascendente es el punto donde la órbita cruza el plano de referencia de sur a norte, y su longitud `Ω` se mide en ese plano desde la dirección de referencia.
- La inclinación es un giro `α` de la superficie.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B01-C12](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md):**
- La ficha de la Luna de NASA da un período sinódico de 29,53 d, un período sidéreo de 27,3217 d, una inclinación orbital de 5,145° respecto de la eclíptica, un semieje de 384 400 km y una excentricidad de 0,0549 (S1); la de la Tierra, un año trópico de 365,242 d (S2).
- 🎯 **Por qué importa:** La Luna es el reloj más a mano del cielo: cada noche cambia, y cada 29,5 días vuelve a empezar. Pero «a mano» no significa «fácil de explicar»: muchas personas creen que las fases son la sombra de la Tierra sobre la Luna.

📘 **Dónde se aprende** (5 clases): [B01-C12 · Fases lunares y ciclos celestes](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md); [B04-C14 · Producto vectorial y orientación](../programa/clases/B04/B04-C14-producto-vectorial-y-orientacion/CLASE.md); [B50-C11 · Errores de inclinación de elementos y superficies](../programa/clases/B50/B50-C11-errores-de-inclinacion-de-elementos-y-superficies/CLASE.md); [B71-C11 · Inclinación y nodo ascendente](../programa/clases/B71/B71-C11-inclinacion-y-nodo-ascendente/CLASE.md); [B85-C22 · Modelos de exposición a radiación en órbita](../programa/clases/B85/B85-C22-modelos-de-exposicion-a-radiacion-en-orbita/CLASE.md).

### Inclinación crítica

- La inclinación crítica es un valor de `i` con propiedades especiales bajo `J₂` (B72).
- La inclinación crítica es la raíz de `5 cos² i = 1`: `63,4349°` (y `116,5651°`).

💡 **Cómo se explica en la clase [B71-C12](../programa/clases/B71/B71-C12-argumento-del-periapsis/CLASE.md):**
- La inclinación crítica `arccos(1/√5) = 63.4349°` (y `116.5651°` retrógrada) es un resultado de la teoría de `J₂` que se deduce en B72 y no se consultó aquí.
- ⚠️ **Error frecuente:** Usar la inclinación crítica sin deducirla. Se corrige con 8.4.
- 🎯 **Por qué importa:** Un elemento mal condicionado puede dar un valor sin sentido aunque el estado sea exacto. La decisión central: ¿cuándo puedes fiarte de `ω` y qué ángulo usas cuando no?

📘 **Dónde se aprende** (2 clases): [B71-C12 · Argumento del periapsis](../programa/clases/B71/B71-C12-argumento-del-periapsis/CLASE.md); [B72-C05 · Precesión del argumento del periapsis](../programa/clases/B72/B72-C05-precesion-del-argumento-del-periapsis/CLASE.md).

### Inclinación crítica de Kozai

- La inclinación crítica de Kozai es `arccos √(3/5) = 39,23°` y su suplemento `140,77°`.

💡 **Cómo se explica en la clase [B73-C18](../programa/clases/B73/B73-C18-satelites-irregulares/CLASE.md):**
- La inclinación crítica de Kozai es `39,23°` (y `140,77°`).
- 🎯 **Por qué importa:** Los satélites irregulares son capturas: están lejos, en órbitas que ningún proceso de formación local explica. Ocupan una fracción de la esfera de Hill que depende del sentido de giro.

📘 **Dónde se aprende** (1 clase): [B73-C18 · Satélites irregulares](../programa/clases/B73/B73-C18-satelites-irregulares/CLASE.md).

### Inclinación crítica del nodo

- La inclinación crítica del nodo es `90°`, donde la tasa se anula.

🎯 **Por qué importa (clase B72-C04):** El nodo decide a qué hora local pasa un satélite sobre un lugar y cuándo su plano apunta al Sol. La decisión central: ¿qué altitud e inclinación hacen que el nodo avance o retroceda lo que necesita la misión?

📘 **Dónde se aprende** (1 clase): [B72-C04 · Precesión del nodo orbital](../programa/clases/B72/B72-C04-precesion-del-nodo-orbital/CLASE.md).

### Inclinación del dipolo

- La inclinación del dipolo respecto del eje de rotación es de `11°` en el ejemplo.

🎯 **Por qué importa (clase B87-C05):** Un cubesat sin sensores estelares usa el campo magnético para saber hacia dónde apunta y para detumbling (C16). La decisión central: ¿cuánto varía el campo a lo largo de la órbita, cuánto ruido y sesgo tolera la dirección medida y qué parte de la actitud no ve el magnetómetro?

📘 **Dónde se aprende** (1 clase): [B87-C05 · Magnetómetros](../programa/clases/B87/B87-C05-magnetometros/CLASE.md).

### Inclinación del eje de azimut

- La inclinación del eje de azimut (AN, AW).

🎯 **Por qué importa (clase B49-C03):** Con un haz estrecho, un error de apuntado pequeño pierde ganancia. La decisión central: ¿qué términos modelar, y cuánto error residual queda frente al ancho del haz?

📘 **Dónde se aprende** (1 clase): [B49-C03 · Apuntamiento y seguimiento de radiotelescopios: modelos de apuntado y errores](../programa/clases/B49/B49-C03-apuntamiento-y-seguimiento-de-radiotelescopios-modelos-de-apuntado-y-errores/CLASE.md).

### Inclinación equivalente

- La inclinación equivalente a un ángulo de campo.

🎯 **Por qué importa (clase B43-C18):** Colimar es ajustar tornillos hasta que el coma deje de verse; el modelo dice cuánto es «suficiente». La decisión central: ¿qué inclinación del primario produce un coma igual al radio de Airy y cuánto desvía un plano inclinado?

📘 **Dónde se aprende** (1 clase): [B43-C18 · Colimación instrumental](../programa/clases/B43/B43-C18-colimacion-instrumental/CLASE.md).

### Inclinación heliosíncrona

- La inclinación heliosíncrona satisface `cos i < 0`.

💡 **Cómo se explica en la clase [B72-C13](../programa/clases/B72/B72-C13-orbitas-heliosincronicas/CLASE.md):**
- A `700 km` de altitud, la inclinación heliosíncrona es `98,188°` y el periodo `98,77 min`; la integración con J2 da `0,98998 °/día` contra los `0,98565 °/día` requeridos (`0,44 %`).
- 🎯 **Por qué importa:** La misma hora local de paso significa la misma iluminación en cada imagen: es lo que usan las misiones de observación de la Tierra. La decisión central: ¿qué inclinación corresponde a cada altitud y cuánta deriva de hora local produce un error de inclinación?

📘 **Dónde se aprende** (1 clase): [B72-C13 · Órbitas heliosincrónicas](../programa/clases/B72/B72-C13-orbitas-heliosincronicas/CLASE.md).

### Incógnita

- La incógnita `x` es un vector de `n` números (aquí, el brillo en `n` posiciones); los datos `b` son `m` números;

🎯 **Por qué importa (clase B22-C01):** Un telescopio nunca entrega la imagen verdadera del cielo: la entrega emborronada por su respuesta óptica y con ruido. Calcular lo que verá el telescopio si conoces el objeto es fácil; el camino contrario, recuperar el objeto desde lo que vio, es el que interesa a la ciencia y el que se complica.

📘 **Dónde se aprende** (1 clase): [B22-C01 · Problemas directos e inversos y mal condicionamiento](../programa/clases/B22/B22-C01-problemas-directos-e-inversos-y-mal-condicionamiento/CLASE.md).

### Incógnitas

- Una ecuación es una igualdad con una o más incógnitas.

💡 **Cómo se explica en la clase [B03-C14](../programa/clases/B03/B03-C14-despeje-de-ecuaciones-elementales/CLASE.md):**
- Descripción larga: una fórmula central de la que salen tantas flechas como incógnitas posibles.
- 🎯 **Por qué importa:** La fórmula de la velocidad de escape, `v = √(2GM/R)`, aparece en las fichas de la NASA como un número (11,186 km/s). Pero un ingeniero puede necesitar lo contrario: dado `v`, ¿cuál es el radio?

📘 **Dónde se aprende** (1 clase): [B03-C14 · Despeje de ecuaciones elementales](../programa/clases/B03/B03-C14-despeje-de-ecuaciones-elementales/CLASE.md).

### Incompatibilidad

- Una incompatibilidad es una cercanía no deseada (polvo, ruido).

🎯 **Por qué importa (clase B109-C02):** Un buen plano ahorra pasos, separa lo sucio de lo limpio y deja las zonas tranquilas lejos de las ruidosas. La decisión central: ¿dónde pongo cada zona para que los recorridos frecuentes sean cortos y las zonas incompatibles estén lejos?

📘 **Dónde se aprende** (1 clase): [B109-C02 · Zonificación y distribución funcional de módulos de un hábitat](../programa/clases/B109/B109-C02-zonificacion-y-distribucion-funcional-de-modulos-de-un-habitat/CLASE.md).

### Incompatible

- Un sistema es compatible si tiene solución e incompatible si no (S1, §1.2(vi): `n` ecuaciones con `n` incógnitas).
- Es compatible determinado si tiene una solución, compatible indeterminado si tiene infinitas, incompatible si no tiene ninguna.

💡 **Cómo se explica en la clase [B04-C03](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md):**
- Con tres referencias, que no cumplan la misma recta, el sistema sería incompatible y habría que ajustar (B12).
- 🎯 **Por qué importa:** Un detector no entrega «brillo»: entrega cuentas. Para convertir cuentas en flujo hay que descubrir dos números, una pendiente y un desfase, y para ello se miden dos fuentes de referencia.

📘 **Dónde se aprende** (2 clases): [B04-C03 · Sistemas de ecuaciones elementales](../programa/clases/B04/B04-C03-sistemas-de-ecuaciones-elementales/CLASE.md); [B10-C05 · Sistemas lineales y eliminación](../programa/clases/B10/B10-C05-sistemas-lineales-y-eliminacion/CLASE.md).

### Incompresible

- Un flujo es incompresible cuando su densidad no cambia y `∇·u = 0`.
- El flujo es incompresible si `ρ` se toma constante.

💡 **Cómo se explica en la clase [B21-C04](../programa/clases/B21/B21-C04-ecuaciones-de-navier-stokes-y-dinamica-de-fluidos-computacional/CLASE.md):**
- El criterio habitual es el número de Mach: por debajo de unos 0,3 los cambios de densidad son pequeños y la formulación incompresible es una buena aproximación (regla práctica estándar, no respaldada por una fuente consultada).
- La formulación incompresible no tiene ondas sonoras, de modo que su paso de tiempo no está atado a la velocidad del sonido; el precio es resolver Poisson en cada paso (C03).
- ⚠️ **Error frecuente:** Usar la formulación incompresible a Mach alto. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un fluido aparece en casi toda la ingeniería aeroespacial: el aire alrededor de un cohete, el propelente que se mueve en un tanque, el refrigerante de un satélite.

📘 **Dónde se aprende** (2 clases): [B21-C04 · Ecuaciones de Navier-Stokes y dinámica de fluidos computacional](../programa/clases/B21/B21-C04-ecuaciones-de-navier-stokes-y-dinamica-de-fluidos-computacional/CLASE.md); [B79-C01 · Conservación de masa en fluidos](../programa/clases/B79/B79-C01-conservacion-de-masa-en-fluidos/CLASE.md).

### Incrementos preintegrados

- Los incrementos preintegrados son `Δψ = Σ(ω_k − b_g)Δt`, `Δv = Σ R(Δψ_k)(f_k − b_a)Δt` y `Δp`.

🎯 **Por qué importa (clase B80-C09):** B87-C06 trata los giroscopios; falta la integración conjunta de acelerómetros y giroscopios para estimar el movimiento de un robot y su deriva. La decisión central: ¿cómo se reutiliza una integración inercial cuando cambian el estado inicial y los sesgos estimados?

📘 **Dónde se aprende** (1 clase): [B80-C09 · Odometría inercial y preintegración de IMU](../programa/clases/B80/B80-C09-odometria-inercial-y-preintegracion-de-imu/CLASE.md).

### Incursión

- La incursión es un acercamiento menor que la esfera de exclusión (`20 m`, hipótesis).

💡 **Cómo se explica en la clase [B76-C20](../programa/clases/B76/B76-C20-simulacion-de-encuentro-seguro/CLASE.md):**
- La velocidad relativa final media es `0,48 cm/s` y la distancia mínima en toda la corrida, `36,80 m`: ninguna incursión en `20 m`.
- En 20 corridas sin el último impulso y con 3 periodos de deriva, la distancia mínima es `26,24 m`: no hay incursión, con margen de solo `6 m` sobre la exclusión supuesta.
- 🎯 **Por qué importa:** Cada pieza del bloque funciona en su caso ideal; la seguridad se juega en la combinación con errores. La decisión central: ¿llega el perseguidor con la precisión pedida y se mantiene fuera de la esfera de exclusión incluso si falla un impulso?

📘 **Dónde se aprende** (1 clase): [B76-C20 · Simulación de encuentro seguro](../programa/clases/B76/B76-C20-simulacion-de-encuentro-seguro/CLASE.md).

### Independencia

- La independencia supone que las medidas no comparten errores.
- Log-verosimilitud: `ln(p/(1−p))`, peso óptimo bajo independencia. Independencia: errores no relacionados.

💡 **Cómo se explica en la clase [B26-C21](../programa/clases/B26/B26-C21-verosimilitud-cosmologica-con-datos-combinados/CLASE.md):**
- ⚠️ **Error frecuente:** Suponer independencia sin comprobarla. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Ninguna sonda fija sola todos los parámetros; combinarlas reduce la incertidumbre, pero solo si son compatibles entre sí y si se tratan bien sus correlaciones. La decisión central: dadas tres restricciones sobre `Ω_m`, ¿cuál es el valor combinado, qué incertidumbre tiene y son consistentes entre sí?

📘 **Dónde se aprende** (2 clases): [B26-C21 · Verosimilitud cosmológica con datos combinados](../programa/clases/B26/B26-C21-verosimilitud-cosmologica-con-datos-combinados/CLASE.md); [B48-C19 · Divulgación y ciencia ciudadana](../programa/clases/B48/B48-C19-divulgacion-y-ciencia-ciudadana/CLASE.md).

### Independencia ingenua

- La independencia ingenua supone que los sitios no están correlacionados.

🎯 **Por qué importa (clase B28-C16):** La cobertura de una red depende de su distribución geográfica, no solo del número de telescopios. La decisión central: ¿qué probabilidad hay de que, al llegar una alerta, al menos un sitio de la red pueda observar la fuente?

📘 **Dónde se aprende** (1 clase): [B28-C16 · Redes internacionales de alertas](../programa/clases/B28/B28-C16-redes-internacionales-de-alertas/CLASE.md).

### Independiente

- La variable dependiente es la que se mide como resultado; la independiente, la que se cambia o se deja evolucionar (por ejemplo, el día del mes).

🎯 **Por qué importa (clase B01-C06):** «¿Hay vida en otros planetas?» es una pregunta legítima y apasionante, pero nadie puede responderla con un cuaderno y una cámara de teléfono. «¿Cambia el tamaño aparente de la Luna a lo largo de un mes?» sí puede responderse con una cámara y un trípode, y su respuesta enseña algo real sobre la órbita lunar.

📘 **Dónde se aprende** (1 clase): [B01-C06 · Preguntas investigables en astronomía](../programa/clases/B01/B01-C06-preguntas-investigables-en-astronomia/CLASE.md).

### Independientes

- Dos eventos son independientes si `P(A∩B) = P(A)P(B)`.
- Dos variables son independientes si el valor de una no informa sobre la otra (formalización en C05).
- Si `r = 0` las variables están no correlacionadas: un cambio en una no implica un cambio esperado en la otra (S1, 5.2.2). Independientes (S1, C.3.7) es más fuerte: la distribución de una no cambia al conocer la otra; independientes ⇒ `Cov = 0`, pero no al revés.

💡 **Cómo se explica en la clase [B12-C01](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md):**
- Si los computadores son independientes, el peso de un resultado es el producto de sus factores: `FFX` pesa `0,9 · 0,9 · 0,1 = 0,081`.
- Paso 1 · Datos. `p = 0,9`, tres computadores independientes, decisión por mayoría.
- ⚠️ **Error frecuente:** Confundir excluyentes con independientes. Se corrige con los ejercicios 7 y 8: eventos excluyentes con probabilidad positiva son dependientes.
- 🎯 **Por qué importa:** Una nave no sabe si un componente va a fallar; un telescopio no sabe cuántos fotones llegarán. Para decidir con información incompleta hace falta un lenguaje que diga con precisión *qué puede pasar* y *cuánto lo esperamos*.

📘 **Dónde se aprende** (3 clases): [B12-C01 · Espacios muestrales y eventos](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md); [B12-C04 · Esperanza y varianza](../programa/clases/B12/B12-C04-esperanza-y-varianza/CLASE.md); [B12-C05 · Covarianza y correlación](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md).

### Indicación

- La indicación es el valor que da el instrumento (aquí DN).

💡 **Cómo se explica en la clase [B13-C05](../programa/clases/B13/B13-C05-calibracion-instrumental/CLASE.md):**
- Con `n` patrones se estiman `a` (ordenada: indicación cuando `x = 0`) y `b` (pendiente: sensibilidad, DN por W/m²).
- Para una indicación media `y₀` de `m` lecturas de una fuente desconocida: `x̂₀ = (y₀ − â)/b̂`, con `u(x̂₀) = (s/|b̂|) √(1/m + 1/n + (x̂₀ − x̄)²/Sxx)` (fórmula clásica de la calibración lineal inversa; no se consultó una fuente específica en esta clase).
- 🎯 **Por qué importa:** Un sensor solar de una nave devuelve cuentas digitales (DN), no vatios por metro cuadrado. Para saber cuánta luz recibe hay que haberlo expuesto antes a fuentes de irradiancia conocida y haber establecido la relación entre ambas.

📘 **Dónde se aprende** (1 clase): [B13-C05 · Calibración instrumental](../programa/clases/B13/B13-C05-calibracion-instrumental/CLASE.md).

### Indicador

- Un indicador es una medida en % del valor previo.

💡 **Cómo se explica en la clase [B107-C09](../programa/clases/B107/B107-C09-progresion-de-recuperacion-y-criterios-de-alta/CLASE.md):**
- En una conjunción el calendario lo fija el indicador más lento: la resistencia (50,2 d).
- 🎯 **Por qué importa:** Los fragmentos consultados indican que la pérdida de fuerza tras misiones largas conlleva riesgos operativos y médicos (English et al., 2015) y que existen baterías de pruebas funcionales y medidas fisiológicas (Mulavara et al., 2018). Una regla de alta combina varios indicadores con ruido.

📘 **Dónde se aprende** (1 clase): [B107-C09 · Progresión de recuperación y criterios de alta](../programa/clases/B107/B107-C09-progresion-de-recuperacion-y-criterios-de-alta/CLASE.md).

### Indicador de excitación

- El indicador de excitación es la desviación típica de la aceleración de cámara.

💡 **Cómo se explica en la clase [B80-C06](../programa/clases/B80/B80-C06-fusion-imu-camara/CLASE.md):**
- El indicador de excitación (desviación típica de `a_cam`) es `2,436` con el movimiento senoidal y `0,124` con velocidad constante, que es solo ruido.
- A velocidad constante, el indicador de excitación cae de `2,436` a `0,124` y las estimaciones de `λ` se dispersan entre `−693` y `1881`.
- 🎯 **Por qué importa:** Ni B74 ni B87 acoplan una IMU y una cámara en una sola solución. La decisión central: ¿qué debe hacer el vehículo para que la fusión visual-inercial sea observable, y qué se pierde si va a velocidad constante?

📘 **Dónde se aprende** (1 clase): [B80-C06 · Fusión IMU-cámara](../programa/clases/B80/B80-C06-fusion-imu-camara/CLASE.md).

### Indicador de salud

- El indicador de salud es la magnitud que resume la condición.

🎯 **Por qué importa (clase B97-C26):** Reparar cuando algo falla puede ser imposible en un entorno remoto, y reparar «por si acaso» desperdicia piezas. Un indicador que avise a tiempo y una proyección con su incertidumbre permiten planificar la reparación.

📘 **Dónde se aprende** (1 clase): [B97-C26 · Monitoreo de condición de maquinaria extraterrestre](../programa/clases/B97/B97-C26-monitoreo-de-condicion-de-maquinaria-extraterrestre/CLASE.md).

### Índice

- Un índice es la posición de un elemento, desde 0; un índice negativo cuenta desde el final.
- El índice `α` de `dN/dE ∝ E^{−α}`.
- El índice `α` de una ley de potencias `m^−α`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C07](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md):**
- ⚠️ **Error frecuente:** Índice fuera de rango. `IndexError`.
- 🎯 **Por qué importa:** Una tabla de ocho planetas con tres propiedades cada uno son 24 datos: no cabe en 24 variables sueltas. Necesitas estructuras que agrupen datos, permitan recorrerlos y los mantengan ordenados y consultables.

📘 **Dónde se aprende** (4 clases): [B07-C07 · Listas y estructuras de datos](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md); [B29-C15 · Eventos eruptivos estelares](../programa/clases/B29/B29-C15-eventos-eruptivos-estelares/CLASE.md); [B38-C02 · Función inicial de masa y su universalidad](../programa/clases/B38/B38-C02-funcion-inicial-de-masa-y-su-universalidad/CLASE.md); [B83-C21 · Identificación de peligros en sistemas de lanzamiento (HAZID)](../programa/clases/B83/B83-C21-identificacion-de-peligros-en-sistemas-de-lanzamiento-hazid/CLASE.md).

### Índice adiabático

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B37-C07):** El período fundamental fija la densidad media. La decisión central: ¿cuánto vale el período de un modo radial y cómo escala con la densidad?

📘 **Dónde se aprende** (1 clase): [B37-C07 · Oscilaciones radiales y relación período-densidad media](../programa/clases/B37/B37-C07-oscilaciones-radiales-y-relacion-periodo-densidad-media/CLASE.md).

### Índice complejo

- El índice complejo `N = n − i k`.

💡 **Cómo se explica en la clase [B43-C07](../programa/clases/B43/B43-C07-aluminizado-y-recubrimientos/CLASE.md):**
- *Descripción textual:* el índice complejo da la reflectancia y la transmisión de la película; la geometría del evaporador da la uniformidad.
- 🎯 **Por qué importa:** Una película delgada deja pasar luz; una gruesa refleja pero no se adhiere ni es uniforme. La decisión central: ¿qué espesor es opaco, qué reflectancia da y cuánto varía de centro a borde por la geometría del evaporador?

📘 **Dónde se aprende** (1 clase): [B43-C07 · Aluminizado y recubrimientos](../programa/clases/B43/B43-C07-aluminizado-y-recubrimientos/CLASE.md).

### Índice crítico

- El índice crítico `α = 2`.

🎯 **Por qué importa (clase B34-C01):** Elegir un mecanismo de calentamiento exige saber cuánta energía hay que reponer y de dónde sale. La decisión central: ¿cuánta energía pierde un bucle y qué eventos pueden reponerla?

📘 **Dónde se aprende** (1 clase): [B34-C01 · Calentamiento coronal: mecanismos y evidencias](../programa/clases/B34/B34-C01-calentamiento-coronal-mecanismos-y-evidencias/CLASE.md).

### Índice de agua

- Un índice de agua (como el NDWI) realza el agua: `(verde − NIR)/(verde + NIR)`.

💡 **Cómo se explica en la clase [B57-C15](../programa/clases/B57/B57-C15-sequias-e-inundaciones/CLASE.md):**
- *Descripción textual:* el histograma del índice de agua tiene dos modas;
- 🎯 **Por qué importa:** Las agencias necesitan mapas de inundación en horas y alertas de sequía en meses. La decisión central: ¿cómo se fija el umbral entre agua y tierra sin fijarlo a ojo, y cómo se declara que un año es seco?

📘 **Dónde se aprende** (1 clase): [B57-C15 · Sequías e inundaciones](../programa/clases/B57/B57-C15-sequias-e-inundaciones/CLASE.md).

### Índice de Atkinson

- El índice de Atkinson penaliza la desigualdad con aversión `ε`.

🎯 **Por qué importa (clase B119-C34):** El acceso desigual al espacio es un asunto de gobernanza que el catálogo no trata; esta clase da las herramientas de medición antes de las discusiones de política (C25, C36). La decisión central: ¿qué tan desigual es el acceso y cuánto lo reduce una regla de uso compartido?

📘 **Dónde se aprende** (1 clase): [B119-C34 · Equidad de acceso al espacio](../programa/clases/B119/B119-C34-equidad-de-acceso-al-espacio/CLASE.md).

### Índice de Banzhaf

- El índice de Banzhaf es la fracción de veces que un miembro es decisivo.

💡 **Cómo se explica en la clase [B125-C03](../programa/clases/B125/B125-C03-gobierno-corporativo-de-una-empresa-espacial/CLASE.md):**
- El índice de Banzhaf cuenta, por miembro, en cuántas coaliciones ganadoras es decisivo y normaliza a suma `1`.
- 🎯 **Por qué importa:** Las decisiones de una empresa se estructuran en su gobierno y, en el espacio, el capital intensivo hace que quien controla la votación controle el rumbo de misiones de años; ninguna clase lo trata.

📘 **Dónde se aprende** (1 clase): [B125-C03 · Gobierno corporativo de una empresa espacial](../programa/clases/B125/B125-C03-gobierno-corporativo-de-una-empresa-espacial/CLASE.md).

### Índice de caída

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B28-C08):** Un transitorio que dura menos que el intervalo entre visitas se pierde. El índice de caída decide cuánto dura un evento sobre el límite de detección.

📘 **Dónde se aprende** (1 clase): [B28-C08 · Señales transitorias](../programa/clases/B28/B28-C08-senales-transitorias/CLASE.md).

### Índice de cambio fiable

- El índice de cambio fiable `RCI` estandariza una diferencia con el error.

🎯 **Por qué importa (clase B107-C04):** Los fragmentos consultados describen una batería computarizada de pruebas breves de varios dominios cognitivos diseñada para astronautas de alto rendimiento (Basner et al., 2015; Casario et al., 2022) y preguntan cómo se relacionan sus descensos con el desempeño operativo (Basner et al., 2020).

📘 **Dónde se aprende** (1 clase): [B107-C04 · Evaluación del rendimiento físico y cognitivo de tripulantes](../programa/clases/B107/B107-C04-evaluacion-del-rendimiento-fisico-y-cognitivo-de-tripulantes/CLASE.md).

### Índice de convergencia de malla (GCI)

- El índice de convergencia de malla (GCI) estima la incertidumbre numérica a partir de tres mallas.

🎯 **Por qué importa (clase B79-C09):** B11-C14/C15 no construyen simulaciones de flujo ni discuten sus límites. Sin esa discusión, una malla fina y un colorido mapa de campos se confunden con una predicción fiable.

📘 **Dónde se aprende** (1 clase): [B79-C09 · CFD académico: fundamentos y límites](../programa/clases/B79/B79-C09-cfd-academico-fundamentos-y-limites/CLASE.md).

### Índice de decaimiento

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B34-C08](../programa/clases/B34/B34-C08-erupciones-de-filamentos-y-prominencias/CLASE.md):**
- *Descripción textual:* el campo externo define el índice de decaimiento y la altura crítica; la masa y la altura dan las energías.
- 🎯 **Por qué importa:** Saber a qué altura el campo ya no sostiene al filamento sirve para anticipar erupciones. La decisión central: ¿a qué altura el decaimiento del campo supera el umbral?

📘 **Dónde se aprende** (1 clase): [B34-C08 · Erupciones de filamentos y prominencias](../programa/clases/B34/B34-C08-erupciones-de-filamentos-y-prominencias/CLASE.md).

### Índice de dificultad

- El índice de dificultad de Fitts es `ID = log₂(D/W + 1)` en bits (formulación de Shannon), con `D` la distancia al objetivo y `W` su ancho.

🎯 **Por qué importa (clase B111-C01):** Una interfaz mal diseñada convierte a una tripulación competente en una fuente de errores. La decisión central: ¿qué parte del tiempo y del error es del diseño y no de la persona?

📘 **Dónde se aprende** (1 clase): [B111-C01 · Fundamentos de factores humanos en operaciones espaciales](../programa/clases/B111/B111-C01-fundamentos-de-factores-humanos-en-operaciones-espaciales/CLASE.md).

### Índice de diversidad de Blau

- El índice de diversidad de Blau es `1 − Σ pg²`, con `pg` la fracción de la tripulación en el grupo `g`.

💡 **Cómo se explica en la clase [B111-C02](../programa/clases/B111/B111-C02-gestion-intercultural-en-tripulaciones-multinacionales/CLASE.md):**
- Una tripulación sintética de seis miembros en tres grupos ficticios (G1, G2, G3) tiene un índice de diversidad de Blau de `0,6667`.
- 🎯 **Por qué importa:** Ninguna clase del programa trataba las diferencias culturales y de idioma en equipos internacionales. La decisión central: ¿cómo se vuelve un riesgo de comunicación cuantificable y cómo se mitiga con procedimientos y no con estereotipos?

📘 **Dónde se aprende** (1 clase): [B111-C02 · Gestión intercultural en tripulaciones multinacionales](../programa/clases/B111/B111-C02-gestion-intercultural-en-tripulaciones-multinacionales/CLASE.md).

### Índice de estabilidad

- La monodromia `M` y el índice de estabilidad `ν = (λ + 1/λ)/2` miden el crecimiento del error por revolución.

🎯 **Por qué importa (clase B76-C05):** La NRHO es la órbita de referencia publicada para la estación Gateway. La decisión central: ¿cómo se calcula una órbita periódica inestable y qué tan cerca queda un modelo simple de la referencia en un modelo de efemérides?

📘 **Dónde se aprende** (1 clase): [B76-C05 · Órbitas NRHO](../programa/clases/B76/B76-C05-orbitas-nrho/CLASE.md).

### Índice de fiabilidad

- El índice de fiabilidad `β = −Φ⁻¹(P_f)`.

🎯 **Por qué importa (clase B84-C24):** Dos miembros con margen positivo no son igual de seguros si sus factores y sus dispersiones difieren; y un margen negativo exige rediseño o una justificación explícita. La decisión central: ¿qué miembros cumplen con sus factores y qué probabilidad de falla implica cada factor?

📘 **Dónde se aprende** (1 clase): [B84-C24 · Factores de seguridad y márgenes estructurales](../programa/clases/B84/B84-C24-factores-de-seguridad-y-margenes-estructurales/CLASE.md).

### Índice de Gini

- El índice de Gini mide la concentración (0 = reparto igual; cercano a 1 = unos pocos hacen casi todo).

💡 **Cómo se explica en la clase [B129-C06](../programa/clases/B129/B129-C06-motivacion-y-permanencia-de-participantes/CLASE.md):**
- *Descripción textual:* de la cohorte se obtienen la curva de Kaplan–Meier y el riesgo, que se contrastan entre sí y entre dos cohortes; aparte, las contribuciones por voluntario dan el índice de Gini.
- 🎯 **Por qué importa:** Los equipos de un proyecto quieren retener voluntarios y a menudo añaden insignias, rachas o clasificaciones sin medir si sirven. La decisión central: ¿cómo medir la permanencia y cuándo se puede decir que algo la mejoró?

📘 **Dónde se aprende** (1 clase): [B129-C06 · Motivación y permanencia de participantes](../programa/clases/B129/B129-C06-motivacion-y-permanencia-de-participantes/CLASE.md).

### Índice de individualidad

- El índice de individualidad `CVi/CVg` menor que 0,6 indica que el rango poblacional detecta mal cambios personales.

💡 **Cómo se explica en la clase [B105-C24](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md):**
- El intervalo de referencia es 69,5–132,6 u.a.; el índice de individualidad `CVi/CVg = 0,33`; el RCV es 16,2 %.
- 🎯 **Por qué importa:** Con tripulaciones pequeñas, el intervalo de la población general es poco sensible a los cambios personales, y un umbral con baja prevalencia da más falsas alarmas que aciertos. La decisión central: ¿cuándo un cambio de un indicador es real y qué umbral equilibra sensibilidad y valor predictivo?

📘 **Dónde se aprende** (1 clase): [B105-C24 · Indicadores clínicos y biomarcadores de vuelo](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md).

### Índice de la cola

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B30-C19](../programa/clases/B30/B30-C19-impactos-del-clima-espacial/CLASE.md):**
- *Descripción textual:* el campo y la longitud dan la corriente por un circuito; el registro da el índice de la cola, el nivel de retorno y su intervalo.
- 🎯 **Por qué importa:** Las infraestructuras se diseñan para eventos raros, que no están en un registro corto. La decisión central: ¿qué corriente induce un campo dado y cuán fiable es extrapolar un nivel de 100 años?

📘 **Dónde se aprende** (1 clase): [B30-C19 · Impactos del clima espacial](../programa/clases/B30/B30-C19-impactos-del-clima-espacial/CLASE.md).

### Índice de Lerner

- El índice de Lerner `L = (P − c)/P` mide el margen de precio sobre costo.

🎯 **Por qué importa (clase B124-C03):** Hablar de «mercado upstream» o «downstream» sin medir su concentración deja la discusión en opinión. La decisión central: ¿qué tan concentrado está un mercado y qué margen de precio permite esa concentración?

📘 **Dónde se aprende** (1 clase): [B124-C03 · Mercados downstream y upstream](../programa/clases/B124/B124-C03-mercados-downstream-y-upstream/CLASE.md).

### Índice de panel

- El índice de panel es `E^(1/3)/ρ`; el de tirante, `σ_y/ρ`; el de columna, `E^(1/2)/ρ`.

🎯 **Por qué importa (clase B84-C05):** Un ganador que cambia con pequeñas variaciones de pesos no es una decisión: es una opinión. La sensibilidad dice si la elección es robusta.

📘 **Dónde se aprende** (1 clase): [B84-C05 · Selección de materiales](../programa/clases/B84/B84-C05-seleccion-de-materiales/CLASE.md).

### Índice de población

- El índice de población `r` mide la proporción de meteoros débiles frente a brillantes y se toma de una fuente o se supone.
- El índice de población `r` es el cociente de meteoros que hay en cada magnitud respecto de la anterior más brillante.

💡 **Cómo se explica en la clase [B08-C18](../programa/clases/B08/B08-C18-introduccion-a-meteoros-y-lluvias/CLASE.md):**
- De la definición de ZHR (S3) se deduce, bajo supuestos declarados, que `ZHR = N · r^(6,5 − lm) / (T · sen h · (1 − c))`, donde `N` es el número de meteoros de la lluvia en `T` horas, `lm` la magnitud límite, `r` el índice de población (aquí 2,5, valor de ejemplo), `h` la altura del radiante y `c` la fracción de cielo cubierta por nubes.
- 🎯 **Por qué importa:** Cada año, titulares prometen «cientos de estrellas fugaces por hora». Con un cielo contaminado o con el radiante bajo el horizonte, verás muy pocas.

📘 **Dónde se aprende** (2 clases): [B08-C18 · Introducción a meteoros y lluvias](../programa/clases/B08/B08-C18-introduccion-a-meteoros-y-lluvias/CLASE.md); [B129-C03 · Seguimiento ciudadano de meteoros](../programa/clases/B129/B129-C03-seguimiento-ciudadano-de-meteoros/CLASE.md).

### Índice de Rand ajustado

- El índice de Rand ajustado (ARI) compara dos agrupaciones: 1 si coinciden, ≈ 0 si coinciden como el azar.

🎯 **Por qué importa (clase B15-C23):** Un satélite fotografía una región que nadie ha cartografiado. Sin muestras, no se puede entrenar un clasificador, pero sí se puede preguntar cuántos «tipos» de superficie distintos hay en las bandas.

📘 **Dónde se aprende** (1 clase): [B15-C23 · Clasificación no supervisada y agrupamiento de imágenes](../programa/clases/B15/B15-C23-clasificacion-no-supervisada-y-agrupamiento-de-imagenes/CLASE.md).

### Índice de refracción

- En un medio, la luz va más lenta: `v = c/n`, con `n` el índice de refracción.
- El índice de refracción `n = c/v`.

🎯 **Por qué importa (clase B05-C19):** Un telescopio espacial o una cámara en órbita baja distinguen detalles hasta cierto límite que no depende de la calidad de la electrónica, y la luz de un objeto lejano llega con retraso. La pregunta motivadora es: ¿qué determina cuán pequeño es el detalle que un instrumento óptico puede resolver y cuánto tarda la luz en llegar?

📘 **Dónde se aprende** (2 clases): [B05-C19 · Óptica y velocidad de la luz](../programa/clases/B05/B05-C19-optica-y-velocidad-de-la-luz/CLASE.md); [B41-C01 · Naturaleza y propagación de la luz](../programa/clases/B41/B41-C01-naturaleza-y-propagacion-de-la-luz/CLASE.md).

### Índice de refracción efectivo

- El índice de refracción efectivo de la luz es `n = 1 − 2Φ/c² = 1 + 2GM/(c²r)`.

🎯 **Por qué importa (clase B26-C09):** La luz de una estrella lejana que pasa cerca del Sol, o de una galaxia, se desvía: es la base de las lentes gravitacionales que miden masas de cúmulos (C18) y de las correcciones al seguimiento de naves en el espacio profundo.

📘 **Dónde se aprende** (1 clase): [B26-C09 · Relatividad general introductoria](../programa/clases/B26/B26-C09-relatividad-general-introductoria/CLASE.md).

### Índice de riesgo aditivo

- SWEG: guía de agua potable. Índice de riesgo aditivo: suma de razones concentración/límite.

🎯 **Por qué importa (clase B106-C24):** Evaluar el aire exige límites y una regla para combinar contaminantes; ninguno basta por sí solo. La decisión central: ¿cumple una mezcla de contaminantes su límite combinado y qué compuesto la domina?

📘 **Dónde se aprende** (1 clase): [B106-C24 · Calidad del aire y límites de exposición en cabina](../programa/clases/B106/B106-C24-calidad-del-aire-y-limites-de-exposicion-en-cabina/CLASE.md).

### Índice de Sérsic

- El perfil de Sérsic describe el brillo superficial: `I(R) = I_e exp{−b_n [(R/R_e)^{1/n} − 1]}`, donde `R` es el radio proyectado, `R_e` el radio efectivo (contiene la mitad de la luz), `I_e` el brillo en `R_e`, `n` el índice de Sérsic y `b_n` una constante que depende de `n` y que garantiza que `R_e` contiene la mitad de la luz.

🎯 **Por qué importa (clase B25-C09):** Las galaxias parecen muy distintas: discos con brazos y gas, o bolas suaves de estrellas viejas. Esa diferencia guarda su historia (formación estelar, fusiones) y exige un lenguaje común para compararlas.

📘 **Dónde se aprende** (1 clase): [B25-C09 · Galaxias elípticas y espirales](../programa/clases/B25/B25-C09-galaxias-elipticas-y-espirales/CLASE.md).

### Índice de Shannon

- El índice de Shannon `H = −Σ p ln p` y el de Simpson `1 − Σ p²` miden diversidad.

🎯 **Por qué importa (clase B105-C11):** Un índice de diversidad depende de la comunidad y de cuántas lecturas se obtuvieron. La decisión central: ¿qué profundidad de muestreo hace fiable un índice y cómo se cuantifica el parecido entre la piel de la tripulación y las superficies?

📘 **Dónde se aprende** (1 clase): [B105-C11 · Microbioma en ambientes cerrados](../programa/clases/B105/B105-C11-microbioma-en-ambientes-cerrados/CLASE.md).

### Índice de shock

- El índice de shock `IS` es `FC/PAS`.

💡 **Cómo se explica en la clase [B117-C03](../programa/clases/B117/B117-C03-emergencia-cardiovascular-simulada/CLASE.md):**
- La hemorragia y la taquiarritmia superan el umbral de alerta de 0,9; la bradicardia no, aunque su presión es baja: el índice de shock mide una cosa y no sirve para todo.
- *Descripción textual:* de la frecuencia y el volumen sistólico salen el gasto, la presión y el índice de shock; en un paro la presión decae hacia `P_mcf` con la constante de tiempo `R C`.
- ⚠️ **Error frecuente:** Tomar el índice de shock como diagnóstico. Se corrige con 8.4 y el ejercicio 10.
- 🎯 **Por qué importa:** Ninguna clase anterior simula una emergencia cardiovascular. La decisión central: ¿qué señales de un modelo simple delatan un problema de circulación y cuáles lo esconden?

📘 **Dónde se aprende** (1 clase): [B117-C03 · Emergencia cardiovascular simulada](../programa/clases/B117/B117-C03-emergencia-cardiovascular-simulada/CLASE.md).

### Índice de Sobol de primer orden

- El índice de Sobol de primer orden `Sᵢ = Var(E[Y|Xᵢ])/Var(Y)` es la fracción de la varianza de `Y` explicada por `Xᵢ` sola; el índice total `S_Tᵢ` incluye además todas sus interacciones.

🎯 **Por qué importa (clase B12-C17):** Mejorar una medida cuesta dinero, masa o tiempo. Si el presupuesto de una misión ofrece mejorar la masa seca o el empuje específico, hay que saber cuál de las dos reduce más la incertidumbre del resultado.

📘 **Dónde se aprende** (1 clase): [B12-C17 · Análisis de sensibilidad](../programa/clases/B12/B12-C17-analisis-de-sensibilidad/CLASE.md).

### Índice de Szigriszt-Pazos

- El índice de Szigriszt-Pazos es `IFSZ = 206,835 − 62,3 · S/P − P/F`, con `S` sílabas, `P` palabras y `F` frases.

🎯 **Por qué importa (clase B130-C03):** Presentar ante público requiere técnicas propias; la clase de comunicación escrita general no cubre el tiempo, el ritmo ni la jerga hablada. La decisión central: ¿qué cabe en el tiempo disponible y qué entenderá una persona que oye el guion una sola vez?

📘 **Dónde se aprende** (1 clase): [B130-C03 · Comunicación oral de la ciencia](../programa/clases/B130/B130-C03-comunicacion-oral-de-la-ciencia/CLASE.md).

### Índice del aire

- El índice del aire `n` hace `λ_aire = λ_vacío/n`.

🎯 **Por qué importa (clase B45-C08):** Un error de calibración es un error de velocidad o de identificación de líneas. La decisión central: ¿qué grado del polinomio es adecuado y cuánto se puede fiar el ajuste fuera de las líneas?

📘 **Dónde se aprende** (1 clase): [B45-C08 · Calibración en longitud de onda](../programa/clases/B45/B45-C08-calibracion-en-longitud-de-onda/CLASE.md).

### Índice del electrón

- El índice del electrón `p` en `N(γ) ∝ γ^{−p}`.

🎯 **Por qué importa (clase B27-C12):** El índice espectral de una fuente sincrotrón entrega el índice de energía de sus electrones; la frecuencia crítica entrega `γ²B`. Sin estas relaciones no se puede leer un espectro de radio o rayos X.

📘 **Dónde se aprende** (1 clase): [B27-C12 · Radiación sincrotrón](../programa/clases/B27/B27-C12-radiacion-sincrotron/CLASE.md).

### Índice Dst

- El índice Dst mide la perturbación.

🎯 **Por qué importa (clase B30-C22):** El índice Dst (B30-C23) es un indicador de la energía del anillo de corriente. La decisión central: ¿qué energía y qué corriente corresponden a una disminución dada del campo?

📘 **Dónde se aprende** (1 clase): [B30-C22 · Anillo de corriente y corrientes magnetosféricas](../programa/clases/B30/B30-C22-anillo-de-corriente-y-corrientes-magnetosfericas/CLASE.md).

### Índice espacial

- Un índice espacial agrupa geometrías por cercanía para hallar rápido las de una región.

🎯 **Por qué importa (clase B14-C28):** Un archivo tiene 50 000 huellas de escenas y tu aplicación pregunta «¿qué escenas cubren este punto?» miles de veces. Recorrerlas todas cada vez desperdicia tiempo.

📘 **Dónde se aprende** (1 clase): [B14-C28 · Bases de datos espaciales](../programa/clases/B14/B14-C28-bases-de-datos-espaciales/CLASE.md).

### Índice espectral

- El índice espectral describe la ley de potencias de la energía.
- El índice espectral `α = (p − 1)/2` con `S_ν ∝ ν^{−α}`.
- El índice espectral `n_s`: `P ∝ k^(n_s − 1)`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

🎯 **Por qué importa (clase B27-C12):** El índice espectral de una fuente sincrotrón entrega el índice de energía de sus electrones; la frecuencia crítica entrega `γ²B`. Sin estas relaciones no se puede leer un espectro de radio o rayos X.

📘 **Dónde se aprende** (4 clases): [B27-C12 · Radiación sincrotrón](../programa/clases/B27/B27-C12-radiacion-sincrotron/CLASE.md); [B30-C14 · Choques y aceleración de partículas](../programa/clases/B30/B30-C14-choques-y-aceleracion-de-particulas/CLASE.md); [B40-C05 · Perturbaciones primordiales y espectro escalar](../programa/clases/B40/B40-C05-perturbaciones-primordiales-y-espectro-escalar/CLASE.md); [B51-C01 · Calibración de amplitud y escala de flujo con calibradores primarios](../programa/clases/B51/B51-C01-calibracion-de-amplitud-y-escala-de-flujo-con-calibradores-primarios/CLASE.md).

### Índice HHI

- El índice HHI es la suma de los cuadrados de las cuotas en porcentaje (0 a 10 000).

🎯 **Por qué importa (clase B125-C04):** Las empresas espaciales dependen de alianzas con socios de otros países y la clase de gobierno no explica cómo se reparte el valor ni cuánta dependencia se acepta; no está tratado. La decisión central: ¿cómo se reparte de forma justa el excedente de una alianza y cuánta dependencia de un solo socio o país es prudente?

📘 **Dónde se aprende** (1 clase): [B125-C04 · Alianzas y cooperación internacional empresarial](../programa/clases/B125/B125-C04-alianzas-y-cooperacion-internacional-empresarial/CLASE.md).

### Índice S4

- El índice S4 es la desviación típica de la potencia normalizada; la potencia sigue una gamma de forma `m = 1/S4²` (Nakagami-m).

💡 **Cómo se explica en la clase [B89-C21](../programa/clases/B89/B89-C21-efectos-ionosfericos-y-centelleo-en-senales-gnss/CLASE.md):**
- *Descripción textual:* el TEC y la frecuencia dan el retardo, que la elevación multiplica; con dos frecuencias se forma la combinación libre de ionosfera, que amplifica el ruido; el índice S4 genera el desvanecimiento por centelleo.
- 🎯 **Por qué importa:** La ionosfera es el mayor error de un receptor GNSS de una sola frecuencia y el origen de pérdidas de señal en regiones ecuatoriales y polares; sin entenderla no se puede interpretar un error de posición. La decisión central: ¿cuánto error añade la ionosfera, cómo se elimina y cuándo el centelleo hace perder la señal?

📘 **Dónde se aprende** (1 clase): [B89-C21 · Efectos ionosféricos y centelleo en señales GNSS](../programa/clases/B89/B89-C21-efectos-ionosfericos-y-centelleo-en-senales-gnss/CLASE.md).

### Índice total

- El índice de Sobol de primer orden `Sᵢ = Var(E[Y|Xᵢ])/Var(Y)` es la fracción de la varianza de `Y` explicada por `Xᵢ` sola; el índice total `S_Tᵢ` incluye además todas sus interacciones.

🎯 **Por qué importa (clase B12-C17):** Mejorar una medida cuesta dinero, masa o tiempo. Si el presupuesto de una misión ofrece mejorar la masa seca o el empuje específico, hay que saber cuál de las dos reduce más la incertidumbre del resultado.

📘 **Dónde se aprende** (1 clase): [B12-C17 · Análisis de sensibilidad](../programa/clases/B12/B12-C17-analisis-de-sensibilidad/CLASE.md).

### Inducción hacia atrás

- La inducción hacia atrás resuelve desde la última ronda.

💡 **Cómo se explica en la clase [B119-C27](../programa/clases/B119/B119-C27-diplomacia-y-comunicacion-entre-estados-ante-incidentes-espaciales/CLASE.md):**
- La inducción hacia atrás da el mismo valor.
- 🎯 **Por qué importa:** C20 simula la respuesta institucional interna; la diplomacia entre Estados no está cubierta. Esta clase aporta el razonamiento básico de negociación sin pretender describir ninguna práctica.

📘 **Dónde se aprende** (1 clase): [B119-C27 · Diplomacia y comunicación entre Estados ante incidentes espaciales](../programa/clases/B119/B119-C27-diplomacia-y-comunicacion-entre-estados-ante-incidentes-espaciales/CLASE.md).

### Inductancia crítica

- La inductancia crítica `L_c = (1−D)R/(2f)` separa ambas.

💡 **Cómo se explica en la clase [B86-C08](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md):**
- La inductancia crítica es `5,04 µH`, menor que `22 µH`: el convertidor opera en CCM.
- 🎯 **Por qué importa:** Un convertidor que reduce la tensión con un interruptor y una bobina puede ser mucho más eficiente que un regulador lineal, pero introduce rizado, ruido y pérdidas de conmutación que hay que dimensionar. La decisión central: ¿qué ciclo de trabajo, bobina y condensador dan `5 V` desde `28 V` con rizado y eficiencia aceptables?

📘 **Dónde se aprende** (1 clase): [B86-C08 · Convertidores DC-DC](../programa/clases/B86/B86-C08-convertidores-dc-dc/CLASE.md).

### Ineficiencia

- La ineficiencia es `1 − CTE`.

💡 **Cómo se explica en la clase [B44-C02](../programa/clases/B44/B44-C02-sensores-ccd/CLASE.md):**
- Una ineficiencia de `10⁻⁵` por transferencia parece despreciable, pero cuesta el 4 % en la esquina.
- 🎯 **Por qué importa:** Cada transferencia pierde una pequeña fracción de carga, y un píxel lejano se transfiere miles de veces. La decisión central: ¿qué CTE hace aceptable un sensor de 2048 × 2048?

📘 **Dónde se aprende** (1 clase): [B44-C02 · Sensores CCD](../programa/clases/B44/B44-C02-sensores-ccd/CLASE.md).

### Inercia

- La inercia es `Σ ‖xᵢ − centro(i)‖²`.
- k-medias busca `k` centroides que minimicen la inercia `Σ ‖x_i − c_{g(i)}‖²`.

💡 **Cómo se explica en la clase [B15-C23](../programa/clases/B15/B15-C23-clasificacion-no-supervisada-y-agrupamiento-de-imagenes/CLASE.md):**
- Cada paso no aumenta la inercia: asignar al más cercano la disminuye o la mantiene; recalcular la media también (la media minimiza la suma de cuadrados).
- En el laboratorio, con `σ = 0,05`, convergió en 6 iteraciones, la inercia pasó de `31,86` a `14,76` y el cambio entre iteraciones fue siempre ≤ 0.
- ⚠️ **Error frecuente:** Elegir `k` solo por la inercia. Se corrige con el ejercicio 7.
- 🎯 **Por qué importa:** Un satélite fotografía una región que nadie ha cartografiado. Sin muestras, no se puede entrenar un clasificador, pero sí se puede preguntar cuántos «tipos» de superficie distintos hay en las bandas.

📖 **Explicado a fondo:** [Masa, inercia y peso](esencial/esencial-m-z.md#masa-inercia-y-peso) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (2 clases): [B15-C23 · Clasificación no supervisada y agrupamiento de imágenes](../programa/clases/B15/B15-C23-clasificacion-no-supervisada-y-agrupamiento-de-imagenes/CLASE.md); [B17-C06 · Aprendizaje no supervisado](../programa/clases/B17/B17-C06-aprendizaje-no-supervisado/CLASE.md).

### Inercia de rueda

- La inercia de rueda `I_w` fija la velocidad `h/I_w`.

🎯 **Por qué importa (clase B87-C11):** La rueda es el actuador estándar del control fino de tres ejes. La decisión central: ¿cuánto tarda una maniobra con límites de par y de momento, y qué velocidad alcanza la rueda?

📘 **Dónde se aprende** (1 clase): [B87-C11 · Ruedas de reacción](../programa/clases/B87/B87-C11-ruedas-de-reaccion/CLASE.md).

### Inercia deseada M_d

- Amortiguamiento `B_d`: N s/m. Inercia deseada `M_d`: kg.

🎯 **Por qué importa (clase B101-C07):** Si un brazo muy rígido empuja una pieza que está 5 mm más lejos de lo que cree, aplica una fuerza grande. La decisión central: ¿qué rigidez y qué amortiguamiento le doy al extremo para que el contacto sea suave y la fuerza predecible?

📘 **Dónde se aprende** (1 clase): [B101-C07 · Control de fuerza e impedancia en manipulación](../programa/clases/B101/B101-C07-control-de-fuerza-e-impedancia-en-manipulacion/CLASE.md).

### Inercial

- Un marco inercial no rota respecto del fondo de estrellas y en él valen las leyes de Newton (S2); los demás, por ejemplo los ligados a un cuerpo, rotan o cambian de orientación con el tiempo y requieren datos para calcular su transformación (S2).

💡 **Cómo se explica en la clase [B10-C16](../programa/clases/B10/B10-C16-transformacion-de-marcos-de-referencia/CLASE.md):**
- Un objeto inmóvil en el marco inercial parece moverse en el marco giratorio con la velocidad `−ω × r`.
- En el marco inercial se mueve a `3,07 km/s`; en el giratorio, `v_rot = 0` (el laboratorio devuelve `10⁻⁹ km/s` o menos): está quieto.
- ⚠️ **Error frecuente:** Llamar «GCRS» o «inercial exacto» a un modelo simplificado. Se corrige en las secciones 8.7 y 10.
- 🎯 **Por qué importa:** Una estación terrestre tiene coordenadas fijas en la Tierra. Un satélite se propaga en un sistema inercial, donde las leyes de Newton valen.

📘 **Dónde se aprende** (1 clase): [B10-C16 · Transformación de marcos de referencia](../programa/clases/B10/B10-C16-transformacion-de-marcos-de-referencia/CLASE.md).

### Inerte

- Un inerte no reacciona (aquí N₂).

💡 **Cómo se explica en la clase [B59-C16](../programa/clases/B59/B59-C16-desechos-y-reciclaje/CLASE.md):**
- El N₂ es un inerte que se acumula o se ventea.
- 🎯 **Por qué importa:** Los residuos son una fuente de agua y de dióxido de carbono, pero también consumen oxígeno. La decisión central: ¿cuánto oxígeno cuesta cerrar el residuo y cuánta agua se recupera?

📘 **Dónde se aprende** (1 clase): [B59-C16 · Desechos y reciclaje](../programa/clases/B59/B59-C16-desechos-y-reciclaje/CLASE.md).

### Inestabilidad

- La inestabilidad por encima del umbral.

🎯 **Por qué importa (clase B34-C08):** Saber a qué altura el campo ya no sostiene al filamento sirve para anticipar erupciones. La decisión central: ¿a qué altura el decaimiento del campo supera el umbral?

📘 **Dónde se aprende** (1 clase): [B34-C08 · Erupciones de filamentos y prominencias](../programa/clases/B34/B34-C08-erupciones-de-filamentos-y-prominencias/CLASE.md).

### Inestabilidad aerodinámica

- La inestabilidad aerodinámica ocurre si el centro de presión va delante del de gravedad (`μ_α > 0`).

🎯 **Por qué importa (clase B77-C23):** Un vehículo inestable es controlable si el control es más rápido que la divergencia, pero el control a su vez fija las cargas ante rachas. La decisión central: ¿cuánto control hace falta para estabilizar un lanzador y qué ángulo de ataque deja una racha según la ganancia?

📘 **Dónde se aprende** (1 clase): [B77-C23 · Estabilidad de vuelo de lanzadores en ascenso](../programa/clases/B77/B77-C23-estabilidad-de-vuelo-de-lanzadores-en-ascenso/CLASE.md).

### Inestabilidad de corriente

- La inestabilidad de corriente es una inestabilidad lineal de la mezcla de polvo y gas en rotación que puede concentrar partículas.

💡 **Cómo se explica en la clase [B52-C04](../programa/clases/B52/B52-C04-formacion-de-planetesimales/CLASE.md):**
- Ni la sedimentación simple ni la razón de metalicidad habitual (`≈ 0,01`) llegan a esos valores; hace falta un mecanismo que concentre, por ejemplo la inestabilidad de corriente o las trampas de presión.
- Qué lo alcanza (y si el polvo conserva su coherencia al colapsar) pertenece a los modelos de inestabilidad de corriente, que aquí no se simulan.
- 🎯 **Por qué importa:** Si la autogravedad solo gana contra las mareas por encima de cierta densidad, esa densidad fija cuánto debe concentrarse el polvo. La decisión central: ¿qué densidad necesita un cúmulo de partículas para colapsar a una distancia dada?

📘 **Dónde se aprende** (1 clase): [B52-C04 · Formación de planetesimales](../programa/clases/B52/B52-C04-formacion-de-planetesimales/CLASE.md).

### Inestabilidad de sesgo

- La inestabilidad de sesgo es el mínimo de la curva.

💡 **Cómo se explica en la clase [B87-C06](../programa/clases/B87/B87-C06-giroscopios-mems/CLASE.md):**
- El mínimo es `0,633 °/h` en `τ ≈ 330 s` (la inestabilidad de sesgo).
- Hoja de datos: da ARW, inestabilidad de sesgo y densidad de ruido, a menudo con otras unidades; hay que convertirlas.
- 🎯 **Por qué importa:** Entre dos medidas de un sensor de vector, la actitud se propaga integrando el giroscopio, y esa integración se desvía. La decisión central: ¿cada cuánto hay que corregir con otro sensor, y qué parte de la deriva es ruido blanco y cuál sesgo?

📘 **Dónde se aprende** (1 clase): [B87-C06 · Giroscopios MEMS](../programa/clases/B87/B87-C06-giroscopios-mems/CLASE.md).

### Inestable

- Un sistema `y′ = A y` es asintóticamente estable si todos los autovalores tienen parte real negativa, marginalmente estable si alguno tiene parte real cero y ninguno positiva (con autovectores completos), e inestable si alguno tiene parte real positiva.
- Es inestable si algún polo tiene parte real positiva.
- Un lazo inestable crece sin cota.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B10-C09](../programa/clases/B10/B10-C09-diagonalizacion-y-estabilidad/CLASE.md):**
- Si `ζ = 0`, la parte real es 0 (marginal: oscila sin extinguirse); si `ζ = −0,02`, es `+0,0628` (inestable: la vibración crece).
- 🎯 **Por qué importa:** Un panel solar largo y delgado vibra después de una maniobra. Si la vibración se amortigua, el panel es estable; si crece, hay un problema serio.

📘 **Dónde se aprende** (4 clases): [B10-C09 · Diagonalización y estabilidad](../programa/clases/B10/B10-C09-diagonalizacion-y-estabilidad/CLASE.md); [B16-C07 · Realimentación y estabilidad](../programa/clases/B16/B16-C07-realimentacion-y-estabilidad/CLASE.md); [B88-C19 · Simulación hardware-in-the-loop](../programa/clases/B88/B88-C19-simulacion-hardware-in-the-loop/CLASE.md); [B118-C10 · Síndrome de Kessler como escenario](../programa/clases/B118/B118-C10-sindrome-de-kessler-como-escenario/CLASE.md).

### Inferencia

- Una inferencia es una conclusión que se saca de ese dato añadiendo un método o un supuesto.
- Una inferencia es una conclusión que se obtiene del dato mediante razonamiento o cálculo: «la galaxia se aleja a unos 3 000 km/s».
- Una inferencia es una conclusión que no se observa directamente.

💡 **Cómo se explica en la clase [B01-C01](../programa/clases/B01/B01-C01-naturaleza-del-universo/CLASE.md):**
- Fíjate cómo se encadenan las tres capas: Hα en 662,9 nm (observación) → `z` y `v` (inferencia) → `d` con `H₀` (modelo).
- B --> C["Inferencia: z, velocidad aparente, distancia"]
- 🎯 **Por qué importa:** Seguramente has leído que «el universo tiene 13 800 millones de años» o que «el universo observable mide 93 000 millones de años luz». Son frases que se repiten con total seguridad.

📘 **Dónde se aprende** (3 clases): [B01-C01 · Naturaleza del universo](../programa/clases/B01/B01-C01-naturaleza-del-universo/CLASE.md); [B01-C05 · Observación frente a interpretación](../programa/clases/B01/B01-C05-observacion-frente-a-interpretacion/CLASE.md); [B02-C13 · Galileo y primeras observaciones telescópicas](../programa/clases/B02/B02-C13-galileo-y-primeras-observaciones-telescopicas/CLASE.md).

### Infinita

- Si falla, hay una discontinuidad: removible (el límite existe pero no coincide con `f(a)` o `f(a)` no existe), de salto (existen ambos límites laterales y son distintos) o infinita (la función crece sin cota).

💡 **Cómo se explica en la clase [B09-C02](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md):**
- Cada tipo de discontinuidad es una razón para levantarlo: un hueco (removible), un salto de nivel (salto) o una subida al infinito (infinita).
- D --> F["Removible, de salto o infinita"]
- 🎯 **Por qué importa:** Un vehículo espacial cambia de masa de dos maneras: gradualmente, al quemar propelente, y de golpe, al soltar una etapa vacía. Un modelo de trayectoria que ignore los saltos integra mal; uno que los trate como suaves, también.

📘 **Dónde se aprende** (1 clase): [B09-C02 · Continuidad y discontinuidad](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md).

### Información de Fisher

- La información de Fisher `I(θ)` mide cuánta información sobre `θ` contienen los datos; para `N` datos independientes se suma.
- La información de Fisher suma las contribuciones de cada observable.

💡 **Cómo se explica en la clase [B15-C15](../programa/clases/B15/B15-C15-estimacion-de-parametros-senales-imagenes-y-estimacion-cientifica/CLASE.md):**
- La información de Fisher es `N/σ²`, así que la CRB es `σ²/N` y la media la alcanza.
- Paso 4 · Información de Fisher. `I = N/λ = 5/4 = 1,25`.
- 🎯 **Por qué importa:** Un telescopio recoge 100 fotones de una estrella y quieres su posición con la mayor exactitud posible. ¿Basta con promediar las posiciones?

📘 **Dónde se aprende** (2 clases): [B15-C15 · Estimación de parámetros — Señales, imágenes y estimación científica](../programa/clases/B15/B15-C15-estimacion-de-parametros-senales-imagenes-y-estimacion-cientifica/CLASE.md); [B74-C17 · Navegación en espacio profundo](../programa/clases/B74/B74-C17-navegacion-en-espacio-profundo/CLASE.md).

### Información JᵀJ

- Degeneración: entorno que no determina alguna dirección del movimiento. Información `JᵀJ`: matriz cuyos autovalores miden la certeza por dirección.

🎯 **Por qué importa (clase B99-C07):** Un estimador que funciona en el laboratorio puede fallar sin avisar cuando el entorno empeora. La decisión central: ¿qué estimador usar, cómo detectar que el entorno no determina el movimiento y cuándo dejar de confiar en el mapa?

📘 **Dónde se aprende** (1 clase): [B99-C07 · Robustez del mapeo ante entornos degradados](../programa/clases/B99/B99-C07-robustez-del-mapeo-ante-entornos-degradados/CLASE.md).

### Información mutua

- La información mutua es la reducción de entropía.

💡 **Cómo se explica en la clase [B119-C32](../programa/clases/B119/B119-C32-interpretacion-de-tratados-internacionales/CLASE.md):**
- Entropía marginal `H(X) = 1.829` bits; condicional `1.737`; información mutua `0.092` bits: conocer las condiciones reduce la incertidumbre.
- 🎯 **Por qué importa:** B119 enseña los tratados y su contenido, no el método para interpretarlos, que el rol de derecho espacial exige; la regla general de interpretación se menciona como conocimiento no verificado. La decisión central: ¿cuánta ambigüedad queda en una cláusula y qué fuentes de interpretación la reducen más?

📘 **Dónde se aprende** (1 clase): [B119-C32 · Interpretación de tratados internacionales](../programa/clases/B119/B119-C32-interpretacion-de-tratados-internacionales/CLASE.md).

### Información Ω_ij

- Medida `z_ij`: pose relativa medida entre `i` y `j`. Información `Ω_ij`: inversa de la covarianza de la medida.

🎯 **Por qué importa (clase B99-C03):** Sumar movimientos da una trayectoria que no cierra el lazo; una medida de cierre de bucle dice que la pose final es la inicial. La decisión central: ¿cómo repartir el desacuerdo entre cientos de poses de modo coherente con la incertidumbre de cada medida?

📘 **Dónde se aprende** (1 clase): [B99-C03 · SLAM basado en grafos de poses](../programa/clases/B99/B99-C03-slam-basado-en-grafos-de-poses/CLASE.md).

### Informe Belmont

- El informe Belmont nombra tres principios: respeto por las personas (autonomía y protección de quienes tienen autonomía disminuida), beneficencia (no dañar y maximizar beneficios) y justicia (reparto equitativo de cargas y beneficios).

💡 **Cómo se explica en la clase [B105-C19](../programa/clases/B105/B105-C19-bioetica-en-investigacion-tripulada/CLASE.md):**
- Un resumen de búsqueda web (2026-11-10) del informe Belmont indica tres principios: respeto por las personas (voluntariedad e información adecuada; protección de quienes tienen autonomía disminuida), beneficencia (no dañar y maximizar beneficios minimizando daños) y justicia (quién carga con los riesgos y quién recibe los beneficios).
- Los tres principios del informe Belmont (respeto por las personas, beneficencia, justicia) se consultaron solo por un resumen de búsqueda web (2026-11-10).
- 🎯 **Por qué importa:** No basta con quitar el nombre: con edad, sexo, profesión y misión, una persona de una cohorte de 6 suele ser única. La decisión central: ¿qué se puede publicar de una cohorte pequeña sin identificar a nadie y cuánta utilidad se pierde al protegerla?

📘 **Dónde se aprende** (1 clase): [B105-C19 · Bioética en investigación tripulada](../programa/clases/B105/B105-C19-bioetica-en-investigacion-tripulada/CLASE.md).

### Informe de árbitro

- Un informe de árbitro reúne un resumen del trabajo, comentarios mayores y menores y una recomendación.

🎯 **Por qué importa (clase B20-C03):** Una crítica recibida a las once de la noche se lee con el estómago antes que con la cabeza. La reacción inmediata, defenderse o rendirse, suele empeorar el trabajo y la relación con quien revisa.

📘 **Dónde se aprende** (1 clase): [B20-C03 · Revisión por pares y respuesta a árbitros](../programa/clases/B20/B20-C03-revision-por-pares-y-respuesta-a-arbitros/CLASE.md).

### Informe de cierre

- Un informe de cierre resume resultados, desviaciones y aprendizajes.

💡 **Cómo se explica en la clase [B08-C20](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md):**
- El informe de cierre describe qué se hizo, qué se midió (con su procedencia), qué se desvió del plan y qué se aprende.
- 🎯 **Por qué importa:** Una salida sin plan termina en una noche perdida o en un accidente. La pregunta motivadora: ¿cómo preparo una salida de observación para que sea segura, útil, accesible y reproducible?

📘 **Dónde se aprende** (1 clase): [B08-C20 · Proyecto de campaña de observación nocturna](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md).

### Informe de desviaciones

- Un informe de desviaciones las lista con motivo y efecto.

🎯 **Por qué importa (clase B14-C24):** Seis meses después de un análisis, nadie recuerda por qué se excluyeron tres puntos ni cuándo se cambió el modelo. Y un revisor pregunta si la exclusión estaba prevista.

📘 **Dónde se aprende** (1 clase): [B14-C24 · Documentación de hipótesis y decisiones de análisis](../programa/clases/B14/B14-C24-documentacion-de-hipotesis-y-decisiones-de-analisis/CLASE.md).

### Informe de errores

- El informe de errores lista lo que falla.

🎯 **Por qué importa (clase B28-C17):** Un catálogo sin identificadores estables, versiones ni huellas no se puede citar ni auditar. La decisión central: ¿cómo se guarda un evento para que se pueda verificar, actualizar y cruzar con otros?

📘 **Dónde se aprende** (1 clase): [B28-C17 · Archivos de eventos multimensajero](../programa/clases/B28/B28-C17-archivos-de-eventos-multimensajero/CLASE.md).

### Informe final

- El informe final cierra el caso.

💡 **Cómo se explica en la clase [B122-C08](../programa/clases/B122/B122-C08-comunicacion-de-crisis-con-operadores-autoridades-y-publico/CLASE.md):**
- Informe final: un mes tras el envío, `2026-04-08 20:00 UTC`.
- N --> F["informe final: 1 mes tras enviar la notificacion"]
- ⚠️ **Error frecuente:** Contar el informe final desde el conocimiento. Se cuenta desde el envío de la notificación; ver 8.1.
- 🎯 **Por qué importa:** B124-C18 trata divulgación; la comunicación de crisis con mensajes oportunos no está cubierta. La decisión central: ¿qué hay que comunicar, a quién y antes de qué plazo?

📘 **Dónde se aprende** (1 clase): [B122-C08 · Comunicación de crisis con operadores, autoridades y público](../programa/clases/B122/B122-C08-comunicacion-de-crisis-con-operadores-autoridades-y-publico/CLASE.md).

### Informe integrado

- Un informe integrado reúne datos, modelo, resultados, verificación y límites.

🎯 **Por qué importa (clase B05-C20):** Un problema real no viene etiquetado «esto es de energía» o «esto es de momento». La pregunta motivadora es: ¿cómo planteo, resuelvo y valido un problema físico completo, eligiendo el modelo correcto para cada parte y declarando dónde dejan de valer?

📘 **Dónde se aprende** (1 clase): [B05-C20 · Problema físico integrado de satélite ideal](../programa/clases/B05/B05-C20-problema-fisico-integrado-de-satelite-ideal/CLASE.md).

### Informe reproducible

- Un informe reproducible es el generado desde los resultados y registrado con su huella (C07).

🎯 **Por qué importa (clase B23-C08):** Un conjunto de pruebas que pasan no es un informe. Quien debe decidir si usar el código necesita saber para qué uso se evaluó, con qué criterios, qué falló y qué no se probó.

📘 **Dónde se aprende** (1 clase): [B23-C08 · Informe de verificación y validación](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md).

### Infrarrojo térmico

- Una banda de infrarrojo medio (3,9 µm) es muy sensible a temperaturas altas; la de infrarrojo térmico (11 µm) lo es al fondo.

🎯 **Por qué importa (clase B57-C16):** Un incendio pequeño puede ser un desastre en horas, pero un píxel mide cientos de metros. La decisión central: ¿cuál es la fracción de píxel más pequeña que se puede detectar y cuánto sesga la estimación un error en el fondo?

📘 **Dónde se aprende** (1 clase): [B57-C16 · Incendios forestales](../programa/clases/B57/B57-C16-incendios-forestales/CLASE.md).

### Infrarrojo terrestre

- El infrarrojo terrestre es la emisión propia del planeta, `M_IR = σ T_BB⁴`.

💡 **Cómo se explica en la clase [B85-C01](../programa/clases/B85/B85-C01-balance-radiativo-de-satelite/CLASE.md):**
- Descripción larga: el caso caliente supera al frío en unos 60 K con estos datos; el infrarrojo terrestre aporta más que el albedo y la disipación interna es el término menor.
- 🎯 **Por qué importa:** Las temperaturas de una nave no se miden primero: se predicen con un balance de energía. Un error de 30 K en el equilibrio decide si una batería sobrevive.

📘 **Dónde se aprende** (1 clase): [B85-C01 · Balance radiativo de satélite](../programa/clases/B85/B85-C01-balance-radiativo-de-satelite/CLASE.md).

### Ingreso diferido

- El ingreso diferido es lo cobrado y aún no reconocido.

💡 **Cómo se explica en la clase [B125-C02](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md):**
- Se cobran `120 000` u.m. en el mes 1; el ingreso reconocido es `10 000` por mes y el ingreso diferido al final del mes `m` es `120 000 − 10 000 m`: `110 000` en el mes 1 y `0` en el 12.
- 🎯 **Por qué importa:** El modelo de ingresos define cuándo entra el dinero y cuánto vale un cliente; ninguna clase anterior lo trata. La decisión central: ¿cuánto vale un cliente de suscripción, cuándo se reconoce su ingreso y cuánto abandono puede tolerar el negocio?

📘 **Dónde se aprende** (1 clase): [B125-C02 · Modelos de ingresos: suscripción y servicio](../programa/clases/B125/B125-C02-modelos-de-ingresos-suscripcion-y-servicio/CLASE.md).

### Ingreso por cliente

- El ingreso por cliente `R(P)` es el precio por la probabilidad de compra.

💡 **Cómo se explica en la clase [B125-C01](../programa/clases/B125/B125-C01-mercado-de-datos-espaciales/CLASE.md):**
- El ejemplo conductor es sintético: 10 000 clientes con DAP uniforme en `[0, 100]` u.m. por mes; sin sustituto el precio óptimo es `50` y el ingreso por cliente `25`; con un sustituto que cubre el 80 % del valor, `10` y `5`.
- 🎯 **Por qué importa:** [B124](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) trata los segmentos de la industria en general; ninguna clase explica por qué un dato crudo puede valer cero y aun así sostener empresas.

📘 **Dónde se aprende** (1 clase): [B125-C01 · Mercado de datos espaciales](../programa/clases/B125/B125-C01-mercado-de-datos-espaciales/CLASE.md).

### Inhibidor

- Un inhibidor es un dispositivo físico entre una fuente de energía y un peligro.
- El inhibidor es un dispositivo físico que impide la liberación.

💡 **Cómo se explica en la clase [B95-C01](../programa/clases/B95/B95-C01-unidad-cubesat-dimensiones-y-formatos/CLASE.md):**
- ⚠️ **Error frecuente:** Contar el temporizador como inhibidor. Se corrige con 8.4.
- 🎯 **Por qué importa:** Un CubeSat que no cumple el estándar no entra en el dispensador, aunque funcione perfectamente. La decisión central: ¿esta configuración cabe, pesa y se equilibra dentro de lo que el estándar permite, y cuándo puede encenderse, desplegar y transmitir?

📘 **Dónde se aprende** (2 clases): [B95-C01 · Unidad CubeSat, dimensiones y formatos](../programa/clases/B95/B95-C01-unidad-cubesat-dimensiones-y-formatos/CLASE.md); [B95-C04 · Antenas desplegables para satélites pequeños](../programa/clases/B95/B95-C04-antenas-desplegables-para-satelites-pequenos/CLASE.md).

### Inicio múltiple

- El inicio múltiple protege de mínimos locales.

🎯 **Por qué importa (clase B29-C09):** La excentricidad y el argumento del periastro cambian la forma de la curva y el sesgo de `K` que vimos en C03. Y la densidad de la estrella que sale del tránsito ayuda a validar al anfitrión.

📘 **Dónde se aprende** (1 clase): [B29-C09 · Parámetros orbitales exoplanetarios](../programa/clases/B29/B29-C09-parametros-orbitales-exoplanetarios/CLASE.md).

### Inlier / atípico

- RANSAC: ajusta con muestras mínimas aleatorias y se queda con el modelo de más inliers. Inlier / atípico: correspondencia consistente / inconsistente con el modelo.

🎯 **Por qué importa (clase B99-C01):** Una trayectoria se obtiene sumando movimientos pequeños, y cada uno trae un error; esos errores no se corrigen solos. La decisión central: ¿con qué calidad de correspondencias y de medida puedo confiar en la odometría, y cuándo necesito corregirla con cierres de bucle (C04)?

📘 **Dónde se aprende** (1 clase): [B99-C01 · Odometría visual](../programa/clases/B99/B99-C01-odometria-visual/CLASE.md).

### Inmutable

- Una tupla es una secuencia ordenada e inmutable, entre paréntesis (S3).

🎯 **Por qué importa (clase B07-C07):** Una tabla de ocho planetas con tres propiedades cada uno son 24 datos: no cabe en 24 variables sueltas. Necesitas estructuras que agrupen datos, permitan recorrerlos y los mantengan ordenados y consultables.

📘 **Dónde se aprende** (1 clase): [B07-C07 · Listas y estructuras de datos](../programa/clases/B07/B07-C07-listas-y-estructuras-de-datos/CLASE.md).

### Innovación

- La innovación es `ỹ = z − H x⁻`; su covarianza es `S = H P⁻ Hᵀ + R`.
- La innovación es `y − H x̂⁻`.
- La innovación es la medición menos la predicha.

💡 **Cómo se explica en la clase [B15-C17](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md):**
- La innovación normalizada `ỹ²/S` sigue una distribución `χ²` con 1 grado de libertad si todo está bien.
- Una medida que da una innovación de 50 m con `S = 51 m²` tiene `ỹ²/S = 49`, y se rechaza.
- 🎯 **Por qué importa:** Un radar mide la distancia a un objeto cada segundo, con 5 m de ruido. Si solo usas la última medida, tu error es de 5 m.

📘 **Dónde se aprende** (3 clases): [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md); [B74-C08 · Filtrado recursivo de estados](../programa/clases/B74/B74-C08-filtrado-recursivo-de-estados/CLASE.md); [B80-C04 · Fusión inercial con mediciones externas (acoplamiento débil y fuerte)](../programa/clases/B80/B80-C04-fusion-inercial-con-mediciones-externas-acoplamiento-debil-y-fuerte/CLASE.md).

### Inocuidad

- La inocuidad es la ausencia de peligros que dañen a quien consume.

🎯 **Por qué importa (clase B115-C07):** Una contaminación en un circuito compartido afecta a todos los lotes a la vez. La decisión central: ¿con qué frecuencia se muestrea, qué se mide y qué barreras (desinfección, lavado, temperatura) hacen falta para que una contaminación se detecte antes de llegar a un nivel de acción?

📘 **Dónde se aprende** (1 clase): [B115-C07 · Bioseguridad e inocuidad alimentaria en hábitats](../programa/clases/B115/B115-C07-bioseguridad-e-inocuidad-alimentaria-en-habitats/CLASE.md).

### Inserción en órbita lunar (LOI)

- La inserción en órbita lunar (LOI) es el impulso en el perilune de la hipérbola.

🎯 **Por qué importa (clase B76-C07):** Un diseño preliminar de misión empieza por el presupuesto de velocidad. La decisión central: ¿cuánto `Δv` cuestan la salida de la Tierra y la captura en la Luna, y cuánto cambia la segunda según la órbita lunar elegida?

📘 **Dónde se aprende** (1 clase): [B76-C07 · Maniobras de inserción cislunar](../programa/clases/B76/B76-C07-maniobras-de-insercion-cislunar/CLASE.md).

### Insesgado

- El sesgo de un estimador es `E[θ̂] − θ`; es insesgado si vale cero.
- Es insesgado si `q > 0` donde `h p ≠ 0`.

💡 **Cómo se explica en la clase [B12-C07](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md):**
- La cota de Cramér–Rao —que fija la menor varianza posible de un estimador insesgado— coincide con `λ/n` para este modelo: la media es el mejor estimador insesgado posible.
- Repitiendo el experimento 200 000 veces con `λ = 4` y `n = 10`, la varianza del MLE es `0,4009` (teórica `0,4000`) y su sesgo `+0,0007`: insesgado.
- ⚠️ **Error frecuente:** Creer que un estimador insesgado siempre es mejor. Se corrige con 8.6 y el ejercicio 11.
- 🎯 **Por qué importa:** Una misión no «conoce» la tasa de impactos ni el ruido de su sensor: los estima a partir de unas decenas de datos. Un estimador mal elegido, o mal interpretado, da parámetros sesgados o con una confianza injustificada.

📘 **Dónde se aprende** (2 clases): [B12-C07 · Estimación de parámetros](../programa/clases/B12/B12-C07-estimacion-de-parametros/CLASE.md); [B12-C15 · Muestreo de importancia](../programa/clases/B12/B12-C15-muestreo-de-importancia/CLASE.md).

### Insolación diaria media

- La insolación diaria media `Q` es el promedio de 24 h en una latitud.

🎯 **Por qué importa (clase B54-C12):** La radiación solar es la fuente de energía de todo el bloque. La pregunta motivadora: ¿cuánta energía llega a un punto y cuánta alcanza el suelo?

📘 **Dónde se aprende** (1 clase): [B54-C12 · Interacción con radiación solar](../programa/clases/B54/B54-C12-interaccion-con-radiacion-solar/CLASE.md).

### Instalación

- La instalación `S` es la irradiancia que recibe el planeta.

💡 **Cómo se explica en la clase [B54-C17](../programa/clases/B54/B54-C17-clima-exoplanetario/CLASE.md):**
- Para `L = 0,05 L☉`, la instalación del borde interno solar se da a `0,221 UA` y la del externo a `0,380 UA`.
- *Descripción textual:* la luminosidad y la distancia dan la instalación; con albedo y redistribución se obtiene `T_e`, que se compara con las instalaciones solares de los bordes.
- 🎯 **Por qué importa:** La temperatura de equilibrio de un exoplaneta es el primer número que se calcula. La pregunta motivadora: ¿cuánto cambia esa temperatura si el calor se redistribuye o no?

📘 **Dónde se aprende** (1 clase): [B54-C17 · Clima exoplanetario](../programa/clases/B54/B54-C17-clima-exoplanetario/CLASE.md).

### Instalación relativa

- La instalación relativa es `S/S_Tierra`.

🎯 **Por qué importa (clase B54-C20):** Comparar mundos tienta a ordenarlos por «habitabilidad». La pregunta motivadora: ¿qué dicen realmente la temperatura y la presión de superficie sobre la posibilidad de agua líquida?

📘 **Dónde se aprende** (1 clase): [B54-C20 · Comparación de habitabilidad climática](../programa/clases/B54/B54-C20-comparacion-de-habitabilidad-climatica/CLASE.md).

### Instante del máximo

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B29-C16):** El estiramiento de la curva de luz es una de las magnitudes con que se estandarizan las supernovas de tipo Ia para medir distancias. Saber con qué precisión se recupera guía la planificación de observaciones.

📘 **Dónde se aprende** (1 clase): [B29-C16 · Supernovas y curvas de luz](../programa/clases/B29/B29-C16-supernovas-y-curvas-de-luz/CLASE.md).

### Instante inicial

- El instante inicial es `t₀`.

🎯 **Por qué importa (clase B11-C02):** Una nave no sigue «la» solución de las ecuaciones del movimiento: sigue la que corresponde a *su* posición y velocidad en el instante en que se midieron. Saber cuántos datos exige la ecuación, cuándo garantizan una única trayectoria y cuánto se amplifica su error es la base de toda predicción de trayectoria.

📘 **Dónde se aprende** (1 clase): [B11-C02 · Problemas de valor inicial](../programa/clases/B11/B11-C02-problemas-de-valor-inicial/CLASE.md).

### Instante inválido

- Un instante inválido es una fecha que no existe, como `23:59:60` donde no se insertó un segundo.

🎯 **Por qué importa (clase B13-C09):** Una nave graba un evento a las `23:59:59` del 31 de diciembre de 2016 y otro a las `00:00:00` del 1 de enero de 2017. ¿Cuánto tiempo pasó?

📘 **Dónde se aprende** (1 clase): [B13-C09 · Segundos intercalares y cronología](../programa/clases/B13/B13-C09-segundos-intercalares-y-cronologia/CLASE.md).

### Instrumento

- Un instrumento es un dispositivo para medir la posición del Sol, la Luna o las estrellas; un gnomon es una varilla vertical que proyecta sombra, y un cuadrante mide ángulos con un arco.
- El instrumento es la norma o acto que la cumple.

💡 **Cómo se explica en la clase [B02-C04](../programa/clases/B02/B02-C04-astronomia-de-india-china-y-mundo-islamico/CLASE.md):**
- Los tres casos usan evidencia de tipo distinto: un registro (supernova), un instrumento (Jantar Mantar) y una institución (Maraga).
- Para cada tradición necesitas distinguir qué tipo de evidencia tienes: un registro (qué se vio y cuándo), un instrumento (con qué se midió) y un texto de método (cómo se calculó).
- 🎯 **Por qué importa:** Contar la historia de la astronomía como una línea recta de Grecia a Europa deja fuera lo que otras sociedades observaron, calcularon y construyeron. La pregunta motivadora es: ¿qué sabemos con precisión de estas tradiciones, qué falta y cómo evitar contar la historia desde un solo lado?

📘 **Dónde se aprende** (2 clases): [B02-C04 · Astronomía de India, China y mundo islámico](../programa/clases/B02/B02-C04-astronomia-de-india-china-y-mundo-islamico/CLASE.md); [B121-C04 · Marco legal espacial en Chile](../programa/clases/B121/B121-C04-marco-legal-espacial-en-chile/CLASE.md).

### Instrumento radiométrico

- Un instrumento radiométrico mide la intensidad de esta radiación.

🎯 **Por qué importa (clase B26-C15):** El fondo de microondas es la reliquia más antigua observable y da los parámetros del modelo cosmológico. Entender su espectro de cuerpo negro permite calibrar un instrumento, estimar el contenido de fotones y comprender por qué un solo número, la razón barión–fotón, resume tanta física.

📘 **Dónde se aprende** (1 clase): [B26-C15 · Radiación cósmica de fondo](../programa/clases/B26/B26-C15-radiacion-cosmica-de-fondo/CLASE.md).

### Integración

- Ensamblaje: unir piezas mecánicamente. Integración: unir elementos y comprobar que interactúan como se espera.

💡 **Cómo se explica en la clase [B90-C01](../programa/clases/B90/B90-C01-plan-de-ensamblaje-e-integracion/CLASE.md):**
- El *Systems Engineering Handbook* de NASA (F3) dice que el propósito de la integración es asegurar que los elementos funcionen como un todo, que se construye de abajo hacia arriba y que cada nivel se comprueba antes de unirse al superior.
- *Descripción textual:* la integración avanza de recepción a estructura, de allí a potencia y a computador/comunicaciones, luego a control de actitud y carga útil, y todo converge en la prueba funcional, seguida de vibración, termovacío, prueba posensayo y cierre.
- 🎯 **Por qué importa:** La integración es la fase donde los errores de diseño se vuelven visibles y caros. Un plan que no distingue las tareas críticas de las que tienen holgura gasta esfuerzo en el lugar equivocado.

📘 **Dónde se aprende** (1 clase): [B90-C01 · Plan de ensamblaje e integración](../programa/clases/B90/B90-C01-plan-de-ensamblaje-e-integracion/CLASE.md).

### Integración condicional

- La integración condicional (*clamping*) detiene la integral cuando hay saturación y el error tiene el mismo signo.

💡 **Cómo se explica en la clase [B16-C18](../programa/clases/B16/B16-C18-saturacion-y-anti-windup/CLASE.md):**
- Integración condicional (detener la integral si hay saturación y el error empuja hacia más saturación): sin parámetros, pero con transiciones bruscas.
- 🎯 **Por qué importa:** Una rueda de reacción entrega un par máximo y almacena un momento angular máximo (el Hubble usa ruedas de hasta unas 3000 rpm, y magnetopares para gestionar su velocidad, S1). Cuando el controlador pide más de lo que el actuador puede dar, el lazo deja de comportarse como se diseñó.

📘 **Dónde se aprende** (1 clase): [B16-C18 · Saturación y anti-windup](../programa/clases/B16/B16-C18-saturacion-y-anti-windup/CLASE.md).

### Integración iterada

- Una integral doble `∬_D f dA` suma `f` sobre una región `D` del plano; se calcula por integración iterada `∫∫ f dx dy` (S1, §1.5(v), ecs. 1.5.27 y 1.5.31).

🎯 **Por qué importa (clase B09-C18):** La masa de la Tierra se conoce mucho mejor que la distribución de esa masa en su interior. Un solo número, la densidad media, no basta: el momento de inercia depende de cómo se reparte la masa.

📘 **Dónde se aprende** (1 clase): [B09-C18 · Integrales dobles y triples](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md).

### Integración numérica

- La integración numérica de la ecuación de velocidad aproxima la solución con pasos de tiempo finitos.

💡 **Cómo se explica en la clase [B06-C14](../programa/clases/B06/B06-C14-cinetica-quimica-inicial/CLASE.md):**
- La integración numérica es la herramienta general (B11); la solución analítica sirve de prueba.
- Paso 5 · Integración numérica. RK4 con `kΔt = 0,01` da `0,031250` frente a `0,031250` analítico.
- 🎯 **Por qué importa:** Que una reacción sea posible (energía favorable, `K` grande) no significa que ocurra: puede ser tan lenta que no ocurra nunca en la edad del universo. En una nube molecular a 10 K, la energía térmica es de apenas 0,86 meV (C10).

📘 **Dónde se aprende** (1 clase): [B06-C14 · Cinética química inicial](../programa/clases/B06/B06-C14-cinetica-quimica-inicial/CLASE.md).

### Integración por partes

- La integración por partes dice que `∫ u dv = u v − ∫ v du` (S1, §1.4(iv), ec. 1.4.16).

💡 **Cómo se explica en la clase [B09-C10](../programa/clases/B09/B09-C10-integracion-por-partes/CLASE.md):**
- Pasar un término al otro lado es la integración por partes.
- 🎯 **Por qué importa:** Un detector cuenta fotones que llegan al azar. Cuánto hay que esperar, en promedio, entre uno y el siguiente, y cuánto varía esa espera, decide el tiempo de exposición, el tiempo muerto aceptable y el ruido.

📘 **Dónde se aprende** (1 clase): [B09-C10 · Integración por partes](../programa/clases/B09/B09-C10-integracion-por-partes/CLASE.md).

### Integración reducida

- La integración reducida evalúa el cortante en un punto.

🎯 **Por qué importa (clase B84-C27):** Una viga corta modelada con Euler subestima la flecha en 17 %; no es un error de malla sino de hipótesis. La decisión central: ¿para qué esbeltez es válido el elemento de Euler y cuándo hace falta cortante?

📘 **Dónde se aprende** (1 clase): [B84-C27 · Tipos de elementos finitos: viga, placa y sólido](../programa/clases/B84/B84-C27-tipos-de-elementos-finitos-viga-placa-y-solido/CLASE.md).

### Integrador

- Un integrador avanza el estado en pasos `dt`.
- El integrador `u[n] = u[n−1] + g e[n−D]`.

💡 **Cómo se explica en la clase [B42-C16](../programa/clases/B42/B42-C16-lazo-de-control-de-optica-adaptativa/CLASE.md):**
- *Descripción textual:* un integrador con retardo rechaza perturbaciones lentas, amplifica las rápidas y es estable solo bajo cierta ganancia.
- 🎯 **Por qué importa:** El lazo decide qué tan rápido es el rechazo y cuánto ruido se amplifica. La decisión central: ¿qué ganancia da el mejor compromiso entre rechazo, ruido y estabilidad con retardo?

📘 **Dónde se aprende** (2 clases): [B07-C20 · Primer simulador de un movimiento celeste](../programa/clases/B07/B07-C20-primer-simulador-de-un-movimiento-celeste/CLASE.md); [B42-C16 · Lazo de control de óptica adaptativa](../programa/clases/B42/B42-C16-lazo-de-control-de-optica-adaptativa/CLASE.md).

### Integrador de Boris

- El integrador de Boris separa la aceleración eléctrica y la rotación magnética.

🎯 **Por qué importa (clase B30-C06):** El movimiento de las partículas explica cómo se atrapan en los cinturones, cómo derivan y cómo se aceleran. La decisión central: ¿cuándo queda atrapada una partícula y cuánto vale su radio de giro?

📘 **Dónde se aprende** (1 clase): [B30-C06 · Partículas cargadas y movimientos](../programa/clases/B30/B30-C06-particulas-cargadas-y-movimientos/CLASE.md).

### Integrador independiente

- Un integrador independiente no comparte fórmulas con el sistema bajo prueba.

💡 **Cómo se explica en la clase [B71-C20](../programa/clases/B71/B71-C20-propagador-kepleriano-verificable/CLASE.md):**
- *Descripción textual:* los elementos se propagan con Kepler; seis pruebas con tolerancias fijadas de antemano decidieron si se acepta; la mutación demuestra que la comparación con un integrador independiente detecta lo que los invariantes no.
- 🎯 **Por qué importa:** Un propagador que «parece funcionar» puede tener un error de tiempo que ningún invariante detecta. La decisión central: ¿qué pruebas, con qué tolerancias y contra qué referencia independiente demuestran que el propagador es correcto?

📘 **Dónde se aprende** (1 clase): [B71-C20 · Propagador kepleriano verificable](../programa/clases/B71/B71-C20-propagador-kepleriano-verificable/CLASE.md).

### Integrador leapfrog

- El integrador leapfrog es simpléctico de segundo orden.

🎯 **Por qué importa (clase B38-C05):** Toda simulación de estrellas necesita una fuerza. La decisión central: ¿qué potencial simple reproduce una curva de rotación plana y cuánto aporta cada componente?

📘 **Dónde se aprende** (1 clase): [B38-C05 · Potenciales galácticos: Plummer, Miyamoto-Nagai y NFW](../programa/clases/B38/B38-C05-potenciales-galacticos-plummer-miyamoto-nagai-y-nfw/CLASE.md).

### Integral de Fermi–Dirac

- La integral de Fermi–Dirac `F_j(η) = ∫ x^j/(1 + e^{x−η}) dx`.

💡 **Cómo se explica en la clase [B37-C02](../programa/clases/B37/B37-C02-ecuaciones-de-estado-estelares-gas-ideal-radiacion-y-degeneracion/CLASE.md):**
- *Descripción textual:* se suman las presiones de iones, radiación y electrones, y estos últimos se obtienen de la integral de Fermi–Dirac.
- 🎯 **Por qué importa:** La estructura depende de `P(ρ, T, composición)`. La decisión central: ¿qué término domina en cada estado y cuándo deja de valer el gas ideal?

📘 **Dónde se aprende** (1 clase): [B37-C02 · Ecuaciones de estado estelares: gas ideal, radiación y degeneración](../programa/clases/B37/B37-C02-ecuaciones-de-estado-estelares-gas-ideal-radiacion-y-degeneracion/CLASE.md).

### Integral de línea

- La integral de línea `∫_C F·dr` suma la componente tangencial a lo largo de una curva (ec. 1.6.38).

💡 **Cómo se explica en la clase [B09-C19](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md):**
- A --> F["∇×F = 0 → F = ∇f<br/>integral de línea sin camino"]
- 🎯 **Por qué importa:** La gravedad no tiene fuentes fuera de la masa que la produce, y eso permite calcular la gravedad de un planeta esférico sin sumar cada átomo: basta medir el flujo. La rotación de la Tierra produce un campo de velocidades con circulación no nula, y esa circulación mide cuánto «gira» el campo.

📘 **Dónde se aprende** (1 clase): [B09-C19 · Cálculo vectorial introductorio](../programa/clases/B09/B09-C19-calculo-vectorial-introductorio/CLASE.md).

### Integral de Planck

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B31-C06](../programa/clases/B31/B31-C06-estadisticas-cuanticas/CLASE.md):**
- *Descripción textual:* las tres distribuciones dependen de `x`; la de bosones da la integral de Planck y las constantes `σ` y `b`, que se comparan con NIST; la de fermiones da la energía de Fermi.
- 🎯 **Por qué importa:** La radiación de las estrellas y la presión de degeneración de los remanentes estelares dependen de estas estadísticas. La decisión central: ¿qué distribución usar y qué constantes se derivan?

📘 **Dónde se aprende** (1 clase): [B31-C06 · Estadísticas cuánticas](../programa/clases/B31/B31-C06-estadisticas-cuanticas/CLASE.md).

### Integral definida

- La integral definida `∫_a^b f(x) dx` es el límite de las sumas de Riemann `Σ f(x_i*) Δx` cuando `Δx → 0` (S1, §1.4(v)).

🎯 **Por qué importa (clase B09-C11):** Un motor entrega una aceleración que cambia con el tiempo; la maniobra cambia la velocidad del vehículo en la integral de esa aceleración durante el encendido. Los datos llegan como muestras de un acelerómetro, no como una fórmula.

📘 **Dónde se aprende** (1 clase): [B09-C11 · Integrales definidas](../programa/clases/B09/B09-C11-integrales-definidas/CLASE.md).

### Integral diaria de luz (DLI)

- La integral diaria de luz (DLI) es su suma en un día (mol m⁻² d⁻¹).

🎯 **Por qué importa (clase B115-C02):** La luz es el mayor consumo eléctrico de un cultivo cerrado. La decisión central: ¿cuántos fotones por metro cuadrado y día hacen falta, con qué eficacia se producen y qué potencia y calor suponen para el hábitat?

📘 **Dónde se aprende** (1 clase): [B115-C02 · Iluminación de cultivos con LED y espectro de crecimiento](../programa/clases/B115/B115-C02-iluminacion-de-cultivos-con-led-y-espectro-de-crecimiento/CLASE.md).

### Integral doble

- Una integral doble `∬_D f dA` suma `f` sobre una región `D` del plano; se calcula por integración iterada `∫∫ f dx dy` (S1, §1.5(v), ecs. 1.5.27 y 1.5.31).

🎯 **Por qué importa (clase B09-C18):** La masa de la Tierra se conoce mucho mejor que la distribución de esa masa en su interior. Un solo número, la densidad media, no basta: el momento de inercia depende de cómo se reparte la masa.

📘 **Dónde se aprende** (1 clase): [B09-C18 · Integrales dobles y triples](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md).

### Integral impropia

- Una integral impropia tiene un límite infinito; se define como `lim_{b→∞} ∫_a^b`.

💡 **Cómo se explica en la clase [B09-C12](../programa/clases/B09/B09-C12-teorema-fundamental-del-calculo/CLASE.md):**
- Con un cambio de variable `u = 1/r`: la integral impropia se vuelve finita (`∫_0^{1/R} GM du`).
- 🎯 **Por qué importa:** Para que una sonda abandone la Tierra hay que darle energía suficiente para vencer la gravedad hasta una distancia infinita. Esa energía es una integral de la fuerza sobre una distancia sin cota superior.

📘 **Dónde se aprende** (1 clase): [B09-C12 · Teorema fundamental del cálculo](../programa/clases/B09/B09-C12-teorema-fundamental-del-calculo/CLASE.md).

### Integral indefinida

- La integral indefinida `∫ f(x) dx` es la familia de todas las antiderivadas: `F(x) + C` (S1, §1.4(iv)).

🎯 **Por qué importa (clase B09-C08):** Un acelerómetro mide aceleración; lo que se necesita es velocidad y posición. Una gravedad `g(r)` se conoce; lo que decide si una sonda escapa es la energía, que sale de «deshacer» esa derivada.

📘 **Dónde se aprende** (1 clase): [B09-C08 · Integrales indefinidas](../programa/clases/B09/B09-C08-integrales-indefinidas/CLASE.md).

### Integral I²t

- La integral `I²t` mide la energía de fusión.

🎯 **Por qué importa (clase B86-C10):** Si el fusible aguas arriba se funde antes que el de la rama averiada, un fallo local deja sin energía a toda la nave. Una protección bien coordinada aísla la rama y conserva el resto.

📘 **Dónde se aprende** (1 clase): [B86-C10 · Protección contra sobrecorriente](../programa/clases/B86/B86-C10-proteccion-contra-sobrecorriente/CLASE.md).

### Integral triple

- Una integral triple `∭_V f dV` lo hace sobre un volumen (ec. 1.5.37).

🎯 **Por qué importa (clase B09-C18):** La masa de la Tierra se conoce mucho mejor que la distribución de esa masa en su interior. Un solo número, la densidad media, no basta: el momento de inercia depende de cómo se reparte la masa.

📘 **Dónde se aprende** (1 clase): [B09-C18 · Integrales dobles y triples](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md).

### Integrales de movimiento

- Las integrales de movimiento de un campo axisimétrico son la energía `½v² − U` y `h_z = x v_y − y v_x`.

🎯 **Por qué importa (clase B72-C18):** Un integrador mal elegido da una órbita que parece correcta y está equivocada en kilómetros. La decisión central: ¿qué método, paso o tolerancia da el error de posición que necesita la tarea al menor coste, y cómo saber que no engaña?

📘 **Dónde se aprende** (1 clase): [B72-C18 · Integración numérica perturbada](../programa/clases/B72/B72-C18-integracion-numerica-perturbada/CLASE.md).

### Integridad

- La integridad es que no hayan cambiado.
- La integridad exige que las huellas coincidan.
- Reenvío: nuevo intento de un trozo dañado. Integridad: igualdad entre lo enviado y lo recibido.

💡 **Cómo se explica en la clase [B74-C22](../programa/clases/B74/B74-C22-informe-de-navegacion-verificable/CLASE.md):**
- *Descripción textual:* las entradas con su huella y el proceso con su versión producen el estado y el informe; un verificador independiente revisa completitud, integridad, covarianza válida y reproducibilidad.
- 🎯 **Por qué importa:** Cuando dos equipos discrepan en una trayectoria, la primera pregunta es qué entradas y qué versiones usó cada uno. La decisión central: ¿qué debe llevar un informe para que cualquiera pueda reproducirlo y detectar que se alteró un dato?

📘 **Dónde se aprende** (3 clases): [B74-C22 · Informe de navegación verificable](../programa/clases/B74/B74-C22-informe-de-navegacion-verificable/CLASE.md); [B96-C22 · Transferencia de datos entre estación y centro de datos](../programa/clases/B96/B96-C22-transferencia-de-datos-entre-estacion-y-centro-de-datos/CLASE.md); [B122-C09 · Preservación de evidencias y cadena de custodia de datos de incidentes](../programa/clases/B122/B122-C09-preservacion-de-evidencias-y-cadena-de-custodia-de-datos-de-incidentes/CLASE.md).

### Intensidad

- La intensidad es `I = |z|²`.
- La intensidad es `|B|`.

💡 **Cómo se explica en la clase [B69-C03](../programa/clases/B69/B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md):**
- La intensidad `I = |z|²` sigue una exponencial con `CV = 1`: la simulación da `0,9987`.
- *Descripción textual:* la intensidad es la reflectividad multiplicada por un speckle exponencial; se reduce promediando vistas o con un filtro adaptativo.
- 🎯 **Por qué importa:** Un valor de píxel aislado de una imagen SAR no mide la reflectividad de la superficie: es una muestra de una distribución muy ancha. La decisión central: ¿cuánto hay que promediar o filtrar para estimar la reflectividad con una incertidumbre dada, y a qué precio en resolución?

📘 **Dónde se aprende** (2 clases): [B69-C03 · Ruido speckle y filtrado en imágenes SAR](../programa/clases/B69/B69-C03-ruido-speckle-y-filtrado-en-imagenes-sar/CLASE.md); [B87-C05 · Magnetómetros](../programa/clases/B87/B87-C05-magnetometros/CLASE.md).

### Intensidad aritmética

- La intensidad aritmética es el número de operaciones por byte movido.

🎯 **Por qué importa (clase B14-C15):** Un equipo promete que su simulación irá «100 veces más rápido en GPU» y, al compararla con la de CPU, los resultados difieren en el séptimo dígito. ¿Error del código o característica de la máquina?

📘 **Dónde se aprende** (1 clase): [B14-C15 · Cálculo en GPU y limitaciones](../programa/clases/B14/B14-C15-calculo-en-gpu-y-limitaciones/CLASE.md).

### Intensidad específica

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B32-C01):** El espectro depende de dónde se forma la luz. La decisión central: ¿qué capa determina la intensidad emergente y cómo cambia con el ángulo?

📘 **Dónde se aprende** (1 clase): [B32-C01 · Ecuación de transferencia radiativa en atmósferas estelares](../programa/clases/B32/B32-C01-ecuacion-de-transferencia-radiativa-en-atmosferas-estelares/CLASE.md).

### Intensidad integrada

- La intensidad integrada `W_CO` es la integral de la temperatura de brillo del `CO` sobre la velocidad, en `K km/s`.
- La intensidad integrada `I` es el área de la sección eficaz sobre la línea, a una temperatura dada.

💡 **Cómo se explica en la clase [B25-C04](../programa/clases/B25/B25-C04-nubes-moleculares-y-polvo/CLASE.md):**
- Bolatto, Wolfire y Leroy (S1) recomiendan, para el disco de la Vía Láctea, un factor de conversión `X_CO = 2 × 10²⁰ cm⁻² (K km/s)⁻¹` con una incertidumbre de `±30 %`: es el número de moléculas de `H₂` por cm² que corresponde a cada `K km/s` de intensidad integrada de CO.
- El ejemplo conductor es una nube sintética (no es una nube real): intensidad integrada `W_CO = 10 K km/s` sobre un área de `400 pc²`.
- 🎯 **Por qué importa:** El hidrógeno molecular `H₂`, el componente principal de las nubes donde nacen las estrellas, casi no emite en el gas frío. Por eso la masa de una nube se estima con un trazador indirecto, el monóxido de carbono `CO`, y con el polvo que apaga la luz de fondo.

📘 **Dónde se aprende** (2 clases): [B25-C04 · Nubes moleculares y polvo](../programa/clases/B25/B25-C04-nubes-moleculares-y-polvo/CLASE.md); [B62-C04 · Momentos dipolares y fuerza de línea](../programa/clases/B62/B62-C04-momentos-dipolares-y-fuerza-de-linea/CLASE.md).

### Intensidad o flujo

- La intensidad o flujo es la potencia por unidad de área (W/m²).

🎯 **Por qué importa (clase B05-C18):** Un satélite se comunica con ondas de radio, un telescopio observa luz y rayos X, y la misma radiación a otras energías puede dañar electrónica y tejidos. La pregunta motivadora es: ¿qué es la radiación electromagnética, cómo se ordena por frecuencia y energía, cómo decae con la distancia y qué la hace peligrosa?

📘 **Dónde se aprende** (1 clase): [B05-C18 · Electromagnetismo y radiación](../programa/clases/B05/B05-C18-electromagnetismo-y-radiacion/CLASE.md).

### Intentos

- Los intentos hasta una pieza buena siguen una geométrica de media `1/(1 − p_d)`.

💡 **Cómo se explica en la clase [B84-C38](../programa/clases/B84/B84-C38-produccion-de-piezas-y-repuestos-con-materia-prima-in-situ/CLASE.md):**
- Intentos esperados `1/(1 − 0,15) = 1,1765`;
- *Descripción textual:* la masa de la pieza da el hierro y el regolito; la energía da el tiempo; los defectos dan los intentos; la masa de la planta da el punto de equilibrio.
- 🎯 **Por qué importa:** Un repuesto que llega en 180 días puede producirse en 1,3 días, pero la planta pesa 400 kg y procesa 74 kg de regolito por pieza: el balance dice cuándo compensa. La decisión central: ¿cuántos repuestos hacen que producir in situ sea mejor que transportarlos?

📘 **Dónde se aprende** (1 clase): [B84-C38 · Producción de piezas y repuestos con materia prima in situ](../programa/clases/B84/B84-C38-produccion-de-piezas-y-repuestos-con-materia-prima-in-situ/CLASE.md).

### Interacción

- Una interacción es un encuentro gravitatorio que deforma a las galaxias sin fundirlas; una fusión las une.

🎯 **Por qué importa (clase B25-C12):** Las galaxias no evolucionan aisladas: se atraen, se deforman y a veces se funden. Muchas elípticas masivas pueden provenir de fusiones, y los encuentros llevan gas al centro, alimentando la formación estelar y los núcleos activos de C11.

📘 **Dónde se aprende** (1 clase): [B25-C12 · Interacciones y fusiones galácticas](../programa/clases/B25/B25-C12-interacciones-y-fusiones-galacticas/CLASE.md).

### Intercalado

- El intercalado lo decide aquí un planificador aleatorio con semilla.

🎯 **Por qué importa (clase B88-C27):** Una carrera no falla siempre: falla de vez en cuando y no se reproduce. La decisión central: ¿qué mecanismo garantiza que el acceso a un dato compartido sea exclusivo y que un buffer no se desborde ni se vacíe?

📘 **Dónde se aprende** (1 clase): [B88-C27 · Exclusión mutua y semáforos](../programa/clases/B88/B88-C27-exclusion-mutua-y-semaforos/CLASE.md).

### Intercalar

- La deriva es la diferencia acumulada entre un calendario y el fenómeno que pretende seguir. Intercalar es añadir un día o un mes de vez en cuando para corregir la deriva.

💡 **Cómo se explica en la clase [B02-C01](../programa/clases/B02/B02-C01-calendarios-astronomicos-en-civilizaciones-antiguas/CLASE.md):**
- E --> F["Intercalar<br/>(bisiesto, mes extra)"]
- De la diferencia sale la deriva por año, y de ella tres estrategias posibles: intercalar días o meses, dejar derivar y contar cuándo se cierra el ciclo completo, o combinar varios ciclos en uno mayor.
- 🎯 **Por qué importa:** Un calendario es una promesa: «dentro de tantos días ocurrirá tal cosa en el cielo o en la tierra». Esa promesa solo se cumple si el calendario sigue algún ciclo natural.

📘 **Dónde se aprende** (1 clase): [B02-C01 · Calendarios astronómicos en civilizaciones antiguas](../programa/clases/B02/B02-C01-calendarios-astronomicos-en-civilizaciones-antiguas/CLASE.md).

### Intercambiabilidad

- La intercambiabilidad supone que, antes de ver los datos, nada distingue a un sensor de otro.

💡 **Cómo se explica en la clase [B12-C21](../programa/clases/B12/B12-C21-modelos-jerarquicos-bayesianos/CLASE.md):**
- (i) Intercambiabilidad: si los sensores vienen de lotes distintos, hay que modelar covariables.
- Su límite: si hay alumnos de otro grupo etario mezclados, el promedio de la clase no les sirve (violación de la intercambiabilidad).
- ⚠️ **Error frecuente:** Suponer intercambiabilidad sin examinarla. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Ocho sensores del mismo tipo miden un mismo desfase con errores distintos. Tratarlos como idénticos (agrupación completa) ignora diferencias reales entre ellos; tratarlos como independientes (sin agrupación) desperdicia lo que cada uno enseña de los demás.

📘 **Dónde se aprende** (1 clase): [B12-C21 · Modelos jerárquicos bayesianos](../programa/clases/B12/B12-C21-modelos-jerarquicos-bayesianos/CLASE.md).

### Intercambiables

- El factor de encogimiento `B_j = σ_j²/(σ_j² + τ²)` es la fracción por la que el sensor `j` se acerca al grupo. Intercambiables: las unidades se tratan como sorteos de una misma población.

💡 **Cómo se explica en la clase [B19-C02](../programa/clases/B19/B19-C02-modelos-jerarquicos/CLASE.md):**
- Límite de la analogía: «pedir prestado» solo es razonable si los sensores son realmente intercambiables.
- 🎯 **Por qué importa:** Seis sensores de temperatura de un satélite miden cada uno un desvío de calibración. Tres decisiones ingenuas son posibles: tratar a cada sensor por separado, ignorar las diferencias y promediar todo, o confiar en el sensor más preciso.

📘 **Dónde se aprende** (1 clase): [B19-C02 · Modelos jerárquicos](../programa/clases/B19/B19-C02-modelos-jerarquicos/CLASE.md).

### Intercambio

- El intercambio `Q_x` es el caudal de aire entre zonas (m³/h).
- Un intercambio es una intervención de cada lado.

💡 **Cómo se explica en la clase [B110-C02](../programa/clases/B110/B110-C02-protocolos-operativos-de-aislamiento-de-un-tripulante-enfermo-o-contaminado/CLASE.md):**
- *Descripción textual:* la fuente emite en la zona 1; parte pasa a la zona 2 por el intercambio y cada zona elimina por su cuenta; la dosis se calcula con la concentración de la zona 2.
- 🎯 **Por qué importa:** Aislar a alguien en una cabina cuesta espacio, tiempo y trabajo de la tripulación; no aislar cuesta exposición. La decisión central: ¿cuánta exposición evita cada barrera y con qué incertidumbre?

📘 **Dónde se aprende** (2 clases): [B110-C02 · Protocolos operativos de aislamiento de un tripulante enfermo o contaminado](../programa/clases/B110/B110-C02-protocolos-operativos-de-aislamiento-de-un-tripulante-enfermo-o-contaminado/CLASE.md); [B113-C03 · Comunicación diferida y soporte psicológico a distancia](../programa/clases/B113/B113-C03-comunicacion-diferida-y-soporte-psicologico-a-distancia/CLASE.md).

### Intercambio entre placas paralelas

- El intercambio entre placas paralelas es `q = σ(T₁⁴ − T₂⁴)/(1/ε₁ + 1/ε₂ − 1)`.

🎯 **Por qué importa (clase B85-C04):** La mitad del control térmico es elegir cuánto emite o absorbe cada superficie. La decisión central: ¿cuánto calor intercambian dos superficies y cómo lo cambia poner una emisividad baja entre ellas?

📘 **Dónde se aprende** (1 clase): [B85-C04 · Radiación térmica de superficies](../programa/clases/B85/B85-C04-radiacion-termica-de-superficies/CLASE.md).

### Intercomparación

- Una intercomparación es la medición de la misma magnitud con varios instrumentos o laboratorios para evaluar su concordancia.

🎯 **Por qué importa (clase B13-C18):** Tres radiómetros miden la misma irradiancia solar y dan `1361,4`, `1360,1` y `1362,9 W/m²`. Cada uno declara una incertidumbre.

📘 **Dónde se aprende** (1 clase): [B13-C18 · Intercomparación de instrumentos](../programa/clases/B13/B13-C18-intercomparacion-de-instrumentos/CLASE.md).

### Interés

- El poder es su capacidad de influir; el interés, cuánto le afecta.

💡 **Cómo se explica en la clase [B83-C02](../programa/clases/B83/B83-C02-partes-interesadas-y-usuarios/CLASE.md):**
- Con `poder×interés` (15, 20, 6, 8, 10, 10) y suma 69, los pesos son 21,7 %, 29,0 %, 8,7 %, 11,6 %, 14,5 % y 14,5 %.
- Solo la agencia financiadora cae en «gestionar de cerca» (poder 5, interés 4): hay 1 parte en esa casilla.
- 🎯 **Por qué importa:** Cuando las necesidades de dos partes chocan (alta resolución frente a bajo costo), alguien debe decidir con criterio. La decisión central: ¿qué necesidades pasan a requisitos primero y cuánto confías en ese orden?

📘 **Dónde se aprende** (1 clase): [B83-C02 · Partes interesadas y usuarios](../programa/clases/B83/B83-C02-partes-interesadas-y-usuarios/CLASE.md).

### Interfaz

- La interfaz `i+½` es el borde entre las celdas `i` e `i+1`.
- Una interfaz es un límite de intercambio.
- Protocolo: reglas de comunicación con un dispositivo. Interfaz: conjunto de operaciones por tipo de dispositivo.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B21-C01](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md):**
- Eso es conservación discreta, y vale para cualquier flujo numérico que use el mismo valor en la interfaz para las dos celdas vecinas.
- En cada interfaz hay un salto entre el estado izquierdo `q_L` y el derecho `q_R`.
- ⚠️ **Error frecuente:** Usar en una interfaz un flujo distinto para cada celda vecina. Rompe la conservación; se detecta con el residuo del ejercicio 7.
- 🎯 **Por qué importa:** Casi todo lo que fluye en el espacio —el viento solar, el gas de un disco de acreción, el gas que rodea a una nave en reentrada, la onda de choque de una eyección coronal— obedece leyes de conservación: una cantidad cambia en una región solo porque entra o sale por sus bordes.

📘 **Dónde se aprende** (5 clases): [B21-C01 · Volúmenes finitos y solucionadores de Riemann para leyes de conservación](../programa/clases/B21/B21-C01-volumenes-finitos-y-solucionadores-de-riemann-para-leyes-de-conservacion/CLASE.md); [B41-C01 · Naturaleza y propagación de la luz](../programa/clases/B41/B41-C01-naturaleza-y-propagacion-de-la-luz/CLASE.md); [B48-C21 · Protocolos estándar de control instrumental (ASCOM e INDI)](../programa/clases/B48/B48-C21-protocolos-estandar-de-control-instrumental-ascom-e-indi/CLASE.md); [B83-C08 · Interfaz entre subsistemas](../programa/clases/B83/B83-C08-interfaz-entre-subsistemas/CLASE.md); [B96-C19 · Lecciones aprendidas operativas](../programa/clases/B96/B96-C19-lecciones-aprendidas-operativas/CLASE.md).

### Interfaz de reentrada

- La interfaz de reentrada es la altitud (aquí 120 km, ilustrativa) a la que se evalúa el ángulo.

🎯 **Por qué importa (clase B118-C13):** La reentrada controlada dirige los restos a una zona despoblada; la no controlada deja el lugar al azar del arrastre. Pero un impulso con error cambia el ángulo y el punto de entrada.

📘 **Dónde se aprende** (1 clase): [B118-C13 · Desorbitación controlada](../programa/clases/B118/B118-C13-desorbitacion-controlada/CLASE.md).

### Interfaz explícita

- La interfaz explícita crea figura y ejes y llama a sus métodos (`ax.plot`); la interfaz implícita usa `plt.plot` y deja que `pyplot` gestione todo; la documentación recomienda la explícita para código reutilizable (S2).

🎯 **Por qué importa (clase B07-C10):** Un gráfico es una afirmación: dice «mira esta relación». Un gráfico sin unidades, con una escala que esconde la mitad de los datos o sin leyenda puede inducir a error aunque los números sean correctos.

📘 **Dónde se aprende** (1 clase): [B07-C10 · Gráficos bidimensionales iniciales](../programa/clases/B07/B07-C10-graficos-bidimensionales-iniciales/CLASE.md).

### Interfaz implícita

- La interfaz explícita crea figura y ejes y llama a sus métodos (`ax.plot`); la interfaz implícita usa `plt.plot` y deja que `pyplot` gestione todo; la documentación recomienda la explícita para código reutilizable (S2).

🎯 **Por qué importa (clase B07-C10):** Un gráfico es una afirmación: dice «mira esta relación». Un gráfico sin unidades, con una escala que esconde la mitad de los datos o sin leyenda puede inducir a error aunque los números sean correctos.

📘 **Dónde se aprende** (1 clase): [B07-C10 · Gráficos bidimensionales iniciales](../programa/clases/B07/B07-C10-graficos-bidimensionales-iniciales/CLASE.md).

### Interferencia

- La interferencia `I` es la potencia no deseada recibida;

💡 **Cómo se explica en la clase [B51-C13](../programa/clases/B51/B51-C13-marcado-de-datos-espurios-e-interferencia-en-visibilidades/CLASE.md):**
- La interferencia débil (1,5 σ durante 16 muestras) pasa inadvertida con el umbral simple; la suma de 16 muestras la ve solo en parte (25 %) y a cambio marca 0,83 % de muestras limpias.
- *Descripción textual:* la σ robusta fija el umbral; las sumas de muestras vecinas permiten detectar interferencia débil y extendida.
- 🎯 **Por qué importa:** Dejar RFI en los datos degrada la imagen; marcar demasiado pierde señal. La decisión central: ¿qué umbral marca la interferencia sin marcar el ruido, y cómo se detecta la interferencia débil y extendida?

📘 **Dónde se aprende** (2 clases): [B51-C13 · Marcado de datos espurios e interferencia en visibilidades](../programa/clases/B51/B51-C13-marcado-de-datos-espurios-e-interferencia-en-visibilidades/CLASE.md); [B89-C19 · Coordinación del espectro ante ITU](../programa/clases/B89/B89-C19-coordinacion-del-espectro-ante-itu/CLASE.md).

### Interferencia perjudicial

- La interferencia perjudicial degrada un servicio.

🎯 **Por qué importa (clase B119-C09):** Ninguna clase anterior vincula el derecho de telecomunicaciones con el cálculo de interferencia; B120 trata licencias y espectro en detalle y esta clase fija el marco.

📘 **Dónde se aprende** (1 clase): [B119-C09 · Derecho y normas de telecomunicaciones](../programa/clases/B119/B119-C09-derecho-y-normas-de-telecomunicaciones/CLASE.md).

### Interferómetro

- Un interferómetro combina varias antenas para actuar como una más grande (ALMA).

💡 **Cómo se explica en la clase [B02-C18](../programa/clases/B02/B02-C18-expansion-de-la-astronomia-en-chile/CLASE.md):**
- Es un cálculo nuestro (área geométrica, no eficaz) y el interferómetro se comporta como una única antena de gran diámetro (B46).
- 🎯 **Por qué importa:** Chile alberga observatorios de primer nivel porque combina cielos oscuros, aire seco y altitud. Pero un observatorio también es una historia de decisiones, instituciones y territorios.

📘 **Dónde se aprende** (1 clase): [B02-C18 · Expansión de la astronomía en Chile](../programa/clases/B02/B02-C18-expansion-de-la-astronomia-en-chile/CLASE.md).

### Interferómetro de Michelson

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B42-C09):** La medida interferométrica de fase es la base de la metrología óptica (superficies, frentes de onda; C13).

📘 **Dónde se aprende** (1 clase): [B42-C09 · Interferometría de dos haces](../programa/clases/B42/B42-C09-interferometria-de-dos-haces/CLASE.md).

### Interior

- Un planeta exterior orbita más lejos del Sol que la Tierra; uno interior, más cerca.
- Un destino exterior (Marte, Júpiter) tiene `φ` positivo; un destino interior (Venus), negativo.

💡 **Cómo se explica en la clase [B02-C11](../programa/clases/B02/B02-C11-revolucion-copernicana-y-metodos/CLASE.md):**
- La Tierra y Marte son dos corredores que recorren pistas circulares alrededor del Sol; la Tierra, en la pista interior, es más rápida.
- 🎯 **Por qué importa:** La «revolución copernicana» suele resumirse como «el Sol en el centro». Pero lo que cambió la ciencia fue que el modelo permitió calcular cosas nuevas: convertir lo observado en lo real.

📘 **Dónde se aprende** (2 clases): [B02-C11 · Revolución copernicana y métodos](../programa/clases/B02/B02-C11-revolucion-copernicana-y-metodos/CLASE.md); [B75-C02 · Ángulos de fase planetaria](../programa/clases/B75/B75-C02-angulos-de-fase-planetaria/CLASE.md).

### Intermitencia

- La intermitencia es la concentración de la energía en pocas regiones.

💡 **Cómo se explica en la clase [B35-C09](../programa/clases/B35/B35-C09-turbulencia-en-plasmas-y-mhd/CLASE.md):**
- C["cascada p-model"] --> I["intermitencia"]
- *Descripción textual:* la serie da espectro y estructura; la cascada da la intermitencia exacta.
- ⚠️ **Error frecuente:** Olvidar la intermitencia. Se corrige con 8.2.
- 🎯 **Por qué importa:** La pendiente de un espectro y su intermitencia distinguen modelos de turbulencia. La decisión central: ¿qué pendiente y qué curtosis tiene la serie y qué modelo sugiere?

📘 **Dónde se aprende** (1 clase): [B35-C09 · Turbulencia en plasmas y MHD](../programa/clases/B35/B35-C09-turbulencia-en-plasmas-y-mhd/CLASE.md).

### Intermodulación

- La intermodulación son productos `2f₁ − f₂`.

🎯 **Por qué importa (clase B49-C09):** Un receptor que satura con una señal fuerte arruina la observación de una señal débil cercana. La decisión central: ¿qué potencia máxima admite el receptor y qué productos de intermodulación genera?

📘 **Dónde se aprende** (1 clase): [B49-C09 · Linealidad, compresión e intermodulación de receptores de RF](../programa/clases/B49/B49-C09-linealidad-compresion-e-intermodulacion-de-receptores-de-rf/CLASE.md).

### Interno

- El ocultador externo y el interno.

🎯 **Por qué importa (clase B47-C07):** La luz difractada del disco es mayor que la señal buscada. La decisión central: ¿cuánta supresión de luz difractada se necesita y con qué geometría de ocultador?

📘 **Dónde se aprende** (1 clase): [B47-C07 · Coronógrafos espaciales](../programa/clases/B47/B47-C07-coronografos-espaciales/CLASE.md).

### Interoperabilidad

- La interoperabilidad es que clientes distintos puedan usar el servicio sin adaptarlo.
- La interoperabilidad es que dos implementaciones distintas intercambien datos.

🎯 **Por qué importa (clase B14-C29):** Has producido un mosaico de imágenes y varias organizaciones quieren verlo en sus propios visores. Enviar archivos a cada una no escala, y cada una usa un programa distinto.

📘 **Dónde se aprende** (2 clases): [B14-C29 · Servicios de datos geoespaciales estándar (OGC)](../programa/clases/B14/B14-C29-servicios-de-datos-geoespaciales-estandar-ogc/CLASE.md); [B94-C06 · Validación y conformidad de protocolos de enlace](../programa/clases/B94/B94-C06-validacion-y-conformidad-de-protocolos-de-enlace/CLASE.md).

### Interpolación

- La interpolación estima valores dentro del rango de los datos.
- La interpolación `atan2(s, c)`.
- La interpolación reemplaza un valor por el de sus vecinos.

💡 **Cómo se explica en la clase [B15-C19](../programa/clases/B15/B15-C19-reconstruccion-por-datos-incompletos/CLASE.md):**
- La interpolación lineal falla porque el hueco abarca casi medio periodo de la oscilación mayor; el modelo gana cuando es correcto.
- *Descripción textual:* según lo que se sepa de la señal se elige interpolación, ajuste de modelo o extrapolación de banda limitada; el resultado se verifica con una simulación de hueco conocido y con los residuos en los puntos medidos, y lo reconstruido se marca.
- 🎯 **Por qué importa:** Si falta el 8 % de una serie, ¿se puede rellenar sin contaminar el análisis? Depende de lo que se sepa de la señal: si es suave y se conoce su forma, el relleno es casi exacto; si es un evento breve que cayó en el hueco, no hay método que lo recupere.

📘 **Dónde se aprende** (3 clases): [B15-C19 · Reconstrucción por datos incompletos](../programa/clases/B15/B15-C19-reconstruccion-por-datos-incompletos/CLASE.md); [B43-C16 · Encoders y medición angular](../programa/clases/B43/B43-C16-encoders-y-medicion-angular/CLASE.md); [B44-C15 · Píxeles defectuosos](../programa/clases/B44/B44-C15-pixeles-defectuosos/CLASE.md).

### Interpolación bilineal

- La interpolación bilineal completa entre cuatro vecinos.

🎯 **Por qué importa (clase B37-C03):** Un código no integra en frecuencia en cada capa: lee una tabla de `κ_R(ρ, T)`. La decisión central: ¿cómo se promedia la opacidad y qué error añade la interpolación de la tabla?

📘 **Dónde se aprende** (1 clase): [B37-C03 · Opacidad media de Rosseland y tablas de opacidad en interiores](../programa/clases/B37/B37-C03-opacidad-media-de-rosseland-y-tablas-de-opacidad-en-interiores/CLASE.md).

### Interpolar

- Si `f` tiene derivada continua de orden `n + 1`, el error es `f(x) − P_n(x) = f^{(n+1)}(ξ) ω(x)/(n + 1)!` para algún `ξ` en el intervalo (S1, ec. 3.3.5). Interpolar es evaluar dentro del intervalo de los nodos;

💡 **Cómo se explica en la clase [B11-C18](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md):**
- ⚠️ **Error frecuente:** Interpolar datos ruidosos. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Si una nave debe saber dónde está un cuerpo en un instante que no figura en la tabla, interpola. Si interpola con un grado equivocado o fuera del rango, el error puede pasar de metros a miles de kilómetros sin que el programa avise.

📘 **Dónde se aprende** (1 clase): [B11-C18 · Interpolación y extrapolación](../programa/clases/B11/B11-C18-interpolacion-y-extrapolacion/CLASE.md).

### Interpretación

- La interpretación asigna sentido a un texto.

💡 **Cómo se explica en la clase [B119-C32](../programa/clases/B119/B119-C32-interpretacion-de-tratados-internacionales/CLASE.md):**
- Una lectura mayoritaria no es necesariamente la correcta; la interpretación autorizada depende de las reglas y de quien las aplique.
- Límite: la interpretación jurídica no es un concurso de votos; un panel mide ambigüedad, no corrección.
- ⚠️ **Error frecuente:** Citar la regla de interpretación como verificada. Se corrige con la sección 11.
- 🎯 **Por qué importa:** B119 enseña los tratados y su contenido, no el método para interpretarlos, que el rol de derecho espacial exige; la regla general de interpretación se menciona como conocimiento no verificado. La decisión central: ¿cuánta ambigüedad queda en una cláusula y qué fuentes de interpretación la reducen más?

📘 **Dónde se aprende** (1 clase): [B119-C32 · Interpretación de tratados internacionales](../programa/clases/B119/B119-C32-interpretacion-de-tratados-internacionales/CLASE.md).

### Intérprete de comandos

- La terminal (o consola) es un programa donde escribes comandos de texto; el intérprete de comandos (*shell*), como bash o PowerShell, los ejecuta.

🎯 **Por qué importa (clase B07-C15):** Una causa muy común de «el programa no encuentra el archivo» es que la ruta funciona en el computador del autor y no en otro: se escribió con `C:\Usuarios\ana\datos\...`, o se asumió que el programa se ejecuta desde cierta carpeta.

📘 **Dónde se aprende** (1 clase): [B07-C15 · Terminal y rutas de archivos](../programa/clases/B07/B07-C15-terminal-y-rutas-de-archivos/CLASE.md).

### Interrupción

- Tiempo de respuesta: tiempo hasta la llegada de la respuesta. Interrupción: respuesta que llega antes de que el evento se complete.
- La interrupción corta la secuencia y puede hacer retomar mal.

💡 **Cómo se explica en la clase [B96-C25](../programa/clases/B96/B96-C25-seguridad-fisica-y-control-de-acceso-de-estaciones-terrestres/CLASE.md):**
- Detectar no basta: con respuesta de 240 s la probabilidad de interrupción es cero aunque la de detección sea 0,999955.
- Una capa adicional de 45 s (guardia en sitio) sube la interrupción a 0,9991 para la respuesta de 180 s.
- 🎯 **Por qué importa:** Una alarma que llega tarde no sirve: lo que importa es si el retardo restante supera el tiempo de respuesta cuando se detecta. La decisión central: ¿qué capas y qué tiempo de respuesta dan una probabilidad de interrupción aceptable?

📘 **Dónde se aprende** (2 clases): [B96-C25 · Seguridad física y control de acceso de estaciones terrestres](../programa/clases/B96/B96-C25-seguridad-fisica-y-control-de-acceso-de-estaciones-terrestres/CLASE.md); [B104-C22 · Diseño y uso de listas de comprobación de cabina](../programa/clases/B104/B104-C22-diseno-y-uso-de-listas-de-comprobacion-de-cabina/CLASE.md).

### Interruptor de despliegue

- El interruptor de despliegue corta la energía mientras el CubeSat está dentro.

💡 **Cómo se explica en la clase [B95-C01](../programa/clases/B95/B95-C01-unidad-cubesat-dimensiones-y-formatos/CLASE.md):**
- Además, el CDS pide un interruptor de despliegue, una clavija de retirar antes del vuelo, tres inhibidores independientes de RF y tres de liberación de desplegables.
- 🎯 **Por qué importa:** Un CubeSat que no cumple el estándar no entra en el dispensador, aunque funcione perfectamente. La decisión central: ¿esta configuración cabe, pesa y se equilibra dentro de lo que el estándar permite, y cuándo puede encenderse, desplegar y transmitir?

📘 **Dónde se aprende** (1 clase): [B95-C01 · Unidad CubeSat, dimensiones y formatos](../programa/clases/B95/B95-C01-unidad-cubesat-dimensiones-y-formatos/CLASE.md).

### Intersecar

- La caja envolvente `[minX, minY, maxX, maxY]` acota la escena. Intersecar dos cajas es que se solapen con área positiva; cajas que solo comparten un borde no se intersecan en este laboratorio.

🎯 **Por qué importa (clase B14-C25):** Un satélite produce miles de escenas al día. Para estudiar una inundación necesitas las que cubren una región, en unas fechas, con poca nube.

📘 **Dónde se aprende** (1 clase): [B14-C25 · Catálogos de datos geoespaciales y metadatos (STAC)](../programa/clases/B14/B14-C25-catalogos-de-datos-geoespaciales-y-metadatos-stac/CLASE.md).

### Intersección

- Una intersección es un punto con el mismo radio y la misma longitud en ambas.
- La unión `A∪B` ocurre si ocurre `A` o `B`; la intersección `A∩B`, si ocurren ambos.

💡 **Cómo se explica en la clase [B12-C01](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md):**
- Para dos eventos cualquiera, `P(A∪B) = P(A) + P(B) − P(A∩B)`: al sumar `P(A)` y `P(B)` se cuenta dos veces la intersección.
- 🎯 **Por qué importa:** Una nave no sabe si un componente va a fallar; un telescopio no sabe cuántos fotones llegarán. Para decidir con información incompleta hace falta un lenguaje que diga con precisión *qué puede pasar* y *cuánto lo esperamos*.

📘 **Dónde se aprende** (2 clases): [B12-C01 · Espacios muestrales y eventos](../programa/clases/B12/B12-C01-espacios-muestrales-y-eventos/CLASE.md); [B75-C21 · Intersección de cónicas en transferencias](../programa/clases/B75/B75-C21-interseccion-de-conicas-en-transferencias/CLASE.md).

### Intersección de covarianzas

- La intersección de covarianzas (CI) combina `P⁻¹ = ω P₁⁻¹ + (1 − ω) P₂⁻¹` y es consistente para cualquier correlación.

💡 **Cómo se explica en la clase [B80-C08](../programa/clases/B80/B80-C08-filtrado-distribuido-y-descentralizado/CLASE.md):**
- *Descripción textual:* dos estimaciones llegan a un nodo de fusión; si se conoce su correlación se usa; si no, la intersección de covarianzas con peso optimizado; si se ignora, la suma ingenua declara una confianza excesiva.
- La intersección de covarianzas con el peso `0,500` declara `3,2`, es conservadora y su NEES medio es `1,555`.
- 🎯 **Por qué importa:** B74-C08..C10 tratan filtros centralizados, en los que un solo nodo ve todas las mediciones. La decisión central: ¿cómo fundir estimaciones de varios nodos sin conocer la correlación entre sus errores y sin declarar más confianza de la que se tiene?

📘 **Dónde se aprende** (1 clase): [B80-C08 · Filtrado distribuido y descentralizado](../programa/clases/B80/B80-C08-filtrado-distribuido-y-descentralizado/CLASE.md).

### Intersección sobre unión

- La intersección sobre unión (IoU) de una clase es `TP/(TP + FP + FN)`.

🎯 **Por qué importa (clase B103-C05):** Un modelo que acierta el 91 % de los píxeles en el dominio de entrenamiento puede acertar el 45 % cuando cambia la luz. La decisión central: ¿qué métrica y qué prueba demuestran que un segmentador es utilizable en otras condiciones, y no solo en las de entrenamiento?

📘 **Dónde se aprende** (1 clase): [B103-C05 · Segmentación semántica de superficies planetarias](../programa/clases/B103/B103-C05-segmentacion-semantica-de-superficies-planetarias/CLASE.md).

### Intersísmica

- La deformación cosísmica es el cambio del suelo durante el terremoto; la intersísmica, la acumulada entre terremotos.

🎯 **Por qué importa (clase B57-C17):** Medir la deformación permite saber cuánto deslizó la falla y cuánta tensión queda. La decisión central: ¿cómo se pasa de un número de magnitud al deslizamiento y a la deformación que verá un satélite?

📘 **Dónde se aprende** (1 clase): [B57-C17 · Terremotos y deformación](../programa/clases/B57/B57-C17-terremotos-y-deformacion/CLASE.md).

### Intervalo

- El peso atómico estándar es la masa atómica relativa media del elemento en materiales terrestres normales; puede darse como un valor con incertidumbre o como un intervalo (S2).
- Un intervalo o límite define `lo` y `hi`: mínimo–máximo o por percentiles (el percentil `p` es el valor bajo el cual está `p`% de los datos).
- El intervalo `s² = (ct)² − x²` es la combinación que no cambia.

💡 **Cómo se explica en la clase [B06-C03](../programa/clases/B06/B06-C03-isotopos-y-masa-atomica/CLASE.md):**
- El peso atómico estándar de la NIST es el intervalo [35,446; 35,457] (S2): el valor cae dentro.
- La NIST da entonces un intervalo que cubre las muestras terrestres normales.
- 🎯 **Por qué importa:** El carbono del Sol, ¿es igual que el de la Tierra? Una forma de preguntarlo con rigor es comparar cuántos átomos de carbono-12 hay por cada uno de carbono-13.

📘 **Dónde se aprende** (3 clases): [B06-C03 · Isótopos y masa atómica](../programa/clases/B06/B06-C03-isotopos-y-masa-atomica/CLASE.md); [B15-C10 · Histogramas y normalización](../programa/clases/B15/B15-C10-histogramas-y-normalizacion/CLASE.md); [B26-C02 · Transformaciones de Lorentz](../programa/clases/B26/B26-C02-transformaciones-de-lorentz/CLASE.md).

### Intervalo cerrado–abierto

- Un intervalo cerrado–abierto `[t₀, t₁)` incluye `t₀` y excluye `t₁`.

🎯 **Por qué importa (clase B14-C22):** Quieres estudiar una región activa del Sol durante un día usando imágenes ultravioleta. Hay cientos de miles de archivos repartidos en varios proveedores.

📘 **Dónde se aprende** (1 clase): [B14-C22 · Acceso a datos heliofísicos abiertos con SunPy](../programa/clases/B14/B14-C22-acceso-a-datos-heliofisicos-abiertos-con-sunpy/CLASE.md).

### Intervalo compatible

- El intervalo compatible es la intersección de los intervalos que admite cada evidencia.

🎯 **Por qué importa (clase B132-C02):** Un instrumento antiguo no trae su fecha ni su precisión grabadas. La decisión central: ¿qué intervalo de fechas dejan las evidencias compatibles y qué precisión astronómica podía dar el instrumento, con qué sesgos?

📘 **Dónde se aprende** (1 clase): [B132-C02 · Arqueología de observatorios y de instrumentos antiguos](../programa/clases/B132/B132-C02-arqueologia-de-observatorios-y-de-instrumentos-antiguos/CLASE.md).

### Intervalo creíble

- Un intervalo creíble al 95 % contiene el 95 % de la probabilidad posterior; es una afirmación sobre `θ`, a diferencia de un intervalo de confianza (C08), que describe un procedimiento.

💡 **Cómo se explica en la clase [B12-C12](../programa/clases/B12/B12-C12-inferencia-bayesiana/CLASE.md):**
- Con prior débil `Gamma(1; 0,1)` (media 10, muy difuso), `S = 37` y `n = 10`: posterior `Gamma(38; 10,1)`, media `3,7624`, intervalo creíble 95 % `[2,662; 5,049]`.
- 27 éxitos en 30 pruebas con prior uniforme `Beta(1,1)`: posterior `Beta(28, 4)`, media `0,875`, intervalo creíble 95 % `[0,742; 0,964]`.
- ⚠️ **Error frecuente:** Confundir intervalo creíble y de confianza. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** Una misión rara vez parte de cero: hay pruebas en tierra, misiones anteriores y física conocida. Y a menudo el dato es escaso (diez intervalos, treinta pruebas).

📘 **Dónde se aprende** (1 clase): [B12-C12 · Inferencia bayesiana](../programa/clases/B12/B12-C12-inferencia-bayesiana/CLASE.md).

### Intervalo de 68 %

- El intervalo de 68 % para un parámetro es la región con `Δχ² ≤ 1`.

🎯 **Por qué importa (clase B26-C20):** Una cifra cosmológica sin incertidumbre no significa nada. Para decidir si dos resultados concuerdan, o si un modelo queda excluido, hay que saber construir y leer un intervalo de confianza.

📘 **Dónde se aprende** (1 clase): [B26-C20 · Límites observacionales de modelos cosmológicos](../programa/clases/B26/B26-C20-limites-observacionales-de-modelos-cosmologicos/CLASE.md).

### Intervalo de cobertura

- El intervalo de cobertura contiene la salida con una probabilidad dada (típicamente 95 %); la incertidumbre expandida es `U = k u_c` con factor de cobertura `k`.

💡 **Cómo se explica en la clase [B12-C16](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md):**
- Con `M = 10⁶` sorteos de `a ~ N(6 778 100; 1 000)`: media `7 668,580 m/s`, desviación `0,5654 m/s` (GUM: `0,5657`, diferencia `0,05 %`) e intervalo de cobertura del 95 % `[7 667,474; 7 669,688] m/s`.
- 🎯 **Por qué importa:** Casi todo resultado en ciencias espaciales es una función de medidas: una velocidad a partir de un radio, una distancia a partir de una paralaje, una masa a partir de un período. Dar el valor sin su incertidumbre no permite comparar con otros resultados ni decidir si cumple un requisito.

📘 **Dónde se aprende** (1 clase): [B12-C16 · Propagación de incertidumbre](../programa/clases/B12/B12-C16-propagacion-de-incertidumbre/CLASE.md).

### Intervalo de comparación

- El intervalo de comparación `K` es cada cuántos ciclos se compara.

🎯 **Por qué importa (clase B88-C25):** Lockstep detecta fallos transitorios de un núcleo, pero no los corrige ni cubre causas comunes. La decisión central: ¿cada cuántos ciclos comparar, y qué fallas escapan?

📘 **Dónde se aprende** (1 clase): [B88-C25 · Redundancia de procesamiento y ejecución en paralelo (lockstep)](../programa/clases/B88/B88-C25-redundancia-de-procesamiento-y-ejecucion-en-paralelo-lockstep/CLASE.md).

### Intervalo de confianza

- Un intervalo de confianza bilateral es un par de funciones de los datos `T₁ < T₂` tales que, repetido el experimento, la fracción de veces que el intervalo contiene el parámetro es el nivel de confianza (S1, C.2.27 y C.2.29).

🎯 **Por qué importa (clase B12-C08):** Un número sin rango es una afirmación sin evidencia de su precisión. «La distancia es 148,5 m» no dice si el valor es fiable al metro o al decámetro. Un intervalo con su nivel de confianza lo dice, y permite decidir si una medición cumple un requisito o si hay que tomar más datos.

📘 **Dónde se aprende** (1 clase): [B12-C08 · Intervalos de confianza](../programa/clases/B12/B12-C08-intervalos-de-confianza/CLASE.md).

### Intervalo de diseño

- Un intervalo de diseño es el rango de percentiles que el diseño cubre.

🎯 **Por qué importa (clase B109-C06):** Si se dimensiona para la media, la mitad de las personas no cabe o no alcanza. La decisión central: ¿qué percentil de qué población usar para cada dimensión?

📘 **Dónde se aprende** (1 clase): [B109-C06 · Antropometría y dimensionamiento para tripulación](../programa/clases/B109/B109-C06-antropometria-y-dimensionamiento-para-tripulacion/CLASE.md).

### Intervalo de género tiempo

- El intervalo de género tiempo (`s² > 0`) conecta eventos que un objeto con masa puede unir.

🎯 **Por qué importa (clase B26-C04):** Comunicar con una sonda, sincronizar relojes de dos estaciones o decidir si un evento puede haber causado otro exige saber cuándo dos sucesos están conectados por una señal. El intervalo lo decide para todos los observadores.

📘 **Dónde se aprende** (1 clase): [B26-C04 · Espacio-tiempo de Minkowski](../programa/clases/B26/B26-C04-espacio-tiempo-de-minkowski/CLASE.md).

### Intervalo de muestreo

- El intervalo de muestreo `s` es el tiempo entre muestras.

🎯 **Por qué importa (clase B105-C10):** Si un episodio dura 3 días y se muestrea cada semana, la mayoría pasa inadvertida: una tasa de detección baja no implica pocos episodios. La decisión central: ¿cada cuántos días hay que muestrear para detectar una fracción dada de los episodios y cuántos se perderán?

📘 **Dónde se aprende** (1 clase): [B105-C10 · Respuesta inmune](../programa/clases/B105/B105-C10-respuesta-inmune/CLASE.md).

### Intervalo de predicción

- El intervalo de predicción cubre una nueva medida, no solo la media.
- El intervalo de predicción acota un valor nuevo.

💡 **Cómo se explica en la clase [B84-C37](../programa/clases/B84/B84-C37-compuestos-y-aglomerantes-a-base-de-regolito/CLASE.md):**
- Por incertidumbre: intervalo de predicción.
- Con `P = 0,25`, `σ = 26,50 MPa` con intervalo de predicción `[21,86; 32,13]`.
- ⚠️ **Error frecuente:** Usar la media en vez del intervalo de predicción. Se corrige con 8.2.
- 🎯 **Por qué importa:** La resistencia de un compuesto cae exponencialmente con la porosidad: pasar de 10 a 25 % de huecos divide la resistencia por 2,4. La decisión central: ¿qué porosidad máxima permite cumplir una resistencia mínima y cuánto ligante hay que transportar?

📘 **Dónde se aprende** (2 clases): [B84-C37 · Compuestos y aglomerantes a base de regolito](../programa/clases/B84/B84-C37-compuestos-y-aglomerantes-a-base-de-regolito/CLASE.md); [B124-C05 · Estimación de costos de misión](../programa/clases/B124/B124-C05-estimacion-de-costos-de-mision/CLASE.md).

### Intervalo de protección

- El intervalo de revisión `R` es el tiempo entre pedidos; la demora `L` es el tiempo entre pedir y recibir; el intervalo de protección es `T = R + L`.

💡 **Cómo se explica en la clase [B100-C03](../programa/clases/B100/B100-C03-gestion-de-inventarios-y-reposicion-de-suministros/CLASE.md):**
- *Descripción textual:* de la demanda y del intervalo de protección salen la demanda media esperada y la reserva; su suma es el nivel máximo, que la simulación contrasta con el nivel de servicio objetivo.
- Descripción larga: el nivel máximo crece casi con el intervalo de protección y la reserva con su raíz cuadrada; sin reserva, el servicio es de una moneda al aire.
- 🎯 **Por qué importa:** Con una reposición de 10 días basta una reserva pequeña; con una ventana sinódica de Marte la misma demanda exige guardar casi dos años y medio de consumo. La decisión central: ¿hasta qué nivel conviene reponer en cada ventana para que la probabilidad de quedarse sin existencias en el ciclo sea de un 5 %?

📘 **Dónde se aprende** (1 clase): [B100-C03 · Gestión de inventarios y reposición de suministros](../programa/clases/B100/B100-C03-gestion-de-inventarios-y-reposicion-de-suministros/CLASE.md).

### Intervalo de reabastecimiento

- El intervalo de reabastecimiento `τ` es el tiempo entre vuelos.

🎯 **Por qué importa (clase B97-C19):** Un stock grande cuesta masa inicial; reabastecer a menudo cuesta vuelos. El mínimo está en un punto intermedio que solo aparece al calcular ambos efectos con la misma confianza de misión.

📘 **Dónde se aprende** (1 clase): [B97-C19 · Logística de piezas y reparaciones](../programa/clases/B97/B97-C19-logistica-de-piezas-y-reparaciones/CLASE.md).

### Intervalo de referencia

- El intervalo de referencia son los percentiles 2,5–97,5 de la población sana.

💡 **Cómo se explica en la clase [B105-C24](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md):**
- P["poblacion sana<br/>N(100, 15)"] --> R["intervalo de referencia"]
- El intervalo de referencia es 69,5–132,6 u.a.; el índice de individualidad `CVi/CVg = 0,33`; el RCV es 16,2 %.
- 🎯 **Por qué importa:** Con tripulaciones pequeñas, el intervalo de la población general es poco sensible a los cambios personales, y un umbral con baja prevalencia da más falsas alarmas que aciertos. La decisión central: ¿cuándo un cambio de un indicador es real y qué umbral equilibra sensibilidad y valor predictivo?

📘 **Dónde se aprende** (1 clase): [B105-C24 · Indicadores clínicos y biomarcadores de vuelo](../programa/clases/B105/B105-C24-indicadores-clinicos-y-biomarcadores-de-vuelo/CLASE.md).

### Intervalo de revisión

- El intervalo de revisión `R` es el tiempo entre pedidos; la demora `L` es el tiempo entre pedir y recibir; el intervalo de protección es `T = R + L`.

💡 **Cómo se explica en la clase [B100-C03](../programa/clases/B100/B100-C03-gestion-de-inventarios-y-reposicion-de-suministros/CLASE.md):**
- La demora tecnológica `L` (180 d) pesa menos que el intervalo de revisión `R` (780 d): la ventana fija casi todo el nivel máximo.
- 🎯 **Por qué importa:** Con una reposición de 10 días basta una reserva pequeña; con una ventana sinódica de Marte la misma demanda exige guardar casi dos años y medio de consumo. La decisión central: ¿hasta qué nivel conviene reponer en cada ventana para que la probabilidad de quedarse sin existencias en el ciclo sea de un 5 %?

📘 **Dónde se aprende** (1 clase): [B100-C03 · Gestión de inventarios y reposición de suministros](../programa/clases/B100/B100-C03-gestion-de-inventarios-y-reposicion-de-suministros/CLASE.md).

### Intervalo de validez

- Un intervalo de validez es el rango de `x` cubierto por los patrones.
- El intervalo de validez es el rango de temperatura en que se contrastó el ajuste.

💡 **Cómo se explica en la clase [B60-C02](../programa/clases/B60/B60-C02-coeficientes-de-velocidad-dependientes-de-la-temperatura-y-bases-cineticas/CLASE.md):**
- ⚠️ **Error frecuente:** Evaluar fuera del intervalo de validez sin decirlo. Se corrige con 8.4.
- 🎯 **Por qué importa:** Un modelo de nube a 10 K usa coeficientes que se midieron o calcularon a otras temperaturas. La decisión central: ¿hasta dónde se puede confiar en un ajuste de `k(T)` fuera del intervalo donde se ajustó?

📘 **Dónde se aprende** (2 clases): [B13-C05 · Calibración instrumental](../programa/clases/B13/B13-C05-calibracion-instrumental/CLASE.md); [B60-C02 · Coeficientes de velocidad dependientes de la temperatura y bases cinéticas](../programa/clases/B60/B60-C02-coeficientes-de-velocidad-dependientes-de-la-temperatura-y-bases-cineticas/CLASE.md).

### Intervalo de verificación

- El intervalo de verificación es el tiempo máximo entre comprobaciones para que la probabilidad de vigencia no baje de un umbral.

🎯 **Por qué importa (clase B111-C04):** Falta la clase que trate la conciencia situacional de la tripulación. La decisión central: ¿cómo se cuantifica lo que el equipo sabe y cada cuánto debe verificarlo para que no se quede desactualizado?

📘 **Dónde se aprende** (1 clase): [B111-C04 · Conciencia situacional en operaciones de vuelo](../programa/clases/B111/B111-C04-conciencia-situacional-en-operaciones-de-vuelo/CLASE.md).

### Intervalo de Wilson

- El intervalo de Wilson al 95 % para una proporción `p̂` con `n` pruebas.

🎯 **Por qué importa (clase B88-C34):** Un FDIR no probado es una hipótesis. La decisión central: ¿cuántas inyecciones hacen falta para estimar la cobertura con una incertidumbre aceptable y qué fallas escapan?

📘 **Dónde se aprende** (1 clase): [B88-C34 · Pruebas de inyección de fallos](../programa/clases/B88/B88-C34-pruebas-de-inyeccion-de-fallos/CLASE.md).

### Intervalo juliano

- El intervalo juliano `365,25 d = 31 557 600 s` es la convención usada para el año en esta clase.

🎯 **Por qué importa (clase B13-C06):** Cuando un telémetro láser mide la distancia a la Luna, lo que mide es el tiempo que tarda un pulso en ir y volver. Un error de un nanosegundo en ese tiempo equivale a 15 centímetros de distancia.

📘 **Dónde se aprende** (1 clase): [B13-C06 · Patrones de longitud y tiempo](../programa/clases/B13/B13-C06-patrones-de-longitud-y-tiempo/CLASE.md).

### Intervalo Δ

- El intervalo `Δ` es el tiempo entre siembras.

🎯 **Por qué importa (clase B115-C05):** Cosechar mucho un día y nada los siguientes es inútil si lo cosechado se estropea. La decisión central: ¿cada cuántos días se siembra y cuántas plantas por lote hacen falta para cubrir la demanda diaria con una probabilidad aceptable, y qué área exige?

📘 **Dónde se aprende** (1 clase): [B115-C05 · Ciclos de producción y calendarización de cultivos](../programa/clases/B115/B115-C05-ciclos-de-produccion-y-calendarizacion-de-cultivos/CLASE.md).

### Intolerancia ortostática

- La intolerancia ortostática es la dificultad para mantener la presión al ponerse de pie (descrita por la NASA como un efecto posvuelo, consultado el 2026-11-10).

🎯 **Por qué importa (clase B105-C01):** En la Tierra la gravedad empuja la sangre hacia los pies y el sistema cardiovascular lo compensa en cada postura. En microgravedad esa carga desaparece y el cuerpo se reajusta; al volver, la compensación puede no bastar.

📘 **Dónde se aprende** (1 clase): [B105-C01 · Respuesta cardiovascular a microgravedad](../programa/clases/B105/B105-C01-respuesta-cardiovascular-a-microgravedad/CLASE.md).

### Invariante

- Es lineal si la salida de una suma es la suma de las salidas, e invariante si no depende de cuándo empieza la serie.
- Un modelo es lineal si cumple superposición (lo precisa C03), invariante si sus parámetros no cambian con el tiempo, continuo si el tiempo es una variable real `t` y discreto si solo existe en instantes `kT`.
- Un invariante es una cantidad que la transformación no debe cambiar.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B16-C01](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md):**
- El modelo de la sección 8.2 es lineal (el estado aparece solo multiplicado por constantes), invariante (`J` no cambia), continuo y de orden 2.
- 🎯 **Por qué importa:** Un telescopio espacial tiene que apuntar a una estrella y mantenerse allí. El telescopio Hubble lo hace con una desviación de no más de 0,007 segundos de arco durante al menos 24 horas (fuente S2).

📘 **Dónde se aprende** (6 clases): [B15-C07 · Filtrado digital](../programa/clases/B15/B15-C07-filtrado-digital/CLASE.md); [B16-C01 · Modelos dinámicos y estados](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md); [B71-C17 · Movimientos en planos orbitales](../programa/clases/B71/B71-C17-movimientos-en-planos-orbitales/CLASE.md); [B71-C20 · Propagador kepleriano verificable](../programa/clases/B71/B71-C20-propagador-kepleriano-verificable/CLASE.md); [B96-C20 · Simulación de jornada de control de misión](../programa/clases/B96/B96-C20-simulacion-de-jornada-de-control-de-mision/CLASE.md); [B98-C02 · Sistemas de decisión autónomos y máquinas de estados de comportamiento](../programa/clases/B98/B98-C02-sistemas-de-decision-autonomos-y-maquinas-de-estados-de-comportamiento/CLASE.md).

### Invariante adiabático

- El invariante adiabático de una órbita atrapada es el área `J` que encierra en el plano `(φ, q)`.

🎯 **Por qué importa (clase B73-C12):** Muchas resonancias observadas (satélites, planetas migrantes, asteroides) no son primordiales: los cuerpos entraron en ellas. Saber cuándo una captura es segura y cuándo es improbable, y cuándo un cuerpo atrapado debe escapar, evita explicaciones erróneas.

📘 **Dónde se aprende** (1 clase): [B73-C12 · Captura y escape resonante](../programa/clases/B73/B73-C12-captura-y-escape-resonante/CLASE.md).

### Invariante en el tiempo

- Un sistema es lineal si la salida de `αx₁ + βx₂` es `αy₁ + βy₂`, e invariante en el tiempo si retrasar la entrada solo retrasa la salida.
- Es invariante en el tiempo si retrasar la entrada `d` segundos solo retrasa la salida `d` segundos.

🎯 **Por qué importa (clase B15-C08):** Un termistor a bordo de una nave no mide la temperatura del instante: mide una versión retrasada y suavizada, porque su cuerpo tarda en calentarse o enfriarse. Si la nave entra en eclipse y el entorno baja 50 K de golpe, el sensor irá bajando poco a poco.

📘 **Dónde se aprende** (2 clases): [B15-C08 · Convolución y respuesta impulsional](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md); [B16-C03 · Sistemas lineales invariantes](../programa/clases/B16/B16-C03-sistemas-lineales-invariantes/CLASE.md).

### Invariantes

- Los invariantes `I₁ = tr S`, `I₂ = (I₁² − tr S²)/2` e `I₃ = det S` no cambian al girar los ejes.

💡 **Cómo se explica en la clase [B84-C22](../programa/clases/B84/B84-C22-tension-deformacion-y-elasticidad-lineal/CLASE.md):**
- *Descripción textual:* el tensor da los autovalores y los invariantes, dos vías para von Mises, la deformación y la energía, y el margen.
- 🎯 **Por qué importa:** Una tensión de 120 MPa en una dirección no dice si la pieza cede: la fluencia depende de la combinación de las seis componentes. La decisión central: ¿cede el material en este punto y con qué margen, dado un estado de tensión 3D?

📘 **Dónde se aprende** (1 clase): [B84-C22 · Tensión, deformación y elasticidad lineal](../programa/clases/B84/B84-C22-tension-deformacion-y-elasticidad-lineal/CLASE.md).

### Inversa

- La inversa de una rotación es su traspuesta: `R⁻¹ = Rᵀ`.
- La inversa `f⁻¹` deshace `f`: `f⁻¹(f(x)) = x`.
- La inversa de `A`, si existe, cumple `A A⁻¹ = I`.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B04-C04](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md):**
- Si `f(a) = k a^(3/2)`, su inversa es `a = (P/k)^(2/3)`.
- *Descripción textual:* una entrada `x` con su unidad pasa por la regla `f` y produce una salida `y` con su unidad; de las parejas se forma la gráfica; la inversa devuelve de `y` a `x`.
- 🎯 **Por qué importa:** Un astrónomo no solo calcula un valor: pregunta «¿qué pasa con el periodo de un planeta si su órbita es el doble de grande?». Responderlo con un solo caso no basta; hace falta la regla que liga ambas magnitudes.

📘 **Dónde se aprende** (4 clases): [B04-C04 · Funciones y gráficas](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md); [B04-C15 · Rotación de puntos y ejes](../programa/clases/B04/B04-C15-rotacion-de-puntos-y-ejes/CLASE.md); [B10-C04 · Determinantes y soluciones](../programa/clases/B10/B10-C04-determinantes-y-soluciones/CLASE.md); [B85-C24 · Efectos de la radiación ionizante en materiales y electrónica](../programa/clases/B85/B85-C24-efectos-de-la-radiacion-ionizante-en-materiales-y-electronica/CLASE.md).

### Inversamente proporcionales

- Son inversamente proporcionales si su producto `x·y` es constante: `y = k/x`.

🎯 **Por qué importa (clase B03-C10):** Un panel solar en órbita de Marte no recibe la misma energía que uno en órbita de la Tierra. ¿Cuánta menos?

📘 **Dónde se aprende** (1 clase): [B03-C10 · Proporcionalidad directa e inversa](../programa/clases/B03/B03-C10-proporcionalidad-directa-e-inversa/CLASE.md).

### Inversión

- La inversión es hallar `ψ` a partir de los conteos.
- La inversión busca los parámetros que explican las observaciones.

💡 **Cómo se explica en la clase [B32-C08](../programa/clases/B32/B32-C08-sintesis-espectral-e-inversion-de-perfiles/CLASE.md):**
- Probar recetas hasta que el plato coincida con la muestra: la inversión busca los parámetros cuya síntesis se parece más al dato.
- *Descripción textual:* los parámetros generan el espectro sintético con ruido; la inversión los recupera y se evalúa su incertidumbre.
- ⚠️ **Error frecuente:** Confundir síntesis e inversión. Se corrige con la sección 6.
- 🎯 **Por qué importa:** Una inversión sin barras de error no sirve. La decisión central: ¿qué parámetros se recuperan y con qué incertidumbre?

📘 **Dónde se aprende** (4 clases): [B32-C08 · Síntesis espectral e inversión de perfiles](../programa/clases/B32/B32-C08-sintesis-espectral-e-inversion-de-perfiles/CLASE.md); [B34-C05 · Diagnóstico de densidad electrónica coronal](../programa/clases/B34/B34-C05-diagnostico-de-densidad-electronica-coronal/CLASE.md); [B38-C04 · Historia de formación estelar a partir de poblaciones resueltas](../programa/clases/B38/B38-C04-historia-de-formacion-estelar-a-partir-de-poblaciones-resueltas/CLASE.md); [B57-C18 · Volcanismo y monitoreo](../programa/clases/B57/B57-C18-volcanismo-y-monitoreo/CLASE.md).

### Inversión de orden

- Mover y esperar: pasos cortos con espera de la imagen. Inversión de orden: cambio de signo de la orden.

🎯 **Por qué importa (clase B101-C10):** Cuanto más tarda en llegar la imagen y la orden, más difícil es corregir. La decisión central: ¿con qué retardo total y qué ganancia el operador puede capturar con éxito y cuándo conviene pasar a «mover y esperar»?

📘 **Dónde se aprende** (1 clase): [B101-C10 · Simulación de una tarea tripulada con manipulador](../programa/clases/B101/B101-C10-simulacion-de-una-tarea-tripulada-con-manipulador/CLASE.md).

### Inversión de prioridad

- La inversión de prioridad retrasa a A por una tarea M de menor prioridad.

🎯 **Por qué importa (clase B88-C28):** El caso Pathfinder mostró que un error de concurrencia puede aparecer solo en operación y provocar reinicios por watchdog. La decisión central: ¿cómo se garantiza que una tarea de alta prioridad no quede bloqueada indefinidamente por otras de menor prioridad?

📘 **Dónde se aprende** (1 clase): [B88-C28 · Inversión de prioridad y deadlocks](../programa/clases/B88/B88-C28-inversion-de-prioridad-y-deadlocks/CLASE.md).

### Inversionista acreditado

- Un inversionista acreditado es una categoría legal cuya definición no se consultó.

🎯 **Por qué importa (clase B126-C06):** [B124-C19](../../../tronco-comun/B124-industria-economia-etica-y-proyectos-espaciales.md) redacta propuestas de misión, no financieras. La decisión central: ¿qué cifra se muestra, con qué rótulo y con qué rango, de modo que un tercero pueda comprobarla?

📘 **Dónde se aprende** (1 clase): [B126-C06 · Presentación financiera ante inversionistas con evidencia](../programa/clases/B126/B126-C06-presentacion-financiera-ante-inversionistas-con-evidencia/CLASE.md).

### Inyección

- La inyección es el estado en que la etapa final suelta la carga.

💡 **Cómo se explica en la clase [B77-C13](../programa/clases/B77/B77-C13-inyeccion-y-dispersion-orbital/CLASE.md):**
- El perigeo casi no depende de `v` (inyección en el perigeo) y la derivada respecto de `γ` es 0 en el nominal.
- *Descripción textual:* los errores de inyección se propagan a los elementos por linealización (jacobiano) y por Monte Carlo; ambas desviaciones se comparan y la diferencia de la media revela el efecto de segundo orden.
- 🎯 **Por qué importa:** La órbita lograda es una variable aleatoria. La decisión central: ¿cuánto vale la dispersión de cada elemento orbital y cuándo basta la propagación lineal?

📘 **Dónde se aprende** (1 clase): [B77-C13 · Inyección y dispersión orbital](../programa/clases/B77/B77-C13-inyeccion-y-dispersion-orbital/CLASE.md).

### Inyección de detalle

- La inyección de detalle suma a la banda de baja resolución, replicada, el detalle de alta frecuencia de la pancromática: `F_b = MS_b + g_b (Pan − Pan_baja)`, con `Pan_baja` el promedio de bloques de la pancromática replicado.

💡 **Cómo se explica en la clase [B15-C24](../programa/clases/B15/B15-C24-fusion-de-imagenes-de-distintos-sensores/CLASE.md):**
- Inyección de detalle con modulación (como aquí): conserva la consistencia.
- 🎯 **Por qué importa:** Un mapa de cobertura exige distinguir objetos pequeños (caminos, parcelas) y también su firma espectral (si son vegetación o suelo). Ninguna imagen entrega ambas cosas a la vez.

📘 **Dónde se aprende** (1 clase): [B15-C24 · Fusión de imágenes de distintos sensores](../programa/clases/B15/B15-C24-fusion-de-imagenes-de-distintos-sensores/CLASE.md).

### Inyección de errores

- Calidad es la fracción de objetos sin errores. Inyección de errores es introducir fallos conocidos para probar las reglas.

🎯 **Por qué importa (clase B119-C07):** C04 estudia qué se registra y calcula el período; esta clase estudia la calidad del registro como sistema y la auditoría de coherencia, que ninguna otra clase trata. La decisión central: ¿qué reglas mínimas permiten confiar en un registro nacional y cómo se mide su calidad?

📘 **Dónde se aprende** (1 clase): [B119-C07 · Registro nacional de objetos](../programa/clases/B119/B119-C07-registro-nacional-de-objetos/CLASE.md).

### Inyección translunar (TLI)

- La inyección translunar (TLI) es el impulso en el perigeo.

🎯 **Por qué importa (clase B76-C07):** Un diseño preliminar de misión empieza por el presupuesto de velocidad. La decisión central: ¿cuánto `Δv` cuestan la salida de la Tierra y la captura en la Luna, y cuánto cambia la segunda según la órbita lunar elegida?

📘 **Dónde se aprende** (1 clase): [B76-C07 · Maniobras de inserción cislunar](../programa/clases/B76/B76-C07-maniobras-de-insercion-cislunar/CLASE.md).

### Inyección–recuperación

- La inyección–recuperación mide la completitud.

🎯 **Por qué importa (clase B29-C20):** Una detección sin completitud no se puede contar: ¿cuántos planetas se perdieron? La inyección y recuperación responde.

📘 **Dónde se aprende** (1 clase): [B29-C20 · Proyecto de detección exoplanetaria](../programa/clases/B29/B29-C20-proyecto-de-deteccion-exoplanetaria/CLASE.md).

### Ion

- Un ion es un átomo o grupo con carga neta: un catión (positivo) pierde electrones; un anión (negativo) los gana.

💡 **Cómo se explica en la clase [B06-C04](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md):**
- Para una molécula se suman las valencias de todos los átomos; para un ion se resta la carga positiva o se suma la negativa.
- Esta estimación es un orden de magnitud: en medios con agua las cargas se apantallan y la energía efectiva es mucho menor, y en un cristal cada ion interacciona con muchos vecinos.
- ⚠️ **Error frecuente:** Olvidar restar o sumar la carga del ion al contar electrones. Se corrige con el ejercicio 1 y la sección 8.1.
- 🎯 **Por qué importa:** Las muestras del asteroide Bennu contienen amoníaco, pero en gran parte no como gas libre: los autores concluyen que la mayor parte probablemente quedó retenida como sales o ligada a minerales arcillosos y a materia orgánica, porque el amoníaco libre es muy volátil y se pierde (S1).

📘 **Dónde se aprende** (1 clase): [B06-C04 · Enlaces iónicos y covalentes](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md).

### Iones isobáricos

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C08):** La resolución de masa decide qué especies se separan. La decisión central: ¿qué tiempo de vuelo, qué dispersión y qué resolución permiten distinguir dos iones casi isobáricos?

📘 **Dónde se aprende** (1 clase): [B47-C08 · Espectrómetros de masas orbitales](../programa/clases/B47/B47-C08-espectrometros-de-masas-orbitales/CLASE.md).

### Ionización por rayos cósmicos

- La ionización por rayos cósmicos de `H₂` da `H₂⁺`, que reacciona con `H₂` para formar `H3+`.

🎯 **Por qué importa (clase B55-C04):** Una nube molecular fría es un reactor lento sostenido por una fuente débil de ionización. Entender el balance de una sola especie clave enseña a leer cualquier red.

📘 **Dónde se aprende** (1 clase): [B55-C04 · Química de nubes moleculares](../programa/clases/B55/B55-C04-quimica-de-nubes-moleculares/CLASE.md).

### Ionizado

- En un sólido las partículas ocupan posiciones casi fijas; en un líquido están juntas pero se deslizan; en un gas están lejos y se mueven libres; en un plasma el gas está parcialmente o totalmente ionizado, es decir, hay electrones libres e iones.

🎯 **Por qué importa (clase B06-C10):** En Marte, la temperatura media es 214 K y la presión media en superficie 6,36 mb (S1). Ese valor está casi en el punto triple del agua, la presión mínima a la que puede existir agua líquida (S2).

📘 **Dónde se aprende** (1 clase): [B06-C10 · Estados de la materia](../programa/clases/B06/B06-C10-estados-de-la-materia/CLASE.md).

### Ionizado caliente

- El medio neutro frío (CNM) y el medio neutro tibio (WNM) son gas de hidrógeno atómico; el medio ionizado tibio (WIM) y el ionizado caliente (HIM) están ionizados.

💡 **Cómo se explica en la clase [B25-C03](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md):**
- C --> E["Ionizado caliente<br/>~10⁶ K, 0,0065"]
- 🎯 **Por qué importa:** Las estrellas nacen del gas y devuelven gas enriquecido; el medio interestelar (MIS) es el almacén y el escenario de ese ciclo. Pero «gas» sirve de poco: un volumen del MIS puede estar a `10 K` o a `10⁶ K`, y su densidad variar un factor 10⁷ de un punto a otro.

📘 **Dónde se aprende** (1 clase): [B25-C03 · Medio interestelar multifásico](../programa/clases/B25/B25-C03-medio-interestelar-multifasico/CLASE.md).

### Ion–molécula

- Una reacción ion–molécula ocurre entre un ion y una molécula neutra y casi no tiene barrera.

💡 **Cómo se explica en la clase [B55-C03](../programa/clases/B55/B55-C03-reacciones-en-medio-interestelar/CLASE.md):**
- Las reacciones ion–molécula son rápidas incluso en el frío; las neutro–neutro con barrera necesitan calor.
- Dos reacciones ilustrativas: una ion–molécula con `α = 10⁻⁹ cm³ s⁻¹` y sin barrera, y una neutro–neutro con `α = 10⁻¹⁰` y barrera `γ = 1500 K`.
- 🎯 **Por qué importa:** En el espacio la densidad es tan baja que una reacción puede tardar siglos o millones de años, y la temperatura de 10 K cierra casi todas las reacciones con barrera. Saber cuáles ocurren define qué moléculas pueden existir.

📘 **Dónde se aprende** (1 clase): [B55-C03 · Reacciones en medio interestelar](../programa/clases/B55/B55-C03-reacciones-en-medio-interestelar/CLASE.md).

### IoU

- La IoU (intersección sobre unión) es `|A ∩ B|/|A ∪ B|`; el coeficiente de Dice es `2|A ∩ B|/(|A| + |B|)`.
- El IoU (*intersection over union*, índice de Jaccard) es `|P ∩ V| / |P ∪ V|` entre la máscara predicha `P` y la verdadera `V` (S2).
- El IoU de dos regiones es `área(A ∩ B)/área(A ∪ B)`.

💡 **Cómo se explica en la clase [B15-C13](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md):**
- Para dos cuadrados de 10 × 10 desplazados 2 columnas, la intersección es de 80 píxeles y la unión de 120: IoU `= 0,6667`, Dice `= 160/200 = 0,8`.
- Entre ambas hay una relación: `Dice = 2 IoU/(1 + IoU)`.
- 🎯 **Por qué importa:** Medir el área de las manchas solares, el porcentaje de nubes de una escena o el tamaño de un cráter exige delimitar el objeto. La delimitación no es neutra: un umbral distinto cambia el área.

📘 **Dónde se aprende** (3 clases): [B15-C13 · Segmentación de imágenes](../programa/clases/B15/B15-C13-segmentacion-de-imagenes/CLASE.md); [B17-C11 · Redes de segmentación semántica de imágenes](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md); [B103-C08 · Métricas de evaluación de percepción](../programa/clases/B103/B103-C08-metricas-de-evaluacion-de-percepcion/CLASE.md).

### I/Q

- Las muestras I/Q son la parte real e imaginaria de la señal en banda base.

💡 **Cómo se explica en la clase [B46-C10](../programa/clases/B46/B46-C10-radioastronomia-mediante-sdr/CLASE.md):**
- Un SDR real tiene pico de continua, desbalance I/Q, ganancia inestable y espurios que el laboratorio no modela.
- IQ["muestras I/Q"] --> W["ventana de Hann"]
- 🎯 **Por qué importa:** Promediar espectros es la forma práctica de aplicar la ecuación del radiómetro con un instrumento barato, pero la ventana cambia el ancho de banda efectivo. La decisión central: ¿cuántos espectros promediar para detectar una línea débil?

📘 **Dónde se aprende** (1 clase): [B46-C10 · Radioastronomía mediante SDR](../programa/clases/B46/B46-C10-radioastronomia-mediante-sdr/CLASE.md).

### Irradiancia

- La irradiancia es la potencia por unidad de área (W/m²).
- La irradiancia `f` es la potencia por unidad de área que llega (W/m²) y la luminosidad `L` la potencia total que emite (W).
- La irradiancia `S` es la potencia por unidad de área (W/m²).
- *(y 7 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C10](../programa/clases/B03/B03-C10-proporcionalidad-directa-e-inversa/CLASE.md):**
- La irradiancia es `S = P/(4πd²)`, que es proporcional a `1/d²`.
- Pregunta. ¿Qué fracción de la irradiancia terrestre recibe Marte?
- 🎯 **Por qué importa:** Un panel solar en órbita de Marte no recibe la misma energía que uno en órbita de la Tierra. ¿Cuánta menos?

📘 **Dónde se aprende** (10 clases): [B03-C10 · Proporcionalidad directa e inversa](../programa/clases/B03/B03-C10-proporcionalidad-directa-e-inversa/CLASE.md); [B04-C05 · Funciones exponenciales y logarítmicas](../programa/clases/B04/B04-C05-funciones-exponenciales-y-logaritmicas/CLASE.md); [B09-C18 · Integrales dobles y triples](../programa/clases/B09/B09-C18-integrales-dobles-y-triples/CLASE.md); [B45-C01 · Radiometría y fotometría](../programa/clases/B45/B45-C01-radiometria-y-fotometria/CLASE.md); [B54-C03 · Equilibrio radiativo](../programa/clases/B54/B54-C03-equilibrio-radiativo/CLASE.md); [B56-C08 · Habitabilidad de Marte](../programa/clases/B56/B56-C08-habitabilidad-de-marte/CLASE.md) y 4 más.

### Irradiancia solar

- La irradiancia solar `S = L/(4π d²)` es la potencia solar por unidad de superficie a la distancia `d`, con `L` la luminosidad del Sol.
- La irradiancia solar cae con el cuadrado de la distancia.

🎯 **Por qué importa (clase B13-C16):** Un sensor de temperatura pegado a un panel de una nave devuelve una resistencia. Convertirla en kelvin exige calibrarlo contra referencias conocidas, y comprobar que la temperatura medida concuerda con un balance térmico previsto.

📘 **Dónde se aprende** (2 clases): [B13-C16 · Calibración térmica](../programa/clases/B13/B13-C16-calibracion-termica/CLASE.md); [B54-C12 · Interacción con radiación solar](../programa/clases/B54/B54-C12-interaccion-con-radiacion-solar/CLASE.md).

### Irradiancia solar total

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B43-C19):** La seguridad empieza por saber cuán grande es el riesgo. La decisión central: ¿cuánta potencia y qué temperatura aparecen en el foco, cómo se balancea la montura y cuánto polvo es aceptable?

📘 **Dónde se aprende** (1 clase): [B43-C19 · Seguridad y mantenimiento](../programa/clases/B43/B43-C19-seguridad-y-mantenimiento/CLASE.md).

### Irreducible

- Una cadena irreducible puede llegar de cualquier estado a cualquier otro;

🎯 **Por qué importa (clase B12-C13):** Una posterior de diez o veinte parámetros (órbita, calibración, ruido) no se puede tabular. Pero sí se pueden generar muestras que sigan su forma, aunque no se conozca su normalización.

📘 **Dónde se aprende** (1 clase): [B12-C13 · Cadenas de Markov y muestreo](../programa/clases/B12/B12-C13-cadenas-de-markov-y-muestreo/CLASE.md).

### Irregular

- Los tipos espiral, elíptica e irregular describen su forma (S1).

🎯 **Por qué importa (clase B01-C15):** La galaxia de la línea Hα (C01) está a 43 Mpc, pero ¿qué significa eso comparado con lo que ya conoces? ¿Está más lejos o más cerca que Andrómeda?

📘 **Dónde se aprende** (1 clase): [B01-C15 · Galaxias y agrupaciones cósmicas](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md).

### ISCO

- El ISCO es la órbita circular estable más interna.

💡 **Cómo se explica en la clase [B27-C07](../programa/clases/B27/B27-C07-metricas-de-agujeros-negros/CLASE.md):**
- El ISCO es el radio donde `E(r)` es mínimo.
- Con espín prógrado crece la energía liberable y el ISCO baja: `4,2330` (`a = 0,5`), `2,3209` (`0,9`), `1,2370` (`0,998`).
- 🎯 **Por qué importa:** El espín cambia el ISCO y, con él, cuánta energía se libera: de `5,7 %` a más de `30 %` de la masa en reposo. La decisión central: ¿dónde están el horizonte y el ISCO para un espín dado y qué eficiencia implica?

📘 **Dónde se aprende** (1 clase): [B27-C07 · Métricas de agujeros negros](../programa/clases/B27/B27-C07-metricas-de-agujeros-negros/CLASE.md).

### Isentrópico

- Un proceso isentrópico es adiabático y reversible.
- Un proceso isentrópico tiene `s_gen = 0`.

💡 **Cómo se explica en la clase [B79-C11](../programa/clases/B79/B79-C11-segunda-ley-y-entropia/CLASE.md):**
- ⚠️ **Error frecuente:** Confundir trabajo perdido con la diferencia respecto al isentrópico. Se corrige con 8.2.
- 🎯 **Por qué importa:** Ninguna clase del tronco trata entropía ni irreversibilidad, necesarias para entender por qué un compresor real consume más que uno ideal y por qué un choque pierde presión total. La decisión central: ¿cuánta capacidad de trabajo pierde cada componente y por qué mecanismo?

📘 **Dónde se aprende** (2 clases): [B79-C11 · Segunda ley y entropía](../programa/clases/B79/B79-C11-segunda-ley-y-entropia/CLASE.md); [B79-C12 · Procesos adiabáticos e isentrópicos](../programa/clases/B79/B79-C12-procesos-adiabaticos-e-isentropicos/CLASE.md).

### ISO

- La exposición es el tiempo con el obturador abierto; el ISO es la amplificación de la señal; la apertura relativa del objetivo (f/) controla la luz.

🎯 **Por qué importa (clase B08-C19):** Un teléfono o una cámara réflex puede captar la Vía Láctea o la Luna con detalle, pero una exposición demasiado larga convierte las estrellas en rayas. La pregunta motivadora: ¿cuánto puedo exponer y con qué focal para obtener estrellas puntuales, y qué debo anotar para que la foto sirva como dato?

📘 **Dónde se aprende** (1 clase): [B08-C19 · Fotografía astronómica elemental](../programa/clases/B08/B08-C19-fotografia-astronomica-elemental/CLASE.md).

### ISO 12312-2

- ISO 12312-2 es la norma internacional para filtros de observación directa del Sol; la AAS la considera el referente de seguridad, aunque advierte que la conformidad requiere pruebas de un laboratorio acreditado, no una etiqueta (S2).

💡 **Cómo se explica en la clase [B08-C16](../programa/clases/B08/B08-C16-observacion-solar-con-filtros-certificados/CLASE.md):**
- B -->|"Visor"| D["Visor ISO 12312-2<br/>sin óptica, de proveedor verificado"]
- Tú aplicas lo que aprendes: la AAS advierte que una etiqueta de conformidad ISO 12312-2 no basta y que algunas empresas imprimen falsamente el nombre de un fabricante listado (S2);
- 🎯 **Por qué importa:** Una persona que mira un eclipse parcial con gafas falsas, o enfoca el Sol con un telescopio sin filtro frontal, puede quedar con una lesión permanente. La pregunta motivadora: ¿cómo observo el Sol sin dañarme y sin dañar a otros?

📘 **Dónde se aprende** (1 clase): [B08-C16 · Observación solar con filtros certificados](../programa/clases/B08/B08-C16-observacion-solar-con-filtros-certificados/CLASE.md).

### ISO 8601

- Un registro (fila) contiene los campos: fecha y hora, lugar, objeto, método, instrumento, condiciones, procedencia, observador y notas. ISO 8601 es el formato de fecha y hora `AAAA-MM-DDTHH:MM`; la `T` separa fecha y hora.

💡 **Cómo se explica en la clase [B08-C17](../programa/clases/B08/B08-C17-registro-sistematico-en-bitacora/CLASE.md):**
- Anota la fecha y hora en UT en formato ISO 8601 (`2025-11-05T04:00`).
- 🎯 **Por qué importa:** Un dato sin fecha, sin lugar o sin procedencia es una anécdota. La pregunta motivadora: ¿qué debo anotar para que mi observación se pueda repetir, revisar y comparar?

📘 **Dónde se aprende** (1 clase): [B08-C17 · Registro sistemático en bitácora](../programa/clases/B08/B08-C17-registro-sistematico-en-bitacora/CLASE.md).

### Isócrona

- Una isócrona es la curva del diagrama HR que reúne estrellas de la misma edad y composición.

🎯 **Por qué importa (clase B24-C19):** La edad de una estrella aislada es difícil de medir; la de un cúmulo se puede leer en su diagrama HR, porque las estrellas más masivas ya han salido de la secuencia principal y el «punto de desvío» marca la edad. Esas edades fijan la cronología de la Galaxia y calibran los modelos.

📘 **Dónde se aprende** (1 clase): [B24-C19 · Cúmulos y edades estelares](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md).

### Isómeros

- Los isómeros son moléculas con la misma fórmula y distinta estructura (etanol y éter dimetílico, ambos `C₂H₆O`).

💡 **Cómo se explica en la clase [B06-C16](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md):**
- Puedes dar la fórmula molecular (qué átomos y cuántos, suficiente para la masa y la insaturación) o la fórmula estructural (cómo están unidos, necesaria para saber el grupo funcional y distinguir isómeros).
- ⚠️ **Error frecuente:** Confundir isómeros con la misma sustancia. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** El análisis de las muestras de Bennu detectó aminoácidos (incluidos 14 de los 20 usados en la biología terrestre), aminas, formaldehído, ácidos carboxílicos, hidrocarburos aromáticos policíclicos y heterociclos de nitrógeno, entre ellos las cinco nucleobases del ADN y el ARN, además de unas 10 000 especies nitrogenadas (S1).

📘 **Dónde se aprende** (1 clase): [B06-C16 · Química orgánica esencial](../programa/clases/B06/B06-C16-quimica-organica-esencial/CLASE.md).

### Isoterma

- Una atmósfera isoterma tiene `T` constante.
- La expansión isoterma mantiene `T_e` por aporte de calor de los electrones.

💡 **Cómo se explica en la clase [B54-C04](../programa/clases/B54/B54-C04-presion-y-densidad/CLASE.md):**
- Para una atmósfera isoterma de Marte (`H = R T/(M g)`), RK4 con 4000 pasos hasta 30 km da `P = 41,279279 Pa`, igual a la exponencial `P₀ e^{−z/H}`; la diferencia relativa es `5,7 × 10⁻¹⁵`.
- La presión cae a `P₀/e` en `z = H` y a `P₀/1000` en `H ln 1000`: para la Tierra (isoterma ilustrativa a 288 K) `8,42 km` y `58,1 km`.
- 🎯 **Por qué importa:** La densidad del gas fija el empuje, el arrastre, la opacidad y el peso de la atmósfera, y sale de una sola fórmula si el gas es ideal. La pregunta motivadora: ¿cuánto pesa la atmósfera de cada mundo sobre un metro cuadrado, y hasta dónde vale el gas ideal?

📘 **Dónde se aprende** (2 clases): [B54-C04 · Presión y densidad](../programa/clases/B54/B54-C04-presion-y-densidad/CLASE.md); [B78-C09 · Propulsión por plasma](../programa/clases/B78/B78-C09-propulsion-por-plasma/CLASE.md).

### Isotermo

- Un gas isotermo mantiene la misma temperatura mientras se comprime.

🎯 **Por qué importa (clase B24-C01):** Toda estrella es un trozo de gas interestelar que se contrajo. Sin saber cuándo la gravedad vence a la presión no se entiende por qué las estrellas nacen en nubes frías y densas y no en el gas tenue del medio interestelar, ni por qué la masa de las estrellas depende del entorno.

📘 **Dónde se aprende** (1 clase): [B24-C01 · Colapso de nubes moleculares](../programa/clases/B24/B24-C01-colapso-de-nubes-moleculares/CLASE.md).

### Isótopos

- Dos átomos son isótopos del mismo elemento si tienen igual `Z` pero distinto número de neutrones `N`, de modo que `A = Z + N`.

💡 **Cómo se explica en la clase [B06-C03](../programa/clases/B06/B06-C03-isotopos-y-masa-atomica/CLASE.md):**
- Los isótopos de algunos elementos (H, Li, B, C, N, O, Mg, Si, S, Cl…) se reparten de modo algo distinto según el origen del material: agua de mar, roca, aire, organismos (S2).
- *Descripción textual:* tres cajas de isótopos con su masa y su abundancia alimentan un promedio ponderado que produce el peso atómico; de las mismas abundancias salen las razones isotópicas.
- 🎯 **Por qué importa:** El carbono del Sol, ¿es igual que el de la Tierra? Una forma de preguntarlo con rigor es comparar cuántos átomos de carbono-12 hay por cada uno de carbono-13.

📘 **Dónde se aprende** (1 clase): [B06-C03 · Isótopos y masa atómica](../programa/clases/B06/B06-C03-isotopos-y-masa-atomica/CLASE.md).

### Isotropía

- La isotropía supone igual probabilidad en todas direcciones.

🎯 **Por qué importa (clase B28-C11):** Que dos señales coincidan no prueba que estén relacionadas: la pregunta es cuán probable es la coincidencia por azar. Una probabilidad fortuita muy baja es lo que convierte una coincidencia en un descubrimiento.

📘 **Dónde se aprende** (1 clase): [B28-C11 · Coincidencias entre observatorios](../programa/clases/B28/B28-C11-coincidencias-entre-observatorios/CLASE.md).

### Isp

- El Isp (impulso específico) mide la eficiencia del propulsor.

💡 **Cómo se explica en la clase [B118-C07](../programa/clases/B118/B118-C07-estrategias-de-evasion/CLASE.md):**
- A --> F["Δm = m0 (1 - e^(-Δv/(Isp g0)))"]
- El ejemplo conductor es un satélite sintético de 500 kg e Isp 220 s en una órbita circular de 550 km que ejecuta un impulso tangencial de 0,2 m/s dos órbitas antes del TCA.
- 🎯 **Por qué importa:** La evasión es la respuesta operativa a una conjunción, pero cada maniobra cuesta combustible y vida útil. La decisión central: ¿cuánto Δv hace falta para lograr una separación dada y cuánto más cuesta decidir tarde?

📘 **Dónde se aprende** (1 clase): [B118-C07 · Estrategias de evasión](../programa/clases/B118/B118-C07-estrategias-de-evasion/CLASE.md).

### ISW

- El ISW surge de `dΦ/dη ≠ 0`.

💡 **Cómo se explica en la clase [B40-C09](../programa/clases/B40/B40-C09-efecto-sachs-wolfe-y-efecto-sachs-wolfe-integrado/CLASE.md):**
- *Descripción textual:* la integral de Bessel da la meseta de SW; la caída de los potenciales por Λ fija el ISW.
- Descripción larga: los potenciales decaen un 21 % y el ISW se opone a SW.
- ⚠️ **Error frecuente:** Tomar la cota como el ISW real. Se corrige con 8.3.
- 🎯 **Por qué importa:** SW domina las escalas grandes; el ISW es una señal de la energía oscura. La decisión central: ¿qué amplitud tiene la meseta y cuánto decaen los potenciales?

📘 **Dónde se aprende** (1 clase): [B40-C09 · Efecto Sachs-Wolfe y efecto Sachs-Wolfe integrado](../programa/clases/B40/B40-C09-efecto-sachs-wolfe-y-efecto-sachs-wolfe-integrado/CLASE.md).

### Ítem

- Un ítem describe una escena.

💡 **Cómo se explica en la clase [B14-C25](../programa/clases/B14/B14-C25-catalogos-de-datos-geoespaciales-y-metadatos-stac/CLASE.md):**
- Cada ítem del laboratorio tiene `type: Feature`, `id`, `bbox`, `geometry` (un polígono GeoJSON), `properties` (con `fecha` y `nubosidad_pct`) y `assets` (con un enlace ficticio).
- Un ítem ocupa unos 337 caracteres de JSON: mucho menos que la escena que describe.
- 🎯 **Por qué importa:** Un satélite produce miles de escenas al día. Para estudiar una inundación necesitas las que cubren una región, en unas fechas, con poca nube.

📘 **Dónde se aprende** (1 clase): [B14-C25 · Catálogos de datos geoespaciales y metadatos (STAC)](../programa/clases/B14/B14-C25-catalogos-de-datos-geoespaciales-y-metadatos-stac/CLASE.md).

### Iteración

- Una iteración es una vuelta.

💡 **Cómo se explica en la clase [B07-C05](../programa/clases/B07/B07-C05-bucles-y-simulaciones-sencillas/CLASE.md):**
- Una simulación es como una película hecha de fotogramas: cada iteración es una foto del estado (posición, velocidad) y pasar a la siguiente aplica la regla del modelo durante un instante `dt`.
- 🎯 **Por qué importa:** Una simulación es un bucle: calcula el estado siguiente a partir del actual, una y otra vez. Si el paso es demasiado grande, el resultado se aparta de la realidad; si es demasiado pequeño, tarda.

📘 **Dónde se aprende** (1 clase): [B07-C05 · Bucles y simulaciones sencillas](../programa/clases/B07/B07-C05-bucles-y-simulaciones-sencillas/CLASE.md).

### Iteración de punto fijo

- Una iteración de punto fijo actualiza `r` con el `h` de la posición anterior.
- La iteración de punto fijo lo resuelve: `m = g(m)` con `g(m) = (carga + resto + paneles(m) + batería(m))/(1 − f_estr)`.

💡 **Cómo se explica en la clase [B83-C20](../programa/clases/B83/B83-C20-diseno-preliminar-completo-de-mision/CLASE.md):**
- La iteración de punto fijo parte de 60 kg y converge en 10 pasos a 55,575 kg; la bisección sobre `f(m) = m − g(m)` da el mismo valor (diferencia 0,00 kg).
- 🎯 **Por qué importa:** Cada presupuesto aislado puede cerrar y el conjunto no. La decisión central: ¿existe una masa seca que sea coherente con la potencia, las baterías, la estructura y el propelente que ella misma exige, y cabe en el límite?

📘 **Dónde se aprende** (2 clases): [B53-C25 · Corrección geométrica y ortorrectificación de imágenes planetarias](../programa/clases/B53/B53-C25-correccion-geometrica-y-ortorrectificacion-de-imagenes-planetarias/CLASE.md); [B83-C20 · Diseño preliminar completo de misión](../programa/clases/B83/B83-C20-diseno-preliminar-completo-de-mision/CLASE.md).

### Iteraciones

- Las iteraciones son las del bucle del solucionador.

💡 **Cómo se explica en la clase [B82-C07](../programa/clases/B82/B82-C07-benchmark-entre-solucionadores-de-lambert/CLASE.md):**
- La variable `x` es más precisa (residuo máximo `10⁻¹²` frente a `10⁻¹⁰`) y requiere menos iteraciones que las variables universales.
- El orden entre los métodos con `x` y los universales es coherente con las iteraciones, pero el orden fino (Halley frente a Householder) no se interpreta.
- 🎯 **Por qué importa:** Elegir un solucionador sin medirlo es adivinar. La decisión central: ¿qué solucionador conviene para un banco de transferencias, y qué cifras sustentan esa elección?

📘 **Dónde se aprende** (1 clase): [B82-C07 · Benchmark entre solucionadores de Lambert](../programa/clases/B82/B82-C07-benchmark-entre-solucionadores-de-lambert/CLASE.md).

### ITRF

- Una realización del ITRS se llama ITRF (*International Terrestrial Reference Frame*): coordenadas y velocidades de estaciones que materializan el sistema (S1, §4.1.5).

🎯 **Por qué importa (clase B13-C11):** Una estación terrestre transmite a un satélite; el software de seguimiento necesita su posición en X, Y, Z. El técnico de campo tiene su posición en latitud, longitud y altura.

📘 **Dónde se aprende** (1 clase): [B13-C11 · Sistemas de referencia terrestres](../programa/clases/B13/B13-C11-sistemas-de-referencia-terrestres/CLASE.md).

### ITRS

- El GCRS (sistema celeste geocéntrico) y el ITRS (sistema terrestre internacional) son sistemas de referencia; el IERS los relaciona con `[GCRS] = Q(t) R(t) W(t) [ITRS]`, donde `Q` es el movimiento del polo celeste, `R` la rotación de la Tierra alrededor del eje del polo y `W` el movimiento polar (S1, ec. 5.1).

💡 **Cómo se explica en la clase [B10-C16](../programa/clases/B10/B10-C16-transformacion-de-marcos-de-referencia/CLASE.md):**
- A["ITRS<br/>(fijo a la Tierra)"] -->|"W: movimiento polar<br/>(omitido aquí)"| B["Marco intermedio"]
- 🎯 **Por qué importa:** Una estación terrestre tiene coordenadas fijas en la Tierra. Un satélite se propaga en un sistema inercial, donde las leyes de Newton valen.

📘 **Dónde se aprende** (1 clase): [B10-C16 · Transformación de marcos de referencia](../programa/clases/B10/B10-C16-transformacion-de-marcos-de-referencia/CLASE.md).
