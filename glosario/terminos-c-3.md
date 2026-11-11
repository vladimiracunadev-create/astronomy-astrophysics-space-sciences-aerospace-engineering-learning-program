# Términos · C (parte 3 de 3)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · **C** · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-c.md) · [2](terminos-c-2.md) · **3**

### Contenedor

- Una imagen es el paquete inmutable; un contenedor es una instancia en ejecución de una imagen.

💡 **Cómo se explica en la clase [B14-C17](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md):**
- Según S1, un contenedor es autocontenido y aislado, y comparte el núcleo del anfitrión.
- Un contenedor que lleva datos dentro oculta su procedencia.
- ⚠️ **Error frecuente:** Creer que el contenedor lo reproduce todo. Se corrige con los ejercicios 3 y 8.
- 🎯 **Por qué importa:** Tu análisis funciona con el bloqueo de C12 en tu equipo, pero en el servidor del laboratorio falla porque falta una biblioteca del sistema. La pregunta motivadora es: ¿cómo entrego el análisis junto con todo lo que necesita para correr, de modo que otra persona lo ejecute igual?

📘 **Dónde se aprende** (1 clase): [B14-C17 · Contenedores y ambientes científicos](../programa/clases/B14/B14-C17-contenedores-y-ambientes-cientificos/CLASE.md).

### Contenido

- El contenido del elipsoide `k²` es la probabilidad de que el error caiga dentro.

💡 **Cómo se explica en la clase [B74-C11](../programa/clases/B74/B74-C11-matrices-de-covarianza-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md):**
- En 3D el contenido de un elipsoide `1σ` es solo `0,1987`.
- Descripción larga: rotar no cambia la incertidumbre total; la correlación aplana el elipsoide; el contenido de un elipsoide de k sigma en 3D es mucho menor que el intervalo 1D.
- 🎯 **Por qué importa:** Los números de la diagonal engañan: dos errores muy correlacionados pueden ser individualmente grandes y conjuntamente pequeños. La decisión central: ¿qué dicen realmente los autovalores, las correlaciones y el elipsoide, y qué probabilidad encierra cada «k sigma» en tres dimensiones?

📘 **Dónde se aprende** (1 clase): [B74-C11 · Matrices de covarianza — Estimación de órbitas y navegación espacial](../programa/clases/B74/B74-C11-matrices-de-covarianza-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md).

### Contenido canónico

- El contenido canónico es una forma de escribir el registro con claves ordenadas y sin espacios, para que el hash sea reproducible.

💡 **Cómo se explica en la clase [B13-C19](../programa/clases/B13/B13-C19-metadatos-y-registros-de-calibracion/CLASE.md):**
- El contenido canónico (claves ordenadas, sin espacios) del registro, sin el campo `sha256`, se codifica en UTF-8 y se procesa con SHA-256; el resultado se guarda en el propio registro.
- R --> H["Hash SHA-256<br/>del contenido canónico"]
- 🎯 **Por qué importa:** Dentro de un año alguien usará los datos de un fotodiodo calibrado hoy. Necesitará saber con qué patrones, a qué temperatura, con qué incertidumbre y hasta cuándo es válida la calibración.

📘 **Dónde se aprende** (1 clase): [B13-C19 · Metadatos y registros de calibración](../programa/clases/B13/B13-C19-metadatos-y-registros-de-calibracion/CLASE.md).

### Contenido electrónico total

- El contenido electrónico total (TEC), en TECU (`1 TECU = 10¹⁶ m⁻²`).

🎯 **Por qué importa (clase B51-C05):** A frecuencias bajas la ionosfera domina el error de fase y de polarización. La decisión central: ¿cómo se mide y se quita el efecto con las propias frecuencias de la observación?

📘 **Dónde se aprende** (1 clase): [B51-C05 · Efectos ionosféricos en radioastronomía: retardo, rotación de Faraday y su corrección](../programa/clases/B51/B51-C05-efectos-ionosfericos-en-radioastronomia-retardo-rotacion-de-faraday-y-su-correccion/CLASE.md).

### Conteo

- El conteo `N ~ Poisson(sH + B)`.

🎯 **Por qué importa (clase B105-C07):** Un número de dosis sin su incertidumbre no es utilizable: cerca del fondo, el dosímetro no distingue una dosis pequeña de cero. La decisión central: ¿desde qué dosis se puede afirmar que el dosímetro vio algo y con qué incertidumbre se informa?

📘 **Dónde se aprende** (1 clase): [B105-C07 · Dosimetría personal](../programa/clases/B105/B105-C07-dosimetria-personal/CLASE.md).

### Conteo acumulado

- El conteo acumulado `N(>d)` es el número de objetos mayores que `d`.

🎯 **Por qué importa (clase B118-C01):** Los catálogos solo contienen los objetos que los sensores pueden seguir; el resto se conoce por modelos y por mediciones in situ. Esta clase fija el vocabulario cuantitativo (conteos acumulados, pendiente, densidad) que usan todas las demás.

📘 **Dónde se aprende** (1 clase): [B118-C01 · Población de objetos orbitales](../programa/clases/B118/B118-C01-poblacion-de-objetos-orbitales/CLASE.md).

### Conteo cíclico

- Un conteo cíclico cuenta una parte del inventario cada vez.

💡 **Cómo se explica en la clase [B100-C01](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md):**
- *Descripción textual:* los lotes entran al almacén; salen por emisión (que queda registrada) o por caducidad; el conteo cíclico compara el registro con lo físico.
- 🎯 **Por qué importa:** Un inventario que solo sabe «cuántas unidades hay» no puede decir de qué lote vienen, cuándo caducan ni dónde se usaron. La decisión central: ¿qué registro mínimo hace falta para emitir primero lo que caduca antes y para encontrar, si un lote resulta defectuoso, adónde fue?

📘 **Dónde se aprende** (1 clase): [B100-C01 · Gestión de inventario de materias primas y piezas](../programa/clases/B100/B100-C01-gestion-de-inventario-de-materias-primas-y-piezas/CLASE.md).

### Conteo de fotones

- El conteo de fotones registra eventos individuales en vez de energía.
- El conteo de fotones registra eventos individuales.

💡 **Cómo se explica en la clase [B92-C05](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md):**
- Como contexto publicado, el receptor de DSOC en Palomar es un receptor de conteo de fotones de nanohilos superconductores (NASA/JPL), sin más especificaciones en la página consultada.
- 🎯 **Por qué importa:** Un detector de imagen integra luz durante milisegundos; uno de comunicaciones decide, en nanosegundos, en qué ranura llegó el pulso. La decisión central: ¿cuántos fotones hacen falta por símbolo y qué detector soporta la tasa de ranuras sin saturarse?

📘 **Dónde se aprende** (2 clases): [B57-C11 · LiDAR satelital](../programa/clases/B57/B57-C11-lidar-satelital/CLASE.md); [B92-C05 · Receptores y detectores para comunicaciones ópticas](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md).

### Conteo de Poisson

- El conteo de Poisson tiene varianza igual a su media.

🎯 **Por qué importa (clase B67-C07):** Un sensor no mide «agua»: mide cuentas, y de ellas se infiere la abundancia con un modelo. La decisión central: ¿cuánto tiempo de medición y qué canales hacen falta para detectar y separar un volátil con la incertidumbre requerida?

📘 **Dónde se aprende** (1 clase): [B67-C07 · Sensores para volátiles: espectrometría de neutrones y de masas](../programa/clases/B67/B67-C07-sensores-para-volatiles-espectrometria-de-neutrones-y-de-masas/CLASE.md).

### Conteo independiente

- El conteo independiente es un recuento por un método distinto del que se verifica.
- Un conteo independiente usa otro método (C18).

💡 **Cómo se explica en la clase [B14-C18](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md):**
- Un conteo independiente, con arreglos de NumPy y sin pandas, da 1594: coincide.
- Comprueba con un conteo independiente: 1594.
- 🎯 **Por qué importa:** Un artículo usa «datos de un archivo público filtrados por paralaje y magnitud». Dos años después nadie puede repetir el filtro: el archivo se actualizó, los parámetros no se anotaron y la consulta no se guardó.

📘 **Dónde se aprende** (2 clases): [B14-C18 · Flujos de datos espaciales](../programa/clases/B14/B14-C18-flujos-de-datos-espaciales/CLASE.md); [B14-C25 · Catálogos de datos geoespaciales y metadatos (STAC)](../programa/clases/B14/B14-C25-catalogos-de-datos-geoespaciales-y-metadatos-stac/CLASE.md).

### Conteos esperados

- Los conteos esperados son `N [P(X>u_k) − P(X>u_{k+1})]`.

💡 **Cómo se explica en la clase [B33-C04](../programa/clases/B33/B33-C04-escalas-de-severidad-de-clima-espacial/CLASE.md):**
- *Descripción textual:* los umbrales definen niveles; la cola de potencias da conteos esperados que el Monte Carlo verifica.
- 🎯 **Por qué importa:** Comparar severidades exige conocer cómo se definió cada nivel. La decisión central: ¿cuántos eventos caen en cada nivel y por qué no son comparables entre escalas?

📘 **Dónde se aprende** (1 clase): [B33-C04 · Escalas de severidad de clima espacial](../programa/clases/B33/B33-C04-escalas-de-severidad-de-clima-espacial/CLASE.md).

### Conteos «off»

- Los conteos «off» `N_off` son los de una región de fondo.

🎯 **Por qué importa (clase B27-C19):** Decir «detectamos la fuente a 5σ» exige saber qué fórmula se usó y cuántos falsos positivos produce. La decisión central: ¿qué significancia tiene un par de conteos y qué señal mínima se necesita para una detección?

📘 **Dónde se aprende** (1 clase): [B27-C19 · Observatorios de rayos X y gamma](../programa/clases/B27/B27-C19-observatorios-de-rayos-x-y-gamma/CLASE.md).

### Conteos «on»

- Los conteos «on» `N_on` son los de la región de la fuente.

🎯 **Por qué importa (clase B27-C19):** Decir «detectamos la fuente a 5σ» exige saber qué fórmula se usó y cuántos falsos positivos produce. La decisión central: ¿qué significancia tiene un par de conteos y qué señal mínima se necesita para una detección?

📘 **Dónde se aprende** (1 clase): [B27-C19 · Observatorios de rayos X y gamma](../programa/clases/B27/B27-C19-observatorios-de-rayos-x-y-gamma/CLASE.md).

### Conteos oscuros

- Los conteos oscuros y el fondo son eventos sin señal.

🎯 **Por qué importa (clase B92-C05):** Un detector de imagen integra luz durante milisegundos; uno de comunicaciones decide, en nanosegundos, en qué ranura llegó el pulso. La decisión central: ¿cuántos fotones hacen falta por símbolo y qué detector soporta la tasa de ranuras sin saturarse?

📘 **Dónde se aprende** (1 clase): [B92-C05 · Receptores y detectores para comunicaciones ópticas](../programa/clases/B92/B92-C05-receptores-y-detectores-para-comunicaciones-opticas/CLASE.md).

### Contexto

- El contexto y el objeto y fin son fuentes que restringen la lectura.
- El contexto (`info`) distingue propósito y época.

💡 **Cómo se explica en la clase [B88-C38](../programa/clases/B88/B88-C38-gestion-de-claves-y-secretos-en-avionica/CLASE.md):**
- Se extrae con una sal y se expande con el contexto `propósito|época=n`.
- Paso 2 · Derivar. `expand(PRK, contexto, 32)`.
- 🎯 **Por qué importa:** Una clave filtrada o reutilizada anula toda la autenticación. La decisión central: ¿cómo se separan las claves por función y época para que el compromiso de una no arrastre a las demás?

📘 **Dónde se aprende** (2 clases): [B88-C38 · Gestión de claves y secretos en aviónica](../programa/clases/B88/B88-C38-gestion-de-claves-y-secretos-en-avionica/CLASE.md); [B119-C32 · Interpretación de tratados internacionales](../programa/clases/B119/B119-C32-interpretacion-de-tratados-internacionales/CLASE.md).

### Contexto ritual y social

- El contexto ritual y social es el conjunto de prácticas, calendarios, jerarquías y creencias en que se inscribe una observación del cielo.

🎯 **Por qué importa (clase B132-C05):** El catálogo trata alineaciones sin ese contexto. La decisión central: ¿cuánto apoyo da cada línea de evidencia a la intención de una alineación, y qué parte de la conclusión depende de lo que se supone de antemano?

📘 **Dónde se aprende** (1 clase): [B132-C05 · Contexto ritual y social de la observación del cielo](../programa/clases/B132/B132-C05-contexto-ritual-y-social-de-la-observacion-del-cielo/CLASE.md).

### Contingencia

- DITL: prueba de «día en la vida». Contingencia: tiempo reservado para fallas.

💡 **Cómo se explica en la clase [B90-C20](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md):**
- Para una confianza de 90 % hay que reservar `25 − 15 = 10 d` de contingencia sobre los 15 d sin fallas.
- Por calendario: duración y contingencia (esta clase).
- ⚠️ **Error frecuente:** Planificar con la duración sin fallas. Reserva contingencia (8.4)
- 🎯 **Por qué importa:** Un calendario de ensayos sin contingencia casi nunca se cumple: cada falla suma retrabajo y repetición. La decisión central: ¿cuánto tiempo reservar para terminar con una confianza dada?

📘 **Dónde se aprende** (1 clase): [B90-C20 · Campaña conceptual de calificación de CubeSat](../programa/clases/B90/B90-C20-campana-conceptual-de-calificacion-de-cubesat/CLASE.md).

### Continua

- Es discreta si toma valores aislados y continua si toma cualquier valor de un intervalo (S1, C.2.2, nota 1).

💡 **Cómo se explica en la clase [B12-C02](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md):**
- Su límite: en una variable continua no hay pilas contables; la «pila» de un valor exacto pesa cero y sólo pesan los intervalos.
- Paso 1 · Variables. `X` discreta (pmf de 8.1), `Y` continua (8.3); se supone que `X` e `Y` son independientes (el telémetro no depende de los computadores en este modelo).
- 🎯 **Por qué importa:** Casi nunca interesa *qué* resultado ocurrió, sino *un número* que resume el resultado: cuántos computadores funcionan, qué error tuvo una medición, cuántos fotones llegaron. Poner un número en cada resultado permite sumar, promediar y comparar.

📘 **Dónde se aprende** (1 clase): [B12-C02 · Variables aleatorias](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md).

### Continua en a

- Una función `f` es continua en `a` si existen `f(a)` y `lim_{x→a} f(x)` y son iguales (S1, §1.4(ii)).

🎯 **Por qué importa (clase B09-C02):** Un vehículo espacial cambia de masa de dos maneras: gradualmente, al quemar propelente, y de golpe, al soltar una etapa vacía. Un modelo de trayectoria que ignore los saltos integra mal; uno que los trate como suaves, también.

📘 **Dónde se aprende** (1 clase): [B09-C02 · Continuidad y discontinuidad](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md).

### Continua por tramos

- Una función es continua por tramos si lo es salvo en un número finito de saltos.

🎯 **Por qué importa (clase B09-C02):** Un vehículo espacial cambia de masa de dos maneras: gradualmente, al quemar propelente, y de golpe, al soltar una etapa vacía. Un modelo de trayectoria que ignore los saltos integra mal; uno que los trate como suaves, también.

📘 **Dónde se aprende** (1 clase): [B09-C02 · Continuidad y discontinuidad](../programa/clases/B09/B09-C02-continuidad-y-discontinuidad/CLASE.md).

### Continuación

- La continuación sigue la familia en `A`.

💡 **Cómo se explica en la clase [B76-C06](../programa/clases/B76/B76-C06-orbitas-dro-dinamica-cislunar-y-operaciones-de-proximidad/CLASE.md):**
- Una búsqueda directa a `70.000 km` puede caer en otra solución; la continuación evita ese riesgo.
- ⚠️ **Error frecuente:** Buscar la DRO sin continuación. Se corrige con 8.2.
- 🎯 **Por qué importa:** La NRHO es inestable y exige mantenimiento; la DRO es estable. La decisión central: ¿qué se gana y qué se paga al elegir una órbita estable y lejana frente a una NRHO cercana?

📘 **Dónde se aprende** (1 clase): [B76-C06 · Órbitas DRO — Dinámica cislunar y operaciones de proximidad](../programa/clases/B76/B76-C06-orbitas-dro-dinamica-cislunar-y-operaciones-de-proximidad/CLASE.md).

### Continuidad

- La continuidad estacionaria dice que `ṁ` es el mismo en todas las secciones.
- La continuidad exige que `P` y `e` coincidan en la unión.

💡 **Cómo se explica en la clase [B27-C04](../programa/clases/B27/B27-C04-ecuacion-de-estado-nuclear/CLASE.md):**
- Para `ρ < ρ_t`, `P = K₁ρ^{Γ₁}`; para `ρ ≥ ρ_t`, `P = K₂ρ^{Γ₂}` con `K₂ = K₁ρ_t^{Γ₁−Γ₂}` (continuidad de `P`).
- 🎯 **Por qué importa:** Las estrellas de neutrones son el único laboratorio de materia más allá de la densidad nuclear. Su EOS no se conoce con precisión; las medidas de masa máxima y de radio la acotan.

📘 **Dónde se aprende** (2 clases): [B27-C04 · Ecuación de estado nuclear](../programa/clases/B27/B27-C04-ecuacion-de-estado-nuclear/CLASE.md); [B79-C01 · Conservación de masa en fluidos](../programa/clases/B79/B79-C01-conservacion-de-masa-en-fluidos/CLASE.md).

### Continuo

- Un modelo es lineal si cumple superposición (lo precisa C03), invariante si sus parámetros no cambian con el tiempo, continuo si el tiempo es una variable real `t` y discreto si solo existe en instantes `kT`.
- El continuo es la opacidad de fondo.
- El continuo es la línea base sin la banda.

💡 **Cómo se explica en la clase [B16-C01](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md):**
- El modelo de la sección 8.2 es lineal (el estado aparece solo multiplicado por constantes), invariante (`J` no cambia), continuo y de orden 2.
- Un modelo continuo describe el fenómeno; uno discreto describe lo que ve el computador de a bordo, que mide y actúa cada `T` segundos (C02).
- 🎯 **Por qué importa:** Un telescopio espacial tiene que apuntar a una estrella y mantenerse allí. El telescopio Hubble lo hace con una desviación de no más de 0,007 segundos de arco durante al menos 24 horas (fuente S2).

📘 **Dónde se aprende** (4 clases): [B16-C01 · Modelos dinámicos y estados](../programa/clases/B16/B16-C01-modelos-dinamicos-y-estados/CLASE.md); [B29-C12 · Espectroscopía de transmisión](../programa/clases/B29/B29-C12-espectroscopia-de-transmision/CLASE.md); [B32-C10 · Normalización y modelado del continuo espectral](../programa/clases/B32/B32-C10-normalizacion-y-modelado-del-continuo-espectral/CLASE.md); [B53-C17 · Mineralogía espectral](../programa/clases/B53/B53-C17-mineralogia-espectral/CLASE.md).

### Contracción

- La contracción (*shrinkage*) acerca cada `y_j` a la media del conjunto con peso `B_j = σ_j²/(σ_j² + τ²)`: la media posterior condicionada a `τ` es `(1 − B_j) y_j + B_j μ̂`.
- La contracción de un par de índices los iguala y suma: `Tᵢᵢ` (traza), `Tᵢⱼ bⱼ` (producto por un vector), `aᵢ bᵢ` (producto escalar).

💡 **Cómo se explica en la clase [B10-C18](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md):**
- La contracción de sus dos índices da `4 + 10 + 18 = 32 = a · b`, y la contracción de un índice con `b` da `(a ⊗ b) b = a (b · b)`.
- Paso 3 · Contracción. `δa = T δx = (2,3242 × 10⁻⁵; 0; 0) m/s²`.
- 🎯 **Por qué importa:** La gravedad no es uniforme a lo largo de un satélite: lo que está más cerca de la Tierra se acelera más que lo que está lejos, y lo que está a los lados se comprime. Con una sola derivada `dg/dr` solo describes la dirección radial; el tensor de marea describe las tres direcciones a la vez.

📘 **Dónde se aprende** (2 clases): [B10-C18 · Producto tensorial y contracción](../programa/clases/B10/B10-C18-producto-tensorial-y-contraccion/CLASE.md); [B12-C21 · Modelos jerárquicos bayesianos](../programa/clases/B12/B12-C21-modelos-jerarquicos-bayesianos/CLASE.md).

### Contracción de longitudes

- La contracción de longitudes dice que, en un marco donde el objeto se mueve, su longitud a lo largo del movimiento es `L = L₀/γ`.

🎯 **Por qué importa (clase B26-C03):** Los muones se producen en la alta atmósfera por rayos cósmicos, viven microsegundos y, sin embargo, llegan al suelo en cantidad. Los relojes de satélites de navegación se ajustan por el mismo efecto.

📘 **Dónde se aprende** (1 clase): [B26-C03 · Dilatación temporal y contracción](../programa/clases/B26/B26-C03-dilatacion-temporal-y-contraccion/CLASE.md).

### Contracción global

- La contracción global reduce el radio `ΔR/R = ε/2`, con `ε` la deformación areal.

🎯 **Por qué importa (clase B53-C12):** La flexión revela el espesor elástico de la litosfera y la contracción, el balance térmico global. La decisión central: ¿qué espesor elástico y qué acortamiento explican la deformación observada?

📘 **Dónde se aprende** (1 clase): [B53-C12 · Tectónica planetaria](../programa/clases/B53/B53-C12-tectonica-planetaria/CLASE.md).

### Contrachorro

- El contrachorro es el que se aleja.

💡 **Cómo se explica en la clase [B27-C11](../programa/clases/B27/B27-C11-chorros-relativistas/CLASE.md):**
- Por cociente chorro/contrachorro: observacional.
- ⚠️ **Error frecuente:** Olvidar el contrachorro. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un chorro que se acerca puede parecer más rápido que la luz sin violar nada, y su brillo cambia en órdenes de magnitud según el ángulo. Sin estos efectos no se pueden comparar chorros ni inferir su velocidad.

📘 **Dónde se aprende** (1 clase): [B27-C11 · Chorros relativistas](../programa/clases/B27/B27-C11-chorros-relativistas/CLASE.md).

### Contracorriente

- El esquema contracorriente (*upwind*) para `u_t + c u_x = 0` con `c > 0` usa el nodo de aguas arriba: `u_i^{n+1} = u_i^n − ν (u_i^n − u_{i−1}^n)`.

💡 **Cómo se explica en la clase [B11-C14](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md):**
- Para `u_t + c u_x = 0`, el esquema contracorriente es estable si `ν = c Δt/Δx ≤ 1`: la información no puede cruzar más de una celda por paso.
- Contracorriente: para advección, orden 1, estable con `ν ≤ 1` y que difunde el pulso (suaviza la forma).
- 🎯 **Por qué importa:** Casi todo código de simulación de calor, fluidos o plasma en una malla regular usa diferencias finitas. Elegir el paso de tiempo equivocado no da un resultado ligeramente malo: da un resultado que explota.

📘 **Dónde se aprende** (1 clase): [B11-C14 · Diferencias finitas](../programa/clases/B11/B11-C14-diferencias-finitas/CLASE.md).

### Contraejemplo

- Un contraejemplo es un caso concreto que hace falsa una afirmación.

💡 **Cómo se explica en la clase [B10-C01](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md):**
- Contraejemplo. `W = {(x, y, 1)}`, el plano `z = 1`: `(0, 0, 0)` no está, y `(1, 0, 1) + (0, 1, 1) = (1, 1, 2)` no está.
- Contraejemplo numérico: basta uno para refutar.
- 🎯 **Por qué importa:** El estado de un satélite en un instante se describe con seis números: tres de posición y tres de velocidad. Los programas de navegación suman, restan y multiplican por escalares esos «vectores de estado» todo el tiempo: promedian estimaciones, corrigen con un error medido, propagan pequeñas perturbaciones.

📘 **Dónde se aprende** (1 clase): [B10-C01 · Espacios vectoriales](../programa/clases/B10/B10-C01-espacios-vectoriales/CLASE.md).

### Contraluz

- El contraluz es una fase mayor que `120°` (hipótesis).

💡 **Cómo se explica en la clase [B76-C18](../programa/clases/B76/B76-C18-restricciones-de-iluminacion/CLASE.md):**
- Con `β = 0` solo el `30,5 %` de la órbita está al sol con buena fase; con `β` alto hay más sol pero el contraluz deja de ser el límite y la fase se limita por `β`.
- 🎯 **Por qué importa:** Una aproximación planificada de noche, o con el Sol detrás del objetivo, puede dejar ciego al sensor. La decisión central: ¿qué fracción de la órbita está al sol y con buena fase, según el ángulo `β`?

📘 **Dónde se aprende** (1 clase): [B76-C18 · Restricciones de iluminación](../programa/clases/B76/B76-C18-restricciones-de-iluminacion/CLASE.md).

### Contramedida

- La contramedida es una intervención que reduce la pérdida (aquí, `δ/2`, ilustrativa).
- La contramedida es una medida para prevenir o mitigar un riesgo.

💡 **Cómo se explica en la clase [B105-C03](../programa/clases/B105/B105-C03-atrofia-muscular/CLASE.md):**
- La contramedida es una suposición del modelo, no una prescripción.
- Con la mitad de `δ` (contramedida simulada) la fuerza a 180 días es 1.335,9 N.
- ⚠️ **Error frecuente:** Tomar la contramedida simulada como recomendación. Es una hipótesis del modelo (8.3).
- 🎯 **Por qué importa:** Sin carga y sin aporte adecuado, el músculo se pierde más rápido que en la Tierra. La decisión central: ¿cuánta área y cuánta fuerza quedan tras 30, 90 y 180 días, y cuánto cambia una contramedida?

📘 **Dónde se aprende** (2 clases): [B105-C03 · Atrofia muscular](../programa/clases/B105/B105-C03-atrofia-muscular/CLASE.md); [B113-C05 · Intervenciones de apoyo y contramedidas conductuales](../programa/clases/B113/B113-C05-intervenciones-de-apoyo-y-contramedidas-conductuales/CLASE.md).

### Contrapeso

- El contrapeso `m_c r_c = m_t r_t`.

💡 **Cómo se explica en la clase [B43-C19](../programa/clases/B43/B43-C19-seguridad-y-mantenimiento/CLASE.md):**
- Un tubo de 7 kg con el centro a 0,20 m y un contrapeso de 4 kg a 0,35 m dejan un desbalance de `2,2 × 10⁻¹⁶ kg m`; el contrapeso necesario es `4,000 kg`.
- 🎯 **Por qué importa:** La seguridad empieza por saber cuán grande es el riesgo. La decisión central: ¿cuánta potencia y qué temperatura aparecen en el foco, cómo se balancea la montura y cuánto polvo es aceptable?

📘 **Dónde se aprende** (1 clase): [B43-C19 · Seguridad y mantenimiento](../programa/clases/B43/B43-C19-seguridad-y-mantenimiento/CLASE.md).

### Contraste

- El contraste `c = (T_m/T_ef)⁴` es el cociente entre el flujo por unidad de área de la mancha y el del entorno.
- El contraste es el cociente de flujos planeta/estrella.
- El contraste WCAG es `(L₁ + 0,05)/(L₂ + 0,05)` con `L` la luminancia relativa.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B24-C12](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md):**
- A["Mancha: radio ρ,<br/>contraste c"] --> B["Área proyectada<br/>A cos γ(t)"]
- 🎯 **Por qué importa:** La modulación del brillo por manchas permite medir el periodo de rotación de miles de estrellas sin necesitar espectros, pero también contamina la búsqueda de exoplanetas y limita la precisión de las velocidades radiales.

📘 **Dónde se aprende** (8 clases): [B24-C12 · Manchas y actividad estelar](../programa/clases/B24/B24-C12-manchas-y-actividad-estelar/CLASE.md); [B29-C06 · Imagen directa de exoplanetas](../programa/clases/B29/B29-C06-imagen-directa-de-exoplanetas/CLASE.md); [B30-C04 · Manchas solares](../programa/clases/B30/B30-C04-manchas-solares/CLASE.md); [B42-C24 · Métricas de desempeño de óptica adaptativa: Strehl y energía encerrada](../programa/clases/B42/B42-C24-metricas-de-desempeno-de-optica-adaptativa-strehl-y-energia-encerrada/CLASE.md); [B47-C07 · Coronógrafos espaciales](../programa/clases/B47/B47-C07-coronografos-espaciales/CLASE.md); [B53-C26 · Publicación de mapas geológicos planetarios: estándares y leyendas](../programa/clases/B53/B53-C26-publicacion-de-mapas-geologicos-planetarios-estandares-y-leyendas/CLASE.md) y 2 más.

### Contribución

- La contribución de `xᵢ` a la varianza combinada es `(cᵢ u(xᵢ))²` (S1, 5.1.2–5.1.3).
- Una contribución es el término `|c_i| u(x_i)`, en unidades del mensurando.
- La contribución de cada dimensión es `tᵢ²/Σt²`.

💡 **Cómo se explica en la clase [B12-C17](../programa/clases/B12/B12-C17-analisis-de-sensibilidad/CLASE.md):**
- B --> D["Contribución (cᵢ uᵢ)²<br/>y fracción de varianza"]
- 🎯 **Por qué importa:** Mejorar una medida cuesta dinero, masa o tiempo. Si el presupuesto de una misión ofrece mejorar la masa seca o el empuje específico, hay que saber cuál de las dos reduce más la incertidumbre del resultado.

