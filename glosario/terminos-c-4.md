# Términos · C (parte 4 de 4)

[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)

[A](terminos-a.md) · [B](terminos-b.md) · **C** · [D](terminos-d.md) · [E](terminos-e.md) · [F](terminos-f.md) · [G](terminos-g.md) · [H](terminos-h.md) · [I](terminos-i.md) · [J](terminos-j.md) · [K](terminos-k.md) · [L](terminos-l.md) · [M](terminos-m.md) · [N](terminos-n.md) · [O](terminos-o.md) · [P](terminos-p.md) · [Q](terminos-q.md) · [R](terminos-r.md) · [S](terminos-s.md) · [T](terminos-t.md) · [U](terminos-u.md) · [V](terminos-v.md) · [W](terminos-w.md) · [X](terminos-x.md) · [Y](terminos-y.md) · [Z](terminos-z.md) · [0-9](terminos-0-9.md)

Partes: [1](terminos-c.md) · [2](terminos-c-2.md) · [3](terminos-c-3.md) · **4**

### Corriente de corte

- La corriente de corte (`C/20`) termina la carga.

💡 **Cómo se explica en la clase [B86-C06](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md):**
- La fase CV termina en la corriente de corte y repone `1,314 Ah` de los `1,399 Ah` (quedan `0,084 Ah`, que se recuperan en la órbita siguiente o con un corte más bajo).
- *Descripción textual:* la carga empieza a corriente constante hasta alcanzar la tensión máxima; luego sigue a tensión constante con corriente decreciente hasta la corriente de corte; la integral de la corriente da la carga repuesta.
- 🎯 **Por qué importa:** Cargar más rápido reduce el tiempo pero eleva el calor y la tensión sobre la celda; cargar más lento puede no completar el ciclo antes del siguiente eclipse. El perfil de carga decide si la batería vuelve a su estado de carga en cada órbita.
- 🔗 **Se estudia junto con:** fase CC, fase CV, tasa C, eficiencia de energía.

📘 **Dónde se aprende** (1 clase): [B86-C06 · Gestión de carga](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md).

### Corriente de fusión

- La corriente de fusión `I_f` es la mínima que lo funde.

💡 **Cómo se explica en la clase [B86-C10](../programa/clases/B86/B86-C10-proteccion-contra-sobrecorriente/CLASE.md):**
- *Descripción textual:* el bus da la corriente de falla; de ella salen los tiempos y las integrales `I²t` de cada fusible; si la de despeje del fusible de la rama es menor que la de fusión del de aguas arriba, es selectivo.
- Paso 4 · Lectura. Con `10 A`, más de tres veces la corriente de fusión, el fusible abre en unas décimas de segundo.
- 🎯 **Por qué importa:** Si el fusible aguas arriba se funde antes que el de la rama averiada, un fallo local deja sin energía a toda la nave. Una protección bien coordinada aísla la rama y conserva el resto.
- 🔗 **Se estudia junto con:** fusible, integral I²t, despeje, selectividad.

📘 **Dónde se aprende** (1 clase): [B86-C10 · Protección contra sobrecorriente](../programa/clases/B86/B86-C10-proteccion-contra-sobrecorriente/CLASE.md).

### Corriente de oscuridad

- La corriente de oscuridad es la señal que se acumula sin luz y crece con la exposición (S1).

💡 **Cómo se explica en la clase [B15-C09](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md):**
- Dividir por el plano antes de restar el oscuro, o restar un oscuro de otra duración sin escalar la corriente de oscuridad, produce errores sistemáticos.
- La guía de reducción de datos CCD de Astropy (S1) describe el modelo estándar: la imagen cruda es bias, corriente de oscuridad, ruido y un «plano» que multiplica al cielo y a las estrellas; resolver ese modelo da las cuentas de las estrellas.
- 🎯 **Por qué importa:** Una cámara de un telescopio no mide «luz de estrellas»: mide un número por píxel que incluye un desplazamiento electrónico, corriente de oscuridad, el cielo, la estrella y una sensibilidad que cambia de un píxel a otro. Si analizas el número crudo, mides la cámara, no el cielo.
- 🔗 **Se estudia junto con:** imagen digital, píxel, ADU, ganancia.

📘 **Dónde se aprende** (2 clases): [B15-C09 · Procesamiento de imágenes digitales](../programa/clases/B15/B15-C09-procesamiento-de-imagenes-digitales/CLASE.md); [B47-C04 · Telescopios infrarrojos](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md).

### Corriente de oscuridad D

- La corriente de oscuridad `D` es la carga generada térmicamente, en `e⁻/s/píxel`.

💡 **Cómo se explica en la clase [B13-C15](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md):**
- Con estos órdenes de magnitud (`R = 3,0 e⁻`, `1,6 e⁻/DN`) y un cielo, una corriente de oscuridad y una apertura sintéticos, se analiza una fuente débil.
- 🎯 **Por qué importa:** Una cámara espacial debe decidir cuánto tiempo exponer para detectar una fuente débil con una relación señal-ruido (SNR) dada. Exponer poco no la detecta; exponer demasiado satura los píxeles brillantes o desperdicia tiempo de misión.
- 🔗 **Se estudia junto con:** ruido de disparo, fondo de cielo B, ruido de lectura R, ganancia.

📘 **Dónde se aprende** (1 clase): [B13-C15 · Sensibilidad de detectores](../programa/clases/B13/B13-C15-sensibilidad-de-detectores/CLASE.md).

### Corriente de saturación

- La corriente de saturación `I_0` fija la tensión de circuito abierto.

💡 **Contexto en la clase [B86-C02](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md):**
- 🎯 **Por qué importa:** La potencia de una celda no es un número fijo: depende de la tensión a la que se la haga trabajar y de su temperatura. Elegir mal el punto de operación o ignorar la temperatura del ala cambia la potencia entregada.
- 🔗 **Se estudia junto con:** corriente fotogenerada, factor de idealidad, resistencia en serie, punto de máxima potencia.

📘 **Dónde se aprende** (1 clase): [B86-C02 · Celdas solares](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md).

### Corriente de tierra

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B33-C07](../programa/clases/B33/B33-C07-impactos-del-clima-espacial-en-redes-electricas/CLASE.md):**
- La subestación de menor resistencia a tierra (nodo 2) recibe la mayor corriente.
- 🎯 **Por qué importa:** Una subestación con una corriente de tierra alta puede saturar un transformador. La decisión central: ¿cómo se reparte la corriente inducida entre las subestaciones?
- 🔗 **Se estudia junto con:** análisis nodal, conductancia, fuente en serie, conservación.

📘 **Dónde se aprende** (1 clase): [B33-C07 · Impactos del clima espacial en redes eléctricas](../programa/clases/B33/B33-C07-impactos-del-clima-espacial-en-redes-electricas/CLASE.md).

### Corriente eléctrica

- La corriente eléctrica `I` es la carga que atraviesa una sección por unidad de tiempo, `I = ΔQ/Δt`; se mide en amperios (`1 A = 1 C/s`).

💡 **Contexto en la clase [B05-C16](../programa/clases/B05/B05-C16-corriente-y-circuitos-elementales/CLASE.md):**
- **Idea central (modelo mental):** Piensa en tuberías: la tensión es la diferencia de presión, la corriente es el caudal y la resistencia es el estrechamiento. La energía que entrega la fuente se disipa en las resistencias.
- 🎯 **Por qué importa:** Un satélite recibe energía del Sol mediante paneles, la guarda en baterías y la reparte a equipos; si el cálculo está mal, la nave se apaga en el eclipse. La pregunta motivadora es: ¿cómo calcular corrientes, tensiones y potencias en una red de componentes y cuánta energía debe guardarse para pasar un eclipse?
- 🔗 **Se estudia junto con:** tensión, resistencia, ley de Ohm, potencia.

📘 **Dónde se aprende** (1 clase): [B05-C16 · Corriente y circuitos elementales](../programa/clases/B05/B05-C16-corriente-y-circuitos-elementales/CLASE.md).

### Corriente fotogenerada

- La corriente fotogenerada `I_ph` es proporcional a la irradiancia.

💡 **Contexto en la clase [B86-C02](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md):**
- 🎯 **Por qué importa:** La potencia de una celda no es un número fijo: depende de la tensión a la que se la haga trabajar y de su temperatura. Elegir mal el punto de operación o ignorar la temperatura del ala cambia la potencia entregada.
- 🔗 **Se estudia junto con:** corriente de saturación, factor de idealidad, resistencia en serie, punto de máxima potencia.

📘 **Dónde se aprende** (1 clase): [B86-C02 · Celdas solares](../programa/clases/B86/B86-C02-celdas-solares/CLASE.md).

### Corriente galvánica

- La corriente galvánica `I = ΔV/(Rp_a/A_a + Rp_c/A_c)` es la de la pila.

💡 **Cómo se explica en la clase [B84-C21](../programa/clases/B84/B84-C21-compatibilidad-quimica-y-galvanica-de-materiales/CLASE.md):**
- Calcular la corriente galvánica con un modelo de resistencias.
- El script [galvanica.py](galvanica.py) calcula `ΔV`, la corriente galvánica y la velocidad de corrosión según la relación de áreas (comprueba coincidencia entre la masa de Faraday y `ρ × espesor × área` (< 1e-12)).
- 🎯 **Por qué importa:** Un tornillo de acero inoxidable en un panel de aluminio puede corroerlo 90 veces más rápido que otro de aluminio, y la corrosión ocurre en tierra, antes del lanzamiento. La decisión central: ¿qué pares de materiales pueden ir en contacto y cómo debe ser la relación de áreas?
- 🔗 **Se estudia junto con:** potencial de corrosión, velocidad de corrosión, relación de áreas.

📘 **Dónde se aprende** (1 clase): [B84-C21 · Compatibilidad química y galvánica de materiales](../programa/clases/B84/B84-C21-compatibilidad-quimica-y-galvanica-de-materiales/CLASE.md).

### Corriente inducida

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B33-C06](../programa/clases/B33/B33-C06-corrientes-geomagneticas-inducidas-gic/CLASE.md):**
- Ejercicio 12. Integrador. Elabora tu *ficha de las corrientes inducidas*: campo, serie temporal y corriente.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de las corrientes inducidas*: campo, serie temporal y corriente.
- 🎯 **Por qué importa:** El campo eléctrico depende de la conductividad y de la frecuencia. La decisión central: ¿cuánto vale el campo geoeléctrico y la corriente en una línea para un campo magnético dado?
- 🔗 **Se estudia junto con:** semiespacio uniforme, impedancia de superficie, campo geoeléctrico, transformada discreta.

📘 **Dónde se aprende** (1 clase): [B33-C06 · Corrientes geomagnéticas inducidas (GIC)](../programa/clases/B33/B33-C06-corrientes-geomagneticas-inducidas-gic/CLASE.md).

### Corriente oscura

- La corriente oscura `D(T)` es la tasa de electrones térmicos por píxel.

💡 **Cómo se explica en la clase [B44-C07](../programa/clases/B44/B44-C07-corriente-oscura/CLASE.md):**
- Paso 3 · Resultado. La corriente oscura baja `6,34` veces.
- Evaluar una ley térmica de la corriente oscura.
- 🎯 **Por qué importa:** La oscuridad añade señal y ruido; saber cómo escala permite elegir temperatura y exposición. La decisión central: ¿cuánto hay que enfriar para que la corriente oscura deje de importar?
- 🔗 **Se estudia junto con:** energía de activación, temperatura de duplicación, ajuste lineal.

📘 **Dónde se aprende** (1 clase): [B44-C07 · Corriente oscura](../programa/clases/B44/B44-C07-corriente-oscura/CLASE.md).

### Corrimiento

- El corrimiento `z = Δλ/λ`.

💡 **Cómo se explica en la clase [B45-C12](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md):**
- Como la sirena de una ambulancia: el tono sube al acercarse y baja al alejarse; el corrimiento de las líneas es proporcional a la velocidad.
- Medir un corrimiento por correlación cruzada.
- 🎯 **Por qué importa:** Las velocidades radiales descubren planetas, binarias y la expansión del universo. La decisión central: ¿cómo se pasa de un corrimiento a una velocidad y con qué precisión?
- 🔗 **Se estudia junto con:** Doppler clásico, relativista, correlación cruzada, paso en velocidad.

📘 **Dónde se aprende** (1 clase): [B45-C12 · Efecto Doppler en espectros](../programa/clases/B45/B45-C12-efecto-doppler-en-espectros/CLASE.md).

### Corrimiento al rojo

- El corrimiento al rojo es ```text z = λ_obs / λ_reposo − 1 ``` y, para `z ≪ 1`, la velocidad radial aproximada es `v = c z`.

💡 **Contexto en la clase [B06-C17](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md):**
- **Idea central (modelo mental):** Cada elemento tiene un patrón propio de líneas, como una huella dactilar. Para identificarla no basta con una marca: se comparan varias marcas y sus separaciones. Si las marcas están desplazadas todas en la misma proporción, se trata de la misma huella corrida por el movimiento.
- 🎯 **Por qué importa:** En B01-C01 estimaste la velocidad de una galaxia con una sola línea, H-alfa en 662,9 nm. Pero ¿cómo se sabe que esa línea es H-alfa y no otra?
- 🔗 **Se estudia junto con:** espectro, espectro continuo, espectro de emisión, absorción.