📘 **Dónde se aprende** (3 clases): [B12-C17 · Análisis de sensibilidad](../programa/clases/B12/B12-C17-analisis-de-sensibilidad/CLASE.md); [B13-C13 · Presupuestos de incertidumbre](../programa/clases/B13/B13-C13-presupuestos-de-incertidumbre/CLASE.md); [B84-C16 · Tolerancias de fabricación](../programa/clases/B84/B84-C16-tolerancias-de-fabricacion/CLASE.md).

### Contribución a la varianza

- La contribución a la varianza de un factor es su `σ²` entre la suma de las `σ²` en la escala logarítmica.
- La contribución a la varianza de cada parámetro.

🎯 **Por qué importa (clase B33-C02):** Un pronóstico de llegada sin incertidumbre es engañoso. La decisión central: ¿qué parámetro domina la incertidumbre del tiempo de llegada?

📘 **Dónde se aprende** (2 clases): [B33-C02 · Modelos de propagación de CME](../programa/clases/B33/B33-C02-modelos-de-propagacion-de-cme/CLASE.md); [B67-C08 · Informe de disponibilidad de volátiles con incertidumbre](../programa/clases/B67/B67-C08-informe-de-disponibilidad-de-volatiles-con-incertidumbre/CLASE.md).

### Contribuyente

- Un contribuyente es una fuente de error con su `σ` (1σ).

💡 **Cómo se explica en la clase [B87-C22](../programa/clases/B87/B87-C22-presupuesto-de-error-de-apuntamiento/CLASE.md):**
- Sin el mayor contribuyente (el alineamiento), el RSS bajaría a `6,12″`: el alineamiento aporta el 40 % de la varianza y es donde conviene invertir.
- *Descripción textual:* cada contribuyente se describe por su desviación; la suma cuadrática da el error total, el Monte Carlo la confirma y la comparación con el requisito da el margen; con dos ejes aparece el error radial.
- 🎯 **Por qué importa:** Un requisito de apuntamiento solo se cumple si el diseño lo respalda con números. La decisión central: ¿qué contribuyentes dominan, cómo se combinan (suma lineal o cuadrática), con qué margen se cumple el requisito y qué ocurre con dos ejes?

📘 **Dónde se aprende** (1 clase): [B87-C22 · Presupuesto de error de apuntamiento](../programa/clases/B87/B87-C22-presupuesto-de-error-de-apuntamiento/CLASE.md).

### Control

- Un control es una medida defensiva.
- Un control reduce la probabilidad de una hoja.

💡 **Cómo se explica en la clase [B119-C14](../programa/clases/B119/B119-C14-amenazas-ciberneticas-a-satelites/CLASE.md):**
- Cada control reduce a la mitad una hoja.
- 🎯 **Por qué importa:** La amenaza cibernética conecta el derecho con la seguridad operativa; el modelo defensivo de infraestructura espacial (B122-C03) lo desarrolla, y esta clase fija el razonamiento de riesgo. La decisión central: ¿qué control reduce más el riesgo residual y cuánto se gana al combinarlos?

📘 **Dónde se aprende** (2 clases): [B119-C14 · Amenazas cibernéticas a satélites](../programa/clases/B119/B119-C14-amenazas-ciberneticas-a-satelites/CLASE.md); [B122-C03 · Modelo defensivo de riesgos de infraestructura espacial](../programa/clases/B122/B122-C03-modelo-defensivo-de-riesgos-de-infraestructura-espacial/CLASE.md).

### Control de actitud fija

- El control de actitud fija mantiene `θ = 0`; la carga ante racha es `q·α`.

🎯 **Por qué importa (clase B77-C23):** Un vehículo inestable es controlable si el control es más rápido que la divergencia, pero el control a su vez fija las cargas ante rachas. La decisión central: ¿cuánto control hace falta para estabilizar un lanzador y qué ángulo de ataque deja una racha según la ganancia?

📘 **Dónde se aprende** (1 clase): [B77-C23 · Estabilidad de vuelo de lanzadores en ascenso](../programa/clases/B77/B77-C23-estabilidad-de-vuelo-de-lanzadores-en-ascenso/CLASE.md).

### Control de calidad

- El control de calidad (QC) acepta o rechaza el lote con criterios declarados.

💡 **Cómo se explica en la clase [B14-C30](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md):**
- Cada etapa recibe un dato con su huella, calcula la clave del resultado, y si ya existe lo reutiliza; si no, lo calcula, y si falla lo reintenta; si el control de calidad lo rechaza, detiene el lote.
- I["Ingestar"] --> V["Validar<br/>control de calidad"]
- ⚠️ **Error frecuente:** Dejar pasar un lote sin control de calidad. Se corrige con la sección 8.3 y el ejercicio 7.
- 🎯 **Por qué importa:** Cada madrugada llegan datos nuevos. Si un humano debe lanzar cada paso, tarde o temprano se olvida uno; si un lote corrupto atraviesa la cadena, contamina el producto final; si un fallo de red detiene todo y al reiniciar se repite desde cero, se pierde tiempo.

📘 **Dónde se aprende** (1 clase): [B14-C30 · Cadenas de procesamiento automatizado de datos](../programa/clases/B14/B14-C30-cadenas-de-procesamiento-automatizado-de-datos/CLASE.md).

### Control PD

- El control PD usa el error y su derivada: `δ = Kp(θ_c − θ) − Kd θ̇`.

🎯 **Por qué importa (clase B77-C24):** El control de un lanzador inestable debe ser lo bastante rápido para estabilizarlo y lo bastante suave para no saturar la tobera. La decisión central: ¿qué ganancias cumplen una especificación dada y qué ocurre cuando la demanda supera los límites del actuador?

📘 **Dónde se aprende** (1 clase): [B77-C24 · Guiado y control de actitud de lanzadores (TVC)](../programa/clases/B77/B77-C24-guiado-y-control-de-actitud-de-lanzadores-tvc/CLASE.md).

### Control supervisado

- En control supervisado el operador da una meta de mayor alcance y el vehículo la ejecuta con autonomía.

💡 **Cómo se explica en la clase [B98-C03](../programa/clases/B98/B98-C03-control-supervisado-y-autonomia-compartida/CLASE.md):**
- Sin retardo, «mover y esperar» (pasos de 1 m, `v = 0,04 m/s`, 30 s de decisión por orden) tarda 1,53 h y el control supervisado (metas de 10 m, `v = 0,02 m/s`, 120 s por meta) 1,72 h: gana el manual.
- 🎯 **Por qué importa:** Ni siempre conviene más autonomía ni siempre más control manual: sin retardo, el manual puede ser más rápido. La decisión central: ¿a partir de qué retardo compensa pasar de órdenes cortas a metas supervisadas, y qué se pierde al hacerlo?

📘 **Dónde se aprende** (1 clase): [B98-C03 · Control supervisado y autonomía compartida](../programa/clases/B98/B98-C03-control-supervisado-y-autonomia-compartida/CLASE.md).

### Controlable

- El sistema `ẋ = A x + B u` (con `n` estados) es controlable si, desde cualquier estado inicial, existe una entrada que lo lleva a cualquier otro estado en un tiempo finito.

💡 **Cómo se explica en la clase [B16-C13](../programa/clases/B16/B16-C13-observabilidad-y-controlabilidad/CLASE.md):**
- Con `A = [[0,1],[0,0]]`, `B = [0, 1/J]ᵀ`: `AB = [1/J, 0]ᵀ`, luego `𝒞 = [[0, 1/J],[1/J, 0]]` de rango 2: controlable.
- El sistema no lineal real, con momento almacenado, puede ser controlable de otras maneras (por ejemplo, usando el acoplamiento giroscópico); la prueba lineal no lo afirma ni lo descarta.
- ⚠️ **Error frecuente:** Confundir «controlable» con «barato». Se corrige con los ejercicios 5 y 11.
- 🎯 **Por qué importa:** Un satélite puede perder actuadores o sensores en vuelo. Antes de diseñar una ley de control conviene saber si el problema tiene solución: ninguna ley, por ingeniosa que sea, mueve un estado que ningún actuador alcanza, ni estima uno que ningún sensor ve.

📘 **Dónde se aprende** (1 clase): [B16-C13 · Observabilidad y controlabilidad](../programa/clases/B16/B16-C13-observabilidad-y-controlabilidad/CLASE.md).

### Controlador

- Un controlador implementa la HAL para un dispositivo.
- Balance ambiental: suma de generaciones, retiros y acumulación de cada magnitud. Controlador: lazo que enciende o apaga un equipo.

💡 **Cómo se explica en la clase [B88-C24](../programa/clases/B88/B88-C24-capa-de-abstraccion-de-hardware-hal-y-controladores/CLASE.md):**
- HAL --> R["Controlador de registros (FIFO 4)"]
- 🎯 **Por qué importa:** Si la aplicación toca registros, no se puede probar sin el hardware y cada cambio de componente la rompe. La decisión central: ¿qué interfaz mínima expone el dispositivo para que la aplicación no dependa de él?

📘 **Dónde se aprende** (2 clases): [B88-C24 · Capa de abstracción de hardware (HAL) y controladores](../programa/clases/B88/B88-C24-capa-de-abstraccion-de-hardware-hal-y-controladores/CLASE.md); [B106-C20 · Proyecto de balance ambiental de hábitat](../programa/clases/B106/B106-C20-proyecto-de-balance-ambiental-de-habitat/CLASE.md).

### Controlador PD

- El controlador PD `τ = K_p e − K_d θ'`.

🎯 **Por qué importa (clase B43-C15):** El motor fija la resolución, la fuerza útil y la estabilidad del lazo. La decisión central: ¿cuánto se desvía un motor paso a paso bajo carga y qué ganancias dan una respuesta de servo sin sobreimpulso excesivo?

📘 **Dónde se aprende** (1 clase): [B43-C15 · Motores paso a paso y servomotores](../programa/clases/B43/B43-C15-motores-paso-a-paso-y-servomotores/CLASE.md).

### Convección

- La convección es el transporte por movimiento macroscópico del gas.

💡 **Cómo se explica en la clase [B24-C05](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md):**
- Si `∇_rad > ∇_ad`, una burbuja desplazada hacia arriba sigue siendo más caliente que su entorno, sigue subiendo y aparece convección.
- Una opacidad alta (capas externas frías) o una luminosidad alta por unidad de masa (núcleos de estrellas masivas) empujan a la convección.
- 🎯 **Por qué importa:** La energía generada en el núcleo tarda milenios en salir y el modo de transporte decide la estructura: si el interior de una estrella es convectivo, su composición se mezcla; si es radiativo, no. De ello depende cuánto combustible alcanza el núcleo, y por tanto la vida de la estrella.

📘 **Dónde se aprende** (1 clase): [B24-C05 · Transporte radiativo y convectivo](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md).

### Convección natural

- La convección natural se apaga si `Ra` es menor que el valor crítico, aquí `1708`.
- La convección natural depende de la flotabilidad; en microgravedad `h_c ≈ 0` sin ventilación.

💡 **Cómo se explica en la clase [B85-C03](../programa/clases/B85/B85-C03-conveccion-y-ausencia-de-conveccion-exterior/CLASE.md):**
- Descripción larga: la convección natural a 1 atm equivale a la radiación; con la presión a la décima parte, `Ra` cae cien veces, y con microgravedad desaparece aunque haya aire.
- 🎯 **Por qué importa:** Un equipo que se enfría bien sobre la mesa puede sobrecalentarse en vacío y en microgravedad. La decisión central: ¿cuánto del enfriamiento de un equipo se pierde al quitar la convección y qué queda para sustituirla?

📘 **Dónde se aprende** (2 clases): [B85-C03 · Convección y ausencia de convección exterior](../programa/clases/B85/B85-C03-conveccion-y-ausencia-de-conveccion-exterior/CLASE.md); [B105-C23 · Termorregulación humana en vuelo](../programa/clases/B105/B105-C23-termorregulacion-humana-en-vuelo/CLASE.md).

### Convención

- Una convención es un acuerdo que no se deduce de la naturaleza: el umbral de 20 000 km lo es.

🎯 **Por qué importa (clase B07-C04):** Toda clasificación astronómica es una decisión sobre un dato: ¿esta señal supera el ruido?, ¿esta estrella es más brillante que el umbral?, ¿esta imagen está saturada? Una decisión mal escrita no falla ruidosamente: clasifica mal en silencio, justo en los casos frontera, que son los que importan.

📘 **Dónde se aprende** (1 clase): [B07-C04 · Condicionales y decisiones](../programa/clases/B07/B07-C04-condicionales-y-decisiones/CLASE.md).

### Convención de signo

- Una convención de signo es el acuerdo sobre qué sentido es positivo.

🎯 **Por qué importa (clase B03-C09):** Cuando observas una llamarada solar a las 12:00:00, el evento ocurrió antes: su tiempo es el observado menos 499 s. Si sumas en vez de restar, afirmas que la llamarada ocurre en el futuro.

📘 **Dónde se aprende** (1 clase): [B03-C09 · Operaciones con números negativos](../programa/clases/B03/B03-C09-operaciones-con-numeros-negativos/CLASE.md).

### Convención de suma de Einstein

- La convención de suma de Einstein dice que un índice repetido en un término se suma de 1 a 3: `aᵢ bᵢ = Σ aᵢ bᵢ`.

🎯 **Por qué importa (clase B10-C17):** La inercia de un satélite frente a un giro depende de la dirección: se necesita nueve números ordenados en una matriz, y esos nueve números cambian si cambias los ejes del cuerpo, pero de forma que la física no cambie.

📘 **Dónde se aprende** (1 clase): [B10-C17 · Tensores y notación indicial](../programa/clases/B10/B10-C17-tensores-y-notacion-indicial/CLASE.md).

### Convenio de signos

- El convenio de signos aquí es el de `U` positivo, con `J_n` positivo para un achatamiento ecuatorial.

💡 **Cómo se explica en la clase [B72-C02](../programa/clases/B72/B72-C02-potencial-gravitatorio-no-esferico/CLASE.md):**
- ⚠️ **Error frecuente:** Mezclar el convenio de signos del potencial. Se corrige con la sección 10: aquí `U` es positivo.
- 🎯 **Por qué importa:** Sin un potencial no hay perturbación gravitatoria que calcular, y los números de la bibliografía (J2, J3, J4) dependen de un convenio de signos y de un radio de referencia. La decisión central: ¿qué términos del potencial incluir y con qué radio y convenio, para que J2 signifique lo mismo en tu código y en la fuente?

📘 **Dónde se aprende** (1 clase): [B72-C02 · Potencial gravitatorio no esférico](../programa/clases/B72/B72-C02-potencial-gravitatorio-no-esferico/CLASE.md).

### Convergencia

- La convergencia de un integrador es la reducción del error al disminuir el paso; su orden `p` cumple `error ∝ h^p`.
- Un calentamiento (*warm-up*) son las primeras iteraciones, que se descartan. Convergencia significa que las cadenas muestrean la misma distribución estacionaria, la posterior; no es una propiedad que se demuestre, solo que se detecta su ausencia.
- La convergencia es la reducción del error al refinar la malla.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B16-C19](../programa/clases/B16/B16-C19-verificacion-de-lazo-cerrado/CLASE.md):**
- (c) el orden de convergencia: el error a `t = 20 s` es 4,1×10⁻⁹ con `h = 0,4`, 1,4×10⁻¹⁰ con 0,2 y 5,3×10⁻¹² con 0,1; los órdenes son 4,89 y 4,71, es decir, al menos 4, como corresponde a RK4.
- 🎯 **Por qué importa:** Un lazo que «se ve bien» en una simulación puede estar mal por tres razones: el diseño no cumple un requisito en parte del rango de parámetros, la discretización en el computador de vuelo cambia el comportamiento, o el simulador tiene un error numérico.

📘 **Dónde se aprende** (5 clases): [B16-C19 · Verificación de lazo cerrado](../programa/clases/B16/B16-C19-verificacion-de-lazo-cerrado/CLASE.md); [B19-C04 · Diagnóstico de convergencia de cadenas](../programa/clases/B19/B19-C04-diagnostico-de-convergencia-de-cadenas/CLASE.md); [B39-C06 · Introducción a la relatividad numérica: formalismo 3+1](../programa/clases/B39/B39-C06-introduccion-a-la-relatividad-numerica-formalismo-3-1/CLASE.md); [B73-C20 · Proyecto de integración celeste de precisión](../programa/clases/B73/B73-C20-proyecto-de-integracion-celeste-de-precision/CLASE.md); [B116-C03 · Historia clínica remota y registros médicos de misión](../programa/clases/B116/B116-C03-historia-clinica-remota-y-registros-medicos-de-mision/CLASE.md).

### Convergencia en el paso

- La convergencia en el paso es la estabilización del resultado al reducir `Δt`.

🎯 **Por qué importa (clase B77-C20):** Una simulación solo vale si se sabe cuánto error numérico tiene y a dónde va cada metro por segundo. La decisión central: ¿cómo se verifica que una simulación de vuelo es numéricamente fiable y cómo se lee su presupuesto de pérdidas?

📘 **Dónde se aprende** (1 clase): [B77-C20 · Simulación académica de una trayectoria de vuelo](../programa/clases/B77/B77-C20-simulacion-academica-de-una-trayectoria-de-vuelo/CLASE.md).

### Convergencia espectral

- La convergencia espectral (o exponencial) es un error que decae como `e^{−c N}`.

🎯 **Por qué importa (clase B11-C16):** Cuando la solución es suave y periódica —una señal a lo largo de una órbita, un perfil de temperatura alrededor de un vehículo que gira, el campo en una caja periódica—, un método espectral logra con 24 puntos lo que unas diferencias finitas lograrían con millones.

📘 **Dónde se aprende** (1 clase): [B11-C16 · Métodos espectrales iniciales](../programa/clases/B11/B11-C16-metodos-espectrales-iniciales/CLASE.md).

### Convergencia exponencial

- La convergencia exponencial es un error `~ e^{−c N}` si la solución es analítica.

💡 **Cómo se explica en la clase [B11-C24](../programa/clases/B11/B11-C24-metodos-espectrales-avanzados-chebyshev-y-fourier/CLASE.md):**
- ⚠️ **Error frecuente:** Esperar convergencia exponencial con funciones no analíticas. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Cuando la solución es suave, un método espectral reduce un problema que necesita miles de puntos con diferencias a una docena con Chebyshev. Pero tiene un costo: el paso máximo estable de un esquema explícito baja como `1/N⁴`, y funciona mal si la solución no es suave.

📘 **Dónde se aprende** (1 clase): [B11-C24 · Métodos espectrales avanzados (Chebyshev y Fourier)](../programa/clases/B11/B11-C24-metodos-espectrales-avanzados-chebyshev-y-fourier/CLASE.md).

### Conversación en tiempo real

- La conversación en tiempo real exige retardos pequeños.

🎯 **Por qué importa (clase B113-C03):** Ninguna clase trata el efecto del retardo en el apoyo psicológico. La decisión central: ¿qué formatos de apoyo siguen siendo posibles cuando una respuesta tarda decenas de minutos?

📘 **Dónde se aprende** (1 clase): [B113-C03 · Comunicación diferida y soporte psicológico a distancia](../programa/clases/B113/B113-C03-comunicacion-diferida-y-soporte-psicologico-a-distancia/CLASE.md).

### Conversión

- Una conversión (o *cast*) transforma un valor de un tipo a otro.
- Una conversión cambia la unidad sin cambiar la cantidad física.

💡 **Cómo se explica en la clase [B14-C04](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md):**
- La página enseña `42.0 * u.meter` y conversión con `.to`: `(1.0 * u.parsec).to(u.km)`.
- Si `a` estuviera en km y `GM_earth` en m³/s², Astropy resuelve la conversión sola; un número sin unidad no lo haría.
- ⚠️ **Error frecuente:** Confundir `.value` con una conversión. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** En 1999 la sonda Mars Climate Orbiter se perdió al llegar a Marte. NASA atribuye la pérdida a un error de navegación causado por no traducir unidades inglesas a métricas: el software en tierra usaba unidades inglesas y el de a bordo, métricas (S1).

📘 **Dónde se aprende** (2 clases): [B07-C02 · Tipos de datos y variables](../programa/clases/B07/B07-C02-tipos-de-datos-y-variables/CLASE.md); [B14-C04 · Unidades y constantes con Astropy](../programa/clases/B14/B14-C04-unidades-y-constantes-con-astropy/CLASE.md).

### Conversión AB

- La conversión AB es `m_AB = −2,5 log₁₀(f/3631 Jy)`.

💡 **Cómo se explica en la clase [B45-C21](../programa/clases/B45/B45-C21-estandares-fotometricos-y-sistemas-de-referencia/CLASE.md):**
- Conversión AB: 3631,0 Jy → -0,000, 363,1 Jy → 2,500, 1,0 Jy → 8,900, 0,001 Jy → 16,400.
- 🎯 **Por qué importa:** Sin estándares la escala de un cielo concreto es arbitraria. La decisión central: ¿qué ecuación de transformación se ajusta y con qué error en la magnitud final?

📘 **Dónde se aprende** (1 clase): [B45-C21 · Estándares fotométricos y sistemas de referencia](../programa/clases/B45/B45-C21-estandares-fotometricos-y-sistemas-de-referencia/CLASE.md).

### Conversión ida y vuelta

- La conversión ida y vuelta es la prueba `estado → elementos → estado`.

🎯 **Por qué importa (clase B72-C12):** Un catálogo publica elementos de un instante; usarlos como si fueran constantes introduce errores de kilómetros. La decisión central: ¿cuánto difiere un elemento osculador del medio y qué error de fase o de periodo produce usar el equivocado?

📘 **Dónde se aprende** (1 clase): [B72-C12 · Variaciones de elementos osculadores](../programa/clases/B72/B72-C12-variaciones-de-elementos-osculadores/CLASE.md).

### Conversión superficie–frente de onda

- La conversión superficie–frente de onda es `2 cos θ` en un espejo y `(n − 1)` en una cara refractiva con aire.

🎯 **Por qué importa (clase B50-C15):** El requisito de un instrumento se cumple o no según cómo se reparta el error entre diseño, fabricación y alineación. La decisión central: ¿cuánto frente de onda se puede gastar en cada etapa sin superar el requisito?

📘 **Dónde se aprende** (1 clase): [B50-C15 · Presupuesto de error de frente de onda de un instrumento](../programa/clases/B50/B50-C15-presupuesto-de-error-de-frente-de-onda-de-un-instrumento/CLASE.md).

### Convolución

- La convolución de `x` y `h` es `(x ∗ h)[n] = Σ_m x[m] h[n − m]` (la definición de NumPy en S2 es la misma con otro orden de nombres: se voltea una secuencia y se desliza sobre la otra).
- La convolución de `h` y `u` es `(h∗u)(t) = ∫₀ᵗ h(t−s) u(s) ds` (fuente S2).
- La convolución (en redes, una correlación cruzada: producto punto de un núcleo con cada ventana de la imagen, sin invertir el núcleo) produce un mapa de respuestas; en modo válido la salida mide `N − k + 1` por lado.
- *(y 2 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C08](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md):**
- Resulta `y[n] = Σ_m x[m] h[n − m]`: la convolución.
- La media móvil de C07 es la convolución con `h[m] = 1/M`.
- ⚠️ **Error frecuente:** Multiplicar DFT sin rellenar y creer que se obtiene la convolución lineal. Se corrige con el ejercicio 10.
- 🎯 **Por qué importa:** Un termistor a bordo de una nave no mide la temperatura del instante: mide una versión retrasada y suavizada, porque su cuerpo tarda en calentarse o enfriarse. Si la nave entra en eclipse y el entorno baja 50 K de golpe, el sensor irá bajando poco a poco.

📘 **Dónde se aprende** (7 clases): [B15-C08 · Convolución y respuesta impulsional](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md); [B16-C03 · Sistemas lineales invariantes](../programa/clases/B16/B16-C03-sistemas-lineales-invariantes/CLASE.md); [B17-C11 · Redes de segmentación semántica de imágenes](../programa/clases/B17/B17-C11-redes-de-segmentacion-semantica-de-imagenes/CLASE.md); [B32-C06 · Micro y macroturbulencia y granulación estelar](../programa/clases/B32/B32-C06-micro-y-macroturbulencia-y-granulacion-estelar/CLASE.md); [B32-C11 · Ensanchamiento rotacional y v sin i](../programa/clases/B32/B32-C11-ensanchamiento-rotacional-y-v-sin-i/CLASE.md); [B38-C08 · Observaciones sintéticas de galaxias simuladas](../programa/clases/B38/B38-C08-observaciones-sinteticas-de-galaxias-simuladas/CLASE.md) y 1 más.

### Convolución circular

- La convolución circular es la que implícitamente calcula el producto de DFT: supone que las series se repiten.

💡 **Cómo se explica en la clase [B15-C08](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md):**
- El teorema de convolución (S1, §1.14, la propiedad de convolución: la transformada de `f ∗ g` es el producto de las transformadas, con la normalización de S1) tiene una versión discreta: la DFT de la convolución circular es el producto de las DFT.
- 🎯 **Por qué importa:** Un termistor a bordo de una nave no mide la temperatura del instante: mide una versión retrasada y suavizada, porque su cuerpo tarda en calentarse o enfriarse. Si la nave entra en eclipse y el entorno baja 50 K de golpe, el sensor irá bajando poco a poco.

📘 **Dónde se aprende** (1 clase): [B15-C08 · Convolución y respuesta impulsional](../programa/clases/B15/B15-C08-convolucion-y-respuesta-impulsional/CLASE.md).

### Coordenada

- La coordenada `r` se define de modo que una circunferencia mide `2πr`.

💡 **Cómo se explica en la clase [B26-C07](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md):**
- Paso 2 · Distancia coordenada. `Δr = 6,957 × 10⁸ m`.
- Paso 6 · Sentido. La distancia propia es `1,5 × 10⁻⁶` mayor que la coordenada.
- 🎯 **Por qué importa:** Medir una distancia cerca de una masa grande no da lo mismo que en el espacio plano: el radio de un círculo y su circunferencia dejan de cumplir `C = 2πR`. Los GPS, las lentes gravitacionales y los agujeros negros dependen de esa diferencia.

📘 **Dónde se aprende** (1 clase): [B26-C07 · Curvatura y métricas](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md).

### Coordenadas

- Las coordenadas de `v` en la base `{b₁, …, b_n}` son los números `c_k` tales que `v = Σ c_k b_k`.

💡 **Cómo se explica en la clase [B10-C02](../programa/clases/B10/B10-C02-bases-y-dimension/CLASE.md):**
- En `ℝ³` la base canónica es `{(1,0,0), (0,1,0), (0,0,1)}` y las coordenadas son las componentes habituales.
- Una base ortonormal es cómoda (coordenadas por producto escalar) y numéricamente estable.
- ⚠️ **Error frecuente:** Pensar que las coordenadas son el vector. Se corrige con el ejercicio 9.
- 🎯 **Por qué importa:** Un vector es una entidad geométrica; sus «componentes» dependen de los ejes que elijas. Un operador de estación terrestre describe un satélite con ejes ligados al ecuador; el satélite mismo, con ejes ligados a su órbita; un instrumento, con ejes del instrumento.

📘 **Dónde se aprende** (1 clase): [B10-C02 · Bases y dimensión](../programa/clases/B10/B10-C02-bases-y-dimension/CLASE.md).

### Coordenadas cartesianas

- Las coordenadas cartesianas `(x, y)` dan la posición por las distancias a dos ejes perpendiculares.

🎯 **Por qué importa (clase B04-C10):** Un cometa se describe mejor diciendo «está a 2,19 au del Sol, a 120° del perihelio» que dando dos coordenadas rectangulares. Y un programa que convierte mal el ángulo coloca el cometa en el lado opuesto del Sol.

📘 **Dónde se aprende** (1 clase): [B04-C10 · Coordenadas polares y cartesianas](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md).

### Coordenadas esféricas

- Las coordenadas esféricas dan un punto del espacio por su distancia `r` al origen y dos ángulos.

🎯 **Por qué importa (clase B04-C11):** Un catálogo de estrellas da para cada una dos números: dónde está en el cielo. Pero un programa que cruza catálogos, calcula separaciones o apunta un telescopio no trabaja con horas y grados: trabaja con vectores.

📘 **Dónde se aprende** (1 clase): [B04-C11 · Coordenadas esféricas](../programa/clases/B04/B04-C11-coordenadas-esfericas/CLASE.md).

### Coordenadas estándar

- Las coordenadas estándar `(ξ, η)` son las del plano.

💡 **Cómo se explica en la clase [B58-C06](../programa/clases/B58/B58-C06-astrometria-de-objetos-menores/CLASE.md):**
- *Descripción textual:* las estrellas de referencia fijan por mínimos cuadrados las constantes que llevan los píxeles a coordenadas estándar; la proyección inversa da la ascensión recta y la declinación.
- 🎯 **Por qué importa:** Una órbita no puede ser mejor que sus posiciones: un error de décimas de segundo de arco se amplifica al propagar. La decisión central: ¿con qué exactitud puedo asignar coordenadas a un objeto en una imagen y qué la limita?

📘 **Dónde se aprende** (1 clase): [B58-C06 · Astrometría de objetos menores](../programa/clases/B58/B58-C06-astrometria-de-objetos-menores/CLASE.md).

### Coordenadas generalizadas

- Las coordenadas generalizadas `q = (q₁, q₂)` son los ángulos de las articulaciones, medidos desde la horizontal.

🎯 **Por qué importa (clase B102-C01):** Un manipulador de un rover se diseña y se ensaya en la Tierra, pero trabaja en Marte o en la Luna. La decisión central: ¿qué par necesita cada articulación en otro cuerpo, y qué cambia además del par?

📘 **Dónde se aprende** (1 clase): [B102-C01 · Dinámica multicuerpo de rovers y manipuladores](../programa/clases/B102/B102-C01-dinamica-multicuerpo-de-rovers-y-manipuladores/CLASE.md).

### Coordenadas ICRS

- Las coordenadas ICRS `(α, δ)` son ascensión recta y declinación respecto de esos ejes.

🎯 **Por qué importa (clase B13-C21):** Para seguir una nave en el espacio profundo hay que decir en qué dirección está respecto de un marco fijo. Si el marco gira aunque sea un poco, todas las direcciones se desplazan.

📘 **Dónde se aprende** (1 clase): [B13-C21 · Sistema de referencia celeste ICRF y cuásares](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md).

### Coordenadas polares

- Las coordenadas polares `(r, θ)` la dan por la distancia `r` a un origen (el polo) y el ángulo `θ` medido desde un eje polar.

🎯 **Por qué importa (clase B04-C10):** Un cometa se describe mejor diciendo «está a 2,19 au del Sol, a 120° del perihelio» que dando dos coordenadas rectangulares. Y un programa que convierte mal el ángulo coloca el cometa en el lado opuesto del Sol.

📘 **Dónde se aprende** (1 clase): [B04-C10 · Coordenadas polares y cartesianas](../programa/clases/B04/B04-C10-coordenadas-polares-y-cartesianas/CLASE.md).

### Coordenadas (u, v, w)

- Las coordenadas `(u, v, w)` están en longitudes de onda y miran a la fuente (`w` hacia ella).

🎯 **Por qué importa (clase B46-C14):** La línea de base fija la escala angular que se ve y el retardo que hay que compensar. La decisión central: ¿qué punto del plano `uv` y qué retardo corresponden a una línea de base y a una dirección?

📘 **Dónde se aprende** (1 clase): [B46-C14 · Líneas de base interferométricas](../programa/clases/B46/B46-C14-lineas-de-base-interferometricas/CLASE.md).

### Coordinación

- La coordinación es la negociación con administraciones cuyos servicios pueden verse afectados.
- La coordinación busca evitar interferencia entre sistemas.

💡 **Cómo se explica en la clase [B119-C09](../programa/clases/B119/B119-C09-derecho-y-normas-de-telecomunicaciones/CLASE.md):**
- N["Notificación a la UIT"] --> C["Coordinación"]
- Por procedimiento: notificación, coordinación, inscripción.
- 🎯 **Por qué importa:** Ninguna clase anterior vincula el derecho de telecomunicaciones con el cálculo de interferencia; B120 trata licencias y espectro en detalle y esta clase fija el marco.

📘 **Dónde se aprende** (2 clases): [B119-C09 · Derecho y normas de telecomunicaciones](../programa/clases/B119/B119-C09-derecho-y-normas-de-telecomunicaciones/CLASE.md); [B120-C01 · Licencias satelitales y procedimiento de notificación](../programa/clases/B120/B120-C01-licencias-satelitales-y-procedimiento-de-notificacion/CLASE.md).

### Copa de Faraday

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C24):** La energía por carga elegida por el analizador determina qué se mide; la resolución de los canales limita la temperatura que se recupera. La decisión central: ¿cuántos canales y qué corrección dan la velocidad y la temperatura del plasma con error aceptable?

📘 **Dónde se aprende** (1 clase): [B47-C24 · Instrumentos de plasma y campos in situ](../programa/clases/B47/B47-C24-instrumentos-de-plasma-y-campos-in-situ/CLASE.md).

### Copia

- Una vista es un arreglo que mira los mismos datos que otro sin copiarlos; una copia tiene datos propios.

💡 **Cómo se explica en la clase [B14-C02](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md):**
- Indexar con una lista de posiciones `est[[0, 1]]` crea una copia.
- ⚠️ **Error frecuente:** Confundir vista y copia. Se corrige con los ejercicios 5 y 11.
- 🎯 **Por qué importa:** Una constelación de seis satélites y cinco estaciones en tierra producen treinta distancias. Un catálogo de estrellas produce millones.

📘 **Dónde se aprende** (1 clase): [B14-C02 · Arreglos multidimensionales NumPy](../programa/clases/B14/B14-C02-arreglos-multidimensionales-numpy/CLASE.md).

### COPUOS

- COPUOS es la Comisión sobre la Utilización del Espacio Ultraterrestre con Fines Pacíficos.

💡 **Cómo se explica en la clase [B119-C06](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md):**
- *Descripción textual:* la Asamblea crea COPUOS; este tiene dos subcomités y una secretaría; decide por consenso, lo que da poder de bloqueo a cada miembro.
- Según el resumen de búsqueda de las páginas de UNOOSA (2026-11-11), la Asamblea General creó COPUOS como órgano ad hoc con 18 miembros por la res. 1348 (XIII) del 13-12-1958 y lo hizo permanente por la res. 1472 (XIV) del 12-12-1959; tiene un Subcomité Científico y Técnico y un Subcomité Jurídico, y UNOOSA es su secretaría.
- ⚠️ **Error frecuente:** Atribuir la decisión a UNOOSA y no a COPUOS. Se corrige con la sección 8.1.
- 🎯 **Por qué importa:** Quien estudia el derecho espacial necesita saber dónde se negocia y cómo se decide; ninguna clase anterior trata los organismos. La decisión central: ¿cómo cambia la probabilidad de bloqueo cuando crece el número de miembros que deben consentir?

📘 **Dónde se aprende** (1 clase): [B119-C06 · Organismos UNOOSA y COPUOS](../programa/clases/B119/B119-C06-organismos-unoosa-y-copuos/CLASE.md).

### Cordón

- El cordón es el material depositado; su ancho es `w`.

💡 **Cómo se explica en la clase [B59-C13](../programa/clases/B59/B59-C13-impresion-3d-extraterrestre/CLASE.md):**
- Una cúpula hemisférica de 3,0 m de radio exterior y 0,30 m de pared, con cordón de 5 cm y velocidad 0,10 m/s (todo ilustrativo).
- 🎯 **Por qué importa:** Una capa más fina da mejor forma pero más tiempo; y una cúpula tiene una zona alta que no se puede imprimir sin apoyo. La decisión central: ¿qué grosor de capa y qué perfil de cúpula hacen viable la impresión?

📘 **Dónde se aprende** (1 clase): [B59-C13 · Impresión 3D extraterrestre](../programa/clases/B59/B59-C13-impresion-3d-extraterrestre/CLASE.md).

### Cordón de seguridad

- El cordón de seguridad ata a la persona a un anclaje; limita la distancia al anclaje.

🎯 **Por qué importa (clase B108-C02):** Ninguna clase planifica rutas y accesibilidad de una EVA en una estructura. La decisión central: ¿por qué asideros pasa la persona, cuánto tarda y qué restricciones (alcance, cordón) pueden dejar un puesto inaccesible?

📘 **Dónde se aprende** (1 clase): [B108-C02 · Planificación de desplazamientos y rutas de EVA](../programa/clases/B108/B108-C02-planificacion-de-desplazamientos-y-rutas-de-eva/CLASE.md).

### Coriolis y centrífugo

- El término de Coriolis y centrífugo `C(q, q̇) q̇` aparece al girar varias articulaciones a la vez.

🎯 **Por qué importa (clase B102-C01):** Un manipulador de un rover se diseña y se ensaya en la Tierra, pero trabaja en Marte o en la Luna. La decisión central: ¿qué par necesita cada articulación en otro cuerpo, y qué cambia además del par?

📘 **Dónde se aprende** (1 clase): [B102-C01 · Dinámica multicuerpo de rovers y manipuladores](../programa/clases/B102/B102-C01-dinamica-multicuerpo-de-rovers-y-manipuladores/CLASE.md).

### Corona

- La fotosfera es la capa que emite la luz visible; la cromosfera y la corona están encima.
- Una corona es una estructura circular asociada a procesos del manto (concepto; no se calcula aquí).

💡 **Cómo se explica en la clase [B30-C02](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md):**
- Para la corona de `1,5 × 10⁶ K` el exponente en el infinito es `GMμu/(kTR) = 9,18`.
- La corona, 260 veces más caliente que la fotosfera, es un gas que se extiende tanto que su presión a gran distancia no desaparece.
- 🎯 **Por qué importa:** La corona caliente es el origen del viento solar y de gran parte de la actividad. Entender por qué no puede estar en reposo conecta el Sol con el medio interplanetario.

📘 **Dónde se aprende** (2 clases): [B30-C02 · Fotosfera, cromosfera y corona](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md); [B70-C05 · Actividad volcánica venusina: llanuras, coronas e indicios de actividad reciente](../programa/clases/B70/B70-C05-actividad-volcanica-venusina-llanuras-coronas-e-indicios-de-actividad-reciente/CLASE.md).

### Coronógrafo

- El coronógrafo bloquea el disco solar para ver la corona.

🎯 **Por qué importa (clase B30-C13):** Saber cuándo llegará una CME determina el margen de alerta. La decisión central: ¿cuánto tarda en llegar y cuánto depende ese tiempo del arrastre?

📘 **Dónde se aprende** (1 clase): [B30-C13 · Eyecciones de masa coronal](../programa/clases/B30/B30-C13-eyecciones-de-masa-coronal/CLASE.md).

### Corpus

- El corpus guarda entradas que descubren ramas nuevas.

💡 **Cómo se explica en la clase [B88-C37](../programa/clases/B88/B88-C37-fuzzing-autorizado-de-software-embarcado-en-banco-de-pruebas/CLASE.md):**
- C["Corpus de semillas"] --> M["Mutar una entrada"]
- *Descripción textual:* se muta una entrada del corpus y se ejecuta el objetivo; las excepciones se registran y las entradas que abren ramas nuevas pasan al corpus.
- 🎯 **Por qué importa:** Las pruebas diseñadas por una persona no prevén todas las combinaciones. La decisión central: ¿qué estrategia de entradas encuentra más fallos con menos ejecuciones en un banco autorizado?

📘 **Dónde se aprende** (1 clase): [B88-C37 · Fuzzing autorizado de software embarcado en banco de pruebas](../programa/clases/B88/B88-C37-fuzzing-autorizado-de-software-embarcado-en-banco-de-pruebas/CLASE.md).

### Corrección

- La corrección es el valor que se suma para compensar un sesgo conocido.
- La corrección en el instante `t` es `dv(t) = −Φ_rv(T,t)⁻¹ [Φ_rr(T,t) δr(t) + Φ_rv(T,t) δv(t)]`.
- La detección es que el error se advierta; la corrección, que se acepte y se repare.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B13-C04](../programa/clases/B13/B13-C04-errores-sistematicos-y-aleatorios/CLASE.md):**
- La corrección resultante hereda esa incertidumbre;
- *Descripción textual:* una lectura se descompone en verdad, sesgo y ruido; el promedio solo reduce el ruido; el sesgo se elimina con una corrección obtenida de un patrón.
- 🎯 **Por qué importa:** Una estación mide el instante de llegada de un pulso de una baliza. Cada lectura fluctúa por ruido electrónico, y además hay un retardo constante del cable que nadie incluyó.

📘 **Dónde se aprende** (6 clases): [B13-C04 · Errores sistemáticos y aleatorios](../programa/clases/B13/B13-C04-errores-sistematicos-y-aleatorios/CLASE.md); [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md); [B74-C08 · Filtrado recursivo de estados](../programa/clases/B74/B74-C08-filtrado-recursivo-de-estados/CLASE.md); [B81-C15 · Robustez de trayectoria ante fallas](../programa/clases/B81/B81-C15-robustez-de-trayectoria-ante-fallas/CLASE.md); [B104-C07 · Factores de liderazgo](../programa/clases/B104/B104-C07-factores-de-liderazgo/CLASE.md); [B104-C12 · Robótica tripulada](../programa/clases/B104/B104-C12-robotica-tripulada/CLASE.md).

### Corrección atmosférica

- La corrección atmosférica convierte `ρ_TOA` en `ρ_s`.

🎯 **Por qué importa (clase B57-C26):** Comparar imágenes de fechas distintas con atmósferas distintas confunde atmósfera con cambio. La decisión central: ¿cuánto sesga la atmósfera y cómo se estima y descuenta con la información disponible?

📘 **Dónde se aprende** (1 clase): [B57-C26 · Corrección atmosférica de imágenes](../programa/clases/B57/B57-C26-correccion-atmosferica-de-imagenes/CLASE.md).

### Corrección baricéntrica

- La corrección baricéntrica quita el movimiento de la Tierra.

💡 **Cómo se explica en la clase [B45-C12](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md):**
- ⚠️ **Error frecuente:** Olvidar la corrección baricéntrica. Se corrige con 8.3.
- 🎯 **Por qué importa:** Las velocidades radiales descubren planetas, binarias y la expansión del universo. La decisión central: ¿cómo se pasa de un corrimiento a una velocidad y con qué precisión?

📘 **Dónde se aprende** (1 clase): [B45-C12 · Efecto Doppler en espectros](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md).

### Corrección de Bonferroni

- La corrección de Bonferroni usa `α/k` por prueba.
- La corrección de Bonferroni divide `α` entre el número de pruebas.
- Las comparaciones múltiples inflan `α`; la corrección de Bonferroni usa `α/m`.

💡 **Cómo se explica en la clase [B20-C02](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md):**
- La corrección de Bonferroni exige `p < α/k` en cada prueba.
- 🎯 **Por qué importa:** Un grupo mide cinco variantes razonables de un mismo análisis y publica la que da «un resultado significativo». Nadie mintió con un número, y sin embargo el resultado ya no significa lo que dice.

📘 **Dónde se aprende** (3 clases): [B14-C23 · Protocolo preregistrado de análisis](../programa/clases/B14/B14-C23-protocolo-preregistrado-de-analisis/CLASE.md); [B20-C02 · Diseño de un plan de análisis y preregistro](../programa/clases/B20/B20-C02-diseno-de-un-plan-de-analisis-y-preregistro/CLASE.md); [B105-C20 · Diseño de protocolo médico simulado](../programa/clases/B105/B105-C20-diseno-de-protocolo-medico-simulado/CLASE.md).

### Corrección de flujo

- La corrección de flujo (*refluxing*) reemplaza el flujo grueso en una interfaz por el flujo fino.

💡 **Cómo se explica en la clase [B21-C05](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md):**
- Paso 4 · Corrección de flujo. Sea la advección con `a = 1`, `ν = 0,8` y una celda gruesa a la izquierda del parche con `u_viejo = 1,0`.
- 🎯 **Por qué importa:** Los códigos de referencia en astrofísica, como RAMSES (S1) y Athena++ (S2), usan mallas adaptativas porque los problemas tienen rangos de escala enormes. Pero un esquema adaptativo mal construido no conserva: crea o destruye masa en las interfaces entre niveles, justo donde está el fenómeno interesante.

📘 **Dónde se aprende** (1 clase): [B21-C05 · Mallas adaptativas (AMR)](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md).

### Corrección de primer orden

- La corrección de primer orden por sesgo usa el jacobiano `J = ∂Δ/∂b` evaluado en el sesgo de linealización.

🎯 **Por qué importa (clase B80-C09):** B87-C06 trata los giroscopios; falta la integración conjunta de acelerómetros y giroscopios para estimar el movimiento de un robot y su deriva. La decisión central: ¿cómo se reutiliza una integración inercial cuando cambian el estado inicial y los sesgos estimados?

📘 **Dónde se aprende** (1 clase): [B80-C09 · Odometría inercial y preintegración de IMU](../programa/clases/B80/B80-C09-odometria-inercial-y-preintegracion-de-imu/CLASE.md).

### Corrección de sesgo

- La corrección de sesgo resta el aporte esperado del ruido.

💡 **Cómo se explica en la clase [B103-C04](../programa/clases/B103/B103-C04-deteccion-de-obstaculos-y-mapas-de-traversabilidad/CLASE.md):**
- Con el ruido ilustrativo `σ_h = 0,0005 r²` (5 cm a 10 m), el clasificador bruto deja pasar solo 27 peligros de 22 144, pero da un 99,4 % de falsas alarmas entre 10 y 15 m; con corrección de sesgo, las falsas alarmas bajan a 0,6 % pero se pierde el 72,9 % de los peligros en esa banda.
- 🎯 **Por qué importa:** El ruido del MDE crece con el cuadrado del rango y, a partir de cierta distancia, la señal de un obstáculo queda por debajo del ruido. La decisión central: ¿hasta qué rango se puede clasificar el terreno de forma útil, y qué política (conservadora o corregida) elegir más allá?

📘 **Dónde se aprende** (1 clase): [B103-C04 · Detección de obstáculos y mapas de traversabilidad](../programa/clases/B103/B103-C04-deteccion-de-obstaculos-y-mapas-de-traversabilidad/CLASE.md).

### Corrección de Van Vleck

- La corrección de Van Vleck: `ρ = sin(π ρ_q/2)` para 1 bit.

🎯 **Por qué importa (clase B51-C12):** La elección de bits y de formato fija cuánta sensibilidad se pierde y cuánto disco y red se necesitan. La decisión central: ¿cuántos bits por muestra, qué eficiencia se obtiene y cómo se empaqueta sin perder información?

📘 **Dónde se aprende** (1 clase): [B51-C12 · Formatos de datos VLBI y geodésicos](../programa/clases/B51/B51-C12-formatos-de-datos-vlbi-y-geodesicos/CLASE.md).

### Corrección determinista

- La corrección determinista busca `g * t ≈ error`.

🎯 **Por qué importa (clase B43-C05):** Pulir es controlar un retiro de décimas de micrón: sin un modelo se oscila entre sobrecorregir y subcorregir. La decisión central: ¿cuánto hay que retirar de la mejor esfera para obtener un paraboloide y cuánto tiempo debe permanecer la herramienta en cada zona?

📘 **Dónde se aprende** (1 clase): [B43-C05 · Pulido óptico](../programa/clases/B43/B43-C05-pulido-optico/CLASE.md).

### Corrección diferencial

- La corrección diferencial ajusta `v_y0` hasta anular `vx` en el cruce.
- La corrección diferencial ajusta el estado inicial hasta que la órbita se cierre.

🎯 **Por qué importa (clase B73-C05):** Una nave que orbita un punto de Lagrange sigue una órbita periódica, no el punto. Hallarla exige resolver un problema de contorno: no hay fórmula.

📘 **Dónde se aprende** (2 clases): [B73-C05 · Órbitas periódicas](../programa/clases/B73/B73-C05-orbitas-periodicas/CLASE.md); [B76-C05 · Órbitas NRHO](../programa/clases/B76/B76-C05-orbitas-nrho/CLASE.md).

### Corrección norte-sur

- La corrección norte-sur es la maniobra que devuelve la inclinación a cero.

🎯 **Por qué importa (clase B72-C10):** Un satélite geoestacionario sin maniobras de inclinación deriva de su plano ecuatorial algo menos de un grado por año, y el combustible de ese mantenimiento fija su vida útil. La decisión central: ¿cuánto contribuye cada cuerpo a la deriva de la inclinación y cuánto de ese resultado depende de simplificar la órbita lunar?

📘 **Dónde se aprende** (1 clase): [B72-C10 · Perturbaciones lunares](../programa/clases/B72/B72-C10-perturbaciones-lunares/CLASE.md).

### Correcto pero insuficiente

- Un requisito puede ser correcto pero insuficiente si no cubre un escenario de uso.

🎯 **Por qué importa (clase B83-C17):** Un proyecto puede pasar todas las pruebas de requisitos y fracasar en el uso. La decisión central: ¿además de cumplir los requisitos, el sistema satisface la necesidad en las condiciones reales de uso?

📘 **Dónde se aprende** (1 clase): [B83-C17 · Verificación frente a validación](../programa/clases/B83/B83-C17-verificacion-frente-a-validacion/CLASE.md).

### Corrector

- `s_{k+1} = s_k + (h/2)(k₁ + k₂)` (corrector).

🎯 **Por qué importa (clase B11-C06):** Una evaluación de `F` en un cálculo de trayectorias es cara cuando incluye gravedad de varios cuerpos o un modelo de atmósfera. La pregunta práctica es siempre cuánta precisión compra cada evaluación.

📘 **Dónde se aprende** (1 clase): [B11-C06 · Método de Heun](../programa/clases/B11/B11-C06-metodo-de-heun/CLASE.md).

### Corrector de coma

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C20](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md):**
- El cálculo muestra que el espejo y el plano cumplen, pero que el instrumento no cubre el sensor completo sin un corrector de coma: la conclusión del diseño no es «todo cumple» sino qué hay que añadir.
- 🎯 **Por qué importa:** Un diseño es un conjunto de compromisos. La decisión central: ¿qué apertura y qué focal cumplen el objetivo y qué defecto domina?

📘 **Dónde se aprende** (1 clase): [B41-C20 · Diseño preliminar de un telescopio](../programa/clases/B41/B41-C20-diseno-preliminar-de-un-telescopio/CLASE.md).

### Corredor de aerofrenado

- El corredor de aerofrenado es el rango de altitudes de periapsis útiles.

🎯 **Por qué importa (clase B75-C15):** Cada pasada baja el apoapsis un poco, y hace falta algún margen de seguridad con la densidad. La decisión central: ¿cuántas pasadas y cuánto tiempo hacen falta para bajar el apoapsis, y qué delta-v propulsivo se ahorra?

📘 **Dónde se aprende** (1 clase): [B75-C15 · Aerofrenado conceptual](../programa/clases/B75/B75-C15-aerofrenado-conceptual/CLASE.md).

### Corredor de entrada

- El corredor de entrada es el intervalo de ángulos de entrada aceptables.

🎯 **Por qué importa (clase B77-C25):** El corredor es la tolerancia que se le deja a la navegación y a la guía antes de entrar. La decisión central: ¿entre qué ángulos puede entrar el vehículo, cuánto ensancha el corredor la sustentación y cuándo falla la estimación de Allen–Eggers?

📘 **Dónde se aprende** (1 clase): [B77-C25 · Corredores de entrada y límites de trayectoria](../programa/clases/B77/B77-C25-corredores-de-entrada-y-limites-de-trayectoria/CLASE.md).

### Correlación

- La correlación `ρ` entre dos medidas cambia la incertidumbre combinada: `σ² = 1/(1ᵀC⁻¹1)`.
- La correlación de Pearson.
- Ruido: error independiente de cada revisor. Correlación: acuerdo lineal entre nota y mérito.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B26-C21](../programa/clases/B26/B26-C21-verosimilitud-cosmologica-con-datos-combinados/CLASE.md):**
- Con dos medidas de `σ = 0,018` y `0,015` y correlación `ρ`, la incertidumbre combinada es `0,01152` si `ρ = 0`, `0,01400` si `ρ = 0,5` y `0,01483` si `ρ = 0,9`: la correlación quita información.
- 🎯 **Por qué importa:** Ninguna sonda fija sola todos los parámetros; combinarlas reduce la incertidumbre, pero solo si son compatibles entre sí y si se tratan bien sus correlaciones. La decisión central: dadas tres restricciones sobre `Ω_m`, ¿cuál es el valor combinado, qué incertidumbre tiene y son consistentes entre sí?

📘 **Dónde se aprende** (7 clases): [B26-C21 · Verosimilitud cosmológica con datos combinados](../programa/clases/B26/B26-C21-verosimilitud-cosmologica-con-datos-combinados/CLASE.md); [B33-C01 · Validación de modelos MHD con eventos solares documentados](../programa/clases/B33/B33-C01-validacion-de-modelos-mhd-con-eventos-solares-documentados/CLASE.md); [B34-C07 · Comparación de modelos coronales con observaciones](../programa/clases/B34/B34-C07-comparacion-de-modelos-coronales-con-observaciones/CLASE.md); [B48-C03 · Propuestas científicas y criterios](../programa/clases/B48/B48-C03-propuestas-cientificas-y-criterios/CLASE.md); [B74-C11 · Matrices de covarianza — Estimación de órbitas y navegación espacial](../programa/clases/B74/B74-C11-matrices-de-covarianza-estimacion-de-orbitas-y-navegacion-espacial/CLASE.md); [B85-C27 · Márgenes y correlación térmica](../programa/clases/B85/B85-C27-margenes-y-correlacion-termica/CLASE.md) y 1 más.

### Correlación cruzada

- La correlación cruzada mide cuánto se parecen dos imágenes al desplazarlas.
- La correlación cruzada compara una curva con otra desplazada.
- La correlación cruzada compara el espectro con una plantilla desplazada.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C14](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md):**
- Correlación cruzada normalizada: más robusta al ruido, algo más lenta.
- 🎯 **Por qué importa:** El telescopio apunta con deriva, la nave rota entre tomas y el campo gira un poco. Apilar diez imágenes sin alinearlas emborrona las estrellas; restar dos sin alinear crea falsos «residuos».

📘 **Dónde se aprende** (5 clases): [B15-C14 · Registro y alineación](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md); [B27-C20 · Análisis multibanda de un evento extremo](../programa/clases/B27/B27-C20-analisis-multibanda-de-evento-extremo/CLASE.md); [B34-C09 · Integración multiinstrumento de datos heliofísicos](../programa/clases/B34/B34-C09-integracion-multiinstrumento-de-datos-heliofisicos/CLASE.md); [B45-C12 · Efecto Doppler en espectros](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md); [B51-C08 · Compensación de retardo y alineación temporal de flujos de antenas](../programa/clases/B51/B51-C08-compensacion-de-retardo-y-alineacion-temporal-de-flujos-de-antenas/CLASE.md).

### Correlación de fase

- La correlación de fase usa solo la fase del espectro cruzado: `R = conj(F₁) F₂ / |conj(F₁) F₂|`, y su transformada inversa tiene un pico en el desplazamiento.

💡 **Cómo se explica en la clase [B15-C14](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md):**
- Correlación de fase: no necesita identificar estrellas, es rápida (FFT), pero solo traslaciones (con extensiones para giros) y sufre con ruido.
- La correlación de fase hace ese deslizamiento con la FFT, de una sola vez.
- ⚠️ **Error frecuente:** Usar correlación de fase con mucho ruido. Se corrige con el ejercicio 5.
- 🎯 **Por qué importa:** El telescopio apunta con deriva, la nave rota entre tomas y el campo gira un poco. Apilar diez imágenes sin alinearlas emborrona las estrellas; restar dos sin alinear crea falsos «residuos».

📘 **Dónde se aprende** (1 clase): [B15-C14 · Registro y alineación](../programa/clases/B15/B15-C14-registro-y-alineacion/CLASE.md).

### Correlación ítem–total corregida

- La correlación ítem–total corregida correlaciona un ítem con la suma de los demás.

🎯 **Por qué importa (clase B105-C27):** Un cuestionario con ítems que no miden lo mismo produce una puntuación poco fiable, y con pocos participantes su fiabilidad ni siquiera se puede estimar. La decisión central: ¿qué ítems sobran, cuántos ítems hacen falta y cuántos participantes se necesitan para estimar el alfa con una incertidumbre aceptable?

📘 **Dónde se aprende** (1 clase): [B105-C27 · Instrumentos validados y psicometría en investigación](../programa/clases/B105/B105-C27-instrumentos-validados-y-psicometria-en-investigacion/CLASE.md).

### Correlación positiva

- Independientes (S1, C.3.7) es más fuerte: la distribución de una no cambia al conocer la otra; independientes ⇒ `Cov = 0`, pero no al revés. Correlación positiva significa que tienden a subir juntas;

🎯 **Por qué importa (clase B12-C05):** En navegación espacial, la posición y la velocidad estimadas por un filtro no tienen errores independientes: un error de posición hacia delante suele ir acompañado de uno de velocidad. Ignorar esa relación da incertidumbres falsas, a veces demasiado optimistas y a veces demasiado pesimistas.

📘 **Dónde se aprende** (1 clase): [B12-C05 · Covarianza y correlación](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md).

### Correspondencia

- Odometría visual: estimación del movimiento propio a partir de imágenes (F6). Correspondencia: par de observaciones del mismo punto en dos instantes.

🎯 **Por qué importa (clase B99-C01):** Una trayectoria se obtiene sumando movimientos pequeños, y cada uno trae un error; esos errores no se corrigen solos. La decisión central: ¿con qué calidad de correspondencias y de medida puedo confiar en la odometría, y cuándo necesito corregirla con cierres de bucle (C04)?

📘 **Dónde se aprende** (1 clase): [B99-C01 · Odometría visual](../programa/clases/B99/B99-C01-odometria-visual/CLASE.md).

### Correspondencia por bloques

- La correspondencia por bloques busca, para cada ventana de la imagen izquierda, la ventana de la derecha con menor coste (aquí, la suma de diferencias absolutas, SAD).

🎯 **Por qué importa (clase B103-C03):** La profundidad estéreo es barata y densa, pero su error crece con el cuadrado de la distancia: a 20 m una incertidumbre de 0,3 px en la disparidad son 71 cm. La decisión central: ¿hasta qué distancia se puede confiar en el mapa de profundidad para decidir si un camino es seguro, y qué línea de base lo permite?

📘 **Dónde se aprende** (1 clase): [B103-C03 · Mapas de profundidad y correspondencia estéreo](../programa/clases/B103/B103-C03-mapas-de-profundidad-y-correspondencia-estereo/CLASE.md).

### Corriente a la pared

- La corriente a la pared `j` es la densidad de iones que la golpean.

💡 **Cómo se explica en la clase [B78-C21](../programa/clases/B78/B78-C21-erosion-y-vida-util-de-propulsores-electricos/CLASE.md):**
- *Descripción textual:* la tensión fija la energía de impacto y el rendimiento; con la corriente a la pared da la velocidad de recesión; como la energía baja al retirarse la pared resulta una ecuación lineal con solución cerrada, contrastada con una integración numérica.
- 🎯 **Por qué importa:** El impulso total que un propulsor eléctrico puede entregar no lo limita el propelente sino su desgaste. La decisión central: ¿cómo depende la vida útil de la tensión de descarga y qué fracción del empuje máximo posible con el propelente alcanza a entregar?