📖 **Explicado a fondo:** [Corrimiento al rojo (redshift)](esencial/esencial-a-c.md#corrimiento-al-rojo-redshift) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B06-C17 · Espectros atómicos y moleculares](../programa/clases/B06/B06-C17-espectros-atomicos-y-moleculares/CLASE.md).

### Corrimiento al rojo cosmológico

- El corrimiento al rojo cosmológico `z` es el cambio fraccional de longitud de onda por la expansión.

💡 **Contexto en la clase [B26-C11](../programa/clases/B26/B26-C11-expansion-cosmica-y-ley-de-hubble-lemaitre/CLASE.md):**
- **Idea central (modelo mental):** Dibuja puntos sobre una goma y estírala: todos se alejan de todos, y los más lejanos se alejan más deprisa porque entre ellos hay más goma que se estira.
- 🎯 **Por qué importa:** `H₀` fija la escala de distancias del universo y su edad aproximada, y hoy su valor depende de cómo se mida (C23). Para entender esa discusión hay que saber ajustar la ley a datos con dispersión, cuándo vale `v = cz` y qué incertidumbre se arrastra.
- 🔗 **Se estudia junto con:** ley de Hubble–Lemaître, constante de Hubble, tiempo de Hubble, velocidad peculiar.

📘 **Dónde se aprende** (1 clase): [B26-C11 · Expansión cósmica y ley de Hubble-Lemaître](../programa/clases/B26/B26-C11-expansion-cosmica-y-ley-de-hubble-lemaitre/CLASE.md).

### Corrimiento de transición

- El corrimiento de transición `z_t` es aquel en que `ä = 0`.

💡 **Cómo se explica en la clase [B26-C13](../programa/clases/B26/B26-C13-modelo-flrw-relatividad-y-cosmologia/CLASE.md):**
- Calcular el parámetro de deceleración y el corrimiento de transición.
- 🎯 **Por qué importa:** La edad del universo, la distancia a una galaxia y el calendario de su historia salen de la ecuación de Friedmann. Con ella se interpreta cualquier parámetro cosmológico.
- 🔗 **Se estudia junto con:** factor de escala, ecuación de Friedmann, densidad crítica, parámetro de densidad.

📘 **Dónde se aprende** (1 clase): [B26-C13 · Modelo FLRW — Relatividad y cosmología](../programa/clases/B26/B26-C13-modelo-flrw-relatividad-y-cosmologia/CLASE.md).

### Corrimiento exacto

- El corrimiento exacto (Schwarzschild) es `1 + z = 1/√(1 − r_s/R)`.

💡 **Cómo se explica en la clase [B26-C10](../programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/CLASE.md):**
- Ejercicio 5. Corrimiento exacto de la estrella de neutrones.
- Ejercicio 12 · integrador. Elabora tu *tabla de corrimientos*: calcula `z` exacto y débil para cuatro cuerpos, el error de la serie, la velocidad equivalente y la razón suelo–órbita; interpreta la prueba Galileo.
- 🎯 **Por qué importa:** El corrimiento gravitacional ajusta los relojes de los satélites de navegación, contamina la medida de velocidades en enanas blancas y revela la compacidad de las estrellas de neutrones. La decisión central: dada la compacidad de un cuerpo, ¿cuánto vale el corrimiento de su luz y cuándo falla la aproximación de campo débil?
- 🔗 **Se estudia junto con:** corrimiento gravitacional al rojo, emisor estático, serie de campo débil, velocidad equivalente.

📘 **Dónde se aprende** (1 clase): [B26-C10 · Desplazamiento gravitacional al rojo](../programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/CLASE.md).

### Corrimiento gravitacional al rojo

- El corrimiento gravitacional al rojo es el cambio de frecuencia de la luz al subir en un campo.
- El corrimiento gravitacional al rojo es el aumento de longitud de onda de la luz al salir de un pozo de potencial.

💡 **Cómo se explica en la clase [B26-C10](../programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/CLASE.md):**
- python programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/corrimientos.py
- 🎯 **Por qué importa:** El corrimiento gravitacional ajusta los relojes de los satélites de navegación, contamina la medida de velocidades en enanas blancas y revela la compacidad de las estrellas de neutrones. La decisión central: dada la compacidad de un cuerpo, ¿cuánto vale el corrimiento de su luz y cuándo falla la aproximación de campo débil?
- 🔗 **Se estudia junto con:** emisor estático, corrimiento exacto, serie de campo débil, velocidad equivalente.

📘 **Dónde se aprende** (2 clases): [B26-C06 · Principio de equivalencia](../programa/clases/B26/B26-C06-principio-de-equivalencia/CLASE.md); [B26-C10 · Desplazamiento gravitacional al rojo](../programa/clases/B26/B26-C10-desplazamiento-gravitacional-al-rojo/CLASE.md).

### Corrupción

- La corrupción es una alteración involuntaria de los bytes.
- La corrupción es el cambio de un elemento a una versión errónea.

💡 **Cómo se explica en la clase [B14-C11](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md):**
- Detectar la corrupción de un solo bit y la modificación de un único valor.
- El script [versiones_de_datos.py](versiones_de_datos.py) implementa un almacén direccionado por contenido con SHA-256, comprueba el vector de prueba del NIST, inserta dos versiones y un duplicado, usa manifiestos como versiones, localiza el cambio, detecta la corrupción de un bit y mide el efecto avalancha.
- 🎯 **Por qué importa:** Un análisis usó «la tabla de catálogo de octubre». En noviembre alguien reemplazó el archivo por otro con el mismo nombre.
- 🔗 **Se estudia junto con:** suma de verificación, función de hash criptográfica, direccionamiento por contenido, deduplicación.

📘 **Dónde se aprende** (2 clases): [B14-C11 · Control de versiones de datos](../programa/clases/B14/B14-C11-control-de-versiones-de-datos/CLASE.md); [B133-C02 · Narrativas orales y transmisión del saber del cielo](../programa/clases/B133/B133-C02-narrativas-orales-y-transmision-del-saber-del-cielo/CLASE.md).

### Corte

- Un corte es la masa donde cambia el índice.
- Un corte (sección) fija una variable y deja la otra libre.
- Acuerdo entre revisores: cuánto coinciden entre sí. Corte: fracción que se financia.

💡 **Cómo se explica en la clase [B09-C15](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md):**
- B --> D["Cada corte es una<br/>función de una variable"]
- Paso 3 · Corte a lo largo de `x`. A `±5000 km`: `−1,2818` y `−1,2824`, ambos menores.
- 🎯 **Por qué importa:** Una sonda que viaja de la Tierra a la Luna se mueve en un campo de potencial que depende de dos coordenadas del plano. Dónde están los puntos de equilibrio y qué forma tiene el campo alrededor de ellos se lee en un mapa de curvas de nivel.
- 🔗 **Se estudia junto con:** función de dos variables, dominio, gráfica, curva de nivel.

📘 **Dónde se aprende** (3 clases): [B09-C15 · Funciones de varias variables](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md); [B38-C02 · Función inicial de masa y su universalidad](../programa/clases/B38/B38-C02-funcion-inicial-de-masa-y-su-universalidad/CLASE.md); [B48-C03 · Propuestas científicas y criterios](../programa/clases/B48/B48-C03-propuestas-cientificas-y-criterios/CLASE.md).

### Corte de energía

- Un corte de energía interrumpe la escritura en un byte.

💡 **Cómo se explica en la clase [B88-C35](../programa/clases/B88/B88-C35-reinicio-en-caliente-y-persistencia-de-estado/CLASE.md):**
- La evidencia es la prueba exhaustiva de corte de energía del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *prueba exhaustiva de corte de energía*: registro, esquema, cortes, resultados y lista de qué es sintético.
- 🎯 **Por qué importa:** Un corte durante una escritura deja un registro a medias. La decisión central: ¿qué esquema garantiza que, cortes donde cortes, siempre haya un estado válido recuperable?
- 🔗 **Se estudia junto con:** doble búfer, secuencia, CRC-16, recuperación.

📘 **Dónde se aprende** (1 clase): [B88-C35 · Reinicio en caliente y persistencia de estado](../programa/clases/B88/B88-C35-reinicio-en-caliente-y-persistencia-de-estado/CLASE.md).

### Corte GZK

- El corte GZK es el límite por interacción con el fondo.

💡 **Contexto en la clase [B31-C13](../programa/clases/B31/B31-C13-rayos-cosmicos-y-cascadas/CLASE.md):**
- **Idea central (modelo mental):** Una partícula se parte en dos, cada una en dos más, hasta que la energía por partícula baja del umbral crítico y la avalancha se apaga.
- 🎯 **Por qué importa:** La energía y la composición de un rayo cósmico se infieren de la forma de su cascada, y el fondo de microondas limita la energía que llega. La decisión central: ¿qué profundidad y tamaño tiene una cascada y a qué energía aparece un corte?
- 🔗 **Se estudia junto con:** cascada, energía crítica, profundidad del máximo, tasa de elongación.

📘 **Dónde se aprende** (1 clase): [B31-C13 · Rayos cósmicos y cascadas](../programa/clases/B31/B31-C13-rayos-cosmicos-y-cascadas/CLASE.md).

### Corteza

- La corteza es la capa superior de un cuerpo diferenciado.

💡 **Cómo se explica en la clase [B61-C07](../programa/clases/B61/B61-C07-cuencas-multianillo-y-grandes-impactos/CLASE.md):**
- Con profundidad de excavación ilustrativa 0,1 D y corteza de 40 km: 300 km → 30 km (corteza); 600 km → 60 km (manto); 1000 km → 100 km (manto).
- Comparar una profundidad de excavación ilustrativa con el espesor de la corteza.
- 🎯 **Por qué importa:** Las cuencas dejan huella en la corteza entera. La decisión central: ¿cómo se espacian los anillos, qué proyectil implica una cuenca y cuándo excava hasta el manto?
- 🔗 **Se estudia junto con:** cuenca multianillo, espaciado radial, protocuenca, profundidad de excavación.

📘 **Dónde se aprende** (1 clase): [B61-C07 · Cuencas multianillo y grandes impactos](../programa/clases/B61/B61-C07-cuencas-multianillo-y-grandes-impactos/CLASE.md).

### Cortisol relativo

- El cortisol relativo `C` es adimensional.

💡 **Contexto en la clase [B105-C22](../programa/clases/B105/B105-C22-sistema-neuroendocrino-y-respuesta-al-estres-en-vuelo/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR R["reloj: A cos"] --> U["entrada u(t)"] S["estresor S(t)"] --> U U --> P["produccion a u/(1+g C)"] P --> C["cortisol C"] C --> F["eliminacion C/tau"] C --> P ``` *Descripción textual:* el reloj y el estresor forman la entrada; la producción se frena cuando el cortisol sube (retroalimentación) y se elimina con una constante `τ`.
- 🎯 **Por qué importa:** Una medición de cortisol sin hora del día no se interpreta: el ritmo diario domina. Y un estresor crónico cambia el nivel medio de una forma distinta que uno agudo.
- 🔗 **Se estudia junto con:** entrada, ganancia de retroalimentación, semivida, estresor agudo.

📘 **Dónde se aprende** (1 clase): [B105-C22 · Sistema neuroendocrino y respuesta al estrés en vuelo](../programa/clases/B105/B105-C22-sistema-neuroendocrino-y-respuesta-al-estres-en-vuelo/CLASE.md).

### Cosmovisión

- Una cosmovisión es la manera en que una sociedad entiende el mundo y su lugar en él, y la astronomía es una de las formas en que se expresa.

💡 **Cómo se explica en la clase [B02-C05](../programa/clases/B02/B02-C05-cosmovisiones-andinas-del-cielo/CLASE.md):**
- Esta relación entre cielo y ciclo biológico es un ejemplo de lo que significa una cosmovisión: el cielo y la vida están conectados en una misma explicación.
- Para Machu Picchu, un artículo propone reinterpretarlo como centro de peregrinación ligado a la cosmovisión inca, en lugar de residencia real de Pachacuti, analizando el entorno y los ciclos celestes (S4).
- 🎯 **Por qué importa:** Hablar de «astronomía andina» en singular es un error: los Andes reúnen sociedades de épocas y regiones muy distintas. La pregunta motivadora es: ¿cómo se estudia respetuosamente un cielo que otra cultura leyó de otra manera, sin imponerle nuestras categorías y sin inventar lo que las fuentes no dicen?
- 🔗 **Se estudia junto con:** huaca, solsticio, constelación oscura, orto helíaco.

📘 **Dónde se aprende** (1 clase): [B02-C05 · Cosmovisiones andinas del cielo](../programa/clases/B02/B02-C05-cosmovisiones-andinas-del-cielo/CLASE.md).

### Coste

- El coste es el número de evaluaciones de la fuerza: leapfrog `1` por paso, Yoshida `3`.
- Un criterio de beneficio es mejor cuanto mayor; uno de coste es mejor cuanto menor.
- El coste se cuenta en operaciones de punto flotante por paso.

💡 **Cómo se explica en la clase [B73-C20](../programa/clases/B73/B73-C20-proyecto-de-integracion-celeste-de-precision/CLASE.md):**
- *Descripción textual:* los requisitos fijan un presupuesto frente al error de modelo; la convergencia da el paso requerido de cada integrador; el coste decide cuál usar.
- Por coste: evaluaciones para el presupuesto.
- 🎯 **Por qué importa:** Una integración «de precisión» no es la que usa el paso más pequeño sino la que mantiene el error numérico por debajo de la incertidumbre del modelo, con el menor coste. Sin ese presupuesto se gasta cómputo sin ganar exactitud o se afirma una exactitud que no existe.
- 🔗 **Se estudia junto con:** presupuesto de error, convergencia, error de modelo, paso requerido.

📘 **Dónde se aprende** (3 clases): [B73-C20 · Proyecto de integración celeste de precisión](../programa/clases/B73/B73-C20-proyecto-de-integracion-celeste-de-precision/CLASE.md); [B74-C18 · Estimación autónoma a bordo](../programa/clases/B74/B74-C18-estimacion-autonoma-a-bordo/CLASE.md); [B95-C03 · Selección y comparación de plataformas](../programa/clases/B95/B95-C03-seleccion-y-comparacion-de-plataformas/CLASE.md).

### Coste asimétrico

- El coste asimétrico pondera más un error que el otro.

💡 **Contexto en la clase [B119-C17](../programa/clases/B119/B119-C17-conflictos-y-normas-humanitarias-aplicables/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR X["Indicador observable x"] --> P["P(militar | x) (Bayes)"] P --> T{"≥ t ?"} T -->|sí| M["Tratar como militar"] T -->|no| C["Presumir civil"] K["Costes de error"] --> U["Umbral óptimo t*"] U --> T ``` *Descripción textual:* el indicador da una probabilidad posterior que se compara con un umbral fijado por los costes de error.
- 🎯 **Por qué importa:** C11 trata los límites militares del tratado; esta clase aborda cómo razonar la distinción bajo incertidumbre, un tema que ninguna clase del bloque cubre y que exige cautela jurídica. La decisión central: ¿cómo cambia el umbral de decisión cuando equivocarse en un sentido es mucho más grave que en el otro?
- 🔗 **Se estudia junto con:** Doble uso, umbral, falso positivo, presunción protectora.

📘 **Dónde se aprende** (1 clase): [B119-C17 · Conflictos y normas humanitarias aplicables](../programa/clases/B119/B119-C17-conflictos-y-normas-humanitarias-aplicables/CLASE.md).

### Coste de arranque

- El coste de arranque es el tiempo de crear procesos y copiar datos.

💡 **Cómo se explica en la clase [B14-C13](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md):**
- Decisión. Para esta tarea de poco más de un segundo, no compensa; sí compensaría con trozos cien veces más largos, donde el coste de arranque es una fracción pequeña.
- Límites: los tiempos cambian en cada ejecución y en cada máquina; en Linux, con `fork`, el coste de arranque sería menor; no se probaron hilos; el ajuste de `s` usa tres puntos.
- 🎯 **Por qué importa:** Un análisis de miles de simulaciones tarda una noche. Tienes ocho núcleos.
- 🔗 **Se estudia junto con:** proceso, hilo, GIL, trabajador.

📘 **Dónde se aprende** (1 clase): [B14-C13 · Computación paralela](../programa/clases/B14/B14-C13-computacion-paralela/CLASE.md).

### Coste de celda

- El coste de celda es `1 + w_s (pendiente/límite)² + w_r (rugosidad/límite)` y es infinito si se supera algún umbral.

💡 **Cómo se explica en la clase [B102-C08](../programa/clases/B102/B102-C08-traversabilidad-y-evaluacion-de-riesgo-de-terreno/CLASE.md):**
- Dijkstra con 8 vecinos y paso `Δx √2` o `Δx` por la media de los costes de las dos celdas encuentra una ruta de `56` celdas, `122,4 m` y coste `257,1`, frente a `99,0 m` en línea recta (`23,6 %` más larga).
- Endurecer el límite de `30°` a `20°` triplica las celdas prohibidas y sube el coste de la ruta un `18,5 %`, aunque la geometría de la ruta no cambia.
- 🎯 **Por qué importa:** Elegir la ruta es elegir qué riesgo se acepta. La decisión central: ¿qué celdas son intransitables, cuánto cuesta cruzar las demás y cuánto se alarga la ruta de mínimo riesgo respecto de la recta?
- 🔗 **Se estudia junto con:** pendiente, altura de obstáculo, rugosidad, ruta de mínimo coste.

📘 **Dónde se aprende** (1 clase): [B102-C08 · Traversabilidad y evaluación de riesgo de terreno](../programa/clases/B102/B102-C08-traversabilidad-y-evaluacion-de-riesgo-de-terreno/CLASE.md).

### Coste de trazado

- El coste de trazado es `Σ f·d`.

💡 **Cómo se explica en la clase [B109-C02](../programa/clases/B109/B109-C02-zonificacion-y-distribucion-funcional-de-modulos-de-un-habitat/CLASE.md):**
- *Descripción textual:* las zonas y sus flujos definen un coste; una cuadrícula fija las posiciones posibles; la enumeración de todas las permutaciones da el mejor trazado, que se compara con los trazados al azar.
- Calcular el coste de un trazado como suma de flujo por distancia.
- 🎯 **Por qué importa:** Un buen plano ahorra pasos, separa lo sucio de lo limpio y deja las zonas tranquilas lejos de las ruidosas. La decisión central: ¿dónde pongo cada zona para que los recorridos frecuentes sean cortos y las zonas incompatibles estén lejos?
- 🔗 **Se estudia junto con:** zona, flujo, adyacencia, incompatibilidad.

📘 **Dónde se aprende** (1 clase): [B109-C02 · Zonificación y distribución funcional de módulos de un hábitat](../programa/clases/B109/B109-C02-zonificacion-y-distribucion-funcional-de-modulos-de-un-habitat/CLASE.md).

### Costo

- El costo se mide aquí como número de comparaciones.
- El costo es `C(φ, T) = v∞,sal + v∞,lleg` en km/s.
- El costo de un par es tiempo de viaje más trabajo.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B07-C18](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md):**
- Casos: lista vacía, un elemento, repetidos, ya ordenada (mínimo costo de inserción), inversa (máximo), y listas aleatorias contrastadas con `sorted`.
- Contar comparaciones para medir el costo sin depender de la velocidad del equipo.
- 🎯 **Por qué importa:** Un catálogo estelar tiene millones de objetos. Buscar uno a uno es posible con diez planetas y ruinoso con diez millones.
- 🔗 **Se estudia junto con:** búsqueda lineal, búsqueda binaria, ordenada, ordenamiento por inserción.

📘 **Dónde se aprende** (4 clases): [B07-C18 · Algoritmos de búsqueda y ordenamiento](../programa/clases/B07/B07-C18-algoritmos-de-busqueda-y-ordenamiento/CLASE.md); [B33-C05 · Comunicación de riesgo y alertas de clima espacial](../programa/clases/B33/B33-C05-comunicacion-de-riesgo-y-alertas-de-clima-espacial/CLASE.md); [B75-C12 · Optimización de trayectoria](../programa/clases/B75/B75-C12-optimizacion-de-trayectoria/CLASE.md); [B97-C09 · Robótica colaborativa](../programa/clases/B97/B97-C09-robotica-colaborativa/CLASE.md).

### Costo cuadrático

- El costo cuadrático es `C = ∫₀^∞ (xᵀ Q x + uᵀ R u) dt` con `Q` simétrica semidefinida positiva y `R` simétrica definida positiva.

💡 **Cómo se explica en la clase [B16-C15](../programa/clases/B16/B16-C15-control-optimo-lqr/CLASE.md):**
- Es el amortiguamiento del filtro de Butterworth de segundo orden; el costo cuadrático con `Q = diag(q, 0)` lleva a él.
- Límite: el costo cuadrático penaliza mucho los picos y poco los ruidos pequeños; puede no reflejar un límite físico estricto.
- 🎯 **Por qué importa:** Con un PD hay dos perillas, `Kp` y `Kd`, y no es obvio cuánto esfuerzo gasta cada combinación. En un satélite el esfuerzo tiene un costo real: energía de las ruedas, momento almacenado, desgaste.
- 🔗 **Se estudia junto con:** LQR, ecuación algebraica de Riccati.

📘 **Dónde se aprende** (1 clase): [B16-C15 · Control óptimo LQR](../programa/clases/B16/B16-C15-control-optimo-lqr/CLASE.md).

### Costo de espera

- El costo de espera es el gasto adicional por cada año extra.

💡 **Cómo se explica en la clase [B124-C06](../programa/clases/B124/B124-C06-financiamiento-publico/CLASE.md):**
- Si cada año extra cuesta 6 % del total, el costo de espera es `6,0` uc (`6,0` % del total), un supuesto sintético.
- *Descripción textual:* cada año se gasta lo menor entre el tope y lo pendiente; lo que no se paga queda como atraso, que define el año de término y el costo de espera, y todo se comprueba con una fórmula del mínimo.
- 🎯 **Por qué importa:** Un proyecto puede estar bien estimado y aun así fallar porque el dinero no llega al ritmo que necesita. La decisión central: ¿qué tope anual evita el atraso y cuánto cuesta cada año de espera?
- 🔗 **Se estudia junto con:** demanda acumulada, tope, atraso, comprometido.

📘 **Dónde se aprende** (1 clase): [B124-C06 · Financiamiento público](../programa/clases/B124/B124-C06-financiamiento-publico/CLASE.md).

### Costo del operador

- El costo del operador es las primas más las pérdidas que él retiene.

💡 **Cómo se explica en la clase [B127-C08](../programa/clases/B127/B127-C08-simulacion-de-cobertura-de-seguros-para-una-mision/CLASE.md):**
- *Descripción textual:* el mismo conjunto de eventos aleatorios se aplica a cuatro estrategias que añaden coberturas de a una; para cada una se simula el costo del operador y se resumen su media, su desviación, su cuantil 99 % y la probabilidad de superar `60 MUSD`.
- Límite: aquí el operador es neutral al costo de capital y no hay efectos de segundo orden, como la caída del negocio tras una pérdida.
- 🎯 **Por qué importa:** Integrar los seguros de una misión en un caso permite practicar la decisión; no existía tal caso. La decisión central: ¿cuánto se paga de más por reducir el riesgo y qué riesgo se está dispuesto a retener?
- 🔗 **Se estudia junto con:** estrategia, pérdida retenida, riesgo retenido, autoseguro.

📘 **Dónde se aprende** (1 clase): [B127-C08 · Simulación de cobertura de seguros para una misión](../programa/clases/B127/B127-C08-simulacion-de-cobertura-de-seguros-para-una-mision/CLASE.md).

### Costo esperado

- Un costo esperado pondera cada tipo de error por su costo.

💡 **Cómo se explica en la clase [B17-C12](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md):**
- Costo esperado: el que lleva a una decisión; exige conocer costos.
- Elegir un umbral minimizando un costo esperado.
- 🎯 **Por qué importa:** Un modelo marca candidatos a planeta, y cada alerta cuesta horas de revisión. Si el modelo acierta el 99 % en una muestra donde el 99 % son negativos, no dice nada útil.
- 🔗 **Se estudia junto con:** matriz de confusión, verdaderos positivos, falsos positivos, verdaderos negativos.

📘 **Dónde se aprende** (1 clase): [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md).

### Costo fijo

- El costo fijo `F` se paga siempre; el variable `v`, por producto; el escalonado `S` se suma por cada tramo de capacidad `cap`.

💡 **Cómo se explica en la clase [B124-C22](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md):**
- F["costo fijo F"] --> C["C(Q) = F + vQ + S ⌈Q/cap⌉"]
- *Descripción textual:* los costos fijo, variable y escalonado forman el costo total, del que salen el costo medio, el precio con margen y el equilibrio; la incertidumbre de la demanda se evalúa con dos métodos.
- 🎯 **Por qué importa:** B124 trata financiamiento, pero un servicio sostenible depende de un modelo de costo que explique cómo cambia el costo medio con el volumen. La decisión central: ¿a qué precio y con qué volumen el servicio cubre sus costos, y cuánto riesgo tiene si la demanda varía?
- 🔗 **Se estudia junto con:** variable, escalonado, costo medio, margen sobre precio.

📘 **Dónde se aprende** (1 clase): [B124-C22 · Modelo de costo de un servicio de datos](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md).

### Costo más incentivo (CPIF)

- Precio fijo (FFP): el pago no depende del costo real. Costo más incentivo (CPIF): se paga el costo real más un honorario que baja cuando el costo supera el objetivo.

💡 **Cómo se explica en la clase [B124-C10](../programa/clases/B124/B124-C10-contratos-y-compras-espaciales/CLASE.md):**
- Ninguno es mejor en sí: depende de qué tan bien se conoce el costo, y el modelo no incluye incentivos a ocultar costos ni renegociaciones.
- Describir un contrato de precio fijo y uno de costo más honorario con incentivo.
- 🎯 **Por qué importa:** El tipo de contrato reparte el riesgo de sobrecosto entre quien compra y quien vende. La decisión central: ¿cuánto riesgo asume cada parte con cada tipo de contrato y cuánto cuesta ese reparto en promedio?
- 🔗 **Se estudia junto con:** Precio fijo (FFP), honorario objetivo, razón de reparto, techo.

📘 **Dónde se aprende** (1 clase): [B124-C10 · Contratos y compras espaciales](../programa/clases/B124/B124-C10-contratos-y-compras-espaciales/CLASE.md).

### Costo medio

- El costo medio es `C(Q)/Q`.

💡 **Cómo se explica en la clase [B124-C22](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md):**
- Con margen sobre precio de 25 %, `p = costo medio/0,75`: `78,67` um a 1 000, `37,60` a 2 500 y `23,20` a 5 000 productos.
- *Descripción textual:* los costos fijo, variable y escalonado forman el costo total, del que salen el costo medio, el precio con margen y el equilibrio; la incertidumbre de la demanda se evalúa con dos métodos.
- 🎯 **Por qué importa:** B124 trata financiamiento, pero un servicio sostenible depende de un modelo de costo que explique cómo cambia el costo medio con el volumen. La decisión central: ¿a qué precio y con qué volumen el servicio cubre sus costos, y cuánto riesgo tiene si la demanda varía?
- 🔗 **Se estudia junto con:** costo fijo, variable, escalonado, margen sobre precio.

📘 **Dónde se aprende** (1 clase): [B124-C22 · Modelo de costo de un servicio de datos](../programa/clases/B124/B124-C22-modelo-de-costo-de-un-servicio-de-datos/CLASE.md).

### Costo neto

- El costo neto es pérdida retenida más prima de reaseguro.

💡 **Cómo se explica en la clase [B127-C07](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md):**
- Costo neto medio: `0,70 × 67,745 + 18,00 = 65,42`.
- Costo neto medio `74,58`: cuesta `6,8 MUSD` más que no reasegurar, a cambio de desviación `76,9` y cuantil 99 % `336,8`.
- 🎯 **Por qué importa:** El riesgo espacial se reparte mediante reaseguro; no había clase al respecto. La decisión central: ¿qué parte del riesgo se cede y cuánto cuesta reducir la cola?
- 🔗 **Se estudia junto con:** cesión, cuota parte, exceso de pérdida, prioridad.

📘 **Dónde se aprende** (1 clase): [B127-C07 · Reaseguro espacial](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md).

### Costo nivelado (LCOP)

- El costo nivelado (LCOP) es `(CapEx·CRF + OpEx)/Q`.

💡 **Cómo se explica en la clase [B124-C24](../programa/clases/B124/B124-C24-capex-y-opex-de-una-instalacion-extraterrestre/CLASE.md):**
- *Descripción textual:* el equipo y su transporte forman el CapEx, que se convierte en anualidad y se suma al OpEx para dar el costo anual y el costo nivelado, que se verifica con valor actual y se compara con traer el producto.
- Descripción larga: el transporte domina el capital y la operación, y el costo nivelado es una pequeña fracción del de traer el producto, siempre que la producción llegue a lo planificado.
- 🎯 **Por qué importa:** B124 estima costos de misión, pero una instalación que opera años necesita separar el capital de la operación y ponerlos en una misma unidad. La decisión central: ¿a qué costo por kilogramo produce la instalación y desde qué producción conviene frente a traer el producto?
- 🔗 **Se estudia junto con:** CapEx, OpEx, factor de recuperación de capital, valor actual.

📘 **Dónde se aprende** (1 clase): [B124-C24 · CapEx y OpEx de una instalación extraterrestre](../programa/clases/B124/B124-C24-capex-y-opex-de-una-instalacion-extraterrestre/CLASE.md).

### Costo por kilogramo

- El costo por kilogramo es el precio dividido por la carga útil.

💡 **Cómo se explica en la clase [B124-C23](../programa/clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md):**
- El costo por kilogramo es el precio dividido por una fracción pequeña: cualquier mejora de la fracción mejora el costo en la misma proporción.
- El descenso desde órbita baja (`Δv = 6 000 m/s`, `Isp` 340 s, `e = 0,12`) deja una fracción de `0,05157`, así que cada kilogramo en superficie exige `1/0,05157` kg en órbita: el costo sube a `87176` um/kg (`19,4` veces); con reutilización, `61024`.
- ⚠️ **Error frecuente:** Tomar un costo por kilogramo como un dato universal. Se corrige con la sección 10 y el ejercicio 11.
- 🎯 **Por qué importa:** El costo por kilogramo a superficie no se puede leer en una lista de precios: depende de una cadena de fracciones de masa que se multiplican. La decisión central: ¿cuánto cuesta llevar un kilogramo a la superficie, de qué depende ese costo y qué lo hace más sensible?
- 🔗 **Se estudia junto con:** ecuación del cohete, razón de masas, coeficiente estructural, fracción de carga útil.

📘 **Dónde se aprende** (1 clase): [B124-C23 · Costos de transporte por kilogramo a superficie](../programa/clases/B124/B124-C23-costos-de-transporte-por-kilogramo-a-superficie/CLASE.md).

### Costo por metro

- El costo por metro es el `Δv` entre el cambio de posición.

💡 **Cómo se explica en la clase [B76-C11](../programa/clases/B76/B76-C11-operaciones-de-aproximacion/CLASE.md):**
- Comparar el costo por metro de tramos de distinta duración.
- Ejercicio 2 · con una pista. Calcula el costo por metro del tramo 1.
- 🎯 **Por qué importa:** Una aproximación a baja velocidad no puede depender de que todos los impulsos se ejecuten. La decisión central: ¿cuántos tramos usar, cuánto cuestan y qué ocurre si el segundo impulso de un tramo falla?
- 🔗 **Se estudia junto con:** salto V-bar, aproximación R-bar, seguridad pasiva, esfera de exclusión.

📘 **Dónde se aprende** (1 clase): [B76-C11 · Operaciones de aproximación](../programa/clases/B76/B76-C11-operaciones-de-aproximacion/CLASE.md).

### Costo por suscriptor-mes

- El costo por suscriptor-mes es el costo anual repartido en suscriptores y meses.

💡 **Cómo se explica en la clase [B124-C11](../programa/clases/B124/B124-C11-sostenibilidad-economica-de-constelaciones/CLASE.md):**
- Con 100 000 suscriptores el ingreso es `60,0` Mum/año, el margen `21,100` Mum/año y el costo por suscriptor-mes `32,42` um; el despliegue se recupera en `4,27` años (sin descuento).
- *Descripción textual:* la flota y su vida dan la tasa de reposición, que se verifica por simulación; esta, más el costo operativo, da el costo anual y, con el ARPU, el equilibrio en suscriptores.
- 🎯 **Por qué importa:** Una constelación puede ser técnicamente exitosa y económicamente inviable si la reposición se come el margen. La decisión central: ¿cuántos suscriptores se necesitan para cubrir la reposición y la operación, y qué tan sensible es eso a la vida útil?
- 🔗 **Se estudia junto con:** reposición, tasa de renovación, reserva de desorbitación, ARPU.

📘 **Dónde se aprende** (1 clase): [B124-C11 · Sostenibilidad económica de constelaciones](../programa/clases/B124/B124-C11-sostenibilidad-economica-de-constelaciones/CLASE.md).

### Costo total

- El costo total es `J = m₀ + c_t·TOF`, con `m₀` en toneladas y `c_t` en unidades por día.

💡 **Cómo se explica en la clase [B75-C27](../programa/clases/B75/B75-C27-duracion-de-mision-y-tiempo-de-vuelo-como-restriccion/CLASE.md):**
- Por costo total: con `c_t` el óptimo se desplaza.
- Con un costo temporal ilustrativo de `0,02 u/d`, el costo total mínimo (masa en toneladas + tiempo) cae en `220 d`: se paga más masa (`4,512 t` en vez de `4,189 t`) para ahorrar 40 días.
- ⚠️ **Error frecuente:** Confundir el óptimo en delta-v con el óptimo en costo total. Se corrige con 8.3.
- 🎯 **Por qué importa:** Un viaje más corto gasta más combustible y uno más largo gasta más tiempo. La decisión central: ¿qué tiempo de vuelo minimiza el costo total cuando se pesan la masa lanzada y la duración?
- 🔗 **Se estudia junto con:** delta-v mínimo para un tiempo, curva de costo, óptimo.

📘 **Dónde se aprende** (1 clase): [B75-C27 · Duración de misión y tiempo de vuelo como restricción](../programa/clases/B75/B75-C27-duracion-de-mision-y-tiempo-de-vuelo-como-restriccion/CLASE.md).

### Costos

- Los costos se reparten por igual salvo decisión distinta (art.

💡 **Cómo se explica en la clase [B123-C03](../programa/clases/B123/B123-C03-mecanismos-de-reclamacion-entre-estados/CLASE.md):**
- Ejercicio 5 · autónomo. ¿Quién paga los costos de la comisión?
- 🎯 **Por qué importa:** Un derecho a reclamar se pierde o se debilita si no se ejerce por la vía y en el plazo previstos. La decisión central: ¿cuándo y cómo se presenta la reclamación, cuándo se puede pedir una comisión y qué valor tiene su decisión?
- 🔗 **Se estudia junto con:** presentación, plazo, comisión de reclamaciones.

📘 **Dónde se aprende** (1 clase): [B123-C03 · Mecanismos de reclamación entre Estados](../programa/clases/B123/B123-C03-mecanismos-de-reclamacion-entre-estados/CLASE.md).

### Costura

- Una costura es la línea de unión entre dos teselas.

💡 **Cómo se explica en la clase [B14-C27](../programa/clases/B14/B14-C27-procesamiento-por-teselas-de-grandes-volumenes-de-imagenes/CLASE.md):**
- Un píxel junto a la costura necesita hasta 2 píxeles de la tesela vecina.
- El laboratorio comprueba que todos esos píxeles están a 2 o menos píxeles de una costura interior: el error vive en las franjas de ancho `2R` alrededor de las costuras, no en el interior de las teselas.
- ⚠️ **Error frecuente:** Culpar al redondeo de un error de costuras. Se corrige con el ejercicio 11.
- 🎯 **Por qué importa:** Una cobertura global de imágenes ocupa terabytes y ningún equipo la carga entera. Para suavizarla, calcular un índice o detectar cambios hay que procesarla por pedazos.
- 🔗 **Se estudia junto con:** operación local, radio, borde, borde replicado.

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
- 🔗 **Se estudia junto con:** cifra significativa, Redondear, estimación, error de redondeo.

📘 **Dónde se aprende** (7 clases): [B03-C11 · Estimación y redondeo responsable](../programa/clases/B03/B03-C11-estimacion-y-redondeo-responsable/CLASE.md); [B03-C19 · Propagación elemental de redondeos](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md); [B27-C17 · Explosiones de rayos gamma](../programa/clases/B27/B27-C17-explosiones-de-rayos-gamma/CLASE.md); [B28-C01 · Fundamentos de mensajeros astronómicos](../programa/clases/B28/B28-C01-fundamentos-de-mensajeros-astronomicos/CLASE.md); [B53-C05 · Sistemas de coordenadas lunares](../programa/clases/B53/B53-C05-sistemas-de-coordenadas-lunares/CLASE.md); [B81-C12 · Restricciones dinámicas en optimización](../programa/clases/B81/B81-C12-restricciones-dinamicas-en-optimizacion/CLASE.md) y 1 más.

### Cota aproximada

- La cota aproximada supone `k × (celdas medias por campo)` celdas.

💡 **Cómo se explica en la clase [B28-C15](../programa/clases/B28/B28-C15-busqueda-de-contrapartidas-opticas/CLASE.md):**
- Comparar la cobertura con una cota aproximada y con la garantía `1 − 1/e`.
- Ejercicio 11 · transferencia. ¿Qué valida la comparación con la cota aproximada?
- 🎯 **Por qué importa:** Observar más campos cubre más probabilidad, pero cada campo recibe menos tiempo y es menos profundo. Si la fuente es débil, el exceso de campos hace que no se vea.
- 🔗 **Se estudia junto con:** teselado, algoritmo voraz, garantía 1 − 1/e, profundidad.

📘 **Dónde se aprende** (1 clase): [B28-C15 · Búsqueda de contrapartidas ópticas](../programa/clases/B28/B28-C15-busqueda-de-contrapartidas-opticas/CLASE.md).

### Cota de cortes mínimos

- La aproximación de evento raro suma las probabilidades de los cortes; la cota de cortes mínimos es `1 − Π(1 − P(cᵢ))`.

💡 **Cómo se explica en la clase [B83-C24](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md):**
- La enumeración exacta de los 128 estados da 0,016132; la inclusión–exclusión, 0,016132; la aproximación de evento raro, 0,016200 (un 0,42 % de más); la cota de cortes mínimos, 0,016132 (aquí coincide porque los cortes mínimos no comparten eventos);
- Comparar la aproximación de evento raro y la cota de cortes mínimos con el valor exacto.
- 🎯 **Por qué importa:** Un fallo combinado como «dos sensores fallan a la vez» no aparece en una lista de modos individuales. La decisión central: ¿qué combinaciones de fallos causan el evento no deseado, cuál es su probabilidad y qué evento básico conviene proteger primero?
- 🔗 **Se estudia junto con:** árbol de fallos, eventos básicos, conjunto de corte, mínimo.

📘 **Dónde se aprende** (1 clase): [B83-C24 · Árboles de fallos (FTA) y análisis de causas](../programa/clases/B83/B83-C24-arboles-de-fallos-fta-y-analisis-de-causas/CLASE.md).

### Cota de Cramér–Rao

- La matriz de información de Fisher es `F = Jᵀ J / σ²` (ruido gaussiano independiente); la cota de Cramér–Rao dice que la covarianza de cualquier estimador insesgado es al menos `F⁻¹`.
- La cota de Cramér–Rao es el límite de precisión.
- La cota de Cramér–Rao (CRB) dice que cualquier estimador sin sesgo cumple `Var(θ̂) ≥ 1/I(θ)`.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B15-C15](../programa/clases/B15/B15-C15-estimacion-de-parametros-senales-imagenes-y-estimacion-cientifica/CLASE.md):**
- *Descripción textual:* los datos con ruido alimentan un estimador; de su sesgo y su varianza sale el error cuadrático medio; la varianza de un estimador sin sesgo se compara con la cota de Cramér–Rao.
- Calcular la información de Fisher y la cota de Cramér–Rao.
- 🎯 **Por qué importa:** Un telescopio recoge 100 fotones de una estrella y quieres su posición con la mayor exactitud posible. ¿Basta con promediar las posiciones?
- 🔗 **Se estudia junto con:** parámetro, estimador, sesgo, varianza.

📘 **Dónde se aprende** (6 clases): [B15-C15 · Estimación de parámetros — Señales, imágenes y estimación científica](../programa/clases/B15/B15-C15-estimacion-de-parametros-senales-imagenes-y-estimacion-cientifica/CLASE.md); [B22-C03 · Identificabilidad de parámetros](../programa/clases/B22/B22-C03-identificabilidad-de-parametros/CLASE.md); [B29-C16 · Supernovas y curvas de luz](../programa/clases/B29/B29-C16-supernovas-y-curvas-de-luz/CLASE.md); [B46-C18 · VLBI y geodesia](../programa/clases/B46/B46-C18-vlbi-y-geodesia/CLASE.md); [B74-C03 · Medición de alcance por radio](../programa/clases/B74/B74-C03-medicion-de-alcance-por-radio/CLASE.md); [B74-C27 · Navegación por púlsares de rayos X como técnica de investigación](../programa/clases/B74/B74-C27-navegacion-por-pulsares-de-rayos-x-como-tecnica-de-investigacion/CLASE.md).

### Cota de escape

- La cota de escape es `√(2 f ε)`.
- La cota de escape `Vₑ_max = √(2ηε)` es el escape máximo con una fuente de energía específica `ε`.

💡 **Cómo se explica en la clase [B78-C16](../programa/clases/B78/B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md):**
- *Descripción textual:* la energía por reacción y la masa de los reactivos dan la energía específica; ésta da la fracción de masa convertida y, con la fracción dirigida, la cota de escape, que se contrasta con la relativista; con una potencia dada se calcula el consumo.
- Descripción larga: la energía por kilo de la fusión supera a la química en siete órdenes de magnitud; la cota de escape sigue siendo una fracción de la velocidad de la luz.
- 🎯 **Por qué importa:** Si la energía por kilo es millones de veces mayor, el escape posible es enorme; pero eso es una cota, no un propulsor. La decisión central: ¿cuánta energía por kilo libera cada reacción y cuánto escape acotaría, según la fracción que se logre dirigir?
- 🔗 **Se estudia junto con:** energía específica, fracción de masa convertida, fracción dirigida, fusión como investigación.

📘 **Dónde se aprende** (2 clases): [B78-C16 · Propulsión de fusión como investigación](../programa/clases/B78/B78-C16-propulsion-de-fusion-como-investigacion/CLASE.md); [B78-C18 · Energía específica y limitaciones](../programa/clases/B78/B78-C18-energia-especifica-y-limitaciones/CLASE.md).

### Cota de Liu y Layland

- La cota de Liu y Layland `U ≤ n(2^(1/n) − 1)` es suficiente para RM con plazos iguales a los períodos y tiende a `ln 2 = 0,6931`.

💡 **Contexto en la clase [B88-C06](../programa/clases/B88/B88-C06-planificacion-de-tareas-rtos/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR T["Conjunto de tareas"] --> B["Cota n(2^(1/n)-1)"] T --> RM["Simulacion RM"] T --> ED["Simulacion EDF"] B --> V["Veredicto"] RM --> V ED --> V ``` *Descripción textual:* cada conjunto se evalúa con la cota (solo suficiente) y con dos simulaciones; el veredicto cruza las tres. Analogía: RM es una fila con orden fijo por tamaño de tarea;
- 🎯 **Por qué importa:** Elegir la política determina cuánta CPU se puede usar con garantías. La decisión central: ¿RM basta, o se necesita EDF para el conjunto de tareas?
- 🔗 **Se estudia junto con:** EDF, cambio de contexto.

📘 **Dónde se aprende** (1 clase): [B88-C06 · Planificación de tareas RTOS](../programa/clases/B88/B88-C06-planificacion-de-tareas-rtos/CLASE.md).

### Cota de Liu–Layland

- La cota de Liu–Layland `n(2^(1/n) − 1)` es una condición suficiente de planificabilidad con prioridades por tasa.

💡 **Cómo se explica en la clase [B98-C07](../programa/clases/B98/B98-C07-arquitectura-de-autonomia-a-bordo-percepcion-decision-accion/CLASE.md):**
- Calcular la utilización de un conjunto de tareas periódicas y compararla con la cota de Liu–Layland.
- El script [tres_capas.py](tres_capas.py) calcula la utilización, la cota de Liu–Layland, el tiempo de respuesta de cada tarea por punto fijo y la probabilidad de plan tardío por Monte Carlo y por fórmula (comprueba `R ≤ T`, `U ≤` cota, latencia reflejo ≤ 0,5 s y concordancia Monte Carlo–fórmula < 0,005).
- 🎯 **Por qué importa:** Una arquitectura sin presupuesto de tiempos puede parecer correcta hasta que una tarea lenta retrasa un reflejo. La decisión central: ¿cada capa cumple sus plazos aunque las demás consuman su peor caso, y qué pasa cuando el planificador tarda más de lo previsto?
- 🔗 **Se estudia junto con:** capa reactiva, ejecutiva, deliberativa, Remote Agent.

📘 **Dónde se aprende** (1 clase): [B98-C07 · Arquitectura de autonomía a bordo (percepción-decisión-acción)](../programa/clases/B98/B98-C07-arquitectura-de-autonomia-a-bordo-percepcion-decision-accion/CLASE.md).

### Cota de peor caso

- La cota de peor caso supone que todos los errores actúan en la dirección más desfavorable.
- La cota de peor caso suma los máximos: `2 + 15 + 8 = 25 µs`.

💡 **Cómo se explica en la clase [B03-C19](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md):**
- La cota de peor caso, que considera todos los redondeos en la dirección peor, es `[29,745; 30,027] km/s`; la incertidumbre en cuadratura es `0,062 km/s`.
- Distinguir la cota de peor caso de la incertidumbre estándar en cuadratura, y usar `a/√3` para una distribución uniforme.
- ⚠️ **Error frecuente:** Confundir cota de peor caso con incertidumbre estándar. Ejercicio 11.
- 🎯 **Por qué importa:** Con los datos de la Tierra redondeados a tres cifras (semieje `1,50 × 10⁸ km` y período `365 d`), la rapidez orbital sale `29,89 km/s`. La NASA publica 29,78 km/s.
- 🔗 **Se estudia junto con:** error de redondeo, cota, error absoluto, error relativo.

📘 **Dónde se aprende** (2 clases): [B03-C19 · Propagación elemental de redondeos](../programa/clases/B03/B03-C19-propagacion-elemental-de-redondeos/CLASE.md); [B88-C26 · Latencia de interrupciones y jitter](../programa/clases/B88/B88-C26-latencia-de-interrupciones-y-jitter/CLASE.md).

### Cota de pila

- La cota de pila suma un marco por nivel de prioridad.

💡 **Cómo se explica en la clase [B88-C22](../programa/clases/B88/B88-C22-interrupciones-y-manejo-de-excepciones-en-el-computador-de-vuelo/CLASE.md):**
- Ejercicio 4 · autónomo. Calcula la cota de pila.
- Cota de pila (un marco por nivel) = 120 B ; observada con anidamiento = 80 B
- 🎯 **Por qué importa:** Las interrupciones fijan cuánto tarda el sistema en reaccionar y cuánta pila usa. La decisión central: ¿se permite que una interrupción de mayor prioridad interrumpa a otra, y qué cuesta eso en latencia y pila?
- 🔗 **Se estudia junto con:** latencia, tiempo de respuesta, anidamiento, pila máxima.

📘 **Dónde se aprende** (1 clase): [B88-C22 · Interrupciones y manejo de excepciones en el computador de vuelo](../programa/clases/B88/B88-C22-interrupciones-y-manejo-de-excepciones-en-el-computador-de-vuelo/CLASE.md).

### Cota de sección eficaz

- La cota de sección eficaz `σ < s_up/(εΦ)`.

💡 **Cómo se explica en la clase [B31-C18](../programa/clases/B31/B31-C18-restricciones-experimentales-de-teorias/CLASE.md):**
- *Descripción textual:* las observaciones y el fondo dan el límite por cada método; el límite se convierte en cota de sección eficaz y la cobertura se verifica por Monte Carlo.
- 🎯 **Por qué importa:** Un límite mal calculado puede excluir una teoría que no estaba excluida. La decisión central: ¿qué señal máxima es compatible con lo observado y cuán fiable es el método?
- 🔗 **Se estudia junto con:** límite superior, método clásico, bayesiano, fondo.

📘 **Dónde se aprende** (1 clase): [B31-C18 · Restricciones experimentales de teorías](../programa/clases/B31/B31-C18-restricciones-experimentales-de-teorias/CLASE.md).

### Cota de Sellke–Bayarri–Berger

- La cota de Sellke–Bayarri–Berger acota el `BF` a favor de la alternativa con `BF ≤ 1/(−e p ln p)` para `p < 1/e`.

💡 **Contexto en la clase [B132-C05](../programa/clases/B132/B132-C05-contexto-ritual-y-social-de-la-observacion-del-cielo/CLASE.md):**
- 🎯 **Por qué importa:** El catálogo trata alineaciones sin ese contexto. La decisión central: ¿cuánto apoyo da cada línea de evidencia a la intención de una alineación, y qué parte de la conclusión depende de lo que se supone de antemano?
- 🔗 **Se estudia junto con:** contexto ritual y social, línea de evidencia, factor de Bayes, descuento por dependencia.

📘 **Dónde se aprende** (1 clase): [B132-C05 · Contexto ritual y social de la observación del cielo](../programa/clases/B132/B132-C05-contexto-ritual-y-social-de-la-observacion-del-cielo/CLASE.md).

### Cota de unión

- Matriz de confusión: frecuencia de cada clasificación por causa verdadera. Cota de unión: `1 − Σ Q(dᵢⱼ/2)`.

💡 **Cómo se explica en la clase [B96-C29](../programa/clases/B96/B96-C29-diagnostico-de-fallas-de-enlace/CLASE.md):**
- La cota de unión `1 − Σ Q(d/2)` queda por debajo de cada acierto simulado (por ejemplo, 0,8191 frente a 0,8159 en apuntamiento, dentro de 0,01).
- Comparar el acierto con una cota inferior de unión.
- 🎯 **Por qué importa:** Perder tiempo de contacto buscando la causa equivocada es caro. La decisión central: ¿qué medidas distinguen las causas y cuáles se confunden entre sí?
- 🔗 **Se estudia junto con:** Firma, Diccionario de fallas, Mínima distancia, Matriz de confusión.

📘 **Dónde se aprende** (1 clase): [B96-C29 · Diagnóstico de fallas de enlace](../programa/clases/B96/B96-C29-diagnostico-de-fallas-de-enlace/CLASE.md).

### Cota de Δv

- La cota de Δv es el valor al que tiende la etapa con propelente infinito.

💡 **Cómo se explica en la clase [B78-C02](../programa/clases/B78/B78-C02-propulsion-quimica-como-sistema-fisico/CLASE.md):**
- Descripción larga: el Δv crece con el logaritmo de la razón de masas y tiene una cota que depende solo de la fracción de tanques y del `Isp`.
- Calcular la cota de Δv que impone la fracción de tanques.
- 🎯 **Por qué importa:** Más propelente da más Δv, pero cada kilo de propelente exige tanques, y esos tanques también se aceleran. La decisión central: ¿cuánto propelente hace falta para un Δv dado y existe un máximo de Δv que ninguna cantidad de propelente supera?
- 🔗 **Se estudia junto con:** ecuación del cohete, masa inicial, masa final, fracción de tanques.

📘 **Dónde se aprende** (1 clase): [B78-C02 · Propulsión química como sistema físico](../programa/clases/B78/B78-C02-propulsion-quimica-como-sistema-fisico/CLASE.md).

### Cota superior

- Eficiencia de recuperación: fracción recuperada por el hisopo. Cota superior: valor que, con confianza `CL`, no es menor que la densidad verdadera.
- Una cota superior acota por arriba.

💡 **Cómo se explica en la clase [B90-C21](../programa/clases/B90/B90-C21-biocarga-de-naves-espaciales-verificacion-y-requisitos-normativos/CLASE.md):**
- *Descripción textual:* los hisopos recogen colonias; la densidad estimada es `C/(eA)` y la cota superior usa el límite de Poisson de `C`; se compara la cota con el límite.
- La densidad observada es 40 /m² y la corregida 266,7 esporas/m², bajo el límite de ejemplo de 300; pero la cota superior al 95 % es 481,2 /m²: no cumple con esa confianza.
- 🎯 **Por qué importa:** Un hisopo recoge solo una fracción de las esporas de una superficie y se cuentan pocas colonias; el resultado es una estimación con incertidumbre. La decisión central: ¿la biocarga cumple el límite con la confianza exigida o hace falta muestrear más o reducir?
- 🔗 **Se estudia junto con:** Biocarga, Protección planetaria, Espora, UFC.

📘 **Dónde se aprende** (2 clases): [B90-C21 · Biocarga de naves espaciales: verificación y requisitos normativos](../programa/clases/B90/B90-C21-biocarga-de-naves-espaciales-verificacion-y-requisitos-normativos/CLASE.md); [B119-C23 · Protección ambiental de las actividades de lanzamiento](../programa/clases/B119/B119-C23-proteccion-ambiental-de-las-actividades-de-lanzamiento/CLASE.md).

### Cota superior de confianza

- Causa raíz: origen de la falla. Cota superior de confianza: valor que, con probabilidad `CL`, no es inferior a la tasa verdadera.

💡 **Cómo se explica en la clase [B90-C17](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md):**
- Calcular la cota superior de Poisson de la tasa de fallas con una confianza dada.
- 🎯 **Por qué importa:** Una falla única en 500 horas de ensayo no demuestra que el equipo sea confiable: solo acota la tasa de fallas. Y una anomalía mal registrada se pierde.
- 🔗 **Se estudia junto con:** Anomalía/discrepancia, No conformidad, Disposición, Severidad.

📘 **Dónde se aprende** (1 clase): [B90-C17 · Gestión de anomalías de prueba](../programa/clases/B90/B90-C17-gestion-de-anomalias-de-prueba/CLASE.md).

### Cotas de Voigt y Reuss

- Las cotas de Voigt y Reuss son `E_V = V_f E_f + (1 − V_f)E_m` y `E_R = 1/(V_f/E_f + (1 − V_f)/E_m)`.

💡 **Cómo se explica en la clase [B84-C37](../programa/clases/B84/B84-C37-compuestos-y-aglomerantes-a-base-de-regolito/CLASE.md):**
- Calcular las cotas de rigidez de Voigt y Reuss.
- 🎯 **Por qué importa:** La resistencia de un compuesto cae exponencialmente con la porosidad: pasar de 10 a 25 % de huecos divide la resistencia por 2,4. La decisión central: ¿qué porosidad máxima permite cumplir una resistencia mínima y cuánto ligante hay que transportar?
- 🔗 **Se estudia junto con:** relación de Ryshkewitch, intervalo de predicción, porosidad residual.

📘 **Dónde se aprende** (1 clase): [B84-C37 · Compuestos y aglomerantes a base de regolito](../programa/clases/B84/B84-C37-compuestos-y-aglomerantes-a-base-de-regolito/CLASE.md).

### COTS

- El COTS (*commercial off-the-shelf*) es un componente comercial no diseñado para el espacio.

💡 **Contexto en la clase [B95-C02](../programa/clases/B95/B95-C02-componentes-comerciales-en-vuelo-seleccion-y-riesgo/CLASE.md):**
- 🎯 **Por qué importa:** Un componente comercial puede funcionar bien en tierra y degradarse o fallar en órbita. La decisión central: ¿qué componente comercial se puede usar en esta misión, con qué margen de radiación y con qué fiabilidad del conjunto?
- 🔗 **Se estudia junto con:** TID, SEU, SEL, RDM.

📘 **Dónde se aprende** (1 clase): [B95-C02 · Componentes comerciales en vuelo: selección y riesgo](../programa/clases/B95/B95-C02-componentes-comerciales-en-vuelo-seleccion-y-riesgo/CLASE.md).

### Couette

- El flujo de Couette lo arrastra una placa; el de Poiseuille lo impulsa un gradiente de presión.

💡 **Cómo se explica en la clase [B79-C03](../programa/clases/B79/B79-C03-ecuaciones-de-navier-stokes/CLASE.md):**
- Paso 1 · Término de Couette. `0,5 × 0,2 = 0,10 m/s`.
- Obtener el perfil de Couette–Poiseuille analítico.
- 🎯 **Por qué importa:** Casi todo flujo de ingeniería tiene paredes, y en ellas la viscosidad impone velocidad cero. Sin Navier–Stokes no hay arrastre ni fricción ni calentamiento por pared.
- 🔗 **Se estudia junto con:** ecuación de Navier–Stokes, viscosidad cinemática, Poiseuille, tensión viscosa.

📘 **Dónde se aprende** (1 clase): [B79-C03 · Ecuaciones de Navier-Stokes](../programa/clases/B79/B79-C03-ecuaciones-de-navier-stokes/CLASE.md).

### Covalente polar

- Si los electrones se reparten de forma desigual, el enlace es covalente polar.

💡 **Cómo se explica en la clase [B06-C04](../programa/clases/B06/B06-C04-enlaces-ionicos-y-covalentes/CLASE.md):**
- E -->|"Sí"| F["Covalente polar (cargas parciales)"]
- Si ambos atraen electrones, los comparten (covalente); si el reparto es desigual, el enlace es polar.
- 🎯 **Por qué importa:** Las muestras del asteroide Bennu contienen amoníaco, pero en gran parte no como gas libre: los autores concluyen que la mayor parte probablemente quedó retenida como sales o ligada a minerales arcillosos y a materia orgánica, porque el amoníaco libre es muy volátil y se pierde (S1).
- 🔗 **Se estudia junto con:** electrones de valencia, regla del octeto, ion, catión.

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
- 🔗 **Se estudia junto con:** coeficiente de correlación, no correlacionadas, Independientes, no.

📘 **Dónde se aprende** (13 clases): [B11-C17 · Optimización numérica](../programa/clases/B11/B11-C17-optimizacion-numerica/CLASE.md); [B12-C05 · Covarianza y correlación](../programa/clases/B12/B12-C05-covarianza-y-correlacion/CLASE.md); [B26-C22 · Degeneraciones de parámetros cosmológicos](../programa/clases/B26/B26-C22-degeneraciones-de-parametros-cosmologicos/CLASE.md); [B29-C04 · Astrometría de exoplanetas](../programa/clases/B29/B29-C04-astrometria-de-exoplanetas/CLASE.md); [B37-C06 · Calibración de modelos estelares con el Sol y binarias](../programa/clases/B37/B37-C06-calibracion-de-modelos-estelares-con-el-sol-y-binarias/CLASE.md); [B40-C13 · Ruido, haz y covarianza instrumental en mapas del fondo](../programa/clases/B40/B40-C13-ruido-haz-y-covarianza-instrumental-en-mapas-del-fondo/CLASE.md) y 7 más.

### Covarianza cruzada

- La covarianza cruzada entre el estado actual y el ruido de proceso del intervalo es lo que las aproximaciones deben tratar.

💡 **Cómo se explica en la clase [B74-C24](../programa/clases/B74/B74-C24-medidas-retardadas-y-fuera-de-secuencia-en-filtros-de-estimacion/CLASE.md):**
- Descripción larga: reprocesar en orden es el mejor; usar la medida como actual es el peor; una retrodicción sin correlación cruzada es peor que descartar y deja una covarianza inválida.
- 🎯 **Por qué importa:** Una medida tardía contiene información valiosa pero tratarla mal puede dañar más que descartarla. La decisión central: ¿qué tratamiento de una medida tardía mejora el estimado sin romper la consistencia, y a qué coste?
- 🔗 **Se estudia junto con:** OOSM, retardo, retrodicción, reprocesado.

📘 **Dónde se aprende** (1 clase): [B74-C24 · Medidas retardadas y fuera de secuencia en filtros de estimación](../programa/clases/B74/B74-C24-medidas-retardadas-y-fuera-de-secuencia-en-filtros-de-estimacion/CLASE.md).

### Covarianza de los parámetros

- La covarianza de los parámetros es `s²(XᵀX)⁻¹` (S1).

💡 **Cómo se explica en la clase [B12-C10](../programa/clases/B12/B12-C10-regresion-lineal-y-no-lineal/CLASE.md):**
- *Descripción textual:* de los datos y un modelo se minimizan los cuadrados de los residuos; se obtienen los parámetros y la varianza del ruido; con ellos, la covarianza de los parámetros; los residuos se examinan por si muestran patrón; con la covarianza se da una predicción con su incertidumbre.
- Ejercicio 12 · integrador. Elabora tu *informe de ajuste*: elige datos sintéticos que sigan una recta y otros una exponencial; ajusta cada uno, tabula parámetros con errores típicos, verifica la covarianza por simulación, examina los residuos y da una predicción fuera del rango con su incertidumbre y su advertencia.
- 🎯 **Por qué importa:** Casi todo en ciencias espaciales es un ajuste: la deriva de un oscilador, la curva de luz de un tránsito, la degradación de una celda solar, la relación período–luminosidad. Un ajuste sin incertidumbre de parámetros ni diagnóstico de residuos es sólo una línea dibujada.
- 🔗 **Se estudia junto con:** modelo lineal en los parámetros, Mínimos cuadrados ordinarios, ecuaciones normales, residuo.

📘 **Dónde se aprende** (1 clase): [B12-C10 · Regresión lineal y no lineal](../programa/clases/B12/B12-C10-regresion-lineal-y-no-lineal/CLASE.md).

### Covarianza de medida

- La covarianza de medida es `R` (ruido) o `H P Hᵀ` (efecto de la incertidumbre del estado).

💡 **Cómo se explica en la clase [B74-C01](../programa/clases/B74/B74-C01-modelos-de-observacion/CLASE.md):**
- Propagar una covarianza de posición a covarianza de medida con `H P Hᵀ`.
- Ejercicio 8 · autónomo. Para `σ_ρ = 5 m` y `σ_r = 100 m`, ¿qué domina la covarianza de la medida esperada?
- 🎯 **Por qué importa:** Todo método de B74 (mínimos cuadrados, filtros, validación) deriva del par `h` y `H = ∂h/∂x`. La decisión central: ¿qué función y qué derivadas describen la medida, y cómo sé que están bien escritas antes de dárselas a un estimador?
- 🔗 **Se estudia junto con:** modelo de observación, residuo, jacobiano, marco ENU.

📘 **Dónde se aprende** (1 clase): [B74-C01 · Modelos de observación](../programa/clases/B74/B74-C01-modelos-de-observacion/CLASE.md).

### Covarianza del ruido de medida

- `Q` es la covarianza del ruido de proceso (cuánto se aparta el movimiento real del modelo) y `R` la covarianza del ruido de medida (S1).

💡 **Contexto en la clase [B15-C17](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md):**
- **Idea central (modelo mental):** El modelo es un testigo que dice «el objeto debería estar aquí» con una fiabilidad `P⁻`; el sensor es otro testigo que dice «lo medí aquí» con fiabilidad `R`. La ganancia pesa cada testigo según su fiabilidad: si el modelo es más fiable, `K` es pequeña; si el sensor lo es, `K` es grande. Analogía: dos testigos ponderados.
- 🎯 **Por qué importa:** Un radar mide la distancia a un objeto cada segundo, con 5 m de ruido. Si solo usas la última medida, tu error es de 5 m.
- 🔗 **Se estudia junto con:** estado, matriz de transición, matriz de medida, covarianza del ruido de proceso.

📘 **Dónde se aprende** (1 clase): [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md).

### Covarianza del ruido de proceso

- `Q` es la covarianza del ruido de proceso (cuánto se aparta el movimiento real del modelo) y `R` la covarianza del ruido de medida (S1).

💡 **Contexto en la clase [B15-C17](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md):**
- **Idea central (modelo mental):** El modelo es un testigo que dice «el objeto debería estar aquí» con una fiabilidad `P⁻`; el sensor es otro testigo que dice «lo medí aquí» con fiabilidad `R`. La ganancia pesa cada testigo según su fiabilidad: si el modelo es más fiable, `K` es pequeña; si el sensor lo es, `K` es grande. Analogía: dos testigos ponderados.
- 🎯 **Por qué importa:** Un radar mide la distancia a un objeto cada segundo, con 5 m de ruido. Si solo usas la última medida, tu error es de 5 m.
- 🔗 **Se estudia junto con:** estado, matriz de transición, matriz de medida, covarianza del ruido de medida.

📘 **Dónde se aprende** (1 clase): [B15-C17 · Filtros de Kalman introductorios](../programa/clases/B15/B15-C17-filtros-de-kalman-introductorios/CLASE.md).

### Covarianza formal

- La covarianza formal `(JᵀWJ)⁻¹` mide la incertidumbre bajo el modelo lineal.
- La covarianza formal `P = (HᵀWH)⁻¹` supone modelo lineal y ruido bien descrito.

💡 **Cómo se explica en la clase [B58-C07](../programa/clases/B58/B58-C07-determinacion-de-orbitas/CLASE.md):**
- Límites: dos cuerpos, Tierra circular, sin aberración ni retardo de luz; covarianza formal lineal.
- 🎯 **Por qué importa:** Una órbita ajustada es el producto central de la defensa planetaria: de ella salen las predicciones y las probabilidades. La decisión central: ¿cuántas observaciones y qué arco hacen falta para que la órbita sea fiable, y cómo se sabe que el ajuste es bueno?
- 🔗 **Se estudia junto con:** determinación de órbitas, Levenberg–Marquardt, arco, residuos.

📘 **Dónde se aprende** (2 clases): [B58-C07 · Determinación de órbitas](../programa/clases/B58/B58-C07-determinacion-de-orbitas/CLASE.md); [B74-C07 · Ajuste por mínimos cuadrados](../programa/clases/B74/B74-C07-ajuste-por-minimos-cuadrados/CLASE.md).

### CPI

- El CPI es `EV/AC`; el SPI, `EV/PV`.

💡 **Cómo se explica en la clase [B124-C15](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md):**
- `CPI = 0,7950` (se gasta más de lo que se gana) y `SPI = 0,8368` (hay atraso).
- Si el rendimiento de costo se mantiene, `EAC = BAC/CPI = 100,63` Mum (ETC `40,63`, VAC `-20,63`), idéntico a `AC + (BAC − EV)/CPI` (error `0,0e+00`).
- ⚠️ **Error frecuente:** Confundir gastar con avanzar. Se corrige con 8.2: el CPI compara lo ganado con lo gastado.
- 🎯 **Por qué importa:** Un proyecto se descontrola de a poco; el valor ganado convierte «vamos bien» en números comparables. La decisión central: ¿cuánto va a costar el proyecto al terminar si el rendimiento actual se mantiene y qué paquete es el problema?
- 🔗 **Se estudia junto con:** BAC, PV, EV, AC.

📘 **Dónde se aprende** (1 clase): [B124-C15 · Gestión de proyectos espaciales](../programa/clases/B124/B124-C15-gestion-de-proyectos-espaciales/CLASE.md).

### CR3BP

- El CR3BP estudia una masa despreciable bajo la gravedad de dos cuerpos masivos en órbita circular mutua.

💡 **Cómo se explica en la clase [B73-C01](../programa/clases/B73/B73-C01-problema-restringido-de-tres-cuerpos/CLASE.md):**
- Escribir las ecuaciones del CR3BP adimensional con el parámetro de masa `μ`.
- La evidencia es la ficha del CR3BP Tierra–Luna con control de conservación del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Con tres cuerpos no hay solución cerrada, pero sí una cantidad conservada que organiza todo lo demás: puntos de equilibrio, regiones prohibidas y transferencias de bajo costo. La decisión central: ¿cuándo basta el modelo de tres cuerpos restringido, y cómo sé que mi integración no inventa dinámica?
- 🔗 **Se estudia junto con:** parámetro de masa, marco sinódico, constante de Jacobi, unidades adimensionales.

📘 **Dónde se aprende** (1 clase): [B73-C01 · Problema restringido de tres cuerpos](../programa/clases/B73/B73-C01-problema-restringido-de-tres-cuerpos/CLASE.md).

### Crank–Nicolson

- La fotoevaporación es la pérdida de gas calentado por radiación. Crank–Nicolson es un esquema implícito de segundo orden.
- La fracción termalizada `η` es la parte que se convierte en calor. Crank–Nicolson es un esquema implícito de segundo orden.
- El esquema Crank–Nicolson avanza en el tiempo promediando la derivada al inicio y al final del paso (orden 2).

💡 **Cómo se explica en la clase [B23-C04](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md):**
- El error total tiene una parte espacial (`∝ Δz²`) y otra temporal (`∝ Δt²` en Crank–Nicolson).
- La diferencia con Crank–Nicolson (2000 pasos) es `5,8 × 10⁻⁷ K`: es el error temporal de Crank–Nicolson.
- 🎯 **Por qué importa:** Un modelo de conducción de calor en el regolito, con una fuente variable y una condición de flujo en el borde, no tiene solución cerrada. Pero su código puede estar mal en la frontera, en el término fuente o en el tiempo, y ninguna propiedad global lo delata fácilmente.
- 🔗 **Se estudia junto con:** solución fabricada, término fuente, condiciones de frontera, estudio de refinamiento.

📘 **Dónde se aprende** (3 clases): [B23-C04 · Soluciones de referencia y manufactured solutions](../programa/clases/B23/B23-C04-soluciones-de-referencia-y-manufactured-solutions/CLASE.md); [B52-C09 · Dispersión de discos de gas](../programa/clases/B52/B52-C09-dispersion-de-discos-de-gas/CLASE.md); [B52-C17 · Colisiones y evolución térmica](../programa/clases/B52/B52-C17-colisiones-y-evolucion-termica/CLASE.md).

### Cráter aparente

- Un cráter aparente es el visible hoy.

💡 **Cómo se explica en la clase [B61-C02](../programa/clases/B61/B61-C02-crateres-simples-morfologia-y-formacion/CLASE.md):**
- Con `d/D` = 0,2, un cráter aparente de 1000 m tiene 200 m de profundidad y un volumen de 8,27×10⁷ m³; su radio de curvatura vale 1,45 `R`.
- Distinguir el cráter transitorio del aparente y usar el factor de ensanchamiento.
- ⚠️ **Error frecuente:** Confundir cráter transitorio y aparente. Se corrige con 8.2.
- 🎯 **Por qué importa:** Medir un cráter es medir un bol, pero lo que se ve es el bol después de colapsar y rellenarse. La decisión central: ¿cuánto volumen tenía la cavidad original y cuánto se perdió en el relleno de brecha?
- 🔗 **Se estudia junto con:** casquete esférico, ensanchamiento, lente de brecha, abultamiento.

📘 **Dónde se aprende** (1 clase): [B61-C02 · Cráteres simples: morfología y formación](../programa/clases/B61/B61-C02-crateres-simples-morfologia-y-formacion/CLASE.md).

### Cráter simple

- El cráter simple conserva forma de cuenco.

💡 **Cómo se explica en la clase [B58-C15](../programa/clases/B58/B58-C15-modelos-de-impacto-planetario/CLASE.md):**
- El escalamiento recordado da un cráter transitorio de `6.01 km` y uno final simple de `7.51 km`.
- Crater transitorio D_tc = 6.010 km ; crater simple final = 7.512 km
- 🎯 **Por qué importa:** Para decidir si una desviación es necesaria hay que saber qué haría el impacto. La decisión central: ¿cómo escalan la energía y el cráter con el tamaño, la velocidad y el ángulo?
- 🔗 **Se estudia junto con:** cráter transitorio, ley de escalamiento, velocidad de impacto, ángulo.

📘 **Dónde se aprende** (1 clase): [B58-C15 · Modelos de impacto planetario](../programa/clases/B58/B58-C15-modelos-de-impacto-planetario/CLASE.md).

### Cráter transitorio

- El cráter transitorio es la cavidad máxima antes del colapso.

💡 **Cómo se explica en la clase [B58-C15](../programa/clases/B58/B58-C15-modelos-de-impacto-planetario/CLASE.md):**
- Con `v = 30 km/s` y la misma energía (`6756 Mt`), el cuerpo mediría `359 m` y el cráter transitorio sería `5.82 km`: la energía no basta, importan el tamaño y la velocidad por separado.
- El escalamiento recordado da un cráter transitorio de `6.01 km` y uno final simple de `7.51 km`.
- 🎯 **Por qué importa:** Para decidir si una desviación es necesaria hay que saber qué haría el impacto. La decisión central: ¿cómo escalan la energía y el cráter con el tamaño, la velocidad y el ángulo?
- 🔗 **Se estudia junto con:** cráter simple, ley de escalamiento, velocidad de impacto, ángulo.

📘 **Dónde se aprende** (2 clases): [B58-C15 · Modelos de impacto planetario](../programa/clases/B58/B58-C15-modelos-de-impacto-planetario/CLASE.md); [B61-C01 · Dinámica de eyección y escalado de cráteres](../programa/clases/B61/B61-C01-dinamica-de-eyeccion-y-escalado-de-crateres/CLASE.md).

### CRC

- Prueba de extremo a extremo: prueba de un hilo operativo completo entre elementos e interfaces externas. CRC: código de redundancia cíclica.

💡 **Cómo se explica en la clase [B90-C16](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md):**
- CCSDS publica protocolos de datos espaciales, pero sus recomendaciones no se consultaron; el CRC-16/CCITT-FALSE (polinomio 0x1021, valor inicial 0xFFFF) y su valor de comprobación 0x29B1 son datos de uso general no consultados en una fuente concreta.
- El laboratorio calcula `CRC("123456789") = 0x29B1`, igual al valor de comprobación.
- 🎯 **Por qué importa:** Cada subsistema puede pasar sus pruebas y la cadena fallar: un formato de trama distinto, un retraso mayor que el tiempo de espera, un error de bit no detectado. La decisión central: ¿qué errores detecta la cadena, con qué frecuencia reintenta y cuánto tarda cada acuse?
- 🔗 **Se estudia junto con:** Prueba de extremo a extremo, BER, FER, Ráfaga.

📘 **Dónde se aprende** (1 clase): [B90-C16 · Pruebas de extremo a extremo](../programa/clases/B90/B90-C16-pruebas-de-extremo-a-extremo/CLASE.md).

### CRC-15

- El CRC-15 usa el polinomio `0x4599`.

💡 **Cómo se explica en la clase [B88-C07](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md):**
- Implementar el CRC-15 del CAN y el relleno.
- Ejercicio 10 · transferencia. Transferencia. ¿Qué cambia si el CRC-15 se calcula con un polinomio distinto?
- 🎯 **Por qué importa:** El bus fija cuánta telemetría y cuántos comandos caben y con qué retardo. La decisión central: ¿cuál es el caudal útil y el peor tiempo de trama de cada bus para mi carga?
- 🔗 **Se estudia junto con:** trama CAN 2.0A, relleno de bits, carácter de datos.

📘 **Dónde se aprende** (1 clase): [B88-C07 · Buses I2C SPI CAN y SpaceWire](../programa/clases/B88/B88-C07-buses-i2c-spi-can-y-spacewire/CLASE.md).

### CRC-16

- El CRC-16 con polinomio `0x1021` e inicio `0xFFFF` da `0x29B1` para la cadena `123456789`.
- El CRC-16 valida el registro.
- El CRC-16 usa el polinomio `x¹⁶ + x¹² + x⁵ + 1` (0x1021).

💡 **Cómo se explica en la clase [B88-C08](../programa/clases/B88/B88-C08-telemetria-interna/CLASE.md):**
- El CRC-16 de `123456789` es `0x29B1` (valor de comprobación del propio laboratorio).
- Con CRC-16, un error de un byte (ráfaga ≤ 16 bits) siempre se detecta; esto lo comprueba el laboratorio, no una norma.
- 🎯 **Por qué importa:** Sin telemetría no se ve la salud de la nave; con demasiada, se satura el enlace. La decisión central: ¿qué parámetros, a qué frecuencia y con qué protección caben en el enlace sin perder los críticos?
- 🔗 **Se estudia junto con:** sincronía, volumen, ocupación, perfil.

📘 **Dónde se aprende** (3 clases): [B88-C08 · Telemetría interna](../programa/clases/B88/B88-C08-telemetria-interna/CLASE.md); [B88-C35 · Reinicio en caliente y persistencia de estado](../programa/clases/B88/B88-C35-reinicio-en-caliente-y-persistencia-de-estado/CLASE.md); [B89-C12 · Telecomandos CCSDS](../programa/clases/B89/B89-C12-telecomandos-ccsds/CLASE.md).

### CRC-32

- SHA-256: hash criptográfico de 256 bits. CRC-32: código cíclico de 32 bits.

💡 **Cómo se explica en la clase [B48-C17](../programa/clases/B48/B48-C17-gestion-de-archivos-observacionales/CLASE.md):**
- El CRC-32 detecta con seguridad cualquier cambio de un bit, pero no protege de una alteración deliberada; para eso se usa SHA-256.
- El SHA-256 de «abc» es ba7816bf8f01cfea…, y el CRC-32 de «123456789» es 0xcbf43926.
- 🎯 **Por qué importa:** Un archivo que se corrompe en silencio contamina todos los análisis posteriores. La decisión central: ¿qué suma de verificación y con cuántos bits detecta la corrupción?
- 🔗 **Se estudia junto con:** Suma de verificación, SHA-256, Colisión, Problema del cumpleaños.

📘 **Dónde se aprende** (1 clase): [B48-C17 · Gestión de archivos observacionales](../programa/clases/B48/B48-C17-gestion-de-archivos-observacionales/CLASE.md).

### CRC-8

- El CRC-8 con polinomio `0x07` da `0xF4` para `123456789`.

💡 **Cómo se explica en la clase [B88-C09](../programa/clases/B88/B88-C09-telecomandos-y-estados-de-mision/CLASE.md):**
- Ejercicio 6 · autónomo. Calcula el CRC-8 de un solo byte `0x00` con polinomio `0x07`.
- El script [telecomandos_modos.py](telecomandos_modos.py) imprime la matriz estado–comando, ejecuta un guion de nueve telecomandos con CRC y secuencia y comprueba 11 celdas aceptadas, el modo final `SAFE` y el CRC-8 de prueba `0xF4`.
- 🎯 **Por qué importa:** Un telecomando aceptado en el estado equivocado puede dañar la nave; uno rechazado en el estado correcto puede perderla. La decisión central: ¿qué comando es válido en cada modo y qué comprobaciones lo protegen?
- 🔗 **Se estudia junto con:** modo, transición, matriz estado–comando, contador de secuencia.

📘 **Dónde se aprende** (1 clase): [B88-C09 · Telecomandos y estados de misión](../programa/clases/B88/B88-C09-telecomandos-y-estados-de-mision/CLASE.md).

### Creciente

- Una función es creciente si, al aumentar `x`, `f(x)` no disminuye.
- El ángulo de fase `i` es el ángulo Sol–Luna–Tierra visto desde la Luna. Creciente es el tramo de Luna nueva a llena;

💡 **Cómo se explica en la clase [B04-C04](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md):**
- Comprueba: la función creciente da `P(292) ≈ 996 d`, coherente con redondeo.
- Componer funciones y hallar la inversa de una función creciente.
- 🎯 **Por qué importa:** Un astrónomo no solo calcula un valor: pregunta «¿qué pasa con el periodo de un planeta si su órbita es el doble de grande?». Responderlo con un solo caso no basta; hace falta la regla que liga ambas magnitudes.
- 🔗 **Se estudia junto con:** función, dominio, rango, variable independiente.

📘 **Dónde se aprende** (2 clases): [B04-C04 · Funciones y gráficas](../programa/clases/B04/B04-C04-funciones-y-graficas/CLASE.md); [B08-C08 · Fases lunares y libración](../programa/clases/B08/B08-C08-fases-lunares-y-libracion/CLASE.md).

### Crecimiento aditivo

- El crecimiento aditivo añade módulos sin retirar los existentes.

💡 **Contexto en la clase [B109-C05](../programa/clases/B109/B109-C05-crecimiento-modular-y-escalabilidad-de-asentamientos/CLASE.md):**
- 🎯 **Por qué importa:** Si el primer módulo no admite ampliación, crecer obliga a desechar lo construido. La decisión central: ¿qué funciones se duplican con la tripulación, cuáles no, y cómo se añaden módulos sin rediseñar?
- 🔗 **Se estudia junto con:** módulo, fase, escalabilidad, fija.

📘 **Dónde se aprende** (1 clase): [B109-C05 · Crecimiento modular y escalabilidad de asentamientos](../programa/clases/B109/B109-C05-crecimiento-modular-y-escalabilidad-de-asentamientos/CLASE.md).

### Crecimiento del núcleo

- El crecimiento del núcleo es `dM_c/dt = L/(X ε c²)` si toda la luminosidad viene de la capa.

💡 **Cómo se explica en la clase [B24-C16](../programa/clases/B24/B24-C16-gigantes-rojas/CLASE.md):**
- Estimar el crecimiento del núcleo por quemado de hidrógeno en capa.
- Ejercicio 12 · integrador. Elabora tu *ficha de una gigante roja*: elige `M`, `L` y `T_ef` (ilustrativos), calcula `R`, `g`, `ρ̄`, `t_dyn`, `Δν` por escala, el ritmo de crecimiento del núcleo y nombra dos fenómenos omitidos.
- 🎯 **Por qué importa:** Una gigante roja es mucho mayor y más luminosa que su estrella original y tiene una densidad media ínfima. Entender su tamaño, su gravedad y cómo crece su núcleo permite interpretar las gigantes observadas, usarlas como sondas asterosísmicas y anticipar el destino del Sol.
- 🔗 **Se estudia junto con:** gigante roja, núcleo inerte de helio, quemado en capa, rama de las gigantes rojas.

📘 **Dónde se aprende** (1 clase): [B24-C16 · Gigantes rojas](../programa/clases/B24/B24-C16-gigantes-rojas/CLASE.md).

### Crecimiento descontrolado

- El crecimiento descontrolado (*runaway*) es el régimen en que el cuerpo más masivo crece más rápido en términos relativos.

💡 **Contexto en la clase [B52-C05](../programa/clases/B52/B52-C05-crecimiento-de-embriones-planetarios/CLASE.md):**
- **Idea central (modelo mental):** Como una bola de nieve en una ladera: cuanto más pesa, más nieve recoge, hasta que ya limpió la franja por la que rueda. Límite: `v_rel` constante, un solo embrión, sin fragmentación ni gas, y un coeficiente de orden uno no calibrado.
- 🎯 **Por qué importa:** El tiempo de crecimiento decide si un núcleo existe antes de que el gas se disipe. La decisión central: ¿cómo cambia la tasa de acreción con la masa y cuándo se detiene?
- 🔗 **Se estudia junto con:** enfoque gravitacional, zona de alimentación, masa de aislamiento.

📘 **Dónde se aprende** (1 clase): [B52-C05 · Crecimiento de embriones planetarios](../programa/clases/B52/B52-C05-crecimiento-de-embriones-planetarios/CLASE.md).

### Crecimiento lineal

- El crecimiento lineal `D(a)` describe cómo `δ` crece mientras `δ ≪ 1`.

💡 **Cómo se explica en la clase [B26-C17](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md):**
- Escribir la ecuación de crecimiento lineal.
- 🎯 **Por qué importa:** Los grandes sondeos de galaxias miden cómo se agrupan, y de su agrupamiento salen la densidad de materia y la historia de la expansión. Para interpretarlos hace falta saber cómo crece una fluctuación y qué distancia angular corresponde a una escala física.
- 🔗 **Se estudia junto con:** perturbación de densidad, ecuación de crecimiento, supresión, oscilaciones acústicas de bariones (BAO).

📘 **Dónde se aprende** (1 clase): [B26-C17 · Estructura cosmológica](../programa/clases/B26/B26-C17-estructura-cosmologica/CLASE.md).

### Crecimiento logístico

- Confianza: probabilidad de detectar. Crecimiento logístico: curva en S.

💡 **Cómo se explica en la clase [B106-C28](../programa/clases/B106/B106-C28-monitoreo-microbiologico-de-agua-y-superficies-del-habitat/CLASE.md):**
- G["crecimiento logistico"] --> T["t hasta el umbral"]
- Calcular el crecimiento logístico y el tiempo hasta el umbral de acción.
- 🎯 **Por qué importa:** Una muestra pequeña puede no contener ningún organismo de una contaminación real, y un muestreo espaciado deja crecer la población. La decisión central: ¿qué volumen y qué intervalo de muestreo dan una confianza dada de detectar una contaminación antes de que supere el umbral de acción?
- 🔗 **Se estudia junto con:** UFC, Recuperación ε, Confianza, Umbral de acción.

📘 **Dónde se aprende** (1 clase): [B106-C28 · Monitoreo microbiológico de agua y superficies del hábitat](../programa/clases/B106/B106-C28-monitoreo-microbiologico-de-agua-y-superficies-del-habitat/CLASE.md).

### Crecimiento, mantenimiento y supervivencia

- Un tiempo de renovación es lo que tarda en renovarse una unidad de carbono celular. Crecimiento, mantenimiento y supervivencia son tres regímenes de actividad.

💡 **Cómo se explica en la clase [B64-C03](../programa/clases/B64/B64-C03-psicrofilos-y-vida-en-frio/CLASE.md):**
- Si a 25 °C una unidad de carbono se renovara en 1 h (supuesto sintético), el régimen de crecimiento a −40 °C tardaría 26,9 años, el de mantenimiento 2,69·10⁴ años y el de supervivencia 2,69·10⁷ años.
- Price y Sowers [S1] compararon tasas metabólicas de microbios en muchos ambientes fríos y no hallaron una temperatura mínima de metabolismo; según su resumen, crecimiento, mantenimiento y supervivencia siguen una misma energía de activación de unos 110 kJ y se escalan aproximadamente como 10⁶ : 10³ : 1.
- 🎯 **Por qué importa:** El frío no detiene la vida de golpe: la ralentiza. La pregunta motivadora: ¿cuánto más lento es el metabolismo a −40 °C que a 25 °C, y qué significa «vivir» a esa velocidad?
- 🔗 **Se estudia junto con:** psicrófilo, energía de activación, Q10, tiempo de renovación.

📘 **Dónde se aprende** (1 clase): [B64-C03 · Psicrófilos y vida en frío](../programa/clases/B64/B64-C03-psicrofilos-y-vida-en-frio/CLASE.md).

### Crecimiento por madurez

- El crecimiento por madurez es la reserva de cada equipo según lo conocido que sea (comercial, modificado, nuevo).

💡 **Cómo se explica en la clase [B86-C19](../programa/clases/B86/B86-C19-presupuesto-de-potencia-de-mision/CLASE.md):**
- S["subsistemas y modos"] --> M["crecimiento por madurez"]
- *Descripción textual:* los subsistemas, con su crecimiento por madurez y la reserva de sistema, dan la demanda por fase y la potencia de ala requerida; con la generación de cada fase resultan los márgenes y la fase crítica; un Monte Carlo del crecimiento estima la probabilidad de exceso.
- 🎯 **Por qué importa:** Un presupuesto es un compromiso de ingeniería: cada subsistema promete una potencia que todavía puede crecer. Las reservas por madurez evitan que el ala quede corta cuando una carga nueva consume más de lo previsto.
- 🔗 **Se estudia junto con:** reserva de sistema, fase, margen, fase crítica.

📘 **Dónde se aprende** (1 clase): [B86-C19 · Presupuesto de potencia de misión](../programa/clases/B86/B86-C19-presupuesto-de-potencia-de-mision/CLASE.md).

### Crecimiento secular

- El crecimiento secular es el que aumenta con `t`.

💡 **Contexto en la clase [B72-C19](../programa/clases/B72/B72-C19-analisis-de-sensibilidad-orbital/CLASE.md):**
- 🎯 **Por qué importa:** Las incertidumbres de la órbita inicial y de los parámetros determinan cuánto tiempo vale una predicción. La decisión central: ¿cómo crece con el tiempo el error de posición por cada fuente de incertidumbre y cuál de ellas manda?
- 🔗 **Se estudia junto con:** sensibilidad, matriz de transición de estado, error radial, linealidad.

📘 **Dónde se aprende** (1 clase): [B72-C19 · Análisis de sensibilidad orbital](../programa/clases/B72/B72-C19-analisis-de-sensibilidad-orbital/CLASE.md).

### Crédito

- Un crédito nombra al autor, enlaza la fuente y la licencia, e indica si hubo cambios.

💡 **Cómo se explica en la clase [B130-C01](../programa/clases/B130/B130-C01-infografias-con-fuentes-verificables/CLASE.md):**
- ESO publica sus imágenes bajo CC BY 4.0 y pide un crédito completo y visible, con enlace en línea, e indicar si se modificó el material, también si se usó IA.
- *Descripción textual:* cada dato pasa por una ficha; si la auditoría la encuentra completa se dibuja con una escala honesta y su crédito; si no, se corrige o se rotula como ilustrativo.
- 🎯 **Por qué importa:** Comunicar con imágenes exige mantener la fuente y la incertidumbre; la clase de comunicación general no entra en cómo se audita una pieza visual. La decisión central: ¿qué debe llevar cada cifra de una infografía para que otra persona pueda verificarla, y qué diseño la deforma?
- 🔗 **Se estudia junto con:** ficha de procedencia, estado, factor de mentira, color representativo.

📘 **Dónde se aprende** (1 clase): [B130-C01 · Infografías con fuentes verificables](../programa/clases/B130/B130-C01-infografias-con-fuentes-verificables/CLASE.md).

### Crédito de servicio

- El crédito de servicio compensa al cliente.

💡 **Cómo se explica en la clase [B124-C21](../programa/clases/B124/B124-C21-acuerdos-de-nivel-de-servicio-para-productos-de-datos/CLASE.md):**
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de acuerdo de nivel de servicio de un producto de datos*: componentes con MTBF y MTTR, disponibilidad en serie y con redundancia, presupuesto de error, simulación, plazo, créditos esperados y lista de qué es sintético, con el aviso de que no es un contrato.
- 🎯 **Por qué importa:** B124 trata propuestas de valor, pero un servicio de observación se compromete con plazos y calidad, y esos compromisos tienen una aritmética precisa. La decisión central: ¿qué disponibilidad y qué plazo puede prometer un servicio sin incumplir seguido y cuánto cuesta cada incumplimiento?
- 🔗 **Se estudia junto con:** disponibilidad, SLO, SLA, presupuesto de error.

📘 **Dónde se aprende** (1 clase): [B124-C21 · Acuerdos de nivel de servicio para productos de datos](../programa/clases/B124/B124-C21-acuerdos-de-nivel-de-servicio-para-productos-de-datos/CLASE.md).

### Cribado

- El cribado es la aplicación de esos criterios, primero al título y resumen y luego al texto completo.
- El cribado es el filtro rápido previo al cálculo fino.
- El cribado descarta pares.
- *(y 1 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B20-C01](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md):**
- Cuenta en cada etapa: identificados; duplicados eliminados; cribados; excluidos por cada motivo; incluidos.
- Debe cumplirse una conservación sencilla: `identificados − duplicados = cribados = incluidos + excluidos`.
- ⚠️ **Error frecuente:** Contar mal el flujo. Restar dos veces o mezclar cribados con identificados.
- 🎯 **Por qué importa:** Cuando alguien afirma «no hay estudios sobre esto» o «es sabido que…», la frase vale tanto como el procedimiento con que se buscó. Dos personas que buscan lo mismo sin anotar cómo lo hicieron obtendrán listas distintas y no podrán explicar por qué.
- 🔗 **Se estudia junto con:** pregunta de revisión, cadena de consulta, operador lógico, criterios de inclusión y exclusión.

📘 **Dónde se aprende** (4 clases): [B20-C01 · Búsqueda bibliográfica sistemática y gestión de referencias](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md); [B118-C15 · Seguimiento de mega constelaciones](../programa/clases/B118/B118-C15-seguimiento-de-mega-constelaciones/CLASE.md); [B118-C18 · Gestión del tráfico espacial](../programa/clases/B118/B118-C18-gestion-del-trafico-espacial/CLASE.md); [B119-C13 · Vigilancia y conciencia situacional espacial](../programa/clases/B119/B119-C13-vigilancia-y-conciencia-situacional-espacial/CLASE.md).

### Crimen inverso

- Si son el mismo, hay crimen inverso.

💡 **Cómo se explica en la clase [B22-C05](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md):**
- Wirgin define el crimen inverso como usar los mismos componentes teóricos, o casi los mismos, para generar los datos y para invertirlos en un problema inverso, y recuerda que Colton y Kress lo consideran una práctica trivial que debe evitarse (S3).
- Definir el crimen inverso y reconocerlo en un experimento.
- 🎯 **Por qué importa:** Con datos reales no conoces la verdad, así que no puedes medir el error de tu inversión. Con datos sintéticos sí: tú fijas la verdad, generas los datos y miras si el método la recupera.
- 🔗 **Se estudia junto con:** prueba sintética, modelo generador, modelo de inversión, discrepancia de modelo.

📘 **Dónde se aprende** (1 clase): [B22-C05 · Pruebas de inversión con datos sintéticos](../programa/clases/B22/B22-C05-pruebas-de-inversion-con-datos-sinteticos/CLASE.md).

### Criógeno

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C13](../programa/clases/B47/B47-C13-criogenia-instrumental/CLASE.md):**
- *Descripción textual:* la radiación entre escudos y la conducción por soportes suman una carga que consume el criógeno.
- Con emisividad `0,02`, área `0,2 m²`, 4 soportes y 50 kg de criógeno (ilustrativos), la carga parásita baja de `818,2 mW` sin escudos a `28,0 mW` con 40 escudos, y la vida pasa de `0,040` a `1,182 años`.
- 🎯 **Por qué importa:** Cada vatio parásito acorta la vida de un criógeno. La decisión central: ¿cuántos escudos y qué soportes bastan para una vida útil dada?
- 🔗 **Se estudia junto con:** escudo radiativo, aislamiento multicapa, emisividad, conducción.

📘 **Dónde se aprende** (1 clase): [B47-C13 · Criogenia instrumental](../programa/clases/B47/B47-C13-criogenia-instrumental/CLASE.md).

### Criomagma

- El criomagma es el material líquido o semilíquido que sube.

💡 **Contexto en la clase [B70-C06](../programa/clases/B70/B70-C06-criovulcanismo-lavas-heladas-y-emision-de-volatiles/CLASE.md):**
- **Idea central (modelo mental):** El líquido sube por el pitillo si se le aplica presión extra; al abrir, el gas disuelto sale expandiéndose y arrastra gotas.
- 🎯 **Por qué importa:** El agua líquida es más densa que el hielo, así que no sube sola. La decisión central: ¿qué presión extra y qué mecanismo hacen falta para que el agua llegue a la superficie?
- 🔗 **Se estudia junto con:** criovulcanismo, sobrepresión, flujo estrangulado, velocidad de escape.

📘 **Dónde se aprende** (1 clase): [B70-C06 · Criovulcanismo: lavas heladas y emisión de volátiles](../programa/clases/B70/B70-C06-criovulcanismo-lavas-heladas-y-emision-de-volatiles/CLASE.md).

### Criovulcanismo

- El criovulcanismo es la erupción de volátiles helados o agua en lugar de silicatos.

💡 **Cómo se explica en la clase [B70-C06](../programa/clases/B70/B70-C06-criovulcanismo-lavas-heladas-y-emision-de-volatiles/CLASE.md):**
- La evidencia es la ficha del criovulcanismo del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha del criovulcanismo*: gravedad, escape, sobrepresión, chorro y límites.
- 🎯 **Por qué importa:** El agua líquida es más densa que el hielo, así que no sube sola. La decisión central: ¿qué presión extra y qué mecanismo hacen falta para que el agua llegue a la superficie?
- 🔗 **Se estudia junto con:** criomagma, sobrepresión, flujo estrangulado, velocidad de escape.

📘 **Dónde se aprende** (1 clase): [B70-C06 · Criovulcanismo: lavas heladas y emisión de volátiles](../programa/clases/B70/B70-C06-criovulcanismo-lavas-heladas-y-emision-de-volatiles/CLASE.md).

### Criterio

- Un criterio es una propiedad que se compara (reserva, pendiente, iluminación, riesgo).
- El criterio es el nivel de desempeño exigido.
- Un criterio es un aspecto de comparación.
- *(y 3 formulaciones más en otras clases; ábrelas desde los enlaces)*

💡 **Cómo se explica en la clase [B67-C01](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md):**
- Para un criterio donde más es mejor, `z = (x − mín)/(máx − mín)`; donde menos es mejor, `z = 1 − (x − mín)/(máx − mín)`.
- S7 (90 kt, 7°, 35 %, riesgo 5) está dominado por S4 (95 kt, 6°, 40 %, riesgo 4): S4 es mejor en los cuatro criterios.
- 🎯 **Por qué importa:** Elegir con una sola cifra (la reserva) lleva a sitios que no se pueden explotar; elegir con una suma de unidades distintas es un error. La decisión central: ¿cuál sitio conviene, y cuánto de esa respuesta depende de los pesos que fija quien decide?
- 🔗 **Se estudia junto con:** normalización min-max, puntaje ponderado, domina, frente de Pareto.

📘 **Dónde se aprende** (6 clases): [B43-C20 · Proyecto mecánico completo de telescopio](../programa/clases/B43/B43-C20-proyecto-mecanico-completo-de-telescopio/CLASE.md); [B67-C01 · Selección de sitios de extracción con criterios múltiples](../programa/clases/B67/B67-C01-seleccion-de-sitios-de-extraccion-con-criterios-multiples/CLASE.md); [B83-C13 · Revisiones SRR y PDR](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md); [B104-C09 · Entrenamiento en simuladores](../programa/clases/B104/B104-C09-entrenamiento-en-simuladores/CLASE.md); [B124-C04 · Diseño de propuesta de valor](../programa/clases/B124/B124-C04-diseno-de-propuesta-de-valor/CLASE.md); [B128-C11 · Auditoría de accesibilidad de un recurso educativo](../programa/clases/B128/B128-C11-auditoria-de-accesibilidad-de-un-recurso-educativo/CLASE.md).

### Criterio de aceptación

- El criterio de aceptación es la regla de decisión fijada de antemano: aquí, `z ≤ 2` en todos los blancos.
- El criterio de aceptación es una condición medible (p. ej. «error ≤ 10⁻³ au a 91 d») fijada antes de comparar.
- Un criterio de aceptación es una condición medible con umbral.

💡 **Cómo se explica en la clase [B13-C20](../programa/clases/B13/B13-C20-validacion-de-una-cadena-de-medida/CLASE.md):**
- Definir un criterio de aceptación `z ≤ 2` por blanco.
- 🎯 **Por qué importa:** Un telémetro calibrado, con presupuesto y registro, puede seguir fallando: un error de escala oculto que la calibración en una sola distancia no ve.
- 🔗 **Se estudia junto con:** validación, calibración, blanco de referencia, tasa de aceptación.

📘 **Dónde se aprende** (3 clases): [B13-C20 · Validación de una cadena de medida](../programa/clases/B13/B13-C20-validacion-de-una-cadena-de-medida/CLASE.md); [B23-C05 · Validación con conjuntos oficiales](../programa/clases/B23/B23-C05-validacion-con-conjuntos-oficiales/CLASE.md); [B23-C08 · Informe de verificación y validación](../programa/clases/B23/B23-C08-informe-de-verificacion-y-validacion/CLASE.md).

### Criterio de beneficio

- Un criterio de beneficio es mejor cuanto mayor; uno de coste es mejor cuanto menor.

💡 **Cómo se explica en la clase [B95-C03](../programa/clases/B95/B95-C03-seleccion-y-comparacion-de-plataformas/CLASE.md):**
- Normalizar criterios de beneficio y de coste a `[0, 1]`.
- 🎯 **Por qué importa:** Elegir una plataforma «porque la conocemos» no se puede defender. La decisión central: ¿qué plataforma cumple lo imprescindible, cuál puntúa mejor y cuánto depende ese resultado de los pesos que elegimos?
- 🔗 **Se estudia junto con:** restricción dura, coste, normalización min-max, puntaje ponderado.

📘 **Dónde se aprende** (1 clase): [B95-C03 · Selección y comparación de plataformas](../programa/clases/B95/B95-C03-seleccion-y-comparacion-de-plataformas/CLASE.md).

### Criterio de comparación

- Un criterio de comparación es la regla que decide qué modelo describe mejor los datos.

💡 **Cómo se explica en la clase [B01-C17](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md):**
- Ese es el criterio de comparación: el que deje menor residuo en escala logarítmica, declarado antes de calcular.
- Ejercicio 8. ¿Por qué el criterio de comparación se escribe antes de calcular?
- 🎯 **Por qué importa:** Al final de C13, la tercera ley de Kepler daba `T²/a³ = 1` para siete planetas con error menor al 1,5 %, y 0,975 para Neptuno. ¿Falla el modelo con Neptuno?
- 🔗 **Se estudia junto con:** modelo científico, variable, parámetro, supuesto.

📘 **Dónde se aprende** (1 clase): [B01-C17 · Construcción de modelos científicos](../programa/clases/B01/B01-C17-construccion-de-modelos-cientificos/CLASE.md).

### Criterio de comprobación

- Un criterio de comprobación es una prueba objetiva que dice si el requisito se cumple.
- Un requisito es una condición que la campaña debe cumplir; debe ser verificable: tener un criterio de comprobación (un número o un sí/no) y un método de comprobación.

💡 **Cómo se explica en la clase [B08-C20](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md):**
- Cada uno tiene criterio, método de comprobación y fuente: R1, seguridad solar (nadie mira el Sol sin protección certificada verificada; revisión por una segunda persona;
- Escribir requisitos de una campaña con su criterio y método de comprobación.
- 🎯 **Por qué importa:** Una salida sin plan termina en una noche perdida o en un accidente. La pregunta motivadora: ¿cómo preparo una salida de observación para que sea segura, útil, accesible y reproducible?
- 🔗 **Se estudia junto con:** requisito, verificable, método de comprobación, componente.

📘 **Dónde se aprende** (2 clases): [B03-C20 · Problema integrado de escala del sistema solar](../programa/clases/B03/B03-C20-problema-integrado-de-escala-del-sistema-solar/CLASE.md); [B08-C20 · Proyecto de campaña de observación nocturna](../programa/clases/B08/B08-C20-proyecto-de-campana-de-observacion-nocturna/CLASE.md).

### Criterio de correlación

- El criterio de correlación (aquí `|ΔT| ≤ 3 K`, ilustrativo) acepta o rechaza el modelo.

💡 **Cómo se explica en la clase [B85-C27](../programa/clases/B85/B85-C27-margenes-y-correlacion-termica/CLASE.md):**
- Ejercicio 10 · transferencia. Transferencia. Un criterio de correlación de `±3 K` ¿es universal?
- Ejercicio 12 · integrador. Integrador. Elabora tu *informe de correlación y margen térmico*: residuos, ajuste, criterio, Monte Carlo, margen y lista de lo sintético.
- 🎯 **Por qué importa:** Un modelo sin correlación no sirve para predecir y un margen sin incertidumbre es una apuesta. La decisión central: ¿el modelo reproduce el ensayo dentro del criterio y cuánto margen queda tras la incertidumbre?
- 🔗 **Se estudia junto con:** correlación, sesgo, RMS, margen.

📘 **Dónde se aprende** (1 clase): [B85-C27 · Márgenes y correlación térmica](../programa/clases/B85/B85-C27-margenes-y-correlacion-termica/CLASE.md).

### Criterio de daño

- El criterio de daño compara la interferencia con el ruido.

💡 **Contexto en la clase [B118-C17](../programa/clases/B118/B118-C17-interferencia-radioastronomica/CLASE.md):**
- 🎯 **Por qué importa:** La radioastronomía opera en bandas donde la ITU asigna protección, pero las constelaciones numerosas y sus emisiones no deseadas pueden degradar la sensibilidad. La decisión central: ¿cuánto debe bajar una emisión para quedar por debajo del umbral de daño y de qué depende ese umbral?
- 🔗 **Se estudia junto con:** ruido rms, densidad de flujo, densidad de flujo de potencia, EIRP espectral.

📘 **Dónde se aprende** (1 clase): [B118-C17 · Interferencia radioastronómica](../programa/clases/B118/B118-C17-interferencia-radioastronomica/CLASE.md).

### Criterio de detección

- El objetivo científico y el criterio de detección (5σ).

💡 **Contexto en la clase [B46-C20](../programa/clases/B46/B46-C20-proyecto-de-observacion-radioastronomica/CLASE.md):**
- **Idea central (modelo mental):** Se parte del destino (la sensibilidad), se calcula el consumo (el tiempo) y se añade reserva (la eficiencia) antes de partir.
- 🎯 **Por qué importa:** Un proyecto viable cuadra objetivo, sensibilidad, tiempo y datos. La decisión central: ¿cuánto tiempo de observación pide el objetivo y con qué margen?
- 🔗 **Se estudia junto con:** objetivo científico, presupuesto de sensibilidad, conmutación en posición, eficiencia de observación.

📘 **Dónde se aprende** (1 clase): [B46-C20 · Proyecto de observación radioastronómica](../programa/clases/B46/B46-C20-proyecto-de-observacion-radioastronomica/CLASE.md).

### Criterio de éxito

- El criterio de éxito combina condiciones (agua y ciencia).

💡 **Cómo se explica en la clase [B104-C20](../programa/clases/B104/B104-C20-mision-tripulada-simulada/CLASE.md):**
- Fallas independientes y del mismo tamaño, sin cascadas, sin consumos que cambien por fatiga o estrés, sin reabastecimiento ni abortos, y criterios de éxito inventados.
- *Descripción textual:* la tasa de fallas determina cuántas ocurren; cada una consume horas y agua; junto con el consumo variable, determinan si se cumple el criterio de éxito.
- 🎯 **Por qué importa:** Cada margen parece suficiente por separado, pero las fallas consumen a la vez agua y tiempo. La decisión central: ¿hasta qué tasa de fallas mantiene la misión una probabilidad de éxito alta, y cuál recurso se agota primero?
- 🔗 **Se estudia junto con:** analógica, proceso de Poisson, recurso limitante, holgura.

📘 **Dónde se aprende** (1 clase): [B104-C20 · Misión tripulada simulada](../programa/clases/B104/B104-C20-mision-tripulada-simulada/CLASE.md).

### Criterio de Gladman

- El criterio de Gladman para dos planetas en órbitas circulares es `Δ > 2√3 ≈ 3,46`.

💡 **Cómo se explica en la clase [B73-C17](../programa/clases/B73/B73-C17-estabilidad-de-sistemas-exoplanetarios/CLASE.md):**
- El criterio de Gladman no se consultó en su fuente y solo se contrasta numéricamente.
- Ejercicio 10 · transferencia. Transferencia. Un colega usa el criterio de Gladman para tres planetas.
- 🎯 **Por qué importa:** Muchos sistemas exoplanetarios son compactos y su existencia depende de no haberse desestabilizado. Un criterio simple de separación permite descartar configuraciones inviables antes de integrar.
- 🔗 **Se estudia junto con:** radio de Hill mutuo, separación, encuentro cercano, tiempo de cruce.

📘 **Dónde se aprende** (1 clase): [B73-C17 · Estabilidad de sistemas exoplanetarios](../programa/clases/B73/B73-C17-estabilidad-de-sistemas-exoplanetarios/CLASE.md).

### Criterio de Hill

- El criterio de Hill pide que el radio de la partícula iguale su esfera de Hill: `1,442 R (ρ_M/ρ_m)^{1/3}`.

💡 **Cómo se explica en la clase [B73-C16](../programa/clases/B73/B73-C16-dinamica-de-anillos/CLASE.md):**
- El criterio de Hill cae entre los dos límites, como debe.
- Calcular los límites de Roche rígido y fluido y el criterio de Hill.
- 🎯 **Por qué importa:** Un anillo existe donde las mareas impiden que las partículas se junten, se ensancha por viscosidad y se estructura por resonancias con las lunas. La decisión central: ¿qué escalas fijan dónde hay un anillo, cuánto dura y dónde lo moldean las lunas?
- 🔗 **Se estudia junto con:** límite de Roche, cizalla kepleriana, resonancia, ensanchamiento viscoso.

📘 **Dónde se aprende** (1 clase): [B73-C16 · Dinámica de anillos](../programa/clases/B73/B73-C16-dinamica-de-anillos/CLASE.md).

### Criterio de Hillas

- El criterio de Hillas limita `E_max` por el tamaño y el campo de la fuente.
- El criterio de Hillas limita la energía por el tamaño y el campo.

💡 **Contexto en la clase [B28-C04](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md):**
- **Idea central (modelo mental):** Una partícula se acelera mientras su órbita cabe en la fuente: `r_L ≤ R`. Cuando el radio de giro supera el tamaño, escapa. Eso fija el techo de energía.
- 🎯 **Por qué importa:** El origen de los rayos cósmicos de mayor energía sigue abierto; el criterio de Hillas descarta fuentes y la anisotropía apunta a regiones. La decisión central: ¿qué fuentes pueden alcanzar una energía dada y qué anisotropía se puede detectar con un número dado de eventos?
- 🔗 **Se estudia junto con:** rodilla, flujo integral, dipolo, estimador.

📘 **Dónde se aprende** (2 clases): [B28-C04 · Rayos cósmicos de alta energía](../programa/clases/B28/B28-C04-rayos-cosmicos-de-alta-energia/CLASE.md); [B31-C16 · Astropartículas de alta energía](../programa/clases/B31/B31-C16-astroparticulas-de-alta-energia/CLASE.md).

### Criterio de información de Akaike

- El criterio de información de Akaike es `AIC = 2k − 2 ln L_max`, con `k` parámetros; el bayesiano es `BIC = k ln n − 2 ln L_max`, con `n` datos.
- El criterio de información de Akaike (AIC) penaliza los parámetros: `n ln(RSS/n) + 2k`.

💡 **Contexto en la clase [B12-C22](../programa/clases/B12/B12-C22-comparacion-de-modelos-evidencia-bayesiana-y-criterios-de-informacion/CLASE.md):**
- **Idea central (modelo mental):** Cada modelo se evalúa por dos cosas: qué tan bien ajusta (verosimilitud máxima) y cuánto «cuesta» su flexibilidad. AIC y BIC ponen un precio fijo por parámetro; la evidencia pone un precio que depende del prior, calculado automáticamente al promediar.
- 🎯 **Por qué importa:** Un modelo más flexible siempre ajusta mejor los datos que uno más sencillo, así que el ajuste solo no sirve para elegir. Hace falta penalizar la complejidad: ¿vale la pena el parámetro extra?
- 🔗 **Se estudia junto con:** evidencia, factor de Bayes, navaja de Occam, bayesiano.

📘 **Dónde se aprende** (2 clases): [B12-C22 · Comparación de modelos: evidencia bayesiana y criterios de información](../programa/clases/B12/B12-C22-comparacion-de-modelos-evidencia-bayesiana-y-criterios-de-informacion/CLASE.md); [B15-C21 · Series temporales multivariadas y regresión dinámica](../programa/clases/B15/B15-C21-series-temporales-multivariadas-y-regresion-dinamica/CLASE.md).

### Criterio de ligada

- El criterio de ligada de este laboratorio: la distancia a la Luna no supera `R_H` en 30 d.

💡 **Cómo se explica en la clase [B76-C03](../programa/clases/B76/B76-C03-orbitas-alrededor-de-la-luna/CLASE.md):**
- Límites: CR3BP plano, 30 d, un solo criterio de ligada; sin Sol ni campo no esférico.
- 🎯 **Por qué importa:** Un orbitador lunar bajo y un satélite de relevo alto obedecen leyes distintas. La decisión central: ¿hasta qué distancia de la Luna puede mantenerse una órbita casi circular y qué sentido de giro resiste mejor la perturbación terrestre?
- 🔗 **Se estudia junto con:** radio de Hill, prógrada, retrógrada, velocidad de escape.

📘 **Dónde se aprende** (1 clase): [B76-C03 · Órbitas alrededor de la Luna](../programa/clases/B76/B76-C03-orbitas-alrededor-de-la-luna/CLASE.md).

### Criterio de muestreo

- El criterio de muestreo usado aquí (supuesto del ejemplo) pide al menos dos píxeles por rasgo: `GSD ≤ rasgo/2`.

💡 **Cómo se explica en la clase [B83-C01](../programa/clases/B83/B83-C01-necesidad-de-mision-y-caso-cientifico/CLASE.md):**
- Derivar la resolución en tierra (GSD) a partir del tamaño del rasgo con un criterio de muestreo explícito.
- Límites: difracción sin aberraciones ni ruido; criterio de muestreo de ejemplo; puntajes inventados; no hay una misión real detrás.
- 🎯 **Por qué importa:** Un equipo sabe que quiere «mirar la costa» pero no cuánto debe resolver ni qué objetivo merece el presupuesto. La decisión central: ¿qué requisito de medición se deduce de la pregunta científica y qué objetivo conviene perseguir primero?
- 🔗 **Se estudia junto con:** necesidad de misión, caso científico, requisito de medición, GSD.

📘 **Dónde se aprende** (1 clase): [B83-C01 · Necesidad de misión y caso científico](../programa/clases/B83/B83-C01-necesidad-de-mision-y-caso-cientifico/CLASE.md).

### Criterio de Rayleigh

- El criterio de Rayleigh es un PV de λ/4.
- El ruido de fotones (o de disparo) es de tamaño `√N`; el criterio de Rayleigh da el límite de difracción `1,22 λ/D`.
- El criterio de Rayleigh: separación igual al primer cero.

💡 **Cómo se explica en la clase [B41-C12](../programa/clases/B41/B41-C12-difraccion-y-limite-de-rayleigh/CLASE.md):**
- Ejercicio 11 · transferencia. Transferencia. ¿Qué criterio da el menor ángulo, Rayleigh, Sparrow o Dawes?
- ⚠️ **Error frecuente:** Usar Rayleigh como límite absoluto. Es un criterio, no un muro.
- 🎯 **Por qué importa:** La difracción fija el mejor detalle posible. La decisión central: ¿cuándo se resuelven dos estrellas y qué cuesta una obstrucción?
- 🔗 **Se estudia junto con:** disco de Airy, función de Bessel, criterio de Sparrow, regla de Dawes.

📘 **Dónde se aprende** (4 clases): [B41-C12 · Difracción y límite de Rayleigh](../programa/clases/B41/B41-C12-difraccion-y-limite-de-rayleigh/CLASE.md); [B42-C05 · Patrones de Airy](../programa/clases/B42/B42-C05-patrones-de-airy/CLASE.md); [B50-C14 · Criterios de aceptación: Strehl, error de frente de onda y especificaciones](../programa/clases/B50/B50-C14-criterios-de-aceptacion-strehl-error-de-frente-de-onda-y-especificaciones/CLASE.md); [B57-C04 · Satélites ópticos de observación](../programa/clases/B57/B57-C04-satelites-opticos-de-observacion/CLASE.md).

### Criterio de rechazo de datos

- Un criterio de rechazo de datos es la regla, escrita antes, para descartar una lectura.

💡 **Contexto en la clase [B01-C20](../programa/clases/B01/B01-C20-proyecto-de-observacion-cientifica-inicial/CLASE.md):**
- **Idea central (modelo mental):** Imagina una cadena en la que cada eslabón es un compromiso que tomas antes de mirar el resultado: una pregunta, una hipótesis, una predicción, un criterio. Después viene la medición, y al final el análisis y la conclusión, que deben respetar los compromisos.
- 🎯 **Por qué importa:** Entender el método no es lo mismo que aplicarlo. Cuando mides de verdad, aparecen problemas que los ejercicios no tienen: el cielo se nubla, el palo no está del todo vertical, la regla se mueve, los datos no coinciden con lo que predijiste.
- 🔗 **Se estudia junto con:** protocolo, bitácora, incidencia, conclusión acotada.

📘 **Dónde se aprende** (1 clase): [B01-C20 · Proyecto de observación científica inicial](../programa/clases/B01/B01-C20-proyecto-de-observacion-cientifica-inicial/CLASE.md).

### Criterio de refinamiento

- Un criterio de refinamiento decide qué celdas se dividen.

💡 **Cómo se explica en la clase [B21-C05](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md):**
- Por eso el criterio equivale a fijar una tolerancia de error `≈ C/2`, y hay refinamiento solo mientras no se alcance.
- 🎯 **Por qué importa:** Los códigos de referencia en astrofísica, como RAMSES (S1) y Athena++ (S2), usan mallas adaptativas porque los problemas tienen rangos de escala enormes. Pero un esquema adaptativo mal construido no conserva: crea o destruye masa en las interfaces entre niveles, justo donde está el fenómeno interesante.
- 🔗 **Se estudia junto con:** malla adaptativa, nivel, suavizado de malla, restricción.

📘 **Dónde se aprende** (1 clase): [B21-C05 · Mallas adaptativas (AMR)](../programa/clases/B21/B21-C05-mallas-adaptativas-amr/CLASE.md).

### Criterio de refutación

- Un criterio de refutación es el resultado que, de ocurrir, te hace rechazar la hipótesis.

💡 **Cómo se explica en la clase [B01-C07](../programa/clases/B01/B01-C07-hipotesis-y-predicciones-falsables/CLASE.md):**
- Paso 4 · Criterio de refutación. Se rechaza si `|R − 1| ≤ 2σ_R`; se mantiene si `|R − 1,116| ≤ 2σ_R` y no es compatible con 1.
- Distinguir hipótesis, predicción y criterio de refutación.
- 🎯 **Por qué importa:** Una afirmación que ningún resultado posible contradice no enseña nada. Si dices «la Luna cambia de tamaño aparente» y, ocurra lo que ocurra, tu frase queda a salvo, no has dicho gran cosa.
- 🔗 **Se estudia junto con:** hipótesis, predicción, hipótesis alternativa, falsable.

📘 **Dónde se aprende** (1 clase): [B01-C07 · Hipótesis y predicciones falsables](../programa/clases/B01/B01-C07-hipotesis-y-predicciones-falsables/CLASE.md).

### Criterio de Routh–Hurwitz

- El arreglo de Routh es una tabla construida con los coeficientes; el criterio de Routh–Hurwitz dice que el número de cambios de signo en su primera columna es el número de raíces con parte real positiva.

💡 **Cómo se explica en la clase [B16-C08](../programa/clases/B16/B16-C08-criterio-de-routh-hurwitz/CLASE.md):**
- python programa/clases/B16/B16-C08-criterio-de-routh-hurwitz/arreglo_de_routh.py
- 🎯 **Por qué importa:** Al diseñar un lazo, la ganancia `K` es una incógnita que quieres elegir. Calcular las raíces para cada `K` es posible con un computador, pero no da la frontera: el valor exacto de `K` por encima del cual el sistema se desestabiliza.
- 🔗 **Se estudia junto con:** polinomio característico, Hurwitz, arreglo de Routh, ganancia crítica.

📘 **Dónde se aprende** (1 clase): [B16-C08 · Criterio de Routh-Hurwitz](../programa/clases/B16/B16-C08-criterio-de-routh-hurwitz/CLASE.md).

### Criterio de Schwarzschild

- El criterio de Schwarzschild dice que una capa es inestable si su gradiente real `−dT/dz` supera `Γ`.
- El criterio de Schwarzschild dice que hay convección si `∇_rad > ∇_ad`.

💡 **Cómo se explica en la clase [B24-C05](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md):**
- El criterio de Schwarzschild se cumple en las capas externas, donde `κ` es alta y `T` baja, aunque en el interior profundo sea radiativo.
- 🎯 **Por qué importa:** La energía generada en el núcleo tarda milenios en salir y el modo de transporte decide la estructura: si el interior de una estrella es convectivo, su composición se mezcla; si es radiativo, no. De ello depende cuánto combustible alcanza el núcleo, y por tanto la vida de la estrella.
- 🔗 **Se estudia junto con:** recorrido libre medio, marcha aleatoria, tiempo de difusión, gradiente adiabático.

📘 **Dónde se aprende** (2 clases): [B24-C05 · Transporte radiativo y convectivo](../programa/clases/B24/B24-C05-transporte-radiativo-y-convectivo/CLASE.md); [B54-C05 · Transporte convectivo](../programa/clases/B54/B54-C05-transporte-convectivo/CLASE.md).

### Criterio de Sparrow

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B41-C12](../programa/clases/B41/B41-C12-difraccion-y-limite-de-rayleigh/CLASE.md):**
- Ejercicio 11 · transferencia. Transferencia. ¿Qué criterio da el menor ángulo, Rayleigh, Sparrow o Dawes?
- 🎯 **Por qué importa:** La difracción fija el mejor detalle posible. La decisión central: ¿cuándo se resuelven dos estrellas y qué cuesta una obstrucción?
- 🔗 **Se estudia junto con:** disco de Airy, función de Bessel, criterio de Rayleigh, regla de Dawes.

📘 **Dónde se aprende** (1 clase): [B41-C12 · Difracción y límite de Rayleigh](../programa/clases/B41/B41-C12-difraccion-y-limite-de-rayleigh/CLASE.md).

### Criterio de tolerancia

- El criterio de tolerancia pide coma menor que el radio de Airy.

💡 **Contexto en la clase [B43-C18](../programa/clases/B43/B43-C18-colimacion-instrumental/CLASE.md):**
- **Idea central (modelo mental):** Como una linterna torcida: aunque el haz esté bien enfocado, su patrón se deforma en un lado; torcer el espejo es como mirar a una estrella fuera del eje.
- 🎯 **Por qué importa:** Colimar es ajustar tornillos hasta que el coma deje de verse; el modelo dice cuánto es «suficiente». La decisión central: ¿qué inclinación del primario produce un coma igual al radio de Airy y cuánto desvía un plano inclinado?
- 🔗 **Se estudia junto con:** colimación, coma, desviación del plano, inclinación equivalente.

📘 **Dónde se aprende** (1 clase): [B43-C18 · Colimación instrumental](../programa/clases/B43/B43-C18-colimacion-instrumental/CLASE.md).

### Criterio necesario

- Un criterio necesario debe cumplirse siempre; uno suficiente basta por sí solo.

💡 **Cómo se explica en la clase [B56-C01](../programa/clases/B56/B56-C01-definiciones-operativas-de-vida/CLASE.md):**
- Definir definición operativa, criterio necesario y suficiente, caso límite y coincidencia entre definiciones.
- 🎯 **Por qué importa:** Una misión que busca vida necesita saber qué buscar y qué contará como hallazgo. Si el criterio es vago, cualquier resultado se puede discutir; si es demasiado estrecho, se pasa por alto lo que no se parece a la vida terrestre.
- 🔗 **Se estudia junto con:** definición operativa, suficiente, caso límite, Metabolismo.

📘 **Dónde se aprende** (1 clase): [B56-C01 · Definiciones operativas de vida](../programa/clases/B56/B56-C01-definiciones-operativas-de-vida/CLASE.md).

### Criterios de aceptación

- Los criterios de aceptación del ejemplo son: base sin defectos, 100 % de comandos probados y todos los operadores con al menos 32 h.

💡 **Cómo se explica en la clase [B83-C19](../programa/clases/B83/B83-C19-aceptacion-y-transferencia-a-operaciones/CLASE.md):**
- Con los tres criterios fallidos la transferencia no se acepta; las acciones son corregir la base, probar los dos comandos con un simulador y completar 8 h al operador con 24 h.
- T["Comandos probados"] --> A["Criterios de aceptacion"]
- ⚠️ **Error frecuente:** Aceptar por calendario. Acepta por criterios cumplidos
- 🎯 **Por qué importa:** Un satélite entregado con una base de datos errónea muestra valores falsos o alarmas inútiles; operadores sin entrenamiento no saben responder. La decisión central: ¿la base de datos, los comandos y las personas están listos, de modo que operaciones pueda recibir el sistema?
- 🔗 **Se estudia junto con:** base de datos de telemetría y comandos, calibración polinómica, fuera de límites, aceptación.

📘 **Dónde se aprende** (1 clase): [B83-C19 · Aceptación y transferencia a operaciones](../programa/clases/B83/B83-C19-aceptacion-y-transferencia-a-operaciones/CLASE.md).

### Criterios de inclusión y exclusión

- Los criterios de inclusión y exclusión son reglas escritas antes de ver los resultados que deciden qué obra entra al análisis.

💡 **Cómo se explica en la clase [B20-C01](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md):**
- Redactar criterios de inclusión y exclusión operativos, fijados antes de ver los resultados.
- 🎯 **Por qué importa:** Cuando alguien afirma «no hay estudios sobre esto» o «es sabido que…», la frase vale tanto como el procedimiento con que se buscó. Dos personas que buscan lo mismo sin anotar cómo lo hicieron obtendrán listas distintas y no podrán explicar por qué.
- 🔗 **Se estudia junto con:** pregunta de revisión, cadena de consulta, operador lógico, cribado.

📘 **Dónde se aprende** (1 clase): [B20-C01 · Búsqueda bibliográfica sistemática y gestión de referencias](../programa/clases/B20/B20-C01-busqueda-bibliografica-sistematica-y-gestion-de-referencias/CLASE.md).

### Crítica de fuentes

- La crítica de fuentes es el examen de origen, fecha, propósito y dependencia de un testimonio.

💡 **Cómo se explica en la clase [B132-C01](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md):**
- La evidencia es la matriz de crítica de fuentes con sensibilidad del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Integrador. Elabora tu *matriz de crítica de fuentes con sensibilidad* para un hecho ficticio con 5 fuentes: tipo, distancia, grupo, sesgo, peso, soporte ingenuo y por grupos, y un barrido de al menos un parámetro.
- 🎯 **Por qué importa:** Un relato histórico es tan fiable como las fuentes que lo sostienen, y tres copias de una misma fuente no son tres fuentes. La decisión central: ¿cuánto apoyo da realmente un conjunto de fuentes a una afirmación y cuánto de ese apoyo es robusto ante cambios razonables de criterio?
- 🔗 **Se estudia junto con:** fuente primaria, secundaria, terciaria, estema.

📘 **Dónde se aprende** (1 clase): [B132-C01 · Crítica histórica de fuentes y método historiográfico](../programa/clases/B132/B132-C01-critica-historica-de-fuentes-y-metodo-historiografico/CLASE.md).

### Criticidad

- La criticidad mide cuántos nodos caen por una falla.
- Criticidad: consecuencia de un comando.

💡 **Cómo se explica en la clase [B96-C07](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md):**
- Se evalúan `3 × 4 × 5 × 2 = 120` combinaciones (rol, criticidad, cinco listas de aprobaciones, armado sí/no) con la política y con una referencia independiente basada en tablas de mínimos.
- C["Comando y criticidad"] --> R{"Rol minimo?"}
- 🎯 **Por qué importa:** Un comando enviado por la persona equivocada o sin segunda revisión puede perder la misión. La decisión central: ¿qué rol, qué aprobaciones y qué armado exige cada nivel de criticidad y cómo se prueba que la política no tiene huecos?
- 🔗 **Se estudia junto con:** Rol, Aprobación, Armado, Referencia independiente.

📘 **Dónde se aprende** (2 clases): [B96-C07 · Telecomandos y autorizaciones](../programa/clases/B96/B96-C07-telecomandos-y-autorizaciones/CLASE.md); [B119-C16 · Protección de infraestructura crítica](../programa/clases/B119/B119-C16-proteccion-de-infraestructura-critica/CLASE.md).

### Crítico

- Es crítico si su fallo impide la revisión.
- Un criterio crítico bloquea el veredicto si no se cumple.

💡 **Cómo se explica en la clase [B83-C13](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md):**
- SRR: requisitos verificables (≥ 95 %), necesidades con requisito (100 %), requisitos con origen (100 %), CONOPS documentado y estabilidad del orden de necesidades (≥ 70 %, no crítico).
- *Descripción textual:* el estado del proyecto y los umbrales dan criterios evaluados; los críticos fallidos determinan si la revisión está lista y generan acciones, cuyo cierre se estima en semanas.
- ⚠️ **Error frecuente:** Promediar criterios críticos. Un crítico fallido impide la revisión
- 🎯 **Por qué importa:** Una revisión aprobada sin criterios es un trámite; una revisión con criterios medibles es una decisión. La decisión central: ¿el proyecto cumple los criterios de entrada de la SRR y de la PDR y qué falta para llegar?
- 🔗 **Se estudia junto con:** SRR, PDR, criterio, RID.

📘 **Dónde se aprende** (2 clases): [B83-C13 · Revisiones SRR y PDR](../programa/clases/B83/B83-C13-revisiones-srr-y-pdr/CLASE.md); [B128-C11 · Auditoría de accesibilidad de un recurso educativo](../programa/clases/B128/B128-C11-auditoria-de-accesibilidad-de-un-recurso-educativo/CLASE.md).

### Críticos

- Los eventos críticos nunca pasan por el limitador.

💡 **Cómo se explica en la clase [B88-C10](../programa/clases/B88/B88-C10-gestion-de-eventos/CLASE.md):**
- Con limitador: registrados `48`, suprimidos `978` (todos del identificador 5) y críticos registrados `2` de `2`.
- E["Evento con id y severidad"] --> Q{"Critico?"}
- ⚠️ **Error frecuente:** Limitar también los críticos. Exímelos del limitador (8.2)
- 🎯 **Por qué importa:** Un sensor que parpadea puede generar miles de eventos y saturar el registro y el enlace, ocultando el único evento importante. La decisión central: ¿cómo se limita el ruido sin perder lo crítico?
- 🔗 **Se estudia junto con:** severidad, cubo de fichas, supresión.

📘 **Dónde se aprende** (1 clase): [B88-C10 · Gestión de eventos](../programa/clases/B88/B88-C10-gestion-de-eventos/CLASE.md).

### Cromosfera

- La fotosfera es la capa que emite la luz visible; la cromosfera y la corona están encima.

💡 **Cómo se explica en la clase [B30-C02](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md):**
- Las temperaturas (5772 K nominal de la fotosfera; 10⁴ K y 1,5 × 10⁶ K ilustrativas para cromosfera y corona) y las masas moleculares medias (1,3; 1,2; 0,6) son ilustrativas.
- `T` y `μ` de cromosfera y corona ilustrativos.
- 🎯 **Por qué importa:** La corona caliente es el origen del viento solar y de gran parte de la actividad. Entender por qué no puede estar en reposo conecta el Sol con el medio interplanetario.
- 🔗 **Se estudia junto con:** altura de escala, equilibrio hidrostático isotermo, velocidad del sonido isoterma, radio sónico.

📘 **Dónde se aprende** (1 clase): [B30-C02 · Fotosfera, cromosfera y corona](../programa/clases/B30/B30-C02-fotosfera-cromosfera-y-corona/CLASE.md).

### Crónica

- Una crónica es un relato histórico escrito, aquí por cronistas del siglo XVI.
- La carga aguda es el promedio de los últimos 7 días; la crónica, el de 28.

💡 **Cómo se explica en la clase [B02-C05](../programa/clases/B02/B02-C05-cosmovisiones-andinas-del-cielo/CLASE.md):**
- B["Texto: crónicas del siglo XVI<br/>(escritas por terceros)"] --> D
- El límite: en los Andes, el «diario» de las crónicas fue escrito por quienes ocupaban el territorio, con sus propios sesgos.
- ⚠️ **Error frecuente:** Tomar crónicas como voz indígena. Ejercicio 8.
- 🎯 **Por qué importa:** Hablar de «astronomía andina» en singular es un error: los Andes reúnen sociedades de épocas y regiones muy distintas. La pregunta motivadora es: ¿cómo se estudia respetuosamente un cielo que otra cultura leyó de otra manera, sin imponerle nuestras categorías y sin inventar lo que las fuentes no dicen?
- 🔗 **Se estudia junto con:** cosmovisión, huaca, solsticio, constelación oscura.

📘 **Dónde se aprende** (2 clases): [B02-C05 · Cosmovisiones andinas del cielo](../programa/clases/B02/B02-C05-cosmovisiones-andinas-del-cielo/CLASE.md); [B107-C05 · Prevención de lesiones en entrenamiento y trabajo operativo](../programa/clases/B107/B107-C05-prevencion-de-lesiones-en-entrenamiento-y-trabajo-operativo/CLASE.md).

### Crónico

- El estresor agudo `S(t) = 1` durante 2 h y el crónico `S = 0,5` durante 7 días.

💡 **Cómo se explica en la clase [B105-C22](../programa/clases/B105/B105-C22-sistema-neuroendocrino-y-respuesta-al-estres-en-vuelo/CLASE.md):**
- Con `S = 0,5` durante 7 días (`g = 1`), la media diaria sube de 1,000 a 1,341 (+34,1 %) y la amplitud pico-valle baja de 1,156 a 0,926: el estrés crónico eleva el nivel y aplana el ritmo en el modelo.
- Con `g = 1`, el aumento cae al 10 % en 2,74 h; un estresor crónico (+0,5 durante 7 días) sube la media diaria de 1,000 a 1,341 (+34,1 %).
- ⚠️ **Error frecuente:** Confundir estrés agudo y crónico. Efectos distintos en nivel y ritmo.
- 🎯 **Por qué importa:** Una medición de cortisol sin hora del día no se interpreta: el ritmo diario domina. Y un estresor crónico cambia el nivel medio de una forma distinta que uno agudo.
- 🔗 **Se estudia junto con:** cortisol relativo, entrada, ganancia de retroalimentación, semivida.

📘 **Dónde se aprende** (1 clase): [B105-C22 · Sistema neuroendocrino y respuesta al estrés en vuelo](../programa/clases/B105/B105-C22-sistema-neuroendocrino-y-respuesta-al-estres-en-vuelo/CLASE.md).

### Cronología

- Una cronología es una lista ordenada de hitos con fecha.
- La cronología `N₁(T)` convierte edad `T` en densidad.

💡 **Cómo se explica en la clase [B70-C04](../programa/clases/B70/B70-C04-vulcanismo-marciano-provincias-edades-y-evolucion/CLASE.md):**
- Las edades reales requieren la cronología publicada y la verificación de la saturación;
- *Descripción textual:* el conteo da una densidad; la cronología la convierte en edad y la fluctuación de Poisson da el intervalo.
- ⚠️ **Error frecuente:** Creer que la cronología es la publicada. Se corrige en la sección 5.
- 🎯 **Por qué importa:** Un conteo de cráteres es un número entero y ruidoso. La decisión central: ¿qué edad y qué incertidumbre le corresponden a una provincia dada su área y su conteo?
- 🔗 **Se estudia junto con:** densidad de cráteres, provincia, edad de modelo, saturación.

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
- 🔗 **Se estudia junto con:** registro, identificador, versión, huella.

📘 **Dónde se aprende** (6 clases): [B28-C17 · Archivos de eventos multimensajero](../programa/clases/B28/B28-C17-archivos-de-eventos-multimensajero/CLASE.md); [B53-C07 · Topografía por altimetría](../programa/clases/B53/B53-C07-topografia-por-altimetria/CLASE.md); [B86-C22 · Suministro de energía durante la noche lunar](../programa/clases/B86/B86-C22-suministro-de-energia-durante-la-noche-lunar/CLASE.md); [B88-C32 · Redundancia fría y caliente: estrategias y conmutación](../programa/clases/B88/B88-C32-redundancia-fria-y-caliente-estrategias-y-conmutacion/CLASE.md); [B88-C33 · Votación y redundancia modular triple (TMR)](../programa/clases/B88/B88-C33-votacion-y-redundancia-modular-triple-tmr/CLASE.md); [B88-C44 · Mantenimiento predictivo y pronóstico de salud de sistemas](../programa/clases/B88/B88-C44-mantenimiento-predictivo-y-pronostico-de-salud-de-sistemas/CLASE.md).

### Cruce de fase

- El cruce de ganancia `ω_gc` es donde `|L| = 1` (0 dB); el cruce de fase `ω_pc` es donde la fase es −180°.

💡 **Cómo se explica en la clase [B16-C10](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md):**
- El cruce de fase ocurre en `ω_pc = √2 = 1,414 rad/s`, donde `|L| = K/(√2·√3·√6) = K/6`.
- Obtener las frecuencias de cruce y los márgenes de ganancia y de fase.
- 🎯 **Por qué importa:** Los modelos nunca son exactos: la inercia varía, el sensor tarda más de lo supuesto, un modo flexible aparece. La estabilidad nominal no basta; hay que saber cuánto error aguanta el lazo.
- 🔗 **Se estudia junto con:** respuesta en frecuencia, diagrama de Bode, cruce de ganancia, margen de fase.

📘 **Dónde se aprende** (1 clase): [B16-C10 · Diagramas de Bode y Nyquist](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md).

### Cruce de ganancia

- El cruce de ganancia `ω_gc` es donde `|L| = 1` (0 dB); el cruce de fase `ω_pc` es donde la fase es −180°.

💡 **Cómo se explica en la clase [B16-C10](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md):**
- Paso 1 · cruce de ganancia. Se resuelve `|L(jω)| = 1` con `K = 2`: `ω_gc = 0,749 rad/s`.
- Obtener las frecuencias de cruce y los márgenes de ganancia y de fase.
- 🎯 **Por qué importa:** Los modelos nunca son exactos: la inercia varía, el sensor tarda más de lo supuesto, un modo flexible aparece. La estabilidad nominal no basta; hay que saber cuánto error aguanta el lazo.
- 🔗 **Se estudia junto con:** respuesta en frecuencia, diagrama de Bode, cruce de fase, margen de fase.

📘 **Dónde se aprende** (1 clase): [B16-C10 · Diagramas de Bode y Nyquist](../programa/clases/B16/B16-C10-diagramas-de-bode-y-nyquist/CLASE.md).

### Cruce de láminas

- El cruce de láminas ocurre cuando `1 − aε = 0`.

💡 **Cómo se explica en la clase [B36-C05](../programa/clases/B36/B36-C05-simulaciones-cosmologicas-de-n-cuerpos-condiciones-iniciales-y-caja-periodica/CLASE.md):**
- En Einstein–de Sitter (`4πGρ̄ = 1,5 H²`) la ecuación de cada lámina es `x'' + (3/2a) x' = (3/2) a⁻² (x − q)` en la variable `a`, donde `q` es la posición lagrangiana del rango (la fuerza en 1D es exacta incluso después del cruce).
- Solo antes del cruce de láminas (`a < 1/ε`); a `a = 1,51` se desvía 3,8 espaciados.
- 🎯 **Por qué importa:** Una simulación sin comprobar contra un caso exacto no es una prueba. La decisión central: ¿converge el integrador al resultado analítico y qué pasa cuando las láminas se cruzan?
- 🔗 **Se estudia junto con:** lámina, aproximación de Zel'dovich, posición lagrangiana, caja periódica.

📘 **Dónde se aprende** (1 clase): [B36-C05 · Simulaciones cosmológicas de N cuerpos: condiciones iniciales y caja periódica](../programa/clases/B36/B36-C05-simulaciones-cosmologicas-de-n-cuerpos-condiciones-iniciales-y-caja-periodica/CLASE.md).

### Cruce de planos

- El cruce de planos es donde dos planos se intersecan.

💡 **Contexto en la clase [B118-C15](../programa/clases/B118/B118-C15-seguimiento-de-mega-constelaciones/CLASE.md):**
- 🎯 **Por qué importa:** La sección 5.5 de la IADC Rev. 4 pide planificar y operar las constelaciones para minimizar la probabilidad de colisión entre sus miembros, en los cruces de planos y con otras constelaciones, y minimizar el riesgo acumulado de reentradas.
- 🔗 **Se estudia junto con:** constelación, Walker-delta, par cercano, expectativa de gas uniforme.

📘 **Dónde se aprende** (1 clase): [B118-C15 · Seguimiento de mega constelaciones](../programa/clases/B118/B118-C15-seguimiento-de-mega-constelaciones/CLASE.md).

### Cruce posicional

- Un cruce posicional (*cross-match*) empareja filas de dos catálogos que probablemente son el mismo objeto.

💡 **Cómo se explica en la clase [B14-C05](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md):**
- A["Catálogo A<br/>id, ra, dec, paralaje, procedencia"] --> X["Cruce posicional<br/>vecino más cercano"]
- *Descripción textual:* los dos catálogos entran a un cruce posicional que busca, para cada fuente de B, la más cercana de A.
- 🎯 **Por qué importa:** Un catálogo de estrellas no es una lista de números: cada columna tiene una unidad, algunas filas no tienen paralaje, y la tabla viene de un instrumento, una época y una versión. Si pierdes eso al copiar los datos a un arreglo, pierdes la mitad del significado.
- 🔗 **Se estudia junto con:** tabla, fila, columna, catálogo.

📘 **Dónde se aprende** (1 clase): [B14-C05 · Tablas astronómicas y catálogos](../programa/clases/B14/B14-C05-tablas-astronomicas-y-catalogos/CLASE.md).

### Cruda

- La carga ponderada es `Σ valoración × peso / 15`; la cruda, la media simple.

💡 **Cómo se explica en la clase [B111-C03](../programa/clases/B111/B111-C03-carga-cognitiva-y-gestion-de-la-atencion/CLASE.md):**
- Con los pesos de sus 15 comparaciones por pares la carga ponderada es `65,333` frente a `51,667` de la cruda.
- Calcular la carga ponderada y la carga cruda.
- 🎯 **Por qué importa:** Ninguna clase trataba la carga cognitiva ni el diseño de tareas para limitarla. La decisión central: ¿cómo se mide la carga y cómo se rediseña una secuencia para que no haya picos que superen la capacidad?
- 🔗 **Se estudia junto con:** carga de trabajo, carga ponderada, utilización.

📘 **Dónde se aprende** (1 clase): [B111-C03 · Carga cognitiva y gestión de la atención](../programa/clases/B111/B111-C03-carga-cognitiva-y-gestion-de-la-atencion/CLASE.md).

### CSI

- El POD es la fracción de eventos detectados, el FAR la de alertas falsas y el CSI la de aciertos sobre todos los casos relevantes.

💡 **Cómo se explica en la clase [B30-C20](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md):**
- Calcular POD, FAR, CSI y la puntuación de Heidke por dos fórmulas.
- El script [alerta.py](alerta.py) clasifica un año sintético, arma la tabla de contingencia y calcula POD, FAR, CSI y Heidke por dos fórmulas (comprueba que las dos fórmulas de Heidke coinciden a `10⁻¹²`).
- 🎯 **Por qué importa:** Una alerta con muchas falsas alarmas se ignora y una con muchos fallos no sirve; medir ambas cosas es parte del oficio. La decisión central: ¿cómo se clasifica un evento y cómo se mide si una regla de alerta tiene habilidad?
- 🔗 **Se estudia junto con:** escala, acierto, falsa alarma, fallo.

📘 **Dónde se aprende** (1 clase): [B30-C20 · Análisis de alerta solar real](../programa/clases/B30/B30-C20-analisis-de-alerta-solar-real/CLASE.md).

### CSV

- Un archivo CSV (*comma-separated values*) guarda una tabla como líneas de texto con campos separados por un delimitador, normalmente la coma.

💡 **Cómo se explica en la clase [B07-C08](../programa/clases/B07/B07-C08-lectura-de-archivos-csv/CLASE.md):**
- Un CSV sin procedencia no es un dato científico.
- Para `planetas_nssdc.csv` se declara en la cabecera del script y en la sección 11: quién publicó cada valor (NASA NSSDC), qué páginas, cuándo se consultaron y cuáles valores están redondeados (la densidad y la gravedad vienen de la tabla comparativa, con precisión menor).
- 🎯 **Por qué importa:** Un archivo CSV parece trivial y por eso engaña: todo se lee como texto, un decimal con coma rompe una columna, una línea vacía pasa inadvertida, y una codificación equivocada convierte «Júpiter» en símbolos raros. Un análisis hecho sobre datos mal leídos puede ser plausible y erróneo a la vez.
- 🔗 **Se estudia junto con:** delimitador, encabezado, entre comillas, codificación.

📘 **Dónde se aprende** (1 clase): [B07-C08 · Lectura de archivos CSV](../programa/clases/B07/B07-C08-lectura-de-archivos-csv/CLASE.md).

### CT

- Chick–Watson: inactivación proporcional a `C·t`. CT: concentración por tiempo.

💡 **Cómo se explica en la clase [B106-C26](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md):**
- Una desinfección de 4 log exige `CT = 8 mg·min/L`.
- Ejercicio 6 · autónomo. ¿Qué `CT` da 3 log?
- ⚠️ **Error frecuente:** Olvidar la desinfección. Añade CT (8.3).
- 🎯 **Por qué importa:** Las aguas grises son el mayor volumen del lazo y su carga orgánica hay que destruirla antes de potabilizar. La decisión central: ¿qué volumen de biorreactor y qué desinfección dan la remoción y la reducción de microorganismos requeridas?
- 🔗 **Se estudia junto con:** Aguas grises, Biorreactor, Mezcla completa (CSTR), Flujo pistón (PFR).

📘 **Dónde se aprende** (1 clase): [B106-C26 · Tratamiento de aguas grises en hábitats](../programa/clases/B106/B106-C26-tratamiento-de-aguas-grises-en-habitats/CLASE.md).

### CTE

- La CTE es la fracción de carga que pasa de un píxel al siguiente.

💡 **Cómo se explica en la clase [B44-C02](../programa/clases/B44/B44-C02-sensores-ccd/CLASE.md):**
- Con `1000 e⁻`, `CTE = 0,9999` y `400` transferencias, el valor analítico es `960,79 e⁻` y el simulado (300 repeticiones, semilla 20261109) `960,75 e⁻`, con error estándar de la media `0,35 e⁻`.
- *Descripción textual:* la carga inicial atraviesa `n` transferencias; la fracción restante es `CTE^n` y la simulación lo confirma.
- ⚠️ **Error frecuente:** Creer que la CTE es irrelevante por ser casi 1. Se corrige con 8.4.
- 🎯 **Por qué importa:** Cada transferencia pierde una pequeña fracción de carga, y un píxel lejano se transfiere miles de veces. La decisión central: ¿qué CTE hace aceptable un sensor de 2048 × 2048?
- 🔗 **Se estudia junto con:** ineficiencia, registro de salida, transferencia.

📘 **Dónde se aprende** (1 clase): [B44-C02 · Sensores CCD](../programa/clases/B44/B44-C02-sensores-ccd/CLASE.md).

### Cuaderno

- Un cuaderno es un documento con celdas de texto y de código, y las salidas de ese código.

💡 **Cómo se explica en la clase [B14-C09](../programa/clases/B14/B14-C09-jupyter-y-experimentos-reproducibles/CLASE.md):**
- El laboratorio construye el cuaderno con `nbformat` y lo valida contra el esquema: sus claves de nivel superior son `cells`, `metadata`, `nbformat` y `nbformat_minor`, con versión 4.5 y cuatro celdas (una de texto y tres de código).
- El texto del cuaderno no cambió, la salida sí.
- 🎯 **Por qué importa:** Alguien te manda un cuaderno con un gráfico que apoya una conclusión. Lo abres, ejecutas las celdas y el gráfico sale distinto.
- 🔗 **Se estudia junto con:** kernel, estado oculto, Reiniciar y ejecutar todo, semilla.

📘 **Dónde se aprende** (1 clase): [B14-C09 · Jupyter y experimentos reproducibles](../programa/clases/B14/B14-C09-jupyter-y-experimentos-reproducibles/CLASE.md).

### Cuadrada

- Una matriz es cuadrada si `m = n`.

💡 **Contexto en la clase [B10-C03](../programa/clases/B10/B10-C03-matrices-y-operadores-lineales/CLASE.md):**
- **Idea central (modelo mental):** Una matriz dice qué hace el operador con cada vector de la base; todo lo demás sale por linealidad.
- 🎯 **Por qué importa:** Una estación terrestre está fija respecto de la Tierra, pero la Tierra gira respecto del espacio inercial. Para saber dónde está la estación en el sistema inercial a cada instante hay que aplicar una transformación que depende del tiempo.
- 🔗 **Se estudia junto con:** operador lineal, matriz, matriz de T en una base, producto matricial.

📘 **Dónde se aprende** (1 clase): [B10-C03 · Matrices y operadores lineales](../programa/clases/B10/B10-C03-matrices-y-operadores-lineales/CLASE.md).

### Cuadrado

- El cuadrado de `a` es `a²`; el cubo, `a³`.

💡 **Cómo se explica en la clase [B03-C04](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md):**
- Si `√a` es el número que al cuadrado da `a`, entonces `(a^(1/2))² = a^(1/2 · 2) = a`, así que `a^(1/2) = √a` (por la regla 8.2).
- Un cuadrado de lado 3 se llena con `3 × 3 = 9` casillas; un cubo de arista 3, con `3 × 3 × 3 = 27` cajas.
- ⚠️ **Error frecuente:** Sumar al elevar una suma al cuadrado. Ejercicio 8.
- 🎯 **Por qué importa:** En 1619 Johannes Kepler publicó que el cuadrado del período de un planeta es proporcional al cubo del tamaño de su órbita. Hoy esa relación sigue sirviendo para estimar el período de cualquier objeto que orbita otro conocido.
- 🔗 **Se estudia junto con:** potencia, base, exponente, cubo.

📘 **Dónde se aprende** (1 clase): [B03-C04 · Potencias y raíces](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md).

### Cuadrante

- Un instrumento es un dispositivo para medir la posición del Sol, la Luna o las estrellas; un gnomon es una varilla vertical que proyecta sombra, y un cuadrante mide ángulos con un arco.

💡 **Cómo se explica en la clase [B02-C04](../programa/clases/B02/B02-C04-astronomia-de-india-china-y-mundo-islamico/CLASE.md):**
- Tenía un cuadrante mural de cobre de unos 4 m y un cuadrante azimutal inventado por al-Tusi, y una biblioteca con libros de muchas ciencias.
- 🎯 **Por qué importa:** Contar la historia de la astronomía como una línea recta de Grecia a Europa deja fuera lo que otras sociedades observaron, calcularon y construyeron. La pregunta motivadora es: ¿qué sabemos con precisión de estas tradiciones, qué falta y cómo evitar contar la historia desde un solo lado?
- 🔗 **Se estudia junto con:** estrella visitante, instrumento, gnomon, observatorio.

📘 **Dónde se aprende** (1 clase): [B02-C04 · Astronomía de India, China y mundo islámico](../programa/clases/B02/B02-C04-astronomia-de-india-china-y-mundo-islamico/CLASE.md).

### Cuadrática

- Una ecuación es lineal si la incógnita aparece solo a la primera potencia, y cuadrática si el mayor exponente es 2.

💡 **Cómo se explica en la clase [B04-C02](../programa/clases/B04/B04-C02-ecuaciones-lineales-y-cuadraticas/CLASE.md):**
- Para la cuadrática, piensa que `y = ax² + bx + c` dibuja una curva en forma de «U» (o «∩»), una parábola, y las raíces son los puntos donde corta el eje horizontal: dos, uno o ninguno.
- Su límite: en la cuadrática hay dos «pesos» que equilibran, no uno, y hay que decidir cuál es el real.
- 🎯 **Por qué importa:** Una sonda desciende hacia la Luna; un instrumento cae desde una mesa de trabajo; una señal de radio viaja hasta un espejo y vuelve. En cada caso hay un número que no conoces (un tiempo, una distancia) y una relación que lo liga a otros que sí conoces.
- 🔗 **Se estudia junto con:** ecuación, resolverla, lineal, forma general.

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
- 🔗 **Se estudia junto con:** escalera de distancias, anclaje, peldaño, error fraccional.

📘 **Dónde se aprende** (4 clases): [B26-C12 · Escalas de distancia cosmológicas](../programa/clases/B26/B26-C12-escalas-de-distancia-cosmologicas/CLASE.md); [B32-C06 · Micro y macroturbulencia y granulación estelar](../programa/clases/B32/B32-C06-micro-y-macroturbulencia-y-granulacion-estelar/CLASE.md); [B58-C09 · Probabilidades de impacto](../programa/clases/B58/B58-C09-probabilidades-de-impacto/CLASE.md); [B77-C19 · Seguridad de rango a nivel conceptual](../programa/clases/B77/B77-C19-seguridad-de-rango-a-nivel-conceptual/CLASE.md).

### Cuadro maestro

- El cuadro maestro combina muchos cuadros para reducir ruido.

💡 **Cómo se explica en la clase [B44-C12](../programa/clases/B44/B44-C12-calibracion-con-bias/CLASE.md):**
- La desviación de `cuadro − maestro` es `4,1182 ADU` (analítico `4 √(1 + 1/25) = 4,0792`) con media `+0,0190`.
- Con `N = 25` el maestro agrega solo un 2 % al ruido de un cuadro.
- ⚠️ **Error frecuente:** Usar pocos cuadros para el maestro. Se corrige con 8.3.
- 🎯 **Por qué importa:** Si el bias no se resta, el patrón fijo queda en la imagen. La decisión central: ¿cuántos cuadros se necesitan para que el maestro no añada ruido apreciable?
- 🔗 **Se estudia junto con:** mediana, patrón de columnas, propagación.

📘 **Dónde se aprende** (1 clase): [B44-C12 · Calibración con bias](../programa/clases/B44/B44-C12-calibracion-con-bias/CLASE.md).

### Cuádruple

- La cobertura simple es la fracción de tiempo con al menos un satélite visible; la cuádruple, con al menos cuatro.

💡 **Cómo se explica en la clase [B89-C17](../programa/clases/B89/B89-C17-constelaciones-y-cobertura/CLASE.md):**
- La cobertura global simple es `83,7 %` y la cuádruple `0,0 %`.
- Una constelación sintética 55°: 24/6/1 a 1200 km, con máscara de 10°, tiene una huella de semiángulo `24,03°`, `1,04` satélites visibles en promedio (teoría `1,04`), cobertura simple `83,7 %` y cuádruple `0,0 %`.
- 🎯 **Por qué importa:** El número de satélites, su altitud y la inclinación fijan cuánta gente o cuántos usuarios ven al menos uno (o cuatro, para navegar) y cuánto cuesta lograrlo. La decisión central: ¿cuántos satélites y qué geometría dan la cobertura necesaria?
- 🔗 **Se estudia junto con:** constelación Walker delta, huella, cobertura simple, promedio global de visibles.

📘 **Dónde se aprende** (1 clase): [B89-C17 · Constelaciones y cobertura](../programa/clases/B89/B89-C17-constelaciones-y-cobertura/CLASE.md).

### Cuadrupolo

- El cuadrupolo `ℓ = 2`.

💡 **Cómo se explica en la clase [B40-C15](../programa/clases/B40/B40-C15-varianza-cosmica-y-limites-de-las-mediciones-del-fondo/CLASE.md):**
- Calcular la probabilidad de un cuadrupolo bajo.
- Ejercicio 9 · transferencia. Transferencia. Un compañero dice que un cuadrupolo bajo prueba física nueva.
- 🎯 **Por qué importa:** La varianza cósmica es el límite fundamental de la medición del fondo. La decisión central: ¿qué precisión máxima permite el número de modos disponibles?
- 🔗 **Se estudia junto con:** varianza cósmica, grados de libertad, distribución χ², precisión de una amplitud.

📘 **Dónde se aprende** (1 clase): [B40-C15 · Varianza cósmica y límites de las mediciones del fondo](../programa/clases/B40/B40-C15-varianza-cosmica-y-limites-de-las-mediciones-del-fondo/CLASE.md).

### Cualquier

- Un límite en dos variables exige que el valor sea el mismo por cualquier trayectoria.

💡 **Contexto en la clase [B09-C15](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md):**
- **Idea central (modelo mental):** Una función de dos variables es un terreno: el valor es la altura. Un mapa topográfico dibuja las líneas de igual altura (curvas de nivel): juntas indican pendiente fuerte, separadas indican llanura. Una cumbre o un pozo son cerrados por curvas concéntricas; una silla de montar, por curvas en forma de cruz.
- 🎯 **Por qué importa:** Una sonda que viaja de la Tierra a la Luna se mueve en un campo de potencial que depende de dos coordenadas del plano. Dónde están los puntos de equilibrio y qué forma tiene el campo alrededor de ellos se lee en un mapa de curvas de nivel.
- 🔗 **Se estudia junto con:** función de dos variables, dominio, gráfica, corte.

📘 **Dónde se aprende** (1 clase): [B09-C15 · Funciones de varias variables](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md).

### Cuantía

- La cuantía es la cifra reclamada.

💡 **Cómo se explica en la clase [B123-C01](../programa/clases/B123/B123-C01-prueba-del-dano-y-cuantificacion-de-la-reparacion/CLASE.md):**
- Con los grados `0,95; 0,85; 0,60; 0,40`, la cuantía ponderada es `171 000 + 357 000 + 180 000 + 100 000 = 808 000` UMF.
- Si el costo de descontaminación varía de forma lognormal con sigma `0,25`, la cuantía ponderada tiene mediana `807 690` UMF y un intervalo P5–P95 de `747 588` a `900 205` UMF (20 000 sorteos, semilla 123).
- 🎯 **Por qué importa:** Un Estado puede tener derecho a reclamar y aun así perder o cobrar poco si no demuestra el daño o no lo cuantifica de forma defendible. La decisión central: ¿qué partidas puedo sostener con pruebas, por cuánto, en qué moneda y con qué margen de error?
- 🔗 **Se estudia junto con:** daño, grado de prueba, no, reparación.

📘 **Dónde se aprende** (1 clase): [B123-C01 · Prueba del daño y cuantificación de la reparación](../programa/clases/B123/B123-C01-prueba-del-dano-y-cuantificacion-de-la-reparacion/CLASE.md).

### Cuantil

- Un cuantil `q_α` cumple `F(q_α) = α`; la mediana es `q_0,5`.

💡 **Cómo se explica en la clase [B12-C02](../programa/clases/B12/B12-C02-variables-aleatorias/CLASE.md):**
- El cuantil del 95 % cumple `F(q) = 0,95`: `(q + 2)/4 = 0,95`, `q = 1,8 m`.
- Los cuantiles son la forma natural de dar límites de aceptación.
- 🎯 **Por qué importa:** Casi nunca interesa *qué* resultado ocurrió, sino *un número* que resume el resultado: cuántos computadores funcionan, qué error tuvo una medición, cuántos fotones llegaron. Poner un número en cada resultado permite sumar, promediar y comparar.
- 🔗 **Se estudia junto con:** variable aleatoria, discreta, continua, función de masa de probabilidad.

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
- 🔗 **Se estudia junto con:** bias, patrón fijo, ruido de lectura.

📘 **Dónde se aprende** (9 clases): [B44-C06 · Ruido de lectura](../programa/clases/B44/B44-C06-ruido-de-lectura/CLASE.md); [B46-C09 · Conversión analógica digital](../programa/clases/B46/B46-C09-conversion-analogica-digital/CLASE.md); [B47-C16 · Compresión de datos científicos](../programa/clases/B47/B47-C16-compresion-de-datos-cientificos/CLASE.md); [B51-C12 · Formatos de datos VLBI y geodésicos](../programa/clases/B51/B51-C12-formatos-de-datos-vlbi-y-geodesicos/CLASE.md); [B57-C03 · Resolución radiométrica y espectral](../programa/clases/B57/B57-C03-resolucion-radiometrica-y-espectral/CLASE.md); [B85-C25 · Sensores y telemetría térmica](../programa/clases/B85/B85-C25-sensores-y-telemetria-termica/CLASE.md) y 3 más.

### Cuantización de Sheppard

- La cuantización de Sheppard `1/12` px².

💡 **Contexto en la clase [B42-C14](../programa/clases/B42/B42-C14-sensores-shack-hartmann/CLASE.md):**
- **Idea central (modelo mental):** Como muchas cámaras pequeñas, cada una mirando un trozo del frente: si el trozo está inclinado, la imagen se corre.
- 🎯 **Por qué importa:** El Shack-Hartmann es el sensor más usado en óptica adaptativa. La decisión central: ¿cuántos fotones hacen falta por subapertura para que el centroide sea preciso?
- 🔗 **Se estudia junto con:** subapertura, centroide, ruido de fotones, de lectura.

📘 **Dónde se aprende** (1 clase): [B42-C14 · Sensores Shack-Hartmann](../programa/clases/B42/B42-C14-sensores-shack-hartmann/CLASE.md).

### Cuartos

- La luna nueva ocurre cuando la Luna está entre la Tierra y el Sol (no se ve el lado iluminado); la luna llena, cuando la Tierra está entre la Luna y el Sol; los cuartos, cuando el ángulo Sol–Tierra–Luna es de 90°.

💡 **Cómo se explica en la clase [B01-C12](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md):**
- N["Luna nueva: edad 0"] --> C1["Cuarto creciente: edad ≈ P/4"]
- LL --> C2["Cuarto menguante: edad ≈ 3P/4"]
- 🎯 **Por qué importa:** La Luna es el reloj más a mano del cielo: cada noche cambia, y cada 29,5 días vuelve a empezar. Pero «a mano» no significa «fácil de explicar»: muchas personas creen que las fases son la sombra de la Tierra sobre la Luna.
- 🔗 **Se estudia junto con:** fase, luna nueva, luna llena, edad.

📘 **Dónde se aprende** (1 clase): [B01-C12 · Fases lunares y ciclos celestes](../programa/clases/B01/B01-C12-fases-lunares-y-ciclos-celestes/CLASE.md).

### Cuásar

- Un cuásar es un núcleo galáctico activo muy lejano; su movimiento propio esperado es despreciable (S1, cap. 2).

💡 **Cómo se explica en la clase [B13-C21](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md):**
- La IAU recomendó en 1991 que el origen del sistema celeste estuviera en el baricentro del sistema solar y que sus ejes fueran fijos respecto de los cuásares, con plano principal cercano al ecuador medio de J2000.0; en 1997 adoptó el ICRS, que reemplazó al FK5 el 1 de enero de 1998 (S1, cap. 2).
- Las coordenadas de cada cuásar son las marcas del mapa; los ejes salen de ellas.
- 🎯 **Por qué importa:** Para seguir una nave en el espacio profundo hay que decir en qué dirección está respecto de un marco fijo. Si el marco gira aunque sea un poco, todas las direcciones se desplazan.
- 🔗 **Se estudia junto con:** Sistema Celeste de Referencia Internacional (ICRS), Marco Celeste de Referencia Internacional (ICRF), fuente definidora, suelo de ruido.

📘 **Dónde se aprende** (1 clase): [B13-C21 · Sistema de referencia celeste ICRF y cuásares](../programa/clases/B13/B13-C21-sistema-de-referencia-celeste-icrf-y-cuasares/CLASE.md).

### Cuasiespecie

- Una cuasiespecie es la nube de mutantes alrededor de la maestra.

💡 **Cómo se explica en la clase [B56-C03](../programa/clases/B56/B56-C03-origen-de-moleculas-autorreplicantes/CLASE.md):**
- Cuasiespecie completa: resuelve una matriz de mutación; más realista, costosa.
- 🎯 **Por qué importa:** Un replicador que copia mal pierde su información; uno que copia bien necesita una maquinaria que, sin vida previa, aún no existe. Esa tensión limita el tamaño de los primeros genomas.
- 🔗 **Se estudia junto con:** replicador, secuencia maestra, fidelidad, calidad de copia.

📘 **Dónde se aprende** (1 clase): [B56-C03 · Origen de moléculas autorreplicantes](../programa/clases/B56/B56-C03-origen-de-moleculas-autorreplicantes/CLASE.md).

### Cuasi-identificador

- El cuasi-identificador combina atributos.

💡 **Cómo se explica en la clase [B105-C19](../programa/clases/B105/B105-C19-bioetica-en-investigacion-tripulada/CLASE.md):**
- Descripción: la salida con la unicidad por esquema de cuasi-identificadores y el error de Laplace por `ε`.
- Medir cómo la generalización de los cuasi-identificadores reduce la unicidad.
- ⚠️ **Error frecuente:** Creer que quitar el nombre anonimiza. Los cuasi-identificadores reidentifican (8.2).
- 🎯 **Por qué importa:** No basta con quitar el nombre: con edad, sexo, profesión y misión, una persona de una cohorte de 6 suele ser única. La decisión central: ¿qué se puede publicar de una cohorte pequeña sin identificar a nadie y cuánta utilidad se pierde al protegerla?
- 🔗 **Se estudia junto con:** informe Belmont, respeto por las personas, beneficencia, justicia.

📘 **Dónde se aprende** (1 clase): [B105-C19 · Bioética en investigación tripulada](../programa/clases/B105/B105-C19-bioetica-en-investigacion-tripulada/CLASE.md).

### Cuasi-isótropo

- Un laminado cuasi-isótropo tiene `A` isótropa en el plano.

💡 **Cómo se explica en la clase [B84-C03](../programa/clases/B84/B84-C03-materiales-compuestos/CLASE.md):**
- El cuasi-isótropo pierde 61 % del módulo longitudinal del UD y gana igualdad en todas las direcciones.
- En el cuasi-isótropo `|A₁₁ − A₂₂|/A₁₁ = 0` y `|A₆₆ − (A₁₁ − A₁₂)/2|/A₆₆ = 3,6 × 10⁻¹⁶`, y `E = 54,07 GPa`, `ν = 0,311` dan `G = 20,62 GPa`, igual a `A₆₆/h`.
- 🎯 **Por qué importa:** Un panel de fibra con las capas mal orientadas puede ser 14 veces más blando en una dirección que en otra sin que el material cambie. La decisión central: ¿cómo cambia la rigidez efectiva de un laminado según el ángulo de sus capas?
- 🔗 **Se estudia junto con:** lámina, matriz de rigidez reducida, matriz A.

📘 **Dónde se aprende** (1 clase): [B84-C03 · Materiales compuestos](../programa/clases/B84/B84-C03-materiales-compuestos/CLASE.md).

### Cuasineutralidad

- La cuasineutralidad es la neutralidad a escalas mayores que `λ_D`.

💡 **Contexto en la clase [B30-C07](../programa/clases/B30/B30-C07-longitud-de-debye-y-plasma/CLASE.md):**
- **Idea central (modelo mental):** Una persona con un cartel llama la atención solo de los más cercanos: la multitud la rodea y su señal se apaga a unos metros. La longitud de Debye es esa distancia.
- 🎯 **Por qué importa:** Sin apantallamiento no hay plasma, y sin muchas partículas en la esfera de Debye no hay comportamiento colectivo. La decisión central: ¿cuándo un gas ionizado es un plasma?
- 🔗 **Se estudia junto con:** longitud de Debye, parámetro de plasma, apantallamiento.

📘 **Dónde se aprende** (1 clase): [B30-C07 · Longitud de Debye y plasma](../programa/clases/B30/B30-C07-longitud-de-debye-y-plasma/CLASE.md).

### Cuasi-satélite

- El ángulo coorbital `θ = λ_part − λ_Tierra` (sin envolver) distingue: tadpole (`θ` oscila alrededor de `±60°` sin cruzar `0` ni `π`), herradura (`θ` cubre `π` sin cruzar `0` ni `2π`) y cuasi-satélite (`θ` oscila alrededor de `0` con una amplitud pequeña y la partícula se mantiene a unos pocos `R_H`).

💡 **Cómo se explica en la clase [B73-C22](../programa/clases/B73/B73-C22-capturas-temporales-y-cuasi-satelites/CLASE.md):**
- El caso `e = 0,02` se acerca a `0,04 R_H` de la Tierra, es dispersado y sale de la coorbitalidad: no todo estado inicial parecido a un cuasi-satélite lo es.
- Un cuasi-satélite no es un satélite: `θ` libra alrededor de `0` pero la partícula orbita al Sol en un año con `a ≈ 1`; su distancia a la Tierra (`4,7–11,7 R_H`) la deja fuera de la esfera de Hill.
- ⚠️ **Error frecuente:** Tomar un cuasi-satélite por un satélite. Se corrige con 8.5.
- 🎯 **Por qué importa:** Un asteroide puede acompañar a la Tierra durante siglos sin orbitarla: dando vueltas alrededor de L4 (tadpole), de L3–L4–L5 (herradura) o de la propia Tierra (cuasi-satélite); y puede ser capturado temporalmente dentro de su esfera de Hill. Distinguirlos requiere una clasificación operativa y una advertencia: no son satélites.
- 🔗 **Se estudia junto con:** ángulo coorbital, tadpole, herradura, captura temporal.

📘 **Dónde se aprende** (1 clase): [B73-C22 · Capturas temporales y cuasi-satélites](../programa/clases/B73/B73-C22-capturas-temporales-y-cuasi-satelites/CLASE.md).

### Cuaternión

- Un cuaternión es `q = (q₀, q₁, q₂, q₃) = q₀ + q₁ i + q₂ j + q₃ k` con `i² = j² = k² = ijk = −1`.
- El cuaternión `q = (w, x, y, z)` rota del cuerpo al marco de navegación.
- El cuaternión `q = [qv; qw]` tiene norma 1.

💡 **Cómo se explica en la clase [B10-C15](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md):**
- Un cuaternión unitario tiene tres grados de libertad reales (cuatro números, una restricción de norma), igual que una rotación.
- El ángulo del cuaternión es la mitad del de la rotación: `θ = 2 arccos q₀`.
- 🎯 **Por qué importa:** Un seguidor estelar entrega la actitud del satélite varias veces por segundo; el sistema de control la combina con las lecturas de giróscopos, la propaga y la compara con la actitud deseada. Hacerlo con ángulos de Euler es frágil; hacerlo con matrices cuesta más y acumula deriva.
- 🔗 **Se estudia junto con:** parte escalar, parte vectorial, escalar primero, producto de Hamilton.

📘 **Dónde se aprende** (3 clases): [B10-C15 · Cuaterniones unitarios](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md); [B80-C03 · Mecanización strapdown e integración de actitud y velocidad](../programa/clases/B80/B80-C03-mecanizacion-strapdown-e-integracion-de-actitud-y-velocidad/CLASE.md); [B87-C02 · Representaciones de orientación](../programa/clases/B87/B87-C02-representaciones-de-orientacion/CLASE.md).

### Cuaternión de error

- El cuaternión de error es `q_e = q_obj⁻¹ ⊗ q`; vale `[1, 0, 0, 0]` (o su opuesto) cuando la orientación alcanzó el objetivo.

💡 **Cómo se explica en la clase [B16-C20](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md):**
- *Descripción textual:* se calcula el cuaternión de error entre la orientación y el objetivo; si su escalar es no negativo se aplica la ley normal, y si es negativo se invierte el signo de la parte proporcional para tomar el camino corto; el par actúa sobre el cuerpo cuya orientación realimenta el error.
- Un error de implementación (un signo, el orden del producto de cuaterniones, una convención) o un paso de integración demasiado grande, pues con 0,02 rad la diferencia entre lineal y no lineal debe ser del orden del cuadrado (4×10⁻⁴ relativo), muy por debajo de 10⁻².
- 🎯 **Por qué importa:** Un telescopio debe girar desde una orientación a otra y quedarse allí. Con tres ejes acoplados y rotaciones grandes, ni los ángulos de Euler (tienen singularidades y dependen de la secuencia de giros) ni el modelo lineal bastan.
- 🔗 **Se estudia junto con:** cuaternión unitario, producto de cuaterniones, cinemática, dinámica.

📘 **Dónde se aprende** (1 clase): [B16-C20 · Control de orientación en un simulador](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md).

### Cuaternión puro

- Un cuaternión puro `(0, v)` representa un vector.

💡 **Contexto en la clase [B10-C15](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md):**
- **Idea central (modelo mental):** Los cuaterniones unitarios forman una esfera de cuatro dimensiones. Cada punto es una rotación (y su antípoda, la misma): el ángulo se guarda a la mitad.
- 🎯 **Por qué importa:** Un seguidor estelar entrega la actitud del satélite varias veces por segundo; el sistema de control la combina con las lecturas de giróscopos, la propaga y la compara con la actitud deseada. Hacerlo con ángulos de Euler es frágil; hacerlo con matrices cuesta más y acumula deriva.
- 🔗 **Se estudia junto con:** cuaternión, parte escalar, parte vectorial, escalar primero.

📘 **Dónde se aprende** (1 clase): [B10-C15 · Cuaterniones unitarios](../programa/clases/B10/B10-C15-cuaterniones-unitarios/CLASE.md).

### Cuaternión unitario

- Un cuaternión unitario `q = [q0, q_v]` (escalar primero, `q_v` de tres componentes) con `q0² + |q_v|² = 1` representa una rotación; usamos la convención de que lleva componentes del sistema inercial al del cuerpo.

💡 **Cómo se explica en la clase [B16-C20](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md):**
- El espacio de cuaterniones unitarios recubre dos veces el de las orientaciones: cada orientación tiene dos representaciones, `q` y `−q`.
- Usar un cuaternión unitario para representar y componer orientaciones.
- 🎯 **Por qué importa:** Un telescopio debe girar desde una orientación a otra y quedarse allí. Con tres ejes acoplados y rotaciones grandes, ni los ángulos de Euler (tienen singularidades y dependen de la secuencia de giros) ni el modelo lineal bastan.
- 🔗 **Se estudia junto con:** producto de cuaterniones, cuaternión de error, cinemática, dinámica.

📘 **Dónde se aprende** (1 clase): [B16-C20 · Control de orientación en un simulador](../programa/clases/B16/B16-C20-control-de-orientacion-en-un-simulador/CLASE.md).

### CubeSat 3U

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C25](../programa/clases/B47/B47-C25-diseno-de-cargas-utiles-educativas/CLASE.md):**
- La matriz es un ejemplo de método: los umbrales son ilustrativos y no provienen de ninguna convocatoria ni estándar de CubeSat.
- 🎯 **Por qué importa:** Muchos CubeSat universitarios fracasan por requisitos sin cifra o sin evidencia. La decisión central: ¿qué requisitos medibles se fijan, cómo se verifican y cuáles cumple un diseño preliminar?
- 🔗 **Se estudia junto con:** carga útil, GSD, parámetro Q = λF/p, profundidad de descarga.

📘 **Dónde se aprende** (1 clase): [B47-C25 · Diseño de cargas útiles educativas](../programa/clases/B47/B47-C25-diseno-de-cargas-utiles-educativas/CLASE.md).

### Cubierta

- Regolito: material suelto de la superficie. Cubierta: capa de regolito sobre el habitat.

💡 **Cómo se explica en la clase [B106-C19](../programa/clases/B106/B106-C19-arquitectura-de-asentamiento-lunar-conceptual/CLASE.md):**
- V["cubierta 3 m"] --> X["excavacion y blindaje"]
- *Descripción textual:* la noche fija la energía almacenada; la gravedad baja la presión que ejerce el regolito, de modo que el casco sostiene la presión interior y la cubierta se reserva para blindaje y estabilidad térmica.
- 🎯 **Por qué importa:** La Luna cambia las reglas: noches de dos semanas, gravedad de un sexto y un regolito que protege pero no contiene la presión. La decisión central: ¿qué recursos (energía, masa de cubierta, esfuerzo de excavación) exige un asentamiento enterrado y qué parte soporta cada elemento?
- 🔗 **Se estudia junto con:** Noche lunar, Regolito, Espesor másico, Profundidad de descarga.

📘 **Dónde se aprende** (1 clase): [B106-C19 · Arquitectura de asentamiento lunar conceptual](../programa/clases/B106/B106-C19-arquitectura-de-asentamiento-lunar-conceptual/CLASE.md).

### Cubo

- El cuadrado de `a` es `a²`; el cubo, `a³`.

💡 **Cómo se explica en la clase [B03-C04](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md):**
- Y `a^(3/2) = (√a)³ = √(a³)`: primero raíz y luego cubo, o al revés.
- Un cuadrado de lado 3 se llena con `3 × 3 = 9` casillas; un cubo de arista 3, con `3 × 3 × 3 = 27` cajas.
- 🎯 **Por qué importa:** En 1619 Johannes Kepler publicó que el cuadrado del período de un planeta es proporcional al cubo del tamaño de su órbita. Hoy esa relación sigue sirviendo para estimar el período de cualquier objeto que orbita otro conocido.
- 🔗 **Se estudia junto con:** potencia, base, exponente, cuadrado.

📘 **Dónde se aprende** (1 clase): [B03-C04 · Potencias y raíces](../programa/clases/B03/B03-C04-potencias-y-raices/CLASE.md).

### Cubo de fichas

- El cubo de fichas tiene capacidad `B` y se rellena a `r` fichas por segundo; cada evento gasta una.

💡 **Cómo se explica en la clase [B88-C10](../programa/clases/B88/B88-C10-gestion-de-eventos/CLASE.md):**
- *Descripción textual:* un evento crítico se registra siempre; uno no crítico solo si el cubo de su identificador tiene una ficha; si no, se suprime y se cuenta.
- El script [eventos.py](eventos.py) genera 1026 eventos con semilla 10, aplica un cubo de fichas por identificador y comprueba que se suprimen 978 del parpadeo y no se suprime ningún crítico.
- 🎯 **Por qué importa:** Un sensor que parpadea puede generar miles de eventos y saturar el registro y el enlace, ocultando el único evento importante. La decisión central: ¿cómo se limita el ruido sin perder lo crítico?
- 🔗 **Se estudia junto con:** severidad, supresión, críticos.

📘 **Dónde se aprende** (1 clase): [B88-C10 · Gestión de eventos](../programa/clases/B88/B88-C10-gestion-de-eventos/CLASE.md).

### Cubo hiperespectral

- El cubo hiperespectral tiene dos dimensiones espaciales y una espectral.

💡 **Cómo se explica en la clase [B57-C22](../programa/clases/B57/B57-C22-espectrometros-de-imagen-e-hiperespectrales/CLASE.md):**
- Describir un cubo hiperespectral y su flujo de datos.
- 🎯 **Por qué importa:** Dos materiales distintos pueden parecer iguales en cuatro bandas anchas y diferenciarse en cientos de bandas estrechas. La decisión central: ¿cuándo vale la pena el costo en datos de un sensor hiperespectral y cómo se separa una mezcla de materiales?
- 🔗 **Se estudia junto con:** miembro extremo, desmezclado lineal, abundancias, ángulo espectral.

📘 **Dónde se aprende** (1 clase): [B57-C22 · Espectrómetros de imagen e hiperespectrales](../programa/clases/B57/B57-C22-espectrometros-de-imagen-e-hiperespectrales/CLASE.md).

### Cuello

- El cuello es la zona de unión entre dos partículas y `x/a` su razón.
- Un cuello está abierto si `C ≤ C(Li)`.

💡 **Cómo se explica en la clase [B59-C12](../programa/clases/B59/B59-C12-sinterizacion-de-materiales/CLASE.md):**
- Como miel que se espesa al enfriarse: a baja temperatura casi no fluye y el cuello crece muy despacio.
- Límite: la ley de Frenkel supone flujo viscoso newtoniano y cuellos pequeños; el regolito real puede cristalizar.
- ⚠️ **Error frecuente:** Extrapolar Frenkel a cuellos grandes. Se corrige con la sección 14.
- 🎯 **Por qué importa:** Una variación de 50 K en el horno cambia el tiempo de sinterización en un factor 2,6. La decisión central: ¿con qué precisión hay que controlar la temperatura, y cuánta energía cuesta alcanzarla?
- 🔗 **Se estudia junto con:** sinterización, ley de Frenkel, ley de Arrhenius, regresión de Arrhenius.

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
- 🔗 **Se estudia junto con:** vectorización, perfilador, tiempo acumulado, propio.

📘 **Dónde se aprende** (7 clases): [B14-C14 · Vectorización y rendimiento](../programa/clases/B14/B14-C14-vectorizacion-y-rendimiento/CLASE.md); [B18-C04 · Perfilado de rendimiento](../programa/clases/B18/B18-C04-perfilado-de-rendimiento/CLASE.md); [B89-C20 · Diseño de red de comunicaciones de misión](../programa/clases/B89/B89-C20-diseno-de-red-de-comunicaciones-de-mision/CLASE.md); [B97-C27 · Simulación de productividad de flotas de maquinaria](../programa/clases/B97/B97-C27-simulacion-de-productividad-de-flotas-de-maquinaria/CLASE.md); [B110-C03 · Evacuación y refugio de emergencia](../programa/clases/B110/B110-C03-evacuacion-y-refugio-de-emergencia/CLASE.md); [B114-C01 · Rutas de evacuación y salidas de emergencia en hábitats](../programa/clases/B114/B114-C01-rutas-de-evacuacion-y-salidas-de-emergencia-en-habitats/CLASE.md) y 1 más.

### Cuello de botella del deuterio

- El cuello de botella del deuterio es el retraso hasta que el deuterio deja de fotodisociarse.

💡 **Cómo se explica en la clase [B26-C16](../programa/clases/B26/B26-C16-nucleosintesis-primordial/CLASE.md):**
- Estimar la temperatura del cuello de botella del deuterio.
- cuello de botella del deuterio: kT ~ B_d / ln(1/eta) = 2.2246/21.22 = 0.1048 MeV = 1.217e+09 K (orden de magnitud)
- 🎯 **Por qué importa:** La cuarta parte de la masa bariónica del universo es helio, y la proporción casi no cambió desde los primeros minutos. Su valor da información sobre cuántas especies de neutrinos existen y sobre la densidad de bariones.
- 🔗 **Se estudia junto con:** nucleosíntesis primordial, razón n/p, congelación, vida media del neutrón libre.

📘 **Dónde se aprende** (1 clase): [B26-C16 · Nucleosíntesis primordial](../programa/clases/B26/B26-C16-nucleosintesis-primordial/CLASE.md).

### Cuenca multianillo

- Una cuenca multianillo tiene varios anillos concéntricos.

💡 **Cómo se explica en la clase [B61-C07](../programa/clases/B61/B61-C07-cuencas-multianillo-y-grandes-impactos/CLASE.md):**
- La evidencia es la ficha de la cuenca multianillo del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *ficha de la cuenca multianillo*: la recurrencia de anillos, su contraste con √2, la estimación de `c`, la energía inferida y su incertidumbre, con rótulos de lo sintético.
- 🎯 **Por qué importa:** Las cuencas dejan huella en la corteza entera. La decisión central: ¿cómo se espacian los anillos, qué proyectil implica una cuenca y cuándo excava hasta el manto?
- 🔗 **Se estudia junto con:** espaciado radial, protocuenca, profundidad de excavación, corteza.

📘 **Dónde se aprende** (1 clase): [B61-C07 · Cuencas multianillo y grandes impactos](../programa/clases/B61/B61-C07-cuencas-multianillo-y-grandes-impactos/CLASE.md).

### Cuenta

- La cuenta `N = f/(presc)·Δt`.
- Parámetro: una magnitud con nombre, unidad y límites. Cuenta: valor entero del conversor.

💡 **Cómo se explica en la clase [B88-C02](../programa/clases/B88/B88-C02-microcontroladores-embarcados/CLASE.md):**
- Límite: los engranajes reales no tienen error de redondeo en cuentas enteras.
- Paso 1 · Cuenta. `16·10⁶/64 · 10⁻³ = 250`.
- 🎯 **Por qué importa:** Un error de configuración (un divisor mal calculado, una resolución insuficiente) no se ve en el escritorio y aparece en órbita. La decisión central: ¿qué valores de registro dan la temporización, la velocidad y la resolución que exige el requisito, con qué error?
- 🔗 **Se estudia junto con:** prescaler, divisor, LSB, error de cuantización.

📘 **Dónde se aprende** (2 clases): [B88-C02 · Microcontroladores embarcados](../programa/clases/B88/B88-C02-microcontroladores-embarcados/CLASE.md); [B96-C06 · Telemetría operativa](../programa/clases/B96/B96-C06-telemetria-operativa/CLASE.md).

### Cuenta continua

- La cuenta continua es una numeración de segundos sin saltos (aquí desde 1972-01-01 00:00:00 UTC, basada en TAI).

💡 **Cómo se explica en la clase [B13-C09](../programa/clases/B13/B13-C09-segundos-intercalares-y-cronologia/CLASE.md):**
- La cuenta continua es la regla uniforme.
- C --> D["Cuenta continua<br/>de segundos"]
- 🎯 **Por qué importa:** Una nave graba un evento a las `23:59:59` del 31 de diciembre de 2016 y otro a las `00:00:00` del 1 de enero de 2017. ¿Cuánto tiempo pasó?
- 🔗 **Se estudia junto con:** segundo intercalar, calendario gregoriano, día juliano (JD), día juliano modificado (MJD).

📘 **Dónde se aprende** (1 clase): [B13-C09 · Segundos intercalares y cronología](../programa/clases/B13/B13-C09-segundos-intercalares-y-cronologia/CLASE.md).

### Cuenta de arranques

- La cuenta de arranques limita los intentos.

💡 **Cómo se explica en la clase [B88-C13](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md):**
- Tras el cambio, el cargador cuenta los arranques.
- 🎯 **Por qué importa:** Una actualización fallida en órbita no se arregla con un cable. La decisión central: ¿qué comprobaciones aceptan solo la imagen correcta y qué mecanismo vuelve a una versión conocida si la nueva no arranca?
- 🔗 **Se estudia junto con:** hash, HMAC-SHA256, ranuras A/B, reversión.

📘 **Dónde se aprende** (1 clase): [B88-C13 · Actualización segura de software](../programa/clases/B88/B88-C13-actualizacion-segura-de-software/CLASE.md).

### Cuenta de Coulomb

- La cuenta de Coulomb integra la corriente.

💡 **Cómo se explica en la clase [B86-C06](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md):**
- Simular la carga con cuenta de Coulomb y una OCV con resistencia interna.
- 🎯 **Por qué importa:** Cargar más rápido reduce el tiempo pero eleva el calor y la tensión sobre la celda; cargar más lento puede no completar el ciclo antes del siguiente eclipse. El perfil de carga decide si la batería vuelve a su estado de carga en cada órbita.
- 🔗 **Se estudia junto con:** fase CC, fase CV, corriente de corte, tasa C.

📘 **Dónde se aprende** (1 clase): [B86-C06 · Gestión de carga](../programa/clases/B86/B86-C06-gestion-de-carga/CLASE.md).

### Cuenta integrada

- La cuenta integrada acumula ciclos de Doppler y da la variación de alcance.

💡 **Contexto en la clase [B74-C04](../programa/clases/B74/B74-C04-doppler-de-navegacion/CLASE.md):**
- 🎯 **Por qué importa:** Una velocidad radial de `1 mm/s` produce un desplazamiento de decenas de milihercios, medible; por eso el Doppler es el observable más preciso de la navegación en espacio profundo. La decisión central: ¿qué información da el Doppler (velocidad en la línea de visión) y qué no (posición transversal)?
- 🔗 **Se estudia junto con:** Doppler de dos sentidos, velocidad radial, sensibilidad.

📘 **Dónde se aprende** (1 clase): [B74-C04 · Doppler de navegación](../programa/clases/B74/B74-C04-doppler-de-navegacion/CLASE.md).

### Cuenta regresiva

- Una cuenta regresiva usa T− antes de un instante de referencia y T+ después.

💡 **Cómo se explica en la clase [B03-C09](../programa/clases/B03/B03-C09-operaciones-con-numeros-negativos/CLASE.md):**
- La cuenta regresiva es una recta de tiempo con signos.
- Datos: publicados (NASA, IAU, SI); la cuenta regresiva es sintética.
- 🎯 **Por qué importa:** Cuando observas una llamarada solar a las 12:00:00, el evento ocurrió antes: su tiempo es el observado menos 499 s. Si sumas en vez de restar, afirmas que la llamarada ocurre en el futuro.
- 🔗 **Se estudia junto con:** número negativo, opuesto, valor absoluto, recta numérica.

📘 **Dónde se aprende** (1 clase): [B03-C09 · Operaciones con números negativos](../programa/clases/B03/B03-C09-operaciones-con-numeros-negativos/CLASE.md).

### Cuentas

- Las cuentas son el número de partículas por canal.
- La línea del disco y las cuentas `4 × líneas`.

💡 **Cómo se explica en la clase [B35-C06](../programa/clases/B35/B35-C06-mediciones-in-situ-de-plasmas-espaciales/CLASE.md):**
- Con `σ = 28,730 km/s` y bins de `5,746 km/s`, 300 realizaciones de 20 000 cuentas dan: `V − V₀ = −11,9 m/s` (error estándar `11,6`), dispersión de `V` de `201,7 m/s` frente a `σ/√N = 203,2 m/s`, `T` media `100 078 K` con sesgo `78 K` (error estándar `53 K`) y dispersión `913 K` frente a `T√(2/N) = 1000 K`.
- El ruido de Poisson se controla con más cuentas (`σ_V ∝ 1/√N`).
- ⚠️ **Error frecuente:** Creer que más cuentas quitan el sesgo. Se corrige con 8.4.
- 🎯 **Por qué importa:** Un momento sin su incertidumbre ni sus sesgos no es una medición. La decisión central: ¿cuántas cuentas hacen falta y qué sesgos introduce el instrumento?
- 🔗 **Se estudia junto con:** momento, ventana, potencial de la nave, ruido de Poisson.

📘 **Dónde se aprende** (2 clases): [B35-C06 · Mediciones in situ de plasmas espaciales](../programa/clases/B35/B35-C06-mediciones-in-situ-de-plasmas-espaciales/CLASE.md); [B43-C16 · Encoders y medición angular](../programa/clases/B43/B43-C16-encoders-y-medicion-angular/CLASE.md).

### Cuerda

- La cuerda entre dos puntos de la esfera unidad es la longitud del segmento que los une, `|u − v|`; se relaciona con el ángulo por `|u − v| = 2 sen(γ/2)`.
- La cuerda `c` es la distancia entre los dos puntos y el semiperímetro `s = (r₁ + r₂ + c)/2`.
- La cuerda `c = |r2 − r1|`.

💡 **Cómo se explica en la clase [B04-C13](../programa/clases/B04/B04-C13-producto-escalar-y-angulo-entre-vectores/CLASE.md):**
- La fórmula por cuerda, `γ = 2 arcsen(|u − v|/2)`, no resta números casi iguales y da `1,000000 × 10⁻³″` en esos casos.
- Regla de la clase: usar la forma por cuerda cuando `γ` sea menor de unos minutos de arco.
- 🎯 **Por qué importa:** Antes de apuntar un telescopio de una estrella a otra, antes de saber si dos objetos caben en el mismo campo de visión, antes de decidir si un planeta está demasiado cerca del Sol para observarlo, hay que saber cuántos grados los separan en el cielo.
- 🔗 **Se estudia junto con:** producto escalar, ángulo entre vectores, perpendiculares, proyección.

📘 **Dónde se aprende** (3 clases): [B04-C13 · Producto escalar y ángulo entre vectores](../programa/clases/B04/B04-C13-producto-escalar-y-angulo-entre-vectores/CLASE.md); [B75-C04 · Ecuación de Lambert](../programa/clases/B75/B75-C04-ecuacion-de-lambert/CLASE.md); [B82-C01 · Lambert de arco corto](../programa/clases/B82/B82-C01-lambert-de-arco-corto/CLASE.md).

### Cuerpo celeste

- Un cuerpo celeste incluye la Luna.

💡 **Cómo se explica en la clase [B119-C11](../programa/clases/B119/B119-C11-uso-pacifico-y-limitaciones-militares/CLASE.md):**
- *Descripción textual:* primero se pregunta por armas de destrucción masiva; luego por el cuerpo celeste; por último por bases o ensayos; el resultado puede ser prohibido, condicionado, permitido o fuera del artículo.
- Paso 1. `loc = cuerpo celeste`, `wmd = 0`, `inst = 0`, `pers = 1`.
- 🎯 **Por qué importa:** C01 reduce el art. IV a una regla booleana; esta clase lo desagrega por ubicación y propósito y conecta con el art. 3 del Acuerdo sobre la Luna, y deja explícito lo no consultado.
- 🔗 **Se estudia junto con:** ADM, Condicionado, Fuera del art. IV, lista de reglas.

📘 **Dónde se aprende** (1 clase): [B119-C11 · Uso pacífico y limitaciones militares](../programa/clases/B119/B119-C11-uso-pacifico-y-limitaciones-militares/CLASE.md).

### Cuerpo gris

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Cómo se explica en la clase [B47-C04](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md):**
- Cuerpo gris con emisividad constante, sin fondo zodiacal ni emisión del cielo residual.
- Límites: cuerpo gris, sin fondo zodiacal.
- 🎯 **Por qué importa:** Enfriar un telescopio cuesta masa, potencia y complejidad. La decisión central: ¿a qué temperatura el fondo propio deja de dominar sobre el detector?
- 🔗 **Se estudia junto con:** ley de Planck, ley de Wien, ley de Stefan-Boltzmann, emisividad.

📘 **Dónde se aprende** (1 clase): [B47-C04 · Telescopios infrarrojos](../programa/clases/B47/B47-C04-telescopios-infrarrojos/CLASE.md).

### Cuerpo menor

- Un cuerpo menor es un asteroide o cometa.

💡 **Cómo se explica en la clase [B58-C01](../programa/clases/B58/B58-C01-clasificacion-de-cuerpos-menores/CLASE.md):**
- python programa/clases/B58/B58-C01-clasificacion-de-cuerpos-menores/clasificacion.py
- 🎯 **Por qué importa:** La pregunta que organiza el bloque es *¿qué es este objeto y qué tan cerca pasa?* Un mismo punto de luz puede ser un asteroide del cinturón principal sin ningún interés para la defensa planetaria o un objeto cercano a la Tierra.
- 🔗 **Se estudia junto con:** objeto cercano a la Tierra, grupos, parámetro de Tisserand, magnitud absoluta.

📘 **Dónde se aprende** (1 clase): [B58-C01 · Clasificación de cuerpos menores](../programa/clases/B58/B58-C01-clasificacion-de-cuerpos-menores/CLASE.md).

### Cuerpo menor del sistema solar

- Un cuerpo menor del sistema solar es cualquier otro objeto que orbita el Sol y no es satélite (la IAU incluye a la mayoría de los asteroides, la mayoría de los objetos transneptunianos y los cometas).

💡 **Cómo se explica en la clase [B01-C03](../programa/clases/B01/B01-C03-objetos-celestes-y-sus-diferencias/CLASE.md):**
- Aplicar los tres criterios de la IAU de 2006 para clasificar un cuerpo del sistema solar como planeta, planeta enano o cuerpo menor.
- Cometa: orbita el Sol, no es casi redondo → cuerpo menor del sistema solar (nota 3 de la B5: los cometas son cuerpos menores).
- 🎯 **Por qué importa:** En 2006 la Asamblea General de la Unión Astronómica Internacional votó una definición de planeta y, desde entonces, Plutón dejó de contarse como el noveno planeta. Muchas personas sintieron que «se había cambiado la realidad».
- 🔗 **Se estudia junto con:** planeta, planeta enano, satélite, estrella.

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
- 🔗 **Se estudia junto con:** longitud de onda, frecuencia, espectro, espectro continuo.

📖 **Explicado a fondo:** [Cuerpo negro](esencial/esencial-a-c.md#cuerpo-negro) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (5 clases): [B01-C09 · Luz como fuente de información](../programa/clases/B01/B01-C09-luz-como-fuente-de-informacion/CLASE.md); [B05-C13 · Temperatura y energía térmica](../programa/clases/B05/B05-C13-temperatura-y-energia-termica/CLASE.md); [B13-C17 · Calibración radiométrica](../programa/clases/B13/B13-C17-calibracion-radiometrica/CLASE.md); [B22-C04 · Inversión espectral](../programa/clases/B22/B22-C04-inversion-espectral/CLASE.md); [B28-C02 · Fotones en múltiples longitudes de onda](../programa/clases/B28/B28-C02-fotones-en-multiples-longitudes-de-onda/CLASE.md).

### Cuerpo rígido

- Un cuerpo rígido tiene un único `Ω`.

💡 **Cómo se explica en la clase [B37-C11](../programa/clases/B37/B37-C11-rotacion-interna-a-partir-del-desdoblamiento-de-frecuencias/CLASE.md):**
- Un cuerpo rígido (`0,25 μHz` en todos los modos) recupera `Ω_c = Ω_e = 0,250000`.
- cuerpo rigido (0,25 uHz en todos los modos): Omega_c = 0.250000 ;
- 🎯 **Por qué importa:** El desdoblamiento promedia la rotación de las regiones que el modo explora. La decisión central: ¿cuánto giran el núcleo y la envoltura y con qué incertidumbre y correlación?
- 🔗 **Se estudia junto con:** desdoblamiento rotacional, fracción de inercia, rotación diferencial, coeficiente de Ledoux.

📘 **Dónde se aprende** (1 clase): [B37-C11 · Rotación interna a partir del desdoblamiento de frecuencias](../programa/clases/B37/B37-C11-rotacion-interna-a-partir-del-desdoblamiento-de-frecuencias/CLASE.md).

### Culminación

- La culminación es el paso por el meridiano, el punto más alto del día.
- El ángulo horario `H` es el ángulo, medido hacia el oeste, entre el meridiano y el círculo que pasa por el astro y los polos; vale cero cuando el astro cruza el meridiano (tránsito o culminación, S2).
- La culminación (o tránsito meridiano) es el momento en que el astro cruza el meridiano, con `H = 0`.

💡 **Cómo se explica en la clase [B08-C04](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md):**
- Predecir cuándo un objeto sale, culmina y se pone.
- Ejercicio 1. ¿A qué altura culmina un astro de `δ = −45°` desde `φ = −30°`?
- 🎯 **Por qué importa:** Una tabla dice «Luna: AR 2,14 h, Dec +17,1°». Un telescopio, una cámara o tus ojos necesitan «a 35° de altura, hacia el nornoreste».
- 🔗 **Se estudia junto con:** altura, distancia cenital, acimut, ángulo horario.

📘 **Dónde se aprende** (3 clases): [B01-C11 · Movimiento aparente del Sol y las estrellas](../programa/clases/B01/B01-C11-movimiento-aparente-del-sol-y-las-estrellas/CLASE.md); [B08-C04 · Altura y acimut](../programa/clases/B08/B08-C04-altura-y-acimut/CLASE.md); [B09-C05 · Derivadas trigonométricas](../programa/clases/B09/B09-C05-derivadas-trigonometricas/CLASE.md).

### Cultura de seguridad

- La cultura de seguridad son las actitudes y prácticas compartidas sobre el riesgo.
- La cultura de seguridad se modela como un factor `r` que aumenta la tasa de reporte.

💡 **Cómo se explica en la clase [B111-C06](../programa/clases/B111/B111-C06-gestion-del-error-humano-y-cultura-de-seguridad/CLASE.md):**
- Pero las cifras son sintéticas, el modelo no distingue tipos de daño y la cultura de seguridad real no se reduce a un factor `r`.
- De 1000 casi-eventos se reportan `395` con las tasas sintéticas y `592,5` si una cultura de seguridad las multiplica por `1,5`.
- 🎯 **Por qué importa:** Falta la clase sobre tipos de error, barreras y reporte. La decisión central: ¿dónde se pone el esfuerzo: en culpar al que erró o en reforzar las barreras y las condiciones que dejaron pasar el error?
- 🔗 **Se estudia junto con:** resbalón, descuido, equivocación, violación.

📘 **Dónde se aprende** (2 clases): [B111-C06 · Gestión del error humano y cultura de seguridad](../programa/clases/B111/B111-C06-gestion-del-error-humano-y-cultura-de-seguridad/CLASE.md); [B119-C21 · Cultura de seguridad aeroespacial y aprendizaje de incidentes](../programa/clases/B119/B119-C21-cultura-de-seguridad-aeroespacial-y-aprendizaje-de-incidentes/CLASE.md).

### Cultura justa

- Una cultura justa protege el reporte honesto.

💡 **Contexto en la clase [B119-C21](../programa/clases/B119/B119-C21-cultura-de-seguridad-aeroespacial-y-aprendizaje-de-incidentes/CLASE.md):**
- 🎯 **Por qué importa:** B88-C16 cubre la seguridad funcional técnica; ninguna clase trata la dimensión cultural, y los indicadores de reportes se malinterpretan con facilidad. La decisión central: ¿qué indicador permite saber si una organización aprende cuando los reportes dependen de la confianza para informar?
- 🔗 **Se estudia junto con:** cultura de seguridad, fracción reportada, curva de aprendizaje, Subnotificación.

📘 **Dónde se aprende** (1 clase): [B119-C21 · Cultura de seguridad aeroespacial y aprendizaje de incidentes](../programa/clases/B119/B119-C21-cultura-de-seguridad-aeroespacial-y-aprendizaje-de-incidentes/CLASE.md).

### Cúmulo

- Un grupo de galaxias tiene unas cien o menos; un cúmulo puede contener miles (S3).
- Un grupo de galaxias reúne típicamente cien o menos (S1); un cúmulo, hasta miles (S1).

💡 **Cómo se explica en la clase [B01-C03](../programa/clases/B01/B01-C03-objetos-celestes-y-sus-diferencias/CLASE.md):**
- Un grupo reúne a unas cien galaxias o menos (la Vía Láctea y Andrómeda pertenecen al Grupo Local, con más de 50 galaxias), y un cúmulo puede reunir miles, como el de Virgo de C02 (S3).
- Los planetas orbitan estrellas; las estrellas forman galaxias; las galaxias forman grupos y cúmulos.
- 🎯 **Por qué importa:** En 2006 la Asamblea General de la Unión Astronómica Internacional votó una definición de planeta y, desde entonces, Plutón dejó de contarse como el noveno planeta. Muchas personas sintieron que «se había cambiado la realidad».
- 🔗 **Se estudia junto con:** planeta, planeta enano, cuerpo menor del sistema solar, satélite.

📘 **Dónde se aprende** (2 clases): [B01-C03 · Objetos celestes y sus diferencias](../programa/clases/B01/B01-C03-objetos-celestes-y-sus-diferencias/CLASE.md); [B01-C15 · Galaxias y agrupaciones cósmicas](../programa/clases/B01/B01-C15-galaxias-y-agrupaciones-cosmicas/CLASE.md).

### Cúmulo abierto

- Un cúmulo abierto es un grupo ligado de estrellas jóvenes y poco masivo del disco; un cúmulo globular es un grupo masivo, esférico y viejo; un cúmulo masivo joven (S2) tiene menos de ~100 Myr y más de ~10⁴ M☉.

💡 **Cómo se explica en la clase [B25-C06](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md):**
- Los cúmulos abiertos son grupos menos masivos del disco.
- Distinguir cúmulo abierto, globular y masivo joven, y nombrar sus rangos de edad y masa citados.
- 🎯 **Por qué importa:** La mayoría de las estrellas nace en grupos. Los cúmulos son laboratorios: sus estrellas comparten edad, distancia y composición.
- 🔗 **Se estudia junto con:** cúmulo globular, cúmulo masivo joven, perfil de Plummer, radio de media masa.

📘 **Dónde se aprende** (1 clase): [B25-C06 · Cúmulos estelares](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md).

### Cúmulo de escombros

- Un cúmulo de escombros (*rubble pile*) es un cuerpo hecho de fragmentos unidos por gravedad.

💡 **Contexto en la clase [B58-C03](../programa/clases/B58/B58-C03-composicion-de-asteroides/CLASE.md):**
- **Idea central (modelo mental):** ```mermaid flowchart LR M["masa M"] --> B["densidad aparente<br/>M/V"] V["volumen V"] --> B B --> P["porosidad<br/>1 - rho_b/rho_g"] G["densidad de grano"] --> P ``` *Descripción textual:* la masa y el volumen dan la densidad aparente; con la densidad de grano se obtiene la porosidad.
- 🎯 **Por qué importa:** La densidad aparente de un asteroide es casi siempre menor que la de sus rocas: la diferencia es porosidad, y de ella depende cuánta energía hace falta para desviarlo o fragmentarlo (C17). La decisión central: ¿cuánto de lo que parece masa es vacío, y cuánta incertidumbre arrastra la masa?
- 🔗 **Se estudia junto con:** densidad aparente, densidad de grano, porosidad, propagación de errores.

📘 **Dónde se aprende** (1 clase): [B58-C03 · Composición de asteroides](../programa/clases/B58/B58-C03-composicion-de-asteroides/CLASE.md).

### Cúmulo de galaxias

- Un cúmulo de galaxias es un sistema ligado de cientos a miles de galaxias, gas caliente y materia oscura.

💡 **Cómo se explica en la clase [B25-C13](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md):**
- Los dos métodos coinciden por construcción en este ejemplo sintético: en un cúmulo real, comparar la masa del gas con la de la dispersión de galaxias es una verificación de los supuestos.
- Definir cúmulo de galaxias, medio intracúmulo, equilibrio hidrostático y perfil beta.
- 🎯 **Por qué importa:** Los cúmulos de galaxias son las mayores estructuras ligadas por la gravedad. Contienen galaxias, un gas a decenas de millones de kelvin y mucha más masa de la que ambos aportan; por eso sirven para estudiar la materia oscura y poner a prueba el modelo cosmológico.
- 🔗 **Se estudia junto con:** medio intracúmulo (ICM), temperatura, equilibrio hidrostático, perfil beta.

📘 **Dónde se aprende** (1 clase): [B25-C13 · Cúmulos de galaxias](../programa/clases/B25/B25-C13-cumulos-de-galaxias/CLASE.md).

### Cúmulo estelar

- Un cúmulo estelar es un conjunto ligado de estrellas nacidas de la misma nube.

💡 **Cómo se explica en la clase [B24-C19](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md):**
- python programa/clases/B24/B24-C19-cumulos-y-edades-estelares/cumulo.py
- 🎯 **Por qué importa:** La edad de una estrella aislada es difícil de medir; la de un cúmulo se puede leer en su diagrama HR, porque las estrellas más masivas ya han salido de la secuencia principal y el «punto de desvío» marca la edad. Esas edades fijan la cronología de la Galaxia y calibran los modelos.
- 🔗 **Se estudia junto con:** punto de desvío, isócrona, función inicial de masa, ilustrativo.

📘 **Dónde se aprende** (1 clase): [B24-C19 · Cúmulos y edades estelares](../programa/clases/B24/B24-C19-cumulos-y-edades-estelares/CLASE.md).

### Cúmulo globular

- Un cúmulo abierto es un grupo ligado de estrellas jóvenes y poco masivo del disco; un cúmulo globular es un grupo masivo, esférico y viejo; un cúmulo masivo joven (S2) tiene menos de ~100 Myr y más de ~10⁴ M☉.

💡 **Cómo se explica en la clase [B25-C06](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md):**
- Harris (S1) cataloga `157` objetos clasificados como cúmulos globulares de la Vía Láctea, con coordenadas, metalicidades, parámetros estructurales y dispersión central de velocidades.
- Distinguir cúmulo abierto, globular y masivo joven, y nombrar sus rangos de edad y masa citados.
- 🎯 **Por qué importa:** La mayoría de las estrellas nace en grupos. Los cúmulos son laboratorios: sus estrellas comparten edad, distancia y composición.
- 🔗 **Se estudia junto con:** cúmulo abierto, cúmulo masivo joven, perfil de Plummer, radio de media masa.

📖 **Explicado a fondo:** [Cúmulo globular](esencial/tercera-a-e.md#cúmulo-globular) (intuición, fórmula, ejemplo numérico y errores frecuentes).

📘 **Dónde se aprende** (1 clase): [B25-C06 · Cúmulos estelares](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md).

### Cúmulo masivo joven

- Un cúmulo abierto es un grupo ligado de estrellas jóvenes y poco masivo del disco; un cúmulo globular es un grupo masivo, esférico y viejo; un cúmulo masivo joven (S2) tiene menos de ~100 Myr y más de ~10⁴ M☉.

💡 **Cómo se explica en la clase [B25-C06](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md):**
- Portegies Zwart, McMillan y Gieles (S2) revisan los cúmulos jóvenes masivos: más jóvenes que unos `100 Myr` y más masivos que unos `10⁴ M☉`.
- Distinguir cúmulo abierto, globular y masivo joven, y nombrar sus rangos de edad y masa citados.
- 🎯 **Por qué importa:** La mayoría de las estrellas nace en grupos. Los cúmulos son laboratorios: sus estrellas comparten edad, distancia y composición.
- 🔗 **Se estudia junto con:** cúmulo abierto, cúmulo globular, perfil de Plummer, radio de media masa.

📘 **Dónde se aprende** (1 clase): [B25-C06 · Cúmulos estelares](../programa/clases/B25/B25-C06-cumulos-estelares/CLASE.md).

### Cuota

- La cuota `s_i` es `q_i/Q`.
- La cuota es el peso mínimo para ganar una votación.

💡 **Cómo se explica en la clase [B48-C02](../programa/clases/B48/B48-C02-concesion-de-tiempo-de-observacion/CLASE.md):**
- Ambos métodos coinciden aquí; con otras cuotas pueden diferir en una hora.
- Como repartir una torta en porciones enteras: las cuotas dan trozos con fracciones y alguna regla decide quién recibe las migas sobrantes.
- 🎯 **Por qué importa:** Un reparto sin regla clara genera conflicto, y uno sin clima genera promesas incumplibles. La decisión central: ¿cuántas horas se asignan y cuántas se esperan efectivas?
- 🔗 **Se estudia junto con:** Sobresuscripción, Método de Hamilton, Método de D'Hondt, Horas efectivas.

📘 **Dónde se aprende** (3 clases): [B48-C02 · Concesión de tiempo de observación](../programa/clases/B48/B48-C02-concesion-de-tiempo-de-observacion/CLASE.md); [B124-C03 · Mercados downstream y upstream](../programa/clases/B124/B124-C03-mercados-downstream-y-upstream/CLASE.md); [B125-C03 · Gobierno corporativo de una empresa espacial](../programa/clases/B125/B125-C03-gobierno-corporativo-de-una-empresa-espacial/CLASE.md).

### Cuota inicial

- La cuota inicial `U` se paga al firmar.

💡 **Cómo se explica en la clase [B124-C09](../programa/clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md):**
- Paso 4 · Con cuota. Con una cuota inicial de 1: valor total `2,2434` Mum.
- Distinguir cuota inicial, regalía y valor actual de la licencia.
- 🎯 **Por qué importa:** La propiedad intelectual es un activo, pero su valor depende de cuánto se vende con ella y de cuánto del margen se queda el que la usa. La decisión central: ¿qué licencia conviene ofrecer y cuántas regalías soporta el licenciatario?
- 🔗 **Se estudia junto con:** licencia, regalía, valor actual, apilamiento.

📘 **Dónde se aprende** (1 clase): [B124-C09 · Propiedad intelectual y licencias](../programa/clases/B124/B124-C09-propiedad-intelectual-y-licencias/CLASE.md).

### Cuota interna

- La cuota interna es la parte final de cada responsable.

💡 **Cómo se explica en la clase [B119-C03](../programa/clases/B119/B119-C03-convenio-de-responsabilidad/CLASE.md):**
- Culpas 0,7 y 0,3: cuotas internas `A = 70.0` y `B = 30.0` u.m.; la víctima puede cobrar los 100 de A o de B.
- Si A no puede pagar, B paga `100.0` u.m. a la víctima; su cuota interna es `30.0`; reclama a A el regreso de `70.0` u.m.
- 🎯 **Por qué importa:** El art. VII del tratado de 1967 (no discutido en la fuente de C01) fundamenta la responsabilidad; el convenio de 1972 la desarrolla, y la cuantificación del daño se trata en el bloque de reclamaciones (B123); esta clase fija la regla de reparto.
- 🔗 **Se estudia junto con:** responsabilidad absoluta, responsabilidad por culpa, solidaridad, regreso.

📘 **Dónde se aprende** (1 clase): [B119-C03 · Convenio de Responsabilidad](../programa/clases/B119/B119-C03-convenio-de-responsabilidad/CLASE.md).

### Cuota parte

- La cuota parte cede una fracción fija `q` de cada siniestro y de la prima.

💡 **Cómo se explica en la clase [B127-C07](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md):**
- La cuota parte lo hace barato porque la comisión es generosa (dato sintético); el exceso de pérdida lo hace caro pero solo protege contra siniestros grandes, como los que dominan este tipo de cartera, y deja intacta la frecuencia de los pequeños.
- X["siniestro X"] --> Q["cuota parte: reasegurador paga q X"]
- 🎯 **Por qué importa:** El riesgo espacial se reparte mediante reaseguro; no había clase al respecto. La decisión central: ¿qué parte del riesgo se cede y cuánto cuesta reducir la cola?
- 🔗 **Se estudia junto con:** cesión, exceso de pérdida, prioridad, límite.

📘 **Dónde se aprende** (1 clase): [B127-C07 · Reaseguro espacial](../programa/clases/B127/B127-C07-reaseguro-espacial/CLASE.md).

### Curaduría

- La curaduría es el cuidado, registro y distribución de una colección.

💡 **Cómo se explica en la clase [B63-C03](../programa/clases/B63/B63-C03-curaduria-y-cadena-de-custodia-de-muestras/CLASE.md):**
- La página de curaduría no detalla procedimientos de manejo ni de contaminación, y esos procedimientos no se describen aquí como reales.
- python programa/clases/B63/B63-C03-curaduria-y-cadena-de-custodia-de-muestras/custodia.py
- 🎯 **Por qué importa:** Una muestra planetaria es irrepetible y se estudia durante décadas. La decisión central: ¿cómo demuestras, años después, qué le pasó a una muestra y cuánto de lo que mides es suyo?
- 🔗 **Se estudia junto con:** cadena de custodia, hash, encadenamiento, alícuota.

📘 **Dónde se aprende** (1 clase): [B63-C03 · Curaduría y cadena de custodia de muestras](../programa/clases/B63/B63-C03-curaduria-y-cadena-de-custodia-de-muestras/CLASE.md).

### Curtosis

- La curtosis mide las colas.
- La curtosis mide su carácter impulsivo.
- La curtosis `E[x⁴]/σ⁴` vale 3 en una gaussiana.

💡 **Cómo se explica en la clase [B35-C09](../programa/clases/B35/B35-C09-turbulencia-en-plasmas-y-mhd/CLASE.md):**
- Un campo gaussiano tiene curtosis 3 a todas las escalas; la cascada multiplicativa la hace crecer al disminuir la escala.
- La curtosis de los incrementos gaussianos es `≈ 3`, mientras que una cascada binomial con `p = 0,7` llega a `106,6` en 12 niveles.
- 🎯 **Por qué importa:** La pendiente de un espectro y su intermitencia distinguen modelos de turbulencia. La decisión central: ¿qué pendiente y qué curtosis tiene la serie y qué modelo sugiere?
- 🔗 **Se estudia junto con:** espectro, función de estructura, intermitencia, cascada.

📘 **Dónde se aprende** (3 clases): [B35-C09 · Turbulencia en plasmas y MHD](../programa/clases/B35/B35-C09-turbulencia-en-plasmas-y-mhd/CLASE.md); [B84-C32 · Vibración aleatoria y densidad espectral de potencia](../programa/clases/B84/B84-C32-vibracion-aleatoria-y-densidad-espectral-de-potencia/CLASE.md); [B97-C26 · Monitoreo de condición de maquinaria extraterrestre](../programa/clases/B97/B97-C26-monitoreo-de-condicion-de-maquinaria-extraterrestre/CLASE.md).

### Curtosis en exceso

- La asimetría y la curtosis en exceso: momentos de la forma de `z`.

💡 **Cómo se explica en la clase [B51-C07](../programa/clases/B51/B51-C07-evaluacion-de-residuos-y-diagnostico-de-calidad-de-calibracion/CLASE.md):**
- desviacion de z = 0.8861 ; asimetria = +0.0226 ; curtosis en exceso = +0.0994
- 🎯 **Por qué importa:** Una calibración mala puede dar una imagen bonita. La decisión central: ¿qué valor de χ² reducido y qué forma de los residuos indican que el modelo es suficiente?
- 🔗 **Se estudia junto con:** residuo, residuo normalizado, grados de libertad, χ² reducido.

📘 **Dónde se aprende** (1 clase): [B51-C07 · Evaluación de residuos y diagnóstico de calidad de calibración](../programa/clases/B51/B51-C07-evaluacion-de-residuos-y-diagnostico-de-calidad-de-calibracion/CLASE.md).

### Curva

- Una curva tiene pendiente que cambia.

💡 **Cómo se explica en la clase [B03-C16](../programa/clases/B03/B03-C16-pendiente-e-interpretacion-de-graficos/CLASE.md):**
- En escalas lineales, el gráfico `T` frente a `a` de los planetas es una curva.
- Hablar de «la pendiente» de una curva es engañoso: cada tramo tiene la suya.
- ⚠️ **Error frecuente:** Hablar de «la pendiente» de una curva. Ejercicio 8.
- 🎯 **Por qué importa:** Si sitúas en un gráfico logarítmico el período frente al semieje de los planetas, los puntos forman una recta. Su pendiente es 1,5: ese número es el exponente de la tercera ley de Kepler.
- 🔗 **Se estudia junto con:** pendiente, ordenada en el origen, recta, relación lineal.

📘 **Dónde se aprende** (1 clase): [B03-C16 · Pendiente e interpretación de gráficos](../programa/clases/B03/B03-C16-pendiente-e-interpretacion-de-graficos/CLASE.md).

### Curva de aprendizaje

- Una curva de aprendizaje relaciona el error con el número de sesiones.
- La curva de aprendizaje muestra la baja de la tasa de fallas con la experiencia.
- La curva de aprendizaje de Wright da `T_n = T₁ n^β` con `β = log₂(pendiente)`.

💡 **Cómo se explica en la clase [B107-C03](../programa/clases/B107/B107-C03-entrenamiento-vestibular-y-de-orientacion-espacial/CLASE.md):**
- Una curva de aprendizaje sintética baja de 20,0° a `5,01°` en 20 sesiones;
- Ajustar una curva de aprendizaje `e_k = e∞ + (e0 − e∞) r^k` y calcular sesiones al 95 %.
- 🎯 **Por qué importa:** Los fragmentos consultados indican que tras el vuelo hay alteraciones del control postural y locomotor (Macaulay et al., 2021) y que el equilibrio dinámico, la percepción del tiempo y el tiempo de reacción cambian tras el aterrizaje (Clément et al., 2023). Antes del vuelo la pregunta es cómo preparar la desorientación.
- 🔗 **Se estudia junto con:** canal semicircular, otolito, ambigüedad inclinación-traslación.

📘 **Dónde se aprende** (3 clases): [B107-C03 · Entrenamiento vestibular y de orientación espacial](../programa/clases/B107/B107-C03-entrenamiento-vestibular-y-de-orientacion-espacial/CLASE.md); [B119-C21 · Cultura de seguridad aeroespacial y aprendizaje de incidentes](../programa/clases/B119/B119-C21-cultura-de-seguridad-aeroespacial-y-aprendizaje-de-incidentes/CLASE.md); [B124-C05 · Estimación de costos de misión](../programa/clases/B124/B124-C05-estimacion-de-costos-de-mision/CLASE.md).

### Curva de calibración

- La curva de calibración es la relación entre indicación y valor de la magnitud.

💡 **Cómo se explica en la clase [B13-C05](../programa/clases/B13/B13-C05-calibracion-instrumental/CLASE.md):**
- La evidencia es la curva de calibración con su incertidumbre del ejercicio 12 (sección 20).
- 🎯 **Por qué importa:** Un sensor solar de una nave devuelve cuentas digitales (DN), no vatios por metro cuadrado. Para saber cuánta luz recibe hay que haberlo expuesto antes a fuentes de irradiancia conocida y haber establecido la relación entre ambas.
- 🔗 **Se estudia junto con:** calibración, indicación, mínimos cuadrados ordinarios, residuo.

📘 **Dónde se aprende** (1 clase): [B13-C05 · Calibración instrumental](../programa/clases/B13/B13-C05-calibracion-instrumental/CLASE.md).

### Curva de costo

- La curva de costo tiene un mínimo de delta-v en el tiempo de Hohmann.

💡 **Cómo se explica en la clase [B75-C27](../programa/clases/B75/B75-C27-duracion-de-mision-y-tiempo-de-vuelo-como-restriccion/CLASE.md):**
- La evidencia es tu curva de costo total del ejercicio 12 (sección 20).
- Ejercicio 12 · integrador. Elabora tu *curva de costo total* para un `c_t` que justifiques: tabla de `TOF`, `Δv`, `m₀`, `J`, el óptimo y la comparación con Hohmann.
- 🎯 **Por qué importa:** Un viaje más corto gasta más combustible y uno más largo gasta más tiempo. La decisión central: ¿qué tiempo de vuelo minimiza el costo total cuando se pesan la masa lanzada y la duración?
- 🔗 **Se estudia junto con:** costo total, delta-v mínimo para un tiempo, óptimo.

📘 **Dónde se aprende** (1 clase): [B75-C27 · Duración de misión y tiempo de vuelo como restricción](../programa/clases/B75/B75-C27-duracion-de-mision-y-tiempo-de-vuelo-como-restriccion/CLASE.md).

### Curva de crecimiento

- La curva de crecimiento es `W` frente a la columna.

💡 **Cómo se explica en la clase [B32-C09](../programa/clases/B32/B32-C09-medicion-de-perfiles-de-linea-ancho-equivalente-y-ajuste/CLASE.md):**
- La evidencia es la ficha de la curva de crecimiento del ejercicio 12 (sección 20).
- Ejercicio 12. Integrador. Elabora tu *ficha de la curva de crecimiento*: tabla y regímenes.
- 🎯 **Por qué importa:** Medir una abundancia exige saber en qué régimen está la línea. La decisión central: ¿cómo depende el ancho equivalente de la columna de absorbedores?
- 🔗 **Se estudia junto con:** ancho equivalente, profundidad óptica central, régimen lineal, saturado.

📘 **Dónde se aprende** (2 clases): [B32-C09 · Medición de perfiles de línea: ancho equivalente y ajuste](../programa/clases/B32/B32-C09-medicion-de-perfiles-de-linea-ancho-equivalente-y-ajuste/CLASE.md); [B45-C11 · Líneas de absorción](../programa/clases/B45/B45-C11-lineas-de-absorcion/CLASE.md).

### Curva de fase

- La curva de fase pliega la serie al periodo.

💡 **Cómo se explica en la clase [B29-C14](../programa/clases/B29/B29-C14-estrellas-variables-periodicas/CLASE.md):**
- *Descripción textual:* se ajusta una curva armónica para cada frecuencia y se toma el mínimo de `χ²`; la dispersión de fase da un estimador independiente; ambos coinciden y la incertidumbre de una sinusoide sigue una fórmula estándar.
- 🎯 **Por qué importa:** El periodo es la propiedad básica de una variable periódica; de él y de la forma de la curva se deducen la masa, la edad o la distancia en muchos casos. La decisión central: ¿qué periodo y qué incertidumbre da la serie y qué métodos coinciden?
- 🔗 **Se estudia junto con:** armónico, dispersión de fase, rejilla de frecuencias, amplitud.

📘 **Dónde se aprende** (1 clase): [B29-C14 · Estrellas variables periódicas](../programa/clases/B29/B29-C14-estrellas-variables-periodicas/CLASE.md).

### Curva de Hill

- La curva de Hill `R(L) = Rmax L/(L + L50)` satura en `Rmax`;

💡 **Cómo se explica en la clase [B105-C16](../programa/clases/B105/B105-C16-contramedidas-de-ejercicio/CLASE.md):**
- Una curva de Hill `R = Rmax L/(L + L50)` con `Rmax = 0,8` y `L50 = 100` (ilustrativas) reduce la pérdida ósea: con `L = 100`, `R = 0,40` y la pérdida a 6 meses baja de 7,27 % a 4,21 %; con `L = 800`, a 2,15 %.
- Ajustar una curva de Hill de dosis–respuesta a datos sintéticos por mínimos cuadrados.
- 🎯 **Por qué importa:** Más ejercicio ayuda, pero con rendimientos decrecientes y con un costo de energía y tiempo. La decisión central: ¿qué parte de la pérdida se evita con una carga dada y cuánta energía extra exige?
- 🔗 **Se estudia junto con:** MET, carga semanal, reducción relativa, fuerza de reacción.

📘 **Dónde se aprende** (1 clase): [B105-C16 · Contramedidas de ejercicio](../programa/clases/B105/B105-C16-contramedidas-de-ejercicio/CLASE.md).

### Curva de la bañera

- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.

💡 **Contexto en la clase [B47-C19](../programa/clases/B47/B47-C19-mantenimiento-y-vida-util/CLASE.md):**
- **Idea central (modelo mental):** Es una cadena: se rompe por el eslabón más débil; duplicar un eslabón fuerte no sirve si otro se gasta antes.
- 🎯 **Por qué importa:** No sirve duplicar un equipo si otro componente falla antes. La decisión central: ¿qué recurso limita la vida de la misión y qué redundancia vale la pena?
- 🔗 **Se estudia junto con:** confiabilidad, tasa de falla, redundancia, propulsor.

📘 **Dónde se aprende** (1 clase): [B47-C19 · Mantenimiento y vida útil](../programa/clases/B47/B47-C19-mantenimiento-y-vida-util/CLASE.md).

### Curva de Lorenz

- La curva de Lorenz la visualiza.

💡 **Contexto en la clase [B119-C34](../programa/clases/B119/B119-C34-equidad-de-acceso-al-espacio/CLASE.md):**
- 🎯 **Por qué importa:** El acceso desigual al espacio es un asunto de gobernanza que el catálogo no trata; esta clase da las herramientas de medición antes de las discusiones de política (C25, C36). La decisión central: ¿qué tan desigual es el acceso y cuánto lo reduce una regla de uso compartido?
- 🔗 **Se estudia junto con:** Gini, índice de Atkinson, fondo compartido, equidad.

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
- 🔗 **Se estudia junto con:** transitorio, índice de caída, límite de detección, cadencia.

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
- 🔗 **Se estudia junto con:** función de dos variables, dominio, gráfica, corte.

📘 **Dónde se aprende** (2 clases): [B09-C15 · Funciones de varias variables](../programa/clases/B09/B09-C15-funciones-de-varias-variables/CLASE.md); [B09-C17 · Gradiente y derivada direccional](../programa/clases/B09/B09-C17-gradiente-y-derivada-direccional/CLASE.md).

### Curva de olvido

- La curva de olvido `R = e^(−Δt/S)` da la retención tras `Δt` días con estabilidad `S`.

💡 **Cómo se explica en la clase [B104-C06](../programa/clases/B104/B104-C06-entrenamiento-de-procedimientos/CLASE.md):**
- Calcular la retención con una curva de olvido exponencial.
- ⚠️ **Error frecuente:** Suponer que el dominio es permanente. Aplica la curva de olvido (8.3).
- 🎯 **Por qué importa:** Los procedimientos se practican en tierra y a veces se usan meses después, en el momento crítico. La decisión central: ¿cuándo repasar para que el procedimiento siga disponible sin gastar tiempo de entrenamiento de más?
- 🔗 **Se estudia junto con:** ley de práctica, repaso espaciado, sobreaprendizaje.

📘 **Dónde se aprende** (1 clase): [B104-C06 · Entrenamiento de procedimientos](../programa/clases/B104/B104-C06-entrenamiento-de-procedimientos/CLASE.md).

### Curva de partición

- La curva de partición (de Tromp) da la probabilidad de que un grano de tamaño `d` vaya a un producto.

💡 **Cómo se explica en la clase [B59-C22](../programa/clases/B59/B59-C22-beneficio-y-separacion-granulometrica-de-regolito/CLASE.md):**
- Describir una curva de partición con tamaño de corte y agudeza.
- Ejercicio 12 · integrador. Elabora tu *ficha del beneficio*: curva de partición, leyes, recuperación, balance cerrado y compromiso al variar `d50`.
- 🎯 **Por qué importa:** Calentar o reducir todo el regolito es caro; separar la fracción rica antes ahorra energía. La decisión central: ¿qué tamaño de corte equilibra la ley del concentrado y la recuperación del mineral?
- 🔗 **Se estudia junto con:** tamaño de corte, imperfección, rendimiento másico, razón de enriquecimiento.

📘 **Dónde se aprende** (1 clase): [B59-C22 · Beneficio y separación granulométrica de regolito](../programa/clases/B59/B59-C22-beneficio-y-separacion-granulometrica-de-regolito/CLASE.md).

### Curva de polarización

- La curva de polarización `V(i)` suma el potencial reversible, la caída óhmica y la activación.

💡 **Cómo se explica en la clase [B59-C10](../programa/clases/B59/B59-C10-electrolisis-y-balances-energeticos/CLASE.md):**
- *Descripción textual:* la entalpía fija la tensión termoneutra; la curva de polarización da la tensión de operación; su comparación indica si la celda absorbe o cede calor.
- Leer una curva de polarización y su eficiencia.
- 🎯 **Por qué importa:** La electrólisis es el mayor consumidor de energía de la planta. La decisión central: ¿a qué densidad de corriente conviene operar, entre una celda pequeña que gasta más electricidad y una grande que gasta menos?
- 🔗 **Se estudia junto con:** tensión termoneutra, modo endotérmico, exotérmico, eficiencia farádica.

📘 **Dónde se aprende** (1 clase): [B59-C10 · Electrólisis y balances energéticos](../programa/clases/B59/B59-C10-electrolisis-y-balances-energeticos/CLASE.md).

### Curva de precisión–exhaustividad

- La curva de precisión–exhaustividad grafica precisión contra exhaustividad, y la precisión promedio resume su área (S2).

💡 **Cómo se explica en la clase [B17-C12](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md):**
- La curva ROC no cambia con la prevalencia, porque usa tasas dentro de cada clase; la de precisión–exhaustividad sí, y por eso refleja la carga de falsos positivos.
- Grafica las dos curvas (ROC y precisión–exhaustividad) en paneles separados con trazos distintos y describe en texto que la primera se acerca a la esquina superior izquierda y la segunda cae pronto.
- 🎯 **Por qué importa:** Un modelo marca candidatos a planeta, y cada alerta cuesta horas de revisión. Si el modelo acierta el 99 % en una muestra donde el 99 % son negativos, no dice nada útil.
- 🔗 **Se estudia junto con:** matriz de confusión, verdaderos positivos, falsos positivos, verdaderos negativos.

📘 **Dónde se aprende** (1 clase): [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md).

### Curva de rotación

- La curva de rotación es la velocidad circular en función del radio.
- La curva de rotación `v(R)` da la velocidad circular en función del radio.

💡 **Cómo se explica en la clase [B25-C08](../programa/clases/B25/B25-C08-curvas-de-rotacion-de-galaxias/CLASE.md):**
- *Descripción textual:* del disco visible se calcula su curva de rotación; la diferencia de cuadrados con la observada indica la masa que falta, que se modela como un halo.
- Rotación y curva de un disco (esta clase): directa y sencilla, pero supone órbitas circulares.
- 🎯 **Por qué importa:** Si la masa estuviera donde brilla, la velocidad de rotación debería caer en las afueras de una galaxia, como la de los planetas lejanos del Sol. Que una curva de rotación se mantenga plana indica más masa de la que se ve.
- 🔗 **Se estudia junto con:** velocidad circular, disco exponencial delgado, funciones de Bessel modificadas, halo pseudo-isotermo.

📘 **Dónde se aprende** (4 clases): [B25-C08 · Curvas de rotación de galaxias](../programa/clases/B25/B25-C08-curvas-de-rotacion-de-galaxias/CLASE.md); [B26-C18 · Materia oscura y evidencias](../programa/clases/B26/B26-C18-materia-oscura-y-evidencias/CLASE.md); [B31-C17 · Materias oscuras candidatas](../programa/clases/B31/B31-C17-materias-oscuras-candidatas/CLASE.md); [B46-C11 · Observación de hidrógeno a 21 centímetros](../programa/clases/B46/B46-C11-observacion-de-hidrogeno-a-21-centimetros/CLASE.md).

### Curva de transferencia

- Plano (*flat*): imagen de iluminación uniforme. Curva de transferencia: varianza contra media.

💡 **Contexto en la clase [B48-C13](../programa/clases/B48/B48-C13-calibraciones-nocturnas/CLASE.md):**
- **Idea central (modelo mental):** Como contar granos de arena: la fluctuación de la cuenta dice cuántos granos hay por unidad; la pendiente de la varianza revela el tamaño del grano (la ganancia).
- 🎯 **Por qué importa:** Sin ganancia ni ruido de lectura, las incertidumbres de cada medida no se pueden calcular. La decisión central: ¿cuánto valen la ganancia y el ruido de lectura del detector?
- 🔗 **Se estudia junto con:** Ganancia, Ruido de lectura, Ruido de disparo, Plano.

📘 **Dónde se aprende** (1 clase): [B48-C13 · Calibraciones nocturnas](../programa/clases/B48/B48-C13-calibraciones-nocturnas/CLASE.md).

### Curva de transferencia de fotones

- La curva de transferencia de fotones es `var = media/g + RN²/g²`.
- La curva de transferencia de fotones (PTC): varianza frente a media.

💡 **Contexto en la clase [B45-C19](../programa/clases/B45/B45-C19-reduccion-e-incertidumbre-instrumental/CLASE.md):**
- **Idea central (modelo mental):** Como cocinar con una balanza imprecisa: tara (sesgo), corriente de aire (oscuro) y platos de distinto tamaño (plano); el ruido total suma las incertidumbres de cada paso.
- 🎯 **Por qué importa:** Un flujo sin incertidumbre no es una medida. La decisión central: ¿qué términos dominan el ruido y cómo se estiman ganancia y ruido de lectura?
- 🔗 **Se estudia junto con:** sesgo, oscuro, ganancia, ecuación del CCD.

📘 **Dónde se aprende** (2 clases): [B45-C19 · Reducción e incertidumbre instrumental](../programa/clases/B45/B45-C19-reduccion-e-incertidumbre-instrumental/CLASE.md); [B47-C15 · Calibración a bordo](../programa/clases/B47/B47-C15-calibracion-a-bordo/CLASE.md).

### Curva diferencial

- La curva diferencial es objetivo/comparación.

💡 **Cómo se explica en la clase [B45-C17](../programa/clases/B45/B45-C17-fotometria-diferencial/CLASE.md):**
- Ejercicio 12. Integrador. Elabora tu *ficha de fotometría diferencial*: curvas, ruido previsto, profundidad y límites.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de fotometría diferencial*: curvas, ruido previsto, profundidad y límites.
- 🎯 **Por qué importa:** La atmósfera varía más que la señal; sin una referencia, la curva de luz no sirve. La decisión central: ¿qué comparaciones y qué precisión se necesitan para una profundidad dada?
- 🔗 **Se estudia junto con:** transparencia, conjunto, ruido de fotones, profundidad.

📘 **Dónde se aprende** (1 clase): [B45-C17 · Fotometría diferencial](../programa/clases/B45/B45-C17-fotometria-diferencial/CLASE.md).

### Curva dosis-profundidad

- La curva dosis-profundidad `D(x) ∝ (1 + x/x₀)^−p`.

💡 **Cómo se explica en la clase [B85-C22](../programa/clases/B85/B85-C22-modelos-de-exposicion-a-radiacion-en-orbita/CLASE.md):**
- *Descripción textual:* la órbita da la posición geográfica en cada instante, el mapa sintético da la tasa local, el promedio sobre un día da la dosis diaria y anual, y la curva dosis-profundidad ajusta el blindaje.
- Ejercicio 12 · integrador. Integrador. Elabora tu *ficha de dosis por órbita (sintética)*: tabla por altitud e inclinación, curva dosis-profundidad, convergencia y lista de lo consultado, sintético y no usado.
- 🎯 **Por qué importa:** La dosis anual decide el blindaje y la vida de la electrónica y los materiales. La decisión central: ¿cuánta dosis acumula una órbita al año y cuánto la reduce un milímetro más de blindaje?
- 🔗 **Se estudia junto con:** mapa de flujo, promedio orbital, inclinación.

📘 **Dónde se aprende** (1 clase): [B85-C22 · Modelos de exposición a radiación en órbita](../programa/clases/B85/B85-C22-modelos-de-exposicion-a-radiacion-en-orbita/CLASE.md).

### Curva en V

- HFD: diámetro de media energía de una estrella. Curva en V: HFD contra posición.

💡 **Contexto en la clase [B48-C22](../programa/clases/B48/B48-C22-control-automatico-del-enfocador-y-autoenfoque/CLASE.md):**
- **Idea central (modelo mental):** Es encontrar el fondo de un valle a partir de unos pocos puntos de la ladera: la parábola ajustada indica dónde está el fondo.
- 🎯 **Por qué importa:** Un enfoque erróneo pierde resolución en todas las imágenes de la noche. La decisión central: ¿en qué posición del enfocador está el mínimo y con qué incertidumbre?
- 🔗 **Se estudia junto con:** HFD, Enfocador, Número f, Ecuaciones normales.

📘 **Dónde se aprende** (1 clase): [B48-C22 · Control automático del enfocador y autoenfoque](../programa/clases/B48/B48-C22-control-automatico-del-enfocador-y-autoenfoque/CLASE.md).

### Curva L

- La curva L es la gráfica, en escala log–log, de la norma de la solución frente a la norma del residuo al variar `λ` (S2).

💡 **Cómo se explica en la clase [B22-C02](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md):**
- La curva tiene forma de «L» (S2): con `λ` muy pequeño la norma de la solución explota y el residuo ya casi no baja (rama vertical); con `λ` muy grande el residuo crece y la solución casi no cambia (rama horizontal).
- El vértice de la L es un compromiso: se localiza donde la curvatura de la curva log–log es máxima.
- 🎯 **Por qué importa:** Si no puedes confiar en `x = A⁻¹ b` y no puedes bajar el ruido a voluntad, necesitas una regla que ignore lo que los datos no pueden decir. Esa regla debe tener una perilla: cuánto ignorar.
- 🔗 **Se estudia junto con:** solución regularizada, desajuste, penalización, parámetro de regularización.

📘 **Dónde se aprende** (1 clase): [B22-C02 · Regularización de Tikhonov](../programa/clases/B22/B22-C02-regularizacion-de-tikhonov/CLASE.md).

### Curva NC

- La curva NC es un límite por bandas de octava.

💡 **Cómo se explica en la clase [B109-C10](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md):**
- El resumen técnico OCHMO-TB-035 de NASA (Rev C, 2023) indica que NASA-STD-3001 Vol. 2 limita el ruido peligroso a menos de `85 dBA` sin importar la duración y el ruido continuo de las áreas de trabajo a la curva NC-50.
- Ejercicio 11 · transferencia. Transferencia. ¿Cumple esta cabina la curva NC-50?
- 🎯 **Por qué importa:** El ruido continuo degrada la comunicación, el sueño y el trabajo aunque no dañe el oído. La decisión central: ¿qué fuente reduzco primero y cuánto baja el nivel de la cabina?
- 🔗 **Se estudia junto con:** nivel de potencia sonora, nivel de presión, campo directo, reverberante.

📘 **Dónde se aprende** (1 clase): [B109-C10 · Acústica y control de ruido interior](../programa/clases/B109/B109-C10-acustica-y-control-de-ruido-interior/CLASE.md).

### Curva plana

- La curva plana es la velocidad de rotación constante a gran radio.

💡 **Cómo se explica en la clase [B36-C11](../programa/clases/B36/B36-C11-gravedad-modificada-mond-y-relativistas-frente-a-materia-oscura/CLASE.md):**
- Para una galaxia de `5×10¹⁰ M☉` y escala de `3 kpc` (ilustrativa), la curva MOND llega a `191,3 km/s` a 10 kpc frente a `134,8` newtoniana, un halo NFW la reproduce con una desviación de `1,55 km/s`, y la velocidad plana `168,62` coincide con `(G M a₀)^(1/4) = 167,98 km/s` al `0,4 %`.
- Descripción larga: la curva MOND es plana a 180 a 190 km/s y el NFW la reproduce.
- 🎯 **Por qué importa:** Una alternativa debe confrontarse con todas las pruebas. La decisión central: ¿qué observación separa la materia oscura de la gravedad modificada?
- 🔗 **Se estudia junto con:** aceleración de Milgrom, función de interpolación, aceleración newtoniana, relación de Tully–Fisher bariónica.

📘 **Dónde se aprende** (1 clase): [B36-C11 · Gravedad modificada (MOND y relativistas) frente a materia oscura](../programa/clases/B36/B36-C11-gravedad-modificada-mond-y-relativistas-frente-a-materia-oscura/CLASE.md).

### Curva ROC

- La curva ROC grafica exhaustividad contra tasa de falsos positivos al variar el umbral; su área es el AUC.
- La curva ROC es POD frente a la tasa de falsas alarmas.
- La curva ROC grafica la fracción de anomalías detectadas contra la de falsas alarmas al variar el umbral; su área (AUC) vale 1 si el método separa perfectamente y 0,5 si no distingue (S2).

💡 **Cómo se explica en la clase [B17-C05](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md):**
- Comparar métodos con el área bajo la curva ROC.
- 🎯 **Por qué importa:** El subsistema térmico de un satélite entrega temperatura y corriente. Cada una, por separado, puede estar dentro de su rango normal y sin embargo la pareja ser imposible: la corriente alta con temperatura baja no ocurre nunca en operación sana.
- 🔗 **Se estudia junto con:** anomalía, distancia de Mahalanobis, distribución chi-cuadrado, bosque de aislamiento.

📘 **Dónde se aprende** (3 clases): [B17-C05 · Detección de anomalías](../programa/clases/B17/B17-C05-deteccion-de-anomalias/CLASE.md); [B17-C12 · Evaluación de modelos: precisión, exhaustividad y falsos positivos](../programa/clases/B17/B17-C12-evaluacion-de-modelos-precision-exhaustividad-y-falsos-positivos/CLASE.md); [B33-C14 · Verificación de alertas con tablas de contingencia](../programa/clases/B33/B33-C14-verificacion-de-alertas-con-tablas-de-contingencia/CLASE.md).

### Curvas de equilibrio

- Las curvas de equilibrio separan regiones: fusión (sólido–líquido), vaporización (líquido–gas) y sublimación (sólido–gas).

💡 **Cómo se explica en la clase [B06-C11](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md):**
- Las fronteras son las curvas de equilibrio.
- 🎯 **Por qué importa:** La temperatura de ebullición del agua no es una constante de la naturaleza: depende de la presión. En lo alto de una montaña hierve a menos de 100 °C; en Marte, con 6 mb, el agua apenas puede ser líquida; en Venus, a 92 bar y 737 K, el CO₂ no es ni líquido ni gas.
- 🔗 **Se estudia junto con:** diagrama de fases, fusión, vaporización, sublimación.

📘 **Dónde se aprende** (1 clase): [B06-C11 · Diagramas de fase](../programa/clases/B06/B06-C11-diagramas-de-fase/CLASE.md).

### Curvatura escalar

- La curvatura escalar es `R = g^bd R_bd`.

💡 **Cómo se explica en la clase [B39-C03](../programa/clases/B39/B39-C03-tensor-de-riemann-ricci-y-curvatura-escalar/CLASE.md):**
- La curvatura escalar numérica es `0,50000006` frente a `2/a² = 0,50000000`.
- Descripción larga: la esfera tiene la curvatura escalar esperada y Schwarzschild es vacío con Kretschmann no nulo.
- 🎯 **Por qué importa:** Un espacio-tiempo es curvo si el Riemann no se anula. La decisión central: ¿qué mide cada contracción del Riemann y cómo se comprueba un cálculo de curvatura?
- 🔗 **Se estudia junto con:** tensor de Riemann, tensor de Ricci, escalar de Kretschmann, plano.

📘 **Dónde se aprende** (1 clase): [B39-C03 · Tensor de Riemann, Ricci y curvatura escalar](../programa/clases/B39/B39-C03-tensor-de-riemann-ricci-y-curvatura-escalar/CLASE.md).

### Curvatura extrínseca

- La curvatura extrínseca `K_ij` mide cómo se curva la capa en el espacio-tiempo.

💡 **Cómo se explica en la clase [B39-C06](../programa/clases/B39/B39-C06-introduccion-a-la-relatividad-numerica-formalismo-3-1/CLASE.md):**
- La rebanada de Painlevé–Gullstrand es plana pero tiene curvatura extrínseca no nula: `K² = K_ij K^ij` hace que la ligadura de vacío se cumpla.
- 🎯 **Por qué importa:** Una simulación necesita un tiempo y un espacio. La decisión central: ¿cómo se separa el espacio-tiempo en capas y cómo se sabe que una evolución converge?
- 🔗 **Se estudia junto con:** lapso, desplazamiento, métrica espacial, ligadura hamiltoniana.

📘 **Dónde se aprende** (1 clase): [B39-C06 · Introducción a la relatividad numérica: formalismo 3+1](../programa/clases/B39/B39-C06-introduccion-a-la-relatividad-numerica-formalismo-3-1/CLASE.md).

### Curvatura gaussiana

- La curvatura gaussiana `K` de una superficie es `1/R²` para una esfera de radio `R`.

💡 **Contexto en la clase [B26-C07](../programa/clases/B26/B26-C07-curvatura-y-metricas/CLASE.md):**
- **Idea central (modelo mental):** En una hoja de goma horizontal, la distancia en línea recta entre dos puntos es la de la regla. Si apoyas una bola pesada, la hoja se hunde y la distancia sobre la superficie entre dos puntos cercanos a la bola es mayor que la proyectada en el plano.
- 🎯 **Por qué importa:** Medir una distancia cerca de una masa grande no da lo mismo que en el espacio plano: el radio de un círculo y su circunferencia dejan de cumplir `C = 2πR`. Los GPS, las lentes gravitacionales y los agujeros negros dependen de esa diferencia.
- 🔗 **Se estudia junto con:** métrica, distancia propia, exceso angular, métrica de Schwarzschild.

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
- 🔗 **Se estudia junto con:** Anomalía, Límite fijo, Puntuación robusta, Falsa alarma.

📘 **Dónde se aprende** (5 clases): [B96-C13 · Detección de anomalías](../programa/clases/B96/B96-C13-deteccion-de-anomalias/CLASE.md); [B97-C22 · Detección autónoma de eventos científicos](../programa/clases/B97/B97-C22-deteccion-autonoma-de-eventos-cientificos/CLASE.md); [B104-C18 · Aislamiento y convivencia](../programa/clases/B104/B104-C18-aislamiento-y-convivencia/CLASE.md); [B105-C09 · Salud mental en aislamiento](../programa/clases/B105/B105-C09-salud-mental-en-aislamiento/CLASE.md); [B107-C10 · Indicadores de rehabilitación y seguimiento](../programa/clases/B107/B107-C10-indicadores-de-rehabilitacion-y-seguimiento/CLASE.md).

### CVCM

- RML `= TML − WVR`; CVCM (*collected volatile condensable material*) es la masa condensada en el colector, en % de la masa inicial.
- TML: pérdida total de masa, `100 (mᵢ − m_f)/mᵢ`. CVCM: volátiles condensables recogidos, `100 m_col/mᵢ`.

💡 **Cómo se explica en la clase [B84-C07](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md):**
- Con `m_i = 500 mg`: `TML = (m_i − m_f)/m_i`, `WVR = (m_h − m_f)/m_i`, `RML = TML − WVR`, `CVCM = Δm_colector/m_i`.
- La silicona B pasa en `TML` y falla en `CVCM`: por eso se exigen ambos criterios.
- 🎯 **Por qué importa:** Una película de 10 nm sobre un espejo de telescopio o un sensor estelar degrada la misión; el cribado de desgasificación se hace antes de elegir el adhesivo. La decisión central: ¿pasa un material el cribado de desgasificación y cuántos días de bakeout necesita para limpiarlo?
- 🔗 **Se estudia junto con:** TML, WVR, RML, bakeout.

📘 **Dónde se aprende** (2 clases): [B84-C07 · Desgasificación de materiales](../programa/clases/B84/B84-C07-desgasificacion-de-materiales/CLASE.md); [B90-C04 · Control de contaminación](../programa/clases/B90/B90-C04-control-de-contaminacion/CLASE.md).