📘 **Dónde se aprende** (1 clase): [B78-C21 · Erosión y vida útil de propulsores eléctricos](../programa/clases/B78/B78-C21-erosion-y-vida-util-de-propulsores-electricos/CLASE.md).

### Corriente admisible

- La corriente admisible de una pista depende de su sección y del aumento de temperatura `ΔT` aceptado.

💡 **Cómo se explica en la clase [B93-C01](../programa/clases/B93/B93-C01-diseno-de-pcb-espacial-conceptual/CLASE.md):**
- Por margen: corriente admisible menos corriente real.
- 🎯 **Por qué importa:** El tronco no trataba el diseño de placas: B90 integra y B86 trata potencia, pero nadie calculaba una pista. La decisión central: ¿qué ancho de cobre y qué geometría de microtira necesita una placa para llevar una corriente y una señal dadas, y qué margen queda?

📘 **Dónde se aprende** (1 clase): [B93-C01 · Diseño de PCB espacial (conceptual)](../programa/clases/B93/B93-C01-diseno-de-pcb-espacial-conceptual/CLASE.md).

### Corriente anular

- La corriente anular es la corriente equivalente de un anillo de radio `a`.

🎯 **Por qué importa (clase B30-C22):** El índice Dst (B30-C23) es un indicador de la energía del anillo de corriente. La decisión central: ¿qué energía y qué corriente corresponden a una disminución dada del campo?

📘 **Dónde se aprende** (1 clase): [B30-C22 · Anillo de corriente y corrientes magnetosféricas](../programa/clases/B30/B30-C22-anillo-de-corriente-y-corrientes-magnetosfericas/CLASE.md).

### Corriente de alimentación

- La corriente de alimentación es la del punto de entrada.

💡 **Cómo se explica en la clase [B49-C01](../programa/clases/B49/B49-C01-antenas-de-hilo-dipolo-monopolo-e-impedancia-de-radiacion/CLASE.md):**
- La resistencia de entrada es `R/sin²(kh)`, porque la corriente de alimentación es `I₀ sin(kh)`.
- A `L = λ` la corriente de alimentación es nula y la resistencia de entrada del modelo diverge.
- 🎯 **Por qué importa:** Sin la resistencia de radiación no se sabe qué carga ve la línea ni cuánta potencia se irradia. La decisión central: ¿de qué longitud hacer el hilo y qué impedancia presentará a la línea?

📘 **Dónde se aprende** (1 clase): [B49-C01 · Antenas de hilo: dipolo, monopolo e impedancia de radiación](../programa/clases/B49/B49-C01-antenas-de-hilo-dipolo-monopolo-e-impedancia-de-radiacion/CLASE.md).

### Corriente de corte

- La corriente de corte (`C/20`) termina la carga.

💡 **Cómo se explica en la clase [B86-C06](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md):**
- La fase CV termina en la corriente de corte y repone `1,314 Ah` de los `1,399 Ah` (quedan `0,084 Ah`, que se recuperan en la órbita siguiente o con un corte más bajo).
- *Descripción textual:* la carga empieza a corriente constante hasta alcanzar la tensión máxima; luego sigue a tensión constante con corriente decreciente hasta la corriente de corte; la integral de la corriente da la carga repuesta.
- 🎯 **Por qué importa:** Cargar más rápido reduce el tiempo pero eleva el calor y la tensión sobre la celda; cargar más lento puede no completar el ciclo antes del siguiente eclipse. El perfil de carga decide si la batería vuelve a su estado de carga en cada órbita.

📘 **Dónde se aprende** (1 clase): [B86-C06 · Gestión de carga](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md).

### Corriente de fusión

- La corriente de fusión `I_f` es la mínima que lo funde.

💡 **Cómo se explica en la clase [B86-C10](../programa/clases/B86/B86-C10-proteccion-contra-sobrecorriente/CLASE.md):**
- Paso 4 · Lectura. Con `10 A`, más de tres veces la corriente de fusión, el fusible abre en unas décimas de segundo.
- 🎯 **Por qué importa:** Si el fusible aguas arriba se funde antes que el de la rama averiada, un fallo local deja sin energía a toda la nave. Una protección bien coordinada aísla la rama y conserva el resto.

📘 **Dónde se aprende** (1 clase): [B86-C10 · Protección contra sobrecorriente](../programa/clases/B86/B86-C10-proteccion-contra-sobrecorriente/CLASE.md).

### Corriente de oscuridad

- La corriente de oscuridad es la señal que se acumula sin luz y crece con la exposición (S1).

💡 **Cómo se explica en la clase [B15-C09](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md):**
- Dividir por el plano antes de restar el oscuro, o restar un oscuro de otra duración sin escalar la corriente de oscuridad, produce errores sistemáticos.
- La guía de reducción de datos CCD de Astropy (S1) describe el modelo estándar: la imagen cruda es bias, corriente de oscuridad, ruido y un «plano» que multiplica al cielo y a las estrellas; resolver ese modelo da las cuentas de las estrellas.
- 🎯 **Por qué importa:** Una cámara de un telescopio no mide «luz de estrellas»: mide un número por píxel que incluye un desplazamiento electrónico, corriente de oscuridad, el cielo, la estrella y una sensibilidad que cambia de un píxel a otro. Si analizas el número crudo, mides la cámara, no el cielo.

📘 **Dónde se aprende** (2 clases): [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md); [B47-C04 · Telescopios infrarrojos](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md).

### Corriente de oscuridad D

- La corriente de oscuridad `D` es la carga generada térmicamente, en `e⁻/s/píxel`.

🎯 **Por qué importa (clase B13-C15):** Una cámara espacial debe decidir cuánto tiempo exponer para detectar una fuente débil con una relación señal-ruido (SNR) dada. Exponer poco no la detecta; exponer demasiado satura los píxeles brillantes o desperdicia tiempo de misión.

📘 **Dónde se aprende** (1 clase): [B13-C15 · Sensibilidad de detectores](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md).

### Corriente de saturación

- La corriente de saturación `I_0` fija la tensión de circuito abierto.

🎯 **Por qué importa (clase B86-C02):** La potencia de una celda no es un número fijo: depende de la tensión a la que se la haga trabajar y de su temperatura. Elegir mal el punto de operación o ignorar la temperatura del ala cambia la potencia entregada.

📘 **Dónde se aprende** (1 clase): [B86-C02 · Celdas solares](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md).

### Corriente de tierra

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B33-C07):** Una subestación con una corriente de tierra alta puede saturar un transformador. La decisión central: ¿cómo se reparte la corriente inducida entre las subestaciones?

📘 **Dónde se aprende** (1 clase): [B33-C07 · Impactos del clima espacial en redes eléctricas](../programa/clases/B33/B33-C07-impactos-del-clima-espacial-en-redes-electricas/CLASE.md).

### Corriente eléctrica

- La corriente eléctrica `I` es la carga que atraviesa una sección por unidad de tiempo, `I = ΔQ/Δt`; se mide en amperios (`1 A = 1 C/s`).

🎯 **Por qué importa (clase B05-C16):** Un satélite recibe energía del Sol mediante paneles, la guarda en baterías y la reparte a equipos; si el cálculo está mal, la nave se apaga en el eclipse. La pregunta motivadora es: ¿cómo calcular corrientes, tensiones y potencias en una red de componentes y cuánta energía debe guardarse para pasar un eclipse?

📘 **Dónde se aprende** (1 clase): [B05-C16 · Corriente y circuitos elementales](../programa/clases/B05/B05-C16-corriente-y-circuitos-elementales/CLASE.md).

### Corriente fotogenerada

- La corriente fotogenerada `I_ph` es proporcional a la irradiancia.

🎯 **Por qué importa (clase B86-C02):** La potencia de una celda no es un número fijo: depende de la tensión a la que se la haga trabajar y de su temperatura. Elegir mal el punto de operación o ignorar la temperatura del ala cambia la potencia entregada.

📘 **Dónde se aprende** (1 clase): [B86-C02 · Celdas solares](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md).

### Corriente galvánica

- La corriente galvánica `I = ΔV/(Rp_a/A_a + Rp_c/A_c)` es la de la pila.

🎯 **Por qué importa (clase B84-C21):** Un tornillo de acero inoxidable en un panel de aluminio puede corroerlo 90 veces más rápido que otro de aluminio, y la corrosión ocurre en tierra, antes del lanzamiento. La decisión central: ¿qué pares de materiales pueden ir en contacto y cómo debe ser la relación de áreas?

📘 **Dónde se aprende** (1 clase): [B84-C21 · Compatibilidad química y galvánica de materiales](../programa/clases/B84/B84-C21-compatibilidad-quimica-y-galvanica-de-materiales/CLASE.md).

### Corriente inducida

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B33-C06):** El campo eléctrico depende de la conductividad y de la frecuencia. La decisión central: ¿cuánto vale el campo geoeléctrico y la corriente en una línea para un campo magnético dado?

📘 **Dónde se aprende** (1 clase): [B33-C06 · Corrientes geomagnéticas inducidas (GIC)](../programa/clases/B33/B33-C06-corrientes-geomagneticas-inducidas-gic/CLASE.md).

### Corriente oscura

- La corriente oscura `D(T)` es la tasa de electrones térmicos por píxel.

💡 **Cómo se explica en la clase [B44-C07](../programa/clases/B44/B44-C07-corriente-oscura/CLASE.md):**
- Paso 3 · Resultado. La corriente oscura baja `6,34` veces.
- 🎯 **Por qué importa:** La oscuridad añade señal y ruido; saber cómo escala permite elegir temperatura y exposición. La decisión central: ¿cuánto hay que enfriar para que la corriente oscura deje de importar?

📘 **Dónde se aprende** (1 clase): [B44-C07 · Corriente oscura](../programa/clases/B44/B44-C07-corriente-oscura/CLASE.md).

### Corrimiento

- El corrimiento `z = Δλ/λ`.

💡 **Cómo se explica en la clase [B45-C12](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md):**
- Como la sirena de una ambulancia: el tono sube al acercarse y baja al alejarse; el corrimiento de las líneas es proporcional a la velocidad.
- 🎯 **Por qué importa:** Las velocidades radiales descubren planetas, binarias y la expansión del universo. La decisión central: ¿cómo se pasa de un corrimiento a una velocidad y con qué precisión?

📘 **Dónde se aprende** (1 clase): [B45-C12 · Efecto Doppler en espectros](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md).

### Corrimiento al rojo

- El corrimiento al rojo es ```text z = λ_obs / λ_reposo − 1 ``` y, para `z ≪ 1`, la velocidad radial aproximada es `v = c z`.

🎯 **Por qué importa (clase B06-C17):** En B01-C01 estimaste la velocidad de una galaxia con una sola línea, H-alfa en 662,9 nm. Pero ¿cómo se sabe que esa línea es H-alfa y no otra?

📖 **Explicado a fondo:** [Corrimiento al rojo (redshift)](esencial/esencial-a-c.md#corrimiento-al-rojo-redshift) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B06-C17 · Espectros atómicos y moleculares](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md).

### Corrimiento al rojo cosmológico

- El corrimiento al rojo cosmológico `z` es el cambio fraccional de longitud de onda por la expansión.

🎯 **Por qué importa (clase B26-C11):** `H₀` fija la escala de distancias del universo y su edad aproximada, y hoy su valor depende de cómo se mida (C23). Para entender esa discusión hay que saber ajustar la ley a datos con dispersión, cuándo vale `v = cz` y qué incertidumbre se arrastra.

📘 **Dónde se aprende** (1 clase): [B26-C11 · Expansión cósmica y ley de Hubble-Lemaître](../programa/clases/B26/B26-C11-expansion-cosmica-y-ley-de-hubble-lemaitre/CLASE.md).

### Corrimiento de transición

- El corrimiento de transición `z_t` es aquel en que `ä = 0`.

🎯 **Por qué importa (clase B26-C13):** La edad del universo, la distancia a una galaxia y el calendario de su historia salen de la ecuación de Friedmann. Con ella se interpreta cualquier parámetro cosmológico.

📘 **Dónde se aprende** (1 clase): [B26-C13 · Modelo FLRW — Relatividad y cosmología](../programa/clases/B26/B26-C13-modelo-flrw-relatividad-y-cosmologia/CLASE.md).

### Corrimiento exacto

- El corrimiento exacto (Schwarzschild) es `1 + z = 1/√(1 − r_s/R)`.

🎯 **Por qué importa (clase B26-C10):** El corrimiento gravitacional ajusta los relojes de los satélites de navegación, contamina la medida de velocidades en enanas blancas y revela la compacidad de las estrellas de neutrones. La decisión central: dada la compacidad de un cuerpo, ¿cuánto vale el corrimiento de su luz y cuándo falla la aproximación de campo débil?

📘 **Dónde se aprende** (1 clase): [B26-C10 · Desplazamiento gravitacional al rojo](../programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/CLASE.md).

### Corrimiento gravitacional al rojo

- El corrimiento gravitacional al rojo es el cambio de frecuencia de la luz al subir en un campo.
- El corrimiento gravitacional al rojo es el aumento de longitud de onda de la luz al salir de un pozo de potencial.

🎯 **Por qué importa (clase B26-C06):** Los relojes de los satélites de navegación van a un ritmo ligeramente distinto de los terrestres, y un maser en una torre ve su frecuencia cambiar con la altura. Todo eso se deduce de la equivalencia entre aceleración y gravedad.

📘 **Dónde se aprende** (2 clases): [B26-C06 · Principio de equivalencia](../programa/clases/B26/B26-C06-principio-de-equivalencia/CLASE.md); [B26-C10 · Desplazamiento gravitacional al rojo](../programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/CLASE.md).

### Corrupción

- La corrupción es una alteración involuntaria de los bytes.
- La corrupción es el cambio de un elemento a una versión errónea.

💡 **Cómo se explica en la clase [B133-C02](../programa/clases/B133/B133-C02-narrativas-orales-y-transmision-del-saber-del-cielo/CLASE.md):**
- El ejemplo conductor es sintético: un relato de 12 elementos sostenido por `k` canales, con una pérdida de 0,15 y una corrupción de 0,05 por canal y generación.
- 🎯 **Por qué importa:** La transmisión oral se trata a menudo como una cadena frágil («se pierde») o como un archivo infalible («se conservó intacto»). Ninguna de las dos cosas está probada en general.

📘 **Dónde se aprende** (2 clases): [B14-C11 · Control de versiones de datos](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md); [B133-C02 · Narrativas orales y transmisión del saber del cielo](../programa/clases/B133/B133-C02-narrativas-orales-y-transmision-del-saber-del-cielo/CLASE.md).

### Corte

- Un corte es la masa donde cambia el índice.
- Un corte (sección) fija una variable y deja la otra libre.
- Acuerdo entre revisores: cuánto coinciden entre sí. Corte: fracción que se financia.

💡 **Cómo se explica en la clase [B09-C15](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md):**
- B --> D["Cada corte es una<br/>función de una variable"]
- Paso 3 · Corte a lo largo de `x`. A `±5000 km`: `−1,2818` y `−1,2824`, ambos menores.
- 🎯 **Por qué importa:** Una sonda que viaja de la Tierra a la Luna se mueve en un campo de potencial que depende de dos coordenadas del plano. Dónde están los puntos de equilibrio y qué forma tiene el campo alrededor de ellos se lee en un mapa de curvas de nivel.

📘 **Dónde se aprende** (3 clases): [B09-C15 · Funciones de varias variables](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md); [B38-C02 · Función inicial de masa y su universalidad](../programa/clases/B38/B38-C02-funcion-inicial-de-masa-y-su-universalidad/CLASE.md); [B48-C03 · Propuestas científicas y criterios](../programa/clases/B48/B48-C03-propuestas-cientificas-y-criterios/CLASE.md).

### Corte de energía

- Un corte de energía interrumpe la escritura en un byte.

🎯 **Por qué importa (clase B88-C35):** Un corte durante una escritura deja un registro a medias. La decisión central: ¿qué esquema garantiza que, cortes donde cortes, siempre haya un estado válido recuperable?

📘 **Dónde se aprende** (1 clase): [B88-C35 · Reinicio en caliente y persistencia de estado](../programa/clases/B88/B88-C35-reinicio-en-caliente-y-persistencia-de-estado/CLASE.md).

### Corte GZK

- El corte GZK es el límite por interacción con el fondo.

🎯 **Por qué importa (clase B31-C13):** La energía y la composición de un rayo cósmico se infieren de la forma de su cascada, y el fondo de microondas limita la energía que llega. La decisión central: ¿qué profundidad y tamaño tiene una cascada y a qué energía aparece un corte?

📘 **Dónde se aprende** (1 clase): [B31-C13 · Rayos cósmicos y cascadas](../programa/clases/B31/B31-C13-rayos-cosmicos-y-cascadas/CLASE.md).

### Corteza

- La corteza es la capa superior de un cuerpo diferenciado.

💡 **Cómo se explica en la clase [B61-C07](../programa/clases/B61/B61-C07-cuencas-multianillo-y-grandes-impactos/CLASE.md):**
- Con profundidad de excavación ilustrativa 0,1 D y corteza de 40 km: 300 km → 30 km (corteza); 600 km → 60 km (manto); 1000 km → 100 km (manto).
- 🎯 **Por qué importa:** Las cuencas dejan huella en la corteza entera. La decisión central: ¿cómo se espacian los anillos, qué proyectil implica una cuenca y cuándo excava hasta el manto?

📘 **Dónde se aprende** (1 clase): [B61-C07 · Cuencas multianillo y grandes impactos](../programa/clases/B61/B61-C07-cuencas-multianillo-y-grandes-impactos/CLASE.md).

### Cortisol relativo

- El cortisol relativo `C` es adimensional.

🎯 **Por qué importa (clase B105-C22):** Una medición de cortisol sin hora del día no se interpreta: el ritmo diario domina. Y un estresor crónico cambia el nivel medio de una forma distinta que uno agudo.

📘 **Dónde se aprende** (1 clase): [B105-C22 · Sistema neuroendocrino y respuesta al estrés en vuelo](../programa/clases/B105/B105-C22-sistema-neuroendocrino-y-respuesta-al-estres-en-vuelo/CLASE.md).

### Cosmovisión

- Una cosmovisión es la manera en que una sociedad entiende el mundo y su lugar en él, y la astronomía es una de las formas en que se expresa.

💡 **Cómo se explica en la clase [B02-C05](../programa/clases/B02/B02-C05-cosmovisiones-andinas-del-cielo/CLASE.md):**
- Esta relación entre cielo y ciclo biológico es un ejemplo de lo que significa una cosmovisión: el cielo y la vida están conectados en una misma explicación.
- Para Machu Picchu, un artículo propone reinterpretarlo como centro de peregrinación ligado a la cosmovisión inca, en lugar de residencia real de Pachacuti, analizando el entorno y los ciclos celestes (S4).
- 🎯 **Por qué importa:** Hablar de «astronomía andina» en singular es un error: los Andes reúnen sociedades de épocas y regiones muy distintas. La pregunta motivadora es: ¿cómo se estudia respetuosamente un cielo que otra cultura leyó de otra manera, sin imponerle nuestras categorías y sin inventar lo que las fuentes no dicen?

📘 **Dónde se aprende** (1 clase): [B02-C05 · Cosmovisiones andinas del cielo](../programa/clases/B02/B02-C05-cosmovisiones-andinas-del-cielo/CLASE.md).

### Coste

- El coste es el número de evaluaciones de la fuerza: leapfrog `1` por paso, Yoshida `3`.
- Un criterio de beneficio es mejor cuanto mayor; uno de coste es mejor cuanto menor.
- El coste se cuenta en operaciones de punto flotante por paso.

💡 **Cómo se explica en la clase [B73-C20](../programa/clases/B73/B73-C20-proyecto-de-integracion-celeste-de-precision/CLASE.md):**
- *Descripción textual:* los requisitos fijan un presupuesto frente al error de modelo; la convergencia da el paso requerido de cada integrador; el coste decide cuál usar.
- Por coste: evaluaciones para el presupuesto.
- 🎯 **Por qué importa:** Una integración «de precisión» no es la que usa el paso más pequeño sino la que mantiene el error numérico por debajo de la incertidumbre del modelo, con el menor coste. Sin ese presupuesto se gasta cómputo sin ganar exactitud o se afirma una exactitud que no existe.

📘 **Dónde se aprende** (3 clases): [B73-C20 · Proyecto de integración celeste de precisión](../programa/clases/B73/B73-C20-proyecto-de-integracion-celeste-de-precision/CLASE.md); [B74-C18 · Estimación autónoma a bordo](../programa/clases/B74/B74-C18-estimacion-autonoma-a-bordo/CLASE.md); [B95-C03 · Selección y comparación de plataformas](../programa/clases/B95/B95-C03-seleccion-y-comparacion-de-plataformas/CLASE.md).

### Coste asimétrico

- El coste asimétrico pondera más un error que el otro.

🎯 **Por qué importa (clase B119-C17):** C11 trata los límites militares del tratado; esta clase aborda cómo razonar la distinción bajo incertidumbre, un tema que ninguna clase del bloque cubre y que exige cautela jurídica. La decisión central: ¿cómo cambia el umbral de decisión cuando equivocarse en un sentido es mucho más grave que en el otro?

📘 **Dónde se aprende** (1 clase): [B119-C17 · Conflictos y normas humanitarias aplicables](../programa/clases/B119/B119-C17-conflictos-y-normas-humanitarias-aplicables/CLASE.md).

### Coste de arranque

- El coste de arranque es el tiempo de crear procesos y copiar datos.

💡 **Cómo se explica en la clase [B14-C13](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md):**
- Decisión. Para esta tarea de poco más de un segundo, no compensa; sí compensaría con trozos cien veces más largos, donde el coste de arranque es una fracción pequeña.
- 🎯 **Por qué importa:** Un análisis de miles de simulaciones tarda una noche. Tienes ocho núcleos.

📘 **Dónde se aprende** (1 clase): [B14-C13 · Computación paralela](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md).

### Coste de celda

- El coste de celda es `1 + w_s (pendiente/límite)² + w_r (rugosidad/límite)` y es infinito si se supera algún umbral.

💡 **Cómo se explica en la clase [B102-C08](../programa/clases/B102/B102-C08-traversabilidad-y-evaluacion-de-riesgo-de-terreno/CLASE.md):**
- *Descripción textual:* las elevaciones dan la pendiente y, con el plano local, la altura de obstáculo y la rugosidad; los tres forman el coste de celda y Dijkstra obtiene la ruta de mínimo coste.
- 🎯 **Por qué importa:** Elegir la ruta es elegir qué riesgo se acepta. La decisión central: ¿qué celdas son intransitables, cuánto cuesta cruzar las demás y cuánto se alarga la ruta de mínimo riesgo respecto de la recta?

📘 **Dónde se aprende** (1 clase): [B102-C08 · Traversabilidad y evaluación de riesgo de terreno](../programa/clases/B102/B102-C08-traversabilidad-y-evaluacion-de-riesgo-de-terreno/CLASE.md).

### Coste de trazado

- El coste de trazado es `Σ f·d`.

🎯 **Por qué importa (clase B109-C02):** Un buen plano ahorra pasos, separa lo sucio de lo limpio y deja las zonas tranquilas lejos de las ruidosas. La decisión central: ¿dónde pongo cada zona para que los recorridos frecuentes sean cortos y las zonas incompatibles estén lejos?

📘 **Dónde se aprende** (1 clase): [B109-C02 · Zonificación y distribución funcional de módulos de un hábitat](../programa/clases/B109/B109-C02-zonificacion-y-distribucion-funcional-de-modulos-de-un-habitat/CLASE.md).

### Costo

- El costo se mide aquí como número de comparaciones.
- El costo es `C(φ, T) = v∞,sal + v∞,lleg` en km/s.
- El costo de un par es tiempo de viaje más trabajo.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C18](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md):**
- Casos: lista vacía, un elemento, repetidos, ya ordenada (mínimo costo de inserción), inversa (máximo), y listas aleatorias contrastadas con `sorted`.
- 🎯 **Por qué importa:** Un catálogo estelar tiene millones de objetos. Buscar uno a uno es posible con diez planetas y ruinoso con diez millones.

📘 **Dónde se aprende** (4 clases): [B07-C18 · Algoritmos de búsqueda y ordenamiento](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md); [B33-C05 · Comunicación de riesgo y alertas de clima espacial](../programa/clases/B33/B33-C05-comunicacion-de-riesgo-y-alertas-de-clima-espacial/CLASE.md); [B75-C12 · Optimización de trayectoria](../programa/clases/B75/B75-C12-optimizacion-de-trayectoria/CLASE.md); [B97-C09 · Robótica colaborativa](../programa/clases/B97/B97-C09-robotica-colaborativa/CLASE.md).

### Costo cuadrático

- El costo cuadrático es `C = ∫₀^∞ (xᵀ Q x + uᵀ R u) dt` con `Q` simétrica semidefinida positiva y `R` simétrica definida positiva.

💡 **Cómo se explica en la clase [B16-C15](../programa/clases/B16/B16-C15-control-optimo-lqr/CLASE.md):**
- Es el amortiguamiento del filtro de Butterworth de segundo orden; el costo cuadrático con `Q = diag(q, 0)` lleva a él.
- Límite: el costo cuadrático penaliza mucho los picos y poco los ruidos pequeños; puede no reflejar un límite físico estricto.
- 🎯 **Por qué importa:** Con un PD hay dos perillas, `Kp` y `Kd`, y no es obvio cuánto esfuerzo gasta cada combinación. En un satélite el esfuerzo tiene un costo real: energía de las ruedas, momento almacenado, desgaste.

📘 **Dónde se aprende** (1 clase): [B16-C15 · Control óptimo LQR](../programa/clases/B16/B16-C15-control-optimo-lqr/CLASE.md).

### Costo de espera

- El costo de espera es el gasto adicional por cada año extra.

💡 **Cómo se explica en la clase [B124-C06](../programa/clases/B124/B124-C06-financiamiento-publico/CLASE.md):**
- Si cada año extra cuesta 6 % del total, el costo de espera es `6,0` uc (`6,0` % del total), un supuesto sintético.
- *Descripción textual:* cada año se gasta lo menor entre el tope y lo pendiente; lo que no se paga queda como atraso, que define el año de término y el costo de espera, y todo se comprueba con una fórmula del mínimo.
- 🎯 **Por qué importa:** Un proyecto puede estar bien estimado y aun así fallar porque el dinero no llega al ritmo que necesita. La decisión central: ¿qué tope anual evita el atraso y cuánto cuesta cada año de espera?

📘 **Dónde se aprende** (1 clase): [B124-C06 · Financiamiento público](../programa/clases/B124/B124-C06-financiamiento-publico/CLASE.md).

### Costo del operador

- El costo del operador es las primas más las pérdidas que él retiene.

💡 **Cómo se explica en la clase [B127-C08](../programa/clases/B127/B127-C08-simulacion-de-cobertura-de-seguros-para-una-mision/CLASE.md):**
- *Descripción textual:* el mismo conjunto de eventos aleatorios se aplica a cuatro estrategias que añaden coberturas de a una; para cada una se simula el costo del operador y se resumen su media, su desviación, su cuantil 99 % y la probabilidad de superar `60 MUSD`.
- 🎯 **Por qué importa:** Integrar los seguros de una misión en un caso permite practicar la decisión; no existía tal caso. La decisión central: ¿cuánto se paga de más por reducir el riesgo y qué riesgo se está dispuesto a retener?

📘 **Dónde se aprende** (1 clase): [B127-C08 · Simulación de cobertura de seguros para una misión](../programa/clases/B127/B127-C08-simulacion-de-cobertura-de-seguros-para-una-mision/CLASE.md).

### Costo esperado

- Un costo esperado pondera cada tipo de error por su costo.

💡 **Cómo se explica en la clase [B17-C12](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md):**
- Costo esperado: el que lleva a una decisión; exige conocer costos.
- 🎯 **Por qué importa:** Un modelo marca candidatos a planeta, y cada alerta cuesta horas de revisión. Si el modelo acierta el 99 % en una muestra donde el 99 % son negativos, no dice nada útil.

📘 **Dónde se aprende** (1 clase): [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md).

### Costo fijo

- El costo fijo `F` se paga siempre; el variable `v`, por producto; el escalonado `S` se suma por cada tramo de capacidad `cap`.

💡 **Cómo se explica en la clase [B124-C22](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md):**
- F["costo fijo F"] --> C["C(Q) = F + vQ + S ⌈Q/cap⌉"]
- 🎯 **Por qué importa:** B124 trata financiamiento, pero un servicio sostenible depende de un modelo de costo que explique cómo cambia el costo medio con el volumen. La decisión central: ¿a qué precio y con qué volumen el servicio cubre sus costos, y cuánto riesgo tiene si la demanda varía?

📘 **Dónde se aprende** (1 clase): [B124-C22 · Modelo de costo de un servicio de datos](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md).

### Costo más incentivo (CPIF)

- Precio fijo (FFP): el pago no depende del costo real. Costo más incentivo (CPIF): se paga el costo real más un honorario que baja cuando el costo supera el objetivo.

🎯 **Por qué importa (clase B124-C10):** El tipo de contrato reparte el riesgo de sobrecosto entre quien compra y quien vende. La decisión central: ¿cuánto riesgo asume cada parte con cada tipo de contrato y cuánto cuesta ese reparto en promedio?

📘 **Dónde se aprende** (1 clase): [B124-C10 · Contratos y compras espaciales](../programa/clases/B124/B124-C10-contratos-y-compras-espaciales/CLASE.md).

### Costo medio

- El costo medio es `C(Q)/Q`.

💡 **Cómo se explica en la clase [B124-C22](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md):**
- Con margen sobre precio de 25 %, `p = costo medio/0,75`: `78,67` um a 1 000, `37,60` a 2 500 y `23,20` a 5 000 productos.
- *Descripción textual:* los costos fijo, variable y escalonado forman el costo total, del que salen el costo medio, el precio con margen y el equilibrio; la incertidumbre de la demanda se evalúa con dos métodos.
- 🎯 **Por qué importa:** B124 trata financiamiento, pero un servicio sostenible depende de un modelo de costo que explique cómo cambia el costo medio con el volumen. La decisión central: ¿a qué precio y con qué volumen el servicio cubre sus costos, y cuánto riesgo tiene si la demanda varía?

📘 **Dónde se aprende** (1 clase): [B124-C22 · Modelo de costo de un servicio de datos](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md).

### Costo neto

- El costo neto es pérdida retenida más prima de reaseguro.

💡 **Cómo se explica en la clase [B127-C07](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md):**
- Costo neto medio: `0,70 × 67,745 + 18,00 = 65,42`.
- Costo neto medio `74,58`: cuesta `6,8 MUSD` más que no reasegurar, a cambio de desviación `76,9` y cuantil 99 % `336,8`.
- 🎯 **Por qué importa:** El riesgo espacial se reparte mediante reaseguro; no había clase al respecto. La decisión central: ¿qué parte del riesgo se cede y cuánto cuesta reducir la cola?

📘 **Dónde se aprende** (1 clase): [B127-C07 · Reaseguro espacial](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md).

### Costo nivelado (LCOP)

- El costo nivelado (LCOP) es `(CapEx·CRF + OpEx)/Q`.

💡 **Cómo se explica en la clase [B124-C24](../programa/clases/B124/B124-C24-capex-y-opex-de-una-instalacion-extraterrestre/CLASE.md):**
- *Descripción textual:* el equipo y su transporte forman el CapEx, que se convierte en anualidad y se suma al OpEx para dar el costo anual y el costo nivelado, que se verifica con valor actual y se compara con traer el producto.
- Descripción larga: el transporte domina el capital y la operación, y el costo nivelado es una pequeña fracción del de traer el producto, siempre que la producción llegue a lo planificado.
- 🎯 **Por qué importa:** B124 estima costos de misión, pero una instalación que opera años necesita separar el capital de la operación y ponerlos en una misma unidad. La decisión central: ¿a qué costo por kilogramo produce la instalación y desde qué producción conviene frente a traer el producto?

📘 **Dónde se aprende** (1 clase): [B124-C24 · CapEx y OpEx de una instalación extraterrestre](../programa/clases/B124/B124-C24-capex-y-opex-de-una-instalacion-extraterrestre/CLASE.md).

### Costo por kilogramo

- El costo por kilogramo es el precio dividido por la carga útil.

💡 **Cómo se explica en la clase [B124-C23](../programa/clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md):**
- El costo por kilogramo es el precio dividido por una fracción pequeña: cualquier mejora de la fracción mejora el costo en la misma proporción.
- *Descripción textual:* el Δv y la eficiencia dan la razón de masas de cada etapa y, con el coeficiente estructural, la fracción de carga; el producto de fracciones y el precio dan el costo por kilogramo a órbita, que se divide por la fracción de descenso para llegar a superficie.
- ⚠️ **Error frecuente:** Tomar un costo por kilogramo como un dato universal. Se corrige con la sección 10 y el ejercicio 11.
- 🎯 **Por qué importa:** El costo por kilogramo a superficie no se puede leer en una lista de precios: depende de una cadena de fracciones de masa que se multiplican. La decisión central: ¿cuánto cuesta llevar un kilogramo a la superficie, de qué depende ese costo y qué lo hace más sensible?

📘 **Dónde se aprende** (1 clase): [B124-C23 · Costos de transporte por kilogramo a superficie](../programa/clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md).

### Costo por metro

- El costo por metro es el `Δv` entre el cambio de posición.

🎯 **Por qué importa (clase B76-C11):** Una aproximación a baja velocidad no puede depender de que todos los impulsos se ejecuten. La decisión central: ¿cuántos tramos usar, cuánto cuestan y qué ocurre si el segundo impulso de un tramo falla?

📘 **Dónde se aprende** (1 clase): [B76-C11 · Operaciones de aproximación](../programa/clases/B76/B76-C11-operaciones-de-aproximacion/CLASE.md).

### Costo por suscriptor-mes

- El costo por suscriptor-mes es el costo anual repartido en suscriptores y meses.

💡 **Cómo se explica en la clase [B124-C11](../programa/clases/B124/B124-C11-sostenibilidad-economica-de-constelaciones/CLASE.md):**
- Con 100 000 suscriptores el ingreso es `60,0` Mum/año, el margen `21,100` Mum/año y el costo por suscriptor-mes `32,42` um; el despliegue se recupera en `4,27` años (sin descuento).
- 🎯 **Por qué importa:** Una constelación puede ser técnicamente exitosa y económicamente inviable si la reposición se come el margen. La decisión central: ¿cuántos suscriptores se necesitan para cubrir la reposición y la operación, y qué tan sensible es eso a la vida útil?

📘 **Dónde se aprende** (1 clase): [B124-C11 · Sostenibilidad económica de constelaciones](../programa/clases/B124/B124-C11-sostenibilidad-economica-de-constelaciones/CLASE.md).

### Costo total

- El costo total es `J = m₀ + c_t·TOF`, con `m₀` en toneladas y `c_t` en unidades por día.

💡 **Cómo se explica en la clase [B75-C27](../programa/clases/B75/B75-C27-duracion-de-mision-y-tiempo-de-vuelo-como-restriccion/CLASE.md):**
- Por costo total: con `c_t` el óptimo se desplaza.
- Con un costo temporal ilustrativo de `0,02 u/d`, el costo total mínimo (masa en toneladas + tiempo) cae en `220 d`: se paga más masa (`4,512 t` en vez de `4,189 t`) para ahorrar 40 días.
- ⚠️ **Error frecuente:** Confundir el óptimo en delta-v con el óptimo en costo total. Se corrige con 8.3.
- 🎯 **Por qué importa:** Un viaje más corto gasta más combustible y uno más largo gasta más tiempo. La decisión central: ¿qué tiempo de vuelo minimiza el costo total cuando se pesan la masa lanzada y la duración?

📘 **Dónde se aprende** (1 clase): [B75-C27 · Duración de misión y tiempo de vuelo como restricción](../programa/clases/B75/B75-C27-duracion-de-mision-y-tiempo-de-vuelo-como-restriccion/CLASE.md).

### Costos

- Los costos se reparten por igual salvo decisión distinta (art.

🎯 **Por qué importa (clase B123-C03):** Un derecho a reclamar se pierde o se debilita si no se ejerce por la vía y en el plazo previstos. La decisión central: ¿cuándo y cómo se presenta la reclamación, cuándo se puede pedir una comisión y qué valor tiene su decisión?

📘 **Dónde se aprende** (1 clase): [B123-C03 · Mecanismos de reclamación entre Estados](../programa/clases/B123/B123-C03-mecanismos-de-reclamacion-entre-estados/CLASE.md).

### Costura

- Una costura es la línea de unión entre dos teselas.

💡 **Cómo se explica en la clase [B14-C27](../programa/clases/B14/B14-C27-procesamiento-por-teselas-de-grandes-volumenes-de-imagenes/CLASE.md):**
- Un píxel junto a la costura necesita hasta 2 píxeles de la tesela vecina.
- El laboratorio comprueba que todos esos píxeles están a 2 o menos píxeles de una costura interior: el error vive en las franjas de ancho `2R` alrededor de las costuras, no en el interior de las teselas.
- 🎯 **Por qué importa:** Una cobertura global de imágenes ocupa terabytes y ningún equipo la carga entera. Para suavizarla, calcular un índice o detectar cambios hay que procesarla por pedazos.

📘 **Dónde se aprende** (1 clase): [B14-C27 · Procesamiento por teselas de grandes volúmenes de imágenes](../programa/clases/B14/B14-C27-procesamiento-por-teselas-de-grandes-volumenes-de-imagenes/CLASE.md).

### Cota

- Una cota es un valor que el resultado no debería superar (superior) o no debería bajar de él (inferior).
- Un error de redondeo es la diferencia entre el valor y su redondeo; su cota es el máximo posible: ±media unidad de la última cifra conservada (`365` → ±0,5).
- La cota es un límite superior, no una medición del valor.
- *(y 4 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B03-C11](../programa/clases/B03/B03-C11-estimacion-y-redondeo-responsable/CLASE.md):**
- D --> E["Reportar con unidad, cifras y cota"]
- Primero se estima con una cifra; luego se calcula sin redondear; se compara con la estimación; se redondea al final según la calidad de los datos; y se reporta con unidad, cifras y cota.
- 🎯 **Por qué importa:** Si te piden el tiempo que tarda la luz del Sol en llegar a la Tierra y respondes «499,004783836 s», parece muy preciso, pero tus datos (1 au y `c`) son exactos; en cambio, si respondes lo mismo para la distancia a la Luna, que varía entre unos 357 000 y 407 000 km, esas cifras serían falsas.

📘 **Dónde se aprende** (7 clases): [B03-C11 · Estimación y redondeo responsable](../programa/clases/B03/B03-C11-estimacion-y-redondeo-responsable/CLASE.md); [B03-C19 · Propagación elemental de redondeos](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md); [B27-C17 · Explosiones de rayos gamma](../programa/clases/B27/B27-C17-explosiones-de-rayos-gamma/CLASE.md); [B28-C01 · Fundamentos de mensajeros astronómicos](../programa/clases/B28/B28-C01-fundamentos-de-mensajeros-astronomicos/CLASE.md); [B53-C05 · Sistemas de coordenadas lunares](../programa/clases/B53/B53-C05-sistemas-de-coordenadas-lunares/CLASE.md); [B81-C12 · Restricciones dinámicas en optimización](../programa/clases/B81/B81-C12-restricciones-dinamicas-en-optimizacion/CLASE.md) y 1 más.

### Cota aproximada

- La cota aproximada supone `k × (celdas medias por campo)` celdas.

🎯 **Por qué importa (clase B28-C15):** Observar más campos cubre más probabilidad, pero cada campo recibe menos tiempo y es menos profundo. Si la fuente es débil, el exceso de campos hace que no se vea.

📘 **Dónde se aprende** (1 clase): [B28-C15 · Búsqueda de contrapartidas ópticas](../programa/clases/B28/B28-C15-busqueda-de-contrapartidas-opticas/CLASE.md).

### Cota de cortes mínimos

- La aproximación de evento raro suma las probabilidades de los cortes; la cota de cortes mínimos es `1 − Π(1 − P(cᵢ))`.

💡 **Cómo se explica en la clase [B83-C24](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md):**
- La enumeración exacta de los 128 estados da 0,016132; la inclusión–exclusión, 0,016132; la aproximación de evento raro, 0,016200 (un 0,42 % de más); la cota de cortes mínimos, 0,016132 (aquí coincide porque los cortes mínimos no comparten eventos);
- 🎯 **Por qué importa:** Un fallo combinado como «dos sensores fallan a la vez» no aparece en una lista de modos individuales. La decisión central: ¿qué combinaciones de fallos causan el evento no deseado, cuál es su probabilidad y qué evento básico conviene proteger primero?

📘 **Dónde se aprende** (1 clase): [B83-C24 · Árboles de fallos (FTA) y análisis de causas](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md).

### Cota de Cramér–Rao

- La matriz de información de Fisher es `F = Jᵀ J / σ²` (ruido gaussiano independiente); la cota de Cramér–Rao dice que la covarianza de cualquier estimador insesgado es al menos `F⁻¹`.
- La cota de Cramér–Rao es el límite de precisión.
- La cota de Cramér–Rao (CRB) dice que cualquier estimador sin sesgo cumple `Var(θ̂) ≥ 1/I(θ)`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C15](../programa/clases/B15/B15-C15-estimacion-de-parametros-senales-imagenes-y-estimacion-cientifica/CLASE.md):**
- *Descripción textual:* los datos con ruido alimentan un estimador; de su sesgo y su varianza sale el error cuadrático medio; la varianza de un estimador sin sesgo se compara con la cota de Cramér–Rao.
- 🎯 **Por qué importa:** Un telescopio recoge 100 fotones de una estrella y quieres su posición con la mayor exactitud posible. ¿Basta con promediar las posiciones?

📘 **Dónde se aprende** (6 clases): [B15-C15 · Estimación de parámetros — Señales, imágenes y estimación científica](../programa/clases/B15/B15-C15-estimacion-de-parametros-senales-imagenes-y-estimacion-cientifica/CLASE.md); [B22-C03 · Identificabilidad de parámetros](../programa/clases/B22/B22-C03-identificabilidad-de-parametros/CLASE.md); [B29-C16 · Supernovas y curvas de luz](../programa/clases/B29/B29-C16-supernovas-y-curvas-de-luz/CLASE.md); [B46-C18 · VLBI y geodesia](../programa/clases/B46/B46-C18-vlbi-y-geodesia/CLASE.md); [B74-C03 · Medición de alcance por radio](../programa/clases/B74/B74-C03-medicion-de-alcance-por-radio/CLASE.md); [B74-C27 · Navegación por púlsares de rayos X como técnica de investigación](../programa/clases/B74/B74-C27-navegacion-por-pulsares-de-rayos-x-como-tecnica-de-investigacion/CLASE.md).

### Cota de escape

- La cota de escape es `√(2 f ε)`.
- La cota de escape `Vₑ_max = √(2ηε)` es el escape máximo con una fuente de energía específica `ε`.

💡 **Cómo se explica en la clase [B78-C16](../programa/clases/B78/B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md):**
- *Descripción textual:* la energía por reacción y la masa de los reactivos dan la energía específica; ésta da la fracción de masa convertida y, con la fracción dirigida, la cota de escape, que se contrasta con la relativista; con una potencia dada se calcula el consumo.
- Descripción larga: la energía por kilo de la fusión supera a la química en siete órdenes de magnitud; la cota de escape sigue siendo una fracción de la velocidad de la luz.
- 🎯 **Por qué importa:** Si la energía por kilo es millones de veces mayor, el escape posible es enorme; pero eso es una cota, no un propulsor. La decisión central: ¿cuánta energía por kilo libera cada reacción y cuánto escape acotaría, según la fracción que se logre dirigir?

📘 **Dónde se aprende** (2 clases): [B78-C16 · Propulsión de fusión como investigación](../programa/clases/B78/B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md); [B78-C18 · Energía específica y limitaciones](../programa/clases/B78/B78-C18-energia-especifica-y-limitaciones/CLASE.md).

### Cota de Liu y Layland

- La cota de Liu y Layland `U ≤ n(2^(1/n) − 1)` es suficiente para RM con plazos iguales a los períodos y tiende a `ln 2 = 0,6931`.

🎯 **Por qué importa (clase B88-C06):** Elegir la política determina cuánta CPU se puede usar con garantías. La decisión central: ¿RM basta, o se necesita EDF para el conjunto de tareas?

📘 **Dónde se aprende** (1 clase): [B88-C06 · Planificación de tareas RTOS](../programa/clases/B88/B88-C06-planificacion-de-tareas-rtos/CLASE.md).

### Cota de Liu–Layland

- La cota de Liu–Layland `n(2^(1/n) − 1)` es una condición suficiente de planificabilidad con prioridades por tasa.

🎯 **Por qué importa (clase B98-C07):** Una arquitectura sin presupuesto de tiempos puede parecer correcta hasta que una tarea lenta retrasa un reflejo. La decisión central: ¿cada capa cumple sus plazos aunque las demás consuman su peor caso, y qué pasa cuando el planificador tarda más de lo previsto?

📘 **Dónde se aprende** (1 clase): [B98-C07 · Arquitectura de autonomía a bordo (percepción-decisión-acción)](../programa/clases/B98/B98-C07-arquitectura-de-autonomia-a-bordo-percepcion-decision-accion/CLASE.md).

### Cota de peor caso

- La cota de peor caso supone que todos los errores actúan en la dirección más desfavorable.
- La cota de peor caso suma los máximos: `2 + 15 + 8 = 25 µs`.

💡 **Cómo se explica en la clase [B03-C19](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md):**
- La cota de peor caso, que considera todos los redondeos en la dirección peor, es `[29,745; 30,027] km/s`; la incertidumbre en cuadratura es `0,062 km/s`.
- ⚠️ **Error frecuente:** Confundir cota de peor caso con incertidumbre estándar. Ejercicio 11.
- 🎯 **Por qué importa:** Con los datos de la Tierra redondeados a tres cifras (semieje `1,50 × 10⁸ km` y período `365 d`), la rapidez orbital sale `29,89 km/s`. La NASA publica 29,78 km/s.

📘 **Dónde se aprende** (2 clases): [B03-C19 · Propagación elemental de redondeos](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md); [B88-C26 · Latencia de interrupciones y jitter](../programa/clases/B88/B88-C26-latencia-de-interrupciones-y-jitter/CLASE.md).

### Cota de pila

- La cota de pila suma un marco por nivel de prioridad.

🎯 **Por qué importa (clase B88-C22):** Las interrupciones fijan cuánto tarda el sistema en reaccionar y cuánta pila usa. La decisión central: ¿se permite que una interrupción de mayor prioridad interrumpa a otra, y qué cuesta eso en latencia y pila?

📘 **Dónde se aprende** (1 clase): [B88-C22 · Interrupciones y manejo de excepciones en el computador de vuelo](../programa/clases/B88/B88-C22-interrupciones-y-manejo-de-excepciones-en-el-computador-de-vuelo/CLASE.md).

### Cota de sección eficaz

- La cota de sección eficaz `σ < s_up/(εΦ)`.

💡 **Cómo se explica en la clase [B31-C18](../programa/clases/B31/B31-C18-restricciones-experimentales-de-teorias/CLASE.md):**
- *Descripción textual:* las observaciones y el fondo dan el límite por cada método; el límite se convierte en cota de sección eficaz y la cobertura se verifica por Monte Carlo.
- 🎯 **Por qué importa:** Un límite mal calculado puede excluir una teoría que no estaba excluida. La decisión central: ¿qué señal máxima es compatible con lo observado y cuán fiable es el método?

📘 **Dónde se aprende** (1 clase): [B31-C18 · Restricciones experimentales de teorías](../programa/clases/B31/B31-C18-restricciones-experimentales-de-teorias/CLASE.md).

### Cota de Sellke–Bayarri–Berger

- La cota de Sellke–Bayarri–Berger acota el `BF` a favor de la alternativa con `BF ≤ 1/(−e p ln p)` para `p < 1/e`.

🎯 **Por qué importa (clase B132-C05):** El catálogo trata alineaciones sin ese contexto. La decisión central: ¿cuánto apoyo da cada línea de evidencia a la intención de una alineación, y qué parte de la conclusión depende de lo que se supone de antemano?

📘 **Dónde se aprende** (1 clase): [B132-C05 · Contexto ritual y social de la observación del cielo](../programa/clases/B132/B132-C05-contexto-ritual-y-social-de-la-observacion-del-cielo/CLASE.md).

### Cota de unión

- Matriz de confusión: frecuencia de cada clasificación por causa verdadera. Cota de unión: `1 − Σ Q(dᵢⱼ/2)`.

💡 **Cómo se explica en la clase [B96-C29](../programa/clases/B96/B96-C29-diagnostico-de-fallas-de-enlace/CLASE.md):**
- La cota de unión `1 − Σ Q(d/2)` queda por debajo de cada acierto simulado (por ejemplo, 0,8191 frente a 0,8159 en apuntamiento, dentro de 0,01).
- 🎯 **Por qué importa:** Perder tiempo de contacto buscando la causa equivocada es caro. La decisión central: ¿qué medidas distinguen las causas y cuáles se confunden entre sí?

📘 **Dónde se aprende** (1 clase): [B96-C29 · Diagnóstico de fallas de enlace](../programa/clases/B96/B96-C29-diagnostico-de-fallas-de-enlace/CLASE.md).

### Cota de Δv

- La cota de Δv es el valor al que tiende la etapa con propelente infinito.

🎯 **Por qué importa (clase B78-C02):** Más propelente da más Δv, pero cada kilo de propelente exige tanques, y esos tanques también se aceleran. La decisión central: ¿cuánto propelente hace falta para un Δv dado y existe un máximo de Δv que ninguna cantidad de propelente supera?

📘 **Dónde se aprende** (1 clase): [B78-C02 · Propulsión química como sistema físico](../programa/clases/B78/B78-C02-propulsion-quimica-como-sistema-fisico/CLASE.md).

### Cota superior

- Eficiencia de recuperación: fracción recuperada por el hisopo. Cota superior: valor que, con confianza `CL`, no es menor que la densidad verdadera.
- Una cota superior acota por arriba.

💡 **Cómo se explica en la clase [B90-C21](../programa/clases/B90/B90-C21-biocarga-de-naves-espaciales-verificacion-y-requisitos-normativos/CLASE.md):**
- *Descripción textual:* los hisopos recogen colonias; la densidad estimada es `C/(eA)` y la cota superior usa el límite de Poisson de `C`; se compara la cota con el límite.
- La densidad observada es 40 /m² y la corregida 266,7 esporas/m², bajo el límite de ejemplo de 300; pero la cota superior al 95 % es 481,2 /m²: no cumple con esa confianza.
- 🎯 **Por qué importa:** Un hisopo recoge solo una fracción de las esporas de una superficie y se cuentan pocas colonias; el resultado es una estimación con incertidumbre. La decisión central: ¿la biocarga cumple el límite con la confianza exigida o hace falta muestrear más o reducir?

📘 **Dónde se aprende** (2 clases): [B90-C21 · Biocarga de naves espaciales: verificación y requisitos normativos](../programa/clases/B90/B90-C21-biocarga-de-naves-espaciales-verificacion-y-requisitos-normativos/CLASE.md); [B119-C23 · Protección ambiental de las actividades de lanzamiento](../programa/clases/B119/B119-C23-proteccion-ambiental-de-las-actividades-de-lanzamiento/CLASE.md).

### Cota superior de confianza

- Causa raíz: origen de la falla. Cota superior de confianza: valor que, con probabilidad `CL`, no es inferior a la tasa verdadera.

🎯 **Por qué importa (clase B90-C17):** Una falla única en 500 horas de ensayo no demuestra que el equipo sea confiable: solo acota la tasa de fallas. Y una anomalía mal registrada se pierde.

📘 **Dónde se aprende** (1 clase): [B90-C17 · Gestión de anomalías de prueba](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md).

### Cotas de Voigt y Reuss

- Las cotas de Voigt y Reuss son `E_V = V_f E_f + (1 − V_f)E_m` y `E_R = 1/(V_f/E_f + (1 − V_f)/E_m)`.

🎯 **Por qué importa (clase B84-C37):** La resistencia de un compuesto cae exponencialmente con la porosidad: pasar de 10 a 25 % de huecos divide la resistencia por 2,4. La decisión central: ¿qué porosidad máxima permite cumplir una resistencia mínima y cuánto ligante hay que transportar?

📘 **Dónde se aprende** (1 clase): [B84-C37 · Compuestos y aglomerantes a base de regolito](../programa/clases/B84/B84-C37-compuestos-y-aglomerantes-a-base-de-regolito/CLASE.md).

### COTS

- El COTS (*commercial off-the-shelf*) es un componente comercial no diseñado para el espacio.

🎯 **Por qué importa (clase B95-C02):** Un componente comercial puede funcionar bien en tierra y degradarse o fallar en órbita. La decisión central: ¿qué componente comercial se puede usar en esta misión, con qué margen de radiación y con qué fiabilidad del conjunto?

📘 **Dónde se aprende** (1 clase): [B95-C02 · Componentes comerciales en vuelo: selección y riesgo](../programa/clases/B95/B95-C02-componentes-comerciales-en-vuelo-seleccion-y-riesgo/CLASE.md).

### Couette

- El flujo de Couette lo arrastra una placa; el de Poiseuille lo impulsa un gradiente de presión.

💡 **Cómo se explica en la clase [B79-C03](../programa/clases/B79/B79-C03-ecuaciones-de-navier-stokes/CLASE.md):**
- Paso 1 · Término de Couette. `0,5 × 0,2 = 0,10 m/s`.
- 🎯 **Por qué importa:** Casi todo flujo de ingeniería tiene paredes, y en ellas la viscosidad impone velocidad cero. Sin Navier–Stokes no hay arrastre ni fricción ni calentamiento por pared.

📘 **Dónde se aprende** (1 clase): [B79-C03 · Ecuaciones de Navier-Stokes](../programa/clases/B79/B79-C03-ecuaciones-de-navier-stokes/CLASE.md).

### Covalente polar

- Si los electrones se reparten de forma desigual, el enlace es covalente polar.

💡 **Cómo se explica en la clase [B06-C04](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md):**
- E -->|"Sí"| F["Covalente polar (cargas parciales)"]
- 🎯 **Por qué importa:** Las muestras del asteroide Bennu contienen amoníaco, pero en gran parte no como gas libre: los autores concluyen que la mayor parte probablemente quedó retenida como sales o ligada a minerales arcillosos y a materia orgánica, porque el amoníaco libre es muy volátil y se pierde (S1).

📘 **Dónde se aprende** (1 clase): [B06-C04 · Enlaces iónicos y covalentes](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md).

### Covarianza

- La covarianza estimada de los parámetros es `σ̂² (JᵀJ)⁻¹`.
- La covarianza `Cov(X,Y) = E[(X − E[X])(Y − E[Y])] = E[XY] − E[X]E[Y]` mide la variación conjunta; su unidad es el producto de las unidades; el GUM la define y tabula su papel en la propagación (S1, C.3.4; 5.2.2).
- Su inversa es la covarianza (cota de Cramér–Rao).
- *(y 10 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B12-C05](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md):**
- Con 1 000 000 de pares normales con `ρ = 0,8`, la correlación simulada es `0,8002` y la covarianza `9,609` (exacta `9,600`).
- La covarianza es la mitad «sin escala» de esa inclinación, y `r` la normaliza.
- ⚠️ **Error frecuente:** Sumar varianzas ignorando la covarianza. Se corrige con 8.3 y el ejercicio 2.
- 🎯 **Por qué importa:** En navegación espacial, la posición y la velocidad estimadas por un filtro no tienen errores independientes: un error de posición hacia delante suele ir acompañado de uno de velocidad. Ignorar esa relación da incertidumbres falsas, a veces demasiado optimistas y a veces demasiado pesimistas.

📘 **Dónde se aprende** (13 clases): [B11-C17 · Optimización numérica](../programa/clases/B11/B11-C17-optimizacion-numerica/CLASE.md); [B12-C05 · Covarianza y correlación](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md); [B26-C22 · Degeneraciones de parámetros cosmológicos](../programa/clases/B26/B26-C22-degeneraciones-de-parametros-cosmologicos/CLASE.md); [B29-C04 · Astrometría de exoplanetas](../programa/clases/B29/B29-C04-astrometria-de-exoplanetas/CLASE.md); [B37-C06 · Calibración de modelos estelares con el Sol y binarias](../programa/clases/B37/B37-C06-calibracion-de-modelos-estelares-con-el-sol-y-binarias/CLASE.md); [B40-C13 · Ruido, haz y covarianza instrumental en mapas del fondo](../programa/clases/B40/B40-C13-ruido-haz-y-covarianza-instrumental-en-mapas-del-fondo/CLASE.md) y 7 más.

### Covarianza cruzada

- La covarianza cruzada entre el estado actual y el ruido de proceso del intervalo es lo que las aproximaciones deben tratar.

🎯 **Por qué importa (clase B74-C24):** Una medida tardía contiene información valiosa pero tratarla mal puede dañar más que descartarla. La decisión central: ¿qué tratamiento de una medida tardía mejora el estimado sin romper la consistencia, y a qué coste?

📘 **Dónde se aprende** (1 clase): [B74-C24 · Medidas retardadas y fuera de secuencia en filtros de estimación](../programa/clases/B74/B74-C24-medidas-retardadas-y-fuera-de-secuencia-en-filtros-de-estimacion/CLASE.md).

### Covarianza de los parámetros

- La covarianza de los parámetros es `s²(XᵀX)⁻¹` (S1).

💡 **Cómo se explica en la clase [B12-C10](../programa/clases/B12/B12-C10-regresion-lineal-y-no-lineal/CLASE.md):**
- *Descripción textual:* de los datos y un modelo se minimizan los cuadrados de los residuos; se obtienen los parámetros y la varianza del ruido; con ellos, la covarianza de los parámetros; los residuos se examinan por si muestran patrón; con la covarianza se da una predicción con su incertidumbre.
- 🎯 **Por qué importa:** Casi todo en ciencias espaciales es un ajuste: la deriva de un oscilador, la curva de luz de un tránsito, la degradación de una celda solar, la relación período–luminosidad. Un ajuste sin incertidumbre de parámetros ni diagnóstico de residuos es sólo una línea dibujada.

📘 **Dónde se aprende** (1 clase): [B12-C10 · Regresión lineal y no lineal](../programa/clases/B12/B12-C10-regresion-lineal-y-no-lineal/CLASE.md).

### Covarianza de medida

- La covarianza de medida es `R` (ruido) o `H P Hᵀ` (efecto de la incertidumbre del estado).

🎯 **Por qué importa (clase B74-C01):** Todo método de B74 (mínimos cuadrados, filtros, validación) deriva del par `h` y `H = ∂h/∂x`. La decisión central: ¿qué función y qué derivadas describen la medida, y cómo sé que están bien escritas antes de dárselas a un estimador?

📘 **Dónde se aprende** (1 clase): [B74-C01 · Modelos de observación](../programa/clases/B74/B74-C01-modelos-de-observacion/CLASE.md).

### Covarianza del ruido de medida

- `Q` es la covarianza del ruido de proceso (cuánto se aparta el movimiento real del modelo) y `R` la covarianza del ruido de medida (S1).

🎯 **Por qué importa (clase B15-C17):** Un radar mide la distancia a un objeto cada segundo, con 5 m de ruido. Si solo usas la última medida, tu error es de 5 m.

📘 **Dónde se aprende** (1 clase): [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md).

### Covarianza del ruido de proceso

- `Q` es la covarianza del ruido de proceso (cuánto se aparta el movimiento real del modelo) y `R` la covarianza del ruido de medida (S1).

🎯 **Por qué importa (clase B15-C17):** Un radar mide la distancia a un objeto cada segundo, con 5 m de ruido. Si solo usas la última medida, tu error es de 5 m.

📘 **Dónde se aprende** (1 clase): [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md).

### Covarianza formal

- La covarianza formal `(JᵀWJ)⁻¹` mide la incertidumbre bajo el modelo lineal.
- La covarianza formal `P = (HᵀWH)⁻¹` supone modelo lineal y ruido bien descrito.

💡 **Cómo se explica en la clase [B74-C07](../programa/clases/B74/B74-C07-ajuste-por-minimos-cuadrados/CLASE.md):**
- La covarianza formal da `σ = (1,848, 17,342, 12,628) m` y `(0,00470, 0,01652, 0,00815) m/s`; el error real queda dentro de unos pocos sigma.
- Con 100 realizaciones de ruido, el cociente entre la dispersión empírica y la formal está entre `0,923` y `1,100`: la covarianza formal describe bien la dispersión en este problema casi lineal.
- ⚠️ **Error frecuente:** Usar la covarianza formal sin comprobarla. Contrástala con Monte Carlo o con `χ²`, como en 8.3–8.4.
- 🎯 **Por qué importa:** Un estado sin covarianza es un número sin garantía. La decisión central: ¿cuál es el estado que mejor explica las observaciones, qué incertidumbre tiene y cómo compruebo que esa incertidumbre es honesta?

📘 **Dónde se aprende** (2 clases): [B58-C07 · Determinación de órbitas](../programa/clases/B58/B58-C07-determinacion-de-orbitas/CLASE.md); [B74-C07 · Ajuste por mínimos cuadrados](../programa/clases/B74/B74-C07-ajuste-por-minimos-cuadrados/CLASE.md).

### CPI

- El CPI es `EV/AC`; el SPI, `EV/PV`.

💡 **Cómo se explica en la clase [B124-C15](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md):**
- `CPI = 0,7950` (se gasta más de lo que se gana) y `SPI = 0,8368` (hay atraso).
- Si el rendimiento de costo se mantiene, `EAC = BAC/CPI = 100,63` Mum (ETC `40,63`, VAC `-20,63`), idéntico a `AC + (BAC − EV)/CPI` (error `0,0e+00`).
- ⚠️ **Error frecuente:** Confundir gastar con avanzar. Se corrige con 8.2: el CPI compara lo ganado con lo gastado.
- 🎯 **Por qué importa:** Un proyecto se descontrola de a poco; el valor ganado convierte «vamos bien» en números comparables. La decisión central: ¿cuánto va a costar el proyecto al terminar si el rendimiento actual se mantiene y qué paquete es el problema?

📘 **Dónde se aprende** (1 clase): [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### CR3BP

- El CR3BP estudia una masa despreciable bajo la gravedad de dos cuerpos masivos en órbita circular mutua.

🎯 **Por qué importa (clase B73-C01):** Con tres cuerpos no hay solución cerrada, pero sí una cantidad conservada que organiza todo lo demás: puntos de equilibrio, regiones prohibidas y transferencias de bajo costo. La decisión central: ¿cuándo basta el modelo de tres cuerpos restringido, y cómo sé que mi integración no inventa dinámica?

📘 **Dónde se aprende** (1 clase): [B73-C01 · Problema restringido de tres cuerpos](../programa/clases/B73/B73-C01-problema-restringido-de-tres-cuerpos/CLASE.md).

### Crank–Nicolson

- La fotoevaporación es la pérdida de gas calentado por radiación. Crank–Nicolson es un esquema implícito de segundo orden.
- La fracción termalizada `η` es la parte que se convierte en calor. Crank–Nicolson es un esquema implícito de segundo orden.
- El esquema Crank–Nicolson avanza en el tiempo promediando la derivada al inicio y al final del paso (orden 2).

💡 **Cómo se explica en la clase [B23-C04](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md):**
- El error total tiene una parte espacial (`∝ Δz²`) y otra temporal (`∝ Δt²` en Crank–Nicolson).
- La diferencia con Crank–Nicolson (2000 pasos) es `5,8 × 10⁻⁷ K`: es el error temporal de Crank–Nicolson.
- 🎯 **Por qué importa:** Un modelo de conducción de calor en el regolito, con una fuente variable y una condición de flujo en el borde, no tiene solución cerrada. Pero su código puede estar mal en la frontera, en el término fuente o en el tiempo, y ninguna propiedad global lo delata fácilmente.

📘 **Dónde se aprende** (3 clases): [B23-C04 · Soluciones de referencia y manufactured solutions](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md); [B52-C09 · Dispersión de discos de gas](../programa/clases/B52/B52-C09-dispersion-de-discos-de-gas/CLASE.md); [B52-C17 · Colisiones y evolución térmica](../programa/clases/B52/B52-C17-colisiones-y-evolucion-termica/CLASE.md).

### Cráter aparente

- Un cráter aparente es el visible hoy.

💡 **Cómo se explica en la clase [B61-C02](../programa/clases/B61/B61-C02-crateres-simples-morfologia-y-formacion/CLASE.md):**
- Con `d/D` = 0,2, un cráter aparente de 1000 m tiene 200 m de profundidad y un volumen de 8,27×10⁷ m³; su radio de curvatura vale 1,45 `R`.
- 🎯 **Por qué importa:** Medir un cráter es medir un bol, pero lo que se ve es el bol después de colapsar y rellenarse. La decisión central: ¿cuánto volumen tenía la cavidad original y cuánto se perdió en el relleno de brecha?

📘 **Dónde se aprende** (1 clase): [B61-C02 · Cráteres simples: morfología y formación](../programa/clases/B61/B61-C02-crateres-simples-morfologia-y-formacion/CLASE.md).

### Cráter simple

- El cráter simple conserva forma de cuenco.

🎯 **Por qué importa (clase B58-C15):** Para decidir si una desviación es necesaria hay que saber qué haría el impacto. La decisión central: ¿cómo escalan la energía y el cráter con el tamaño, la velocidad y el ángulo?

📘 **Dónde se aprende** (1 clase): [B58-C15 · Modelos de impacto planetario](../programa/clases/B58/B58-C15-modelos-de-impacto-planetario/CLASE.md).

### Cráter transitorio

- El cráter transitorio es la cavidad máxima antes del colapso.

💡 **Cómo se explica en la clase [B58-C15](../programa/clases/B58/B58-C15-modelos-de-impacto-planetario/CLASE.md):**
- Con `v = 30 km/s` y la misma energía (`6756 Mt`), el cuerpo mediría `359 m` y el cráter transitorio sería `5.82 km`: la energía no basta, importan el tamaño y la velocidad por separado.
- El escalamiento recordado da un cráter transitorio de `6.01 km` y uno final simple de `7.51 km`.
- 🎯 **Por qué importa:** Para decidir si una desviación es necesaria hay que saber qué haría el impacto. La decisión central: ¿cómo escalan la energía y el cráter con el tamaño, la velocidad y el ángulo?

📘 **Dónde se aprende** (2 clases): [B58-C15 · Modelos de impacto planetario](../programa/clases/B58/B58-C15-modelos-de-impacto-planetario/CLASE.md); [B61-C01 · Dinámica de eyección y escalado de cráteres](../programa/clases/B61/B61-C01-dinamica-de-eyeccion-y-escalado-de-crateres/CLASE.md).

### CRC

- Prueba de extremo a extremo: prueba de un hilo operativo completo entre elementos e interfaces externas. CRC: código de redundancia cíclica.

💡 **Cómo se explica en la clase [B90-C16](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md):**
- CCSDS publica protocolos de datos espaciales, pero sus recomendaciones no se consultaron; el CRC-16/CCITT-FALSE (polinomio 0x1021, valor inicial 0xFFFF) y su valor de comprobación 0x29B1 son datos de uso general no consultados en una fuente concreta.
- El laboratorio calcula `CRC("123456789") = 0x29B1`, igual al valor de comprobación.
- 🎯 **Por qué importa:** Cada subsistema puede pasar sus pruebas y la cadena fallar: un formato de trama distinto, un retraso mayor que el tiempo de espera, un error de bit no detectado. La decisión central: ¿qué errores detecta la cadena, con qué frecuencia reintenta y cuánto tarda cada acuse?

📘 **Dónde se aprende** (1 clase): [B90-C16 · Pruebas de extremo a extremo](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md).

### CRC-15

- El CRC-15 usa el polinomio `0x4599`.

🎯 **Por qué importa (clase B88-C07):** El bus fija cuánta telemetría y cuántos comandos caben y con qué retardo. La decisión central: ¿cuál es el caudal útil y el peor tiempo de trama de cada bus para mi carga?

📘 **Dónde se aprende** (1 clase): [B88-C07 · Buses I2C SPI CAN y SpaceWire](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md).

### CRC-16

- El CRC-16 con polinomio `0x1021` e inicio `0xFFFF` da `0x29B1` para la cadena `123456789`.
- El CRC-16 valida el registro.
- El CRC-16 usa el polinomio `x¹⁶ + x¹² + x⁵ + 1` (0x1021).

💡 **Cómo se explica en la clase [B88-C08](../programa/clases/B88/B88-C08-telemetria-interna/CLASE.md):**
- El CRC-16 de `123456789` es `0x29B1` (valor de comprobación del propio laboratorio).
- Con CRC-16, un error de un byte (ráfaga ≤ 16 bits) siempre se detecta; esto lo comprueba el laboratorio, no una norma.
- 🎯 **Por qué importa:** Sin telemetría no se ve la salud de la nave; con demasiada, se satura el enlace. La decisión central: ¿qué parámetros, a qué frecuencia y con qué protección caben en el enlace sin perder los críticos?

📘 **Dónde se aprende** (3 clases): [B88-C08 · Telemetría interna](../programa/clases/B88/B88-C08-telemetria-interna/CLASE.md); [B88-C35 · Reinicio en caliente y persistencia de estado](../programa/clases/B88/B88-C35-reinicio-en-caliente-y-persistencia-de-estado/CLASE.md); [B89-C12 · Telecomandos CCSDS](../programa/clases/B89/B89-C12-telecomandos-ccsds/CLASE.md).

### CRC-32

- SHA-256: hash criptográfico de 256 bits. CRC-32: código cíclico de 32 bits.

💡 **Cómo se explica en la clase [B48-C17](../programa/clases/B48/B48-C17-gestion-de-archivos-observacionales/CLASE.md):**
- El CRC-32 detecta con seguridad cualquier cambio de un bit, pero no protege de una alteración deliberada; para eso se usa SHA-256.
- El SHA-256 de «abc» es ba7816bf8f01cfea…, y el CRC-32 de «123456789» es 0xcbf43926.
- 🎯 **Por qué importa:** Un archivo que se corrompe en silencio contamina todos los análisis posteriores. La decisión central: ¿qué suma de verificación y con cuántos bits detecta la corrupción?

📘 **Dónde se aprende** (1 clase): [B48-C17 · Gestión de archivos observacionales](../programa/clases/B48/B48-C17-gestion-de-archivos-observacionales/CLASE.md).

### CRC-8

- El CRC-8 con polinomio `0x07` da `0xF4` para `123456789`.

🎯 **Por qué importa (clase B88-C09):** Un telecomando aceptado en el estado equivocado puede dañar la nave; uno rechazado en el estado correcto puede perderla. La decisión central: ¿qué comando es válido en cada modo y qué comprobaciones lo protegen?

📘 **Dónde se aprende** (1 clase): [B88-C09 · Telecomandos y estados de misión](../programa/clases/B88/B88-C09-telecomandos-y-estados-de-mision/CLASE.md).

### Creciente

- Una función es creciente si, al aumentar `x`, `f(x)` no disminuye.
- El ángulo de fase `i` es el ángulo Sol–Luna–Tierra visto desde la Luna. Creciente es el tramo de Luna nueva a llena;

💡 **Cómo se explica en la clase [B04-C04](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md):**
- Comprueba: la función creciente da `P(292) ≈ 996 d`, coherente con redondeo.
- 🎯 **Por qué importa:** Un astrónomo no solo calcula un valor: pregunta «¿qué pasa con el periodo de un planeta si su órbita es el doble de grande?». Responderlo con un solo caso no basta; hace falta la regla que liga ambas magnitudes.

📘 **Dónde se aprende** (2 clases): [B04-C04 · Funciones y gráficas](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md); [B08-C08 · Fases lunares y libración](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md).

### Crecimiento aditivo

- El crecimiento aditivo añade módulos sin retirar los existentes.

🎯 **Por qué importa (clase B109-C05):** Si el primer módulo no admite ampliación, crecer obliga a desechar lo construido. La decisión central: ¿qué funciones se duplican con la tripulación, cuáles no, y cómo se añaden módulos sin rediseñar?

📘 **Dónde se aprende** (1 clase): [B109-C05 · Crecimiento modular y escalabilidad de asentamientos](../programa/clases/B109/B109-C05-crecimiento-modular-y-escalabilidad-de-asentamientos/CLASE.md).

### Crecimiento del núcleo

- El crecimiento del núcleo es `dM_c/dt = L/(X ε c²)` si toda la luminosidad viene de la capa.

🎯 **Por qué importa (clase B24-C16):** Una gigante roja es mucho mayor y más luminosa que su estrella original y tiene una densidad media ínfima. Entender su tamaño, su gravedad y cómo crece su núcleo permite interpretar las gigantes observadas, usarlas como sondas asterosísmicas y anticipar el destino del Sol.

📘 **Dónde se aprende** (1 clase): [B24-C16 · Gigantes rojas](../programa/clases/B24/B24-C16-gigantes-rojas/CLASE.md).

### Crecimiento descontrolado

- El crecimiento descontrolado (*runaway*) es el régimen en que el cuerpo más masivo crece más rápido en términos relativos.

🎯 **Por qué importa (clase B52-C05):** El tiempo de crecimiento decide si un núcleo existe antes de que el gas se disipe. La decisión central: ¿cómo cambia la tasa de acreción con la masa y cuándo se detiene?

📘 **Dónde se aprende** (1 clase): [B52-C05 · Crecimiento de embriones planetarios](../programa/clases/B52/B52-C05-crecimiento-de-embriones-planetarios/CLASE.md).

### Crecimiento lineal

- El crecimiento lineal `D(a)` describe cómo `δ` crece mientras `δ ≪ 1`.

🎯 **Por qué importa (clase B26-C17):** Los grandes sondeos de galaxias miden cómo se agrupan, y de su agrupamiento salen la densidad de materia y la historia de la expansión. Para interpretarlos hace falta saber cómo crece una fluctuación y qué distancia angular corresponde a una escala física.

📘 **Dónde se aprende** (1 clase): [B26-C17 · Estructura cosmológica](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md).

### Crecimiento logístico

- Confianza: probabilidad de detectar. Crecimiento logístico: curva en S.

🎯 **Por qué importa (clase B106-C28):** Una muestra pequeña puede no contener ningún organismo de una contaminación real, y un muestreo espaciado deja crecer la población. La decisión central: ¿qué volumen y qué intervalo de muestreo dan una confianza dada de detectar una contaminación antes de que supere el umbral de acción?

📘 **Dónde se aprende** (1 clase): [B106-C28 · Monitoreo microbiológico de agua y superficies del hábitat](../programa/clases/B106/B106-C28-monitoreo-microbiologico-de-agua-y-superficies-del-habitat/CLASE.md).

### Crecimiento, mantenimiento y supervivencia

- Un tiempo de renovación es lo que tarda en renovarse una unidad de carbono celular. Crecimiento, mantenimiento y supervivencia son tres regímenes de actividad.

💡 **Cómo se explica en la clase [B64-C03](../programa/clases/B64/B64-C03-psicrofilos-y-vida-en-frio/CLASE.md):**
- Price y Sowers [S1] compararon tasas metabólicas de microbios en muchos ambientes fríos y no hallaron una temperatura mínima de metabolismo; según su resumen, crecimiento, mantenimiento y supervivencia siguen una misma energía de activación de unos 110 kJ y se escalan aproximadamente como 10⁶ : 10³ : 1.
- 🎯 **Por qué importa:** El frío no detiene la vida de golpe: la ralentiza. La pregunta motivadora: ¿cuánto más lento es el metabolismo a −40 °C que a 25 °C, y qué significa «vivir» a esa velocidad?

📘 **Dónde se aprende** (1 clase): [B64-C03 · Psicrófilos y vida en frío](../programa/clases/B64/B64-C03-psicrofilos-y-vida-en-frio/CLASE.md).

### Crecimiento por madurez

- El crecimiento por madurez es la reserva de cada equipo según lo conocido que sea (comercial, modificado, nuevo).

💡 **Cómo se explica en la clase [B86-C19](../programa/clases/B86/B86-C19-presupuesto-de-potencia-de-mision/CLASE.md):**
- S["subsistemas y modos"] --> M["crecimiento por madurez"]
- *Descripción textual:* los subsistemas, con su crecimiento por madurez y la reserva de sistema, dan la demanda por fase y la potencia de ala requerida; con la generación de cada fase resultan los márgenes y la fase crítica; un Monte Carlo del crecimiento estima la probabilidad de exceso.
- 🎯 **Por qué importa:** Un presupuesto es un compromiso de ingeniería: cada subsistema promete una potencia que todavía puede crecer. Las reservas por madurez evitan que el ala quede corta cuando una carga nueva consume más de lo previsto.

📘 **Dónde se aprende** (1 clase): [B86-C19 · Presupuesto de potencia de misión](../programa/clases/B86/B86-C19-presupuesto-de-potencia-de-mision/CLASE.md).

### Crecimiento secular

- El crecimiento secular es el que aumenta con `t`.

🎯 **Por qué importa (clase B72-C19):** Las incertidumbres de la órbita inicial y de los parámetros determinan cuánto tiempo vale una predicción. La decisión central: ¿cómo crece con el tiempo el error de posición por cada fuente de incertidumbre y cuál de ellas manda?

📘 **Dónde se aprende** (1 clase): [B72-C19 · Análisis de sensibilidad orbital](../programa/clases/B72/B72-C19-analisis-de-sensibilidad-orbital/CLASE.md).

### Crédito

- Un crédito nombra al autor, enlaza la fuente y la licencia, e indica si hubo cambios.

💡 **Cómo se explica en la clase [B130-C01](../programa/clases/B130/B130-C01-infografias-con-fuentes-verificables/CLASE.md):**
- ESO publica sus imágenes bajo CC BY 4.0 y pide un crédito completo y visible, con enlace en línea, e indicar si se modificó el material, también si se usó IA.
- *Descripción textual:* cada dato pasa por una ficha; si la auditoría la encuentra completa se dibuja con una escala honesta y su crédito; si no, se corrige o se rotula como ilustrativo.
- 🎯 **Por qué importa:** Comunicar con imágenes exige mantener la fuente y la incertidumbre; la clase de comunicación general no entra en cómo se audita una pieza visual. La decisión central: ¿qué debe llevar cada cifra de una infografía para que otra persona pueda verificarla, y qué diseño la deforma?

📘 **Dónde se aprende** (1 clase): [B130-C01 · Infografías con fuentes verificables](../programa/clases/B130/B130-C01-infografias-con-fuentes-verificables/CLASE.md).

### Crédito de servicio

- El crédito de servicio compensa al cliente.

🎯 **Por qué importa (clase B124-C21):** B124 trata propuestas de valor, pero un servicio de observación se compromete con plazos y calidad, y esos compromisos tienen una aritmética precisa. La decisión central: ¿qué disponibilidad y qué plazo puede prometer un servicio sin incumplir seguido y cuánto cuesta cada incumplimiento?

📘 **Dónde se aprende** (1 clase): [B124-C21 · Acuerdos de nivel de servicio para productos de datos](../programa/clases/B124/B124-C21-acuerdos-de-nivel-de-servicio-para-productos-de-datos/CLASE.md).

### Cribado

- El cribado es la aplicación de esos criterios, primero al título y resumen y luego al texto completo.
- El cribado es el filtro rápido previo al cálculo fino.
- El cribado descarta pares.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B20-C01](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md):**
- Paso 5 · Cribado. Fuera de periodo: `a6` (2012), `a15` (2014), `a16` (2013).
- 🎯 **Por qué importa:** Cuando alguien afirma «no hay estudios sobre esto» o «es sabido que…», la frase vale tanto como el procedimiento con que se buscó. Dos personas que buscan lo mismo sin anotar cómo lo hicieron obtendrán listas distintas y no podrán explicar por qué.

📘 **Dónde se aprende** (4 clases): [B20-C01 · Búsqueda bibliográfica sistemática y gestión de referencias](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md); [B118-C15 · Seguimiento de mega constelaciones](../programa/clases/B118/B118-C15-seguimiento-de-mega-constelaciones/CLASE.md); [B118-C18 · Gestión del tráfico espacial](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md); [B119-C13 · Vigilancia y conciencia situacional espacial](../programa/clases/B119/B119-C13-vigilancia-y-conciencia-situacional-espacial/CLASE.md).

### Crimen inverso

- Si son el mismo, hay crimen inverso.

💡 **Cómo se explica en la clase [B22-C05](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md):**
- Wirgin define el crimen inverso como usar los mismos componentes teóricos, o casi los mismos, para generar los datos y para invertirlos en un problema inverso, y recuerda que Colton y Kress lo consideran una práctica trivial que debe evitarse (S3).
- 🎯 **Por qué importa:** Con datos reales no conoces la verdad, así que no puedes medir el error de tu inversión. Con datos sintéticos sí: tú fijas la verdad, generas los datos y miras si el método la recupera.

📘 **Dónde se aprende** (1 clase): [B22-C05 · Pruebas de inversión con datos sintéticos](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md).

### Criógeno

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C13](../programa/clases/B47/B47-C13-criogenia-instrumental/CLASE.md):**
- *Descripción textual:* la radiación entre escudos y la conducción por soportes suman una carga que consume el criógeno.
- Con emisividad `0,02`, área `0,2 m²`, 4 soportes y 50 kg de criógeno (ilustrativos), la carga parásita baja de `818,2 mW` sin escudos a `28,0 mW` con 40 escudos, y la vida pasa de `0,040` a `1,182 años`.
- 🎯 **Por qué importa:** Cada vatio parásito acorta la vida de un criógeno. La decisión central: ¿cuántos escudos y qué soportes bastan para una vida útil dada?

📘 **Dónde se aprende** (1 clase): [B47-C13 · Criogenia instrumental](../programa/clases/B47/B47-C13-criogenia-instrumental/CLASE.md).

### Criomagma

- El criomagma es el material líquido o semilíquido que sube.

🎯 **Por qué importa (clase B70-C06):** El agua líquida es más densa que el hielo, así que no sube sola. La decisión central: ¿qué presión extra y qué mecanismo hacen falta para que el agua llegue a la superficie?

📘 **Dónde se aprende** (1 clase): [B70-C06 · Criovulcanismo: lavas heladas y emisión de volátiles](../programa/clases/B70/B70-C06-criovulcanismo-lavas-heladas-y-emision-de-volatiles/CLASE.md).

### Criovulcanismo

- El criovulcanismo es la erupción de volátiles helados o agua en lugar de silicatos.

🎯 **Por qué importa (clase B70-C06):** El agua líquida es más densa que el hielo, así que no sube sola. La decisión central: ¿qué presión extra y qué mecanismo hacen falta para que el agua llegue a la superficie?

📘 **Dónde se aprende** (1 clase): [B70-C06 · Criovulcanismo: lavas heladas y emisión de volátiles](../programa/clases/B70/B70-C06-criovulcanismo-lavas-heladas-y-emision-de-volatiles/CLASE.md).

### Criterio

- Un criterio es una propiedad que se compara (reserva, pendiente, iluminación, riesgo).
- El criterio es el nivel de desempeño exigido.
- Un criterio es un aspecto de comparación.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B67-C01](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md):**
- Para un criterio donde más es mejor, `z = (x − mín)/(máx − mín)`; donde menos es mejor, `z = 1 − (x − mín)/(máx − mín)`.
- Límite: los criterios se suponen independientes y los puntajes lineales; un sitio con un valor inaceptable en un criterio (por ejemplo, riesgo extremo) puede requerir una regla de exclusión y no un promedio.
- 🎯 **Por qué importa:** Elegir con una sola cifra (la reserva) lleva a sitios que no se pueden explotar; elegir con una suma de unidades distintas es un error. La decisión central: ¿cuál sitio conviene, y cuánto de esa respuesta depende de los pesos que fija quien decide?

📘 **Dónde se aprende** (6 clases): [B43-C20 · Proyecto mecánico completo de telescopio](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md); [B67-C01 · Selección de sitios de extracción con criterios múltiples](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md); [B83-C13 · Revisiones SRR y PDR](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md); [B104-C09 · Entrenamiento en simuladores](../programa/clases/B104/B104-C09-entrenamiento-en-simuladores/CLASE.md); [B124-C04 · Diseño de propuesta de valor](../programa/clases/B124/B124-C04-diseno-de-propuesta-de-valor/CLASE.md); [B128-C11 · Auditoría de accesibilidad de un recurso educativo](../programa/clases/B128/B128-C11-auditoria-de-accesibilidad-de-un-recurso-educativo/CLASE.md).

### Criterio de aceptación

- El criterio de aceptación es la regla de decisión fijada de antemano: aquí, `z ≤ 2` en todos los blancos.
- El criterio de aceptación es una condición medible (p. ej. «error ≤ 10⁻³ au a 91 d») fijada antes de comparar.
- Un criterio de aceptación es una condición medible con umbral.

🎯 **Por qué importa (clase B13-C20):** Un telémetro calibrado, con presupuesto y registro, puede seguir fallando: un error de escala oculto que la calibración en una sola distancia no ve.

📘 **Dónde se aprende** (3 clases): [B13-C20 · Validación de una cadena de medida](../programa/clases/B13/B13-C20-validacion-de-una-cadena-de-medida/CLASE.md); [B23-C05 · Validación con conjuntos oficiales](../programa/clases/B23/B23-C05-validacion-con-conjuntos-oficiales/CLASE.md); [B23-C08 · Informe de verificación y validación](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md).

### Criterio de beneficio

- Un criterio de beneficio es mejor cuanto mayor; uno de coste es mejor cuanto menor.

🎯 **Por qué importa (clase B95-C03):** Elegir una plataforma «porque la conocemos» no se puede defender. La decisión central: ¿qué plataforma cumple lo imprescindible, cuál puntúa mejor y cuánto depende ese resultado de los pesos que elegimos?

📘 **Dónde se aprende** (1 clase): [B95-C03 · Selección y comparación de plataformas](../programa/clases/B95/B95-C03-seleccion-y-comparacion-de-plataformas/CLASE.md).

### Criterio de comparación

- Un criterio de comparación es la regla que decide qué modelo describe mejor los datos.

💡 **Cómo se explica en la clase [B01-C17](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md):**
- Ese es el criterio de comparación: el que deje menor residuo en escala logarítmica, declarado antes de calcular.
- 🎯 **Por qué importa:** Al final de C13, la tercera ley de Kepler daba `T²/a³ = 1` para siete planetas con error menor al 1,5 %, y 0,975 para Neptuno. ¿Falla el modelo con Neptuno?

📘 **Dónde se aprende** (1 clase): [B01-C17 · Construcción de modelos científicos](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md).

### Criterio de comprobación

- Un criterio de comprobación es una prueba objetiva que dice si el requisito se cumple.
- Un requisito es una condición que la campaña debe cumplir; debe ser verificable: tener un criterio de comprobación (un número o un sí/no) y un método de comprobación.

🎯 **Por qué importa (clase B03-C20):** Un ingeniero no recibe un ejercicio con una sola fórmula: recibe requisitos («que quepa en un patio de 350 m», «que se vea el Sol», «que Neptuno esté a su sitio») y debe decidir qué se puede cumplir y qué no.

📘 **Dónde se aprende** (2 clases): [B03-C20 · Problema integrado de escala del sistema solar](../programa/clases/B03/B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md); [B08-C20 · Proyecto de campaña de observación nocturna](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md).

### Criterio de correlación

- El criterio de correlación (aquí `|ΔT| ≤ 3 K`, ilustrativo) acepta o rechaza el modelo.

🎯 **Por qué importa (clase B85-C27):** Un modelo sin correlación no sirve para predecir y un margen sin incertidumbre es una apuesta. La decisión central: ¿el modelo reproduce el ensayo dentro del criterio y cuánto margen queda tras la incertidumbre?

📘 **Dónde se aprende** (1 clase): [B85-C27 · Márgenes y correlación térmica](../programa/clases/B85/B85-C27-margenes-y-correlacion-termica/CLASE.md).

### Criterio de daño

- El criterio de daño compara la interferencia con el ruido.

🎯 **Por qué importa (clase B118-C17):** La radioastronomía opera en bandas donde la ITU asigna protección, pero las constelaciones numerosas y sus emisiones no deseadas pueden degradar la sensibilidad. La decisión central: ¿cuánto debe bajar una emisión para quedar por debajo del umbral de daño y de qué depende ese umbral?

📘 **Dónde se aprende** (1 clase): [B118-C17 · Interferencia radioastronómica](../programa/clases/B118/B118-C17-interferencia-radioastronomica/CLASE.md).

### Criterio de detección

- El objetivo científico y el criterio de detección (5σ).

🎯 **Por qué importa (clase B46-C20):** Un proyecto viable cuadra objetivo, sensibilidad, tiempo y datos. La decisión central: ¿cuánto tiempo de observación pide el objetivo y con qué margen?

📘 **Dónde se aprende** (1 clase): [B46-C20 · Proyecto de observación radioastronómica](../programa/clases/B46/B46-C20-proyecto-de-observacion-radioastronomica/CLASE.md).

### Criterio de éxito

- El criterio de éxito combina condiciones (agua y ciencia).

💡 **Cómo se explica en la clase [B104-C20](../programa/clases/B104/B104-C20-mision-tripulada-simulada/CLASE.md):**
- *Descripción textual:* la tasa de fallas determina cuántas ocurren; cada una consume horas y agua; junto con el consumo variable, determinan si se cumple el criterio de éxito.
- 🎯 **Por qué importa:** Cada margen parece suficiente por separado, pero las fallas consumen a la vez agua y tiempo. La decisión central: ¿hasta qué tasa de fallas mantiene la misión una probabilidad de éxito alta, y cuál recurso se agota primero?

📘 **Dónde se aprende** (1 clase): [B104-C20 · Misión tripulada simulada](../programa/clases/B104/B104-C20-mision-tripulada-simulada/CLASE.md).

### Criterio de Gladman

- El criterio de Gladman para dos planetas en órbitas circulares es `Δ > 2√3 ≈ 3,46`.

💡 **Cómo se explica en la clase [B73-C17](../programa/clases/B73/B73-C17-estabilidad-de-sistemas-exoplanetarios/CLASE.md):**
- El criterio de Gladman no se consultó en su fuente y solo se contrasta numéricamente.
- 🎯 **Por qué importa:** Muchos sistemas exoplanetarios son compactos y su existencia depende de no haberse desestabilizado. Un criterio simple de separación permite descartar configuraciones inviables antes de integrar.

📘 **Dónde se aprende** (1 clase): [B73-C17 · Estabilidad de sistemas exoplanetarios](../programa/clases/B73/B73-C17-estabilidad-de-sistemas-exoplanetarios/CLASE.md).

### Criterio de Hill

- El criterio de Hill pide que el radio de la partícula iguale su esfera de Hill: `1,442 R (ρ_M/ρ_m)^{1/3}`.

💡 **Cómo se explica en la clase [B73-C16](../programa/clases/B73/B73-C16-dinamica-de-anillos/CLASE.md):**
- El criterio de Hill cae entre los dos límites, como debe.
- 🎯 **Por qué importa:** Un anillo existe donde las mareas impiden que las partículas se junten, se ensancha por viscosidad y se estructura por resonancias con las lunas. La decisión central: ¿qué escalas fijan dónde hay un anillo, cuánto dura y dónde lo moldean las lunas?

📘 **Dónde se aprende** (1 clase): [B73-C16 · Dinámica de anillos](../programa/clases/B73/B73-C16-dinamica-de-anillos/CLASE.md).

### Criterio de Hillas

- El criterio de Hillas limita `E_max` por el tamaño y el campo de la fuente.
- El criterio de Hillas limita la energía por el tamaño y el campo.

🎯 **Por qué importa (clase B28-C04):** El origen de los rayos cósmicos de mayor energía sigue abierto; el criterio de Hillas descarta fuentes y la anisotropía apunta a regiones. La decisión central: ¿qué fuentes pueden alcanzar una energía dada y qué anisotropía se puede detectar con un número dado de eventos?

📘 **Dónde se aprende** (2 clases): [B28-C04 · Rayos cósmicos de alta energía](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md); [B31-C16 · Astropartículas de alta energía](../programa/clases/B31/B31-C16-astroparticulas-de-alta-energia/CLASE.md).

### Criterio de información de Akaike

- El criterio de información de Akaike es `AIC = 2k − 2 ln L_max`, con `k` parámetros; el bayesiano es `BIC = k ln n − 2 ln L_max`, con `n` datos.
- El criterio de información de Akaike (AIC) penaliza los parámetros: `n ln(RSS/n) + 2k`.

🎯 **Por qué importa (clase B12-C22):** Un modelo más flexible siempre ajusta mejor los datos que uno más sencillo, así que el ajuste solo no sirve para elegir. Hace falta penalizar la complejidad: ¿vale la pena el parámetro extra?

📘 **Dónde se aprende** (2 clases): [B12-C22 · Comparación de modelos: evidencia bayesiana y criterios de información](../programa/clases/B12/B12-C22-comparacion-de-modelos-evidencia-bayesiana-y-criterios-de-informacion/CLASE.md); [B15-C21 · Series temporales multivariadas y regresión dinámica](../programa/clases/B15/B15-C21-series-temporales-multivariadas-y-regresion-dinamica/CLASE.md).

### Criterio de ligada

- El criterio de ligada de este laboratorio: la distancia a la Luna no supera `R_H` en 30 d.

🎯 **Por qué importa (clase B76-C03):** Un orbitador lunar bajo y un satélite de relevo alto obedecen leyes distintas. La decisión central: ¿hasta qué distancia de la Luna puede mantenerse una órbita casi circular y qué sentido de giro resiste mejor la perturbación terrestre?

📘 **Dónde se aprende** (1 clase): [B76-C03 · Órbitas alrededor de la Luna](../programa/clases/B76/B76-C03-orbitas-alrededor-de-la-luna/CLASE.md).

### Criterio de muestreo

- El criterio de muestreo usado aquí (supuesto del ejemplo) pide al menos dos píxeles por rasgo: `GSD ≤ rasgo/2`.

🎯 **Por qué importa (clase B83-C01):** Un equipo sabe que quiere «mirar la costa» pero no cuánto debe resolver ni qué objetivo merece el presupuesto. La decisión central: ¿qué requisito de medición se deduce de la pregunta científica y qué objetivo conviene perseguir primero?

📘 **Dónde se aprende** (1 clase): [B83-C01 · Necesidad de misión y caso científico](../programa/clases/B83/B83-C01-necesidad-de-mision-y-caso-cientifico/CLASE.md).

### Criterio de Rayleigh

- El criterio de Rayleigh es un PV de λ/4.
- El ruido de fotones (o de disparo) es de tamaño `√N`; el criterio de Rayleigh da el límite de difracción `1,22 λ/D`.
- El criterio de Rayleigh: separación igual al primer cero.

💡 **Cómo se explica en la clase [B50-C14](../programa/clases/B50/B50-C14-criterios-de-aceptacion-strehl-error-de-frente-de-onda-y-especificaciones/CLASE.md):**
- La esférica de una onda con el mejor enfoque tiene PV `0,2500`, RMS `0,0746`, `S = 0,8002` y Maréchal `0,8030`: el criterio de Rayleigh (λ/4 PV) y el de Maréchal (`S ≈ 0,8`) coinciden.
- 🎯 **Por qué importa:** Una especificación solo sirve si se puede verificar con una medida que tiene incertidumbre. La decisión central: ¿cuánto margen se deja para que una medida incierta no acepte una unidad mala?

📘 **Dónde se aprende** (4 clases): [B41-C12 · Difracción y límite de Rayleigh](../programa/clases/B41/B41-C12-difraccion-y-limite-de-rayleigh/CLASE.md); [B42-C05 · Patrones de Airy](../programa/clases/B42/B42-C05-patrones-de-airy/CLASE.md); [B50-C14 · Criterios de aceptación: Strehl, error de frente de onda y especificaciones](../programa/clases/B50/B50-C14-criterios-de-aceptacion-strehl-error-de-frente-de-onda-y-especificaciones/CLASE.md); [B57-C04 · Satélites ópticos de observación](../programa/clases/B57/B57-C04-satelites-opticos-de-observacion/CLASE.md).

### Criterio de rechazo de datos

- Un criterio de rechazo de datos es la regla, escrita antes, para descartar una lectura.

🎯 **Por qué importa (clase B01-C20):** Entender el método no es lo mismo que aplicarlo. Cuando mides de verdad, aparecen problemas que los ejercicios no tienen: el cielo se nubla, el palo no está del todo vertical, la regla se mueve, los datos no coinciden con lo que predijiste.

📘 **Dónde se aprende** (1 clase): [B01-C20 · Proyecto de observación científica inicial](../programa/clases/B01/B01-C20-proyecto-de-observacion-cientifica-inicial/CLASE.md).

### Criterio de refinamiento

- Un criterio de refinamiento decide qué celdas se dividen.

🎯 **Por qué importa (clase B21-C05):** Los códigos de referencia en astrofísica, como RAMSES (S1) y Athena++ (S2), usan mallas adaptativas porque los problemas tienen rangos de escala enormes. Pero un esquema adaptativo mal construido no conserva: crea o destruye masa en las interfaces entre niveles, justo donde está el fenómeno interesante.

📘 **Dónde se aprende** (1 clase): [B21-C05 · Mallas adaptativas (AMR)](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md).

### Criterio de refutación

- Un criterio de refutación es el resultado que, de ocurrir, te hace rechazar la hipótesis.

💡 **Cómo se explica en la clase [B01-C07](../programa/clases/B01/B01-C07-hipotesis-y-predicciones-falsables/CLASE.md):**
- Paso 4 · Criterio de refutación. Se rechaza si `|R − 1| ≤ 2σ_R`; se mantiene si `|R − 1,116| ≤ 2σ_R` y no es compatible con 1.
- 🎯 **Por qué importa:** Una afirmación que ningún resultado posible contradice no enseña nada. Si dices «la Luna cambia de tamaño aparente» y, ocurra lo que ocurra, tu frase queda a salvo, no has dicho gran cosa.

📘 **Dónde se aprende** (1 clase): [B01-C07 · Hipótesis y predicciones falsables](../programa/clases/B01/B01-C07-hipotesis-y-predicciones-falsables/CLASE.md).

### Criterio de Routh–Hurwitz

- El arreglo de Routh es una tabla construida con los coeficientes; el criterio de Routh–Hurwitz dice que el número de cambios de signo en su primera columna es el número de raíces con parte real positiva.

🎯 **Por qué importa (clase B16-C08):** Al diseñar un lazo, la ganancia `K` es una incógnita que quieres elegir. Calcular las raíces para cada `K` es posible con un computador, pero no da la frontera: el valor exacto de `K` por encima del cual el sistema se desestabiliza.

📘 **Dónde se aprende** (1 clase): [B16-C08 · Criterio de Routh-Hurwitz](../programa/clases/B16/B16-C08-criterio-de-routh-hurwitz/CLASE.md).

### Criterio de Schwarzschild

- El criterio de Schwarzschild dice que una capa es inestable si su gradiente real `−dT/dz` supera `Γ`.
- El criterio de Schwarzschild dice que hay convección si `∇_rad > ∇_ad`.

🎯 **Por qué importa (clase B24-C05):** La energía generada en el núcleo tarda milenios en salir y el modo de transporte decide la estructura: si el interior de una estrella es convectivo, su composición se mezcla; si es radiativo, no. De ello depende cuánto combustible alcanza el núcleo, y por tanto la vida de la estrella.

📘 **Dónde se aprende** (2 clases): [B24-C05 · Transporte radiativo y convectivo](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md); [B54-C05 · Transporte convectivo](../programa/clases/B54/B54-C05-transporte-convectivo/CLASE.md).

### Criterio de Sparrow

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B41-C12):** La difracción fija el mejor detalle posible. La decisión central: ¿cuándo se resuelven dos estrellas y qué cuesta una obstrucción?

📘 **Dónde se aprende** (1 clase): [B41-C12 · Difracción y límite de Rayleigh](../programa/clases/B41/B41-C12-difraccion-y-limite-de-rayleigh/CLASE.md).

### Criterio de tolerancia

- El criterio de tolerancia pide coma menor que el radio de Airy.

🎯 **Por qué importa (clase B43-C18):** Colimar es ajustar tornillos hasta que el coma deje de verse; el modelo dice cuánto es «suficiente». La decisión central: ¿qué inclinación del primario produce un coma igual al radio de Airy y cuánto desvía un plano inclinado?

📘 **Dónde se aprende** (1 clase): [B43-C18 · Colimación instrumental](../programa/clases/B43/B43-C18-colimacion-instrumental/CLASE.md).

### Criterio necesario

- Un criterio necesario debe cumplirse siempre; uno suficiente basta por sí solo.

🎯 **Por qué importa (clase B56-C01):** Una misión que busca vida necesita saber qué buscar y qué contará como hallazgo. Si el criterio es vago, cualquier resultado se puede discutir; si es demasiado estrecho, se pasa por alto lo que no se parece a la vida terrestre.

📘 **Dónde se aprende** (1 clase): [B56-C01 · Definiciones operativas de vida](../programa/clases/B56/B56-C01-definiciones-operativas-de-vida/CLASE.md).

### Criterios de aceptación

- Los criterios de aceptación del ejemplo son: base sin defectos, 100 % de comandos probados y todos los operadores con al menos 32 h.

💡 **Cómo se explica en la clase [B83-C19](../programa/clases/B83/B83-C19-aceptacion-y-transferencia-a-operaciones/CLASE.md):**
- *Descripción textual:* la base de datos se revisa y se calibra; los límites dan alarmas; junto con los comandos probados y el entrenamiento forman los criterios de aceptación, que deciden si la transferencia se acepta.
- 🎯 **Por qué importa:** Un satélite entregado con una base de datos errónea muestra valores falsos o alarmas inútiles; operadores sin entrenamiento no saben responder. La decisión central: ¿la base de datos, los comandos y las personas están listos, de modo que operaciones pueda recibir el sistema?

📘 **Dónde se aprende** (1 clase): [B83-C19 · Aceptación y transferencia a operaciones](../programa/clases/B83/B83-C19-aceptacion-y-transferencia-a-operaciones/CLASE.md).

### Criterios de inclusión y exclusión

- Los criterios de inclusión y exclusión son reglas escritas antes de ver los resultados que deciden qué obra entra al análisis.

🎯 **Por qué importa (clase B20-C01):** Cuando alguien afirma «no hay estudios sobre esto» o «es sabido que…», la frase vale tanto como el procedimiento con que se buscó. Dos personas que buscan lo mismo sin anotar cómo lo hicieron obtendrán listas distintas y no podrán explicar por qué.

📘 **Dónde se aprende** (1 clase): [B20-C01 · Búsqueda bibliográfica sistemática y gestión de referencias](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md).

### Crítica de fuentes

- La crítica de fuentes es el examen de origen, fecha, propósito y dependencia de un testimonio.

🎯 **Por qué importa (clase B132-C01):** Un relato histórico es tan fiable como las fuentes que lo sostienen, y tres copias de una misma fuente no son tres fuentes. La decisión central: ¿cuánto apoyo da realmente un conjunto de fuentes a una afirmación y cuánto de ese apoyo es robusto ante cambios razonables de criterio?

📘 **Dónde se aprende** (1 clase): [B132-C01 · Crítica histórica de fuentes y método historiográfico](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md).

### Criticidad

- La criticidad mide cuántos nodos caen por una falla.
- Criticidad: consecuencia de un comando.

💡 **Cómo se explica en la clase [B96-C07](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md):**
- Se evalúan `3 × 4 × 5 × 2 = 120` combinaciones (rol, criticidad, cinco listas de aprobaciones, armado sí/no) con la política y con una referencia independiente basada en tablas de mínimos.
- C["Comando y criticidad"] --> R{"Rol minimo?"}
- 🎯 **Por qué importa:** Un comando enviado por la persona equivocada o sin segunda revisión puede perder la misión. La decisión central: ¿qué rol, qué aprobaciones y qué armado exige cada nivel de criticidad y cómo se prueba que la política no tiene huecos?

📘 **Dónde se aprende** (2 clases): [B96-C07 · Telecomandos y autorizaciones](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md); [B119-C16 · Protección de infraestructura crítica](../programa/clases/B119/B119-C16-proteccion-de-infraestructura-critica/CLASE.md).

### Crítico

- Es crítico si su fallo impide la revisión.
- Un criterio crítico bloquea el veredicto si no se cumple.

💡 **Cómo se explica en la clase [B83-C13](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md):**
- SRR: requisitos verificables (≥ 95 %), necesidades con requisito (100 %), requisitos con origen (100 %), CONOPS documentado y estabilidad del orden de necesidades (≥ 70 %, no crítico).
- Analogía: la lista de verificación previa al despegue de un avión: si un punto crítico falla, no se despega, aunque el resto esté bien.
- ⚠️ **Error frecuente:** Promediar criterios críticos. Un crítico fallido impide la revisión
- 🎯 **Por qué importa:** Una revisión aprobada sin criterios es un trámite; una revisión con criterios medibles es una decisión. La decisión central: ¿el proyecto cumple los criterios de entrada de la SRR y de la PDR y qué falta para llegar?

📘 **Dónde se aprende** (2 clases): [B83-C13 · Revisiones SRR y PDR](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md); [B128-C11 · Auditoría de accesibilidad de un recurso educativo](../programa/clases/B128/B128-C11-auditoria-de-accesibilidad-de-un-recurso-educativo/CLASE.md).

### Críticos

- Los eventos críticos nunca pasan por el limitador.

💡 **Cómo se explica en la clase [B88-C10](../programa/clases/B88/B88-C10-gestion-de-eventos/CLASE.md):**
- Con limitador: registrados `48`, suprimidos `978` (todos del identificador 5) y críticos registrados `2` de `2`.
- Paso 4 · Críticos. Ambos `RESET_WDG` se registran.
- ⚠️ **Error frecuente:** Limitar también los críticos. Exímelos del limitador (8.2)
- 🎯 **Por qué importa:** Un sensor que parpadea puede generar miles de eventos y saturar el registro y el enlace, ocultando el único evento importante. La decisión central: ¿cómo se limita el ruido sin perder lo crítico?

📘 **Dónde se aprende** (1 clase): [B88-C10 · Gestión de eventos](../programa/clases/B88/B88-C10-gestion-de-eventos/CLASE.md).

### Cromosfera

- La fotosfera es la capa que emite la luz visible; la cromosfera y la corona están encima.

💡 **Cómo se explica en la clase [B30-C02](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md):**
- Las temperaturas (5772 K nominal de la fotosfera; 10⁴ K y 1,5 × 10⁶ K ilustrativas para cromosfera y corona) y las masas moleculares medias (1,3; 1,2; 0,6) son ilustrativas.
- 🎯 **Por qué importa:** La corona caliente es el origen del viento solar y de gran parte de la actividad. Entender por qué no puede estar en reposo conecta el Sol con el medio interplanetario.

📘 **Dónde se aprende** (1 clase): [B30-C02 · Fotosfera, cromosfera y corona](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md).

### Crónica

- Una crónica es un relato histórico escrito, aquí por cronistas del siglo XVI.
- La carga aguda es el promedio de los últimos 7 días; la crónica, el de 28.

💡 **Cómo se explica en la clase [B02-C05](../programa/clases/B02/B02-C05-cosmovisiones-andinas-del-cielo/CLASE.md):**
- La crónica da contexto, pero fue escrita desde fuera.
- 🎯 **Por qué importa:** Hablar de «astronomía andina» en singular es un error: los Andes reúnen sociedades de épocas y regiones muy distintas. La pregunta motivadora es: ¿cómo se estudia respetuosamente un cielo que otra cultura leyó de otra manera, sin imponerle nuestras categorías y sin inventar lo que las fuentes no dicen?

📘 **Dónde se aprende** (2 clases): [B02-C05 · Cosmovisiones andinas del cielo](../programa/clases/B02/B02-C05-cosmovisiones-andinas-del-cielo/CLASE.md); [B107-C05 · Prevención de lesiones en entrenamiento y trabajo operativo](../programa/clases/B107/B107-C05-prevencion-de-lesiones-en-entrenamiento-y-trabajo-operativo/CLASE.md).

### Crónico

- El estresor agudo `S(t) = 1` durante 2 h y el crónico `S = 0,5` durante 7 días.

💡 **Cómo se explica en la clase [B105-C22](../programa/clases/B105/B105-C22-sistema-neuroendocrino-y-respuesta-al-estres-en-vuelo/CLASE.md):**
- Con `S = 0,5` durante 7 días (`g = 1`), la media diaria sube de 1,000 a 1,341 (+34,1 %) y la amplitud pico-valle baja de 1,156 a 0,926: el estrés crónico eleva el nivel y aplana el ritmo en el modelo.
- Con `g = 1`, el aumento cae al 10 % en 2,74 h; un estresor crónico (+0,5 durante 7 días) sube la media diaria de 1,000 a 1,341 (+34,1 %).
- ⚠️ **Error frecuente:** Confundir estrés agudo y crónico. Efectos distintos en nivel y ritmo.
- 🎯 **Por qué importa:** Una medición de cortisol sin hora del día no se interpreta: el ritmo diario domina. Y un estresor crónico cambia el nivel medio de una forma distinta que uno agudo.

📘 **Dónde se aprende** (1 clase): [B105-C22 · Sistema neuroendocrino y respuesta al estrés en vuelo](../programa/clases/B105/B105-C22-sistema-neuroendocrino-y-respuesta-al-estres-en-vuelo/CLASE.md).

### Cronología

- Una cronología es una lista ordenada de hitos con fecha.
- La cronología `N₁(T)` convierte edad `T` en densidad.

💡 **Cómo se explica en la clase [B70-C04](../programa/clases/B70/B70-C04-vulcanismo-marciano-provincias-edades-y-evolucion/CLASE.md):**
- Las edades reales requieren la cronología publicada y la verificación de la saturación;
- *Descripción textual:* el conteo da una densidad; la cronología la convierte en edad y la fluctuación de Poisson da el intervalo.
- ⚠️ **Error frecuente:** Creer que la cronología es la publicada. Se corrige en la sección 5.
- 🎯 **Por qué importa:** Un conteo de cráteres es un número entero y ruidoso. La decisión central: ¿qué edad y qué incertidumbre le corresponden a una provincia dada su área y su conteo?

📘 **Dónde se aprende** (2 clases): [B70-C04 · Vulcanismo marciano: provincias, edades y evolución](../programa/clases/B70/B70-C04-vulcanismo-marciano-provincias-edades-y-evolucion/CLASE.md); [B104-C01 · Historia de vuelos tripulados](../programa/clases/B104/B104-C01-historia-de-vuelos-tripulados/CLASE.md).

### Cruce

- Un cruce es el punto donde dos pasadas se intersecan.
- El cruce es la potencia a partir de la cual otra fuente pesa menos.
- El cruce es la `c` donde ambas valen lo mismo.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B28-C17](../programa/clases/B28/B28-C17-archivos-de-eventos-multimensajero/CLASE.md):**
- REG --> CRU["cruce: |Δt| ≤ ventana y separación ≤ radio"]
- *Descripción textual:* cada registro se serializa de forma canónica y se firma con SHA-256; el validador revisa esquema, rangos, formato de tiempo, versión y huella; el cruce busca pares de mensajeros distintos.
- 🎯 **Por qué importa:** Un catálogo sin identificadores estables, versiones ni huellas no se puede citar ni auditar. La decisión central: ¿cómo se guarda un evento para que se pueda verificar, actualizar y cruzar con otros?

📘 **Dónde se aprende** (6 clases): [B28-C17 · Archivos de eventos multimensajero](../programa/clases/B28/B28-C17-archivos-de-eventos-multimensajero/CLASE.md); [B53-C07 · Topografía por altimetría](../programa/clases/B53/B53-C07-topografia-por-altimetria/CLASE.md); [B86-C22 · Suministro de energía durante la noche lunar](../programa/clases/B86/B86-C22-suministro-de-energia-durante-la-noche-lunar/CLASE.md); [B88-C32 · Redundancia fría y caliente: estrategias y conmutación](../programa/clases/B88/B88-C32-redundancia-fria-y-caliente-estrategias-y-conmutacion/CLASE.md); [B88-C33 · Votación y redundancia modular triple (TMR)](../programa/clases/B88/B88-C33-votacion-y-redundancia-modular-triple-tmr/CLASE.md); [B88-C44 · Mantenimiento predictivo y pronóstico de salud de sistemas](../programa/clases/B88/B88-C44-mantenimiento-predictivo-y-pronostico-de-salud-de-sistemas/CLASE.md).

### Cruce de fase

- El cruce de ganancia `ω_gc` es donde `|L| = 1` (0 dB); el cruce de fase `ω_pc` es donde la fase es −180°.

💡 **Cómo se explica en la clase [B16-C10](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md):**
- El cruce de fase ocurre en `ω_pc = √2 = 1,414 rad/s`, donde `|L| = K/(√2·√3·√6) = K/6`.
- 🎯 **Por qué importa:** Los modelos nunca son exactos: la inercia varía, el sensor tarda más de lo supuesto, un modo flexible aparece. La estabilidad nominal no basta; hay que saber cuánto error aguanta el lazo.

📘 **Dónde se aprende** (1 clase): [B16-C10 · Diagramas de Bode y Nyquist](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md).

### Cruce de ganancia

- El cruce de ganancia `ω_gc` es donde `|L| = 1` (0 dB); el cruce de fase `ω_pc` es donde la fase es −180°.

💡 **Cómo se explica en la clase [B16-C10](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md):**
- Paso 1 · cruce de ganancia. Se resuelve `|L(jω)| = 1` con `K = 2`: `ω_gc = 0,749 rad/s`.
- 🎯 **Por qué importa:** Los modelos nunca son exactos: la inercia varía, el sensor tarda más de lo supuesto, un modo flexible aparece. La estabilidad nominal no basta; hay que saber cuánto error aguanta el lazo.

📘 **Dónde se aprende** (1 clase): [B16-C10 · Diagramas de Bode y Nyquist](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md).

### Cruce de láminas

- El cruce de láminas ocurre cuando `1 − aε = 0`.

🎯 **Por qué importa (clase B36-C05):** Una simulación sin comprobar contra un caso exacto no es una prueba. La decisión central: ¿converge el integrador al resultado analítico y qué pasa cuando las láminas se cruzan?

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
- 🎯 **Por qué importa:** Ninguna clase trataba la carga cognitiva ni el diseño de tareas para limitarla. La decisión central: ¿cómo se mide la carga y cómo se rediseña una secuencia para que no haya picos que superen la capacidad?

📘 **Dónde se aprende** (1 clase): [B111-C03 · Carga cognitiva y gestión de la atención](../programa/clases/B111/B111-C03-carga-cognitiva-y-gestion-de-la-atencion/CLASE.md).

### CSI

- El POD es la fracción de eventos detectados, el FAR la de alertas falsas y el CSI la de aciertos sobre todos los casos relevantes.

🎯 **Por qué importa (clase B30-C20):** Una alerta con muchas falsas alarmas se ignora y una con muchos fallos no sirve; medir ambas cosas es parte del oficio. La decisión central: ¿cómo se clasifica un evento y cómo se mide si una regla de alerta tiene habilidad?

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

🎯 **Por qué importa (clase B106-C26):** Las aguas grises son el mayor volumen del lazo y su carga orgánica hay que destruirla antes de potabilizar. La decisión central: ¿qué volumen de biorreactor y qué desinfección dan la remoción y la reducción de microorganismos requeridas?

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

🎯 **Por qué importa (clase B44-C12):** Si el bias no se resta, el patrón fijo queda en la imagen. La decisión central: ¿cuántos cuadros se necesitan para que el maestro no añada ruido apreciable?

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

🎯 **Por qué importa (clase B40-C15):** La varianza cósmica es el límite fundamental de la medición del fondo. La decisión central: ¿qué precisión máxima permite el número de modos disponibles?

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
- 🎯 **Por qué importa:** Casi nunca interesa *qué* resultado ocurrió, sino *un número* que resume el resultado: cuántos computadores funcionan, qué error tuvo una medición, cuántos fotones llegaron. Poner un número en cada resultado permite sumar, promediar y comparar.

📘 **Dónde se aprende** (1 clase): [B12-C02 · Variables aleatorias](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md).

### Cuantización

- La cuantización es el redondeo del ADC, con varianza `1/12 ADU²`.
- La cuantización reemplaza el valor por el nivel más cercano.
- La cuantización con pérdida.
- *(y 6 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B44-C06](../programa/clases/B44/B44-C06-ruido-de-lectura/CLASE.md):**
- La cuantización importa solo si el ruido es menor que unos `1 ADU`.
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
- *Descripción textual:* un ciclo de cuatro estaciones: luna nueva (edad 0), cuarto creciente (un cuarto del período), luna llena (la mitad) y cuarto menguante (tres cuartos); luego vuelve a la luna nueva.
- 🎯 **Por qué importa:** La Luna es el reloj más a mano del cielo: cada noche cambia, y cada 29,5 días vuelve a empezar. Pero «a mano» no significa «fácil de explicar»: muchas personas creen que las fases son la sombra de la Tierra sobre la Luna.

📘 **Dónde se aprende** (1 clase): [B01-C12 · Fases lunares y ciclos celestes](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md).

### Cuásar

- Un cuásar es un núcleo galáctico activo muy lejano; su movimiento propio esperado es despreciable (S1, cap. 2).

💡 **Cómo se explica en la clase [B13-C21](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md):**
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

🎯 **Por qué importa (clase B105-C19):** No basta con quitar el nombre: con edad, sexo, profesión y misión, una persona de una cohorte de 6 suele ser única. La decisión central: ¿qué se puede publicar de una cohorte pequeña sin identificar a nadie y cuánta utilidad se pierde al protegerla?

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
- 🎯 **Por qué importa:** Un telescopio debe girar desde una orientación a otra y quedarse allí. Con tres ejes acoplados y rotaciones grandes, ni los ángulos de Euler (tienen singularidades y dependen de la secuencia de giros) ni el modelo lineal bastan.

📘 **Dónde se aprende** (1 clase): [B16-C20 · Control de orientación en un simulador](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md).

### Cuaternión puro

- Un cuaternión puro `(0, v)` representa un vector.

🎯 **Por qué importa (clase B10-C15):** Un seguidor estelar entrega la actitud del satélite varias veces por segundo; el sistema de control la combina con las lecturas de giróscopos, la propaga y la compara con la actitud deseada. Hacerlo con ángulos de Euler es frágil; hacerlo con matrices cuesta más y acumula deriva.

📘 **Dónde se aprende** (1 clase): [B10-C15 · Cuaterniones unitarios](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md).

### Cuaternión unitario

- Un cuaternión unitario `q = [q0, q_v]` (escalar primero, `q_v` de tres componentes) con `q0² + |q_v|² = 1` representa una rotación; usamos la convención de que lleva componentes del sistema inercial al del cuerpo.

🎯 **Por qué importa (clase B16-C20):** Un telescopio debe girar desde una orientación a otra y quedarse allí. Con tres ejes acoplados y rotaciones grandes, ni los ángulos de Euler (tienen singularidades y dependen de la secuencia de giros) ni el modelo lineal bastan.

📘 **Dónde se aprende** (1 clase): [B16-C20 · Control de orientación en un simulador](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md).

### CubeSat 3U

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

🎯 **Por qué importa (clase B47-C25):** Muchos CubeSat universitarios fracasan por requisitos sin cifra o sin evidencia. La decisión central: ¿qué requisitos medibles se fijan, cómo se verifican y cuáles cumple un diseño preliminar?

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

🎯 **Por qué importa (clase B88-C10):** Un sensor que parpadea puede generar miles de eventos y saturar el registro y el enlace, ocultando el único evento importante. La decisión central: ¿cómo se limita el ruido sin perder lo crítico?

📘 **Dónde se aprende** (1 clase): [B88-C10 · Gestión de eventos](../programa/clases/B88/B88-C10-gestion-de-eventos/CLASE.md).

### Cubo hiperespectral

- El cubo hiperespectral tiene dos dimensiones espaciales y una espectral.

🎯 **Por qué importa (clase B57-C22):** Dos materiales distintos pueden parecer iguales en cuatro bandas anchas y diferenciarse en cientos de bandas estrechas. La decisión central: ¿cuándo vale la pena el costo en datos de un sensor hiperespectral y cómo se separa una mezcla de materiales?

📘 **Dónde se aprende** (1 clase): [B57-C22 · Espectrómetros de imagen e hiperespectrales](../programa/clases/B57/B57-C22-espectrometros-de-imagen-e-hiperespectrales/CLASE.md).

### Cuello

- El cuello es la zona de unión entre dos partículas y `x/a` su razón.
- Un cuello está abierto si `C ≤ C(Li)`.

💡 **Cómo se explica en la clase [B59-C12](../programa/clases/B59/B59-C12-sinterizacion-de-materiales/CLASE.md):**
- Como miel que se espesa al enfriarse: a baja temperatura casi no fluye y el cuello crece muy despacio.
- *Descripción textual:* la temperatura fija la viscosidad; la ley de Frenkel da el tiempo para un cuello; la regresión del logaritmo del tiempo recupera la energía de activación.
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

🎯 **Por qué importa (clase B26-C16):** La cuarta parte de la masa bariónica del universo es helio, y la proporción casi no cambió desde los primeros minutos. Su valor da información sobre cuántas especies de neutrinos existen y sobre la densidad de bariones.

📘 **Dónde se aprende** (1 clase): [B26-C16 · Nucleosíntesis primordial](../programa/clases/B26/B26-C16-nucleosintesis-primordial/CLASE.md).

### Cuenca multianillo

- Una cuenca multianillo tiene varios anillos concéntricos.

🎯 **Por qué importa (clase B61-C07):** Las cuencas dejan huella en la corteza entera. La decisión central: ¿cómo se espacian los anillos, qué proyectil implica una cuenca y cuándo excava hasta el manto?

📘 **Dónde se aprende** (1 clase): [B61-C07 · Cuencas multianillo y grandes impactos](../programa/clases/B61/B61-C07-cuencas-multianillo-y-grandes-impactos/CLASE.md).

### Cuenta

- La cuenta `N = f/(presc)·Δt`.
- Parámetro: una magnitud con nombre, unidad y límites. Cuenta: valor entero del conversor.

💡 **Cómo se explica en la clase [B88-C02](../programa/clases/B88/B88-C02-microcontroladores-embarcados/CLASE.md):**
- Paso 1 · Cuenta. `16·10⁶/64 · 10⁻³ = 250`.
- El laboratorio verifica que la cuenta 250 sea exacta.
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

🎯 **Por qué importa (clase B88-C13):** Una actualización fallida en órbita no se arregla con un cable. La decisión central: ¿qué comprobaciones aceptan solo la imagen correcta y qué mecanismo vuelve a una versión conocida si la nueva no arranca?

📘 **Dónde se aprende** (1 clase): [B88-C13 · Actualización segura de software](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md).

### Cuenta de Coulomb

- La cuenta de Coulomb integra la corriente.

🎯 **Por qué importa (clase B86-C06):** Cargar más rápido reduce el tiempo pero eleva el calor y la tensión sobre la celda; cargar más lento puede no completar el ciclo antes del siguiente eclipse. El perfil de carga decide si la batería vuelve a su estado de carga en cada órbita.

📘 **Dónde se aprende** (1 clase): [B86-C06 · Gestión de carga](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md).

### Cuenta integrada

- La cuenta integrada acumula ciclos de Doppler y da la variación de alcance.

🎯 **Por qué importa (clase B74-C04):** Una velocidad radial de `1 mm/s` produce un desplazamiento de decenas de milihercios, medible; por eso el Doppler es el observable más preciso de la navegación en espacio profundo. La decisión central: ¿qué información da el Doppler (velocidad en la línea de visión) y qué no (posición transversal)?

📘 **Dónde se aprende** (1 clase): [B74-C04 · Doppler de navegación](../programa/clases/B74/B74-C04-doppler-de-navegacion/CLASE.md).

### Cuenta regresiva

- Una cuenta regresiva usa T− antes de un instante de referencia y T+ después.

💡 **Cómo se explica en la clase [B03-C09](../programa/clases/B03/B03-C09-operaciones-con-numeros-negativos/CLASE.md):**
- La cuenta regresiva es una recta de tiempo con signos.
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
- 🎯 **Por qué importa:** Enfriar un telescopio cuesta masa, potencia y complejidad. La decisión central: ¿a qué temperatura el fondo propio deja de dominar sobre el detector?

📘 **Dónde se aprende** (1 clase): [B47-C04 · Telescopios infrarrojos](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md).

### Cuerpo menor

- Un cuerpo menor es un asteroide o cometa.

🎯 **Por qué importa (clase B58-C01):** La pregunta que organiza el bloque es *¿qué es este objeto y qué tan cerca pasa?* Un mismo punto de luz puede ser un asteroide del cinturón principal sin ningún interés para la defensa planetaria o un objeto cercano a la Tierra.

📘 **Dónde se aprende** (1 clase): [B58-C01 · Clasificación de cuerpos menores](../programa/clases/B58/B58-C01-clasificacion-de-cuerpos-menores/CLASE.md).

### Cuerpo menor del sistema solar

- Un cuerpo menor del sistema solar es cualquier otro objeto que orbita el Sol y no es satélite (la IAU incluye a la mayoría de los asteroides, la mayoría de los objetos transneptunianos y los cometas).

🎯 **Por qué importa (clase B01-C03):** En 2006 la Asamblea General de la Unión Astronómica Internacional votó una definición de planeta y, desde entonces, Plutón dejó de contarse como el noveno planeta. Muchas personas sintieron que «se había cambiado la realidad».

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
- 🎯 **Por qué importa:** El desdoblamiento promedia la rotación de las regiones que el modo explora. La decisión central: ¿cuánto giran el núcleo y la envoltura y con qué incertidumbre y correlación?

📘 **Dónde se aprende** (1 clase): [B37-C11 · Rotación interna a partir del desdoblamiento de frecuencias](../programa/clases/B37/B37-C11-rotacion-interna-a-partir-del-desdoblamiento-de-frecuencias/CLASE.md).

### Culminación

- La culminación es el paso por el meridiano, el punto más alto del día.
- El ángulo horario `H` es el ángulo, medido hacia el oeste, entre el meridiano y el círculo que pasa por el astro y los polos; vale cero cuando el astro cruza el meridiano (tránsito o culminación, S2).
- La culminación (o tránsito meridiano) es el momento en que el astro cruza el meridiano, con `H = 0`.

💡 **Cómo se explica en la clase [B09-C05](../programa/clases/B09/B09-C05-derivadas-trigonometricas/CLASE.md):**
- (Esto es derivación implícita en pequeño; se generaliza en C06.) Se anula en `H = 0`: en la culminación la altitud deja de subir y todavía no baja.
- Descripción larga: la curva baja de 12,55 a 0 ″/s, casi plana al principio y con más pendiente cerca de la culminación; después cambia de signo (la estrella desciende).
- 🎯 **Por qué importa:** Un telescopio con montura altacimutal apunta con dos ejes: altitud y azimut. Para mantener una estrella en el centro del campo, cada eje debe girar a una velocidad que cambia con el tiempo.

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
- C --> D["Grupo o cúmulo<br/>galaxias ligadas entre sí"]
- 🎯 **Por qué importa:** En 2006 la Asamblea General de la Unión Astronómica Internacional votó una definición de planeta y, desde entonces, Plutón dejó de contarse como el noveno planeta. Muchas personas sintieron que «se había cambiado la realidad».

📘 **Dónde se aprende** (2 clases): [B01-C03 · Objetos celestes y sus diferencias](../programa/clases/B01/B01-C03-objetos-celestes-y-sus-diferencias/CLASE.md); [B01-C15 · Galaxias y agrupaciones cósmicas](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md).

### Cúmulo abierto

- Un cúmulo abierto es un grupo ligado de estrellas jóvenes y poco masivo del disco; un cúmulo globular es un grupo masivo, esférico y viejo; un cúmulo masivo joven (S2) tiene menos de ~100 Myr y más de ~10⁴ M☉.

🎯 **Por qué importa (clase B25-C06):** La mayoría de las estrellas nace en grupos. Los cúmulos son laboratorios: sus estrellas comparten edad, distancia y composición.

📘 **Dónde se aprende** (1 clase): [B25-C06 · Cúmulos estelares](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md).

### Cúmulo de escombros

- Un cúmulo de escombros (*rubble pile*) es un cuerpo hecho de fragmentos unidos por gravedad.

🎯 **Por qué importa (clase B58-C03):** La densidad aparente de un asteroide es casi siempre menor que la de sus rocas: la diferencia es porosidad, y de ella depende cuánta energía hace falta para desviarlo o fragmentarlo (C17). La decisión central: ¿cuánto de lo que parece masa es vacío, y cuánta incertidumbre arrastra la masa?

📘 **Dónde se aprende** (1 clase): [B58-C03 · Composición de asteroides](../programa/clases/B58/B58-C03-composicion-de-asteroides/CLASE.md).

### Cúmulo de galaxias

- Un cúmulo de galaxias es un sistema ligado de cientos a miles de galaxias, gas caliente y materia oscura.

🎯 **Por qué importa (clase B25-C13):** Los cúmulos de galaxias son las mayores estructuras ligadas por la gravedad. Contienen galaxias, un gas a decenas de millones de kelvin y mucha más masa de la que ambos aportan; por eso sirven para estudiar la materia oscura y poner a prueba el modelo cosmológico.

📘 **Dónde se aprende** (1 clase): [B25-C13 · Cúmulos de galaxias](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md).

### Cúmulo estelar

- Un cúmulo estelar es un conjunto ligado de estrellas nacidas de la misma nube.

🎯 **Por qué importa (clase B24-C19):** La edad de una estrella aislada es difícil de medir; la de un cúmulo se puede leer en su diagrama HR, porque las estrellas más masivas ya han salido de la secuencia principal y el «punto de desvío» marca la edad. Esas edades fijan la cronología de la Galaxia y calibran los modelos.

📘 **Dónde se aprende** (1 clase): [B24-C19 · Cúmulos y edades estelares](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md).

### Cúmulo globular

- Un cúmulo abierto es un grupo ligado de estrellas jóvenes y poco masivo del disco; un cúmulo globular es un grupo masivo, esférico y viejo; un cúmulo masivo joven (S2) tiene menos de ~100 Myr y más de ~10⁴ M☉.

🎯 **Por qué importa (clase B25-C06):** La mayoría de las estrellas nace en grupos. Los cúmulos son laboratorios: sus estrellas comparten edad, distancia y composición.

📖 **Explicado a fondo:** [Cúmulo globular](esencial/tercera-a-e.md#cúmulo-globular) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B25-C06 · Cúmulos estelares](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md).

### Cúmulo masivo joven

- Un cúmulo abierto es un grupo ligado de estrellas jóvenes y poco masivo del disco; un cúmulo globular es un grupo masivo, esférico y viejo; un cúmulo masivo joven (S2) tiene menos de ~100 Myr y más de ~10⁴ M☉.

🎯 **Por qué importa (clase B25-C06):** La mayoría de las estrellas nace en grupos. Los cúmulos son laboratorios: sus estrellas comparten edad, distancia y composición.

📘 **Dónde se aprende** (1 clase): [B25-C06 · Cúmulos estelares](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md).

### Cuota

- La cuota `s_i` es `q_i/Q`.
- La cuota es el peso mínimo para ganar una votación.

💡 **Cómo se explica en la clase [B124-C03](../programa/clases/B124/B124-C03-mercados-downstream-y-upstream/CLASE.md):**
- Aguas arriba la mayor cuota es `0,5238` y el HHI `4059`; aguas abajo, `1989`.
- El promedio ponderado por cuota es `HHI/ε = 0,4486`, igual al calculado directamente `0,4486`.
- 🎯 **Por qué importa:** Hablar de «mercado upstream» o «downstream» sin medir su concentración deja la discusión en opinión. La decisión central: ¿qué tan concentrado está un mercado y qué margen de precio permite esa concentración?

📘 **Dónde se aprende** (3 clases): [B48-C02 · Concesión de tiempo de observación](../programa/clases/B48/B48-C02-concesion-de-tiempo-de-observacion/CLASE.md); [B124-C03 · Mercados downstream y upstream](../programa/clases/B124/B124-C03-mercados-downstream-y-upstream/CLASE.md); [B125-C03 · Gobierno corporativo de una empresa espacial](../programa/clases/B125/B125-C03-gobierno-corporativo-de-una-empresa-espacial/CLASE.md).

### Cuota inicial

- La cuota inicial `U` se paga al firmar.

💡 **Cómo se explica en la clase [B124-C09](../programa/clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md):**
- Paso 4 · Con cuota. Con una cuota inicial de 1: valor total `2,2434` Mum.
- 🎯 **Por qué importa:** La propiedad intelectual es un activo, pero su valor depende de cuánto se vende con ella y de cuánto del margen se queda el que la usa. La decisión central: ¿qué licencia conviene ofrecer y cuántas regalías soporta el licenciatario?

📘 **Dónde se aprende** (1 clase): [B124-C09 · Propiedad intelectual y licencias](../programa/clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md).

### Cuota interna

- La cuota interna es la parte final de cada responsable.

💡 **Cómo se explica en la clase [B119-C03](../programa/clases/B119/B119-C03-convenio-de-responsabilidad/CLASE.md):**
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

🎯 **Por qué importa (clase B51-C07):** Una calibración mala puede dar una imagen bonita. La decisión central: ¿qué valor de χ² reducido y qué forma de los residuos indican que el modelo es suficiente?

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
- 🎯 **Por qué importa:** Los fragmentos consultados indican que tras el vuelo hay alteraciones del control postural y locomotor (Macaulay et al., 2021) y que el equilibrio dinámico, la percepción del tiempo y el tiempo de reacción cambian tras el aterrizaje (Clément et al., 2023). Antes del vuelo la pregunta es cómo preparar la desorientación.

📘 **Dónde se aprende** (3 clases): [B107-C03 · Entrenamiento vestibular y de orientación espacial](../programa/clases/B107/B107-C03-entrenamiento-vestibular-y-de-orientacion-espacial/CLASE.md); [B119-C21 · Cultura de seguridad aeroespacial y aprendizaje de incidentes](../programa/clases/B119/B119-C21-cultura-de-seguridad-aeroespacial-y-aprendizaje-de-incidentes/CLASE.md); [B124-C05 · Estimación de costos de misión](../programa/clases/B124/B124-C05-estimacion-de-costos-de-mision/CLASE.md).

### Curva de calibración

- La curva de calibración es la relación entre indicación y valor de la magnitud.

🎯 **Por qué importa (clase B13-C05):** Un sensor solar de una nave devuelve cuentas digitales (DN), no vatios por metro cuadrado. Para saber cuánta luz recibe hay que haberlo expuesto antes a fuentes de irradiancia conocida y haber establecido la relación entre ambas.

📘 **Dónde se aprende** (1 clase): [B13-C05 · Calibración instrumental](../programa/clases/B13/B13-C05-calibracion-instrumental/CLASE.md).

### Curva de costo

- La curva de costo tiene un mínimo de delta-v en el tiempo de Hohmann.

🎯 **Por qué importa (clase B75-C27):** Un viaje más corto gasta más combustible y uno más largo gasta más tiempo. La decisión central: ¿qué tiempo de vuelo minimiza el costo total cuando se pesan la masa lanzada y la duración?

📘 **Dónde se aprende** (1 clase): [B75-C27 · Duración de misión y tiempo de vuelo como restricción](../programa/clases/B75/B75-C27-duracion-de-mision-y-tiempo-de-vuelo-como-restriccion/CLASE.md).

### Curva de crecimiento

- La curva de crecimiento es `W` frente a la columna.

🎯 **Por qué importa (clase B32-C09):** Medir una abundancia exige saber en qué régimen está la línea. La decisión central: ¿cómo depende el ancho equivalente de la columna de absorbedores?

📘 **Dónde se aprende** (2 clases): [B32-C09 · Medición de perfiles de línea: ancho equivalente y ajuste](../programa/clases/B32/B32-C09-medicion-de-perfiles-de-linea-ancho-equivalente-y-ajuste/CLASE.md); [B45-C11 · Líneas de absorción](../programa/clases/B45/B45-C11-lineas-de-absorcion/CLASE.md).

### Curva de fase

- La curva de fase pliega la serie al periodo.

🎯 **Por qué importa (clase B29-C14):** El periodo es la propiedad básica de una variable periódica; de él y de la forma de la curva se deducen la masa, la edad o la distancia en muchos casos. La decisión central: ¿qué periodo y qué incertidumbre da la serie y qué métodos coinciden?

📘 **Dónde se aprende** (1 clase): [B29-C14 · Estrellas variables periódicas](../programa/clases/B29/B29-C14-estrellas-variables-periodicas/CLASE.md).

### Curva de Hill

- La curva de Hill `R(L) = Rmax L/(L + L50)` satura en `Rmax`;

💡 **Cómo se explica en la clase [B105-C16](../programa/clases/B105/B105-C16-contramedidas-de-ejercicio/CLASE.md):**
- Una curva de Hill `R = Rmax L/(L + L50)` con `Rmax = 0,8` y `L50 = 100` (ilustrativas) reduce la pérdida ósea: con `L = 100`, `R = 0,40` y la pérdida a 6 meses baja de 7,27 % a 4,21 %; con `L = 800`, a 2,15 %.
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
- *Descripción textual:* la curva de luz se ajusta con una recta en `log t`; el tiempo sobre el límite sale del modelo; la probabilidad de detección depende de la razón entre el tiempo visible y la cadencia.
- Esta clase no usa ninguna curva de luz medida: genera una sintética con `m₀ = 17`, `t₀ = 1 d`, `α = 1,3` (ilustrativos), 14 épocas entre `1` y `18,2 d` y un ruido de `0,1 mag`.
- 🎯 **Por qué importa:** Un transitorio que dura menos que el intervalo entre visitas se pierde. El índice de caída decide cuánto dura un evento sobre el límite de detección.

📖 **Explicado a fondo:** [Curva de luz](esencial/esencial-a-c.md#curva-de-luz) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (3 clases): [B28-C08 · Señales transitorias](../programa/clases/B28/B28-C08-senales-transitorias/CLASE.md); [B58-C13 · Caracterización de rotación](../programa/clases/B58/B58-C13-caracterizacion-de-rotacion/CLASE.md); [B129-C02 · Fotometría participativa](../programa/clases/B129/B129-C02-fotometria-participativa/CLASE.md).

### Curva de nivel

- Una curva de nivel es el conjunto de puntos donde `f` vale una constante `c`.
- Una curva de nivel es `f = c`; el gradiente es perpendicular a ella.

💡 **Cómo se explica en la clase [B09-C17](../programa/clases/B09/B09-C17-gradiente-y-derivada-direccional/CLASE.md):**
- Un paso de `100 km` a lo largo de la tangente a la curva de nivel cambia `Φ` en `1,75 × 10⁻⁷ km²/s²`; a lo largo del gradiente, en `7,90 × 10⁻⁴`.
- Caminar por una curva de nivel no sube ni baja.
- ⚠️ **Error frecuente:** Olvidar que el gradiente es perpendicular a la curva de nivel. Se corrige con el ejercicio 6.
- 🎯 **Por qué importa:** La gravedad no es un número: es un vector que apunta a un lado y tiene una magnitud. En un campo con dos cuerpos, como Tierra–Luna, esa dirección cambia de punto a punto.

📘 **Dónde se aprende** (2 clases): [B09-C15 · Funciones de varias variables](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md); [B09-C17 · Gradiente y derivada direccional](../programa/clases/B09/B09-C17-gradiente-y-derivada-direccional/CLASE.md).

### Curva de olvido

- La curva de olvido `R = e^(−Δt/S)` da la retención tras `Δt` días con estabilidad `S`.

💡 **Cómo se explica en la clase [B104-C06](../programa/clases/B104/B104-C06-entrenamiento-de-procedimientos/CLASE.md):**
- ⚠️ **Error frecuente:** Suponer que el dominio es permanente. Aplica la curva de olvido (8.3).
- 🎯 **Por qué importa:** Los procedimientos se practican en tierra y a veces se usan meses después, en el momento crítico. La decisión central: ¿cuándo repasar para que el procedimiento siga disponible sin gastar tiempo de entrenamiento de más?

📘 **Dónde se aprende** (1 clase): [B104-C06 · Entrenamiento de procedimientos](../programa/clases/B104/B104-C06-entrenamiento-de-procedimientos/CLASE.md).

### Curva de partición

- La curva de partición (de Tromp) da la probabilidad de que un grano de tamaño `d` vaya a un producto.

🎯 **Por qué importa (clase B59-C22):** Calentar o reducir todo el regolito es caro; separar la fracción rica antes ahorra energía. La decisión central: ¿qué tamaño de corte equilibra la ley del concentrado y la recuperación del mineral?

📘 **Dónde se aprende** (1 clase): [B59-C22 · Beneficio y separación granulométrica de regolito](../programa/clases/B59/B59-C22-beneficio-y-separacion-granulometrica-de-regolito/CLASE.md).

### Curva de polarización

- La curva de polarización `V(i)` suma el potencial reversible, la caída óhmica y la activación.

💡 **Cómo se explica en la clase [B59-C10](../programa/clases/B59/B59-C10-electrolisis-y-balances-energeticos/CLASE.md):**
- *Descripción textual:* la entalpía fija la tensión termoneutra; la curva de polarización da la tensión de operación; su comparación indica si la celda absorbe o cede calor.
- 🎯 **Por qué importa:** La electrólisis es el mayor consumidor de energía de la planta. La decisión central: ¿a qué densidad de corriente conviene operar, entre una celda pequeña que gasta más electricidad y una grande que gasta menos?

📘 **Dónde se aprende** (1 clase): [B59-C10 · Electrólisis y balances energéticos](../programa/clases/B59/B59-C10-electrolisis-y-balances-energeticos/CLASE.md).

### Curva de precisión–exhaustividad

- La curva de precisión–exhaustividad grafica precisión contra exhaustividad, y la precisión promedio resume su área (S2).

🎯 **Por qué importa (clase B17-C12):** Un modelo marca candidatos a planeta, y cada alerta cuesta horas de revisión. Si el modelo acierta el 99 % en una muestra donde el 99 % son negativos, no dice nada útil.

📘 **Dónde se aprende** (1 clase): [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md).

### Curva de rotación

- La curva de rotación es la velocidad circular en función del radio.
- La curva de rotación `v(R)` da la velocidad circular en función del radio.

💡 **Cómo se explica en la clase [B25-C08](../programa/clases/B25/B25-C08-curvas-de-rotacion-de-galaxias/CLASE.md):**
- *Descripción textual:* del disco visible se calcula su curva de rotación; la diferencia de cuadrados con la observada indica la masa que falta, que se modela como un halo.
- Para una espiral de disco sirve la curva de rotación; para elípticas, dispersiones o lentes.
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

🎯 **Por qué importa (clase B45-C17):** La atmósfera varía más que la señal; sin una referencia, la curva de luz no sirve. La decisión central: ¿qué comparaciones y qué precisión se necesitan para una profundidad dada?

📘 **Dónde se aprende** (1 clase): [B45-C17 · Fotometría diferencial](../programa/clases/B45/B45-C17-fotometria-diferencial/CLASE.md).

### Curva dosis-profundidad

- La curva dosis-profundidad `D(x) ∝ (1 + x/x₀)^−p`.

💡 **Cómo se explica en la clase [B85-C22](../programa/clases/B85/B85-C22-modelos-de-exposicion-a-radiacion-en-orbita/CLASE.md):**
- *Descripción textual:* la órbita da la posición geográfica en cada instante, el mapa sintético da la tasa local, el promedio sobre un día da la dosis diaria y anual, y la curva dosis-profundidad ajusta el blindaje.
- 🎯 **Por qué importa:** La dosis anual decide el blindaje y la vida de la electrónica y los materiales. La decisión central: ¿cuánta dosis acumula una órbita al año y cuánto la reduce un milímetro más de blindaje?

📘 **Dónde se aprende** (1 clase): [B85-C22 · Modelos de exposición a radiación en órbita](../programa/clases/B85/B85-C22-modelos-de-exposicion-a-radiacion-en-orbita/CLASE.md).

### Curva en V

- HFD: diámetro de media energía de una estrella. Curva en V: HFD contra posición.

🎯 **Por qué importa (clase B48-C22):** Un enfoque erróneo pierde resolución en todas las imágenes de la noche. La decisión central: ¿en qué posición del enfocador está el mínimo y con qué incertidumbre?

📘 **Dónde se aprende** (1 clase): [B48-C22 · Control automático del enfocador y autoenfoque](../programa/clases/B48/B48-C22-control-automatico-del-enfocador-y-autoenfoque/CLASE.md).

### Curva L

- La curva L es la gráfica, en escala log–log, de la norma de la solución frente a la norma del residuo al variar `λ` (S2).

💡 **Cómo se explica en la clase [B22-C02](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md):**
- Exige conocer `σ_ruido`; la curva L, no.
- Hansen advierte que el vértice de la curva L falla cuando la solución exacta es muy suave, es decir, cuando está dominada por pocos modos de la SVD: cuanto más suave, peor es el `λ` que da el criterio (S2, sec. 8.1, que atribuye el resultado a Hanke).
- 🎯 **Por qué importa:** Si no puedes confiar en `x = A⁻¹ b` y no puedes bajar el ruido a voluntad, necesitas una regla que ignore lo que los datos no pueden decir. Esa regla debe tener una perilla: cuánto ignorar.

📘 **Dónde se aprende** (1 clase): [B22-C02 · Regularización de Tikhonov](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md).

### Curva NC

- La curva NC es un límite por bandas de octava.

💡 **Cómo se explica en la clase [B109-C10](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md):**
- El resumen técnico OCHMO-TB-035 de NASA (Rev C, 2023) indica que NASA-STD-3001 Vol. 2 limita el ruido peligroso a menos de `85 dBA` sin importar la duración y el ruido continuo de las áreas de trabajo a la curva NC-50.
- 🎯 **Por qué importa:** El ruido continuo degrada la comunicación, el sueño y el trabajo aunque no dañe el oído. La decisión central: ¿qué fuente reduzco primero y cuánto baja el nivel de la cabina?

📘 **Dónde se aprende** (1 clase): [B109-C10 · Acústica y control de ruido interior](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md).

### Curva plana

- La curva plana es la velocidad de rotación constante a gran radio.

🎯 **Por qué importa (clase B36-C11):** Una alternativa debe confrontarse con todas las pruebas. La decisión central: ¿qué observación separa la materia oscura de la gravedad modificada?

📘 **Dónde se aprende** (1 clase): [B36-C11 · Gravedad modificada (MOND y relativistas) frente a materia oscura](../programa/clases/B36/B36-C11-gravedad-modificada-mond-y-relativistas-frente-a-materia-oscura/CLASE.md).

### Curva ROC

- La curva ROC grafica exhaustividad contra tasa de falsos positivos al variar el umbral; su área es el AUC.
- La curva ROC es POD frente a la tasa de falsas alarmas.
- La curva ROC grafica la fracción de anomalías detectadas contra la de falsas alarmas al variar el umbral; su área (AUC) vale 1 si el método separa perfectamente y 0,5 si no distingue (S2).

💡 **Cómo se explica en la clase [B17-C12](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md):**
- La curva ROC no cambia con la prevalencia, porque usa tasas dentro de cada clase; la de precisión–exhaustividad sí, y por eso refleja la carga de falsos positivos.
- Esa cifra es de ordenamiento, el equivalente de un área bajo la curva ROC: no dice cuántas alertas son reales a un umbral dado, que depende además de cuántos candidatos son planetas.
- 🎯 **Por qué importa:** Un modelo marca candidatos a planeta, y cada alerta cuesta horas de revisión. Si el modelo acierta el 99 % en una muestra donde el 99 % son negativos, no dice nada útil.

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
